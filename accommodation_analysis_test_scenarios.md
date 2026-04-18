# ADA Decision Engine — Accommodation Analysis Test Scenarios
## Module 2 | Version 0.2 | 2026-04-17

Ten attorney-reviewable test scenarios. Each maps exactly to a fixture in `accommodation_analysis_test_fixtures.json`. Module 1 dependency inputs are included in each Structured Input section, clearly labeled.

---

## AA-001 — Clear Accommodation Required: Ergonomic Chair, Large Employer

**Scenario ID:** AA-001
**Scenario Name:** Accommodation Required — Ergonomic Chair for Employee with Lumbar Condition, Large Employer, No Hardship, No Threat

**Fact Pattern:** Patricia Owens is a data entry specialist at NatioTech Corp, a covered private employer with 2,400 employees and $180 million in annual revenue. She has chronic lumbar disc disease (a qualifying actual disability under Module 1) that substantially limits her ability to sit for extended periods. She requests an ergonomic chair with adjustable lumbar support, estimated at $400 one-time cost. NatioTech does not assert undue hardship or direct threat. Patricia can perform all essential functions of her data entry role with the ergonomic chair.

**Legal Analysis:**
- **Rule (Request):** Valid — made by employee, functional limitation identified, for performing_job_functions. R026.
- **Rule (Hardship):** Employer does not assert hardship. R029 — automatic no.
- **Rule (Threat):** No threat claimed. R032 — automatic no.
- **Rule (Determination):** All thresholds pass. No defenses. R045 — accommodation required.
- **Conclusion:** Accommodation required. Net cost $400 (0.00% of $180M revenue). No operational impact. No procedural issues.

**Structured Input (JSON):**
```json
{
  "module_1_inputs": {
    "is_covered_employer": true,
    "is_covered_individual": true,
    "has_qualifying_disability": "yes",
    "accommodation_rights_attach": true,
    "is_qualified_individual": "yes"
  },
  "accommodation_request": {
    "accommodation_type_requested": "equipment_modification",
    "accommodation_description": "Ergonomic chair with adjustable lumbar support",
    "accommodation_request_date": "2026-03-01",
    "request_made_by": "employee",
    "accommodation_is_for": "performing_job_functions",
    "functional_limitation_identified": true,
    "accommodation_request_in_writing": true
  },
  "undue_hardship_analysis": {
    "accommodation_gross_cost": 400,
    "tax_credits_available": 0,
    "outside_funding_available": 0,
    "accommodation_net_cost": 400,
    "accommodation_frequency": "one_time",
    "facility_annual_revenue": 180000000,
    "facility_employee_count": 2400,
    "entity_annual_revenue": 180000000,
    "entity_total_employees": 2400,
    "entity_type": "single_facility",
    "impact_on_operations": "none",
    "impact_on_other_employees": "none",
    "employer_asserts_hardship": false,
    "employer_documented_hardship_analysis": false
  },
  "direct_threat_analysis": {
    "direct_threat_claimed": false
  }
}
```

**Expected Output (JSON):**
```json
{
  "accommodation_request": {
    "accommodation_request_valid": true,
    "accommodation_category": "equipment_modification",
    "request_validity_basis": "employee_request_with_limitation",
    "reasoning": "The accommodation request was made by the employee and identified a functional limitation (extended sitting) requiring an adjustment to performing_job_functions. Under EEOC Enforcement Guidance No. 915.002, no magic words are required. This request meets the threshold for validity.",
    "sources_cited": ["29 CFR § 1630.2(o)(1)", "EEOC Enforcement Guidance No. 915.002 § Requesting Reasonable Accommodation"]
  },
  "undue_hardship_analysis": {
    "undue_hardship_applies": "no",
    "undue_hardship_analysis": {
      "cost_burden_ratio": 0.0,
      "cost_burden_denominator_used": "facility_annual_revenue",
      "factors_for_hardship": [],
      "factors_against_hardship": ["employer has not asserted undue hardship — defense not raised"],
      "key_uncertainties": []
    },
    "alternative_accommodations_available": false,
    "alternative_accommodations_suggested": [],
    "reasoning": "Employer has not asserted undue hardship. Under 42 U.S.C. § 12112(b)(5)(A), undue hardship is an affirmative defense that must be raised by the employer. Defense not raised; undue_hardship_applies is no.",
    "sources_cited": ["42 U.S.C. § 12112(b)(5)(A)", "29 CFR § 1630.15(d)"]
  },
  "direct_threat_analysis": {
    "direct_threat_exists": "no",
    "direct_threat_analysis": {
      "factors_for_threat": [],
      "factors_against_threat": ["employer has not asserted direct threat defense"],
      "mitigation_possible": null,
      "assessment_methodology_adequate": null,
      "key_uncertainties": []
    },
    "reasoning": "Employer has not asserted direct threat. direct_threat_exists is no.",
    "sources_cited": ["42 U.S.C. § 12113(b)", "29 CFR § 1630.15(b)(2)"]
  },
  "accommodation_determination": {
    "accommodation_required": "yes",
    "accommodation_type_approved": "equipment_modification",
    "denial_basis": null,
    "factors_summary": {
      "factors_for_accommodation": [
        "covered employer and covered individual confirmed",
        "qualifying disability with accommodation rights established",
        "individual is qualified — can perform all essential functions with ergonomic chair",
        "valid accommodation request — employee identified functional limitation",
        "no undue hardship asserted",
        "no direct threat claimed"
      ],
      "factors_against_accommodation": []
    },
    "recommended_actions": [
      "Provide the ergonomic chair with adjustable lumbar support as requested",
      "Document the accommodation in the interactive process file (not in the personnel file)",
      "Follow up within 30 days to confirm accommodation is effective"
    ],
    "reasoning": "All threshold requirements are satisfied. No defenses apply. Under 42 U.S.C. § 12112(b)(5)(A) and 29 CFR § 1630.9(a), NatioTech Corp must provide the ergonomic chair. Net cost of $400 represents 0.00% of $180M annual revenue — a de minimis expense for this employer.",
    "sources_cited": ["42 U.S.C. § 12112(b)(5)(A)", "29 CFR § 1630.9(a)"]
  }
}
```

---

## AA-002 — Undue Hardship: Small Employer, High-Cost Facility Modification

**Scenario ID:** AA-002
**Scenario Name:** Undue Hardship Established — Small Private Employer, $80,000 Structural Modification

**Fact Pattern:** Carlos Mendez is a warehouse worker at QuickShip LLC, a private employer with 18 employees and $1.2 million in annual revenue (a single-facility, decentralized operation). Carlos has a mobility impairment requiring a wheelchair and requests installation of a freight elevator to access the upper mezzanine level where some storage functions occur. The estimated cost is $80,000 (one-time). QuickShip asserts undue hardship, has documented a detailed analysis, and has also identified that Carlos can perform 90% of his essential functions on the ground floor without elevator access. No tax credits or outside funding are available.

**Legal Analysis:**
- **Rule (Request):** Valid — employee, limitation identified, performing_job_functions. R026.
- **Rule (Hardship):** Employer asserts and documents hardship. R031. Cost burden ratio: $80,000 / $1,200,000 = 6.67%. Factor UH-F01 fires (>5%). Factor UH-F04 fires (18 employees < 25, cost > $5,000). Impact moderate (upper mezzanine temporarily inaccessible during construction). factors_for ≥ 3 (UH-F01, UH-F04, plus moderate impact approaching significant), factors_against ≤ 1. UH applies = yes.
- **Conclusion:** Undue hardship established. Accommodation required = no. BUT: employer must consider alternatives (job restructuring to eliminate mezzanine functions, or portable lift equipment at lower cost).

