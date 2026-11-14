# R133 supplement: an actual physical-angle fold and its complete Airy collar

2026-11-13, visible-exact / phase_inverse.

**Status: proved.** This is a new-object statement for the exact dyadic
reciprocal M256 candidate at amplitude $3/4$, accepted checkpoint 000,
and its complete intrinsic target on the original whole real affine
parameter interval. It constructs a genuine two-dimensional fold chart
through the true curvature root, proves a rectangular canonical domain,
and solves the complete linearized two-state equation there, with every
Fourier mode, both means, both boundary outputs and ordinary physical
two-dimensional $L^2$ sources retained.

There is one incoming port on the negative side and one unstable port on
the positive side. These are two scalar conditions for two states. The
zero Fourier mode is treated by its two independent ordinary equations.

The complete transformed matrix has norm less than $358259$. On the
actual inverse image of $|T|\le\delta$, $\delta=2^{-104}$, its full
$L^2$ perturbation norm is less than $0.010677$. In particular the local
inverse exists in the same two-dimensional $L^2$ space. Its ordinary
physical source-to-physical-state norm is less than $1.616803\cdot10^{-6}$.

These are curved physical boundary sections, defined by the actual fold.
This theorem does not identify the exterior fixed-radial sections or the
nonlinear regular cap relation, solve the complete body feedback, or
assert that the approximate candidate solves the nonlinear equations.
No old nonradial turning constant is transferred to this candidate.

## 1. The same complete physical object

Write the reciprocal variables as

$$
 u=B/C=\alpha U,\qquad v=1/C=s_\nu+\alpha V,
 \qquad s_\nu=1/C_{\mathrm{ref},\nu}.
 \tag{F.1}
$$

Here $U$ contains all 256 sine coefficients, $V$ contains its mean and
all 256 cosine coefficients, and their physical frequencies are $4j$.
All saved floating coefficients are interpreted as exact dyadic numbers.
The radial candidate is its full piecewise cubic polynomial, without
discarding any mode or coefficient.

The exact reciprocal Codazzi equations are

$$
\begin{aligned}
u_r&=\gamma(u u_\theta+K v v_\theta)
       -\beta u(1+u^2+Kv^2),\\
v_r&=\gamma(u v_\theta-v u_\theta)
       -\beta v(u^2-1+Kv^2).
\end{aligned}                                                   \tag{F.2}
$$

At any such candidate, including one with a nonzero residual, their
complete fixed-coordinate linearization is

$$
 h_r=\gamma[uI+vJ(K)]h_\theta+Lh+f,
 \qquad J(K)=\begin{pmatrix}0&K\\-1&0\end{pmatrix},       \tag{F.3}
$$
$$
\begin{aligned}
g&=\gamma v_\theta-2\beta uv,\\
L_{11}&=\gamma u_\theta-\beta(1+3u^2+Kv^2),\qquad L_{12}=Kg,\\
L_{21}&=g,\qquad
L_{22}=-\gamma u_\theta+\beta(1-u^2-3Kv^2).
\end{aligned}                                                   \tag{F.4}
$$

This is direct differentiation of (F.2); it does not use the candidate
equations to replace a derivative. Thus it does not omit a
residual-dependent coordinate variation. The source $f$ is the entire
physical two-component source. Metric-parameter derivatives, prescribed
data, and the original normalized residual multiplied by its actual
amplitude must all be included in $f$ when this inverse is used.

Use the constant matrix $R=\operatorname{diag}(-1,1)$ and put $y=Rh$.
Then (F.3) becomes

$$
 y_r=[dI+aJ(K)]y_\theta+\widetilde L y+\widetilde f,
 \quad d=\gamma u,\quad a=-\gamma v,
 \quad \widetilde L=RLR,\quad \widetilde f=Rf.             \tag{F.5}
$$

On the real domain $a>0$. The exact identity
$\widetilde L_{12}=K\widetilde L_{21}$ remains true. The coefficient
$a$ is allowed to depend on the physical angle. We do not remove $d$
and then pretend that the remaining principal coefficient is radial.

The true root enclosure from
[the actual-root calculation](../notes/2026-11-13-R133-actual-root-and-three-common-germs-native.json.gz)
is

$$
0.2383968742994\le r_*(\eta)\le0.2383968743003.            \tag{F.6}
$$

The entire root lies in one original scalar germ and one cubic candidate
piece. Their endpoints are saved exactly in the native reports. The
compact metric bump vanishes identically for $r>9/50$, so it vanishes on
the complete complex neighborhood used below. The candidate and its
actual fixed $\nu$ remain the same; this observation does not grant a
different candidate's coefficients.

## 2. A genuine joint complex domain

Let $R_0=10^{-5}$ and $\sigma=1/1024$. For each real parameter in the
original complete affine interval, use

