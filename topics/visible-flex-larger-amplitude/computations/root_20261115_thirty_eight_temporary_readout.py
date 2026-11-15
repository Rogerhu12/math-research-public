#!/usr/bin/env python3
"""Request171 complete original37/38 scalar and interrupted-output readout.

This is a byte/JSON transport adapter, without model arithmetic. Restore
actual98 through the unchanged request155 helper; preserve the true same-job
37-to38 handoff. Read every surviving original trial and error before cleanup.
The request155 semantic stream protocol is reused explicitly as transport.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import os
from pathlib import Path
import sys

BASE_HELPER_NAME = "root_20261115_thirty_seven_temporary_readout.py"
BASE_HELPER_SHA = "f5d598cdde4c46d2904eea2ef0d20b6009e8eb284ee9a2f6f18d20cbdfc582b7"
base_path = Path(__file__).resolve().parent/BASE_HELPER_NAME
if hashlib.sha256(base_path.read_bytes()).hexdigest() != BASE_HELPER_SHA:
    raise ValueError("The original request155 byte/JSON helper changed")
spec = importlib.util.spec_from_file_location("_request171_original155_readout", base_path)
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)

REPOSITORY = base.REPOSITORY
TOPIC = base.TOPIC
SCHEMA = "same-job37-to38-temporary-source-and-scalar-support-v1"
PARENT_OPTIMIZER_SCHEMA = base.OPTIMIZER_SCHEMA
OPTIMIZER_SCHEMA = "exact-constraint-thirty-eight-query-condensed-complete-H-warm-v1"
OUTPUT_NAME = "thirty-eight-condensed-warm"
MODEL_ENTRY = "geometry_20261115_thirty_eight_query_collocation_observer_warm.py"
FD_ENTRY = "geometry_20261115_thirty_eight_query_condensed_response.py"
MODEL_FLAGS = base.MODEL_FLAGS
SCIENTIFIC_MODEL_FIELDS = base.SCIENTIFIC_MODEL_FIELDS
READER_ENTRY, READER_SHA = base.READER_ENTRY, base.READER_SHA
PARENT, INPUTS = base.PARENT, base.INPUTS
sha, file_sha, require = base.sha, base.file_sha, base.require
load, read, emit = base.load, base.read, base.emit
restore_inputs, restore_parent = base.restore_inputs, base.restore_parent
run_child, output_receipt = base.run_child, base.output_receipt
stream_bytes, stream_complete_json = base.stream_bytes, base.stream_complete_json
canonical, bounded_event = base.canonical, base.bounded_event
primitive_fields, angle_record, domain_record = base.primitive_fields, base.angle_record, base.domain_record

def summarize(reader, model, status, qp, fd):
    trials = model.get("trials", []) if isinstance(model, dict) else []
    accepted_indices = [i for i, row in enumerate(trials) if row.get("accepted") is True]
    nearest = (accepted_indices[0]-1 if accepted_indices and accepted_indices[0] > 0
               else (len(trials)-1 if trials and not accepted_indices else None))
    records = []
    for i, row in enumerate(trials):
        item = dict(original_trial_index=i, **reader.shallow(row))
        item["domain"] = domain_record(reader, row.get("domain"), i == nearest)
        item["RMS_stage_present"] = "complete_original_RMS_query_domain" in row
        item["complete_original_RMS_query_domain"] = domain_record(
            reader, row.get("complete_original_RMS_query_domain"), i == nearest)
        for key in ("selected_linear_beta_squared", "all_selected_linear_reserve_slack"):
            item[key] = primitive_fields(reader, row.get(key))
        selected = row.get("actual_selected_original_angles", [])
        # Query definition appears once. These parallel lists retain every
        # actual selected row in its original order without repeating metadata.
        item["selected_query_count"] = len(selected)
        item["selected_query_indices"] = [x.get("query_index") for x in selected]
        item["selected_beta_squared_minima"] = [
            x.get("original_beta_squared", {}).get("minimum") for x in selected]
        item["selected_negative_angle_counts"] = [
            x.get("original_beta_squared", {}).get("negative_count") for x in selected]
        item["selected_nonfinite_angle_counts"] = [
            x.get("original_beta_squared", {}).get("nonfinite_count") for x in selected]
        if i == nearest:
            item["nearest_failed_selected_queries"] = [
                angle_record(x) for x in selected if
                x.get("original_beta_squared", {}).get("negative_count", 0) != 0 or
                x.get("original_beta_squared", {}).get("nonfinite_count", 0) != 0]
        records.append(item)
    embedded = (status.get("iterations") or [None])[0]
    same_fields = {}
    if isinstance(model, dict) and isinstance(embedded, dict):
        for field in SCIENTIFIC_MODEL_FIELDS:
            same_fields[field] = dict(present_in_both=field in model and field in embedded,
                equal=model.get(field) == embedded.get(field))
    queries = ((model or {}).get("thirty_eight_query_projection_entry") or {}).get("query_specs")
    if queries is None:
        queries = ((status.get("identity") or {}).get("thirty_eight_query_projection_entry") or {}).get("query_specs")
    return dict(status=reader.shallow(status),
        model_before=domain_record(reader, (model or {}).get("before")),
        fixed_weight_merit_before=(model or {}).get("fixed_weight_merit_before"),
        model_damping=(model or {}).get("damping"),
        model_accepted=(model or {}).get("accepted"),
        original_typed_queries=queries, all_original_trials=records,
        nearest_rejected_original_trial_index=nearest,
        QP=reader.qp_readout(qp) if isinstance(qp, dict) else None,
        FD=reader.fd_readout(fd) if isinstance(fd, dict) else None,
        status_standalone_model_science_fields=same_fields,
        standalone_document_provenance_not_required_equal_to_nested_model=True,
        model_relation_readout_is_not_a_new_scientific_gate=True,
        no_cross_model_weighted_merit_subtraction=True,
        actual_added_queries_this_request=[dict(kind="left-RMS",interval=462,fraction=.17267316464601146)],
        query_addition_reference="the complete original37 pair generated in this same job",
        query_definition_origin="request171-original37-plus-full-LEFT462-after-eight-real37-pairs",
        query_changes_since_this_model_input=([dict(kind="left-RMS",interval=462,fraction=.17267316464601146)]
            if ((status.get("identity") or {}).get("thirty_eight_query_projection_entry") or {}).get("parent_optimizer_schema")==PARENT_OPTIMIZER_SCHEMA else []),
        initial_parent_is_real_same_job37_not_removed_actual155=True,
        original_twenty_one_LEFT_and_sixteen_MID_queries_retained=True,
        added_capture_intervals=[462],added_capture_nodes=[462],
        complete_B_endpoint_and_local_support_changed=True,
        baseline_C_and_complete_H_outside_scope_unchanged=True,
        complete_original_trial_JSON_records=trials,
        complete_original_status_iteration_trial_JSON_records=[
            dict(original_iteration_index=i,trials=entry.get("trials",[]))
            for i,entry in enumerate(status.get("iterations") or []) if isinstance(entry,dict)],
        complete_trial_JSON_is_original_parsed_value_not_a_new_evaluation=True,
        scientific_arrays_in_separate_raw_files_are_not_recreated_or_logged=True,
        native_at_current_height_solved=False, new_full_DN_acceptance=False)



def readback_only(argv=None):
    """All actual surviving original37 and38 files; never rerun science."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--readback-only", action="store_true", required=True)
    parser.add_argument("--temporary-root", type=Path, required=True)
    parser.add_argument("--code-directory", type=Path, required=True)
    args = parser.parse_args(argv)
    require(os.environ.get("GITHUB_ACTIONS") == "true"
        and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
        "Read existing output only in this public Actions job")
    root = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    require(args.temporary_root.resolve(strict=True) == root,
        "Only this job RUNNER_TEMP is scanned")
    require(args.code_directory.resolve(strict=True) == Path(__file__).resolve().parent,
        "Use the bound source directory")
    reader = load("_request171_pure_scalar_selectors",
        args.code_directory/READER_ENTRY, READER_SHA)
    recovered, errors = [], []
    for work in sorted(root.glob("visible-thirty-eight-171-*")):
        require(not work.is_symlink() and work.resolve().is_relative_to(root),
            "Owned request171 namespace only")
        if not work.is_dir():
            continue
        for batch in sorted(work.glob("batch-*")):
            require(not batch.is_symlink() and batch.resolve().is_relative_to(work),
                "Owned original batch only")
            if not batch.is_dir():
                continue
            for output_name, scalar_reader in (
                ("thirty-seven-condensed-warm", base.summarize),
                ("thirty-eight-condensed-warm", summarize)):
                output = batch/output_name
                if not output.exists():
                    continue
                require(not output.is_symlink() and output.resolve().is_relative_to(batch),
                    "Owned original output only")
                named = [("model", output/"model-000.json"),
                    ("status", output/"driver-status.json"),
                    ("qp", output/"condensed-QP-summary.json"),
                    ("fd", batch/"physical-response/response-check.json")]
                values, identities, local_errors = {}, [], []
                for key, path in named:
                    values[key] = None
                    if not path.is_file():
                        continue
                    identities.append(dict(file=path.relative_to(work).as_posix(),
                        bytes=path.stat().st_size, sha256=file_sha(path)))
                    try:
                        values[key] = read(path)
                    except Exception as error:
                        local_errors.append(dict(file=path.relative_to(work).as_posix(),
                            error=repr(error)))
                        stream_bytes(work.name+"/"+path.relative_to(work).as_posix(), path)
                if identities:
                    status = values["status"] if isinstance(values["status"], dict) else {}
                    try:
                        report = scalar_reader(reader, values["model"], status,
                            values["qp"], values["fd"])
                        report.update(actual_surviving_batch=batch.name,
                            actual_output_directory=output_name,
                            actual_namespace=work.name, original_files=identities,
                            readback_errors=local_errors,
                            no_process_exit_or_missing_phase_inferred=True,
                            readback_only=True, no_scientific_replay=True,
                            no_warm_reconstruction=True)
                        record = stream_complete_json(
                            work.name+"/"+batch.name+"/"+output_name+"/interrupted-original-readout",
                            report)
                        recovered.append(dict(namespace=work.name, batch=batch.name,
                            output_directory=output_name, readback=record))
                    except Exception as error:
                        errors.append(dict(namespace=work.name, batch=batch.name,
                            output_directory=output_name, error=repr(error),
                            original_report_bytes_forwarded_below=True))
                        for key, path in named:
                            if path.is_file():
                                stream_bytes(work.name+"/"+path.relative_to(work).as_posix(), path)
            for logfile in sorted(batch.glob("*.log")):
                if logfile.is_file() and not logfile.is_symlink():
                    stream_bytes(work.name+"/"+logfile.relative_to(work).as_posix(), logfile)
        # A move may have completed only one file. Read the real status wherever
        # it survived, without inferring successful FD, handoff or acceptance.
        for carrier in sorted(work.glob("parent-after-*")):
            require(not carrier.is_symlink() and carrier.resolve().is_relative_to(work),
                "Owned actual pair carrier only")
            if not carrier.is_dir():
                continue
            path = carrier/"driver-status.json"
            if not path.is_file():
                continue
            identity = dict(file=path.relative_to(work).as_posix(),
                bytes=path.stat().st_size, sha256=file_sha(path))
            try:
                status = read(path)
                require(isinstance(status, dict), "Original status must remain an object")
                if status.get("schema") == base.OPTIMIZER_SCHEMA:
                    scalar_reader = base.summarize
                elif status.get("schema") == OPTIMIZER_SCHEMA:
                    scalar_reader = summarize
                else:
                    raise ValueError("Unexpected original status schema; preserve its bytes")
                report = scalar_reader(reader, None, status, None, None)
                report.update(actual_surviving_parent_carrier=carrier.name,
                    actual_namespace=work.name, original_status_file=identity,
                    original_trial_source="original driver-status iterations; not a recreated model",
                    warm_file_if_present=output_receipt(carrier/"warm-001.json.gz",
                        carrier.name+"/warm-001.json.gz"),
                    readback_only=True, no_scientific_replay=True,
                    no_model_success_FD_success_or_completed_handoff_inferred=True,
                    previous_complete_batch_readout_may_also_exist=True)
                record = stream_complete_json(
                    work.name+"/"+carrier.name+"/original-status-trials", report)
                recovered.append(dict(namespace=work.name, parent_carrier=carrier.name,
                    readback=record))
            except Exception as error:
                errors.append(dict(namespace=work.name, parent_carrier=carrier.name,
                    error=repr(error), original_status_bytes_forwarded_below=True))
                stream_bytes(work.name+"/"+path.relative_to(work).as_posix(), path)
        # Small orchestration receipts can survive a failure after the phase change.
        for name in ("phase-handoff.json", "chain-progress.json"):
            path = work/name
            if path.is_file() and not path.is_symlink():
                try:
                    record = stream_complete_json(work.name+"/"+name, read(path))
                    recovered.append(dict(namespace=work.name, orchestration_file=name,
                        readback=record))
                except Exception as error:
                    errors.append(dict(namespace=work.name, file=name, error=repr(error)))
                    stream_bytes(work.name+"/"+name, path)
    stream_complete_json("request171-surviving-output-readback",
        dict(recovered=recovered, errors=errors, readback_only=True,
            scientific_acceptance_not_inferred=True,
            no_surviving_batch_does_not_mean_a_scientific_success=True,
            this_reader_does_not_delete_any_original_file=True))
    return 0 if not errors else 70


if __name__ == "__main__":
    raise SystemExit(readback_only())
