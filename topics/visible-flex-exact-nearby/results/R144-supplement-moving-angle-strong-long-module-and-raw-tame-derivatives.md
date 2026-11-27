# R144 RG: the moving-angle strong long module and raw tame derivatives

2026-11-27, visible-exact-astra-fb31ed6-20261127 / geometric_closure.

**Proved; all14 new saved-rational comparisons pass.** The actual
pulled long PDE has a complete strong module for its angle-parameter
direction: the angle coefficient is supplied in $H^1$, while its
nonmean curvature and twice differentiated pulled-height data are
supplied in $L^2$. The full module norm is below $2^{15}$.
This includes the holonomy root, its radial derivative, the physical
mean-height recovery and the distinct ordinary moving-mean shift.

The resulting genuine function-parameter family gives all angular
orders and the first two derivatives of the **raw moving-angle**
height graph, with one higher endpoint $A^{n+2}$ factor and the
displayed finite direction buffer. The proof works directly in
the original Fourier $\ell^2$ of coefficientwise radial suprema.
It does not infer boundedness there from pointwise-in-radius
real composition.

This pays the raw-height distinction in U.25 and
[LG6](R144-supplement-all-angular-strong-long-height-graph-with-complete-means.md).
LG's physical-output graph remains a separate valid realization.
The complete horizontal reconstruction and the remaining global
matching equations are not inferred from this height theorem.

## RG1. The same complete pulled graph and its parameters

Use the actual finite long interval, intrinsic coefficients,
both actual endpoints and full pulled equation of
[FX.1--FX.20](R144-supplement-fixed-moving-angle-long-module-and-full-exterior-commutators.md).
The independent function parameters are

$$
 j=1+e,\qquad
 \|e\|_{A^1}<\epsilon_j=2^{-18},\qquad
 \|z\|_{A^0}<R_z=5\,10^{-10},\qquad
 \|\mathfrak g\|_{A^0}<R_g=10^{-11}.
 \tag{RG.1}
$$

All three parameters have ordinary mean zero.
At the actual raw endpoint

$$
 e=v/m-1,\qquad z=P_{\perp,\phi}(1/v),\qquad
 \mathfrak g=-\partial_\phi^2(f_B\circ\Theta),\qquad
 \Theta=\mathrm{id}+I_\phi e,\quad m=\langle v\rangle.
 \tag{RG.2}
$$

The parameter $\mathfrak g$ is the twice differentiated
**pulled** nonmean height. Its relation to a fixed physical
height direction is paid in RG5, not assumed here.

For ordinary mean-zero $y$ use
$h^\flat=J_jy=y-M_jy$,
$M_jf=\langle jf\rangle$, and $D_j=j^{-1}\partial_\phi$.
The genuine equation and right curvature condition are

$$
 \begin{gathered}
 [(\partial_t+2)^2+\partial_\phi^2]y
      =\mathcal Q_j(y)-\mathcal V_jy,\\
 \mathcal V_jy=P_{\perp,\phi}
 \{(j^{-2}-1)y_{\phi\phi}-j^{-3}e_\phi y_\phi\},\\
 y(0)=|D_\phi|^{-2}\mathfrak g,\qquad
 P_{\perp,\phi}C_j(y)(L)=z .
 \end{gathered}
 \tag{RG.3}
$$

The right Dirichlet value is determined by the genuine
curvature inverse. The full physical mean and its
compatibility with the cap mean are not imposed by
this nonmean condition.
All coefficients, primitives, the holonomy small root
and its actual mean normalization in FX are retained.

Use precisely the strong spaces $\mathcal Y_s$ of LG.3,
now with frequencies in the fixed moving angle $\phi$.
The previously proved graph on (RG.1) satisfies

$$
 Y:=\|y\|_{\mathcal Y_A}<r_y=2^{-24},\quad
 \|G_D^{\rm actual}\|<64,\quad
 \|\text{actual right lift}\|<4,\quad
 \|(D C_R)^{-1}\|<12 .
 \tag{RG.4}
