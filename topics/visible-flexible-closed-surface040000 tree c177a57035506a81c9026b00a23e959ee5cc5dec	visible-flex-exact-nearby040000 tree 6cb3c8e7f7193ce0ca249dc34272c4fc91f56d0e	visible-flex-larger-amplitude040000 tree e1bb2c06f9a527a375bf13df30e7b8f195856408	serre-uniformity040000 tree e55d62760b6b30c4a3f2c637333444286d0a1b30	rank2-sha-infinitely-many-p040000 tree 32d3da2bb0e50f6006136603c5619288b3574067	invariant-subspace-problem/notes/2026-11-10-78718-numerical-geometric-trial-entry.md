# R95 geometric Newton trial entry and independent warm input

2026-11-10, Astra-visible-flex-78718bd0. **Executable numerical branch; no new
DN/BVP success is asserted here.** The physical metric, requested final cut
height, original residual, Newton correction, branch floor `.05`, ten trial
steps, residual decrease rule and `2e-9` success tolerance are unchanged.
The prior fast04 calculation uses its already loaded previous code and its
original momentum trial. The new core, split and worker have distinct names.

## 1. What changes

`78718-tail-geometric-trial-core.mjs` is the existing tangent core with an
optional `opts.retractTrial(states, delta, lambda)` at the original trial
construction point. The original correction is computed once. The exact same
trial residual is then evaluated and the exact same `test.norm < ev.norm`
condition decides acceptance. Absent a hook, the old affine momentum update
is used. Trial construction is inside the same error-handling block as the
subsequent residual evaluation.

`78718-prefix-tail-geometric-trial-worker.mjs` supplies the R95 hook from
`78718-tail-geometric-newton-retraction-v2.mjs`. The latter imports the v1
differential calculation and uses the base mean root plus its directional
derivative to initialize the **same** mean equation. It does not initialize
that mean from an unrelated zero. The original 30 mean iterations, 20
backtracking attempts, `8e-14` relative stopping condition and positive branch
floor are retained. Geometry's small fixed-node experiment and complete
mathematics are separate from any full shooting success.

The following three facts remain distinct:

- A retraction construction can fail before the original shooting residual
  has been evaluated.
- A successfully constructed trial can fail during an original flow/root
  evaluation.
- A successfully evaluated trial can have a nondecreasing shooting norm.

The first case is recorded as `geometric-trial-construction-rejection`, with
the literal wrapped error, original cause and node. It is never recorded as
an ODE stage failure. The original stage diagnostics remain unchanged for
the second case. `78718-tail-geometric-trial-control.py` recognizes completed
trial groups only for the listed numerical root/mean/Gram failures and allows
the existing H continuation controller to subdivide its increment. Unknown
errors remain errors. This classification never accepts a DN solution or
establishes nonexistence of a mathematical solution.

## 2. Zero extra ODE residual location

The new core observes the residual entries already produced by `evaluate`.
It records one maximum location with
`stage, component, absolute, scale, normalized, rawCell, rawSegment` and a
`kind` distinguishing shooting, far Robin and cut Dirichlet terms. The old
norm calculation is preserved. The new observation is emitted in iteration
progress and the recovery checkpoint's iteration metadata, without modifying
the existing `response.history` schema. No new root or flow is run to obtain
this location. In the shooting block components `0..W-1` are Q and `W..2W-1`
are momentum components, so future large normalized residuals can be
attributed to their actual coordinate and physical segment.

## 3. A failed warm is not a successful seed

The generic command now accepts `--tail-initial-checkpoint`. It changes only
the worker's initial shooting state. The known successful packet specified by
`--tail-seed` remains the coordinator seed and determines the original height.
The separate `known_seed_packet` policy field makes this distinction explicit.
The bootstrap multiplier is separately declared on the command line, and the
subsequent actual continuation must return the original requested H, with its
requested Jacobian/audit.

