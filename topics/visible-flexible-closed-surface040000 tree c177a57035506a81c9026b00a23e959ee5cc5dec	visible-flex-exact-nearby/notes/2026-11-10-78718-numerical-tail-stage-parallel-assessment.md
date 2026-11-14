# Read-only assessment of parallel tail stage evaluation

2026-11-10, Astra-visible-flex-78718bd0. **Assessment only: no worker thread
was created, no new ODE or DN was run, and no production source was edited.**
The live fast07 computation is unaffected.

## Conclusion and exact scope

The expensive stage flows in the current full residual and full Jacobian
evaluation are independent at a fixed shooting state. There is no cross-stage
momentum-root warm guess in the selected `fourier-root` implementation.
It is therefore possible to evaluate those stage maps concurrently while
keeping every stage's arithmetic, root branch, RK sequence and normalization
unchanged. This is a concrete implementation opportunity, not a measured
parallel speedup or a claim that all of the nonlinear solve is parallel.

The Newton correction, Riccati sweep, trial construction, acceptance decision,
height continuation and final reduction should remain in their present order.

## Actual call path examined

The active entry is `78718-prefix-tail-partition-centered-worker.mjs`, using
`78718-tail-geometric-trial-split.mjs` and
`78718-tail-geometric-trial-core.mjs`. The selected engine is built by
`78718-tail-fourier-root-split-engine.mjs`, with the root in
`78718-tail-fourier-root-momentum.mjs` and the variational flow in
`78718-tail-fourier-product-flow.mjs` /
`78718-tail-fourier-product-jacobian.mjs`.

Actual source reads were `5901e5`, `aa1ee0`, `8e5f0f`, followed by the
untruncated selected-engine reads `44e05e`, `6c277a`, `ac8001`, `fe8c6a`,
`ed7661`, and `18ae9b`. No numerical source function was called by these reads.

At a fixed array of shooting states, the core evaluates

\[
f_n=\Phi_n(y_{n+1}),\qquad r_n=f_n-y_n.
\]

`cellFlow(n,input,withJac)` takes only `states[n+1]` and the fixed descriptor
`cells[n]`. It allocates a new `K+2` state, initializes the two mean-height
components to zero, and performs that stage's prescribed profile/RK sequence.
It returns the output state, optional stage tangent, accumulated mean height,
and positivity scalars. In particular, it does not feed the output of stage
`n` into the input of stage `n-1`: those inputs are independent shooting
unknowns during a residual evaluation. The implicit coupling is imposed by
the residual and the subsequent serial Newton correction.

The stage output and tangent rows for momentum are divided by that stage's
own `portRatio`. This operation remains part of the individual stage map.
The mean-height contributions are added later in increasing stage order;
that serial summation order can be preserved exactly.

## Root guesses and shared mutable state

The selected momentum `root(state,profile,x,guess)` supports an explicit guess,
but the full residual and variational flow call it without that optional
argument. Each invocation initializes `L` from the current root target.
There is no mutable `lastRoot`, previous-stage solution, or adaptive root
branch state used to seed another stage. The local Fourier tables are built
once per engine and then read without modification.

The original split RHS increments `statistics.evaluations`,
`maximumRootRelativeResidual`, and `roundoffFallbacks`. These are observations;
none controls a numerical branch. A parallel implementation would sum the
actual counts and maximize the maxima explicitly. If it evaluates stages
beyond the first serial failure, its actual work counters can be larger;
they must be labelled as actual parallel work rather than copied as serial
counts. This does not change the residual or first-error policy.

The physical profiles do have memoization. In
`closing_recalibrated_tail.mjs`, `getEntries(n,beta)` caches fixed physical
construction data, and `entry.point(x)` caches a value computed from that
fixed data and the exact binary64 `x`. It does not depend on a preceding
Newton root or a preceding stage state. The weighted wrapper finishes its
integrand/table updates before profiles are consumed. Thus this memoization
is not a physical continuation dependency, but its values must be reproduced
or transferred faithfully when profiles move to separate isolates.

The shooting graph cache and the retained R92 predictor are different:
they belong to the global coupled correction and to preceding *successful*
DN solves. They should stay in the parent. Parallel stage evaluation must
not replace or recompute a global predictor as a side effect.

## Preserving the exact stage operation

The `f6tail_cusp_grid.mjs` and `950f-tail-subdivision.mjs` reads show two
requirements beyond retaining the same number of RK steps:

1. Keep each stage's actual profile function, raw interval, `mu`, and
   `portRatio`, including all installed `integrationBreakpoints`.
