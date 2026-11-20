# Exact spectral residual Hessian: first four actual QP directions

Date: 2026-11-20 UTC. The complete new v7 source is
[`resume_20261120_curvature_qp_v7_spectral_hessian.py`](../scripts/resume_20261120_curvature_qp_v7_spectral_hessian.py).
It consumes [R664](../results/R664-positive-spectral-residual-Hessian-and-true-gradient-pullback.md)
and its frozen module
[`positive_spectral_gram_hessian.py`](../scripts/resume_20261120/positive_spectral_gram_hessian.py).
The input is the actual ca3679 field from
[the four further v6 directions](2026-11-20-curvature-qp-spectral-p8-next-four-result.md).
This batch retains the same true p8 objective, physical-H² norm, fixed scalar
metric, original observation rows, 1,964 physical columns and numerical
geometry margin 0.992. Only the positive residual second-order model changes.

## 1. What changes in the direction model

For the relative Gram matrix $E$ and fixed parameters $k=4$, $c=0.05$,
$\epsilon=0.001$, define

$$
h(t)=t\left((t^2+\epsilon^2)/c^2\right)^{k-1}.
$$

With $T(e,f,g)=\left(\begin{smallmatrix}e&f\\f&g\end{smallmatrix}\right)$,
R664 provides the positive raw-residual block

$$
L(E)=T^*Dh(E)T.
$$

The new data normal and the unchanged half-gradient are

$$
N=\frac{k}{c^2}\sum w_sm_\phi J^TL(E)J,
\qquad g=\frac{k}{c^2}\sum w_sm_\phi J^TK(E)r.
$$

In particular, **the gradient is not replaced by $J^TL(E)r$**. Both external
factors remain $k/c^2=1600$, and the true mean objective is normalized by
$C_0=S\cdot2048=4856.422137302683$. The point Hessian is exact with respect
to the symmetric Gram residual. The full nonlinear field Hessian also has
terms involving second derivatives of the Gram map; those are not included
or claimed to be exact here.

The module uses a positive spectral square-root factor and a positive
Gauss integral for the divided difference of $h$. This avoids subtracting
nearly equal spectral values. The source still accepts only against the
actual fixed-parameter Phi and actual geometry; a positive local quadratic
is not asserted to be an MM majorant.

The physical coordinate norm $G$, its whitening $R^TGR=I$, and the general
finite curvature QP are unchanged. The initial explicit damping is inherited
from v6, $\mu=0.015440957971131026$, corresponding to an unnormalized
penalty coefficient $C_0\mu^2=1.157883624289033$. No trace-based damping reset
or new angular/radial basis is performed in this batch.

## 2. Actual result

Four directions and six nonlinear trial fields completed in
150.996568011 seconds. The first three directions were accepted at full
step. Their actual/predicted Phi decrease ratios were 1.0003347843,
1.0001103925 and 1.0006893297. The fourth direction had a similarly accurate
objective prediction, but its larger steps failed the finite geometry
screen; its quarter step was accepted.

| Quantity | Input ca3679 | Output 077087 |
|---|---:|---:|
| True normalized Phi | 1.907280008101566e-7 | 1.8198200809540876e-7 |
| Maximum sampled Gram operator norm | 0.01507268828896618 | 0.01495643901349162 |
| Old positive radial Jw | 0.20417889354529722 | 0.20418344137988473 |
| Old mean Jw/(S·2048) | 4.204306952169127e-5 | 4.2044005979531824e-5 |
| All raw quadratic sum | 754.4818009811452 | 754.3946753556374 |
| Legacy raw quadratic sum | 188.73441998911667 | 188.71193594730013 |
| Minimum sampled relative Gram determinant | 0.9797826242389714 | 0.979849823470919 |
| Current known-point 0.03·D_lb·K | 0.9918324577164394 | 0.9918000012232376 |
| H | 1.8782943995597212 | 1.8782497136899416 |

Jw is still a diagnostic, and its very small increase is not hidden. The
final highest known curvature is K=8.071398530758998 at cell 191, u=1,
phi=0.594426180406, s=0.455. The largest known point radius yields
D_lb=4.09594445309415 at cell 880, u=0.924226584431,
phi=0.451800207911. The final scan tests 642 fixed/current arbitrary
locations, the complete Gauss/grid set, and local searches. It passes the
implemented finite 0.992 screen.

The scalar carrier, fixed support core coefficients, and exact affine port
conditions remain unchanged. No continuous metric, full reach or completion
certificate is claimed. The maximum error remains far above 1e-6.

