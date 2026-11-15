# R133 supplement: complete primitive and mean propagation on the selected strict negative interval

2026-11-15, visible-exact / phase_inverse.

**Proved analytic identities and a conditional scalar consumer contract.**
This note propagates the complete angular primitive and the independent
mean in ordinary L2. Its initial data may therefore be supplied by the
already completed negative Hminus1 Cauchy theorem. The old 3071-row H1
four-state propagator is not used as an L2 primitive propagator.

The real family is the same exactly repaired
$Q_\delta=Q_0+\delta Z_{\rm can}$, at fixed $\eta_0$ and
$\nu=\nu_0+\delta$. The declared new range is
$|\delta|\le d_*=10^{-8}$, subject to the original compact metric type
interval and the explicit positive denominator tests below.
The state and direction definitions are respectively
440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47 and
6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04.
This is the explicit reference family, not an assertion that its
nonlinear residual is zero.

The new scalar evolution, its numerical constants and any use of the
current genuine source remain to be evaluated in public Actions.
All old targets, Fourier sums, coefficient enclosures, grouped curvature
integrals and successful source consumers remain read-only.

## 1. Exact coordinates, with both mean coordinates retained

Use Q.4--9 of
[the complete moving equation](R133-supplement-negative-quadratic-density-and-full-frequency-transport.md)
on $0\le r\le r_c<r_*$, with its true compact metric and the same moving
angle. The physical Fourier frequencies are $4j$, the circle measure
is normalized, and all two-component norms are Euclidean. Write
$$
 q=\sqrt{-K}>0,\quad \eta=-\gamma m>0,\quad
 S=u^2+Kv^2,\quad d=-\beta I S,\quad
 I=\partial_\phi^{-1}(1-\Pi),\quad m=\langle v\rangle .
 \tag{SP.1}
$$
Let $T(q)$ be the exact matrix in N.4 of
[the strict cut theorem](R133-supplement-complete-negative-source-to-strict-density-cut-readout.md).
To avoid the radial derivative of the approximate reference mean, first
use the unscaled characteristic state
$$
 \xi=T(q)h,\qquad y=I\xi,\qquad z=\Pi\xi,\qquad
 \xi=y_\phi+z,\qquad \Pi y=0 .
 \tag{SP.2}
$$
The relation to the original quadratic density is
$w=n_g\xi$, where $n_g=a_{\rm phys}^2/m^2$ is radial.
In particular $Iw=n_gy$ and $\Pi w=n_gz$ exactly.
No integration constant or mean is reset.

Put
$$
 C=\operatorname{diag}(d+\eta q,d-\eta q),\qquad
 \ell_0=-2\beta\langle S\rangle,\qquad
 B_{\sigma,-\sigma}=-\frac{q_r}{2q}-\beta(1+r_\sigma^2),
 \quad r_\sigma=u+\sigma qv .
 \tag{SP.3}
$$
The diagonal of $B$ is zero. The complete nonlocal operator remains
$$
 (\mathcal N\xi)_\sigma
 =-\beta(r_\sigma)_\phi I(r_-\xi_++r_+\xi_-)
 -\frac{\sigma\gamma}{2}(r_\sigma)_\phi
                    \langle\xi_+-\xi_-\rangle .
 \tag{SP.4}
$$
Since $-2\beta S=2d_\phi+\ell_0$, Q.7 is
$$
 \xi_r=C\xi_\phi+(2d_\phi+\ell_0)\xi+B\xi+\mathcal N\xi+Tf .
 \tag{SP.5}
$$
This formula holds at the unsolved background. It has not used a
nonlinear equation for $m$.

## 2. The exact closed primitive--mean system

Define the full matrix
$$
 A=d_{\phi\phi}\operatorname{Id}+B_\phi .
$$
The primitive identities, including their constant Fourier outputs, give
$$
 \begin{aligned}
 y_r={}&\partial_\phi(Cy)+\ell_0y+P_\perp(By)-I(Ay)\\
       &+I[(2d_\phi\operatorname{Id}+B)z]
            +I\mathcal N(y_\phi+z)+ITf,\\
 z_r={}&-\langle Ay\rangle+
           (\ell_0\operatorname{Id}+\langle B\rangle)z
            +\langle\mathcal N(y_\phi+z)\rangle+\langle Tf\rangle .
 \end{aligned}\tag{SP.6}
