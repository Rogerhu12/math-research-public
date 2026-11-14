# Actual54: all 868 direct-LD maps completed; original trial blocked before launch

分类：启发式/数值证据与原件字节核。作者：ChatGPT（geometry / exact_refinement，root统筹发布）。日期：2026-11-14。

## Public outcome and its scope

The public run [43634889730](https://github.com/Rogerhu12/math-research-public/actions/runs/43634889730), source `7eb383af1ca2bb04c7eaef9c65578dbc124269d8`, completed the entire original 868-step capture and the subsequent new 1372 finite-system solver. Its original nonlinear trial entry then failed while opening an incorrectly named actual28 metadata file. The original ten trial evaluations have not run.

Job `132569417352` records the capture step as successful at 20:02:00 UTC, after starting at 19:58:37 UTC. The new-system solver and full residual readback completed at 20:03:48 UTC. The trial entry failed at 20:03:49 UTC, before constructing its native client. Artifact upload and the bounded publisher both succeeded.

This note records the capture and complete byte/metadata audit. The actual new-system direction and exact residuals are treated separately in [the solver/readback note](2026-11-14-actual54-direct-LD1372-solver-and-exact-readback.md). Capture completion establishes the complete saved target and its provenance; it does not itself establish a small linear defect, an accepted original trial, or native completion.

## Complete capture actually produced

The actual capture `native-rawcell0-direct-ld/result.json` is 82529 bytes with SHA256

```text
e60da64312819a87388cfa96c209fc9188dca02c0ab055cbcc934f3507888ac6
```

Its summary `direct-ld-summary.json` is 13698 bytes, SHA256 `98be7804c09c150de4faee22ed91dc68d5a330ecab2dca7febd1d52fe5100a1c`. Its complete array manifest is 609264 bytes, SHA256 `06004e6d6d526efd10e5ac29747585af163c0dfb23f64398eb226f58744de384`.

| Actual recorded quantity | Value |
| --- | ---: |
| Completed original rawCell0 stages |72, exactly indices 0–71 |
| Original scheduled steps |868 |
| Original local RHS/J field calls |3472, four per step |
| Complete new original-coordinate maps |868 of shape 226×224 |
| Shape-J arrays |72, with each stage's actual number of 224×224 blocks |
| Two-mean-row arrays |72, with each stage's actual number of 2×224 blocks |
| Binary array chunks |1736 |
| Saved target array bytes |351533056 |
| Saved binary64 words |43941632 |
| Original protocol requests in capture |1 |
| Additional ODE steps |0 |
| Recomputed original long-J blocks |0 |
| Whole-tail J, endpoint J, final audit or original solve |Not called by this capture |
| Nonlinear trial evaluations |0 |

The 868 count follows the original actual41 profile schedules, including its cusp subdivision, rather than assuming 12 steps in every stage. Each step starts from its original saved complete 226-component input. The original four field stages reproduce the saved state/geometry/root records, original full 226-component output, and original post-port shape output. The direct-LD worker then recomposes the variational map from the four newly returned complete 226×224 local matrices, using the unchanged actual50 `direct_rk` function and a single final cast to binary64.

The produced maps retain both mean rows, with no mean feedback into the 224 shape components. The original Pi port is applied at its original stage exit. This is a new saved original-coordinate f64 map target, with the unchanged original base nodes, residuals, scales, cut/far data and subsequent node restriction contract.

The original native request ends at its declared observation stop:

```text
Error: VISIBLE_NATIVE_RAWCELL0_DIRECT_LD_COMPLETE_V1
```

The completed capture records this exact planned stop, one protocol request and worker exit0. That intentional stop occurs before original native solve and is distinct from the later trial-entry I/O exception.

## Actual source and precision identity

| Source role | Actual SHA256 |
| --- | --- |
| Complete capture launcher | `a63ffda643044787cb0ad5fb0d7c2aa4e4b34090fefa4b9053f4f2550bf85dbf` |
| Native observation hook | `3499f7abb96a4f25c4c3a986d97dc8aea3b21742770aabe7abe2822ad8b3caf4` |
| Original selected-step window | `1ba3f30702b26aa78b4aceb0b2d3d5d71ea8fa858b114d982ead185330faa5d9` |
| Persistent direct-LD worker | `87ab92d9234d6e58103d44d125ce5510f9cde34ac37df251b7e63dcb6747a9c8` |
| Unchanged actual50 arithmetic helper | `01ec3476ce8d2331b49122ce3d001908eb427d52ea52d367a978cd6de9dde548` |

The worker reports Python 3.12.14, NumPy 2.3.5 and x86_64. The actual longdouble representation is x87 binary80 with 64 significand bits, stored in 16 bytes; `numpy_finfo_nmant=63` counts its explicit fraction bits. It is not binary128.

Working longdouble arrays were deliberately not persisted in this complete capture. The runtime precision record identifies the working representation; the independent byte audit concerns the final original-coordinate f64 files. In particular this audit does not claim to have inspected nonexistent longdouble padding files. The unchanged helper and the earlier actual50 working-array audit remain separately identified evidence.

The real recorded timings have different scopes:

- Launcher elapsed: 201.723169902 seconds.
- Hook capture elapsed: 186.829 seconds.
- Persistent worker elapsed: 186.558308511 seconds.
- Worker maximum RSS: 403544 KiB.

These are actual reported measurements. They are not added together, and no unmeasured timing split between local-A capture and matrix formation is inferred.

## Complete byte and saved-field audit

The [audit summary](2026-11-14-actual54-direct-LD-capture-byte-audit.json) and [complete audited-file receipts](2026-11-14-actual54-direct-LD-capture-audited-files.json.gz) were produced by a [local stdlib-only byte reader](../computations/geometry_20261114_actual54_capture_byte_audit.py). It reads stored bytes and metadata; it does not import a scientific producer, recompute an RHS/J/RK step, solve a system, evaluate a norm, or generate a new scientific comparison.

The audit verified all 144 target arrays, every one of their 1736 chunks, full per-array stream hashes, and the complete interleaved chunk journal. All868 worker full-output hashes equal the concatenation of their saved 224 shape rows and two mean rows. All 43941632 stored f64 words are finite by exponent-bit inspection; the stored negative-zero count is 0, matching every worker record.

All 72 complete new field packets were checked against their gzip receipts. After removing the additional `local_A` descriptor, every one of the 3472 saved field records equals its full actual41 counterpart, including the original x/h and geometry/root numberRecords and their explicit float64 bit strings. The original full 226-component step inputs and outputs and the original post-port shape outputs were independently rebound to 3254976 bytes of actual41 state/output arrays. Both the raw gzip identities and the structured comparisons were checked.

The complete source A matrices are represented here by 3472 full-matrix hashes, source identities, same-state/field bindings and complete descriptors. Successful steps did not retain all four raw A matrices, and the audit did not independently regenerate them. The directly inspected target matrices are the complete stored f64 maps.

The two following stream hashes use ascending original stage index and, within each original stage, inner-to-outer flow-step order:

| Saved stream | SHA256 |
| --- | --- |
| 868 shape maps (224×224 each) | `722a11fc8e010cbd7cb89c0ccacbd017bcc4b2c18a1747b335c44fbe62f58f6c` |
| 868 mean maps (2×224 each) | `ea7eae82a14031400030700b7d5c88cd64aead29f29f101ff1cf1d7c369a8a61` |

These are raw capture-stream identities. The new 1372 shooting-system identity additionally includes the adapter's prescribed reverse local ordering, the remaining 504 old blocks and all original boundary/base data; it is supplied by the solver consumer.

The audit checked 4221 stored-file receipts across this capture and the consumed actual41 evidence. Summing the 868 actual worker reports gives 0 working-nonzero entries cast to binary64 zero. That is a reported worker diagnostic; it was not recomputed from unsaved longdouble arrays and is not an added acceptance condition.

## Gzip repair paid by the real run

The full real specification has 1056735 uncompressed bytes. Its gzip file has 145192 bytes:

```text
stored-file SHA256:
ba9894bf30440cdbfb7a58684abbb2901193cf8c2cf3456425814cc2369d9d05

uncompressed JSON SHA256:
ebec051c37ab50b6b5c36c3381afcf39c2a30cd0323c3207a09ba1a81440a989
```

The result, hook, worker-ready record and worker completion all bind the stored compressed-file SHA. The audit verified both representations and the complete decompressed specification. This pays the real transport path that [actual52 had not reached](2026-11-14-actual-request52-direct-LD-spec-transport-failure.md), without changing any scientific expression or reducing the evidence.

## Original trial-entry failure and continuation

The first actual trial traceback identifies:

```text
geometry_20261114_native_direct_ld_trial_replay.py, validate_capture:
    directory=a.capture_directory.resolve();result_path=directory/"result.json.gz"

FileNotFoundError:
.../direct52-original28-43634889730-1/native-correction-capture/result.json.gz
```

The old actual28 capture's file is `result.json`, with its already fixed SHA `ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7`. The newer direction result really is `rawcell0-direct-ld-correction/result.json.gz`; these two different contracts must remain distinct. The actual54 direction result SHA, also printed in the attempted trial CLI, is `e1ac6c83434ac3b269663e930b1370a38f280b2d31c5e720955b5ed0aed7e105`.

This exception occurs during old-input binding, before the trial entry constructs its native client. It is an I/O filename error, not a domain-guard rejection or failure of the original strict-norm-decrease test. No original trial has been accepted or rejected mathematically in this run.

The minimal continuation is a trial-only run that fixes this old28 filename and consumes the already completed actual54 capture and direction together with their original28/41 inputs. It does not require another 868-step capture or another finite-system solve, and it does not insert a new linear-residual acceptance threshold.

The full artifact is `visible-mainline-directld-43634889730-1`, ID `14129522378`, ZIP 457357361 bytes, SHA256 `df3a54716ecbed8645783373657f7e40b08429173ca976efc73ecc7e8ce5f819`. It was downloaded once by the repository coordinator; this note and audit use that completed extraction.
