#!/usr/bin/env python3
"""Whole reversible parameter-only derivation for the existing observed run16 source.

This constructs JSON, not a scientific field. No Torch/NumPy, Actions dispatch,
runtime input, checkpoint, report or source guard is executed here. The three
existing scientific/launcher/reader bodies stay unchanged. This is a source
construction utility, not an admission test or a prerequisite scientific job.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path

DATA = json.loads(r'''{
  "schema": "complete-observed-same-source-restart-parameter-derivation-v1",
  "parent": {
    "name": "fixed-fejer-stage-point-observed-independent-complete-ready.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-stage-point-observed-independent-complete-ready.json",
    "bytes": 97225,
    "sha256": "86d39c01d5a93c5a4d897a02d79bddd23a9b98daa6d6fae6940cc5d348da92f6",
    "git_blob_sha": "03daa9af5617879a6fea591a2a2d6dfe78e78836"
  },
  "output": {
    "name": "fixed-fejer-stage-point-observed-same-source-restart-ready.json",
    "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-stage-point-observed-same-source-restart-ready.json",
    "bytes": 98954,
    "sha256": "6453b121b05d8e226fded98313249074fcdfa55776403a43a6703bf386f69a04"
  },
  "old_base": "fixed-fejer-stage-point-observed-independent",
  "new_base": "fixed-fejer-stage-point-observed-restart-01",
  "top_changes": [
    {
      "key": "schema",
      "existed": true,
      "before": "complete-fixed-fejer-stage-point-observed-ready-v1",
      "after": "complete-fixed-fejer-stage-point-observed-same-source-restart-ready-v1"
    },
    {
      "key": "parameter_mode",
      "existed": true,
      "before": "independent-original-reference",
      "after": "same-source-complete-observed-report-and-final"
    },
    {
      "key": "scope",
      "existed": true,
      "before": "Independent full solve of the same predeclared Fejer target from its exact frozen reference point; all original peer history obligations and the actual run12 peer are explicit, without inventing any unreturned typed row or parent final. All original variables, 32 stages, sixjets and numerical budgets remain. Stage requests use the immutable owner; complete entry and exit point reads and all other guards remain. No measured acceleration is claimed. Existing statistics/geometry/decision scalar observations are published at their own actual points without new F/J/root calls.",
      "after": "Strict same-source continuation from a genuinely returned complete 8dc9/c9ce observed report and its matching final.npz, in the same still-available runner input/history/source context. All free variable words, complete permanent typed/protected history and inherited unknown-peer origin are retained. The original complete field, 32 stages, numerical parameters and direction budgets are reread from that point; old Phi, final damping, QP/root/cache states and feasibility are not substituted. Partial reports, accepted-only checkpoints and mutable progress are not eligible. This plan is prepared, not queued or executed; a usable platform/admission time window and a future complete return are not claimed."
    },
    {
      "key": "complete_parent_parameter_file",
      "existed": true,
      "before": {
        "name": "fixed-fejer-stage-point-independent-complete-ready.json",
        "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-stage-point-independent-complete-ready.json",
        "bytes": 99934,
        "sha256": "db456635a1811b993398d8ade8276ab753e63a2ac13ea878d27b98d313ef4b39",
        "git_blob_sha": "87b735efa8f879ded64cac07e878b41a6385834f"
      },
      "after": {
        "name": "fixed-fejer-stage-point-observed-independent-complete-ready.json",
        "path": "topics/visible-flex-larger-amplitude/computations/fixed-fejer-stage-point-observed-independent-complete-ready.json",
        "bytes": 97225,
        "sha256": "86d39c01d5a93c5a4d897a02d79bddd23a9b98daa6d6fae6940cc5d348da92f6",
        "git_blob_sha": "03daa9af5617879a6fea591a2a2d6dfe78e78836"
      }
    },
    {
      "key": "parameter_contract",
      "existed": true,
      "before": {
        "original_complete_science_and_pure_argv_values_and_order_retained": true,
        "only_script_output_paths_and_scalar_observation_sources_changed": true,
        "original_398_and385_scalar_selector_pairs_retained": true,
        "new_observer_summary_scalars_per_step": 10,
        "original_48_progress_mapping_preserved_in_complete_correspondence": true,
        "original_48_live_mapping_unchanged_claimed": false,
        "current_live_original_normal_fields": 18,
        "current_live_mathematical_fields": 30,
        "current_total_live_fields": 48,
        "all_original_normal_progress_scalar_values_captured_in_full_report_and_readout": true,
        "actual_unknown_parent_and_history_responsibilities_retained": true,
        "no_F_J_or_root_computation_added": true,
        "no_numerical_budget_or_acceptance_change": true
      },
      "after": {
        "original_complete_science_and_pure_argv_values_and_order_retained": false,
        "only_script_output_paths_and_scalar_observation_sources_changed": false,
        "original_398_and385_scalar_selector_pairs_retained": true,
        "new_observer_summary_scalars_per_step": 10,
        "original_48_progress_mapping_preserved_in_complete_correspondence": true,
        "original_48_live_mapping_unchanged_claimed": false,
        "current_live_original_normal_fields": 18,
        "current_live_mathematical_fields": 30,
        "current_total_live_fields": 48,
        "all_original_normal_progress_scalar_values_captured_in_full_report_and_readout": true,
        "actual_unknown_parent_and_history_responsibilities_retained": true,
        "no_F_J_or_root_computation_added": true,
        "no_numerical_budget_or_acceptance_change": true,
        "all_original_numeric_option_words_and_order_retained": true,
        "all_original_scripts_sources_120_roles_and_selector_values_retained": true,
        "only_existing_restart_mode_paths_and_inherited_pending_cli_representation_changed": true,
        "new_scientific_source_or_interface_added": false
      }
    },
    {
      "key": "inherited_pending_parallel_sources",
      "existed": false,
      "before": null,
      "after": [
        {
          "run_attempt": "45909290354/1",
          "driver_sha256": "cc0a07369a2d9ea5e22d261441420acb4e486a8c0d43f29f57e03378e82627b5"
        },
        {
          "run_attempt": "45929088658/1",
          "driver_sha256": "95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9"
        },
        {
          "run_attempt": "45943410994/1",
          "driver_sha256": "ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5"
        },
        {
          "run_attempt": "45972294636/1",
          "driver_sha256": "c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1"
        },
        {
          "run_attempt": "46011377225/1",
          "driver_sha256": "477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd"
        }
      ]
    },
    {
      "key": "same_source_restart_contract",
      "existed": false,
      "before": null,
      "after": {
        "actual_origin_run_id": 46037017666,
        "actual_origin_run_attempt": 1,
        "parent_report": "{work}/fixed-fejer-stage-point-observed-independent/report.json",
        "parent_checkpoint": "{work}/fixed-fejer-stage-point-observed-independent/final.npz",
        "parent_report_schema": "complete-fixed-fejer-stage-point-observed-material-envelope-SO3-QP-v1",
        "parent_driver_sha256": "8dc9d876f28ef78cc5c80279136af6f1391d3591598cdfecbcecc91aa3582a6d",
        "parent_reader_sha256": "c9ce27c75ab2b384642d3ccbf83f323bf018a63bfbd31a3364fd3c5e3707653f",
        "parent_required_complete": true,
        "parent_whole_report_sha256": null,
        "parent_whole_checkpoint_sha256": null,
        "actual_parent_model_identity_sha256": null,
        "actual_parent_full_point_sha256": null,
        "complete_is_not_feasibility": true,
        "inner_QP_iteration_limit_is_not_outer_completion": true,
        "pending_inherited_from": "material_envelope_transfer.independent_branch_origin",
        "partial_or_accepted_only_checkpoint_supported": false,
        "same_runner_files_and_source_paths_must_remain_readable": true,
        "admission_and_platform_time_window_verified": false,
        "restart_preserves_variables_and_history_but_recomputes_baseline": true,
        "prior_adaptive_damping_QP_root_or_cache_state_restored": false
      }
    }
  ],
  "removed_original_mode_suffix": [
    "--independent-envelope-branch",
    "--pending-parallel-envelope-run",
    "45909290354/1",
    "--pending-parallel-envelope-source",
    "45909290354/1=cc0a07369a2d9ea5e22d261441420acb4e486a8c0d43f29f57e03378e82627b5",
    "--pending-parallel-envelope-run",
    "45929088658/1",
    "--pending-parallel-envelope-source",
    "45929088658/1=95559b0cd44e3bf521b01ca8fe35b515bf7aad5dc4dc6b008ab0d015b9211da9",
    "--pending-parallel-envelope-run",
    "45943410994/1",
    "--pending-parallel-envelope-source",
    "45943410994/1=ff5444af4c31869a1a4d7b87cb4912f2d025b8da5ee90922924c3542ff6f0dd5",
    "--pending-parallel-envelope-run",
    "45972294636/1",
    "--pending-parallel-envelope-source",
    "45972294636/1=c3dc77f40445eaf30ab743311dd97ea7d62a41be80db504fc778eccffa30e5d1",
    "--pending-parallel-envelope-run",
    "46011377225/1",
    "--pending-parallel-envelope-source",
    "46011377225/1=477499b17141d8ae22558156e8b85a4c01b7a40ff07b6b46f5827e20d11b9ccd"
  ],
  "original_step_parent_bundles": [
    "fixed-fejer-reference/reference.npz",
    "fixed-fejer-reference/reference.npz"
  ],
  "original_science_scope": "Independent full solve of the same predeclared Fejer target from its exact frozen reference point; all original peer history obligations and the actual run12 peer are explicit, without inventing any unreturned typed row or parent final. All original variables, 32 stages, sixjets and numerical budgets remain. Stage requests use the immutable owner; complete entry and exit point reads and all other guards remain. No measured acceleration is claimed. Existing statistics/geometry/decision scalar observations are published at their own actual points without new F/J/root calls.",
  "new_science_scope": "Strict same-source continuation from a genuinely returned complete 8dc9/c9ce observed report and its matching final.npz, in the same still-available runner input/history/source context. All free variable words, complete permanent typed/protected history and inherited unknown-peer origin are retained. The original complete field, 32 stages, numerical parameters and direction budgets are reread from that point; old Phi, final damping, QP/root/cache states and feasibility are not substituted. Partial reports, accepted-only checkpoints and mutable progress are not eligible. This plan is prepared, not queued or executed; a usable platform/admission time window and a future complete return are not claimed.",
  "restart_suffix": [
    "--restart-report",
    "{work}/fixed-fejer-stage-point-observed-independent/report.json",
    "--restart-checkpoint",
    "{work}/fixed-fejer-stage-point-observed-independent/final.npz"
  ],
  "source_script_pairs": [
    "topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_fixed_fejer_stage_point_observed_actions.py",
    "topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_fixed_fejer_stage_point_observed_so3_report.py"
  ],
  "science_argv_words_before": 157,
  "science_argv_words_after": 140,
  "pure_argv_words": 7,
  "all_complete_source_role_count": 120,
  "summary_counts": [
    408,
    395
  ],
  "progress_count": 48
}''')


def encode(value):
    return (json.dumps(value, ensure_ascii=False, allow_nan=False,
                       separators=(",", ":")) + "\n").encode("utf-8")


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def require_bytes(raw, record):
    if len(raw) != record["bytes"] or digest(raw) != record["sha256"]:
        raise ValueError("The complete parameter input/output bytes changed")
    if len(raw) >= 100000:
        raise ValueError("Keep every complete deliverable below 100000 bytes")


def rename(value, old, new):
    if isinstance(value, str):
        return value.replace(old, new)
    if isinstance(value, list):
        return [rename(item, old, new) for item in value]
    if isinstance(value, dict):
        result = {}
        for key, item in value.items():
            changed = key.replace(old, new)
            if changed in result:
                raise ValueError("A path-key replacement must not merge objects")
            result[changed] = rename(item, old, new)
        return result
    return value


def selectors(step):
    return [list(mapping.items()) for mapping in step["summary"].values()]


def check_correspondence(original, result):
    if (len(original["steps"]) != 2 or len(result["steps"]) != 2
            or original["all_complete_source_role_count"] != 120
            or result["all_complete_source_role_count"] != 120):
        raise ValueError("Retain two whole steps and the whole 120-role source closure")
    for key in ("complete_unchanged_scientific_source_closure",
                "complete_new_runtime_sources", "source_reproducer",
                "complete_display_correspondence"):
        if original[key] != result[key]:
            raise ValueError("No scientific source or complete display origin changes")
    suffix = DATA["removed_original_mode_suffix"]
    prefix = original["steps"][0]["args"][:-len(suffix)]
    expected = rename(prefix, DATA["old_base"], DATA["new_base"]) + DATA["restart_suffix"]
    if (original["steps"][0]["args"][-len(suffix):] != suffix
            or result["steps"][0]["args"] != expected
            or len(original["steps"][0]["args"]) != 157
            or len(result["steps"][0]["args"]) != 140):
        raise ValueError("Keep every original non-mode argument word in original order")
    pending = []
    position = 1
    if suffix[0] != "--independent-envelope-branch":
        raise ValueError("The original complete independent-mode declaration changed")
    while position < len(suffix):
        run_flag, run, source_flag, source = suffix[position:position + 4]
        if (run_flag != "--pending-parallel-envelope-run"
                or source_flag != "--pending-parallel-envelope-source"
                or not source.startswith(run + "=")):
            raise ValueError("Retain every original ordered run/source pending pair")
        pending.append(dict(run_attempt=run, driver_sha256=source[len(run) + 1:]))
        position += 4
    if result["inherited_pending_parallel_sources"] != pending:
        raise ValueError("The exact original five unknown-peer objects must remain")
    for ordinal, (before, after) in enumerate(zip(original["steps"], result["steps"])):
        if before["script"] != after["script"] or after["script"] != DATA["source_script_pairs"][ordinal]:
            raise ValueError("The original launcher and pure reader scripts are unchanged")
        if selectors(before) != selectors(after):
            raise ValueError("Keep every summary label and selector value in order")
        count = sum(len(item) for item in before["summary"].values())
        if count != DATA["summary_counts"][ordinal]:
            raise ValueError("Keep all 408 science and 395 pure selectors")
    if (result["steps"][1]["args"] != rename(original["steps"][1]["args"],
                                             DATA["old_base"], DATA["new_base"])
            or len(result["steps"][1]["args"]) != 7):
        raise ValueError("Keep the complete original seven pure arguments")
    first, second = original["steps"][0], result["steps"][0]
    if (list(first["progress_summary"].values()) != list(second["progress_summary"].values())
            or sum(len(item) for item in second["progress_summary"].values()) != 48):
        raise ValueError("Keep all 48 actual progress selectors; only directory keys change")
    if (rename(first["cleanup_generated_patterns"], DATA["old_base"], DATA["new_base"])
            != second["cleanup_generated_patterns"]
            or first["retain_fixed_reference_cache_for_same_field_diagnostics"]
            != second["retain_fixed_reference_cache_for_same_field_diagnostics"]):
        raise ValueError("Keep the complete original cleanup/cache-retention rules")
    for key in ("actual_run_id", "actual_parent_report_sha256",
                "actual_parent_checkpoint_sha256", "actual_model_identity_sha256",
                "actual_current_point_sha256", "actual_accepted_or_complete_result"):
        if original[key] is not None or result[key] is not None:
            raise ValueError("Do not prefill a future actual complete field or restart result")


def forward(original):
    result = copy.deepcopy(original)
    for change in DATA["top_changes"]:
        key = change["key"]
        if change["existed"]:
            if key not in result or result[key] != change["before"]:
                raise ValueError("The pinned complete original top-level value changed")
        elif key in result:
            raise ValueError("A new metadata key already exists in the original")
        result[key] = copy.deepcopy(change["after"])
    result["steps"] = rename(result["steps"], DATA["old_base"], DATA["new_base"])
    suffix = DATA["removed_original_mode_suffix"]
    if original["steps"][0]["args"][-len(suffix):] != suffix:
        raise ValueError("The complete original mode suffix is not the pinned suffix")
    prefix = original["steps"][0]["args"][:-len(suffix)]
    result["steps"][0]["args"] = (rename(prefix, DATA["old_base"], DATA["new_base"])
                                  + copy.deepcopy(DATA["restart_suffix"]))
    result["steps"][0]["scope"] = DATA["new_science_scope"]
    for step in result["steps"]:
        step["parent_bundle"] = DATA["old_base"] + "/final.npz"
    check_correspondence(original, result)
    return result


def inverse(result):
    original = copy.deepcopy(result)
    if result["steps"][0]["args"][-4:] != DATA["restart_suffix"]:
        raise ValueError("The restart inputs changed from the complete declared pair")
    original["steps"][0]["args"] = original["steps"][0]["args"][:-4]
    original["steps"] = rename(original["steps"], DATA["new_base"], DATA["old_base"])
    original["steps"][0]["args"] += copy.deepcopy(DATA["removed_original_mode_suffix"])
    original["steps"][0]["scope"] = DATA["original_science_scope"]
    for ordinal, step in enumerate(original["steps"]):
        step["parent_bundle"] = DATA["original_step_parent_bundles"][ordinal]
    for change in DATA["top_changes"]:
        key = change["key"]
        if key not in original or original[key] != change["after"]:
            raise ValueError("The entire derived top-level value changed")
        if change["existed"]:
            original[key] = copy.deepcopy(change["before"])
        else:
            del original[key]
    check_correspondence(original, result)
    return original


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--direction", choices=("forward", "inverse"), default="forward")
    args = parser.parse_args()
    input_path, output_path = args.input.resolve(), args.output.resolve()
    if input_path == output_path:
        raise ValueError("Construct the other complete file without replacing its input")
    raw = input_path.read_bytes()
    expected_input = DATA["parent" if args.direction == "forward" else "output"]
    expected_output = DATA["output" if args.direction == "forward" else "parent"]
    require_bytes(raw, expected_input)
    value = json.loads(raw)
    if encode(value) != raw:
        raise ValueError("Retain the exact whole compact UTF-8 JSON encoding")
    operation, undo = ((forward, inverse) if args.direction == "forward"
                       else (inverse, forward))
    result = operation(value)
    produced = encode(result)
    require_bytes(produced, expected_output)
    if encode(undo(result)) != raw:
        raise ValueError("The complete inverse must recover the original bytes exactly")
    if output_path.exists() and output_path.read_bytes() != produced:
        raise ValueError("Do not overwrite a different complete parameter artifact")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(produced)
    print(json.dumps(dict(direction=args.direction, output=str(output_path),
                          bytes=len(produced), sha256=digest(produced),
                          science_executed=False), sort_keys=True))


if __name__ == "__main__":
    main()
