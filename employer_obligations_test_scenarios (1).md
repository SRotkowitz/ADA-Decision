# ADA Module 3 — Employer Obligations Test Scenarios

**Module:** `ada_employer_obligations`  
**Version:** 0.1  
**Last updated:** 2026-04-20  
**Scenario count:** 8 (EO-001 through EO-008)

---

## EO-001 — Full Compliance: All Three Components Pass

### Fact Pattern
A warehouse employee with Type 2 diabetes requests an accommodation for a modified break schedule to allow insulin injections and snacks. The employer acknowledges the request the same day, initiates dialogue with the employee within 5 business days, consults JAN, considers three alternatives (modified break schedule, private break room access, partial telework), communicates its decision granting the modified break schedule with a written explanation, and follows up two weeks later to confirm effectiveness. Medical information is kept in a separate file. Access is limited to HR and the direct supervisor. No disclosures to unauthorized parties. The inquiry that surfaced the need arose during employment when the employee voluntarily disclosed and requested documentation of work restrictions — job-related and supported by business necessity in the context of the accommodation process.

### Legal Analysis
- **3.1a:** All three mechanical steps satisfied — acknowledgment (same day), dialogue within 5 business days (within engine-defined 10-day heuristic), options documented. process_mechanically_compliant = true.
- **3.1b:** Four factors for good faith: employer initiated promptly (PQ-F01), multiple alternatives considered (PQ-F02), JAN consulted (PQ-F03), decision communicated with explanation (PQ-F04), follow-up conducted (PQ-F05). Zero factors against. process_quality = yes.
- **3.1c:** true + yes = yes. interactive_process_compliant = yes. Risk: minimal.
- **3.2:** During-employment documentation request — job-related (managing accommodation process) and consistent with business necessity. inquiry_permitted = yes. No pre-offer or post-offer inquiries involved.
- **3.3:** Separate file maintained, access limited to permitted parties, no unauthorized disclosure. confidentiality_compliant = true.

### Rules Fired
R061 (during-employment inquiry), R047 (mechanical compliance — all pass), R051 (process quality factors), R052 (composite — true+yes=yes), R064 (confidentiality full compliance)

### Structured Input
```json
{
  "dependency_inputs": {
    "is_covered_employer": true,
    "is_covered_individual": true,
    "accommodation_required": "yes"
  },
  "interactive_process": {
    "request_acknowledged": true,
    "accommodation_request_date": "2026-03-01",
    "dialogue_initiated_date": "2026-03-06",
    "business_days_to_initiation": 5,
    "accommodation_options_documented": true,
    "employer_initiated_dialogue_promptly": true,
    "multiple_alternatives_considered": true,
    "jan_or_equivalent_consulted": true,
    "decision_communicated_with_explanation": true,
    "follow_up_on_implemented_accommodation": true,
    "employer_delayed_without_explanation": false,
    "all_options_rejected_without_rationale": false,
    "relied_on_disability_stereotypes": false,
    "process_terminated_unilaterally": false,
    "employee_interactive_process_participation": "good_faith"
  },
  "medical_inquiry_limitations": {
    "multiple_inquiry_stages": [
      {
        "inquiry_stage": "during_employment",
        "inquiry_type": "request_for_documentation",
        "inquiry_description": "Employer requested medical documentation confirming diabetes diagnosis and need for modified breaks",
        "during_employment_inquiry_job_related": true,
        "during_employment_inquiry_business_necessity": true,
        "during_employment_voluntary_wellness": false
      }
    ]
  },
  "confidentiality": {
    "medical_info_in_separate_file": true,
    "access_limited_to_permitted_parties": true,
    "unauthorized_disclosure_occurred": false
  }
}
```

