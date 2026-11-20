# Bounded active memory: twelve native-stage QP steps and their Gauss failure

Date: 2026-11-20 UTC. Status: numerical evidence. The twelve steps improved the old sampled objective and passed its old point screen. **The final candidate fails the necessary curvature condition at newly observed Gauss points and is not retained as a feasible geometric parent.**

## Complete source and memory rule

Source: `scripts/resume_20261120_curvature_qp_v2.py`.
SHA256: `87978e04453f44914efed0bff933e3ff0790d3a24656f941b3a6c296cb458d80`.

This complete continuation driver imports the preserved first QP source, SHA256
`a2a5d27edddc6fc20f88fde62677d904bb52db5fa9af37ca82d95272cb21a854`.
Its original operator, batched angular implementation, physical basis, and coarse-three-jet dependency hashes are unchanged from the first six-step note.

The memory stores only fixed-grid locations. At each location both principal branches are computed again from the current field, regardless of the old sign or which branch was previously worst. Radius derivatives are likewise recomputed. Current extreme points are included independently of memory.

Memory has capacities 32 curvature locations and four radius locations. A rejected trial inserts its actual worst-curvature and maximum-radius locations, moving repeated entries to the recent end. Oldest locations are evicted when capacity is exceeded. Thus at most
$$
(32+2\cdot32)(4+4+2)=960
$$
linear constraints occur. The two extra diameter constraints are the fixed core and the cap-height lower bounds. This is a bounded optimization heuristic; it never substitutes for the complete nonlinear point screen.

The first run restored all rejected-trial locations from the first QP report, then wrote a compact `.memory.json` after each step. This memory is sufficient as an algorithmic checkpoint together with the actual field bundle; it contains no stale curvature values, signs, eigenvectors, or derivatives.

## Actual invocation and provenance

The actual input bundle was
`0c53537771085266634794d82a0f133e2d1f149d1af7e0248e136d9ceee6812d`.

The restored first-QP report SHA256 was
`218308e0592508e453e18730f2a92530ded8ce27e14dcd86162cc04c24d7dc16`.

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python "$topic/scripts/resume_20261120_curvature_qp_v2.py" \
  --qp-source "$topic/scripts/resume_20261120_curvature_qp.py" \
  --bundle "$work/geometry_path/curvature-qp-six-step.npz" \
  --memory-input "$work/geometry_path/curvature-qp-six-step.json" \
  --operator "$topic/notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py" \
  --batch-source "$batch_source" \
  --base-source "$topic/scripts/resume_20261120_physical_subspace.py" \
  --coarse-source "$topic/scripts/resume_20261120_physical_subspace_v3.py" \
  --out "$work/geometry_path/curvature-qp-memory-twelve-step.json" \
  --steps 12 --seconds 1200
