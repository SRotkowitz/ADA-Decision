"""
ADA Decision Engine — Wrapper: is_qualified_individual Composite + Unified Orchestration
Wrapper rules: WR-1 through WR-5
Legal source: 42 U.S.C. § 12111(8); module_interface_spec.json design decision DD-1, DD-2.

Executed AFTER Module 2 completes and BEFORE Module 3 begins. Resolves the final
is_qualified_individual value by combining Module 1's preliminary determination with
Module 2's accommodation_required output.

Also provides the unified full-assessment orchestrator.

PATCH APPLIED (Phase 8 — WR-3b addition):
  WR-3b added between WR-3 and WR-4. Owns the not_qualified determination previously
  held by Module 2 SC5. Fires when preliminary=no AND accommodation_required=no AND
  denial_basis is NOT undue_hardship or direct_threat (i.e., no substantive defense
  was the reason — accommodation simply was not required at all).

  Full WR chain after patch:
    WR-1:  preliminary=yes → is_qualified_individual=yes
    WR-2:  preliminary=no AND accommodation_required=yes AND theoretically_effective=yes → yes
    WR-3:  preliminary=no AND accommodation_required=no AND denial_basis in [undue_hardship, direct_threat] → no
    WR-3b: preliminary=no AND accommodation_required=no AND denial_basis NOT IN [undue_hardship, direct_threat] → no / not_qualified
    WR-4:  preliminary=no AND accommodation_required=indeterminate → indeterminate
    WR-5:  any upstream indeterminate and no prior rule fired → indeterminate
"""

from schemas.input_models import UnifiedInput, Module4Input
from schemas.output_models import (
    Module1Output,
    Module2Output,
    Module3Output,
    Module4Output,
    WrapperOutput,
    ModuleOutputs,
    UnifiedOutput,
)
from engine.module1_coverage_eligibility import run_module1
from engine.module2_accommodation_analysis import run_module2
from engine.module3_employer_obligations import run_module3
from engine.module4_violation_risk import run_module4


def apply_wrapper(
    m1_out: Module1Output,
    m2_out: Module2Output,
    accommodation_theoretically_effective: str,
) -> WrapperOutput:
    """Compute the final is_qualified_individual composite per WR-1 through WR-5.

    Executed after Module 2 and before Module 3. The final composite is_qualified_individual
    is the only determination computed at wrapper level.

    WR-1:  preliminary_qualified_without_accommodation = yes → is_qualified_individual = yes
    WR-2:  preliminary=no AND accommodation_required=yes AND theoretically_effective=yes → yes
    WR-3:  preliminary=no AND accommodation_required=no AND denial_basis in [undue_hardship, direct_threat] → no
    WR-3b: preliminary=no AND accommodation_required=no AND denial_basis NOT IN [undue_hardship, direct_threat] → no / not_qualified
    WR-4:  preliminary=no AND accommodation_required=indeterminate → indeterminate
    WR-5:  Any upstream indeterminate AND no prior WR rule fired → indeterminate

    Citation: 42 U.S.C. § 12111(8); 29 CFR § 1630.2(m).
    """
    prelim = m1_out.qualified_individual.preliminary_qualified_without_accommodation
    acc_required = m2_out.accommodation_determination.accommodation_required
    denial_basis = m2_out.accommodation_determination.denial_basis

    # WR-1: Can perform essential functions without accommodation → qualified
    if prelim == "yes":
        return WrapperOutput(is_qualified_individual="yes", rule_applied="WR-1")

    # WR-2: Cannot without accommodation, but accommodation required and would be effective → qualified
    if (
        prelim == "no"
        and acc_required == "yes"
        and accommodation_theoretically_effective == "yes"
    ):
        return WrapperOutput(is_qualified_individual="yes", rule_applied="WR-2")

    # WR-3: Cannot without accommodation, denied on substantive defense → not qualified
    if (
        prelim == "no"
        and acc_required == "no"
        and denial_basis in ("undue_hardship", "direct_threat")
    ):
        return WrapperOutput(is_qualified_individual="no", rule_applied="WR-3")

    # WR-3b: preliminary=no, accommodation_required=no, non-UH/DT denial → not qualified
    # Owns the not_qualified path formerly held by Module 2 SC5.
    # Fires when preliminary=no AND accommodation_required=no AND the denial was not
    # a substantive undue_hardship or direct_threat defense — individual cannot perform
    # essential functions without accommodation, and no accommodation is required.
    # Citation: 42 U.S.C. § 12111(8); 29 CFR § 1630.2(m).
    if (
        prelim == "no"
        and acc_required == "no"
        and denial_basis not in ("undue_hardship", "direct_threat")
    ):
        return WrapperOutput(is_qualified_individual="no", rule_applied="WR-3b")

    # WR-4: Cannot without accommodation, accommodation indeterminate → indeterminate
    if prelim == "no" and acc_required == "indeterminate":
        return WrapperOutput(is_qualified_individual="indeterminate", rule_applied="WR-4")

    # WR-5: Any upstream indeterminate and no prior rule fired → indeterminate
    return WrapperOutput(is_qualified_individual="indeterminate", rule_applied="WR-5")


