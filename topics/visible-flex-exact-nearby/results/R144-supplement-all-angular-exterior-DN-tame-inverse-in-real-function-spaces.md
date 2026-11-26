# R144 supplement: all-angular exterior DN tame inverse in real function spaces

Date: 2026-11-27.
Session: visible-exact-astra-fb31ed6-20261127 / geometric_closure.

This proves all integer angular commutators of the actual exterior DN
derivative, and a tame inverse of its physical nonmean curvature graph,
through every finite Sobolev order. It holds on the real full-tail
endpoint domain of
[QN](R144-supplement-actual-whole-positive-high-inverse-in-a-full-tail-neighbourhood.md)
and
[QH](R144-supplement-real-H2-exterior-DN-and-one-angular-positive-high-inverse.md).
The high background norm occurs once and linearly. It is not required
to be small. Its physical-angle moment is bounded explicitly by one
raw endpoint $A^{n+1}$ norm below.

The complete height and physical curvature-mean DN columns are
retained. Their adjoints also give the genuine extensions to negative
Sobolev input spaces. The physical $B$ mean and overall height
translation keep their independent scalar rows. This result does not
identify the physical graph with a full raw boundary inverse, and does
not by itself prove the all-order positive body/high inverse.

## DT1. The same actual nonlinear graph on a larger zero-width ball

Let $g=|D_\theta|^2f_B$, with its zero mode omitted only in this
nonmean normalization. The independent overall height translation
is not part of $g$.
At the actual endpoint QN/QH have already proved

$$
 \|Z\|_{A^0}<4\,10^{-11},\quad
 \|Z_\theta\|_{A^0}<7\,10^{-11},\qquad
 \|g\|_{A^0_\sigma}\le b=2^{-60},\quad \sigma\ge1/16.
 \tag{DT.1}
$$

The unknown raw endpoint has only its real unweighted $A^3$ bound
$10^{-9}$. In particular (DT.1) is not a positive spatial strip
hypothesis for $Z$.

The same zero-width value and square-zero L2 module construction in
QN5 applies on the larger complex function-parameter product ball

$$
 \|Z\|_{A^0}<R_Z=5\,10^{-10},\qquad
 \|g\|_{A^0}<R_B=10^{-11}.
 \tag{DT.2}
$$

Here is the complete qualification from the already established
long-module positive formulas. For $z=R_Z,b_h=R_B$ set

$$
 \begin{gathered}
 r_f=10(z+b_h),\quad F=r_f+b_h,\quad
 \kappa=36(4096)F,\quad \epsilon=2^{-512},\\
 J_f={9\over1-\kappa},\qquad
 J_B={\epsilon+\kappa\over1-\kappa}.
 \end{gathered}
 \tag{DT.3}
$$

Exact rational arithmetic gives all four original sufficient
conditions

$$
 2F<2^{-25},\qquad 6F<2^{-20},\qquad \kappa<10^{-3},
 \qquad 9z+\epsilon b_h+9(4096)F^2<r_f .
 \tag{DT.4}
$$

These are the original boundary/state, contraction and curvature
self-map conditions. The unchanged proof therefore constructs the
same full nonlinear graph on (DT.2). Its holonomy small root,
the complete mean equation and mean-height integral survive by the
zero-width limit already proved in QN.26--QN.27. They are not
replaced by a graph of only nonzero-mode equations.

Write its four actual derivative rows as

$$
 T(Y)=D_Zd,\quad C(Y)=D_Zc_0,\quad
 U(Y)=D_gd,\quad V(Y)=D_gc_0,\qquad Y=(Z,g).
 \tag{DT.5}
$$

Equivalently $D_g=D_{f_B}|D_\theta|^{-2}$ on nonzero modes.
The first and third outputs are nonmean functions; the other two
are actual scalar curvature-mean functionals.
The original formulas give on (DT.2)

$$
 \begin{gathered}
 T\le\epsilon+4(16384)FJ_f,\qquad C\le(T-\epsilon)/8,\\
 U\le\epsilon+4(16384)F(1+J_B),\qquad V\le(U-\epsilon)/8,\\
 \|T\|_2+\|C\|_2<M_Z=.0035,\qquad
 \|U\|_2+\|V\|_2<M_B=.00039.
 \end{gathered}
 \tag{DT.6}
$$

