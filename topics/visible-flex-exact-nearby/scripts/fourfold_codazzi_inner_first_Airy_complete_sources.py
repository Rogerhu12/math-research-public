#!/usr/bin/env python3
"""Complete inner first-correction sources from accepted Taylor and matrix natives.

All new interval arithmetic runs only in the public repository Actions.
No original coefficient, Fourier, flow, fold or Taylor stage is re-evaluated.
"""
from __future__ import annotations
import argparse,copy,gzip,hashlib,json,math,os,sys,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy as np
from flint import arb,ctx

PUBLIC="Rogerhu12/math-research-public"
TAYLOR="18990ac2c1ed8e559d00982b75d663c08ad7e193455de1f8482511c36938b719"
TPROC="eebbbf37419729069c28ef3cd7c7d34f02154b8c391b0cfa9ca093de8855a356"
TSOURCE="e4ccbf4b343623d74d089f79b6605a0601975c6ea5c1d2e113bad568fe60167d"
TMANIFEST="226e5acac42026431acbd166f92d423b6292ba6f73e65f58f808647d4701f1ad"
AUX="84e2bd1b7637299e94428b22cc19aba290d0b661f9dbe18dae918bf752f10077"
APROC="855730f8bf86d04c6cc7622e1881f9fc29a2af754694dfaf5dad16012b98544e"
FOLD="0ceafc2ba2adb8c1e14ab74c3059b0a0fde39446855df0889dec741f1cb61cfe"
RADIAL="fec8740c26064b973c61828a960c3e5c7e864b83542222c155b9e56474c39853"
NORM="7662350ac2cf5c0838e545fb6ba4994c118b985b5a133b869b3ca5486b70563c"
BASE="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
ZDEF="6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
DELTA=Q(1,10**8)
SIGMA=Q(1,512)
INNER=Q(9,10**6)
CUTOFF=97
WORD_NAMES=("SV","SQ","RQJ","RQJL","primitive","uJ","uJL","uJB")
TERM_NAMES=("complete_SV","complete_SQ","complete_RQ_J_gd","complete_RQ_JL_h",
    "complete_primitive_error","old_mean_rQ","old_mean_vphi","old_mean_raw_D","old_mean_V0")

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def payload_sha(v):
    return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def read(path):
    path=Path(path);raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix==".gz" else raw)
def save(path,v):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(v,separators=(",",":"),allow_nan=False)+"\n").encode()
    if path.suffix==".gz":raw=gzip.compress(raw,compresslevel=6,mtime=0)
    t=path.with_name(path.name+".partial");t.write_bytes(raw);t.replace(path)
def ex(v):
    v=Q(v);return arb(v.numerator)/v.denominator
def box(v):
    if isinstance(v,str):return arb(v)
    if "lower" in v and "upper" in v:
        return arb(v["lower"]).lower().union(arb(v["upper"]).upper())
    return arb(v["ball"])
def up(v):return abs(v).upper()
def record(v):
    v=arb(v)
    if not v.is_finite():raise ValueError("nonfinite inner source bound")
    return dict(ball=v.str(64))
def encode(v):
    if isinstance(v,dict):return {str(k):encode(x) for k,x in v.items()}
    if isinstance(v,(tuple,list)):return [encode(x) for x in v]
    return record(v)
def decode(v):
    if isinstance(v,dict):
        if "ball" in v:return box(v)
        return {k:decode(x) for k,x in v.items()}
    if isinstance(v,list):return [decode(x) for x in v]
    return v
def powr(v,p):
    if not v>0:raise ValueError("a fractional power lacks its proved positive argument")
    return (v.log()*ex(p)).exp()
def ipow(v,n):
    if n<0:raise ValueError("negative integer power requires a paid denominator")
    out=arb(1)
    for _ in range(n):out*=v
    return out
def ensure_nonnegative(v):
    if isinstance(v,dict):return all(ensure_nonnegative(x) for x in v.values())
    if isinstance(v,list):return all(ensure_nonnegative(x) for x in v)
    return v.is_finite() and v.lower()>=0
def vadd(*vv):
    return [sum((v[k] for v in vv),arb(0)).upper() for k in range(2)]
def vscale(v,c):return [(c*x).upper() for x in v]
def vjadd(*aa):
    if len({len(a) for a in aa})!=1:raise ValueError("unpaid vector jet in sum")
    return [vadd(*(a[k] for a in aa)) for k in range(len(aa[0]))]
def svjets(s,v,last):
    if len(s)<=last or len(v)<=last:raise ValueError("unpaid scalar vector jet")
    return [[sum((math.comb(k,l)*s[l]*v[k-l][i] for l in range(k+1)),arb(0)).upper()
             for i in range(2)] for k in range(last+1)]
def mv(a,v):
    return [sum((a[i][j]*v[j] for j in range(2)),arb(0)).upper() for i in range(2)]
def mvjets(a,v,last):
    if len(a)<=last or len(v)<=last:raise ValueError("unpaid ordered matrix jet")
    return [[sum((math.comb(k,l)*mv(a[l],v[k-l])[i] for l in range(k+1)),arb(0)).upper()
             for i in range(2)] for k in range(last+1)]

def power_angular_jets(p,Am,Ap,A):
    p=Q(p)
    return [powr(Ap if p>0 else Am,p),
        (ex(abs(p))*powr(Am,p-1)*A[1]).upper(),
        (ex(abs(p))*powr(Am,p-1)*A[2]+ex(abs(p*(p-1)))*powr(Am,p-2)*A[1]*A[1]).upper(),
        (ex(abs(p))*powr(Am,p-1)*A[3]
         +3*ex(abs(p*(p-1)))*powr(Am,p-2)*A[1]*A[2]
         +ex(abs(p*(p-1)*(p-2)))*powr(Am,p-3)*ipow(A[1],3)).upper()]

