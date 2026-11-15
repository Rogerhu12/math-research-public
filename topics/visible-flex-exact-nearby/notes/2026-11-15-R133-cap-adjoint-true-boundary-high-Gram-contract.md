# Same-proposal true endpoint and complete high-output adjoint Grams

This consumer completes the endpoint and trial-output inputs of
[R133 full cap adjoint high-to-low boundary Grams](../results/R133-supplement-full-cap-adjoint-high-to-low-boundary-grams.md).
It uses the same fixed repaired M32 background, physical $\eta_0$ and
original $\nu$ as the actual 97-input adjoint proposal and its four
successful residual quarters. No new adjoint trial, intrinsic target,
whole-quarter jet or native midpoint is constructed.

## B.1 Same exact trial, true endpoints and independent mean

The original native is
acb2151b60f24ad88b30e6f7d1d966851abc53c15e45df19df2bfca27c2393c7.
All seven original array receipts are validated. The exact state has
128 odd physical sine amplitudes, one even mean, and 128 nonmean even
cosine amplitudes. There are 97 Euclidean input coordinates: the 96
orthonormal moving odd functions $\sqrt2\sin(4j\phi)$ and the independent
mean input $a$.

At $L=9/10$ the consumer evaluates the original first exact Hermite
polynomial, including its already specified tiny left extension from
the first binary64 node. It does not substitute the value at
$\operatorname{float}(9/10)$. At $R=25/8$ it uses the exact original final
state. All internal values use one shared exact dyadic state per
original node; the two original one-sided derivatives may differ.
Therefore the exact physical value jumps of this particular trial
are zero. No new approximate inverse or boundary condition is inferred
from this continuity statement.

Let the resulting endpoint matrices be $z_L,z_R$. The first- and
second-component means retain the reflection convention: the odd
B mean is zero, and the C mean is a full independent row.

## B.2 Exact background and analytic inverse angle at the true left

The actual mean $m$ is negative. Throughout the bounds below, $\underline m$ and $\overline m$ are positive lower and upper bounds for $|m|$; the $m$ in every exact signed formula retains its original negative sign.

The original first closed quarter contains the true $L$. Its saved
whole intrinsic jets enclose the intrinsic values at $L$. The exact
candidate cubic and full continuous repair offsets supply $u$, $v$,
$m=\langle v\rangle$ and

$$
 \Theta(\phi)=\phi+\psi(\phi),\qquad
 \psi=I_\phi(v/m-1).
 \tag{B.1}
$$

The new consumer only evaluates these saved finite polynomials and
their directed enclosures. It does not call an intrinsic target.
With $\rho=1/16$, it explicitly verifies

$$
 P_0=\|\psi\|_{A_{2\rho}}<\rho,\qquad
 P_1=\|\psi_\phi\|_{A_{2\rho}}<1 .
 \tag{B.2}
$$

The inverse-angle Picard map
$X\mapsto-\psi(\theta+X)$ maps the $A_\rho$ ball of radius $P_0$
into itself and contracts by $P_1$. In particular the true inverse
$\phi(\theta)=\theta+X(\theta)$ has $\|X\|_{A_\rho}\le P_0$.
The displacement condition alone would not establish this conclusion;
both parts of (B.2) are required.

At each of the 4096 quadrature angles a floating Newton value only
chooses a bracket centre. Directed endpoint signs and a positive
directed derivative certify the root. Subsequent interval Newton
intersections contain the same true inverse. All trigonometric
transforms use directed arithmetic.

## B.3 Complete left endpoint covariance

For the input $\lambda=(f,a)$ the exact physical left target is

$$
 d_\lambda=m(f\circ\phi),\qquad
 e_{\lambda,L}=(z_{L,B}-d_\lambda,\ z_{L,C,0}-a).
 \tag{B.3}
$$

For input $f_j=\sqrt2\sin(4j\phi)$ its complete signed Fourier norm on
the physical strip obeys

$$
 \|m f_j\circ\phi\|_{A_\rho}
 \le \overline m\sqrt2\exp(4j(\rho+P_0)).
 \tag{B.4}
$$

The last input column has $d=0$; it still has the independent mean
defect in (B.3). The physical FFT retains modes through 512. The
original $z_{L,B}$ has only 128 modes and is embedded with exact
zeros thereafter. All 97 signed column correlations are retained
in the finite endpoint Gram.

For a function with full signed $A_\rho$ bound $A$, a directed
$N$-point Fourier transform retaining $|j|\le K$ has aggregate
retained alias and omitted-tail bounds

$$
 E_{\rm alias}\le A e^{-4\rho(N-K)},\qquad
 E_{\rm tail}\le A e^{-4\rho(K+1)}.
 \tag{B.5}
$$

There is no additional factor $2K+1$: each original Fourier
coefficient in the alias set is charged once in the full signed
Wiener sum. These bounds use the real odd parity; the negative
Fourier coefficient is not discarded without its matching
positive-frequency contribution.

For the error in column $j$ let $E_j$ be the sum of the two complete
fees in (B.5). Then

$$
 \|E\lambda\|_2^2
 \le\left(\sum_{j=1}^{97}E_j^2\right)\|\lambda\|^2.
 \tag{B.6}
$$

This is a complete Hilbert--Schmidt bound, not a claim of
orthogonality between column errors. A fixed positive-weight
Young inequality combines it with the finite signed Gram to give
$W_L$. The independent C mean row is included before this
combination.

