#!/usr/bin/env python3
"""Minimal original-point carrier and public runner for R852."""
import argparse
import datetime as dt
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import tarfile
import traceback

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO/"topics/serre-uniformity"
REQUEST = TOPIC/"notes/R852-original-one-Z-coefficients-public-request.json"
RESULT = "R852-original-one-Z-coefficients-and-constant-DAG"
FINAL = "p41-original-one-Z-coefficients-certificate.json"
PREFIX = "R852-one-Z-"
MANIFEST = "full-outputs-manifest.json"
REFERENCE = "full-outputs-manifest-reference.json"
INVENTORY = PREFIX+"original-source-inventory.json"
BUNDLE = PREFIX+"retained-original-inputs.tar.gz"
INPUT_RECEIPT = PREFIX+"retained-inputs-receipt.json"
PARENT = "R850_public_original_rigidified_fibres.py"
PARENT_SHA = "ff318ca06e5bf2a385c866df2abb0ea102d6606eb2af2a818a0493f075b123cf"
DAG = "R792_original_CM_response_beta_DAG.py"
DAG_SHA = "afb49c1ac4245674d29364789e817b566517e1f5bf6d506cee684ed03fa34b8b"
HELPER_SHA = "c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
P = None

def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as stream:
        for data in iter(lambda:stream.read(4*1024*1024),b""):
            h.update(data)
    return h.hexdigest()

def read(path):
    path=Path(path)
    with (gzip.open if path.suffix==".gz" else open)(path,"rt",encoding="utf-8") as stream:
        return json.load(stream)