For example the four separate upper expressions are below
$.003016273403,.000377034176,.000335141490,.000041892687$.
The operator norm is the genuine L2 module norm, including its
original radial summation, not an assumed consequence of a Wiener
value norm.

At an actual background (DT.1), the smaller original formulas give

$$
 \|T\|_2<t_{\rm low}=.00024,\quad
 \|C\|_2<c_{\rm low}=.00003,\quad
 \|U\|_2<u_{\rm low}=.000027,\quad
 \|V\|_2<v_{\rm low}=.000003375 .
 \tag{DT.7}
$$

Only (DT.7) is used on the highest input derivative. The larger
ball is used to bound background commutators.

## DT2. A translation-equivariant analytic multiplier lemma

Normalize the parameter algebra by

$$
 \|Y\|_{\mathfrak A}
 =\|Z\|_{A^0}/R_Z+\|g\|_{A^0}/R_B .
 \tag{DT.8}
$$

Its complex open unit ball lies inside (DT.2). At every actual
background set

$$
 t=\|Y\|_{\mathfrak A}<.081,\qquad x_0=.243,\qquad
 \Gamma_j={\|\partial_\theta^j Z\|_{A^0}\over R_Z}
              +{\|\partial_\theta^j g\|_{A^0}\over R_B}
 \quad(j\ge1).
 \tag{DT.9}
$$

The actual complete first moment satisfies $\Gamma_1<.141$.
For higher $j$ its finiteness is required, but not smallness.
Because the nonzero physical frequencies have absolute value at
least4, $\Gamma_j\le\Gamma_n$ when $1\le j\le n$.

Let $A(Y)$ be any of the four actual operators (DT.5).
Use $M=M_Z$ for $T,C$ or $M=M_B$ for $U,V$.
The operator-valued map is holomorphic on the parameter ball;
write its Taylor series there as

$$
 A(Y)=\sum_{p\ge0}A_p(Y,\ldots,Y).
 \tag{DT.10}
$$

Here $A_p$ is the symmetric $p$-linear Taylor coefficient, so
the factor $1/p!$ is included.
Complex Cauchy on $p$ direction discs of radius $1/p$ gives

$$
 \|A_p\|\le {p^p\over p!}M<3^pM,\qquad p\ge1 .
 \tag{DT.11}
$$

The estimate follows first on slightly smaller discs and then by a
limit. For the elementary last inequality, integrating $\log t$ from
1 to $p$ gives $p!>(p/e)^p$, and $e<3$.
These bounds apply to the actual L2 operator columns. Their constant
Taylor coefficient is translation invariant.

The full nonlinear problem, including its unique holonomy small
root, is equivariant under real angular translations. Thus

$$
 A(\mathcal T_\tau Y)=
       \mathcal T_\tau A(Y)\mathcal T_{-\tau}.
 \tag{DT.12}
$$

For a scalar output the left translation is the identity.
Consequently a Taylor coefficient on background frequencies
$\lambda_1,\ldots,\lambda_p$ and input frequency $k$ has the
exact output frequency $k+\sum_i\lambda_i$. For a scalar output
that sum must be zero. This follows by applying (DT.12) for every
real $\tau$; no spatial complex translation is used.

To make the ensuing absolute bound explicit, let

$$
 a_\lambda=|Z_\lambda|/R_Z+|g_\lambda|/R_B .
 \tag{DT.13}
$$

Testing (DT.11) on unit single-frequency background directions
and a unit L2 input mode bounds the corresponding Taylor kernel
by $3^pM$. Hence its whole absolute Fourier series is dominated
by $3^pM\,a^{*p}*|\widehat h|$.
This is a consequence of the full module estimate and exact
frequency conservation. It is not an assertion that an arbitrary
bounded L2 operator admits a positive convolution majorant.
Since $3t<x_0<1$, this full majorant is summable.

For every integer $n\ge1$, put $L=\sum_i\lambda_i$. The exact
commutator kernel is multiplied by
$(i(k+L))^n-(ik)^n$. The binomial theorem and separation at
$|k|=|L|$ give the sufficient bound

$$
 |(k+L)^n-k^n|
 \le2^n\{\,|L||k|^{n-1}+|L|^n\,\}.
 \tag{DT.14}
$$

The two background sums obey

