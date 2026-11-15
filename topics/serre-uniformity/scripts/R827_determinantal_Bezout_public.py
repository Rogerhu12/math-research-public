#!/usr/bin/env python3
"""Public source-preserving IO for R827 determinant/Bezout termination.

Standard-library-only.  Completed original columns are transported byte for
byte; mathematical computation occurs solely in the separate frozen core.
HTTP Range transfers do not claim to rehash the complete multi-GB source ZIP.
"""
import argparse
import datetime as dt
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import signal
import subprocess
import sys
import tarfile

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO/"topics/serre-uniformity"
REQUEST = TOPIC/"notes/R827-determinantal-Bezout-public-request.json"
RESULT = "R827-original-global-modular-derivative-termination"
FINAL = "p41-original-global-modular-derivative-termination-certificate.json"
MODE = "tau_determinantal_Bezout_and_sigma_infinity_rank"
PREFIX = "R827-det-"
REFERENCE = "full-outputs-manifest-reference.json"
MANIFEST = "full-outputs-manifest.json"
SOURCE_BUNDLE = "R827-determinantal-completed-source.tar.gz"
CONTINUED_BUNDLE = "R827-retained-producer-inputs.tar.gz"
SOURCE_INVENTORY = "R827-determinantal-source-inventory.json"
INPUT_RECEIPT = "determinantal-retained-inputs-receipt.json"
SOURCE_CORE = "d9cf773976f3beff7f44ff30f8b593665f481470cb52297239710e0ce6e062d2"
SOURCE_WRAPPER = "dbd8356e46ace9fcde94800a1e36f2f2f94c3f1d4a72afafea6fc21e20ae8b1d"
SOURCE_METHOD = "c55655f9df10a294dbd16071d0f08436e558e4d4edd4b899e526d308f3fb25e3"
ORIGINAL_PROOF = "17e9c828e01e652b1a73281bf2249ae2b39133faae3cf22384a5fd6d6a3d4a71"
RANGE_SHA = "c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
PRIME, N, Q = 1000000753, 272, 4
EPS = [0]+[1]*144+[2]*127
PARAMETERS = (0, 1, -1, 2)
BASE_KEYS = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
AUDIT = "R827-original-place-and-unit-source-audit.json.gz"
C_SOURCE = "R827-original-two-chart-C-reduction.json.gz"
OPERATORS = "R827-complete-short-operator-identities-and-sigma-transport.json.gz"
INFINITY = "R827-sigma-infinity-order-0004-certificate.json.gz"
B_EXPANSION = "R827-canonical-B-original-V5-expansion.json.gz"
H64 = re.compile(r"[0-9a-f]{64}")
IO = None
STRATEGY = {
    "source_column_order": "derivative_order=0..4, original_normal_basis_column=0..271",
    "projection_family": "V(a)=(I,aI,a^2 I,a^3 I,a^4 I)^transpose",
    "ordered_integer_parameters": list(PARAMETERS),
    "determinant_nodes": "all consecutive integers 0 through the proven degree bound",
    "degree_formula": "sum(projected original homogeneous column weights)-398-20",
    "block_projection_degree_bounds": [1340, 3516, 3516, 3516],
    "interpolation": "exact forward differences / factorials in the original prime field",
    "node_determinants": "python-flint nmod_mat.det; singular nodes retained as zero",
    "success": "complete exact polynomial Bezout sum equals one and original sigma infinity certificate",
    "right_inverse": "sum(a_i V_i adj(G V_i)); adjugate entries are not materialized",
    "old_column_or_Hermite_arithmetic_recomputed": False,
    "projection_prefix_and_budget_excluded_from_mathematical_identity": True,
}


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(4*1024*1024), b""):
            h.update(block)
    return h.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == ".gz" else open)(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(value, sort_keys=True, separators=(",", ":"))+"\n").encode()
    temporary = path.with_name(path.name+".tmp")
    temporary.write_bytes(raw); temporary.replace(path)


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def safe_name(name):
    assert isinstance(name, str) and Path(name).name == name
    assert name not in ("", ".", "..") and "\\" not in name


def plain(row):
    value = {key: row[key] for key in ("file", "bytes", "sha256")}
    safe_name(value["file"])
    assert type(value["bytes"]) is int and value["bytes"] >= 0
    assert H64.fullmatch(value["sha256"])
    return value


def file_spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def bound(directory, entry):
    entry = plain(entry); path = Path(directory)/entry["file"]
    assert path.is_file() and file_spec(path) == entry
    return path


def topic_path(relative):
    relative = PurePosixPath(relative)
    assert not relative.is_absolute() and ".." not in relative.parts
    path = (TOPIC/str(relative)).resolve()
    assert path.is_relative_to(TOPIC.resolve())
    return path


def identity(item):
    return {key: item[key] for key in BASE_KEYS}


def import_io(item):
    global IO
    path = S/item["io_helper"]
    assert path.name == "R824_public_original_global_polar_generators.py"
    assert sha(path) == item["io_helper_sha256"] == RANGE_SHA
    module = importlib.util.spec_from_file_location("R827_determinant_frozen_Range_IO", path)
    IO = importlib.util.module_from_spec(module); module.loader.exec_module(IO)


