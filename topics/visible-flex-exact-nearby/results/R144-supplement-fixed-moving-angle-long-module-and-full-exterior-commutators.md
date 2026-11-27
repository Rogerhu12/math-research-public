# R144 FX: fixed-moving-angle long module and complete exterior commutators

2026-11-27, visible-exact-astra-fb31ed6-20261127 / geometric_closure.

**Proved; all27 saved-rational comparisons pass.** The actual complete
exterior row of
[QN](R144-supplement-actual-whole-positive-high-inverse-in-a-full-tail-neighbourhood.md)
admits an operator-valued holomorphic extension in zero-width
**function parameters in the moving angle**. It retains the original
finite long interval, both endpoint lifts, true curvature inverse,
holonomy root, two curvature-mean rows, and independent height and
Robin inputs. Its full signed Fourier Taylor kernels give all angular
commutators of the actual boundary feedback, with only one high
endpoint norm.

This pays a coordinate obligation left separate in
[PT](R144-supplement-all-angular-positive-Cauchy-graph-with-one-high-background-factor.md).
The physical-angle commutator from
[DT](R144-supplement-all-angular-exterior-DN-tame-inverse-in-real-function-spaces.md)
alone would not control an arbitrary variable-vector-field
commutator. Here the conjugated operator is instead constructed from
the pulled **complete PDE and its actual module**, using the original
[fixed-angle proof T.7--T.25](R133-supplement-full-delta-fixed-angle-regular-graph-analytic-translation.md).
No complex-angle composition is assigned to an arbitrary $L^2$
direction.

The real-axis small norms remain exactly QN/QH's completed norms.
The large complex-parameter bound below is used only for lower
angular commutators. It is not a new smallness test.

## FX1. Actual angle, independent parameters and full mean chart

At $R=25/8$ use the same nearby endpoint as QN:
$Q=(u,v)$, $m=\langle v\rangle<0$,
$\|Q-Q_*\|_{A^3,\oplus_1}\le10^{-9}$.
The actual normalized angle is

$$
 \theta(\phi)=\phi+I_\phi e(\phi),\qquad
 j=\theta_\phi=1+e=v/m,\qquad \langle e\rangle=0.
 \tag{FX.1}
$$

Extend this one angle to every long radius without radial dependence.
For any pulled function define the exact physical mean and its
complement

$$
 M_jf=\langle jf\rangle_\phi,\qquad J_jf=f-M_jf,\qquad
 D_j=j^{-1}\partial_\phi .
 \tag{FX.2}
$$

The physical mean-zero primitive is the full operator

$$
 I_jf=I_\phi\{j(f-M_jf)\}
             -M_jI_\phi\{j(f-M_jf)\}.
 \tag{FX.3}
$$

It satisfies $D_jI_jf=f-M_jf$ and $M_jI_jf=0$.
These are precisely T.7--T.9 and
[U.8--U.11](R133-supplement-exact-unknown-outer-angle-good-tangent-and-full-means.md).

Use ordinary mean-zero curvature and height parameters

$$
 z=P_{\perp,\phi}(1/v),\qquad
 y_B=P_{\perp,\phi}(f_B\circ\theta),\qquad
 g=|D_\phi|^2y_B .
 \tag{FX.4}
$$

The actual physical curvature input, pulled to $\phi$, is exactly
$J_jz=1/v-1/m$, since $M_j(1/v)=1/m$. The long curvature-mean
output is separate: it is not assumed already equal to the raw
state's $1/m$. The physical $B$ mean of the raw state is
$M_j(u/v)=\langle u\rangle/m$; it vanishes in the stated reflection
class, while the full row is retained during the construction.

For the analytic extension let $m$ be any fixed real scalar with
$5.8<|m|<8$, put $v=m(1+e)$, and allow the four functions
$(e,z,g,u)$ to vary independently on

$$
 \begin{gathered}
 \|e\|_{A^1}<\epsilon_j=2^{-18},\qquad
 \|z\|_{A^0}<R_z=5\,10^{-10},\\
 \|g\|_{A^0}<R_g=10^{-11},\qquad
 \|u\|_{A^1}<R_u=10^{-5}.
 \end{gathered}
 \tag{FX.5}
$$

Means of $e,z,g$ are zero. The full Fourier space is used before
restriction to reflection symmetry. The norm $A^s$ is the complete
weighted Fourier $\ell^1$ norm with weight $(1+|k|)^s$ on $4\mathbb Z$.
These are complex function-parameter balls, with no spatial strip.
Allowing $z$ independently of $v$ is an analytic extension used to
prove bounds; at the actual point their exact relation is (FX.4).

## FX2. The complete pulled long PDE in its original radial module

Keep the original finite interval $0\le t\le\mathcal L$ and every
intrinsic coefficient of
[the long Dirichlet theorem](R119-supplement-actual-long-radial-nonlinear-dirichlet-problem.md).
For an ordinary mean-zero $y$, the pulled physical nonmean height is
$h^\flat=J_jy$. Define

