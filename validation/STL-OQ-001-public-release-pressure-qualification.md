# STL-OQ-001 — Public-Release Pressure Qualification Receipt

> **MOCK / FICTIONAL — DEMONSTRATION ONLY — NOT FOR GxP USE**

| Field | Value |
|---|---|
| Record type | Public-release adversarial successor qualification |
| Qualification disposition | PASS FOR BOUNDED MOCK OQ AFTER PRESSURE TEST |
| Exact application/runner candidate | `df40d5b71517e30af425d3b0f02e4e05c920cca6` |
| Candidate tree | `14431f747e3072435f7664263724cd10c3365da1` |
| GitHub Actions run | `36947244505` |
| Job | `110652043880` |
| Execution ID | `OQ-CI-36947244505` |
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
- **DEV-010:** the TC-015 QA audit-review assertion used the wrong authenticated role after read-boundary hardening;
- **DEV-011:** receiving records could complete without the distinct receipt date required by URS-002.

The first pressure run failed before OQ. A later second-wave probe also failed before OQ. Neither failure was rewritten into a pass.

## 3. Corrective behavior

The successor:

- invalidates prior critical-data verification when the lot value changes;
- requires rationale for GMP-relevant On Hold status transitions;
- requires authenticated authority for regulated record, search, export and history retrieval;
- validates session authority before a same-status no-op return;
- invalidates issued sessions after account disable or role change;
- rejects nonnumeric and non-finite temperature values through controlled validation errors;
- executes TC-015's QA audit-review step with `QA_REVIEW_01`;
- requires and validates a distinct ISO receipt date and retains it in authoritative and exported records.

## 4. Final execution result

Environment:

- Ubuntu 24.04
- x86_64
- Python 3.13.15
- SQLite 3.45.1

Gates:

- compilation: **PASS**
- expanded development/adversarial suite: **19 / 19 PASS**
- unchanged frozen OQ: **19 / 19 PASS**
- OQ failures: **0**

No frozen OQ expected result was changed to obtain the passing result.

## 5. Source identity

SHA-256:

- `demo/sampletrack.py`: `f61136b70b020d1516470c263308750427ac65fff621be73dacf824ef70a35d0`
- `demo/test_sampletrack.py`: `36b0f41d79476d9f42f412e33a20f71de2840ea5c3eee4c2adb1895589d1928a`
- `demo/test_pressure.py`: `dc35140bde0618f769f3897d31debad643c2e7c581b1d63f03bfe802f636df94`
- `demo/oq_runner.py`: `982a635c3fff19e942401e272cba5f2c061572c614d192951b4f44632c7bbf37`

## 6. Execution evidence identity

Core execution SHA-256:

- `execution.json`: `0b6e1ce0a48b0a31c2340b77051b2736dfca9dbecbf421f962f97f879a9bf062`
- `execution.md`: `3a63c0aa3a18223b46efda35bb90d0828d92d340222652841d94fc51a3b6ad01`
- `manifest.json`: `4cecdd948d3f997ca4d98feb8f2c3a97e391e1f22b4edee9c1d480c157283e04`

GitHub Actions artifact:

- artifact ID: `11203030254`
- artifact: `sampletrack-oq-36947244505`
- ZIP SHA-256: `45c51df8787a32a5851ee6895d89a4c7bfc3e424364b49019f08ebe232b28845`
- size: 26,208 bytes

The downloaded ZIP was independently re-hashed to the same SHA-256 and passed a ZIP integrity test.

A durable repository copy of the final step-level execution record, evidence manifest, environment receipt and hash ledgers is stored under:

`validation/evidence/OQ-CI-36947244505/`

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

DEV-001 through DEV-011 are resolved for the successor application/runner candidate.

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
| 1.1 | Evidence hardening | Added exact SHA-256 identity for the adversarial pressure-test source after CI source-ledger hardening. |
| 2.0 | Final pressure successor | DEV-011 receipt-date completeness failure preserved and resolved; successor passed 19/19 expanded development/adversarial tests plus unchanged 18/18 frozen OQ. |
