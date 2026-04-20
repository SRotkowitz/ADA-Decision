# ADA Decision Engine — Unified Test Scenarios

**Engine:** ADA Reasonable Accommodation Decision Engine  
**Wrapper Version:** 0.1  
**Last Updated:** 2026-04-20  
**Coverage:** End-to-end unified assessment — all eight summary output fields  

---

## UA-001: Full Yes — Covered, Disabled, Qualified Without Accommodation

**Fact Pattern:**  
A private employer with 200 employees requests an ergonomic workstation for a current employee with a documented lumbar condition that substantially limits the major life activity of bending. The employee can perform all essential functions of their data entry role without accommodation. A valid accommodation request was made in writing by the employee. The employer engaged in a full interactive process, maintained proper documentation, conducted no pre-offer medical inquiries, and stored all medical information in a confidential file. No adverse action was taken and no harassment or retaliation is alleged. Accommodation cost is $800 one-time with $0 offset against a $2M facility budget.

**WR Rule Fired:** WR-1 (preliminary_qualified_without_accommodation = yes → is_qualified_individual = yes)

**Structured Unified Input:**
```json
{
  "wrapper_inputs": {
    "accommodation_theoretically_effective": "yes"
  },
  "module_inputs": {
    "module_1_coverage_eligibility": {
      "employer_type": "private_employer",
      "total_employees": 200,
      "weeks_with_15_employees": 52,
      "individual_status": "current_employee",
      "disability_basis": "actual_disability",
      "impairment_type": "physical",
      "impairment_description": "Lumbar disc disease with documented limitation in bending and prolonged sitting",
      "major_life_activities_affected": ["bending", "sitting"],
      "substantially_limits": "yes",
      "condition_is_episodic_or_remission": false,
      "condition_duration": "permanent",
      "essential_functions_identified": true,
      "can_perform_essential_functions_without_accommodation": "yes",
      "meets_skill_experience_education_requirements": true
    },
    "module_2_accommodation_analysis": {
      "accommodation_type_requested": "equipment_modification",
      "accommodation_description": "Ergonomic workstation with lumbar-support chair and adjustable-height desk",
      "accommodation_request_date": "2026-03-01",
      "request_made_by": "employee",
      "accommodation_is_for": "performing_job_functions",
      "functional_limitation_identified": true,
      "accommodation_request_in_writing": true,
      "accommodation_previously_denied": false,
      "accommodation_gross_cost": 800,
      "tax_credits_available": 0,
      "outside_funding_available": 0,
      "accommodation_frequency": "one_time",
      "facility_annual_revenue": 2000000,
      "facility_employee_count": 200,
      "entity_annual_revenue": 2000000,
      "entity_total_employees": 200,
      "impact_on_operations": "none",
      "impact_on_other_employees": "none",
      "direct_threat_basis": "none_claimed"
    },
    "module_3_employer_obligations": {
      "interactive_process_initiated": true,
      "interactive_process_steps_completed": ["acknowledged_request", "identified_barriers", "explored_alternatives", "communicated_decision", "documented_process"],
      "employer_good_faith_shown": "yes",
      "process_breakdown_cause": "no_breakdown",
      "process_documented": true,
      "inquiry_stage": "employment",
      "inquiry_type": "documentation_request",
      "inquiry_job_related": true,
      "inquiry_consistent_with_business_necessity": true,
      "medical_information_in_separate_file": true,
      "access_limited_to_authorized_personnel": true,
      "unauthorized_disclosure_occurred": false
    },
    "module_4_violation_risk": {
      "employee_interactive_process_participation": "good_faith",
      "employee_nonparticipation_documented": false,
      "adverse_action_taken": false,
      "harassment_conduct_occurred": false,
      "engaged_in_protected_activity": true,
      "employer_aware_of_activity": true,
      "causal_nexus_present": "no"
    }
  }
}
```

**Expected Unified Summary Output:**
```json
{
  "ada_covered": true,
  "has_qualifying_disability": "yes",
  "is_qualified_individual": "yes",
  "accommodation_required": "yes",
  "employer_compliance_status": "compliant",
  "violation_risk_level": "minimal",
  "recommended_actions": [],
  "indeterminate_factors": {}
}
```

**Modules and Rules Exercised:**  
- R001–R005 (employer coverage), R006–R008 (individual status), R009–R015 (disability determination), R016–R020 (qualified individual)  
- WR-1 (is_qualified_individual composite)  
- R026–R028 (accommodation request), R029–R035 (undue hardship), R036–R040 (direct threat), R041–R046 (accommodation determination)  
- R047–R057 (interactive process), R058–R062 (medical inquiry), R063–R067 (confidentiality)  
- R068–R075 (FTA — 0 elements active; minimal risk), R076–R082 (discrimination — minimal), R083–R089 (harassment — minimal), R090–R095 (retaliation — minimal), R096–R110 (overall — minimal)

---

## UA-002: Not Covered Employer — All Downstream Short-Circuits

**Fact Pattern:**  
A private employer with only 10 employees and 52 qualifying weeks requests a schedule modification for a current employee. The employer has never met the 15-employee threshold in the current or preceding calendar year.

**WR Rule Fired:** None (Module 2 short-circuits at step 1 before wrapper composite executes)

