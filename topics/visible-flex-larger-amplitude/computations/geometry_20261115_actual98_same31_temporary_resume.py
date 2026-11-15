#!/usr/bin/env python3
"""Request107: one unchanged same31 model/FD; temporary inputs and outputs only."""
from __future__ import annotations
import argparse
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time
import zipfile

REPOSITORY = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-larger-amplitude"
SCHEMA = "actual98-same31-one-model-temporary-orchestration-v1"
OPTIMIZER_SCHEMA = "exact-constraint-thirty-one-query-condensed-complete-H-warm-v1"
HISTORICAL_SOURCE = "918fdb11dbb7a424b6149b405e2c7fab3cc0c737"
PARENT = dict(run_id=43677587785, artifact_id=14147700690,
    artifact_name="visible-followup-condensedqp-43677587785-1",
    expected_size=809042943,
    expected_sha256="9917774d965e86b0a8d46677a1f54c0fb23fc8fa61a67cbab998e7493d33151a")
PARENT_MEMBERS = {
    "warm-001.json.gz": ("thirty-one-condensed-warm/warm-001.json.gz",
        4927052, "b59f40c003bf924f3f3c10aa6783425a606b3e395fd86311cbba159b835feb67"),
    "driver-status.json": ("thirty-one-condensed-warm/driver-status.json",
        3379453, "b7ad389fad867fecf85edc4313145980d6e8686f207acf781ff6a050e7eae6ff"),
}
INPUTS = {
    "accepted.json.gz": (
        "notes/public-actions-43580643038-1-free3/stage-00/actual.json.gz",
        "b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff"),
    "prepared.json.gz": (
        "notes/public-actions-43588155190-1-prepare112/preparation112/prepared.json.gz",
        "0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714"),
    "tail-anchor.json.gz": (
        "notes/public-actions-43592195185-1-coupling112banded/full-DN112/outer-00-anchor-tail.json.gz",
        "e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51"),
    "tail-config.json": (
        "notes/public-actions-43588155190-1-prepare112/T112-config.json",
        "01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5"),
}
MODEL_ENTRY = "geometry_20261114_thirty_one_query_collocation_observer_warm.py"
FD_ENTRY = "geometry_20261114_thirty_one_query_condensed_response.py"
READER_ENTRY = "root_20261115_read_existing98_scalar_summary.py"
READER_SHA = "e2e8ec32c30bbc9ff0e77709524ff09f100f0ff5f4decd23c43b6445562b7484"
TRANSPORT_ENTRY = "exact_20261114_fetch_pinned_public_artifact.py"
TRANSPORT_SHA = "51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859"
MODEL_FLAGS = [
    "--iterations", "1", "--damping", "270", "--lsmr-iterations", "200",
    "--projection-sweeps", "200", "--line-search-steps", "17",
    "--budget-seconds", "1200", "--angles", "4096", "--jac-workers", "2",
    "--condensed-budget-seconds", "600", "--condensed-trial-reserve-seconds", "90",
    "--condensed-recovery-reserve-seconds", "30", "--condensed-max-working", "512",
    "--condensed-dual-sweeps", "200", "--condensed-store-root",
]
SCIENTIFIC_MODEL_FIELDS = (
    "iteration", "before", "fixed_weight_merit_before", "damping",
    "accepted", "trials", "actual_coefficient_direction_max",
)
progress = dict(schema=SCHEMA, phase="source-and-argument-binding",
    scientific_calls_started=False, new_native_or_full_DN_call=False)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def file_sha(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def require(ok, message):
    if not ok:
        raise ValueError(message)


def load(name, path, expected=None):
    raw = path.read_bytes()
    if expected is not None:
        require(sha(raw) == expected, "Frozen source identity changed: " + path.name)
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def read(path):
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw,
        parse_constant=lambda x: {"original_nonfinite_JSON_token": x})


def emit(event, value):
    print(json.dumps(dict(event=event, **value), ensure_ascii=True,
        separators=(",", ":"), allow_nan=False), flush=True)


