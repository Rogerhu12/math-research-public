#!/usr/bin/env python3
"""R448 one necessary original mesh/full450 readback after observed quiescence.

This standard-library reader imports pinned metadata-only helpers, never a
scientific module. It parses actual originals and selects one <=90000-byte
conclusion. Complete arrays, old native trials and success-factor tables are
identified, not encoded, split, or claimed fully returned. It never deletes.
Author: geometry agent (AI), derived from the frozen original necessary reader, 2026-11-16.
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
SCHEMA = "R448-current-C-radial-resolution450-one-necessary-readback-v1"
LAUNCH_SCHEMA = 'R448-current-C-frozen450-radial-resolution-owned-launch-v1'
DRIVER_SCHEMA = 'R448-current-C-continuous-ten-frozen450-radial-resolution-original-full-DN-v1'
LAUNCH = "geometry_20261116_current_C_frozen450_radial_resolution_owned_launch.py"
LAUNCH_SHA = "f3a2abf626fbb7f636315e40608b55170748a779e7bdf1287ebc362e04b73cf2"
DRIVER = "geometry_20261116_continuous_ten_frozen450_radial_resolution_refinement.py"
DRIVER_SHA = "137d42cb27bb1aef227d42445adf07a6d11f7bba57315abdf151cc3b0086c7e8"
LIFECYCLE = "geometry_20261115_current_C_ten450_postsolve_geometry.py"
LIFECYCLE_SHA = "84d0450f2f362138045c222f5a47162e030fd0be8b6c7a99c5d66c0e41da425a"
PHASE_READER = "root_20261116_continuous_ten_resolution_phase_readout.py"
PHASE_READER_SHA = "448c35c390abd78d169db8bad0c292d89b18cb0109fe5216420b5133479132bf"
BASE_READER = "root_20261115_current_C_pruefer_positive_full453_necessary_readout.py"
BASE_READER_SHA = "34b49f026338b90b691cbd170d6d6303c7ec3549f2329ba0f4457a2cfeab75c9"
PINS = {LAUNCH: LAUNCH_SHA, DRIVER: DRIVER_SHA, LIFECYCLE: LIFECYCLE_SHA,
        PHASE_READER: PHASE_READER_SHA, BASE_READER: BASE_READER_SHA}
JOINT_READER = "root_20261115_current_C_pruefer_joint_full453_necessary_readout.py"
JOINT_READER_SHA = "19878e48ed25dec8bdcbd36c3d7ea7168796a08fb60675ad7455dbb296a0918c"
PINS[JOINT_READER] = JOINT_READER_SHA
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
LAUNCH_KEYS += ("actual_origin_source_tuple","original_origin_recipe","parent_resolution",
    "actual_resolution","refinement_factors","actual_sampling_started","actual_BVP_child_started",
    "actual_sampling_completed","actual_sampling_result","actual_sampling_scope",
    "actual_previous_sampling_result","declared_sampling_parameters","actual_sampling_steps",
    "actual_new_native_configuration","actual_new_native_geometry","old_native_arrays_or_factors_reused",
    "actual_sampling_result_absent","possibly_mutable_sampling_not_read",
    "actual_refinement_not_started_after_sampler_return","declared_changes_only_resolution_and_explicit_sampling_work_resources",
    "original_nonlinear_acceptance_policy_changed","complete_original_C_and_deep_family_inputs_preserved")
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
SESSION_KEYS += ("actual_resolution","refinement_factors","actual_parent_resolution",
    "same_ten_target_identity_verified_by_actual_resolution_writer",
    "same_physical_angle_target_not_identical_material_components")
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

PLAN_KEYS += ("new_midpoints_requested","resolution_seed_nodes","radial_seed_policy",
    "actual_duplicate_nodes_not_counted_twice","resolution_seed_float64le_sha256",
    "radial_seed_preserves_parent_nodes_but_not_an_error_certificate",
    "angular_and_native_step_refinement_declared_separately",
    "spectral_mode_count_or_native_stage_count_changed")


PLAN_KEYS += ("parent_closed_interval_count","radial_mesh_factor",
    "complete_requested_candidate_count","candidate_rule","mandatory_parent_and_knot_union_nodes",
    "every_parent_interval_uses_the_same_declared_factor","duplicate_rounded_values_not_counted_twice",
    "complete_requested_candidate_enumeration","complete_seed_constructed",
    "processed_candidate_count","new_distinct_candidate_count","rounded_onto_parent_endpoint_count",
    "duplicate_candidate_or_knot_count","first_machine_collapsed_candidate","last_machine_collapsed_candidate",
    "last_completed_candidate","other_four_resolution_factors",
    "current_H_FD_fullDN_final_J_audit_unvisited_at_seed_plan_creation",
    "abrupt_stop_plan_frontier_is_conservative_and_may_overlap_the_actual_candidate_ledger",
    "unvisited_subdivision_scope","candidate_ledger","distinct_union_nodes_at_resource_stop",
    "resource_reason","added_seed_nodes","actual_resolution_increase",
    "all_requested_union_nodes_retained_by_original_preflight",
    "original_parent_state_word_retention_applies_to_seed_not_terminal_solution",
    "terminal_solver_mesh_is_its_actual_output_not_a_promised_unchanged_seed")


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


def quiescence(H,launch):
    record=dict(launcher_returned=launch.get("launcher_returned") is True,
        original_owned_group_quiescent=launch.get("owned_group_quiescent_before_readback") is True,
        observed_active_matching_processes=[],actual_child_group_members=[],errors=[],
        no_signals_or_process_mutation_performed=True)
    leader=launch.get("actual_launcher_process")
    if not isinstance(leader,dict):record["errors"].append("actual-launcher-process-identity-absent")
    else:
        now=H.proc_record(leader["pid"])
        if H.same_process(leader,now) and now["state"]!="Z":record["observed_active_matching_processes"].append(now)
    children=launch.get("observed_children")
    require(isinstance(children,list),"All actual owned sampler/solver records are required")
    for entry in children:
        if not entry.get("started"):continue
        child=entry.get("observed_child")
        if not isinstance(child,dict):
            record["errors"].append("started-child-identity-absent:"+str(entry.get("role")));continue
        for old in child.get("observed_processes",[]):
            now=H.proc_record(old["pid"])
            if H.same_process(old,now) and now["state"]!="Z":record["observed_active_matching_processes"].append(now)
        record["actual_child_group_members"].extend(v for v in H.group_rows(child["pid"]) if v["state"]!="Z")
        if child.get("identity_conflicts") or entry.get("owned_group_quiescent") is not True:
            record["errors"].append("child-owner-not-quiet:"+str(entry.get("role")))
        if child.get("actual_child_returncode") is None:
            record["errors"].append("child-return-unreaped:"+str(entry.get("role")))
    record["all_original_owned_child_records_identity"]=member(children)
    record["observed_quiet"]=bool(record["launcher_returned"] and record["original_owned_group_quiescent"]
        and not record["observed_active_matching_processes"] and not record["actual_child_group_members"]
        and not record["errors"])
    return record


def plan_view(L, path):
    value, identity = L.document(path, "R448-original-mesh-plan")
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
    print("BEGIN_R448_FROZEN450_RESOLUTION_NECESSARY", flush=True)
    print(raw.decode("ascii"), end="", flush=True)
    print("END_R448_FROZEN450_RESOLUTION_NECESSARY", flush=True)
    identity = dict(bytes=len(raw), sha256=sha(raw))
    print(json.dumps(dict(event="R448_necessary_summary_identity", **identity,
                         hash_scope="canonical ASCII JSON including LF")), flush=True)
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as stream:
            stream.write("resolution_summary=" + raw.decode("ascii").rstrip("\n") + "\n")
            stream.write("resolution_summary_bytes=" + str(len(raw)) + "\n")
            stream.write("resolution_summary_sha256=" + sha(raw) + "\n")
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
    H = imported(comp, LIFECYCLE, LIFECYCLE_SHA, "_R448_reader_owned_metadata")
    A = imported(comp, PHASE_READER, PHASE_READER_SHA, "_R448_original_phase_metadata")
    # Load the actual source-family selector. No scientific module is imported.
    raw_launch=(root/"result.json").read_bytes()
    selector_hint=json.loads(raw_launch)
    family=selector_hint.get("actual_origin_source_tuple",{}).get("kind")
    if family=="joint203":
        L=imported(comp,JOINT_READER,JOINT_READER_SHA,"_R448_actual_joint_metadata")
    elif family=="original193" or family is None:
        L=A.load_reader(comp)
    else:raise ValueError("No unnamed native source family is selected")
    pins = {}
    for name, expected in PINS.items():
        item = L.identity(comp / name)
        require(item["sha256"] == expected, "The actual independent source differs: " + name)
        pins[name] = item
    launch, lid = L.document(root / "result.json", "R448-actual-launch", required=True)
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
            summary["actual_owned_children"]=[dict(
                original_selected=fields(L,row,("role","declared_process_budget_seconds",
                    "actual_process_budget_seconds","actual_remaining_science_seconds","actual_start_free_bytes",
                    "started","actual_child_exit","owned_group_quiescent","latest_free_bytes","stdout","stderr")),
                complete_actual_owner_identity=member(row)) for row in launch.get("observed_children",[])]
            for row in launch.get("observed_children",[]):
                for key in ("stdout","stderr"):
                    if row.get(key) is not None:
                        path=H.contained(row[key]["file"],root,exists=True)
                        require(H.same_payload(L.identity(path),row[key]),"Actual child log differs")
                        L.log_view(path,"R448-"+str(row.get("role"))+"-"+key)
            sample=root/"native-sampling"
            if sample.is_dir():
                expected=(launch.get("actual_sampling_result") or {}).get("sha256")
                summary["actual_new_sampling"]=A.sampler_view(L,sample,expected)
            else:
                summary["actual_new_sampling"]=dict(exists=False,actual_started=launch.get("actual_sampling_started"),
                    no_native_geometry_inferred=True)
            if launch.get("actual_mesh_recipe") is not None:
                recipe, rid = L.document(root / "actual-resolution-recipe.json", "R448-actual-mesh-recipe", True)
                require(recipe is not None and H.same_payload(rid, launch["actual_mesh_recipe"]),
                        "Actual generated mesh recipe differs from the launcher receipt")
                summary["actual_mesh_recipe"] = dict(identity=rid, complete_original_small_recipe=recipe)
            driver = root / "refined-BVP"
            state, sid = L.document(driver / "adapter-status.json", "R448-actual-adapter-state")
            if state is not None:
                current(state)
                require(state.get("schema") == DRIVER_SCHEMA and state.get("source_sha256") == DRIVER_SHA,
                        "The original actual R448 producer differs")
                if launch.get("actual_adapter_status") is not None:
                    require(H.same_payload(sid, launch["actual_adapter_status"]), "Mutable adapter receipt differs")
                summary["actual_mesh_state"] = dict(identity=sid, original_selected=fields(L, state, SESSION_KEYS))
                for key in ("consumed_source_sha256", "native_live_calls"):
                    if key in state:
                        summary["actual_" + key + "_identity"] = member(state[key])
                summary["native_call_ledger_count"] = len(state.get("native_live_calls", []))
                summary["stage_started_false_does_not_imply_no_seed_or_preflight_evaluation"] = True
            elif launch.get("actual_BVP_child_started") is True:
                summary["actual_adapter_absent_after_child"] = True
                summary["runtime_or_binding_error_scope_only_from_original_entry_logs"] = True
            else:
                summary["R448_scientific_child_not_started_by_actual_launcher"] = True
            phase = driver / "refined450"
            summary["original_refined450_outputs"] = A.phase_documents(L, phase)
            seed = phase / "initial-guess"
            summary["original_mesh_plans"] = [plan_view(L, seed / name) for name in (
                "radial-resolution-plan.json", "complete-nested-seed-binding.json")]
            first_H, first_id = L.document(phase / "actual-H-response" / "actual-first-height-input.json",
                                           "R448-original-first-height")
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
                    L.log_view(p, "R448-outer-entry-" + key)
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
        all_literal_knots_parsed_but_only_complete_identity_returned=True,
        radial_plan_complete_pending_interval_and_subdivision_addresses_returned=True,
        original_candidate_counts_and_first_last_machine_collapse_returned=True,
        full_candidate_ledger_and_earlier_collapse_rows_only_byte_identity_not_body=True,
        abrupt_driver_stop_pending_scope_may_conservatively_overlap_retained_ledger=True,
        every_present_original_FD_error_level_and_flag_selected_by_unchanged_original_phase_reader=True,
        actual_original_RMS_BC_final_J_audit_cut_and_checkpoint_values_selected_if_present=True,
        all_present_native_trace_trial_and_linear_child_streams_parse_attempted_when_quiet=quiet,
        every_native_call_original_scalar_row_selected=True,
        last_actual_native_call_detail_and_all_failed_call_scopes_selected=True,
        earlier_native_trials_large_states_J_and_success_factor_RHS_tables_identity_only=True,
        original193_and_prior_mesh_readbacks_not_replaced_or_reclaimed_here=True,
        actual_new_sampler_full112_modes_and_every_unpaid_stream_selected_by_original_source_family_reader=True,
        successful_far_row_full_interval_tables_and_native_arrays_identity_only=True,
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
