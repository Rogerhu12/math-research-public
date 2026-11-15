#!/usr/bin/env python3
"""R360 exact decomposition of actually observed current-H noJ trials.

This child performs new exact arithmetic only in public Actions.  It never
calls RHS, root, RK, QR or native solve and never returns an acceptance flag.
Every input state/residual is an actual copied binary64 array.  The old exact
e=rJ+A*delta ledger is reused; only A*q is newly formed.  Dynamic integer
units include the explicit dyadic alpha, including subnormal products.
"""
from __future__ import annotations
import argparse
from collections import deque
from concurrent.futures import ProcessPoolExecutor
from decimal import Decimal, localcontext
from fractions import Fraction
import gzip
import hashlib
import importlib
import json
import multiprocessing
import os
from pathlib import Path, PurePosixPath
import re
import struct
import time
import traceback

HERE=Path(__file__).resolve().parent
SYSTEM="exact_20261115_current_H_secant576_system.py"
SYSTEM_SHA="9933e75ab4a07e920f8784e36eae93345c3735cf11b5a90f86d0eaef3073f25e"
QR="exact_20261115_current_H_secant576_chain_qr.py"
QR_SHA="0cc45afa1cec2f73d53e370cf8be7cd75a7ba9a1b6025da4724e2b2d0bde9036"
KERNEL="exact_20261114_native_allrows_dyadic_residual.py"
KERNEL_SHA="0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f"
PROOF_SHA="f11d3084cc2d2d651d1c61dbe1ce9dd35a195e2cde4b4535e12f522d2d998ad7"
SCHEMA="current-H-complete-original576-secant-decomposition-v1"
M,K,D=112,224,576
ROWS=M+D*K+M
_E=None


class ResourcePartial(Exception):
    pass


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS")!="true" or
            os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public"):
        raise RuntimeError("Exact current-H work belongs only to this public repository Actions")


def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as f:
        for raw in iter(lambda:f.read(1<<20),b""):h.update(raw)
    return h.hexdigest()


def encoded(value):
    return (json.dumps(value,ensure_ascii=True,separators=(",",":"),allow_nan=False)+"\n").encode()


def write(path,value):
    raw=encoded(value);path=Path(path)
    with path.open("xb") as f:f.write(raw)
    return dict(file=path.name,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())


def same(a,b,label):
    if a!=b:raise ValueError("Actual diagnostic binding differs: "+label)


def safe(root,name):
    p=PurePosixPath(name)
    if p.is_absolute() or ".." in p.parts or not p.parts:
        raise ValueError("A contained actual relative file is required")
    result=root.joinpath(*p.parts)
    if result.is_symlink() or not result.is_file():raise ValueError("An original regular file is required")
    if not result.resolve().is_relative_to(root.resolve()):raise ValueError("Escaping input")
    return result


def read_desc(root,d):
    p=safe(root,d["file"])
    same(p.stat().st_size,d["bytes"],"input bytes "+d["file"])
    same(sha(p),d["sha256"],"input SHA "+d["file"])
    raw=p.read_bytes()
    full=gzip.decompress(raw) if raw[:2]==b"\x1f\x8b" else raw
    if "raw_sha256" in d:same(hashlib.sha256(full).hexdigest(),d["raw_sha256"],"decoded SHA")
    if "raw_bytes" in d:same(len(full),d["raw_bytes"],"decoded size")
    return json.loads(full)


def kernel():
    global _E
    if _E is None:
        require_actions()
        same(sha(HERE/KERNEL),KERNEL_SHA,"frozen bit decoder")
        _E=importlib.import_module(Path(KERNEL).stem)
        same(Path(_E.__file__).resolve(),HERE/KERNEL,"loaded decoder path")
    return _E


def pairs(raw):
    E=kernel()
    return [E.decode_bits(w[0]) for w in struct.iter_unpack("<Q",raw)]


def unit(pair,exponent):
    m,e=pair
    if not m:return 0
    if e<exponent:raise ValueError("Dynamic integer unit excludes an actual dyadic")
    return m << (e-exponent)


def compact(value,exponent):
    if not value:return ["0x0",0]
    shift=(abs(value)&-abs(value)).bit_length()-1
    return [hex(value>>shift),exponent+shift]


