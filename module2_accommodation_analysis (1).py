"""
ADA Decision Engine — Module 2: Accommodation Analysis
Rule range: R026–R046
Legal source: 42 U.S.C. §§ 12111(10), 12112(b)(5)(A), 12113(b);
              29 CFR § 1630.2(p),(r); 29 CFR § 1630.9;
              EEOC Enforcement Guidance No. 915.002.

Implements four components:
  2.1 Accommodation Request (rule-based)
  2.2 Undue Hardship Analysis (standards-based)
  2.3 Direct Threat Analysis (standards-based)
  2.4 Accommodation Determination (composite, short-circuit)

PATCH APPLIED (Phase 8 — SC5 removal):
  SC5 (preliminary_qualified_without_accommodation = no → not_qualified) has been
  removed from the short-circuit chain. The not_qualified determination is now owned
  by the wrapper (WR-3b). This makes WR-2 structurally reachable: when preliminary=no,
  accommodation analysis now runs to completion, and if accommodation_required=yes and
  accommodation_theoretically_effective=yes, WR-2 fires and is_qualified_individual=yes.

  Renumbering after SC5 removal:
    Old SC1–SC4  → New SC1–SC4 (unchanged)
    Old SC6      → New SC5  (accommodation_request_valid = false)
    Old SC7      → New SC6  (undue_hardship_applies = yes)
    Old SC8      → New SC7  (direct_threat_exists = yes)
    Old SC9      → New SC8  (all pass → accommodation_required = yes)
    Old SC10     → New SC9  (indeterminate catch-all)
"""

from schemas.input_models import Module2Input
from schemas.output_models import (
    AccommodationRequestOutput,
    UndueHardshipOutput,
    DirectThreatOutput,
    AccommodationDeterminationOutput,
    Module1Output,
    Module2Output,
)


def _sort(arr: list) -> list:
    """Sort a factor/uncertainty array alphabetically for determinism."""
    return sorted(arr)


# ---------------------------------------------------------------------------
# Component 2.1 — Accommodation Request
# ---------------------------------------------------------------------------

def assess_accommodation_request(inp: Module2Input) -> AccommodationRequestOutput:
    """Determine whether a valid accommodation request has been made.

    Rule-based. Valid if: (1) identifies a functional limitation, (2) made by an
    authorized party (employee, family member, healthcare provider, or representative),
    (3) for a qualifying purpose.

    Citation: EEOC Enforcement Guidance No. 915.002.
    """
    # R026: All three validity elements must be present
    authorized_parties = {"employee", "family_member", "healthcare_provider", "representative"}
    valid = (
        inp.functional_limitation_identified
        and inp.requesting_party in authorized_parties
        and inp.qualifying_purpose
    )
    return AccommodationRequestOutput(accommodation_request_valid=valid)


# ---------------------------------------------------------------------------
# Component 2.2 — Undue Hardship Analysis
# ---------------------------------------------------------------------------

