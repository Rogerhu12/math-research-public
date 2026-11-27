# R144 WH: complete passive world-height Hessian with independent ports

2026-11-27, visible-exact-astra-fb31ed6-20261127.

This proves a quantitative second derivative of the entire passive
world-frame and position reconstruction on $[0,R]$, $R=25/8$, at the
full-tail compact backgrounds. The moving position has an actual $L^2$
Hessian. Its height in the **fixed physical angle** has an actual
$H^{-3}$ Hessian, including every physical Fourier mode and its mean.
The independent outer frame, outer position and waist trace are all
inputs. No radial $L^2$ norm is used to manufacture a trace.

The constants below are deliberately uniform. They pay this complete
residual map without solving its homogeneous boundary response or
claiming the stronger high-order height inverse. The same world anchor,
position periodicity, cap matching and full Schur conditions remain.

## WH1. Same real background and intrinsic constants

Keep the fixed $\eta_0$, the entire $|\nu-\nu_0|\le10^{-10}$ and
$Q=\widetilde Q_\nu+q$ of
[SM](R144-supplement-mean-exact-compact-centres-on-the-selected-metric.md),
with the original two-component full-tail $A^3$ radius $10^{-6}$.
The background is not assumed to solve the nonmean equation. Write
$Q=(u,v)$, $m=\Pi v$, $n=1/m$, and $I=\partial_\phi^{-1}P_{\ne0}$.
The completed SM and
[TH](R144-supplement-complete-low-norm-tame-Hessian-and-mean-preserving-smoothing.md)
bounds imply

$$
 m<-1,\quad \|Q\|_{A^0}<7,\quad
 |\beta|\max(1,|K|)<6,\quad
 |\gamma|,|\gamma K|<14.                         \tag{WH.1}
$$

The pair Wiener norm in (WH.1) uses Euclidean coefficient norms.
In particular the sum of the squares of the two component Wiener
norms is at most49. Directions below instead use component sums,
so no unrecorded pair conversion is needed.

Also throughout the whole interval,

$$
 |\beta/\gamma|<2.                                  \tag{WH.2}
$$

Here are the domains behind this inequality. On the completed strict
interval, [SJA](R133-supplement-actual-complete-strict-radial-first-symbol-defect.md)
gives $|\beta|<1/4$ and $\gamma>1$. The remaining negative sliver and
the actual root germ use the intrinsic $\gamma>1.119607700127$ of
[the original full root budget](R133-supplement-actual-full-frequency-moving-root-budget.md)
and $|\beta|<9/5$ on the same root rectangle in
[P](R133-supplement-current-moving-positive-root-Riccati-and-full-head.md).
The compact metric bump vanishes on that entire germ. On the positive
body the original complete coefficient gate retains
$\mathscr R=(\gamma^2-\beta^2)/a^2>0$, hence $|\beta|<\gamma$;
the same actual rotational gap is part of P on its root collar.
These are the original intrinsic gates, independent of the unknown
state. No negative-side lower bound is extended to an uncovered
positive interval.

Let $A=2^{20}$. A convenient complete radius bound is

$$
                         0<a(r)<A.                   \tag{WH.3}
$$

Indeed the completed
[two-sided intrinsic collar](R133-supplement-actual-selected-parameter-core-scalar-fees-and-collar-jets.md)
gives $a(9/10)<1$. TH gives $|\beta|=|a'/a|<6$ on the
whole $[0,R]$. Thus $a(r)<e^{267/20}<e^{27/2}<(5/3)^{27}<2^{20}$.
For the elementary exponential step, the factorial series gives
$e<65/24+1/100<11/4<25/9$; the final comparison is exact rational
arithmetic. This bound does not need a new evaluation of the radius.

TH's true parameter derivatives, with $w$ the original compact bump,
give

$$
\begin{gathered}
 |\beta K_\nu|<4,\quad |\beta K_{\nu\nu}|<8,\quad
 |(\gamma K)_\nu|,|(\gamma K)_{\nu\nu}|<24,\\
 |\gamma_\nu|<7,\quad |\gamma_{\nu\nu}|<7/2,\quad
 |(\beta/\gamma)_\nu|<1,\quad
 |(\beta/\gamma)_{\nu\nu}|<1/2 .                  \tag{WH.4}
