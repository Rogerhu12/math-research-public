# Actual request67 revision 2: same-base lambda27 tradeoff and complete saved-input byte comparison

**Classification:** numerical evidence and source/byte identities; not a theorem or an accepted coupled solution.  
**Author:** ChatGPT (`exact_refinement`).  
**Date:** 2026-11-14 UTC.

## 1. Result and comparison scope

The real request67 revision 2 completed one warm update and its new full boundary FD check. It used the same actual64 parent and the same twenty-query model as request66, with the single declared damping change from $270$ to $27$. The new accepted warm has SHA256 `efed68a084adf31fafa5c91ddda8747f9a2eac658072f87e28a839346b4bee4d`. Both `success` and `new_coupled_finite_acceptance` remain false.

The result has a concrete tradeoff. At its actually accepted step, lambda27 reduces the maximum physical collocation residual more than lambda270, while reducing the original fixed-weight nonlinear merit less. Both runs encounter the same nearest-rejected left-RMS query at interval 466. The lambda27 local QP also exhausts its 512-row and 200-dual-sweep budgets, and its final full stationarity diagnostic is large. These observations concern the directions actually obtained with the specified finite budgets. They do not rank the exact constrained minimizers of the two damped models.

All numerical values below are copied from the original Actions reports. The local work only parsed original JSON, retained its floating-point decimal lexemes as strings, and verified source/file/array bytes. It did not recompute a norm, matrix action, residual, ratio, difference, or rational expression. The complete copied readout is [actual67-same-base-original-scalars.json.gz](actual67-same-base-original-scalars.json.gz). The byte comparison is [actual67r2-byte-comparison/summary.json](actual67r2-byte-comparison/summary.json), with its complete detail in the same directory.

## 2. Actual public provenance