def assess_undue_hardship(inp: Module2Input) -> UndueHardshipOutput:
    """Evaluate whether providing the accommodation would impose an undue hardship.

    Standards-based. Evaluates 29 CFR § 1630.2(p)(2) factors. Engine-defined
    cost-burden ratio thresholds applied as heuristics (not statutory).
    Employer bears burden of proof — undocumented hardship defense weighs against defense.

    Cost-burden thresholds:
      < 50 employees: ratio > 0.03 → factor FOR hardship
      50–500 employees: ratio > 0.07 → factor FOR hardship
      > 500 employees: ratio > 0.15 → factor FOR hardship
      All sizes: ratio < 0.01 → factor AGAINST hardship

    Citation: 42 U.S.C. § 12111(10); 29 CFR § 1630.2(p).
    """
    factors_for: list = []
    factors_against: list = []
    key_uncertainties: list = []

    cost = getattr(inp, "accommodation_estimated_cost", None)
    budget = getattr(inp, "employer_annual_operating_budget", None)
    financial_resources_adequate = getattr(inp, "employer_financial_resources_adequate", None)
    other_resources = getattr(inp, "other_resources_available", None)
    fundamentally_alters = getattr(inp, "accommodation_fundamentally_alters_operations", None)
    undocumented_defense = getattr(inp, "undocumented_hardship_defense", False)

    # R027: Cost-burden ratio analysis
    if cost is not None and budget is not None and budget > 0:
        ratio = cost / budget
        size = inp.total_employees

        # R028: Ratio < 0.01 → factor AGAINST hardship (all sizes)
        if ratio < 0.01:
            factors_against.append(
                f"Accommodation cost-to-budget ratio ({ratio:.4f}) is below 0.01 — cost burden is minimal"
            )
        # R029: Size-based upper thresholds
        elif size < 50 and ratio > 0.03:
            factors_for.append(
                f"Cost-to-budget ratio ({ratio:.4f}) exceeds 0.03 threshold for employers with fewer than 50 employees"
            )
        elif 50 <= size <= 500 and ratio > 0.07:
            factors_for.append(
                f"Cost-to-budget ratio ({ratio:.4f}) exceeds 0.07 threshold for employers with 50–500 employees"
            )
        elif size > 500 and ratio > 0.15:
            factors_for.append(
                f"Cost-to-budget ratio ({ratio:.4f}) exceeds 0.15 threshold for employers with more than 500 employees"
            )
        else:
            factors_against.append(
                f"Cost-to-budget ratio ({ratio:.4f}) does not exceed applicable size-based hardship threshold"
            )
    elif cost is not None or budget is not None:
        key_uncertainties.append(
            "Facility operating budget not provided — cost burden ratio cannot be calculated"
        )

    # R030: Financial resources factor
    if financial_resources_adequate is False:
        factors_for.append(
            "Employer's financial resources are inadequate to absorb accommodation cost (29 CFR § 1630.2(p)(2)(ii))"
        )
    elif financial_resources_adequate is True:
        factors_against.append(
            "Employer's overall financial resources are adequate (29 CFR § 1630.2(p)(2)(ii))"
        )
    else:
        key_uncertainties.append(
            "Employer financial resource adequacy not provided"
        )

    # R031: Other funding sources
    if other_resources is True:
        factors_against.append(
            "Other funding sources (tax credits, insurance, grants) are available to offset cost"
        )

    # R032: Fundamental alteration
    if fundamentally_alters is True:
        factors_for.append(
            "Accommodation would fundamentally alter the nature or operation of the business (29 CFR § 1630.2(p)(2)(v))"
        )
    elif fundamentally_alters is False:
        factors_against.append(
            "Accommodation would not fundamentally alter the nature or operation of the business"
        )

    # R033: Undocumented hardship defense weighs against the defense
    if undocumented_defense:
        factors_against.append(
            "Employer has not documented the basis for hardship claim — undocumented defense weighs against employer"
        )

    # R034: Undue hardship determination
    if factors_for and not factors_against and not key_uncertainties:
        result = "yes"
    elif factors_against and not factors_for and not key_uncertainties:
        result = "no"
    elif not factors_for and not factors_against:
        result = "indeterminate"
    elif factors_for and not factors_against:
        result = "yes"
    elif factors_against and not factors_for:
        result = "no"
    else:
        result = "indeterminate"

    return UndueHardshipOutput(
        undue_hardship_applies=result,
        factors_for=_sort(factors_for),
        factors_against=_sort(factors_against),
        key_uncertainties=_sort(key_uncertainties),
    )


# ---------------------------------------------------------------------------
# Component 2.3 — Direct Threat Analysis
# ---------------------------------------------------------------------------

