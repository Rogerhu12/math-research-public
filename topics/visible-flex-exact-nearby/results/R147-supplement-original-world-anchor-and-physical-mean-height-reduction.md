# R147 WMR: original world anchor and complete physical mean-height reduction

2026-11-27, visible-exact-astra-fb31ed6-20261127 / positive_inverse.

**Proved:** the original nontrivial world anchor has the exact orientation
and immutable identity below. Its already paid complete waist alignment
reduces a new physical mean-height parameter pairing to the relative RHI
carrier, with a reference-covector fee below0.000108627. The full coordinate
variation and both physical means are retained. The actual outer position,
outer frame and their variations remain independent ports.

This is an exact reduction and complete error contract for a new signed
pairing. It does not assert that RHI has completed, assign its new pairing
a numerical value, or prove the world-height Schur border. In particular
it does not replace a true tail anchor by the old reference model.

## WMR1. The old reference model and its orientation

The original candidate is
ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413,
with the exact original $\alpha,\nu_0,\eta_0$ of
[G](R133-supplement-complete-141-block-continuous-model-geometry.md).
The producer
[scripts/fourfold_codazzi_moving_connection_frame_probe.py](../scripts/fourfold_codazzi_moving_connection_frame_probe.py),
function Connection.anchor, uses $R=25/8$ and

$$
\begin{gathered}
 \Theta_R=\phi+I(v_R-m_R)/m_R,\quad
 \rho_R=\beta_R/\gamma_R,\quad z_R=-a_R C_{{\rm ref},R},\\
 F_R^{\rm raw}=a_R(\cos\Theta_R,\sin\Theta_R,0),\\
 X_R=(\rho_R\cos\Theta_R,\rho_R\sin\Theta_R,z_R),\\
 Y_R=(-\sin\Theta_R,\cos\Theta_R,0),\\
 N_R=(z_R\cos\Theta_R,z_R\sin\Theta_R,-\rho_R),\quad
 \mathsf Q_R=(X_R,Y_R,N_R).                              \tag{WMR.1}
\end{gathered}
$$

The exact rotational reference has $\rho_R^2+z_R^2=1$.
Consequently $\mathsf Q_R$ is orthogonal with **determinant $-1$**.
The later radial connection is skew and preserves this orientation.
In particular

$$
              e_z^T\mathsf Q_R=(z_R,0,-\rho_R).           \tag{WMR.2}
$$

One must not flip a normal, perform a per-label rotation, silently
orthogonalize a binary64 frame, or replace this matrix by $I_3$.
The relative matrix $A$ in RH/RHI is in $SO(3)$; this is compatible
with the absolute frame having determinant $-1$.

The only fixed world translation is the original one

$$
 H_*={4347844570122155\over4503599627370496},\qquad
                  F^R=F^{R,{\rm raw}}+H_*e_z.             \tag{WMR.3}
$$

The exact-angle verifier
[scripts/fourfold_codazzi_verify_moving_geometry_grid.py](../scripts/fourfold_codazzi_verify_moving_geometry_grid.py),
function exact_anchor, retains the full scalar balls and exact
$\phi_k=\pi k/1024$. It explicitly records
actual_tail_world_anchor_error_not_included = true.
The original floating report likewise retains
true_cap_world_position_and_frame_difference_not_yet_paid = true.
These are mathematical scope statements, not missing zeros to fill.

There is an immutable public copy of the complete final original block.
The original
[identity document](../notes/2026-11-14-R133-complete-exact-waist-grid-alignment-identities.json)
records the following whole objects:

| Input | Whole identity |
| --- | --- |
| notes/2026-11-14-R133-waist-grid-original-model-report.json | 7187 bytes; SHA256 49870375c7397a53b867d67ce94aa8fcd2d86a69bfe7fc3a7f482b9232d30a2e |
| notes/2026-11-14-R133-waist-grid-original-terminal-block.npz | 199666 bytes; SHA256 4d87057a72944913d013636f57c1b90688a5df95264825f86241e47535e5ffa1 |

The latter was added in 931c4f60ac19d1e2e9606fc290111be803b1bad5
and is retained at immutable history
46f127c7153f5393dcd2a00f42d4c1d3662c294d, before the
reproducible-data removal 315bf6e06a2e21fae980f538286dcec6b739bc59.
A later genuinely new consumer can fetch that whole object if needed.
It need not replay the old observe/geometry norms or recreate a block
whose SHA also includes the old summary.

The reduction below is smaller still: it consumes the old complete
alignment bound directly. Neither that binary block nor the old long
geometry ODE is a necessary numerical input for this reduction.

## WMR2. Same selected short background and the paid reference row

