# R144 LG: the all-angular strong long height graph with complete means

2026-11-27, visible-exact-astra-fb31ed6-20261127 / geometric_closure.

**Proved; all6 new saved-rational combinations pass.** The same actual
finite long graph used by QN/FX has a complete strong radial value,
first derivative and Hessian at every angular order in its physical
angle. The holonomy root, its radial derivative, the mean-height
integral, both true endpoint mean slopes and the one independent
overall height translation are retained. The estimates contain one
high endpoint background factor after composition with the raw cap
curvature chart.

This concerns the complete radial height graph, not only an endpoint
DN observation. Its space is the original Fourier $\ell^2$ norm of
**coefficientwise radial suprema**. No pointwise-in-radius Sobolev
bound is silently transferred to that stronger space. In particular
a change to a raw moving-angle strong module needs its own argument;
ordinary real composition at each radius does not supply that
argument.

## LG1. The same finite graph and its actual strong spaces

Use the exact finite interval $0\le t\le L$, intrinsic functions
$a,w$ and physical angle $\theta$ of
[D.1--D.5](R119-supplement-actual-long-radial-nonlinear-dirichlet-problem.md).
In particular

$$
 (aw)_t=2aw,\qquad 0<aw<1,\quad 0<w<1,\quad w/a<5/28 .
 \tag{LG.1}
$$

The graph is the same actual curvature-selected graph as
[DT](R144-supplement-all-angular-exterior-DN-tame-inverse-in-real-function-spaces.md):
its right nonmean curvature is $Z$, its left normalized height
has $g=|D_\theta|^2f_B$, and its right normalized height $f_*$
is solved by the genuine finite-length curvature inverse.
Neither the right endpoint nor the positive finite-length
reflection is replaced by a half-line.

The actual and wide parameter domains are precisely DT.1--DT.2:

$$
 \begin{gathered}
 \|Z\|_{A^0}<4\,10^{-11},\qquad
 \|g\|_{A^0_\sigma}\le2^{-60},\quad \sigma\ge1/16,\\
 \|Z\|_{A^0}<5\,10^{-10},\qquad
 \|g\|_{A^0}<10^{-11}
 \quad\hbox{on the wide complex function ball}.
 \end{gathered}
 \tag{LG.2}
$$

Only the actual height background has the stated analytic
norm. The unknown cap background and the displayed directions
need not have a spatial strip.
The wide graph is the already constructed zero-width function
graph, including its true holonomy and both curvature means.

For $s\ge0$ define the complete nonmean direction norm

$$
 \|h\|_{\mathcal Y_s}^2
 =\sum_{k\in4\mathbb Z\setminus\{0\}}\langle k\rangle^{2s}
 \left\{
 |k|^2\|h_k\|_{C_t^0}
       +|k|\|(h_k)_t\|_{C_t^0}
       +\|(h_k)_{tt}\|_{C_t^0}
 \right\}^2 .
 \tag{LG.3}
$$

Its background algebra $\mathcal Y_A$ uses the $\ell^1$
sum of the same three coefficientwise radial suprema.
This is exactly the original strong module, with its two
angular derivatives, one mixed derivative and two radial
derivatives. The order of supremum and summation is fixed.
For a scalar mean use ordinary $C^1_t$ or $C^2_t$ with
the sum of the displayed derivative suprema.

The completed FX bounds, restricted to $j=1$, give on
the whole wide ball

$$
 \|h\|_{\mathcal Y_A}<r_y=2^{-24},\qquad
 \|D_Zh:L^2_\perp\to\mathcal Y_0\|<48,\qquad
 \|D_gh:L^2_\perp\to\mathcal Y_0\|<2^{14}.
 \tag{LG.4}
$$

Here the curvature column uses the actual inverse below12
and the right lift below4. The height column is the complete
left lift followed by its actual right-curvature correction,
not only its direct lift. These are the genuine
$\ell^2(C_t)$ module statements of FX2--FX3; no new Green
calculation is being claimed.

## LG2. Full scalar recovery without an unproved radial derivative

Put

$$
 \begin{gathered}
 P=h_\theta,\quad U=h_{\theta\theta},\quad
 K_\perp=2h+h_t,\quad V=2h_\theta+h_{t\theta},\\
 K=K_\perp+\kappa,\qquad
 \mathcal Q_{\rm full}
 ={E(V-P)^2+K^2+2EKU+EU^2-qP^2\over1+K+EU}.
 \end{gathered}
 \tag{LG.5}
$$