def assess_direct_threat(inp: Module2Input) -> DirectThreatOutput:
    """Evaluate whether the individual poses a direct threat to health or safety.

    Standards-based. All four § 1630.2(r) factors required: nature of risk,
    duration, severity, probability. Individualized assessment required —
    stereotype-based assessment is automatic procedural defeater producing
    direct_threat_exists = no.

    Citation: 42 U.S.C. § 12113(b); 29 CFR § 1630.2(r).
    """
    factors_for: list = []
    factors_against: list = []
    key_uncertainties: list = []

    risk_assessed = getattr(inp, "direct_threat_risk_assessed", None)
    risk_nature = getattr(inp, "risk_nature_documented", None)
    risk_duration = getattr(inp, "risk_duration_documented", None)
    risk_severity = getattr(inp, "risk_severity_documented", None)
    risk_probability = getattr(inp, "risk_probability_documented", None)
    individualized = getattr(inp, "individualized_assessment_conducted", None)
    stereotype_based = getattr(inp, "stereotype_based_assessment", False)

    # R035: Stereotype-based assessment is automatic defeater — direct_threat_exists = no
    if stereotype_based:
        factors_against.append(
            "Assessment was based on stereotypes rather than individualized evaluation — "
            "automatic defeater under 29 CFR § 1630.2(r)"
        )
        return DirectThreatOutput(
            direct_threat_exists="no",
            factors_for=_sort(factors_for),
            factors_against=_sort(factors_against),
            key_uncertainties=_sort(key_uncertainties),
        )

    # R036: No direct threat risk identified
    if risk_assessed is False:
        factors_against.append(
            "No direct threat risk identified for this position or individual"
        )
        return DirectThreatOutput(
            direct_threat_exists="no",
            factors_for=_sort(factors_for),
            factors_against=_sort(factors_against),
            key_uncertainties=_sort(key_uncertainties),
        )

    # R037: Individualized assessment required
    if individualized is True:
        factors_against.append(
            "Individualized assessment of risk was conducted as required (29 CFR § 1630.2(r))"
        )
    elif individualized is False:
        factors_for.append(
            "Individualized assessment of direct threat risk was not conducted — required by 29 CFR § 1630.2(r)"
        )
    else:
        key_uncertainties.append(
            "Whether an individualized assessment was conducted is not documented"
        )

    # R038: All four § 1630.2(r) factors must be present
    all_four_present = all([risk_nature, risk_duration, risk_severity, risk_probability])
    any_missing = not all([
        risk_nature is not None,
        risk_duration is not None,
        risk_severity is not None,
        risk_probability is not None,
    ])

    if all_four_present:
        factors_for.append(
            "All four direct threat factors documented: nature, duration, severity, and probability of risk (29 CFR § 1630.2(r))"
        )
    else:
        missing = []
        if not risk_nature:
            missing.append("nature of risk")
        if not risk_duration:
            missing.append("duration of risk")
        if not risk_severity:
            missing.append("severity of risk")
        if not risk_probability:
            missing.append("probability of risk")
        if missing:
            key_uncertainties.append(
                f"Required direct threat factors not documented: {', '.join(missing)}"
            )

    # R039: Risk not assessed at all
    if risk_assessed is None:
        key_uncertainties.append("Whether a direct threat risk was assessed is unknown")

    # R040: Direct threat determination
    if factors_for and all_four_present and individualized is not False and not stereotype_based:
        result = "yes"
    elif not factors_for or (individualized is False) or (not any_missing and not risk_assessed):
        result = "no"
    else:
        result = "indeterminate"

    return DirectThreatOutput(
        direct_threat_exists=result,
        factors_for=_sort(factors_for),
        factors_against=_sort(factors_against),
        key_uncertainties=_sort(key_uncertainties),
    )


# ---------------------------------------------------------------------------
# Component 2.4 — Accommodation Determination (short-circuit composite)
# ---------------------------------------------------------------------------