def restore_inputs(repo, destination):
    destination.mkdir()
    result = []
    for name, (relative, digest) in INPUTS.items():
        # This commit was explicitly fetched before this orchestrator. The
        # public Git object may be lazily fetched; no working-tree ref is changed.
        original_path = TOPIC + "/" + relative
        raw = subprocess.check_output([
            "git", "-C", str(repo), "show", HISTORICAL_SOURCE+":"+original_path])
        require(sha(raw) == digest, "Original mathematical input changed: " + name)
        target = destination/name
        with target.open("xb") as stream:
            stream.write(raw)
        result.append(dict(file=name, historical_path=original_path,
            historical_commit=HISTORICAL_SOURCE, bytes=len(raw), sha256=digest))
    return result


def restore_parent(comp, reader, destination, work):
    require(os.environ.get("GITHUB_TOKEN"), "Actions read token is required")
    transport = reader.load_transport(comp/TRANSPORT_ENTRY)
    require(transport.PIN == PARENT, "Use only the completed original98 artifact")
    opener = transport.make_opener()
    metadata, canonical = transport.read_metadata(opener, os.environ["GITHUB_TOKEN"])
    require(metadata["workflow_run"].get("head_sha") == HISTORICAL_SOURCE,
        "Original98 artifact source mismatch")
    archive_path = work/"original98.zip"
    downloaded = transport.download_archive(
        opener, os.environ["GITHUB_TOKEN"], canonical, archive_path, {})
    destination.mkdir()
    members = []
    try:
        with zipfile.ZipFile(archive_path, "r") as archive:
            index, count = reader.zip_index(archive, transport)
            for name, (suffix, length, digest) in PARENT_MEMBERS.items():
                matching = [entry for path, entry in index.items()
                            if path == suffix or path.endswith("/"+suffix)]
                require(len(matching) == 1, "Exactly one original parent member: " + name)
                entry = matching[0]
                require(entry.file_size == length, "Original parent member size: " + name)
                raw = archive.read(entry)
                require(len(raw) == length and sha(raw) == digest,
                    "Original parent member bytes: " + name)
                with (destination/name).open("xb") as stream:
                    stream.write(raw)
                members.append(dict(file=name, bytes=length, sha256=digest,
                    original_member_CRC_checked=True, JSON_reserialized=False))
        status = read(destination/"driver-status.json")
        require(status.get("schema") == OPTIMIZER_SCHEMA
            and status.get("accepted_warm_steps") == 1
            and status.get("optimization_progress") is True
            and status.get("success") is False
            and status.get("new_coupled_finite_acceptance") is False
            and status.get("latest_warm_file") == "warm-001.json.gz"
            and status.get("latest_warm_sha256") == PARENT_MEMBERS["warm-001.json.gz"][2],
            "Use the real completed but unaccepted actual98 pair")
        return dict(artifact=PARENT, complete_ZIP_bytes_and_SHA=downloaded,
            selected_members=members, central_directory_entries=count,
            unused_members_not_decompressed_or_audited=True,
            parent_not_an_accepted_native_or_full_DN_anchor=True)
    finally:
        archive_path.unlink(missing_ok=True)


def primitive_fields(reader, obj):
    return reader.shallow(obj) if isinstance(obj, dict) else None


def angle_record(row):
    """All original selected query records, without repeated source descriptors."""
    beta = row.get("original_beta_squared", {})
    return dict(query_index=row.get("query_index"), kind=row.get("kind"),
        interval=row.get("interval"), fraction=row.get("fraction"),
        station=row.get("station"), input_finite=row.get("original_query_input_finite"),
        beta_squared={k:beta[k] for k in (
            "minimum", "angle_index", "phi", "negative_count", "zero_count",
            "finite_count", "nonfinite_count") if k in beta})


