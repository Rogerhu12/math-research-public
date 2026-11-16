#!/usr/bin/env python3
"""R883 source-bound standard-library transport, execution and complete output IO."""
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
TOPIC=S.parent
REQUEST=TOPIC/"notes/R883-original-t-first-order-frame-public-request.json"
RESULT="R883-original-t-first-order-frame"
FINAL="p41-original-t-first-order-frame-certificate.json"
CORE="R883_original_t_first_order_frame.py"
MANIFEST="full-outputs-manifest.json"
REFERENCE="full-outputs-manifest-reference.json"
INVENTORY="R883-original-source-inventory.json"
RETAINED="R883-retained-original-sources-receipt.json"
HELPER_SHA="c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c"
SOURCE_KEYS=("result","run_id","source_commit","core_sha256","manifest_sha256")
META=("public-actions-input.json","run-receipt.json","core-receipt.json")
ANCHORS={"R807":"R807-original-nonzero-pole-clearing-theta.json.gz",
         "R801":"R801-original-recipe-dependency-plan.json.gz",
         "R872":"R872-source-audit.json.gz"}

def fingerprint(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda:f.read(4*1024*1024),b""):
            h.update(block)
    return h.hexdigest()

def spec(path):
    p=Path(path)
    return {"file":p.name,"bytes":p.stat().st_size,"sha256":sha(p)}

def plain(value):
    r={k:value[k] for k in ("file","bytes","sha256")}
    assert isinstance(r["file"],str) and Path(r["file"]).name==r["file"]
    assert r["file"] not in (".","..") and "\\" not in r["file"]
    assert isinstance(r["bytes"],int) and r["bytes"]>=0
    assert re.fullmatch("[0-9a-f]{64}",r["sha256"])
    return r

def read(path):
    p=Path(path)
    with (gzip.open(p,"rt",encoding="utf-8") if p.suffix==".gz" else p.open(encoding="utf-8")) as f:
        return json.load(f)

def save(path,value):
    p=Path(path);p.parent.mkdir(parents=True,exist_ok=True)
    q=p.with_name(p.name+".tmp")
    q.write_text(json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False)+"\n",encoding="utf-8")
    q.replace(p)

def bound(folder,value):
    value=plain(value);p=Path(folder)/value["file"]
    assert spec(p)==value,p.name
    return p

def topic_path(name):
    p=PurePosixPath(name)
    assert not p.is_absolute() and ".." not in p.parts
    q=(TOPIC/str(p)).resolve()
    assert q.is_relative_to(TOPIC.resolve())
    return q

def identity(value):
    return {k:value[k] for k in SOURCE_KEYS}

def guard(item):
    assert os.environ.get("GITHUB_ACTIONS")=="true"
    assert os.environ.get("GITHUB_REPOSITORY")=="Rogerhu12/math-research-public"
    assert item["schema"]==1 and item["result"]==RESULT and item["p"]==41
    assert item["producer_inputs_pending"] is False
    assert item["core"]==CORE and sha(S/CORE)==item["core_sha256"]
    assert item["wrapper"]==Path(__file__).name and sha(__file__)==item["wrapper_sha256"]
    assert 0<item["budget_minutes"]<=300
    assert sha(REPO/"README.md")==item["readme_sha256"]["root"]
    assert sha(TOPIC/"README.md")==item["readme_sha256"]["topic"]
    assert sha(topic_path(item["method"]))==item["method_sha256"]
    for row in item["proofs"].values():
        assert sha(topic_path(row["path"]))==row["sha256"]
    helper=S/"R824_public_original_global_polar_generators.py"
    assert item["io_helper"]==helper.name and item["io_helper_sha256"]==sha(helper)==HELPER_SHA
    ms=importlib.util.spec_from_file_location("R883_retained_stdlib_IO",helper)
    module=importlib.util.module_from_spec(ms);ms.loader.exec_module(module)
    return module

