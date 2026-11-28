# R149 ASQ8. A convergent physical phase iteration on an explicit ball at the selected state

**Proved for every input in the ball.** Fix the actual selected
$(Q_*,\nu_*,g_0)$ of CP.2, the original NP trial $h^a$ of CP.9,
and the exact $R$ of PD.1. For every real negative-body perturbation
$z$ with the physical symmetry, original pieces and
$$
 \|z\|_{L^2([0,r_*];\mathcal A_{1/1024},\oplus_1)}\le2^{-33000},
 \qquad
 \|v\|_{\mathcal A_s}=\sum_j e^{4|j|s}|\widehat v_j|,
 \tag{ASQ8.1}
$$
there exist a real $k$ and a real orientation-preserving degree-one
analytic lift $g$ for which, as an equality of full lifts,
$$
 P(Q_*+z+kh^a,\nu_*+k)\circ g=g\circ R .
 \tag{ASQ8.2}
$$
The perturbation need not have finite Fourier support or zero physical
mean. A fixed $z$ is chosen throughout the iteration. This theorem
solves the entire nonlinear phase fibre in the actual physical chart;
the regular equations evaluated on these states are separate.

## A positive complex value domain with explicit constants

Throughout this proof $\|\cdot\|_{S_r}$ is the supremum on
$|\operatorname{Im}x|<r$. Let $\sigma=2^{-10}$,
$s_F=2^{-2100}$, $\tau=2^{-2200}$, and $M=2^{6000}$.
The finite support of $Q_*$ is at most 96 by
[D.1](R133-supplement-exact-selected-parameter-core-differences-and-finite193-transfer.md).
RP.4, [SM.29](R144-supplement-mean-exact-compact-centres-on-the-selected-metric.md),
and $|\delta_*|<10^{-10}$ give
$$
 \sup_r\|Q_*\|_{\mathcal A_\sigma,1}
 \le e^{384/1024}\sqrt2(7+19\cdot10^{-10})<16 .
$$
Likewise the complete degree96 NP trial and CP.9 give
$\|h^a\|_{L^2_r\mathcal A_\sigma,1}
 \le e^{384/1024}\sqrt{2(193)}\,32<2048$.
The zero extension after the original support is retained.

Use the exact chronologically folded field $V$ of
[RP.5–7](R144-supplement-full-off-constraint-principal-return-Hessian.md),
on length $2r_*<1/2$. The actual $\beta,\beta K,c$ satisfy
$|\beta|,|\beta K|<6$, $|c|<8$. At the selected metric the
one-leg bound on $\partial_\phi V$ on $S_\sigma$ is
$6(16)^2$: differentiation of $I$ gives $P_{\ne0}$, a contraction
in the complete Wiener norm; the mean speed is angularly constant.
In particular the integral on both legs is $<1024$.
These bounds concern angular analyticity and integration in radius.
No radial derivative is taken at the turning point.

