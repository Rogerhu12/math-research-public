#!/usr/bin/env python3
"""Read actual98 once; print conclusions/hashes; retain no recomputable payload."""
from __future__ import annotations
import argparse
import gzip
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import zipfile

REPOSITORY = "Rogerhu12/math-research-public"
SOURCE_COMMIT = "918fdb11dbb7a424b6149b405e2c7fab3cc0c737"
TRANSPORT_SHA = "51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859"
REQUEST_GIT_BLOB = "6aa7cc61e52b314c31699e8849fb9a9cc5c11b62"
WORKFLOW_GIT_BLOB = "f998c08cc5320559204b7b2d5a67f4f2f1afdc99"
SCHEMA = "actual98-original-scalar-readback-no-payload-retention-v1"
OPTIMIZER_SCHEMA = "exact-constraint-thirty-one-query-condensed-complete-H-warm-v1"
WARM_FROM_ORIGINAL_JOB_LOG = "b59f40c003bf924f3f3c10aa6783425a606b3e395fd86311cbba159b835feb67"
PIN = dict(run_id=43677587785, artifact_id=14147700690,
    artifact_name="visible-followup-condensedqp-43677587785-1",
    expected_size=809042943,
    expected_sha256="9917774d965e86b0a8d46677a1f54c0fb23fc8fa61a67cbab998e7493d33151a")
