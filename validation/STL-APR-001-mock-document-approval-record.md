# STL-APR-001 — Mock Approval Record for Frozen Input Documents

> **MOCK / FICTIONAL — TRAINING & INTERVIEW DEMONSTRATION ONLY — NOT FOR GxP USE**
>
> **MOCK APPROVAL RECORD. No real person has signed anything in this file.** Every signature cell reads `UNSIGNED – MOCK`. No fictional named approvers are created, consistent with STL-VP-001.

| Field | Value |
|---|---|
| Document ID | STL-APR-001 |
| Title | Mock Approval Record for Frozen Input Documents |
| System | SampleTrack Lite |
| Document status | Approved (mock) |
| Approval status | Mock approval blocks only, `UNSIGNED – MOCK` |

## 1. Purpose

This record moves the frozen input documents of the package from Draft to **Approved (mock)** without changing a single byte of them.

Five input documents are part of the STL-OQ-001 protocol freeze, and the qualification workflow (`.github/workflows/sampletrack-oq.yml`, step "Verify frozen validation authority") checks that their current Git blob hashes still equal the frozen values. Editing their header status or adding an approval block inside them would change those hashes. Under STL-OQ-001-protocol-freeze.md section 8 that would create a new protocol candidate after the terminal OQ had already been executed against the frozen blobs, and it would break the release record that points to them.

So the approval is recorded here, bound to the exact frozen blob identity of each document. This is also how a document-control system usually works: the signature manifest names the exact version being approved.

## 2. How to read the status

- The `Document status` field inside each frozen document still reads as it did at freeze (`Draft` or `Draft / pre-execution`). That text is part of the frozen blob and is left unchanged on purpose.
- The approval state for that exact blob is recorded in this file as `Approved (mock)`.
- If a frozen document is ever changed, the approval below does not carry over. The new blob needs a successor freeze and a new approval entry.

STL-RSK-001 is not hash-pinned by the workflow and has been revised after freeze through its own revision history, so its mock approval block is inside the document itself (STL-RSK-001 section 18).

## 3. Approval entries

### 3.1 STL-SD-001 — System Description and Intended Use

| Field | Value |
|---|---|
| File | [`validation/STL-SD-001-system-description-intended-use.md`](STL-SD-001-system-description-intended-use.md) |
| Approved blob (Git blob SHA) | `d4729f5e0f2b6151dda7b3fc73ba5adf253b8c56` |
| In-file status at freeze | Draft |
| In-file revision at freeze | 0.1 |
| Mock approval status | Approved (mock) |

| Signatory role | Name | Date | Meaning of signature | Signature |
|---|---|---|---|---|
| Author (validation lead / exercise owner) | Not entered (mock) | YYYY-MM-DD, not signed | I prepared this document and confirm it is accurate and complete for its stated scope. | `UNSIGNED – MOCK` |
| Reviewer (technical / process SME) | Not entered (mock) | YYYY-MM-DD, not signed | I reviewed this document for technical accuracy, consistency with upstream documents, and traceability. | `UNSIGNED – MOCK` |
| QA Approver (Quality Assurance) | Not entered (mock) | YYYY-MM-DD, not signed | I approve this document for use within the bounded mock validation package. | `UNSIGNED – MOCK` |

### 3.2 STL-RA-001 — Regulatory Applicability Statement

| Field | Value |
|---|---|
| File | [`validation/STL-RA-001-regulatory-applicability.md`](STL-RA-001-regulatory-applicability.md) |
| Approved blob (Git blob SHA) | `a270ed06c54c43fe94ff4583def0de44594f5b13` |
| In-file status at freeze | Draft |
| In-file revision at freeze | 0.1 |
| Mock approval status | Approved (mock) |

| Signatory role | Name | Date | Meaning of signature | Signature |
|---|---|---|---|---|
| Author (validation lead / exercise owner) | Not entered (mock) | YYYY-MM-DD, not signed | I prepared this document and confirm it is accurate and complete for its stated scope. | `UNSIGNED – MOCK` |
| Reviewer (technical / process SME) | Not entered (mock) | YYYY-MM-DD, not signed | I reviewed this document for technical accuracy, consistency with upstream documents, and traceability. | `UNSIGNED – MOCK` |
| QA Approver (Quality Assurance) | Not entered (mock) | YYYY-MM-DD, not signed | I approve this document for use within the bounded mock validation package. | `UNSIGNED – MOCK` |