Use $b=9/50$ and the original implicit selected member
$(Q_\delta,\nu_\delta)$ of
[NP](R147-supplement-independent-strict-nu-particular-and-signed-waist-column.md).
Here $Q_\delta$ is the physical moving state pair; $\mathsf Q$ denotes
an absolute three-column geometric frame. The compact mean-exact
R144 centre is a different object.

Let $A_\delta(r)$ solve the original passive connection on $[0,b]$
with $A_\delta(b)=I$. Write $\mathsf Q_b^{\rm raw}$ for the old exact
reference-model frame at $b$. Define its selected short reference row by

$$
 q_0^{\rm ref}(\phi)
     =e_z^T\mathsf Q_b^{\rm raw}(\phi)A_\delta(0,\phi).     \tag{WMR.4}
$$

This is the short model with the old frame at $b$ held fixed. It is
not an assertion about the actual tail frame of an unknown closed solution.

The complete old waist alignment is already paid:
[G.2 and G4](R133-supplement-complete-141-block-continuous-model-geometry.md),
with
[A.1](R133-supplement-exact-waist-grid-and-complete-canonical-alignment.md),
give the whole-angle operator estimate

$$
 \|\mathsf Q^{\rm raw}(0)-\mathsf Q^{\rm can}(0)\|_{\infty,\rm op}
                 <0.000108594777739,\qquad
             e_z^T\mathsf Q^{\rm can}(0)=e_1^T.            \tag{WMR.5}
$$

This includes the complete directed radial error and the full angular
alignment error, not just the 512-point floating discrepancy.

By [D1--2](R133-supplement-exact-selected-parameter-core-differences-and-finite193-transfer.md),
on the required short interval the physical centre repair costs less
than $3.861\,10^{-18}$ and $|\delta_*|\|Z\|_{A^0,\rm pair}\le19\,10^{-10}$.
The full physical state difference from the raw state is therefore
less than $2\,10^{-9}$; the metric difference is less than $10^{-10}$.
These bounds include the actual means.

Apply the exact orthogonal Duhamel comparison
[C.16](R133-supplement-complete-C0-state-and-nu-geometry-response.md)
only on $[0,b]$. Its nonnegative coefficient integrals are bounded by
the already paid full-interval integrals. No selected core outside
its defined interval is needed. Hence

$$
 \|A_\delta(0)-A_{\rm raw}(0)\|_{\infty,\rm op}
 \le15.736315(2\,10^{-9})+0.304809(10^{-10}).                \tag{WMR.6}
$$

Adding these genuine component bounds to (WMR.5), without subtracting
one upper bound from another, gives

$$
 \boxed{\quad
 \|q_0^{\rm ref}-e_1^T\|_\infty
                  <\kappa_{\rm ref}:=0.000108627 .
 \quad}                                                     \tag{WMR.7}
$$

For an actual independent frame $\mathsf Q_b$, set
$q_0=e_z^T\mathsf Q_b A_\delta(0)$ and
$B_Q=\|\mathsf Q_b-\mathsf Q_b^{\rm raw}\|_{\infty,\rm op}$.
Real orthogonality gives
$\|q_0-q_0^{\rm ref}\|_\infty\le B_Q$. The value $B_Q$ remains
an independent actual anchor input and has not been computed here.

## WMR3. Exact world functional and its complete coordinate variation

Use the full relative RHI functions at the waist,

$$
 A=A_\delta(0),\quad x=x(0),\quad y=y_\nu(0),\qquad
                w=A^Tx,\quad z=A^Ty.                    \tag{WMR.8}
$$

The variation $y_\nu$ is generated by the full strict particular
$(h,\kappa)=(v_\nu,1)$, including the direct metric terms. It is not a
homogeneous state variation. The exact world formulas are

$$
 F_0=F_b+\mathsf Q_bx,\qquad
 \dot F_0=Y_b+K_b\mathsf Q_bx+\mathsf Q_by,                 \tag{WMR.9}
$$

where $Y_b=\dot F_b$ and
$K_b=\dot{\mathsf Q}_b\mathsf Q_b^T$ are independent position and
skew-frame ports. Local state vanishing at $b$ does not set either
port to zero.

For the original physical angular map $\Theta$, let $m=\Pi v$,
$\mu=\Pi h_2$ and retain

$$
 J=\Theta_\phi={v\over m},\qquad
 \dot\Theta={Ih_2\over m}-{Iv\over m^2}\mu,\qquad
       g=\dot J={h_2\over m}-{v\over m^2}\mu.              \tag{WMR.10}
$$

If the original angular convention includes a varying constant phase,
its full constant is added to $\dot\Theta$ for a nonconstant test.
It changes neither $J,g$ nor the physical mean formula below.
In particular $\Pi g=0$ exactly, but neither $\mu$ nor $\Pi v$
has been removed.

