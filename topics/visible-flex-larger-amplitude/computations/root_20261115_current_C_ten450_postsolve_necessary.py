#!/usr/bin/env python3
"""One necessary <=90KB original postsolve conclusion, no raw/table transport.

Only standard-library file/JSON/process metadata is read here. No scientific
module is imported and no number is recomputed. Large ledgers, all radial
nodes, enclosures and full pair frontiers retain their original identities
and explicit unread-body scope. Missing keys remain distinguishable from
recorded null. No raw is deleted, uploaded, split or encoded for transport.
Author: AI, 2026-11-15.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import traceback

REPO = "Rogerhu12/math-research-public"
SCHEMA = "current-C-ten450-postsolve-one-necessary-conclusion-v1"
PROCEDURE_SCHEMA = "current-C-ten450-same-job-postsolve-complete-geometry-v1"
PROCEDURE_NAME = "geometry_20261115_current_C_ten450_postsolve_geometry.py"
PROCEDURE_SHA = "84d0450f2f362138045c222f5a47162e030fd0be8b6c7a99c5d66c0e41da425a"
LIMIT = 90000
STDERR_EXCERPT_LIMIT = 8192
STAGES = ("radial_replay", "original_cuff_atlas", "shared_field", "metric", "reach")
STAGE_SCHEMA = {
    "radial_replay": "current-C-ten450-complete-radial-Cartesian-readout-v1",
    "original_cuff_atlas": "R413-current-C-original-cuff-target-atlas-binding-v1",
    "shared_field": "R409-current-C-ten450-shared-background-complete-field-v1",
    "metric": "R418-current-C-accurate-ten-complete-closed-relative-metric-v1",
    "reach": "R422-current-C-ten450-complete-closed-reach-cover-v1",
}
COMMON = ("schema", "source", "repository", "run_id", "source_commit", "completed",
          "resource_partial", "resource_stop", "resource_reason", "external_interruption",
          "external_signal", "error", "execution_error", "pending", "elapsed_seconds")
RADIAL = ("actual_stages", "actual_nodes", "completed_stages", "current_stage", "current_step",
          "total_nodes", "root_calls", "RK_calls", "complete", "checkpoint",
          "node_ledger", "stage_ledger", "new_root_and_RK_scientific_replay",
          "no_new_BVP_or_native_solve", "geometry_or_metric_acceptance_created",
          "actual_original_geometry_usage")
ATLAS = ("original_checkpoint", "construction", "generated_plan", "target_atlas",
         "original_cuff", "complete_current_target_identity_sha256",
         "original_complete_C_input_binding_sha256", "original_ten_parameter_words_retained",
         "marker_count", "exact_flat_cap_annulus", "local_cuff_target_twojet_compatibility",
         "unpaid", "scientific_solver_or_E_query_run", "new_actual_surface_or_BVP_acceptance",
         "full_target_atlas_paid", "original_field_acceptance_is_metadata_source_not_recomputed_certificate")
SHARED = ("checkpoint", "checkpoint_directory", "radial_replay", "plan_input", "payloads",
          "complete_prefix_definition_sha256", "normal_form_prefix_definition_sha256",
          "node_count", "angular", "coefficient_count", "background_nodes",
          "coefficient_records_completed", "node_identity_ledger",
          "all_shape_mean_Nyquist_and_full_twojets_retained",
          "real_shared_node_Hermite_geometry_defined",
          "finite_native_replay_not_certified_exact_continuous_C_trajectory",
          "target_metric_error_or_curvature_or_reach_or_embedding_or_held_certified",
          "display_mesh_or_complete_pair_enumeration_generated",
          "original_BVP_acceptance_replaced")
METRIC = ("complete_active_partition", "complete_active_relative_operator_bound",
          "complete_two_cap_relative_operator_identity",
          "complete_closed_relative_operator_bound_for_bound_accurate_target",
          "requested_eta_exact", "actual_field_binding_identity", "parameters",
          "counts", "members", "same_actual_C_target", "scope", "timer_scope")
REACH = ("stage", "input_binding", "members", "ledgers", "universe_counts",
         "unstarted_scope", "parameters", "accurate_family_embedding_and_reach_certified",
         "accurate_family_reach_lower", "K_times_tau", "curvature_radius_gate",
         "README_reach_fraction_paid", "original_K_and_tau_not_reselected",
         "original_native_or_BVP_acceptance_changed", "diameter",
         "remaining_original_responsibilities", "task_completed")
CURVATURE = ("all_original_closed_roots_accounted_for", "processed_original_roots",
             "planned_original_roots", "counts", "actual_cell_attempts",
             "full_closed_immersion_proved", "full_closed_K_proved", "K",
             "full_first_jet_path_envelopes", "whole_phase_curvature_paid",
             "original_K_not_reselected")
PAIRS = ("complete_root_rank_enumeration", "processed_root_pairs", "planned_root_pairs",
         "complete_pair_responsibility_paid", "all_space_phase_nodes_attempted",
         "counts", "by_family")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPO,
            "Read actual same-job public Actions metadata only")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=True, allow_nan=False) + "\n").encode("ascii")


def receipt(path):
    path = Path(path)
    size = 0
    h = hashlib.sha256()
    with path.open("rb") as stream:
        while block := stream.read(1048576):
            size += len(block)
            h.update(block)
    return dict(file=str(path), bytes=size, sha256=h.hexdigest())


def identity(value):
    raw = canonical(value)
    return dict(canonical_bytes=len(raw), canonical_sha256=sha(raw),
                canonical_serialization_not_original_member_bytes=True)


def original(path, expected=None):
    path = Path(path)
    raw = path.read_bytes()
    if expected is not None:
        require(sha(raw) == expected, "Actual file bytes changed: " + str(path))
    return json.loads(raw), dict(file=str(path), bytes=len(raw), sha256=sha(raw))


def within(path, root, exists=False):
    path = Path(path).resolve(strict=exists)
    root = Path(root).resolve(strict=True)
    require(path != root and path.is_relative_to(root),
            "Actual metadata must remain in its declared owned directory")
    return path


def selected(value, keys):
    require(isinstance(value, dict), "Select only an actual original JSON object")
    return dict(values={key: value[key] for key in keys if key in value},
                absent_keys=[key for key in keys if key not in value])


def proc_record(pid):
    try:
        values = (Path("/proc") / str(pid) / "stat").read_text().rsplit(")", 1)[1].split()
        return dict(pid=int(pid), state=values[0], pgid=int(values[2]),
                    sid=int(values[3]), start_ticks=values[19])
    except (FileNotFoundError, ProcessLookupError):
        return None


def same_process(left, right):
    return (isinstance(left, dict) and right is not None
            and left.get("pid") == right["pid"] and left.get("start_ticks") == right["start_ticks"])


def process_quiet(procedure):
    owner = procedure.get("actual_procedure_process")
    current = None if owner is None else proc_record(owner["pid"])
    live_owner = same_process(owner, current) and current["state"] != "Z"
    groups = []
    for row in procedure.get("stages", []):
        group = row.get("owned_process", {}).get("pid")
        if group is None:
            continue
        live = []
        for item in Path("/proc").iterdir():
            if item.name.isdigit():
                process = proc_record(int(item.name))
                if (process is not None and process["pgid"] == group and process["sid"] == group
                        and process["state"] != "Z"):
                    live.append(process)
        groups.append(dict(stage=row["name"], actual_owned_group=group,
                           still_live_group_members=live, quiescent=not live))
    return dict(procedure_process=owner, actual_matching_procedure_still_live=bool(live_owner),
                groups=groups,
                all_actual_owned_processes_quiet=not live_owner and all(r["quiescent"] for r in groups),
                no_process_signalled_by_reader=True)


def original_current(value):
    require(value.get("run_id") == os.environ["GITHUB_RUN_ID"]
            and value.get("source_commit") == os.environ["GITHUB_SHA"],
            "Keep this actual same-job source and run")


def excerpt(path, expected, root):
    if path is None:
        return dict(present=False)
    path = within(path, root, exists=True)
    record = receipt(path)
    require(record["sha256"] == expected["sha256"] and record["bytes"] == expected["bytes"],
            "Original child log changed before readback")
    count = min(STDERR_EXCERPT_LIMIT, record["bytes"])
    start = record["bytes"] - count
    with path.open("rb") as stream:
        stream.seek(start)
        data = stream.read(count)
    try:
        text = data.decode("utf-8")
        utf8 = True
    except UnicodeDecodeError:
        text = data.decode("utf-8", "replace")
        utf8 = False
    return dict(present=True, original_file=record, displayed_byte_range=[start, record["bytes"]],
                display_is_complete_original_bytes=start == 0 and utf8,
                valid_UTF8_for_displayed_range=utf8, text=text,
                invalid_UTF8_display_replacements_are_not_a_lossless_encoding=not utf8,
                omitted_prefix_bytes=start,
                full_error_table_or_stdout_not_inferred_from_this_excerpt=True,
                no_segmented_encoded_or_reconstructable_raw_transport=True)


def pending_projection(value, keys, frontier_keys=()):
    if value is None:
        return dict(present=True, original_value=None)
    result = selected(value, keys)
    result["original_complete_object_identity"] = identity(value)
    result["not_returned_fields"] = {}
    for key, original_value in value.items():
        if key not in keys:
            record = dict(identity=identity(original_value), body_not_returned=True)
            if isinstance(original_value, (list, dict)):
                record["metadata_item_count"] = len(original_value)
            result["not_returned_fields"][key] = record
    result["no_unvisited_responsibility_claimed_paid_from_identity"] = True
    return result


def project_result(name, value):
    result = selected(value, COMMON)
    result["complete_original_result_object_identity"] = identity(value)
    if name == "radial_replay":
        result["original_radial_fields"] = selected(value, RADIAL)
    elif name == "original_cuff_atlas":
        result["original_cuff_fields"] = selected(value, ATLAS)
    elif name == "shared_field":
        result["original_shared_fields"] = selected(value, SHARED)
        if "current_target_identity" in value:
            result["current_target_identity_only"] = identity(value["current_target_identity"])
    elif name == "metric":
        result["original_metric_fields"] = selected(value, METRIC)
    elif name == "reach":
        result["original_reach_fields"] = selected(value, REACH)
        curvature = value.get("curvature")
        pairs = value.get("pairs")
        result["curvature_present"] = "curvature" in value
        result["pairs_present"] = "pairs" in value
        if curvature is not None:
            result["original_curvature_fields"] = selected(curvature, CURVATURE)
            result["original_curvature_pending"] = pending_projection(
                curvature.get("pending"), (
                    "current_root_index", "unvisited_root_suffix", "terminal_unpaid_count",
                    "terminal_unpaid_addresses", "boundary_points_never_omitted"))
            if "meridian_path_envelope" in curvature:
                result["meridian_path_envelope_identity_only"] = identity(curvature["meridian_path_envelope"])
        if pairs is not None:
            result["original_pair_fields"] = selected(pairs, PAIRS)
            result["original_pair_pending"] = pending_projection(
                pairs.get("pending"), (
                    "current_unretired_root_pair", "unvisited_rank_suffix", "terminal_unpaid_leaves",
                    "terminal_unpaid_addresses", "no_unvisited_pair_or_same_point_product_discarded"))
    return result


def inspect_stage(row, root):
    out = dict(name=row["name"], actual_lifecycle=selected(row, (
        "started", "status", "unstarted_reason", "requested_stage_budget_seconds",
        "actual_science_budget_seconds", "actual_wall_allowance_seconds",
        "original_job_remaining_seconds_at_launch", "actual_child_exit", "elapsed_seconds",
        "resource_stop", "external_interruption", "error", "original_result_missing",
        "original_result_not_read_while_owner_active", "original_schema",
        "original_completed_flag", "original_resource_partial", "original_error",
        "metadata_read_error", "completed_original_plan_with_stdout_summary_overflow",
    )))
    out["owned_process_identity"] = identity(row.get("owned_process"))
    out["complete_original_lifecycle_identity"] = identity(row)
    if row.get("started") is not True:
        return out
    stderr = row.get("stderr")
    out["original_stderr"] = (
        dict(present=False) if stderr is None
        else excerpt(row["stderr_path"], stderr, root))
    stdout = row.get("stdout")
    if stdout is not None:
        path = within(row["stdout_path"], root, exists=True)
        actual = receipt(path)
        require(actual["sha256"] == stdout["sha256"] and actual["bytes"] == stdout["bytes"],
                "The original child stdout changed")
        out["original_stdout_identity_only"] = actual
        out["scientific_stdout_body_not_transported"] = True
    target = row.get("original_result")
    if target is None:
        out["actual_result_body_not_available_in_closed_procedure"] = True
        # A missing result has no synthetic successful default. Original error
        # and direct stderr remain above; all science outside them is unpaid.
        return out
    path = within(target["file"], root, exists=True)
    value, original = original_json_with_identity(path, target)
    original_current(value)
    require(value.get("schema") == STAGE_SCHEMA[row["name"]],
            "Keep the actual frozen consumer result schema")
    out["original_result"] = original
    out["necessary_original_values"] = project_result(row["name"], value)
    # Preserve complete source-level pending ranges without transporting the
    # entire geometric DFS tree. Exact cell bodies remain in original ledgers.
    if row["name"] == "metric":
        summary_path = path.parent / "summary.json"
        if summary_path.is_file():
            summary, sid = original_json_with_identity(summary_path)
            require(summary.get("result", {}).get("sha256") == original["sha256"],
                    "Original metric necessary-summary/result binding differs")
            out["original_consumer_summary_identity"] = sid
            out["original_metric_pending"] = pending_projection(
                summary.get("complete_pending_addresses"), (
                    "current_root_rank", "current_original_root", "untouched_root_rank_suffix",
                    "exact_split_algorithm_source_sha256", "complete_coverage_record",
                    "full_terminal_unresolved_cells",
                    "each_pending_cell_reconstructed_by_original_root_and_original_four_closed_splits",
                    "all_other_unfinished_roots_preserved_as_original_rank_suffix",
                    "whole_domain_unpaid_before_root_plan"))
        else:
            out["original_consumer_summary_missing"] = True
    return out


def original_json_with_identity(path, expected=None):
    digest = None if expected is None else expected["sha256"]
    value, record = original(path, digest)
    if expected is not None:
        require(record["bytes"] == expected["bytes"], "Actual member byte count differs")
    return value, record


def build(directory):
    root = Path(directory).resolve(strict=True)
    temporary = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    require(root != temporary and root.is_relative_to(temporary),
            "Read only this actual Actions temporary postsolve directory")
    procedure, pid = original(root / "procedure.json")
    require(procedure.get("schema") == PROCEDURE_SCHEMA
            and procedure.get("source", {}).get("sha256") == PROCEDURE_SHA,
            "The independent postsolve source identity differs")
    original_current(procedure)
    require(procedure.get("procedure_returned") is True,
            "The procedure has not completed its own finally/owner accounting")
    quiet = process_quiet(procedure)
    require(quiet["all_actual_owned_processes_quiet"] is True
            and procedure.get("all_owned_children_quiescent") is True,
            "Do not read mutable scientific files while their actual owner remains live")
    stages = procedure.get("stages")
    require(isinstance(stages, list) and [r.get("name") for r in stages] == list(STAGES),
            "Preserve all five actual stage rows and the complete unstarted suffix")
    input_record = procedure["input"]
    input_value, input_id = original(input_record["file"], input_record["sha256"])
    require(input_id["bytes"] == input_record["bytes"], "Original postsolve input bytes differ")
    outputs = []
    for row in stages:
        outputs.append(inspect_stage(row, root))
    # Rehash the producer journal after all necessary original-member reads.
    require(receipt(root / "procedure.json") == pid,
            "The closed producer record changed during necessary readback")
    value = dict(
        schema=SCHEMA, repository=REPO, run_id=os.environ["GITHUB_RUN_ID"],
        source_commit=os.environ["GITHUB_SHA"], source=receipt(__file__),
        procedure=pid, procedure_source=procedure["source"], input=input_id,
        necessary_readback_complete=True, raw_file_or_large_table_transport=False,
        actual_process_quiet_evidence=quiet,
        original_procedure=selected(procedure, (
            "started", "procedure_returned", "upstream_finite450_acceptance_observed",
            "upstream_acceptance_is_not_geometric_completion", "upstream_stop",
            "dependency_order", "reach_does_not_require_metric_success",
            "original_BVP_native_FD_RMS_BC_or_final_acceptance_changed",
            "new_threshold_or_scientific_gate_added", "held_rigidity_deltaE_executed",
            "on_demand_C_refinement_provider_executed", "global_clock_restarted",
            "error", "resource_stop", "external_interruption",
            "all_owned_children_quiescent", "raw_cleanup_performed",
            "cleanup_allowed", "complete_task_certified",
            "absolute_science_deadline_unix_seconds", "original_readback_reserve_seconds",
            "elapsed_seconds", "future_same_C_query_payloads_present",
            "actual_original_450_not_resolved_again", "unstarted_stage_names",
            "actual_metric_original_flags", "actual_reach_original_flags",
            "actual_held_deltaE_and_new_C_query_provider_not_executed",
        )),
        upstream_launch=procedure.get("upstream_launch"),
        original_inputs=procedure.get("inputs"),
        explicit_original_parameter_inputs=selected(input_value, ("construction", "metric", "reach", "resources")),
        stage_rows=outputs,
        direct_source_closure_identity=identity(procedure.get("source_pins")),
        selected_source_field_projection_not_a_per_value_audit_of_large_data=True,
        untouched_large_payload_scope=dict(
            radial_all226_nodes_all2048_root_samples_and_coefficients="original temporary files; identities/counts only",
            full_coverage_terminal_enclosure_and_pair_ledgers="original temporary files; identities/counts/necessary pending suffixes only",
            original_C_source_ledger_and_index="retained in same namespace until all actual consumers/readback; never reconstructed from SHA",
            native_field_resolved_or_J_recomputed_by_reader=False,
            future_R425_held_and_deltaE_or_R426_refinement_executed=False,
        ),
        postsolve_cleanup_readback_condition_paid=True,
        original_upstream_BVP_readback_condition_must_also_be_paid=True,
        cleanup_not_performed_by_this_reader=True,
        whole_task_or_unexecuted_geometric_responsibility_certified=False,
    )
    return value


def write_output(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = canonical(value)
    complete = value.get("necessary_readback_complete") is True
    if len(raw) > LIMIT:
        # One honest small failure; never split/encode the oversized object.
        value = dict(
            schema=SCHEMA + "-over-budget", necessary_readback_complete=False,
            requested_summary_bytes=len(raw), requested_summary_sha256=sha(raw),
            limit=LIMIT, actual_procedure=value.get("procedure"),
            original_run_id=os.environ.get("GITHUB_RUN_ID"),
            original_source_commit=os.environ.get("GITHUB_SHA"),
            postsolve_cleanup_readback_condition_paid=False,
            no_raw_upload_deletion_or_reconstructable_transport=True,
            scientific_success_or_failure_not_inferred=True,
            complete_task_certified=False,
        )
        raw = canonical(value)
        complete = False
    with path.open("wb") as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    print("BEGIN_CURRENT_C_TEN450_POSTSOLVE_NECESSARY", flush=True)
    print(raw.decode("ascii"), end="", flush=True)
    print("END_CURRENT_C_TEN450_POSTSOLVE_NECESSARY", flush=True)
    record = receipt(path)
    print(json.dumps(dict(event="current_ten450_postsolve_necessary_identity",
        original_summary=record, necessary_readback_complete=complete,
        whole_task_certified=False), separators=(",", ":")), flush=True)
    if os.environ.get("GITHUB_OUTPUT"):
        delimiter = "POSTSOLVE_" + sha(raw)
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="ascii") as stream:
            stream.write("postsolve_summary<<" + delimiter + "\n" + raw.decode("ascii") + delimiter + "\n")
            stream.write("postsolve_summary_bytes=" + str(len(raw)) + "\n")
            stream.write("postsolve_summary_sha256=" + sha(raw) + "\n")
            stream.write("postsolve_readback_complete=" + ("true" if complete else "false") + "\n")
    return 0 if complete else 70


def main(argv=None):
    actions()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)
    temporary = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    output = within(args.out, temporary)
    require(not output.exists(), "Do not replace an existing necessary readback")
    try:
        value = build(args.directory)
    except BaseException as error:
        value = dict(schema=SCHEMA, repository=REPO,
            run_id=os.environ.get("GITHUB_RUN_ID"), source_commit=os.environ.get("GITHUB_SHA"),
            source=receipt(__file__), necessary_readback_complete=False,
            metadata_error=dict(type=type(error).__name__, message=str(error),
                                traceback=traceback.format_exc()),
            postsolve_cleanup_readback_condition_paid=False,
            scientific_result_not_inferred_from_metadata_error=True,
            whole_task_or_unexecuted_geometric_responsibility_certified=False,
            raw_not_deleted_or_uploaded=True)
    return write_output(output, value)


if __name__ == "__main__":
    raise SystemExit(main())