def domain_record(reader, report, detailed=False):
    if not isinstance(report, dict):
        return None
    answer = {key:report[key] for key in (
        "node_domain_failures", "midpoint_domain_failures", "boundary_finite", "finite",
        "original_uniform_phi_rho_guard_valid", "original_rho_guard_angles",
        "original_uniform_phi_rho_min", "boundary_domain_error",
        "complete_trial_RHS_recomputed", "all_core_states_identical",
        "all_control_states_identical", "left_residual_max",
        "physical_collocation_max", "complete_boundary_max", "constant_collocation_max",
        "original_RMS_query_domain_failures") if key in report}
    answer["RMS_checks_present"] = "original_RMS_query_checks" in report
    if "original_RMS_query_checks" in report:
        columns = ("interval", "s", "left", "right", "minimum_beta_squared",
                   "phi", "a", "ap", "app", "curve_curvature_at_minimum")
        answer["RMS_failed_point_columns"] = list(columns)
        answer["RMS_checks"] = [
            dict(**reader.shallow(row), first_invalid_point_rows=[
                [point.get(key) for key in columns]
                for point in row.get("first_invalid_points", [])])
            for row in report["original_RMS_query_checks"]]
    mid = report.get("read_only_midpoint_observer")
    if isinstance(mid, dict):
        answer["bad_midpoint_indices"] = mid.get("bad_midpoint_indices")
        answer["midpoint_observer_changed_original_result"] = mid.get(
            "original_returned_finite_or_merit_changed")
        answer["midpoint_failed_point_columns"] = ["interval", "station",
            "left", "right", "middle_input_finite", "classification",
            "beta_squared_minimum", "phi", "angle_index", "negative_count",
            "nonfinite_count"]
        answer["midpoint_failed_point_rows"] = [
            [point.get(key) for key in ("interval", "station", "left", "right",
                "middle_input_finite", "classification")] +
            [point.get("original_beta_squared", {}).get(key) for key in (
                "minimum", "phi", "angle_index", "negative_count", "nonfinite_count")]
            for point in mid.get("points", [])]
    col = report.get("read_only_collocation_location_observer", {})
    if isinstance(col.get("full_physical_argmax"), dict):
        answer["physical_argmax"] = reader.point_readout(col["full_physical_argmax"])
    return answer


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
    queries = ((model or {}).get("thirty_one_query_projection_entry") or {}).get("query_specs")
    if queries is None:
        queries = ((status.get("identity") or {}).get("thirty_one_query_projection_entry") or {}).get("query_specs")
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
        actual_added_queries_this_request=[],
        frozen_entry_added_query_labels_refer_to_its_original94_to98_introduction=True,
        native_at_current_height_solved=False, new_full_DN_acceptance=False)


def run_child(label, command, repo, env, work):
    path = work/(label+".log")
    started = time.monotonic()
    with path.open("wb") as stream:
        result = subprocess.run(command, cwd=repo, env=env, stdout=stream,
                                stderr=subprocess.STDOUT, check=False)
    report = dict(label=label, command=list(map(str, command)), exit_code=result.returncode,
        elapsed_seconds=time.monotonic()-started, log_bytes=path.stat().st_size,
        log_sha256=file_sha(path), log_temporary_only=True)
    if result.returncode:
        with path.open("rb") as stream:
            stream.seek(max(0, path.stat().st_size-4096))
            report["original_failure_log_tail"] = stream.read().decode("utf-8", errors="replace")
    emit("original_child_finished", report)
    return result.returncode


