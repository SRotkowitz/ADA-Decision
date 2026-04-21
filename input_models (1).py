"""
ADA Decision Engine — Input Models
All Pydantic input schemas for all endpoints.
Field definitions derived from ada_unified_input_schema.json v0.1.
"""

from __future__ import annotations
from typing import List, Literal, Optional
from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Shared literal types
# ---------------------------------------------------------------------------

DetermState = Literal["yes", "no", "indeterminate"]
RiskLevel = Literal["minimal", "low", "moderate", "high", "critical"]

EmployerType = Literal[
    "private_employer",
    "state_local_government",
    "employment_agency",
    "labor_organization",
    "joint_labor_management_committee",
]

IndividualStatus = Literal["current_employee", "job_applicant", "former_employee"]

DisabilityBasis = Literal["actual_disability", "record_of_disability", "regarded_as"]

ImpairmentType = Literal[
    "physical",
    "mental",
    "sensory",
    "neurological",
    "musculoskeletal",
    "cardiovascular",
    "respiratory",
    "digestive",
    "genitourinary",
    "hemic_lymphatic",
    "skin",
    "endocrine",
    "chronic_disease",
    "episodic",
    "in_remission",
    "other",
]

ConditionDuration = Literal[
    "transitory_minor",
    "six_months_or_less",
    "more_than_six_months",
    "permanent",
    "unknown",
]

AccommodationType = Literal[
    "job_restructuring",
    "modified_schedule",
    "reassignment",
    "equipment_modification",
    "policy_modification",
    "reader_interpreter",
    "leave_as_accommodation",
    "telework",
    "facility_access",
    "other",
]

RequestingParty = Literal[
    "employee", "family_member", "healthcare_provider", "representative"
]

InteractiveParticipation = Literal["good_faith", "partial", "refused", "abandoned"]

AdverseActionType = Literal[
    "termination",
    "demotion",
    "reduction_in_hours",
    "denial_of_promotion",
    "suspension",
    "reassignment_punitive",
    "constructive_discharge",
    "other",
]

AdverseActionReason = Literal[
    "performance",
    "conduct",
    "reduction_in_force",
    "position_elimination",
    "accommodation_denial_basis",
    "undocumented",
]

HarassmentSeverity = Literal[
    "isolated_minor", "repeated_minor", "isolated_severe", "pervasive"
]

InquiryStage = Literal["pre_offer", "post_offer", "during_employment"]

InquiryType = Literal[
    "disability_related_question",
    "medical_examination",
    "documentation_request",
    "functional_capacity_evaluation",
]

EvidenceType = Literal["direct", "circumstantial", "none"]


# ---------------------------------------------------------------------------
# Module 1 — Coverage & Eligibility
# ---------------------------------------------------------------------------

class Module1Input(BaseModel):
    """Input fields for Module 1: Coverage and Eligibility.
    Sources: 42 U.S.C. §§ 12111–12112; 29 CFR § 1630.2.
    """
    employer_type: EmployerType
    total_employees: int = Field(..., ge=0)
    weeks_with_15_employees: int = Field(..., ge=0, le=52)
    individual_status: IndividualStatus
    is_independent_contractor: bool = False
    disability_basis: DisabilityBasis
    impairment_type: ImpairmentType
    impairment_description: Optional[str] = None
    major_life_activities_affected: List[str]
    substantially_limits: DetermState
    condition_is_episodic_or_remission: Optional[bool] = False
    condition_duration: Optional[ConditionDuration] = None
    essential_functions_identified: bool
    can_perform_essential_functions_without_accommodation: DetermState
    meets_skill_experience_education_requirements: bool


# ---------------------------------------------------------------------------
# Module 2 — Accommodation Analysis  (also requires M1 dependency fields)
# ---------------------------------------------------------------------------