$$

The curvature inverse has the original
$L^2_\perp\to\dot H^2_\perp$ units. Its finite-length
reference, two endpoints and full Fourier signs have
not changed.

## RG2. The angle direction is a genuine H1 module input

Let $\xi$ be a zero-mean angle-parameter direction.
We now construct $D_ey[\xi]$ for $\xi\in H^1_\phi$
inside the actual $\ell^2(C_t)$ module.
The additional derivative in this input is essential:
the coefficient variation contains $\xi_\phi$.

First consider only the fixed-state coefficient algebra.
It remains valid on

$$
                       \|e\|_{A^1}<1/64 .
 \tag{RG.5}
$$

This is **not** an enlargement of the nonlinear PDE
or curvature inverse domain in (RG.1).
It is used solely to differentiate explicit coefficients
at a fixed state. The original physical states satisfy
on this algebra ball

$$
 \|P\|<Y/3,\quad \|U\|<2Y,\quad
 \|K_\perp\|<Y/2,\quad \|V\|<2Y,\qquad
 \|M_j\|<33/32 .
 \tag{RG.6}
$$

For example the corresponding positive expressions are

$$
 {1\over4(1-1/64)},\quad
 {1\over(1-1/64)^2}+{1/64\over4(1-1/64)^3},\quad
 {3\over8}(1+1/64),\quad
 {3/2\over1-1/64}.
 \tag{RG.7}
$$

The estimate for $K_\perp$ uses that $2y+y_t$ has
ordinary mean zero:
$M_j(2y+y_t)=\langle e(2y+y_t)\rangle$.
It does not use the unnecessarily larger norm of
$J_j$ on a general function with a nonzero mean.

Thus the same absolute holonomy and complete source
estimates apply, for $Y\le2r_y$:

$$
 |\kappa|\le2^{12}Y^2,\qquad
 \|\mathcal Q_j(y)\|\le2^{11}Y^2,\qquad
 \|C_j(y)-C_{\rm ref}\|<16Y .
 \tag{RG.8}
$$

For the last bound, $|K|<Y$, $|U|<2Y$, $|P|<Y/3$
give $|D-1|<3Y$ in the exact curvature formula.
Using $|D^{-1/2}|<2$, $|D^{-1/2}-1|<6Y$ and
$\chi/\sqrt E<1/5$ gives the smaller bound
$(16/5)Y$.
The actual $C$ mean is part of this estimate.

At any original $e$ in (RG.1), a disc of radius
$1/128$ in the coefficient direction remains in
(RG.5), since $2^{-18}+1/128<1/64$.
The square-zero algebra here is
$A^1\oplus\varepsilon H^1$, with the outputs in
$A^0\oplus\varepsilon L^2$, retaining the original
coefficientwise radial suprema. Multiplication by
an $A^1$ coefficient is bounded on $H^1$; the
single derivative maps its module factor to $L^2$.
The physical mean, normalized primitive and root
series are bounded on this same distinguished
factor. Hence the **module**, rather than only
the Wiener value map, admits Cauchy's bounds

$$
 \|D_e\mathcal Q_j(y)[\xi]\|_{\mathcal F_2}
       \le2^{18}Y^2\|\xi\|_{H^1},\qquad
 \|D_eC_j(y)[\xi]\|_2
       \le2^{11}Y\|\xi\|_{H^1}.
 \tag{RG.9}
$$

The full principal coefficient has the explicit
derivative

$$
 D_e(\mathcal V_jy)[\xi]
 =P_\perp\{-2j^{-3}\xi y_{\phi\phi}
            +3j^{-4}e_\phi\xi y_\phi
            -j^{-3}\xi_\phi y_\phi\}.
 \tag{RG.10}
$$

Its complete source norm is below
$8Y\|\xi\|_{H^1}$.
For example with $s=(1-1/64)^{-1}$ the direct
coefficient is $2s^3+(3/4)(1/64)s^4+s^3/4<8$.
All these products act in the original
$\ell^2(C_t)$ source space, with the background
coefficients in the corresponding $\ell^1(C_t)$
algebra.

