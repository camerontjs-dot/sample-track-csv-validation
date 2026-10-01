# OQ-EXEC-001 — Initial Qualification Evidence

> **MOCK / FICTIONAL — TRAINING & INTERVIEW DEMONSTRATION ONLY — NOT FOR GxP USE**

## Identity

- Candidate: `e1636c513661a8d6784e9594f8929b1592b690c7`
- Tree: `de00cdd3281acb538bc09e43bd4f2ea8ee94e320`
- Workflow run: `36812149305`
- Job: `110209333784`
- GitHub Actions artifact: `11140370333`
- Artifact digest: `sha256:1ad3a8c83f17897e9982c32459023036b66f99c246098b3110e0a74be8afd3b8`
- Executed: 2026-10-01T03:47:54+00:00
- Result: **17 PASS / 1 FAIL**

## Failed test

`OQ-TC-009`, frozen input **8.0 °C**:

- expected: `Within range`
- actual: `Excursion`
- result: `FAIL`

See `STL-EV-OQ-009-01-temperature-boundaries.json` in the uploaded workflow artifact.

## Source SHA-256

- `demo/sampletrack.py`: `15f206cf8c7b59be9a4f6ecb9bba29dda9315096baec81ea8dfc9e8cc3d8c0f4`
- `demo/test_sampletrack.py`: `5d6fa457258548264120c946aa6d3a34a8b633670daf05ddc0d0c47b1a334e26`
- `demo/oq_runner.py`: `9e11e8474bc97bc6b5c9fe8f6ae461cce82b07047486dda2937db6ee0dd53c1b`

## Execution-file SHA-256

- `execution.json`: `3e7f1f56148bfb17117cb0980893fc73d822accc64ed7f0c19eec8baf57dad70`
- `execution.md`: `5ac07cd7719704721fe93a7c3e3714589729e27572cefa0e25fa856aa6e77efe`
- `manifest.json`: `7c59dc26dddee80624b9bf940b58623cbae8141f0405fe26b4a8cae5c488bcab`
- `qualification-environment.txt`: `015bcd9342350d2339dae6ad5237f7b5f8363c7ecdb35956ac735f36954485ab`
- `source-sha256.txt`: `2b09ab3a23ddc5c4d44d69918a725bff93d5d53ba5f7c4d93b45ec9380834b81`
- `execution-sha256.txt`: `ae7e6e1863ad789aba94849eb2e8cd707d915459f2d6b123ca4fb15dceb33425`

The complete original evidence bundle remains attached to workflow run `36812149305`. DEV-001 records the impact and controlled correction path.
