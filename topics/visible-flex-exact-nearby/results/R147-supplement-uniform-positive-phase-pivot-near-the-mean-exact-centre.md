# R147 CP: a uniform positive phase pivot near the mean-exact centre

2026-11-27, visible-exact-astra-fb31ed6-20261127 / positive_inverse.

**Proved from completed whole bounds and the complete return Hessian.**
The original finite NP particular, used as a candidate column with its
entire current regular defect retained, gives a positive PD phase pivot
at the mean-exact centre on the actual selected metric. At that centre
and with the original true conjugacy its scalar is greater than $1/50$.
On the full Fourier neighbourhood specified in (CP.13), including a
metric interval and an unfixed constant phase, the same candidate gives

$$
             \frac1{60}<S(Q,\nu,g)<\frac3{50},
             \qquad S(Q,\nu,g)^{-1}<60.                 \tag{CP.1}
$$

This supplies the actual scalar hypothesis PD.7 for that candidate on
that neighbourhood. It does not assert that the candidate solves the
current regular equations. Their full residual, both means, the
physical fourth Robin row, nonmean phase and the raw $E'a$ term remain.
No old NP, phase, propagation, norm or pairing target is evaluated again.

## CP1. The unchanged candidate and the exact phase chart

Write $(Q_*,\nu_*)=(Q_{\delta_*},\nu_0+\delta_*)$ for the original
selected member at the actual fixed $\eta_0$. Let $h^a$ be the exact
original NP degree96 trial, including its true two means and all
original radial pieces; extend it by zero above $b=9/50$. The
[complete APHI receipt](R147-supplement-actual-nonzero-phase-border-of-the-strict-parameter-particular.md)
identifies all four restored $740$ by $193$ original arrays and the
whole trial-definition SHA256
83da6322dbb4702fe6ae308acbcfb7bb1ed9410d17e0cded65bc1215dec233db.
No new trial is selected here. Its complete actual state jumps are zero.

Let $H$ be W's actual selected conjugacy, with its original constant
phase, and let $g_0=H^{-1}$. In exactly
[P.12--15](R133-supplement-full-regular-phase-counterterm-and-actual-error-functional.md),

$$
 H\circ P(Q_*,\nu_*)=H+\Omega_\star,\qquad
 J_0=g_0'\circ R,\qquad R(x)=x+\Omega_\star .
                                                               \tag{CP.2}
$$

Here $P=H_-^{-1}\circ H_+$ is the original moving-angle principal
return, not one outgoing ray and not a fitted physical return. For
any variation $f$ of this return define

