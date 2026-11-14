# Actual bounded-memory continuation and accepted-state retention

2026-11-12, Astra-visible-flex-fd2d / numerical_recovery.

Current status: this old route is closed by its owner after preserving its actual states.
The maintained current-runtime note records the stop and strong-goal transition.
Status: resume-04 ended with external SIGKILL before a complete new iteration.
The later actual continuation is recorded in the current-runtime note;
see `2026-11-12-fd2d-numerical-current-runtime.md`. The resume-05 discussion
in the cached-stage note is historical and also closed.
This note does not assert
a new prefix solution, complete tail response, closed graph, or metric bound.

## Why this execution differs materially from resume-03

The prior 03 driver exited 2 after its Node process received SIGKILL (-9).
The last readable RSS was 1,029,840 kB. No complete new iteration or response
was produced. The sender of SIGKILL and any particular memory limit remain
unidentified; visible cgroup counters are absent.

The actual saved pool metadata showed four heap limits of 1,660,944,384 B,
although the resourceLimits object requested a 256 MiB old generation.
The global `NODE_OPTIONS=--max-old-space-size=1536` had overridden the worker
setting. In a small actual runtime probe with global old heap 384 MiB,
all three worker variants (inherited environment, cleared NODE_OPTIONS,
and NODE_OPTIONS replaced by 128 MiB) reported the same 427,819,008 B limit.
Every variant used execArgv=[] and nominal worker old heap 128 MiB.
The scalar probe is saved in `2026-11-12-fd2d-numerical-heap-override-probe.json`.
This is implementation evidence, not a mathematical benchmark.

The new launcher therefore starts with **no global V8 heap flag**. It creates
a host Worker with old heap 384 MiB, young heap 16 MiB, and stack 4 MiB;
the host runs the unchanged numerical protocol. Its two stage Workers each
have old heap 128 MiB, young heap 16 MiB, and stack 4 MiB. stdin/stdout/stderr
are piped without modifying the numerical JSON messages. The pool's actual
`v8.getHeapStatistics().heap_size_limit` values are recorded on startup;
the solver's ready message also reports its effective heap limit.
The requested and observed values are distinguished below as they arrive.

## Accepted-state recovery

The prior 02 solver accepted a step with scalar residual
0.0074002192307086635, but it died during the following full-Jacobian pass.
Its latest complete saved state still had residual 0.027350999413424816.
Only that latter state is recoverable, and the accepted step must be redone.

The new core inserts an observation callback immediately after the existing
`test.norm < ev.norm` acceptance. It saves the actual accepted states before
the following full Jacobian, with the actual target cutHeight, rawNode,
rawStates, parameters, and observed state-only trial residual. The record is
explicitly `accepted-trial-recovery-only`. It neither invents full-Jacobian
extrema nor marks the state as a successful DN response. The old full-Jacobian
iteration record continues separately. A storage exception is recorded and
does not alter the mathematical algorithm.

Accepted records use the derived filename
`*_tail-iteration-accepted.json.gz`; they are atomically replaced by each
later accepted full state. Each must remain below 5 MB. The observation
does not add an output-only key to the physical configuration identity.

## Actual run 04

Launch tool `ce19fa`, session **72611**; numerical_recovery exclusively owns
the process and its polling. Stem:
`notes/2026-11-12-fd2d-numerical-m15-w22-resume-04`.
The historical 02 and 03 sessions are closed and are not live backups.

The warm input is the complete saved 02 call2/iteration1 state, retained in
`2026-11-12-fd2d-numerical-m15-w22-resume-03-tail-warm-input.json.gz`,
754912 B, SHA256
`12d4aeb41efd1b04c51476f32de56650cbb2dde5b2af63a75b68015a986b3849`.
The bootstrap reads its exact complete cutHeight, nominally 207/256 original
height, maximum component 0.0006474599609535065. This is an unconverged
initial guess. The known full-height successful W15 packet remains the
physical-parameter source. The final requested prefix height is unchanged.

The same physical geometry, g, target, projectionFloor=.05, solveTolerance
2e-9, boundary tolerance, and numerical equations remain. The finite
discretization is M15/N512 prefix, W22/N512 tail, physical depth 12,
P16/S16/audit16, 1729 shooting nodes, 256 RK steps per raw profile.

