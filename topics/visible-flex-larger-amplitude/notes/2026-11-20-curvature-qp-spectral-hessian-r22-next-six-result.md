# Six further r22 exact-Hessian p8 directions after restoration

Execution location: the completed numerical runs below were local terminal runs, with no GitHub Actions run ID. This execution deviation and the change to public Actions are recorded in [the correction note](2026-11-20-public-actions-execution-correction.md).

Date: 2026-11-20 UTC. This continues the restored 35f74961 field from
[the r22 and restoration result](2026-11-20-curvature-qp-spectral-hessian-r22-and-restore-result.md).
The executed v7 source is unchanged. The true p8 objective, epsilon=0.001,
scale=0.05, 2,534 physical columns, original scalar metric and core support,
all original observation rows, physical-H² norm, 0.992 actual geometry
screen, and 0.0002 linear margin all remain the same.

The current worst known basin at cell 289,
u=0.5290121805813988, phi=0.7022676402048246 is added as the ninth protected
local seed. All older protected and immutable positions remain. Local-refine
is 11, leaving two additional local-search starts beyond those nine seeds.

## 1. Actual successful batch

Six directions and ten actual trial fields complete in
267.059462472 seconds. Each direction has an accepted field. The final
bundle a04f9faf passes the solver's final finite known-point screen.
The recorded initial damping is 0.012063248414946114 and its final next
value is 0.0015079060518682643.

| Quantity | Input 35f74961 | Output a04f9faf |
|---|---:|---:|
| True normalized Phi | 1.1923035857631737e-7 | 1.1393712529996062e-7 |
| Maximum sampled Gram operator norm | 0.013343526276563303 | 0.01323315849480303 |
| Old positive radial Jw | 0.19654005323887383 | 0.19567657193480562 |
| Old Jw/(S·2048) | 4.04701337079471e-5 | 4.029233176247047e-5 |
| All raw quadratic sum | 671.7092342682915 | 661.4628807079937 |
| Legacy raw quadratic sum | 168.03479015845517 | 165.47333976051834 |
| Minimum sampled relative Gram determinant | 0.9815235525282252 | 0.9817623595052539 |
| Known-point 0.03·D_lb·K | 0.9918918984053982 | 0.9918292977193249 |
| H | 1.8777124287284133 | 1.877592395637553 |

The final maximum metric value is among the added Gauss observations. The
legacy-only maximum is 0.01308050622506399. The highest retained curvature
is 8.070289516305575 at cell 113, u=0.17836061753131477,
phi=0.11275230115214022, s=0.2579459015438283. The largest known radius gives
D_lb=4.096628320935238 at cell 881, u=0,
phi=0.4166232387667864. The final screen reads 1,116 fixed/current arbitrary
positions, the whole Gauss/grid set, and the declared local searches.

The exact original scalar/core arrays and affine endpoint conditions
remain unchanged. This result is an ordinary numerical optimization
result. It does not provide continuous metric control, full reach, or
completion; the metric defect remains far above the README threshold 1e-6.
The value 0.992 remains an algorithmic margin.

## 2. Every direction and rejection

| Direction | mu used | Accepted alpha | True Phi after | Old Jw after | Max Gram after | Product after |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 0.012063248414946114 | 1 | 1.1912047844452563e-7 | 0.1965002758486676 | 0.013343807309464224 | 0.9918395013237957 |
| 2 | 0.006031624207473057 | 1/4 | 1.1901616425444131e-7 | 0.19647016347284751 | 0.013342084858267577 | 0.9919961481118711 |
| 3 | 0.006031624207473057 | 1 | 1.1860587590943861e-7 | 0.19635967551242334 | 0.013335047786851514 | 0.9918227983686233 |
| 4 | 0.0030158121037365286 | 1/2 | 1.1783561863219804e-7 | 0.19623520157010962 | 0.013319868941743154 | 0.9919022450576963 |
| 5 | 0.0030158121037365286 | 1 | 1.1637291107602936e-7 | 0.19602127099631608 | 0.013289708364389707 | 0.9918535477531765 |
| 6 | 0.0015079060518682643 | 1/2 | 1.1393712529996062e-7 | 0.19567657193480562 | 0.01323315849480303 | 0.9918292977193243 |

