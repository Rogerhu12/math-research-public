#!/usr/bin/env python3
"""Request155: complete37 model/FD pairs from actual98.

Retain all original35 queries and add actual full MID489/MID490 capture.
Actual141 is selection evidence, never a deleted warm input. Each next own37
pair is truly produced and fresh-FD checked in this job. Preserve every trial
JSON member before cleanup; keep interrupted unread output until the always
readback step. No nonlinear native or full-DN solve is requested.
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
SCHEMA = "thirty_seven-real-pair-temporary-batches-v1"
REQUEST_SCHEMA = "thirty_seven-real-pair-batch-continuation-request-v1"
HELPER_NAME = "root_20261115_thirty_seven_temporary_readout.py"
HELPER_SHA = "f5d598cdde4c46d2904eea2ef0d20b6009e8eb284ee9a2f6f18d20cbdfc582b7"
BASE_REQUEST_NAME = "public-thirty-seven-model-recipe.json"
BASE_REQUEST_SHA = "f8a382475b48cd322b4f44c6a34047fe0552b14ee38832c99924edd08c5156ea"
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
    require(file_sha(path) == HELPER_SHA, "Frozen request155 orchestration helpers changed")
    spec = importlib.util.spec_from_file_location("_thirty_seven_batch_original_helpers", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def field_identity(warm):
    """Only JSON selection/hashing; no array conversion or numerical action."""
    selected = {key: warm[key] for key in FIELD_NAMES if key in warm}
    present = list(selected)
    return dict(schema=FIELD_SCHEMA, ordered_fields=list(FIELD_NAMES),
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


def print_batch(helper, reader, summary):
    """Complete original values; an oversized summary is a semantic stream."""
    raw=encoded(summary)
    identity=dict(batch_index=summary["batch_index"],bytes=len(raw),sha256=sha(raw),
        size_is_not_a_scientific_gate=True)
    emit("thirty_seven_batch_scalar_identity",identity)
    if len(raw)<=SUMMARY_LIMIT:
        print("BEGIN_THIRTY_SEVEN_BATCH_SCALAR_SUMMARY",flush=True)
        sys.stdout.write(raw.decode("utf-8"))
        print("END_THIRTY_SEVEN_BATCH_SCALAR_SUMMARY",flush=True)
        return dict(**identity,complete_selected_scalar_summary_printed=True,
            complete_original_trial_JSON_fields_preserved=True,single_frame_summary_complete=True)
    stream=helper.stream_complete_json("batch-%03d/complete-original-summary"%summary["batch_index"],summary)
    index=dict(schema=SCHEMA,batch_index=summary["batch_index"],
        scalar_summary_complete=False,complete_semantic_stream=True,
        complete_original_summary=stream,original_summary_bytes=len(raw),original_summary_sha256=sha(raw),
        original_trial_count=len(summary["complete_original_trial_JSON_records"]),
        original_model_exit_code=summary["original_model_exit_code"],
        original_FD_exit_code=summary["original_FD_exit_code"],
        next_batch_eligible=summary["next_batch_eligible"],stop_reason=summary["stop_reason"],
        input_pair=summary["input_pair"],produced_pair=summary["produced_pair"],
        no_original_trial_JSON_member_omitted=True,raw_payload_uploads=0)
    helper.bounded_event("thirty_seven_complete_summary_stream_index",index)
    return dict(**identity,complete_selected_scalar_summary_printed=True,
        single_frame_summary_complete=False,complete_semantic_stream=stream,
        complete_original_trial_JSON_fields_preserved=True)


@contextlib.contextmanager
def owned_namespace(root):
    """Retain interrupted unread output for the following always-readback step."""
    work=Path(tempfile.mkdtemp(prefix="visible-thirty-seven-155-",dir=root))
    try:
        yield work
    except BaseException:
        emit("request155_unread_namespace_retained",dict(basename=work.name,
            readback_then_cleanup_required=True,raw_uploads=0,
            scientific_success_not_inferred=True))
        raise
    else:
        shutil.rmtree(work)


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
    output, fd_output = batch/"thirty-seven-condensed-warm", batch/"physical-response"
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
            (model_path, "thirty-seven-condensed-warm/model-000.json"),
            (status_path, "thirty-seven-condensed-warm/driver-status.json"),
            (qp_path, "thirty-seven-condensed-warm/condensed-QP-summary.json"),
            (fd_path, "physical-response/response-check.json"),
            (output/"warm-001.json.gz", "thirty-seven-condensed-warm/warm-001.json.gz"))],
        original_A_AT_full_H_C_algorithms_and_budgets_unchanged=True,
        independent37_query_definition_declared=True,
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
    require(request.get("request") == 155 and request.get("schema") == REQUEST_SCHEMA
        and request.get("repository") == REPOSITORY,
        "Use the independent request155 batch contract")
    require(request.get("source_sha256") == file_sha(Path(__file__)),
        "Bind this actual new orchestration source")
    require(request.get("base_request_sha256") == BASE_REQUEST_SHA
        and file_sha(comp/BASE_REQUEST_NAME) == BASE_REQUEST_SHA,
        "Retain the complete frozen request155 source/input/budget recipe")
    count, seconds = request.get("maximum_batches"), request.get("chain_budget_seconds")
    require(type(count) is int and 1 <= count <= 64,
        "An explicit bounded number of original atomic models is required")
    require(type(seconds) is int and seconds > 0,
        "An explicit positive between-batches orchestration budget is required")
    reference = request.get("reference_first_batch")
    require(reference is None or isinstance(reference, dict), "Reference is optional readout only")
    helper = load_helper(comp/HELPER_NAME)
    base = json.loads((comp/BASE_REQUEST_NAME).read_bytes())
    require(base.get("request") == 155 and base.get("schema") == "actual98-thirty-seven-model-and-FD-recipe-v1" and base.get("parent_artifact") == helper.PARENT
        and base.get("model_flags") == helper.MODEL_FLAGS,
        "Original initial pair and atomic scientific flags stay unchanged")
    for family in ("source_sha256", "parameter_sha256"):
        for name, digest in base[family].items():
            require(Path(name).name == name and file_sha(comp/name) == digest,
                "Frozen original source/parameter changed: " + name)
    reader = helper.load("_thirty_seven_batch_original_selectors", comp/helper.READER_ENTRY,
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
        public = helper.load("_thirty_seven_batch_public_sources", comp/"exact_20261114_public_resume.py",
            base["source_sha256"]["exact_20261114_public_resume.py"])
        public_source = public.prepare_public_source(repo, work/"public-source", report_dir)
        env = dict(os.environ, VISIBLE_SOURCE_TOPIC=str(public_source),
            PYTHONDONTWRITEBYTECODE="1", OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1",
            MKL_NUM_THREADS="1", NUMEXPR_NUM_THREADS="1")
        for token in ("GITHUB_TOKEN","GH_TOKEN","MR_TOKEN"):
            env.pop(token,None)
        emit("thirty_seven_batch_chain_start", dict(schema=SCHEMA, request=155,
            run_id=os.environ.get("GITHUB_RUN_ID"), source_commit=os.environ.get("GITHUB_SHA"),
            source_sha256=file_sha(Path(__file__)), request_sha256=file_sha(args.request),
            base_request_sha256=BASE_REQUEST_SHA, helper_sha256=HELPER_SHA,
            maximum_batches=count, chain_budget_seconds=seconds,
            between_batches_budget_does_not_interrupt_an_active_original_call=True,
            new_trajectory_from_actual98_not_a_relabelled_141_parent=True,
            initial_parent_schema=helper.PARENT_OPTIMIZER_SCHEMA,
            current_optimizer_schema=helper.OPTIMIZER_SCHEMA,
            parent=original_parent, inputs=original_inputs,
            actual_query_changes=[dict(kind="collocation-midpoint",interval=j,fraction=.5) for j in (489,490)],
            query_change_reference="original35 model",
            query_changes_from_first_actual98=[dict(kind="left-RMS",interval=463,fraction=0.17267316464601146)]+[dict(kind="collocation-midpoint",interval=j,fraction=.5) for j in (471,472,483,489,490)],
            original_damping_and_atomic_budgets_unchanged=True,
            added_capture_intervals=[489,490],added_capture_nodes=[489,490,491],unique_capture_interval_count=24,
            actual_endpoint_count=29,complete_B_local_coordinates=9805,
            previous35_endpoint_and_local_B_support_unchanged=False,
            baseline_C_and_full_H_outside_scope_unchanged=True,
            no_complete_native_or_full_BVP_acceptance_claim=True))
        started = time.monotonic()
        for batch_index in range(count):
            if time.monotonic()-started >= seconds:
                stop_reason = dict(kind="explicit_between_batches_time_budget",
                    completed_original_model_FD_pairs=len(chain_rows),
                    next_batch_not_started=True)
                break
            batch = work/f"batch-{batch_index:03d}"
            summary, output, eligible, code = run_batch(helper, reader, repo, comp, env,
                inputs, parent, input_pair, batch, batch_index, reference)
            actual_pair, fields = summary["produced_pair"], summary["output_field_identity"]
            carrier = None
            # Keep both original files here through complete readback. Actual
            # movement and its byte identity check follow the finished print.
            summary.update(batch_payload_removed=False,
                batch_payload_retirement_scheduled_after_complete_readback=True,
                next_parent_pair_temporarily_retained=False,
                next_parent_pair_movement_scheduled_after_complete_readback=bool(eligible),
                temporary_pair_is_not_an_external_checkpoint_or_published_raw=True)
            printed = print_batch(helper, reader, summary)
            if eligible:
                # Original FD and complete trial readback have both finished.
                carrier = work/f"parent-after-{batch_index:03d}"
                moved = move_pair(helper, output, carrier, actual_pair)
                last_pair, last_fields = moved, fields
            shutil.rmtree(batch)
            if eligible:
                shutil.rmtree(parent)
                parent, input_pair = carrier, moved
            emit("thirty_seven_batch_payload_retired",dict(batch_index=batch_index,
                batch_payload_removed=True,summary_identity=printed,
                complete_original_trial_readback_preceded_cleanup=True,
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
        final = dict(schema=SCHEMA, request=155, run_id=os.environ.get("GITHUB_RUN_ID"),
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
            independent37_query_definition_declared=True)
    final["all_owned_temporary_payload_removed"] = True
    final["Actions_ephemeral_Git_object_cache_not_erased_by_this_wrapper"] = True
    emit("thirty_seven_batch_chain_end", final)
    return int(final_code)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        emit("thirty_seven_batch_orchestration_failure", dict(schema=SCHEMA, progress=progress,
            error_type=type(error).__name__, error=str(error)[:800],
            scientific_success_not_inferred=True,
            previous_batch_summaries_already_printed_are_not_retracted=True,
            owned_cleanup_not_silently_claimed=True, raw_payload_uploads=0))
        traceback.print_exc()
        raise SystemExit(2)
