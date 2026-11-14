# Same-density shooting partition backup: P8/S32 to P16/S16

2026-11-10, Astra-visible-flex-78718bd0. **Source-derived implementation plan;
not executed.** Fast06 currently keeps P8/S32 and uses the centered R95 trial.
The mathematical zero-set and nonzero-defect statements are in
[R98](../results/R98-rk-shooting-refinement-and-defect-propagation.md).

## 1. Actual stage builder and the unchanged integration density

`950f-tail-subdivision.mjs::subdividePhysical` partitions each unchanged raw
profile into P equal intervals. On part k, the profile is

$$
g_P(x)=g((k+x)/P),\qquad
(r_x,(\log w)_x)_P=P^{-1}(r_u,(\log w)_u).
$$

It maps the actual profile's critical points by the same affine coordinate
change. `f6tail_cusp_grid.mjs` then splits a uniform RK step only at those
critical points. Consequently P8/S32 and P16/S16 use the same 256 nominal RK
steps per raw profile, as does P32/S8. A critical point lying at the newly
inserted shooting boundary was already an original RK boundary; a critical
point inside a smaller stage remains the same physical split point.

In exact arithmetic these are the same RK updates, merely grouped into
shorter maps. The source does not justify a blanket binary64 bitwise-identity
claim: affine-coordinate evaluation, critical-point reconstruction and
projective normalization can change the order of floating operations. A
finite grid/one-stage comparison can record that actual effect if this branch
is chosen; it is not a new independent-review gate.

The far graph is computed beyond the same physical depth with unchanged
physical profiles and calibration. Within the finite region,
`buildStableStageGraphs` uses `max(8, ceil(linearSteps/P))` steps per stage.
With the actual current `linearSteps=256`, P8, P16 and P32 all retain 256 nominal
linear RK steps per raw profile. The intermediate projective charts differ;
the underlying real-arithmetic composed linear map is unchanged.

## 2. An actual midpoint warm, with all old nodes retained

For each old stage i, begin at its saved inner state `old.states[i+1]` in the
existing cell-engine momentum normalization. Execute its first 16 original
RK steps, including the actual critical-point splits. Store that actual
half-stage state as the new midpoint; copy the two old endpoint states
without reprojecting them. Thus for P16,

$$
new[2i]=old[i],\qquad new[2i+2]=old[i+1],
$$

and `new[2i+1]` is the actual half-flow from the old inner endpoint. The inner
half-stage port ratio is 1; the outer half retains the old stage's port ratio.
No new midpoint is labelled converged. Old endpoint residuals remain genuine
defects, as R98 explains.

The existing `950f-tail-warm-remesh.mjs::remeshCheckpoint` already implements
this basic construction for an integral partition refinement. For a P16
midpoint its `ceil(old.steps*oldParts*h)` is exactly 16. It must receive the
actual selected engine factory to reproduce the same state RHS; no physical
factory needs to be changed. A more efficient P32 implementation could march
once and retain three quarter points, instead of integrating each quarter
from the same old inner endpoint independently.

The current `geometricWarmRemesh` deliberately requires the same partition;
it must not silently be called for this case. Since the contemplated branch
keeps W22/N512, no spectral or angular re-embedding is needed. An explicit
same-M/N partition-refinement branch can call the existing actual-RK remesh
and record the added-node role as UNCONVERGED warm data.

## 3. Minimal numerical interface changes if needed

The generic driver would expose explicit tail shooting-parts and steps
options, record P*S=256, and change only those declared numerical fields.
The mode-continuation adapter would extend its present M/N numerical
comparison to the declared P/S change and corresponding stage-count change;
the known seed remains the same physical parameter/height source. The worker
would choose the explicit actual-RK midpoint warm described above.

The original projection floor, finite residual target, physical depth,
geometry, calibration, outer height target, full-W boundary jets and final
closed-map metric requirement remain. The final audit must explicitly state
its own step count; if its previous per-raw-profile sample density is to be
kept, its per-stage count changes with P as well. No prior geometric bounds
are transferred merely because the RK grouping has changed.

For the present 864-stage P8 grid, P16 has 1728 stages and 1729 nodes; P32 has
3456 stages and 3457 nodes. The total nonlinear RK step count stays the same
under S16/S8. Stored per-stage tangent matrices and the shooting algebra grow
with P, while the dominant number of root/RHS/Jacobian calls does not double
simply from repartitioning. These are work-count observations, not measured
runtime or memory guarantees.

The observed stage12 gains make shorter shooting maps a motivated backup:
the actual full shape Jacobian has max entry about `2.42e13`, while its
momentum-to-momentum maximum is about `1.97e6`. The exact reduction for a
specific shorter map must be evaluated, not replaced by a square-root guess.
No P16/P32 solver or midpoint construction was started for this note.