$$
 \begin{gathered}
 P=D_jh^\flat,\quad U=D_j^2h^\flat,\quad
 K_\perp=2h^\flat+h^\flat_t,\quad V=D_jK_\perp,\quad
 K=K_\perp+\kappa(t),\\
 {\cal Q}_j(y)=P_{\perp,\phi}
 {E(V-P)^2+K^2+2EKU+EU^2-qP^2\over1+K+EU},
 \qquad q=w_{\rm long}^2,\quad E=1+q .
 \end{gathered}
 \tag{FX.6}
$$

The scalar $\kappa$ is the original holonomy-one small root,
with all physical means evaluated by $M_j$. It is not set to zero.
In the exact ordinary mean-zero chart the strong equation is

$$
 [(\partial_t+2)^2+\partial_\phi^2]y
       ={\cal Q}_j(y)-{\cal V}_jy,\qquad
 {\cal V}_j=P_{\perp,\phi}
 \{(j^{-2}-1)\partial_\phi^2-j^{-3}j_\phi\partial_\phi\}.
 \tag{FX.7}
$$

The value space $\mathcal Y_A$ and direction module $\mathcal Y_2$
are exactly T.8: first take the radial supremum separately for
each Fourier coefficient, then take the $\ell^1$ or $\ell^2$ norm
of
$|k|^2\|y_k\|_\infty+|k|\|(y_k)_t\|_\infty+\|(y_k)_{tt}\|_\infty$.
The source spaces use the same order of operations.
The original constant-angle zero-Dirichlet Green has norm below32;
the two actual endpoint lifts have bounds5 and3.

The full mean equation is preserved by this chart. The physical
projection is $J_j$, and applying $P_{\perp,\phi}$ only removes
the difference between two constant representatives. At a solution,
the remaining mean PDE follows from the same holonomy derivative
identity as QN.27. Since $j_t=0$, no radial coordinate term or
new interface impulse occurs. The original mean-height integral
and both endpoint mean slopes are recovered with this same $\kappa$.

Set

$$
 r_y=2^{-24},\qquad r_f=8\,10^{-9},\qquad
 v_j=3\epsilon_j .
 \tag{FX.8}
$$

All state and holonomy estimates T.11--T.14 apply on
$\|y\|_{\mathcal Y_A}\le2r_y$. In detail,
$\|j^{-1}\|<33/32$ and
$\|j_\phi\|<\epsilon_j$ give

$$
 \|P\|<\|y\|/3,\quad \|U\|<2\|y\|,\quad
 \|K_\perp\|<\|y\|/2,\quad \|V\|<2\|y\|,
 \tag{FX.9}
$$

so the exact removable holonomy series still has
$|\kappa|\le2^{12}\|y\|^2$ and
$|\partial_\kappa\Phi_q-1|<1/4$.
The original complete formulas yield

$$
 \|{\cal Q}_j(y)\|<2^{11}\|y\|^2,\qquad
 \|{\cal R}_{C,j}(y)\|<2^{14}\|y\|^2 .
 \tag{FX.10}
$$

The second is the curvature remainder after subtracting the
constant and the complete linear $-\chi\sqrt E(K_\perp+U)$.
It includes the true mean correction. All these bounds also
hold in the original square-zero Hilbert module by its product
inequality; no product of two Hilbert directions is required.

The new coordinate fee is the actual whole expression

$$
 \|{\cal V}_j:\mathcal Y_2\to\mathcal F_2\|
 \le(1-\epsilon_j)^{-2}-1
             +{\epsilon_j\over4(1-\epsilon_j)^3}<v_j .
 \tag{FX.11}
$$

The same formula holds in the value algebra. Cauchy on a function
direction disc of radius $r_y$ gives

$$
 d_Q=2^{13}r_y=2^{-11},\qquad
 d_C=2^{16}r_y=2^{-8}
 \tag{FX.12}
$$

for the complete derivatives of the two maps in (FX.10) at
$\|y\|\le r_y$. The containing $2r_y$ ball is inside the original
$2^{-20}$ state domain.

Consequently

$$
 32(v_j+d_Q)=.0159912109375<1/32 .
 \tag{FX.13}
$$

The actual pulled Dirichlet Jacobi inverse exists on the full
$\ell^2(C_t)$ module; its right and left lifts have norms below4
and8. The nonlinear value map also exists for
$\|y_*(R)\|_{\dot A^2}<r_f$ and $\|g\|<R_g$, because

$$
 3r_f+5R_g+32v_jr_y+2^{16}r_y^2<r_y .
 \tag{FX.14}
$$

Uniform contraction constructs this value map holomorphically on
the complex function-parameter balls. On real data it is the
same complete pulled long equation.

## FX3. The true curvature inverse, full means and value graph

Use the original exact endpoint formulas T.20:

