# R144 supplement: root angular tame flow with one high background factor

Date: 2026-11-27.
Session: visible-exact-astra-fb31ed6-20261127 / geometric_closure.

This gives every integer angular order for the actual negative root
Cauchy flow on the full-tail low-norm domain of
[NR](R144-supplement-actual-negative-and-root-propagation-in-a-full-tail-neighbourhood.md).
The only background smallness is its existing real $A^3$ bound
$10^{-6}$. For order $n$, the possibly large background norm
$A^{n+4/3}$ appears once and linearly. It does not enter a growth
exponential or a denominator.

The first angular increment already needs no additional regularity
assumption. At the actual radius-$1/200$ root-to-cut window it gives

$$
 \sup\|h\|_{H^1}
 <15\,\mathcal D_1+17200\,\mathcal D_0,\qquad
 \mathcal X_j=H^{j+1/3}\oplus H^j,
 \tag{RT.1}
$$

where $\mathcal D_j$ includes the true root input, ordinary
$L^1_r\mathcal X_j$ source and every original actual jump. Combining
this with the completed strict theorem gives a full root-to-waist
$H^1$ estimate below. Both means, the nonmonotone root-weight fee,
both endpoints of the true root enclosure and all original jumps
are retained.

The source increment in (RT.1) matches the mixed root trace actually
provided by the new
[positive H1 inverse](R144-supplement-real-H2-exterior-DN-and-one-angular-positive-high-inverse.md).
It does not invert the finite/high coupling or the complete return
operator.

## RT1. Same intrinsic root weight and exact differentiated equation

The background is $Q=\widetilde Q_\delta+q$, with
$|\delta|\le10^{-10}$ and
$\sup_r(\|q_1\|_{A^3}+\|q_2\|_{A^3})\le10^{-6}$ on the domain of NR.
Every root window considered lies above $9/50$, so the intrinsic
metric bump is identically zero there. Its actual mean, including
the unknown mean, still determines the characteristic principal
speed. No radial derivative of $q$ or of that mean is assumed.

Write $\varrho=r_*-r$, and use the exact multiplier of NR.15:

$$
 \Lambda_j=(1+16j^2)^{1/2},\quad
 x=\varrho\Lambda_j^{2/3},\quad
 w_j^2=\kappa^2+\Lambda_j^{-2/3}e^{-x},\quad
 \theta_j=e^{-(13/10)(1-e^{-x})},\quad
 M=\operatorname{diag}(\theta/w,\theta).
 \tag{RT.2}
$$

The following are already paid on the entire root enclosure:

$$
 \begin{gathered}
 \kappa^2\le K_+=1.049,\quad \kappa\le q_+=1.025,\quad
 w\le W=1.432,\quad \theta^{-1}<4,\quad w\ge\Lambda^{-1/3},\\
 |\eta_Q|<13/10,\qquad
 \left|\partial_{\log\Lambda}\log M_\nu\right|\le1/3 .
 \end{gathered}
 \tag{RT.3}
$$

The intrinsic nonmonotone radial weight term is included in NR's
actual growth $G(\varrho)\ge0$. The complete principal cancellation
in E.5 of the
[original root theorem](R133-supplement-full-real-large-root-Cauchy-two-source-windows.md)
holds for $M\partial_\phi^nh$ at every $n$, because $M$ and angular
differentiation commute. It is not replaced by a bound on a
first-order ordinary-source perturbation.

Let $\mathcal A_Q$ be the full physical $r$-operator NT.5 in
[the strict tame theorem](R144-supplement-strict-angular-tame-Cauchy-flow-with-one-high-background-factor.md).
Thus

