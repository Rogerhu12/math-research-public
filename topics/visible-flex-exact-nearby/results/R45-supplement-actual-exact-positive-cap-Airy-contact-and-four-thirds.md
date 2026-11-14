# R45 supplement: actual exact positive-cap contact and full Airy 4/3 reflection

**Proved for the same complete actual cap and parameter family.** In the
exact two-sided canonical chart, the whole positive cap has the local source
and contact bounds

$$
 C_s<140.771775,\qquad C_w<70.378782.                         \tag{A.1}
$$

These constants include the root mean, the regular mean and its contact,
the full uncompressed body and the true infinite-tail Robin form. Sources
are supported in the actual canonical collar $0\le y\le H=1/4000$;
the solution still occupies the entire cap.

In the **original R39 root Airy frame**, with a balanced regular scalar
port, let $R_+$ be the complete augmented reflection and set
$\mathcal L=\operatorname{diag}(\langle D_\phi\rangle,1)$. Then

$$
 \boxed{\quad
 \|(R_++I)\mathcal L^{4/3}\|,
 \quad\|\mathcal L^{4/3}(R_++I)\|
       <7.698072853\,10^{11}.
 \quad}                                                     \tag{A.2}
$$

Both norms are on $L^2(\mathbb S^1_\phi)\oplus\mathbb C$. Thus
$R_++I:H^s\oplus\mathbb C\to H^{s+4/3}\oplus\mathbb C$ has this bound
for $-4/3\le s\le0$. The root mean and regular input columns are retained,
with all of their infinite output rows. The ordinary local source to the
actual affine outgoing wave has norm below $377.600482$; the corresponding
weak-source norm is below $188.781182$.

This result does not solve the final regular-mean compatibility equations,
provide the full larger Sobolev window or a nonzero same-width angular
weight, or close the complete returned inverse. It does supply an actual
full-cap $-I+R_{4/3}$ factor with its complete local source column.

## 1. Same object, exact chart, full realization and actual periods

The parameter family is unchanged:

$$
 p_5=-7789843107295549/4611686018427387904,
 \qquad |p-p_5|\le10^{-9},\qquad \rho=t(p)-r.
$$

The preceding two-sided-chart supplement proves the same exact canonical
coordinates through the root and gives, on the positive side,

$$
 s=r-t(p)=-\rho,\quad y=-\xi,\quad
 P_+=-\partial_y^2-y\partial_\phi^2-V(-y,\phi),
 \quad |V|<752813.541687.                                   \tag{A.3}
$$

The full bound is on the product
$\operatorname{dist}(\xi,[-H,H])\le10^{-5}$,
$|\operatorname{Im}\phi|\le1/40000$. There is **no principal matrix
error** in (A.3). This is not R87's finite approximate positive chart,
whose nonzero principal error would require additional residual terms.
The original grounded height is $w=\tau U$, with

$$
 \tau=\alpha_c^{-1/2},\qquad
 \alpha_c=\sqrt{\mathcal U}\,\Delta^{-1/3},\qquad
 C_0=\operatorname{diag}(1,y).                              \tag{A.4}
$$

R74/R94's complete positive-cap realization, its nonnegative actual
infinite-tail Robin form, and its independent regular mean constraint are
used without change. The consumer checks their input bytes, producer,
dependencies, original affine origin/direction, and parameter inclusion.
The older full-cap parameter box contains the entire box above.

Use the actual canonical quarter circle and its physical frequencies
$\lambda_n=q_c|n|$, where

$$
 38.8838516058692<q_c<38.8838516230918.                       \tag{A.5}
$$

The scalar regular basis is the unit $L^2$ constant on the physical quarter
circle of length $\ell_\theta=\pi/2$. Passing from the old full physical
circle's fourfold subspace to this quarter circle uses the unitary
restriction $f\mapsto2f$. The energy, source pairings and normalized
regular coefficient transform together. The already proved regular
extension energy is consequently unchanged:

$$
 E_{\rm reg}<50.912957.                                    \tag{A.6}
$$

The true period factor in (A.5) is retained throughout. There is no second
extra factor four in the quarter-circle Fourier multiplier.

## 2. Complete native first jets of the actual grounded density

Write

$$
 C=F_\theta\times F_r,\quad A=C\cdot C,\quad B=C\cdot F,
 \qquad \mathcal U=QF_z^4A^2/B^4.
$$

Here $Q$ is the actual deflated curvature factor, and $\mathcal U$ is
distinct from the seven-field $U_0$. Let

$$
 C_r=F_{r\theta}\times F_r+F_\theta\times F_{rr},\qquad
 C_\theta=F_{\theta\theta}\times F_r+F_\theta\times F_{r\theta}.
$$

Using $C\cdot F_r=C\cdot F_\theta=0$ and
$\partial_\rho=-\partial_r$ gives the exact formulas

$$
 \begin{split}
 (\log\mathcal U)_\rho
  &=Q_\rho/Q-4F_{r,z}/F_z-4(C\cdot C_r)/A+4(C_r\cdot F)/B,\\
 (\log\mathcal U)_\theta
  &=4F_{\theta,z}/F_z+4(C\cdot C_\theta)/A-4(C_\theta\cdot F)/B.
 \end{split}                                                \tag{A.7}
$$

The new native producer evaluates these formulas on the complete disk
$|\rho|\le279/10^6$ and physical strip
$|\operatorname{Im}\theta|\le11/5000$. It uses all 1024 closed angular
cells, the same 512-mode primitive evaluation, radial precision 48, the
complete infinite primitive and radial tails, the exact moving root and
whole affine parameter interval. The original six physical jets, full
$Q,Q_\rho$ disk and positive-real denominator gates are established before
division. Schwarz reflection and successive maximum principles extend
the boundary enclosures to the full bidisk.

All 1024 cells completed in approximately 80.15 seconds, giving

$$
 |\log\mathcal U|<1.664809218,\quad
 |(\log\mathcal U)_\rho|<151.160395,\quad
 |(\log\mathcal U)_\theta|<2.299676.                        \tag{A.8}
$$

These are direct complete derivative enclosures, rather than a small-gap
Cauchy estimate for the much larger zeroth-order logarithm.

## 3. Exact deflated-coordinate derivatives and the true height gradient

Let $e=e^{M_{\mathcal C}R}-1<.028750705256$ and $S_1=3/2000$ as in
the complete root certificate. On the paid physical half strip,

$$
 |\Delta_\theta|\le2e/S_1=:D_\theta<38.334274.
$$

The exact identity
$D_0(T_+-T_-)=2z^2(F_++F_-)$, $z^2=\rho$, gives

$$
 \boxed{\quad
 \Delta_\rho+q\Delta_\theta
   =\frac{3}{2\rho}\left(\frac{F_++F_-}{2}-\Delta\right).
 \quad}                                                     \tag{A.9}
$$

The value at zero is removable. Both quantities in parentheses differ
from one by at most $e^{M_{\mathcal C}|\rho|}-1$. Hence

$$
 |\Delta_\rho|\le
 3M_{\mathcal C}e^{M_{\mathcal C}R}+M_qD_\theta
       =:D_\rho<345.114179.                                \tag{A.10}
$$

This uses the exact radial identity, and does not differentiate an
uncontrolled remainder. With $L=\log\alpha_c$, (A.4), (A.8) and
$|\Delta|\ge1-e$ give

$$
 |L_\rho|<194.023588,\qquad |L_\theta|<14.306184.
$$

Compose these physical derivatives with the complete inverse differential
of the same two-sided chart. Since $y=-\xi$, signs disappear in the
modulus bounds

$$
 |L_y|<275.301222,\qquad |L_\phi|<319.361762.