For a fixed physical test $\zeta$ define the normalized height functional

$$
 {\cal H}_\zeta=\Pi_\phi\{\zeta(\Theta)J\,e_z^TF_0\},\qquad
 \psi_\zeta=\zeta'(\Theta)J\dot\Theta+\zeta(\Theta)g.
                                                               \tag{WMR.11}
$$

Changing variables to physical angle and differentiating gives the
complete identity

$$
\begin{aligned}
 \dot{\cal H}_\zeta&=\Pi q_0{\cal K}_\zeta+{\cal P}_\zeta,\\
 {\cal K}_\zeta&=\zeta(\Theta)Jz+\psi_\zeta w,\\
 {\cal P}_\zeta&=\Pi\{\zeta(\Theta)J\,e_z^T
       (Y_b+K_b\mathsf Q_bx)+\psi_\zeta e_z^TF_b\}.
\end{aligned}                                                \tag{WMR.12}
$$

Equivalently $\psi_\zeta=\partial_\phi(\zeta(\Theta)\dot\Theta)$.
Integration by parts changes this term into the original
$-\zeta(\Theta)\dot\Theta\,e_z^TF_{0,\phi}$ coordinate term.
Thus (WMR.12) retains the complete off-shell world $F_{0,\phi}$;
it never replaces it by an unpaid angular connection formula.

For the physical mean $\zeta=1$ the result is particularly small:

$$
\boxed{\begin{aligned}
 {\cal K}&=A^T(Jy+gx),\\
 \dot{\cal H}_1&=\Pi q_0{\cal K}
  +\Pi\{J\,e_z^T(Y_b+K_b\mathsf Q_bx)+g\,e_z^TF_b\}.
\end{aligned}}                                               \tag{WMR.13}
$$

The $gx$ term is essential. A pairing of $y$ alone is not the
physical mean-height column. The fixed translation $H_*e_z$ makes
no contribution to $gF_b$ because $\Pi g=0$. An independent varying
vertical translation in $Y_b$ still contributes and remains a port.

RHI reflection gives $\mathcal K(-\phi)=R\mathcal K(\phi)$ for
$R=\operatorname{diag}(1,-1,1)$. Only its second moving mean is
exactly zero. Its first and third means remain. No reflection
identity sets the entire height column to zero.

## WMR4. A complete new kernel from the unchanged RHI carrier

Suppose the genuine completed RHI result supplies its full private
$2048\times18$ endpoint identity and complete profile errors. Let
$\widehat A,\widehat x,\widehat y$ be its exact trigonometric
interpolants, including the real Nyquist convention. These functions
cannot be replaced by their six moving means.

Let $J_0=v_0/m_0$ be the complete continuous centre Jacobian at the
waist, and put

$$
 g_0={h_2^a\over m_0}-{v_0\over m_0^2}\Pi h_2^a,\quad
 \widehat B=J_0\widehat y+g_0\widehat x,\quad
 \widehat{\cal K}=\widehat A^T\widehat B.                  \tag{WMR.14}
$$

The original whole NP array determines $h^a$. Its whole mean is used.
All following angular measures are normalized. Use joint Euclidean
vector norms and the Frobenius matrix norm, and suppose

$$
\begin{gathered}
 \|A-\widehat A\|_2\le E_A,\quad
 \|x-\widehat x\|_2\le E_X,\quad
 \|y-\widehat y\|_2\le E_Y,\\
 X_2\ge\|\widehat x\|_2,\quad Y_2\ge\|\widehat y\|_2,\quad
 G_2\ge\|g_0\|_2,\quad B_2\ge\|\widehat B\|_2,\quad
 H_2\ge\|h_2^a\|_2.                                     \tag{WMR.15}
\end{gathered}
$$

$E_Y$ is RHI's complete true-particular profile error, not just its
ODE trial error. The saved ASB uniform strong error gives the
actual waist estimate

$$
            \|h_2-h_2^a\|_2<E_H:=1.594684\,10^{-5}.        \tag{WMR.16}
$$

This is the true uniform propagation conclusion of
[ASB](R147-supplement-actual-short-parameter-errors-and-refined-signed-borders.md),
whose whole native record is complete_true_NP_uniform_L2_error_upper.
It does not take a trace of an ordinary radial $L^2$ bound.

The already paid short bounds in
[RRM2](R149-supplement-relative-frame-position-means-in-original-negative-source-windows.md)
give $|m|,|m_0|>16/15$ and
$\|v\|_\infty,\|v_0\|_\infty<18/5$.
Also $\|v-v_0\|_\infty,|m-m_0|<e:=2\,10^{-9}$.
Set $M=16/15$, $V=18/5$ and