$$
 \begin{gathered}
 \mathcal A_Qh=(dI_2+\gamma mJ)h_\phi+L_0h
       -2\beta Q_\phi I(Q^tDh)+\gamma\langle h_2\rangle JQ_\phi,\\
 d=-\beta I(Q^tDQ),\quad
 D=\operatorname{diag}(1,K),\quad
 J=\begin{pmatrix}0&K\\-1&0\end{pmatrix},\quad m=\langle Q_2\rangle,\\
 L_0=\beta\operatorname{diag}(-1,1)
            -\beta(Q^tDQ)I_2-2\beta Q(Q^tD).
 \end{gathered}
 \tag{RT.4}
$$

Put $h_\varrho=-\mathcal A_Qh+f$ and $w_n=\partial_\phi^nh$.
The exact equation is

$$
 (w_n)_\varrho
 =-(\mathcal A_Q+n d_\phi I_2)w_n
              +\partial_\phi^nf-\mathcal R_n(Q,h),
 \tag{RT.5}
$$

where

$$
 \begin{aligned}
 \mathcal R_n={}&
 \sum_{a=2}^n{n\choose a}d^{(a)}
                                 \partial_\phi^{\,n-a+1}h\\
 &+\sum_{a=1}^n{n\choose a}L_0^{(a)}
                                 \partial_\phi^{\,n-a}h\\
 &-2\beta
 \sum_{\substack{a+b+c=n\\a+b\ge1}}
 {n!\over a!\,b!\,c!}\,
 Q^{(a+1)}I((Q^{(b)})^tD\,\partial_\phi^ch)
          +\gamma\langle h_2\rangle JQ^{(n+1)} .
 \end{aligned}
 \tag{RT.6}
$$

Here $Q^{(a)}=\partial_\phi^aQ$, including $Q^{(0)}=Q$.
The independent source is $f$, with the orientation sign already
absorbed. At every original impulse,
$[w_n]_i=\partial_\phi^nj_i$.
Coefficient jumps are not new state impulses.

The angular derivative of the radial constant $m$ is zero. That
identity explains the absence of a derivative of $\gamma mJ$ in
(RT.6). The original mean $\langle h_2\rangle$ remains in the last
term. Although $w_n$ has zero mean when $n\ge1$, no original
mean forcing or attached mean row is removed. The full energy
estimate can be applied to (RT.5), including its exact mean
compatibility.

## RT2. Highest derivative growth uses only the low background

For arbitrary signed frequencies, including zero, (RT.3) implies

$$
 |M_{\nu,k}/M_{\nu,l}|\le(1+|k-l|)^{1/3}.
 \tag{RT.7}
$$

This bound has no finite lag restriction. In particular

$$
 \|M d_\phi M^{-1}\|_{2\to2}
 \le\|d_\phi\|_{A^{1/3}}
 \le2(1.049)(8.732+10^{-6})^2<161 .
 \tag{RT.8}
$$

The last estimate uses the complete compact-centre
$A^{1/3}$ bound from TH and the actual unknown $A^3$ norm.
The computed positive expression is below159.967971392.
The mean-zero projection in
$d_\phi=-\beta P_{\ne0}(Q^tDQ)$ is contractive in the Wiener norm.

Thus the auxiliary highest-derivative flow in (RT.5) has energy
growth at most $G+161n$. In particular no high background norm
appears in its exponential.

For a passed root radius $R\le1/50$ let
$\ell=R+\omega$, where the original root width is
$\omega=9\,10^{-13}$, and define

$$
 g_R=\left(1-{161\ell\over16}\right)^{-16}.
 \tag{RT.9}
$$

The denominator is positive on all six completed windows.
Since $e^x\le(1-x/16)^{-16}$ for $0\le x<16$, the extra
homogeneous growth at order $n$ is at most $g_R^n$.
The enlargement by $\omega$ is retained in this nonnegative
growth comparison. Ordinary-source lengths below are the actual
root-to-point lengths, at most $R$.

## RT3. A full-frequency tame bound in the actual root energy

Use Euclidean-pair Wiener norms, physical frequencies $4\mathbb Z$,
and the following convenient fixed low bounds:

