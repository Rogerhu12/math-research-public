#!/usr/bin/env python3
"""R877 standard-library intake transport, resume and output verification.
The original four sources are read byte for byte. No mathematical module is imported.
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
REQUEST=TOPIC/"notes/R877-canonical-A-public-request.json"
RESULT="R877-original-canonical-A-normal-input"
FINAL="p41-original-canonical-A-normal-input-certificate.json"
PREFIX="R877-"
MANIFEST="full-outputs-manifest.json"
REFERENCE="full-outputs-manifest-reference.json"
INVENTORY=PREFIX+"original-source-inventory.json"
RETAINED_RECEIPT=PREFIX+"retained-inputs-receipt.json"
BASE=("result","run_id","source_commit","core_sha256","manifest_sha256")
SOURCES=("R827","R842","R787","R849")
PROOFS=("R872","GP")
EPS=[0]+[1]*144+[2]*127
PRIME,DIM,ROWS,RANK=1000000753,1234,1380,272
IO_HELPER_SHA="c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
META=("public-actions-input.json","run-receipt.json","core-receipt.json")
STRATEGY = {
    "scope":"one_original_canonical_A_normal_right_hand_side",
    "prime":PRIME,"original_branch":0,"canonical_free_column":1186,
    "source_A":"same characteristic-zero U.1 unit-chart solution as R849",
    "source_B":"completed R827 normal vector, read without recomputation",
    "S5_matrix":"completed R842 original 1380 by 1234 matrix",
    "S5_inverse":"completed R827 prime753 selected inverse",
    "original_V5_prefix_blocks":69,"real_coordinates_per_block":20,
    "new_rhs_count":1,"source_column_chunk_size":64,
    "old_original_Fourier_rows_recomputed":False,
    "old_S5_matrix_reduced_again":False,
    "old_S5_inverse_or_determinant_recomputed":False,
    "old_B_normal_conversion_recomputed":False,
    "original_scale_applied_again":False,
    "exact_coordinate_definition":"solve original S5 selected rows against original F69*A_U1",
    "finite_image_verified_in_all1380_original_coordinates":True,
    "normal_polynomial_bound":"5+0-epsilon_output",
    "characteristic_zero_A_coefficients_reconstructed":False,
    "characteristic_zero_normal_coordinates_reconstructed":False,
    "Galois_conjugate_normal_inputs_computed":False,
    "original_five_Lj_RR_spaces_computed":False,
    "only_budget_and_transport_excluded_from_identity":True,
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
    return {"result":RESULT,"source_sha256":item["core_sha256"],"python_flint":"0.9.0","p":41,
        "method_sha256":item["method_sha256"],
        "proofs_sha256":{key:item["proofs"][key]["sha256"] for key in PROOFS},
        "sources":{label:stable_source(item["sources"][label]) for label in SOURCES},
        "inputs":item["inputs"],"normal_basis_degrees":EPS,"strategy":STRATEGY}

def load_IO(item):
    path=S/"R824_public_original_global_polar_generators.py"
    assert item["io_helper"]==path.name
    assert item["io_helper_sha256"]==sha(path)==IO_HELPER_SHA
    module_spec=importlib.util.spec_from_file_location("R877_frozen_original_IO",path)
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
    assert item["core"]=="R877_original_canonical_A_normal_input.py"
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
        assert len(entries)==len(index["sources"])==4 and set(entries)==set(SOURCES)
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

def expected_original_names(item,label,files):
    if label=="R787":
        return {"R787-real-power5-row-"+str(i).zfill(4)+".json.gz" for i in range(DIM)}|{
            "R787-prime-1000000753-chart.json.gz","R787-prime-1000000753-rational-blocks.json.gz",
            "R787-prime-1000000753-selection.json.gz",*META,MANIFEST,REFERENCE}
    return set(item["sources"][label]["selected_file_names"])

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
        assert label in ("R827","R787") and run["complete"] is False
        assert run["process_exit_code"] in value["accepted_checkpoint_exit_codes"]
        assert 0 not in value["accepted_checkpoint_exit_codes"]
        anchor=read(bound(folder,value["configuration_stage"]))
        assert anchor["complete"] is True
        tag=anchor["configuration"]
    assert tag["result"]==value["result"] and tag["source_sha256"]==value["core_sha256"]
    assert fingerprint(tag)==value["configuration_sha256"]
    if run.get("core_receipt_sha256") is not None:
        assert files[META[2]]["sha256"]==run["core_receipt_sha256"]
        core=read(folder/META[2])
        assert core["result"]==value["result"] and core["source_sha256"]==value["core_sha256"]
        if value.get("certificate"):
            assert core["complete"] is True
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
    assert str(index["workflow_run_id"])==str(intake["run_id"]) and index["source_commit"]==intake["source_commit"]
    assert index["request_sha256"]==intake["request_sha256"]
    entries={entry["label"]:entry for entry in index["sources"]}
    assert set(entries)==set(SOURCES) and len(entries)==len(index["sources"])==4
    sources={};total=0;tags={};summaries={}
    for label in SOURCES:
        raw=item["sources"][label]
        entry=entries[label]
        for key in ("run_id","source_commit","core_sha256","manifest_sha256"):
            assert str(entry["source"][key])==str(raw[key])
        summary=read(bound(out,entry["summary"]))
        summaries[label]=summary
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
        assert len(files)==summary["selected_file_count"]
        files[MANIFEST]=plain(summary["manifest"])
        files[REFERENCE]=plain(summary["manifest_reference"])
        assert set(files)==expected_original_names(item,label,files)
        assert len(files)==raw["expected_selected_file_count"]
        for name,pinned in raw.get("file_pins",{}).items():
            assert files[name]==plain(pinned)
        directory=work/"retained"/label
        unpack_source(bound(out,bundle_spec),directory,files)
        value=dict(raw,directory=str(directory),files=files,
            selected_file_count=len(files),selected_files_sha256=fingerprint(files))
        tags[label]=review_original(label,value)
        sources[label]=value;total+=len(files)
    bname="R827-canonical-B-normal-vector.json.gz"
    b=read(bound(work/"retained"/"R827",sources["R827"]["files"][bname]))
    assert b["complete"] is True and b["configuration"]==tags["R827"]
    assert b["canonical_free_column"]==1186 and b["original_branch"]==0 and b["prime"]==PRIME
    assert b["abstract_p_integral_original_normal_lift_certified"] is True
    assert b["all1380_original_short_coordinates_verified"] is True
    assert identity(tags["R827"]["source_identities"]["R787"])==identity(sources["R787"])
    rows=b["source_original_V5_rows"]
    assert len(rows)==DIM
    for i,ref in enumerate(rows):
        assert ref["file"]=="R787-real-power5-row-"+str(i).zfill(4)+".json.gz"
        assert ref["producer"]=="R787" and sources["R787"]["files"][ref["file"]]==plain(ref)
    inputs={}
    for key,selector in item["input_selectors"].items():
        label,name=selector["source_group"],selector["file"]
        assert label in sources and name in sources[label]["files"]
        inputs[key]={"source_group":label,**sources[label]["files"][name]}
        if "sha256" in selector:
            assert inputs[key]["sha256"]==selector["sha256"]
        if "bytes" in selector:
            assert inputs[key]["bytes"]==selector["bytes"]
    assert set(inputs)=={"canonical_coefficients","B_normal","S5_inverse","S5_matrix",
        "global_DAG","place_audit","original_chart","original_rational_blocks"}
    expanded=dict(item,sources=sources,inputs=inputs)
    expanded["method"]=str(topic_path(item["method"]))
    expanded["proofs"]={key:{**v,"path":str(topic_path(v["path"]))} for key,v in item["proofs"].items()}
    inventory={"result":RESULT,"source_identities":{label:stable_source(v) for label,v in sources.items()},
        "selected_files":{label:v["files"] for label,v in sources.items()},"actual_selected_source_count":total}
    receipt={"result":RESULT,"complete":True,"intake":item["intake"],
        "source_index":plain(item["intake"]["source_index"]),
        "summaries":{label:plain(entries[label]["summary"]) for label in SOURCES},
        "original_carriers":{label:plain(entries[label]["retained_input_bundle"]) for label in SOURCES},
        "original_source_identities":{label:stable_source(v) for label,v in sources.items()},
        "actual_selected_source_count":total,"all_selected_original_members_bytes_and_SHA_verified":True,
        "all1234_original_V5_rows_match_the_completed_B_normal_source":True,
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
            for key in ("source_audit","full1380_rhs","normal_A","normal_fraction_input","resume_state"):
                bound(out,final[key])
            shutil.copyfile(folder/FINAL,out/FINAL)
        # An old false FINAL is a historical receipt, not the restored completion state.

def compute(item,out,request,IO):
    out.mkdir(parents=True,exist_ok=True)
    work=out.parent/"R877-working";work.mkdir(parents=True,exist_ok=True)
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
            print("R877_CORE_RECEIPT="+json.dumps({k:v for k,v in cr.items()
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
            "canonical_A_normal_input_certified":bool(final and final["canonical_A_normal_input_certified"]),
            "original_global_y_normal_fraction_input_certified":bool(final and final["original_global_y_normal_fraction_input_certified"]),
            "original_five_Lj_RR128_or_144_computed":False,
            "finished_at_utc":dt.datetime.now(dt.timezone.utc).isoformat()})
        output_manifest(out)
    return code

def dimensions(value,rows,columns):
    assert isinstance(value,list) and len(value)==rows
    assert all(isinstance(v,list) and len(v)==columns for v in value)

def verify(item,out,request,IO):
    files=inspect_manifest(out)
    run=read(out/META[1])
    assert run["result"]==RESULT and run["source_commit"]==os.environ["GITHUB_SHA"]
    if META[0] not in files:
        assert run["complete"] is False and run["process_exit_code"]!=0 and run["core_receipt_sha256"] is None
        print("R877_VERIFY="+json.dumps({"complete":False,"source_preparation_failed":True,
            "all_existing_output_bytes_verified":True,"new_mathematics_executed":False}),flush=True)
        return 0
    work=out.parent/"R877-verification"
    expanded,source_receipt=prepare_sources(item,out,work)
    tag=expected_tag(expanded)
    initial=read(out/META[0])
    assert initial["result"]==RESULT and initial["source_commit"]==os.environ["GITHUB_SHA"]
    assert initial["core_sha256"]==item["core_sha256"] and initial["driver_sha256"]==item["wrapper_sha256"]
    assert initial["request_sha256"]==sha(request) and initial["job"]==item
    assert initial["actual_configuration"]==tag
    assert files[INVENTORY]==spec(out/INVENTORY) and files[RETAINED_RECEIPT]==spec(out/RETAINED_RECEIPT)
    assert initial["actual_source_inventory"]==files[INVENTORY]
    assert initial["retained_inputs"]==files[RETAINED_RECEIPT]
    complete_stages={}
    for name,ref in files.items():
        if not(name.startswith(PREFIX) and name.endswith(".json.gz")):
            continue
        value=read(out/name)
        assert value["result"]==RESULT and value["configuration"]==tag
        if name==PREFIX+"current.json.gz":
            assert value["complete"] is False and isinstance(value["status"],str)
        else:
            assert value["complete"] is True
            if not name.startswith(PREFIX+"stage-manifest-"):
                complete_stages[name]=ref
    def stage(ref):
        ref=plain(ref);assert files[ref["file"]]==ref
        value=read(bound(out,ref))
        assert value["result"]==RESULT and value["configuration"]==tag and value["complete"] is True
        return value
    core=read(out/META[2]) if META[2] in files else None
    if core is not None:
        assert core["result"]==RESULT and core["source_sha256"]==item["core_sha256"]
        assert files[META[2]]["sha256"]==run["core_receipt_sha256"]
    else:
        assert run["complete"] is False and run["core_receipt_sha256"] is None
    final=read(out/FINAL) if FINAL in files else None
    if final is not None:
        assert final["result"]==RESULT and final["configuration"]==tag
        for key in ("old_S5_matrix_inverse_and_B_conversion_recomputed",
                    "characteristic_zero_normal_coordinates_reconstructed",
                    "Galois_conjugate_normal_inputs_computed","original_five_Lj_RR128_or_144_computed",
                    "original_connection_rigidification_or_height_computed"):
            assert final[key] is False
        if final["complete"]:
            assert run["complete"] is True and run["process_exit_code"]==0 and run["error"] is None
            assert core is not None and core["complete"] is True and core["error"] is None
            assert core["certificate_sha256"]==files[FINAL]["sha256"]
            assert core["configuration"]==tag
            for key in ("canonical_A_normal_input_certified","original_global_y_normal_fraction_input_certified"):
                assert final[key] is core[key] is True
            assert final["all1380_original_short_coordinates_verified"] is True
            assert final["new_right_hand_side_count"]==1
            assert final["prime"]==PRIME and final["original_branch"]==0 and final["canonical_free_column"]==1186
            inv=stage(final["stage_manifest"])
            indexed={ref["file"]:plain(ref) for ref in inv["files"]}
            assert len(indexed)==len(inv["files"]) and indexed==complete_stages
            assert plain(final["resume_state"])==files[PREFIX+"current.json.gz"]
            audit=stage(final["source_audit"])
            assert audit["same_full_original_U1_free1186_solution_certified"] is True
            assert audit["same_original_F69_rows_and_S5_basis_certified"] is True
            assert audit["old_S5_matrix_inverse_and_B_conversion_recomputed"] is False
            for key,input_key in (("source_original_A_coefficients","canonical_coefficients"),
                 ("source_original_B_normal","B_normal"),("source_original_S5_matrix","S5_matrix"),
                 ("source_original_S5_inverse","S5_inverse"),("source_original_global_DAG","global_DAG"),
                 ("source_original_unit_chart","original_chart"),("source_original_rational_blocks","original_rational_blocks")):
                assert audit[key]==expanded["inputs"][input_key]
            assert audit["original_82power10_scale"]=="13744803133596058624"
            assert len(audit["original_real_V5_rows"])==DIM
            rhs=stage(final["full1380_rhs"])
            assert rhs["source_audit"]==final["source_audit"]
            assert rhs["new_right_hand_side_count"]==1 and rhs["matrix_shape"]==[ROWS,DIM]
            assert len(rhs["rhs_mod_prime"])==ROWS
            assert rhs["original_constant_block_retained"] is True
            assert rhs["old_B_rhs_or_original_phase_conversion_recomputed"] is False
            assert len(rhs["source_prefix_groups"])==20
            next_column=0
            for ref in rhs["source_prefix_groups"]:
                value=stage(ref)
                assert value["source_audit"]==final["source_audit"]
                first,stop=value["first_column"],value["stop_column"]
                assert first==next_column and stop==min(DIM,first+64)
                next_column=stop
                assert value["source_original_V5_rows"]==audit["original_real_V5_rows"][first:stop]
                dimensions(value["original_prefix_columns_mod_prime"],stop-first,ROWS)
                assert len(value["partial_A_rhs_mod_prime"])==ROWS
                assert len(value["source_original_A_coefficient_slice"])==stop-first
                assert value["any_B_rhs_or_old_inverse_recomputed"] is False
            assert next_column==DIM
            normal=stage(final["normal_A"])
            assert normal["source_audit"]==final["source_audit"] and normal["source_rhs"]==final["full1380_rhs"]
            assert normal["source_completed_inverse"]==expanded["inputs"]["S5_inverse"]
            assert normal["source_completed_S5_matrix"]==expanded["inputs"]["S5_matrix"]
            assert normal["normal_basis_rank"]==RANK and normal["normal_basis_degrees"]==EPS
            assert normal["normal_basis_row_mapping"]==[[i,j] for i in range(RANK) for j in range(6-EPS[i])]
            assert normal["regular_degree_bound"]==5 and len(normal["S5_coordinates_mod_prime"])==DIM
            dimensions(normal["vector_coefficients_mod_prime"],6,RANK)
            for key in ("all1380_original_short_coordinates_verified","all_weighted_support_bounds_verified",
                        "same_original_82power10_scales_preserved","abstract_p_integral_original_normal_A_lift_certified"):
                assert normal[key] is True
            assert normal["characteristic_zero_coordinates_reconstructed"] is False
            exact=normal["exact_unit_solve_expression"]
            assert exact["source_original_global_DAG"]==expanded["inputs"]["global_DAG"]
            assert exact["source_original_F69_rows"]==audit["original_real_V5_rows"]
            assert exact["source_original_A_coefficient_node"]==audit["source_original_A_coefficient_node"]
            assert exact["source_original_A_global_function_node"]==audit["source_original_normal_A_function_node"]
            assert exact["selected_unit_minor_source"]==expanded["inputs"]["S5_inverse"]
            assert exact["same_original_A_as_R849_independent_of_selected_S5_row_set"] is True
            assert exact["original_scale_applied_again"] is False
            pair=stage(final["normal_fraction_input"])
            assert pair["source_new_A_normal"]==final["normal_A"]
            assert pair["source_completed_B_normal"]==expanded["inputs"]["B_normal"]
            assert pair["source_original_global_DAG"]==expanded["inputs"]["global_DAG"]
            assert pair["original_global_y_node"]==audit["source_original_global_y_node"]
            assert pair["same_original_U1_normalization_preserved"] is True
            assert pair["global_characteristic_zero_fraction_defined_and_modular_inputs_certified"] is True
            for key in ("B_normal_conversion_recomputed","finite_fiber_B_invertibility_checked",
                        "finite_fiber_original_y_values_computed","Galois_conjugate_normal_inputs_computed",
                        "original_Lj_RR128_or_144_computed"):
                assert pair[key] is False
        else:
            assert run["complete"] is False
            # Historical false FINAL references need not describe later resumed current bytes.
    if run["complete"]:
        assert final is not None and final["complete"] is True
    print("R877_VERIFY="+json.dumps({"result":RESULT,"complete":bool(final and final["complete"]),
        "actual_selected_source_count":source_receipt["actual_selected_source_count"],
        "actual_complete_math_stage_count":len(complete_stages),
        "canonical_A_normal_input_certified":bool(final and final["canonical_A_normal_input_certified"]),
        "all1380_original_short_coordinates_verified":bool(final and final["all1380_original_short_coordinates_verified"]),
        "old_S5_matrix_inverse_or_B_recomputed":False,
        "original_five_Lj_RR128_or_144_computed":False,"new_mathematics_executed_in_verifier":False},sort_keys=True),flush=True)
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
