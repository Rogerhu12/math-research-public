# Actual same-metric recovery from the last committed successful tail

2026-11-12, Astra-visible-flex-fd2d / numerical_recovery.

Current status: this old route is closed by its owner after preserving its actual states.
The maintained current-runtime note records the stop and strong-goal transition.
Status: numerical work continues in an independent runtime, under the current
exclusive supervisor recorded in `2026-11-12-fd2d-numerical-current-runtime.md`.
The original .027350999413424816 state has a complete retained1728-stage
full-J evaluation and the next actual trial has partial retained stage work.
Closed run identities below are historical outcomes, not active sessions.
No new closed surface, prefix solution, or whole-surface error bound is
claimed here.

## Recoverable state

The former workspace
`/workspace/scratch/78718bd0c4a9/math-research` does not exist in this executor.
The old tool session recorded in HANDOFF is therefore not treated as an
inherited live process. No old process has been killed or modified. The
uncommitted later stages cannot be recovered from that path and are being
recomputed from the last committed actual success.

The checked-out fast07 packets contain calls 1, 6 and 9. The recovery input is
`2026-11-10-78718-numerical-m15-w22-fast-07_tail_0009.json.gz`:

- 764073 bytes; SHA256
  `2cc67a7a0cd1652df817aff62770ca20c6b3804bd3e38af581032f787bb2ad52`.
- `response.converged=true`, recorded shooting residual
  `1.0528345037007498e-9`.
- Its physical boundary height is the recorded `25/32` of the original
  height; maximum absolute cut-height component
  `0.0006255651796652237`.
- W22/N512, P16/S16, 1729 shooting nodes, physical depth 12, original
  `.05` projection floor. The original finite tolerance remains `2e-9`.

This packet is an initial state. Its old success flag is not relabelled as a
newly computed success. The new request actually evaluates/solves its own
first tail response and then must continue to the original prefix target.

## Started computation

The new main process was launched by actual tool `9155db`, session `42321`,
on 2026-11-12 at about 02:32 UTC. The numerical agent exclusively polls it.
Its output prefix is
`notes/2026-11-12-fd2d-numerical-m15-w22-resume-02`.
The separately named console log is
`notes/2026-11-12-fd2d-numerical-runlog-02.log`.

From the repository root the complete command is:

```bash
python topics/visible-flexible-closed-surface/scripts/78718-run-prefix-parallel.py \
  --modes 15 --angular 512 --tail-modes 22 --tail-angular 512 \
  --jacobian fourier --transforms fourier --tail-jacobian fourier-root \
  --tail-predictor tangent --tail-trial geometric-centered --tail-root-precision original \
  --tail-stage-workers 2 --direct-relative-limit 0.01 \
  --tail-shooting-parts 16 --tail-steps 16 --tail-audit-steps 16 \
  --bootstrap-height-scale 1 --max-nodes 8000 --data-gib 6 --node-heap 1536 \
  --restart topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-matched-cut-s63of64-warm-01.json.gz \
  --tail-seed topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-m15-w22-fast-07_tail_0009.json.gz \
  --out-prefix topics/visible-flexible-closed-surface/notes/2026-11-12-fd2d-numerical-m15-w22-resume-02 \
  > topics/visible-flexible-closed-surface/notes/2026-11-12-fd2d-numerical-runlog-02.log 2>&1
```

The first attempted stem `resume-01` was rejected before any solve because
shell redirection created a console filename sharing that output stem; the
driver's existing non-overwrite check then saw it. The real tool `510a5d`
exited 1. The retained traceback documents this launch error. The new console
filename avoids the output-stem collision. There was no change of a physical
or mathematical solver setting.

The actual preparation record reports 2633 prefix nodes, M15/N512 and
W22/N512. It entered `tail-initialize-start` at
`2026-11-12T02:32:14` UTC. At the first observation, no new completed tail or
inner prefix had yet been produced.

At `02:35:10.439` UTC the first new request actually converged, in
163.015 seconds, to residual `1.0528345037007498e-9`. This is the genuine
same-height re-evaluation, not a relabelled input flag. Its saved packet is
`2026-11-12-fd2d-numerical-m15-w22-resume-02_tail_0001.json.gz`, 764064 bytes.
The worker constructed its own full shooting tangent and at `02:35:12.011`
UTC requested the first new height, `207/256` of the original height. The
relative target change from the recovered height is 3.5 percent. The
reported maximum relative tangent correction was `0.0818563190578319`.
This second request had not returned at the observation recorded here.

