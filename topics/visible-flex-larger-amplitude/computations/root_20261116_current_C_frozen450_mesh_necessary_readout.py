#!/usr/bin/env python3
"""R431 one necessary original mesh/full450 readback after observed quiescence.

This standard-library reader imports pinned metadata-only helpers, never a
scientific module. It parses actual originals and selects one <=90000-byte
conclusion. Complete arrays, old native trials and success-factor tables are
identified, not encoded, split, or claimed fully returned. It never deletes.
Author: ChatGPT /root/amplitude (AI), 2026-11-16.
"""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys

REPO = "Rogerhu12/math-research-public"
SCHEMA = "current-C-frozen450-mesh-one-necessary-readback-v1"
LAUNCH_SCHEMA = "current-C-continuous-ten-frozen450-mesh-owned-launch-v1"
DRIVER_SCHEMA = "current-C-continuous-ten-frozen450-nested-mesh-original-full-DN-v1"
LAUNCH = "geometry_20261116_current_C_frozen450_mesh_owned_launch.py"
LAUNCH_SHA = "4375375b343bc2e3b359a2e1ca566bb6648e08b691d7208cced348f185272868"
DRIVER = "geometry_20261115_continuous_ten_frozen450_mesh_refinement.py"
DRIVER_SHA = "70a5709d6bca4bf124a029ebcc33fae31407c3214c5164a867a8de9f37d53928"
LIFECYCLE = "geometry_20261115_current_C_ten450_postsolve_geometry.py"
LIFECYCLE_SHA = "84d0450f2f362138045c222f5a47162e030fd0be8b6c7a99c5d66c0e41da425a"
PHASE_READER = "root_20261115_continuous_ten_two_phase_necessary_readout.py"
PHASE_READER_SHA = "622f4f3c8255a4980e931457f912cca1ee00d25af965da18f39aecc6860c8d72"
BASE_READER = "root_20261115_current_C_pruefer_positive_full453_necessary_readout.py"
BASE_READER_SHA = "34b49f026338b90b691cbd170d6d6303c7ec3549f2329ba0f4457a2cfeab75c9"
PINS = {LAUNCH: LAUNCH_SHA, DRIVER: DRIVER_SHA, LIFECYCLE: LIFECYCLE_SHA,
        PHASE_READER: PHASE_READER_SHA, BASE_READER: BASE_READER_SHA}
LIMIT = 90000
LAUNCH_KEYS = ("schema", "source", "repository", "run_id", "source_commit", "input", "phase",
    "resources", "requested_max_nodes", "driver", "driver_output_directory", "band_factor_directory",
    "actual_child_process_started", "actual_child_exit", "launcher_returned", "launcher_exit_code",
    "completed_driver_return", "upstream_original450_accepted", "actual_parent450_accepted",
    "current_refined450_accepted", "actual_adapter_status", "actual_refined_checkpoint",
    "actual_refined_checkpoint_directory", "owned_group_quiescent_before_readback",
    "upstream_stop", "resource_stop", "external_interruption", "error", "shutdown_error",
    "original_global_clock_restarted", "original_numeric_policy_changed",
    "actual_parent_arrays_used_as_initial_guess_not_new_acceptance", "new_scientific_gate_added",
    "mesh_convergence_or_closed_geometry_certified", "origin_launch", "actual_job_deadline",
    "original_deadline_values", "original_193_recipe", "absolute_science_deadline_unix_seconds",
    "original_readback_reserve_seconds", "origin_adapter_status", "origin_checkpoint", "parent_kind",
    "parent_launch", "parent_adapter_status", "actual_parent_checkpoint", "actual_parent_checkpoint_directory",
    "actual_parent_ten_float64le", "actual_parent_ten_exact_dyadics", "same_target_identity_sha256",
    "actual_mesh_recipe", "original_numeric_policy", "actual_inputs", "actual_remaining_science_seconds_before_mesh",
    "actual_mesh_process_budget_seconds", "actual_start_free_bytes", "latest_observed_free_bytes",
    "stdout", "stderr", "adapter_status_absent", "no_scientific_scope_inferred_from_missing_status",
    "actual_adapter_scope", "actual_refined_ten_float64le", "actual_refined_ten_exact_dyadics",
    "actual_new_checkpoint_source", "actual_new_original_acceptance",
    "all_original_phase_science_unstarted", "new_refinement_not_started_because_real_parent_unavailable",
    "mutable_driver_tree_not_read_until_observed_quiet", "elapsed_seconds")