$$
 Q_0=6.408,\quad Q_1=11.846,\quad
 Q_{4/3}=34.142,\quad Q_{7/3}=4404.190.
 \tag{RT.10}
$$

They bound the actual nearby $\|Q\|_{A^s}$ at the indicated orders.
Only the known degree32 centre uses
$\|Q_*\|_{A^{7/3}}\le129\|Q_*\|_{A^{4/3}}$.
The unknown tail is charged by $A^3$, without assigning it a
frequency cutoff.

For $n\ge1$ set

$$
 B_{n+4/3}=\sup_{\varrho}\|Q(\varrho)\|_{A^{n+4/3}},
 \quad
 b=2,\quad g=7,\quad
 C_L=8b(K_++q_++W),\quad C_P=8bW(41/100).
 \tag{RT.11}
$$

The high norm $B_{n+4/3}$ is required to be finite, not small.
At $n=1$ it is already bounded by (RT.10).
Define

$$
 \begin{aligned}
 L_n={}&2^n(C_L+bK_+)Q_{4/3}^2
             +3^n C_P(Q_0Q_{7/3}+Q_{4/3}Q_1),\\
 H_n={}&2^{2n+1}(C_L+bK_+)Q_0
             +6^n C_P(Q_0+Q_{4/3})+4gq_+ .
 \end{aligned}
 \tag{RT.12}
$$

Then the entire remainder obeys the actual-energy inequality

$$
 \boxed{\quad
 \|M\mathcal R_n(Q,h)\|_2
 \le L_n\|M\partial_\phi^{\,n-1}h\|_2
       +H_n B_{n+4/3}\|Mh\|_2 .
 \quad}
 \tag{RT.13}
$$

Here is a direct proof of all its terms.

For the diagonal local entries, (RT.7) charges the coefficient
lag by $(1+|\lambda|)^{1/3}$. For the upper off-diagonal entry,
retain $K/w$ before estimating, so its norm is at most $q_+$.
For the lower entry retain $w\le W$. The two $\theta$ factors
cost at most4. Expanding the quadratic expression for $L_0$
in (RT.4), its complete ordered two-factor coefficient kernel
is consequently dominated by $C_L$ times the convolution of
the two Euclidean absolute Fourier sequences, with that same
$(1+|\lambda|)^{1/3}$ weight. This constant covers both
diagonal entries and both off-diagonal entries. The differentiated
constant part $\beta\operatorname{diag}(-1,1)$ is zero.

If $a\ge1$ and $a\le n$,

$$
 |\lambda|^a|k|^{n-a}
 \le|\lambda|\,|k|^{n-1}+|\lambda|^n .
 \tag{RT.14}
$$

For the lower drift terms $a\ge2$, their coefficient has one
fewer angular derivative because $d=-\beta I(Q^tDQ)$:

$$
 |\lambda|^{a-1}|k|^{n-a+1}
 \le|\lambda|\,|k|^{n-1}+|\lambda|^n .
 \tag{RT.15}
$$

Each inequality follows by separating $|k|\ge|\lambda|$ and
its complement. Multiplying by the weight from (RT.7), the
low product is bounded by $Q_{4/3}^2$. The high product is
bounded by

$$
 \|\,|Q|*|Q|\,\|_{A^{n+1/3}}
 \le2^{n+1}Q_0 B_{n+4/3}.
 \tag{RT.16}
$$

This is the elementary inequality for a power of the sum of
the two coefficient frequencies. The binomial coefficients
sum to at most $2^n$, giving the first terms of (RT.12).
For the drift the coefficient constant is $bK_+$.

For an ordered primitive word use its true intermediate
frequency $k+\lambda_2$. If it is zero the primitive removes
exactly that mode. Otherwise

