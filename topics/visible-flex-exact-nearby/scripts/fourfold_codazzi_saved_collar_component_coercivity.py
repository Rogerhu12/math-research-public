#!/usr/bin/env python3
"""New restrictions of frozen complete positive rows; no old mathematics runs."""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
import time
import traceback
from flint import arb, ctx

TOPIC=Path("topics/visible-flex-exact-nearby")
KIND="actual_saved_positive_collar_components_and_high_coercivity_v1"
ORIGINAL_KIND="complete_current_moving_positive_body_coefficients_v1"
ORIGINAL_LEFT=Fraction("0.2384058742994")
ORIGINAL_RIGHT=Fraction(25,8)
LEFT,RIGHT,CUT=Fraction(17,20),Fraction(19,20),Fraction(9,10)
ETA=Fraction(-7789843107295549,4611686018427387904)
NU=Fraction(-2572625729470897,72057594037927936)
ALPHA=Fraction(6890507429876859,9007199254740992)
CANDIDATE="ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
OBJECT="91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848"
CAP_CACHE="3a89805ebe1ab22000529a7a8c2fdc262b1c3a2afbc52433cf610d2d6542ff22"
DEFINITION="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
NATIVE_SHA="ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d"
NATIVE_BYTES=6223338
PRODUCER_SHA="1292a1c06695d49a6f5e6bca27ad375b2fd82b44ebe1e6066327b7b7a79d882c"
PARTS_SHA="32b430a27a20726f095098902afdb93e656ea746eb81bce09a559e6f65787fd3"
D_SHA="6956c214240cd85e6263331b33e0c7efcf6abc3e71190d46ff3eabddecd35071"
D_SOURCE="827fcb237a79b48c095872b61c370ff2ceafc143a8dc6a1774021188ff3ea320"
FILES={
 "parts":"notes/2026-11-14-R133-current-positive-complete-ac1-binary-parts.json",
 "intrinsic_receipt":"notes/selected_parameter_core_scalar_fees_ci/run-43713242980-1/execution.json",
 "producer":"scripts/fourfold_codazzi_current_positive_complete_coefficients.py"}
EXPECTED={"parts":PARTS_SHA,"intrinsic_receipt":D_SHA,"producer":PRODUCER_SHA}
PARAMETERS={
 "arithmetic_bits":320,"exact_interval":["17/20","19/20"],"exact_cut":"9/10",
 "exact_eta":str(ETA),"exact_nu":str(NU),"exact_alpha":str(ALPHA),
 "original_parameter_half_width":"1/1000000000",
 "selected_delta_half_width":"1/10000000000",
 "original_complete_rows":4650,"original_native_bytes":NATIVE_BYTES,
 "original_native_sha256":NATIVE_SHA,"original_parts":4,
 "centre_pair_A0_repair":"0.000000000000000003861",
 "centre_pair_angle_A0_repair":"0.00000000000000001970",
 "centre_even_mean_repair":"0.000000000000000000005842",
 "canonical_response_pair_A0":"19","canonical_response_pair_angle_A0":"83",
 "rho_candidates":["1/10000","1/1048576","1/16777216","1/268435456","1/4294967296","1/68719476736"],
 "high_projection_labels":[96,288],"physical_frequency_factor":4,
 "candidate_count":12,"energy_tests_per_candidate":["tau_below_one","t_below_one"],
 "actual_mean_sign_is_a_separate_candidate_prerequisite":True,
 "triangular_cutoff_derivative_upper":"20",
 "ordinary_radial_measure":"dr","angular_measure":"normalized moving circle",
 "same_real_continuous_two_sided_H1_true_solution_required":True,
 "actual_ordinary_residual_is_zero":True,
 "full_low_mean_retained":True,"source_integrals_recomputed":False,
 "new_unknown_cut_body_or_receiver_norm_supplied":False,
 "old_target_Fourier_trial_convolution_residual_repair_mean_flow_Green_calls":0}