def guard(item, request_path):
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("R827 determinant execution belongs to this public repository's Actions.")
    assert item["result"] == RESULT and item["producer_inputs_pending"] is False
    assert item["certification_mode"] == MODE
    assert item["p"] == 41 and item["derivative_order"] == Q and item["auxiliary_prime"] == PRIME
    assert 1 <= item["controls"]["maximum_projections"] <= len(PARAMETERS)
    assert 0 < item["budget_minutes"] <= 300
    assert sha(__file__) == item["wrapper_sha256"]
    assert sha(S/item["core"]) == item["core_sha256"]
    assert sha(topic_path(item["proof"])) == item["determinantal_proof_sha256"]
    assert sha(topic_path(item["original_proof"])) == item["R827_proof_sha256"] == ORIGINAL_PROOF
    assert sha(REPO/"README.md") == item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md") == item["readme_sha256"]["topic"]
    assert request_path.resolve() == REQUEST.resolve()
    assert item["source"]["result"] == RESULT and item["source"]["core_sha256"] == SOURCE_CORE
    assert item["source"]["expected_conclusion"] == "failure"
    assert item["source"]["accepted_process_exit_codes"] == [124]
    assert item["continue_original_input_bundle_without_recomputing_members"] is True
    import_io(item)


def column_name(k, c):
    return "R827-tau-layer-"+str(k).zfill(3)+"-C-column-"+str(c).zfill(3)+".json.gz"


def layer_name(k):
    return "R827-target-B-tau-polynomial-index.json.gz" if k == 0 else \
        "R827-tau-layer-"+str(k).zfill(3)+"-precision-"+str(8+2*k).zfill(4)+"-index.json.gz"


def selected_names():
    names = {MANIFEST, REFERENCE, "run-receipt.json", "core-receipt.json", "public-actions-input.json",
             "retained-inputs-receipt.json", AUDIT, C_SOURCE, OPERATORS, INFINITY, B_EXPANSION}
    for k in range(Q+1):
        names.add(layer_name(k))
        for c in range(N):
            names.add(column_name(k,c))
    return sorted(names)


def load_manifest(source, directory):
    path = Path(directory)/MANIFEST
    assert sha(path) == source["manifest_sha256"] and path.stat().st_size == source["manifest_bytes"]
    manifest = read(path)
    assert manifest["result"] == source["result"]
    assert manifest["reproducible_data_in_git_or_release"] is False
    assert manifest["temporary_active_checkpoint_retention_days"] == 1
    entries = {entry["file"]: plain(entry) for entry in manifest["files"]}
    assert len(entries) == len(manifest["files"]) == source["manifest_file_count"]
    reference = read(Path(directory)/REFERENCE)
    assert reference["result"] == source["result"]
    assert reference["manifest_file"] == MANIFEST
    assert reference["manifest_sha256"] == source["manifest_sha256"]
    assert reference["manifest_bytes"] == source["manifest_bytes"]
    assert reference["file_count"] == len(entries)
    return entries


