"""
ADA Decision Engine — Module 1: Coverage and Eligibility
Rule range: R001–R025
Legal source: 42 U.S.C. §§ 12111–12112; 29 CFR § 1630.2; ADA Amendments Act of 2008.

Implements four components:
  1.1 Employer Coverage (rule-based)
  1.2 Individual Status (rule-based)
  1.3 Disability Determination (standards-based)
  1.4 Qualified Individual (standards-based, preliminary)
"""

from schemas.input_models import Module1Input
from schemas.output_models import (
    EmployerCoverageOutput,
    IndividualStatusOutput,
    DisabilityDeterminationOutput,
    QualifiedIndividualOutput,
    Module1Output,
)

# Employer types that are covered regardless of employee count
_ALWAYS_COVERED_EMPLOYER_TYPES = {
    "state_local_government",
    "employment_agency",
    "labor_organization",
    "joint_labor_management_committee",
}


def _sort(arr: list) -> list:
    """Sort a factor/uncertainty array alphabetically for determinism."""
    return sorted(arr)


# ---------------------------------------------------------------------------
# Component 1.1 — Employer Coverage
# ---------------------------------------------------------------------------

def assess_employer_coverage(inp: Module1Input) -> EmployerCoverageOutput:
    """Determine whether the employer is a covered entity under Title I of the ADA.

    Rule-based determination. Private employers must meet both the 15-employee
    threshold and the 20-workweeks threshold. Other entity types are covered
    per 29 CFR § 1630.2(b) without a size threshold.

    Citation: 42 U.S.C. § 12111(5)(A); 29 CFR § 1630.2(e).
    """
    # R001: Non-private employer types are covered without size threshold
    if inp.employer_type in _ALWAYS_COVERED_EMPLOYER_TYPES:
        return EmployerCoverageOutput(is_covered_employer=True)

    # R002: Private employer — must have ≥15 employees for ≥20 workweeks
    covered = (
        inp.total_employees >= 15
        and inp.weeks_with_15_employees >= 20
    )
    return EmployerCoverageOutput(is_covered_employer=covered)


# ---------------------------------------------------------------------------
# Component 1.2 — Individual Status
# ---------------------------------------------------------------------------

def assess_individual_status(inp: Module1Input) -> IndividualStatusOutput:
    """Determine whether the individual is a covered individual under the ADA.

    Rule-based determination. Independent contractors are excluded.
    Current employees, job applicants, and former employees are covered.

    Citation: 42 U.S.C. § 12112(a); 29 CFR § 1630.2(f).
    """
    # R003: Independent contractors are not covered
    if getattr(inp, "is_independent_contractor", False):
        return IndividualStatusOutput(is_covered_individual=False)

    # R004: Covered statuses
    covered_statuses = {"current_employee", "job_applicant", "former_employee"}
    covered = inp.individual_status in covered_statuses
    return IndividualStatusOutput(is_covered_individual=covered)


# ---------------------------------------------------------------------------
# Component 1.3 — Disability Determination
# ---------------------------------------------------------------------------

def assess_disability_determination(inp: Module1Input) -> DisabilityDeterminationOutput:
    """Determine whether the individual has a qualifying disability under the ADA.

    Standards-based determination. ADAAA broad construction applies — ambiguous
    cases resolved toward coverage. Episodic conditions and conditions in remission
    evaluated at worst manifestation. Mitigating measures ignored except ordinary
    eyeglasses/contact lenses. Regarded-as prong: transitory-and-minor exclusion
    applies (expected duration < 6 months AND objectively minor). accommodation_rights_attach
    is false when disability_basis is regarded_as only.

    Citation: 42 U.S.C. § 12102; 29 CFR § 1630.2(g),(j).
    """
    factors_for: list = []
    factors_against: list = []
    key_uncertainties: list = []

    basis = inp.disability_basis
    substantially_limits = inp.substantially_limits
    condition_duration = getattr(inp, "condition_duration", None)
    is_episodic = getattr(inp, "condition_is_episodic_or_remission", False)

    # R005: regarded_as prong — check transitory-and-minor exclusion
    if basis == "regarded_as":
        # Transitory-and-minor = expected duration < 6 months AND objectively minor
        if condition_duration == "transitory_minor":
            # R006: Transitory-and-minor exclusion bars regarded-as coverage
            factors_against.append(
                "Condition classified as transitory and minor — regarded-as prong exclusion applies (29 CFR § 1630.2(l))"
            )
            return DisabilityDeterminationOutput(
                has_qualifying_disability="no",
                accommodation_rights_attach=False,
                disability_basis=basis,
                factors_for=_sort(factors_for),
                factors_against=_sort(factors_against),
                key_uncertainties=_sort(key_uncertainties),
            )
        elif condition_duration in (None, "unknown"):
            key_uncertainties.append(
                "Condition duration is unknown — regarded-as exclusion cannot be ruled out"
            )
        # R007: No transitory-and-minor exclusion — regarded-as prong established
        factors_for.append(
            "Individual subjected to prohibited action based on actual or perceived impairment (29 CFR § 1630.2(g)(1)(iii))"
        )
        # Accommodation rights do NOT attach under regarded-as only
        return DisabilityDeterminationOutput(
            has_qualifying_disability="yes" if not key_uncertainties else "indeterminate",
            accommodation_rights_attach=False,
            disability_basis=basis,
            factors_for=_sort(factors_for),
            factors_against=_sort(factors_against),
            key_uncertainties=_sort(key_uncertainties),
        )

    # R008: actual_disability or record_of_disability prong
    # accommodation_rights_attach is True for these prongs
    accommodation_rights_attach = True

    # R009: Episodic/in-remission — evaluate at worst manifestation per 29 CFR § 1630.2(j)(1)(vii)
    if is_episodic:
        factors_for.append(
            "Episodic condition or condition in remission — evaluated at worst manifestation (29 CFR § 1630.2(j)(1)(vii))"
        )

    # R010: Substantially limits evaluation (ADAAA broad construction)
    if substantially_limits == "yes":
        factors_for.append(
            "Impairment substantially limits one or more major life activities (29 CFR § 1630.2(j))"
        )
    elif substantially_limits == "no":
        factors_against.append(
            "Impairment does not substantially limit a major life activity"
        )
    else:  # indeterminate
        key_uncertainties.append(
            "Substantial limitation not established — medical documentation may be needed"
        )

    # R011: Major life activities affected
    mlas = getattr(inp, "major_life_activities_affected", [])
    if mlas:
        factors_for.append(
            f"Major life activities affected: {', '.join(mlas)}"
        )
    else:
        key_uncertainties.append(
            "No major life activities identified — required for disability determination"
        )

    # R012: ADAAA broad construction — resolve ambiguous cases toward coverage
    has_qualifying_disability: str
    if factors_against and not factors_for and not key_uncertainties:
        has_qualifying_disability = "no"
    elif key_uncertainties and not factors_against:
        # Ambiguous — ADAAA says resolve toward coverage but genuinely indeterminate
        has_qualifying_disability = "indeterminate"
    elif substantially_limits == "yes" and mlas:
        has_qualifying_disability = "yes"
    elif substantially_limits == "no":
        has_qualifying_disability = "no"
    else:
        has_qualifying_disability = "indeterminate"

    # R013: record_of_disability requires history/classification — add note
    if basis == "record_of_disability":
        factors_for.append(
            "Record of disability prong asserted — history or classification of substantially limiting impairment (29 CFR § 1630.2(k))"
        )

    return DisabilityDeterminationOutput(
        has_qualifying_disability=has_qualifying_disability,
        accommodation_rights_attach=accommodation_rights_attach if has_qualifying_disability != "no" else False,
        disability_basis=basis,
        factors_for=_sort(factors_for),
        factors_against=_sort(factors_against),
        key_uncertainties=_sort(key_uncertainties),
    )