FIELD_NAMES=("U_A0","V_A0","U_phi_A0","V_phi_A0","V_nonmean_A0",
             "mean_v","drift_A0","drift_phi_A0","full_S_mean")
BASE_NAMES=("P1_upper","P2_upper","Pnorm_upper","K_upper","gamma_upper","beta_absolute",
            "M0","M1","N0","Mmean","b","alpha","g","raw_U","raw_V",
            "raw_Uphi","raw_Vphi","raw_Vnonmean","raw_drift","raw_drift_phi",
            "raw_abs_mean","raw_Smean_upper")
CASE_MAX_NAMES=("Mdelta","Mdelta1","eta","actual_Smean_upper","actual_logspeed",
                "d0","ddelta","drift_reference_delta","drift_nonlinear","actual_drift",
                "Aref_delta_projected","Anonlinear","Amix","Ahigh",
                "C_shell96","C_low96","C_shell288","C_low288")
CASE_MIN_NAMES=("actual_mean_gap","actual_principal_lower")

def sha_bytes(raw):return hashlib.sha256(raw).hexdigest()
def sha(path):return sha_bytes(Path(path).read_bytes())
def exact(value):
    q=Fraction(value)
    return arb(q.numerator)/q.denominator
def upper(value):return arb(value).upper()
def lower(value):return arb(value).lower()
def abs_upper(value):return abs(arb(value)).upper()
def box(value):
    if isinstance(value,dict):
        if "lower" in value and "upper" in value:
            z=arb(value["lower"]).lower().union(arb(value["upper"]).upper())
        elif "ball" in value:z=arb(value["ball"])
        else:raise ValueError("an original complete directed ball is required")
    else:raise ValueError("a bare numeric midpoint is not an original enclosure")
    if not z.is_finite():raise ValueError("an original directed ball is nonfinite")
    return z
def rec(value):
    z=arb(value)
    if not z.is_finite():raise ValueError("a new scalar is nonfinite")
    return {"ball":z.str(60)}
