"""First complete fixed-affine base Newton physical trajectory and its selected response bounds."""
import argparse
import ast
import base64
from fractions import Fraction
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
REPO="Rogerhu12/math-research-public"
KIND="R149_fixed_affine_base_Newton_trajectory_and_true_selected_response_v1"
MANIFEST_KIND="R149_fixed_affine_base_Newton_trajectory_inputs_v1"
RUNTIME={"python":"3.12.14","packages":{"numpy":"2.3.5","python-flint":"0.9.0"}}
PARAMETERS={"arithmetic_bits":320,"original_negative_cells":3073,"base_unscaled_real_rows":65,
    "physical_trial_rows":193,"radial_trial_degree":8,"geometry_taylor_degree":22,
    "geometry_disk_ratio":24,"residual_disk_ratio":16,"flat_quadrature_degree":48,
    "complete_residual_quarter_degree":160,"selected_operator_difference_quarter_degree":288,
    "whole_body_radius_test":"2e-14","maximum_actual_bytes":50000,"maximum_scientific_seconds":19000,
    "maximum_private_bytes":12884901888,"maximum_aggregate_rss":3221225472}
TARGETS=["complete_fixed_affine_base_trial_and_three_full_residual_integrals",
         "true_selected_negative_Newton_ordinary_body_and_signed_physical_waist"]
FIELDS=("kind","parameters","runtime","identity","original_input_identity","original_affine_geometry",
    "source_restoration","plan","complete","proved","failure","stage","actual_returncode","seconds",
    "complete_cells","complete_suffix","new_records","completed_targets","actual_resource_peaks",
    "old_completed_scientific_targets_called","new_arrays_published","new_artifacts","new_Releases")
FM="e99e081cd404c36e9f754c0839e9f8f7d95502fffa2db02bff093fe90a0599a8"
FIXED={"ASQ23_manifest":"1f6734a0decbaa7eabe8236723a0b3929908176811854cabba5b189b0e73f04c",
    "ASQ23_science":"23d172da685dda01620f4ec4f041f9d8c7a4aa10c4442f4ddeabdf7c505fd736",
    "FM_manifest":FM,"FM_science":"b3e7b85933f6d1e5bae7f39b3a84a98a0d9a8db11255d22d9cefa0edc1a6bd4b",
    "ASQ26_proof":"92446d3b4781f4d88e3fad8f74eeabc98add473ef151344e0e0d97c497c32295",
    "ASQ26_receipt":"91868905e6baafb58fde566c22f9d5780e74cae7bf0c3662bf100805ef65daa9",
    "D_execution":"6956c214240cd85e6263331b33e0c7efcf6abc3e71190d46ff3eabddecd35071"}
