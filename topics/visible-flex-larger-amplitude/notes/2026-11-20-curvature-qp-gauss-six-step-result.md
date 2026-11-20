# All legacy plus Gauss observations: weighted curvature-QP continuation

Date: 2026-11-20 UTC. Status: finite numerical progress on the unchanged field and scalar metric. The first actual six-step run below passes the expanded sampled necessary curvature screen. It does not certify continuous metric, embedding, all-phase reach, or held amplitude.

## Why the observation set changed

The earlier coarse-QP endpoint `0c535...` and bounded-memory endpoint `c71db...` passed the original node/midpoint screen but failed the necessary curvature condition at newly sampled Gauss points. The failures are retained in their result notes. They are not used as geometric parents.

This run returns to the actually available full-space H2 parent
`e8b2ca40e184157abba15c3c85ebdd651e38cbb4035edb2cfd652c8b57ad0637`,
which passes the expanded point screen. Its initial expanded maximum principal-curvature magnitude is 7.966176659104062, the sampled complete-body diameter lower bound is 4.065061285135142, and their necessary product is 0.971489889824134.

The original 1845 stages remain a literal prefix. Six Gauss observations in each of the 922 original cells append 5532 stages, for 7377 total. The same exact scalar oracle supplies their values; the mesh, original field, analytic lift, scalar, core conditions, and terminal residual three-jets remain unchanged.

There are 15,108,096 full angular-orbit points, represented by 3,784,401 quarter points. The three Gram components therefore have 45,324,288 full rows or 11,353,203 weighted quarter rows. Every old row is retained.

## A new, explicitly declared finite radial objective

Let $s_\ell$ denote all old and added observations. Let $w_\ell^{S}$ be the composite Simpson weights on the old node/midpoint rows, extended by zero on new rows. Let $w_\ell^{G}$ be the physical-cell Gauss weights on the added rows, extended by zero on old rows. This run uses
$$
w_\ell=\tfrac12w_\ell^{S}+\tfrac12w_\ell^{G}>0.
$$
Both component sums equal $S$, so $\sum_\ell w_\ell=S$. The actual weights have minimum
$6.692362983545742\times10^{-7}$, maximum $0.0066890618319262645$, and sum
$2.3712998717298257$.

The accepted optimization objective is
$$
J_w=\sum_{\ell,k}w_\ell m_k
\left(r_{ss}^2+2r_{s\phi}^2+r_{\phi\phi}^2\right),
$$
with the same exact angular orbit multiplicities $m_k$ as before. This is a finite quadrature approximation to a radial $L^2$ objective. It is **not** the old unweighted raw sum, and it is not asserted to equal the continuous integral exactly.

Every original and added row has positive weight. Thus zero weighted finite objective is equivalent to zero residual on all these finite rows. This does not establish a continuous zero-residual result.

At every stage, the normal matrix and gradient receive the same multiplier $w_\ell$:
$$
A=\sum_\ell w_\ell J_\ell^\top W_\phi J_\ell,\qquad
g=\sum_\ell w_\ell J_\ell^\top W_\phi r_\ell.
$$
Here $W_\phi$ includes angular multiplicities and Frobenius factors $(1,2,1)$. The existing separated angular-kernel identity is used without deleting equations. Scaled damping is applied after diagonal normalization of this weighted matrix.

The maximum relative Gram error, principal curvatures, radii, and necessary product are all read **without radial weights**. Raw sums over the old rows and over the full expanded row set are retained as separate diagnostics. They are never subtracted from $J_w$ to claim progress.

## Retargeting the exact physical basis

The 1280-dimensional physical correction space is first constructed from the original nodal three-jets. It is then evaluated at every new observation by the supplied actual Hermite weights:
$$
(Y_b,U_b,A_b)(s_\ell)
=W_\ell\,(Y_{b,i},U_{b,i},A_{b,i},Y_{b,i+1},U_{b,i+1},A_{b,i+1}).
$$
The actual $\chi,\chi',\chi''$ contributions are added to the joint-height direction. The angular fields and their frame derivatives are unchanged.

The new reusable function `fields_block_observed` reads the observation operator's actual $F_s,F_\phi,F_{ss},F_{s\phi},F_{\phi\phi}$ and adds the actual position $F$. The curvature scan therefore visits every old and new point. The old assumption that alternating stage indices are nodes and midpoints is not used on the expanded stage list.

Bounded memory retains only point locations. Old locations are valid because the old stage list is a literal prefix. New memory files bind themselves to the scalar-observation carrier and angle count. Both principal branches at every remembered location are freshly evaluated and differentiated.

## Exact executed sources and carriers

Main source `scripts/resume_20261120_curvature_qp_v3.py`:
`3131377740b06ff400b1a74e3efe349c987769c4c4d3c2cbf40ea40ad9c9308e`.

| Dependency | SHA256 |
|---|---|
| QP derivative and dual implementation | `a2a5d27edddc6fc20f88fde62677d904bb52db5fa9af37ca82d95272cb21a854` |
| Bounded memory driver | `87978e04453f44914efed0bff933e3ff0790d3a24656f941b3a6c296cb458d80` |
| New observation operator | `26f61a83505938d409ad97fdfd2b3a96d77dd0233810980aa8cd19faa9920d0d` |
| Same-scalar observation carrier | `71fdec7b9b471cc7e202a859e6907de256f8117f252798baaad794ccab918112` |
| Original dense operator | `e7aa70c3458f2b1bf823d19870da4e050d50125c31d161d94e2cc8c3cb384b6d` |
| Batched angular operator | `02a5e83a799d929a9d1426b5eaff9f65484a660932b0bf51634298a1a2284b4a` |
| Physical basis v1 | `1da3fac6c2050f9615c9c023e87e58a67e1d36cb578e791abb8903a771d2bfc7` |
| Complete coarse-three-jet v3 | `118e1a89745988c06ecf89c392b84f7e47397f58aad86f90c3efff2c401ffae8` |

