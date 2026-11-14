# R133 supplement: the actual balanced fold, physical source, and negative ports

2026-11-13, visible-exact / phase_inverse. **Status: proved.**

This consumes the same complete M256 amplitude-$3/4$ accepted candidate,
its whole real affine parameter box, and its actual physical-angle fold
from [the preceding theorem](R133-supplement-actual-physical-fold-and-full-Airy-collar.md).
The canonical half-width is enlarged from $2^{-104}$ to
$$
 \boxed{\delta=2^{-36}}.                                      \tag{B.1}
$$
The enlargement uses the complete two-line structure, including the
exact factor $T$ in the upper-right remainder. All frequencies, both
mean states and every low-high interaction remain. The full balanced
perturbation norm is less than $0.012668520$. Physical $L^2$
reconstruction has no factor $\delta^{-1/4}$. The ordinary source has
the explicitly paid full physical $H^1(dr\,d\theta)$ norm, including
its radial derivative.

A two-sided complete negative propagator, in the identical full norm,
has constant less than $66.268954$ from the inner negative port to
every canonical section as far as $T=-15\cdot2^{-38}$.
The fixed physical section $r=r_*(\eta)-2^{-37}$ is proved to lie
inside this negative annulus; its angle-dependent graph trace operator
is a separate interface, not silently identified with a fixed-$T$ map.

## 1. Same actual equation and complete state

Retain exactly the physical variation $h=(\delta u,\delta v)$,
$R=\operatorname{diag}(-1,1)$, and
$$
 Rh=FU,\quad F=\operatorname{diag}(b^{-1/2},b^{1/2}),\quad b^2=T/K,
 \qquad U_T=J(T)U_X+\mathcal VU+g,\quad
 g=F^{-1}A_T^{-1}Rf.                                       \tag{B.2}
$$
The actual inverse chart exists on the entire product
$|T|\le2^{-34}$, $|\operatorname{Im}X|\le1/4096$.
The physical collar is the exact inverse image of
$[-\delta,\delta]\times\mathbb R/(\pi/2\mathbb Z)$.
No physical rectangle is substituted for it.

The exact formulas (F.37)--(F.38) of the preceding theorem give
$$
 \mathcal V=\begin{pmatrix}d_1&T e_{12}\\e_{21}&d_2\end{pmatrix}. \tag{B.3}
$$
All four functions are holomorphic on that full product, including
the removable quotient $e_{12}$ at zero. No candidate PDE identity
or mean-zero condition is used. Consuming the already paid actual
$A,b,\Delta,T_\theta,L$ and logarithmic frame derivatives gives
$$
 |d_i|\le D_*<327626.813,\qquad
 |e_{12}|,|e_{21}|\le E_*<30366.860.                       \tag{B.4}
$$
These are bounds for the complete coefficients, not their nonconstant
parts.

Let $P=\langle D_X\rangle$ have symbol $P_m=\sqrt{1+m^2}$. For
$m\in4\mathbb Z\setminus\{0\}$ put
$$
 \omega_m=(|T|+|m|^{-2/3})^{1/2},\quad W_m=\omega_m^{-1/2},
 \quad D_m=\operatorname{diag}(W_m,W_m^{-1}).
$$
For the two independent means set $W_0=1,D_0=I$. Our complete norm is
$$
 \|U\|_{\mathcal E(T)}=\|\mathcal D(T)U\|_2,\qquad
 \mathcal D=P^{1/6}\operatorname{diag}(W,W^{-1}).           \tag{B.5}
$$
Because $|T|<1/16$ and the smallest nonzero physical frequency is 4,
every mode, including the mean, satisfies
$$
 1\le W_m\le P_m^{1/6},\qquad
 \|U\|_2\le\|U\|_{\mathcal E(T)},\qquad
 \|\mathcal D(T)g\|_2\le\|g\|_{H_X^{1/3}}.               \tag{B.6}
$$
The first reconstruction inequality has no frequency threshold or
quarter-power of the distance to the root.

## 2. Full multiplication in the padded Airy norm

For $t=|T|\in[0,1/16]$ define
$$
 A_t=P(1+t^3P^2)^{-1/2}.
$$
Its exact norm for $t>0$ has the variational formula
$$
 \|A_tf\|_2^2
 =\inf_{f=f_1+f_0}\{\|Pf_1\|_2^2+t^{-3}\|f_0\|_2^2\}.   \tag{B.7}
