# First six positive-spectral p8 physical-H² QP directions

Date: 2026-11-20 UTC. This is the first actual execution of the new v6
[positive spectral objective and formula](2026-11-20-curvature-qp-spectral-p8-formulas.md).
It starts from the exact 0241 field produced by the
[six further v5 directions](2026-11-20-curvature-qp-physical-h2-next-six-result.md).
The scalar metric, mesh, original affine ports, observation rows, fixed core
support coefficients, 1,964 physical coarse columns, and physical-H² norm
are unchanged. The optimization target is now true normalized Phi with
p=8, epsilon=0.001, scale=0.05. Jw remains an independently reported diagnostic.

## 1. Actual result and limitations

The declared batch completed six directions, all with an accepted nonlinear
trial, in 196.730058893 seconds. It evaluated 18 actual trial fields. Its
final actual Phi is 1.9794928665089188e-7 and its maximum sampled Gram norm
is 0.015773377107712205. The final fixed/protected/current geometry screen
passes at 0.9919678809041862 against the algorithmic margin 0.992.

| Quantity | Input 0241 | Final 8d7407 |
|---|---:|---:|
| True normalized Phi | 2.0068202402652498e-6 | 1.9794928665089188e-7 |
| Maximum sampled Gram operator norm | 0.024013578471355768 | 0.015773377107712205 |
| Old positive radial quadratic Jw | 0.13368399851982452 | 0.2061976085003055 |
| Old Jw/(S·2048) | 2.75272607570466e-5 | 4.2458748986518334e-5 |
| All 7,377-stage raw quadratic sum | 608.2059957615014 | 765.6888688223185 |
| Legacy raw quadratic sum | 152.17766336711398 | 191.53718633579336 |
| Minimum sampled relative Gram determinant | 0.974207252946016 | 0.9804141816471336 |
| Maximum known 0.03·D_lb·K | 0.9918941656379898 | 0.9919678809041862 |
| H | 1.879857759511436 | 1.8784136406728087 |

The larger old Jw is a real tradeoff of the declared objective change. This
run must not be registered as a Jw decrease. The raw sums are also distinct
from the normalized spectral target. The final maximum metric value occurs
among added Gauss observations; the legacy-only maximum is
0.01564214692825705.

The final highest retained curvature value is 8.072474650213938 at cell
191, u=0, phi=0.500782163149, s=0.4525. The largest known point radius gives
D_lb=4.09609165254712 at cell 880, u=0.8916478820082541,
phi=0.4633229874106666. The final scan tested 474 distinct fixed/current
arbitrary locations in addition to the complete original Gauss/grid
geometry scan and local refinements. Both principal branches are actually
recomputed at each retained location; none of these values is inherited
from a previous field.

These are ordinary numerical observations. There is no claim here of
continuous metric error, global curvature control, reach, or completion.
The README error threshold remains 1e-6, and the metric error above is far
larger. A 0.992 screen is an algorithmic margin; it is not the user’s reach
criterion and does not certify nonlocal separation.

## 2. Every accepted direction

| Direction | mu used | Accepted alpha | True Phi | Old Jw | Max Gram | Known-point product |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 0.00024126496829892228 | 1/16 | 1.3170306829014683e-6 | 0.16679788234007115 | 0.022649172781959326 | 0.9914510955885104 |
| 2 | 0.0009650598731956891 | 1/4 | 3.847144379978304e-7 | 0.22852694513382277 | 0.01771617646392043 | 0.9914874730471525 |
| 3 | 0.0009650598731956891 | 1/2 | 3.0286150297284846e-7 | 0.20868489399459927 | 0.015589322517369055 | 0.9917069736261408 |
| 4 | 0.0038602394927827566 | 1/4 | 2.111865993593961e-7 | 0.21069267114461881 | 0.015685208258343408 | 0.9917305965112653 |
| 5 | 0.0038602394927827566 | 1/4 | 1.9833726938599657e-7 | 0.20490653641979334 | 0.01505069925252123 | 0.9917184613370704 |
| 6 | 0.0038602394927827566 | 1/2 | 1.9794928665089188e-7 | 0.2061976085003055 | 0.015773377107712205 | 0.9919678809041846 |

The fifth accepted field has the smallest sampled maximum in this batch;
the sixth has lower Phi but a slightly larger maximum. The reported final
field follows the declared true-Phi acceptance rule. No earlier state was
retroactively relabeled the final optimization result. Every accepted
field is saved as an independent `.accepted-i.npz` checkpoint.