The scalar $\kappa$ is the original holonomy-one small root.
The complete original absolute estimates, before a nonmean
projection is taken, give for $Y=\|h\|_{\mathcal Y_A}\le2r_y$

$$
 \|\kappa\|_{C_t^0}\le2^{12}Y^2,\qquad
 \|\mathcal Q_{\rm full}\|_{\mathcal F_A}\le2^{11}Y^2 .
 \tag{LG.6}
$$

For a genuine solved graph the holonomy derivative identity
in D5 gives the exact missing mean equation

$$
                         \kappa_t+2\kappa
                            =\langle\mathcal Q_{\rm full}\rangle.
 \tag{LG.7}
$$

The same identity follows first on smooth real or complex
angular approximations and then in the original zero-width
module, as in QN.26--QN.27.
In particular one must not differentiate the algebraic
formula for $\kappa$ and assume an extra angular/radial
derivative of the unknown state.

Keep a single independent physical height translation
$\lambda$. The true mean-height recovery is

$$
 \begin{gathered}
 v_0(t)=\lambda+\int_0^t a(s)w(s)\kappa(s)\,ds,\\
 c(t)={v_0(t)-\lambda\over a(t)w(t)}
       =\int_0^t e^{-2(t-s)}\kappa(s)\,ds,\\
 v(t,\theta)=a(t)w(t)\{h(t,\theta)+c(t)\}+\lambda .
 \end{gathered}
 \tag{LG.8}
$$

Thus $c(0)=0$ and the two endpoint mean heights are
not independently specifiable. Their true difference
is $a(L)w(L)c(L)$.
Equations (LG.7)--(LG.8) give the full jet

$$
 \begin{gathered}
 \kappa_t=\langle\mathcal Q_{\rm full}\rangle-2\kappa,\qquad
 c_t=\kappa-2c,\\
 c_{tt}=\langle\mathcal Q_{\rm full}\rangle-4\kappa+4c .
 \end{gathered}
 \tag{LG.9}
$$

Consequently, uniformly in the actual long length,

$$
 \|\kappa\|_{C_t^1}+\|c\|_{C_t^2}
       \le51200Y^2<2^{16}Y^2 .
 \tag{LG.10}
$$

The five coefficient charges are respectively
$4096,10240,2048,8192,26624$, whose sum is51200.
They include both the value and the radial derivative
of the actual holonomy root.

There is also a genuine direction-module version of
this estimate. Extend the five jets in (LG.9) algebraically
to any nearby $h$ by defining $\kappa_t$ and $c_{tt}$
through their right sides. All operations, including the
weighted physical mean, use the same absolute algebra
and its square-zero $\ell^2(C_t)$ module.
The entire bound (LG.10) therefore holds in that
square-zero algebra with norm equal to the sum of the
background and direction norms.
Putting a direction amplitude $r_y$ into the ball
$2r_y$ gives the complete module derivative bound

$$
 \|D_h(\kappa,\kappa_t,c,c_t,c_{tt})\|
               <4(2^{16})r_y=1/64 .
 \tag{LG.11}
$$

This is not an inference from a bare Wiener value norm:
the same mean, products, reciprocal/root series and
exponential integral are bounded on the distinguished
module factor. On the solved graph the five jets are
the actual compatible $C^1$ and $C^2$ jets by (LG.7).
The closed jet identities then identify their parameter
derivatives with the derivatives in those genuine
function spaces.

Define the full graph and its norm by

$$
 \mathcal H(Z,g)=(h,\kappa,c),\qquad
 \|\mathcal H\|_{\mathfrak Y_s}
          =\|h\|_{\mathcal Y_s}
                      +\|\kappa\|_{C_t^1}+\|c\|_{C_t^2}.
 \tag{LG.12}
$$

All scalar outputs have their true zero angular frequency.
The independent $\lambda$ remains outside this normalization;
dividing it by the extremely small $aw$ would be incorrect.
Equations (LG.4), (LG.10)--(LG.11) give

$$
 \|\mathcal H\|_{\mathfrak Y_A}<2r_y,\qquad
 \|D_Z\mathcal H\|+\|D_g\mathcal H\|
       <{65\over64}(48+2^{14})<2^{15}.
 \tag{LG.13}
$$

The second bound is for the full two-column module sum on
the wide function-parameter ball.

## LG3. Every angular order in the actual radial module

Retain the physical parameter moments

$$
 \Gamma_n={\|\partial_\theta^nZ\|_{A^0}\over5\,10^{-10}}
           +{\|\partial_\theta^ng\|_{A^0}\over10^{-11}}
 \quad(n\ge1),\qquad \Gamma_0=1 .
 \tag{LG.14}
