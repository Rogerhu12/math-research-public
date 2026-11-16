#!/usr/bin/env python3
"""R885 standard-library source selection, same-core recovery and public runner."""
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
TOPIC=S.parent
REPO=TOPIC.parent.parent
REPOSITORY="Rogerhu12/math-research-public"
RESULT="R885-original-polynomial-one-row-adjugate"
FINAL="p41-original-polynomial-one-row-adjugate-certificate.json"
PREFIX="R885-adjugate-"
CORE="R885_original_one_row_adjugate.py"
REQUEST=TOPIC/"notes/R885-polynomial-one-row-adjugate-public-request.json"
MANIFEST="full-outputs-manifest.json"
REFERENCE="full-outputs-manifest-reference.json"
BUNDLE="R885-retained-R827-inputs.tar.gz"
INVENTORY="R885-original-source-inventory.json"
INPUT_RECEIPT="R885-retained-inputs-receipt.json"
EXPANDED="R885-expanded-job.json"
META=("public-actions-input.json","run-receipt.json","core-receipt.json")
BASE=("result","run_id","source_commit","core_sha256","manifest_sha256")
SOURCE_RESULT="R827-original-global-modular-derivative-termination"
SOURCE_CORE="d9cf773976f3beff7f44ff30f8b593665f481470cb52297239710e0ce6e062d2"
RANGE_FILE="R824_public_original_global_polar_generators.py"
RANGE_SHA="c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
P=1000000753
ROOT=549966761
EPS=[0]+[1]*144+[2]*127
IO=None
STRATEGY={
    "scope": "universal-original-one-row-adjugate",
    "original_curve": "original genus127 Y; p41; level82; original minus3 descent",
    "auxiliary_prime": 1000000753,
    "normal_basis_rank": 272,
    "normal_basis_degrees": [
        0,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        2
    ],
    "W_degree": 3,
    "weighted_W_bound": "1+epsilon_input-epsilon_output",
    "characteristic_coefficient_bound": "degree_z(c_k)<=k",
    "interpolation_node_count": 273,
    "interpolation_nodes": "all actual completed original eight cyclic nodes in saved order, then least unused nonnegative integers",
    "old_nodes": "reuse original W(a),K,Kinv; only missing k272 and relation are new",
    "new_nodes": "original polynomial W evaluation and exact nmod_mat charpoly; no new Krylov inverse",
    "characteristic_interpolation": "first k+1 nodes for c_k; complete all273-node substitution",
    "row_convention": "left e0 transpose",
    "row_recurrence": "b0=e0^T; b_k=b_(k-1)*W+c_k*e0^T",
    "row_bound": "degree_z(b_k,j)<=k+epsilon_j",
    "full_terminal_Cayley_Hamilton_row_verified": True,
    "whole_adjugate_matrix_computed": False,
    "old_W_or_Krylov_arithmetic_recomputed": False,
    "target_Artin_normal_coordinates_or_nine_norms_computed": False,
    "Picard_support_or_nonp_calibration_or_height_computed": False,
    "budget_excluded_from_identity": True
}

def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for part in iter(lambda:f.read(4*1024*1024),b""):
            h.update(part)
    return h.hexdigest()

def read(path):
    path=Path(path)
    with (gzip.open if path.suffix==".gz" else open)(path,"rt",encoding="utf-8") as f:
        return json.load(f)