**Structured Unified Input:**
```json
{
  "wrapper_inputs": {
    "accommodation_theoretically_effective": "yes"
  },
  "module_inputs": {
    "module_1_coverage_eligibility": {
      "employer_type": "private_employer",
      "total_employees": 10,
      "weeks_with_15_employees": 0,
      "individual_status": "current_employee",
      "disability_basis": "actual_disability",
      "impairment_type": "mental",
      "major_life_activities_affected": ["concentrating"],
      "substantially_limits": "yes",
      "essential_functions_identified": true,
      "can_perform_essential_functions_without_accommodation": "no",
      "meets_skill_experience_education_requirements": true
    },
    "module_2_accommodation_analysis": {
      "accommodation_type_requested": "modified_schedule",
      "accommodation_request_date": "2026-02-15",
      "request_made_by": "employee",
      "accommodation_is_for": "performing_job_functions",
      "functional_limitation_identified": true,
      "accommodation_gross_cost": 0,
      "accommodation_frequency": "ongoing",
      "facility_annual_revenue": 500000,
      "facility_employee_count": 10,
      "entity_annual_revenue": 500000,
      "entity_total_employees": 10,
      "impact_on_operations": "minor",
      "impact_on_other_employees": "none",
      "direct_threat_basis": "none_claimed"
    },
    "module_3_employer_obligations": {
      "interactive_process_initiated": false,
      "interactive_process_steps_completed": [],
      "employer_good_faith_shown": "no",
      "inquiry_stage": "employment",
      "inquiry_type": "documentation_request",
      "inquiry_job_related": true,
      "inquiry_consistent_with_business_necessity": true,
      "medical_information_in_separate_file": true,
      "access_limited_to_authorized_personnel": true,
      "unauthorized_disclosure_occurred": false
    },
    "module_4_violation_risk": {
      "employee_interactive_process_participation": "good_faith",
      "adverse_action_taken": false,
      "harassment_conduct_occurred": false,
      "engaged_in_protected_activity": false
    }
  }
}
```

**Expected Unified Summary Output:**
```json
{
  "ada_covered": false,
  "has_qualifying_disability": "yes",
  "is_qualified_individual": "indeterminate",
  "accommodation_required": "no",
  "employer_compliance_status": "indeterminate",
  "violation_risk_level": "minimal",
  "recommended_actions": [],
  "indeterminate_factors": {}
}
```

**Modules and Rules Exercised:**  
- R001–R005 (employer not covered — R002 fires), R006–R008 (individual status evaluated), R009–R015 (disability evaluated)  
- R041 (Module 2 short-circuits: not_covered_employer at step 1)  
- R068–R075 (FTA: element 1 not met — minimal risk)

---

## UA-003: Disability Indeterminate — Propagates Through Summary Outputs

**Fact Pattern:**  
A current employee claims a mental health impairment but has provided no medical documentation. The employer is covered (300 employees). It is unclear whether the condition substantially limits a major life activity. The employer has received an accommodation request for telework and has initiated the interactive process, but the disability determination cannot be resolved.

**WR Rule Fired:** WR-5 (upstream indeterminate — preliminary_qualified_without_accommodation indeterminate because disability indeterminate)

**Structured Unified Input:**
```json
{
  "wrapper_inputs": {
    "accommodation_theoretically_effective": "indeterminate"
  },
  "module_inputs": {
    "module_1_coverage_eligibility": {
      "employer_type": "private_employer",
      "total_employees": 300,
      "weeks_with_15_employees": 52,
      "individual_status": "current_employee",
      "disability_basis": "actual_disability",
      "impairment_type": "mental",
      "impairment_description": "Self-reported anxiety; no medical documentation provided",
      "major_life_activities_affected": ["sleeping", "concentrating"],
      "substantially_limits": "indeterminate",
      "condition_duration": "unknown",
      "essential_functions_identified": true,
      "can_perform_essential_functions_without_accommodation": "indeterminate",
      "meets_skill_experience_education_requirements": true
    },
    "module_2_accommodation_analysis": {
      "accommodation_type_requested": "telework",
      "accommodation_request_date": "2026-03-10",
      "request_made_by": "employee",
      "accommodation_is_for": "performing_job_functions",
      "functional_limitation_identified": true,
      "accommodation_gross_cost": 0,
      "accommodation_frequency": "ongoing",
      "facility_annual_revenue": 5000000,
      "facility_employee_count": 300,
      "entity_annual_revenue": 5000000,
      "entity_total_employees": 300,
      "impact_on_operations": "minor",
      "impact_on_other_employees": "none",
      "direct_threat_basis": "none_claimed"
    },
    "module_3_employer_obligations": {
      "interactive_process_initiated": true,
      "interactive_process_steps_completed": ["acknowledged_request", "requested_medical_documentation"],
      "employer_good_faith_shown": "indeterminate",
      "process_breakdown_cause": "unknown",
      "process_documented": false,
      "inquiry_stage": "employment",
      "inquiry_type": "documentation_request",
      "inquiry_job_related": true,
      "inquiry_consistent_with_business_necessity": true,
      "medical_information_in_separate_file": true,
      "access_limited_to_authorized_personnel": true,
      "unauthorized_disclosure_occurred": false
    },
    "module_4_violation_risk": {
      "employee_interactive_process_participation": "partial",
      "adverse_action_taken": false,
      "harassment_conduct_occurred": false,
      "engaged_in_protected_activity": true,
      "causal_nexus_present": "indeterminate"
    }
  }
}
```