$$

Thus the true positive height gradient satisfies

$$
 \boxed{\quad
 |\nabla\log\tau|_{C_0}
 \le\frac12\sqrt{|L_y|^2+H|L_\phi|^2}
 =:G<137.673764,\qquad d=1-GH>.965581559089.
 \quad}                                                     \tag{A.11}
$$

All bounds hold for every real parameter and on the actual fixed
canonical collar. No finite-chart height gradient has been substituted.

## 4. Complete full-cap Poisson and local contact estimates

Let $\mathcal H_g$ be the original full grounded Poisson operator. For
canonical root data $a$ and physical regular coefficient $\zeta$, define

$$
 \mathcal H_c(a,\zeta)
 =\left[\mathcal H_g(T_0a,\zeta)/\tau\right]\circ\Psi_+^{-1},
 \quad T_0a=\tau_0(a\circ Y_0),\quad
 X=H^{1/3}_\phi\oplus\mathbb C.                            \tag{A.12}
$$

This is the restriction of the solution on the entire actual cap. No
Dirichlet or Robin condition is introduced at $y=H$. The true energy obeys

$$
 \|\nabla u+u\nabla\log\tau\|_{L^2_{C_0}}^2
       \le\mathfrak b(\mathcal H_g,\mathcal H_g).
$$

The one-dimensional trace inequality and (A.11) therefore give

$$
 \|\nabla u\|_{L^2_{C_0}}
 \le d^{-1}\left[\sqrt{\mathfrak b}
                +G\sqrt{2H}\|a\|_{L^2}\right].             \tag{A.13}
$$

For every frequency the ramp supported on
$h_\lambda=\min(H,\lambda^{-2/3})$, with $h_0=H$, is a legitimate
root extension vanishing before the rest of the cap. Its gradient and
mass integrals are $h_\lambda^{-1}+\lambda^2h_\lambda^2/12$ and
$h_\lambda/3$. The complete root extension energy is thus at most

$$
 E_a=\left[\sqrt{\max(H^{-1},13/12)}+G\sqrt{H/3}\right]^2
             <4160.551475.                                 \tag{A.14}
$$

For the low-frequency part, the maximum of
$(H^{-1}+\lambda^2H^2/12)/(1+\lambda^2)^{1/3}$ is at an endpoint:
its derivative has an increasing affine numerator in $\lambda^2$.
This includes the mean. The regular extension is still (A.6), with zero
root trace. The minimum-energy property of the full solution yields

$$
 T_a=\frac{\sqrt{E_a}+G\sqrt{2H}}d,\qquad
 T_r=\frac{\sqrt{E_{\rm reg}}}d,\qquad
 C_w=(T_a^2+T_r^2)^{1/2}<70.378782.                         \tag{A.15}
$$

The complete internal gain, with the actual root trace and mean, is

$$
 \|u\|_{L^2_yH^{2/3}_\phi}^2
 \le(4+H^2)\|\nabla u\|_{L^2_{C_0}}^2
                  +(4+2H)\|a\|_{H^{1/3}}^2.
$$

Indeed, at each nonzero frequency split at $\lambda^{-2/3}$ when it is
at most $H/2$ and compare neighboring radial intervals as in R45. This
bounds the $\lambda^{4/3}$ mass by twice the radial and three times the
weighted angular energy. At the remaining frequencies, multiply the
trace inequality by $\lambda^{4/3}$ to get four times the radial energy
plus $4\lambda^{2/3}|a_\lambda|^2$. Add the mass trace inequality and
sum all modes. This proves the estimate for arbitrary period and the mean.
Consequently

$$
 C_s=\sqrt{(4+H^2)C_w^2+4+2H}<140.771775.                   \tag{A.16}
$$

For a complete canonical source $f-\operatorname{div}F$ supported in this
collar, full contact is the negative Poisson adjoint. Hence

