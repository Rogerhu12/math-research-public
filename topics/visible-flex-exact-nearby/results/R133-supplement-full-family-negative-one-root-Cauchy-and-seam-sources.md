# R133 supplement: the complete negative-one root Cauchy window and true seam sources

2026-11-14, phase_inverse. **Proved energy estimate under an explicit
small public numerical gate.** This extends the already executed
root-to-negative estimate to output $H^{-1}$, with its actual
$H^{-2/3}$ ordinary-source window. The same full repaired family,
both original curvature rows and the independent even mean remain.

The numerical growth gate below requires its independent public
execution. No new numerical success, positive-side Sobolev estimate,
milliscale domain or cutoff-97 inverse is asserted here.

## 1. Same objects and regular root weight

Use precisely the real family, actual radial interval and whole
coefficient bounds in
[the complete root-to-negative Cauchy theorem](R133-supplement-full-family-root-to-negative-Cauchy-energy.md).
Thus $|\delta|\le10^{-8}$ is real, $\rho=r_*-r$ lies in
$[0,R]$, $R=9/10^6$, $q^2=-K$, and
$$
 (q^2)_\rho>59,\quad \eta<63/50,\quad
 q^2<61/10^5,\quad \theta^{-1}<4,\quad
 w\le W=\sqrt{1+\sup q^2}<1001/1000.                  \tag{N.1}
$$
The exact multipliers, on every frequency including zero, are
$$
 \Lambda_j=\sqrt{1+16j^2},\quad x=\rho\Lambda_j^{2/3},
 \quad w^2=q^2+\Lambda_j^{-2/3}e^{-x},\quad
 \theta=\exp[-(63/50)(1-e^{-x})].
$$
Write $M=\operatorname{diag}(\theta/w,\theta)$ as in that theorem,
but now use the complete energy variable
$$
                 Z_{-1}=\Lambda^{-1}Mh .             \tag{N.2}
$$
Since $\Lambda$ commutes with every radial Fourier multiplier and
with the constant-angular principal operator, the principal
skew part and the dissipative cancellation are exactly unchanged.
In particular the unbounded frequency supremum near $\rho=0$
is still not integrated.

At the root,
$$
 \|Z_{-1}(0)\|^2
 =\|h_1(0)\|_{H^{-2/3}}^2+\|h_2(0)\|_{H^{-1}}^2 .
                                                               \tag{N.3}
$$
Everywhere on the interval,
$$
 \|h\|_{H^{-1}\times H^{-1}}\le4W\|Z_{-1}\|,\qquad
 \|(\Lambda^{-1}M)g\|
       \le\|g\|_{H^{-2/3}\times H^{-2/3}} .           \tag{N.4}
$$
The sharper anisotropic source norm
$(H^{-2/3},H^{-1})$ is also valid. We retain the common isotropic
window in the displayed final estimate.

## 2. Repaid multiplier and transport costs

The two original $M_\nu$ have logarithmic derivative in
$[-1/3,1/3]$. For $W_\nu=\Lambda^{-1}M_\nu$ it therefore lies
in $[-4/3,-2/3]$. If the physical Fourier lag is $\ell$, then
$$
 {W_\nu(k+\ell)\over W_\nu(k)}
       \le(1+|\ell|)^{4/3},\qquad
 |k|\left|{W_\nu(k+\ell)\over W_\nu(k)}-1\right|
       \le\tfrac43|\ell|(1+|\ell|)^{4/3}.             \tag{N.5}
$$
For the second bound compare the larger and smaller Bessel
frequencies, use $t^{4/3}-1\le(4/3)t^{4/3}(1-t^{-1})$,
and $|\Lambda(k+\ell)-\Lambda(k)|\le|\ell|$.

The complete family has degree 96; quadratic local coefficients
have degree 192 and physical lags at most 768. Hence
$(1+|\ell|)^{4/3}<10(1+|\ell|)$. Young convolution gives
$$
 \|W_\nu a W_\nu^{-1}\|
 \le10(\|a\|_{\mathcal A_0}+\|a_\phi\|_{\mathcal A_0}),\quad
 \|[W_\nu,d]W_\nu^{-1}\partial_\phi\|
 \le\tfrac{40}3(D_1+D_2),                            \tag{N.6}
$$
where $D_j=\|\partial_\phi^j d\|_{\mathcal A_0}$.
Together with the real transport energy, the drift fee is
$$
                   L_d=\tfrac12D_1+\tfrac{40}3(D_1+D_2).
                                                               \tag{N.7}
$$
The factor $4/3$ in the commutator must be retained; the old
concave exponent $1/3$ estimate cannot simply be relabelled.

Let $U_j,V_j$ be the original complete ordinary angular Wiener
bounds, controlled by the saved positive-width bounds. Sufficient
complete local norms and first derivatives are
$$
 A_0=|b|(1+3U_0^2+q_{\max}^2V_0^2),\quad
 A_1=|b|(6U_0U_1+2q_{\max}^2V_0V_1),
$$
$$
 E_0=|b|(1+U_0^2+3q_{\max}^2V_0^2),\quad
 E_1=|b|(2U_0U_1+6q_{\max}^2V_0V_1),
$$
$$
 L_0=2|b|U_0V_0,\quad
 L_1=2|b|(U_1V_0+U_0V_1).