def integer_pair(value,exponent):
    if not value:return (0,0)
    shift=(abs(value)&-abs(value)).bit_length()-1
    return value>>shift,exponent+shift


def lift_saved(pair,exponent):
    if not isinstance(pair,list) or len(pair)!=2 or type(pair[1]) is not int:
        raise ValueError("A complete original signed exact dyadic pair is required")
    return unit((int(pair[0],16),pair[1]),exponent)


def divide_power(value,power):
    if power<0:raise ValueError("Nonnegative alpha exponent required")
    if power and value% (1<<power):raise ValueError("Exact alpha division lost a bit")
    return value>>power


def fraction(numerator,denominator):
    if denominator<=0:raise ValueError("A strictly positive original sigma is required")
    f=Fraction(numerator,denominator)
    with localcontext() as c:
        c.prec=68
        text=str(Decimal(f.numerator)/Decimal(f.denominator))
    return dict(numerator_hex=hex(f.numerator),denominator_hex=hex(f.denominator),decimal68=text)


def check_time(deadline):
    if time.monotonic()>=deadline:raise ResourcePartial("Declared diagnostic wall budget reached")


def raw_array(directory,entry,shape):
    same(entry["shape"],shape,"full original observation shape")
    same(entry["dtype"],"<f8","original f64 dtype")
    same(entry["order"],"C","original array order")
    same(entry["completed"],True,"all original chunks closed")
    digest=hashlib.sha256();parts=[];nextrow=0
    width=1
    for q in shape[1:]:width*=q
    for index,c in enumerate(entry["chunks"]):
        same(c["chunk_index"],index,"ordered chunk")
        same(c["row_start"],nextrow,"complete chunk row cover")
        p=safe(directory,c["file"]);raw=p.read_bytes()
        same(len(raw),c["bytes"],"chunk bytes")
        same(hashlib.sha256(raw).hexdigest(),c["raw_sha256"],"chunk SHA")
        same(len(raw),(c["row_stop"]-c["row_start"])*width*8,"all raw row words")
        nextrow=c["row_stop"];parts.append(raw);digest.update(raw)
    same(nextrow,shape[0],"all raw observation rows")
    raw=b"".join(parts)
    same(len(raw),entry["total_bytes"],"complete observation array bytes")
    same(digest.hexdigest(),entry["raw_sha256"],"complete observation raw SHA")
    return raw


def observation(root,d,identity):
    p=safe(root,d["file"]);directory=p.parent
    value=read_desc(root,d)
    same(value["schema"],"current-H-actual-noJ-observation-v1","noJ observation schema")
    for key in ("native_call","nonlinear_iteration","snapshot_sequence","current_state_sha256"):
        same(value[key],identity[key],"current observation "+key)
    raw={}
    if value.get("state_input") is not None:
        state=value["state_input"]
        same(state["schema"],"current-H-actual-state-input-v1","actual input schema")
        raw["states"]=raw_array(directory,state["states"],[577,224])
        same(hashlib.sha256(raw["states"]).hexdigest(),state["states"]["raw_sha256"],"actual states")
    if value["returned_complete_residual"]:
        entries={a["name"]:a for a in value["arrays"]}
        for name,shape in (("stage-residuals",[576,224]),("cut-residual",[1,112]),
                           ("end-residual",[1,112]),("stage-out",[576,224])):
            raw[name]=raw_array(directory,entries[name],shape)
        raw["rows"]=raw["cut-residual"]+raw["stage-residuals"]+raw["end-residual"]
        same(len(raw["rows"]),ROWS*8,"all original cut/stage/far row words")
    return dict(value=value,raw=raw,receipt=d)


def location(kind,node,row):
    index=row if kind=="cut" else M+D*K+row if kind=="far" else M+node*K+row
    return dict(kind=kind,node=node,row_in_block=row,global_equation_row=index,
                coordinate=("Q" if row<M else "Pi")+str(row%M+1) if kind=="stage" else
                    ("Q" if kind=="cut" else "Pi")+str(row+1))