Since $2^{18}r_y<1$, the total fixed-state source
for the angle variation is below
$9Y\|\xi\|_{H^1}$.
The actual zero-Dirichlet inverse in (RG.4) therefore
gives $576Y\|\xi\|_{H^1}$.
Its right curvature charge, including the direct
coefficient variation and the full state curvature
derivative below16, is at most

$$
              (2^{11}+16\cdot576)Y\|\xi\|_{H^1}
                       =11264Y\|\xi\|_{H^1}.
 \tag{RG.11}
$$

Correct this by the actual curvature inverse below12
and the actual right lift below4. The complete
angle-state derivative is consequently

$$
 \|D_ey[\xi]\|_{\mathcal Y_0}
  \le\{576+4(12)(11264)\}Y\|\xi\|_{H^1}
  =541248Y\|\xi\|_{H^1}
  <2^{20}Y\|\xi\|_{H^1}.
 \tag{RG.12}
$$

The zero-Dirichlet source and both boundary
corrections are included. The fixed-state
coefficient disc has not been used as an
unproved PDE inverse disc.

## RG3. Physical and ordinary means remain distinct

The complete physical mean recovery obeys

$$
 \kappa_t+2\kappa=M_j\mathcal Q_{\rm full,j},\qquad
 c(t)=\int_0^t e^{-2(t-s)}\kappa(s)\,ds .
 \tag{RG.13}
$$

Here $j_t=0$ exactly. The mean-height normalization,
its two true endpoint slopes, and the independent
translation $\lambda$ are the same as LG2.
Using $\|M_j\|<2$ gives

$$
 \|\kappa\|_{C_t^1}+\|c\|_{C_t^2}
              \le55296Y^2<2^{16}Y^2 .
 \tag{RG.14}
$$

The five charges are
$4096,12288,2048,8192,28672$.
The same compatible-jet and square-zero argument
as LG2 gives the state-module derivative below
$1/64$, and the fixed-state angle derivative
below $2^{23}Y^2\|\xi\|_{H^1}$.
In particular the mean equation is not
differentiated by assuming an unavailable
derivative of the nonlinear root formula.

The raw height also contains the distinct
ordinary mean shift

$$
 \bar y_j(t)=M_jy(t)=\langle e\,y(t)\rangle,\qquad
 h^\flat+c=y+c-\bar y_j .
 \tag{RG.15}
$$

Because $y$ has ordinary mean zero,

$$
 \|\bar y_j\|_{C_t^2}<2\epsilon_jY,\quad
 \|D_y\bar y_j\|<2\epsilon_j,\quad
 \|D_e\bar y_j[\xi]\|_{C_t^2}<2Y\|\xi\|_2 .
 \tag{RG.16}
$$

The coefficient $21/16$ from
$\|y\|+\|y_t\|+\|y_{tt}\|$ is below2.
It would be incorrect to call either $c$ or
$-\bar y_j$ a disposable constant: both are
actual radial functions in the raw graph.

Define

$$
 \begin{gathered}
 \mathcal G(e,z,\mathfrak g)=(y,\kappa,c,\bar y_j),\\
 \|\mathcal G\|_{\mathfrak Z_s}
   =\|y\|_{\mathcal Y_s}
          +\|\kappa\|_{C_t^1}+\|c\|_{C_t^2}
          +\|\bar y_j\|_{C_t^2},\\
 |X|_{\mathfrak M_s}
   =\|\xi\|_{H^{s+1}}+\|\zeta\|_{H^s}
                              +\|\omega\|_{H^s},
 \qquad X=(\xi,\zeta,\omega).
 \end{gathered}
 \tag{RG.17}
$$

The physical raw perturbation is exactly
$v^\flat=aw(y+c-\bar y_j)+\lambda$.
The scalar translation stays independent, without
division by $aw$.

The actual complete angle column has norm below

