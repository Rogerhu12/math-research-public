# R115: Complete middle source and a paid interval-frequency strip

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

**Proved and actually evaluated.** For the same R101 outer low46 centre, the complete source mass in modes94–5758 is less than $2\cdot10^{-41}$, and the complete source above that range is less than $7\cdot10^{-73}$. Separately, the original10793 true leaves and R68 frames define a fixed hybrid-comparison analytic width with terminal value greater than $1/64$, and a rigorous comparison theorem covering each frequency interval with ratio at most33/32. The complete mean, inverse, zero numerator coefficient, all original source leaves, and all future frame costs are explicit.

This result does not claim that the interval-frequency response kernels have all run or that their nonlinear budget closes. The root source is the outer projected centre $C_L$, not the distinct inner auxiliary field. The two-mode fixed point of R114 is also not enlarged by this result.

## A. Complete outer-centre source

**Proved and exactly evaluated.** For the same real R100 low46 outer centre $C_L$ of R101, the complete weak source in source-x units satisfies

$$
\sum_{94\le |m|\le5758}\sup_x
\frac{e^{(18/125)|m|}|\mathcal N_m(C_L)(x)|}
{c_{\rm bg}(x)V_I(x)^2}<2\cdot10^{-41}.
\tag{115.A1}
$$

The sum over all $|m|\ge5760$ is less than $7\cdot10^{-73}$ in the same units. Both signs, the full mean root, the numerator's zero coefficient and the complete inverse tail are included. These are source bounds only. They do not replace a middle or high response kernel, unknown-field derivative, cut equation, or full nonlinear fixed point.

This uses the **outer** projected centre $C_L$ of R91/R101. It is not a source bound for the different inner auxiliary field of R39/R74.

### 1. Exact coefficient majorants

Let $a_m$ be R101's paid positive-mode strong pair cap, $m=2,4,\ldots,92$, in the constant strip $\tau_*=18/125$, divided by the same $V_I$. The completed packet gives $\sum a_m<10$. To avoid needing a parity equality, place the whole pair cap at each sign:

$$
A_m=A_{-m}=a_m,\qquad A_k=0\quad(k\notin\{\pm2,\ldots,\pm92\}).
\tag{115.A2}
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
\tag{115.A3}
$$

All symbols in (3) are the same true physical variables; no saved independent $E$ field or truncated mean is substituted.

For each signed input frequency the weak coefficient of $K_\theta-P$ and of $K+P_\theta$ is bounded by the corresponding strong coefficient. The weak coefficients of $P$ and $K$ together gain $1/(1+|m|)\le1/3$. Since $E\le5/4$ and $w^2\le1/4$, the radial quadratic coefficient is at most $5/4$ times $A*A$, and the log-w coefficient at most

$$\left(\frac54+\frac1{36}\right)A*A=\frac{23}{18}A*A.$$

Their two radial proportions are $s/c_{\rm bg}$ and $|\ell|/c_{\rm bg}$, whose sum is one. Hence $23/18$ also controls their combined source, not twice that number.

The nonmean leading coefficient is bounded modewise by $(5/4)V_IA$. The full mean and inverse are therefore dominated by the following nonnegative Laurent sequences:

$$
L=\frac54 V_0 A+4C_0^2V_0^2\delta_0,
\tag{115.A4}
$$
$$
B=\frac{23}{18}A*A+10C_0^2V_0 A
+16C_0^4V_0^2\delta_0.
\tag{115.A5}
$$

Here B bounds the complete numerator divided by $c_{\rm bg}V_I^2$. The middle term follows from $2c\Lambda$, and the final term from $c^2$. The zero coefficient of the first convolution is retained as well. The constants $V_I\le V_0$ are used only on the extra powers left after the source's common $V_I^2$ is removed.

Fourier multiplication is bounded by positive convolution because $e^{\tau_*|j+k|}\le e^{\tau_*|j|}e^{\tau_*|k|}$. Each modal radial supremum is fixed before convolution. Thus (4)–(5) dominate the actual strong radial source norm, not merely a pointwise angular sum.

### 2. Polynomial part and one shared complete tail

The exact consumer verifies $\lambda:=\|L\|_1<1$. The entire inverse is majorized by $\sum_{k\ge0}L^{*k}$. Define the complete finite polynomial

$$
P=B*\sum_{k=0}^{6}L^{*k},\qquad
T=\frac{\|B\|_1\lambda^7}{1-\lambda}.
\tag{115.A6}
$$

