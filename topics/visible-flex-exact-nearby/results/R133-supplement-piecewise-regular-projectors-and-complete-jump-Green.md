# R133 supplement: piecewise regular projectors and the complete jump Green operator

2026-11-14, visible-exact-astra-ac0d / newton_source.

**Proved.** The continuous 193-state regular-subspace inverse criterion
extends to independently validated polynomial frames with small jumps of
their orthogonal projectors. The exact interface coupling has norm equal
to the projector gap; neither a derivative of a discontinuous projector
nor an unrecorded change of state is introduced. This permits high-order
local fundamental polynomials to retain rapid principal rotation without
paying the much larger cubic Hermite interpolation defect.

This is a criterion for the actual continuous finite head. Its numerical
rates, Gram bounds, projector gaps and full boundary errors must still
be consumed. It does not assert that the whole 193-state inverse or its
coupling to the infinite high modes has already closed.

## 1. Same physical state and complete data

Use the actual moving reflection space with 96 odd amplitudes, the even
mean and 96 even nonzero amplitudes. The physical Gram and its Euclidean
coordinate are

$$
 W=\operatorname{diag}(\tfrac12 I_{96},1,\tfrac12 I_{96}),
 \qquad z=W^{1/2}h.
 \tag{J.1}
$$

Let $A(r)$ be the complete compressed Jacobi operator in these
coordinates. Any further radial weight must include its logarithmic
derivative and all source/trace transformations, as in
[the continuous projector theorem](R133-supplement-continuous-head-Green-from-a-regular-subspace.md).
The problem is

$$
 z'=Az+f,\qquad Uz(0)=g_0,\qquad Bz(L)=g_L,
 \qquad [z]_{r_i}=j_i.
 \tag{J.2}
$$

There are 96 left and 97 right rows. At $L=9/10$ the right operator must
be the entire genuine moving cap row, including its independent mean;
the physical-to-moving change of equations and all of its output tails
are separate paid inputs. A proposed finite cut matrix is not declared
equal to this operator. The parameter column, when used, is an ordinary
source in (J.2); it is not an artificial replacement for a boundary row.

The finite partition includes every true coefficient and trial
interface needed in the computation. A projector interface can be
inserted even when $j_i=0$. Conversely a real state source $j_i$ is kept
whether or not the projector changes there.

## 2. The two exact interface equations

On each open interval take a continuously differentiable orthogonal
projector $P(r)$ of rank 96, and put $Q=I-P$. At an interface write
$P_\pm=P(r_i\pm)$ and $Q_\pm=I-P_\pm$, and suppose

$$
 \delta_i:=\|P_+-P_-\|<1.
 \tag{J.3}
$$

For $x=Pz$, $y=Qz$, the full state jump in (J.2) implies the exact
forward/backward interface rules

$$
 \begin{aligned}
 x_+&=P_+x_-+P_+Q_-y_-+P_+j_i,\\
 y_-&=Q_-y_++Q_-P_+x_+-Q_-j_i.
 \end{aligned}
 \tag{J.4}
$$

In the first line $y_-\in\operatorname{ran}Q_-$ and in the second
$x_+\in\operatorname{ran}P_+$, so the inserted projections do not
change the equations. The backward real source has the displayed minus
sign.

Conversely let the four variables lie in their stated one-sided
subspaces and satisfy (J.4). For
$d=x_++y_+-x_--y_--j_i$ these equations give $P_+d=0$ and $Q_-d=0$.
Thus $d\in\operatorname{ran}Q_+\cap\operatorname{ran}P_-$. If $d$
were nonzero, then $(P_--P_+)d=d$, contradicting (J.3). Hence $d=0$,
and (J.4) is equivalent to the entire original state jump.

The homogeneous forward interface $P_+|_{\operatorname{ran}P_-}$ and
backward interface $Q_-|_{\operatorname{ran}Q_+}$ are contractions.
The two cross-interface maps satisfy

$$
 \|P_+Q_-\|=\|Q_-P_+\|\le\delta_i.
 \tag{J.5}
$$

In equal rank the maximum sine of the principal angles gives equality
with $\delta_i$; only the displayed upper bound is needed. There is no
factor $(1-\delta_i)^{-1}$ in these forward/backward equations.

## 3. Continuous propagation with all interface feedback

On each open piece define, exactly as in the continuous theorem,

$$
 C=PAQ+PP'Q,\qquad E=QAP-QP'P.
 \tag{J.6}
