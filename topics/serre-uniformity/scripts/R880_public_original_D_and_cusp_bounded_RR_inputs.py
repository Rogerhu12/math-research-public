#!/usr/bin/env python3
"""R880 standard-library intake transport, resume and output verification.
The original six sources are read byte for byte. No mathematical module is imported.
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

S=Path(__file__).resolve().parent
REPO=S.parents[2]
TOPIC=REPO/"topics/serre-uniformity"
REQUEST=TOPIC/"notes/R880-D-cusp-bounded-RR-public-request.json"
RESULT="R880-original-D-and-cusp-bounded-RR-inputs"
FINAL="p41-original-D-and-cusp-bounded-RR-inputs-certificate.json"
PREFIX="R880-"
MANIFEST="full-outputs-manifest.json"
REFERENCE="full-outputs-manifest-reference.json"
INVENTORY=PREFIX+"original-source-inventory.json"
RETAINED_RECEIPT=PREFIX+"retained-inputs-receipt.json"
BASE=("result","run_id","source_commit","core_sha256","manifest_sha256")
SOURCES=("R845","R872","R827","R820","R842","R849")
PROOFS=("R880","R872","R845")
EPS=[0]+[1]*144+[2]*127
PRIME,RANK=1000000753,272
ROOT_ZETA,ROOT_S,ROOT_B=549966761,99932770,3197390
IO_HELPER_SHA="c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
META=("public-actions-input.json","run-receipt.json","core-receipt.json")
INPUTS = (
    "old_rank","old_sections","old_normal_index","old_alias_audit","old_pole_DAG",
    "D_basis","D_matrix","point_jets","point_linearization","V2_jets",
    "chi_divisor","chi_kernel","chi_anchor","cusp_reduction","place_audit",
    "W_reduction","global_DAG")
STRATEGY = {
    "scope":"original_D_bounded_representative_and_complete_common_cusp_space",
    "prime":PRIME,"original_branch":0,
    "original_integral_B_root":ROOT_B,"original_s_root":ROOT_S,
    "original_zeta_root":ROOT_ZETA,
    "field":"original L=Q(b,zeta); fixed cusp and chi inputs first over K",
    "normal_basis_degrees":EPS,"normal_integer_scale_applied_again":False,
    "old_fiber_nodes":[0,1,2,3,4],"old_product_matrix_shape":[1360,1380],
    "old_pencil_rank":1111,"old_complete_relation_dimension":269,
    "old_rank_selection_recomputed":False,"old_products_recomputed":False,
    "old_selected_inverse_was_not_saved":True,
    "P0_section_selection":"old a if its actual value is a unit, else old b if unit",
    "point_jet_orders_required":[0,251],
    "V3_jet_matrix_shape":[252,690],"old_V2_jet_columns_copied":418,
    "new_highest_normal_z_power_columns":272,
    "residual_jet_matrix_shape":[123,269],"standardizing_space_dimension":146,
    "standardizing_section_selection":"first unit order123 coefficient, no rescaling",
    "fixed_v_fiber_products_shared_across_trials":True,
    "second_anchor_schedule":"sum(integer_parameter^j * exact_U_j), j=0..145",
    "new_pencil_required_rank":962,"complete_Dstar_dimension":418,
    "common_cusp_constraint_shape":[272,690],
    "common_cusp_rows":20,"common_P0_jet_rows":252,
    "complete_common_cusp_dimension":418,
    "C_quotient_is_a_module_map_not_asserted_a_ring_homomorphism":True,
    "old_Krylov_inverses_normal_conversion_and_P0_jets_recomputed":False,
    "no_sixth_fiber_or_full_polynomial_multiplier_required":True,
    "exact_objects":"original source-bound unit-solve expressions",
    "characteristic_zero_coefficients_reconstructed":False,
    "principal_function":"(a_star/v)^3/(u_chi/tau^2)^4",
    "principal_function_P0_order":-1457,
    "original_five_Lj_RR128_or_144_computed":False,
    "only_budget_trial_limit_and_transport_excluded_from_identity":True,
}
def sha(path):
    value=hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda:stream.read(4*1024*1024),b""):
            value.update(block)
    return value.hexdigest()

def fingerprint(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def read(path):
    path=Path(path)
    with (gzip.open(path,"rt",encoding="utf-8") if path.suffix==".gz" else path.open("r",encoding="utf-8")) as stream:
        return json.load(stream)

def save(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_name(path.name+".tmp")
    temporary.write_text(json.dumps(value,sort_keys=True,separators=(",",":"))+"\n",encoding="utf-8")
    temporary.replace(path)

def safe_name(name):
    assert isinstance(name,str) and Path(name).name==name and name not in (".","..") and "\\" not in name
    return name

def plain(value):
    result={key:value[key] for key in ("file","bytes","sha256")}
    safe_name(result["file"])
    assert isinstance(result["bytes"],int) and result["bytes"]>=0
    assert re.fullmatch(r"[0-9a-f]{64}",result["sha256"])
    return result

def spec(path):
    path=Path(path)
    return {"file":path.name,"bytes":path.stat().st_size,"sha256":sha(path)}

def bound(folder,value):
    value=plain(value);path=Path(folder)/value["file"]
    assert spec(path)==value,path.name
    return path

def topic_path(name):
    relative=PurePosixPath(name)
    assert not relative.is_absolute() and ".." not in relative.parts
    path=(TOPIC/str(relative)).resolve()
    assert path.is_relative_to(TOPIC.resolve())
    return path
def identity(value):
    return {key:value[key] for key in BASE}

def stable_source(value):
    return {**identity(value),
        "certificate":plain(value["certificate"]) if value.get("certificate") else None,
        "configuration_stage":plain(value["configuration_stage"]) if value.get("configuration_stage") else None,
        "configuration_sha256":value["configuration_sha256"],
        "selected_file_count":value["selected_file_count"],
        "selected_files_sha256":value["selected_files_sha256"]}

def expected_tag(item):
    return {
        "result":RESULT,"source_sha256":item["core_sha256"],"p":41,"python_flint":"0.9.0",
        "method_sha256":item["method_sha256"],
        "proofs_sha256":{key:item["proofs"][key]["sha256"] for key in PROOFS},
        "sources":{label:stable_source(item["sources"][label]) for label in SOURCES},
        "inputs":item["inputs"],"strategy":STRATEGY,
    }

def load_IO(item):
    path=S/"R824_public_original_global_polar_generators.py"
    assert item["io_helper"]==path.name
    assert item["io_helper_sha256"]==sha(path)==IO_HELPER_SHA
    module_spec=importlib.util.spec_from_file_location("R880_frozen_original_IO",path)
    module=importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    return module

def guard(item,request):
    assert os.environ.get("GITHUB_ACTIONS")=="true"
    assert os.environ.get("GITHUB_REPOSITORY")=="Rogerhu12/math-research-public"
    assert request.resolve()==REQUEST.resolve()
    assert item["schema"]==1 and item["result"]==RESULT and item["p"]==41
    assert item["producer_inputs_pending"] is False
    assert item["wrapper"]==Path(__file__).name and sha(__file__)==item["wrapper_sha256"]
    assert item["core"]=="R880_original_D_and_cusp_bounded_RR_inputs.py"
    assert sha(S/item["core"])==item["core_sha256"]
    assert sha(topic_path(item["method"]))==item["method_sha256"]
    assert set(item["proofs"])==set(PROOFS)
    for proof in item["proofs"].values():
        assert sha(topic_path(proof["path"]))==proof["sha256"]
    assert sha(REPO/"README.md")==item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md")==item["readme_sha256"]["topic"]
    assert isinstance(item["session"],str) and item["session"]
    assert set(item["sources"])==set(SOURCES)
    assert item["budget_minutes"]>0 and item["budget_minutes"]<=300
    assert item["resume"] is None or isinstance(item["resume"],dict)
    return load_IO(item)

def output_manifest(out):
    rows=[]
    for path in sorted(out.iterdir()):
        if not path.is_file() or path.name in (MANIFEST,REFERENCE) or path.name.endswith(".tmp"):
            continue
        rows.append({**spec(path),"included_in_git":False})
    save(out/MANIFEST,{"result":RESULT,"files":rows,"temporary_active_checkpoint_retention_days":1,
        "reproducible_data_in_git_or_release":False})
    save(out/REFERENCE,{"result":RESULT,**spec(out/MANIFEST)})

def inspect_manifest(out):
    manifest=read(out/MANIFEST)
    assert manifest["result"]==RESULT
    files={entry["file"]:plain(entry) for entry in manifest["files"]}
    assert len(files)==len(manifest["files"])
    actual={p.name for p in out.iterdir() if p.is_file() and p.name not in (MANIFEST,REFERENCE)
        and not p.name.endswith(".tmp")}
    assert actual==set(files)
    for ref in files.values():
        bound(out,ref)
    ref=read(out/REFERENCE)
    assert ref["result"]==RESULT and plain(ref)==spec(out/MANIFEST)
    return files

def intake_from_archive(item,out,work,IO):
    intake=item["intake"]
    archive=IO.Archive(intake,work/"intake-transport",whole=True)
    try:
        index_spec=plain(intake["source_index"])
        archive.extract_bound(index_spec["file"],index_spec["sha256"],out/index_spec["file"],index_spec["bytes"])
        index=read(out/index_spec["file"])
        assert index["schema"]==1 and index["new_mathematics_executed"] is False and index["errors"]==[]
        assert str(index["workflow_run_id"])==str(intake["run_id"])
        assert index["source_commit"]==intake["source_commit"]
        assert index["request_sha256"]==intake["request_sha256"]
        entries={v["label"]:v for v in index["sources"]}
        assert len(entries)==len(index["sources"])==6 and set(entries)==set(SOURCES)
        wanted={index_spec["file"]}
        for label in SOURCES:
            entry=entries[label]
            for kind in ("summary","retained_input_bundle"):
                ref=plain(entry[kind])
                archive.extract_bound(ref["file"],ref["sha256"],out/ref["file"],ref["bytes"])
                wanted.add(ref["file"])
            assert plain(entry["retained_input_bundle"])==plain(intake["bundles"][label])
        assert set(archive.by_name)==wanted
        return archive.receipt()
    finally:
        archive.close()


def unpack_source(bundle,directory,files):
    directory.mkdir(parents=True,exist_ok=True)
    seen=set()
    with tarfile.open(bundle,"r|gz") as tar:
        for member in tar:
            name=PurePosixPath(member.name)
            assert member.isfile() and len(name.parts)==2 and name.parts[0]=="original"
            assert "\\" not in member.name and ".." not in name.parts and not name.is_absolute()
            basename=safe_name(name.name)
            assert basename in files and basename not in seen
            seen.add(basename)
            ref=files[basename]
            assert member.size==ref["bytes"]
            stream=tar.extractfile(member)
            assert stream is not None
            path=directory/basename
            temporary=path.with_name(path.name+".tmp")
            digest=hashlib.sha256();count=0
            if path.exists():
                assert spec(path)==ref
                for block in iter(lambda:stream.read(4*1024*1024),b""):
                    digest.update(block);count+=len(block)
            else:
                with temporary.open("wb") as target:
                    for block in iter(lambda:stream.read(4*1024*1024),b""):
                        target.write(block);digest.update(block);count+=len(block)
                assert count==ref["bytes"] and digest.hexdigest()==ref["sha256"],basename
                temporary.replace(path)
            assert count==ref["bytes"] and digest.hexdigest()==ref["sha256"],basename
    assert seen==set(files)

def review_original(label,value):
    folder=Path(value["directory"]);files=value["files"]
    for entry in files.values():
        bound(folder,entry)
    manifest=read(folder/MANIFEST)
    assert manifest["result"]==value["result"]
    original={row["file"]:plain(row) for row in manifest["files"]}
    assert len(original)==value["manifest_file_count"]
    assert files[MANIFEST]["sha256"]==value["manifest_sha256"]
    for name,entry in files.items():
        if name not in (MANIFEST,REFERENCE):
            assert original[name]==entry
    reference=read(folder/REFERENCE)
    if "manifest" in reference:
        assert plain(reference["manifest"])==files[MANIFEST]
    elif all(k in reference for k in ("file","bytes","sha256")):
        assert plain(reference)==files[MANIFEST]
    else:
        assert reference["manifest_sha256"]==value["manifest_sha256"]
        assert reference["manifest_bytes"]==files[MANIFEST]["bytes"]
    initial,run=(read(folder/name) for name in META[:2])
    assert initial["result"]==run["result"]==value["result"]
    assert initial["source_commit"]==run["source_commit"]==value["source_commit"]
    assert str(run["workflow_run_id"])==str(value["run_id"])
    assert initial["core_sha256"]==value["core_sha256"]
    assert initial.get("driver_sha256",initial.get("wrapper_sha256"))==value["wrapper_sha256"]
    if value.get("certificate"):
        cert=read(bound(folder,value["certificate"]))
        assert cert["result"]==value["result"] and cert["complete"] is True
        assert run["complete"] is True and run["process_exit_code"]==0 and run["error"] is None
        tag=cert["configuration"]
    else:
        assert label=="R827" and run["complete"] is False
        assert run["process_exit_code"] in value["accepted_checkpoint_exit_codes"]
        assert 0 not in value["accepted_checkpoint_exit_codes"]
        anchor=read(bound(folder,value["configuration_stage"]))
        assert anchor["complete"] is True
        tag=anchor["configuration"]
    assert tag["result"]==value["result"] and tag["source_sha256"]==value["core_sha256"]
    if value.get("configuration_sha256") is None:
        assert value["derive_configuration_from_pinned_original_stage"] is True
        value["configuration_sha256"]=fingerprint(tag)
    else:
        assert fingerprint(tag)==value["configuration_sha256"]
    if run.get("core_receipt_sha256") is not None:
        assert files[META[2]]["sha256"]==run["core_receipt_sha256"]
        core=read(folder/META[2])
        assert core["result"]==value["result"] and core["source_sha256"]==value["core_sha256"]
        if value.get("certificate"):
            assert core["complete"] is True
            if "certificate_sha256" in core:
                assert core["certificate_sha256"]==value["certificate"]["sha256"]
        else:
            assert core["complete"] is False
    else:
        assert not value.get("certificate")
    return tag


def prepare_sources(item,out,work):
    intake=item["intake"]
    index=read(bound(out,intake["source_index"]))
    assert index["schema"]==1 and index["new_mathematics_executed"] is False and index["errors"]==[]
    assert str(index["workflow_run_id"])==str(intake["run_id"])
    assert index["source_commit"]==intake["source_commit"]
    assert index["request_sha256"]==intake["request_sha256"]
    entries={entry["label"]:entry for entry in index["sources"]}
    assert set(entries)==set(SOURCES) and len(entries)==len(index["sources"])==6
    sources={};total=0;tags={}
    for label in SOURCES:
        raw=item["sources"][label];entry=entries[label]
        for key in ("run_id","source_commit","core_sha256","manifest_sha256"):
            assert str(entry["source"][key])==str(raw[key])
        summary=read(bound(out,entry["summary"]))
        assert summary["label"]==label and summary["original_result"]==raw["result"]
        assert summary["new_mathematics_executed"] is False
        assert summary["source"]==entry["source"]
        assert summary["manifest"]["sha256"]==raw["manifest_sha256"]
        assert summary["original_manifest_count"]==raw["manifest_file_count"]
        assert summary["source_core_sha256"]==raw["core_sha256"]
        assert summary["source_wrapper_sha256"]==raw["wrapper_sha256"]
        bundle_spec=plain(entry["retained_input_bundle"])
        assert bundle_spec==plain(summary["retained_input_bundle"])==plain(intake["bundles"][label])
        files={name:plain(v) for name,v in summary["selected_files"].items()}
        assert len(files)==summary["selected_file_count"]==raw["selected_math_and_metadata_count"]
        files[MANIFEST]=plain(summary["manifest"])
        files[REFERENCE]=plain(summary["manifest_reference"])
        assert len(files)==raw["expected_selected_file_count"]
        for name,pinned in raw["file_pins"].items():
            assert files[name]==plain(pinned)
        directory=work/"retained"/label
        unpack_source(bound(out,bundle_spec),directory,files)
        certificate=files[raw["certificate_name"]] if raw["certificate_name"] else None
        anchor=files[raw["configuration_stage_name"]] if raw["configuration_stage_name"] else None
        value=dict(raw,directory=str(directory),files=files,
            certificate=certificate,configuration_stage=anchor,
            selected_file_count=len(files),selected_files_sha256=fingerprint(files))
        tags[label]=review_original(label,value)
        sources[label]=value;total+=len(files)
    assert total==944
    inputs={}
    for key,selector in item["input_selectors"].items():
        label,name=selector["source_group"],selector["file"]
        assert label in sources and name in sources[label]["files"]
        inputs[key]={"source_group":label,**sources[label]["files"][name]}
        for field in ("sha256","bytes"):
            if field in selector:
                assert inputs[key][field]==selector[field]
    assert set(inputs)==set(INPUTS)
    def source_stage(key):
        entry=inputs[key];label=entry["source_group"]
        value=read(bound(sources[label]["directory"],entry))
        assert value["complete"] is True and value["configuration"]==tags[label]
        if "result" in value:
            assert value["result"]==sources[label]["result"]
        return value
    place=source_stage("place_audit")
    assert place["prime"]==PRIME and place["original_branch"]==0
    assert place["canonical_free_column"]==1186
    assert place["original_integral_B_root"]==ROOT_B and place["original_b_root"]==637573097
    assert place["original_zeta_root"]==ROOT_ZETA and place["original_s_root"]==ROOT_S
    for label in ("R845","R872","R842"):
        assert identity(tags[label]["sources"]["R827"])==identity(sources["R827"])
    assert identity(tags["R849"]["source_identities"]["R845"])==identity(sources["R845"])
    assert identity(tags["R827"]["source_identities"]["R820"])==identity(sources["R820"])
    normal=source_stage("old_normal_index")
    assert len(normal["blocks"])==23 and normal["dimension"]==690
    for entry in normal["blocks"]:
        assert sources["R845"]["files"][entry["file"]]==plain(entry)
    point_jets=source_stage("point_jets")
    assert len(point_jets["orders"])==273
    for entry in point_jets["orders"]:
        assert sources["R872"]["files"][entry["file"]]==plain(entry)
    cusp=source_stage("cusp_reduction")
    for chart in ("tau","sigma"):
        entry=cusp["source_R820_indexes"][chart]
        assert sources["R820"]["files"][entry["file"]]==plain(entry)
        index=read(bound(sources["R820"]["directory"],entry))
        assert index["configuration"]==tags["R820"] and index["complete"] is True
        originals=cusp["charts"][chart]["original_column_sources"]
        assert len(originals)==272
        assert [plain(x) for x in originals]==[plain(x) for x in index["Hermite_columns_in_original_basis_order"]]
        for entry in originals:
            assert sources["R820"]["files"][entry["file"]]==plain(entry)
    expanded=dict(item,sources=sources,inputs=inputs)
    expanded["method"]=str(topic_path(item["method"]))
    expanded["proofs"]={key:{**value,"path":str(topic_path(value["path"]))}
                        for key,value in item["proofs"].items()}
    inventory={"result":RESULT,"source_identities":{label:stable_source(value) for label,value in sources.items()},
        "selected_files":{label:value["files"] for label,value in sources.items()},
        "actual_selected_source_count":total}
    receipt={"result":RESULT,"complete":True,"intake":item["intake"],
        "source_index":plain(intake["source_index"]),
        "summaries":{label:plain(entries[label]["summary"]) for label in SOURCES},
        "original_carriers":{label:plain(entries[label]["retained_input_bundle"]) for label in SOURCES},
        "original_source_identities":{label:stable_source(value) for label,value in sources.items()},
        "actual_selected_source_count":total,
        "all_selected_original_members_bytes_and_SHA_verified":True,
        "all544_original_C_columns_and273_original_jets_bound":True,
        "R845_R872_original_K_and_L_place_identity_verified":True,
        "new_mathematics_executed":False}
    save(out/INVENTORY,inventory);save(out/RETAINED_RECEIPT,receipt)
    return expanded,receipt

def restore_archive(item,out,work,IO):
    source=item["resume"]
    if source is None:
        return None
    assert source["result"]==RESULT and source["core_sha256"]==item["core_sha256"]
    assert source["wrapper_sha256"]==item["wrapper_sha256"]
    archive=IO.Archive(source,work/"resume-transport",whole=True)
    folder=work/"previous-output";folder.mkdir(parents=True,exist_ok=True)
    try:
        manifest_spec=plain(source["manifest"])
        archive.extract_bound(MANIFEST,manifest_spec["sha256"],folder/MANIFEST,manifest_spec["bytes"])
        manifest=read(folder/MANIFEST)
        assert manifest["result"]==RESULT
        files={v["file"]:plain(v) for v in manifest["files"]}
        assert len(files)==len(manifest["files"])
        assert set(archive.by_name)==set(files)|{MANIFEST,REFERENCE}
        for ref in files.values():
            archive.extract_bound(ref["file"],ref["sha256"],folder/ref["file"],ref["bytes"])
        ref_info=archive.by_name[REFERENCE]
        assert len(ref_info)==1 and ref_info[0].file_size<1000000
        (folder/REFERENCE).write_bytes(archive.zip.read(ref_info[0]))
        reference=read(folder/REFERENCE)
        assert reference["result"]==RESULT and plain(reference)==manifest_spec
        old=read(folder/META[0]);run=read(folder/META[1])
        assert old["result"]==run["result"]==RESULT
        assert old["source_commit"]==run["source_commit"]==source["source_commit"]
        assert old["core_sha256"]==item["core_sha256"] and old["driver_sha256"]==item["wrapper_sha256"]
        assert str(run["workflow_run_id"])==str(source["run_id"])
        if run.get("core_receipt_sha256") is not None:
            assert files[META[2]]["sha256"]==run["core_receipt_sha256"]
            cr=read(folder/META[2])
            assert cr["source_sha256"]==item["core_sha256"] and cr["result"]==RESULT
        else:
            assert run["complete"] is False
        index=read(bound(folder,item["intake"]["source_index"]))
        needed=[plain(item["intake"]["source_index"])]
        for entry in index["sources"]:
            needed.extend([plain(entry["summary"]),plain(entry["retained_input_bundle"])])
        for ref in needed:
            assert files[ref["file"]]==ref
            target=out/ref["file"]
            if target.exists():
                assert spec(target)==ref
            else:
                shutil.copyfile(bound(folder,ref),target)
        return {"folder":folder,"files":files,"initial":old,"run":run,"transport":archive.receipt()}
    finally:
        archive.close()

def restore_stages(previous,tag,out):
    if previous is None:
        return
    assert previous["initial"]["actual_configuration"]==tag
    folder,files=previous["folder"],previous["files"]
    for name,ref in files.items():
        if not (name.startswith(PREFIX) and name.endswith(".json.gz")):
            continue
        value=read(folder/name)
        assert value["result"]==RESULT and value["configuration"]==tag
        if name==PREFIX+"current.json.gz":
            assert value["complete"] is False
        else:
            assert value["complete"] is True
        target=out/name
        if target.exists():
            assert spec(target)==ref
        else:
            shutil.copyfile(folder/name,target)
    if FINAL in files:
        final=read(folder/FINAL)
        assert final["result"]==RESULT and final["configuration"]==tag
        if final["complete"] is True:
            assert previous["run"]["complete"] is True
            inventory=read(bound(folder,final["stage_manifest"]))
            assert inventory["result"]==RESULT and inventory["configuration"]==tag and inventory["complete"] is True
            for ref in inventory["files"]:
                assert files[ref["file"]]==plain(ref)
                bound(out,ref)
            for key in ("source_audit","original_V3_point_jets","complete_common_cusp_418_kernel",
                        "complete_residual_F_269_space","complete_standardizing_146_space","fixed_v",
                        "accepted_new_pencil_profile","complete_Dstar_418_kernel",
                        "original_D_cusp_chi_principal_inputs","resume_state"):
                bound(out,final[key])
            shutil.copyfile(folder/FINAL,out/FINAL)
        # An old false FINAL is a historical receipt, not the restored completion state.

def compute(item,out,request,IO):
    out.mkdir(parents=True,exist_ok=True)
    work=out.parent/"R880-working";work.mkdir(parents=True,exist_ok=True)
    code=1;error=None;outer=False;expanded=None;tag=None;child=None;transport=None
    try:
        previous=restore_archive(item,out,work,IO)
        transport=previous["transport"] if previous is not None else intake_from_archive(item,out,work,IO)
        expanded,source_receipt=prepare_sources(item,out,work)
        tag=expected_tag(expanded)
        restore_stages(previous,tag,out)
        config=work/"expanded-job.json";save(config,expanded)
        initial={"result":RESULT,"source_commit":os.environ["GITHUB_SHA"],
            "workflow_run_id":os.environ["GITHUB_RUN_ID"],"workflow_attempt":os.environ.get("GITHUB_RUN_ATTEMPT","1"),
            "core_sha256":item["core_sha256"],"driver_sha256":item["wrapper_sha256"],
            "request_sha256":sha(request),"job":item,"actual_configuration":tag,
            "actual_source_inventory":spec(out/INVENTORY),"retained_inputs":spec(out/RETAINED_RECEIPT),
            "transport":transport,"root_readme_sha256":item["readme_sha256"]["root"],
            "topic_readme_sha256":item["readme_sha256"]["topic"],
            "execution_environment":"public-repository-github-actions"}
        save(out/META[0],initial)
        command=[sys.executable,"-u",str(S/item["core"]),"--config",str(config),
            "--out",str(out),"--budget-minutes",str(item["budget_minutes"])]
        with (out/"core.log").open("ab",buffering=0) as log:
            child=subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
            try:
                code=child.wait(timeout=60*item["budget_minutes"]+180)
            except subprocess.TimeoutExpired:
                outer=True;code=124
                os.killpg(child.pid,signal.SIGTERM)
                try:
                    child.wait(timeout=15)
                except subprocess.TimeoutExpired:
                    os.killpg(child.pid,signal.SIGKILL);child.wait()
        if code<0:
            code=128-code
        if (out/"core.log").exists():
            for line in (out/"core.log").read_text(errors="replace").splitlines()[-18:]:
                if len(line)<=2000:
                    print(line,flush=True)
        if (out/META[2]).exists():
            cr=read(out/META[2])
            print("R880_CORE_RECEIPT="+json.dumps({k:v for k,v in cr.items()
                if k!="configuration"},sort_keys=True),flush=True)
    except BaseException as exc:
        traceback.print_exc()
        error={"type":type(exc).__name__,"message":str(exc)}
        code=1
    finally:
        core=read(out/META[2]) if (out/META[2]).exists() else None
        final=read(out/FINAL) if (out/FINAL).exists() else None
        complete=bool(code==0 and core and core["complete"] and final and final["complete"])
        save(out/META[1],{"result":RESULT,"p":41,"complete":complete,
            "process_exit_code":code,"error":error,"outer_timeout":outer,
            "source_commit":os.environ["GITHUB_SHA"],"workflow_run_id":os.environ["GITHUB_RUN_ID"],
            "workflow_attempt":os.environ.get("GITHUB_RUN_ATTEMPT","1"),
            "core_receipt_sha256":sha(out/META[2]) if core is not None else None,
            "actual_complete_common_cusp_418_space_certified":bool(final and final["actual_complete_common_cusp_418_space_certified"]),
            "actual_complete_Dstar_418_space_certified":bool(final and final["actual_complete_Dstar_418_space_certified"]),
            "actual_original_Qf_principal_identity_certified":bool(final and final["actual_original_Qf_principal_identity_certified"]),
            "original_five_Lj_RR128_or_144_computed":False,
            "finished_at_utc":dt.datetime.now(dt.timezone.utc).isoformat()})
        output_manifest(out)
    return code



def dimensions(value,height,width):
    assert isinstance(value,list) and len(value)==height
    assert all(isinstance(row,list) and len(row)==width for row in value)

def verify(item,out,request,IO):
    files=inspect_manifest(out)
    run=read(out/META[1])
    assert run["result"]==RESULT and run["source_commit"]==os.environ["GITHUB_SHA"]
    if META[0] not in files:
        assert run["complete"] is False and run["process_exit_code"]!=0
        assert run["core_receipt_sha256"] is None
        print("R880_VERIFY="+json.dumps({"complete":False,"source_preparation_failed":True,
            "all_existing_output_bytes_verified":True,"new_mathematics_executed":False}),flush=True)
        return 0
    expanded,source_receipt=prepare_sources(item,out,out.parent/"R880-verification")
    tag=expected_tag(expanded)
    initial=read(out/META[0])
    assert initial["result"]==RESULT and initial["source_commit"]==os.environ["GITHUB_SHA"]
    assert initial["core_sha256"]==item["core_sha256"] and initial["driver_sha256"]==item["wrapper_sha256"]
    assert initial["request_sha256"]==sha(request) and initial["job"]==item
    assert initial["actual_configuration"]==tag
    assert initial["actual_source_inventory"]==files[INVENTORY]==spec(out/INVENTORY)
    assert initial["retained_inputs"]==files[RETAINED_RECEIPT]==spec(out/RETAINED_RECEIPT)
    inventory_name=PREFIX+"exact-stages-manifest.json.gz"
    current_name=PREFIX+"current.json.gz"
    complete_stages={}
    def external(ref):
        label=ref["source_group"];assert label in expanded["sources"]
        source=expanded["sources"][label]
        assert source["files"][ref["file"]]==plain(ref)
        bound(source["directory"],ref)
    def check_references(value):
        if isinstance(value,dict):
            if all(k in value for k in ("file","bytes","sha256")):
                ref=plain(value)
                if "source_group" in value:
                    external(value)
                elif ref["file"] in files and files[ref["file"]]==ref:
                    bound(out,ref)
                else:
                    matches=[source for source in expanded["sources"].values()
                             if source["files"].get(ref["file"])==ref]
                    assert matches,ref["file"]
                    bound(matches[0]["directory"],ref)
                return
            for key,child in value.items():
                if key=="configuration" or key.endswith("_mod_prime"):
                    continue
                if isinstance(child,dict):
                    check_references(child)
                elif isinstance(child,list):
                    for entry in child:
                        if isinstance(entry,dict):
                            check_references(entry)
        elif isinstance(value,list):
            for entry in value:
                if isinstance(entry,dict):
                    check_references(entry)
    for name,ref in files.items():
        if not(name.startswith(PREFIX) and name.endswith(".json.gz")):
            continue
        value=read(out/name)
        assert value["result"]==RESULT and value["configuration"]==tag
        if name==current_name:
            assert value["complete"] is False and isinstance(value["stage"],str)
        else:
            assert value["complete"] is True
            if name!=inventory_name:
                complete_stages[name]=ref
                check_references(value)
                if value.get("accepted") is True and "inverse_mod_prime" in value:
                    n=len(value["selected_rows"])
                    dimensions(value["inverse_mod_prime"],n,n)
                    assert value["both_inverse_products_verified"] is True
                if "kernel_basis_mod_prime" in value:
                    if "matrix_shape" in value:
                        _,width=value["matrix_shape"]
                        dim=value["actual_kernel_dimension"]
                        dimensions(value["kernel_basis_mod_prime"],width,dim)
                    assert value.get("all_original_equations_verified",
                                     value.get("all_original_fiber_equations_verified")) is True
                    assert value["free_normalization_identity_verified"] is True
                    assert value["full_characteristic_zero_kernel_certified"] is True
                if "product_evaluation_matrix_mod_prime" in value:
                    dimensions(value["product_evaluation_matrix_mod_prime"],272,690)
                    assert value["old_Krylov_inverse_and_original_V3_evaluation_not_recomputed"] is True
                    assert value["no_full_polynomial_multiplier_or_sixth_fiber_computed"] is True
                if value.get("accepted") is True and "original_V3_basis_mod_prime" in value:
                    dim=value.get("actual_projected_rank",value.get("dimension"))
                    dimensions(value["original_V3_basis_mod_prime"],690,dim)
                    dimensions(value["normal_V3_basis_mod_prime"],690,dim)
    def stage(ref):
        ref=plain(ref);assert files[ref["file"]]==ref
        value=read(bound(out,ref))
        assert value["result"]==RESULT and value["configuration"]==tag and value["complete"] is True
        return value
    core=read(out/META[2]) if META[2] in files else None
    if core is not None:
        assert core["result"]==RESULT and core["source_sha256"]==item["core_sha256"]
        assert files[META[2]]["sha256"]==run["core_receipt_sha256"]
        if core["configuration_sha256"] is not None:
            assert core["configuration_sha256"]==fingerprint(tag)
    else:
        assert run["complete"] is False and run["core_receipt_sha256"] is None
    final=read(out/FINAL) if FINAL in files else None
    if final is not None:
        assert final["result"]==RESULT and final["configuration"]==tag
        assert final["prime"]==PRIME and final["original_branch"]==0
        assert final["original_integral_B_root"]==ROOT_B
        assert final["original_zeta_root"]==ROOT_ZETA and final["original_s_root"]==ROOT_S
        for key in ("characteristic_zero_RR_coefficients_reconstructed",
                    "old_products_normal_conversion_Hensel_jets_or_Krylov_inverses_recomputed",
                    "five_original_Lj_RR128_computed",
                    "five_original_Lj_weight_one_144_complements_computed",
                    "remaining_six_b_branches_A_B_computed","original_t_frame_calibration_computed",
                    "connection_Poincare_period_or_height_computed"):
            assert final[key] is False
        assert final["source_characteristic_zero_objects_are_exact_unit_solve_expressions"] is True
        if final["complete"] is True:
            assert run["complete"] is True and run["process_exit_code"]==0 and run["error"] is None
            assert core is not None and core["complete"] is True and core["error"] is None
            assert core["certificate_sha256"]==files[FINAL]["sha256"]
            for key in ("actual_complete_common_cusp_418_space_certified",
                        "actual_complete_Dstar_418_space_certified",
                        "actual_original_Qf_principal_identity_certified"):
                assert final[key] is core[key] is True
            assert final["actual_complete_residual_F_269_space_certified"] is True
            assert final["actual_complete_standardizing_146_space_certified"] is True
            assert final["actual_new_pencil_rank"]==core["actual_new_pencil_rank"]==962
            assert isinstance(final["accepted_trial"],int) and final["accepted_trial"]>=1
            inventory=stage(final["stage_manifest"])
            indexed={ref["file"]:plain(ref) for ref in inventory["files"]}
            assert indexed==complete_stages and len(indexed)==len(inventory["files"])
            assert plain(final["resume_state"])==files[current_name]
            audit=stage(final["source_audit"])
            assert audit["R845_R872_R842_same_original_R827_place_verified"] is True
            assert audit["original_b_root"]==637573097
            assert audit["old_original_products_jets_or_inverse_arithmetic_recomputed"] is False
            assert audit["finite_images_not_relabelled_as_characteristic_zero_coefficients"] is True
            jets=stage(final["original_V3_point_jets"])
            dimensions(jets["matrix_mod_prime"],252,690)
            assert len(jets["copied_original_V2_to_V3_column_pairs"])==418
            assert len(jets["new_highest_power_columns"])==272
            assert jets["all418_original_columns_copied_without_recomputation"] is True
            assert jets["no_original_Hensel_step_recomputed"] is True
            cusp_matrix=stage(final["common_cusp_constraint_matrix"])
            dimensions(cusp_matrix["matrix_mod_prime"],272,690)
            dimensions(cusp_matrix["cusp_quotient_matrix_mod_prime"],20,690)
            assert cusp_matrix["source_original_two_chart_C"]==expanded["inputs"]["cusp_reduction"]
            assert cusp_matrix["source_V3_point_jets"]==final["original_V3_point_jets"]
            assert cusp_matrix["all20_original_cusp_field_coordinates_retained"] is True
            cusp=stage(final["complete_common_cusp_418_kernel"])
            assert cusp["accepted"] is True and cusp["actual_rank_mod_prime"]==272
            assert cusp["actual_kernel_dimension"]==418
            assert cusp["source_references"]["constraint_matrix"]==final["common_cusp_constraint_matrix"]
            original=stage(final["original_269_relation_kernel"])
            assert original["actual_rank"]==1111 and original["actual_kernel_dimension"]==269
            dimensions(original["kernel_basis_mod_prime"],1380,269)
            assert original["source_references"]["old_rank_profile"]==expanded["inputs"]["old_rank"]
            residual=stage(final["complete_residual_F_269_space"])
            assert residual["accepted"] is True and residual["actual_projected_rank"]==269
            assert residual["source_complete_kernel"]==final["original_269_relation_kernel"]
            standard=stage(final["complete_standardizing_146_space"])
            assert standard["accepted"] is True and standard["dimension"]==146
            assert standard["source_complete_residual_F_space"]==final["complete_residual_F_269_space"]
            assert standard["selected_column_rescaled"] is False
            v=stage(final["fixed_v"])
            assert v["which"]=="v" and v["trial"] is None
            assert v["source_complete_standardizing_space"]==final["complete_standardizing_146_space"]
            assert v["order123_is_exact"] is True and v["order123_coefficient_mod_prime"]!=0
            profile=stage(final["accepted_new_pencil_profile"])
            assert profile["accepted"] is True and profile["actual_rank"]==962
            assert profile["source_fixed_v"]==final["fixed_v"]
            assert profile["source_candidate_w"]==final["accepted_w"]
            assert profile["integer_parameter"]==final["accepted_trial"]
            assert profile["additional_common_zero_divisor_degree"]==0
            assert profile["image_is_exactly_H0_6H_minus_F_minus_123P0"] is True
            Dstar=stage(final["complete_Dstar_418_kernel"])
            assert Dstar["accepted"] is True and Dstar["actual_projected_rank"]==418
            dimensions(Dstar["original_V3_basis_mod_prime"],690,418)
            complete_kernel=stage(Dstar["source_complete_kernel"])
            assert complete_kernel["actual_rank"]==962 and complete_kernel["actual_kernel_dimension"]==418
            assert complete_kernel["source_references"]["profile"]==final["accepted_new_pencil_profile"]
            principal=stage(final["original_D_cusp_chi_principal_inputs"])
            assert principal["source_complete_Dstar_418_space"]==final["complete_Dstar_418_kernel"]
            assert principal["source_complete_D_C_418_space"]==final["complete_common_cusp_418_kernel"]
            assert principal["source_complete_D_chi_418_space"]==expanded["inputs"]["chi_kernel"]
            assert principal["source_original_global_eta_DAG"]==expanded["inputs"]["global_DAG"]
            assert principal["complete_original_Dstar_space_certified"] is True
            assert principal["complete_original_common_cusp_space_certified"] is True
            assert principal["ideal_principal_factor_direction"]=="positive multiplication by Q_f"
            assert principal["Q_f_order_in_actual_local_parameter"]==-1457
            assert principal["Q_f_leading_coefficient_mod_prime"]!=0
            assert principal["Galois_norm_identity"]["remaining_six_b_branches_each_A_and_B_RHS"]==12
            assert principal["original_t_equals_actual_local_parameter_asserted"] is False
            assert principal["original_theta_rigidification_or_non_p_terms_changed"] is False
        else:
            assert run["complete"] is False
            # A false FINAL can predate later saved stages or current; only true completion
            # binds all terminal references as an immutable inventory.
    if run["complete"]:
        assert final is not None and final["complete"] is True
    print("R880_VERIFY="+json.dumps({
        "result":RESULT,"complete":bool(final and final["complete"]),
        "actual_selected_source_count":source_receipt["actual_selected_source_count"],
        "actual_complete_math_stage_count":len(complete_stages),
        "actual_complete_common_cusp_418_space_certified":bool(final and final["actual_complete_common_cusp_418_space_certified"]),
        "actual_complete_Dstar_418_space_certified":bool(final and final["actual_complete_Dstar_418_space_certified"]),
        "actual_new_pencil_rank":final.get("actual_new_pencil_rank") if final else None,
        "five_original_Lj_RR128_or_144_computed":False,
        "new_mathematics_executed_in_verifier":False},sort_keys=True),flush=True)
    return 0

def main():
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode",choices=("compute","verify"))
    parser.add_argument("--request",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    item=read(args.request);IO=guard(item,args.request)
    try:
        code=compute(item,args.output,args.request,IO) if args.mode=="compute" else verify(item,args.output,args.request,IO)
    except BaseException:
        traceback.print_exc()
        raise
    raise SystemExit(code)

if __name__=="__main__":
    main()