The actual first complete evaluation of this second request was recorded at
`02:41:10.744` UTC: norm `205.02414491889832`, minimum A
`0.4039249345155809`, minimum D `0.9932495200146062`, and subsequent Riccati
chart condition `240637.37110704652`. Its first original full Newton trial
was genuinely accepted at `02:43:19.903` UTC, reducing the shooting norm to
`0.027350999413424816`. This accepted trial is not yet a converged response;
the new complete variational evaluation and correction continue.

## Remaining mathematical work

The two-worker entry was already committed by the previous session. It uses
the same stage maps, roots, nonlinear acceptance and boundary conditions;
the execution-order justification is in
`2026-11-10-78718-numerical-parallel-small-height-entry.md`.
The small-height controller can try complete target changes of at most one
percent after a real success, while recognised failures still halve the
step. None of this asserts convergence of the nonlinear problem.

A successful tail at an intermediate height is not the required original
height, and a small shooting residual is not a metric bound. The next
usable actual inner will be saved by the existing snapshot producer; its
own Cartesian prefix base is then passed to metric analysis. Only the new
complete prefix/tail construction, its actual two-jets and whole-domain
metric and geometry can supply completion evidence.

## Optional four-worker follow-up

At preparation time the two-worker run and all its source files were left
unchanged. A separate selectable four-worker route was prepared in:

- `fd2d-run-prefix-parallel.py`;
- `fd2d-tail-parallel-continuation.py`;
- `fd2d-prefix-tail-parallel-client.py`;
- `fd2d-prefix-tail-parallel-stage-worker.mjs`;
- `fd2d-tail-parallel-stage-pool.mjs`.

It generalises the existing finite set of two workers to either two or four.
The stage maps, profile tables, stage index order, scalar reductions,
Newton correction, retraction, roots and acceptance criteria are unchanged.
For a given complete input state, each stage reads only its own saved inner
endpoint and immutable physical profiles. All completed results are copied
out in the original stage index order. Consequently the dependency and
ordered-reduction argument in the previous parallel-entry note applies to
any of these finite worker counts. The worker count is now recorded from the
actual selection in both ready records and pool metadata.

The `fd2d-tail-stage-pool-benchmark.mjs` experiment used only the old real
call9 stages 0, 12, 74 and 1440. Actual tool `eb4cae`/session9544 completed
with exit 0 at `d19252`, elapsed 23.2496 seconds including geometry setup.
All states, means and Jacobians were bitwise equal to the same serial stage
calculation in this experiment. For these four selected stages:

| Branch | Serial ms | Four-worker ms | Ratio |
|---|---:|---:|---:|
| State only | 994.190 | 792.776 | 1.2541 |
| State and Jacobian | 3552.843 | 1853.549 | 1.9168 |

Pool startup took 1052.795 ms. The full original tail was simultaneously
running in the two-worker route, so these local timings are not a clean
whole-run comparison and do not imply the same speedup for a complete solve.
No new DN or BVP was computed by the benchmark. The report is
`2026-11-12-fd2d-numerical-four-worker-stage-benchmark.json`, 20508 bytes,
SHA256 `88d3d149b93bc950fe1851570ca34555e50ea9a3dbee85b361772135bc014065`.
The Python route compiles and the new Node worker parses. The separate route
was not yet the active full solver at benchmark time. Its later actual use
is recorded below.

## Actual early exit and exact-height four-worker recovery

The second two-worker Newton step was accepted at `02:50:57.196` UTC:
`0.027350999413424816` decreased to `0.0074002192307086635`. That accepted
state was not serialized before the later worker stopped. The last complete
iteration checkpoint therefore remains call 2, iteration 1, norm
`0.027350999413424816`, minimum A `0.40449209888917953`, minimum D
`0.9932495875797576`.

The producer ended at `02:54:59` UTC. Actual polling tool `13756d` returned
exit 2 for session 42321. Its Python client saw worker EOF, and the controller
then reported the absent `resume-02_tail_0002.json.gz`. The old client did
not record the Node return code. No mathematical failure response, Node OOM
message, or native failure diagnostic was written. Thus the cause is
**unknown**; this is not evidence that the nonlinear system has no solution.
The observed exit and recoverable state are recorded in
`2026-11-12-fd2d-numerical-resume02-observed-exit.json`.

The complete saved height vector differs from multiplying the old full-height
successful seed by `207/256` in three high-mode slots, with maximum absolute
difference `1.9721522630525295e-31`; the first component is identical. Even
that tiny difference would prevent the old exact-height branch from
recognising identity and could trigger a ratio-one raw roundtrip. To preserve
the actual saved state, the new driver has an explicit
`--bootstrap-from-initial-checkpoint` option. It copies the retained warm
`cutHeight` as the first true requested target, records that the nominal
height-scale multiplication is not applied, and changes neither the known
physical parameter source nor the final prefix target. An unconverged warm
record remains unconverged until the original nonlinear solve succeeds.

