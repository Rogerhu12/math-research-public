# Actual-RK warm for the P16/S16 shooting partition

2026-11-10, Astra-visible-flex-78718bd0. This is an executable numerical
entry, not a new solution or certificate. Root actually started fast07 with
tool `be42ba`, session `67954`, after intentionally stopping fast06 with
`719dc2` (actual exit 1). Root exclusively observes the process. The unchanged
fixed geometry and physical target are those already recorded in HANDOFF.

## Why this change

The actual fast05 worst stage has a momentum-to-momentum Jacobian entry of
order `1.97e6`. Centering R95 removes its measured zero-direction conversion
bias but does not assert that the whole finite system will converge. The
P16/S16 entry instead halves each shooting map while retaining the original
256 nominal RK steps per raw physical profile. R98 proves the exact-arithmetic
zero-set and defect-propagation statements. In particular, **nonzero old and
new normalized residuals are not asserted equal**.

The original physical depth 12, original floor `.05`, root precision, Fourier
equations, finite shooting target `2e-9`, original prefix target and final
metric/reach requirements all remain. The numerical parameters are now
`shootingParts=16`, `steps=16`, `auditSteps=16`. The last is explicitly recorded
in configuration, run metadata, policy and the worker ready record, so the
final point audit also keeps 256 nominal steps per raw profile.

The actual configuration uses `linearSteps=256`, not 512. Its original
`max(8, ceil(linearSteps/P))` is 32 for P8 and 16 for P16, again retaining 256
nominal linear steps per raw profile. The far graph beyond physical depth 12
uses the same original parameters.

## Actual warm construction

The actual input is the newer saved **UNCONVERGED** fast06 iteration 2:

`2026-11-10-78718-numerical-m15-w22-fast-06-partition-recovery-input.json.gz`,
385457 bytes, SHA256
`662846709e8882f73efd8c4fe743c0ca186829083bf472ef3b835974d2fc1f4c`.

Root closed this snapshot with actual tool `04c7b5`; its own saved norm is
`2.9962890661398417e-9`, minimum A `0.9605876583918307`, minimum D
`0.9989651369830822`. It supersedes the fast05 iteration-3 input in the initial
proposed command. The earlier input and its run remain preserved.

It has W22/N512, P8/S32 and the actual height `h/8`. It is used only as the
worker initial state. The known successful W15 packet still supplies the
unchanged physical parameters and original height `h`; the actual first new
request is `h/8`, and genuine continuation must subsequently return to `h`.

The new `78718-tail-partition-warm-remesh.mjs` calls the existing
`950f-tail-warm-remesh.mjs::remeshCheckpoint` with the **actual selected cell
engine objects**, already using the original-precision Fourier-root backend.
It does not silently switch to the older root implementation. Each inserted
midpoint comes from 16 actual RK updates from its saved inner endpoint, with
the actual critical-point splits. All 865 old nodes are copied without a root,
raw conversion, amplitude change or momentum reprojection. The new grid has
1728 stages and 1729 nodes, including 864 inserted nodes.

The worker records whether all old values remain bitwise equal and the actual
construction duration. It does not claim bitwise equality of the entire old
flow and the new composed flow: reconstructed affine profile coordinates and
critical-point arithmetic can change floating evaluation order. The new full
residual is actually evaluated. Same-height warm reuse then directly copies
these new canonical states, without another zero-amplitude conversion.

## Exact launch command

From the repository root, after the previous heavy task has actually exited:

```sh
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python \
  topics/visible-flexible-closed-surface/scripts/78718-run-prefix-mode.py \
  --modes 15 --angular 512 --tail-modes 22 --tail-angular 512 \
  --jacobian fourier --transforms fourier \
  --tail-jacobian fourier-root --tail-predictor tangent \
  --tail-trial geometric-centered --tail-root-precision original \
  --tail-shooting-parts 16 --tail-steps 16 --tail-audit-steps 16 \
  --bootstrap-height-scale 0.125 \
  --max-nodes 8000 --data-gib 6 --node-heap 1536 \
  --restart topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-matched-cut-s63of64-warm-01.json.gz \
  --tail-seed topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-m15-linear-01_tail_0001.json.gz \
  --tail-initial-checkpoint topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-m15-w22-fast-06-partition-recovery-input.json.gz \
  --out-prefix topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-m15-w22-fast-07
```