def assess_accommodation_determination(
    inp: Module2Input,
    m1_out: Module1Output,
    request_out: AccommodationRequestOutput,
    hardship_out: UndueHardshipOutput,
    threat_out: DirectThreatOutput,
) -> AccommodationDeterminationOutput:
    """Composite accommodation determination with short-circuit logic.

    Short-circuit order (first matching rule fires):
    SC1: is_covered_employer = false → no / not_covered_employer
    SC2: is_covered_individual = false → no / not_covered_individual
    SC3: has_qualifying_disability = no → no / not_disabled
    SC4: accommodation_rights_attach = false → no / not_disabled
    SC5: accommodation_request_valid = false → no / invalid_request
    SC6: undue_hardship_applies = yes → no / undue_hardship
    SC7: direct_threat_exists = yes → no / direct_threat
    SC8: All pass AND hardship=no AND threat=no → yes
    SC9: No short-circuit AND any upstream indeterminate → indeterminate

    NOTE: preliminary_qualified_without_accommodation is NO LONGER a short-circuit gate
    in Module 2 (former SC5 removed). The not_qualified determination is now owned by
    the wrapper at WR-3b. This allows WR-2 to fire when preliminary=no but
    accommodation_required=yes and accommodation_theoretically_effective=yes.

    Citation: 42 U.S.C. § 12112(b)(5)(A); 29 CFR § 1630.9.
    """
    ec = m1_out.employer_coverage
    ic = m1_out.individual_status
    dd = m1_out.disability_determination

    # R041-SC1: Covered employer check
    if not ec.is_covered_employer:
        return AccommodationDeterminationOutput(
            accommodation_required="no",
            denial_basis="not_covered_employer",
        )

    # R041-SC2: Covered individual check
    if not ic.is_covered_individual:
        return AccommodationDeterminationOutput(
            accommodation_required="no",
            denial_basis="not_covered_individual",
        )

    # R041-SC3: Qualifying disability check
    if dd.has_qualifying_disability == "no":
        return AccommodationDeterminationOutput(
            accommodation_required="no",
            denial_basis="not_disabled",
        )

    # R041-SC4: Accommodation rights attach check
    if not dd.accommodation_rights_attach:
        return AccommodationDeterminationOutput(
            accommodation_required="no",
            denial_basis="not_disabled",
        )

    # SC5 REMOVED: preliminary_qualified_without_accommodation check no longer gates
    # Module 2. Ownership of the not_qualified determination transferred to wrapper WR-3b.
    # This makes WR-2 structurally reachable.

    # R041-SC5: Valid accommodation request check
    if not request_out.accommodation_request_valid:
        return AccommodationDeterminationOutput(
            accommodation_required="no",
            denial_basis="invalid_request",
        )

    # R041-SC6: Undue hardship check
    if hardship_out.undue_hardship_applies == "yes":
        return AccommodationDeterminationOutput(
            accommodation_required="no",
            denial_basis="undue_hardship",
        )

    # R041-SC7: Direct threat check
    if threat_out.direct_threat_exists == "yes":
        return AccommodationDeterminationOutput(
            accommodation_required="no",
            denial_basis="direct_threat",
        )

    # R041-SC8: All pass — accommodation required
    if (
        hardship_out.undue_hardship_applies == "no"
        and threat_out.direct_threat_exists == "no"
    ):
        return AccommodationDeterminationOutput(
            accommodation_required="yes",
            denial_basis=None,
        )

    # R041-SC9: No short-circuit fired but upstream indeterminate
    return AccommodationDeterminationOutput(
        accommodation_required="indeterminate",
        denial_basis=None,
    )


# ---------------------------------------------------------------------------
# Module 2 orchestrator
# ---------------------------------------------------------------------------

def run_module2(inp: Module2Input, m1_out: Module1Output) -> Module2Output:
    """Execute all four Module 2 components and return the full module output.

    Citation: 42 U.S.C. §§ 12111(10), 12112(b)(5)(A), 12113(b); 29 CFR § 1630.2(p),(r); 29 CFR § 1630.9.
    """
    request_out = assess_accommodation_request(inp)
    hardship_out = assess_undue_hardship(inp)
    threat_out = assess_direct_threat(inp)
    determination_out = assess_accommodation_determination(
        inp, m1_out, request_out, hardship_out, threat_out
    )
    return Module2Output(
        accommodation_request=request_out,
        undue_hardship_analysis=hardship_out,
        direct_threat_analysis=threat_out,
        accommodation_determination=determination_out,
    )