def action_job(task):
    """Complete one actual stage; share each J word across all observed q."""
    require_actions()
    check_time(task["deadline"])
    exponent=task["unit_exponent"];sunit=task["state_unit"]
    kind,node=task["kind"],task["node"]
    count=K if kind=="stage" else M
    old=pairs(task["base_current"]);nxt=pairs(task["base_next"])
    delta=pairs(task["delta_current"]);dnxt=pairs(task["delta_next"])
    rj=pairs(task["rj"]);r0=pairs(task["r0"]) if task["r0"] is not None else None
    graph=pairs(task["graph"]);target=pairs(task["target"])
    sigma=unit(pairs(task["sigma"])[0],exponent)
    if sigma<=0:raise ValueError("Original sigma must be finite and strictly positive")
    data=[]
    for obs in task["observations"]:
        tc=pairs(obs["current"]);tn=pairs(obs["next"])
        k=obs["alpha_exponent"]
        qc=[integer_pair(unit(t,sunit)-unit(x,sunit)-divide_power(unit(d,sunit),k),sunit)
            for t,x,d in zip(tc,old,delta)]
        qn=[integer_pair(unit(t,sunit)-unit(x,sunit)-divide_power(unit(d,sunit),k),sunit)
            for t,x,d in zip(tn,nxt,dnxt)]
        data.append(dict(label=obs["label"],k=k,trial=pairs(obs["residual"]),
                         qc=qc,qn=qn,tc=tc,rows=[],maxima={},products=0,nonzero_products=0))
    E=kernel()
    jwords=struct.iter_unpack("<Q",task["J"]) if kind=="stage" else None
    for row in range(count):
        check_time(task["deadline"])
        if kind=="stage":
            aq=[-unit(d["qc"][row],exponent) for d in data]
            for col in range(K):
                jm,je=E.decode_bits(next(jwords)[0])
                for index,d in enumerate(data):
                    d["products"]+=1
                    qm,qe=d["qn"][col]
                    if jm and qm:
                        shift=je+qe-exponent
                        if shift<0:raise ValueError("Dynamic product exponent is outside the exact unit")
                        aq[index]+=(jm*qm)<<shift
                        d["nonzero_products"]+=1
        elif kind=="cut":
            aq=[unit(d["qc"][row],exponent) for d in data]
        else:
            gm,ge=graph[row]
            aq=[]
            for d in data:
                qm,qe=d["qc"][row]
                product=(gm*qm)<<(ge+qe-exponent) if gm and qm else 0
                aq.append(unit(d["qc"][M+row],exponent)-product)
                d["products"]+=1;d["nonzero_products"]+=bool(gm and qm)
        j=unit(rj[row],exponent)
        zero=unit(r0[row],exponent) if r0 is not None else None
        e=lift_saved(task["saved_e"][row],exponent)
        for d,aqi in zip(data,aq):
            actual=unit(d["trial"][row],exponent)
            linear=j+divide_power(e-j,d["k"])
            bias=None if zero is None else zero-j
            secant=None if zero is None else actual-zero-(linear-j)-aqi
            difference=actual-linear
            realized_affine=linear+aqi
            if bias is not None:same(difference,bias+aqi+secant,"R360 exact component identity")
            vec=[j,zero,actual,linear,bias,aqi,secant,difference,realized_affine]
            metrics={"withJ_base":j,"noJ_base":zero,"trial":actual,"ideal_affine":linear,
                     "baseline_path_difference":bias,"state_formation":aqi,
                     "finite_secant":secant,"total_difference":difference,
                     "realized_affine":realized_affine}
            if kind!="stage" and zero is not None:
                if kind=="cut":
                    btrue=unit(old[row],exponent)-unit(target[row],exponent)
                    ttrue=unit(d["tc"][row],exponent)-unit(target[row],exponent)
                else:
                    gm,ge=graph[row]
                    def far_value(state):
                        qm,qe=state[row]
                        product=(gm*qm)<<(ge+qe-exponent) if gm and qm else 0
                        return unit(state[M+row],exponent)-product
                    btrue=far_value(old);ttrue=far_value(d["tc"])
                base_form=zero-btrue;trial_form=actual-ttrue
                same(secant,trial_form-base_form,"complete affine boundary formation identity")
                metrics.update(boundary_base_formation=base_form,boundary_trial_formation=trial_form)
            record=[compact(v,exponent) if v is not None else None for v in vec]
            d["rows"].append(record)
            for name,value in metrics.items():
                if value is None:continue
                prior=d["maxima"].get(name)
                if prior is None or abs(value)>abs(prior["value"]):
                    d["maxima"][name]=dict(value=value,sigma=sigma,location=location(kind,node,row),
                        vector=record)
    if jwords is not None and next(jwords,None) is not None:raise ValueError("Extra J words")
    return dict(kind=kind,node=node,rows=count,J_sha256=hashlib.sha256(task["J"]).hexdigest()
                if kind=="stage" else None,unit_exponent=exponent,
                observations=[dict(label=d["label"],rows=d["rows"],maxima=d["maxima"],
                    original_product_positions=d["products"],nonzero_products=d["nonzero_products"])
                    for d in data])