\end{gathered}
$$

The last two follow from the exact factor $e^{-(\nu-\nu_0)w/2}$.
All parameter derivatives vanish outside $[1/20,9/50]$; $a$ and
$\beta$ have zero parameter derivative. The bounds deliberately
allow the whole interval when taking a norm, without deleting
the genuine direct or mixed parameter terms.

## WH2. Exact off-constraint passive map and its input norms

Use precisely the connection of
[the full moving-frame identity](R133-supplement-moving-frame-with-complete-residual-and-mean.md)
and [PH.18](R147-supplement-exact-nonlocal-phase-and-height-parameter-ports.md):

$$
\begin{gathered}
 d=-\beta I(u^2+Kv^2),\quad b=\beta/\gamma,\quad
 p=bdvn-\beta u,\\
 k=a((\gamma K)v+dun),\quad t=adn,\quad
 M=\begin{pmatrix}0&-p&-k\\p&0&-t\\k&t&0\end{pmatrix},\\
 c=(a\gamma,a(dvn-\gamma u),0)^t,\qquad
 O_r=OM,\quad F_r=Oc,\quad O(R)=O_R,\quad F(R)=F_R.
                                                        \tag{WH.5}
\end{gathered}
$$

Every real $M$ is skew, even away from a PDE solution. Its right
propagators are exactly orthogonal. At physical anchors $O_R$ is
the supplied orthogonal world frame; it is never reset to $Id$.
For derivatives, (WH.5) has an exact affine extension in the
matrix input $O_R$. We use the convex domain
$\|O_R\|_{L^\infty,op}\le1$, which contains the convex hull of
all physical anchors. Consequently $\|O(r)\|_{op}\le1$ on that
whole domain. The independently supplied position obeys the
generous low-norm bound $\|F_R\|_\infty\le A$.

This affine extension is a device for estimating the actual map;
it does not replace the original orthogonality or cap equations.
A consumer composing $O_R,F_R$ with a nonlinear cap graph must
also retain that graph's own derivatives and boundary residuals.

For a direction $x=(h,\kappa,U,Y,h_w)$, $\kappa$ is the actual
metric increment, $U,Y$ are the independent terminal matrix and
position increments, and $h_w$ is the actual waist state trace.
On smooth fields $h_w=h(0)$; its norm is still charged separately.
Define

$$
\begin{aligned}
 E_r(x)&=\|h_1(r)\|_2+\|h_2(r)\|_2+100|\kappa|,\\
 H_r(x)&=\|h_1(r)\|_{H^1}+\|h_2(r)\|_{H^1}+100|\kappa|,\\
 \mathcal E(x)&=\|h\|_{L^2_r(L^2\oplus_1L^2)}
       +100\sqrt R|\kappa|+\|U\|_2+\|Y\|_2+\|h_w\|_{2,1},\\
 \mathcal H(x)&=\|h\|_{L^2_r(H^1\oplus_1H^1)}
       +100\sqrt R|\kappa|+\|U\|_{H^1}
                    +\|Y\|_{H^1}+\|h_w\|_{H^1,1},\\
 \mathcal S(x,y)&=\mathcal H(x)\mathcal E(y)
                          +\mathcal H(y)\mathcal E(x).
                                                        \tag{WH.6}
\end{aligned}
$$

Matrix directions use Frobenius Sobolev norms; output matrix
estimates may use the smaller pointwise operator norm. The angular
measure is normalized on $2\pi$; on the original fourfold scalar
fields this is exactly the old normalized $\pi/2$ measure.
World-vector and frame inputs may have their genuine full $2\pi$
dependence. The embedding constant2 suffices there; the original
fourfold scalar embedding constant $11/10$ is used only for $h$.
No trace, Fourier sign, physical mean or terminal port is omitted.

