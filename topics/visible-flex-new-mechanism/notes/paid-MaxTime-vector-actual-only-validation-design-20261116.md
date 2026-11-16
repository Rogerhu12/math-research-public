# Paid MaxTime proposal: value-only validation under the continuing finite-cone ledger

## 1. New operation and fixed scope

The completed finite-cone run 43792959676, job 133055320913, source c0e7336c28b8d1b1f83306e3a0781069f57c0f48, stopped after model 27's first backend call returned MaxTime. This operation evaluates the physical proposal that was already returned and saved by that paid call. It does not solve that model again, reclassify MaxTime as Solved/AlmostSolved, or claim the old finite-cone return qualification.

Proposed policy: **same159-paid-MaxTime-vector-actual-only-validation-v1**.

The operation authorizes zero new solver calls, zero new SOC calls, zero Jacobian or full-grid directional oracle calls, and no replay of any of the earlier 26 physical trials. Its only potentially new scientific values are the original complete coarse and fine evaluations at previously untried fractions of this one paid direction. All actual gate tolerances, g, b0, height/reference objects, coordinate map, actual target, and the continuing finite-cone and original global resource ceilings remain unchanged.

The final current state is accepted index **52**, physical SHA256 **0c03e09059cac846ec5ab6a246236c52b42d28394930aa35759953ea2ce1fc21**, with η = **0.2660182947853381**, B = **0.00025**, legacy/covered streaks **0/0**, pools **4448/4543** at versions **13/12**, bank **512**, and committed curvature memory **62 events / 61 commits / pending 0**.

## 2. Why no model or J reconstruction is needed

The existing actual acceptance block in scripts/frame_metric_finite_cone_recovery.py separates into:

1. Construct the physical point from a current state and physical direction.
2. Validate the coordinate and exact height identities.
3. Evaluate ordinary geometry and the original coarse/fine gate decisions.
4. Compare the true metric values to the accepted base.
5. Subsequently compute affine diagnostics, update model-based memories, and update controller quality.

Only items 1–4 are needed to establish whether a particular saved physical point is admissible and improves the true metric. None requires the two missing solver auxiliaries, an affine prediction, or J.

The actual point construction remains the original expression:

`step = float(Q(alpha_exact)) * p`

`y = objective.subspace.apply(x, step[objective.subspace.columns])`

The value-only branch must use this same map and rounding order. It records the actual y, actual y−x, exact binary64 159 coordinates, and exact original physical 163 coefficients. It must not replace this by an independently rounded x+p formula or reconstruct unknown original solver auxiliaries.

The original source acceptance test is:

- Both actual grid decisions are admissible under their original gates.
- The maximum of their direct η values is strictly smaller than the original accepted η.
- The decrease is at least the original minimum accepted amount, **1/10000000**, unless both original new-target-qualified flags are true.

The latter exception is the existing acceptance rule; it is not an added tolerance or change to the target.

A standalone physical validation may prove this test for the saved point without proving that the point passed the old optimizer return path. Its output must keep these two claims separate.

## 3. One latest-source read and exact provenance

Read the completed finite-cone job log once with the existing read-only GitHub reader. Do not download predecessor logs or restore an earlier optimizer.

Required original byte fingerprints:

| Record | Bytes | SHA256 |
|---|---:|---|
| Whole original log | 7416045 | a4a20c9f481fc5d8f1fcce7f279c9c8361e5c84d2da7edd324bd9180b97024c0 |
| REQUEST JSON + LF | 30464 | 071fa607bf2fb70a7300876a4b53c669ea520faeb8cfe0a0ad7f6532ec474899 |
| DEVELOPMENT JSON + LF | 2464 | 3e3f8828d6340932c7661f2c35d6aa8da972b45609fcc80759db5e82a9292e75 |
| PRIOR_WORK_REUSED JSON + LF | 2069 | 1cd1679d023e03a470570c4bf5f35b5d7514fd07db43a19a46048afefe48a271 |
| MODEL 27 JSON + LF | 84126 | 046520467133e26d2449bfcf1a7aedb7e85b16da3b00e480727706daa567cbb9 |
| COMPLETE JSON + LF | 3202149 | 8a67d74a139e06c50c6f19e6b265a0c7e5788bd7e6681259712fb8d70a3b189e |

The source request file is 41315 B / 340d6f063831331cfa56f9da64785a05f74a60c7d76c9a858be6c63c5563df64. Its old 175 bindings, including 164 Python files, remain frozen and are checked by the new request. New entry files, if implemented, are separate additions.

The source DEVELOPMENT is already passed: three groups, 3/4/5 checks, 12 total. Reuse it without any new call to developer_check. The prior nine geometry and eleven release checks remain transitive paid evidence. Source integrity checks and decoding are not new developer/scientific execution.

Parse all native MODEL records, require exactly 27, and select original number 27. Require:

