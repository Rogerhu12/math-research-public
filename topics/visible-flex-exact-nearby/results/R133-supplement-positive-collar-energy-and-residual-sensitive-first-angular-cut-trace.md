# R133 supplement: exact positive-collar energy and a residual-sensitive first-angular cut trace

2026-11-15. Analytic lemma for a real approximate moving state on a
two-sided positive collar. The full ordinary residual and both means are
included. The lemma applies before the PDE residual vanishes; it does
not assume that a core solution or a nonlinear core graph already exists.

No numerical target or old certificate is recomputed. The displayed
constants are explicit functions of genuine collar coefficient bounds.
The last section identifies the remaining inputs needed to turn this
lemma into a quantitative high-order inner-data gate.

## 1. Actual equation and the required two-sided domain

Let
$$
 I=[c-2\ell,c+2\ell],\qquad \ell>0,\qquad K(r)>0,\quad G(r)>0 ,
 \tag{E.1}
$$
be a true positive interval, with the original moving angle $\phi$ of
period $\pi/2$. In the intended application $c=9/10$ is an artificial
cut. Both sides of this cut must be part of the **same** approximate
state on $I$.

All angular $L^2$ norms use the normalized circle measure
$(2/\pi)\,d\phi$; radial integrals use the true measure $dr$.
Use the exact raw moving equation from
[the complete moving operator](R133-supplement-negative-quadratic-density-and-full-frequency-transport.md),
with an ordinary residual:
$$
 \begin{split}
 Q_r&=dQ_\phi+GmJ(K)Q_\phi
                    +\beta DQ-\beta S Q+f,\\
 Q&=(u,v)^t,\quad m=\langle v\rangle_\phi,\quad
 S=u^2+Kv^2,\quad d=-\beta I_\phi S,\\
 J(K)&=\begin{pmatrix}0&K\\-1&0\end{pmatrix},\qquad
 D=\operatorname{diag}(-1,1),\qquad
 I_\phi=\partial_\phi^{-1}P_{\ne0,\phi}.
 \end{split}
 \tag{E.2}
$$
Here $f=Q_r-\mathcal F(Q)$ has its actual ordinary moving units.
The $\nu$ bump, if changed, belongs to the genuine coefficient triple
$(\beta,G,K)$; a difference of two metrics cannot be silently put into
a same-coefficient comparison below.

Assume the coefficient functions are continuous and piecewise
$W^{1,\infty}$ on their genuine radial partition, with their actual
one-sided derivative bounds. Assume $Q$ is real, is continuous across
the radial seams, and is sufficiently regular on each open piece for
the displayed integrations and one angular differentiation. Finite
smooth angular Nash iterates satisfy this regularity assumption.
The resulting inequalities also pass through justified Sobolev
approximation with the stated bounds.

The mean is required to retain its actual sign and gap,
$$
                            m(r)<0 .
 \tag{E.3}
$$
A merely positive reference speed is not a substitute for this
condition on the actual state.

The complete circle mean of (E.2) gives
$$
 \begin{split}
 \langle u\rangle_r
       &=-\beta(1+\langle S\rangle)\langle u\rangle+\langle f_1\rangle,\\
 m_r&=\beta(1-\langle S\rangle)m+\langle f_2\rangle .
 \end{split}
 \tag{E.4}
$$
For example $\langle d v_\phi\rangle=-\langle d_\phi v\rangle
=\beta\langle Sv\rangle-\beta\langle S\rangle m$, which cancels the
other cubic mean term. The angular principal term has zero mean.
Thus (E.4) does not require parity and does not set either residual
mean equal to zero.

## 2. Exact radial scaling and the real energy identity

Put
$$
 P(r)=\operatorname{diag}(K^{-1/4},K^{1/4}),\quad W=PQ,\quad
 J_0=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
$$
$$
 b=\beta\sqrt K,\quad
 \alpha=\beta+\frac{K_r}{4K},\quad
 g=GK^{1/4},\quad
 a=-Gm\sqrt K=-g\langle W_2\rangle>0.
 \tag{E.5}
$$
The letter $a$ in this lemma denotes this principal speed only; it is
not the physical radial coordinate used in the exterior geometry.

