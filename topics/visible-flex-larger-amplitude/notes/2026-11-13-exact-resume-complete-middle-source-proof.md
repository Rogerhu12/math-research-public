# Complete middle-source mass from all forty-six paid centre caps

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

**Proved and exactly evaluated.** For the same real R100 low46 outer centre $C_L$ of R101, the complete weak source in source-x units satisfies

$$
\sum_{94\le |m|\le5758}\sup_x
\frac{e^{(18/125)|m|}|\mathcal N_m(C_L)(x)|}
{c_{\rm bg}(x)V_I(x)^2}<2\cdot10^{-41}.
\tag{1}
$$

The sum over all $|m|\ge5760$ is less than $7\cdot10^{-73}$ in the same units. Both signs, the full mean root, the numerator's zero coefficient and the complete inverse tail are included. These are source bounds only. They do not replace a middle or high response kernel, unknown-field derivative, cut equation, or full nonlinear fixed point.

This uses the **outer** projected centre $C_L$ of R91/R101. It is not a source bound for the different inner auxiliary field of R39/R74.

## 1. Exact coefficient majorants

Let $a_m$ be R101's paid positive-mode strong pair cap, $m=2,4,\ldots,92$, in the constant strip $\tau_*=18/125$, divided by the same $V_I$. The completed packet gives $\sum a_m<10$. To avoid needing a parity equality, place the whole pair cap at each sign:

$$
A_m=A_{-m}=a_m,\qquad A_k=0\quad(k\notin\{\pm2,\ldots,\pm92\}).
\tag{2}
$$

Each actual signed strong coefficient is bounded by its pair cap, so (2) is conservative and $\|A\|_1<20$. It is not a claim that both signs independently realize the full cap.

Keep $C_0=10$, $V_0=2^{-40}$, and $c_{\rm bg}=s+|\ell|$. The actual whole field has physical strong norm at most $C_0V_I<1/64$. Thus the complete mean root obeys $|c|\le4C_0^2V_I^2$. Use the exact full source of R98,

$$
\mathcal N=\Pi_\perp\frac{Q+\ell(2c\Lambda+c^2)}{1+c+\Lambda},
\quad \Lambda=K+EP_\theta,
$$
$$
Q=Es(K_\theta-P)^2+
\ell\{E(K+P_\theta)^2-w^2(K^2+P^2)\}.
\tag{3}
$$

All symbols in (3) are the same true physical variables; no saved independent $E$ field or truncated mean is substituted.

For each signed input frequency the weak coefficient of $K_\theta-P$ and of $K+P_\theta$ is bounded by the corresponding strong coefficient. The weak coefficients of $P$ and $K$ together gain $1/(1+|m|)\le1/3$. Since $E\le5/4$ and $w^2\le1/4$, the radial quadratic coefficient is at most $5/4$ times $A*A$, and the log-w coefficient at most

$$\left(\frac54+\frac1{36}\right)A*A=\frac{23}{18}A*A.$$

Their two radial proportions are $s/c_{\rm bg}$ and $|\ell|/c_{\rm bg}$, whose sum is one. Hence $23/18$ also controls their combined source, not twice that number.

The nonmean leading coefficient is bounded modewise by $(5/4)V_IA$. The full mean and inverse are therefore dominated by the following nonnegative Laurent sequences:

$$
L=\frac54 V_0 A+4C_0^2V_0^2\delta_0,
\tag{4}
$$
$$
B=\frac{23}{18}A*A+10C_0^2V_0 A
+16C_0^4V_0^2\delta_0.
\tag{5}
$$

Here B bounds the complete numerator divided by $c_{\rm bg}V_I^2$. The middle term follows from $2c\Lambda$, and the final term from $c^2$. The zero coefficient of the first convolution is retained as well. The constants $V_I\le V_0$ are used only on the extra powers left after the source's common $V_I^2$ is removed.

Fourier multiplication is bounded by positive convolution because $e^{\tau_*|j+k|}\le e^{\tau_*|j|}e^{\tau_*|k|}$. Each modal radial supremum is fixed before convolution. Thus (4)–(5) dominate the actual strong radial source norm, not merely a pointwise angular sum.

## 2. Polynomial part and one shared complete tail

The exact consumer verifies $\lambda:=\|L\|_1<1$. The entire inverse is majorized by $\sum_{k\ge0}L^{*k}$. Define the complete finite polynomial

$$
P=B*\sum_{k=0}^{6}L^{*k},\qquad
T=\frac{\|B\|_1\lambda^7}{1-\lambda}.
\tag{6}
$$

The remainder after P has total nonnegative modal mass at most T. There is **one shared tail mass** in a joint frequency partition. It cannot be assigned once to every mode or every window and then reported as the same total bound.

The support of B is at most 184, and that of each L is at most 92. Consequently P has support at most 736, including its mean coefficient. The full nonlinear source still has infinitely many modes; above 736 their total is bounded by T. Projection onto nonzero outputs is applied after the complete product, so the zero numerator coefficient can contribute to nonzero outputs through the inverse and is never deleted.

For any finite or infinite output set $S\subset2\mathbb Z\setminus\{0\}$,

$$
\|\Pi_S\mathcal N(C_L)/(c_{\rm bg}V_I^2)\|_{\tau_*,0}
\le\sum_{m\in S}P_m+T.
\tag{7}
$$

Taking $S=\{94\le|m|\le5758\}$ gives (1). Taking $S=\{|m|\ge5760\}$ uses only T. Any fixed variable strip $\tau(x)\le\tau_*$ may consume the same majorant by restriction; no unknown field is upgraded to a larger strip.

## 3. Actual exact consumption

The standard-library Fraction program consumes all 46 original exact field caps in `2026-11-13-closure-r101-exact-summary-r1.json`, with its complete gates checked. It performs the signed convolutions, all seven inverse-polynomial terms, the zero coefficients, and the exact geometric remainder using rational arithmetic.

The resulting displays are

$$
\lambda=2.065369004682085\ldots\cdot10^{-11},\qquad
\|B\|_1=421.72589486451034\ldots,
$$
$$
\sum_{94\le|m|\le5758}P_m+T
=1.9583385835323265\ldots\cdot10^{-41}<2\cdot10^{-41},
$$
$$
T=6.761045441961842\ldots\cdot10^{-73}<7\cdot10^{-73}.
\tag{8}
$$

The inequalities in (8) were checked on the exact saved rational quantities. Decimal displays do not define any input or gate. The primary saves every polynomial pair coefficient together with the shared tail, so an interval-frequency response may use either (1) as a common source mass or a sharper explicitly weighted partition.

The source is `2026-11-13-exact-resume-complete-middle-source-v1.py`. The completed primary `2026-11-13-exact-resume-complete-source-r1.json.gz` is 178274 bytes, SHA256 `bed3d6882f144cc4a82f8488eeaa66b04671a5f297dfb952f0251222b7847b3e`. Its summary and resource record have the same prefix. The actual wrapper returned exit 0, wall 29.870859146 seconds, peak 15104 KiB. This consumer performed no ODE solve, new source quadrature, or Arb computation.

No improved unknown-source derivative follows merely from (1). The complete nonlinear feedback still requires the R98 derivative estimate, actual middle kernels, the shared mean domain and the coupled low/high equations.
