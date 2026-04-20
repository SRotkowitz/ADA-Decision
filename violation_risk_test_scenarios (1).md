# ADA Violation Risk — Module 4 Test Scenarios

**Module:** ada_violation_risk  
**Version:** 0.1  
**Last Updated:** 2026-04-20  
**Scenario Count:** 8  
**Risk Levels Covered:** minimal, low, moderate, high (×2), critical (×2)

---

## VR-001 — Critical: All FTA Elements, Bad-Faith Process, No Legitimate Denial

### Fact Pattern

Maria, a warehouse employee, has Type 1 diabetes (a documented actual disability). She asked her supervisor in writing for a modified break schedule to manage her blood sugar. The employer ignored the request for six weeks, never initiated the interactive process, and ultimately terminated Maria for "attendance issues" that were directly caused by her unmanaged condition. The employer has no documented undue hardship or direct threat analysis. Maria participated fully in every meeting the employer belatedly attempted. There is no adverse action in the discrimination or retaliation components of this scenario (the termination is being analyzed only under FTA and separately in VR-005). No harassment conduct is alleged.

### Legal Analysis

- R068: All five FTA prima facie elements met (covered employer: yes; qualifying disability: yes — actual disability established; qualified individual: yes — she could perform the job with accommodation; valid accommodation request: yes — written request to supervisor satisfies the no-magic-words standard under EEOC Guidance § 1; accommodation required but not provided: yes — modified break schedule is a reasonable accommodation, denied without analysis).
- R069: 5 elements present + interactive_process_compliant = no + documented_legitimate_denial = false → critical pre-weighting.
- R077: Employee participation was good_faith → no downward shift. Final FTA risk: critical.
- R085: Only 1 harassment element met (protected class) → R090 fires → harassment: minimal.
- R078: DD elements: protected class yes, qualified yes, adverse action (termination) yes, causal nexus: this scenario stipulates discriminatory_intent_evidence = none and legitimate_nondiscriminatory_reason_documented = true for the termination → R084: DD elements < 2 met (causal nexus not established) → minimal. NOTE: in this scenario we stipulate causal_nexus_present = no to isolate FTA as the driver.
- R091: Retaliation elements: no protected activity alleged → R103: minimal.
- R104/R105: Maximum = critical. Only contributing claim = failure_to_accommodate. Primary claim basis = failure_to_accommodate.
- R106: Recommended actions for critical.

### Structured Input

```json
{
  "dependency_inputs": {
    "is_covered_employer": true,
    "has_qualifying_disability": "yes",
    "is_covered_individual_with_disability": true,
    "is_qualified_individual": "yes",
    "accommodation_request_valid": true,
    "accommodation_required": "yes",
    "interactive_process_compliant": "no",
    "undue_hardship_applies": "no",
    "direct_threat_exists": "no"
  },
  "components": {
    "failure_to_accommodate": {
      "employee_interactive_process_participation": "good_faith",
      "employee_nonparticipation_documented": false
    },
    "disability_discrimination": {
      "adverse_action_taken": false,
      "causal_nexus_present": "no",
      "discriminatory_intent_evidence": "none",
      "legitimate_nondiscriminatory_reason_documented": false
    },
    "harassment": {
      "unwelcome_conduct_occurred": false,
      "conduct_severity": "isolated_minor",
      "employer_knew_or_should_have_known": false
    },
    "retaliation": {
      "engaged_in_protected_activity": false,
      "employer_aware_of_activity": false,
      "adverse_action_taken": false,
      "causal_nexus_present": "no",
      "days_between_activity_and_action": null
    }
  }
}
```

### Expected Output

```json
{
  "components": {
    "failure_to_accommodate": {
      "fta_element_1_met": true,
      "fta_element_2_met": true,
      "fta_element_3_met": true,
      "fta_element_4_met": true,
      "fta_element_5_met": true,
      "prima_facie_elements_present": 5,
      "documented_legitimate_denial": false,
      "risk_level_pre_weighting": "critical",
      "employee_participation_shift_applied": false,
      "fta_risk_level": "critical"
    },
    "disability_discrimination": {
      "dd_element_1_met": true,
      "dd_element_2_met": true,
      "dd_element_3_met": false,
      "dd_element_4_met": false,
      "discrimination_elements_present": 2,
      "discrimination_risk_level": "low"
    },
    "harassment": {
      "harassment_element_1_met": true,
      "harassment_element_2_met": false,
      "harassment_element_3_met": false,
      "harassment_element_4_met": false,
      "harassment_elements_present": 1,
      "harassment_risk_level": "minimal"
    },
    "retaliation": {
      "retaliation_element_1_met": false,
      "retaliation_element_2_met": false,
      "retaliation_element_3_met": false,
      "retaliation_element_4_met": false,
      "retaliation_elements_present": 0,
      "proximity_strength": "not_provided",
      "retaliation_risk_level": "minimal"
    }
  },
  "overall_violation_risk": {
    "component_risk_levels": {
      "failure_to_accommodate": "critical",
      "disability_discrimination": "low",
      "harassment": "minimal",
      "retaliation": "minimal"
    },
    "overall_risk_level": "critical",
    "primary_claim_basis": "failure_to_accommodate",
    "contributing_claims": ["failure_to_accommodate"],
    "reasoning": "Overall risk level is critical driven by failure to accommodate. All five prima facie elements are present, the employer did not conduct a compliant interactive process, and no documented legitimate denial exists.",
    "recommended_actions": [
      "Engage employment counsel immediately — do not take further adverse action without legal review.",
      "Preserve all documentation related to the accommodation request, interactive process, adverse action, and any complaints.",
      "Conduct an internal investigation to assess whether the conduct can be remediated prior to an EEOC charge.",
      "Evaluate whether corrective action (accommodation provision, reinstatement, or similar) can reduce exposure.",
      "Review and update ADA reasonable accommodation policies and training."
    ]
  }
}
```