$$
This follows by minimizing each Fourier mode's two scalar squares;
the zero mode is included. If $a_j\ge\|\partial_X^j a\|_\infty$,
multiplication by $a$ has $L^2$ norm at most $a_0$ and $H^1$ norm
at most $a_0+a_1$. Formula (B.7) gives the latter bound in the
$A_t$ norm as well. Complex interpolation of these Hilbert multiplier
spaces therefore gives
$$
 \|A_t^{1/6}aA_t^{-1/6}\|
       \le a_0^{5/6}(a_0+a_1)^{1/6}.                    \tag{B.8}
$$
At $t=0$ this is ordinary $L^2,H^1$ interpolation with $A_0=P$.

Set $\widetilde W=(t+P^{-2/3})^{-1/4}$. The elementary inequality
$$
 1\le\frac{(1+x^{1/3})^3}{1+x}\le4\qquad(x\ge0)
$$
gives $2^{-1/6}\le\widetilde W/A_t^{1/6}\le1$.
For nonzero $m$, $W_m/\widetilde W_m$ lies between
$(|m|/P_m)^{1/6}$ and one; for $m=0$ it is $(1+t)^{1/4}$.
Hence on the entire Fourier space
$$
 2^{-1/3}\le W/A_t^{1/6}\le2^{1/6}.                     \tag{B.9}
$$
Combining (B.8)--(B.9), enlarging $\sqrt2$ to 2, proves
$$
 \|WaW^{-1}\|,\ \|W^{-1}aW\|
 \le M_0(a):=2a_0^{5/6}(a_0+a_1)^{1/6}.                \tag{B.10}
$$
The second estimate follows by adjoint from the first applied to
$\bar a$ on the real circle; no analytic continuation of $\bar a$
is needed.

Spatial differentiation commutes with $W$. Thus the angular commutator
in (B.10) is the same conjugation of $a_X$, with norm at most
$M_1(a)=2a_1^{5/6}(a_1+a_2)^{1/6}$. The $H^1$ norm is at most
$M_0+M_1$, by the product rule. Interpolating gives
$$
 \|P^{1/6}W^{\pm1}aW^{\mp1}P^{-1/6}\|
 \le M_0(a)^{5/6}(M_0(a)+M_1(a))^{1/6}.                \tag{B.11}
$$
These are full multiplication operators. Every mean crossing and
every finite-frequency interaction is present.

For the lower-left term, $W^{-1}$ is a contraction by (B.6).
Thus $W^{-1}e_{21}W^{-1}$ and its commutator are bounded by
$E_*$ and $E_1$, respectively. Its further conjugation by $P^{1/6}$
has bound $E_*^{5/6}(E_*+E_1)^{1/6}$.
For the upper-right term, $\|W\|\le t^{-1/4}$ for $t>0$, so
$$
 \|TWe_{12}W\|\le\sqrt t\,E_*.
$$
The commutator has the same $\sqrt t$ factor, which survives
interpolation. Its bounded extension at $T=0$ is zero.
This uses the exact factor $T$ in (B.3).

## 3. The actual complete matrix bound

The actual analytic inverse strip gives complete Cauchy bounds with
$Q=8192$:
$$
 D_1=QD_*,\quad D_2=2Q^2D_*,\quad E_1=QE_*.
$$
Insert these into (B.11) and the off-diagonal estimate. The norm of
the full two-state operator is bounded by the maximum diagonal norm
plus the maximum off-diagonal norm. The latter is no larger than the
lower-left budget, since $t<1$. The native result is
$$
 \boxed{\|\mathcal D\mathcal V\mathcal D^{-1}\|
          \le M_{\mathcal E}<13602719.023.}             \tag{B.12}
$$
Its diagonal and off-diagonal contributions are less than
$13466373.661$ and $136345.362$. These bounds hold on the entire
actual product domain used here and on the whole real parameter box.

## 4. Enlarged full two-port inverse

The [complete universal Airy kernel](R133-supplement-uniform-two-port-Airy-kernel-with-full-source.md)
has kernel and individual Poisson column bounds 32 in $D_m$. It
commutes with $P^{1/6}$, so the same bound holds in $\mathcal D$.
The two scalar input functions have their full $H_X^{1/6}$ norms:
one negative incoming and one positive unstable port. Both mean
inputs are retained with weight one.

