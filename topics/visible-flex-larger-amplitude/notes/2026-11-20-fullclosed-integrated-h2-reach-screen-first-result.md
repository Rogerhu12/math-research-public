# Complete H2 direction with the reflected-body necessary geometric screen

Date: 2026-11-20. Actual complete-space continuation by /root/fullclosed_solver.

## Genuine parent and corrected geometric condition

The parent is the actually computed 63-dimensional physical candidate, SHA256 `af89a4414fb0cee35d75dba5530e9b45b62abd248ddf7509cca92c2a9696a505`. It has complete Frobenius SSE6430.55548312496, maximal relative Gram error .586426369922, and sampled maximum absolute principal curvature7.211250722623923.

The closed model contains the upper sheet, its reflection across z=0, and flat disks at +/-H. Together with pi angular symmetry, every active body point F has the point -F. Consequently 2*max_sample|F| is a lower bound on the complete body's diameter. For the declared axial phase family the actual point pairs survive and their radius is preserved; this supplies a lower bound on the reference F0 diameter D0. It is not a substitution of arbitrary current Ft diameter for D0. The support constant also gives D0>=2 and the caps give D0>=2|H|.

The source uses D_lb=max(2,2|H|,2*max_sample|F|) and imposes the numerical point screen .03*D_lb*K_sample<=.98 during the nonlinear trial selection. The factor .98 is a declared numerical margin. This is only a necessary screen, not a continuous curvature bound or reach certificate. A different family must establish its reference diameter relation separately.

The exact position formula and reflected-body argument were read from `scripts/read_closed_residual_spectrum_20261120.py`. The solver obtains F from the already evaluated actual six jets, retaining all current node/midpoint and angular points. The diagnostic source SHA256 is recorded in the raw report.

The initial readout matches the independent diagnostic: D_lb=4.0693862363269195, K=7.211250722623923, product=.8803609331204504. The corresponding initial numerical curvature cap is8.02741857606321. Thus this real parent, unlike the previously attempted m6/r5 parent, is not excluded by the declared necessary point screen.

## Complete coordinate and solver specification

All original free variables, every A/E/D defect, every original angle-value Gram row, and the complete endpoint projection are retained. The H2-type scale and same-norm coarse whitening are the previously documented ones, with the rigorous norm equivalence and whitening bound in R654. This run enlarges only the redundant physical coarse space to low_modes=12 and eleven radial centers, giving1280 columns. The original complete DoubleIntegrated directions remain, so this is not a restricted physical fit.

The requested centers are .3, .6, .8275, 1.0570671854957785, 1.1975374839662283, 1.3580749679324564, 1.5587468228902417, 1.759418677848027, 1.9600905328058122, 2.140695202267819, and2.26109831524249. The basis uses the nearest original nodes, recorded in the report. No mesh or prescribed metric changes.

One BLAS thread, one declared direction, up to256 LSMR iterations, mu=.005, atol=btol=1e-6; original Frobenius and full-angle normalization. Exact nonlinear half-step trials require the original metric descent and positivity conditions as well as the new necessary point screen. The initial parent is checked before spending a linear budget.

## Actual first direction

The 256-iteration LSMR solve returns stop7 (the declared inner budget). Its full nonlinear alpha=1 trial passes all declared numerical conditions on the first attempt.

| Quantity | Actual parent | Actual accepted full step |
|---|---:|---:|
| Complete Frobenius SSE | 6430.55548312496 | 1277.0304067322386 |
| Maximum relative Gram | .586426369922 | .33329462549082134 |
| Maximum sampled absolute principal curvature | 7.211250722623923 | 7.958664294054591 |
| Reflected-body diameter point lower bound | 4.0693862363269195 | 4.065057941959583 |
| Necessary reach product .03 D_lb K | .8803609331204504 | .9705729448781031 |
| H | 1.9392157715615652 | 1.939617501351516 |

The accepted dynamic numerical curvature cap is8.03596581723495. The minimum relative metric determinant is .8076489645333614, relative E minimum .8107419620205435, rho minimum .1659647847694956, and the existing simple angular Lipschitz rho lower estimate .1381315578040358.

The accepted metric worst point is s=1.2477054477056746, phi=pi/2. The curvature worst point is s=1.01275, phi=.04908738521234052. The radius maximum giving D_lb occurs at s=2.291199093486158, phi=.923456434307156. The area minimum is .09372598587004956. All curvature and radius values are actual common-quintic point values at946,485 representative points, covering3,778,560 complete angular orbit points.

The normalized objective decreases from .0017018534794008711 to .000337967481456491. Its linear full-step prediction is .00024629077789352057; half-objective directional derivative is -.0013430295841638368; actual-to-predicted decrease ratio is .9370163143999005.

Max absolute nodal delta Y/U/A are .016354135160528787, .10858138356267821, and .8835789480419767. Delta H is .0004017297899507486. The literal projected endpoint residual is2.293087594806842e-17. LSMR diagnostics: normr=.016873691977036028, normar=.00014428255217970352, normA=40.242564043549095, condA=26.65659806246972, normx=1.2398500399853105. The complete direction, line search and accepted geometric readout take83.9885198030006 seconds.

## Identity and continuation status

Complete source: `scripts/resume_20261120/fullclosed_integrated_h2_lm_v3.py`, SHA256 `9283403609c185dfcaa9de70038cc98d89618d99e3200a7cfd519f0af650e3d1`. The earlier unexecuted v3 preparation SHA25f8... was revised to include the actual 2*max_sample|F| diameter readout before this first execution; it is not the executed source. The v1/v2 sources and earlier actual or partial runs remain separate.

Accepted/final NPZ SHA256: `e8b2ca40e184157abba15c3c85ebdd651e38cbb4035edb2cfd652c8b57ad0637`.
Direction NPZ SHA256: `1529853ad0ba032a0a207d1e9206df8c76790f2c6013c0ea32096970b2e6cf78`.
All raw arrays and full reports remain outside Git.

Reproduction follows the source defaults for the unchanged operator and H2 dependencies, with `--coarse-source .../scripts/resume_20261120_physical_subspace_v3.py`, `--low-modes12`, the eleven comma-separated `--coarse-centers` above, `--reach-ratio .03 --reach-safety-factor .98 --max-directions1 --maxiter256 --damping .005`, and the genuine af89... parent. All paths and dependency SHA256 values are recorded by role in the work-only report.

The sampled metric target remains false. The current point is close to the necessary curvature-screen boundary, so the next correction should account for active geometry constraints rather than interpret small backtracked metric-only steps as completion. No continuous metric, reach, all-t family, held/E3, or fixed-g refinement certificate is claimed.
