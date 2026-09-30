# STL-RSK-001 — SampleTrack Lite Functional Risk Assessment

> **MOCK / FICTIONAL — TRAINING & INTERVIEW DEMONSTRATION ONLY — NOT FOR GxP USE**

| Field | Value |
|---|---|
| Document ID | STL-RSK-001 |
| Title | SampleTrack Lite Functional Risk Assessment |
| System | SampleTrack Lite |
| Document status | Draft |
| Risk method | FMEA-style qualitative functional risk assessment |
| Approval status | Mock approval: Not executed |

## 1. Purpose

This assessment identifies plausible functional failure modes for the bounded SampleTrack Lite validation scenario and determines the **planned depth of verification** needed to challenge them.

The assessment is not a mathematical proof of safety and does not convert a numerical score into a release decision.

A risk is not considered controlled merely because a requirement or mitigation has been written. Residual-risk disposition remains **OPEN pending verification** until the relevant controls have been exercised and the resulting evidence is assessed.

## 2. Governing inputs

This assessment is based on:

- STL-SD-001 — System Description and Intended Use;
- STL-RA-001 — Regulatory Applicability Statement;
- STL-VP-001 — Validation Plan;
- STL-URS-001 — User Requirements Specification.

The current assessment assumes the intended-use and regulatory boundaries in those documents remain unchanged.

## 3. Regulatory and guidance basis

### 3.1 Health Canada GUI-0050

Health Canada GUI-0050 §4.1 states that computerized-system risk management should be applied throughout the lifecycle with consideration of:

- patient safety;
- data integrity;
- product quality.

The extent of validation and data-integrity controls should be based on a **justified and documented risk assessment**.

GUI-0050 §4.4 further states that:

- validation standards, protocols, acceptance criteria, procedures, and records should be justified by risk;
- URS should be based on documented risk assessment and GMP impact;
- user requirements should remain traceable through the lifecycle;
- test methods and scenarios should consider process parameter limits, data limits, and error handling.

GUI-0050 §4.6 also requires risk management to consider the criticality and potential consequences of erroneous manually entered data.

### 3.2 Health Canada GUI-0069

GUI-0069 states that quality risk management for storage and transportation should:

- be based on scientific knowledge and process experience;
- ultimately link to protection of the patient;
- use effort, formality, and documentation commensurate with risk.

Temperature is identified as an important environmental parameter, and drug storage/transport should reduce the risk of exposure outside labelled conditions. Excursions require scientific/technical assessment rather than automatic acceptance.

### 3.3 ICH Q9 / Q9(R1) methodology note

Health Canada GUI-0001 and GUI-0069 refer to ICH Q9 for quality risk-management examples.

The current ICH final revision is **ICH Q9(R1), adopted at Step 4 on 18 January 2023**. It defines risk as the combination of the probability of occurrence of harm and the severity of that harm and notes that detectability may sometimes be considered.

This exercise uses Q9(R1) as **current international QRM methodology/background guidance**. It does not assert that Health Canada's general ICH implementation table has replaced its listed Q9 implementation with Q9(R1).

ICH Q9(R1) also highlights the need to manage subjectivity in risk assessment and to scale QRM formality to the decision and risk.

### 3.4 GAMP 5 Second Edition

GAMP 5 Second Edition is used as industry guidance for risk-based computerized-system lifecycle activity.

Software categorization is treated as one input to risk assessment and supplier/lifecycle scaling, not as a checklist that automatically determines validation effort.

## 4. Risk question

For each material SampleTrack function:

> What could fail in a way that compromises patient/product protection, material control, data integrity, required GxP records, or the ability to reconstruct and control the warehouse/distribution process, and what verification is needed to expose that failure?

## 5. Assessment method

This exercise uses a structured FMEA-style approach with three ordinal factors:

- **Severity (S)** — consequence if the failure occurs;
- **Probability (P)** — qualitative likelihood of the failure under the fictional configured-product scenario;
- **Detectability (D)** — likelihood that the failure would remain undetected before it causes or supports the consequential outcome.

A supporting Risk Priority Number is calculated as:

```text
RPN = Severity × Probability × Detectability
```

The RPN is a prioritization aid only.

It is **not** treated as the regulatory definition of risk and does not override professional judgment or severity.

## 6. Rating scales

### 6.1 Severity