Since $PJ(K)P^{-1}=\sqrt KJ_0$ and
$P_rP^{-1}=(K_r/4K)D$, (E.2) is exactly
$$
 \mathcal L W=\alpha DW-b|W|^2W+Pf,\qquad
 \mathcal L=\partial_r-d\partial_\phi+aJ_0\partial_\phi,\qquad
 d=-bI_\phi(|W|^2).
 \tag{E.6}
$$
The square $|W|^2=W_1^2+W_2^2$ is the real pointwise square.
All coefficients in the principal part are real.

The logarithmic radial derivative of the speed is also exact:
$$
 \frac{a_r}{a}
 =\frac{G_r}{G}+\frac{K_r}{2K}
       +\beta(1-\langle S\rangle)+\frac{\langle f_2\rangle}{m}.
 \tag{E.7}
$$
In particular a near-solution has the last term in (E.7). The formula
for a true solution is obtained by setting its actual residual to zero;
it cannot be used prematurely on an iterate.

Let $z$ be compactly supported in the interior of $I$ and continuous
through every true radial seam. Real-part pairings below also allow
complex test vectors $z$ against these real coefficients. Since $J_0$
is skew symmetric,
$$
 2\operatorname{Re}\int_I
       \langle-dz_\phi,aJ_0z_\phi\rangle_\phi\,dr=0.
$$
The operator $J_0\partial_\phi$ is self adjoint. Integration by parts
in $r$ consequently gives
$$
 \begin{split}
 &2\operatorname{Re}\int_I
       \langle(\partial_r-d\partial_\phi)z,aJ_0z_\phi\rangle_\phi\,dr\\
 &\hspace{25mm}
       =-\int_I a_r\langle z,J_0z_\phi\rangle_\phi\,dr .
 \end{split}
 \tag{E.8}
$$
There is no angular derivative of $d$ in (E.8), and no radial derivative
of $d$ is needed. This is an identity of the complete two-row system,
not an estimate on one positive branch.

Suppose on this actual collar that
$$
 a\ge a_->0,\qquad
 \|d\|_\infty\le d_+,\qquad
 \left\|\frac{a_r}{a}\right\|_\infty\le L .
 \tag{E.9}
$$
Young's inequality in (E.8) yields
$$
 \|(\partial_r-d\partial_\phi)z\|_2^2
       +\frac12\|az_\phi\|_2^2
 \le\|\mathcal Lz\|_2^2+\frac{L^2}{2}\|z\|_2^2 .
 \tag{E.10}
$$
Every norm in (E.10) is the actual ordinary $L^2_{r,\phi}$ norm.
If
$$
                         E=\|\mathcal Lz\|_2+L\|z\|_2,
$$
then
$$
 \|z_\phi\|_2\le\frac2{a_-}E,\qquad
 \|z_r\|_2\le\left(1+\frac{2d_+}{a_-}\right)E .
 \tag{E.11}
$$
The unknown drift derivative has not been treated as a bounded
zero-order operator. Its cancellation is confined to the exact
real energy pairing (E.8).

The coefficient $L$ in (E.9) may be supplied directly, or from (E.7)
using a genuine bound for $\langle f_2\rangle/m$. For instance an
$L^\infty_r$ bound for that scalar residual suffices. A small ordinary
$L^2$ residual alone is not relabelled as that $L^\infty$ bound.

## 3. Difference from a fixed reference, with its nonzero residual

Let $Q^0$ be any real continuous reference on the same collar and with
the **same** $(\beta,G,K)$. Its ordinary residual is
$f^0=Q^0_r-\mathcal F(Q^0)$ and need not vanish. Define
$$
 W^0=PQ^0,\qquad z=P(Q-Q^0)=W-W^0,\qquad
 F=P(f-f^0),\qquad B=W+W^0.
 \tag{E.12}
$$
The speed and drift in $\mathcal L$ continue to be those of the actual
state $Q$, not of a convenient independent radial reference.

Subtracting the two complete equations gives
$$
 \begin{split}
 \mathcal Lz={}&\alpha Dz
       -b\{|W|^2z+W^0(B\cdot z)\}\\
       &-bW^0_\phi I_\phi(B\cdot z)
       +g\langle z_2\rangle J_0W^0_\phi+F .
 \end{split}
 \tag{E.13}