```

The unchanged defaults use 2048 full angles, 12 low correction modes, the previously recorded 11 centers, 32 current curvature branches and four current radii, safety 0.98, initial damping 0.001, and 12 step lengths. All original $M=160$ field modes and all old node/midpoint equations remain present.

The process actually completed with exit 0 in 88.15140979599892 seconds, local session `52476`. The output report SHA256 is
`e51e3ec6723170645d9521326afce397965d18f9b1fe190c0501c19dfc6c1520`.
No Actions run identifier is inferred from this local execution.

## Twelve accepted old-grid states

The initial old-grid SSE was 371.14518899335843 and maximum Gram norm was 0.1801261226964055.

| Step | Old raw Gram SSE | Old maximum Gram | Old $0.03D_{\rm lb}K_{\max}$ |
|---:|---:|---:|---:|
| 1 | 337.86638941628917 | 0.17138814775296418 | 0.9735997407585169 |
| 2 | 278.5208662448261 | 0.15429571723399294 | 0.969906728630933 |
| 3 | 230.33818499824554 | 0.13877754120599772 | 0.9702044832206173 |
| 4 | 210.05683929258703 | 0.13177690638554584 | 0.9722959115071408 |
| 5 | 191.64256539762354 | 0.12505280197639057 | 0.9700843919971488 |
| 6 | 161.82356102136444 | 0.1130412230064699 | 0.9712199430722489 |
| 7 | 148.55540949343646 | 0.10723408729433337 | 0.9724131638071626 |
| 8 | 125.7643239987143 | 0.09615905994275042 | 0.9779607177927684 |
| 9 | 117.09891402040316 | 0.09164519834843876 | 0.9780900254785251 |
| 10 | 101.07252299371723 | 0.08247830047723492 | 0.9783291676502219 |
| 11 | 88.65158524839862 | 0.07706456023777375 | 0.9784984139512508 |
| 12 | 80.92234226606062 | 0.07324989313371955 | 0.9785856210933103 |

Every accepted trial had strictly smaller old raw SSE and passed the old complete point screen. The final old-grid values were $K_{\max}=7.972797448014852$, $D_{\rm lb}=4.091351989787761$, minimum relative determinant 0.9599501801933937, and $H=1.897894704586109$.

The actual active constraint counts ranged from 560 to 910. The dual optimizer hit its iteration limit in steps 5, 8, and 10; these statuses were retained. Explicit feasible contraction and the actual nonlinear screen still determined acceptance. The old derivative implementation was unchanged, so its already passed complex-step checks were not repeated.

Output bundle SHA256:
`c71db2bcf628d0126fe178037bf9f04cb22a3baeb593a196daf5ddec5a92dbca`.

## New Gauss observations invalidate the old necessary screen

The same actual field was then read, without a nonlinear solve, at all 1845 old stages plus six Gauss points in each of 922 original cells: 7377 stages total. The additional scalar values came from the unchanged exact scalar oracle. The original field, mesh, parameters, and core coefficients were not altered.

The same-scalar observation carrier SHA256 is
`71fdec7b9b471cc7e202a859e6907de256f8117f252798baaad794ccab918112`.
The actual readout report SHA256 is
`49cda756108f72ceaaf7accb38ab72876c8aa330ef6b46ce3e4a061227c97da7`.
Its entry-point source SHA256 is
`95e55c8436e94c1d2520556b65e800af67bd58430d2c4d8f9fc761a9e9bf7b18`,
reader SHA256
`124bfa173faaa836ba0294cb79d0b82ffa004f61b9fd1bbc2d1ae646d3a588fc`,
and observation-operator SHA256
`26f61a83505938d409ad97fdfd2b3a96d77dd0233810980aa8cd19faa9920d0d`.

The largest newly sampled Gram norm is 0.07270386385936001, so the old maximum Gram remains the maximum over the union. But the newly sampled curvature reaches
$$
K_{\max}=8.220342313508384,
$$
at new stage 6865, parent cell 836, local coordinate 0.8306046932331322:
$$
s=1.1740710114274446,\qquad \phi=1.217980745581199.
$$
Already the old diameter lower bound implies
$$
0.03(4.091351989787761)(8.220342313508384)=1.0089694164332714>1.
$$
Thus this field fails a necessary condition for reach $/D\ge0.03$, even before continuous or all-phase checking. It is not a selected geometric parent.

The new reader used all 3,784,401 quarter points, equivalent to 15,108,096 full angular-orbit points. All sampled areas remained positive; that does not repair the curvature failure.

## Continuing on the expanded observations

The bounded memory idea and the exact coarse derivative formulas remain usable. The old native-grid endpoint is retained as a recorded failed branch, and its learned point locations remain useful optimization hints. The actual next solve returns to the earlier `e8b2ca40...` parent, which passes the expanded point screen, and puts every old and added row into the objective and every added point into curvature screening.

That next solve uses a declared positive radial integral weight, half composite Simpson plus half Gauss. Its weighted SSE is a new optimization objective and must not be subtracted from these old unweighted SSE values. All field equations, affine variables, scalar values, and geometric completion requirements remain unchanged.