def public_max(record,exponent):
    if record is None:return None
    return dict(**record["location"],
        signed_unscaled=compact(record["value"],exponent),
        exact_original_sigma_absolute=fraction(abs(record["value"]),record["sigma"]),
        row_vector_order=["withJ","same_state_noJ","actual_trial","ideal_affine",
                          "b","Aq","s","d","realized_affine"],
        complete_row_vector=record["vector"])


def preferable(a,b):
    return b is None or abs(a["value"])*b["sigma"]>abs(b["value"])*a["sigma"]


def record_original_norm(obs,maximum,exponent):
    original=obs["value"].get("original_norm")
    if original is None or maximum is None:return dict(original=original,exact_sigma_max=None)
    h=original["float64le_hex"]
    raw=bytes.fromhex(h)
    if len(raw)!=8:raise ValueError("Original norm word must have eight bytes")
    if original.get("classification") not in ("finite","negative-zero"):
        return dict(original=original,exact_sigma_max=public_max(maximum,exponent),
            absolute_printed_norm_minus_exact_sigma_max=None,original_printed_norm_nonfinite=True,
            finite_exact_rows_do_not_override_original_printed_acceptance=True)
    pair=pairs(raw)[0]
    norm=unit(pair,exponent)
    return dict(original=original,exact_sigma_max=public_max(maximum,exponent),
        absolute_printed_norm_minus_exact_sigma_max=fraction(
            abs(norm*maximum["sigma"]-abs(maximum["value"])*(1<<(-exponent))),
            (1<<(-exponent))*maximum["sigma"]),
        original_printed_norm_not_replaced_by_this_exact_readback=True)