All 12 rejected trials had insufficient true Phi decrease, before any
costlier geometry approval. For the first direction, the full, half,
quarter, and eighth trials gave actual Phi values 156.8722995689679,
0.7406094338309294, 0.0033389861453204978, and
1.6235921423077615e-5. The sixteenth step was accepted. This paid result
shows why the frozen positive quadratic cannot be used as an MM acceptance
surrogate. Later full-step rejections likewise used actual Phi, not an
inferred reduction from the local normal equations.

The first direction has 9 negative linear bounds because the current
parent is within the 0.992 screen but above some 0.9918 linear-margin
constraints. General halfspace repair correctly handles this situation;
contraction toward a presumed feasible zero is not used. The six QPs had
1375, 1524, 1572, 1452, 1584, 1548 linear rows. Every final unscaled maximum
linear violation was negative, between approximately -4.26e-9 and -2.03e-9.

## 3. Normalization and new derivative check

The initial whitened mean data-normal trace per dimension is
5.820878492827997e-5. The predeclared rule
mu²=0.001·trace(C_data)/1964 gives
mu=0.00024126496829892228. C0=S·2048=4856.422137302683, so the initial
unnormalized step penalty is 0.0002826864317111897 times the fixed physical
norm G. The data normal and half-gradient both include the factor
k/scale²=1600. Their true mean normalization is C0.

A new single whitened physical-direction check compares the separated
coarse spectral matrix with the original complete operator derivative and
the complex polynomial derivative of Phi:

| New check | Actual relative difference |
|---|---:|
| Coarse spectral quadratic versus original full Jv | 1.353886639342194e-13 |
| True Phi gradient versus complex polynomial derivative | 2.149749048458748e-14 |
| Coarse true Phi versus actual complete operator | 2.5324628392496513e-15 |

The predicted and independently computed Phi directional derivatives are
-4.255359869518271e-6 and -4.255359869518179e-6. The corresponding mean
quadratics are 4.7247624961957324e-5 and 4.724762496195093e-5.
The probe does not replace any geometric certificate.

The trust rule multiplied mu by four after the first small accepted step,
after direction 3’s model ratio 0.16026796604115512, and after direction
6’s model ratio 0.027294565168480996. The final mu is
0.015440957971131026. The latter direction still gave a genuine positive
Phi decrease of 3.879827351046942e-10; it was not reported as convergence.

## 4. Frozen artifacts

| Item | SHA-256 |
|---|---|
| Executed v6 source, 48,485 bytes | 1872298863d3d0309c74a35f4f93bdf1373528c5e28d3cfd0e6c4545f3be0ea0 |
| Exact spectral block module | e83742c6f4237eca9d1593199209725d5f898e333f963d88873d5aaf79b0db91 |
| Input bundle | 0241f7144f82b485350f684e999c8fb3fa71c94a942339da0bfa9f00bdb30023 |
| Output bundle | 8d7407edf7587403ebec783d1c208888f78ef78b4079c719ad3c87dcfc50db59 |
| Complete result JSON | 72a34f84f096972a112d59b023210cb5b10bc38719ceb0a63df4a111c075c133 |
| Output grid-memory JSON | c0e330c598b1ed593f0d2ee633d3459790b11c58d1200f91441f905a6d6289dd |
| Output arbitrary-memory JSON | 884cad870f8b69879bd66c00139dc401b99ebedb932d186b007e012c35a4646d |
| Initial immutable geometry manifest | b00981e15137d35846a1c7c71acc58d533478ef51ca531b810853efc44fe3698 |
| Exported final immutable geometry manifest | 2dacff35a61b1d18c107083a6022a0440a9ac92faef3ae0d20c7db7738b110d0 |
| Same-scalar carrier | 71fdec7b9b471cc7e202a859e6907de256f8117f252798baaad794ccab918112 |

The run stem is `work/geometry_path/curvature-qp-spectral-p8-six-step`.
Its final immutable handoff manifest contains 482 curvature locations,
79 radius locations and 7 protected seeds, including all paid old and new
trial positions. It contains locations only and must be reread at any new
field. These raw local bundles and reports are reproducible numerical
outputs; complete source and compact findings are retained in the repository.

## 5. Full command and dependencies