## 3. Paid directions and actual rejection cause

| Direction | mu | Accepted alpha | Phi after | Max Gram after | Known product after |
|---|---:|---:|---:|---:|---:|
| 1 | 0.015440957971131026 | 1 | 1.902485943128411e-7 | 0.01504084772857216 | 0.9917999950935417 |
| 2 | 0.007720478985565513 | 1 | 1.8882235259348782e-7 | 0.015028029937779318 | 0.9918000679591348 |
| 3 | 0.0038602394927827566 | 1 | 1.8471306545259696e-7 | 0.0149894789606816 | 0.9918002732754005 |
| 4 | 0.0019301197463913783 | 1/4 | 1.8198200809540876e-7 | 0.01495643901349162 | 0.9918000012232385 |

After the first three full accepted steps, the existing trust rule halved
mu each time. The final damping is 0.0019301197463913783.

The fourth full and half trials both **decreased true Phi**, to
1.7454988314865442e-7 and 1.7937905763567192e-7. Their model ratios were
1.0029781263 and 1.0009204416. They were rejected because the current known
geometry products reached 0.9939724006615348 and 0.9920213507977304.
These exceed the algorithmic 0.992 margin, while remaining below the bare
necessary threshold 1; they are not labeled actual reach failures.

For the half trial the Gauss-only product was 0.9919892261094878, below the
margin, but the additional actual point at cell 305,
u=0.5241260342065466, phi=0.7697983356428246 exposed
K=8.073109869685323 and caused the correct finite-screen rejection. Thus
the additional paid geometry positions still matter even after the
objective model is improved. The quarter step's ratio is 1.0003135143.

The four QPs have 1548, 1548, 1548, and 1512 rows, with 10, 0, 4, and 4
negative bounds. General halfspace repair explicitly handles these bounds;
all final maximum unscaled linear violations are negative. The saved
accepted checkpoints preserve each actual field independently of later
rejected-trial memory.

## 4. Necessary new assembly check

Because the data normal changed, one new complete-operator direction check
was enabled. It compares the separated 1,964-column assembly with the
original complete Jv under R664's new positive block, while independently
checking the **unchanged true Phi gradient**:

| Check | Actual relative difference |
|---|---:|
| New residual-Hessian quadratic versus original full Jv | 1.1955538000871935e-13 |
| True Phi gradient versus complex polynomial derivative | 3.820441431093225e-14 |
| Coarse actual Phi versus original operator | 6.939143568133946e-16 |

The two mean quadratic readings are 0.00015552681323724693 and
0.00015552681323726552. The predicted and complex Phi derivatives are
-8.244868634723658e-8 and -8.244868634723343e-8. R664's independent small
point-Hessian and native-bridge checks were not rerun here. None of these
numerical derivative checks is a geometric certificate.

## 5. Current residual locations before radial enrichment

A single read-only use of the existing full-Gauss spectrum source confirms
that the actual 077087 field still has its largest metric defect at cell
832, stage 6842, s=1.096523983094783, phi=1.3775147475213059. Its components
are (0.014815185517675689, 0.0016663295911527496,
-0.0047008040891469705). The fine-prefix peak at cell 656,
s=0.9974713968016624, phi=1.3621749396424494 remains
0.014168894362377346, with components
(-0.004981059252315623, 0.0086968353192748, -0.005936819704468355).

The first three full accepted steps demonstrate useful actual behavior of
the new direction model for this batch, not a universal convergence claim.
Its remaining small metric improvement and these persistent locations give
a concrete reason to enrich radial columns. The next declared run adds
existing mesh nodes nearest 0.99, 0.995, 1.0, 1.02 and 1.097, while retaining
every old center and angular mode. Their actual mesh values are 0.99,
0.995, 1.0, 1.0195 and 1.0972015564873356; the resulting space has 2,534
columns. That enriched run is a distinct actual experiment and is not
included in the results above.

## 6. Exact artifacts

