#!/usr/bin/env python3
"""R868 standard-library source transport, checkpoint recovery and verification.
No mathematical core or flint module is imported by this public wrapper.
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
import traceback

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO / "topics/serre-uniformity"
REQUEST = TOPIC / "notes/R868-P0-socle-RR-modules-public-request.json"
RESULT = "R868-original-P0-socle-and-degree254-RR-modules"
FINAL = "p41-original-P0-socle-and-RR-module-certificate.json"
PREFIX = "R868-"
MANIFEST = "full-outputs-manifest.json"
REFERENCE = "full-outputs-manifest-reference.json"
BUNDLE = "R868-retained-original-inputs.tar.gz"
INVENTORY = "R868-original-source-inventory.json"
INPUT_RECEIPT = "R868-retained-inputs-receipt.json"
META = ("public-actions-input.json", "run-receipt.json", "core-receipt.json")
BASE = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
SOURCE_LABELS = ("R805", "R806", "R849", "R856", "R860")
PROOF_KEYS = ("R868", "YP", "FM", "R856", "R860", "GP")
TRANSPORT_SHA = "eec99c9e849c051a8314f00ff594037e962d9bc23e2d2bfaa6334307a3bb5eae"
RANGE_SHA = "c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
EPS = [0] + [1]*144 + [2]*127
CERTIFICATES = {'R805': 'p41-original-affine-pencil-free-basis-certificate.json', 'R806': 'p41-original-primitive-multiplication-certificate.json', 'R849': 'p41-original-global-addition-polar-ideal-DAG-certificate.json', 'R856': 'p41-original-fixed-branch-ideal-bases-certificate.json', 'R860': 'p41-original-semilinear-resolvent-DAG-certificate.json'}
STRATEGY = {'scope': 'P0_single_pole_and_five_degree254_module_sources', 'normal_basis_rank': 272, 'point_fiber_rank_target': 271, 'point_inverse_power': 254, 'K_basis': '1,zeta; zeta^2+zeta+1=0', 'W_matrix_convention': 'row_output_column_input', 'point_source': 'original_R856_P0_in_both_charts', 'prime_schedule': 'successive_primes_p>=1000000753_with_p_mod_3=1', 'root_order': 'first_integer_a>=2_with_nontrivial_cube_root_then_its_square', 'minor_selection': 'first_embedding_RREF_columns_then_transpose_RREF_rows', 'one_common_minor_must_be_unit_at_both_K_embeddings': True, 'integer_column_scaling': 'original_denominator*point_z_denominator^3*point_w_denominator/gcd_content', 'free_coordinate_in_integral_system': 1, 'final_free_original_normal_coordinate': 1, 'Dixon': 'one_fixed_pair_of_271_inverses_and_two_integral_K_residuals', 'RR_rectangle': 'each_Q_coordinate_bound_floor_sqrt((M-1)/2);2*bound^2<M', 'RR_attempt_every_digits': 8, 'full_exact_original_normal_equations': 272, 'full_exact_K_coordinate_equations': 544, 'sigma_kernel_transport': 'h_sigma[i]=v0^(-epsilon[i])*h_tau[i]', 'socle_argument_allows_ramified_fiber': True, 'point_inverse_generators': '1,f_chart^254; complete by curve DVR valuations', 'source_eta_root': 'eta_degree_zero_fractional_ideal', 'two_weight_certificate': {'weight0': 128, 'weight1': 144}, 'old_W_point_values_or_ideals_recomputed': False, 'characteristic_zero_determinant_or_full_Krylov_inverse_computed': False, 'degree254_RR_basis_128_computed': False, 'original_connection_or_height_computed': False, 'only_transport_resume_budget_and_search_limits_excluded_from_identity': True}

def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open(path, "rt", encoding="utf-8") if path.suffix == ".gz"
          else path.open("r", encoding="utf-8")) as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")
    temporary.replace(path)


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def safe_name(name):
    assert isinstance(name, str) and Path(name).name == name and name not in (".", "..")
    assert "\\" not in name
    return name


def plain(value):
    result = {key: value[key] for key in ("file", "bytes", "sha256")}
    safe_name(result["file"])
    assert isinstance(result["bytes"], int) and result["bytes"] >= 0
    assert re.fullmatch(r"[0-9a-f]{64}", result["sha256"])
    return result


def file_spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def bound(folder, reference):
    reference = plain(reference)
    path = Path(folder) / reference["file"]
    assert file_spec(path) == reference, path.name
    return path


def identity(source):
    return {key: source[key] for key in BASE}


def source_identity(source):
    return {
        **identity(source), "certificate": plain(source["certificate"]),
        "configuration_sha256": source["configuration_sha256"],
        "selected_files_sha256": fingerprint(source["files"]),
        "selected_file_count": len(source["files"]),
    }


def topic_path(value):
    path = PurePosixPath(value)
    assert not path.is_absolute() and ".." not in path.parts
    result = (TOPIC / str(path)).resolve()
    assert result.is_relative_to(TOPIC.resolve())
    return result


def load_transport(item):
    path = S / safe_name(item["transport_helper"])
    assert path.name == "R837_original_branch_pencil_public.py"
    assert sha(path) == item["transport_helper_sha256"] == TRANSPORT_SHA
    assert item["io_helper"] == "R824_public_original_global_polar_generators.py"
    assert item["io_helper_sha256"] == RANGE_SHA
    module_spec = importlib.util.spec_from_file_location("R868_frozen_R837_transport", path)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    module.load_io(item)
    return module


def output_manifest(out):
    files = []
    for path in sorted(out.iterdir()):
        if not path.is_file() or path.name in (MANIFEST, REFERENCE) or path.name.endswith(".tmp"):
            continue
        files.append({**file_spec(path), "included_in_git": False})
    save(out / MANIFEST, {"result": RESULT, "files": files,
         "temporary_active_checkpoint_retention_days": 1, "reproducible_data_in_git_or_release": False})
    save(out / REFERENCE, {"result": RESULT, **file_spec(out / MANIFEST)})


def guard(item, request):
    assert os.environ.get("GITHUB_ACTIONS") == "true"
    assert os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public"
    assert request.resolve() == REQUEST.resolve()
    assert item["result"] == RESULT and item["p"] == 41
    assert item["producer_inputs_pending"] is False
    assert item["core"] == "R868_original_P0_socle_and_RR_modules.py"
    assert item["wrapper"] == "R868_public_original_P0_socle_and_RR_modules.py"
    assert sha(S/item["core"]) == item["core_sha256"]
    assert sha(__file__) == item["wrapper_sha256"]
    assert 0 < item["budget_minutes"] <= 300
    assert set(item["controls"]) == {"maximum_prime_trials", "maximum_Dixon_digits"}
    assert all(isinstance(value,int) and value >= 1 for value in item["controls"].values())
    assert set(item["proofs"]) == set(PROOF_KEYS)
    for entry in item["proofs"].values():
        assert sha(topic_path(entry["path"])) == entry["sha256"]
    assert sha(topic_path(item["method"])) == item["method_sha256"]
    assert sha(REPO/"README.md") == item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md") == item["readme_sha256"]["topic"]
    assert set(item["sources"]) == set(SOURCE_LABELS)
    for label, source in item["sources"].items():
        assert source["certificate"]["file"] == CERTIFICATES[label]
        assert source["expected_conclusion"] == "success"
        assert len(source["files"]) == source["selected_file_count"]
        assert fingerprint(source["files"]) == source["selected_files_sha256"]
    assert set(item["carrier_routes"]) == {"R860", "R850"}
    assert item["carrier_routes"]["R860"]["original_member_count"] == 61
    assert item["carrier_routes"]["R860"]["selected_groups"] == {"R805":"R805","R806":"R806"}
    assert item["carrier_routes"]["R850"]["original_member_count"] == 40
    assert item["carrier_routes"]["R850"]["selected_groups"] == {"GLOBAL":"R849"}
    return load_transport(item)


def expected_tag(item, sources):
    return {"result":RESULT,"source_sha256":item["core_sha256"],"p":41,
            "python_flint":"0.9.0","method_sha256":item["method_sha256"],
            "proofs_sha256":{k:item["proofs"][k]["sha256"] for k in PROOF_KEYS},
            "sources":{k:source_identity(sources[k]) for k in SOURCE_LABELS},
            "normal_basis_degrees":EPS,"strategy":STRATEGY}


def meta_review(source, directory):
    directory = Path(directory)
    manifest = read(bound(directory,{"file":MANIFEST,"bytes":source["manifest_bytes"],
                                     "sha256":source["manifest_sha256"]}))
    assert manifest["result"] == source["result"]
    entries = {v["file"]:plain(v) for v in manifest["files"]}
    assert len(entries) == len(manifest["files"]) == source["manifest_file_count"]
    initial,run,core = [read(bound(directory,entries[n])) for n in META]
    assert initial["result"] == run["result"] == core["result"] == source["result"]
    assert initial["source_commit"] == run["source_commit"] == source["source_commit"]
    assert str(run["workflow_run_id"]) == str(source["run_id"])
    assert initial["core_sha256"] == core["source_sha256"] == source["core_sha256"]
    assert run["complete"] is True and run["process_exit_code"] == 0
    assert run["error"] is None and core["complete"] is True
    assert run["core_receipt_sha256"] == entries["core-receipt.json"]["sha256"]
    certspec = plain(source["certificate"])
    assert entries[certspec["file"]] == certspec
    cert = read(bound(directory,certspec))
    assert cert["result"] == source["result"] and cert["complete"] is True
    assert core["certificate_sha256"] == certspec["sha256"]
    tag = cert["configuration"]
    assert tag["source_sha256"] == source["core_sha256"] and tag["result"] == source["result"]
    assert fingerprint(tag) == source["configuration_sha256"]
    return entries,cert,tag


def source_review(label, source, directory):
    directory = Path(directory)
    files = {name:plain(entry) for name,entry in source["files"].items()}
    assert all(name == entry["file"] for name,entry in files.items())
    for entry in files.values():
        bound(directory,entry)
    assert len(files) == source["selected_file_count"]
    assert fingerprint(files) == source["selected_files_sha256"]
    entries,cert,tag = meta_review(source,directory)
    for name,entry in files.items():
        if name != MANIFEST:
            assert entries[name] == entry
        if name.endswith(".json.gz"):
            value = read(directory/name)
            assert value["complete"] is True and value["configuration"] == tag,(label,name)
    if label == "R860":
        index = read(bound(directory,cert["coefficient_source_index"]))
        assert index["normal_basis_rank"] == 272 and index["normal_basis_degrees"] == EPS
        assert index["complete_original_coefficient_sources_retained"] is True
        assert len(index["source_exact_coordinate_groups"]) == 34
    elif label == "R856":
        assert cert["complete_two_chart_point_ideals_certified"] is True
        point = read(directory/"R856-original-P0-normal-values.json.gz")
        assert point["all_272_two_chart_value_transitions_verified"] is True
        assert point["original_P0_in_both_charts_verified"] is True
        for chart in ("tau","sigma"):
            value = read(directory/("R856-chart-"+chart+"-complete-P0-ideal-basis.json.gz"))
            assert value["complete_original_P0_evaluation_kernel_certified"] is True
            assert value["actual_colength_over_K"] == 1 and len(value["columns"]) == 272
    elif label == "R849":
        dag = read(directory/"R839-global-polar-exact-global-function-and-five-polar-expression-DAG.json.gz")
        assert dag["original_eta_Picard_input_DAGs_defined"] is True
        assert dag["actual_graph_node_count"] == len(dag["graph_nodes"]) == 523
        assert dag["expanded_global_function_coordinates_computed"] is False
        assert dag["normal_polynomial_ideal_lattices_materialized"] is False
    return {**identity(source),"certificate":plain(source["certificate"]),
            "configuration_sha256":source["configuration_sha256"],
            "selected_files_sha256":fingerprint(files),"selected_file_count":len(files),"files":files}


def cross_source_review(sources, retained):
    c860 = read(retained/"R860"/CERTIFICATES["R860"])
    for label in ("R805","R806"):
        assert identity(c860["configuration"]["sources"][label]) == identity(sources[label])
        assert c860["configuration"]["sources"][label]["certificate"] == sources[label]["certificate"]
    index = read(retained/"R860"/c860["coefficient_source_index"]["file"])
    assert identity(index["source_original_R806_producer"]) == identity(sources["R806"])
    for entry in index["source_exact_coordinate_groups"]:
        assert sources["R806"]["files"][entry["file"]] == plain(entry)
    p0 = read(retained/"R856"/"R856-original-P0-normal-values.json.gz")
    gp = read(retained/"R849"/"R839-global-polar-exact-global-function-and-five-polar-expression-DAG.json.gz")
    free = sources["R805"]["files"]["R805-graded-free-basis.json.gz"]
    assert p0["source_free_basis"] == gp["normal_basis_source"] == free
    assert identity(gp["configuration"]["source_identities"]["R806"]) == identity(sources["R806"])


def fetch_selected(archive, source, directory, names=None):
    directory.mkdir(parents=True,exist_ok=True)
    archive.extract_bound(MANIFEST,source["manifest_sha256"],directory/MANIFEST,source["manifest_bytes"])
    manifest = read(directory/MANIFEST)
    entries = {v["file"]:plain(v) for v in manifest["files"]}
    assert len(entries) == len(manifest["files"]) == source["manifest_file_count"]
    assert manifest["result"] == source["result"]
    assert set(archive.by_name) == set(entries)|{MANIFEST,REFERENCE}
    chosen = source["files"] if names is None else {name:entries[name] for name in names if name != MANIFEST}
    requests = []
    for name,entry in chosen.items():
        if name == MANIFEST:
            continue
        assert entries[name] == plain(entry)
        requests.append((name,entry["sha256"],directory/name,entry["bytes"]))
    archive.extract_many(requests)
    return entries


def extract_carrier(bundle, inventory, route, item, retained):
    members = {}
    for group,record in inventory["sources"].items():
        safe_name(group)
        for name,entry in record["files"].items():
            assert safe_name(name) == entry["file"]
            members[group+"/"+name] = plain(entry)
    assert len(members) == route["original_member_count"]
    for original,label in route["selected_groups"].items():
        src = item["sources"][label]
        record = inventory["sources"][original]
        assert identity(record) == identity(src)
        assert record["configuration_sha256"] == src["configuration_sha256"]
        if "certificate" in record:
            assert plain(record["certificate"]) == plain(src["certificate"])
        else:
            assert record["certificate_name"] == src["certificate"]["file"]
            assert plain(record["files"][record["certificate_name"]]) == plain(src["certificate"])
        for name,entry in src["files"].items():
            assert plain(record["files"][name]) == plain(entry)
        (retained/label).mkdir(parents=True,exist_ok=True)
    seen,kept = set(),[]
    with tarfile.open(bundle,"r:gz") as archive:
        for entry in archive:
            name = PurePosixPath(entry.name)
            assert entry.isfile() and not name.is_absolute() and ".." not in name.parts and len(name.parts) == 2
            assert entry.name in members and entry.name not in seen
            seen.add(entry.name)
            reference = members[entry.name]
            assert entry.size == reference["bytes"]
            group,basename = name.parts
            label = route["selected_groups"].get(group)
            chosen = label is not None and basename in item["sources"][label]["files"]
            target = retained/label/basename if chosen else None
            temporary = target.with_name(target.name+".transfer") if chosen else None
            output = temporary.open("wb") if chosen else None
            stream = archive.extractfile(entry)
            assert stream is not None
            digest,total = hashlib.sha256(),0
            try:
                for chunk in iter(lambda:stream.read(4*1024*1024),b""):
                    digest.update(chunk);total += len(chunk)
                    if output is not None:
                        output.write(chunk)
            finally:
                stream.close()
                if output is not None:
                    output.close()
            assert total == reference["bytes"] and digest.hexdigest() == reference["sha256"]
            if chosen:
                temporary.replace(target)
                kept.append({"original_group":group,"selected_group":label,"file":reference})
    assert seen == set(members)
    assert len(kept) == sum(len(item["sources"][label]["files"]) for label in route["selected_groups"].values())
    return len(seen),kept


def download_sources_once(item, retained, out, transport):
    reviewed,transfers = {},{}
    for label in ("R860","R856"):
        source = item["sources"][label]
        directory = retained/label
        archive = transport.IO.Archive(source,out.parent/("download-"+label),whole=False)
        try:
            entries = fetch_selected(archive,source,directory)
            reviewed[label] = source_review(label,source,directory)
            transfers[label] = archive.receipt()
            if label == "R860":
                route = item["carrier_routes"]["R860"]
                metadata = out.parent/"carrier-R860"
                metadata.mkdir(parents=True,exist_ok=True)
                for ref in (route["source_inventory"],route["input_receipt"],route["input_bundle"]):
                    ref = plain(ref);assert entries[ref["file"]] == ref
                    archive.extract_bound(ref["file"],ref["sha256"],metadata/ref["file"],ref["bytes"])
                inventory = read(bound(metadata,route["source_inventory"]))
                receipt = read(bound(metadata,route["input_receipt"]))
                assert inventory["complete"] is receipt["complete"] is True
                assert inventory["result"] == receipt["result"] == source["result"]
                assert receipt["minimal_bundle_member_count"] == route["original_member_count"]
                assert plain(receipt["source_inventory"]) == plain(route["source_inventory"])
                assert plain(receipt["source_bundle"]) == plain(route["input_bundle"])
                count,kept = extract_carrier(metadata/route["input_bundle"]["file"],inventory,route,item,retained)
                for selected in route["selected_groups"].values():
                    reviewed[selected] = source_review(selected,item["sources"][selected],retained/selected)
                preserved = []
                for ref in (route["source_inventory"],route["input_receipt"]):
                    name = ref["file"]
                    dest = out/(PREFIX+"transport-R860-"+name)
                    shutil.copyfile(metadata/name,dest)
                    preserved.append({"original_file":name,"retained_file":file_spec(dest)})
                transfers["R860_carrier"] = {"producer":identity(source),"input_bundle":plain(route["input_bundle"]),
                    "all_original_member_count_hashed":count,"selected_original_member_count":len(kept),
                    "transport_metadata_original_bytes":preserved,"range_transport":archive.receipt()}
                (metadata/route["input_bundle"]["file"]).unlink()
        finally:
            archive.close()
    route = item["carrier_routes"]["R850"]
    parent = route["producer"]
    metadata = out.parent/"carrier-R850"
    archive = transport.IO.Archive(parent,out.parent/"download-R850",whole=False)
    try:
        names = {*META,parent["certificate"]["file"],route["source_inventory"]["file"],
                 route["input_receipt"]["file"],route["input_bundle"]["file"]}
        entries = fetch_selected(archive,parent,metadata,names)
        meta_review(parent,metadata)
        for ref in (route["source_inventory"],route["input_receipt"],route["input_bundle"]):
            assert entries[ref["file"]] == plain(ref)
            bound(metadata,ref)
        inventory = read(metadata/route["source_inventory"]["file"])
        receipt = read(metadata/route["input_receipt"]["file"])
        assert inventory["complete"] is receipt["complete"] is True
        assert inventory["result"] == receipt["result"] == parent["result"]
        assert receipt["minimal_bundle_member_count"] == route["original_member_count"]
        assert plain(receipt["source_inventory"]) == plain(route["source_inventory"])
        assert plain(receipt["source_bundle"]) == plain(route["input_bundle"])
        assert identity(receipt["source_requests"]["GLOBAL"]) == identity(item["sources"]["R849"])
        count,kept = extract_carrier(metadata/route["input_bundle"]["file"],inventory,route,item,retained)
        reviewed["R849"] = source_review("R849",item["sources"]["R849"],retained/"R849")
        preserved = []
        for name in (MANIFEST,*META,parent["certificate"]["file"],route["source_inventory"]["file"],route["input_receipt"]["file"]):
            dest = out/(PREFIX+"transport-R850-"+name)
            shutil.copyfile(metadata/name,dest)
            preserved.append({"original_file":name,"retained_file":file_spec(dest)})
        transfers["R850_carrier"] = {"producer":identity(parent),"input_bundle":plain(route["input_bundle"]),
            "all_original_member_count_hashed":count,"selected_original_member_count":len(kept),
            "transport_metadata_original_bytes":preserved,"range_transport":archive.receipt(),
            "nested_395MB_original_GP_carrier_not_reopened_or_retained":True,
            "original_R849_mathematical_identity_unchanged":True}
        (metadata/route["input_bundle"]["file"]).unlink()
    finally:
        archive.close()
    assert set(reviewed) == set(SOURCE_LABELS)
    cross_source_review(reviewed,retained)
    return reviewed,transfers


def prepare_sources(item, out, transport, allow_download=True):
    retained = out.parent/"retained-original-R868"
    retained.mkdir(parents=True,exist_ok=True)
    wanted = {k:source_identity(item["sources"][k]) for k in SOURCE_LABELS}
    if all((out/name).exists() for name in (INPUT_RECEIPT,INVENTORY,BUNDLE)):
        receipt,inventory = read(out/INPUT_RECEIPT),read(out/INVENTORY)
        assert receipt["result"] == inventory["result"] == RESULT
        assert receipt["complete"] is inventory["complete"] is True
        assert receipt["source_mathematical_identities"] == wanted
        bound(out,receipt["source_inventory"]);bound(out,receipt["source_bundle"])
        for key in ("R860_carrier","R850_carrier"):
            for entry in receipt["range_transport"][key]["transport_metadata_original_bytes"]:
                bound(out,entry["retained_file"])
        count = transport.unpack_sources(out/BUNDLE,retained,inventory)
        reviewed = {k:source_review(k,item["sources"][k],retained/k) for k in SOURCE_LABELS}
        assert reviewed == inventory["sources"]
        assert count == receipt["minimal_bundle_member_count"] == sum(len(v["files"]) for v in reviewed.values())
        cross_source_review(reviewed,retained)
        return retained,receipt,reviewed
    assert allow_download,"The exact selected source carrier is required."
    reviewed,transfers = download_sources_once(item,retained,out,transport)
    inventory = {"result":RESULT,"complete":True,"sources":reviewed,"all_original_bytes_preserved":True}
    save(out/INVENTORY,inventory)
    transport.pack_sources(retained,inventory,out/BUNDLE)
    receipt = {"result":RESULT,"complete":True,"source_mathematical_identities":wanted,
               "source_inventory":file_spec(out/INVENTORY),"source_bundle":file_spec(out/BUNDLE),
               "minimal_bundle_member_count":sum(len(v["files"]) for v in reviewed.values()),
               "range_transport":transfers,"new_mathematics_executed_in_source_preparation":False}
    save(out/INPUT_RECEIPT,receipt)
    print("R868_INPUT_REVIEW="+json.dumps(receipt,sort_keys=True),flush=True)
    return retained,receipt,reviewed


def stable_job(item):
    value = {k:v for k,v in item.items() if k not in
             ("resume","budget_minutes","rules_last_read_commit","readme_sha256","sources","carrier_routes","controls")}
    value["sources"] = {k:source_identity(item["sources"][k]) for k in SOURCE_LABELS}
    return value


def restore(item, out, transport):
    resume = item.get("resume")
    if resume is None:
        return
    assert resume["result"] == RESULT and resume["core_sha256"] == item["core_sha256"]
    directory = out.parent/"resume-metadata"
    directory.mkdir(parents=True,exist_ok=True)
    archive = transport.IO.Archive(resume,out.parent/"download-R868-continuation",whole=False)
    try:
        archive.extract_bound(MANIFEST,resume["manifest_sha256"],directory/MANIFEST,resume["manifest_bytes"])
        manifest = read(directory/MANIFEST)
        assert manifest["result"] == RESULT
        entries = {row["file"]:plain(row) for row in manifest["files"]}
        assert len(entries) == len(manifest["files"]) == resume["manifest_file_count"]
        assert set(archive.by_name) == set(entries)|{MANIFEST,REFERENCE}
        for name in (*META,INPUT_RECEIPT,INVENTORY,BUNDLE):
            if name == "core-receipt.json" and name not in entries:
                continue
            ref = entries[name]
            target = out/name if name in (INPUT_RECEIPT,INVENTORY,BUNDLE) else directory/name
            archive.extract_bound(name,ref["sha256"],target,ref["bytes"])
        initial,run = read(directory/META[0]),read(directory/META[1])
        assert initial["result"] == run["result"] == RESULT
        assert initial["source_commit"] == run["source_commit"] == resume["source_commit"]
        assert str(run["workflow_run_id"]) == str(resume["run_id"])
        assert initial["core_sha256"] == item["core_sha256"]
        assert stable_job(initial["job"]) == stable_job(item)
        if META[2] in entries:
            core = read(directory/META[2])
            assert core["result"] == RESULT and core["source_sha256"] == item["core_sha256"]
            assert run["core_receipt_sha256"] == entries[META[2]]["sha256"]
        else:
            assert run["complete"] is False and run["core_receipt_sha256"] is None
        for name,ref in entries.items():
            if name.startswith(PREFIX+"transport-") and name.endswith(".json"):
                archive.extract_bound(name,ref["sha256"],out/name,ref["bytes"])
        unused,receipt,sources = prepare_sources(item,out,transport,allow_download=False)
        tag = expected_tag(item,sources)
        restored = []
        for name,ref in sorted(entries.items()):
            if not (name.startswith(PREFIX) and name.endswith(".json.gz")):
                continue
            archive.extract_bound(name,ref["sha256"],out/name,ref["bytes"])
            value = read(out/name)
            assert value["result"] == RESULT and value["configuration"] == tag
            assert value["complete"] is (name != PREFIX+"Dixon-current.json.gz")
            restored.append(ref)
        final_complete = False
        if FINAL in entries:
            ref = entries[FINAL]
            archive.extract_bound(FINAL,ref["sha256"],directory/FINAL,ref["bytes"])
            value = read(directory/FINAL)
            assert value["result"] == RESULT and value["configuration"] == tag
            final_complete = value["complete"]
            assert isinstance(final_complete,bool)
            if final_complete:
                shutil.copyfile(directory/FINAL,out/FINAL)
        save(out/(PREFIX+"resume-transport-receipt.json"),{
            "result":RESULT,"complete":True,"source":resume,"restored_mathematical_stages":restored,
            "source_inventory":receipt["source_inventory"],"previous_FINAL_complete":final_complete,
            "false_FINAL_not_restored_or_used_to_lock_later_current":True,
            "range_transport":archive.receipt(),"old_arithmetic_recomputed":False})
    finally:
        archive.close()


def compute(item, out, request, transport):
    out.mkdir(parents=True,exist_ok=True)
    code,error,outer_timeout = 1,None,False
    try:
        restore(item,out,transport)
        retained,receipt,sources = prepare_sources(item,out,transport)
        expanded = dict(item)
        expanded["sources"] = {k:dict(v,directory=str((retained/k).resolve())) for k,v in sources.items()}
        expanded["proofs"] = {k:dict(v,file=str(topic_path(v["path"]))) for k,v in item["proofs"].items()}
        expanded["method"] = str(topic_path(item["method"]))
        save(out/"public-actions-expanded-job.json",expanded)
        save(out/"public-actions-input.json",{
            "result":RESULT,"p":41,"source_repository":"Rogerhu12/math-research-public",
            "source_commit":os.environ["GITHUB_SHA"],"job":item,
            "core_sha256":item["core_sha256"],"driver_sha256":sha(__file__),
            "method_sha256":item["method_sha256"],"proofs_sha256":{k:v["sha256"] for k,v in item["proofs"].items()},
            "request_sha256":sha(request),"workflow_sha256":sha(REPO/item["workflow"]),
            "root_readme_sha256":sha(REPO/"README.md"),"topic_readme_sha256":sha(TOPIC/"README.md"),
            "transport_helper_sha256":item["transport_helper_sha256"],"io_helper_sha256":item["io_helper_sha256"],
            "source_inventory":receipt["source_inventory"],"actual_configuration":expected_tag(item,sources),
            "prepared_at_utc":dt.datetime.now(dt.timezone.utc).isoformat(),"new_arithmetic_in_wrapper":False})
        command = [sys.executable,str(S/item["core"]),"--config",str(out/"public-actions-expanded-job.json"),
                   "--out",str(out),"--budget-minutes",str(item["budget_minutes"])]
        with (out/"public-actions-run.log").open("ab") as log:
            process = subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
            try:
                code = process.wait(timeout=60*(item["budget_minutes"]+10))
            except subprocess.TimeoutExpired:
                outer_timeout = True
                os.killpg(process.pid,signal.SIGTERM)
                try:
                    process.wait(timeout=15)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid,signal.SIGKILL);process.wait()
                code,error = 124,"outer_timeout"
        if code == 0:
            assert read(out/FINAL)["complete"] is True
        print((out/"public-actions-run.log").read_text(errors="replace")[-16000:],flush=True)
    except Exception as exc:
        if code == 0:
            code = 1
        error = type(exc).__name__+": "+str(exc)
        traceback.print_exc()
    finally:
        save(out/"run-receipt.json",{
            "result":RESULT,"p":41,"complete":code == 0,"process_exit_code":code,
            "error":error,"outer_timeout":outer_timeout,"source_commit":os.environ["GITHUB_SHA"],
            "workflow_run_id":os.environ["GITHUB_RUN_ID"],"workflow_attempt":os.environ.get("GITHUB_RUN_ATTEMPT","1"),
            "execution_environment":"public-repository-github-actions",
            "core_receipt_sha256":sha(out/"core-receipt.json") if (out/"core-receipt.json").exists() else None,
            "finished_at_utc":dt.datetime.now(dt.timezone.utc).isoformat()})
        output_manifest(out)
    return code


def verify(item, out, request, transport):
    manifest = read(out/MANIFEST)
    assert manifest["result"] == RESULT
    entries = {v["file"]:plain(v) for v in manifest["files"]}
    assert len(entries) == len(manifest["files"])
    actual = {p.name for p in out.iterdir() if p.is_file() and p.name not in (MANIFEST,REFERENCE) and not p.name.endswith(".tmp")}
    assert actual == set(entries)
    for entry in entries.values():
        bound(out,entry)
    reference = read(out/REFERENCE)
    assert reference["result"] == RESULT and plain(reference) == file_spec(out/MANIFEST)
    initial,run = read(out/META[0]),read(out/META[1])
    assert initial["result"] == run["result"] == RESULT
    assert initial["source_commit"] == run["source_commit"] == os.environ["GITHUB_SHA"]
    assert initial["core_sha256"] == item["core_sha256"] and initial["driver_sha256"] == item["wrapper_sha256"]
    assert initial["request_sha256"] == sha(request)
    assert stable_job(initial["job"]) == stable_job(item)
    retained,receipt,sources = prepare_sources(item,out,transport,allow_download=False)
    tag = expected_tag(item,sources)
    assert initial["actual_configuration"] == tag
    complete_stages = {}
    for name,ref in entries.items():
        if not (name.startswith(PREFIX) and name.endswith(".json.gz")):
            continue
        value = read(out/name)
        assert value["result"] == RESULT and value["configuration"] == tag
        if name == PREFIX+"Dixon-current.json.gz":
            assert value["complete"] is False and value["digits"] >= 1
            assert len(value["solution_residues_K_coordinates"]) == len(value["exact_current_residual_K_coordinates"]) == 2
            assert all(len(row) == 271 for row in value["solution_residues_K_coordinates"]+value["exact_current_residual_K_coordinates"])
        else:
            assert value["complete"] is True
            if not name.startswith(PREFIX+"stage-manifest-"):
                complete_stages[name] = ref
    def stage(ref):
        ref = plain(ref)
        assert entries[ref["file"]] == ref
        value = read(bound(out,ref))
        assert value["complete"] is True and value["result"] == RESULT and value["configuration"] == tag
        return value
    core = read(out/"core-receipt.json") if "core-receipt.json" in entries else None
    if core is None:
        assert run["complete"] is False and run["core_receipt_sha256"] is None
    else:
        assert core["result"] == RESULT and core["source_sha256"] == item["core_sha256"]
        assert run["core_receipt_sha256"] == entries["core-receipt.json"]["sha256"]
    final = read(out/FINAL) if FINAL in entries else None
    if final is not None:
        assert final["result"] == RESULT and final["configuration"] == tag
        assert final["degree254_RR_basis_128_computed"] is False
        assert final["original_connection_or_height_computed"] is False
        assert final["old_W_point_values_or_ideals_recomputed"] is False
        inventory = stage(final["stage_manifest"])
        indexed = {v["file"]:plain(v) for v in inventory["files"]}
        assert len(indexed) == len(inventory["files"]) == inventory["file_count"]
        for ref in indexed.values():
            assert entries[ref["file"]] == ref
        if final["complete"]:
            assert indexed == complete_stages
            assert core is not None and core["complete"] is True and core["error"] is None
            assert core["certificate_sha256"] == entries[FINAL]["sha256"]
            for key in ("point_fiber_rank_271_certified","exact_normal_socle_vector_computed",
                        "both_point_inverse_power_ideals_certified","five_degree254_affine_module_DAGs_defined"):
                assert final[key] is core[key] is True
            audit = stage(final["source_audit"])
            assert audit["source_eta_root_name"] == "eta_degree_zero_fractional_ideal"
            matrix = stage(final["integral_matrix"])
            assert len(matrix["column_groups"]) == 34 and len(matrix["column_scales_Q"]) == 272
            for group,ref in enumerate(matrix["column_groups"]):
                value = stage(ref)
                assert value["column_start"] == 8*group and value["column_stop"] == 8*group+8
                assert len(value["columns"]) == len(value["column_scales_Q"]) == 8
                assert value["all_original_P0_left_equations_exactly_zero"] is True
                for col in value["columns"]:
                    assert len(col["K_integer_coordinates"]) == 272
            minor = stage(final["point_minor"])
            assert minor["accepted"] is True and minor["rank_target"] == 271
            assert minor["characteristic_zero_rank_271_certified"] is True
            assert minor["characteristic_zero_determinant_computed"] is False
            assert len(minor["row_indices"]) == len(minor["column_indices"]) == 271
            assert minor["row_indices"] == sorted(set(minor["row_indices"]))
            assert minor["column_indices"] == sorted(set(minor["column_indices"]))
            assert set(minor["column_indices"])|{minor["free_normal_coordinate"]} == set(range(272))
            assert len(minor["determinants_mod_prime"]) == 2 and all(0 < x < minor["prime"] for x in minor["determinants_mod_prime"])
            socle = stage(final["exact_socle"])
            assert socle["source_point_minor"] == final["point_minor"]
            assert socle["source_integral_matrix"] == final["integral_matrix"]
            inverse = stage(socle["source_fixed_inverse"])
            assert inverse["both_products_verified_for_both_embeddings"] is True
            rr = stage(socle["source_successful_reconstruction"])
            assert rr["all_coordinates_reconstructed_and_exact_system_verified"] is True
            assert socle["all_272_original_W_minus_w0_equations_exactly_verified"] is True
            assert socle["original_column_scaling_restored_exactly"] is True
            assert len(socle["h_tau_K_1_zeta"]) == 272
            assert socle["h_tau_K_1_zeta"][minor["free_normal_coordinate"]] == [["1","1"],["0","1"]]
            assert socle["full_residual_K_1_zeta"] == [[["0","1"],["0","1"]] for _ in range(272)]
            point = stage(final["point_inverse_power"])
            assert point["source_exact_socle"] == final["exact_socle"]
            assert point["sigma_transport_all_272_exactly_verified"] is True
            assert point["all_272_degree2_overlap_polynomial_identities_exactly_verified"] is True
            for chart in ("tau","sigma"):
                a = point["charts"][chart]
                assert a["point_inverse_power"] == 254 and a["exact_pole_order_of_f"] == 1
                assert a["full_H_plus_P0_basis_dimension"] == 147
                assert len(a["numerator_constant_normal_vector_K_1_zeta"]) == 272
                assert len(a["denominator_polynomial_K_1_zeta"]) == 2
                assert a["complete_inverse_ideal_certified_by_all_DVR_valuations"] is True
            modules = stage(final["five_affine_module_DAGs"])
            assert modules["source_point_inverse_power"] == final["point_inverse_power"]
            assert modules["five_degree254_affine_module_DAGs_defined"] is True
            assert modules["not_the_three_isogenous_real_descent_ideal"] is True
            assert modules["degree254_RR_basis_128_computed"] is modules["original_connection_or_height_computed"] is False
            gp = read(retained/"R849"/modules["source_original_global_eta_DAG"]["file"])
            nodes = {n["id"]:n for n in modules["graph_nodes"]}
            assert len(nodes) == modules["actual_new_graph_node_count"]
            for node in nodes.values():
                assert all(n in nodes for n in node["inputs"])
                if node["operation"] == "certified_original_external_fractional_ideal_DAG_root":
                    d = node["data"]
                    assert d["source_key"] == "eta_degree_zero_fractional_ideal"
                    assert d["source_node"] == gp["five_original_polar_and_eta_outputs"][str(d["original_j"])][d["source_key"]][d["chart"]]
            assert set(modules["five_outputs"]) == set(map(str,range(1,6)))
            for value in modules["five_outputs"].values():
                assert value["degree"] == 254
                assert all(root in nodes for root in value["charts"].values())
            if final["current_checkpoint"] is not None:
                assert entries[final["current_checkpoint"]["file"]] == plain(final["current_checkpoint"])
        else:
            assert run["complete"] is False
    if run["complete"]:
        assert run["process_exit_code"] == 0 and run["error"] is None
        assert final is not None and final["complete"] is True
    summary = {"result":RESULT,"complete":bool(final and final["complete"]),
               "all_output_bytes_and_source_identities_verified":True,
               "actual_selected_source_count":receipt["minimal_bundle_member_count"],
               "actual_complete_stage_count":len(complete_stages),
               "point_fiber_rank_271_certified":bool(final and final["point_fiber_rank_271_certified"]),
               "exact_normal_socle_vector_computed":bool(final and final["exact_normal_socle_vector_computed"]),
               "degree254_RR_basis_128_computed":False,"new_mathematics_executed_in_verifier":False}
    print("R868_VERIFY="+json.dumps(summary,sort_keys=True))
    return 0

def main():
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("compute", "verify"))
    parser.add_argument("--request", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    item = read(args.request)
    transport = guard(item, args.request)
    code = compute(item, args.output, args.request, transport) if args.mode == "compute" else \
        verify(item, args.output, args.request, transport)
    raise SystemExit(code)


if __name__ == "__main__":
    main()