$$
 S={1\over M}+{V\over M^2}={525\over128},\qquad
 T={2\over M^2}+{2V\over M^3}={7875\over1024}.
$$

The full, mean-preserving differences obey

$$
\begin{aligned}
 J_*&={V\over M}={27\over8},\\
 \|J-J_0\|_\infty&\le E_J:=Se<8.204\,10^{-9},\\
 \|g-g_0\|_2&\le E_G:=SE_H+TeH_2
              <6.541\,10^{-5}+1.539\,10^{-8}H_2.
\end{aligned}                                                \tag{WMR.17}
$$

For example the $SE_H$ term follows directly from
$h_2/m-v\Pi h_2/m^2$ on the whole $L^2$ space. The background
difference uses
$|m^{-1}-m_0^{-1}|\le e/M^2$ and
$|m^{-2}-m_0^{-2}|\le2e/M^3$. Both occurrences of the true mean
are included.

Define

$$
\begin{aligned}
 E_B&=J_*E_Y+E_JY_2+(G_2+E_G)E_X+E_GX_2,\\
 E_{\cal K}&=E_B+E_AB_2,\qquad U_{\cal K}=B_2+E_B.
\end{aligned}                                                \tag{WMR.18}
$$

Then

$$
 \boxed{\quad
 \|{\cal K}-\widehat{\cal K}\|_1\le E_{\cal K},\qquad
             \|{\cal K}\|_1\le U_{\cal K}.
 \quad}                                                     \tag{WMR.19}
$$

To prove this, expand $B-\widehat B$ as
$J(y-\widehat y)+(J-J_0)\widehat y+
 g(x-\widehat x)+(g-g_0)\widehat x$ and use Cauchy--Schwarz.
Next $A$ is exactly orthogonal and
$\|(A-\widehat A)^T\widehat B\|_1\le E_AB_2$.
This requires no unproved $L^\infty$ error for a numerical
interpolant, no discarded sine components and no extra factor
$\sqrt3$ from separate scalar error estimates.

If the new complete Fourier contraction gives
$c^a=\Pi e_1^T\widehat{\cal K}$, the frozen original
reference-model body contribution is rigorously enclosed by

$$
 \boxed{\quad
 c^a+[-1,1]\{E_{\cal K}+\kappa_{\rm ref}U_{\cal K}\}.
 \quad}                                                     \tag{WMR.20}
$$

For the actual independent anchor, add $B_QU_{\cal K}$ to this
radius and add the actual whole port in (WMR.13). This is an
explicit dependence on an actual anchor error; it does not
declare that error to vanish.

## WMR5. Minimal actual successor and permitted restoration

A first numerical consumer can save the whole signed three-vector
$\Pi\widehat{\cal K}$ with its joint radius $E_{\cal K}$, the
whole $U_{\cal K}$ and the derived original-reference interval
(WMR.20). Its record must retain the independent
$B_QU_{\cal K}$ coefficient and the exact outer-port formula.

Only after a real complete RHI receipt exists may it restore the
necessary original RHI endpoint carrier. Use the unchanged
coefficient construction and original proposal recurrence in
precisely the original cell order. Match the whole final binary64
SHA, shape, byte count and complete ordered chain. Do not call
the old RHI step residual certification, old strip-error
accumulation, old finish mean targets, old NP residuals or old
pairings. An identity mismatch is a restoration failure, not
permission to choose a new carrier.

The contraction must use all trigonometric coefficients and all
products. For $N=2048$, the interpolants have frequency index
at most1024, $J_0$ has degree32 and $g_0$ at most96.
Thus $\widehat{\cal K}$ has degree at most2144. Its mean and
complete Parseval bounds can use exact Fourier convolution or
a directed zero-padded transform of length at least8192.
Pointwise multiplication on the old2048 grid is not the whole
contraction.

Existing whole norms are read from their original records.
Only genuinely new kernel contractions and their necessary
complete norms are evaluated. The original geometry141 block
is not necessary for (WMR.20), and no old long-world ODE or
geometry gate is repeated.

This reduction addresses the true physical mean-height
functional. Nonconstant tests retain the full $\dot\Theta$ and
$\psi_\zeta$ of (WMR.12). The true phase row, independent mean
constraints, world rigid ports, finite/high inverse and final
nonlinear closure remain separate obligations.

## WMR6. New exact saved-bound combinations

The companion
[saved-bound consumer](../scripts/fourfold_codazzi_world_mean_height_saved_bounds.py)
contains only rational combinations of the already completed
constants. The seven new comparisons of WMR2/WMR4 were evaluated
once with exact integer fractions; all passed. No numerical
source field, old geometry target, old NP target or RHI target
was evaluated. The symbolic kernel error assembly is included
for later directed consumers and requires their full actual
input records.