**Structured Input (JSON):**
```json
{
  "module_1_inputs": {
    "is_covered_employer": true,
    "is_covered_individual": true,
    "has_qualifying_disability": "yes",
    "accommodation_rights_attach": true,
    "is_qualified_individual": "yes"
  },
  "accommodation_request": {
    "accommodation_type_requested": "facility_access",
    "accommodation_description": "Freight elevator installation for mezzanine access",
    "accommodation_request_date": "2026-02-10",
    "request_made_by": "employee",
    "accommodation_is_for": "performing_job_functions",
    "functional_limitation_identified": true,
    "accommodation_request_in_writing": true
  },
  "undue_hardship_analysis": {
    "accommodation_gross_cost": 80000,
    "tax_credits_available": 0,
    "outside_funding_available": 0,
    "accommodation_net_cost": 80000,
    "accommodation_frequency": "one_time",
    "facility_annual_revenue": 1200000,
    "facility_employee_count": 18,
    "facility_operating_budget": 950000,
    "entity_annual_revenue": 1200000,
    "entity_total_employees": 18,
    "entity_number_of_facilities": 1,
    "entity_type": "single_facility",
    "administrative_relationship": "decentralized",
    "geographic_separateness": false,
    "impact_on_operations": "moderate",
    "impact_on_other_employees": "minor",
    "impact_description": "Construction would temporarily block loading dock access for approximately 6 weeks",
    "employer_asserts_hardship": true,
    "employer_documented_hardship_analysis": true,
    "alternative_accommodation_considered": false
  },
  "direct_threat_analysis": {
    "direct_threat_claimed": false
  }
}
```

**Expected Output (JSON):**
```json
{
  "accommodation_request": {
    "accommodation_request_valid": true,
    "accommodation_category": "facility_access",
    "request_validity_basis": "employee_request_with_limitation",
    "reasoning": "Valid accommodation request. Employee identified mobility impairment as functional limitation requiring facility access modification for performing_job_functions.",
    "sources_cited": ["29 CFR § 1630.2(o)(1)", "EEOC Enforcement Guidance No. 915.002 § Requesting Reasonable Accommodation"]
  },
  "undue_hardship_analysis": {
    "undue_hardship_applies": "yes",
    "undue_hardship_analysis": {
      "cost_burden_ratio": 8.42,
      "cost_burden_denominator_used": "facility_operating_budget",
      "factors_for_hardship": [
        "cost burden ratio exceeds 5% of facility_operating_budget (8.42%) — high cost relative to facility resources under 29 CFR § 1630.2(p)(2)(i)-(ii)",
        "impact on facility operations is moderate — notable operational disruption weighs toward hardship under 29 CFR § 1630.2(p)(2)(ii)",
        "small entity (18 employees) with gross accommodation cost of $80,000 — small employer size weighs toward hardship under 29 CFR § 1630.2(p)(2)(ii); NOTE: $5,000 threshold is an engine heuristic, not a statutory figure — flagged for review"
      ],
      "factors_against_hardship": [
        "employer has not considered alternative lower-cost accommodations before asserting hardship — failure to explore alternatives weighs against hardship defense per EEOC Enforcement Guidance No. 915.002 § Undue Hardship"
      ],
      "key_uncertainties": []
    },
    "alternative_accommodations_available": true,
    "alternative_accommodations_suggested": [
      "Job restructuring to reassign mezzanine-only functions to other employees (marginal function analysis required)",
      "Portable powered stair climber or lift equipment (approximate cost $3,000–$8,000)",
      "Reorganize storage layout so all functions essential to Carlos's role are ground-floor accessible"
    ],
    "reasoning": "Net accommodation cost: $80,000 (8.42% of $950,000 facility operating budget). Entity resources: 18 employees, $1.2M annual revenue — a small, single-facility operation. Operational impact: moderate (6-week construction disruption to loading dock). Under 29 CFR § 1630.2(p), both facility and entity resources must be considered. Three factors support hardship: cost burden ratio, small entity size, and operational impact. One factor weighs against: employer did not explore alternative accommodations. Factors_for (3) > factors_against (1); employer has documented the analysis; burden of proof met. Undue hardship applies. However, under EEOC Enforcement Guidance No. 915.002, the employer must still consider whether a less burdensome alternative accommodation is effective.",
    "sources_cited": ["42 U.S.C. § 12111(10)", "29 CFR § 1630.2(p)(2)(i)-(iii)", "29 CFR § 1630.15(d)", "EEOC Enforcement Guidance No. 915.002 §§ 42–46"]
  },
  "direct_threat_analysis": {
    "direct_threat_exists": "no",
    "direct_threat_analysis": {
      "factors_for_threat": [],
      "factors_against_threat": ["employer has not asserted direct threat defense"],
      "mitigation_possible": null,
      "assessment_methodology_adequate": null,
      "key_uncertainties": []
    },
    "reasoning": "No direct threat claimed.",
    "sources_cited": ["42 U.S.C. § 12113(b)"]
  },
  "accommodation_determination": {
    "accommodation_required": "no",
    "accommodation_type_approved": null,
    "denial_basis": "undue_hardship",
    "factors_summary": {
      "factors_for_accommodation": [
        "covered employer and individual confirmed",
        "qualifying disability with accommodation rights",
        "valid accommodation request"
      ],
      "factors_against_accommodation": [
        "undue hardship established: cost burden ratio 8.42% of operating budget for 18-employee entity",
        "moderate operational disruption during construction"
      ]
    },
    "recommended_actions": [
      "Explore alternative lower-cost accommodations (portable lift, job restructuring, storage reorganization) before issuing final denial",
      "Document the alternative accommodation exploration in the interactive process file",
      "If alternatives are not effective, provide written explanation of the undue hardship determination with supporting documentation",
      "Consider whether state vocational rehabilitation or tax credits (IRS Form 8826) may offset costs of alternative options"
    ],
    "reasoning": "All threshold requirements are met but undue hardship is established for the elevator installation. Under 42 U.S.C. § 12112(b)(5)(A), the employer need not provide an accommodation that imposes undue hardship. However, the employer must still explore whether alternative, less burdensome accommodations can effectively address the functional limitation before issuing a final denial.",
    "sources_cited": ["42 U.S.C. § 12112(b)(5)(A)", "29 CFR § 1630.15(d)", "EEOC Enforcement Guidance No. 915.002 § Undue Hardship Issues"]
  }
}
```

---

## AA-003 — No Undue Hardship: Large Employer Asserts Cost Defense

**Scenario ID:** AA-003
**Scenario Name:** Undue Hardship Defense Fails — Fortune 500 Employer, $50,000 Cost Ratio Below 0.1%

**Fact Pattern:** Diane Okafor is a software engineer at MegaCorp Inc., a national technology company with 45,000 employees and $2.1 billion in annual revenue. Diane has a hearing impairment (qualifying disability) and requests installation of specialized caption software and a hardware amplification system for her workstation, estimated at $50,000 one-time cost. MegaCorp asserts undue hardship, has documented the analysis, and reports no operational impact and no impact on other employees. No alternative accommodations have been considered.

**Legal Analysis:**
- **Rule (Hardship):** Employer asserts and documents hardship. R031. Cost burden ratio: $50,000 / $2,100,000,000 = 0.002%. Factor UH-A01 fires (<1%) — low ratio. Factor UH-A02 fires (45,000 employees, $2.1B revenue — large entity). Factor UH-A03 fires (impact_on_operations = none). Factor UH-A04 fires (impact_on_other_employees = none). Factor UH-A06 fires (alternative not considered). factors_for = 0, factors_against = 5. UH applies = no.
- **Conclusion:** No undue hardship. Accommodation required = yes.