def source_review(item, directory, write_inventory=False):
    """Only bytes, schemas and old exact-stage assertions; no old arithmetic."""
    directory = Path(directory); source = item["source"]
    entries = load_manifest(source, directory)
    required = selected_names()
    selected = []
    for name in required:
        if name == MANIFEST:
            expected = {"file":name,"bytes":source["manifest_bytes"],"sha256":source["manifest_sha256"]}
        elif name == REFERENCE:
            expected = plain(source["manifest_reference"])
        else:
            expected = entries[name]
        bound(directory, expected); selected.append(expected)
    run, core, initial = [read(directory/name) for name in ("run-receipt.json", "core-receipt.json", "public-actions-input.json")]
    assert run["result"] == core["result"] == initial["result"] == RESULT
    assert str(run["workflow_run_id"]) == str(source["run_id"])
    assert run["source_commit"] == initial["source_commit"] == source["source_commit"]
    assert run["complete"] is False and core["complete"] is False
    assert run["process_exit_code"] in source["accepted_process_exit_codes"] and run["error"] is None
    assert isinstance(core["budget_stop"], str) and core["actual_D_eta_or_height_computed"] is False
    assert run["core_receipt_sha256"] == entries["core-receipt.json"]["sha256"]
    assert core["source_sha256"] == initial["core_sha256"] == initial["job"]["core_sha256"] == SOURCE_CORE
    assert initial["driver_sha256"] == initial["job"]["wrapper_sha256"] == SOURCE_WRAPPER
    assert initial["proof_sha256"] == initial["job"]["R827_proof_sha256"] == ORIGINAL_PROOF
    assert initial["method_sha256"] == initial["job"]["R827_method_sha256"] == SOURCE_METHOD
    assert initial["source_repository"] == "Rogerhu12/math-research-public"
    assert initial["root_readme_sha256"] == source["original_readme_sha256"]["root"]
    assert initial["topic_readme_sha256"] == source["original_readme_sha256"]["topic"]
    assert initial["job"]["requested_derivative_order"] == Q
    assert initial["job"]["auxiliary_prime"] == PRIME and initial["job"]["canonical_free_column"] == 1186
    assert entries[CONTINUED_BUNDLE] == plain(source["continued_input_bundle"])
    infinity = read(directory/INFINITY)
    old_tag = infinity["configuration"]
    assert fingerprint(old_tag) == item["source_configuration_sha256"]
    assert old_tag["result"] == RESULT and old_tag["source_sha256"] == SOURCE_CORE
    assert old_tag["R827_proof_sha256"] == ORIGINAL_PROOF and old_tag["R827_method_sha256"] == SOURCE_METHOD
    assert old_tag["python_flint"] == "0.9.0" and old_tag["auxiliary_prime"] == PRIME
    assert old_tag["normal_basis_rank"] == N and old_tag["normal_basis_degrees"] == EPS
    assert old_tag["certification_mode"] == "tau_polynomial_Hermite_and_sigma_infinity_rank"
    assert old_tag["original_branch"] == 0 and old_tag["canonical_free_column"] == 1186
    assert old_tag["original_field_coordinates"] == "B=lambda*b, s=1+2*zeta; exact original branch"
    assert infinity["complete"] is True and infinity["actual_rank_mod_prime"] == N
    assert infinity["actual_full_minor_determinant_mod_prime"] == 695832206
    assert infinity["whole_infinity_fiber_surjective"] is True
    assert infinity["chart"] == "sigma" and infinity["base_point"] == 0 and infinity["derivative_order"] == Q
    assert plain(infinity["source_C_reduction"]) == entries[C_SOURCE]
    for name in (AUDIT, C_SOURCE, OPERATORS, B_EXPANSION):
        stage = read(directory/name)
        assert stage["complete"] is True and stage["configuration"] == old_tag
    for k in range(Q+1):
        layer = read(directory/layer_name(k))
        assert layer["complete"] is True and layer["configuration"] == old_tag
        assert layer["prime"] == PRIME and layer["normal_basis_rank"] == N
        assert layer["normal_basis_degrees"] == EPS and layer["chart"] == "tau"
        if k == 0:
            assert layer["target"] == "B" and layer["regular_degree_bound"] == 5
            assert layer["all_weighted_support_zeros_verified"] is True
            assert layer["original_true_operator_reduction_certified"] is True
        else:
            assert layer["derivative_order"] == k and layer["precision_stop"] == 8+2*k
            assert layer["full_polynomial_coefficients_computed"] is True
            assert layer["all_required_coefficient_blocks_complete"] is True
        for c in range(N):
            data = read(directory/column_name(k,c))
            assert data["complete"] is True and data["configuration"] == old_tag
            assert data["prime"] == PRIME and data["chart"] == "tau" and data["derivative_order"] == k
            assert data["original_B_times_normal_basis_index"] == c
            assert data["original_generator_weight"] == 5+EPS[c]
            assert plain(data["source_original_layer"]) == entries[layer_name(k)]
            assert plain(data["source_complete_C"]) == entries[C_SOURCE]
            assert data["exact_monic_degree20_division_and_original_column_multiplyback_verified"] is True
            assert data["complete_C_basis_change_not_an_ideal_quotient"] is True
            rows = data["column_coefficients_in_original_C_basis"]
            assert len(rows) == N
            for r, values in enumerate(rows):
                bound_degree = 5+EPS[c]+2*k-(EPS[r] if r < N-1 else 1)
                assert isinstance(values, list) and len(values) <= bound_degree+1
                assert all(type(v) is int and 0 <= v < PRIME for v in values)
                assert not values or values[-1] != 0
    inventory = {"result": RESULT, "source": source,
                 "source_configuration_sha256": item["source_configuration_sha256"],
                 "selected_files": selected}
    if write_inventory:
        save(directory/SOURCE_INVENTORY, inventory)
    else:
        assert read(directory/SOURCE_INVENTORY) == inventory
    assert sha(directory/SOURCE_INVENTORY) == item["source_inventory_sha256"]
    return {"source": source, "source_configuration_sha256": item["source_configuration_sha256"],
            "source_inventory":file_spec(directory/SOURCE_INVENTORY),
            "original_source_column_count":1360,"all_selected_original_member_SHA_verified":True,
            "all_completed_columns_original_C_basis_and_layer_sources_verified":True,
            "original_sigma_infinity_rank":N,"original_sigma_infinity_minor":695832206,
            "original_source_ended_on_budget_and_not_global_failure":True,
            "old_Hermite_or_C_division_arithmetic_recomputed":False,
            "selected_file_count":len(selected)}


def pack_source(directory, target):
    directory, target = Path(directory), Path(target)
    inventory = read(directory/SOURCE_INVENTORY)
    rows = inventory["selected_files"]+[file_spec(directory/SOURCE_INVENTORY)]
    temporary = target.with_name(target.name+".tmp")
    with temporary.open("wb") as raw:
        with gzip.GzipFile(fileobj=raw,mode="wb",mtime=0,compresslevel=2) as compressed:
            with tarfile.open(fileobj=compressed,mode="w|") as archive:
                for row in rows:
                    path = bound(directory,row)
                    info = archive.gettarinfo(str(path),arcname=path.name)
                    info.uid=info.gid=0; info.uname=info.gname=""; info.mtime=0
                    with path.open("rb") as stream:archive.addfile(info,stream)
    temporary.replace(target)