**Expected Unified Summary Output:**
```json
{
  "ada_covered": true,
  "has_qualifying_disability": "indeterminate",
  "is_qualified_individual": "indeterminate",
  "accommodation_required": "indeterminate",
  "employer_compliance_status": "indeterminate",
  "violation_risk_level": "low",
  "recommended_actions": ["Obtain medical documentation to resolve disability determination before proceeding", "Continue interactive process in good faith pending documentation"],
  "indeterminate_factors": {
    "ada_coverage_eligibility.disability_determination": [
      "No medical documentation provided to establish substantial limitation",
      "Condition duration unknown — cannot rule out transitory and minor exclusion"
    ],
    "ada_accommodation_analysis.undue_hardship_analysis": [
      "Disability determination unresolved — undue hardship analysis contingent on disability confirmation"
    ],
    "ada_employer_obligations.interactive_process": [
      "Process incomplete — awaiting medical documentation; good faith cannot be fully assessed"
    ]
  }
}
```

**Modules and Rules Exercised:**  
- R009–R015 (disability — indeterminate), R016–R020 (qualified individual — indeterminate)  
- WR-5 (catch-all indeterminate)  
- R041 (accommodation determination — has_qualifying_disability indeterminate → propagates)  
- R047–R057 (interactive process — indeterminate)

---

## UA-004: Qualified Without Accommodation — WR-1 Fires; Accommodation Not Required

**Fact Pattern:**  
A job applicant with a controlled diabetic condition applies for a warehouse position. The employer has 50 employees. The applicant can perform all essential functions without accommodation. No accommodation request has been made. The employer did not conduct any pre-offer medical inquiries. No adverse action taken.

**WR Rule Fired:** WR-1 (preliminary_qualified_without_accommodation = yes)

**Structured Unified Input:**
```json
{
  "wrapper_inputs": {
    "accommodation_theoretically_effective": "yes"
  },
  "module_inputs": {
    "module_1_coverage_eligibility": {
      "employer_type": "private_employer",
      "total_employees": 50,
      "weeks_with_15_employees": 52,
      "individual_status": "job_applicant",
      "disability_basis": "actual_disability",
      "impairment_type": "chronic_disease",
      "impairment_description": "Type 2 diabetes, well-controlled with oral medication",
      "major_life_activities_affected": ["endocrine_function"],
      "substantially_limits": "yes",
      "condition_is_episodic_or_remission": false,
      "condition_duration": "permanent",
      "essential_functions_identified": true,
      "can_perform_essential_functions_without_accommodation": "yes",
      "meets_skill_experience_education_requirements": true
    },
    "module_2_accommodation_analysis": {
      "accommodation_type_requested": "other",
      "accommodation_description": "No accommodation requested",
      "accommodation_request_date": "2026-04-01",
      "request_made_by": "employer_initiated",
      "accommodation_is_for": "application_process",
      "functional_limitation_identified": false,
      "accommodation_gross_cost": 0,
      "accommodation_frequency": "one_time",
      "facility_annual_revenue": 1000000,
      "facility_employee_count": 50,
      "entity_annual_revenue": 1000000,
      "entity_total_employees": 50,
      "impact_on_operations": "none",
      "impact_on_other_employees": "none",
      "direct_threat_basis": "none_claimed"
    },
    "module_3_employer_obligations": {
      "interactive_process_initiated": false,
      "interactive_process_steps_completed": [],
      "employer_good_faith_shown": "yes",
      "inquiry_stage": "pre_offer",
      "inquiry_type": "disability_related_question",
      "inquiry_job_related": false,
      "inquiry_consistent_with_business_necessity": false,
      "medical_information_in_separate_file": true,
      "access_limited_to_authorized_personnel": true,
      "unauthorized_disclosure_occurred": false
    },
    "module_4_violation_risk": {
      "employee_interactive_process_participation": "good_faith",
      "adverse_action_taken": false,
      "harassment_conduct_occurred": false,
      "engaged_in_protected_activity": false
    }
  }
}
```

**Expected Unified Summary Output:**
```json
{
  "ada_covered": true,
  "has_qualifying_disability": "yes",
  "is_qualified_individual": "yes",
  "accommodation_required": "no",
  "employer_compliance_status": "non_compliant",
  "violation_risk_level": "moderate",
  "recommended_actions": [
    "Cease pre-offer disability-related inquiries immediately",
    "Train HR and hiring managers on pre-offer inquiry prohibitions under 42 U.S.C. § 12112(d)(2)",
    "Document remedial steps taken"
  ],
  "indeterminate_factors": {}
}
```

**Notes:** Accommodation not required because functional_limitation_identified = false and WR-1 makes the accommodation question moot as to qualified status. The pre-offer inquiry violation drives non_compliant employer_compliance_status and moderate violation risk (medical inquiry violation absent adverse action).