**Structured Input (JSON):**
```json
{
  "module_1_inputs": {
    "is_covered_employer": true,
    "is_covered_individual": true,
    "has_qualifying_disability": "yes",
    "accommodation_rights_attach": true,
    "is_qualified_individual": "yes"
  },
  "accommodation_request": {
    "accommodation_type_requested": "equipment_modification",
    "accommodation_description": "Specialized caption software and hardware amplification system",
    "accommodation_request_date": "2026-01-15",
    "request_made_by": "employee",
    "accommodation_is_for": "performing_job_functions",
    "functional_limitation_identified": true,
    "accommodation_request_in_writing": true
  },
  "undue_hardship_analysis": {
    "accommodation_gross_cost": 50000,
    "tax_credits_available": 0,
    "outside_funding_available": 0,
    "accommodation_net_cost": 50000,
    "accommodation_frequency": "one_time",
    "facility_annual_revenue": 2100000000,
    "facility_employee_count": 45000,
    "entity_annual_revenue": 2100000000,
    "entity_total_employees": 45000,
    "entity_number_of_facilities": 28,
    "entity_type": "multi_facility_national",
    "administrative_relationship": "centralized",
    "geographic_separateness": false,
    "impact_on_operations": "none",
    "impact_on_other_employees": "none",
    "employer_asserts_hardship": true,
    "employer_documented_hardship_analysis": true,
    "alternative_accommodation_considered": false
  },
  "direct_threat_analysis": {
    "direct_threat_claimed": false
  }
}
```

**Expected Output (JSON):**
```json
{
  "undue_hardship_analysis": {
    "undue_hardship_applies": "no",
    "undue_hardship_analysis": {
      "cost_burden_ratio": 0.0,
      "cost_burden_denominator_used": "facility_annual_revenue",
      "factors_for_hardship": [],
      "factors_against_hardship": [
        "cost burden ratio is 0.0% of facility_annual_revenue — low cost relative to facility resources weighs against hardship under 29 CFR § 1630.2(p)(2)(i)-(ii); NOTE: 1% threshold is an engine heuristic — flagged for review",
        "employer has not considered alternative lower-cost accommodations before asserting hardship — failure to explore alternatives weighs against hardship defense per EEOC Enforcement Guidance No. 915.002 § Undue Hardship",
        "impact on other employees is none — minimal employee disruption weighs against hardship under 29 CFR § 1630.2(p)(2)(ii)",
        "large entity (45000 employees, $2100000000 annual revenue) — substantial resources weigh against hardship under 29 CFR § 1630.2(p)(2)(ii)",
        "operational impact is none — minimal operations disruption weighs against hardship under 29 CFR § 1630.2(p)(2)(ii)"
      ],
      "key_uncertainties": []
    },
    "alternative_accommodations_available": false,
    "alternative_accommodations_suggested": [],
    "reasoning": "Net accommodation cost: $50,000 (0.00% of $2.1B annual revenue). Entity resources: 45,000 employees, $2.1B annual revenue — a large national multi-facility employer. Operational impact: none. Employee impact: none. Under 29 CFR § 1630.2(p), both facility and entity resources must be considered. Five factors weigh against hardship: negligible cost ratio, large entity size, zero operational impact, zero employee impact, and failure to explore alternatives. Zero factors support hardship. Factors_for (0) << factors_against (5). Undue hardship is not established. The employer's assertion of hardship is not supported by the factual record.",
    "sources_cited": ["42 U.S.C. § 12111(10)", "29 CFR § 1630.2(p)(2)(i)-(iii)", "29 CFR § 1630.15(d)", "EEOC Enforcement Guidance No. 915.002 §§ 42–46"]
  },
  "accommodation_determination": {
    "accommodation_required": "yes",
    "accommodation_type_approved": "equipment_modification",
    "denial_basis": null,
    "factors_summary": {
      "factors_for_accommodation": [
        "all coverage and eligibility thresholds met",
        "valid accommodation request",
        "undue hardship defense rejected: cost burden is 0.00% of $2.1B revenue; no operational or employee impact",
        "no direct threat claimed"
      ],
      "factors_against_accommodation": []
    },
    "recommended_actions": [
      "Provide caption software and hardware amplification system as requested",
      "Document accommodation in interactive process file",
      "Follow up within 30 days to confirm effectiveness"
    ],
    "reasoning": "Undue hardship defense fails. $50,000 represents a de minimis expense for a $2.1B employer. Under 42 U.S.C. § 12112(b)(5)(A) and 29 CFR § 1630.9(a), MegaCorp must provide the accommodation.",
    "sources_cited": ["42 U.S.C. § 12112(b)(5)(A)", "29 CFR § 1630.9(a)"]
  }
}
```

---

## AA-004 — Indeterminate Undue Hardship: Mid-Size Employer, Moderate Cost Ratio, Partial Documentation

**Scenario ID:** AA-004
**Scenario Name:** Indeterminate Undue Hardship — Mid-Size Employer, 3.4% Cost Ratio, Moderate Impact, Incomplete Documentation

**Fact Pattern:** James Whitfield is a laboratory technician at BioResearch Inc., a mid-size employer with 95 employees and $4.8 million in annual operating budget. James has a qualifying visual impairment and requests specialized screen magnification hardware and software for his workstation, estimated at $16,500 one-time. BioResearch asserts undue hardship and has produced a partial financial analysis covering cost only (not operational impact factors). The operational impact is described as moderate (other technicians may need workflow adjustments during a 2-week setup period). No alternative accommodations were considered.

**Legal Analysis:**
- **Rule (Hardship):** Employer asserts hardship and has partially documented. Documentation is partial — covers cost but not all statutory factors. R030 applies (undocumented analysis → indeterminate) but employer's documentation is partial, not absent. Treat as R031 with indeterminate output due to mixed factors and incomplete burden-of-proof satisfaction.
- **Application:** Cost burden ratio: $16,500 / $4,800,000 = 0.34%. UH-F01 does NOT fire (0.34% < 5%). UH-A01 does NOT fire (0.34% > 1% but < 5%). UH-F02 does NOT fire (moderate, not significant/severe). UH-A03 does NOT fire (moderate, not none/minor). UH-A06 fires (no alternative considered). factors_for: 0. factors_against: 1 (UH-A06). Mixed — neither clear threshold met. Output: indeterminate.
- **Conclusion:** Indeterminate. Additional documentation and alternative accommodation exploration needed.

**Structured Input (JSON):**
```json
{
  "module_1_inputs": {
    "is_covered_employer": true,
    "is_covered_individual": true,
    "has_qualifying_disability": "yes",
    "accommodation_rights_attach": true,
    "is_qualified_individual": "yes"
  },
  "accommodation_request": {
    "accommodation_type_requested": "equipment_modification",
    "accommodation_description": "Screen magnification hardware and software system for laboratory workstation",
    "accommodation_request_date": "2026-03-20",
    "request_made_by": "employee",
    "accommodation_is_for": "performing_job_functions",
    "functional_limitation_identified": true,
    "accommodation_request_in_writing": true
  },
  "undue_hardship_analysis": {
    "accommodation_gross_cost": 16500,
    "tax_credits_available": 0,
    "outside_funding_available": 0,
    "accommodation_net_cost": 16500,
    "accommodation_frequency": "one_time",
    "facility_annual_revenue": 5200000,
    "facility_employee_count": 95,
    "facility_operating_budget": 4800000,
    "entity_annual_revenue": 5200000,
    "entity_total_employees": 95,
    "entity_number_of_facilities": 1,
    "entity_type": "single_facility",
    "administrative_relationship": "centralized",
    "geographic_separateness": false,
    "impact_on_operations": "moderate",
    "impact_on_other_employees": "moderate",
    "impact_description": "Other technicians require workflow adjustments during 2-week setup; some shared equipment temporarily unavailable",
    "employer_asserts_hardship": true,
    "employer_documented_hardship_analysis": true,
    "alternative_accommodation_considered": false
  },
  "direct_threat_analysis": {
    "direct_threat_claimed": false
  }
}
```