$$
In particular the last rank-one term is the actual principal mean
variation. It cannot be omitted because an angular primitive occurs
elsewhere in the formula.

Introduce genuine bounds, uniform over the collar,
$$
 |W|,|W^0|\le M,\qquad
 |W^0_\phi|\le M_1,\qquad
 |W^0_{\phi\phi}|\le M_2,
$$
$$
 |\alpha|\le\alpha_+,\qquad |b|\le b_+,\qquad |g|\le g_+ .
 \tag{E.14}
$$
Here vector absolute values are Euclidean. Complete pair Wiener bounds
may be used to provide these supremum bounds, but a pointwise bound is
not used as a joint Wiener bound.

The multiplication and mean maps in (E.13), together with
$\|I_\phi\|_{L^2\to L^2}=1/4$, imply
$$
 \|\mathcal Lz-F\|_{L^2_\phi}\le A_0\|z\|_{L^2_\phi},\qquad
 A_0=\alpha_++3b_+M^2+(b_+M/2+g_+)M_1 .
 \tag{E.15}
$$
This bound is pointwise in $r$ and hence integrates in the actual
ordinary radial measure. It includes the full mean.

## 4. One angular derivative costs only low state bounds

For use at the true cut one needs the first derivative of (E.13).
Write $p=z_\phi$. The highest derivative terms are
$$
 \begin{split}
 \mathcal Lp={}& A_1(r,\phi)p+\mathcal B_{10}z+F_\phi,\\
 A_1={}&d_\phi I+\alpha D
        -b\{|W|^2I+2WW^t\},
 \end{split}
 \tag{E.16}
$$
where the complete lower-order operator is
$$
 \begin{split}
 \mathcal B_{10}z={}&
 -b\{W^0_\phi(B\cdot z)+2z(W\cdot W^0_\phi)
                                  +2W^0(W^0_\phi\cdot z)\}\\
 &-bW^0_{\phi\phi}I_\phi(B\cdot z)
       -bW^0_\phi P_{\perp,\phi}(B\cdot z)
       +g\langle z_2\rangle J_0W^0_{\phi\phi}.
 \end{split}
 \tag{E.17}
$$
For the local cubic one can check the entire split directly from
$N(W)=|W|^2W$:
$$
 \partial_\phi\{N(W)-N(W^0)\}
  =DN(W)z_\phi+\{DN(W)-DN(W^0)\}W^0_\phi,
 \qquad DN(W)=|W|^2I+2WW^t.
$$
The derivative of the primitive is exactly the full nonmean projection.
No derivative of an unknown product is left inside that primitive.

Since
$d_\phi=-b(|W|^2-\langle|W|^2\rangle)$, it has size at most
$2b_+M^2$. Thus
$$
 \|A_1\|_\infty\le A_1^+:=\alpha_++5b_+M^2,\qquad
 \|\mathcal B_{10}\|_{L^2_\phi\to L^2_\phi}
       \le B_{10}:=8b_+MM_1+(b_+M/2+g_+)M_2 .
 \tag{E.18}
$$
Only the actual state's $C^0$ bound occurs in (E.18). The two angular
derivatives in $M_1,M_2$ belong to the fixed reference, whose full
coefficient content remains available. In particular this is not a
bootstrap assumption that the unknown already has a controlled
$H^2$ norm.

For the repaired explicit reference and its fixed finite parameter
direction, $M_2$ can be supplied from their complete finite angular
support and true coefficient envelopes. This does not truncate $z$.

## 5. A complete quantitative $H^1$ trace inequality at the interior cut

Set
$$
 I_1=[c-\ell,c+\ell],\qquad
 I_2=[c-\ell/2,c+\ell/2].
$$
Take real radial cutoffs equal to one on $I_1$ and $I_2$, respectively,
with supports in $I$ and $I_1$, and derivative bounds $1/\ell$ and
$2/\ell$. Piecewise linear cutoffs suffice by approximation.

All norms in the next definitions are over $I\times S^1_{\pi/2}$:
$$
 Z=\|z\|_2,\qquad F_0=\|F\|_2,\qquad F_1=\|F_\phi\|_2,
$$
$$
 E_0=F_0+(A_0+L+\ell^{-1})Z,\qquad
 E_1=F_1+B_{10}Z
                +(A_1^++L+2\ell^{-1})\frac2{a_-}E_0 .
 \tag{E.19}
