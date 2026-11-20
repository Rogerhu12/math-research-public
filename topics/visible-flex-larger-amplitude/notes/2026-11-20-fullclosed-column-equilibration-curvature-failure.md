# Complete-space column equilibration: a metric decrease with unacceptable curvature

Date: 2026-11-20. Numerical continuation by /root/fullclosed_solver.

## Scope and actual parent

This is the first executed column-equilibrated, 173-column-augmented direction for the documented complete shared-quintic / analytic-lift closed-surface model. It retains all 1,332,245 original free variables and all 11,335,680 original stage/angle metric equations; exact quarter-orbit weighting evaluates 2,839,455 representative rows. The 173 additional coordinates are redundant physical directions. The original prescribed metric and all affine constraints are unchanged. This is not a closed isometry or a reach certificate.

The genuine parent is the six-step physical three-jet candidate with NPZ SHA256
`f062a4b2684c09e55f90265468699eea638ee8739f3e16d99fa6bd874036971a`.
Its complete Frobenius SSE is 817.5061370945074, maximal relative Gram error 0.31047503010094935, and minimal sampled relative determinant 0.7976487736505589. An added actual common-quintic curvature point readout gives maximum absolute principal curvature 14.093376646895273 at s=1.30790700419301, phi=1.2762720155208536. These point values do not bound the continuous surface.

## Reproducible positive coordinate map

Source: `scripts/resume_20261120/fullclosed_augmented_lm.py`, SHA256
`dc559be406dadc1680c04d9cabda5cfb54c5559f71015c2d49ed55a8cce4d02a`.
The operator, batch implementation, physical basis, and helper source SHA256 values are recorded by role in the raw report; their published paths are the source defaults.

Use one BLAS thread and the real parent above:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python topics/visible-flex-larger-amplitude/scripts/resume_20261120/fullclosed_augmented_lm.py --repo . --bundle /path/to/physical-threejet-six-step.npz --outdir /path/to/fresh/augmented-first --max-directions 1 --maxiter 256 --damping .01
```

Let W include Frobenius weights (1,sqrt(2),1)/sqrt(1845*2048); quarter-orbit multiplicity is already in the operator. With the earlier positive local jet scale S0, use 16 independent Rademacher row probes with fixed NumPy RNG seed 2026112001 to estimate d=mean((S0 J^T W xi)^2). Set S=S0/sqrt(max(d,1e-12*max(d))). This estimator is a numerical preconditioner, not a rigorous enclosure. Normalize each physical coarse column by its exact current complete Gram diagonal, giving Sc. The right map is

T(zf,zc)=S zf+B Sc zc, and T^T g=(S g, Sc B^T g).

Every entry of S is strictly positive, so T remains onto the original free space. The new LM problem minimizes ||W(R+JTz)||^2+mu^2||z||^2. The redundant-coordinate norm differs from the earlier local or integrated norm. No nonlinear equation is removed or reweighted beyond the already declared objective.

This run uses 256 LSMR iterations, mu=.01, atol=btol=1e-6, and up to 15 exact-current nonlinear half-step trials. The mesh minimum remains 1.5624999999963585e-5 (maximum .020067185495778794); there is no sub-1e-12 cell in this actual parent.

## Actual direction and line search

The diagonal estimate ranges from 9.956161026312131e-16 to 1052.4326920596438. The absolute floor is 1.0524326920596438e-9 and affects 11,994 coordinates. The resulting S entries range from 1.6091036027166368e-6 to 401325083.66605204. The 16 probes take 2.297979409999243 seconds. No coarse diagonal is floored; its scales range .05410439778513571 to 508.64308277658483.

LSMR reaches its declared iteration budget (stop code 7): normr=.0035132420839087985, normar=7.255666470297799e-5, normA=81.00334149060573, condA=11.40482982871251, normx=.11215595539065831. The original normalized objective is .00021635388536757599; the linearized full-step prediction is .000011084974107179255, with half-objective directional derivative -.00020098558756173062. The full physical jet correction has max |delta Y|=.018211863422556478, |delta U|=.34119969304827913, |delta A|=49727.21765113396, and delta H=-.002687446450021759.

| Actual step alpha | Complete SSE | Max relative Gram | Accepted by original metric criterion |
|---:|---:|---:|:---|
| 1 | 22647428.69776603 | 209.6495598287618 | no |
| 1/2 | 1415725.6108005 | 52.41238061161578 | no |
| 1/4 | 88958.46270933442 | 13.103091053117039 | no |
| 1/8 | 6170.752893795105 | 3.275771286388763 | no |
| 1/16 | 1071.6866836444885 | .8189426561605666 | no |
| 1/32 | 792.5303770626725 | .30083663759909696 | yes |

All these trials have finite residuals and positive sampled rho, relative E and metric determinant. The accepted trial has determinant minimum .8037231681156474, relative E minimum .7546720024659035, rho minimum .16601946618026764, and the simple angular Lipschitz rho lower estimate .1383286452814113.

## Curvature failure and continuation decision

At the numerically accepted alpha=1/32, the maximum actual node/midpoint absolute principal curvature is 2748.111022402379, attained at s=.9999062499999886, phi=1.3314953238847365. The readout covers all 946,485 representative points, corresponding to 3,778,560 full orbit points. Minimum area remains .09375686633147089. This enormous curvature increase is an observed failure of this direction as a reach candidate, despite its modest decrease in metric SSE and maximum Gram error.

The full step also has a large nonlinear Gram error near the flat terminal cap, where normal displacement is weak or invisible to the first-order metric derivative. The observed small Jacobian column norms and large second-jet correction explain why inverse metric-column equilibration alone is insufficient. This is a numerical diagnosis, not a proof of a general obstruction or a bound on the nonlinear feasible set.

Do not promote this candidate to a reach continuation parent. Preserve it as an honest metric-only accepted trial and return to the genuine f062a4b... three-jet parent for a full-space coordinate norm that controls bending; the prepared double-integrated L2 norm is a concrete next option. No old continuous certificate is rerun or inherited.

The direction including line search and accepted curvature readout takes 76.66371696500028 seconds. Work-only files: report.json, direction-000.npz, accepted-000.npz, final.npz. Final and accepted bundle SHA256 both equal
`d3cc2d526906eae653bdf992b6130fad17b17b404e7b28982f4471167c0388c2`;
the saved direction SHA256 is
`6ec73c46beaef4aec37c91f516a38045abb001ad2227b135b5e086e7ca3bc9a5`.
The sampled target remains false. There is no continuous metric, reach, all-t, held/E3, or fixed-g refinement conclusion.