$$
For example,
$$
 I(Cy_{\phi\phi}+2d_\phi y_\phi)
       =\partial_\phi(Cy)-I(d_{\phi\phi}y),\qquad
 I(By_\phi)=P_\perp(By)-I(B_\phi y).
 \tag{SP.7}
$$
In the first identity the constant output from the two terms cancels
exactly. In the second it is explicitly retained in $P_\perp$.
Averaging the same two complete terms gives
$-\langle(d_{\phi\phi}\operatorname{Id}+B_\phi)y\rangle$.
Also $\langle d_\phi\rangle=0$ and $\ell_0$ is radial. This proves both
rows of (SP.6), including their mean coupling.

For smooth inputs these are ordinary identities. The bounds below
remove every derivative of $y$ from the nonlocal terms, so the system
extends by density to $y\in L^2$, $z\in\mathbb C^2$ and the stated
ordinary source spaces. This is a full Fourier evolution, not a
finite matrix approximation to the angular equation.

## 3. Complete nonlocal fees without an angular derivative of the input

On one genuine closed radial cell take real upper bounds
$$
 b\ge|\beta|,\quad g\ge\gamma,\quad
 R\ge\sup_\phi\sqrt{u^2+q^2v^2},\quad
 L\ge\sup_\phi\sqrt{u_\phi^2+q^2v_\phi^2},\quad
 D\ge\|d_\phi\|_\infty .
 \tag{SP.8}
$$
These are complete pointwise bounds of the same real family.
Set
$$
 B_1=4bRL,\quad A_1=6bRL,\quad
 N_y=2bL(R+L/4),\quad
 N_z=bLR/2,\quad N_\gamma=gL .
 \tag{SP.9}
$$
Then $\|B_\phi\|\le B_1$ and $\|A\|\le A_1$, because
$|S_\phi|\le2RL$ and
$|r_\sigma(r_\sigma)_\phi|\le2RL$.

For the nonlocal row use the exact ordered identity
$$
 I(a\cdot y_\phi+a\cdot z)
       =P_\perp(a\cdot y)-I(a_\phi\cdot y)+I(a\cdot z),
       \qquad a=(r_-,r_+).
 \tag{SP.10}
$$
The complete primitive has L2 norm $1/4$; $P_\perp$ is an orthogonal
projection. Since $|a|\le\sqrt2R$ and $|a_\phi|\le\sqrt2L$,
$$
 \|\mathcal N(y_\phi+z)\|_2
        \le N_y\|y\|_2+(N_z+N_\gamma)|z| .
 \tag{SP.11}
$$
In the mean of this expression only the last, explicitly displayed
rank-one term of (SP.4) vanishes:
$\langle(r_\sigma)_\phi\rangle=0$. Thus
$$
 |\langle\mathcal N(y_\phi+z)\rangle|
        \le N_y\|y\|_2+N_z|z| .
 \tag{SP.12}
$$
The primitive nonlocal mean is not removed.

The other constant-to-primitive column obeys
$$
 \|I[(2d_\phi\operatorname{Id}+B)z]\|_2
        \le (D/2+B_1/16)|z| .
 \tag{SP.13}
$$
Indeed $d$ has mean zero, $2\|d\|_2\le D/2$, and
$IB=I^2B_\phi$ entrywise. These factors use the full $4\mathbb Z$
circle and no high-mode cutoff.

## 4. A common radial factor and two true comparison states

Use
$$
 Y=\sqrt q\,\|y\|_2,\qquad Z=\sqrt q\,|z| .
 \tag{SP.14}
$$
Their combined square is precisely
$$
 Y^2+Z^2
 =\|Ih_1\|_2^2+q^2\|Ih_2\|_2^2
                +|\Pi h_1|^2+q^2|\Pi h_2|^2 .
 \tag{SP.15}
$$
Thus the weighting is an exact change of norm, not a free passage
from a raw Hminus1 state to a raw L2 state.

Define the two radial-free complete physical logarithmic rates
$$
 \begin{aligned}
 F&\ge\sup_\phi\max\{\ell_1-d_\phi/2,\ell_2-d_\phi/2\},\\
 B_{\rm rev}&\ge\sup_\phi\max\{-\ell_1+d_\phi/2,-\ell_2+d_\phi/2\},\\
 \ell_1&=-\beta(1+3u^2+Kv^2),\qquad
 \ell_2=\beta(1-u^2-3Kv^2).
 \end{aligned}\tag{SP.16}
