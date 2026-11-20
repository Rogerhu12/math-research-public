# Physical-H² curvature QP: six further accepted directions

Date: 2026-11-20 UTC. This is the immediate continuation of
[the first physical-H² result](2026-11-20-curvature-qp-physical-h2-first-result.md).
It uses the **same executed v5 source, same positive radial Gram objective,
same original fixed scalar metric, same 1,964-dimensional physical subspace,
and same numerical safety margin 0.992**. No spectral-Lp objective was used in
this batch.

## 1. Result and exact scope

All six complete QP directions yielded accepted actual nonlinear trials. The
batch took 172.624160722 seconds and paid for 15 true trial fields. Its final
field passes the implemented finite numerical screen, including the retained
Gauss/grid points, immutable witness manifest, protected curvature basins,
bounded moving memories, direction-pinned constraint locations, and the
final local re-evaluation. This is **not** a continuous metric, embedding, or
reach certificate.

| Quantity | Input e19 | Output 0241 |
|---|---:|---:|
| Positive radial Gram sum Jw | 0.19933799357553592 | 0.13368399851982452 |
| Jw/(S·2048) | 4.104626573633294e-5 | 2.75272607570466e-5 |
| All 7,377-stage raw sum | 639.1846917448484 | 608.2059957615014 |
| Legacy 1,845-stage raw sum | 159.90671659019984 | 152.17766336711398 |
| Maximum sampled Gram operator norm | 0.03058934153500248 | 0.024013578471355768 |
| Minimum sampled relative Gram determinant | 0.9733882381025515 | 0.974207252946016 |
| Current known-point 0.03·D_lb·K | 0.9908179272691353 | 0.9918941656379913 |
| H | 1.8953801947486573 | 1.879857759511436 |

The final worst sampled metric value is on an added Gauss observation; its
legacy-only counterpart is 0.023812027917665457. The final highest known
curvature is K=8.07248383453774 at cell 188, u=0,
phi=0.5009630056335069, s=0.445. The largest known radius gives
D_lb=4.095782603260305 at cell 880, u=0.6868410963222171,
phi=0.529274999274405. These are current values, not inherited values at
remembered locations. The original scalar data, mesh, fixed core support
coefficients, and exact affine endpoint conditions remain unchanged.

The README target still requires continuous relative metric error at most
1e-6 and all the complete geometric conditions. Neither 0.02401 nor this
finite curvature screen meets that target. The value 0.992 is an algorithmic
margin below the necessary curvature threshold 1; a rejection against 0.992
alone does not prove failure of the actual reach target.

## 2. Paid directions and rejections

| Direction | Square-root damping mu | Accepted alpha | Jw after | Max Gram after | Known-point product after |
|---|---:|---:|---:|---:|---:|
| 1 | 0.0025 | 1/2 | 0.16233756278426964 | 0.027131100250244566 | 0.9916009619043427 |
| 2 | 0.0025 | 1/4 | 0.15322691320235285 | 0.026213824144398767 | 0.9917734649591986 |
| 3 | 0.0025 | 1/2 | 0.14156925868939035 | 0.024947186954118017 | 0.9917624160903644 |
| 4 | 0.0025 | 1/2 | 0.13535729576354327 | 0.02425940862563003 | 0.9917563860402296 |
| 5 | 0.0025 | 1/8 | 0.13431466556002963 | 0.024134147287862007 | 0.9917718638894878 |
| 6 | 0.01 | 1/2 | 0.13368399851982452 | 0.024013578471355768 | 0.9918941656379883 |

The nine rejected trials had lower true Jw, but failed the numerical geometry
screen. In direction 2, alpha=1/2 passed the Gauss-only product
0.9906662091982505 while the arbitrary/protected points reached
0.9939065252810401. In direction 6, the full trial similarly passed the
Gauss-only value 0.9918143899147247 but failed the additional-point value
0.9923296039143646. Thus these actual line searches used more than the
Gauss-only geometry test.

The fifth direction's full step exposed a product 1.042771458450074; alpha=1/4
still gave 0.9920881435825816, and alpha=1/8 was accepted. Its small accepted
step multiplied mu by four, so direction 6 used mu=0.01. The final damping is
0.01. The 6 QPs used respectively 1419, 1441, 1408, 1300, 1290, 1408 rows;
all had nonnegative initial bounds. Every repaired maximum unscaled linear
violation was negative, between approximately -4.82e-9 and -8.59e-10.

## 3. Norm and unchanged objective

The exact norm, physical height compensation, and whitening are given in
[the first v5 result](2026-11-20-curvature-qp-physical-h2-first-result.md).
In coefficient variables alpha, the positive norm is

    ||DoubleIntegrated.inverse(A_height^{-1} B alpha, affine=False)/scale||²

with matrix G, and R satisfies RᵀGR=I. Each QP uses the original weighted
Gram data model divided by C0=S·2048=4856.422137302683, plus mu²I in
whitened coordinates. At mu=0.0025 the corresponding unnormalized penalty
coefficient is C0·mu²=0.03035263835814177. This positive integrated coordinate
norm is not asserted to equal exact geometric bending energy.

