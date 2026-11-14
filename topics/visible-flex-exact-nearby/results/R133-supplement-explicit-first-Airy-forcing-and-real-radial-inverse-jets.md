# R133 supplement: explicit first Airy forcing and real radial inverse derivatives

2026-11-14, phase_inverse.

**Proved identities and complete quantitative recipes.** This supplies
the actual degree-zero Airy operator, direct real radial bounds for the
old-circle inverse, and a nonsingular recipe for bounding its first
forcing on the original real polynomial pieces. The companion consumer
uses already completed intrinsic third jets and the completed
radius-$1/50$ root native. It does not recompute a target, ray solve,
response solve or any of the original 1300 coefficient rows.

Numerical values from that new consumer are only claims after its
actual public Actions execution. The finite old-primitive and inverse
remainders, the complete even mean, and next-amplitude state jumps
remain separate parts of the full strong-remainder budget.

## 1. Exact degree-zero coefficient in the old angle

Use (O.1)--(O.20) of
[the ordered scalar operator](R133-supplement-ordered-scalar-root-operator-and-one-gain-radial-remainder.md).
Set
$$
 D=\partial_r-d\partial_\phi,\quad
 \ell=-2buv,\quad e=-b(1+3u^2+Kv^2),\quad
 b_0=b(1-u^2-3Kv^2),\quad
 t_Q=\eta_r/\eta+d_\phi+e.
 \tag{L.1}
$$
In this section $b_0$ is the local coefficient of the original
operator $B$, not the second leading Airy amplitude.

With $n=4|j|$, $\epsilon=\operatorname{sgn}j$, let
$U_n(w)$ be the genuine two-profile Airy expression (P.6), and put
$$
 H=i\epsilon X_\phi\,1+
        T_\phi\begin{pmatrix}0&T\\1&0\end{pmatrix},\qquad
 H_D=i\epsilon DX\,1+
        DT\begin{pmatrix}0&T\\1&0\end{pmatrix}.
 \tag{L.2}
$$
The two exact derivative rules are
$$
 \partial_\phi U_n(w)=U_n(nHw+\partial_\phi w),\qquad
 DU_n(w)=U_n(nH_Dw+Dw).
 \tag{L.3}
$$
The degree-minus-one inverse symbols on these amplitudes are
$n^{-1}H^{-1}$ for the old primitive and
$n^{-1}\eta^{-1}H^{-1}$ for $J$. They are the leading terms of the
previously proved finite exact expansions; the final remainders are
retained.

Define actual coefficient functions
$$
\begin{split}
 r_Q&=D\ell+\eta e_\phi-2b\eta u_\phi u
               -\ell(\eta_r/\eta+d_\phi),\\
 \vartheta&=r_Q/\eta-2bKvv_\phi,\\
 V_0&=t_Qb_0-Db_0-K(\ell^2-4b\eta vu_\phi),\\
 T_0&=\eta_r/\eta-4b\langle u^2+Kv^2\rangle+5d_\phi .
\end{split}
 \tag{L.4}
$$
Then the actual degree-zero amplitude operator is
$$
 \boxed{\displaystyle
 \mathcal L_0w=\mu^{-1}
 \left[(D^2+\eta^2K\partial_\phi^2-T_0D)w
                +V_0w-\vartheta H^{-1}H_Dw\right].}
 \tag{L.5}
$$
In the transport convention $\mathcal T(a,b)=(F_b,F_a)$, the first
forcing is exactly
$$
                    (F_b,F_a)=-\mathcal L_0(a_0,b_0^{\rm Airy}).
 \tag{L.6}
$$
The order of $H^{-1}H_D$ in (L.5) is fixed.

To verify (L.4), the multiplication part of (O.15) is
$D\ell+\eta e_\phi-2b\eta u_\phi u+\ell e-t_Q\ell$.
The apparent order-zero pieces of $[d\partial_\phi,N_A]$ cancel
because their scalar multipliers commute. Their complete
order-minus-one and mean terms remain. The local part of $AC$ is
$\ell^2-4b\eta vu_\phi$. Finally $N_B+R_QJ$ has leading amplitude
$n^{-1}\vartheta H^{-1}$; its product with $D$ gives the last,
degree-zero term in (L.5). This also proves that the one-gain radial
term cannot be omitted from the first forcing.