### Expected Output
```json
{
  "interactive_process": {
    "process_mechanically_compliant": true,
    "mechanical_compliance_checks": {
      "acknowledged_request": true,
      "initiated_dialogue_timely": true,
      "documented_options_considered": true
    },
    "process_quality": "yes",
    "process_quality_analysis": {
      "factors_for": [
        "employer considered multiple accommodation alternatives before reaching a decision — factor for good faith under EEOC Enforcement Guidance No. 915.002",
        "employer consulted the Job Accommodation Network or equivalent resource — factor for good faith",
        "employer communicated its accommodation decision with a reasoned explanation — factor for good faith",
        "employer followed up after implementation to confirm effectiveness — factor for good faith",
        "employer initiated dialogue promptly after the accommodation request — factor for good faith"
      ],
      "factors_against": [],
      "key_uncertainties": [],
      "nonparticipation_weighting_applied": false
    },
    "interactive_process_compliant": "yes",
    "interactive_process_risk_level": "minimal"
  },
  "medical_inquiry_limitations": {
    "inquiry_evaluations": [
      {
        "inquiry_stage": "during_employment",
        "inquiry_type": "request_for_documentation",
        "inquiry_permitted": "yes",
        "violation_basis": "none",
        "source_citation": "42 U.S.C. § 12112(d)(4)(A); 29 CFR § 1630.14(c)"
      }
    ],
    "medical_inquiry_compliant": true,
    "medical_inquiry_risk_level": "minimal"
  },
  "confidentiality": {
    "confidentiality_checks": {
      "separate_file_maintained": true,
      "access_properly_limited": true,
      "no_unauthorized_disclosure": true
    },
    "confidentiality_compliant": true,
    "violated_requirements": [],
    "confidentiality_risk_level": "minimal"
  }
}
```

---

## EO-002 — Mechanical Compliance Only: 3.1a Passes, 3.1b Fails → Indeterminate Composite

### Fact Pattern
A retail employee with a visual impairment requests large-format screen accommodations. The employer acknowledges the request, initiates dialogue within 7 business days, and documents that it considered two options. However, it rejected both options without any documented rationale, terminated the interactive process before reaching a conclusion, and communicated no explanation for its decision. It did not consult JAN or any equivalent resource. No inquiry or confidentiality issues present.

### Legal Analysis
- **3.1a:** Acknowledgment — yes. Dialogue initiated in 7 days — yes (within heuristic). Options documented — yes. process_mechanically_compliant = true.
- **3.1b:** Factors for: none that trigger (no prompt dialogue credit without follow-through, no JAN, no explanation, no follow-up). Factors against: all_options_rejected_without_rationale (PQ-A02), process_terminated_unilaterally (PQ-A04). process_quality = no (factors_against >= 2, factors_for <= 1).
- **3.1c:** true + no = indeterminate (mechanical compliance does not cure bad faith). interactive_process_compliant = indeterminate. Risk: moderate.
- **3.2:** No inquiries evaluated.
- **3.3:** No confidentiality issues.

### Rules Fired
R047 (mechanical — all pass), R051 (process quality — factors against dominate), R052 (composite — true+no=indeterminate)

### Structured Input
```json
{
  "dependency_inputs": {
    "is_covered_employer": true,
    "is_covered_individual": true,
    "accommodation_required": "indeterminate"
  },
  "interactive_process": {
    "request_acknowledged": true,
    "accommodation_request_date": "2026-02-10",
    "dialogue_initiated_date": "2026-02-19",
    "business_days_to_initiation": 7,
    "accommodation_options_documented": true,
    "employer_initiated_dialogue_promptly": false,
    "multiple_alternatives_considered": false,
    "jan_or_equivalent_consulted": false,
    "decision_communicated_with_explanation": false,
    "follow_up_on_implemented_accommodation": false,
    "employer_delayed_without_explanation": false,
    "all_options_rejected_without_rationale": true,
    "relied_on_disability_stereotypes": false,
    "process_terminated_unilaterally": true,
    "employee_interactive_process_participation": "good_faith"
  },
  "medical_inquiry_limitations": {
    "multiple_inquiry_stages": []
  },
  "confidentiality": {
    "medical_info_in_separate_file": true,
    "access_limited_to_permitted_parties": true,
    "unauthorized_disclosure_occurred": false
  }
}
```