Every legacy and added Gauss row has strictly positive radial weight:
0.5 times composite Simpson plus 0.5 times the six-point Gauss quadrature.
Angular quarter-orbit multiplicities reproduce the full N=2048 sum. The
normalization, fixed scalar oracle values, row set, Frobenius factor two on
the mixed Gram entry, and true Jw acceptance are unchanged from v5's first
run. Initial basis/operator objective disagreement was 8.326672684688674e-17;
the existing one-point arbitrary derivative check gave relative error
6.027954069247058e-15 for curvature and zero for diameter. These checks do
not certify the continuous surface.

## 4. Files and hashes

| Item | SHA-256 |
|---|---|
| Executed source fullclosed_curvature_qp_v5_h2.py | fac7b5834a932242f320d91af1dad4466dd2c895b0074a7d4b7ab6601fb5e693 |
| Input curvature-qp-physical-h2-first.npz | e19acbc3cc600b37ac5d50bc7448ffe229a6a1c8119798b62165d7460ac9fec7 |
| Output curvature-qp-physical-h2-next-six.npz | 0241f7144f82b485350f684e999c8fb3fa71c94a942339da0bfa9f00bdb30023 |
| Complete output JSON | a271ce1eb1cc2ec6b64ebc29241fb0863c3e37ed19de67a3d36425f4187b5481 |
| Output grid-memory JSON | 8209201dc289ed22185c2d3790b8cfaf46744dee2c026f685e10225a16da65c3 |
| Output arbitrary-memory JSON | 1212b26a617b851d5a67651c712e35a73266ed0a8d9a3e064790d05c987710ba |
| Immutable initial witness manifest | 52723ab1e61df0bb52c23f32d5c9396e54d7ef3e1869f05bc285a45910845f60 |
| Same-scalar observation carrier | 71fdec7b9b471cc7e202a859e6907de256f8117f252798baaad794ccab918112 |

The run stem is `work/geometry_path/curvature-qp-physical-h2-next-six`.
Each accepted field was also written separately as `.accepted-i.npz` before
any later trial could change the parent or its memory. Raw numerical bundles
and large reports are regenerable scratch products, not repository evidence
substitutes. The complete compact source is published as
[`scripts/resume_20261120_curvature_qp_v5_h2.py`](../scripts/resume_20261120_curvature_qp_v5_h2.py).

## 5. Actual command and regeneration

Run from `/workspace/scratch/24b2ab87057a` with the byte-identical published dependency paths shown below. The dependency map, exact hashes, and
commands to recreate the e19 input and its memory files are in
[the first v5 result](2026-11-20-curvature-qp-physical-h2-first-result.md).
That note in turn links the actual 13ce parent construction and the complete
witness-manifest generator. The same-scalar carrier comes from the published
Gauss observation builder; no new scalar metric is solved here. The e19
`.memory.json` and `.local-memory.json` are outputs of the first v5 command,
not undocumented hand-created inputs. The immutable manifest is recreated
by `scripts/resume_20261120_rebuild_curvature_witness_manifest.py` from the
recorded r17 and dense-angle reports, with the stated checksum.

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_curvature_qp_v5_h2.py \
 --gauss-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_curvature_qp_v3.py \
 --qp-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_curvature_qp.py \
 --memory-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_curvature_qp_v2.py \
 --observed-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/gauss_observed_closed_gram.py \
 --carrier work/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz \
 --bundle work/geometry_path/curvature-qp-physical-h2-first.npz \
 --memory-input work/geometry_path/curvature-qp-physical-h2-first.memory.json \
 --local-memory-input work/geometry_path/curvature-qp-physical-h2-first.local-memory.json \
 --fixed-point-input work/geometry_path/curvature-qp-r17-angular8192-witnesses.json \
 --operator math-research-public/topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py \
 --batch-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_batched_closed_gram.py \
 --base-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_physical_subspace.py \
 --coarse-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_physical_subspace_v3.py \
 --norm-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/fullclosed_gauss_physical_height_lm.py \
 --coordinate-source math-research-public/topics/visible-flex-larger-amplitude/notes/2026-11-17-parallel-root-fullclosed-integrated-coordinates.py \
 --scale-source math-research-public/topics/visible-flex-larger-amplitude/scripts/integrated_l2_scale_20261120.py \
 --height-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/physical_height_coordinates.py \
 --out work/geometry_path/curvature-qp-physical-h2-next-six.json \
 --safety .992 --steps 6 --damping .0025 --local-refine 9 \
 --centers .30,.60,.83,1.05,1.077134370991557,1.20,1.35,1.55,1.75,1.95,2.020292089293148,2.100560831276262,2.15,2.2410311297467116,2.26,2.301232686234047,2.321299871729826 \
 --seconds 1800
```

All remaining parameters used the source defaults: legacy fraction 0.5;
grid memories 32 curvature locations and 4 radii; moving arbitrary memories
12 and 2; N=2048; stage block 64; low modes 12; top grid selection 32 and 4;
reach ratio 0.03; linear margin 0.0002; 12 backtracks; 40,000 halfspace repair
iterations; and 3 consecutive failed restoration attempts. Protected basins
and immutable witness locations were restored from the e19 memory/manifest;
no previously protected location was deliberately removed in this run.
The 1800-second limit did not bind. The status `iteration_budget` records
completion of the declared six directions, not completion of the research
problem. Work continues from the exact 0241 field.