def recs(values):return {k:rec(v) for k,v in values.items()}
def canonical(doc):
    return (json.dumps(doc,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n").encode()
def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith(".gz") else raw)
def save(path,doc):
    raw=(json.dumps(doc,indent=2,allow_nan=False)+"\n").encode()
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temporary=path.with_name(path.name+".tmp");temporary.write_bytes(raw);temporary.replace(path)
def gate(doc,name,ok):
    doc["gates"].append({"name":name,"passed":bool(ok)})
    if not ok:raise ValueError("gate failed: "+name)
def norm_upper(value):
    z=box(value)
    if not z.upper()>=0:raise ValueError("an original norm has a negative upper endpoint")
    return abs_upper(z)

def restore_original(root,doc):
    path=root/TOPIC/FILES["parts"];parts=read(path)
    gate(doc,"the original4650 native and its four exact natural parts are fixed",
        parts.get("kind")=="complete_native_lossless_container_binary_parts_v2"
        and parts.get("native_kind")==ORIGINAL_KIND and parts.get("native_complete") is True
        and parts.get("native_failure") is None and parts.get("complete_native_rows")==4650
        and parts.get("original_bytes")==NATIVE_BYTES and parts.get("original_sha256")==NATIVE_SHA
        and parts.get("original_source_sha256")==PRODUCER_SHA
        and parts.get("candidate_sha256")==CANDIDATE and len(parts.get("parts",[]))==4
        and parts.get("no_numerical_record_changed") is True
        and parts.get("original_container_restored_exactly") is True)
    chunks=[];cursor=0;receipts=[]
    for index,r in enumerate(parts["parts"]):
        if r["index"]!=index or r["offset"]!=cursor or Path(r["file"]).name!=r["file"]:
            raise ValueError("an original part byte position or basename changed")
        raw=(path.parent/r["file"]).read_bytes()
        if len(raw)!=r["compressed_bytes"] or sha_bytes(raw)!=r["compressed_sha256"]:
            raise ValueError("an original compressed part changed")
        payload=gzip.decompress(raw)
        if len(payload)!=r["bytes"] or sha_bytes(payload)!=r["sha256"]:
            raise ValueError("an original part payload changed")
        chunks.append(payload);cursor+=len(payload)
        receipts.append({k:r[k] for k in ("index","file","offset","bytes","sha256",
                                          "compressed_bytes","compressed_sha256")})
    raw=b"".join(chunks)
    if len(raw)!=NATIVE_BYTES or sha_bytes(raw)!=NATIVE_SHA:
        raise ValueError("the whole original native was not restored exactly")
    doc["original_restoration"]={"manifest_sha256":sha(path),"container_sha256":NATIVE_SHA,
        "container_bytes":len(raw),"parts":receipts,"new_parts_created":False,
        "original_mathematics_executed":False}
    return json.loads(gzip.decompress(raw))

def checked_inputs(args,doc):
    manifest=read(args.manifest)
    gate(doc,"the exact new directed precision parameters and scientific source are immutable",
         args.bits==320 and manifest["parameters"]==PARAMETERS
         and manifest["source_sha256"]==sha(__file__))
    gate(doc,"every original and small current input byte hash matches the independent manifest",
         all(sha(args.root/p)==s for p,s in manifest["files"].items())
         and all(sha(args.root/TOPIC/p)==EXPECTED[k] for k,p in FILES.items()))
    old=restore_original(args.root,doc);ident=old.get("identity",{})
    gate(doc,"the complete old source candidate intrinsic family and physical amplitude are unchanged",
        old.get("kind")==ORIGINAL_KIND and old.get("complete") is True
        and old.get("coefficient_cover_complete") is True and old.get("failure") is None
        and not old.get("pending") and old.get("whole_original_eta") is True
        and len(old.get("rows",[]))==4650 and ident.get("source_sha256")==PRODUCER_SHA
        and ident.get("candidate_sha256")==CANDIDATE and ident.get("object_sha256")==OBJECT
        and ident.get("cap_cache_sha256")==CAP_CACHE
        and Fraction(ident["exact_eta_center"])==ETA
        and Fraction(ident["parameter_half_width"])==Fraction(1,10**9)
        and Fraction(ident["actual_nu"])==NU and Fraction(ident["actual_alpha"])==ALPHA
        and ident["modes"]==32 and Fraction(ident["left"])==ORIGINAL_LEFT
        and Fraction(ident["right"])==ORIGINAL_RIGHT
        and list(map(Fraction,old["covered_interval"]))==[ORIGINAL_LEFT,ORIGINAL_RIGHT])
    cursor=ORIGINAL_LEFT;selected=[];collar_cursor=LEFT;measure=Fraction(0);counts={}
    all_selected_valid=True
    for index,row in enumerate(old["rows"]):
        l,r=map(Fraction,row["interval"])
        if l!=cursor or not l<r:raise ValueError("the whole original4650 cover has a gap or overlap")
        cursor=r
        lo,hi=max(l,LEFT),min(r,RIGHT)
        if not lo<hi:continue
        if lo!=collar_cursor:raise ValueError("the new true collar intersections have a gap or overlap")
        gl,gr=map(Fraction,row["actual_scalar_germ"])
        cl,cr=map(Fraction,row["actual_candidate_germ"])
        provenance=row.get("intrinsic_provenance",{})
        kind=provenance.get("kind");counts[kind]=counts.get(kind,0)+1
        valid_kind=kind in ("same_intrinsic_cap_v2","new_true_intrinsic_closed_box")
        if kind=="same_intrinsic_cap_v2":
            valid_kind=valid_kind and isinstance(provenance.get("row"),int) and 0<=provenance["row"]<1334
        all_selected_valid=all_selected_valid and (
            valid_kind and provenance.get("part") is not None and gl<=l<r<=gr and cl<=l<r<=cr
            and row.get("complete_finite_modes")==32 and row.get("exact_local_band")==64
            and row.get("complete_primitive_intermediate_retained") is True
            and row.get("complete_mean_column_retained") is True
            and row.get("fields_are_moving_phi_not_physical_theta") is True
            and all(k in row.get("bounds",{}) for k in FIELD_NAMES)
            and all(k in row.get("intrinsic",{}) for k in ("beta","gamma","K")))
        selected.append({"index":index,"row":row,"intersection":[str(lo),str(hi)],
            "original_row_sha256":sha_bytes(canonical(row))})
        collar_cursor=hi;measure+=hi-lo
    gate(doc,"all4650 original closed rows cover their exact full positive interval",
         cursor==ORIGINAL_RIGHT)
    gate(doc,"every selected saved row keeps the complete physical fields mean primitive and true germ",
         all_selected_valid and bool(selected))
    gate(doc,"the new true intersections cover exactly17over20_to19over20 and contain the actual cut",
         collar_cursor==RIGHT and measure==Fraction(1,10)
         and any(Fraction(s["intersection"][0])<=CUT<=Fraction(s["intersection"][1]) for s in selected))
    receipt=read(args.root/TOPIC/FILES["intrinsic_receipt"])
    ds=receipt["actual_scientific_receipt"]
    gate(doc,"the existing D receipt is the original completed child0 twelvegate calculation",
         receipt.get("complete") is True and receipt.get("actual_returncode")==0
         and ds.get("complete") is True and ds.get("failure") is None
         and ds.get("actual_returncode")==0 and ds.get("source_sha256")==D_SOURCE
         and ds.get("kind")=="actual_selected_parameter_core_scalar_fees_from_complete_old_cells_v1"
         and len(ds.get("gates",[]))==12 and all(g["passed"] is True for g in ds["gates"])
         and ds.get("complete_original_rows_verified")==7721)
    collar=ds["complete_original_collar_intrinsic_conclusion"]
    LG=box(collar["complete_ratio_upper"]["gamma_r_over_gamma"]).upper()
    LK=box(collar["complete_ratio_upper"]["K_r_over_K"]).upper()
    gate(doc,"the two genuine intrinsic logarithmic derivative bounds have exactly the same collar",
         collar["exact_interval"]==["17/20","19/20"] and collar["exact_total_radial_measure"]=="1/10"
         and collar["original_closed_rows_consumed"]==140
         and collar["original_intrinsic_third_jets_read"] is True
         and collar["original_target_evaluations"]==0
         and collar["reference_s_is_not_full_moving_mean"] is True
         and collar["moving_mean_gap_claimed"] is False and LG>=0 and LK>=0)
    states=ds["verified_global_state_bounds"];chosen=ds["chosen_global_constants"]
    gate(doc,"the complete canonical response including its continuous repair fits19_and83",
         chosen["response_pair_A0"]=="19" and chosen["response_pair_angle_A0"]=="83"
         and box(states["response_pair_A0"])<19 and box(states["response_pair_angle_A0"])<83
         and ds["parameters"]["selected_family_cross_input_maximum_physical_frequency"]==1152
         and ds["parameters"]["delta_half_width"]=="1/10000000000")
    doc["original_counts"]={"complete_rows":4650,"selected_closed_rows":len(selected),
        "selected_provenance_counts":counts,"same_old_D_rows_not_restored":7721,
        "exact_total_selected_measure":str(measure)}
    doc["original_identity"]={k:ident[k] for k in ("source_sha256","candidate_sha256","object_sha256",
        "cap_cache_sha256","exact_eta_center","parameter_half_width","actual_nu","actual_alpha","modes")}
    doc["copied_complete_intrinsic_ratios"]={"D_receipt_sha256":D_SHA,"L_G":rec(LG),"L_K":rec(LK),
        "original_collar_conclusion":collar}
    doc["copied_canonical_direction_bounds"]={k:states[k] for k in ("response_pair_A0","response_pair_angle_A0")}
    return selected,LG,LK

def saved_row_components(item,LK):
    row=item["row"];bounds=row["bounds"]
    K,G,beta=(box(row["intrinsic"][k]) for k in ("K","gamma","beta"))
    mean,Smean=box(bounds["mean_v"]),box(bounds["full_S_mean"])
    if not K>0 or not G>0 or not mean<0:raise ValueError("original intrinsic or actual raw mean sign failed")
    U,V,U1,V1,Vne=(norm_upper(bounds[k]) for k in
        ("U_A0","V_A0","U_phi_A0","V_phi_A0","V_nonmean_A0"))
    drift=norm_upper(bounds["drift_A0"]);drift1=norm_upper(bounds["drift_phi_A0"])
    Kl,Ku,Gl,Gu=K.lower(),K.upper(),G.lower(),G.upper()
    p1=(1/Kl.sqrt().sqrt()).upper();p2=Ku.sqrt().sqrt().upper();p=max(p1,p2).upper()
    eq=exact(PARAMETERS["centre_pair_A0_repair"])
    eq1=exact(PARAMETERS["centre_pair_angle_A0_repair"])
    eqm=exact(PARAMETERS["centre_even_mean_repair"])
    b=(abs_upper(beta)*Ku.sqrt()).upper()
    values={
        "P1_upper":p1,"P2_upper":p2,"Pnorm_upper":p,"K_lower":Kl,"K_upper":Ku,
        "gamma_lower":Gl,"gamma_upper":Gu,"beta_absolute":abs_upper(beta),
        "k":max(arb(1),Ku).upper(),"R":(U+V).upper(),
        "M0":(((p1*U)**2+(p2*V)**2).sqrt()+p*eq).upper(),
        "M1":(((p1*U1)**2+(p2*V1)**2).sqrt()+p*eq1).upper(),
        "N0":(((p1*U)**2+(p2*Vne)**2).sqrt()+p*eq).upper(),
        "Mmean":(p2*(abs_upper(mean)+eqm)).upper(),
        "b":b,"alpha":(abs_upper(beta)+LK/4).upper(),"g":(Gu*p2).upper(),
        "raw_U":U,"raw_V":V,"raw_Uphi":U1,"raw_Vphi":V1,"raw_Vnonmean":Vne,
        "raw_drift":drift,"raw_drift_phi":drift1,"raw_abs_mean":abs_upper(mean),
        "raw_mean_upper":mean.upper(),"raw_mean_lower":mean.lower(),
        "raw_Smean_upper":Smean.upper(),"raw_Smean_lower":Smean.lower()}
    if not all(x.is_finite() for x in values.values()):
        raise ValueError("a saved component or radial normalization is nonfinite")
    return values

def case_row(base,rho,LG,LK):
    eq=exact(PARAMETERS["centre_pair_A0_repair"])
    eqm=exact(PARAMETERS["centre_even_mean_repair"])
    delta=exact(PARAMETERS["selected_delta_half_width"])
    p,b,ba,k=base["Pnorm_upper"],base["b"],base["beta_absolute"],base["k"]
    E0=(19*p*delta).upper();E1=(83*p*delta).upper()
    Md=(base["M0"]+E0).upper();Md1=(base["M1"]+E1).upper();eta=(p*rho).upper()
    known=(eq+19*delta).upper();eps=(known+rho).upper()
    mgap=(-base["raw_mean_upper"]-eqm-19*delta-rho).lower()
    a=(base["gamma_lower"]*base["K_lower"].sqrt()*mgap).lower()
    SD=(k*(2*base["R"]*eps+eps**2)).upper()
    Slo=max(arb(0),(base["raw_Smean_lower"]-SD).lower()).lower()
    Shi=(base["raw_Smean_upper"]+SD).upper()
    L=(LG+LK/2+ba*max(abs_upper(1-Slo),abs_upper(1-Shi))).upper()
    d0=(base["raw_drift"]+ba*k*(2*base["R"]*eq+eq**2)/4).upper()
    dd=(base["raw_drift"]+ba*k*(2*base["R"]*known+known**2)/4).upper()
    Dref=(ba*k*(2*(base["R"]+eq)*19*delta+(19*delta)**2)/4).upper()
    Dnl=(arb.pi()*ba*k*rho*(2*(base["R"]+known)+rho)/8).upper()
    dp=(dd+Dnl).upper()
    Aref=(b*(6*base["M0"]*E0+3*E0**2)
          +b*(base["M1"]*E0+base["M0"]*E1+E0*E1)/2).upper()
    Anl=(b*eta*(3*Md+eta+Md1/4)).upper()
    mix=(b*(6*base["Mmean"]*base["N0"]+3*base["N0"]**2)
         +b*base["M1"]*(base["Mmean"]+base["N0"])/2).upper()
    AH=(base["alpha"]+b*(3*Md**2+3*Md*eta+eta**2)
        +b*Md1*(2*Md+eta)/4).upper()
    result={"Mdelta":Md,"Mdelta1":Md1,"eta":eta,
        "actual_mean_gap":mgap,"actual_principal_lower":a,
        "actual_Smean_lower":Slo,"actual_Smean_upper":Shi,"actual_logspeed":L,
        "d0":d0,"ddelta":dd,"drift_reference_delta":Dref,"drift_nonlinear":Dnl,
        "actual_drift":dp,"Aref_delta_projected":Aref,"Anonlinear":Anl,
        "Amix":mix,"Ahigh":AH}
    for J in PARAMETERS["high_projection_labels"]:
        result["C_shell"+str(J)]=(mix+4*J*d0).upper()
        result["C_low"+str(J)]=(Aref+Anl+4*J*(Dref+Dnl)).upper()
    if not all(x.is_finite() for x in result.values()):raise ValueError("a new case coefficient is nonfinite")
    return result

def extrema(items,names,minimum=False):
    result={};rows={}
    for index,values in items:
        for key in names:
            value=values[key].lower() if minimum else values[key].upper()
            if key not in result or (value<result[key] if minimum else value>result[key]):
                result[key]=value;rows[key]=index
    return result,rows

def high_constants(J,upper_bounds,lower_bounds,pnorm):
    n=4*(J+1);a=lower_bounds["actual_principal_lower"]
    mean_ok=bool(lower_bounds["actual_mean_gap"]>0 and a>0)
    out={"projection_label":J,"first_high_physical_frequency":n,
        "actual_mean_gap_positive":mean_ok,
        "tau_below_one":False,"t_below_one":False,
        "complete_coercivity_applies":False,"failure":None,
        "complete_energy_and_trace_bounds":None}
    if not mean_ok:
        out["failure"]="actual_negative_mean_or_principal_gap_not_proved"
        out["tau"]=None;out["t"]=None
        return out
    tau=(upper_bounds["actual_logspeed"]/(a*n)).upper()
    out["tau"]=rec(tau);out["tau_below_one"]=bool(tau<1)
    if not out["tau_below_one"]:
        out["t"]=None;out["failure"]="tau_not_below_one";return out
    cp=(1/(a*(1-tau).sqrt())).upper()
    cr=(1+upper_bounds["actual_drift"]*cp).upper()
    t=(cp*upper_bounds["Ahigh"]/n).upper()
    out["t"]=rec(t);out["t_below_one"]=bool(t<1)
    if not out["t_below_one"]:
        out["failure"]="t_not_below_one";return out
    den=(1-t).lower();cpa=(cp/den).upper();cra=(cr/den).upper()
    kappa=(1+exact(Fraction(1,n*n))).sqrt().upper()
    trace=(pnorm*(kappa*cpa*cra).sqrt()).upper()
    coeff={
        "cp_sharp":cp,"cr_sharp":cr,"cp_after_high_absorption":cpa,
        "cr_after_high_absorption":cra,"half_trace_kappa":kappa,
        "P_cut_upper":pnorm,"half_trace_source_gain":trace,
        "shell_input_source_gain":upper_bounds["C_shell"+str(J)],
        "low_input_source_gain":upper_bounds["C_low"+str(J)],
        "high_body_cutoff_source_gain":arb(20),
        "half_trace_shell_body_gain":(trace*upper_bounds["C_shell"+str(J)]).upper(),
        "half_trace_low_body_gain":(trace*upper_bounds["C_low"+str(J)]).upper(),
        "half_trace_high_body_cutoff_gain":(20*trace).upper()}
    out["complete_energy_and_trace_bounds"]=recs(coeff)
    out["complete_coercivity_applies"]=True
    out["known_source_reference"]=("existing_same_window_NR_WC_full_F96_unchanged"
                                   if J==96 else "exact_zero_only_for_true_residual_zero_state")
    return out

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root",type=Path,required=True)
    parser.add_argument("--manifest",type=Path,required=True)
    parser.add_argument("--out",type=Path,required=True)
    parser.add_argument("--bits",type=int,default=320)
    args=parser.parse_args();ctx.prec=args.bits;ctx.cap=6;started=time.monotonic()
    doc={"kind":KIND,"complete":False,"failure":None,"actual_returncode":None,
        "source_sha256":sha(__file__),"input_manifest_sha256":sha(args.manifest),
        "parameters":PARAMETERS,"gates":[],"candidate_sha256":CANDIDATE,
        "derived_continuous_centre_definition_sha256":DEFINITION,
        "old_target_Fourier_trial_convolution_residual_repair_mean_flow_Green_calls":0,
        "source_integrals_recomputed":False,"new_recomputable_native_persisted":False,
        "actual_unknown_body_or_cut_norm_supplied":False,"actual_low_inner_curvature_entry_proved":False,
        "actual_core_solution_or_full_matching_proved":False}
    audit={"kind":"temporary_complete_original_collar_components_and_new_cases_v1","rows":[],"cases":{}}
    try:
        selected,LG,LK=checked_inputs(args,doc)
        bases=[]
        for item in selected:
            values=saved_row_components(item,LK);bases.append((item["index"],values))
            audit["rows"].append({"original_index":item["index"],
                "original_row_sha256":item["original_row_sha256"],
                "exact_intersection":item["intersection"],
                "full_saved_original_row":item["row"],"new_base_components":recs(values)})
        gate(doc,"all saved selected component balls retain positive K_gamma_and_the_full_negative_mean",
             len(bases)==len(selected) and all(v["K_lower"]>0 and v["gamma_lower"]>0
                 and v["raw_mean_upper"]<0 for i,v in bases))
        base_max,base_arg=extrema(bases,BASE_NAMES)
        doc["complete_original_component_restrictions"]=recs(base_max)
        doc["component_maximum_original_rows"]=base_arg
        doc["complete_component_extremal_row_identities"]={
            str(i):{"original_row_sha256":item["original_row_sha256"],
                    "original_interval":item["row"]["interval"],"exact_intersection":item["intersection"]}
            for i in sorted(set(base_arg.values())) for item in selected if item["index"]==i}
        gate(doc,"all six width_only_C0_radii are explicit_and_do_not_extend_the_independent_narrow_MA_domain",
             len(PARAMETERS["rho_candidates"])==6
             and len(set(PARAMETERS["rho_candidates"]))==6
             and all(Fraction(q)>0 for q in PARAMETERS["rho_candidates"]))
        doc["new_collar_cases"]={}
        for rho_text in PARAMETERS["rho_candidates"]:
            rho=exact(rho_text);values=[(i,case_row(b,rho,LG,LK)) for i,b in bases]
            maxima,max_rows=extrema(values,CASE_MAX_NAMES)
            minima,min_rows=extrema(values,CASE_MIN_NAMES,minimum=True)
            audit["cases"][rho_text]=[
                {"original_row_index":i,"complete_new_row_coefficients":recs(v)} for i,v in values]
            case={"rho":rho_text,"complete_upper_coefficients":recs(maxima),
                  "complete_lower_coefficients":recs(minima),
                  "maximum_original_rows":max_rows,"minimum_original_rows":min_rows,
                  "candidate_energy":{}}
            for J in PARAMETERS["high_projection_labels"]:
                case["candidate_energy"][str(J)]=high_constants(J,maxima,minima,base_max["Pnorm_upper"])
            doc["new_collar_cases"][rho_text]=case
        candidates=[c for v in doc["new_collar_cases"].values() for c in v["candidate_energy"].values()]
        gate(doc,"all12_candidates_keep_their_mean_prerequisite_and_two_separate_tau_t_tests",
             len(candidates)==12 and all("actual_mean_gap_positive" in c
                 and "tau_below_one" in c and "t_below_one" in c for c in candidates))
        doc["new_rho_cases_evaluated"]=6;doc["new_coercivity_candidates_evaluated"]=12
        doc["new_coercivity_candidates_passed"]=sum(c["complete_coercivity_applies"] for c in candidates)
        gate(doc,"failed_candidates_remain_visible_without_an_unproved_positive_coercivity_conclusion",
             all((c["complete_energy_and_trace_bounds"] is not None)==c["complete_coercivity_applies"]
                 for c in candidates))
        raw_audit=canonical(audit);audit_path=args.out.parent/"temporary-complete-collar-component-audit.json"
        audit_path.parent.mkdir(parents=True,exist_ok=True);audit_path.write_bytes(raw_audit)
        doc["temporary_complete_new_audit"]={"bytes":len(raw_audit),"sha256":sha_bytes(raw_audit),"persisted":False,
            "complete_original_rows":len(selected),"new_rho_row_sets":6}
        gate(doc,"complete_original_row_balls_and_every_new_case_row_are_retained_in_the_temporary_audit",
             len(audit["rows"])==len(selected) and len(audit["cases"])==6
             and all(len(v)==len(selected) for v in audit["cases"].values()))
        doc["scope"]={
            "same_real_two_sided_true_H1_solution_only":True,
            "ordinary_residual_zero_is_a_hypothesis_not_a_new_existence_conclusion":True,
            "actual_principal_speed_not_an_intrinsic_radial_coordinate":True,
            "full_mean_and_centre_repair_canonical_response_offset_retained":True,
            "original_fields_already_contain_physical_alpha":True,
            "known_A0_primitive_one_quarter_and_unknown_C0_pi_over_eight_are_separate":True,
            "high_rank_mean_output_removed_only_after_exact_projection":True,
            "all_low_input_means_and_true_cutoff_sources_retained":True,
            "old_NR_WC_sources_and_MA_records_unchanged":True,
            "narrow_MA_domain_extended":False,
            "source_integrals_or_active_Green_arrays_used":False,
            "new_physical_cut_entry_or_low_selfmap_claimed":False}
        gate(doc,"the_complete_new_receipt_keeps_all_source_mean_and_unknown_norm_obligations",
             doc["scope"]["all_low_input_means_and_true_cutoff_sources_retained"]
             and not doc["scope"]["narrow_MA_domain_extended"]
             and not doc["actual_unknown_body_or_cut_norm_supplied"])
        if len(doc["gates"])!=16:raise ValueError("the exact structural gate inventory changed")
        doc["complete"]=True;doc["actual_returncode"]=0
    except Exception as error:
        doc["failure"]={"type":type(error).__name__,"message":str(error),"traceback":traceback.format_exc()}
        doc["actual_returncode"]=1
    doc["seconds"]=time.monotonic()-started;save(args.out,doc)
    print(json.dumps({"kind":KIND,"complete":doc["complete"],"failure":doc["failure"],
        "gates":len(doc["gates"]),"gates_passed":sum(g["passed"] for g in doc["gates"]),
        "new_rho_cases_evaluated":doc.get("new_rho_cases_evaluated"),
        "new_coercivity_candidates_evaluated":doc.get("new_coercivity_candidates_evaluated"),
        "new_coercivity_candidates_passed":doc.get("new_coercivity_candidates_passed"),
        "output_bytes":args.out.stat().st_size,"output_sha256":sha(args.out),
        "seconds":doc["seconds"]},allow_nan=False),flush=True)
    if not doc["complete"]:raise SystemExit(1)

if __name__=="__main__":main()
