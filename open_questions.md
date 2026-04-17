# Open Questions — ADA Decision Engine Phase 1

Generated: 2026-04-17  
Status: All items open — resolution deferred to module build phases per Phase 1 protocol.

---

## OQ-001 — Federal Law Conflict Defense (§ 1630.15(e)) vs. EEOC Guidance

**Source:** 29 CFR § 1630.15(e) (Source 05)  
**Issue:** § 1630.15(e) allows "conflict with other Federal laws" as a defense to any discrimination charge, including RA failure. EEOC guidance (Source 06) treats this defense very narrowly — it applies mainly where another statute *affirmatively requires* an exclusion (e.g., certain DOT physical standards, NRC radiation standards). The regulation on its face appears broader than EEOC's application.  
**Potential Impact:** Module 4 (Defenses). If an API caller asserts a federal law conflict defense, the engine must apply the narrower EEOC standard, not the regulation's literal text. This needs to be resolved before Module 4 logic is written.  
**Resolution Needed:** Confirm that the engine applies EEOC's interpretation (narrow: other law must affirmatively prohibit the accommodation, not merely make it inconvenient or inconsistent).

---

## OQ-002 — Pre-ADAAA Disability Definition Language in Source 06

**Source:** EEOC Enforcement Guidance on RA (Source 06), issued Oct. 17, 2002  
**Issue:** Source 06 is the primary operative guidance on RA and undue hardship, but it was issued 7 years before ADAAA took effect (Jan. 1, 2009). Its disability definition language uses the pre-ADAAA "substantially limits" standard, which Congress explicitly rejected as too demanding. EEOC has posted an ADAAA notice on this guidance but has not re-issued it.  
**Potential Impact:** Modules 2 and 3. Any section of Source 06 that discusses who qualifies for RA based on disability determination must be read against the ADAAA-amended § 1630.2(j) (Source 03) and not taken literally. Sections of Source 06 addressing the RA analysis itself (interactive process, undue hardship factors, accommodation types) remain fully current.  
**Resolution Needed:** For each Source 06 passage used in module logic, tag whether it addresses (a) disability determination (deferring to Source 03/09) or (b) RA process (applying Source 06 directly). Do not use Source 06's disability definition passages as operative rules.

---

## OQ-003 — No Formal Process Required (JAN) vs. Interactive Process Strongly Encouraged (EEOC)

**Source:** JAN Guide § III.A.1 (Source 10) vs. EEOC Enforcement Guidance (Source 06)  
**Issue:** JAN Guide states "There are no specific policies or procedures that employers must follow when trying to accommodate an employee with a disability." EEOC enforcement guidance, while not mandating a formal process, strongly implies that failure to engage in an informal interactive process (clarifying needs, exploring options) constitutes a deficiency and can support a discrimination finding. Courts have treated employer failure to engage as evidence of bad faith.  
**Potential Impact:** Module 3 (Interactive Process). The engine should distinguish between "no formal written process required" (JAN/EEOC: correct) and "no interactive process needed" (incorrect). The `interactive_process_steps` vocabulary is valid; the engine should flag cases where the employer skipped interactive process steps as elevated risk even absent a formal policy requirement.  
**Resolution Needed:** In Module 3, apply the rule that interactive process is effectively required in practice (EEOC enforcement posture) even though no specific formal procedures are mandated (JAN/regulation text). Document the distinction in module reasoning output.

---

## OQ-004 — § 1630.2(l), (n), (o), (p), (r) Not Captured (Page Truncation)

**Source:** 29 CFR § 1630.2 (Source 03)  
**Issue:** The fetch of § 1630.2 was truncated before reaching subsections (l) (regarded as — full text), (n) (essential functions), (o) (reasonable accommodation definition), (p) (undue hardship — full factor list), and (r) (direct threat). These subsections contain vocabulary terms required by Phase 1 (specifically `undue_hardship_factors.net_cost`, `direct_threat_factors.harm_imminence`, `disability_bases.regarded_as`).  
**Disposition:** These subsections are well-established regulatory text known from authoritative sources. Vocabulary terms derived from them are marked `"derived_from"` in `ada_vocabulary.json` with accurate citations and will be spot-check verified against the Cornell LII source in a supplemental fetch during Module 2/4 build phases. The vocabulary entries below are grounded in the regulatory text as confirmed by EEOC Q&A (Source 08) and EEOC Enforcement Guidance (Source 06).  
**Resolution Needed:** Before Module 2 build: re-fetch § 1630.2 in segments or fetch the eCFR version to capture (l), (n), (o), (p), and (r) verbatim.

---
