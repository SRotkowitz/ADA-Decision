# ADA-Decision
ADA-Decision Engine is a repository of database and schema logic for API 

# ADA Decision Engine

A commercial, deterministic decision engine that evaluates whether an employer must provide a reasonable accommodation under the Americans with Disabilities Act, Title I. The engine accepts structured JSON input and returns structured JSON output with legal reasoning and source citations. Designed for consumption by developers and HR software vendors via API.

**This is not legal advice.** Outputs are structured legal analysis for informational purposes and should be reviewed by qualified employment counsel before use in personnel decisions.

---

## What it does

Given facts about an employer, an individual, a disability, and an accommodation request, the engine evaluates:

- Whether the employer and individual are covered under ADA Title I
- Whether the individual has a qualifying disability under the ADAAA broad construction standard
- Whether the individual is a qualified individual with or without accommodation
- Whether a reasonable accommodation is required
- Whether the employer met its procedural obligations (interactive process, medical inquiry limits, confidentiality)
- The employer's violation risk across four claim types: failure to accommodate, disability discrimination, harassment, and retaliation

Outputs are deterministic — same input always produces same output. Standards-based determinations (substantial limitation, essential functions, undue hardship, direct threat) return `yes` / `no` / `indeterminate` with documented factors, never fabricated certainty.

---

## Legal domain

| | |
|---|---|
| **Statute** | Americans with Disabilities Act, Title I — 42 U.S.C. §§ 12111–12117 |
| **Regulations** | 29 CFR Part 1630 |
| **Amendments** | ADA Amendments Act of 2008 (ADAAA) |
| **Enforcing agency** | Equal Employment Opportunity Commission (EEOC) |

---

## Architecture

The engine is organized into four modules executed in sequence by a unified wrapper:

| Module | ID | Rule range | Purpose |
|---|---|---|---|
| 1 | `ada_coverage_eligibility` | R001–R025 | Employer coverage, individual status, disability determination, qualified individual |
| 2 | `ada_accommodation_analysis` | R026–R046 | Accommodation request validity, undue hardship, direct threat, accommodation determination |
| 3 | `ada_employer_obligations` | R047–R067 | Interactive process, medical inquiry limits, confidentiality |
| 4 | `ada_violation_risk` | R068–R110 | Failure to accommodate, disability discrimination, harassment, retaliation, overall risk |

The unified wrapper executes modules in order, resolves the `is_qualified_individual` composite determination (WR-1 through WR-3b), aggregates indeterminate factors, and produces top-level summary outputs.

**Determination types:**
- **Rule-based:** Binary yes/no. Same input always produces same output.
- **Standards-based:** `yes` / `no` / `indeterminate` with `factors_for`, `factors_against`, `key_uncertainties` arrays.
- **Composite:** Aggregates upstream outputs per documented short-circuit or aggregation logic.

**Risk levels:** `minimal` / `low` / `moderate` / `high` / `critical` — categorical only, no numeric scores.

---

## API endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Server status |
| GET | `/version` | Engine version and module versions |
| GET | `/schema/{module}` | JSON schema for a specific module |
| POST | `/assess/coverage_eligibility` | Module 1 only |
| POST | `/assess/accommodation_analysis` | Module 2 only |
| POST | `/assess/employer_obligations` | Module 3 only |
| POST | `/assess/violation_risk` | Module 4 + wrapper composite |
| POST | `/assess/full` | Full unified assessment |

### Example: POST /assess/full

**Request:**
```json
{
  "accommodation_theoretically_effective": "yes",
  "employer_coverage": {
    "employer_type": "private_employer",
    "employer_employee_count": 28,
    "workweeks_with_fifteen_plus": 52
  },
  "individual_status": {
    "individual_status": "current_employee",
    "is_independent_contractor": false
  },
  "disability_determination": {
    "disability_basis": "actual_disability",
    "impairment_type": "neurological",
    "limitation_severity": "substantial",
    "limitation_duration": "long_term",
    "is_per_se_substantially_limiting": true
  },
  "qualified_individual": {
    "can_perform_essential_functions_without_accommodation": false,
    "can_perform_essential_functions_with_accommodation": true
  },
  "accommodation_request": {
    "functional_limitation_identified": true,
    "request_made_by_authorized_party": true,
    "qualifying_purpose": true
  }
}
```

