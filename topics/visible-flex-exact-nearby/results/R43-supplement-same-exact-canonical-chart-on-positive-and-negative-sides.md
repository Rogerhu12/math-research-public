# R43 supplement: the same exact canonical chart on both sides of the root

**Proved for the actual complete family.** The exact characteristic chart
already used on the negative side has a real positive-side continuation, with
the same height, root angle and potential. It is a real diffeomorphism on
both sides, and its holomorphic inverse contains the full product domain

$$
 \operatorname{dist}\bigl(\xi,[-L,L]\bigr)\le\varepsilon,
 \qquad |\operatorname{Im}\phi|\le\sigma,
 \quad L=\frac1{4000},\quad\varepsilon=\frac1{100000},
 \quad\sigma=\frac1{40000}.                                  \tag{T.1}
$$

The entire actual potential satisfies $|V|<752813.541687$ there. Its radial
derivative has the bound $|V_\xi|<7.528136\,10^{10}$ on **real**
$-L\le\xi\le L$ and the same complex angular strip, rather than on the
boundary of the radial halo. This statement includes every angular mode, the
mean and every parameter in

$$
 p_5=-7789843107295549/4611686018427387904,
 \qquad |p-p_5|\le10^{-9}.
$$

On the positive side set $s=r-t(p)=-\rho$ and $y=-\xi$. The positive
canonical operator is exactly

$$
 P_+=-\partial_y^2-y\partial_\phi^2-V(-y,\phi).              \tag{T.2}
$$

The zero-two-trace form of (T.2) on $[0,L]$ is coercive with relative
constant greater than $.995232752555$. This is a finite-collar Dirichlet
conclusion. No positive Cauchy evolution bound, full-cap contact estimate or
Ai reflection estimate is inferred from it.

## 1. The exact fields and the symmetry that makes the positive chart real

All inputs are the already completed full physical bidisk, with
$R=279/10^6$, physical field strip $11/5000$, and characteristic start
strip $S_1=3/2000$. The same complete seven-field report, parameter transfer,
moving root and original grounded density are used. The full-root-potential
supplement proves, on this bidisk,

$$
 k=(2U_0)^{-1},\qquad
 D_\pm=\partial_z+(2zq\mp2z^2k)\partial_\theta,
 \quad z^2=\rho,
$$
$$
 D_\pm T_\pm=0,\qquad T_\pm(0,\theta)=Y_0(\theta),\qquad
 F_\pm=kT_{\pm,\theta},\qquad
 D_\pm F_\pm=2z\mathcal C F_\pm,
 \quad F_\pm(0)=1.                                         \tag{T.3}
$$

The two exact solutions obey $T_+(-z)=T_-(z)$. Thus

$$
 \phi=\frac{T_++T_-}{2},\qquad
 \Delta=\frac{3(T_+-T_-)}{4z^3},\qquad
 \xi=\rho\Delta^{2/3}                                      \tag{T.4}
$$

are holomorphic in $\rho$. The removable value of $\Delta$ at zero is one.
Their Taylor coefficients in $\rho$ are real on the real angular circle:
the coefficients of (T.3), its initial value and its unique power-series
solution have this reality property. Consequently $\phi$ and $\Delta$ are
real also when $\rho<0$.

More explicitly, at $z=i\sqrt{|\rho|}$ complex conjugation and the exact
branch symmetry give

$$
 \overline{F_+(z,\theta)}=F_+(-z,\theta)=F_-(z,\theta)
 \qquad(\rho<0,\ \theta\ \hbox{real}).                      \tag{T.5}
$$

This is the required positive-side relation. It is not an assertion that
the two signed characteristics remain real on that side.

Write $C=M_{\mathcal C}$ and $e=e^{CR}-1$. The complete complex estimates
already proved from (T.3) are

$$
 |F_\pm-1|\le e<.028750705256,\qquad
 e^{-CR}\le|F_\pm|\le e^{CR},\qquad |\Delta-1|\le e.        \tag{T.6}
$$

They hold along the full nested complex paths, not only at radial or angular
nodes. In particular the real $\Delta$ is strictly positive on both sides.
The branch of $\Delta^{2/3}$ is the same branch fixed at the root.

## 2. A genuine two-sided real inverse

The exact differential identities are

$$
 \phi_\theta=\frac{F_++F_-}{2k},\qquad
 J_\Psi=\det D_{\rho,\theta}(\xi,\phi)
       =\Delta^{-1/3}\frac{F_+F_-}{k},                     \tag{T.7}
$$
$$
 \left.\xi_\rho\right|_\phi
 =2\Delta^{-1/3}\frac{F_+F_-}{F_++F_-}.                    \tag{T.8}
$$

