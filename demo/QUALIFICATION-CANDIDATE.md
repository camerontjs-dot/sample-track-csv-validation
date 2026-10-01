# SampleTrack Surrogate Qualification Candidate - Historical Record

> **MOCK / FICTIONAL - DEMONSTRATION ONLY - NOT FOR GxP USE**

This historical record identifies the pre-correction surrogate state submitted to the repaired GitHub Actions qualification apparatus. It does not represent the final qualified candidate. The final qualified candidate is `37a23e1bb28c4fc96d6fcdc252d91e8a4e57ba0e`; see `validation/STL-OQ-001-final-qualification-receipt.md`.

## System-under-test source objects

- `demo/sampletrack.py` blob: `4fbe45cc3c5314c8456d390f6da581db9e087e19`
- `demo/test_sampletrack.py` blob: `79937d8497497b0cf6a7088ce7cb80411882d1f7`
- `demo/oq_runner.py` blob: `aa98aae1dc503c964136447e94e7b83f9878073e`

The application, development tests, and OQ runner are unchanged from the initial pre-CI candidate. GitHub Actions records the exact repository commit and environment used for each qualification attempt.

## Apparatus lineage

Workflow run `36811955161` failed before checkout because the workflow supplied an escaped SHA ref. No compile, unit test, or OQ execution occurred in that run.

The workflow expression was corrected without changing the system-under-test source blobs above. The next pull-request-head run is the first eligible hosted qualification attempt.
