#!/usr/bin/env python3
"""Read the already completed actual62 artifact; never rerun mathematics.

This entry runs only in Rogerhu12/math-research-public Actions.  It uses
the unchanged SHA-locked public-artifact transport for the complete ZIP,
safe extraction, every member CRC/size/SHA, and read-only publication.
The sole adapter changes are the explicit artifact/source pin and truthful
adapter provenance.  No scientific source is imported.

JSON readout copies original scalar diagnostics.  NumPy is used only for
NPZ decoding, dtype/shape/byte conversion and hashing.  There is no RHS,
Jacobian, ODE, boundary, norm, dot product, QR, optimization, or finite
difference call.  Complete large audit records remain artifact-only.
Small result/trial/FD reports are written before optional byte auditing;
an audit failure does not erase the observations already recovered.
"""
from __future__ import annotations

import argparse
import datetime
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import sys
import traceback

REPOSITORY = "Rogerhu12/math-research-public"
KERNEL_NAME = "exact_20261114_fetch_pinned_public_artifact.py"
KERNEL_SHA = "51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859"
KERNEL_SCHEMA = "pinned-public-actions-artifact-fetch-v3"
PIN = dict(run_id=43642866864, artifact_id=14132473712,
    artifact_name="visible-followup-condensedqp-43642866864-1",
    expected_size=492837872,
    expected_sha256="220ad8c51a147942b663cd9196f009ecc976d1ff270b0348e494e08cf5e90730")
SOURCE_COMMIT = "cc813fa7521098fdeba86b8bf8c0fe7d8c96bba0"
WARM_DIR = "eighteen-condensed-warm"
PARENT_WARM_SHA = "bc7cadbc17f17832785ace32b011136fd43c04147d450d557730de0f05d40a23"
PARENT_STATUS_SHA = "5b419af7340777328184d7699cf1a4de539cd608c889f6e4f81fe549b253a922"
SCHEMA = "actual62-completed-artifact-readback-and-byte-audit-v1"
PRODUCER_SCHEMA = "exact-constraint-eighteen-query-condensed-complete-H-warm-v1"
ENTRY_PINS = {
    "geometry_20261114_eighteen_query_domain_operator.py":
        "ec43c049542f523e1c4f2b1956c07a9216497eb066a8f6f22ceddd8f11e2c051",
    "geometry_20261114_eighteen_query_condensed_warm.py":
        "b9f7d9150c57cff485f5f891881870095fc91f7a58fd40f63544e6bb9c3ef335",
    "geometry_20261114_eighteen_query_condensed_response.py":
        "5885daeced8a8961f7f12d259ed5479683e7fd8dc2cccb8a2873ac9424918c9e",
    "geometry_20261114_eighteen_query_collocation_observer_warm.py":
        "6ad75ce4b350aee4ae52afe2c6045f50d657931419ef7c4b46d0758db3acd1ca",
}
CHUNK = 1024 * 1024
OMIT = {"entry", "identity", "resume_producer", "optimization_warm",
    "source_sha256", "consumed_source_sha256", "frozen_dependencies",
    "condensed_QP_entry", "read_only_collocation_observer_entry",
    "original_source_and_parent_entry", "source_files", "sources",
    "compiled_blocks", "query_gradients", "original_functions",
    "files", "parts", "arrays", "array_identity", "input_binding",
    "actual_selected_original_angles_after", "complete_scalar_profile"}

class AuditError(RuntimeError):
    pass

def require(condition, label):
    if not condition:
        raise AuditError(label)

def sha(path):
    digest = hashlib.sha256()
    with open(path, "rb") as stream:
        for block in iter(lambda: stream.read(CHUNK), b""):
            digest.update(block)
    return digest.hexdigest()

def json_bytes(value):
    return (json.dumps(value, indent=2, ensure_ascii=False,
        allow_nan=False) + "\n").encode("utf-8")

def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
        ensure_ascii=False, allow_nan=False).encode("utf-8")

def write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = json_bytes(value)
    path.write_bytes(raw)
    return dict(file=path.name, bytes=len(raw),
        sha256=hashlib.sha256(raw).hexdigest())

def decoded_bytes(path):
    path = Path(path)
    with open(path, "rb") as stream:
        magic = stream.read(2)
    if magic == b"\x1f\x8b":
        with gzip.open(path, "rb") as stream:
            return stream.read()
    return path.read_bytes()

