# R144 supplement: compact-centre residual as ordinary and angular-divergence sources

2026-11-26, visible-exact-astra-198c63d-20261126 / global_geometry.

This note gives an executable source receiver for the new compact-density
mean centre. It uses its actual parameter interval and its actual whole
mean profile or an independently proved uniform mean ball. It does not
inherit the residual, phase or inverse of the selected centre.
The main identities avoid differentiating the new radial mean and keep
the angular derivatives as genuine divergence sources.

## CS1. Exact object and residual convention

Use the fixed original metric at eta0 and nu0 and the original raw
fourfold moving fields. The definitions and compact mean construction
are those of
[CD](R144-supplement-compact-density-quadratic-mean-compensator.md),
[CR](R144-supplement-complete-C0-mean-receiver-and-compact-moments.md),
and
[CP](R144-supplement-profile-weighted-mean-feedback-polynomial.md).

Put

$$
 m=\langle v\rangle<0,\quad j=v/m=1+z,\quad
 U=\langle u^2\rangle,\quad V=\langle(v-m)^2\rangle,\quad
 Z=\sqrt V/|m|,\quad \kappa=Km^2.
$$

The primitive $\mathcal I$ is the zero-mean inverse of $\partial_\phi$
on the fourfold circle, and

$$
 d=-\beta\mathcal I(u^2+\kappa j^2).
$$

Let the new exact scalar mean be $m_\xi=m+h<0$, with

$$
 e=\xi\chi,\quad \lambda=1+e,\quad
 j_\xi=1+\lambda z,\quad
 u_\xi=u,\quad v_\xi=m_\xi j_\xi,\quad
 \kappa_\xi=Km_\xi^2.
\tag{CS.1}
$$

The new mean equation is solved on every original piece and its
mean is continuous across the actual original mean joins. Its raw
nonmean joins are retained.

Use the residual convention of MV/CD: the residual is added to the
right side of each moving equation. In particular
$R_0=\langle R_v\rangle$ is the true raw mean residual, not a
defining equation for the raw candidate. Define

$$
 \Delta\kappa=\kappa_\xi-\kappa,\qquad
 A=\kappa_\xi\lambda-\kappa,\qquad
 B=\kappa_\xi\lambda^2-\kappa.
\tag{CS.2}
$$

These are radial scalars. The letters $A,B$ here are coefficient
differences, not the compact moments $A_R,B_R$ or physical curvature
coordinates.

Then the exact angular expressions are

$$
\begin{aligned}
 \Delta S&=\kappa_\xi j_\xi^2-\kappa j^2
          =\Delta\kappa+2Az+Bz^2,\\
 \langle\Delta S\rangle&=\Delta\kappa+BZ^2,\\
 \mathcal I\Delta S&=2A\mathcal Iz+B\mathcal I(z^2),\\
 \Delta P&=\kappa_\xi j_\xi-\kappa j
          =\Delta\kappa+Az,\qquad
 (\Delta P)^\circ=Az .
\end{aligned}
\tag{CS.3}
$$

Here $\circ$ removes the normalized angular mean. The equality
$\langle z^2\rangle=Z^2$ uses the actual full original variance.

## CS2. Exact ordinary/divergence decomposition

The full changed first residual is

$$
 R_{u,\xi}
 =R_u+\beta(\mathcal I\Delta S)u_\phi
       -\gamma\partial_\phi\Delta P+\beta u\Delta S.
$$

Since $(\mathcal I\Delta S)_\phi=\Delta S-\langle\Delta S\rangle$,
the two beta terms combine exactly. Thus

$$
 \boxed{
 R_{u,\xi}=F_u+\partial_\phi Q_u,\qquad
 F_u=R_u+\beta\langle\Delta S\rangle u,\qquad
 Q_u=\beta u\mathcal I\Delta S-\gamma Az .
 }
\tag{CS.4}
$$

