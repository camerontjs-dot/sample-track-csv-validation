# STL-IQ-001 — Installation Qualification Checklist: Demonstration Surrogate Environment

> **MOCK / FICTIONAL — TRAINING & INTERVIEW DEMONSTRATION ONLY — NOT FOR GxP USE**
>
> **MOCK IQ CHECKLIST.** This is not a production IQ and does not qualify any real infrastructure. STL-VSR-001 section 14 still lists formal installation qualification of real infrastructure as not established. Approvals are `UNSIGNED – MOCK`.

| Field | Value |
|---|---|
| Document ID | STL-IQ-001 |
| Title | IQ Checklist: Demonstration Surrogate Environment |
| System | SampleTrack Lite demonstration surrogate (`demo/`) |
| Environment | GitHub-hosted Actions runner used by `.github/workflows/sampletrack-oq.yml` |
| Reference execution | `OQ-CI-36947930824` (run `36947930824`, candidate `c3463a18b18c359d4d639055c4e3f6121df79f80`) |
| Document status | Approved (mock) |
| Approval status | Mock approval blocks only, `UNSIGNED – MOCK` |

## 1. Purpose

The OQ evidence in this package was produced on a GitHub-hosted runner, not on a qualified server. This checklist records what that environment is, where each fact comes from, and what was observed on the terminal run. It is a short, honest stand-in for IQ, so a reviewer can see the installation assumptions behind the OQ.

## 2. Sources

- `.github/workflows/sampletrack-oq.yml` (what the workflow requests);
- `validation/evidence/OQ-CI-36947930824/qualification-environment.txt` (what the runner reported);
- `validation/evidence/OQ-CI-36947930824/source-sha256.txt` (what code was installed);
- the import lists of `demo/sampletrack.py`, `demo/oq_runner.py`, `demo/test_sampletrack.py`, `demo/test_pressure.py`.

"Observed" below means the value appears in the preserved evidence for `OQ-CI-36947930824`. It does not mean a person inspected the runner.

## 3. Checklist

| # | Item | Requirement / specification | Source | Observed on OQ-CI-36947930824 | Result (mock) |
|---|---|---|---|---|---|
| IQ-01 | Runner image | `runs-on: ubuntu-latest` (GitHub-hosted) | workflow | Ubuntu 24.04 (STL-VSR-001 section 6); kernel `6.17.0-1022-azure` (`qualification-environment.txt`) | Observed |
| IQ-02 | Architecture | x86_64 | workflow default | `architecture=x86_64` | Observed |
| IQ-03 | Python interpreter | `actions/setup-python@v5`, `python-version: "3.13"` | workflow | `Python 3.13.15` | Observed |
| IQ-04 | SQLite library | Python standard-library `sqlite3` | source imports | `sqlite=3.45.1` | Observed |
| IQ-05 | Third-party packages | None required; standard library only | source imports, README | No install step in workflow; imports are standard library only | Observed |
| IQ-06 | Source checkout | `actions/checkout@v4` at exact candidate SHA, `fetch-depth: 0` | workflow | `candidate_sha=c3463a18b18c359d4d639055c4e3f6121df79f80`, tree `dcc0159f5cfaca61e3768497442e3fce8ae9613f` | Observed |
| IQ-07 | Clean working tree | Only the evidence output directory may be untracked | workflow (`git status --porcelain`) | `?? validation/evidence/OQ-CI-36947930824/` only | Observed |
| IQ-08 | Installed source identity | SHA-256 of `sampletrack.py`, `test_sampletrack.py`, `test_pressure.py`, `oq_runner.py` captured before OQ | workflow "Source digests" step | Recorded in `source-sha256.txt`; matches STL-VSR-001 section 2 | Observed |
| IQ-09 | Frozen validation authority | Five frozen documents and the test configuration match pinned blob SHAs | workflow "Verify frozen validation authority" step | Guard PASS (evidence README) | Observed |
| IQ-10 | Compilation | `python -m py_compile` on the four Python files | workflow "Compile candidate" step | PASS | Observed |
| IQ-11 | Workflow permissions | `permissions: contents: read` | workflow | As configured | Configuration review only |
| IQ-12 | Evidence retention | `actions/upload-artifact@v4`, `retention-days: 30`; durable copy committed under `validation/evidence/` | workflow, evidence README | Artifact `11203126111`; repository copy matches hosted SHA-256 after DEV-013 | Observed |
| IQ-13 | Time source | Runner system clock, UTC timestamps | `execution.md` | Executed at `2026-10-02T00:49:49+00:00` | Observed, not independently verified |

## 4. Known gaps

- `ubuntu-latest` and `python-version: "3.13"` are moving targets. A rerun can land on a different image or patch release, so the observed values above belong to this run only.
- The runner clock, image provenance, and hosted network are GitHub's, not qualified by this package.
- No backup/restore, access control of the hosting platform, or disaster recovery is covered.
- Local reproduction (for example Python 3.13.5 on another machine) is useful behavioral evidence but is outside this checklist.

## 5. Mock approvals

| Signatory role | Name | Date | Meaning of signature | Signature |
|---|---|---|---|---|
| Author (validation lead / exercise owner) | Not entered (mock) | YYYY-MM-DD, not signed | I prepared this document and confirm it is accurate and complete for its stated scope. | `UNSIGNED – MOCK` |
| Reviewer (technical / process SME) | Not entered (mock) | YYYY-MM-DD, not signed | I reviewed this document for technical accuracy, consistency with upstream documents, and traceability. | `UNSIGNED – MOCK` |
| QA Approver (Quality Assurance) | Not entered (mock) | YYYY-MM-DD, not signed | I approve this document for use within the bounded mock validation package. | `UNSIGNED – MOCK` |

## 6. Revision history

| Revision | Status | Description |
|---|---|---|
| 1.0 | Approved (mock) | Initial mock IQ checklist for the GitHub-hosted surrogate environment, grounded in the workflow file and OQ-CI-36947930824 evidence. |