**Modules and Rules Exercised:**  
- R001–R025 (Module 1 — all pass), WR-1  
- R026 (invalid request — no functional limitation), R041 (short-circuit step 6: invalid_request)  
- R058–R062 (medical inquiry: pre-offer inquiry prohibited → inquiry_permitted = no)  
- R076–R082 (discrimination risk — pre-offer inquiry without adverse action → moderate)

---

## UA-005: Qualified With Accommodation — WR-2 Fires

**Fact Pattern:**  
A current employee with multiple sclerosis cannot perform essential functions without accommodation (frequent fatigue limits standing). The employer has 75 employees. A valid accommodation request for a modified schedule was made. Undue hardship does not apply (net cost $0, schedule adjustment only). Direct threat not asserted. The accommodation would be theoretically effective. The employer conducted a full interactive process. No adverse action or harassment.

**WR Rule Fired:** WR-2 (preliminary_qualified_without_accommodation = no AND accommodation_required = yes AND accommodation_theoretically_effective = yes)

**Structured Unified Input:**
```json
{
  "wrapper_inputs": {
    "accommodation_theoretically_effective": "yes"
  },
  "module_inputs": {
    "module_1_coverage_eligibility": {
      "employer_type": "private_employer",
      "total_employees": 75,
      "weeks_with_15_employees": 52,
      "individual_status": "current_employee",
      "disability_basis": "actual_disability",
      "impairment_type": "neurological",
      "impairment_description": "Multiple sclerosis with relapsing-remitting fatigue affecting sustained standing",
      "major_life_activities_affected": ["standing", "walking"],
      "substantially_limits": "yes",
      "condition_is_episodic_or_remission": true,
      "condition_duration": "permanent",
      "essential_functions_identified": true,
      "can_perform_essential_functions_without_accommodation": "no",
      "meets_skill_experience_education_requirements": true
    },
    "module_2_accommodation_analysis": {
      "accommodation_type_requested": "modified_schedule",
      "accommodation_description": "Allow employee to take two additional 15-minute rest breaks during shift",
      "accommodation_request_date": "2026-02-01",
      "request_made_by": "employee",
      "accommodation_is_for": "performing_job_functions",
      "functional_limitation_identified": true,
      "accommodation_request_in_writing": true,
      "accommodation_previously_denied": false,
      "accommodation_gross_cost": 0,
      "accommodation_frequency": "ongoing",
      "facility_annual_revenue": 3000000,
      "facility_employee_count": 75,
      "entity_annual_revenue": 3000000,
      "entity_total_employees": 75,
      "impact_on_operations": "none",
      "impact_on_other_employees": "none",
      "direct_threat_basis": "none_claimed"
    },
    "module_3_employer_obligations": {
      "interactive_process_initiated": true,
      "interactive_process_steps_completed": ["acknowledged_request", "requested_medical_documentation", "identified_barriers", "explored_alternatives", "communicated_decision", "documented_process"],
      "employer_good_faith_shown": "yes",
      "process_breakdown_cause": "no_breakdown",
      "process_documented": true,
      "inquiry_stage": "employment",
      "inquiry_type": "documentation_request",
      "inquiry_job_related": true,
      "inquiry_consistent_with_business_necessity": true,
      "medical_information_in_separate_file": true,
      "access_limited_to_authorized_personnel": true,
      "unauthorized_disclosure_occurred": false
    },
    "module_4_violation_risk": {
      "employee_interactive_process_participation": "good_faith",
      "adverse_action_taken": false,
      "harassment_conduct_occurred": false,
      "engaged_in_protected_activity": true,
      "causal_nexus_present": "no"
    }
  }
}
```

**Expected Unified Summary Output:**
```json
{
  "ada_covered": true,
  "has_qualifying_disability": "yes",
  "is_qualified_individual": "yes",
  "accommodation_required": "yes",
  "employer_compliance_status": "compliant",
  "violation_risk_level": "minimal",
  "recommended_actions": [],
  "indeterminate_factors": {}
}
```

**Modules and Rules Exercised:**  
- R001–R025 (Module 1), WR-2  
- R026–R046 (Module 2 — all defenses fail; accommodation required)  
- R047–R067 (Module 3 — full compliance)  
- R068–R110 (Module 4 — FTA minimal because accommodation required and process compliant; no other claims)

---

## UA-006: Not Qualified — WR-3 Fires; Denial Basis Undue Hardship

**Fact Pattern:**  
A current employee with a severe back injury cannot perform the essential lifting functions of their warehouse role (lifting 75 lbs regularly) without accommodation. The requested accommodation — full elimination of lifting requirements — would fundamentally alter the position's essential functions and impose significant operational burden on a facility with 20 employees and $400K annual revenue. Undue hardship is established. The employee has been placed on leave.

**WR Rule Fired:** WR-3 (preliminary_qualified_without_accommodation = no AND accommodation_required = no AND denial_basis = undue_hardship → is_qualified_individual = no)

