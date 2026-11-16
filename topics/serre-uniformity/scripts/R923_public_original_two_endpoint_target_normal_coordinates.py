#!/usr/bin/env python3
"""Standard-library provenance, resume and output review for original endpoint target functions."""
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

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
TOPIC = REPO / "topics/serre-uniformity"
REQUEST = TOPIC / "notes/R923-original-two-endpoint-target-normal-coordinates-public-request.json"
RESULT = "R923-original-two-endpoint-target-normal-coordinates"
FINAL = "p41-original-two-endpoint-target-normal-coordinates-certificate.json"
PREFIX = "R923-target-"
CURRENT = PREFIX + "current.json.gz"
INVENTORY = PREFIX + "stage-manifest.json.gz"
PRIME, ZETA, SROOT = 1000000753, 549966761, 99932770
DIM, NORMAL, COLUMN_BLOCK, LEVEL_BLOCK = 8, 272, 16, 16
EPS = [0] + [1] * 144 + [2] * 127
BASE = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
META = ("public-actions-input.json", "run-receipt.json", "core-receipt.json")
SOURCES = ("R917", "POLY", "R827", "R873")
PROOFS = ("R923", "R917", "R912", "R860", "R885", "R873")
HELPER_SHA = "c728c8e06cef3dfbe4d33f3a988cbbc1c3012909d67b4684d941effdec67033d"
H64 = re.compile(r"[0-9a-f]{64}")
DEFINITIONS = {
    "R917": ("R917-original-two-endpoint-normal-orders",
        "f0e321a19ef6dbd259e88de1b670f514b0f9ed0df5b24659a9f787978b8fd743"),
    "POLY": ("R885-original-polynomial-one-row-adjugate",
        "dd4ef0d445e7c90caf568d7aa87951166d6730cc86da0a44be11b664742d3035"),
    "R827": ("R827-original-global-modular-derivative-termination",
        "d9cf773976f3beff7f44ff30f8b593665f481470cb52297239710e0ce6e062d2"),
    "R873": ("R873-original-cyclic-seven-correspondence",
        "3c4922ee5b83d82123d234df47e67f82d7c8032f1152c6cf14df34622101918c"),
}
STRATEGY = {
    "scope": "two_original_endpoint_target_w_and_all272_normal_functions",
    "original_auxiliary_prime": PRIME, "original_zeta_root": ZETA, "original_s_root": SROOT,
    "rank": DIM, "normal_dimension": NORMAL,
    "endpoint_parameters": ["rho0=z-z0", "rho1=iota^*rho0=z-2*beta72-z0"],
    "actual_R917_primitive_h": 0, "actual_R917_primitive_precision": 273,
    "actual_R917_primitive_discriminant_order": 6,
    "actual_R917_normal_order_precision": 271,
    "target_w": "B_inverse*adj(M_mprime)*(Ktilde/Ptilde8), then divide old primitive disc",
    "old_primitive_discriminant_recomputed": False,
    "target_w_uniform_precision": 267,
    "shared_adjugate_algorithm": "seven constant-unit Newton matrix steps; both adjugate products",
    "polynomial_source": "complete original R885 row levels0..271; no z0 coordinate substitution",
    "normal_column_block": COLUMN_BLOCK, "Horner_level_block": LEVEL_BLOCK,
    "first_cofactor_block_precedes_shared_denominator_decision": True,
    "integral_quotient_precision": "N-vrho(det); deflate all numerators before unit inversion",
    "zero_truncation": "NeedPrecision, never an exact zero or inactive flag",
    "full_verification": "Ptilde_U*V=Ktilde; chi(U,V)=0; gamma0=1; gamma1=V; all272 gammaW=Vgamma",
    "all_factors_nilpotents_and_original_P_K_preserved": True,
    "basis_and_original_t_frame": "unchanged source R917, both determinant factors under original dual7",
    "exact_nu": "82*tau*dqY/qY; iota fixes nu; no new numeric differential transport",
    "no_original_W_Krylov_273nodes_polynomial_adjugate_or_idealizer_recomputed": True,
    "characteristic_zero_expanded_coordinates": False,
    "only_budget_and_transport_paths_excluded_from_identity": True,
}

STAGES = INVENTORY
MANIFEST = "full-outputs-manifest.json"
REFERENCE = "full-outputs-manifest-reference.json"
BUNDLE = "R923-retained-original-inputs.tar.gz"
SOURCE_INVENTORY = "R923-original-source-inventory.json"
INPUT_RECEIPT = "R923-retained-inputs-receipt.json"
EXPANDED = "public-actions-expanded-job.json"
RANGE_SHA = "c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
FINALS = {
    "R917": "p41-original-two-endpoint-normal-orders-certificate.json",
    "POLY": "p41-original-polynomial-one-row-adjugate-certificate.json",
    "R873": "p41-original-cyclic-seven-correspondence-certificate.json",
}
PARENT_FILES = {
    "R917": {"bundle": "R917-retained-original-inputs.tar.gz",
             "inventory": "R917-original-source-inventory.json",
             "receipt": "R917-retained-inputs-receipt.json"},
    "POLY": {"bundle": "R885-retained-R827-inputs.tar.gz",
             "inventory": "R885-original-source-inventory.json",
             "receipt": "R885-retained-inputs-receipt.json"},
}
def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1048576), b""):
            h.update(block)
    return h.hexdigest()


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                    ensure_ascii=False).encode()).hexdigest()


def plain(value):
    answer = {k: value[k] for k in ("file", "bytes", "sha256")}
    assert Path(answer["file"]).name == answer["file"] and "\\" not in answer["file"]
    assert isinstance(answer["bytes"], int) and answer["bytes"] >= 0
    assert H64.fullmatch(answer["sha256"])
    return answer


def spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def read(path):
    path = Path(path)
    with (gzip.open(path, "rt", encoding="utf-8") if path.name.endswith(".gz")
          else path.open("r", encoding="utf-8")) as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    payload = (json.dumps(value, sort_keys=True, separators=(",", ":"),
                          ensure_ascii=False) + "\n").encode()
    with tmp.open("wb") as raw:
        if path.name.endswith(".gz"):
            with gzip.GzipFile(filename="", fileobj=raw, mode="wb", mtime=0, compresslevel=2) as stream:
                stream.write(payload)
        else:
            raw.write(payload)
        raw.flush()
        os.fsync(raw.fileno())
    tmp.replace(path)


