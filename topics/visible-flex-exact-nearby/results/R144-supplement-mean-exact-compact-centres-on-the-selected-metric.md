# R144 supplement: exact-mean compact centres on the actual selected intrinsic metric

2026-11-27, visible-exact-astra-fb31ed6-20261127 / geometric_closure.

**Proved for the entire real interval $|\delta|\le10^{-10}$.**
At each original intrinsic metric $\nu=\nu_0+\delta$, there is
a unique compact density control $|\xi(\delta)|<1.75\,10^{-11}$
whose complete terminal mean has both the original waist and
outer values. Its state differs from the original raw state by
less than $4.739\,10^{-7}$ in the same-$\phi$ pair $A^0$ norm.
At the same metric it differs from the original repaired
selected-family state by less than $4.760\,10^{-7}$, and their
angular derivatives differ by less than $1.264\,10^{-6}$.
The actual signed metric moments also prove
$0.1275<\xi'(\delta)<0.166$ throughout this metric interval.

This puts an exact-mean centre on the actual selected metric,
with all original raw nonmean interfaces retained. These are
centres at different intrinsic metrics, not an isometric
flexible family for one metric. No nonmean inverse, phase
qualification or nonlinear existence theorem is transferred
merely by changing the centre.

## 1. Fixed shape coordinates and complete inputs

Use the raw $u,m,w=v-m$, the cutoff $\chi$ and the exact
compact root $\xi_*$ from
[SR](R144-supplement-sharp-compact-root-from-completed-forward-mean.md).
The same small complete CP record gives the following safe
strict bounds:

$$
 \begin{gathered}
 1.068<|m|<6,\quad V=\langle w^2\rangle<0.474,\quad
 q:=V/m^2<0.416,\\
 H_c:=H(9/50)<1.003,\qquad
 0.00452<\overline a<0.00462,\qquad
 0<\overline b<0.00172,
 \end{gathered}
 \tag{SM.1}
$$

where $H(r)=\exp\int_0^r2\beta\langle u^2\rangle$.
The lower bound for $|m|$ and the upper for $V$ imply the
displayed bound for $q$ by exact rational arithmetic.
At $\delta=0$ the already proved mean $m_*$ satisfies

$$
 |\xi_*|<\rho_s:=8\,10^{-13},\qquad
 \|m_*-m\|_\infty\le b_s:=2\,10^{-7},\qquad
 m_*(0)=-a_0,\quad m_*(R)=m(R).
 \tag{SM.2}
$$

In particular $|m_*|<6.001$. The old waist certificate gives
$a_0>1.06873282>1$.

Let $d=10^{-10}$ and $r_\xi=2\,10^{-8}$.
Hold the physical functions $u,m,w$ used in the density
coordinates fixed and put