The remainder after P has total nonnegative modal mass at most T. There is **one shared tail mass** in a joint frequency partition. It cannot be assigned once to every mode or every window and then reported as the same total bound.

The support of B is at most 184, and that of each L is at most 92. Consequently P has support at most 736, including its mean coefficient. The full nonlinear source still has infinitely many modes; above 736 their total is bounded by T. Projection onto nonzero outputs is applied after the complete product, so the zero numerator coefficient can contribute to nonzero outputs through the inverse and is never deleted.

For any finite or infinite output set $S\subset2\mathbb Z\setminus\{0\}$,

$$
\|\Pi_S\mathcal N(C_L)/(c_{\rm bg}V_I^2)\|_{\tau_*,0}
\le\sum_{m\in S}P_m+T.
\tag{115.A7}
$$

Taking $S=\{94\le|m|\le5758\}$ gives (1). Taking $S=\{|m|\ge5760\}$ uses only T. Any fixed variable strip $\tau(x)\le\tau_*$ may consume the same majorant by restriction; no unknown field is upgraded to a larger strip.

### 3. Actual exact consumption

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
\tag{115.A8}
$$

The inequalities in (8) were checked on the exact saved rational quantities. Decimal displays do not define any input or gate. The primary saves every polynomial pair coefficient together with the shared tail, so an interval-frequency response may use either (1) as a common source mass or a sharper explicitly weighted partition.

The source is `2026-11-13-exact-resume-complete-middle-source-v1.py`. The completed primary `2026-11-13-exact-resume-complete-source-r1.json.gz` is 178274 bytes, SHA256 `bed3d6882f144cc4a82f8488eeaa66b04671a5f297dfb952f0251222b7847b3e`. Its summary and resource record have the same prefix. The actual wrapper returned exit 0, wall 29.870859146 seconds, peak 15104 KiB. This consumer performed no ODE solve, new source quadrature, or Arb computation.

No improved unknown-source derivative follows merely from (1). The complete nonlinear feedback still requires the R98 derivative estimate, actual middle kernels, the shared mean domain and the coupled low/high equations.

## B. Fixed hybrid strip and whole-leaf comparison

**Proved comparison tool; the actual coefficient and strip gates are complete.** This note defines a single positive analytic-strip function on the original 10793 leaves, and a valid comparison covering every frequency in a specified interval. A completed response run is still required before this tool supplies a numerical middle inverse. All frame entry, frame exit and frame changes below are part of that response computation.

### 1. A comparison preserving both physical diagonal terms

In R104's physical sine/cosine coordinates,

$$
P_x=-(s+\ell)P-msK,\qquad
K_x=-m\ell P-2\ell K+N_m.
\tag{115.B1}
$$

For real or complex coefficients the component moduli obey the upper-Dini inequalities

$$
D^+\binom{|P|}{|K|}\preceq
\begin{pmatrix}-(s+\ell)&ms\\m|\ell|&-2\ell\end{pmatrix}
\binom{|P|}{|K|}+\binom0{|N_m|}.
\tag{115.B2}
$$

The off-diagonal entries are nonnegative. Consequently the associated positive comparison preserves the signed diagonal damping. This proof uses the modulus derivative at nonzero components and its standard upper bound at a zero; it applies to the same complex Fourier coefficients as the original real-axis equation.

Let $m_-\le m\le m_+$ and fix $\rho=33/32$ with $m_+/m_-\le\rho$. On one original leaf choose a fixed exact upper coefficient $q_I\ge0$, and define the analytic width by $\tau_x=-\rho q_I$. With $z=e^{m\tau}(|P|,|K|)^T$, (2) is dominated by the constant Metzler matrix

$$
\widehat M_I=
\begin{pmatrix}
a_I-m_-\rho q_I&m_+s_I\\
m_+e_I&d_I-m_-\rho q_I
\end{pmatrix},
\tag{115.B3}
$$

where $a_I\ge-s-\ell$, $d_I\ge-2\ell$, $s_I\ge s$, and $e_I\ge|\ell|$ are actual whole-leaf bounds. No monotonicity of the signed original transfer in m is assumed: domination in (3) follows entry by entry after taking component moduli, with the upper frequency on the positive entries and the lower frequency on the negative strip term.

On the leaves treated by (3), the coefficient producer chooses

$$q_I=\operatorname{up}_{96}\sqrt{s_Ie_I}.$$

This choice is not needed to assert (3); it is the fixed width profile whose complete strip cost is checked below.

### 2. One true energy segment

On cell10/segment3 only, use the same original exact positive R68 leaf frame b and the norm

