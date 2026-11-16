#!/usr/bin/env python3
"""R879 standard-library source selection, same-core recovery and public runner."""
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
RESULT="R879-original-reference-pole254-pencil"
FINAL="p41-original-reference-pole254-pencil-certificate.json"
PREFIX="R879-reference-"
CORE="R879_original_reference_pole254_function.py"
REQUEST=TOPIC/"notes/R879-reference-pole254-public-request.json"
MANIFEST="full-outputs-manifest.json"
REFERENCE="full-outputs-manifest-reference.json"
BUNDLE="R879-retained-R872-inputs.tar.gz"
INVENTORY="R879-original-source-inventory.json"
INPUT_RECEIPT="R879-retained-inputs-receipt.json"
EXPANDED="R879-expanded-job.json"
META=("public-actions-input.json","run-receipt.json","core-receipt.json")
BASE=("result","run_id","source_commit","core_sha256","manifest_sha256")
SOURCE_RESULT="R872-original-P0-jets-and-fixed-Picard-RR-spaces"
SOURCE_CORE="0e5897512a2f45baaed9cd1b6b2badcb6bf6ee2b100fcd45db871ad9f6db1874"
RANGE_FILE="R824_public_original_global_polar_generators.py"
RANGE_SHA="c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
INPUT_FIELDS={
    "source_audit":"source_audit",
    "point_linearization":"point_linearization",
    "V2_jets":"original_V2_jet_matrix",
    "V2_point_kernel":"complete_original_146_kernel",
    "anchor_u":"anchor_u",
    "anchor_b":"accepted_anchor_b",
    "pencil_profile":"accepted_pencil_profile",
    "paired_kernel":"complete_fixed_chi_418_kernel",
    "fixed_divisor":"fixed_chi_divisor_and_principal_function"}
P=1000000753
ROOT=549966761
EPS=[0]+[1]*144+[2]*127
IO=None
STRATEGY = {
    "original_curve": "original genus127 Y at p41 with the original minus3 descent",
    "original_point": "original P0, finite tau chart",
    "source_exact_leaves": "completed R872 characteristic-zero unit-solve expressions",
    "coefficient_field": "K=Q(zeta); zeta^2+zeta+1=0",
    "prime": P, "original_zeta_root": ROOT,
    "normal_basis_degrees": EPS,
    "normal_basis_order": "normal row first, increasing z power",
    "V2_dimension": 418, "V3_dimension": 690,
    "source_paired_kernel_dimension": 418,
    "source_relation": "u*T(c)+b*S(c)=0 in original V5",
    "high_rows": "one z^(3-epsilon_i) row for each original normal row",
    "constraint_row_order": "272 S-high;272 T-high;J0*S-low through J18*S-low",
    "system_shape": [563,418], "exact_rank": 291,
    "right_hand_side": "zero at rows0..561 and one at row562",
    "row_profile": "left-to-right pivots of transpose",
    "column_profile": "left-to-right pivots in selected rows",
    "unselected_coordinates": "all127 free coordinates zero",
    "reference_function": "(S(c)/tau)/u",
    "paired_function_identity": "f/u=-g/b; u*g+b*f=0",
    "unique_pole": {"point":"P0","order":254},
    "reference_pencil": ["1","v0"],
    "reference_128_basis_computed": False,
    "new_pencil_672_minor_needed": False,
    "original_t_frame_scalar": "(leading_coefficient(t/x))^254 / U272",
    "original_t_frame_scalar_expanded": False,
    "old_jets_kernel_products_or_inverse_recomputed": False,
    "characteristic_zero_coefficients_reconstructed": False,
    "old_large_source_carrier_needed_for_this_finite_scope": False,
    "budget_and_transport_excluded_from_identity": True,
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
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),
                                     ensure_ascii=False).encode()).hexdigest()

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
            "certificate":plain(source["certificate"]),
            "selected_file_count":len(source["files"]),
            "selected_files_sha256":fingerprint(source["files"])}