**Structured Unified Input:**
```json
{
  "wrapper_inputs": {
    "accommodation_theoretically_effective": "no"
  },
  "module_inputs": {
    "module_1_coverage_eligibility": {
      "employer_type": "private_employer",
      "total_employees": 20,
      "weeks_with_15_employees": 52,
      "individual_status": "current_employee",
      "disability_basis": "actual_disability",
      "impairment_type": "physical",
      "impairment_description": "Severe lumbar disc herniation — cannot lift more than 10 lbs",
      "major_life_activities_affected": ["lifting", "bending"],
      "substantially_limits": "yes",
      "condition_duration": "more_than_six_months",
      "essential_functions_identified": true,
      "can_perform_essential_functions_without_accommodation": "no",
      "meets_skill_experience_education_requirements": true
    },
    "module_2_accommodation_analysis": {
      "accommodation_type_requested": "job_restructuring",
      "accommodation_description": "Eliminate all lifting requirements from warehouse associate position",
      "accommodation_request_date": "2026-01-15",
      "request_made_by": "employee",
      "accommodation_is_for": "performing_job_functions",
      "functional_limitation_identified": true,
      "accommodation_gross_cost": 45000,
      "accommodation_frequency": "ongoing",
      "facility_annual_revenue": 400000,
      "facility_employee_count": 20,
      "entity_annual_revenue": 400000,
      "entity_total_employees": 20,
      "impact_on_operations": "severe",
      "impact_on_other_employees": "significant",
      "direct_threat_basis": "none_claimed"
    },
    "module_3_employer_obligations": {
      "interactive_process_initiated": true,
      "interactive_process_steps_completed": ["acknowledged_request", "identified_barriers", "explored_alternatives", "communicated_decision", "documented_process"],
      "employer_good_faith_shown": "yes",
      "process_breakdown_cause": "no_breakdown",
      "process_documented": true,
      "inquiry_stage": "employment",
      "inquiry_type": "documentation_request",
      "inquiry_job_related": true,
      "inquiry_consistent_with_business_necessity": true,
      "medical_information_in_separate_file": true,
      "access_limited_to_authorized_personnel": true,
      "unauthorized_disclosure_occurred": false
    },
    "module_4_violation_risk": {
      "employee_interactive_process_participation": "good_faith",
      "adverse_action_taken": false,
      "harassment_conduct_occurred": false,
      "engaged_in_protected_activity": true,
      "causal_nexus_present": "no"
    }
  }
}
```

**Expected Unified Summary Output:**
```json
{
  "ada_covered": true,
  "has_qualifying_disability": "yes",
  "is_qualified_individual": "no",
  "accommodation_required": "no",
  "employer_compliance_status": "compliant",
  "violation_risk_level": "low",
  "recommended_actions": [
    "Document the undue hardship analysis thoroughly",
    "Explore whether reassignment to a vacant position is available before making an adverse employment decision"
  ],
  "indeterminate_factors": {}
}
```

**Modules and Rules Exercised:**  
- R001–R025 (Module 1), WR-3  
- R029–R035 (undue hardship — established), R041 (denial_basis = undue_hardship)  
- R047–R067 (Module 3 — compliant)  
- R068–R075 (FTA — elements 3 and 5 not met due to not_qualified + undue_hardship defense → low)

---

## UA-007: Critical Violation Risk — All FTA Elements Present, Interactive Process Non-Compliant

**Fact Pattern:**  
A current employee with a documented physical disability makes a valid accommodation request. The employer is covered (150 employees). All five FTA prima facie elements are present: covered employer, qualifying disability (yes), qualified individual (yes, WR-1 fires), valid request, accommodation required. The employer never initiated the interactive process (bad faith), denied the accommodation without documented basis, then terminated the employee three weeks after the accommodation request was made. Retaliation nexus is strong.

**WR Rule Fired:** WR-1 (preliminary_qualified_without_accommodation = yes)

**Structured Unified Input:**
```json
{
  "wrapper_inputs": {
    "accommodation_theoretically_effective": "yes"
  },
  "module_inputs": {
    "module_1_coverage_eligibility": {
      "employer_type": "private_employer",
      "total_employees": 150,
      "weeks_with_15_employees": 52,
      "individual_status": "current_employee",
      "disability_basis": "actual_disability",
      "impairment_type": "physical",
      "major_life_activities_affected": ["walking"],
      "substantially_limits": "yes",
      "condition_duration": "permanent",
      "essential_functions_identified": true,
      "can_perform_essential_functions_without_accommodation": "yes",
      "meets_skill_experience_education_requirements": true
    },
    "module_2_accommodation_analysis": {
      "accommodation_type_requested": "facility_access",
      "accommodation_description": "Reserved accessible parking space near building entrance",
      "accommodation_request_date": "2026-03-01",
      "request_made_by": "employee",
      "accommodation_is_for": "performing_job_functions",
      "functional_limitation_identified": true,
      "accommodation_request_in_writing": true,
      "accommodation_previously_denied": false,
      "accommodation_gross_cost": 200,
      "accommodation_frequency": "one_time",
      "facility_annual_revenue": 8000000,
      "facility_employee_count": 150,
      "entity_annual_revenue": 8000000,
      "entity_total_employees": 150,
      "impact_on_operations": "none",
      "impact_on_other_employees": "none",
      "direct_threat_basis": "none_claimed"
    },
    "module_3_employer_obligations": {
      "interactive_process_initiated": false,
      "interactive_process_steps_completed": [],
      "employer_good_faith_shown": "no",
      "process_breakdown_cause": "employer_failure",
      "process_documented": false,
      "inquiry_stage": "employment",
      "inquiry_type": "documentation_request",
      "inquiry_job_related": true,
      "inquiry_consistent_with_business_necessity": true,
      "medical_information_in_separate_file": true,
      "access_limited_to_authorized_personnel": true,
      "unauthorized_disclosure_occurred": false
    },
    "module_4_violation_risk": {
      "employee_interactive_process_participation": "good_faith",
      "adverse_action_taken": true,
      "adverse_action_type": "termination",
      "adverse_action_reason_documented": "undocumented",
      "discriminatory_statements_made": true,
      "comparator_treated_differently": true,
      "harassment_conduct_occurred": false,
      "engaged_in_protected_activity": true,
      "employer_aware_of_activity": true,
      "causal_nexus_present": "yes",
      "days_between_activity_and_action": 21
    }
  }
}
```

