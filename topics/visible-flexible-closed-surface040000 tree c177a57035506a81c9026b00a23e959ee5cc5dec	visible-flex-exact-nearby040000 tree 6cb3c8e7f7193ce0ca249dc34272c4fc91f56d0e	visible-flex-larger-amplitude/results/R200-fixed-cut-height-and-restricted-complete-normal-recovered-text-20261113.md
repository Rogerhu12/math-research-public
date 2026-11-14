# R200. Fixed cut height and the restriction of a complete nonlinear normal system

## Scope

This result supplies an exact coordinate restriction for the complete R187/R190/R191 direct-position objective. It also records the elementary angular nesting used before the restriction. It is a representation and linear-algebra result, not an existence theorem for an isometric surface, a global reach certificate, or a proof that a fixed-height branch converges.

The executable is `scripts/fd2d-fixed-cut-height-R200.cjs`. It imports the frozen R196 nonuniform metric and curvature providers, the full R191 parameter derivatives, and the R195 v2 Armijo solver. None of those sources is modified.

## 1. Endpoint coordinate and angular nesting

Let $z$ be the complete parameter vector. Its five blocks are the radial coefficients for the two tangent angles, the vertical correction, the scalar cut-height correction, and the designed radius. For $J$ radial functions and $K$ angular modes, the total dimension and cut-height index (zero based) are

$$
n=2JK+2J+1,\qquad i_*=2JK+J.
$$

Write $c=z_{i_*}$. The endpoint conventions of R187, R190 and R196 give

$$
X(S,u)=(a_c\cos u,a_c\sin u,Z_b(S)+c).
\tag{1}
$$

Indeed, the two angle corrections and all radial cubic-basis corrections have zero value at the cut; the cut-height lifting has value one there. The prescribed derivative conventions also retain the existing cut collar two-jets. Thus fixing $c$ fixes the cut height in that particular field definition without removing any angle, height-basis, or radius-basis variable.

If the angular order is increased from $K$ to $L\ge K$, copy every old angular coefficient to the same radial block and angular index and append zeros. Copy all vertical, cut-height, and radius coefficients unchanged. This leaves both complete tangent angles equal pointwise, together with all available radial and angular derivatives. Therefore the nonlinear tangent vector, its derivatives, the quarter-period primitives, and the Cartesian position zero-, first-, and second-jets are unchanged in exact real arithmetic. The physical metric radius is also unchanged. The proof uses equality of the input functions before the nonlinear trigonometric operations; it does not identify two unrelated Fourier projections.

In binary arithmetic the old coefficients are copied without arithmetic. The evaluation loops may still have different floating accumulation paths, so a numerical equality claim is reported separately. For the actual J30/K7 to J30/K15 initialization below, the complete finite value and three common-point Cartesian two-jets happened to agree exactly in binary64. This observation is not needed for the real-arithmetic nesting theorem.

## 2. Restricted complete Gauss–Newton model

Let $R(z)\in\mathbb R^M$ denote the complete weighted residual vector at a current admissible state. It includes all the original metric and actual-curvature rows. Let $J$ be its actual parameter Jacobian (or the specified branchwise generalized derivative at a curvature-hinge threshold), and set

$$
H=J^\mathsf TJ,\qquad g=J^\mathsf T R,\qquad
P=I-e_{i_*}e_{i_*}^{\mathsf T}.
$$

At a state satisfying $z_{i_*}=c_*$, restrict increments to $d_{i_*}=0$. The complete linearized objective on that affine subspace is

$$
\frac12\|R+JPd\|^2.
$$

Expanding the square proves that its embedded normal matrix and gradient are exactly

$$
\widehat H=PHP,\qquad \widehat g=Pg.
\tag{2}
$$

Consequently one may assemble every row and every derivative of the original residual first, then set precisely row $i_*$ and column $i_*$ of $H$ to zero and set $g_{i_*}=0$. No residual row is discarded; $R$, $\|R\|^2$, and every free/free entry of $H$ retain their original values.

This also proves that the actual unconstrained coordinate gradient may be nonzero and need not be falsely reported as vanishing. The implementation records its value and the original diagonal and column maximum before applying (2).

## 3. Column scaling and the dummy direction

For a free column use the same R195 scale as before:

$$
D_{jj}=H_{jj}^{-1/2}\quad(H_{jj}>0),
$$

and use $D_{jj}=1$ for a zero diagonal. In particular $D_{i_*i_*}=1$ after the restriction. For every explicitly chosen $\lambda>0$, the scaled damped system is

$$
(D\widehat H D+\lambda I)y=-D\widehat g,\qquad d=Dy.
\tag{3}
$$

