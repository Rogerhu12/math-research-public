# R144 supplement: complete low-norm tame body Hessian and mean-preserving smoothing

2026-11-27, visible-exact-astra-fb31ed6-20261127 / geometric_closure.

**Proved on the whole actual radial interval and the whole selected
metric interval.** The raw moving body map, including its true metric
parameter, has explicit second-derivative tame bounds at every angular
order. Smallness is needed only in the complete low Wiener norm; each
high norm occurs linearly. For the exact-mean compact centres and
$\sup_r\|h(r)\|_{A^0}\le\rho\le10^{-4}$, its complete fixed-metric
remainder satisfies

$$
 \|\mathcal N(h)\|_{L^2_rH^{1/3}_\phi}
       \le579\rho\|h\|_{L^2_rX_{4/3}},\qquad
 \|\mathcal N(h)\|_{L^2_rH^{-2/3}_\phi}
       \le215\rho\|h\|_{L^2_rX_{1/3}} .
 \tag{TH.1}
$$

The independent even mean is included and is bounded separately below.
The same estimates apply on every radial subinterval. No angular
support assumption is made about $h$.

This improves the old
[Sobolev flux theorem S](R133-supplement-complete-moving-Sobolev-flux-and-derivative-loss.md)
in a necessary way for an iteration: S assumes a small
$A^{s+1}$ norm at every target order, whereas the bounds here use only
small $A^0$ and one high norm. The old conservative identities are
reused, not reevaluated. The new mixed and pure metric Hessian
coefficients are actual scalar consequences of the completed D
positive algorithm.

These are the body and raw-join parts of the nonlinear problem.
They do not supply the physical-angle/height/phase Hessians, a
same-state full regular inverse, the true parameter Schur denominator,
or a convergent global iteration.

## TH1. State, parameter, and norms

Work at any $\nu=\nu_0+\delta$, $|\delta|\le10^{-10}$, with the
original fixed $\eta_0$. The centre $\widetilde Q_\delta$ is exactly
the one in
[SM](R144-supplement-mean-exact-compact-centres-on-the-selected-metric.md).
Its two mean endpoints, its actual raw nonmean joins, and its
degree32 angular support are retained. The metric interval contains
the actual selected $\delta_*$. It is a parameter domain used to
construct the solution, not an isometric family with varying metric.

Use the normalized circle of length $\pi/2$, Fourier indices $j\in
\mathbb Z$ and physical frequencies $4j$. For vector coefficients use
the Euclidean norm inside the sum:

$$
 \|f\|_{A^s}=\sum_j(1+4|j|)^s|\widehat f_j|,\qquad
 \|f\|_{X_s}^2=\sum_j(1+4|j|)^{2s}|\widehat f_j|^2.
 \tag{TH.2}
$$

This makes $X_0$ exactly the normalized-circle Euclidean pair $L^2$.
All previously paid component-sum Wiener bounds dominate this
convention. No factor $\sqrt2$ is needed. Means have their actual
coefficient with weight one. For $s\ge0$, put

$$
 c_s=\max(1,2^{s-1}),\qquad
 A_s=1+\frac{c_s}{4}+\frac{c_s^2}{2}.
 \tag{TH.3}
$$

The complete convolution inequalities are

$$
 \begin{aligned}
 \|fg\|_{X_s}
 &\le c_s(\|f\|_{X_s}\|g\|_{A^0}
                         +\|f\|_{A^0}\|g\|_{X_s}),\\
 \|fg\|_{X_s}&\le\|f\|_{A^s}\|g\|_{X_s},&
 \|If\|_{X_s}&\le\frac14\|f\|_{X_s},\\
 \|\partial_\phi f\|_{H^{s-1}}&\le\|f\|_{X_s},&
 \|f\|_{H^{s-1}}&\le\|f\|_{X_s}.
 \end{aligned}
 \tag{TH.4}
$$

In the first two inequalities a scalar/vector product or a Euclidean
bilinear contraction is meant. The first follows from
$(1+|k+\ell|)^s\le c_s[(1+|k|)^s+(1+|\ell|)^s]$ and Young's
inequality. The second uses submultiplicativity instead. The
primitive is the original $I=\partial_\phi^{-1}P_{\ne0}$; its zero
coefficient is removed only at the displayed intermediate product.
The derivative estimate in (TH.4) is valid also for $0\le s<1$.

The low Wiener domain is an ordinary Sobolev domain:

