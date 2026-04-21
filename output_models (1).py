"""
ADA Decision Engine — Output Models
All Pydantic output schemas for all endpoints.
Field definitions derived from ada_unified_output_schema.json v0.1 and module_interface_spec.json v0.1.
"""

from __future__ import annotations
from typing import Any, Dict, List, Literal, Optional
from pydantic import BaseModel


# ---------------------------------------------------------------------------
# Shared literal types (mirrored from input_models for output use)
# ---------------------------------------------------------------------------

DetermState = Literal["yes", "no", "indeterminate"]
RiskLevel = Literal["minimal", "low", "moderate", "high", "critical"]
ComplianceStatus = Literal["compliant", "non_compliant", "indeterminate"]


# ---------------------------------------------------------------------------
# Module 1 Outputs
# ---------------------------------------------------------------------------

class EmployerCoverageOutput(BaseModel):
    """Output for Component 1.1 — Employer Coverage (rule-based).
    Citation: 42 U.S.C. § 12111(5)(A); 29 CFR § 1630.2(e).
    """
    is_covered_employer: bool
    citation: str = "42 U.S.C. § 12111(5)(A); 29 CFR § 1630.2(e)"


class IndividualStatusOutput(BaseModel):
    """Output for Component 1.2 — Individual Status (rule-based).
    Citation: 42 U.S.C. § 12112(a); 29 CFR § 1630.2(f).
    """
    is_covered_individual: bool
    citation: str = "42 U.S.C. § 12112(a); 29 CFR § 1630.2(f)"


class DisabilityDeterminationOutput(BaseModel):
    """Output for Component 1.3 — Disability Determination (standards-based).
    Citation: 42 U.S.C. § 12102; 29 CFR § 1630.2(g),(j).
    """
    has_qualifying_disability: DetermState
    accommodation_rights_attach: bool
    disability_basis: Optional[str]
    factors_for: List[str]
    factors_against: List[str]
    key_uncertainties: List[str]
    citation: str = "42 U.S.C. § 12102; 29 CFR § 1630.2(g),(j)"


class QualifiedIndividualOutput(BaseModel):
    """Output for Component 1.4 — Qualified Individual (standards-based, preliminary).
    Citation: 42 U.S.C. § 12111(8); 29 CFR § 1630.2(m),(n).
    """
    preliminary_qualified_without_accommodation: DetermState
    is_qualified_individual: DetermState  # preliminary only; wrapper resolves final
    factors_for: List[str]
    factors_against: List[str]
    key_uncertainties: List[str]
    citation: str = "42 U.S.C. § 12111(8); 29 CFR § 1630.2(m),(n)"


class Module1Output(BaseModel):
    """Complete output for Module 1: Coverage and Eligibility."""
    employer_coverage: EmployerCoverageOutput
    individual_status: IndividualStatusOutput
    disability_determination: DisabilityDeterminationOutput
    qualified_individual: QualifiedIndividualOutput


# ---------------------------------------------------------------------------
# Module 2 Outputs
# ---------------------------------------------------------------------------

class AccommodationRequestOutput(BaseModel):
    """Output for Component 2.1 — Accommodation Request (rule-based).
    Citation: EEOC Enforcement Guidance No. 915.002.
    """
    accommodation_request_valid: bool
    citation: str = "EEOC Enforcement Guidance No. 915.002"


class UndueHardshipOutput(BaseModel):
    """Output for Component 2.2 — Undue Hardship Analysis (standards-based).
    Citation: 42 U.S.C. § 12111(10); 29 CFR § 1630.2(p).
    """
    undue_hardship_applies: DetermState
    factors_for: List[str]
    factors_against: List[str]
    key_uncertainties: List[str]
    citation: str = "42 U.S.C. § 12111(10); 29 CFR § 1630.2(p)"


class DirectThreatOutput(BaseModel):
    """Output for Component 2.3 — Direct Threat Analysis (standards-based).
    Citation: 42 U.S.C. § 12113(b); 29 CFR § 1630.2(r).
    """
    direct_threat_exists: DetermState
    factors_for: List[str]
    factors_against: List[str]
    key_uncertainties: List[str]
    citation: str = "42 U.S.C. § 12113(b); 29 CFR § 1630.2(r)"


DenialBasis = Literal[
    "not_covered_employer",
    "not_covered_individual",
    "not_disabled",
    "not_qualified",
    "invalid_request",
    "undue_hardship",
    "direct_threat",
]


class AccommodationDeterminationOutput(BaseModel):
    """Output for Component 2.4 — Accommodation Determination (composite).
    Citation: 42 U.S.C. § 12112(b)(5)(A); 29 CFR § 1630.9.
    """
    accommodation_required: DetermState
    denial_basis: Optional[DenialBasis] = None
    citation: str = "42 U.S.C. § 12112(b)(5)(A); 29 CFR § 1630.9"


class Module2Output(BaseModel):
    """Complete output for Module 2: Accommodation Analysis."""
    accommodation_request: AccommodationRequestOutput
    undue_hardship_analysis: UndueHardshipOutput
    direct_threat_analysis: DirectThreatOutput
    accommodation_determination: AccommodationDeterminationOutput


