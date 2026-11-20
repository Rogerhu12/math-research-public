# First complete DoubleIntegrated H2-type direction: actual metric and curvature improvement

Date: 2026-11-20. Numerical work by /root/fullclosed_solver.

## Decision and complete model

The preceding inverse metric-column diagonal direction was accepted by its metric-only line search but had sampled principal curvature about 2748. Its child is not used here. This run returns to the genuine physical three-jet parent, NPZ SHA256 `f062a4b2684c09e55f90265468699eea638ee8739f3e16d99fa6bd874036971a`.

A dimensional observation corrected the prepared L2 coordinate norm before any L2 solve was launched: the trapezoidal position defect D contributes D/h to the physical quintic second derivative. Thus a radial L2 norm of D alone does not uniformly control that term on small cells. No unsuccessful L2 numerical run is invented.

All 1,332,245 original free variables and 11,335,680 original full stage/angle Gram equations remain. The original DoubleIntegrated map has 1,333,209 scaled variables, keeps every A/E/D coordinate and projects all 964 endpoint rows. The 173 additional physical coarse columns give 1,333,382 redundant optimization variables. Exact weighted quarter orbits evaluate 2,839,455 rows. The prescribed metric, mesh, angular model, core constraints and terminal constraints are unchanged.

## New positive step norm and coarse whitening

For cell length h_i, nodal trapezoidal weight w_j, and coefficient frequency nu, use

- acceleration scale A_j = 1/sqrt(w_j*(1+nu^2));
- velocity-defect scale E_i = 1/sqrt(h_i*(1+nu^2));
- position-defect scale D_i = sqrt(h_i)/sqrt(1+nu^2);
- free core coefficient scale = 1/(1+nu^2), and H scale = width.

This is the prepared positive L2 scale with the D slots multiplied by h. It is an H2-type coefficient norm, not an assertion that it equals the exact geometric bending energy. The original endpoint projection, lift and transpose are reused unchanged. Every scale is finite and positive; all original free directions remain available.

For the 173 physical columns B, form the exact Gram of DoubleIntegrated.inverse(B alpha, affine=False)/scale using separated radial and coefficient-channel products. The weights are w*(1+nu^2) for A, h*(1+nu^2) for E, (1+nu^2)/h for D, and width^-2 for H. Diagonal normalization followed by Cholesky gives R with R^T G_B R=I. The full right map is

T(zi,zc)=DoubleIntegrated.lift(zi)+B R zc,

with the literal transpose. The linearized objective remains ||W(Rmetric+J Tz)||^2+mu^2||z||^2, where W is Frobenius (1,sqrt(2),1)/sqrt(1845*2048), in addition to the operator's exact angular orbit weights. This new step norm is explicitly different from previous local, inverse-column and L2 norms.

In exact arithmetic the whitened physical columns are orthonormal in the integrated coordinate norm. Adding them can lower the induced squared step norm by at most a factor of two: it cannot use a weak metric column to evade the bending penalty without bound.

## Actual preparation

The complete H2-type scale ranges from 9.765529633499673e-6 to 252.98221281376513. The existing endpoint partition contains 168 two-dimensional and 157 four-dimensional blocks; their maximum diagonally normalized condition number is 13.960165322888349.

The coarse norm's diagonally normalized condition number is 1005.2932062706129. One necessary verification of this new separated Gram against its literal DI.inverse(B)/scale norm gives relative difference 1.67575599769823e-16. This is not a rerun of the previously registered lift/transpose certificate. The minimum actual cell remains 1.5624999999963585e-5.

## Actual complete direction

One BLAS thread; 256 maximum LSMR iterations; mu=.01; atol=btol=1e-6. LSMR reaches the declared inner budget, stop code 7. The linearized and actual full-step decreases agree well, and the first alpha=1 trial is accepted by the original full metric objective and sampled positivity rules.

| Quantity | Genuine parent | Accepted full step |
|---|---:|---:|
| Complete Frobenius SSE | 817.5061370945074 | 492.20269298748 |
| Normalized objective | .00021635388536757599 | .00013026197625219132 |
| Maximum relative Gram error | .31047503010094935 | .22964195543170085 |
| Minimum relative determinant | .7976487736505589 | .8329792213741505 |
| Minimum relative E | .746756849810117 | .792525465382657 |
| Maximum sampled absolute principal curvature | 14.093376646895273 | 13.234204952480813 |
| Minimum sampled area | .09375628136909153 | .0936719131253985 |

The accepted metric worst point is s=1.3179405969408993, phi=pi/2. Its curvature worst point is s=1.30790700419301, phi=1.2793399770966247. The curvature readout uses the actual common-quintic six jets at all 946,485 representative nodes/midpoints and angles, equivalent to 3,778,560 complete angular orbit points. These are point values, not continuous upper bounds.

The linearized full-step normalized objective is .00012976896716366762; the actual-to-predicted decrease ratio is .9943060627791707. Max absolute nodal corrections are delta Y=.003936043333338364, delta U=.012932968540212982, delta A=.24412413285603315; delta H=-.00006931523199511371. The literal projected endpoint residual is 4.099639464710814e-18.

LSMR diagnostics: normr=.012127677922618138, normar=.000038353336965911754, normA=38.90066409747424, condA=12.419595742192888, normx=.41607216478579406. Direction, exact nonlinear line search and accepted curvature readout take 76.96013925199986 seconds.

The accepted rho minimum is .16586903574808387 and the existing angular Lipschitz lower estimate is .13809963576076836. Sampled target is false. This is a concrete full-space improvement, not a closed isometry, continuous reach, all-t family, held/E3 quotient, or fixed-g refinement certificate.

## Source and continuation identity

Complete source: `scripts/resume_20261120/fullclosed_integrated_h2_lm.py`, SHA256 `861a9de1a1ae9859cae0adcc813de3f4f76d656c7f9e48821b3069ec483f02c6`.
The original integrated coordinate source and unchanged prepared scale source are dependencies; the new script applies the declared D factor explicitly. All dependency hashes are recorded in the work-only report by role.

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python topics/visible-flex-larger-amplitude/scripts/resume_20261120/fullclosed_integrated_h2_lm.py --repo . --bundle /path/to/physical-threejet-six-step.npz --outdir /path/to/new/integrated-h2-first --max-directions 1 --maxiter 256 --damping .01
```

Accepted/final bundle SHA256: `16a0ba1d8e08b9c6e5023179af34b9e728527b204a3ed9849c514cadd2e8dfba`.
Saved direction SHA256: `fcb6c180c0829308929062d3af4c2dbf81f1411572739d66706aa7e4633bf3eb`.
All raw NPZ and report arrays stay outside Git. The next actual batch has already been started from this real child with three directions, 256 inner iterations each, and initial mu=.005 under the source's declared accepted-step damping update. Its result must be recorded separately; this first-step note does not predict its outcome.