On length $2\delta$, the weighted Green has $L^2$ norm at most
$B=64\delta$, and the two-column Poisson map has norm at most
$P_*=64\sqrt\delta$. Thus
$$
 B=2^{-30},\qquad P_*=2^{-12},\qquad
 BM_{\mathcal E}<0.012668520<1/8.                       \tag{B.13}
$$
Neumann inversion on the single Hilbert space $L^2_T\mathcal E(T)$
gives
$$
 \|U\|_{L^2_T\mathcal E}
 <9.432724398\cdot10^{-10}\|g\|_{L^2_TH_X^{1/3}}
   +0.000247273211\|\mathfrak g\|_{H_X^{1/6}\oplus H_X^{1/6}}. \tag{B.14}
$$
There is no repeated angular loss. Finite Fourier approximation and
the same bounded inverse justify the construction; (B.6) recovers an
ordinary full $L^2$ state satisfying the original equation.

The two full boundary-state outputs, in the identical weights, obey
$$
 \|\operatorname{Tr}_\pm U\|_{\mathcal E\oplus\mathcal E}
 <0.000247273211\|g\|_{L^2_TH_X^{1/3}}
   +64.821189\|\mathfrak g\|_{H_X^{1/6}\oplus H_X^{1/6}}. \tag{B.15}
$$
Indeed the source coefficient is
$64\sqrt\delta(1+M_{\mathcal E}B/(1-BM_{\mathcal E}))$, and the
input coefficient is
$64+64\sqrt\delta M_{\mathcal E}P_* /(1-BM_{\mathcal E})$.
Both independent complementary means are among these outputs.

## 5. Ordinary physical source and original means

The preceding fold theorem supplies
$$
 \|g\|_{L^2_{T,X}}\le S_0\|f\|_{L^2_{r,\theta}},
 \quad S_0<23.132428,\quad
 |r_X|<0.000334091,\quad|\theta_X|<5.497224.             \tag{B.16}
$$
The actual analytic source matrix $M_f=F^{-1}A_T^{-1}R$ has
$\|(M_f)_X\|\le Q\|M_f\|_\infty$ on the real product, by Cauchy
on its proved strip. Applying the exact chain rule gives
$$
 \|g\|_{L^2_TH_X^1}
 \le S_1\|f\|_{H^1(\Omega_\delta)},\qquad
 S_1=S_0(1+Q+|r_X|+|\theta_X|)<189651.149.               \tag{B.17}
$$
This physical $H^1$ norm includes the ordinary $L^2$ norms of
$f,f_r,f_\theta$. It is not only an angular Sobolev norm.
Fourier interpolation in the target product domain yields
$$
 \|g\|_{L^2_TH_X^{1/3}}
 \le S_0^{2/3}S_1^{1/3}\|f\|_{L^2}^{2/3}\|f\|_{H^1}^{1/3}
 <466.443769\|f\|_{H^1(\Omega_\delta)}.                  \tag{B.18}
$$
No interpolation or extension theorem for an unspecified curved
physical domain is needed: both physical norms are explicit, and
the interpolation is performed after the exact transformation.

From $h=RFU$, the actual Jacobian and (B.6),
$$
 \boxed{\|h\|_{L^2(\Omega_\delta)}
 <1.020846\cdot10^{-6}\|f\|_{H^1(\Omega_\delta)}
   +0.000573722\|\mathfrak g\|_{H^{1/6}\oplus H^{1/6}}.} \tag{B.19}
$$
On a canonical boundary the angle Jacobian and frame give
$\|h\|_{L^2(d\theta)}<6.124995\|U\|_{\mathcal E}$. Thus
$$
 \|h_{\partial\Omega_\delta}\|_{L^2\oplus L^2}
 <0.706452\|f\|_{H^1(\Omega_\delta)}
       +397.029432\|\mathfrak g\|_{H^{1/6}\oplus H^{1/6}}. \tag{B.20}
$$
Neither reconstruction uses a factor $\delta^{-1/4}$.
The physical means are exactly
$\frac2\pi\int RFU(T_r/\mathcal J)\,dX$. They are not replaced by
canonical zero coefficients. Their interactions were included in
every multiplication and inversion above.