## B.4 Exact trial high output and all composition tails

The reflection-limited identity A.24 of the published theorem is

$$
 \widehat C_H^*\lambda
 =P_{|j|\ge97}I_\phi
   \left[(u/v)f_\phi+
       m^{-2}\{z_{L,C,\theta}\circ\Theta\}\right].
 \tag{B.7}
$$

It uses the original complete C row, including dependence on the
independent input $a$. The angular derivative of its mean is zero,
while its nonmean response to $a$ is retained. The two scalar
primitive means that would occur outside the odd/even reflection
class vanish by parity here. No extension to arbitrary all-$4\mathbb Z$
functions is claimed.

The forward angle $\Theta$ in (B.7) is evaluated directly. Set
$U_\rho=\|u\|_{A_\rho}$, $V_\rho=\|v-m\|_{A_\rho}$,
$\psi_\rho=\|\psi\|_{A_\rho}$ and
$g_\rho=\underline m-V_\rho$. The actual gate $g_\rho>0$ gives
$\|1/v\|_{A_\rho}\le1/g_\rho$. If $c_{k,j}$ denotes the original
left C cosine amplitude, the complete forcing for column $j$ has
the bound

$$
 A_j\le
 \frac{U_\rho}{g_\rho}\sqrt2(4j)e^{4j\rho}
 +\underline m^{-2}
       \sum_{k=1}^{128}4k|c_{k,j}|
                      e^{4k(\rho+\psi_\rho)}.
 \tag{B.8}
$$

The first term is omitted for the independent mean input, while
the second term still includes that column. The exact finite
trial derivative is composed with the complete forward angle, so
the true result generally has infinitely many moving Fourier
modes.

The saved finite high output contains every $97\le |j|\le512$ mode,
with the true primitive divisor $4j$. Its odd forcing coefficient
$g_j$ produces the even amplitude $2\operatorname{Im}g_j/(4j)$.
The complete alias fee in (B.5) is divided by 388, and the tail
beyond 512 by $4\cdot513$. Formula (B.6) and fixed Young weights
give a full 97 by 97 matrix $W_T$. The infinite high input/output
is not replaced by a 512-mode operator.

## B.5 Full true outer port and original positive comparison fee

The consumer checks the original complete actual-$q_*$ native,
its intrinsic object identity and whole affine-parameter scope,
together with the complete physical Green native. The endpoint
reference multiplier $Q_{\rm ref}$ is enclosed using that true
$q_*$ interval and the original positive historical/current
comparison fee. No finite dyadic $q_j$ is identified with the
true reference for free.

It forms all 128 entries of

$$
 e_R=P_\perp z_{R,C}-Q_{\rm ref}Jz_{R,B}
 \tag{B.9}
$$

in the original physical amplitudes and builds its full signed
matrix $W_R$. It separately saves the full B endpoint Gram
$W_{RB}$ and the independent C mean Gram $W_{R0}$.

The original true outer fees remain

$$
 L_D=5.898255\,10^{-6}+\epsilon_{\rm old}+2^{-512},
 \qquad L_0=7.372818\,10^{-7}.
 \tag{B.10}
$$

The comparison used to enclose (B.9) is not subtracted from (B.10).
Keeping both is a valid conservative enclosure of the same true
outer graph. It retains the positive fee and every independent
mean row.

## B.6 Full $H_C$ and complete corrected Green constants

At the true left endpoint, direct complete bounds yield

$$
 C_*\le g_0^{-1},\quad
 C_1\le\overline m\,\|v_\phi\|_{A_0}/g_0^3,\quad
 J_\phi\le1+\|v-m\|_{A_0}/\underline m,
 \qquad g_0=\underline m-\|v-m\|_{A_0}>0 .
 \tag{B.11}
$$

Here $C_\theta=-m v_\phi/v^3$, so $C_1$ is a physical-angle
derivative bound. Hence the all-input even map of P.9 satisfies

$$
 c_*^2=J_\phi(C_*^2+C_1C_*/4)^2 .
 \tag{B.12}
$$

This is a bound for the full even $H_C$, not the original 97-column
finite inlet matrix. The consumer also checks the exact already
completed repaired Green and local Hessian bounds before recording

$$
 \kappa=\frac{13.316116}{1-.003840162}.
 \tag{B.13}
$$

Specifically it reads the corrected gain
original_closed_physical_Green_gains.inner_C_port from the actual
local-Hessian native, and the original complete bridge feedback.
The uncorrected raw-centre gain is not substituted for this field.

## B.7 Saved covariances and remaining work

The directed source keeps complete signed 97 by 97 upper triangles
with the same exact dyadic plus diagonal-slack convention as the
actual body pilot. Physical nonmean Parseval weight is $1/2$ and
the even mean weight is one. Every stage has its own exact array
receipt, and existing successful stages can be reused after a
later publication failure.

The resulting $W_L,W_R,W_{RB},W_{R0},W_T$ and zero physical jump
Gram are inputs to A.19--A.28. They still require the actual
complete7908 ordinary source covariance and the same-input Young
combination. Contracting the resulting $W_{\rm cap}$ with the
true finite193 right-boundary Poisson Gram is another distinct
consumer. No small global feedback, full high BVP inverse,
coupled infinite inverse or true parameter Schur value is
claimed by the present endpoint/high-output calculation.