The 0241 parent and its memory files are regenerated by the full command in
[the v5 next-six result](2026-11-20-curvature-qp-physical-h2-next-six-result.md).
That record links the first v5 norm/source/dependency map and the preceding
actual parent chain. The new module is the complete published source at
`scripts/resume_20261120/positive_spectral_gram_weights.py`; copying it to
the indicated scratch path preserves SHA e83742c6…. The v6 source is at
`scripts/resume_20261120_curvature_qp_v6_spectral.py`. No new oracle solve or
change of the scalar carrier is involved.

The initial manifest was actually generated with the complete source
`scripts/resume_20261120_export_curvature_history_manifest.py` as follows:

```sh
PYTHONDONTWRITEBYTECODE=1 python math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_export_curvature_history_manifest.py \
 --report work/geometry_path/curvature-qp-physical-h2-first.json \
 --report work/geometry_path/curvature-qp-physical-h2-next-six.json \
 --input-manifest work/geometry_path/curvature-qp-r17-angular8192-witnesses.json \
 --carrier work/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz \
 --bundle work/geometry_path/curvature-qp-physical-h2-next-six.npz \
 --out work/geometry_path/curvature-qp-physical-h2-next-six-witnesses.json
```

The full actual optimization command, run from
`/workspace/scratch/24b2ab87057a`, was:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_curvature_qp_v6_spectral.py \
 --gauss-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_curvature_qp_v3.py \
 --qp-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_curvature_qp.py \
 --memory-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_curvature_qp_v2.py \
 --observed-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/gauss_observed_closed_gram.py \
 --carrier work/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz \
 --bundle work/geometry_path/curvature-qp-physical-h2-next-six.npz \
 --memory-input work/geometry_path/curvature-qp-physical-h2-next-six.memory.json \
 --local-memory-input work/geometry_path/curvature-qp-physical-h2-next-six.local-memory.json \
 --fixed-point-input work/geometry_path/curvature-qp-physical-h2-next-six-witnesses.json \
 --operator math-research-public/topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py \
 --batch-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_batched_closed_gram.py \
 --base-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_physical_subspace.py \
 --coarse-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_physical_subspace_v3.py \
 --norm-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/fullclosed_gauss_physical_height_lm.py \
 --coordinate-source math-research-public/topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-root-fullclosed-integrated-coordinates.py \
 --scale-source math-research-public/topics/visible-flex-larger-amplitude/scripts/integrated_l2_scale_20261120.py \
 --height-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/physical_height_coordinates.py \
 --spectral-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/positive_spectral_gram_weights.py \
 --out work/geometry_path/curvature-qp-spectral-p8-six-step.json \
 --safety .992 --steps 6 --relative-damping .001 --local-refine 9 \
 --spectral-p 8 --spectral-epsilon .001 --spectral-scale .05 \
 --centers .30,.60,.83,1.05,1.077134370991557,1.20,1.35,1.55,1.75,1.95,2.020292089293148,2.100560831276262,2.15,2.2410311297467116,2.26,2.301232686234047,2.321299871729826 \
 --seconds 1800
```

Remaining source defaults: positive Simpson/Gauss fraction 0.5; grid memory
32 curvature/4 radii; moving arbitrary memory 12/2; N=2048; stage block 64;
12 nonzero angular modes; top grid selection 32/4; reach ratio 0.03; linear
margin 0.0002; 12 backtracks; 40,000 halfspace repair iterations; and 3 failed
restoration attempts. The spectral coarse probe was enabled in this first
new assembly run. The 1800-second bound did not bind. Immutable fixed
positions and protected seeds were imported from the exact input files;
every new witness was also appended to the persistent fixed list.

After completion the final immutable handoff was generated with the same
exporter, `--report work/geometry_path/curvature-qp-spectral-p8-six-step.json`,
`--input-manifest work/geometry_path/curvature-qp-physical-h2-next-six-witnesses.json`,
the unchanged carrier, the final `.npz`, and
`--out work/geometry_path/curvature-qp-spectral-p8-six-step-witnesses.json`.
The `iteration_budget` status means only that the six declared directions
completed. Same-objective continuation is already underway from 8d7407,
with its final damping and complete paid geometry positions retained.


公开CLI把原scratch源路径换成仓库内逐字相同完整源；执行源SHA保持。临时输入/报告路径仍按原实际运行，需依父链再生，不把source路径字符串变化当作原raw报告逐字重现。