$$
 B=\chi(V-P)D^{-1/2},\qquad
 C=-{\chi\over\sqrt E}(1+K+EU)D^{-1/2},\qquad
 D=1-q(2K+K^2+EP^2).
 \tag{FX.15}
$$

Keep the original **finite-length** constant-angle curvature
operator $\mathcal L_C$ and its inverse bound9. Its diagonal
contains the exact $\coth(|k|\mathcal L)$; neither endpoint
nor the strictly positive finite-length/regular correction
is removed.

For a unit right $\dot H^2$ datum, the new state norm is below4.
Writing the difference from the original linear lift through its
same zero-Dirichlet Green, the original endpoint derivative kernel
T.19 gives the complete difference fee $16(v_j+d_Q)$.
The angular principal change contributes $v_j$, and the
nonlinear curvature derivative contributes $4d_C$. Thus

$$
 E_C=16(v_j+d_Q)+v_j+4d_C,\qquad
       9E_C<.212688447<1/4 .
 \tag{FX.16}
$$

It follows that the true curvature derivative has inverse

$$
 \|(D C_R)^{-1}:L^2_\perp\to\dot H^2_\perp\|
       \le{9\over1-9E_C}<12.
 \tag{FX.17}
$$

The same absolute module bounds hold for its Wiener version.
The complete long state from a curvature direction has norm
below48. Its physical curvature-mean functional has norm

$$
             (1+\epsilon_j)d_C(48)<1/4 .
 \tag{FX.18}
$$

For this last assertion the weighted mean of the complete linear
$K_\perp+U$ term is zero by its exact identities.
Its holonomy contribution is already in $\mathcal R_{C,j}$;
it has not been discarded.

For completeness the nonlinear curvature value inverse is also
defined on (FX.5), rather than assumed there. If the right
Dirichlet value is zero, (FX.10) and the value equation give

$$
 \|y\|\le
 {5\|g\|\over1-32v_j-2^{16}r_y}<6\|g\|.
 \tag{FX.19}
$$

At that right endpoint $P=U=0$ and
$\|K_\perp\|\le(1+\epsilon_j)\|y\|/4$.
The holonomy bound in (FX.9) then gives $\|K\|<2\|g\|$.
Here the derivative of the scalar $C(K)$ in (FX.15) has norm
$\chi\sqrt E D^{-3/2}<2/5$, using the same original
$\chi\sqrt E<1/5$. Hence its entire nonmean curvature is,
conservatively, below $4\|g\|$.
Subtract this left-only value and the exact $\mathcal L_C$
right column. By (FX.16) the remaining right derivative has
contraction factor below $1/4$, and

$$
                     9(R_z+4R_g)+r_f/4<r_f .
 \tag{FX.20}
$$

This constructs the complete curvature value graph
$y=y(e,z,g)$ with $\|y\|_{\mathcal Y_A}<r_y$, together with
its full Jacobi module. Ordinary nonmean $z$ prescribes
$P_{\perp,\phi}(C-C_{\rm ref})$; its physical nonmean
representative is $J_jz$. The weighted curvature mean and
both endpoint height means remain actual outputs.

As in T.23, a normalized independent left height direction has
state norm at most
$8+4(12)(16)(8)<2^{14}$. The norm16 here bounds the complete
endpoint curvature differential in the same original state
module. Its physical $C$-mean column is below
$(1+\epsilon_j)d_C2^{14}<128$.
The independent overall constant height is still a separate
translation datum, not a member of $g$.

## FX4. The actual unknown-tail endpoint belongs to this function ball

All numbers in this section are previously completed whole
endpoint conclusions. QN and QH give

$$
 \begin{gathered}
 U_s=1.643190\,10^{-9},\quad V_s=9.603792\,10^{-9},
 \quad \sigma_*=1/8,\quad |m|>5.84,\\
 \|Z_{\rm phys}\|_{A^0}<4\,10^{-11},\quad
 \|(Z_{\rm phys})_\theta\|_{A^0}<7\,10^{-11},\quad
 \|(Z_{\rm phys})_{\theta\theta}\|_{A^0}<1.9\,10^{-9}.
 \end{gathered}
 \tag{FX.21}
$$

$U_s,V_s$ are the original complete strip norms of the known
$u_*$ and $v_*-m_*$. Only those known fields use that strip.
The unknown endpoint adds its genuine unweighted
$A^3$ allowance $\varepsilon_R=10^{-9}$.
Using the old analytic scalar inequalities for the known
fields gives the actual finite bounds

$$
 \begin{gathered}
 e_0={V_s+\varepsilon_R\over5.84},\quad
 e_1={8V_s+\varepsilon_R\over5.84},\quad
 e_2={128V_s+\varepsilon_R\over5.84},\quad
 e_3={3072V_s+\varepsilon_R\over5.84},\\
 \|e\|_{A^1}\le{9V_s+\varepsilon_R\over5.84},\qquad
 \|u\|_{A^1}\le9U_s+\varepsilon_R .
 \end{gathered}
 \tag{FX.22}
