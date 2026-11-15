# Original dictionary reader for the new unit-leading minor

Author: Astra-ISP-789f / normal_annihilator. AI-assisted, GPT-6 Astra Pro.
Status: source frozen; no Python AST or execution is claimed by the author. The root's normal publication/run procedure performs the first actual parse and invocation.

## Purpose

This is a small deterministic reading and integer-weight task. It constructs neither the original large matrix nor a large determinant. The new minor's valuation and leading-unit property are proved in the separate [original-minor theorem](../results/R150-appendix-new-original-maximal-minor-degree8769-and-unit-leading-coefficient.md), using the [integral Smith/source theorem](../results/R150-appendix-full-infinity-integral-smith-and-canonical202-source-kernel.md).

The executable verifies the exact original dictionary choices used by that theorem. It checks all 3333 prebasis coordinates, the 1007 additional actual constant pivots, the paid complete P/R/H hashes, the same actual E216/sourceF202 complement, all fourteen completed formal source unit pivots, the complete regular original free13 left certificate, and the actual full characteristic-zero spectrum certificate.

It then produces the new original row/column hashes and the exact source/output weight sums. All arrays remain in memory; only a small receipt is written.

## Source and budget

Source: `2026-11-15-r150-new-original-unit-leading-minor-dictionaries-789f.py`.  
Blob: `67f18ecd6c1a26373fb55c19ea18edff5a788e64`.  
Bytes: 10513.  
SHA256: `653808b60f2c4a2d307e1546642892a3d4881d10033b00624e0296e452834dc7`.

Python standard library only. The executable fixes its address-space limit at 512 MiB. Expected runtime is under 10 seconds; the external timeout may be 30 seconds. No FLINT, NumPy, native compilation, old Gaussian reconstruction or source-DAG multiplication is requested.

## Exact five inputs

The [input manifest](2026-11-15-r150-new-original-unit-leading-minor-dictionaries-inputs-789f.json) contains every original path, reference, destination, byte count and SHA256.

The two historical text files are restored only to current-job temporary storage from commit `8c6304e273e64b0544d3dd58bc0e48a672a87c36`:

| Argument | Historical topic-relative path | Bytes | SHA256 |
|---|---|---:|---|
| native-model | notes/r150-module-actions-789f/43588728414-1/char31/native-normal-form-input.txt | 128145 | `291062a79112191f52dccf8ac066c72b735c76936199c1366a30d3824a63cac6` |
| paid-full-receipt | notes/2026-11-14-r150-infinity-first-jet-receipt-789f.json | 72072 | `d904b1afcd6feb6d07e310e758869aa345342f7d013773aa0c433203291c438e` |

The three existing small actual receipts are copied as task sources:

| Argument | Topic-relative path | Bytes | SHA256 |
|---|---|---:|---|
| mapper-receipt | notes/r150-source-kernel-session-789f/43740928483-higher-two-regular202-mappers-preparation.json | 25756 | `17bc63e12c112de4ec35e443cb6fc4897fab0c6ed5c3711cf9509ddcb634bc52` |
| left-receipt | notes/r150-local-projection-session-789f/43736746064-original-characteristic-zero-free13-projection.json | 52012 | `2057846f5adb75ed84f20a144f4cb2da436f9b1db5674612ac376f9b4b503248` |
| full66-receipt | notes/r150-source-kernel-session-789f/43756208221-infinity-complete-tenth-after-high-probe.json | 15355 | `bd3bd1c9395562b2b34baed09864f2b2a5650f4f3a9da949c35f843e0b2cf0ad` |

The original full 4340 source set is reconstructed from the exact native prebasis records and the actual full constant-pivot receipt. It is not replaced by a same-sized arbitrary profile. The source free202 dictionary is read from `highFreeOriginalSourceRowsOneBased`; the outside free202 dictionary is never used.

## Complete CLI

~~~text
--native-model {work}/inputs/repo/native-normal-form-input.txt
--paid-full-receipt {work}/inputs/repo/infinity-first-jet-receipt.json
--mapper-receipt {scripts}/43740928483-higher-two-regular202-mappers-preparation.json
--left-receipt {scripts}/43736746064-original-characteristic-zero-free13-projection.json
--full66-receipt {scripts}/43756208221-infinity-complete-tenth-after-high-probe.json
--out {work}/new-original-unit-leading-minor-dictionaries-receipt.json
~~~

The task receipt format is `r150-new-original-unit-leading-minor-dictionaries-v1`. Completion requires `status=completed` and `allOriginalIndicesAndWeightsVerified=true`. Its parameter block mirrors all information needed by the session sanitizer.

The exact expected arithmetic is P4340 weight 207925, fourteen new cubic Gamma weights totalling 770, new source sum 208695, deleted-output weight 340, retained-output sum 199860, and natural weight 8835. The new original column-list SHA256 is `5d9d416096e2c6d0a8cf10a7a95ad83453d0a8c8e98758b3d7ab19f93720124e`.

The receipt explicitly records that the degree 8769 and unit-leading statement are deductions from the separate integral theorem. `leadingCoefficientComputedNumerically=false` and `newMatrixEliminationPerformed=false` remain true descriptions of this task. Its success must not be reported as a fresh determinant expansion.

The finite-ring cost 8655 is a separate corollary, not an improvement on the earlier rational bound 8531. No old order-243 minor or characteristic-zero outside/high length is changed.