$$

The actual normalized mass is below $.081$ and its
Taylor mass below $.243<1/4$, exactly as in DT.
Set $M=2^{15}$ and use $J_n,K_n$ of OX.15.
For physical pairs of direction data $X,Y$, the complete
graph satisfies

$$
 \begin{aligned}
 \|D\mathcal H[Y]\|_{\mathfrak Y_n}
       &\le M J_n\{|Y|_{H^n}+\Gamma_n|Y|_{L^2}\},\\
 \|D^2\mathcal H[X,Y]\|_{\mathfrak Y_n}
       &\le M K_n\{|X|_{A^0}|Y|_{H^n}
                 +|X|_{A^n}|Y|_{L^2}
                 +\Gamma_n|X|_{A^0}|Y|_{L^2}\}.
 \end{aligned}
 \tag{LG.15}
$$

The notation for pairs is the component sum of the
two true curvature/normalized-height input norms.
The all-order value bound can be chosen as

$$
 \|\mathcal H(Z,g)\|_{\mathfrak Y_n}
          \le2^{2n+6}(n+1)!\,r_y(1+\Gamma_n).
 \tag{LG.16}
$$

Here is why the original radial space, not just pointwise
angular norms, is covered. The module derivatives in
(LG.13) are holomorphic operator-valued families.
Their Taylor coefficients have complete bounds $3^qM$.
Translation covariance forces an input frequency plus
all background lags to equal the actual output frequency.
Test each coefficient on genuine single Fourier
directions, retaining the full radial function at the
output. Its norm is the sum of the three weighted
radial suprema in (LG.3), or the scalar jet norm
for a mean output.

The resulting nonnegative convolution majorant acts
directly on these Banach-valued coefficients.
The triangle inequality is taken before the radial
supremum, and then ordinary $\ell^1*\ell^2\to\ell^2$
Young is applied. Thus the order of supremum and
Fourier summation is never reversed.
The complete first and second Taylor sums are exactly
OX.23--OX.26 with the multiplier $M$, proving (LG.15).
All original intermediate Fourier signs and scalar
outputs remain.
The same argument on the value map, whose wide norm
is below $2r_y$, bounds its $n$th angular moment by
$6r_y n!\Gamma_n/(1-1/4)^{n+1}$ for $n\ge1$.
The Bessel enlargement and the order-zero bound
give (LG.16).

These arguments also establish genuine continuous
Fréchet derivatives in the stated scales: finite
Fourier approximations obey the same complete
module bounds, their exact integral equations
converge, and the unique low graph identifies the
limit. No arbitrary analytic extension of an
$L^2$ direction in its spatial variable is used.

## LG4. Raw cap parameters with one high background factor

Return to the actual endpoint background
$Q=Q_*+q$, $\|q\|_{A^3,\oplus_1}\le10^{-9}$, and set

$$
 \widehat{\mathcal H}(Q,g)
       =\mathcal H(P_{\perp,\theta}(C_Q-C_{\rm ref}),g).
 \tag{LG.17}
$$

The **output is still in the fixed physical angle**.
Use $B_s,E_s,P_n,C_n$ and $\mathcal T_n$ of
[OX](R144-supplement-physical-output-boundary-differential-and-all-angular-Hessian.md).
The full composition obeys

$$
 \boxed{\displaystyle
 \begin{aligned}
 \|D\widehat{\mathcal H}[x]\|_{\mathfrak Y_n}
   &\le2^{15}C_n\{E_{n+3}(x)+B_{n+2}E_3(x)\},\\
 \|D^2\widehat{\mathcal H}[x,y]\|_{\mathfrak Y_n}
   &\le2^{15}C_n\,\mathcal T_n(x,y).
 \end{aligned}}
 \tag{LG.18}
$$

The proof uses the exact two chain-rule terms
$D^2\mathcal H[(Z'_Q[h],p),(Z'_Q[k],t)]$
and $D_Z\mathcal H\,Z''_Q[h,k]$.
OX.29 supplies the low $L^2$ and $A^0$ direction bounds;
OX.16 and OX.22 supply the high input and the single
background moment. Applying those low bounds in the
second terms of (LG.15) is essential: substituting
two high chart estimates there would incorrectly
produce their product.
The same bookkeeping as OX5 gives the coefficient
$5\,2^{15}P_n(J_n+K_n)$, which is smaller than
the displayed $2^{15}C_n$.