$$

The first line bounds successive pure derivatives of $e$,
with $e_0$ bounding its value. In particular
$1-e_0<j<1+e_0$ on the actual real circle.

The following real composition estimate is sufficient, including
the coefficientwise radial-sup value algebra:

$$
                 \|f\circ\theta\|_{A^0}
                         \le1.101\|f\|_{A^1}.
 \tag{FX.23}
$$

Indeed each single physical mode obeys
$\|e^{ik\theta}\|_{H^1}^2
=1+k^2\langle j^2\rangle\le1+k^2(1+e_0)^2$.
The complete fourfold inequality $A^0\le1.1H^1$ then gives
its $A^0$ norm at most $1.101(1+|k|)$. Sum these absolute
mode bounds, taking radial suprema first when necessary.
This is a real one-derivative value estimate; it does not
claim that arbitrary composition is bounded $A^0\to A^0$.

Since $P_{\perp,\phi}$ is a contraction on $A^0$, (FX.21)--(FX.23)
give

$$
 \|z\|_{A^0}<1.101(4+7)\,10^{-11}.
 \tag{FX.24}
$$

For the independent analytic height background put $b=2^{-60}$.
The real chain rule, with the original $\sigma\ge1/16$, gives

$$
 \|g\|_{A^0}
 \le1.101b\{17(1+e_0)^2+(5/4)e_1\}.
 \tag{FX.25}
$$

This follows from
$\partial_\phi^2(f_B\circ\theta)
=j^2(f_B)_{\theta\theta}\circ\theta+
 j_\phi(f_B)_\theta\circ\theta$ and (FX.23).
It is the true pulled height normalization in (FX.4).

Normalize the four parameter algebras by

$$
 t={\|e\|_{A^1}\over\epsilon_j}
       +{\|z\|_{A^0}\over R_z}
       +{\|g\|_{A^0}\over R_g}
       +{\|u\|_{A^1}\over R_u}.
 \tag{FX.26}
$$

The completed rational combination is

$$
                         t<.247725208834<1/4 .
 \tag{FX.27}
$$

It remains to identify the actual physical long solution with
the value graph just constructed. The original physical graph
has value norm
$6\{10(4\,10^{-11}+b)+b\}$.
Its first angular derivative has value norm below
$30(7\,10^{-11})+6(16b)$: the original right lift bound3,
Dirichlet contraction, and true curvature inverse give the
complete $Z$-to-state derivative below30, and the height
column below6 at this smaller actual physical ball.
The real chain rule in the three strong-state components,
followed by (FX.23), therefore bounds its pulled ordinary
mean-zero state by

$$
 \begin{aligned}
 1.101\max\{(1+e_0)^2+e_1/4,1+e_0,1\}
 \bigl[6\{10(4\,10^{-11}+b)+b\}
            +30(7\,10^{-11})+96b\bigr]\\
                         <4.954501\,10^{-9}<r_y .
 \end{aligned}
 \tag{FX.28}
$$

In particular its two angular, mixed and second radial components
have the required coefficientwise radial-sup summability.
It solves the same pulled PDE and curvature equation, so uniqueness
identifies the two complete graphs. Finite Fourier approximation
and these same bounds justify the identity for the real finite
regularity input. The holonomy mean and mean-height recovery pass
to the limit as in QN5; no positive strip is asserted for the
unknown endpoint.

## FX5. A bounded holomorphic family for the actual raw boundary row

Freeze $j$ in a physical curvature direction. By the exact good-tangent
identities U.7--U.22, the pulled Jacobi problem constructed above is
the pullback of the actual physical-angle derivative. This statement
includes its holonomy direction and both physical curvature means.
It does not require the raw approximate centre already to satisfy
the nonlinear exterior equation.

Let $\xi$ denote an ordinary mean-zero curvature direction.
The complete pulled curvature direction has the form
$c^\flat=J_j\xi+c_0'\xi$ and $b^\flat=B'\xi$,
with the independent height and residual columns added afterwards.
By (FX.17)--(FX.18),

$$
 \|c^\flat\|_2\le(1+\epsilon_j+1/4)\|\xi\|_2,\qquad
 \|b^\flat\|_2<16(48)\|\xi\|_2 .
 \tag{FX.29}
$$

The exact raw variation, including its phase primitive, is QN.34:

$$
 h_1=vb^\flat-uvc^\flat-u_\phi I_\phi(vc^\flat),\qquad
 h_2=-v^2c^\flat-v_\phi I_\phi(vc^\flat),\qquad
 \langle h_2\rangle=-m^2M_jc^\flat .
 \tag{FX.30}
$$

In particular the ordinary nonmean chart from $\xi$ to
$y_2=P_{\perp,\phi}h_2$ has leading part $-m^2\xi$.
Its full error is bounded by