### Rules Fired

R068, R069, R077, R078, R083, R085, R090, R091, R096, R103, R104, R105, R106

---

## VR-002 — High: All FTA Elements, Interactive Process Indeterminate, No Legitimate Denial

### Fact Pattern

James, a call center employee, has major depressive disorder (actual disability). He requested a schedule modification to attend weekly therapy appointments. The employer engaged in some back-and-forth but the documentation is incomplete — it is unclear whether the employer followed through in good faith or stalled. There is no documented undue hardship or direct threat analysis. The accommodation was ultimately denied without a documented reason. James participated in all meetings. No discrimination, harassment, or retaliation allegations exist in this scenario.

### Legal Analysis

- R068: All five FTA elements met.
- R070: 5 elements + interactive_process_compliant = indeterminate + no documented legitimate denial → high pre-weighting. Indeterminate is not equivalent to non-compliant per R070 note.
- R077: Employee participation = good_faith → no shift. FTA risk: high.
- R078: Only elements 1 and 2 met (no adverse action taken) → R083 → DD: low.
- R085/R090: Harassment elements < 4 → minimal.
- R091/R103: No protected activity → minimal.
- R104/R105: Maximum = high, single contributor = failure_to_accommodate.
- R107: Recommended actions for high.

### Structured Input

```json
{
  "dependency_inputs": {
    "is_covered_employer": true,
    "has_qualifying_disability": "yes",
    "is_covered_individual_with_disability": true,
    "is_qualified_individual": "yes",
    "accommodation_request_valid": true,
    "accommodation_required": "yes",
    "interactive_process_compliant": "indeterminate",
    "undue_hardship_applies": "no",
    "direct_threat_exists": "no"
  },
  "components": {
    "failure_to_accommodate": {
      "employee_interactive_process_participation": "good_faith",
      "employee_nonparticipation_documented": false
    },
    "disability_discrimination": {
      "adverse_action_taken": false,
      "causal_nexus_present": "no",
      "discriminatory_intent_evidence": "none",
      "legitimate_nondiscriminatory_reason_documented": false
    },
    "harassment": {
      "unwelcome_conduct_occurred": false,
      "conduct_severity": "isolated_minor",
      "employer_knew_or_should_have_known": false
    },
    "retaliation": {
      "engaged_in_protected_activity": false,
      "employer_aware_of_activity": false,
      "adverse_action_taken": false,
      "causal_nexus_present": "no",
      "days_between_activity_and_action": null
    }
  }
}
```

### Expected Output

```json
{
  "components": {
    "failure_to_accommodate": {
      "fta_element_1_met": true,
      "fta_element_2_met": true,
      "fta_element_3_met": true,
      "fta_element_4_met": true,
      "fta_element_5_met": true,
      "prima_facie_elements_present": 5,
      "documented_legitimate_denial": false,
      "risk_level_pre_weighting": "high",
      "employee_participation_shift_applied": false,
      "fta_risk_level": "high"
    },
    "disability_discrimination": {
      "dd_element_1_met": true,
      "dd_element_2_met": true,
      "dd_element_3_met": false,
      "dd_element_4_met": false,
      "discrimination_elements_present": 2,
      "discrimination_risk_level": "low"
    },
    "harassment": {
      "harassment_element_1_met": true,
      "harassment_element_2_met": false,
      "harassment_element_3_met": false,
      "harassment_element_4_met": false,
      "harassment_elements_present": 1,
      "harassment_risk_level": "minimal"
    },
    "retaliation": {
      "retaliation_element_1_met": false,
      "retaliation_element_2_met": false,
      "retaliation_element_3_met": false,
      "retaliation_element_4_met": false,
      "retaliation_elements_present": 0,
      "proximity_strength": "not_provided",
      "retaliation_risk_level": "minimal"
    }
  },
  "overall_violation_risk": {
    "component_risk_levels": {
      "failure_to_accommodate": "high",
      "disability_discrimination": "low",
      "harassment": "minimal",
      "retaliation": "minimal"
    },
    "overall_risk_level": "high",
    "primary_claim_basis": "failure_to_accommodate",
    "contributing_claims": ["failure_to_accommodate"],
    "reasoning": "Overall risk level is high driven by failure to accommodate. All five prima facie elements are present. Interactive process compliance is indeterminate — reflecting genuine uncertainty, not a finding of non-compliance. No documented legitimate denial exists.",
    "recommended_actions": [
      "Consult employment counsel promptly to evaluate exposure and remediation options.",
      "Preserve all documentation related to the accommodation request, interactive process, and adverse action.",
      "Assess whether the interactive process can be reopened or corrective steps taken.",
      "Review ADA reasonable accommodation procedures for systemic gaps."
    ]
  }
}
```

