# R144 PT: all-angular positive two-end graph with one high background factor

2026-11-27, visible-exact-astra-fb31ed6-20261127 / geometric_closure.

**Proved; all18 saved-rational comparisons pass.** On the same real
full-tail background domain as
[QN](R144-supplement-actual-whole-positive-high-inverse-in-a-full-tail-neighbourhood.md),
the actual whole positive high equation has an inverse at every
integer angular order when its stable root input and its unstable
outer input are prescribed independently. The background is small
only in the original low $A^3$ norm. Its higher norm occurs once,
linearly; it is neither required small nor put in an exponential.

The proof uses the already completed order0 and order1 inverses.
A higher-frequency split controls the auxiliary differentiated
equation by its actual principal damping. The intervening modes
are bounded by the order1 solution; no new finite inverse, larger
retained head, or replacement of the original193 reference is made.

The true outer unstable input remains an independent port in this
theorem. The complete physical exterior feedback is already closed
in orders0 and1 by QN and
[QH](R144-supplement-real-H2-exterior-DN-and-one-angular-positive-high-inverse.md).
The all-order moving-angle commutator of that exterior feedback is
a separate interface. In particular the physical translation
commutator in
[DT](R144-supplement-all-angular-exterior-DN-tame-inverse-in-real-function-spaces.md)
is not silently identified with a variable-vector-field commutator.

## PT1. The same state, actual equation and ports

Let $I=[a,R]$, where $a$ is the actual positive root and $R=25/8$.
Use precisely QN.2--QN.4:

$$
 Q=Q_*+q,\qquad
 \sup_I\|q\|_{A^3,\oplus_1}\le10^{-6},\qquad
 \|q(R)\|_{A^3,\oplus_1}\le10^{-9}.
 \tag{PT.1}
$$

The compact centre on $I$ is independent of
$|\delta|\le10^{-10}$; the intrinsic metric is the original selected
metric. Unknown $q$ can have infinitely many modes. All original
radial interfaces, both actual endpoint locations, and one-sided
values are retained. No radial derivative of $q$ is assumed.

Write $P_H=P_{\{|k|\ge388\}}$ on physical frequencies
$k\in4\mathbb Z$. The prescribed full finite head $h_L$ includes its
moving mean. The high equation is

$$
 (h_H)_r=P_HA_QP_Hh_H+f_H,\qquad
 [h_H]_i=P_Hj_i,\qquad
 f_H=P_Hf+P_HA_Qh_L .
 \tag{PT.2}
$$

Here $A_Q$ is the complete physical differential
[NT.5](R144-supplement-strict-angular-tame-Cauchy-flow-with-one-high-background-factor.md):

$$
 \begin{gathered}
 A_Qh=(dI_2+\gamma mJ)h_\phi+L_0h
       -2\beta Q_\phi I(Q^tD_Kh)
       +\gamma\langle h_2\rangle JQ_\phi,\\
 d=-\beta I(u^2+Kv^2),\quad m=\langle v\rangle,\quad
 D_K=\operatorname{diag}(1,K),\quad
 J=\begin{pmatrix}0&K\\-1&0\end{pmatrix},\qquad
 I=\partial_\phi^{-1}P_{\ne0}.
 \end{gathered}
 \tag{PT.3}
$$

Every primitive retains all signed intermediate modes except its
exact zero mode. The mean-input rank is zero in $P_HA_QP_H$ because
the input is high. It remains, with its full actual coefficient,
in $P_HA_Qh_L$.

Use the actual QN reference, without changing its terminal value:

$$
 h_k=S_{\operatorname{sgn}k}^{-1}F_{|k|}Z_k,\qquad
 F_N=N^{-1/6}W_N^{-1/2}
       \begin{pmatrix}p_N&-g_N\\1&1\end{pmatrix}.
 \tag{PT.4}
$$

Thus $g_N(a)=N^{-1/3}$ and $p_N(R)$ is the actual terminal scalar.
Prescribe $Z_s(a)=s$ and $Z_u(R)=t$ independently. The matrices
$S_{\operatorname{sgn}k}$ are the original unitary signed changes.

For integer $n\ge0$ define

$$
 \begin{aligned}
 V_n&=\sup_{r\in I}\|\partial_\phi^nZ(r)\|_{\ell^2},\\
 {\cal D}_n&=\|s\|_{H^n}+\|t\|_{H^n}
       +18\|f_H\|_{L^2_rH^{n+1/3}_\phi}
       +12\sum_i\|P_Hj_i\|_{H^{n+1/3}_\phi}.
 \end{aligned}
 \tag{PT.5}
$$

