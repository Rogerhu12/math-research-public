# Public Actions free3: accepted 0.996 and 0.9975; 0.997875 failed

Evidence: [public run 43582043166](https://github.com/Rogerhu12/math-research-public/actions/runs/43582043166), source commit `8fa6b3f3b5365bfffd674cdc04f7d77519fa0d76`, artifact `visible-mainline-free3-43582043166-1` (artifact id `14109068159`). The complete 62-file artifact is archived, byte-for-byte, in `public-actions-43582043166-1-free3/`. All numerical values below are returned Actions data; this note does not rerun a solver locally.

The run retained two newly accepted finite open prefixes before its final failure. Its terminal nonzero exit does not invalidate those earlier accepted files. The authoritative latest accepted file is `attempt-03/run/stage-00/actual.json.gz`, with endpoint 0.9975. The final attempted file, `attempt-06/run/stage-00/actual.json.gz`, is **not accepted**.

## Accepted and failed solver calls

All calls used complete M96 / angular 1024 data, fixed core modes 1 through 3, free modes 4 through 96, the original 93-row principal normal projector, RMS tolerance `1e-6`, boundary tolerance `1e-11`, and mesh budget 900. No threshold was changed.

| Attempt | End | Accepted | Nodes | Maximum collocation RMS | Maximum BC residual | Solver seconds |
| --- | ---: | --- | ---: | ---: | ---: | ---: |
| 00 | 0.996 | True | 430 | 5.45702302622e-07 | 3.46944695195e-18 | 65.053914 |
| 03 | 0.9975 | True | 432 | 7.01923146597e-07 | 1.08420217249e-19 | 79.819132 |
| 06 | 0.997875 | False | 688 | 1.03996492904e-05 | 8.67361737988e-19 | 817.300747 |

The actual attempt sequence is:

| Attempt | Start | Duration | Outcome |
| --- | ---: | ---: | --- |
| 00 | 0.990 | 0.006 | Accepted finite BVP and physical quintic readout |
| 01 | 0.996 | 0.006 | Taylor-predicted principal elliptic projector failed before Newton |
| 02 | 0.996 | 0.003 | Same preparation guard failed before Newton |
| 03 | 0.996 | 0.0015 | Accepted finite BVP and physical quintic readout |
| 04 | 0.9975 | 0.0015 | Taylor-predicted principal elliptic projector failed before Newton |
| 05 | 0.9975 | 0.00075 | Same preparation guard failed before Newton |
| 06 | 0.9975 | 0.000375 | Preparation passed; actual nonlinear solve failed its RMS / mesh acceptance |

Only the four preparation failures triggered step halving. Each reports the unchanged guard `Principal elliptic boundary requires strictly positive sampled det II and nonzero II_phi_phi`. The adaptive driver stopped on the final genuine nonlinear failure with phase `actual-solver-or-readout-not-accepted`, `accepted_stages=2`, `latest_accepted_end=0.9974999999999999`, `returncode=2`. It did not call the last file accepted or replace the accepted checkpoint by it.

## Physical C2 and complete-core readouts

Both accepted outputs have the original physical quintic readouts at (angular, radial subdivision) `(1024,2)` and `(2048,4)`. These are sampled results, not continuous metric or embedded-surface certificates.

| Accepted end | Material metric error, both levels | Curvature sample, fine level | Reflected prefix diameter sample | Exact complete-core lower bound for rho | Exact core gap enclosure |
| --- | ---: | ---: | ---: | ---: | --- |
| 0.996 | 4.605340642616085e-6 | 6.301227852244267 | 3.507786606875019 | > 0.162553786500455621371135 | (0.960001844711965818778851, 0.960001844711965818778852) |
| 0.9975 | 8.086619004088469e-6 | 6.301149487839376 | 3.5096383977213543 | > 0.159219002481429886307628 | (0.960001948326721801244854, 0.960001948326721801244855) |

The R237-style certificates use every one of the 96 binary64 core coefficients as exact rationals. Both certify the finite planar core's strict convexity, the material-circle diffeomorphism, and the axis witness gap. Neither certifies the continued prefix ball exclusion, a closed surface, reach, or the whole material metric.

The accepted finite BVP residual and the sampled material metric error measure different things. In particular the material error has grown relative to the 0.990 seed; the accepted status must not be represented as an exact isometric annulus. Attempt 03's log includes a Newton backtracking failure after its first correction, but the outer solver subsequently accepted its actual RMS `7.019231465972388e-7` and BC `1.0842021724855044e-19` under the unchanged gates. Both facts are retained.

## What caused the final failure

At attempt 06 the principal projector was actually constructed, with sampled `det II` minimum `0.02929451113852875`, `II_phi_phi` minimum `0.05287803726216113`, and normalized projector-row condition `4002.5310110452165`. Therefore this last failure is not another failed preparation.

The separated shooting reduction was much more ill-conditioned than in either accepted step: its reduced condition was about `6.714e3` at 0.996 and `1.165e4` at 0.9975, but `4.816e6` at the start of attempt 06 and then about `5.995e7` after its first correction. Subsequent mesh refinements did not remove the Newton backtracking failures. It refined through 433, 434, 436, 440, 448, 464, 496, 560 and 688 nodes. At the last mesh the outer code requested another 256 nodes, exceeding the budget 900, and returned status 1. The final RMS remained `1.0399649290374451e-5`; the BC residual alone was small. Thus simply treating the error as a missing projector or silently raising acceptance tolerance would be incorrect. A larger mesh budget alone has no demonstrated cure for this conditioning / failed-correction mechanism.

The final record is preserved as a failed checkpoint, useful for diagnosing this normal-boundary continuation branch. It is not a physical tail cut: its radius is about 1.169 and its scalar derivative is still positive. The complete physical-cut nonlinear tail-DN boundary work remains the primary different boundary formulation. No tail DN, closed-surface assembly, fixed-metric frequency refinement, reach certificate, or full completion claim follows from these three finite solves.

## SHA256 of original artifact evidence

- `attempt-00/run/stage-00/actual.json.gz`: `82eb5f704d1d2e996f100ad87f4dfcfe860d615d7072eeef00a1b8fb08e99303`
- `attempt-00/run/stage-00/core-certificate.json`: `15a0f18e1f8a1e41fc2a7367977f0064bbbfc5eb883cf6000b0a5390b8b3bc7a`
- `attempt-00/run/stage-00/material-quintic.json`: `8b80d47ce8c7f7261078f278d0353788f3bb5ebce71554be45704e4a65f627a2`
- `attempt-00/run/stage-00/prepare.log`: `299173036dd611e89b9c7cb4059326dcb20ba5c3d1d6ccc06e4074837c1b32b9`
- `attempt-00/run/stage-00/run.log`: `a396fe2d48d5594c76e0c862a6a40100ca57044de32c1343e4145ce48ea17888`
- `attempt-03/run/stage-00/actual.json.gz`: `a6a278d0b435b5587bbbc2ec6c93b50c74da80dae51708c6d4461d67033430ef`
- `attempt-03/run/stage-00/core-certificate.json`: `1c419c910f3dc7a05e02476b582fab7a9d96e260af74f121878ae0aa9dc41032`
- `attempt-03/run/stage-00/material-quintic.json`: `0607ccac59fa4d73577c19626954cbc2e0e2971da2834d1cff53c43f4981c5ee`
- `attempt-03/run/stage-00/prepare.log`: `0273730d967047c16fc71bc0eb63c5ad16343b86f395afcb651dff140ceb8eee`
- `attempt-03/run/stage-00/run.log`: `4098170c407f9a81c9ca2a5bf1f8663d534f8570de4077294e097e9647257d54`
- `attempt-06/run/stage-00/actual.json.gz`: `5632bed61e232cb0b62e42548dea19054e7c9fd63f0faf4e6433b6fc73b93a67`
- `attempt-06/run/stage-00/prepare.log`: `3952676831f59278179ba459647c836ccff24b661537bb63dfd039c3390a3868`
- `attempt-06/run/stage-00/run.log`: `11dedb168bad6a01232939ed9ad2f3f3e24ba93e50bcbf112e440d84ee4190fe`