SESSION_KEYS = ("schema", "source_sha256", "repository", "run_id", "source_commit", "phase", "success",
    "actual_refined450_accepted", "new_coupled_finite_acceptance",
    "exact_continuous_target_or_C2_metric_or_closed_surface_certified", "recipe", "input_sha256",
    "original_native_policy", "original_phase_policy", "resources", "phases", "actual_parent",
    "parent_field_must_be_a_real_current_job_checkpoint", "large_results_owned_temporary_only",
    "complete_necessary_reader_still_required_before_cleanup", "resource_partial", "resource_reason",
    "original_new_current_H_FD_and_fullDN_unstarted", "no_nonlinear_failure_or_new_acceptance_inferred",
    "unvisited_phase_suffix", "actual_final_checkpoint", "actual_final_checkpoint_directory",
    "same_ten_target_identity_verified_by_original_writer",
    "mesh_or_spectral_convergence_or_closed_geometry_certified", "exception", "traceback",
    "native_close_exception", "native_owner_close_attempted", "native_owner_closed",
    "native_owner_close_exception", "all_phase_leases_released")
PLAN_KEYS = ("schema", "parent_checkpoint", "parent_fullDN", "parent_mesh_nodes",
    "representable_source_midpoints", "literal_numeric_knot_count", "nested_mesh_nodes",
    "maximum_declared_nodes", "ordinary_exact_midpoint_union_count_without_duplicate_knots",
    "actual_duplicate_or_machine_unrepresentable_nodes_not_counted_twice",
    "original_mesh_float64le_sha256", "nested_mesh_float64le_sha256",
    "original_nodes_retained_with_identical_words", "all_literal_numeric_knots_present_by_value",
    "original_knot_words_not_overwritten_to_change_the_profile",
    "same_original_public_u_and_finite_s_coordinate", "numerical_mesh_refinement_only",
    "spectral_modes_quadrature_native_RK_or_tailsteps_changed",
    "parent_acceptance_is_only_source_provenance_not_new_acceptance",
    "original_complete_preflight_returned", "final_seed_mesh_nodes", "preflight_added_nodes",
    "every450_RHS_row_evaluated_fresh_before_original_preflight",
    "parent_RHS_used_only_to_define_the_initial_interpolant",
    "all_original_physical338_core112_seed_words_retained",
    "original_full_current_H_FD_fullDN_final_J_and_audit_still_required", "new_accepted_field_created")


def require(value, message):
    if not value:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True,
                       allow_nan=False) + "\n").encode("ascii")