GEOMETRY=("original_affine_origin_inputs","original_affine_direction")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(v):
    return (json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()


def load(path,name):
    s=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(s)
    sys.modules[name]=m
    s.loader.exec_module(m)
    return m


def whole(root,s):
    p=Path(s["path"])
    require(not p.is_absolute() and ".." not in p.parts and str(p).startswith(TOPIC+"/"),"same approved topic")
    b=(root/p).read_bytes()
    require(len(b)==s["bytes"] and sha(b)==s["sha256"] and
            hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()==s["git_blob_sha"],"whole "+str(p))
    return b


def admit(root,raw,digest,rows_index):
    root=Path(root)
    require(len(raw)<100000 and sha(raw)==digest,"whole immutable ASQ27 manifest")
    m=json.loads(raw)
    require((m["kind"],m["scientific_kind"],m["repository"],m["runtime"],m["target_order"],m["parameters"],
             m["allowed_scientific_fields"])==(MANIFEST_KIND,KIND,REPO,RUNTIME,TARGETS,PARAMETERS,sorted(FIELDS)),
            "complete first trajectory definition")
    roles={s["role"]:s for s in m["files"]}
    require(len(roles)==len(m["files"]) and roles["science"]["sha256"]==sha(Path(__file__).read_bytes()) and
            all(roles[k]["sha256"]==v for k,v in FIXED.items()),"all fixed whole parents and original definition")
    raws={k:whole(root,s) for k,s in roles.items()}
    for k in roles:
        if roles[k]["path"].endswith(".py"):
            ast.parse(raws[k],filename=roles[k]["path"])
    no=load(root/roles["ASQ23_science"]["path"],"_ASQ27_original_metadata_only")
    nm,nr,admitted=no.admit(root,raws["ASQ23_manifest"],FIXED["ASQ23_manifest"],rows_index)
    require(m["whole_original_descriptors"]==nm["whole_original_descriptors"] and
            all(roles["ASQ23_"+k]["sha256"]==s["sha256"] and roles["ASQ23_"+k]["path"]==s["path"] for k,s in nr.items()),
            "the full 184/32 original mathematical admission and WSS source identity")
    fixed=json.loads(raws["FM_manifest"])
    by={s["role"]:s for s in fixed["files"]}
    for k in ("science","object","definition_arb","definition_bulk"):
        require(all(by[k][a]==roles["FM_"+k][a] for a in ("path","bytes","sha256","git_blob_sha")),
                "unchanged original affine and analytic primitive sources")
    hist=[s for s in fixed["historical_inputs"] if s["role"] in GEOMETRY]
    require(len(hist)==2 and hist==m["original_affine_historical_inputs"] and
            [s["role"] for s in hist]==list(GEOMETRY),"exact two original affine arrays")
    for s in hist:
        whole(root,s)
    definition=json.loads(raws["FM_object"])
    q=definition["delta_fraction"]
    require(Fraction(int(q["numerator"]),int(q["denominator"]))==Fraction(-7789843107295549,4611686018427387904)
            and all(definition[k]["sha256"]==s["sha256"] and TOPIC+"/"+definition[k]["path"]==s["path"]
                    for k,s in zip(("origin_inputs","direction"),hist)),"true fixed original affine member")
    transfer=json.loads(raws["ASQ26_receipt"])
    require(transfer["complete"] and len(transfer["new_exact_rational_checks"])==16 and
            all(v is True for v in transfer["new_exact_rational_checks"].values()),"actual whole ASQ26 transfer")
    execution=json.loads(raws["D_execution"])
    receipt=execution["actual_scientific_receipt"]
    fees=receipt["selected_parameter_operator_fees"]
    require(str(execution["run_id"])==str(receipt["run_id"])=="43713242980" and
            str(execution["run_attempt"])==str(receipt["run_attempt"])=="1" and execution["complete"] and receipt["proved"] and
            receipt["complete"] and execution["actual_returncode"]==receipt["actual_returncode"]==0 and
            len(receipt["gates"])==12 and all(g["passed"] is True for g in receipt["gates"]) and
            fees["exact_core_interval"]==["0","9/10"] and fees["source_head_physical_frequency"]==384,
            "complete original selected operator difference on the actual head")
    require(not any(x in sys.modules for x in ("numpy","flint","scipy")),"metadata admission before numerical import")
    return m,roles,admitted


def validate(d,m):
    require(set(d)==set(FIELDS) and d["kind"]==KIND and d["parameters"]==PARAMETERS and d["runtime"]==RUNTIME and
            d["original_affine_geometry"]==m["original_affine_historical_inputs"] and
            all(d[k]==0 for k in ("old_completed_scientific_targets_called","new_arrays_published","new_artifacts","new_Releases")),
            "whole actual scientific contract")
    n=d["complete_cells"]
    c=d["complete_suffix"]
    require(type(n) is int and n>=0 and (n==0)==(c is None),"complete contiguous negative suffix")
    if c is not None:
        b=base64.b64decode(c["physical_trace_f64_le_base64"],validate=True)
        require(len(b)==193*8 and sha(b)==c["physical_trace_sha256"] and c["subcells"]==n and
                0<=c["completed_original_cells"]<=3073 and c["trial_bytes"]==n*9*193*8 and
                len(c["trial_sha256"])==len(c["trial_chain_sha256"])==64 and
                set(c["quadratic_integrals"])=={"strict","root","bracket"} and
                all(len(q)==2 and all(r["kind"]=="complete_decimal_ball_v1" for r in q) for q in c["quadratic_integrals"].values()),
                "entire signed lower endpoint and every accepted integrated norm")
    k=len(d["completed_targets"])
    require(d["completed_targets"]==TARGETS[:k] and set(d["new_records"])==set(TARGETS[:k]),"complete natural target prefix")
    if k:
        require(c["lower_radius"]=="0" and c["completed_original_cells"]==3073 and
                d["new_records"][TARGETS[0]]["whole_trace"]["sha256"]==c["trial_sha256"],"true whole radial cell accounting")
    if d["complete"]:
        require(k==2 and d["proved"] and d["actual_returncode"]==0 and d["failure"] is None and
                type(d["new_records"][TARGETS[1]]["body_below_2e_minus14"]) is bool,"both actual mathematical targets")


def execute(args):
    from importlib.metadata import version
    root,manifest,private,out=map(Path,(args.repo,args.manifest,args.private,args.out))
    m,r,admitted=admit(root,manifest.read_bytes(),args.manifest_sha,args.rows_index)
    if args.preflight_only:
        print(encode(dict(original_identity=admitted[-1],original_affine=m["original_affine_historical_inputs"],new_science=0)).decode(),end="")
        return 0
    require(os.environ.get("GITHUB_ACTIONS")=="true" and os.environ.get("GITHUB_REPOSITORY")==REPO and
            os.environ.get("GITHUB_RUN_ATTEMPT")=="1" and platform.python_version()==RUNTIME["python"] and
            all(version(k)==v for k,v in RUNTIME["packages"].items()) and all(os.environ.get(k)=="1" for k in
            ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS")),"one actual public first invocation")
    import numpy as np
    import flint
    import fourfold_codazzi_fixed_negative_Newton_radial as radial
    import fourfold_codazzi_fixed_negative_Newton_trial as trial
    import fourfold_codazzi_fixed_eta0_correlated_mean_retraction as fm
    require(all(sha(Path(x.__file__).read_bytes())==r[y]["sha256"] for x,y in
                ((radial,"radial"),(trial,"trial"),(fm,"FM_science"))),"three actually imported scientific sources")
    flint.ctx.prec=320
    def mod(role):
        return load(root/r[role]["path"],"_ASQ27_"+role)
    core,field,resources,disk=map(mod,("ASQ23_wss_raw_input_helper","ASQ23_wss_carrier",
                                      "ASQ23_wss_resource_carriers","ASQ23_wss_resource_directory"))
    original,old_roles,raws,helper,prior,rows,ident=admitted
    wss=json.loads((root/r["ASQ23_wss_actual"]["path"]).read_bytes())
    dfee=json.loads((root/r["D_execution"]["path"]).read_bytes())["actual_scientific_receipt"]["selected_parameter_operator_fees"]
    require(flint.arb(dfee["e"]["ball"])<fm.rat(Fraction("1.049107e-5")) and
            (fm.rat(1+1152**2).log()/6).exp()<fm.rat(Fraction("10.484")),"actual whole selected-operator and strong finite degree")
    began=time.monotonic()
    state=dict(kind=KIND,parameters=PARAMETERS,runtime=RUNTIME,
        identity=dict(manifest_sha256=args.manifest_sha,source_sha256=r["science"]["sha256"],run_id=os.environ["GITHUB_RUN_ID"],
        run_attempt="1",actual_scientific_checkout=args.checkout,workflow_event_commit=os.environ["GITHUB_SHA"]),
        original_input_identity=ident,original_affine_geometry=m["original_affine_historical_inputs"],source_restoration=None,
        plan=None,complete=False,proved=False,failure=None,stage="raw_input_restoration",actual_returncode=None,seconds=0.,
        complete_cells=0,complete_suffix=None,new_records={},completed_targets=[],
        actual_resource_peaks=dict(aggregate_rss=0,private_bytes=0),old_completed_scientific_targets_called=0,
        new_arrays_published=0,new_artifacts=0,new_Releases=0)
    def save():
        state["seconds"]=time.monotonic()-began
        validate(state,m)
        body=encode(state)
        require(len(body)<=PARAMETERS["maximum_actual_bytes"],"whole contiguous physical suffix")
        core.atomic(out,body)
    def progress(s,detail):
        print(json.dumps(dict(stage=s,**detail),sort_keys=True),flush=True)
    def stop(signum,frame):
        raise TimeoutError("keep every completed new strict or root subcell")
    signal.signal(signal.SIGTERM,stop)
    last=0.
    def budget():
        nonlocal last
        now=time.monotonic()
        p=state["actual_resource_peaks"]
        p["aggregate_rss"]=max(p["aggregate_rss"],resources.aggregate_rss_bytes([]))
        if now-last>20:
            p["private_bytes"]=max(p["private_bytes"],disk.private_bytes((root,private)))
            last=now
        require(now-began<PARAMETERS["maximum_scientific_seconds"] and p["aggregate_rss"]<=PARAMETERS["maximum_aggregate_rss"] and
                p["private_bytes"]<=PARAMETERS["maximum_private_bytes"],"complete current resource budget")
    require(not out.exists(),"one initial fixed-affine owner result")
    save()
    try:
        base,direction,offsets,rows,receipt=core.raw_inputs(np,flint,admitted,root,private,progress)
        require(receipt==wss["source_restoration"] and helper.ALPHA==fm.ALPHA,"whole original physical repair arrays and exact alpha")
        state["source_restoration"]=receipt
        plan=field.partition(helper,rows,base,direction)
        desc=encode([[j,k,str(a),str(b)] for j,k,a,b in plan])
        require(len(plan)==7728 and len(desc)==wss["plan"]["bytes"] and sha(desc)==wss["plan"]["canonical_sha256"] and
                sum(1 for p in plan if p[2]<helper.ROOT[1])==3073,"every original finite negative cell")
        state["plan"]=dict(original_whole_sha256=sha(desc),original_negative_cells=3073,
                           root_bracket=list(map(str,helper.ROOT)),strict_root_split=str(helper.NEGATIVE_CUT))
        target=fm.FixedObject(root/r["FM_object"]["path"],root/TOPIC)
        state["stage"]="signed_fixed_affine_backward_trial"
        save()
        def checkpoint(count,original,j,k,lo,right,sums,size,whole_sha,chain):
            raw=np.ascontiguousarray(right,dtype="<f8").tobytes()
            state["complete_cells"]=count
            state["complete_suffix"]=dict(subcells=count,completed_original_cells=original,lower_radius=str(lo),
                original_scalar_row=j,original_cubic_piece=k,physical_trace_f64_le_base64=base64.b64encode(raw).decode(),
                physical_trace_sha256=sha(raw),trial_bytes=size,trial_sha256=whole_sha,trial_chain_sha256=chain,
                quadratic_integrals={key:[fm.record(v,"upper") for v in vals] for key,vals in sums.items()})
            save()
            if count==1 or count%64==0 or lo==0:
                progress("accepted_fixed_affine_negative_suffix",dict(count=count,original=original,left=str(lo),whole_sha256=whole_sha))
            budget()
        waist,sums,trace=trial.run(target,base,offsets["base"],plan,helper,private/"fixed-same-r",checkpoint)
        require(trace["original_cells"]==3073,"entire original window received")
        state["new_records"][TARGETS[0]]=dict(whole_trace=trace,integrals="complete_suffix.quadratic_integrals",
            signed_dyadic_waist="complete_suffix.physical_trace_f64_le_base64",geometric_carrier_calls=target.carrier_calls,
            complex_geometric_calls=target.complex_calls,full_primitive_tail_max=fm.record(target.angular_tail_max,"upper"))
        state["completed_targets"].append(TARGETS[0]);save()
        dd=fm.rat(Fraction("1.049107e-5"))
        T={k:z[1].sqrt() for k,z in sums.items()}
        E={k:z[0].sqrt() for k,z in sums.items()}
        require(T["bracket"].is_zero(),"identically zero on the complete bracket")
        es,er,eb=E["strict"]+dd*T["strict"],E["root"]+fm.rat(Fraction("10.484"))*dd*T["root"],E["bracket"]
        c=fm.rat(helper.NEGATIVE_CUT)
        r,b=fm.rat(Fraction(1,200)),fm.rat(helper.ROOT[1]-helper.ROOT[0])
        u,C,A=(fm.rat(Fraction(x)) for x in ("8.22","6.531704","25.943"))
        rootcost=r.sqrt()*er+b.sqrt()*eb
        bodyerr=c*u/flint.arb(2).sqrt()*es+A*rootcost+fm.rat(Fraction("1.019e-15"))
        waisterr=u*c.sqrt()*es+u*C*rootcost+fm.rat(Fraction("2.12e-15"))
        trialbody=sum((v[1] for v in sums.values()),flint.arb(0)).sqrt()
        body=trialbody+bodyerr
        upper=lambda v:fm.record(v.upper(),"upper")
        state["new_records"][TARGETS[1]]=dict(trial_ordinary_body=upper(trialbody),
            selected_body_error=upper(bodyerr),selected_body_total=upper(body),selected_waist_error=upper(waisterr),
            selected_waist_center="complete_suffix.physical_trace_f64_le_base64",
            source_error_after_operator_transfer={k:upper(v) for k,v in (("strict",es),("root",er),("bracket",eb))},
            each_signed_receiver_radius={k:upper(waisterr*fm.rat(Fraction(v))) for k,v in
                 (("raw_waist","1"),("x",".251"),("x_high",".025"),("Theta",".456"),
                  ("T_inverse_Theta",".457"),("each_independent_mean",".681"))},
            body_below_2e_minus14=bool(body<fm.rat(Fraction("2e-14"))))
        state["completed_targets"].append(TARGETS[1])
        budget()
        state.update(complete=True,proved=True,stage="complete",actual_returncode=0)
    except BaseException as ex:
        state.update(failure=dict(type=type(ex).__name__,message=str(ex),traceback=traceback.format_exc()),actual_returncode=1)
    save()
    return state["actual_returncode"]


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    for k in ("repo","manifest","manifest-sha","rows-index","checkout","private","out"):
        p.add_argument("--"+k,required=True)
    p.add_argument("--preflight-only",action="store_true")
    sys.exit(execute(p.parse_args()))
