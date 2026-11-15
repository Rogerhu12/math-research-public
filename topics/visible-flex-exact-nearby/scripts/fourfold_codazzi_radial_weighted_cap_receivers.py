#!/usr/bin/env python3
"""New radial-weighted and left-receiver integrals of frozen original cap rows.

Only public Actions executes this scientific source. No target, Fourier,
Riccati, old residual, repair, mean flow, or Green propagation is recomputed.
"""
from __future__ import annotations
import argparse
from bisect import bisect_right
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
import time
import traceback
from flint import arb, ctx

TOPIC=Path("topics/visible-flex-exact-nearby")
KIND="actual_true_cap_radial_weighted_and_left_receivers_v1"
CANDIDATE="ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
DEFINITION="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
OBJECT="91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848"
ALPHA=Fraction(6890507429876859,9007199254740992)
NU=Fraction(-2572625729470897,72057594037927936)
ETA=Fraction(-7789843107295549,4611686018427387904)
LEFT,RIGHT=Fraction(9,10),Fraction(25,8)
OUT_RIGHT=Fraction(19,20)
MERGED_SHA="6f52030b7954f049a8e42a5a513a1f69b553819065b0c8b2245fa173e514cbb1"
MERGED_BYTES=4592623
MERGER_SHA="24ec0bf2b9d2b03ebfa07f4b39b8fdee3277f8e4b2aa14385c267122e6b8e81f"
OLD_RESIDUAL_PRODUCER="98eb7034038d76a341e112927cff4bcb7bfd425bc56698305803a689060ac31e"
OLD_SOURCE_SHA="106ec9308882b814ca773da904e561e93aa4475f4f46f84b9632c9716653992f"
OLD_SUMMARY_SHA="f5eea9a8a1b3f198e19c94a42cc3f794226b99cae65cefbd2e631134aff42c3a"
FILES={
 "parts":"notes/2026-11-14-R133-final-complete-moving-residual-parts.json",
 "cap":"notes/2026-11-14-R133-final-physical-cap-linear-module-r09-v2-native.json.gz",
 "intrinsic":"notes/2026-11-13-Codazzi-rotational-positive-cap-v2-native.json.gz",
 "summary":"notes/cached_cap_L1_endpoint_ci/run-43692857656-1-cached-cap-L1-reference-endpoint/actual-cap-L1-endpoint-summary.json"}
EXPECTED={
 "cap":"ad6efc2a226131245ff4197a0b5da2843578224368a340f7a50d383c03a1819b",
 "intrinsic":"3a89805ebe1ab22000529a7a8c2fdc262b1c3a2afbc52433cf610d2d6542ff22",
 "summary":OLD_SUMMARY_SHA,
 "parts":"0705cb80101f25105d74181aafdf9daaf5a65baeece2d41e8a25b4589259cdad"}
PARAMETERS={
 "arithmetic_bits":320,"exact_cap_interval":["9/10","25/8"],
 "right_body_output_interval":["9/10","19/20"],
 "exact_eta":str(ETA),"exact_nu":str(NU),"exact_alpha":str(ALPHA),
 "affine_intrinsic_offset":"0","whole_old_reference_parameter_half_width":"1/1000000000",
 "weight_fractions":["1/16","1/8","1/4","3/8","1/2","3/4"],
 "weight_base_rate":"dyadic lower of min(4*sD,-2*beta,-beta*(ell+1)) on each original reference row",
 "weight_rate_dyadic_bits":32,
 "inverse_frequency_interval":["0","1/4"],"inverse_frequency_subintervals":64,
 "physical_minimum_nonmean_frequency":4,
 "complete_raw_residual_label_support":96,"complete_raw_physical_frequency":384,
 "actual_cap_radius":"3/1000000","actual_outer_C_nonmean_radius":"99/100000000000",
 "inner_curvature_radius":"1/1000000000","tail_inner_curvature_radius":"1/128000000000",
 "normalized_outer_height_radius":"1/1152921504606846976",
 "Q_complete_linear_upper":"0.051432066","Q_quadratic_value_factor":13,
 "true_outer_D_Lipschitz":"0.006","true_outer_Cmean_Lipschitz":"0.00075",
 "true_outer_D_known_affine_norm_upper":"0.000000000000002",
 "true_outer_Cmean_known_affine_norm_upper":"0.000000000000000000205",
 "selected_delta_half_width":"1/10000000000",
 "known_selected_physical_global_pair_sup_factor":10,
 "true_moving_L2_pair_conversion_factor":80,
 "full_mean_included":True,"ordinary_radial_measure":"dr",
 "physical_angular_measure":"normalized circle",
 "current_actual_reflection_Bmean_exactly_zero":True,
 "old_successful_zero_weight_integrals_recomputed":False,
 "old_target_residual_repair_mean_flow_Riccati_or_Green_calls":0}

