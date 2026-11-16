#!/usr/bin/env python3
"""R872 standard-library source transport, checkpoint recovery and verification.
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
REQUEST = TOPIC / "notes/R872-point-jets-fixed-Picard-public-request.json"
RESULT = "R872-original-P0-jets-and-fixed-Picard-RR-spaces"
FINAL = "p41-original-P0-jets-and-fixed-Picard-RR-spaces-certificate.json"
PREFIX = "R872-"
MANIFEST = "full-outputs-manifest.json"
REFERENCE = "full-outputs-manifest-reference.json"
BUNDLE = "R872-retained-original-inputs.tar.gz"
INVENTORY = "R872-original-source-inventory.json"
INPUT_RECEIPT = "R872-retained-inputs-receipt.json"
META = ("public-actions-input.json", "run-receipt.json", "core-receipt.json")
BASE = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
SOURCE_LABELS = ("R805", "R806", "R856", "R860", "R868", "R827")
PROOF_KEYS = ("R872", "R868", "R805", "R809")
TRANSPORT_SHA = "eec99c9e849c051a8314f00ff594037e962d9bc23e2d2bfaa6334307a3bb5eae"
RANGE_SHA = "c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
EPS = [0] + [1]*144 + [2]*127
CERTIFICATES = {
    "R805":"p41-original-affine-pencil-free-basis-certificate.json",
    "R806":"p41-original-primitive-multiplication-certificate.json",
    "R856":"p41-original-fixed-branch-ideal-bases-certificate.json",
    "R860":"p41-original-semilinear-resolvent-DAG-certificate.json",
    "R868":"p41-original-P0-socle-and-RR-module-certificate.json",
    "R827":None,
}
PRIME, RANK, JET_LAST = 1000000753, 272, 272
R872_PROOF_SHA = "bd6ee11af3fbbce8db2767bc327265176992bb3be15395018df6612ab4e2dae2"
STRATEGY = {
    "scope": "original_P0_jets_and_fixed_chi_complete_RR_spaces",
    "field": "K=Q(zeta), zeta^2+zeta+1=0",
    "prime": PRIME,
    "normal_basis_degrees": EPS,
    "normal_basis_integer_scale_applied_again": False,
    "point_source": "R856 actual original P0",
    "socle_source": "R868 actual h with selected free coordinate",
    "reuse_complete_original_W_modular_reduction": True,
    "reuse_original_point_minor_and_both_inverse_products": True,
    "local_parameter": "first z-z0 if alpha is a unit; otherwise w-w0 if beta is a unit",
    "jet_first_order": 0,
    "jet_last_order": JET_LAST,
    "jet_coefficient_count": JET_LAST+1,
    "jet_equations": "all272 normal eigenvector equations and beta0/beta1 normalizations",
    "exact_jet_source": "unique formal Hensel solution with the original fixed unit minor",
    "characteristic_zero_jet_coefficients_reconstructed": False,
    "V2_basis": "beta_i*z^a with i first and 0<=a<=2-epsilon_i",
    "V3_basis": "beta_i*z^a with i first and 0<=a<=3-epsilon_i",
    "V5_basis": "beta_i*z^a with i first and 0<=a<=5-epsilon_i",
    "first_kernel": {"rows": 272, "columns": 418, "rank": 272, "dimension": 146},
    "u_selection": "first normalized exact kernel basis vector with nonzero order272 coefficient",
    "pencil_a": "the selected u itself",
    "pencil_b_schedule": "sum(c^j * U_j), c=1,2,..., exact integer coefficients",
    "new_V2_multiplier_degree_bound": "2+epsilon_input-epsilon_output<=4",
    "existing_cyclic_nodes": [0, 1, 2, 3, 4],
    "multiplication_matrix_convention": "row_output_column_input",
    "pencil_complete_rank": 962,
    "fixed_chi_kernel_rank": 272,
    "fixed_chi_kernel_dimension": 418,
    "fixed_chi_kernel_equation": "u*t+b*s=0 in complete V5; projection to s",
    "single_u_product_and_690_inverse_reused_across_trials": True,
    "full_characteristic_zero_Krylov_inverse_computed": False,
    "old_W_point_kernel_and_Krylov_inverses_recomputed": False,
    "original_Gamma_or_Mg_required": False,
    "actual_five_Lj_RR128_or_144_computed": False,
    "original_t_frame_calibration_computed": False,
    "only_budget_pencil_limit_and_transport_excluded_from_identity": True,
}

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
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")).hexdigest()


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
        **identity(source),
        "certificate":plain(source["certificate"]) if source.get("certificate") else None,
        "configuration_stage":plain(source["configuration_stage"]) if source.get("configuration_stage") else None,
        "configuration_sha256":source["configuration_sha256"],
        "selected_files_sha256":fingerprint(source["files"]),
        "selected_file_count":len(source["files"]),
    }


def selected_names(source):
    if "selected_file_names" in source:
        names = source["selected_file_names"]
        assert len(names) == len(set(names))
        return names
    return sorted(source["files"])


def selected_files(source, entries):
    names = selected_names(source)
    files = {}
    for name in names:
        safe_name(name)
        files[name] = ({"file":MANIFEST,"bytes":source["manifest_bytes"],
                        "sha256":source["manifest_sha256"]} if name == MANIFEST else plain(entries[name]))
    for name,entry in source.get("file_pins",source.get("files",{})).items():
        assert files[name] == plain(entry),(name,"changed pinned original file")
    return files

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
    module_spec = importlib.util.spec_from_file_location("R872_frozen_R837_transport", path)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    module.load_io(item)
    return module


def output_manifest(out):
    files = []
    for path in sorted(out.iterdir()):
        if not path.is_file() or path.name in (MANIFEST,REFERENCE) or path.name.endswith(".tmp"):
            continue
        files.append({**file_spec(path),"included_in_git":False})
    save(out/MANIFEST,{"result":RESULT,"files":files,
        "temporary_active_checkpoint_retention_days":1,"reproducible_data_in_git_or_release":False})
    save(out/REFERENCE,{"result":RESULT,**file_spec(out/MANIFEST)})


def guard(item, request):
    assert os.environ.get("GITHUB_ACTIONS") == "true"
    assert os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public"
    assert request.resolve() == REQUEST.resolve()
    assert item["result"] == RESULT and item["p"] == 41
    assert item["producer_inputs_pending"] is False
    assert item["core"] == "R872_original_point_jets_and_fixed_Picard_space.py"
    assert item["wrapper"] == "R872_public_original_point_jets_and_fixed_Picard_space.py"
    assert sha(S/item["core"]) == item["core_sha256"]
    assert sha(__file__) == item["wrapper_sha256"]
    assert 0 < item["budget_minutes"] <= 300
    assert set(item["controls"]) == {"maximum_pencil_trials"}
    assert isinstance(item["controls"]["maximum_pencil_trials"],int)
    assert item["controls"]["maximum_pencil_trials"] > 0
    assert set(item["proofs"]) == set(PROOF_KEYS)
    assert item["proofs"]["R872"]["sha256"] == R872_PROOF_SHA
    for entry in item["proofs"].values():
        assert sha(topic_path(entry["path"])) == entry["sha256"]
    assert sha(topic_path(item["method"])) == item["method_sha256"]
    assert sha(REPO/"README.md") == item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md") == item["readme_sha256"]["topic"]
    assert set(item["sources"]) == set(SOURCE_LABELS)
    for label,source in item["sources"].items():
        assert MANIFEST in selected_names(source)
        assert all(name in selected_names(source) for name in META[:2])
        assert re.fullmatch(r"[0-9a-f]{64}",source["configuration_sha256"])
        if label == "R827":
            assert source["certificate"] is None and source["expected_conclusion"] == "failure"
            assert source["accepted_checkpoint_exit_codes"] == [124]
            assert source["configuration_stage"]["file"] == "R827-original-W-g-h-reductions.json.gz"
        else:
            assert source["certificate"]["file"] == CERTIFICATES[label]
            assert source["expected_conclusion"] == "success"
        if "files" in source:
            assert len(source["files"]) == source["selected_file_count"]
            assert fingerprint(source["files"]) == source["selected_files_sha256"]
    assert set(item["carrier_routes"]) == {"R868"}
    route = item["carrier_routes"]["R868"]
    assert route["original_member_count"] == 80
    assert route["selected_groups"] == {label:label for label in ("R805","R806","R856","R860")}
    assert set(item["intake_routes"]) == {"R827"}
    assert item["intake_routes"]["R827"]["original_member_count"] == 12
    assert set(item["inputs"]) == {
        "exact_socle","point_minor","point_inverse","point_integral_index",
        "point_values","free_basis","W_source_index","W_reduction","place_audit","Krylov_points"}
    assert len(item["inputs"]["Krylov_points"]) == 5
    return load_transport(item)


def expected_tag(item,sources):
    return {
        "result":RESULT,"source_sha256":item["core_sha256"],"p":41,"python_flint":"0.9.0",
        "method_sha256":item["method_sha256"],
        "proofs_sha256":{key:item["proofs"][key]["sha256"] for key in PROOF_KEYS},
        "sources":{label:source_identity(sources[label]) for label in SOURCE_LABELS},
        "inputs":item["inputs"],"normal_basis_degrees":EPS,"strategy":STRATEGY,
    }


def meta_review(label,source,directory):
    directory = Path(directory)
    manifest = read(bound(directory,{"file":MANIFEST,"bytes":source["manifest_bytes"],
                                     "sha256":source["manifest_sha256"]}))
    assert manifest["result"] == source["result"]
    entries = {entry["file"]:plain(entry) for entry in manifest["files"]}
    assert len(entries) == len(manifest["files"]) == source["manifest_file_count"]
    initial = read(bound(directory,entries[META[0]]))
    run = read(bound(directory,entries[META[1]]))
    assert initial["result"] == run["result"] == source["result"]
    assert initial["source_commit"] == run["source_commit"] == source["source_commit"]
    assert str(run["workflow_run_id"]) == str(source["run_id"])
    assert initial["core_sha256"] == source["core_sha256"]
    core = None
    if run.get("core_receipt_sha256") is not None:
        assert entries[META[2]]["sha256"] == run["core_receipt_sha256"]
        core = read(bound(directory,entries[META[2]]))
        assert core["result"] == source["result"] and core["source_sha256"] == source["core_sha256"]
    else:
        assert label == "R827" and run["complete"] is False
    if label == "R827":
        assert run["complete"] is False and run["process_exit_code"] in source["accepted_checkpoint_exit_codes"]
        assert source["certificate"] is None
        if core is not None:
            assert core["complete"] is False
        anchor = read(bound(directory,source["configuration_stage"]))
        assert anchor["complete"] is True
        tag,cert = anchor["configuration"],None
    else:
        assert run["complete"] is True and run["process_exit_code"] == 0 and run["error"] is None
        assert core is not None and core["complete"] is True
        certspec = plain(source["certificate"])
        assert entries[certspec["file"]] == certspec
        cert = read(bound(directory,certspec))
        assert cert["result"] == source["result"] and cert["complete"] is True
        assert core["certificate_sha256"] == certspec["sha256"]
        tag = cert["configuration"]
    assert tag["source_sha256"] == source["core_sha256"] and tag["result"] == source["result"]
    assert fingerprint(tag) == source["configuration_sha256"]
    return entries,cert,tag


def source_review(label,source,directory):
    directory = Path(directory)
    entries,cert,tag = meta_review(label,source,directory)
    files = selected_files(source,entries)
    for name,entry in files.items():
        bound(directory,entry)
        if name.endswith(".json.gz"):
            value = read(directory/name)
            assert value["complete"] is True and value["configuration"] == tag,(label,name)
    if "selected_file_count" in source:
        assert len(files) == source["selected_file_count"]
    if "selected_files_sha256" in source:
        assert fingerprint(files) == source["selected_files_sha256"]
    if label == "R868":
        for key in ("point_fiber_rank_271_certified","exact_normal_socle_vector_computed",
                    "both_point_inverse_power_ideals_certified","five_degree254_affine_module_DAGs_defined"):
            assert cert[key] is True
        h = read(bound(directory,files["R868-exact-original-normal-socle-vector.json.gz"]))
        assert h["all_272_original_W_minus_w0_equations_exactly_verified"] is True
        assert h["all_272_integral_K_equations_exactly_zero"] is True
    if label == "R827":
        W = read(bound(directory,source["configuration_stage"]))
        assert W["original_rational_denominators_all_units"] is True
        assert W["original_W_e0_equals_e1_verified"] is True
    value = {
        **identity(source),"certificate":plain(source["certificate"]) if source.get("certificate") else None,
        "configuration_stage":plain(source["configuration_stage"]) if source.get("configuration_stage") else None,
        "configuration_sha256":source["configuration_sha256"],
        "selected_files_sha256":fingerprint(files),"selected_file_count":len(files),"files":files}
    if label == "R827":
        value["accepted_checkpoint_exit_codes"] = source["accepted_checkpoint_exit_codes"]
    return value


def cross_source_review(item,sources,retained):
    c860 = read(retained/"R860"/CERTIFICATES["R860"])
    for label in ("R805","R806"):
        assert identity(c860["configuration"]["sources"][label]) == identity(sources[label])
        assert plain(c860["configuration"]["sources"][label]["certificate"]) == sources[label]["certificate"]
    c868 = read(retained/"R868"/CERTIFICATES["R868"])
    for label in ("R805","R806","R856","R860"):
        assert identity(c868["configuration"]["sources"][label]) == identity(sources[label])
        assert plain(c868["configuration"]["sources"][label]["certificate"]) == sources[label]["certificate"]
    def get(key):
        ref = item["inputs"][key]
        assert ref["source_group"] in SOURCE_LABELS
        assert sources[ref["source_group"]]["files"][ref["file"]] == plain(ref)
        return read(bound(retained/ref["source_group"],ref))
    index,point,free = get("W_source_index"),get("point_values"),get("free_basis")
    assert identity(index["source_original_R806_producer"]) == identity(sources["R806"])
    assert plain(point["source_free_basis"]) == plain(item["inputs"]["free_basis"])
    assert free["degree_distribution"] == [1,144,127]
    assert index["normal_basis_degrees"] == point["normal_basis_degrees"] == EPS
    groups = index["source_exact_coordinate_groups"]
    assert len(groups) == 34
    for ref in groups:
        assert sources["R806"]["files"][ref["file"]] == plain(ref)
    reduced,place = get("W_reduction"),get("place_audit")
    assert identity(reduced["configuration"]["source_identities"]["R806"]) == identity(sources["R806"])
    assert [plain(x) for x in reduced["source_R806_coordinate_groups"]] == [plain(x) for x in groups]
    assert reduced["prime"] == place["prime"] == PRIME
    assert place["original_zeta_root"] in get("point_minor")["roots_zeta_mod_prime"]
    for i,ref in enumerate(item["inputs"]["Krylov_points"]):
        assert ref["source_group"] == "R827"
        assert sources["R827"]["files"][ref["file"]] == plain(ref)
        stage = read(bound(retained/"R827",ref))
        assert stage["z0"] == i and stage["prime"] == PRIME
        assert stage["usable"] is True and stage["actual_cyclic_rank"] == 272
        assert stage["both_inverse_products_verified"] is True
        assert plain(stage["source_original_W"]) == plain(item["inputs"]["W_reduction"])


def fetch_selected(archive,source,directory):
    directory.mkdir(parents=True,exist_ok=True)
    archive.extract_bound(MANIFEST,source["manifest_sha256"],directory/MANIFEST,source["manifest_bytes"])
    manifest = read(directory/MANIFEST)
    entries = {entry["file"]:plain(entry) for entry in manifest["files"]}
    assert len(entries) == len(manifest["files"]) == source["manifest_file_count"]
    assert manifest["result"] == source["result"]
    assert set(archive.by_name) == set(entries)|{MANIFEST,REFERENCE}
    files = selected_files(source,entries)
    archive.extract_many([(name,ref["sha256"],directory/name,ref["bytes"])
                          for name,ref in files.items() if name != MANIFEST])
    return entries


def extract_original_groups(bundle,inventory,route,item,retained):
    members = {}
    for group,record in inventory["sources"].items():
        safe_name(group)
        for name,entry in record["files"].items():
            assert safe_name(name) == entry["file"]
            members[group+"/"+name] = plain(entry)
    assert len(members) == route["original_member_count"]
    for original,label in route["selected_groups"].items():
        source,record = item["sources"][label],inventory["sources"][original]
        assert identity(record) == identity(source)
        assert record["configuration_sha256"] == source["configuration_sha256"]
        assert plain(record["certificate"]) == plain(source["certificate"])
        for name,entry in source["files"].items():
            assert plain(record["files"][name]) == plain(entry)
        (retained/label).mkdir(parents=True,exist_ok=True)
    seen,kept = set(),[]
    with tarfile.open(bundle,"r:gz") as archive:
        for member in archive:
            name = PurePosixPath(member.name)
            assert member.isfile() and not name.is_absolute() and ".." not in name.parts and len(name.parts) == 2
            assert member.name in members and member.name not in seen
            seen.add(member.name)
            ref = members[member.name]
            assert member.size == ref["bytes"]
            group,basename = name.parts
            label = route["selected_groups"].get(group)
            selected = label is not None and basename in item["sources"][label]["files"]
            target = retained/label/basename if selected else None
            temporary = target.with_name(target.name+".transfer") if target else None
            destination = temporary.open("wb") if temporary else None
            stream = archive.extractfile(member)
            assert stream is not None
            digest,count = hashlib.sha256(),0
            try:
                for chunk in iter(lambda:stream.read(4*1024*1024),b""):
                    digest.update(chunk);count += len(chunk)
                    if destination is not None:
                        destination.write(chunk)
            finally:
                stream.close()
                if destination is not None:
                    destination.close()
            assert count == ref["bytes"] and digest.hexdigest() == ref["sha256"]
            if selected:
                temporary.replace(target)
                kept.append({"original_group":group,"selected_group":label,"file":ref})
    assert seen == set(members)
    assert len(kept) == sum(len(item["sources"][label]["files"]) for label in route["selected_groups"].values())
    return len(seen),kept


def intake_R827(item,retained,out,transport):
    route,source = item["intake_routes"]["R827"],item["sources"]["R827"]
    directory = out.parent/"intake-R827"
    directory.mkdir(parents=True,exist_ok=True)
    archive = transport.IO.Archive(route["producer"],out.parent/"download-R827-intake",whole=False)
    try:
        indexref = plain(route["source_index"])
        archive.extract_bound(indexref["file"],indexref["sha256"],directory/indexref["file"],indexref["bytes"])
        index = read(directory/indexref["file"])
        assert index["schema"] == 1 and index["new_mathematics_executed"] is False
        assert index["source_commit"] == route["producer"]["source_commit"]
        assert str(index["workflow_run_id"]) == str(route["producer"]["run_id"])
        assert index["errors"] == []
        selected = [record for record in index["sources"] if record["label"] == "R827"]
        assert len(selected) == 1
        record = selected[0]
        assert record["source"]["run_id"] == source["run_id"]
        assert record["source"]["source_commit"] == source["source_commit"]
        assert record["source"]["artifact_id"] == source["artifact_id"]
        assert plain(record["retained_input_bundle"]) == plain(route["input_bundle"])
        summaryref = plain(record["summary"])
        for ref in (summaryref,plain(route["input_bundle"])):
            archive.extract_bound(ref["file"],ref["sha256"],directory/ref["file"],ref["bytes"])
        summary = read(directory/summaryref["file"])
        assert summary["label"] == "R827" and summary["original_result"] == source["result"]
        assert summary["new_mathematics_executed"] is False
        assert summary["source_core_sha256"] == source["core_sha256"]
        assert summary["source_wrapper_sha256"] == source["wrapper_sha256"]
        assert plain(summary["manifest"]) == {"file":MANIFEST,"bytes":source["manifest_bytes"],
                                             "sha256":source["manifest_sha256"]}
        assert summary["original_manifest_count"] == source["manifest_file_count"]
        assert summary["selected_file_count"] == len(summary["selected_files"]) == 10
        originals = {name:plain(ref) for name,ref in summary["selected_files"].items()}
        originals[MANIFEST] = plain(summary["manifest"])
        originals[REFERENCE] = plain(summary["manifest_reference"])
        assert len(originals) == route["original_member_count"] == 12
        wanted = set(selected_names(source))
        assert wanted <= set(originals)
        destination = retained/"R827"
        destination.mkdir(parents=True,exist_ok=True)
        seen = set()
        with tarfile.open(directory/route["input_bundle"]["file"],"r:gz") as carrier:
            for member in carrier:
                name = PurePosixPath(member.name)
                assert member.isfile() and len(name.parts) == 2 and name.parts[0] == "original"
                assert not name.is_absolute() and ".." not in name.parts
                basename = safe_name(name.parts[1])
                assert basename in originals and basename not in seen
                seen.add(basename)
                ref = originals[basename]
                assert member.size == ref["bytes"]
                target = destination/basename if basename in wanted else None
                temporary = target.with_name(target.name+".transfer") if target else None
                output = temporary.open("wb") if temporary else None
                stream = carrier.extractfile(member)
                assert stream is not None
                digest,count = hashlib.sha256(),0
                try:
                    for chunk in iter(lambda:stream.read(4*1024*1024),b""):
                        digest.update(chunk);count += len(chunk)
                        if output is not None:
                            output.write(chunk)
                finally:
                    stream.close()
                    if output is not None:
                        output.close()
                assert count == ref["bytes"] and digest.hexdigest() == ref["sha256"]
                if target:
                    temporary.replace(target)
        assert seen == set(originals)
        reviewed = source_review("R827",source,destination)
        preserved = []
        for ref in (indexref,summaryref):
            target = out/(PREFIX+"transport-R827-"+ref["file"])
            shutil.copyfile(directory/ref["file"],target)
            preserved.append({"original_file":ref["file"],"retained_file":file_spec(target)})
        transfer = {
            "producer":route["producer"],"original_mathematical_source":identity(source),
            "input_bundle":plain(route["input_bundle"]),
            "all_original_member_count_hashed":len(seen),
            "selected_original_member_count":len(wanted),
            "transport_metadata_original_bytes":preserved,
            "range_transport":{**archive.receipt(),
                "selected_members_verified_against_original_manifest":False,
                "selected_members_verified_against_pinned_intake_index":True,
                "original_R827_members_bound_to_the_original_manifest":True},
            "original_math_tag_not_rewritten":True}
        (directory/route["input_bundle"]["file"]).unlink()
        return reviewed,transfer
    finally:
        archive.close()


def download_sources_once(item,retained,out,transport):
    reviewed,transfers = {},{}
    source,route = item["sources"]["R868"],item["carrier_routes"]["R868"]
    archive = transport.IO.Archive(source,out.parent/"download-R868",whole=False)
    metadata = out.parent/"carrier-R868"
    metadata.mkdir(parents=True,exist_ok=True)
    try:
        entries = fetch_selected(archive,source,retained/"R868")
        reviewed["R868"] = source_review("R868",source,retained/"R868")
        for ref in (route["source_inventory"],route["input_receipt"],route["input_bundle"]):
            ref = plain(ref)
            assert entries[ref["file"]] == ref
            archive.extract_bound(ref["file"],ref["sha256"],metadata/ref["file"],ref["bytes"])
        inventory = read(bound(metadata,route["source_inventory"]))
        receipt = read(bound(metadata,route["input_receipt"]))
        assert inventory["complete"] is receipt["complete"] is True
        assert inventory["result"] == receipt["result"] == source["result"]
        assert receipt["minimal_bundle_member_count"] == route["original_member_count"]
        assert plain(receipt["source_inventory"]) == plain(route["source_inventory"])
        assert plain(receipt["source_bundle"]) == plain(route["input_bundle"])
        count,kept = extract_original_groups(metadata/route["input_bundle"]["file"],inventory,route,item,retained)
        for label in route["selected_groups"].values():
            reviewed[label] = source_review(label,item["sources"][label],retained/label)
        preserved = []
        for ref in (route["source_inventory"],route["input_receipt"]):
            target = out/(PREFIX+"transport-R868-"+ref["file"])
            shutil.copyfile(metadata/ref["file"],target)
            preserved.append({"original_file":ref["file"],"retained_file":file_spec(target)})
        transfers["R868_carrier"] = {
            "producer":identity(source),"input_bundle":plain(route["input_bundle"]),
            "all_original_member_count_hashed":count,"selected_original_member_count":len(kept),
            "transport_metadata_original_bytes":preserved,"range_transport":archive.receipt(),
            "unused_R849_group_not_reopened_or_selected":True}
        (metadata/route["input_bundle"]["file"]).unlink()
    finally:
        archive.close()
    reviewed["R827"],transfers["R827_intake"] = intake_R827(item,retained,out,transport)
    assert set(reviewed) == set(SOURCE_LABELS)
    cross_source_review(item,reviewed,retained)
    return reviewed,transfers


def prepare_sources(item,out,transport,allow_download=True):
    retained = out.parent/"retained-original-R872"
    retained.mkdir(parents=True,exist_ok=True)
    if all((out/name).exists() for name in (INPUT_RECEIPT,INVENTORY,BUNDLE)):
        receipt,inventory = read(out/INPUT_RECEIPT),read(out/INVENTORY)
        assert receipt["result"] == inventory["result"] == RESULT
        assert receipt["complete"] is inventory["complete"] is True
        bound(out,receipt["source_inventory"]);bound(out,receipt["source_bundle"])
        for record in receipt["range_transport"].values():
            for entry in record["transport_metadata_original_bytes"]:
                bound(out,entry["retained_file"])
        count = transport.unpack_sources(out/BUNDLE,retained,inventory)
        reviewed = {label:source_review(label,item["sources"][label],retained/label)
                    for label in SOURCE_LABELS}
        assert reviewed == inventory["sources"]
        wanted = {label:source_identity(reviewed[label]) for label in SOURCE_LABELS}
        assert receipt["source_mathematical_identities"] == wanted
        assert count == receipt["minimal_bundle_member_count"] == sum(len(v["files"]) for v in reviewed.values())
        cross_source_review(item,reviewed,retained)
        return retained,receipt,reviewed
    assert allow_download,"The original selected input carrier is required."
    reviewed,transfers = download_sources_once(item,retained,out,transport)
    inventory = {"result":RESULT,"complete":True,"sources":reviewed,"all_original_bytes_preserved":True}
    save(out/INVENTORY,inventory)
    transport.pack_sources(retained,inventory,out/BUNDLE)
    receipt = {
        "result":RESULT,"complete":True,
        "source_mathematical_identities":{label:source_identity(reviewed[label]) for label in SOURCE_LABELS},
        "source_inventory":file_spec(out/INVENTORY),"source_bundle":file_spec(out/BUNDLE),
        "minimal_bundle_member_count":sum(len(v["files"]) for v in reviewed.values()),
        "range_transport":transfers,"new_mathematics_executed_in_source_preparation":False}
    save(out/INPUT_RECEIPT,receipt)
    print("R872_INPUT_REVIEW="+json.dumps(receipt,sort_keys=True),flush=True)
    return retained,receipt,reviewed


def stable_job(item):
    value = {key:v for key,v in item.items() if key not in (
        "resume","budget_minutes","rules_last_read_commit","readme_sha256",
        "carrier_routes","intake_routes","controls")}
    value["sources"] = {
        label:{key:v for key,v in item["sources"][label].items() if key not in (
            "directory","artifact_id","artifact_name","archive_bytes","archive_sha256",
            "artifact_expires_at","expected_conclusion","files")}
        for label in SOURCE_LABELS}
    for label in SOURCE_LABELS:
        source = item["sources"][label]
        value["sources"][label]["requested_selected_names"] = selected_names(source)
        value["sources"][label]["requested_pins"] = source.get("file_pins",source.get("files",{}))
    return value
def restore(item, out, transport):
    resume = item.get("resume")
    if resume is None:
        return
    assert resume["result"] == RESULT and resume["core_sha256"] == item["core_sha256"]
    directory = out.parent/"resume-metadata"
    directory.mkdir(parents=True,exist_ok=True)
    archive = transport.IO.Archive(resume,out.parent/"download-R872-continuation",whole=False)
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
            assert value["complete"] is (name != PREFIX+"current.json.gz")
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


def dimensions(rows,m,n):
    assert isinstance(rows,list) and len(rows) == m
    assert all(isinstance(row,list) and len(row) == n for row in rows)


def verify(item,out,request,transport):
    manifest = read(out/MANIFEST)
    assert manifest["result"] == RESULT
    entries = {entry["file"]:plain(entry) for entry in manifest["files"]}
    assert len(entries) == len(manifest["files"])
    actual = {path.name for path in out.iterdir() if path.is_file()
              and path.name not in (MANIFEST,REFERENCE) and not path.name.endswith(".tmp")}
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
        if name == PREFIX+"current.json.gz":
            assert value["complete"] is False and isinstance(value["phase"],str)
        else:
            assert value["complete"] is True
            if name != PREFIX+"exact-stages-manifest.json.gz":
                complete_stages[name] = ref
    def stage(ref):
        ref = plain(ref)
        assert entries[ref["file"]] == ref
        value = read(bound(out,ref))
        assert value["complete"] is True and value["result"] == RESULT and value["configuration"] == tag
        return value
    def original(ref):
        assert ref["source_group"] in sources
        assert sources[ref["source_group"]]["files"][ref["file"]] == plain(ref)
        return read(bound(retained/ref["source_group"],ref))
    core = read(out/META[2]) if META[2] in entries else None
    if core is None:
        assert run["complete"] is False and run["core_receipt_sha256"] is None
    else:
        assert core["result"] == RESULT and core["source_sha256"] == item["core_sha256"]
        assert run["core_receipt_sha256"] == entries[META[2]]["sha256"]
    final = read(out/FINAL) if FINAL in entries else None
    if final is not None:
        assert final["result"] == RESULT and final["configuration"] == tag
        assert final["source_identities"] == {label:source_identity(sources[label]) for label in SOURCE_LABELS}
        for key in ("five_original_Lj_RR128_computed","five_original_Lj_weight_one_144_complements_computed",
                    "original_t_frame_calibration_computed","original_Gamma_or_Mg_computed",
                    "connection_Poincare_period_or_height_computed"):
            assert final[key] is False
        inventory = stage(final["stage_manifest"])
        indexed = {ref["file"]:plain(ref) for ref in inventory["files"]}
        assert len(indexed) == len(inventory["files"])
        for ref in indexed.values():
            assert entries[ref["file"]] == ref
        if final["resume_state"] is not None:
            ref = plain(final["resume_state"])
            assert ref["file"] == PREFIX+"current.json.gz"
            assert entries[ref["file"]] == ref
        if final["complete"]:
            assert indexed == complete_stages
            assert core is not None and core["complete"] is True and core["error"] is None
            assert core["certificate_sha256"] == entries[FINAL]["sha256"]
            for key in ("actual_original_P0_jets_through_order272_computed",
                        "actual_original_complete_146_kernel_certified",
                        "actual_fixed_chi_complete_418_RR_space_certified"):
                assert final[key] is core[key] is True
            assert final["actual_original_P0_local_parameter_certified"] is True
            assert final["actual_fixed_degree272_divisor_certified"] is True
            assert final["actual_pencil_rank"] == core["actual_pencil_rank"] == 962
            assert final["characteristic_zero_sources_are_exact_unit_solve_expressions"] is True
            assert final["characteristic_zero_jet_or_RR_coefficients_reconstructed"] is False
            audit = stage(final["source_audit"])
            linear = stage(final["point_linearization"])
            assert audit["source_point_linearization"] == final["point_linearization"]
            assert linear["chosen_local_parameter"] == audit["chosen_local_parameter"]
            assert linear["chosen_parameter_derivative_is_a_unit"] is True
            assert linear["source_exact_socle"] == item["inputs"]["exact_socle"]
            assert linear["source_point_values"] == item["inputs"]["point_values"]
            assert linear["source_W_reduction"] == item["inputs"]["W_reduction"]
            assert audit["all_original_W_polynomial_coefficients_are_integral_at_this_place"] is True
            assert audit["integrality_not_inferred_from_only_W_at_P0"] is True
            dimensions(linear["A0_mod_prime"],272,272)
            assert len(linear["Taylor_W_coefficients_mod_prime"]) == 4
            for matrix in linear["Taylor_W_coefficients_mod_prime"]:
                dimensions(matrix,272,272)
            jets = stage(final["point_jets"])
            assert jets["source_point_linearization"] == final["point_linearization"]
            assert jets["coefficient_count"] == len(jets["orders"]) == 273
            assert jets["first_order"] == 0 and jets["last_order"] == 272
            assert jets["all273_orders_and_all272_normal_equations_verified"] is True
            previous = None
            for n,ref in enumerate(jets["orders"]):
                value = stage(ref)
                assert value["order"] == n and value["source_previous_order"] == previous
                assert value["source_point_linearization"] == final["point_linearization"]
                assert value["all272_original_eigenvector_equations_verified_at_this_order"] is True
                assert value["beta0_and_beta1_normalizations_verified"] is True
                assert value["rational_coefficients_reconstructed"] is False
                assert len(value["normal_basis_jet_mod_prime"]) == 272
                previous = ref
            J = stage(final["original_V2_jet_matrix"])
            assert J["source_point_jets"] == final["point_jets"]
            assert J["row_orders"] == list(range(273)) and J["matrix_shape"] == [273,418]
            dimensions(J["matrix_mod_prime"],273,418)
            U = stage(final["complete_original_146_kernel"])
            assert U["source_jet_matrix"] == final["original_V2_jet_matrix"]
            assert U["accepted"] is True and U["actual_rank_mod_prime"] == 272
            assert U["actual_kernel_dimension"] == U["characteristic_zero_kernel_dimension"] == 146
            assert U["both_selected_inverse_products_verified"] is True
            assert U["all272_by146_residuals_zero"] is True
            assert U["full_characteristic_zero_RR_kernel_certified"] is True
            assert len(U["selected_pivot_columns"]) == 272 and len(U["free_columns"]) == 146
            assert sorted(U["selected_pivot_columns"]+U["free_columns"]) == list(range(418))
            dimensions(U["kernel_basis_mod_prime"],418,146)
            dimensions(U["actual_selected_minor_mod_prime"],272,272)
            dimensions(U["inverse_selected_minor_mod_prime"],272,272)
            assert len(U["extra_order272_coefficients_mod_prime"]) == 146
            u = stage(final["anchor_u"])
            assert u["source_complete_kernel"] == final["complete_original_146_kernel"]
            assert u["role"] == "u" and u["order272_is_exact"] is True
            assert 0 < u["exact_order272_unit"] < PRIME
            b = stage(final["accepted_anchor_b"])
            assert b["source_complete_kernel"] == final["complete_original_146_kernel"]
            assert b["role"] == "b" and b["trial"] == final["accepted_pencil_trial"]
            for product_ref,anchor_ref in (
                (final["u_product"],final["anchor_u"]),
                (final["accepted_b_product"],final["accepted_anchor_b"])):
                product = stage(product_ref)
                assert product["source_anchor"] == anchor_ref
                assert product["matrix_shape"] == [1234,690]
                dimensions(product["matrix_mod_prime"],1234,690)
                assert product["all_terms_outside_V5_verified_zero"] is True
                multiplier = stage(product["source_multiplier"])
                assert multiplier["source_anchor"] == anchor_ref
                assert multiplier["nodes"] == [0,1,2,3,4]
                assert multiplier["source_original_Krylov_points"] == item["inputs"]["Krylov_points"]
                assert multiplier["weighted_support_verified"] is True
                assert multiplier["first_column_verified_at_all_coefficients"] is True
                assert multiplier["abstract_characteristic_zero_multiplier_and_true_modular_image_certified"] is True
                assert multiplier["characteristic_zero_multiplier_coefficients_reconstructed"] is False
                assert multiplier["old_point_matrices_or_Krylov_inverses_recomputed"] is False
                assert len(multiplier["coefficient_matrices_mod_prime"]) == 5
                for matrix in multiplier["coefficient_matrices_mod_prime"]:
                    dimensions(matrix,272,272)
                assert len(multiplier["point_stages"]) == 5
                for n,ref in enumerate(multiplier["point_stages"]):
                    point = stage(ref)
                    assert point["source_original_Krylov"] == item["inputs"]["Krylov_points"][n]
                    assert point["source_anchor"] == anchor_ref and point["z0"] == n
                    assert point["old_Krylov_inverse_reused"] is True
                    assert point["first_column_equals_original_anchor_value"] is True
                    dimensions(point["matrix_mod_prime"],272,272)
            uq = stage(final["u_quotient"])
            assert uq["source_u_product"] == final["u_product"] and uq["accepted"] is True
            assert uq["actual_image_rank_mod_prime"] == 690
            assert len(uq["row_indices"]) == 690 and len(uq["remaining_row_indices"]) == 544
            assert sorted(uq["row_indices"]+uq["remaining_row_indices"]) == list(range(1234))
            assert uq["both_selected_inverse_products_verified"] is True
            dimensions(uq["selected_inverse_mod_prime"],690,690)
            dimensions(uq["quotient_coefficient_matrix_mod_prime"],544,690)
            profile = stage(final["accepted_pencil_profile"])
            assert profile["accepted"] is True and profile["actual_pencil_rank_mod_prime"] == 962
            assert profile["actual_quotient_rank_mod_prime"] == 272
            kernel = stage(final["complete_fixed_chi_418_kernel"])
            assert kernel["source_rank_profile"] == final["accepted_pencil_profile"]
            assert kernel["source_anchor_u"] == final["anchor_u"]
            assert kernel["source_anchor_b"] == final["accepted_anchor_b"]
            assert kernel["source_u_product"] == final["u_product"]
            assert kernel["source_b_product"] == final["accepted_b_product"]
            assert kernel["source_u_quotient"] == final["u_quotient"]
            Q = stage(kernel["source_quotient"])
            assert profile["source_quotient"] == kernel["source_quotient"]
            dimensions(Q["matrix_mod_prime"],544,690)
            assert kernel["actual_pencil_rank_mod_prime"] == 962
            assert kernel["actual_quotient_rank_mod_prime"] == 272
            assert kernel["actual_kernel_dimension"] == kernel["full_characteristic_zero_dimension"] == 418
            assert kernel["all544_by418_quotient_residuals_zero"] is True
            assert kernel["all1234_by418_complete_V5_relations_zero"] is True
            assert kernel["exact_full_characteristic_zero_W_Dchi_certified"] is True
            assert kernel["combined_minor_nonzero_by_unit_block_Schur_factorization"] is True
            assert kernel["both_selected_inverse_products_verified"] is True
            assert len(kernel["combined_962_minor_original_rows"]) == 962
            assert len(kernel["combined_962_minor_original_columns"]) == 962
            assert len(kernel["selected_quotient_rows"]) == len(kernel["selected_pivot_columns"]) == 272
            assert len(kernel["free_columns"]) == 418
            assert sorted(kernel["selected_pivot_columns"]+kernel["free_columns"]) == list(range(690))
            dimensions(kernel["V3_kernel_basis_mod_prime"],690,418)
            dimensions(kernel["paired_u_multiplier_coordinates_mod_prime"],690,418)
            divisor = stage(final["fixed_chi_divisor_and_principal_function"])
            assert divisor["source_exact_u"] == final["anchor_u"]
            assert divisor["source_exact_b"] == final["accepted_anchor_b"]
            assert divisor["source_complete_W_Dchi"] == final["complete_fixed_chi_418_kernel"]
            assert divisor["D_chi_degree"] == 272 and divisor["D_chi_effective_and_avoids_original_P0"] is True
            assert divisor["actual_complete_fixed_chi_RR_space_certified"] is True
            assert divisor["principal_function"]["tau_power"] == 2
            assert divisor["original_five_eta_ideals_changed"] is False
        else:
            assert run["complete"] is False
    if run["complete"]:
        assert run["process_exit_code"] == 0 and run["error"] is None
        assert final is not None and final["complete"] is True
    summary = {
        "result":RESULT,"complete":bool(final and final["complete"]),
        "all_output_bytes_and_source_identities_verified":True,
        "actual_selected_source_count":receipt["minimal_bundle_member_count"],
        "actual_complete_stage_count":len(complete_stages),
        "actual_original_P0_jets_through_order272_computed":
            bool(final and final["actual_original_P0_jets_through_order272_computed"]),
        "actual_original_complete_146_kernel_certified":
            bool(final and final["actual_original_complete_146_kernel_certified"]),
        "actual_fixed_chi_complete_418_RR_space_certified":
            bool(final and final["actual_fixed_chi_complete_418_RR_space_certified"]),
        "actual_pencil_rank":final["actual_pencil_rank"] if final else None,
        "five_original_Lj_RR128_computed":False,
        "five_original_Lj_weight_one_144_complements_computed":False,
        "connection_Poincare_period_or_height_computed":False,
        "new_mathematics_executed_in_verifier":False}
    print("R872_VERIFY="+json.dumps(summary,sort_keys=True),flush=True)
    return 0


def main():
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode",choices=("compute","verify"))
    parser.add_argument("--request",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    args = parser.parse_args()
    item = read(args.request)
    transport = guard(item,args.request)
    code = compute(item,args.output,args.request,transport) if args.mode == "compute" else \
        verify(item,args.output,args.request,transport)
    raise SystemExit(code)


if __name__ == "__main__":
    main()