### Rules Fired

R068, R070, R077, R078, R083, R085, R090, R091, R096, R103, R104, R105, R107

---

## VR-003 — High: All Retaliation Elements, Strong Temporal Proximity

### Fact Pattern

Sandra, a manufacturing plant employee, filed an EEOC charge alleging disability discrimination on March 1. Her supervisor was notified of the charge on March 5. On March 22 — 21 days later — Sandra was terminated for alleged performance issues. Sandra has a qualifying disability, is a qualified individual, and participated in prior accommodation discussions. For this scenario, the FTA process was compliant and accommodation was provided (no FTA exposure). No harassment allegations exist. The employer has no documented legitimate reason for the termination apart from vague "performance" notes made after the EEOC charge was filed.

### Legal Analysis

- R068/R077: FTA elements: accommodation_required = no → element 5 not met (4 elements) → R073 → FTA moderate. Wait — if accommodation was provided, accommodation_required = no. 4 elements present → moderate. Adjust: accommodation_request_valid = true, accommodation_required = no → element 5 not met → 4 elements → moderate.
- R078/R082: DD: 4 elements (protected, qualified, adverse action: termination, causal nexus: circumstantial) + legitimate reason documented = true → moderate.
- R085/R090: No harassment → minimal.
- R091: All 4 retaliation elements met: protected activity (EEOC complaint) = yes, employer aware = yes, adverse action (termination) = yes, causal nexus = yes.
- R092: 21 days → proximity_strength = strong.
- R097: 4 elements + strong proximity → retaliation risk = critical.
- R104/R105: Maximum = critical. Only contributor = retaliation. Primary claim = retaliation.
- R106: Critical actions.

### Structured Input

```json
{
  "dependency_inputs": {
    "is_covered_employer": true,
    "has_qualifying_disability": "yes",
    "is_covered_individual_with_disability": true,
    "is_qualified_individual": "yes",
    "accommodation_request_valid": true,
    "accommodation_required": "no",
    "interactive_process_compliant": "yes",
    "undue_hardship_applies": "no",
    "direct_threat_exists": "no"
  },
  "components": {
    "failure_to_accommodate": {
      "employee_interactive_process_participation": "good_faith",
      "employee_nonparticipation_documented": false
    },
    "disability_discrimination": {
      "adverse_action_taken": true,
      "adverse_action_type": "termination",
      "causal_nexus_present": "yes",
      "discriminatory_intent_evidence": "circumstantial",
      "legitimate_nondiscriminatory_reason_documented": true
    },
    "harassment": {
      "unwelcome_conduct_occurred": false,
      "conduct_severity": "isolated_minor",
      "employer_knew_or_should_have_known": false
    },
    "retaliation": {
      "engaged_in_protected_activity": true,
      "protected_activity_type": "eeoc_complaint",
      "employer_aware_of_activity": true,
      "adverse_action_taken": true,
      "causal_nexus_present": "yes",
      "days_between_activity_and_action": 21
    }
  }
}
```

### Expected Output

```json
{
  "components": {
    "failure_to_accommodate": {
      "fta_element_1_met": true,
      "fta_element_2_met": true,
      "fta_element_3_met": true,
      "fta_element_4_met": true,
      "fta_element_5_met": false,
      "prima_facie_elements_present": 4,
      "documented_legitimate_denial": false,
      "risk_level_pre_weighting": "moderate",
      "employee_participation_shift_applied": false,
      "fta_risk_level": "moderate"
    },
    "disability_discrimination": {
      "dd_element_1_met": true,
      "dd_element_2_met": true,
      "dd_element_3_met": true,
      "dd_element_4_met": true,
      "discrimination_elements_present": 4,
      "discrimination_risk_level": "moderate"
    },
    "harassment": {
      "harassment_element_1_met": true,
      "harassment_element_2_met": false,
      "harassment_element_3_met": false,
      "harassment_element_4_met": false,
      "harassment_elements_present": 1,
      "harassment_risk_level": "minimal"
    },
    "retaliation": {
      "retaliation_element_1_met": true,
      "retaliation_element_2_met": true,
      "retaliation_element_3_met": true,
      "retaliation_element_4_met": true,
      "retaliation_elements_present": 4,
      "proximity_strength": "strong",
      "retaliation_risk_level": "critical"
    }
  },
  "overall_violation_risk": {
    "component_risk_levels": {
      "failure_to_accommodate": "moderate",
      "disability_discrimination": "moderate",
      "harassment": "minimal",
      "retaliation": "critical"
    },
    "overall_risk_level": "critical",
    "primary_claim_basis": "retaliation",
    "contributing_claims": ["retaliation"],
    "reasoning": "Overall risk level is critical driven by retaliation. All four retaliation elements are present and the adverse action occurred 21 days after the protected activity (strong temporal proximity). FTA and discrimination are each moderate.",
    "recommended_actions": [
      "Engage employment counsel immediately — do not take further adverse action without legal review.",
      "Preserve all documentation related to the accommodation request, interactive process, adverse action, and any complaints.",
      "Conduct an internal investigation to assess whether the conduct can be remediated prior to an EEOC charge.",
      "Evaluate whether corrective action (accommodation provision, reinstatement, or similar) can reduce exposure.",
      "Review and update ADA reasonable accommodation policies and training."
    ]
  }
}
```