| Score | Definition |
|---:|---|
| 1 | Negligible. No meaningful GxP record, product-quality, patient, status-control, or traceability impact. |
| 2 | Minor. Local process/record inconvenience or easily corrected discrepancy with no credible effect on material disposition, critical traceability, or product quality. |
| 3 | Moderate. Could impair traceability, investigation, or operational control and require a quality-system response, but is unlikely by itself to support release/distribution of unsuitable product if other controls operate. |
| 4 | Major. Could materially compromise required records, quality decision-making, access control, recall/segregation capability, or the ability to reconstruct a significant GxP event. |
| 5 | Critical. Could permit release/distribution/use of unsuitable or potentially affected product, defeat a critical hold/segregation control, or materially prevent effective containment/recall with plausible patient or product-quality harm. |

### 6.2 Probability

Because SampleTrack Lite is fictional and has no operational history, probability is **qualitative**. No invented failure-rate percentages are used.

| Score | Definition |
|---:|---|
| 1 | Rare. Requires an exceptional combination of configuration/conditions and is strongly constrained by ordinary design/process controls. |
| 2 | Unlikely. Credible but not expected during normal operation; opportunity exists through configuration, user action, or defect. |
| 3 | Possible. Plausible during routine use or configuration and not inherently self-preventing. |
| 4 | Likely. Expected to recur if the relevant control is defective or absent. |
| 5 | Frequent. A normal or recurring path is expected to produce the failure without an effective control. |

### 6.3 Detectability

Higher numbers mean **worse detectability**.

| Score | Definition |
|---:|---|
| 1 | Almost certain to be detected before consequential use through an independent or unavoidable control. |
| 2 | Likely to be detected during the normal workflow before consequential use. |
| 3 | May be detected, but normal workflow does not reliably guarantee detection before consequence. |
| 4 | Unlikely to be detected before the affected decision, distribution, or record reliance. |
| 5 | No reliable independent detection before consequential use; the system failure may appear normal to the user. |

## 7. Risk classification

The following exercise-specific rules prevent arithmetic from masking a severe failure:

### High

Classify **HIGH** when any of the following apply:

- Severity = 5; or
- Severity = 4 and Detectability >= 4; or
- RPN >= 50.

### Medium

Classify **MEDIUM** when not already High and either:

- Severity = 4; or
- RPN is 20–49.

### Low

Classify **LOW** when:

- Severity <= 3; and
- RPN <= 19; and
- no critical status, release, excursion, access, signature, or data-integrity control is directly defeated.

These bands are local decision rules for this mock package. They are not presented as GAMP, ICH, or Health Canada thresholds.

## 8. Verification-depth classes

Risk classification influences verification depth, but the plausible failure mode determines the actual test design.

### V1 — Basic

Typical for Low risk:

- direct positive functional check;
- configuration review where relevant;
- evidence sufficient to establish the observed result.

### V2 — Enhanced

Typical for Medium risk:

- positive case;
- at least one negative, edge, or error case relevant to the failure mode;
- direct review of affected stored/history data where applicable;
- explicit evidence reference.

### V3 — Critical

Typical for High risk:

- positive and negative cases;
- boundary/error cases where parameters or limits are material;
- role/authority challenge where access affects the control;
- audit/history/signature verification where the failure could otherwise remain hidden;
- end-to-end challenge where several functions jointly create the control;
- preserved first-run evidence and deviation linkage for any material failure.

V3 does not mean "more screenshots." It means stronger opportunities for the system to fail in the ways that matter.

## 9. Functional risk register