### Expected Output
```json
{
  "interactive_process": {
    "process_mechanically_compliant": true,
    "mechanical_compliance_checks": {
      "acknowledged_request": true,
      "initiated_dialogue_timely": true,
      "documented_options_considered": true
    },
    "process_quality": "no",
    "process_quality_analysis": {
      "factors_for": [],
      "factors_against": [
        "employer rejected all identified accommodation options without documented rationale — factor against good faith",
        "employer terminated the interactive process unilaterally before reaching a conclusion — factor against good faith"
      ],
      "key_uncertainties": [],
      "nonparticipation_weighting_applied": false
    },
    "interactive_process_compliant": "indeterminate",
    "interactive_process_risk_level": "moderate"
  },
  "medical_inquiry_limitations": {
    "inquiry_evaluations": [],
    "medical_inquiry_compliant": true,
    "medical_inquiry_risk_level": "minimal"
  },
  "confidentiality": {
    "confidentiality_checks": {
      "separate_file_maintained": true,
      "access_properly_limited": true,
      "no_unauthorized_disclosure": true
    },
    "confidentiality_compliant": true,
    "violated_requirements": [],
    "confidentiality_risk_level": "minimal"
  }
}
```

---

## EO-003 — Bad Faith Process: Delayed, All Options Rejected Without Rationale

### Fact Pattern
A call center employee with PTSD requests telework as an accommodation. The employer waits 19 business days before initiating any dialogue, never provides an explanation for the delay, does not document what options it considered, relies on a generalized belief that "PTSD employees can't handle customer calls" rather than an individualized assessment, and rejects all accommodation options without documented rationale. It never acknowledged the request in writing or verbally.

### Legal Analysis
- **3.1a:** request_acknowledged = false → all three checks fail immediately (R049). process_mechanically_compliant = false.
- **3.1b:** Factors against: employer_delayed_without_explanation (PQ-A01), all_options_rejected_without_rationale (PQ-A02), relied_on_disability_stereotypes (PQ-A03). Factors for: zero. process_quality = no.
- **3.1c:** false + no = no. interactive_process_compliant = no. Risk: critical (stereotypes present).
- **3.2:** No inquiries evaluated.
- **3.3:** No confidentiality issues.

### Rules Fired
R049 (mechanical — acknowledgment failed), R051 (process quality — three factors against), R052 (composite — false+no=no)

### Structured Input
```json
{
  "dependency_inputs": {
    "is_covered_employer": true,
    "is_covered_individual": true,
    "accommodation_required": "yes"
  },
  "interactive_process": {
    "request_acknowledged": false,
    "accommodation_request_date": "2026-01-05",
    "dialogue_initiated_date": "2026-02-01",
    "business_days_to_initiation": 19,
    "accommodation_options_documented": false,
    "employer_initiated_dialogue_promptly": false,
    "multiple_alternatives_considered": false,
    "jan_or_equivalent_consulted": false,
    "decision_communicated_with_explanation": false,
    "follow_up_on_implemented_accommodation": false,
    "employer_delayed_without_explanation": true,
    "all_options_rejected_without_rationale": true,
    "relied_on_disability_stereotypes": true,
    "process_terminated_unilaterally": false,
    "employee_interactive_process_participation": "good_faith"
  },
  "medical_inquiry_limitations": {
    "multiple_inquiry_stages": []
  },
  "confidentiality": {
    "medical_info_in_separate_file": true,
    "access_limited_to_permitted_parties": true,
    "unauthorized_disclosure_occurred": false
  }
}
```

