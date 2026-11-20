# H2-type continuation: three metric steps cross the necessary curvature limit

Date: 2026-11-20. Actual complete-space numerical continuation by /root/fullclosed_solver.

This is the already-started three-direction continuation of the first successful H2-type direction, with genuine parent SHA256 `16a0ba1d8e08b9c6e5023179af34b9e728527b204a3ed9849c514cadd2e8dfba`. It uses the unchanged complete source `scripts/resume_20261120/fullclosed_integrated_h2_lm.py`, SHA256 `861a9de1a1ae9859cae0adcc813de3f4f76d656c7f9e48821b3069ec483f02c6`.

The original metric equations, all free variables and A/E/D coordinates, exact-model endpoint projection, and 173 physical directions whitened in the same H2-type norm are retained. This batch uses three directions, 256 maximum inner iterations each, atol=btol=1e-6, and initial mu=.005. The unchanged rule halves damping after a full step whose actual-to-predicted decrease exceeds .75. All three directions reach the inner budget (LSMR stop 7), and all accept alpha=1 by the original metric and sampled positivity line search. This source version does not impose a sampled curvature cap.

| State | mu | Complete Frobenius SSE | Max relative Gram | Max sampled absolute principal curvature |
|---|---:|---:|---:|---:|
| Real parent | — | 492.20269298748 | .22964195543170085 | 13.234204952480813 |
| Direction 0 | .005 | 298.9173756463267 | .1836468070438757 | 15.01946666166532 |
| Direction 1 | .0025 | 221.3902581604458 | .152251323486025 | 16.308541846993847 |
| Direction 2 | .00125 | 194.07587774292625 | .149256286181628 | 17.481029835512427 |

Maximum absolute nodal delta A is respectively .15971318029454123, .12881269905265078, and .05397554353113471. Literal projected endpoint errors are 4.118274189550408e-18, 2.07014852308951e-18, and 1.229891839413244e-18. The direction/line-search/curvature readout times are 83.7630372120002, 89.22842604799916, and 76.7329059069998 seconds.

## Geometric consequence and parent choice

The theorem's D is the diameter of the reference family member F0, not the diameter of each current Ft. The fixed support-function constant and pi symmetry of this family's core give the common necessary lower bound D>=2. A surface with reach at least .03D therefore must satisfy |principal curvature|<=1/(.03D)<=50/3. The final ordinary sampled curvature value 17.481 exceeds this necessary threshold. These floating-point point values are a numerical infeasibility diagnostic, not an interval-certified curvature theorem; nevertheless the final child must not be promoted as a reach improvement.

This result shows that controlling the H2-type *increment norm* does not by itself enforce a curvature limit on the *current surface*. The final metric residual improves while curvature increases over successive steps. The data are retained as actual metric-only accepted states; no reach, continuous metric, closed isometry, all-t, held/E3, or fixed-g refinement conclusion is claimed.

A separate next batch was started from the lower-curvature m6/r5 physical parent (not this final child), with an explicit sampled curvature cap of 16, the m12/r11 coarse space of 1280 columns, and all original DoubleIntegrated directions. The cap is a numerical trial-selection choice leaving margin below 50/3, not a continuous reach certificate. Its actual result must be recorded separately.

## Reproduction and actual identities

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python topics/visible-flex-larger-amplitude/scripts/resume_20261120/fullclosed_integrated_h2_lm.py --repo . --bundle /path/to/integrated-h2-first/final.npz --outdir /path/to/new/integrated-h2-next-three --max-directions 3 --maxiter 256 --damping .005
```

The three accepted NPZ SHA256 identities are:

- Direction 0: `02f52d2971a5adc575de4da64359e207c5c0b7c13083527f20cd1397956b6afc`.
- Direction 1: `d1f098c8551b7c4fbc2eb85ee46f43d2f79b51950ad54a3ced77159b7657fcf9`.
- Direction 2 and final: `3f902daa316e8f124ae34bc662ec3cb1abc5b5aea1ba1987b321710de85ac7e8`.

Raw report, directions and states remain in work-only storage; these hashes identify actual generated files, not an externally retrievable lost parent. The sampled metric target remains false.