### Rules Fired

R068, R073, R077, R078, R081, R085, R090, R091, R092, R097, R104, R105, R106

---

## VR-004 — Moderate: 4 FTA Elements Only (One Missing)

### Fact Pattern

David, an office employee, has a recorded history of anxiety disorder (record of disability). He made an oral request to HR for a quieter workspace. The employer acknowledged the request and began the interactive process. No accommodation has been denied yet — the process is ongoing. David is qualified. The employer has not taken any adverse action, no harassment has occurred, and no retaliation is alleged. Because the accommodation has not yet been denied, accommodation_required = no (the process is still open).

### Legal Analysis

- R068: Elements 1 (covered employer), 2 (qualifying disability: yes — record of disability), 3 (qualified: yes), 4 (valid request: yes) met. Element 5 (accommodation_required): no → not met. 4 elements present.
- R073: 4 elements → moderate pre-weighting.
- R077: participation = good_faith → no shift. FTA: moderate.
- R078: DD: adverse_action = false → element 3 not met → 2 elements → R083 → low.
- R085/R090: No harassment → minimal.
- R091/R103: No protected activity → minimal.
- R104/R105: Maximum = moderate. Primary = failure_to_accommodate.
- R108: Moderate actions.

### Structured Input

```json
{
  "dependency_inputs": {
    "is_covered_employer": true,
    "has_qualifying_disability": "yes",
    "is_covered_individual_with_disability": true,
    "is_qualified_individual": "yes",
    "accommodation_request_valid": true,
    "accommodation_required": "no",
    "interactive_process_compliant": "yes",
    "undue_hardship_applies": "no",
    "direct_threat_exists": "no"
  },
  "components": {
    "failure_to_accommodate": {
      "employee_interactive_process_participation": "good_faith",
      "employee_nonparticipation_documented": false
    },
    "disability_discrimination": {
      "adverse_action_taken": false,
      "causal_nexus_present": "no",
      "discriminatory_intent_evidence": "none",
      "legitimate_nondiscriminatory_reason_documented": false
    },
    "harassment": {
      "unwelcome_conduct_occurred": false,
      "conduct_severity": "isolated_minor",
      "employer_knew_or_should_have_known": false
    },
    "retaliation": {
      "engaged_in_protected_activity": false,
      "employer_aware_of_activity": false,
      "adverse_action_taken": false,
      "causal_nexus_present": "no",
      "days_between_activity_and_action": null
    }
  }
}
```

### Expected Output

```json
{
  "components": {
    "failure_to_accommodate": {
      "fta_element_1_met": true,
      "fta_element_2_met": true,
      "fta_element_3_met": true,
      "fta_element_4_met": true,
      "fta_element_5_met": false,
      "prima_facie_elements_present": 4,
      "documented_legitimate_denial": false,
      "risk_level_pre_weighting": "moderate",
      "employee_participation_shift_applied": false,
      "fta_risk_level": "moderate"
    },
    "disability_discrimination": {
      "dd_element_1_met": true,
      "dd_element_2_met": true,
      "dd_element_3_met": false,
      "dd_element_4_met": false,
      "discrimination_elements_present": 2,
      "discrimination_risk_level": "low"
    },
    "harassment": {
      "harassment_element_1_met": true,
      "harassment_element_2_met": false,
      "harassment_element_3_met": false,
      "harassment_element_4_met": false,
      "harassment_elements_present": 1,
      "harassment_risk_level": "minimal"
    },
    "retaliation": {
      "retaliation_element_1_met": false,
      "retaliation_element_2_met": false,
      "retaliation_element_3_met": false,
      "retaliation_element_4_met": false,
      "retaliation_elements_present": 0,
      "proximity_strength": "not_provided",
      "retaliation_risk_level": "minimal"
    }
  },
  "overall_violation_risk": {
    "component_risk_levels": {
      "failure_to_accommodate": "moderate",
      "disability_discrimination": "low",
      "harassment": "minimal",
      "retaliation": "minimal"
    },
    "overall_risk_level": "moderate",
    "primary_claim_basis": "failure_to_accommodate",
    "contributing_claims": ["failure_to_accommodate"],
    "reasoning": "Overall risk level is moderate driven by failure to accommodate. Four of five prima facie elements are present; accommodation has not yet been denied so element five is not satisfied. The interactive process is ongoing.",
    "recommended_actions": [
      "Review the accommodation process and documentation for gaps identified in the analysis.",
      "Consider consulting employment counsel if the identified gaps are not easily remediated.",
      "Document all steps taken in the interactive process going forward.",
      "Ensure supervisor and HR training on ADA obligations is current."
    ]
  }
}
```