$$
The symbol $B_{\rm rev}$ is a scalar budget, not the matrix in (SP.3).

For $b_*=F$ in forward time and $b_*=B_{\rm rev}$ in reversed time,
put
$$
 \mathcal A(b_*)=
 \begin{pmatrix}
 \max\{0,b_*+D+(A_1+N_y)/4\}
       &D/2+B_1/16+(N_z+N_\gamma)/4\\
 A_1+N_y&\max\{0,b_*+N_z\}
 \end{pmatrix}.
 \tag{SP.17}
$$
Every entry is nonnegative. The complete upper-Dini inequalities are
$$
 \begin{aligned}
 D_r^+\binom YZ
   &\le[\mathcal A(F)+c_+\operatorname{Id}]\binom YZ+
                   \sqrt q\binom{\|ITf\|_2}{|\Pi Tf|},\\
 D_t^+\binom YZ
   &\le[\mathcal A(B_{\rm rev})+c_-\operatorname{Id}]\binom YZ+
                   \sqrt q\binom{\|ITf\|_2}{|\Pi Tf|},\qquad t=r_c-r,\\
 c_+&=\max(0,q_r/q),\qquad c_-=\max(0,-q_r/q).
 \end{aligned}\tag{SP.18}
$$
The source in the second row is evaluated at $r_c-t$.

Here is the radial cancellation before taking absolute values.
The symmetric off-diagonal part of $B$ is
$-q_r/(2q)-\beta(1+u^2+q^2v^2)$.
The scalar square-root weighting contributes $q_r/(2q)$ in forward
time and its negative in reverse time. Therefore
$$
 \begin{aligned}
 \frac{q_r}{2q}
 +\left|\frac{q_r}{2q}+\beta(1+u^2+q^2v^2)\right|
   &\le c_++|\beta|(1+u^2+q^2v^2),\\
 -\frac{q_r}{2q}
 +\left|\frac{q_r}{2q}+\beta(1+u^2+q^2v^2)\right|
   &\le c_-+|\beta|(1+u^2+q^2v^2).
 \end{aligned}\tag{SP.19}
$$
The remaining primitive logarithmic rate differs from its corresponding
rate (SP.16) by respectively $-d_\phi$ and $+d_\phi$.
This costs $D$, regardless of the sign of $\beta$.
For the constant vector $z$, averaging the corresponding pointwise
rate (SP.16) removes $d_\phi$ exactly and leaves an upper bound $F$
or $B_{\rm rev}$. This proves the two diagonal terms in (SP.17).
The inner product with $P_\perp By$ is the inner product with $By$
since $\Pi y=0$. Equations (SP.9)--(SP.13) give all other entries.

The radial term is scalar in the complete two-state system.
Removing it by an integrating factor exchanges no matrix products.
There is no factor $\exp\int|q_r/q|$ added independently to both
orientations.

## 5. Read the old complete rows and pay the selected family difference

The original strict native has SHA256
23a7554aa141b51b4c897f42399eb355d003d5fe5dd37b1c62f68025a4c8542a,
8499033 bytes, and 3071 complete closed rows through
$r_a=1191939371497/5000000000000$.
Its [actual theorem](R133-supplement-actual-final-strict-four-state-cover.md)
and [grouped variation theorem](R133-supplement-grouped-curvature-complete-reverse-energy.md)
are immutable inputs.

In that original native the quantities needed in (SP.16) are already
stored separately: the first forward physical energy diagonal, and the
ordinary second-component forward and reverse rates. Consequently
$F_0,B_0$ are obtained by taking their stated maxima; no old angular
enclosure is repeated and no two independent upper bounds are subtracted.
The saved $R_0,L_0,D_0,q_0$, full $|v_0|,|(v_0)_\phi|$ and actual
radial target balls remain on their complete original cells.
The subscript zero in this section denotes the original unrepaired
candidate at $\nu_0$, not a scalar mean.

The exact repair and the already proved complete response bounds give
$$
 \varepsilon_0=3.861\,10^{-18}+19d_*,
 \qquad \varepsilon_1=1.970\,10^{-17}+83d_*,
 \quad |Q_\delta-Q_{\rm old}|\le\varepsilon_0,\quad
 |(Q_\delta-Q_{\rm old})_\phi|\le\varepsilon_1 .
 \tag{SP.20}