$$
 \begin{gathered}
 \sum_{\lambda_1,\ldots,\lambda_p}
  \left(\sum_i|\lambda_i|\right)\prod_i a_{\lambda_i}
       =p\,t^{p-1}\Gamma_1,\\
 \sum_{\lambda_1,\ldots,\lambda_p}
  \left(\sum_i|\lambda_i|\right)^n\prod_i a_{\lambda_i}
       \le p^n t^{p-1}\Gamma_n .
 \end{gathered}
 \tag{DT.15}
$$

The second inequality is the convex inequality for the $n$th power
of a sum. Ordinary convolution Young inequalities now give the
complete commutator bound

$$
 \|[\partial_\theta^n,A(Y)]h\|_2
 \le a_n(M)\|\partial_\theta^{n-1}h\|_2
                     +b_n(M)\Gamma_n\|h\|_2 ,
 \tag{DT.16}
$$

where the explicit low-norm constants can be chosen as

$$
 a_n(M)={2^n\,3M(.141)\over(1-x_0)^2},\qquad
 b_n(M)={2^n\,3M\,n!\over(1-x_0)^{n+1}} .
 \tag{DT.17}
$$

Indeed $\sum_{p\ge1}p x^{p-1}=(1-x)^{-2}$, and

$$
 \sum_{p\ge1}p^n x^{p-1}
 \le{n!\over(1-x)^{n+1}},
 \tag{DT.18}
$$

because $p^n\le n!\binom{p+n-1}{n}$. All infinitely many
background Taylor orders have been summed. The high background
moment occurs once, through $\Gamma_n$.

## DT3. All four actual rows on both Sobolev sides

Combining (DT.16) with the exact Leibniz identity yields

$$
 \|\partial_\theta^n(Ah)\|_2
 \le a_{\rm low}\|\partial_\theta^nh\|_2
       +a_n(M)\|\partial_\theta^{n-1}h\|_2
       +b_n(M)\Gamma_n\|h\|_2 .
 \tag{DT.19}
$$

Here $a_{\rm low}$ is the corresponding entry of (DT.7).
The small highest-derivative coefficient is the actual operator
norm. In particular no growing $2^n$ factor is attached to that
coefficient in an attempted Neumann inversion.

For a scalar row, the left side in (DT.19) is zero for $n\ge1$;
the exact commutator states how that row acts on the $n$th input
derivative. Its original nonzero scalar value is retained.

For completeness, the same proof applies to the adjoint kernel:
it conjugates the Taylor coefficient and reverses the coefficient
frequencies, leaving (DT.11),(DT.13),(DT.15) unchanged.
Equivalently on the real parameter domain it is the conjugate
Taylor series for $A(Y)^*$ with the same coefficient majorants.
Translation on a scalar input is again the identity.
Thus (DT.19) also holds for the adjoint. Density and duality
give the actual derivative's extensions to negative Sobolev
inputs, including the two mean functionals.

One explicit sufficient operator bound for all $|s|\le n$ is

$$
 N_n(A)=2^n\left[(n+1)a_{\rm low}
       +\sum_{j=1}^n\{a_j(M)+b_j(M)\Gamma_j\}\right].
 \tag{DT.20}
$$

The derivative-vector norm proves it on $H^n$; the adjoint
proves it on $H^{-n}$, and interpolation fills the interval.
A scalar output is a constant function in this statement.
The bound is still linear in $\Gamma_n$, since
$\Gamma_j\le\Gamma_n$. The fixed background norm
$\Gamma_1<.141$ remains part of the low constants.

These are bounded realizations of the same actual nonlinear
derivatives. Their value graph and its parameter holomorphy live in
the zero-width algebra (DT.2), while the direction and output spaces
are the indicated Hilbert spaces. No unknown value is evaluated at
a complex angular point.

## DT4. The actual physical nonmean curvature inverse at every order

The exact physical tangent graph has its original rows

$$
 \begin{gathered}
 J_\theta\dot B_{\ne0}+Q_\theta z
       =T(Y)z+U(Y)p+r_B,\qquad p=|D_\theta|^2\dot f_B,\\
 \dot C_0=C(Y)z+V(Y)p+r_C .
 \end{gathered}
 \tag{DT.21}
$$

Here $z=\dot Z$, $Q_\theta$ is the original regular Fourier
multiplier, and $r_B,r_C$ are independent physical nonmean and
mean residuals. Its completed all-frequency multiplier has
$q_m>.9999999999993$; the conservative lower bound
$q_{\min}=.9999$ suffices.
The operator $Q_\theta$ commutes with every angular derivative.
The intrinsic parameter bump vanishes near this endpoint, so the
same multiplier applies throughout the current parameter interval.