def read(path):
    return json.loads(decoded_bytes(path))

def original_json_path(directory, basename):
    for name in (basename, basename + ".gz"):
        path = Path(directory) / name
        if path.is_file():
            return path
    raise AuditError("Missing original JSON or its transparent gzip: " + basename)

def receipt(path, root):
    path = Path(path)
    return dict(file=str(path.relative_to(root)), bytes=path.stat().st_size,
        sha256=sha(path))

def safe_path(base, name):
    require(isinstance(name, str) and name != "", "Required relative payload path")
    part = Path(name)
    require(not part.is_absolute() and ".." not in part.parts,
        "Payload descriptor must stay in its declared directory")
    path = base / part
    require(path.is_file() and not path.is_symlink(), "Regular original payload required")
    require(path.resolve().is_relative_to(base.resolve()), "Payload path escapes directory")
    return path

def scalars(value):
    if not isinstance(value, dict):
        return {}
    return {k:v for k,v in value.items()
        if k not in OMIT and (v is None or isinstance(v, (bool,int,float,str)))
        and (not isinstance(v,str) or len(v) <= 1000)}

def compact(value, depth=0, key=""):
    """Bounded semantic scalar view, never a segmented copy of a large tree."""
    if value is None or isinstance(value, (bool,int,float)):
        return value
    if isinstance(value, str):
        return value if len(value) <= 1000 else dict(original_string_length=len(value))
    if depth > 7:
        return dict(original_metadata_retained_in_pinned_artifact=True)
    if isinstance(value, dict):
        if {"shape","dtype","sha256"}.issubset(value):
            return {k:value[k] for k in ("shape","dtype","sha256","bytes") if k in value}
        return {k:compact(v,depth+1,k) for k,v in value.items() if k not in OMIT}
    if isinstance(value, list):
        if len(value) > 64:
            return dict(original_entries=len(value),
                values_retained_in_pinned_artifact=True)
        return [compact(v,depth+1,key) for v in value]
    raise AuditError("Unexpected non-JSON readout type")

def walk(value, path=()):
    yield path, value
    if isinstance(value, dict):
        for key, child in value.items():
            yield from walk(child, path+(str(key),))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk(child, path+(str(index),))

def subset(actual, expected, label):
    require(isinstance(actual,dict) and isinstance(expected,dict), label+" object")
    for key, value in expected.items():
        require(key in actual and actual[key] == value, label+" key "+key)

def descriptor_file(base, descriptor):
    name = descriptor.get("file", descriptor.get("path"))
    path = safe_path(base, name)
    require(sha(path) == descriptor["sha256"], "Original descriptor file SHA: "+str(name))
    if "bytes" in descriptor:
        require(path.stat().st_size == descriptor["bytes"], "Original descriptor file size: "+str(name))
    return path

def fetch_original(args):
    here = Path(__file__).resolve().parent
    path = here/KERNEL_NAME
    require(sha(path) == KERNEL_SHA, "Unchanged pinned public transport source")
    spec = importlib.util.spec_from_file_location("_actual62_receipt_transport",path)
    require(spec is not None and spec.loader is not None, "Public transport import interface")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    require(module.REPOSITORY == REPOSITORY and module.SCHEMA == KERNEL_SCHEMA,
        "Public transport repository/schema")
    old_metadata = module.read_metadata
    def metadata(opener, token):
        value, url = old_metadata(opener, token)
        require(value["workflow_run"].get("head_sha") == SOURCE_COMMIT,
            "Original completed run source commit")
        return value, url
    old_public = module.public_metadata
    def public(value):
        result = old_public(value)
        result["readback_adapter_not_GitHub_metadata"] = dict(
            schema=SCHEMA, source_file=Path(__file__).name,
            source_sha256=sha(__file__), original_transport_source_sha256=KERNEL_SHA,
            only_pin_metadata_and_schema_changed_in_memory=True,
            full_original_extraction_unchanged=True,
            mathematical_computation_performed=False)
        return result
    module.PIN = dict(PIN)
    module.SCHEMA = "actual62-pinned-complete-public-artifact-fetch-v1"
    module.read_metadata, module.public_metadata = metadata, public
    old_argv = sys.argv
    supplied = [str(path)]
    for key, value in PIN.items():
        supplied += ["--"+key.replace("_","-"), str(value)]
    supplied += ["--out", str(args.download_out)]
    try:
        sys.argv = supplied
        code = module.main()
    finally:
        sys.argv = old_argv
    require(code == 0, "Complete pinned artifact transport did not succeed")
    root = args.download_out
    item = read(root/module.RECEIPT_NAME)
    require(item["success"] is True and item["pinned_input"] == PIN,
        "Complete transport receipt pin")
    require(item["download"]["actual_sha256"] == PIN["expected_sha256"],
        "Complete archive original bytes")
    return root, item

