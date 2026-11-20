# Targeted radial enrichment and an actual p8 geometry restoration

Execution location: the completed numerical runs below were local terminal runs, with no GitHub Actions run ID. This execution deviation and the change to public Actions are recorded in [the correction note](2026-11-20-public-actions-execution-correction.md).

Date: 2026-11-20 UTC. Both experiments in this note use the same frozen
[v7 source](../scripts/resume_20261120_curvature_qp_v7_spectral_hessian.py)
and [R664 positive residual Hessian](../results/R664-positive-spectral-residual-Hessian-and-true-gradient-pullback.md).
They retain true p8 Phi with epsilon=0.001 and scale=0.05, the fixed scalar
metric and core support coefficients, all 7,377 radial observations and
N=2048 angular rows, the original affine ports, and the final numerical
geometry screen 0.992. The first experiment enlarges only the physical
radial search space. Its final known-point screen failed. The second
experiment explicitly restores that same margin without changing the
objective or relaxing a geometric gate.

## 1. Why these radial columns were added

The actual 077087 field in the
[preceding four-direction result](2026-11-20-curvature-qp-spectral-hessian-four-step-result.md)
still has metric peaks near s=1.096524 and s=0.997471. All 17 existing radial
centers and 12 angular modes were retained. Five additional existing mesh
nodes were selected:

| Requested center | Actual mesh node | Actual coordinate |
|---|---:|---:|
| 0.99 | 481 | 0.99 |
| 0.995 | 498 | 0.995 |
| 1.0 | 818 | 1.0 |
| 1.02 | 823 | 1.0195 |
| 1.097 | 833 | 1.0972015564873356 |

Each adds the existing position, velocity, and acceleration cardinal
columns for the same 38 angular channels. The physical dimension therefore
increases from 1,964 to 2,534. The underlying complete model still has
1,332,245 free coordinates; these coarse experiments are a restricted
search in its original affine space. No angular field coefficient, metric
row, scalar oracle value, or endpoint condition is removed.

The positive integrated physical norm is the restriction of the same v5/v7
norm to the enlarged space. Its normalized matrix condition estimate is
808955898.6848406, its diagonal normalization spans 0.02962619358260714 to
397249.33288611955, and its separated-to-literal energy check differs by
2.112557267108805e-15. The increased conditioning is reported explicitly.
The new original-Jv quadratic check below also succeeds; neither diagnostic
is an outward certificate.

## 2. First r22 batch: genuine metric improvement, final screen false

The first batch declares six directions, starting at 077087 with
mu=0.0019301197463913783. It takes 283.776178158 seconds and evaluates 21
actual nonlinear trials. Five directions have accepted fields; the sixth
has no accepted trial among its 12 backtracks.

| Direction | mu used | Accepted alpha | Phi after | Max Gram after | Known product at acceptance |
|---|---:|---:|---:|---:|---:|
| 1 | 0.0019301197463913783 | 1/2 | 1.674467403654608e-7 | 0.014386153593399342 | 0.9917995785978043 |
| 2 | 0.0019301197463913783 | 1/2 | 1.5761251922454412e-7 | 0.014009354792815731 | 0.9917994427213914 |
| 3 | 0.0019301197463913783 | 1 | 1.441572909461266e-7 | 0.013712100530398633 | 0.9918244023431956 |
| 4 | 0.0009650598731956891 | 1/4 | 1.379253877814557e-7 | 0.013633939180940646 | 0.9918182234587922 |
| 5 | 0.0009650598731956891 | 1 | 1.192714730154522e-7 | 0.013342898586344592 | 0.9918179685269672 |
| 6 | 0.00048252993659784457 | none | unchanged | unchanged | final recheck 0.992401641076606 |

Every rejected trial in this batch decreased actual Phi but failed the
numerical geometry screen. The accepted model ratios range from
1.0012005217 to 1.0158689153. Thus the new objective model is informative
here, while geometry remains an active constraint.

A newly refined positive-curvature basin in cell 821, at
u=0.13182023373669122 and phi=0.43591193437744524, reveals
K=8.075084383534215 in the otherwise unchanged fifth accepted field.
Together with D_lb=4.096558392628885, it gives the final product
0.992401641076606. The returned final bundle bede53ea therefore has
`final_known_point_safety_pass=false`. It is **not** promoted as a
0.992-qualified parent. This value is below the bare necessary threshold 1;
the finding is a failure of the declared numerical margin, not a proof
that the actual reach requirement fails.

This is a newly exposed local extremum, not deliberate deletion of a
previously paid witness. The original protected basins and persistent
fixed locations were retained. The observer's finite/local scope is still
limited: a local peak can become visible at a later field or refinement.
The new peak is made a permanent priority seed in the next experiment.