def unpack_source(path, directory, expected_inventory, extract=True):
    """Hash every minimal carrier member; old large carrier is a separate opaque copy."""
    directory=Path(directory); directory.mkdir(parents=True,exist_ok=True)
    with tarfile.open(path,"r:gz") as archive:
        seen=set(); recorded={}
        for member in archive:
            assert member.isfile() and not member.issym() and not member.islnk()
            safe_name(member.name);assert member.name not in seen;seen.add(member.name)
            h=hashlib.sha256();count=0
            target=directory/member.name; temporary=target.with_name(target.name+".tmp")
            destination=temporary.open("wb") if extract else None
            try:
                with archive.extractfile(member) as stream:
                    for block in iter(lambda:stream.read(4*1024*1024),b""):
                        count+=len(block);h.update(block)
                        if destination is not None:destination.write(block)
            finally:
                if destination is not None:destination.close()
            assert count==member.size
            recorded[member.name]={"file":member.name,"bytes":count,"sha256":h.hexdigest()}
            if extract:temporary.replace(target)
    assert recorded[SOURCE_INVENTORY] == plain(expected_inventory)
    inventory=read(directory/SOURCE_INVENTORY)
    wanted={row["file"]:plain(row) for row in inventory["selected_files"]}
    wanted[SOURCE_INVENTORY]=plain(expected_inventory)
    assert recorded==wanted
    return len(recorded)


def prepare_inputs(item,out,allow_download=True):
    out=Path(out);retained=out.parent/"retained-original-R827"
    retained.mkdir(parents=True,exist_ok=True)
    receipt_path=out/INPUT_RECEIPT
    if receipt_path.exists() and (out/SOURCE_BUNDLE).exists() and (out/CONTINUED_BUNDLE).exists():
        receipt=read(receipt_path)
        assert receipt["result"]==RESULT and receipt["complete"] is True
        assert receipt["source"]==item["source"]
        bound(out,receipt["source_bundle"]);bound(out,receipt["continued_original_input_bundle"])
        count=unpack_source(out/SOURCE_BUNDLE,retained,receipt["source_inventory"],extract=True)
        review=source_review(item,retained)
        assert review==receipt["review"] and count==receipt["minimal_bundle_member_count"]
        assert receipt["original_input_bundle_used_by_new_arithmetic"] is False
        return retained,receipt
    assert allow_download,"A complete one-day source carrier is required for read-only verification."
    archive=IO.Archive(item["source"],out.parent/"download-original-R827",whole=False)
    try:
        source=item["source"]
        archive.extract_bound(MANIFEST,source["manifest_sha256"],retained/MANIFEST,source["manifest_bytes"])
        archive.extract_bound(REFERENCE,source["manifest_reference"]["sha256"],retained/REFERENCE,source["manifest_reference"]["bytes"])
        entries=load_manifest(source,retained)
        assert set(archive.by_name)==set(entries)|{MANIFEST,REFERENCE}
        for name,row in entries.items():
            assert len(archive.by_name[name])==1 and archive.by_name[name][0].file_size==row["bytes"]
        names=selected_names()
        archive.extract_many([(name,entries[name]["sha256"],retained/name,entries[name]["bytes"])
                              for name in names if name not in (MANIFEST,REFERENCE)])
        archive.extract_bound(CONTINUED_BUNDLE,source["continued_input_bundle"]["sha256"],
                              out/CONTINUED_BUNDLE,source["continued_input_bundle"]["bytes"])
        review=source_review(item,retained,write_inventory=True)
        pack_source(retained,out/SOURCE_BUNDLE)
        count=unpack_source(out/SOURCE_BUNDLE,retained,review["source_inventory"],extract=False)
        receipt={"result":RESULT,"complete":True,"source":source,"review":review,
                 "source_inventory":review["source_inventory"],"source_bundle":file_spec(out/SOURCE_BUNDLE),
                 "continued_original_input_bundle":file_spec(out/CONTINUED_BUNDLE),
                 "minimal_bundle_member_count":count,"range_transport":archive.receipt(),
                 "original_input_bundle_used_by_new_arithmetic":False,
                 "continued_original_input_bundle_original_bytes_SHA_verified":True,
                 "continued_original_input_bundle_members_recomputed":False,
                 "old_math_or_Hermite_transcripts_required_for_new_arithmetic":False}
        save(receipt_path,receipt)
        print("DETERMINANT_INPUT_REVIEW="+json.dumps(review,sort_keys=True),flush=True)
        return retained,receipt
    finally:archive.close()


def expected_tag(item,retained):
    inventory=read(Path(retained)/SOURCE_INVENTORY)
    entries={row["file"]:plain(row) for row in inventory["selected_files"]}
    return {"result":RESULT,"source_sha256":item["core_sha256"],"python_flint":"0.9.0",
            "p":41,"auxiliary_prime":PRIME,"derivative_order":Q,"certification_mode":MODE,
            "normal_basis_rank":N,"normal_basis_degrees":EPS,"source_column_count":1360,
            "determinantal_proof_sha256":item["determinantal_proof_sha256"],"R827_proof_sha256":ORIGINAL_PROOF,
            "source_identity":identity(item["source"]),"source_configuration_sha256":item["source_configuration_sha256"],
            "source_inventory_sha256":item["source_inventory_sha256"],
            "source_sigma_infinity_certificate":entries[INFINITY],"strategy":STRATEGY}


