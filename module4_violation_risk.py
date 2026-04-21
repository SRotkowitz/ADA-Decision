"""
ADA Decision Engine — Module 4: Violation Risk
Rule range: R068–R110
Legal source: 42 U.S.C. §§ 12112, 12113, 12203;
              29 CFR § 1630.9; module_interface_spec.json design decisions DD-3, DD-4, DD-5.

Implements five components:
  4.1 Failure to Accommodate
  4.2 Disability Discrimination (McDonnell Douglas)
  4.3 Harassment
  4.4 Retaliation
  4.5 Overall Violation Risk (composite, tiebreak order: FTA → DD → harassment → retaliation)
"""

from schemas.input_models import Module4Input
from schemas.output_models import (
    Module1Output,
    Module2Output,
    Module3Output,
    WrapperOutput,
    FailureToAccommodateOutput,
    DisabilityDiscriminationOutput,
    HarassmentOutput,
    RetaliationOutput,
    OverallViolationRiskOutput,
    Module4Output,
)

# Risk level ordinal mapping for comparison
_RISK_ORDER = {"minimal": 0, "low": 1, "moderate": 2, "high": 3, "critical": 4}
_RISK_LABELS = ["minimal", "low", "moderate", "high", "critical"]

# Tiebreak priority order (lower index = higher priority): DD-3
_TIEBREAK_ORDER = [
    "failure_to_accommodate",
    "disability_discrimination",
    "harassment",
    "retaliation",
]


def _shift_down(risk: str) -> str:
    """Shift a risk level one tier downward (floor = minimal). Used for employee non-participation. DD-4."""
    idx = _RISK_ORDER.get(risk, 0)
    return _RISK_LABELS[max(0, idx - 1)]


# ---------------------------------------------------------------------------
# Component 4.1 — Failure to Accommodate
# ---------------------------------------------------------------------------

def assess_failure_to_accommodate(
    inp: Module4Input,
    m1_out: Module1Output,
    m2_out: Module2Output,
    m3_out: Module3Output,
    wrapper_out: WrapperOutput,
) -> FailureToAccommodateOutput:
    """Assess failure-to-accommodate violation risk.

    Five prima facie elements (each boolean):
      1. is_covered_employer
      2. has_qualifying_disability == 'yes' (not indeterminate)
      3. is_qualified_individual (resolved wrapper composite)
      4. accommodation_request_valid
      5. accommodation_required == 'yes' (not indeterminate)

    Risk derivation with interactive process compliance modifier.
    Employee non-participation shifts one tier downward (DD-4, not floor-to-minimal).
    Interaction with indeterminate process compliance: treated as genuinely uncertain (DD-5).

    Citation: 42 U.S.C. § 12112(b)(5)(A); 29 CFR § 1630.9.
    """
    ec = m1_out.employer_coverage.is_covered_employer
    hqd = m1_out.disability_determination.has_qualifying_disability  # must be 'yes'
    qi = wrapper_out.is_qualified_individual
    arv = m2_out.accommodation_request.accommodation_request_valid
    acc_req = m2_out.accommodation_determination.accommodation_required  # must be 'yes'
    denial_basis = m2_out.accommodation_determination.denial_basis
    ip_compliant = m3_out.interactive_process.interactive_process_compliant

    # Build prima facie element map
    # R068: Element 2 requires has_qualifying_disability == 'yes' (not indeterminate)
    # R069: Element 3 uses resolved wrapper composite
    # R070: Element 5 requires accommodation_required == 'yes' (not indeterminate)
    elements = {
        "is_covered_employer": ec,
        "has_qualifying_disability_yes": hqd == "yes",
        "is_qualified_individual": qi == "yes",
        "accommodation_request_valid": arv,
        "accommodation_required_yes": acc_req == "yes",
    }
    count = sum(1 for v in elements.values() if v)

    # R071: Documented legitimate denial (complete affirmative defense)
    documented_legitimate_denial = denial_basis in ("undue_hardship", "direct_threat")

    # R072–R077: Risk derivation
    if count >= 5:
        # R072: 5 elements + non-compliant process + no legitimate denial → critical
        if ip_compliant == "no" and not documented_legitimate_denial:
            risk = "critical"
            rationale = "R072: All 5 prima facie elements met + non-compliant interactive process + no legitimate denial basis → critical"
        # R073: 5 elements + indeterminate process + no legitimate denial → high
        elif ip_compliant == "indeterminate" and not documented_legitimate_denial:
            risk = "high"
            rationale = "R073: All 5 prima facie elements met + indeterminate interactive process + no legitimate denial basis → high (DD-5: indeterminate treated as genuinely uncertain)"
        # R074: 5 elements + compliant process + no legitimate denial → high
        elif ip_compliant == "yes" and not documented_legitimate_denial:
            risk = "high"
            rationale = "R074: All 5 prima facie elements met + compliant interactive process + no legitimate denial basis → high"
        # R075: 5 elements + documented legitimate denial → low
        elif documented_legitimate_denial:
            risk = "low"
            rationale = "R075: All 5 prima facie elements met + documented legitimate denial (undue hardship or direct threat) → low"
        else:
            risk = "high"
            rationale = "R076: All 5 prima facie elements met, process compliance unknown → high"
    elif count == 4:
        # R077: 4 elements → moderate
        risk = "moderate"
        rationale = "R077: 4 of 5 prima facie elements met → moderate"
    elif count == 3:
        # R078: 3 elements → low
        risk = "low"
        rationale = "R078: 3 of 5 prima facie elements met → low"
    else:
        # R079: < 3 elements → minimal
        risk = "minimal"
        rationale = f"R079: {count} of 5 prima facie elements met (< 3) → minimal"

    # R080: Employee non-participation shift — one tier downward only (DD-4)
    participation = getattr(inp, "employee_interactive_process_participation", "good_faith")
    participation_documented = getattr(inp, "employee_nonparticipation_documented", False)
    if participation in ("refused", "abandoned") and participation_documented:
        original = risk
        risk = _shift_down(risk)
        if risk != original:
            rationale += f" | R080: Employee {participation} (documented) — risk shifted one tier downward from {original} to {risk} (DD-4)"

    return FailureToAccommodateOutput(
        elements_met=count,
        prima_facie_elements=elements,
        documented_legitimate_denial=documented_legitimate_denial,
        risk_level=risk,
        risk_rationale=rationale,
    )