def intake(item,out,work,IO):
    pinned=item["intake"]
    archive=IO.Archive(pinned,work/"intake-transport",whole=True)
    try:
        r=plain(pinned["source_index"])
        archive.extract_bound(r["file"],r["sha256"],out/r["file"],r["bytes"])
        index=read(out/r["file"])
        assert index["schema"]==1 and index["new_mathematics_executed"] is False and index["errors"]==[]
        assert str(index["workflow_run_id"])==str(pinned["run_id"])
        assert index["source_commit"]==pinned["source_commit"] and index["request_sha256"]==pinned["request_sha256"]
        entries={r["label"]:r for r in index["sources"]}
        assert set(entries)=={v["intake_label"] for v in item["sources"].values()} and len(entries)==3
        wanted={pinned["source_index"]["file"]}
        for label,src in item["sources"].items():
            row=entries[src["intake_label"]]
            assert identity(row["source"])==identity(src["source"])
            assert plain(row["retained_input_bundle"])==plain(pinned["bundles"][label])
            for kind in ("summary","retained_input_bundle"):
                r=plain(row[kind])
                archive.extract_bound(r["file"],r["sha256"],out/r["file"],r["bytes"])
                wanted.add(r["file"])
        assert set(archive.by_name)==wanted
        return archive.receipt()
    finally:
        archive.close()

def unpack(bundle,directory,files):
    directory.mkdir(parents=True,exist_ok=True);seen=set()
    with tarfile.open(bundle,"r|gz") as tar:
        for member in tar:
            name=PurePosixPath(member.name)
            assert member.isfile() and len(name.parts)==2 and name.parts[0]=="original"
            assert not name.is_absolute() and ".." not in name.parts and "\\" not in member.name
            base=name.name
            assert base in files and base not in seen
            seen.add(base);ref=plain(files[base]);assert member.size==ref["bytes"]
            stream=tar.extractfile(member);assert stream is not None
            target=directory/base;temp=target.with_name(target.name+".tmp")
            h=hashlib.sha256();count=0
            with temp.open("wb") as f:
                for block in iter(lambda:stream.read(4*1024*1024),b""):
                    f.write(block);h.update(block);count+=len(block)
            assert count==ref["bytes"] and h.hexdigest()==ref["sha256"]
            if target.exists():
                assert spec(target)==ref;temp.unlink()
            else:
                temp.replace(target)
    assert seen==set(files)