$$
 \Lambda_g f=\left\langle\frac{f\circ g}{g'\circ R}\right\rangle_x .
                                                               \tag{CP.3}
$$

Changing variables $x=H(\phi)$ gives
$\Lambda_{g_0}f=\int H'(P(\phi))f(\phi)H'(\phi)\,d\phi/(\pi/2)$.
Thus P.13 and the exact two-ray identity D.6 identify
$\Lambda_{g_0}DP[v_\nu,1]$ with APHI's actual squared-label integral.
This coordinate identity keeps the original phase constant. The
physical waist-angle derivative is a coboundary only in that scalar
average at the exact conjugacy; no complete physical row is discarded.

At any current state and degree-one lift, define the **candidate**
phase scalar

$$
 S(Q,\nu,g)=\Lambda_g\bigl(DP(Q,\nu)[h^a,1]\bigr).       \tag{CP.4}
$$

This is exactly $\langle b_\nu+Lh^a\rangle$ in PD.6 with the current
$J=g'\circ R$. Dividing this current linearized row by $J$ does not
replace the nonlinear raw phase residual $E=P\circ g-g\circ R$ by
$E/J$. No conjugacy condition at the current state is assumed.

## CP2. A new bound for the entire fixed trial in the RP direction norm

We need the norm of the complete original trial, rather than the norm
of one waist trace or of its finite nonmean projection. The exact
full parameter source from
[S.8--12](R133-supplement-complete-nu-adjoint-and-dual-residual-Schur.md)
is

$$
\begin{gathered}
 F_\nu=w'A_\nu+wB_\nu,\quad
 T=\frac{\beta}{2a^2\gamma^2},\quad
 {\mathscr W}=I(v^2)Q_\phi+v^2Q,\\
 A_\nu=-\beta T{\mathscr W}+\gamma mT(v_\phi,0),\\
 B_\nu=\beta K{\mathscr W}
                  -\frac{\gamma m}{2}(Kv_\phi,u_\phi).
\end{gathered}                                                   \tag{CP.5}
$$

Every product is formed before taking any mean. In particular the
second mean in S.11 remains. The exact bump is supported on
$C=[1/20,9/50]$, increases from zero to one and then decreases to zero,
and satisfies

$$
                  \int_C|w'|\,dr=2,\qquad
                  \int_Cw\,dr=\frac{256}{5775}.          \tag{CP.6}
$$

Use only the original selected bounds already collected in
[RH.2--4](R147-supplement-relative-height-carriers-and-short-full-frequency-errors.md):
$|\beta|<B=211/1000$, $\gamma<G=28/25$, $|K|<K_*=21/20$,
$\gamma>1$, and $\sqrt{u^2+q^2v^2}<239/125$ with $q>.5338$.
They imply the pair bound $|Q|<V=18/5$ and $|m|<V$.
The complete original raw derivative bound $5.437241$, repaired by
less than $1.970\,10^{-17}$ and changed by less than $83\,10^{-10}$,
gives $|Q_\phi|<Q_1=5.438$ on the selected member
([D.4--6](R133-supplement-exact-selected-parameter-core-differences-and-finite193-transfer.md)).
These are full bounds, not selected Fourier samples.

SP's complete waist physical-radius lower is larger than $1.068$.
Since $a'/a=\beta$,

$$
 a(r)>1.068e^{-Bb}\ge1.068(1-Bb)>1,\qquad |T|<B/2.       \tag{CP.7}
$$

The full fourfold primitive satisfies $\|I\|_{\infty\to\infty}<2/5$.
Consequently the following are complete pair bounds:

$$
\begin{aligned}
 W_*&=\tfrac25V^2Q_1+V^3,\\
 A_*&=\tfrac12B^2W_*+\tfrac12GVBQ_1,\\
 B_*&=BK_*W_*+\tfrac12GVK_*Q_1,\\
 \|F_\nu\|_{L^1_rL^2_\phi}
 &\le2A_*+\frac{256}{5775}B_*<10 .
\end{aligned}                                                   \tag{CP.8}
$$

Normalized angular $L^2$ is bounded by the displayed pointwise pair
norm. No direct metric or mean summand in (CP.5) has been omitted.
The source is ordinary on its original pieces; the compact bump adds
no endpoint impulse.

The completed [ASB](R147-supplement-actual-short-parameter-errors-and-refined-signed-borders.md)
receiver, proved for every full ordinary source by SB.13--16, is
$V_b<7.501268$. It includes all shorter ordered products and both
means on $[0,b]$. The true zero-terminal particular therefore obeys
$\|v_\nu\|_{L^\infty_rL^2}<7.501268\,10$.
ASB also gives its complete trial error
$\|v_\nu-h^a\|_{L^2_rL^2}<6.765672\,10^{-6}$.
As $\sqrt b<17/40$,

$$
 \|h^a\|_{L^2([0,r_*];L^2)}
 <\frac{17}{40}(7.501268)(10)+6.765672\,10^{-6}
 <32,\qquad N(h^a,1)<132.                              \tag{CP.9}
$$

The zero extension above $b$ is used here. The norm is the original
raw pair including both means; no inverse primitive is used. Only
this newly needed consequence of the saved receiver is formed.

## CP3. The selected starting scalar and the fixed averaging norm

APHI and PH's paid ordinary response dual give

$$
\begin{gathered}
 c_*=\Lambda_{g_0}DP(Q_*,\nu_*)[v_\nu,1]
            \in(.038736784,.038768096),\\
 |S(Q_*,\nu_*,g_0)-c_*|<1.014851\,10^{-5}.
\end{gathered}                                                   \tag{CP.10}
$$

The second statement applies PH's complete short-supported
$L^2_rL^2$ phase functional to $h^a-v_\nu$. It includes the full
infinite response error and the mean. It is not an assertion that
the finite trial is the true response.

The whole original complete derivative Wiener sum, retained in
PO run45903437912/1 at the copied original bound H1, is
$[1.0163840908329291811266507432489826\ \mathord{\pm}\ 4.77\,10^{-35}]$.
Its constant coefficient is exactly one. Thus

$$
 \frac{31}{32}<H'<\frac{33}{32},\quad
 \frac{32}{33}<g_0'<\frac{32}{31},\quad
 \|\Lambda_{g_0}\|_{L^2\to\mathbb R}
 \le(33/32)^{3/2}<21/20.                               \tag{CP.11}
$$

Indeed $1/(g_0'\circ R)\le33/32$, while the exact substitution
$x=H(\phi)$ gives $\|f\circ g_0\|_2\le\sqrt{33/32}\|f\|_2$.
Both factors belong to this same $H$; no compound angle map is
substituted for it.

## CP4. Transfer to the actual mean-exact centre

Let $\widetilde Q_*=\widetilde Q_{\delta_*}$ be the centre of
[SM.30](R144-supplement-mean-exact-compact-centres-on-the-selected-metric.md)
on the **same** intrinsic metric $\nu_*$. Its complete distance is
$\|\widetilde Q_*-Q_*\|_{A^0,\mathrm{pair}}<4.760\,10^{-7}$.
The whole segment is inside the convex domain RP.3. The exact
[RP.1](R144-supplement-full-off-constraint-principal-return-Hessian.md)
bound is
$\|D^2P[a,b]\|_2<530N(a)N(b)$ with
$N(h,\kappa)=\|h\|_{L^2_rL^2}+100|\kappa|$.
Because $r_*<.239<(49/100)^2$, the fundamental theorem of calculus,
(CP.9) and (CP.11) give

$$
\begin{aligned}
 |S(\widetilde Q_*,\nu_*,g_0)-S(Q_*,\nu_*,g_0)|
 &<\frac{21}{20}\,530\,132\,\frac{49}{100}
                                (4.760\,10^{-7})\\
 &<.017134,\\
 S(\widetilde Q_*,\nu_*,g_0)
 &>.038736784-1.014851\,10^{-5}-.017134
 >\frac1{50}. 
\end{aligned}                                                   \tag{CP.12}
$$

This pays the change in the complete two-ray return at the new
background, rather than reusing the old phase integral for free.
It keeps the same original trial as a candidate; it does not transfer
the assertion $D_Qv_\nu=F_\nu$ to $\widetilde Q_*$.

## CP5. A full Fourier neighbourhood and a genuine phase interval

Consider the following real neighbourhood, with all the original
interfaces and both means:

$$
\begin{gathered}
 Q=\widetilde Q_*+e,\qquad
 \sup_r\|e(r)\|_{A^3,\mathrm{component\ sum}}\le10^{-7},\\
 |\nu-\nu_*|\le5\,10^{-12},\\
 \|g-g_0\|_\infty\le10^{-8},\qquad
 \|g'-g_0'\|_\infty\le10^{-8}.
\end{gathered}                                                   \tag{CP.13}
$$

The error $e$ may contain every Fourier mode. The constant part of
$g-g_0$ is included in its norm and is not reset. The existing exact
selected bound $|\delta_*|<.936826\,10^{-10}$ implies
$|\nu-\nu_0|<10^{-10}$. RP.3 already contains the larger full-tail
$A^3$ radius $10^{-6}$ around $\widetilde Q_*$, so all state
segments used here are in its common domain.

For the background difference at fixed $g_0$,

$$
\begin{aligned}
 N(Q-Q_*,\nu-\nu_*)
 &<\frac{49}{100}(4.760\,10^{-7}+10^{-7})
                                      +100(5\,10^{-12}),\\
 |S(Q,\nu,g_0)-S(Q_*,\nu_*,g_0)|
 &<\frac{21}{20}\,530\,132
       \left[\frac{49}{100}(5.760\,10^{-7})+5\,10^{-10}\right]
 <.02077 .
\end{aligned}                                                   \tag{CP.14}
$$

The actual metric direction is in the second argument of the
Hessian and is charged its full factor100; it is not put in the
state difference or removed by compact support.

It remains to change the averaging lift. Set
$f=DP(Q,\nu)[h^a,1]$. RP.23 gives
$\|f\|_\infty<2.16(132)$ and
$\|f'\|_2<150(132)$ throughout this domain.
Every straight lift $g_t=g_0+t(g-g_0)$ has
$g_t'>32/33-10^{-8}>24/25$. Hence

$$
\begin{aligned}
 \|f\circ g-f\circ g_0\|_2
 &\le\frac{21}{20}\|g-g_0\|_\infty\|f'\|_2,\\
 \left\|\frac1{g'\circ R}-\frac1{g_0'\circ R}\right\|_\infty
 &\le(25/24)^2\|g'-g_0'\|_\infty .
\end{aligned}                                                   \tag{CP.15}
$$

The first bound is the exact fundamental theorem along $g_t$ and
the change-of-variable factor $\sqrt{25/24}<21/20$. Splitting the
two factors in (CP.3) therefore gives

$$
\begin{aligned}
 |\Lambda_g f-\Lambda_{g_0}f|
 &<132\,10^{-8}
       \left[\frac{25}{24}\frac{21}{20}(150)
                           +(25/24)^2(2.16)\right]\\
 &<.00022 .
\end{aligned}                                                   \tag{CP.16}
$$

Combining (CP.10), (CP.14) and (CP.16), without an exact-conjugacy
assumption at the new point, yields

$$
\begin{aligned}
 S(Q,\nu,g)&>.038736784-1.014851\,10^{-5}-.02077-.00022
                  >1/60,\\
 S(Q,\nu,g)&<.038768096+1.014851\,10^{-5}+.02077+.00022
                  <3/50 .
\end{aligned}                                                   \tag{CP.17}
$$

This proves (CP.1). The lift and state tolerances are sufficient
explicit neighbourhoods; they are not claims about the size of the
eventual Newton correction.

## CP6. What is supplied to the full augmented problem

At every point in (CP.13), use $z_\nu=h^a$ in the original PD
construction, with whatever passive lift is prescribed by the
chosen complete state chart. All other independent ports remain.
Its exact current regular residual is

$$
                     r_\nu=A(Q,\nu)z_\nu-N_\nu(Q,\nu).
                                                               \tag{CP.18}
$$

It includes the full body error, every boundary and waist equation,
both mean equations, the actual fourth Robin equation, physical
chart derivatives, and any genuine height/matching rows. None is
declared zero by (CP.1). PD.9 remains precisely
$(f+r_f+r_\nu\kappa,\ b+E'a)$.

Equivalently one may use the exact rank-one reduction in
[PP](R147-supplement-actual-phase-pivot-with-full-regular-defect-retained.md),
now with the candidate $h^a$, the current $S>1/60$, and the entire
current defect including the nonmean phase row. Its required bounds
in the final coupled function spaces are still separate work.

The accompanying
[saved-bound consumer](../scripts/fourfold_codazzi_compact_phase_pivot_saved_bounds.py)
uses rational arithmetic only on the displayed complete old bounds.
It does not restore carriers or evaluate a scientific target.
In particular no constant here establishes the full regular inverse,
the true-response Schur, nonlinear convergence, or topic completion.