**Expected Output (JSON):**
```json
{
  "undue_hardship_analysis": {
    "undue_hardship_applies": "indeterminate",
    "undue_hardship_analysis": {
      "cost_burden_ratio": 0.34,
      "cost_burden_denominator_used": "facility_operating_budget",
      "factors_for_hardship": [],
      "factors_against_hardship": [
        "employer has not considered alternative lower-cost accommodations before asserting hardship — failure to explore alternatives weighs against hardship defense per EEOC Enforcement Guidance No. 915.002 § Undue Hardship"
      ],
      "key_uncertainties": [
        "cost burden ratio of 0.34% falls between the 1% (clear no) and 5% (clear yes) thresholds — individualized assessment required; neither factor UH-F01 nor UH-A01 fires",
        "operational and employee impact rated moderate — falls between clear minor (factor against) and significant/severe (factor for); additional documentation of specific impacts needed",
        "employer's documented analysis covers cost but not all 29 CFR § 1630.2(p) factors — burden of proof not fully satisfied pending complete factor documentation"
      ]
    },
    "alternative_accommodations_available": true,
    "alternative_accommodations_suggested": [
      "Software-only screen magnification (e.g., ZoomText, MAGic) — estimated $500–$1,500, no hardware required",
      "Tablet-based magnification solution — estimated $800–$2,000",
      "State vocational rehabilitation funding may cover specialized equipment costs"
    ],
    "reasoning": "Net cost: $16,500 (0.34% of $4,800,000 operating budget). This ratio falls in the indeterminate zone between the heuristic thresholds. Entity: 95 employees, $5.2M revenue — mid-size single-facility employer. Operational and employee impact both rated moderate — not clearly minor (which would weigh against hardship) nor significant/severe (which would weigh for hardship). The employer's documentation addresses cost but does not fully analyze all five statutory factor groups under 29 CFR § 1630.2(p). Under 29 CFR § 1630.15(d), the employer bears the burden of proof and must document a complete analysis. Alternative accommodations have not been explored, which weighs against hardship. Additional documentation and alternative exploration are needed before a determination can be made.",
    "sources_cited": ["42 U.S.C. § 12111(10)", "29 CFR § 1630.2(p)(2)(i)-(iii)", "29 CFR § 1630.15(d)", "EEOC Enforcement Guidance No. 915.002 §§ 42–46"]
  },
  "accommodation_determination": {
    "accommodation_required": "indeterminate",
    "accommodation_type_approved": null,
    "denial_basis": null,
    "factors_summary": {
      "factors_for_accommodation": [
        "all coverage and eligibility thresholds met",
        "valid accommodation request",
        "cost burden ratio (0.34%) does not clearly support hardship finding",
        "failure to explore alternative accommodations weighs against hardship defense"
      ],
      "factors_against_accommodation": [
        "employer asserts hardship — defense is live and must be resolved",
        "moderate operational and employee impact require further documentation"
      ]
    },
    "recommended_actions": [
      "Complete a documented analysis of all five statutory undue hardship factor groups under 29 CFR § 1630.2(p) before issuing a determination",
      "Explore and document lower-cost alternative accommodations (software-only solutions)",
      "Investigate state vocational rehabilitation funding sources",
      "Reconvene the interactive process with James to discuss alternatives"
    ],
    "reasoning": "Undue hardship determination is indeterminate due to ambiguous cost ratio and incomplete documentation. Accommodation determination cannot be finalized until hardship analysis is resolved. No other defenses apply.",
    "sources_cited": ["42 U.S.C. § 12112(b)(5)(A)", "29 CFR § 1630.9(a)", "29 CFR § 1630.15(d)"]
  }
}
```

---

## AA-005 — Direct Threat: Clear, Not Mitigable (Uncontrolled Seizures, Commercial Driver)

**Scenario ID:** AA-005
**Scenario Name:** Direct Threat Established — Uncontrolled Seizure Disorder, Commercial Truck Driver, No Viable Mitigation

**Fact Pattern:** Robert Hanson is a commercial truck driver at FreightLine Inc., a covered employer with 380 employees. Robert has been diagnosed with uncontrolled epilepsy — his neurologist has documented that despite medication trials, Robert experiences unpredictable tonic-clonic seizures approximately twice per month. Robert requests continued employment as a long-haul driver. FreightLine has conducted an individualized medical assessment using Robert's neurologist's documentation (current medical knowledge), has not relied on stereotypes, and has concluded that no accommodation can reduce the risk to an acceptable level (e.g., a co-driver does not eliminate the risk during solo unloading operations). The DOT has medically disqualified Robert under federal commercial driver regulations.

**Legal Analysis:**
- **Rule (Threat):** Direct threat claimed. Individualized assessment: yes. No stereotypes. Current medical knowledge: yes. Objective evidence: yes (neurologist letter, DOT disqualification). Cannot mitigate: yes. R036 factor analysis: DT-F01 (probable → highly_likely), DT-F02 (catastrophic — trucking accident), DT-F03 (imminent — seizures ongoing), DT-F04 (ongoing — condition chronic), DT-F05 (objective evidence + current medical knowledge). All five factors for threat fire. Zero against. Threshold: factors_for ≥ 4, factors_against = 0 → direct_threat_exists = yes.
- **Conclusion:** Direct threat established. Accommodation = no, denial_basis = direct_threat. Note: employer must consider reassignment to non-driving position.

**Structured Input (JSON):**
```json
{
  "module_1_inputs": {
    "is_covered_employer": true,
    "is_covered_individual": true,
    "has_qualifying_disability": "yes",
    "accommodation_rights_attach": true,
    "is_qualified_individual": "indeterminate"
  },
  "accommodation_request": {
    "accommodation_type_requested": "policy_modification",
    "accommodation_description": "Continued employment as long-haul commercial truck driver despite medical disqualification",
    "accommodation_request_date": "2026-02-01",
    "request_made_by": "employee",
    "accommodation_is_for": "performing_job_functions",
    "functional_limitation_identified": true,
    "accommodation_request_in_writing": true
  },
  "undue_hardship_analysis": {
    "accommodation_gross_cost": 0,
    "accommodation_net_cost": 0,
    "accommodation_frequency": "ongoing",
    "facility_annual_revenue": 42000000,
    "facility_employee_count": 380,
    "entity_annual_revenue": 42000000,
    "entity_total_employees": 380,
    "impact_on_operations": "none",
    "impact_on_other_employees": "none",
    "employer_asserts_hardship": false,
    "employer_documented_hardship_analysis": false
  },
  "direct_threat_analysis": {
    "direct_threat_claimed": true,
    "threat_to": "others",
    "risk_duration": "ongoing",
    "potential_harm_severity": "catastrophic",
    "harm_likelihood": "highly_likely",
    "harm_imminence": "imminent",
    "individualized_assessment_performed": true,
    "assessment_based_on_current_medical_knowledge": true,
    "objective_evidence_exists": true,
    "evidence_description": "Neurologist letter documenting uncontrolled tonic-clonic seizures averaging twice monthly despite medication; DOT CDL medical disqualification certificate",
    "threat_can_be_mitigated_by_accommodation": false,
    "assessment_relied_on_stereotypes": false
  }
}
```

