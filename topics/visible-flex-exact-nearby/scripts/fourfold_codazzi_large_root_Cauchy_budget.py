#!/usr/bin/env python3
"""Consume saved full root rows and original intrinsic jets for real Cauchy energies."""
from __future__ import annotations
import argparse,gzip,hashlib,json,os,shutil,time
from bisect import bisect_right
from fractions import Fraction as Q
from pathlib import Path
from flint import arb,ctx
PUBLIC="Rogerhu12/math-research-public"
KIND="actual_full_real_large_root_Cauchy_two_windows_v1"
ROOT_NATIVE="dbaaf9f7866fceae9583d6cb639441365a64b3ac0d381291fa6d1a5afe247212"
ROOT_SOURCE="840d7ae96c023f0f1055516cfefe62f22a8f46a3f8a0ea2974553b32760eb112"
ROOT_CI="0f688d095b2e6a62d8ba50e678d59bacb89dc25d721964bedd1b37184188a530"
ROOT_MANIFEST="93346b9eb5d968cfdb160c665bd6f524b108d629e81487905b67708ab6c61166"
SHARED="517de329d0cee3466523e9eaaa2747a79ab3da2c771d4ec2984b38784a9b33ee"
BASE="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
ZDEF="6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
RADII=(Q(1,1000),Q(1,500),Q(1,200),Q(1,100),Q(3,200),Q(1,50))
NAME="full-real-large-root-Cauchy-two-windows.json.gz"

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):
    b=Path(path).read_bytes()
    return json.loads(gzip.decompress(b) if str(path).endswith(".gz") else b)
def ex(v):
    x=Q(v);return arb(x.numerator)/x.denominator
def box(v):
    if "lower" in v and "upper" in v:
        return arb(v["lower"]).lower().union(arb(v["upper"]).upper())
    return arb(v["ball"])
def up(v):return abs(arb(v)).upper()
def rec(v):
    v=arb(v);return {"ball":v.str(60),"lower":v.lower().str(60),"upper":v.upper().str(60)}
def save(path,doc):
    raw=(json.dumps(doc,indent=2,allow_nan=False)+"\n").encode()
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=gzip.compress(raw,mtime=0) if str(path).endswith(".gz") else raw
    tmp=path.with_name(path.name+".partial");tmp.write_bytes(raw);tmp.replace(path)