$$
Using (E.11) first on the cutoff of $z$ and then on the cutoff of $p$
gives
$$
 \begin{aligned}
 \|z_\phi\|_{L^2(I_1)}&\le2E_0/a_-,&
 \|z_r\|_{L^2(I_1)}
                 &\le(1+2d_+/a_-)E_0,\\
 \|(z_\phi)_r\|_{L^2(I_2)}
                 &\le(1+2d_+/a_-)E_1,&
 \|z_{\phi\phi}\|_{L^2(I_2)}&\le2E_1/a_- .
 \end{aligned}
 \tag{E.20}
$$
All full means in these estimates are the actual ones; differentiating
the first component does not remove the independent undifferentiated
second mean already controlled by $Z,E_0$.

For a Hilbert-valued function on the interval $I_2$ of length $\ell$,
averaging its fundamental-theorem-of-calculus identity gives
$$
 \|w(c)\|\le\ell^{-1/2}\|w\|_{L^2(I_2)}
                              +\ell^{1/2}\|w_r\|_{L^2(I_2)} .
$$
Applying it to $z$ and $z_\phi$ proves
$$
 \boxed{\quad
 \begin{split}
 \|z(c)\|_{H^1_\phi}
 \le{}&\ell^{-1/2}\bigl(Z+2E_0/a_-\bigr)\\
      &+\ell^{1/2}(1+2d_+/a_-)(E_0+E_1).
 \end{split}
 \quad}
 \tag{E.21}
$$
For the actual raw moving trace the final radial normalization is
$$
 \|(Q-Q^0)(c)\|_{H^1_\phi}
 \le p_c\|z(c)\|_{H^1_\phi},\qquad
 p_c=\max\{K(c)^{1/4},K(c)^{-1/4}\}.
 \tag{E.22}
$$
Likewise one may bound $Z,F_0,F_1$ by the corresponding raw norms using
the explicitly retained
$\sup_I\max(K^{1/4},K^{-1/4})$. These are ordinary moving units; no
physical-angle pullback is required in (E.21).

This proves an interior trace estimate for an approximate core
iterate with its full ordinary residual difference. It does not use
the positive-cap boundary input as if it were an interior value.

## 6. Seams, nonmatching boundary states, and the higher-order task

The seam condition is substantive. If $z$ or the principal speed has a
true jump, integrating the left side of (E.8) piece by piece additionally
produces the complete interface forms
$$
 \sum_{r_i}\left[
 a(r_i^-)\langle z^-,J_0z_\phi^-\rangle
       -a(r_i^+)\langle z^+,J_0z_\phi^+\rangle\right].
 \tag{E.23}
$$
They vanish for the continuous same-state collar used above. They do
not vanish for two independent one-sided states merely because their
cut is artificial. An arbitrary $L^2$ boundary jump is not an ordinary
$L^2_r$ source, and (E.21) does not turn it into a smooth trace. Such a
jump must be lifted with its actual angular regularity, or kept as a
separate boundary form.

For the current exact repaired reference, all reference state joins
are genuinely continuous. New iterates must satisfy this condition
themselves, or supply their own jump data. A centre's continuity does
not certify another trial's interfaces.

Equation (E.21) is the first-angular gate needed in the physical
inner-curvature conversion. If actual collar bounds and actual iterate
source/body bounds make its right side at most $10^{-9}/128$, the full
physical zero-width curvature radius follows from that conversion.
No current core estimate is asserted here to satisfy this numerical
inequality.

Higher angular differentiation has the same principal energy (E.8).
It retains the exact mean variation and the full differentiated
ordinary source; it cannot be inferred from a small low-order
residual alone. In particular, to obtain a uniform $H^{8193}$ trace
for a family of approximate iterates, one must either pay the
corresponding complete high source bounds and the ordered nonlinear
product recursion, or prove a more specific smoothing mechanism.
A high norm that is merely finite at every step is not a uniform
inner-data ball. The present lemma does not yet grant that high gate.

For a true residual-zero limit, (E.7) and the differentiated equation
simplify, but the existence of that limit and the whole-core matching
are not prerequisites silently inserted into the approximate-state
estimate proved above.