def identity(value):
    return {k: str(value[k]) for k in BASE}


def source_identity(value):
    return {**identity(value), "configuration_sha256": value["configuration_sha256"],
        "selected_files_sha256": value["selected_files_sha256"],
        "selected_file_count": value["selected_file_count"],
        "certificate": None if value.get("certificate") is None else plain(value["certificate"]),
        "configuration_stage": None if value.get("configuration_stage") is None
                                    else plain(value["configuration_stage"])}


def expected_tag(item):
    return {"result": RESULT, "source_sha256": item["core_sha256"],
        "helper_sha256": item["helper_sha256"], "p": 41, "prime": PRIME,
        "python_flint": "0.9.0", "method_sha256": item["method_sha256"],
        "proofs_sha256": {k: item["proofs"][k]["sha256"] for k in PROOFS},
        "sources": {k: source_identity(item["sources"][k]) for k in SOURCES},
        "inputs": item["inputs"],
        "requested_minimum_output_precision": item["requested_minimum_output_precision"],
        "strategy": STRATEGY}


def bound(folder, value):
    value = plain(value)
    path = Path(folder)/value["file"]
    assert spec(path) == value, str(path)
    return path


def topic_path(name):
    p = PurePosixPath(name)
    assert not p.is_absolute() and ".." not in p.parts
    path = (TOPIC/str(p)).resolve()
    assert path.is_relative_to(TOPIC.resolve())
    return path


def load_module(name, path, expected):
    assert sha(path) == expected
    loader = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(loader)
    loader.loader.exec_module(module)
    return module


def guard(item):
    assert os.environ.get("GITHUB_ACTIONS") == "true"
    assert os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public"
    assert item["result"] == RESULT and item["p"] == 41
    assert item["producer_inputs_pending"] is False
    assert item["future_target_sources"] == {"R903": None, "R907": None}
    assert item["core"] == "R923_original_two_endpoint_target_normal_coordinates.py"
    assert item["helper"] == "R917_endpoint_order_arithmetic.py"
    assert item["helper_sha256"] == HELPER_SHA
    assert item["wrapper"] == Path(__file__).name
    assert sha(HERE/item["core"]) == item["core_sha256"]
    assert sha(HERE/item["helper"]) == HELPER_SHA
    assert sha(__file__) == item["wrapper_sha256"]
    assert 0 < item["budget_minutes"] <= 300
    assert 1 <= item["requested_minimum_output_precision"] <= 267
    assert sha(REPO/"README.md") == item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md") == item["readme_sha256"]["topic"]
    assert set(item["source_pins"]) == set(SOURCES)
    assert set(item["source_artifacts"]) == {"R917","POLY"}
    assert set(item["proofs"]) == set(PROOFS)
    for value in item["proofs"].values():
        assert sha(topic_path(value["file"])) == value["sha256"]
    assert sha(topic_path(item["method"])) == item["method_sha256"]
    for label, source in item["source_pins"].items():
        assert (source["result"],source["core_sha256"]) == DEFINITIONS[label]
        assert H64.fullmatch(source["configuration_sha256"])
        assert source["manifest_bytes"] > 0 and source["manifest_file_count"] > 0
        if label == "R827":
            assert source["certificate"] is None
            assert plain(source["configuration_stage"]) == plain(item["input_pins"]["original_W"])
        else:
            assert source["certificate"]["file"] == FINALS[label]
        if label in item["source_artifacts"]:
            assert identity(source) == identity(item["source_artifacts"][label])
    assert item["io_helper"] == "R824_public_original_global_polar_generators.py"
    assert item["io_helper_sha256"] == RANGE_SHA
    return load_module("R923_frozen_Range_IO",HERE/item["io_helper"],RANGE_SHA)


def entry_map(folder, source):
    manifest_path = Path(folder)/MANIFEST
    assert manifest_path.stat().st_size == source["manifest_bytes"]
    assert sha(manifest_path) == source["manifest_sha256"]
    manifest = read(manifest_path)
    assert manifest["result"] == source["result"]
    entries = {row["file"]:plain(row) for row in manifest["files"]}
    assert len(entries) == len(manifest["files"]) == source["manifest_file_count"]
    entries[MANIFEST] = spec(manifest_path)
    return entries


def open_primary(io_module, source, folder, work):
    folder.mkdir(parents=True,exist_ok=True)
    archive = io_module.Archive(source,work,whole=False)
    try:
        if not (folder/MANIFEST).exists():
            archive.extract_bound(MANIFEST,source["manifest_sha256"],folder/MANIFEST,source["manifest_bytes"])
        entries = entry_map(folder,source)
        assert set(archive.by_name) == (set(entries)-{MANIFEST})|{MANIFEST,REFERENCE}
        for name,row in entries.items():
            assert len(archive.by_name[name]) == 1
            assert archive.by_name[name][0].file_size == row["bytes"]
        return archive,entries
    except BaseException:
        archive.close()
        raise


def extract_names(archive, entries, folder, names):
    todo = []
    for name in sorted(set(names)):
        assert name in entries,name
        row = entries[name]
        if (folder/name).exists():
            bound(folder,row)
        else:
            todo.append((name,row["sha256"],folder/name,row["bytes"]))
    archive.extract_many(todo)


def source_review(label, source, folder, names):
    expected = {k:source[k] for k in BASE}
    assert (source["result"],source["core_sha256"]) == DEFINITIONS[label]
    entries = entry_map(folder,source)
    files = {name:entries[name] for name in sorted(set(names))}
    for row in files.values():
        bound(folder,row)
    assert {MANIFEST,*META} <= set(files)
    initial,run,core = (read(folder/name) for name in META)
    assert initial["source_commit"] == run["source_commit"] == source["source_commit"]
    assert str(run["workflow_run_id"]) == str(source["run_id"])
    recorded = initial["core_sha256"] if "core_sha256" in initial else initial["job"]["core_sha256"]
    assert recorded == core["source_sha256"] == source["core_sha256"]
    if run.get("core_receipt_sha256") is not None:
        assert run["core_receipt_sha256"] == files["core-receipt.json"]["sha256"]
    if label == "R827":
        assert source["certificate"] is None
        assert run["complete"] is False and core["complete"] is False
        assert run["process_exit_code"] == 124
        anchor = read(bound(folder,source["configuration_stage"]))
        assert anchor["complete"] is True
        tag = anchor["configuration"]
    else:
        assert run["complete"] is True and run["process_exit_code"] == 0
        assert core["complete"] is True
        cert = read(bound(folder,source["certificate"]))
        assert cert["result"] == source["result"] and cert["complete"] is True
        assert core["certificate_sha256"] == source["certificate"]["sha256"]
        tag = cert["configuration"]
    assert fingerprint(tag) == source["configuration_sha256"]
    assert tag.get("source_sha256",tag.get("core_sha256")) == source["core_sha256"]
    return {**expected,"manifest_bytes":source["manifest_bytes"],
        "manifest_file_count":source["manifest_file_count"],
        "configuration_sha256":source["configuration_sha256"],
        "certificate":None if source.get("certificate") is None else plain(source["certificate"]),
        "configuration_stage":None if source.get("configuration_stage") is None else plain(source["configuration_stage"]),
        "files":files,"selected_file_count":len(files),"selected_files_sha256":fingerprint(files)}