def selected_domain(report):
    if not isinstance(report,dict):
        return None
    out = scalars(report)
    for key in ("original_RMS_query_checks",):
        if key in report:
            out[key] = compact(report[key])
    for key, value in report.items():
        if "midpoint" in key.lower() and isinstance(value,dict):
            out[key] = compact(value)
    observer = report.get("read_only_collocation_location_observer")
    if isinstance(observer,dict):
        out["read_only_collocation_location_observer"] = {
            **scalars(observer),
            "full_physical_argmax":compact(observer.get("full_physical_argmax")),
            "complete_residual_argmax":compact(observer.get("complete_residual_argmax"))}
    return out

def readout(root, out):
    directory = root/WARM_DIR
    status_path = original_json_path(directory, "driver-status.json")
    status_raw = decoded_bytes(status_path)
    status = json.loads(status_raw)
    write(out/"actual62-original-status-provisional.json",dict(
        schema=SCHEMA, original_status_scalars=scalars(status),
        original_status_file=receipt(status_path,root),
        original_status_decoded_sha256=hashlib.sha256(status_raw).hexdigest(),
        producer_and_array_validation_not_yet_completed=True,
        mathematical_computation_performed=False))
    require(status.get("schema") == PRODUCER_SCHEMA, "Actual62 producer schema")
    model = read(directory/"model-000.json")
    require(len(status.get("iterations",[])) == 1, "One original saved model")
    for key in ("iteration","before","trials"):
        require(status["iterations"][0].get(key) == model.get(key),
            "Original status/model same saved "+key)
    warm_path = safe_path(directory,status["latest_warm_file"])
    require(sha(warm_path) == status["latest_warm_sha256"], "Actual62 saved warm SHA")
    warm = read(warm_path)
    parent_dir = root/"parent60"
    parent_path = parent_dir/"warm-001.json.gz"
    parent_status_path = original_json_path(parent_dir,"driver-status.json")
    parent_status_raw = decoded_bytes(parent_status_path)
    require(sha(parent_path) == PARENT_WARM_SHA, "Original actual60 parent warm")
    require(hashlib.sha256(parent_status_raw).hexdigest() == PARENT_STATUS_SHA,
        "Transparent restored actual60 status bytes")
    parent = read(parent_path)
    parent_status = json.loads(parent_status_raw)
    require(parent_status["latest_warm_sha256"] == PARENT_WARM_SHA, "Parent pair binding")
    subset(parent["optimization_warm"], parent_status["identity"], "Parent status producer")
    require(status["identity"]["resume_producer"] == parent["optimization_warm"],
        "Complete original parent producer subtree")
    subset(warm["optimization_warm"], status["identity"], "Actual62 status producer")
    fd_path = root/"physical-response"/"response-check.json"
    fd = read(fd_path)
    require(fd["prepared_sha256"] == status["latest_warm_sha256"], "Actual62 FD new warm binding")
    require(fd["optimization_warm"] == warm["optimization_warm"], "FD complete producer identity")
    comparison = read(directory/"condensed-versus-C-comparison.json")
    qp_summary = read(directory/"condensed-QP-summary.json")
    qp_scalar = dict(comparison=scalars(comparison),
        original_C_selection_scalars=scalars(comparison.get("original_C_selection")),
        selected_selection_scalars=scalars(comparison.get("condensed_candidate_selection")),
        final_actual_full_model_evidence=compact(comparison.get("final_actual_full_model_evidence")),
        local_QP_report_scalars=scalars(qp_summary.get("local_QP_report")),
        last_saved_local_stage=compact(qp_summary.get("last_saved_local_stage")),
        condensation_report_scalars=scalars(qp_summary.get("condensation_report")),
        last_recovery_scalars=scalars(qp_summary.get("condensation_report",{}).get("last_recovery")))
    write(out/"actual62-original-QP-scalars.json",qp_scalar)
    trials = []
    for original in model["trials"]:
        row = scalars(original)
        for key in ("selected_linear_beta_squared","all_selected_linear_reserve_slack",
                "independent_actual_directional_check"):
            if key in original:
                row[key] = compact(original[key])
        for key in ("domain","complete_original_RMS_query_domain"):
            if key in original:
                row[key] = selected_domain(original[key])
        row["actual_selected_original_angles"] = [
            {**scalars(x), "original_beta_squared":compact(x.get("original_beta_squared"))}
            for x in original.get("actual_selected_original_angles",[])]
        if "selected_angle_values" in original:
            descriptor_file(directory,original["selected_angle_values"])
            row["selected_angle_values"] = original["selected_angle_values"]
        trials.append(row)
    trial_doc = dict(schema=SCHEMA, source="original model-000.json, no evaluation",
        before=selected_domain(model["before"]), original_model_scalars=scalars(model),
        all_original_trials=trials)
    write(out/"actual62-original-trials.json",trial_doc)
    fd_small = dict(schema=SCHEMA, **scalars(fd),
        direct_boundary=scalars(fd.get("direct_boundary")),
        separated_boundary=scalars(fd.get("separated_boundary")),
        response_file=receipt(fd_path,root),
        actual_warm_native_height=fd.get("actual_warm_native_height"),
        source_ledger=fd.get("consumed_source_sha256"),
        original_complete_producer_canon_sha256=
            hashlib.sha256(canonical(fd["optimization_warm"])).hexdigest())
    write(out/"actual62-original-FD.json",fd_small)
    accepted = [row for row in trials if row.get("accepted") is True]
    nearest = None
    if accepted:
        at = trials.index(accepted[-1])
        if at > 0:
            nearest = trials[at-1]
    summary = dict(schema=SCHEMA, completed=False,
        original_artifact_pin=PIN, original_source_commit=SOURCE_COMMIT,
        source_file=Path(__file__).name, source_sha256=sha(__file__),
        mathematical_computation_performed=False,
        original_status=scalars(status),
        original_model_scalars=scalars(model),
        original_status_file=receipt(status_path,root),
        original_status_decoded_bytes=len(status_raw),
        original_status_decoded_sha256=hashlib.sha256(status_raw).hexdigest(),
        actual_new_warm=receipt(warm_path,root),
        parent_warm=receipt(parent_path,root),
        original_parent_status_decoded_sha256=hashlib.sha256(parent_status_raw).hexdigest(),
        actual_new_warm_flags={k:warm.get(k) for k in (
            "success","new_coupled_finite_acceptance","complete_closed_surface",
            "finite_boundary_scheme","source_sha256","initial_collocation_max")},
        full_original_parent_producer_retained=True,
        status_and_newwarm_and_FD_original_producer_bound=True,
        trial_count=len(trials), accepted_trial=accepted[-1] if accepted else None,
        nearest_previous_rejected_trial=nearest,
        original_FD_summary=scalars(fd),
        original_QP_comparison_scalars=scalars(comparison),
        original_QP_last_unrepaired=compact(qp_summary.get("last_saved_local_stage",{}).get("actual_unrepaired")),
        original_QP_local_radial=compact(qp_summary.get("last_saved_local_stage",{}).get("local_only_radial_repair")),
        original_QP_global_radial=compact(comparison.get("condensed_candidate_selection",{}).get("projected_candidate_feasibility_repair")),
        sources_and_full_arrays_are_audited_separately=True,
        full_factor_array_files_not_exported_by_original_producer=True,
        byte_audit_completed=False)
    write(out/"actual62-readback.json",summary)
    return dict(root=root, directory=directory, status=status, model=model,
        warm=warm, parent=parent, parent_status=parent_status, fd=fd, summary=summary)

