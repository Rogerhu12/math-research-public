# First actual six curvature-constrained coarse steps

Date: 2026-11-20 UTC. Status: numerical evidence; the candidate remains far from the README completion criteria.

The actual input was the full-space H2 step's output
`e8b2ca40e184157abba15c3c85ebdd651e38cbb4035edb2cfd652c8b57ad0637`.
It passed the sampled necessary curvature/diameter screen and had original Gram SSE 1277.0304067322386, maximum Gram error 0.33329462549082134, and product $0.03D_{\rm lb}K=0.9705729448781107$.

The complete 1,280-column coarse QP then ran for six steps and exited naturally with status 0. Local session `39533` took 39.32841696600008 seconds. This is an actual local execution, not an Actions run claim.

## Source and command

Executed source `scripts/resume_20261120_curvature_qp.py`:
`a2a5d27edddc6fc20f88fde62677d904bb52db5fa9af37ca82d95272cb21a854`.

Dependencies:

| Role | SHA256 |
|---|---|
| Original dense Gram operator | `e7aa70c3458f2b1bf823d19870da4e050d50125c31d161d94e2cc8c3cb384b6d` |
| Batched quarter operator | `02a5e83a799d929a9d1426b5eaff9f65484a660932b0bf51634298a1a2284b4a` |
| Physical basis v1 | `1da3fac6c2050f9615c9c023e87e58a67e1d36cb578e791abb8903a771d2bfc7` |
| Complete coarse three-jet v3 | `118e1a89745988c06ecf89c392b84f7e47397f58aad86f90c3efff2c401ffae8` |

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python "$topic/scripts/resume_20261120_curvature_qp.py" \
  --bundle "$work/fullclosed_solver/integrated-h2-reach-screen-first/final.npz" \
  --operator "$topic/notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py" \
  --batch-source "$batch_source" \
  --base-source "$topic/scripts/resume_20261120_physical_subspace.py" \
  --coarse-source "$topic/scripts/resume_20261120_physical_subspace_v3.py" \
  --out "$work/geometry_path/curvature-qp-six-step.json" \
  --steps 6 --seconds 900
```

Defaults used: 2048 original full-circle angles, quarter orbit weights, 12 low correction modes, initial scaled damping 0.001, 32 separated curvature branches, four separated radius points, two explicit diameter lower bounds, safety 0.98, and at most 12 step lengths.

Requested coarse centers were `.30,.60,.83,1.05,1.20,1.35,1.55,1.75,1.95,2.15,2.26`. Their actual existing mesh nodes were:
`0.3,0.6,0.8300000000000001,1.0570671854957785,1.1975374839662283,1.3580749679324564,1.5587468228902417,1.759418677848027,1.9400233473100337,2.140695202267819,2.26109831524249`.
These precise choices are part of this run; they are not silently identified with earlier coarse-node lists.

## Necessary derivative check actually passed

The source first checked a simple principal branch at native stage 1642, angle 16. The principal curvature was $-7.958664294054589$, the gap between principal branches was $6.501474274249281$, and the generalized principal tangent had squared norm $0.9999999999999999$.

With complex step $10^{-25}$:

- Six independent physical jets, analytic cotangent relative error: $4.149059170844337\times10^{-16}$.
- A complete actual coarse-field direction, curvature derivative relative error: $3.3173369987097765\times10^{-16}$.
- The actual coarse-field diameter-lower-bound derivative relative error: $5.3573257408963505\times10^{-16}$.

The latter two probes use the original field's actual shared-quintic and analytic lift evaluation, including the height direction. They check the derivative implementation, not continuous geometry.

## Accepted states

| Step | Original Gram SSE | Maximum sampled Gram | Sampled $K_{\max}$ | Sampled $D_{\rm lb}$ | $0.03D_{\rm lb}K_{\max}$ | Accepted alpha |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1277.0304067322386 | 0.33329462549082134 | 7.958664294054653 | 4.065057941959583 | 0.9705729448781107 | — |
| 1 | 1018.6640177228076 | 0.3010881841472579 | 7.885493068246932 | 4.067036330469334 | 0.9621176037667312 | 0.125 |
| 2 | 631.4279832693724 | 0.23638830917938347 | 7.787251311433618 | 4.07525994572164 | 0.952052200702612 | 0.25 |
| 3 | 511.529315658503 | 0.21280995182517493 | 7.951030061164062 | 4.078361392797165 | 0.9728152210326356 | 0.125 |
| 4 | 484.6257275985593 | 0.20704020229728792 | 7.983648012782186 | 4.079103524911643 | 0.9769838025178094 | 0.03125 |
| 5 | 387.8206441624871 | 0.18429182346608686 | 7.981899776787703 | 4.082063171677567 | 0.9774785735653941 | 0.125 |
| 6 | 371.14518899335843 | 0.1801261226964055 | 7.9822776456329745 | 4.082530716916818 | 0.9776368103776523 | 0.0625 |

Every accepted state passes the complete native-stage point screen over 946,485 quarter points. The final sampled minimum determinant is 0.906685647411109 and minimum sampled area is 0.09372598587004956. Initial and final affine packing checks are exact, with zero projection differences.

$H$ changes from 1.939617501351516 to 1.9253372237681199. The final maximum-curvature point is stage 1675, angle 44:
$s=1.187503891218339$, $\phi=0.1349903093339364$.
The sampled maximum-radius point is stage 1763, angle 189:
$s=2.070460053032594$, $\phi=0.5798447378207724$.

The final bundle SHA256 is
`0c53537771085266634794d82a0f133e2d1f149d1af7e0248e136d9ceee6812d`.

## What the constraints did and did not achieve

The first unconstrained damped GN direction satisfied the selected linear inequalities but failed the full actual curvature screen at large step lengths. Starting with the second iteration, dual multipliers became active. The numbers of multipliers above $10^{-9}$ were 0, 2, 22, 7, 6, and 15.

Several L-BFGS-B terminations left positive linear constraint residuals. The source explicitly reported them and contracted toward the feasible zero step. The last contraction was 0.4078198218493378; the corresponding final maximum linear violation was approximately $-2.54\times10^{-13}$. No exact QP optimality is claimed for these repaired directions.

The complete nonlinear screen detected new curvature peaks near $s\approx0.59$, $1.18$, $2.14$, and $2.26$ that were not always among the previously selected active points. Some rejected trials had much smaller Gram SSE but failed the curvature condition. They were not accepted or selected as parents.

The next actual batch will retain rejected-trial locations in a bounded active memory, reevaluate both principal branches and the current diameter derivatives at those fixed locations, and continue from the final bundle above. No stale derivative is carried across changing fields.

The original 11,335,680 Gram rows remain present, as 2,839,455 exact weighted quarter rows; the full field remains $M=160$ with 1,332,245 original free coordinates. The correction subspace fixes core support coefficients while moving physical interior jets and cap height. The sampled error 0.1801 is still vastly above $10^{-6}$. This is neither a continuous metric certificate nor an embedding, all-phase reach, held-amplitude, or exact-solution result.