def output_receipt(path, relative):
    if not path.is_file():
        return dict(file=relative, present=False)
    return dict(file=relative, present=True, bytes=path.stat().st_size,
                sha256=file_sha(path), retained=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--request", type=Path, required=True)
    args = parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true"
        and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
        "All scientific work belongs to the public repository Actions")
    repo = args.repo_root.resolve(strict=True)
    comp = repo/TOPIC/"computations"
    request = json.loads(args.request.read_bytes())
    require(request.get("request") == 107 and request.get("repository") == REPOSITORY,
        "Use the explicit one-model request107")
    require(request.get("parent_artifact") == PARENT
        and request.get("model_flags") == MODEL_FLAGS,
        "Do not alter the original source parent or scientific budgets")
    for name, digest in request["source_sha256"].items():
        require(Path(name).name == name and file_sha(comp/name) == digest,
            "Exact consumed source identity: " + name)
    for name, digest in request["parameter_sha256"].items():
        require(Path(name).name == name and file_sha(comp/name) == digest,
            "Exact original parameter manifest: " + name)
    reader = load("_request107_original_scalar_selectors", comp/READER_ENTRY, READER_SHA)
    require(file_sha(comp/TRANSPORT_ENTRY) == TRANSPORT_SHA, "Original transport identity")
    runner_temp = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    summary = None
    final_code = 2
    with tempfile.TemporaryDirectory(prefix="visible-same31-107-", dir=runner_temp) as temporary:
        work = Path(temporary)
        progress["phase"] = "original98-parent-and-four-input-bytes"
        inputs = restore_inputs(repo, work/"inputs")
        parent = restore_parent(comp, reader, work/"parent98", work)
        progress["parent_bytes_verified"] = True
        emit("actual107_parent_and_original_inputs", dict(parent=parent, inputs=inputs,
            source_sha256=file_sha(Path(__file__)),
            request_sha256=file_sha(args.request), no_parent_JSON_reserialization=True))
        report_dir = work/"source-receipts"
        report_dir.mkdir()
        public = load("_request107_public_source_restore",
                      comp/"exact_20261114_public_resume.py",
                      request["source_sha256"]["exact_20261114_public_resume.py"])
        source = public.prepare_public_source(repo, work/"public-source", report_dir)
        env = dict(os.environ, VISIBLE_SOURCE_TOPIC=str(source),
            PYTHONDONTWRITEBYTECODE="1", OPENBLAS_NUM_THREADS="1",
            OMP_NUM_THREADS="1", MKL_NUM_THREADS="1", NUMEXPR_NUM_THREADS="1")
        paths = work/"inputs"
        output = work/"thirty-one-condensed-warm"
        fd_output = work/"physical-response"
        command = [sys.executable, "-u", str(comp/MODEL_ENTRY),
            "--accepted", str(paths/"accepted.json.gz"),
            "--prepared", str(paths/"prepared.json.gz"),
            "--tail-anchor", str(paths/"tail-anchor.json.gz"),
            "--tail-config", str(paths/"tail-config.json"),
            "--resume", str(work/"parent98/warm-001.json.gz"),
            "--expected-resume-sha", PARENT_MEMBERS["warm-001.json.gz"][2],
            "--parent-status", str(work/"parent98/driver-status.json"),
            "--expected-parent-status-sha", PARENT_MEMBERS["driver-status.json"][2],
            "--out", str(output), *MODEL_FLAGS]
        progress.update(phase="original-one-model", scientific_calls_started=True)
        model_code = run_child("original-model", command, repo, env, work)
        status_path, model_path = output/"driver-status.json", output/"model-000.json"
        status = read(status_path) if status_path.is_file() else {}
        model = read(model_path) if model_path.is_file() else None
        qp_path = output/"condensed-QP-summary.json"
        qp = read(qp_path) if qp_path.is_file() else None
        fd_code, fd = None, None
        warm_name = status.get("latest_warm_file")
        if (model_code == 0 and status.get("schema") == OPTIMIZER_SCHEMA
                and status.get("optimization_progress") is True
                and status.get("accepted_warm_steps") == 1):
            require(warm_name == "warm-001.json.gz", "Original single-model warm filename")
            require(file_sha(output/warm_name) == status["latest_warm_sha256"],
                    "Original accepted-warm output identity")
            progress["phase"] = "original-complete-new-warm-boundary-FD"
            fd_command = [sys.executable, "-u", str(comp/FD_ENTRY),
                "--accepted", str(paths/"accepted.json.gz"),
                "--prepared", str(output/warm_name),
                "--tail-anchor", str(paths/"tail-anchor.json.gz"),
                "--tail-config", str(paths/"tail-config.json"),
                "--out", str(fd_output), "--angles", "4096"]
            fd_code = run_child("original-boundary-FD", fd_command, repo, env, work)
            fd_path = fd_output/"response-check.json"
            fd = read(fd_path) if fd_path.is_file() else None
        summary = summarize(reader, model, status, qp, fd)
        summary.update(schema=SCHEMA, run_id=os.environ.get("GITHUB_RUN_ID"),
            source_commit=os.environ.get("GITHUB_SHA"),
            source_sha256=file_sha(Path(__file__)), request_sha256=file_sha(args.request),
            parent_artifact=PARENT, parent_members=parent["selected_members"],
            original_model_exit_code=model_code, original_FD_exit_code=fd_code,
            primary_outputs=[output_receipt(path, relative) for path, relative in (
                (model_path, "thirty-one-condensed-warm/model-000.json"),
                (status_path, "thirty-one-condensed-warm/driver-status.json"),
                (qp_path, "thirty-one-condensed-warm/condensed-QP-summary.json"),
                (fd_output/"response-check.json", "physical-response/response-check.json"),
                (output/"warm-001.json.gz", "thirty-one-condensed-warm/warm-001.json.gz"))],
            parent_producer_not_rewritten=True,
            original_model_and_boundary_sources_not_patched=True,
            raw_arrays_not_independently_reaudited=True,
            full_factor_not_claimed_independently_exported_or_checked=True,
        raw_payload_uploads=0, Release_uploads=0, Git_data_publication=0,
        all_available_original_trial_and_failure_scalar_rows_selected=True,
        summary_scope="All original trial flags, selected minima/counts and actual failed-point scalar rows; not raw reports or arrays",
        frozen_report_storage_words_do_not_describe_this_workflows_retention=True)
        final_code = model_code if model_code else (fd_code if fd_code is not None else 2)
    # Both original child processes have exited. Delete only this owned
    # temporary tree, never any working source or another request's output.
    summary["all_owned_temporary_payload_removed"] = True
    encoded = (json.dumps(summary, ensure_ascii=True, separators=(",", ":"),
                           allow_nan=False)+"\n").encode("utf-8")
    emit("actual107_scalar_summary_identity", dict(bytes=len(encoded), sha256=sha(encoded),
        original_child_exit_code_retained=final_code,
        output_size_is_not_a_new_scientific_acceptance_test=True))
    if len(encoded) <= 90000:
        print("BEGIN_ACTUAL107_SCALAR_SUMMARY", flush=True)
        sys.stdout.write(encoded.decode("utf-8"))
        print("END_ACTUAL107_SCALAR_SUMMARY", flush=True)
    else:
        # Never split or retain a raw/oversized report. This fallback names
        # omissions and keeps the actual science status and all trial decisions.
        reduced = dict(schema=SCHEMA, original_summary_bytes=len(encoded),
            original_summary_sha256=sha(encoded), optional_detail_not_printed=True,
            scalar_summary_complete=False,
            all_original_trial_query_and_failed_point_details_printed=False,
            status=summary["status"], original_model_exit_code=summary["original_model_exit_code"],
            original_FD_exit_code=summary["original_FD_exit_code"],
            primary_outputs=summary["primary_outputs"], FD=summary["FD"],
            fixed_weight_merit_before=summary["fixed_weight_merit_before"],
            all_trial_scalars=[reader.shallow(x) for x in summary["all_original_trials"]],
            nearest_original_trial_index=summary["nearest_rejected_original_trial_index"],
            all_owned_temporary_payload_removed=True)
        emit("actual107_explicit_scalar_only_fallback", reduced)
    return int(final_code)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        # TemporaryDirectory still cleans its owned payload on every exception.
        emit("actual107_orchestration_failure", dict(progress=progress,
            error_type=type(error).__name__, error=(str(error)[:600]
                if isinstance(error, (ValueError, TypeError, FileNotFoundError)) else type(error).__name__),
            scientific_success_not_inferred=True, raw_payload_uploads=0,
            owned_temporary_cleanup_not_silently_claimed=True))
        raise SystemExit(2)
