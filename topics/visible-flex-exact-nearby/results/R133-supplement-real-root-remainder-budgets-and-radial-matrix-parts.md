# R133 supplement: real root remainder budgets with radial constant matrix parts retained

2026-11-14, phase_inverse.

This is the concrete norm recipe for the leading-amplitude consumer of
[the exact old-circle inverse remainder](R133-supplement-exact-old-circle-inverse-remainder-in-negative-source-window.md), especially (U.20)--(U.29).
It uses only the completed original root and first-forcing rows and the
six already certified forcing windows. It does not solve a target or
construct higher radial intrinsic jets.

## B.1. Real windows and complete coefficient moments

Fix one of the six actual root windows, and let $R$ denote its maximum
possible true $|\rho|$, including the width of the exact root enclosure.
Use the actual $A_-,A_+,a_+,D_1$ and the constants $c_{A,1},c_{A,2},C_2,C_3$
from that window's complete forcing record. All parameter statements are
for the same real $|\delta|\le10^{-8}$ at $\eta_0$.

A complete old Fourier derivative bound at width $\sigma=1/16$ is
$F_p\ge\sum_k|4k|^p e^{\sigma|4k|}|\widehat f(k)|$.
For $q>p$ it gives

$$
 \|\partial^q f\|_{\mathcal A_0}
 \le \left(\frac{q-p}{e\sigma}\right)^{q-p}F_p.
 \tag{B.1}
$$

For $q=p>0$, or for a coefficient with exactly zero mean,
one may instead use the factor $e^{-4\sigma}$. For $q<p$ on
the nonmean part, the valid factor is
$4^{q-p}e^{-4\sigma}$. If $q=0$ and the mean is not zero,
add its separate absolute bound before using that nonmean estimate.
Every selected minimum is a minimum of valid full bounds.
No nonmean coefficient is inferred by subtracting two unrelated
interval enclosures.

The complete moment needed in (U.24) is then bounded by

$$
 m_3(f)\le F^{(0)}+3F^{(1)}+3F^{(2)}+F^{(3)}.
 \tag{B.2}
$$

For products, the derivative majorants use their complete Leibniz
convolutions. The given mean of $v$ and its radial derivatives are
retained. The odd coefficients $u,u_r$ and the drift $d$ have
exact zero mean. The nonmean part $v-m$ has
$\|v-m\|_{\mathcal A_0}\le\|v_\phi\|_{\mathcal A_0}/4$.

For the one-gain commutator (U.3), write
$P_i=m_3(\partial^i p)$, $Q_i=m_3(\partial^i q)$ and
$D_i=m_3(\partial^i d)$. A sufficient cost is

$$
 \|\mathcal C(p,q)\|_{H^s\to H^{s+1}}
 \le C_I\{D_0(P_1Q_0+P_0Q_1)+3P_0D_1Q_0\}.
 \tag{B.3}
$$

It holds for both $s=-8/3$ and $s=-5/3$ under (U.24).
The three copies of $P_0D_1Q_0$ retain the two rank maps and
the middle commutator. A radial derivative of $\kappa T_pIT_q$
uses (U.4) with all three terms.

## B.2. Subtracting genuine radial constants before angular Cauchy

The full inverse point matrix has bound
$H_*\ge\|H^{-1}\|$. Put

$$
 E=e^{D_1R},\quad j=E-1,\quad
 A_\phi^+=Rc_{A,1},\quad
 Y=\tfrac23R A_-^{-1/3}A_\phi^+,\quad
 T^+=R A_+^{2/3},\quad
 \Delta_H=j+\max(1,T^+)Y .
 \tag{B.4}
$$

These are complete old-angle complex-strip bounds. Since
$H-i\epsilon1$ has norm at most $\Delta_H$, the exact resolvent
identity gives

$$
 \|H^{-1}+i\epsilon1\|\le H_*\Delta_H.
 \tag{B.5}
$$

The subtracted matrix is independent of $\phi$. Consequently for
any positive integer $k$, angular Cauchy from the actual leading
strip $\sigma_a=3/64$ yields

$$
 \|\partial_\phi^k H^{-1}\|
 \le k!\sigma_a^{-k} H_*\min(1,\Delta_H).
 \tag{B.6}
$$

This improves a derivative bound when the matrix oscillation is
small; its zeroth-order bound remains $H_*$.

There is a corresponding exact radial reference for $H_D$.
The Abel formula for the genuine fold defines

$$
 \overline A(\rho)=\frac32\int_0^1s^{1/2}a(s\rho)\,ds,
 \qquad |A-\overline A|\le a_+j=:\Delta_A .
 \tag{B.7}
$$

The flow Jacobian in the original integral differs from 1 by
at most $j$; the radial function $a$ is independent of the
angle. Thus (B.7) retains its actual radial dependence and
does not freeze the target at its root value. On the complex
angular strip both $A$ and the straight segment to the positive
real $\overline A$ have real part at least $A_-$.

Set

$$
 \begin{gathered}
 \overline T=-\rho\overline A^{2/3},\qquad
 \overline D_T=a\overline A^{-1/3},\\
 \Delta_T=\tfrac23R A_-^{-1/3}\Delta_A,\qquad
 \Delta_{D_T}=a_+\{A_-^{-1/3}j+
                         \tfrac13A_-^{-4/3}\Delta_A\},\\
 D_X^+=\tfrac23a_+R^2 A_\phi^+ .
 \end{gathered}                                       \tag{B.8}
$$

