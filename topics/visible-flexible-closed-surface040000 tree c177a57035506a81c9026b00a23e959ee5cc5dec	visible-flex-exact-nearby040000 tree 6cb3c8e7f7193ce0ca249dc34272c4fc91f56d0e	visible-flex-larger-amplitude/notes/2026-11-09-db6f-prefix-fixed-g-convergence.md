# Fixed-g macro coupling: convergence record

All rows below use the physical profile selected by the completed macro M8
coupling: outward flat ramp, `vu=.17`, `vd=.18`, `ramp=.4`, `ramp_eta=.05`,
one cycle, and `delta=.07254443456654512`. The angular chart and reference
warp amplitude .1 and the complete physical weighted-tail parameters are
identical. The support amplitude is an output in the fixed-metric rows.
Numerical tail depth is a cutoff of the same infinite material metric.

This separation was also checked in the constructor code, rather than
inferred only from equal parameter dictionaries. The physical source call
in`closing_recalibrated_tail.mjs` explicitly uses`modes:1`,
`depth:protectCell`,`steps:1` and`quadrature:16`, while its physical
formula reads the frozen calibration/geometry inputs. The weighted wrapper
uses the frozen`warpWeightLevels` and`warpSteps`. The worker's Fourier order,
finite shooting depth, shooting parts, RK steps and angular quadrature do
not recalibrate that physical profile. The current transitive source hashes
are retained in`2026-11-09-db6f-prefix-source-dependencies-v2.json`.

The prefix has the same property. In physical angle its target is
$g=ds^2+a(s)^2d\theta^2$. `PlanarSymmetryFlow.profile` depends on the frozen
flat law and the bridge constructed solely from the frozen port cut. Mode
count and gauge amplitude occur in the representation, not in that radius
profile. The numerical angle is
$\theta=\psi-e(s)\sin(3\psi)/3$, where the fixed recorded spline and
quintic cutoff determine $e(s)$ from the fixed reference amplitude .1.
Consequently, writing $\rho=\theta_\psi$, the same material metric is
$g_{ss}=1+a^2\theta_s^2$, $g_{s\psi}=a^2\theta_s\rho$,
$g_{\psi\psi}=a^2\rho^2$. The small changes in the *output* support
amplitude are changes of the embedding, not changes of this target metric.

The errors in this table are the saved sampled Fourier/Darboux diagnostics.
They are not the final continuous full-Cartesian metric certificate.

| Modes | Parts × RK steps per raw profile | Prefix/tail jointly solved | Prefix metric | Tail metric | Support amplitude |
|---:|---:|:---:|---:|---:|---:|
| 8 | 2 × 32 = 64 | yes | 1.11865856e-7 | 3.16461861e-7 | .1 |
| 8 | 2 × 64 = 128 | yes | 1.11837680e-7 | 3.17850288e-7 | .09999992988510656 |
| 8 | 2 × 128 = 256 | yes | 1.11837762e-7 | 3.22572348e-7 | .09999993007504046 |
| 12 | 4 × 64 = 256 | yes | 8.95134441e-9 | 1.96496598e-8 | .09999976505231697 |
| 14 | 8 × 32 = 256 | yes, tail N256 continuation path | 7.94615495e-8 | 8.56381832e-9 | .09999976437833741 |
| 16 | 8 × 64 = 512 | M14 continuation running at N256 | pending | pending | pending |

The M8 metric plateau is an angular truncation effect and is not claimed
as decreasing radial error. The small increase in the sampled tail maximum
under radial refinement also reflects the denser diagnostic sampling. The
earliest M12 tail-only response used the M8 cut height padded to12modes;
it remains a historical initial response, not the final checkpoint. The
M12 row now records the completed coupled prefix and final actual tail.
The first three rows have depth10; the higher-mode rows use depth12
without changing the metric. The M14 run uses N256 angular quadrature
as a numerical warm path; the final M16 target remains N512.

## Actual radial C2 comparison

`2026-11-09-db6f-prefix-flat-v17v18-radial32-64-128-cauchy.json` was generated
by `db6f-prefix-convergence-packet.py`. It first checks equality of the
frozen material inputs, then compares4416meridian nodes and1024angles in
one common physical `(s,theta)` coordinate system.

| Physical jet supremum difference | 32 → 64 | 64 → 128 |
|---|---:|---:|
| Position | 7.03073e-8 | 1.90455e-10 |
| Meridional first derivative | 9.99675e-8 | 2.47421e-10 |
| Angular first derivative | 3.16766e-7 | 8.58210e-10 |
| Meridional second derivative | 1.36493e-4 | 6.55371e-9 |
| Mixed second derivative | 9.74326e-7 | 2.60680e-9 |
| Angular second derivative | 1.46649e-5 | 3.97204e-8 |