# ---------------------------------------------------------------------------
# Component 4.2 — Disability Discrimination
# ---------------------------------------------------------------------------

def assess_disability_discrimination(
    inp: Module4Input,
    m1_out: Module1Output,
    wrapper_out: WrapperOutput,
) -> DisabilityDiscriminationOutput:
    """Assess disability discrimination violation risk using the McDonnell Douglas framework.

    Four elements:
      1. is_covered_individual_with_disability
      2. is_qualified_individual
      3. adverse_action_taken
      4. causal_nexus_present

    Citation: 42 U.S.C. § 12112(a); McDonnell Douglas Corp. v. Green, 411 U.S. 792 (1973).
    """
    is_cov_individual = m1_out.individual_status.is_covered_individual
    has_disability = m1_out.disability_determination.has_qualifying_disability == "yes"
    qi = wrapper_out.is_qualified_individual == "yes"
    adverse = inp.adverse_action_taken
    causal = getattr(inp, "causal_nexus_present", None)
    causal_met = causal == "yes"
    evidence_type = getattr(inp, "evidence_type", "none")
    adverse_reason = getattr(inp, "adverse_action_reason_documented", None)

    # Element 1: covered individual with disability
    el1 = is_cov_individual and has_disability
    elements = {
        "is_covered_individual_with_disability": el1,
        "is_qualified_individual": qi,
        "adverse_action_taken": adverse,
        "causal_nexus_present": causal_met,
    }
    count = sum(1 for v in elements.values() if v)

    # R081–R086: Risk derivation
    if count >= 4:
        # R081: 4 elements + direct evidence → critical
        if evidence_type == "direct":
            risk = "critical"
            rationale = "R081: All 4 McDonnell Douglas elements + direct evidence of discrimination → critical"
        # R082: 4 elements + circumstantial evidence → high
        elif evidence_type == "circumstantial":
            risk = "high"
            rationale = "R082: All 4 McDonnell Douglas elements + circumstantial evidence → high"
        # R083: 4 elements + documented legitimate reason → moderate
        elif adverse_reason and adverse_reason != "undocumented" and adverse_reason != "accommodation_denial_basis":
            risk = "moderate"
            rationale = f"R083: All 4 elements + documented legitimate non-discriminatory reason ({adverse_reason}) → moderate"
        else:
            risk = "high"
            rationale = "R084: All 4 elements, no strong evidence classification → high (default)"
    elif count == 3:
        # R085: 3 elements → moderate
        risk = "moderate"
        rationale = "R085: 3 of 4 McDonnell Douglas elements met → moderate"
    elif count == 2:
        # R086: 2 elements → low
        risk = "low"
        rationale = "R086: 2 of 4 McDonnell Douglas elements met → low"
    else:
        # R087: < 2 elements → minimal
        risk = "minimal"
        rationale = f"R087: {count} of 4 elements met (< 2) → minimal"

    return DisabilityDiscriminationOutput(
        elements_met=count,
        prima_facie_elements=elements,
        risk_level=risk,
        risk_rationale=rationale,
    )