In particular the radial constant $\gamma\Delta\kappa$ does not belong
to the divergence flux. It has zero angular derivative. The same
$\Delta\kappa$ still enters the genuine ordinary term in $F_u$.

For the second row, CD gives the complete mean-free density residual

$$
 F_{j,\xi}
 =\lambda\frac{R_v-jR_0}{m}
   +\xi\chi' z
   +e(d-\gamma u)_\phi
   +\beta(\mathcal I\Delta S\,j_\xi)_\phi .
$$

Multiplication by the radial scalar $m_\xi$ yields

$$
 \boxed{
 \begin{aligned}
 R_{v,\xi}&=F_v+\partial_\phi Q_v,\\
 F_v&=\frac{m_\xi\lambda}{m}(R_v-jR_0)
                +m_\xi\xi\chi' z,\\
 Q_v&=m_\xi\left[e(d-\gamma u)
                    +\beta\mathcal I\Delta S\,j_\xi\right].
 \end{aligned}}
\tag{CS.5}
$$

Equations (CS.4)--(CS.5) are identities, with no estimate and no
derivative of $h$. The term $\xi\chi' z$ is retained as an ordinary
source. The term $R_v-jR_0$ retains the actual raw mean defect.

All ordinary terms in (CS.4)--(CS.5) have zero angular mean in the
original symmetry class. In the first row this follows from odd
$u$ and odd $R_u$. In the second row it follows from
$\langle j\rangle=1$, $\langle R_v\rangle=R_0$, and $\langle z\rangle=0$.
The divergence terms also have zero mean. Thus the new second
residual has exactly zero mean, as its exact scalar equation requires.

This decomposition concerns the moving angle. It is not a claim that
the corresponding physical-angle flux has the same norm without a
composition and density bound.

## CS3. Complete angular L2 bounds from the original finite variance

The raw centre has 32 sine modes for $u$ and 32 nonconstant cosine
modes for $v-m$, with physical frequencies $4,8,\ldots,128$.
Cauchy--Schwarz gives

$$
 \|u\|_{L^2_\phi}=\sqrt U,\quad
 \|u\|_{A_0}\le8\sqrt U,\qquad
 \|z\|_{L^2_\phi}=Z,\quad
 \|z\|_{A_0}\le8Z.
\tag{CS.6}
$$

These are full finite-centre identities/bounds, not a truncation
of an unknown response. Set $Z_A=8Z$. For every nonzero fourfold
frequency the primitive multiplier has size at most $1/4$, hence

$$
 \|\mathcal I\Delta S\|_{L^2_\phi}
 \le T:=\frac{(2|A|+|B|Z_A)Z}{4}.
\tag{CS.7}
$$

Indeed $\|\mathcal Iz\|_2\le Z/4$, while
$\|\mathcal I(z^2)\|_2\le\|z^2-\langle z^2\rangle\|_2/4
\le Z_AZ/4$. Orthogonal removal of a mean cannot increase the
$L^2$ norm.

Likewise

$$
 \|d\|_{L^2_\phi}
 \le D:=\frac{|\beta|}{4}
       \left[8U+|\kappa|(2+Z_A)Z\right].
\tag{CS.8}
$$

For its first term use
$\|u^2-U\|_2\le\|u\|_\infty\|u\|_2\le8U$.
For the second use
$j^2-\langle j^2\rangle=2z+z^2-Z^2$.

Consequently the four local source bounds are

$$
\begin{aligned}
 f_u(r)&=|\beta|\,|\Delta\kappa+BZ^2|\,\sqrt U,\\
 q_u(r)&=8|\beta|\sqrt U\,T+\gamma|A|Z,\\
 c_v(r)&=\left|\frac{m_\xi\lambda}{m}\right|
                         \sqrt{1+Z^2},\\
 f_{v,\chi}(r)&=|m_\xi|\,|\xi|\,|\chi'|\,Z,\\
 q_v(r)&=|m_\xi|\left[
 |e|(D+\gamma\sqrt U)
       +|\beta|(1+|\lambda|Z_A)T\right].