$$
 K_\delta=e^{-\delta\chi}(K+\delta T\chi'),\qquad
 T=\frac{\beta}{2E_{\nu_0}},\qquad
 \rho_\delta=\frac{a'^2}{E_{\nu_0+\delta}}
             =\rho_0e^{-\delta\chi}.
 \tag{SM.3}
$$

The completed strict intrinsic result used in CD.3--CD.4
holds for $|\nu-\nu_0|\le10^{-8}$, so throughout the present
smaller interval and the compact window

$$
 \beta>0,\quad K_\delta<0,\quad
 \rho_\delta'=-2\beta a^2K_\delta>0.
 \tag{SM.4}
$$

At the compact right endpoint the metric bump vanishes and
the original rotational chart has $E-a'^2>0$. Hence
$\rho_\delta(9/50)=\rho_0(9/50)<1$; monotonicity gives
$0\le\rho_\delta<1$ throughout the compact window.
The same sign proof gives $a(r)\ge a_0>1$ and
$1\le H(r)\le H_c$ for $0\le r\le9/50$.
The function $H$ is independent of $\delta$ because $u,a$
and $\beta$ are held fixed.

The raw density is retained as $j_0=1+w/m$. For
$|\xi|\le r_\xi$ define

$$
 j_\xi=1+(1+\xi\chi)w/m,\qquad
 J_\xi=1+(1+\xi\chi)^2q.
 \tag{SM.5}
$$

## 2. A uniform positive terminal graph on the whole parameter rectangle

Define $Y_{\delta,\xi}$ by the complete piecewise equation

$$
 Y'=2\beta UY+2\beta a^2K_\delta J_\xi,\qquad
 Y(R)=a(R)^2/m(R)^2,\qquad [Y]_i=0.
 \tag{SM.6}
$$

The coefficients use every original raw piece. Ordinary
first-order variation of constants gives a unique continuous
$Y_{\delta,\xi}$, before any positivity assertion.
On $[9/50,R]$ it equals $Y_{0,\xi_*}$ identically, since
both the metric and the controlled density agree there.

On $[0,9/50]$, first vary $\delta$ with $\xi$ fixed.
Using $2\beta a^2\partial_\delta K_\delta
=(\rho_\delta\chi)'$, one obtains

$$
 |\partial_\delta Y_{\delta,\xi}(r)|
 \le H_c J_{\max}
       \int_{1/20}^{9/50}|(\rho_\delta\chi)'|\,dr,
 \qquad J_{\max}=1+(1+r_\xi)^2(0.416)<1.417.
 \tag{SM.7}
$$

For a terminal formula beginning inside the compact window,
the integration range is a subinterval, so the same bound
applies. The exact facts
$\int|\chi'|=2$, $0\le\chi\le1$ and (SM.4) give

$$
 \int|(\rho_\delta\chi)'|
 \le\int\rho_\delta'\chi+\int\rho_\delta|\chi'|<1+2=3.
 \tag{SM.8}
$$

At $\delta=0$, the density change is bounded using the
already completed positive moments, including for a partial
terminal integral:

$$
 |Y_{0,\xi}(r)-Y_{0,\xi_*}(r)|
 \le H_c\{\overline a|\xi-\xi_*|
                    +\overline b|\xi^2-\xi_*^2|\}.
 \tag{SM.9}
$$

This follows from the constant sign of $\beta K$ and the
nonnegative weights $\chi q/H,\chi^2q/H$. The partial
integral is bounded by the same complete moment; no full
upper is subtracted from another full upper.

Combining (SM.7)--(SM.9) gives, uniformly on the entire
rectangle and all $r\le9/50$,

$$
 \begin{aligned}
 |Y_{\delta,\xi}-Y_{0,\xi_*}|
 &<1.003\bigl[
 3(1.417)d+0.00462(r_\xi+\rho_s)
                +0.00172(r_\xi^2+\rho_s^2)\bigr]\\
 &<\epsilon_Y:=5.2\,10^{-10}.
 \end{aligned}
 \tag{SM.10}
$$

The base mean gives
$Y_{0,\xi_*}=a^2/m_*^2>a^2/(6.001)^2$ on that interval.
Since $a>1$ and

$$
 \frac1{6.001^2}-\epsilon_Y>\frac1{6.01^2},
 \tag{SM.11}
$$

one has $Y_{\delta,\xi}>a^2/(6.01)^2>0$ there.
On the remaining interval positivity is the already proved
base positivity. Consequently

$$
 m_{\delta,\xi}=-aY_{\delta,\xi}^{-1/2}
 \tag{SM.12}
$$

is a complete negative continuous scalar mean on the entire
rectangle. Its magnitude is less than $6.01$ wherever it
differs from the base mean.

The mean-value theorem in the positive $Y$ variable, with
$|\partial m/\partial Y|=|m|^3/(2a^2)$, gives

$$
 \|m_{\delta,\xi}-m_*\|_\infty
 <\frac{6.01^3}{2}\epsilon_Y<5.65\,10^{-8}.
 \tag{SM.13}
$$

In particular the complete raw-mean distance obeys

$$
 \|m_{\delta,\xi}-m\|_\infty
 <2\,10^{-7}+5.65\,10^{-8}<b_\nu:=2.57\,10^{-7}.
 \tag{SM.14}
$$

## 3. The exact waist equation has one root throughout the true metric interval

Put $F(\delta,\xi)=Y_{\delta,\xi}(0)-1$.
Then $F(0,\xi_*)=0$. Differentiation of (SM.6) gives

$$
 F_\xi(\delta,\xi)
       =2\int\rho_\delta'\chi(1+\xi\chi)q/H\,dr.
 \tag{SM.15}
$$

All integrals in this section cover the compact window.
Use
$e^d\le(1-d)^{-1}$, $e^{-d}\ge1-d$, and

$$
 \rho_\delta'
    =e^{-\delta\chi}(\rho_0'-\delta\rho_0\chi').
$$

The original compact moment is
$\overline a=2\int\rho_0'\chi q/H$.
Also $\int\rho_0|\chi'|\chi q/H\le2(0.416)$.
Therefore throughout $|\xi|\le r_\xi$,

$$
 F_\xi(\delta,\xi)\ge
 (1-r_\xi)
 \left[(1-d)(0.00452)
             -\frac{4d(0.416)}{1-d}\right]>0.0045.
 \tag{SM.16}
$$

This is a derivative lower bound for the full actual
waist equation, not a norm of a residual.

To bound $F(\delta,\xi_*)$, use the exact metric formula
of VM.8, now at the variable metric and fixed $\xi_*$:

$$
 F_\delta(\delta,\xi_*)=
             -\int(\rho_\delta\chi)'J_{\xi_*}/H\,dr.
 \tag{SM.17}
$$

The constant part integrates to
$-\int2\beta U\rho_\delta\chi/H$ and has absolute value
at most $1-H_c^{-1}<0.003$.
For the variance part, retain $\rho_\delta'\ge0$,
use the completed $\overline a$ and bound the
sign-changing derivative separately. This gives

$$
 \begin{aligned}
 |F_\delta(\delta,\xi_*)|
 &\le0.003+(1+\rho_s)^2
 \left[
 \frac{0.00462/2+2d(0.416)}{1-d}+2(0.416)
 \right]\\
 &<0.838.
 \end{aligned}
 \tag{SM.18}
$$

Hence $|F(\delta,\xi_*)|<0.838d$.
The strict rational inequality

$$
              0.0045(r_\xi-\rho_s)>0.838d
 \tag{SM.19}
$$

and (SM.16) imply
$F(\delta,-r_\xi)<0<F(\delta,r_\xi)$.
The intermediate value theorem and strict monotonicity
prove exactly one root

$$
               \xi(\delta)\in(-2\,10^{-8},2\,10^{-8})
                    \quad (|\delta|\le10^{-10}).
 \tag{SM.20}
$$

The coefficients are real analytic in the two scalar
parameters; the fixed original piecewise spatial functions
do not obstruct differentiation under these finite
bounded integrals. Since (SM.16) is uniform, the implicit
function theorem gives a real analytic $\xi(\delta)$.
It is the old root at $\delta=0$ by uniqueness.

### The actual signed metric moments sharpen the same whole interval

The complete new
[actual VM result](R144-supplement-actual-negative-metric-waist-derivative-and-positive-density-compensation.md),
run45888851105/1, gives

$$
 -0.000745924<F_\delta(0,\xi_*)<-0.000589680,\quad
 |M_1|<0.001135,\quad |M_2|<0.001108.
 \tag{SM.20a}
$$

These are signed values at the actual centre. To transfer
them to the whole rectangle, first hold $\delta=0$ and
use the exact quadratic dependence in VM.12--VM.13:

$$
 |F_\delta(0,\xi)-F_\delta(0,\xi_*)|
 \le2(r_\xi+\rho_s)(0.001135)
                  +(r_\xi^2+\rho_s^2)(0.001108).
 \tag{SM.20b}
$$

For the metric change itself, the exact identity is

$$
 (\rho_\delta\chi)'-(\rho_0\chi)'
 =(e^{-\delta\chi}-1)(\rho_0\chi)'
             -\delta e^{-\delta\chi}\rho_0\chi\chi'.
$$

The first factor has absolute value at most $d/(1-d)$.
By (SM.8), the integral of $|(\rho_0\chi)'|$ is below 3.
Also $\int\chi|\chi'|=1$. Therefore

$$
 |F_\delta(\delta,\xi)-F_\delta(0,\xi)|
              <\frac{4(1.417)d}{1-d}.
 \tag{SM.20c}
$$

The sum of the right sides of (SM.20b)--(SM.20c) is
less than $6.2\,10^{-10}$. It follows, throughout the
same complete rectangle, that

$$
             -0.000746<F_\delta(\delta,\xi)<-0.0005896.
 \tag{SM.20d}
$$

The companion upper bound for (SM.15) is

$$
 F_\xi(\delta,\xi)
 \le\frac{1+r_\xi}{1-d}
                (0.00462+4d(0.416))<0.004621.
 \tag{SM.20e}
$$

Combining (SM.16), (SM.20d) and (SM.20e) at the unique
root proves the full signed compensation derivative

$$
 \boxed{\quad
 0.1275<\xi'(\delta)
          =-\frac{F_\delta(\delta,\xi(\delta))}
                   {F_\xi(\delta,\xi(\delta))}<0.166 .
 \quad}
 \tag{SM.20f}
$$

Consequently the already constructed whole root curve
satisfies

$$
 |\xi(\delta)|<\rho_s+0.166d<r_s:=1.75\,10^{-11}.
 \tag{SM.20g}
$$

Returning to the same complete $Y$ comparison (SM.10)
with this smaller control radius gives

$$
 \begin{aligned}
 \|Y_{\delta,\xi(\delta)}-Y_{0,\xi_*}\|_\infty
 &<1.003\bigl[
 3(1.417)d+0.00462(r_s+\rho_s)
                       +0.00172(r_s^2+\rho_s^2)\bigr]\\
 &<4.265\,10^{-10}.
 \end{aligned}
 \tag{SM.20h}
$$

The same positive denominator proof and mean-value
estimate then give

$$
 \|m_{\delta,\xi(\delta)}-m_*\|_\infty<4.63\,10^{-8},
 \qquad
 \|m_{\delta,\xi(\delta)}-m\|_\infty<b_{\nu,s}:=2.464\,10^{-7}.
 \tag{SM.20i}
$$

No earlier input or completed numerical target is
re-evaluated for this refinement. It uses the actual
signed moment ball and the displayed analytic difference.

## 4. Exact endpoint means, compact change and density positivity

Set

$$
 m_\delta=m_{\delta,\xi(\delta)},\qquad
 \widetilde Q_\delta=(u,m_\delta j_{\xi(\delta)}).
 \tag{SM.21}
$$

The defining waist equation and terminal condition give
exactly

$$
 m_\delta(0)=-a_0,\qquad m_\delta(R)=m(R).
 \tag{SM.22}
$$

For $r\le1/20$, all metrics and densities in (SM.21)
agree with the base ones, and their $Y$ equations have
the same initial value $Y(0)=1$. For $r\ge9/50$ they
have the same terminal equation and value.
Uniqueness on both subintervals therefore gives

$$
 \widetilde Q_\delta=Q_* \quad
       \text{on }[0,1/20]\cup[9/50,R].
 \tag{SM.23}
$$

This is equality of the fields, not just equality of
their endpoint means. All original piecewise transitions
inside the compact window remain. The scalar mean is
continuous; no continuity of the remaining raw nonmean
state is inferred.

The old raw gap gives $|v|>0.09$, and (SM.1) gives
$j_0=v/m>0.09/6=0.015$.
The complete old LC coefficient bound is
$\|w\|_{A^0}<0.986$.
Therefore

$$
 j_{\xi(\delta)}
 \ge j_0-r_\xi\|w\|_{A^0}/1.068
 >0.015-\frac{2\,10^{-8}(0.986)}{1.068}>0.01499.
 \tag{SM.24}
$$

Thus the density chart stays positive on the whole
metric interval. Its angular mean remains exactly one.
The constructed state satisfies the complete scalar
mean equation at its own metric $\nu_0+\delta$.

## 5. Same-circle state and angular-derivative bounds

The old LC density bound $\|j_\xi\|_{A^0}<1.923$ applies
to the present smaller control range. It only uses the
same raw $w/m$ and the cutoff; no metric transfer is
needed for this particular algebraic density bound.
The identity

$$
 m_\delta j_\xi-v
                =(m_\delta-m)j_\xi+\xi\chi w
 \tag{SM.25}
$$

and the actual sharpened bounds (SM.20g)--(SM.20i) give

$$
 \|\widetilde Q_\delta-Q_{\rm raw}\|_{A^0,\mathrm{pair}}
 <1.923(2.464\,10^{-7})+0.986(1.75\,10^{-11})
 <4.739\,10^{-7}.
 \tag{SM.26}
$$

The same bound holds in componentwise $C^0_{r,\phi}$.
The odd component is unchanged. The norm and angular
coordinate are the original raw moving ones.

For angular derivatives use the exact differentiated
coefficient, rather than paying the maximum frequency:

$$
 \partial_\phi(m_\delta j_\xi-v)
 =\left[\frac{m_\delta-m}{m}(1+\xi\chi)
                     +\xi\chi\right]w_\phi .
 \tag{SM.27}
$$

The old complete raw pair derivative bound
$5.437241<5.438$, stated in D.6, bounds
$\|w_\phi\|_{A^0}$ as well. Thus

$$
 \|\partial_\phi(\widetilde Q_\delta-Q_{\rm raw})\|_{A^0,\mathrm{pair}}
 <5.438\left[\frac{2.464\,10^{-7}}{1.068}
                      (1+1.75\,10^{-11})+1.75\,10^{-11}\right]
 <1.255\,10^{-6}.
 \tag{SM.28}
$$

Now compare with the original repaired family
$Q_\delta=Q_0+\delta Z$, at the **same**
intrinsic metric $\nu_0+\delta$.
The complete bounds already used in
[SB](R144-supplement-complete-same-phi-bridge-to-selected-reference.md)
and
[D.1--D.6](R133-supplement-exact-selected-parameter-core-differences-and-finite193-transfer.md)
are

$$
 \|Q_0-Q_{\rm raw}\|_{A^0,\mathrm{pair}}<3.861\,10^{-18},
 \quad \|Z\|_{A^0,\mathrm{pair}}<19,
$$
$$
 \|(Q_0-Q_{\rm raw})_\phi\|_{A^0,\mathrm{pair}}<1.970\,10^{-17},
 \quad \|Z_\phi\|_{A^0,\mathrm{pair}}<83.
 \tag{SM.29}
$$

Combining these complete bounds gives, for all $|\delta|\le d$,

$$
 \boxed{\quad
 \|\widetilde Q_\delta-Q_\delta\|_{A^0,\mathrm{pair}}
       <4.760\,10^{-7},\qquad
 \|(\widetilde Q_\delta-Q_\delta)_\phi\|_{A^0,\mathrm{pair}}
       <1.264\,10^{-6}.
 \quad}
 \tag{SM.30}
$$

In particular the actual selected $\delta_*$ belongs to
this interval, so $\widetilde Q_{\delta_*}$ is an
exact-mean centre on the actual selected metric.

## 6. What the construction changes in the remaining problem

At $\delta_*$ there is no longer an intrinsic metric
mismatch between this centre and $Q_{\delta_*}$.
Their state differential still differs. Any inverse
transfer must pay the full first-order state difference,
including the mean principal coefficient and mean-rank
term, with the actual source and trace spaces.
Equation (SM.30) supplies state and angular derivative
inputs for that task; it is not itself an inverse.

The full nonmean residual at the new metric must likewise
retain the genuine metric contribution. An old
fixed-$\nu_0$ compact residual bound is not silently
assigned to $\widetilde Q_{\delta_*}$.
The true phase, cap, height and global nonlinear matching
retain their original qualifications.

The scalar construction uses only old complete inputs and
the displayed new analytic estimates. Its rational
comparisons are implemented in
[the saved-bound checker](../scripts/fourfold_codazzi_selected_metric_mean_saved_bounds.py).
It does not rerun a scientific native or claim a
fixed-metric flexible family.