```bash
python topics/visible-flexible-closed-surface/scripts/fd2d-run-prefix-bounded.py \
  --modes 15 --angular 512 --tail-modes 22 --tail-angular 512 \
  --jacobian fourier --transforms fourier --tail-jacobian fourier-root \
  --tail-predictor tangent --tail-trial geometric-centered --tail-root-precision original \
  --tail-stage-workers 2 --direct-relative-limit 0.01 \
  --tail-shooting-parts 16 --tail-steps 16 --tail-audit-steps 16 \
  --bootstrap-from-initial-checkpoint --max-nodes 8000 --data-gib 6 --node-heap 384 \
  --restart topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-matched-cut-s63of64-warm-01.json.gz \
  --tail-seed topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-m15-linear-01_tail_0001.json.gz \
  --tail-initial-checkpoint topics/visible-flexible-closed-surface/notes/2026-11-12-fd2d-numerical-m15-w22-resume-03-tail-warm-input.json.gz \
  --out-prefix topics/visible-flexible-closed-surface/notes/2026-11-12-fd2d-numerical-m15-w22-resume-04 \
  > topics/visible-flexible-closed-surface/notes/2026-11-12-fd2d-numerical-runlog-04.log 2>&1
```

## New source files

The actual resume-03 source versions are preserved. This run uses separately
named files:

- `fd2d-run-prefix-bounded.py`, `fd2d-bounded-tail-continuation.py`, and
  `fd2d-bounded-tail-client.py` select the new transport and save process RSS,
  actual return code, global available memory, and exception details.
- `fd2d-bounded-worker-launcher.mjs` implements the independent host limit.
- `fd2d-bounded-tail-stage-pool.mjs` uses the lower independent stage limits.
- `fd2d-bounded-tail-stage-worker.mjs`, `fd2d-bounded-tail-stage-split.mjs`, and
  `fd2d-bounded-tail-stage-core.mjs` retain accepted actual full states.

All eight new source files passed their respective Python or Node syntax
checks before execution. There is no repeated old BVP or new replay gate.
Only this real solve can establish a new finite response. Every actual inner
prefix returned by the existing driver is still saved for immediate own
Cartesian/metric analysis, with outer-UNSOLVED status preserved as applicable.

## Observed execution

At the initial heartbeat, the Node process was alive at RSS 85,720 kB and
global available memory 2,328,528 kB. A later initialization heartbeat gave
RSS 206,152 kB and available memory 2,862,284 kB. Those are actual partial
observations, not a bound on the eventual peak. Startup and iteration outcomes
will be appended as they become available.

At 03:17:20.340 UTC the actual 04 request recognized the exact saved height,
1729 unchanged nodes, zero raw reprojection/scaling calls, and zero canonical
boundary mismatch. At 03:17:23.966 the two-worker pool reported effective
heap limits **159,383,552 B each**, now consistent with the requested independent
128 MiB old-generation limit plus V8's young-generation allowance. Its shared
buffers total 28,028,272 B. At the 03:18:47 heartbeat the process remained
alive with RSS/HWM 528,128 kB and available host memory 1,638,764 kB.
The first full residual/Jacobian pass was still running; no success is inferred.

## Actual exit of 04

The exclusive poll `0eb406` returned driver exit 2 and closed session 72611.
At 03:21:25.853 UTC the client recorded actual Node returncode -9, no response
packet, and no complete new iteration. The driver ran 300.640836437 seconds.
The final readable Node RSS/HWM was 540,676 kB, Python RSS about 102,308 kB,
and global available memory 1,311,360 kB. Therefore the earlier suggestion
of a particular 1 GiB process cap is not established by these observations.
The independent worker heap correction did take effect, but it did not
eliminate the external kill. A universal five-minute rule also is not
established: 03 ran about 224.6 seconds and 02 about 1365.6 seconds.

The visible inherited shell limits have unlimited CPU time and address space;
the numerical driver sets DATA=6 GiB and FSIZE=4,999,999 B. Visible cgroup
limits/events remain absent. The new named cache route records actual child
limits and CPU ticks, and preserves each completed 32-stage block, so a kill
need not discard another entire residual/Jacobian pass. No physical or
nonlinear residual rule is changed.