All $P=1-\Pi$ factors in the original operators are still present.
The exact remainder is the difference between the full projected
operator applied to $PU_n(w)$ and the finite expression containing
$n\mathcal Tw+\mathcal L_0w$. It contains every old mean, projection
commutator, finite inverse endpoint and remaining negative degree.
The identity (L.5) is not a claim that this remainder is zero.

## 2. Direct radial derivatives of the complete inverse

On an open original real piece, the old projection and old primitive
are independent of $r$. Differentiating $AJ=1$ gives
$$
\begin{split}
 J_r&=-JA_rJ,\\
 J_{rr}&=2JA_rJA_rJ-JA_{rr}J,\\
 J_{rrr}&=-6JA_rJA_rJA_rJ
          +3JA_{rr}JA_rJ+3JA_rJA_{rr}J-JA_{rrr}J .
\end{split}
 \tag{L.7}
$$
Suppose the whole angular inverse has
$\|J\|\le J_0$, $\|\partial_\phi J\|\le J_1$ on the chosen
ordinary or weighted Wiener space. With
$$
 M_p=|\eta^{(p)}|J_1+\|L^{(p)}\|J_0,
$$
complete bounds are
$$
 \|J_r\|\le J_0M_1,\quad
 \|J_{rr}\|\le J_0(2M_1^2+M_2),\quad
 \|J_{rrr}\|\le J_0(6M_1^3+6M_1M_2+M_3).
 \tag{L.8}
$$
Each product in (L.7) uses its actual parity spaces. For example
$$
\begin{split}
 \|L_r\|\le{}&
 2|b_r|U_0V_0+2|b|(U_{r,0}V_0+U_0V_{r,0})\\
 &+\tfrac12\{|b_r|V_1U_0+
          |b|(V_{r,1}U_0+V_1U_{r,0})\}.
\end{split}
 \tag{L.9}
$$
For higher $p$ use the full multinomial Leibniz sum in the same
formula $L=M_{-2buv}-2bPM_{v_\phi}IM_uP$. The primitive norm is
exactly at most $1/4$, including all its Fourier inputs.

The original value repair is constant on each original cubic
piece. Its radial derivatives of positive order vanish there;
the corresponding jumps of those derivatives do not vanish.
At a seam where the repaired values agree,
$$
                 [J_r]=-J([\eta_r]\partial_\phi+[L_r])J.
 \tag{L.10}
$$
Thus real derivative information avoids a tiny radial Cauchy radius
without discarding a seam. The exact commutator with $D_0$ can
alternatively be retained as $[D_0,J]=-J[D_0,A]J$ with (O.15)--(O.17).

## 3. Original inputs and their derivative meaning

The shared
[original six-part manifest](../notes/2026-11-14-R133-original-root-window-intrinsic-third-jet-parts.json)
pins the six complete compressed original row files from public
run 43583838026 and the exact original producer. The keys
$({\tt gamma,gamma1,gamma2,gamma3})$, and analogously beta, K and s,
are ordinary derivatives, not Taylor coefficients divided by
factorial. Both whole-interval and midpoint jets were saved.

These records enclose the original whole physical-parameter box
and hence the fixed $\eta_0$. They represent the same smooth
intrinsic metric and rotational background at adjacent cache
boundaries. All of the radius-$1/50$ window lies to the right of
$9/50$, where the compact $\nu$ bump is exactly zero. Consequently
these intrinsic jets also apply to $\nu_\delta=\nu_0+\delta$.
This does not extend that independence into the compact support.

The consumer intersects each original exact interval with the
already accepted radius-$1/50$ rows and original polynomial
pieces. A common-row index is never replaced by a polynomial
piece number. Candidate and response derivatives come directly
from the complete original dyadic cubic coefficients, with all
65 and 193 components retained. Repair offsets enter only
radial order zero. The independent even mean is evaluated as
its actual coefficient.