$$
 (1+1/64+2\epsilon_j)2^{20}r_y
                   +2^{23}r_y^2+2r_y<1/8 .
 \tag{RG.18}
$$

The other two actual columns have sum below
$(1+1/64+2\epsilon_j)(48+2^{14})$.
Thus the whole genuine module family on (RG.1) has

$$
 \|\mathcal G\|_{\mathfrak Z_A}<2r_y,\qquad
 \|D\mathcal G:\mathfrak M_0\to\mathfrak Z_0\|<M=2^{15}.
 \tag{RG.19}
$$

All four output components are retained in this
single module bound.

## RG4. Complete raw angular estimates

The normalized parameter mass is at most the mass
already qualified in FX, with its unused $u$ term
omitted; it is below $1/4$.
For $n\ge1$ define

$$
 \Gamma_n^{\rm raw}
  ={\|\partial_\phi^ne\|_{A^1}\over\epsilon_j}
    +{\|\partial_\phi^nz\|_{A^0}\over R_z}
    +{\|\partial_\phi^n\mathfrak g\|_{A^0}\over R_g},
 \qquad \Gamma_0^{\rm raw}=1 .
 \tag{RG.20}
$$

The largest Taylor mass is now $3/4$.
For a parameter direction use

$$
 |X|_{\mathfrak A_s}
       =\|\xi\|_{A^{s+1}}+\|\zeta\|_{A^s}
                                    +\|\omega\|_{A^s}.
$$

Set

$$
 \widehat J_n=2^{3n+5}(n+1)!,\qquad
 \widehat K_n=2^{4n+48}(n+1)! .
 \tag{RG.21}
$$

Then the full family obeys

$$
 \begin{aligned}
 \|D\mathcal G[Y]\|_{\mathfrak Z_n}
 &\le M\widehat J_n
       \{|Y|_{\mathfrak M_n}
                   +\Gamma_n^{\rm raw}|Y|_{\mathfrak M_0}\},\\
 \|D^2\mathcal G[X,Y]\|_{\mathfrak Z_n}
 &\le M\widehat K_n
       \{|X|_{\mathfrak A_0}|Y|_{\mathfrak M_n}
          +|X|_{\mathfrak A_n}|Y|_{\mathfrak M_0}\\
 &\hspace{33mm}
          +\Gamma_n^{\rm raw}
                    |X|_{\mathfrak A_0}|Y|_{\mathfrak M_0}\}.
 \end{aligned}
 \tag{RG.22}
$$

This is the genuine Hilbert direction module
constructed in RG2--RG3.
For its first input, test a Fourier mode with
its exact $H^1$ normalization. Translation
covariance of the entire pulled PDE, root,
curvature inverse and mean shifts then gives
the same signed frequency conservation as FX.
The background $e$ coefficient carries its
$(1+|k|)$ algebra weight. All outside angular
derivatives commute with these input weights.

The complete kernel proof is therefore the
Banach-valued radial proof in LG3, now with
Taylor mass $x=3/4$.
The first-derivative sums are bounded by
$2^n/(1-x)$ and
$2^n3n!/(1-x)^{n+1}$.
For the differentiated family the corresponding
sums are $3^n3/(1-x)^2$ and
$3^n18(n+1)!/(1-x)^{n+2}$.
The smallest parameter radius has reciprocal
below $2^{37}$.
These expressions are bounded by (RG.21).
Every mean output is included with its true
zero output frequency.

The same value-family argument gives, for example,

$$
 \|\mathcal G\|_{\mathfrak Z_n}
       \le2^{3n+6}(n+1)!\,r_y
                             (1+\Gamma_n^{\rm raw}).
 \tag{RG.23}
$$

The actual higher moments have already been
paid by FX.46--FX.48:

$$
               \Gamma_n^{\rm raw}\le D_nB_{n+1}^R,
        \qquad B_s^R=1+\|Q(R)\|_{A^s,\oplus_1}.
 \tag{RG.24}
$$

The constants $D_n$ are the explicit positive
factorial expressions in FX.48. They are
independent of all high unknown norms.