In the sixth direction, the full step has actual Phi 9.583813742697043e-8
but known product 1.0072214756059892. The half and quarter steps give
0.9974908878584402 and 0.9926237439402804. Smaller steps approach the
ineligible parent; the final alpha=1/2048 still gives
0.9924015663380582. Shrinking toward a parent outside the chosen margin
cannot by itself restore that margin. The actual QP already has 56 negative
linear bounds and uses the general repair; it never assumes the zero step
is feasible.

The enlarged-space checks compare the actual complete operator with the
new separated assembly:

| New r22 check | Relative difference |
|---|---:|
| Exact residual-Hessian quadratic versus original Jv | 5.320066768835291e-15 |
| True Phi gradient versus complex polynomial derivative | 2.344979260913562e-13 |
| Actual Phi versus coarse evaluator | 1.7454327410973126e-15 |

The failed sixth direction increases mu by ten, giving the recorded next
value 0.004825299365978445.

## 3. Same-objective restoration: two actual full accepted steps

The second experiment starts from the actual bede53ea bundle. It keeps all
r22 columns and all previous positions, adds the new cell-821 basin as the
eighth protected local seed, and uses local-refine=10. Its initial
`initial_restore_required` flag is true. The numerical screen remains
0.992 and the linear safety margin remains 0.0002. Phi descent is still
required; no feasibility-only or nonmonotone objective is substituted.

Three directions and 14 actual trials take 156.232240657 seconds:

| Restoration direction | mu used | Outcome | True Phi after | Known product after |
|---|---:|---|---:|---:|
| 1 | 0.004825299365978445 | all 12 trials rejected | 1.192714730154522e-7 | still outside margin |
| 2 | 0.04825299365978446 | full step accepted | 1.1926426160927617e-7 | 0.9917999986972358 |
| 3 | 0.02412649682989223 | full step accepted | 1.1923035857631737e-7 | 0.9918918984053476 |

The first restoration full step reduces Phi but gives product
0.9925842020709303 at the known low-phi cell-821 basin. Its half step gives
0.9921008229215164 at the newly protected phi≈0.435912 basin. All smaller
steps also fail the screen. Increasing the positive norm penalty yields a
different actual direction; it does not accept one of those rejected
fields.

The second direction has 101 negative linear bounds, and its full step
passes actual geometry with a Phi decrease of 7.211406176020846e-12. Its
actual/model decrease ratio is 0.9997561323384487. The third direction has
no negative bounds and takes another full step, with ratio
1.0000426080835854. The three QPs have 1408, 1441, and 1452 rows and
explicitly negative final maximum unscaled linear violations.

The final output 35f74961 has `final_known_point_safety_pass=true`. The
final local re-evaluation gives K=8.070936772956372 at cell 289,
u=0.5290121805813988, phi=0.7022676402048246, s=0.6988225304514535.
The largest known radius gives D_lb=4.096558331489566 at cell 881, u=0,
phi=0.419041163064. Their final product is 0.9918918984053982.
The run's final screen reads 971 fixed/current arbitrary positions plus
the complete Gauss/grid set and local searches. The exported all-history
handoff includes additional paid search locations; consumers must reread
that larger list at their own exact parent.

## 4. State comparison and norm units

| Quantity | Initial 077087 | r22 bede53ea, failed final margin | Restored 35f74961 |
|---|---:|---:|---:|
| True Phi | 1.8198200809540876e-7 | 1.192714730154522e-7 | 1.1923035857631737e-7 |
| Maximum sampled Gram norm | 0.01495643901349162 | 0.013342898586344592 | 0.013343526276563303 |
| Old positive radial Jw | 0.20418344137988473 | 0.1965553862223486 | 0.19654005323887383 |
| All raw quadratic sum | 754.3946753556374 | 671.7162632622396 | 671.7092342682915 |
| Legacy raw quadratic sum | 188.71193594730013 | 168.0365560380149 | 168.03479015845517 |
| Minimum sampled relative Gram determinant | 0.979849823470919 | 0.9815219316201177 | 0.9815235525282252 |
| H | 1.8782497136899416 | 1.8777133385127733 | 1.8777124287284133 |
| Final finite margin flag | true | false | true |

The small maximum-error increase during restoration is recorded. The final
true Phi is still lower; this is not a retrospective replacement of one
objective by another.

The equation used in both batches is

$$
\left(\frac{1600}{C_0}H_L+\mu^2G\right)p
 =-\frac{1600}{C_0}g_K,
\qquad C_0=4856.422137302683,
$$

with the finite inequalities added by the QP. At the first restoration
mu, the mean-Phi coefficient of G is 2.3283513971311987e-5, and multiplying
the equation by C0 gives 0.11307457268447585 G alongside 1600 H_L.
The final recorded next mu is 0.012063248414946114, whose corresponding
mean and raw coefficients are 0.00014552196232069995 and
0.7067160792779741. These are not the earlier v5 coefficient
0.03035263835814177, nor a claim that a different complete-space
preconditioner has the same norm.