### Expected Output
```json
{
  "interactive_process": {
    "process_mechanically_compliant": false,
    "mechanical_compliance_checks": {
      "acknowledged_request": false,
      "initiated_dialogue_timely": false,
      "documented_options_considered": false
    },
    "process_quality": "no",
    "process_quality_analysis": {
      "factors_for": [],
      "factors_against": [
        "employer delayed the interactive process without providing an explanation to the employee",
        "employer rejected all identified accommodation options without documented rationale",
        "employer's assessment relied on generalizations or stereotypes about the disability rather than an individualized assessment"
      ],
      "key_uncertainties": [],
      "nonparticipation_weighting_applied": false
    },
    "interactive_process_compliant": "no",
    "interactive_process_risk_level": "critical"
  },
  "medical_inquiry_limitations": {
    "inquiry_evaluations": [],
    "medical_inquiry_compliant": true,
    "medical_inquiry_risk_level": "minimal"
  },
  "confidentiality": {
    "confidentiality_checks": {
      "separate_file_maintained": true,
      "access_properly_limited": true,
      "no_unauthorized_disclosure": true
    },
    "confidentiality_compliant": true,
    "violated_requirements": [],
    "confidentiality_risk_level": "minimal"
  }
}
```

---

## EO-004 — Employee Refused Participation: Weighting Factor Applied, One-Tier Shift Only

### Fact Pattern
A production employee with a back injury requests a modified lifting schedule. The employer acknowledges the request within 2 business days, initiates dialogue within 6 business days, and documents two accommodation options. However, the employee refuses to attend two scheduled interactive process meetings, is sent written notices by HR documenting each refusal, and then stops communicating. The employer has documentation of both refusals. The employer did not consult JAN, did not communicate a decision with explanation (because the process broke down), and did not follow up. The employer did not terminate the process — the employee abandoned it.

### Legal Analysis
- **3.1a:** Acknowledgment — yes. Dialogue initiated in 6 days — yes. Options documented — yes. process_mechanically_compliant = true.
- **3.1b (pre-weighting):** Factors for: employer_initiated_dialogue_promptly (PQ-F01). Factors against: none triggered by employer. Pre-weighting quality = indeterminate (1 factor for, 0 against — does not reach the "yes" threshold of ≥3, nor "no" threshold). 
- **R053 weighting:** employee_interactive_process_participation = "refused", employer_documented_employee_nonparticipation = true → one-tier shift. indeterminate → yes.
- **3.1c:** true + yes (after weighting) = yes. interactive_process_compliant = yes. Risk: low (note: non-participation documented).
- **3.2:** No inquiries.
- **3.3:** Compliant.

### Rules Fired
R047 (mechanical — all pass), R051 (process quality factors — pre-weighting), R053 (non-participation weighting — indeterminate→yes), R052 (composite — true+yes=yes), R064 (confidentiality)

### Structured Input
```json
{
  "dependency_inputs": {
    "is_covered_employer": true,
    "is_covered_individual": true,
    "accommodation_required": "indeterminate"
  },
  "interactive_process": {
    "request_acknowledged": true,
    "accommodation_request_date": "2026-02-20",
    "dialogue_initiated_date": "2026-02-28",
    "business_days_to_initiation": 6,
    "accommodation_options_documented": true,
    "employer_initiated_dialogue_promptly": true,
    "multiple_alternatives_considered": false,
    "jan_or_equivalent_consulted": false,
    "decision_communicated_with_explanation": false,
    "follow_up_on_implemented_accommodation": false,
    "employer_delayed_without_explanation": false,
    "all_options_rejected_without_rationale": false,
    "relied_on_disability_stereotypes": false,
    "process_terminated_unilaterally": false,
    "employee_interactive_process_participation": "refused",
    "employer_documented_employee_nonparticipation": true
  },
  "medical_inquiry_limitations": {
    "multiple_inquiry_stages": []
  },
  "confidentiality": {
    "medical_info_in_separate_file": true,
    "access_limited_to_permitted_parties": true,
    "unauthorized_disclosure_occurred": false
  }
}
```