def expected_tag(item,source,inputs):
    return {"result":RESULT,"source_sha256":item["core_sha256"],"p":41,
            "python_flint":"0.9.0","method_sha256":item["method_sha256"],
            "proofs":{k:{q:v[q] for q in ("path","sha256")} for k,v in item["proofs"].items()},
            "source_R872":identity(source),"inputs":inputs,"strategy":STRATEGY}

def load_io():
    global IO
    path=S/RANGE_FILE
    assert sha(path)==RANGE_SHA
    description=importlib.util.spec_from_file_location("R879_frozen_standard_library_Range",path)
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
    assert set(item["input_pins"])==set(INPUT_FIELDS)
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
    assert run["complete"] is True and run["process_exit_code"]==0 and run["error"] is None
    assert core["complete"] is True and core["error"] is None
    assert run["core_receipt_sha256"]==entries["core-receipt.json"]["sha256"]
    certspec=plain(source["certificate"])
    assert entries[certspec["file"]]==certspec
    cert=read(bound(folder,certspec))
    assert cert["result"]==SOURCE_RESULT and cert["complete"] is True
    assert core["certificate_sha256"]==certspec["sha256"]
    tag=cert["configuration"]
    assert tag["result"]==SOURCE_RESULT and tag["source_sha256"]==SOURCE_CORE
    assert tag["normal_basis_degrees"]==EPS
    if "actual_configuration" in initial:
        assert initial["actual_configuration"]==tag
    if "configuration_sha256" in source:
        assert fingerprint(tag)==source["configuration_sha256"]
    return cert,tag

def source_review(folder,source,inputs):
    entries=entry_map(folder,source)
    cert,tag=metadata(folder,source,entries)
    assert fingerprint(tag)==source["configuration_sha256"]
    for name,row in source["files"].items():
        assert row==entries[name] and row["file"]==name
        path=bound(folder,row)
        if name.endswith(".json.gz"):
            value=read(path)
            assert value["result"]==SOURCE_RESULT and value["complete"] is True
            assert value["configuration"]==tag
    assert set(inputs)==set(INPUT_FIELDS)
    assert all(plain(cert[right])==plain(inputs[left]) for left,right in INPUT_FIELDS.items())
    assert cert["actual_pencil_rank"]==962 and cert["accepted_pencil_trial"]==1
    for key in ("actual_original_P0_local_parameter_certified",
                "actual_original_P0_jets_through_order272_computed",
                "actual_original_complete_146_kernel_certified",
                "actual_fixed_chi_complete_418_RR_space_certified",
                "characteristic_zero_sources_are_exact_unit_solve_expressions"):
        assert cert[key] is True
    assert cert["characteristic_zero_jet_or_RR_coefficients_reconstructed"] is False
    audit=read(bound(folder,inputs["source_audit"]))
    assert audit["prime"]==P and audit["original_zeta_root"]==ROOT
    assert audit["chosen_parameter_derivative_is_a_unit"] is True
    paired=read(bound(folder,inputs["paired_kernel"]))
    assert paired["actual_kernel_dimension"]==418
    assert paired["exact_full_characteristic_zero_W_Dchi_certified"] is True
    assert paired["all1234_by418_complete_V5_relations_zero"] is True
    assert paired["all544_by418_quotient_residuals_zero"] is True
    assert paired["divisor_definition"]["common_zero_of_u_b"]=="272*P0"
    assert plain(paired["source_anchor_u"])==plain(inputs["anchor_u"])
    assert plain(paired["source_anchor_b"])==plain(inputs["anchor_b"])
    assert paired["exact_kernel_definition"]["full_global_relation"]=="u*t+b*s=0 in original V5"
    u=read(bound(folder,inputs["anchor_u"]))
    assert u["order272_is_exact"] is True and 0<u["exact_order272_unit"]<P
    jets=read(bound(folder,inputs["V2_jets"]))
    assert jets["matrix_shape"]==[273,418] and jets["row_orders"]==list(range(273))
    # The immutable old manifest binds unselected dependencies; those bytes are not rehashed here.
    old_inventory=read(bound(folder,source["files"]["R872-original-source-inventory.json"]))
    old_receipt=read(bound(folder,source["files"]["R872-retained-inputs-receipt.json"]))
    assert old_inventory["result"]==old_receipt["result"]==SOURCE_RESULT
    assert old_inventory["complete"] is True and old_receipt["complete"] is True
    assert plain(old_receipt["source_inventory"])==entries["R872-original-source-inventory.json"]
    return {"result":RESULT,"complete":True,"source_R872":identity(source),
            "selected_file_count":len(source["files"]),
            "all_selected_bytes_and_original_configurations_verified":True,
            "original_122MB_carrier_downloaded":False,
            "unread_original_dependency_bytes_not_rehashed":True,
            "new_mathematics_executed_in_source_review":False}

