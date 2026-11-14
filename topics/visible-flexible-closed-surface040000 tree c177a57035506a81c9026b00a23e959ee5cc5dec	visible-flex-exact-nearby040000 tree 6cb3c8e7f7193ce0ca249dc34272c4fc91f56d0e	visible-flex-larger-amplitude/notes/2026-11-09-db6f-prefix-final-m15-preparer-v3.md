# Final M15 preparation v3: explicit continuation03 identity

## Scope and frozen baseline

This is a five-line identity migration of the independently reviewed `scripts/db6f-prefix-prepare-final-m15-coupling-v2.py`. The new script is `scripts/db6f-prefix-prepare-final-m15-coupling-v3.py`. It prepares the original coupled prefix launch only after the actual continuation03 has closed with the original audited target DN success and a separate successful `/root` tool-exit observation. It does not run a solver and does not assert that the prefix or the whole surface has been solved.

Baseline v2 SHA256: `8b235dfd97d558fc16e446b65bff2412642b041b9bbe6efb193fc88147426b81`.

New v3 SHA256: `273bb318dfaa2839be8fa6c532152cf708880c13591ac0fcbae5f4e97bdacdb5`.

The source ledger is `notes/2026-11-09-db6f-prefix-final-m15-preparer-v3-sources.json`. No frozen v1/v2 source, old response, old execution record, or active continuation03 file has been changed.

## Exact five-line difference

| Source line | v2 | v3 | Effect |
| --- | --- | --- | --- |
| 2 | generic closed audited target description | explicit continuation03 audited target description | Documentation only. |
| 23 | `CONTINUATION = ...amplitude-continuation-02` | `CONTINUATION = ...amplitude-continuation-03` | Changes both the default and the only permitted continuation stem. |
| 26 | `RESUME_LAUNCH = ...resume02-launch.json` | `RESUME_LAUNCH = ...resume03-launch.json` | Uses the genuine call15 response and 83 bound inputs of the reviewed recovery launch. |
| 104 | error names continuation02 | error names continuation03 | Documentation of the unchanged unique-stem rejection. |
| 239 | observation error names continuation02 | observation error names continuation03 | Documentation of the unchanged root-observation gate. |

The author compared the entire two files. Reversing exactly those five substitutions recovers the original v2 bytes. There are no other source changes. In particular `OUTPUT` remains `...fixed-m15-d12-p8-s32-q256-outer-after-amplitude`.

## Gates retained without alteration

All v2 checks remain in their original order. These include the old original command and affine prefix restart bindings; the physical restart mesh and cut-height roundtrip check; continuation progress/reproduction/input-binding consistency; exact target height; the original M15, spacing3, depth12, p8, steps32, N256, tolerance $2\times10^{-9}$ and 36-iteration settings; the original positive-root guard; and the default enabled warm boundary correction.

The final record must still be the continuation's actual `s=1` request with `jacobian=True` and `audit=True`, true convergence and an original residual below $2\times10^{-9}$. Its complete 705-entry Jacobian, 17-field cut-jets schema, eight-field source audit, checkpoint layout, source hashes, full-Jacobian history base and genuine warm parameter comparison are unchanged. The script continues to distinguish this finite source audit from a full XYZ or continuous whole-surface certificate.

Preparation, if this future gate succeeds, still changes only the original coupled command's `--tail-config` and `--out-prefix` paths. The original restart, free inlet support parameter, all numerical and physical flags, empty warmup scales and original boundary conditions remain as in v2. It does not alter the old final preparer, controller or worker.

## Three execution identities must remain distinct

Continuation03 has the genuine launch `notes/2026-11-09-db6f-prefix-amplitude-resume03-launch.json`, SHA256 `0e0f020b7c879790d9e6b3726f324cbde6a2c724f43b3dca5fff30d370a42e3c`. Its initial request resumes the closed $s=31/32$ call15 and advances by $1/64$ to $s=63/64$. The original controller still owns its own progress and reproduction files.

The actual parent invocation is the separately bound space guard in `notes/2026-11-09-db6f-root-amplitude-resume03-guarded-launch.json`, SHA256 `9d2495ea6b48872b40a3c813f0c3076819f48a88f1f5bd9dc1b1ec33bfa49594`. The guard changes process scheduling only. Its eventual `actual_child_exit_code` describes the controller child, not the Node worker and not the outer tool session. The original controller progress describes the worker exit.

Only `/root` can supply the actual observed outer tool completion. The retained v2 predicate requires `status="observed-process-completed"`, `observer="/root"`, `actual_exit_code=0`, the exact new continuation03 stem, and hashes binding the final progress, reproduction, config and target response. Thus the existing started record is insufficient. The guard's `CHILD_COMPLETED_AWAITING_ROOT_TOOL_OBSERVATION` record is also insufficient: it has neither the required status nor a root tool observation. Its `tool_exit_observed_by_root` flag remains false.

The future root observation should additionally retain and bind the guarded launch and the closed guard child record so the actual invocation can be traced. This paragraph states the execution provenance required for the final root review; the five-line v3 change does not add a new separate guard-schema predicate or misrepresent that predicate as already present. The numerical and original observation checks are exactly the reviewed v2 checks.

The genuine continuation02 observation, SHA256 `5cda4dd0fd47dd002b4c57fc648152a6307de27b9a67d5ae00090c9eab8e496e`, records outer tool exit1 from ENOSPC. It cannot pass the new successful observation check by status code or by stem. Its closed call15 is a valid warm input, and this does not turn the interrupted continuation02 into a cleanly completed computation.

## Actual negative-gate execution

The only v3 execution performed for this preparation was:

```bash
python scripts/db6f-prefix-prepare-final-m15-coupling-v3.py --check-current-gate
```

Its working directory was the topic directory. Actual tool receipt `08777d` returned exit0 and this literal metadata result:

```json
{"ready": false, "reason": "Continuation is not closed: missing 2026-11-09-db6f-prefix-flat-v17v18-m15-amplitude-continuation-03-reproduction.json", "files_written": 0, "solver_launches": 0}
```

Exit0 here means the diagnostic mode ran and reported a negative gate. It does not mean the mathematical target passed. No positive fixture, fabricated `s=1` packet, successful branch execution, new candidate, geometry backend, or solver run was made. The negative check does not preclude later completion; it records only the state at this actual invocation.

After genuine closure, the same script can be called with the actual root observation path. Until all unchanged conditions pass, no `outer-after-amplitude` configuration or command is generated. The active continuation03 is held by `/root`; this agent has not restarted or interrupted it.