def array_header(shape, dtype):
    digest = hashlib.sha256()
    digest.update(str(tuple(shape)).encode("ascii"))
    digest.update(b"\0")
    digest.update(dtype.encode("ascii"))
    digest.update(b"\0")
    return digest

def array_identity(array):
    digest = array_header(array.shape,array.dtype.str)
    raw = array.tobytes(order="C")
    digest.update(raw)
    return dict(shape=list(array.shape),dtype=array.dtype.str,
        bytes=int(array.nbytes),sha256=digest.hexdigest(),
        raw_sha256=hashlib.sha256(raw).hexdigest())

def check_array(actual, descriptor, label):
    ident = array_identity(actual)
    for key in ("shape","dtype","bytes","sha256"):
        if key in descriptor:
            require(ident[key] == descriptor[key], label+" "+key)
    if "raw_sha256" in descriptor:
        require(ident["raw_sha256"] == descriptor["raw_sha256"],label+" raw SHA")
    return ident

def npz_file(base, item, np, label):
    path = descriptor_file(base,item)
    result = dict(file=str(path.relative_to(base)),sha256=item["sha256"],
        bytes=path.stat().st_size,arrays={})
    with np.load(path,allow_pickle=False) as archive:
        require(len(archive.files) == len(set(archive.files)),label+" duplicate NPY name")
        descriptors = item.get("arrays")
        if descriptors is None:
            require(archive.files == ["actual"],label+" exact original actual member")
            descriptors = {"actual":item["array"]}
        require(set(archive.files) == set(descriptors),label+" complete member names")
        for key, descriptor in descriptors.items():
            result["arrays"][key] = check_array(archive[key],descriptor,label+"/"+key)
    return result

