#!/usr/bin/env python3
"""R557: necessary actual two-worker ownership, commit and unpaid scopes.

This reads only the current sampler's returned metadata. It neither executes
scientific code nor infers completion from a successful subset. Successful
private mathematical rows remain original payload identities; every returned
uncommitted address and original error is selected explicitly. The original
outer single-body 90000-byte limit is unchanged.
Author: OpenAI / ChatGPT exact_refinement (AI), 2026-11-16.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

SCHEMA = "R557-complete112-two-worker-necessary-scope-v1"
ORIGINAL_SCHEMA = "R556-complete112-two-worker-mode-propagation-v1"
ORIGINAL_SOURCE_SHA = "563022ef9b22ef547ebb800d0689ef4530345f5a728216f47b2239cb1c3eb5c8"
STREAMS = ("coefficient-boxes", "far-accepted-panels", "far-complete-tubes",
    "far-panel-commits", "far-inverse-leaf-coverage", "complete-unpaid-scope")
TASK_COLUMNS = (
    "original_task_index", "mode_index", "physical_frequency",
    "pid", "ppid", "pgid", "sid", "start_ticks",
    "actual_worker_started", "actual_worker_reaped", "actual_worker_exit",
    "global_transfer_started", "global_transfer_complete", "global_mode_row",
    "complete_required_far_propagation", "complete_unit_row_family",
    "actual_cache_records", "actual_mode_result_bytes", "actual_mode_result_sha256",
    "actual_global_commit_bytes", "actual_global_commit_sha256",
    "all_six_redundant_private_streams_retired",
    "retained_original_mode_result_and_ownership", "global_payload_not_retired")
TOP_FIELDS = (
    "schema", "source", "parent_process", "actual_input_binding", "actual_context",
    "worker_count", "max_simultaneous_mode_spools", "original_mode_order",
    "actual_started_modes", "actual_worker_scientific_entry_modes",
    "actual_globally_committed_modes", "owned_child_events",
    "original_phase_clock_restarted", "private_work_allowances_created",
    "every_attempt_uses_one_shared_admission_counter",
    "new_principal_angle_or_root_choice", "original_sample_and_momentum_stages_unchanged",
    "all_internal_interval_transport_uses_exact_midpoint_radius_pairs",
    "worker_entry_list_scope", "process_quiet", "all_required_modes_returned",
    "all_required_mode_families_complete", "actual_not_started_modes",
    "actual_started_but_not_globally_committed_modes",
    "all_unvisited_required_modes_retained", "actual_elapsed_seconds",
    "parent_geometry_cache_records_released", "error", "budget_record_error",
    "cancellation_record_error", "first_parent_resource_observation",
    "spool_retirement_stop")
ERROR_FIELDS = (
    "ownership_unknown", "registration_error", "transfer_error",
    "spool_retirement_errors", "mode_return_read_error", "unpaid_scope_write_error")


def canonical(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True,
        separators=(",", ":"), allow_nan=False)+"\n").encode("utf-8")


def metadata_identity(value):
    raw = canonical(value)
    return dict(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest(),
        byte_scope="canonical complete returned metadata, not original file bytes")


def required_scope(value, state_view, last_failure):
    """Only original large factor-state witnesses use the existing selector."""
    if not isinstance(value, dict):
        return value
    out = dict(value)
    last = value.get("last_paid")
    if isinstance(last, dict):
        chosen = dict(last)
        if "complete_factorized_state" in chosen:
            chosen["complete_factorized_state"] = state_view(
                chosen["complete_factorized_state"])
        out["last_paid"] = chosen
    if "complete_current_factorized_state" in out:
        out["complete_current_factorized_state"] = state_view(
            out["complete_current_factorized_state"])
    if "last_unaccepted_candidate" in out:
        out["last_unaccepted_candidate"] = last_failure(
            out["last_unaccepted_candidate"])
    # The transaction, complete pending stack/suffix and all written spans
    # are original metadata, not count-capped by small().
    return out


def uncommitted_row(row, index, line_sha, state_view, last_failure):
    out = dict(row)
    if "original_mode_scope" in out:
        out["original_mode_scope"] = required_scope(
            out["original_mode_scope"], state_view, last_failure)
    out.update(original_row_index=index, original_line_sha256=line_sha,
        parallel_private_addresses_are_not_global_committed_addresses=True,
        exact_complete_original_row_metadata=metadata_identity(row),
        original_factor_state_witness_selection_is_unchanged=True)
    return out


def _safe_member(root, name):
    root = Path(root).resolve()
    path = root/name
    if Path(name).is_absolute() or path.is_symlink() or root not in path.resolve().parents:
        raise ValueError("Use the actual contained parallel-mode metadata")
    return path


def parallel_scope(value, directory, file_identity, state_view, last_failure):
    """Select a fixed ownership table and full unsuccessful-mode metadata.

    Every table cell is a named actual scalar/identity. An absent selected key
    maps to null, as in the original necessary tables. No table row is dropped.
    This is not a lossless encoding of the private successful scientific tree.
    """
    if value is None:
        return None
    if not isinstance(value, dict):
        raise ValueError("The actual parallel-mode record must be an object")
    if value and (value.get("schema") != ORIGINAL_SCHEMA
            or value.get("source", {}).get("sha256") != ORIGINAL_SOURCE_SHA):
        raise ValueError("Use the actual pinned two-worker helper record")
    root = Path(directory)/"parallel-mode-spools"
    out = {key: value[key] for key in TOP_FIELDS if key in value}
    out.update(necessary_scope_schema=SCHEMA,
        actual_complete_parallel_metadata=metadata_identity(value),
        task_columns=list(TASK_COLUMNS), all_actual_task_rows=[],
        all_task_errors_and_uncommitted_metadata=[],
        table_absent_selected_fields_are_null=True,
        successful_private_mathematical_rows_and_commit_spans_are_identities_only=True,
        original_mode_family_and_pending_scope_still_read_from_global_ledgers=True,
        no_new_numerical_acceptance_or_completion_inferred=True)
    path = _safe_member(root, "result.json")
    if path.is_file():
        out["actual_parallel_result_file"] = file_identity(path)
    else:
        out["actual_parallel_result_file"] = None
        out["parallel_result_file_absent_not_completion"] = True
    tasks = value.get("mode_tasks", [])
    if not isinstance(tasks, list):
        raise ValueError("The actual mode task list differs")
    for index, task in enumerate(tasks):
        if not isinstance(task, dict):
            raise ValueError("An actual mode task is not an object")
        process = task.get("actual_process") or {}
        rid = task.get("actual_mode_result") or {}
        cid = task.get("actual_global_commit") or {}
        retired = task.get("retired_redundant_local_streams")
        all_retired = (retired == list(STREAMS)) if retired is not None else None
        out["all_actual_task_rows"].append([
            index, task.get("mode_index"), task.get("physical_frequency"),
            process.get("pid"), process.get("ppid"), process.get("pgid"),
            process.get("sid"), process.get("start_ticks"),
            task.get("actual_worker_started"), task.get("actual_worker_reaped"),
            task.get("actual_worker_exit"), task.get("global_transfer_started"),
            task.get("global_transfer_complete"), task.get("global_mode_row"),
            task.get("complete_required_far_propagation"), task.get("complete_unit_row_family"),
            task.get("actual_cache_records"), rid.get("bytes"), rid.get("sha256"),
            cid.get("bytes"), cid.get("sha256"), all_retired,
            task.get("retained_original_mode_result_and_ownership"),
            task.get("global_payload_not_retired")])
        unsuccessful = (task.get("global_transfer_complete") is not True
            or task.get("actual_worker_reaped") is not True
            or task.get("complete_required_far_propagation") is not True
            or task.get("complete_unit_row_family") is not True
            or any(task.get(key) for key in ERROR_FIELDS))
        if not unsuccessful:
            continue
        selected = dict(task)
        # The pipe repeats the same original mode-result identity. It is small
        # metadata; preserve its real content, presence and any original errors.
        selected["original_task_index"] = index
        selected["exact_complete_original_task_metadata"] = metadata_identity(task)
        mode_file = _safe_member(root, "mode-"+str(task["mode_index"])+"/mode-result.json")
        if task.get("actual_worker_reaped") is True and mode_file.is_file():
            actual = file_identity(mode_file)
            declared = task.get("actual_mode_result")
            if declared is not None and any(actual.get(key) != declared.get(key)
                    for key in ("bytes", "sha256")):
                raise ValueError("The returned uncommitted mode metadata identity differs")
            original = json.loads(mode_file.read_bytes())
            if original.get("source", {}).get("sha256") != ORIGINAL_SOURCE_SHA:
                raise ValueError("An original mode return has another helper source")
            row = original.get("original_mode")
            selected["actual_mode_result_read"] = actual
            selected["actual_mode_return_error"] = original.get("error")
            selected["actual_mode_finalization_errors"] = original.get("finalization_errors")
            selected["scientific_entry_reached"] = original.get("scientific_entry_reached")
            if isinstance(row, dict):
                keys = ("complete_pending_scope", "last_paid",
                    "complete_current_factorized_state", "last_unaccepted_candidate",
                    "uncommitted_transaction", "uncommitted_written_step_span",
                    "uncommitted_written_far_span", "complete_required_far_propagation",
                    "complete_unit_row_family_enclosed", "error")
                chosen = {key: row[key] for key in keys if key in row}
                selected["actual_original_mode_pending_scope"] = required_scope(
                    chosen, state_view, last_failure)
                selected["private_indices_are_not_global_committed_indices"] = True
            else:
                selected["original_mode_scientific_return_absent"] = True
        else:
            selected["mode_result_not_read_before_actual_reap_or_when_absent"] = True
        out["all_task_errors_and_uncommitted_metadata"].append(selected)
    out["actual_task_count"] = len(tasks)
    out["source_file_identity_path_rules"] = dict(
        mode_result="parallel-mode-spools/mode-{mode_index}/mode-result.json",
        global_commit="parallel-mode-spools/mode-{mode_index}-global-commit.json",
        paths_are_current_sampler_relative=True,
        original_file_paths_retained_in_all_unsuccessful_task_metadata=True)
    for filename, key in (
            ("first-resource-stop.json", "actual_shared_original_resource_stop"),
            ("first-peer-mode-stop.json", "actual_first_peer_mode_stop"),
            ("input-binding.json", "actual_parallel_input_binding")):
        path = _safe_member(root, filename)
        if path.is_file():
            item = json.loads(path.read_bytes())
            actual = file_identity(path)
            if key == "actual_parallel_input_binding":
                # The full original C/root input object is already bound by the
                # sampler. Preserve this additional complete original identity
                # and the actual common budget/context facts, not another copy.
                fields = ("actual_required_source_panel_index",
                    "actual_initial_far_sampling_leaf_prefix", "original_scope_conditions",
                    "physical_far_word", "mu_word", "all_required_frequencies",
                    "actual_context", "precision_bits", "max_depth", "local_defect_bits",
                    "panel_norm_limit", "taylor_terms", "max_geometry_cache_records",
                    "original_phase_started_monotonic", "original_phase_seconds",
                    "original_work_units", "original_free_bytes_reserve")
                chosen = {name: item[name] for name in fields if name in item}
                chosen["complete_original_input_binding_identity"] = metadata_identity(
                    item.get("original_input_binding"))
                out[key] = dict(actual_file=actual, original_selected_fields=chosen)
            else:
                out[key] = dict(actual_file=actual, original_record=item)
        else:
            out[key] = None
    return out


def recover_parallel_scope(directory, file_identity, state_view, last_failure):
    """Return actual helper metadata when the outer sampler result is absent.

    This never supplies missing native geometry, numeric rows or a completed
    sampler. An absent complete helper record leaves the started/committed
    mode sets explicitly unknown; no such set is reconstructed from filenames.
    """
    root = Path(directory)/"parallel-mode-spools"
    if not root.exists():
        return None
    path = _safe_member(root, "result.json")
    if not path.is_file():
        return dict(necessary_scope_schema=SCHEMA, actual_spool_directory=str(root),
            complete_parallel_result_absent=True,
            actual_started_and_committed_mode_sets_not_returned=True,
            no_mode_completion_or_unstarted_suffix_inferred=True,
            original_private_payload_must_remain_owned=True)
    value = json.loads(path.read_bytes())
    out = parallel_scope(value, directory, file_identity, state_view, last_failure)
    out.update(original_complete_sampler_result_absent=True,
        actual_sampler_numeric_or_native_completion_not_inferred=True,
        original_point_sampling_scope_not_reconstructed=True)
    return out
