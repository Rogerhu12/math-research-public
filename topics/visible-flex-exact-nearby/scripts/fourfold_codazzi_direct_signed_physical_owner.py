"""First signed direct physical Theta and recovered original coordinates for both negative waists and the strict column."""
import argparse
import ast
import base64
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import platform
import subprocess
import sys
import time
import traceback

TOPIC="topics/visible-flex-exact-nearby"
REPO="Rogerhu12/math-research-public"
KIND="R149_three_direct_signed_physical_Theta_and_recovered_columns_v1"
MANIFEST_KIND="R149_three_direct_signed_physical_Theta_and_recovered_columns_inputs_v1"
RUNTIME={"python":"3.12.14","packages":{"numpy":"2.3.5","python-flint":"0.9.0"}}
PARAMETERS={"columns":["negative_newton_zero_root","negative_nu_defect_zero_root","original_strict_nu"],
            "arithmetic_bits":320,"source_extent":512,"dense_trial_extent":1024,
            "complete_signed_head":4096,"grid":8192,"coordinate_rows":96,"maximum_actual_bytes":95000,
            "maximum_scientific_seconds":19500,"private_disk_limit_bytes":12884901888}
TARGETS=["two_actual_negative_forward_columns_with_complete_errors","three_signed_direct_true_Theta_columns",
         "three_signed_recovered_true_low_coordinate_columns","all_original_independent_characteristic_means"]
FIELDS=("kind","identity","parameters","runtime","original_input_identity","parents","complete","proved",
        "stage","progress","failure","actual_returncode","wall_seconds","completed_targets","saved_record_count",
        "new_records","private_objects","whole_batch_prefix","carrier_restoration","old_scientific_targets_called",
        "new_arrays_published","new_artifacts","new_Releases")
DCP_SHA="2f90550a3c44e3b2a6c434179992dec191da149d08cfdc7876d379d4522c5e5b"
DCP_MANIFEST="d85c0d55f82e50d9f061756a4d132db6780992654f3c01fbf5ae9a03657c44df"
ASQ23_MANIFEST="1f6734a0decbaa7eabe8236723a0b3929908176811854cabba5b189b0e73f04c"
ASQ23_SOURCE="23d172da685dda01620f4ec4f041f9d8c7a4aa10c4442f4ddeabdf7c505fd736"
DIRECT_SHA="90998d0e922eae9ed68b55c4414abe9c9d6353031ebe0c0f5203dde795d9b6c0"
PROOF_SHA="84650b627b9dc560a9fc96ffe41623710706c1110e0f3868237277a8eb4d1f2c"