def stage_bound(folder, source, row, tag):
    value = read(bound(folder,row))
    assert value["complete"] is True and value["configuration"] == tag
    assert value.get("result",tag["result"]) == source["result"]
    return value


def inspect_parent_metadata(label, source, folder, entries):
    assert entries[source["certificate"]["file"]] == plain(source["certificate"])
    required = {MANIFEST,*META,source["certificate"]["file"]}
    review = source_review(label,source,folder,required)
    cert = read(folder/source["certificate"]["file"])
    return review,cert


def unpack_selected_carrier(bundle, groups, requested, retained):
    # Every original carrier member is hashed, including those not retained.
    expected = {(label,name):plain(row) for label,group in groups.items()
                for name,row in group["files"].items()}
    seen = set()
    with tarfile.open(bundle,"r|gz") as archive:
        for member in archive:
            if member.isdir():
                continue
            path = PurePosixPath(member.name)
            assert not path.is_absolute() and ".." not in path.parts and "\\" not in member.name
            assert member.isfile() and len(path.parts)==2
            key = (path.parts[0],path.name)
            assert key in expected and key not in seen
            row = expected[key]
            assert member.size == row["bytes"]
            wanted = key[0] in requested and key[1] in requested[key[0]]
            destination = retained/key[0]/key[1]
            temporary = destination.with_name(destination.name+".download")
            if wanted:
                destination.parent.mkdir(parents=True,exist_ok=True)
                output = temporary.open("wb")
            else:
                output = None
            h=hashlib.sha256();count=0
            try:
                with archive.extractfile(member) as stream:
                    for data in iter(lambda:stream.read(4*1024*1024),b""):
                        h.update(data);count+=len(data)
                        if output is not None:output.write(data)
            finally:
                if output is not None:output.close()
            assert count==row["bytes"] and h.hexdigest()==row["sha256"],key
            if wanted:
                if destination.exists():
                    assert spec(destination)==row
                    temporary.unlink()
                else:
                    temporary.replace(destination)
            seen.add(key)
    assert seen==set(expected)
    assert all((label,name) in seen for label,names in requested.items() for name in names)
    return {"all_original_member_count":len(seen),
            "retained_member_count":sum(len(names) for names in requested.values()),
            "all_original_member_hashes_verified":True}


def pack_sources(retained, sources, target):
    temporary = target.with_name(target.name+".tmp")
    with temporary.open("wb") as raw:
        with gzip.GzipFile(filename="",fileobj=raw,mode="wb",mtime=0,compresslevel=2) as zipped:
            with tarfile.open(fileobj=zipped,mode="w|") as archive:
                for label,source in sorted(sources.items()):
                    for name,row in sorted(source["files"].items()):
                        path=bound(retained/label,row)
                        info=archive.gettarinfo(str(path),arcname=label+"/"+name)
                        info.uid=info.gid=0;info.uname=info.gname="";info.mtime=0
                        with path.open("rb") as stream:
                            archive.addfile(info,stream)
    temporary.replace(target)


def source_template(item,label):
    return item["source_pins"][label]


def derive_R917_selection(item, folder, cert, entries):
    source=source_template(item,"R917")
    tag=cert["configuration"]
    names={MANIFEST,*META,source["certificate"]["file"]}
    audit_name="R917-endpoint-source-audit.json.gz"
    names.add(audit_name)
    # Math files are pinned by the original completed certificate and manifest.
    inputs={"completed_order_source_audit":dict(entries[audit_name],source_group="R917"),"endpoints":{}}
    for epsilon in (0,1):
        cref=plain(cert["completed_endpoint_certificates"][str(epsilon)])
        ec=stage_bound(folder,source,cref,tag)
        mapping={"certificate":cref,"common_cleared":plain(ec["source_common_cleared_jets"]),
            "primitive":plain(ec["source_primitive_order"]),"normal_order":plain(ec["complete_normal_order"]),
            "normal_discriminant":plain(ec["complete_trace_discriminant"]),
            "special_fibre":plain(ec["complete_length8_special_fibre"]),
            "frame":plain(ec["primitive_and_t_frames"]),
            "primitive_discriminant":entries[f"R917-endpoint-P{epsilon}-order-000-discriminant.json.gz"]}
        assert len(ec["enlargements"])==1 and ec["enlargements"][0]["step"]==0
        mapping["idealizer_kernel"]=plain(ec["enlargements"][0]["kernel"])
        for row in mapping.values():
            assert entries[row["file"]]==plain(row)
            names.add(row["file"])
        inputs["endpoints"][str(epsilon)]=mapping
    names.add(cert["stage_manifest"]["file"])
    assert entries[cert["stage_manifest"]["file"]]==plain(cert["stage_manifest"])
    return names,inputs