**Expected Unified Summary Output:**
```json
{
  "ada_covered": true,
  "has_qualifying_disability": "yes",
  "is_qualified_individual": "yes",
  "accommodation_required": "yes",
  "employer_compliance_status": "non_compliant",
  "violation_risk_level": "critical",
  "recommended_actions": [
    "Engage employment counsel immediately",
    "Preserve all documentation related to the accommodation request, interactive process, and termination decision",
    "Assess reinstatement or other equitable relief as part of any resolution strategy",
    "Conduct organization-wide ADA compliance training",
    "Review and revise accommodation request and interactive process procedures"
  ],
  "indeterminate_factors": {}
}
```

**Modules and Rules Exercised:**  
- R001–R025 (all pass), WR-1  
- R026–R046 (accommodation required — all defenses fail)  
- R047–R057 (interactive process: not initiated → non_compliant), R058–R067 (inquiry and confidentiality compliant)  
- R068–R075 (FTA: all 5 elements present, process non_compliant, no employee nonparticipation → critical)  
- R076–R082 (discrimination: covered, disabled, adverse action, statements → critical)  
- R090–R095 (retaliation: all 4 elements, 21-day proximity = strong → critical)  
- R096–R110 (overall: FTA and discrimination and retaliation all critical → tiebreak → failure_to_accommodate primary)

---

## UA-008: Employer Non-Compliant — Pre-Offer Inquiry + Confidentiality Breach

**Fact Pattern:**  
A private employer with 40 employees conducted disability-related questions at a pre-offer interview. After a conditional offer was extended, the employer shared the applicant's medical information with the applicant's prospective direct supervisor and a coworker (unauthorized disclosure). No accommodation was requested. No adverse action taken yet.

**WR Rule Fired:** WR-1 (can perform without accommodation = yes, assuming standard qualified status)

**Structured Unified Input:**
```json
{
  "wrapper_inputs": {
    "accommodation_theoretically_effective": "yes"
  },
  "module_inputs": {
    "module_1_coverage_eligibility": {
      "employer_type": "private_employer",
      "total_employees": 40,
      "weeks_with_15_employees": 52,
      "individual_status": "job_applicant",
      "disability_basis": "actual_disability",
      "impairment_type": "mental",
      "major_life_activities_affected": ["thinking"],
      "substantially_limits": "yes",
      "condition_duration": "permanent",
      "essential_functions_identified": true,
      "can_perform_essential_functions_without_accommodation": "yes",
      "meets_skill_experience_education_requirements": true
    },
    "module_2_accommodation_analysis": {
      "accommodation_type_requested": "other",
      "accommodation_description": "No accommodation requested",
      "accommodation_request_date": "2026-03-20",
      "request_made_by": "employer_initiated",
      "accommodation_is_for": "application_process",
      "functional_limitation_identified": false,
      "accommodation_gross_cost": 0,
      "accommodation_frequency": "one_time",
      "facility_annual_revenue": 1500000,
      "facility_employee_count": 40,
      "entity_annual_revenue": 1500000,
      "entity_total_employees": 40,
      "impact_on_operations": "none",
      "impact_on_other_employees": "none",
      "direct_threat_basis": "none_claimed"
    },
    "module_3_employer_obligations": {
      "interactive_process_initiated": false,
      "interactive_process_steps_completed": [],
      "employer_good_faith_shown": "yes",
      "inquiry_stage": "pre_offer",
      "inquiry_type": "disability_related_question",
      "inquiry_job_related": false,
      "inquiry_consistent_with_business_necessity": false,
      "medical_information_in_separate_file": false,
      "access_limited_to_authorized_personnel": false,
      "unauthorized_disclosure_occurred": true
    },
    "module_4_violation_risk": {
      "employee_interactive_process_participation": "good_faith",
      "adverse_action_taken": false,
      "harassment_conduct_occurred": false,
      "engaged_in_protected_activity": false
    }
  }
}
```

**Expected Unified Summary Output:**
```json
{
  "ada_covered": true,
  "has_qualifying_disability": "yes",
  "is_qualified_individual": "yes",
  "accommodation_required": "no",
  "employer_compliance_status": "non_compliant",
  "violation_risk_level": "high",
  "recommended_actions": [
    "Immediately cease pre-offer disability inquiries",
    "Establish confidential medical records procedures separating medical files from personnel files",
    "Train all personnel with access to medical information on disclosure prohibitions",
    "Consult employment counsel regarding remediation"
  ],
  "indeterminate_factors": {}
}
```