def combine_parts(base, parts, member, descriptor, np, label):
    digest = array_header(descriptor["shape"],descriptor["dtype"])
    raw_digest, total, leading = hashlib.sha256(), 0, 0
    for item in parts:
        path = safe_path(base,item.get("file",item.get("path")))
        with np.load(path,allow_pickle=False) as archive:
            value = archive[member]
            require(value.dtype.str == descriptor["dtype"],label+" assembled dtype")
            require(list(value.shape[1:]) == descriptor["shape"][1:],label+" trailing shape")
            if "leading_slice" in item and item["leading_slice"] is not None:
                lo,hi = item["leading_slice"]
                require(lo == leading and hi-lo == value.shape[0],label+" leading slices")
            raw = value.tobytes(order="C")
            digest.update(raw); raw_digest.update(raw); total += len(raw)
            leading += value.shape[0] if value.ndim else 1
    if descriptor["shape"]:
        require(leading == descriptor["shape"][0],label+" full leading count")
    require(total == descriptor["bytes"],label+" full byte count")
    require(digest.hexdigest() == descriptor["sha256"],label+" full identity SHA")
    return dict(label=label,shape=descriptor["shape"],dtype=descriptor["dtype"],
        bytes=total,sha256=digest.hexdigest(),raw_sha256=raw_digest.hexdigest(),parts=len(parts))

def source_audit(context, repository_root):
    topic = repository_root/"topics"/"visible-flex-larger-amplitude"
    supplied = {}
    for obj in (context["status"],context["fd"]):
        for route,value in walk(obj):
            if isinstance(value,dict):
                for key,digest in value.items():
                    if (isinstance(key,str) and key.endswith((".py",".mjs"))
                            and isinstance(digest,str) and re.fullmatch("[0-9a-f]{64}",digest)):
                        supplied.setdefault(key,set()).add(digest)
    for name,digest in ENTRY_PINS.items():
        supplied.setdefault(name,set()).add(digest)
    reports = []
    for name,digests in sorted(supplied.items()):
        require(len(digests)==1,"Conflicting frozen source digest: "+name)
        expected = next(iter(digests))
        candidates = [topic/"computations"/name,topic/"repro"/"source-root"/name]
        existing = [p for p in candidates if p.is_file()]
        if not existing:
            reports.append(dict(source=name,expected_sha256=expected,
                verified=False,reason="not present in this receipt checkout",
                producer_claim_retained_not_independent_file_audit=True))
            require(name not in ENTRY_PINS,"Required current entry source absent")
            continue
        actual = sha(existing[0])
        require(actual==expected,"Frozen consumed source SHA: "+name)
        reports.append(dict(source=name,expected_sha256=expected,sha256=actual,
            path=str(existing[0].relative_to(repository_root)),verified=True))
    return reports