$$
 \|f\|_{A^0}\le
 \left(\sum_{j\in\mathbb Z}(1+16j^2)^{-1}\right)^{1/2}\|f\|_{H^1}
 <\frac{11}{10}\|f\|_{H^1}.
 \tag{TH.5}
$$

Indeed the square of the prefactor is at most
$1+\pi^2/48<1+10/48<(11/10)^2$. This estimate includes the true
mean and both Fourier signs.

## TH2. Whole-body intrinsic bounds and new true-metric derivatives

Set $D_K=\operatorname{diag}(1,K)$ and

$$
 C_\nu=\gamma_\nu J(K_\nu)
   =\begin{pmatrix}0&\gamma_\nu K_\nu\\-\gamma_\nu&0\end{pmatrix}.
 \tag{TH.6}
$$

Here the subscript $\nu$ labels the coefficient at that parameter;
derivatives are written $\partial_\nu C_\nu$.
The actual WLA products on $[0,9/10]$ are
$|\beta|\max(1,|K_\nu|)<4.730$ and
$\|C_\nu\|<13.862$. On the whole cap $[9/10,25/8]$, the completed
intrinsic constants are $|\beta|,\gamma<6$, $0<K<1$.
Thus, for the entire real interval and parameter domain,

$$
 |\beta|\|D_K\|<B:=6,\qquad \|C_\nu\|<G:=14.
 \tag{TH.7}
$$

These are intrinsic bounds independent of the current state.
They therefore apply at the compact centre and at a nonlinear
iterate without an operator-transfer assumption.

For the new metric derivative bounds read the original D producer
**selected_parameter_fees**. With its fixed positive values

$$
 d=10^{-10},\quad e=19d,\quad e_1=83d,\quad
 U=14e+e^2,\quad V=(7+e)^2,
 \tag{TH.8}
$$

the saved positive expression **N_nu** contains the summands

$$
 b\,k_{\nu,+}\,c_K+j_{\nu,+}\,c_J,\qquad
 \begin{aligned}
 c_K&=6U/4+Ve_1/4+7U+Ve,\\
 c_J&=6e+(7+e)e_1 .
 \end{aligned}
 \tag{TH.9}
$$

All its other terms are nonnegative. Its actual closed-row
quantities obey
$b\,k_{\nu,+}\ge|\beta\,\partial_\nu K_\nu|$ and
$j_{\nu,+}\ge\|\partial_\nu C_\nu\|$ on the whole selected
parameter interval. The saved complete supremum and ordinary
$L^2dr$ budgets for **N_nu** on $C=[1/20,9/50]$ are

$$
 \begin{aligned}
 N_\infty&=[1.638768133273072080558708590726722927039848743417943065816242075
                 \,10^{-6}\ \mathord\pm6.22\,10^{-71}],\\
 N_2&=[4.266126750274453460280035543616779566573407555037988400119247035
                 \,10^{-7}\ \mathord\pm2.49\,10^{-71}].
 \end{aligned}
 \tag{TH.10}
$$

The explicit positivity of the producer, followed by its already
completed maximum or integral, proves

$$
 \begin{array}{c|cc}
 &L^\infty(C)&L^2(C;dr)\\ \hline
 |\beta\,\partial_\nu K_\nu|&
      N_\infty^+/c_K<3.893717&
      N_2^+/c_K<1.013633\\
 \|\partial_\nu C_\nu\|&
      N_\infty^+/c_J<23.579398&
      N_2^+/c_J<6.138312 .
 \end{array}
 \tag{TH.11}
$$

The divisors in (TH.9) are fixed positive rational budget
coefficients. This is not a reverse inequality for the norm of
$F_\nu(Q_\delta)-F_\nu(Q_0)$ and does not use a lower bound on
that difference. No old row or radial integral is recomputed.

The original exact compact coefficient identities give, with
the original $\chi,T,K,\gamma$ at $\nu_0$,