def prepare_sources(item,out,io_module,allow_download=True):
    retained=out.parent/"R923-retained-original"
    retained.mkdir(parents=True,exist_ok=True)
    if all((out/name).exists() for name in (BUNDLE,SOURCE_INVENTORY,INPUT_RECEIPT)):
        inventory=read(out/SOURCE_INVENTORY);receipt=read(out/INPUT_RECEIPT)
        assert inventory["result"]==receipt["result"]==RESULT
        assert inventory["complete"] is True and receipt["complete"] is True
        bound(out,receipt["source_bundle"]);bound(out,receipt["source_inventory"])
        sources=inventory["sources"];inputs=inventory["inputs"]
        assert set(sources)==set(SOURCES)
        for label in SOURCES:
            pin=source_template(item,label)
            assert identity(sources[label])==identity(pin)
            assert sources[label]["configuration_sha256"]==pin["configuration_sha256"]
            assert sources[label]["certificate"]==pin.get("certificate")
        unpack_selected_carrier(out/BUNDLE,sources,
            {label:set(sources[label]["files"]) for label in SOURCES},retained)
        reviewed={label:source_review(label,source_template(item,label),retained/label,
                                      sources[label]["files"]) for label in SOURCES}
        assert reviewed==sources
        expanded=dict(item,sources=sources,inputs=inputs)
        assert receipt["actual_configuration"]==expected_tag(expanded)
        return retained,sources,inputs,receipt
    assert allow_download,"A completed original-source carrier is required for this output review"
    routes={}
    # R917 parent contributes its actual own endpoint stages and original R873 bytes.
    label="R917";source=source_template(item,label);folder=retained/label
    archive,entries=open_primary(io_module,item["source_artifacts"][label],folder,out.parent/"R923-fetch-R917")
    try:
        first={*META,source["certificate"]["file"],"R917-endpoint-source-audit.json.gz",*PARENT_FILES[label].values()}
        extract_names(archive,entries,folder,first)
        unused,cert=inspect_parent_metadata(label,source,folder,entries)
        assert cert["actual_original_two_endpoint_normal_orders_certified"] is True
        endpoint_certs=[plain(x) for x in cert["completed_endpoint_certificates"].values()]
        extract_names(archive,entries,folder,[x["file"] for x in endpoint_certs])
        names917,inputs=derive_R917_selection(item,folder,cert,entries)
        extract_names(archive,entries,folder,names917)
        par=read(folder/PARENT_FILES[label]["receipt"])
        inv=read(folder/PARENT_FILES[label]["inventory"])
        assert par["result"]==inv["result"]==source["result"] and par["complete"] is True and inv["complete"] is True
        assert plain(par["source_bundle"])==entries[PARENT_FILES[label]["bundle"]]
        assert plain(par["source_inventory"])==entries[PARENT_FILES[label]["inventory"]]
        assert identity(inv["sources"]["R873"])==identity(source_template(item,"R873"))
        requested873={MANIFEST,*META,source_template(item,"R873")["certificate"]["file"],
            item["input_pins"]["correspondence_DAG"]["file"],
            item["input_pins"]["exact_coordinate_expression"]["file"]}
        route=unpack_selected_carrier(folder/PARENT_FILES[label]["bundle"],inv["sources"],
                                     {"R873":requested873},retained)
        routes["R873_via_R917"]={**route,"bundle":entries[PARENT_FILES[label]["bundle"]],
            "inventory":entries[PARENT_FILES[label]["inventory"]],"receipt":entries[PARENT_FILES[label]["receipt"]]}
        routes[label]=archive.receipt()
    finally:
        archive.close()
    # POLY parent supplies all old polynomial row levels and the original R827 carrier.
    label="POLY";source=source_template(item,label);folder=retained/label
    archive,entries=open_primary(io_module,item["source_artifacts"][label],folder,out.parent/"R923-fetch-POLY")
    try:
        first={*META,source["certificate"]["file"],item["input_pins"]["adjugate_row_index"]["file"],
               item["input_pins"]["characteristic_relation"]["file"],*PARENT_FILES[label].values()}
        extract_names(archive,entries,folder,first)
        unused,cert=inspect_parent_metadata(label,source,folder,entries)
        tag=cert["configuration"]
        adj=stage_bound(folder,source,item["input_pins"]["adjugate_row_index"],tag)
        assert adj["r_is_exactly_original_e0_transpose_adjugate"] is True
        assert adj["all272_polynomial_components_of_terminal_row_zero"] is True
        levels=[]
        for k,term in enumerate(adj["adjugate_row_T_terms"]):
            assert term["b_level"]==k and term["T_power"]==271-k
            row=plain(term["source"]);assert entries[row["file"]]==row
            levels.append(dict(row,source_group="POLY"))
        assert len(levels)==272
        namespoly={MANIFEST,*META,source["certificate"]["file"],
            item["input_pins"]["adjugate_row_index"]["file"],
            item["input_pins"]["characteristic_relation"]["file"],*(x["file"] for x in levels)}
        extract_names(archive,entries,folder,namespoly)
        inv=read(folder/PARENT_FILES[label]["inventory"])
        par=read(folder/PARENT_FILES[label]["receipt"])
        assert inv["result"]==par["result"]==source["result"] and inv["complete"] is True and par["complete"] is True
        assert plain(par["source_bundle"])==entries[PARENT_FILES[label]["bundle"]]
        assert plain(par["source_inventory"])==entries[PARENT_FILES[label]["inventory"]]
        old=inv["source_R827"]
        assert identity(old)==identity(source_template(item,"R827"))
        assert old["configuration_sha256"]==source_template(item,"R827")["configuration_sha256"]
        requested827={MANIFEST,*META,item["input_pins"]["original_W"]["file"],item["input_pins"]["original_place"]["file"]}
        route=unpack_selected_carrier(folder/PARENT_FILES[label]["bundle"],{"R827":old},
                                     {"R827":requested827},retained)
        routes["R827_via_POLY"]={**route,"bundle":entries[PARENT_FILES[label]["bundle"]],
            "inventory":entries[PARENT_FILES[label]["inventory"]],"receipt":entries[PARENT_FILES[label]["receipt"]]}
        routes[label]=archive.receipt()
    finally:
        archive.close()
    names={"R917":names917,"POLY":namespoly,"R873":requested873,"R827":requested827}
    sources={label:source_review(label,source_template(item,label),retained/label,names[label]) for label in SOURCES}
    for key,row in item["input_pins"].items():
        group=row["source_group"]
        assert sources[group]["files"][row["file"]]==plain(row)
        inputs[key]=dict(plain(row),source_group=group)
    inputs["row_levels"]=levels
    expanded=dict(item,sources=sources,inputs=inputs)
    inventory={"result":RESULT,"complete":True,"sources":sources,"inputs":inputs,
        "all_entries_are_unchanged_original_source_bytes":True,
        "new_mathematics_executed":False}
    save(out/SOURCE_INVENTORY,inventory)
    pack_sources(retained,sources,out/BUNDLE)
    receipt={"result":RESULT,"complete":True,"actual_configuration":expected_tag(expanded),
        "source_bundle":spec(out/BUNDLE),"source_inventory":spec(out/SOURCE_INVENTORY),
        "actual_selected_original_file_count":sum(len(s["files"]) for s in sources.values()),
        "actual_original_source_groups":list(SOURCES),"transport_routes":routes,
        "all_live_mathematical_inputs_in_selected_bundle":True,
        "old_source_arithmetic_recomputed":False,"new_mathematics_executed":False}
    save(out/INPUT_RECEIPT,receipt)
    print("R923_SOURCE_IO_COMPLETE="+json.dumps({"source_bundle":receipt["source_bundle"],
        "source_inventory":receipt["source_inventory"],
        "actual_selected_original_file_count":receipt["actual_selected_original_file_count"],
        "source_group_counts":{k:len(v["files"]) for k,v in sources.items()},
        "mathematics_executed":False},sort_keys=True),flush=True)
    return retained,sources,inputs,receipt