def main():
    require_actions()
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--iteration-directory",type=Path,required=True)
    parser.add_argument("--model-sha256",required=True)
    parser.add_argument("--loop-sha256",required=True)
    parser.add_argument("--budget-seconds",type=float,required=True)
    parser.add_argument("--workers",type=int,default=2)
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args()
    if not 1<=args.workers<=4 or not args.budget_seconds>0:
        raise ValueError("Explicit positive diagnostic resources required")
    root=args.iteration_directory.resolve();out=args.out.resolve()
    temporary=Path(os.environ["RUNNER_TEMP"]).resolve()
    if not root.is_relative_to(temporary) or not out.is_relative_to(root) or out==root:
        raise ValueError("All actual diagnostic inputs/output belong to this owned temporary iteration")
    out.mkdir(exist_ok=False);(out/"large-arrays").mkdir()
    started=time.monotonic();deadline=started+args.budget_seconds
    result=dict(schema=SCHEMA,source_sha256=sha(__file__),proof_sha256=PROOF_SHA,
        kernel_sha256=KERNEL_SHA,system_sha256=SYSTEM_SHA,complete=False,
        original_native_acceptance_not_modified=True,new_RHS_J_ODE_QR_calls_by_this_child=0,
        diagnostic_exact_arithmetic_is_new_science=True,full_original_rows=ROWS,
        error=None,unpaid_scope=[],trial_results=[],input_binding=None)
    pool=None;handle=None;ledger=None;closed_blocks=0;processed_rows=0
    trial_stats={};all_observations=[];base=None;exponent=None
    try:
        check_time(deadline)
        model_path=root/"diagnostic-model.json";loop_path=root/"diagnostic-loop.json"
        same(sha(model_path),args.model_sha256,"actual model receipt")
        same(sha(loop_path),args.loop_sha256,"actual completed loop receipt")
        model=json.loads(model_path.read_bytes());loop=json.loads(loop_path.read_bytes())
        same(model["schema"],"current-H-secanted-model-input-v1","actual model")
        same(model["exact_diagram_proof_sha256"],PROOF_SHA,"actual R360 proof identity")
        same(loop["schema"],"current-H-actual-ten-trial-loop-observation-v1","actual loop")
        identity={k:model[k] for k in ("native_call","nonlinear_iteration","snapshot_sequence","current_state_sha256")}
        for key,value in identity.items():same(loop[key],value,"same model loop "+key)
        same(sha(HERE/SYSTEM),SYSTEM_SHA,"actual source system")
        S=importlib.import_module(Path(SYSTEM).stem)
        same(Path(S.__file__).resolve(),HERE/SYSTEM,"actual source system loaded")
        system=S.CurrentHSecant576System(root/"snapshot",model["snapshot_result"]["sha256"])
        for key,value in identity.items():
            actual={"native_call":system.native_call,"nonlinear_iteration":system.iteration,
                    "snapshot_sequence":system.sequence,"current_state_sha256":system.current_state_sha256}[key]
            same(actual,value,"actual bound model "+key)
        same(sha(HERE/QR),QR_SHA,"unchanged current QR producer")
        qr=read_desc(root,model["qr_result"])
        same(qr["schema"],"complete-native-current-H-secant-r273-current576-damped-square-root-direction-v1","actual QR schema")
        same(qr["source_sha256"],QR_SHA,"actual QR source")
        same(qr["system_source_sha256"],SYSTEM_SHA,"actual QR system")
        same(qr["linear_direction_computed"],True,"actual complete direction")
        same(qr["snapshot_result"]["sha256"],model["snapshot_result"]["sha256"],"QR this snapshot")
        same(qr["new_matrix_identity_sha256"],system.binding["new_matrix_identity_sha256"],"actual matrix")
        delta_entry=qr["native_delta"]
        delta_file=safe(root/"qr",delta_entry["file"])
        same(sha(delta_file),delta_entry["sha256"],"all original delta bytes")
        delta=delta_file.read_bytes();same(len(delta),577*224*8,"complete returned delta")
        old_manifest=read_desc(root/"qr",qr["array_manifest"])
        signed=[e for e in old_manifest["arrays"] if e["name"]=="current576-all-exact-rows"]
        same(len(signed),1,"unique complete old e ledger")
        old_signed=signed[0];old_path=safe(root/"qr",old_signed["file"])
        same(old_path.stat().st_size,old_signed["bytes"],"old exact signed ledger bytes")
        same(sha(old_path),old_signed["sha256"],"old exact signed ledger SHA")
        base=observation(root,loop["baseline"],identity)
        same(base["value"]["role"],"additional-same-state-noJ-baseline","explicit added baseline call")
        same(base["raw"].get("states"),system.raw("base-states"),"same complete state words for baseline")
        descriptors=loop["original_trials"]+loop["extra_diagnostic_trials"]
        visited=[]
        for descriptor in descriptors:
            ob=observation(root,descriptor,identity);v=ob["value"]
            k=v["alpha_exponent"]
            if type(k) is not int or not 0<=k<=12:raise ValueError("Explicit original ten or declared three extra exponents")
            same(v["alpha_float64le_hex"],struct.pack("<d",2.0**(-k)).hex(),"actual alpha word")
            if v["role"]=="original-native-trial":
                if k>=10:raise ValueError("Only original ten trials can have original eligibility")
                same(v["eligible_for_original_acceptance"],True,"original eligibility");visited.append(k)
            elif v["role"]=="post-ten-rejection-diagnostic":
                same(loop["original_loop_accepted"],False,"post rejection scope")
                same(loop["all_original_ten_visited"],True,"all ten really visited")
                same(v["eligible_for_original_acceptance"],False,"extra is not original acceptance")
                if k not in (10,11,12):raise ValueError("Only explicit extra exponents")
            else:raise ValueError("Unknown observation role")
            all_observations.append(ob)
        same(visited,list(range(len(visited))),"actual original ordered prefix, no fabricated visits")
        same(loop["original_trials_visited"],len(visited),"actual original trial count")
        if not visited:raise ValueError("No actual original trial result was captured")
        maxk=max(o["value"]["alpha_exponent"] for o in all_observations)
        exponent=-2148-maxk;sunit=-1074-maxk
        retained=[o for o in all_observations if o["value"]["returned_complete_residual"]]
        for ob in all_observations:
            key=ob["value"]["label"]
            if key in trial_stats:raise ValueError("Unique actual observation labels")
            trial_stats[key]=dict(observation=ob["receipt"],role=ob["value"]["role"],
                alpha_exponent=ob["value"]["alpha_exponent"],
                original_eligible=ob["value"]["eligible_for_original_acceptance"],
                actual_error=ob["value"].get("error"),returned_complete_residual=ob["value"]["returned_complete_residual"],
                processed_original_rows=0,identity_rows=0,maxima={"all":{},"cut":{},"stage":{},"far":{}})
        result.update(native_call=system.native_call,nonlinear_iteration=system.iteration,
            snapshot_sequence=system.sequence,current_state_sha256=system.current_state_sha256,
            new_matrix_identity_sha256=system.binding["new_matrix_identity_sha256"],
            dynamic_exact_unit_binary_exponent=exponent,state_formation_unit_binary_exponent=sunit,
            withJ_base_original_norm=system.current_records["norm"],
            original_loop_accepted=loop["original_loop_accepted"],
            unvisited_extra_scope=loop["unvisited_extra_scope"],
            actual_original_trials=len(loop["original_trials"]),
            actual_extra_diagnostic_trials=len(loop["extra_diagnostic_trials"]),
            baseline_returned_complete_residual=base["value"]["returned_complete_residual"],
            input_binding=dict(model=dict(file="diagnostic-model.json",sha256=args.model_sha256),
                loop=dict(file="diagnostic-loop.json",sha256=args.loop_sha256),
                complete_system_binding=system.binding,
                original_exact_ledger=old_signed,delta=delta_entry,
                baseline=loop["baseline"],observations=descriptors),
            original_QR_acceptance_and_worker_last_not_assigned=True,
            extra_noJ_calls_may_affect_mutable_internal_caches_or_timing=True,
            derivative_or_unique_error_cause_not_claimed=True)
        inputs={name:system.raw(name) for name in ("base-states","stage-residuals","cut-residual",
                                                 "end-residual","original-scales","original-far-graph","cut-target")}
        original_rows=inputs["cut-residual"]+inputs["stage-residuals"]+inputs["end-residual"]
        base_rows=base["raw"].get("rows")
        handle=(out/"large-arrays/complete-row-decomposition.jsonl.gz").open("xb")
        ledger=gzip.GzipFile(fileobj=handle,mode="wb",mtime=0)
        def blocks():
            stages=iter(system.stage_bytes())
            with gzip.open(old_path,"rt",encoding="utf-8") as stream:
                for index,line in enumerate(stream):
                    check_time(deadline)
                    old=json.loads(line)
                    kind="cut" if index==0 else "far" if index==D+1 else "stage"
                    node=0 if index==0 else D if index==D+1 else index-1
                    same((old["kind"],old["node"]),(kind,node),"whole e ledger block order")
                    same(old["direction_label"],"current_damped","old e direction label")
                    same(old["direction_float64le_sha256"],delta_entry["sha256"],"old e delta")
                    for key,value in identity.items():same(old[key],value,"old e current "+key)
                    same(old["new_matrix_identity_sha256"],system.binding["new_matrix_identity_sha256"],"old e matrix")
                    count=K if kind=="stage" else M
                    first=location(kind,node,0)["global_equation_row"]
                    same(old["first_global_equation_row"],first,"old e original row order")
                    same(len(old["all_exact_unscaled_rows"]),count,"all old signed e rows")
                    J=None
                    if kind=="stage":
                        n,J=next(stages);same(n,node,"original complete J stage")
                        same(hashlib.sha256(J).hexdigest(),old["original_J_stage_sha256"],"old e bound actual J")
                    current=node;nextnode=node+1 if kind=="stage" else node
                    obs=[]
                    for ob in retained:
                        raw=ob["raw"];value=ob["value"]
                        obs.append(dict(label=value["label"],alpha_exponent=value["alpha_exponent"],
                            current=raw["states"][current*K*8:(current+1)*K*8],
                            next=raw["states"][nextnode*K*8:(nextnode+1)*K*8],
                            residual=raw["rows"][first*8:(first+count)*8]))
                    yield dict(kind=kind,node=node,J=J,unit_exponent=exponent,state_unit=sunit,
                        base_current=inputs["base-states"][current*K*8:(current+1)*K*8],
                        base_next=inputs["base-states"][nextnode*K*8:(nextnode+1)*K*8],
                        delta_current=delta[current*K*8:(current+1)*K*8],
                        delta_next=delta[nextnode*K*8:(nextnode+1)*K*8],
                        rj=original_rows[first*8:(first+count)*8],
                        r0=None if base_rows is None else base_rows[first*8:(first+count)*8],
                        graph=inputs["original-far-graph"],target=inputs["cut-target"],
                        sigma=inputs["original-scales"][node*8:(node+1)*8],
                        saved_e=old["all_exact_unscaled_rows"],observations=obs,deadline=deadline)
                same(index+1,D+2,"every old e block and no extra")
                if next(stages,None) is not None:raise ValueError("Unexpected remaining J stage")
        def consume(row):
            nonlocal closed_blocks,processed_rows
            expected_kind="cut" if closed_blocks==0 else "far" if closed_blocks==D+1 else "stage"
            expected_node=0 if closed_blocks==0 else D if closed_blocks==D+1 else closed_blocks-1
            same((row["kind"],row["node"]),(expected_kind,expected_node),"closed exact block prefix")
            emitted=dict(kind=row["kind"],node=row["node"],first_global_equation_row=location(row["kind"],row["node"],0)["global_equation_row"],
                         complete_J_stage_sha256=row["J_sha256"],unit_binary_exponent=exponent,
                         row_vector_order=["withJ","same_state_noJ","actual_trial","ideal_affine","b","Aq","s","d","realized_affine"],
                         observations=[])
            for item in row["observations"]:
                stats=trial_stats[item["label"]]
                stats["processed_original_rows"]+=row["rows"]
                if base_rows is not None:stats["identity_rows"]+=row["rows"]
                for name,record in item["maxima"].items():
                    for scope in ("all",row["kind"]):
                        if preferable(record,stats["maxima"][scope].get(name)):
                            stats["maxima"][scope][name]=record
                emitted["observations"].append(dict(label=item["label"],all_rows=item["rows"],
                    original_product_positions=item["original_product_positions"],nonzero_products=item["nonzero_products"]))
            ledger.write(encoded(emitted));closed_blocks+=1;processed_rows+=row["rows"]
            if closed_blocks%32==0 or closed_blocks==D+2:
                print(json.dumps(dict(event="request172_exact_prefix",native_call=system.native_call,
                    nonlinear_iteration=system.iteration,completed_blocks=closed_blocks,completed_original_rows=processed_rows,
                    observed_trials=len(retained),elapsed_seconds=time.monotonic()-started)),flush=True)
        if retained:
            if args.workers==1:
                for task in blocks():consume(action_job(task))
            else:
                pool=ProcessPoolExecutor(max_workers=args.workers,mp_context=multiprocessing.get_context("spawn"))
                queue=deque();source=iter(blocks())
                for _ in range(2*args.workers):
                    task=next(source,None)
                    if task is None:break
                    queue.append(pool.submit(action_job,task))
                while queue:
                    check_time(deadline);consume(queue.popleft().result())
                    task=next(source,None)
                    if task is not None:queue.append(pool.submit(action_job,task))
                pool.shutdown(wait=True);pool=None
            same(processed_rows,ROWS,"all original equation rows")
        result["complete"]=bool(retained and base_rows is not None and processed_rows==ROWS and
                                len(retained)==len(all_observations) and not loop["unvisited_extra_scope"])
    except Exception as error:
        result["error"]=dict(type=type(error).__name__,message=str(error),traceback=traceback.format_exc(),
                             resource_partial=isinstance(error,ResourcePartial))
    finally:
        if pool is not None:pool.shutdown(wait=True,cancel_futures=True)
        if ledger is not None:ledger.close()
        if handle is not None:handle.close()
        result["completed_original_blocks"]=closed_blocks
        result["completed_original_rows_per_returned_trial"]=processed_rows
        for pending in result.get("unvisited_extra_scope",[]):
            result["unpaid_scope"].append(dict(kind="declared-extra-noJ-not-called",**pending))
        if processed_rows<ROWS:result["unpaid_scope"].append(dict(
            kind="whole-original-row-suffix",first_global_equation_row=processed_rows,stop_global_equation_row=ROWS,
            original_block_prefix_completed=closed_blocks,all_original_cut_stage_far_required=True))
        if base is not None and not base["value"]["returned_complete_residual"]:
            result["unpaid_scope"].append(dict(kind="same-state-noJ-unreturned",
                original_error=base["value"].get("error"),b_and_s_not_filled=True))
        by_label={o["value"]["label"]:o for o in all_observations}
        for label,stats in trial_stats.items():
            value=by_label[label]
            if not stats["returned_complete_residual"]:
                result["unpaid_scope"].append(dict(kind="actual-trial-full-residual-unreturned",label=label,
                    original_error=stats["actual_error"],original_state=stats["observation"],
                    no_missing_stage_residual_or_s_fabricated=True))
            maxima=stats.pop("maxima")
            paid=stats["processed_original_rows"]==ROWS
            row=dict(schema="current-H-one-observed-trial-exact-decomposition-v1",label=label,
                     **stats,full_original_rows_paid=paid,
                     exact_component_identity_verified=stats["identity_rows"]==ROWS,
                     original_norm_comparison_full_domain=paid,
                     maxima={scope:{name:public_max(v,exponent) for name,v in mm.items()}
                             for scope,mm in maxima.items()},
                     original_norm=value["value"].get("original_norm"),
                     original_gate_result=value["value"].get("original_gate_result"),
                     original_error=value["value"].get("error"),
                     no_new_native_acceptance_gate=True)
            if paid:
                row["withJ_printed_norm_readback"]=record_original_norm(
                    {"value":{"original_norm":result["withJ_base_original_norm"]}},
                    maxima["all"].get("withJ_base"),exponent)
                row["trial_printed_norm_readback"]=record_original_norm(value,maxima["all"].get("trial"),exponent)
                if base is not None and base["value"]["returned_complete_residual"]:
                    row["baseline_printed_norm_readback"]=record_original_norm(base,maxima["all"].get("noJ_base"),exponent)
            report=out/(label+"-exact-result.json")
            result["trial_results"].append(dict(label=label,**write(report,row)))
        ledger_path=out/"large-arrays/complete-row-decomposition.jsonl.gz"
        if ledger_path.is_file():
            result["complete_row_ledger"]=dict(file="large-arrays/"+ledger_path.name,
                bytes=ledger_path.stat().st_size,sha256=sha(ledger_path),
                completed_blocks=closed_blocks,original_rows_per_returned_trial=processed_rows,
                temporary_only=True,no_local_or_Git_payload_claim=True)
        result["elapsed_seconds"]=time.monotonic()-started
        result["declared_budget_seconds"]=args.budget_seconds
        result["RHS_root_RK_J_native_calls_in_this_child"]=0
        write(out/"result.json",result)
        compact_result={k:v for k,v in result.items() if k!="input_binding"}
        compact_result["input_binding_sha256"]=hashlib.sha256(encoded(result["input_binding"])).hexdigest()
        write(out/"summary.json",compact_result)
        print(json.dumps(dict(event="request172_exact_decomposition_returned",
            complete=result["complete"],error=result["error"],completed_original_rows=processed_rows,
            trial_result_count=len(result["trial_results"]),unpaid_scope=result["unpaid_scope"],
            result_sha256=sha(out/"result.json"),diagnostic_does_not_choose_original_acceptance=True)),flush=True)
    return 0 if result["complete"] else 2


if __name__=="__main__":
    raise SystemExit(main())