def save(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_name(path.name+".tmp")
    tmp.write_text(json.dumps(value,sort_keys=True,separators=(",",":"))+"\n")
    tmp.replace(path)

def spec(path):
    path=Path(path)
    return {"file":path.name,"bytes":path.stat().st_size,"sha256":sha(path)}

def load_parent(item):
    global P
    assert item["source_transport_helper"]==PARENT
    assert item["source_transport_helper_sha256"]==PARENT_SHA==sha(S/PARENT)
    module=importlib.util.spec_from_file_location("R852_frozen_original_source_transport",S/PARENT)
    P=importlib.util.module_from_spec(module);module.loader.exec_module(P)
    assert item["io_helper_sha256"]==HELPER_SHA
    P.load_helper(item)

def topic_path(name):
    answer=(TOPIC/name).resolve()
    assert answer.is_relative_to(TOPIC.resolve())
    return answer

def guard(item,path):
    assert os.environ.get("GITHUB_ACTIONS")=="true"
    assert os.environ.get("GITHUB_REPOSITORY")=="Rogerhu12/math-research-public"
    assert path.resolve()==REQUEST.resolve()
    assert item["result"]==RESULT and item["p"]==41 and item["producer_inputs_pending"] is False
    assert item["core"]=="R852_original_one_Z_coefficients.py"
    assert item["wrapper"]=="R852_public_original_one_Z_coefficients.py"
    assert item["core_sha256"]==sha(S/item["core"])
    assert item["wrapper_sha256"]==sha(__file__)
    assert item["dag_core"]==DAG and item["dag_core_sha256"]==DAG_SHA==sha(S/DAG)
    assert 0<item["budget_minutes"]<=300
    assert set(item["proofs"])=={"ZA","method"}
    for row in item["proofs"].values():
        assert sha(topic_path(row["path"]))==row["sha256"]
    assert sha(REPO/"README.md")==item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md")==item["readme_sha256"]["topic"]
    assert item["source"]["selected_file_count"]==9
    assert item["source"]["expected_conclusion"]=="success"
    assert item["source"]["accepted_process_exit_codes"]==[0]
    load_parent(item)

def stable_job(item):
    return {k:v for k,v in item.items()
            if k not in ("resume","budget_minutes","readme_sha256","rules_last_read_commit")}

def source_parent_identity(item):
    source=item["source"]
    return {**P.identity(source),"selected_files_sha256":source["selected_files_sha256"],
            "selected_file_count":source["selected_file_count"]}

def pack_source(folder,reviewed,target):
    folder,target=Path(folder),Path(target)
    temporary=target.with_name(target.name+".tmp")
    with temporary.open("wb") as raw:
        with gzip.GzipFile(fileobj=raw,mode="wb",mtime=0,filename="",compresslevel=0) as zipped:
            with tarfile.open(fileobj=zipped,mode="w|") as tar:
                for name,row in sorted(reviewed["files"].items()):
                    path=P.bound(folder,row)
                    info=tar.gettarinfo(str(path),arcname="POINTS/"+name)
                    info.uid=info.gid=info.mtime=0;info.uname=info.gname=""
                    with path.open("rb") as stream:
                        tar.addfile(info,stream)
    temporary.replace(target)

def sources(item,out):
    out=Path(out)
    retained=out.parent/"retained-R852-direct"
    nested=out.parent/"retained-R852-original-point-leaves"
    retained.mkdir(parents=True,exist_ok=True)
    present=[(out/name).exists() for name in (INVENTORY,BUNDLE,INPUT_RECEIPT)]
    if all(present):
        inventory,receipt=read(out/INVENTORY),read(out/INPUT_RECEIPT)
        assert inventory["result"]==receipt["result"]==RESULT
        assert inventory["complete"] is True and receipt["complete"] is True
        assert receipt["source_request"]==item["source"]
        P.bound(out,receipt["source_inventory"]);P.bound(out,receipt["source_bundle"])
        assert P.unpack_groups(out/BUNDLE,retained,inventory["sources"])==9
        reviewed=P.review_source("POINTS",item["source"],retained/"POINTS")
        assert inventory["sources"]=={"POINTS":reviewed}
    else:
        assert not any(present),"Incomplete source carrier must be recovered from the actual completed source."
        transport=P.fetch_direct("POINTS",item["source"],retained)
        reviewed=P.review_source("POINTS",item["source"],retained/"POINTS")
        save(out/INVENTORY,{"result":RESULT,"complete":True,
            "sources":{"POINTS":reviewed},"all_members_are_unchanged_original_producer_bytes":True})
        pack_source(retained/"POINTS",reviewed,out/BUNDLE)
        receipt={"result":RESULT,"complete":True,"source_request":item["source"],
            "source_inventory":spec(out/INVENTORY),"source_bundle":spec(out/BUNDLE),
            "minimal_bundle_member_count":9,"range_transport":transport,
            "archive_digest_semantics":"original API digest and selected member SHA; whole source ZIP not rehashed",
            "original_270_member_carrier_preserved":True,"old_numeric_arithmetic_recomputed":False}
        save(out/INPUT_RECEIPT,receipt)
    groups=P.review_nested_points(retained/"POINTS",nested)
    assert sum(group["selected_file_count"] for group in groups.values())==270
    print("R852_SOURCE_IO "+json.dumps({"direct_members":9,"original_point_members":270,
        "source_bundle":receipt["source_bundle"],"new_math_executed":False},sort_keys=True),flush=True)
    return nested,groups,receipt

def manifest(out):
    out=Path(out)
    rows=[dict(spec(path),included_in_git=False) for path in sorted(out.iterdir())
          if path.is_file() and path.name not in (MANIFEST,REFERENCE)
          and not path.name.endswith((".tmp",".download",".partial"))]
    save(out/MANIFEST,{"result":RESULT,"files":rows,
        "temporary_active_checkpoint_retention_days":1,"reproducible_data_in_git_or_release":False})
    save(out/REFERENCE,{"result":RESULT,"manifest_file":MANIFEST,"manifest_sha256":sha(out/MANIFEST),
        "manifest_bytes":(out/MANIFEST).stat().st_size,"file_count":len(rows)})

def restore(item,out):
    resume=item.get("resume")
    if resume is None:
        return
    assert resume["result"]==RESULT and resume["core_sha256"]==item["core_sha256"]
    meta=out.parent/"R852-resume-metadata";meta.mkdir(parents=True,exist_ok=True)
    archive=P.IO.Archive(resume,out.parent/"R852-resume-download",whole=False)
    try:
        archive.extract_bound(MANIFEST,resume["manifest_sha256"],meta/MANIFEST,resume["manifest_bytes"])
        inventory=read(meta/MANIFEST)
        assert inventory["result"]==RESULT
        entries={row["file"]:P.plain(row) for row in inventory["files"]}
        assert len(entries)==len(inventory["files"])==resume["manifest_file_count"]
        assert set(archive.by_name)==set(entries)|{MANIFEST,REFERENCE}
        for name in ("run-receipt.json","public-actions-input.json"):
            row=entries[name]
            archive.extract_bound(name,row["sha256"],meta/name,row["bytes"])
        run,public=read(meta/"run-receipt.json"),read(meta/"public-actions-input.json")
        assert str(run["workflow_run_id"])==str(resume["run_id"])
        assert run["source_commit"]==public["source_commit"]==resume["source_commit"]
        assert run["process_exit_code"] in (0,75,124,137,-15)
        assert public["source_repository"]=="Rogerhu12/math-research-public"
        assert stable_job(public["job"])==stable_job(item)
        names=[INVENTORY,BUNDLE,INPUT_RECEIPT]
        names += [name for name in entries if name.startswith(PREFIX) and name.endswith(".json.gz")]
        if run["complete"] is True:
            names.append(FINAL)
        for name in dict.fromkeys(names):
            row=entries[name]
            archive.extract_bound(name,row["sha256"],out/name,row["bytes"])
        save(out/"resume-source-receipt.json",{
            "result":RESULT,"source_request":resume,"old_stable_job_identical":True,
            "all_completed_stages_restored_unchanged":True,"transport":archive.receipt()})
    finally:
        archive.close()

def compute(item,out):
    out=Path(out);out.mkdir(parents=True,exist_ok=True)
    source=os.environ["GITHUB_SHA"]
    started=dt.datetime.now(dt.timezone.utc).isoformat()
    process_code,error,cert = 1,None,None
    process=None
    try:
        restore(item,out)
        retained,expanded,receipt=sources(item,out)
        save(out/"public-actions-input.json",{
            "result":RESULT,"source_repository":"Rogerhu12/math-research-public",
            "source_commit":source,"job":item,"core_sha256":item["core_sha256"],
            "wrapper_sha256":item["wrapper_sha256"],
            "root_readme_sha256":item["readme_sha256"]["root"],
            "topic_readme_sha256":item["readme_sha256"]["topic"],
            "source_inventory":receipt["source_inventory"],"expanded_sources":expanded})
        config={"result":RESULT,"p":41,"core_sha256":item["core_sha256"],
            "dag_core_sha256":DAG_SHA,"proofs":item["proofs"],"expanded_sources":expanded,
            "transport_parent_identity":source_parent_identity(item)}
        config_path=out.parent/"R852-expanded-config.json"
        save(config_path,config)
        command=[sys.executable,str(S/item["core"]),"--config",str(config_path),
            "--retained",str(retained),"--output",str(out),"--topic",str(TOPIC),
            "--dag-core",str(S/DAG),"--budget-minutes",str(item["budget_minutes"])]
        process=subprocess.Popen(command,start_new_session=True)
        try:
            process_code=process.wait(timeout=item["budget_minutes"]*60+90)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid,signal.SIGTERM)
            try:
                process.wait(timeout=15)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid,signal.SIGKILL);process.wait()
            process_code=124
            error="Core exceeded its declared budget and shutdown allowance; completed stages retained."
        if process_code==0:
            cert=read(out/FINAL)
            assert cert["result"]==RESULT and cert["complete"] is True
            assert cert["configuration"]["source_sha256"]==item["core_sha256"]
            assert cert["configuration"]["proofs"]==item["proofs"]
            assert cert["configuration"]["transport_parent_identity"]==source_parent_identity(item)
            assert cert["complete_math_stage_count"]==3
            for flag in ("original_one_Z_coefficient_program_certified",
                         "five_C_coefficients_in_original_L_exactly_expanded",
                         "five_D_coefficients_as_original_exact_DAG",
                         "original_seven_and_normalized_trace_scale_preserved",
                         "original_T7_phase_and_whole_expression_Galois_action_preserved"):
                assert cert[flag] is True
            for flag in ("old_mathematical_computations_repeated","actual_41_response_balls_computed",
                         "actual_41_Z_computed","D_coefficients_expanded_as_rational_coordinates",
                         "actual_Y_Picard_period_computed","actual_height_computed",
                         "height_nonzero_proved","original_CM_candidate_A1_accepted","all_p_uniformity_proved"):
                assert cert[flag] is False
            for key in ("source_audit","coefficient_program","five_exact_C_coordinates","stage_manifest"):
                path=P.bound(out,cert[key]);value=read(path)
                assert value["complete"] is True and value["configuration"]==cert["configuration"]
            core=read(out/"core-receipt.json")
            assert core["complete"] is True and core["process_exit_code"]==0 and core["error"] is None
            assert core["source_sha256"]==item["core_sha256"]
            assert core["certificate_sha256"]==sha(out/FINAL)
            assert core["configuration"]==cert["configuration"]
    except Exception:
        error=traceback.format_exc();process_code=1
        print(error,flush=True)
    finally:
        run={"result":RESULT,"source_commit":source,
            "workflow_run_id":os.environ["GITHUB_RUN_ID"],
            "workflow_run_attempt":os.environ.get("GITHUB_RUN_ATTEMPT","1"),
            "started_UTC":started,"finished_UTC":dt.datetime.now(dt.timezone.utc).isoformat(),
            "process_exit_code":process_code,"complete":process_code==0 and cert is not None,
            "error":error,"core_receipt_sha256":sha(out/"core-receipt.json") if (out/"core-receipt.json").exists() else None,
            "certificate_sha256":sha(out/FINAL) if cert is not None else None,
            "old_arithmetic_repeated":False}
        save(out/"run-receipt.json",run)
        manifest(out)
        print("R852_RUN_RECEIPT "+json.dumps(run,sort_keys=True),flush=True)
    return process_code

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request",type=Path,default=REQUEST)
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args()
    item=read(args.request);guard(item,args.request)
    return compute(item,args.out)

if __name__=="__main__":
    raise SystemExit(main())