| Risk ID | Failure mode / harmful condition | Principal URS | S | P | D | RPN | Class | Planned control / verification focus | Depth | Residual status |
|---|---|---|---:|---:|---:|---:|---|---|---|---|
| RSK-001 | Duplicate or non-persistent SampleTrack record identity causes ambiguity between otherwise controlled records. | URS-001 | 3 | 1 | 2 | 6 | LOW | Verify unique/persistent identifier behavior and attempt a duplicate/identity-conflict condition where practical. | V1 | OPEN — pending verification |
| RSK-002 | A receiving record can be completed without required GxP fields, leaving material identity/storage information incomplete. | URS-002 | 4 | 2 | 2 | 16 | MEDIUM | Verify required fields, rejected incomplete completion, and retained completed record content. | V2 | OPEN — pending verification |
| RSK-003 | Critical manually entered receiving data is wrong and can support later release without the defined independent/electronic accuracy check. | URS-004 | 4 | 3 | 3 | 36 | MEDIUM | Exercise the configured accuracy-check gate with correct and deliberately discrepant critical data. | V2 | OPEN — pending verification |
| RSK-004 | Material can be assigned an incorrect required storage condition or an incompatible storage location, creating risk of environmental exposure outside approved conditions. | URS-009, URS-010 | 5 | 2 | 3 | 30 | HIGH | Challenge compatible/incompatible locations and storage conditions; verify rejection and retained state. | V3 | OPEN — pending verification |
| RSK-005 | Invalid workflow transition or unauthorized disposition can place unreviewed/held material into Released status or otherwise bypass required QA control. | URS-011–URS-015 | 5 | 2 | 4 | 40 | HIGH | Challenge initial state, allowed/prohibited transitions, Warehouse Operator vs QA authority, rationale, and status history. | V3 | OPEN — pending verification |
| RSK-006 | Temperature-excursion logic fails at or around configured limits, allowing an out-of-range condition to appear acceptable. | URS-016, URS-017 | 5 | 3 | 5 | 75 | HIGH | Boundary-value challenge immediately inside, at, and outside both limits; preserve exact input/output evidence. | V3 | OPEN — pending verification |
| RSK-007 | Excursion record is incomplete or linked to the wrong material, preventing reliable scientific/quality assessment. | URS-018 | 4 | 3 | 3 | 36 | MEDIUM | Verify required excursion fields, affected-record linkage, rejected incomplete data, and retrieval. | V2 | OPEN — pending verification |
| RSK-008 | Material with an unresolved excursion can leave On Hold or be dispositioned without required QA authority/rationale. | URS-019, URS-020 | 5 | 2 | 4 | 40 | HIGH | Challenge hold enforcement, unauthorized release attempt, QA disposition, rationale, history, and end-to-end state. | V3 | OPEN — pending verification |
| RSK-009 | Custody/history events are lost, overwritten, or associated with the wrong record, reducing handling traceability. | URS-021–URS-023 | 3 | 2 | 3 | 18 | LOW | Record successive transfers and verify all prior events remain linked and intelligible. | V1 | OPEN — pending verification |
| RSK-010 | Authentication, unique-user, or role controls fail, allowing unauthorized access or data-changing actions. | URS-024–URS-026 | 4 | 3 | 4 | 48 | HIGH | Valid/invalid authentication, shared-identity prohibition as configured, cross-role negative tests, and attempted unauthorized changes. | V3 | OPEN — pending verification |
| RSK-011 | Revoked access remains usable or access-authorisation changes are not reconstructable. | URS-027, URS-028 | 4 | 2 | 4 | 32 | HIGH | Disable an account and verify rejection; inspect creation/change/cancellation records for access authorisation. | V3 | OPEN — pending verification |
| RSK-012 | GMP-relevant audit trail is absent, incomplete, alterable by ordinary users, or not reviewable, hiding changes to critical records. | URS-005, URS-029–URS-032 | 4 | 3 | 4 | 48 | HIGH | Exercise representative create/change/status/disposition/signature events; verify prior/new values, user/time/reason, immutability, retrieval, and intelligibility. | V3 | OPEN — pending verification |
| RSK-013 | Electronic signature lacks required identity/meaning/date-time, is detachable from the record, or can be applied through another user's credentials. | URS-033–URS-035 | 4 | 2 | 4 | 32 | HIGH | Verify manifestation, permanent record linkage, human-readable output, unique identity, and negative authentication/signature attempt. | V3 | OPEN — pending verification |
| RSK-014 | Required GxP record can be permanently deleted, cannot be reliably retrieved, loses related history, or produces an inaccurate/incomplete human-readable copy. | URS-006–URS-008 | 4 | 2 | 4 | 32 | HIGH | Attempt ordinary-user deletion; retrieve by key identifiers; compare human-readable copy with stored record/history relationships. | V3 | OPEN — pending verification |
| RSK-015 | System records the wrong user or time for a GxP action, weakening attribution and reconstruction even when the business action itself succeeds. | URS-003, URS-015, URS-022, URS-030 | 3 | 2 | 4 | 24 | MEDIUM | Compare acting user/time with receiving, status, custody, and audit events across representative workflows. | V2 | OPEN — pending verification |

## 10. Risk distribution

Current design-time distribution:

| Class | Count |
|---|---:|
| HIGH | 9 |
| MEDIUM | 4 |
| LOW | 2 |
| Total | 15 |

The concentration of High risks is not being treated as a reason to lower scores for visual balance.

The system was intentionally scoped around GxP controls such as material release/hold, temperature excursions, access authority, audit trails, electronic signatures, and regulated-record integrity. Those functions can legitimately carry high consequence.