def audit_domain(context,np):
    directory = context["directory"]/"domain-operator"
    path = directory/"manifest.json"
    manifest = read(path)
    require(sha(path)==context["model"]["domain_operator_export"]["manifest_sha256"],
        "Original domain manifest binding")
    require(manifest["shape"] == [36864,236036] and manifest["local_shape"] == [36864,5749],
        "Actual18 full/local domain dimensions")
    files = [npz_file(directory,x,np,"domain") for x in manifest["files"]]
    groups = {}
    for item in manifest["files"]:
        q = item.get("query")
        if isinstance(q,dict) and "query_index" in q and "rows" in item.get("arrays",{}):
            groups.setdefault(q["query_index"],[]).append(item)
    require(sorted(groups) == list(range(18)),"All eighteen typed query groups")
    combinations = []
    all_beta_parts = []
    for index in range(18):
        parts = sorted(groups[index],key=lambda x:x["path"])
        block = manifest["compiled_blocks"][index]
        gradient = manifest["query_gradients"][index]
        for key,descriptor in (("rows",block["rows"]),("Gamma",gradient["Gamma"]),
                               ("Pi",gradient["Pi"])):
            combinations.append(combine_parts(directory,parts,key,descriptor,np,
                "query-"+str(index)+"/"+key))
        for part in parts:
            for key in ("global_columns","local_columns"):
                require(part["arrays"][key]["sha256"] == block[key]["sha256"],
                    "Every query part keeps complete column identity")
        all_beta_parts.extend(parts)
    combinations.append(combine_parts(directory,all_beta_parts,"beta_squared",
        manifest["beta_squared"],np,"all-typed-query-beta"))
    model = dict(schema=manifest["schema"],sources=manifest["source_sha256"],
        base=manifest["base_identity"],query_specs=manifest["query_specs"],
        query_reports=manifest["queries"],
        original_midpoint_base=manifest["original_midpoint_base_identity"],
        N=manifest["angular_grid_size"],beta_squared=manifest["beta_squared"],
        blocks=manifest["compiled_blocks"],
        unchanged_left_component_model_sha256=manifest["unchanged_left_component_model_sha256"],
        original_unit_jet_sha256=manifest["original_unit_jet_sha256"],
        midpoint_unit_jet_sha256=manifest["midpoint_original_unit_jet_sha256"])
    # The producer's identity uses json.dumps defaults for ensure_ascii.
    model_sha = hashlib.sha256(json.dumps(model,sort_keys=True,
        separators=(",",":"),allow_nan=False).encode()).hexdigest()
    require(model_sha==manifest["model_sha256"],"Complete original finite B model metadata")
    basepath=directory/"base-and-local-layout.npz"
    with np.load(basepath,allow_pickle=False) as base:
        for key,source_key in (("mesh","mesh"),("y","states"),("rhs","rhs")):
            require(source_key in context["parent"],"Parent checkpoint "+source_key)
            original=np.asarray(context["parent"][source_key],dtype=base[key].dtype)
            require(array_identity(original)==array_identity(base[key]),
                "Original actual60 parent "+source_key+" exactly matches B base")
    return dict(manifest=receipt(path,context["root"]),model_sha256=model_sha,
        file_count=len(files),array_count=sum(len(x["arrays"]) for x in files),
        files=files,complete_group_byte_combinations=combinations,
        original_saved_checks=compact(read(context["directory"]/"full-angle-operator-check.json")),
        capture=compact(manifest["capture"]),
        no_matrix_action_performed=True)

def audit_condensed(context,np):
    directory=context["directory"]
    path=directory/"condensed-array-manifest.json"
    manifest=read(path)
    result_path=descriptor_file(directory,manifest["result"])
    result=read(result_path)
    require(manifest["actual_parent_warm_sha256"]==PARENT_WARM_SHA,"Condensed parent identity")
    files=[npz_file(directory,item,np,"condensed") for item in manifest["files"]]
    byfile={x["file"]:x for x in manifest["files"]}
    combinations,seen,reference_count=[],set(),0
    for route,value in walk(result):
        if not (isinstance(value,dict) and "array_identity" in value and "parts" in value):
            continue
        reference_count+=1
        descriptor=value["array_identity"]
        for item in value["parts"]:
            require(byfile.get(item["file"])==item,"Full array reference matches original manifest")
        signature=descriptor["sha256"]
        if signature in seen:
            continue
        seen.add(signature)
        combinations.append(combine_parts(directory,value["parts"],"actual",
            descriptor,np,"/".join(route)))
    require(seen,"Actual condensed array references must exist")
    return dict(manifest=receipt(path,context["root"]),result=receipt(result_path,context["root"]),
        file_count=len(files),array_count=sum(len(x["arrays"]) for x in files),
        reference_count=reference_count,unique_complete_arrays=len(seen),
        files=files,complete_array_byte_combinations=combinations,
        all_full_array_parts_kept_no_basis_truncation=True,
        no_model_action_performed=True)

