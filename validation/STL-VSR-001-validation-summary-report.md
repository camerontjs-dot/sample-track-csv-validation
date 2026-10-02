# STL-VSR-001 — SampleTrack Lite Validation Summary Report

> **MOCK / FICTIONAL - DEMONSTRATION ONLY - NOT FOR GxP USE**

| Field | Value |
|---|---|
| Document ID | STL-VSR-001 |
| Title | SampleTrack Lite Validation Summary Report |
| System | SampleTrack Lite demonstration surrogate |
| Document status | Final mock validation summary |
| Final disposition | ACCEPTED FOR BOUNDED MOCK DEMONSTRATION USE |
| Production disposition | NOT APPROVED FOR GxP PRODUCTION USE |
| Approval status | Mock approval: Not executed |

## 1. Purpose

This Validation Summary Report summarizes the evidence generated for the SampleTrack Lite mock computerized-system validation exercise and records the final bounded validation decision.

The report evaluates whether the exact custom demonstration surrogate satisfied the frozen functional validation scope defined by the mock package.

It does not establish that a real supplier product has been validated, that a production environment has been qualified, or that any real pharmaceutical operation may rely on this surrogate for GxP use.

## 2. System and candidate identity

Validation scenario:

- fictional SampleTrack Lite configured-product scenario;
- custom Python/SQLite demonstration surrogate used only to generate genuine execution evidence.

Exact qualified system-under-test candidate:

- commit: `c3463a18b18c359d4d639055c4e3f6121df79f80`
- tree: `dcc0159f5cfaca61e3768497442e3fce8ae9613f`
- `demo/sampletrack.py` SHA-256: `1e1b016debc4ca45319171468b2fe048a473e92b5eb6a5f1e60d4a95412db939`
- `demo/test_sampletrack.py` SHA-256: `36b0f41d79476d9f42f412e33a20f71de2840ea5c3eee4c2adb1895589d1928a`
- `demo/oq_runner.py` SHA-256: `982a635c3fff19e942401e272cba5f2c061572c614d192951b4f44632c7bbf37`

The repository branch later advanced through documentation-only reconciliation commits.

A direct Git blob comparison confirmed that the current branch copies of the application, development tests, and OQ runner remain byte-identical to the exact tested candidate.

## 3. Governing validation package

The final decision is based on:

- STL-SD-001 — System Description and Intended Use
- STL-RA-001 — Regulatory Applicability Statement
- STL-VP-001 — Validation Plan
- STL-URS-001 — User Requirements Specification
- STL-RSK-001 — Functional Risk Assessment
- STL-RTM-001 — Requirements Traceability Matrix
- STL-OQ-001 — Operational Qualification Protocol
- STL-OQ-001 — Test Configuration and Data Set
- STL-OQ-001 — Protocol Freeze Record
- STL-OQ-001 — Execution Readiness Record
- STL-DL-001 — Validation Deviation Log
- STL-OQ-001 — Final Qualification Receipt
- preserved GitHub Actions execution evidence

The OQ protocol and test oracle were frozen before implementation qualification.

## 4. Regulatory and guidance basis

The package was designed primarily against the Canadian GMP scenario defined in STL-RA-001.

Primary sources included:

- Health Canada GUI-0001;
- Health Canada GUI-0050, Annex 11 to the GMP Guide: Computerized Systems;
- Health Canada GUI-0069 for environmental control during storage and transportation.

GAMP 5 Second Edition was used as industry lifecycle/risk guidance.

Selected 21 CFR Part 11 controls were included as a conditional electronic-record/electronic-signature exercise overlay. U.S. legal applicability was not asserted.

A pre-OQ source review identified and corrected a requirement gap before execution: URS-007 was expanded to require accurate and complete record copies in both human-readable and electronic form because the package explicitly mapped that requirement to Part 11 §11.10(b).

No frozen expected result was changed after observing OQ behavior in order to obtain the final passing disposition.

### Public-release regulatory recheck

