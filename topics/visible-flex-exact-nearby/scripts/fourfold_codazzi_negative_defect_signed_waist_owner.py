"""First directed signed negative waist responses to the selected Newton and q_nu-Z sources."""
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
import signal
import sys
import time
import traceback

TOPIC="topics/visible-flex-exact-nearby"
REPOSITORY="Rogerhu12/math-research-public"
KIND="R149_negative_solutions_signed_joint_waists_v1"
MANIFEST_KIND="R149_negative_solutions_signed_joint_waists_inputs_v1"
TARGETS=["two_signed_negative_waist_centres_and_full_joint_residual_Grams",
         "true_negative_waist_and_Theta_error_for_each_column_and_every_real_combination"]
RUNTIME={"python":"3.12.14","packages":{"numpy":"2.3.5","python-flint":"0.9.0"}}
PARAMETERS={"arithmetic_bits":320,"angular_grid":1024,"negative_cells":3073,"rows":193,
    "residual_quarter_degree":288,"columns":["ordinary_Newton_minus_f_delta","ordinary_nu_proposal_defect_s_delta"],
    "origin":"true_unknown_root","strict_root_split":"2333968743003/10000000000000",
    "mixed_weight_exponent":"1/3","maximum_actual_bytes":90000,
    "maximum_private_bytes":8589934592,"maximum_aggregate_rss":15032385536,"maximum_scientific_seconds":19500}
FIELDS=("kind","identity","parameters","runtime","original_input_identity","source_restoration","plan",
        "complete","proved","stage","failure","actual_returncode","actual_mathematical_wall_seconds","completed_targets",
        "new_complete_negative_trial_cells","complete_suffix","new_records","actual_resource_peaks",
        "original_success_targets_recomputed","new_arrays_published","new_artifacts","new_Releases")
FIXED={"wss_manifest":"dc6422b48e17064f7493510aa289a6cc9111887c95d7cb38093241663b5c4bb9",
       "wss_science":"d2108940e9f6094651fc62256133fc6a4834efa8f881ffac8ee5d4e26cd626b4",
       "wss_worker":"a7cefd09f678228db19141f111a0277484323677f27fd64f09e8a7e146caa767",
       "wss_actual":"d3135d3cf9855b2312a922c9bfd9162da3debd844855eea22668ba0d8318b16e",
       "wss_execution":"fb1e7e7a828cc8a8086ecd9eb50d96bc895b194a58017271aad210cf986a563a",
       "wss_admission":"763efa2689c82b9daa82132067371ce23887d5a30699cbe637bdcf928c916d97",
       "asq22":"6a3568c62ba7bfff45d2a5509f2721d7581c312602d47afc47f7ab3825f218ee"}