## RG5. The true raw cap parameter derivatives

The raw graph is

$$
 \widehat{\mathcal G}(Q,g)
       =\mathcal G(\Pi(Q,g)),\qquad
 \Pi(Q,g)=(e,z,\mathfrak g),
 \qquad g=|D_\theta|^2f_B .
 \tag{RG.25}
$$

This is its ordinary Fréchet derivative as a
moving-angle value map. In particular the
angle transport is now part of the derivative
itself.

For $x=(h,p)$ retain the exact normalized
$\mu_h,\ell_h$ of OX.5. The three first
parameter directions are

$$
 \begin{aligned}
 e_x&=m^{-1}(h_2-j\mu_h),\\
 z_x&=P_{\perp,\phi}(-h_2/v^2),\\
 \mathfrak g_x
   &=-\partial_\phi^2\{
       (|D_\theta|^{-2}p)\circ\Theta
                   +\ell_h(f_{B,\theta}\circ\Theta)\}.
 \end{aligned}
 \tag{RG.26}
$$

Every inverse angular power acts on its
actual nonmean input.
The second directions, for $y=(k,t)$, are

$$
 \begin{aligned}
 e_{xy}&=-m^{-1}(\mu_ke_x+\mu_he_y),\\
 z_{xy}&=P_{\perp,\phi}(2h_2k_2/v^3),\\
 \mathfrak g_{xy}
   &=-\partial_\phi^2\{
       ((|D_\theta|^{-2}p)_\theta\circ\Theta)\ell_k
       +((|D_\theta|^{-2}t)_\theta\circ\Theta)\ell_h\\
   &\hspace{26mm}
       +(f_{B,\theta\theta}\circ\Theta)\ell_h\ell_k
       +(f_{B,\theta}\circ\Theta)\Theta_{hk}\},\\
 \Theta_{hk}&=-m^{-1}(\mu_k\ell_h+\mu_h\ell_k).
 \end{aligned}
 \tag{RG.27}
$$

They retain both mean variations and the
actual phase convention. In particular a
raw pulled height direction is not replaced
by its good physical direction in these
formulas.

Here is one explicit sufficient tame
normalization for this parameter chain.
Use $E_s$ and $\mathcal T_n$ of OX, with
$B_s=B_s^R$, and set

$$
 \begin{gathered}
 \mathcal P_n=(1+D_{n+1})\,
          2^{120(n+50)}((n+50)!)^{20},\\
 L_0=16\mathcal P_0 .
 \end{gathered}
 \tag{RG.28}
$$

The exact formulas (RG.26)--(RG.27) imply

$$
 \begin{aligned}
 |\Pi'[x]|_{\mathfrak M_n},\
 |\Pi'[x]|_{\mathfrak A_n}
   &\le\mathcal P_n\{E_{n+3}(x)+B_{n+2}E_3(x)\},\\
 |\Pi''[x,y]|_{\mathfrak M_n}
   &\le\mathcal P_n\mathcal T_n(x,y),\\
 |\Pi'[x]|_{\mathfrak M_0},\
 |\Pi'[x]|_{\mathfrak A_0}
   &\le L_0E_3(x),\\
 |\Pi''[x,y]|_{\mathfrak M_0}
   &\le L_0E_3(x)E_3(y).
 \end{aligned}
 \tag{RG.29}
$$

We give the regularity and high-factor
bookkeeping explicitly. The $e$ column
has one extra derivative in
$\mathfrak M_n$; hence the raw cap
direction must indeed supply at least
one derivative beyond an $L^2$ input.
The normalized phase has one gained
derivative, and each physical height
potential has two. After the two
displayed derivatives in
$\mathfrak g_x,\mathfrak g_{xy}$, the
largest needed direction order is
below the displayed $n+3$ buffer.
Requesting an algebra norm instead
uses one additional Cauchy--Schwarz
derivative at this **endpoint**.
The highest possible background
derivative is then $n+2$.