### Expected Output
```json
{
  "interactive_process": {
    "process_mechanically_compliant": true,
    "mechanical_compliance_checks": {
      "acknowledged_request": true,
      "initiated_dialogue_timely": true,
      "documented_options_considered": true
    },
    "process_quality": "yes",
    "process_quality_analysis": {
      "factors_for": [
        "employer initiated dialogue promptly after the accommodation request — factor for good faith"
      ],
      "factors_against": [],
      "key_uncertainties": [],
      "nonparticipation_weighting_applied": true
    },
    "interactive_process_compliant": "yes",
    "interactive_process_risk_level": "low"
  },
  "medical_inquiry_limitations": {
    "inquiry_evaluations": [],
    "medical_inquiry_compliant": true,
    "medical_inquiry_risk_level": "minimal"
  },
  "confidentiality": {
    "confidentiality_checks": {
      "separate_file_maintained": true,
      "access_properly_limited": true,
      "no_unauthorized_disclosure": true
    },
    "confidentiality_compliant": true,
    "violated_requirements": [],
    "confidentiality_risk_level": "minimal"
  }
}
```

---

## EO-005 — Pre-Offer Inquiry Violation: Disability-Related Question Before Job Offer

### Fact Pattern
During a job interview for a warehouse position, the hiring manager asks the applicant: "Do you have any physical conditions that would prevent you from lifting 50 pounds?" and "Have you ever filed a workers' compensation claim?" Both questions are asked before any conditional job offer is extended. The employer is a covered entity. No accommodation request has been made — this is purely a pre-offer inquiry issue.

### Legal Analysis
- **3.1:** No accommodation request made — interactive process component is not evaluated.
- **3.2 (pre-offer):** Both questions are disability-related questions at the pre-offer stage. "Physical conditions" question and "workers' compensation" question are classic EEOC examples of prohibited pre-offer disability-related inquiries. Both trigger R054. inquiry_permitted = no for both. violation_basis = pre_offer_disability_question_prohibited. Risk: critical.
- **3.3:** No medical information obtained or stored — no confidentiality analysis needed.

### Rules Fired
R054 (pre-offer disability question — both inquiries), R054 (applied twice for two inquiries)

### Structured Input
```json
{
  "dependency_inputs": {
    "is_covered_employer": true,
    "is_covered_individual": true,
    "accommodation_required": "indeterminate"
  },
  "interactive_process": null,
  "medical_inquiry_limitations": {
    "multiple_inquiry_stages": [
      {
        "inquiry_stage": "pre_offer",
        "inquiry_type": "disability_related_question",
        "inquiry_description": "Hiring manager asked: 'Do you have any physical conditions that would prevent you from lifting 50 pounds?'"
      },
      {
        "inquiry_stage": "pre_offer",
        "inquiry_type": "disability_related_question",
        "inquiry_description": "Hiring manager asked: 'Have you ever filed a workers' compensation claim?'"
      }
    ]
  },
  "confidentiality": null
}
```

### Expected Output
```json
{
  "interactive_process": null,
  "medical_inquiry_limitations": {
    "inquiry_evaluations": [
      {
        "inquiry_stage": "pre_offer",
        "inquiry_type": "disability_related_question",
        "inquiry_permitted": "no",
        "violation_basis": "pre_offer_disability_question_prohibited",
        "source_citation": "42 U.S.C. § 12112(d)(2); 29 CFR § 1630.13(a)"
      },
      {
        "inquiry_stage": "pre_offer",
        "inquiry_type": "disability_related_question",
        "inquiry_permitted": "no",
        "violation_basis": "pre_offer_disability_question_prohibited",
        "source_citation": "42 U.S.C. § 12112(d)(2); 29 CFR § 1630.13(a)"
      }
    ],
    "medical_inquiry_compliant": false,
    "medical_inquiry_risk_level": "critical"
  },
  "confidentiality": null
}
```

---

## EO-006 — During-Employment Inquiry Without Business Necessity

### Fact Pattern
A long-tenured accounts receivable clerk requests a reasonable accommodation for depression. During the accommodation process, HR requires the employee to undergo a comprehensive psychological evaluation — going far beyond documentation of functional limitations — and asks the employee's treating physician for a full psychiatric history. The disability and need for accommodation are already established from prior documentation. The employer cannot articulate a business necessity basis for the expanded examination beyond general curiosity about the employee's full medical history.

