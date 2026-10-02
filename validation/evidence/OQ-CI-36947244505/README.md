# OQ-CI-36947244505 — Final Source-to-URS Successor Evidence

> **MOCK / FICTIONAL — DEMONSTRATION ONLY — NOT FOR GxP USE**

Exact system-under-test candidate:

`df40d5b71517e30af425d3b0f02e4e05c920cca6`

Candidate tree:

`14431f747e3072435f7664263724cd10c3365da1`

## Result

- frozen-authority guard: **PASS**
- compilation: **PASS**
- expanded development/adversarial tests: **19 / 19 PASS**
- unchanged frozen OQ: **18 / 18 PASS**
- OQ execution ID: `OQ-CI-36947244505`
- GitHub Actions run: `36947244505`
- job: `110652043880`

## DEV-011 closure

This execution follows the preserved failure in run `36946957100`, where the source-to-URS pressure test demonstrated that receiving could complete without the distinct receipt date required by URS-002.

The corrected successor requires a valid ISO receipt date and retains it separately from system creation time in the authoritative record and both output forms.

## Artifact identity

- artifact ID: `11203030254`
- artifact: `sampletrack-oq-36947244505`
- ZIP SHA-256: `45c51df8787a32a5851ee6895d89a4c7bfc3e424364b49019f08ebe232b28845`
- size: 26,208 bytes

Repository-native copies below preserve the final execution record, evidence manifest, environment receipt, and source/execution hash ledgers after the Actions artifact expires.

The manifest records SHA-256 identities for all per-test evidence JSON files even though the compact repository evidence surface does not duplicate every JSON payload.