def stable_job(item):
    return {key:value for key,value in item.items()
            if key not in ("resume","budget_minutes","controls","readme_sha256","rules_last_read_commit")}


def restore(item,out):
    resume=item.get("resume")
    if resume is None:return
    assert resume["result"]==RESULT and resume["core_sha256"]==item["core_sha256"]
    original=out.parent/"resume-metadata";original.mkdir(parents=True,exist_ok=True)
    archive=IO.Archive(resume,out.parent/"download-determinantal-continuation",whole=False)
    try:
        archive.extract_bound(MANIFEST,resume["manifest_sha256"],original/MANIFEST,resume["manifest_bytes"])
        manifest=read(original/MANIFEST);assert manifest["result"]==RESULT
        entries={row["file"]:plain(row) for row in manifest["files"]}
        assert len(entries)==len(manifest["files"])==resume["manifest_file_count"]
        for name in ("run-receipt.json","public-actions-input.json",INPUT_RECEIPT,SOURCE_BUNDLE,CONTINUED_BUNDLE):
            row=entries[name]; target=out/name if name in (INPUT_RECEIPT,SOURCE_BUNDLE,CONTINUED_BUNDLE) else original/name
            archive.extract_bound(name,row["sha256"],target,row["bytes"])
        run=read(original/"run-receipt.json");initial=read(original/"public-actions-input.json")
        assert run["result"]==initial["result"]==RESULT
        assert str(run["workflow_run_id"])==str(resume["run_id"])
        assert run["source_commit"]==initial["source_commit"]==resume["source_commit"]
        assert initial["core_sha256"]==item["core_sha256"]
        assert stable_job(initial["job"])==stable_job(item)
        if "core-receipt.json" in entries:
            row=entries["core-receipt.json"];archive.extract_bound(row["file"],row["sha256"],original/row["file"],row["bytes"])
            core=read(original/row["file"])
            assert core["result"]==RESULT and core["source_sha256"]==item["core_sha256"]
            assert run["core_receipt_sha256"]==row["sha256"]
        else:
            assert run["complete"] is False and run["core_receipt_sha256"] is None
        retained,_=prepare_inputs(item,out,allow_download=False)
        tag=expected_tag(item,retained)
        selected=sorted(name for name in entries if name.startswith(PREFIX) and name.endswith(".json.gz"))
        archive.extract_many([(name,entries[name]["sha256"],out/name,entries[name]["bytes"]) for name in selected])
        for name in selected:
            stage=read(out/name)
            assert stage["configuration"]==tag and stage["result"]==RESULT and stage["complete"] is True
        restored_final=False
        if FINAL in entries:
            row=entries[FINAL];archive.extract_bound(FINAL,row["sha256"],original/FINAL,row["bytes"])
            final=read(original/FINAL)
            assert final["result"]==RESULT and final["configuration"]==tag
            if final["complete"] and final["original_characteristic_zero_Iq_equals_C"]:
                assert run["complete"] is True and run["process_exit_code"]==0
                assert core["complete"] is True and core["certificate_sha256"]==row["sha256"]
                bound(out,final["stage_manifest"])
                shutil.copyfile(original/FINAL,out/FINAL);restored_final=True
        save(out/"resume-inheritance-receipt.json",{
            "result":RESULT,"complete":True,"source_resume":resume,
            "original_manifest":file_spec(original/MANIFEST),"range_transport":archive.receipt(),
            "all_restored_complete_stages":[entries[name] for name in selected],
            "restored_successful_final":restored_final,"old_failed_prefix_final_not_used_as_new_snapshot":not restored_final,
            "all_original_nodes_and_projection_coefficients_reused_without_arithmetic":True})
    finally:archive.close()


def output_manifest(out):
    entries=[]
    for path in sorted(out.iterdir()):
        if path.is_file() and path.name not in (MANIFEST,REFERENCE) and not path.name.endswith((".tmp",".download")):
            entries.append(dict(file_spec(path),included_in_git=False))
    save(out/MANIFEST,{"result":RESULT,"files":entries,"temporary_active_checkpoint_retention_days":1,
                       "reproducible_data_in_git_or_release":False})
    save(out/REFERENCE,{"result":RESULT,"manifest_file":MANIFEST,"manifest_sha256":sha(out/MANIFEST),
                        "manifest_bytes":(out/MANIFEST).stat().st_size,"file_count":len(entries)})


