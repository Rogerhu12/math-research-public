# Warm fixed-metric lambda-one entry to the original finite nonlinear DN

Session: Astra-held10-06bbeb39-20261126.  This is an executable interface
record.  No lambda-one warm candidate or nonlinear-tail acceptance is asserted
by adding these files.

The entry is

```text
python scripts/resume_20261126/warm_true_dn_continue.py \
  --repo <repository> --work <owned-runner-work> \
  --source-run <actual-accepted-warm-lambda-one-run.json> \
  --outdir <new-owned-runner-work-directory>
```

`warm_true_dn_continue.py` validates its actual input before preparing or
calling the native tail.  Its worker is `warm_true_dn_solve.py`.  For v1 the
source must have a genuinely successful warm BVP return.  For the explicit
v2 phase contract it calls
`warm_fixed_m3_model_v2.accepted_input(require_lambda_one=True)` and preserves
the distinction between `actual_warm_bvp_return` and
`same_cartesian_map_verified_reexpression`; a reexpression never becomes a
new solver return.  Both lambda fields must equal one.  Original tolerances,
positive finite residual bounds, the complete source metric audit, and the
angular floor `16*(3*M+1)` remain mandatory.  The source raw, physical field,
port, origin and numerical implementations are bound by their actual hashes.

The actual evaluator is the source's warm model with `fixed=True` and
`p[0] = log(q_aux / gauge_q)`.  It retains actual delta, the complete anchor
support, material angular chart, gauge, mean1168, and BC normalization 0.02.
For v2 it also retains the literal frozen radial chart and corrected physical
phase scale rule.  The actual DN mixin is attached to this evaluator; the
original design runner's delta interpretation is never used.  Its final
read-only geometry loader reconstructs the same declared source model and
does not invoke the BVP or DN.

The base tail configuration must have the exact SHA recorded in the actual
source port.  Its explicitly supplied physical keys are checked, and the
real worker's ready packet is then checked against every physical parameter
in that source.  Defaults and derived worker parameters are not fabricated
in the base config.  The ready packet is saved in full.  Only declared
runtime tracing, three bounded chord corrections, and an optional accepted
same-source full checkpoint may be added.  The original native manifest,
all owned source and binary hashes, actual dimensions, physical cut,
quadrature, orientation, projection floor, and two-worker scope are checked.

The initial height is the actual unscaled vector
`bridge.sigma * gauge_q * Y_height_at_cut`.  Every initial/outer height has
an immutable `height-target-*.json` containing its complete `candidate_H`
and the source/raw/physical file hashes.  The initial warm order is
0.25, 0.5, 0.75, 0.9, then complete H.  Its arithmetic is explicitly
NumPy `H * factor**arange(1,M+1)`.  Every accepted response must come from the
original nonlinear worker with residual at most 2e-9, a complete saved
checkpoint binding the exact requested height, and a real audit.  Complete
H also requests all `(3*M+2)*M` entries of the original height-jet Jacobian.
An optional previous packet is only a new Newton initializer.

The original eight-outer continuation then alternates the temporary affine
inner DN with an actual full-H original nonlinear solve and checks both the
full scaled BC and physical BC.  It retains the original BVP/domain/RMS
gates.  Radial batching uses eight points and releases only the obsolete LU
factor before a refresh.  Last-Jacobian snapshots are explicitly unaccepted
Newton inputs.  The final saved physical field receives the complete
relative metric audit with the source's mean1168 convention.

The cut diagnostic uses the original mean/nonmean formulas and cut angular
audit, but independently computes both the physical mean and its derivative
with the frozen 1168 nodes.  It reuses the exact already accepted full-H
packet; it does not perform an unnecessary second solve at the same height.
These finite checks do not pay the Cartesian seam, convergence of a fixed-g
C2 family, the all-tail geometry estimates, or complete closure.  Those
flags remain false and are handled by their separate actual-field proofs.

Runner projections should request only the controller's `summary.json`
and the allowed top keys `status`, `progress`, `stages`, `result`, `error`,
`exception`, and `source_hashes`.  Each local summary is limited to 24 KiB.
The acceptance scalar is `result.original_nonlinear_DN_accepted`; full
packets and arrays remain under runner work.  No additional diagnostics
paths or publication limits are required.

For the optional initializer, checkpoint `depth` counts subdivided shooting
intervals; `physicalDepth` is the physical cell count from configuration
`depth`.  The entry checks all `depth+1` finite state rows of length `2*M`,
the complete strictly increasing `rawNode` physical-cell mesh, and literal
`rawStates == states[rawNode]`.  It does not replace a complete state with
the much shorter physical-cell subset.

Verification performed: both Python files compile; the entry rejects a real
recorded pre-lambda-one source before any BVP or DN call.  The frozen-mean
chain-rule formulas and the height-reference interface were independently
reviewed with the seam-geometry agent.  Actual lambda-one execution remains
conditional on the same-metric continuation producing an accepted input.

The separate read-only gate `warm_actual_dn_acceptance.py` now validates the complete final raw/physical/metric/mean artifacts, the real final outer boundary check, full-H target and packet, original full Jacobian, complete shooting state and physical-cell subset, frozen numerical sources and all finite gates. It calls no solver. The port physical contract has exactly the original exporter's declared 22 keys and contains no `depth`; subdivided `depth` and physical `physicalDepth` are checked separately against states and configuration, never silently renamed. No actual lambda-one input has yet been passed through this complete gate.

## Explicit v3 source family

The unexecuted nonlinear-DN entry now explicitly dispatches v3 to warm_fixed_m3_model_v3.accepted_input(require_lambda_one=True). Its complete warm_definition, true complementary-arc frequency definition, basis_anchor_v2 identity, frozen charts and every provider_bindings SHA are retained in the actual-DN record and checked again in the geometry loader and centralized actual acceptance gate. The original BVP/native DN equations, eight outer checks, full-H/J packet identity and all finite gates are unchanged. The source finite family is recorded explicitly; unknown versions remain rejected. The v3 provider/model/step being queued on the runner are not edited by this reader/solver-interface update. No actual lambda-one input or nonlinear-DN success is claimed.

The actual inner raw return and its SHA/status/RMS/complete candidate_H are now recorded before reconstructing the returned core. A later domain error therefore preserves the real solver return instead of leaving only an unindexed raw file. Successful numerical paths and all gates are unchanged; a failed solver return is rejected before any new geometry is accepted.
