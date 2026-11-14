# R133 supplement: the phase Schur row as a complete distributed adjoint source

2026-11-14, visible-exact-astra-ac0d / phase_inverse.

**Proved exact identity, conditional only on the stated genuine circle
conjugacy.** The full principal phase derivative can be represented by a
distributed source on the actual negative body, without an inverse
turning weight and without retaining a spurious root-angle boundary
term. Its state part has the complete adjoint forcing (D.8), including a
nonzero constant second component. This identifies the phase Schur
consumer for a true full regular body inverse; it does not assert that
that inverse or conjugacy has already been constructed.

## 1. The genuine two-ray return and the invariant measure

Use the exact conventions of
[the full counterterm theorem](R133-supplement-full-regular-phase-counterterm-and-actual-error-functional.md):

$$
 F_\sigma=\beta I(u^2+Kv^2)-\sigma\gamma m q,
 \quad q=\sqrt{-K},\quad m=\langle v\rangle,
 \quad (H_\sigma)_r=F_\sigma\circ H_\sigma,
 \quad P=H_-^{-1}H_+ .                               \tag{D.1}
$$

The period is $p_0=\pi/2$ and every angular integral below uses the
normalized measure $d\phi/p_0$. Suppose a true differentiable
degree-one conjugacy has been proved:

$$
 H\circ P=H+\Omega,\qquad H'>0,
 \qquad H(x+p_0)=H(x)+p_0.                           \tag{D.2}
$$

Then $d\mu=H'(x)dx/p_0$ is the invariant probability measure. Denote
the actual inverse intermediate labels by $S_\sigma(r)=H_\sigma(r)^{-1}$
and put

$$
 A_\sigma(r,\phi)=H\bigl(S_\sigma(r,\phi)\bigr),
 \qquad a_\sigma=\partial_\phi A_\sigma.
                                                               \tag{D.3}
$$

These are full actual transported phases and derivatives. They are not
identified with a finite fit. They satisfy

$$
 (A_\sigma)_r+F_\sigma(A_\sigma)_\phi=0,
 \quad
 (a_\sigma)_r+\partial_\phi(F_\sigma a_\sigma)=0,
 \quad A_\sigma(0)=H.                               \tag{D.4}
$$

The inverse labels, density transport and genuine angular Jacobians are
all contained in these equations.

## 2. Exact elimination of the endpoint pullbacks

For an arbitrary full field variation $\dot F_\sigma$, variation of
constants gives

$$
 \dot P(x)=P'(x)\int_0^{r_*}
  \frac{\dot F_+(r,H_+(r,x))}{J_+(r,x)}\,dr
 -\int_0^{r_*}
  \frac{\dot F_-(r,H_-(r,P(x)))}{J_-(r,P(x))}\,dr.
                                                               \tag{D.5}
$$

Insert this into
$\dot\Omega=\int H'(P(x))\dot P(x)\,d\mu(x)$.
For the first term use $H'(P)P'=H'$. For the second change variables
$y=P(x)$ and use $H'(x)dx=H'(y)dy$. The two weights become respectively
$H'(x)^2$ and $H'(y)^2$. On each leg now change variables
$\phi=H_\sigma(r,x)$, so $dx=d\phi/J_\sigma$. The result is the
complete identity

$$
 \boxed{\quad
 \dot\Omega=\int_0^{r_*}
  \left\langle a_+^2\dot F_+-a_-^2\dot F_-\right\rangle dr.
 \quad}                                             \tag{D.6}
$$

The square in $a_\sigma^2$ is essential: one Jacobian comes from
variation of the characteristic, and the other from change of measure.
Using only one would change the true scalar row.

At the root, $S_-=P\circ S_+$, hence
$A_-(r_*)=A_+(r_*)+\Omega$ and
$a_-(r_*)=a_+(r_*)$. The physical root-angle map also cancels exactly
between the two original legs before this calculation. The complete
physical waist-angle variation contributes a conjugacy coboundary
whose integral is zero, as proved in the cited counterterm theorem.
These facts remove a boundary coordinate artifact, not any root
amplitude, first scalar phase, mean equation or positive-cap row.

## 3. The complete state source, including its mean

At fixed metric, a full physical unnormalized moving variation
$h=(\xi,\zeta)$ changes the characteristic fields by

$$
 D_QF_\sigma[h]=2\beta I(u\xi+Kv\zeta)
                       -\sigma\gamma q\langle\zeta\rangle.
                                                               \tag{D.7}
$$

Define
$A=I(a_+^2-a_-^2)$ and $M=\langle a_+^2+a_-^2\rangle$.
The mean-zero primitive is skew-adjoint under normalized angular
integration. Applying $I^*=-I$ in (D.6) gives