The32→64 comparison also tightens prefix collocation tolerance to2e-9 and
increases its mesh from778 to2570nodes. The64→128 pair retains that
tolerance and has2570nodes in each result. Its mean cut height changes by
-1.52383e-11. These are sampled C2 Cauchy diagnostics of the prefix, not a
uniform proof or a substitute for the tail's Cartesian comparison.

## Original equations checked after an affine inner solve

The128-step row uses the optional shared-engine implementation and the
outer-actual/inner-affine DN algorithm. One outer correction sufficed. The
original nonlinear boundary residual was7.21645e-16 against the original
weighted tolerance1e-8. Its actual tail residual at that check was
5.34894e-11. The final separate true-DN seam audit gave8.19167e-11, mean
first/second mismatch1.45417e-12/-1.83200e-11, nonmean first mismatch
2.60209e-18 and nonmean second mismatch2.45580e-9. It used four actual DN
calls. The64-step reference used the original actual-DN-at-every-query
algorithm and18actual calls. Their agreement above also checks the
optional solver against a different numerical path; no affine response
is treated as a solved tail or used for the final seam audit.

## Completed M12 joint solve

The M12 run completed with2570nodes, maximum RMS collocation residual
1.99713151e-9 against tolerance2e-9, and sampled physical boundary residual
1.01602e-18. It used the original actual-DN-at-every-query algorithm and
18actual tail calls. The final actual tail has shooting residual
1.54223814e-9, minimum leading coefficient .1915650642, and formal
curvature6.42892223. Mean first/second seam differences are
1.60982e-14/-2.10942e-13; nonmean first/second differences are
1.73472e-18/1.42580e-10.

Compared with the completed M8/128 row at the same total256RK steps per
raw profile, the prefix metric diagnostic decreases by12.49fold and the
source-developed tail metric diagnostic by16.42fold. These remain
sampled diagnostics. The full explicit M12 Cartesian tail has now also
been exported: its actual Cartesian metric diagnostic is1.96721814e-8,
a16.39fold decrease from the M8 native128 export. Its actual curvature
diagnostic is6.42897612. The manifest is
`2026-11-09-db6f-tail-inc-flat17-m12-p4-native64-n8-s64-q512-manifest.json`.
`sourceFullD=8.23926300e-5` is a second-order Darboux
defect and must not be relabelled as the metric error.

The saved M12 numerical checkpoint retains one stale descriptive string
in `summary.scope`, inherited from the early process's `adaptive.audit`,
saying "Linear finite port only". Its actual configuration, final
`tail_seam`, and final `_tail_0018` record unambiguously contain the true
nonlinear coupled response. The string is a metadata erratum, not a
different solve. The checkpoint is kept unchanged so its recorded hash
remains stable. Later runner source already corrects the description.

`2026-11-09-db6f-prefix-flat-v17v18-frequency8-12-cauchy.json` checks the
identical frozen inputs and compares3654radial nodes and1024angles.
The sampled physical differences are:

| Jet | M8/128 → M12/64 |
|---|---:|
| Position | 1.72921e-7 |
| Meridional first derivative | 9.79857e-7 |
| Angular first derivative | 2.89344e-6 |
| Meridional second derivative | 3.82286e-5 |
| Mixed second derivative | 5.13690e-5 |
| Angular second derivative | 2.07976e-4 |

The support amplitude changes by-1.65023e-7 and the mean cut height by
1.32041e-8. A single frequency comparison is not an infinite Cauchy proof.
The M14 intermediate path was started in parallel after the original
M16 warm Newton residual decreased only from14.75935 to14.52212. The
original path was later stopped at14.434856 after the M14 initial true
tail converged, to preserve resources for the better continuation path.
Its inputs, raw lift and trace remain saved in the companion
`fixed-m16-d12-p8-s64-outer-interrupted.json` record. This is a solver-path
decision, not a branch nonexistence result. M14 uses a completed M12 tail
only as an initial guess; the physical metric is unchanged. Its initial
true response has shooting residual9.2534e-10, sourceMetric8.5642e-9,
and positive minimum leading coefficient .116947. The completed M14
joint solve and its nonmonotone prefix diagnostic are recorded below.

## Completed M14: an explicit nonmonotone prefix diagnostic