**Expected Output (JSON):**
```json
{
  "direct_threat_analysis": {
    "direct_threat_exists": "yes",
    "direct_threat_analysis": {
      "factors_for_threat": [
        "assessment is supported by objective evidence and current medical knowledge — procedural requirements of 29 CFR § 1630.2(r) are satisfied",
        "harm imminence is imminent — immediate risk of harm weighs toward direct threat under 29 CFR § 1630.2(r) factor 4",
        "harm likelihood is highly_likely based on objective evidence — high probability of harm is a factor supporting direct threat under 29 CFR § 1630.2(r) factor 3",
        "potential harm severity is catastrophic — catastrophic potential harm weighs strongly toward direct threat under 29 CFR § 1630.2(r) factor 2",
        "risk duration is ongoing — continuous risk weighs toward direct threat under 29 CFR § 1630.2(r) factor 1"
      ],
      "factors_against_threat": [],
      "mitigation_possible": false,
      "assessment_methodology_adequate": true,
      "key_uncertainties": []
    },
    "reasoning": "FreightLine conducted an individualized assessment using current medical knowledge (neurologist letter, DOT disqualification) without relying on stereotypes — procedural requirements of 29 CFR § 1630.2(r) are met. Assessment of all four statutory factors: (1) Risk duration: ongoing (chronic uncontrolled condition). (2) Harm severity: catastrophic (truck accident involving a 40-ton vehicle). (3) Harm likelihood: highly_likely (documented seizures twice monthly despite treatment). (4) Harm imminence: imminent (seizures unpredictable, ongoing). No accommodation can reduce the risk to an acceptable level. All five factors for threat fire; zero factors against. Under 29 CFR § 1630.2(r) and 42 U.S.C. § 12113(b), direct threat is established.",
    "sources_cited": ["42 U.S.C. § 12113(b)", "29 CFR § 1630.2(r)", "29 CFR § 1630.15(b)(2)"]
  },
  "accommodation_determination": {
    "accommodation_required": "no",
    "accommodation_type_approved": null,
    "denial_basis": "direct_threat",
    "factors_summary": {
      "factors_for_accommodation": [
        "qualifying disability established",
        "valid accommodation request"
      ],
      "factors_against_accommodation": [
        "direct threat established: highly likely catastrophic harm, imminent, ongoing, no mitigation available",
        "DOT medical disqualification confirms federal safety standard"
      ]
    },
    "recommended_actions": [
      "Exclude Robert from the CDL truck driver position based on established direct threat",
      "Engage in interactive process to determine whether reassignment to a non-driving position is possible (direct threat applies only to this specific role)",
      "Document the individualized assessment and basis for the direct threat determination in writing",
      "Do not apply direct threat determination to other positions without conducting a separate individualized assessment for each"
    ],
    "reasoning": "Direct threat to others (motorists, pedestrians, co-workers) is established under 42 U.S.C. § 12113(b). The threat cannot be mitigated by reasonable accommodation. FreightLine may exclude Robert from the truck driver position. However, the employer must separately evaluate whether Robert can be reassigned to a non-driving position — the direct threat determination applies to this role, not to Robert's employment generally.",
    "sources_cited": ["42 U.S.C. § 12113(b)", "42 U.S.C. § 12112(b)(5)(A)", "29 CFR § 1630.2(r)"]
  }
}
```

---

## AA-006 — Direct Threat Defense Fails: Stereotype-Based Assessment

**Scenario ID:** AA-006
**Scenario Name:** Direct Threat Defense Fails — Assessment Based on HIV Stereotype, No Individualized Evaluation

**Fact Pattern:** Michael Torres is a dietary aide at Memorial Hospital, a covered state employer. Michael has HIV (a qualifying actual disability — per se substantially limiting immune function). The hospital's food services director learned of Michael's HIV status and, without consulting a physician or conducting any individualized assessment, reassigned Michael from patient food preparation to non-food-contact duties, citing safety concerns about "contamination risk." The hospital asserts direct threat. No objective medical evidence of actual transmission risk was gathered. Michael requests return to his original food preparation duties.

**Legal Analysis:**
- **Rule (Threat):** Direct threat claimed. assessment_relied_on_stereotypes = true. R033 applies — automatic procedural defeater. direct_threat_exists = no regardless of any substantive factors.
- **Application:** The food services director relied on the generalized (and medically inaccurate) assumption that HIV poses a food contamination risk. Current public health and medical consensus establishes that HIV is not transmitted through food handling. The assessment was based on a stereotype, not an individualized evaluation.
- **Conclusion:** Direct threat defense fails. Accommodation required = yes (return to food preparation role).

**Structured Input (JSON):**
```json
{
  "module_1_inputs": {
    "is_covered_employer": true,
    "is_covered_individual": true,
    "has_qualifying_disability": "yes",
    "accommodation_rights_attach": true,
    "is_qualified_individual": "yes"
  },
  "accommodation_request": {
    "accommodation_type_requested": "policy_modification",
    "accommodation_description": "Return to original patient food preparation duties",
    "accommodation_request_date": "2026-03-10",
    "request_made_by": "employee",
    "accommodation_is_for": "performing_job_functions",
    "functional_limitation_identified": true,
    "accommodation_request_in_writing": false
  },
  "undue_hardship_analysis": {
    "accommodation_gross_cost": 0,
    "accommodation_net_cost": 0,
    "accommodation_frequency": "ongoing",
    "facility_annual_revenue": 85000000,
    "facility_employee_count": 1200,
    "entity_annual_revenue": 85000000,
    "entity_total_employees": 1200,
    "impact_on_operations": "none",
    "impact_on_other_employees": "none",
    "employer_asserts_hardship": false,
    "employer_documented_hardship_analysis": false
  },
  "direct_threat_analysis": {
    "direct_threat_claimed": true,
    "threat_to": "others",
    "risk_duration": "permanent",
    "potential_harm_severity": "severe",
    "harm_likelihood": "remote",
    "harm_imminence": "not_imminent",
    "individualized_assessment_performed": false,
    "assessment_based_on_current_medical_knowledge": false,
    "objective_evidence_exists": false,
    "evidence_description": "No medical or public health documentation gathered; decision based on food services director's assumption",
    "threat_can_be_mitigated_by_accommodation": false,
    "assessment_relied_on_stereotypes": true
  }
}
```

**Expected Output (JSON):**
```json
{
  "direct_threat_analysis": {
    "direct_threat_exists": "no",
    "direct_threat_analysis": {
      "factors_for_threat": [],
      "factors_against_threat": [
        "assessment relied on stereotypes or generalizations about the disability rather than individualized evaluation — fatal procedural defect under 29 CFR § 1630.2(r); this defeater applies regardless of substantive factors"
      ],
      "mitigation_possible": false,
      "assessment_methodology_adequate": false,
      "key_uncertainties": []
    },
    "reasoning": "Under 29 CFR § 1630.2(r), a direct threat assessment must be based on an individualized evaluation using current medical knowledge and best available objective evidence — not stereotypes or generalizations. The food services director's decision was based on the generalized and medically unsupported assumption that HIV poses a food contamination risk. This is a textbook stereotype. Current CDC and public health guidance establishes that HIV is not transmitted through food handling. The reliance on stereotypes is a fatal procedural defect that negates the direct threat defense regardless of any substantive risk factors. No individualized assessment was performed; no objective evidence was gathered.",
    "sources_cited": ["29 CFR § 1630.2(r)", "EEOC Enforcement Guidance No. 915.002 §§ 36–41"]
  },
  "accommodation_determination": {
    "accommodation_required": "yes",
    "accommodation_type_approved": "policy_modification",
    "denial_basis": null,
    "factors_summary": {
      "factors_for_accommodation": [
        "covered employer and individual confirmed (state government employer — categorically covered)",
        "HIV is per se substantially limiting — qualifying disability established",
        "valid accommodation request — return to original duties",
        "no undue hardship (zero cost, no operational impact)",
        "direct threat defense fails: assessment relied on HIV stereotype without individualized evaluation"
      ],
      "factors_against_accommodation": []
    },
    "recommended_actions": [
      "Return Michael to his original food preparation duties immediately",
      "Document that the prior reassignment was based on a legally invalid assessment",
      "If the hospital genuinely believes a direct threat exists, conduct a proper individualized assessment using current CDC and public health guidance before taking any adverse action",
      "Train food services management on ADA direct threat requirements and the prohibition on stereotype-based assessments"
    ],
    "reasoning": "All threshold requirements are met. The direct threat defense is defeated by the procedural defect of stereotype-reliance. Under 42 U.S.C. § 12112(b)(5)(A) and 29 CFR § 1630.9(a), Memorial Hospital must return Michael to his food preparation role. The hospital's reassignment decision constitutes disability discrimination under 42 U.S.C. § 12112(a).",
    "sources_cited": ["42 U.S.C. § 12112(b)(5)(A)", "29 CFR § 1630.9(a)", "29 CFR § 1630.2(r)"]
  }
}
```

