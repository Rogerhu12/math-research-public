# db6f prefix work: actual nonlinear coupling and short-core redesign

Status: ongoing numerical research. All numbers below are finite discretization or first-order screening diagnostics; no complete closed surface or exact-solution claim.

## Restarted actual coupling

The latest previously completed genuine nonlinear prefix+tail state is q_support=.02, stored in `2026-11-09-950f-prefix-coupled-v2-m8-q0p02.json.gz`, with terminal tail record `_tail_0024.json.gz`. The interrupted q=.03 run had 14 tail responses but no completed prefix checkpoint.

`db6f-prefix-coupled.py` resumes that branch using the recovered v3 client (warm remeshing only, unchanged physical equations). The first run is q=.03, M8, angular256, prefix tolerance2e-7, physical BC tolerance2e-9, 601 initial nodes, tail depth10/parts2/32 steps. Its complete configuration, every response and log use prefix `2026-11-09-db6f-prefix-coupled-m8-q03`. The first full-Dirichlet warm response converged with residual1.10e-10. A final q=.03 coupled result is still being computed.

## Useful previously unreported short-core observation

The recovered `2026-11-09-950f-prefix-macro-m12-support-distance.json` reports, for the old q=.08 linear-port prefix, ell=0 and 3546 radial samples by1536 angles:

- support/height distance lower-bound diagnostic .159950944791925, minimized at s=0;
- two-ball diameter diagnostic2.77208175272;
- comparison ratio .05770065931.

The underlying section bound is `sqrt(max(R-max_theta(F.u),0)^2 + max(min_theta(z)+ell,0)^2)` when all heights have the indicated sign. Sampling does not prove the continuous lower bound. It does show that a central cylinder of half-length .16 is unnecessary for the most promising numerical geometry. Root is treating the exact held witness and the required all-domain estimates.

## First-order redesign with ell=0

`db6f-prefix-zero-core-screen.py` replays all the stored meridian roots from the previous 81-design flat/cosine screen, choosing q so that the first-order two-ball comparison gives2q/D=.051. It found102 bounded-amplitude roots in53.50 seconds. These comparisons omit nonlinear corrections and the actual tail/caps.

A promising conservative candidate is the flat-acceleration law with

    vu=.15, vd=.3, ramp=.4, ramp_eta=.1, cycles=1,
    delta=.08240009875178618,
    rCut=.6, wCut=.5, unchanged weighted K6 tail.

The selected first-order q=.09605830642234 gives D=3.76699240872, cut height .000850901379765, sampled support/height witness exactly2q, background K=4.173993558 and core K*D=16.26975. This cut is close to the already-computed finite-tail H1=.000851206965 (lambda=.67), unlike the old macro cut .00127046. The higher harmonics and true nonlinear geometry must be solved, not inferred from this comparison.

The flat ramp=.48 design has lower cut .0008199373774 but requires q=.1050989 and D=4.12153, so its core curvature allowance is tighter. The simpler ramp=.4 candidate is tried first.

## New exact profile implementation and current runs

`db6f-prefix-flat-profile.py` adds the already-defined flat-acceleration formula according to the saved physical config `ramp_law=flat`, `ramp_eta`. It does not edit inherited source files. Its derivatives agree with the original screen's explicit profile formula. The config identifies a different physical metric during design.

- `db6f-prefix-flat-linear.py`: full nonlinear Frenet prefix, finite *linear* tail port. First run q=.08/M8, no old nonlinear prefix grafted into the new metric. Output prefix `2026-11-09-db6f-prefix-flat-v15v30-m8-q08`.
- `db6f-prefix-flat-coupled.py`: same physical profile class but the actual nonlinear tail DN; will be used after obtaining the flat linear-port warm start.
- `db6f-prefix-local-design-screen.py`: extends the first-order screen to slower return speeds .18,.22,.26 and ramp_eta=.05, testing whether there is more tail regularity margin without exhausting the global curvature/diameter budget. These are physical design trials, not fixed-metric refinement.

The final promising metric must be frozen before M/radial/depth refinement. Actual mean jets and C1 metric seam diagnostics remain mandatory, as do the all-domain reach, diameter, H, noncongruence and independent rerun gates.