$$
 \boxed{\quad
 \|K_c(f,F)\|_{X^*}
 \le C_s\|f\|_{L^2_yH^{-2/3}_\phi}
       +C_w\|(F_y,F_\phi/\sqrt y)\|_{L^2}.
 \quad}                                                     \tag{A.17}
$$

This output contains the full root distribution and regular scalar
contact. Restricting only the root test trace to $|n|>N$ improves the
same complete output projection, while retaining regular output:

| Quarter-circle root cutoff $N$ | Ordinary contact | Weak contact |
|---:|---:|---:|
| $0$ | $56.888488$ | $28.426658$ |
| $64$ | $18.526559$ | $9.209138$ |
| $256$ | $16.375451$ | $8.126422$ |
| $65536$ | $15.077126$ | $7.471935$ |
| $1048576$ | $15.071947$ | $7.469322$ |

The entries use $\lambda_N=q_{c,-}(N+1)$,
$\mu_N=(1+\lambda_N^2)^{-1/6}$ and

$$
 E_N=\left[\sqrt{\max(1,(H\lambda_N^{2/3})^{-1})+1/12}
          +\frac{G}{\sqrt3\lambda_N^{2/3}}\right]^2
$$

in (A.15), with root numerator $\sqrt{E_N}+G\sqrt{2H}\mu_N$.
The whole solution can still generate every body frequency. The
unconditional constants used below are (A.15)–(A.16), not this table.

## 5. True physical source density and the grounded mean charge

For $\Psi_+(s,\theta)=(y,\phi)$, $J_+=\det D\Psi_+>0$, the exact
physical source is

$$
 F_g=\frac{J_+}{\tau}(D\Psi_+)^{-1}F\circ\Psi_+,\qquad
 f_g=\frac{J_+}{\tau}
       [f-\nabla\log\tau\cdot F]\circ\Psi_+.                 \tag{A.18}
$$

Piola and the derivative of $1/\tau$ prove this formula. Its weak-vector
energy is exactly $\int F^*C_0^{-1}F$. Boundary vector loads, when
present, use the same conormal density. The Ai source below is ordinary
and has no separate boundary vector load.

The grounded constant solution is canonical $1/\tau$, rather than the
canonical constant one. Its full charge identity is

$$
 \left\langle K_c(f,F),
       \left(\tau_0^{-1},\sqrt{\ell_\theta}\right)\right\rangle
 =-\int\left[f\tau^{-1}+F\cdot\nabla(\tau^{-1})\right].       \tag{A.19}
$$

By (A.18) this equals the original physical total source charge. It
retains the root mean and regular mean-flux relation, including the
height-gradient term. The source norm is the canonical mixed norm in
(A.17). No physical anisotropic Bochner-norm invariance is assumed.

## 6. An exact original-frame trial and every term of its residual

Let $c_A=-\operatorname{Ai}'(0)/\operatorname{Ai}(0)$ and
$c=c_A^{-1/2}$ as in R39. Set $\chi=1$ for $y\le H/2$,
$\chi=0$ for $y\ge H$, and use $1-10t^3+15t^4-6t^5$ on the intervening
interval. It is $C^2$ with matched first and second derivatives, and

$$
 |\chi'|\le15/(4H)=15000,\qquad
 |\chi''|\le24/H^2=384000000.                              \tag{A.20}
$$

On every nonzero root frequency define

$$
 U_{\rm tr}(y,n)=2ic\,\lambda_n^{-1/3}
          \operatorname{Ai}(y\lambda_n^{2/3})\chi(y).        \tag{A.21}
$$

On the root mean and regular input slots take the zero trial; those
columns remain in the error. Each nonzero input has exactly the root
Cauchy data for incoming one and outgoing minus one:

$$
 U(0)=2ic\operatorname{Ai}(0)\lambda^{-1/3},\qquad
 p_{\rm out}=-U_y(0)=-2ic\operatorname{Ai}'(0)\lambda^{1/3}.