def complete_fourier(tau):
    if not tau>0:raise ValueError("the actual inverse-phase strip is not positive")
    q=(-4*tau).exp();L=CUTOFF
    while not (q*powr(ex(Q(L+1,L)),Q(4,3))).upper()<1:
        L*=2
        if L>2**20:raise ValueError("no finite proved geometric-tail start")
    def lam(j):return ex(1+16*j*j).sqrt()
    center=powr(lam(CUTOFF),Q(-1,3))
    finite=sum((ipow(q,l)*powr(lam(CUTOFF),Q(4,3))
        /powr(lam(CUTOFF-l),Q(5,3)) for l in range(1,CUTOFF)),arb(0)).upper()
    bridge=sum((ipow(q,l)*powr(lam(l),Q(4,3))
        for l in range(CUTOFF,L)),arb(0)).upper()
    ratio=(q*powr(ex(Q(L+1,L)),Q(4,3))).upper()
    tail=(ipow(q,L)*powr(lam(L),Q(4,3))/(1-ratio)).upper()
    total=(center+2*finite+2*bridge+2*tail).upper()
    return total,dict(exact_output_old_phi_width=str(SIGMA),tail_first_lag=L,
        inverse_phase_width=record(tau),complete_factor=record(total),
        diagonal=record(center),both_small_lags=record(2*finite),
        both_bridge_lags=record(2*bridge),both_infinite_tails=record(2*tail),
        geometric_ratio=record(ratio),mean_output_and_both_lag_signs_retained=True)

def inner_profile(case,R):
    if not (case["complete"] and case["proved"] and case["failure"] is None):
        raise ValueError("the original smaller auxiliary case is not proved")
    if Q(case["exact_fold_radius"])!=Q(3,40000):
        raise ValueError("the originally paid smaller auxiliary domain changed")
    if not (Q(case["exact_old_leading_width"])==Q(3,128)
        and Q(case["exact_coefficient_width"])==Q(1,32)
        and SIGMA<Q(case["exact_old_leading_width"])):
        raise ValueError("an actual amplitude coefficient strip is missing")
    c=decode(case["coefficient_evidence"]["complete_coefficient_majorants"])
    f=decode(case["fold_evidence"]["complete_fold_and_leading_bounds"])
    le=case["direct_leading_evidence"]
    aj=decode(le["A_mixed_derivatives"])
    A=[up(f["Ap"])]+[up(aj[str((0,q))]) for q in range(1,4)]
    Am=f["Am"].lower();Ap=up(f["Ap"])
    E=up(f["E"]);m=(2-E).lower();M=E
    flow=decode(le["finite_variational_C"])
    F2=(ex(Q(case["exact_fold_radius"]))*up(flow["2"])).upper()
    F3=(ex(Q(case["exact_fold_radius"]))*up(flow["3"])).upper()
    if not (Am>0 and m>0 and c["em"]>0 and R<ex(Q(case["exact_fold_radius"]))):
        raise ValueError("the common inner interval lost a true fold or coefficient gap")
    P2=(F2/ipow(m,3)).upper()
    P3=(F3/ipow(m,4)+3*F2*F2/ipow(m,5)).upper()
    C0=(1/m.sqrt()).upper()
    C2=(M.sqrt()*(1/ipow(m,2)+2*P2*P2+1/ipow(m,4)+P3*P3
        +ex(Q(9,2))*P2*P2/ipow(m,2)+1/ipow(m,6)).sqrt()).upper()
    composition=(powr(C0,Q(1,6))*powr(C2,Q(5,6))).upper()
    fourier,evidence=complete_fourier((m*ex(SIGMA)).lower())
    plus=power_angular_jets(Q(1,3),Am,Ap,A)
    minus=power_angular_jets(Q(-1,3),Am,Ap,A)
    PQ=[[[arb(0),(c["ap"]*R*plus[q]).upper()],
         [(c["ap"]*minus[q]).upper(),arb(0)]] for q in range(4)]
    L1=(ex(Q(2,3))*A[1]/Am).upper()
    L2=(ex(Q(2,3))*(A[2]/Am+A[1]*A[1]/(Am*Am))).upper()
    H=powr(Am,Q(-1,6));N=powr(R,Q(1,4))*powr(ex(4*CUTOFF),Q(-1,6))
    B=powr(R,Q(1,2))*powr(Ap,Q(1,6))
    def sc(x,v):return [(x*y).upper() for y in v]
    real_negative=[
        [sc(H,[16,94*L1,1208*L1*L1+94*L2]),sc(N,[8,51*L1,650*L1*L1+51*L2])],
        [sc(H,[3,16*L1,209*L1*L1+16*L2]),sc(B,[4,22*L1,290*L1*L1+22*L2])],
        [sc(H,[3,16*L1,209*L1*L1+16*L2]),sc(B,[4,22*L1,290*L1*L1+22*L2])]]
    real_positive=[[sc(H,[3,3*L1,5*L1*L1+3*L2]),sc(N,[3,3*L1,6*L1*L1+3*L2])]]
    zz=powr(3*Ap/(2*Am),Q(2,3));ez=(zz+zz*zz/2).exp().upper()
    cm=(ex(Q(5,36)).exp()/(2*arb.pi().sqrt())).upper()
    cp=(ex(Q(5,72)).exp()/(2*arb.pi().sqrt())).upper()
    analytic=dict(central=[(ez*powr(3/(2*Am),Q(1,6))).upper(),(ez*N).upper()],
        negative=[(cm*H).upper(),(ex(Q(47,36))*cm*B).upper()],
        positive=[(cp*H).upper(),(ex(Q(47,36))*cp*B).upper()])
    near=(powr(ex(2),Q(5,3))*powr(ex(1+16*CUTOFF*CUTOFF).sqrt(),Q(-1,3))).upper()
    far_sum=powr(ex(CUTOFF),Q(-4,3))+3*powr(ex(CUTOFF),Q(-1,3))
    far=(8*far_sum.sqrt()).upper()
    payload=dict(numeric=encode(dict(c=c,PQ=PQ,m=m,M=M,F2=F2,F3=F3,
        composition=composition,fourier=fourier,near=near,far=far,
        analytic_profiles=analytic,real_negative=real_negative,real_positive=real_positive)),
        complete_fourier_evidence=evidence,original_smaller_auxiliary_payload_sha256=payload_sha(case),
        exact_inner_rho_cover=record(R),all_old_auxiliary_values_reused=True,
        only_new_inner_profile_and_PQ_budget_arithmetic=True,
        analytic_amplitude_old_phi_width=str(SIGMA),real_two_derivative_space_separate=True,
        exact_PQ_top_right_identity="-a*rho*A^(1/3)",all_original_carrier_signs_retained=True)
    return payload