At real $\rho<0$, (T.5) makes $F_+F_-=|F_+|^2>0$, while
$(F_++F_-)/2=\operatorname{Re}F_+\ge1-e>0$. Also $k>0$ because the full
physical bidisk certificate proves $\operatorname{Re}U_0>0$. The same
signs on real $\rho\ge0$ follow from the real positive exponential in
(T.3). Therefore every quantity in (T.7)–(T.8) is positive on the whole
real interval $[-R,R]$.

For each fixed $\rho$, $\theta\mapsto\phi$ has its unchanged degree-one
periodic lift and is a diffeomorphism of the complete actual quarter circle.
After solving its angular equation, (T.8) says that $\xi$ is strictly
increasing in $\rho$ at fixed $\phi$. At the two radial endpoints,
(T.4) and (T.6) give

$$
 |\xi(\pm R,\phi)|\ge R(1-e)^{2/3}
       >.000273626411094195.                               \tag{T.9}
$$

This proves that the unique real inverse contains
$[-L,L]\times\mathbb S^1_\phi$. Its radial starting points obey

$$
 |\rho|\le \frac{L}{(1-e)^{2/3}}
             <.000254909603649294.                         \tag{T.10}
$$

The stronger negative-side real weighted-average bound
$\Delta\ge e^{-CR}$ was not used in (T.9)–(T.10): it does not follow on
the positive side from a real characteristic flow. The full complex bound
$\Delta\ge1-e$ is sufficient.

The directed consumer gives complete real bounds

| Quantity | Lower bound | Upper bound |
|---|---:|---:|
| $\phi_\theta$ | $.0509989385250$ | $.307346224028$ |
| $\left.\xi_\rho\right|_\phi$ | $.962911718560$ | $1.100303944722$ |
| $J_\Psi$ | $.0491481015106$ | $.319272212854$ |

For example the radial lower bound uses the exact inverse identity
$\rho_\xi=\Delta^{1/3}(F_+^{-1}+F_-^{-1})/2$ and
$|\rho_\xi|\le e^{4CR/3}$. The radial upper bound follows directly from
(T.8) as $e^{2CR}(1-e)^{-4/3}$. Thus the bounds do not use a positive-side
analogue of the negative real harmonic-mean estimate without proof.

## 3. The same complete complex product domain

On the physical half strip $|\operatorname{Im}\theta|\le S_1/2$, the
already proved complex inverse-differential estimates are

$$
 |\rho_\phi|<.146492885,\quad
 |\theta_\phi|<20.336569168,\quad
 |\rho_\xi|<1.038516804,\quad
 |\theta_\xi|<5.158920726.                                  \tag{T.11}
$$

These are estimates on the complete physical disk $|\rho|\le R$; their
proof never required the radial center to be positive. Starting at the new
real inverse (T.10), lift a canonical angular segment of length at most
$\sigma$, followed by a canonical radial segment of length at most
$\varepsilon$. Equation (T.11) bounds their total physical movements by

$$
 |\delta\rho|<.000014047490153,
 \qquad |\delta\theta|<.000560003437.
$$

The remaining strict margins are

$$
 R-\frac{L}{(1-e)^{2/3}}-|\delta\rho|
       >1.0042906197\,10^{-5},\qquad
 S_1/2-|\delta\theta|>.000189996563.                         \tag{T.12}
$$

Thus continuation of the local inverse cannot leave its paid physical
domain or encounter a zero of the Jacobian. The inverse differential is the
inverse of the derivative of one holomorphic map, so it is integrable.
The inverse germs agree on overlapping neighborhoods by continuation from
the unique real inverse. Working on the periodic lift first gives the full
simply connected rectangle; the original degree-one periodicity then gives
the actual circle. This proves (T.1).

The complete second-order removable potential quotient of the full-root
supplement is holomorphic on the entire physical bidisk. Its modulus bound
there is independent of the sign of $\rho$. Composing with this new inverse
therefore gives the stated bound for $V$ on (T.1). A radius-$\varepsilon$
radial disk about every real $\xi\in[-L,L]$ is contained in (T.1), which
gives the stated $V_\xi$ bound by Cauchy. No such radius is asserted at the
radial halo boundary.

## 4. The actual principal density, positive height and ordinary source

Let $\mathcal U$ denote the **grounded** physical determinant factor of the
existing log-density certificate. It is distinct from the seven-field
$U_0$. Its exact formula is

$$
 \mathcal U=Q F_z^4\,\operatorname{area}^2/\operatorname{support}^4,
 \qquad |\log\mathcal U|<1.665294041858.                    \tag{T.13}
$$

Here $\operatorname{area}=|F_\theta\times F_r|^2$, with its analytic
complex extension. The common full domain proves the logarithm branches
and their real positivity before the quotients are formed.

The exact transformed principal density is