The exact identities $DX=-\tfrac23a\rho^2A_\phi$ and
$DT=aA^{-1/3}X_\phi$ give

$$
 H_D^{\rm rad}=
 \overline D_T\begin{pmatrix}0&\overline T\\1&0\end{pmatrix},
$$

$$
 \|H_D-H_D^{\rm rad}\|
 \le D_X^++\max(1,T^+)\Delta_{D_T}
                       +a_+A_-^{-1/3}\Delta_T
 =:\Delta_{H_D}.                                     \tag{B.9}
$$

Every angular derivative of $H_D^{\rm rad}$ is zero. If $H_{D,*}$
is the actual complete zeroth-order bound, therefore

$$
 \|\partial_\phi^kH_D\|
 \le k!\sigma_a^{-k}\min(H_{D,*},\Delta_{H_D}),
 \qquad k\ge1.                                       \tag{B.10}
$$

Only derivatives of a radial constant have been cancelled.
Neither the radial dependence nor a lower-order matrix entry is
discarded.

## B.3. Finite angular-jet arithmetic for the full residual

Use four ordinary angular derivatives of amplitude majorants.
For a known analytic derivative of order $p$ bounded by $V_p$
on the same leading strip, the $k$th real derivative for $k\ge p$
has bound $(k-p)!\sigma_a^{p-k}V_p$.
The minimum over the actually recorded derivatives is valid.
The saved leading $w_0$ bounds supply orders 0, 1 and 2; the
saved $\partial_rw_0$ bounds supply orders 0 and 1.
Their higher angular derivatives are obtained this way.

Products of scalar, matrix and vector jets use ordinary Leibniz
coefficients. Use (B.6), (B.10) for the matrix jets, and the
complete original coefficient moments for $d,u,v$ and $\eta$.
This constructs bounds for every amplitude expression in
(U.21), (U.23), (U.26), (U.27) and (U.29).
The fourth angular derivative is sufficient even for
$\mathfrak D^2(H_Dw_0)$: the Airy operator itself consumes only
two derivatives after the two displayed angular derivatives.
There is no additional derivative of an Airy profile.

The exact $J$ windows are evaluated from the original
$\mathtt{one\_gain}$ rows as in (U.25), and the existing
$H^{-5/3}\to H^{-2/3}$ field is used after the scalar residual.

## B.4. A common integrable radial envelope

In A.7--A.11 of the real Airy operator proof set
$h=|T|=|\rho|A^{2/3}$, and let $N=4J_0$.
For all $0<|\rho|\le R$,

$$
 h^{-1/4}\le |\rho|^{-1/4}A_-^{-1/6},\qquad
 N^{-1/6}\le|\rho|^{-1/4}R^{1/4}N^{-1/6},
$$

$$
 h^{1/4}\le|\rho|^{-1/4}R^{1/2}A_+^{1/6}.
 \tag{B.11}
$$

The logarithmic angular derivative factors are bounded by

$$
 L_1=\tfrac23\,R c_{A,1}/A_-,\qquad
 L_2=\tfrac23\{R c_{A,2}/A_-+(R c_{A,1}/A_-)^2\}.
$$

Use the actual real-map bounds
$m=2-E$, $M=E$, $F_2=RC_2$, $F_3=RC_3$.
The central and two oscillatory phase tables are retained on
the negative side; the exact real decaying table is retained
on the positive side. Equations (B.11) extract a single
$|\rho|^{-1/4}$ factor from the complete operator cost.
All scalar and matrix jet operations preceding that factor
are finite.

For each original closed common cell this gives constants
$\widehat C_1,\widehat C_2$ such that the full nonlocal first-row
and independent even-mean residuals of the leading trial obey

$$
 \|(g_{1,\rm nl},g_2)(r)\|_{H^{-2/3}\times H^{-2/3}}
 \le|\rho|^{-1/4}
          (\widehat C_1^2+\widehat C_2^2)^{1/2}
          \|c\|_{H^{-4/3}}.
 \tag{B.12}
$$

The first constant includes the final complete old $J$ factor;
the second includes (U.29). Each coefficient cell retains its
own true identity and full mean.

## B.5. Integration with the actual root interval

Let the certified root interval be $[r_-,r_+]$.
For a cell $[\ell,h]$ strictly below $r_-$, a valid upper
bound on the squared radial singular weight is

$$
 \int_\ell^h|\rho|^{-1/2}\,dr
 \le2\{\sqrt{r_--\ell}-\sqrt{r_--h}\}.
 \tag{B.13}
$$

Above $r_+$ use
$2\{\sqrt{h-r_+}-\sqrt{\ell-r_+}\}$.
For any cell inside the root bracket, either one-sided part has
weight at most $2\sqrt{h-\ell}$. The original closed partition
already contains both root endpoints. These statements hold
for every true root in its full interval.

Multiply each weight by the cell's
$\widehat C_1^2+\widehat C_2^2$, sum the complete cover and take
the square root. This is an ordinary radial $L^2$ source bound,
with all angular modes present. On the negative side it can be
composed with the actual same-family Cauchy source factor and
primitive bound. On the positive side it stays a raw source
bound until the separately proved positive source window is
explicitly consumed.

This calculation pays the complete old $I/J$ remainder and
even-mean source of the leading trial. It does not pay
$n^{-1}\mathcal L_0w_1$, the remaining first-corrected trial
residual, cutoff sources, later seams or a complete return norm.
Its success condition is a complete finite budget, not a preset
claim that frequency 97 is already sufficient.