PRIMARY = {
    "model": "thirty-one-condensed-warm/model-000.json",
    "status": "thirty-one-condensed-warm/driver-status.json",
    "QP": "thirty-one-condensed-warm/condensed-QP-summary.json",
    "FD": "physical-response/response-check.json",
    "warm": "thirty-one-condensed-warm/warm-001.json.gz",
}
MAX_MEMBER = 64 * 1024 * 1024
MAX_DECODED = 128 * 1024 * 1024
MAX_TEXT = 90000
BULK_KEYS = {
    "states", "rhs", "y", "f", "fm", "middle", "vector", "vectors",
    "direction", "directions_raw", "action", "Bz", "z", "z0",
    "physical_values", "original_beta_squared_values", "local_A",
    "resume_producer", "optimization_warm", "producer", "identity", "entry",
    "original_source_and_parent_entry", "original_B_over_C_row_norm",
    "condensed_QP_entry", "thirty_one_query_projection_entry",
    "all_source_sha256", "consumed_source_sha256", "large_arrays",
    "full_array_manifest", "array_manifest", "input_arrays",
}
omitted = []
progress = {"phase": "argument-and-source-identity", "artifact": dict(PIN)}

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def git_blob(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()

def require(ok, message):
    if not ok:
        raise ValueError(message)

def parsed(raw):
    # Original non-standard nonfinite JSON tokens remain explicit strings.
    return json.loads(raw, parse_constant=lambda s: {"original_nonfinite_JSON_token": s})

def scalar(value):
    return value is None or isinstance(value, (str, int, float, bool))

def shallow(value):
    return {k: v for k, v in value.items() if scalar(v)} if isinstance(value, dict) else value

def omitted_record(path, value, reason):
    item = {"path": path, "reason": reason}
    if isinstance(value, (dict, list, str)):
        item["item_or_character_count"] = len(value)
    omitted.append(item)
    return {"summary_omitted": True, "reason": reason}

def brief(value, path="", depth=0):
    """Copy metadata only. Complete original file hashes bind every omitted field."""
    if scalar(value):
        if isinstance(value, str) and len(value) > 3000:
            return omitted_record(path, value, "long original text")
        return value
    if depth > 12:
        return omitted_record(path, value, "deep metadata; original file remains hash-bound")
    if isinstance(value, list):
        if len(value) > 128:
            return omitted_record(path, value, "bulk list; no numerical vector is retained")
        return [brief(v, path+"/"+str(i), depth+1) for i, v in enumerate(value)]
    if isinstance(value, dict):
        # Existing external ndarray descriptors are identity metadata, not arrays.
        answer = {}
        for k, v in value.items():
            p = path+"/"+k.replace("~", "~0").replace("/", "~1")
            if k in BULK_KEYS:
                omitted_record(p, v, "bulk data or historical producer tree")
                continue
            answer[k] = brief(v, p, depth+1)
        return answer
    raise TypeError("Only original JSON values can be summarized")

def at(value, path):
    current = value
    for key in path:
        if not isinstance(current, dict) or key not in current:
            return None
        current = current[key]
    return current

def identity_pick(value):
    if not isinstance(value, dict):
        return None
    keys = (
        "entry_source_sha256", "source_sha256", "optimizer_schema",
        "actual_parent_warm_sha256", "actual_parent_status_sha256",
        "actual_resume_sha256", "parent_optimizer_schema", "actual_parent_schema",
        "original_full_coordinate_count", "full_original_coordinate_count",
        "full_B_local_dimension", "C_projection_dimension", "constraint_rows",
        "selected_query_count", "selected_angle_row_count", "physical_angles_per_query",
        "complete_B_physical_nodes", "complete_B_outside_C_nodes",
        "actual_query_endpoint_nodes", "fixed_projection_physical_nodes",
        "expected_complete_B_local_dimension", "expected_fixed_projection_dimension",
        "actual_current_B_C_layout", "nonlinear_native_H_solved",
        "nonlinear_native_solved", "query_specs", "local_QP_budgets",
    )
    return {key: brief(value[key], "/selected_identity/"+key)
            for key in keys if key in value}

def load_transport(path):
    raw = path.read_bytes()
    require(sha(raw) == TRANSPORT_SHA, "Frozen byte transport source SHA mismatch")
    spec = importlib.util.spec_from_file_location("_actual98_private_byte_transport", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.PIN = dict(PIN)
    return module

def zip_index(archive, transport):
    index, kinds = {}, {}
    for info in archive.infolist():
        name, parts, is_directory = transport.safe_member_name(info)
        require(name not in kinds, "Duplicate ZIP path")
        kinds[name] = is_directory
        if not is_directory:
            index[name] = info
    for name in kinds:
        parts = name.split("/")
        for i in range(1, len(parts)):
            ancestor = "/".join(parts[:i])
            require(kinds.get(ancestor, True), "ZIP file/ancestor conflict")
    return index, len(kinds)

def read_primary(archive, index, suffix, label):
    alternatives = [suffix] if suffix.endswith(".gz") else [suffix, suffix+".gz"]
    matches = [name for name in index
        if any(name == s or name.endswith("/"+s) for s in alternatives)]
    require(len(matches) <= 1, "Ambiguous original primary member: "+label)
    if not matches:
        return None, {"missing": True, "logical_path": suffix}
    name = matches[0]
    info = index[name]
    require(info.file_size <= MAX_MEMBER, "Primary member exceeds metadata read budget")
    with archive.open(info) as stream:
        raw = stream.read(MAX_MEMBER+1)
        require(len(raw) == info.file_size and len(raw) <= MAX_MEMBER,
            "Incomplete original primary member")
    if raw[:2] == b"\x1f\x8b":
        with gzip.GzipFile(fileobj=io.BytesIO(raw)) as stream:
            decoded = stream.read(MAX_DECODED+1)
        require(len(decoded) <= MAX_DECODED, "Decompressed primary exceeds read budget")
    else:
        decoded = raw
    value = parsed(decoded)
    require(isinstance(value, dict), "Original primary JSON is not an object")
    return value, dict(file=name, bytes=len(raw), sha256=sha(raw),
        decoded_bytes=len(decoded), decoded_sha256=sha(decoded),
        selected_member_CRC_checked_by_complete_zipfile_read=True,
        raw_member_retained=False, decoded_JSON_retained=False)

def copy_trials(model):
    source = model.get("trials")
    require(isinstance(source, list), "Original model.trials is missing")
    answer = []
    for i, trial in enumerate(source):
        require(isinstance(trial, dict), "Original trial must be an object")
        record = {"original_trial_index": i, **shallow(trial)}
        for key in ("selected_linear_beta_squared", "all_selected_linear_reserve_slack",
                    "domain", "actual_selected_original_angles",
                    "complete_original_RMS_query_domain",
                    "independent_actual_directional_check"):
            record[key+"_present_in_original"] = key in trial
            if key in trial:
                record[key] = brief(trial[key], "/model/trials/"+str(i)+"/"+key)
        answer.append(record)
    return answer

def assemble(objects, receipts, request, source_receipts, official, downloaded):
    model, status, qp, fd, warm = [objects[k] for k in ("model", "status", "QP", "FD", "warm")]
    require(model is not None and status is not None, "No original model/status to read")
    checks = []
    def check(label, ok):
        checks.append(dict(label=label, passed=bool(ok)))
    check("status optimizer schema", status.get("schema") == OPTIMIZER_SCHEMA)
    if isinstance(status.get("iterations"), list) and status["iterations"]:
        check("status embeds exact original model object", status["iterations"][0] == model)
    else:
        checks.append(dict(label="status embeds original model", present=False))
    if warm is not None:
        check("warm compressed bytes agree with original job log",
              receipts["warm"]["sha256"] == WARM_FROM_ORIGINAL_JOB_LOG)
        check("status current warm SHA", status.get("latest_warm_sha256") == receipts["warm"]["sha256"])
        check("status current warm basename", status.get("latest_warm_file") == "warm-001.json.gz")
        if fd is not None:
            check("FD prepared SHA is this actual new warm",
                  fd.get("prepared_sha256") == receipts["warm"]["sha256"])
    expected = request["source_sha256"]
    if fd is not None:
        actual = fd.get("consumed_source_sha256", {})
        require(isinstance(actual, dict), "Original FD source mapping invalid")
        source_checks = {name: digest == expected[name] for name, digest in actual.items()
                         if name in expected}
    else:
        source_checks = {}
    model_summary = shallow(model)
    if "before" in model:
        model_summary["before"] = brief(model["before"], "/model/before")
    model_summary["trials"] = copy_trials(model)
    for key in ("selection", "direction_selection", "lsmr", "linearization_check",
                "operator_adjoint_check", "B_directional_check", "baseline_C_projection",
                "chosen_direction", "projection", "selected_direction"):
        if key in model:
            model_summary[key] = brief(model[key], "/model/"+key)
    fd_summary = None
    if fd is not None:
        fd_summary = shallow(fd)
        fd_summary["recorded_consumed_source_sha256"] = fd.get("consumed_source_sha256")
        for key in ("direct_boundary", "separated_boundary"):
            if key in fd:
                fd_summary[key] = brief(fd[key], "/FD/"+key)
        fd_summary["thirty_one_query_response_identity"] = identity_pick(
            fd.get("thirty_one_query_condensed_QP_response_entry"))
    qp_summary = None
    if qp is not None:
        qp_summary = shallow(qp)
        for key in ("comparison", "local_QP_report", "last_saved_local_stage",
                    "condensation_report"):
            if key in qp:
                qp_summary[key] = brief(qp[key], "/QP/"+key)
    identities = {
        "model_entry": identity_pick(model.get("condensed_QP_entry")),
        "status_entry": identity_pick(at(status, ("identity", "condensed_QP_entry"))),
        "status_thirty_one": identity_pick(at(status, ("identity", "thirty_one_query_projection_entry"))),
        "warm_entry": identity_pick(warm.get("condensed_QP_entry")) if warm else None,
        "warm_optimizer": identity_pick(warm.get("optimization_warm")) if warm else None,
        "warm_thirty_one": identity_pick(at(warm, ("optimization_warm", "thirty_one_query_projection_entry"))) if warm else None,
    }
    # Metadata comparison only. No missing relation is converted into a pass.
    result = dict(schema=SCHEMA, source_sha256=sha(Path(__file__).read_bytes()),
        original_run=PIN["run_id"], original_job=132701028492,
        original_source_commit=SOURCE_COMMIT, artifact=PIN,
        official_artifact=official, verified_download=downloaded,
        primary_files=receipts, original_request_and_workflow=source_receipts,
        original_request_parameters={k: request[k] for k in (
            "request", "optimizer_schema", "query_specs", "declared_budgets",
            "actual_parent_run", "actual_parent_source_commit", "actual_parent_schema",
            "actual_parent_warm_sha256", "actual_parent_status_sha256",
            "expected_complete_B_local_dimension",
            "expected_baseline_C_dimension_from_frozen_support_formula",
            "complete_B_outside_C_nodes", "baseline_C_support_nodes",
            "scientific_thresholds_changed", "native_tail_requested",
        ) if k in request},
        status=shallow(status), model=model_summary, QP=qp_summary, FD=fd_summary,
        actual_producer_identity=identities, identity_checks=checks,
        common_FD_request_source_pin_checks=source_checks,
        all_reported_identity_checks_passed=all(x.get("passed", True) for x in checks)
            and all(source_checks.values()),
        root_science_count=0, new_scientific_imports=0,
        new_RHS_Jacobian_ODE_FD_or_solver_calls=0,
        numerical_fields_copied_from_original_JSON_without_recomputation=True,
        complete_existing_ZIP_SHA_verified=True,
        unused_ZIP_members_individually_decompressed_or_CRC_checked=False,
        full_arrays_audited=False, science_acceptance_reclassified=False,
        raw_payload_retained_or_republished=False,
        Release_uploads=0, Git_mutations=0, new_artifact_uploads=0,
        summary_scope="Original scalar conclusion and identity readback only; not full payload audit or BVP acceptance")
    result["metadata_omissions"] = omitted
    return result

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--transport", type=Path, required=True)
    parser.add_argument("--request98", type=Path, required=True)
    parser.add_argument("--workflow98", type=Path, required=True)
    args = parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true", "Actions-only metadata readback")
    require(os.environ.get("GITHUB_REPOSITORY") == REPOSITORY, "Expected public repository")
    require(sys.platform.startswith("linux"), "Original Linux byte transport")
    token = os.environ.get("GITHUB_TOKEN")
    require(bool(token), "A read-only Actions token is required")
    runner_temp = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    rraw, wraw = args.request98.read_bytes(), args.workflow98.read_bytes()
    require(git_blob(rraw) == REQUEST_GIT_BLOB, "Original request98 Git blob mismatch")
    require(git_blob(wraw) == WORKFLOW_GIT_BLOB, "Original workflow98 Git blob mismatch")
    request = parsed(rraw)
    require(request.get("request") == 98, "Original request number mismatch")
    receipts = dict(request98=dict(git_blob=REQUEST_GIT_BLOB, bytes=len(rraw), sha256=sha(rraw)),
                    workflow98=dict(git_blob=WORKFLOW_GIT_BLOB, bytes=len(wraw), sha256=sha(wraw)))
    transport = load_transport(args.transport)
    opener = transport.make_opener()
    progress["phase"] = "official-artifact-metadata"
    metadata, canonical = transport.read_metadata(opener, token)
    progress["official_artifact"] = transport.public_metadata(metadata)
    require(metadata["workflow_run"].get("head_sha") == SOURCE_COMMIT,
            "Original artifact source commit mismatch")
    with tempfile.TemporaryDirectory(prefix="existing98-read-only-", dir=runner_temp) as work:
        archive_path = Path(work)/"actual98.zip"
        state = {}
        progress["phase"] = "verified-download"
        downloaded = transport.download_archive(opener, token, canonical, archive_path, state)
        progress["verified_download"] = downloaded
        print("actual98 complete ZIP size and SHA verified; reading five primary members", flush=True)
        with zipfile.ZipFile(archive_path, "r") as archive:
            index, member_count = zip_index(archive, transport)
            objects, primary_receipts = {}, {}
            progress["phase"] = "original-primary-member-read"
            progress["primary_files"] = primary_receipts
            for label, suffix in PRIMARY.items():
                objects[label], primary_receipts[label] = read_primary(archive, index, suffix, label)
        progress["phase"] = "original-scalar-and-identity-readback"
        result = assemble(objects, primary_receipts, request, receipts,
                          transport.public_metadata(metadata), downloaded)
        result["ZIP_central_directory_entry_count"] = member_count
        result["owned_temporary_payload_cleanup"] = "completed before this summary is emitted"
        encoded = (json.dumps(result, ensure_ascii=True, indent=2, allow_nan=False)+"\n").encode("utf-8")
        progress["summary_bytes"] = len(encoded)
        progress["summary_sha256"] = sha(encoded)
        require(len(encoded) <= MAX_TEXT, "Scalar summary exceeds 90000-byte output budget; no trial data was silently truncated")
    # Temporary ZIP has been removed; no retained payload or external mutation.
    print("BEGIN_ACTUAL98_SCALAR_SUMMARY")
    sys.stdout.write(encoded.decode("utf-8"))
    print("END_ACTUAL98_SCALAR_SUMMARY")
    print(json.dumps(dict(event="actual98_scalar_summary_identity",
        bytes=len(encoded), sha256=sha(encoded), payload_files_retained=0), sort_keys=True))
    return 0 if result["all_reported_identity_checks_passed"] else 2

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        # Do not print response bodies, signed URLs, credentials or arbitrary repr.
        safe = str(error) if isinstance(error, (ValueError, TypeError)) else type(error).__name__
        print(json.dumps(dict(schema=SCHEMA, readback_completed=False,
            error_type=type(error).__name__, diagnostic=safe,
            original_identity_progress=progress,
            scientific_conclusion_inferred_from_readback_failure=False)), flush=True)
        raise SystemExit(2)