def stable_math(item):
    return {key:item[key] for key in (
        "result","p","core","core_sha256","helper","helper_sha256",
        "method","method_sha256","proofs","source_pins","input_pins",
        "requested_minimum_output_precision","future_target_sources")}


def restore(item,out,io_module):
    resume=item.get("resume")
    if resume is None:
        return
    assert resume["result"]==RESULT and resume["core_sha256"]==item["core_sha256"]
    folder=out.parent/"R923-resume-original-metadata"
    archive,entries=open_primary(io_module,resume,folder,out.parent/"R923-resume-transport")
    try:
        names={META[0],META[1],BUNDLE,SOURCE_INVENTORY,INPUT_RECEIPT}
        if META[2] in entries:names.add(META[2])
        extract_names(archive,entries,folder,names)
        initial,run=read(folder/META[0]),read(folder/META[1])
        assert initial["result"]==run["result"]==RESULT
        assert initial["source_commit"]==run["source_commit"]==resume["source_commit"]
        assert str(run["workflow_run_id"])==str(resume["run_id"])
        assert initial["core_sha256"]==item["core_sha256"]
        assert stable_math(initial["job"])==stable_math(item)
        assert run["process_exit_code"] in resume["accepted_process_exit_codes"]
        core=None
        if META[2] in entries:
            core=read(folder/META[2])
            assert core["result"]==RESULT and core["source_sha256"]==item["core_sha256"]
            assert run["core_receipt_sha256"]==entries[META[2]]["sha256"]
        else:
            assert run["complete"] is False and run["core_receipt_sha256"] is None
        for name in (BUNDLE,SOURCE_INVENTORY,INPUT_RECEIPT):
            if (out/name).exists():assert spec(out/name)==entries[name]
            else:shutil.copyfile(folder/name,out/name)
        unused,sources,inputs,receipt=prepare_sources(item,out,io_module,allow_download=False)
        tag=expected_tag(dict(item,sources=sources,inputs=inputs))
        assert initial["actual_configuration"]==tag
        names=sorted(n for n in entries if n.startswith(PREFIX) and n.endswith(".json.gz"))
        extract_names(archive,entries,out,names)
        for name in names:
            value=read(out/name)
            assert value["result"]==RESULT and value["configuration"]==tag
            assert value["complete"] is (name!=CURRENT)
        restored_success=False
        if FINAL in entries:
            extract_names(archive,entries,folder,[FINAL])
            final=read(folder/FINAL)
            assert final["result"]==RESULT and final["configuration"]==tag
            if final["complete"] is True:
                assert core is not None and core["complete"] is True
                assert run["complete"] is True and run["process_exit_code"]==0
                assert core["certificate_sha256"]==entries[FINAL]["sha256"]
                inventory=read(bound(out,final["stage_manifest"]))
                assert inventory["configuration"]==tag and inventory["complete"] is True
                for row in inventory["files"]:bound(out,row)
                bound(out,final["resume_state"])
                shutil.copyfile(folder/FINAL,out/FINAL)
                restored_success=True
        save(out/"resume-inheritance-receipt.json",{"result":RESULT,"complete":True,
            "source_resume":resume,"source_manifest":spec(folder/MANIFEST),
            "restored_complete_and_current_files":[entries[n] for n in names],
            "restored_true_final":restored_success,
            "false_final_not_used_as_completion_or_stale_current_SHA_constraint":True,
            "range_transport":archive.receipt(),"mathematics_reexecuted_by_wrapper":False})
    finally:
        archive.close()


def write_manifest(out):
    entries=[dict(spec(path),included_in_git=False) for path in sorted(out.iterdir())
             if path.is_file() and path.name not in (MANIFEST,REFERENCE)
             and not path.name.endswith((".tmp",".download",".partial"))]
    save(out/MANIFEST,{"result":RESULT,"files":entries,
        "temporary_active_checkpoint_retention_days":1,
        "reproducible_data_in_git_or_release":False})
    save(out/REFERENCE,{"result":RESULT,"manifest_file":MANIFEST,
        "manifest_sha256":sha(out/MANIFEST),"manifest_bytes":(out/MANIFEST).stat().st_size,
        "file_count":len(entries)})