# ---------------------------------------------------------------------------
# Component 4.3 — Harassment
# ---------------------------------------------------------------------------

def assess_harassment(
    inp: Module4Input,
    m1_out: Module1Output,
) -> HarassmentOutput:
    """Assess disability-based harassment violation risk.

    Four elements:
      1. individual_in_protected_class
      2. unwelcome_conduct_occurred
      3. conduct_severity (isolated_minor / repeated_minor / isolated_severe / repeated_severe)
      4. employer_knew_or_should_have_known

    Note: input schema uses 'pervasive' for repeated_severe; mapped accordingly.
    Citation: 42 U.S.C. § 12112(a); EEOC harassment guidance.
    """
    # Element 1: individual in protected class = has qualifying disability or covered by regarded-as
    has_disability = m1_out.disability_determination.has_qualifying_disability == "yes"
    is_individual = m1_out.individual_status.is_covered_individual
    el1 = has_disability and is_individual

    # Element 2: unwelcome conduct occurred
    el2 = getattr(inp, "harassment_conduct_occurred", False)

    # Element 3: conduct severity
    severity_raw = getattr(inp, "harassment_severity", None)
    el3 = el2 and severity_raw is not None

    # Element 4: employer knew or should have known
    reported = getattr(inp, "harassment_reported_to_employer", None)
    remedial = getattr(inp, "employer_remedial_action_taken", None)
    # Employer knew/should have known if reported OR employer failed to act
    el4 = bool(reported) or (el2 and reported is None)  # absence of reporting data treated as unknown (element not confirmed)
    el4 = bool(reported)  # strict: known if reported

    elements = {
        "individual_in_protected_class": el1,
        "unwelcome_conduct_occurred": el2,
        "conduct_severity_established": el3,
        "employer_knew_or_should_have_known": el4,
    }
    count = sum(1 for v in elements.values() if v)

    # R088–R093: Risk derivation based on severity when all 4 elements met
    if count >= 4:
        # Map pervasive → repeated_severe for risk evaluation
        severity_mapped = severity_raw
        if severity_raw == "pervasive":
            severity_mapped = "repeated_severe"

        # R088: 4 elements + repeated_severe → critical
        if severity_mapped == "repeated_severe":
            risk = "critical"
            rationale = "R088: All 4 harassment elements + repeated/severe conduct → critical"
        # R089: 4 elements + isolated_severe → high
        elif severity_mapped == "isolated_severe":
            risk = "high"
            rationale = "R089: All 4 harassment elements + isolated severe conduct → high"
        # R090: 4 elements + repeated_minor → moderate
        elif severity_mapped == "repeated_minor":
            risk = "moderate"
            rationale = "R090: All 4 harassment elements + repeated minor conduct → moderate"
        # R091: 4 elements + isolated_minor → low
        elif severity_mapped == "isolated_minor":
            risk = "low"
            rationale = "R091: All 4 harassment elements + isolated minor conduct → low"
        else:
            risk = "moderate"
            rationale = "R092: All 4 harassment elements, severity unclassified → moderate (default)"
    else:
        # R093: < 4 elements → minimal
        risk = "minimal"
        rationale = f"R093: {count} of 4 harassment elements met (< 4) → minimal"

    return HarassmentOutput(
        elements_met=count,
        prima_facie_elements=elements,
        risk_level=risk,
        risk_rationale=rationale,
    )