def pack(folder,source,target):
    temporary=Path(target).with_name(Path(target).name+".tmp")
    with temporary.open("wb") as raw:
        with gzip.GzipFile(filename="",fileobj=raw,mode="wb",mtime=0,compresslevel=2) as zipped:
            with tarfile.open(fileobj=zipped,mode="w|") as archive:
                for name,row in sorted(source["files"].items()):
                    path=bound(folder,row)
                    info=archive.gettarinfo(str(path),arcname="R872/"+name)
                    info.uid=info.gid=0;info.uname=info.gname="";info.mtime=0
                    with path.open("rb") as f:
                        archive.addfile(info,f)
    temporary.replace(target)

def unpack(bundle,retained,source):
    folder=Path(retained)/"R872";folder.mkdir(parents=True,exist_ok=True)
    seen=set()
    with tarfile.open(bundle,"r|gz") as archive:
        for member in archive:
            if member.isdir():
                continue
            name=PurePosixPath(member.name)
            assert not name.is_absolute() and ".." not in name.parts and "\\" not in member.name
            assert member.isfile() and len(name.parts)==2 and name.parts[0]=="R872"
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
    assert plain(prior["certificate"])==plain(source["certificate"])
    assert inputs=={k:plain(v) for k,v in item["input_pins"].items()}