def compute(item,out,io_module):
    out.mkdir(parents=True,exist_ok=True)
    code,error,outer_timeout,proc=1,None,False,None
    try:
        restore(item,out,io_module)
        retained,sources,inputs,receipt=prepare_sources(item,out,io_module)
        expanded=dict(item,sources={label:dict(value,directory=str((retained/label).resolve()))
                                    for label,value in sources.items()},
                      inputs=inputs,topic_directory=str(TOPIC.resolve()))
        save(out/EXPANDED,expanded)
        initial={"result":RESULT,"p":41,"source_repository":"Rogerhu12/math-research-public",
            "source_commit":os.environ["GITHUB_SHA"],"core_sha256":item["core_sha256"],
            "wrapper_sha256":sha(__file__),"request_sha256":sha(REQUEST),"job":item,
            "method_sha256":item["method_sha256"],"proofs":item["proofs"],
            "actual_configuration":expected_tag(expanded),
            "source_inventory":receipt["source_inventory"],"source_bundle":receipt["source_bundle"],
            "workflow_sha256":sha(REPO/item["workflow"]),
            "prepared_at_utc":dt.datetime.now(dt.timezone.utc).isoformat(),
            "all_new_mathematics_only_in_separate_public_Actions_core":True}
        save(out/META[0],initial)
        command=[sys.executable,str(HERE/item["core"]),"--config",str(out/EXPANDED),
                 "--out",str(out),"--budget-minutes",str(item["budget_minutes"])]
        with (out/"public-actions-run.log").open("w",encoding="utf-8") as log:
            proc=subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
            try:
                code=proc.wait(timeout=60*item["budget_minutes"]+600)
            except subprocess.TimeoutExpired:
                outer_timeout,code=True,124
                os.killpg(proc.pid,signal.SIGTERM)
                try:proc.wait(timeout=30)
                except subprocess.TimeoutExpired:
                    os.killpg(proc.pid,signal.SIGKILL);proc.wait()
                error="Actual outer timeout; complete atomic stages retained."
        with (out/"public-actions-run.log").open("r",encoding="utf-8",errors="replace") as log:
            for line in log:print(line,end="",flush=True)
    except BaseException as exc:
        traceback.print_exc()
        code=1;error=type(exc).__name__+": "+str(exc)
    finally:
        core=read(out/META[2]) if (out/META[2]).exists() else None
        complete=bool(code==0 and core and core["complete"] is True and (out/FINAL).exists())
        save(out/META[1],{"result":RESULT,"p":41,"source_commit":os.environ.get("GITHUB_SHA"),
            "workflow_run_id":os.environ.get("GITHUB_RUN_ID"),"workflow_attempt":os.environ.get("GITHUB_RUN_ATTEMPT"),
            "complete":complete,"process_exit_code":code,"outer_timeout":outer_timeout,
            "error":error,"core_receipt_sha256":sha(out/META[2]) if core else None,
            "finished_at_utc":dt.datetime.now(dt.timezone.utc).isoformat(),
            "execution_environment":"public_GitHub_Actions"})
        write_manifest(out)
    return code


def own(out,row,tag):
    value=read(bound(out,row))
    assert value["result"]==RESULT and value["configuration"]==tag and value["complete"] is True
    return value


def shape(value,dimensions):
    if not dimensions:
        assert isinstance(value,int) and not isinstance(value,bool) and 0<=value<PRIME
        return
    assert isinstance(value,list) and len(value)==dimensions[0]
    for entry in value:shape(entry,dimensions[1:])


def own_live_refs(out,value,tag):
    # Source tags contain historical nested specs. Only this new producer's live
    # filenames are interpreted as its own output references.
    if isinstance(value,dict):
        if {"file","bytes","sha256"}<=set(value) and isinstance(value["file"],str):
            name=value["file"]
            if name.startswith(PREFIX):
                referenced=read(bound(out,value))
                assert referenced["result"]==RESULT and referenced["configuration"]==tag
                assert referenced["complete"] is (name!=CURRENT)
                return
        for key,entry in value.items():
            if key!="configuration":own_live_refs(out,entry,tag)
    elif isinstance(value,list):
        for entry in value:own_live_refs(out,entry,tag)


