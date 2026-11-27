# R147 PP: an actual phase pivot with the entire regular defect retained

2026-11-27, visible-exact-astra-fb31ed6-20261127 / positive_inverse.

**New consequence of the completed APHI column.** The scalar phase
pivot can now be performed before proving a full regular inverse.
This is an exact reduction of the original augmented linearized
equations at the original selected member. It keeps the candidate
particular's entire regular defect, the nonmean conjugacy equation,
the raw $E'a$ term, all means and every physical boundary row.
The reduced operator is still to be certified; a nonzero pivot does
not alone prove that operator invertible.

In its already certified physical half-sum response component, the
phase-normalized strict column has ordinary $L^2$ norm below
.041426 and physical high97 norm below .001376. Its rank-one feedback
from the ordinary distributed state phase row has norms below
.062139 and .002064 respectively. These are the original PO physical
target spaces, not an unpaid incoming/Theta renormalization.

## PP1. The paid scalar and the exact particular

The [whole completed APHI result](R147-supplement-actual-nonzero-phase-border-of-the-strict-parameter-particular.md)
gives, on the original selected $Q_\delta$,

$$
 c:=\langle b_\nu+Lv_\nu\rangle
   \in(.038736784,.038768096),\qquad c^{-1}<25.82.       \tag{PP.1}
$$

Here the scalar is precisely the PH transported-label phase average
used in that actual computation, identified with the corresponding
selected conjugacy realization of
[PD.6](R133-supplement-complete-phase-row-approximate-inverse-and-quadratic-defect.md).
The original phase constant and true squared label weight remain.
It is not the fourth-mode physical Robin scalar of RNS.27.

The coordinate identification is explicit. In P.12 the same moving
return satisfies $H\circ P=H+\Omega_\star$. Put $g_0=H^{-1}$
and $J_0=g_0'\circ R$. Then

$$
 \left\langle\frac{f\circ g_0}{J_0}\right\rangle_x
 =\int H'(P(\phi))f(\phi)H'(\phi)\,\frac{d\phi}{\pi/2}.
                                                               \tag{PP.1a}
$$

Taking $f=DP[v_\nu,1]$, P.13 and D.6 give exactly PH's
transported-label integral. The physical waist-angle variation is
a coboundary only in this scalar average at the exact conjugacy;
its full pointwise row is still P.11 and is not deleted here.

The strict particular $v_\nu$ is the full infinite-dimensional
solution, not its finite NP trial. In the original moving body
coordinates it solves $D_Qv_\nu=F_\nu$, is identically zero for
$r\ge9/50$, and has the original zero state jumps. Thus it extends
to the entire original body with zero parameter residual there.
Its moving and physical means at the waist are not set to zero.
Its passive position/frame variation is the genuine lift in
[RH](R147-supplement-relative-height-carriers-and-short-full-frequency-errors.md),
with zero independent terminal ports only when defining this
particular column. Other independent ports remain variables in the
full system. In particular a nonlocal height row need not vanish.

The result and constants here remain on that same original selected
background. They have not been transferred for free to a new compact
mean-exact centre or an entire varying chart family.

## PP2. Keep the full raw phase equation while extracting its average

Use PD's exact signs and variables:

$$
 D\mathcal R[h,\kappa]=Ah-N_\nu\kappa,\qquad
 \delta E=J\{Lh+b_\nu\kappa+a-a\circ R\}+E'a .          \tag{PP.2}
$$

The original regular residual $\mathcal R$ still contains the
physical fourth-mode Robin equation, full body, cap, waist, jump,
height and independent mean rows. The raw phase target is a whole
function $b$. Set $\sigma=\langle b/J\rangle$,
$P_0f=f-\langle f\rangle$, and $u=(h,a)$, with PD's stated
linear constant-gauge convention for $a$. Define