def amplitude_jets(row,c,PQ):
    vals=decode(row["first_amplitude_budgets"])
    w=[[up(vals[k]["strip_sup"]["0,"+str(q)]) for k in ("a1","b1")] for q in range(4)]
    wr=[[up(vals[k]["strip_sup"]["1,"+str(q)]) for k in ("a1","b1")] for q in range(3)]
    U=[up(x) for x in c["U"][0]]
    V=[up(x) for x in c["V"][0]]
    D=[up(x) for x in c["D"]]
    if min(len(U),len(V),len(D))<4:raise ValueError("complete coefficient angular jets missing")
    Pw=mvjets(PQ,w,3)
    h=[vscale(x,1/c["em"].lower()) for x in Pw[:3]]
    y=svjets(V,Pw,2)
    dw=vjadd(wr,svjets(D,w[1:],2))
    gd=vjadd(dw,Pw[1:])
    qv=vjadd(svjets(V,gd,2),svjets(V[1:],Pw,2))
    vn=list(V);vn[0]=min(V[0],V[1]/4).upper()
    result=dict(w=w[:3],h=h,y=y,gd=gd,qv=qv,uh=svjets(U,h,2),vmw=svjets(vn,w,2))
    if not ensure_nonnegative(result):raise ValueError("an inner complete amplitude jet is invalid")
    return result

def Airy_bound(real_jets,analytic_value,p,side):
    def scalar(profile):
        return sum((a*b for a,b in zip(profile,analytic_value)),arb(0)).upper()
    central=scalar(p["analytic_profiles"]["central"])
    branch=scalar(p["analytic_profiles"][side])
    core=((central*central+4*branch*branch).sqrt().upper()
        if side=="negative" else max(central,branch).upper())
    analytic=(p["composition"]*p["fourier"]*core).upper()
    real=None
    if real_jets is not None:
        real=arb(0)
        for pa,pb in p["real_"+side]:
            symbol=[sum((math.comb(k,l)*(pa[l]*real_jets[k-l][0]
                +pb[l]*real_jets[k-l][1]) for l in range(k+1)),arb(0)).upper()
                for k in range(3)]
            b2=(symbol[2]/(p["m"]*p["m"])
                +symbol[1]*p["F2"]/ipow(p["m"],3)).upper()
            real+=(p["composition"]*(p["near"]*(symbol[0]+arb.pi()*arb.pi()*b2/48)
                +p["far"]*b2)).upper()
        real=real.upper()
    chosen=analytic if real is None else min(analytic,real).upper()
    if not (chosen.is_finite() and chosen.lower()>=0):raise ValueError("invalid all-output Airy bound")
    return dict(bound=record(chosen),analytic_complete=record(analytic),
        real_two_derivative_complete=None if real is None else record(real),
        choice="analytic" if real is None or analytic<=real else "real_two_derivative",
        full_mean_and_all_outputs_retained=True)

def matrix_conversion(row):
    candidates=[];evidence=[]
    for width in row["complete_width_evidence"]:
        if not width["usable"]:
            evidence.append(dict(width=width["width"],usable=False,
                original_reason=width.get("reason")))
            continue
        k=up(box(width["kappa_5over3"]))
        words=width["operator_words"]
        values={name:(k*up(box(words[name]["z"]))).upper() for name in WORD_NAMES}
        if not ensure_nonnegative(values):raise ValueError("invalid complete same-order matrix word")
        candidates.append(values)
        evidence.append(dict(width=width["width"],usable=True,
            original_complete_word_payload_sha256=payload_sha(words),
            original_kappa_5over3=width["kappa_5over3"],same_order_costs=encode(values)))
    if not candidates:raise ValueError("no original admissible full-matrix width")
    values={k:min(d[k] for d in candidates).upper() for k in WORD_NAMES}
    return dict(costs=encode(values),complete_original_width_choices=evidence,
        original_coefficient_row_payload_sha256=payload_sha(row),
        old_complete_operator_triples_recomputed=False,conversion="kappa_5over3 times z, not right_gain")