## WH3. Complete mixed derivatives of the actual connection

All statements in this section are pointwise in $r$.
For two directions put $S_r=H_r(x)E_r(y)+H_r(y)E_r(x)$.
The exact primitive has norms
$I:L^2\to L^2\le1/4$, $I:L^2\to L^\infty<1/2$ and
$I:A^0\to A^0\le1/4$. These include the actual zero-mode
projection; the mean of $h_2$ is not part of that projection.

Differentiating the full $d$, including its true parameter, gives

$$
\begin{aligned}
 d_x={}&-2\beta I(uh_1+Kvh_2)-\kappa\beta K_\nu I(v^2),\\
 d_{xy}={}&-2\beta I(h_1k_1+Kh_2k_2)
 -2\beta K_\nu I(v(\lambda h_2+\kappa k_2))
 -\kappa\lambda\beta K_{\nu\nu}I(v^2).
                                                        \tag{WH.7}
\end{aligned}
$$

Consequently

$$
\begin{gathered}
 \|d\|_\infty<74,\quad \|d_x\|_2\le21E_r(x),\quad
 \|d_x\|_\infty\le42E_r(x),\quad
 \|d_{xy}\|_2\le4S_r,\\
 |n|<1,\quad |n_x|\le E_r(x),\quad |n_{xy}|\le S_r.
                                                        \tag{WH.8}
\end{gathered}
$$

For example $\|d\|_{A^0}\le6\cdot49/4=73.5$.
The state-state term in (WH.7) is at most
$(33/20)S_r$ by the fourfold $H^1$ embedding, the two mixed
parameter terms cost at most $(7/100)S_r$, and the last costs
at most $(49/10000)S_r$. Their sum is less than4.
The reciprocal formulas are $n_x=-\Pi h_2/m^2$ and
$n_{xy}=2(\Pi h_2)(\Pi k_2)/m^3$, with both actual means.

Here is a full product ledger. The columns bound the value,
the first derivative in $L^2/E_r$, the first derivative in
$L^\infty/H_r$, and the mixed second derivative in $L^2/S_r$.
In the row for $d$, its stronger $L^\infty/E_r$ bound is used
when useful.

| Complete expression | Value | First $L^2$ | First $L^\infty$ | Second $L^2$ |
|---|---:|---:|---:|---:|
| $dvn$ or $dun$ | $518$ | $739$ | $893.4$ | $800$ |
| $dn$ | $74$ | $95$ | $116$ | $100$ |
| $p$ | $1078$ | $1490$ | $1800$ | $1610$ |
| $k/a$ | $616$ | $755$ | $911$ | $801$ |
| $t/a$ | $74$ | $95$ | $116$ | $100$ |

For clarity the entire second derivative of $dvn$ is

$$
 d_{xy}vn+dv n_{xy}
 +(d_xk_2+d_yh_2)n
 +(d_xn_y+d_yn_x)v
 +d(h_2n_y+k_2n_x).                                  \tag{WH.9}
$$

The five complete groups cost respectively
$28,518,23.1,147,74$ times $S_r$, whose sum is below800.
The $dn$ row costs $4+74+21=99<100$.
For the $p$ row, $b_x$ costs $1/100$ and $b_{xy}$ costs
$1/40000$ in the weighted direction norms. Its second bound
is $2(800)+(739/100)+(518/40000)<1610$.
For $k/a$, the complete additional $(\gamma K)v$ second bound
is $24/100+7(24/20000)<1$.
These calculations include all placements of the two directions;
there is no finite support assumption on either one.

Since the operator norm of a three-dimensional skew matrix is
$\sqrt{p^2+k^2+t^2}$, the sum of its three absolute coefficients
is a valid complete majorant. Applying the ledger to (WH.5) gives

$$
\begin{array}{lll}
 \|M_x\|_2\le2340A E_r(x),&
 \|M_x\|_\infty\le2900A H_r(x),&
 \|M_{xy}\|_2\le2600A S_r,\\
 \|c\|_\infty\le630A,&
 \|c_x\|_2\le754A E_r(x),&
 \|c_{xy}\|_2\le801A S_r .