def endpoint_review(out,ref,epsilon,tag,inputs,retained,sources):
    cert=own(out,ref,tag)
    assert cert["endpoint"]==epsilon and cert["prime"]==PRIME
    assert cert["original_zeta_root"]==ZETA and cert["original_s_root"]==SROOT
    assert cert["local_parameter"]==STRATEGY["endpoint_parameters"][epsilon]
    old=inputs["endpoints"][str(epsilon)]
    for field,sourcekey in (
        ("source_original_order_certificate","certificate"),("source_original_normal_order","normal_order"),
        ("source_original_special_fibre","special_fibre"),("source_original_primitive_and_t_frames","frame")):
        assert plain(cert[field])==plain(old[sourcekey])
    for field in ("all272_original_target_normal_coordinates_computed",
                  "all272_by8_series_original_equations_verified",
                  "complete_length8_endpoint_algebra_and_nilpotents_retained",
                  "original_basis_parameter_nu_and_dual7_frames_preserved"):
        assert cert[field] is True
    assert cert["characteristic_zero_expanded_coordinates"] is False
    assert cert["target_ideal_NormPhi_reference_or_height_evaluated"] is False
    assert cert["actual_target_w_precision"]==267
    d=cert["actual_shared_denominator_order"];T=cert["actual_target_normal_coordinate_precision"]
    assert isinstance(d,int) and 0<=d<267
    assert T==267-d and T>=tag["requested_minimum_output_precision"]
    w=own(out,cert["target_w"],tag)
    assert w["endpoint"]==epsilon and w["absolute_rho_precision"]==267
    assert w["target_w_definition"]=="Ktilde(U)/d_U_Ptilde(U)"
    for field in ("original_Ptilde8_inverse_reused","all48_coefficients_below_discriminant_order6_are_zero",
                  "basis_transport_precedes_discriminant_deflation",
                  "full_original_Ptilde_derivative_times_V_equals_Ktilde_verified","all8_coordinates_retained"):
        assert w[field] is True
    assert w["characteristic_zero_expanded_target_w"] is False
    shape(w["normal_numerator_before_deflation"],[8,273])
    shape(w["target_w_normal_coordinates_mod_prime"],[8,267])
    shape(w["discriminant_unit_part"],[267]);shape(w["discriminant_unit_inverse"],[267])
    for field,key in (("source_original_normal_order","normal_order"),
                      ("source_original_primitive_discriminant","primitive_discriminant"),
                      ("source_original_common_cleared_jets","common_cleared"),
                      ("source_original_basis_and_t_frame","frame")):
        assert plain(w[field])==plain(old[key])
    assert w["source_exact_global_P_K"]==inputs["correspondence_DAG"]
    primitive=own(out,w["source_original_adjugate"],tag)
    assert primitive["absolute_rho_precision"]==273
    assert primitive["source_primitive_order"]==plain(old["primitive"])
    assert primitive["source_original_primitive_discriminant"]==plain(old["primitive_discriminant"])
    assert primitive["actual_original_discriminant_order"]==6
    for field in ("both_adjugate_products_equal_old_primitive_discriminant",
                  "only_constant_denominators_1_through7_inverted",
                  "normal_basis_discriminant_order4_not_used_as_derivative_norm"):
        assert primitive[field] is True
    assert primitive["old_discriminant_series_recomputed"] is False
    shape(primitive["multiplication_by_original_mprime"],[8,8,273])
    shape(primitive["adjugate_matrix"],[8,8,273])
    shape(primitive["newton_coefficients_c1_through_c7"],[7,273])
    operators=own(out,cert["target_operators"],tag)
    assert operators["endpoint"]==epsilon and operators["absolute_rho_precision"]==267
    assert operators["source_target_w"]==plain(cert["target_w"])
    assert operators["complete_rank8_multiplication_operators"] is True
    assert operators["basis_or_original_parameter_replaced"] is False
    shape(operators["target_U_coordinates"],[8,267])
    shape(operators["multiplication_by_target_U"],[8,8,267])
    shape(operators["multiplication_by_target_V"],[8,8,267])
    chi=own(out,cert["target_characteristic_equation"],tag)
    assert chi["absolute_rho_precision"]==267
    assert chi["source_characteristic_relation"]==inputs["characteristic_relation"]
    assert chi["full_original_chi_U_V_equals_zero"] is True and chi["all8_series_coordinates_checked"] is True
    assert chi["new_characteristic_polynomial_computed"] is False
    shared=own(out,cert["shared_r0_adjugate"],tag)
    assert shared["absolute_rho_precision"]==267 and shared["actual_determinant_order"]==d
    assert shared["determinant_order_visible"] is True
    assert shared["determinant_valuation_lower_bound"]==d
    assert shared["both_adjugate_products_equal_determinant_identity"] is True
    assert shared["zero_truncation_is_not_exact_zero"] is True and shared["shared_by_all272_right_hand_sides"] is True
    shape(shared["multiplication_by_r0"],[8,8,267]);shape(shared["adjugate_matrix"],[8,8,267])
    shape(shared["determinant_series"],[267]);shape(shared["newton_coefficients_c1_through_c7"],[7,267])
    inverse=own(out,cert["shared_r0_unit_inverse"],tag)
    assert inverse["source_shared_adjugate"]==plain(cert["shared_r0_adjugate"])
    assert inverse["input_absolute_rho_precision"]==267 and inverse["actual_determinant_order"]==d
    assert inverse["output_absolute_rho_precision"]==T
    assert inverse["unit_product_verified"] is True and inverse["division_precedes_unit_inverse"] is True
    shape(inverse["determinant_unit_part"],[T]);shape(inverse["determinant_unit_inverse"],[T])
    position=0
    assert len(cert["complete_target_normal_coordinate_blocks"])==17
    assert len(cert["complete_cofactor_blocks"])==17
    for normalref,cofactorref in zip(cert["complete_target_normal_coordinate_blocks"],cert["complete_cofactor_blocks"]):
        normal=own(out,normalref,tag);cofactor=own(out,cofactorref,tag)
        first,stop=normal["normal_columns"]
        assert first==position and stop==min(first+16,272)
        assert normal["endpoint"]==epsilon and normal["absolute_rho_precision"]==T
        assert normal["shared_denominator_order"]==d and normal["source_complete_cofactor_block"]==plain(cofactorref)
        assert normal["source_shared_r0_adjugate"]==plain(cert["shared_r0_adjugate"])
        assert normal["source_shared_r0_unit_inverse"]==plain(cert["shared_r0_unit_inverse"])
        assert normal["source_original_normal_order"]==plain(old["normal_order"])
        assert normal["all_low_numerator_coefficients_below_shared_d_vanish"] is True
        assert normal["actual_low_coefficients_checked"]==(stop-first)*8*d
        assert normal["all_complete8_r0_times_gamma_equals_ri_equations_verified"] is True
        assert normal["gamma0_and_gamma1_checked_when_present"] is (first==0)
        assert normal["source_normal_basis_and_original_t_frame_unchanged"] is True
        assert normal["characteristic_zero_expanded_coordinates"] is False
        shape(normal["normal_values_in_original_endpoint_order_mod_prime"],[stop-first,8,T])
        assert cofactor["normal_columns"]==[first,stop] and cofactor["included_b_levels"]==[0,272]
        assert cofactor["absolute_rho_precision"]==267 and cofactor["Horner_T_is_actual_target_w"] is True
        assert cofactor["all8_coordinates_and_nilpotents_retained"] is True
        shape(cofactor["cofactor_values_normal_coordinates"],[stop-first,8,267])
        position=stop
    assert position==272
    equations=own(out,cert["all_original_normal_equations"],tag)
    assert equations["absolute_rho_precision"]==T
    assert equations["source_normal_coordinate_blocks"]==cert["complete_target_normal_coordinate_blocks"]
    assert equations["source_original_W"]==inputs["original_W"]
    for field in ("all272_original_target_equations_verified","all8_series_coordinates_of_every_equation_checked",
                  "all_factors_and_nilpotents_retained","no_characteristic_zero_coordinate_reconstruction_claimed"):
        assert equations[field] is True
    assert len(equations["source_four_original_coefficient_products"])==4
    for degree,row in enumerate(equations["source_four_original_coefficient_products"]):
        product=own(out,row,tag)
        assert product["W_power"]==degree and product["absolute_rho_precision"]==T
        assert product["all272_original_columns_used"] is True
        shape(product["products_flat_mod_prime"],[272,8*T])
    original_frame=read(bound(retained/"R917",old["frame"]))
    assert fingerprint(original_frame["configuration"])==sources["R917"]["configuration_sha256"]
    assert original_frame["both_determinant_factors_required_under_dual7"] is True
    assert original_frame["original_nu"]["iota_fixes_nu"] is True
    assert original_frame["reference_or_target_NormPhi_detU_numeric_calibration_computed"] is False
    return {"certificate":plain(ref),"target_w":plain(cert["target_w"]),
        "actual_target_w_precision":267,"actual_shared_denominator_order":d,
        "actual_target_normal_coordinate_precision":T,
        "original_frames":plain(old["frame"]),"full272_by8_original_equations_verified":True}