Conversely a complete physical boundary field in $H^{1/3}(d\theta)$
supplies the full balanced state. The true boundary diffeomorphism
has $L^2$ composition norm at most
$c_0=\sqrt{(dX/d\theta)_+}$ and $H^1$ norm at most
$c_1=\max(c_0,1/\sqrt{(dX/d\theta)_-})$.
Interpolation and the complete frame Cauchy bound imply
$$
 \|U\|_{\mathcal E}
 \le\|F^{-1}\|_\infty(1+Q)^{1/3}c_0^{2/3}c_1^{1/3}
       \|h\|_{H^{1/3}(d\theta)}
 <123.455847\|h\|_{H^{1/3}(d\theta)}.                   \tag{B.21}
$$
This is a bound for the full transformed state. Extraction of the
specified input ports uses their stated full linear functionals.

## 6. Negative propagation without changing the norm

The complete negative interval
$$
 I_-=[-15\cdot2^{-38},-2^{-36}]                         \tag{B.22}
$$
lies inside the same actual canonical product.
The preceding fold theorem's two-sided negative reference propagator
has bound 64 in $D_m$ at any two interior points. It commutes with
$P^{1/6}$. Duhamel and ordinary Gronwall in the unchanged full
$\mathcal E$ norm give
$$
 \|U(t)\|_{\mathcal E(t)}
 \le C_-\left(\|U(s)\|_{\mathcal E(s)}
       +\int_s^t\|g(\tau)\|_{H_X^{1/3}}\,|d\tau|\right),
$$
$$
 C_-=64\exp(64M_{\mathcal E}|I_-|)<66.268954.            \tag{B.23}
$$
The mean states and their entire coupling are retained. By
Cauchy--Schwarz in $T$ and (B.18), its complete physical $H^1$
source fee is
$$
 C_-\sqrt{|I_-|}\,S_0^{2/3}S_1^{1/3}<0.195541.          \tag{B.24}
$$
Neither endpoint is converted first to the unpadded degenerate
$\sqrt{-K}$ energy.

For an explicit combined budget, the outer canonical section's
complete physical trace satisfies the conservative bound
$$
 \|h_{\rm outer}\|_{L^2(d\theta)}
 <55\|f_{\rm collar}\|_{H^1}
    +1.4\|f_{\rm negative}\|_{H^1}
    +30500\|\mathfrak g\|_{H^{1/6}\oplus H^{1/6}}.        \tag{B.25}
$$
This follows from (B.15), (B.18), (B.23), (B.24) and the exact
roundings: trace frame $<7$, $C_-<67$, source-map factor $<467$,
source trace $<1/4000$, port trace $<65$.
It records the whole remaining total gain, not just the small
Neumann number of the inner block.

## 7. Locate the genuine fixed-radial interface

For real arguments the fold factor $C=(3G/2)^{2/3}$ has lower
bound twice the complex-real-part bound $C_-$ in the earlier proof.
At the actual parameter-dependent fixed radial section
$$
 r_c(\eta)=r_*(\eta)-2^{-37},
$$
the entire canonical graph satisfies
$$
 1.8892589\cdot10^{-11}<-T(r_c,\theta)
          <5.0488771\cdot10^{-11}.                     \tag{B.26}
$$
It lies strictly inside (B.22), on the identical scalar and candidate
germs. This is a geometric inclusion. Evaluation at this
angle-dependent time is not a constant-$T$ propagator; its trace
operator and the remaining strict piece to the shared candidate
boundary still require explicit interface estimates. The positive
regular graph and the complete body feedback are also not granted.

## 8. Actual native record

The certified consumer is
[fourfold_codazzi_balanced_fold_ports_v3.py](../scripts/fourfold_codazzi_balanced_fold_ports_v3.py)
with
[the complete v3 report](../notes/2026-11-13-R133-actual-alpha075-balanced-fold-ports-v3.json.gz).
It consumes the unchanged actual germ and fold and requires the
corrected universal Airy v2 report's explicit negative-root reflection
flag. All 12 gates passed. Reproduction is

    python3 scripts/fourfold_codazzi_balanced_fold_ports_v3.py \
      --out /tmp/actual-alpha075-balanced-fold-ports-v3.json.gz

The final report SHA-256 is
ac54148b15a47d5969b6baf3581bcf3149e6a404e29b725d098cb362b68853de.
The preliminary v1 budget used the older $2^{25}$ reference constant.
The intermediate v2 budget consumed the excluded first orientation
attempt of the universal calculation. Neither replaces this corrected
v3 chain; their scope is recorded in the universal theorem's named
orientation-correction note.
