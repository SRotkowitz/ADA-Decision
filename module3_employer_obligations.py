"""
ADA Decision Engine — Module 3: Employer Obligations
Rule range: R047–R067
Legal source: 42 U.S.C. § 12112(d); 29 CFR § 1630.13, § 1630.14;
              29 CFR § 1630 Appendix; EEOC Enforcement Guidance No. 915.002.

Implements three components:
  3.1 Interactive Process (hybrid: rule-based + standards-based + composite)
  3.2 Medical Inquiry Limitations (rule-based)
  3.3 Confidentiality (rule-based)
"""

from schemas.input_models import Module3Input
from schemas.output_models import (
    Module1Output,
    Module2Output,
    WrapperOutput,
    InteractiveProcessOutput,
    MedicalInquiryOutput,
    ConfidentialityOutput,
    Module3Output,
)


def _sort(arr: list) -> list:
    """Sort a factor/uncertainty array alphabetically for determinism."""
    return sorted(arr)


# ---------------------------------------------------------------------------
# Component 3.1 — Interactive Process (hybrid)
# ---------------------------------------------------------------------------

def assess_interactive_process(
    inp: Module3Input,
    m2_out: Module2Output,
    wrapper_out: WrapperOutput,
) -> InteractiveProcessOutput:
    """Evaluate employer compliance with the interactive process obligation.

    3.1a process_mechanically_compliant (rule-based boolean):
         acknowledgment completed AND dialogue initiated within 10 business days
         (engine heuristic, not a statutory deadline) AND documentation scope recorded.

    3.1b process_quality (standards-based): good-faith engagement factors.

    3.1c interactive_process_compliant (composite):
         Aggregates 3.1a and 3.1b per documented logic matrix.

    Citation: EEOC Enforcement Guidance No. 915.002; 29 CFR § 1630 Appendix.
    """
    factors_for: list = []
    factors_against: list = []
    key_uncertainties: list = []

    ack = getattr(inp, "acknowledgment_completed", None)
    dialogue = getattr(inp, "dialogue_initiated_within_10_days", None)
    doc_scope = getattr(inp, "documentation_scope_recorded", None)
    multialts = getattr(inp, "multiple_alternatives_considered", None)
    jan = getattr(inp, "jan_consulted", None)
    decision_communicated = getattr(inp, "decision_communicated_with_explanation", None)
    follow_up = getattr(inp, "follow_up_on_implementation", None)
    unexplained_delay = getattr(inp, "unexplained_delay_occurred", None)
    all_rejected = getattr(inp, "all_options_rejected_without_rationale", None)
    stereotype_reasoning = getattr(inp, "stereotype_based_reasoning", None)
    unilateral_termination = getattr(inp, "unilateral_termination_of_process", None)
    participation = getattr(inp, "employee_interactive_process_participation", "good_faith")
    participation_documented = getattr(inp, "employee_nonparticipation_documented", None)

    # R047: Mechanical compliance — rule-based boolean
    # Engine heuristic: 10 business days for dialogue initiation (not a statutory deadline)
    mechanical_compliant = bool(ack and dialogue and doc_scope)

    # R048: Process quality — standards-based factors FOR good faith
    if ack:
        factors_for.append("Acknowledgment of accommodation request completed")
    if dialogue:
        factors_for.append("Dialogue initiated within 10 business days of request (engine heuristic)")
    if multialts:
        factors_for.append("Multiple accommodation alternatives were considered")
    if jan:
        factors_for.append("Job Accommodation Network (JAN) was consulted")
    if decision_communicated:
        factors_for.append("Decision communicated to employee with explanation")
    if follow_up:
        factors_for.append("Follow-up conducted on accommodation implementation")

    # R049: Factors AGAINST good faith
    if unexplained_delay:
        factors_against.append("Unexplained delay in initiating or completing interactive process")
    if all_rejected:
        factors_against.append("All accommodation options rejected without documented rationale")
    if stereotype_reasoning:
        factors_against.append("Stereotype-based reasoning identified in accommodation decision-making")
    if unilateral_termination:
        factors_against.append("Interactive process was unilaterally terminated by employer")
    if not ack:
        if ack is False:
            factors_against.append("Acknowledgment of accommodation request was not completed")
        else:
            key_uncertainties.append("Whether acknowledgment was completed is not documented")
    if not dialogue and dialogue is False:
        factors_against.append("Dialogue was not initiated within 10 business days")
    elif dialogue is None:
        key_uncertainties.append("Whether dialogue was initiated timely is not documented")
    if not doc_scope and doc_scope is False:
        factors_against.append("Documentation scope was not recorded")
    elif doc_scope is None:
        key_uncertainties.append("Whether documentation scope was recorded is not documented")

    # R050: Employee non-participation as weighting factor (not automatic defeater)
    # When employee refused or abandoned with documented basis: weighting factor FOR employer good faith
    if participation in ("refused", "abandoned") and participation_documented:
        factors_for.append(
            f"Employee {participation} interactive process with documented basis — shifts process quality one level in employer's favor"
        )

    # R051: Derive process_quality
    if factors_for and not factors_against and not key_uncertainties:
        process_quality = "yes"
    elif factors_against and not factors_for:
        process_quality = "no"
    elif factors_against and not key_uncertainties and len(factors_against) > len(factors_for):
        process_quality = "no"
    elif key_uncertainties and not factors_against:
        process_quality = "indeterminate"
    elif factors_for and factors_against:
        process_quality = "indeterminate"
    else:
        process_quality = "indeterminate"

    # R052: interactive_process_compliant composite matrix
    # mechanical=false AND quality=no → no
    if not mechanical_compliant and process_quality == "no":
        interactive_process_compliant = "no"
    # mechanical=false AND quality=indeterminate → indeterminate
    elif not mechanical_compliant and process_quality == "indeterminate":
        interactive_process_compliant = "indeterminate"
    # mechanical=true AND quality=no → indeterminate
    elif mechanical_compliant and process_quality == "no":
        interactive_process_compliant = "indeterminate"
    # mechanical=true AND quality=yes → yes
    elif mechanical_compliant and process_quality == "yes":
        interactive_process_compliant = "yes"
    # all other combinations → indeterminate
    else:
        interactive_process_compliant = "indeterminate"

    return InteractiveProcessOutput(
        process_mechanically_compliant=mechanical_compliant,
        process_quality=process_quality,
        interactive_process_compliant=interactive_process_compliant,
        factors_for=_sort(factors_for),
        factors_against=_sort(factors_against),
        key_uncertainties=_sort(key_uncertainties),
    )