def prepare(item,out,allow_download=True):
    out=Path(out);retained=out.parent/"retained-R879";retained.mkdir(parents=True,exist_ok=True)
    if all((out/name).exists() for name in (BUNDLE,INVENTORY,INPUT_RECEIPT)):
        inventory=read(out/INVENTORY);receipt=read(out/INPUT_RECEIPT)
        assert inventory["result"]==receipt["result"]==RESULT
        assert inventory["complete"] is True and receipt["complete"] is True
        assert plain(receipt["source_inventory"])==spec(out/INVENTORY)
        assert plain(receipt["source_bundle"])==spec(out/BUNDLE)
        source=inventory["source_R872"];inputs=inventory["inputs"]
        original_pins(item,source,inputs)
        folder=unpack(out/BUNDLE,retained,source)
        review=source_review(folder,source,inputs)
        assert receipt["selected_file_count"]==len(source["files"])
        return folder,source,inputs,review
    assert allow_download,"No retained R879 original-source bundle is available."
    prior=item["source_artifact"]
    folder=retained/"R872";folder.mkdir(parents=True,exist_ok=True)
    archive=IO.Archive(prior,out.parent/"R879-R872-archive",whole=False)
    try:
        archive.extract_bound(MANIFEST,prior["manifest_sha256"],folder/MANIFEST,prior["manifest_bytes"])
        entries=entry_map(folder,prior)
        names=set(META)|{prior["certificate"]["file"]}
        archive.extract_many([(n,entries[n]["sha256"],folder/n,entries[n]["bytes"]) for n in sorted(names)])
        cert,tag=metadata(folder,prior,entries)
        inputs={left:plain(cert[right]) for left,right in INPUT_FIELDS.items()}
        assert inputs=={k:plain(v) for k,v in item["input_pins"].items()}
        names.update(row["file"] for row in inputs.values())
        names.update((cert["stage_manifest"]["file"],"R872-point-jets-index.json.gz",
                      "R872-original-source-inventory.json","R872-retained-inputs-receipt.json"))
        assert "R872-retained-original-inputs.tar.gz" not in names
        archive.extract_many([(n,entries[n]["sha256"],folder/n,entries[n]["bytes"]) for n in sorted(names)])
        names.add(MANIFEST)
        source={**{k:prior[k] for k in BASE},
                "manifest_bytes":prior["manifest_bytes"],"manifest_file_count":prior["manifest_file_count"],
                "certificate":plain(prior["certificate"]),"configuration_sha256":fingerprint(tag),
                "files":{n:entries[n] for n in sorted(names)}}
        original_pins(item,source,inputs)
        review=source_review(folder,source,inputs)
        range_receipt=archive.receipt()
        inventory={"result":RESULT,"complete":True,"source_R872":source,"inputs":inputs,
                   "range_transport":range_receipt,
                   "large_original_source_carrier_read":False,
                   "unread_source_dependencies_remain_certified_external_unit_solve_leaves":True}
        save(out/INVENTORY,inventory)
        pack(folder,source,out/BUNDLE)
        receipt={"result":RESULT,"complete":True,"source_bundle":spec(out/BUNDLE),
                 "source_inventory":spec(out/INVENTORY),"selected_file_count":len(source["files"]),
                 "source_R872":identity(source),"range_transport":range_receipt,
                 "all_selected_original_bytes_verified":True,"new_mathematics_executed":False}
        save(out/INPUT_RECEIPT,receipt)
        print("R879_INPUT_REVIEW="+json.dumps(review,sort_keys=True),flush=True)
        return folder,source,inputs,review
    finally:
        archive.close()

def restore(item,out):
    resume=item.get("resume")
    if not resume:
        return
    assert resume["result"]==RESULT and resume["core_sha256"]==item["core_sha256"]
    directory=out.parent/"R879-resume"
    directory.mkdir(parents=True,exist_ok=True)
    archive=IO.Archive(resume,out.parent/"R879-resume-archive",whole=False)
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
        for key in ("proofs","method_sha256","input_pins"):
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
        source,inputs=inventory["source_R872"],inventory["inputs"]
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
        expanded={**item,"source":dict(source,directory=str(folder.resolve())),"inputs":inputs,
                  "method_file":str(topic_path(item["method"]))}
        expanded["proofs"]={k:dict(v,file=str(topic_path(v["path"]))) for k,v in item["proofs"].items()}
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
            "source_R872":identity(source),"new_mathematics_in_wrapper":False})
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
    assert isinstance(value,list) and len(value)==m
    assert all(isinstance(row,list) and len(row)==n for row in value)

