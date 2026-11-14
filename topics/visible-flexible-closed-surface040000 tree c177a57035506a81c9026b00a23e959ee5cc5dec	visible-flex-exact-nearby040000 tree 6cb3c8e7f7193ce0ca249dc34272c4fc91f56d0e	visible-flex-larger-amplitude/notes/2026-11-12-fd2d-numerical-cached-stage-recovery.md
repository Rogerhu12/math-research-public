# Exact-input retention of actual stage work after external kills

2026-11-12, Astra-visible-flex-fd2d / numerical_recovery.

Current status: this old route is closed by its owner after preserving its actual states.
The maintained current-runtime note records the stop and strong-goal transition.
Status: the resume-05 launch recorded here is closed with actual Node -9.
Its computed maps are preserved in the independent runtime; by 04:22 UTC
resume-12 had accumulated and reduced all 1728 maps of the original base.
Resume-12–17 subsequently closed; the later route uses one stage worker
and retained complete trial construction.
See `2026-11-12-fd2d-numerical-current-runtime.md` for the active identity.
No new prefix, full DN
response, closed graph, or whole-surface metric bound is asserted.

## Concrete reason for this change

Resume-03 and 04 both ended with observed Node SIGKILL (-9), before a new
complete full-Jacobian evaluation. Run 04 had correctly effective independent
stage heap limits of 159,383,552 B each and last Node RSS about 541 MB; the
Python parent was about 102 MB. The visible resource interface does not
establish the sender or a particular OOM/CPU/time limit. Run 04 took about
300.64 seconds, 03 about 224.60 seconds, and 02 about 1365.59 seconds, so a
universal five-minute wall limit is not established either.

An accepted-state checkpoint only helps after the long current evaluation
returns. We now preserve **already completed independent stage maps** during
that evaluation. This directly prevents another external kill from losing
all actual work in the current pass. It is a recovery implementation, not a
new acceptance rule or a replay prerequisite.

## Exact finite map identity

For the actual finite shooting states y, stage n computes its own map from
y[n+1], its fixed profile, and the requested Jacobian flag. It has no input
dependency on another stage's output. The existing pool computes the same
stage engine/RK operations and later reduces outputs in ascending n order.

The cache context includes the exact serialized profile tables at the union
of the original state-only/full-J RK arguments, all engine options, RK step
count, architecture, V8 version, and the recursively discovered actual mjs
source dependency closure of the stage evaluator. The evaluation key also
includes the **complete binary64 input array bytes** and withJac flag.
Input hashes preserve signed zero and all bit patterns; no decimal rounding
or nearby-state matching is used.

Each saved block contains at most 32 stages' actual output vectors, complete
J matrices when requested, and actual mean/minimum scalars. It uses V8 binary
serialization and gzip. A block is saved only after all its status entries
are 1, published by the original workers after those outputs have been fully
written. Atomic status operations and the existing completion barrier retain
the original visibility/order rules. Files are atomically renamed, smaller
than 5 MB, and accompanied by scalar indices with SHA256 and context keys.

On a matching later evaluation, completed blocks are copied back into the
same shared output/scalar/J slots and marked complete. Workers skip those
already completed map calls and compute all missing stages. The original
ascending residual subtraction, normalization, maxima/minima, witness tie
rule, Riccati correction, line search, and nonlinear acceptance then operate
on these same actual outputs. No solve success is inferred from a cache hit.
Engine work counters count only newly executed work; they are not equations.
Cached higher stages do not suppress an earlier failure: the original
minimum failed-stage logic and ordered reduction remain authoritative.

A missing, truncated, corrupt, wrong-key, or wrong-dimension block is ignored
and recomputed. Cache I/O failure is observed and disables retention for
that evaluation without changing the mathematical algorithm. There is no
mandatory complete-cache gate. Each evaluation has its own small index so
one append-only index cannot reach the driver's file-size limit.

The cache is an intermediate computation under
`/workspace/scratch/fd2dbfd2c83e/visible-flex-stage-cache`.
Large blocks stay outside git. Source, precise invocation, scalar indices,
hashes and actual iteration/accepted/response checkpoints supply the durable
record. The cache is not a new geometrical candidate and not an infinite-tail
certificate.

## Actual run 05

Actual launch tool `73403c`, session **42979**, exclusively polled by the
numerical agent. Output stem:
`notes/2026-11-12-fd2d-numerical-m15-w22-resume-05`.
The 04 session is closed with real driver exit 2 and Node -9.

The warm state is still the complete 02 call2/iteration1 state at exact
207/256 original h, residual 0.027350999413424816, retained in the 03 warm
file (SHA256 `12d4aeb41efd1b04c51476f32de56650cbb2dde5b2af63a75b68015a986b3849`).
The scalar .007400219 later accepted by 02 does not have a saved state and
is not used as one. The new run must actually recompute that step.

The original full-height successful W15 packet is the known physical seed;
the unconverged warm supplies only its exact starting cutHeight/states.
M15/N512 prefix, W22/N512 tail, P16/S16/audit16, physical depth 12, original
2e-9 tolerance and .05 floor remain. The final prefix target/g/BC are unchanged.
The independently bounded host remains old heap 384 MiB, young 16 MiB;
two stage workers remain old heap 128 MiB, young 16 MiB.

From the repository root:

```bash
VISIBLE_FLEX_STAGE_CACHE_ROOT=/workspace/scratch/fd2dbfd2c83e/visible-flex-stage-cache \
python topics/visible-flexible-closed-surface/scripts/fd2d-run-prefix-cached.py \
  --modes 15 --angular 512 --tail-modes 22 --tail-angular 512 \
  --jacobian fourier --transforms fourier --tail-jacobian fourier-root \
  --tail-predictor tangent --tail-trial geometric-centered --tail-root-precision original \
  --tail-stage-workers 2 --direct-relative-limit 0.01 \
  --tail-shooting-parts 16 --tail-steps 16 --tail-audit-steps 16 \
  --bootstrap-from-initial-checkpoint --max-nodes 8000 --data-gib 6 --node-heap 384 \
  --restart topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-matched-cut-s63of64-warm-01.json.gz \
  --tail-seed topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-m15-linear-01_tail_0001.json.gz \
  --tail-initial-checkpoint topics/visible-flexible-closed-surface/notes/2026-11-12-fd2d-numerical-m15-w22-resume-03-tail-warm-input.json.gz \
  --out-prefix topics/visible-flexible-closed-surface/notes/2026-11-12-fd2d-numerical-m15-w22-resume-05 \
  > topics/visible-flexible-closed-surface/notes/2026-11-12-fd2d-numerical-runlog-05.log 2>&1
```

New sources are `fd2d-run-prefix-cached.py`, `fd2d-cached-tail-continuation.py`,
`fd2d-cached-tail-client.py`, `fd2d-cached-tail-stage-worker.mjs`,
`fd2d-cached-tail-stage-pool.mjs`, and `fd2d-stage-map-cache.mjs`.
The accepted-state core and bounded launcher from 04 are reused unchanged.
The 04 actual source versions are preserved. All six new sources passed
syntax checks before launch; no old mathematical solve was repeated as a
validation gate. The real solve remains the numerical task itself.

The runtime sidecar now also records actual Node CPU ticks, inherited child
limits, and the Python parent's RSS, alongside the existing real exit code
and Node/global memory observations. The solver trace records its actual
host heap limit as well as the stage heap limits and completed cache blocks.

## Actual progress

Startup and completed stage/iteration observations will be recorded here as
they arrive. A partial cache is useful recovered work, not a complete F/J
evaluation and not a DN response.