$$
 {\Lambda_{k+\lambda_1+\lambda_2}^{1/3}\over|k+\lambda_2|}
 \le(1+|\lambda_1|)^{1/3}
       {\Lambda_{k+\lambda_2}^{1/3}\over|k+\lambda_2|}
 <{41\over100}(1+|\lambda_1|)^{1/3}.
 \tag{RT.17}
$$

This is the full $L^2\to H^{1/3}$ primitive bound; the smallest
nonzero physical frequency is4. Also
$\|DM^{-1}\|\le4W$, because $K_+<W$.
Thus the complete ordered primitive kernel is bounded by $C_P$
times

$$
 (1+|\lambda_1|)^{1/3}
 |\lambda_1|^{a+1}|\lambda_2|^b|k|^c,
 \qquad a+b+c=n,\quad a+b\ge1 .
 \tag{RT.18}
$$

For $L=|\lambda_1|+|\lambda_2|$, separation at $|k|=L$
gives

$$
 |\lambda_1|^{a+1}|\lambda_2|^b|k|^c
 \le|\lambda_1|L|k|^{n-1}+|\lambda_1|L^n.
 \tag{RT.19}
$$

The first convolution costs at most
$Q_0Q_{7/3}+Q_{4/3}Q_1$.
The second costs at most
$2^n(Q_0+Q_{4/3})B_{n+4/3}$.
The multinomial coefficients sum to at most $3^n$.
This gives both primitive terms of (RT.12). Every intermediate
frequency remains in (RT.17); no high projection was inserted
between the two multiplications.

Finally
$|\langle h_2\rangle|\le4\|Mh\|_2$ and
$\|MJQ^{(n+1)}\|_2\le q_+\|Q^{(n+1)}\|_2$.
The latter uses $|K|/w\le\kappa$ in the first row and
$\theta\le1$ in the second. This proves the final term
$4gq_+ B_{n+4/3}\|Mh\|_2$ and retains the actual
independent mean path.

Every high coefficient norm in this proof is multiplied by a
low coefficient norm from (RT.10). There is no product of two
uncontrolled high background norms.

## RT4. Explicit tame recurrence in the original source and trace units

For $j\ge0$ define

$$
 \begin{gathered}
 \mathcal X_j=H^{j+1/3}\oplus H^j,\\
 \mathcal D_j=
 \|h(0)\|_{\mathcal X_j}
 +\int_0^R\|f(\varrho)\|_{\mathcal X_j}\,d\varrho
 +\sum_i\|j_i\|_{\mathcal X_j}.
 \end{gathered}
 \tag{RT.20}
$$

The norms are of the actual root input and original sources.
For an $L^2_\varrho\mathcal X_j$ source, replace the integral by
at most $\sqrt R$ times that norm, or the square root of its
smaller actual support length. Impulses get no length factor.
At the true root, the identity
$M(0)=\operatorname{diag}(\Lambda^{1/3},1)$ proves these exact
anisotropic units.

Let $C_0^Q(R)$ be the already completed NR root constant in its
strong window. It bounds $4W_R\exp\int G$, where $W_R$ is the
original complete intrinsic weight maximum for that radius.
Define the entirely low-norm recurrence

$$
 A_0=1,\qquad
 A_n=(1+g_R^n R L_n)A_{n-1}
                       +g_R^n(1+R H_n)\quad(n\ge1).
 \tag{RT.21}
$$

All these constants are finite positive rational expressions.
They are independent of $B_{n+4/3}$.
Then

$$
 \boxed{\quad
 \sup_{0\le\varrho\le R}\|h(\varrho)\|_{H^n\oplus H^n}
 \le 2^n(n+1)\,C_0^Q(R) A_n
       [\,\mathcal D_n+B_{n+4/3}\mathcal D_0\,].
 \quad}
 \tag{RT.22}
$$

