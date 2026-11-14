# Full selected-angle feasible-projection warm: executable interface

This is an independent optimizer entry following the actual request24
evidence. It starts at the latest request22 warm, SHA256
`03ca9477cbb759cdbf07117f2540aa51dbe07545985c957289d0f0a3079f4be8`,
and retains the same complete original699 problem. It does not replay the
old request22 direction as a new solution. All scientific numerical work
is restricted by the entry to this public repository's GitHub Actions.

## Fixed problem and finite algorithm

The exact-coordinate chart still enforces the inlet and all constant
core/control rows algebraically. All 338 physical collocation rows per
interval and all 112 physical-phi boundary rows remain in the residual.
The complete actual T112 zero-H Jacobian is held explicitly affine, just
as in the prior warm stages. No new native height is solved here.

At this actual base, define the original fixed-weight complete model

$$
 b=W_rR,\qquad A=W_rDRS^{-1},\qquad
 f(z)=\tfrac12\|Az+b\|^2+\tfrac{270^2}{2}\|z\|^2.
$$

The first direction comes from the unchanged unprojected regularized
operator `[A C^-1; 270 C^-1]`, where
`C=sqrt(original complete column_norm_squared+270^2)`, with LSMR `damp=0`,
`atol=btol=1e-7`, `conlim=1e12`, and at most 200 iterations. The three
previous artificial tangent equalities are replaced by all selected
angular inequalities; they are not original BVP equations.

The selected queries are intervals 473, 475, 477, 479 and 480 at the
original left RMS fraction `0.17267316464601146`. Every original N2048
physical-phi grid angle is retained, giving 10,240 inequalities. For
their actual positive base margins `beta` and complete scaled derivative
`B`, the algorithm uses

$$
 Bz+c\ge0,\qquad c=\tfrac12\beta,
$$

equivalently `beta+Bz >= beta/2`. This fixed one-half reserve is an
optimizer choice, not a changed scientific tolerance. It is motivated by
the actual24 distinction between the nearest first-order exit and the
larger-step nonlinear remainders. It is not a continuous-angle guarantee.

## Complete local operator and projection

`geometry_20261114_full_angle_domain_operator.py` captures the needed
original nodal Jacobian blocks from the **same** single
`CompleteLinearization` construction. It compiles five full angular row
blocks containing both endpoint physical derivatives and all global
scalar derivatives. The complete nonlinear Hermite chain is retained.
The row blocks act only on the union of nine physical node vectors and
the three global controls: 3,045 possible local columns. Inlet/core
coordinates remain in the complete original model; their explicit
contribution to these interior queries is zero under this chart and the
original flow.

Shared endpoints, including node480, and the global controls use the same
coordinates and scatter-add convention. If an endpoint appears in two
original Jacobian chunks, both actual returned blocks are preserved and
only bitwise equal copies may be identified. No dense
`10240 x 236036` matrix is formed.

For a raw LSMR direction `z0`, the local projection minimizes

$$
 \tfrac12\|C_{\rm local}(z_{\rm local}-z_{0,\rm local})\|^2
$$

subject to all 10,240 linear halfspaces, while the outside coordinates
remain fixed. This diagonal metric is **not** the full model Hessian.
All `B/C` row blocks and their normalizations are prepared once. A cyclic
Hildreth dual coordinate iteration, equivalent to Dykstra halfspace
projection, performs at most 200 sweeps. It never recomputes `Gamma @ J`
per row or per sweep. Its coordinate update uses the actual squared norm
of the rounded normalized row.

The projection reports every normalized multiplier, the unnormalized
constraint multipliers, all original-row slacks, stationarity in the
declared `x=C_local*z_local` coordinates, complementarity, sweep history
and the reason for stopping. The stopping scale
`1e-10*max(1, ||x0||)` concerns this finite projection algorithm only.
An iteration limit does not become a new nonlinear acceptance gate or a
claim of projection optimality. These multipliers are not relabeled as
KKT multipliers of the original complete model in R265.

## Feasible descent backup and selection

Projection alone need not preserve descent of the original residual.
The entry therefore makes the following concrete selection in the same
fixed model.

For the actual raw direction, let

$$
 g_0=b^TAz_0<0,\qquad
 h_0=\|Az_0\|^2+270^2\|z_0\|^2>0.
$$

Choose the positive ray factor `min(1,-g0/h0)`, and repair all original
linear inequalities radially using R265's factor

$$
 t=\frac1{1+\max_i((-c_i-(Bz)_i)_+/c_i)}.
$$