All four rejected trials reduce actual Phi but fail the geometric margin.
Direction 2's full and half trials give known products 0.9927097541454444
and 0.9922340166677597. Direction 4's full trial gives
0.9920045605313509; direction 6's full trial gives 0.9921342771737576.
These values are recorded as failures of the 0.992 numerical margin,
without being promoted to proofs of actual reach failure.

The six accepted actual/model Phi ratios are 1.0000192355, 1.0000140968,
1.0000773177, 1.0001013527, 1.0002831107 and 1.0004724682. Thus these
directions continue to have a close local objective prediction, while
geometry accounts for the backtracking. The six QPs have respectively
1463, 1452, 1474, 1463, 1430 and 1310 rows. Their negative-bound counts
are 37, 9, 63, 50, 18 and 13. All repaired maximum unscaled linear
violations are negative, between approximately -3.41e-9 and -9.51e-10.
The existing general repair handles these negative bounds.

The true mean normal and half-gradient remain

$$
N_{mean}=\frac{1600}{C_0}H_L,\qquad
g_{mean}=\frac{1600}{C_0}g_K,\qquad
C_0=4856.422137302683,
$$

with the positive penalty $\mu^2G$. The same residual-Hessian module and
physical norm were already checked at this exact dimension. The new
spectral assembly probe is therefore explicitly skipped; no old probe is
presented as a new test.

## 3. Two recorded startup argument errors

Before the successful invocation, two startup invocations fail before any
QP direction, nonlinear trial, or output field is produced. Their source
bytes are the same as the successful run:

1. The first mistakenly sets `--gauss-source` to
   `math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_curvature_qp.py` instead of the v3 Gauss
   retarget helper. It raises `AttributeError` for missing `retarget_basis`.
2. The second fixes that path but mistakenly sets `--coarse-source` to
   `scripts/resume_20261120/fullclosed_gauss_physical_height_lm.py` instead
   of the three-jet basis source. It raises `AttributeError` for missing
   `make_space`.

Both fail during basis construction, before the initial geometry/objective
report, with zero scientific directions and zero nonlinear trials. Their
wall times are about 0.898 and 0.881 seconds. Their logs are preserved as
`.launch-error.log` and `.launch-error-2.log`; neither produced a bundle.
The subsequent successful invocation uses a fixed structured argument map
with the correct dependency roles. The two startup errors are not counted
as accepted/rejected scientific trials and are not concealed inside the
267.059-second successful-run budget.

## 4. Exact artifacts and permanent handoff

| Item | SHA-256 |
|---|---|
| Unchanged executed v7 source | 702c9e13db661d39771aa673dca7c19120c695da16556919e63918705b038ec8 |
| R664 exact residual-Hessian module | 29e2cf8cf7e558168bec6cc90df662638d69da188770c17862a511352a0fb8b4 |
| R660 true-Phi module | e83742c6f4237eca9d1593199209725d5f898e333f963d88873d5aaf79b0db91 |
| Actual input bundle | 35f74961a297775f7e38c01cee7f9ed5516e98c48964f758f1795b76d2061ebf |
| Actual output bundle | a04f9faf228c3785ab785314eb14836bdad598a6d6ac826c4abf15100225f4e0 |
| Complete successful result JSON | 6331d563fa897161634c1fb772d0d549c3be82c1414183eb067f2f3c7e61f2b4 |
| Output grid memory | b686d179946c9dce802190222a35d86022cd9297cc9fc29c3715937051c86f8d |
| Output arbitrary memory | 8856fcc9675983a30b69b3922c493f2ddb19f6e5415a2c1d633ae7b1bdb4a4a4 |
| Input immutable history manifest | 9226cba553ac24c2d8303a94019c87715f8ff16f7f02c293fa9bf9fae763258c |
| Output immutable history manifest | 87cd630a6fa12e5e8aaca40a0f559d3adf1082fc8b318f0894cd1c1bad9c2bbf |
| First startup error log | a09868dac6163d8ef8fde0e3f4497fb61766ddc8c5526334ee18cd73bbae9846 |
| Second startup error log | 5d5f1fd84f6e0db898b4a02207081bae7b783cbc1d2e8aa25402ecee2820f10b |