Immediately before public-release reconciliation on 2026-10-01, the package mappings were rechecked against the current official Health Canada GUI-0001, GUI-0050 and GUI-0069 pages and the current eCFR Part 11 text.

That recheck continued to support the package's bounded design choices around risk-based validation, URS traceability, parameter/data limits and error handling, critical manual-data checks, authorized access, audit trails, electronic-signature linkage, controlled storage, receiving and excursion handling.

The public-release pressure suite added explicit malformed/non-finite temperature tests in response to GUI-0050's data-limit/error-handling expectation.

## 5. Validation scope executed

The mock qualification exercised:

- authentication and disabled-account behavior;
- unique user identity and role-based authority;
- receiving and inventory record creation;
- critical manually entered data verification;
- storage-condition and location compatibility;
- controlled material statuses and permitted transitions;
- temperature-excursion boundary detection;
- excursion hold and QA disposition;
- chain-of-custody history;
- GMP-relevant audit-trail behavior;
- electronic-signature manifestation, authentication, attribution, and record linkage;
- regulated-record retrieval;
- human-readable and electronic record copies;
- end-to-end receipt through excursion and disposition.

Formal production IQ and PQ were not executed.

## 6. Execution environment

Final full OQ:

- GitHub Actions run: `36947930824`
- job: `110654144729`
- execution ID: `OQ-CI-36947930824`
- executed: 2026-10-02T00:49:49+00:00
- GitHub-hosted Ubuntu 24.04 runner
- architecture: x86_64
- Python: 3.13.15
- SQLite: 3.45.1

The workflow checked out the exact candidate in detached-HEAD state.

## 7. Execution ownership and independence

The final OQ was executed automatically by GitHub Actions against the exact pinned repository candidate.

The `Tester: Cameron` field in the generated execution record identifies the exercise owner/protocol operator. It does **not** mean Cameron manually performed each automated test step.

Independence is limited:

- the OQ requirements and expected results were frozen before the demonstration surrogate was qualified;
- GitHub Actions provided a clean hosted execution environment against exact committed code;
- however, the surrogate implementation, automated qualification runner, and validation package were developed within the same overall project;
- the final OQ is therefore reproducible behavioral evidence, but not an organizationally independent validation or independent second implementation.

This limitation is retained in the final claim rather than describing CI execution as independent QA approval.

## 8. Development verification

Before final OQ execution:

- Python compilation: **PASS**
- development/adversarial tests: **20 / 20 PASS**

The development suite included targeted regression/adversarial checks for:

- inclusive 8.0 °C upper boundary behavior;
- controlled denial of unauthenticated GxP writes;
- rejection of a caller-constructed forged session;
- authentication and disabled-account behavior;
- storage compatibility;
- QA authority;
- audit-trail protection;
- electronic-signature credential enforcement.

These tests supplement but do not replace OQ.

## 9. Operational Qualification result

Final frozen OQ result:

| Measure | Result |
|---|---:|
| Planned OQ cases | 18 |
| Executed OQ cases | 18 |
| PASS | 18 |
| FAIL | 0 |
| Open OQ deviations | 0 |

The final execution includes the complete frozen behavior set.

OQ-TC-001 expands one combined frozen step into separate invalid-password and disabled-account post-failure GxP-access checks. This increases inspectability without changing the expected behavior.

### Evidence identity

GitHub Actions artifact:

- artifact ID: `11203126111`
- artifact: `sampletrack-oq-36947930824`
- artifact ZIP SHA-256: `0ac0db89702f40c98204f65537e23950b04fb3b5348bc0c11d03ca54f4315749`

Core execution hashes:

- `execution.json`: `6463f66f0a3d8a32c44368e9fc314a7b13ab90f26fcaa577f82726db6e3396f4`
- `execution.md`: `560add9b413a2ada9e5803a5f9857c274035aee96ca33fe3d2fac38984650904`
- `manifest.json`: `80d8d58ce14cb0e0561957fb8443622e2148a369a7d572314d044b69b989a9e6`