# ---------------------------------------------------------------------------
# Module 3 Outputs
# ---------------------------------------------------------------------------

class InteractiveProcessOutput(BaseModel):
    """Output for Component 3.1 — Interactive Process (hybrid).
    Citation: EEOC Enforcement Guidance No. 915.002; 29 CFR § 1630 Appendix.
    """
    process_mechanically_compliant: bool
    process_quality: DetermState
    interactive_process_compliant: DetermState
    factors_for: List[str]
    factors_against: List[str]
    key_uncertainties: List[str]
    citation: str = "EEOC Enforcement Guidance No. 915.002; 29 CFR § 1630 Appendix"


class MedicalInquiryOutput(BaseModel):
    """Output for Component 3.2 — Medical Inquiry Limitations (rule-based).
    Citation: 42 U.S.C. § 12112(d); 29 CFR § 1630.13, § 1630.14.
    """
    inquiry_permitted: bool
    violation_basis: Optional[str] = None
    citation: str = "42 U.S.C. § 12112(d); 29 CFR § 1630.13, § 1630.14"


class ConfidentialityOutput(BaseModel):
    """Output for Component 3.3 — Confidentiality (rule-based).
    Citation: 42 U.S.C. § 12112(d)(3)(B); 29 CFR § 1630.14(b)(1).
    """
    confidentiality_compliant: bool
    violation_details: Optional[List[str]] = None
    citation: str = "42 U.S.C. § 12112(d)(3)(B); 29 CFR § 1630.14(b)(1)"


class Module3Output(BaseModel):
    """Complete output for Module 3: Employer Obligations."""
    interactive_process: InteractiveProcessOutput
    medical_inquiry_limitations: MedicalInquiryOutput
    confidentiality: ConfidentialityOutput


# ---------------------------------------------------------------------------
# Module 4 Outputs
# ---------------------------------------------------------------------------

class FailureToAccommodateOutput(BaseModel):
    """Output for Component 4.1 — Failure to Accommodate.
    Citation: 42 U.S.C. § 12112(b)(5)(A); 29 CFR § 1630.9.
    """
    elements_met: int
    prima_facie_elements: Dict[str, bool]
    documented_legitimate_denial: bool
    risk_level: RiskLevel
    risk_rationale: str


class DisabilityDiscriminationOutput(BaseModel):
    """Output for Component 4.2 — Disability Discrimination.
    Citation: 42 U.S.C. § 12112(a).
    """
    elements_met: int
    prima_facie_elements: Dict[str, bool]
    risk_level: RiskLevel
    risk_rationale: str


class HarassmentOutput(BaseModel):
    """Output for Component 4.3 — Harassment.
    Citation: 42 U.S.C. § 12112(a); EEOC harassment guidance.
    """
    elements_met: int
    prima_facie_elements: Dict[str, bool]
    risk_level: RiskLevel
    risk_rationale: str


class RetaliationOutput(BaseModel):
    """Output for Component 4.4 — Retaliation.
    Citation: 42 U.S.C. § 12203.
    """
    elements_met: int
    prima_facie_elements: Dict[str, bool]
    proximity_strength: str
    risk_level: RiskLevel
    risk_rationale: str


class OverallViolationRiskOutput(BaseModel):
    """Output for Component 4.5 — Overall Violation Risk.
    Tiebreak order: failure_to_accommodate → disability_discrimination → harassment → retaliation.
    """
    overall_risk_level: RiskLevel
    primary_claim_basis: str
    contributing_claims: List[str]
    component_risk_levels: Dict[str, RiskLevel]
    recommended_actions: List[str]


class Module4Output(BaseModel):
    """Complete output for Module 4: Violation Risk."""
    failure_to_accommodate: FailureToAccommodateOutput
    disability_discrimination: DisabilityDiscriminationOutput
    harassment: HarassmentOutput
    retaliation: RetaliationOutput
    overall_violation_risk: OverallViolationRiskOutput


# ---------------------------------------------------------------------------
# Wrapper output
# ---------------------------------------------------------------------------

class WrapperOutput(BaseModel):
    """Output of the WR composite is_qualified_individual determination (WR-1 through WR-5)."""
    is_qualified_individual: DetermState
    rule_applied: str  # e.g. "WR-1"


# ---------------------------------------------------------------------------
# Unified / full assessment output
# ---------------------------------------------------------------------------

class ModuleOutputs(BaseModel):
    """Container for complete per-module outputs in the unified assessment."""
    ada_coverage_eligibility: Module1Output
    ada_accommodation_analysis: Module2Output
    ada_employer_obligations: Module3Output
    ada_violation_risk: Module4Output


class UnifiedOutput(BaseModel):
    """Full output for /assess/full endpoint.
    Defined by ada_unified_output_schema.json v0.1.
    """
    ada_covered: bool
    has_qualifying_disability: DetermState
    is_qualified_individual: DetermState
    accommodation_required: DetermState
    employer_compliance_status: ComplianceStatus
    violation_risk_level: RiskLevel
    recommended_actions: List[str]
    indeterminate_factors: Dict[str, List[str]]
    module_outputs: ModuleOutputs
