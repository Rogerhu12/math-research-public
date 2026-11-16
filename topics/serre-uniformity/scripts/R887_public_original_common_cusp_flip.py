#!/usr/bin/env python3
"""R887 pure-IO original source transport, resumable run and certificate verification."""
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
REQUEST=TOPIC/"notes/R887-common-cusp-flip-public-request.json"
RESULT="R887-original-common-cusp-flip-and-bounded-RR-space"
FINAL="p41-original-common-cusp-flip-and-bounded-RR-certificate.json"
PREFIX="R887-"
MANIFEST="full-outputs-manifest.json"
REFERENCE="full-outputs-manifest-reference.json"
META=("public-actions-input.json","run-receipt.json","core-receipt.json")
LEGACY_WRAPPER="R880_public_original_D_and_cusp_bounded_RR_inputs.py"
LEGACY_WRAPPER_SHA="3a888af1b0ff3339743a1369c416be0d85111562c167260637b4b0da1b52b630"
LEGACY_CORE="R880_original_D_and_cusp_bounded_RR_inputs.py"
LEGACY_CORE_SHA="ca46e8f9a9410be240ad77c0863b193e77ef701b06186a31b3edb20eb3e997a4"
IO_HELPER_SHA="c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
PARENT_RESULT="R880-original-D-and-cusp-bounded-RR-inputs"
PARENT_FINAL="p41-original-D-and-cusp-bounded-RR-inputs-certificate.json"
PARENT_BUNDLE="R887-completed-R880-selected-original-sources.tar.gz"
PARENT_FILE_INDEX="R887-completed-R880-source-files.json"
INVENTORY=PREFIX+"original-source-inventory.json"
RETAINED_RECEIPT=PREFIX+"retained-inputs-receipt.json"
BASE=("result","run_id","source_commit","core_sha256","manifest_sha256")
SOURCES=("R880","R845","R872","R827")
OLD_GROUPS=("R845","R872","R827")
PROOFS=("R887","R880","R872","R845")
INPUTS=("parent_cusp_matrix","parent_complete_cusp","parent_principal_inputs",
        "parent_source_audit","V2_jets","old_normal_index","old_rank","W_reduction","place_audit")
PRIME,RANK=1000000753,272
EPS=[0]+[1]*144+[2]*127
STRATEGY={
    "scope":"common_Cstar_full418_and_exact_Qtilde_minus1205",
    "prime":PRIME,"original_branch":0,"original_zeta_root":549966761,
    "original_s_root":99932770,"original_integral_B_root":3197390,
    "normal_basis_degrees":EPS,
    "original_divisor":"D_C=C+252P0, degree272",
    "restriction_shape":[272,418],"restriction_kernel_dimension":146,
    "new_original_Hensel_jets_computed":False,
    "u_C_selection":"first original kernel basis column with unit jet252, no rescaling",
    "second_anchor_schedule":"sum(integer_parameter^j * U_j), j=0..145",
    "fixed_u_C_products_shared_across_trials":True,
    "old_fiber_nodes":[0,1,2,3,4],"new_pencil_shape":[1360,1380],
    "required_new_pencil_rank":962,"Cstar_complete_space_dimension":418,
    "Cstar_divisor":"div_2H(u_C)-C-252P0, degree272",
    "Cstar_avoids_original_P0":True,
    "principal_function":"old_Q_f * (u_C/tau^2)",
    "principal_function_rho_order":-1205,
    "old_C_jets_normal_conversion_and_Krylov_inverses_recomputed":False,
    "exact_sources":"original characteristic-zero unit-solve expressions",
    "characteristic_zero_coefficients_reconstructed":False,
    "original_Lj_RR128_or_144_computed":False,
    "only_budget_trial_limit_and_transport_excluded_from_identity":True,
}

def sha(path):
    result=hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda:stream.read(4*1024*1024),b""):result.update(block)
    return result.hexdigest()