# ---------------------------------------------------------------------------
# Component 4.4 — Retaliation
# ---------------------------------------------------------------------------

def assess_retaliation(inp: Module4Input) -> RetaliationOutput:
    """Assess retaliation violation risk.

    Four elements:
      1. engaged_in_protected_activity
      2. employer_aware_of_activity
      3. adverse_action_taken
      4. causal_nexus_present

    Temporal proximity (engine heuristic, not statutory):
      ≤ 30 days → strong
      31–90 days → moderate
      91–180 days → weak
      > 180 days → minimal
      Not provided → default to 'high' risk (absence of data does not reduce risk)

    Citation: 42 U.S.C. § 12203.
    """
    el1 = getattr(inp, "engaged_in_protected_activity", False)
    el2 = getattr(inp, "employer_aware_of_activity", None)
    el2_met = bool(el2)
    el3 = getattr(inp, "adverse_action_taken", False)
    causal = getattr(inp, "causal_nexus_present", None)
    el4 = causal == "yes"

    elements = {
        "engaged_in_protected_activity": el1,
        "employer_aware_of_activity": el2_met,
        "adverse_action_taken": el3,
        "causal_nexus_present": el4,
    }
    count = sum(1 for v in elements.values() if v)

    # R094: Temporal proximity derivation
    days = getattr(inp, "days_between_activity_and_action", None)
    if days is None:
        proximity = "not_provided"
    elif days <= 30:
        proximity = "strong"
    elif days <= 90:
        proximity = "moderate"
    elif days <= 180:
        proximity = "weak"
    else:
        proximity = "minimal"

    # R095–R103: Risk derivation
    if count >= 4:
        # R095: 4 elements + strong temporal proximity → critical
        if proximity == "strong":
            risk = "critical"
            rationale = "R095: All 4 retaliation elements + strong temporal proximity (≤30 days) → critical"
        # R096: 4 elements + moderate temporal proximity → high
        elif proximity == "moderate":
            risk = "high"
            rationale = "R096: All 4 retaliation elements + moderate temporal proximity (31–90 days) → high"
        # R097: 4 elements + weak temporal proximity → moderate
        elif proximity == "weak":
            risk = "moderate"
            rationale = "R097: All 4 retaliation elements + weak temporal proximity (91–180 days) → moderate"
        # R098: 4 elements + minimal temporal proximity → low
        elif proximity == "minimal":
            risk = "low"
            rationale = "R098: All 4 retaliation elements + minimal temporal proximity (>180 days) → low"
        # R099: 4 elements + not_provided → high (absence of data does not reduce risk)
        elif proximity == "not_provided":
            risk = "high"
            rationale = "R099: All 4 retaliation elements + temporal proximity not provided — absence of data does not reduce risk → high"
        else:
            risk = "high"
            rationale = "R100: All 4 retaliation elements, proximity unclassified → high"
    elif count == 3:
        # R101: 3 elements → low
        risk = "low"
        rationale = "R101: 3 of 4 retaliation elements met → low"
    else:
        # R102: < 3 elements → minimal
        risk = "minimal"
        rationale = f"R102: {count} of 4 retaliation elements met (< 3) → minimal"

    return RetaliationOutput(
        elements_met=count,
        prima_facie_elements=elements,
        proximity_strength=proximity,
        risk_level=risk,
        risk_rationale=rationale,
    )


# ---------------------------------------------------------------------------
# Component 4.5 — Overall Violation Risk
# ---------------------------------------------------------------------------