On $C=[1/20,9/50]$ the function $c(k)^2$ is affine and
$c_*>1/2$, $|c'_*|<47$. For complex $|k|\le2^{-16}$ write
$c(k)=c_*\sqrt{1+2(c'_*/c_*)k}$ on the branch at one. The argument
of the square root stays in $|w-1|<1/2$. Thus
$|c(k)-c_*|\le94|k|$, $|c(k)|<9$.
From D.2 at the selected base,
$\beta K(k)=e^{-kw}[\beta K_*+k(\beta K'_*+w\beta K_*)]$,
so $|\beta K(k)-\beta K_*|\le32|k|$, $|\beta K(k)|<8$.
The parameter changes are identically zero off $C$ before the root.
All these coefficients use $\eta_0$ and the same $r_*$.

Write $Z=\|z\|_{L^2_r\mathcal A_\sigma,1}$ also for complex $z$.
Whenever $Z,|k|\le2^{-16}$,
$d=\|z+kh^a\|_{L^2_r\mathcal A_\sigma,1}\le Z+2048|k|<1$.
The integrated supremum on $S_\sigma$ of the change of the whole
two-leg field is bounded by
$$
 2[8(32+1)d+32(16)^2|k|+9d+94(16)|k|]
      <2^{24}(Z+|k|)                                      \tag{ASQ8.3}
$$
when $Z+|k|>0$, and is zero at zero.
Indeed the quadratic difference uses the genuine products of the
two input fields, with $L^2_r$ Cauchy--Schwarz for two perturbations.
The outer factor two pays the return leg. The primitive has Wiener
norm at most one. The last two terms retain the entire speed mean
and the genuine metric change. Formula (ASQ8.3) only costs the stated
radial norm, even if an input varies sharply in radius.

Take $Z,|k|<\tau$. Compare each complex trajectory starting at
$\phi$ in $S_{s_F}$ with the real unperturbed trajectory from
$\operatorname{Re}\phi$. As long as it is in $S_\sigma$, the
difference is at most
$$
 e^{1024}[s_F+2^{24}(Z+|k|)]<2^{2048}(2^{-2100}+2^{-2175})
                                             <\sigma/4 .
$$
The straight line for the unperturbed field Lipschitz estimate stays
in the strip, so continuation gives this bound on the entire folded
path. The ordinary complex integral equation is holomorphic in the
angular input and in $k$ and the complex Banach input $z$. Indeed
on the smaller strip the field and its first angular derivative
are integrably bounded by the Wiener data and strip margin; Picard
iteration on pieces of small integrated Lipschitz norm converges
uniformly locally in these variables, with ordinary concatenation of
all original interfaces. Equivalently one may use complex lines in
$z$ for the Cauchy estimates below. The periodic terminal displacement
satisfies $\|P-\mathrm{Id}\|_{S_{s_F}}<2^{12}$: integrate
the unperturbed field (bounded by $6(16)^2+8(16)$) and (ASQ8.3).

Cauchy's formula therefore bounds by $M$ each first and second
derivative of this displacement in $k$, angular input, and unit
Banach $z$ directions, on
$Z,|k|\le\tau/4$, $|\operatorname{Im}\phi|\le s_F/2$.
For example two data directions may each use a circle of radius
$\tau/8$, and angular circles may have radius $s_F/8$; even
$2^{16}(8/\tau)^2$ is less than $M$. The degree-one constant of
$P'$ is included in the same $M$. This applies to the original
return, not a fitted flow on the real sample points.

By [W.3–5](R133-supplement-actual-physical-Wiener-conjugacy-strip.md),
$H'=1+h'$, $\|h'\|_{\mathcal A_{1/128}}<.017$ since its constant
is zero. The original inverse $g_0$ has analytic continuation to
$S_{1/512}$ with $|g'_0-1|<1/32$ and
$|\operatorname{Im}g_0(x+iy)|\le2|y|$ there. In fact at each real
$x$, solve $H(g_0(x)+v)=x+iy$ by
$v=iy-[h(g_0(x)+v)-h(g_0(x))]$ in $|v|\le1/256$.
The contraction factor is $<.017$ on the original strip and gives
the asserted bound. Local uniqueness glues the original inverse.

## The actual pivot and one full step

Let $r_0=s_F/16$ and $a=(2^{12}M)^{-1}$. On strips $r\le r_0$
work in the tube
$$
 Z+|k|+\|g-g_0\|_{S_r}+\|g'-g'_0\|_{S_r}\le a.          \tag{ASQ8.4}
$$
All states and lifts are real on the real circle. The composition
stays in $S_{s_F/2}$, $\|g'\|,\|(g'\circ R)^{-1}\|\le2$
and the Cauchy bounds above apply throughout. Put
$B=(P_k\circ g)/(g'\circ R)$ for this physical $z$-fibre.
At the exact seed CP.10 gives
$\langle B_*\rangle>.038736784-1.014851\,10^{-5}>1/32$
for the **candidate** $(h^a,1)$. By the explicit $M$ bounds and the
two denominator factors, the change of its mean from the exact seed
is at most $6Ma$ along (ASQ8.4). Thus
$$
                  \langle B\rangle>1/64,\qquad
                  \|B\|_{S_r}\le2M .                       \tag{ASQ8.5}
$$
This starts at the actual $Q_*$ and does not need to identify it with
the smaller CP.13 ball around a different state.

Set $E=P\circ g-g\circ R$ and $\epsilon=\|E\|_{S_r}$.
For $0<4d<r$, suppose $\epsilon d^{-3}\le(2^{22}M)^{-1}$.
We give the strip estimate for the **exact** inverse (ASQ6.3–4).
On $S_{r-d}$, $\|E'/J\|\le2\epsilon/d$, so
$\|\ell=\log(1+E'/J)\|\le4\epsilon/d$ on the branch at zero.
For the real data, $\lambda=e^{\langle\ell\rangle}>1/2$ and
$|\lambda-1|\le8\epsilon/d$.
Fourier coefficient bounds on a sup strip and PD.13 give a loss
of at most $16d^{-2}$ for $D_R^{-1}P_0$ in sup strips, and
$32d^{-2}$ for $(\lambda I-R^*)^{-1}_{\ne0}P_0$. Indeed the
first exact sum is bounded by
$136\sum_{n\ge1} n e^{-4nd}=136/[4\sinh^2(2d)]\le(17/2)d^{-2}$.
The weighted inverse adds at most $1/\sqrt\lambda$.
The estimate already projects the mean and never divides it.

Thus $\|u\|_{S_{r-2d}}\le128\epsilon d^{-3}=:b_0<1/16$.
There $\|w\|,\|\chi\|\le2$, $\|\chi-1\|\le2b_0$.
For $G$ evaluated on that strip, ASQ6.3 gives
$\|U(G)\|_{S_{r-3d}}\le64d^{-2}\|G\|$ and
$|d(G)|\le256d^{-2}\|G\|$ since $\langle w\rangle>1/2$.
Combining these estimates on the real means gives
$$
 |\mathfrak l_m G-\langle G\rangle|
       \le4096\epsilon d^{-3}\|G\| .
$$
For $G=B$, (ASQ8.5) implies $\mathfrak l_m B>1/128$.
For $F=-E/J$ the ASQ6 correction $(a_{\rm ph},\Delta k)$ therefore
satisfies $|\Delta k|\le512\epsilon$ and
$\|F-B\Delta k\|\le2^{11}M\epsilon$. Reconstructing the gauge and
then $\Delta g=g'a_{\rm ph}$ gives
$$
 \|\Delta g\|_{S_{r-3d}}\le2^{22}M d^{-2}\epsilon,\qquad
 |\Delta k|+\|\Delta g\|_{S_{r-4d}}+\|\Delta g'\|_{S_{r-4d}}
                         \le A d^{-3}\epsilon,
 \quad A=2^{24}M.                                          \tag{ASQ8.6}
$$
All correction functions are real on the real circle, and $\Delta g$
is periodic. ASQ6.2 gives the full first variation $-E$ in the raw
units, including the constant mode. On an admitted segment the
second variation on $S_{r-4d}$ costs at most
$M(|\Delta k|+\|\Delta g\|)^2$ by the complete complex $P_{kk},P_k',P''$
bounds. Hence
$$
               \epsilon_{\rm new}\le C d^{-4}\epsilon^2,
                  \qquad C=2^{52}M^3.                       \tag{ASQ8.7}
$$
The term $-g\circ R$ is linear. The second derivative here is in
the affine variables $(k,g)$ on this fibre, with both the metric
and state changing along the actual NP direction. No regular row
has been used as a substitute for the phase mean.

## A summable sequence with verified initial data

Start at $k_0=0,g=g_0$. Put $d_0=r_0/16$, $d_j=2^{-j}d_0$,
$r_{j+1}=r_j-4d_j$; their lower limit is $r_0/2$.
At the fixed input (ASQ8.1) exact conjugacy at $z=0$ and the
Cauchy data bound give $\epsilon_0\le M2^{-33000}$. Define
$e_j=16C d_j^{-4}\epsilon_j$. The actual powers
$d_0=2^{-2108}$, $C=2^{18052}$, $M=2^{6000}$
give $e_0\le2^{4+18052+8432+6000-33000}<1/4$.
Equation (ASQ8.7) then gives $e_{j+1}\le e_j^2$.
This also validates all the domains: suppose only the estimates
through $e_j$ have been established. For these same indices
$\epsilon_i d_i^{-3}=d_i e_i/(16C)<(2^{22}M)^{-1}$.
The sum of (ASQ8.6), including the pending correction, is at most
$A d_0/(8C)<a/4$. Together with $Z\le a/4$ this places every
straight correction segment inside (ASQ8.4) on its new strip,
before using (ASQ8.7) on that segment. This closes the induction.
In particular the increments of $k$, $g$ and $g'$ are absolutely
summable, while $e_j\le(1/4)^{2^j}$.

The limits on $S_{r_0/2}$ have the original degree, true phase
constant determined by this process, and positive real derivative.
Analytic composition is continuous in this strictly smaller input
tube, so the limit obeys (ASQ8.2) as a full function. The original
negative radius and its genuine means have never been projected
out. The scalar $k$ chooses one intrinsic metric per input and
does not furnish a flex by varying that metric. This result gives
an actual family of nearby roots for the nonlinear phase subsystem.
The NP trial has its original nonzero regular defect; (ASQ8.2) places
no bound on that defect or the ordinary finite complement. Solving
the physical waist, cap, holonomy and geometry conditions together
with the phase still requires the complete coupled inverse.