### Rules Fired

R068, R073, R077, R078, R083, R085, R090, R091, R096, R103, R104, R105, R108

---

## VR-005 — Moderate: All DD Elements, Legitimate Non-Discriminatory Reason Documented

### Fact Pattern

Elena, a retail employee with a documented visual impairment (actual disability), was passed over for a promotion. She is a qualified individual. The employer promoted a non-disabled candidate. Elena contends the disability was a motivating factor (circumstantial evidence: the deciding manager made a comment that vision impairment would be a "limitation" in a supervisory role). The employer has documented that the selected candidate had significantly higher performance ratings and prior supervisory experience. No accommodation request was pending. No harassment or retaliation alleged.

### Legal Analysis

- R068: FTA: accommodation_required = no, accommodation_request_valid = false → elements 4 and 5 not met → 2 elements → R083 → low.
- R078: DD: 4 elements met (protected: yes, qualified: yes, adverse action (failure_to_promote): yes, causal nexus: yes — comment is circumstantial). legitimate_nondiscriminatory_reason_documented = true → R081 → moderate.
- R085/R090: No harassment → minimal.
- R091/R103: No protected activity → minimal.
- R104/R105: Maximum = moderate. FTA = low, DD = moderate, harassment = minimal, retaliation = minimal. Primary = disability_discrimination.
- R108: Moderate actions.

### Structured Input

```json
{
  "dependency_inputs": {
    "is_covered_employer": true,
    "has_qualifying_disability": "yes",
    "is_covered_individual_with_disability": true,
    "is_qualified_individual": "yes",
    "accommodation_request_valid": false,
    "accommodation_required": "no",
    "interactive_process_compliant": "yes",
    "undue_hardship_applies": "no",
    "direct_threat_exists": "no"
  },
  "components": {
    "failure_to_accommodate": {
      "employee_interactive_process_participation": "good_faith",
      "employee_nonparticipation_documented": false
    },
    "disability_discrimination": {
      "adverse_action_taken": true,
      "adverse_action_type": "failure_to_promote",
      "causal_nexus_present": "yes",
      "discriminatory_intent_evidence": "circumstantial",
      "legitimate_nondiscriminatory_reason_documented": true
    },
    "harassment": {
      "unwelcome_conduct_occurred": false,
      "conduct_severity": "isolated_minor",
      "employer_knew_or_should_have_known": false
    },
    "retaliation": {
      "engaged_in_protected_activity": false,
      "employer_aware_of_activity": false,
      "adverse_action_taken": false,
      "causal_nexus_present": "no",
      "days_between_activity_and_action": null
    }
  }
}
```

### Expected Output

```json
{
  "components": {
    "failure_to_accommodate": {
      "fta_element_1_met": true,
      "fta_element_2_met": true,
      "fta_element_3_met": true,
      "fta_element_4_met": false,
      "fta_element_5_met": false,
      "prima_facie_elements_present": 3,
      "documented_legitimate_denial": false,
      "risk_level_pre_weighting": "low",
      "employee_participation_shift_applied": false,
      "fta_risk_level": "low"
    },
    "disability_discrimination": {
      "dd_element_1_met": true,
      "dd_element_2_met": true,
      "dd_element_3_met": true,
      "dd_element_4_met": true,
      "discrimination_elements_present": 4,
      "discrimination_risk_level": "moderate"
    },
    "harassment": {
      "harassment_element_1_met": true,
      "harassment_element_2_met": false,
      "harassment_element_3_met": false,
      "harassment_element_4_met": false,
      "harassment_elements_present": 1,
      "harassment_risk_level": "minimal"
    },
    "retaliation": {
      "retaliation_element_1_met": false,
      "retaliation_element_2_met": false,
      "retaliation_element_3_met": false,
      "retaliation_element_4_met": false,
      "retaliation_elements_present": 0,
      "proximity_strength": "not_provided",
      "retaliation_risk_level": "minimal"
    }
  },
  "overall_violation_risk": {
    "component_risk_levels": {
      "failure_to_accommodate": "low",
      "disability_discrimination": "moderate",
      "harassment": "minimal",
      "retaliation": "minimal"
    },
    "overall_risk_level": "moderate",
    "primary_claim_basis": "disability_discrimination",
    "contributing_claims": ["disability_discrimination"],
    "reasoning": "Overall risk level is moderate driven by disability discrimination. All four McDonnell Douglas elements are present; however, the employer has documented a legitimate non-discriminatory reason for the adverse action, satisfying step-two burden. The claimant would need to show pretext.",
    "recommended_actions": [
      "Review the accommodation process and documentation for gaps identified in the analysis.",
      "Consider consulting employment counsel if the identified gaps are not easily remediated.",
      "Document all steps taken in the interactive process going forward.",
      "Ensure supervisor and HR training on ADA obligations is current."
    ]
  }
}
```

### Rules Fired

