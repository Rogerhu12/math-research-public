# Observed m10 cache fixture: coarse tolerance shape passed to the fine view

Date: 2026-11-15 UTC. This records a developer-fixture failure before scientific input preparation. The production cache-reinstallation repair has still not been scientifically executed.

## Actual boundary

Run [43749820822](https://github.com/Rogerhu12/math-research-public/actions/runs/43749820822), job **132921093515**, source **dc282749384a4416e89d2f544a139779983dbec0**, completed with failure.

The decoded original log is **111,755 bytes**, SHA256
013f188cf8ec7edc50e0f05972af76a72e54032edc7870e3248342bceef1f100.

The unique M10_SOC_CACHE_DEVELOPMENT JSON plus LF is **16,752 bytes**, SHA256
1855b83bae6649a8f552e8c772ca67e3ce638a07817d5e4fd2ece20b31b06c4b.

The emitted developer duration is **0.07740371299999538 s**. Its source dictionary has 120 Python files. Geometry, primary LP and SOC LP executions are all zero.

| Evidence | Actual outcome |
|---|---|
| Original expanded ten groups | Read-only proof reuse passed; zero executions |
| Original m10 seven groups | Read-only proof reuse passed; zero executions |
| New charged-cache-miss group | Passed |
| New positive reinstall/full_views/capture group | Failed on artificial tolerance shape |
| Original-input scientific preparation | Not started |
| Historical x/y, expanded J, SOC and final values in this run | Not executed |

The old seven-group reuse also verified the immutable original driver and text-identical helper definitions. This attempt neither invalidates those paid checks nor reaches the earlier scientific capture failure again.

## Exact first error

The positive fixture reached:

    _restore_and_capture
      -> restore_failed_y_layout
      -> EntryTail154Objective.full_views
      -> FullGridValues(... tolerances ...)
      -> ValueError("finite array with the declared shape required")

Its source-defined artificial_arrays constructor expands the eleven-group tolerance vector into a complete coarse-grid tolerance array. The fixture's row_tolerances method returned that expanded coarse array. The real inherited full_views calls the same method once for the coarse grid and once for the finer angular grid. The coarse-shaped array is not the fine shape.

The source-defined coarse and fine grids have respectively four and eight angular nodes. The original full_views contract needs the **eleven group tolerances**, which FullGridValues broadcasts separately to each full-grid shape.

This is a positive-fixture interface error. It is not a failure of actual geometry, of the production same-y cache restoration, or of the SOC model.

## Minimal correction and reuse

Only the positive test, immediately after obtaining its fixture, takes:

    group_tolerances = np.asarray(objective.row_tolerances(), float)[:, 0, 0].copy()
    objective.row_tolerances = lambda: group_tolerances

The original _fixture and _charged_restore_rejected functions remain text-identical. The production restore_failed_y_layout function and all scientific paths remain text-identical.

The successful charged-miss result is reused from this partial developer report. The continuation binds its original run/job/source, complete log, exact DEV JSON plus LF, successful individual check/detail, and unchanged frozen dependencies. It reads the original small sources as text and compares the complete _fixture, _charged_restore_rejected and restore_failed_y_layout function texts with the current ones. It does not execute the charged-miss group again.

Only the unfinished positive group runs. The combined developer report explicitly distinguishes the reused negative evidence from the newly executed positive check; it does not call the original partial report wholly successful.

No new science, numerical guard, extra test group, model, LP, iteration or budget is introduced. The 117 scientific dependencies, original seven-check source, old ten checks, source configuration, bank, two-grid gates, original scalar SOC RHS and eight-value replay limit are unchanged. Runtime proof reuse requires small read-only GitHub metadata/source requests, not an old optimizer or scientific replay.

## Continuing scope

The next scientific work remains the same fixed historical m10 attempt: recover the original x/y and old model, observe zero charged ordinary evaluations while reinstalling the post-learning y layout, capture the actual failed displacement, rebuild the expanded model at x, and apply at most one original SOC under the unchanged limits. None of the latter stages is claimed paid by this fixture run.

The root agent consumed actual public pull/read at **18:59:48.888010 UTC**, after commit
7af9b9da8bee95c4cd12a68fe8f2ae64b01dd890, and private pull/read at
**18:59:52.006107 UTC**, after commit a35d33da1ba98d03e91523188f9d0e5f4d232a25.
Both rules had no diff and QUEUE remained ongoing.

Responsibility: tail_cost parsed the existing public log and repaired the fixture source without local execution. Root owns publication and any subsequent Actions run. Payloads remain temporary/job stdout; this note preserves the human outcome and hashes.