\end{array}                                             \tag{WH.10}
$$

The $c_x$ coefficient is bounded by
$7/100+739+14+7(7/100)=753.56$.
Its complete second coefficient is at most
$800+7/100+8(7/40000)<801$.
All real metric second derivatives have been included before
these constants are rounded upward. An arbitrary actual mean
direction is allowed in every row.

## WH4. Orthogonal propagation pays the whole frame and position

The exact first and second variation equations, with their original
terminal data, are

$$
\begin{aligned}
 (O_x)_r&=O_xM+OM_x, &O_x(R)&=U,\\
 (O_{xy})_r&=O_{xy}M+O_xM_y+O_yM_x+OM_{xy},
       &O_{xy}(R)&=0,\\
 (F_x)_r&=O_xc+Oc_x, &F_x(R)&=Y,\\
 (F_{xy})_r&=O_{xy}c+O_xc_y+O_yc_x+Oc_{xy},
       &F_{xy}(R)&=0.
                                                        \tag{WH.11}
\end{aligned}
$$

The zero second terminal data are the exact affine extension in
the independent ports, not a claim that their first variations
vanish. Derivatives of a supplied nonlinear anchor map are
additional chain-rule inputs, as specified in WH2.

Orthogonal right propagation, Minkowski and radial Cauchy--Schwarz,
with $\sqrt R<9/5$, give

$$
 \sup_r\|O_x(r)\|_2\le4213A\mathcal E(x),\qquad
 \sup_r\|O_x(r)\|_\infty\le5222A\mathcal H(x).
                                                        \tag{WH.12}
$$

For the second equation of (WH.11), the two cross terms have
joint coefficient $(5222A)(2340A)(9/5)$ multiplying
$\mathcal S$. The last has coefficient $2600A$.
Thus the complete second frame bound is

$$
 \boxed{\sup_r\|O_{xy}(r)\|_2
                 <22000000 A^2\mathcal S(x,y).}        \tag{WH.13}
$$

This has no factor $e^{\int\|M\|}$: the homogeneous propagator
in the exact equation is orthogonal. No commutativity between
different $M(r)$ is assumed.

The last two equations of (WH.11) then give

$$
\begin{gathered}
 \sup_r\|F_x(r)\|_2<9000000 A^2\mathcal E(x),\\
 \boxed{\sup_r\|F_{xy}(r)\|_2
                   <44000000000 A^3\mathcal S(x,y).}\tag{WH.14}
\end{gathered}
$$

The full positive expressions used before rounding are

$$
\begin{aligned}
 C_{F,1}&=1+R(630A)(4213A)+(754A)(9/5),\\
 C_{F,2}&=R(630A)(22000000A^2)
                 +(5222A)(754A)(9/5)+801A.             \tag{WH.15}
\end{aligned}
$$

Both directions are already present in $\mathcal S$; no second
factor two is concealed in the middle term. Also
$\sup_r\|F(r)\|_\infty\le A+R(630A)$.

These are complete ordinary $dr$ estimates through the original
radial interfaces. The passive reconstruction is transmitted
continuously there, using each genuine one-sided coefficient.
Discontinuous background coefficients are not new position or
frame jumps. If an external consumer instead prescribes actual
frame or position impulses, their independent whole values and
variations must be inserted in (WH.11); they are not charged a
radial length or silently set to zero.

## WH5. Exact fixed-physical-angle height, including its mean

At the waist use the actual trace $v_w$, its actual mean $m_w$ and

$$
 \Theta(\phi)=\phi+Iv_w/m_w,\qquad J=\Theta_\phi=v_w/m_w.
                                                        \tag{WH.16}
$$

The original complete
[waist chart](R133-supplement-final-waist-amplitude-coordinate-and-mean-Schur.md)
gives $-v>0.0833357128$ throughout its radius-$10^{-6}$
full-tail neighbourhood. SM's complete compact-to-raw difference
and the present perturbation put the waist within $2\cdot10^{-6}$
of that same raw trace. Subtracting only the extra $10^{-6}$
therefore gives $-v_w>1/13$; (WH.1) gives $-m_w>1$ and
$|m_w|<7$. In particular

