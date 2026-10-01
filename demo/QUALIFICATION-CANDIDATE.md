# SampleTrack Surrogate Qualification Candidate

> **MOCK / FICTIONAL — TRAINING & INTERVIEW DEMONSTRATION ONLY — NOT FOR GxP USE**

This record submits the current pull-request head to the repaired GitHub Actions qualification apparatus. It does not modify the frozen validation protocol or expected results.

## System-under-test source objects

- `demo/sampletrack.py` blob: `4fbe45cc3c5314c8456d390f6da581db9e087e19`
- `demo/test_sampletrack.py` blob: `79937d8497497b0cf6a7088ce7cb80411882d1f7`
- `demo/oq_runner.py` blob: `aa98aae1dc503c964136447e94e7b83f9878073e`

The application, development tests, and OQ runner are unchanged from the initial pre-CI candidate. GitHub Actions records the exact repository commit and environment used for each qualification attempt.

## Apparatus lineage

Workflow run `36811955161` failed before checkout because the workflow supplied an escaped SHA ref. No compile, unit test, or OQ execution occurred in that run.

The workflow expression was corrected without changing the system-under-test source blobs above. The next pull-request-head run is the first eligible hosted qualification attempt.