$$
 E_{\rm chart}
 =64\{2\epsilon_j+\epsilon_j^2+
                \epsilon_j(1+\epsilon_j)/4\}
                        (1+\epsilon_j+1/4).
 \tag{FX.31}
$$

Here the first terms are $v^2-m^2$ and the final one is the
entire ordered primitive. The weighted mean and the attached
$c_0'$ are included in the last factor. Consequently

$$
 \|(\xi\mapsto y_2)^{-1}\|
       \le(5.8^2-E_{\rm chart})^{-1}
                    <.029727122833<.03 .
 \tag{FX.32}
$$

Thus the actual raw equation can again be written, on the fixed
$\phi$ circle, in exactly QN's form

$$
 P_{\perp,\phi}(-J_\phi h_1-p_{*,Q}h_2)
       ={\cal E}y_2+{\cal B}_gG+
                         {\cal B}_BR_B+{\cal B}_Cr_C .
 \tag{FX.33}
$$

Here $G=|D_\phi|^2P_{\perp,\phi}(\dot f_B\circ\theta)$
is the independent good physical height direction in its true
pulled chart, $R_B=P_{\perp,\phi}(r_B\circ\theta)$ is the
independent physical nonmean Robin residual, and $r_C$ is the
independent physical curvature-mean residual. The scalar moving
mean and physical $B$-mean compatibility equations are kept
as additional rows of this same family. A pure overall height
translation is retained separately.

All operators in (FX.33) are holomorphic on the function-parameter
ball (FX.5). The following complete coarse bounds suffice there:

$$
 \begin{array}{c|c}
 \text{raw exterior column}&L^2\text{ norm upper}\\ \hline
 {\cal E}&256\\
 {\cal B}_g&2^{24}\\
 {\cal B}_B&64\\
 {\cal B}_C&2^{15}.
 \end{array}
 \tag{FX.34}
$$

For the first row, (FX.29)--(FX.32), $|p_{*,Q}|<1/5$,
$\|v\|<9$, and $\|u\|,\|u_\phi\|<10^{-5}$ give the
complete expression below184.521.
For the height column, the state bound $2^{14}$ from FX3 gives
$B$ direction below $2^{18}$ and $C$-mean direction below128.
Its complete raw even affine shift has norm below $2^{14}$.
Solve this shift with (FX.32), then use (FX.30); the full row
is below $2^{24}$. This explicitly includes the shift of the
onto chart, rather than only the direct height term.
For the physical-mean residual the corresponding raw even shift
is at most
$[\,\|v\|^2+\|v_\phi\|\|v\|/4\,]|r_C|$; the same calculation
gives $2^{15}$.

For the Robin column the exact conjugated Hilbert kernel is used,
not a naked complex composition. The regularized periodic kernel
T.6, with $\|j-1\|,\|j_\phi\|<\epsilon_j$, has norm below4.
Its weighted nonmean input $J_jR_B$ costs $1+\epsilon_j$,
so $b^\flat$ costs less than5 and $h_1$ less than45.
The original real and complex pole cancellation is valid on this
zero-width coefficient ball, because it needs only those two
uniform derivative bounds. The full finite-period kernel and
its exact normalization are retained.

The attached mean and the other physical-mean row have the same
bounded-module construction. For example the homogeneous moving
mean is bounded by $64(1/4)(.03)\|y_2\|$, and the independent
height and physical-mean columns include their actual affine
chart shifts just computed. A common bound

$$
                              {\mathcal M}=2^{32}
 \tag{FX.35}
$$

dominates the sum of the complete row/column norms, including
these scalar outputs. Nothing in (FX.34)--(FX.35) replaces the
far smaller **actual real-axis** bounds QN.36--QN.40 and
QH.19--QH.24.

The family (FX.33) is the same pullback of the physical tangent
row used by QN. If instead one differentiates the value of a
nonzero nonlinear residual already pulled to $\phi$, U.19 and
U.22 retain its additional angular transport term. This theorem
does not delete that off-shell term or identify the two derivative
conventions.

## FX6. Full signed kernels and angular boundary commutators

For the four parameters put

$$
 a_\ell=(1+|\ell|)
        \left({|e_\ell|\over\epsilon_j}
                      +{|u_\ell|\over R_u}\right)
                   +{|z_\ell|\over R_z}+{|g_\ell|\over R_g},
 \qquad
 \Gamma_r=\sum_\ell|\ell|^r a_\ell \quad(r\ge1).
 \tag{FX.36}
$$

Then $\sum a_\ell=t<1/4$. The complete second moment at the
actual endpoint satisfies

$$
                             \Gamma_2<74.053652814<100 .
 \tag{FX.37}
$$

Here is its explicit qualification. The $e$ and $u$ contributions
are bounded by $(e_2+e_3)/\epsilon_j$ and
$(3200U_s+2\varepsilon_R)/R_u$.
The actual reciprocal identity gives