def require(ok,message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()


def load(path,label):
    p=Path(path)
    ast.parse(p.read_bytes(),filename=str(p))
    spec=importlib.util.spec_from_file_location(label,p)
    mod=importlib.util.module_from_spec(spec)
    sys.modules[label]=mod
    spec.loader.exec_module(mod)
    return mod


def verify_file(root,spec):
    from pathlib import PurePosixPath
    path=PurePosixPath(spec["path"])
    require(not path.is_absolute() and ".." not in path.parts and spec["path"].startswith(TOPIC+"/"),
            "a complete original topic path")
    raw=(root/path).read_bytes()
    require(len(raw)==spec["bytes"] and sha(raw)==spec["sha256"] and
            hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()==spec["git_blob_sha"],
            "entire source and native Git identity: "+str(path))
    return raw


def admit(root,raw,digest,rows_index):
    root=Path(root)
    require(len(raw)<100000 and sha(raw)==digest,"one complete new manifest")
    m=json.loads(raw)
    require(m["kind"]==MANIFEST_KIND and m["scientific_kind"]==KIND and m["repository"]==REPO and
            m["target_order"]==TARGETS and m["parameters"]==PARAMETERS and m["runtime"]==RUNTIME and
            m["allowed_scientific_fields"]==sorted(FIELDS),"same complete new targets")
    roles={s["role"]:s for s in m["files"]}
    require(len(roles)==len(m["files"]) and roles["science"]["sha256"]==sha(Path(__file__).read_bytes()) and
            roles["direct"]["sha256"]==DIRECT_SHA and roles["proof"]["sha256"]==PROOF_SHA and
            roles["DCP_manifest"]["sha256"]==DCP_MANIFEST and roles["DCP_actual"]["sha256"]==DCP_SHA and
            roles["ASQ23_manifest"]["sha256"]==ASQ23_MANIFEST and roles["ASQ23_science"]["sha256"]==ASQ23_SOURCE,
            "immutable full source identities")
    raws={role:verify_file(root,s) for role,s in roles.items()}
    def module(role):
        return load(root/roles[role]["path"],"_ASQ25_"+role)
    nm=json.loads(raws["ASQ23_manifest"])
    no=module("ASQ23_science")
    require(no.MANIFEST_KIND==nm["kind"] and nm["target_order"]==no.TARGETS and
            m["whole_original_descriptors"]==nm["whole_original_descriptors"],"original ASQ23 complete definition")
    unused,unused_roles,ancestry=no.admit(root,raws["ASQ23_manifest"],ASQ23_MANIFEST,rows_index)
    neg,ne,marker=(json.loads(raws["ASQ23_"+key]) for key in ("actual","execution","consumed"))
    no.validate(neg,nm)
    ni=neg["identity"]
    require(neg["complete"] is neg["proved"] is ne["complete"] is True and
            ni["run_id"]==ne["run_id"]==marker["run_id"]=="46144609049" and
            ni["run_attempt"]==str(ne["run_attempt"])==str(marker["run_attempt"])=="1" and
            ni["workflow_event_commit"]==ne["event_commit"]=="35c012f749d84448a64ddfa8ac15a34e3fa7cd20" and
            ni["manifest_sha256"]==ne["manifest_sha256"]==marker["manifest_sha256"]==ASQ23_MANIFEST and
            ni["source_sha256"]==ASQ23_SOURCE and ni["actual_scientific_checkout"]==ne["actual_scientific_checkout"] and
            neg["actual_returncode"]==ne["actual_child_returncode"]==0 and ne["scientific_children"]==1 and
            ne["failure"] is neg["failure"] is None and neg["completed_targets"]==ne["completed_natural_targets"]==no.TARGETS and
            neg["complete_suffix"]["count"]==3073 and neg["complete_suffix"]["lower_radius"]=="0" and
            neg["original_input_identity"]==ne["whole_original_input_admission"]==ancestry[-1] and
            any(all(s[k]==roles["ASQ23_actual"][k] for k in ("path","bytes","sha256")) for s in ne["scientific_files"]),
            "real complete ASQ23 first run, both targets, all 3073 cells and two whole physical Grams")
    require(m["parents"]["ASQ23"]=={"run":"46144609049/1","actual":roles["ASQ23_actual"]["sha256"],
        "execution":roles["ASQ23_execution"]["sha256"],"manifest":ASQ23_MANIFEST},"published whole negative parent")
    cfc=module("cfc")
    desc={k:roles["DCP_"+k] for k in ("manifest","actual","execution")}
    parent=cfc.completed_parent(root,desc)
    ds=parent["actual"]["identity"]
    require(ds["run_id"]=="46124617641" and ds["run_attempt"]=="1" and
            ds["event_commit"]=="c1da88994f48c908055120f9f8a0de6e3e463d62" and
            ds["actual_checkout_commit"]=="60a37fea0f57df6c4dedb5addfd1b975a33ab2cd" and
            len(parent["manifest"]["files"])==269 and len(parent["manifest"]["historical_inputs"])==53 and
            len(parent["specs"])==322 and m["parents"]["DCP"]=={"run":"46124617641/1","actual":DCP_SHA,
             "execution":roles["DCP_execution"]["sha256"],"manifest":DCP_MANIFEST},"original successful complete DCP18 all 322 inputs")
    dcp=parent["owner"].admit_complete_inputs(parent["contents"],parent["specs"],parent["manifest"],parent["paths"])
    dcp["completed_actual"]=parent["actual"]
    dcp["BFP_context"]["BFP_owner"]=dcp["BFP_owner"]
    data={"root":root,"ASQ23":neg,"DCP_parent":parent,"dcp":dcp,"PA":json.loads(raws["PA"]),
          "NP":json.loads(raws["NP"]),"raw18":raws["asq18"],"cfc":cfc,"ids":m["parents"]}
    for role in ("recover","carrier","batch","direct","physical"):
        data[role]=module(role)
    require(roles["PA"]["sha256"]=="04d09519aeeaaf7d63d1efcc6ee38481a3cdbf25dfaa9868dd8558ecd4e35387" and
            roles["NP"]["sha256"]=="76f00af5bac4a3c64c414844fe31878bb188af9553bb824b92c0071674fd8e2a" and
            parent["actual"]["copied_complete_input_records"]["prior_two_independent_density_means"] and
            not any(k in sys.modules for k in ("numpy","flint","scipy")),"metadata only, signed means and both genuine physical parents")
    return m,roles,data,ancestry


def validate(doc,m):
    n=doc["saved_record_count"]
    require(set(doc)==set(FIELDS) and doc["parameters"]==PARAMETERS and doc["kind"]==KIND and
            type(n) is int and 0<=n<=len(TARGETS) and doc["completed_targets"]==TARGETS[:n] and
            set(doc["new_records"])==set(TARGETS[:n]) and doc["parents"]==m["parents"] and
            all(doc[k]==0 for k in ("old_scientific_targets_called","new_arrays_published","new_artifacts","new_Releases")),
            "whole exact new target prefix")
    if n>=1:
        r=doc["new_records"][TARGETS[0]]
        require(len(r["complete_forward_errors"])==len(r["complete_two_raw_errors"])==2 and
                set(r["original_raw_cross_Grams"])=={"strict","root"},"both finite columns and cross Grams")
    for j,label in ((1,"signed_columns"),(2,"signed_recovered_columns")):
        if n>j:
            r=doc["new_records"][TARGETS[j]]
            require(len(r[label])==3,"three genuine signed columns")
            for col in r[label]:
                raw=base64.b64decode(col["exact_dyadic_centres_f64_le"],validate=True)
                require(col["rows"]==96 and len(raw)==768 and
                        all(math.isfinite(v[0]) for v in __import__("struct").iter_unpack("<d",raw)) and
                        isinstance(col["joint_error_upper"],str),"all96 signed finite coordinates and one joint radius")
            aux=r["finite_direct_inverse" if j==1 else "combined_residual"]
            require(aux["complete_head"]==4096 and aux["complete_source"]==2560 and aux["infinite_tail_paid"] and
                    len(aux["whole_upper_records"])==len(aux["signed_grid_Gram"])==3,"whole finite and infinite receipts")
    if n==4:
        r=doc["new_records"][TARGETS[3]]
        require(len(r["signed_negative_column_means"])==2 and all(set(v)=={"plus","minus"} for v in
                r["signed_negative_column_means"]+[r["original_strict_independent_means"]]),"all original signed means")
    if doc["complete"]:
        require(doc["proved"] and n==4 and doc["actual_returncode"]==0 and doc["failure"] is None,
                "complete new original signed actions")


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for key in ("repo","manifest","rows-index","out","private"):
        parser.add_argument("--"+key,type=Path,required=True)
    parser.add_argument("--checkout",required=True)
    parser.add_argument("--manifest-sha",required=True)
    parser.add_argument("--carrier-mode",choices=["GRID"])
    parser.add_argument("--carrier-directory",type=Path)
    parser.add_argument("--carrier-receipt",type=Path)
    a=parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS")=="true" and os.environ.get("GITHUB_REPOSITORY")==REPO and
            os.environ.get("GITHUB_RUN_ATTEMPT")=="1","one first genuine public scientific run")
    m,roles,data,ancestry=admit(a.repo,a.manifest.read_bytes(),a.manifest_sha,a.rows_index)
    bfp=data["dcp"]["BFP_context"]
    if a.carrier_mode:
        bfp["BNC"]["owner"].carrier_child(a,bfp["BNC"]["admitted"])
        return
    from importlib.metadata import version
    runtime={"python":platform.python_version(),"packages":{n:version(n) for n in RUNTIME["packages"]}}
    require(runtime==RUNTIME and os.environ.get("OPENBLAS_CORETYPE")=="Haswell" and not a.out.exists(),
            "original runtime and fresh new scientific output")
    started=time.monotonic()
    state=dict(kind=KIND,identity=dict(source_sha256=roles["science"]["sha256"],manifest_sha256=a.manifest_sha,
        run_id=os.environ["GITHUB_RUN_ID"],run_attempt="1",actual_scientific_checkout=a.checkout,
        workflow_event_commit=os.environ["GITHUB_SHA"]),parameters=PARAMETERS,runtime=runtime,
        original_input_identity=ancestry[-1],parents=m["parents"],complete=False,proved=False,stage="whole_parents_admitted",
        progress={},failure=None,actual_returncode=None,wall_seconds=0,completed_targets=[],saved_record_count=0,
        new_records={},private_objects={},whole_batch_prefix=None,carrier_restoration={},
        old_scientific_targets_called=0,new_arrays_published=0,new_artifacts=0,new_Releases=0)
    def save():
        state["wall_seconds"]=time.monotonic()-started
        validate(state,m)
        body=encode(state)
        require(len(body)<PARAMETERS["maximum_actual_bytes"],"whole public carrier within its original budget")
        data["cfc"].atomic(a.out,body)
    def progress(stage,details):
        state["stage"],state["progress"]=stage,details
        save()
        require(time.monotonic()-started<PARAMETERS["maximum_scientific_seconds"],"complete saved before wall limit")
        print(encode({"stage":stage,**details}).decode(),end="",flush=True)
    def publish(index,record):
        require(index==state["saved_record_count"],"genuine ordered new target")
        state["new_records"][TARGETS[index]]=record
        state["completed_targets"].append(TARGETS[index])
        state["saved_record_count"]+=1
        save()
        require(json.loads(a.out.read_bytes())["new_records"][TARGETS[index]]==record,"whole natural target read back")
    save()
    try:
        grid_dir,receipt=a.private/"original-AS",a.private/"original-AS-receipt.json"
        child_args=[sys.executable,"-B",str(Path(__file__).resolve()),*sys.argv[1:],"--carrier-mode","GRID",
                "--carrier-directory",str(grid_dir),"--carrier-receipt",str(receipt)]
        env=dict(os.environ)
        env.pop("OPENBLAS_CORETYPE",None)
        with (a.private/"AS-restoration.log").open("wb") as log:
            child=subprocess.Popen(child_args,stdout=log,stderr=subprocess.STDOUT,env=env)
            try:
                while child.poll() is None:
                    progress("necessary_whole_AS_grid_restoration",{})
                    try:
                        child.wait(timeout=35)
                    except subprocess.TimeoutExpired:
                        pass
            finally:
                if child.poll() is None:
                    child.terminate()
                    try: child.wait(timeout=15)
                    except subprocess.TimeoutExpired:
                        child.kill()
                        child.wait()
        r=json.loads(receipt.read_bytes())
        require(r["complete"] and r["failure"] is None and child.returncode==0,"same original AS grid only")
        state["carrier_restoration"]["AS"]=r
        import numpy as np
        import flint
        flint.ctx.prec,flint.ctx.cap=320,9
        actual=data["DCP_parent"]["actual"]
        ot=bfp["UACT"]["admitted"]["owner"]
        api=ot.directed_api(flint)
        api.midpoint_real=lambda value:value.mid()
        api.midpoint_complex=lambda value:api.acb(value.real.mid(),value.imag.mid())
        unused,old_roles,raws,helper,prior,rows,ident=ancestry
        tc=load(a.repo/old_roles["trial_math"]["path"],"_ASQ25_TCXV_full_arithmetic")
        backend,br=helper.directed_backend(np,flint,raws[old_roles["box_math"]["path"]],raws[old_roles["fft_math"]["path"]])
        require(br==data["ASQ23"]["source_restoration"]["directed_backend"],"same whole actual negative-column backend")
        c=tc.DirectedContext(np,flint.arb,backend["Box"],backend["CBox"],backend["zeros"],
                             backend["arb_box"],backend["reduce_box"],backend["DirectedFFT"]())
        io=data["cfc"].PrivateStore(a.private/"new-whole-signed-science",c,api,state,save)
        data["physical"].run(data,a.private,(grid_dir/"complete-original-AS-grid.json").read_bytes(),np,flint,api,c,
                             io,state,progress,publish)
        require(state["saved_record_count"]==4,"every original signed physical column and both means actually finished")
        state.update(complete=True,proved=True,actual_returncode=0,stage="complete")
        save()
    except BaseException as exc:
        state.update(failure={"type":type(exc).__name__,"message":str(exc),"traceback":traceback.format_exc()},
                     actual_returncode=1,stage="failed_with_complete_prefix")
        save()
        raise


if __name__=="__main__":
    main()