# ---------------------------------------------------------------------------
# Component 3.2 — Medical Inquiry Limitations
# ---------------------------------------------------------------------------

def assess_medical_inquiry(inp: Module3Input) -> MedicalInquiryOutput:
    """Evaluate whether the medical inquiry complies with ADA limitations by employment stage.

    Pre-offer: disability questions and medical exams prohibited.
    Post-offer: permitted if all entering employees in same job category examined,
                info kept confidential, results used only as ADA permits.
    During employment: permitted only if job-related and consistent with business necessity;
                       voluntary wellness program exception.

    Citation: 42 U.S.C. § 12112(d); 29 CFR § 1630.13, § 1630.14.
    """
    stage = inp.medical_inquiry_stage
    inq_type = inp.inquiry_type
    job_related = inp.inquiry_job_related
    business_necessity = inp.inquiry_consistent_with_business_necessity
    all_same_category = getattr(inp, "all_same_category_examined", None)

    # R053: Pre-offer stage — disability questions and medical exams prohibited
    if stage == "pre_offer":
        if inq_type in ("disability_related_question", "medical_examination"):
            return MedicalInquiryOutput(
                inquiry_permitted=False,
                violation_basis=(
                    f"Pre-offer {inq_type.replace('_', ' ')} is prohibited by 42 U.S.C. § 12112(d)(2)(A)"
                ),
            )
        # Other inquiry types (document requests etc.) may be permissible pre-offer
        return MedicalInquiryOutput(inquiry_permitted=True)

    # R054: Post-offer stage — permitted with three conditions
    if stage == "post_offer":
        violations = []
        if all_same_category is False:
            violations.append(
                "Not all entering employees in same job category examined — violates 29 CFR § 1630.14(b)(1)"
            )
        if violations:
            return MedicalInquiryOutput(
                inquiry_permitted=False,
                violation_basis="; ".join(violations),
            )
        return MedicalInquiryOutput(inquiry_permitted=True)

    # R055: During employment — job-related and business necessity required
    if stage == "during_employment":
        if not job_related or not business_necessity:
            violation_parts = []
            if not job_related:
                violation_parts.append("inquiry is not job-related")
            if not business_necessity:
                violation_parts.append("inquiry is not consistent with business necessity")
            return MedicalInquiryOutput(
                inquiry_permitted=False,
                violation_basis=(
                    f"Employment-stage inquiry not permitted: {' and '.join(violation_parts)} "
                    "(42 U.S.C. § 12112(d)(4)(A); 29 CFR § 1630.14(c))"
                ),
            )
        return MedicalInquiryOutput(inquiry_permitted=True)

    return MedicalInquiryOutput(inquiry_permitted=True)


# ---------------------------------------------------------------------------
# Component 3.3 — Confidentiality
# ---------------------------------------------------------------------------

def assess_confidentiality(inp: Module3Input) -> ConfidentialityOutput:
    """Evaluate employer compliance with ADA medical information confidentiality requirements.

    Medical info must be on separate forms and in separate files. Access limited to:
    supervisors needing to know restrictions/accommodations, first aid/safety personnel,
    government investigators. No unauthorized disclosure permitted.

    Citation: 42 U.S.C. § 12112(d)(3)(B); 29 CFR § 1630.14(b)(1).
    """
    separate_file = inp.medical_information_in_separate_file
    limited_access = inp.access_limited_to_authorized_personnel
    unauthorized = inp.unauthorized_disclosure_occurred

    violations = []

    # R056: Separate file requirement
    if not separate_file:
        violations.append(
            "Medical information not maintained in separate confidential file — required by 42 U.S.C. § 12112(d)(3)(B)"
        )

    # R057: Access limitation requirement
    if not limited_access:
        violations.append(
            "Medical information access not limited to authorized personnel — required by 29 CFR § 1630.14(b)(1)"
        )

    # R058: Unauthorized disclosure
    if unauthorized:
        violations.append(
            "Unauthorized disclosure of medical information occurred — violates 42 U.S.C. § 12112(d)(3)(B)"
        )

    compliant = len(violations) == 0
    return ConfidentialityOutput(
        confidentiality_compliant=compliant,
        violation_details=_sort(violations) if violations else None,
    )


# ---------------------------------------------------------------------------
# Module 3 orchestrator
# ---------------------------------------------------------------------------

def run_module3(
    inp: Module3Input,
    m1_out: Module1Output,
    m2_out: Module2Output,
    wrapper_out: WrapperOutput,
) -> Module3Output:
    """Execute all three Module 3 components and return the full module output.

    Citation: 42 U.S.C. § 12112(d); 29 CFR § 1630.13, § 1630.14; EEOC Guidance 915.002.
    """
    return Module3Output(
        interactive_process=assess_interactive_process(inp, m2_out, wrapper_out),
        medical_inquiry_limitations=assess_medical_inquiry(inp),
        confidentiality=assess_confidentiality(inp),
    )