---

## AA-007 — Direct Threat Mitigable: Controlled Diabetes in Safety-Sensitive Role

**Scenario ID:** AA-007
**Scenario Name:** Direct Threat Mitigable — Diabetes in Safety-Sensitive Manufacturing Role, Blood Sugar Monitoring Accommodation

**Fact Pattern:** Angela Kim is a machine operator at PrecisionMfg Inc., a covered employer with 210 employees. Angela has Type 2 diabetes (qualifying disability — per se substantially limiting). Her employer asserts direct threat, citing incidents where low blood sugar caused brief disorientation near heavy machinery. The employer's occupational health physician conducted an individualized assessment and concluded that the risk can be reduced to an acceptable level if Angela monitors her blood sugar before each shift and during breaks, keeps fast-acting glucose tablets on her person, and is permitted to take a 5-minute break if she feels hypoglycemic symptoms. Angela has agreed to these protocols and has requested this monitoring and break accommodation. No stereotypes were relied upon.

**Legal Analysis:**
- **Rule (Threat):** Direct threat claimed. Procedural requirements met (individualized assessment, current medical knowledge, objective evidence, no stereotypes). Mitigation possible: yes (monitoring + glucose access + breaks). R035 applies — automatic no because threat can be mitigated.
- **Conclusion:** Direct threat does not exist once accommodation is provided. Accommodation required = yes (monitoring breaks and glucose access policy modification).

**Structured Input (JSON):**
```json
{
  "module_1_inputs": {
    "is_covered_employer": true,
    "is_covered_individual": true,
    "has_qualifying_disability": "yes",
    "accommodation_rights_attach": true,
    "is_qualified_individual": "yes"
  },
  "accommodation_request": {
    "accommodation_type_requested": "policy_modification",
    "accommodation_description": "Blood glucose monitoring before each shift and during breaks; permission to carry and consume fast-acting glucose tablets; 5-minute symptom-response break when needed",
    "accommodation_request_date": "2026-01-28",
    "request_made_by": "employee",
    "accommodation_is_for": "performing_job_functions",
    "functional_limitation_identified": true,
    "accommodation_request_in_writing": true
  },
  "undue_hardship_analysis": {
    "accommodation_gross_cost": 0,
    "accommodation_net_cost": 0,
    "accommodation_frequency": "ongoing",
    "facility_annual_revenue": 28000000,
    "facility_employee_count": 210,
    "entity_annual_revenue": 28000000,
    "entity_total_employees": 210,
    "impact_on_operations": "minor",
    "impact_on_other_employees": "none",
    "employer_asserts_hardship": false,
    "employer_documented_hardship_analysis": false
  },
  "direct_threat_analysis": {
    "direct_threat_claimed": true,
    "threat_to": "self",
    "risk_duration": "ongoing",
    "potential_harm_severity": "serious",
    "harm_likelihood": "possible",
    "harm_imminence": "somewhat_imminent",
    "individualized_assessment_performed": true,
    "assessment_based_on_current_medical_knowledge": true,
    "objective_evidence_exists": true,
    "evidence_description": "Occupational health physician assessment; 2 documented hypoglycemic incidents in 18 months; physician concludes risk is manageable with monitoring protocol",
    "threat_can_be_mitigated_by_accommodation": true,
    "mitigation_accommodation_description": "Pre-shift and break-time blood glucose monitoring, glucose tablets on person, 5-minute symptom-response break protocol",
    "assessment_relied_on_stereotypes": false
  }
}
```

**Expected Output (JSON):**
```json
{
  "direct_threat_analysis": {
    "direct_threat_exists": "no",
    "direct_threat_analysis": {
      "factors_for_threat": [],
      "factors_against_threat": [
        "threat can be eliminated or reduced to an acceptable level through reasonable accommodation — accommodation is required; exclusion is not permitted under 29 CFR § 1630.2(r)"
      ],
      "mitigation_possible": true,
      "assessment_methodology_adequate": true,
      "key_uncertainties": []
    },
    "reasoning": "The employer's individualized assessment using current medical knowledge satisfies the procedural requirements of 29 CFR § 1630.2(r). However, the occupational health physician has concluded that the risk can be reduced to an acceptable level through a blood glucose monitoring and response protocol. Under 29 CFR § 1630.2(r), direct threat requires that the risk 'cannot be eliminated or reduced to an acceptable level through reasonable accommodation.' Because the threat is mitigable, the direct threat defense fails. The employer must provide the monitoring accommodation rather than exclude Angela.",
    "sources_cited": ["29 CFR § 1630.2(r)", "42 U.S.C. § 12113(b)"]
  },
  "accommodation_determination": {
    "accommodation_required": "yes",
    "accommodation_type_approved": "policy_modification",
    "denial_basis": null,
    "factors_summary": {
      "factors_for_accommodation": [
        "all coverage and eligibility thresholds met",
        "valid accommodation request",
        "no undue hardship (zero cost to employer)",
        "direct threat mitigable — occupational health physician confirms monitoring protocol reduces risk to acceptable level"
      ],
      "factors_against_accommodation": []
    },
    "recommended_actions": [
      "Implement blood glucose monitoring protocol as described",
      "Amend workplace policy to permit glucose tablets and monitoring equipment",
      "Establish documented protocol for 5-minute symptom-response breaks",
      "Revisit assessment after 90 days to confirm protocol effectiveness"
    ],
    "reasoning": "Direct threat is mitigable by accommodation. Under 42 U.S.C. § 12112(b)(5)(A) and 29 CFR § 1630.9(a), PrecisionMfg must provide the monitoring accommodation. Excluding Angela would constitute disability discrimination when an effective accommodation exists.",
    "sources_cited": ["42 U.S.C. § 12112(b)(5)(A)", "29 CFR § 1630.9(a)", "29 CFR § 1630.2(r)"]
  }
}
```

---

## AA-008 — Reassignment as Accommodation

**Scenario ID:** AA-008
**Scenario Name:** Reassignment as Last-Resort Accommodation — Employee Cannot Perform Current Role, Vacant Position Available

**Fact Pattern:** Sandra Lee is a floor nurse at HealthSystem Corp, a covered employer with 3,200 employees. Sandra has a documented progressive back condition (qualifying disability) that now prevents her from performing the essential function of lifting patients — a core function confirmed by written job description, incumbent history, and severe operational consequence. No accommodation will enable her to perform patient lifting. However, a vacant Medical Records Coordinator position exists at an equivalent pay grade; Sandra is qualified for this position based on her education and clinical documentation experience. Sandra requests reassignment.

**Legal Analysis:**
- **Rule (Request):** Valid — employee, limitation identified (cannot lift), for performing_job_functions → reassignment. R026.
- **Rule (Hardship):** $0 net cost (existing position). No hardship asserted. R029.
- **Rule (Threat):** No threat claimed. R032.
- **Rule (Determination):** All thresholds met. R045 — accommodation required (reassignment).
- **Legal Note:** Reassignment is the accommodation of last resort under EEOC guidance — provided after other options are exhausted, not in lieu of other exploration. Here, no other accommodation can address the lifting limitation, so reassignment is appropriate.

**Structured Input (JSON):**
```json
{
  "module_1_inputs": {
    "is_covered_employer": true,
    "is_covered_individual": true,
    "has_qualifying_disability": "yes",
    "accommodation_rights_attach": true,
    "is_qualified_individual": "yes"
  },
  "accommodation_request": {
    "accommodation_type_requested": "reassignment",
    "accommodation_description": "Reassignment to vacant Medical Records Coordinator position at equivalent pay grade",
    "accommodation_request_date": "2026-02-15",
    "request_made_by": "employee",
    "accommodation_is_for": "performing_job_functions",
    "functional_limitation_identified": true,
    "accommodation_request_in_writing": true
  },
  "undue_hardship_analysis": {
    "accommodation_gross_cost": 0,
    "accommodation_net_cost": 0,
    "accommodation_frequency": "one_time",
    "facility_annual_revenue": 320000000,
    "facility_employee_count": 3200,
    "entity_annual_revenue": 320000000,
    "entity_total_employees": 3200,
    "impact_on_operations": "minor",
    "impact_on_other_employees": "none",
    "employer_asserts_hardship": false,
    "employer_documented_hardship_analysis": false
  },
  "direct_threat_analysis": {
    "direct_threat_claimed": false
  }
}
```