New actual launch: tool `ec7597`, session `17640`, output stem
`notes/2026-11-12-fd2d-numerical-m15-w22-resume-03`. The numerical agent
exclusively owns this process. The previous heavy process had already ended.

```bash
python topics/visible-flexible-closed-surface/scripts/fd2d-run-prefix-parallel.py \
  --modes 15 --angular 512 --tail-modes 22 --tail-angular 512 \
  --jacobian fourier --transforms fourier --tail-jacobian fourier-root \
  --tail-predictor tangent --tail-trial geometric-centered --tail-root-precision original \
  --tail-stage-workers 4 --direct-relative-limit 0.01 \
  --tail-shooting-parts 16 --tail-steps 16 --tail-audit-steps 16 \
  --bootstrap-from-initial-checkpoint --max-nodes 8000 --data-gib 6 --node-heap 1536 \
  --restart topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-matched-cut-s63of64-warm-01.json.gz \
  --tail-seed topics/visible-flexible-closed-surface/notes/2026-11-10-78718-numerical-m15-linear-01_tail_0001.json.gz \
  --tail-initial-checkpoint topics/visible-flexible-closed-surface/notes/2026-11-12-fd2d-numerical-m15-w22-resume-02_tail-iteration.json.gz \
  --out-prefix topics/visible-flexible-closed-surface/notes/2026-11-12-fd2d-numerical-m15-w22-resume-03 \
  > topics/visible-flexible-closed-surface/notes/2026-11-12-fd2d-numerical-runlog-03.log 2>&1
```

The warm input was closed as
`2026-11-12-fd2d-numerical-m15-w22-resume-03-tail-warm-input.json.gz`,
754912 bytes, SHA256
`12d4aeb41efd1b04c51476f32de56650cbb2dde5b2af63a75b68015a986b3849`.
Its status is `iteration-recovery-only`, with no true convergence flag.
The actual bootstrap maximum height is `0.0006474599609535065`.
At `03:03:39.067` UTC the worker reported exact height equality, 1729 copied
nodes, zero raw reprojections, zero amplitude scalings, and zero boundary
correction. At `03:03:44.451` UTC the actual four-worker stage pool was ready.

### Concrete early-exit diagnostics

The new client records its own Node process's return code and last readable
`VmRSS`, `VmHWM`, `VmData`, state and thread count every five seconds in
`resume-03_tail-worker-runtime.json`. A client exception gets a separate
small scalar record. These observations do not fabricate a missing response
or alter a root, derivative, residual, or acceptance rule. Recording errors
are ignored by the numerical algorithm. The monitor stops when the client
closes.

The first observed new Node RSS was about 1,005,776 kB and grew slowly to
about 1,026,948 kB; the latter observation had `VmData=3,733,728 kB` and 15
threads. `VmData` is not resident memory. Available host memory was around
1,497,360 kB at the latter observation and swap was zero. These are actual
observations, not predictions of the peak or a diagnosis of the old EOF.

The executor exposes `/proc/self/cgroup` as `0::/`, but no cgroup mount or
v1/v2 memory limit, current, peak, event or failure-count files are visible.
Each exec has a separate PID namespace, so a new command's process list does
not establish whether another session has a residual process. No attempt is
made to identify or stop unrelated work. The root coordinates other large
calculations; numerical memory growth is watched while recovery proceeds.


### Actual end of resume-03 and material resource correction

Exclusive poll `3f8a39` returned driver exit 2 and closed session 17640.
`resume-03_tail-worker-exception-0001.json` records its actual Node return
code **-9 (SIGKILL)**, no response file, and no complete new Newton iteration.
The final readable heartbeat gave VmRSS=VmHWM=1,029,840 kB and
VmData=3,734,920 kB. SIGKILL is established; its sender or a particular OOM
limit cannot be identified from the exposed cgroup interface. This is not a
nonlinear rejection. The 02 call2/iteration1 state remains the recoverable
state; the later .007400219 accepted scalar still had no saved state.

The saved stage-pool record reveals a concrete resource-setting defect:
its four *actual* V8 heap limits were 1,660,944,384 bytes each despite the
nominal worker resourceLimits of 256 MiB. The process-wide NODE_OPTIONS
heap flag overrode those worker limits. An actual small runtime probe showed
that merely clearing or replacing worker env.NODE_OPTIONS with execArgv=[]
did not remove this override. A newly named launcher/host-worker hierarchy
has no global heap flag and gives each isolate its own resourceLimits.
The original numerical source versions used by 03 remain unchanged.
04 also observes and saves every accepted full state before the following
expensive full Jacobian, without changing residuals or acceptance. See the
separate bounded-recovery note for its source list and real execution.