def compute(item,out,request_path):
    out.mkdir(parents=True,exist_ok=True)
    process=None;exitcode=1;error=None;outer_timeout=False
    try:
        restore(item,out)
        retained,receipt=prepare_inputs(item,out)
        save(out/"public-actions-expanded-job.json",item)
        initial={"result":RESULT,"source_repository":"Rogerhu12/math-research-public",
                 "source_commit":os.environ["GITHUB_SHA"],"p":41,"job":item,
                 "request_sha256":sha(request_path),"driver_sha256":sha(__file__),"core_sha256":item["core_sha256"],
                 "proof_sha256":item["determinantal_proof_sha256"],"original_proof_sha256":ORIGINAL_PROOF,
                 "io_helper_sha256":RANGE_SHA,"workflow_sha256":sha(REPO/item["workflow"]),
                 "root_readme_sha256":sha(REPO/"README.md"),"topic_readme_sha256":sha(TOPIC/"README.md"),
                 "source_inventory":receipt["source_inventory"],"prepared_at_utc":dt.datetime.now(dt.timezone.utc).isoformat(),
                 "all_new_math_runs_only_in_separate_public_Actions_core":True}
        save(out/"public-actions-input.json",initial)
        command=[sys.executable,str(S/item["core"]),"--config",str(out/"public-actions-expanded-job.json"),
                 "--proof",str(topic_path(item["proof"])),"--original-proof",str(topic_path(item["original_proof"])),
                 "--retained",str(retained),"--output",str(out),"--budget-minutes",str(item["budget_minutes"])]
        with (out/"public-actions-run.log").open("w",encoding="utf-8") as log:
            process=subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
            try:exitcode=process.wait(timeout=item["budget_minutes"]*60+900)
            except subprocess.TimeoutExpired:
                outer_timeout=True;os.killpg(process.pid,signal.SIGTERM)
                try:process.wait(timeout=20)
                except subprocess.TimeoutExpired:os.killpg(process.pid,signal.SIGKILL);process.wait()
                exitcode=124
    except BaseException as caught:
        error=type(caught).__name__+": "+str(caught)
        if process is not None and process.poll() is None:
            os.killpg(process.pid,signal.SIGTERM)
            try:process.wait(timeout=20)
            except subprocess.TimeoutExpired:os.killpg(process.pid,signal.SIGKILL);process.wait()
        exitcode=1
    finally:
        core_path=out/"core-receipt.json"
        core=read(core_path) if core_path.exists() else None
        complete=(exitcode==0 and core is not None and core.get("complete") is True and (out/FINAL).is_file())
        receipt={"result":RESULT,"p":41,"complete":complete,"process_exit_code":exitcode,"error":error,
                 "core_receipt_sha256":sha(core_path) if core_path.exists() else None,
                 "source_commit":os.environ.get("GITHUB_SHA"),"workflow_run_id":os.environ.get("GITHUB_RUN_ID"),
                 "workflow_attempt":os.environ.get("GITHUB_RUN_ATTEMPT"),
                 "execution_environment":"public-repository-github-actions","outer_timeout":outer_timeout,
                 "finished_at_utc":dt.datetime.now(dt.timezone.utc).isoformat()}
        save(out/"run-receipt.json",receipt);output_manifest(out)
        print("DETERMINANT_RUN_RECEIPT="+json.dumps(receipt,sort_keys=True),flush=True)
    return exitcode


