# Stable runtime, preserved stage work, and actual resume-07

2026-11-12, Astra-visible-flex-fd2d / numerical_recovery.

Current status: this old route is closed by its owner after preserving its actual states.
The maintained current-runtime note records the stop and strong-goal transition.
Status: the resume-07 initialization described here is historical and closed.
The subsequent actual running route is recorded in
`2026-11-12-fd2d-numerical-current-runtime.md`.
No new DN response,
prefix solution, closed graph, or whole-surface metric bound is asserted.

## Closed predecessor outcomes

Resume-05 ended with actual Node returncode -9 and driver exit 2
(`35f4d9`, session 42979). Unlike 03/04, it retained 14 completed blocks,
448 actual full-J stage maps. No complete new full-J evaluation or Newton
iteration had finished. Its last readable Node CPU total was about 214.72 s,
RSS/HWM 548,936 kB, Python RSS 102,844 kB, and global available memory
1,528,848 kB. The observed child CPU/AS/RSS limits were unlimited, DATA 6 GiB.
The particular sender or reason for SIGKILL remains unestablished.

Resume-06 exited 1 before creating Node or a DN request (`3eac14`, session
82820). The parent's concurrent ordinary git rebase temporarily removed a
newly committed source at startup. This was a missing-file launch failure,
not a mathematical rejection. Its 4-worker plan did not execute any new map.
The 448 already computed stage maps remained intact.

## Independent source and input tree

The actual source/input copy is
`/workspace/scratch/fd2dbfd2c83e/visible-flex-live-07`.
It is outside the live git worktree and contains no symlinks. Its numerical
topic is under `topics/visible-flexible-closed-surface`; active outputs are
under its `outputs` directory. Ordinary git pull/rebase therefore cannot
temporarily remove these active files or rewrite an active mode-run report.
Closed recoverable outputs are copied back into repository notes.

`fd2d-prepare-numerical-runtime.py` copied all scripts, the complete small
`repro/source-root`, and the actual profile/chart/port/restart/seed/warm/config
inputs. The first manifest covers 725 files and 8,041,253 bytes. Each copied
file was byte-equal to its recorded source at copying. The compressed
manifest is `2026-11-12-fd2d-numerical-live07-source-input-manifest.json.gz`,
48,180 B, SHA256
`ce3005194aabfd49b19f7256dca012f9c14f260ad9eb404a38ac078a72125026`.

The 719-byte `closing_tail_dependency_blobs.json` was then copied as an
explicit additional required input, before any numerical run. The addendum
records its hash. The new relocation-v2 utility is likewise separately
recorded; it is not among the finite stage map's eleven mathematical/runtime
dependencies. No active source file is edited after launch.

## Preserving the real 448-stage cache under new paths

The previous cache context includes absolute source paths. Copying the same
code changes those paths, so it changes that context key even though the
finite map is unchanged. `fd2d-relocate-stage-cache-v2.mjs` handles this exact
path relocation without repeating a stage flow.

It checks all eleven copied dependency files against their old SHA256 values;
uses the saved pool's exact profile-tabulation routine on the copied physical
configuration; and serializes those tables, options, runtime and old source
identities. The resulting **complete old context hash must equal the old
recorded hash**. This checks all tabulated profile bits and options, rather
than inferring equivalence from filenames. The newly created context must
have exactly the same dependency closure under the new paths.

For each old block, the binary record's old key and dimensions are checked.
The same Float64 arrays for output/J/mean/minima are retained; only the
path-sensitive context key is changed before serialization to the new cache
directory. The original blocks are untouched. This is recovery of already
computed map values, not a mathematical solve or a new acceptance condition.

The actual relocation completed with exit 0 (`acd115`, session 82526):

- Old context: `62559272cbca5892f83ba486e8c077a74d1d0e9c6d22a6db712cda244ee0e875`.
- New context: `365129aaa13944659ed3b55a21ac4726ccbe2a28d94fc003e6b0af63f6aa0e04`.
- Actual input hash remains
  `f42ccb23c4ea27a86079e2ff574f9d9bc4dab0ad64e2ec476eb475454d240066`.
- Retained 14 blocks / 448 stages; zero new stage flows, DN solves or BVP calls.

The closed 15,415-byte report is
`2026-11-12-fd2d-numerical-live07-stage-cache-relocation.json`, SHA256
`01ae2316448b183820c11899e39dcba3575e992b14db80e7c2137da476e4123e`.
Its block indices retain both old and new file hashes. The large binary
cache remains under `/workspace/scratch/fd2dbfd2c83e/visible-flex-stage-cache`.

Two preparation failures are retained honestly: the first attempt lacked
the dependency-blob manifest; the next used `cfg.projectionFloor` without
the original DN's `.05` default. It therefore correctly failed to reproduce
the old context. V2 supplies the same original default; it does not change
the numerical solver's floor. Neither failure evaluated a stage flow or
altered an existing cache block.

## Actual run 07

Launch `a232d4`, session **3553**, exclusively polled by numerical_recovery.
The active output prefix is
`/workspace/scratch/fd2dbfd2c83e/visible-flex-live-07/outputs/2026-11-12-fd2d-numerical-m15-w22-resume-07`.
Its console is the separately named `2026-11-12-fd2d-numerical-runlog-07.log`
in the same output directory.

The copied entry is `fd2d-run-prefix-snapshot.py`. This explicitly saves
each request's complete initial state before its first long full-J pass,
in addition to full-iteration and immediately accepted-state snapshots.
The request-initial record is marked unconverged and is not an accepted
Newton step. Thus a kill at a newly requested height no longer loses its
complete initial state or forces a changed-height reconstruction.

The finite configuration remains M15/N512 prefix, W22/N512 tail, physical
depth 12, P16/S16/audit16, projectionFloor .05, solveTolerance 2e-9, and the
original physical/boundary conditions. It bootstraps the actual retained
207/256-height vector, not a re-multiplied approximation. The saved state
still has norm 0.027350999413424816; the lost later .007400219 state is not
invented. The known physical seed is still the copied successful full-height
W15 packet. The final requested original height and fixed g are unchanged.

This run selects four independently limited 128 MiB old-generation stage
workers and a 256 MiB old-generation host Worker (all young generations
16 MiB). No process-wide V8 heap flag is used. Actual effective limits, RSS,
CPU ticks and cached stage counts are recorded as the run initializes.
The smaller host envelope and retained stages are explicit resource choices;
they are not assertions about the unexplained external kill.

The invocation is the prior full cached command with the independent copied
driver/source-root and copied six named data inputs, `--tail-stage-workers 4`,
`--node-heap 256`, and the above independent output prefix. Its actual
mode-run/config metadata retain every numerical argument. Active metadata
are not staged in git. On a real external -9, the next attempt resumes the
latest complete request/accepted/iteration state and same exact-input cache;
a numerical rejection remains a separate issue to diagnose.

Observed startup and actual completed iterations will be appended as they
arrive. A cache hit or a small shooting residual does not replace the required
own prefix/complete tail, physical residuals, continuous metric and geometry.