2. Keep the original state-only and full-J RK code paths, with their own
   exact floating coordinate expressions and original cusp splits. Do not
   replace the stage by a different grouped flow or interpolate a profile
   approximately.

Within a stage, RK substeps and tangent multiplication remain sequential.
Parallelism is across complete stage evaluations only.

Results should be placed by stage index, then reduced in the original
increasing-index order. This preserves the `worst` residual's tie rule and
all deterministic reductions. If multiple stages fail, the parent must
raise the error at the smallest stage index, with its original message and
`tailStage/rawCell/rawSegment` annotations. Accepting the first wall-clock
error would alter the recorded failure route. Infrastructure failures must
remain infrastructure failures, not be relabelled numerical root rejection.

## Minimal prospective implementation boundary

The current `solve` closes over its local `evaluate`, so assigning to the
exported `dn.tail.evaluate` alone would **not** parallelize Newton. A narrow
future source change would add an optional synchronous batch-flow provider
inside that actual `evaluate`. The existing serial reduction, correction,
line search, norm, tolerance and return would remain unchanged. A pool based
on `worker_threads` can compute indexed complete stage results; the present
API is synchronous, so either a synchronous shared-buffer completion barrier
or an explicit asynchronous API change is required. The former has the
smaller mathematical call-path footprint, but would need proper worker-error
and shutdown handling.

JavaScript profile closures cannot simply be passed as structured-clone
data. There are two honest options:

- Reconstruct the same fixed physical profiles once in each worker from the
  actual configuration, then use the same stage subdivision. This repeats
  construction for all `protectCell=160` physical cells, even though the
  nonlinear shooting depth is only 12.
- Transfer the parent's exact saved profile values for every finite RK
  evaluation coordinate, together with the exact cusp lists and descriptors.
  A lookup must return those original binary64 values and reject a missing
  coordinate; it must not approximate or interpolate them. Both state-only
  and full-J coordinate-expression sets must be included. This is faithful
  memoization of the already specified finite map and avoids reconstructing
  all 160 physical cells in each worker.

The second option needs careful finite-grid enumeration but smaller worker
state. A reusable pool can then give each worker a private engine cache by
`mu`. Shared input states are immutable during an evaluation; stage outputs
use disjoint slots. Returned tangent snapshots must not alias buffers that
later trials overwrite. The existing retained R92 matrices are actual
successful-state data and cannot silently become mutable worker scratch.

None of these prospective changes has been implemented in this assessment.

## Observed resources and scale of the data

Read-only resource call `1df111` at 2026-11-10 15:40:28 UTC observed:

- Python CPU affinity count 9 and `os.cpu_count()` 9.
- `MemTotal=10,206,472 KiB`, `MemAvailable=4,891,952 KiB`, and zero swap.
- No visible cgroup CPU/memory quota files in this tool's mount namespace.

The separate non-computational Node query `e260d8` reported Node
`v24.22.1`, `os.availableParallelism()=9`, and 9 CPU entries. There were no
cgroup mounts visible to that query. These observations are **not** a CPU
throughput benchmark or proof of the older solver session's quota. They
support investigating a small pool, not assuming a guaranteed ninefold gain.

The actual configuration read `4fc1ea` gives W22/N512, P16/S16, 12 nonlinear
physical cells, 1728 shooting stages, `linearFar=32`, `linearSteps=256`,
`protectCell=160`, and `warpSteps=16`. Therefore K=44 and the finite buffers
have modest sizes before engine/profile heaps:

| Buffer | Binary64 bytes |
| --- | ---: |
| All 1729 shooting input states | 608,608 |
| All 1728 output states | 608,256 |
| All 1728 stage K-by-K Jacobians | 26,763,264 |
| Mean height, minA and minD for all stages | 41,472 |
| Nominal 33 points/stage, four profile scalars/point | 1,824,768 |

The last row excludes extra cusp coordinates and lookup/index overhead.
None is an estimate of total V8 RSS. Engine tables, cached profiles, local
RK/root allocations, native thread stacks and private isolate heaps must be
accounted for separately. The existing 6 GiB per-process data limit and
1536 MiB Node heap setting must not be interpreted as automatically safe
aggregate allowances for an arbitrary number of additional isolates.

A later implementation could start with two or four workers and compare a
small actual closed stage batch, its original branch outcomes, and memory
usage. That would be an implementation check and timing experiment, not a
new mathematical acceptance gate. At present there is no measured speedup,
no new parallel result, and no reason to interrupt fast07 for this assessment.