def verify(item,out):
    """Complete source/output byte and certificate-schema verification; no arithmetic import."""
    manifest=read(out/MANIFEST);reference=read(out/REFERENCE)
    assert manifest["result"]==reference["result"]==RESULT
    assert reference["manifest_file"]==MANIFEST and reference["manifest_sha256"]==sha(out/MANIFEST)
    assert reference["manifest_bytes"]==(out/MANIFEST).stat().st_size
    files={row["file"]:plain(row) for row in manifest["files"]}
    assert len(files)==len(manifest["files"])==reference["file_count"]
    actual={path.name for path in out.iterdir() if path.is_file() and path.name not in (MANIFEST,REFERENCE)
            and not path.name.endswith((".tmp",".download"))}
    assert actual==set(files)
    for row in files.values():bound(out,row)
    retained,receipt=prepare_inputs(item,out,allow_download=False)
    tag=expected_tag(item,retained)
    initial=read(out/"public-actions-input.json")
    assert initial["result"]==RESULT and initial["job"]==item
    assert initial["driver_sha256"]==item["wrapper_sha256"] and initial["core_sha256"]==item["core_sha256"]
    assert initial["source_inventory"]==receipt["source_inventory"]
    assert initial["root_readme_sha256"]==item["readme_sha256"]["root"]
    assert initial["topic_readme_sha256"]==item["readme_sha256"]["topic"]
    stages={}
    for name,row in files.items():
        if name.startswith(PREFIX) and name.endswith(".json.gz"):
            data=read(out/name)
            assert data["result"]==RESULT and data["configuration"]==tag and data["complete"] is True
            stages[name]=row
    def stage(entry):
        entry=plain(entry)
        assert stages[entry["file"]]==entry
        return read(bound(out,entry))
    run=read(out/"run-receipt.json")
    assert run["result"]==RESULT and run["source_commit"]==initial["source_commit"]
    core=None
    if "core-receipt.json" in files:
        core=read(out/"core-receipt.json")
        assert run["core_receipt_sha256"]==files["core-receipt.json"]["sha256"]
        assert core["result"]==RESULT and core["source_sha256"]==item["core_sha256"]
        assert core["certification_mode"]==MODE
    else:
        assert run["core_receipt_sha256"] is None and run["complete"] is False
    if not run["complete"]:
        assert run["process_exit_code"]!=0
        if core is not None and core["complete"] is True:
            assert FINAL in files
            completed=read(out/FINAL)
            assert completed["complete"] is True and completed["configuration"]==tag
            assert core["certificate_sha256"]==files[FINAL]["sha256"]
        print("DETERMINANT_PARTIAL_IO_REVIEW="+json.dumps({"result":RESULT,"complete_stages":len(stages),
              "manifest_files":len(files),"core_receipt_present":core is not None,
              "all_current_output_and_selected_source_bytes_verified":True,
              "mathematical_completion_claimed":False},sort_keys=True),flush=True)
        return 1
    assert run["process_exit_code"]==0 and run["error"] is None and core is not None and core["complete"] is True
    final=read(out/FINAL)
    assert final["result"]==RESULT and final["complete"] is True and final["configuration"]==tag
    assert core["certificate_sha256"]==files[FINAL]["sha256"]
    assert final["p"]==41 and final["certification_mode"]==MODE
    assert final["completed_scope"]=="determinantal_sufficient_original_order4_termination_test"
    assert final["requested_projection_prefix_length"]==item["controls"]["maximum_projections"]
    count=final["actual_completed_projection_count"]
    assert 1<=count<=item["controls"]["maximum_projections"]
    assert core["actual_completed_projection_count"]==count
    assert final["requested_derivative_order"]==final["actual_derivative_order"]==core["actual_derivative_order"]==Q
    inventory=stage(final["stage_manifest"])
    assert inventory["all_listed_stages_complete"] is True
    inventory_rows={row["file"]:plain(row) for row in inventory["files"]}
    complete_names={name for name in stages if not name.startswith(PREFIX+"stage-manifest-") and not name.endswith("-current.json.gz")}
    assert set(inventory_rows)==complete_names
    assert all(inventory_rows[name]==stages[name] for name in complete_names)
    source=stage(final["source_completed_column_interface"])
    assert source["prime"]==PRIME and source["derivative_order"]==Q and source["original_column_count"]==1360
    assert source["same_original_field_branch_free_column_and_C_preserved"] is True
    assert source["source_incomplete_Hermite_not_claimed_as_complete"] is True
    assert source["old_columns_divisions_operators_Hermite_or_infinity_arithmetic_recomputed"] is False
    original_inventory=read(retained/SOURCE_INVENTORY)
    original_files={row["file"]:plain(row) for row in original_inventory["selected_files"]}
    assert source["source_column_inventory_sha256"]==fingerprint([original_files[column_name(k,c)] for k in range(5) for c in range(N)])
    assert source["source_original_tau_layer_indexes"]==[original_files[layer_name(k)] for k in range(5)]
    assert final["sigma_infinity_source_group"]=="original_R827"
    assert plain(final["sigma_infinity_certificate"])==original_files[INFINITY]
    assert source["source_original_sigma_infinity_certificate"]==original_files[INFINITY]
    determinants=final["source_determinant_polynomials"]
    assert len(determinants)==count
    node_counts=[];degrees=[]
    for number,entry in enumerate(determinants):
        determinant=stage(entry)
        assert determinant["prime"]==PRIME and determinant["projection_number"]==number
        assert determinant["integer_parameter"]==PARAMETERS[number]
        degree_bound=STRATEGY["block_projection_degree_bounds"][number]
        assert determinant["proven_determinant_degree_bound"]==degree_bound
        values=determinant["determinant_coefficients_mod_prime"]
        assert isinstance(values,list) and len(values)<=degree_bound+1
        assert all(type(v) is int and 0<=v<PRIME for v in values)
        assert not values or values[-1]!=0
        assert determinant["actual_determinant_degree"]==len(values)-1
        assert determinant["zero_polynomial_retained_as_valid_determinant"]==(not bool(values))
        for key in ("all_degree_bound_plus_one_nodes_exactly_verified","exact_interpolant_is_the_entire_determinant_by_proven_degree_bound","no_adjugate_coefficients_computed"):
            assert determinant[key] is True
        matrix=stage(determinant["source_projection_matrix"])
        assert matrix["prime"]==PRIME and matrix["projection_number"]==number and matrix["integer_parameter"]==PARAMETERS[number]
        assert matrix["proven_determinant_degree_bound"]==degree_bound
        maximum_layer=0 if number==0 else Q
        assert matrix["source_homogeneous_column_weights"]==[5+e+2*maximum_layer for e in EPS]
        assert matrix["original_normal_weight_sum"]==398 and matrix["source_C_determinant_degree"]==20
        assert matrix["source_completed_columns"]==final["source_completed_column_interface"]
        assert matrix["polynomial_coefficient_count"]==len(matrix["coefficient_blocks"])==8+2*maximum_layer
        for power,block_entry in enumerate(matrix["coefficient_blocks"]):
            block=stage(block_entry)
            assert block["prime"]==PRIME and block["projection_number"]==number
            assert block["integer_parameter"]==PARAMETERS[number] and block["coefficient_exponent"]==power
            assert block["matrix_rows"]==block["matrix_columns"]==N
            assert block["source_completed_columns"]==final["source_completed_column_interface"]
            assert block["source_original_column_inventory_sha256"]==source["source_column_inventory_sha256"]
            assert block["only_new_constant_projection_linear_combination_performed"] is True
            assert block["old_source_columns_recomputed"] is False
            rows=block["coefficient_matrix_mod_prime"]
            assert len(rows)==N and all(len(row)==N for row in rows)
            assert all(type(v) is int and 0<=v<PRIME for row in rows for v in row)
        nodes=stage(determinant["source_complete_nodes"])
        assert nodes["source_projection_matrix"]==determinant["source_projection_matrix"]
        assert nodes["projection_number"]==number and nodes["integer_parameter"]==PARAMETERS[number]
        assert nodes["proven_determinant_degree_bound"]==degree_bound
        assert nodes["node_count"]==len(nodes["node_records"])==degree_bound+1
        assert nodes["points_are_exactly_consecutive_zero_through_bound"] is True
        assert nodes["all_required_node_determinants_complete"] is True
        for point,node_entry in enumerate(nodes["node_records"]):
            node=stage(node_entry)
            assert node["prime"]==PRIME and node["projection_number"]==number and node["integer_parameter"]==PARAMETERS[number]
            assert node["point"]==point and node["source_projection_matrix"]==determinant["source_projection_matrix"]
            assert node["matrix_rows"]==node["matrix_columns"]==N and node["proven_determinant_degree_bound"]==degree_bound
            assert type(node["determinant_mod_prime"]) is int and 0<=node["determinant_mod_prime"]<PRIME
            assert node["singular_node_is_valid_zero_not_discarded"] is True
            assert node["actual_exact_finite_field_determinant_computed"] is True
        node_counts.append(degree_bound+1);degrees.append(determinant["actual_determinant_degree"])
        prefix_name=PREFIX+"prefix-"+str(number+1).zfill(3)+"-exact-Bezout.json.gz"
        prefix=stage(stages[prefix_name])
        assert prefix["prime"]==PRIME and prefix["completed_projection_count"]==number+1
        assert prefix["source_determinant_polynomials"]==determinants[:number+1]
        assert prefix["complete_polynomial_Bezout_multiplyback_verified"] is True
        assert len(prefix["Bezout_coefficients_mod_prime"])==number+1
        gcd=prefix["monic_gcd_coefficients_mod_prime"]
        assert prefix["actual_monic_gcd_degree"]==len(gcd)-1
        assert not gcd or gcd[-1]==1
        for polynomial in [gcd]+prefix["Bezout_coefficients_mod_prime"]:
            assert isinstance(polynomial,list) and all(type(v) is int and 0<=v<PRIME for v in polynomial)
            assert not polynomial or polynomial[-1]!=0
        assert prefix["sum_ai_actual_determinants_equals_one"]==(gcd==[1])
        if number+1<count:assert prefix["sum_ai_actual_determinants_equals_one"] is False
    final_bezout=stage(final["tau_determinantal_Bezout_certificate"])
    assert final["tau_determinantal_Bezout_certificate"]==stages[PREFIX+"prefix-"+str(count).zfill(3)+"-exact-Bezout.json.gz"]
    success=final_bezout["sum_ai_actual_determinants_equals_one"]
    assert type(success) is bool
    assert final["whole_sigma_infinity_fiber_surjective"] is True
    for key in ("whole_tau_affine_polynomial_module_surjective","original_characteristic_zero_Iq_equals_C","factored_adjugate_right_inverse_certified"):
        assert final[key] is success
    assert final["safe_D_multiplicity_bound"]==(1 if success else None)
    assert core["original_characteristic_zero_Iq_equals_C"] is success
    assert core["safe_D_multiplicity_bound"]==final["safe_D_multiplicity_bound"]
    assert final["failed_projection_prefix_does_not_disprove_original_termination"] is (not success)
    if not success:assert count==item["controls"]["maximum_projections"]
    for data in (final,final_bezout):
        assert data["adjugate_coefficients_materialized"] is False
        assert data["expanded_right_inverse_coefficients_materialized"] is False
    assert final["actual_D_eta_or_height_computed"] is False
    assert final["old_columns_derivatives_C_divisions_Hermite_or_infinity_arithmetic_recomputed"] is False
    assert final["no_probability_or_finite_point_rank_used_as_global_certificate"] is True
    print("DETERMINANT_COMPLETE_IO_REVIEW="+json.dumps({
        "result":RESULT,"certification_mode":MODE,"actual_completed_projection_count":count,
        "integer_projection_parameters":list(PARAMETERS[:count]),"complete_node_counts":node_counts,
        "actual_determinant_degrees":degrees,"actual_gcd_degree":final_bezout["actual_monic_gcd_degree"],
        "original_I4_equals_C":success,"safe_D_multiplicity_bound":final["safe_D_multiplicity_bound"],
        "factored_right_inverse_certified":success,"expanded_adjugate_or_right_inverse_materialized":False,
        "manifest_files":len(files),"complete_stages":len(stages),
        "source_bundle":files[SOURCE_BUNDLE],"continued_original_input_bundle":files[CONTINUED_BUNDLE],
        "certificate":files[FINAL],"stage_manifest":final["stage_manifest"],
        "all_output_and_selected_source_bytes_verified":True,"seconds":final["seconds"]},sort_keys=True),flush=True)
    return 0


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--verify",action="store_true")
    args=parser.parse_args()
    item=read(REQUEST)
    guard(item,REQUEST)
    return verify(item,args.output) if args.verify else compute(item,args.output,REQUEST)


if __name__=="__main__":
    raise SystemExit(main())