## Successful small-step design continuation and preserved rejected starts

The first flat15 q=.08 direct large-amplitude start did not converge: the saved
summary reports metric .13019 and loss of core curvature margin. It is rejected,
with full state retained. The flat17 q=.1 direct first-order start left the
Frenet domain and also is rejected. Neither failure is a nonexistence result.

The attempted flat17 q=.08 `remap` start was rejected after checking
that its source `950f-prefix-adaptive-design-m8-q08` was itself a rejected old
first attempt (metric .40355), not the later successful `adaptive-cont` state.
It had already exited with a Frenet-domain error when inspected. Its log is retained; no mathematical nonexistence conclusion is drawn from it. Small-step continuation
from a clean q=.01 seed is the useful route.

`db6f-prefix-flat-continue.py` with flat17, M4 and amplitudes
.01,.02,.04,.06,.08,.1 has already completed through .08. Each finite BVP
converged; M4's metric diagnostic grows to1.93e-5 at .08, so these are warm
starts only. The actual tail first height is .000650350 at .08, agreeing with
the planned attenuation. Higher modes and actual nonlinear DN are next.

## Macro M8 prefix and current actual-tail coupling

The flat17 M4 continuation reached q=.1 in20.89s at its last stage. Starting
M8 from that *successful* state converged in32.66s, delta=.07254444640570741,
780nodes. Its finite linear-port prefix has sampled metric1.11868e-7 (almost
entirely the inlet truncation), curvature5.11257, cutH1=-.000812997893 and
core gap .1999585461. Its sampled geometry at ell=0 gives D_ball3.785619358,
outward support≥.8178843, and support/height held comparison .05282056.
For s≤.25, the physical-meridian diagnostics are b=.963612 and L=1.127268;
b²−DeltaL=.703141 and the far-prefix minimum height is .247018.
These are still diagnostics of the finite **linear-port** warm start.

The actual nonlinear tail at this full macro cut has now converged via
.85,.9,.95,1 amplitude steps from the previous .8 solution. At the full
cut, shoot=1.73312e-9 with positive leading coefficient near .1953. The
actual prefix+tail coupled BVP is running under suffix
`flat-v17v18-coupled-m8-q10-fine`; final matching is still awaited.

The geometry loader's initial mesh merge left a few near-coincident knots,
which can cause catastrophic coefficients in a subsequent exact-Hermite
representation. This was a representation bug, not physical source curvature.
The loader now first clusters knots themselves at2e-11 with physical profile
priority, then merges the old mesh. For the macro M8 source it returns851nodes,
minimum span8.16881165e-6 and zero miss at all15 physical profile knots.
See `flat-mesh-source-check-v2.json`; old diagnostic files are retained.

`db6f-prefix-freeze-refine.py` now provides the reproducible fixed-metric
continuation path from any completed actual coupled checkpoint. It freezes
all physical profile/tail parameters and retains the exact commands and hashes;
only M, numerical quadrature, radial steps/parts and finite depth may change.

The final actual coupled macro M8 run completed successfully. The frozen
profile has delta=.07254443456654512 and actual support amplitude .1; the
prefix sampled metric error is1.11865856e-7, the actual nonlinear tail sampled
metric error is3.16461861e-7, minLeading=.19508944, and the final shooting
residual is1.35056538e-10. First/second mean seam defects are-1.06797e-11 and
1.33534e-10. Nonmean first/second seam defects are1.60897e-17 and2.45573e-9.
The checkpoint is`2026-11-09-db6f-prefix-flat-v17v18-coupled-m8-q10-fine.json.gz`;
its final tail checkpoint is the matching`_tail_0017.json.gz`. This is a
finite M8 coupled solution, not yet a fixed-g convergence certificate.

The first fixed-g refinement (M12, depth12, parts2, steps32) failed in the
initial tail warm evaluation with`momentum branch D/S/A rejected`, before
any coupled iteration. Its full records are retained under
`2026-11-09-db6f-prefix-flat-v17v18-fixed-m12-depth12`. It proves no branch
obstruction. A new run under`fixed-m12-d12-p4-s64` refines both the shooting
partition and RK integration and re-solves the true tail and prefix BVP.
Radial refinement must re-solve the tail: using a saved32-step checkpoint
with64/128-step geometry integration alone creates endpoint RK differences
and is not a convergence test of the coupled surface.