Set

$$
 K_Y=Q_\theta-T(Y),\qquad
 F=-J_\theta\dot B_{\ne0}+r_B,\qquad K_Yz=F+U(Y)p .
 \tag{DT.22}
$$

This fixes the sign convention of the residual.
The actual L2 inverse exists and satisfies

$$
 \|K_Y^{-1}\|_{2\to2}
 \le(q_{\min}-t_{\rm low})^{-1}<c_*=1.001 .
 \tag{DT.23}
$$

It is the complete nonmean curvature graph, including the feedback
of its true holonomy mean inside $T$. No finite frequency cutoff
is used in this inverse.

Define

$$
 \begin{gathered}
 a_n^Z=a_n(M_Z),\quad b_n^Z=b_n(M_Z),\quad
 a_n^B=a_n(M_B),\quad b_n^B=b_n(M_B),\\
 K_0=c_*,\qquad
 K_n=(1+c_*a_n^Z)K_{n-1}
             +c_*[1+a_n^B+c_*b_n^Z+b_n^B].
 \end{gathered}
 \tag{DT.24}
$$

These constants are positive rational numbers, independent of
every $\Gamma_j$ for $j\ge2$. Even for $j=1$ they use only the
already paid bound .141. For example $K_1<2.048560688355<2.1$.

For every integer $n\ge1$ one has the actual tame inverse

$$
 \boxed{\quad
 \|z\|_{H^n}
 \le2^n(n+1)K_n
 \left[\|F\|_{H^n}+\|p\|_{H^n}
       +\Gamma_n(\|F\|_2+\|p\|_2)\right].
 \quad}
 \tag{DT.25}
$$

To prove this, differentiate (DT.22) exactly:

$$
 K_Y\partial_\theta^nz
 =\partial_\theta^nF+U\partial_\theta^np
          +[\partial_\theta^n,U]p+[\partial_\theta^n,T]z .
 \tag{DT.26}
$$

Use (DT.23), (DT.16) and
$\|z\|_2\le c_*(\|F\|_2+\|p\|_2)$.
Writing $S_n(z)=\sum_{j=0}^n\|\partial_\theta^jz\|_2$
and $E_n=\sum_{j=0}^n
(\|\partial_\theta^jF\|_2+\|\partial_\theta^jp\|_2)$,
induction gives

$$
 S_n(z)\le K_n[E_n+\Gamma_n E_0].
 \tag{DT.27}
$$

The new derivative uses $a_n^Z$ times the preceding derivative
of $z$, and its high-background term uses only $\|z\|_2$.
The height commutator is treated in the same way.
This is precisely recurrence (DT.24).
The derivative-vector Sobolev norm and
$E_n\le(n+1)(\|F\|_{H^n}+\|p\|_{H^n})$ give (DT.25).
There is no product of two uncontrolled high moments.

The same argument for $K_Y^*$ gives its $H^n$ inverse, and hence
the actual $H^{-n}$ inverse of $K_Y$ by duality. Its boundedness
constants remain linear in the high background moment.

The attached physical mean is still the second row of (DT.21).
For positive-order data it has the independent complete bound

$$
 |\dot C_0|\le c_{\rm low}c_*(\|F\|_2+\|p\|_2)
                           +v_{\rm low}\|p\|_2+|r_C| .
 \tag{DT.28}
$$

For negative-order data its genuine continuous extension follows
from DT3 and the adjoint inverse just proved. The physical
$\dot B_0$ row is kept independently, with the original exact
graph value $B_0=0$ and its independent inhomogeneous scalar
residual. It is not included in a power of $|D|$ or solved
by the nonmean operator $K_Y$. The overall height translation
likewise remains an independent scalar.

Thus (DT.25) does not claim that supplying an arbitrary raw
finite head automatically satisfies either physical mean equation.

## DT5. The high physical background is paid by one raw high norm

The high moment $\Gamma_n$ in the preceding formulas has a
direct real-coordinate bound. Keep the actual raw endpoint
$v=m+w$ and the actual $\theta_\phi=v/m$ of QN/QH.
Use their already completed constants

$$
 |m|\le M=7+10^{-9},\quad
 \|1/v\|_{A^0}<t_v=1/5.84,\quad
 \|w\|_{A^0}\le W_a=145(9.603792\,10^{-9})+10^{-9},\quad
 j=\theta_\phi\le j_u .
 \tag{DT.29}