$$

The exact ordinary residual of (A.3) is

$$
 f_{\rm tr}=-\chi V(-y,\phi)U_0
                -2\chi'\partial_yU_0-\chi''U_0,\qquad
 U_0=2ic\lambda^{-1/3}\operatorname{Ai}(y\lambda^{2/3}).      \tag{A.22}
$$

The first term contains the entire nonconstant potential and every
Fourier lag. Both cutoff terms are retained. Since $\chi$ and its first
two derivatives vanish at the outer endpoint, the physical trial extends
by zero without any jump or delta source.

## 7. Full-matrix ordinary residual bound with right 4/3 gain

All norms here use the actual physical frequency $\lambda_n$. Cauchy on
the full strip gives $M_{V_\phi}\le M_V/\sigma$, $\sigma=1/40000$.
Multiplication by $V$ has $L^2$ norm at most $M_V$ and $H^1$ norm at
most $M_V+M_{V_\phi}$. Interpolation and duality give

$$
 M_{-2/3}(V)\le M_V^{1/3}(M_V+M_{V_\phi})^{2/3}
              <880510735.                                 \tag{A.23}
$$

This is a complete infinite-matrix bound. Set
$r_q=(1+q_{c,-}^{-2})^{1/3}<1.000220417$.
The exact identity
$\int_0^\infty\operatorname{Ai}(z)^2dz=\operatorname{Ai}'(0)^2$
follows by integrating
$(z\operatorname{Ai}^2-\operatorname{Ai}'^2)'=\operatorname{Ai}^2$;
the boundary term at infinity vanishes by R96's proved positive-axis
decay. Parseval and $z=y\lambda^{2/3}$ thus give

$$
 \|\chi VU_0\mathcal L^{4/3}\|_{L^2\to L^2_yH^{-2/3}}
 \le2c\,r_qM_{-2/3}(V)|\operatorname{Ai}'(0)|
       <533937125.                                        \tag{A.24}
$$

The Fourier integration is performed before taking the uniform
frequency bound; this is not a single-column estimate.

R96 proves, for both $\operatorname{Ai}$ and $\operatorname{Ai}'$,

$$
 |\operatorname{Ai}(z)|,\ |\operatorname{Ai}'(z)|
 \le\tfrac34(1+z)^{1/4}e^{-2z^{3/2}/3},\qquad z\ge0.
$$

Put $\kappa=(H/2)^{3/2}/3$ and

$$
 M_*^2=\frac9{16}\frac23
     \left[(2/3)^{-2/3}\Gamma(2/3)+(2/3)^{-1}\right].
$$

Split half of the squared exponential at
$z\ge(H/2)\lambda^{2/3}$. Since $\sqrt{1+z}\le1+\sqrt z$, the
$L^2_z$ tail of either function is at most $M_*e^{-\kappa\lambda}$,
where $M_*<1.108106$ and $\kappa>4.65847495312\,10^{-7}$.
The first cutoff term leaves a factor $\lambda^{2/3}$, whose full maximum
is

$$
 \sup_{\lambda>0}\lambda^{2/3}e^{-\kappa\lambda}
  =\left(\frac{2}{3e_{\rm Euler}\kappa}\right)^{2/3}
       <6519.991.                                         \tag{A.25}
$$

The consumer evaluates this closed expression, not the function at a
rounded critical point. The second cutoff term needs only
$e^{-\kappa q_{c,-}}$. Therefore

$$
 \begin{split}
 \|2\chi' U_{0,y}\mathcal L^{4/3}\|_{L^2\to L^2H^{-2/3}}
  &\le4c r_q\|\chi'\|_\infty M_*
       \left(\frac{2}{3e_{\rm Euler}\kappa}\right)^{2/3}
       <507818066,\\
 \|\chi''U_0\mathcal L^{4/3}\|_{L^2\to L^2H^{-2/3}}
  &\le2c r_q\|\chi''\|_\infty M_*e^{-\kappa q_{c,-}}
       <996926760.
 \end{split}                                                \tag{A.26}
$$

The entire residual consequently satisfies

$$
 \boxed{\quad
 \|f_{\rm tr}\mathcal L^{4/3}\|_{L^2\to L^2_yH^{-2/3}}
       <2038681950=:F_*.
 \quad}                                                     \tag{A.27}
$$

The actual consumer uses unrounded directed endpoints. Both Fourier
signs occur in the trial; multiplication and the full cap retain every
opposite-sign and mean output.

## 8. Full original Airy frame, its mean, and the regular scalar port

The R39 root columns are, for $n\ne0$,

$$
 D_\pm(\xi,n)=c\lambda_n^{-1/3}
  [\operatorname{Bi}(-\xi\lambda_n^{2/3})
       \pm i\operatorname{Ai}(-\xi\lambda_n^{2/3})],
$$

and for the mean $D_\pm(\xi,0)=c(1\pm i\xi/\pi)$. Their determinant
is $-2ic^2/\pi$ for every mode, and

$$
 F_*^*\left[\frac{\pi c_A}{2i}
    \begin{pmatrix}0&I\\-I&0\end{pmatrix}\right]F_*
       =\operatorname{diag}(I,-I).                         \tag{A.28}
$$

At the regular scalar port use the same exact Green factor:

$$
 z_\pm^{\rm reg}
   =\frac{\sqrt{\pi c_A}}2(\zeta\mp i\lambda_{\rm reg}).       \tag{A.29}
$$

The true root height, angular Jacobian and normal shear in (A.4) are
real Green-preserving boundary transformations. Their direct and inverse
maps are bounded on the trace pair, by the full chart, its positive
real angular derivative and analytic height. The original full grounded
DN relation is bounded and selfadjoint on $H^{1/3}\oplus\mathbb C$ and
its dual. R85's graph proof therefore applies after the transformations:
a bounded invertible Green map sends its maximal neutral subspace to
another maximal neutral subspace with closed positive and negative
projections. A nonzero orthogonal complement of either projection
would give a nonzero positive or negative vector in that same neutral
subspace, which is impossible. Both projections are thus onto.
Consequently the actual $R_+$ is onto unitary on the full augmented
$L^2\oplus\mathbb C$. This argument uses the complete cap/Robin
realization, not a half-line Ai impedance.

For a contact-only variation, the exact inverse frame gives the norm
to either wave:

$$
 \begin{split}
 N_{\ne0}&=\frac{\pi\operatorname{Ai}(0)}c
                (1+q_{c,-}^{-2})^{1/6}<.952418,\\
 N_0&=\frac{\pi}{2c}<1.341180,\\
 N_{\rm reg}&=\frac{\sqrt{\pi c_A}}2<.756680.
 \end{split}
$$

Hence in the product norm

$$
 N=\max(N_{\ne0},N_0,N_{\rm reg})<1.341180.                 \tag{A.30}
$$

The root mean is explicitly evaluated by its own exact columns. The
height shear is already subtracted in the canonical contact; it
contributes no extra term to a zero-root-trace correction. It was not
dropped in defining the actual full boundary graph.

## 9. Correct the trial on the whole cap, then use genuine unitarity

Let $G$ be the same full-cap zero-root-trace, zero-regular-mean inverse.
The homogeneous Poisson solution with trial traces is
$U_{\rm tr}-Gf_{\rm tr}$, with the source density understood as in
(A.18). Equation (A.17) controls its full contact correction. Write its
two waves as

$$
 A_{\rm in}=I+E_A,\qquad A_{\rm out}=-I+E_B.
$$

On root mean and regular input columns the trial is zero, so
$E_A=-I$, $E_B=I$ exactly on those input columns. Each contributes one
to the right-weighted bound, since $\mathcal L=1$ there. The actual
reflection on these columns has not been prescribed. For every other
input, (A.21) has exact root traces, and (A.17), (A.27), (A.30) give

$$
 \|E_A\mathcal L^{4/3}\|,\quad
 \|E_B\mathcal L^{4/3}\|\le1+NC_sF_*.
$$

The full graph identity $R_+A_{\rm in}=A_{\rm out}$ holds without
assuming the trial incoming map invertible. Therefore

$$
 S:=R_++I=E_B-R_+E_A,\qquad
 \|S\mathcal L^{4/3}\|
       \le2+2NC_sF_*<769807285232.                          \tag{A.31}
$$

Actual unitarity gives $S=S^*R_+$. Taking adjoints in (A.31) and using
this exact identity yields

$$
 \|\mathcal L^{4/3}S\|
 \le\|\mathcal L^{4/3}S^*\|\,\|R_+\|\le2+2NC_sF_*.
$$

For the unbounded weight, start on finite Fourier data, use the bounded
adjoint extension and closedness to obtain this full-domain statement.
Interpolation between the right and left bounds gives exactly
$-4/3\le s\le0$ in (A.2), without assuming a higher Sobolev norm of $R_+$.

For an ordinary or weak local source, take its zero-Dirichlet particular
solution and cancel its incoming wave with the full homogeneous graph.
The outgoing correction is
$z_{\rm out}^{\,G}-R_+z_{\rm in}^{\,G}$. Thus

$$
 \boxed{\quad
 \|z_{\rm out}^{\,\rm aff}\|
 \le377.600482\,\|f\|_{L^2H^{-2/3}}
       +188.781182\,\|C_0^{-1/2}F\|_{L^2}.
 \quad}                                                     \tag{A.32}
$$

This includes both actual finite mean/contact rows and every root
output. Its source support and units are precisely those of (A.17).

## 10. Executed artifacts, reproduction and remaining scope

Native first-jet producer and report:

- scripts/fourfold_root_full_grounded_density_first_jets.py, SHA256
  404e3584213a64b997826147c1132b795aa21a8ee26b7df89377e72befafc16a;
- notes/2026-11-13-root-full-grounded-density-first-jets.json.gz, SHA256
  8665a302ad230fca4c648be87896d20c178ba71c283ac247d3650a727c978cf1.

Full-cap/Airy consumer and final directed report:

- scripts/fourfold_actual_exact_positive_cap_Airy_contact.py, SHA256
  d6a00d2bd579c8dd0d7e2e8f404b253cad4c4087a95b0429a6dede397520ecd8;
- notes/2026-11-13-exact-positive-cap-Airy-contact-v2.json, SHA256
  f61369e1e740269a11c271efb5cfd9a27df5b1aa91a275ae40e01edee4402649.

Reproduce from the topic directory using fresh output paths:

~~~bash
python3 scripts/fourfold_root_full_grounded_density_first_jets.py \
  --out notes/2026-11-13-root-full-grounded-density-first-jets.json.gz
python3 scripts/fourfold_actual_exact_positive_cap_Airy_contact.py \
  --out notes/2026-11-13-exact-positive-cap-Airy-contact-v2.json
~~~

The preliminary consumer stopped at a domain gate because overlapping
Arb enclosures of equal prescribed rational radii did not establish their
ordering. The final consumer compares exact domain fractions. No failed
native cell was removed or replaced. The cutoff maximum uses the exact
expression (A.25), including all frequencies.

The proved factor is the complete original-frame positive reflection
on the stated unweighted smoothing window. Its deviation from $-I$
does not introduce an unlisted order-$1/|n|$ term at this level.
The larger finite Sobolev and signed-weight windows, global ordinary
source wiring, final regular compatibility, other interval factors and
the complete high/low Schur inverse remain necessary for the final
returned inverse and nonlinear closed family.