def row_constants(c,z,A):
    aa={k:up(box(v["bound"])) for k,v in A.items()}
    terms=dict(
        complete_SV=z["SV"]*aa["w"],
        complete_SQ=z["SQ"]*aa["h"],
        complete_RQ_J_gd=z["RQJ"]*aa["gd"],
        complete_RQ_JL_h=z["RQJL"]*aa["h"],
        complete_primitive_error=z["primitive"]*aa["qv"],
        old_mean_rQ=c["m0_rQ"]*aa["h"],
        old_mean_vphi=c["cB"]*c["V"][1]*aa["y"],
        old_mean_raw_D=(c["cB"]*c["V"][1]*min(c["V"][0],c["V"][1]/4)/4
                       +c["m0_T0"])*aa["gd"],
        old_mean_V0=c["m0_V0"]*aa["w"])
    meanparts=dict(direct_u_h=aa["uh"],complete_uJ_gd=z["uJ"]*aa["gd"],
        complete_uJL_h=z["uJL"]*aa["h"],complete_uJB_w=z["uJB"]*aa["w"],
        complete_curvature_v_nonmean_w=c["K"]*aa["vmw"])
    first=(c["C_J_scalar"]*sum(terms.values(),arb(0))).upper()
    local=(c["C_J_scalar"]*aa["local_numerator"]).upper()
    mean=(c["exact_nonlocal_even_mean_row_factor"]*sum(meanparts.values(),arb(0))).upper()
    total=((first+local)*(first+local)+mean*mean).upper()
    if not ensure_nonnegative([first,local,mean,total]):
        raise ValueError("a complete inner first-correction source is invalid")
    return dict(first_nonlocal_singular_envelope=record(first),
        first_local_singular_envelope=record(local),independent_even_mean_singular_envelope=record(mean),
        complete_squared_vector_envelope=record(total),
        complete_nine_nonlocal_terms=encode(terms),complete_five_even_mean_terms=encode(meanparts),
        original_final_J_window=record(c["C_J_scalar"]),
        original_even_mean_factor=record(c["exact_nonlocal_even_mean_row_factor"]),
        local_numerator_is_unnormalized=True,local_nonlocal_triangle_before_component_squares=True)

def radial_weight(left,right,roots,side):
    lo,hi=roots
    if not left<right:raise ValueError("empty new partial source interval")
    if right<=lo:
        return arb(0) if side=="positive" else (2*(ex(lo-left).sqrt()-ex(lo-right).sqrt())).upper()
    if left>=hi:
        return arb(0) if side=="negative" else (2*(ex(right-hi).sqrt()-ex(left-hi).sqrt())).upper()
    if not lo<=left<right<=hi:raise ValueError("a new integral crossed a root endpoint")
    return (2*ex(right-left).sqrt()).upper()

DIRECTED="3c8c4f3c93108de5a1c17149518f3aa16500a7f8ad58343f7a8dac325cc48d4b"
DPROC="00afd54464db46f110ecff8c1968b158deedac719a363590fc366038b47fedb8"
DSOURCE="f3a5d7b0caad97d65464e6b79e0884e3a50085cbc6b2d9bab35e9ab1e8a66b0d"
DMANIFEST="29465d2a93165f40f42b2ea73c772374a882475fd59f44fdbce20b37ff4d402f"
LEGACY_SOURCE="bac8b991fb2672017f14b1068282eb7876aa93eda6f198f3bedd6c5e2f23c095"
LEGACY_MANIFEST="373af63c2d6357a01210dc2d746d26fea79758f6c9068f5bef68d06c671ecef6"
LEGACY_NATIVE="76df4e555b4bbaa84c061ee922c799671190c6a47736a52a5fed12f1c91a957b"
LEGACY_PROCESS="ee53c2516f4d1c8fdd4512d93b5d50d56c1b2fe4f088a42c15e7b37cdf495279"
LEGACY_STAGES={
    "new-inner-Airy-profile-and-exact-PQ-jets":
        "9809a086152cbf69649dea0a0fcc90710411897caa02863992294530ca2f87b2",
    "all-inner-amplitudes-and-complete-Airy-operators":
        "1f46b066ae07b7d06cf9678040aa4bab0a04232b80f24a899819cef7eea3a0a8"}