| Item | SHA-256 |
|---|---|
| Executed v7 source, 49,261 bytes | 702c9e13db661d39771aa673dca7c19120c695da16556919e63918705b038ec8 |
| R664 exact residual-Hessian source | 29e2cf8cf7e558168bec6cc90df662638d69da188770c17862a511352a0fb8b4 |
| R660 true-Phi source | e83742c6f4237eca9d1593199209725d5f898e333f963d88873d5aaf79b0db91 |
| Input bundle | ca3679b4d6401febdf89b222d253ae6ae88b0b3ab2cd7b4464185ae2d9c2c632 |
| Output bundle | 077087b778921efd85e1b6bbe3b8389bd60f385e2de0e5a767b8f705bc847dc3 |
| Complete result JSON | ec681d29056787f7ac2ff47eb5b49df7fbb26cc0b9c0aedba2624bd53a7f3a90 |
| Output grid memory | 7c35bd8f181c4e9e733de3e44351e368520bd2ad8fb53012fd7a05e1e5d7d345 |
| Output arbitrary memory | 1e34c9b1929eccdbe0c4c43b4341b1b9368d9785d7b8df9756f3e3805af0c49e |
| Initial immutable history manifest | 7c07f3f39f609f0c3ff0b3b3b160e72a83df27be4f2da91b8605f6b87864974c |
| Final immutable history manifest | 377b3837348fc455b7cd81452906fe427051602c4b4911646a4ca41b7879ce0c |
| New 077087 spectrum JSON | 360f990b888fc25e9c4749c74d85462a4ac887e105949de3c8ac726393fa11c9 |

The run stem is `work/geometry_path/curvature-qp-spectral-hessian-four-step`.
The exported final immutable history has 578 curvature points, 100 radius
points, and 7 protected seeds. It contains only actual paid locations, not
transferred numerical curvature values.

## 7. Complete actual command and reproduction

The ca3679 input and its memory/manifest files are generated by the complete
command in [the previous result](2026-11-20-curvature-qp-spectral-p8-next-four-result.md),
which also supplies the exact public dependency chain. The same-scalar
carrier remains SHA 71fdec7b9b471cc7e202a859e6907de256f8117f252798baaad794ccab918112.
The only new consumed module is the complete R664 source at
`scripts/resume_20261120/positive_spectral_gram_hessian.py`. The true Phi
module and all earlier sources retain their recorded bytes.

From `/workspace/scratch/24b2ab87057a`, the actual command was:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_curvature_qp_v7_spectral_hessian.py \
 --gauss-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_curvature_qp_v3.py \
 --qp-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_curvature_qp.py \
 --memory-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_curvature_qp_v2.py \
 --observed-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/gauss_observed_closed_gram.py \
 --carrier work/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz \
 --bundle work/geometry_path/curvature-qp-spectral-p8-next-four.npz \
 --memory-input work/geometry_path/curvature-qp-spectral-p8-next-four.memory.json \
 --local-memory-input work/geometry_path/curvature-qp-spectral-p8-next-four.local-memory.json \
 --fixed-point-input work/geometry_path/curvature-qp-spectral-p8-next-four-witnesses.json \
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
 --out work/geometry_path/curvature-qp-spectral-hessian-four-step.json \
 --safety .992 --steps 4 --damping .015440957971131026 --local-refine 9 \
 --spectral-p 8 --spectral-epsilon .001 --spectral-scale .05 \
 --centers .30,.60,.83,1.05,1.077134370991557,1.20,1.35,1.55,1.75,1.95,2.020292089293148,2.100560831276262,2.15,2.2410311297467116,2.26,2.301232686234047,2.321299871729826 \
 --seconds 1800
```

Unspecified defaults are: positive legacy fraction 0.5, grid memory 32/4,
moving arbitrary memory 12/2, N=2048, stage block 64, angular low modes 12,
top grid selection 32/4, reach ratio 0.03, linear margin 0.0002, 12 backtracks,
40,000 halfspace repairs and 3 failed restoration attempts. The new spectral
probe was enabled. The time bound did not bind.

The read-only spectrum command was the previously published
`math-research-public/topics/visible-flex-larger-amplitude/scripts/read_gauss_residual_spectrum_20261120.py` with `--repo math-research-public`,
`--bundle work/geometry_path/curvature-qp-spectral-hessian-four-step.npz`,
the same `--carrier`, and
`--out work/geometry_path/curvature-qp-spectral-hessian-four-step-spectrum.json`,
with the default N=2048 and legacy fraction 0.5. Its exact source is
`scripts/read_gauss_residual_spectrum_20261120.py`, SHA 1705bee9921b429152943f78065bc24f2b541898de71b5230d5deaa85ed1300c.
The history exporter uses this batch's report, the prior ca3679 manifest,
the unchanged carrier and the actual 077087 bundle to create the stated
final witness file. Both full small sources are retained in the repository.
The `iteration_budget` status records completion of four directions only;
the enriched radial-space continuation is already running.


执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