**Expected Output (JSON):**
```json
{
  "accommodation_request": {
    "accommodation_request_valid": true,
    "accommodation_category": "reassignment",
    "request_validity_basis": "employee_request_with_limitation",
    "reasoning": "Valid request. Employee identified inability to perform patient lifting (functional limitation) and requests reassignment to a vacant position for which she is qualified. Reassignment is a recognized form of reasonable accommodation under 29 CFR § 1630.2(o)(2)(ii) and EEOC Enforcement Guidance No. 915.002 § Reassignment.",
    "sources_cited": ["29 CFR § 1630.2(o)(2)(ii)", "EEOC Enforcement Guidance No. 915.002 § Reassignment"]
  },
  "accommodation_determination": {
    "accommodation_required": "yes",
    "accommodation_type_approved": "reassignment",
    "denial_basis": null,
    "factors_summary": {
      "factors_for_accommodation": [
        "all coverage and eligibility thresholds met",
        "valid reassignment request — no other accommodation can address patient lifting limitation",
        "vacant equivalent-grade position exists for which employee is qualified",
        "no undue hardship (reassignment costs zero additional expense)",
        "no direct threat"
      ],
      "factors_against_accommodation": []
    },
    "recommended_actions": [
      "Reassign Sandra to the Medical Records Coordinator position",
      "Do not displace another employee to create the vacancy — reassignment applies only to existing vacancies per ADA National Network guidance",
      "Confirm Sandra meets all qualification requirements for the Coordinator role before formalizing the transfer",
      "Document the reassignment as an ADA accommodation in the interactive process file (not the personnel file)"
    ],
    "reasoning": "Reassignment is a required reasonable accommodation when no accommodation enables performance of essential functions in the current role and a suitable vacant position exists. Under EEOC Enforcement Guidance No. 915.002 § Reassignment and ADA National Network guidance, the employer must place a qualified individual in a vacant position — no competition required, no new position creation required, no other employee displacement required. HealthSystem Corp must reassign Sandra to the Medical Records Coordinator position.",
    "sources_cited": ["42 U.S.C. § 12112(b)(5)(A)", "29 CFR § 1630.9(a)", "EEOC Enforcement Guidance No. 915.002 § Reassignment", "ADA National Network Fact Sheet § Examples"]
  }
}
```

---

## AA-009 — Leave as Accommodation: 4-Week Treatment Leave, 30-Employee Company

**Scenario ID:** AA-009
**Scenario Name:** Leave as Accommodation — 4-Week Treatment Leave, Small-to-Mid Employer, No Hardship Established

**Fact Pattern:** Thomas Reed is a marketing coordinator at SmallBiz Media, a private employer with 30 employees and $3.5 million annual revenue. Thomas has a qualifying anxiety disorder and requests 4 weeks of unpaid leave to attend an intensive outpatient treatment program. SmallBiz has no FMLA obligation (fewer than 50 employees). The employer asserts undue hardship based on operational disruption, has documented the analysis, but has not explored coverage alternatives (co-worker cross-training, temporary staffing). The position can be temporarily covered by a junior employee during Thomas's absence.

**Legal Analysis:**
- **Rule (Hardship):** $0 direct cost. Impact on operations: moderate (need for temporary coverage). Impact on other employees: moderate (junior employee takes on additional duties). Factor analysis: UH-F01 does not fire (ratio = 0%). UH-F04 does not fire (no gross cost). UH-F02 does not fire (moderate, not significant/severe). UH-A06 fires (no alternatives explored). factors_for = 0, factors_against = 1. Threshold: factors_for (0) ≤ 1 but factors_against (1) < 2. Indeterminate — neither threshold met. However: EEOC guidance treats leave as a required accommodation absent true hardship, and the employer has not demonstrated that coverage is truly unavailable.
- **Conclusion:** Indeterminate — employer should document impact more fully and confirm whether coverage alternatives exist.

**Structured Input (JSON):**
```json
{
  "module_1_inputs": {
    "is_covered_employer": true,
    "is_covered_individual": true,
    "has_qualifying_disability": "yes",
    "accommodation_rights_attach": true,
    "is_qualified_individual": "yes"
  },
  "accommodation_request": {
    "accommodation_type_requested": "leave_as_accommodation",
    "accommodation_description": "4 weeks unpaid leave for intensive outpatient anxiety treatment program",
    "accommodation_request_date": "2026-04-01",
    "request_made_by": "employee",
    "accommodation_is_for": "performing_job_functions",
    "functional_limitation_identified": true,
    "accommodation_request_in_writing": true
  },
  "undue_hardship_analysis": {
    "accommodation_gross_cost": 0,
    "tax_credits_available": 0,
    "outside_funding_available": 0,
    "accommodation_net_cost": 0,
    "accommodation_frequency": "one_time",
    "facility_annual_revenue": 3500000,
    "facility_employee_count": 30,
    "entity_annual_revenue": 3500000,
    "entity_total_employees": 30,
    "entity_type": "single_facility",
    "impact_on_operations": "moderate",
    "impact_on_other_employees": "moderate",
    "impact_description": "Junior employee would cover duties; some client deadlines may be affected during 4-week absence",
    "employer_asserts_hardship": true,
    "employer_documented_hardship_analysis": true,
    "alternative_accommodation_considered": false
  },
  "direct_threat_analysis": {
    "direct_threat_claimed": false
  }
}
```

**Expected Output (JSON):**
```json
{
  "undue_hardship_analysis": {
    "undue_hardship_applies": "indeterminate",
    "undue_hardship_analysis": {
      "cost_burden_ratio": 0.0,
      "cost_burden_denominator_used": "facility_annual_revenue",
      "factors_for_hardship": [],
      "factors_against_hardship": [
        "employer has not considered alternative lower-cost accommodations before asserting hardship — failure to explore alternatives weighs against hardship defense per EEOC Enforcement Guidance No. 915.002 § Undue Hardship"
      ],
      "key_uncertainties": [
        "zero direct monetary cost but employer asserts operational hardship — operational impact analysis requires more specificity: which client deliverables, what deadlines, what actual consequences of delay",
        "impact rated moderate for both operations and employees — falls between clear minor (factor against) and significant/severe (factor for); insufficient to resolve without more detail",
        "employer has not documented whether temporary staffing, cross-training, or other coverage alternatives are feasible or were considered"
      ]
    },
    "alternative_accommodations_available": true,
    "alternative_accommodations_suggested": [
      "Temporary contractor or staffing agency placement for 4-week period",
      "Co-worker cross-training for critical tasks prior to leave start",
      "Phased or reduced-hour intensive outpatient program that allows partial work hours"
    ],
    "reasoning": "Net cost: $0. Cost burden ratio: 0.00% — no direct financial hardship from cost alone. However, employer asserts operational disruption (moderate) for a 30-employee firm. The moderate rating falls in the indeterminate zone. EEOC Enforcement Guidance No. 915.002 § Leave establishes that leave can be a required accommodation when it does not impose true hardship. The employer has not explored coverage alternatives. Under 29 CFR § 1630.15(d), the burden of proof rests with the employer, and the current documentation does not fully meet that burden. Additional specificity on operational impact and coverage options is needed.",
    "sources_cited": ["42 U.S.C. § 12111(10)", "29 CFR § 1630.2(p)(2)(i)-(iii)", "29 CFR § 1630.15(d)", "EEOC Enforcement Guidance No. 915.002 § Leave"]
  },
  "accommodation_determination": {
    "accommodation_required": "indeterminate",
    "accommodation_type_approved": null,
    "denial_basis": null,
    "factors_summary": {
      "factors_for_accommodation": [
        "all coverage thresholds met",
        "zero direct monetary cost to employer",
        "EEOC guidance treats leave as required accommodation absent true hardship"
      ],
      "factors_against_accommodation": [
        "employer asserts moderate operational disruption for 30-employee business during 4-week absence",
        "hardship analysis requires more specificity to resolve"
      ]
    },
    "recommended_actions": [
      "Document specific client deliverables and deadlines at risk during a 4-week absence",
      "Explore and document temporary staffing, contractor, or cross-training coverage options",
      "Complete a full 29 CFR § 1630.2(p) factor analysis before issuing a determination",
      "If coverage is feasible, approve the leave as a required ADA accommodation",
      "If coverage is genuinely impossible and hardship is documented, explore alternative: phased intensive outpatient program"
    ],
    "reasoning": "Leave accommodation determination is indeterminate pending more complete hardship documentation and exploration of coverage alternatives. No other defenses apply. Determination cannot be finalized until the undue hardship analysis is resolved.",
    "sources_cited": ["42 U.S.C. § 12112(b)(5)(A)", "29 CFR § 1630.9(a)", "29 CFR § 1630.15(d)"]
  }
}
```