def prepare(item,out,work):
    pinned=item["intake"]
    index=read(bound(out,pinned["source_index"]))
    assert str(index["workflow_run_id"])==str(pinned["run_id"])
    assert index["source_commit"]==pinned["source_commit"] and index["request_sha256"]==pinned["request_sha256"]
    assert index["errors"]==[] and index["new_mathematics_executed"] is False
    entries={r["label"]:r for r in index["sources"]}
    sources={};summaries={};total=0
    for label,src in item["sources"].items():
        entry=entries[src["intake_label"]]
        assert identity(entry["source"])==identity(src["source"])
        summary=read(bound(out,entry["summary"]));summaries[label]=plain(entry["summary"])
        assert summary["source"]==entry["source"] and summary["label"]==src["intake_label"]
        assert summary["original_result"]==src["source"]["result"]
        assert summary["source_core_sha256"]==src["source"]["core_sha256"]
        assert summary["new_mathematics_executed"] is False
        files={n:plain(v) for n,v in summary["selected_files"].items()}
        assert len(files)==summary["selected_file_count"]==src["selected_file_count"]
        files[MANIFEST]=plain(summary["manifest"])
        files[REFERENCE]=plain(summary["manifest_reference"])
        assert files[MANIFEST]["sha256"]==src["source"]["manifest_sha256"]
        assert files[MANIFEST]["bytes"]==src["source"]["manifest_bytes"]
        assert summary["original_manifest_count"]==src["source"]["manifest_file_count"]
        for row in src["file_pins"]:
            assert files[row["file"]]==plain(row)
        bundle=plain(entry["retained_input_bundle"])
        assert bundle==plain(summary["retained_input_bundle"])==plain(pinned["bundles"][label])
        folder=work/"retained"/label
        unpack(bound(out,bundle),folder,files)
        manifest=read(folder/MANIFEST)
        assert manifest["result"]==src["source"]["result"]
        originals={r["file"]:plain(r) for r in manifest["files"]}
        assert len(originals)==len(manifest["files"])==src["source"]["manifest_file_count"]
        for name,row in files.items():
            bound(folder,row)
            if name not in (MANIFEST,REFERENCE):
                assert originals[name]==row
        reference=read(folder/REFERENCE)
        if "manifest" in reference:
            assert plain(reference["manifest"])==files[MANIFEST]
        elif all(k in reference for k in ("file","bytes","sha256")):
            assert plain(reference)==files[MANIFEST]
        else:
            assert reference["manifest_sha256"]==files[MANIFEST]["sha256"]
            assert reference["manifest_bytes"]==files[MANIFEST]["bytes"]
        initial,run,core=[read(folder/name) for name in META]
        assert initial["result"]==run["result"]==core["result"]==src["source"]["result"]
        assert initial["source_commit"]==run["source_commit"]==src["source"]["source_commit"]
        assert str(run["workflow_run_id"])==str(src["source"]["run_id"])
        assert initial["core_sha256"]==core.get("source_sha256",core.get("core_sha256"))==src["source"]["core_sha256"]
        assert initial.get("driver_sha256",initial.get("wrapper_sha256"))==summary["source_wrapper_sha256"]
        assert run["complete"] is True and run["process_exit_code"]==0 and run["error"] is None
        assert run["core_receipt_sha256"]==files[META[2]]["sha256"] and core["complete"] is True
        cert_name=src["certificate_name"]
        cert=read(folder/cert_name)
        assert files[cert_name]["sha256"]==src["certificate_sha256"]
        assert cert["result"]==src["source"]["result"] and cert["complete"] is True
        assert core["certificate_sha256"]==files[cert_name]["sha256"]
        anchor=read(folder/ANCHORS[label]);cfg=anchor["configuration"]
        assert anchor["complete"] is True
        assert cfg["result"]==src["source"]["result"] and cfg["source_sha256"]==src["source"]["core_sha256"]
        if "configuration" in cert:
            assert cert["configuration"]==cfg
        for ref in src["file_pins"]:
            stage=read(folder/ref["file"])
            assert stage["complete"] is True and stage["configuration"]==cfg
        sources[label]={"identity":identity(src["source"]),"directory":str(folder.resolve()),
            "files":files,"configuration_sha256":fingerprint(cfg),
            "certificate":files[cert_name],"wrapper_sha256":summary["source_wrapper_sha256"]}
        total+=len(files)
    assert total==28
    stable={label:{k:v[k] for k in ("identity","files","configuration_sha256","certificate","wrapper_sha256")}
            for label,v in sources.items()}
    tag={"result":RESULT,"source_sha256":item["core_sha256"],"p":41,
        "prime":1000000753,"original_zeta_root":549966761,"original_s_root":99932770,
        "orders":3,"python_arithmetic":"standard_library_integer_modular_arithmetic",
        "method_sha256":item["method_sha256"],"proofs":item["proofs"],
        "sources":stable,
        "strategy":"original_R807_two_V4_sections_and_theta_on_original_R872_first_three_jets; unit_denominator_only",
        "old_Hensel_inverse_or_q_coefficients_recomputed":False,
        "modular_zero_used_as_exact_vanishing":False,
        "characteristic_zero_c_expanded":False}
    inventory={"result":RESULT,"sources":stable,"actual_selected_original_file_count":total}
    save(out/INVENTORY,inventory)
    receipt={"result":RESULT,"complete":True,"intake":pinned,"summary_files":summaries,
        "source_inventory":spec(out/INVENTORY),"actual_selected_original_file_count":total,
        "all_original_members_and_producer_identities_verified":True,"new_mathematics_executed":False}
    save(out/RETAINED,receipt)
    return dict(item,prepared_sources=sources,actual_configuration=tag),receipt

def restore(item,out,work,IO):
    source=item.get("resume")
    if source is None:
        return False
    assert source["result"]==RESULT and source["core_sha256"]==item["core_sha256"]
    assert source["wrapper_sha256"]==item["wrapper_sha256"]
    a=IO.Archive(source,work/"resume-transport",whole=True)
    folder=work/"previous";folder.mkdir(parents=True,exist_ok=True)
    try:
        m=plain(source["manifest"])
        a.extract_bound(m["file"],m["sha256"],folder/m["file"],m["bytes"])
        manifest=read(folder/MANIFEST)
        assert manifest["result"]==RESULT
        entries={r["file"]:plain(r) for r in manifest["files"]}
        assert len(entries)==len(manifest["files"]) and set(a.by_name)==set(entries)|{MANIFEST,REFERENCE}
        for r in entries.values():
            a.extract_bound(r["file"],r["sha256"],folder/r["file"],r["bytes"])
        initial=read(folder/META[0]);run=read(folder/META[1])
        assert initial["result"]==run["result"]==RESULT
        assert initial["source_commit"]==run["source_commit"]==source["source_commit"]
        assert str(run["workflow_run_id"])==str(source["run_id"])
        assert initial["core_sha256"]==item["core_sha256"] and initial["driver_sha256"]==item["wrapper_sha256"]
        for key in ("method_sha256","proofs","sources"):
            assert initial["job"][key]==item[key]
        if run.get("core_receipt_sha256") is not None:
            assert entries[META[2]]["sha256"]==run["core_receipt_sha256"]
        else:
            assert run["complete"] is False
        index=read(bound(folder,item["intake"]["source_index"]))
        names=[item["intake"]["source_index"]["file"]]
        for row in index["sources"]:
            names.extend([row["summary"]["file"],row["retained_input_bundle"]["file"]])
        for name in names:
            assert name in entries;shutil.copyfile(folder/name,out/name)
        for name in entries:
            if name.startswith("R883-") and name.endswith(".json.gz"):
                d=read(folder/name)
                assert d["result"]==RESULT and d["complete"] is True and d["configuration"]==initial["actual_configuration"]
                shutil.copyfile(folder/name,out/name)
        if FINAL in entries:
            c=read(folder/FINAL)
            assert c["configuration"]==initial["actual_configuration"]
            if c["complete"] is True:
                shutil.copyfile(folder/FINAL,out/FINAL)
        save(out/"resume-import-receipt.json",{"result":RESULT,"source":source,
            "configuration_sha256":fingerprint(initial["actual_configuration"]),
            "retained_completed_stages_reused":True,"new_mathematics_executed":False})
        return initial["actual_configuration"]
    finally:
        a.close()