- source job completed successfully as an audit, with the exact source head/link;
- model 27 base accepted index 52 and physical SHA equal to the final checkpoint;
- one cone event, new cone ordinal 31, backend MaxTime, finite_original161_vector true;
- returned_candidate false and no model-27 physical trial;
- the saved step source is the actual new cone return before any filter;
- the exact159 list exists, is finite, and round-trips through its binary64 rational representation;
- its recorded array SHA256 is **17605ea24e9cefa4a73410913b3287c7b0f4b5303550a38f2da0f99850a0c644**;
- the report has no saved rho/norm on this event, and the new code does not manufacture them.

The paid event's A/J/rhs/guard/binding hashes remain provenance. This value-only operation does not claim to reconstruct or independently verify those numerical arrays.

## 4. Base restoration without base geometry

Use only the latest COMPLETE.future_finite_cone_checkpoint and the same 24 necessary original immutable input reports. Restore the original reference163, exact current159/current163, coordinate definition, DirectReferenceFiveHeightField, original quadrature order 8, and the original physical gate through its correct field-bound constructor.

The complete source field and coordinate identities are:

- Configuration 1c8a50e50f7428e61e5fc6aedb258c857afff72c1819b2f7950677f014964e19.
- Ordinary field 8e77c49888fce6d8abe6b02f2e9a0a7651d4b76ef83328b3d134a2adde697ab1.
- Coordinate definition b37cadb78c9b9e70a6359bbf81d3debbd4089104ce5758105739c9278752a580.
- Factorization definition b6cc198b6b58ec0484438c910a1e05a1273bc0cec81715415b8f538d31661963, retained as provenance; no factorized J is evaluated.
- Source conic objective e101bd909dbdb5fb2c7f839b2d416b66e473bf7326dfb80e7af396f3f97a26b6, retained as source identity.

Do not call FiniteConeObjective.__init__ unchanged: it correctly describes the first transition from the older accepted27 source, including hardcoded source counts and versions. Reusing that first-entry constructor would reset the current scope or reject a legitimate latest checkpoint. Implement a thin value-only restoration around the already frozen ordinary-value base class instead, with explicit source52 counters and a separate validation-procedure identity. Do not impersonate the old conic objective definition.

The source physical state is checked against its exact map and source reference. The initial accepted η and 14/14 gate booleans come from the existing actual model-26 accepted trial whose physical SHA and index agree with the source checkpoint and COMPLETE final selection. Do not call evaluate(x) or fine_decision(x) just to reproduce already paid source values. Do not populate a numerical geometry cache with invented arrays.

The first new adapter call is therefore at y, not x. Its cold prefix initialization may still cost time; that time remains fully charged.

## 5. Fractions, exact point evidence, and ordinary gates

Try α = 1 first. No previously executed physical point is included: model 27 has no trial, and the source log is checked for this fact.

If backtracking is needed, use only the original finite list defined by maximum_backtracks_per_model = 6:

**1, 1/2, 1/4, 1/8, 1/16, 1/32**.

Each fraction is constructed from the same source x and original paid p. A returned candidate from a failed fraction must not become the next base. Stop on the first accepted candidate. Repeated or bitwise identical rounded points are identified and not reevaluated.

Before a geometry call, enforce the existing coordinate validation, fixed exact height slots, and original physical-box eligibility. Preserve the original trust parameter and report actual displacement norms through the original physical map; do not rescale or normalize p into a different direction. No unavailable auxiliary norm is inferred from the stored physical vector.

At each new point, save the exact159/exact163 point and physical hash before evaluation. Call the original ordinary coarse evaluation, then the original fine evaluation when the coarse regularity screen permits it. Missing fine is reported as missing, never filled from the source or another fraction. A candidate cannot be accepted without complete original two-grid admissibility.

For this validation, the fine value may be requested after a regular coarse value even when the coarse value already fails another acceptance condition, so the true two-grid outcome is visible. This does not change any acceptance gate. There are at most 12 started ordinary evaluations for the six fractions, below both remaining value limits. An early invalid/duplicate point may consume zero values. A started value that fails or returns after a time boundary remains charged.

All gate booleans and underlying direct quantities are recorded with the original tolerances. The exact physical coefficient box remains distinct from floating-point height/cap comparisons.

## 6. Information updates that are and are not available

Ordinary full-grid values support the existing coarse/fine row-learning functions without any J. If those functions are used, retain their actual original IDs, order, pool versions/history, capacity checks, and all newly observed hard/soft rows. A failed candidate that learns new rows ends the original fixed-direction backtracking attempt, as in the source ordinary path. No unreported pool initialization or automatic min-row expansion is allowed.

This operation does not call any of the model-dependent routines:

- curvature_trial_diagnostics against a rebuilt or guessed base/J;
- observe_first_primary_defect;
- actual_metric_error or any complete affine-error decomposition;
- primary_observable_model or a selected/fine J builder;
- the directional oracle, new support selection, or norm-bank update;
- covered-growth, SOC-hold, or any actual/predicted-ratio controller.