The resulting ordinary derivatives give
$$
 \eta^{(p)}
 =-\sum_{l=0}^p{p\choose l}\gamma^{(l)}m^{(p-l)}.
 \tag{L.11}
$$
Neither a difference of unrelated values nor the derivative of
a value-only interval is used.

## 4. Complete radial bounds for the leading fold amplitude

Write $\rho=r_*-r$, $e_d=-d$ to distinguish the drift from (L.1),
$k=-K/\rho$, and $a=\eta\sqrt{k}$. The root is fixed on this
parameter window. The exact divided-derivative formulas imply
$$
 |k_\rho|\le\tfrac12\sup|K_{rr}|,\qquad
 |k_{\rho\rho}|\le\tfrac13\sup|K_{rrr}|.
 \tag{L.12}
$$
These are integrals along the actual root-to-point segment,
using $K(r_*)=0$; they introduce no singular division by $\rho$.
The ordinary product rule now bounds $a_\rho,a_{\rho\rho}$
from (L.11)--(L.12).

Let $R$ be a closed upper bound for $|\rho|$ on the exact cover,
$D_j=\|\partial_\phi^j d\|$ on the outer old strip, and
$E=\exp(D_1R)$. The complete upper bounds $D_0,D_1,D_2$ are reused
from the actual old rows. Higher $D_j$ are bounded from the full
finite Fourier products, not from a finite output projection.

For either genuine ray or the common-drift characteristic,
Faà di Bruno's variational equation gives
$$
 C_j=E\sum_{l=2}^jD_l\,
       {\rm Bell}_{j,l}(E,RC_2,\ldots,RC_{j-l+1}),
 \qquad j\ge2.
 \tag{L.13}
$$
Thus $|X_\phi|\le E$ and
$|\partial_\phi^jX|\le|\rho|C_j$ for $j\ge2$.
The common-drift integral for $A$ in (M.3) then yields
$$
 |\partial_\phi^jA|
 \le|\rho|A_j,\qquad
 A_j=\tfrac35a_+
     \sum_{l=1}^j C_{l+1}
        {\rm Bell}_{j,l}(E,RC_2,\ldots).
 \tag{L.14}
$$
Only $j\le4$ is needed below.

For real parameters the principal radial speed on the negative
side is real. On the positive side its imaginary displacement
is bounded by the already paid optical integral $O_+$.
Since the drift is real on the real angle,
$|\operatorname{Im}d(x+iy)|\le D_1|y|$.
A sufficient analytic-domain condition for all leading
characteristics is therefore
$$
                  E(\sigma_{\rm lead}+O_+)<\sigma_{\rm coeff}.
 \tag{L.15}
$$
This sharper strip condition does not identify a real radial
piecewise domain with a complex radial disk. It is only an
angular continuation estimate, also valid for a characteristic
on a subsegment.

The following formulas are a finite nonsingular differentiation
recipe. Use the exact relations
$$
 X_\rho=e_dX_\phi+\tfrac23a\rho^2A_\phi,\qquad
 2\rho(A_\rho-e_dA_\phi)+3A=3aX_\phi .
 \tag{L.16}
$$
After $j$ angular derivatives the second identity gives
$$
 \rho^2 A_{\rho\phi^j}
 =\rho^2\sum_{l=0}^j{j\choose l}(e_d)_{\phi^l}
                        A_{\phi^{j-l+1}}
       +\tfrac32\rho(aX_{\phi^{j+1}}-A_{\phi^j}).
 \tag{L.17}
$$
Consequently differentiating the first identity twice never
requires a separate bound for $A_\rho/\rho$.
Together with actual $d_{\rho\phi^j}$, (L.13)--(L.17) give all
$X_{\rho\phi^j}$ for $j\le3$ and
$X_{\rho\rho\phi^j}$ for $j\le2$ used below.