def save(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_name(path.name+".tmp")
    temporary.write_text(json.dumps(value,sort_keys=True,separators=(",",":"),
                                    ensure_ascii=False)+"\n",encoding="utf-8")
    temporary.replace(path)

def fingerprint(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def plain(row):
    ans={k:row[k] for k in ("file","bytes","sha256")}
    p=PurePosixPath(ans["file"])
    assert len(p.parts)==1 and p.name not in ("",".","..") and "\\" not in ans["file"]
    assert isinstance(ans["bytes"],int) and ans["bytes"]>=0
    assert re.fullmatch("[0-9a-f]{64}",ans["sha256"])
    return ans

def spec(path):
    path=Path(path)
    return {"file":path.name,"bytes":path.stat().st_size,"sha256":sha(path)}

def bound(folder,row):
    row=plain(row);path=Path(folder)/row["file"]
    assert spec(path)==row,("bound_file",row["file"])
    return path

def topic_path(name):
    p=PurePosixPath(name)
    assert not p.is_absolute() and ".." not in p.parts
    path=(TOPIC/str(p)).resolve()
    assert path.is_relative_to(TOPIC.resolve())
    return path

def identity(source):
    return {**{k:source[k] for k in BASE},
            "configuration_sha256":source["configuration_sha256"],
            "configuration_stage":plain(source["configuration_stage"]),
            "selected_files_sha256":fingerprint(source["files"])}

def expected_tag(item,source,inputs):
    return {"result":RESULT,"source_sha256":item["core_sha256"],"p":41,
            "python_flint":"0.9.0","method_sha256":item["method_sha256"],
            "proofs":item["proofs"],"source_R827":identity(source),
            "inputs":inputs,"strategy":STRATEGY}

def load_io():
    global IO
    path=S/RANGE_FILE
    assert sha(path)==RANGE_SHA
    description=importlib.util.spec_from_file_location("R885_frozen_standard_library_Range",path)
    IO=importlib.util.module_from_spec(description)
    description.loader.exec_module(IO)

def guard(item,request):
    assert os.environ.get("GITHUB_ACTIONS")=="true"
    assert os.environ.get("GITHUB_REPOSITORY")==REPOSITORY
    assert request.resolve()==REQUEST.resolve()
    assert item["result"]==RESULT and item["p"]==41
    assert item["producer_inputs_pending"] is False
    assert item["core"]==CORE and sha(S/CORE)==item["core_sha256"]
    assert item["wrapper"]==Path(__file__).name and sha(__file__)==item["wrapper_sha256"]
    assert item["io_helper"]==RANGE_FILE and item["io_helper_sha256"]==RANGE_SHA
    assert 0<item["budget_minutes"]<=300
    assert sha(REPO/"README.md")==item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md")==item["readme_sha256"]["topic"]
    assert sha(topic_path(item["method"]))==item["method_sha256"]
    for row in item["proofs"].values():
        assert sha(topic_path(row["path"]))==row["sha256"]
    assert set(item["input_names"])=={"W_reduction","place_audit","cyclic_grid"}
    assert set(item["input_pins"])=={"W_reduction","place_audit"}
    load_io()

def entry_map(folder,source):
    path=Path(folder)/MANIFEST
    assert sha(path)==source["manifest_sha256"]
    if "manifest_bytes" in source:
        assert path.stat().st_size==source["manifest_bytes"]
    data=read(path)
    assert data["result"]==source["result"]
    entries={row["file"]:plain(row) for row in data["files"]}
    assert len(entries)==len(data["files"])
    if "manifest_file_count" in source:
        assert len(entries)==source["manifest_file_count"]
    entries[MANIFEST]=spec(path)
    return entries

def metadata(folder,source,entries):
    initial,run,core=[read(bound(folder,entries[name])) for name in META]
    assert initial["result"]==run["result"]==core["result"]==source["result"]==SOURCE_RESULT
    assert initial["source_commit"]==run["source_commit"]==source["source_commit"]
    assert str(run["workflow_run_id"])==str(source["run_id"])
    assert initial["core_sha256"]==core["source_sha256"]==source["core_sha256"]==SOURCE_CORE
    assert run["complete"] is False and run["process_exit_code"]==124
    assert core["complete"] is False
    assert run["core_receipt_sha256"]==entries["core-receipt.json"]["sha256"]
    anchor_spec=plain(source["configuration_stage"])
    assert entries[anchor_spec["file"]]==anchor_spec
    anchor=read(bound(folder,anchor_spec))
    assert anchor["complete"] is True
    tag=anchor["configuration"]
    assert tag["result"]==SOURCE_RESULT and tag["source_sha256"]==SOURCE_CORE
    assert fingerprint(tag)==source["configuration_sha256"]
    assert tag["normal_basis_rank"]==272 and tag["normal_basis_degrees"]==EPS
    return tag

def source_review(folder,source,inputs):
    entries=entry_map(folder,source)
    assert entries[MANIFEST]==plain(source["files"][MANIFEST])
    assert all(entries[name]==plain(row) for name,row in source["files"].items())
    for row in source["files"].values():
        bound(folder,row)
    tag=metadata(folder,source,entries)
    def stage(row):
        row=plain(row)
        assert source["files"][row["file"]]==row
        value=read(bound(folder,row))
        assert value["complete"] is True and value["configuration"]==tag
        if "result" in value:
            assert value["result"]==SOURCE_RESULT
        return value
    W=stage(inputs["W_reduction"])
    place=stage(inputs["place_audit"])
    grid=stage(inputs["cyclic_grid"])
    assert W["prime"]==place["prime"]==grid["prime"]==P
    assert place["original_zeta_root"]==ROOT
    assert W["original_rational_denominators_all_units"] is True
    assert W["original_W_e0_equals_e1_verified"] is True
    assert len(W["W_coefficients_mod_prime"])==4
    assert all(len(a)==272 and all(len(row)==272 for row in a) for a in W["W_coefficients_mod_prime"])
    assert grid["all_eight_actual_determinants_nonzero"] is True
    assert grid["distinct_residue_values_and_unit_Vandermonde_certified"] is True
    assert len(grid["points"])==len(set(grid["points"]))==8
    assert len(grid["Krylov_point_stages"])==8
    assert inputs["Krylov_points"]==grid["Krylov_point_stages"]
    for z0,row in zip(grid["points"],inputs["Krylov_points"]):
        value=stage(row)
        assert value["prime"]==P and value["z0"]==z0
        assert value["usable"] is True and value["actual_cyclic_rank"]==272
        assert value["both_inverse_products_verified"] is True
        assert 0<value["actual_determinant_mod_prime"]<P
        assert value["source_original_W"]==plain(inputs["W_reduction"])
        for key in ("W_evaluated_mod_prime","Krylov_matrix_mod_prime","inverse_Krylov_matrix_mod_prime"):
            assert len(value[key])==272 and all(len(a)==272 for a in value[key])
    required=set(META)|{MANIFEST}|{inputs[k]["file"] for k in ("W_reduction","place_audit","cyclic_grid")}
    required.update(row["file"] for row in inputs["Krylov_points"])
    assert required==set(source["files"]) and len(required)==15
    return {"result":RESULT,"source_R827":identity(source),"actual_old_cyclic_nodes":grid["points"],
            "selected_original_file_count":len(required),"complete_old_W_and_eight_Krylov_stages_verified":True,
            "original_source_completed_stages_preserved_despite_later_BudgetStop":True,
            "original_large_carrier_or_Hermite_history_read":False,
            "new_mathematics_executed":False}

def pack(folder,source,target):
    temporary=Path(target).with_name(Path(target).name+".tmp")
    with temporary.open("wb") as raw:
        with gzip.GzipFile(filename="",fileobj=raw,mode="wb",mtime=0,compresslevel=2) as zipped:
            with tarfile.open(fileobj=zipped,mode="w|") as archive:
                for name,row in sorted(source["files"].items()):
                    path=bound(folder,row)
                    info=archive.gettarinfo(str(path),arcname="R827/"+name)
                    info.uid=info.gid=0;info.uname=info.gname="";info.mtime=0
                    with path.open("rb") as f:
                        archive.addfile(info,f)
    temporary.replace(target)

def unpack(bundle,retained,source):
    folder=Path(retained)/"R827";folder.mkdir(parents=True,exist_ok=True)
    seen=set()
    with tarfile.open(bundle,"r|gz") as archive:
        for member in archive:
            if member.isdir():
                continue
            name=PurePosixPath(member.name)
            assert not name.is_absolute() and ".." not in name.parts and "\\" not in member.name
            assert member.isfile() and len(name.parts)==2 and name.parts[0]=="R827"
            filename=name.name
            assert filename in source["files"] and filename not in seen
            row=source["files"][filename]
            assert member.size==row["bytes"]
            path=folder/filename
            h=hashlib.sha256();count=0
            temporary=path.with_name(path.name+".download")
            with archive.extractfile(member) as f,temporary.open("wb") as out:
                for part in iter(lambda:f.read(4*1024*1024),b""):
                    out.write(part);h.update(part);count+=len(part)
            assert count==row["bytes"] and h.hexdigest()==row["sha256"]
            if path.exists():
                assert spec(path)==row
                temporary.unlink()
            else:
                temporary.replace(path)
            seen.add(filename)
    assert seen==set(source["files"])
    return folder

def original_pins(item,source,inputs):
    prior=item["source_artifact"]
    assert all(str(prior[k])==str(source[k]) for k in BASE)
    assert prior["configuration_sha256"]==source["configuration_sha256"]
    assert plain(prior["configuration_stage"])==plain(source["configuration_stage"])
    for key,name in item["input_names"].items():
        assert inputs[key]["file"]==name
    for key,row in item["input_pins"].items():
        assert inputs[key]==plain(row)

def prepare(item,out,allow_download=True):
    out=Path(out);retained=out.parent/"retained-R885";retained.mkdir(parents=True,exist_ok=True)
    if all((out/name).exists() for name in (BUNDLE,INVENTORY,INPUT_RECEIPT)):
        inventory=read(out/INVENTORY);receipt=read(out/INPUT_RECEIPT)
        assert inventory["result"]==receipt["result"]==RESULT
        assert inventory["complete"] is True and receipt["complete"] is True
        assert plain(receipt["source_inventory"])==spec(out/INVENTORY)
        assert plain(receipt["source_bundle"])==spec(out/BUNDLE)
        source=inventory["source_R827"];inputs=inventory["inputs"]
        original_pins(item,source,inputs)
        folder=unpack(out/BUNDLE,retained,source)
        review=source_review(folder,source,inputs)
        assert receipt["selected_file_count"]==len(source["files"])
        return folder,source,inputs,review
    assert allow_download,"No retained R885 original-source bundle is available."
    prior=item["source_artifact"]
    folder=retained/"R827";folder.mkdir(parents=True,exist_ok=True)
    archive=IO.Archive(prior,out.parent/"R885-R827-archive",whole=False)
    try:
        archive.extract_bound(MANIFEST,prior["manifest_sha256"],folder/MANIFEST,prior["manifest_bytes"])
        entries=entry_map(folder,prior)
        names=set(META)|set(item["input_names"].values())
        for key,row in item["input_pins"].items():
            assert entries[item["input_names"][key]]==plain(row)
        archive.extract_many([(n,entries[n]["sha256"],folder/n,entries[n]["bytes"]) for n in sorted(names)])
        tag=metadata(folder,prior,entries)
        inputs={key:entries[name] for key,name in item["input_names"].items()}
        grid=read(bound(folder,inputs["cyclic_grid"]))
        assert grid["complete"] is True and grid["configuration"]==tag
        inputs["Krylov_points"]=[plain(row) for row in grid["Krylov_point_stages"]]
        assert len(inputs["Krylov_points"])==8
        for row in inputs["Krylov_points"]:
            assert entries[row["file"]]==row
        points={row["file"] for row in inputs["Krylov_points"]}
        archive.extract_many([(n,entries[n]["sha256"],folder/n,entries[n]["bytes"]) for n in sorted(points)])
        names.update(points);names.add(MANIFEST)
        source={**{k:prior[k] for k in BASE},
                "manifest_bytes":prior["manifest_bytes"],"manifest_file_count":prior["manifest_file_count"],
                "configuration_stage":plain(prior["configuration_stage"]),
                "configuration_sha256":fingerprint(tag),
                "files":{n:entries[n] for n in sorted(names)}}
        original_pins(item,source,inputs)
        review=source_review(folder,source,inputs)
        transport=archive.receipt()
        save(out/INVENTORY,{"result":RESULT,"complete":True,"source_R827":source,"inputs":inputs,
                           "range_transport":transport,"large_original_carrier_or_Hermite_history_read":False})
        pack(folder,source,out/BUNDLE)
        save(out/INPUT_RECEIPT,{"result":RESULT,"complete":True,"source_bundle":spec(out/BUNDLE),
                               "source_inventory":spec(out/INVENTORY),"selected_file_count":len(source["files"]),
                               "source_R827":identity(source),"range_transport":transport,
                               "all_selected_original_bytes_verified":True,"new_mathematics_executed":False})
        print("R885_INPUT_REVIEW="+json.dumps(review,sort_keys=True),flush=True)
        return folder,source,inputs,review
    finally:
        archive.close()

def restore(item,out):
    resume=item.get("resume")
    if not resume:
        return
    assert resume["result"]==RESULT and resume["core_sha256"]==item["core_sha256"]
    directory=out.parent/"R885-resume"
    directory.mkdir(parents=True,exist_ok=True)
    archive=IO.Archive(resume,out.parent/"R885-resume-archive",whole=False)
    try:
        archive.extract_bound(MANIFEST,resume["manifest_sha256"],directory/MANIFEST,resume.get("manifest_bytes"))
        entries=entry_map(directory,resume)
        names=set(META)&set(entries)
        names.update((BUNDLE,INVENTORY,INPUT_RECEIPT))
        archive.extract_many([(n,entries[n]["sha256"],directory/n,entries[n]["bytes"]) for n in sorted(names)])
        initial=read(directory/"public-actions-input.json");run=read(directory/"run-receipt.json")
        assert initial["result"]==run["result"]==RESULT
        assert initial["source_commit"]==run["source_commit"]==resume["source_commit"]
        assert str(run["workflow_run_id"])==str(resume["run_id"])
        assert initial["core_sha256"]==item["core_sha256"]
        assert initial["wrapper_sha256"]==item["wrapper_sha256"]
        for key in ("proofs","method_sha256","input_pins","input_names"):
            assert initial["job"][key]==item[key]
        core=None
        if run.get("core_receipt_sha256") is not None:
            assert "core-receipt.json" in entries
            assert entries["core-receipt.json"]["sha256"]==run["core_receipt_sha256"]
            core=read(directory/"core-receipt.json")
            assert core["result"]==RESULT and core["source_sha256"]==item["core_sha256"]
        else:
            assert run["complete"] is False
        inventory=read(directory/INVENTORY);receipt=read(directory/INPUT_RECEIPT)
        assert plain(receipt["source_inventory"])==entries[INVENTORY]
        assert plain(receipt["source_bundle"])==entries[BUNDLE]
        source,inputs=inventory["source_R827"],inventory["inputs"]
        original_pins(item,source,inputs)
        tag=expected_tag(item,source,inputs)
        assert initial["mathematical_configuration_sha256"]==fingerprint(tag)
        for name in (BUNDLE,INVENTORY,INPUT_RECEIPT):
            target=out/name
            if target.exists():
                assert spec(target)==entries[name]
            else:
                shutil.copyfile(directory/name,target)
        stages=[n for n in entries if n.startswith(PREFIX) and n.endswith(".json.gz")]
        archive.extract_many([(n,entries[n]["sha256"],directory/n,entries[n]["bytes"]) for n in stages])
        for name in stages:
            value=read(directory/name)
            assert value["result"]==RESULT and value["configuration"]==tag
            if name==PREFIX+"current.json.gz":
                assert value["complete"] is False
            else:
                assert value["complete"] is True
            target=out/name
            if target.exists():
                assert spec(target)==entries[name]
            else:
                shutil.copyfile(directory/name,target)
        if FINAL in entries:
            archive.extract_bound(FINAL,entries[FINAL]["sha256"],directory/FINAL,entries[FINAL]["bytes"])
            cert=read(directory/FINAL)
            assert cert["result"]==RESULT and cert["configuration"]==tag
            if cert["complete"] is True:
                # Only a true endpoint fixes the exact complete inventory.
                assert plain(cert["stage_manifest"])==entries[cert["stage_manifest"]["file"]]
                stage_manifest=read(bound(directory,cert["stage_manifest"]))
                for row in stage_manifest["files"]:
                    assert plain(row)==entries[row["file"]]
                shutil.copyfile(directory/FINAL,out/FINAL)
        save(out/"resume-import-receipt.json",{
            "result":RESULT,"complete":True,"source":resume,
            "original_manifest":spec(directory/MANIFEST),
            "mathematical_configuration_sha256":fingerprint(tag),
            "restored_stage_count":len(stages),"same_core_and_original_tags_preserved":True,
            "old_incomplete_final_did_not_constrain_later_current":True,
            "missing_core_receipt_honestly_retained":core is None,
            "range_transport":archive.receipt()})
    finally:
        archive.close()

def output_manifest(out):
    files=[]
    for path in sorted(Path(out).iterdir()):
        if not path.is_file() or path.name in (MANIFEST,REFERENCE):
            continue
        if path.name.endswith((".tmp",".download",".partial")):
            continue
        files.append(spec(path))
    value={"result":RESULT,"source_commit":os.environ["GITHUB_SHA"],
           "workflow_run_id":os.environ["GITHUB_RUN_ID"],"files":files}
    save(Path(out)/MANIFEST,value)
    save(Path(out)/REFERENCE,{"result":RESULT,**spec(Path(out)/MANIFEST)})
    return spec(Path(out)/MANIFEST)

def compute(item,out,request):
    out=Path(out);out.mkdir(parents=True,exist_ok=True)
    code,error,outer_timeout=1,None,False
    try:
        restore(item,out)
        folder,source,inputs,review=prepare(item,out)
        expanded={**item,"source":dict(source,directory=str(folder.resolve())),"inputs":inputs}
        save(out/EXPANDED,expanded)
        tag=expected_tag(item,source,inputs)
        save(out/"public-actions-input.json",{
            "result":RESULT,"p":41,"source_commit":os.environ["GITHUB_SHA"],
            "workflow_run_id":os.environ["GITHUB_RUN_ID"],"job":item,
            "core_sha256":item["core_sha256"],"wrapper_sha256":item["wrapper_sha256"],
            "request_sha256":sha(request),"workflow_sha256":sha(REPO/item["workflow"]),
            "root_readme_sha256":sha(REPO/"README.md"),"topic_readme_sha256":sha(TOPIC/"README.md"),
            "expanded_job":spec(out/EXPANDED),"source_inventory":spec(out/INVENTORY),
            "mathematical_configuration_sha256":fingerprint(tag),
            "source_R827":identity(source),"new_mathematics_in_wrapper":False})
        command=[sys.executable,str(S/CORE),"--config",str(out/EXPANDED),
                 "--output",str(out),"--budget-minutes",str(item["budget_minutes"])]
        with (out/"core.log").open("ab") as log:
            process=subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
            try:
                code=process.wait(timeout=item["budget_minutes"]*60+900)
            except subprocess.TimeoutExpired:
                outer_timeout=True
                os.killpg(process.pid,signal.SIGTERM)
                try:
                    process.wait(timeout=15)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid,signal.SIGKILL);process.wait()
                code=124;error="outer_timeout"
        if code==0:
            assert read(out/FINAL)["complete"] is True
        print((out/"core.log").read_text(errors="replace")[-16000:],flush=True)
    except Exception as exc:
        code=code if code not in (0,1) else 1
        error=type(exc).__name__+": "+str(exc)
        traceback.print_exc()
    finally:
        save(out/"run-receipt.json",{
            "result":RESULT,"source_commit":os.environ["GITHUB_SHA"],
            "workflow_run_id":os.environ["GITHUB_RUN_ID"],"workflow_attempt":os.environ.get("GITHUB_RUN_ATTEMPT","1"),
            "core_sha256":item["core_sha256"],"wrapper_sha256":item["wrapper_sha256"],
            "complete":code==0,"process_exit_code":code,"error":error,"outer_timeout":outer_timeout,
            "execution_environment":"public-repository-github-actions",
            "core_receipt_sha256":sha(out/"core-receipt.json") if (out/"core-receipt.json").exists() else None,
            "finished_at_utc":dt.datetime.now(dt.timezone.utc).isoformat()})
        output_manifest(out)
    return code

def dimensions(value,m,n):
    assert len(value)==m and all(len(row)==n for row in value)

def verify(item,out,request):
    out=Path(out)
    manifest=read(out/MANIFEST)
    assert manifest["result"]==RESULT
    entries={r["file"]:plain(r) for r in manifest["files"]}
    assert len(entries)==len(manifest["files"])
    for row in entries.values():
        bound(out,row)
    actual={p.name for p in out.iterdir() if p.is_file() and not p.name.endswith((".tmp",".download",".partial"))}
    assert actual==set(entries)|{MANIFEST,REFERENCE}
    assert plain(read(out/REFERENCE))==spec(out/MANIFEST)
    folder,source,inputs,review=prepare(item,out,allow_download=False)
    tag=expected_tag(item,source,inputs)
    initial=read(out/"public-actions-input.json");run=read(out/"run-receipt.json")
    assert initial["result"]==run["result"]==RESULT
    assert initial["source_commit"]==run["source_commit"]==os.environ["GITHUB_SHA"]
    assert str(run["workflow_run_id"])==os.environ["GITHUB_RUN_ID"]
    assert initial["core_sha256"]==run["core_sha256"]==item["core_sha256"]
    assert initial["wrapper_sha256"]==run["wrapper_sha256"]==item["wrapper_sha256"]
    assert initial["request_sha256"]==sha(request)
    assert initial["expanded_job"]==entries[EXPANDED]
    assert initial["mathematical_configuration_sha256"]==fingerprint(tag)
    expanded=read(out/EXPANDED)
    assert expected_tag(expanded,expanded["source"],expanded["inputs"])==tag
    core=None
    if run["core_receipt_sha256"] is not None:
        assert entries["core-receipt.json"]["sha256"]==run["core_receipt_sha256"]
        core=read(out/"core-receipt.json")
        assert core["result"]==RESULT and core["source_sha256"]==item["core_sha256"]
        if core["configuration"] is not None:
            assert core["configuration"]==tag
    else:
        assert run["complete"] is False
    complete_stages=[]
    for name,row in entries.items():
        if not name.startswith(PREFIX) or not name.endswith(".json.gz"):
            continue
        value=read(out/name)
        assert value["result"]==RESULT and value["configuration"]==tag
        if name==PREFIX+"current.json.gz":
            assert value["complete"] is False
            for member in value["completed_stages"].values():
                assert plain(member)==entries[member["file"]]
            continue
        assert value["complete"] is True
        if name.startswith(PREFIX+"stage-manifest-"):
            for member in value["files"]:
                assert plain(member)==entries[member["file"]]
            # Historical inventories may refer to an earlier version of the current pointer.
            continue
        complete_stages.append(row)
    cert=read(out/FINAL) if FINAL in entries else None
    if cert is not None:
        assert cert["result"]==RESULT and cert["configuration"]==tag
        assert cert["p"]==41 and cert["actual_auxiliary_prime"]==P and cert["normal_basis_rank"]==272
        for key in ("old_Krylov_inverses_or_original_W_recomputed","full_adjugate_matrix_computed",
                    "target_Artin_normal_coordinates_computed","nine_reference_norms_computed",
                    "original_Picard_support_or_nonp_calibration_or_height_computed"):
            assert cert[key] is False
        if cert["complete"] is True:
            assert plain(cert["stage_manifest"])==entries[cert["stage_manifest"]["file"]]
            inventory=read(bound(out,cert["stage_manifest"]))
            assert inventory["files"]==sorted(complete_stages,key=lambda row:row["file"])
            assert plain(cert["resume_state"])==entries[cert["resume_state"]["file"]]
            assert inventory["current_checkpoints"]==[plain(cert["resume_state"])]
            assert cert["actual_completed_node_count"]==273 and cert["actual_completed_row_level_count"]==273
            assert cert["actual_original_modular_characteristic_polynomial_certified"] is True
            assert cert["actual_original_complete_polynomial_adjugate_row_certified"] is True
            assert cert["full_terminal_Cayley_Hamilton_row_verified"] is True
            audit=read(bound(out,cert["source_audit"]))
            assert audit["source_R827"]==identity(source) and audit["inputs"]==inputs
            assert audit["all_original_weighted_W_entries_verified"] is True
            assert audit["old_W_and_original_primitive_solutions_not_recomputed"] is True
            nodes=audit["actual_interpolation_nodes"]
            assert nodes==cert["actual_interpolation_nodes"] and len(nodes)==len(set(nodes))==273
            assert nodes[:8]==read(bound(folder,inputs["cyclic_grid"]))["points"]
            relation=read(bound(out,cert["characteristic_relation"]))
            assert relation["exact_original_modular_characteristic_polynomial_certified"] is True
            assert relation["all273_nodes_for_all273_T_coefficients_verified"] is True
            assert relation["degree_bounds_from_original_principal_minor_weights_verified"] is True
            assert relation["coefficient_degree_bounds"]==list(range(273))
            coefficients=relation["coefficient_polynomials_ascending_z"]
            assert len(coefficients)==273 and coefficients[0]==[1]
            assert all(len(row)==k+1 for k,row in enumerate(coefficients))
            assert len(relation["source_node_stages"])==273
            for k,row in enumerate(relation["source_node_stages"]):
                node=read(bound(out,row))
                assert node["prime"]==P and node["ordinal"]==k and node["z_value"]==nodes[k]
                co=node["characteristic_coefficients_ascending_T"]
                assert len(co)==273 and co[-1]==1 and node["monic"] is True
                if k<8:
                    assert node["kind"]=="one_new_k272_from_completed_original_Krylov"
                    assert node["source_original_Krylov"]==inputs["Krylov_points"][k]
                    assert node["full_K_times_relation_equals_k272"] is True
                    assert node["completed_original_Krylov_inverse_recomputed"] is False
                    assert len(node["new_k272"])==len(node["relation_coefficients"])==272
                else:
                    assert node["kind"]=="new_nmod_mat_characteristic_polynomial"
                    assert node["new_Krylov_matrix_or_inverse_computed"] is False
            adj=read(bound(out,cert["one_row_adjugate"]))
            assert adj["characteristic_relation"]==plain(cert["characteristic_relation"])
            assert adj["r_is_exactly_original_e0_transpose_adjugate"] is True
            assert adj["all272_polynomial_components_of_terminal_row_zero"] is True
            assert adj["all_coefficient_bounds_k_plus_epsilon_verified"] is True
            assert adj["entire_adjugate_matrix_materialized"] is False
            assert adj["target_Artin_substitution_or_r0_unit_certified"] is False
            terms=adj["adjugate_row_T_terms"]
            assert len(terms)==272
            previous=None
            for k,row in enumerate(terms):
                assert row["T_power"]==271-k and row["b_level"]==k
                data=read(bound(out,row["source"]))
                assert data["row_level"]==k and data["shape"]==[k+3,272]
                assert data["source_previous_row"]==previous
                assert data["source_characteristic_relation"]==plain(cert["characteristic_relation"])
                dimensions(data["coefficient_rows_ascending_z"],k+3,272)
                assert data["component_degree_bounds"]==[k+e for e in EPS]
                assert data["full_weighted_support_verified"] is True
                assert data["full_left_row_recurrence_computed"] is True
                previous=plain(row["source"])
            terminal=read(bound(out,adj["terminal_Cayley_Hamilton_row"]))
            assert terminal["source_previous_row"]==previous and terminal["row_level"]==272
            assert terminal["terminal_complete_polynomial_row_zero"] is True
            dimensions(terminal["coefficient_rows_ascending_z"],275,272)
            assert all(x==0 for row in terminal["coefficient_rows_ascending_z"] for x in row)
            assert len(complete_stages)==549
    if run["complete"] is True:
        assert run["process_exit_code"]==0 and run["error"] is None
        assert core is not None and core["complete"] is True and core["error"] is None
        assert core["process_exit_code"]==0 and core["configuration"]==tag
        assert cert is not None and cert["complete"] is True
        assert core["certificate_sha256"]==entries[FINAL]["sha256"]
    summary={"result":RESULT,"complete":bool(run["complete"] and cert and cert["complete"]),
             "actual_complete_stage_count":len(complete_stages),"selected_original_file_count":len(source["files"]),
             "all_output_bytes_and_original_source_identities_verified":True,
             "actual_original_modular_characteristic_polynomial_certified":
                 bool(cert and cert["actual_original_modular_characteristic_polynomial_certified"]),
             "actual_original_complete_polynomial_adjugate_row_certified":
                 bool(cert and cert["actual_original_complete_polynomial_adjugate_row_certified"]),
             "actual_completed_node_count":cert.get("actual_completed_node_count") if cert else None,
             "actual_completed_row_level_count":cert.get("actual_completed_row_level_count") if cert else None,
             "old_W_or_Krylov_arithmetic_recomputed":False,"new_mathematics_executed_in_verifier":False,
             "target_Artin_coordinates_nine_norms_Picard_support_or_height_computed":False}
    print("R885_VERIFY="+json.dumps(summary,sort_keys=True),flush=True)
    return 0 if summary["complete"] else 1

def main():
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser()
    parser.add_argument("command",choices=("compute","verify"))
    parser.add_argument("--request",default=str(REQUEST))
    parser.add_argument("--output",required=True)
    args=parser.parse_args()
    request=Path(args.request);item=read(request)
    if "job" in item:
        item=item["job"]
    guard(item,request)
    if args.command=="compute":
        raise SystemExit(compute(item,Path(args.output),request))
    raise SystemExit(verify(item,Path(args.output),request))

if __name__=="__main__":
    main()