# ---------------------------------------------------------------------------
# Component 1.4 — Qualified Individual (preliminary)
# ---------------------------------------------------------------------------

def assess_qualified_individual(inp: Module1Input) -> QualifiedIndividualOutput:
    """Preliminary determination of whether the individual is a qualified individual.

    Standards-based. The final is_qualified_individual composite is computed by the
    wrapper (WR-1 through WR-5) after Module 2 completes. preliminary_qualified_without_accommodation
    is the explicit field consumed by Module 2 component 2.4 (R041) and the wrapper WR rules.

    Evaluates: (a) can perform essential functions without accommodation;
    (b) can perform essential functions with accommodation (preliminary).

    Citation: 42 U.S.C. § 12111(8); 29 CFR § 1630.2(m),(n).
    """
    factors_for: list = []
    factors_against: list = []
    key_uncertainties: list = []

    can_without = inp.can_perform_essential_functions_without_accommodation
    meets_reqs = inp.meets_skill_experience_education_requirements
    essential_identified = inp.essential_functions_identified

    # R014: Skill/experience/education requirements
    if meets_reqs:
        factors_for.append(
            "Individual meets position skill, experience, education, and job-related requirements (29 CFR § 1630.2(m))"
        )
    else:
        factors_against.append(
            "Individual does not meet position skill, experience, education, or job-related requirements (29 CFR § 1630.2(m))"
        )

    # R015: Essential functions identification
    if not essential_identified:
        key_uncertainties.append(
            "Essential functions not documented — qualified individual determination may be unreliable"
        )
    else:
        factors_for.append(
            "Essential functions of position identified and documented (29 CFR § 1630.2(n))"
        )

    # R016: Can perform essential functions without accommodation
    if can_without == "yes":
        factors_for.append(
            "Individual can perform all essential functions without accommodation"
        )
        preliminary_qualified_without_accommodation = "yes"
    elif can_without == "no":
        factors_against.append(
            "Individual cannot perform one or more essential functions without accommodation"
        )
        preliminary_qualified_without_accommodation = "no"
    else:
        key_uncertainties.append(
            "Ability to perform essential functions without accommodation is undetermined"
        )
        preliminary_qualified_without_accommodation = "indeterminate"

    # R017: Preliminary is_qualified_individual — only considers without-accommodation scenario here
    # (with-accommodation resolution is a wrapper-level composite)
    if not meets_reqs:
        preliminary_qi = "no"
    elif preliminary_qualified_without_accommodation == "yes":
        preliminary_qi = "yes"
    elif preliminary_qualified_without_accommodation == "indeterminate":
        preliminary_qi = "indeterminate"
    else:
        # no — may still qualify with accommodation; wrapper resolves
        preliminary_qi = "indeterminate"

    return QualifiedIndividualOutput(
        preliminary_qualified_without_accommodation=preliminary_qualified_without_accommodation,
        is_qualified_individual=preliminary_qi,
        factors_for=_sort(factors_for),
        factors_against=_sort(factors_against),
        key_uncertainties=_sort(key_uncertainties),
    )


# ---------------------------------------------------------------------------
# Module 1 orchestrator
# ---------------------------------------------------------------------------

def run_module1(inp: Module1Input) -> Module1Output:
    """Execute all four Module 1 components in order and return the full module output.

    Citation: 42 U.S.C. §§ 12111–12112; 29 CFR § 1630.2.
    """
    return Module1Output(
        employer_coverage=assess_employer_coverage(inp),
        individual_status=assess_individual_status(inp),
        disability_determination=assess_disability_determination(inp),
        qualified_individual=assess_qualified_individual(inp),
    )
