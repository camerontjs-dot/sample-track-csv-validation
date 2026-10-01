# STL-OQ-001 — Public-Release Pressure Qualification Receipt

> **MOCK / FICTIONAL — DEMONSTRATION ONLY — NOT FOR GxP USE**

| Field | Value |
|---|---|
| Record type | Public-release adversarial successor qualification |
| Qualification disposition | PASS FOR BOUNDED MOCK OQ AFTER PRESSURE TEST |
| Exact application/runner candidate | `b528234a0a14db68200c9213516d0ed6a76ca56b` |
| Candidate tree | `834831c3df75d2a610c338c02657036c8ee9695a` |
| GitHub Actions run | `36897449285` |
| Job | `110487913996` |
| Execution ID | `OQ-CI-36897449285` |
| Frozen OQ protocol blob | `c3e0b589362d3c12650e1ade1290da36db1a3f31` |
| Approval status | Mock approval: Not executed |

## 1. Why this successor exists

The earlier bounded qualification candidate `37a23e1bb28c4fc96d6fcdc252d91e8a4e57ba0e` passed the then-current development gates and complete frozen OQ.

Before publication, an additional adversarial pressure review challenged assumptions and behavior outside the original OQ's explicit examples.

That review found additional material gaps. Publication was blocked, the failures were preserved as DEV-005 through DEV-010, corrections were applied without weakening the frozen OQ, and the full successor gates were rerun.

This receipt therefore supersedes the earlier qualification receipt as the current release authority.

## 2. Pressure-test findings

The public-release pressure test exposed and preserved:

- **DEV-005:** prior QA verification remained valid after critical lot data changed;
- **DEV-006:** a GMP-relevant On Hold status change could be recorded without reason;
- **DEV-007:** regulated record/history/export reads lacked an authenticated authority boundary;
- **DEV-008:** a same-status request returned before authentication;
- **DEV-009:** NaN/infinite temperature values were not rejected and malformed text leaked a raw conversion error;
- **DEV-010:** the TC-015 QA audit-review assertion used the wrong authenticated role after read-boundary hardening.

The first pressure run failed before OQ. A later second-wave probe also failed before OQ. Neither failure was rewritten into a pass.

## 3. Corrective behavior

The successor:

- invalidates prior critical-data verification when the lot value changes;
- requires rationale for GMP-relevant On Hold status transitions;
- requires authenticated authority for regulated record, search, export and history retrieval;
- validates session authority before a same-status no-op return;
- invalidates issued sessions after account disable or role change;
- rejects nonnumeric and non-finite temperature values through controlled validation errors;
- executes TC-015's QA audit-review step with `QA_REVIEW_01`.

## 4. Final execution result

Environment:

- Ubuntu 24.04
- x86_64
- Python 3.13.15
- SQLite 3.45.1

Gates:

- compilation: **PASS**
- expanded development/adversarial suite: **18 / 18 PASS**
- unchanged frozen OQ: **18 / 18 PASS**
- OQ failures: **0**

No frozen OQ expected result was changed to obtain the passing result.

## 5. Source identity

SHA-256:

- `demo/sampletrack.py`: `c719094618123bc280cb0d9ce204da1f7072004e40e48a9787b38b02f1aa14b5`
- `demo/test_sampletrack.py`: `1a9a45f3710b452b9b078d738698011b21d964f4803e97b510afe410f1484363`
- `demo/oq_runner.py`: `aac407bec114b285298642f4ae22f8fa8d32d384e5cd170542073687689ea5b6`

## 6. Execution evidence identity

Core execution SHA-256:

- `execution.json`: `1ccd18f02deaf920f08f2742906a37e70d375e6b0f7f3f87c13e39df774e2b3b`
- `execution.md`: `6129581178cad83cd9fadf64a20795ea4128e73d220794c78dd9358b8fad55d7`
- `manifest.json`: `2f572bad3c11ea34a2c343da5dee839b602874c14ce36c9bbee3772f56df1e08`

GitHub Actions artifact:

- artifact ID: `11180665087`
- artifact: `sampletrack-oq-36897449285`
- ZIP SHA-256: `7c1d8c52dd6161b16130d20699ce1a5ff47a4edc9ef54454cd469966af6c05af`
- size: 25,925 bytes

The downloaded ZIP was independently re-hashed to the same SHA-256 and passed a ZIP integrity test.

A durable repository copy of the final step-level execution record, evidence manifest, environment receipt and hash ledgers is stored under:

`validation/evidence/OQ-CI-36897449285/`

## 7. Regulatory/source pressure recheck

Immediately before release reconciliation, current official Health Canada GUI-0001, GUI-0050, GUI-0069 and the current eCFR Part 11 text were rechecked.

The mappings used by the package remain supportable for the bounded exercise, including:

- risk-based validation and documented risk assessment;
- traceable user requirements;
- process/data-limit and error-handling tests;
- critical manually entered data checks;
- authorized system access;
- audit trails and retained reasons;
- electronic-signature manifestation/linkage;
- controlled storage, receiving and excursion handling.

The Part 11 material remains a conditional exercise overlay rather than an assertion that the fictional Canadian operation is subject to FDA jurisdiction.

## 8. Deviation disposition

DEV-001 through DEV-010 are resolved for the successor application/runner candidate.

Earlier failed executions remain preserved and continue to constrain the claim.

## 9. Bounded disposition

**PASS FOR BOUNDED MOCK OQ AFTER PUBLIC-RELEASE PRESSURE TEST**

This supports the mock functional-validation claim only.

It does not establish:

- supplier qualification;
- formal production IQ/PQ;
- qualified production infrastructure;
- backup/restore or long-term archive qualification;
- production cybersecurity;
- production-grade identity/credential architecture;
- real SOP/training effectiveness;
- scientific suitability of a real excursion;
- actual regulatory compliance;
- production readiness.

## 10. Revision history

| Revision | Status | Description |
|---|---|---|
| 1.0 | Qualified successor | Final public-release pressure qualification after DEV-005 through DEV-010. |