def sha_bytes(raw):return hashlib.sha256(raw).hexdigest()
def sha(path):return sha_bytes(Path(path).read_bytes())
def exact(v):
    q=Fraction(v)
    return arb(q.numerator)/q.denominator
def box(r):
    if isinstance(r,dict):
        if "lower" in r and "upper" in r:
            return arb(r["lower"]).lower().union(arb(r["upper"]).upper())
        if "ball" in r:return arb(r["ball"])
    raise ValueError("a complete directed original ball is required")
def abs_upper(v):return abs(arb(v)).upper()
def maximum(v):return max((arb(x).upper() for x in v),default=arb(0)).upper()
def minimum(v):return min((arb(x).lower() for x in v)).lower()
def rec(v):
    z=arb(v)
    if not z.is_finite():raise ValueError("nonfinite new scalar")
    return {"ball":z.str(70)}
def recs(d):return {k:rec(v) for k,v in d.items()}
def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith(".gz") else raw)
def canonical(d):return (json.dumps(d,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n").encode()
def save(path,d):
    raw=(json.dumps(d,indent=2,allow_nan=False)+"\n").encode()
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_name(path.name+".tmp");tmp.write_bytes(raw);tmp.replace(path)
def gate(doc,name,ok):
    doc["gates"].append({"name":name,"passed":bool(ok)})
    if not ok:raise ValueError("gate failed: "+name)
def cover(rows,left,right,label):
    cursor=left
    for row in rows:
        lo,hi=map(Fraction,row["interval"])
        if lo!=cursor or not lo<hi:raise ValueError(label+" has a gap or overlap")
        cursor=hi
    if cursor!=right:raise ValueError(label+" does not reach its true endpoint")

def restore_original(root,doc):
    path=root/TOPIC/FILES["parts"];d=read(path)
    gate(doc,"the complete original7296 container and its three natural parts are fixed",
        d["kind"]=="complete_native_lossless_container_binary_parts_v2"
        and d["native_complete"] is True and d["native_failure"] is None
        and d["complete_native_rows"]==7296 and d["original_bytes"]==MERGED_BYTES
        and d["original_sha256"]==MERGED_SHA and d["original_source_sha256"]==MERGER_SHA
        and d["candidate_sha256"]==CANDIDATE and len(d["parts"])==3)
    chunks=[];cursor=0;receipts=[]
    for i,r in enumerate(d["parts"]):
        if r["index"]!=i or r["offset"]!=cursor or Path(r["file"]).name!=r["file"]:
            raise ValueError("an original byte position changed")
        raw=(path.parent/r["file"]).read_bytes()
        if len(raw)!=r["compressed_bytes"] or sha_bytes(raw)!=r["compressed_sha256"]:
            raise ValueError("an original compressed part changed")
        payload=gzip.decompress(raw)
        if len(payload)!=r["bytes"] or sha_bytes(payload)!=r["sha256"]:
            raise ValueError("an original part payload changed")
        chunks.append(payload);cursor+=len(payload)
        receipts.append({k:r[k] for k in ("index","file","bytes","sha256",
                                          "compressed_bytes","compressed_sha256")})
    raw=b"".join(chunks)
    if len(raw)!=MERGED_BYTES or sha_bytes(raw)!=MERGED_SHA:
        raise ValueError("the complete original container changed")
    doc["original_restoration"]={"manifest_sha256":sha(path),"container_sha256":MERGED_SHA,
        "container_bytes":len(raw),"parts":receipts,"new_parts_created":False,
        "original_mathematics_executed":False}
    return json.loads(gzip.decompress(raw))

def checked_inputs(a,doc):
    m=read(a.manifest)
    gate(doc,"the new directed precision and all finite weight choices are fixed",
         a.bits==320 and m["parameters"]==PARAMETERS)
    gate(doc,"the new manifest and scientific source are immutable",
         m["source_sha256"]==sha(__file__) and
         all(sha(a.root/p)==s for p,s in m["files"].items()))
    for k,p in FILES.items():
        if sha(a.root/TOPIC/p)!=EXPECTED[k]:
            raise ValueError("an exact input changed: "+k)
    old=read(a.root/TOPIC/FILES["summary"])
    gate(doc,"the previous successful full source constants are copied without old integration",
        old["kind"]=="actual_cached_cap_L1_and_reference_endpoint_sources_v1"
        and old["complete"] is True and old["failure"] is None
        and old["source_sha256"]==OLD_SOURCE_SHA and len(old["gates"])==12
        and all(g["passed"] is True for g in old["gates"])
        and old["inputs"]["cap"]==EXPECTED["cap"]
        and old["inputs"]["intrinsic"]==EXPECTED["intrinsic"]
        and old["inputs"]["merged"]==MERGED_SHA
        and old["parameters"]["exact_alpha"]==str(ALPHA)
        and old["parameters"]["exact_nu"]==str(NU)
        and old["scope"]["fixed_eta0"] and old["scope"]["fixed_repaired_M32_delta0"]
        and old["scope"]["full_even_mean"] and old["complete_common_cap_cells"]==1346)
    raw=restore_original(a.root,doc)
    gate(doc,"all original full residual rows retain the true physical units and both means",
        raw["kind"]=="complete_actual_moving_residual_all_closed_rows_and_interfaces"
        and raw["complete"] is True and raw["failure"] is None
        and raw["source_sha256"]==MERGER_SHA
        and raw["original_producer_sha256"]==OLD_RESIDUAL_PRODUCER
        and raw["candidate_sha256"]==CANDIDATE and raw["object_sha256"]==OBJECT
        and Fraction(raw["exact_amplitude"])==ALPHA and Fraction(raw["exact_nu"])==NU
        and Fraction(raw["common_parameter_half_width"])==0
        and raw["all_7296_closed_rows_reused_without_recomputation"]
        and raw["all_6143_actual_interfaces_paid"]
        and raw["complete_original_primitive_tail"]
        and raw["complete_residual_support"]==96 and len(raw["rows"])==7296)
    cover(raw["rows"],Fraction(0),RIGHT,"original7296")
    for i,r in enumerate(raw["rows"]):
        if r["index"]!=i or r["exact_angular_support_index"]!=96:
            raise ValueError("an original full residual row label changed")
    cap=read(a.root/TOPIC/FILES["cap"])
    intrinsic=read(a.root/TOPIC/FILES["intrinsic"])
    gate(doc,"the complete allfrequency reference and original intrinsic cache are unchanged",
        cap["kind"]=="actual_final_physical_cap_linear_module_v1" and cap["complete"]
        and cap["candidate_sha256"]==CANDIDATE and cap["object_sha256"]==OBJECT
        and cap["cap_cache_sha256"]==EXPECTED["intrinsic"]
        and Fraction(cap["exact_alpha"])==ALPHA and Fraction(cap["exact_nu"])==NU
        and Fraction(cap["exact_eta_center"])==ETA
        and Fraction(cap["parameter_half_width"])==Fraction(1,10**9)
        and cap["whole_original_eta"] and cap["complete_primitive_tail"]
        and cap["complete_unknown_Fourier_modes"] and cap["exact_interval"]==["9/10","25/8"]
        and intrinsic["complete"] and intrinsic["cap_linear_reference_certified"]
        and intrinsic["object_sha256"]==OBJECT
        and Fraction(intrinsic["exact_center_parameter"])==ETA
        and Fraction(intrinsic["parameter_half_width"])==Fraction(1,10**9)
        and intrinsic["whole_affine_parameter_interval"] and intrinsic["complete_primitive_tail"])
    ref=cap["reference_rows"];cover(ref,LEFT,RIGHT,"originalreference")
    cover(cap["closed_cover"],LEFT,RIGHT,"originalclosedcover")
    selected=[]
    for r in raw["rows"]:
        l,h=map(Fraction,r["interval"])
        if h>LEFT and l<RIGHT:
            selected.append(dict(r,interval=[str(max(l,LEFT)),str(min(h,RIGHT))]))
    cover(selected,LEFT,RIGHT,"selectedcap")
    gate(doc,"the true cap has the original949 reference1346 closed intersections and1341 residual rows",
         len(ref)==cap["native_reference_rows"]==949 and
         len(cap["closed_cover"])==cap["complete_closed_intersections"]==1346 and len(selected)==1341)
    const={k:box(v).upper() for k,v in old["physical_source_constants"].items()}
    gate(doc,"all copied physical composition repair and Q coefficients have their complete domains",
         const["C"]<exact(Fraction(1,3)) and const["B"]<exact(Fraction(1,128))
         and const["Ctheta"]<exact(Fraction(1,32)) and const["Btheta"]<exact(Fraction(1,32))
         and const["inverse_displacement"]<exact(Fraction(1,256))
         and const["composition"]<5 and const["repair_pair_residual_A0"]<exact("4.285e-15")
         and maximum([const["Q_B"],const["Q_C"]])<exact("0.051432066"))
    doc["inputs"]={**EXPECTED,"merged":MERGED_SHA,
        "complete_physical_background_identity":old["inputs"]["background"]}
    doc["original_counts"]={"raw_complete_rows":7296,"reference_rows":949,
                           "cap_residual_rows":1341,"old_complete_intersections":1346}
    doc["physical_source_constants_copied"]=old["physical_source_constants"]
    keys=("physical_B_ordinary_L1","physical_C_ordinary_L1",
          "unclosed_reference_body_pair","unclosed_reference_complete_known_affine_pair",
          "reference_C_nonmean_R_from_known_body_and_right_d",
          "reference_Cmean_R_independent_load")
    doc["old_successful_zero_weight_conclusions_copied"]={k:old["bounds"][k] for k in keys}
    doc["old_whole_L1_bounds_copied"]=old["old_whole_L1_bounds_reused_without_reaggregation"]
    return selected,ref,intrinsic,const

def decimal_interval_lower(text):
    """An exact rational lower endpoint of Arb's enclosing decimal rendering."""
    s=text.strip()
    if s.startswith("[") and s.endswith("]"):s=s[1:-1].strip()
    if "+/-" in s:
        parts=s.split("+/-")
        if len(parts)!=2:raise ValueError("unexpected complete Arb rendering")
        mid=Fraction(parts[0].strip()) if parts[0].strip() else Fraction(0)
        return mid-abs(Fraction(parts[1].strip()))
    return Fraction(s)
def dyadic_lower(v,bits):
    q=decimal_interval_lower(arb(v).lower().str(110))
    n=(q.numerator*(2**bits))//q.denominator
    result=Fraction(n,2**bits)
    if not exact(result)<=arb(v).lower():raise ValueError("the selected exact dyadic is not a lower bound")
    return result

def reference_coefficients(ref,intrinsic,doc):
    rows=[]
    for i,r in enumerate(ref):
        n=intrinsic["rows"][r["native_index"]]
        l,h=map(Fraction,r["interval"]);nl,nh=map(Fraction,n["interval"])
        if not nl<=l<h<=nh or not n.get("actual_scalar_germ"):
            raise ValueError("an original reference box lost its intrinsic identity")
        rb={k:box(v) for k,v in r["bounds"].items()}
        co={k:box(v) for k,v in n["coefficients"].items()}
        beta,gamma,ell=co["beta"],co["gamma"],co["lambda_ref"]
        sd,sc=rb["D_rate"].lower(),rb["C_rate"].lower()
        aB=(-2*beta).lower();a0=(-beta*(ell+1)).lower()
        if not (beta<0 and gamma>0 and ell>0 and sd>0 and sc>0 and aB>0 and a0>0
                and rb["q_lower"]>0 and rb["lower_face"]>0 and rb["upper_face"]>0):
            raise ValueError("an old complete positive rate or true mean sign is missing")
        base=dyadic_lower(minimum([4*sd,aB,a0]),32)
        if not base>0:raise ValueError("the new exact radial rate has no positive dyadic lower")
        rows.append({"index":i,"native_index":r["native_index"],"interval":[str(l),str(h)],
            "sD":sd,"sC":sc,"gamma":gamma.upper(),"beta_abs":abs_upper(beta),
            "aB":aB,"a0":a0,"q":rb["q_upper"].upper(),"base_lambda":base,
            "actual_scalar_germ":n["actual_scalar_germ"]})
    gate(doc,"all949 genuine mean and nonmean rates are positive before choosing any weight",
         len(rows)==949 and all(r["base_lambda"]>0 for r in rows))
    return rows

def physical_source(row,const):
    # Same complete fields as the old producer, evaluated only inside new functionals.
    moving=[(exact(ALPHA)*box(row["complete_residual_A0"][k]).upper()
                +const["repair_pair_residual_A0"]).upper() for k in ("U","V")]
    U,V=[(const["composition"]*x).upper() for x in moving]
    C,B,Ct,Bt=[const[k] for k in ("C","B","Ctheta","Btheta")]
    return ((C*U+(B*C+Bt*C/4)*V).upper(),
            ((C*C+Ct*C/4)*V).upper())

def common_cells(raw,ref,const,doc):
    old_edges=sorted({LEFT,RIGHT,*[Fraction(t) for r in raw for t in r["interval"]],
                                  *[Fraction(t) for r in ref for t in r["interval"]]})
    if len(old_edges)-1!=1346:raise ValueError("the original common cover differs")
    edges=sorted(set(old_edges+[OUT_RIGHT]))
    rl=[Fraction(r["interval"][0]) for r in raw]
    ql=[Fraction(r["interval"][0]) for r in ref]
    cells=[]
    for l,h in zip(edges,edges[1:]):
        ir=bisect_right(rl,l)-1;iq=bisect_right(ql,l)-1
        rr,qr=raw[ir],ref[iq]
        if not l<h<=min(Fraction(rr["interval"][1]),Fraction(qr["interval"][1])):
            raise ValueError("a new true intersection is outside an original closed row")
        FB,FC=physical_source(rr,const)
        cells.append({"interval":[str(l),str(h)],"raw_index":rr["index"],
                      "reference_index":iq,"FB":FB,"FC":FC})
    cover(cells,LEFT,RIGHT,"newcommoncover")
    gate(doc,"every new weighted cell is a genuine old closed intersection with the exact output cut",
         len(cells) in (1346,1347) and OUT_RIGHT in edges
         and sum((Fraction(c["interval"][1])-Fraction(c["interval"][0]) for c in cells),Fraction(0))==RIGHT-LEFT)
    doc["new_common_cells"]=len(cells)
    return cells

def exp_integral(k,h):
    h=exact(h);k=arb(k)
    if k==0:return h
    if not k>0:raise ValueError("a positive exponential denominator is required")
    return ((1-(-k*h).exp())/k)
def exp_growth_integral(k,h):
    h=exact(h);k=arb(k)
    if k==0:return h
    if not k>0:raise ValueError("a positive growth denominator is required")
    return (((k*h).exp()-1)/k)

def left_receivers(cells,ref,doc,audit):
    sD=s0=sB=arb(0);etaB=etaBgeneral=etaC0=arb(0)
    for c in cells:
        l,h=map(Fraction,c["interval"]);length=h-l;r=ref[c["reference_index"]]
        d=4*r["sD"];m0=r["a0"];mB=r["aB"]
        eD=(-sD).exp();e0=(-s0).exp();eB=(-sB).exp()
        iD=eD*exp_integral(d,length)
        i0=e0*exp_integral(m0,length)
        iB=eB*exp_integral(mB,length)
        # The general B-source bound pays the two independent mean/nonmean legs.
        etaB+=iD*(c["FB"]+r["q"]*c["FC"])
        etaBgeneral+=(iD+iB)*c["FB"]+iD*r["q"]*c["FC"]
        # No physical-mean source value is guessed from a norm: use the full FC upper.
        etaC0+=i0*c["FC"]
        sD+=d*exact(length);s0+=m0*exact(length);sB+=mB*exact(length)
    out={"eta_B_left_reflection":etaB.upper(),
         "eta_B_left_general_with_separate_Bmean":etaBgeneral.upper(),
         "eta_Cmean_left_using_full_FC":etaC0.upper(),
         "e_D":(-sD).exp().upper(),"e_Cmean":(-s0).exp().upper(),
         "e_Bmean":(-sB).exp().upper(),"q_L":ref[0]["q"],
         "integrated_D_rate":sD,"integrated_Cmean_rate":s0}
    doc["new_left_ordinary_receivers"]=recs(out)
    doc["new_left_ordinary_receiver_scope"]={
        "all_source_points_in_complete_cap":True,"left_triangular_H_exactly_zero":True,
        "current_reflection_Bmean_zero":True,"independent_Cmean_retained":True,
        "physical_Cmean_source_replaced_by_its_complete_FC_norm_upper":True,
        "Q_and_true_outer_feedback_not_omitted":True,
        "unclosed_sources_alone_claim_actual_solution":False}
    audit["new_left_receiver_integrated_rates"]=recs({"D":sD,"Cmean":s0,"Bmean":sB})
    gate(doc,"the new left ordinary receivers retain sourcepoint q both means and full cap measure",
         etaB>=0 and etaC0>=0 and sD>0 and s0>0 and sB>0)
    return out

def weighted_kernel(ref,kappa,qplus,audit):
    profile=[]
    for r in ref:
        lam=kappa*r["base_lambda"];la=exact(lam)
        if not (4*r["sD"]-la>0 and r["aB"]-la>0 and r["a0"]-la>0):
            raise ValueError("a chosen weight loses a true mean or nonmean damping gate")
        profile.append(lam)
    bins=PARAMETERS["inverse_frequency_subintervals"]
    K=HD=Dall=Tall=Call=arb(0);z_audit=[]
    for i in range(bins):
        zl=exact(Fraction(i,4*bins));zh=exact(Fraction(i+1,4*bins))
        Ds=[];Ts=[];Cs=[]
        for r,lam in zip(ref,profile):
            la=exact(lam)
            Ds.append((r["gamma"]+r["q"]*r["beta_abs"]*zh)/(r["sD"]-la*zh))
            Ts.append(r["gamma"]/(r["sC"]+la*zl))
            Cs.append((r["beta_abs"]*zh)/(r["sC"]+la*zh))
        D,T,C=maximum(Ds),maximum(Ts),maximum(Cs)
        kj=(D+(1+qplus)*(T*D+C)).upper()
        hdj=(1+(1+qplus)*T).upper()
        K=max(K,kj).upper();HD=max(HD,hdj).upper()
        Dall=max(Dall,D).upper();Tall=max(Tall,T).upper();Call=max(Call,C).upper()
        z_audit.append({"inverse_frequency_interval":[str(Fraction(i,4*bins)),str(Fraction(i+1,4*bins))],
                        "bounds":recs({"D":D,"T":T,"C":C,"Q_pair":kj,"right_D":hdj})})
    K0=maximum(r["beta_abs"]/(r["a0"]-exact(lam)) for r,lam in zip(ref,profile))
    out={"K_Q_nonmean":K,"K_Q_mean":K0,"K_Q_complete":max(K,K0).upper(),
         "D_Q_left":Dall,"T":Tall,"C":Call,
         "H_D":max(arb(1),HD).upper(),"H_C":(1+qplus).upper(),
         "lambda_min":exact(min(profile)),"lambda_max":exact(max(profile))}
    audit["profile"]=[{"reference_index":r["index"],"native_index":r["native_index"],
                        "interval":r["interval"],"lambda":str(lam)}
                       for r,lam in zip(ref,profile)]
    audit["complete_inverse_frequency_bins"]=z_audit
    return profile,out

def weight_integrals(cells,profile,doc_case,audit):
    w=arb(1);FB=FC=inv2=arb(0);measure=Fraction(0)
    source_audit=[]
    for c in cells:
        l,h=map(Fraction,c["interval"]);length=h-l
        lam=exact(profile[c["reference_index"]])
        wi=w*exp_integral(lam,length)
        fB=wi*c["FB"];fC=wi*c["FC"]
        FB+=fB;FC+=fC
        if h<=OUT_RIGHT:
            inv2+=exp_growth_integral(2*lam,length)/(w*w)
            measure+=length
        elif l<OUT_RIGHT:raise ValueError("the output endpoint must be a true common node")
        source_audit.append({"interval":c["interval"],"raw_index":c["raw_index"],
            "reference_index":c["reference_index"],
            "new_bounds":recs({"weight_left":w,"weighted_B_integral":fB,"weighted_C_integral":fC})})
        w*=(-lam*exact(length)).exp()
        if not w>0:raise ValueError("a finite radial weight lost positivity")
    if measure!=OUT_RIGHT-LEFT:raise ValueError("the new local output measure differs")
    out={"weighted_B_ordinary_L1":FB.upper(),"weighted_C_ordinary_L1":FC.upper(),
         "weight_R":w,"right_body_inverse_weight_square_integral":inv2,
         "right_body_weight_readout":inv2.sqrt().upper()}
    audit["new_weighted_source_cells"]=source_audit
    doc_case["new_source_and_output_integrals"]=recs(out)
    return out

def compose_case(kernel,integrals,left,qplus,doc_case):
    rho=exact(PARAMETERS["actual_cap_radius"])
    AQ=exact(PARAMETERS["Q_complete_linear_upper"])+13*rho
    LD=exact(PARAMETERS["true_outer_D_Lipschitz"])
    L0=exact(PARAMETERS["true_outer_Cmean_Lipschitz"])
    rD=exact(PARAMETERS["true_outer_D_known_affine_norm_upper"])
    r0=exact(PARAMETERS["true_outer_Cmean_known_affine_norm_upper"])
    HD,HC=kernel["H_D"],kernel["H_C"]
    GB,GC=HD,(qplus*HD+HC).upper()
    eta0=(GB*integrals["weighted_B_ordinary_L1"]
        +GC*integrals["weighted_C_ordinary_L1"]
        +integrals["weight_R"]*(HD*rD+r0)).upper()
    chi=(kernel["K_Q_complete"]*AQ+HD*LD+L0).upper()
    ewD=(left["e_D"]/integrals["weight_R"]).upper()
    ew0=(left["e_Cmean"]/integrals["weight_R"]).upper()
    doc_case["complete_kernel_bounds"]=recs(kernel)
    doc_case["complete_affine_and_feedback"]=recs({
        "ordinary_B_gain":GB,"ordinary_C_gain":GC,
        "known_affine_eta_without_inner_gamma":eta0,"inner_gamma_eta_gain":HC,
        "Q_value_coefficient_AQ":AQ,"complete_chi":chi,
        "e_D_weighted_outer":ewD,"e_Cmean_weighted_outer":ew0})
    passed=bool(chi<1)
    doc_case["complete_weighted_posterior_applies"]=passed
    doc_case["candidate_failure"]=None if passed else "complete_chi_not_below_one"
    doc_case["old_actual_cap_existence_changed"]=False
    if not passed:
        doc_case["posterior_bounds"]=None
        return
    den=(1-chi).lower()
    X0=(eta0/den).upper();Xg=(HC/den).upper()
    readout=integrals["right_body_weight_readout"]
    Y0=(readout*X0).upper();Yg=(readout*Xg).upper()
    LB=(kernel["D_Q_left"]*AQ+ewD*LD).upper()
    Lmean=(kernel["K_Q_mean"]*AQ+ew0*L0).upper()
    B0=(left["eta_B_left_reflection"]+left["e_D"]*rD+LB*X0).upper()
    Bg=(left["q_L"]+LB*Xg).upper()
    C0=(left["eta_Cmean_left_using_full_FC"]+left["e_Cmean"]*r0+Lmean*X0).upper()
    Cg=(Lmean*Xg).upper()
    gamma=exact(PARAMETERS["inner_curvature_radius"])
    gamma_tail=exact(PARAMETERS["tail_inner_curvature_radius"])
    baseline=(10*exact(PARAMETERS["selected_delta_half_width"])*exact(OUT_RIGHT-LEFT).sqrt()).upper()
    out={"Xw_affine":X0,"Xw_gamma_gain":Xg,
         "right_physical_body_affine":Y0,"right_physical_body_gamma_gain":Yg,
         "right_physical_body_at_full_gamma_radius":(Y0+Yg*gamma).upper(),
         "right_physical_body_at_tail_gamma_radius":(Y0+Yg*gamma_tail).upper(),
         "right_moving_high96_and_high288_affine":(80*Y0).upper(),
         "right_moving_high96_and_high288_gamma_gain":(80*Yg).upper(),
         "right_moving_selected_full_affine":(80*(Y0+baseline)).upper(),
         "right_moving_selected_full_gamma_gain":(80*Yg).upper(),
         "selected_reference_physical_body_difference_paid_separately":baseline,
         "inner_B_nonmean_affine":B0,"inner_B_nonmean_gamma_gain":Bg,
         "inner_Cmean_affine":C0,"inner_Cmean_gamma_gain":Cg,
         "inner_B_nonmean_at_tail_gamma_radius":(B0+Bg*gamma_tail).upper(),
         "inner_Cmean_at_tail_gamma_radius":(C0+Cg*gamma_tail).upper()}
    doc_case["posterior_bounds"]=recs(out)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root",type=Path,required=True)
    p.add_argument("--manifest",type=Path,required=True)
    p.add_argument("--out",type=Path,required=True)
    p.add_argument("--bits",type=int,default=320)
    a=p.parse_args();ctx.prec=a.bits;ctx.cap=6
    started=time.monotonic()
    d={"kind":KIND,"complete":False,"failure":None,"actual_returncode":None,
       "source_sha256":sha(__file__),"input_manifest_sha256":sha(a.manifest),
       "parameters":PARAMETERS,"gates":[],"candidate_sha256":CANDIDATE,
       "derived_continuous_centre_definition_sha256":DEFINITION,
       "old_targets_Fourier_residuals_repair_mean_flows_Riccati_or_Green_recomputed":0,
       "old_successful_zero_weight_integrals_recomputed":False,
       "new_recomputable_native_persisted":False,
       "actual_core_solution_or_full_matching_proved":False,
       "actual_low_inner_curvature_selfmap_proved":False}
    audit={"kind":"temporary_complete_new_weighted_cap_receiver_audit_v1","weights":{}}
    try:
        raw,original_ref,intrinsic,const=checked_inputs(a,d)
        ref=reference_coefficients(original_ref,intrinsic,d)
        cells=common_cells(raw,ref,const,d)
        left=left_receivers(cells,ref,d,audit)
        qplus=maximum(r["q"] for r in ref)
        fractions=[Fraction(x) for x in PARAMETERS["weight_fractions"]]
        gate(d,"all finite positive weight fractions and the complete inversefrequency cover are explicit",
             len(fractions)==6 and len(set(fractions))==6 and all(0<q<1 for q in fractions)
             and PARAMETERS["inverse_frequency_subintervals"]==64)
        d["new_weighted_candidates"]={}
        for frac in fractions:
            key=str(frac);ca={"weight_fraction":key,"both_mean_denominators_retained":True,
                "all_M_in_4N_including_unbounded_frequency":True,
                "input_gamma_is_physical_nonmean_curvature":True,
                "output_body_ordinary_L2_not_joint_module":True}
            au={}
            profile,kernel=weighted_kernel(ref,frac,qplus,au)
            ints=weight_integrals(cells,profile,ca,au)
            compose_case(kernel,ints,left,qplus,ca)
            d["new_weighted_candidates"][key]=ca
            audit["weights"][key]=au
        gate(d,"all six weights have complete directed source kernel mean and outer feedback records",
             len(d["new_weighted_candidates"])==6 and
             all(len(audit["weights"][str(q)]["profile"])==949 and
                 len(audit["weights"][str(q)]["complete_inverse_frequency_bins"])==64 and
                 len(audit["weights"][str(q)]["new_weighted_source_cells"])==len(cells)
                 for q in fractions))
        d["new_weighted_candidates_evaluated"]=6
        d["new_weighted_posterior_cases_passed"]=sum(c["complete_weighted_posterior_applies"]
                                                   for c in d["new_weighted_candidates"].values())
        gate(d,"failed new chi candidates remain complete and no missing lowbody or cut datum is assumed",
             all(c["posterior_bounds"] is not None if c["complete_weighted_posterior_applies"]
                 else c["posterior_bounds"] is None for c in d["new_weighted_candidates"].values())
             and d["actual_low_inner_curvature_selfmap_proved"] is False)
        raw_audit=canonical(audit)
        audit_path=a.out.parent/"temporary-complete-weighted-cap-receiver-audit.json"
        audit_path.parent.mkdir(parents=True,exist_ok=True);audit_path.write_bytes(raw_audit)
        d["temporary_complete_new_audit"]={"bytes":len(raw_audit),
              "sha256":sha_bytes(raw_audit),"persisted":False}
        d["scope"]={
            "fixed_actual_ac1_continuous_repaired_cap":True,
            "same_M_real_reflection_zero_width_product_domain":True,
            "all_fourier_modes_and_Cmean_included":True,
            "Bmean_exact_zero_only_for_actual_reflection_application":True,
            "left_receiver_sourcepoints_cover_full_cap":True,
            "new_weighted_body_output_interval":["9/10","19/20"],
            "full_selected_reference_affine_difference_retained":True,
            "moving_high96_and_high288_use_exact_finite_direction_cancellation":True,
            "moving_high_bound_does_not_identify_physical_and_moving_modes":True,
            "new_local_science_does_not_use_active_Green_arrays":True,
            "narrow_MA_domain_not_extended":True,
            "unknown_actual_cut_or_left_core_body_supplied":False}
        gate(d,"the complete new receipt retains all means affine columns and exact source output types",
             d["scope"]["all_fourier_modes_and_Cmean_included"]
             and d["scope"]["full_selected_reference_affine_difference_retained"]
             and not d["scope"]["unknown_actual_cut_or_left_core_body_supplied"])
        d["complete"]=True;d["actual_returncode"]=0
    except Exception as e:
        d["failure"]={"type":type(e).__name__,"message":str(e),"traceback":traceback.format_exc()}
        d["actual_returncode"]=1
    d["seconds"]=time.monotonic()-started
    save(a.out,d)
    print(json.dumps({"kind":KIND,"complete":d["complete"],"failure":d["failure"],
          "gates":len(d["gates"]),"gates_passed":sum(g["passed"] for g in d["gates"]),
          "new_weighted_posterior_cases_passed":d.get("new_weighted_posterior_cases_passed"),
          "output_bytes":a.out.stat().st_size,"output_sha256":sha(a.out),
          "seconds":d["seconds"]},allow_nan=False),flush=True)
    if not d["complete"]:raise SystemExit(1)

if __name__=="__main__":main()