def assess_overall_violation_risk(
    fta: FailureToAccommodateOutput,
    dd: DisabilityDiscriminationOutput,
    har: HarassmentOutput,
    ret: RetaliationOutput,
) -> OverallViolationRiskOutput:
    """Compute overall violation risk as maximum across all four claim types.

    Tiebreak order (DD-3): failure_to_accommodate → disability_discrimination → harassment → retaliation
    primary_claim_basis: tiebreak winner
    contributing_claims: all components tied at maximum

    Citation: module_interface_spec.json design decision DD-3.
    """
    component_risks = {
        "failure_to_accommodate": fta.risk_level,
        "disability_discrimination": dd.risk_level,
        "harassment": har.risk_level,
        "retaliation": ret.risk_level,
    }

    # R103: Find maximum risk level
    max_score = max(_RISK_ORDER[v] for v in component_risks.values())
    max_level = _RISK_LABELS[max_score]

    # R104: All components at max level
    tied = [c for c in component_risks if _RISK_ORDER[component_risks[c]] == max_score]

    # R105: Tiebreak order (DD-3): FTA → DD → harassment → retaliation
    primary = None
    for candidate in _TIEBREAK_ORDER:
        if candidate in tied:
            primary = candidate
            break
    if primary is None:
        primary = tied[0]

    # R106: Build recommended actions based on overall risk and primary claim
    recommended_actions = _build_recommended_actions(max_level, primary, component_risks)

    return OverallViolationRiskOutput(
        overall_risk_level=max_level,
        primary_claim_basis=primary,
        contributing_claims=sorted(tied),
        component_risk_levels=component_risks,
        recommended_actions=recommended_actions,
    )


def _build_recommended_actions(
    risk_level: str,
    primary_claim: str,
    component_risks: dict,
) -> list:
    """Generate plain-language recommended actions based on overall risk level and primary claim.

    Citation: R106 — derived from overall risk level and primary claim basis.
    """
    actions = []

    if risk_level == "minimal":
        actions.append("No immediate action required. Maintain current ADA compliance practices.")
        return sorted(actions)

    if risk_level in ("low", "moderate"):
        actions.append("Conduct internal ADA compliance review for the situation described.")

    if risk_level in ("high", "critical"):
        actions.append("Consult employment counsel immediately regarding ADA compliance obligations.")
        actions.append("Preserve all documentation related to the accommodation request and interactive process.")

    # Claim-specific recommendations
    if primary_claim == "failure_to_accommodate" or component_risks.get("failure_to_accommodate") not in ("minimal", "low"):
        actions.append("Document all steps taken in the interactive process and rationale for any denial.")
        actions.append("Consider whether an effective reasonable accommodation remains available.")

    if primary_claim == "disability_discrimination" or component_risks.get("disability_discrimination") not in ("minimal", "low"):
        actions.append("Review the adverse action for any disability-related nexus and document a legitimate non-discriminatory reason.")

    if primary_claim == "harassment" or component_risks.get("harassment") not in ("minimal", "low"):
        actions.append("Investigate harassment complaint promptly and take documented remedial action.")
        actions.append("Review and reinforce anti-harassment policies and training.")

    if primary_claim == "retaliation" or component_risks.get("retaliation") not in ("minimal", "low"):
        actions.append("Ensure no adverse actions are taken against employees who have engaged in protected ADA activity.")

    if risk_level == "critical":
        actions.append("Consider proactive remediation before any EEOC charge is filed.")

    return sorted(actions)


# ---------------------------------------------------------------------------
# Module 4 orchestrator
# ---------------------------------------------------------------------------

def run_module4(
    inp: Module4Input,
    m1_out: Module1Output,
    m2_out: Module2Output,
    m3_out: Module3Output,
    wrapper_out: WrapperOutput,
) -> Module4Output:
    """Execute all five Module 4 components and return the full module output.

    Citation: 42 U.S.C. §§ 12112, 12113, 12203.
    """
    fta = assess_failure_to_accommodate(inp, m1_out, m2_out, m3_out, wrapper_out)
    dd = assess_disability_discrimination(inp, m1_out, wrapper_out)
    har = assess_harassment(inp, m1_out)
    ret = assess_retaliation(inp)
    overall = assess_overall_violation_risk(fta, dd, har, ret)

    return Module4Output(
        failure_to_accommodate=fta,
        disability_discrimination=dd,
        harassment=har,
        retaliation=ret,
        overall_violation_risk=overall,
    )