$$
 \begin{aligned}
 \partial_\nu^n K_{\nu_0+\delta}
 &=e^{-\delta\chi}
   [(-\chi)^n(K+\delta T\chi')
                       +n(-\chi)^{n-1}T\chi'],\\
 \partial_\nu^n(\gamma K)_{\nu_0+\delta}
 &=\gamma e^{-\delta\chi/2}
   [(-\chi/2)^n(K+\delta T\chi')
                    +n(-\chi/2)^{n-1}T\chi'],\\
 \partial_\nu^n\gamma_{\nu_0+\delta}
 &=\gamma e^{\delta\chi/2}(\chi/2)^n .
 \end{aligned}
 \tag{TH.12}
$$

Because $0\le\chi\le1$, the same original first-derivative
majorants give, for every $n\ge1$,

$$
 |\beta\,\partial_\nu^nK_\nu|
       \le n\,b k_{\nu,+},\qquad
 \|\partial_\nu^nC_\nu\|
       \le n2^{1-n}j_{\nu,+}.
 \tag{TH.13}
$$

These inequalities hold pointwise before taking a radial norm.
Consequently usable complete constants are

$$
 \begin{gathered}
 |\beta K_\nu'|<4,\quad \|C_\nu'\|<24,\qquad
 |\beta K_\nu''|<8,\quad \|C_\nu''\|<24,\\
 \|\beta K_\nu''\|_{L^2}<2.028,\qquad
 \|C_\nu''\|_{L^2}<6.139 .
 \end{gathered}
 \tag{TH.14}
$$

Primes in (TH.14) mean parameter derivatives, not radial
derivatives. Every derivative in (TH.12)--(TH.14) is exactly zero
off $C$, including at both compact endpoints. No root singular
factor or positive-side parameter source is introduced.

The small inputs are the completed D execution
43713242980/1, SHA256
6956c214240cd85e6263331b33e0c7efcf6abc3e71190d46ff3eabddecd35071;
the completed WLA execution 43749764738/1, SHA256
936633fcfb2cdc9ed3f0e108909275497337f59daea9e1fa33ee0ab40de0ec5d;
and the whole-cap intrinsic summary 43674917925/1, SHA256
7a08e94850d66de1d9dba184df205a5a288436fbb0cc005edaa462261976a17f.
The corresponding theorems are
[WLA](R133-supplement-actual-complete-original96-waist-lifting.md),
[D](R133-supplement-exact-selected-parameter-core-differences-and-finite193-transfer.md)
and [V](R133-supplement-complete-real-delta-fixed-base-cap-linear-inverse.md).

## TH3. The complete joint Hessian in the original raw coordinates

Use the already proved conservative identity

$$
 F(Q,\nu)=\partial_\phi[-\beta I(Q^tD_KQ)Q+
                  \langle v\rangle C_\nu Q]
       +\beta\operatorname{diag}(-1,1)Q
       -\beta\langle Q^tD_KQ\rangle Q.
 \tag{TH.15}
$$

For directions $h,k$, write
$B_h=Q^tD_Kh$, $B_k=Q^tD_Kk$,
$B_{hk}=h^tD_Kk$, $m_h=\langle h_2\rangle$ and
$m_k=\langle k_2\rangle$. Its exact state Hessian is

$$
 \begin{aligned}
 D_Q^2F(Q,\nu)[h,k]
 ={}&\partial_\phi\{
 -2\beta[I(B_h)k+I(B_k)h+I(B_{hk})Q]
                  +m_h C_\nu k+m_k C_\nu h\}\\
 &-2\beta[\langle B_h\rangle k+
                 \langle B_k\rangle h+\langle B_{hk}\rangle Q].
 \end{aligned}
 \tag{TH.16}
$$

For the mixed derivative, put $m=\langle v\rangle$:

$$
 \begin{aligned}
 D_Q\partial_\nu F(Q,\nu)[h]
 ={}&\partial_\phi\{
 -\beta K_\nu'[2I(vh_2)Q+I(v^2)h]
                        +m_h C_\nu'Q+m C_\nu'h\}\\
 &-\beta K_\nu'[2\langle vh_2\rangle Q+
                                      \langle v^2\rangle h],\\
 \partial_\nu^2F(Q,\nu)
 ={}&\partial_\phi[-\beta K_\nu''I(v^2)Q+mC_\nu''Q]
                         -\beta K_\nu''\langle v^2\rangle Q .
 \end{aligned}
 \tag{TH.17}
$$

Thus the full Hessian on raw state and true metric directions is

$$
 \begin{aligned}
 D_{(Q,\nu)}^2F[(h,\kappa),(k,\lambda)]
 ={}&D_Q^2F[h,k]
       +\kappa D_Q\partial_\nu F[k]
       +\lambda D_Q\partial_\nu F[h]
       +\kappa\lambda\partial_\nu^2F .
 \end{aligned}
 \tag{TH.18}
$$

There is no normalized rotational reference in these formulas.
In particular (TH.17) is the partial metric derivative at a fixed
physical $Q$, not a second derivative of the explicit SM curve
$\delta\mapsto\widetilde Q_\delta$. The latter would also contain
its own first and second state derivatives. All means in
(TH.16)--(TH.18) are retained; no zero-mean condition on $h_2$
or $k_2$ is imposed.

Write $q_0=\|Q\|_{A^0}$, $q_s=\|Q\|_{X_s}$ and similarly
$h_0,h_s,k_0,k_s$. The complete tame bounds are

$$
 \begin{aligned}
 \|D_Q^2F[h,k]\|_{H^{s-1}}
 \le{}&12A_s(q_sh_0k_0+q_0h_sk_0+q_0h_0k_s)
                   +14(h_0k_s+k_0h_s),\\
 \|D_Q\partial_\nu F[h]\|_{H^{s-1}}
 \le{}&4A_s(2q_0q_sh_0+q_0^2h_s)
                         +24(q_sh_0+q_0h_s),\\
 \|\partial_\nu^2F\|_{H^{s-1}}
 \le{}&(8A_sq_0^2+24q_0)q_s .
 \end{aligned}
 \tag{TH.19}
$$

The last two lines vanish off $C$. To verify the coefficients,
the three primitive terms in (TH.16), after applying (TH.4),
give coefficient $B(c_s^2+c_s/2)$ on each of the three
single-high products. Their complete mean reactions add $2B$.
The sum is $2BA_s=12A_s$. The two holonomy terms give the
last summand of the first line. For (TH.17), the primitive
coefficient on $q_0^2h_s$ is $c_s^2/2+c_s/4$ and the
coefficient on $q_0q_sh_0$ is twice this; the mean reaction
adds respectively one and two. This proves exactly $A_s$
and $2A_s$, with both independent mean-rank terms included.

The expressions have one high factor, not two. In particular a
bound on $q_0,h_0,k_0$ does not require any bound on their
high Wiener norms. The state-third derivative is also complete:

$$
 \|D_Q^3F[h,k,\ell]\|_{H^{s-1}}
 \le12A_s(h_sk_0\ell_0+h_0k_s\ell_0+h_0k_0\ell_s),
 \qquad D_Q^4F=0 .
 \tag{TH.20}
$$

The actual metric dependence is smooth to every parameter order
by (TH.12)--(TH.13). These facts establish the angular smooth
tame property of the full raw body map.

For $L^2_rH^{s-1}_\phi$, take the low norms as radial suprema and
each high norm as its actual $L^2_rX_s$ norm. In the last two
lines of (TH.19), those high norms may be restricted to $C$;
the first line uses the whole interval under consideration.
This procedure follows directly from the pointwise inequalities.
It neither treats an endpoint trace as a body norm nor inserts
a length factor into a jump norm.

## TH4. Actual compact-centre constants and complete remainder

The full raw state bounds and the complete SM same-$\phi$
difference give, uniformly in $r$ and $|\delta|\le10^{-10}$,

$$
 \|\widetilde Q_\delta\|_{A^0}<6.407,\qquad
 \|(\widetilde Q_\delta)_\phi\|_{A^0}<5.438 .
 \tag{TH.21}
$$

The checker permits the entire continuous-repair allowances
$3.861\,10^{-18}$ and $1.970\,10^{-17}$ as well as SM's
$4.739\,10^{-7}$ and $1.255\,10^{-6}$, so no strict margin
is taken from an upper bound equal to seven.

Only this known centre has degree32. Therefore

$$
 \|\widetilde Q_\delta\|_{A^s}
 \le6.407+5.438
       \max_{1\le j\le32}\frac{(1+4j)^s}{4j}.
 \tag{TH.22}
$$

For $s=1/3$ the maximum is at $j=1$.
For $s=4/3$ the function decreases and then increases, so its
maximum is at one of the two endpoints. The strict rational
comparisons $5^{1/3}<1.71$ and
$129^{4/3}/128<5.1$, together with the other endpoint, give

$$
 Q_{1/3}:=\|\widetilde Q_\delta\|_{A^{1/3}}<8.732,\qquad
 Q_{4/3}:=\|\widetilde Q_\delta\|_{A^{4/3}}<34.141 .
 \tag{TH.23}
$$

Now hold the actual metric fixed, put $Q=\widetilde Q_\delta$
and let $\|h\|_{A^0}\le\rho$. Reuse the exact old NF conservative
remainder. Instead of requiring $A^s$ smallness of $h$, apply
both inequalities in (TH.4). Its three primitive terms satisfy

$$
 \begin{aligned}
 \|I(h^tD_Kh)Q\|_{X_s}
 &\le\|D_K\|\,\frac{c_s}{2}Q_s\rho\,\|h\|_{X_s},\\
 \|2I(Q^tD_Kh)h\|_{X_s}
 &\le\|D_K\|\,\frac{c_s}{2}(Q_s+q_0)\rho\,\|h\|_{X_s},\\
 \|I(h^tD_Kh)h\|_{X_s}
 &\le\|D_K\|(c_s^2/2+c_s/4)\rho^2\,\|h\|_{X_s}.
 \end{aligned}
 \tag{TH.24}
$$

Here $Q_s$ means the known $A^s$ bound in (TH.22), not the
unknown correction norm. The complete mean reaction is bounded
by $|\beta|\|D_K\|(Q_s+2q_0+\rho)\rho\|h\|_{X_s}$.
The quadratic holonomy flux costs at most
$\|C_\nu\|\rho\|h\|_{X_s}$. Consequently

$$
 \|\mathcal N(h)\|_{H^{s-1}}
 \le\left\{6[c_s(Q_s+q_0/2)+Q_s+2q_0+A_s\rho]+14\right\}
                                      \rho\|h\|_{X_s}.
 \tag{TH.25}
$$

For $\rho\le10^{-4}$, use $c_{4/3}<1.26$ and $c_{1/3}=1$.
The two exact rational evaluations give precisely (TH.1).
They are complete whole-body statements, with no sampled
frequency or radial values. A high-high product can create a
low mode; all such products have been included.

The complete even mean is

$$
 \langle\mathcal N_2(h)\rangle
 =-\beta\{\langle h^tD_Kh\rangle m+
       2\langle Q^tD_Kh\rangle\langle h_2\rangle+
       \langle h^tD_Kh\rangle\langle h_2\rangle\}.
 \tag{TH.26}
$$

It follows, in the same normalized pair convention, that

$$
 |\langle\mathcal N_2(h)\rangle|
 \le115.327\,\rho\|h\|_{L^2_\phi}.
 \tag{TH.27}
$$

This includes the independent scalar source generated even when
the centre's own mean equation is exact. The reflection class
sets the odd first mean to zero, but does not set (TH.26) to zero.

For a joint step $(h,\kappa)$, the exact remainder is the integral
of (TH.18) along $(Q+th,\nu+t\kappa)$ with weight $1-t$.
The whole segment must lie in $|\nu-\nu_0|\le10^{-10}$.
Its mixed terms and its pure parameter term are bounded by
(TH.19), not by the fixed-metric constants (TH.1) alone.
For example, at the compact centre, (TH.11) and (TH.23) give

$$
 \|\partial_\nu^2 F(\widetilde Q_\delta,\nu_\delta)\|
                    _{L^2_rH^{1/3}_\phi}<7334.150,\qquad
 \|\partial_\nu^2 F(\widetilde Q_\delta,\nu_\delta)\|
                    _{L^2_rH^{-2/3}_\phi}<1615.076 .
 \tag{TH.28}
$$

These use the complete saved radial $L^2$ coefficient budget;
no $\sqrt{|C|}$ substitute or newly computed integral is used.
They do not bound a total second derivative of the SM family.

## TH5. Actual consumption by the compact high inverse

Let $H=P_{|j|\ge97}$ and use the genuine compact given-head inverse
$G_H^*$ proved in
[PH](R144-supplement-actual-positive-high-graph-for-compact-centres.md).
Consider the contribution with body source $H\mathcal N(h)$
and zero independent head/boundary/jump inputs. This is a linear
contribution to the full correction, not a claim that those
other full-problem inputs vanish.

The collar and body source intervals are disjoint in $dr$.
The two ordinary-source entries in each PH row can therefore be
combined by Cauchy--Schwarz with the single full source norm.
Include PH's factor $1.000002$ to express all high root data in
the old frame. Equations (TH.1) and the actual PH columns yield

$$
 \begin{array}{c|cc}
 \text{output of }G_H^*H\mathcal N&
     \text{base window, times }\rho\|h\|_{L^2X_{4/3}}&
     \text{negative window, times }\rho\|h\|_{L^2X_{1/3}}\\ \hline
 \text{whole raw }L^2\text{ or }H^{-1}&266&336\\
 \text{old-frame root outgoing}&106&134\\
 \text{physical outer even }H^{-5/6}&1.362&534 .
 \end{array}
 \tag{TH.29}
$$

All entries are strict upper bounds. For instance the first
base entry uses
$579(1.000002)\sqrt{.032658^2+.457708^2}<266$.
No extra $\sqrt2$ is added, and no source length is attached
to an impulse.

The low body and mean parts of $\mathcal N$ remain in their
own equations. The known centre residual has zero direct high
source, but an unknown nonlinear correction does not. In
particular (TH.29) neither drops that correction nor grants
the unclosed full low/high Schur gate. The source/state loss
is still $4/3$ angular derivatives in both windows.

## TH6. Smoothing keeps the raw means and all original join equations

For $N\ge0$ let $S_N=P_{|j|\le N}$ on the raw moving circle,
including $j=0$. It is a contraction on every $X_s$ and on
$A^0$, preserves odd/even reflection, commutes with $I$ and
with radial differentiation on each actual piece, and satisfies
for $t\ge s$,

$$
 \begin{aligned}
 \|S_N f\|_{X_t}
       &\le(1+4N)^{t-s}\|f\|_{X_s},\\
 \|(1-S_N)f\|_{X_s}
       &\le(1+4(N+1))^{s-t}\|f\|_{X_t},\\
 \langle S_Nf\rangle&=\langle f\rangle .
 \end{aligned}
 \tag{TH.30}
$$

Thus an angularly smoothed state increment preserves its
prescribed two raw mean endpoint increments exactly. For every
one of the original joins,
$[S_Nf]_i=S_N[f]_i$; a continuous increment stays continuous.
For the actual compact centre, its value jumps have degree at
most32 and its ordinary body residual degree at most96.
Hence all of its initial raw jump data and ordinary residual
are unchanged by $S_N$ when $N\ge96$.

In the augmented residual, retain each scalar row as the
identity under smoothing. This includes both physical-density
means, the moving mean, the true parameter/phase scalar row,
and every independently supplied height or normalization
scalar. They are not identified with one another.
Raw jump rows may be left unsmoothed; their initial prescribed
data are already finite degree. Their exact nonlinear Hessian
is zero, since the raw jump equation is $Q^+-Q^-=0$.
The actual nonzero centre jumps are still affine data.

For an actual linear solve with the raw join rows exact, those
rows are consequently exact after the first update and receive
no nonlinear Taylor defect at later updates. An approximate
linear solve must still pay its actual join defect. Changing
to physical-angle or Riccati coordinates does not make their
nonlinear join maps linear; their separate transformations
must still be included.

For the ordinary body residual
$\mathcal R(Q,\nu)=Q_r-F(Q,\nu)$ and a step that solves its
smoothed linear equation up to $e_N$, one has exactly

$$
 \begin{aligned}
 \mathcal R(Q+h,\nu+\kappa)
 ={}&(1-S_N)\mathcal R(Q,\nu)+e_N\\
 &-\int_0^1(1-t)D^2_{(Q,\nu)}F(Q+th,\nu+t\kappa)
                         [(h,\kappa),(h,\kappa)]\,dt .
 \end{aligned}
 \tag{TH.31}
$$

The complete mean of the last line is present. No claim that
$S_N$ commutes with the nonlinear field or with its current
inverse is used. On a physical boundary row, any angular
smoothing must instead use that row's own fixed physical
chart as required by PD; (TH.30) is not a free composition
identity between $\phi$ and $\theta$.

## TH7. Completed scope

The companion
[exact rational reader](../scripts/fourfold_codazzi_compact_tame_Hessian_saved_bounds.py)
passes all29 comparisons. It only reads the three completed
small objects listed above and forms the new positive
quotients, polynomial bounds and source-column combinations.
It imports no old scientific producer and redoes no native
row, primitive, Fourier transform, radial integral, reference
flow or Green calculation.

The new paid items are the complete all-order low-norm body
Hessian, its actual whole-interval true-metric coefficients,
the two compact-centre nonlinear source constants, their
actual given-head high responses, and compatible raw mean
and join smoothing identities.

The full inverse at a varying unknown background, physical
chart and phase compositions, all independent boundary
Hessians, the true scalar Schur, and a summable complete
smoothing iteration remain separate. The angular estimates
above do not assert unproved high radial smoothness across
the original piecewise interfaces. Final fixed-metric
geometric closure is not inferred from a body tame bound.