All compositions in (RG.26)--(RG.27)
are endpoint functions, not radial
module elements. The real integer
composition rule FX.56--FX.57
therefore applies in its proved
space. Expand its complete chain
rule, keep both direction colours,
and apply the moment allocation
OX.19, or its equivalent interpolation
and weighted Young form, before taking
high bounds. Every term has either
one high direction or one high
background factor. The fixed low
bound is $B_3<10$.
The exact analytic height background
derivatives cost at most
$n!16^n2^{-60}$ after its two
normalized derivatives; no analytic
extension of $p$ or $t$ is used.

To make the coarse constants
transparent, the raw ratio, phase
and inverse-power factors have the
same convergent reciprocal
majorants as OX3. The additional
height chain has at most $(n+4)!$
coefficient mass and a further
factor $16^{n+4}(n+4)!$.
Their product, the first- and
second-direction terms in
(RG.26)--(RG.27), and the two
endpoint derivative embeddings
are all bounded by
$2^{100(n+50)}((n+50)!)^{16}$.
This is smaller than the explicit
$\mathcal P_n$ in (RG.28).
For the low statements in
(RG.29), the first two lines at
$n=0$ use only $B_2<10$, giving
factors below $11\mathcal P_0$
and $12\mathcal P_0$.
Thus $L_0$ is a genuine fixed
low constant, not a high-norm
quantity.

The mean $m$ and all zero-frequency
direction factors remain in this
calculation. Fourier zero modes
are omitted only at the exact
original primitives or nonmean
projections.

## RG6. Complete raw first and second tame derivatives

Define the explicit order constant

$$
 \mathcal C_n
 =2^{15}\mathcal P_n
 \{(1+L_0)\widehat J_n
              +(2L_0+L_0^2)\widehat K_n\}.
 \tag{RG.30}
$$

It depends solely on the order and
the fixed low domain. Then

$$
 \boxed{\displaystyle
 \begin{aligned}
 \|D\widehat{\mathcal G}[x]\|_{\mathfrak Z_n}
  &\le\mathcal C_n
          \{E_{n+3}(x)+B_{n+2}E_3(x)\},\\
 \|D^2\widehat{\mathcal G}[x,y]\|_{\mathfrak Z_n}
  &\le\mathcal C_n\,\mathcal T_n(x,y).
 \end{aligned}}
 \tag{RG.31}
$$

For the proof apply (RG.22) to
$D^2\mathcal G[\Pi'x,\Pi'y]$
and $D\mathcal G[\Pi''(x,y)]$.
Use (RG.29)'s low lines in every
low factor. The high moment
(RG.24) is bounded by
$\mathcal P_nB_{n+2}$.
The first chain-rule term costs
at most
$2^{15}\mathcal P_n
(2L_0+L_0^2)\widehat K_n
\mathcal T_n$;
the second costs at most
$2^{15}\mathcal P_n
(1+L_0)\widehat J_n
\mathcal T_n$.
The same second coefficient
dominates the first derivative.
This is exactly (RG.30).
No product of two high
background bounds appears.

The usual integral Taylor and
difference remainder estimates
follow as in OX.31--OX.32,
with $\mathcal C_n$ and the
actual raw output norm
$\mathfrak Z_n$, for segments
staying in the stated endpoint
and independent height domain.
All scalar outputs, the one
free physical translation
and both endpoint matching
units remain as stated in
RG3 and LG5.

Finally, this direct pulled-PDE
construction explains the
extra input regularity in
U.25: it is paid by the
$H^1$ angle module and by
the explicit parameter
chain (RG.26), not by an
unsupported same-space
composition claim.
Finite Fourier approximations
retain all the displayed
uniform inverse and module
bounds; the actual integral
equations and their unique
low solution give the
infinite-mode limit.

The companion
[rational combination](../scripts/fourfold_codazzi_raw_long_module_saved_bounds.py)
evaluates only14 new positive
combinations for this angle
module and its complete
mean charges. It evaluates
no native array, old
scientific target, Green
integral or new long
solution.