---

## AA-010 — Telework Request: Employer Denies Despite Same-Role Telework by Others

**Scenario ID:** AA-010
**Scenario Name:** Telework Accommodation Required — Employer Denies Based on Policy But Other Employees in Same Role Telework

**Fact Pattern:** Lisa Chen is a software developer at DevCorp Inc., a covered employer with 650 employees and $95 million in annual revenue. Lisa has a qualifying autoimmune condition (rheumatoid arthritis — per se substantially limiting musculoskeletal function) that causes severe flare-ups. During flares, commuting and sitting in the office for extended periods is substantially limiting. She requests the ability to work from home during flare periods (estimated 3–5 days per month on an as-needed basis). DevCorp has a general policy against remote work for "all positions" but 8 of 12 developers in Lisa's team already work from home full-time. DevCorp asserts undue hardship but has not documented any individualized analysis and has not explored any alternatives.

**Legal Analysis:**
- **Rule (Hardship):** Employer asserts hardship. R030 applies — employer asserts hardship but has NOT documented analysis → indeterminate from R030. But combined with the factual pattern (8 of 12 peers telework, zero additional cost), indeterminate tilts strongly against hardship.
- **Additional Note:** The employer's blanket "no remote work" policy applied inconsistently (8 of 12 developers already telework) undermines the hardship assertion. EEOC guidance treats blanket policy denials of telework as requiring individualized assessment, not categorical denial.
- **Conclusion:** Undue hardship indeterminate per R030 (no documentation). Accommodation determination: indeterminate pending proper hardship analysis. Strong indicators point toward required accommodation.

**Structured Input (JSON):**
```json
{
  "module_1_inputs": {
    "is_covered_employer": true,
    "is_covered_individual": true,
    "has_qualifying_disability": "yes",
    "accommodation_rights_attach": true,
    "is_qualified_individual": "yes"
  },
  "accommodation_request": {
    "accommodation_type_requested": "telework",
    "accommodation_description": "Work from home on an as-needed basis during rheumatoid arthritis flare-ups, estimated 3-5 days per month",
    "accommodation_request_date": "2026-03-05",
    "request_made_by": "employee",
    "accommodation_is_for": "performing_job_functions",
    "functional_limitation_identified": true,
    "accommodation_request_in_writing": true
  },
  "undue_hardship_analysis": {
    "accommodation_gross_cost": 0,
    "tax_credits_available": 0,
    "outside_funding_available": 0,
    "accommodation_net_cost": 0,
    "accommodation_frequency": "occasional",
    "facility_annual_revenue": 95000000,
    "facility_employee_count": 650,
    "entity_annual_revenue": 95000000,
    "entity_total_employees": 650,
    "entity_type": "single_facility",
    "impact_on_operations": "none",
    "impact_on_other_employees": "none",
    "impact_description": "8 of 12 developers in the same team already work full-time remotely; Lisa's role is software development performed on a laptop with no in-person collaboration requirement",
    "employer_asserts_hardship": true,
    "employer_documented_hardship_analysis": false,
    "alternative_accommodation_considered": false
  },
  "direct_threat_analysis": {
    "direct_threat_claimed": false
  }
}
```

**Expected Output (JSON):**
```json
{
  "undue_hardship_analysis": {
    "undue_hardship_applies": "indeterminate",
    "undue_hardship_analysis": {
      "cost_burden_ratio": 0.0,
      "cost_burden_denominator_used": "facility_annual_revenue",
      "factors_for_hardship": [],
      "factors_against_hardship": [
        "employer asserts hardship but has not produced documented, individualized analysis — burden of proof not met under 29 CFR § 1630.15(d)"
      ],
      "key_uncertainties": [
        "employer has asserted undue hardship but has not documented the factor-by-factor analysis required to meet the burden of proof under 29 CFR § 1630.15(d) — determination is indeterminate until documentation is produced",
        "employer's blanket policy against remote work appears inconsistently applied — 8 of 12 developers in the same role already telework full-time, which strongly undermines any operational impact claim"
      ]
    },
    "alternative_accommodations_available": false,
    "alternative_accommodations_suggested": [],
    "reasoning": "Net cost: $0. Cost burden ratio: 0.00%. 8 of 12 developers in Lisa's peer group already telework full-time. The employer asserts hardship based on a blanket no-remote-work policy but has produced no individualized analysis. Under 29 CFR § 1630.15(d), the employer bears the burden of proof and must document an individualized hardship analysis — a generalized policy citation is insufficient. The existing practice of peer telework makes any operational-impact claim facially implausible and requires specific documentation to overcome. Determination is indeterminate pending required documentation.",
    "sources_cited": ["42 U.S.C. § 12111(10)", "29 CFR § 1630.2(p)(2)(i)-(iii)", "29 CFR § 1630.15(d)", "EEOC Enforcement Guidance No. 915.002 § Modified Workplace Policies"]
  },
  "accommodation_determination": {
    "accommodation_required": "indeterminate",
    "accommodation_type_approved": null,
    "denial_basis": null,
    "factors_summary": {
      "factors_for_accommodation": [
        "all coverage and eligibility thresholds met",
        "zero direct cost to employer",
        "same-role peers already telework full-time — blanket policy appears inapplicable",
        "no operational or employee impact identified",
        "no direct threat"
      ],
      "factors_against_accommodation": [
        "employer asserts hardship — defense must be resolved",
        "hardship analysis not yet documented — determination pending"
      ]
    },
    "recommended_actions": [
      "Produce a documented, individualized undue hardship analysis under all 29 CFR § 1630.2(p) factors — blanket policy citation is legally insufficient",
      "Address specifically why the accommodation cannot be granted given that 8 of 12 peers already telework in the same role",
      "If no documented hardship can be demonstrated, approve the as-needed telework accommodation",
      "Do not deny based on blanket policy alone — EEOC guidance requires individualized assessment of each accommodation request"
    ],
    "reasoning": "Accommodation determination is indeterminate because the undue hardship analysis is unresolved. However, the factual record — zero cost, zero impact, peer telework practice — creates a strong baseline against hardship. DevCorp must produce an individualized analysis or approve the accommodation. A blanket policy denial without individualized analysis likely constitutes disability discrimination under 42 U.S.C. § 12112(a).",
    "sources_cited": ["42 U.S.C. § 12112(b)(5)(A)", "29 CFR § 1630.9(a)", "29 CFR § 1630.15(d)", "EEOC Enforcement Guidance No. 915.002 § Modified Workplace Policies"]
  }
}
```