def require(ok,msg):
    if not ok:
        raise ValueError(msg)

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def canonical(v):
    return (json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()

def load(p,name):
    entry=importlib.util.spec_from_file_location(name,p)
    require(entry is not None and entry.loader is not None,"complete source module")
    module=importlib.util.module_from_spec(entry)
    sys.modules[name]=module
    entry.loader.exec_module(module)
    return module

def admit(root,raw,digest,rows_index):
    require(len(raw)<100000 and sha(raw)==digest,"entire new manifest")
    m=json.loads(raw)
    require(m["kind"]==MANIFEST_KIND and m["scientific_kind"]==KIND and m["target_order"]==TARGETS
       and m["parameters"]==PARAMETERS and m["runtime"]==RUNTIME and m["repository"]==REPOSITORY
       and m["allowed_scientific_fields"]==sorted(FIELDS),"whole new science definition")
    roles={s["role"]:s for s in m["files"]}
    require(len(roles)==len(m["files"]) and roles["science"]["sha256"]==sha(Path(__file__).read_bytes())
            and roles["science"]["path"]==TOPIC+"/scripts/"+Path(__file__).name,"entire actually executing owner")
    for role,s in roles.items():
        p=Path(s["path"])
        require(not p.is_absolute() and ".." not in p.parts and str(p).startswith(TOPIC+"/"),"same whole topic")
        body=(root/p).read_bytes()
        require(len(body)==s["bytes"] and sha(body)==s["sha256"] and hashlib.sha1(
            b"blob "+str(len(body)).encode()+b"\0"+body).hexdigest()==s["git_blob_sha"],"whole "+role)
        if p.suffix==".py":
            ast.parse(body,filename=str(p))
    require(all(roles[k]["sha256"]==v for k,v in FIXED.items()),"all original immutable whole sources and actuals")
    def read(k):
        return (root/roles[k]["path"]).read_bytes()
    old=load(root/roles["wss_science"]["path"],"_ASQ23_frozen_WSS_metadata_only")
    wm,wr,admitted=old.admit(root,read("wss_manifest"),FIXED["wss_manifest"],rows_index)
    require(m["whole_original_descriptors"]==wm["whole_original_descriptors"] and len(wr)==19
            and all(roles["wss_"+k]["path"]==v["path"] and roles["wss_"+k]["sha256"]==v["sha256"]
                    for k,v in wr.items()),"all nineteen frozen scientific inputs and complete 184/32 parent")
    d,e,approval=map(json.loads,(read("wss_actual"),read("wss_execution"),read("wss_admission")))
    old.validate(d,wm)
    i=d["identity"]
    require(i["run_id"]==e["run_id"]=="46136409179" and str(e["run_attempt"])==i["run_attempt"]=="1"
        and i["manifest_sha256"]==e["manifest_sha256"]==FIXED["wss_manifest"] and i["source_sha256"]==FIXED["wss_science"]
        and i["actual_scientific_checkout"]==e["actual_scientific_checkout"]
        and i["workflow_event_commit"]==e["event_commit"] and d["complete"] and e["complete"] and d["proved"]
        and e["actual_child_returncode"]==0 and e["scientific_children"]==1 and approval["complete"]
        and approval["actual_original_preflight_identity"]==e["whole_original_input_admission"]==d["original_input_identity"]==admitted[-1]
        and d["new_complete_signed_cells"]==7728 and d["completed_targets"]==e["completed_natural_targets"]==old.TARGETS
        and any(s["path"]==roles["wss_actual"]["path"] and s["sha256"]==FIXED["wss_actual"]
                and s["bytes"]==len(read("wss_actual")) for s in e["scientific_files"]),"real whole WSS run and both original targets")
    require(not any(k in sys.modules for k in ("numpy","flint","scipy")),"all current and historical inputs before numerical import")
    return m,roles,admitted

def validate(d,m):
    require(set(d)==set(FIELDS) and d["kind"]==KIND and d["parameters"]==m["parameters"] and d["runtime"]==RUNTIME
        and all(d[k]==0 for k in ("original_success_targets_recomputed","new_arrays_published","new_artifacts","new_Releases")),
        "whole signed negative scope")
    n=d["new_complete_negative_trial_cells"]
    suffix=d["complete_suffix"]
    require(type(n) is int and 0<=n<=PARAMETERS["negative_cells"] and (suffix is None)==(n==0),"complete suffix count")
    if n:
        b=base64.b64decode(suffix["lower_trace_f64_le_base64"],validate=True)
        require(len(b)==193*2*8 and sha(b)==suffix["lower_trace_sha256"] and suffix["count"]==n
                and suffix["whole_trial_bytes"]==n*4*len(b) and len(suffix["ordered_hash_chain"])==len(suffix["whole_trial_sha256"])==64
                and set(suffix["grams"])=={"strict","root"},"the whole two-column lower boundary and all suffix Grams")
        for table in suffix["grams"].values():
            require(len(table)==len(table[0])==len(table[1])==2 and table[0][1]==table[1][0]
                    and all(len(x)==2 and math.isfinite(float.fromhex(x[0])) and math.isfinite(float.fromhex(x[1]))
                            and float.fromhex(x[0])<=float.fromhex(x[1]) for row in table for x in row),
                    "both signed off-diagonal and diagonal outward bounds")
    count=len(d["completed_targets"])
    require(d["completed_targets"]==TARGETS[:count] and set(d["new_records"])==set(d["completed_targets"])
            and (not count or (n==3073 and suffix["lower_radius"]=="0")),"whole natural target order")
    if count:
        r=d["new_records"][TARGETS[0]]
        require(r["trace"]["sha256"]==suffix["whole_trial_sha256"] and r["trace"]["bytes"]==suffix["whole_trial_bytes"]
                and r["trace"]["ordered_hash_chain"]==suffix["ordered_hash_chain"] and r["trace"]["shape"]==[3073,4,193,2]
                and r["trace"]["complete_cells"]==3073,"whole signed two-column cubic from root to waist")
    if count==2:
        r=d["new_records"][TARGETS[1]]
        require(set(r)=={"joint_formula","radii","waist_indexing","root_zero_and_all_interfaces_exact"}
                and r["root_zero_and_all_interfaces_exact"] and len(r["radii"])==2
                and all(set(v)=={"raw_waist","x","x_high","Theta","T_inverse_Theta","each_density_mean"}
                        and all(math.isfinite(float.fromhex(x)) and float.fromhex(x)>=0 for x in v.values()) for v in r["radii"]),
                "both original Newton/nu error receivers with full cross rows retained")
    if d["complete"]:
        require(count==2 and d["proved"] and d["actual_returncode"]==0 and d["failure"] is None,"both genuine new targets")

def execute(args):
    from fractions import Fraction
    from importlib.metadata import version
    root,manifest,private,out=map(Path,(args.repo,args.manifest,args.private,args.out))
    m,r,admitted=admit(root,manifest.read_bytes(),args.manifest_sha,args.rows_index)
    if args.preflight_only:
        print(canonical({"whole_original_identity":admitted[-1],"new_scientific_calls":0,"new_targets":TARGETS}).decode(),end="")
        return 0
    require(os.environ.get("GITHUB_ACTIONS")=="true" and os.environ.get("GITHUB_REPOSITORY")==REPOSITORY
        and os.environ.get("GITHUB_RUN_ATTEMPT")=="1" and platform.python_version()==RUNTIME["python"]
        and all(version(k)==v for k,v in RUNTIME["packages"].items()) and all(os.environ.get(k)=="1" for k in
        ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS")),"actual public first execution and fixed runtime")
    import numpy as np
    import flint
    flint.ctx.prec=PARAMETERS["arithmetic_bits"]
    def module(role):
        return load(root/r[role]["path"],"_ASQ23_"+role)
    core,positive,field,np_math,maths,resources,disk=map(module,("wss_raw_input_helper","wss_positive_signed_source",
        "wss_carrier","nu_math","math","wss_resource_carriers","wss_resource_directory"))
    original,old_roles,raws,helper,prior,rows,ident=admitted
    tc=load(root/old_roles["trial_math"]["path"],"_ASQ23_full_signed_Fourier")
    wss=json.loads((root/r["wss_actual"]["path"]).read_bytes())
    require(not out.exists(),"one first owner outcome")
    begun=time.monotonic()
    state=dict(kind=KIND,identity=dict(manifest_sha256=args.manifest_sha,source_sha256=r["science"]["sha256"],
        run_id=os.environ["GITHUB_RUN_ID"],run_attempt="1",actual_scientific_checkout=args.checkout,workflow_event_commit=os.environ["GITHUB_SHA"]),
        parameters=PARAMETERS,runtime=RUNTIME,original_input_identity=ident,source_restoration=None,plan=None,complete=False,proved=False,
        stage="whole_original_admission",failure=None,actual_returncode=None,actual_mathematical_wall_seconds=0.,
        completed_targets=[],new_complete_negative_trial_cells=0,complete_suffix=None,new_records={},
        actual_resource_peaks={"aggregate_rss":0,"private_and_native_bytes":0},original_success_targets_recomputed=0,
        new_arrays_published=0,new_artifacts=0,new_Releases=0)
    def save():
        state["actual_mathematical_wall_seconds"]=time.monotonic()-begun
        validate(state,m)
        body=canonical(state)
        require(len(body)<=PARAMETERS["maximum_actual_bytes"],"whole small actual")
        core.atomic(out,body)
    def progress(name,detail):
        print(json.dumps(dict(stage=name,**detail),sort_keys=True),flush=True)
    def stop(signum,frame):
        raise TimeoutError("preserve every last whole reverse suffix")
    signal.signal(signal.SIGTERM,stop)
    last_disk=0.
    def budget():
        nonlocal last_disk
        now=time.monotonic()
        peaks=state["actual_resource_peaks"]
        peaks["aggregate_rss"]=max(peaks["aggregate_rss"],resources.aggregate_rss_bytes([]))
        if now-last_disk>20:
            peaks["private_and_native_bytes"]=max(peaks["private_and_native_bytes"],disk.private_bytes((root,private)))
            last_disk=now
        require(peaks["aggregate_rss"]<=PARAMETERS["maximum_aggregate_rss"] and peaks["private_and_native_bytes"]<=PARAMETERS["maximum_private_bytes"]
                and now-begun<PARAMETERS["maximum_scientific_seconds"],"complete resource budget")
    save()
    try:
        budget()
        base,direction,offsets,rows,receipt=core.raw_inputs(np,flint,admitted,root,private,progress)
        require(receipt==wss["source_restoration"],"same whole raw repaired cubics, same selected true original")
        state["source_restoration"]=receipt
        backend,br=helper.directed_backend(np,flint,raws[old_roles["box_math"]["path"]],raws[old_roles["fft_math"]["path"]])
        require(br==receipt["directed_backend"],"same complete directed arithmetic")
        c=tc.DirectedContext(np,flint.arb,backend["Box"],backend["CBox"],backend["zeros"],
                             backend["arb_box"],backend["reduce_box"],backend["DirectedFFT"]())
        read=lambda r:field.historical_ball(flint,r)
        plan=field.partition(helper,rows,base,direction)
        descr=canonical([[j,k,str(a),str(b)] for j,k,a,b in plan])
        chosen=[p for p in plan if p[2]<helper.ROOT[1]]
        require(len(chosen)==3073 and len(plan)==wss["plan"]["pieces"]==7728
            and len(descr)==wss["plan"]["bytes"] and sha(descr)==wss["plan"]["canonical_sha256"],"original whole parent plan and genuine negative cells")
        state["plan"]={"original_whole_sha256":sha(descr),"negative_cells":len(chosen),
             "negative_plan_sha256":sha(canonical([[j,k,str(a),str(b)] for j,k,a,b in chosen])),
             "genuine_root_bracket":[str(x) for x in helper.ROOT],"strict_root_split":str(helper.NEGATIVE_CUT)}
        state["stage"]="signed_backward_trial_and_joint_residual"
        save()
        def checkpoint(n,total,lo,trace,grams,whole,chain):
            raw=np.ascontiguousarray(trace,dtype="<f8").tobytes()
            state["new_complete_negative_trial_cells"]=n
            state["complete_suffix"]={"count":n,"lower_radius":str(lo),"lower_trace_sha256":sha(raw),
                "lower_trace_f64_le_base64":base64.b64encode(raw).decode("ascii"),"whole_trial_bytes":n*4*len(raw),
                "whole_trial_sha256":whole,"ordered_hash_chain":chain,
                "grams":{name:[[[float(v.lo).hex(),float(v.hi).hex()] for v in row] for row in tab] for name,tab in grams.items()}}
            save()
            if n%64==0 or n==1 or n==total:
                progress("complete_negative_reverse_suffix",{"count":n,"total":total,"lower":str(lo),"chain":chain})
            budget()
        waist,grams,record=maths.run(c,tc,positive,np_math,helper,base,direction,offsets,rows,plan,read,
                                     private/"signed-waist",checkpoint)
        state["new_records"][TARGETS[0]]={"trace":record,"source_order":PARAMETERS["columns"],
              "waist_representation":"complete_suffix.lower_trace_f64_le_base64","signed_Gram_representation":"complete_suffix.grams"}
        state["completed_targets"].append(TARGETS[0])
        save()
        U,c0=c.exact(Fraction("8.22")),c.exact(Fraction("6.531704"))
        fees={"raw_waist":"1","x":".251","x_high":".025","Theta":".456","T_inverse_Theta":".457","each_density_mean":".681"}
        radii=[]
        for j in range(2):
            es,er=[c.arb(max(0.,float(grams[key][j][j].hi))).sqrt() for key in ("strict","root")]
            rad=U*c.exact(helper.NEGATIVE_CUT).sqrt()*es+U*c0*c.exact(Fraction(1,200)).sqrt()*er
            radii.append({k:float(c.arb_box(rad*c.exact(Fraction(v))).hi).hex() for k,v in fees.items()})
        state["new_records"][TARGETS[1]]={"joint_formula":"8.22*(sqrt(c)*sqrt(t^t G_strict t)+6.531704*sqrt(1/200)*sqrt(t^t G_root t))",
             "waist_indexing":"odd sine rows 0..95, independent even mean row 96, even cosine rows 97..192, normalized real basis",
             "radii":radii,"root_zero_and_all_interfaces_exact":True}
        state["completed_targets"].append(TARGETS[1])
        budget()
        state.update(complete=True,proved=True,stage="complete",actual_returncode=0)
    except BaseException as ex:
        state.update(failure={"type":type(ex).__name__,"message":str(ex),"traceback":traceback.format_exc()},actual_returncode=1)
    save()
    return state["actual_returncode"]

if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    for key in ("repo","manifest","manifest-sha","rows-index","out","private","checkout"):
        parser.add_argument("--"+key,required=True)
    parser.add_argument("--preflight-only",action="store_true")
    sys.exit(execute(parser.parse_args()))