$$
The constants 19 and 83 include the exact canonical response repair
and the full physical mean, as certified by the accepted response-repair
summary. They do not truncate the unknown variation $h$.

The exact compact metric relation is D.2 of
[the selected-parameter theorem](R133-supplement-exact-selected-parameter-core-differences-and-finite193-transfer.md):
$$
 \gamma_\delta=\gamma_0 e^{\delta w/2},\quad
 K_\delta=e^{-\delta w}(K_0+\delta T_0w_r),\quad
 T_0=\frac{\beta}{2\gamma_0^2a_{\rm phys}^2}.
 \tag{SP.21}
$$
In this equation $T_0$ is radial and is not the fold coordinate.
The radius $a_{\rm phys}$ and $\beta$ do not change.
The weight is $w=4096s^6(1-s)^6$,
$s=(r-1/20)/(13/100)$ on the compact support, and zero outside.
Valid complete bounds are
$$
 W=1,\quad W_1=2400/13,\quad W_2=5280000/169 .
 \tag{SP.22}
$$
For the last inequality differentiate twice in $s$ and use
$s(1-s)\le1/4$ and $|1-2s|\le1$.
The weight and its required derivatives agree with zero at both seams.

On a genuine intersection of an old strict row with an original
whole intrinsic third-jet row, read $a,\beta,\beta_r,\gamma,\gamma_r$;
do not call their producer. With positive lower bounds $a_-,\gamma_-$,
$$
 T_+=\frac{b}{2\gamma_-^2a_-^2},\qquad
 T_1^+=\frac{|\beta_r|_+}{2\gamma_-^2a_-^2}
     +\frac{b|\gamma_r|_+}{\gamma_-^3a_-^2}
     +\frac{b^2}{\gamma_-^2a_-^2}.
 \tag{SP.23}
$$
This is the complete derivative of $T_0$ using $a_r=\beta a$.
Outside the compact support all metric difference fees are exactly zero.

Set
$$
 k_\Delta=(e^{d_*W}-1)|K_0|_+
                +d_*e^{d_*W}T_+W_1 .
$$
Obtain positive $q_{\delta,-},q_{\delta,+}$ from the whole
$-K_\delta$ enclosure, and use
$$
 q_\Delta=\frac{k_\Delta}{q_{0,-}+q_{\delta,-}},\quad
 R=R_0+\max(1,q_{\delta,+})\varepsilon_0+q_\Delta V_0,\quad
 L=L_0+\max(1,q_{\delta,+})\varepsilon_1+q_\Delta V_1 .
 \tag{SP.24}
$$
Here $V_0,V_1$ are the saved complete absolute $v_0,(v_0)_\phi$
bounds. One may take $U_0=R_0\ge|u_0|$ and define
$$
 \Delta_U=2U_0\varepsilon_0+\varepsilon_0^2,\quad
 \Delta_{Kv}=|K_\delta|_+(2V_0\varepsilon_0+\varepsilon_0^2)
                                      +k_\Delta V_0^2,\quad
 \Delta_S=\Delta_U+\Delta_{Kv}.
 \tag{SP.25}
$$
Then complete valid inputs to (SP.17) are
$$
 D=D_0+2b\Delta_S,\quad
 F=F_0+4b\Delta_S,\quad B_{\rm rev}=B_0+4b\Delta_S,\quad
 g=\gamma_{0,+}e^{d_*W/2}.
 \tag{SP.26}
$$
Indeed each changed local diagonal costs at most $3b\Delta_S$,
and half the changed drift derivative costs at most $b\Delta_S$.
These are actual state/metric perturbation estimates on unrestricted
angular inputs; the principal speed difference is not treated as a
bounded zero-order operator.

## 6. Reuse the complete curvature variation and add only its new delta fee

Let $k_-=q_{0,-}^2$, $K_{1,+}\ge|(K_0)_r|$ on a compact-support
intersection, and put
$$
 H_0=\frac{T_+W_1}{k_-},\qquad
 H_1=\frac{T_1^+W_1+T_+W_2}{k_-}
                  +\frac{T_+W_1K_{1,+}}{k_-^2}.
 \tag{SP.27}
$$
The new consumer must pass $d_*H_0<1$ on every such intersection.
From
$$
 q_\delta=q_0 e^{-\delta w/2}(1-\delta H)^{1/2},
 \qquad H=T_0w_r/q_0^2 ,
