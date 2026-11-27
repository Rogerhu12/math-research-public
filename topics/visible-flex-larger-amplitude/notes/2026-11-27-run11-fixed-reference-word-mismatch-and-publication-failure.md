# Run 11: actual fixed-reference input rejection and separate publication failure

Observation: 2026-11-27 13:12 UTC. Session: Astra-larger-e4e2a2bf-20261126. This is an actual execution conclusion, not a proposed diagnostic or a completed surface construction.

## Actual job and two distinct failures

[Public run 46000835895/1](https://github.com/Rogerhu12/math-research-public/actions/runs/46000835895), job 140511753433, started at 12:42:09 UTC and completed with failure at 12:53:58 UTC. The GitHub job-step response identifies “Execute public research and publish independent compact records” as the failed step. Dependency installation and checkout succeeded.

The decoded complete job log was 59783 bytes, SHA256 `0562a2178c8a536808da67d673387cdc9e9d4913070e9f3259dd71824c88958d`. It was small enough to inspect. The log is not copied into Git, and no large numerical payload was fetched. The source-specific events and traceback below are the evidence for the actual input result; the older public index alone did not contain this terminal state.

Two failures occurred in order:

1. The necessary fixed-reference reconstruction process actually started and returned code 1 after 6.170325379000019 seconds. Its source rejected the actual new warm because the complete frozen mesh/chart-word contract did not hold.
2. When the controller tried to publish that failed stage, its HANDOFF replacement made the file reach the 10000-byte bound. It raised `RuntimeError('HANDOFF must be condensed before independent run publication')` before committing the new stage volume.

The second failure explains the stale public index; it does not explain or excuse the first failure. Neither is a conclusion that the mathematical research problem has no solution.

## Successful warm stage remains successful within its original scope

The complete [stage-1 public volume](2026-11-27-public-actions-46000835895-1-part-001.md) is 13752 bytes, Git blob `d7f150b0a8a68b2871b4a74b0808920c1506652f`. Its original unchanged warm recipe `561308ca74186ac8eeb302dc786b633f2f643a1f98896d0685691d06eec556a4` returned code 0 after 233.441131869 seconds.

| Actual run11 output | Bytes | Whole SHA256 |
| --- | ---: | --- |
| Warm bundle | 8767273 | `4c34e0889a40e67a3a0a38abce030bb0358f74333fc1d8c95f669d5beefd9a0f` |
| Node report | 553903 | `224a796ec9ebb5197dbfc5747394804d78a528d08198b1e2fd257a0b51b08973` |
| Scalar input | 14227536 | `89d9ebe9dc15df811af8e089e36a2d935d021b5f49b260ccde30f35820933c73` |
| Mode warm | 8809324 | `6b826d9923523f7cd61498578525be39b6b640dc5b61c926b1fe6f7e83166cb5` |
| Warm manifest | 4834 | `3ed877539c64b1ce79fd9ffdc6538f779df51560fbd07c90ccba1dd216c04983` |

The actual prefix identity was `2a27056afc507bb3d833dbaff39e7c04e4cb3f953ca160139b09142128a30eba`. The complete stage volume preserves all 22 source/input entries, literal commands and actual declarations. The warm recipe rebuilt its actual prefix, 923-node full warm and M160 input. It did not reproduce historical optimization directions. Its success never established equality with run10's frozen 160-word chart or reference bundle.

The original run10 warm is `3df37dd362a1c700eaa86eece3d0b9a17524068c2a78fe0bebb1e96f1d09518c`, 8767118 bytes. Different whole warm bytes alone do not identify which mathematical projection differs. The later complete projection guard is the specific actual rejection recorded here.

## Exact failed input execution

At 12:53:47.792 UTC the controller loaded the complete one-step queue from path commit `3690efef7159e101d59d87fe421792c7a49bb7f3`, checkout `53bd2b68206c65db2449d57b7f8df5c941a3094e`, queue SHA256 `40bdd36caede53961a10e71b54e20c9e23879822b83571999959a0e72d6f4a80`.

At 12:53:48.964 UTC it started the step with PID 3600. At 12:53:53.968 UTC it emitted the following actual compact return event:

```json
{
  "event": "followup_returned",
  "step_id": "reconstruct-complete-frozen-run10-reference-2218-first-20261127-run11",
  "state": "failed",
  "returncode": 1,
  "seconds": 6.170325379000019,
  "source_commit": "53bd2b68206c65db2449d57b7f8df5c941a3094e",
  "source_sha256": "5989b2b299d9b6a9bbc2c6bd2ee87f04eb5288ead69bcc4ec6bbb9497b9e40f6",
  "parent_sha256": "4c34e0889a40e67a3a0a38abce030bb0358f74333fc1d8c95f669d5beefd9a0f",
  "outputs": [
    {
      "path": "/home/runner/work/_temp/visible-larger-research-46000835895-1/research/same-run10-fixed-reference/report.json",
      "sha256": "3a5506df1182aa292aa1ecb28a5ea07e14ccd0bbc163e195fe4b68afa5902d2e",
      "bytes": 5149
    }
  ],
  "metrics": {
    "same-run10-fixed-reference/report.json": {
      "schema": "actual-complete-same-run10-reference-regeneration-v1",
      "source": "5989b2b299d9b6a9bbc2c6bd2ee87f04eb5288ead69bcc4ec6bbb9497b9e40f6",
      "source_commit": "53bd2b68206c65db2449d57b7f8df5c941a3094e",
      "complete": false,
      "error": "ValueError('The real new warm does not reproduce every consumed frozen mesh/chart word')",
      "origin_run": "45972294636",
      "origin_attempt": "1",
      "current_run": "46000835895",
      "current_attempt": "1",
      "physicalF": 0,
      "J": 0,
      "roots": 0,
      "old_final_or_typed_reconstructed": false
    }
  }
}
```

These are the actual selectors emitted from the runner's 5149-byte report, not a claimed full copy of that report. Its complete byte identity is known from the event; fields not emitted by the compact selector remain unread. The raw report and any runner-only data are not manufactured or replaced by this note.

The traceback points to line 310 of the complete source `reconstruct_same_run10_fixed_reference.py`, SHA256 `5989b2b299d9b6a9bbc2c6bd2ee87f04eb5288ead69bcc4ec6bbb9497b9e40f6`, at source commit `53bd2b68206c65db2449d57b7f8df5c941a3094e`. That single compound guard checks all of:

- the complete warm qjets shape (923,3,482), the mesh shape (923,), and float64 mesh/core types;
- finite strictly increasing mesh words and the complete original mesh array hash;
- the complete original 160-word core/chart array hash;
- equality of the first three core words with the actual fixed-core words;
- the exact original width .05 word.

The emitted aggregate error does not identify the particular failed clause. It is therefore not recorded as a proved failure of a specified one of the 157 other chart coefficients, nor as an observed hash of a new chart. It is enough to show that this attempted complete origin-reference reconstruction did not pass its actual input contract.

The failure occurs before `read_scalar`, the complete accurate scalar initialization, and the construction of the original 2218-leaf table, full7377 carrier and reference. The actual event reports physicalF=0, J=0 and roots=0. No original `512f/71f/081/e711` reference, same-g bridge success, old2397 address carrier, original final point or typed-memory reconstruction is inferred from this failed attempt. All scientific unknowns from runs07–10 remain unknown, not empty.

## Complete sources and parameters remain reproducible

The complete five-file input delivery and its source derivation are in [the original input note](2026-11-27-same-run10-fixed-reference-cross-runner-reconstruction.md), published by `3690efef7159e101d59d87fe421792c7a49bb7f3`.

| Complete input source or parameter file | Bytes | SHA256 |
| --- | ---: | --- |
| `computations/run10_frozen_reference_continuation_origin.json` | 45929 | `d7c6fd9d571542f9c17f3ddc4e7ace589025ca74b69246c45b0c2e4239b8c088` |
| `scripts/resume_20261126/same_run10_frozen_reference_input_binding.py` | 20775 | `5aee3276dc2c70a3adc52dda618494a8ef458f4b1496c34a5c2640c00a5735b0` |
| `scripts/resume_20261126/reconstruct_same_run10_fixed_reference.py` | 44484 | `5989b2b299d9b6a9bbc2c6bd2ee87f04eb5288ead69bcc4ec6bbb9497b9e40f6` |
| `computations/same-run10-reference-2218-run11-complete-ready.json` | 5714 | `1154925fb6b4c8fff8455903d450eb2bd7894e1e57405c6702fe39721e9751d3` |

The full ready file retains the original step, all 16 argument tokens, all 10 output paths and all 36 selectors. Its `executed:false` is its original preparation-time statement, not a new assertion that the actual run did not execute. This note supplies the later actual failed status without silently editing the original plan. The original warm request/controller/workflow are retained at launch commit `c61258a2ceb155b30b89ac032bc02a3d202f3040`.

For clarity, the whole actual input argument list is:

```json
[
  "--repo",
  "{repo}",
  "--warm-bundle",
  "{work}/fullclosed_solver/data/fullclosed-hold-warm.npz",
  "--node-report",
  "{work}/fullclosed_solver/data/fullclosed-hold-warm.json",
  "--scalar-input",
  "{work}/fullclosed_solver/data/pulse-a5-complete-base.json.gz",
  "--origin-parameters",
  "{repo}/topics/visible-flex-larger-amplitude/computations/run10_frozen_reference_continuation_origin.json",
  "--historical-public-record",
  "{repo}/topics/visible-flex-larger-amplitude/notes/2026-11-26-public-actions-45870334713-1-part-001.md",
  "--manifest",
  "{repo}/topics/visible-flex-larger-amplitude/scripts/resume_20261120/a04_historical_location_seeds.json",
  "--outdir",
  "{work}/same-run10-fixed-reference"
]
```

The 45929-byte origin definition retains the complete original actual three input-stage objects, whole origin target, complete actual parameters, old/current carrier distinctions and their sources. It does not contain fabricated raw chart words. The lower mathematical context, complete original4e methods and same-g bridge guards remain unchanged. The attempted regeneration failed before they could establish their stated current-input claims.

The complete one-step followup queue remains as the historical attempted plan. This job has ended; its presence is not a live pending invocation. Its one input step is now known to have returned failure, while no downstream solver, pure reader or accurate fee computation was launched by run11. The full source and plan obligations are retained; none is relabelled as an actual successful field.

## Publication fault and last real rule read

At 12:53:54.295 UTC the controller performed a real `git pull --rebase origin main`, reported already up to date, and then emitted `rules_unchanged_after_real_pull` at 12:53:54.320 with read commit `53bd2b68206c65db2449d57b7f8df5c941a3094e`.

The traceback then followed:

`run_followups → run_step → finish_record → publisher.publish → write_parallel_handoff`.

The complete parallel11 controller, 19587 bytes, SHA256 `4b080e95edde613e0ad5639562c73063bac9d78045608c222a234190b28f3a30`, raised its explicit HANDOFF bound error at line193. It had written the new index/volume in its working tree, but the exception occurred before `git add` and `git commit`. The last successful stage publication was `53bd2b68206c65db2449d57b7f8df5c941a3094e`, covering stage1. The repository index at 12:53:45 consequently remains a historical running snapshot rather than the actual terminal job status.

Root's later HANDOFF shortening at `0bc4ffc25343f16c4e042d1dc50b095bf3f670cc` could not repair the already-ended process. The current update records the true terminal state and gives HANDOFF more room. A future controller must avoid a long phase string exhausting the allowed summary while still publishing complete stage/source/parameter records in its proper compact volume.

Root's own last real local pull remains `eda95d51e82b126439d51d42185a880e6ddad3e9`; the execution environment has been unavailable since 07:21 UTC. Cloud metadata comparisons are recorded separately and are not described as root git pulls. The run11 actual pull above is independently supported by its log.

## Consequence for the research continuation

Do not relax the complete original chart, carrier, model or target guards to turn this return into success. Do not rerun the same hardware-dependent warm recipe and assume that it will reproduce all frozen words. A public source hash and matching first three core words do not determine the remaining coefficients of a separately rebuilt finite warm.

The next input route must either actually reconstruct the original complete fixed input from its allowed sources, or explicitly choose a different complete, predetermined and reproducible mathematical input and retain the distinction from origin run10. The user's scope permits a different mechanism or input. Repository rule15 still forbids exporting raw numerical outputs under a new “parameter” or “input” name, or through Git/Release/artifact packaging.

The live run10 continues against its original fixed reference; its later point/report/typed history are not inferred from run11. All original full-variable, accurate geometry, whole-image Hausdorff, fixed grip, all-t reach, relative-metric and same-problem refinement requirements remain. This failure note establishes neither an accepted field nor completion. Work continues toward every README requirement.
