# Actual characteristic-density comparison consumer

2026-11-13, reproduce-newton.

**Unrun source.** The native executor is unavailable. This note describes
the executable contract of
[scripts/fourfold_phase_characteristic_density_energy.py](../scripts/fourfold_phase_characteristic_density_energy.py).
It supplies no new numerical growth constant.

The complete equations and source matrices are proved in
[the R110 density supplement](../results/R110-characteristic-densities-mean-and-weak-sources.md).
The independent actual diagonal transport report already passed sixteen
BigInt gates:
[characteristic-density transport](2026-11-13-R110-characteristic-density-transport.json).
The native entry pins its SHA256, full-family identity and exact-arithmetic
source. In particular, the $6.202$ entry is a pure density $L^2$ bound;
the higher density uses $38.459$ for the $J_{\rm char}^{3/2}$ principal
transport and retains the complete low-to-high remainder.

## Inputs and continuous coefficient construction

The entry takes one or more completed original R110 energy reports.
It verifies their producer/dependency hashes, full radial/angular status,
strict-negative status, original field report/array hashes, exact object,
origin, direction and **the full** $p_0\pm10^{-9}$ interval.
It does not accept a source-only receipt, a center-only field, a positive
collar or a list of angular samples.

Each coefficient rectangle is evaluated across its entire declared radial
piece and every closed angular cell. The extra quantities are algebraic
functions of the same complete nine fields. The consumer computes
$A=(\gamma/\alpha)^{1/4}$, $c=\sqrt{\alpha\gamma}$, $B_\pm$,
$s_\pm$, $t=d/A$, and the true mean functionals $h_\pm$.
All divisions require real closed-cell $\alpha,\gamma>0$.
The target $\kappa=-K_0$ is also checked positive.

It adds no new geometric primitive evaluation. The original field errors
already contain the physical-r derivative through angular order two.
The mixed derivative needed in $B_{\pm,\theta}$ is obtained by differentiating
the whole finite radial polynomial, evaluating its finite angular derivative,
and adding the saved complete mixed-derivative error.

For closed-cell angular gaps:

- a finite second derivative is bounded with its complete finite third
  angular moment and the saved **true second-derivative** uniform error;
- a finite radial/first-angular derivative is bounded with the finite
  radial/second-angular moment and the saved **true mixed first-derivative**
  uniform error.

These steps do not assert a third angular derivative for the infinite
error. They use the already complete lower-derivative error uniformly.
Even angular grids with $N>2K$ retain all finite frequencies without DFT
alias. The whole real parameter interval stays inside the same coefficient
balls throughout.

The full periodic-kernel bounds give the complete commutators of
$A^{\pm1},t,B_\pm$ and the signed transport remainders of $s_\pm$.
The saved full Fourier $\mathcal M_{3/2}(\alpha)$ and
$\mathcal M_{3/2}(v)$ supply the high weak-source factors. No nonlinear
quarter-power Fourier truncation is introduced.

## Full comparison and exact radial ordering

Each complete piece produces the matrices $C,R,S_0,S_h$ from R110,
followed by
$$
 D_*=\operatorname{diag}(1,6.202,6.202,1,38.459,38.459),\quad
 B=D_*\begin{pmatrix}C&0\\R&C\end{pmatrix},\quad
 S=D_*\binom{S_0}{S_h}.
$$
All comparison entries are nonnegative true upper bounds.
The vector has six entries because the base and half-order estimates each
carry the **same** physical mean. This is a comparison device, not a second
independent mean port.

The local coupling transition $e^{hB}$ is enclosed by a finite matrix
Taylor sum and a complete explicit remainder.
If $q=h\|B\|_\infty$ and $n$ terms are retained, the scalar tail
$$
 e^q q^n/n!
$$
bounds every missing matrix entry. The consumer adds it to every entry.
All powers of possibly zero real balls are evaluated by repeated
bilinear multiplication. It never calls a numerical matrix logarithm
or assumes an unverified eigendecomposition.

For the piece's radial source, monotonicity of the nonnegative matrix
exponential gives the componentwise complete $L^2$ kernel
$$
 K_i=\sqrt h\,\big\|e_i^t e^{hB}S\big\|_{\mathbb R^3}.
$$
The actual positive upper matrix replaces $e^{hB}$ in the executable,
including its full remainder. Forward and backward global products use
the corresponding actual interval order. Source kernels are propagated
through all later pieces, then their squares are summed using disjoint
radial supports.

The raw diagonal transport factor $D_*$ appears only once at the original
initial endpoint. It is not multiplied at every arbitrary spline seam.
The coupling generators contain $D_*C_*$ because the actual
variation-of-constants kernels act on genuine coupling events.
Thus subdividing an unchanged physical interval does not insert a spurious
factor $6.202$ per subdivision.

The declared pieces must cover a contiguous interval with no gap or overlap.
Every piece must use the same complete actual parameter family.
The energy-weight choice of the *old* report is not a new assumption here:
the density comparison uses its own exact state, with its retained mean.

## Physical reconstruction and full source Gram

The entry retains the exact R107 load
$f_0=-R_0$, $f_r=R_r$, $f_\theta=R_\theta$ and shifted physical momentum
$p=p_N$. Its common source space is
$$
 L^2(dr;\ H^{1/2}f_0\oplus H^{3/2}f_r\oplus H^{3/2}f_\theta),
$$
using physical frequencies $4k$ and weight one on the zero mode.

The outgoing positive map uses the complete identities
$$
 Jq=\tfrac12A^{-1}(Jy_++Jy_-)
             +\tfrac12[J,A^{-1}](y_++y_-),
$$
$$
 Jp=\tfrac12A(Jy_+-Jy_-)
             +\tfrac12[J,A](y_+-y_-),
$$
together with $\|u\|_{H^{3/2}}^2=|m|^2+\|q\|_{H^{1/2}}^2$.
The incoming map likewise retains both commutators, both channels and the
mean.

The output provides:

- the complete ordered six-component comparison;
- the positive two-component physical
  $H^{3/2}u\oplus H^{1/2}p$ comparison;
- a verified homogeneous physical norm upper bound;
- a complete physical source norm upper bound.

If the full five-input weak-source Gram is $G$ in the common source space,
the zero-initial physical endpoint Gram is at most the square of the last
source norm bound times $G$. This uses the whole input Gram, including
all three residual components and every actual angular output.
The sixth regular cap input has zero direct core source; it is retained
in the separate full cap/Schur map.

These outputs do not include true-root/Airy transport, positive collars,
actual canonical/label frame injection or the full feedback inverse.
They cannot be applied to all of $[-1/4,1/4]$ as one hyperbolic window.

## Replay once the native environment is restored

First reproduce or restore the complete nine-field and old energy inputs;
the small execution receipt is insufficient. Then, from the topic directory:
~~~sh
python scripts/fourfold_phase_characteristic_density_energy.py \
  --energy-reports notes/strict_core_energy_gate.json \
  --density-budget notes/2026-11-13-R110-characteristic-density-transport.json \
  --matrix-terms 32 --bits 256 \
  --out notes/strict_core_characteristic_density.json
~~~
The simpler kernel refinement of the old two-level energy can be run
independently on the same inputs:
~~~sh
python scripts/fourfold_phase_strict_core_kernel_tame_energy.py \
  --energy-reports notes/strict_core_energy_gate.json \
  --method signed --bits 256 \
  --out notes/strict_core_kernel_tame_signed.json
~~~
Both methods remain independently valid. Their actually completed
same-domain bounds may be compared after execution. No improvement is
claimed in advance, and neither unrun source is a global inverse certificate.