Both batches keep the exact original scalar/core arrays and affine port
constraints. Neither numerical report claims continuous metric control,
complete embedding, or reach. The restored 0.01334 metric error remains
far above the README's continuous 1e-6 target.

## 5. Exact sources and files

| Item | SHA-256 |
|---|---|
| Same executed v7 source, 49,261 bytes | 702c9e13db661d39771aa673dca7c19120c695da16556919e63918705b038ec8 |
| R664 residual-Hessian module | 29e2cf8cf7e558168bec6cc90df662638d69da188770c17862a511352a0fb8b4 |
| R660 true-Phi module | e83742c6f4237eca9d1593199209725d5f898e333f963d88873d5aaf79b0db91 |
| Initial 077087 bundle | 077087b778921efd85e1b6bbe3b8389bd60f385e2de0e5a767b8f705bc847dc3 |
| First r22 output bundle | bede53ea69f41d6bb4dedd4805cb94e2bc5abefc8ec69fff3a793f4fd3beffa2 |
| First r22 complete JSON | 2adf08f2baaff22f81dcca0381da4b683ab70c039da4c8815db10507d3d69df4 |
| First r22 grid memory | 719db4931881c39d0d38f1f7fc03327c179c0de997c84903332c4b8d64d6eca2 |
| First r22 arbitrary memory | aea5a6cf6f0d45528cb05a71d41b1c055e5e2091323d7a69ce39aa35c8e8d99d |
| First r22 immutable handoff | 63cc7cd64036f8ab18cc3a5eb4c94577eafbad43544f40bf2437f0d07675b7db |
| Restored final bundle | 35f74961a297775f7e38c01cee7f9ed5516e98c48964f758f1795b76d2061ebf |
| Restoration complete JSON | 05a1474edb5d4b54f4f04bf70487f995dc93403a2c536e23f887097fc7e82088 |
| Restoration grid memory | 2404ea1d17fb65243a557849f85079e6f9684227905850c59fa6b42ef22d8170 |
| Restoration arbitrary memory | 908b79d48b10b8ae4dcc6578c90874a7d21df50240406c61c47513610e5e6754 |
| Restored immutable all-history handoff | 9226cba553ac24c2d8303a94019c87715f8ff16f7f02c293fa9bf9fae763258c |
| Same-scalar carrier | 71fdec7b9b471cc7e202a859e6907de256f8117f252798baaad794ccab918112 |

The first run stem is
`work/geometry_path/curvature-qp-spectral-hessian-r22-six-step`;
the restoration stem is
`work/geometry_path/curvature-qp-spectral-hessian-r22-restore-three`.
Every accepted field was saved separately. The restoration's
`.accepted-2.npz` is the first actual recovered field, SHA
be4d3e676adfa083851613e1b9ffc84bd69d594d7e705288116b66610a0decae;
its `.accepted-3.npz` is byte-identical to final 35f74961.

The first all-history handoff contains 780 curvature locations, 137 radius
locations and the prior 7 protected seeds. The restored handoff has 921,
150 and 8 respectively. It carries locations only; all previous numerical
values must be discarded and reread at a new field.

## 6. Complete scientific commands

The exact original dependency map and the 077087 parent recipe are in the
[preceding v7 result](2026-11-20-curvature-qp-spectral-hessian-four-step-result.md).
All named scratch source paths below correspond to the complete published
sources linked there, with the same hashes. In particular, the Gauss
retarget helper is `fullclosed_curvature_qp_v3.py` and the three-jet
coarse-space helper is
`scripts/resume_20261120_physical_subspace_v3.py`. No new oracle solve is
used.

The first full invocation, from `/workspace/scratch/24b2ab87057a`, is:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_curvature_qp_v7_spectral_hessian.py \
 --gauss-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_curvature_qp_v3.py \
 --qp-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_curvature_qp.py \
 --memory-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_curvature_qp_v2.py \
 --observed-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/gauss_observed_closed_gram.py \
 --carrier work/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz \
 --operator math-research-public/topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py \
 --batch-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_batched_closed_gram.py \
 --base-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_physical_subspace.py \
 --coarse-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_physical_subspace_v3.py \
 --norm-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/fullclosed_gauss_physical_height_lm.py \
 --coordinate-source math-research-public/topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-root-fullclosed-integrated-coordinates.py \
 --scale-source math-research-public/topics/visible-flex-larger-amplitude/scripts/integrated_l2_scale_20261120.py \
 --height-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/physical_height_coordinates.py \
 --spectral-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/positive_spectral_gram_weights.py \
 --hessian-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/positive_spectral_gram_hessian.py \
 --bundle work/geometry_path/curvature-qp-spectral-hessian-four-step.npz \
 --memory-input work/geometry_path/curvature-qp-spectral-hessian-four-step.memory.json \
 --local-memory-input work/geometry_path/curvature-qp-spectral-hessian-four-step.local-memory.json \
 --fixed-point-input work/geometry_path/curvature-qp-spectral-hessian-four-step-witnesses.json \
 --out work/geometry_path/curvature-qp-spectral-hessian-r22-six-step.json \
 --safety .992 \
 --steps 6 \
 --damping .0019301197463913783 \
 --local-refine 9 \
 --spectral-p 8 \
 --spectral-epsilon .001 \
 --spectral-scale .05 \
 --centers .30,.60,.83,.99,.995,1.0,1.02,1.05,1.077134370991557,1.097,1.20,1.35,1.55,1.75,1.95,2.020292089293148,2.100560831276262,2.15,2.2410311297467116,2.26,2.301232686234047,2.321299871729826 \
 --seconds 1800