$$
                   1/100<J<7.                         \tag{WH.17}
$$

The lift is a genuine degree-one circle diffeomorphism, with the
original constant and mean convention. No new phase normalization
is made. Let $\Phi=\Theta^{-1}$ and fix the original world vertical
unit covector $e_z$. The physical height is

$$
 Z_{\rm phys}(\theta)=e_z\cdot F(0,\Phi(\theta)).
                                                        \tag{WH.18}
$$

For every fixed real $2\pi$-periodic test $\zeta\in H^3$, the
exact change of variables, with normalized measures, is

$$
 \langle\zeta,Z_{\rm phys}\rangle_\theta
 =\langle W_\zeta,e_z\cdot F(0)\rangle_\phi,
 \qquad W_\zeta=\zeta(\Theta)J.                       \tag{WH.19}
$$

It remains true off the PDE constraints. Thus it includes the
original actual $F_\phi=O(c_\phi+P)$ and its true defect whenever
one chooses to integrate by parts. We do not replace this derivative
by $Oc_\phi$ or set the angular connection defect to zero.

Write $\mu=\Pi h_{w,2}$, $\lambda=\Pi k_{w,2}$. The entire
coordinate variations are

$$
\begin{aligned}
 \Theta_x&=Ih_{w,2}/m_w-Iv_w\mu/m_w^2,\\
 \Theta_{xy}&=-(Ih_{w,2}\lambda+Ik_{w,2}\mu)/m_w^2
                         +2Iv_w\mu\lambda/m_w^3,\\
 J_x&=h_{w,2}/m_w-v_w\mu/m_w^2,\\
 J_{xy}&=-(h_{w,2}\lambda+k_{w,2}\mu)/m_w^2
                         +2v_w\mu\lambda/m_w^3 .       \tag{WH.20}
\end{aligned}
$$

For $e_x=\|h_w\|_{2,1}$ and $H_x=\|h_w\|_{H^1,1}$,
the primitive and reciprocal bounds give

$$
\begin{gathered}
 \|\Theta_x\|_\infty\le(9/4)e_x,\quad
 \|\Theta_{xy}\|_\infty\le(9/2)e_xe_y,\\
 \|J_x\|_2\le8e_x,\quad \|J_x\|_\infty\le9H_x,\quad
 \|J_{xy}\|_2\le16e_xe_y.                            \tag{WH.21}
\end{gathered}
$$

For example $\|Iv_w\|_\infty\le7/4$ and
$\|Ih_{w,2}\|_\infty\le e_x/2$. These are bounds on the
complete primitive; they do not assume $\mu=0$.

On the full $2\pi$ circle,
$\|\zeta^{(j)}\|_\infty<2\|\zeta\|_{H^3}$ for $j=0,1,2$.
Indeed $\sum_{k\in\mathbb Z}(1+k^2)^{-1}<2+\pi/2<4$,
using the decreasing-integrand bound for $|k|\ge2$.
Differentiate (WH.19)'s weight exactly:

$$
\begin{aligned}
 (W_\zeta)_x={}&\zeta'(\Theta)\Theta_xJ+\zeta(\Theta)J_x,\\
 (W_\zeta)_{xy}={}&\zeta''(\Theta)\Theta_x\Theta_yJ
 +\zeta'(\Theta)\Theta_{xy}J\\
 &+\zeta'(\Theta)(\Theta_xJ_y+\Theta_yJ_x)
 +\zeta(\Theta)J_{xy}.                              \tag{WH.22}
\end{aligned}
$$

All four second-derivative groups are retained. They give

$$
\begin{gathered}
 \|W_\zeta\|_\infty\le14\|\zeta\|_{H^3},\qquad
 \|(W_\zeta)_x\|_2<48e_x\|\zeta\|_{H^3},\\
 \|(W_\zeta)_{xy}\|_2
       <120(H_xe_y+H_ye_x)\|\zeta\|_{H^3}.          \tag{WH.23}