def verify(item,out,io_module):
    manifest=read(out/MANIFEST)
    assert manifest["result"]==RESULT
    entries={row["file"]:plain(row) for row in manifest["files"]}
    assert len(entries)==len(manifest["files"])
    for row in entries.values():bound(out,row)
    reference=read(out/REFERENCE)
    assert reference["manifest_sha256"]==sha(out/MANIFEST)
    assert reference["manifest_bytes"]==(out/MANIFEST).stat().st_size and reference["file_count"]==len(entries)
    run=read(out/META[1])
    assert run["result"]==RESULT and str(run["workflow_run_id"])==str(os.environ["GITHUB_RUN_ID"])
    assert run["source_commit"]==os.environ["GITHUB_SHA"]
    if META[0] not in entries:
        assert run["complete"] is False and run["process_exit_code"]!=0 and run["core_receipt_sha256"] is None
        print("R923_SOURCE_PREPARATION_FAILED="+json.dumps(run,sort_keys=True),flush=True)
        return 0
    initial=read(out/META[0])
    assert initial["result"]==RESULT and initial["source_commit"]==run["source_commit"]
    assert initial["core_sha256"]==item["core_sha256"] and initial["wrapper_sha256"]==item["wrapper_sha256"]
    assert stable_math(initial["job"])==stable_math(item)
    retained,sources,inputs,receipt=prepare_sources(item,out,io_module,allow_download=False)
    tag=expected_tag(dict(item,sources=sources,inputs=inputs))
    assert initial["actual_configuration"]==tag
    assert initial["source_inventory"]==receipt["source_inventory"] and initial["source_bundle"]==receipt["source_bundle"]
    core=read(out/META[2]) if META[2] in entries else None
    if core is not None:
        assert core["result"]==RESULT and core["source_sha256"]==item["core_sha256"]
        assert run["core_receipt_sha256"]==entries[META[2]]["sha256"]
        assert core["configuration_sha256"] in (None,fingerprint(tag))
        assert core["endpoint_target_NormPhi_frames_or_height_computed"] is False
    else:
        assert run["complete"] is False and run["core_receipt_sha256"] is None
    all_stages={}
    for name,row in entries.items():
        if name.startswith(PREFIX) and name.endswith(".json.gz"):
            value=read(out/name)
            assert value["result"]==RESULT and value["configuration"]==tag
            assert value["complete"] is (name!=CURRENT)
            own_live_refs(out,value,tag)
            if name not in (CURRENT,STAGES):all_stages[name]=row
    final=read(out/FINAL) if FINAL in entries else None
    endpoints={}
    if final is not None:
        assert final["result"]==RESULT and final["configuration"]==tag
        assert isinstance(final["complete"],bool)
        assert final["source_identities"]==tag["sources"]
        assert final["future_target_sources"]=={"R903":None,"R907":None}
        assert final["requested_minimum_output_precision"]==item["requested_minimum_output_precision"]
        assert final["actual_completed_endpoint_count"]==len(final["completed_endpoint_certificates"])
        assert set(final["completed_endpoint_certificates"])<={"0","1"}
        for key in ("original_R917_orders_and_frames_recomputed",
                    "original_W_charpoly_adjugate_273nodes_or_2058_solve_recomputed",
                    "characteristic_zero_expanded_target_coordinates","five_target_endpoint_ideal_lattices_computed",
                    "P0_endpoint_numeric_Norm_calibration_computed","P1_endpoint_numeric_Norm_calibration_computed",
                    "NmPhi_detU_and_reference_original_frames_evaluated","Hecke_Picard_active_support_or_height_computed"):
            assert final[key] is False
        if core is not None:assert core["certificate_sha256"]==entries[FINAL]["sha256"]
        for epsilon,ref in final["completed_endpoint_certificates"].items():
            endpoints[epsilon]=endpoint_review(out,ref,int(epsilon),tag,inputs,retained,sources)
    if not run["complete"]:
        assert run["process_exit_code"]!=0 and (final is None or final["complete"] is False)
        if final is not None:
            assert final["actual_original_two_endpoint_target_normal_coordinates_certified"] is False
            assert final["actual_full_length8_endpoint_algebras_preserved"] is False
        print("R923_INCOMPLETE_IO_REVIEW="+json.dumps({"result":RESULT,
            "actual_complete_math_stages":len(all_stages),"core_receipt_present":core is not None,
            "actual_process_exit_code":run["process_exit_code"],
            "actual_stop":core.get("error") if core else run.get("error"),
            "actual_completed_endpoint_count":len(endpoints),"completed_endpoints":endpoints,
            "original_source_files":receipt["actual_selected_original_file_count"],
            "mathematics_reexecuted":False},sort_keys=True),flush=True)
        return 0
    assert run["process_exit_code"]==0 and core is not None and core["complete"] is True
    assert core["configuration_sha256"]==fingerprint(tag)
    assert final is not None and final["complete"] is True and final["stop_reason"] is None
    assert final["prime"]==PRIME and final["original_zeta_root"]==ZETA and final["original_s_root"]==SROOT
    assert core["actual_original_two_endpoint_target_normal_coordinates_certified"] is True
    assert final["actual_completed_endpoint_count"]==core["actual_completed_endpoint_count"]==2
    assert final["actual_original_two_endpoint_target_normal_coordinates_certified"] is True
    assert final["actual_full_length8_endpoint_algebras_preserved"] is True
    assert set(endpoints)=={"0","1"} and final["endpoint_stops"]=={}
    inventory=own(out,final["stage_manifest"],tag)
    assert {row["file"]:plain(row) for row in inventory["files"]}==all_stages
    assert inventory["only_actual_complete_stages_listed"] is True and inventory["current_checkpoint_excluded"] is True
    assert plain(final["resume_state"])["file"]==CURRENT
    current=read(bound(out,final["resume_state"]))
    assert current["configuration"]==tag and current["complete"] is False
    assert current["completed_endpoint_certificates"]==final["completed_endpoint_certificates"]
    audit=own(out,final["source_audit"],tag)
    assert audit["source_identities"]==tag["sources"] and audit["inputs"]==inputs
    assert audit["actual_selected_original_file_count"]==receipt["actual_selected_original_file_count"]
    assert audit["old_order_273_jets_and_polynomial_row_recomputed"] is False
    assert audit["original_W_four_blocks_reused"] is True
    print("R923_COMPLETE_IO_REVIEW="+json.dumps({"result":RESULT,"certificate":entries[FINAL],
        "stage_manifest":final["stage_manifest"],"actual_complete_math_stages":len(all_stages),
        "actual_original_source_files":receipt["actual_selected_original_file_count"],
        "endpoints":endpoints,"actual_target_NormPhi_endpoint_frames_computed":False,
        "mathematics_reexecuted_by_wrapper":False,"seconds":final["seconds"]},sort_keys=True),flush=True)
    return 0


def main():
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--verify",action="store_true")
    args=parser.parse_args()
    item=read(REQUEST)
    io_module=guard(item)
    return verify(item,args.output,io_module) if args.verify else compute(item,args.output,io_module)


if __name__=="__main__":
    raise SystemExit(main())
