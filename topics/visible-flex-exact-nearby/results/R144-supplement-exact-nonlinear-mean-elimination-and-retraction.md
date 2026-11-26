# R144 supplement: exact nonlinear mean elimination and a complete mean retraction

2026-11-26, visible-exact-astra-198c63d-20261126 / global_geometry.

**Proved.** After the exact waist-mean replacement in
[R144](R144-fourfold-holonomy-transfers-outer-mean-to-waist.md),
the full nonlinear moving mean can be recovered from a scalar linear
Volterra equation in the angular density $j=v/\langle v\rangle$.
The two remaining shape equations retain every nonzero frequency and
their full mean feedback.

For an arbitrary approximate centre there is also an exact mean
retraction which keeps $u$ and $j$, and hence the real material angle,
unchanged. The retraction pays the complete signed mean residual and
has explicit new nonmean residuals. Positivity, whole-core closeness
and exterior admission are stated as genuine gates, not conclusions
from a tiny waist residual. The forward kernel explicitly retains its
$a(R)^{-2}$ amplification.

## 0. Relation to the already proved scalar-mean reduction

The reciprocal-mean scalarization itself is not new.
[R133's full scalar-mean theorem, Sections 1--2](R133-supplement-full-scalar-mean-Green-and-residual-sensitive-nu.md)
already uses $n=a^2/m^2$ with the complete variables
$(u,\widetilde v=v-m)$ and proves
$$
 n'=2\beta\mathcal V n+2\beta Ka^2+\tau R_0,\qquad
 \mathcal V=\langle u^2\rangle+K\langle\widetilde v^2\rangle,\qquad
 \tau=-2a^2/m^3.
$$
Its [complete 7721-cell mean Green calculation](R133-supplement-actual-final-complete-mean-Green.md)
and every saved diagonal, interface and backward Green target remain
completed results and are not repeated here.

The present new ingredients are the initial value made valid by R144,
the choice of fixed density $j=v/m$, the retraction preserving the real
material angle, and its complete changed nonmean residuals. Indeed,
$\widetilde v=m(j-1)$ and $\langle j\rangle=1$ give
$$
 \mathcal V=U+Km^2(J-1),\qquad
 2\beta\mathcal V n+2\beta Ka^2
                     =2\beta U n+2\beta Ka^2J.
$$
Thus the old variance term has moved to an explicit density-dependent
forcing; it has not been dropped. Fixing $j$ during a retraction is a
different operation from fixing $\widetilde v$.

The forward signed retraction (MV.16) with the exact new waist initial
value is also different from the completed old backward Green
operator or the old mean-completed response trial. No numerical
smallness for this new retraction is supplied by those old statuses.

## 1. Variables and the complete equations

Keep the original radial metric, fixed actual parameter, fourfold
odd/even symmetry, and the full moving system
$$
 \begin{split}
 u_r&=d u_\phi+\gamma mK v_\phi-\beta u(1+S)+R_u,\\
 v_r&=d v_\phi-\gamma m u_\phi+\beta v(1-S)+R_v,
 \end{split}
$$
$$
 m=\langle v\rangle<0,\qquad
 S=u^2+Kv^2,\qquad d=-\beta I_\phi S,\qquad
 R_0=\langle R_v\rangle.
 \tag{MV.1}
$$
Here $\gamma=\sqrt E/a$, $\beta=a'/a$,
$I_\phi=\partial_\phi^{-1}P_{\ne0}$, and means are normalized on
$L=\pi/2$. The exact source convention is that of the
[complete moving-frame theorem](R133-supplement-moving-frame-with-complete-residual-and-mean.md).
In particular
$$
                    m'=\beta m(1-\langle S\rangle)+R_0.
 \tag{MV.2}
$$

Introduce
$$
 j=v/m,\qquad \langle j\rangle=1,\qquad
 h=m^{-2}>0,\qquad
 U=\langle u^2\rangle,\qquad J=\langle j^2\rangle,\qquad
 \kappa=K/h.
 \tag{MV.3}
$$
The original physical chart has $j>0$. Conversely, $h>0$ and $j>0$
reconstruct $m=-h^{-1/2}$ and $v=mj<0$.
The material lift is exactly
$$
                 \Theta(\phi)=\phi+I_\phi(j-1).
 \tag{MV.4}
$$
It depends on $j$, not separately on $m$.

Substitute (MV.3) into the first equation and differentiate $j=v/m$.
Using (MV.2) gives the complete exact system
$$
 \begin{split}
 u_r={}&d u_\phi+\gamma\kappa j_\phi
               -\beta u(1+u^2+\kappa j^2)+R_u,\\
 j_r={}&(dj-\gamma u)_\phi+\frac{R_v-jR_0}{m},\\
 h'+2\beta(1-U)h={}&2\beta KJ-2m^{-3}R_0,\\
 d={}&-\beta I_\phi(u^2+\kappa j^2).
 \end{split}
 \tag{MV.5}
$$
For example $d_\phi=-\beta(S-\langle S\rangle)$, so the density row
is a true conservation law with its full source.
The source $(R_v-jR_0)/m$ has mean zero because $\langle j\rangle=1$.
The last mean term $-2m^{-3}R_0$ has not been discarded.

## 2. A linear Volterra formula on the true zero set

When the complete mean residual is zero, define
$$
 c(r)=2\beta(r)(1-U(r)),\qquad
 G(r,s)=\exp\left(-\int_s^r c(t)\,dt\right).
 \tag{MV.6}
$$
The new R144 boundary row is $m(0)=-a_0$, hence $h(0)=a_0^{-2}$.
For given complete shape fields $u,j$ the unique mean candidate is
$$
 \boxed{\quad
 h[u,j](r)=G(r,0)a_0^{-2}
                  +2\int_0^r G(r,s)\beta(s)K(s)J(s)\,ds.
 \quad}
 \tag{MV.7}
$$
This is linear in $h$ once the shape fields have been specified.
It is not linear in the full pair $(u,j)$.

There is an exact explicit positivity gate:
$$
 a_0^{-2}
 +2\int_0^r
       \exp\left(\int_0^s c(t)\,dt\right)\beta(s)K(s)J(s)\,ds>0
                 \quad\hbox{for every }0\le r\le R.
 \tag{MV.8}
$$
Since the exponential prefactor in (MV.7) is positive, (MV.8) is
equivalent to $h[u,j]>0$. The sign changes of $K$ remain in this
formula. No positivity theorem is inferred merely from $J\ge1$.

Using $\beta=a'/a$, the full forward kernel is also exactly
$$
 \boxed{\quad
 G(r,s)=\left(\frac{a(s)}{a(r)}\right)^2
             \exp\left(2\int_s^r\beta(t)U(t)\,dt\right).
 \quad}
 \tag{MV.9}
$$
Thus a small waist error can be amplified by the small outer radius.
The factor $a(R)^{-2}$ is not a removable normalization fee.

**Theorem MV.1.** On a regularity class where all displayed equations
are defined, suppose $u$ is odd, $j$ is even and positive,
$\langle j\rangle=1$, and (MV.8) holds. Define $h$ by (MV.7),
$m=-h^{-1/2}$ and $v=mj$. Then the complete source-free moving
system with the waist mean $m(0)=-a_0$ is equivalent to the two full
shape equations
$$
 \begin{split}
 u_r&=d u_\phi+\gamma(K/h)j_\phi
                      -\beta u(1+u^2+(K/h)j^2),\\
 j_r&=(dj-\gamma u)_\phi,\qquad
 d=-\beta I_\phi(u^2+(K/h)j^2).
 \end{split}
 \tag{MV.10}
$$

**Proof.** A true solution gives (MV.5) with $R_u=R_v=R_0=0$,
and uniqueness of the scalar initial-value problem gives (MV.7).
Conversely, (MV.7) gives the complete mean equation. Multiplying the
second row of (MV.10) by $m$ and adding $m'j$ reconstructs
the second row of (MV.1) exactly. The first row is already its exact
substitution. Also $\langle v\rangle=m\langle j\rangle=m$.
The positivity gates give the original valid real chart. $\square$

The normalization $\langle j\rangle=1$ is preserved by the conservation
law when imposed initially. It is not a new physical boundary equation.
Likewise $B(0)=0$ becomes the complete row $u(0)=0$ because $v\ne0$.

All coefficients, nonlocal products and angular frequencies in
(MV.10) remain. The outer $B$ and nonmean $C$ conditions still use
$$
 B=(-\sqrt h\,u/j)\circ\Theta^{-1},\qquad
 C=(-\sqrt h/j)\circ\Theta^{-1}.
 \tag{MV.11}
$$
For exact fields and a genuine cap satisfying R144's other hypotheses,
the outer mean follows from R144. Without those hypotheses it does not.

## 3. Quantitative dependence of the full mean on the shape fields

This reduction does not turn the mean into a constant or discard its
nonlocal feedback. For two shape pairs on the same fixed metric, let
$h_i=h[u_i,j_i]$, $U_i=\langle u_i^2\rangle$,
$J_i=\langle j_i^2\rangle$, and let $G_1$ be (MV.6) for $U_1$.
The exact difference is
$$
 h_1(r)-h_0(r)
 =2\int_0^rG_1(r,s)\beta(s)
       \{(U_1-U_0)h_0+K(J_1-J_0)\}(s)\,ds.
 \tag{MV.12}
$$
To verify it, subtract the scalar equations after putting both
left sides in the coefficient $2\beta(1-U_1)$.
The initial difference is zero.

Cauchy--Schwarz gives
$$
 |U_1-U_0|
   \le(\|u_1\|_2+\|u_0\|_2)\|u_1-u_0\|_2,
$$
$$
 |J_1-J_0|
   \le(\|j_1\|_2+\|j_0\|_2)\|j_1-j_0\|_2.
 \tag{MV.13}
$$
Equations (MV.12)--(MV.13) are a full Lipschitz budget with no angular
derivative loss. They retain the actual radial kernel (MV.9).
Any bound for a reduced-system inverse must still pay this feedback.

## 4. Exact mean retraction of an approximate centre

Now let a specified approximate centre $(\bar u,\bar v)$ have its
actual residuals $(\bar R_u,\bar R_v)$ and
$\bar R_0=\langle\bar R_v\rangle$ from (MV.1).
Define
$$
 \bar m=\langle\bar v\rangle<0,\quad
 \bar j=\bar v/\bar m>0,\quad
 \bar h=\bar m^{-2},\quad
 \bar U=\langle\bar u^2\rangle,\quad
 \bar J=\langle\bar j^2\rangle .
$$
Keep $\bar u$ and $\bar j$ fixed and define
$$
 h^\flat=G(r,0)a_0^{-2}
               +2\int_0^rG(r,s)\beta(s)K(s)\bar J(s)\,ds,
 \tag{MV.14}
$$
where $G$ uses the actual $\bar U$.
If $h^\flat>0$, set
$$
 m^\flat=-(h^\flat)^{-1/2},\qquad
 u^\flat=\bar u,\qquad v^\flat=m^\flat\bar j.
 \tag{MV.15}
$$
This new centre has $m^\flat(0)=-a_0$ and **exactly zero full even mean
residual** on every smooth radial piece. Its actual angular chart is
unchanged by (MV.4). No old scientific array has been modified in this
definition.

The complete signed difference, valid without assuming that the old
centre solves any equation, is
$$
 \boxed{\quad
 h^\flat(r)-\bar h(r)
 =G(r,0)(a_0^{-2}-\bar h(0))
       +2\int_0^rG(r,s)\bar m(s)^{-3}\bar R_0(s)\,ds.
 \quad}
 \tag{MV.16}
$$
Indeed the old third row in (MV.5) has forcing
$-2\bar m^{-3}\bar R_0$; subtracting it from (MV.14) gives (MV.16).
The sign of $\bar m^{-3}$ is negative and must be retained.

For piecewise fields with actual mean jumps, (MV.16) additionally has
$$
                       -\sum_{r_i<r}G(r,r_i)[\bar h]_{r_i}.
 \tag{MV.17}
$$
This follows by telescoping the piecewise variation-of-constants
formula. The original exactly continuous repaired centre has no such
value jumps. An unrelated iterate does not inherit that fact.

In particular, the nonzero saved initial $V_0$ cannot be erased for
free. Its tiny waist mean error enters the first term of (MV.16),
and the old signed mean residual enters the second term. Both must be
estimated together if their cancellation is needed. The separate
triangle bound can be large because of (MV.9).

## 5. All new nonmean residuals are explicit

The retraction changes the full field $v$, not just an independently
dropped mean row. Put
$$
 \bar\kappa=K/\bar h,\qquad
 \kappa^\flat=K/h^\flat,\qquad
 \Delta\kappa=\kappa^\flat-\bar\kappa,
$$
$$
 L_u=-\beta I_\phi(\bar j^2)\bar u_\phi
                         +\gamma\bar j_\phi-\beta\bar u\bar j^2,
 \qquad
 T_j=(I_\phi(\bar j^2)\bar j)_\phi.
 \tag{MV.18}
$$
Then the **complete original moving residuals** of the new centre are
$$
 \boxed{\begin{split}
 R_u^\flat&=\bar R_u-\Delta\kappa\,L_u,\\
 R_v^\flat&=m^\flat\left\{
     \frac{\bar R_v-\bar j\bar R_0}{\bar m}
                                  +\beta\Delta\kappa\,T_j
                         \right\},\\
 \langle R_v^\flat\rangle&=0.
 \end{split}}
 \tag{MV.19}
$$

**Proof.** The change in $d$ is
$d^\flat-\bar d=-\beta\Delta\kappa I_\phi(\bar j^2)$.
Consequently the first shape-equation right side changes by
$\Delta\kappa L_u$. Since $\bar u$ is unchanged, its residual has the
first sign in (MV.19). The density residual
$j_r-(dj-\gamma u)_\phi$ increases by
$\beta\Delta\kappa T_j$. The old density residual is exactly
$(\bar R_v-\bar j\bar R_0)/\bar m$ by (MV.5).
The new mean residual is zero, so multiplying that new density
residual by $m^\flat$ gives the second row. Both terms inside braces
have zero mean. $\square$

The old raw mean source thus appears in (MV.16) and (MV.19);
it has not disappeared from the error budget.
For example, if $\bar h,h^\flat\ge h_->0$, then
$$
 |m^\flat-\bar m|\le
          \frac{|h^\flat-\bar h|}{2h_-^{3/2}},\qquad
 |\Delta\kappa|\le
          \frac{|K|\,|h^\flat-\bar h|}{h_-^2},
$$
$$
 \|v^\flat-\bar v\|_{A^0}
             \le|m^\flat-\bar m|\|\bar j\|_{A^0}.
 \tag{MV.20}
$$
No change of angular argument occurs in these comparisons.

For explicit complete Fourier budgets write
$J_A=\|\bar j\|_{A^0}$, $J_{A,1}=\|\bar j_\phi\|_{A^0}$,
$U_A=\|\bar u\|_{A^0}$ and $U_{A,1}=\|\bar u_\phi\|_{A^0}$.
The fourfold primitive has norm at most $1/4$, and therefore
$$
 \begin{split}
 \|L_u\|_{A^0}
 &\le |\beta|J_A^2U_{A,1}/4
                     +\gamma J_{A,1}+|\beta|U_AJ_A^2,\\
 \|T_j\|_{A^0}
 &\le J_A^3+J_A^2J_{A,1}/4.
 \end{split}
 \tag{MV.21}
$$
These apply to the complete functions, not a truncated unknown.
Together (MV.16), (MV.19)--(MV.21) give a concrete new-centre
consumer. They do not assert that its actual smallness or positivity
gate has already passed.

## 6. Boundaries, conditioning and the final task

The retraction fixes the waist mean and preserves its density chart.
It does not automatically preserve the original full outer rows,
far label, height equation or any independent design phase.
Those remain actual residuals until the complete new BVP is solved.
The physical waist amplitude is still an output in the current
fixed-parameter formulation; no fixed-amplitude row is added here.

The scalar Volterra elimination removes a mean state together with
the new mean boundary condition. It leaves the nonlinear nonmean
feedback (MV.12), the full outer graph and all interfaces. The
$a(R)^{-2}$ factor in (MV.9) is the same type of genuine conditioning
cost exposed by R144's quarter-trace mean derivative. A local
retraction at the waist is not a whole-core error certificate.

The new formulation is regular at $K=0$, since no $1/K$ occurs.
It still requires positive $h$, positive density $j$, regularity,
the actual R144 outer neighbourhood, and a genuine periodic cap.
Actual evaluation of the signed integral, full inverse, nonlinear
convergence, far installation, global embedding, reach and visible
fixed-metric motion remain to be completed.