The M14 joint checkpoint `flat-v17v18-fixed-m14-d12-p8-s32-q256-outer`
has2633nodes, RMS collocation residual1.99789982e-9, and four actual
tail calls. The original nonlinear outer boundary residual is
2.08563930e-14; a separate final physical BC evaluation gives
4.17127860e-17. The final true response is `_tail_0004`, with shooting
residual3.85559519e-10, sourceMetric8.56381832e-9,
sourceFullD4.90828194e-5, and minLeading.1169560746.

The prefix metric rises from the M12 value8.95134e-9 to7.94615e-8.
Its projected inlet differs from the exact support curve by1.23306e-9
in position,5.97567e-8 in first derivative, and3.00035e-6 in second
derivative; the inlet metric diagnostic is1.32299e-8. The new highest
central support coefficient is1.18921e-8. These are saved facts and
must not be hidden by reporting only the improved tail metric. It is
not yet justified to claim a monotone whole-surface frequency sequence.
The prefix localization script separately evaluates source projection
and saved interpolation on the same state, to resolve the cause.

M16 now starts from this completed M14 joint solve, with both prefix
and tail N256 quadrature, parts8×steps64, and the original2e-9 solver
tolerance. A final N512 actual-DN correction is still required.
The optional saved-adaptive-mesh initializer only changes the initial
guess. Its same-order and M14→M16 checks preserve the physical nonmean
Fourier profile exactly outside the explicitly recorded inlet adjustment,
move saved physical nodes by at most4.44e-16, satisfy the inlet exactly,
and reject a changed physical profile. See
`2026-11-09-db6f-prefix-preserve-restart-check-m14.json`.

## Explicit Cartesian tail comparison at M8

The latest finite native64/native128 Cartesian tail metric diagnostics
are3.22525713e-7 and3.22357830e-7. The respective `fullTensor` quantities
8.20271e-4 and6.42445e-4 are second-order tensor diagnostics, not relative
metric errors.

`2026-11-09-db6f-prefix-tail-flat17-native64-128-c2.json` compares the
two explicit perturbations with outward-rounded coefficients on27697
exact common physical radial spans. Signed planar modes are extended
by exact zeros to a common union, because the exports retain degree96
and192 respectively. Their recorded physical statistics and all common
source hashes are identical. Both have the same inner and outer anchors
and the same nonlinear mean-height gauge at raw depth8.

The C0/theta/theta-theta/r/r-theta difference bounds are respectively
7.58e-10/5.24e-9/4.77e-8/5.98e-8/6.70e-7. The rr bound is .0324932,
localized to r in[.5209378646,.5209492975]. A separate floating diagnostic
there finds rr difference .0118198 at theta0, so a real representation
refinement effect remains. This does not prevent the small metric
diagnostic, but it must not be advertised as a tail C2 tolerance result.
The sibling's independent source localization,
`2026-11-09-db6f-tail-critical-source-native64-128.json`, finds source
height-rr difference4.60995e-8 and planar-rr difference3.28077e-9 at the
same radius; changing the planar finite-difference step changes those
source jets by less than4.48e-10. These are numerical source diagnostics,
which locate the large finite-map difference in radial interpolation,
not a certificate of the exact ODE. The M12 export's fullTensor remains
6.41913e-4 at the same radial resolution even though its metric decreases;
this further emphasizes the distinction between the two diagnostics.
The background cancels only in the common unassembled height gauge;
closed-map vertical placement constants and endpoint collars are not
included in this exterior perturbation comparison. Detailed scope and
localization are recorded in the companion tail-C2 note.

## Checkpoints

- M8/32: `2026-11-09-db6f-prefix-flat-v17v18-coupled-m8-q10-fine.json.gz`,
  final actual tail `_tail_0017.json.gz`.
- M8/64: `2026-11-09-db6f-prefix-flat-v17v18-fixed-m8-d10-p2-s64.json.gz`,
  final actual tail `_tail_0018.json.gz`.
- M8/128: `2026-11-09-db6f-prefix-flat-v17v18-fixed-m8-d10-p2-s128.json.gz`,
  final actual tail `_tail_0004.json.gz`.
- M12 final coupled entry: `2026-11-09-db6f-prefix-flat-v17v18-fixed-m12-d12-p4-s64.json.gz`,
  final actual tail `_tail_0018.json.gz`.
- M14 final coupled entry: `2026-11-09-db6f-prefix-flat-v17v18-fixed-m14-d12-p8-s32-q256-outer.json.gz`,
  final actual tail `_tail_0004.json.gz`; prefix metric is nonmonotone.

Every completed checkpoint has its companion summary/config/reproduction
files. No completion claim follows before the whole-surface all-phase
metric, embedding/reach, exact public seams, fixed-hold size, noncongruence,
frequency convergence and independent rerun gates are all paid.
