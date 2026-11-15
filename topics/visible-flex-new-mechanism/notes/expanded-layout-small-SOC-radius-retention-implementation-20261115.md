# Covered expanded-layout SOC radius retention: implementation handoff

Status: source writing and static inspection only. No compiler, developer fixture,
scientific geometry, optimizer, local research script, or new Actions has run.

## Frozen new files

| Repository script | UTF-8 blob | Bytes | SHA256 |
|---|---|---:|---|
| frame_metric_expanded_layout_hold.py | 32f3577194e35a69f1ca5cbdcee71b5514686b16 | 30871 | 69ce5f724b6642d094537c36a9778834e8ef6ec2911feb663cd752c1c6cd2ae8 |
| frame_metric_expanded_layout_hold_recovery.py | f36071a5190c805ac6bcb1a00ae511f4e9119327 | 40048 | f16d7803c37f85e558cf58587af907e278726551aee4fac7dbade7a5d6363cbc |
| frame_metric_expanded_layout_hold_development.py | 37373c6e57182126f0e16843c598b69aeab3d151 | 23192 | 960c59aea0ca64a3b1993553415ce49b43592e1297cfe2bec2d41a1e0df6f88c |

All are below 100 KB. The root owns tree/commit/ref/request/workflow publication.

## Explicit public interfaces

The new class is ExpandedLayoutHoldObjective, a subclass of the frozen
ExpandedPoolSOCObjective. Its new required keyword arguments are:

- initial_bank_context;
- initial_bank_entries;
- expected_initial_bank_state_sha256;
- expected_initial_bank_entries (exactly 11 for this successor);
- expanded_layout_hold_policy (the new POLICY).

initial_direction_records must be empty. The inherited expanded_pool_policy is
fixed internally to the frozen expanded policy; it is not added to cfg.

The exact new POLICY is:

same159-covered-expanded-pool-small-SOC-retains-model-radius-v1.

The new constructor deliberately initializes the RememberingCompleteObjective
branch directly, then installs the complete ordered checkpoint. It does not
construct a fake nine-entry predecessor or overwrite a validated expected size.
The inherited capture/rebuild, two-factory final binding, registry and original
SOC mathematics are reused. The first current complete model must match the
checkpoint context, all rational-grid row tags, the 11-entry SHA and ordering
before the first LP. No old e/f event is replayed and no normal is recomputed.

The recovery entry is run_expanded_layout_hold_recovery, with unchanged public
parameter names:

objective, initial, known_metric_locations, restored_controller,
artificial_inputs_only, evaluate_only.

Return layout and old model/trial/correction record keys remain usable.

## Exact production changes

The new outer is an explicit source-derived file from
frame_metric_expanded_pool_soc_recovery.py SHA256
db447f3395b3754a7adc95432fbb288aed2efe7393382bf6c6cbf9bc49ca963e.

Its ten text-edit regions are:

1. New source/scope header.
2. Remove the unused direct old controller import.
3. Give the original expanded POLICY a distinct EXPANDED_POLICY alias.
4. Import the new objective/controller and the already-paid cache helper.
5. Rename only the private outer entry.
6. Check the new objective type plus both policy domains.
7. Add the independent new definition to the finish metadata.
8. Replace only the radius-update callback, passing the actual live objective.
9. After learning and before capture, call the already-paid
   restore_failed_y_layout on the same y and preserve its measured charge and
   original schema/failure text.
10. Wrap the unchanged return/primary/rebound attachment with the new public
    entry and independent method metadata.

Primary inner LPs, same-layout SOC, expanded SOC arrays/RHS, all actual gates,
shared budgets, backtracking, accepted-point selection and original learning
remain as in the frozen outer. There is no monkeypatch of old modules/functions.

The cache helper is imported directly from
frame_metric_observed_m10_soc_audit.py. Its function source was already exercised
in the successful run 43750302276; it is not re-tested by this new development.
It must observe zero additional ordinary calls. A miss is reported and stops
through the inherited error/budget behavior; zero charge is never assumed.

## Full selected versus active LP rows

The live ReboundContext contains all selected base/J/groups/tolerances.
build_primary removes invariant rows from its active LP arrays. The final new
coverage check therefore reconstructs the all-selected arrays from
primary.selections and compares that domain with the context. It does not compare
active_values directly with the unfiltered context.

The final primary/observable signatures remain independently bound after both
factories. The new positive fixture contains invariant rows, so this distinction
is part of the new interface check.

## New controller evidence

next_expanded_layout_hold_trust first calls the complete frozen old controller.
Ordinary primary and same-layout SOC return the exact old tuple/report. An
accepted expanded SOC may retain B only after the explicit new checks:

- same first full x/y and unique full accepted z;
- original true descent and all original non-curvature/accepted-point gates;
- all learned ID differences soft, all old IDs retained, exact original grids;
- complete current pool/order/versions and final two-factory rebound identity;
- actual rounded z-x/z-y hashes bound to the total-step evidence;
- actual complete ratio, nonnegative small correction and small total step;
- unchanged scalar SOC RHS and original finite primal/residual gate;
- original y learning preserved, z learns no row, omitted hard rows zero;
- only the original primary curvature failure caused the old half-radius result.

Failure or unavailable evidence falls back to the exact old radius/streak. The
old successful_SOC_radius_retention object is retained unchanged, and its full
old scale-feedback report is also preserved. The independent new object is:

scale_feedback_update.expanded_layout_SOC_radius_retention.

Its fields used by the audit include:
qualified_to_retain_expanded_model_radius,
old_controller_next_radius, new_next_radius, failed_conditions.

A qualified next radius is B, never a growth, with success streak zero. The
ratio is the already-computed complete rebound prediction of actual z-x at x,
not a y-correction ratio or an old selected-model prediction.

## New development only

developer_check() returns passed and all_passed as the same boolean, plus four
independent groups. Each group catches its own error, so completed group results
remain visible if another new interface fails.

1. Covered expanded context and retention: real frozen array data/build_primary/
   capture and the new live coverage; complete affine prediction values are
   explicitly labelled protocol stubs, not research observations.
2. New-policy negative evidence: corrected new rows, missing live context,
   changed order, stale final factory binding, invalid ratio, oversized
   correction, cfg identity mismatch, and a consistently rebuilt hard-row
   addition. All must fall back.
3. Exact ordered 11-entry bank and first-model binding, including duplicate,
   invalid-normal, ordering/hash and changed-context rejection. The new
   constructor is exercised with a labelled parent-constructor/model stub.
4. Exact ordinary fallback and unchanged public recovery parameter names.

No old developer_check, old optimizer, actual surface, historic m10 trial, or
real scientific checkpoint is used as developer input. The original public
environment guard runs first. No pass is claimed until public Actions executes.

## Root transfer/audit interface inspection

The proposed root transfer blob
2b47317c82a26e2f085dc1381c057c2e9fbfa919 and audit blob
b9b9a8db7e182f322c80c5d9b81a70b065fe7be5 were read only at the constructor,
checkpoint and new_policy_observation interfaces. Their new keyword arguments,
empty old event list, passed/all_passed handling and new controller report fields
match the three files above.

The audit checks whether a later actual model uses the retained B at the accepted
z SHA; it does not infer effectiveness just from a qualification at the budget
end. That scope is consistent with this implementation.

This narrow static interface inspection is not an execution claim or a review
of unrelated transfer mathematics. All frozen source bindings and public
execution are finalized by the root.

## Root final source and public dispatch binding

The reviewed transfer above was followed by one metadata-only edit: it now records the last primary pool versions and the actual terminal pool versions separately (the final accepted m7 learned a fine row). Constructor arguments and restoration mathematics are unchanged. Final root-owned files are:

| Repository script | Blob | Bytes | SHA256 |
|---|---|---:|---|
| frame_metric_expanded_layout_hold_transfer.py | ba2f3914cfcd158e9f2d096b21bd5b7489eb6ced | 16325 | db9fc9ca1b6995a81c009268bf5ad53690ccd60e842b66518479a001a86743a7 |
| frame_metric_expanded_layout_hold_audit.py | b9b9a8db7e182f322c80c5d9b81a70b065fe7be5 | 29705 | cde42fcbaff2a47fd1f74d92cb1cbc7e6595571d4b70facccfaf50e98663c841 |

The request is `computations/request-expanded-layout-hold.json`, 31451 bytes, SHA256 c9d4d2ead7efd0ecd0fbbccc3b53bdbefedce431d772f46bf7becd2906b22346. Its 128 bindings cover 125 Python sources and the three checked-out workflows. Only the five new Python files are compiled; only the four new development groups are executed. Frozen 117-source expanded checks and 120-source successful cache evidence are consumed from their pinned completed logs, with zero old optimizer, developer, direction-event or historical-m10 replays.

The independent workflow `visible-expanded-layout-hold.yml` performs actual public and private pulls and README comparisons before science, retains the same-session ongoing QUEUE entry, removes MR_TOKEN from the scientific subprocess environment, restores the pinned source, verifies every requested binding, then calls the one new audit. Source checkpoint: run43744903357/job132905938795; physical 981e092c54a5a7059bc75ffaea2f2c8bfa47c0b4c2f5932a67bd3fc74cee5376; original eleven-entry bank d5b1b9d6128f05e0003baa1c22b109d0d9d4fb6598bfa0ba93f0ec969c127cb8; complete pools4418/4188; B=1/8000 and streak0. Old configuration and 12LP/40values/120active/10perLP limits are unchanged. This commit authorizes this one method stage; its success, actual new-policy qualification and next-model use remain to be observed.