$$

In particular $t_vW_a<1$.
For every $j\ge1$ the exact expression

$$
 C_{\theta^j}\circ\theta
 =\left({m\over v}\partial_\phi\right)^j{1\over v}
 \tag{DT.30}
$$

is a sum of terms

$$
 c_\alpha m^j v^{-j-p-1}
            \prod_{i=1}^p v^{(\alpha_i)},\qquad
 \alpha_i\ge1,\quad \sum_i\alpha_i=j .
 \tag{DT.31}
$$

Their absolute coefficient sum is at most
$s_j=3^{j-1}j!$.
Indeed differentiating such a term and multiplying by $m/v$
increases the absolute coefficient sum by at most
$p+(j+p+1)\le3j+1\le3(j+1)$.
Starting with $s_1=1$ proves the claimed bound by induction.

All derivatives in (DT.31) are derivatives of $w$.
Hölder interpolation of the nonnegative Fourier moments gives

$$
 \prod_{i=1}^p\|\partial_\phi^{\alpha_i}w\|_{A^0}
 \le\|w\|_{A^0}^{p-1}\|w\|_{\dot A^j}.
 \tag{DT.32}
$$

When $w=0$ the differentiated expression is zero, so the formula
extends by continuity. Combining (DT.29)--(DT.32) yields

$$
 \|C_{\theta^j}\circ\theta\|_{A^0}
 \le s_j M^j t_v^{j+2}\|w\|_{A^j}.
 \tag{DT.33}
$$

The factor $(t_v\|w\|_{A^0})^{p-1}$ has been bounded by1.
Thus no higher product of background norms remains.

The exact real change of measure has factor at most
$\sqrt{j_u}\le j_u$. For $n\ge1$ the physical mean of
$\partial_\theta^nC$ is zero, so the complete fourfold
embedding of QH.11 gives

$$
 \begin{aligned}
 \|\partial_\theta^n Z\|_{A^0}
 &\le .46\,\|C_{\theta^{n+1}}\|_2\\
 &\le .46\,j_u\,3^n(n+1)!\,
              M^{n+1}t_v^{n+3}\|w\|_{A^{n+1}_\phi}.
 \end{aligned}
 \tag{DT.34}
$$

The only derivative loss is the one explicit angular derivative
in the real $H^1$-to-Wiener embedding. The unknown is never
continued to a spatial strip.
The independent analytic height background already obeys
$\|\partial_\theta^ng\|_{A^0}\le n!16^n b$.
Consequently

$$
 \boxed{\quad
 \Gamma_n\le
 {.46\,j_u\,3^n(n+1)!M^{n+1}t_v^{n+3}\over R_Z}
                 \|w\|_{A^{n+1}_\phi}
              +{n!16^n b\over R_B}.
 \quad}
 \tag{DT.35}
$$

This is one linear raw high-background factor.
The actual endpoint $A^3$ domain supplies it through $n=2$.
For larger $n$ a finite raw $A^{n+1}$ norm is enough; it
need not be small.
The convenient small first-moment constant used in every
recurrence is still the sharper actual $\Gamma_1<.141$
from (DT.1), not this coarse high-norm conversion.
The original moving mean affects the low constants in
(DT.29) and is not frozen to the centre value.

## DT6. Reproducible arithmetic and the remaining coupling

The reader
[fourfold_codazzi_exterior_all_order_tame_saved_bounds.py](../scripts/fourfold_codazzi_exterior_all_order_tame_saved_bounds.py)
performs 18 exact rational comparisons. It verifies the enlarged
same-module ball, its complete four derivative bounds, the
actual low ratio and first moment, the true L2 curvature inverse,
and the first explicit tame recurrence. These are finite positive
combinations of the completed QN module formulas and real
endpoint bounds. No long nonlinear solve, old coefficient
enclosure, native row or old scientific target is evaluated.

The result supplies an actual all-order physical nonmean exterior
curvature inverse, its complete scalar mean/height rows and
explicit one-high-factor commutators. QH has already connected
the first angular order to the real positive high graph.
To extend that entire positive graph through all orders, its
body/frame commutators and the raw-to-physical direction
conversion still have to be combined in their actual source
and trace units. The finite/high Schur problem, the independent
physical scalar equations and world-height/phase closure remain
in that coupled problem.
