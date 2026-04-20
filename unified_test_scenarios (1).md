# ADA Decision Engine — Unified Test Scenarios

**Engine:** ADA Reasonable Accommodation Decision Engine  
**Wrapper Version:** 0.1  
**Last Updated:** 2026-04-20  
**Scenario Range:** UA-001 through UA-010

---

## UA-001: Full Yes — Covered, Disabled, Qualified Without Accommodation

**Fact Pattern:**  
Greenfield Manufacturing (private employer, 220 employees) employs Maria, an assembly line worker with Type 2 diabetes (actual disability, substantially limits endocrine function). Maria's diabetes is well-managed; she can perform all essential assembly functions without any modification. She requests a small refrigerator at her workstation to store insulin. The employer conducts a good-faith interactive process, approves the request, and processes it promptly. No adverse actions have occurred. No harassment or retaliation claims arise.

**WR Rule Fired:** WR-1 (preliminary_qualified_without_accommodation = yes)

**Structured Unified Input:**
```json
{
  "wrapper_inputs": {
    "accommodation_theoretically_effective": "yes"
  },
  "module_inputs": {
    "module_1_coverage_eligibility": {
      "employer_coverage": {
        "employer_type": "private_employer",
        "employee_count_current_year": 220,
        "employee_count_prior_year": 215,
        "is_us_government": false,
        "is_indian_tribe": false,
        "affects_commerce": true
      },
      "individual_status": {
        "individual_status": "current_employee",
        "individual_employed_by_covered_entity": true
      },
      "disability_determination": {
        "impairment_type": "endocrine",
        "impairment_description": "Type 2 diabetes mellitus",
        "disability_basis_claimed": "actual_disability",
        "major_life_activity_affected": "endocrine_function",
        "limitation_severity": "substantially_limits",
        "mitigating_measures_used": true,
        "mitigating_measures_description": "insulin therapy and glucose monitoring"
      },
      "qualified_individual": {
        "essential_functions_identified": true,
        "can_perform_essential_functions_without_accommodation": "yes",
        "satisfies_skill_experience_requirements": true,
        "job_description_exists": true
      }
    },
    "module_2_accommodation_analysis": {
      "accommodation_request": {
        "accommodation_type_requested": "equipment_modification",
        "accommodation_description": "Small refrigerator at workstation for insulin storage",
        "accommodation_request_date": "2026-03-01",
        "request_made_by": "employee",
        "accommodation_is_for": "performing_job_functions",
        "functional_limitation_identified": true,
        "accommodation_request_in_writing": true,
        "accommodation_previously_denied": false
      },
      "undue_hardship_analysis": {
        "accommodation_gross_cost": 350,
        "tax_credits_available": 0,
        "outside_funding_available": 0,
        "accommodation_frequency": "one_time",
        "facility_annual_revenue": 8500000,
        "facility_employee_count": 220,
        "entity_annual_revenue": 8500000,
        "entity_total_employees": 220,
        "impact_on_operations": "none",
        "impact_on_other_employees": "none",
        "employer_asserts_hardship": false
      },
      "direct_threat_analysis": {
        "direct_threat_claimed": false
      }
    },
    "module_3_employer_obligations": {
      "interactive_process": {
        "employer_initiated_interactive_process": true,
        "interactive_process_steps_completed": ["acknowledged_request", "identified_limitation", "identified_accommodation", "implemented_accommodation"],
        "good_faith_effort_documented": true,
        "process_breakdown_reason": "no_breakdown",
        "response_time_days": 7
      },
      "medical_inquiry_limitations": {
        "employment_stage": "employed",
        "inquiry_type": "request_for_documentation",
        "inquiry_is_job_related": true,
        "inquiry_consistent_with_business_necessity": true,
        "inquiry_triggered_by_accommodation_request": true
      },
      "confidentiality": {
        "medical_information_maintained_separately": true,
        "medical_information_treated_as_confidential": true,
        "disclosure_made": false
      }
    },
    "module_4_violation_risk": {
      "failure_to_accommodate": {
        "employee_interactive_process_participation": "good_faith"
      },
      "disability_discrimination": {
        "adverse_action_taken": false,
        "causal_nexus_present": false
      },
      "harassment": {
        "unwelcome_conduct_occurred": false
      },
      "retaliation": {
        "engaged_in_protected_activity": true,
        "protected_activity_type": "accommodation_request",
        "employer_aware_of_activity": true,
        "adverse_action_taken": false,
        "causal_nexus_present": false
      }
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
R001–R004 (employer coverage), R005–R007 (individual status), R008–R015 (disability determination), R016–R025 (qualified individual preliminary), R026–R030 (accommodation request), R031–R038 (undue hardship), R039–R041 (direct threat / accommodation determination), WR-1, R047–R055 (interactive process), R056–R060 (medical inquiry), R061–R067 (confidentiality), R068–R090 (FTA/discrimination/harassment/retaliation), R091–R110 (overall risk)

---

## UA-002: Not Covered Employer — All Downstream Outputs Short-Circuit

**Fact Pattern:**  
A small family restaurant (private employer, 9 employees in current year, 8 in prior year) receives an accommodation request from a cook with a shoulder injury. The employer is below the 15-employee threshold in both the current and prior years and is therefore not a covered employer under Title I.

**WR Rule Fired:** None (short-circuit at Module 1 — ada_covered = false)

**Structured Unified Input:**
```json
{
  "wrapper_inputs": {
    "accommodation_theoretically_effective": "yes"
  },
  "module_inputs": {
    "module_1_coverage_eligibility": {
      "employer_coverage": {
        "employer_type": "private_employer",
        "employee_count_current_year": 9,
        "employee_count_prior_year": 8,
        "is_us_government": false,
        "is_indian_tribe": false,
        "affects_commerce": true
      },
      "individual_status": {
        "individual_status": "current_employee",
        "individual_employed_by_covered_entity": true
      },
      "disability_determination": {
        "impairment_type": "musculoskeletal",
        "disability_basis_claimed": "actual_disability",
        "major_life_activity_affected": "lifting",
        "limitation_severity": "substantially_limits"
      },
      "qualified_individual": {
        "essential_functions_identified": true,
        "can_perform_essential_functions_without_accommodation": "no",
        "satisfies_skill_experience_requirements": true
      }
    },
    "module_2_accommodation_analysis": {
      "accommodation_request": {
        "accommodation_type_requested": "modified_schedule",
        "accommodation_request_date": "2026-02-10",
        "request_made_by": "employee",
        "accommodation_is_for": "performing_job_functions",
        "functional_limitation_identified": true
      },
      "undue_hardship_analysis": {
        "accommodation_gross_cost": 0,
        "accommodation_frequency": "ongoing",
        "facility_annual_revenue": 420000,
        "facility_employee_count": 9,
        "entity_annual_revenue": 420000,
        "entity_total_employees": 9,
        "impact_on_operations": "minor",
        "impact_on_other_employees": "minor",
        "employer_asserts_hardship": false
      },
      "direct_threat_analysis": {
        "direct_threat_claimed": false
      }
    },
    "module_3_employer_obligations": {
      "interactive_process": {
        "employer_initiated_interactive_process": false,
        "interactive_process_steps_completed": [],
        "good_faith_effort_documented": false,
        "process_breakdown_reason": "no_breakdown"
      },
      "medical_inquiry_limitations": {
        "employment_stage": "employed",
        "inquiry_type": "request_for_documentation",
        "inquiry_is_job_related": true,
        "inquiry_consistent_with_business_necessity": true,
        "inquiry_triggered_by_accommodation_request": true
      },
      "confidentiality": {
        "medical_information_maintained_separately": true,
        "medical_information_treated_as_confidential": true,
        "disclosure_made": false
      }
    },
    "module_4_violation_risk": {
      "failure_to_accommodate": {
        "employee_interactive_process_participation": "good_faith"
      },
      "disability_discrimination": {
        "adverse_action_taken": false,
        "causal_nexus_present": false
      },
      "harassment": {
        "unwelcome_conduct_occurred": false
      },
      "retaliation": {
        "engaged_in_protected_activity": false,
        "adverse_action_taken": false,
        "causal_nexus_present": false
      }
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
  "employer_compliance_status": "non_compliant",
  "violation_risk_level": "minimal",
  "recommended_actions": [],
  "indeterminate_factors": {}
}
```

**Notes:** When ada_covered = false, is_covered_employer = false short-circuits all substantive analyses. accommodation_required = no with denial_basis = not_covered_employer. is_qualified_individual is indeterminate because no WR rule fires (preliminary_qualified_without_accommodation = no; accommodation_required = no but denial_basis is not undue_hardship or direct_threat; WR-5 catch-all fires on upstream not-applicable). employer_compliance_status = non_compliant because is_covered_employer = false means obligations analysis is not applicable, and the engine reflects non-coverage.

**Modules and Rules Exercised:** R001–R004 (employer coverage, short-circuit fires), Module 2 short-circuit (R026, R041), Module 4 short-circuit at R068

---

## UA-003: Disability Indeterminate — Propagates Through Summary Outputs

**Fact Pattern:**  
A retail employee claims a back condition limits her ability to stand for extended periods. Medical documentation is ambiguous — the physician notes "may limit standing" without quantifying duration or severity. The employer disputes that a substantial limitation exists. Disability basis is actual_disability but limitation_severity is uncertain.

**WR Rule Fired:** WR-5 (catch-all — upstream indeterminate prevents resolution)

**Structured Unified Input:**
```json
{
  "wrapper_inputs": {
    "accommodation_theoretically_effective": "yes"
  },
  "module_inputs": {
    "module_1_coverage_eligibility": {
      "employer_coverage": {
        "employer_type": "private_employer",
        "employee_count_current_year": 85,
        "employee_count_prior_year": 82,
        "is_us_government": false,
        "is_indian_tribe": false,
        "affects_commerce": true
      },
      "individual_status": {
        "individual_status": "current_employee",
        "individual_employed_by_covered_entity": true
      },
      "disability_determination": {
        "impairment_type": "musculoskeletal",
        "impairment_description": "Lumbar back condition, unspecified",
        "disability_basis_claimed": "actual_disability",
        "major_life_activity_affected": "standing",
        "limitation_severity": "uncertain",
        "mitigating_measures_used": false
      },
      "qualified_individual": {
        "essential_functions_identified": true,
        "can_perform_essential_functions_without_accommodation": "no",
        "satisfies_skill_experience_requirements": true
      }
    },
    "module_2_accommodation_analysis": {
      "accommodation_request": {
        "accommodation_type_requested": "equipment_modification",
        "accommodation_description": "Anti-fatigue mat and periodic seating",
        "accommodation_request_date": "2026-01-15",
        "request_made_by": "employee",
        "accommodation_is_for": "performing_job_functions",
        "functional_limitation_identified": true
      },
      "undue_hardship_analysis": {
        "accommodation_gross_cost": 200,
        "accommodation_frequency": "one_time",
        "facility_annual_revenue": 3200000,
        "facility_employee_count": 85,
        "entity_annual_revenue": 3200000,
        "entity_total_employees": 85,
        "impact_on_operations": "none",
        "impact_on_other_employees": "none",
        "employer_asserts_hardship": false
      },
      "direct_threat_analysis": {
        "direct_threat_claimed": false
      }
    },
    "module_3_employer_obligations": {
      "interactive_process": {
        "employer_initiated_interactive_process": true,
        "interactive_process_steps_completed": ["acknowledged_request", "requested_documentation"],
        "good_faith_effort_documented": true,
        "process_breakdown_reason": "no_breakdown",
        "response_time_days": 14
      },
      "medical_inquiry_limitations": {
        "employment_stage": "employed",
        "inquiry_type": "request_for_documentation",
        "inquiry_is_job_related": true,
        "inquiry_consistent_with_business_necessity": true,
        "inquiry_triggered_by_accommodation_request": true
      },
      "confidentiality": {
        "medical_information_maintained_separately": true,
        "medical_information_treated_as_confidential": true,
        "disclosure_made": false
      }
    },
    "module_4_violation_risk": {
      "failure_to_accommodate": {
        "employee_interactive_process_participation": "good_faith"
      },
      "disability_discrimination": {
        "adverse_action_taken": false,
        "causal_nexus_present": false
      },
      "harassment": {
        "unwelcome_conduct_occurred": false
      },
      "retaliation": {
        "engaged_in_protected_activity": true,
        "protected_activity_type": "accommodation_request",
        "employer_aware_of_activity": true,
        "adverse_action_taken": false,
        "causal_nexus_present": false
      }
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
  "employer_compliance_status": "compliant",
  "violation_risk_level": "low",
  "recommended_actions": ["Obtain clarifying medical documentation to resolve disability determination before making accommodation decision"],
  "indeterminate_factors": {
    "ada_coverage_eligibility.disability_determination": [
      "Medical documentation insufficient to confirm substantial limitation — physician noted possible limitation without quantifying severity or duration",
      "Employer disputes that back condition substantially limits standing as compared to most people in the general population"
    ],
    "ada_accommodation_analysis.accommodation_determination": [
      "Accommodation analysis indeterminate pending resolution of disability determination"
    ]
  }
}
```

**Modules and Rules Exercised:** R001–R025, R026–R041 (accommodation indeterminate due to upstream), WR-5, R047–R067, R068–R110

---

## UA-004: Qualified Without Accommodation — WR-1 Fires; Accommodation Not Required

**Fact Pattern:**  
A software engineer with well-controlled bipolar disorder (actual disability, substantially limits brain function per se) requests a flexible start time. She can fully perform all essential engineering functions on her current schedule without any modification — the accommodation request is for convenience and wellness, not functional necessity. The accommodation is approved. No adverse actions.

**WR Rule Fired:** WR-1 (preliminary_qualified_without_accommodation = yes)

**Structured Unified Input:**
```json
{
  "wrapper_inputs": {
    "accommodation_theoretically_effective": "yes"
  },
  "module_inputs": {
    "module_1_coverage_eligibility": {
      "employer_coverage": {
        "employer_type": "private_employer",
        "employee_count_current_year": 540,
        "employee_count_prior_year": 510,
        "is_us_government": false,
        "is_indian_tribe": false,
        "affects_commerce": true
      },
      "individual_status": {
        "individual_status": "current_employee",
        "individual_employed_by_covered_entity": true
      },
      "disability_determination": {
        "impairment_type": "mood_disorder",
        "impairment_description": "Bipolar I disorder, well-controlled on medication",
        "disability_basis_claimed": "actual_disability",
        "major_life_activity_affected": "brain_function",
        "limitation_severity": "substantially_limits",
        "mitigating_measures_used": true,
        "mitigating_measures_description": "lithium carbonate and quetiapine"
      },
      "qualified_individual": {
        "essential_functions_identified": true,
        "can_perform_essential_functions_without_accommodation": "yes",
        "satisfies_skill_experience_requirements": true,
        "job_description_exists": true
      }
    },
    "module_2_accommodation_analysis": {
      "accommodation_request": {
        "accommodation_type_requested": "modified_schedule",
        "accommodation_description": "Flexible start time — begin between 9:30 and 10:30 AM instead of 9:00 AM",
        "accommodation_request_date": "2026-02-01",
        "request_made_by": "employee",
        "accommodation_is_for": "performing_job_functions",
        "functional_limitation_identified": true,
        "accommodation_request_in_writing": true
      },
      "undue_hardship_analysis": {
        "accommodation_gross_cost": 0,
        "accommodation_frequency": "ongoing",
        "facility_annual_revenue": 45000000,
        "facility_employee_count": 540,
        "entity_annual_revenue": 45000000,
        "entity_total_employees": 540,
        "impact_on_operations": "none",
        "impact_on_other_employees": "none",
        "employer_asserts_hardship": false
      },
      "direct_threat_analysis": {
        "direct_threat_claimed": false
      }
    },
    "module_3_employer_obligations": {
      "interactive_process": {
        "employer_initiated_interactive_process": true,
        "interactive_process_steps_completed": ["acknowledged_request", "identified_limitation", "identified_accommodation", "implemented_accommodation"],
        "good_faith_effort_documented": true,
        "process_breakdown_reason": "no_breakdown",
        "response_time_days": 5
      },
      "medical_inquiry_limitations": {
        "employment_stage": "employed",
        "inquiry_type": "request_for_documentation",
        "inquiry_is_job_related": true,
        "inquiry_consistent_with_business_necessity": true,
        "inquiry_triggered_by_accommodation_request": true
      },
      "confidentiality": {
        "medical_information_maintained_separately": true,
        "medical_information_treated_as_confidential": true,
        "disclosure_made": false
      }
    },
    "module_4_violation_risk": {
      "failure_to_accommodate": {
        "employee_interactive_process_participation": "good_faith"
      },
      "disability_discrimination": {
        "adverse_action_taken": false,
        "causal_nexus_present": false
      },
      "harassment": {
        "unwelcome_conduct_occurred": false
      },
      "retaliation": {
        "engaged_in_protected_activity": true,
        "protected_activity_type": "accommodation_request",
        "employer_aware_of_activity": true,
        "adverse_action_taken": false,
        "causal_nexus_present": false
      }
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
  "employer_compliance_status": "compliant",
  "violation_risk_level": "minimal",
  "recommended_actions": [],
  "indeterminate_factors": {}
}
```

**Notes:** accommodation_required = no because can_perform_essential_functions_without_accommodation = yes means no accommodation is legally required (though the employer approved it voluntarily). WR-1 fires on preliminary_qualified_without_accommodation = yes regardless of accommodation_required.

**Modules and Rules Exercised:** R001–R025, R026–R041, WR-1, R047–R067, R068–R110

---

## UA-005: Qualified With Accommodation — WR-2 Fires

**Fact Pattern:**  
A warehouse picker with moderate hearing loss cannot perform her essential function of hearing verbal conveyor belt alerts without accommodation. She requests a vibrating wristband alert device ($600 one-time cost). The employer has 3,000 employees and $180M annual revenue. The device is effective and affordable. The employer conducts a good-faith interactive process and provides the accommodation.

**WR Rule Fired:** WR-2 (preliminary_qualified_without_accommodation = no; accommodation_required = yes; accommodation_theoretically_effective = yes)

**Structured Unified Input:**
```json
{
  "wrapper_inputs": {
    "accommodation_theoretically_effective": "yes"
  },
  "module_inputs": {
    "module_1_coverage_eligibility": {
      "employer_coverage": {
        "employer_type": "private_employer",
        "employee_count_current_year": 3000,
        "employee_count_prior_year": 2900,
        "is_us_government": false,
        "is_indian_tribe": false,
        "affects_commerce": true
      },
      "individual_status": {
        "individual_status": "current_employee",
        "individual_employed_by_covered_entity": true
      },
      "disability_determination": {
        "impairment_type": "sensory",
        "impairment_description": "Moderate bilateral sensorineural hearing loss",
        "disability_basis_claimed": "actual_disability",
        "major_life_activity_affected": "hearing",
        "limitation_severity": "substantially_limits",
        "mitigating_measures_used": true,
        "mitigating_measures_description": "hearing aids — do not fully restore hearing in industrial noise environment"
      },
      "qualified_individual": {
        "essential_functions_identified": true,
        "can_perform_essential_functions_without_accommodation": "no",
        "can_perform_with_reasonable_accommodation": "yes",
        "satisfies_skill_experience_requirements": true,
        "job_description_exists": true
      }
    },
    "module_2_accommodation_analysis": {
      "accommodation_request": {
        "accommodation_type_requested": "equipment_modification",
        "accommodation_description": "Vibrating wristband alert device for conveyor alerts",
        "accommodation_request_date": "2026-03-10",
        "request_made_by": "employee",
        "accommodation_is_for": "performing_job_functions",
        "functional_limitation_identified": true,
        "accommodation_request_in_writing": true
      },
      "undue_hardship_analysis": {
        "accommodation_gross_cost": 600,
        "accommodation_frequency": "one_time",
        "facility_annual_revenue": 180000000,
        "facility_employee_count": 3000,
        "entity_annual_revenue": 180000000,
        "entity_total_employees": 3000,
        "impact_on_operations": "none",
        "impact_on_other_employees": "none",
        "employer_asserts_hardship": false
      },
      "direct_threat_analysis": {
        "direct_threat_claimed": false
      }
    },
    "module_3_employer_obligations": {
      "interactive_process": {
        "employer_initiated_interactive_process": true,
        "interactive_process_steps_completed": ["acknowledged_request", "identified_limitation", "consulted_employee", "identified_accommodation", "implemented_accommodation"],
        "good_faith_effort_documented": true,
        "process_breakdown_reason": "no_breakdown",
        "response_time_days": 10
      },
      "medical_inquiry_limitations": {
        "employment_stage": "employed",
        "inquiry_type": "request_for_documentation",
        "inquiry_is_job_related": true,
        "inquiry_consistent_with_business_necessity": true,
        "inquiry_triggered_by_accommodation_request": true
      },
      "confidentiality": {
        "medical_information_maintained_separately": true,
        "medical_information_treated_as_confidential": true,
        "disclosure_made": false
      }
    },
    "module_4_violation_risk": {
      "failure_to_accommodate": {
        "employee_interactive_process_participation": "good_faith"
      },
      "disability_discrimination": {
        "adverse_action_taken": false,
        "causal_nexus_present": false
      },
      "harassment": {
        "unwelcome_conduct_occurred": false
      },
      "retaliation": {
        "engaged_in_protected_activity": true,
        "protected_activity_type": "accommodation_request",
        "employer_aware_of_activity": true,
        "adverse_action_taken": false,
        "causal_nexus_present": false
      }
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

**Modules and Rules Exercised:** R001–R025, R026–R041, WR-2, R047–R067, R068–R110

---

## UA-006: Not Qualified — WR-3 Fires; Denial Basis = Undue Hardship

**Fact Pattern:**  
A concert pianist with severe essential tremor cannot perform as a staff musician without playing piano. There is no effective accommodation that would allow her to play at the required professional level. The employer (a performing arts conservatory, 25 employees) has engaged in good-faith interactive process and documented that no accommodation — including reassignment — is available or effective. The employer establishes undue hardship for the only potentially effective technical accommodation (robotic assistance system, $800,000 ongoing).

**WR Rule Fired:** WR-3 (preliminary_qualified_without_accommodation = no; accommodation_required = no; denial_basis = undue_hardship)

**Structured Unified Input:**
```json
{
  "wrapper_inputs": {
    "accommodation_theoretically_effective": "no"
  },
  "module_inputs": {
    "module_1_coverage_eligibility": {
      "employer_coverage": {
        "employer_type": "private_employer",
        "employee_count_current_year": 25,
        "employee_count_prior_year": 25,
        "is_us_government": false,
        "is_indian_tribe": false,
        "affects_commerce": true
      },
      "individual_status": {
        "individual_status": "current_employee",
        "individual_employed_by_covered_entity": true
      },
      "disability_determination": {
        "impairment_type": "neurological",
        "impairment_description": "Severe essential tremor affecting bilateral fine motor control",
        "disability_basis_claimed": "actual_disability",
        "major_life_activity_affected": "fine_motor_function",
        "limitation_severity": "substantially_limits",
        "mitigating_measures_used": true,
        "mitigating_measures_description": "propranolol — does not adequately control tremor for professional performance"
      },
      "qualified_individual": {
        "essential_functions_identified": true,
        "can_perform_essential_functions_without_accommodation": "no",
        "can_perform_with_reasonable_accommodation": "no",
        "satisfies_skill_experience_requirements": true,
        "job_description_exists": true
      }
    },
    "module_2_accommodation_analysis": {
      "accommodation_request": {
        "accommodation_type_requested": "equipment_modification",
        "accommodation_description": "Robotic piano assistance system",
        "accommodation_request_date": "2025-11-01",
        "request_made_by": "employee",
        "accommodation_is_for": "performing_job_functions",
        "functional_limitation_identified": true,
        "accommodation_request_in_writing": true
      },
      "undue_hardship_analysis": {
        "accommodation_gross_cost": 800000,
        "accommodation_frequency": "ongoing",
        "facility_annual_revenue": 2100000,
        "facility_employee_count": 25,
        "entity_annual_revenue": 2100000,
        "entity_total_employees": 25,
        "impact_on_operations": "severe",
        "impact_on_other_employees": "moderate",
        "employer_asserts_hardship": true,
        "employer_documented_hardship_analysis": true,
        "alternative_accommodation_considered": true
      },
      "direct_threat_analysis": {
        "direct_threat_claimed": false
      }
    },
    "module_3_employer_obligations": {
      "interactive_process": {
        "employer_initiated_interactive_process": true,
        "interactive_process_steps_completed": ["acknowledged_request", "identified_limitation", "consulted_employee", "considered_alternatives", "documented_denial"],
        "good_faith_effort_documented": true,
        "process_breakdown_reason": "no_breakdown",
        "response_time_days": 45
      },
      "medical_inquiry_limitations": {
        "employment_stage": "employed",
        "inquiry_type": "request_for_documentation",
        "inquiry_is_job_related": true,
        "inquiry_consistent_with_business_necessity": true,
        "inquiry_triggered_by_accommodation_request": true
      },
      "confidentiality": {
        "medical_information_maintained_separately": true,
        "medical_information_treated_as_confidential": true,
        "disclosure_made": false
      }
    },
    "module_4_violation_risk": {
      "failure_to_accommodate": {
        "employee_interactive_process_participation": "good_faith"
      },
      "disability_discrimination": {
        "adverse_action_taken": true,
        "adverse_action_type": "termination",
        "causal_nexus_present": true,
        "discriminatory_intent_evidence": false,
        "legitimate_nondiscriminatory_reason_documented": true
      },
      "harassment": {
        "unwelcome_conduct_occurred": false
      },
      "retaliation": {
        "engaged_in_protected_activity": true,
        "protected_activity_type": "accommodation_request",
        "employer_aware_of_activity": true,
        "adverse_action_taken": false,
        "causal_nexus_present": false
      }
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
  "recommended_actions": ["Maintain complete documentation of hardship analysis and good-faith interactive process record in case of EEOC charge"],
  "indeterminate_factors": {}
}
```

**Modules and Rules Exercised:** R001–R025, R026–R041, WR-3, R047–R067, R068–R110

---

## UA-007: Critical Violation Risk — All FTA Elements Present, No Compliant Process

**Fact Pattern:**  
A call center employee with major depressive disorder (actual disability) makes a written accommodation request for a reduced-noise workspace and schedule modification. The employer ignores the request entirely for six weeks, never initiates an interactive process, then terminates the employee for "performance issues" — issues that began after the accommodation need arose. No undue hardship analysis was conducted, no direct threat claimed. The employer has 250 employees.

**WR Rule Fired:** WR-2 (preliminary_qualified_without_accommodation = no; accommodation_required = yes; accommodation_theoretically_effective = yes)

**Structured Unified Input:**
```json
{
  "wrapper_inputs": {
    "accommodation_theoretically_effective": "yes"
  },
  "module_inputs": {
    "module_1_coverage_eligibility": {
      "employer_coverage": {
        "employer_type": "private_employer",
        "employee_count_current_year": 250,
        "employee_count_prior_year": 240,
        "is_us_government": false,
        "is_indian_tribe": false,
        "affects_commerce": true
      },
      "individual_status": {
        "individual_status": "current_employee",
        "individual_employed_by_covered_entity": true
      },
      "disability_determination": {
        "impairment_type": "mood_disorder",
        "impairment_description": "Major depressive disorder, recurrent",
        "disability_basis_claimed": "actual_disability",
        "major_life_activity_affected": "brain_function",
        "limitation_severity": "substantially_limits"
      },
      "qualified_individual": {
        "essential_functions_identified": true,
        "can_perform_essential_functions_without_accommodation": "no",
        "can_perform_with_reasonable_accommodation": "yes",
        "satisfies_skill_experience_requirements": true
      }
    },
    "module_2_accommodation_analysis": {
      "accommodation_request": {
        "accommodation_type_requested": "policy_modification",
        "accommodation_description": "Reduced-noise workspace and modified schedule with later start time",
        "accommodation_request_date": "2026-01-06",
        "request_made_by": "employee",
        "accommodation_is_for": "performing_job_functions",
        "functional_limitation_identified": true,
        "accommodation_request_in_writing": true,
        "accommodation_previously_denied": false
      },
      "undue_hardship_analysis": {
        "accommodation_gross_cost": 0,
        "accommodation_frequency": "ongoing",
        "facility_annual_revenue": 22000000,
        "facility_employee_count": 250,
        "entity_annual_revenue": 22000000,
        "entity_total_employees": 250,
        "impact_on_operations": "minor",
        "impact_on_other_employees": "none",
        "employer_asserts_hardship": false
      },
      "direct_threat_analysis": {
        "direct_threat_claimed": false
      }
    },
    "module_3_employer_obligations": {
      "interactive_process": {
        "employer_initiated_interactive_process": false,
        "interactive_process_steps_completed": [],
        "good_faith_effort_documented": false,
        "process_breakdown_reason": "employer_refused_to_engage",
        "response_time_days": 42
      },
      "medical_inquiry_limitations": {
        "employment_stage": "employed",
        "inquiry_type": "request_for_documentation",
        "inquiry_is_job_related": true,
        "inquiry_consistent_with_business_necessity": true,
        "inquiry_triggered_by_accommodation_request": true
      },
      "confidentiality": {
        "medical_information_maintained_separately": true,
        "medical_information_treated_as_confidential": true,
        "disclosure_made": false
      }
    },
    "module_4_violation_risk": {
      "failure_to_accommodate": {
        "employee_interactive_process_participation": "good_faith",
        "employee_nonparticipation_documented": false
      },
      "disability_discrimination": {
        "adverse_action_taken": true,
        "adverse_action_type": "termination",
        "causal_nexus_present": true,
        "discriminatory_intent_evidence": true,
        "legitimate_nondiscriminatory_reason_documented": false
      },
      "harassment": {
        "unwelcome_conduct_occurred": false
      },
      "retaliation": {
        "engaged_in_protected_activity": true,
        "protected_activity_type": "accommodation_request",
        "employer_aware_of_activity": true,
        "adverse_action_taken": true,
        "causal_nexus_present": true,
        "days_between_activity_and_action": 42
      }
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
    "Immediately engage in good-faith interactive process",
    "Document all accommodation considerations and business rationale",
    "Consult employment counsel regarding EEOC charge exposure",
    "Preserve all communications related to accommodation request and termination decision",
    "Assess reinstatement or settlement posture given strength of FTA and retaliation claims"
  ],
  "indeterminate_factors": {}
}
```

**Modules and Rules Exercised:** R001–R025, R026–R041, WR-2, R047–R067 (non-compliant), R068–R110 (critical FTA, high discrimination, critical retaliation)

---

## UA-008: Employer Non-Compliant — Pre-Offer Inquiry Violation + Confidentiality Breach

**Fact Pattern:**  
A job applicant with epilepsy applies for a marketing analyst position. During the pre-offer interview, the hiring manager asks whether the applicant has any medical conditions that would affect the job. The applicant discloses epilepsy. The employer shares the disclosed information with the applicant's prospective supervisor (not authorized) and with the sales team lead. The applicant is not hired. No accommodation request was made at the pre-offer stage.

**WR Rule Fired:** WR-5 (catch-all — qualified individual status indeterminate for applicant without accommodation request)

**Structured Unified Input:**
```json
{
  "wrapper_inputs": {
    "accommodation_theoretically_effective": "indeterminate"
  },
  "module_inputs": {
    "module_1_coverage_eligibility": {
      "employer_coverage": {
        "employer_type": "private_employer",
        "employee_count_current_year": 180,
        "employee_count_prior_year": 175,
        "is_us_government": false,
        "is_indian_tribe": false,
        "affects_commerce": true
      },
      "individual_status": {
        "individual_status": "job_applicant",
        "individual_employed_by_covered_entity": false
      },
      "disability_determination": {
        "impairment_type": "neurological",
        "impairment_description": "Epilepsy, controlled",
        "disability_basis_claimed": "actual_disability",
        "major_life_activity_affected": "neurological_function",
        "limitation_severity": "substantially_limits"
      },
      "qualified_individual": {
        "essential_functions_identified": true,
        "can_perform_essential_functions_without_accommodation": "yes",
        "satisfies_skill_experience_requirements": true
      }
    },
    "module_2_accommodation_analysis": {
      "accommodation_request": {
        "accommodation_type_requested": "other",
        "accommodation_description": "No accommodation requested at pre-offer stage",
        "accommodation_request_date": "2026-03-15",
        "request_made_by": "employee",
        "accommodation_is_for": "application_process",
        "functional_limitation_identified": false
      },
      "undue_hardship_analysis": {
        "accommodation_gross_cost": 0,
        "accommodation_frequency": "one_time",
        "facility_annual_revenue": 14000000,
        "facility_employee_count": 180,
        "entity_annual_revenue": 14000000,
        "entity_total_employees": 180,
        "impact_on_operations": "none",
        "impact_on_other_employees": "none",
        "employer_asserts_hardship": false
      },
      "direct_threat_analysis": {
        "direct_threat_claimed": false
      }
    },
    "module_3_employer_obligations": {
      "interactive_process": {
        "employer_initiated_interactive_process": false,
        "interactive_process_steps_completed": [],
        "good_faith_effort_documented": false,
        "process_breakdown_reason": "no_breakdown"
      },
      "medical_inquiry_limitations": {
        "employment_stage": "pre_offer",
        "inquiry_type": "disability_related_question",
        "inquiry_is_job_related": false,
        "inquiry_consistent_with_business_necessity": false,
        "inquiry_triggered_by_accommodation_request": false
      },
      "confidentiality": {
        "medical_information_maintained_separately": false,
        "medical_information_treated_as_confidential": false,
        "disclosure_made": true,
        "disclosure_recipient": "unauthorized_party",
        "disclosure_basis": "no_permissible_basis"
      }
    },
    "module_4_violation_risk": {
      "failure_to_accommodate": {
        "employee_interactive_process_participation": "good_faith"
      },
      "disability_discrimination": {
        "adverse_action_taken": true,
        "adverse_action_type": "failure_to_hire",
        "causal_nexus_present": true,
        "discriminatory_intent_evidence": true,
        "legitimate_nondiscriminatory_reason_documented": false
      },
      "harassment": {
        "unwelcome_conduct_occurred": false
      },
      "retaliation": {
        "engaged_in_protected_activity": false,
        "adverse_action_taken": false,
        "causal_nexus_present": false
      }
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
    "Immediately train hiring managers on pre-offer inquiry prohibitions",
    "Implement medical information confidentiality procedures and audit current files",
    "Consult employment counsel regarding exposure from pre-offer inquiry and confidentiality breach",
    "Review hiring decision for discriminatory nexus"
  ],
  "indeterminate_factors": {}
}
```

**Notes:** employer_compliance_status = non_compliant because inquiry_permitted = no (pre-offer disability-related question without exception) AND confidentiality_compliant = no. WR-1 fires (can_perform_essential_functions_without_accommodation = yes).

**Modules and Rules Exercised:** R001–R025, R026–R041, WR-1, R047–R067 (non-compliant on inquiry and confidentiality), R068–R110

---

## UA-009: Maximum Indeterminate — Multiple Modules Produce Indeterminate

**Fact Pattern:**  
An employee with an undiagnosed condition claims disability based on fatigue and cognitive difficulties. Medical documentation is minimal and conflicting. The employer and employee give contradictory accounts of the interactive process. The accommodation requested (permanent telework) may or may not be technically feasible given the job's coordination requirements. Direct threat has been claimed but no individualized assessment was conducted. Disability basis, accommodation feasibility, process quality, and direct threat are all indeterminate.

**WR Rule Fired:** WR-4 (preliminary_qualified_without_accommodation = no; accommodation_required = indeterminate)

**Structured Unified Input:**
```json
{
  "wrapper_inputs": {
    "accommodation_theoretically_effective": "indeterminate"
  },
  "module_inputs": {
    "module_1_coverage_eligibility": {
      "employer_coverage": {
        "employer_type": "private_employer",
        "employee_count_current_year": 120,
        "employee_count_prior_year": 115,
        "is_us_government": false,
        "is_indian_tribe": false,
        "affects_commerce": true
      },
      "individual_status": {
        "individual_status": "current_employee",
        "individual_employed_by_covered_entity": true
      },
      "disability_determination": {
        "impairment_type": "immune",
        "impairment_description": "Undiagnosed condition — fatigue and cognitive symptoms; workup ongoing",
        "disability_basis_claimed": "actual_disability",
        "major_life_activity_affected": "concentrating",
        "limitation_severity": "uncertain"
      },
      "qualified_individual": {
        "essential_functions_identified": true,
        "can_perform_essential_functions_without_accommodation": "no",
        "can_perform_with_reasonable_accommodation": "indeterminate",
        "satisfies_skill_experience_requirements": true
      }
    },
    "module_2_accommodation_analysis": {
      "accommodation_request": {
        "accommodation_type_requested": "telework",
        "accommodation_description": "Permanent full-time telework",
        "accommodation_request_date": "2026-02-15",
        "request_made_by": "employee",
        "accommodation_is_for": "performing_job_functions",
        "functional_limitation_identified": true,
        "accommodation_request_in_writing": true
      },
      "undue_hardship_analysis": {
        "accommodation_gross_cost": 0,
        "accommodation_frequency": "ongoing",
        "facility_annual_revenue": 9500000,
        "facility_employee_count": 120,
        "entity_annual_revenue": 9500000,
        "entity_total_employees": 120,
        "impact_on_operations": "moderate",
        "impact_on_other_employees": "moderate",
        "employer_asserts_hardship": true,
        "employer_documented_hardship_analysis": false,
        "alternative_accommodation_considered": false
      },
      "direct_threat_analysis": {
        "direct_threat_claimed": true,
        "threat_to": "others",
        "individualized_assessment_performed": false,
        "assessment_based_on_current_medical_knowledge": false,
        "objective_evidence_exists": false,
        "assessment_relied_on_stereotypes": true
      }
    },
    "module_3_employer_obligations": {
      "interactive_process": {
        "employer_initiated_interactive_process": true,
        "interactive_process_steps_completed": ["acknowledged_request"],
        "good_faith_effort_documented": false,
        "process_breakdown_reason": "other",
        "process_breakdown_documented": false,
        "response_time_days": 30
      },
      "medical_inquiry_limitations": {
        "employment_stage": "employed",
        "inquiry_type": "request_for_documentation",
        "inquiry_is_job_related": true,
        "inquiry_consistent_with_business_necessity": true,
        "inquiry_triggered_by_accommodation_request": true
      },
      "confidentiality": {
        "medical_information_maintained_separately": true,
        "medical_information_treated_as_confidential": true,
        "disclosure_made": false
      }
    },
    "module_4_violation_risk": {
      "failure_to_accommodate": {
        "employee_interactive_process_participation": "partial"
      },
      "disability_discrimination": {
        "adverse_action_taken": false,
        "causal_nexus_present": false
      },
      "harassment": {
        "unwelcome_conduct_occurred": false
      },
      "retaliation": {
        "engaged_in_protected_activity": true,
        "protected_activity_type": "accommodation_request",
        "employer_aware_of_activity": true,
        "adverse_action_taken": false,
        "causal_nexus_present": false
      }
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
    "Obtain complete medical documentation before making any accommodation decision",
    "Conduct individualized direct threat assessment — stereotypes-based assessment is not legally sufficient",
    "Document good-faith interactive process steps in real time",
    "Consider partial accommodations pending full diagnosis"
  ],
  "indeterminate_factors": {
    "ada_coverage_eligibility.disability_determination": [
      "Diagnosis not yet established — medical workup ongoing",
      "Limitation severity uncertain without completed evaluation",
      "Cannot assess substantial limitation without baseline functional capacity documentation"
    ],
    "ada_accommodation_analysis.undue_hardship_analysis": [
      "Hardship asserted but no documented individualized analysis provided",
      "Impact on operations disputed — employer has not demonstrated specific operational disruption"
    ],
    "ada_accommodation_analysis.direct_threat_analysis": [
      "Direct threat claimed but no individualized assessment was conducted",
      "Assessment relied on stereotypes — legally insufficient basis for direct threat finding",
      "No objective evidence of specific risk to identifiable individuals"
    ],
    "ada_accommodation_analysis.accommodation_determination": [
      "Accommodation analysis indeterminate pending resolution of disability determination, hardship analysis, and direct threat assessment"
    ],
    "ada_employer_obligations.interactive_process": [
      "Process quality disputed — employer and employee accounts conflict on whether employer proposed alternative accommodations",
      "Process steps incomplete — only initial acknowledgment documented"
    ]
  }
}
```

**Modules and Rules Exercised:** R001–R025, R026–R046 (all indeterminate paths), WR-4, R047–R067 (process indeterminate), R068–R110

---

## UA-010: Tiebreak Fires — FTA and Retaliation Both Critical; FTA Wins Tiebreak

**Fact Pattern:**  
A production supervisor with a back condition requiring a sit-stand workstation is denied accommodation with no explanation. The supervisor files an EEOC charge. Within 30 days, the employer terminates the supervisor citing "reorganization" — despite no other supervisors being terminated. All five FTA prima facie elements are satisfied. All four retaliation elements are satisfied with strong temporal proximity. Disability discrimination elements also present (3 of 4). Interactive process was not conducted. No undue hardship or direct threat was established.

**WR Rule Fired:** WR-2 (preliminary_qualified_without_accommodation = no; accommodation_required = yes; accommodation_theoretically_effective = yes)

**Structured Unified Input:**
```json
{
  "wrapper_inputs": {
    "accommodation_theoretically_effective": "yes"
  },
  "module_inputs": {
    "module_1_coverage_eligibility": {
      "employer_coverage": {
        "employer_type": "private_employer",
        "employee_count_current_year": 310,
        "employee_count_prior_year": 295,
        "is_us_government": false,
        "is_indian_tribe": false,
        "affects_commerce": true
      },
      "individual_status": {
        "individual_status": "current_employee",
        "individual_employed_by_covered_entity": true
      },
      "disability_determination": {
        "impairment_type": "musculoskeletal",
        "impairment_description": "Lumbar disc herniation L4-L5 with radiculopathy",
        "disability_basis_claimed": "actual_disability",
        "major_life_activity_affected": "standing",
        "limitation_severity": "substantially_limits"
      },
      "qualified_individual": {
        "essential_functions_identified": true,
        "can_perform_essential_functions_without_accommodation": "no",
        "can_perform_with_reasonable_accommodation": "yes",
        "satisfies_skill_experience_requirements": true,
        "job_description_exists": true
      }
    },
    "module_2_accommodation_analysis": {
      "accommodation_request": {
        "accommodation_type_requested": "equipment_modification",
        "accommodation_description": "Sit-stand workstation",
        "accommodation_request_date": "2026-01-10",
        "request_made_by": "employee",
        "accommodation_is_for": "performing_job_functions",
        "functional_limitation_identified": true,
        "accommodation_request_in_writing": true,
        "accommodation_previously_denied": true
      },
      "undue_hardship_analysis": {
        "accommodation_gross_cost": 1200,
        "accommodation_frequency": "one_time",
        "facility_annual_revenue": 28000000,
        "facility_employee_count": 310,
        "entity_annual_revenue": 28000000,
        "entity_total_employees": 310,
        "impact_on_operations": "none",
        "impact_on_other_employees": "none",
        "employer_asserts_hardship": false
      },
      "direct_threat_analysis": {
        "direct_threat_claimed": false
      }
    },
    "module_3_employer_obligations": {
      "interactive_process": {
        "employer_initiated_interactive_process": false,
        "interactive_process_steps_completed": [],
        "good_faith_effort_documented": false,
        "process_breakdown_reason": "employer_refused_to_engage"
      },
      "medical_inquiry_limitations": {
        "employment_stage": "employed",
        "inquiry_type": "request_for_documentation",
        "inquiry_is_job_related": true,
        "inquiry_consistent_with_business_necessity": true,
        "inquiry_triggered_by_accommodation_request": true
      },
      "confidentiality": {
        "medical_information_maintained_separately": true,
        "medical_information_treated_as_confidential": true,
        "disclosure_made": false
      }
    },
    "module_4_violation_risk": {
      "failure_to_accommodate": {
        "employee_interactive_process_participation": "good_faith",
        "employee_nonparticipation_documented": false
      },
      "disability_discrimination": {
        "adverse_action_taken": true,
        "adverse_action_type": "termination",
        "causal_nexus_present": true,
        "discriminatory_intent_evidence": true,
        "legitimate_nondiscriminatory_reason_documented": false
      },
      "harassment": {
        "unwelcome_conduct_occurred": false
      },
      "retaliation": {
        "engaged_in_protected_activity": true,
        "protected_activity_type": "eeoc_charge",
        "employer_aware_of_activity": true,
        "adverse_action_taken": true,
        "causal_nexus_present": true,
        "days_between_activity_and_action": 28
      }
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
    "Immediately consult employment counsel — EEOC charge is active",
    "Preserve all communications, personnel records, and documentation related to accommodation denial and termination",
    "Assess reinstatement and settlement options given critical FTA and retaliation exposure",
    "Do not make further adverse employment decisions regarding this employee without counsel review",
    "Audit accommodation request handling and interactive process procedures across the organization"
  ],
  "indeterminate_factors": {}
}
```

**Notes — Tiebreak Verification:**  
FTA and retaliation both produce critical risk. Tiebreak order: failure_to_accommodate → disability_discrimination → harassment → retaliation. Result: `primary_claim_basis = "failure_to_accommodate"`, `contributing_claims = ["failure_to_accommodate", "retaliation"]`. Disability discrimination produces high (not critical — legitimate nondiscriminatory reason not documented but intent evidence is present; engine does not produce critical for discrimination without all four elements at maximum). FTA produces critical: all five elements met, interactive_process_compliant = no, no documented legitimate denial.

**Modules and Rules Exercised:** R001–R025, R026–R041, WR-2, R047–R067 (non-compliant interactive process), R068–R110 (critical FTA, high discrimination, critical retaliation, tiebreak R108–R110)