Sobolev norms use the original Bessel weights, normalized circle
measure, and Euclidean pair norm. Ordinary sources use the actual
radial measure. Impulses have no radial-length multiplier. A
coefficient seam is not an extra state impulse. The displayed head
source is an interior input; an actual low endpoint trace, when
needed by a physical boundary equation, is independent data.

## PT2. A whole-positive damping ratio from existing intrinsic positivity

Put $a_Q=-\gamma m>0$. The following inequality is valid on
the **entire** positive interval:

$$
                         {|\beta|\over a_Q}<1 .
 \tag{PT.6}
$$

Here is its precise already completed intrinsic input. On the root
collar, P.7 in
[the actual root Riccati theorem](R133-supplement-current-moving-positive-root-Riccati-and-full-head.md)
proves the true rotational gap
$E-(a_{\rm phys}')^2>0$, hence $|\beta|<\gamma$.
On the remaining positive body, the complete certificate in
[the actual whole-positive theorem](R133-supplement-actual-whole-positive-N97-inverse.md)
contains the positivity of the original intrinsic quantity
$R_{\rm rot}$. In its
[producer](../scripts/fourfold_codazzi_current_positive_complete_coefficients.py),
the function
$\mathrm{intersect\_intrinsic\_K}$ checks
$a_{\rm phys},\overline E,R_{\rm rot},K>0$ for every original body
row; $\mathrm{checked\_cap}$ retains those inequalities on all1334
cap rows. The exact formulas in
[the intrinsic producer](../scripts/fourfold_codazzi_rotational_cap_jacobi.py),
$\mathrm{body\_values}$ and its graft continuation, are

$$
 \gamma^2=\overline E=\beta^2+a_{\rm phys}^2R_{\rm rot},
 \qquad R_{\rm rot}>0 .
 \tag{PT.7}
$$

They prove $|\beta|<\gamma$ on the full covered body, not just a
sample or the negative interval. The compact metric perturbation
vanishes throughout this positive region. Finally QN.5 gives

$$
 |m|>1.068-2\,10^{-7}-10^{-6}>1,
 \tag{PT.8}
$$

which proves (PT.6). No negative-interval lower bound for $\gamma$
is imported into the positive body.

In the body the actual QN reference satisfies
$W_N>1/46$ and $p_N,g_N<2$. The floor follows directly from the
old $W_N>1/45$ and QN's relative factor $1-\tau$.
In the collar its original comparison gives
$W_N>\tfrac12N^{-1/3}$ and $a_Q>\tfrac12$. Therefore the actual
branch damping $\lambda_N=a_QNW_N/2$ obeys

$$
 \begin{array}{c|cc}
 &\lambda_N&|\beta|/\lambda_N\\ \hline
 \text{body}&>a_QN/92&<92/N\\
 \text{collar}&>N^{2/3}/8&<4/N^{2/3}.
 \end{array}
 \tag{PT.9}
$$

The last collar ratio uses (PT.6) before the lower bound for $a_Q$.
For every $N\ge M$ with $M^{1/3}\ge23$, both ratios are at most

$$
                         r(M)={4\over M^{2/3}}.
 \tag{PT.10}
$$

## PT3. Complete low-norm energy of the auxiliary equation

For this proof use the weaker signed frame weight
$w(\ell)=(1+|\ell|/388)^{2/3}$. QN.9 and its exact structured
rank-one calculation give the same local bound
$2(A+E+181B+4C)$ in the body; in the collar replace181 by1.
Scalar multiplication costs at most4 times its $A_w$ norm.
For the drift, use the base frame rather than its order1
conjugation: its logarithmic frequency derivative is at most
$5/3$, and I.7--I.12 of
[the all-signed-frequency proof](R133-supplement-all-frequency-frame-and-infinite-tail-neighbourhood.md)
give the full exponent $2/3$ and drift constant $17/2$.
That argument uses the Riccati logarithmic derivative bounds,
which hold globally here; the changed body ratio $K/W$ affects
only the structured reaction constant.
The complete drift remainder, after retaining
$P_H(d\partial_\phi+d_\phi/2)P_H$ as an exact skew operator in
each branch, is bounded by $(35/2)\|d_\phi\|_{A_w}$.

The following convenient low bounds hold uniformly on (PT.1):

$$
 \|Q\|_{A_w}<Q_{0w}=12.815,\quad
 \|Q_\phi\|_{A_w}<Q_{1w}=10.877,\quad
 \|Q_{\phi\phi}\|_{A_w}<Q_{2w}=1392.129,\quad
 \|Q\|_{A^0}<Q_0=6.408.
 \tag{PT.11}
$$

Only the known centre has degree32. Its saved pair bounds are
$6.407$ and $5.438$ at angular orders0 and1. The centre weight
costs at most2, and its second derivative costs128 times its first.
For the unknown all required orders are at most $2+2/3<3$, so
its contribution is at most $10^{-6}$. Thus no finite support has
been assigned to the unknown.

Differentiating $n$ times leaves the highest derivative operator
$A_Q+n d_\phi I_2$. Its complete zeroth-order energy in the
base frame, including drift, reaction and the ordered primitive,
is at most

$$
 |\beta|C_b(n),\qquad
 C_b(n)=C_b+nD_b,\quad
 C_b=4+472Q_{0w}^2+190Q_{0w}Q_{1w},\quad
 D_b=16Q_{0w}^2.
 \tag{PT.12}
$$

Indeed the constant reaction contributes4; the quadratic
reaction contributes at most402$Q_{0w}^2$; the drift remainder
contributes70$Q_{0w}^2$. For the primitive, the structured four
entries have coefficients $1,181,4,K$, with $K<4$, after the
exact factor $2\cdot2/4$; their sum is at most190. The extra
$n d_\phi$ costs $4nK|\beta|Q_{0w}^2$.

The completed collar base energy is $144+92\,10^{-6}<144.001$.
Its intrinsic $|\beta|<.211$ gives the sharper auxiliary bound

$$
                         E_c(n)=144.001+139n,
 \qquad4(.211)Q_{0w}^2<139.
 \tag{PT.13}
$$

The saved-rational evaluation gives
$C_b<104001.697651$ and $D_b<2627.587601$.
These constants depend only on the fixed low domain.

Choose, for every integer $n\ge1$, the physical cutoff

$$
                        M_n=[560(n+1)]^3 .
 \tag{PT.14}
$$

It is a multiple of4. The three exact base comparisons

$$
 1472(C_b+D_b)<560^3,\qquad
 128(144.001+139)<560^2,\qquad23^3<560^3
 \tag{PT.15}
$$

imply, for all $n\ge1$,

$$
 {92C_b(n)\over M_n}<{1\over16},\qquad
 {8E_c(n)\over M_n^{2/3}}<{1\over16}.
 \tag{PT.16}
$$

For example use $C_b(n)\le(n+1)(C_b+D_b)$ and
$E_c(n)\le(n+1)(144.001+139)$.
Projecting the true skew transport to $|k|\ge M_n$ preserves its
skew identity. The two branch Volterra gains are therefore at
most $\sqrt2/16<1/8$, so the complete auxiliary tail inverse has
gain below2. A forcing bounded pointwise by $|\beta|B$ has tail
response at most

$$
                              4r_nB,\qquad
                  r_n={4\over M_n^{2/3}} .
 \tag{PT.17}
$$

For each branch, integrate its actual damping kernel and use
$|\beta|/\lambda\le r_n$; combining the two branch norms costs
at most2 and the inverse costs less than2. This argument also
works across the original collar/body join. The frame and its
actual Riccati equations are the same on both sides.

## PT4. The full ordered commutator has only one high background factor

Let $B_s=\sup_I\|Q\|_{A^s,\oplus_1}$. Assume $B_{n+5/3}<\infty$
at the requested order, without any smallness requirement.
The exact differentiated physical remainder is NT.8 applied to
$h_H$. Its last mean-input term is zero for this high input.
The supplied head source in (PT.2) retains that term separately.
Since angular differentiation commutes with $P_H$ and the radial
Fourier frame, the complete projected remainder satisfies

$$
 \begin{aligned}
 \|F^{-1}S P_H{\cal R}_n(Q,h_H)\|_{\ell^2}
 \le|\beta|\left\{
       L_n\|\partial_\phi^{n-1}Z\|_{\ell^2}
       +H_nB_{n+5/3}\|Z\|_{\ell^2}\right\},\\
 L_n=2^{n+1}418Q_{0w}Q_{1w}
          +3^n190(Q_{0w}Q_{2w}+Q_{1w}^2),\\
 H_n=2^{2n+1}418Q_0+4\,6^n190Q_0.
 \end{aligned}
 \tag{PT.18}
$$

Here are the complete frequency estimates, including the primitive.
For a coefficient lag $\ell$, an input frequency $k$, and
$1\le a\le n$,

$$
 |\ell|^a|k|^{n-a}
 \le|\ell|\,|k|^{n-1}+|\ell|^n .
 \tag{PT.19}
$$

Split at $|k|\ge|\ell|$ to prove this inequality. The differentiated
quadratic reaction and the lower drift sum then have total
structured constant $402+4K_+=418$. Their low weighted first
derivative is at most $2Q_{0w}Q_{1w}$. Their high weighted
derivative is at most $2^{n+1}Q_0B_{n+5/3}$.
The binomial sum is at most $2^n$, giving the first terms of
$L_n,H_n$. In the drift sum the primitive removes one
coefficient derivative exactly: $d^{(a)}=-\beta
P_{\ne0}\partial^{a-1}(u^2+Kv^2)$, $a\ge2$.

For the ordered primitive let $\ell_1,\ell_2$ be the outer and
inner coefficient lags and put $L=|\ell_1|+|\ell_2|$.
Every lower word has $a+b+c=n$, $a+b\ge1$, and

$$
 |\ell_1|^{a+1}|\ell_2|^b|k|^c
 \le|\ell_1|L\,|k|^{n-1}+|\ell_1|L^n .
 \tag{PT.20}
$$

The first term, with
$w(\ell_1+\ell_2)\le w(\ell_1)w(\ell_2)$, sums to
$Q_{2w}Q_{0w}+Q_{1w}^2$.
For the second use
$|\ell_1|L^nw(\ell_1+\ell_2)\le(1+L)^{n+5/3}$ and the
two-factor moment inequality to obtain
$2^{n+2}Q_0B_{n+5/3}$.
The complete multinomial sum is at most $3^n$.
The intermediate frequency remains $k+\ell_2$;
its divisor is bounded by $1/4$ when it is nonzero and its
coefficient is exactly zero otherwise. In particular no
high projection is inserted inside $I$. Applying the same
structured coefficient190 proves the remaining terms of
(PT.18). All Fourier signs are included in the frame estimate.

## PT5. The middle band uses the already paid first-order solution

Put $Z_n=\partial_\phi^nZ$. Its part with
$388\le|k|<M_n$ obeys exactly

$$
                   \|(Z_n)_{\rm mid}\|_{\ell^2}
                          \le M_n^{n-1}V_1 .
 \tag{PT.21}
$$

There is no inversion on this large middle band. In the auxiliary
equation its forcing into the tail has norm at most

$$
 |\beta|K_n\|(Z_n)_{\rm mid}\|_{\ell^2},\qquad
 K_n=3Q_{0w}^2M_n+C_b(n).
 \tag{PT.22}
$$

The radial frame derivative and the principal angular matrix are
Fourier diagonal, so neither crosses the split. The full scalar
transport costs
$3\|d\|_{A_w}M_n\le3|\beta|Q_{0w}^2M_n$ by $K<4$
and the original primitive bound. All other coefficients and
$n d_\phi$ are bounded by $|\beta|C_b(n)$.
This includes the collar as well; its structured constants are
smaller than the displayed body constants.

The unchanged ordinary source frame is below6 globally.
The length of $I$ is below4. The two-branch unperturbed
$L^2_r$ source gain is consequently below18, since
$2(6)^2(4)<18^2$. At an actual raw jump the two branch
inputs cost at most12. Thus (PT.5) bounds all unperturbed
tail data at order $n$. Combining (PT.17)--(PT.22) gives

$$
 \begin{aligned}
 V_n\le{}&2{\cal D}_n+4r_nL_nV_{n-1}\\
 &+M_n^{n-1}(1+4r_nK_n)V_1
                  +4r_nH_nB_{n+5/3}V_0 .
 \end{aligned}
 \tag{PT.23}
$$

The low estimates needed here are already genuine inverses:

$$
                           V_0\le2{\cal D}_0,\qquad
                           V_1\le6{\cal D}_1 .
 \tag{PT.24}
$$

For clarity these constants do not follow from (PT.16).
Use the exact matching formulas QN.43/QH.31, set the physical
outer reflection to zero, and put its independent input $t$
in the affine outer port. At order0 the larger saved bounds
$(\chi,q_c,r_c)=(.310,750/749,1/749)$ apply.
At order1 use $(.801,250/249,1/249)$, which dominate QH.26
with independent outer data. With
$B_f=.126142$ and $B_c=.009000020$, every coefficient of both
complete frame suprema is below2 and6 respectively.
The source and raw-jump terms in (PT.5) dominate the corresponding
seven-port inputs. This proves (PT.24) on the entire collar/body
problem, not on a single local segment.

Set $A_1=6$ and, for $n\ge2$, define the explicit recurrence

$$
 A_n=2+4r_nL_nA_{n-1}
       +6M_n^{n-1}(1+4r_nK_n)+8r_nH_n .
 \tag{PT.25}
$$

Then (PT.23), monotonicity of $\mathcal D_j$ and $B_j$, and induction give
the promised complete tame bound

$$
 \boxed{\displaystyle
 V_n\le A_n\bigl\{{\cal D}_n
                    +B_{n+5/3}{\cal D}_1\bigr\},
 \qquad n\ge2 .}
 \tag{PT.26}
$$

Only the displayed higher background norm is variable in this
formula. The large explicit $A_n$ and $M_n$ depend solely on $n$
and the fixed low domain. For the first new order $n=2$ the
saved-rational evaluation gives

$$
 \begin{gathered}
 M_2=4741632000,\quad
 92C_b(2)/M_2<.002119867654,\quad
 8E_c(2)/M_2^{2/3}<.001196147960,\\
 L_2<31175052.268161,\quad H_2<261036.288001,\quad
 A_2<376761822306908686.583523 .
 \end{gathered}
 \tag{PT.27}
$$

These conservative constants prove regularity and a tame inverse;
they are not asserted to be useful small nonlinear contraction
constants.

## PT6. Actual raw reconstruction, traces, head and realization

In the body,
$\|F_N\|_{\rm Frob}^2\le N^{-1/3}(2+2/W_N)
<94N^{-1/3}<16$ for $N\ge388$.
The collar bound is smaller than9.
At $R$, $W_N>1/8$ gives
$\|F_N(R)\|<\sqrt{18}\,N^{-1/6}$.
The true root mixed-frame equivalence is the original factor9.
Consequently the actual solution satisfies, with a harmless
Bessel conversion $\langle k\rangle/|k|<17/16$,

$$
 \begin{aligned}
 \|h_H\|_{L^\infty_rH^n}&\le4(17/16)^nV_n,&
 \|h_H\|_{L^2_rH^n}&\le8(17/16)^nV_n,\\
 \|h_H(R)\|_{H^{n+1/6}}&\le6(17/16)^{n+1}V_n,&
 \|h_H(a)\|_{H^{n+1/3}\oplus H^n}
                      &\le9(17/16)^{n+1}V_n .
 \end{aligned}
 \tag{PT.28}
$$

The last two are traces of this solved graph; they are not trace
assertions for arbitrary radial $L^2$ heads. The triangular
old/new root conversion QN.44 commutes with every angular
derivative. Its original input/output fee $1.00001$ therefore
applies at every order here. Original root97, outer96 and the
low193 observation weights are retained.

The source convention does not hide any low-to-high path.
For example, with $s=n+1/3$, the whole-body intrinsic bounds
$|\beta|\max(1,|K|)<6$, $\gamma\max(1,|K|)<14$ from
[TH.7](R144-supplement-complete-low-norm-tame-Hessian-and-mean-preserving-smoothing.md)
give the explicit convenient estimate

$$
 \begin{gathered}
 \|P_HA_Qh_L\|_{L^2_rH^s}
       \le C_{\rm head}(s)B_{s+1}\|h_L\|_{L^2_rL^2},\\
 C_{\rm head}(s)
    =385^{s+1}2^{s+5}(6+14)(1+Q_0+Q_{1w}).
 \end{gathered}
 \tag{PT.29}
$$

To see this, the head derivative and its $H^s$ norm cost384
and $385^s$. The principal angular matrix is radial and its
head-to-high projection is exactly zero. Quadratic multiplication
uses its two-factor moment bound, the ordered primitive costs
$1/4$ and at most one derivative of $Q$, and the genuine
mean-input rank costs $14B_{s+1}|\langle(h_L)_2\rangle|$.
The displayed constant dominates their sum. Thus this source
also uses just one high background factor, including the
original moving mean. Its actual endpoint input, the two
physical curvature means, independent height and Robin data
are not assigned an interior trace by (PT.29).

For existence and regularity, start with finite angular
approximations of the unknown background and data, retaining
the original finite centre and its mean. The $A^3$ and higher
moment bounds do not increase under Fourier truncation.
The same actual mean reference and the same low two-end
inverse apply. The projected skew identities, (PT.18), and
all estimates above are uniform in this approximation.
Weak compactness followed by the exact Green equations gives
the infinite high solution; the order0 inverse gives uniqueness.
Applying (PT.23) successively proves its asserted higher
regularity. Piecewise radial approximation preserves the
actual state impulses and yields the same result for the
piecewise continuous coefficients in (PT.1).

The companion
[saved-rational calculation](../scripts/fourfold_codazzi_positive_angular_tame_saved_bounds.py)
evaluates only the18 displayed scalar comparisons and the
explicit recurrence example. It evaluates no old coefficient
array, Riccati equation, native Green kernel or new scientific
target. The unresolved all-order physical exterior feedback
must retain its actual angle changes and independent mean,
height, Robin and head endpoint ports when attached to this
two-end graph.