Let $\chi(s\rho;\rho,\phi)$ be the common-drift backward
characteristic. Its initial and final time differentiation gives
$$
 \chi_\rho=s\,v(s\rho,\chi)-\chi_\phi v(\rho,\phi),
 \qquad v=-e_d .
 \tag{L.18}
$$
If $P_0,P_1,P_2,P_{00},P_{11}$ bound respectively
$\chi_\rho,\chi_{\rho\phi},\chi_{\rho\phi\phi},
\chi_{\rho\rho},\chi_{\rho\rho\phi}$, sufficient bounds are
$$
\begin{split}
 P_0&=D_0(1+E),\\
 P_1&=2D_1E+RC_2D_0,\\
 P_2&=D_2(E^2+E)+3D_1RC_2+D_0RC_3,\\
 P_{00}&=(1+E)D_{\rho,0}+D_1P_0+D_0P_1,\\
 P_{11}&=2ED_{\rho,1}+D_2EP_0+2D_1P_1+D_0P_2+RC_2D_{\rho,0}.
\end{split}
 \tag{L.19}
$$
All suprema in these expressions are on the same outer angular
domain. The formulas follow by differentiating (L.18);
they do not take a derivative of an independently rounded flow
interval.

Insert (L.18)--(L.19) into the exact integral
$$
 A(\rho,\phi)=\tfrac32\int_0^1\sqrt{s}\,
        a(s\rho)X_\phi(s\rho,\chi(s\rho;\rho,\phi))\,ds.
 \tag{L.20}
$$
The ordinary product and chain rules now give
$A_\rho,A_{\rho\rho},A_{\rho\phi},A_{\rho\phi\phi},
A_{\rho\rho\phi}$. For each factor $s^p$, the weight integrates
exactly to $3/(2p+3)$. This is a finite recipe using only
(L.12)--(L.19), with one necessary seam correction next.

The function $a$ is continuous, but $a_\rho$ can jump at an
original polynomial seam. Differentiating (L.20) twice must
retain its distributional second derivative. If $h_s>0$
is a verified lower bound for the absolute distance of every
such seam from the true root, and
$J_a=\sum_{\rm seams}|[a_\rho]|$, additional sufficient fees are
$$
 \Delta A_{\rho\rho}\le{3EJ_a\over2h_s},\qquad
 \Delta A_{\rho\rho\phi}\le\tfrac32 C_2EJ_a .
 \tag{L.21}
$$
Indeed each crossed seam has $s_c=|\rho_c/\rho|$ and contributes
$\tfrac32s_c^{5/2}[a_\rho]X_\phi/|\rho|$ before angular
differentiation. For the second inequality
$|X_{\phi\phi}(s_c\rho)|\le s_c|\rho|C_2$ cancels
that denominator. No seam correction is needed for a first
radial derivative of the continuous integrand.

Here
$[a_\rho]=-\sqrt{k}\,\gamma[m_\rho]$ in absolute norm,
since the intrinsic coefficients are smooth and the repaired
mean is continuous. The exact original even-mean derivative
jumps saved by the completed piecewise native therefore pay
$J_a$. Its second and third derivative jumps remain saved for
the later amplitude residual; their large sizes are not suppressed.

## 5. Leading derivative array and a complete first-forcing bound

Use the already proved exact leading amplitudes
$$
 G=(k_*/\eta_*)^{1/6}A^{1/6}k^{-1/4}
          \exp\left(-2\int_{r_*}^{r}b\langle S\rangle\,dr\right),
 \quad
 a_0=G(X_\phi^2-TT_\phi^2),\quad
 b_0^{\rm Airy}=-2i\epsilon GX_\phi T_\phi .
 \tag{L.22}
$$
The radial exponential is independent of the angle. Its
logarithmic $\rho$ derivatives are
$2b\langle S\rangle$ and
$2(b\langle S\rangle)_\rho$.
Thus all derivatives of $G$ of total order at most two follow
from
$$
 \log G={\rm constant}+\tfrac16\log A-\tfrac14\log k+\log E_G
 \tag{L.23}
