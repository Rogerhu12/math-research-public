#!/usr/bin/env python3
"""Request171: regenerate original37, then continue complete38 in the same job.

Run exactly eight eligible original37 model/FD pairs from the recovered
actual98 pair before attempting the38 extension. Keep the true final two
files unchanged and bind their runtime SHA values. The only new query is
LEFT-RMS462, with the actual node462 capture. Each accepted successor is
freshly modeled and FD checked. All original trial/error fields are printed
before movement or deletion; interruption leaves unread files for readback.
No original native or full-DN solve is requested.
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
SCHEMA = "same-job-original37-to38-real-pair-temporary-batches-v1"
REQUEST_SCHEMA = "same-job-original37-to38-batch-continuation-request-v1"
HELPER_NAME = "root_20261115_thirty_eight_temporary_readout.py"
HELPER_SHA = "32c2bca1cb068143dd01d99ef0eced97550fd24331a49684b66c7dad2743b80d"
BASE_REQUEST_NAME = "public-thirty-eight-same-job-recipe.json"
BASE_REQUEST_SHA = "947ace5169e6d3037ba61c561ed92a4be554f3e37b133966dd897c321e3fc890"
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
    require(file_sha(path) == HELPER_SHA, "Frozen request171 orchestration helper changed")
    spec = importlib.util.spec_from_file_location("_request171_thirty_eight_helpers", path)
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
    emit("thirty_eight_same_job_batch_scalar_identity",identity)
    if len(raw)<=SUMMARY_LIMIT:
        print("BEGIN_THIRTY_EIGHT_SAME_JOB_BATCH_SCALAR_SUMMARY",flush=True)
        sys.stdout.write(raw.decode("utf-8"))
        print("END_THIRTY_EIGHT_SAME_JOB_BATCH_SCALAR_SUMMARY",flush=True)
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
    helper.bounded_event("thirty_eight_same_job_complete_summary_stream_index",index)
    return dict(**identity,complete_selected_scalar_summary_printed=True,
        single_frame_summary_complete=False,complete_semantic_stream=stream,
        complete_original_trial_JSON_fields_preserved=True)


@contextlib.contextmanager
def owned_namespace(root):
    """Retain interrupted unread output for the following always-readback step."""
    work=Path(tempfile.mkdtemp(prefix="visible-thirty-eight-171-",dir=root))
    try:
        yield work
    except BaseException:
        emit("request171_unread_namespace_retained",dict(basename=work.name,
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
    output_name = getattr(helper, "OUTPUT_NAME", "thirty-seven-condensed-warm")
    output, fd_output = batch/output_name, batch/"physical-response"
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
            (model_path, output_name+"/model-000.json"),
            (status_path, output_name+"/driver-status.json"),
            (qp_path, output_name+"/condensed-QP-summary.json"),
            (fd_path, "physical-response/response-check.json"),
            (output/"warm-001.json.gz", output_name+"/warm-001.json.gz"))],
        original_A_AT_full_H_C_algorithms_and_budgets_unchanged=True,
        current_optimizer_schema=helper.OPTIMIZER_SCHEMA,
        complete_current_query_definition_bound=True,
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
    # This resource clock includes restoring actual98 and original sources.
    started = time.monotonic()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--request", type=Path, required=True)
    args = parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true"
        and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
        "Only this public Actions repository may execute scientific children")
    repo = args.repo_root.resolve(strict=True)
    comp = repo/TOPIC/"computations"
    request = json.loads(args.request.read_bytes())
    require(request.get("request") == 171
        and request.get("schema") == REQUEST_SCHEMA
        and request.get("repository") == REPOSITORY,
        "Use the independent request171 contract")
    require(request.get("source_sha256") == file_sha(Path(__file__)),
        "Bind this actual orchestration source")
    require(request.get("base_request_sha256") == BASE_REQUEST_SHA
        and file_sha(comp/BASE_REQUEST_NAME) == BASE_REQUEST_SHA,
        "Bind the complete source/input/phase/budget recipe")
    prefix_count = request.get("prefix_complete_model_FD_pairs")
    extension_count = request.get("maximum_extension_model_FD_pairs")
    seconds = request.get("chain_budget_seconds")
    minimum_remaining = request.get("minimum_remaining_before_original_pair_seconds")
    require(type(prefix_count) is int and prefix_count == 8,
        "Regenerate exactly eight original37 eligible pairs before the extension")
    require(type(extension_count) is int and 1 <= extension_count <= 8,
        "Declare at most eight original38 pairs")
    require(type(seconds) is int and seconds > 0
        and type(minimum_remaining) is int and 0 < minimum_remaining < seconds,
        "Declare the between-pair resource budget without changing atomic budgets")
    helper = load_helper(comp/HELPER_NAME)
    prefix_helper = helper.base
    base = json.loads((comp/BASE_REQUEST_NAME).read_bytes())
    require(base.get("request") == 171
        and base.get("schema") == "actual98-original37-to38-model-and-FD-recipe-v1"
        and base.get("parent_artifact") == prefix_helper.PARENT
        and base.get("model_flags") == helper.MODEL_FLAGS == prefix_helper.MODEL_FLAGS,
        "Retain the real actual98 pair and every original atomic scientific flag")
    original_recipe = base["original37_recipe"]
    original_recipe_path = comp/original_recipe["file"]
    original_recipe_raw = original_recipe_path.read_bytes()
    require(len(original_recipe_raw) == original_recipe["bytes"]
        and sha(original_recipe_raw) == original_recipe["sha256"],
        "The original155 source/input recipe must remain unchanged")
    prefix_recipe = json.loads(original_recipe_raw)
    require(prefix_recipe.get("request") == 155
        and prefix_recipe.get("schema") == "actual98-thirty-seven-model-and-FD-recipe-v1"
        and prefix_recipe.get("model_flags") == base["model_flags"]
        and prefix_recipe.get("parent_artifact") == base["parent_artifact"]
        and prefix_recipe.get("parent_warm") == base["parent_warm"]
        and prefix_recipe.get("parent_status") == base["parent_status"],
        "No original37 parameters, input bytes or flags are replaced")
    for family in ("source_sha256", "parameter_sha256"):
        for entry_name, digest in prefix_recipe[family].items():
            require(base[family].get(entry_name) == digest,
                "Retain the original155 source/parameter identity: "+entry_name)
        for entry_name, digest in base[family].items():
            require(Path(entry_name).name == entry_name
                and file_sha(comp/entry_name) == digest,
                "Bound original or independent source/parameter changed: "+entry_name)
    reader = helper.load("_request171_original_scalar_selectors",
        comp/helper.READER_ENTRY, helper.READER_SHA)
    runner_temp = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    chain_rows, stop_reason, final_code = [], None, 0
    last_pair, last_fields, handoff = None, None, None
    total_count = prefix_count+extension_count
    with owned_namespace(runner_temp) as work:
        inputs = work/"inputs"
        original_inputs = prefix_helper.restore_inputs(repo, inputs)
        parent = work/"parent98"
        original_parent = prefix_helper.restore_parent(comp, reader, parent, work)
        input_pair = pair_identity(prefix_helper, parent)
        report_dir = work/"source-receipts"
        report_dir.mkdir()
        public = helper.load("_request171_original_public_sources",
            comp/"exact_20261114_public_resume.py",
            base["source_sha256"]["exact_20261114_public_resume.py"])
        public_source = public.prepare_public_source(repo, work/"public-source", report_dir)
        env = dict(os.environ, VISIBLE_SOURCE_TOPIC=str(public_source),
            PYTHONDONTWRITEBYTECODE="1", OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1",
            MKL_NUM_THREADS="1", NUMEXPR_NUM_THREADS="1")
        for token in ("GITHUB_TOKEN", "GH_TOKEN", "MR_TOKEN"):
            env.pop(token, None)
        emit("thirty_eight_same_job_chain_start", dict(schema=SCHEMA, request=171,
            run_id=os.environ.get("GITHUB_RUN_ID"), source_commit=os.environ.get("GITHUB_SHA"),
            source_sha256=file_sha(Path(__file__)), request_sha256=file_sha(args.request),
            base_request_sha256=BASE_REQUEST_SHA, helper_sha256=HELPER_SHA,
            original37_recipe=original_recipe,
            prefix_complete_model_FD_pairs=prefix_count,
            maximum_extension_model_FD_pairs=extension_count,
            chain_budget_seconds=seconds, elapsed_preparation_seconds=time.monotonic()-started,
            resource_clock_includes_original_input_and_source_recovery=True,
            minimum_remaining_before_original_pair_seconds=minimum_remaining,
            between_pairs_budget_does_not_rewrite_an_active_original_call=True,
            original1200_model_and_full_original_FD_retained=True,
            outer_timeout_may_leave_an_incomplete_original_pair=True,
            new_actual98_trajectory_not_a_relabelled_deleted155_parent=True,
            parent=original_parent, inputs=original_inputs,
            initial_parent_schema=prefix_helper.PARENT_OPTIMIZER_SCHEMA,
            prefix_optimizer_schema=prefix_helper.OPTIMIZER_SCHEMA,
            extension_optimizer_schema=helper.OPTIMIZER_SCHEMA,
            extension_added_queries=[dict(kind="left-RMS", interval=462,
                fraction=.17267316464601146)],
            extension_added_capture_intervals=[462], extension_added_capture_nodes=[462],
            extension_query_count=38, extension_unique_capture_intervals=25,
            extension_endpoint_count=30, extension_complete_B_local_coordinates=10143,
            original_C_dimension=4059, complete_original_coordinates=236036,
            baseline_C_and_complete_H_outside_scope_unchanged=True,
            no_complete_native_or_full_BVP_acceptance_claim=True))
        for batch_index in range(total_count):
            phase = "original37-regeneration" if batch_index < prefix_count else "complete38-extension"
            phase_batch_index = batch_index if batch_index < prefix_count else batch_index-prefix_count
            current_helper = prefix_helper if batch_index < prefix_count else helper
            remaining = seconds-(time.monotonic()-started)
            if remaining < minimum_remaining:
                stop_reason = dict(kind="explicit_between_pairs_resource_budget",
                    next_global_batch_index=batch_index, next_phase=phase,
                    next_phase_batch_index=phase_batch_index,
                    completed_original_model_FD_pairs=sum(row["eligible"] for row in chain_rows),
                    remaining_seconds=remaining,
                    required_remaining_to_start_an_original_pair_seconds=minimum_remaining,
                    active_original_atomic_budgets_not_reduced=True,
                    next_original_pair_not_started=True,
                    not_an_original_nonlinear_or_FD_refusal=True)
                final_code = 3
                break
            if batch_index == prefix_count:
                require(len(chain_rows) == prefix_count
                    and all(row["eligible"] and row["phase"] == "original37-regeneration"
                        for row in chain_rows),
                    "The38 extension requires the eight actual same-job37 model/FD pairs")
                # Re-read bytes only. The new38 producer independently applies
                # the full original producer/status/constant-state/source binder.
                actual_pair = pair_identity(prefix_helper, parent)
                require(actual_pair == input_pair,
                    "The actual retained37 parent changed after completed FD/readback")
                parent_status = prefix_helper.read(parent/"driver-status.json")
                require(parent_status.get("schema") == prefix_helper.OPTIMIZER_SCHEMA,
                    "This handoff must still be the original37 producer")
                handoff = dict(schema="actual-same-job37-to38-pair-handoff-v1",
                    run_id=os.environ.get("GITHUB_RUN_ID"),
                    source_commit=os.environ.get("GITHUB_SHA"),
                    completed_prefix_original_model_FD_pairs=prefix_count,
                    original_parent_directory=parent.name, original_pair=actual_pair,
                    original_status_schema=parent_status.get("schema"),
                    original_status_optimization_progress=parent_status.get("optimization_progress"),
                    original_status_accepted_warm_steps=parent_status.get("accepted_warm_steps"),
                    original_status_success=parent_status.get("success"),
                    original_status_new_coupled_finite_acceptance=parent_status.get("new_coupled_finite_acceptance"),
                    last_original37_summary_identity=chain_rows[-1]["summary_identity"],
                    receiving_model_entry=helper.MODEL_ENTRY, receiving_FD_entry=helper.FD_ENTRY,
                    receiving_optimizer_schema=helper.OPTIMIZER_SCHEMA,
                    runtime_CLI_expected_warm_sha256=actual_pair["warm_sha256"],
                    runtime_CLI_expected_parent_status_sha256=actual_pair["status_sha256"],
                    neither_original_file_reserialized_or_producer_relabelled=True,
                    no_external_deleted_warm_recovered_from_SHA=True,
                    no_old_direction_or_model_reused=True,
                    new38_model_not_yet_executed=True)
                (work/"phase-handoff.json").write_bytes(encoded(handoff))
                helper.stream_complete_json("request171-real37-to38-handoff", handoff)
            progress.update(phase=phase, phase_batch_index=phase_batch_index,
                batch_index=batch_index, current_optimizer_schema=current_helper.OPTIMIZER_SCHEMA)
            (work/"chain-progress.json").write_bytes(encoded(dict(progress,
                input_pair=input_pair, completed_prefix_pairs=min(len(chain_rows), prefix_count),
                elapsed_seconds=time.monotonic()-started)))
            batch = work/f"batch-{batch_index:03d}"
            summary, output, eligible, code = run_batch(current_helper, reader, repo, comp, env,
                inputs, parent, input_pair, batch, batch_index, None)
            actual_pair, fields = summary["produced_pair"], summary["output_field_identity"]
            summary.update(phase=phase, phase_batch_index=phase_batch_index,
                complete_same_job_prefix_required_before_extension=True,
                actual37_to38_handoff=(handoff if batch_index == prefix_count else None),
                original_atomic_source_and_flags_not_relabelled=True,
                input_pair_is_current_original_file_bytes=True,
                batch_payload_removed=False,
                batch_payload_retirement_scheduled_after_complete_readback=True,
                next_parent_pair_temporarily_retained=False,
                next_parent_pair_movement_scheduled_after_complete_readback=bool(eligible),
                temporary_pair_is_not_an_external_checkpoint_or_published_raw=True)
            printed = print_batch(current_helper, reader, summary)
            carrier = None
            if eligible:
                carrier = work/f"parent-after-{batch_index:03d}"
                moved = move_pair(current_helper, output, carrier, actual_pair)
                last_pair, last_fields = moved, fields
            shutil.rmtree(batch)
            if eligible:
                shutil.rmtree(parent)
                parent, input_pair = carrier, moved
            emit("thirty_eight_same_job_payload_retired", dict(batch_index=batch_index,
                phase=phase, phase_batch_index=phase_batch_index,
                batch_payload_removed=True, summary_identity=printed,
                complete_original_trial_readback_preceded_pair_move_and_cleanup=True,
                next_actual_parent_pair_retained=bool(eligible)))
            accepted = next((row for row in summary["all_original_trials"]
                if row.get("accepted") is True), {})
            chain_rows.append(dict(batch_index=batch_index, phase=phase,
                phase_batch_index=phase_batch_index, eligible=eligible,
                input_warm_sha256=summary["input_pair"]["warm_sha256"],
                output_pair=actual_pair, field_identity=fields,
                accepted_alpha=accepted.get("alpha"),
                fixed_weight_merit_before=summary.get("fixed_weight_merit_before"),
                fixed_weight_merit_after=accepted.get("actual_fixed_weight_merit"),
                original_model_exit_code=summary["original_model_exit_code"],
                original_FD_exit_code=summary["original_FD_exit_code"],
                summary_identity=printed))
            if not eligible:
                stop_reason, final_code = dict(kind="original_pair_did_not_supply_eligible_successor",
                    phase=phase, phase_batch_index=phase_batch_index,
                    original_stop=summary["stop_reason"]), code
                break
        else:
            stop_reason = dict(kind="explicit_maximum_two_phase_batch_count",
                prefix_complete_model_FD_pairs=prefix_count,
                maximum_extension_model_FD_pairs=extension_count,
                total_original_model_FD_pairs_completed=total_count)
        if stop_reason is None:
            stop_reason = dict(kind="no_next_original_pair_started")
        row_columns = ("batch_index", "phase", "phase_batch_index", "eligible",
            "input_warm_sha256", "output_warm_sha256", "output_status_sha256",
            "field_subset_sha256", "accepted_alpha", "fixed_weight_merit_before",
            "fixed_weight_merit_after", "original_model_exit_code",
            "original_FD_exit_code", "summary_sha256")
        compact_rows = [dict(batch_index=row["batch_index"], phase=row["phase"],
            phase_batch_index=row["phase_batch_index"], eligible=row["eligible"],
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
        completed_prefix = sum(row["eligible"] and row["phase"] == "original37-regeneration"
            for row in chain_rows)
        completed_extension = sum(row["eligible"] and row["phase"] == "complete38-extension"
            for row in chain_rows)
        unvisited = [dict(global_batch_index=i,
            phase=("original37-regeneration" if i < prefix_count else "complete38-extension"),
            phase_batch_index=(i if i < prefix_count else i-prefix_count))
            for i in range(len(chain_rows), total_count)]
        final = dict(schema=SCHEMA, request=171, run_id=os.environ.get("GITHUB_RUN_ID"),
            source_commit=os.environ.get("GITHUB_SHA"), source_sha256=file_sha(Path(__file__)),
            request_sha256=file_sha(args.request), stop_reason=stop_reason,
            elapsed_seconds_including_original_source_and_input_recovery=time.monotonic()-started,
            attempted_original_pairs=len(chain_rows), completed_prefix_model_FD_pairs=completed_prefix,
            completed_extension_model_FD_pairs=completed_extension,
            original37_to38_handoff=handoff, unvisited_original_pair_suffix=unvisited,
            last_actual_completed_pair=last_pair, last_completed_field_identity=last_fields,
            original_exit_code=final_code, batch_row_columns=list(row_columns),
            batch_rows=[[row[key] for key in row_columns] for row in compact_rows],
            no_cross_model_fixed_weight_merit_subtraction=True,
            all_models_recomputed_from_the_actual_previous_pair=True,
            complete38_is_not_a_relabelled_original37_model=True,
            final_field_not_recoverable_from_hash_alone=True,
            maximum_declared_pair_count_not_guaranteed_by_wall_time=True,
            success=False, new_coupled_finite_acceptance=False,
            nonlinear_native_or_full_DN_called=False,
            raw_payload_uploads=0, Release_uploads=0, Git_data_publication=0,
            all_original_scientific_sources_preserved=True,
            original_acceptance_gates_unchanged=True)
        # This complete bounded final record is printed before namespace cleanup.
        helper.stream_complete_json("request171-complete-chain-end-before-cleanup", final)
    final["all_owned_temporary_payload_removed"] = True
    final["Actions_ephemeral_Git_object_cache_not_erased_by_this_wrapper"] = True
    emit("thirty_eight_same_job_chain_end", final)
    return int(final_code)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        emit("thirty_eight_same_job_orchestration_failure",
            dict(schema=SCHEMA, progress=progress, error_type=type(error).__name__,
                error=str(error)[:800], scientific_success_not_inferred=True,
                previous_original_summaries_already_printed_are_not_retracted=True,
                owned_cleanup_not_silently_claimed=True, raw_payload_uploads=0))
        traceback.print_exc()
        raise SystemExit(2)
