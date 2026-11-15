# Actual79: an accepted 1/32 step; the nearest rejection is the original left RMS query 465

**Classification:** numerical evidence read from the original public Actions reports, with primary-file byte and provenance checks. All scientific values below were saved by that run. Local work only read original fields, checked identities, and hashed bytes; it did not evaluate a field, derivative, matrix action, norm, optimization model, or native tail.

**Author:** amplitude branch of the visible-flex-larger-amplitude session, 2026-11-15 UTC.

## 1. Actual result and execution identity

[Run 43663293492](https://github.com/Rogerhu12/math-research-public/actions/runs/43663293492), source `31d2ad909638aa3eb3211a9ea0feed632c0e9a2b`, job `132657162468`, completed successfully. It continued once from the accepted optimization warm of actual76, using the same frozen 24-query entry and all original budgets and tests. The original warm calculation, new-warm boundary finite-difference check, artifact upload, and publication completed.

The run accepted $\alpha=1/32$ after five rejected trials. Its freshly fixed model-weight merit changed from `43.57627837509625` to `43.5661119869748`. The original producer saved decrease `0.010166388121447767`, predicted unregularized decrease `0.010171022793922435`, and actual/predicted ratio `0.9995443258196769`. At that accepted trial, every original node, midpoint, both 698-point RMS sets, and all 24 selected complete angular grids passed the original domain checks. The new-warm boundary FD passed with maximum fourth-order relative error `1.006440735979892e-9` and the unchanged `5e-5` implementation threshold.

This remains an optimization warm. The saved flags are `optimization_progress: true`, `success: false`, and `new_coupled_finite_acceptance: false`. No actual nonlinear native solve at its new height, accepted complete BVP, or closed surface is asserted. Warm elapsed time was `644.909743449` seconds; the FD took `23.871735339999987` seconds.

The complete science artifact has the following official metadata:

```text
artifact: 14141611284
name: visible-followup-condensedqp-43663293492-1
ZIP bytes: 639331603
ZIP SHA256: c2432e485c0d7e1c2a047d43ade9b0ec9bb159a1e266c8cee81a1b163f298257
```

This primary readback used the five exact published original files obtained by the root agent. The ZIP identity above is official artifact metadata; it is not a claim that the complete science ZIP or its large payloads were independently audited for this note.

## 2. The unchanged finite model and actual parent

The original parent is actual76 warm SHA `bba24c1f882d14751c4272148ee0cd6271c584485c6d0d3efaafa1a081a2a97f`, paired with decoded original status SHA `a1a67b9a1e0e97aa23404a8fa6c5936805de34f763f0076516c4f736aedc4cb5`. Its gzip transport SHA is `d8e9133a002280ff7f116738a53203ff273681414ec8aae2405ced1ee5726c8d`. The complete previous producer subtree and original mesh are retained. The own-schema continuation does not reuse the previous model's frozen weights or call it the same linearization.

The current 24 grids are the 16 original left RMS queries at intervals

```text
466,467,468,469,470,471,472,473,475,477,479,480,481,482,484,485
```

and the eight original collocation-midpoint queries at

```text
473,475,477,480,481,482,484,485.
```

Each grid contains all 2048 original physical-angle samples. There are 49,152 modeled inequality rows. The actual and declared B column sets both contain all physical coordinates at nodes 466 through 486, plus the three shared controls: 7,101 local coordinates, with no zero-layout-only node. The full physical/core/control model retains all 236,036 coordinates.

The C baseline retains its original 4,059-column support and the full outside affine offsets. Complete-H condensation and recovery retain all outside physical variables and all 109 free core variables through their conditional response; they do not freeze these variables to the raw LSMR direction. The run preserves $\lambda=270$, 512 working rows, 200 dual sweeps, original LSMR and projection budgets, the original 17-trial maximum, complete domain checks, original merit rule, and original FD threshold.

All merit comparisons in this note use this model's fixed weights and baseline `43.57627837509625`. A subtraction from actual76's differently weighted final merit would not measure this step's decrease.

## 3. All six trials and the actual nearest rejection

| Actual step | Original node / midpoint failures | Complete selected grids | Original full RMS pass | Saved actual merit |
|---|---|---|---|---:|
| $1$ | 0 / 5: 480,481,482,485,487 | Several existing grids negative | Not evaluated | Not defined |
| $1/2$ | 0 / 1: 487 | All 24 positive | Not evaluated | Not defined |
| $1/4$ | 0 / 0 | All 24 positive | Only left465 invalid | `43.497786820954964` |
| $1/8$ | 0 / 0 | All 24 positive | Only left465 invalid | `43.536202558762135` |
| $1/16$ | 0 / 0 | All 24 positive | Only left465 invalid | `43.55604559818204` |
| **$1/32$** | **0 / 0** | **All 24 positive** | **Both 698-point sets valid** | **`43.5661119869748`** |

The nearest rejected trial is $\alpha=1/16$. Its original nodes and collocation midpoints are finite, all 24 selected angular grids are positive, and its actual merit decreases by `0.02023277691421299`, with ratio `0.9991216630485871`. Its only reported complete-RMS failure is the unmodeled **left RMS query in interval 465**:

```text
fraction: 0.17267316464601146
station: 1.1603320320063233
interval endpoints: 1.1594713509918353, 1.1644558024915952
original beta_squared minimum: -0.421944063367393
physical angle: 0
actual a: 1.193937869693328
actual a_s: -0.04947478091233733
actual a_ss: -2.4969384329285087
curvature at the failing angle: 0.03475048706032548
```

The right RMS set has no invalid query. The original full RMS pass also isolates left465 at the rejected quarter and eighth steps. Their saved beta-squared minima are respectively `-0.23817190989754655` at phi `3.074097498922825` and `-0.9467277660868318` at phi `3.107845076256309`. Their actual merit decreases are `0.07849155414128717` and `0.04007581633411661`, with ratios `0.9960011483498186` and `0.9985204082651623`. These original values do not establish monotonicity of the nonlinear domain margin with step size.

The farther half-step has a different observed obstruction: original midpoint487, station `1.2566681552371528`. Its midpoint input is finite, while its original RHS is nonfinite. The midpoint observer saves minimum beta squared `-0.01312680173833014`, angle index 42, phi `0.12885438618239387`, and four negative angle samples. Its original scalar triple is `[1.1776868977517243, -0.28627350334365187, -2.3953698582934853]`. The associated raw observer descriptor is retained in the compact readout. Because the original midpoint check fails, that half-step does not execute the complete RMS pass or produce an actual merit. Midpoint487 is not the nearest rejection and does not justify adding it in the immediate successor.

At the unit trial, the original bad midpoints are 480,481,482,485,487. Existing selected left466 through left472 and left480, and selected midpoints480,481,482,485, also have negative angular values. The modeled linear beta-squared prediction still has positive global minimum `0.0005926361018506465` at that unit step. This separation between a finite linear model and the actual nonlinear field is why all original full-domain backtracking remains necessary.

At the accepted step, core and control states remain identical across all nodes; original left and constant collocation residuals remain zero. The 4096-angle original uniform-phi guard saves minimum rho `0.16604058243275`. Both RMS fractions `0.17267316464601146` and `0.8273268353539885` have 698 valid queries. The complete original boundary maximum is `1.7532371533528647e-8`.

## 4. Same-model C/H selection and finite optimization scope

The producer selects `R270-condensed-complete-H`. Its same-model objective is `43.40638896445367`, compared with the retained C candidate's `43.57610856795521`. The final full-model directional derivative is `-0.326936439089015`; the saved damped-model decrease is `0.16988941064254867`.

The local QP stops at its 512-working-row budget. Its final local stage has used all 200 dual sweeps and reports minimum unrepaired slack `-1.9906298831529057e-13`, 492 negative slacks, two exact zeros, and local stationarity L2 `1.2095937956011798e-10`. Its largest relative violation is at row 26624, query index 13, left-RMS482, angle index 0. The corresponding original slack is `-1.7458257062230587e-14` and its original positive margin c is `0.0005926361018505633`.

The local radial repair factor is `0.999999999970527`. After full conditional recovery, the complete-vector repair factor is `0.9999999995717347`; the feasible segment parameter is 1 and the final composed repair factor is 1. These values identify the chosen direction as the recovered H candidate with the recorded repairs. It is not the heavily scaled C candidate, whose repair factor is `0.0012716447338104457`, or the raw-ray backup, whose factor is `4.2416560818870586e-5`.

After every repair and combination, the producer reevaluates the complete original A/AT/B/BT model. All 49,152 final linear slacks are finite and positive, with minimum `8.326672684688674e-17`, zero negative entries, and zero exact zeros. The saved final full stationarity L2 is `9.709373195833235e-5`; complementarity is `5.642183874230422e-12`. The best cross-evidence R267 lower readout is `43.40638896444804`, with saved gap `5.6274984672199935e-12` and distance bound `1.242535845391864e-8`.

These are ordinary floating-point posterior readouts, not validated enclosures or a proof of full QP optimality. They also do not certify nonlinear domain feasibility. The selector records that the global repair changed the conditional recovery, so the final direction is not called an exact exterior conditional optimum. The saved scaled-direction L2 is `0.001738835194805129`, weighted J-direction squared norm is `0.09367741974381358`, and damping penalty is `0.22041663714911905`; all are original report values, not local recomputations.

The local QP phase took `205.45696353399995` seconds. Its saved counters are 1543 local H actions, 512 local H inverse calls, 2063 local B actions, 1029 local BT actions, and 512 rows read. The helper time including original factor, condensation, QP and recovery is `262.92533747799996` seconds. The evidence does not require changing these budgets before addressing the nearest actual missing query.

## 5. Original complete-H and implementation readbacks

R270 retains the same 21 physical nodes and three controls and uses 212 reverse fronts, 512 local H solves, and one original full-chain recovery. Its saved peak RSS is `4696248` KiB. The condensation itself takes `24.788932515` seconds.

The original affine construction retains the original gradient: its saved linear-term error is L2 `7.160013625800203e-11` and Linf `5.820766091346741e-11`, against original g L2 `226700.1077110342`. It does not delete g by treating a computed center as an exact minimizer. The final recovered local mismatch is L2 `7.395553761742045e-17` and Linf `2.7853090283681565e-17`. The original full H residual is L2 `2.2803571679325582e-10`, relative `1.0070616734690292e-15`; the exterior gradient L2 is `2.2803370057142033e-10`. Same-vector supplied-versus-frozen original A and AT readbacks are both zero.

The actual condensation model identity is `51961711c7066195d9682335803e8c882a12beb9effb81cc4ad609b3d7784f35`. The B model identity is `656a644d77d438deb67f454a8c588ae9c05043570691072d6779300c92157fc3`. The original factor's `input_identity` is null; its `74234e98...` hash is the hash of that null value, not a unique model identity. The full chain QR factor remains in memory and was not exported for an independent file audit.

The original Actions implementation checks report B adjoint error `5.41044007575205e-18`, local/full action difference zero, and maximum original complex-chain relative discrepancy `9.904960962078049e-13`. The actual supplied direction is included in that check. The independent original nonlinear-collocation complex check saves `8.673617379884035e-19` on its stated direction scope: free inlet core and shared controls, with all interior physical direction coordinates zero. It does not independently check every interior physical column.

The three saved real full-residual direction diagnostics, at step sizes `1e-4`, `5e-5`, and `2.5e-5`, have relative discrepancies `8.271804781898352e-5`, `0.00017177743166718194`, and `0.00031068293317345567`. Their saved merit slopes are `-0.3269364456670587`, `-0.32693645863446363`, and `-0.32693646687675937`. These diagnostics are recorded with their actual scope and are not a new acceptance gate or a claim of monotone FD convergence.

## 6. Physical maximum component and new-warm FD

The read-only collocation observer again locates the largest physical component at interval461, radial mode1, state component1, frequency2 cosine, original residual row155819. Its signed value changes from `-0.00710855617496271` to `-0.007108516833554497`. Its original fixed model row weight is `199.03341577247605`, read from the original base weight array with raw SHA `9623d5a91f1f2a8ce05986ed20c60fb618572adcb93c02175bd76c8bfcef21f7`. The weight is not recomputed from trial midpoint RHS.

Interval461 is outside the selected B support, but its row and its full-H response remain in the complete residual/model. This is not a missing or zero-weight equation. A small model posterior readout and a positive aggregate merit decrease do not establish that this particular maximum component must decrease rapidly. No extra row-action or damping-cause calculation is made here.

The original boundary FD actually recomputes all original directions, perturbations and Richardson tests on the new warm, binding its exact compressed SHA and full producer. It saves maximum fourth-order relative error `1.006440735979892e-9`, second-order error `9.88343372199221e-6`, second-order contraction true, separated off-blocks zero, and implementation pass true under threshold `5e-5`.

Its reference is the completed actual T112 zero-height full Jacobian, anchor SHA `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51`, with configuration SHA `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5`, held explicitly affine. It does not use a ready linear proxy. The report explicitly says that the current H differs from the anchor, no nonlinear native solve at that H was performed, nonlinear DN was not evaluated, full BVP was not solved, and a full Cartesian closed surface was not produced.

## 7. New pair and exact primary-file scope

The new warm is:

```text
warm-001.json.gz: 4868398 bytes
565e2487317ffbc85560dd01efa2cfb4e479447d51a17216deb4ef61f55b4504
```

The paired original status is:

```text
driver-status.json: 2683314 bytes
e790e998ed6eebdc084546131e206dd4e5d723aebf7f92830b3153f82a25a8c0

driver-status.json.gz: 312135 bytes
aea13404a1cd1109f207cbb2a6f3c46fb885518ab7e29c480ba332ea21d756b6
```

The unchanged current schema is `exact-constraint-twenty-four-query-condensed-complete-H-warm-v1`. Both decoded status bytes and compressed transport bytes are bound; parent status is not reserialized to obtain its identity.

The [primary identity readback](2026-11-15-actual79-primary-identity-readback.json) verifies all 17 parent/report/publication relations, including the actual76 pair, whole producer subtree, new warm/status/FD binding, exact transparent JSON decompression, unchanged mesh, original unaccepted flags, accepted trial, and all five fetched original identities. All 62 distinct source hashes in the original current status and FD ledgers match the corresponding actual frozen local bytes.

The remaining original primary identities are:

| File | Original bytes | SHA256 |
|---|---:|---|
| model-000.json | 797264 | `66f99fcc91f07ad472fab3f0d7a65f2a30fdc12afabb75f3820a78cebf20f174` |
| condensed-QP-summary.json | 106477 | `d9f3f08fc44996a44ee462c3d8e83123a6f3868d60d17e32aeffcf09ea21c060` |
| decoded response-check.json | 1880630 | `3ede22cd04faab1a1b3868818a9455f3b33cd9b6cca3ae600bfcb2b48f0430c7` |
| response-check.json.gz | 231474 | `5e299c319b5e0281d637ab1ab5cb76a4cbbb9be370a5fa8147833ccfd95d7373` |

The [compact original readout](2026-11-15-actual79-original-readout.json) preserves all six actual trials and the selected optimization/recovery/FD/observer fields. The large B, condensed NPZ and raw-array payloads have not been independently audited in this primary note; an actual completed-artifact byte reader can report its precise payload scope separately without becoming a new scientific gate. Nothing here claims an independent full-factor byte audit.

## 8. Evidence-based successor

Continue from the new actual79 pair with one independent 25-query model that adds only **left RMS interval465**, retaining all 24 previous typed queries. This is 17 left RMS grids plus eight midpoint grids, each with 2048 angles: 51,200 rows. The complete B support becomes physical nodes465 through486 plus the three controls, with 7,439 local columns. The C baseline remains 4,059 columns, and the complete outside offset and full-H affine recovery remain present.

The reason is specific: the closest rejected step passes all existing modeled grids, original nodes/midpoints and merit decrease, while the complete original RMS pass identifies left465 alone. The quarter and eighth trials corroborate that same original query as a limitation. The farther midpoint487 failure is retained as evidence but is not added in this successor. There is no decrease or larger-step guarantee; the original nonlinear backtracking remains responsible for discovering any next limitation.

The successor preserves $\lambda=270$, 512 working rows, 200 dual sweeps, all original budgets, all 17 possible actual trial steps, every original full-domain and merit condition, and the real new-warm FD. It changes an algorithmic inequality model at a new accepted optimization warm, not the original mathematical BVP or its acceptance tolerances. This section records the next configuration, not a completed future run or an accepted final field.