To see the recurrence, write $\Phi(\varrho)=\int_0^\varrho G$,
$E_j=\|M\partial_\phi^jh\|_2$ and
$v_j=\sup e^{-\Phi}E_j$.
The undifferentiated equation gives $v_0\le d_0$, where $d_j$
is the sum of the $\mathcal X_0$ norms of the $j$th derivatives
of the same data, sources and jumps. Equations (RT.5),(RT.8),
(RT.13) give

$$
 v_j\le g_R^j\{d_j+R L_jv_{j-1}
                          +R H_jB_{j+4/3}d_0\}.
 \tag{RT.23}
$$

Summing through $n$, using monotonicity of the background norm
and (RT.21), bounds the sum by
$A_n[\sum_{j=0}^n d_j+B_{n+4/3}d_0]$.
Since $\sum d_j\le(n+1)\mathcal D_n$, and the derivative-vector
Sobolev norm is at most $2^{n/2}$ times the sum of derivative
norms, (RT.22) follows with the stated convenient rational factor.

The common factor $e^\Phi$ is stripped before applying Duhamel.
Thus the original growth over two adjacent subintervals is
counted once, not squared. The same argument handles every
actual source insertion and impulse in its correct order.
The original $\omega$ appears in the whole enclosing growth
bound, but it is not assigned to a physical source length.

The energy argument begins on smooth full Fourier solutions.
Density and the same uniform multiplier estimates extend it
whenever the data and the single high background norm in
(RT.22) are finite. There is no requirement that all high
background norms be small simultaneously.

## RT5. Actual first increment on all six completed root radii

The general tame constants are intentionally conservative. At
$n=1$ there is no lower drift term, and a sharper direct bound
is useful. Let

$$
 \begin{gathered}
 U=.629+\rho,\quad V=6.407+\rho,\quad
 U_1=V_1=5.438+\rho,\quad \rho=10^{-6},\\
 U_2=V_2=128(5.438)+\rho,\quad
 U_{2,1/3}=128(5.06)(5.438)+\rho,\\
 Q_{0,1/3}=8.732+\rho,\qquad
 Q_{1,1/3}=5.06(5.438)+\rho .
 \end{gathered}
 \tag{RT.24}
$$

Only the known centre uses the factor128 or
$129^{1/3}<5.06$; the unknown's first two derivatives, with
the indicated fractional weights, are bounded directly by $A^3$.

The complete first remainder is
$L_{0,\phi}h-2\beta Q_{\phi\phi}I(Q^tDh)
-2\beta Q_\phi I(Q_\phi^tDh)
+\gamma\langle h_2\rangle JQ_{\phi\phi}$.
Its norm in the root energy is at most $R_1\|Mh\|_2$, where

$$
 \begin{aligned}
 R_1={}&8bK_+Q_{0,1/3}Q_{1,1/3}
        +8b(q_++W)(U_1V+UV_1)\\
 &+8b(WU+K_+V)\{(41/100)U_{2,1/3}+V_2/4\}\\
 &+8b(WU_1+K_+V_1)\{(41/100)Q_{1,1/3}+V_1/4\}\\
 &+4gq_+\{128(5.438)+\rho\}
 <225561.188939<230000.
 \end{aligned}
 \tag{RT.25}
$$

For the two primitive terms this is exactly the ordered E.9
argument with the differentiated outer or inner coefficient,
respectively. For the diagonal reaction, (RT.7) charges its
$A^{1/3}$ norm. For the last mean term the complete pair's
second-derivative bound is used. No mean direction is absent.

Applying the normalized Duhamel argument at orders0 and1
gives the sharper actual bound

$$
 \sup\|h\|_{H^1}
 \le C_0^Q(R)
   [\,g_R\mathcal D_1+(1+230000R g_R)\mathcal D_0\,].
 \tag{RT.26}
$$

The following coefficients are strict upper bounds for this
formula, using the completed original root ball and NR's
same full .0200 growth enlargement.