$$

Then

$$
 x'=(PAP+P'P)x+Cy+Pf,\qquad
 y'=(QAQ-P'Q)y+Ex+Qf.
 \tag{J.7}
$$

The useful exact cancellation is still
$C=2P\operatorname{Sym}(A)Q-E^*$. Let $\mu,\nu,c,e$ be paid
piecewise bounds for the two logarithmic rates and $\|C\|,\|E\|$.
Keep the true signs of $\mu$ and $\nu$.

Define $\Phi_P(r,t)$ by the homogeneous forward equation on each open
piece and the homogeneous $P_+$ contraction at every crossed interface.
Define $\Phi_Q(r,t)$ backward, using the homogeneous $Q_-$
contractions. They retain the same scalar bounds

$$
 \|\Phi_P(r,t)\|\le L_P(r,t)=e^{\int_t^r\mu},\quad r\ge t,
 \qquad
 \|\Phi_Q(r,t)\|\le L_Q(r,t)=e^{\int_r^t\nu},\quad r\le t.
 \tag{J.8}
$$

One-sided arguments of these maps specify whether the endpoint
projection has been included. No artificial exponential cost is added
at an interface because its homogeneous map is a contraction.

Suppose $U|_{\operatorname{ran}P(0)}$ and
$B|_{\operatorname{ran}Q(L)}$ have full inverses $L_U,L_R$. Put
$D_0=L_UU|_{\operatorname{ran}Q(0)}$ and
$D_L=L_RB|_{\operatorname{ran}P(L)}$. The complete unknown feedback is

$$
 \begin{aligned}
 (\mathcal S y)(r)={}&-\Phi_P(r,0)D_0y(0)
 +\int_0^r\Phi_P(r,t)C(t)y(t)\,dt\\
 &+\sum_{r_i\le r}\Phi_P(r,r_i+)P_{i,+}Q_{i,-}y(r_i-),\\
 (\mathcal T x)(r)={}&-\Phi_Q(r,L)D_Lx(L)
 -\int_r^L\Phi_Q(r,t)E(t)x(t)\,dt\\
 &+\sum_{r<r_i}\Phi_Q(r,r_i-)Q_{i,-}P_{i,+}x(r_i+).
 \end{aligned}
 \tag{J.9}
$$

Both interface feedback sums have a plus sign; they come from (J.4),
not from differentiating a discontinuous $P$. The ordinary-source and
independent-jump terms are

$$
 \begin{aligned}
 x_f(r)={}&\Phi_P(r,0)L_Ug_0+
 \int_0^r\Phi_P(r,t)P(t)f(t)\,dt
 +\sum_{r_i\le r}\Phi_P(r,r_i+)P_{i,+}j_i,\\
 y_f(r)={}&\Phi_Q(r,L)L_Rg_L-
 \int_r^L\Phi_Q(r,t)Q(t)f(t)\,dt
 -\sum_{r<r_i}\Phi_Q(r,r_i-)Q_{i,-}j_i.
 \end{aligned}
 \tag{J.10}
$$

Work in the Banach spaces of bounded piecewise continuous sections,
including both one-sided traces in the supremum norm. This makes every
point evaluation in (J.9) a bounded map; no point evaluation on an
equivalence class of arbitrary $L^\infty$ functions is being used.

The following two explicit numbers bound $\mathcal S,\mathcal T$:

$$
 \begin{aligned}
 s={}&\sup_r\left\{
 L_P(r,0)\|D_0\|+\int_0^rL_P(r,t)c(t)\,dt
 +\sum_{r_i\le r}L_P(r,r_i+)\delta_i\right\},\\
 t={}&\sup_r\left\{
 L_Q(r,L)\|D_L\|+\int_r^LL_Q(r,t)e(t)\,dt
 +\sum_{r<r_i}L_Q(r,r_i-)\delta_i\right\}.
 \end{aligned}
 \tag{J.11}
$$

All endpoint and interface one-sided limits are included in these
suprema. At $r_i-$ the forward sum excludes the $i$th interface; at
$r_i+$ it includes it. The backward sum includes that interface at
$r_i-$ and excludes it at $r_i+$. Ordinary $L^2_r$ source gains are still the square roots of
the integrals of $L_P^2,L_Q^2$; genuine jump gains are the corresponding
pointwise kernels in (J.10). The mean remains a full coordinate in all
of these operations.

