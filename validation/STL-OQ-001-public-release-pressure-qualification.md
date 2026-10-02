# STL-OQ-001 — Public-Release Pressure Qualification Receipt

> **MOCK / FICTIONAL — DEMONSTRATION ONLY — NOT FOR GxP USE**

| Field | Value |
|---|---|
| Record type | Public-release adversarial successor qualification |
| Qualification disposition | PASS FOR BOUNDED MOCK OQ AFTER PRESSURE TEST |
| Exact application/runner candidate | `c3463a18b18c359d4d639055c4e3f6121df79f80` |
| Candidate tree | `dcc0159f5cfaca61e3768497442e3fce8ae9613f` |
| GitHub Actions run | `36947930824` |
| Job | `110654144729` |
| Execution ID | `OQ-CI-36947930824` |
| Frozen OQ protocol blob | `c3e0b589362d3c12650e1ade1290da36db1a3f31` |
| Approval status | Mock approval: Not executed |

## 1. Why this successor exists

The earlier bounded qualification candidate `37a23e1bb28c4fc96d6fcdc252d91e8a4e57ba0e` passed the then-current development gates and complete frozen OQ.

Before publication, an additional adversarial pressure review challenged assumptions and behavior outside the original OQ's explicit examples.

That review found additional material gaps. Publication was blocked, the failures were preserved as DEV-005 through DEV-011, corrections were applied without weakening the frozen OQ, and the full successor gates were rerun.

This receipt therefore supersedes the earlier qualification receipt as the current release authority.

## 2. Pressure-test findings

The public-release pressure test exposed and preserved:

- **DEV-005:** prior QA verification remained valid after critical lot data changed;
- **DEV-006:** a GMP-relevant On Hold status change could be recorded without reason;
- **DEV-007:** regulated record/history/export reads lacked an authenticated authority boundary;
- **DEV-008:** a same-status request returned before authentication;
- **DEV-009:** NaN/infinite temperature values were not rejected and malformed text leaked a raw conversion error;
- **DEV-010:** the TC-015 QA audit-review assertion used the wrong authenticated role after read-boundary hardening;
- **DEV-011:** receiving records could complete without the distinct receipt date required by URS-002;
- **DEV-012:** denied completed-record deletion attempts were not represented in the audit trail.

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
- requires and validates a distinct ISO receipt date and retains it in authoritative and exported records;
- authenticates before deletion-attempt record resolution and records attributable audit evidence for denied completed-record deletion attempts.

## 4. Final execution result

Environment:

- Ubuntu 24.04
- x86_64
- Python 3.13.15
- SQLite 3.45.1

Gates:

- compilation: **PASS**
- expanded development/adversarial suite: **20 / 20 PASS**
- unchanged frozen OQ: **18 / 18 PASS**
- OQ failures: **0**

No frozen OQ expected result was changed to obtain the passing result.

## 5. Source identity

SHA-256:

- `demo/sampletrack.py`: `1e1b016debc4ca45319171468b2fe048a473e92b5eb6a5f1e60d4a95412db939`
- `demo/test_sampletrack.py`: `36b0f41d79476d9f42f412e33a20f71de2840ea5c3eee4c2adb1895589d1928a`
- `demo/test_pressure.py`: `34c05b01dad118b06b32ec0fcc56e616e72411c50e0ed3a20a1fe3db3c97609a`
- `demo/oq_runner.py`: `982a635c3fff19e942401e272cba5f2c061572c614d192951b4f44632c7bbf37`

## 6. Execution evidence identity

Core execution SHA-256:

- `execution.json`: `6463f66f0a3d8a32c44368e9fc314a7b13ab90f26fcaa577f82726db6e3396f4`
- `execution.md`: `560add9b413a2ada9e5803a5f9857c274035aee96ca33fe3d2fac38984650904`
- `manifest.json`: `80d8d58ce14cb0e0561957fb8443622e2148a369a7d572314d044b69b989a9e6`

GitHub Actions artifact:

- artifact ID: `11203126111`
- artifact: `sampletrack-oq-36947930824`
- ZIP SHA-256: `0ac0db89702f40c98204f65537e23950b04fb3b5348bc0c11d03ca54f4315749`
- size: 26,321 bytes

The downloaded ZIP was independently re-hashed to the same SHA-256 and passed a ZIP integrity test.

A durable repository copy of the final step-level execution record, evidence manifest, environment receipt and hash ledgers is stored under:

`validation/evidence/OQ-CI-36947930824/`

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

DEV-001 through DEV-012 are resolved for the successor application/runner candidate.

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
