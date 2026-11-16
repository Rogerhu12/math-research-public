#!/usr/bin/env python3
"""Request206 original39 restoration and one necessary chain after actual200 overflow.

The original complete31 parent is restored with unchanged pinned transport.
The independent complete39 trajectory retains all38 and adds RIGHT-RMS459.
No RHS, matrix, norm, derivative or acceptance arithmetic occurs here.
All actual batches have ONE whole-chain necessary scalar/trial document.
Only repeated names and identical source/parameter receipts are shared;
explicit addressed tables contain the already selected necessary scalars.
The document must fit90000 bytes, otherwise transport remains incomplete70.
Per-batch necessary records remain temporary until that print. Full scientific JSON/arrays stay temporary and are never split,
encoded or reconstructed through stdout. Overflow is transport incomplete70;
unread output remains until the always-readback step or runner destruction.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import tempfile
import time
import zipfile

REPOSITORY = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-larger-amplitude"
SCHEMA = "actual98-thirty-nine-tabular-necessary-source-and-scalar-support-v1"
PARENT_OPTIMIZER_SCHEMA = "exact-constraint-thirty-one-query-condensed-complete-H-warm-v1"
OPTIMIZER_SCHEMA = "exact-constraint-thirty-nine-query-condensed-complete-H-warm-v1"
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
MODEL_ENTRY = "geometry_20261115_thirty_nine_query_collocation_observer_warm.py"
FD_ENTRY = "geometry_20261115_thirty_nine_query_condensed_response.py"
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
        require(status.get("schema") == PARENT_OPTIMIZER_SCHEMA
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



SUMMARY_LIMIT = 90000
ERROR_TEXT_LIMIT = 64000
NAMESPACE_PREFIX = "visible-thirty-nine-206-"

OWNER_FILE = NAMESPACE_PREFIX+"owner.json"
OWNER_CHILDREN_FILE = NAMESPACE_PREFIX+"child-identities.jsonl"
OWNER_QUIET_FILE = NAMESPACE_PREFIX+"quiet.json"


def process_identity(pid):
    """Linux identity only; never read argv or environment/token bytes."""
    try:
        raw=(Path("/proc")/str(pid)/"stat").read_text()
    except (FileNotFoundError,ProcessLookupError):
        return None
    fields=raw.rsplit(")",1)[1].split()
    return dict(pid=int(pid),state=fields[0],ppid=int(fields[1]),
        pgid=int(fields[2]),sid=int(fields[3]),start_ticks=int(fields[19]))


def owner_paths():
    root=Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    return root,root/OWNER_FILE,root/OWNER_CHILDREN_FILE,root/OWNER_QUIET_FILE


def owner_binding(comp,record):
    request_path=comp/"public-thirty-nine-tabular-batch-request.json"
    request=read(request_path)
    source=comp/"geometry_20261116_thirty_nine_tabular_batches.py"
    require(record.get("schema")=="request206-exclusive-session-owner-v1"
        and record.get("repository")==REPOSITORY
        and record.get("run_id")==os.environ.get("GITHUB_RUN_ID")
        and record.get("run_attempt")==os.environ.get("GITHUB_RUN_ATTEMPT","1")
        and record.get("source_commit")==os.environ.get("GITHUB_SHA")
        and record.get("request_sha256")==file_sha(request_path)
        and record.get("worker_sha256")==file_sha(source)==request.get("source_sha256")
        and record.get("helper_sha256")==file_sha(Path(__file__))
        and record.get("boot_id")==Path("/proc/sys/kernel/random/boot_id").read_text().strip(),
        "Only the current206 recorded source/run/session may be observed or stopped")
    saved=record.get("own_process")
    require(isinstance(saved,dict) and saved.get("pid")==saved.get("pgid")==saved.get("sid")
        and record.get("exclusive_group_from_original_3b8_start_new_session") is True,
        "The actual original runner child must have recorded an exclusive session")
    return saved


def register_owner(comp,request_path):
    root,path,children,quiet=owner_paths()
    require(not path.exists() and not children.exists() and not quiet.exists(),
        "Use a fresh request206 owner record")
    own=process_identity(os.getpid())
    require(own is not None and own["pid"]==own["pgid"]==own["sid"],
        "Original3b8 must launch this worker in its own session")
    record=dict(schema="request206-exclusive-session-owner-v1",
        repository=REPOSITORY,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT","1"),
        source_commit=os.environ.get("GITHUB_SHA"),
        request_sha256=file_sha(request_path),
        worker_sha256=file_sha(comp/"geometry_20261116_thirty_nine_tabular_batches.py"),
        helper_sha256=file_sha(Path(__file__)),
        boot_id=Path("/proc/sys/kernel/random/boot_id").read_text().strip(),
        own_process=own,unix_seconds=time.time(),
        exclusive_group_from_original_3b8_start_new_session=True,
        original_3b8_source_unmodified=True,record_contains_no_token_or_environment=True)
    receipt=save_json_exact(path,record)
    emit("request206_actual_exclusive_owner_registered",dict(
        **receipt,own_process=own,no_scientific_threshold_added=True))
    return record


def record_original_child(label,pid):
    root,path,journal,quiet=owner_paths()
    require(path.is_file() and not path.is_symlink(),"Own206 launch record must precede children")
    owner=read(path); saved=owner["own_process"]; current=process_identity(pid)
    require(current is not None and current["pgid"]==saved["pgid"]
        and current["sid"]==saved["sid"] and current["ppid"]==saved["pid"],
        "Actual original model/FD child stays in the recorded206 session")
    row=dict(schema="request206-original-child-process-identity-v1",
        owner_record_sha256=file_sha(path),label=label,actual_process=current)
    raw=canonical(row)
    require(not journal.is_symlink(),"No child identity journal symlink")
    with journal.open("ab") as stream:
        stream.write(raw);stream.flush();os.fsync(stream.fileno())
    emit("request206_original_child_process_registered",dict(
        label=label,actual_process=current,record_bytes=len(raw),record_sha256=sha(raw),
        source_and_scientific_argv_unchanged=True))
    return row


def own_group_snapshot(saved):
    members=[];unknown=[]
    for entry in Path("/proc").iterdir():
        if not entry.name.isdigit():
            continue
        try:
            value=process_identity(int(entry.name))
            if value is not None and value["pgid"]==saved["pgid"]:
                members.append(value)
        except Exception as error:
            unknown.append(dict(pid=int(entry.name),error_type=type(error).__name__,
                error=str(error)))
    if any(row["sid"]!=saved["sid"] or row["start_ticks"]<saved["start_ticks"]
            for row in members):
        unknown.append(dict(error="A group member does not have the recorded session/start order"))
    leader=process_identity(saved["pid"])
    if leader is not None and leader["start_ticks"]!=saved["start_ticks"]:
        unknown.append(dict(error="Recorded leader PID has been reused; no signal is permitted"))
    return members,unknown


def quiesce_owned(comp,terminate):
    """After the science step only: identify/reap the own group, or keep partial."""
    root,path,journal,quiet=owner_paths()
    result=dict(schema="request206-owned-session-quiescence-v1",
        repository=REPOSITORY,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT","1"),
        source_commit=os.environ.get("GITHUB_SHA"),helper_sha256=file_sha(Path(__file__)),
        after_original_science_step=True,termination_allowed=bool(terminate),
        original_scientific_result_not_reclassified=True,
        signals=[],unknown_scope=[],quiescent=False)
    try:
        require(path.is_file() and not path.is_symlink(),
            "No valid original206 owner receipt; mutable output must remain unread")
        record=read(path);saved=owner_binding(comp,record)
        require(saved["pgid"]!=os.getpgrp() and saved["sid"]!=os.getsid(0),
            "Never signal the readback caller or its shared job group")
        result["actual_owner_record"]=original_file_receipt(path)
        result["original_owner"]=saved
        anchors=[saved]
        if journal.is_file():
            require(not journal.is_symlink(),"No journal symlink")
            for number,line in enumerate(journal.read_bytes().splitlines()):
                row=json.loads(line)
                require(row.get("schema")=="request206-original-child-process-identity-v1"
                    and row.get("owner_record_sha256")==file_sha(path),
                    "Child identity row must bind this exact owner")
                child=row["actual_process"]
                require(child["pgid"]==saved["pgid"] and child["sid"]==saved["sid"],
                    "A child identity must belong to the same original session")
                anchors.append(child)
        members,unknown=own_group_snapshot(saved)
        result["before"]=members;result["unknown_scope"].extend(unknown)
        live=[row for row in members if row["state"] not in ("Z","X")]
        # When the session leader has already vanished, a live, exact-start-time
        # recorded model/FD child can still identify the original group.
        identified=any(current["pid"]==anchor["pid"]
            and current["start_ticks"]==anchor["start_ticks"]
            for current in live for anchor in anchors)
        if live and not identified:
            result["unknown_scope"].append(dict(
                error="Live group has no exact recorded owner/child anchor; do not signal it"))
        if live and terminate and identified and not result["unknown_scope"]:
            # Actual group members seen with a live original anchor become
            # start-time anchors too, including original worker descendants.
            anchors.extend(members)
            for sig,seconds in ((signal.SIGTERM,15.0),(signal.SIGKILL,5.0)):
                members,unknown=own_group_snapshot(saved)
                result["unknown_scope"].extend(unknown)
                live=[row for row in members if row["state"] not in ("Z","X")]
                if not live or result["unknown_scope"]:
                    break
                identified=any(current["pid"]==anchor["pid"]
                    and current["start_ticks"]==anchor["start_ticks"]
                    for current in live for anchor in anchors)
                if not identified:
                    result["unknown_scope"].append(dict(
                        error="No live exact-start-time anchor before signal; keep partial"))
                    break
                anchors.extend(members)
                try:
                    os.killpg(saved["pgid"],sig)
                except ProcessLookupError:
                    # The identified group may have exited between observation
                    # and signal. Its fresh final scan decides quiescence.
                    result["signals"].append(dict(pgid=saved["pgid"],signal=int(sig),
                        group_vanished_before_signal=True))
                    break
                result["signals"].append(dict(pgid=saved["pgid"],signal=int(sig),
                    original_session_identified_before_signal=True))
                until=time.monotonic()+seconds
                while True:
                    members,unknown=own_group_snapshot(saved)
                    if unknown:
                        result["unknown_scope"].extend(unknown)
                        break
                    live=[row for row in members if row["state"] not in ("Z","X")]
                    if not live or time.monotonic()>=until:
                        break
                    time.sleep(.1)
                if result["unknown_scope"]:
                    break
        final,unknown=own_group_snapshot(saved)
        result["unknown_scope"].extend(unknown);result["after"]=final
        result["live_original_group_after"]=[row for row in final if row["state"] not in ("Z","X")]
        result["quiescent"]=not result["live_original_group_after"] and not result["unknown_scope"]
        result["zombies_not_treated_as_live_writers"]=True
        result["unidentified_group_never_signalled"]=True
        result["no_claim_about_unrecorded_detached_processes"]=True
    except Exception as error:
        result["unknown_scope"].append(dict(error_type=type(error).__name__,error=str(error)))
        result["quiescent"]=False
    raw=canonical(result)
    if len(raw)>SUMMARY_LIMIT:
        result["quiescent"]=False
        result["necessary_process_metadata_readback_complete"]=False
        receipt=save_json_exact(quiet,result)
        emit("request206_owner_metadata_transport_incomplete",dict(
            **receipt,quiescent=False,transport_exit_code=70))
    else:
        save_json_exact(quiet,result)
        emit("request206_actual_owner_quiescence",result)
    return result




class ReadbackIncomplete(RuntimeError):
    pass


def canonical(value):
    return (json.dumps(value, ensure_ascii=True, sort_keys=True,
        separators=(",", ":"), allow_nan=False)+"\n").encode("ascii")


def metadata_identity(value):
    raw = canonical(value)
    return dict(canonical_bytes=len(raw), canonical_sha256=sha(raw),
        identity_scope="parsed ASCII canonical JSON plus LF, not original file bytes")


def primitive_fields(reader, obj):
    """Original necessary scalar values; never truncate a returned error string."""
    if not isinstance(obj, dict):
        return None
    answer = reader.shallow(obj)
    for key, value in obj.items():
        if isinstance(value, str) and (
                key in answer or key in ("exception", "error", "message", "reason", "stop_reason")):
            answer[key] = value
    return answer


def necessary_point(point):
    """Only the original physical address, value and frozen weight, not a field row."""
    if not isinstance(point, dict):
        return point
    keys = ("interval", "left_node", "right_node", "left_station", "right_station",
        "existing_midpoint_station", "original_residual_row", "signed_value",
        "absolute_value", "original_vector_value", "kind", "right_row",
        "original_separated_boundary_row")
    answer = {key:point[key] for key in keys if key in point}
    component = point.get("component")
    if isinstance(component, dict):
        answer["component"] = {key:value for key,value in component.items()
            if value is None or isinstance(value,(str,int,float,bool))}
    elif component is not None:
        answer["component"] = component
    weight = point.get("frozen_model_row_weight")
    if isinstance(weight, dict):
        answer["frozen_model_row_weight"] = {key:weight[key] for key in (
            "available", "value", "model_weight_call", "base_evaluate_call", "reason")
            if key in weight}
    return answer


def necessary_QP(reader, value):
    """Keep real selected model/gates/budget outcomes; full QP history stays hash-bound."""
    if not isinstance(value, dict):
        return None
    comparison = value.get("comparison")
    answer = {}
    if isinstance(comparison, dict):
        keys = ("selected_candidate", "helper_completed",
            "same_original_A_b_damping_B_c", "original_C_candidate_retained",
            "original_C_objective", "condensed_candidate_objective",
            "original_verified_C_candidate_still_used",
            "global_selector_changed_conditional_recovery",
            "full_QP_optimality_claimed", "final_actual_full_A_AT_B_BT_readback",
            "helper_seconds_including_factor_condensation_QP_recovery",
            "posterior_is_not_a_validated_enclosure")
        answer["comparison"] = {key:comparison[key] for key in keys if key in comparison}
        for key in ("original_C_selection", "condensed_candidate_selection"):
            selection = comparison.get(key)
            if isinstance(selection, dict):
                answer[key] = {name:selection[name] for name in (
                    "selection", "segment_parameter", "selected_damped_model_decrease",
                    "actual_full_model_directional_derivative",
                    "all_original_linear_rows_rechecked_after_every_repair_and_combination",
                    "complete_R265_quadratic_optimality_claimed") if name in selection}
        final = comparison.get("final_actual_full_model_evidence")
        if isinstance(final, dict):
            answer["final_actual_full_model_evidence"] = primitive_fields(reader, final)
            if isinstance(final.get("all_original_linear_slack"), dict):
                answer["final_actual_full_model_evidence"]["all_original_linear_slack"] = (
                    primitive_fields(reader,final["all_original_linear_slack"]))
        failure = comparison.get("optional_optimization_failure")
        if isinstance(failure, dict):
            answer["optional_optimization_failure"] = {
                key:failure[key] for key in ("type","message","complete_exception_report_preserved")
                if key in failure}
            if "traceback" in failure:
                answer["optional_optimization_failure"]["original_traceback_identity"] = (
                    metadata_identity(failure["traceback"]))
    for key in ("local_QP_report", "last_saved_local_stage"):
        row = value.get(key)
        if isinstance(row,dict):
            names = ("schema", "stage", "active_stop_reason", "dual_stop_reason",
                "maximum_working_rows", "maximum_dual_sweeps", "completed_dual_sweeps",
                "elapsed_seconds", "selected_candidate", "final_selection", "segment_parameter",
                "segment_first_derivative", "segment_curvature",
                "original_full_coordinate_count", "local_coordinate_count",
                "original_inequality_row_count", "no_constraints_or_control_columns_removed",
                "new_full_QP_optimum_claimed", "full_QP_optimality_claimed",
                "budget_exhausted", "success")
            answer[key] = {name:row[name] for name in names if name in row}
            if isinstance(row.get("actual_working_rows"), list):
                answer[key]["actual_working_row_count"] = len(row["actual_working_rows"])
    answer["full_original_QP_summary_identity"] = metadata_identity(value)
    answer["QP_arrays_and_iteration_history_not_exported"] = True
    return answer


def publish(label, value):
    """One necessary document only; never split a scientific JSON object."""
    raw = canonical(value)
    receipt = dict(label=label, bytes=len(raw), sha256=sha(raw),
        scope="necessary scalar JSON with one LF; full scientific data not copied",
        summary_complete=len(raw) <= SUMMARY_LIMIT,
        scientific_acceptance_not_changed_by_transport=True)
    emit("request206_necessary_summary_identity", receipt)
    if len(raw) > SUMMARY_LIMIT:
        emit("request206_necessary_summary_incomplete", dict(**receipt,
            transport_exit_code=70, reason="necessary-summary-exceeds-90000-bytes",
            full_result_not_split_or_encoded=True,
            unread_necessary_records_retained=True,
            prior_large_raw_may_have_retired_after_durable_necessary_selection=True))
        raise ReadbackIncomplete("Necessary summary exceeds90000; preserve unread necessary records and surviving raw")
    print("BEGIN_REQUEST206_"+label.upper().replace("-", "_")+"_NECESSARY_SUMMARY", flush=True)
    sys.stdout.write(raw.decode("ascii"))
    print("END_REQUEST206_"+label.upper().replace("-", "_")+"_NECESSARY_SUMMARY", flush=True)
    return receipt


def original_file_receipt(path, relative=None):
    if not path.is_file():
        return dict(file=relative or path.name, present=False)
    return dict(file=relative or path.name, present=True,
        bytes=path.stat().st_size, sha256=file_sha(path))


def output_receipt(path, relative):
    return original_file_receipt(path, relative)


def angle_record(row):
    beta = row.get("original_beta_squared", {})
    return dict(query_index=row.get("query_index"), kind=row.get("kind"),
        interval=row.get("interval"), fraction=row.get("fraction"),
        station=row.get("station"), input_finite=row.get("original_query_input_finite"),
        beta_squared={key:beta[key] for key in (
            "minimum", "angle_index", "phi", "negative_count", "zero_count",
            "finite_count", "nonfinite_count") if key in beta})


DOMAIN_COLUMNS = (
    "node_domain_failures", "midpoint_domain_failures", "boundary_finite", "finite",
    "original_uniform_phi_rho_guard_valid", "original_rho_guard_angles",
    "original_uniform_phi_rho_min", "boundary_domain_error",
    "complete_trial_RHS_recomputed", "all_core_states_identical",
    "all_control_states_identical", "left_residual_max",
    "physical_collocation_max", "complete_boundary_max", "constant_collocation_max",
    "original_RMS_query_domain_failures")


def domain_record(reader, report):
    if not isinstance(report, dict):
        return None
    answer = dict(scalar_values=[report.get(key) for key in DOMAIN_COLUMNS])
    answer["RMS_checks_present"] = "original_RMS_query_checks" in report
    if "original_RMS_query_checks" in report:
        columns = ("interval", "s", "left", "right", "minimum_beta_squared",
                   "phi", "a", "ap", "app", "curve_curvature_at_minimum")
        answer["RMS_failed_point_columns"] = list(columns)
        answer["RMS_checks"] = [
            dict(**primitive_fields(reader, row), first_invalid_point_rows=[
                [point.get(key) for key in columns]
                for point in row.get("first_invalid_points", [])])
            for row in report["original_RMS_query_checks"]]
    mid = report.get("read_only_midpoint_observer")
    if isinstance(mid, dict):
        bad = mid.get("bad_midpoint_indices")
        answer["bad_midpoint_indices"] = bad
        answer["midpoint_observer_changed_original_result"] = mid.get(
            "original_returned_finite_or_merit_changed")
        columns = ("interval", "station", "left", "right",
            "middle_input_finite", "classification")
        beta_columns = ("minimum", "phi", "angle_index", "negative_count", "nonfinite_count")
        points = mid.get("points", [])
        # Selection uses the original explicit failure-index list only.
        # Missing list keeps all original returned points; no new domain test.
        selected = [point for point in points
            if not isinstance(bad, list) or point.get("interval") in bad]
        answer["midpoint_point_record_count"] = len(points)
        answer["midpoint_returned_failure_record_count"] = len(selected)
        answer["midpoint_failed_point_columns"] = list(columns)+list(beta_columns)
        answer["midpoint_failed_point_rows"] = [
            [point.get(key) for key in columns]+[
                point.get("original_beta_squared", {}).get(key) for key in beta_columns]
            for point in selected]
        point_errors = []
        # Observer errors can occur outside bad_midpoint_indices. Read every
        # returned point's actual error fields, without a new domain decision.
        for point_index, point in enumerate(points):
            errors = {key:point[key] for key in (
                "angular_observer_exception", "observer_export_exception")
                if key in point}
            if not errors:
                continue
            item = dict(point_index=point_index, **{
                key:point[key] for key in ("interval", "station",
                    "original_solver_result_still_used") if key in point}, **errors)
            if "angular_observer_traceback" in point:
                item["angular_observer_traceback_identity"] = metadata_identity(
                    point["angular_observer_traceback"])
            point_errors.append(item)
        answer["midpoint_point_observer_errors"] = point_errors
    weight_error = report.get("collocation_weight_observer_error")
    if isinstance(weight_error, dict):
        item = {key:weight_error[key] for key in (
            "schema", "observer_exception", "diagnostic_only",
            "original_weights_returned_unchanged") if key in weight_error}
        if "observer_traceback" in weight_error:
            item["observer_traceback_identity"] = metadata_identity(
                weight_error["observer_traceback"])
        if "entry" in weight_error:
            item["entry_identity"] = metadata_identity(weight_error["entry"])
        answer["collocation_weight_observer_error"] = item
    col = report.get("read_only_collocation_location_observer", {})
    if isinstance(col, dict) and isinstance(col.get("full_physical_argmax"), dict):
        answer["physical_argmax"] = necessary_point(col["full_physical_argmax"])
    for name, observer in (("midpoint",mid),("collocation",col)):
        if isinstance(observer,dict):
            errors = {key:value for key,value in observer.items()
                if isinstance(value,str) and (key.endswith("_exception") or key.endswith("_error"))}
            if errors:
                answer[name+"_observer_errors"] = errors
    return answer


def fd_record(reader, value):
    if not isinstance(value, dict):
        return None
    answer = primitive_fields(reader, value)
    failed_contractions = []
    for key in ("direct_boundary", "separated_boundary"):
        group = value.get(key)
        if not isinstance(group, dict):
            continue
        answer[key] = primitive_fields(reader, group)
        # Every original scientific level still executes. This necessary
        # readout copies the original group decisions and direction addresses;
        # the complete numerical histories stay in response-check.json.
        directions=group.get("directions", [])
        answer[key]["direction_columns"]=[
            "direction","centered_levels","Richardson_levels","contraction_records"]
        answer[key]["direction_rows"]=[
            [row.get("direction"),len(row.get("levels",[])),
             len(row.get("fourth_order_levels",[])),
             len(row.get("second_order_contraction",[]))] for row in directions]
        for direction_index, row in enumerate(directions):
            for record_index, record in enumerate(row.get("second_order_contraction", [])):
                if record.get("contracts") is False:
                    failed_contractions.append(dict(group=key,
                        direction_index=direction_index, direction=row.get("direction"),
                        record_index=record_index, original_contraction_record=dict(record)))
        answer[key]["full_original_direction_history_identity"]=metadata_identity(directions)
        answer[key]["individual_level_numeric_histories_not_exported"]=True
    answer["failed_second_order_contraction_records"] = failed_contractions
    answer["all_original_contracts_false_records_returned_without_recomputing_gate"] = True
    for key in ("accepted_sha256", "prepared_sha256", "tail_anchor_sha256",
                "tail_config_sha256", "source_sha256"):
        if key in value:
            answer[key] = value[key]
    mapping = value.get("consumed_source_sha256", {})
    answer["complete_consumed_source_mapping_identity"] = dict(
        source_count=len(mapping), **metadata_identity(mapping))
    return answer


def summarize(reader, model, status, qp, fd):
    """Read all actual trials and selected query outcomes, without array actions."""
    embedded = (status.get("iterations") or [None])[0]
    source = "original standalone model"
    if not isinstance(model, dict):
        model = embedded if isinstance(embedded, dict) else {}
        source = "original driver-status first iteration" if model else "no original model returned"
    trials = model.get("trials", [])
    accepted_indices = [i for i,row in enumerate(trials) if row.get("accepted") is True]
    nearest = (accepted_indices[0]-1 if accepted_indices and accepted_indices[0] > 0
        else (len(trials)-1 if trials and not accepted_indices else None))
    records = []
    for index, row in enumerate(trials):
        selected = row.get("actual_selected_original_angles", [])
        item = dict(original_trial_index=index, **primitive_fields(reader, row))
        item["domain"] = domain_record(reader, row.get("domain"))
        item["RMS_stage_present"] = "complete_original_RMS_query_domain" in row
        item["complete_original_RMS_query_domain"] = domain_record(
            reader, row.get("complete_original_RMS_query_domain"))
        for key in ("selected_linear_beta_squared", "all_selected_linear_reserve_slack",
                    "independent_actual_directional_check"):
            item[key] = primitive_fields(reader, row.get(key))
        item["selected_query_count"] = len(selected)
        item["evaluated_selected_query_index_ranges"] = index_ranges(
            point.get("query_index") for point in selected)
        # All source-declared failed selected queries, never only the worst one.
        item["failed_selected_query_records"] = [angle_record(point) for point in selected
            if point.get("original_query_input_finite") is False
            or point.get("original_beta_squared", {}).get("negative_count", 0) != 0
            or point.get("original_beta_squared", {}).get("nonfinite_count", 0) != 0
            or point.get("original_beta_squared", {}).get("zero_count", 0) != 0]
        records.append(item)
    same_fields = {}
    if isinstance(embedded, dict):
        for field in SCIENTIFIC_MODEL_FIELDS:
            same_fields[field] = dict(present_in_both=field in model and field in embedded,
                equal=model.get(field) == embedded.get(field))
    identity = status.get("identity") or {}
    entry = model.get("thirty_nine_query_projection_entry")
    if not isinstance(entry, dict):
        entry = identity.get("thirty_nine_query_projection_entry") or {}
    queries = entry.get("query_specs")
    declared = model.get("condensed_QP_entry") or {}
    layout = declared.get("actual_current_B_C_layout")
    if not isinstance(layout, dict):
        layout = {}
    return dict(status=primitive_fields(reader, status), original_trial_source=source,
        model_before=domain_record(reader, model.get("before")),
        fixed_weight_merit_before=model.get("fixed_weight_merit_before"),
        model_damping=model.get("damping"), model_accepted=model.get("accepted"),
        original_typed_queries=queries,
        all_original_trials=records,
        returned_original_trial_count=len(trials), declared_original_trial_limit=17,
        returned_trial_indices=list(range(len(trials))),
        not_recorded_original_trial_indices=list(range(len(trials), 17)),
        not_recorded_suffix_not_assumed_evaluated_or_unvisited_after_interruption=True,
        unavailable_trials_not_filled_with_predicted_results=True,
        nearest_rejected_original_trial_index=nearest,
        full_original_trial_tree_identity=metadata_identity(trials),
        full_original_status_iterations_identity=metadata_identity(status.get("iterations")),
        status_standalone_model_science_fields=same_fields,
        QP=necessary_QP(reader, qp),
        FD=fd_record(reader, fd),
        actual_B_C_layout=reader.shallow(layout),
        complete_actual_query_endpoint_nodes=entry.get("actual_query_endpoint_nodes"),
        actual_parent_optimizer_schema=entry.get("parent_optimizer_schema"),
        actual_resume_sha256=entry.get("actual_resume_sha256"),
        actual_parent_status_sha256=entry.get("actual_parent_status_sha256"),
        actual_added_queries_this_request=[dict(kind="right-RMS", interval=459,
            fraction=0.8273268353539885)],
        query_addition_reference="complete frozen38 query set, not initial original31 field producer",
        initial_parent_is_real_actual98_not_deleted171=True,
        actual171_replayed_before_new39=False,
        all22_LEFT_and16_MID_queries_retained=True,
        added_capture_intervals=[459], added_capture_nodes=[459,460],
        complete_B_endpoint_nodes=[459,460]+list(range(462,492)),
        complete_B_local_coordinates=10819,
        no_fictitious_B461_column=True, node461_retained_in_full_H=True,
        baseline_C_and_complete_H_outside_scope_unchanged=True,
        all_actual_trial_scalars_and_declared_failed_query_rows_selected=True,
        complete_trial_scientific_JSON_not_encoded_or_semantically_streamed=True,
        full_original_scientific_arrays_temporary_only=True,
        no_new_scientific_arithmetic_in_readout=True,
        model_relation_readout_is_not_a_new_scientific_gate=True,
        no_cross_model_weighted_merit_subtraction=True,
        native_at_current_height_solved=False, new_full_DN_acceptance=False)


def error_log_readout(path):
    receipt = original_file_receipt(path)
    if not receipt["present"]:
        return receipt
    raw = path.read_bytes()
    # Genuine stderr text is not a scientific array transport. Still keep
    # one bounded document; larger text is explicitly unread, never split.
    if len(raw) <= ERROR_TEXT_LIMIT:
        return dict(**receipt, complete_original_stderr_text=True,
            text=raw.decode("utf-8", "surrogateescape"))
    return dict(**receipt, complete_original_stderr_text=False,
        original_stderr_not_returned=True, reason="original-stderr-exceeds-64000",
        unread_owned_error_bytes_retained=True)


def run_child(label, command, repo, env, work):
    stdout_path, stderr_path = work/(label+".log"), work/(label+".stderr.log")
    started = time.monotonic()
    with stdout_path.open("wb") as out, stderr_path.open("wb") as err:
        result = subprocess.Popen(command, cwd=repo, env=env, stdout=out,
            stderr=err, start_new_session=False)
        record_original_child(label,result.pid)
        result.wait()
    report = dict(label=label, command=list(map(str, command)),
        exit_code=result.returncode, elapsed_seconds=time.monotonic()-started,
        stdout=original_file_receipt(stdout_path),
        stderr=error_log_readout(stderr_path), log_temporary_only=True,
        scientific_stdout_not_forwarded_as_a_large_data_stream=True)
    if result.returncode and stdout_path.is_file():
        with stdout_path.open("rb") as stream:
            size=stdout_path.stat().st_size
            stream.seek(max(0,size-4096))
            tail=stream.read()
        report["necessary_failure_stdout_tail"]=dict(
            bytes=len(tail), exact_original_tail_sha256=sha(tail),
            text=tail.decode("utf-8","surrogateescape"),
            is_complete_stdout=len(tail)==size,
            scope="original terminal byte slice, not a complete scientific stdout replay")
    progress.setdefault("child_process_receipts", []).append({
        key:report[key] for key in ("label", "exit_code", "elapsed_seconds", "stdout", "stderr")})
    # Operational error metadata is bounded separately; scientific batch
    # scalars are emitted only in the single final whole-chain document.
    raw=canonical(dict(event="request206_original_child_finished", **report))
    if len(raw)>SUMMARY_LIMIT:
        emit("request206_child_error_transport_incomplete", dict(
            label=label, exit_code=result.returncode,
            stdout=report["stdout"], stderr=original_file_receipt(stderr_path),
            necessary_error_bytes=len(raw), transport_exit_code=70,
            unread_owned_error_bytes_retained=True))
        raise ReadbackIncomplete("Original child ended; necessary error readout exceeds90000")
    sys.stdout.write(raw.decode("ascii")); sys.stdout.flush()
    if report["stderr"].get("complete_original_stderr_text") is False:
        raise ReadbackIncomplete("Original child ended; its oversized stderr remains unread")
    return result.returncode



def index_ranges(indices):
    """Only integer record addresses; not an encoding of scientific vectors."""
    values=sorted(set(value for value in indices if type(value) is int))
    result=[]
    for value in values:
        if result and value==result[-1][1]+1:
            result[-1][1]=value
        else:
            result.append([value,value])
    return result


def save_json_exact(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    raw=canonical(value)
    pending=path.with_name(path.name+".writing")
    with pending.open("xb") as stream:
        stream.write(raw); stream.flush(); os.fsync(stream.fileno())
    os.replace(pending,path)
    require(path.stat().st_size==len(raw) and file_sha(path)==sha(raw),
        "Temporary necessary record must contain these complete selected fields")
    return dict(file=path.name,bytes=len(raw),sha256=sha(raw),
        necessary_record_temporary_only=True,scientific_stdout_not_emitted=True)


def save_necessary_batch(work,summary):
    # Persist before pair movement and before retiring large original files.
    # A later exception can still recover every selected original trial field.
    path=work/"necessary-batches"/("batch-%03d.json"%summary["batch_index"])
    receipt=save_json_exact(path,summary)
    emit("request206_necessary_batch_record_saved",dict(
        batch_index=summary["batch_index"],**receipt,
        complete_original_trial_count=summary["returned_original_trial_count"],
        whole_chain_stdout_readback_still_pending=True))
    return receipt


def same_necessary_json(left,right):
    """Equality of selected canonical JSON, preserving signed zero and scalar types."""
    return canonical(left)==canonical(right)


class NecessaryScalarTables:
    """Fixed semantic tables of selected scalars, not a generic JSON/tree codec.

    Callers name each scientific role explicitly. No ndarray, full FD level
    history, field vector, recursive object, or arbitrary source tree enters
    these tables. The address columns are original record addresses only.
    """
    def __init__(self):
        self.records = {}

    def add(self, name, address_columns, address, values):
        if not isinstance(values, dict):
            raise ReadbackIncomplete("A selected necessary scalar row is not an object: "+name)
        if len(address_columns) != len(address):
            raise ReadbackIncomplete("Necessary address length differs: "+name)
        old = self.records.setdefault(name, dict(
            address_columns=list(address_columns), rows=[]))
        if old["address_columns"] != list(address_columns):
            raise ReadbackIncomplete("Necessary semantic address changed: "+name)
        for key, value in values.items():
            scalar = value is None or isinstance(value, (str,int,float,bool))
            literal_nonfinite = (isinstance(value,dict)
                and set(value)=={"original_nonfinite_JSON_token"})
            if not scalar and not literal_nonfinite:
                raise ReadbackIncomplete("Unselected non-scalar in necessary table: "+name+"/"+key)
        old["rows"].append((list(address),dict(values)))

    def finish(self):
        result = {}
        for name, item in self.records.items():
            columns = sorted({key for _, values in item["rows"] for key in values})
            # Only labels repeat less. Every original selected value remains.
            result[name] = dict(address_columns=item["address_columns"],
                value_columns=columns,
                rows=[address+[values.get(key) for key in columns]
                      for address,values in item["rows"]])
        return result


def short_canonical_identity(value):
    """Share only the two explicit repeated identity-scope sentences."""
    if not isinstance(value,dict):
        return value
    answer=dict(value)
    known={
        "identity_scope":"parsed ASCII canonical JSON plus LF, not original file bytes",
        "scope":"original parsed JSON, sorted ASCII keys, one LF; not raw array bytes",
    }
    for key,sentence in known.items():
        if answer.get(key)==sentence:
            del answer[key]
    return answer


def necessary_parameters(value):
    if not isinstance(value,dict):
        return value
    answer={key:value[key] for key in (
        "original_frozen_design_parameters","original_global_scalar_parameters",
        "original_parameter_sources_present","original_parameter_readout_complete",
        "complete_scalar_profile_identity","original_native_height_identity",
        "readout_error_type","readout_error") if key in value}
    for key in ("complete_scalar_profile_identity","original_native_height_identity"):
        if key in answer:
            answer[key]=short_canonical_identity(answer[key])
    return answer


def add_domain_tables(tables, errors, index_sets, batch_record, phase, trial, value,
                      same_candidate=False):
    """Preserve both actual evaluation roles; share only exact equal selected records."""
    address=(batch_record,phase,trial)
    labels=("batch_record","evaluation_role","original_trial_index")
    present=isinstance(value,dict)
    fields=dict(original_domain_report_present=present,
        same_original_necessary_record_as_candidate=bool(same_candidate))
    if not present or same_candidate:
        tables.add("domain_returns",labels,address,fields)
        return
    scalars=value.get("scalar_values",[])
    if len(scalars)!=len(DOMAIN_COLUMNS):
        raise ReadbackIncomplete("Selected original domain scalar columns differ")
    fields.update(zip(DOMAIN_COLUMNS,scalars))
    for key in ("RMS_checks_present","midpoint_observer_changed_original_result",
                "midpoint_point_record_count","midpoint_returned_failure_record_count"):
        if key in value:
            fields[key]=value[key]
    fields["physical_argmax_record_present"]="physical_argmax" in value
    tables.add("domain_returns",labels,address,fields)
    if "bad_midpoint_indices" in value:
        bad=value["bad_midpoint_indices"]
        index_sets.append(dict(batch_record=batch_record,evaluation_role=phase,
            original_trial_index=trial,original_bad_midpoint_index_ranges=(
                index_ranges(bad) if isinstance(bad,list) else bad)))
    rms_point_columns=("interval","s","left","right","minimum_beta_squared",
        "phi","a","ap","app","curve_curvature_at_minimum")
    for check_index,row in enumerate(value.get("RMS_checks",[])):
        fields={key:item for key,item in row.items() if key!="first_invalid_point_rows"}
        tables.add("original_RMS_checks",labels+("original_check_index",),
            address+(check_index,),fields)
        for point_index,point in enumerate(row.get("first_invalid_point_rows",[])):
            if len(point)!=len(rms_point_columns):
                raise ReadbackIncomplete("Original RMS failure sample columns differ")
            tables.add("original_RMS_returned_failure_samples",
                labels+("original_check_index","original_returned_sample_index"),
                address+(check_index,point_index),dict(zip(rms_point_columns,point)))
    midpoint_columns=("interval","station","left","right","middle_input_finite",
        "classification","minimum","phi","angle_index","negative_count","nonfinite_count")
    for point_index,point in enumerate(value.get("midpoint_failed_point_rows",[])):
        if len(point)!=len(midpoint_columns):
            raise ReadbackIncomplete("Original midpoint failure columns differ")
        tables.add("original_midpoint_failure_records",
            labels+("original_returned_failure_index",),address+(point_index,),
            dict(zip(midpoint_columns,point)))
    point=value.get("physical_argmax")
    if isinstance(point,dict):
        tables.add("original_physical_argmax",labels,address,
            {key:item for key,item in point.items()
             if key not in ("component","frozen_model_row_weight")})
        component=point.get("component")
        if isinstance(component,dict):
            tables.add("original_physical_argmax_component",labels,address,component)
        elif "component" in point:
            tables.add("original_physical_argmax_component",labels,address,dict(component=component))
        if isinstance(point.get("frozen_model_row_weight"),dict):
            tables.add("original_physical_argmax_frozen_weight",labels,address,
                point["frozen_model_row_weight"])
    # Exceptions are independent of the source's bad-point index selection.
    # Keep the complete original selected strings and all actual addresses.
    for key in ("midpoint_point_observer_errors","collocation_weight_observer_error",
                "midpoint_observer_errors","collocation_observer_errors"):
        if key in value and value[key]:
            errors.append(dict(batch_record=batch_record,evaluation_role=phase,
                original_trial_index=trial,original_location=key,original_record=value[key]))


def add_QP_tables(tables,batch_record,value):
    if not isinstance(value,dict):
        return dict(original_report_present=False)
    address=(batch_record,)
    labels=("batch_record",)
    answer=dict(original_report_present=True,
        full_original_QP_summary_identity=short_canonical_identity(
            value.get("full_original_QP_summary_identity")),
        QP_arrays_and_iteration_history_not_exported=value.get(
            "QP_arrays_and_iteration_history_not_exported"))
    parts=("comparison","original_C_selection","condensed_candidate_selection",
        "local_QP_report","last_saved_local_stage")
    answer["actual_returned_scalar_sections"]=[name for name in parts if isinstance(value.get(name),dict)]
    for name in parts:
        if isinstance(value.get(name),dict):
            tables.add("QP_"+name,labels,address,value[name])
    final=value.get("final_actual_full_model_evidence")
    answer["final_actual_full_model_evidence_present"]=isinstance(final,dict)
    if isinstance(final,dict):
        tables.add("QP_final_actual_full_model_evidence",labels,address,{
            key:item for key,item in final.items() if key!="all_original_linear_slack"})
        if isinstance(final.get("all_original_linear_slack"),dict):
            tables.add("QP_all_original_linear_slack",labels,address,
                final["all_original_linear_slack"])
    if "optional_optimization_failure" in value:
        answer["optional_optimization_failure"]=value["optional_optimization_failure"]
    return answer


def add_FD_tables(tables,schedules,batch_record,value):
    if not isinstance(value,dict):
        return dict(original_report_present=False)
    groups=("direct_boundary","separated_boundary")
    skip=set(groups)|{"failed_second_order_contraction_records",
        "complete_consumed_source_mapping_identity"}
    tables.add("FD_original_report",("batch_record",),(batch_record,),
        {key:item for key,item in value.items() if key not in skip})
    answer=dict(original_report_present=True,
        complete_consumed_source_mapping_identity=short_canonical_identity(
            value.get("complete_consumed_source_mapping_identity")),
        groups={})
    for name in groups:
        group=value.get(name)
        if not isinstance(group,dict):
            answer["groups"][name]=dict(original_group_present=False)
            continue
        scalar={key:item for key,item in group.items() if key not in (
            "direction_columns","direction_rows","full_original_direction_history_identity")}
        rows=group.get("direction_rows",[])
        columns=group.get("direction_columns")
        schedule=dict(columns=columns,rows=rows)
        # This is a fixed semantic direction/level-count schedule, not the
        # actual derivative/error history. Share it only after exact equality.
        if name not in schedules:
            schedules[name]=schedule
        equal=same_necessary_json(schedule,schedules[name])
        scalar["original_direction_record_count"]=len(rows)
        scalar["schedule_equals_first_actual_group_schedule"]=equal
        tables.add("FD_original_groups",("batch_record","original_group"),
            (batch_record,name),scalar)
        item=dict(original_group_present=True,
            full_original_direction_history_identity=short_canonical_identity(
                group.get("full_original_direction_history_identity")),
            schedule_equals_first_actual_group_schedule=equal)
        if not equal:
            item["actual_different_direction_schedule"]=schedule
        answer["groups"][name]=item
    failed=value.get("failed_second_order_contraction_records",[])
    answer["original_failed_contraction_record_count"]=len(failed)
    for row in failed:
        address=(batch_record,row.get("group"),row.get("direction_index"),
            row.get("direction"),row.get("record_index"))
        tables.add("FD_all_original_failed_contractions",
            ("batch_record","original_group","original_direction_index",
             "original_direction","original_contraction_index"),
            address,row.get("original_contraction_record",{}))
    return answer


def compact_chain_state(state):
    """Control flow and the real last pair, without duplicating per-batch tables."""
    if not isinstance(state,dict):
        return state
    keys = ("schema", "request", "run_id", "source_commit", "source_sha256",
        "request_sha256", "phase", "batch_index", "stop_reason", "attempted_batches",
        "completed_model_FD_pairs", "completed_batch_indices", "current_real_input_pair",
        "last_actual_completed_pair", "original_exit_code", "actual_elapsed_batch_loop_seconds",
        "readback_only", "actual_owner_quiescent_before_read", "actual_surviving_namespaces",
        "necessary_error_logs", "no_process_exit_or_missing_phase_inferred",
        "no_surviving_batch_does_not_mean_scientific_success",
        "this_reader_does_not_delete_original_files", "whole_chain_stdout_readback_pending",
        "success", "new_coupled_finite_acceptance", "cleanup_after_single_complete_whole_chain_readback",
        "all_owned_temporary_payload_removed", "final_field_not_recoverable_from_hash_alone")
    out={key:state[key] for key in keys if key in state}
    fields=state.get("last_completed_field_identity")
    if isinstance(fields,dict):
        out["last_actual_pair_necessary_parameters"]={key:fields[key] for key in (
            "original_frozen_design_parameters", "original_global_scalar_parameters",
            "original_parameter_sources_present", "original_parameter_readout_complete",
            "complete_scalar_profile_identity",
            "original_native_height_identity") if key in fields}
    if "actual_saved_chain_states" in state:
        out["actual_saved_chain_states"]=[compact_chain_state(row)
            for row in state["actual_saved_chain_states"]]
    return out


def assemble_chain(summaries,state,binding,errors=None):
    """One addressed necessary document; no recursive science-tree encoding."""
    errors=list(errors or [])
    tables=NecessaryScalarTables()
    schedules={}
    query_definitions=[]
    observer_errors=[]
    domain_index_sets=[]
    selected_index_sets=[]
    batches=[]
    trial_nested={"domain","complete_original_RMS_query_domain",
        "selected_linear_beta_squared","all_selected_linear_reserve_slack",
        "independent_actual_directional_check","evaluated_selected_query_index_ranges",
        "failed_selected_query_records"}
    status_names=("schema","phase","accepted_warm_steps","optimization_progress",
        "success","new_coupled_finite_acceptance","latest_warm_file","latest_warm_sha256",
        "elapsed_seconds","exception","error","reason","stop_reason")
    linear_names=("selected_linear_beta_squared","all_selected_linear_reserve_slack",
        "independent_actual_directional_check")
    for record_index, summary in enumerate(summaries):
        queries=summary.get("original_typed_queries")
        if queries is not None and not any(same_necessary_json(queries,old)
                for old in query_definitions):
            query_definitions.append(queries)
        keys=("batch_index","original_trial_source","returned_original_trial_count",
            "returned_trial_indices","not_recorded_original_trial_indices",
            "nearest_rejected_original_trial_index","actual_parent_optimizer_schema",
            "input_pair","produced_pair","original_model_exit_code","original_FD_exit_code",
            "next_batch_eligible","stop_reason","primary_outputs",
            "actual_surviving_batch","actual_surviving_parent_carrier","actual_namespace",
            "original_files","original_status_file","readback_errors",
            "no_process_exit_or_missing_phase_inferred",
            "no_model_FD_success_or_completed_handoff_inferred")
        item={key:summary[key] for key in keys if key in summary}
        item["batch_record"]=record_index
        item["full_original_trial_tree_identity"]=short_canonical_identity(
            summary.get("full_original_trial_tree_identity"))
        tables.add("model_scalar_results",("batch_record",),(record_index,),{
            key:summary[key] for key in (
                "fixed_weight_merit_before","model_damping","model_accepted") if key in summary})
        status=summary.get("status")
        item["original_status_present"]=isinstance(status,dict)
        if isinstance(status,dict):
            tables.add("original_status",("batch_record",),(record_index,),
                {key:status[key] for key in status_names if key in status})
        item["QP"]=add_QP_tables(tables,record_index,summary.get("QP"))
        item["FD"]=add_FD_tables(tables,schedules,record_index,summary.get("FD"))
        fields=summary.get("output_field_identity")
        if isinstance(fields,dict):
            item["actual_pair_parameters"]=necessary_parameters(fields)
            item["field_subset_identity"]={key:fields[key] for key in (
                "schema","complete_selected_fields_present","sha256") if key in fields}
        relation=summary.get("status_standalone_model_science_fields")
        if isinstance(relation,dict):
            for name in ("iteration","fixed_weight_merit_before","damping","accepted","trials"):
                if isinstance(relation.get(name),dict):
                    tables.add("status_standalone_model_field_relation",
                        ("batch_record","original_model_field"),(record_index,name),relation[name])
        add_domain_tables(tables,observer_errors,domain_index_sets,
            record_index,"base",None,summary.get("model_before"))
        for row in summary.get("all_original_trials",[]):
            index=row.get("original_trial_index")
            scalars={key:value for key,value in row.items()
                     if key not in trial_nested and key!="original_trial_index"}
            for name in linear_names:
                scalars[name+"_record_present"]=isinstance(row.get(name),dict)
            tables.add("all_original_trials",("batch_record","original_trial_index"),
                (record_index,index),scalars)
            add_domain_tables(tables,observer_errors,domain_index_sets,
                record_index,"candidate",index,row.get("domain"))
            rms=row.get("complete_original_RMS_query_domain")
            same=(isinstance(rms,dict) and same_necessary_json(rms,row.get("domain")))
            add_domain_tables(tables,observer_errors,domain_index_sets,
                record_index,"complete_RMS",index,rms,same_candidate=same)
            selected_index_sets.append(dict(batch_record=record_index,
                original_trial_index=index,
                evaluated_selected_query_index_ranges=row.get(
                    "evaluated_selected_query_index_ranges")))
            for name in linear_names:
                if isinstance(row.get(name),dict):
                    tables.add(name,("batch_record","original_trial_index"),
                        (record_index,index),row[name])
            for failure_index,point in enumerate(row.get("failed_selected_query_records",[])):
                values={key:point.get(key) for key in (
                    "query_index","kind","interval","fraction","station","input_finite")}
                values.update(point.get("beta_squared",{}))
                tables.add("all_original_failed_selected_queries",
                    ("batch_record","original_trial_index","original_failure_record_index"),
                    (record_index,index,failure_index),values)
        batches.append(item)
    compact_state=compact_chain_state(state)
    # The real last-pair parameter receipt already occurs at the actual batch.
    # Only exact JSON equality of both pair and selected parameter record
    # permits this one explicit semantic reference. A difference is retained.
    if isinstance(compact_state,dict):
        def remove_repeated_last_parameters(part):
            if not isinstance(part,dict):
                return
            parameters=part.get("last_actual_pair_necessary_parameters")
            pair=part.get("last_actual_completed_pair")
            if isinstance(parameters,dict):
                parameters=necessary_parameters(parameters)
                part["last_actual_pair_necessary_parameters"]=parameters
                for batch in reversed(batches):
                    if (isinstance(pair,dict) and same_necessary_json(pair,batch.get("produced_pair"))
                            and same_necessary_json(parameters,batch.get("actual_pair_parameters"))):
                        del part["last_actual_pair_necessary_parameters"]
                        part["last_parameters_same_as_actual_batch_record"]=batch["batch_record"]
                        break
            for child in part.get("actual_saved_chain_states",[]):
                remove_repeated_last_parameters(child)
        remove_repeated_last_parameters(compact_state)
    return dict(schema="request206-one-necessary-whole-chain-tables-v1",
        request=206,run_id=os.environ.get("GITHUB_RUN_ID"),
        source_commit=os.environ.get("GITHUB_SHA"),source_sha256=file_sha(Path(__file__)),
        source_and_actual_input_binding=binding,actual_chain_state=compact_state,
        summary_complete=not errors,readback_errors=errors,
        original_typed_query_definitions=query_definitions,
        necessary_scalar_tables=tables.finish(),batches=batches,
        original_domain_index_sets=domain_index_sets,
        original_selected_query_index_sets=selected_index_sets,
        all_actual_original_observer_errors=observer_errors,
        original_FD_first_actual_direction_schedules=schedules,
        FD_schedule_sharing_is_exact_metadata_equality_not_reused_science=True,
        canonical_identity_scopes=dict(
            canonical_bytes_and_sha256="parsed ASCII canonical JSON plus LF, not original file bytes",
            original_parameter_record_identities="original parsed JSON, sorted ASCII keys, one LF; not raw array bytes"),
        table_contract=dict(
            rows_address_only_already_selected_necessary_scalars=True,
            value_columns_are_explicit_original_field_names_once_per_role=True,
            absent_original_scalar_cells_are_null_as_in_request200=True,
            actual_batch_indices_and_partial_carrier_addresses_are_in_batches=True,
            no_recursive_JSON_object_dictionary_or_array_encoding=True,
            no_new_scientific_or_acceptance_arithmetic=True),
        original_RMS_producer_samples_at_most_first24_per_fraction=True,
        all_original_returned_RMS_failure_samples_kept_without_another_limit=True,
        identical_RMS_domain_reference_requires_exact_selected_JSON_equality=True,
        original_FD_all_levels_executed_but_numeric_histories_only_file_identity=True,
        all_original_contracts_false_records_preserved_with_group_direction_indices=True,
        original_trial_limit_per_model=17,maximum_model_FD_pairs=8,
        observed_batch_indices=[row.get("batch_index") for row in summaries],
        not_represented_batch_indices=[i for i in range(8)
            if i not in [row.get("batch_index") for row in summaries]],
        unstarted_batch_indices=(list(range(state["attempted_batches"],8))
            if type(state.get("attempted_batches")) is int and "stop_reason" in state else None),
        missing_record_not_relabelled_as_unstarted_or_completed=True,
        original_numeric_results_not_recomputed=True,
        original_merit_policy=dict(
            actual_reduction_must_exceed="64*binary64_eps*max(1,base_fixed_weight_merit)",
            actual_to_predicted_ratio_minimum=0.1,
            actual_floor_number_not_stored_by_original_producer=True,
            reader_does_not_recompute_the_floor=True),
        all_R428_selected_scalar_values_and_returned_failed_addresses_retained=True,
        no_large_scientific_JSON_split_or_dictionary_encoding=True,
        source_identity_not_a_payload_reconstruction=True,
        actual200_unread_values_not_reconstructed_or_used_as_parent=True,
        success=False,new_coupled_finite_acceptance=False,
        nonlinear_native_or_full_DN_called=False)


def read_saved_summaries(work):
    result=[]
    for path in sorted((work/"necessary-batches").glob("batch-*.json")):
        require(not path.is_symlink() and path.resolve().is_relative_to(work),
            "Owned necessary original-field record only")
        value=read(path)
        require(isinstance(value,dict),"A complete necessary batch object")
        result.append(value)
    return result


def finish_chain(work,state):
    save_json_exact(work/"necessary-chain-state.json",state)
    summaries=read_saved_summaries(work)
    binding=read(work/"necessary-input-binding.json")
    report=assemble_chain(summaries,state,binding)
    save_json_exact(work/"necessary-whole-chain.json",report)
    return publish("whole-chain",report)


def readback_only(argv=None):
    """Recover ONE bounded chain from saved scalar records and actual partials."""
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--readback-only",action="store_true",required=True)
    parser.add_argument("--temporary-root",type=Path,required=True)
    parser.add_argument("--code-directory",type=Path,required=True)
    args=parser.parse_args(argv)
    require(os.environ.get("GITHUB_ACTIONS")=="true"
        and os.environ.get("GITHUB_REPOSITORY")==REPOSITORY,
        "Read existing output in the original public Actions only")
    root=Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    require(args.temporary_root.resolve(strict=True)==root,"Only this job temporary root")
    ownership=quiesce_owned(args.code_directory.resolve(strict=True),terminate=True)
    if not ownership["quiescent"]:
        emit("request206_mutable_output_readback_skipped",dict(
            transport_exit_code=70,reason="own-session-not-proved-quiescent",
            scientific_result_not_reclassified=True,unread_raw_not_deleted=True))
        return 70
    reader=load("_request206_pure_scalar_selectors",
        args.code_directory/READER_ENTRY,READER_SHA)
    errors=[]; summaries=[]; states=[]; bindings=[]; namespaces=[]; error_logs=[]
    for work in sorted(root.glob(NAMESPACE_PREFIX+"*")):
        require(not work.is_symlink() and work.resolve().is_relative_to(root),"Owned namespace only")
        if not work.is_dir() or work.name.endswith("-rules"):
            continue
        namespaces.append(work.name)
        try:
            saved=read_saved_summaries(work)
            summaries.extend(saved)
        except Exception as error:
            saved=[]
            errors.append(dict(namespace=work.name,source="necessary-batches",error=repr(error)))
        saved_batches={row.get("batch_index") for row in saved}
        for name,collection in (("necessary-input-binding.json",bindings),
                                ("necessary-chain-state.json",states)):
            path=work/name
            if path.is_file():
                try:collection.append(read(path))
                except Exception as error:
                    errors.append(dict(namespace=work.name,file=name,error=repr(error)))
        for batch in sorted(work.glob("batch-*")):
            require(not batch.is_symlink() and batch.resolve().is_relative_to(work),"Owned batch only")
            try:
                index=int(batch.name.split("-")[-1])
            except ValueError:
                errors.append(dict(namespace=work.name,batch=batch.name,error="invalid batch name"))
                continue
            if index not in saved_batches:
                output=batch/"thirty-nine-condensed-warm"
                named=[("model",output/"model-000.json"),("status",output/"driver-status.json"),
                    ("qp",output/"condensed-QP-summary.json"),
                    ("fd",batch/"physical-response/response-check.json")]
                values={}; identities=[]; local_errors=[]
                for key,path in named:
                    if not path.is_file():
                        values[key]=None; continue
                    identities.append(original_file_receipt(path,path.relative_to(work).as_posix()))
                    try:values[key]=read(path)
                    except Exception as error:
                        values[key]=None
                        local_errors.append(dict(file=path.relative_to(work).as_posix(),error=repr(error)))
                try:
                    status=values["status"] if isinstance(values["status"],dict) else {}
                    report=summarize(reader,values["model"],status,values["qp"],values["fd"])
                    report.update(batch_index=index,actual_surviving_batch=batch.name,
                        actual_namespace=work.name,original_files=identities,
                        readback_errors=local_errors,no_process_exit_or_missing_phase_inferred=True)
                    summaries.append(report)
                except Exception as error:
                    errors.append(dict(namespace=work.name,batch=batch.name,error=repr(error)))
                errors.extend(dict(namespace=work.name,batch=batch.name,**row) for row in local_errors)
            for logfile in sorted(batch.glob("*.stderr.log")):
                record=error_log_readout(logfile)
                error_logs.append(record)
                if record.get("complete_original_stderr_text") is False:
                    errors.append(dict(namespace=work.name,batch=batch.name,
                        error="original stderr exceeds necessary text bound",
                        identity=original_file_receipt(logfile)))
        known_statuses={row.get("produced_pair",{}).get("status_sha256")
            for row in saved if isinstance(row.get("produced_pair"),dict)}
        for carrier in sorted(work.glob("parent-after-*")):
            require(not carrier.is_symlink() and carrier.resolve().is_relative_to(work),"Owned parent only")
            path=carrier/"driver-status.json"
            if not path.is_file() or file_sha(path) in known_statuses:
                continue
            try:
                status=read(path);require(isinstance(status,dict),"Actual status object")
                report=summarize(reader,None,status,None,None)
                report.update(batch_index=None,actual_surviving_parent_carrier=carrier.name,
                    actual_namespace=work.name,original_status_file=original_file_receipt(path),
                    no_model_FD_success_or_completed_handoff_inferred=True)
                summaries.append(report)
            except Exception as error:
                errors.append(dict(namespace=work.name,parent_carrier=carrier.name,error=repr(error)))
    state=dict(readback_only=True,actual_owner_quiescent_before_read=True,
        actual_surviving_namespaces=namespaces,
        actual_saved_chain_states=states,necessary_error_logs=error_logs,
        no_process_exit_or_missing_phase_inferred=True,
        no_surviving_batch_does_not_mean_scientific_success=True,
        this_reader_does_not_delete_original_files=True)
    if not namespaces:
        emit("request206_no_surviving_owned_payload",state)
        return 0
    report=assemble_chain(summaries,state,bindings,errors)
    publish("whole-chain-recovery",report)
    return 0 if not errors else 70


if __name__=="__main__":
    try:
        raise SystemExit(readback_only())
    except ReadbackIncomplete as error:
        emit("request206_readback_incomplete",dict(error=str(error),transport_exit_code=70,
            scientific_result_not_reclassified=True,unread_owned_output_not_deleted=True))
        raise SystemExit(70)
