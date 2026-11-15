#!/usr/bin/env python3
"""Consume original closed rows for new cap L1 and reference endpoint bounds.

No target, coefficient enclosure, old residual, Riccati or matrix is recomputed.
All new numerical arithmetic belongs in the public Actions runner.
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
KIND="actual_cached_cap_L1_and_reference_endpoint_sources_v1"
CANDIDATE="ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
DEFINITION="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
OBJECT="91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848"
ALPHA=Fraction(6890507429876859,9007199254740992)
NU=Fraction(-2572625729470897,72057594037927936)
ETA=Fraction(-7789843107295549,4611686018427387904)
LEFT,RIGHT=Fraction(9,10),Fraction(25,8)
MERGED_SHA="6f52030b7954f049a8e42a5a513a1f69b553819065b0c8b2245fa173e514cbb1"
MERGED_BYTES=4592623
MERGER_SHA="24ec0bf2b9d2b03ebfa07f4b39b8fdee3277f8e4b2aa14385c267122e6b8e81f"
OLD_RESIDUAL_PRODUCER="98eb7034038d76a341e112927cff4bcb7bfd425bc56698305803a689060ac31e"
FILES={
 "parts":"notes/2026-11-14-R133-final-complete-moving-residual-parts.json",
 "cap":"notes/2026-11-14-R133-final-physical-cap-linear-module-r09-v2-native.json.gz",
 "intrinsic":"notes/2026-11-13-Codazzi-rotational-positive-cap-v2-native.json.gz",
 "background":"notes/2026-11-14-R133-continuous-repair-physical-cap-background-v2-native.json.gz"}
EXPECTED={
 "cap":"ad6efc2a226131245ff4197a0b5da2843578224368a340f7a50d383c03a1819b",
 "intrinsic":"3a89805ebe1ab22000529a7a8c2fdc262b1c3a2afbc52433cf610d2d6542ff22",
 "background":"35db98d4124d50ef3bd69f3ec3aa6906289e3f6083c3ba91c8197da7547830ff"}
PARAMETERS={
 "bits":320,"cap_interval":["9/10","25/8"],"physical_eta":str(ETA),
 "affine_parameter_offset":"0","original_parameter_half_width":"1/1000000000",
 "exact_nu":str(NU),"exact_alpha":str(ALPHA),"physical_minimum_frequency":4,
 "complete_residual_support":96,"maximum_physical_residual_frequency":384,
 "candidate_outer_radii":["1/10000000000","1/1000000000"],
 "fixed_normalized_outer_height_radius":"1/1152921504606846976",
 "nonlinear_body_radius":"1/32768","physical_Q_remainder_coefficient":13}

def sha_bytes(b):return hashlib.sha256(b).hexdigest()
def sha(p):return sha_bytes(Path(p).read_bytes())
def exact(v):
    q=Fraction(v)
    return arb(q.numerator)/q.denominator
def upper(v):return abs(arb(v)).upper()
def point_upper(v):return arb(v).upper()
def maximum(values):
    return max((point_upper(v) for v in values),default=arb(0)).upper()
def b(r):return arb(r["lower"]).lower().union(arb(r["upper"]).upper())
def rec(v):
    z=arb(v)
    if not z.is_finite():raise ValueError("nonfinite output bound")
    return {"ball":z.str(90),"lower":z.lower().str(90),"upper":z.upper().str(90)}
def records(v):return {k:rec(x) for k,x in v.items()}
def read(p):
    raw=Path(p).read_bytes()
    return json.loads(gzip.decompress(raw) if str(p).endswith(".gz") else raw)
def save(p,d):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(d,indent=2,allow_nan=False)+"\n").encode()
    t=p.with_name(p.name+".tmp");t.write_bytes(raw);t.replace(p)
def gate(doc,name,ok):
    doc["gates"].append({"name":name,"passed":bool(ok)})
    if not ok:raise ValueError("gate failed: "+name)

def restore_original(root,doc):
    path=root/TOPIC/FILES["parts"]
    d=read(path)
    gate(doc,"same_original_three_part_complete7296_container",
        d["kind"]=="complete_native_lossless_container_binary_parts_v2"
        and d["native_complete"] is True and d["native_failure"] is None
        and d["complete_native_rows"]==7296 and d["original_bytes"]==MERGED_BYTES
        and d["original_sha256"]==MERGED_SHA and d["original_source_sha256"]==MERGER_SHA
        and d["candidate_sha256"]==CANDIDATE and len(d["parts"])==3)
    chunks=[];cursor=0;receipts=[]
    for i,r in enumerate(d["parts"]):
        if r["index"]!=i or r["offset"]!=cursor or Path(r["file"]).name!=r["file"]:
            raise ValueError("an original byte-part position changed")
        raw=(path.parent/r["file"]).read_bytes()
        if len(raw)!=r["compressed_bytes"] or sha_bytes(raw)!=r["compressed_sha256"]:
            raise ValueError("an original compressed byte part changed")
        payload=gzip.decompress(raw)
        if len(payload)!=r["bytes"] or sha_bytes(payload)!=r["sha256"]:
            raise ValueError("an original byte part payload changed")
        chunks.append(payload);cursor+=len(payload)
        receipts.append({k:r[k] for k in ("index","file","offset","bytes","sha256",
                                          "compressed_bytes","compressed_sha256")})
    raw=b"".join(chunks)
    if len(raw)!=MERGED_BYTES or sha_bytes(raw)!=MERGED_SHA:
        raise ValueError("the restored original container differs")
    doc["original_restoration"]={"manifest_sha256":sha(path),"container_sha256":MERGED_SHA,
        "container_bytes":len(raw),"parts":receipts,"new_parts_created":False,
        "original_mathematics_executed":False}
    return json.loads(gzip.decompress(raw))

def cover(rows,left,right,label):
    cursor=left
    for row in rows:
        lo,hi=map(Fraction,row["interval"])
        if lo!=cursor or not lo<hi:raise ValueError(label+" has a gap, overlap or zero cell")
        cursor=hi
    if cursor!=right:raise ValueError(label+" has an incorrect final endpoint")

def inputs(a,doc):
    root=a.root
    for k,p in FILES.items():
        if k!="parts" and sha(root/TOPIC/p)!=EXPECTED[k]:
            raise ValueError("immutable original input changed: "+k)
    residual=restore_original(root,doc)
    cap,intrinsic,bg=[read(root/TOPIC/FILES[k]) for k in ("cap","intrinsic","background")]
    gate(doc,"same_complete_raw7296_fixed_eta_and_full_mean",
        residual["kind"]=="complete_actual_moving_residual_all_closed_rows_and_interfaces"
        and residual["complete"] is True and residual["failure"] is None
        and residual["source_sha256"]==MERGER_SHA
        and residual["original_producer_sha256"]==OLD_RESIDUAL_PRODUCER
        and residual["candidate_sha256"]==CANDIDATE and residual["object_sha256"]==OBJECT
        and Fraction(residual["exact_amplitude"])==ALPHA
        and Fraction(residual["exact_nu"])==NU
        and Fraction(residual["common_parameter_half_width"])==0
        and residual["all_7296_closed_rows_reused_without_recomputation"]
        and residual["all_6143_actual_interfaces_paid"]
        and residual["complete_original_primitive_tail"]
        and residual["complete_residual_support"]==96 and len(residual["rows"])==7296)
    cover(residual["rows"],Fraction(0),RIGHT,"original7296")
    for i,r in enumerate(residual["rows"]):
        if r["index"]!=i or r["exact_angular_support_index"]!=96:
            raise ValueError("original full residual row identity differs")
    gate(doc,"same_exact_all_mode_reference_and_whole_original_intrinsic_cache",
        cap["kind"]=="actual_final_physical_cap_linear_module_v1"
        and cap["complete"] is True and cap["candidate_sha256"]==CANDIDATE
        and cap["object_sha256"]==OBJECT and cap["cap_cache_sha256"]==EXPECTED["intrinsic"]
        and Fraction(cap["exact_alpha"])==ALPHA and Fraction(cap["exact_nu"])==NU
        and Fraction(cap["exact_eta_center"])==ETA
        and Fraction(cap["parameter_half_width"])==Fraction(1,10**9)
        and cap["whole_original_eta"] and cap["complete_primitive_tail"]
        and cap["complete_unknown_Fourier_modes"] and cap["exact_interval"]==["9/10","25/8"]
        and intrinsic["complete"] is True and intrinsic["cap_linear_reference_certified"]
        and intrinsic["object_sha256"]==OBJECT
        and Fraction(intrinsic["exact_center_parameter"])==ETA
        and Fraction(intrinsic["parameter_half_width"])==Fraction(1,10**9)
        and intrinsic["whole_affine_parameter_interval"] and intrinsic["complete_primitive_tail"])
    ref=cap["reference_rows"]
    if len(ref)!=cap["native_reference_rows"]:raise ValueError("reference row count changed")
    cover(ref,LEFT,RIGHT,"original reference")
    gate(doc,"same_complete_reference1346_intersections_and_actual_germs",
         len(cap["closed_cover"])==cap["complete_closed_intersections"]==1346)
    cover(cap["closed_cover"],LEFT,RIGHT,"original1346cover")
    for r in ref:
        n=intrinsic["rows"][r["native_index"]]
        nl,nr=map(Fraction,n["interval"]);l,h=map(Fraction,r["interval"])
        if not nl<=l<h<=nr:raise ValueError("reference row does not belong to its true intrinsic row")
        if not n.get("actual_scalar_germ"):raise ValueError("true intrinsic germ identity missing")
        rb={k:b(v) for k,v in r["bounds"].items()}
        gamma=b(n["coefficients"]["gamma"])
        if not (gamma>0 and rb["D_rate"]>0 and rb["C_rate"]>0
            and rb["lower_face"]>0 and rb["upper_face"]>0 and rb["q_lower"]>0):
            raise ValueError("a complete original rate or invariant face is not positive")
    gate(doc,"same_continuous_repair_full_background_and_residual_difference",
        bg["kind"]=="actual_continuous_repair_physical_cap_and_residual_conjugation_v1"
        and bg["complete"] is True and all(g["passed"] for g in bg["gates"])
        and bg["original_candidate_sha256"]==CANDIDATE
        and bg["derived_definition_sha256"]==DEFINITION and bg["object_sha256"]==OBJECT
        and bg["cap_input_sha256"]==EXPECTED["cap"]
        and bg["exact_interval"]==["9/10","25/8"]
        and bg["whole_original_eta_for_background_transfer"]
        and Fraction(bg["background_parameter_half_width"])==Fraction(1,10**9)
        and bg["real_continuous_repaired_centre"]
        and bg["original_ac1_native_silently_relabelled"] is False)
    selected=[r for r in residual["rows"] if Fraction(r["interval"][1])>LEFT
        and Fraction(r["interval"][0])<RIGHT]
    clipped=[dict(r,interval=[str(max(LEFT,Fraction(r["interval"][0]))),
                            str(min(RIGHT,Fraction(r["interval"][1])))]) for r in selected]
    cover(clipped,LEFT,RIGHT,"selected exact cap")
    gate(doc,"all1341_actual_cap_residual_rows_with_true_9over10",len(clipped)==1341)
    doc["inputs"]={**EXPECTED,"merged":MERGED_SHA,
        "parts_manifest":sha(root/TOPIC/FILES["parts"])}
    doc["original_complete_residual_rows"]=7296
    doc["selected_cap_residual_rows"]=len(clipped)
    doc["original_reference_rows"]=len(ref)
    doc["original_reference_closed_intersections"]=1346
    doc["old_whole_L1_bounds_reused_without_reaggregation"]=residual["bounds"]["residual_L1_r_A0"]
    return residual,clipped,cap,intrinsic,bg

def physical_constants(bg,doc):
    q={k:b(v) for k,v in bg["bounds"].items()}
    out={k:q[n].upper() for k,n in {
        "C":"physical_C_A_1over64","B":"physical_B_A_1over64",
        "Ctheta":"physical_C_theta_A_1over64","Btheta":"physical_B_theta_A_1over64",
        "inverse_displacement":"actual_inverse_displacement_A_1over64",
        "repair_pair_residual_A0":"exact_repair_residual_difference_A0",
        "Q_B":"corrected_physical_Q_B_A_1over64",
        "Q_C":"corrected_physical_Q_C_A_1over64",
        "original_corrected_Z_at_R":"corrected_outer_Z_A0"}.items()}
    gate(doc,"fixed_r_full_degree96_composition_and_complete_physical_units",
        out["inverse_displacement"]<exact(Fraction(1,256))
        and out["C"]<exact(Fraction(1,3)) and out["B"]<exact(Fraction(1,128))
        and out["Ctheta"]<exact(Fraction(1,32)) and out["Btheta"]<exact(Fraction(1,32)))
    out["composition"]=(384*out["inverse_displacement"]).exp().upper()
    gate(doc,"complete_fixed_r_inverse_angle_factor_below5",out["composition"]<5)
    return out

def physical_source(row,const):
    moving=[(exact(ALPHA)*b(row["complete_residual_A0"][k]).upper()
             +const["repair_pair_residual_A0"]).upper() for k in ("U","V")]
    U,V=[(const["composition"]*v).upper() for v in moving]
    C,B,Ct,Bt=[const[k] for k in ("C","B","Ctheta","Btheta")]
    FB=(C*U+(B*C+Bt*C/4)*V).upper()
    FC=((C*C+Ct*C/4)*V).upper()
    return moving,[FB,FC]

def finite_integral(k,h):
    k=arb(k);h=exact(h)
    if k==0:return h
    if not k>0:raise ValueError("a signed denominator cannot be used as positive damping")
    return ((1-(-k*h).exp())/k).upper()

def consume(rows,cap,intrinsic,const,doc):
    ref=cap["reference_rows"];rl=[Fraction(r["interval"][0]) for r in rows]
    ql=[Fraction(r["interval"][0]) for r in ref]
    edges=sorted({LEFT,RIGHT,*[Fraction(t) for r in rows for t in r["interval"]],
                  *[Fraction(t) for r in ref for t in r["interval"]]})
    common=[];prefix=arb(0);sourceL1=[arb(0),arb(0)];movingL1=[arb(0),arb(0)]
    for i,(left,right) in enumerate(zip(edges,edges[1:])):
        ir=bisect_right(rl,left)-1;iq=bisect_right(ql,left)-1
        rr,qr=rows[ir],ref[iq]
        if not (Fraction(rr["interval"][0])<=left<right<=Fraction(rr["interval"][1])
            and Fraction(qr["interval"][0])<=left<right<=Fraction(qr["interval"][1])):
            raise ValueError("common endpoint grid has a gap or crossed a closed input cell")
        rb={k:b(v) for k,v in qr["bounds"].items()}
        target=intrinsic["rows"][qr["native_index"]]
        gamma=upper(b(target["coefficients"]["gamma"]))
        sd,sc=rb["D_rate"].lower(),rb["C_rate"].lower()
        ratio=(gamma/(sd+sc)).upper();prefix=max(prefix,ratio).upper()
        moving,F=physical_source(rr,const);h=exact(right-left)
        for k in range(2):
            movingL1[k]+=h*moving[k];sourceL1[k]+=h*F[k]
        common.append({"index":i,"interval":[str(left),str(right)],"original_residual_index":rr["index"],
            "reference_index":iq,"intrinsic_index":qr["native_index"],
            "actual_scalar_germ":target["actual_scalar_germ"],
            "C_rate":sc,"D_rate":sd,"q_upper":rb["q_upper"].upper(),
            "prefix_Tdc":prefix,"source_B":F[0],"source_C":F[1]})
    if not common or common[-1]["interval"][1]!=str(RIGHT):
        raise ValueError("the common true cap cover is incomplete")
    suffix=arb(0);endpoint=arb(0);pieces=[]
    for r in reversed(common):
        left,right=map(Fraction,r["interval"]);sc=r["C_rate"]
        weight=((-4*suffix).exp()*finite_integral(4*sc,right-left)).upper()
        Bweight=(r["prefix_Tdc"]*weight).upper()
        Cweight=((1+r["q_upper"]*r["prefix_Tdc"])*weight).upper()
        contribution=(Bweight*r["source_B"]+Cweight*r["source_C"]).upper()
        endpoint+=contribution
        pieces.append({k:r[k] for k in ("index","interval","original_residual_index",
            "reference_index","intrinsic_index","actual_scalar_germ")}|{
            "bounds":records({k:r[k] for k in ("C_rate","D_rate","q_upper","prefix_Tdc",
                "source_B","source_C")}|{"C_source_B_weight":Bweight,"C_source_C_weight":Cweight,
                "C_known_body_contribution":contribution})})
        suffix=(suffix+sc*exact(right-left)).lower()
    pieces.reverse()
    cb={k:b(v) for k,v in cap["bounds"].items()}
    HD=cb["outer_nonzero_d_port"].upper();HC=cb["inner_C_port"].upper()
    qplus=cb["q_upper"].upper();KG=cb["complete_module_Q_kernel"].upper()
    Bgain=max(arb(1),HD).upper()
    Cgain=max(arb(1),(HD*qplus+HC).upper()).upper()
    gate(doc,"full_reference_L1_source_gains_with_both_means",Bgain<10 and Cgain<17 and KG<16)
    gD=exact(Fraction(13,10**16));g0=exact(Fraction(205,10**21))
    unclosed_body=(Bgain*sourceL1[0]+Cgain*sourceL1[1]).upper()
    unclosed_affine=(unclosed_body+HD*gD+g0).upper()
    weighted_known=(endpoint+prefix*gD).upper()
    totals={"moving_U_L1":movingL1[0].upper(),"moving_V_L1":movingL1[1].upper(),
        "physical_B_ordinary_L1":sourceL1[0].upper(),"physical_C_ordinary_L1":sourceL1[1].upper(),
        "complete_reference_B_L1_gain":Bgain,"complete_reference_C_L1_gain":Cgain,
        "complete_reference_Q_gain":KG,"unclosed_reference_body_pair":unclosed_body,
        "unclosed_reference_complete_known_affine_pair":unclosed_affine,
        "reference_C_nonmean_R_from_known_body":endpoint.upper(),
        "reference_C_nonmean_R_from_known_body_and_right_d":weighted_known,
        "reference_Cmean_R_independent_load":g0,
        "reference_C_R_from_left_C_gain":(-4*suffix).exp().upper(),
        "reference_C_R_from_right_d_gain":prefix,
        "true_repaired_right_d_known_load":gD,
        "true_repaired_right_Cmean_known_load":g0,
        "integrated_C_rate_lower":suffix}
    doc["complete_common_cap_cells"]=len(common)
    doc["reference_endpoint_rows"]=pieces
    doc["bounds"]=records(totals)
    doc["physical_source_constants"]=records(const)
    gate(doc,"complete_new_weighted_integrals_are_finite_nonnegative",
         all(v.is_finite() and v>=0 for v in totals.values()))
    return totals,cb

def outer_diagnostics(t,cb,const,doc):
    rho=exact(Fraction(1,32768));height=arb(2)**-60
    eps=arb(2)**-256
    comparison=cb["historical_to_current_outer_q_comparison"].upper()
    gate(doc,"old_and_current_regular_multiplier_difference_is_retained",
         comparison<arb(2)**-500)
    DB,DC=const["Q_B"],const["Q_C"]
    # max is the operator norm from the SUM pair norm to the scalar Q source.
    multiplication=max(DB,DC).upper()
    KG=t["complete_reference_Q_gain"];HD=cb["outer_nonzero_d_port"].upper()
    eta=t["unclosed_reference_complete_known_affine_pair"]
    entries=[]
    for text in PARAMETERS["candidate_outer_radii"]:
        z=exact(text);rf=10*(z+height);F=rf+height;kappa=36*(arb(2)**12)*F
        valid0=bool(kappa<1 and 2*F<arb(2)**-25 and 6*F<arb(2)**-20)
        if not valid0:raise ValueError("a requested larger true long ball exceeds the complete primary domain")
        Jf=9/(1-kappa)
        Jheight=(eps+kappa)/(1-kappa)
        T=(eps+4*(arb(2)**14)*F*Jf+comparison).upper()
        C=(4*(arb(2)**11)*F*Jf).upper()
        U=(eps+4*(arb(2)**14)*F*(1+Jheight)).upper()
        V=(4*(arb(2)**11)*F*(1+Jheight)).upper()
        image=(9*z+eps*height+9*(arb(2)**12)*F*F).upper()
        valid=bool(image<rf)
        chi=(KG*multiplication+HD*T+C).upper()
        body_image=(eta+chi*rho+13*KG*rho*rho).upper()
        body_lip=(chi+26*KG*rho).upper()
        room=(z-const["original_corrected_Z_at_R"]).lower()
        entries.append({"Z_radius":text,"normalized_height_radius":str(Fraction(1,2**60)),
            "reflection_Bmean_exactly_zero":True,"full_even_Cmean_retained":True,
            "true_long_background_domain_and_image_passed":valid,
            "formal_body_image_if_endpoint_domain_is_preserved":bool(body_image<rho),
            "formal_body_Lipschitz_if_endpoint_domain_is_preserved":bool(body_lip<1),
            "known_reference_endpoint_column_fits_remaining_room":bool(
                room>0 and t["reference_C_nonmean_R_from_known_body_and_right_d"]<room),
            "complete_nonlinear_endpoint_invariance_proved":False,
            "unknown_linear_Q_nonlinear_Q_and_outer_endpoint_feedback_paid":False,
            "bounds":records({"r_f":rf,"F":F,"kappa":kappa,"fixed_point_image":image,
                "D_Z_d":T,"D_Z_cmean":C,"D_height_d_order2":U,"D_height_cmean_order2":V,
                "complete_body_linear_and_outer_coefficient":chi,
                "formal_body_image":body_image,"formal_body_Lipschitz":body_lip,
                "endpoint_remaining_room":room})})
    doc["candidate_larger_outer_ball_diagnostics"]=entries
    gate(doc,"requested_complete_long_value_balls_are_legitimate",
         all(r["true_long_background_domain_and_image_passed"] for r in entries))

def summary(doc):
    keep=("kind","complete","failure","source_sha256","parameters","inputs","seconds","gates",
        "original_complete_residual_rows","selected_cap_residual_rows","original_reference_rows",
        "original_reference_closed_intersections","complete_common_cap_cells","bounds",
        "physical_source_constants","candidate_larger_outer_ball_diagnostics",
        "old_whole_L1_bounds_reused_without_reaggregation","scope",
        "old_targets_residual_enclosures_reference_ODE_and_primitive_recomputed",
        "new_reference_Riccati_or_Fourier_samples","new_recomputable_data_persisted")
    return {k:doc[k] for k in keep if k in doc}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root",type=Path,required=True)
    p.add_argument("--out",type=Path,required=True)
    p.add_argument("--summary",type=Path,required=True)
    a=p.parse_args();ctx.prec=PARAMETERS["bits"];ctx.cap=6
    if a.out.exists() or a.summary.exists():raise FileExistsError("preserve each actual mathematical attempt")
    start=time.monotonic()
    d={"kind":KIND,"complete":False,"failure":None,"source_sha256":sha(__file__),
       "parameters":PARAMETERS,"gates":[],
       "old_targets_residual_enclosures_reference_ODE_and_primitive_recomputed":0,
       "new_reference_Riccati_or_Fourier_samples":0,"new_recomputable_data_persisted":False,
       "scope":{"fixed_eta0":True,"fixed_repaired_M32_delta0":True,"full_even_mean":True,
           "reference_all_physical_frequencies":True,"ordinary_sources_only":True,
           "known_centre_residual_reflection_parity":True,
           "old_whole_L1_norm_recomputed":False,"new_cap_intersection_L1_consumption":True,
           "unclosed_reference_endpoint_columns_only":True,
           "complete_nonlinear_endpoint_invariance_proved":False,
           "complete_nonlinear_cap_solution_proved":False,"whole_infinite_BVP_inverse_proved":False}}
    try:
        residual,rows,cap,intrinsic,bg=inputs(a,d)
        const=physical_constants(bg,d)
        totals,cb=consume(rows,cap,intrinsic,const,d)
        outer_diagnostics(totals,cb,const,d)
        d["complete"]=True
    except Exception as e:
        d["failure"]={"type":type(e).__name__,"message":str(e),"traceback":traceback.format_exc()}
    finally:
        d["seconds"]=time.monotonic()-start
        save(a.out,d)
        s=summary(d);s["temporary_full_output_sha256"]=sha(a.out)
        s["temporary_full_output_bytes"]=a.out.stat().st_size
        raw=(json.dumps(s,indent=2,allow_nan=False)+"\n").encode()
        if len(raw)>60000:raise ValueError("genuine cap conclusion exceeds60000 UTF8 bytes")
        save(a.summary,s)
        print(json.dumps(s,allow_nan=False),flush=True)
    if not d["complete"]:raise RuntimeError("actual new cap consumer failed; small evidence retained")

if __name__=="__main__":main()