| Exact radius | Coefficient of $\mathcal D_1$ | Coefficient of $\mathcal D_0$ |
|---|---:|---:|
| $1/1000$ | 5.040143 | 1163.519996 |
| $1/500$ | 6.458679 | 2975.657463 |
| $1/200$ | 14.920329 | 17164.909681 |
| $1/100$ | 75.952660 | 174705.035147 |
| $3/200$ | 440.740132 | 1520585.604856 |
| $1/50$ | 2681.318389 | 12334138.196346 |

These are all complete-root estimates. No original growth
integral is repeated. The convenient selected-window form is
(RT.1), and its independent low estimate remains
$\sup\|h\|_2<6.532358\,\mathcal D_0$.
Strict inequalities are understood for nonzero data; zero
data gives the exact zero solution.

## RT6. Actual root-to-waist H1 composition at the original cut

Use the actual original cut
$r_c=2333968743003/10^{13}=r_+-1/200$.
Its true distance to the root is at most $1/200$.
The root output in (RT.26) is a true solution trace at this
cut, and is therefore a legitimate input for
NT's strict $H^1$ flow. No arbitrary radial $L^2$ trace is taken.

For sources and jumps strictly below the cut put

$$
 \mathcal S_j=\int_0^{r_c}\|f(r)\|_{H^j\oplus H^j}\,dr
                        +\sum_{r_i<r_c}\|j_i\|_{H^j\oplus H^j}.
 \tag{RT.27}
$$

An impulse at the cut is assigned once, to either the outgoing
root data or the incoming strict data, according to the
original interface convention.
The actual strict estimate
$340(\|h(r_c)\|_{H^1}+\mathcal S_1)
+1120000(\|h(r_c)\|_2+\mathcal S_0)$ then gives

$$
 \boxed{\quad
 \|h(0)\|_{H^1\oplus H^1}
 <5100\,\mathcal D_1
  +13200000\,\mathcal D_0
  +340\,\mathcal S_1+1120000\,\mathcal S_0 .
 \quad}
 \tag{RT.28}
$$

The two root coefficients are finite positive combinations
of the actual entries in the preceding table and NR's complete
low root constant. Ordinary $L^2$ root sources pay
$\sqrt{1/200}$ in their respective $\mathcal X_j$ norms;
ordinary strict sources pay the square root of their actual
support length. Root and strict source spaces are distinct.

If the output is the actual nearby waist density
$w_Q=n_QT(\kappa)h$, NR's full waist factor gives

$$
 \|w_Q(0)\|_{H^1}\le
 {1.000002\over.9616}\|h(0)\|_{H^1}
 <1.041\|h(0)\|_{H^1}.
 \tag{RT.29}
$$

This includes its complete mean vector because the
normalization is angularly constant. It does not identify this
nearby density with the old finite193 normalization, nor
change the original observations.

For higher orders, (RT.22) composes with NT's complete
single-high-background strict estimate on the same actual
solution. Such composition remains linear in the high
background norm: both use low-data bounds for the factor
multiplying that high norm. The first increment (RT.28)
is the explicit numerical instance needed here.

## RT7. Arithmetic and scope

The reader
[fourfold_codazzi_compact_root_angular_tame_saved_bounds.py](../scripts/fourfold_codazzi_compact_root_angular_tame_saved_bounds.py)
performs 19 exact rational comparisons on the already completed
small root conclusion and the stated scalar inequalities.
It evaluates no native coefficient row, Fourier tail, radial
flow or growth integral. Its first-commutator sum retains the
five separately displayed positive contributions; the two
primitive words and the independent moving mean are all present.

Together with NT this supplies a real angular tame Cauchy
operator through the entire negative side for arbitrary
finite high background norms on the fixed low $A^3$ domain.
QH separately supplies the first positive high increment with
the actual physical DN boundary. These are concrete
source/state/trace components for the coupled problem.
No finite/head Schur denominator, all-order positive DN tame
bound, or completed nonlinear geometric family follows merely
from their existence.
