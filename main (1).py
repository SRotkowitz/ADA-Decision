"""
ADA Decision Engine — FastAPI Server
Version: 0.1
Repository: SRotkowitz/ADA-Decision-Engine

Exposes the ADA Reasonable Accommodation Decision Engine via HTTP API.
Executes the four modules in order with the qualified-individual wrapper composite,
and returns structured JSON responses with legal reasoning and source citations.

Endpoints:
  GET  /health
  GET  /version
  GET  /schema/{module}
  POST /assess/coverage_eligibility
  POST /assess/accommodation_analysis
  POST /assess/employer_obligations
  POST /assess/violation_risk
  POST /assess/full
"""

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from schemas.input_models import (
    Module1Input,
    Module2Input,
    Module3Input,
    Module4Input,
    UnifiedInput,
)
from schemas.output_models import (
    Module1Output,
    Module2Output,
    Module3Output,
    Module4Output,
    WrapperOutput,
    UnifiedOutput,
)
from engine.module1_coverage_eligibility import run_module1
from engine.module2_accommodation_analysis import run_module2
from engine.module3_employer_obligations import run_module3
from engine.module4_violation_risk import run_module4
from engine.wrapper import apply_wrapper, run_full_assessment

app = FastAPI(
    title="ADA Decision Engine",
    version="0.1",
    description=(
        "Deterministic decision engine for ADA Title I reasonable accommodation analysis. "
        "Legal domain: Americans with Disabilities Act — Title I (Employment). "
        "Governing law: 42 U.S.C. §§ 12111–12117; 29 CFR Part 1630."
    ),
)

# ---------------------------------------------------------------------------
# Schema store — populated at module import time for /schema/{module}
# ---------------------------------------------------------------------------

_MODULE_SCHEMAS: dict = {
    "coverage_eligibility": {
        "module_id": "ada_coverage_eligibility",
        "version": "0.2",
        "components": ["employer_coverage (1.1)", "individual_status (1.2)", "disability_determination (1.3)", "qualified_individual (1.4)"],
        "rule_range": "R001–R025",
        "governing_law": ["42 U.S.C. §§ 12111–12112", "29 CFR § 1630.2"],
    },
    "accommodation_analysis": {
        "module_id": "ada_accommodation_analysis",
        "version": "0.2",
        "components": ["accommodation_request (2.1)", "undue_hardship_analysis (2.2)", "direct_threat_analysis (2.3)", "accommodation_determination (2.4)"],
        "rule_range": "R026–R046",
        "governing_law": ["42 U.S.C. §§ 12111(10)", "42 U.S.C. § 12112(b)(5)(A)", "42 U.S.C. § 12113(b)", "29 CFR § 1630.2(p),(r)", "29 CFR § 1630.9"],
    },
    "employer_obligations": {
        "module_id": "ada_employer_obligations",
        "version": "0.1",
        "components": ["interactive_process (3.1)", "medical_inquiry_limitations (3.2)", "confidentiality (3.3)"],
        "rule_range": "R047–R067",
        "governing_law": ["42 U.S.C. § 12112(d)", "29 CFR § 1630.13", "29 CFR § 1630.14"],
    },
    "violation_risk": {
        "module_id": "ada_violation_risk",
        "version": "0.1",
        "components": ["failure_to_accommodate (4.1)", "disability_discrimination (4.2)", "harassment (4.3)", "retaliation (4.4)", "overall_violation_risk (4.5)"],
        "rule_range": "R068–R110",
        "governing_law": ["42 U.S.C. §§ 12112", "42 U.S.C. § 12113", "42 U.S.C. § 12203"],
    },
    "unified": {
        "module_id": "ada_unified",
        "version": "0.1",
        "description": "Unified assessment schema covering all four modules plus wrapper composite. See unified_input_schema.json and unified_output_schema.json.",
        "execution_order": [
            "ada_coverage_eligibility",
            "ada_accommodation_analysis",
            "is_qualified_individual_composite (WR-1 through WR-5)",
            "ada_employer_obligations",
            "ada_violation_risk",
        ],
        "governing_law": ["42 U.S.C. §§ 12111–12117", "29 CFR Part 1630"],
    },
}

_VALID_MODULES = sorted(_MODULE_SCHEMAS.keys())


# ---------------------------------------------------------------------------
# GET /health
# ---------------------------------------------------------------------------

@app.get("/health")
def health():
    """Server health check. Returns engine name and status."""
    return {"status": "ok", "engine": "ADA Decision Engine", "version": "0.1"}


# ---------------------------------------------------------------------------
# GET /version
# ---------------------------------------------------------------------------

@app.get("/version")
def version():
    """Returns version metadata for the engine and all modules."""
    return {
        "engine": "ADA Decision Engine",
        "version": "0.1",
        "modules": {
            "ada_coverage_eligibility": "0.2",
            "ada_accommodation_analysis": "0.2",
            "ada_employer_obligations": "0.1",
            "ada_violation_risk": "0.1",
        },
        "legal_domain": "Americans with Disabilities Act — Title I",
        "governing_law": ["42 U.S.C. §§ 12111-12117", "29 CFR Part 1630"],
    }


# ---------------------------------------------------------------------------
# GET /schema/{module}
# ---------------------------------------------------------------------------