Output stems remain exclusive; no existing output is overwritten. The source
`78718-prefix-tail-partition-centered-worker.mjs` is a new worker, so the active
fast06 centered worker file was not edited. The generic driver/client and
continuation adapter accept and record the three explicitly declared numerical
fields plus their resulting stage count; all other physical comparisons stay.
The full-W terminal response, genuine final Jacobian/audit and original
physical BVP/BC tests remain.

## Resource and actual check scope

The main full evaluation still has 27648 nominal state RK steps before cusp
splits. The one-time midpoint warm has 13824 nominal state RK steps. Shooting
algebra and per-stage storage grow with the stage count: one retained W22
44-by-44 float64 Jacobian per new stage occupies 26763264 bytes (about 25.5 MiB),
twice the previous family. This is a count, not a measured total-memory bound;
the unchanged DATA 6 GiB / Node 1536 MiB limits apply and no second heavy task
is launched concurrently.

Actual tool `63fe15` naturally exited 0 after syntax and algorithm-selection
checks: the Python entry/client/adapter compile, both new Node files parse,
and the explicit branch selects the new partition worker and 12 additional
sources. These checks executed **0 RK steps, 0 DN calls and 0 BVP calls**. They
do not stand in for the future actual warm construction or finite solve.

Changed implementation files: `78718-run-prefix-mode.py`,
`78718-prefix-tail-geometric-client.py`, `78718-tail-mode-continuation.py`.
New files: `78718-prefix-tail-partition-centered-worker.mjs`,
`78718-tail-partition-warm-remesh.mjs`. The original core, centered helper,
physical evaluator, root source and active fast06 worker are unchanged.

Read-only tool `8ff3a5` checked the newer input's size/hash and scalar labels.
It observed `partition_warm_start` at `2026-11-10T13:40:41.830Z`, explicitly
P8/S32 to P16/S16, using the new run's retained input copy. At that observation
there was no completed warm record or finite response. This is an actual
initialization event, not a claim of finite success or a process exit.

Read-only `3e22bb` subsequently observed the actual warm complete at
`13:41:07.093Z`: **25.262 seconds**, 865 old nodes bitwise preserved (maximum
change 0), 864 actual RK midpoints, 1729 total nodes, 13824 nominal partial-flow
RK steps and no momentum reprojection. At `13:41:07.124Z` the first request
reused those same-height states directly, with zero boundary mismatch, zero
raw reprojections and zero amplitude scalings. The closed scalar excerpt is
`2026-11-10-78718-numerical-m15-w22-fast-07-partition-warm-observation.json`.
Its 13 selected actual worker/source identities match the run record. The
retained warm input equals the root-closed input byte for byte. Neither this
observation nor midpoint construction supplies a new successful finite DN.

The tail-research agent independently executed just the old worst stage12's
two half maps (`ab6859` / session5390, then `acceb4` exit 0). It reported
momentum-block maxima `1.970607e6` for the old full map versus `2538.806` and
`4950.734` for the halves; the frequency63 diagonal entries were about
`-1.08368e6` versus `-1855.041` and `-3544.254`. In this **single tested stage**,
the first-half midpoint and the composed final shape were bitwise equal to
the original saved RK trajectory. Full details are in
`2026-11-10-78718-tail-half-stage-gain-01.json`. This local observation supports
shorter shooting blocks, without promoting it to a whole-tail or nonlinear
convergence claim. Its input was the earlier fast05 iteration3 state
(`18996bebb3b...`), as verified by read-only `4cc7e9`; it was not a separate
Jacobian evaluation of the newer fast06 iteration2 warm used in fast07.