Its $i_*$ row is simply $\lambda y_{i_*}=0$, hence

$$
y_{i_*}=d_{i_*}=0.
\tag{4}
$$

All other equations are precisely the column-scaled, damped normal equations of the restricted least-squares problem. Equivalently, (3) minimizes

$$
\frac12\|R+JPDy\|^2+\frac\lambda2\|y\|^2.
$$

In exact arithmetic the positive damping makes this quadratic strictly convex. The claim does not replace an actual floating factorization check: if the implemented factorization or a physical-domain evaluation fails, that real outcome must be recorded.

The cut-height coordinate is the global border in the R195 layout. After (2), both border coupling vectors and the border normal entry are exactly zero. The scalar Schur value in the actual algorithm is therefore $\lambda$, and its right-hand side is zero. No new Schur approximation, hidden diagonal shift, or neglected small off-band entry is involved. The existing explicit half-bandwidth four still checks all remaining entries.

## 4. Original objective and original Armijo acceptance

For every proposed step length $\alpha$, use the original actual value function at

$$
z_{\rm trial}=z+\alpha d.
$$

By (4), this point still satisfies the fixed-coordinate constraint. Moreover

$$
g^\mathsf T d=\widehat g^\mathsf T d,\qquad
d^\mathsf T H d=d^\mathsf T\widehat H d.
$$

Thus the slope and quadratic prediction used by the unchanged R195 Armijo rule are exactly those of the complete objective restricted to the fixed-height subspace. They are not derivatives of an objective with selected rows suppressed.

The executable wraps the actual value call with a bitwise check of the saved fixed coefficient. It never assigns the fixed value back into a trial. A changed coefficient is an explicit error, not a clipped trial. After an accepted step it also checks that the returned fixed-coordinate direction equals zero and that the accepted coefficient still has the saved bits. All original angle, vertical-basis and radius derivatives are assembled before (2).

This proves the claimed fixed-coordinate method independently of whether it improves the nonlinear objective.

## 5. Exact constants versus a finite endpoint evaluation

For an exact field definition, prescribing a real height $Z_*$ means selecting the exact constant

$$
c_*=Z_*-Z_b(S).
\tag{5}
$$

The current numerical experiment instead fixes the binary64 coefficient computed from the declared finite background evaluation. These two statements must not be conflated. Its constants are

$$
Z_*=\frac58,\qquad
Z_b(S)_{\rm finite}=0.743536989256208,\qquad
c_{*,{\rm binary64}}=-0.11853698925620804.
$$

The coefficient bits are `bfbe5870ac38c270`. The actual finite subtraction and addition satisfy $Z_b(S)_{\rm finite}+c_{*,{\rm binary64}}=5/8$ exactly in binary64, and this is checked on initialization and restart.

For the accurate physical target, the true cut height differs from $5/8$ by the background endpoint-evaluation error, plus any explicitly defined coefficient-rounding error. Those terms remain to be paid by the accurate scalar and position consumers, such as R193. The fixed finite height is not a substitute for that bound, and it does not automatically establish any R168/R199 cap condition.

Changing the old free cut coefficient to this new constant changes the actual position field throughout its lifting support. The initialization is therefore recorded as a new baseline, not as an accepted step from the old field. Its radius coefficients initially remain unchanged; later radius optimization is still an explicit design of a new physical metric, rather than same-metric certification.

## 6. Actual initialization and saved evidence

The input is the complete strong-gap R196 field after cumulative iteration 32, with N128 and explicit rational nonuniform knots. The old report SHA256 is

`5a3d10f12fcff453f9b1848a309bcbc5f4c7ccfbb918a0f0fe8e4e0c951336d8`.

Its J30/K7 to J30/K15 zero injection gives dimension 961 and retains finite squared objective $0.008129793506931191$. At the three recorded common points, all six Cartesian zero/first/second jet vectors agree exactly in the actual binary64 computation.

The subsequent fixed-height field has a separately evaluated initial squared objective $0.22817643141261687$, maximum sampled metric residual $1.2111344869052791$, maximum sampled curvature $17.42144801764258$, and minimum sampled immersion $0.5397091355337821$. These are initialization diagnostics only. The actual initialization child exited naturally with code zero; the complete source, coefficient vector, source hashes, baseline, and exit receipt are saved under the R200 prefix.

The first finite target keeps guide $9.5$, curvature weight $0.01$, nodeShare $0.5$, and all original physical parameter bounds. Any later accepted steps and process exits are separate actual evidence. No continuous metric, full-core reach, held displacement, fixed-cap graft, or strong completion is claimed by this theorem.