Conversely, not every requirement is treated as High: record identity and custody history receive lighter verification where their specific bounded failure does not directly defeat a release/hold or product-quality control.

## 11. Highest-risk controls

The following are the primary **release-decision controls** for this exercise:

1. **RSK-004 — storage-condition/location compatibility**
2. **RSK-005 — material-status transition and QA authority**
3. **RSK-006 — excursion threshold logic**
4. **RSK-008 — excursion hold and QA disposition**
5. **RSK-010/011 — authentication, role, and revoked-access control**
6. **RSK-012 — audit-trail integrity/reviewability**
7. **RSK-013 — electronic-signature attribution/linkage**
8. **RSK-014 — GxP record preservation/retrieval**

A material unresolved failure in one of these controls may block a positive validation disposition even if the aggregate test count is otherwise high.

## 12. Risk-to-test design implications

The successor OQ should not allocate test cases evenly across URS rows.

Instead:

- excursion boundary logic should receive several input cases within a single controlled test;
- release/hold authority should be challenged using multiple user roles;
- audit-trail behavior should be inspected after real business events rather than tested only as an isolated screen;
- electronic signatures should be tested for manifestation **and** record linkage;
- record retrieval should compare output to the authoritative stored record rather than merely confirm that an export button works;
- a final end-to-end scenario should exercise the combined control chain from receipt through excursion, hold, QA disposition, audit history, and retrieval.

## 13. Residual-risk rule

No risk in this document is currently marked ACCEPTED or CLOSED.

After OQ:

- a passing test may reduce confidence in the likelihood of the tested failure under the exact conditions exercised;
- a failed test may increase assessed risk or expose a new failure mode;
- a deviation may require re-scoring if the cause changes the assumed failure mechanism;
- residual risk must consider unresolved limitations and production dependencies;
- arithmetic scoring alone cannot authorize release.

The Validation Summary Report will make the final bounded risk/validation disposition.

## 14. Subjectivity controls

Because this is a single-owner mock exercise rather than a real cross-functional QRM team, risk ratings have an inherent subjectivity limitation.

The package reduces that limitation by:

- defining scoring criteria before assigning individual rows;
- separating consequence from test depth;
- recording the reason for each score;
- using explicit severity overrides;
- preserving the exact risk table used to design OQ;
- allowing OQ evidence to revise the assessment rather than forcing the first score to remain correct.

If this were a real implementation, process owner, QA/validation, system owner, IT, supplier, and other appropriate SMEs would participate according to the actual risk.

## 15. Reassessment triggers

Reassess affected risks if:

- intended use changes;
- a URS requirement changes materially;
- a supplier/software version changes;
- configured statuses, roles, storage rules, or excursion limits change;
- an interface is introduced;
- OQ exposes a previously unidentified failure mode;
- a deviation changes the assumed probability, detectability, or consequence;
- operational evidence shows a control is less effective than assumed.

## 16. References

Primary sources used:

- Health Canada GUI-0001 — Good manufacturing practices guide for drug products  
  https://www.canada.ca/en/health-canada/services/drugs-health-products/compliance-enforcement/good-manufacturing-practices/guidance-documents/gmp-guidelines-0001/document.html
- Health Canada GUI-0050 — Annex 11 to the good manufacturing practices guide: Computerized Systems  
  https://www.canada.ca/en/health-canada/services/drugs-health-products/compliance-enforcement/good-manufacturing-practices/guidance-documents/annex-11-guide-computerized-systems-gui-0050.html
- Health Canada GUI-0069 — Guidelines for environmental control of drugs during storage and transportation  
  https://www.canada.ca/en/health-canada/services/drugs-health-products/compliance-enforcement/good-manufacturing-practices/guidance-documents/guidelines-temperature-control-drug-products-storage-transportation-0069.html
- ICH Q9(R1) — Quality Risk Management, final Step 4 guideline, adopted 18 January 2023  
  https://database.ich.org/sites/default/files/ICH_Q9%28R1%29_Guideline_Step4_2023_0126.pdf
- Health Canada — implemented ICH guidelines table  
  https://www.canada.ca/en/health-canada/services/drugs-health-products/drug-products/applications-submissions/guidance-documents/international-council-harmonisation/guidelines.html
- ISPE GAMP 5 Second Edition — industry guidance; copyrighted guide text is not reproduced here.

## 17. Revision history

| Revision | Status | Description |
|---|---|---|
| 0.1 | Draft | Initial risk method, 15 functional failure modes, and verification-depth decisions. |