$$q=e^{m\tau}\bigl|(P,K/b)\bigr|_2.$$

The already proved physical logarithmic-norm bound gives

$$
D^+q\le\left[\max(a_I,d_I)+m_+q_I-m_-\rho q_I\right]q
+e^{m\tau}|N_m|/b,
\tag{115.B4}
$$

where now

$$q_I=\operatorname{up}_{96}\frac12\sup_I|sb+\ell/b|.$$

Both terms involving m use the same genuine leaf coefficient. The condition $m_+/m_-\le\rho$ gives a nonpositive frequency contribution, but the nonphase coefficient is still present.

Entering this norm from a physical component box $(u,v)$ costs $\sqrt{u^2+(v/b)^2}$. A change from $b_-$ to $b_+$ costs $\max(1,b_-/b_+)$. Returning to physical components costs $(q,bq)$. These operations remain mandatory even though the analytic-width function is continuous. The strip budget never pays or removes these frequency-independent amplitude factors.

### 3. Exact strip function and completed coefficient data

Start at $\tau(b)=18/125$. On each original source leaf set the derivative to $-\rho q_I$ in that leaf's original source-x coordinate. Define the next leaf's initial width by continuity. This defines one fixed function, independent of the mode window, source origin, iterate or field. The physical interfaces use the same endpoint value.

The producer consumes all 18 original source groups and 10793 leaves, with every original source/frame hash checked. Widths and all saved q values are exact rationals/dyadics. Its Fraction sum evaluates

$$
\tau_{\rm end}=\frac{18}{125}
-\frac{33}{32}\sum_I q_I\Delta x_I
>\frac1{64}.
\tag{115.B5}
$$

For exactly the energy selection cell10/segment3, the actual terminal-width display is

$$0.02163667990889687\ldots>0.015625.$$

Because every $q_I\ge0$, this also proves $1/64<\tau(x)\le18/125$ at every leaf and every internal point. The all-Metzler choice fails the same actual check, with negative terminal width; its midpoint phase estimate is not a substitute for (5).

The completed source `2026-11-13-exact-resume-hybrid-middle-leaves-v1.py` has SHA256 `aaecb235974878b88101bc07aec095b655cc1b796cbd92deb3c1206543fc0578`. The complete leaf stream is `2026-11-13-exact-resume-hybrid-leaves-r1-leaves.jsonl.gz`, 1656696 bytes, SHA256 `dadf463497d12f85e5fb3046d46eb6d2d2b2fa26ca36d3c19fbd061c4ea1fad1`. Its summary retains the individual segment costs and all tested exact selections. The actual resource wrapper returned exit 0, wall 66.182956219 seconds and peak 32944 KiB. This is an evaluation of the same certified whole-leaf coefficient boxes, not a new background ODE or a change to the original Taylor tolerances.

### 4. Whole-leaf forced responses to be consumed

For a matrix leaf let $E=\exp(\widehat M_I\Delta)$ and let $M_I^+$ be obtained by replacing negative diagonal entries in $\widehat M_I$ by zero. For any incoming nonnegative bound $u_0$ and constant nonnegative forcing bound f,

$$
u_{\rm end}\preceq Eu_0+\Delta\exp(M_I^+\Delta)f,
$$
$$
u(t)\preceq\exp(M_I^+\Delta)(u_0+\Delta f),
\qquad0\le t\le\Delta.
\tag{115.B6}
$$

Indeed, the exponential of a Metzler matrix preserves the positive cone; increasing its entries increases the positive semigroup. All entries of $M_I^+$ are nonnegative, so its exponential is also entrywise increasing in elapsed time. Applying these facts to the exact Duhamel formula proves both bounds in (6).

For an energy leaf the scalar equation with the coefficient in (4) gives the exact affine comparison endpoint. The comparison's derivative has fixed sign, so its maximum over the leaf is the larger of its initial and endpoint values. The forcing is $c_{\rm bg}V_I^p/b$ for each of the original materials $p=2,1,0$ and a unit weak source mass.

The subsequent numerical consumer must retain both genuine initial columns, all original source positions and the whole-leaf targets. Source outputs divide by the actual target $V_I$ before separate component suprema. A weak source to strong output pays $1+m_+$; initial-to-initial strong weights cancel. A mode window containing several even modes still receives only the shared modal mass, with the supremum of its per-mode bounds, rather than a gratuitous mode-count multiplier.

These statements prove that the proposed interval-frequency comparison is legal. They do not state that its full response has run, that its kernel is small enough, or that the coupled low/middle/high and cut equations are closed.