$$
 |r-r_*(\eta)|\le R_0,\qquad |\operatorname{Im}\theta|\le\sigma.
 \tag{F.7}
$$

The executed coefficient calculation encloses this domain by the
complex radial rectangle with real interval
$[r_{*,-}-R_0,r_{*,+}+R_0]$ and imaginary interval $[-R_0,R_0]$.
It lies strictly inside the actual common scalar germ and the selected
candidate piece. No PPoly join is analytically continued across.

For clarity, the intrinsic analytic energy is constructed as follows.
Let $F_j$ be the complete finite Fourier coefficient vector of the
$j$th radial derivative of the original three-component primitive, and
let $e_j$ bound the complete omitted primitive in angular Wiener norm.
The exact finite zero convolution is bilinear:

$$
 \langle F_i\cdot F_j\rangle
   =\sum_n F_{i,n}\cdot F_{j,-n}.                         \tag{F.8}
$$

It uses no complex conjugation. If each component's finite Wiener norm
is bounded by $M_i$, the omitted complex product has modulus at most

$$
 3(M_i e_j+M_j e_i+e_i e_j).                            \tag{F.9}
$$

Adding this fee to both rectangular coordinates encloses the full
complex product. Consequently the actual analytic functions

$$
 E=\langle F_1\cdot F_1\rangle,\quad
 E'=2\langle F_1\cdot F_2\rangle,\quad
 E''=2\langle F_2\cdot F_2\rangle+2\langle F_1\cdot F_3\rangle
 \tag{F.10}
$$

are paid on the whole rectangle. The original complete primitive tail
uses $|r-\text{anchor}|+$ its radial Cauchy radius, so it covers the
complex rectangle as well as real radial boxes. The intrinsic radius
and its first three derivatives use the same exact scalar polynomial
germ and the same whole real affine parameter box.

The scalar formulas are