$$
\begin{aligned}
 \mathcal A u&=
 \left(Ah,\ P_0[Lh+a-a\circ R+(E'/J)a]\right),\\
 g&=\left(-N_\nu,\ P_0b_\nu\right),\\
 \ell u&=\langle Lh+(E'/J)a\rangle,\qquad
 \omega=\langle b_\nu\rangle,\\
 f_{\rm all}&=(f,P_0(b/J)).                              \tag{PP.3}
\end{aligned}
$$

The original augmented equation is then exactly

$$
       \mathcal A u+g\kappa=f_{\rm all},\qquad
       \ell u+\omega\kappa=\sigma .                     \tag{PP.4}
$$

No average of $E'a/J$ has been set to zero. Dividing the current
linearized row by the true $J$ does not replace the nonlinear
residual $E$ by $E/J$. The nonmean phase equation, including
the cohomological operator and its small-divisor obligations, is
explicitly in $\mathcal A$.

## PP3. Shift by the particular and use the actual positive pivot

Let $Z_\nu=(v_\nu,0)$, including the passive lift and the actual
other state components induced by this chosen particular. Put

$$
 u=z+\kappa Z_\nu,\qquad
 r_\nu=\mathcal A Z_\nu+g
 =\left(Av_\nu-N_\nu,\ P_0[b_\nu+Lv_\nu]\right).        \tag{PP.5}
$$

Only the body/jump entries already solved by the true strict
particular vanish in $r_\nu$. Its complete regular boundary,
waist, mean, physical-coordinate and height entries, and its entire
nonmean phase function, remain. In particular the first component
is not declared zero by the PDE-only particular construction.

By (PP.1), $\omega+\ell Z_\nu=c>0$. Hence (PP.4) is equivalent
to the single complete reduced equation and reconstruction

$$
\boxed{
 \left(\mathcal A-r_\nu c^{-1}\ell\right)z
       =f_{\rm all}-r_\nu c^{-1}\sigma,\qquad
 \kappa=c^{-1}(\sigma-\ell z),\qquad
 u=z+\kappa Z_\nu .}                                   \tag{PP.6}
$$

This is substitution, so it does not presume $A^{-1}$, a high
inverse or a finite determinant. The operator difference is one
rank-one term, but its output vector is the **complete** $r_\nu$,
not a selected subset of paid rows. All remaining finite/high cross
terms and both physical means stay in the reduced equation.

The identity first holds on the original compatible smooth core.
It yields a bounded-operator equivalence on a chosen realization
once $Z_\nu,r_\nu,\ell$ have their required bounds in those exact
spaces. The ordinary body phase dual below does not itself supply
$\ell$ on an unproved rough incoming realization.

This is distinct from claiming a nonzero full response Schur
$\langle b_\nu+LA^{-1}N_\nu\rangle$. If a true full regular
inverse is later used, its response generally differs from
$v_\nu$. Formula (PP.6) instead keeps that difference as the
entire retained regular defect and solves the corrected regular
operator. It also does not exchange a Robin row for the phase row.

## PP4. Parameter-dependent input charts and output normalizers

For every actual original row $i$, write its parameter entry after
the shift as
$r_{\nu,i}=\mathcal R_i v_\nu+d_{\nu,i}$, with the original
sign already included in $d_{\nu,i}$. Then (PP.6) applies that
whole entry. An endpoint metric derivative known to vanish does
not imply that a nonlocal or chart derivative vanishes.

Specifically, under the original parameter-dependent input chart
$y=\Xi(x,\nu)$,
[RNS.24--26](R133-supplement-actual-root-faithfulness-and-complete-incoming-parameter-Schur-reduction.md)
gives the exact Jacobian
$\left(\begin{smallmatrix}D&\partial_\nu\Xi\\0&1\end{smallmatrix}\right)$.
Its terms $B\partial_\nu\Xi$ and
$\ell\partial_\nu\Xi$ remain on their original sides.
A state-dependent left normalization also has its product derivative
acting on the nonzero base residual. Neither contribution is
absorbed into the physical response estimates below without its
own exact identification. A frozen constant coordinate at this one
base point is allowed only as that explicitly stated convention;
it is not a proof that the original chart derivative is zero.

## PP5. New bounds in the unchanged physical response target

Let $F=F_\nu^{\rm phys}$ denote exactly the physical even half-sum
density response of PO/ASB. This is one known response component of
the column, not the complete incoming vector. The completed
[ASB.9--12](R147-supplement-actual-short-parameter-errors-and-refined-signed-borders.md)
give

$$
 \|F\|_2<.0016047,\quad
 \|P_{|j|\ge97}F\|_2<5.330\,10^{-5},\quad
 \|B^{-1}F\|_2<.1696,\quad
 \|P_{|j|>2^{4608}}B^{-1}F\|_2<5.330\,10^{-5}.           \tag{PP.7}
$$

Here the unchanged original operator is
$B=\mathrm{Id}+(\Pi_+M_w\Pi_++\Pi_-M_w\Pi_-)I$.
It is neither a whole $PM_wP$ multiplier nor the density inverse
$C^{-1}$. Its target normalizer is not changed.
Dividing by the positive whole lower endpoint in (PP.1) proves

$$
\begin{gathered}
 \|F/c\|_2<.041426,\qquad
 \|P_{|j|\ge97}F/c\|_2<.001376,\\
 \|B^{-1}F/c\|_2<4.378268,\qquad
 \|P_{|j|>2^{4608}}B^{-1}F/c\|_2<.001376.                \tag{PP.8}
\end{gathered}
$$

Thus the known raw physical response part of the rank-one feedback,
restricted to the distributed ordinary body phase functional,
has complete bounds

$$
 \|(F/c)L_\Omega\|_{L^2_rL^2\to L^2}<.062139,
\quad
 \|P_{|j|\ge97}(F/c)L_\Omega\|_{L^2_rL^2\to L^2}<.002064,
                                                               \tag{PP.9}
$$

Here the displayed $L^2_r$ input is on $[0,9/50]$, extended
by zero to the full body. PH proved $\|L_\Omega\|<3/2$ on
exactly this support, including both means and all response modes.
No phase dual bound on unrestricted full-negative-body directions
is inferred from that short restriction. These bounds do not include any independent
phase-chart term or an unpriced $d_{\nu,i}$. They are not a high
Neumann test for the complete incoming map. In particular the
normalized finite complement $97\le|j|\le2^{4608}$ is retained;
the last tail estimate in (PP.8) cannot be moved down to cutoff97.

## PP6. A complete error for the normalized signed physical96 column

Let $s\in\mathbb R^{96}$ be the exact original uninﬂated NP
physical trial observation vector used in
[APO.2](R147-supplement-actual-physical-parameter-observation-inverse-and-high-tail.md),
with all its whole signed balls. Keep its original phases, signs
and $\sqrt2\cos(4j\theta)$ normalization. It is not the 194
inflated true observations or a new shifted physical frame.
Write $\mathcal O_{96}$ for those true orthonormal physical
observations. ASB pays

$$
 \|\mathcal O_{96}F-s\|_{\ell^2}<E:=6\,10^{-7},\qquad
 \|s\|_{\ell^2}<.0016047+E .                            \tag{PP.10}
$$

The second inequality follows from Bessel and the first; no
unobserved sine or mean energy is subtracted. Choose the exact
rational scalar $c_0=.03875244$. This is a computational
normalization only, not a declaration that the true pivot equals
its midpoint. Equation (PP.1) gives $|c-c_0|<.000015656$.
Consequently

$$
\begin{aligned}
 \left\|\frac{\mathcal O_{96}F}{c}-\frac{s}{c_0}\right\|_{\ell^2}
 &\le \frac{E}{.038736784}
 +\frac{.000015656\,(.0016047+E)}{.038736784\,.03875244}\\
 &<3.224\,10^{-5}.                                    \tag{PP.11}
\end{aligned}
$$

This is a joint96 error, not 96 separate copies of one norm. Future
finite assembly consumes the whole original signed balls divided
by $c_0$; selecting their centers would need the entire original
serialization/quadrature radius as an additional error. No old
pairing or observation inverse has been rerun to obtain (PP.11).

All six displayed new rational bounds are implemented in the
[saved-scalar consumer](../scripts/fourfold_codazzi_phase_pivot_saved_bounds.py).
It evaluates no scientific target. The remaining work is the
complete realization and inversion of the operator in (PP.6),
including all of $r_\nu$, the nonmean raw phase, the original
fourth Robin row, means, height, affine ports and the infinite
remainder. No completion of the topic is asserted here.