Individual evidence IDs and hashes are preserved in the execution manifest and final qualification receipt.

## 10. Validation deviations

Twelve validation deviations were preserved across qualification and public-release pressure testing.

### DEV-001 — Upper temperature boundary defect

Initial OQ observed:

- expected 8.0 °C: Within range;
- actual: Excursion.

Classification: system/configuration failure.

The defect was corrected without modifying the frozen expected result, and the complete OQ was rerun.

Final status: **RESOLVED**.

### DEV-002 — Qualification harness protocol coverage

The first automated OQ harness did not expose every frozen protocol step with sufficient step-level clarity.

Classification: protocol/execution-apparatus discrepancy.

The runner was reconciled to the frozen protocol and the complete OQ was rerun.

Final status: **RESOLVED**.

### DEV-003 — Duplicate execution identity

Separate qualification bundles initially reused the same internal execution ID.

Classification: evidence/execution-apparatus deficiency.

Unique GitHub-run-derived execution IDs were added and the complete OQ was rerun.

Final status: **RESOLVED**.

### DEV-004 — Authentication authority boundary

Corrected harness coverage exposed an uncontrolled unauthenticated access failure. Requirement-derived adversarial tests then confirmed a forged-session authorization path.

Classification: system authentication/authorization boundary failure.

The surrogate was corrected to use application-issued opaque session authority, validate session state, reject absent/forged/stale sessions, and invalidate session authority when access changes.

Final candidate passed the adversarial development tests and full OQ.

Final status: **RESOLVED**.

### DEV-005 — Critical verification remained valid after critical lot correction

Pressure testing demonstrated that a previous QA verification could remain set after the underlying lot value changed.

Correction: critical lot correction now invalidates the prior critical-data verification and requires re-verification before release.

Final status: **RESOLVED**.

### DEV-006 — On Hold transition allowed without required reason

Pressure testing showed that a GMP-relevant Quarantine → On Hold transition could be recorded without rationale.

Correction: the transition now requires a non-empty reason and preserves it in audit history.

Final status: **RESOLVED**.

### DEV-007 — Regulated record retrieval lacked an authentication boundary

Pressure testing showed that public retrieval/history/export methods could return regulated record data without an authenticated session.

Correction: regulated record, lot search, export, audit, custody, excursion and signature retrieval now require authenticated role authority.

Final status: **RESOLVED**.

### DEV-008 — Same-status request returned before authentication

A no-op status request could return before session authorization was checked.

Correction: authentication/role validation now occurs before the same-status early return.

Final status: **RESOLVED**.

### DEV-009 — Malformed and non-finite temperature values were not controlled

Second-wave pressure testing showed that NaN and infinite numeric values were accepted by the comparison path, while nonnumeric text leaked a raw conversion exception.

Correction: temperature input is normalized through controlled conversion and rejects nonnumeric or non-finite values with ValidationError before classification/evidence creation.

Final status: **RESOLVED**.

### DEV-010 — QA audit-review OQ step used the wrong authenticated read role

After read-boundary hardening, apparatus inspection found that TC-015's QA-reviewability assertion still read the audit trail using a Warehouse session.

Correction: the frozen QA-reviewability step now retrieves and evaluates the audit trail using QA_REVIEW_01.

Final status: **RESOLVED**.

### DEV-011 — Required receipt date absent from receiving record

Final source-to-URS review showed that URS-002 explicitly required a distinct receipt date before receiving completion, while the surrogate stored only system creation time and had no receipt-date field.

Classification: system / required-data completeness failure, with a qualification-coverage gap because the frozen OQ fixture did not separately exercise receipt date.

Correction: the surrogate now requires a valid ISO receipt date, retains it separately from system creation time, and includes it in electronic and human-readable output.

Final status: **RESOLVED**.

### DEV-012 — Denied deletion attempt lacked audit evidence