def audit_root_raw(context,np):
    directory=context["directory"]/"condensed-root"
    status_path=original_json_path(directory,"status.json")
    status=read(status_path)
    records=[]
    for name,descriptor in status["output_arrays"].items():
        file=descriptor["file"]
        path=safe_path(directory,file)
        actual=sha(path)
        require(actual==descriptor["raw_sha256"],"Condensed raw root array "+name)
        require(path.stat().st_size==descriptor["bytes"],"Condensed raw size "+name)
        byte_count=np.dtype(descriptor["dtype"]).itemsize
        for length in descriptor["shape"]:
            byte_count*=length
        require(byte_count==descriptor["bytes"],"Condensed raw shape/dtype size "+name)
        records.append(dict(name=name,**receipt(path,context["root"]),
            shape=descriptor["shape"],dtype=descriptor["dtype"],raw_sha256=actual))
    require(len(records)==14,"All fourteen original root/recovery raw outputs")
    return dict(status=receipt(status_path,context["root"]),files=records,
        file_count=len(records),bytes=sum(x["bytes"] for x in records),
        full_factor_file_byte_audit=False,original_complete_chain_factor_RAM_only=True,
        original_reported_recovery=compact(status.get("last_recovery")),
        no_scientific_computation_performed=True)

def audit_observers(context,np):
    directory=context["directory"]
    reports=[]
    for path in sorted((directory/"collocation-observer").glob("evaluate-*.json")):
        obj=read(path)
        for key in ("original_returned_finite_unchanged",
                "original_returned_residual_bytes_unchanged",
                "original_returned_collocation_bytes_unchanged"):
            require(obj.get(key) is True,"Original observer did not change returned arrays: "+key)
        reports.append(dict(**receipt(path,context["root"]),evaluate_call=obj.get("evaluate_call"),
            original_require_rms=obj.get("original_require_rms"),
            original_returned_finite=obj.get("original_returned_finite"),
            full_physical_argmax=compact(obj.get("full_physical_argmax"))))
    # Every declared midpoint NPZ descriptor found in original model is
    # checked; repeated references are audited once by path and full SHA.
    mids={}
    for route,value in walk(context["model"]):
        if not isinstance(value,dict):
            continue
        name=value.get("file",value.get("path"))
        if isinstance(name,str) and name.endswith(".npz") and "midpoint-observer" in name:
            mids.setdefault(name,value)
    midpoint_records=[]
    for name,item in sorted(mids.items()):
        if "sha256" not in item:
            continue
        path=descriptor_file(directory,item)
        record=dict(**receipt(path,context["root"]),arrays={})
        with np.load(path,allow_pickle=False) as archive:
            declared=item.get("arrays")
            for key in archive.files:
                identity=array_identity(archive[key])
                if isinstance(declared,dict) and key in declared:
                    check_array(archive[key],declared[key],"Midpoint original "+key)
                record["arrays"][key]=identity
            record["NPY_payload_identity_scope"]=(
                "Compared with original declared array identities" if isinstance(declared,dict)
                else "Decoded original NPY identities recorded; file SHA/CRC is the binding")
        midpoint_records.append(record)
    present=sorted(str(p.relative_to(directory)) for p in (directory/"midpoint-observer").glob("*.npz"))
    matched=sorted(x["file"].split(WARM_DIR+"/",1)[-1] for x in midpoint_records)
    return dict(collocation=reports,
        original_collocation_run_summary=read(directory/"collocation-observer"/"run-summary.json"),
        midpoint_descriptors=midpoint_records,
        midpoint_payloads_present=present,midpoint_payloads_matched=matched,
        every_midpoint_file_has_original_descriptor=(present==matched),
        no_extra_evaluate_or_RHS_or_J_calls=True)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--download-out",type=Path,required=True)
    parser.add_argument("--out",type=Path,required=True)
    parser.add_argument("--repository-root",type=Path,required=True)
    args=parser.parse_args()
    if (os.environ.get("GITHUB_ACTIONS")!="true"
            or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY):
        raise SystemExit("This read-only receipt entry runs only in the public repository's Actions.")
    args.out.mkdir(parents=True,exist_ok=False)
    result=dict(schema=SCHEMA,completed=False,byte_audit_completed=False,
        original_artifact_pin=PIN,original_source_commit=SOURCE_COMMIT,
        source_file=Path(__file__).name,source_sha256=sha(__file__),
        mathematical_computation_performed=False,phase="complete-pinned-download")
    context=None
    try:
        root,transport=fetch_original(args)
        write(args.out/"large-arrays"/"complete-transport-receipt.json",transport)
        result["phase"]="original-report-readback"
        context=readout(root,args.out)
        result=context["summary"]
        result["phase"]="byte-audit"
        write(args.out/"actual62-readback.json",result)
        import numpy as np
        audit=dict(schema=SCHEMA,original_artifact_pin=PIN,
            original_source_commit=SOURCE_COMMIT,NumPy=np.__version__,
            no_scientific_module_imported=True,
            source_files=source_audit(context,args.repository_root))
        for name,function in (("domain",audit_domain),("condensed",audit_condensed),
                ("root_raw",audit_root_raw),("observers",audit_observers)):
            result["phase"]="byte-audit-"+name
            write(args.out/"actual62-readback.json",result)
            audit[name]=function(context,np)
            write(args.out/"large-arrays"/"complete-original-byte-audit.json",audit)
        source_verified=sum(x["verified"] for x in audit["source_files"])
        result.update(completed=True,byte_audit_completed=True,phase="complete",
            byte_audit_scope=dict(domain_NPZ_files=audit["domain"]["file_count"],
                domain_NPY_arrays=audit["domain"]["array_count"],
                original_B_model_sha256=audit["domain"]["model_sha256"],
                condensed_NPZ_files=audit["condensed"]["file_count"],
                condensed_complete_arrays=audit["condensed"]["unique_complete_arrays"],
                condensed_array_references=audit["condensed"]["reference_count"],
                root_raw_files=audit["root_raw"]["file_count"],
                root_raw_bytes=audit["root_raw"]["bytes"],
                source_file_SHA_verified=source_verified,
                source_claims_not_present_in_receipt_checkout=
                    len(audit["source_files"])-source_verified,
                every_midpoint_file_has_original_descriptor=
                    audit["observers"]["every_midpoint_file_has_original_descriptor"],
                full_factor_files_independently_audited=False,
                full_factor_arrays_not_exported_by_original_producer=True))
        result["complete_byte_audit_artifact"]=receipt(
            args.out/"large-arrays"/"complete-original-byte-audit.json",args.out)
        return_code=0
    except Exception as error:
        trace_path=args.out/"large-arrays"/"failure-traceback.txt"
        trace_path.parent.mkdir(parents=True,exist_ok=True)
        trace_path.write_text(traceback.format_exc(),encoding="utf-8")
        result.update(completed=False,failed_stage=result.get("phase"),
            error_type=type(error).__name__,
            local_exception_repr=repr(error)[:2000],
            full_local_exception_traceback=receipt(trace_path,args.out),
            error=(str(error) if isinstance(error,AuditError) else
                "Local readback error; original artifact and already-written readouts are retained"),
            original_successful_scientific_run_not_reclassified=True)
        return_code=2
    finally:
        result["completed_utc"]=datetime.datetime.now(datetime.timezone.utc).isoformat()
        # Preserve the complete derived report in the artifact even if a
        # future producer adds enough scalar metadata to exceed Git's
        # bounded-text reader limit.  Never throw away earlier readouts.
        write(args.out/"large-arrays"/"complete-readback-status.json",result)
        raw=json_bytes(result)
        if len(raw)<90000:
            write(args.out/"actual62-readback.json",result)
        else:
            thin={k:v for k,v in result.items() if k not in (
                "accepted_trial","nearest_previous_rejected_trial","original_FD_summary")}
            thin.update(target_scalar_report_size_exceeded=True,
                complete_readback_status_artifact="large-arrays/complete-readback-status.json",
                trial_report="actual62-original-trials.json",
                FD_report="actual62-original-FD.json")
            write(args.out/"actual62-readback.json",thin)
        print(json.dumps(dict(schema=SCHEMA,completed=result.get("completed"),
            phase=result.get("phase"),failed_stage=result.get("failed_stage"),
            byte_audit_completed=result.get("byte_audit_completed"),
            report="actual62-readback.json",
            mathematical_computation_performed=False),allow_nan=False),flush=True)
    return return_code

if __name__=="__main__":
    raise SystemExit(main())
