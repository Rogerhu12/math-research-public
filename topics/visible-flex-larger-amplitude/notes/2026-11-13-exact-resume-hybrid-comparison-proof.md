# Whole-leaf mixed comparison for interval frequencies

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.

**Proved comparison tool; the actual coefficient and strip gates are complete.** This note defines a single positive analytic-strip function on the original 10793 leaves, and a valid comparison covering every frequency in a specified interval. A completed response run is still required before this tool supplies a numerical middle inverse. All frame entry, frame exit and frame changes below are part of that response computation.

## 1. A comparison preserving both physical diagonal terms

In R104's physical sine/cosine coordinates,

$$
P_x=-(s+\ell)P-msK,\qquad
K_x=-m\ell P-2\ell K+N_m.
\tag{1}
$$

For real or complex coefficients the component moduli obey the upper-Dini inequalities

$$
D^+\binom{|P|}{|K|}\preceq
\begin{pmatrix}-(s+\ell)&ms\\m|\ell|&-2\ell\end{pmatrix}
\binom{|P|}{|K|}+\binom0{|N_m|}.
\tag{2}
$$

The off-diagonal entries are nonnegative. Consequently the associated positive comparison preserves the signed diagonal damping. This proof uses the modulus derivative at nonzero components and its standard upper bound at a zero; it applies to the same complex Fourier coefficients as the original real-axis equation.

Let $m_-\le m\le m_+$ and fix $\rho=33/32$ with $m_+/m_-\le\rho$. On one original leaf choose a fixed exact upper coefficient $q_I\ge0$, and define the analytic width by $\tau_x=-\rho q_I$. With $z=e^{m\tau}(|P|,|K|)^T$, (2) is dominated by the constant Metzler matrix

$$
\widehat M_I=
\begin{pmatrix}
a_I-m_-\rho q_I&m_+s_I\\
m_+e_I&d_I-m_-\rho q_I
\end{pmatrix},
\tag{3}
$$

where $a_I\ge-s-\ell$, $d_I\ge-2\ell$, $s_I\ge s$, and $e_I\ge|\ell|$ are actual whole-leaf bounds. No monotonicity of the signed original transfer in m is assumed: domination in (3) follows entry by entry after taking component moduli, with the upper frequency on the positive entries and the lower frequency on the negative strip term.

On the leaves treated by (3), the coefficient producer chooses

$$q_I=\operatorname{up}_{96}\sqrt{s_Ie_I}.$$

This choice is not needed to assert (3); it is the fixed width profile whose complete strip cost is checked below.

## 2. One true energy segment

On cell10/segment3 only, use the same original exact positive R68 leaf frame b and the norm

$$q=e^{m\tau}\bigl|(P,K/b)\bigr|_2.$$

The already proved physical logarithmic-norm bound gives

$$
D^+q\le\left[\max(a_I,d_I)+m_+q_I-m_-\rho q_I\right]q
+e^{m\tau}|N_m|/b,
\tag{4}
$$

where now

$$q_I=\operatorname{up}_{96}\frac12\sup_I|sb+\ell/b|.$$

Both terms involving m use the same genuine leaf coefficient. The condition $m_+/m_-\le\rho$ gives a nonpositive frequency contribution, but the nonphase coefficient is still present.

Entering this norm from a physical component box $(u,v)$ costs $\sqrt{u^2+(v/b)^2}$. A change from $b_-$ to $b_+$ costs $\max(1,b_-/b_+)$. Returning to physical components costs $(q,bq)$. These operations remain mandatory even though the analytic-width function is continuous. The strip budget never pays or removes these frequency-independent amplitude factors.

## 3. Exact strip function and completed coefficient data

Start at $\tau(b)=18/125$. On each original source leaf set the derivative to $-\rho q_I$ in that leaf's original source-x coordinate. Define the next leaf's initial width by continuity. This defines one fixed function, independent of the mode window, source origin, iterate or field. The physical interfaces use the same endpoint value.

The producer consumes all 18 original source groups and 10793 leaves, with every original source/frame hash checked. Widths and all saved q values are exact rationals/dyadics. Its Fraction sum evaluates

$$
\tau_{\rm end}=\frac{18}{125}
-\frac{33}{32}\sum_I q_I\Delta x_I
>\frac1{64}.
\tag{5}
$$

For exactly the energy selection cell10/segment3, the actual terminal-width display is

$$0.02163667990889687\ldots>0.015625.$$

Because every $q_I\ge0$, this also proves $1/64<\tau(x)\le18/125$ at every leaf and every internal point. The all-Metzler choice fails the same actual check, with negative terminal width; its midpoint phase estimate is not a substitute for (5).

The completed source `2026-11-13-exact-resume-hybrid-middle-leaves-v1.py` has SHA256 `aaecb235974878b88101bc07aec095b655cc1b796cbd92deb3c1206543fc0578`. The complete leaf stream is `2026-11-13-exact-resume-hybrid-leaves-r1-leaves.jsonl.gz`, 1656696 bytes, SHA256 `dadf463497d12f85e5fb3046d46eb6d2d2b2fa26ca36d3c19fbd061c4ea1fad1`. Its summary retains the individual segment costs and all tested exact selections. The actual resource wrapper returned exit 0, wall 66.182956219 seconds and peak 32944 KiB. This is an evaluation of the same certified whole-leaf coefficient boxes, not a new background ODE or a change to the original Taylor tolerances.

## 4. Whole-leaf forced responses to be consumed

For a matrix leaf let $E=\exp(\widehat M_I\Delta)$ and let $M_I^+$ be obtained by replacing negative diagonal entries in $\widehat M_I$ by zero. For any incoming nonnegative bound $u_0$ and constant nonnegative forcing bound f,

$$
u_{\rm end}\preceq Eu_0+\Delta\exp(M_I^+\Delta)f,
$$
$$
u(t)\preceq\exp(M_I^+\Delta)(u_0+\Delta f),
\qquad0\le t\le\Delta.
\tag{6}
$$

Indeed, the exponential of a Metzler matrix preserves the positive cone; increasing its entries increases the positive semigroup. All entries of $M_I^+$ are nonnegative, so its exponential is also entrywise increasing in elapsed time. Applying these facts to the exact Duhamel formula proves both bounds in (6).

For an energy leaf the scalar equation with the coefficient in (4) gives the exact affine comparison endpoint. The comparison's derivative has fixed sign, so its maximum over the leaf is the larger of its initial and endpoint values. The forcing is $c_{\rm bg}V_I^p/b$ for each of the original materials $p=2,1,0$ and a unit weak source mass.

The subsequent numerical consumer must retain both genuine initial columns, all original source positions and the whole-leaf targets. Source outputs divide by the actual target $V_I$ before separate component suprema. A weak source to strong output pays $1+m_+$; initial-to-initial strong weights cancel. A mode window containing several even modes still receives only the shared modal mass, with the supremum of its per-mode bounds, rather than a gratuitous mode-count multiplier.

These statements prove that the proposed interval-frequency comparison is legal. They do not state that its full response has run, that its kernel is small enough, or that the coupled low/middle/high and cut equations are closed.