**Response:**
```json
{
  "ada_covered": true,
  "has_qualifying_disability": "yes",
  "is_qualified_individual": "yes",
  "accommodation_required": "yes",
  "employer_compliance_status": "indeterminate",
  "violation_risk_level": "high",
  "recommended_actions": [
    "Engage in good-faith interactive process to identify effective accommodation",
    "Document all accommodation options considered",
    "Consult Job Accommodation Network (JAN) for accommodation ideas"
  ],
  "indeterminate_factors": {},
  "module_outputs": { "..." : "..." }
}
```

---

## Running locally

**Requirements:** Python 3.11+

```bash
# Clone the repo
git clone https://github.com/SRotkowitz/ADA-Decision-Engine.git
cd ADA-Decision-Engine

# Install dependencies
pip install -r requirements.txt

# Start the server
python run.py

# Server runs at http://localhost:8000
# API docs at http://localhost:8000/docs
```

---

## Repository structure

```
/
├── main.py                              # FastAPI app and route definitions
├── run.py                               # Uvicorn entry point
├── requirements.txt
├── engine/
│   ├── module1_coverage_eligibility.py
│   ├── module2_accommodation_analysis.py
│   ├── module3_employer_obligations.py
│   ├── module4_violation_risk.py
│   └── wrapper.py                       # WR composite + unified orchestration
├── schemas/
│   ├── input_models.py                  # Pydantic input models
│   └── output_models.py                 # Pydantic output models
├── logic/                               # JSON rule logic files (one per module)
├── docs/
│   ├── module_interface_spec.json       # Authoritative cross-module reference
│   └── attorney_spot_check_memo.md      # Legal grounding verification [PENDING]
├── tests/
│   ├── unified_test_fixtures.json       # End-to-end test fixtures
│   └── ...                              # Per-module test fixtures and scenarios
└── vocabulary/
    └── ada_vocabulary.json              # Controlled vocabulary for all modules
```

---

## Validation status

| Check | Status |
|---|---|
| Deterministic replay (10 fixtures, 2 runs each) | PENDING |
| Correctness check against expected outputs | PENDING |
| WR-2 reachability (SC5 patch confirmed) | PENDING |
| Attorney spot-check memo | PENDING |

*Validation is in progress. This section will be updated upon completion of Phase 8.*

---

## Design decisions

Key architectural choices are documented in `docs/module_interface_spec.json`. Highlights:

- **`is_qualified_individual` is a wrapper-level composite**, not a Module 1 output, to avoid a circular dependency between qualification and accommodation analysis.
- **Standards-based determinations never fake certainty.** When facts are genuinely ambiguous, the engine returns `indeterminate` with documented uncertainties rather than forcing a yes/no.
- **Risk levels are categorical only.** No numeric scores. Every risk level derives from an explicit documented rule — same input always produces same output.
- **Employee non-participation is a weighting factor, not a defeater.** Documented employee refusal of the interactive process shifts FTA risk one tier downward but does not eliminate employer liability.

---

## Open items for attorney review

The following engine design choices are flagged for attorney calibration before production use:

- Interactive process good-faith threshold (≥3 factors for `process_quality = yes`) — engine heuristic, not stated in statute or EEOC guidance
- 10-business-day timeliness heuristic for interactive process acknowledgment — not a statutory deadline
- Undue hardship cost-burden ratio tiers (3% / 7% / 15% by employer size) — engine heuristic
- Temporal proximity tiers for retaliation risk (≤30 / 31–90 / 91–180 / >180 days) — engine heuristic
- FTA risk residual of `low` (not `minimal`) when legitimate denial is documented
- Employee non-participation one-tier shift calibration

---

## License

*To be determined.*

---

## Disclaimer

This engine produces structured legal analysis for informational purposes only. Outputs do not constitute legal advice. Results should be reviewed by qualified employment counsel before use in any personnel decision.