Final requirement-level review showed that the surrogate correctly denied permanent deletion of a completed GxP record but did not create an audit event for the denied deletion attempt required by URS-029 where supported.

Correction: authentication/authority is evaluated before target-record disclosure, the deletion remains denied, and an attributable `delete_attempt_denied` audit event records the actor, date/time, record, and reason.

Final status: **RESOLVED**.

### Public-release pressure qualification

Pressure-test lineage:

- run `36895767954`: four requirement-level failures, frozen OQ not entered;
- run `36896153123`: first-wave corrections passed 16/16 development/adversarial tests and 18/18 frozen OQ;
- run `36897292169`: second-wave data-limit tests exposed malformed/non-finite temperature handling, frozen OQ not entered;
- run `36946957100`: final source-to-URS receipt-date challenge exposed DEV-011, frozen OQ not entered;
- run `36947244505`: DEV-011 correction passed 19/19 development/adversarial tests and 18/18 unchanged frozen OQ;
- run `36947828276`: deletion-attempt audit challenge exposed DEV-012, frozen OQ not entered;
- run `36947930824`: **20/20 development/adversarial tests PASS and 18/18 unchanged frozen OQ PASS**.

The final pressure test therefore did not merely rerun the previous success. It added new falsifiers that found additional defects, preserved them, and required a successor qualification.

### Pre-execution apparatus incident

GitHub Actions run `36811955161` failed during checkout because of an escaped SHA ref.

No system-under-test code or OQ step executed.

Classification: **pre-execution apparatus failure**.

This incident is preserved separately and is not treated as a SampleTrack functional result.

## 11. Requirements traceability

Final RTM status:

- URS requirements: **35 / 35 represented**
- requirements with risk linkage: **35 / 35**
- requirements with final OQ evidence: **35 / 35**
- final requirement status: **35 / 35 VERIFIED — PASS**
- open validation deviations: **0**
- total recorded validation deviations: **12 / 12 resolved**

Requirement-specific deviation history remains visible for the affected temperature and authentication controls.

The RTM references exact final OQ evidence IDs and separately records supplemental public-release pressure evidence for the requirements that exposed DEV-005 through DEV-012.

## 12. Functional risk disposition

Design-time risk assessment:

- High: 9
- Medium: 4
- Low: 2

The original Severity, Probability, Detectability, RPN, and class values remain unchanged after testing.

Following final OQ:

- all 15 functional risks have at least one executed verification path;
- the associated application controls are marked **SUPPORTED WITH BOUNDS — OQ-CI-36947930824 PASS**.

A successful OQ does not mean the risks cease to exist or that real production probability has been measured.

## 13. Validation Plan acceptance criteria

| Acceptance criterion | Final status | Evidence basis |
|---|---|---|
| Final in-scope URS uniquely identified | PASS | STL-URS-001, 35 requirements |
| Every in-scope URS traced or explicitly dispositioned | PASS | STL-RTM-001, 35/35 |
| All planned OQ tests executed or formally dispositioned | PASS | OQ-CI-36947930824, 18/18 executed |
| High-risk functions receive risk-proportionate verification | PASS | STL-RSK-001 V3 paths; final OQ |
| No unresolved deviation invalidates a high-risk requirement or conclusion | PASS | STL-DL-001, 0 open deviations |
| Failed tests corrected through impact assessment and justified retest | PASS | DEV-001 through DEV-012 lineage |
| Access, status, excursion, audit, e-signature, and record-retrieval controls meet applicable criteria | PASS | Final 18/18 OQ evidence |
| Tested system/configuration identity known | PASS | exact commit/tree/source SHA-256 |
| RTM reflects final executed evidence | PASS | STL-RTM-001 executed/reconciled revision |
| Residual risks and untested production dependencies explicit | PASS | STL-RSK-001 and this VSR |

Formal organizational QA approval is intentionally not fabricated.

## 14. Residual limitations

The following were not established by this mock package:

- supplier quality-system qualification;
- validation of a real commercial configured product;
- production server/cloud/network/database qualification;
- formal installation qualification of real infrastructure;
- formal PQ under actual warehouse operating conditions;
- backup/restore qualification;
- long-term archive accessibility and retention;
- production business-continuity/disaster-recovery performance;
- real SOP and training effectiveness;
- cybersecurity assessment or penetration testing;
- production-grade credential storage or identity-provider integration; the surrogate's local credential mechanism is deliberately demonstrative and is not a production authentication design;
- production workload/performance;
- real sensor/logger qualification;
- warehouse temperature mapping;
- pharmaceutical stability or scientific acceptability of a real temperature excursion;
- actual Canadian, U.S., or EU regulatory compliance;
- FDA Part 11 jurisdiction;
- production deployment.

These are boundaries, not hidden assumptions that are being treated as passed.

## 15. Final validation decision

### Disposition

**ACCEPTED FOR BOUNDED MOCK DEMONSTRATION USE**

Within the defined fictional scenario, the exact custom demonstration surrogate candidate `c3463a18b18c359d4d639055c4e3f6121df79f80` satisfied the frozen functional URS/OQ acceptance criteria after documented correction and requalification of the observed validation deviations.

### Production decision

**NOT APPROVED FOR GxP PRODUCTION USE**

This package does not qualify SampleTrack Lite, the demonstration surrogate, or any real computerized system for regulated production use.

The final claim is limited to the tested mock functional boundary.

## 16. Revalidation / reconsideration triggers

The bounded disposition should be reconsidered if any of the following materially change:

- application source or validated behavior;
- authentication/session authority;
- roles or permissions;
- material-status workflow;
- storage conditions or location rules;
- excursion thresholds or comparison logic;
- audit-trail behavior;
- electronic-signature behavior;
- persistence/data representation;
- external interfaces;
- qualification runner or evidence semantics;
- frozen URS/risk/OQ authority;
- regulatory requirements applicable to the intended use.

A documentation-only change does not automatically require requalification, but its impact should be assessed if it changes interpretation of the validation claim.

## 17. Conclusion

The mock package achieved its intended demonstration objective:

```text
intended use
  → regulatory applicability
  → user requirements
  → functional risk
  → frozen OQ
  → preserved failure
  → deviation / correction / retest
  → final evidence
  → traceability closure
  → bounded validation decision
```

The evidence supports the bounded mock disposition above and no broader claim.

## 18. References

- STL-RA-001 — Regulatory Applicability Statement
- STL-VP-001 — Validation Plan
- STL-RSK-001 — Functional Risk Assessment
- STL-RTM-001 — Requirements Traceability Matrix
- STL-DL-001 — Validation Deviation Log
- STL-OQ-001 — Final Qualification Receipt
- GitHub Actions run `36947930824`

## 19. Revision history

| Revision | Status | Description |
|---|---|---|
| 1.0 | Final mock summary | Final bounded validation decision for exact qualified candidate after complete deviation reconciliation. |
| 1.1 | Final mock summary | Clarified automated execution ownership, limited independence, and non-executed mock approval boundary. |
| 2.0 | Final pressure-tested summary | Public-release adversarial review preserved DEV-005 through DEV-010 and qualified successor b528234a with 18/18 pressure tests plus unchanged 18/18 frozen OQ. |
| 2.1 | Final source-to-URS successor | DEV-011 receipt-date completeness failure preserved and resolved; intermediate successor df40d5b passed 19/19 expanded development/adversarial tests plus unchanged 18/18 frozen OQ. |
| 2.2 | Final requirement-level pressure successor | DEV-012 denied-deletion audit gap preserved and resolved; exact successor c3463a18 passed 20/20 development/adversarial tests plus unchanged 18/18 frozen OQ. |
| 2.3 | Evidence-provenance reconciliation | DEV-013 corrected the terminal execution timestamp and repository evidence custody to the hosted-original bytes; no executable, frozen authority, qualification verdict, or validation scope changed. |