$$
 K=-\frac{a_{\rm phys}''}{a_{\rm phys}E}
       +\frac{a_{\rm phys}'E'}{2a_{\rm phys}E^2},\quad
 \gamma=\frac{\sqrt E}{a_{\rm phys}},\quad
 \beta=\frac{a_{\rm phys}'}{a_{\rm phys}},\quad
 s=-a_{\rm phys}\sqrt{\frac{E}{E-(a_{\rm phys}')^2}}.
 \tag{F.11}
$$

The complete complex enclosures put $a_{\rm phys}$, $E$,
$E-(a_{\rm phys}')^2$, and the quotient in the last square root in
the open right half-plane. Their indicated analytic branches therefore
exist throughout the domain. Differentiating (F.11) with the complete
jets gives the same exact $K'$ as on the real axis.

The finite candidate is evaluated by complex Horner arithmetic in its
one exact radial piece. If its sine/cosine coefficient at frequency
$4j$ is $c_j$, the full complex-strip derivative norm is bounded by
$\sum_j |c_j|(4j)^q e^{4j\sigma}$. This includes all coefficients,
the exact amplitude, and the complete radial scalar $s$. The mean of
$v$ is retained separately before estimating the nonconstant part.
In particular the negative real part of $v$ is proved before using
any reciprocal or characteristic branch.

The executed domain bounds include

| Complete joint-domain quantity | Strict bound |
| --- | ---: |
| $\operatorname{Re}K'$ | $>59.74380437$ |
| $|K'|$ | $<60.465470$ |
| $-\operatorname{Re}v$ | $>0.49902324$ |
| $\operatorname{Re}a$ | $>0.55866985$ |
| $|d|$ | $<0.919042$ |
| $|a|$ | $<2.343709$ |
| $|d_\theta|$ | $<5.747013$ |
| $|a_\theta|$ | $<5.524086$ |
| $|a\sqrt{k}|$ | $<18.278786$ |
| $\operatorname{Re}(a\sqrt{k})$ | $>4.25$ |
| $|(a\sqrt{k})_\theta|$ | $<43.082830$ |
| $\|\widetilde L\|_{\mathbb C^2\to\mathbb C^2}$ | $<18.744936$ |

Here the removable function

$$
 k(r,\eta)=\frac{K(r,\eta)}{r-r_*(\eta)}
   =\int_0^1 K'(r_*+t(r-r_*),\eta)\,dt                  \tag{F.12}
$$

has the same right-half-plane enclosure as $K'$. Convexity of the
rectangle justifies this enclosure for every point of (F.7).
Its square root is the positive one on the real root.

## 3. Construct the two true characteristic labels

Set $r=r_*-z^2$ and $Z=1/512$. For $|z|\le Z$, solve the two actual
holomorphic angular ODEs

$$
 \partial_z H_\pm(z,x)
 =2z\,d(r_*-z^2,H_\pm)
    \mp2z^2\,p(r_*-z^2,H_\pm),\quad
 H_\pm(0,x)=x,\quad p=a\sqrt{k}.                        \tag{F.13}
$$

All coefficients in this equation are those of (F.5). Let
$M_d,M_p,L_d,L_p$ be their complete modulus and angular derivative
bounds. Define

$$
 \epsilon=Z^2M_d+\frac23Z^3M_p,
 \qquad \lambda=Z^2L_d+\frac23Z^3L_p.                   \tag{F.14}
$$

The native bounds give

$$
 \epsilon<3.596658\cdot10^{-6}<\sigma/32,\qquad
 \lambda<2.213711\cdot10^{-5}<1/4,
 \qquad Z^2<R_0.                                      \tag{F.15}
$$

Picard iteration on holomorphic functions of $z$, with angular labels
in $|\operatorname{Im}x|\le15\sigma/16$ and displacement radius
$\epsilon$, maps the ball into itself and contracts by at most
$\lambda$. Integration may be taken along the straight complex radial
segment; its length bounds are exactly (F.14). Uniqueness patches these
solutions on the disk, and differentiation of the ODE gives

$$
 |\partial_xH_\pm-1|\le e^\lambda-1<1/4,
 \qquad |(\partial_xH_\pm)^{-1}|\le e^\lambda.           \tag{F.16}
$$

To invert, solve $x=\theta-(H_\pm(z,x)-x)$. The same angular margins
and (F.16) give a unique holomorphic inverse label $S_\pm(z,\theta)$
for $|\operatorname{Im}\theta|\le7\sigma/8$. It has
$|S_\pm-\theta|\le\epsilon$ and $|(S_\pm)_\theta|\le e^\lambda$.
Both labels have the original period as lifts, and real data give real
labels when $z,\theta$ are real.

The exact symmetry of (F.13), uniqueness, and the common root
normalization imply

$$
 S_+(-z,\theta)=S_-(z,\theta).                          \tag{F.17}
$$

Moreover $(S_\pm)_z(0)=0$ and their common quadratic term is
$-d(r_*,\theta)z^2$. The first difference is cubic:

$$
 S_\pm(z,\theta)=\theta-d(r_*,\theta)z^2
          \pm\frac23p(r_*,\theta)z^3+O(z^4).           \tag{F.18}
$$

Define

$$
 X=\frac{S_++S_-}{2},\quad W=\frac{S_+-S_-}{2}=z^3G.
 \tag{F.19}
$$

The function $G$ is holomorphic and even in $z$, with
$G(0,\theta)=2p(r_*,\theta)/3$. Its uniform bound is not obtained by
dividing a coarse quadratic displacement by a small cube. Indeed the
equations for the inverse labels give

$$
 (S_+-S_-)_z+F_+(S_+-S_-)_\theta
       =4z^2p(S_-)_\theta,                             \tag{F.20}
$$

where $F_+=2zd-2z^2p$. The backward $F_+$ characteristic from an
angle in $|\operatorname{Im}\theta|\le3\sigma/4$ moves by at most
$\epsilon$ and stays inside the inverse-label domain. Integrating
(F.20) and using (F.16) proves

$$
 |G|\le M_G:=\frac23M_pe^\lambda.
 \tag{F.21}
$$

Likewise $X-\theta=(r-r_*)H$ is holomorphic in $r$ and
$|H|\le M_H:=\epsilon/Z^2$. These are entire disk bounds on
$|r-r_*|\le Z^2$, $|\operatorname{Im}\theta|\le3\sigma/4$.

## 4. Division, the fold, and an actual rectangular inverse domain

Take $\rho=2^{-26}$ and $t=\rho/Z^2=1/256$. Cauchy's coefficient
bounds in the even variable give, throughout $|r-r_*|\le\rho$,

$$
 |G-G(0)|\le\frac{M_Gt}{1-t},\qquad
 |G_r|\le\frac{M_G}{Z^2(1-t)^2}.                        \tag{F.22}
$$

The first fee is less than $0.047789$. In particular
$\operatorname{Re}G>2.7893995$ on this entire complex domain.
There is therefore a single holomorphic branch

$$
 C=(3G/2)^{2/3},\qquad T=(r-r_*)C,
 \qquad W=\frac23(-T)^{3/2}\quad(r<r_*).                \tag{F.23}
$$

The last equality fixes the branch on the real negative side; the
first two expressions extend through $r=r_*$ to the elliptic side.
There is no fractional power singularity in $T(r,\theta)$.

For use below, put

$$
 C_-:=\tfrac12(3G_-/2)^{2/3},\quad
 C_+:=(3M_G/2)^{2/3},\quad
 C_r^+:=G_r^+/(3G_-/2)^{1/3},\quad C_\theta^+:=4C_+/\sigma.
 \tag{F.24}
$$

The factor $1/2$ in $C_-$ follows from
$|\arg G|<\pi/2$ and $\cos(2\arg G/3)>1/2$.
Thus $\operatorname{Re}C\ge C_-$ on the complex domain, not merely
on the real axis. On $|\operatorname{Im}\theta|\le\sigma/2$,

$$
\begin{aligned}
 |X_r|&\le M_H/(1-t)^2,&
 |X_\theta-1|&\le4\rho M_H/\sigma,\\
 \operatorname{Re}T_r&\ge C_--\rho C_r^+,&
 |T_r|&\le C_++\rho C_r^+,&
 |T_\theta|&\le\rho C_\theta^+.
\end{aligned}                                                   \tag{F.25}
$$

The native lower bound for the real part of the full Jacobian is

$$
 \operatorname{Re}\mathcal J
 =\operatorname{Re}(T_rX_\theta-X_rT_\theta)
 >1.26771220265,
 \qquad |\mathcal J|<6.969701.                          \tag{F.26}
$$

Local nonvanishing alone is not used as a global inverse theorem.
For a specified $(T,X)$, solve the two-variable equations

$$
 u=\frac{T}{C(r_*+u,\theta)},\qquad
 \theta=X-uH(r_*+u,\theta).                             \tag{F.27}
$$

Take $|u|\le\rho/4$, $|\theta-X|\le\sigma/8$,
$|T|\le T_b:=2^{-34}$, and $|\operatorname{Im}X|\le\sigma/4$.
The map sends the first disk into radius less than
$4.483414\cdot10^{-11}<\rho/4$ and the second into radius less than
$3.512362\cdot10^{-9}<\sigma/8$. In the weighted max norm with these
two radii, its derivative row sums are bounded by

$$
 \frac{T_b}{C_-^2}
    \left(C_r^++C_\theta^+\frac{\sigma/8}{\rho/4}\right)
 <0.032232,
 \qquad
 \frac{\rho/4}{\sigma/8}|X_r|+\frac{\rho M_H}{\sigma}
 <0.000044.                                            \tag{F.28}
$$

Banach's theorem consequently constructs a unique holomorphic inverse
on this entire canonical product domain. It is real for real data,
periodic as a lift in $X$, and stays within the one actual common germ.
This also proves global one-to-one identification of its real image.

The physical collar in this theorem is precisely

$$
 \Omega_\delta=\{(r,\theta):(T(r,\theta),X(r,\theta))
       \in[-\delta,\delta]\times\mathbb R/(\tfrac\pi2\mathbb Z)\},
 \qquad \delta=2^{-104}.                               \tag{F.29}
$$

Thus its image really is a rectangle. We have not extended a source
through an unproved curved boundary. The original-angle parametrization
of each boundary curve has

$$
 0.1819100<\left.\frac{dX}{d\theta}\right|_T
       =\frac{\mathcal J}{T_r}<5.494375.                 \tag{F.30}
$$

Both physical sections and both full traces are well defined. Any later
comparison with exterior constant-$r$ sections is an additional interface
calculation, not part of the rectangular Green argument below.

## 5. Exact principal normalization and the complete matrix

Write $D=\partial_r-d\partial_\theta$, $A=DT$, $C_0=DX$.
The actual characteristic label equations imply

$$
 A C_0+a^2K T_\theta X_\theta=0.                        \tag{F.31}
$$

With

$$
 A_T=A I-aT_\theta J(K),\quad
 \Delta=A^2+a^2K T_\theta^2,\quad
 b=\frac{a\mathcal J}{\Delta},
 \tag{F.32}
$$

changing independent variables in (F.5) gives the principal matrix
$bJ(K)$, and its determinant is exactly

$$
 b^2K=T,\qquad b^2=C/k.                                \tag{F.33}
$$

For example on the negative side (F.19), (F.23) give characteristic
labels $X\pm(2/3)(-T)^{3/2}$, whose canonical slopes are
$\pm\sqrt{-T}$. Alternatively, multiply
$-A_T^{-1}(C_0I-aX_\theta J(K))$ and use (F.31); its scalar part
vanishes and its $J(K)$ coefficient is $a\mathcal J/\Delta$.
Analytic continuation and cancellation of $r-r_*$ then give (F.33)
at the root as well.

The identities used here are also polynomial identities before dividing
by $\Delta$: the two null label gradients give zero mixed transformed
coefficient and transformed angular coefficient $T\Delta$; taking
determinants gives $T\Delta^2=a^2K\mathcal J^2$. Cancelling the known
simple factor $r-r_*$ yields $C\Delta^2=a^2k\mathcal J^2$ on the
entire domain. Its right-hand side is nonzero, so $\Delta$ cannot
vanish and (F.32) is legitimate everywhere.

Moreover $|\arg C|<\pi/3$ and the actual $K'$ enclosure gives
$|\arg k|<1/100$. Thus $C/k$ stays in the open right half-plane.
The branch $b=\sqrt{C/k}$ is holomorphic and positive on the real
domain; its agreement with (F.32) follows at the real root and hence
everywhere by analytic continuation. These identities also
give its quantitative lower bound before the source inverse is used:

$$
 |\Delta|\ge a_-\mathcal J_-/b_+>2.078117,
 \quad 0.1465318<|b|<0.340805,
 \quad \|A_T^{-1}\|<3.354132.                           \tag{F.34}
$$

Set

$$
 F=\operatorname{diag}(b^{-1/2},b^{1/2}),\qquad y=FU.
 \tag{F.35}
$$

The complete equation is exactly

$$
 U_T=J(T)U_X+\mathcal V U+g,
 \quad g=F^{-1}A_T^{-1}Rf,
 \tag{F.36}
$$
$$
 \mathcal V=F^{-1}A_T^{-1}\widetilde L F
       +J(T)(F^{-1}F_X)-F^{-1}F_T.                      \tag{F.37}
$$

In particular there is no scalarization that discards a state or
creates an unproved second radial derivative. If
$\widetilde g=\widetilde L_{21}$, the two off-diagonal entries are

$$
\begin{aligned}
 \mathcal V_{12}
   &=T\left[\frac{A\widetilde g+aT_\theta\widetilde L_{22}}
                    {b\Delta}+\tfrac12(\log b)_X\right],\\
 \mathcal V_{21}
   &=\frac{A\widetilde g-aT_\theta\widetilde L_{11}}
                    {b\Delta}+\tfrac12(\log b)_X.
\end{aligned}                                                   \tag{F.38}
$$

The upper-right entry therefore has an exact factor $T$. We do not
claim the two bracketed functions are equal: their difference includes
$aT_\theta\operatorname{tr}\widetilde L/(b\Delta)$.

For completeness, the derivative bounds used for the whole matrix are

$$
\begin{aligned}
 |(\log b)_r|&\le\tfrac12
   \left(C_r^+/C_-+\frac{k_+}{(R_0-\rho)k_-}\right),\\
 |(\log b)_\theta|&\le C_\theta^+/(2C_-),\\
 |(\log b)_T|&\le
   ((1+|X_\theta-1|)| (\log b)_r|+|X_r|| (\log b)_\theta|)/\mathcal J_-,\\
 |(\log b)_X|&\le
   (|T_\theta|| (\log b)_r|+|T_r|| (\log b)_\theta|)/\mathcal J_-.
\end{aligned}                                                   \tag{F.39}
$$

Here the bound for $k_r$ is Cauchy on its already established actual
complex disk. The resulting native bound on the complete inverse-chart
product domain is

$$
 \|F\|,\|F^{-1}\|<2.612367,\qquad
 \|\mathcal V\|<358258.324571=:M.                       \tag{F.40}
$$

This number is deliberately an upper bound for the whole matrix, not
just its principal part or its nonconstant angular part.

## 6. A full two-port Airy Green bound with no frequency loss

We prove the reference fact used here, independently of any old
nonradial native constants. Consider

$$
 U_T=J(T)U_X+g,\qquad -\delta\le T\le\delta,
 \quad 0<\delta\le1/16.                                \tag{F.41}
$$

For $m\in4\mathbb Z\setminus\{0\}$ put

$$
 \omega_m(T)=(|T|+|m|^{-2/3})^{1/2},\quad
 D_m(T)=\operatorname{diag}(\omega_m^{-1/2},\omega_m^{1/2}).
 \tag{F.42}
$$

The second state $u=U_{2,m}$ solves $u_{TT}=m^2Tu$, and
$U_{1,m}=i u_T/m$. These are two full state components, not a
height-only Green function.

### 6.1 Negative side, both complete rows

With $x=-|m|^{2/3}T\ge0$ the scalar equation is $u_{xx}+xu=0$.
For $x\ge1$ let

$$
 Z=\operatorname{diag}(x^{1/4},x^{-1/4})(u,u_x),\quad
 S=\begin{pmatrix}1&e\\e&1\end{pmatrix},\quad e=(4x^{3/2})^{-1}.
$$

The equation for $Z$ is
$Z_x=[\sqrt x(0,1;-1,0)+(4x)^{-1}\operatorname{diag}(1,-1)]Z$.
Its matrix satisfies $M^*S+SM=0$. Hence

$$
 (Z^*SZ)'=Z^*S'Z,\qquad
 \int_1^\infty\frac{|e'|}{1-e}\,dx=\log(4/3).           \tag{F.43}
$$

On $[0,1]$ the scalar two-state matrix has norm at most one,
so its propagator and inverse have norm at most $e$. The changes
between $x$ and $1+x$ weights cost at most $2^{1/4}$ each.
Using (F.43), or its determinant-one inverse, gives a bound less than
6 for the weighted fundamental matrix based at zero and its inverse.
Thus every two-point negative-side propagator, in the complete
$D_m$ state, is bounded by $36<64$. The common scalar
$|m|^{-1/6}$ and the permutation/unit phases connecting the two
weighted states cancel from the propagator.

### 6.2 Positive stable and unstable lines

Now put $x=|m|^{2/3}T\ge0$, so $u_{xx}=xu$. For $x\ge1$, the same
power weights and the orthogonal coordinates $(a_1,b_1)$ give

$$
 a_1'=\sqrt x\,a_1+\epsilon_x b_1,\qquad
 b_1'=\epsilon_x a_1-\sqrt x\,b_1,\qquad \epsilon_x=1/(4x).
 \tag{F.44}
$$

Construct the stable line by prescribing $a_1/b_1=0$ at $x=R$
and taking $R\to\infty$. Its Riccati equation is
$r'=2\sqrt x\,r+\epsilon_x(1-r^2)$. The interval
$[-1/4,1/4]$ is invariant backward for $x\ge1$; the difference
of two such solutions contracts backward by the positive coefficient
$2\sqrt x-\epsilon_x(r_1+r_2)$. This proves convergence on every
compact interval and defines the actual stable solution $A$.
Its $b_1$ component decreases forward and never vanishes.

The growing line $B$ is defined by $a_1(1)=1,b_1(1)=0$.
The ratio $b_1/a_1$ stays in $[0,1/4]$ forward, and its $a_1$
component increases. The two line ratios have product of modulus at
most $1/16$. Consequently the stable forward and unstable backward
projection kernels have norm at most

$$
 \frac{1+1/16}{1-1/16}=17/15                            \tag{F.45}
$$

in the $x$ power weights on $x\ge1$. Passage to the $(1+x)$ weights
makes this less than 2. On $[0,1]$, direct two-state propagation in
these weights costs less than $\sqrt2e<4$ in each direction.
Inserting these two comparisons proves that both split kernels are
bounded by 32 for every allowed pair of positive times, including
both points in $[0,1]$ and either point on its boundary.

Denote these complete kernels by $P_A(T,S)$ for $T\ge S$ and
$P_B(T,S)$ for $T\le S$. At $T=\delta$ normalize $B$ to unit
$D_m$ norm. Its coefficient in the $(A,B)$ basis is the positive
unstable input port. This definition does not invert any exponentially
small transmission entry.

### 6.3 The negative incoming condition and the full source

At $T=-\delta$ define the negative incoming port to be

$$
 \mathfrak i_m(U)=\big((D_mU)_1+(D_mU)_2\big)/\sqrt2.
 \tag{F.46}
$$

The reference system conserves the Hermitian flux $U^*\Sigma_1U$,
$\Sigma_1=(0,1;1,0)$, because
$(imJ(T))^*\Sigma_1+\Sigma_1(imJ(T))=0$.
The stable Airy solution has $U_1$ purely imaginary and $U_2$ real
up to a common complex scalar. Thus it is isotropic for this flux,
and the modulus of (F.46) on that solution is exactly
$\|D_mU\|/\sqrt2$.

Normalize the stable solution $A$ to unit $D_m(0)$ norm.
The negative two-sided propagator gives
$|\mathfrak i_m(A)|\ge1/(64\sqrt2)$. The stable column with negative
incoming value one is therefore bounded by

$$
 \sup_T\|D_m(T)P_{-,m}(T)\|<64^2\sqrt2<8192.            \tag{F.47}
$$

For zero source-port data first define on the positive half

$$
 V(T)=\int_0^T P_A(T,S)g(S)\,dS
              -\int_T^\delta P_B(T,S)g(S)\,dS.         \tag{F.48}
$$

This sets its stable coefficient at zero to zero and its unstable
coefficient at $\delta$ to zero. Continue it to the negative half by
the complete Cauchy propagator based at zero and the negative source.
The resulting full kernel has balanced norm at most $64\cdot32=2048$.
Finally subtract $P_{-,m}\mathfrak i_m(V(-\delta))$.
This enforces the one negative incoming condition. The zero positive
unstable condition is preserved because the correcting column is stable.

This construction yields a full zero-port kernel bounded by
$(1+8192)2048<2^{25}$ in the balanced two-state norm. A nonzero
positive unstable input is first propagated backward on its normalized
$B$ line, then corrected in exactly the same way at the negative
incoming port; its full column has the same $2^{25}$ bound.
The negative input column has (F.47). Thus

$$
 \|D_m(T)G_m(T,S)D_m(S)^{-1}\|\le K_A:=2^{25},
 \qquad \|D_m(T)P_{\pm,m}(T)\|\le K_A.                 \tag{F.49}
$$

The intermediate continuation in (F.48) is only a particular solution.
We have not imposed both negative Cauchy traces and then a third
positive condition. Uniqueness follows because a zero positive
unstable solution is on the stable line and its negative incoming
coefficient is nonzero unless the solution is zero.

### 6.4 Mean and the unbalanced two-dimensional estimate

For $m=0$ use $D_0=I$ and the exact equations $U'_0=g_0$.
The independent inputs are $U_{1,0}(-\delta)$ and
$U_{2,0}(\delta)$. The solutions are respectively their left-to-right
and right-to-left integrals. Both complementary endpoint values are
outputs. This gives kernel and individual column bounds at most one,
so it is included in (F.49). No limit $m\to0$ is taken in (F.42).

For nonzero $m$ and $0<|T|\le\delta\le1/16$,
$\omega_m(T)<1$ and $\omega_m(T)\ge\sqrt{|T|}$.
Both $D_m$ and its inverse therefore have norm at most
$|T|^{-1/4}$. With

$$
 w(T)=1+|T|^{-1/4},\qquad
 W_2=\int_{-\delta}^{\delta}w(T)^2\,dT
     =2\delta+\frac{16}{3}\delta^{3/4}+4\sqrt\delta,
 \tag{F.50}
$$

(F.49) implies the complete Fourier operator kernel bound
$K_Aw(T)w(S)$. At $T=0$ the scalar bound is interpreted almost
everywhere; $w$ belongs to $L^2$ and no singular point trace is claimed
from this unbalanced majorant. Cauchy--Schwarz in the physical radial
variable proves

$$
 \|G_0\|_{L^2_{T,X}\to L^2_{T,X}}\le K_AW_2=:B,
 \qquad
 \|P_0\|_{\ell^2\oplus\ell^2\to L^2_{T,X}}
       \le K_A\sqrt{2W_2}=:P.                          \tag{F.51}
$$

All Fourier modes are included simultaneously. The source uses the
ordinary $dT\,dX$ measure, with no angular width loss. At each actual
endpoint the balanced source trace is bounded by
$K_A\sqrt{W_2}$; combining both full endpoint states costs $\sqrt2$.

## 7. Absorb the whole actual matrix and pay the physical source

Apply (F.51) to (F.36):

$$
 U=P_0\mathfrak g+G_0(g+\mathcal VU).                   \tag{F.52}
$$

The pointwise matrix norm (F.40) acts boundedly on the complete
two-dimensional $L^2$ space. It includes every low-high, mean-nonmean,
and cross-state interaction. At the stated $\delta$, the native
calculation gives

$$
 B<2.980232298\cdot10^{-8},\quad
 P<1.414213577,\quad
 BM<0.010676931<1/8.                                   \tag{F.53}
$$

Ordinary Banach inversion on this one space gives a unique complete
solution with

$$
 \|U\|_{L^2}\le
    3.012395435\cdot10^{-8}\|g\|_{L^2}
       +1.429475993\|\mathfrak g\|_{\ell^2\oplus\ell^2}.
 \tag{F.54}
$$

The two full balanced endpoint outputs have the explicit bound

$$
 \|\mathrm{Tr}_{\pm}U\|
 \le K_A\sqrt{2W_2}(1+M B/(1-BM))\|g\|_{L^2}
  +\left[2K_A+K_A\sqrt{2W_2}M P/(1-BM)\right]\|\mathfrak g\|.
 \tag{F.55}
$$

Their native constants are respectively less than $1.429475993$ and
$67833114$. This includes the two independent mean outputs.

The exact two-dimensional source change is paid using (F.26), (F.34),
(F.35), without identifying anisotropic Sobolev norms across a mixed
radial/angular map:

$$
 \|g\|_{L^2(dT\,dX)}
    \le \|F^{-1}\|\|A_T^{-1}\|\sqrt{\mathcal J_+}
                \|f\|_{L^2(dr\,d\theta)}
    <23.132428\|f\|_{L^2(dr\,d\theta)},                 \tag{F.56}
$$
$$
 \|h\|_{L^2(dr\,d\theta)}
   \le\|F\|/\sqrt{\mathcal J_-}\,\|U\|_{L^2(dT\,dX)}
   <2.320191\|U\|_{L^2(dT\,dX)}.                       \tag{F.57}
$$

Combining these gives

$$
 \boxed{\quad
 \|h\|_{L^2(\Omega_\delta)}
 <1.616803\cdot10^{-6}\|f\|_{L^2(\Omega_\delta)}
       +3.316658\|\mathfrak g\|.
 \quad}                                                \tag{F.58}
$$

The physical boundary fields themselves are reconstructed by
$h=RFU$ on the two actual curves. Their $L^2(d\theta)$ trace changes
are bounded by (F.30) and the full matrix $F$.
In particular original means are the complete integrals

$$
 \frac2\pi\int_{\mathbb R/(\pi/2\mathbb Z)}
       RF(T,X)U(T,X)\,\frac{T_r}{\mathcal J}(T,X)\,dX.
 \tag{F.59}
$$

This weighted expression is retained. It is not replaced by the
canonical zero Fourier coefficient. The original physical mean paths
are therefore present even when the coordinate or frame mixes them
with nonzero modes.

## 8. A specified higher-order canonical staircase

The same inverse exists on the entire complex $X$ strip $\sigma/4$.
The complete coefficient matrix there has the same bound $M$.
For $j\ge1$, Cauchy's estimate, with the smaller half-strip if needed,
gives

$$
 M_j:=\|\partial_X^j\mathcal V\|_\infty
       \le j!(8/\sigma)^jM.                            \tag{F.60}
$$

The reference Green and both port columns commute with $\partial_X$.
Difference quotients first justify differentiating (F.52); induction
then gives, for every integer $q$ with the indicated data,

$$
\begin{aligned}
 \|\partial_X^qU\|_{L^2}
 \le\frac1{1-BM}\bigg[
 B\|\partial_X^qg\|_{L^2}+P\|\partial_X^q\mathfrak g\|
 +B\sum_{j=1}^q{q\choose j}M_j
             \|\partial_X^{q-j}U\|_{L^2}\bigg].
\end{aligned}                                                   \tag{F.61}
$$

This is a triangular induction after one actual same-space inversion;
it does not repeatedly spend an angular strip. The report evaluates
all coefficients through $q=6$, with source constants for the
$q$th derivative less than, respectively,

$$
 (3.013\cdot10^{-8},\ 2.694\cdot10^{-6},\ 0.044111,
   1095.766,\ 3.629354\cdot10^7,\ 1.502627\cdot10^{12},
   7.465420\cdot10^{16}).                               \tag{F.62}
$$

Each displayed constant multiplies the sum of the supplied source
derivative norms through that order; independent port constants are
also saved. Finite sums give the corresponding full Sobolev norms.
For $q>0$, the source here is the actual pulled-back $g(T,X)$ with its
stated $X$ derivatives. Since the chart mixes $r$ and $\theta$, this
does not grant a free bound from only physical angular derivatives
of an arbitrary source. Equations (F.56)--(F.58) require only the
ordinary physical two-dimensional $L^2$ source and have no such
additional assumption.

## 9. Actual execution and the remaining exterior interfaces

The complex germ was executed by
`scripts/fourfold_codazzi_turning_complex_germ.py`; its report is
`notes/2026-11-13-R133-actual-alpha075-complex-turning-germ.json.gz`.
All six original coefficient gates passed in 6.74 seconds.
The fold, rectangular inverse, complete matrix, source and all-mode
Green budget were then executed by
`scripts/fourfold_codazzi_actual_fold_Airy_contract.py`; its report is
`notes/2026-11-13-R133-actual-alpha075-fold-Airy-contract.json.gz`.
All 16 gates passed. The sources and reports record the full input
identities and exact parameter intervals.

The candidate SHA-256 is
`45923b3675d2789376361192c6e0841e82914e27605d362872d5ac1dcf7a628e`.
It is recovered according to
[the complete accepted-checkpoint reconstruction record](../notes/2026-11-13-R133-reciprocal-m256-exit137-and-complete-resume.md),
using its original producer, complete accepted checkpoint and lossless
Hermite reconstruction. The large reproducible intermediate candidate
is not duplicated by this result. Pass its actual recovered path
explicitly:

```sh
python3 scripts/fourfold_codazzi_turning_complex_germ.py \
  --candidate /path/to/reciprocal-m256-alpha075-accepted000-candidate.json \
  --out /tmp/actual-alpha075-complex-turning-germ.json.gz
python3 scripts/fourfold_codazzi_actual_fold_Airy_contract.py \
  --germ /tmp/actual-alpha075-complex-turning-germ.json.gz \
  --out /tmp/actual-alpha075-fold-Airy-contract.json.gz
```

The actual coefficient and fold reports have SHA-256 values
`bec7db3231da76476217f3bd27e976e73be5a14c9c0425264fbf440e8fcb5ff7`
and
`78d3677e7c664d8a0285cf543fff59c02845096b14740970f05ab7d308208b72`
respectively.

The single-germ construction never crosses a PPoly interface. All
exterior jumps must still be supplied at their actual locations when
this module is attached to a larger body. Likewise the positive
unstable port is not silently set equal to the nonlinear tail's
regular graph, and the negative incoming port is not silently equal
to a waist condition. These complete port outputs are available for
that exterior Schur problem, which is not proved here.