The 512-entry bank, its eight supplemental supports, and committed curvature learning are retained as source information. The bank remains a set of true unit-ball normals for future models, but no claim is made that it was numerically rebound to a new model here. The curvature memory stays at 62 events / 61 commits / pending 0 with unchanged coefficients and state hash; no extra commit_pending call is made.

The source B = 0.00025 and both zero streaks are retained. This is a validation-only operation; it claims no newly qualified ordinary growth or new held-radius decision. If a candidate is accepted, its index becomes 53 in a separately recorded validation trace, with the exact paid direction and source model as provenance. Otherwise the selected point remains 52. Old model 27 and its MaxTime status are immutable.

## 7. Continuing clocks and value accounting

The source final top-level COMPLETE is authoritative:

- Finite-cone science already spent: **657.9451113929999 s**.
- Original cumulative science already spent: **1014.074931654 s**.
- Older source offset: **356.129820261 s**, already included once.
- Finite-cone calls already started: **31 / 32**.
- HiGHS already closed: **64**, with 63 primary and one SOC.
- Actual values already used: **116**, with 58 coarse and 58 fine.
- Finite-cone new values already used: **54 / 96**.

Start this continuation's monotonic scientific clock before the new source-log read or required original inputs. At time now, add only this attempt's elapsed scientific time to the two authoritative source clocks above. Do not use the earlier checkpoint clock, reset the finite-cone task, or re-add the old 356-second offset.

Both deadlines are enforced before and after nonpreemptive value calls:

- Finite-cone cumulative science ≤ 1200 s.
- Original cumulative science ≤ 1800 s.

The effective initial remaining science is **542.054888607 s**. Source/input read, object reconstruction, current cold primitive construction, geometry, gate evaluation, source/checkpoint serialization and all validation work are charged. Import/process overhead is reported separately and is not fabricated as a second copy of the scientific elapsed time.

Both value limits are enforced:

- Finite-cone cumulative new values ≤ 96, leaving **42**.
- Original cumulative values ≤ 160, leaving **44**.

The operation starts no solver and leaves the unused 32nd cone allowance untouched. Its own new-solver budget is exactly zero. This is not an instruction to spend the remaining allowance after validation.

For each started value, increment the proper coarse/fine counter exactly once even if the call raises. If a nonpreemptive cold call finishes after a deadline, report the actual overshoot and stop; do not call it an in-budget completion. A failure before geometry still retains paid parsing/prepare time. Future retry, if ever authorized, must inherit that final cumulative clock and completed value counters.

## 8. Output and a minimal source split

Two new Python files are sufficient in principle:

1. A thin validation engine / value-only objective containing explicit current-state restoration, continuing dual clock and value caps, same physical map, original ordinary decisions, and the finite fraction loop.
2. An audit/transfer entry containing the one latest-log reader, exact fingerprints and source closure, paid-development reuse, original 24-input restoration, semantic output, and final recoverable checkpoint.

Neither file edits an old source or calls a solver. The existing original value routines, row-learning routines, physical gate constructor, coordinate map, and DirectReferenceFiveHeightField are invoked without mathematical changes. An existing read-only pull workflow pattern can run the new entry after its source manifest is reviewed.

Output must retain:

- immutable original MaxTime event identity and exact paid p159;
- source accepted52 exact point and original two-grid gate receipt;
- every new candidate's α, exact159/exact163, physical hash, actual map norms, start/completion/error and charged values;
- both actual grid decisions and all 14 gate booleans where computed;
- true decrease / original threshold decision and source-or-new selected point ownership;
- actual row-learning IDs and pool histories if updated;
- explicit null/unavailable affine prediction, model residual certificate, rho/norm and controller qualification;
- unchanged bank/curvature-memory hashes and the reason no model-based learning occurred;
- original31/64 solver counts, zero new solver calls, final current and cumulative clocks, value counters, process/RSS, and new geometry component timings;
- a recoverable selected checkpoint with source or new actual gate ownership.

The first entry checks this new source schema and receipt chain. It does not rerun the paid 12, nine, or eleven development checks, and it does not run an additional old numerical suite. No published claim that a new implementation has executed is made by this paper contract.

No scientific payload, raw log, full checkpoint, or numerical array is stored in Git or an artifact/cache service. New source and the human result may be published; actual payload remains in the authorized runner stdout and temporary files.

## 9. Exact conclusions permitted by each outcome

If α = 1 or a permitted untried fraction passes both original grid gates and the unchanged true-decrease rule, the new point is an actual admissible improving point obtained from a previously paid MaxTime physical proposal. It is not a retrospectively successful Clarabel solve or a certified old conic incumbent.

If it fails the gates or decrease rule, report the actual failed conditions and retained source point. If the clock or value allowance stops the work, report the true partial result and charged cost. If all fractions fail, only this fixed finite list has failed; no stationarity, local nonexistence, or continuous feasibility conclusion follows.

This task extracts genuine new physical information from an already saved vector. It does not repeat the paid cone solve or silently weaken its status filter.