$$
 \|z_{\phi\phi}\|_{A^0}
 \le{1\over5.84}
       \left\{{e_2\over(1-e_0)^2}
                    +{2e_1^2\over(1-e_0)^3}\right\}.
 \tag{FX.38}
$$

For the height moment apply the full fourth chain rule to
$f_B\circ\theta$ and then (FX.23). Its upper bound is

$$
 \begin{aligned}
 \|g_{\phi\phi}\|_{A^0}\le1.101b\{&
 25088(1+e_0)^4+3168(1+e_0)^2e_1+51e_1^2\\
 &+68(1+e_0)e_2+(5/4)e_3\}.
 \end{aligned}
 \tag{FX.39}
$$

The constants use the already permitted analytic background
height derivatives: $16b,512b,24576b$ after its two physical
derivatives. No spatial regularity is assigned to a height
direction by this calculation.

Let $A$ denote any raw operator column or scalar row of the
family (FX.33). On the normalized parameter unit ball its
symmetric Taylor coefficients satisfy, exactly as in DT.10--DT.13,

$$
 \|A_p\|<3^p\mathcal M,\qquad p\ge1 .
 \tag{FX.40}
$$

The factorial is included in $A_p$. The complete pulled equations,
holonomy root, curvature inverse, Hilbert kernel and onto chart
commute with simultaneous real translations of all four
parameters. Thus an input frequency $k$ and background lags
$\ell_1,\ldots,\ell_p$ have exact output
$k+\sum_i\ell_i$; for a scalar output this sum is zero.
Their full kernel is bounded by
$3^p\mathcal M\,a_{\ell_1}\cdots a_{\ell_p}$.
This follows by testing the genuine bounded module on single
Fourier directions, not from an unsupported claim about all
bounded $L^2$ operators.

Since $3t<3/4$, every background Taylor order is summable.
For $r\ge1$ and $S=\sum_i|\ell_i|$ the full moments satisfy

$$
 \sum S^r\prod_i a_{\ell_i}
       \le p^r t^{p-1}\Gamma_r,\qquad
 \sum_{p\ge1}p^r x^{p-1}\le{r!\over(1-x)^{r+1}} .
 \tag{FX.41}
$$

These are the convex power inequality and the exact factorial
series majorant. They retain every signed mode and all scalar
rows. Combined with
$|(k+L)^n-k^n|\le2^n(|L||k|^{n-1}+|L|^n)$,
they already prove all raw-row commutators with one moment
$\Gamma_n$.

For use at the **original positive Riccati boundary**, set

$$
 {\cal A}
  =-P_H|D|^{1/6}W^{-1/2}{\cal E}
            |D|^{-1/6}W^{-1/2}P_H .
 \tag{FX.42}
$$

This is the exact base-frame self-feedback in QN.38, before
its boundary Neumann solve. The same actual $W_N(R)>1/8$
is kept. Every kernel is enlarged by at most

$$
 8\left({|k+L|\over|k|}\right)^{1/6}
               \le8(1+|L|).
 \tag{FX.43}
$$

The projections in (FX.42) impose the true high input and
output; the intermediate background and primitive frequencies
are unrestricted. The outside Fourier weights commute with
every angular derivative.

Using (FX.37), (FX.41), and $x=3/4$ in the full commutator sum
therefore proves the explicit, actual estimate

$$
 \boxed{\displaystyle
 \|[\partial_\phi^n,{\cal A}]Z\|_2
 \le2^{n+52}\|\partial_\phi^{n-1}Z\|_2
    +2^{3n+42}(n+1)!\,\Gamma_{n+1}\|Z\|_2,\quad n\ge1 .}
 \tag{FX.44}
$$

Indeed before the last enlargement the two constants are
$96\,2^n\mathcal M(100)/(1-x)^3$ and
$48\,2^n\mathcal M(n+1)!/(1-x)^{n+2}$.
The inequalities $614400<2^{20}$ and $768<2^{10}$ give
(FX.44). Only the first term uses the fixed low moment100;
the high moment occurs once.

The same proof applies to the complete affine columns normalized
from $H^{1/6}_\phi$ to the boundary frame, and to the attached
scalar mean rows. A scalar input is assigned its true zero
frequency, with no $|D|^{-1/6}$ at zero. Transpose and conjugate
the complete kernels for adjoint rows; their means remain.
This gives their genuine negative-space extensions, rather
than suppressing a scalar output.

## FX7. The higher moment is one actual raw endpoint norm

The moments in (FX.44) are not new independent unknown long-state
inputs. They are bounded by the actual raw endpoint and the already
specified analytic **height background**.
Write

$$
 B_s^R=1+\|Q(R)\|_{A^s,\oplus_1}.
 \tag{FX.45}
$$

For integer $r\ge1$, the exact identities $e=v/m-1$ and
$z=m^{-1}P_{\perp,\phi}(1+e)^{-1}$ give