The actual carrier is regenerated from its published same-scalar recipe; no raw carrier is retained in Git or a Release.

## Actual command and run

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python "$topic/scripts/resume_20261120_curvature_qp_v3.py" \
  --qp-source "$topic/scripts/resume_20261120_curvature_qp.py" \
  --memory-source "$topic/scripts/resume_20261120_curvature_qp_v2.py" \
  --observed-source "$observed_source" \
  --carrier "$work/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz" \
  --bundle "$work/fullclosed_solver/integrated-h2-reach-screen-first/final.npz" \
  --memory-input "$work/geometry_path/curvature-qp-memory-twelve-step.memory.json" \
  --operator "$topic/notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py" \
  --batch-source "$batch_source" \
  --base-source "$topic/scripts/resume_20261120_physical_subspace.py" \
  --coarse-source "$topic/scripts/resume_20261120_physical_subspace_v3.py" \
  --out "$work/geometry_path/curvature-qp-gauss-six-step.json" \
  --steps 6 --seconds 1800
```

The source uses `--legacy-fraction .5`, 2048 full angles, modes through 12, the previously recorded 11 coarse centers, and a maximum of 960 selected curvature/diameter inequalities. All 160 modes remain in the actual field. The current core support coefficients stay fixed during these coarse corrections.

The local process actually completed with exit 0, session `98651`, in 154.44616413499898 seconds. The report SHA256 is
`07133c09fc3d3a23412cab593067dfcea98985c917be56ce3e0ee6357295b342`.

## Necessary new interpolation checks

At an added Gauss stage, the actual six-jet cotangent and complete retargeted coarse field were checked with complex step $10^{-25}$. The relative errors were:

- Local six-jet curvature derivative: $1.9819606115099408\times10^{-15}$.
- Actual retargeted coarse curvature derivative: $1.3098677315781934\times10^{-10}$.
- Actual retargeted coarse diameter derivative: $7.216449660063518\times10^{-16}$.

The probe was at added stage 4614, angle 171, on a simple principal branch with gap 3.5066833170402947. These are binary64 checks of the new interpolation map, not interval bounds.

At the actual initial field, the weighted objective from the retargeted basis evaluator and the actual full observation operator agreed to relative difference $1.5277634566628848\times10^{-15}$. The same scalar-value comparison remains part of each iteration; it is not reported as a separate proof of continuous geometry.

## Six accepted expanded-grid states

| Step | New weighted $J_w$ | Full expanded raw SSE | Old-row raw SSE | Full maximum Gram | Full $K_{\max}$ | Full necessary product |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 9.301737551860922 | 5114.116312890511 | 1277.0304067322386 | 0.33426098300234397 | 7.966176659104062 | 0.971489889824134 |
| 1 | 7.349048302329948 | 4071.6000672982773 | 1016.609763106318 | 0.2952062407173779 | 7.946491212283034 | 0.9695752299175988 |
| 2 | 5.806377843308245 | 3269.600063401471 | 816.3005152477897 | 0.2613937111200413 | 7.937834077153251 | 0.9694017103944292 |
| 3 | 3.427959711379933 | 2108.669211933838 | 526.4144365097859 | 0.19952300912852317 | 7.929288009131124 | 0.9702927399595991 |
| 4 | 2.0712586535245325 | 1451.256312083815 | 362.3247568800364 | 0.15315493820825377 | 7.935035772486723 | 0.9723118545516031 |
| 5 | 1.6767734103752248 | 1259.442145929461 | 314.4615067023222 | 0.13694744142956905 | 7.937636968643721 | 0.972992190332214 |
| 6 | 1.3604706615368882 | 1108.6689095307765 | 276.8493731902904 | 0.12250456992212366 | 7.935384160595875 | 0.9730101709423132 |

Every accepted state decreases the same declared weighted objective and passes the full 7377-stage curvature/diameter screen. The final sampled minimum determinant is 0.9333233018303938. $H$ is 1.9113893513515579, the sampled complete-body diameter lower bound is 4.087221451205496, and the smallest sampled area is 0.09372598587004956.

The final maximum-curvature point is added stage 6772, in parent cell 821:
$s=1.0134699300537593$, $\phi=0.6381360077604268$, principal branch 1.
The final maximum-radius point is added stage 7132:
$s=2.06382574732771$, $\phi=0.5368932757599744$.

Output bundle SHA256:
`2038ba41e2001036eebe8bc43fccbb54b8d9ccf180f73139420798de278bcaa9`.

## Remaining obligations

The maximum error remains 0.1225, far above $10^{-6}$. Six Gauss samples detect the previously identified derivative-sampling deficiency, but their finite values do not bound the continuous nonlinear Gram residual or curvature. All-phase embedding, true reach, diameter, held amplitude, and fixed-metric refinement still require their actual checks.

The actual next batch continues on this same observation plan and weighted objective from the output bundle above, carrying only its bounded point-location memory. The full-space solver may also use this parent. The prior native-grid failures remain recorded and are not substituted for the expanded-grid state.
