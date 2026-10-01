# STL-OQ-001 — Final Qualification Receipt

> **MOCK / FICTIONAL — TRAINING & INTERVIEW DEMONSTRATION ONLY — NOT FOR GxP USE**

| Field | Value |
|---|---|
| Record type | Corrective full-OQ qualification receipt |
| Qualification disposition | PASS FOR BOUNDED MOCK OQ |
| Candidate commit | `37a23e1bb28c4fc96d6fcdc252d91e8a4e57ba0e` |
| Candidate tree | `0fd797f7a4532ef18284aa8484c2db7036532c02` |
| GitHub Actions run | `36813357212` |
| Job | `110213023142` |
| Execution ID | `OQ-CI-36813357212` |
| Executed at | 2026-10-01T04:03:52+00:00 |
| Protocol | STL-OQ-001 frozen blob `c3e0b589362d3c12650e1ade1290da36db1a3f31` |
| Approval status | Mock approval: Not executed |

## 1. Purpose

This receipt records the final corrective qualification run of the SampleTrack Lite **custom demonstration surrogate** after preservation and disposition of the earlier validation failures.

It does not transform the custom Python surrogate into the fictional GAMP Category 4 supplier product and does not establish fitness for real GxP production use.

## 2. Exact execution boundary

GitHub Actions checked out the exact candidate commit in detached-HEAD state.

Observed environment:

- GitHub-hosted Ubuntu 24.04 runner;
- architecture: x86_64;
- Python: 3.13.15;
- SQLite: 3.45.1;
- candidate SHA: `37a23e1bb28c4fc96d6fcdc252d91e8a4e57ba0e`;
- candidate tree: `0fd797f7a4532ef18284aa8484c2db7036532c02`.

The only working-tree addition at environment capture was the qualification evidence output directory created by the workflow.

## 3. Execution mode and independence

GitHub Actions executed the qualification steps automatically against the exact candidate.

The generated execution record uses `Tester: Cameron` to identify the exercise owner/protocol operator. It does not represent a manual step-by-step execution by Cameron.

The qualification has useful separation from implementation state because the expected behavior was frozen before qualification and the hosted runner checked out exact committed source. It is **not** organizationally independent validation: the application, runner, and package were developed within the same project.

## 4. Development gates

Before OQ execution:

- Python compilation: **PASS**
- development tests: **10 / 10 PASS**

The development tests include requirement-derived adversarial checks added after DEV-004:

- unauthenticated GxP write must fail through a controlled authentication error;
- caller-constructed forged session authority must be rejected;
- inclusive 8.0 °C upper boundary remains within range.

Development tests are supporting evidence. The frozen OQ remains the qualification authority.

## 5. Frozen OQ result

Complete STL-OQ-001 execution:

- OQ cases: **18**
- PASS: **18**
- FAIL: **0**

The final run includes:

- direct unauthenticated GxP access challenge;
- valid, invalid, and disabled authentication;
- GxP access challenge after failed authentication;
- receiving-record identity and required data;
- critical-data verification;
- retained correction history and deletion denial;
- human-readable and electronic record copies;
- storage-location compatibility;
- controlled status values and status authority;
- all six frozen temperature-boundary inputs;
- excursion record linkage and hold/disposition;
- custody-history retention;
- RBAC and user-access lifecycle;
- GMP audit-trail coverage, content, immutability, and reviewability;
- electronic-signature manifestation, linkage, credential challenge, and attribution;
- end-to-end receiving → storage → custody → excursion → hold → QA disposition → retrieval.

## 6. Protocol-conformance check

The frozen OQ contains 18 cases and 99 numbered protocol steps.

The final qualification runner exposes the complete frozen behavior set.

For OQ-TC-002 through OQ-TC-018, runner assertion counts match the frozen protocol step counts.

OQ-TC-001 is deliberately expanded rather than compressed:

- the frozen protocol has five numbered steps, including one combined instruction to attempt a GxP data-changing function after each failed authentication;
- the runner separately records the invalid-password post-failure access challenge and the disabled-account post-failure access challenge.

This expansion increases inspectability and does not change the frozen expected behavior.

DEV-002 is therefore closed by the final full execution.

## 7. Source identity

SHA-256 captured from the exact checkout before OQ:

- `demo/sampletrack.py`: `c0bcf3919279d41aabe90f63056f8b63b57e38f3ca8a3d146ab5a128ea28afe4`
- `demo/test_sampletrack.py`: `a3318e9522b01e1e77d4db9247af2085cf89836121737301378350de6e6735e1`
- `demo/oq_runner.py`: `0789c67da040a73904602b3ef0638e3ed27adca72268c180b92ffdf207ce68af`

## 8. Execution evidence identity

Execution-file SHA-256:

- `execution.json`: `33fa401498126a58369b57226d1856bb97ae92548a0c15d2d081e6eec04186cd`
- `execution.md`: `65956cd5541b3efc6a24e7a81cc7945c685e34a5d4ae20fc900bdca2f1d833c3`
- `manifest.json`: `0318f5f73106054e3a1f95d83a08c258af10e75d625454eca7a69ce42f01204a`

Representative evidence hashes and all remaining evidence hashes are recorded in the uploaded manifest.

GitHub Actions artifact:

- artifact ID: `11140757299`
- artifact name: `sampletrack-oq-36813357212`
- artifact ZIP SHA-256: `94f82fb01bdd9999c4d71ccbd2587702181ab45bf7833dc39cb987b16051a490`
- artifact size: 25,879 bytes

The artifact ZIP digest was independently rechecked after download and matched the GitHub artifact digest.

## 9. Deviation lineage

This passing execution does not erase the earlier failures.

Relevant preserved validation history:

- **DEV-001:** upper temperature boundary defect. Corrected and requalified.
- **DEV-002:** automated harness did not initially expose every frozen protocol step clearly enough. Corrected and full OQ rerun.
- **DEV-003:** evidence-bundle execution identity collision. Corrected with unique execution IDs and full OQ rerun.
- **DEV-004:** uncontrolled/forgeable authentication authority boundary. Adversarially confirmed, corrected, development-gated, and full OQ rerun.

The pre-execution workflow checkout failure in run `36811955161` remains classified separately as an apparatus failure because no system-under-test code or OQ step executed.

## 10. Qualification disposition

**PASS FOR BOUNDED MOCK OQ**

The exact candidate above satisfied the complete frozen functional OQ under the recorded hosted environment after correction and requalification.

This supports only the bounded mock functional-validation claim.

It does **not** establish:

- real supplier qualification;
- production IQ or infrastructure qualification;
- formal PQ under actual warehouse operating conditions;
- long-term backup/restore or archive performance;
- real organizational SOP/training effectiveness;
- cybersecurity certification;
- scientific acceptability of a real product excursion;
- FDA jurisdiction or Part 11 compliance of a real system;
- production readiness.

Those non-claims remain part of the final validation decision.

## 11. Revalidation trigger

Any change to the tested application behavior, frozen validation authority, authentication model, status workflow, temperature logic, evidence apparatus, or other material validated behavior requires impact assessment before relying on this receipt.

## 12. Revision history

| Revision | Status | Description |
|---|---|---|
| 1.0 | Qualified | Final corrective full-OQ receipt for exact candidate `37a23e1...`. |
| 1.1 | Qualified | Clarified automated execution ownership and limited independence. |