### Legal Analysis
- **3.1:** The interactive process component is evaluated separately and is not the focus here.
- **3.2 (during-employment):** The comprehensive psychological evaluation and full psychiatric history request are medical examinations / disability-related inquiries during employment. job-related = arguably yes (related to the accommodation). business necessity = no (the disability and functional limitations are already established; a full psychiatric history goes beyond what is necessary). Rule R063 fires: job-related but not business necessity. inquiry_permitted = no. Risk: high.
- **3.3:** Compliant.

### Rules Fired
R063 (during-employment — job-related but not business necessity), R064 (confidentiality — compliant)

### Structured Input
```json
{
  "dependency_inputs": {
    "is_covered_employer": true,
    "is_covered_individual": true,
    "accommodation_required": "yes"
  },
  "interactive_process": {
    "request_acknowledged": true,
    "accommodation_request_date": "2026-03-10",
    "dialogue_initiated_date": "2026-03-14",
    "business_days_to_initiation": 3,
    "accommodation_options_documented": true,
    "employer_initiated_dialogue_promptly": true,
    "multiple_alternatives_considered": true,
    "jan_or_equivalent_consulted": false,
    "decision_communicated_with_explanation": true,
    "follow_up_on_implemented_accommodation": false,
    "employer_delayed_without_explanation": false,
    "all_options_rejected_without_rationale": false,
    "relied_on_disability_stereotypes": false,
    "process_terminated_unilaterally": false,
    "employee_interactive_process_participation": "good_faith"
  },
  "medical_inquiry_limitations": {
    "multiple_inquiry_stages": [
      {
        "inquiry_stage": "during_employment",
        "inquiry_type": "medical_examination",
        "inquiry_description": "Comprehensive psychological evaluation and full psychiatric history from treating physician, beyond established functional limitations",
        "during_employment_inquiry_job_related": true,
        "during_employment_inquiry_business_necessity": false,
        "during_employment_voluntary_wellness": false
      }
    ]
  },
  "confidentiality": {
    "medical_info_in_separate_file": true,
    "access_limited_to_permitted_parties": true,
    "unauthorized_disclosure_occurred": false
  }
}
```

### Expected Output
```json
{
  "interactive_process": {
    "process_mechanically_compliant": true,
    "process_quality": "indeterminate",
    "interactive_process_compliant": "indeterminate",
    "interactive_process_risk_level": "low"
  },
  "medical_inquiry_limitations": {
    "inquiry_evaluations": [
      {
        "inquiry_stage": "during_employment",
        "inquiry_type": "medical_examination",
        "inquiry_permitted": "no",
        "violation_basis": "during_employment_not_business_necessity",
        "source_citation": "42 U.S.C. § 12112(d)(4)(A); 29 CFR § 1630.14(c)"
      }
    ],
    "medical_inquiry_compliant": false,
    "medical_inquiry_risk_level": "high"
  },
  "confidentiality": {
    "confidentiality_checks": {
      "separate_file_maintained": true,
      "access_properly_limited": true,
      "no_unauthorized_disclosure": true
    },
    "confidentiality_compliant": true,
    "violated_requirements": [],
    "confidentiality_risk_level": "minimal"
  }
}
```

---

## EO-007 — Confidentiality Breach: Medical File Not Maintained Separately and Unauthorized Disclosure

### Fact Pattern
A restaurant chain completes a post-offer medical examination for all new kitchen staff (uniformly applied, proper conditions). The results are filed in each employee's general personnel folder rather than a separate medical file. Additionally, an HR clerk who has no need-to-know in terms of the employee's work restrictions shares the examination results with the employee's direct coworkers during a team meeting, ostensibly to "explain why the employee has different duties."