def exact_two_stage_schema_migration(repo,manifest,doc,check):
    """The only cross-source exception is the identified pre-matrix failed run.

    The original complete profile/amplitude functions and all_airy closure are
    byte-identical. Both accepted original payloads are copied unchanged.
    No matrix conversion or integral from a different producer is inherited.
    """
    paths={k:repo/v for k,v in manifest["input_paths"].items()}
    fixed=(("legacy_source",LEGACY_SOURCE,31319),
           ("legacy_manifest",LEGACY_MANIFEST,20483),
           ("legacy_native",LEGACY_NATIVE,12436),
           ("legacy_process",LEGACY_PROCESS,15314))
    check("only the exact identified failed source manifest native and process permit schema migration",
        all(paths[k].is_file() and sha(paths[k])==h and paths[k].stat().st_size==n
            for k,h,n in fixed))
    prev=read(paths["legacy_native"]);process=read(paths["legacy_process"])
    old_manifest=read(paths["legacy_manifest"])
    oldtext=paths["legacy_source"].read_text();newtext=Path(__file__).read_text()
    def closure(text):
        start=text.index("\n        def all_airy():\n")+1
        end=text.index('\n        amplitude=stage("all-inner-amplitudes-and-complete-Airy-operators"',start)+1
        return text[start:end]
    oldprefix=oldtext.split("def matrix_conversion(",1)[0]
    newprefix=newtext.split("def matrix_conversion(",1)[0]
    oldclosure,newclosure=closure(oldtext),closure(newtext)
    thash=lambda x:hashlib.sha256(x.encode()).hexdigest()
    check("both successful stages retain the exact complete original numerical function closure",
        oldprefix==newprefix and oldclosure==newclosure
        and thash(oldprefix)=="45af989916129a4d193e6ad948cc2c83d9a5428c9f8181161b4bafe47c3413df"
        and thash(oldclosure)=="b0b627aaa4ca7edcb14c64f1fcc534a56d565b1e17627420714b44bb3d11406d")
    changed={
        "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_inner_first_Airy_complete_sources.py",
        "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_inner_first_Airy_complete_sources_CI.py"}
    pins={f["path"]:f for f in manifest["files"]}
    check("all original59 inputs except the two declared reader entry points retain exact pins",
        len(old_manifest["files"])==59
        and all(f==pins.get(f["path"]) for f in old_manifest["files"] if f["path"] not in changed)
        and all(manifest["input_paths"].get(k)==v for k,v in old_manifest["input_paths"].items()))
    keys=("public_repository","runtime","original_Taylor_native_sha256",
        "original_Taylor_process_sha256","original_auxiliary_native_sha256",
        "original_exact_fold_native_sha256","original_exact_fold_process_sha256",
        "original_radial_reference_native_sha256","original_completed_norm_native_sha256",
        "exact_real_delta_radius","fixed_intrinsic_parameter","input_cutoff","physical_frequency",
        "source_window","exact_physical_inner_interval","exact_root_interval",
        "exact_original_physical_piece_interval","original_directed_table_sha256")
    failure={"type":"KeyError","message":"'complete_width_evidence'"}
    check("the original child1 ended after exactly two successful stages and before every matrix or integral",
        str(process["run_id"])==str(prev["run_id"])=="43656438723"
        and str(process["run_attempt"])==str(prev["run_attempt"])=="1"
        and process["actual_returncode"]==1 and process["mathematical_failure"]==failure
        and process["mathematical_source_sha256"]==prev["source_sha256"]==LEGACY_SOURCE
        and process["manifest_sha256"]==prev["input_manifest_sha256"]==LEGACY_MANIFEST
        and process["native_sha256"]==LEGACY_NATIVE and process["native_bytes"]==12436
        and prev["complete"] is False and prev["proved"] is False and prev["failure"]==failure
        and all(prev.get(k)==doc.get(k) for k in keys)
        and len(prev["gates"])==9 and all(g["passed"] for g in prev["gates"])
        and process["mathematical_gates"]==prev["gates"]
        and prev["new_stages"]==process["new_stages"]==2
        and prev["reused_stages"]==process["reused_stages"]==0
        and prev["matrix_conversions"]=={} and prev["rows"]==[]
        and prev["new_same_order_matrix_conversions"]==prev["new_source_integral_rows"]==0
        and set(prev["stages"])==set(LEGACY_STAGES)
        and process["accepted_stage_payloads"]=={
            k:dict(complete=True,payload_sha256=v) for k,v in LEGACY_STAGES.items()})
    for name,expected in LEGACY_STAGES.items():
        old=prev["stages"][name]
        if old["complete"] is not True or old["payload_sha256"]!=expected or payload_sha(old["payload"])!=expected:
            raise ValueError("an exact original successful stage payload changed")
    doc["stages"]=copy.deepcopy(prev["stages"])
    doc["specific_legacy_two_stage_reuse"]=dict(
        original_run_id="43656438723",original_run_attempt="1",original_actual_returncode=1,
        original_source_sha256=LEGACY_SOURCE,original_manifest_sha256=LEGACY_MANIFEST,
        original_native_sha256=LEGACY_NATIVE,original_native_bytes=12436,
        original_process_sha256=LEGACY_PROCESS,original_process_bytes=15314,
        original_failure=copy.deepcopy(prev["failure"]),successful_stage_payloads=copy.deepcopy(LEGACY_STAGES),
        original_complete_profile_amplitude_prefix_sha256=thash(oldprefix),
        original_all_airy_closure_sha256=thash(oldclosure),
        inherited_matrix_conversions=0,inherited_integral_rows=0,
        successful_stages_recomputed=0,all_other_cross_source_prefixes_rejected=True)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ("repo-root","manifest","out"):parser.add_argument("--"+name,type=Path,required=True)
    parser.add_argument("--resume",type=Path);a=parser.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("all new interval mathematics requires the actual public Actions repository")
    runtime=dict(python=".".join(map(str,sys.version_info[:3])),flint=flint.__version__,numpy=np.__version__)
    if runtime!=dict(python="3.12.14",flint="0.9.0",numpy="2.3.5"):raise ValueError("the exact runtime changed")
    if a.out.exists():raise FileExistsError("preserve every successful or failed actual native")
    ctx.prec=320;ctx.cap=4;start=time.monotonic()
    doc=dict(kind="actual_complete_inner_first_Airy_sources_from_accepted_Taylor_and_matrix_natives",
        complete=False,proved=False,failure=None,gates=[],stages={},matrix_conversions={},rows=[],
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=sha(__file__),input_manifest_sha256=sha(a.manifest),runtime=runtime,
        original_Taylor_native_sha256=TAYLOR,original_Taylor_process_sha256=TPROC,
        original_auxiliary_native_sha256=AUX,original_exact_fold_native_sha256=FOLD,
        original_exact_fold_process_sha256="67bf926abf9066d8f09dd8fbb16cd439770203b5e551c2fa374ef42f9abfc3b8",
        original_radial_reference_native_sha256=RADIAL,original_completed_norm_native_sha256=NORM,
        original_complete_directed_native_sha256=DIRECTED,original_complete_directed_process_sha256=DPROC,
        exact_real_delta_radius=str(DELTA),fixed_intrinsic_parameter="eta_0",
        input_cutoff=CUTOFF,physical_frequency="4|j|",actual_first_correction_density="n^(1/6)",
        source_window="H^-4/3 -> ordinary radial L2(H^-2/3 x H^-2/3)",
        old_target_FFT_coefficient_flow_fold_and_Taylor_stages_recomputed=0,
        old_complete_matrix_words_recomputed=0,new_stages=0,reused_stages=0,
        new_same_order_matrix_conversions=0,reused_same_order_matrix_conversions=0,
        new_source_integral_rows=0,reused_source_integral_rows=0,
        all_fourier_outputs_and_old_means_retained=True,
        exact_same_complex_parameter_opposite_branch_retained=True,
        fixed_inner_interval_introduces_no_artificial_source=True,
        original_physical_seams_retained=True,local_numerator_is_mu_L0_w1=True,
        old_density_T_alternative_claimed=False,leading_nonlocal_contribution_is_separate=True,
        positive_raw_source_only=True,positive_weighted_port_conversion_claimed=False,
        complete_strong_return_or_cutoff97_inverse_claimed=False,actual_PDE_branch_claimed=False)
    def check(name,truth):
        passed=bool(truth);doc["gates"].append(dict(name=name,passed=passed))
        if not passed:raise ValueError("inner first-correction source gate failed: "+name)
    def checkpoint():
        doc["seconds"]=time.monotonic()-start;save(a.out,doc)
    def stage(name,build):
        if name in doc["stages"]:
            saved=doc["stages"][name]
            if not saved["complete"] or payload_sha(saved["payload"])!=saved["payload_sha256"]:
                raise ValueError("an accepted complete stage changed its payload")
            doc["reused_stages"]+=1
            return saved["payload"]
        value=build();doc["stages"][name]=dict(complete=True,payload=value,payload_sha256=payload_sha(value))
        doc["new_stages"]+=1;checkpoint();return value
    try:
        manifest=read(a.manifest)
        check("the exact complete source manifest belongs to this one public repository",manifest["public_repository"]==PUBLIC)
        for f in manifest["files"]:
            p=a.repo_root/f["path"]
            if not p.is_file() or p.stat().st_size!=f["bytes"] or sha(p)!=f["sha256"]:
                raise ValueError("a pinned original input changed: "+f["path"])
        paths={k:a.repo_root/v for k,v in manifest["input_paths"].items()}
        pins=(("Taylor_native",TAYLOR,52843),("Taylor_process",TPROC,48844),
            ("auxiliary_native",AUX,20319),("auxiliary_process",APROC,46443),
            ("exact_fold_native",FOLD,3180936),("radial_reference_native",RADIAL,3434233),
            ("original_norm_native",NORM,4837715),("directed_native",DIRECTED,7873296),
            ("directed_process",DPROC,49990))
        check("all complete original mathematical natives and receipts retain their exact bytes",
            all(sha(paths[k])==s and paths[k].stat().st_size==n for k,s,n in pins))
        tay,tp,aux,ap,fold,radial,norm,directed,dp=[read(paths[k]) for k,_,_ in pins]
        check("the successful complete Taylor run retains all20 gates and the corrected principal coefficient",
            tay["complete"] and tay["proved"] and tay["failure"] is None
            and tay["source_sha256"]==TSOURCE and tay["input_manifest_sha256"]==TMANIFEST
            and tay["principal_mu_uses_B_plus_and_leading_a0_uses_B_minus"] is True
            and len(tay["gates"])==20 and all(g["passed"] for g in tay["gates"])
            and tp["actual_returncode"]==0 and tp["native_sha256"]==TAYLOR
            and tp["mathematical_source_sha256"]==TSOURCE and tp["manifest_sha256"]==TMANIFEST)
        check("the complete auxiliary and all old norm natives remain proved without failure",
            all(d["complete"] and d["proved"] and d["failure"] is None
                and d["gates"] and all(g["passed"] for g in d["gates"]) for d in (aux,fold,radial,norm))
            and ap["actual_returncode"]==0 and ap["native_sha256"]==AUX
            and aux["complete_smaller_case_payload_unchanged"] is True)
        check("the repaired full family fixed_eta and true root agree in the original physical piece",
            tay["background_definition_sha256"]==aux["background_definition_sha256"]==BASE
            and tay["explicit_direction_definition_sha256"]==aux["explicit_direction_definition_sha256"]==ZDEF
            and tay["actual_intrinsic_parameter"]==aux["actual_intrinsic_parameter"]=="eta_0"
            and Q(tay["exact_complex_delta_radius"])==Q(aux["exact_complex_delta_radius"])==DELTA
            and tay["exact_root_interval"]==aux["exact_root_interval"]==fold["exact_root_interval"]==radial["exact_root_interval"]
            and tay["exact_original_physical_piece_interval"]==aux["exact_original_piece_interval"])
        check("the exact original complete directed matrix native retains all eight actual public gates",
            directed["public_repository"]==PUBLIC and directed["complete"] and directed["proved"]
            and directed["failure"] is None and directed["source_sha256"]==DSOURCE
            and directed["input_manifest_sha256"]==DMANIFEST
            and directed["original_completed_norm_native_sha256"]==NORM
            and len(directed["gates"])==8 and all(g["passed"] for g in directed["gates"])
            and dp["actual_returncode"]==0 and str(dp["run_id"])=="43632464994"
            and dp["native_sha256"]==DIRECTED and dp["native_bytes"]==7873296
            and dp["mathematical_source_sha256"]==DSOURCE and dp["manifest_sha256"]==DMANIFEST
            and dp["mathematical_gates"]==directed["gates"])
        roots=list(map(Q,tay["exact_root_interval"]));R=INNER+roots[1]-roots[0]
        inner=[roots[0]-INNER,roots[1]+INNER];cell=list(map(Q,tay["exact_original_physical_piece_interval"]))
        domain=tay["old_product_domain"]
        check("the fixed complete inner physical interval and genuine Taylor domain are unchanged",
            list(map(Q,domain["exact_physical_interval"]))==inner
            and Q(domain["exact_physical_rho_cover_radius"])==R
            and Q(domain["exact_rho_radius"])==Q(1,6000)
            and Q(domain["exact_phi_width"])==Q(1,128)
            and cell[0]<inner[0]<inner[1]<cell[1])
        rows=radial["coefficient_rows"];nr=norm["coefficient_rows"];dr=directed["coefficient_rows"]
        check("all1328 original coefficient and matrix rows retain the complete original identities",
            len(rows)==len(nr)==1328 and payload_sha(rows)==fold["original_directed_table_sha256"]
            and all(row["common_row"]==i and nr[i]["common_row"]==i
                and row["interval"]==nr[i]["interval"]
                and row["original_root_row"]==nr[i]["original_root_row"] for i,row in enumerate(rows))
            and all(x["interval"][1]==y["interval"][0] for x,y in zip(rows,rows[1:])))
        check("all1328 original radial rows reproduce the complete directed identities and bounds exactly",
            len(dr)==len(rows)==1328
            and all(row==dict(common_row=i,interval=dr[i]["interval"],
                original_root_row=dr[i]["original_root_row"],original_completed_moment_row=i,
                original_completed_directed_row=i,bounds=dr[i]["bounds"])
                and dr[i]["common_row"]==i and dr[i]["original_completed_moment_row"]==i
                and isinstance(dr[i]["complete_width_evidence"],list)
                and len(dr[i]["complete_width_evidence"])==3 for i,row in enumerate(rows))
            and directed["exact_root_interval"]==fold["exact_root_interval"]
            and Q(directed["exact_real_delta_radius"])==DELTA)
        doc["original_complete_directed_table_sha256"]=payload_sha(dr)
        doc.update(exact_root_interval=list(map(str,roots)),exact_physical_inner_interval=list(map(str,inner)),
            exact_physical_rho_cover=str(R),exact_original_physical_piece_interval=list(map(str,cell)),
            original_directed_table_sha256=fold["original_directed_table_sha256"],
            original_all1328_row_identities_verified=True)
        if a.resume:
            prev=read(a.resume)
            keys=("public_repository","source_sha256","input_manifest_sha256","runtime",
                "original_Taylor_native_sha256","original_Taylor_process_sha256","original_auxiliary_native_sha256",
                "original_exact_fold_native_sha256","original_radial_reference_native_sha256",
                "original_completed_norm_native_sha256","original_complete_directed_native_sha256",
                "original_complete_directed_process_sha256","exact_physical_inner_interval","exact_root_interval")
            check("every accepted new prefix has the identical source runtime and all original inputs",
                all(prev.get(k)==doc.get(k) for k in keys))
            for k in ("stages","matrix_conversions","rows"):doc[k]=copy.deepcopy(prev[k])
            doc["original_prefix_audit"]=dict(native_sha256=sha(a.resume),native_bytes=a.resume.stat().st_size,
                complete=prev["complete"],proved=prev["proved"],failure=prev["failure"],
                accepted_stages=len(prev["stages"]),accepted_rows=len(prev["rows"]))
            if "specific_legacy_two_stage_reuse" in prev:
                doc["specific_legacy_two_stage_reuse"]=copy.deepcopy(prev["specific_legacy_two_stage_reuse"])
        else:
            exact_two_stage_schema_migration(a.repo_root,manifest,doc,check)
        checkpoint()
        profile=stage("new-inner-Airy-profile-and-exact-PQ-jets",lambda:inner_profile(aux["cases"][0],ex(R)))
        p=decode(profile["numeric"])
        tables={Q(x["exact_output_phi_width"]):x for x in tay["first_correction_derivative_budgets"]}
        check("both real and positive-strip complete Taylor tables retain separate sup and Wiener values",
            Q(0) in tables and SIGMA in tables
            and all(x["amplitude_Wiener_and_sup_spaces_separately_labelled"] for x in tables.values())
            and tay["complete_branch_identity"]["same_complex_delta_without_conjugation"] is True)
        def all_airy():
            real=amplitude_jets(tables[Q(0)],p["c"],p["PQ"])
            analytic=amplitude_jets(tables[SIGMA],p["c"],p["PQ"])
            local=decode(tables[SIGMA]["unnormalized_local_operator_sup_bounds"])
            localvec=[up(local["first"]),up(local["second"])]
            answer={}
            for side in ("negative","positive"):
                answer[side]={k:Airy_bound(real[k],analytic[k][0],p,side) for k in real}
                answer[side]["local_numerator"]=Airy_bound(None,localvec,p,side)
            return dict(Airy_bounds=answer,complete_real_amplitude_jets=encode(real),
                complete_analytic_amplitude_jets=encode(analytic),
                unnormalized_local_numerator=encode(localvec),
                exact_analytic_width=str(SIGMA),real_derivative_tables_not_used_as_strip_bounds=True)
        amplitude=stage("all-inner-amplitudes-and-complete-Airy-operators",all_airy)
        doc["complete_Airy_source_bounds"]=copy.deepcopy(amplitude["Airy_bounds"])
        selected=[]
        for row in rows:
            lo,hi=map(Q,row["interval"]);left=max(lo,inner[0]);right=min(hi,inner[1])
            if not left<right:continue
            edges=sorted({left,right,*[z for z in roots if left<z<right]})
            selected.extend((row["common_row"],u,v) for u,v in zip(edges,edges[1:]))
        check("new partial integrals cover exactly the fixed inner interval in original row order",
            selected and selected[0][1]==inner[0] and selected[-1][2]==inner[1]
            and all(x[2]==y[1] for x,y in zip(selected,selected[1:])))
        prefix=len(doc["rows"])
        if prefix>len(selected):raise ValueError("an accepted prefix exceeds the exact inner cover")
        for si,(idx,left,right) in enumerate(selected):
            key=str(idx);row=rows[idx];matrix_row=dr[idx]
            if key in doc["matrix_conversions"]:
                cv=doc["matrix_conversions"][key]
                if cv["original_coefficient_row_payload_sha256"]!=payload_sha(matrix_row):
                    raise ValueError("an accepted complete matrix conversion changed its original row")
                doc["reused_same_order_matrix_conversions"]+=1
            else:
                cv=matrix_conversion(matrix_row);doc["matrix_conversions"][key]=cv
                doc["new_same_order_matrix_conversions"]+=1;checkpoint()
            if si<prefix:
                item=doc["rows"][si]
                if item["common_row"]!=idx or item["interval"]!=list(map(str,(left,right))):
                    raise ValueError("an accepted integral row moved its actual radial interval")
                doc["reused_source_integral_rows"]+=1;continue
            c=decode(nr[idx]["bounds"]);z=decode(cv["costs"])
            item=dict(common_row=idx,original_root_row=row["original_root_row"],
                interval=list(map(str,(left,right))),original_whole_row_interval=row["interval"],
                original_moment_row_payload_sha256=payload_sha(nr[idx]))
            doc["last_attempted_source_row"]=dict(common_row=idx,interval=item["interval"])
            for side in ("negative","positive"):
                weight=radial_weight(left,right,roots,side)
                if not weight>0:
                    item[side]=dict(exact_zero_radial_part=True,squared_source_integral=record(arb(0)))
                    continue
                out=row_constants(c,z,amplitude["Airy_bounds"][side])
                out["radial_weight_integral"]=record(weight)
                out["squared_source_integral"]=record((weight*up(box(out["complete_squared_vector_envelope"]))).upper())
                out["separate_squared_source_integrals"]={
                    k:record((weight*ipow(up(box(out[k])),2)).upper())
                    for k in ("first_nonlocal_singular_envelope","first_local_singular_envelope","independent_even_mean_singular_envelope")}
                item[side]=out
            doc["rows"].append(item);doc["new_source_integral_rows"]+=1
            doc.pop("last_attempted_source_row",None);checkpoint()
        check("every fixed inner subinterval has complete nine-term nonlocal local and independent_mean bounds",
            len(doc["rows"])==len(selected)
            and all(set(item[side]["complete_nine_nonlocal_terms"])==set(TERM_NAMES)
                and len(item[side]["complete_five_even_mean_terms"])==5
                for item in doc["rows"] for side in ("negative","positive")
                if not item[side].get("exact_zero_radial_part")))
        totals={}
        for side in ("negative","positive"):
            value=sum((up(box(row[side]["squared_source_integral"])) for row in doc["rows"]),arb(0)).upper()
            separate={}
            for key in ("first_nonlocal_singular_envelope","first_local_singular_envelope","independent_even_mean_singular_envelope"):
                separate[key]=record(sum((up(box(row[side]["separate_squared_source_integrals"][key]))
                    for row in doc["rows"] if not row[side].get("exact_zero_radial_part")),arb(0)).sqrt().upper())
            totals[side]=dict(complete_first_correction_ordinary_L2_source=record(value.sqrt().upper()),
                separate_component_L2_bounds=separate,complete_squared_source_integral=record(value))
        doc["complete_inner_source_totals"]=totals
        doc["complete_inner_integral_rows"]=len(selected)
        doc["complete_same_order_converted_rows"]=len(doc["matrix_conversions"])
        check("all original no-recomputation and full-source scope limits are retained",
            doc["old_target_FFT_coefficient_flow_fold_and_Taylor_stages_recomputed"]==0
            and doc["old_complete_matrix_words_recomputed"]==0
            and not doc["complete_strong_return_or_cutoff97_inverse_claimed"]
            and not doc["positive_weighted_port_conversion_claimed"])
        doc["complete"]=True;doc["proved"]=True
    except BaseException as error:
        doc["failure"]=dict(type=type(error).__name__,message=str(error));raise
    finally:
        checkpoint()
        print(json.dumps(dict(complete=doc["complete"],proved=doc["proved"],failure=doc["failure"],
            new_stages=doc["new_stages"],new_source_integral_rows=doc["new_source_integral_rows"],
            native_sha256=sha(a.out),seconds=doc["seconds"]),allow_nan=False),flush=True)
if __name__=="__main__":main()