class Module2Input(Module1Input):
    """Input fields for Module 2: Accommodation Analysis.
    Extends Module1Input with M1 dependency pass-through fields and M2-specific inputs.
    Sources: 42 U.S.C. §§ 12111(10), 12112(b)(5)(A), 12113(b); 29 CFR § 1630.2(p),(r); EEOC Guidance 915.002.
    """
    # M2-specific: accommodation request
    accommodation_type_requested: AccommodationType
    accommodation_description: Optional[str] = None
    accommodation_request_date: Optional[str] = None
    requesting_party: RequestingParty = "employee"
    functional_limitation_identified: bool
    qualifying_purpose: bool

    # M2-specific: undue hardship
    accommodation_estimated_cost: Optional[float] = Field(default=None, ge=0)
    employer_annual_operating_budget: Optional[float] = Field(default=None, ge=0)
    employer_financial_resources_adequate: Optional[bool] = None
    other_resources_available: Optional[bool] = None
    accommodation_fundamentally_alters_operations: Optional[bool] = None
    undocumented_hardship_defense: Optional[bool] = False

    # M2-specific: direct threat
    direct_threat_risk_assessed: Optional[bool] = None
    risk_nature_documented: Optional[bool] = None
    risk_duration_documented: Optional[bool] = None
    risk_severity_documented: Optional[bool] = None
    risk_probability_documented: Optional[bool] = None
    individualized_assessment_conducted: Optional[bool] = None
    stereotype_based_assessment: Optional[bool] = False


# ---------------------------------------------------------------------------
# Module 3 — Employer Obligations (also requires M1+M2 dependency fields)
# ---------------------------------------------------------------------------

class Module3Input(Module2Input):
    """Input fields for Module 3: Employer Obligations.
    Extends Module2Input. Sources: 42 U.S.C. § 12112(d); 29 CFR § 1630.13, § 1630.14; EEOC Guidance 915.002.
    """
    # 3.1 interactive process
    acknowledgment_completed: Optional[bool] = None
    dialogue_initiated_within_10_days: Optional[bool] = None
    documentation_scope_recorded: Optional[bool] = None
    multiple_alternatives_considered: Optional[bool] = None
    jan_consulted: Optional[bool] = None
    decision_communicated_with_explanation: Optional[bool] = None
    follow_up_on_implementation: Optional[bool] = None
    unexplained_delay_occurred: Optional[bool] = None
    all_options_rejected_without_rationale: Optional[bool] = None
    stereotype_based_reasoning: Optional[bool] = None
    unilateral_termination_of_process: Optional[bool] = None
    employee_interactive_process_participation: InteractiveParticipation = "good_faith"
    employee_nonparticipation_documented: Optional[bool] = None

    # 3.2 medical inquiry
    medical_inquiry_stage: InquiryStage
    inquiry_type: InquiryType
    inquiry_job_related: bool
    inquiry_consistent_with_business_necessity: bool
    all_same_category_examined: Optional[bool] = None  # post-offer: all entering employees in same category

    # 3.3 confidentiality
    medical_information_in_separate_file: bool
    access_limited_to_authorized_personnel: bool
    unauthorized_disclosure_occurred: bool


# ---------------------------------------------------------------------------
# Module 4 — Violation Risk (also requires M1+M2+M3 dependency fields)
# ---------------------------------------------------------------------------

class Module4Input(Module3Input):
    """Input fields for Module 4: Violation Risk.
    Extends Module3Input. Sources: 42 U.S.C. §§ 12112, 12113, 12203.
    """
    # 4.2 disability discrimination
    adverse_action_taken: bool
    adverse_action_type: Optional[AdverseActionType] = None
    adverse_action_reason_documented: Optional[AdverseActionReason] = None
    discriminatory_statements_made: Optional[bool] = None
    comparator_treated_differently: Optional[bool] = None
    evidence_type: Optional[EvidenceType] = "none"

    # 4.3 harassment
    harassment_conduct_occurred: bool
    harassment_severity: Optional[HarassmentSeverity] = None
    harassment_reported_to_employer: Optional[bool] = None
    employer_remedial_action_taken: Optional[bool] = None

    # 4.4 retaliation
    engaged_in_protected_activity: bool
    employer_aware_of_activity: Optional[bool] = None
    causal_nexus_present: Optional[DetermState] = None
    days_between_activity_and_action: Optional[int] = Field(default=None, ge=0)


# ---------------------------------------------------------------------------
# Full / unified input (Module4Input + wrapper input)
# ---------------------------------------------------------------------------

class UnifiedInput(Module4Input):
    """Complete unified input for /assess/full endpoint.
    Includes all module inputs plus wrapper-level field accommodation_theoretically_effective.
    """
    accommodation_theoretically_effective: DetermState
