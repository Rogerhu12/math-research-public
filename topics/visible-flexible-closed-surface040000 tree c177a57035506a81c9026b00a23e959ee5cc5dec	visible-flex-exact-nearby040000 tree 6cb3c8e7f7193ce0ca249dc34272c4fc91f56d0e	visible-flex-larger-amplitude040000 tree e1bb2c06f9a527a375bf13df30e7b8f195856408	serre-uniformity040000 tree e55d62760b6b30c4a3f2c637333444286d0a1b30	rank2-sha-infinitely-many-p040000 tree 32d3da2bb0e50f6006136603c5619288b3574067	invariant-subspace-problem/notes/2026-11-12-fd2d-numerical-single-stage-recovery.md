# One stage worker and the actual local Newton comparison

2026-11-12, Astra-visible-flex-fd2d / numerical_recovery.
At 04:31:59 UTC, actual tool `722b0b`, session `59203`, started attempt15
from the complete actual attempt13 iteration. This is ongoing finite
numerical work. No new complete accepted state, successful DN, prefix-base,
closed surface, or whole-surface error bound is claimed here.

The authoritative activity record is
`2026-11-12-fd2d-numerical-current-runtime.md` and the independent runtime
`outputs/external-exit-supervisor.jsonl`. Prior supervisor session69873 ended
at attempt14's infrastructure diagnosis; it is not still running.

## Actual preceding results

Attempt12 completed all1728 actual full-J stage maps. Its ordered residual
reduction exactly reproduced norm `.027350999413424816`, minA
`.40449209888917953`, minD `.9932495875797576`, worst stage84/component42.
The original Riccati correction also reproduced chart condition
`240613.90680610723`. The complete state is retained separately as
`2026-11-12-fd2d-numerical-m15-w22-resume-12-iteration0-recovery.json.gz`,
754892 B, SHA256
`2e344ac8483f7de937c57228708271d237c3d7d07631b63becbf3511e7a7ce5e`.

Attempt12 subsequently received actual Node SIGKILL before the next trial
stage evaluation. Attempt13 loaded all1728 existing maps, again completed
the original base and correction, then received Node SIGKILL. Their last
readable RSS values were640460 and609720 kB respectively. Their driver
durations were276.189 and116.234 seconds. No fixed wall/CPU limit or a
particular OOM source follows from these observations.

Attempt14 reached the two-worker pool-ready event, then its Python client
saw stdout EOF. At that exact observation `proc.poll()` was still null.
The driver exited2 after156.299 seconds and archived12 files. Its original
supervisor correctly returned for diagnosis rather than silently treating
the unknown exit as another confirmed -9. No mathematical failure was
returned by the numerical worker. Actual closed file identities are in the
attempt12/13/14 `*-closed-archive.json` files.

## Actual local comparison, not a substitute full trial

New script `scripts/fd2d-cached-correction-local-trial.mjs` reads the54
already computed binary Jacobian blocks and the exact .02735 state. It
extracts the original correction and matrix helper definitions verbatim
from the actual copied core, reconstructs the original Riccati correction,
and makes only two new state-flow calls, both on old worst stage84. It does
not run another whole-tail DN or prefix BVP.

The exact cache input hash is
`f42ccb23c4ea27a86079e2ff574f9d9bc4dab0ad64e2ec476eb475454d240066`.
All54 block paths/hashes are retained in the report. The base and chart
values above match the original full calculation. For the observed stage:

| Quantity | Actual value |
| --- | ---: |
| Normalized residual of the linearized correction | 7.568686045697823e-13 |
| Full canonical trial, lambda1, true state-flow residual | .008446059183532044 |
| Centered geometric trial, lambda1, true state-flow residual | .0074002192307086635 |
| Node84 geometric/canonical difference, lambda1 | 6.443997349614428e-9 |
| Same difference, lambda1/2 | 1.6109993530161182e-9 |
| Same difference, lambda1/8 | 1.006874414573311e-10 |
| Same difference, lambda.01 | 6.444042348341394e-13 |