### Legal Analysis
- **3.1:** Interactive process not at issue — this is a post-offer examination scenario.
- **3.2 (post-offer):** All three post-offer conditions met: all employees in job category examined (true), but information kept confidential = false (commingled in personnel file). R058 fires for the confidentiality condition failure at the inquiry stage. inquiry_permitted = no.
- **3.3:** Two violations: (1) separate file not maintained (R065), (2) unauthorized disclosure to coworkers (R067). confidentiality_compliant = false. Risk: high (coworker disclosure) compounding to critical given external disclosure of diagnosis in workplace meeting context.

### Rules Fired
R057 (post-offer — confidentiality not maintained at inquiry evaluation level), R065 (confidentiality — separate file not maintained), R067 (confidentiality — unauthorized disclosure to coworkers)

### Structured Input
```json
{
  "dependency_inputs": {
    "is_covered_employer": true,
    "is_covered_individual": true,
    "accommodation_required": "indeterminate"
  },
  "interactive_process": null,
  "medical_inquiry_limitations": {
    "multiple_inquiry_stages": [
      {
        "inquiry_stage": "post_offer",
        "inquiry_type": "medical_examination",
        "inquiry_description": "Post-offer medical examination for all new kitchen staff",
        "post_offer_all_employees_examined": true,
        "post_offer_information_kept_confidential": false,
        "post_offer_results_used_only_as_permitted": false
      }
    ]
  },
  "confidentiality": {
    "medical_info_in_separate_file": false,
    "access_limited_to_permitted_parties": false,
    "unauthorized_disclosure_occurred": true,
    "disclosure_parties": ["coworker_without_need_to_know"]
  }
}
```

### Expected Output
```json
{
  "interactive_process": null,
  "medical_inquiry_limitations": {
    "inquiry_evaluations": [
      {
        "inquiry_stage": "post_offer",
        "inquiry_type": "medical_examination",
        "inquiry_permitted": "no",
        "violation_basis": "post_offer_confidentiality_not_maintained",
        "source_citation": "42 U.S.C. § 12112(d)(3)(B); 29 CFR § 1630.14(b)(1)"
      }
    ],
    "medical_inquiry_compliant": false,
    "medical_inquiry_risk_level": "high"
  },
  "confidentiality": {
    "confidentiality_checks": {
      "separate_file_maintained": false,
      "access_properly_limited": false,
      "no_unauthorized_disclosure": false
    },
    "confidentiality_compliant": false,
    "violated_requirements": [
      {
        "requirement": "separate_file_not_maintained",
        "source_citation": "42 U.S.C. § 12112(d)(3)(B); 29 CFR § 1630.14(b)(1)",
        "description": "Medical information was not maintained on separate forms and in separate files from general personnel records."
      },
      {
        "requirement": "unauthorized_disclosure_occurred",
        "source_citation": "42 U.S.C. § 12112(d)(3)(B); 29 CFR § 1630.14(b)(1)",
        "description": "Medical examination results were disclosed to coworkers without need-to-know, outside the three permitted categories."
      }
    ],
    "confidentiality_risk_level": "high"
  }
}
```

---

## EO-008 — Mixed Scenario: Interactive Process Indeterminate + Inquiry Violation

### Fact Pattern
An office manager with bipolar disorder requests a schedule modification. The employer acknowledges the request (3 days) and initiates dialogue (8 business days — within heuristic). It documents one option considered. However, the employer also asked the employee during employment: "Has your psychiatric condition ever required hospitalization?" without any documented business necessity basis. The employer considered only one alternative, communicated no explanation, and did not follow up after partially implementing the accommodation. No confidentiality violations.