def fingerprint(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def read(path):
    path=Path(path)
    with (gzip.open(path,"rt",encoding="utf-8") if path.suffix==".gz" else path.open("r",encoding="utf-8")) as stream:
        return json.load(stream)

def save(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temp=path.with_name(path.name+".tmp")
    temp.write_text(json.dumps(value,sort_keys=True,separators=(",",":"))+"\n",encoding="utf-8")
    temp.replace(path)

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
    return {**identity(value),"certificate":plain(value["certificate"]) if value.get("certificate") else None,
        "configuration_stage":plain(value["configuration_stage"]) if value.get("configuration_stage") else None,
        "configuration_sha256":value["configuration_sha256"],
        "selected_file_count":value["selected_file_count"],
        "selected_files_sha256":value["selected_files_sha256"]}

def expected_tag(item):
    return {"result":RESULT,"source_sha256":item["core_sha256"],"python_flint":"0.9.0","p":41,
        "legacy_R880_core_sha256":LEGACY_CORE_SHA,"method_sha256":item["method_sha256"],
        "proofs_sha256":{key:item["proofs"][key]["sha256"] for key in PROOFS},
        "sources":{label:stable_source(item["sources"][label]) for label in SOURCES},
        "inputs":item["inputs"],"strategy":STRATEGY}

def load_IO(item):
    path=S/LEGACY_WRAPPER
    assert sha(path)==LEGACY_WRAPPER_SHA==item["legacy_wrapper_sha256"]
    assert item["legacy_wrapper"]==LEGACY_WRAPPER
    loader=importlib.util.spec_from_file_location("R887_original_stdlib_source_transport",path)
    legacy=importlib.util.module_from_spec(loader);loader.loader.exec_module(legacy)
    io=legacy.load_IO(item)
    return legacy,io

def guard(item,request):
    assert os.environ.get("GITHUB_ACTIONS")=="true"
    assert os.environ.get("GITHUB_REPOSITORY")=="Rogerhu12/math-research-public"
    assert request.resolve()==REQUEST.resolve()
    assert item["schema"]==1 and item["result"]==RESULT and item["p"]==41
    assert item["producer_inputs_pending"] is False
    assert item["wrapper"]==Path(__file__).name and sha(__file__)==item["wrapper_sha256"]
    assert item["core"]=="R887_original_common_cusp_flip.py"
    assert sha(S/item["core"])==item["core_sha256"]
    assert item["legacy_core"]==LEGACY_CORE and item["legacy_core_sha256"]==LEGACY_CORE_SHA
    assert sha(S/LEGACY_CORE)==LEGACY_CORE_SHA
    assert sha(topic_path(item["method"]))==item["method_sha256"]
    assert set(item["proofs"])==set(PROOFS)
    for proof in item["proofs"].values():assert sha(topic_path(proof["path"]))==proof["sha256"]
    assert sha(REPO/"README.md")==item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md")==item["readme_sha256"]["topic"]
    assert 0<item["budget_minutes"]<=300 and item["maximum_trials"]>=1
    assert item["resume"] is None or isinstance(item["resume"],dict)
    assert set(item["input_selectors"])==set(INPUTS)
    parent=item["parent_source"]
    assert parent["result"]==PARENT_RESULT and parent["core_sha256"]==LEGACY_CORE_SHA
    assert parent["wrapper_sha256"]==LEGACY_WRAPPER_SHA and parent["expected_conclusion"]=="success"
    assert parent["files"][MANIFEST]["sha256"]==parent["manifest_sha256"]
    assert parent["files"][PARENT_FINAL]==plain(parent["certificate"])
    assert len(parent["files"])==parent["selected_file_count"]
    return load_IO(item)

def output_manifest(out):
    entries=[{**spec(p),"included_in_git":False} for p in sorted(out.iterdir())
        if p.is_file() and p.name not in (MANIFEST,REFERENCE) and not p.name.endswith(".tmp")]
    save(out/MANIFEST,{"result":RESULT,"files":entries,"temporary_active_checkpoint_retention_days":1,
        "reproducible_data_in_git_or_release":False})
    save(out/REFERENCE,{"result":RESULT,**spec(out/MANIFEST)})

def inspect_manifest(out):
    value=read(out/MANIFEST);assert value["result"]==RESULT
    files={x["file"]:plain(x) for x in value["files"]};assert len(files)==len(value["files"])
    actual={p.name for p in out.iterdir() if p.is_file() and p.name not in (MANIFEST,REFERENCE)
        and not p.name.endswith(".tmp")}
    assert actual==set(files)
    for ref in files.values():bound(out,ref)
    reference=read(out/REFERENCE)
    assert reference["result"]==RESULT and plain(reference)==spec(out/MANIFEST)
    return files

def pack_parent(target,directory,files):
    temporary=target.with_name(target.name+".tmp")
    with temporary.open("wb") as raw:
        with gzip.GzipFile(fileobj=raw,mode="wb",mtime=0,compresslevel=2) as zipped:
            with tarfile.open(fileobj=zipped,mode="w|") as archive:
                for name,ref in sorted(files.items()):
                    path=bound(directory,ref);info=tarfile.TarInfo("original/"+name)
                    info.size=ref["bytes"];info.mode=0o644;info.mtime=0;info.uid=0;info.gid=0
                    with path.open("rb") as stream:archive.addfile(info,stream)
    temporary.replace(target)

def fetch_sources(item,out,work,IO):
    source=item["parent_source"]
    archive=IO.Archive(source,work/"parent-transport",whole=False)
    folder=work/"parent-selected";folder.mkdir(parents=True,exist_ok=True)
    try:
        files={name:plain(x) for name,x in source["files"].items()}
        for name in (MANIFEST,REFERENCE):
            ref=files[name];archive.extract_bound(name,ref["sha256"],folder/name,ref["bytes"])
        manifest=read(folder/MANIFEST);assert manifest["result"]==PARENT_RESULT
        indexed={x["file"]:plain(x) for x in manifest["files"]}
        assert len(indexed)==len(manifest["files"])==source["manifest_file_count"]
        assert set(archive.by_name)==set(indexed)|{MANIFEST,REFERENCE}
        reference=read(folder/REFERENCE)
        assert reference["result"]==PARENT_RESULT and plain(reference)==files[MANIFEST]
        wanted=[]
        for name,ref in files.items():
            if name in (MANIFEST,REFERENCE):continue
            assert indexed[name]==ref
            wanted.append((name,ref["sha256"],folder/name,ref["bytes"]))
        archive.extract_many(wanted)
        initial=read(folder/META[0]);run=read(folder/META[1])
        assert initial["source_commit"]==run["source_commit"]==source["source_commit"]
        assert str(run["workflow_run_id"])==str(source["run_id"])
        assert initial["core_sha256"]==LEGACY_CORE_SHA and initial["driver_sha256"]==LEGACY_WRAPPER_SHA
        oldjob=initial["job"]
        intake=oldjob["intake"];iref=plain(intake["source_index"])
        assert indexed[iref["file"]]==iref
        archive.extract_bound(iref["file"],iref["sha256"],out/iref["file"],iref["bytes"])
        index=read(out/iref["file"])
        assert index["schema"]==1 and index["errors"]==[] and index["new_mathematics_executed"] is False
        assert index["source_commit"]==intake["source_commit"]
        assert str(index["workflow_run_id"])==str(intake["run_id"])
        assert index["request_sha256"]==intake["request_sha256"]
        entries={x["label"]:x for x in index["sources"]}
        assert len(entries)==len(index["sources"])==6
        selected=[]
        for label in OLD_GROUPS:
            entry=entries[label]
            for key in ("summary","retained_input_bundle"):
                ref=plain(entry[key]);assert indexed[ref["file"]]==ref
                selected.append((ref["file"],ref["sha256"],out/ref["file"],ref["bytes"]))
            assert plain(entry["retained_input_bundle"])==plain(intake["bundles"][label])
        archive.extract_many(selected)
        pack_parent(out/PARENT_BUNDLE,folder,files)
        save(out/PARENT_FILE_INDEX,{"result":RESULT,"original_parent":identity(source),
            "files":files,"selected_file_count":len(files),
            "selected_files_sha256":fingerprint(files),"parent_source_bundle":spec(out/PARENT_BUNDLE),
            "original_parent_manifest":files[MANIFEST],"original_944_source_identity_not_changed":True})
        return archive.receipt()
    finally:archive.close()

def prepare_sources(item,out,work,legacy):
    source=item["parent_source"]
    listing=read(out/PARENT_FILE_INDEX)
    assert listing["result"]==RESULT and listing["original_parent"]==identity(source)
    files={name:plain(x) for name,x in listing["files"].items()}
    assert files==source["files"] and len(files)==listing["selected_file_count"]==source["selected_file_count"]
    assert fingerprint(files)==listing["selected_files_sha256"]
    parent_folder=work/"retained"/"R880"
    legacy.unpack_source(bound(out,listing["parent_source_bundle"]),parent_folder,files)
    parent=dict(source,directory=str(parent_folder),files=files,
        configuration_stage=None,selected_files_sha256=fingerprint(files))
    parent_tag=legacy.review_original("R880",parent)
    initial=read(parent_folder/META[0]);oldjob=initial["job"]
    assert parent_tag==initial["actual_configuration"]
    final=read(bound(parent_folder,parent["certificate"]))
    assert final["complete"] is True and final["actual_new_pencil_rank"]==962
    for flag in ("actual_complete_common_cusp_418_space_certified",
                 "actual_complete_Dstar_418_space_certified","actual_original_Qf_principal_identity_certified"):
        assert final[flag] is True
    intake=oldjob["intake"]
    index=read(bound(out,intake["source_index"]))
    assert index["source_commit"]==intake["source_commit"]
    assert str(index["workflow_run_id"])==str(intake["run_id"])
    assert index["request_sha256"]==intake["request_sha256"] and index["errors"]==[]
    entries={x["label"]:x for x in index["sources"]}
    assert len(entries)==len(index["sources"])==6
    sources={"R880":parent};tags={"R880":parent_tag};old_total=0
    carrier_refs={}
    for label in OLD_GROUPS:
        raw=oldjob["sources"][label];entry=entries[label]
        for key in ("run_id","source_commit","core_sha256","manifest_sha256"):
            assert str(entry["source"][key])==str(raw[key])
        summary=read(bound(out,entry["summary"]))
        assert summary["source"]==entry["source"] and summary["label"]==label
        assert summary["original_result"]==raw["result"] and summary["new_mathematics_executed"] is False
        assert summary["manifest"]["sha256"]==raw["manifest_sha256"]
        assert summary["original_manifest_count"]==raw["manifest_file_count"]
        assert summary["source_core_sha256"]==raw["core_sha256"]
        assert summary["source_wrapper_sha256"]==raw["wrapper_sha256"]
        bspec=plain(entry["retained_input_bundle"])
        assert bspec==plain(summary["retained_input_bundle"])==plain(intake["bundles"][label])
        originals={name:plain(x) for name,x in summary["selected_files"].items()}
        assert len(originals)==summary["selected_file_count"]==raw["selected_math_and_metadata_count"]
        originals[MANIFEST]=plain(summary["manifest"]);originals[REFERENCE]=plain(summary["manifest_reference"])
        assert len(originals)==raw["expected_selected_file_count"]
        for name,pin in raw["file_pins"].items():assert originals[name]==plain(pin)
        directory=work/"retained"/label
        legacy.unpack_source(bound(out,bspec),directory,originals)
        certificate=originals[raw["certificate_name"]] if raw["certificate_name"] else None
        anchor=originals[raw["configuration_stage_name"]] if raw["configuration_stage_name"] else None
        value=dict(raw,directory=str(directory),files=originals,certificate=certificate,
            configuration_stage=anchor,selected_file_count=len(originals),selected_files_sha256=fingerprint(originals))
        tags[label]=legacy.review_original(label,value)
        assert stable_source(value)==parent_tag["sources"][label]
        sources[label]=value;old_total+=len(originals);carrier_refs[label]=bspec
    assert old_total==370 and set(sources)==set(SOURCES)
    inputs={}
    for key,selector in item["input_selectors"].items():
        label,name=selector["source_group"],selector["file"]
        assert label in sources and name in sources[label]["files"]
        inputs[key]={"source_group":label,**sources[label]["files"][name]}
        for k in ("bytes","sha256"):
            if k in selector:assert inputs[key][k]==selector[k]
        value=read(bound(sources[label]["directory"],inputs[key]))
        assert value["configuration"]==tags[label] and value["complete"] is True
        if "result" in value:assert value["result"]==sources[label]["result"]
    assert set(inputs)==set(INPUTS)
    for field,key in (("source_audit","parent_source_audit"),
                      ("common_cusp_constraint_matrix","parent_cusp_matrix"),
                      ("complete_common_cusp_418_kernel","parent_complete_cusp"),
                      ("original_D_cusp_chi_principal_inputs","parent_principal_inputs")):
        assert plain(final[field])==plain(inputs[key])
    parent_principal=read(bound(parent_folder,inputs["parent_principal_inputs"]))
    dstar=plain(parent_principal["source_complete_Dstar_418_space"])
    assert files[dstar["file"]]==dstar
    dchi=parent_principal["source_complete_D_chi_418_space"]
    assert dchi["source_group"]=="R872" and sources["R872"]["files"][dchi["file"]]==plain(dchi)
    expanded=dict(item,sources=sources,inputs=inputs)
    expanded["method"]=str(topic_path(item["method"]))
    expanded["proofs"]={key:{**value,"path":str(topic_path(value["path"]))} for key,value in item["proofs"].items()}
    total=sum(value["selected_file_count"] for value in sources.values())
    save(out/INVENTORY,{"result":RESULT,"source_identities":{k:stable_source(v) for k,v in sources.items()},
        "selected_files":{k:v["files"] for k,v in sources.items()},
        "actual_selected_source_count":total,"prior_R880_944_source_identity_unchanged":True})
    transport_files=[spec(out/PARENT_FILE_INDEX),plain(listing["parent_source_bundle"]),plain(intake["source_index"])]
    for label in OLD_GROUPS:
        transport_files.extend([plain(entries[label]["summary"]),carrier_refs[label]])
    receipt={"result":RESULT,"complete":True,"parent_source":identity(parent),
        "parent_source_bundle":plain(listing["parent_source_bundle"]),
        "transport_files":transport_files,"original_carriers":carrier_refs,
        "actual_selected_source_count":total,"original_old_three_group_count":old_total,
        "source_identities":{k:stable_source(v) for k,v in sources.items()},
        "all_selected_original_member_bytes_and_SHA_verified":True,
        "R820_R842_R849_carriers_not_retransported":True,
        "new_mathematics_executed":False}
    save(out/RETAINED_RECEIPT,receipt)
    return expanded,receipt


def restore_archive(item,out,work,IO):
    source=item["resume"]
    if source is None:return None
    assert source["result"]==RESULT and source["core_sha256"]==item["core_sha256"]
    assert source["wrapper_sha256"]==item["wrapper_sha256"]
    archive=IO.Archive(source,work/"resume-transport",whole=True)
    folder=work/"previous-output";folder.mkdir(parents=True,exist_ok=True)
    try:
        ms=plain(source["manifest"])
        archive.extract_bound(MANIFEST,ms["sha256"],folder/MANIFEST,ms["bytes"])
        manifest=read(folder/MANIFEST);assert manifest["result"]==RESULT
        files={x["file"]:plain(x) for x in manifest["files"]}
        assert len(files)==len(manifest["files"])
        assert set(archive.by_name)==set(files)|{MANIFEST,REFERENCE}
        archive.extract_many([(name,ref["sha256"],folder/name,ref["bytes"]) for name,ref in files.items()])
        values=archive.by_name[REFERENCE]
        assert len(values)==1 and values[0].file_size<1000000
        (folder/REFERENCE).write_bytes(archive.zip.read(values[0]))
        reference=read(folder/REFERENCE)
        assert reference["result"]==RESULT and plain(reference)==ms
        initial=read(folder/META[0]);run=read(folder/META[1])
        assert initial["result"]==run["result"]==RESULT
        assert initial["source_commit"]==run["source_commit"]==source["source_commit"]
        assert str(run["workflow_run_id"])==str(source["run_id"])
        assert initial["core_sha256"]==item["core_sha256"] and initial["driver_sha256"]==item["wrapper_sha256"]
        if run.get("core_receipt_sha256") is not None:
            assert files[META[2]]["sha256"]==run["core_receipt_sha256"]
            core=read(folder/META[2])
            assert core["result"]==RESULT and core["source_sha256"]==item["core_sha256"]
        else:assert run["complete"] is False
        retained=read(folder/RETAINED_RECEIPT)
        assert retained["result"]==RESULT and retained["complete"] is True
        for ref in retained["transport_files"]:
            ref=plain(ref);assert files[ref["file"]]==ref
            target=out/ref["file"]
            if target.exists():assert spec(target)==ref
            else:shutil.copyfile(bound(folder,ref),target)
        return {"folder":folder,"files":files,"initial":initial,"run":run,"transport":archive.receipt()}
    finally:archive.close()

def restore_stages(previous,tag,out):
    if previous is None:return
    assert previous["initial"]["actual_configuration"]==tag
    folder,files=previous["folder"],previous["files"]
    for name,ref in files.items():
        if not (name.startswith(PREFIX) and name.endswith(".json.gz")):continue
        value=read(folder/name)
        assert value["result"]==RESULT and value["configuration"]==tag
        assert value["complete"] is (name!=PREFIX+"current.json.gz")
        target=out/name
        if target.exists():assert spec(target)==ref
        else:shutil.copyfile(folder/name,target)
    if FINAL in files:
        final=read(folder/FINAL)
        assert final["result"]==RESULT and final["configuration"]==tag
        if final["complete"] is True:
            assert previous["run"]["complete"] is True
            inventory=read(bound(folder,final["stage_manifest"]))
            assert inventory["result"]==RESULT and inventory["configuration"]==tag and inventory["complete"] is True
            for ref in inventory["files"]:
                assert files[ref["file"]]==plain(ref);bound(out,ref)
            for key in ("source_audit","restriction","complete_U_C_146","u_C","accepted_profile",
                        "accepted_v_C","complete_Cstar_418","original_principal_inputs","resume_state"):
                bound(out,final[key])
            shutil.copyfile(folder/FINAL,out/FINAL)
        # A previous false FINAL is historical and never constrains a later current.

def compute(item,out,request,legacy,IO):
    out.mkdir(parents=True,exist_ok=True)
    work=out.parent/"R887-working";work.mkdir(parents=True,exist_ok=True)
    code=1;error=None;outer=False;expanded=None;tag=None
    try:
        previous=restore_archive(item,out,work,IO)
        transport=previous["transport"] if previous else fetch_sources(item,out,work,IO)
        expanded,receipt=prepare_sources(item,out,work,legacy)
        tag=expected_tag(expanded);restore_stages(previous,tag,out)
        config=work/"expanded-job.json";save(config,expanded)
        save(out/META[0],{"result":RESULT,"source_commit":os.environ["GITHUB_SHA"],
            "workflow_run_id":os.environ["GITHUB_RUN_ID"],"workflow_attempt":os.environ.get("GITHUB_RUN_ATTEMPT","1"),
            "core_sha256":item["core_sha256"],"driver_sha256":item["wrapper_sha256"],
            "legacy_R880_core_sha256":LEGACY_CORE_SHA,"legacy_R880_stdlib_wrapper_sha256":LEGACY_WRAPPER_SHA,
            "request_sha256":sha(request),"job":item,"actual_configuration":tag,
            "actual_source_inventory":spec(out/INVENTORY),"retained_inputs":spec(out/RETAINED_RECEIPT),
            "transport":transport,"root_readme_sha256":item["readme_sha256"]["root"],
            "topic_readme_sha256":item["readme_sha256"]["topic"],
            "execution_environment":"public-repository-github-actions"})
        command=[sys.executable,"-u",str(S/item["core"]),"--config",str(config),
            "--out",str(out),"--budget-minutes",str(item["budget_minutes"])]
        with (out/"core.log").open("ab",buffering=0) as log:
            child=subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
            try:code=child.wait(timeout=60*item["budget_minutes"]+180)
            except subprocess.TimeoutExpired:
                outer=True;code=124;os.killpg(child.pid,signal.SIGTERM)
                try:child.wait(timeout=15)
                except subprocess.TimeoutExpired:
                    os.killpg(child.pid,signal.SIGKILL);child.wait()
        if code<0:code=128-code
        if (out/"core.log").exists():
            for line in (out/"core.log").read_text(errors="replace").splitlines()[-18:]:
                if len(line)<=2000:print(line,flush=True)
        if (out/META[2]).exists():
            print("R887_CORE_RECEIPT="+json.dumps(read(out/META[2]),sort_keys=True),flush=True)
    except BaseException as exc:
        traceback.print_exc();error={"type":type(exc).__name__,"message":str(exc)};code=1
    finally:
        core=read(out/META[2]) if (out/META[2]).exists() else None
        final=read(out/FINAL) if (out/FINAL).exists() else None
        complete=bool(code==0 and core and core["complete"] and final and final["complete"])
        save(out/META[1],{"result":RESULT,"p":41,"complete":complete,
            "process_exit_code":code,"error":error,"outer_timeout":outer,
            "source_commit":os.environ["GITHUB_SHA"],"workflow_run_id":os.environ["GITHUB_RUN_ID"],
            "workflow_attempt":os.environ.get("GITHUB_RUN_ATTEMPT","1"),
            "core_receipt_sha256":sha(out/META[2]) if core else None,
            "complete_U_C_146_certified":bool(final and final["complete_U_C_146_certified"]),
            "original_u_C_order252_certified":bool(final and final["original_u_C_order252_certified"]),
            "complete_Cstar_418_certified":bool(final and final["complete_Cstar_418_certified"]),
            "original_Qtilde_order_minus1205_certified":bool(final and final["original_Qtilde_order_minus1205_certified"]),
            "five_original_Lj_RR128_or_144_computed":False,
            "finished_at_utc":dt.datetime.now(dt.timezone.utc).isoformat()})
        output_manifest(out)
    return code

def dimensions(value,height,width):
    assert isinstance(value,list) and len(value)==height
    assert all(isinstance(row,list) and len(row)==width for row in value)

def verify(item,out,request,legacy,IO):
    files=inspect_manifest(out);run=read(out/META[1])
    assert run["result"]==RESULT and run["source_commit"]==os.environ["GITHUB_SHA"]
    if META[0] not in files:
        assert run["complete"] is False and run["process_exit_code"]!=0 and run["core_receipt_sha256"] is None
        print("R887_VERIFY="+json.dumps({"complete":False,"source_preparation_failed":True,
            "all_existing_output_bytes_verified":True,"new_mathematics_executed":False}),flush=True)
        return 0
    expanded,receipt=prepare_sources(item,out,out.parent/"R887-verification",legacy)
    tag=expected_tag(expanded);initial=read(out/META[0])
    assert initial["result"]==RESULT and initial["source_commit"]==os.environ["GITHUB_SHA"]
    assert initial["core_sha256"]==item["core_sha256"] and initial["driver_sha256"]==item["wrapper_sha256"]
    assert initial["legacy_R880_core_sha256"]==LEGACY_CORE_SHA
    assert initial["legacy_R880_stdlib_wrapper_sha256"]==LEGACY_WRAPPER_SHA
    assert initial["request_sha256"]==sha(request) and initial["job"]==item
    assert initial["actual_configuration"]==tag
    assert initial["actual_source_inventory"]==files[INVENTORY]==spec(out/INVENTORY)
    assert initial["retained_inputs"]==files[RETAINED_RECEIPT]==spec(out/RETAINED_RECEIPT)
    def resolve(ref):
        ref0=plain(ref)
        if "source_group" in ref:
            label=ref["source_group"];assert label in expanded["sources"]
            source=expanded["sources"][label]
            assert source["files"][ref0["file"]]==ref0
            return bound(source["directory"],ref0)
        assert files[ref0["file"]]==ref0
        return bound(out,ref0)
    def visit(value):
        if isinstance(value,dict):
            if all(key in value for key in ("file","bytes","sha256")):
                resolve(value)
            else:
                for part in value.values():visit(part)
        elif isinstance(value,list):
            for part in value:visit(part)
    complete_stages={}
    current_name=PREFIX+"current.json.gz";inventory_name=PREFIX+"exact-stages-manifest.json.gz"
    for name,ref in files.items():
        if not (name.startswith(PREFIX) and name.endswith(".json.gz")):continue
        value=read(out/name)
        assert value["result"]==RESULT and value["configuration"]==tag
        if name==current_name:
            assert value["complete"] is False
            visit(value.get("references",{}));continue
        assert value["complete"] is True
        if name==inventory_name:continue
        complete_stages[name]=ref
        for key,part in value.items():
            if key!="configuration":visit(part)
        if name==PREFIX+"original-418-column-restriction.json.gz":
            assert value["matrix_shape"]==[272,418]
            dimensions(value["matrix_mod_prime"],272,418)
            assert len(value["selected_original_V3_columns"])==418
            assert value["tau_embedding_no_additional_scale"] is True
            assert value["old_constraints_only_selected_not_recomputed"] is True
        elif name==PREFIX+"complete-U_C-146-kernel.json.gz" and value["accepted"]:
            assert value["actual_rank_mod_prime"]==272 and value["actual_kernel_dimension"]==146
            dimensions(value["kernel_basis_mod_prime"],418,146)
            dimensions(value["inverse_selected_minor_mod_prime"],272,272)
            assert value["both_selected_inverse_products_verified"] is True
            assert value["all_original_equations_verified"] is True
            assert value["free_normalization_identity_verified"] is True
            assert value["full_characteristic_zero_kernel_certified"] is True
        elif name==PREFIX+"original-order252-functional-and-u_C.json.gz" and value["accepted"]:
            assert value["original_jet_order"]==252 and len(value["order252_coefficients_mod_prime"])==146
            assert 0<=value["selected_first_unit_column"]<146
            assert value["actual_order252_unit_mod_prime"]!=0
            dimensions(value["u_C_normal_V2_coordinates_mod_prime"],418,1)
            assert value["Cstar_degree"]==272 and value["Cstar_avoids_original_P0"] is True
            assert value["selected_exact_section"]["additional_rescaling"] is False
        elif "product_evaluation_matrix_mod_prime" in value:
            dimensions(value["product_evaluation_matrix_mod_prime"],272,690)
            assert len(value["normal_section_evaluation_mod_prime"])==272
            assert value["source_K_inverse_V3_reused"] is True
            assert value["old_source_arithmetic_recomputed"] is False
        elif name.endswith("-complete-pencil-profile.json.gz"):
            assert value["matrix_shape"]==[1360,1380] and value["required_rank"]==962
            assert 0<=value["actual_rank"]<=962
            assert value["accepted"] is (value["actual_rank"]==962)
            if value["accepted"]:
                assert len(value["selected_rows"])==len(value["selected_columns"])==962
                assert value["image_is_complete_H0_5H_minus_D_C"] is True
                assert value["finite_evaluation_injective_on_the_complete_original_image"] is True
        elif name.endswith("-selected-inverse.json.gz") and value["accepted"]:
            assert len(value["selected_rows"])==len(value["selected_columns"])==962
            dimensions(value["inverse_mod_prime"],962,962)
            assert value["both_inverse_products_verified"] is True
        elif name.endswith("-new-962-complete-kernel.json.gz"):
            assert value["matrix_shape"]==[1360,1380] and value["actual_rank"]==962
            assert value["actual_kernel_dimension"]==418
            dimensions(value["kernel_basis_mod_prime"],1380,418)
            assert value["all_original_fiber_equations_verified"] is True
            assert value["free_normalization_identity_verified"] is True
            assert value["full_characteristic_zero_kernel_certified"] is True
        elif name.endswith("-Cstar-projected-original-V3-basis.json.gz") and value["accepted"]:
            assert value["actual_projected_rank"]==418 and value["matrix_shape"]==[690,418]
            dimensions(value["original_V3_basis_mod_prime"],690,418)
            dimensions(value["normal_V3_basis_mod_prime"],690,418)
            assert value["complete_RR_space_certified"] is True
            assert value["exact_RR_space"]["P0_not_in_Cstar"] is True
        elif name==PREFIX+"original-Cstar-and-Qtilde-principal-inputs.json.gz":
            assert value["Cstar_degree"]==272 and value["Cstar_avoids_original_P0"] is True
            assert value["actual_rho_order"]==-1205 and value["actual_leading_coefficient_mod_prime"]!=0
            assert value["ideal_principal_factor_direction"]=="positive multiplication by Qtilde"
            assert value["complete_Cstar_418_certified"] is True
            assert value["original_Qtilde_order_minus1205_certified"] is True
            assert value["all_three_effective_degree272_representatives_avoid_original_P0"] is True
            assert value["original_Cstar_and_qC_are_fixed_by_L_over_K_Galois_action"] is True
            assert value["original_t_frame_value_computed"] is False
            assert value["five_original_Lj_RR128_or_144_computed"] is False
            assert value["connection_Poincare_period_or_height_computed"] is False
    if META[2] in files:
        core=read(out/META[2])
        assert run["core_receipt_sha256"]==files[META[2]]["sha256"]
        assert core["result"]==RESULT and core["source_sha256"]==item["core_sha256"]
        assert core["configuration_sha256"] in (None,fingerprint(tag))
        assert core["exit_code"]==run["process_exit_code"]
    else:
        assert run["core_receipt_sha256"] is None and run["complete"] is False
        core=None
    final=read(out/FINAL) if FINAL in files else None
    if final is not None:
        assert final["result"]==RESULT and final["configuration"]==tag
        assert final["p"]==41 and final["prime"]==PRIME
        assert final["five_original_Lj_RR128_or_144_computed"] is False
        assert final["connection_Poincare_period_or_height_computed"] is False
        assert final["characteristic_zero_RR_coefficients_reconstructed"] is False
        assert final["original_t_frame_value_computed"] is False
        assert final["new_original_Hensel_jets_computed"] is False
        if final["complete"] is True:
            assert core is not None and core["complete"] is True
            assert core["certificate_sha256"]==files[FINAL]["sha256"]
            assert final["actual_pencil_rank"]==962
            for flag in ("complete_U_C_146_certified","original_u_C_order252_certified",
                         "complete_Cstar_418_certified","original_Qtilde_order_minus1205_certified"):
                assert final[flag] is True and core[flag] is True and run[flag] is True
            assert run["complete"] is True and run["process_exit_code"]==0 and run["error"] is None
            for key in ("source_audit","restriction","complete_U_C_146","u_C","accepted_profile",
                        "accepted_v_C","complete_Cstar_418","original_principal_inputs","stage_manifest","resume_state"):
                resolve(final[key])
            inventory=read(out/final["stage_manifest"]["file"])
            assert inventory["configuration"]==tag and inventory["result"]==RESULT and inventory["complete"] is True
            actual={x["file"]:plain(x) for x in inventory["files"]}
            assert len(actual)==len(inventory["files"]) and actual==complete_stages
            principal=read(out/final["original_principal_inputs"]["file"])
            assert principal["source_complete_Cstar_418"]==final["complete_Cstar_418"]
            assert principal["source_exact_u_C"]==final["u_C"]
        else:
            assert run["complete"] is False and run["process_exit_code"]!=0
            # An interrupted false FINAL may precede newer complete stages/current.
    else:assert run["complete"] is False
    if run["complete"]:assert final is not None and final["complete"] is True
    summary={"result":RESULT,"complete":bool(final and final["complete"]),
        "actual_selected_source_count":receipt["actual_selected_source_count"],
        "actual_complete_math_stage_count":len(complete_stages),
        "complete_U_C_146_certified":bool(final and final["complete_U_C_146_certified"]),
        "original_u_C_order252_certified":bool(final and final["original_u_C_order252_certified"]),
        "complete_Cstar_418_certified":bool(final and final["complete_Cstar_418_certified"]),
        "original_Qtilde_order_minus1205_certified":bool(final and final["original_Qtilde_order_minus1205_certified"]),
        "actual_pencil_rank":final.get("actual_pencil_rank") if final else None,
        "R820_R842_R849_carriers_not_retransported":True,
        "new_mathematics_executed_in_verifier":False}
    print("R887_VERIFY="+json.dumps(summary,sort_keys=True),flush=True)
    return 0

def main():
    sys.set_int_max_str_digits(0)
    parser=argparse.ArgumentParser();parser.add_argument("command",choices=("compute","verify"))
    parser.add_argument("--request",required=True);parser.add_argument("--output",required=True)
    args=parser.parse_args();request=Path(args.request).resolve();out=Path(args.output).resolve()
    item=read(request);legacy,io=guard(item,request)
    if args.command=="compute":return compute(item,out,request,legacy,io)
    return verify(item,out,request,legacy,io)

if __name__=="__main__":
    raise SystemExit(main())