\end{gathered}
$$

Before the last rounding the complete coefficient of $e_xe_y$
is $2[7(9/4)^2+7(9/2)+2(9/4)8+16]=237.875$.
Since $H_xe_y+H_ye_x\ge2e_xe_y$, (WH.23) follows.
There is no assumption about orthogonality of these four errors.

The Hessian of the physical functional is consequently

$$
\begin{aligned}
 D^2\langle\zeta,Z_{\rm phys}\rangle[x,y]
 ={}&\langle W_\zeta,e_z\cdot F_{xy}(0)\rangle\\
 &+\langle(W_\zeta)_x,e_z\cdot F_y(0)\rangle
  +\langle(W_\zeta)_y,e_z\cdot F_x(0)\rangle\\
 &+\langle(W_\zeta)_{xy},e_z\cdot F(0)\rangle .       \tag{WH.24}
\end{aligned}
$$

Use (WH.14), (WH.23) and the complete base position bound.
The sufficient coefficient of $\mathcal S\|\zeta\|_{H^3}$ is

$$
 C_H(A)=14(44000000000 A^3)+48(9000000A^2)
                           +120A(1+630R)<2^{100}.      \tag{WH.25}
$$

Thus the entire actual physical height map satisfies

$$
 \boxed{\|D^2Z_{\rm phys}[x,y]\|_{H^{-3}}
                         \le2^{100}\mathcal S(x,y).}  \tag{WH.26}
$$

The dual norm covers **all** tests, not a truncated observation.
In particular $\zeta=1$ gives the physical height mean and
$\zeta=\cos(4j\theta)$ gives every original cosine row, with
its actual $H^3$ norm. No such row vanishes merely because the
strict parameter state vanishes above $9/50$.

## WH6. Remainders, exact domains and remaining interfaces

The estimates hold on the larger convex real domain specified by
(WH.1), (WH.17), the parameter interval and the terminal bounds,
which contains the declared compact backgrounds and their line
segments. Smooth directions first prove (WH.7)--(WH.26).
Minkowski, the displayed product bounds and density then give the
same bilinear estimates in the direction norms (WH.6).
This is a tame derivative statement at bounded real backgrounds,
not a nonlinear existence theorem on an arbitrary radial $L^2$ ball.

For any admitted increment $z$, Taylor's integral formula gives

$$
\begin{aligned}
 \|Z_{\rm phys}(x+z)-Z_{\rm phys}(x)-DZ_{\rm phys}(x)z\|_{H^{-3}}
   &\le2^{100}\mathcal H(z)\mathcal E(z),\\
 \|(DZ_{\rm phys}(x+z)-DZ_{\rm phys}(x))h\|_{H^{-3}}
   &\le2^{100}[\mathcal H(z)\mathcal E(h)
                        +\mathcal H(h)\mathcal E(z)].  \tag{WH.27}
\end{aligned}
$$

The two scalar means in the original state equations have never
been solved or discarded in this calculation. The terminal inputs
are their **actual moving-coordinate** world frame and position.
If an upstream graph provides them at fixed physical outer angle,
its true coordinate map and both derivatives must be composed as
well. The independent waist trace in (WH.6) is likewise not bounded
by the ordinary radial source norm alone.

The reconstruction has one common supplied world anchor throughout.
It requires neither flatness nor exact angular compatibility to
define its passive value. Turning that value into a closed isometric
embedding still requires the original complete PDE, angular defects,
position periods, means, physical boundary, waist reflection and
regular-cap conditions. The stronger high-order height tame estimates
and the complete bordered inverse are not asserted by (WH.26).

The accompanying
[saved-bound reader](../scripts/fourfold_codazzi_passive_world_height_hessian_saved_bounds.py)
completed 34 new exact rational comparisons of the cited complete inputs.
It calls no original
scientific producer, frame integrator, Fourier target or native-row
evaluation. In particular this proof does not claim to have restored
an unavailable signed world-frame carrier.