@app.get("/schema/{module}")
def get_schema(module: str):
    """Returns the JSON schema reference for the specified module.

    Valid module values: coverage_eligibility, accommodation_analysis,
    employer_obligations, violation_risk, unified.
    Returns 404 for unrecognized module names.
    """
    if module not in _MODULE_SCHEMAS:
        raise HTTPException(
            status_code=404,
            detail={"error": "Module not found", "valid_modules": _VALID_MODULES},
        )
    return _MODULE_SCHEMAS[module]


# ---------------------------------------------------------------------------
# POST /assess/coverage_eligibility
# ---------------------------------------------------------------------------

@app.post("/assess/coverage_eligibility", response_model=Module1Output)
def assess_coverage_eligibility(inp: Module1Input):
    """Execute Module 1: Coverage and Eligibility.

    Returns employer coverage, individual status, disability determination,
    and preliminary qualified individual assessment.
    Citation: 42 U.S.C. §§ 12111–12112; 29 CFR § 1630.2.
    """
    try:
        return run_module1(inp)
    except Exception as exc:
        raise HTTPException(status_code=500, detail={"error": "Engine error", "detail": str(exc)})


# ---------------------------------------------------------------------------
# POST /assess/accommodation_analysis
# ---------------------------------------------------------------------------

@app.post("/assess/accommodation_analysis", response_model=Module2Output)
def assess_accommodation_analysis(inp: Module2Input):
    """Execute Module 2: Accommodation Analysis.

    Requires Module 1 dependency fields in the request body. Runs Module 1 internally
    to produce dependency outputs, then runs Module 2.
    Citation: 42 U.S.C. §§ 12111(10), 12112(b)(5)(A), 12113(b); 29 CFR § 1630.2(p),(r); 29 CFR § 1630.9.
    """
    try:
        m1_out = run_module1(inp)
        return run_module2(inp, m1_out)
    except Exception as exc:
        raise HTTPException(status_code=500, detail={"error": "Engine error", "detail": str(exc)})


# ---------------------------------------------------------------------------
# POST /assess/employer_obligations
# ---------------------------------------------------------------------------

@app.post("/assess/employer_obligations", response_model=Module3Output)
def assess_employer_obligations(inp: Module3Input):
    """Execute Module 3: Employer Obligations.

    Requires Module 1 and Module 2 dependency fields. Runs Modules 1–2 and the
    wrapper composite internally before executing Module 3.
    Citation: 42 U.S.C. § 12112(d); 29 CFR § 1630.13, § 1630.14; EEOC Guidance 915.002.
    """
    try:
        m1_out = run_module1(inp)
        m2_out = run_module2(inp, m1_out)
        # Wrapper requires accommodation_theoretically_effective; default to indeterminate for module-only endpoints
        acc_effective = getattr(inp, "accommodation_theoretically_effective", "indeterminate")
        wrapper_out = apply_wrapper(m1_out, m2_out, acc_effective)
        return run_module3(inp, m1_out, m2_out, wrapper_out)
    except Exception as exc:
        raise HTTPException(status_code=500, detail={"error": "Engine error", "detail": str(exc)})


# ---------------------------------------------------------------------------
# POST /assess/violation_risk
# ---------------------------------------------------------------------------

class ViolationRiskInput(Module4Input):
    """Input for /assess/violation_risk. Extends Module4Input with wrapper-level field."""
    accommodation_theoretically_effective: str = "indeterminate"


class ViolationRiskOutput(Module4Output):
    """Output for /assess/violation_risk. Includes wrapper composite."""
    is_qualified_individual_composite: WrapperOutput


@app.post("/assess/violation_risk")
def assess_violation_risk(inp: ViolationRiskInput):
    """Execute Module 4: Violation Risk.

    Requires all upstream dependency fields. Runs Modules 1–3 and the wrapper
    composite internally before executing Module 4.
    Returns Module 4 output plus the wrapper is_qualified_individual composite.
    Citation: 42 U.S.C. §§ 12112, 12113, 12203.
    """
    try:
        m1_out = run_module1(inp)
        m2_out = run_module2(inp, m1_out)
        wrapper_out = apply_wrapper(m1_out, m2_out, inp.accommodation_theoretically_effective)
        m3_out = run_module3(inp, m1_out, m2_out, wrapper_out)
        m4_out = run_module4(inp, m1_out, m2_out, m3_out, wrapper_out)
        result = m4_out.model_dump()
        result["is_qualified_individual_composite"] = wrapper_out.model_dump()
        return result
    except Exception as exc:
        raise HTTPException(status_code=500, detail={"error": "Engine error", "detail": str(exc)})


# ---------------------------------------------------------------------------
# POST /assess/full
# ---------------------------------------------------------------------------

@app.post("/assess/full", response_model=UnifiedOutput)
def assess_full(inp: UnifiedInput):
    """Execute the complete ADA Decision Engine unified assessment.

    Runs all four modules plus the wrapper composite in the required order:
    M1 → M2 → WR → M3 → M4. Returns unified summary output plus full module_outputs.
    Citation: unified_output_schema.json v0.1; 42 U.S.C. §§ 12111–12117; 29 CFR Part 1630.
    """
    try:
        return run_full_assessment(inp)
    except Exception as exc:
        raise HTTPException(status_code=500, detail={"error": "Engine error", "detail": str(exc)})
