#!/usr/bin/env python3
"""R837 public runner: original R790/R786 subset IO and atomic-stage continuation.

Only the separate core performs mathematics, and only in this public Actions
workflow. This wrapper verifies byte/source interfaces without repeating it.
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

S=Path(__file__).resolve().parent
REPO=S.parents[2]
TOPIC=REPO/"topics/serre-uniformity"
REQUEST=TOPIC/"notes/R837-fixed-branch-pencil-public-request.json"
RESULT="R837-original-fixed-branch-pencil"
FINAL="p41-original-fixed-branch-pencil-certificate.json"
MANIFEST="full-outputs-manifest.json"
REFERENCE="full-outputs-manifest-reference.json"
BUNDLE="R837-retained-original-inputs.tar.gz"
INVENTORY="R837-original-source-inventory.json"
INPUT_RECEIPT="R837-retained-inputs-receipt.json"
RANGE_SHA="c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
BASE_KEYS=("result","run_id","source_commit","core_sha256","manifest_sha256")
PROOFS=("proof","method","descent_proof","CM_proof")
PREFIX="R837-"
H64=re.compile(r"[0-9a-f]{64}")
IO=None
SOURCES={
 "R790":{"result":"R790-original-CM-fiber-jets",
  "core_sha256":"981eb543b791db416fad355d83eedb9bfe3b86b3e5461483fe4397e2129040b6",
  "certificate":"p41-original-CM-fiber-jets-certificate.json",
  "stage_manifest":"R790-stage-manifest.json.gz"},
 "R786":{"result":"R786-exact-original-power5-short-basis",
  "core_sha256":"4508095a95a2bcaec8c8db8fcd550fbc618b017d2bc0007945783bc109dbf851",
  "certificate":"p41-exact-original-power5-short-basis-certificate.json",
  "stage_manifest":"R786-exact-stages-manifest.json.gz",
  "index":"R786-exact-power5-basis-index.json.gz"}}

def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda:f.read(4*1024*1024),b""):h.update(block)
    return h.hexdigest()

def read(path):
    path=Path(path)
    with (gzip.open if path.suffix==".gz" else open)(path,"rt",encoding="utf-8") as f:
        return json.load(f)

def save(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_name(path.name+".tmp")
    tmp.write_text(json.dumps(value,sort_keys=True,separators=(",",":"))+"\n",encoding="utf-8")
    tmp.replace(path)

def fingerprint(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def safe_name(value):
    assert isinstance(value,str) and Path(value).name==value and value not in (".","..")
    assert "\\" not in value
    return value

def plain(value):
    row={k:value[k] for k in ("file","bytes","sha256")}
    safe_name(row["file"])
    assert isinstance(row["bytes"],int) and row["bytes"]>=0 and H64.fullmatch(row["sha256"])
    return row

def file_spec(path):
    path=Path(path)
    return {"file":path.name,"bytes":path.stat().st_size,"sha256":sha(path)}

def bound(folder,row):
    row=plain(row);p=Path(folder)/row["file"]
    assert file_spec(p)==row,("Changed bound bytes",p.name)
    return p

def topic_path(value):
    value=PurePosixPath(value)
    assert not value.is_absolute() and ".." not in value.parts
    path=(TOPIC/str(value)).resolve()
    assert path.is_relative_to(TOPIC.resolve())
    return path

def source_identity(item):
    return {k:item[k] for k in BASE_KEYS}

def selected_names(label):
    p=SOURCES[label]
    names={MANIFEST,"run-receipt.json","core-receipt.json","public-actions-input.json",
           p["certificate"],p["stage_manifest"]}
    if label=="R790":
        names.update("R790-M2-CM-jet-"+str(i).zfill(4)+".json.gz" for i in range(146))
    else:
        names.add(p["index"])
        for power,count in ((1,146),(2,418),(3,690)):
            names.update("R786-exact-power-"+str(power)+"-row-"+str(i).zfill(4)+".json.gz"
                         for i in range(count))
    return sorted(names)

def load_io(item):
    global IO
    p=S/safe_name(item["io_helper"])
    assert p.name=="R824_public_original_global_polar_generators.py"
    assert sha(p)==item["io_helper_sha256"]==RANGE_SHA
    spec=importlib.util.spec_from_file_location("R837_frozen_Range_only_IO",p)
    IO=importlib.util.module_from_spec(spec);spec.loader.exec_module(IO)

def guard(item,path):
    if os.environ.get("GITHUB_ACTIONS")!="true" or \
       os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public":
        raise SystemExit("R837 execution belongs to this public repository's Actions.")
    assert item["result"]==RESULT and item["p"]==41 and item["producer_inputs_pending"] is False
    assert path.resolve()==REQUEST.resolve()
    assert item["core"]=="R837_original_branch_pencil.py"
    assert item["wrapper"]=="R837_original_branch_pencil_public.py"
    assert sha(__file__)==item["wrapper_sha256"] and sha(S/item["core"])==item["core_sha256"]
    assert 0<item["budget_minutes"]<=300
    assert isinstance(item["controls"]["maximum_pencil_trials"],int) and item["controls"]["maximum_pencil_trials"]>0
    for name in PROOFS:assert sha(topic_path(item[name]))==item[name+"_sha256"]
    assert sha(REPO/"README.md")==item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md")==item["readme_sha256"]["topic"]
    assert set(item["sources"])==set(SOURCES)
    for label,source in item["sources"].items():
        assert source["result"]==SOURCES[label]["result"]
        assert source["core_sha256"]==SOURCES[label]["core_sha256"]
        assert source["expected_conclusion"]=="success"
        assert source["manifest_bytes"]>0 and H64.fullmatch(source["configuration_sha256"])
        assert source["selected_file_count"]==len(selected_names(label))
        assert H64.fullmatch(source["selected_files_sha256"])
        for key in ("certificate","stage_manifest"):
            assert plain(source[key])["file"]==SOURCES[label][key]
        if label=="R786":assert plain(source["index"])["file"]==SOURCES[label]["index"]
    load_io(item)

def source_review(label,item,directory):
    """Bind original complete stages to the original producer; no arithmetic."""
    directory=Path(directory);source=item["sources"][label];p=SOURCES[label]
    mp=directory/MANIFEST
    assert mp.stat().st_size==source["manifest_bytes"] and sha(mp)==source["manifest_sha256"]
    manifest=read(mp);assert manifest["result"]==source["result"]
    entries={row["file"]:plain(row) for row in manifest["files"]}
    assert len(entries)==len(manifest["files"])==source["manifest_file_count"]
    entries[MANIFEST]=file_spec(mp)
    names=selected_names(label)
    assert set(names)<=set(entries)
    selected={n:entries[n] for n in names}
    for row in selected.values():bound(directory,row)
    assert fingerprint([selected[n] for n in sorted(selected)])==source["selected_files_sha256"]
    cert=read(bound(directory,source["certificate"]))
    assert cert["complete"] is True and cert["result"]==source["result"]
    tag=cert["configuration"]
    assert fingerprint(tag)==source["configuration_sha256"]
    run=read(directory/"run-receipt.json");core=read(directory/"core-receipt.json")
    public=read(directory/"public-actions-input.json")
    assert run["complete"] is True and run["process_exit_code"]==0
    assert run.get("error") is None
    assert str(run["workflow_run_id"])==str(source["run_id"])
    assert run["source_commit"]==public["source_commit"]==source["source_commit"]
    assert core["result"]==public["result"]==source["result"]
    assert core["complete"] is True
    assert core["source_sha256"]==public["core_sha256"]==source["core_sha256"]
    assert core["certificate_sha256"]==source["certificate"]["sha256"]
    if run.get("core_receipt_sha256") is not None:
        assert run["core_receipt_sha256"]==selected["core-receipt.json"]["sha256"]
    sm=read(bound(directory,source["stage_manifest"]))
    assert sm["complete"] is True and sm["configuration"]==tag
    stages={row["file"]:plain(row) for row in sm["files"]}
    assert len(stages)==len(sm["files"])
    assert all(entries[n]==row for n,row in stages.items())
    mat_names=[n for n in names if n.startswith("R790-M2-CM-jet-") or n.startswith("R786-exact-power-")]
    for name in mat_names:
        assert selected[name]==stages[name]
        data=read(directory/name)
        assert data["complete"] is True and data["configuration"]==tag
    if label=="R790":
        assert cert["M2_dimension"]==146 and cert["original_Y_CM_point"]=="P1"
        assert cert["original_c1"]==4424 and cert["original_M2_scale"]=="6724"
        assert cert["original_psi_values_and_first_coarse_jets_verified"] is True
        assert cert["old_torsion_modulus_or_Weil_pairing_or_M2_basis_recomputed"] is False
        assert plain(cert["stage_manifest"])==plain(source["stage_manifest"])
        cert_rows=cert["M2_output_rows"]
        assert len(cert_rows)==146
        for i,row in enumerate(cert_rows):
            name="R790-M2-CM-jet-"+str(i).zfill(4)+".json.gz"
            assert plain(row)==selected[name]
            data=read(directory/name)
            assert data["index"]==i and data["integer_scale"]=="6724"
            assert data["K_basis"]==["1","zeta=(-1+sqrt(-3))/2"]
            assert data["original_c1"]==4424 and data["R786_power1_scale_preserved"] is True
    else:
        assert cert["exact_power5_basis_dimension"]==1234
        assert cert["exact_K_basis_prefix_bound_qY"]==128
        assert cert["all_original_R775_mod739_short_series_compared"] is True
        assert plain(cert["stages_manifest"])==plain(source["stage_manifest"])
        assert plain(cert["basis_index"])==plain(source["index"])
        index=read(bound(directory,source["index"]))
        assert index["complete"] is True and index["configuration"]==tag
        assert len(index["basis_rows"])==1234
        for power,count in ((1,146),(2,418),(3,690)):
            for i in range(count):
                name="R786-exact-power-"+str(power)+"-row-"+str(i).zfill(4)+".json.gz"
                data=read(directory/name)
                assert data["weight"]==2*power and data["bound_qY"]==128
                assert data["original_R775_finite_coefficients_verified"] is True
    result={**source_identity(source),"configuration_sha256":source["configuration_sha256"],
            "selected_files_sha256":source["selected_files_sha256"],
            "files":selected,"certificate":plain(source["certificate"]),
            "stage_manifest":plain(source["stage_manifest"])}
    if label=="R786":result["index"]=plain(source["index"])
    return result

def pack_sources(retained,inventory,target):
    retained=Path(retained);tmp=target.with_name(target.name+".tmp")
    with tmp.open("wb") as raw:
        with gzip.GzipFile(fileobj=raw,mode="wb",mtime=0,compresslevel=2) as gz:
            with tarfile.open(fileobj=gz,mode="w|") as tar:
                for label,source in sorted(inventory["sources"].items()):
                    for name,row in sorted(source["files"].items()):
                        p=bound(retained/label,row)
                        info=tar.gettarinfo(str(p),arcname=label+"/"+name)
                        info.uid=info.gid=0;info.uname=info.gname="";info.mtime=0
                        with p.open("rb") as f:tar.addfile(info,f)
    tmp.replace(target)

def unpack_sources(path,retained,inventory):
    retained=Path(retained)
    wanted={label+"/"+name:plain(row)
            for label,source in inventory["sources"].items() for name,row in source["files"].items()}
    seen=set()
    with tarfile.open(path,"r:gz") as tar:
        for member in tar:
            assert member.isfile() and not member.issym() and not member.islnk()
            name=PurePosixPath(member.name)
            assert not name.is_absolute() and ".." not in name.parts and len(name.parts)==2
            assert member.name in wanted and member.name not in seen
            seen.add(member.name);row=wanted[member.name]
            assert member.size==row["bytes"]
            dest=retained/member.name;dest.parent.mkdir(parents=True,exist_ok=True)
            tmp=dest.with_name(dest.name+".tmp");h=hashlib.sha256();count=0
            with tar.extractfile(member) as src,tmp.open("wb") as output:
                for block in iter(lambda:src.read(4*1024*1024),b""):
                    output.write(block);h.update(block);count+=len(block)
            assert count==row["bytes"] and h.hexdigest()==row["sha256"]
            tmp.replace(dest)
    assert seen==set(wanted)
    return len(seen)

def prepare_sources(item,out,allow_download=True):
    out=Path(out);retained=out.parent/"retained-original-R837"
    retained.mkdir(parents=True,exist_ok=True)
    receipt_path=out/INPUT_RECEIPT;inventory_path=out/INVENTORY
    if receipt_path.exists() and (out/BUNDLE).exists() and inventory_path.exists():
        receipt=read(receipt_path);inventory=read(inventory_path)
        assert receipt["result"]==RESULT and receipt["complete"] is True
        assert receipt["sources"]==item["sources"]
        assert inventory["result"]==RESULT and inventory["complete"] is True
        bound(out,receipt["source_inventory"]);bound(out,receipt["source_bundle"])
        count=unpack_sources(out/BUNDLE,retained,inventory)
        reviewed={label:source_review(label,item,retained/label) for label in sorted(SOURCES)}
        assert reviewed==inventory["sources"]
        assert count==receipt["minimal_bundle_member_count"]
        return retained,receipt,reviewed
    assert allow_download,"Completed source carrier is required for read-only verification."
    reviewed={};transport={}
    for label in sorted(SOURCES):
        source=item["sources"][label];directory=retained/label;directory.mkdir(exist_ok=True)
        archive=IO.Archive(source,out.parent/("download-"+label),whole=False)
        try:
            archive.extract_bound(MANIFEST,source["manifest_sha256"],directory/MANIFEST,source["manifest_bytes"])
            manifest=read(directory/MANIFEST)
            assert manifest["result"]==source["result"]
            entries={row["file"]:plain(row) for row in manifest["files"]}
            assert len(entries)==len(manifest["files"])==source["manifest_file_count"]
            assert set(entries)<=set(archive.by_name)
            for name,row in entries.items():
                assert len(archive.by_name[name])==1 and archive.by_name[name][0].file_size==row["bytes"]
            archive.extract_many([(n,entries[n]["sha256"],directory/n,entries[n]["bytes"])
                                  for n in selected_names(label) if n!=MANIFEST])
            reviewed[label]=source_review(label,item,directory)
            transport[label]=archive.receipt()
        finally:archive.close()
    inventory={"result":RESULT,"complete":True,"sources":reviewed,
               "all_entries_are_unchanged_completed_original_source_bytes":True}
    save(inventory_path,inventory);pack_sources(retained,inventory,out/BUNDLE)
    count=sum(len(source["files"]) for source in reviewed.values())
    receipt={"result":RESULT,"complete":True,"sources":item["sources"],
             "source_inventory":file_spec(inventory_path),"source_bundle":file_spec(out/BUNDLE),
             "minimal_bundle_member_count":count,"range_transport":transport,
             "old_CM_torsion_q_expansions_or_basis_selection_recomputed":False}
    save(receipt_path,receipt)
    print("BRANCH_PENCIL_INPUT_REVIEW="+json.dumps({
        "source_inventory":receipt["source_inventory"],"source_bundle":receipt["source_bundle"],
        "selected_original_files":count,"sources":[source_identity(item["sources"][k]) for k in sorted(SOURCES)],
        "new_mathematics_executed_in_source_preparation":False},sort_keys=True),flush=True)
    return retained,receipt,reviewed

def stable_job(item):
    return {k:v for k,v in item.items()
            if k not in ("resume","budget_minutes","controls","readme_sha256","rules_last_read_commit")}

def restore(item,out):
    resume=item.get("resume")
    if resume is None:return
    assert resume["result"]==RESULT and resume["core_sha256"]==item["core_sha256"]
    meta=out.parent/"resume-metadata";meta.mkdir(parents=True,exist_ok=True)
    archive=IO.Archive(resume,out.parent/"download-R837-continuation",whole=False)
    try:
        archive.extract_bound(MANIFEST,resume["manifest_sha256"],meta/MANIFEST,resume["manifest_bytes"])
        manifest=read(meta/MANIFEST);assert manifest["result"]==RESULT
        entries={row["file"]:plain(row) for row in manifest["files"]}
        assert len(entries)==len(manifest["files"])==resume["manifest_file_count"]
        for name in ("run-receipt.json","public-actions-input.json","core-receipt.json",
                     INPUT_RECEIPT,INVENTORY,BUNDLE):
            if name=="core-receipt.json" and name not in entries:continue
            row=entries[name]
            destination=out/name if name in (INPUT_RECEIPT,INVENTORY,BUNDLE) else meta/name
            archive.extract_bound(name,row["sha256"],destination,row["bytes"])
        run=read(meta/"run-receipt.json");initial=read(meta/"public-actions-input.json")
        assert run["result"]==initial["result"]==RESULT
        assert str(run["workflow_run_id"])==str(resume["run_id"])
        assert run["source_commit"]==initial["source_commit"]==resume["source_commit"]
        assert initial["core_sha256"]==item["core_sha256"]
        assert stable_job(initial["job"])==stable_job(item)
        assert run["process_exit_code"] in resume["accepted_process_exit_codes"]
        if (meta/"core-receipt.json").exists():
            core=read(meta/"core-receipt.json")
            assert core["result"]==RESULT and core["source_sha256"]==item["core_sha256"]
            assert run["core_receipt_sha256"]==entries["core-receipt.json"]["sha256"]
        prepare_sources(item,out,allow_download=False)
        names=sorted(n for n in entries if n.startswith(PREFIX) and n.endswith(".json.gz"))
        archive.extract_many([(n,entries[n]["sha256"],out/n,entries[n]["bytes"]) for n in names])
        tags=set()
        for name in names:
            stage=read(out/name)
            assert stage["complete"] is True and stage["configuration"]["result"]==RESULT
            assert stage["configuration"]["source_sha256"]==item["core_sha256"]
            tags.add(fingerprint(stage["configuration"]))
        assert len(tags)<=1
        final_restored=False
        if FINAL in entries:
            row=entries[FINAL];archive.extract_bound(FINAL,row["sha256"],meta/FINAL,row["bytes"])
            final=read(meta/FINAL)
            if final.get("complete") is True and final.get("fixed_branch_pencil_certified") is True:
                assert run["complete"] is True and run["process_exit_code"]==0
                assert core["complete"] is True and core["certificate_sha256"]==row["sha256"]
                assert not tags or fingerprint(final["configuration"]) in tags
                shutil.copyfile(meta/FINAL,out/FINAL);final_restored=True
        save(out/"resume-inheritance-receipt.json",{
            "result":RESULT,"complete":True,"source_resume":resume,
            "original_manifest":file_spec(meta/MANIFEST),"range_transport":archive.receipt(),
            "all_restored_complete_stages":[entries[n] for n in names],
            "restored_successful_final":final_restored,
            "old_P0_U_or_pencil_stages_not_recomputed":True})
    finally:archive.close()

def output_manifest(out):
    entries=[dict(file_spec(p),included_in_git=False) for p in sorted(out.iterdir())
             if p.is_file() and p.name not in (MANIFEST,REFERENCE)
             and not p.name.endswith((".tmp",".download"))]
    save(out/MANIFEST,{"result":RESULT,"files":entries,"temporary_active_checkpoint_retention_days":1,
                       "reproducible_data_in_git_or_release":False})
    save(out/REFERENCE,{"result":RESULT,"manifest_file":MANIFEST,
                        "manifest_sha256":sha(out/MANIFEST),"manifest_bytes":(out/MANIFEST).stat().st_size,
                        "file_count":len(entries)})

def compute(item,out,request_path):
    out.mkdir(parents=True,exist_ok=True);process=None;exitcode=1;error=None;outer_timeout=False
    try:
        restore(item,out)
        retained,receipt,sources=prepare_sources(item,out)
        expanded=dict(item)
        expanded["sources"]={label:{**source,"directory":str((retained/label).resolve())}
                             for label,source in sources.items()}
        for key in PROOFS:expanded[key]=str(topic_path(item[key]))
        save(out/"public-actions-expanded-job.json",expanded)
        initial={"result":RESULT,"p":41,"source_repository":"Rogerhu12/math-research-public",
                 "source_commit":os.environ["GITHUB_SHA"],"job":item,"request_sha256":sha(request_path),
                 "driver_sha256":sha(__file__),"core_sha256":item["core_sha256"],
                 "proof_sha256":item["proof_sha256"],"method_sha256":item["method_sha256"],
                 "descent_proof_sha256":item["descent_proof_sha256"],"CM_proof_sha256":item["CM_proof_sha256"],
                 "io_helper_sha256":RANGE_SHA,"workflow_sha256":sha(REPO/item["workflow"]),
                 "root_readme_sha256":sha(REPO/"README.md"),"topic_readme_sha256":sha(TOPIC/"README.md"),
                 "source_inventory":receipt["source_inventory"],
                 "prepared_at_utc":dt.datetime.now(dt.timezone.utc).isoformat(),
                 "all_new_mathematics_runs_only_in_separate_public_Actions_core":True}
        save(out/"public-actions-input.json",initial)
        command=[sys.executable,str(S/item["core"]),"--config",str(out/"public-actions-expanded-job.json"),
                 "--out",str(out),"--budget-minutes",str(item["budget_minutes"])]
        with (out/"public-actions-run.log").open("w",encoding="utf-8") as log:
            process=subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
            try:exitcode=process.wait(timeout=item["budget_minutes"]*60+900)
            except subprocess.TimeoutExpired:
                outer_timeout=True;os.killpg(process.pid,signal.SIGTERM)
                try:process.wait(timeout=20)
                except subprocess.TimeoutExpired:os.killpg(process.pid,signal.SIGKILL);process.wait()
                exitcode=124
    except BaseException as exc:
        error=type(exc).__name__+": "+str(exc)
        if process is not None and process.poll() is None:
            os.killpg(process.pid,signal.SIGTERM)
            try:process.wait(timeout=20)
            except subprocess.TimeoutExpired:os.killpg(process.pid,signal.SIGKILL);process.wait()
        exitcode=1
    finally:
        cp=out/"core-receipt.json";core=read(cp) if cp.exists() else None
        final=read(out/FINAL) if (out/FINAL).exists() else None
        complete=exitcode==0 and core is not None and core.get("complete") is True \
                 and final is not None and final.get("complete") is True \
                 and final.get("fixed_branch_pencil_certified") is True
        run={"result":RESULT,"p":41,"complete":complete,"process_exit_code":exitcode,"error":error,
             "core_receipt_sha256":sha(cp) if cp.exists() else None,
             "source_commit":os.environ.get("GITHUB_SHA"),"workflow_run_id":os.environ.get("GITHUB_RUN_ID"),
             "workflow_attempt":os.environ.get("GITHUB_RUN_ATTEMPT"),
             "execution_environment":"public-repository-github-actions","outer_timeout":outer_timeout,
             "finished_at_utc":dt.datetime.now(dt.timezone.utc).isoformat()}
        save(out/"run-receipt.json",run);output_manifest(out)
        print("BRANCH_PENCIL_RUN_RECEIPT="+json.dumps(run,sort_keys=True),flush=True)
    return exitcode

def verify(item,out,request_path):
    """Read complete source and result schemas; never import or rerun the core."""
    manifest=read(out/MANIFEST);assert manifest["result"]==RESULT
    entries={row["file"]:plain(row) for row in manifest["files"]}
    assert len(entries)==len(manifest["files"])
    for row in entries.values():bound(out,row)
    ref=read(out/REFERENCE)
    assert ref["result"]==RESULT and ref["manifest_sha256"]==sha(out/MANIFEST)
    assert ref["manifest_bytes"]==(out/MANIFEST).stat().st_size and ref["file_count"]==len(entries)
    run=read(out/"run-receipt.json")
    if not run.get("complete"):
        print("BRANCH_PENCIL_INCOMPLETE_IO_REVIEW="+json.dumps({
            "complete":False,"run":run,"manifest_files":len(entries),
            "no_partial_output_is_claimed_as_a_fixed_branch_pencil":True},sort_keys=True),flush=True)
        return 2
    retained,receipt,sources=prepare_sources(item,out,allow_download=False)
    initial=read(out/"public-actions-input.json");core=read(out/"core-receipt.json");final=read(out/FINAL)
    assert initial["job"]==item and initial["request_sha256"]==sha(request_path)
    assert initial["source_commit"]==run["source_commit"]
    assert initial["driver_sha256"]==sha(__file__) and initial["core_sha256"]==item["core_sha256"]
    assert core["result"]==final["result"]==RESULT
    assert core["complete"] is True and final["complete"] is True and run["process_exit_code"]==0
    assert core["source_sha256"]==item["core_sha256"]
    assert run["core_receipt_sha256"]==entries["core-receipt.json"]["sha256"]
    assert core["certificate_sha256"]==entries[FINAL]["sha256"]
    tag=final["configuration"]
    assert tag["result"]==RESULT and tag["source_sha256"]==item["core_sha256"]
    for flag in ("original_P0_evaluation_certified","complete_fixed_branch_space_certified",
                 "fixed_branch_pencil_certified"):
        assert final[flag] is True and core[flag] is True
    assert final["actual_pencil_rank"]==1213
    sm=plain(final["stage_manifest"]);assert entries[sm["file"]]==sm
    inventory=read(bound(out,sm))
    assert inventory["complete"] is True and inventory["configuration"]==tag
    stages={row["file"]:plain(row) for row in inventory["files"]}
    assert len(stages)==len(inventory["files"])
    for name,row in stages.items():
        assert entries[name]==row
        stage=read(bound(out,row))
        assert stage["complete"] is True and stage["configuration"]==tag
    print("BRANCH_PENCIL_COMPLETE_IO_REVIEW="+json.dumps({
        "result":RESULT,"certificate":entries[FINAL],"stage_manifest":sm,
        "original_P0_evaluation_certified":True,"complete_fixed_branch_space_certified":True,
        "fixed_branch_pencil_certified":True,"actual_pencil_rank":final["actual_pencil_rank"],
        "complete_stages":len(stages),"manifest_files":len(entries),
        "source_inventory":receipt["source_inventory"],"source_bundle":receipt["source_bundle"],
        "seconds":final["seconds"],
        "all_output_and_selected_source_bytes_verified":True,
        "mathematics_reexecuted_by_wrapper":False},sort_keys=True),flush=True)
    return 0

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--verify",action="store_true")
    args=parser.parse_args()
    item=read(REQUEST);guard(item,REQUEST)
    return verify(item,args.output,REQUEST) if args.verify else compute(item,args.output,REQUEST)

if __name__=="__main__":raise SystemExit(main())