The run stem is
`work/geometry_path/curvature-qp-spectral-hessian-r22-next-six`.
Every accepted field has an independent `.accepted-i.npz` checkpoint.
The all-history handoff contains 1,053 curvature locations, 165 radius
locations, and 9 protected local seeds. It includes all paid positions
from the inherited chain and this batch, including rejected-trial maxima
and local searches. It is a location-only input: descendants must reread
it at their actual field. The exported list has a broader paid-history
scope than the final run's internal fixed/current subset; no old values
are asserted at those descendants.

## 5. Complete successful invocation and reproduction

The full input generation and public dependency map are in
[the r22 restoration result](2026-11-20-curvature-qp-spectral-hessian-r22-and-restore-result.md).
The same-scalar carrier remains SHA
71fdec7b9b471cc7e202a859e6907de256f8117f252798baaad794ccab918112.
The input memory files and the larger immutable manifest are outputs of
that documented restoration and its public history exporter. No new
scalar oracle solve, hidden witness, or source mutation is involved.

The complete successful arguments, run from
`/workspace/scratch/24b2ab87057a`, are:

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
 --bundle work/geometry_path/curvature-qp-spectral-hessian-r22-restore-three.npz \
 --memory-input work/geometry_path/curvature-qp-spectral-hessian-r22-restore-three.memory.json \
 --local-memory-input work/geometry_path/curvature-qp-spectral-hessian-r22-restore-three.local-memory.json \
 --fixed-point-input work/geometry_path/curvature-qp-spectral-hessian-r22-restore-three-witnesses.json \
 --protected-point 289,.5290121805813988,.7022676402048246 \
 --out work/geometry_path/curvature-qp-spectral-hessian-r22-next-six.json \
 --safety 0.992 \
 --steps 6 \
 --damping 0.012063248414946114 \
 --local-refine 11 \
 --spectral-p 8 \
 --spectral-epsilon 0.001 \
 --spectral-scale 0.05 \
 --skip-spectral-probe \
 --centers .30,.60,.83,.99,.995,1.0,1.02,1.05,1.077134370991557,1.097,1.20,1.35,1.55,1.75,1.95,2.020292089293148,2.100560831276262,2.15,2.2410311297467116,2.26,2.301232686234047,2.321299871729826 \
 --seconds 1800
```

Unspecified defaults remain: positive legacy fraction 0.5; grid memory
32 curvature/4 radii; moving arbitrary memory 12/2; N=2048; stage block 64;
low modes 12; top grid positions 32/4; reach ratio 0.03; linear margin
0.0002; 12 backtracks; 40,000 repair projections; and 3 failed restoration
attempts. The time bound did not bind.

The immutable final handoff is generated with the complete published
`export_curvature_history_manifest.py` from this batch's `--report`,
the 35f restoration's `--input-manifest`, the unchanged `--carrier`,
the exact a04f bundle, and
`--out work/geometry_path/curvature-qp-spectral-hessian-r22-next-six-witnesses.json`.
The `iteration_budget` status means only that the six declared directions
completed. The independent complete-space exact-Hessian inequality direction from the preceding 35f field has since returned da088: actual Phi=1.168356583131e-7 and maximum error=0.01329666734. Its newly reread finite product is 0.991850018963. It is weaker than a04f on the two actual metric measures, so a04f remains the continuation parent; its complete source and result are recorded separately.


执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