R068, R074, R077, R078, R081, R085, R090, R091, R096, R103, R104, R105, R108

---

## VR-006 — Low: Fewer than 3 FTA Elements, No Other Elevated Claims

### Fact Pattern

Robert, an applicant for a delivery driver position, disclosed a hearing impairment during the interview process (not during a pre-offer medical inquiry). The employer is covered (25 employees). Robert was offered and accepted the position; no accommodation request has been made and no adverse action has occurred. He has not engaged in any protected activity. No harassment has occurred. This scenario presents early-stage coverage with no active accommodation request or process.

### Legal Analysis

- R068: FTA: covered employer = yes, qualifying disability = yes, qualified individual = yes. No accommodation request made (element 4 = false). Accommodation_required = no (element 5 = false). 3 elements present.
- R074: 3 elements → low pre-weighting.
- R077: participation = good_faith → no shift. FTA: low.
- R078: DD: adverse_action = false → element 3 not met. 2 elements → R083 → low.
- R085/R090: No harassment → minimal.
- R091/R103: No protected activity → minimal.
- R104/R105: Maximum = low. FTA and DD both low → tiebreak → primary = failure_to_accommodate (tiebreak order position 1). Contributing = [failure_to_accommodate, disability_discrimination].
- R109: Low actions.

### Structured Input

```json
{
  "dependency_inputs": {
    "is_covered_employer": true,
    "has_qualifying_disability": "yes",
    "is_covered_individual_with_disability": true,
    "is_qualified_individual": "yes",
    "accommodation_request_valid": false,
    "accommodation_required": "no",
    "interactive_process_compliant": "yes",
    "undue_hardship_applies": "no",
    "direct_threat_exists": "no"
  },
  "components": {
    "failure_to_accommodate": {
      "employee_interactive_process_participation": "good_faith",
      "employee_nonparticipation_documented": false
    },
    "disability_discrimination": {
      "adverse_action_taken": false,
      "causal_nexus_present": "no",
      "discriminatory_intent_evidence": "none",
      "legitimate_nondiscriminatory_reason_documented": false
    },
    "harassment": {
      "unwelcome_conduct_occurred": false,
      "conduct_severity": "isolated_minor",
      "employer_knew_or_should_have_known": false
    },
    "retaliation": {
      "engaged_in_protected_activity": false,
      "employer_aware_of_activity": false,
      "adverse_action_taken": false,
      "causal_nexus_present": "no",
      "days_between_activity_and_action": null
    }
  }
}
```

### Expected Output

```json
{
  "components": {
    "failure_to_accommodate": {
      "fta_element_1_met": true,
      "fta_element_2_met": true,
      "fta_element_3_met": true,
      "fta_element_4_met": false,
      "fta_element_5_met": false,
      "prima_facie_elements_present": 3,
      "documented_legitimate_denial": false,
      "risk_level_pre_weighting": "low",
      "employee_participation_shift_applied": false,
      "fta_risk_level": "low"
    },
    "disability_discrimination": {
      "dd_element_1_met": true,
      "dd_element_2_met": true,
      "dd_element_3_met": false,
      "dd_element_4_met": false,
      "discrimination_elements_present": 2,
      "discrimination_risk_level": "low"
    },
    "harassment": {
      "harassment_element_1_met": true,
      "harassment_element_2_met": false,
      "harassment_element_3_met": false,
      "harassment_element_4_met": false,
      "harassment_elements_present": 1,
      "harassment_risk_level": "minimal"
    },
    "retaliation": {
      "retaliation_element_1_met": false,
      "retaliation_element_2_met": false,
      "retaliation_element_3_met": false,
      "retaliation_element_4_met": false,
      "retaliation_elements_present": 0,
      "proximity_strength": "not_provided",
      "retaliation_risk_level": "minimal"
    }
  },
  "overall_violation_risk": {
    "component_risk_levels": {
      "failure_to_accommodate": "low",
      "disability_discrimination": "low",
      "harassment": "minimal",
      "retaliation": "minimal"
    },
    "overall_risk_level": "low",
    "primary_claim_basis": "failure_to_accommodate",
    "contributing_claims": ["failure_to_accommodate", "disability_discrimination"],
    "reasoning": "Overall risk level is low. Failure to accommodate and disability discrimination are both low; tiebreak selects failure to accommodate as primary. No accommodation request has been made and no adverse action has occurred. Coverage is established but no active compliance gap exists.",
    "recommended_actions": [
      "Monitor the situation and document the basis for any accommodation-related decisions.",
      "Ensure the accommodation process is complete and documented if still ongoing.",
      "No immediate legal consultation required, but note the flagged gaps."
    ]
  }
}
```

### Rules Fired

R068, R074, R077, R078, R083, R085, R090, R091, R096, R103, R104, R105, R109

---

## VR-007 — Minimal: No Elements Present Across All Four Claim Types

### Fact Pattern

A small retail company with 8 employees has an employee who requested a flexible start time. The employer is not a covered entity under the ADA (fewer than 15 employees). The employee does not have a qualifying disability. No adverse action has been taken. No harassment has occurred. No protected activity has been engaged in.