def verify(item,out,request):
    out=Path(out)
    manifest=read(out/MANIFEST)
    assert manifest["result"]==RESULT
    entries={r["file"]:plain(r) for r in manifest["files"]}
    assert len(entries)==len(manifest["files"])
    for row in entries.values():
        bound(out,row)
    assert set(p.name for p in out.iterdir() if p.is_file() and not p.name.endswith((".tmp",".download",".partial")))==set(entries)|{MANIFEST,REFERENCE}
    reference=read(out/REFERENCE)
    assert plain(reference)==spec(out/MANIFEST)
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
        if core["configuration_sha256"] is not None:
            assert core["configuration_sha256"]==fingerprint(tag)
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
            continue
        assert value["complete"] is True
        if name.startswith(PREFIX+"stage-manifest-"):
            for member in value["files"]:
                assert plain(member)==entries[member["file"]]
            continue
        complete_stages.append(row)
    cert=read(out/FINAL) if FINAL in entries else None
    if cert is not None:
        assert cert["result"]==RESULT and cert["configuration"]==tag
        inventory=read(bound(out,cert["stage_manifest"]))
        assert inventory["files"]==sorted(complete_stages,key=lambda x:x["file"])
        if cert.get("resume_state") is not None:
            assert plain(cert["resume_state"])==entries[cert["resume_state"]["file"]]
        for key in ("old_jets_kernel_products_or_inverses_recomputed",
                    "characteristic_zero_reference_coefficients_expanded",
                    "reference_complete_128_basis_computed","original_t_frame_scalar_expanded",
                    "five_original_Lj_RR128_computed","nine_field_norms_or_Hecke_action_computed",
                    "active_eta_support_or_height_computed"):
            assert cert[key] is False
        if cert["complete"] is True:
            assert cert["actual_reference_pole254_function_certified"] is True
            assert cert["actual_reference_basepoint_free_pencil_certified"] is True
            assert cert["actual_reference_function_pole_order"]==254
            assert cert["actual_system_shape"]==[563,418] and cert["actual_system_rank"]==291
            system=read(bound(out,cert["constraint_system"]))
            dimensions(system["matrix_mod_prime"],563,418)
            assert system["right_hand_side_mod_prime"]==[0]*562+[1]
            solved=read(bound(out,cert["unit_solution"]))
            assert solved["accepted"] is True and solved["actual_rank_mod_prime"]==291
            assert solved["all563_original_equations_verified"] is True
            assert solved["both_exact_modular_inverse_products_verified"] is True
            assert solved["actual_minor_determinant_mod_prime"]!=0
            assert len(solved["selected_rows"])==len(solved["selected_pivot_columns"])==291
            assert len(solved["free_columns"])==127 and len(solved["solution_mod_prime"])==418
            function=read(bound(out,cert["reference_function_and_pencil"]))
            assert function["source_unit_solution"]==cert["unit_solution"]
            assert function["actual_reference_pole254_function_certified"] is True
            assert function["actual_reference_basepoint_free_pencil_certified"] is True
            assert function["exact_pole_divisor"]=={"point":"original_P0","multiplicity":254,"all_other_poles_excluded":True}
            assert function["numerator_first19_local_coefficients_mod_prime"]==[0]*18+[1]
            assert function["denominator_order272_unit_mod_prime"]==read(bound(folder,inputs["anchor_u"]))["exact_order272_unit"]
            for key in ("numerator_V2_coordinates_mod_prime","paired_V2_coordinates_mod_prime",
                        "denominator_V2_coordinates_mod_prime"):
                assert len(function[key])==418
            assert function["exact_function_definition"]["old_global_syzygy_inherited_by_exact_linear_combination"] is True
            assert function["original_t_frame"]["leading_t_over_x_not_replaced_by_one"] is True
            assert function["characteristic_zero_reference_coefficients_expanded"] is False
    if run["complete"] is True:
        assert run["process_exit_code"]==0 and run["error"] is None
        assert core is not None and core["complete"] is True and core["error"] is None
        assert cert is not None and cert["complete"] is True
        assert core["certificate_sha256"]==entries[FINAL]["sha256"]
    summary={"result":RESULT,"complete":bool(run["complete"] and cert and cert["complete"]),
             "actual_complete_stage_count":len(complete_stages),"selected_original_file_count":len(source["files"]),
             "all_output_bytes_and_original_source_identities_verified":True,
             "actual_reference_pole254_function_certified":bool(cert and cert["actual_reference_pole254_function_certified"]),
             "actual_reference_basepoint_free_pencil_certified":bool(cert and cert["actual_reference_basepoint_free_pencil_certified"]),
             "actual_system_rank":cert.get("actual_system_rank") if cert else None,
             "old_mathematics_recomputed":False,"new_mathematics_executed_in_verifier":False,
             "nine_norms_active_support_or_height_computed":False}
    print("R879_VERIFY="+json.dumps(summary,sort_keys=True),flush=True)
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