**Modules and Rules Exercised:**  
- R001–R025 (all pass), WR-1  
- R026 (invalid request — no functional limitation), R041 (short-circuit: invalid_request)  
- R058–R062 (pre-offer inquiry: inquiry_permitted = no)  
- R063–R067 (confidentiality: confidentiality_compliant = no)  
- R076–R082 (discrimination: pre-offer inquiry violation, unauthorized disclosure, no adverse action → high)

---

## UA-009: Maximum Indeterminate — All Three Indeterminate Factors Populated

**Fact Pattern:**  
A current employee at a covered employer (25 employees) reports a possible mental health condition but has provided no documentation. The employer has received an informal verbal request for schedule flexibility. The employer has started an interactive process but it is unclear whether the employer acted in good faith or whether the process was adequate. Disability is indeterminate; accommodation analysis is indeterminate; interactive process compliance is indeterminate. No adverse action taken. No clear retaliation nexus.

**WR Rule Fired:** WR-5 (catch-all — preliminary_qualified_without_accommodation = indeterminate)

**Structured Unified Input:**
```json
{
  "wrapper_inputs": {
    "accommodation_theoretically_effective": "indeterminate"
  },
  "module_inputs": {
    "module_1_coverage_eligibility": {
      "employer_type": "private_employer",
      "total_employees": 25,
      "weeks_with_15_employees": 52,
      "individual_status": "current_employee",
      "disability_basis": "actual_disability",
      "impairment_type": "mental",
      "impairment_description": "Employee reports difficulty with focus and sleep but has not provided any medical records",
      "major_life_activities_affected": ["sleeping", "concentrating"],
      "substantially_limits": "indeterminate",
      "condition_duration": "unknown",
      "essential_functions_identified": true,
      "can_perform_essential_functions_without_accommodation": "indeterminate",
      "meets_skill_experience_education_requirements": true
    },
    "module_2_accommodation_analysis": {
      "accommodation_type_requested": "modified_schedule",
      "accommodation_description": "Verbal request for occasional late starts",
      "accommodation_request_date": "2026-04-01",
      "request_made_by": "employee",
      "accommodation_is_for": "performing_job_functions",
      "functional_limitation_identified": true,
      "accommodation_request_in_writing": false,
      "accommodation_gross_cost": 0,
      "accommodation_frequency": "occasional",
      "facility_annual_revenue": 800000,
      "facility_employee_count": 25,
      "entity_annual_revenue": 800000,
      "entity_total_employees": 25,
      "impact_on_operations": "minor",
      "impact_on_other_employees": "minor",
      "direct_threat_basis": "none_claimed"
    },
    "module_3_employer_obligations": {
      "interactive_process_initiated": true,
      "interactive_process_steps_completed": ["acknowledged_request"],
      "employer_good_faith_shown": "indeterminate",
      "process_breakdown_cause": "unknown",
      "process_documented": false,
      "inquiry_stage": "employment",
      "inquiry_type": "documentation_request",
      "inquiry_job_related": true,
      "inquiry_consistent_with_business_necessity": true,
      "medical_information_in_separate_file": true,
      "access_limited_to_authorized_personnel": true,
      "unauthorized_disclosure_occurred": false
    },
    "module_4_violation_risk": {
      "employee_interactive_process_participation": "partial",
      "adverse_action_taken": false,
      "harassment_conduct_occurred": false,
      "engaged_in_protected_activity": true,
      "causal_nexus_present": "indeterminate"
    }
  }
}
```

**Expected Unified Summary Output:**
```json
{
  "ada_covered": true,
  "has_qualifying_disability": "indeterminate",
  "is_qualified_individual": "indeterminate",
  "accommodation_required": "indeterminate",
  "employer_compliance_status": "indeterminate",
  "violation_risk_level": "moderate",
  "recommended_actions": [
    "Request medical documentation to resolve disability determination",
    "Continue interactive process and document all steps taken"
  ],
  "indeterminate_factors": {
    "ada_coverage_eligibility.disability_determination": [
      "No medical documentation provided to establish substantial limitation of a major life activity",
      "Condition duration unknown — transitory and minor exclusion cannot be ruled out",
      "Impairment categorization requires medical verification"
    ],
    "ada_coverage_eligibility.qualified_individual": [
      "Disability determination unresolved — cannot determine whether individual can perform essential functions without accommodation"
    ],
    "ada_accommodation_analysis.undue_hardship_analysis": [
      "Disability unconfirmed — undue hardship analysis contingent on establishing ADA coverage"
    ],
    "ada_accommodation_analysis.accommodation_determination": [
      "Multiple upstream values indeterminate — accommodation obligation cannot be resolved"
    ],
    "ada_employer_obligations.interactive_process": [
      "Interactive process initiated but incomplete — good faith cannot be fully assessed",
      "Absence of contemporaneous documentation prevents process quality determination"
    ]
  }
}
```