The corresponding node85 differences show the same quadratic scaling.
Both actual state-flow calls returned. The canonical trial was worse on
this stage; this evidence does not support replacing the original centered
geometric trial. The observed maximum canonical corrections at nodes84/85
were approximately `.00079885`/`.00129639`, although the normalized base
residual was already .02735. Thus the small residual alone is not evidence
that the nonlinear correction is negligible. This is a local explanation,
not a proof of future whole-tail convergence.

The geometric stage value happens to equal the old02 accepted scalar. It
does **not** restore the lost full accepted state and is not recorded as a
new global accepted Newton step. A complete trial still has to finish its
original1728 stage evaluations and original acceptance rule.

Actual tool `c194d6`, session40791, naturally completed with `f4483a` exit0.
Report `2026-11-12-fd2d-numerical-cached-local-trial-01.json` is34850 B,
SHA256 `86bcc4bd5d4b68fdd15b21cee2644eec225487a70dd37e69bfb1f714ae797f38`.
The actual script's stable source SHA is
`c5eb2dcf4ea1c886854927f92c2503d561193efe460e5cb5ba097688f1de3c38`.

## Concrete lower-memory execution

The new entry uses one stage worker with128 MiB old/16 MiB young and a
numerical host with256 MiB old/16 MiB young. The previous entries remain
unchanged. Removing one duplicate stage engine/table heap is a direct
resource reduction; no claim about the unknown SIGKILL sender is needed.

`fd2d-prepare-single-stage-runtime.py` generated six distinct sources from
the saved actual live tree and put byte-identical copies in the repository
and independent runtime. The complete sizes, new hashes and original
source paths are in `2026-11-12-fd2d-numerical-single-stage-source.json`:

- `fd2d-run-prefix-single.py` and `fd2d-single-tail-continuation.py` select
  the new client while preserving the physical controller.
- `fd2d-single-tail-client.py` admits one stage worker and observes an EOF
  process for at most two seconds before inherited cleanup. Only genuine
  EOF gets that brief natural-exit observation; mathematical errors do not
  wait on a live worker.
- `fd2d-single-tail-stage-worker.mjs` selects the new resource-only pool.
  Original geometric retraction, acceptance, checkpoint retention and
  original-precision finite equations remain.
- `fd2d-single-tail-stage-pool.mjs` admits one worker and preserves the
  exact original stage-flow body and ordering.
- `fd2d-single-external-exit-supervisor.py` uses the distinct entry, keeping
  the previous confirmed--9-only restart and closed-archive policy.

The pool's entire body is compared byte for byte with the saved original
pool after reversing exactly two declared changes: the allowed worker
count and explicit original cache-provenance naming. Every other line,
including the root/RK calls, profile tabulation/restoration, shared buffers,
failure ordering and mathematical reductions, must be identical. The
actual original/new source SHA values are also printed on stderr when the
pool module loads. This is cache provenance validation, not an additional
research review or replay gate.

Consequently the context continues to name the exact same original
independent mathematical map. Its original54 blocks are retained, not
discarded or relabelled as new solves. Node count, physical profiles,
options, steps, binary inputs and runtime identity still enter the original
cache key. One-worker scheduling changes which thread performs a stateless
map, not its arithmetic. The actual full bootstrap remains the deciding
calculation; this source argument is not a new finite success claim.

## Actual attempt15 identity

The independent source tree is
`/workspace/scratch/fd2dbfd2c83e/visible-flex-live-07` and the stem is
`outputs/2026-11-12-fd2d-numerical-m15-w22-resume-15`.
The actual initial state is13's complete unconverged iteration,
SHA256 `33bdee66549f595c683ec79223aea5c490cd5ec55e00fa79ca22cb55b0db7e85`.
Its exact saved207/256h vector supplies the true bootstrap target.
The original known successful full-height seed still supplies the same
physical parameters and final h. M15/W22/N512/P16/S16/audit16, depth12,
floor.05, target2e-9, original physical BC and fixed g are unchanged.

Active outputs remain outside git and are archived only after closing.
The next complete accepted state will be saved before its next full-J
evaluation; no scalar-only reconstruction is used.