def output_manifest(out):
    files=[spec(p) for p in sorted(out.iterdir()) if p.is_file() and p.name not in (MANIFEST,REFERENCE)
           and not p.name.endswith((".tmp",".download",".partial"))]
    save(out/MANIFEST,{"result":RESULT,"source_commit":os.environ["GITHUB_SHA"],
        "workflow_run_id":os.environ["GITHUB_RUN_ID"],"files":files})
    save(out/REFERENCE,{"result":RESULT,**spec(out/MANIFEST)})
    return spec(out/MANIFEST)

def verify(item,out):
    m=read(out/MANIFEST);assert m["result"]==RESULT
    entries={r["file"]:plain(r) for r in m["files"]}
    assert len(entries)==len(m["files"])
    for r in entries.values():
        bound(out,r)
    assert plain(read(out/REFERENCE))==spec(out/MANIFEST)
    run=read(out/META[1])
    assert run["result"]==RESULT and run["source_commit"]==os.environ["GITHUB_SHA"]
    if META[0] not in entries:
        assert run["complete"] is False
        return {"complete":False,"source_preparation_failed":True,"manifest":spec(out/MANIFEST)}
    initial=read(out/META[0]);tag=initial["actual_configuration"]
    assert tag["result"]==RESULT and tag["source_sha256"]==item["core_sha256"]
    assert initial["driver_sha256"]==item["wrapper_sha256"] and initial["job"]==item
    stages={}
    for name,row in entries.items():
        if name.startswith("R883-") and name.endswith(".json.gz"):
            d=read(out/name)
            assert d["result"]==RESULT and d["configuration"]==tag and d["complete"] is True
            stages[name]=row
    cert=None
    if FINAL in entries:
        cert=read(out/FINAL)
        assert cert["result"]==RESULT and cert["configuration"]==tag
        if cert["complete"] is True:
            assert run["complete"] is True and run["process_exit_code"]==0 and run["error"] is None
            assert cert["actual_complete_math_stage_count"]==5
            for r in cert["stages"].values():
                assert stages[r["file"]]==plain(r)
            assert cert["actual_original_t_first_order_unit_certified"] is True
            assert cert["original_t_frame_DAG_source_certified"] is True
            for key in ("old_Hensel_jets_inverse_q_tail_or_basis_recomputed",
                        "characteristic_zero_c_expanded","all_Picard_frames_evaluated",
                        "five_original_Lj_RR128_or144_computed","height_or_period_computed"):
                assert cert[key] is False
            f=read(out/"R883-original-t-first-order-unit-and-frame-DAG.json.gz")
            assert f["original_t_first_order_unit_certified"] is True
            assert f["quotient_all_three_coefficients_multiplied_back"] is True
            assert f["exact_zero_not_inferred_from_modular_zero"] is True
            assert f["original_t_first_three_coefficients_mod_prime"][0]==0
            assert 0<f["original_t_over_rho_constant_mod_prime"]<1000000753
            assert f["exact_characteristic_zero_c_rational_expansion_computed"] is False
    if run["core_receipt_sha256"] is not None:
        assert entries[META[2]]["sha256"]==run["core_receipt_sha256"]
        core=read(out/META[2])
        assert core["source_sha256"]==item["core_sha256"] and core["result"]==RESULT
        assert core["configuration_sha256"]==fingerprint(tag)
        if run["complete"]:
            assert core["complete"] is True and core["certificate_sha256"]==entries[FINAL]["sha256"]
    else:
        assert run["complete"] is False
    review={"result":RESULT,"complete":run["complete"],"process_exit_code":run["process_exit_code"],
        "manifest":spec(out/MANIFEST),"source_inventory":entries.get(INVENTORY),
        "actual_complete_math_stage_count":len(stages),
        "certificate":entries.get(FINAL),"stages":stages,
        "new_mathematics_executed_in_IO_review":False}
    if cert and cert["complete"]:
        f=read(out/"R883-original-t-first-order-unit-and-frame-DAG.json.gz")
        review["frame_summary"]={k:f[k] for k in ("original_t_first_three_coefficients_mod_prime",
            "original_t_over_rho_constant_mod_prime","actual_c_powers_mod_prime",
            "N693_constant_mod_prime","N693_constant_inverse_mod_prime",
            "exact_c_expression","original_t_first_order_unit_certified")}
    return review