The same-g M8/depth10/parts2/steps64 full coupling has now succeeded under
`flat-v17v18-fixed-m8-d10-p2-s64`. Its final actual tail is`_tail_0018`.
The support amplitude is.09999992988510656, with2570prefix nodes. Prefix
metric1.1183768e-7 and tail metric3.1785029e-7 remain at the M8 angular
truncation scale; they must not be described as a decreasing radial error.
The tail has minLeading=.19515727 and shoot1.87238e-10. Mean first/second
seam defects are1.454e-12/-1.832e-11; nonmean second defect is2.456e-9.
The32→64 comparison also tightened the prefix collocation tolerance, so its
changes cannot be attributed exclusively to the tail RK grid.

`flat-v17v18-radial32-64-cauchy.json` checks identical frozen material inputs
and compares4416physical meridian nodes with1024angles. Position changes
by7.031e-8, physical Fs by9.997e-8, and physical Fss by1.365e-4. These are
sampled Cauchy diagnostics only. A same-tolerance M8/128-step actual coupled
run is now running, using the optional shared-engine and outer-actual-DN
algorithm described in`db6f-prefix-high-mode-refinement.md`.

The first M12/depth12/parts4/steps64 true-tail response has converged:
`flat-v17v18-fixed-m12-d12-p4-s64_tail_0001.json.gz`. It still uses the old
M8 cut-height data padded to12modes, so it is not the completed M12 joint
prefix/tail solution. Its tail metric is1.9650224e-8, full Darboux defect
8.23950e-5, minLeading=.19156156, formal curvature6.4289233 and shoot
1.4628074e-9. The16.2fold tail metric decrease relative to M8 is an actual
frequency/refinement result for one fixed physical metric. Full prefix
coupling and Cartesian geometry validation remain pending.

The M8/128 same-g coupled solve has also completed. It used the optional
shared engines and one outer true-DN correction, with original full BC
residual7.21645e-16, then a separate actual seam audit. The final prefix is
`flat-v17v18-fixed-m8-d10-p2-s128.json.gz`, final tail`_tail_0004`.
Its amplitude.09999993007504046 differs from the64-step result by1.89934e-10.
The64→128 comparison keeps the same2e-9prefix tolerance and2570nodes;
sampled C0/Fs/Fss/Ftheta-theta changes are1.905e-10/2.474e-10/6.554e-9/
3.972e-8. The detailed record and interpretation are in
`db6f-prefix-fixed-g-convergence.md` and`radial32-64-128-cauchy.json`.

The M16 run is now underway under
`flat-v17v18-fixed-m16-d12-p8-s64-outer`. It uses the same physical metric,
eight shooting pieces times64RK steps per raw profile (twice the M12
radial resolution),512angular quadrature, and a raw-preserving lift of the
successful M12 tail. Its first complete evaluation has minA=.19158072,
minD=.99150152, chart condition39849.96 and residual171.9003; this is not
yet a solved M16 tail. The M12 prefix coupling continues independently
with the original actual-DN-at-every-query algorithm. A contemplated
reschedule was not delivered to the running M12 process; its original
computation continues unchanged, as explicitly recorded in its reschedule
note. No numerical branch failure is inferred from that scheduling attempt.

## Completed M12 and the continuous frequency continuation

The M12/depth12/parts4/steps64 coupling has now genuinely completed,
not merely returned a padded-cut warm response. Its final prefix is
`flat-v17v18-fixed-m12-d12-p4-s64.json.gz`, final actual tail `_tail_0018`.
There are2570prefix nodes, RMS residual1.99713e-9, physical BC residual
1.01602e-18, and output support amplitude.09999976505231697. The prefix
metric diagnostic is8.95134e-9; the actual source-developed tail metric
is1.96497e-8 with shooting residual1.54224e-9 and minA.19156506. Relative
to completed M8/128, these metric diagnostics decrease12.49fold and
16.42fold. The final mean second seam difference is-2.1094e-13; the
nonmean second difference is1.4258e-10. The complete actual Cartesian
tail export now has metric diagnostic1.96722e-8, a16.39fold decrease from
M8 native128; its continuous certificate remains separate work.

