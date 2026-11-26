# R144 supplement: compact density control and the exact quadratic outer-mean equation

2026-11-26, visible-exact-astra-198c63d-20261126 / global_geometry.

**Proved analytic construction, with explicit remaining numerical gates.**
One compact change of the material density gives an exact quadratic equation
for the outer mean after the full mean has been eliminated. A uniform
small-root gate is given below. At such a root the entire outer moving
state and its physical angular chart return to the original values.
Whole-domain positivity, closeness, every changed nonmean residual,
all raw interfaces and the true design phase remain explicit obligations.

This is a possible new centre construction if the actual fixed-density
retraction requires an outer-mean correction. It is not another evaluation
of a completed integral. No new actual-run value or successful numerical gate is
asserted here.

## CD1. Fixed object, original equations and an admissible compact window

Fix the original metric and its actual parameter, and write

$$
 g=E_\nu(r)\,dr^2+a(r)^2\,d\theta^2,\qquad
 \beta=a'/a,\qquad \gamma=\sqrt{E_\nu}/a.
$$

For the actual approximate input let

$$
 m=\langle v\rangle<0,\quad j=v/m>0,\quad z=j-1,\quad
 U=\langle u^2\rangle,\quad
 V=\langle(v-m)^2\rangle,\quad
 J=1+V/m^2.
 \tag{CD.1}
$$

Means are normalized on the original fourfold moving circle. The
physical frequency of mode $k$ is $4k$, and every radial integral uses
the actual measure $dr$. The scalar $V$ in this note is not the name of
a Fourier coefficient array.

The complete original moving residuals and the full mean are those of
[MV.1--5](R144-supplement-exact-nonlinear-mean-elimination-and-retraction.md):

$$
 \begin{aligned}
 u_r&=d u_\phi+\gamma\kappa j_\phi
          -\beta u(1+u^2+\kappa j^2)+R_u,\\
 j_r&=(dj-\gamma u)_\phi+F_j,\qquad
 F_j=(R_v-jR_0)/m,\\
 R_0&=\langle R_v\rangle,\qquad
 \kappa=Km^2,\qquad d=-\beta I_\phi(u^2+\kappa j^2).
 \end{aligned}
 \tag{CD.2}
$$

No row in (CD.2) is assumed to vanish.

A strictly negative compact window is already available for the actual
intrinsic metric. The completed [SP result, Sections 2 and 3.4](R133-supplement-actual-complete-primitive-and-mean-strict-propagation-to-the-waist.md)
uses fixed eta0 and the complete range $|\nu-\nu_0|\le10^{-8}$, with

$$
 0\le r\le r_c=\frac{2333968743003}{10^{13}},
 \qquad q=\sqrt{-K}>0.
$$

Its public run is 43731464771/1. We consume only this intrinsic
curvature sign, which also holds at nu0. Its state, repaired-mean and
response bounds are not transferred to a different raw centre.

The metric identity

