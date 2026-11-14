# Executable R240 same-metric refinement interface

This interface is prepared for a genuinely accepted complete full-DN
design.  It has **not** been run on the unaccepted M112 initial guess.
All new entry points reject such a prepared/failed parent; no hypothetical
acceptance data have been created.

## The frozen object and the correct count

The complete v3 scalar specification is retained verbatim: the old
accepted source-prefix geometry and identity, complete connector/coast/
bridge/tail port, three actual support intervals and polynomial, all
three solved `p*` values, and defining source hashes.  The v4 schema
`frozen-complete-scalar-same-metric-refinement-v4` keeps this object as
`frozen_design_scalar_profile`.  Its canonical JSON SHA-256 is unchanged
across subsequent refinements.  Changing live field/tail dimensions does
not change this scalar object.

In the common material angle the same function defines
`g=ds^2+a(s;p*)^2 dtheta^2`.  Refinement has `K=0` fixed core coefficients
and `k=0` active scalar parameters.  Every core coefficient is an embedding
unknown.  With `M=T`, the exact finite count is:

| Field/tail M | Physical rows | Constant core rows | Active scalar rows | Left rows | Right rows | Total |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 112 | 338 | 112 | 0 | 338 | 112 | 450 |
| 128 | 386 | 128 | 0 | 386 | 128 | 514 |

The physical left boundary has `2M+2` rows; identifying the constant core
with the inlet adds M rows.  The right side retains all M native DN rows.
Keeping the old three fixed-core rows while removing their three scalar
controls would overdetermine this system and is not done.

The output field remains the full finite rotating-phi field, including
the entire `z0`.  Its active `scalar_parameters` is an empty list, while
the three **frozen design** parameters remain explicitly stored in the
v4 scalar object.  No empty active list is used to reconstruct the design.

## Source-bound preparation

[`geometry_20261114_same_metric_profile.py`](../computations/geometry_20261114_same_metric_profile.py)
serializes and reconstructs the fixed scalar.  Repeated v4 inputs are
flattened back to the same first v3 design object, preserving its identity.

[`geometry_20261114_same_metric_prepare.py`](../computations/geometry_20261114_same_metric_prepare.py)
requires a genuine accepted complete parent, its producer-bound
`actual-tail-final-audit.json.gz`, and the exact native input config bound
by `parent.actual_tail.sources.input_config`.  It checks the original
parent RMS/BC/frozen-physical gates, full native H/J/three jets/four mean
jets/eight finite audit values, and the original native solve tolerance.

The bare native final response has no `request.audit` field.  The check
does not invent one: its exact bytes are bound by the accepted original
producer's `actual_tail.final_response_sha256`, whose final path actually
requested the full audit.  A new M is never assigned an old response.

The complete parent's physical C2 quintic uses its saved states, its saved
RHS, and the same original finite-ODE second-jet rule as the full-field
readout.  All coefficients and all original nodes are preserved in the
new initial guess; additional field/core coefficients are initially zero.
Optional time subdivision samples this whole C2 curve.  The new original
finite RHS then undergoes the complete node/midpoint/two-RMS-fraction
domain preflight.

For example, after a real M112 acceptance, with the variables below bound
to those actual files:

```sh
python "$C/geometry_20261114_same_metric_prepare.py" \
  --parent-field "$PARENT" \
  --parent-tail-response "$PARENT_TAIL" \
  --parent-tail-config "$PARENT_CONFIG" \
  --field-modes 128 --angles 4096 --subdivisions 1 \
  --max-nodes 1200 --out "$OUT/preparation"
```

`--subdivisions` changes the initial time mesh, while `--max-nodes` is an
explicit computational budget.  Neither changes an acceptance tolerance.
If a requested subdivision already exceeds that budget, preparation
reports it instead of deleting parent nodes.  Field or angle resolution
is never reduced by this entry point.

## Complete response and actual refinement solve

[`geometry_20261114_same_metric_response.py`](../computations/geometry_20261114_same_metric_response.py)
uses the original complete boundary-response CLI, with `--accepted`
pointing to the actual **complete parent** here.  It changes only the
explicit frozen scalar/dimensions and sets `target_core=[]`.  It retains
the original FD levels, Richardson contraction check, complete physical
and augmented boundary, and original `5e-5` implementation threshold.
Its worker `ready.linearD` remains a labeled linear-graph reference.

```sh
python "$C/geometry_20261114_same_metric_response.py" \
  --accepted "$PARENT" --prepared "$OUT/preparation/prepared.json.gz" \
  --port "$PORT" --tail-client "$C/exact_20261114_true_tail_client.py" \
  --tail-config "$NEW_TAIL_CONFIG" --tail-source-root "$SOURCE_ROOT" \
  --material-angles 8192 --out "$OUT/boundary"
```

The new native config must retain M128 and the same physical tail metric;
its quadrature is separately explicit and is not coarsened from the
parent.  A fresh true response/J is required for the complete new H.

[`geometry_20261114_same_metric_full_dn.py`](../computations/geometry_20261114_same_metric_full_dn.py)
then calls the unchanged original actual-tail outer loop, complete
Jacobian/audit path, separated QR, Newton/line search, and `1e-6` RMS /
`1e-11` BC gates.  In this final entry, `--accepted` is deliberately the
real **original M96 design-source prefix** because that is the source
identity checked by the unchanged underlying driver.  The genuinely
accepted complete parent is passed and independently verified as
`--parent-field`; it is never relabelled as M96.

```sh
python "$C/geometry_20261114_same_metric_full_dn.py" \
  --accepted "$DESIGN_SOURCE96" --port "$PORT" \
  --parent-field "$PARENT" --parent-tail-response "$PARENT_TAIL" \
  --parent-tail-config "$PARENT_CONFIG" \
  --warm "$OUT/preparation/prepared.json.gz" \
  --response-check "$OUT/boundary/response-check.json" \
  --tail-client "$C/exact_20261114_true_tail_client.py" \
  --tail-config "$NEW_TAIL_CONFIG" --tail-source-root "$SOURCE_ROOT" \
  --material-angles 8192 --max-nodes 1200 \
  --out "$OUT/solve" --work "$WORK"
```

The real new tail response is used for Newton, followed by an independent
actual final audit.  Reduced matrices/SVD and original linear-residual
logs are retained.  Optional diagnostics cannot swallow or override an
original mathematical factorization failure.

## What success would and would not establish

A success would be a complete accepted **finite** calculation at another
resolution of the same canonical scalar metric.  The fixed scalar SHA
and all active/frozen parameter counts remain explicit.  The newly free
core can move, so the amplitude witness, density certificate, physical
metric readout, closure, whole-family diameter and reach must be read
again from the new actual field.  The parent gap or held Hausdorff lower
bound is not inherited merely from solver success.

The required same-g refinement comparison concerns the isometry error at
the README's stated numerical scale.  Six-jet comparisons remain useful
for the C2 field definition, curvature and reach reliability; this
interface does not add a requirement that every six-jet difference reach
machine precision.

Only static AST checks have been performed on these new entries at the
time this note was written.  They are ready to consume a real accepted
parent when one exists; no numerical refinement result is asserted here.

## Physical full-state reader

`geometry_20261114_same_metric_saved_prefix.py` exposes `SameMetricSavedPrefix` and the same complete material nine-jet API for genuinely accepted v4 outputs. It reconstructs the original three frozen design controls while requiring zero active scalar rows and all released core rows; it does not reinterpret an empty active parameter list as a new scalar design. Its finite physical quintic, global density certificate and source acceptance gates retain the original definitions. This separately named reader also supports the independent inlet-parity consumer without modifying the v3 reader.
