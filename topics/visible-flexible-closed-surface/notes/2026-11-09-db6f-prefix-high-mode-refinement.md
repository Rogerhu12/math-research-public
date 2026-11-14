# Fixed material metric: high-mode and radial refinement

This note concerns the completed macro M8 prefix/tail coupling
`2026-11-09-db6f-prefix-flat-v17v18-coupled-m8-q10-fine.json.gz`.
It is a continuation record, not a completed closed-surface certificate.

## What is held fixed

The physical prefix profile, including its final delta, the adaptive angular
chart, its reference warp amplitude, and every physical weighted-tail
parameter are copied from the completed checkpoint. Increasing the Fourier
order, the quadrature, the number of shooting pieces, the RK steps per piece,
or the finite approximation depth changes only the approximation. In fixed
mode the actual central support amplitude is an output of the coupled BVP.

`scripts/db6f-prefix-freeze-refine.py` writes the frozen profile, target tail
configuration, full command, source checkpoint hash, and result summary.
`scripts/db6f-prefix-convergence-packet.py` checks equality of the frozen
material inputs before comparing position and the five first/second physical
coordinate derivatives of the saved prefixes. Its suprema are sampled
diagnostics and do not replace an interval C2 Cauchy estimate.

The M8 baseline used two numerical shooting pieces per raw profile and32RK
steps per piece. A same-M8, same-depth,64-step coupled solve is running as a
radial check. The M12/depth12 refinement uses four pieces and64steps per
piece. These computations re-solve the full nonlinear shooting equations.
Integrating an old32-step checkpoint with64steps while forcing its old end
traces is not such a check: the RK endpoint difference can create a second
derivative floor in the Cartesian Hermite representation.

## Preserve raw geometry in a spectral warm start

The momentum coordinates are nonlinear functions of the raw Fourier height
and slope data. In particular, adding zeros to the new momentum modes does
not preserve the old raw state. The earlier generic warm remesher used that
simple coordinate padding; it is only an initial guess, so this is not an
error in the equations eventually solved.

`scripts/db6f-prefix-tail-raw-lift.mjs` provides a better initial guess:

1. Remesh the old state onto the new shooting partition with the existing
   initial-guess routine.
2. At each node, use the old engine to recover the raw height and slope data.
3. Zero-pad those raw data to the new Fourier order.
4. Use the new engine's unchanged full mean root and nonlinear momentum map
   to calculate all new momentum coefficients.
5. Apply the documented cross-cell momentum normalization at the outer cut.

The output explicitly says **UNSOLVED warm guess**. It is never accepted in
place of a full shooting response. When lifting the completed macro M8
checkpoint to M12/depth12/four pieces, the432-node conversion preserved the
low height coefficients exactly and the raw slope coefficients to
3.19e-16. Its minimum leading coefficient remained .19508944. The new
momentum coefficients reached .0303 in the normalized coordinate, showing
why zero momentum padding can be a poor warm start even when the old
physical geometry is regular. The first saved warm file predates the added
mean-slope-difference diagnostic; that omission does not change its state.

The ordinary padded M12/four-piece run has nevertheless passed its first
Newton correction: its normalized residual fell from1758.7 to4.61 and its
minimum leading coefficient increased from.1276 to.1904. Convergence of
this run remains pending at the time of this entry.

## Share immutable engine data between numerical pieces

Each numerical shooting piece in one raw physical cell has identical engine
options, including the same momentum normalization. The engine methods take
the state and the physical profile as arguments; their Fourier tables can
be shared. The optional files

- `db6f-prefix-tail-shared-core.mjs`
- `db6f-prefix-tail-shared-split.mjs`
- `db6f-prefix-tail-shared-worker.mjs`
- `db6f-prefix-tail-shared-client.py`

only reuse the engine object across such pieces. They leave the root,
nonlinear field, Jacobian, RK grid, shooting residual, line search, and
response protocol unchanged. Aggregate diagnostic counters are shared too;
they do not enter the numerical equations. The original950f files remain
unchanged.

`db6f-prefix-tail-sharing-check.mjs` compared every actual cut-jet output
and three representative full variational stage flows against the original
implementation at the completed M8 checkpoint. The states, tangents, minA,
minD, and all cut jets were bitwise equal. The number of engine objects fell
from180 to10. The detailed bounded check is in
`2026-11-09-db6f-prefix-tail-sharing-check.json`. This checks arithmetic
equivalence of the exercised paths, not existence or global convergence.

The runner accepts optional`--shared-tail-engines` and`--raw-lift-warm`.
Both are disabled by default so earlier commands retain their behavior.

## Optional outer true-DN correction

The original coupling queried the full nonlinear DN map at every inner
prefix Newton trial. A high-mode tail query can take minutes, although the
cut height changes little between those trials. The new optional
`--lagged-tail` flag uses the actual DN value and its actual variational
Jacobian to form an affine slope boundary operator for an inner prefix BVP.
After each converged inner solve it calls the full nonlinear DN map again
at the new height and evaluates the **original** boundary residual. It
accepts a coupled solution only if that original residual meets the
original boundary tolerance. Otherwise it updates the affine operator and
repeats. No approximate response can provide a seam audit, and the final
seam audit is always performed through the actual nonlinear client.

This is an optional equation-solving algorithm; it does not change the
physical model or the residual required for success. The output records
the solver choice and every outer actual-boundary residual. The flag is
disabled by default. Its first use will be the same-M8 radial refinement,
with the ordinary nonlinear-every-query M8 solution as an independent
reference for the resulting geometry and boundary data.