If $st<1$, the exact equations $x=x_f+\mathcal S y$,
$y=y_f+\mathcal T x$ have the unique solution obtained from the
Neumann inverse of $I-\mathcal S\mathcal T$. If $X_f,Y_f$ bound the
two source terms, then

$$
 \|z\|_\infty\le
 \frac{\sqrt{(X_f+sY_f)^2+(Y_f+tX_f)^2}}{1-st}.
 \tag{J.12}
$$

Equations (J.7) and the equivalence proved in Section 2 recover (J.2)
with every genuine interface and both complete boundaries. This proves
the continuous criterion. It does not infer invertibility from a
finite QR condition number.

## 4. Paying each gap from complete rectangular frames

On an open cell let $X(r)$ be any full $193\times96$ polynomial frame
and suppose its actual Gram satisfies $X^*X\ge gI$, $g>0$. It defines
the exact orthogonal projector $P=X(X^*X)^{-1}X^*$. For any finite
matrix gauge $T(r)$, the exact defect obeys

$$
 \|E(r)\|\le
 \frac{\|X'(r)-A(r)X(r)+X(r)T(r)\|}{\sqrt g}.
 \tag{J.13}
$$

At a projector join take full-rank one-sided frames $X_-,X_+$. For
any explicitly chosen $96\times96$ matrix $R_i$,

$$
 \delta_i\le
 \frac{\|X_--X_+R_i\|}{\sqrt{g_-}},
 \qquad X_-^*X_-\ge g_-I.
 \tag{J.14}
$$

Indeed $(I-P_+)X_+R_i=0$, so the right side bounds
$\|(I-P_+)P_-\|$; equal ranks identify this gap with
$\|P_+-P_-\|$. A numerically convenient $R_i$ is allowed, but every
entry and all rounding in (J.14) must be bounded. No endpoint frame is
assumed orthonormal merely because its floating QR returned one.

Thus independently rounded QR checkpoints do not have to be forced
into a cubic interpolation with a large rotational defect. Their exact
projector jumps can be paid by (J.14), and then by the complete sums in
(J.11). This is a new use of the approximation; it does not relabel any
previous Hermite-frame certificate.

## 5. Local high-order fundamental polynomials

Here is an explicit exact algebraic construction for the finite frames
in Section 4. On one cell take $t=(r-r_0)/h$ with $h\ne0$, and an exact
finite matrix polynomial $A_0(t)=\sum_{j=0}^d A_jt^j$. The full true
operator error $A-A_0$ remains separate. For a complete starting frame
$X_0$ and a chosen degree $p$, define recursively

$$
 X_{n+1}=\frac{h}{n+1}
          \sum_{j=0}^{\min(d,n)}A_jX_{n-j},
 \quad 0\le n<p,
 \qquad X(t)=\sum_{n=0}^pX_nt^n.
 \tag{J.15}
$$

Every coefficient of degree less than $p$ cancels exactly in
$h^{-1}X_t-A_0X$. The remaining complete residual is

$$
 h^{-1}X_t-A_0X
   =-\sum_{n=p}^{p+d}t^n
       \sum_{\substack{0\le j\le d\\0\le n-j\le p}}A_jX_{n-j}.
 \tag{J.16}
$$

Consequently the true residual is (J.16) minus $(A-A_0)X$. It is a
finite exactly specified polynomial plus the separately bounded true
coefficient error. All matrix entries, the even mean, and all input
columns are retained. Equations (J.13), (J.14), and the ordinary
polynomial Gram bounds then apply directly, for either sign of $h$.

For a constant $A_0=A_c$, the leading explicit bound on $|t|\le1$ is

$$
 \|h^{-1}X_t-A_cX\|
 \le\|A_c\|\,\frac{(|h|\|A_c\|)^p}{p!}\,\|X_0\|.
 \tag{J.17}
$$

Thus pure rapid constant-coefficient rotation is retained to the chosen
degree, rather than charged as a fourth-order frame-interpolation
error. This statement is an exact residual identity, not a numerical
order heuristic. For variable $A$, the genuine joint Taylor error and
all required scalar primitive tails still enter through $(A-A_0)X$.

The original infinite high response is not part of this finite-head
construction: the complete high-to-head and head-to-high operators,
their boundary tails, and the true negative return remain in the final
global Schur problem. A numerical implementation of this criterion
must state its actual closed domain and cannot transfer the current
centre's bounds to a changed parameter or background.
