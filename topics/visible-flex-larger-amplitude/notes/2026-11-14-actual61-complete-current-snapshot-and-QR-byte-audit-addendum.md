# Actual61: complete current-snapshot and QR byte-audit addendum

**Classification:** completed Actions byte-readback evidence; no new scientific computation.  
**Author:** ChatGPT (`exact_refinement`).  
**Date:** 2026-11-14 UTC.

The complete original native61 artifact has now been read and byte-audited in public Actions. Readback run [43654012687](https://github.com/Rogerhu12/math-research-public/actions/runs/43654012687), source `49dcce7493a78b158f905d6d218d51e2ae1be1a3`, job `132628443287`, completed successfully. All four current snapshots and returned QR directions passed their complete byte checks. The original native result remains **failure**; the reader's success does not change it.

This adds byte provenance to [the four-current-QR numerical note](2026-11-14-actual61-four-current576-QR-models-and-exact-readback.md). It does not recompute or reinterpret its norms, gradients, directions, trial acceptances or rejected last iteration.

## 1. Complete original input and actual reader

The reader downloaded and verified the entire original artifact for native run `43645948199`, source `cf6b51193255dfc713610d2919598451ccdd49e2`, artifact `14136633570`, size 2,335,870,174 bytes and ZIP SHA256 `7b17d1b0c11bfe14329a1d8715c8451498d0dedb6821859deb8485e5b1c1b469`. The HTTPS/metadata/streaming-size/SHA/ZIP checks precede the readback. The audit inventories all 7,121 original artifact files.

The executed reader SHA256 is `791300246051bad9064a39cc181d0b5eb6d66d7978d73a28f0c8028f6d8e0329`. It reports `mathematical_computation_performed=false`, no scientific values recomputed, no nonlinear acceptance gate, and an empty error list. Its original scalar result is recorded before its complete byte checks. It does not demand native success to audit a failed run.

The reader artifact is only 2,087,233 bytes: `14137397000`, `visible-completed-readback-43654012687-1`, ZIP SHA256 `4dfed0677b135bdb681c84fac58a17d1878478e0ccfa560e5a546a94a2edf2ef`. It preserves the detailed byte receipts without duplicating the original multi-gigabyte scientific payloads. The public small receipts are under `notes/public-actions-43654012687-1-receipts/request61-readback/`.

## 2. Every current snapshot and every complete R273 factor

Each of the four iterations has its own original state, full with-J snapshot, matrix identity and output direction. The actual per-iteration reader reports all of the following counts; these are copied counts, not a new numerical calculation:

| Per-iteration object | Actual completed scope |
|---|---:|
| Current snapshot arrays | 10 |
| Complete original stage Jacobian blocks | 576 |
| Snapshot raw chunks | 583 |
| Snapshot raw bytes | 234,318,472 |
| QR output arrays | 1,168 |
| Float64 QR output arrays | 1,167 |
| Complete factor nodes, including each node penalty | 577 |
| Factor and pure-constant payload bytes | 464,891,392 |
| Preserved pure-constant rows | 129,248 |
| Literal lower-triangular R zero words checked | 14,411,152 |
| Saved recovery underflow count | 0 |
| Full original cut/stage/far exact-ledger rows | 129,248 |
| Ledger blocks, including cut and far | 578 |

The snapshots include actual state, stage outputs, stage residuals, cut residual, far residual, cut target, physical H, original scales, far graph and complete stage J. The reader checks their array, chunk, source and context identities. It does not reform cut/far residuals or a nonlinear state update. Iteration 0's state is byte-bound to the actual59 selected state; later states are bound to their own current snapshots. No actual28 or 1372-stage cache is relabeled as a current model.

The source/loop receipt verifies the original core and actual method source identities, original maximum 32 iterations, original tolerance `2e-9`, the actual eta metadata and the preserved loop. Every full direction checkpoint agrees with its complete raw delta, including the stored signed-zero representation. All factor nodes and the pure-constant payloads are included; this is not a factor-diagonal-only check.

The unpublished intermediate formed V/rho values are not regenerated. Their original saved identity records are bound to the actual reported model. The reader explicitly distinguishes that recorded-identity scope from exported factor bytes it independently reads.

## 3. Complete integer ledgers and exact worst operands

All original integer row records are read in their complete cut/stage/far order. Each ledger's original J, direction and sigma identities agree with its current snapshot. Per-block maxima agree verbatim with the producer's saved full detail, and the reported global worst record is found verbatim. The reader does not recompute a dyadic value, maximum, product, sum or division.

| Iteration | Uncompressed exact-ledger bytes | Uncompressed ledger SHA256 |
|---|---:|---|
| 0 | 12,233,978 | `4cfd4701da3274da6728c513860996ca0c51d5b0227651efc9d63d3f4ac9ab82` |
| 1 | 12,000,045 | `06d43c825137edaece9aa5231c494a63f38765a25f7ee2ecc9ea90a9525bc852` |
| 2 | 11,817,236 | `250b5154e5c04d8e23c760ef04d865e169e193dd2f4ff24ba1c9c1d1b0f26f9b` |
| 3 | 11,867,087 | `4e25d07140fe4d91fbd32cd5def790c1363432dd7576bf85ae2159c72ee3a9b2` |

The four worst-witness checks each report that all saved operand words agree with the original payload. Their J operands come from the declared `large-arrays/stage-jacobians-0002.f64le` chunk, offset 401,408, length 401,408 bytes. The saved four worst rows remain stage 9, Q1, global equation row 2128; their exact rational results are those already published in the numerical note. Locating and comparing the stored witness bytes does not repeat their arithmetic.

The four public `byte-summary.json` identities are respectively:

- iteration 0: `c90852c3b211fd0e5e23977c2ce97e3db60d661a39c0122b65406e20dd93210b`;
- iteration 1: `7adb58a21d50236eb64bcf4f4e7636521ac8750a26e80a53102230bf5f39aef9`;
- iteration 2: `fb72d0f637e0b993b02e6080ec47ab54b930a145fcfa485c9ea8ea1471cf2fd2`;
- iteration 3: `fe04d8dea2be1b70cc7cfc3455b3645a976f124bed90e883c4e53143805d2c5d`.

Each links its own full compressed byte detail in the reader artifact. The public `reader-status.json` also preserves the exact current-state and all ten raw-array identities for that iteration.

## 4. What this completes

The complete exported-byte scope of native61's four current models is paid. The original last-iteration line-search failure, the distinction between no-J and subsequent fresh with-J observations at the saved states, and the lack of native final acceptance remain unchanged. The completed byte audit provides reproducible input/output identity for a separately authorized same-state diagnostic; it is not an additional numerical acceptance requirement and does not select a cause of the failed nonlinear trials.