$$
using the true $A_-,k_-$ gaps and (L.12), (L.20)--(L.21).
Derivatives of $T=-\rho A^{2/3}$ and of $T_\phi$ use the
same finite chain rule through total order three for $A$.
Only the mixed third derivatives already listed after (L.20)
are needed, not $A_{\rho\rho\rho}$.

For complete implementation, store each nonnegative derivative
majorant divided by its multiindex factorial. Multiplication is
the ordinary finite two-variable convolution. For a power $A^p$,
the positive-order coefficient of total degree $m$ is bounded by
$$
 \sum_{l=1}^{m}\left|{p\choose l}\right|
       A_-^{p-l}\,(\Delta A)^l
 \tag{L.24}
$$
coefficientwise, when $p-l<0$; a positive exponent instead uses
$A_+$, and the zero-degree term uses its own actual bound.
This is a finite derivative identity, not an infinite-series
convergence assertion. Take $p=2/3$ and multiply by $-\rho$.
The source retains both ordinary second derivatives and the
fees (L.21).

Let $W_{i,j}$ bound the sum of the two leading amplitude norms
after $i$ radial and $j$ angular derivatives, for $i+j\le2$.
A direct complete norm bound for (L.5) is
$$
\begin{split}
 \|F_a\|+\|F_b\|\le\mu_-^{-1}\big[&
 W_{2,0}+2D_0W_{1,1}
 +(D_0^2+\eta_+^2|K|)W_{0,2}\\
 &+(D_{\rho,0}+D_0D_1)W_{0,1}
 +\|T_0\|(W_{1,0}+D_0W_{0,1})\\
 &+\{\|V_0\|+\|\vartheta\|\|H^{-1}\|\|H_D\|\}W_{0,0}
 \big].
\end{split}
 \tag{L.25}
$$
The bound includes the entire one-gain radial contribution.
The exact principal identities give
$DX=-(2/3)a\rho^2A_\phi$ and
$DT=aA^{-1/3}X_\phi$, so $H_D$ is bounded without
differentiating a small numerical fold residual.
The determinant of $H$ is the actual noncharacteristic
quantity $-(X_\phi^2+TT_\phi^2)$, paid by the fold gap.

These are analytic suprema on $\sigma_{\rm lead}$.
For a smaller forcing strip $\sigma_F$,
the derivative bound is
$(\|F_a\|+\|F_b\|)/(\sigma_{\rm lead}-\sigma_F)$.
It is the sup-norm Cauchy fee, not the Wiener
$1/(e\,{\rm loss})$ fee.

If $\sigma_{\rm out}+M_R<\sigma_F$, the explicit coefficients
(F.15)--(F.16) of
[the nonsingular forced-amplitude theorem](R133-supplement-nonsingular-forced-Airy-amplitude-bounds-on-real-pieces.md)
then give actual sup bounds for both $a_1$ and $b_1$ with zero
common root trace. The complete branch factor is included.
No division of separately bounded branch sums by $\sqrt\rho$
is used. A useful proposed allocation for the public consumer is
$\sigma_{\rm coeff}=1/16$, $\sigma_{\rm lead}=3/64$,
$\sigma_F=5/128$, $\sigma_{\rm out}=1/64$; both (L.15) and
the last strict inequality must actually pass.

## 6. What this calculation pays

The resulting $F_a,F_b$ are the actual first forcing in (L.6),
with complete coefficients, the old angle, both profiles and
all real-piece radial differentiation. The next amplitudes
are actual characteristic integrals and have finite uniform
bounds on the declared real-piece domain.

This alone is not the norm of the reconstructed full Jacobi
residual. That residual also includes the next finite
$\mathcal L_k$, the exact old-$I/J$ endpoints, the true old mean,
the finite-head forcing, and the real reconstructed jumps
(M.16)--(M.17). Those must be paid before evaluating the final
strong constant or claiming that its product with the actual
scalar inverse is small. The companion source preserves this
scope explicitly.