$$
one gets the exact derivative relation and full bound
$$
 \frac{(q_\delta)_r}{q_\delta}-\frac{(q_0)_r}{q_0}
 =-\frac{\delta w_r}{2}
          -\frac{\delta H_r}{2(1-\delta H)},\qquad
 E_q=\frac{d_*W_1}{2}+\frac{d_*H_1}{2(1-d_*H_0)} .
 \tag{SP.28}
$$
It is zero off the compact support. Only the new positive integral
$J_q=\sum |I_i|E_{q,i}$ is evaluated.

The old grouped theorem already proves
$$
 \int_0^{r_a}\max(0,-(q_0)_r/q_0)\,dr<C_-^0,
 \qquad C_-^0=4.386425547 .
 \tag{SP.29}
$$
This explicit rational upper bound is read as the stated proved theorem;
its original grouped integral and exponential are not rerun.
Thus every strict subinterval has reverse scalar cost bounded by
$C_-^0+J_q$.
For the forward cost over the same full old interval,
$$
 C_+\le C_-^0+J_q+
       \log\frac{q_{0,+}(r_a)}{q_{0,-}(0)} .
 \tag{SP.30}
$$
Here $q_\delta=q_0$ at both endpoints, since $w=w_r=0$ there.
The endpoint bounds may be the complete first and last row bounds.
The right side must be a valid nonnegative upper bound; an unresolved
or negative rounded result is not silently clipped into a proof.
This follows from $\int\max(0,\lambda)-\int\max(0,-\lambda)
=\log(q(r_a)/q(0))$. Both costs bound all shorter source insertion
intervals because their integrands are nonnegative.

The curve $q_\delta$ is continuous and piecewise absolutely continuous
through the genuine intrinsic seams and compact-support seams.
There is no artificial curvature impulse at a candidate cubic knot.
The exact continuous background and direction also introduce no
homogeneous state jump; any supplied affine impulse is still retained
as an independent input.

## 7. Chronological products, all source insertions and the waist

Refine the old strict rows by the required original intrinsic
whole-cell intervals, the compact endpoints, and the chosen cut.
Retain both one-sided rows at actual seams. For each orientation take
the chronological product of the nonnegative matrices
$\exp(|I_i|\mathcal A_i)$, in that orientation, and denote a full
entrywise upper product by $\mathcal P_\pm$.
Each factor is entrywise at least the identity. Therefore this same
product bounds all shorter ordered subinterval products and all source
insertion times. Combining it with the scalar costs gives
$$
 \mathcal U_- = e^{C_-^0+J_q}\mathcal P_-,
 \qquad
 \mathcal U_+ = e^{C_+}\mathcal P_+ .
 \tag{SP.31}
$$
These are new two-state scalar products. They are not a recomputation
or reinterpretation of the old four-state flow.

For arbitrary affine sources the complete bound is
$$
 \binom{Y(r_{\rm out})}{Z(r_{\rm out})}
 \le\mathcal U_\pm\left[
       \binom{Y(r_{\rm in})}{Z(r_{\rm in})}
       +\int\sqrt q
             \binom{\|ITf\|_2}{|\Pi Tf|}\,dr
       +\sum_\alpha\sqrt{q(r_\alpha)}
             \binom{\|ITj_\alpha\|_2}{|\Pi Tj_\alpha|}
                         \right].
 \tag{SP.32}
$$
The integrals use true $dr$, and the impulses have no artificial
length factor. The complete source injection from Hminus1 obeys
$$
 \sqrt q\,\|(ITf,\Pi Tf)\|
 \le\frac{\sqrt{17}}4\max(1,q)\|f\|_{H^{-1}\oplus H^{-1}} .
 \tag{SP.33}
$$
The mean column is part of this exact Fourier multiplier bound.
An L2 radial source may be converted to L1 only with its actual
interval length to the power $1/2$.

For the fixed cut $r_c=r_+-1/200$, use the old N.17 numbers
$P_R=C_I C_R$ and $Q_R=C_I C_R\sqrt R$ exactly as saved.
Before any strict normalizer, its complete Cauchy conclusion gives
$$
 \left\|\binom{Y(r_c)}{Z(r_c)}\right\|_{\mathbb R^2}
 \le \max(1,q_+(r_c))
       \{P_R(B_{\rm root}+B_{\rm jump})+Q_R F_{\rm ord}\}.
 \tag{SP.34}