def compute(item,out,IO):
    out.mkdir(parents=True,exist_ok=True);work=out.parent/"R883-working"
    work.mkdir(parents=True,exist_ok=True)
    code=1;error=None;outer=False;expanded=None;transport=None
    try:
        oldtag=restore(item,out,work,IO)
        if oldtag is False:
            transport=intake(item,out,work,IO)
        expanded,receipt=prepare(item,out,work)
        if oldtag is not False:
            assert oldtag==expanded["actual_configuration"]
        save(work/"expanded-job.json",expanded)
        save(out/META[0],{"result":RESULT,"source_commit":os.environ["GITHUB_SHA"],
            "workflow_run_id":os.environ["GITHUB_RUN_ID"],"workflow_attempt":os.environ.get("GITHUB_RUN_ATTEMPT","1"),
            "core_sha256":item["core_sha256"],"driver_sha256":item["wrapper_sha256"],
            "request_sha256":sha(REQUEST),"job":item,"actual_configuration":expanded["actual_configuration"],
            "retained_inputs":spec(out/RETAINED),"source_inventory":spec(out/INVENTORY),"transport":transport,
            "execution_environment":"public-repository-github-actions"})
        command=[sys.executable,"-u",str(S/CORE),"--config",str(work/"expanded-job.json"),
            "--out",str(out),"--budget-minutes",str(item["budget_minutes"])]
        with (out/"core.log").open("ab",buffering=0) as log:
            child=subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
            try:
                code=child.wait(timeout=60*item["budget_minutes"]+180)
            except subprocess.TimeoutExpired:
                outer=True;code=124;os.killpg(child.pid,signal.SIGTERM)
                try:
                    child.wait(timeout=15)
                except subprocess.TimeoutExpired:
                    os.killpg(child.pid,signal.SIGKILL);child.wait()
        if (out/"core.log").exists():
            print((out/"core.log").read_text(errors="replace")[-12000:],flush=True)
    except BaseException as exc:
        traceback.print_exc();error={"type":type(exc).__name__,"message":str(exc)};code=1
    finally:
        core=read(out/META[2]) if (out/META[2]).exists() else None
        complete=bool(code==0 and core and core["complete"] and (out/FINAL).exists())
        save(out/META[1],{"result":RESULT,"complete":complete,"process_exit_code":code,
            "error":error,"outer_timeout":outer,"source_commit":os.environ["GITHUB_SHA"],
            "workflow_run_id":os.environ["GITHUB_RUN_ID"],"workflow_attempt":os.environ.get("GITHUB_RUN_ATTEMPT","1"),
            "core_receipt_sha256":sha(out/META[2]) if core else None,
            "finished_at_utc":dt.datetime.now(dt.timezone.utc).isoformat()})
        output_manifest(out)
    review=verify(item,out)
    print("R883_COMPLETE_IO_REVIEW="+json.dumps(review,sort_keys=True),flush=True)
    return code

def main():
    sys.set_int_max_str_digits(0)
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("mode",choices=("compute","verify"))
    p.add_argument("--output",type=Path,required=True)
    a=p.parse_args();item=read(REQUEST);IO=guard(item)
    if a.mode=="compute":
        raise SystemExit(compute(item,a.output,IO))
    print("R883_COMPLETE_IO_REVIEW="+json.dumps(verify(item,a.output),sort_keys=True),flush=True)

if __name__=="__main__":
    main()
