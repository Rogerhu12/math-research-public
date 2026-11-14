# M112: actual complete preflight and complete boundary response passed

Public Actions run `43588155190`, source
`5870c8dd`, job `132427013789`, returned artifact `14111735884`
(`visible-mainline-prepare112-43588155190-1`).  This note consumes its
actual data.  It is a prepared full-interval initial guess and an
implementation response check, **not an accepted full-DN field**.

## Complete new field and the unchanged source identity

The original accepted source remains M96/N1024, SHA-256
`b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff`.
Its complete physical coefficients and full `z0` are embedded as a new
M112 initial guess.  All 112 field modes and 112 material-tail rows are
retained; the three actual scalar supports remain
`[0.0495,0.297]`, `[0.3465,0.594]`, `[0.6435,0.891]`.

The actual output records the distinct identities:

- Scalar schema `complete-prefix-controls-independent-field-modes-v3`:
  `base_prefix_M=96`, `field_modes=112`, `tail_modes=112`, and all three
  frozen scalar parameters initially zero.
- Field schema `finite-rotating-phi-fourier-full-state-v1`: 338 physical
  coefficients including the full mean height, N2048, and no analytic
  circle lift.
- Augmented state: 338 physical rows, 112 constant core rows and three
  scalar rows, for 453 rows; 341 left and 112 right boundary rows.

## The whole preflight, not just the earlier 48-point probe

The original 690 full-interval mesh nodes were all retained.  Adding the
six new scalar-support endpoints gave 696 nodes.  On that full mesh,
three lower-fraction RMS queries inside the taper were invalid:

| Position s | Original minimum beta squared |
| ---: | ---: |
| 1.2051920955041622 | -0.06720988865082234 |
| 1.210176547003922 | -0.0943839700700635 |
| 1.215160998503682 | -0.05956920735163784 |

These points precede the circular portion inspected by the short probe.
Inserting these actual positions and evaluating the new analytic initial
guess there produced **699 nodes**.  Every node, every midpoint, and both
original Lobatto RMS fractions then remained in the real finite Frenet
domain on all N2048 angular nodes.  The minimum reported margins were:

| Query set | Minimum beta squared |
| --- | ---: |
| Nodes | 0.005147953719069731 |
| Midpoints | 0.005147953702687613 |
| Lower RMS fraction | 0.005083788608082562 |
| Upper RMS fraction | 0.005082723249235643 |

Preparation took `8.525029988` seconds.  The initial collocation defect
was still `0.0071105950777444905`.  The preflight guarantees only that
the indicated actual evaluations are defined; it does not assert that
the original differential equation is solved or that a continuous angular
domain bound has been proved.

The reusable file is `preparation112/prepared.json.gz`, 4,220,043 bytes,
SHA-256
`0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714`.
Its 699 rows each contain all 453 augmented components.  At its physical
cut all 112 nonmean height coefficients are **exactly zero as stored**.
This permits strict import of the independent, genuinely completed T112
zero-height response when that computation finishes.  It does not permit
importing the old T96 response.

## Actual scalar and full boundary responses

The scalar wrapper matched the original M112 finite RHS at the tested
embedded prefix states with maximum difference `0.0`.  The three actual
interior-support derivative probes had largest centered-FD errors of
about `3.24e-11`.  Their state labels explicitly retain their M96 accepted
origin; they are not called accepted M112 states.

The full direct boundary and all 453 rows of the augmented separated
boundary were tested with the original three centered differences and
two Richardson values.  The complete new dimensions, last field mode,
last core mode and all three scalar controls were included.  The report
returned:

| Quantity | Actual value |
| --- | ---: |
| Largest fourth-order relative directional error | 9.517693336564078e-10 |
| Largest original centered-FD relative error | 8.849219733664494e-6 |
| Unchanged verification threshold | 5e-5 |
| Significant second-order errors contract | true |
| Complete implementation check passed | true |

This response check uses the actual public worker's `ready.linearD`
matrix as a **labeled original linear-graph reference**.  It does not
claim that this matrix is the newly computed nonlinear finite DN Jacobian.
The final coupled solve must use the independently completed true
T112/N2048 response/J and a fresh actual final audit.

| Actual file | SHA-256 |
| --- | --- |
| `preparation112/driver-status.json` | `6ddba15ee29868bf8ed26bde840aec7eb9ab210869163092b7733d5257d072c6` |
| `preparation112/RMS-domain-preflight.json` | `a7a8c8ea96781e79d8c9ba4c6c3882b9b6432ccecda0cf58d7a3529d5851ede8` |
| `scalar112-RHS-response.json` | `9e2af20dabdab8e7902be7e76b9c23d97463daff145f211e5f55b07ac1e30eb0` |
| `boundary112-response/response-check.json` | `4bacf0bdbf00fd919e4de48f0b36c8322d2ea26539abeac9b9ddcf7c0db6bf7f` |

## Direct continuation

The separately named
[`geometry_20261114_lifted_modes_full_dn.py`](../computations/geometry_20261114_lifted_modes_full_dn.py)
requires this exact prepared SHA and its passed full boundary response.
It retains the original accepted96 input check, constructs the new
M112/T112 problem explicitly, reuses the saved whole field, and calls the
original complete outer true-tail/inner Newton/QR process.  Its original
RMS and BC gates, complete final native audit and frozen physical residual
remain unchanged.  Reduced-system SVD and actual linear-residual
locations are recorded at the first genuine factorization.

An additional QR computation using only `ready.linearD` is not used to
accept or reject this mainline.  The previously measured difference
between ready graphs and the actual finite native Jacobian makes such a
proxy rank check insufficient to decide the real solve.  The actual
T112 anchor and the first true full-DN factorization are the next required
computation.