### Legal Analysis

- R068: FTA: covered employer = false (8 employees) → element 1 not met. qualifying_disability = no → element 2 not met. All five elements not met. 0 elements → R075 → minimal.
- R078: DD: covered_individual = false → element 1 not met. 0 elements → R084 → minimal.
- R085/R090: covered_individual = false → element 1 not met. 0 elements → minimal.
- R091/R103: No protected activity → 0 elements → minimal.
- R104/R105: Maximum = minimal. All four components = minimal. Tiebreak: primary = failure_to_accommodate.
- R110: Minimal actions.

### Structured Input

```json
{
  "dependency_inputs": {
    "is_covered_employer": false,
    "has_qualifying_disability": "no",
    "is_covered_individual_with_disability": false,
    "is_qualified_individual": "no",
    "accommodation_request_valid": false,
    "accommodation_required": "no",
    "interactive_process_compliant": "yes",
    "undue_hardship_applies": "no",
    "direct_threat_exists": "no"
  },
  "components": {
    "failure_to_accommodate": {
      "employee_interactive_process_participation": "good_faith",
      "employee_nonparticipation_documented": false
    },
    "disability_discrimination": {
      "adverse_action_taken": false,
      "causal_nexus_present": "no",
      "discriminatory_intent_evidence": "none",
      "legitimate_nondiscriminatory_reason_documented": false
    },
    "harassment": {
      "unwelcome_conduct_occurred": false,
      "conduct_severity": "isolated_minor",
      "employer_knew_or_should_have_known": false
    },
    "retaliation": {
      "engaged_in_protected_activity": false,
      "employer_aware_of_activity": false,
      "adverse_action_taken": false,
      "causal_nexus_present": "no",
      "days_between_activity_and_action": null
    }
  }
}
```

### Expected Output

```json
{
  "components": {
    "failure_to_accommodate": {
      "fta_element_1_met": false,
      "fta_element_2_met": false,
      "fta_element_3_met": false,
      "fta_element_4_met": false,
      "fta_element_5_met": false,
      "prima_facie_elements_present": 0,
      "documented_legitimate_denial": false,
      "risk_level_pre_weighting": "minimal",
      "employee_participation_shift_applied": false,
      "fta_risk_level": "minimal"
    },
    "disability_discrimination": {
      "dd_element_1_met": false,
      "dd_element_2_met": false,
      "dd_element_3_met": false,
      "dd_element_4_met": false,
      "discrimination_elements_present": 0,
      "discrimination_risk_level": "minimal"
    },
    "harassment": {
      "harassment_element_1_met": false,
      "harassment_element_2_met": false,
      "harassment_element_3_met": false,
      "harassment_element_4_met": false,
      "harassment_elements_present": 0,
      "harassment_risk_level": "minimal"
    },
    "retaliation": {
      "retaliation_element_1_met": false,
      "retaliation_element_2_met": false,
      "retaliation_element_3_met": false,
      "retaliation_element_4_met": false,
      "retaliation_elements_present": 0,
      "proximity_strength": "not_provided",
      "retaliation_risk_level": "minimal"
    }
  },
  "overall_violation_risk": {
    "component_risk_levels": {
      "failure_to_accommodate": "minimal",
      "disability_discrimination": "minimal",
      "harassment": "minimal",
      "retaliation": "minimal"
    },
    "overall_risk_level": "minimal",
    "primary_claim_basis": "failure_to_accommodate",
    "contributing_claims": ["failure_to_accommodate", "disability_discrimination", "harassment", "retaliation"],
    "reasoning": "Overall risk level is minimal. No ADA compliance exposure identified. The employer is not a covered entity and the individual does not have a qualifying disability. No adverse action, harassment, or protected activity is present.",
    "recommended_actions": [
      "No immediate action required. Employer conduct appears compliant based on available information.",
      "Continue standard ADA compliance practices and documentation."
    ]
  }
}
```

### Rules Fired

R068, R075, R077, R078, R084, R085, R090, R091, R096, R103, R104, R105, R110

---

## VR-008 — Tiebreak: FTA Critical and Retaliation Critical, Tiebreak Applies

### Fact Pattern

Kevin, a hospital employee with multiple sclerosis (actual disability), requested a schedule modification for physical therapy appointments. The employer denied it without engaging in the interactive process and has no documented undue hardship or direct threat finding. Kevin is a covered individual, is qualified, made a valid written request, and accommodation was required. Additionally, Kevin had filed an internal complaint about disability discrimination (opposition to discrimination = protected activity) two weeks before the denial was treated as a constructive adverse action (Kevin left after being informed the request was denied and he would not be reassigned). The employer was aware of the complaint. Causal nexus exists. Days between complaint and constructive termination: 14 days. Interactive process compliance: no. No harassment alleged. No separate discrimination claim in this scenario (adverse action here is the constructive termination, analyzed under retaliation, not independently under discrimination with a non-disability reason).

**Note on tiebreak setup:** FTA produces critical (all 5 elements + no process + no denial). Retaliation produces critical (all 4 elements + strong proximity at 14 days). Both are critical. Tiebreak order fires: failure_to_accommodate (position 1) wins. Contributing claims = [failure_to_accommodate, retaliation].