def imported(comp, name, digest, alias):
    path = comp / name
    require(sha(path.read_bytes()) == digest, "Frozen metadata source differs: " + name)
    spec = importlib.util.spec_from_file_location(alias, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[alias] = module
    try:
        spec.loader.exec_module(module)
    except BaseException:
        sys.modules.pop(alias, None)
        raise
    return module


def fields(L, value, keys):
    return None if not isinstance(value, dict) else {
        key: L.small(value[key], (key,)) for key in keys if key in value}


def member(value):
    raw = canonical(value)
    result = dict(canonical_bytes=len(raw), canonical_sha256=sha(raw))
    if isinstance(value, (list, dict)):
        result["members"] = len(value)
    return result


def current(value):
    require(value.get("repository") == REPO
            and str(value.get("run_id")) == os.environ["GITHUB_RUN_ID"]
            and value.get("source_commit") == os.environ["GITHUB_SHA"],
            "Read only this actual immutable run identity")


def quiescence(H, launch):
    record = dict(launcher_returned=launch.get("launcher_returned") is True,
        original_owned_group_quiescent=launch.get("owned_group_quiescent_before_readback") is True,
        observed_active_matching_processes=[], actual_child_group_members=[], errors=[],
        no_signals_or_process_mutation_performed=True)
    leader = launch.get("actual_launcher_process")
    if not isinstance(leader, dict):
        record["errors"].append("actual-launcher-process-identity-absent")
    else:
        now = H.proc_record(leader["pid"])
        if H.same_process(leader, now) and now["state"] != "Z":
            record["observed_active_matching_processes"].append(now)
    child = launch.get("observed_child")
    if launch.get("actual_child_process_started") is True:
        if not isinstance(child, dict):
            record["errors"].append("actual-started-child-identity-absent")
        else:
            for old in child.get("observed_processes", []):
                now = H.proc_record(old["pid"])
                if H.same_process(old, now) and now["state"] != "Z":
                    record["observed_active_matching_processes"].append(now)
            record["actual_child_group_members"] = [r for r in H.group_rows(child["pid"]) if r["state"] != "Z"]
            record["original_child_identity_conflicts"] = child.get("identity_conflicts", [])
            if child.get("identity_conflicts"):
                record["errors"].append("original-child-identity-conflict")
            if child.get("actual_child_returncode") is None:
                record["errors"].append("actual-child-return-unreaped-or-unknown")
            record["original_complete_child_owner_record_identity"] = member(child)
    record["observed_quiet"] = bool(record["launcher_returned"]
        and record["original_owned_group_quiescent"]
        and not record["observed_active_matching_processes"]
        and not record["actual_child_group_members"] and not record["errors"])
    return record


def plan_view(L, path):
    value, identity = L.document(path, "R427-original-mesh-plan")
    if value is None:
        return dict(file=str(path), available=False, original_identity=identity,
                    no_plan_or_new_mesh_inferred=True)
    selected = fields(L, value, PLAN_KEYS)
    for key in ("literal_numeric_knots_float64le", "current_target_identity"):
        if key in value:
            selected[key + "_identity"] = member(value[key])
    intervals = value.get("machine_unrepresentable_midpoint_intervals")
    if intervals is not None:
        require(isinstance(intervals, list), "Original collapsed-midpoint list required")
        selected["machine_unrepresentable_midpoint_count"] = len(intervals)
        selected["complete_machine_unrepresentable_midpoint_list_identity"] = member(intervals)
        selected["first_and_last_original_machine_unrepresentable_midpoint"] = (
            [] if not intervals else [intervals[0]] if len(intervals) == 1 else [intervals[0], intervals[-1]])
        selected["other_collapsed_midpoint_records_parsed_but_not_exported"] = len(intervals) > 2
    return dict(file=str(path), original_identity=identity, original_selected_values=selected,
                no_scientific_mesh_arithmetic_performed_by_reader=True)


def necessary_native(A, L, directory):
    full = A.native_view(L, directory)
    if full.get("actual_live_client_directory_exists") is not True:
        return full
    # A already parses all actual native trial/trace and linear-child records.
    # Select each call's original scalars, and one complete last-call detail.
    columns = full.get("native_columns", [])
    rows = full.get("all_actual_native_calls", [])
    keep = ("directory", "call", "normalizedResidual", "converged", "current_native_completed",
            "last_withJ_norm", "audit", "predicted", "actual_nonlinear_solve", "minA", "minD",
            "history_count", "trial_count", "last_iteration", "error")
    require(all(name in columns for name in keep), "Pinned original native scalar table layout differs")
    positions = [columns.index(key) for key in keep]
    for row in rows:
        require(len(row) == len(columns), "Every original native table row must keep its declared layout")
    details = full.get("all_actual_call_last_iteration_trials_and_scopes", [])
    require(len(details) == len(rows), "Actual native call/detail address counts differ")
    failures = []
    ci, ni, ei = (columns.index(key) for key in ("converged", "current_native_completed", "error"))
    for index, (row, detail) in enumerate(zip(rows, details)):
        if row[ci] is not True or row[ni] is not True or row[ei] is not None:
            failures.append(dict(original_call_index=index, directory=row[columns.index("directory")],
                selected_original_failure_scope=fields(L, detail, (
                    "last_baseline", "last_actual_iteration", "original_request_scope",
                    "original_request_failure", "actual_checkpoint_scope", "response_scope")),
                complete_original_detail_identity=member(detail)))
    result = {key: value for key, value in full.items() if key not in (
        "native_columns", "all_actual_native_calls", "all_actual_call_last_iteration_trials_and_scopes")}
    result.update(native_columns=list(keep), all_actual_native_call_scalar_rows=[
        [row[i] for i in positions] for row in rows],
        all_original_native_call_rows_identity=member(rows),
        complete_original_call_detail_list_identity=member(details),
        all_failed_or_not_completed_actual_call_scopes=failures,
        last_actual_call_original_detail=None if not details else details[-1],
        every_present_original_native_call_scalar_row_selected=True,
        earlier_last_iteration_trials_are_identity_only_not_claimed_returned=True,
        large_state_J_success_factor_and_full_stream_content_identity_only=True)
    return result


def output(summary, out):
    raw = canonical(summary)
    require(len(raw) <= LIMIT, "Internal output caller must keep one necessary <=90000-byte summary")
    path = out / "scalar-summary.json"
    with path.open("wb") as stream:
        stream.write(raw); stream.flush(); os.fsync(stream.fileno())
    print("BEGIN_R431_FROZEN450_MESH_NECESSARY", flush=True)
    print(raw.decode("ascii"), end="", flush=True)
    print("END_R431_FROZEN450_MESH_NECESSARY", flush=True)
    identity = dict(bytes=len(raw), sha256=sha(raw))
    print(json.dumps(dict(event="R431_necessary_summary_identity", **identity,
                         hash_scope="canonical ASCII JSON including LF")), flush=True)
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as stream:
            stream.write("mesh_summary=" + raw.decode("ascii").rstrip("\n") + "\n")
            stream.write("mesh_summary_bytes=" + str(len(raw)) + "\n")
            stream.write("mesh_summary_sha256=" + sha(raw) + "\n")
    return identity


def main(argv=None):
    require(os.environ.get("GITHUB_ACTIONS") == "true" and os.environ.get("GITHUB_REPOSITORY") == REPO,
            "Necessary original mesh readback belongs to this public Actions repository")
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("namespace", "launch-directory", "computations", "out"):
        parser.add_argument("--" + name, type=Path, required=True)
    for name in ("entry-stdout", "entry-stderr"):
        parser.add_argument("--" + name, type=Path)
    args = parser.parse_args(argv)
    tmp = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    namespace = args.namespace.resolve(strict=True)
    require(tmp in namespace.parents and not args.namespace.is_symlink(), "Actual owned namespace required")
    root, comp, out = args.launch_directory.resolve(), args.computations.resolve(strict=True), args.out.resolve()
    for path in (root, out):
        require(namespace in path.parents and path != namespace, "Owned namespace child required")
    require(not out.exists() and not out.is_relative_to(root) and not root.is_relative_to(out),
            "Use one fresh sibling necessary-readback directory")
    out.mkdir(parents=True)
    H = imported(comp, LIFECYCLE, LIFECYCLE_SHA, "_R431_reader_owned_metadata")
    A = imported(comp, PHASE_READER, PHASE_READER_SHA, "_R431_original_phase_metadata")
    L = A.load_reader(comp)
    pins = {}
    for name, expected in PINS.items():
        item = L.identity(comp / name)
        require(item["sha256"] == expected, "The actual independent source differs: " + name)
        pins[name] = item
    launch, lid = L.document(root / "result.json", "R431-actual-launch", required=True)
    summary = dict(schema=SCHEMA, repository=REPO, run_id=os.environ["GITHUB_RUN_ID"],
        source_commit=os.environ["GITHUB_SHA"], source=L.identity(__file__), source_pins=pins,
        original_launch_identity=lid, original_launch_selected=fields(L, launch, LAUNCH_KEYS),
        namespace=str(namespace), actual_launch_directory=str(root),
        complete_necessary_readback=False, no_scientific_arithmetic_or_scientific_import=True,
        no_new_field_acceptance_created=True, cleanup_performed=False,
        large_raw_or_matrix_transport_split_or_encoded=False)
    quiet = False
    if launch is not None:
        try:
            current(launch)
            require(launch.get("schema") == LAUNCH_SCHEMA
                    and launch.get("source", {}).get("sha256") == LAUNCH_SHA,
                    "Read this actual independent mesh launcher, not a renamed193 result")
            observed = quiescence(H, launch)
            summary["actual_quiescence_observation"] = observed
            quiet = observed["observed_quiet"]
            if not quiet:
                L.fail("quiescence", RuntimeError("Actual owner is live, unknown, or not returned"))
        except Exception as error:
            L.fail("launch-binding", error)
    if quiet:
        try:
            for key in ("stdout", "stderr"):
                path = root / ("mesh." + key + ".log")
                if path.is_file():
                    if key in launch:
                        require(H.same_payload(L.identity(path), launch[key]), "Actual original child log differs")
                    L.log_view(path, "R431-original-child-" + key)
            if launch.get("actual_mesh_recipe") is not None:
                recipe, rid = L.document(root / "actual-mesh-recipe.json", "R431-actual-mesh-recipe", True)
                require(recipe is not None and H.same_payload(rid, launch["actual_mesh_recipe"]),
                        "Actual generated mesh recipe differs from the launcher receipt")
                summary["actual_mesh_recipe"] = dict(identity=rid, complete_original_small_recipe=recipe)
            driver = root / "refined-BVP"
            state, sid = L.document(driver / "adapter-status.json", "R427-actual-adapter-state")
            if state is not None:
                current(state)
                require(state.get("schema") == DRIVER_SCHEMA and state.get("source_sha256") == DRIVER_SHA,
                        "The original actual R427 producer differs")
                if launch.get("actual_adapter_status") is not None:
                    require(H.same_payload(sid, launch["actual_adapter_status"]), "Mutable adapter receipt differs")
                summary["actual_mesh_state"] = dict(identity=sid, original_selected=fields(L, state, SESSION_KEYS))
                for key in ("consumed_source_sha256", "native_live_calls"):
                    if key in state:
                        summary["actual_" + key + "_identity"] = member(state[key])
                summary["native_call_ledger_count"] = len(state.get("native_live_calls", []))
                summary["stage_started_false_does_not_imply_no_seed_or_preflight_evaluation"] = True
            elif launch.get("actual_child_process_started") is True:
                summary["actual_adapter_absent_after_child"] = True
                summary["runtime_or_binding_error_scope_only_from_original_entry_logs"] = True
            else:
                summary["R427_scientific_child_not_started_by_actual_launcher"] = True
            phase = driver / "refined450"
            summary["original_refined450_outputs"] = A.phase_documents(L, phase)
            seed = phase / "initial-guess"
            summary["original_mesh_plans"] = [plan_view(L, seed / name) for name in (
                "nested-mesh-plan.json", "complete-nested-seed-binding.json")]
            first_H, first_id = L.document(phase / "actual-H-response" / "actual-first-height-input.json",
                                           "R427-original-first-height")
            if first_H is not None:
                summary["original_new_height_source"] = dict(identity=first_id, original_selected=fields(L, first_H, (
                    "schema", "actual_phase", "actual_current_height_sha256", "source_prepared",
                    "original_complete_MaterialTrace_and_current_RHS_used",
                    "parent_response_or_affine_used_as_new450_anchor")))
            summary["actual_new_native_owner"] = necessary_native(A, L, phase / "full-DN" / "true-tail")
            summary["complete_owned_byte_scope"] = L.inventory((("new-mesh-launch", root),))
        except Exception as error:
            L.fail("original-mesh-readback", error)
    else:
        summary["possibly_mutable_scientific_tree_not_read"] = True
        summary["no_scientific_failure_or_acceptance_inferred_from_missing_quiet_evidence"] = True
    for key in ("entry_stdout", "entry_stderr"):
        path = getattr(args, key)
        if path is not None:
            try:
                p = path.resolve()
                require(namespace in p.parents and p != namespace and not path.is_symlink(),
                        "Entry diagnostic must be an actual owned namespace file")
                if quiet:
                    L.log_view(p, "R431-outer-entry-" + key)
                else:
                    summary.setdefault("entry_diagnostics_deferred_until_outer_owner_quiet", []).append(str(p))
            except Exception as error:
                L.fail("entry-log", error)
    summary["necessary_original_log_errors"] = [r for r in L.LOGS if r["original_error_matched_lines"]]
    summary["all_read_log_count"] = len(L.LOGS)
    summary["all_read_log_index_identity"] = member(L.LOGS)
    summary["all_parsed_document_count"] = len(L.DOCUMENTS)
    summary["all_parsed_document_index_identity"] = member(L.DOCUMENTS)
    summary["explicit_omitted_member_count"] = len(L.OMISSIONS)
    summary["explicit_omitted_member_index_identity"] = member(L.OMISSIONS)
    summary["original_read_errors"] = L.ERRORS
    summary["complete_necessary_readback"] = quiet and not L.ERRORS
    summary["scope"] = dict(
        actual_mesh_plan_and_preflight_status_selected_if_present=True,
        all_literal_knots_and_all_collapsed_midpoint_records_parsed_but_only_identity_and_first_last_returned=True,
        every_present_original_FD_error_level_and_flag_selected_by_unchanged_original_phase_reader=True,
        actual_original_RMS_BC_final_J_audit_cut_and_checkpoint_values_selected_if_present=True,
        all_present_native_trace_trial_and_linear_child_streams_parse_attempted_when_quiet=quiet,
        every_native_call_original_scalar_row_selected=True,
        last_actual_native_call_detail_and_all_failed_call_scopes_selected=True,
        earlier_native_trials_large_states_J_and_success_factor_RHS_tables_identity_only=True,
        original193_and_prior_mesh_readbacks_not_replaced_or_reclaimed_here=True,
        no_sampler_recalculation_or_accepted_field_from_reader=True,
        no_numeric_mesh_or_spectral_convergence_inferred=True,
        one_necessary_conclusion_no_raw_transport_partition_or_encoding=True)
    index = L.write(out / "necessary-readback-index.json", dict(summary=summary,
        original_documents=L.DOCUMENTS, original_logs=L.LOGS, omitted_members=L.OMISSIONS))
    raw = canonical(summary)
    if len(raw) > LIMIT:
        fallback = dict(schema=SCHEMA + "-over-budget", repository=REPO,
            run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
            source=L.identity(__file__), complete_necessary_readback=False,
            original_summary_identity=dict(bytes=len(raw), sha256=sha(raw)),
            section_bytes={key: len(canonical(value)) for key, value in summary.items()},
            original_error_count=len(L.ERRORS), actual_quiet_observed=quiet,
            actual_temporary_readback_index=index, cleanup_marker_not_written=True,
            original_scientific_acceptance_not_changed_by_transport_failure=True,
            raw_retained_until_runner_destruction_not_claimed_recoverable_after_it=True)
        output(fallback, out)
        return 70
    sid = output(summary, out)
    if summary["complete_necessary_readback"]:
        L.write(out / "readback-complete.json", dict(schema=SCHEMA + "-complete-marker",
            repository=REPO, run_id=os.environ["GITHUB_RUN_ID"], source_commit=os.environ["GITHUB_SHA"],
            reader_source=L.identity(__file__), actual_namespace=str(namespace), actual_launch_directory=str(root),
            actual_launch_result=lid, necessary_summary=sid, complete_necessary_scope=True,
            actual_quiescence_observation=summary["actual_quiescence_observation"],
            original_other_readbacks_and_current_quiet_still_required_before_cleanup=True,
            no_scientific_acceptance_created=True))
    return 0 if summary["complete_necessary_readback"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