$$
 \|\partial_\phi^re\|_{A^1}
       \le B_{r+1}^R/5.84,\qquad
 \|\partial_\phi^rz\|_{A^0}
       \le{r!\over5.84^2(1-\epsilon_j)^{r+1}}B_r^R .
 \tag{FX.46}
$$

For the second formula expand the actual reciprocal in powers
of $e$. For its $p$th power the full moment is at most
$p^r\|e\|_{A^0}^{p-1}\|\partial_\phi^re\|_{A^0}$.
Sum with (FX.41). This includes the original physical mean
through $m$; angular differentiation does not vary that scalar.

The known class
$\|f_B\|_{\dot A^2_\sigma}\le b$, $\sigma\ge1/16$,
also gives the convenient complete bound

$$
 \|\partial_\phi^r g\|_{A^0}
 \le C_r^{\rm ht}b\{1+\|e\|_{A^{r+1}}\},\qquad
 C_r^{\rm ht}=2^{12r+24}((r+2)!)^2 .
 \tag{FX.47}
$$

Here only the specified background $f_B$ is analytic. To prove
the estimate, apply the full $(r+2)$th chain rule to
$f_B(\phi+I_\phi e)$. Its known analytic derivatives may be
composed by their absolutely convergent series because
$\|I_\phi e\|_{A^0}\le\epsilon_j/4$ and the remaining radius
exceeds $1/32$. A derivative of order $p\ge2$ is bounded by
$b(p-2)!32^{p-2}$; the first derivative is bounded by $b/4$.
The other factors are $j$ or derivatives of $e$ whose total
derivative order is at most $r+1$. Moment interpolation of
those factors places at most one factor in $A^{r+1}$, with
all other factors in the fixed low ball. The full chain-rule
coefficient sum is bounded by $3^{r+2}(r+2)!$; the remaining
powers and the harmless $j$ factors fit inside the explicit
$C_r^{\rm ht}$. Thus the high norm occurs once. This argument
never composes a nonanalytic direction at a complex angle.

Combining (FX.36), (FX.46), (FX.47) and the immediate
$u$ bound gives

$$
 \begin{gathered}
 \Gamma_r\le D_rB_{r+1}^R,\\
 D_r={1\over5.84\epsilon_j}+{1\over R_u}
     +{r!\over5.84^2R_z(1-\epsilon_j)^{r+1}}
     +{2C_r^{\rm ht}b\over R_g}.
 \end{gathered}
 \tag{FX.48}
$$

In particular (FX.44) needs only a single endpoint $A^{n+2}$
factor. Its low constants continue to use the actual
$\Gamma_2<100$, already supplied by the original endpoint
$A^3$ domain, rather than demanding a small high norm.

The same Taylor argument applies to the value graph
$y(e,z,g)$ itself, with uniform bound $r_y$. It gives, for
$r\ge1$,

$$
 \|\partial_\phi^ry\|_{\mathcal Y_A}
       \le {3r_y\,r!\over(1-3/4)^{r+1}}\,\Gamma_r .
 \tag{FX.49}
$$

Thus the actual pulled long background acquires its full higher
regularity from the same one-high input estimate. No higher
norm of the long solution was assumed to prove the operator
family or its current qualification.

## FX8. The actual boundary solve keeps its small highest coefficient

Let $s_R,t_R$ be the two original base Riccati coordinates at
the true outer endpoint, and put

$$
 b_R=-P_H|D|^{1/6}W^{-1/2}
       \{ {\cal E}y_L+
                  {\cal B}_gG+{\cal B}_BR_B+{\cal B}_Cr_C\},
 \tag{FX.50}
$$

where $y_L=P_LP_{\perp,\phi}h_2(R)$ is the true supplied low
endpoint value. It is not a trace manufactured from an interior
$L^2_r$ head. The exact high boundary equation is

$$
 t_R={\cal A}(s_R+t_R)+b_R .
 \tag{FX.51}
$$

QN's actual whole high bound gives

$$
 \|(1-{\cal A})^{-1}\|<1.003,\qquad
 \|{\cal R}\|<.0025,\qquad
 {\cal R}=(1-{\cal A})^{-1}{\cal A}.
 \tag{FX.52}
$$

These are the already proved real-axis bounds, not inferences
from the coarse complex bound (FX.35). Differentiating (FX.51)
as an exact spatial identity now gives every integer order:

$$
 \begin{aligned}
 \partial_\phi^nt_R={}&{\cal R}\partial_\phi^ns_R\\
 &+(1-{\cal A})^{-1}
 \{[\partial_\phi^n,{\cal A}](s_R+t_R)
                                  +\partial_\phi^nb_R\}.
 \end{aligned}
 \tag{FX.53}
$$

In particular the coefficient of the highest stable datum
remains below $.0025$ at every order. The remaining terms
have the actual lower-order and single-high bounds (FX.44),
(FX.48). This is the needed genuine boundary increment for
the differentiated positive equation; it is not a formal
new smallness hypothesis.