\end{aligned}
\tag{CS.9}
$$

The function $c_v$ is an operator coefficient for the old raw second
residual. More precisely, for any angular function $g$,

$$
 \|g-j\langle g\rangle\|_2
 \le\sqrt{1+Z^2}\,\|g\|_2 .
\tag{CS.10}
$$

To prove this write $g=c+g^\circ$ with orthogonal mean and mean-free
parts. The map $(c,g^\circ)\mapsto g^\circ-zc$ has product with its
adjoint equal to $Id+z\otimes z$ on the mean-free space, whose norm is
$1+\|z\|_2^2$. This is sharper than separately charging the raw mean
and nonmean parts. It does not remove their true contribution.

If $E_u,E_v$ are the already proved complete physical raw
$L^2_{r,\phi}$ residual bounds, then

$$
\begin{aligned}
 \|F_u\|_{L^2_{r,\phi}}&\le E_u+\|f_u\|_{L^2_r},\\
 \|Q_u\|_{L^2_{r,\phi}}&\le\|q_u\|_{L^2_r},\\
 \|F_v\|_{L^2_{r,\phi}}&\le
     \|c_v\|_\infty E_v+\|f_{v,\chi}\|_{L^2_r},\\
 \|Q_v\|_{L^2_{r,\phi}}&\le\|q_v\|_{L^2_r}.
\end{aligned}
\tag{CS.11}
$$

For the original fixed eta0 raw centre the already recorded bounds are

$$
 E_u=\alpha\,4.201205\,10^{-8},\qquad
 E_v=\alpha\,8.194504\,10^{-8},
$$

with $\alpha=6890507429876859/9007199254740992$.
See the
[actual full original residual note](../notes/2026-11-14-R133-final-complete-moving-residual.md).
They are used only as the unchanged raw terms in (CS.11).
The four new source contributions must still be evaluated.

## CS4. A true profile or a uniform mean ball gives executable bounds

Suppose an actual complete result supplies $|\xi|\le\rho<1$ and a
valid whole radial profile $|h(r)|\le b(r)$. A uniform mean ball from
CR20 or CP8 is an admissible constant choice of $b(r)$.

Set

$$
\begin{aligned}
 M_+&=|m|+b,\qquad
 E=\rho\chi,\\
 K_\Delta&=|K|b(2|m|+b),\qquad
 K_+=|K|M_+^2,\\
 A_+&=K_\Delta+K_+E,\qquad
 B_+=K_\Delta+K_+(2E+E^2).
\end{aligned}
\tag{CS.12}
$$

Then $|\Delta\kappa|\le K_\Delta$, $|A|\le A_+$,
$|B|\le B_+$, $|m_\xi|\le M_+$ and $|\lambda|\le1+E$.
In (CS.9) one may use

$$
 |\Delta\kappa+BZ^2|\le K_\Delta+B_+Z^2,\qquad
 c_v\le (1+b/|m|)(1+E)\sqrt{1+Z^2}.
\tag{CS.13}
$$

These formulas use only the original complete row carriers
$a,\beta,\gamma,K,m,U,V$, the actual certified $\rho,b$, and the
fixed compact polynomial. No new intrinsic primitive or angular
DFT is required for this sufficient source bound.

When a sharper signed terminal profile for $h$ is actually available,
(CS.2)--(CS.9) may be evaluated with that whole profile before taking
absolute values. The outer identity
$Y_{\xi_*}=Y_0-H D_R/H_R$ after the compact support can provide
that profile only if its complete actual input enclosures are
available. A signed final value by itself is not a full radial
profile. No completed old forward target is rerun merely to obtain
a tighter bound.