$$
 \boxed{\begin{aligned}
 L_\Omega h&=\int_0^{r_*}\langle\ell_1\xi+\ell_2\zeta\rangle dr,\\
 \ell_1&=-2\beta u A,\\
 \ell_2&=-2\beta Kv A-\gamma qM.
 \end{aligned}}                                      \tag{D.8}
$$

The last term is an actual constant angular source. It acts on the
complete even mean and cannot be folded into the nonmean primitive.
The products in (D.8) retain all frequencies. Even if the centre is
finite, neither the transported phases nor this forcing is assigned
finite support.

The source has no $q^{-1}$ singularity in the dual of the actual negative
energy norm

$$ E_0(h)^2=\langle|\xi|^2+q^2|\zeta|^2\rangle. $$

Indeed, since $K=-q^2$,

$$
 (\ell_1,\ell_2/q)=
       (-2\beta uA,\ 2\beta qvA-\gamma M).            \tag{D.9}
$$

At $q=0$ this means its continuous limiting dual expression; the raw
second source itself vanishes. Also $A(r_*)=0$ from the exact root
identity above. Thus the whole source vanishes at the root in the raw
two-state variables. The bound in the energy dual remains finite.

For example, if $\|H'\|_\infty\le H_*$ and
$L_d=\int\|d_\phi\|_\infty$, then
$|a_\sigma|\le H_*e^{L_d}$.
The complete primitive bound $\|I\|_{L^\infty\to L^\infty}=\pi/8$
gives

$$
 \|A\|_\infty\le(\pi/4)H_*^2e^{2L_d},\quad
 M\le2H_*^2e^{2L_d},\quad
 \|\ell\|_{E_0^*}
 \le H_*^2e^{2L_d}
       \bigl((\pi/2)|\beta|R_*+2\gamma\bigr),         \tag{D.10}
$$

where $R_*^2=\sup(u^2+q^2v^2)$. This is a full source bound, not a
finite-mode norm. The sharper actual response-error functional already
proved in the counterterm theorem may be used directly:

$$
 |L_\Omega e|<1.273240H_*\|e\|_{L^2_r(E_0)}.           \tag{D.11}
$$

The true value of $H_*$ must still be supplied by a certified conjugacy.
A sampled derivative of its finite proposal is insufficient.

## 4. Direct metric source and its support

For the actual compact control write
$\gamma_\nu=w\gamma/2$, $K_\nu=-wK+Tw'$,
$T=\beta/(2E_\nu)$. The direct field variation is

$$
 t_\sigma=\beta I(v^2)(-wK+Tw')
                  +\sigma\frac{\gamma mT}{2q}w'.      \tag{D.12}
$$

It is supported strictly inside $[.05,.18]$, away from the true root.
Its scalar contribution is exactly

$$
 t_\Omega=\int_0^{r_*}\left\langle
  (a_+^2-a_-^2)\beta I(v^2)(-wK+Tw')
 +(a_+^2+a_-^2)\frac{\gamma mT}{2q}w'
 \right\rangle dr.                                  \tag{D.13}
$$

There is no missing $w$-speed term: the two terms from $\gamma_\nu$
and the $-wK$ part of $K_\nu$ cancel exactly. The state response is
physical and already includes the variation of the rotational part;
no second $s_\nu$ column is added to (D.8).

## 5. Full regular adjoint and the same parameter Schur

Let $\mathcal A_{\rm reg}$ denote the actual complete body operator
with all original waist $u$ rows and all outer physical regular rows,
including both the actual mean row and the physical fourth-mode row.
The waist amplitude is an output. Formally, and rigorously whenever
the complete source and trace realizations have been paid, solve

$$
 \mathcal A_{\rm reg}^*\psi=\ell_\Omega              \tag{D.14}
$$

with the corresponding homogeneous dual boundary conditions. The source
(D.8) is zero on the positive body. The actual mean may be eliminated
by its proved scalar Green, but its induced distributed and outer
finite-rank paths must be retained. Equation (D.14) does not release
the physical fourth-mode row or replace it by a zero mean condition.

For $q_\nu=\mathcal A_{\rm reg}^{-1}(+\partial_\nu F)$,

$$
 \boxed{\quad S_\Omega=t_\Omega+L_\Omega q_\nu
      =t_\Omega+\langle\psi,\partial_\nu F\rangle
      \quad}                                         \tag{D.15}
$$

with every genuine boundary and interface pairing in the selected
realization included. An approximate response or adjoint instead
leaves its complete residual pairing; it cannot simply be replaced
by equality in (D.15). The complete source in (D.8), together with
the true boundary transposes and scalar mean Green already proved for
this object, specifies those consumers without changing the physical
normalization.

This is a useful alternate phase Schur row, not an additional free
surface parameter. The final $(\eta,\nu)$ is chosen once in the
construction. Every member of the eventual flex family retains that
one fixed metric. A nonzero numerical proposal for (D.15), the complete
principal quadratic arithmetic, and the source identity alone do not
prove the required nonlinear phase loop or the full strong return
inverse.