For a fully explicit source convention, normalize the four
inputs of (FX.50) as the Hilbert direct sum

$$
 {\mathfrak d}=
  (\langle D\rangle^{1/6}y_L,\,
   \langle D\rangle^{1/6}G,\,
   \langle D\rangle^{1/6}R_B,\,
   r_C).
 \tag{FX.54}
$$

Use the component-sum norm if preferred; it dominates the
Euclidean sum and costs no hidden dimension factor in
(FX.35). The high normalization of each complete source
column has kernel factor at most $8(1+|L|)$, just as in
(FX.43). Since $t<1/4$ and $\Gamma_1\le\Gamma_2<100$,
its full low norm is below
$8\mathcal M\{4+48(100)\}<2^{48}$.
For $n\ge1$ the complete bound is therefore

$$
 \begin{aligned}
 \|\partial_\phi^nb_R\|_2\le{}&
 2^{48}\|\partial_\phi^n{\mathfrak d}\|
 +2^{n+52}\|\partial_\phi^{n-1}{\mathfrak d}\|\\
 &+2^{3n+42}(n+1)!\Gamma_{n+1}\|{\mathfrak d}\|.
 \end{aligned}
 \tag{FX.55}
$$

Angular derivatives of the scalar input are zero; its
spatially varying output column is still charged by the
last term. The attached moving-mean equation has the
same full-kernel estimate, with its actual scalar output.
The physical $B$-mean row, which vanishes only on the
appropriate reflection directions, is retained in the same
way.

### Physical source units

(FX.54) specifies the exact fixed-$\phi$ inputs. No physical
height or Robin input is silently assigned these norms.
One convenient fully paid integer conversion for higher
orders is as follows. For a real degree-one $\theta$ in the
actual low domain and integer $k\ge2$, a sufficient tame
bound is

$$
 \|f\circ\theta\|_{H^k_\phi}
 \le K_k\{\|f\|_{H^k_\theta}
                  +\|e\|_{A^{k-1}}\|f\|_{H^2_\theta}\},
 \qquad K_k=2^{6k+8}((k+1)!)^2 .
 \tag{FX.56}
$$

For $k=0,1$ the ordinary real change of measure and chain
rule give the sufficient factor2.
For (FX.56), apply the complete integer chain rule.
The leading term uses only $j^k$ and the real $L^2$
change of measure. In a lower term with $p$ derivatives
on $f$ and $q\ge1$ differentiated $e$ factors, their total
derivative order is $k-p$. Interpolate the $e$ derivatives
between $A^1$ and $A^{k-1}$, and the $f$ derivative between
$H^2$ and $H^k$. The sum of the two high exponents is at
most one, since it is at most
$(k-p-q+p-2)/(k-2)\le1$ for $p\ge2$; the case $p=1$
is immediate. Weighted Young then gives one high $f$
or one high $e$, never their product. The known low
$A^1$ bound, the chain-rule coefficient sum, and the
Bessel conversion are all smaller than the displayed
$K_k$. The case $k=2$ follows directly without dividing
by $k-2$.

For example, writing $g_{\rm phys}=|D_\theta|^2\dot f_B$,
the exact height input in (FX.33) obeys for $n\ge1$

$$
 \begin{aligned}
 \|G\|_{H^{n+1}_\phi}
 &\le2K_{n+3}
   \{\|g_{\rm phys}\|_{H^{n+1}_\theta}
              +\|e\|_{A^{n+2}}\|g_{\rm phys}\|_{L^2_\theta}\},\\
 \|R_B\|_{H^{n+1}_\phi}
 &\le K_{n+1}
   \{\|r_B\|_{H^{n+1}_\theta}
              +\|e\|_{A^n}\|r_B\|_{H^2_\theta}\}.
 \end{aligned}
 \tag{FX.57}
$$

The first uses the exact two height derivatives and
$\||D_\theta|^{-2}:H^s_\perp\to H^{s+2}_\perp\|
\le17/16<2$. These stronger integer source norms explicitly
dominate the fractional $H^{n+1/6}$ requirement in (FX.54);
they are a convenient finite source buffer, not a relabeling
of that fractional norm. At the original low orders QN/QH
retain their sharper already paid physical source units.
The independent constant height and both physical means
are not absorbed into a nonmean height norm.
In the last term of (FX.55), use only the low-order real
source conversion, whose coefficients are controlled by the
original endpoint $A^3$ ball. Apply (FX.57) only to the
higher data terms. Thus attaching physical units does not
multiply two high background norms.

The
[companion rational calculation](../scripts/fourfold_codazzi_fixed_angle_long_module_saved_bounds.py)
evaluates only27 positive combinations of the completed
scalar bounds and the explicit new module inequalities.
No coefficient arrays, long solution, old Green integration,
native reference sweep or failed scientific target is repeated.
The original low193 reference, actual principal weights,
root97 and outer96 observations remain unchanged.