$$
 \left(\frac{a'}{\sqrt{E_\nu}}\right)'
       =-a\sqrt{E_\nu}\,K
 \tag{CD.3}
$$

and the same waist condition $a'(0)=0$ imply $a'>0$, hence $\beta>0$,
on $0<r\le r_c$. Indeed the right side of (CD.3) is strictly positive
there. Consequently $\beta K<0$ throughout the original compact
window

$$
 I=[\ell_-,\ell_+]=[1/20,9/50]\subset(0,r_c).
 \tag{CD.4}
$$

The larger ordinary-source interval $[0,.9]$ is not being described
as a negative-curvature interval.

Choose the explicit cutoff

$$
 \chi(r)=
 \begin{cases}
 4096t^6(1-t)^6,&t=(r-\ell_-)/\ell,\quad 0<t<1,\\
 0,&\text{otherwise},
 \end{cases}
 \qquad \ell=\ell_+-\ell_-=13/100.
 \tag{CD.5}
$$

It is the same scalar polynomial shape as the original compact metric
bump, but its use below changes the extrinsic density, not the metric
parameter. It satisfies $0\le\chi\le1$, is globally $C^5$, and is
identically zero near the waist and near the outer endpoint $R=25/8$.

Useful exact derivative bounds are

$$
 \|\chi'\|_\infty
 =\frac{24}{\ell\sqrt{11}}\left(\frac{10}{11}\right)^5<35,
 \qquad
 \|\chi''\|_\infty=\frac{48}{\ell^2}=\frac{480000}{169}.
 \tag{CD.6}
$$

To verify them put $x=2t-1$, so $\chi=(1-x^2)^6$,
$\chi'=-24x(1-x^2)^5/\ell$ and
$\chi''=-48(1-x^2)^4(1-11x^2)/\ell^2$.
The first maximum occurs at $x^2=1/11$. For the second, the maximum
of $(1-y)^4|1-11y|$ on $0\le y\le1$ is 1: the other interior
candidate is $y=3/11$ and has value $8192/14641<1$.
For the strict numerical inequality in (CD.6), use
$\sqrt{11}>33/10$ and $(10/11)^5<5/8$.

The exact integral fees, if useful for an ordinary radial $L^2$ source,
are

$$
 \|\chi\|_{L^2_r}^2
    =2^{24}\ell\,\frac{(12!)^2}{25!},\qquad
 \|\chi'\|_{L^2_r}^2
    =\frac{24576^2}{23\ell}\frac{(10!)^2}{21!}.
 \tag{CD.7}
$$

The second identity follows by integrating
$t^{10}(1-t)^{10}(1-2t)^2$; its value is
$B(11,11)/23$.

## CD2. Density control and the exact quadratic profile

For one real control $\xi$ put

$$
 \lambda_\xi(r)=1+\xi\chi(r),\qquad
 j_\xi=1+\lambda_\xi z,\qquad u_\xi=u.
 \tag{CD.8}
$$

Thus $\langle j_\xi\rangle=1$ exactly, and

$$
 J_\xi=\langle j_\xi^2\rangle
        =1+\lambda_\xi^2 V/m^2.
 \tag{CD.9}
$$

Let $Y_\xi$ be the unique continuous, piecewise absolutely continuous
solution

$$
 Y_\xi'=cY_\xi+2\beta Ka^2J_\xi,\qquad
 Y_\xi(0)=1,\qquad c=2\beta U.
 \tag{CD.10}
$$

It exists as a scalar linear solution before any positivity is asserted.
Write

$$
 \mathcal G(r,s)=\exp\left(\int_s^r c(t)\,dt\right)>0.
 \tag{CD.11}
$$

The $Y_0$ in this section is the fixed-density mean retraction of
[RS](R144-supplement-fixed-density-rotational-reference-subtraction.md),
not the original $n=a^2/m^2$. Expanding (CD.9) and using variation of
constants gives the **exact whole-profile quadratic**

$$
 \boxed{Y_\xi(r)=Y_0(r)+\xi A(r)+\xi^2B(r),}
 \tag{CD.12}
$$

where the new scalar coefficient functions are

$$
 \begin{aligned}
 A(r)&=4\int_0^r\mathcal G(r,s)\,
       \beta(s)K(s)a(s)^2\chi(s)\frac{V(s)}{m(s)^2}\,ds,\\
 B(r)&=2\int_0^r\mathcal G(r,s)\,
       \beta(s)K(s)a(s)^2\chi(s)^2\frac{V(s)}{m(s)^2}\,ds.
 \end{aligned}
 \tag{CD.13}
$$

The full original signed account is retained as well. With the RS
definitions of the original signed bulk $B_D^{\,0}$ and atom sum $A_D$,

$$
 D_\xi(r)=\mathcal G(r,0)D(0)
       +B_D^{\,0}(r)+A_D(r)+\xi A(r)+\xi^2B(r).
 \tag{CD.13a}
$$

Thus the compact control adds its explicit signed forcing; it does
not erase the old initial mean difference, the old true mean residual
or any old interface.

Here $A,B$ are scalar control coefficients, not components of the
second fundamental form. All original raw radial pieces and both
one-sided values at their actual interfaces belong to these integrals.

Since $V\ge0$, $\beta K<0$ on the support, and $\mathcal G>0$,

$$
 A(r)\le0,\qquad B(r)\le0,\qquad |B(r)|\le |A(r)|/2.
 \tag{CD.14}
$$

Strict $A(R)<0$ follows if $V$ is nonzero on a positive-measure subset
where $\chi>0$. A consumer must establish a strict lower bound for
$-A(R)$, rather than infer it from the nonzero waist amplitude.
The cutoff is zero at the waist, so that amplitude alone is not the
required support witness.

No root singularity enters (CD.10)--(CD.13), and no $1/K$ is used.
The exact mean is recovered only when the separate whole-domain
positivity gate $Y_\xi>0$ is established:

$$
 m_\xi=-a/\sqrt{Y_\xi},\qquad v_\xi=m_\xi j_\xi.
 \tag{CD.15}
$$

## CD3. Uniform existence and uniqueness of the small outer root

Let

$$
 n_R=a(R)^2/m(R)^2>0,\quad
 D_R=Y_0(R)-n_R,\quad
 A_*=A(R),\quad B_*=B(R),
$$

and suppose a complete directed input proves

$$
 \mathfrak a=-A_*\ge a_->0,\qquad |D_R|\le d.
 \tag{CD.16}
$$

By (CD.14), $\mathfrak b=-B_*$ satisfies
$0\le\mathfrak b\le\mathfrak a/2$. The outer equation is

$$
 \mathcal F(\xi)=D_R+A_*\xi+B_*\xi^2
             =D_R-\mathfrak a\xi-\mathfrak b\xi^2=0.
 \tag{CD.17}
$$

Choose a radius $0<\rho<1$ and require the complete small-root gate

$$
 \boxed{d<a_-\rho(1-\rho/2).}
 \tag{CD.18}
$$

Then

$$
 \mathcal F(-\rho)
 \ge-d+\mathfrak a\rho-\mathfrak b\rho^2>0,\qquad
 \mathcal F(\rho)\le d-\mathfrak a\rho<0.
$$

Moreover, throughout $|\xi|\le\rho$,

$$
 \mathcal F'(\xi)=-\mathfrak a-2\mathfrak b\xi
       \le-a_-(1-\rho)<0.
 \tag{CD.19}
$$

Hence there is exactly one real root $\xi_*$ in this interval. It
satisfies the sharper bound

$$
 |\xi_*|
 \le\frac{d}{a_-(1-\rho/2)},\qquad
 \operatorname{sgn}\xi_*=\operatorname{sgn}D_R
 \quad(D_R\ne0).
 \tag{CD.20}
$$

For example, $0<d<a_-/4$ permits $\rho=2d/a_-<1/2$.
If $D_R=0$, the small root is exactly zero.

When $\mathfrak b>0$, the stable exact expression is

$$
 \xi_*=\frac{2D_R}
       {\mathfrak a+\sqrt{\mathfrak a^2+4\mathfrak bD_R}},
 \tag{CD.21}
$$

and for $\mathfrak b=0$ it is $D_R/\mathfrak a$. The radicand is
strictly positive under (CD.18); indeed it is bounded below by
$\mathfrak a^2(1-\rho)^2$. No subtraction of two almost equal square
roots is required.

A whole ball for $D_R$ may contain zero. That does not obstruct this
existence proof: (CD.18) is uniform for every actual value in the ball.
It also does not authorize replacing $D_R$ by its midpoint.
A complete bound for $B_*$ can sharpen the interval, but the sign
comparison (CD.14) already supplies the displayed sufficient gate.

The conclusion of this section is a scalar root. It does not by
itself prove $Y_{\xi_*}>0$, $j_{\xi_*}>0$ or smallness of the new full
field.

## CD4. Density positivity, the changed interior angle, and a whole norm gate

Since $j_\xi=j+\xi\chi z$, a direct density gate on $I$ is

$$
 \inf_I j-\rho\sup_I|z|>0.
 \tag{CD.22}
$$

For the complete original 32-mode input, write
$M_{\rm osc}(r)=\sqrt{64V(r)}$. If the old complete negative-$v$
qualification gives $v\le-g_I<0$ on $I$, the alternative sufficient gate

$$
 \rho\sup_I M_{\rm osc}<g_I
 \tag{CD.23}
$$

implies $j_\xi>0$ for all $|\xi|\le\rho$. To see this, use

$$
 m j_\xi=v+\xi\chi(v-m),
$$

whose right side remains strictly negative under (CD.23).
Outside $I$, $j_\xi=j$. This explicitly consumes the old complete
pointwise density qualification and a complete oscillation bound.
Neither is inferred from angular samples.

The exact material lift changes by

$$
 \Theta_\xi=\phi+I_\phi(j_\xi-1)
       =\Theta+\xi\chi I_\phi z,\qquad
 \partial_\phi\Theta_\xi=j_\xi.
 \tag{CD.24}
$$

Thus the material angle is unchanged near both endpoints, while it
generally changes inside the support. Its full fourfold Wiener bound is

$$
 \|\Theta_\xi-\Theta\|_{A^0_\phi}
     \le |\xi|\chi\,\|z\|_{A^0_\phi}/4.
 \tag{CD.25}
$$

The primitive factor $1/4$ comes from the first physical frequency,
not from a change of circle normalization.

Whole $Y_\xi>0$ is a separate gate. It may be proved by direct
same-r signed evaluation of (CD.12). A sufficient triangle estimate
is

$$
 Y_0(r)>\rho|A(r)|+\rho^2|B(r)|\quad\text{for all }r,
 \tag{CD.26}
$$

but (CD.26) is not required. In particular the linear $Y_0$ may have
failed a positivity gate while a boundary-compensated $Y_{\xi_*}$
is positive. Such a conclusion needs its own complete signed
whole-domain enclosure.

On a certified-positive cell put
$q_\xi=m_\xi/m=\sqrt{n/Y_\xi}$ and $D_\xi=Y_\xi-n$.
Then

$$
 q_\xi-1
   =-\frac{D_\xi}{\sqrt{Y_\xi}(\sqrt n+\sqrt{Y_\xi})},
$$

$$
 v_\xi-v=(q_\xi-1)v+q_\xi\xi\chi(v-m).
 \tag{CD.27}
$$

Consequently

$$
 \|v_\xi-v\|_{A^0_\phi}
 \le |q_\xi-1|(-m+\sqrt{64V})
       +q_\xi|\xi|\chi\sqrt{64V}.
 \tag{CD.28}
$$

All denominators and square roots in this bound use strict positive
whole-ball endpoints, as in RS.21. Since $u_\xi=u$, (CD.28) gives
a concrete complete moving-$C^0$ comparison gate, including the
density change inside the support.

For a comparison at the same physical angle in the interior, there
is an additional composition cost. Let
$\widehat Q=(u/v,1/v)$ and
$\widehat Q_\xi=(u/v_\xi,1/v_\xi)$ in moving coordinates.
If $j\ge j_->0$, then

$$
 \|\Theta_\xi^{-1}-\Theta^{-1}\|_\infty
   \le \|\Theta_\xi-\Theta\|_\infty/j_- ,
$$

$$
 \|Q_\xi-Q\|_\infty
 \le \|\widehat Q_\xi-\widehat Q\|_\infty
      +\|\partial_\phi\widehat Q\|_\infty
        \|\Theta_\xi-\Theta\|_\infty/j_- .
 \tag{CD.29}
$$

The first term is bounded by
$\sqrt{1+\|u\|_\infty^2}\|v_\xi-v\|_\infty/
(\inf|v_\xi|\inf|v|)$.
No unchanged interior angular chart is claimed.

## CD5. Exact outer state and the terminal formula outside the support

At the small root, $Y_{\xi_*}(R)=n_R$ and hence
$m_{\xi_*}(R)=m(R)$ on the negative branch.
Because $\chi=0$ near $R$,

$$
 (u_{\xi_*},v_{\xi_*})(R,\phi)=(u,v)(R,\phi),
 \qquad \Theta_{\xi_*}(R,\phi)=\Theta(R,\phi).
 \tag{CD.30}
$$

Therefore the entire physical $B,C$ angular functions at $R$ are
identical, including both full means, all nonmean frequencies and
their physical angular derivatives. Every fixed-parameter boundary
row depending only on those same point-state functions has exactly
its original residual. Such an original residual is not asserted
to be zero.

The density control has a useful exact exterior-of-support formula.
For $r\ge\ell_+$, both coefficient functions in (CD.13) propagate
homogeneously:

$$
 A(r)=\mathcal G(r,R)A_*,\qquad
 B(r)=\mathcal G(r,R)B_*.
$$

Using the root equation gives

$$
 \boxed{
 Y_{\xi_*}(r)=Y_0(r)-\mathcal G(r,R)D_R,\qquad
 D_{\xi_*}(r)=D_0(r)-\mathcal G(r,R)D_R ,
 }\qquad r\ge\ell_+.
 \tag{CD.31}
$$

Here $D_0=Y_0-n$ is the complete fixed-density retraction difference.

Equivalently, on these original smooth pieces
$D_{\xi_*}'=cD_{\xi_*}-\tau R_0$ with
$\tau=-2a^2/m^3$, and $D_{\xi_*}(R)=0$. Including every actual
one-sided raw mean interface gives the exact terminal representation

$$
 D_{\xi_*}(r)
   =\int_r^R\mathcal G(r,s)\tau(s)R_0(s)\,ds
       +\sum_{r<r_i<R}\mathcal G(r,r_i)[n]_{r_i}.
 \tag{CD.32}
$$

At a seam one uses a consistent one-sided endpoint convention.
This is a new boundary-compensated identity, not a reevaluation of
the already completed old fixed-variance mean Green target.
It retains the actual signed sources and all atoms.

Equation (CD.32) removes the free initial contribution from this
terminally constrained part of the profile. It does not bound its
norm for free, and the conversion from $Y$ to the physical mean
still contains the actual radius factors.

Point-state equality at $R$ also does not assert equality of every
radial jet. On a smooth outer piece, where $\chi=0$,
$m_{\xi_*}'(R)-m'(R)=-R_0(R)$, hence

$$
 (v_{\xi_*})_r(R)-v_r(R)=-j(R)R_0(R).
 \tag{CD.33}
$$

This retained old mean source is one reason that boundary state
equality is not a proof of complete smooth cap installation.
Independent position, height, far-label and genuine regular-cap
requirements remain.

## CD6. Every changed nonmean equation, including the cutoff derivative

Define

$$
 \kappa_\xi=Km_\xi^2,\qquad
 \Delta S=\kappa_\xi j_\xi^2-\kappa j^2,\qquad
 \Delta P=\kappa_\xi j_\xi-\kappa j .
 \tag{CD.34}
$$

The drift change is exactly
$d_\xi-d=-\beta I_\phi\Delta S$.
The **complete original residuals** of the new centre are

$$
 \boxed{
 R_{u,\xi}
   =R_u+\beta(I_\phi\Delta S)u_\phi
             -\gamma\partial_\phi\Delta P+\beta u\Delta S ,
 }
 \tag{CD.35}
$$

$$
 \boxed{
 \begin{aligned}
 F_{j,\xi}
  &=\lambda_\xi F_j+\xi\chi' z
       +\xi\chi(d-\gamma u)_\phi
       +\beta(I_\phi\Delta S\,j_\xi)_\phi,\\
 R_{v,\xi}&=m_\xi F_{j,\xi},\qquad
 \langle R_{v,\xi}\rangle=0 .
 \end{aligned}}
 \tag{CD.36}
$$

To prove (CD.35), subtract the first equations in (CD.2), retaining
the full drift and both products. For (CD.36), initially write

$$
 F_{j,\xi}
 =F_j+\partial_r(\xi\chi z)
      -\partial_\phi(d\,\xi\chi z+(d_\xi-d)j_\xi).
$$

Use $z_r=j_r=(dj-\gamma u)_\phi+F_j$ and
$j-z=1$ to obtain (CD.36). In particular the term
$\xi\chi'z$ does not disappear. All four terms of $F_{j,\xi}$ have
zero angular mean, so the exact new mean equation gives the last
line.

Here is one complete Wiener budget, retaining each obligation.
Write

$$
 J_A=\|j\|_{A^0},\quad Z_A=\|z\|_{A^0},\quad
 J_1=\|j_\phi\|_{A^0},\quad
 U_A=\|u\|_{A^0},\quad U_1=\|u_\phi\|_{A^0},
$$

$$
 \epsilon=|\xi|\chi,\quad
 J_{\xi,A}\le J_A+\epsilon Z_A,\quad
 J_{\xi,1}=|\lambda_\xi|J_1\le(1+\epsilon)J_1 .
$$

Put

$$
 \mathcal S=|\kappa_\xi-\kappa|J_A^2
          +|\kappa_\xi|(2\epsilon J_AZ_A+\epsilon^2Z_A^2).
 \tag{CD.37}
$$

Then

$$
 \|\Delta S\|_{A^0}\le\mathcal S,\qquad
 \|\partial_\phi\Delta P\|_{A^0}
       \le(|\kappa_\xi-\kappa|+|\kappa_\xi|\epsilon)J_1,
$$

$$
 \|R_{u,\xi}-R_u\|_{A^0}
 \le|\beta|\mathcal S(U_1/4+U_A)
      +\gamma(|\kappa_\xi-\kappa|+|\kappa_\xi|\epsilon)J_1 ,
 \tag{CD.38}
$$

$$
 \begin{aligned}
 \|F_{j,\xi}\|_{A^0}
 \le{}&(1+\epsilon)\|F_j\|_{A^0}
       +|\xi||\chi'|Z_A\\
 &+\epsilon(\|d_\phi\|_{A^0}+\gamma U_1)
       +|\beta|\mathcal S(J_{\xi,A}+J_{\xi,1}/4),\\
 \|R_{v,\xi}\|_{A^0}&\le|m_\xi|\|F_{j,\xi}\|_{A^0}.
 \end{aligned}
 \tag{CD.39}
$$

One may use
$\|d_\phi\|_{A^0}\le|\beta|(U_A^2+|\kappa|J_A^2)$,
or a sharper complete saved bound. The true original density source
is $F_j=(R_v-jR_0)/m$; its full old mean is not discarded.

The new mean feedback is also exact:

$$
 \kappa_\xi-\kappa
    =-\frac{Ka^2D_\xi}{nY_\xi}
    =K(m_\xi-m)(m_\xi+m).
 \tag{CD.40}
$$

Thus a full certified mean-shift bound supplies a concrete coefficient
fee. On the compact window the new cutoff term can be integrated
using the exact (CD.7). Outside the window (CD.35)--(CD.36) reduce
to the full fixed-density residual formulas MV.19. No unknown
Fourier tail is dropped by these identities or norm estimates.

## CD7. All interfaces and regularity obligations

Because $a$ and the genuine reference are continuous, and the
linear equation (CD.10) has only piecewise finite coefficients,
$Y_\xi$ and $W_\xi=Y_\xi-N_s$ are continuous at each old raw join.
The original $n=a^2/m^2$ may jump, so

$$
 [D_\xi]=-[n].
 \tag{CD.41}
$$

If a signed-atom account is kept, it has the same original atoms
$-[n]$, each propagated once by the same $\mathcal G$. The compact
control does not alter the original raw denominator $m$ in (CD.13).

The new **full fields** have the exact transmission

$$
 [u_\xi]=[u],\qquad
 [j_\xi]=\lambda_\xi[j],\qquad
 [v_\xi]=m_\xi\lambda_\xi[j].
 \tag{CD.42}
$$

In particular zero mean jump is not full continuity. The old jump
$[j]=[v/m]$ must be computed with its actual two means; replacing it
by $[v]/m$ when $[m]\ne0$ is invalid. Original nonmean transmission
and any continuous repair remain necessary.

The cutoff's first five derivatives vanish at its support endpoints,
so it creates no new value, first-derivative or second-derivative
seam there. This does not repair a pre-existing raw PPoly seam.
For an already regular input the construction preserves the
corresponding regularity, provided its whole positive denominator
bounds hold. Reflection through the waist preserves the original
parities because the cutoff is zero near the waist and may be
extended evenly. It does not erase a nonzero original odd waist
trace: $u_\xi(0)=u(0)$.

## CD8. Phase, parameter derivatives and the remaining full BVP

At the waist $m_\xi(0)=-a(0)$, while the entire original odd waist
trace remains. At the outer small root the entire original point
state is restored. These are precise row statements. They do not
prove that the full Codazzi system vanishes in between.

The R144 off-shell holonomy identity still contains the full changed
bulk residual and every interface. Its use must therefore insert
(CD.35)--(CD.42). A phase represented by an outer point-state row
retains its original residual at fixed metric; an interior
holonomy or an additional full boundary construction cannot be
declared solved from (CD.30).

For a genuine differentiable family of inputs with an independent
metric/design parameter $\mu$, the implicit scalar derivative is

$$
 \partial_\mu\xi_*
  =-\frac{\partial_\mu D_R
          +\xi_*\partial_\mu A_*
          +\xi_*^2\partial_\mu B_*}
          {A_*+2\xi_*B_*}.
 \tag{CD.43}
$$

The denominator has the lower magnitude in (CD.19). Every numerator
term refers to the actual same-member state, metric, propagator and
mean; none is supplied by an unrelated old proposal.

For any complete phase functional $\Phi(\mu,\xi)$ the corresponding
derivative after mean selection is

$$
 \frac{d}{d\mu}\Phi(\mu,\xi_*(\mu))
       =\Phi_\mu+\Phi_\xi\,\partial_\mu\xi_* .
 \tag{CD.44}
$$

Both terms remain unless a proved functional identity eliminates one.
If a particular row depends only on outer point-state data and those
data are restored as an identity for the entire input family, then
that specific row has the original family's value and derivative.
That qualification does not supply the unsolved complete phase
functional or the full interior inverse.

The current numerical target is the raw centre at fixed eta0 and
nu0. It does not inherit the selected implicit delta-star or a
selected phase certificate. Applying this construction to a different
selected or repaired input would require that exact input's own
complete moments, residuals and matching conditions.

Finally, the scalar inverse bound
$[a_-(1-\rho)]^{-1}$ concerns only (CD.17).
It is not a full PDE inverse or a free change of Banach-space norm.
For example, at the outer root the physical even-mean derivative is

$$
 \partial_\xi\langle C_\xi\rangle_\theta(R)
  =-\frac{A_*+2\xi_*B_*}{2a(R)\sqrt{n_R}}
  =-\frac{|m(R)|(A_*+2\xi_*B_*)}{2a(R)^2}.
 \tag{CD.45}
$$

The actual radius scaling remains visible. The same complete
nonmean, phase, transmission, height and geometric obligations
must be paid before this mean construction yields a real nearby
isometric immersion or the required closed nonrigid family.