### Legal Analysis

- R068: All 5 FTA elements met. interactive_process_compliant = no. documented_legitimate_denial = false.
- R069: 5 elements + no process + no denial → critical pre-weighting.
- R077: participation = good_faith → no shift. FTA: critical.
- R078: DD: adverse_action = true (constructive termination), causal_nexus = yes, discriminatory_intent = circumstantial, legitimate_reason_documented = false → R080 → DD: high. (Elements: 1 yes, 2 yes, 3 yes, 4 yes = 4 elements.)
- R085/R090: No harassment → minimal.
- R091: All 4 retaliation elements met.
- R092: 14 days → proximity_strength = strong.
- R097: 4 elements + strong proximity → critical.
- R104: Maximum = critical. FTA = critical, DD = high, harassment = minimal, retaliation = critical.
- R105: contributing_claims = [failure_to_accommodate, retaliation]. Tiebreak order position 1 = failure_to_accommodate → primary_claim_basis = failure_to_accommodate.
- R106: Critical actions.

### Structured Input

```json
{
  "dependency_inputs": {
    "is_covered_employer": true,
    "has_qualifying_disability": "yes",
    "is_covered_individual_with_disability": true,
    "is_qualified_individual": "yes",
    "accommodation_request_valid": true,
    "accommodation_required": "yes",
    "interactive_process_compliant": "no",
    "undue_hardship_applies": "no",
    "direct_threat_exists": "no"
  },
  "components": {
    "failure_to_accommodate": {
      "employee_interactive_process_participation": "good_faith",
      "employee_nonparticipation_documented": false
    },
    "disability_discrimination": {
      "adverse_action_taken": true,
      "adverse_action_type": "termination",
      "causal_nexus_present": "yes",
      "discriminatory_intent_evidence": "circumstantial",
      "legitimate_nondiscriminatory_reason_documented": false
    },
    "harassment": {
      "unwelcome_conduct_occurred": false,
      "conduct_severity": "isolated_minor",
      "employer_knew_or_should_have_known": false
    },
    "retaliation": {
      "engaged_in_protected_activity": true,
      "protected_activity_type": "opposition_to_discrimination",
      "employer_aware_of_activity": true,
      "adverse_action_taken": true,
      "causal_nexus_present": "yes",
      "days_between_activity_and_action": 14
    }
  }
}
```

### Expected Output

```json
{
  "components": {
    "failure_to_accommodate": {
      "fta_element_1_met": true,
      "fta_element_2_met": true,
      "fta_element_3_met": true,
      "fta_element_4_met": true,
      "fta_element_5_met": true,
      "prima_facie_elements_present": 5,
      "documented_legitimate_denial": false,
      "risk_level_pre_weighting": "critical",
      "employee_participation_shift_applied": false,
      "fta_risk_level": "critical"
    },
    "disability_discrimination": {
      "dd_element_1_met": true,
      "dd_element_2_met": true,
      "dd_element_3_met": true,
      "dd_element_4_met": true,
      "discrimination_elements_present": 4,
      "discrimination_risk_level": "high"
    },
    "harassment": {
      "harassment_element_1_met": true,
      "harassment_element_2_met": false,
      "harassment_element_3_met": false,
      "harassment_element_4_met": false,
      "harassment_elements_present": 1,
      "harassment_risk_level": "minimal"
    },
    "retaliation": {
      "retaliation_element_1_met": true,
      "retaliation_element_2_met": true,
      "retaliation_element_3_met": true,
      "retaliation_element_4_met": true,
      "retaliation_elements_present": 4,
      "proximity_strength": "strong",
      "retaliation_risk_level": "critical"
    }
  },
  "overall_violation_risk": {
    "component_risk_levels": {
      "failure_to_accommodate": "critical",
      "disability_discrimination": "high",
      "harassment": "minimal",
      "retaliation": "critical"
    },
    "overall_risk_level": "critical",
    "primary_claim_basis": "failure_to_accommodate",
    "contributing_claims": ["failure_to_accommodate", "retaliation"],
    "reasoning": "Overall risk level is critical. Both failure to accommodate and retaliation produced critical risk levels. Tiebreak order selects failure to accommodate as the primary claim basis. FTA: all five prima facie elements present, no compliant interactive process, no documented legitimate denial. Retaliation: all four elements present, 14-day proximity (strong). Disability discrimination is high.",
    "recommended_actions": [
      "Engage employment counsel immediately — do not take further adverse action without legal review.",
      "Preserve all documentation related to the accommodation request, interactive process, adverse action, and any complaints.",
      "Conduct an internal investigation to assess whether the conduct can be remediated prior to an EEOC charge.",
      "Evaluate whether corrective action (accommodation provision, reinstatement, or similar) can reduce exposure.",
      "Review and update ADA reasonable accommodation policies and training."
    ]
  }
}
```

### Rules Fired

R068, R069, R077, R078, R080, R085, R090, R091, R092, R097, R104, R105, R106