$$
Using (N.6) on the two diagonal blocks costs
$10(A_0+A_1+E_0+E_1)$.
For the off-diagonal blocks, commute only the radial multipliers:
$q^2/w\le q_{\max}$ and $w\le W$, while
$$
 \|\Lambda^{-1}a\Lambda\|
 \le\|a\|_{\mathcal A_0}+\|a_\phi\|_{\mathcal A_0}.
$$
Their complete cost is at most
$4(q_{\max}+W)(L_0+L_1)$. Thus
$$
 L_{\rm loc}=10(A_0+A_1+E_0+E_1)
                         +4(q_{\max}+W)(L_0+L_1).     \tag{N.8}
$$
No local coefficient has been commuted freely past $w$ or $\theta$.

## 3. The actual primitive and independent mean

The old primitive satisfies the exact full bound
$$
 \|I\|_{H^{-1}\to L^2}=\sqrt{17}/4=:C_I .             \tag{N.9}
$$
The maximum is at the first nonzero physical frequency 4;
the zero mode is annihilated only by this primitive.
For a multiplier $a$, its $H^{-1}$ norm is bounded by
$\|a\|_{\mathcal A_0}+\|a_\phi\|_{\mathcal A_0}$.
Since $W_1\le\Lambda^{-2/3}$ and $W_2\le\Lambda^{-1}$,
the exact ordered term
$-2b(u_\phi,v_\phi)^T I(uh_1+Kvh_2)$ has the sufficient fee
$$
 L_I=8|b|C_I(U_1+V_1)
                 \{W(U_0+U_1)+q_{\max}^2(V_0+V_1)\}. \tag{N.10}
$$
Indeed first bound its interior in $H^{-1}$, apply (N.9), and
then bound the two exterior multiplications in ordinary $L^2$.
Their negative output weights are contractions. This retains
the precise order of every original operator.

The original mean-rank term is
$\gamma z(Kv_\phi,-u_\phi)$, with $z=\Pi h_2$.
The zero-frequency weight is included in (N.2), so
$|z|\le4\|Z_{-1,2}\|$. Its complete fee is
$$
                  L_\Pi=4\gamma(q_{\max}^2V_1+U_1).   \tag{N.11}
$$
The local equation of the even mean was already included in
(N.8). The term (N.11), its independent ordinary source and
the full nonmean response to it are not removed.

Use
$$
 D_1\le |b|(U_0^2+q_{\max}^2V_0^2),\qquad
 D_2\le2|b|(U_0U_1+q_{\max}^2V_0V_1).
$$
The independent consumer evaluates (N.7)--(N.11) from the two
original complete native files, with no new target or response solve.
Its proposed gates are
$$
 L_{\rm loc}+L_d+L_I+L_\Pi<112,\qquad
       4W e^{112R}<41/10,\qquad (41/10)C_I<17/4 .     \tag{N.12}
$$
The bounds are to be activated only by actual public execution.

## 4. Full source and affine seam theorem

Assume (N.12). The energy inequality is
$$
 \frac{d}{d\rho}\|Z_{-1}\|
 \le112\|Z_{-1}\|+
                    \|g\|_{H^{-2/3}\times H^{-2/3}} .
$$
Consequently
$$
 \boxed{\;
 \sup_{0\le\rho\le R}\|h(\rho)\|_{H^{-1}\times H^{-1}}
 \le\frac{41}{10}\left[
 (\|h_1(0)\|_{H^{-2/3}}^2+\|h_2(0)\|_{H^{-1}}^2)^{1/2}
       +\frac3{1000}\|g\|_{L^2_\rho(H^{-2/3}\times H^{-2/3})}
                  \right].\;}                       \tag{N.13}
$$
Use non-strict inequalities for zero data. The Galerkin proof,
uniform energy limit and uniqueness are exactly the full-frequency
argument of the original theorem, now in these declared spaces.
There is no finite Fourier restriction on the state or source.

If the true state has prescribed affine jumps $j_a=(j_{1,a},j_{2,a})$
at real interior radial interfaces $\rho_a$, add inside the brackets
$$
 \sum_a\|W(\rho_a)j_a\|
 \le\sum_a
    (\|j_{1,a}\|_{H^{-2/3}}^2+\|j_{2,a}\|_{H^{-1}}^2)^{1/2}.
                                                               \tag{N.14}
$$
The same exponential bound covers every ordered subinterval.
This is a genuine impulse/source estimate, not a claim that a
formal order of a seam jump already bounds its norm. It also
applies when a finite trial is corrected by the opposite jumps.

Applying the original primitive after propagation yields
$$
 \sup_\rho\|Ih(\rho)\|_{L^2\times L^2}
 \le\frac{17}{4}\,[\text{the complete bracket in (N.13)--(N.14)}].
                                                               \tag{N.15}
$$
This is useful for density errors: an input gain measured in
$H^{-1}$ survives the actual full propagation. It does not assume
that a propagated column retains its original Fourier support.
Any additional strict wave gauge, multiplier, composition or
normalizer at the final trace still needs its own bounded map.

This estimate concerns only the already paid $9\cdot10^{-6}$
negative root interval and the real explicit family. It neither
extends the positive Green map to a lower source window nor
certifies a larger radial domain. In particular positive-side
ordinary sources still use their previously paid $H^{1/3}$
contract until a separate estimate is proved.
