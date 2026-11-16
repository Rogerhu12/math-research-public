#!/usr/bin/env python3
"""Request206: up to eight complete39 model/FD pairs from actual98.

Retain every frozen38 query and add genuine RIGHT-RMS459 with actual459/460
capture. The original complete31 actual98 pair is the direct first parent;
actual171 is evidence, never a replayed prefix or reconstructed warm.
Each next own39 pair is produced and checked by the original fresh FD.
One whole-chain necessary document contains every actual trial and returned
query-failure address in explicit scalar tables, without repeated field names. Large scientific JSON/arrays stay temporary; they
are not split to stdout. Durable necessary records precede pair movement
and large-payload retirement, so always-readback can recover partial runs.
The original science gates, atomic budgets and native/fullDN scope stay.
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
import time
import traceback

REPOSITORY = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-larger-amplitude"
SCHEMA = "thirty_nine-real-pair-tabular-batches-v1"
REQUEST_SCHEMA = "thirty_nine-real-pair-tabular-continuation-request-v1"
HELPER_NAME = "root_20261116_thirty_nine_tabular_chain_readout.py"
HELPER_SHA = "9840e9ae7c1219b9b3bbef45d4bacb7110f639e980f76a6d592eb9f96c9bb68f"
BASE_REQUEST_NAME = "public-thirty-nine-tabular-model-recipe.json"
BASE_REQUEST_SHA = "2353548631ab0b7a6a67e25b2f1360c4b78066448df6b85cd0bff56e2b7868ab"
FIELD_SCHEMA = "canonical-parsed-warm-field-subset-v1"
FIELD_NAMES = ("mesh", "states", "rhs", "field_representation",
               "complete_scalar_profile")
SUMMARY_LIMIT = 90000
progress = dict(schema=SCHEMA, phase="binding", batch_index=None,
    science_started=False, native_or_full_DN_called=False)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def encoded(value):
    return (json.dumps(value, ensure_ascii=True, sort_keys=True,
        separators=(",", ":"), allow_nan=False)+"\n").encode("utf-8")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def file_sha(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def emit(event, value):
    print(json.dumps(dict(event=event, **value), ensure_ascii=True,
        separators=(",", ":"), allow_nan=False), flush=True)


def load_helper(path):
    require(file_sha(path) == HELPER_SHA, "Frozen request206 orchestration helpers changed")
    spec = importlib.util.spec_from_file_location("_request206_thirty_nine_necessary_helpers", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def original_JSON_identity(value):
    raw = encoded(value)
    return dict(canonical_bytes=len(raw),canonical_sha256=sha(raw),
        scope="original parsed JSON, sorted ASCII keys, one LF; not raw array bytes")


def field_identity(warm):
    """Only JSON selection/hashing; no array conversion or numerical action."""
    selected = {key: warm[key] for key in FIELD_NAMES if key in warm}
    present = list(selected)
    profile = warm.get("complete_scalar_profile")
    producer = warm.get("optimization_warm")
    profile = profile if isinstance(profile,dict) else {}
    producer = producer if isinstance(producer,dict) else {}
    frozen = profile.get("frozen_design_parameters")
    current = producer.get("actual_global_scalar_parameters")
    # The actual original three-word parameter records only; no field,
    # height, profile or new parameter is reconstructed or reevaluated.
    parameter_fields = dict(
        original_frozen_design_parameters=(frozen if isinstance(frozen,list) and len(frozen)==3 else None),
        original_global_scalar_parameters=(current if isinstance(current,list) and len(current)==3 else None),
        original_parameter_sources_present=dict(
            frozen_design_parameters="frozen_design_parameters" in profile,
            actual_global_scalar_parameters="actual_global_scalar_parameters" in producer),
        original_parameter_readout_complete=(
            isinstance(frozen,list) and len(frozen)==3
            and isinstance(current,list) and len(current)==3),
        complete_scalar_profile_identity=original_JSON_identity(profile),
        original_native_height_identity=original_JSON_identity(
            producer.get("actual_native_height")))
    return dict(**parameter_fields, schema=FIELD_SCHEMA, ordered_fields=list(FIELD_NAMES),
        present_fields=present, complete_selected_fields_present=len(present) == len(FIELD_NAMES),
        field_sha256={key:sha(encoded(selected[key])) for key in present},
        sha256=sha(encoded(selected)),
        definition="SHA256 of parsed JSON, sorted object keys, ASCII compact encoding and one LF; original field values only",
        not_native_array_byte_hash=True, not_complete_warm_document_identity=True,
        no_states_rhs_profile_or_producer_rewritten=True)


def compare_reference(reference, pair, fields):
    """A different record hash never gates this actual new trajectory."""
    if reference is None:
        return dict(reference_supplied=False,
            previous_deleted_warm_not_reconstructed_or_assumed=True,
            physical_payload_comparison_available=False,
            comparison_is_not_a_scientific_gate=True)
    previous = reference.get("field_identity")
    comparable = (isinstance(previous, dict)
        and previous.get("schema") == FIELD_SCHEMA
        and previous.get("ordered_fields") == list(FIELD_NAMES)
        and previous.get("complete_selected_fields_present") is True
        and fields.get("complete_selected_fields_present") is True)
    return dict(reference_supplied=True, reference_run_id=reference.get("run_id"),
        reference_source_commit=reference.get("source_commit"),
        full_warm_file_SHA_equal=(pair["warm_sha256"] == reference["warm_sha256"]
            if isinstance(reference.get("warm_sha256"), str) else None),
        full_status_file_SHA_equal=(pair["status_sha256"] == reference["status_sha256"]
            if isinstance(reference.get("status_sha256"), str) else None),
        physical_payload_comparison_available=bool(comparable),
        selected_field_payload_equal=(fields["sha256"] == previous.get("sha256")
            if comparable else None),
        individual_field_equal=({key:fields["field_sha256"].get(key)
            == previous.get("field_sha256", {}).get(key) for key in FIELD_NAMES}
            if comparable else None),
        comparison_is_not_a_scientific_gate=True,
        unequal_document_SHA_does_not_locate_or_quantify_field_difference=True,
        metadata_gzip_or_timing_not_modified_to_force_a_match=True,
        fresh_result_never_relabelled_as_the_reference_run=True)


def pair_identity(helper, directory):
    warm, status = directory/"warm-001.json.gz", directory/"driver-status.json"
    return dict(warm_file=warm.name, warm_bytes=warm.stat().st_size,
        warm_sha256=helper.file_sha(warm), status_file=status.name,
        status_bytes=status.stat().st_size, status_sha256=helper.file_sha(status),
        JSON_reserialized=False, materialized_for_this_job=True)


def validate_completed_pair(helper, output, status):
    """Existing producer/status ownership contract, without a new tolerance."""
    helper.require(status.get("schema") == helper.OPTIMIZER_SCHEMA
        and status.get("optimization_progress") is True
        and status.get("accepted_warm_steps") == 1
        and status.get("success") is False
        and status.get("new_coupled_finite_acceptance") is False
        and status.get("latest_warm_file") == "warm-001.json.gz",
        "Original model must supply its one real unaccepted progress warm")
    pair = pair_identity(helper, output)
    helper.require(pair["warm_sha256"] == status.get("latest_warm_sha256"),
        "Original status must identify these exact warm bytes")
    warm = helper.read(output/pair["warm_file"])
    producer = warm.get("optimization_warm", {})
    identity = status.get("identity", {})
    helper.require(warm.get("success") is False
        and warm.get("new_coupled_finite_acceptance") is False
        and producer.get("schema") == helper.OPTIMIZER_SCHEMA
        and identity.get("schema") == helper.OPTIMIZER_SCHEMA
        and all(key in producer and producer[key] == value
                for key, value in identity.items()),
        "Preserve the actual full producer and paired status identity")
    return pair, warm


def move_pair(helper, output, carrier, expected):
    """Move only two already-consumed real files, without editing either."""
    carrier.mkdir()
    for name in ("warm-001.json.gz", "driver-status.json"):
        os.replace(output/name, carrier/name)
    actual = pair_identity(helper, carrier)
    require(actual == expected, "Same-job parent movement changed original file bytes")
    return actual


def record_batch(helper, work, summary):
    """Durable necessary fields only; one whole-chain print follows later."""
    receipt=helper.save_necessary_batch(work,summary)
    return dict(**receipt,
        complete_necessary_original_trial_fields_saved=True,
        whole_chain_stdout_readback_pending=True,
        large_scientific_JSON_not_printed_or_encoded=True)


@contextlib.contextmanager
def owned_namespace(root):
    """Retain interrupted unread output for the following always-readback step."""
    work=Path(tempfile.mkdtemp(prefix="visible-thirty-nine-206-",dir=root))
    try:
        yield work
    except BaseException:
        emit("request206_unread_namespace_retained",dict(basename=work.name,
            readback_then_cleanup_required=True,raw_uploads=0,
            scientific_success_not_inferred=True))
        raise
    else:
        # The caller prints the complete bounded chain before explicit removal.
        pass


def model_command(helper, comp, inputs, parent, output, pair):
    return [sys.executable, "-u", str(comp/helper.MODEL_ENTRY),
        "--accepted", str(inputs/"accepted.json.gz"),
        "--prepared", str(inputs/"prepared.json.gz"),
        "--tail-anchor", str(inputs/"tail-anchor.json.gz"),
        "--tail-config", str(inputs/"tail-config.json"),
        "--resume", str(parent/pair["warm_file"]),
        "--expected-resume-sha", pair["warm_sha256"],
        "--parent-status", str(parent/pair["status_file"]),
        "--expected-parent-status-sha", pair["status_sha256"],
        "--out", str(output), *helper.MODEL_FLAGS]


def run_batch(helper, reader, repo, comp, env, inputs, parent, input_pair,
              batch, batch_index, reference):
    batch.mkdir()
    output, fd_output = batch/"thirty-nine-condensed-warm", batch/"physical-response"
    command = model_command(helper, comp, inputs, parent, output, input_pair)
    progress.update(phase="one-original-model", batch_index=batch_index, science_started=True)
    model_code = helper.run_child("original-model", command, repo, env, batch)
    status_path, model_path = output/"driver-status.json", output/"model-000.json"
    qp_path, fd_path = output/"condensed-QP-summary.json", fd_output/"response-check.json"
    status = helper.read(status_path) if status_path.is_file() else {}
    model = helper.read(model_path) if model_path.is_file() else None
    qp = helper.read(qp_path) if qp_path.is_file() else None
    fd_code, fd, pair, fields = None, None, None, None
    eligible = False
    stop = dict(kind="original_model_did_not_complete_a_new_warm",
        original_phase=status.get("phase"), original_exit_code=model_code,
        original_optimization_progress=status.get("optimization_progress"),
        original_accepted_warm_steps=status.get("accepted_warm_steps"))
    if (model_code == 0 and status.get("optimization_progress") is True
            and status.get("accepted_warm_steps") == 1):
        try:
            pair, warm = validate_completed_pair(helper, output, status)
        except Exception as error:
            stop = dict(kind="actual_pair_handoff_failed", error_type=type(error).__name__,
                error=str(error)[:800], original_model_exit_code=model_code)
        else:
            # Readout failure is not an extra candidate acceptance test.
            try:
                fields = field_identity(warm)
            except Exception as error:
                fields = dict(schema=FIELD_SCHEMA, complete_selected_fields_present=False,
                    readout_error_type=type(error).__name__, readout_error=str(error)[:400],
                    field_comparison_is_not_a_scientific_gate=True)
            progress["phase"] = "original-new-warm-FD"
            fd_command = [sys.executable, "-u", str(comp/helper.FD_ENTRY),
                "--accepted", str(inputs/"accepted.json.gz"),
                "--prepared", str(output/pair["warm_file"]),
                "--tail-anchor", str(inputs/"tail-anchor.json.gz"),
                "--tail-config", str(inputs/"tail-config.json"),
                "--out", str(fd_output), "--angles", "4096"]
            try:
                fd_code = helper.run_child("original-boundary-FD", fd_command, repo, env, batch)
                fd = helper.read(fd_path) if fd_path.is_file() else None
            except helper.ReadbackIncomplete:
                # Preserve unforwarded error bytes and all original partials.
                # A transport stop is not an original scientific FD refusal.
                raise
            except Exception as error:
                stop = dict(kind="original_FD_process_or_report_failed",
                    original_exit_code=fd_code, error_type=type(error).__name__,
                    error=str(error)[:800])
            else:
                eligible = (fd_code == 0 and isinstance(fd, dict)
                    and fd.get("implementation_check_passed") is True
                    and fd.get("prepared_sha256") == pair["warm_sha256"]
                    and fd.get("complete_current_warm_boundary_FD_actually_recomputed") is True)
                stop = (None if eligible else dict(kind="original_FD_not_completed_on_new_warm",
                    original_exit_code=fd_code, original_report_present=isinstance(fd, dict),
                    original_implementation_check_passed=(fd or {}).get("implementation_check_passed"),
                    actual_prepared_sha256=(fd or {}).get("prepared_sha256")))
    summary = helper.summarize(reader, model, status, qp, fd)
    summary.update(schema=SCHEMA, batch_index=batch_index,
        run_id=os.environ.get("GITHUB_RUN_ID"), source_commit=os.environ.get("GITHUB_SHA"),
        input_pair=input_pair, produced_pair=pair, output_field_identity=fields,
        original_model_exit_code=model_code, original_FD_exit_code=fd_code,
        next_batch_eligible=eligible, stop_reason=stop,
        primary_outputs=[helper.output_receipt(path, relative) for path, relative in (
            (model_path, "thirty-nine-condensed-warm/model-000.json"),
            (status_path, "thirty-nine-condensed-warm/driver-status.json"),
            (qp_path, "thirty-nine-condensed-warm/condensed-QP-summary.json"),
            (fd_path, "physical-response/response-check.json"),
            (output/"warm-001.json.gz", "thirty-nine-condensed-warm/warm-001.json.gz"))],
        original_A_AT_full_H_C_algorithms_and_budgets_unchanged=True,
        independent39_query_definition_declared=True,
        previous_warm_or_FD_never_renamed_as_new=True,
        fresh_child_process_and_original_one_complete_J_per_model=True,
        field_comparison_does_not_gate_a_new_valid_trajectory=True,
        nonlinear_native_or_full_DN_run=False,
        success=False, new_coupled_finite_acceptance=False,
        raw_payload_uploads=0, Release_uploads=0, Git_data_publication=0,
        first_batch_reference_comparison=(compare_reference(reference, pair, fields)
            if batch_index == 0 and pair is not None else None))
    original_exit = model_code if model_code else (fd_code if fd_code is not None else 2)
    if not eligible and original_exit == 0:
        original_exit = 2  # malformed/missing successful handoff, never manufacture a parent
    return summary, output, bool(eligible), int(original_exit)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--request", type=Path, required=True)
    args = parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true"
        and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
        "Only the public repository Actions may execute the scientific children")
    repo = args.repo_root.resolve(strict=True)
    comp = repo/TOPIC/"computations"
    request = json.loads(args.request.read_bytes())
    require(request.get("request") == 206 and request.get("schema") == REQUEST_SCHEMA
        and request.get("repository") == REPOSITORY,
        "Use the independent request206 batch contract")
    require(request.get("source_sha256") == file_sha(Path(__file__)),
        "Bind this actual new orchestration source")
    require(request.get("base_request_sha256") == BASE_REQUEST_SHA
        and file_sha(comp/BASE_REQUEST_NAME) == BASE_REQUEST_SHA,
        "Retain the complete frozen request206 source/input/budget recipe")
    count, seconds = request.get("maximum_batches"), request.get("chain_budget_seconds")
    require(type(count) is int and count == 8,
        "Request206 declares an eight-model resource limit, not guaranteed completion")
    require(type(seconds) is int and seconds > 0,
        "An explicit positive between-batches orchestration budget is required")
    reference = request.get("reference_first_batch")
    require(reference is None or isinstance(reference, dict), "Reference is optional readout only")
    helper = load_helper(comp/HELPER_NAME)
    # This is the original3b8 start_new_session child. Register its real
    # session before restoration or any original model/FD process can start.
    helper.register_owner(comp,args.request)
    base = json.loads((comp/BASE_REQUEST_NAME).read_bytes())
    require(base.get("request") == 206 and base.get("schema") == "actual98-thirty-nine-model-and-FD-tabular-recipe-v1" and base.get("parent_artifact") == helper.PARENT
        and base.get("model_flags") == helper.MODEL_FLAGS,
        "Original initial pair and atomic scientific flags stay unchanged")
    for family in ("source_sha256", "parameter_sha256"):
        for name, digest in base[family].items():
            require(Path(name).name == name and file_sha(comp/name) == digest,
                "Frozen original source/parameter changed: " + name)
    reader = helper.load("_thirty_nine_batch_original_selectors", comp/helper.READER_ENTRY,
                         helper.READER_SHA)
    runner_temp = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    chain_rows, stop_reason, final_code = [], None, 0
    last_pair, last_fields = None, None
    with owned_namespace(runner_temp) as work:
        inputs = work/"inputs"
        original_inputs = helper.restore_inputs(repo, inputs)
        parent = work/"parent98"
        original_parent = helper.restore_parent(comp, reader, parent, work)
        input_pair = pair_identity(helper, parent)
        report_dir = work/"source-receipts"
        report_dir.mkdir()
        public = helper.load("_thirty_nine_batch_public_sources", comp/"exact_20261114_public_resume.py",
            base["source_sha256"]["exact_20261114_public_resume.py"])
        public_source = public.prepare_public_source(repo, work/"public-source", report_dir)
        env = dict(os.environ, VISIBLE_SOURCE_TOPIC=str(public_source),
            PYTHONDONTWRITEBYTECODE="1", OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1",
            MKL_NUM_THREADS="1", NUMEXPR_NUM_THREADS="1")
        for token in ("GITHUB_TOKEN","GH_TOKEN","MR_TOKEN"):
            env.pop(token,None)
        actual_binding = dict(schema=SCHEMA, request=206,
            run_id=os.environ.get("GITHUB_RUN_ID"), source_commit=os.environ.get("GITHUB_SHA"),
            source_sha256=file_sha(Path(__file__)), request_sha256=file_sha(args.request),
            base_request_sha256=BASE_REQUEST_SHA, helper_sha256=HELPER_SHA,
            maximum_batches=count, chain_budget_seconds=seconds,
            between_batches_budget_does_not_interrupt_an_active_original_call=True,
            new_trajectory_from_actual98_not_a_relabelled_171_parent=True,
            initial_parent_schema=helper.PARENT_OPTIMIZER_SCHEMA,
            current_optimizer_schema=helper.OPTIMIZER_SCHEMA,
            parent=original_parent, inputs=original_inputs,
            actual_query_changes=base["actual_query_change"],
            query_change_reference="complete frozen38 model",
            query_changes_from_first_actual98=base["query_changes_from_initial_actual98"],
            original_damping_and_atomic_budgets_unchanged=True,
            added_capture_intervals=[459],added_capture_nodes=[459,460],unique_capture_interval_count=26,
            actual_endpoint_count=32,complete_B_local_coordinates=10819,
            previous38_endpoint_and_local_B_support_unchanged=False,
            actual_B_support_is_noncontiguous=True,hole461_is_a_genuinely_eliminated_free_variable=True,
            baseline_C_and_full_H_outside_scope_unchanged=True,
            no_complete_native_or_full_BVP_acceptance_claim=True,
            source_pin_count=len(base["source_sha256"]),
            source_pin_mapping=helper.metadata_identity(base["source_sha256"]),
            parameter_sha256=base["parameter_sha256"],model_flags=base["model_flags"],
            exact_query_specs=base["query_specs"],gap_condensation=base["gap_condensation"])
        binding_receipt=helper.save_json_exact(work/"necessary-input-binding.json",actual_binding)
        emit("request206_chain_started",dict(request=206,run_id=os.environ.get("GITHUB_RUN_ID"),
            source_commit=os.environ.get("GITHUB_SHA"),source_sha256=file_sha(Path(__file__)),
            actual_input_binding=binding_receipt,maximum_batches=count,
            scientific_results_will_have_one_whole_chain_readback=True))
        started = time.monotonic()
        for batch_index in range(count):
            if time.monotonic()-started >= seconds:
                stop_reason = dict(kind="explicit_between_batches_time_budget",
                    completed_original_model_FD_pairs=len(chain_rows),
                    next_batch_not_started=True)
                break
            batch = work/f"batch-{batch_index:03d}"
            helper.save_json_exact(work/"necessary-chain-state.json",dict(
                phase="starting-original-model-FD-pair",batch_index=batch_index,
                completed_batch_indices=[row["batch_index"] for row in chain_rows],
                current_real_input_pair=input_pair,whole_chain_stdout_readback_pending=True))
            summary, output, eligible, code = run_batch(helper, reader, repo, comp, env,
                inputs, parent, input_pair, batch, batch_index, reference)
            actual_pair, fields = summary["produced_pair"], summary["output_field_identity"]
            carrier = None
            # Preserve complete necessary original fields locally before movement.
            # Only the final whole-chain document is printed to stdout.
            summary.update(batch_payload_removed=False,
                batch_payload_retirement_scheduled_after_complete_local_necessary_record=True,
                next_parent_pair_temporarily_retained=False,
                next_parent_pair_movement_scheduled_after_complete_local_necessary_record=bool(eligible),
                temporary_pair_is_not_an_external_checkpoint_or_published_raw=True)
            printed = record_batch(helper, work, summary)
            if eligible:
                # Original FD and the durable complete necessary record both finished.
                carrier = work/f"parent-after-{batch_index:03d}"
                moved = move_pair(helper, output, carrier, actual_pair)
                last_pair, last_fields = moved, fields
            shutil.rmtree(batch)
            if eligible:
                shutil.rmtree(parent)
                parent, input_pair = carrier, moved
            emit("thirty_nine_batch_payload_retired",dict(batch_index=batch_index,
                batch_payload_removed=True,summary_identity=printed,
                complete_local_necessary_record_preceded_large_raw_cleanup=True,
                whole_chain_stdout_readback_still_pending=True,
                next_actual_parent_pair_retained=bool(eligible)))
            accepted = next((row for row in summary["all_original_trials"]
                             if row.get("accepted") is True), {})
            chain_rows.append(dict(batch_index=batch_index, eligible=eligible,
                input_warm_sha256=summary["input_pair"]["warm_sha256"],
                output_pair=actual_pair, field_identity=fields,
                accepted_alpha=accepted.get("alpha"),
                fixed_weight_merit_before=summary.get("fixed_weight_merit_before"),
                fixed_weight_merit_after=accepted.get("actual_fixed_weight_merit"),
                original_model_exit_code=summary["original_model_exit_code"],
                original_FD_exit_code=summary["original_FD_exit_code"],
                summary_identity=printed))
            if not eligible:
                stop_reason, final_code = summary["stop_reason"], code
                break
        else:
            stop_reason = dict(kind="explicit_maximum_batch_count",
                maximum_batches=count, original_model_FD_pairs_completed=count)
        if stop_reason is None:
            stop_reason = dict(kind="no_next_original_model_started")
        row_columns = ("batch_index", "eligible", "input_warm_sha256",
            "output_warm_sha256", "output_status_sha256", "field_subset_sha256",
            "accepted_alpha", "fixed_weight_merit_before", "fixed_weight_merit_after",
            "original_model_exit_code", "original_FD_exit_code", "summary_sha256")
        compact_rows = [dict(batch_index=row["batch_index"], eligible=row["eligible"],
            input_warm_sha256=row["input_warm_sha256"],
            output_warm_sha256=(row["output_pair"] or {}).get("warm_sha256"),
            output_status_sha256=(row["output_pair"] or {}).get("status_sha256"),
            field_subset_sha256=(row["field_identity"] or {}).get("sha256"),
            accepted_alpha=row["accepted_alpha"],
            fixed_weight_merit_before=row["fixed_weight_merit_before"],
            fixed_weight_merit_after=row["fixed_weight_merit_after"],
            original_model_exit_code=row["original_model_exit_code"],
            original_FD_exit_code=row["original_FD_exit_code"],
            summary_sha256=row["summary_identity"]["sha256"]) for row in chain_rows]
        final = dict(schema=SCHEMA, request=206, run_id=os.environ.get("GITHUB_RUN_ID"),
            source_commit=os.environ.get("GITHUB_SHA"), source_sha256=file_sha(Path(__file__)),
            request_sha256=file_sha(args.request), stop_reason=stop_reason,
            attempted_batches=len(chain_rows),
            completed_model_FD_pairs=sum(row["eligible"] for row in chain_rows),
            last_actual_completed_pair=last_pair, last_completed_field_identity=last_fields,
            original_exit_code=final_code, batch_row_columns=list(row_columns),
            batch_rows=[[row[key] for key in row_columns] for row in compact_rows],
            no_cross_model_fixed_weight_merit_subtraction=True,
            all_new_models_recomputed_from_the_actual_previous_pair=True,
            final_field_not_recoverable_from_hash_alone=True,
            new_trajectory_must_not_be_relabelled_as_previous_run=True,
            success=False, new_coupled_finite_acceptance=False,
            raw_payload_uploads=0, Release_uploads=0, Git_data_publication=0,
            original_frozen_sources_unmodified=True,
            original_acceptance_gates_unchanged=True,
            independent39_query_definition_declared=True)
        final["all_owned_temporary_payload_removed"] = False
        final["Actions_ephemeral_Git_object_cache_not_erased_by_this_wrapper"] = True
        final["actual_elapsed_batch_loop_seconds"] = time.monotonic()-started
        final["cleanup_after_single_complete_whole_chain_readback"] = True
        complete_readback=helper.finish_chain(work,final)
        shutil.rmtree(work)
        emit("request206_complete_chain_cleanup",dict(
            all_owned_temporary_payload_removed=True,complete_necessary_readback=complete_readback,
            original_exit_code=final_code,raw_payload_uploads=0,
            original_acceptance_gates_changed=False))
    return int(final_code)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        emit("thirty_nine_batch_orchestration_failure", dict(schema=SCHEMA, progress=progress,
            error_type=type(error).__name__, error=str(error)[:800],
            scientific_success_not_inferred=True,
            previous_durable_necessary_batch_records_retained_for_always_readback=True,
            whole_chain_stdout_readback_may_be_pending=True,
            owned_cleanup_not_silently_claimed=True, raw_payload_uploads=0))
        traceback.print_exc()
        raise SystemExit(70 if type(error).__name__ == "ReadbackIncomplete" else 2)
