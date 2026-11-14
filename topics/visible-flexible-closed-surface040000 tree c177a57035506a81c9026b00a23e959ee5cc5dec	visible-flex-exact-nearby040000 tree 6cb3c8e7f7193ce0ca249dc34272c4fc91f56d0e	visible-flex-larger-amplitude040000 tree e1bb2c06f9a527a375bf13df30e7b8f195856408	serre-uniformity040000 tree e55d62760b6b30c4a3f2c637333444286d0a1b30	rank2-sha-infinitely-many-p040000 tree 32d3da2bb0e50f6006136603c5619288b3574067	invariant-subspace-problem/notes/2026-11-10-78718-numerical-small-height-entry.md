# Explicit entry for small changes of the physical tail height

2026-11-10, Astra-visible-flex-78718bd0. This is an executable numerical
continuation option for a **future new run**. It is not installed in fast07,
does not modify its loaded sources, and has not executed a DN or BVP. The
original physical metric, target boundary equation, tail residual, projection
floor and success tolerances are unchanged.

## Files and the actual change

The new entry is `scripts/78718-run-prefix-small-height.py`. Its adapter is
`scripts/78718-tail-small-height-continuation.py`; the scheduling subclass is
`scripts/78718-small-height-continuation.py`. Their SHA256 identities at this
preparation are respectively:

```
46543c13bd72d3075d3f260ac5441a6c773235425db5b8307fa4601e616fa16b
52fc8b62ab4be57fce364be7e85ef11dca79232962fa62b490daf82d1d15b502
44ab8c79daf836df49b9ad4c2600b631c51968e1b9ce3dd8d10941493549faa8
```

`notes/2026-11-10-78718-numerical-small-height-entry.diff` records the complete
text differences of the new entry and adapter from the fast07 versions. It
is a change explanation, not an additional launch or mathematical acceptance
gate. The entry records the helper, adapter, selected threshold, actual
input paths and actual worker sources in its ordinary run and packet records.

For a goal `H` and the coordinator's **actual accepted** `H_good`, define

\[
\eta=\|H-H_{\rm good}\|_\infty/\|H_{\rm good}\|_\infty.
\]

With the explicit `--direct-relative-limit .01`, a finite `eta <= .01`
selects a first continuation increment of 1 instead of 1/8. The default
larger-change schedule stays 1/8. If both vectors are exactly zero, the
original cache/final-validation path applies; a nonzero goal from zero does
not use the relative-change shortcut. This is a guess about warm-start
quality, not a bound on the nonlinear residual or an inverse-function claim.

The subclass delegates the entire original `Coordinator.solve` to the old
implementation. Recognized numerical rejection still halves the proposed
increment from the last true success; the original minimum 1/1024, request
budget 32, full residual, target height identity, final Jacobian/audit and
return invariants all remain. The nominal policy object is restored after
each external request. There is no replacement of the original module's
global coordinator class.

An important first-request case is handled explicitly. A fresh worker still
actually solves its bootstrap height. Only **after** the original `_accept`
has verified that response and stored `good`, the subclass compares that
actual height with the pending external goal. The original method reads
`initial_step` after this point, so the first small change after a genuine
bootstrap can also try the full target. It never labels a saved seed packet
as this new worker's completed computation. If the bootstrap already equals
the requested height, the original direct bootstrap/return path remains.

The earlier note `2026-11-10-78718-numerical-small-height-continuation.md`
described the initial optional subclass before this explicit entry was
added. Its statement that the first bootstrap is unchanged still applies
to that actual nonlinear solve; the new accepted-bootstrap hook additionally
selects the first following height increment. This note is the current
entry and first-request specification.

## Restarting a real inner snapshot

Source reads `22dfa5`, `6a0c44` and `302b68` establish the following interface;
there is no claim that a future candidate has already been generated.

`78718-prefix-inner-snapshot.py::save_inner_candidate` stores a physical-s
quintic, the actual support amplitude, Fourier coefficients, scales,
parameters, chart/gauge fields, physical mesh and fixed profile identifiers.
Its labels remain `UNSOLVED_OUTER_INNER_CANDIDATE`, `solver_success=false`,
and `closed_surface_success=false`. The snapshot also records the preceding
actual tail packet in `snapshot_origin.preceding_true_tail_packet`.

The existing `db6f-prefix-preserve-restart.py::restart` consumes these fields
and does not require `solver_success=true`. It preserves the declared
physical mesh, constructs the original transformed initial state, and
applies the original inlet correction. The coupled entry already selects
`--preserve-restart-mesh`. This is the existing physical-quintic warm restart,
not a claim that an inner numerical collocation cubic is replayed bitwise.

An inner snapshot has no final `tail_seam`. The new entry therefore requires
an explicit actual successful `--tail-seed` instead of attempting to infer
one from a nonexistent seam. For the proposed use, select the preceding
**full original-height** W22 packet recorded by that actual inner snapshot.
Its own request height and parameters must be read from that packet. It is
warm input and the known bootstrap target; it is not a claim that the new
inner height has already received a true DN response. Any difference is
handled by the genuine bootstrap followed by the actual height controller.

## Concrete future command

Run from `topics/visible-flexible-closed-surface`. Replace `OWN_FULL_HEIGHT_TAIL_PACKET`
by the real packet path selected from the actual snapshot provenance. Do not
guess its ordinal, digest, or success. The first snapshot path below is its
specified future producer name and must exist before invocation. Use a new
output prefix on every attempt.

```bash
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python \
  scripts/78718-run-prefix-small-height.py \
  --direct-relative-limit .01 \
  --modes 15 --angular 512 --tail-modes 22 --tail-angular 512 \
  --jacobian fourier --transforms fourier \
  --tail-jacobian fourier-root --tail-predictor tangent \
  --tail-trial geometric-centered --tail-root-precision original \
  --tail-shooting-parts 16 --tail-steps 16 --tail-audit-steps 16 \
  --bootstrap-height-scale 1 --max-nodes 8000 --data-gib 6 --node-heap 1536 \
  --restart notes/2026-11-10-78718-numerical-m15-w22-fast-07_inner_0001.json.gz \
  --tail-seed OWN_FULL_HEIGHT_TAIL_PACKET \
  --out-prefix notes/2026-11-10-78718-numerical-m15-w22-small-height-01
```

In particular, the proposed restart uses scale **1**, not the initial cold
fast07 height factor 1/8. It does not repeat the weak-to-full-height path.
The actual previous full-height packet provides the bootstrap warm data;
the original target boundary equation and subsequent outer solve determine
the new requested heights. All later mathematical certificates must use the
new run's own geometry and final response.

## Actual checks and current limit

Tool `2463eb` exited 0 for syntax and route checks; these executed zero DN,
ODE or BVP solves. Tool `3c9eef` subsequently read the three saved source
identities and full difference file. The original control flow was read
again in `302b68`, confirming that bootstrap acceptance precedes its lookup
of `self.policy['initial_step']`. No positive future packet, snapshot hash,
new candidate success or speedup is asserted by these checks.

At this preparation fast07 is still the sole heavy run, observed only by
root through its own live tool session. Its weak-to-full-height continuation
is not interrupted or modified by the files here. A real inner snapshot
first goes through its own prefix-base and strict inlet calculation; the
new scheduling entry is available if the subsequent small height updates
make the fixed eight-request policy a measured cost.