The successful run is [43652955632](https://github.com/Rogerhu12/math-research-public/actions/runs/43652955632), source commit `721edbfcacb28d6e7cfd4d139cc9bb6c939786b4`, job `132625243515`. The artifact is `14136747860`, named `visible-followup-condensedqp-43652955632-1`, size 578,920,426 bytes, ZIP SHA256 `7801971baf316cde64819b00b00a81528a5bf5bf28166f9192051de61d57db80`. Root downloaded and checked the complete ZIP, size, SHA256 and CRC before this readback.

The mathematical warm entry is the output-order-fixed source `geometry_20261114_twenty_query_lambda27_condensed_warm.py`, SHA256 `7de5e7d01efa9464e9c0d671c94d3b70a6e093dc1b3fd844944456ebb46fbbb5`. The FD source remains `8416bcb6ed57f1c2042032e22d1e637ed40fac0fbf0d676a6009b91f5535d9d9`; the read-only observer is `e75ba9319b72af4b3f329d870e3c4e7defa09ab165b7949f7974660db7891504`. Revision 1 stopped at the fresh-output-directory guard before the first residual evaluation; it did not supply a failed mathematical trial. Revision 2 changed that output ordering, not the finite equations or model budget.

The comparator is request66, run [43651436427](https://github.com/Rogerhu12/math-research-public/actions/runs/43651436427). Both runs bind the actual64 warm `3b25ea84dfababece99e1dc098d56cdcebd94737e428e509140e818d48e8eb1e` and status `037fb9eeaeb196f74976188efb9515736396f2c86a44fde4e93251e92ca01466`. Neither run uses the other run's newly updated warm as its base.

Primary request67 files are under `notes/public-actions-43652955632-1-condensedqp/twenty-lambda27-condensed-warm/`: `model-000.json`, `driver-status.json`, `condensed-QP-summary.json`, and `condensed-QP-result.json.gz`. The complete local artifact holds their original file bytes; the public publisher may gzip large JSON files. The complete QP result file has SHA256 `7ade925e0b537916b8b4b6848fdbfd309b1c84f74e385b33e39c1f112587f983`. Its FD report is the sibling `physical-response/response-check.json` in the artifact.

## 3. The original nonlinear comparison

Both runs start at the original fixed-weight merit `43.784169334438104`, physical collocation maximum `0.00710921522417158`, and full boundary maximum `3.1875470774840915e-08`. The original observer identifies the physical maximum as interval 461, radial mode 1, original residual row 155819, with frozen row weight `199.05303333486015` in both runs. That weight was read from the original returned weight array; it was not recomputed at the trial state.

| Original reported quantity | Request66, lambda270 | Request67r2, lambda27 |
|---|---:|---:|
| Accepted alpha | `0.0625` | `0.001953125` |
| Fixed-weight nonlinear merit after acceptance | `43.7556914034461` | `43.77799655333434` |
| Actual nonlinear merit reduction | `0.02847793099200402` | `0.00617278110376418` |
| Actual/predicted unregularized reduction | `0.9952185850982364` | `0.9998507258459568` |
| Physical collocation maximum | `0.007109134582008451` | `0.007108963566953459` |
| Full boundary maximum | `2.9883251941050535e-08` | `3.1813215460748086e-08` |
| Maximum relative FD error | `7.177173622085207e-10` | `7.082800792468702e-10` |

The physical maximum remains at the same interval/mode/row in both accepted states. Thus the smaller maximum in request67 is a real improvement in the previously identified worst row, not a change of the maximum's location. The original merit and boundary maximum favor request66 at the two actually accepted steps. No new percentage or inferred residual change was computed for this comparison.

These merit values use the same original fixed row weights and omit the damping penalty, as required by the original trial engine. The regularized model objectives have different lambda-dependent penalties and cannot by themselves provide this cross-run nonlinear comparison.

## 4. All original request67 trials and the shared nearest rejection

Request67 attempted ten of the original allowed seventeen trials and accepted the tenth. The first four trials fail the original midpoint domain before a complete finite merit is available. At every later trial the complete merit decreases, but the original RMS-query domain independently rejects the next five.

| Trial index | Alpha | Original fixed-weight merit | Actual merit reduction | Original blocking outcome |
|---|---:|---:|---:|---|
| 0 | `1.0` | not reported | not reported | 14 midpoint failures |
| 1 | `0.5` | not reported | not reported | 14 midpoint failures |
| 2 | `0.25` | not reported | not reported | 13 midpoint failures |
| 3 | `0.125` | not reported | not reported | 5 midpoint failures |
| 4 | `0.0625` | `43.58804786277434` | `0.1961214716637656` | left-RMS 463, 464, 465, 466 |
| 5 | `0.03125` | `43.68613610579595` | `0.09803322864215147` | left-RMS 464, 466 |
| 6 | `0.015625` | `43.73496979038097` | `0.04919954405713156` | left-RMS 465, 466 |
| 7 | `0.0078125` | `43.759518179520846` | `0.02465115491725811` | left-RMS 466 |
| 8 | `0.00390625` | `43.77183048836491` | `0.01233884607319169` | left-RMS 466 |
| 9 | `0.001953125` | `43.77799655333434` | `0.00617278110376418` | accepted warm |

At trials 4 through 9, the original reports show no invalid nodes or midpoints, finite boundary values, the unchanged uniform-phi rho guard passing, and no right-RMS failure among its 698 queries. All twenty modeled angular grids at those trials have 2048 finite values with zero negative and zero zero values. This last fact is copied from each original per-query count. It does not claim continuous-angle positivity or positivity at the additional original RMS queries.

The nearest rejected request67 trial, alpha `0.00390625`, has exactly one original RMS failure:

- interval 466, left-RMS fraction `0.17267316464601146`;
- station `1.1653164835060832`, bracket `[1.1644558024915952, 1.169440253991355]`;
- original minimum beta squared `-0.6553113450571904`, at phi `0.0`;
- original curvature there `0.0403167692244389`;
- scalar values `a=1.1936602539168486`, `ap=-0.06191648616754137`, `app=-2.4952033343255122`.

Request66's nearest rejected alpha `0.125` fails at exactly that same original interval/fraction/station and phi. Its reported minimum beta squared is `-0.6545364759053149`, curvature `0.040326208896638`; its merit also decreased and its twenty modeled grids were valid. The two minima belong to different trial states and directions. Their shared location supports putting this actual omitted query into the next finite model, without claiming that the resulting model will settle the full nonlinear domain.

The accepted request67 trial passes both original 698-point RMS query families, the original nodes/midpoints, the complete boundary, and the uniform-phi rho guard. The constant collocation and left residual maxima remain `0.0`. This is one domain-valid, merit-decreasing warm update, not a full finite BVP or native acceptance.

## 5. The obtained local QP is not an accurate optimal lambda27 comparison

The same-model selector chooses the R270 condensed complete-H candidate. At lambda27 its original reported objective is `42.017186305525534`, versus `43.7838809339076` for its own C candidate. The selected full direction has `gdot=-3.1621954192288535` and damped model decrease `1.766983028912524`. Its final original 40,960 linear slacks are finite, with minimum `1.454392162258955e-14`, zero negative entries and zero zero entries.

Nevertheless, the local QP stops at `maximum-working-row-budget`, using 512 rows. Its last local stage is 511 and its dual stop is `maximum-dual-sweeps`, with 200 sweeps. The last coordinate update is `1.2591190664545948e-06`, normalized working minimum slack `-7.610177327616041e-07`, and normalized complementarity `7.077624477295508e-07`. The saved unrepaired stage has a minimum original slack `-0.10516133388980048`; subsequent local repair and actual complete recovery/selection produce the final feasible full vector.

The final original full stationarity L2 is `1788.5803704212726`, complementarity `0.00212618641119642`. The R267 lower-bound diagnostic is `-2152.0999888906913`, final gap `2194.117175196217`, distance diagnostic `2.4534722044231803`. These are ordinary floating calculations, not outward enclosures. They do not certify optimality. By comparison, request66 reports original stationarity `3.6856250700402916e-05`, complementarity `1.008075226124556e-12`, and gap `1.0160761121369433e-12`.

It would therefore be unsupported to infer that the exact lambda27 constrained model inherently has the observed small allowable nonlinear step or that lowering lambda is uniformly harmful. The available evidence is the finite-budget direction, its repaired feasibility, and the real nonlinear trials. The original real merit and domain checks remain decisive; none of the posterior diagnostics was added as an acceptance gate.

## 6. Complete square-root and recovery precision actually reported

The complete chain QR binds all 236,036 unknowns, 698 physical nodes of width 338, 109 free core coordinates and three scalar controls. It completed all 698 fronts with lambda27, preserving the full affine/global terms. The factor report records memory-only storage, 1,486,451,296 factor bytes, time `18.804274265000004` seconds and maximum RSS `3446972` KiB. There are no exported complete chain-factor payloads to byte-audit independently.

The local condensation retains nodes 467 through 486 and the three controls, dimension 6763, including the explicitly zero B layout at node 484. It completes 212 reverse fronts in `15.109767109000018` seconds. Its original local-root diagonal range is `27.000428995642736` to `1028.8582255837805`; its local-center gradient L2 is `3.8244402154763764e-11`. The complete original $g=A^T b$ remains part of the affine problem.

The actual recovery report gives:

| Reported diagnostic | Original value |
|---|---:|
| Actual recovered local mismatch L2 | `4.904752650674095e-15` |
| Actual recovered local mismatch Linf | `1.4229679175421783e-15` |
| Original exterior-gradient L2 | `1.7591268796175806e-09` |
| Original complete H residual L2 | `1.7593220902797898e-09` |
| Original complete H residual Linf | `1.284377049159957e-09` |
| Original right-hand-side L2 | `398833.3525974009` |
| Original relative H residual | `4.41117092846476e-15` |

The live-A/frozen-reference A and transpose actions report zero difference. These ordinary floating diagnostics distinguish the accurately recovered full response from the much larger final inequality stationarity diagnostic. They are not bounds on all floating errors, and they do not certify the exact local QP solution or the nonlinear BVP.

## 7. Complete available-payload byte comparison with request66

The comparison reuses the already completed request66 verification receipt `verified66-baseline.json.gz`, SHA256 `74cb59651a3908ba2dea664775ff76fde2bcb9f7e268579d4c80c366f5bca6aa`, and verifies request67 against its own manifest/source/parent identities. It completes successfully:

- All 181 domain NPZ files and 1,168 contained arrays have their original file and raw identities verified. The complete exported B rows, query Gamma/Pi maps, local endpoint-J/P arrays and base representations compare identically with request66.
- The complete exported original b, g and inequality c payloads compare identically. Base identity, query specifications and scientific binding records agree.
- The original Actions-reported complete A-input identities agree, including the row weights/chart/scalar and global operator data. The full global L/R/P payloads were not exported, so this statement is an equality of their recorded identities, not an independent re-audit of unavailable global arrays.
- Even the complete B metadata model SHA happens to agree: `e6928853c2a125212dc4909a3b2fefada07e7320d23ee0d4817634afec89d511`. In general provenance metadata changes alone would not imply a changed scientific array.
- C changes as intended, from raw identity `2289c3e807976f929f3fd5a80d0f7a7a69ff5b736443032c2449eda52b6616e2` to `20b051d5189ff01597e39cea347a6afe6918281fff8051a12e32e81204f98ab0`. All fourteen exported new condensed-root raw arrays are independently hashed. Neither the old C nor the old local root is relabeled as a lambda27 object.

The complete byte detail is 160,429 bytes compressed, SHA256 `be6993f3e2b71c8d45c8980914f0f3db75fcd93cec3a7d4f67355b324bdad1b7`. The reader explicitly records that it imported no scientific package and computed no norm, matrix action, or Fraction. This supplemental audit creates no additional acceptance condition.

## 8. Consequence for the next controlled experiment

The current evidence preserves both aspects of the lambda27 tradeoff: improved worst physical residual and reduced accepted total merit progress. It also identifies the same omitted left-RMS 466 query in both directions, while exposing incomplete lambda27 inequality optimization. A subsequent twenty-one-query lambda27 comparison against the matching lambda270 run can therefore use their same actual66 parent, add that common query in both models, rebuild C/QR/local roots for each explicit damping, and preserve every original nonlinear trial. It must not start lambda27 from request67's updated warm and call that a same-base comparison. No success or precise QP optimality is predicted for that experiment.