def rowsha(row):
    return hashlib.sha256(json.dumps(row,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def gate(doc,name,ok):
    doc["gates"].append({"name":name,"passed":bool(ok)})
    if not ok:raise ValueError(name)

def validate(a,doc):
    root,p,shared=read(a.root_native),read(a.root_process),read(a.shared)
    gate(doc,"same_actual_successful_1300_row_full_family_real_root_native",
        sha(a.root_native)==ROOT_NATIVE and root.get("complete") and root.get("proved")
        and root.get("failure") is None and root.get("source_sha256")==ROOT_SOURCE
        and root.get("public_repository")==PUBLIC and str(root.get("public_run_id"))=="43616813816"
        and root.get("background_definition_sha256")==BASE
        and root.get("explicit_direction_definition_sha256")==ZDEF
        and root.get("exact_complex_parameter_radius")=="1/100000000"
        and root.get("full193_direction_and_independent_even_mean")
        and len(root.get("rows",[]))==1300 and root.get("complete_original_seams")==1079
        and len(root.get("gates",[]))==15 and all(x["passed"] for x in root["gates"])
        and root.get("all_proposed_radii_passed")
        and len(root.get("cases",[]))==6
        and all(c.get("passed") and len(c.get("gates",[]))==7
            and all(g["passed"] for g in c["gates"]) for c in root["cases"]))
    gate(doc,"original_public_child0_and_exact_root_producer_and_manifest",
        p.get("public_repository")==PUBLIC and str(p.get("run_id"))=="43616813816"
        and p.get("complete") and p.get("failure") is None and p.get("actual_returncode")==0
        and p.get("source_sha256")==ROOT_CI and p.get("manifest_sha256")==ROOT_MANIFEST
        and p.get("mathematical_source_sha256")==ROOT_SOURCE and p.get("mathematical_complete")
        and p.get("mathematical_failure") is None and p.get("native_sha256")==ROOT_NATIVE
        and p.get("native_bytes")==a.root_native.stat().st_size)
    gate(doc,"exact_shared_six_part_original_intrinsic_identity",
        sha(a.shared)==SHARED
        and shared.get("kind")=="fixed_original_intrinsic_third_jet_parts_for_real_root_radius_one_over_fifty_v1"
        and shared.get("repository")==PUBLIC and shared.get("original_body_run")==43583838026
        and len(shared.get("parts",[]))==6)
    intrinsic=[];receipts=[]
    for spec in shared["parts"]:
        path=a.body_artifacts/spec["artifact"]/spec["inner_path"]
        if sha(path)!=spec["sha256"]:raise ValueError("an original intrinsic compressed part changed")
        d=read(path);first,end=spec["common_row_indices"]
        if (d.get("kind")!="actual_full_regular_joint_radial_polynomial_residual_rows_v1"
            or not d.get("complete") or not d.get("selected_cells_complete")
            or d.get("identity")!=shared["original_row_identity"]
            or d.get("selected_indices")!=[first,end] or len(d.get("rows",[]))!=spec["rows"]):
            raise ValueError("the exact complete original intrinsic part identity is required")
        edge=Q(spec["exact_interval"][0])
        for number,row in enumerate(d["rows"],first):
            lo,hi=map(Q,row["interval"])
            if row.get("common_row")!=number or lo!=edge or not lo<hi:
                raise ValueError("original common rows lost their exact closed cover")
            for n in ("gamma","beta","K","K1"):
                value=box(row["intrinsic_whole_third_jets"][n])
                if not value.is_finite():raise ValueError("a saved whole intrinsic jet is nonfinite")
            intrinsic.append((lo,hi,row,spec["sha256"]));edge=hi
        if edge!=Q(spec["exact_interval"][1]) or end-first!=len(d["rows"]):
            raise ValueError("an original part endpoint or count differs")
        receipts.append({"artifact":spec["artifact"],"inner_path":spec["inner_path"],
            "sha256":sha(path),"bytes":path.stat().st_size,"common_row_indices":[first,end]})
    gate(doc,"all_six_original_parts_gap_free_and_no_target_recomputed",
        all(a[1]==b[0] for a,b in zip(intrinsic,intrinsic[1:])))
    lo,hi=map(Q,root["exact_root_interval"]);left=lo-max(RADII);right=hi
    gate(doc,"true_root_ball_and_full_negative_window_are_inside_zero_compact_support",
        Q(9,50)<left<lo<hi and hi-lo<Q(1,10**9)
        and list(map(Q,root["exact_cover"]))==[left,hi+max(RADII)]
        and intrinsic[0][0]<=left<right<=intrinsic[-1][1])
    rows=[]
    edge=Q(root["exact_cover"][0])
    for number,row in enumerate(root["rows"]):
        x,y=map(Q,row["interval"])
        if x!=edge or not x<y:raise ValueError("original root row cover has a gap")
        if x<right and y>left:rows.append((x,y,row,number))
        edge=y
    if edge!=Q(root["exact_cover"][1]):raise ValueError("original root cover lost its far endpoint")
    doc["original_intrinsic_part_receipts"]=receipts
    return root,intrinsic,rows,lo,hi

def budget(rootrow,intrinsic_row,left,right,rlo,rhi):
    jets=intrinsic_row["intrinsic_whole_third_jets"]
    kr=box(jets["K1"]).lower()
    if not kr>1:raise ValueError("the actual whole K_r lower bound does not exceed1")
    rb=rootrow["bounds"];eta=up(box(rb["eta_upper"]))
    if not eta<=ex(Q(13,10)):raise ValueError("the full-family angular speed exceeds13over10")
    rho=max(abs(rlo-left),abs(rlo-right),abs(rhi-left),abs(rhi-right))
    # Both quantities independently bound |K| on this true intersection.
    q2=min(up(box(jets["K"])),(up(box(rb["k_upper"]))*ex(rho)).upper())
    q=q2.sqrt().upper();W=(1+q2).sqrt().upper()
    b=up(box(rb["beta"]));gamma=up(box(jets["gamma"]))
    z=rootrow["strips"]["1/64"]
    U=[up(box(x)) for x in z["U"]];V=[up(box(x)) for x in z["V"]]
    if len(U)!=5 or len(V)!=5:raise ValueError("a full original angular derivative was dropped")
    D1=up(box(z["D1"]));D2=up(box(z["D2"]))
    A0=b*(1+3*U[0]**2+q2*V[0]**2)
    A1=b*(6*U[0]*U[1]+2*q2*V[0]*V[1])
    B0=b*(1+U[0]**2+3*q2*V[0]**2)
    B1=b*(2*U[0]*U[1]+6*q2*V[0]*V[1])
    L0=2*b*U[0]*V[0];L1=2*b*(U[1]*V[0]+U[0]*V[1])
    CI=arb(17).sqrt()/4
    zero={"transport":ex(Q(21,2))*D1,
        "local":10*(A0+B0)+4*(q+W)*L0,
        "primitive":8*b*(W*U[0]+q2*V[0])*(ex(Q(41,100))*(U[1]+U[2])+V[1]/4),
        "independent_mean":4*gamma*(q2*(V[1]+V[2])+U[1])}
    minus={"transport":D1/2+ex(Q(40,3))*(D1+D2),
        "local":10*(A0+A1+B0+B1)+4*(q+W)*(L0+L1),
        "primitive":8*b*CI*(U[1]+V[1])*(W*(U[0]+U[1])+q2*(V[0]+V[1])),
        "independent_mean":4*gamma*(q2*V[1]+U[1])}
    zero={k:v.upper() for k,v in zero.items()};minus={k:v.upper() for k,v in minus.items()}
    return {"K_r_lower":rec(kr),"eta_upper":rec(eta),"q_squared_upper":rec(q2),
        "W_upper":rec(W),"H0_growth_components":{k:rec(v) for k,v in zero.items()},
        "Hminus1_growth_components":{k:rec(v) for k,v in minus.items()},
        "H0_growth":rec(sum(zero.values(),arb(0)).upper()),
        "Hminus1_growth":rec(sum(minus.values(),arb(0)).upper())}

def run(a,doc):
    root,intrinsic,rows,rlo,rhi=validate(a,doc)
    left=rlo-max(RADII);right=rhi
    cuts={left,right}
    for x,y,*_ in intrinsic+rows:
        if left<x<right:cuts.add(x)
        if left<y<right:cuts.add(y)
    for radius in RADII:cuts.add(rlo-radius)
    cuts=sorted(cuts);istarts=[x[0] for x in intrinsic];rstarts=[x[0] for x in rows]
    requests=[]
    for x,y in zip(cuts,cuts[1:]):
        ir=intrinsic[bisect_right(istarts,x)-1];rr=rows[bisect_right(rstarts,x)-1]
        if not(ir[0]<=x<y<=ir[1] and rr[0]<=x<y<=rr[1]):
            raise ValueError("an exact common-refinement cell crossed an original provider interval")
        requests.append((x,y,ir,rr))
    doc["rows"]=[]
    if a.resume:
        old=read(a.resume)
        gate(doc,"same_source_and_inputs_completed_new_common_rows_reused",
            old.get("kind")==KIND and old.get("source_sha256")==sha(__file__)
            and old.get("input_sha256")==doc["input_sha256"])
        if len(old.get("rows",[]))>len(requests):raise ValueError("old prefix exceeds the true request")
        for saved,(x,y,ir,rr) in zip(old.get("rows",[]),requests):
            if (saved.get("interval")!=[str(x),str(y)]
                or saved.get("original_common_row")!=ir[2]["common_row"]
                or saved.get("original_intrinsic_row_sha256")!=rowsha(ir[2])
                or saved.get("original_root_row_sha256")!=rowsha(rr[2])
                or not saved.get("complete_new_scalar_budget")):
                raise ValueError("a completed scalar budget identity changed")
            doc["rows"].append(saved)
        doc["reused_new_common_rows"]=len(doc["rows"])
    else:doc["reused_new_common_rows"]=0
    doc["new_common_rows_in_this_child"]=0
    for x,y,ir,rr in requests[len(doc["rows"]):]:
        values=budget(rr[2],ir[2],x,y,rlo,rhi)
        doc["rows"].append(dict(interval=[str(x),str(y)],
            original_common_row=ir[2]["common_row"],original_body_part_sha256=ir[3],
            original_intrinsic_row_sha256=rowsha(ir[2]),original_root_row_index=rr[3],
            original_root_row_sha256=rowsha(rr[2]),
            original_candidate_and_response_piece=rr[2]["candidate_and_response_piece"],
            complete_new_scalar_budget=True,bounds=values))
        doc["new_common_rows_in_this_child"]+=1
        if len(doc["rows"])%128==0:
            save(a.out,doc);print(json.dumps({"complete_common_rows":len(doc["rows"]),"total":len(requests)}),flush=True)
    gate(doc,"every_actual_common_interval_retained_with_Kprime_and_eta_gates",
        len(doc["rows"])==len(requests) and bool(doc["rows"])
        and doc["rows"][0]["interval"][0]==str(left)
        and doc["rows"][-1]["interval"][1]==str(right))
    gate(doc,"regular_multiplier_constants_are_valid",
        ex(Q(13,10)).exp()<4 and 2*ex(Q(13,10))/(3*arb(1).exp())<ex(Q(1,3))
        and (arb(17).log()/6).exp()/4<ex(Q(41,100)))
    doc["cases"]=[]
    for radius in RADII:
        lo=rlo-radius
        selected=[r for r in doc["rows"] if Q(r["interval"][0])>=lo]
        if not selected or selected[0]["interval"][0]!=str(lo):
            raise ValueError("a requested radius boundary was not in the true common cover")
        Qmax=max(up(box(r["bounds"]["q_squared_upper"])) for r in selected)
        W=(1+Qmax).sqrt().upper()
        C={}
        for label,key in (("H0","H0_growth"),("Hminus1","Hminus1_growth")):
            integral=sum((ex(Q(r["interval"][1])-Q(r["interval"][0]))
                *up(box(r["bounds"][key])) for r in selected),arb(0)).upper()
            growth=integral.exp().upper();raw=(4*W*growth).upper()
            C[label]={"integrated_growth":rec(integral),"exponential_growth":rec(growth),
                "full_root_to_state":rec(raw),
                "ordinary_L2_radial_source":rec((raw*ex(radius).sqrt()).upper()),
                "sum_actual_affine_jumps":rec(raw)}
        rawminus=up(box(C["Hminus1"]["full_root_to_state"]))
        CI=arb(17).sqrt()/4
        C["primitive_after_Hminus1"]={
            "full_root_bracket_to_L2":rec((CI*rawminus).upper()),
            "ordinary_L2_radial_source_to_L2":rec((CI*rawminus*ex(radius).sqrt()).upper())}
        kr=min(box(r["bounds"]["K_r_lower"]).lower() for r in selected)
        eta=max(up(box(r["bounds"]["eta_upper"])) for r in selected)
        okay=bool(kr>1 and eta<=ex(Q(13,10)) and all(
            box(C[k]["full_root_to_state"]).is_finite() for k in ("H0","Hminus1")))
        if not okay:raise ValueError("a complete numerical Cauchy constant is not finite")
        doc["cases"].append(dict(exact_radius=str(radius),
            exact_enclosing_negative_interval=[str(lo),str(rhi)],
            actual_true_rho_interval=["0",str(radius)],common_rows=len(selected),
            K_r_lower=rec(kr),eta_upper=rec(eta),q_squared_upper=rec(Qmax),
            W_upper=rec(W),bounds=C,passed=True))
    gate(doc,"all_six_real_radii_include_complete_both_energy_and_source_windows",
        len(doc["cases"])==6 and all(c["passed"] for c in doc["cases"]))
    doc.update(complete=True,selected=doc["cases"][-1],exact_root_interval=[str(rlo),str(rhi)],
        exact_cover=[str(left),str(right)],exact_real_delta_radius="1/100000000",
        background_definition_sha256=BASE,explicit_direction_definition_sha256=ZDEF,
        physical_parameter="fixed physical eta0 with nu_delta=nu0+delta; compact bump exactly zero here",
        complete_original_root_rows=1300,complete_new_common_rows=len(doc["rows"]),
        all_frequencies_and_independent_even_mean_retained=True,
        source_windows={"H0":{"root_and_jumps":["H1/3","L2"],"ordinary":["H1/3","H1/3"]},
            "Hminus1":{"root_and_jumps":["Hminus2/3","Hminus1"],"ordinary":["Hminus2/3","Hminus2/3"]}},
        same_full_real_family_root_Cauchy_estimate_proved=True,
        old_target_candidate_response_coefficients_recomputed=0,
        actual_reconstructed_trial_jump_norms_evaluated=False,
        positive_side_lower_source_window_proved=False,complex_parameter_Hilbert_energy_claimed=False,
        numerical_full_return_strong_norm_or_cutoff_proved=False,
        full_low_high_Schur_inverse_proved=False,complete_infinite_BVP_inverse_proved=False,
        true_parameter_Schur_proved=False,actual_PDE_branch_proved=False)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for n in ("root-native","root-process","shared","body-artifacts","out"):
        p.add_argument("--"+n,type=Path,required=True)
    p.add_argument("--resume",type=Path);a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("all new mathematical consumption runs only in public repository Actions")
    if a.out.exists():raise FileExistsError("preserve every actual Cauchy-energy prefix")
    ctx.prec=256;ctx.cap=6;started=time.monotonic()
    shared=read(a.shared)
    identities={n:sha(getattr(a,n.replace("-","_"))) for n in ("root-native","root-process","shared")}
    for s in shared["parts"]:
        identities[s["artifact"]+"/"+s["inner_path"]]=sha(a.body_artifacts/s["artifact"]/s["inner_path"])
    doc=dict(kind=KIND,complete=False,failure=None,gates=[],rows=[],source_sha256=sha(__file__),
        input_sha256=identities)
    if a.resume:
        old=read(a.resume)
        if old.get("complete") and not old.get("failure"):
            if (old.get("kind")!=KIND or old.get("source_sha256")!=sha(__file__)
                or old.get("input_sha256")!=identities or not old.get("gates")
                or not all(g["passed"] for g in old["gates"])
                or len(old.get("cases",[]))!=6 or not all(c["passed"] for c in old["cases"])):
                raise ValueError("a complete original scalar budget changed identity")
            a.out.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(a.resume,a.out)
            print(json.dumps({"complete_native_reused":True,"new_scalar_rows":0}),flush=True);return
    try:run(a,doc)
    except BaseException as error:
        doc["failure"]={"type":type(error).__name__,"message":str(error)};raise
    finally:
        doc["seconds"]=time.monotonic()-started;save(a.out,doc)
    print(json.dumps({"complete":True,"gates":len(doc["gates"]),"new_rows":doc["new_common_rows_in_this_child"],
        "radius":doc["selected"]["exact_radius"],"seconds":doc["seconds"]}),flush=True)
if __name__=="__main__":main()