One stale `summary.scope` sentence in that old running process still
says "Linear finite port only". It is a descriptive metadata error:
`config.actual_nonlinear_tail`, `tail_seam`, and the final actual response
record all describe the true coupled solve. The saved data/hash have
not been altered; the current runner already corrects this sentence.

The same-g M8/128→M12 prefix comparison on3654radial nodes and1024angles
has sampled C0 difference1.7292e-7 and largest second-jet difference
2.0798e-4. The detailed six-jet table is in`prefix-fixed-g-convergence.md`.
It does not yet establish infinite C2 convergence.

The original M16 warm solve slowed from residual14.75935 to14.52212,
while minA remained positive. A parallel M14 path now uses N256 angular
quadrature, parts8×steps32, raw-preserving lift, shared engines, and the
outer actual-DN algorithm. It starts from the completed same-g M8/128
prefix and uses completed M12 tail call16 only as a warm guess. Its
first residuals179.14→1.4663→.17008→.001087→5.70e-8→9.25e-10 reached
an actual converged warm tail, with sourceMetric8.56417e-9 and minA.116947.
The complete M14 prefix solve is still active. The old direct M16 run
was stopped at residual14.434856 on root's instruction after this better
warm path succeeded; all inputs and trace are retained, with an explicit
`fixed-m16-d12-p8-s64-outer-interrupted.json` record. No nonexistent-branch
claim follows. The final M16 target uses
N512 and requires a true nonlinear solve there. Separate same-state
RHS/Jacobian comparisons found N256↔512 differences around roundoff
and roughly half component cost; these are diagnostics only.

The macro native64→128 explicit-tail comparison is now also available.
It uses exact common radial partitions and exact zero-extension of
signed Fourier modes. C0 is bounded by7.58e-10, first-r by5.98e-8,
but second-r by.0324932 at r≈.52094; a local floating evaluation gives
.0118198 there. This second-jet representation refinement remains visible,
even though actual Cartesian metric samples are both≈3.22e-7. See
`prefix-tail-flat17-native64-128-c2.json` and its scope note; collars and
closed-map placement constants are not silently included.

## M14 whole coupling completed; prefix diagnostic is nonmonotone

The completed M14 checkpoint is
`flat-v17v18-fixed-m14-d12-p8-s32-q256-outer.json.gz`, with final true
tail `_tail_0004`. It has2633nodes, RMS residual1.99790e-9, actual
outer original BC2.08564e-14, final physical BC4.17128e-17, and four
true DN calls. Its tail sourceMetric8.56382e-9 improves on M12,
with sourceFullD4.90828e-5, shoot3.85560e-10 and minA.1169561.
However the prefix metric rises to7.94615e-8, with projected inlet
second-jet error3.00035e-6 and highest central support coefficient
1.18921e-8. We retain this as a nonmonotone result and are localizing
source-projection versus saved-interpolant error; no full-map frequency
convergence claim follows from the tail improvement alone.

The next genuine M16/N256 solve is running under
`flat-v17v18-fixed-m16-d12-p8-s64-q256-outer-from14`, from completed
M14. Its initializer preserves the saved adaptive mesh and raw Fourier
profile before the explicit inlet correction. Same-M and M14→M16
checks give zero mode-padding error outside that correction, zero inlet
coefficient residual, and saved-node displacement≤4.44e-16; changed
physical input is rejected. This optimization does not change any BVP
equation or acceptance tolerance. A final N512 true DN/coupled correction
remains mandatory. The stopped older M16 path stays available separately.

The sibling's conditional integrated-Fr C2 representation lemma has
also passed our independent mathematical review, recorded in
`prefix-review-integrated-fr-convergence.md`. This pays only finite
representation convergence for a given C2 source and controlled data
errors; it does not establish the nonlinear source, Fourier limit or
infinite-tail existence.