### Legal Analysis
- **3.1a:** Acknowledged — yes. Initiated in 8 business days — yes (within heuristic). Options documented — yes. process_mechanically_compliant = true.
- **3.1b:** Factors for: employer_initiated_dialogue_promptly (PQ-F01 — 8 days is prompt). Factors against: zero explicit factors triggered (no explanation failure if accommodation was partly implemented; no rationale rejection; no stereotypes). But no JAN consultation, no multiple alternatives, no follow-up. Result: 1 factor for, 0 against → indeterminate (does not reach ≥3 threshold for yes; does not reach ≥2 against for no). process_quality = indeterminate.
- **3.1c:** true + indeterminate = indeterminate. interactive_process_compliant = indeterminate. Risk: low.
- **3.2 (during-employment):** "Has your psychiatric condition ever required hospitalization?" is a disability-related question. job-related = no (the employer cannot articulate job-relatedness). R062 fires. inquiry_permitted = no. Risk: high.
- **3.3:** Compliant.

### Rules Fired
R047 (mechanical — all pass), R051 (process quality — 1 factor for, 0 against → indeterminate), R052 (composite — true+indeterminate=indeterminate), R062 (during-employment inquiry not job-related), R064 (confidentiality)

### Structured Input
```json
{
  "dependency_inputs": {
    "is_covered_employer": true,
    "is_covered_individual": true,
    "accommodation_required": "yes"
  },
  "interactive_process": {
    "request_acknowledged": true,
    "accommodation_request_date": "2026-04-01",
    "dialogue_initiated_date": "2026-04-11",
    "business_days_to_initiation": 8,
    "accommodation_options_documented": true,
    "employer_initiated_dialogue_promptly": true,
    "multiple_alternatives_considered": false,
    "jan_or_equivalent_consulted": false,
    "decision_communicated_with_explanation": false,
    "follow_up_on_implemented_accommodation": false,
    "employer_delayed_without_explanation": false,
    "all_options_rejected_without_rationale": false,
    "relied_on_disability_stereotypes": false,
    "process_terminated_unilaterally": false,
    "employee_interactive_process_participation": "good_faith"
  },
  "medical_inquiry_limitations": {
    "multiple_inquiry_stages": [
      {
        "inquiry_stage": "during_employment",
        "inquiry_type": "disability_related_question",
        "inquiry_description": "HR asked: 'Has your psychiatric condition ever required hospitalization?'",
        "during_employment_inquiry_job_related": false,
        "during_employment_inquiry_business_necessity": false,
        "during_employment_voluntary_wellness": false
      }
    ]
  },
  "confidentiality": {
    "medical_info_in_separate_file": true,
    "access_limited_to_permitted_parties": true,
    "unauthorized_disclosure_occurred": false
  }
}
```

### Expected Output
```json
{
  "interactive_process": {
    "process_mechanically_compliant": true,
    "mechanical_compliance_checks": {
      "acknowledged_request": true,
      "initiated_dialogue_timely": true,
      "documented_options_considered": true
    },
    "process_quality": "indeterminate",
    "process_quality_analysis": {
      "factors_for": [
        "employer initiated dialogue promptly after the accommodation request — factor for good faith"
      ],
      "factors_against": [],
      "key_uncertainties": [
        "Insufficient good-faith factors to confirm compliance (only 1 of required 3 factors for present); no factors against identified; additional context on decision communication and alternatives may resolve"
      ],
      "nonparticipation_weighting_applied": false
    },
    "interactive_process_compliant": "indeterminate",
    "interactive_process_risk_level": "low"
  },
  "medical_inquiry_limitations": {
    "inquiry_evaluations": [
      {
        "inquiry_stage": "during_employment",
        "inquiry_type": "disability_related_question",
        "inquiry_permitted": "no",
        "violation_basis": "during_employment_not_job_related",
        "source_citation": "42 U.S.C. § 12112(d)(4)(A); 29 CFR § 1630.14(c)"
      }
    ],
    "medical_inquiry_compliant": false,
    "medical_inquiry_risk_level": "high"
  },
  "confidentiality": {
    "confidentiality_checks": {
      "separate_file_maintained": true,
      "access_properly_limited": true,
      "no_unauthorized_disclosure": true
    },
    "confidentiality_compliant": true,
    "violated_requirements": [],
    "confidentiality_risk_level": "minimal"
  }
}
```