def _derive_employer_compliance_status(m3_out: Module3Output) -> str:
    """Derive employer_compliance_status from all three Module 3 components.

    compliant = interactive_process_compliant==yes AND inquiry_permitted==yes AND confidentiality_compliant==yes
    non_compliant = any component produces 'no'
    indeterminate = no component produces 'no' but at least one produces 'indeterminate'

    Non_compliant takes precedence over indeterminate per unified output schema.
    """
    ip = m3_out.interactive_process.interactive_process_compliant
    inquiry = m3_out.medical_inquiry_limitations.inquiry_permitted
    conf = m3_out.confidentiality.confidentiality_compliant

    # Non-compliant takes precedence
    if ip == "no" or not inquiry or not conf:
        return "non_compliant"

    # All yes
    if ip == "yes" and inquiry and conf:
        return "compliant"

    # Mixed — at least one indeterminate
    return "indeterminate"


def _aggregate_indeterminate_factors(
    m1_out: Module1Output,
    m2_out: Module2Output,
    m3_out: Module3Output,
    m4_out: Module4Output,
) -> dict:
    """Collect all key_uncertainties arrays from indeterminate components, keyed as {module_id}.{component_id}.

    Citation: unified_output_schema.json — indeterminate_factors derivation.
    """
    result = {}

    # Module 1
    dd = m1_out.disability_determination
    if dd.has_qualifying_disability == "indeterminate" and dd.key_uncertainties:
        result["ada_coverage_eligibility.disability_determination"] = dd.key_uncertainties

    qi = m1_out.qualified_individual
    if qi.is_qualified_individual == "indeterminate" and qi.key_uncertainties:
        result["ada_coverage_eligibility.qualified_individual"] = qi.key_uncertainties

    # Module 2
    uh = m2_out.undue_hardship_analysis
    if uh.undue_hardship_applies == "indeterminate" and uh.key_uncertainties:
        result["ada_accommodation_analysis.undue_hardship_analysis"] = uh.key_uncertainties

    dt = m2_out.direct_threat_analysis
    if dt.direct_threat_exists == "indeterminate" and dt.key_uncertainties:
        result["ada_accommodation_analysis.direct_threat_analysis"] = dt.key_uncertainties

    ad = m2_out.accommodation_determination
    if ad.accommodation_required == "indeterminate":
        result["ada_accommodation_analysis.accommodation_determination"] = [
            "Upstream indeterminate inputs prevent accommodation determination"
        ]

    # Module 3
    ip = m3_out.interactive_process
    if ip.interactive_process_compliant == "indeterminate" and ip.key_uncertainties:
        result["ada_employer_obligations.interactive_process"] = ip.key_uncertainties

    return result


def run_full_assessment(inp: UnifiedInput) -> UnifiedOutput:
    """Execute the complete ADA Decision Engine assessment in module order.

    Execution order (per module_interface_spec.json):
      1. Module 1 — ada_coverage_eligibility
      2. Module 2 — ada_accommodation_analysis
      3. Wrapper — is_qualified_individual composite (WR-1 through WR-5)
      4. Module 3 — ada_employer_obligations
      5. Module 4 — ada_violation_risk

    Returns the unified output including summary fields and full module_outputs.
    Citation: unified_output_schema.json v0.1; module_interface_spec.json v0.1.
    """
    # Step 1: Module 1
    m1_out = run_module1(inp)

    # Step 2: Module 2
    m2_out = run_module2(inp, m1_out)

    # Step 3: Wrapper — resolve final is_qualified_individual
    wrapper_out = apply_wrapper(
        m1_out, m2_out, inp.accommodation_theoretically_effective
    )

    # Step 4: Module 3 (receives wrapper is_qualified_individual via inp fields)
    m3_out = run_module3(inp, m1_out, m2_out, wrapper_out)

    # Step 5: Module 4 (receives wrapper is_qualified_individual)
    m4_out = run_module4(inp, m1_out, m2_out, m3_out, wrapper_out)

    # Derive summary outputs
    ada_covered = (
        m1_out.employer_coverage.is_covered_employer
        and m1_out.individual_status.is_covered_individual
    )
    has_qualifying_disability = m1_out.disability_determination.has_qualifying_disability
    is_qualified_individual = wrapper_out.is_qualified_individual
    accommodation_required = m2_out.accommodation_determination.accommodation_required
    employer_compliance_status = _derive_employer_compliance_status(m3_out)
    violation_risk_level = m4_out.overall_violation_risk.overall_risk_level
    recommended_actions = m4_out.overall_violation_risk.recommended_actions
    indeterminate_factors = _aggregate_indeterminate_factors(m1_out, m2_out, m3_out, m4_out)

    return UnifiedOutput(
        ada_covered=ada_covered,
        has_qualifying_disability=has_qualifying_disability,
        is_qualified_individual=is_qualified_individual,
        accommodation_required=accommodation_required,
        employer_compliance_status=employer_compliance_status,
        violation_risk_level=violation_risk_level,
        recommended_actions=recommended_actions,
        indeterminate_factors=indeterminate_factors,
        module_outputs=ModuleOutputs(
            ada_coverage_eligibility=m1_out,
            ada_accommodation_analysis=m2_out,
            ada_employer_obligations=m3_out,
            ada_violation_risk=m4_out,
        ),
    )