The input may be an actual failure or iteration packet. Its status, scope,
available convergence/failure flag, dimensions, byte count and hash are
recorded. It is never marked converged by the loader. The loader reads the
input once and retains exactly those bytes (or losslessly gzip-compresses a
plain JSON input) in `<new-stem>-tail-warm-input.json.gz`. This matters for an
iteration source replaced atomically by another process: the subsequent
worker reads the observed snapshot, not an accidentally later iteration.
Every retained file is smaller than 5 MB. This retention is an initial-guess
operation, not a new review or registration prerequisite.

Alternatively, `--tail-cold-start` removes `initialCheckpoint` from the worker
configuration altogether. It is mutually exclusive with the override above.
The first request then uses the original `dn.tail.initial` rotational linear
shooting graph at the actual requested height. The old successful packet
supplies the same physical parameters and original H, but none of its saved
shooting state is loaded into the worker. This choice is explicitly recorded
in the run metadata and the continuation policy. The coordinator still starts
with no successful response for the new run; a known old packet does not
prepopulate its `good` state.

## 4. Concrete next command

The parent runs one heavy task at a time. The selected next attempt starts
from the original linear graph and actually solves H/8 before continuation
toward the unchanged original H. It does not carry over fast04's low-A
iteration. The separate warm input remains available for a later explicitly
chosen recovery attempt; it is not used in the command below.

```bash
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python \
  topics/visible-flexible-closed-surface/scripts/78718-run-prefix-mode.py \
  --modes 15 --angular 512 --tail-modes 22 --tail-angular 512 \
  --jacobian fourier --transforms fourier \
  --tail-jacobian fourier-root --tail-predictor tangent \
  --tail-trial geometric --tail-cold-start --bootstrap-height-scale 0.125 \
  --max-nodes 8000 --data-gib 6 --node-heap 1536 \
  --restart topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-matched-cut-s63of64-warm-01.json.gz \
  --tail-seed topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-m15-linear-01_tail_0001.json.gz \
  --out-prefix topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-m15-w22-fast-05
```

The generic entry's defaults still select momentum trials. Source selection
records both retraction versions because v2 actually imports v1, along with
the new core/split/worker, R92 predictor and selected Fourier implementation.
The new worker announces
`same-direction-Q-L-Newton-retraction-mean-seeded-v2`. All new actual inner
returns retain the existing explicit `UNSOLVED_OUTER_INNER_CANDIDATE`
snapshots for immediate prefix research.

## 5. Actual limited checks

The current editing session performed only syntax and entry selection checks:

- `a3abb8`, `15f9d9`, `713d01`: the three initially written JavaScript files
  passed `node --check` with natural exit 0.
- After choosing the mean-seeded v2 helper, `337bbc` passed the worker syntax
  check with natural exit 0.
- `45c333` compiled the four Python entry/control files and actually selected
  the `fourier-root / tangent / geometric` worker and all ten additional
  existing sources. Natural exit 0, no worker process, no solver calls.
- `09cc21` actually ran the generic CLI help with the two new options and
  exited 0.
- `27096e` parsed the added mutually exclusive cold-start option and the
  updated adapter after fixing an eager default expression that would have
  indexed the deliberately missing `initialCheckpoint`. Natural exit 0;
  no worker, DN or BVP was started.

These checks do not test full DN convergence. They are not new startup gates.
The next real run, if launched, supplies that numerical evidence.

## 6. Actual switch to fast05

The parent subsequently executed the exact cold H/8 command in §4. It first
observed fast04 still active (`5ac803`), then intentionally sent Ctrl-C and
received **`f4eb4d`, exit code 1**. This is a research scheduling stop, not a
natural mathematical failure; the observed exit code is not rewritten as
130. Fast04's half-H accepted iterations remain unconverged recovery data.

The parent then actually started fast05: **`b8c003`, session `42458`**. The
parent exclusively observes that process. The initial state is the original
rotational linear graph at H/8, the trial construction is the mean-seeded
R95 v2 branch, and the final requested height is the original H. No worker
warm checkpoint is supplied. At this observation there is no completed
response or new inner checkpoint. The source of the now active run is left
unchanged; later actual outcomes belong in subsequent observations.