An all-order value bound follows from (LG.16) and
$\Gamma_n\le P_nB_{n+2}$, with no high norm
smallness condition. The independent physical
height direction is normalized by its actual
$p=|D_\theta|^2\dot f_B$ throughout.

## LG5. Two complete endpoint traces and actual physical height

At each actual endpoint, $f$ denotes $f_B$ or the
solved $f_*$, with no change in its original scale.
The complete physical traces are

$$
 \begin{gathered}
 v_\perp=aw f,\qquad
 (v_a)_\perp=w(2f+h_t),\qquad
 (v_a)_0=w\kappa,\\
 v_0(L)-v_0(0)=a(L)w(L)c(L).
 \end{gathered}
 \tag{LG.19}
$$

Every quantity in (LG.19), and its first two parameter
derivatives, is a bounded observation of the complete
graph (LG.12), in its displayed actual units.
Both mean slopes and the mean-height difference are
outputs. They have not become extra free Dirichlet
conditions. The two outward radial signs are still
opposite when these traces are used for matching.

There is also a useful genuine physical $C^2$ height
consequence. For any graph direction
$H=(\dot h,\dot\kappa,\dot c)$ let
$\dot v=aw(\dot h+\dot c)+\dot\lambda$.
The actual polar derivative formulas, using the
compatible jets, are

$$
 \begin{aligned}
 \dot v_a&=w(2\dot h+\dot h_t+\dot\kappa),\\
 a^{-1}\dot v_\theta&=w\dot h_\theta,\\
 \dot v_{aa}&={w\over a}
       (2\dot h+3\dot h_t+\dot h_{tt}
                              +\dot\kappa+\dot\kappa_t),\\
 (\nabla^2\dot v)_{a\theta}
       &={w\over a}(\dot h_\theta+\dot h_{t\theta}),\\
 (\nabla^2\dot v)_{\theta\theta}
       &={w\over a}(\dot h_{\theta\theta}
                              +2\dot h+\dot h_t+\dot\kappa).
 \end{aligned}
 \tag{LG.20}
$$

There is no isolated inverse of the extremely small
radius in these formulas: it is paired with $w$.
The original fourfold Cauchy--Schwarz embedding
$\mathcal Y_1\to\mathcal Y_A$ costs at most $11/10$.
The nonmean physical $C^2$ coefficient, counting
the mixed Hessian entry twice, is at most

$$
 {11\over10}\left\{
 {1\over16}+{3\over8}+{1\over4}
       +{5\over28}\left({15\over8}
                      +2{5\over4}+{11\over8}\right)\right\}<4 .
 \tag{LG.21}
$$

The corresponding scalar mean coefficient is
$1+2(5/28)<2$.
The convenient full conclusion is therefore

$$
 \|\dot v\|_{C^2({\rm actual\ long})}
       \le16\|H\|_{\mathfrak Y_1}+|\dot\lambda|.
 \tag{LG.22}
$$

The same linear reconstruction applies to the
second parameter derivative; its overall
translation Hessian is zero.
Thus (LG.18) at $n=1$ gives complete actual
physical-height first and second derivatives
with directions at order $H^4$ and one
endpoint background at $A^3$.
The original north-cap height is $Z_0-v$,
so its variation has the corresponding minus
sign. This does not change the norm.

This theorem covers the height component and its
actual strong radial graph. The horizontal
coframe reconstruction and world-frame/position
matching keep their own derivative equations.
Nor is (LG.22) a global reach or embeddedness
conclusion before the remaining matching
conditions have been solved.

## LG6. The still distinct raw moving-angle module

The good physical tangent and a raw pulled tangent
obey exactly U.25:

$$
               \dot h^\flat=z+b\,h^\flat_\phi .
 \tag{LG.23}
$$

For a raw cap input in $L^2$, its angle displacement
has only one gained angular derivative. That alone
does not put the raw term on the right into the
unshifted strong module (LG.3).
This proof has kept the output in the physical
angle, where (LG.15)--(LG.22) are complete.
A future raw-module assertion must either use
the genuine good tangent with its phase, or
differentiate the complete FX pulled PDE with
the appropriate extra derivative on the
angle-parameter input. A pointwise-in-radius
composition bound is insufficient.

The companion
[rational combination](../scripts/fourfold_codazzi_strong_long_tame_saved_bounds.py)
checks only6 new scalar combinations: the complete
mean jet, its module, the two whole long columns,
and the actual physical height observation.
It evaluates no native array, reference equation,
new long solution or completed scientific target.