$$
The source spaces and actual root-distance interval are exactly N.2--3.
The current genuine root-piece source is zero-extended only on its
already declared support. This sets no root or affine-jump input to zero.

At the waist the unnormalized original density and its complete mean
have the exact norm
$$
 \|(Iw(0),\Pi w(0))\|
     =\frac{n_g(0)}{\sqrt{q(0)}}\sqrt{Y(0)^2+Z(0)^2}.
 \tag{SP.35}
$$
Its source-to-waist constant is consequently bounded by
$$
 \frac{n_{g,+}(0)}{\sqrt{q_-(0)}}\,
       \|\mathcal U_-\|_{\mathbb R^2\to\mathbb R^2}\,
       \max(1,q_+(r_c))Q_R ,
 \tag{SP.36}
$$
and the root/jump constant has $P_R$ in place of $Q_R$.
The actual waist $a_{\rm phys},m$ and $q$ must be read with their true
denominator bounds; $n_g$ is not assigned the value one.

If the input is the normalized N.18 coordinate
$(\widehat y_c,z_c)$ instead, its exact entry map is
$$
 \binom YZ(r_c)
 =\frac{\sqrt{q(r_c)}}{n_g(r_c)}
   \binom{\|T_1T_2\widehat y_c\|_2}{|z_c|},
 \quad
 \|T_1T_2\|\le(1+\tau_1)(1+\tau_2).
 \tag{SP.37}
$$
The two forward normalizers occur in this order. Their cutoff leaves
the entire mean and finite head unchanged. Using (SP.37) requires a
strict lower bound for $n_g(r_c)$; the original upper bound alone
cannot supply it. Formula (SP.34) is the direct unnormalized alternative
and does not pay the inverse and forward normalizers twice.

The forward normalized cut readout has the equally explicit bound
$$
 \|(\widehat y_c,z_c)\|
 \le \frac{n_{g,+}(r_c)}{\sqrt{q_-(r_c)}}K_{\rm inv}
       \|\mathcal U_+\|\,
       \frac{\sqrt{q_+(0)}}{n_{g,-}(0)}
          \|(Iw(0),\Pi w(0))\| ,
 \tag{SP.38}
$$
in the homogeneous strict segment, with the complete ordinary-source
and jump additions from (SP.32) in the nonhomogeneous case.
All four radial factors and the positive lower bound $n_{g,-}(0)$
must be supplied. This is a Cauchy readout of prescribed complete
waist data; it is not a selection of the missing boundary data.

The current RJ conclusion is a full two-column, both-sign input map
on $P_{\{|j|\ge97\}}H^{-4/3}$ to ordinary
$L^2_rH^{-2/3}$ in the first row and the independent constant second
row. Its 21 first-row and ten mean terms, original physical measure
and actual compact source support are kept. Multiplication of its
already accepted complete pair bound by (SP.36) therefore gives one
complete strong source-to-waist contribution in these exact density
coordinates. It does not include the independent root/jump columns
or assert that this contribution is the whole strong-return norm.

## 8. Exact output type and the next return obligation

This theorem produces both genuine branches and both complete mean
coordinates at the waist, and the opposite Cauchy direction from the
waist to the same strict cut. It also gives all ordinary-source and
affine-jump insertions in those coordinates. A density row such as
$Iw_+(0)+Iw_-(0)$ has its actual Euclidean row factor $\sqrt2$.

A subsequent true ray or KAM density transformation must use its
Jacobian and its same-coordinate norm. A raw Hminus1 state has not been
promoted to raw L2, and no physical-angle composition is replaced by an
identity. The residual-sensitive moving-to-physical bridge remains
separate where required. The root mixed input/output, the complete
seven-port positive graph, actual root/jump matrices, the normalized
strong remainder and finite border likewise remain in the full return
problem. In particular these complete Cauchy bounds alone do not invert
the return or establish the high BVP.

The public scalar consumer will restore only exact old bytes, verify
the old strict/whole-jet identities and the full continuous family,
evaluate (SP.17), (SP.23)--(SP.31) and the explicit final coordinate
factors, and read the current successful source ledger. It will publish
only the actual small constants, denominator gates, source contributions,
cover counts and input/output SHA receipts. No new row arrays, native
certificates or stages will be put in Git, Releases or Actions artifacts.