```

After it completes, the immutable first-r22 handoff is generated by the
published `export_curvature_history_manifest.py`, with
`--report work/geometry_path/curvature-qp-spectral-hessian-r22-six-step.json`,
`--input-manifest work/geometry_path/curvature-qp-spectral-hessian-four-step-witnesses.json`,
the unchanged `--carrier`, the actual first-r22 `--bundle`, and
`--out work/geometry_path/curvature-qp-spectral-hessian-r22-six-step-witnesses.json`.
This generator's complete source and provenance are in the
[first p8 result](2026-11-20-curvature-qp-spectral-p8-six-step-result.md);
the handoff is not a hand-edited hidden input.

The second full invocation is:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_curvature_qp_v7_spectral_hessian.py \
 --gauss-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_curvature_qp_v3.py \
 --qp-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_curvature_qp.py \
 --memory-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_curvature_qp_v2.py \
 --observed-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/gauss_observed_closed_gram.py \
 --carrier work/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz \
 --operator math-research-public/topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py \
 --batch-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_batched_closed_gram.py \
 --base-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_physical_subspace.py \
 --coarse-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_physical_subspace_v3.py \
 --norm-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/fullclosed_gauss_physical_height_lm.py \
 --coordinate-source math-research-public/topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-root-fullclosed-integrated-coordinates.py \
 --scale-source math-research-public/topics/visible-flex-larger-amplitude/scripts/integrated_l2_scale_20261120.py \
 --height-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/physical_height_coordinates.py \
 --spectral-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/positive_spectral_gram_weights.py \
 --hessian-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/positive_spectral_gram_hessian.py \
 --bundle work/geometry_path/curvature-qp-spectral-hessian-r22-six-step.npz \
 --memory-input work/geometry_path/curvature-qp-spectral-hessian-r22-six-step.memory.json \
 --local-memory-input work/geometry_path/curvature-qp-spectral-hessian-r22-six-step.local-memory.json \
 --fixed-point-input work/geometry_path/curvature-qp-spectral-hessian-r22-six-step-witnesses.json \
 --protected-point 821,.13182023373669122,.43591193437744524 \
 --out work/geometry_path/curvature-qp-spectral-hessian-r22-restore-three.json \
 --safety .992 \
 --steps 3 \
 --damping .004825299365978445 \
 --local-refine 10 \
 --spectral-p 8 \
 --spectral-epsilon .001 \
 --spectral-scale .05 \
 --skip-spectral-probe \
 --centers .30,.60,.83,.99,.995,1.0,1.02,1.05,1.077134370991557,1.097,1.20,1.35,1.55,1.75,1.95,2.020292089293148,2.100560831276262,2.15,2.2410311297467116,2.26,2.301232686234047,2.321299871729826 \
 --seconds 1800
```

Both use the remaining defaults: positive legacy fraction 0.5, grid memory
32/4, moving arbitrary memory 12/2, N=2048, stage block 64, low modes 12, top
grid locations 32/4, reach ratio 0.03, linear margin 0.0002, 12 backtracks,
40,000 halfspace repairs, and 3 failed restoration attempts. The first
enlarged-space run enables the new spectral assembly probe. The restoration
skips that unchanged-space probe explicitly. Neither 1800-second bound
binds.

The restored final handoff is generated by the same exporter from the
restoration report, the first-r22 immutable handoff, the unchanged carrier,
and the exact restored bundle, writing
`work/geometry_path/curvature-qp-spectral-hessian-r22-restore-three-witnesses.json`.
The two `iteration_budget` statuses describe only the declared six- and
three-direction experiments. The original failed final-screen scope is
retained, and work continues from the actual restored 35f74961 field.


公开源码路径均对应实际执行的同SHA字节；临时数组沿原输入链再生。纯位置输入若替代原诊断清单，计算语义保持，文件路径与输入清单SHA不冒称原raw报告逐字相同。