$$
 \alpha_c\operatorname{diag}(1,-\xi),\qquad
 \alpha_c=\sqrt{\mathcal U}\,\Delta^{-1/3},\qquad
 w=\tau U,\quad\tau=\alpha_c^{-1/2}.                       \tag{T.14}
$$

The matrix identity already holds on an open negative-side set. All its
coefficients in (T.14) extend holomorphically through the root with the
branches just fixed, so the identity theorem gives it on the same full
bidisk. On $y=-\xi$, $s=-\rho$, the two reversals leave the coordinate
Jacobian positive and turn this density into
$\alpha_c\operatorname{diag}(1,y)$. Its height conjugation gives exactly
(T.2), including the **minus** sign before $V(-y,\phi)$ in the positive
form convention.

The same complete logarithm gives

$$
 |\log\alpha_c|\le\tfrac12M_{\log\mathcal U}
                  -\tfrac13\log(1-e)<.842371055406.
$$

In particular, on both real sides,

$$
 .430688126417<\alpha_c<2.321865727570,
 \qquad .656268334157<\tau<1.523766953170.                   \tag{T.15}
$$

For a grounded ordinary equation $-\operatorname{div}(B\nabla w)=f_g$,
write $\Psi_+(s,\theta)=(y,\phi)$ and $J_+=\det D\Psi_+>0$. The exact
coordinate and height law is

$$
 P_+U=\left(\frac{\tau}{J_+}f_g\right)\circ\Psi_+^{-1}.
                                                               \tag{T.16}
$$

At the root the canonical outward conormal is
$p_{\rm out}=-U_y=U_\xi$. The grounded conormal still contains the true
height shear:

$$
 p_{g,\rm out}
  =-\alpha_c\,\partial_y(\tau U)
  =\sqrt{\alpha_c}\left[-U_y+\tfrac12
                  (\partial_y\log\alpha_c)U\right].       \tag{T.17}
$$

Piola then converts this density by the actual angular Jacobian. The
unnormalized conormal integrals agree; normalized means retain the actual
period ratio. Equations (T.16)–(T.17) do not identify a tilted mixed
radial-angular source norm with an original physical Bochner norm.

## 5. A complete finite positive Dirichlet bound, with the mean included

On the actual canonical $[0,L]$ define

$$
 E_0(u)=\int_0^L\!\!\int
          (|u_y|^2+y|u_\phi|^2),\qquad u(0)=u(L)=0.
$$

For every angle the exact one-dimensional Dirichlet Poincare inequality is
$\int|u|^2\le L^2\pi^{-2}\int|u_y|^2$. Therefore the full actual form
of (T.2) satisfies

$$
 \mathfrak e_+(u,u)
 =E_0(u)-\int V(-y,\phi)|u|^2
 \ge (1-\eta)E_0(u),
 \quad\eta=\frac{L^2M_V}{\pi^2}<.004767247445.              \tag{T.18}
$$

The real potential is bounded, and (T.18) gives a coercive closed form on
the weighted-energy completion with both zero traces. The Riesz
representation theorem gives its unique inverse. For an ordinary
$f\in L^2(dy\,d\phi)$ the same estimate and Cauchy–Schwarz give

$$
 \|P_+^{-1}f\|_{L^2}
 \le\frac{L^2}{\pi^2(1-\eta)}\|f\|_{L^2}
 <6.362907533\,10^{-9}\|f\|_{L^2}.                         \tag{T.19}
$$

No Fourier projection appears in this proof, so it includes the mean,
opposite signs, arbitrary mode mixing by $V$, and all finite or infinite
head/tail crossings. The boundary condition at $L$ in this subsection is
explicitly zero Dirichlet. It is not the boundary condition of the full
positive cap. In particular its inverse cannot replace the full-cap
Poisson/contact realization.

## 6. Executed files and remaining connection

The consumer is
`scripts/fourfold_root_twosided_canonical_domain.py`, SHA256

    4b78e63a2a0f7abb405352cdf66784e8e7f9aadf989bff1015b2cf5683419d65

and its actual directed report is
`notes/2026-11-13-root-twosided-canonical-domain.json`, SHA256

    aad891d208bafc758b0aa7aeff1415296fcdf8bf2929df6e5cc2ad48c706f2c6

Reproduce from the topic directory, supplying a fresh output path:

```bash
python3 scripts/fourfold_root_twosided_canonical_domain.py \
  --out notes/2026-11-13-root-twosided-canonical-domain.json
```

The consumer checks the frozen input producers, dependencies, byte hashes
and the whole true family identity. It does not rerun any large native
field calculation. This result authorizes the same exact canonical
potential and root frame on the positive side. The full-cap ordinary
source/contact norms, its regular and mean slots, positive Ai residual and
Cayley inverse, parameter derivatives and the full returned strong
remainder still require their own complete consumers.