The code records a small explicit floating-point headroom and rechecks
every original row after repair. Because `c>0`, the origin is strictly
feasible. The same repair is applied to the projected candidate. This
gives a feasible backup `zb` and a feasible projected candidate `zp`.
No height coefficient is rounded to zero or reinterpreted as the zero
native anchor.

On the feasible segment `z(tau)=zb+tau*(zp-zb)`, `0<=tau<=1`, the entry
uses the exact one-dimensional minimizer of the same damped quadratic:

$$
 \tau=\operatorname{clip}_{[0,1]}
 \frac{-[(b+Az_b)^TA(z_p-z_b)+270^2z_b^T(z_p-z_b)]}
 {\|A(z_p-z_b)\|^2+270^2\|z_p-z_b\|^2}.
$$

If the segment is degenerate it chooses the backup. In exact arithmetic
the segment candidate cannot have less model decrease than the backup.
The actual code instead recomputes the composed vector's full `A z`,
`B z`, `gdot`, damped model decrease and all 10,240 slacks, repairs any
rounded feasibility defect, and falls back to the verified original-ray
backup if the computed model inequality or strict descent is lost.

This is a finite feasible direction construction. It does not claim to
solve the full R265 constrained quadratic or to have a small full-model
KKT residual. The full original damped gradient and a clearly labeled
zero-dual R265 bound are retained as diagnostics.

## Original nonlinear checks and saved data

The chosen coefficient direction is `z/S` exactly once. Original
backtracking tries at most the same 17 alphas `1, 1/2, ..., 2^-16`. Each
trial recomputes the original real nodal/midpoint RHS and right boundary.
The merit is the original `0.5*||Wr R||^2` with the same fixed `Wr`; the
positive damping is not inserted into this nonlinear merit. The original
predicted-decrease ratio, reduction floor, complete two-RMS and uniform
rho checks remain unchanged. The entry also reads all selected angles
from each real trial for diagnosis; these readouts do not substitute for
the complete original domain checks.

An accepted optimization step is written immediately as a complete
`warm-001.json.gz`, always with `success=false`,
`new_coupled_finite_acceptance=false` and no closed-surface claim. It
preserves the full scalar formula, actual controls, all physical states,
complete RHS and producer hashes. The FD wrapper then actually reruns the
original full affine Rphi derivative check at that new warm, with the
original directions, three centered levels, Richardson estimator and
`5e-5` implementation threshold. It does not rename an old FD pass.

Principal diagnostics are the original complete operator check, captured
full-angle row files and manifest, independent full-angle derivative and
adjoint checks, raw LSMR direction, local projection arrays/history,
complete candidate-selection slacks, selected actual direction, full
10,240 final linear margins, all tried original nonlinear domains and
per-trial selected-angle arrays. Large array files remain separate from
the nested compact warm provenance.

## CLI

The initial frozen source identities, statically parsed without local
scientific execution, are:

| Source | Bytes | SHA256 |
| --- | ---: | --- |
| `geometry_20261114_full_angle_domain_operator.py` | 38,319 | `af7966fa1417d9cae3481238397314037c656492ff8005cfc6ba2b4cdb3082f7` |
| `geometry_20261114_full_angle_projection_warm.py` | 36,439 | `7d75a44a2e5a736c68e440ffc1a55533f9ea7aa6bbed4430980dc0ad974b0152` |
| `geometry_20261114_full_angle_projection_response.py` | 2,451 | `90e7addef0e03375b40968f54fb55ce85dc02c3f5cb123f895f100af663f2e92` |

The four original input hashes remain the pinned accepted96,
prepared699, actual completed T112 zero-J response and T112 configuration
used in request22. The independent entry is:

```sh
python computations/geometry_20261114_full_angle_projection_warm.py \
  --accepted "$ACCEPTED96" --prepared "$PREPARED699" \
  --tail-anchor "$TRUE_ZERO112" --tail-config "$CONFIG112" \
  --resume "$ACTUAL22_WARM" \
  --expected-resume-sha 03ca9477cbb759cdbf07117f2540aa51dbe07545985c957289d0f0a3079f4be8 \
  --out "$OUT/full-angle-warm" --iterations 1 --lsmr-iterations 200 \
  --damping 270 --projection-sweeps 200 --line-search-steps 17 \
  --budget-seconds 1200

python computations/geometry_20261114_full_angle_projection_response.py \
  --accepted "$ACCEPTED96" --prepared "$OUT/full-angle-warm/warm-001.json.gz" \
  --tail-anchor "$TRUE_ZERO112" --tail-config "$CONFIG112" \
  --out "$OUT/response"
```

The second command runs only if the first produced a verified new warm.
It does not invoke a fresh native tail. A later full coupled solver must
still solve the actual new height and satisfy every original true-tail,
RMS, boundary and final-audit gate.