**Modules and Rules Exercised:**  
- R009–R015 (disability — indeterminate), R016–R020 (qualified individual — indeterminate)  
- WR-5 (catch-all)  
- R041 (accommodation — indeterminate propagation)  
- R047–R057 (interactive process — indeterminate)  
- R068–R075 (FTA — elements 2 and 3 unresolved → moderate base)

---

## UA-010: Tiebreak Fires — FTA and Retaliation Both Critical

**Fact Pattern:**  
A current employee with a qualifying physical disability (wheelchair user) made a valid, written accommodation request for a ramp installation. All five FTA prima facie elements are present. The employer conducted no interactive process and denied the accommodation. The employer then terminated the employee 14 days after the request. No direct threat or undue hardship is documented. Harassing conduct was minor and isolated (no harassment risk elevation). The termination proximate to the accommodation request creates strong retaliation nexus.

**WR Rule Fired:** WR-1 (qualified without accommodation for non-mobility essential functions)

**Structured Unified Input:**
```json
{
  "wrapper_inputs": {
    "accommodation_theoretically_effective": "yes"
  },
  "module_inputs": {
    "module_1_coverage_eligibility": {
      "employer_type": "private_employer",
      "total_employees": 60,
      "weeks_with_15_employees": 52,
      "individual_status": "current_employee",
      "disability_basis": "actual_disability",
      "impairment_type": "physical",
      "impairment_description": "Paraplegia — uses wheelchair; can perform all desk-based essential functions",
      "major_life_activities_affected": ["walking", "standing"],
      "substantially_limits": "yes",
      "condition_duration": "permanent",
      "essential_functions_identified": true,
      "can_perform_essential_functions_without_accommodation": "yes",
      "meets_skill_experience_education_requirements": true
    },
    "module_2_accommodation_analysis": {
      "accommodation_type_requested": "facility_access",
      "accommodation_description": "Ramp installation at building entrance to provide wheelchair access",
      "accommodation_request_date": "2026-03-15",
      "request_made_by": "employee",
      "accommodation_is_for": "performing_job_functions",
      "functional_limitation_identified": true,
      "accommodation_request_in_writing": true,
      "accommodation_previously_denied": false,
      "accommodation_gross_cost": 8000,
      "accommodation_frequency": "one_time",
      "facility_annual_revenue": 4000000,
      "facility_employee_count": 60,
      "entity_annual_revenue": 4000000,
      "entity_total_employees": 60,
      "impact_on_operations": "none",
      "impact_on_other_employees": "none",
      "direct_threat_basis": "none_claimed"
    },
    "module_3_employer_obligations": {
      "interactive_process_initiated": false,
      "interactive_process_steps_completed": [],
      "employer_good_faith_shown": "no",
      "process_breakdown_cause": "employer_failure",
      "process_documented": false,
      "inquiry_stage": "employment",
      "inquiry_type": "documentation_request",
      "inquiry_job_related": true,
      "inquiry_consistent_with_business_necessity": true,
      "medical_information_in_separate_file": true,
      "access_limited_to_authorized_personnel": true,
      "unauthorized_disclosure_occurred": false
    },
    "module_4_violation_risk": {
      "employee_interactive_process_participation": "good_faith",
      "adverse_action_taken": true,
      "adverse_action_type": "termination",
      "adverse_action_reason_documented": "undocumented",
      "discriminatory_statements_made": false,
      "comparator_treated_differently": false,
      "harassment_conduct_occurred": true,
      "harassment_severity": "isolated_minor",
      "harassment_reported_to_employer": false,
      "employer_remedial_action_taken": false,
      "engaged_in_protected_activity": true,
      "employer_aware_of_activity": true,
      "causal_nexus_present": "yes",
      "days_between_activity_and_action": 14
    }
  }
}
```

**Expected Unified Summary Output:**
```json
{
  "ada_covered": true,
  "has_qualifying_disability": "yes",
  "is_qualified_individual": "yes",
  "accommodation_required": "yes",
  "employer_compliance_status": "non_compliant",
  "violation_risk_level": "critical",
  "recommended_actions": [
    "Engage employment counsel immediately",
    "Preserve all records relating to accommodation request, denial, and termination",
    "Assess equitable remedies including reinstatement",
    "Implement ADA accommodation procedures with mandatory management training"
  ],
  "indeterminate_factors": {}
}
```

**Tiebreak Result:**  
- FTA risk level: critical (all 5 elements, process non-compliant, no defense)  
- Disability discrimination: moderate (covered, disabled, adverse action, but no discriminatory statements or comparator evidence)  
- Harassment risk level: low (isolated minor, unreported)  
- Retaliation risk level: critical (all 4 elements, 14-day proximity = strong)  
- Overall: critical; `primary_claim_basis = "failure_to_accommodate"`; `contributing_claims = ["failure_to_accommodate", "retaliation"]`

**Modules and Rules Exercised:**  
- R001–R025 (all pass), WR-1  
- R026–R046 (accommodation required, no defenses)  
- R047–R057 (interactive process non_compliant)  
- R068–R075 (FTA: all 5 elements, process non_compliant → critical)  
- R083–R089 (harassment: isolated minor → low)  
- R090–R095 (retaliation: all 4 elements, 14 days = strong proximity → critical)  
- R096–R110 (overall: FTA and retaliation both critical → tiebreak → FTA primary)