### 3.3 STL-VP-001 — Validation Plan

| Field | Value |
|---|---|
| File | [`validation/STL-VP-001-validation-plan.md`](STL-VP-001-validation-plan.md) |
| Approved blob (Git blob SHA) | `6b798621cf44d8ee28c31f7dfeb267fc5ca8c491` |
| In-file status at freeze | Draft |
| In-file revision at freeze | 0.1 |
| Mock approval status | Approved (mock) |

| Signatory role | Name | Date | Meaning of signature | Signature |
|---|---|---|---|---|
| Author (validation lead / exercise owner) | Not entered (mock) | YYYY-MM-DD, not signed | I prepared this document and confirm it is accurate and complete for its stated scope. | `UNSIGNED – MOCK` |
| Reviewer (technical / process SME) | Not entered (mock) | YYYY-MM-DD, not signed | I reviewed this document for technical accuracy, consistency with upstream documents, and traceability. | `UNSIGNED – MOCK` |
| QA Approver (Quality Assurance) | Not entered (mock) | YYYY-MM-DD, not signed | I approve this document for use within the bounded mock validation package. | `UNSIGNED – MOCK` |

### 3.4 STL-URS-001 — User Requirements Specification

| Field | Value |
|---|---|
| File | [`validation/STL-URS-001-user-requirements.md`](STL-URS-001-user-requirements.md) |
| Approved blob (Git blob SHA) | `673a2739bd817c5c348c94572e65e7e113766118` |
| In-file status at freeze | Draft |
| In-file revision at freeze | 0.2 |
| Mock approval status | Approved (mock) |

| Signatory role | Name | Date | Meaning of signature | Signature |
|---|---|---|---|---|
| Author (validation lead / exercise owner) | Not entered (mock) | YYYY-MM-DD, not signed | I prepared this document and confirm it is accurate and complete for its stated scope. | `UNSIGNED – MOCK` |
| Reviewer (technical / process SME) | Not entered (mock) | YYYY-MM-DD, not signed | I reviewed this document for technical accuracy, consistency with upstream documents, and traceability. | `UNSIGNED – MOCK` |
| QA Approver (Quality Assurance) | Not entered (mock) | YYYY-MM-DD, not signed | I approve this document for use within the bounded mock validation package. | `UNSIGNED – MOCK` |

### 3.5 STL-OQ-001 — Operational Qualification Protocol

| Field | Value |
|---|---|
| File | [`validation/STL-OQ-001-operational-qualification.md`](STL-OQ-001-operational-qualification.md) |
| Approved blob (Git blob SHA) | `c3e0b589362d3c12650e1ade1290da36db1a3f31` |
| In-file status at freeze | Draft / pre-execution |
| In-file revision at freeze | 0.2 |
| Mock approval status | Approved (mock) |

| Signatory role | Name | Date | Meaning of signature | Signature |
|---|---|---|---|---|
| Author (validation lead / exercise owner) | Not entered (mock) | YYYY-MM-DD, not signed | I prepared this document and confirm it is accurate and complete for its stated scope. | `UNSIGNED – MOCK` |
| Reviewer (technical / process SME) | Not entered (mock) | YYYY-MM-DD, not signed | I reviewed this document for technical accuracy, consistency with upstream documents, and traceability. | `UNSIGNED – MOCK` |
| QA Approver (Quality Assurance) | Not entered (mock) | YYYY-MM-DD, not signed | I approve this document for use within the bounded mock validation package. | `UNSIGNED – MOCK` |

## 4. Verification

Anyone can confirm that the approved blob is the file in the repository:

```bash
git hash-object validation/STL-SD-001-system-description-intended-use.md
git hash-object validation/STL-RA-001-regulatory-applicability.md
git hash-object validation/STL-VP-001-validation-plan.md
git hash-object validation/STL-URS-001-user-requirements.md
git hash-object validation/STL-OQ-001-operational-qualification.md
```

Each output must equal the blob SHA in section 3. The qualification workflow runs the same comparison before any test executes.

## 5. Limits

- This is not a GxP approval and does not create one.
- It does not change the bounded disposition in STL-VSR-001.
- It does not assert that any real Author, Reviewer, or QA Approver reviewed these documents.

## 6. Revision history

| Revision | Status | Description |
|---|---|---|
| 1.0 | Approved (mock) | Initial mock approval record for the five hash-frozen input documents, bound to their frozen blob SHAs; all signatures `UNSIGNED – MOCK`. |