For a whole-cell consumer, every positive coefficient is enclosed on
the entire original closed row. The fixed factors $\chi,\chi^2$
and $(\chi')^2$ can be integrated as exact rational polynomials on
their support. Squared positive sums in (CS.9) can either be integrated
as their full polynomial majorants or bounded by a complete cellwise
upper before multiplication by the true row length. Neither method
uses point sampling. The support edges are exact cuts.

The first minimal complete scientific output for this receiver is

$$
 \|f_u\|_{L^2_r},\quad
 \|q_u\|_{L^2_r},\quad
 \|c_v\|_\infty,\quad
 \|f_{v,\chi}\|_{L^2_r},\quad
 \|q_v\|_{L^2_r},
\tag{CS.14}
$$

plus its actual $\rho,b$ or complete-profile identity and all whole
coverage counters. These five scalars give the four ordinary/flux
norms in (CS.11). They do not assert any positive or negative
receiver has already consumed those sources.

## CS5. Weak angular norms retain the derivative at its real location

The ordinary and flux norms in (CS.11) are a convenient strong input
format. For a zero-mean fourfold Fourier series define

$$
 \|f\|_{\dot H^{-s}_\phi}^2
 =\sum_{k\ne0}|4k|^{-2s}|\widehat f_k|^2.
$$

Every flux in (CS.4)--(CS.5) has physical Fourier support at most
$4(3\cdot32)=384$: $z^2$ has twice the raw degree, and its product
with $u$ or $j_\xi$ has at most three times the raw degree.
For $0\le s\le1$,

$$
 \|F+\partial_\phi Q\|_{L^2_r\dot H^{-s}_\phi}
 \le4^{-s}\|F\|_{L^2_{r,\phi}}
       +384^{1-s}\|Q^\circ\|_{L^2_{r,\phi}}
 \le4^{-s}\|F\|_2+384^{1-s}\|Q\|_2.
\tag{CS.15}
$$

The ordinary $F$ has zero mean as proved in CS2. The mean of $Q$
is irrelevant because its angular derivative vanishes. If a receiver
uses an inhomogeneous Bessel norm, the same right side is still a
valid upper bound, since $(1+n^2)^{-s/2}\le|n|^{-s}$ for $n\ne0$.

In particular an ordinary $L^2_r H^{-2/3}$ input pays at most
$4^{-2/3}$ on its ordinary part and $384^{1/3}$ on its flux part.
A genuine second-row $L^2_r H^{-1}$ input pays $1/4$ and $1$,
respectively. These are explicit Fourier conversion bounds;
an angular divergence in the first row is not silently treated as
an $H^{-2/3}$ source of unit norm.

The original full negative strict/root receivers, positive ordinary
or divergence ports, moving-to-physical bridge and all mean/height
rows must be used with their actual declared types. If a receiver
requires a stronger norm than (CS.15), that norm is not supplied
by relabelling these four numbers.

## CS6. Remaining interfaces, physical chart, and full BVP

The change still has the original exact jumps

$$
 [u_\xi]=[u],\qquad [j_\xi]=\lambda[j],\qquad
 [v_\xi]=m_\xi\lambda[j].
\tag{CS.16}
$$

Thus the bulk decomposition does not remove interface sources.
The complete new jump budget must use the two true raw traces and
the continuous $m_\xi$ at each original join. The old raw jump norm
is not automatically the new one.

The material angle is changed in the compact region:
$\Theta_\xi-\Theta=\xi\chi\,\mathcal Iz$.
Any physical-angle norm comparison pays its actual inverse-chart
composition and density factors. At the certified outer root the
point values return to the original outer state, but its radial jet
can still differ by the genuine old mean residual as CD33 states.

Finally, $R_{u,\xi},R_{v,\xi}$ are the actual residual of a new
piecewise mean-exact centre at raw eta0/nu0. No selected phase,
selected whole-family inverse, far height or cap match is inherited.
The present identities make its next complete source computation
concrete; they do not prove those equations or the final fixed-metric
family have been solved.
