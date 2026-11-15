#!/usr/bin/env python3
"""New weighted Q bounds from exact old cap rows and one scalar cubic slot.

Only the known mean polynomial receives a new Bernstein enclosure. Old targets,
complete convolutions, residual integrals and reference Riccati solves are reused.
Run new directed arithmetic only in the authorized public Actions job.
"""
from __future__ import annotations
import argparse
from bisect import bisect_right
from fractions import Fraction
import gzip
import hashlib
import io
import json
from pathlib import Path
import time
import traceback
import numpy as np
from flint import arb, ctx

TOPIC=Path("topics/visible-flex-exact-nearby")
KIND="actual_cached_weighted_cap_Q_joint_gate_v1"
CANDIDATE="ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
DEFINITION="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
OBJECT="91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848"
OLD_SOURCE="1292a1c06695d49a6f5e6bca27ad375b2fd82b44ebe1e6066327b7b7a79d882c"
OLD_NATIVE="ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d"
OLD_NATIVE_BYTES=6223338
CAP_SHA="ad6efc2a226131245ff4197a0b5da2843578224368a340f7a50d383c03a1819b"
INTRINSIC_SHA="3a89805ebe1ab22000529a7a8c2fdc262b1c3a2afbc52433cf610d2d6542ff22"
BACKGROUND_SHA="35db98d4124d50ef3bd69f3ec3aa6906289e3f6083c3ba91c8197da7547830ff"
ALPHA=Fraction(6890507429876859,9007199254740992)
NU=Fraction(-2572625729470897,72057594037927936)
ETA=Fraction(-7789843107295549,4611686018427387904)
LEFT,RIGHT=Fraction(9,10),Fraction(25,8)
POSITIVE_LEFT=Fraction("0.2384058742994")
SIGMA=Fraction(1,8192)
CANDIDATE_DIR="data/phase_transport_resume127_20261114/candidate/"
CANDIDATE_NAME="moving-m32-alpha0765-fullR-v2-tol2e9-candidate.json"
PART_NAME="moving-m32-alpha0765-fullR-v2-tol2e9-candidate-part004.npz.gz"
L1_FOLDER="notes/cached_cap_L1_endpoint_ci/run-43692857656-1-cached-cap-L1-reference-endpoint/"
L1_SOURCE="106ec9308882b814ca773da904e561e93aa4475f4f46f84b9632c9716653992f"
L1_MANIFEST="6378581473d45a1af2c55748ea13a5111a0563e4be183a0e56a5029f9c2021a5"
FILES={
 "parts":"notes/2026-11-14-R133-current-positive-complete-ac1-binary-parts.json",
 "cap":"notes/2026-11-14-R133-final-physical-cap-linear-module-r09-v2-native.json.gz",
 "background":"notes/2026-11-14-R133-continuous-repair-physical-cap-background-v2-native.json.gz",
 "candidate_index":CANDIDATE_DIR+CANDIDATE_NAME,
 "candidate_part004":CANDIDATE_DIR+PART_NAME,
 "L1_summary":L1_FOLDER+"actual-cap-L1-endpoint-summary.json",
 "L1_process":L1_FOLDER+"process.json"}
EXPECTED={
 "parts":"32b430a27a20726f095098902afdb93e656ea746eb81bce09a559e6f65787fd3",
 "cap":CAP_SHA,"background":BACKGROUND_SHA,"candidate_index":CANDIDATE,
 "candidate_part004":"314a6846ef2b5a257ddf20068332d105a7707b5aef27026f30477a47984eec4c",
 "L1_summary":"f5eea9a8a1b3f198e19c94a42cc3f794226b99cae65cefbd2e631134aff42c3a",
 "L1_process":"b782c9a2834df60b7e0961fff17d2dbaca0b96d965b042f1a4194545ebb9b2dc"}
PARAMETERS={
 "bits":320,"cap_interval":["9/10","25/8"],"physical_eta":str(ETA),
 "affine_parameter_offset":"0","original_parameter_half_width":"1/1000000000",
 "exact_nu":str(NU),"exact_alpha":str(ALPHA),"sigma":str(SIGMA),
 "mean_candidate_component":32,"candidate_modes":32,
 "raw_Q_B_labels":[-32,32],"raw_Q_C_labels":[-64,64],
 "physical_frequency_factor":4,"weighted_exponent":2,
 "inverse_displacement_original_width":"1/64","repair_original_width":"1/32",
 "requested_weighted_Q_upper":"1/100000","requested_endpoint_Q_gain_upper":"5",
 "nonlinear_body_radius":"3/1000000","nonmean_endpoint_radius":"99/100000000000",
 "true_outer_Z_radius":"1/1000000000","inner_nonmean_C_radius":"1/1000000000",
 "normalized_outer_height_radius":"1/1152921504606846976"}

def sha_bytes(raw):return hashlib.sha256(raw).hexdigest()
def sha(path):return sha_bytes(Path(path).read_bytes())
def exact(value):
    q=Fraction(value)
    return arb(q.numerator)/q.denominator
def b(r):return arb(r["lower"]).lower().union(arb(r["upper"]).upper())
def up(v):return abs(arb(v)).upper()
def rec(v):
    z=arb(v)
    if not z.is_finite():raise ValueError("a new weighted bound is nonfinite")
    return {"ball":z.str(90),"lower":z.lower().str(90),"upper":z.upper().str(90)}
def records(d):return {k:rec(v) for k,v in d.items()}
def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith(".gz") else raw)
def save(path,doc):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(doc,indent=2,allow_nan=False)+"\n").encode()
    temp=path.with_name(path.name+".tmp");temp.write_bytes(raw);temp.replace(path)
def gate(doc,name,ok):
    doc["gates"].append({"name":name,"passed":bool(ok)})
    if not ok:raise ValueError("gate failed: "+name)
def cover(rows,left,right,label):
    cursor=left
    for row in rows:
        lo,hi=map(Fraction,row["interval"])
        if lo!=cursor or not lo<hi:raise ValueError(label+" is not a complete exact closed partition")
        cursor=hi
    if cursor!=right:raise ValueError(label+" has the wrong exact last endpoint")

def original_positive(root,doc):
    path=root/TOPIC/FILES["parts"];index=read(path)
    gate(doc,"exact_original_four_parts_and_complete4650_identity",
        index["kind"]=="complete_native_lossless_container_binary_parts_v2"
        and index["native_complete"] is True and index["native_failure"] is None
        and index["native_kind"]=="complete_current_moving_positive_body_coefficients_v1"
        and index["complete_native_rows"]==4650 and index["original_bytes"]==OLD_NATIVE_BYTES
        and index["original_sha256"]==OLD_NATIVE and index["original_source_sha256"]==OLD_SOURCE
        and index["candidate_sha256"]==CANDIDATE and len(index["parts"])==4)
    chunks=[];cursor=0;receipts=[]
    for i,r in enumerate(index["parts"]):
        if r["index"]!=i or r["offset"]!=cursor or Path(r["file"]).name!=r["file"]:
            raise ValueError("an original byte-part path or offset differs")
        raw=(path.parent/r["file"]).read_bytes()
        if len(raw)!=r["compressed_bytes"] or sha_bytes(raw)!=r["compressed_sha256"]:
            raise ValueError("an original compressed part differs")
        payload=gzip.decompress(raw)
        if len(payload)!=r["bytes"] or sha_bytes(payload)!=r["sha256"]:
            raise ValueError("an original part payload differs")
        chunks.append(payload);cursor+=len(payload)
        receipts.append({k:r[k] for k in ("index","file","offset","bytes","sha256",
                                          "compressed_bytes","compressed_sha256")})
    raw=b"".join(chunks)
    if len(raw)!=OLD_NATIVE_BYTES or sha_bytes(raw)!=OLD_NATIVE:
        raise ValueError("the complete original4650 container changed")
    d=json.loads(gzip.decompress(raw));ident=d["identity"]
    gate(doc,"whole_original4650_moving_phi_parameter_and_complete_mean",
        d["kind"]=="complete_current_moving_positive_body_coefficients_v1"
        and d["complete"] is True and d["coefficient_cover_complete"] is True
        and d["failure"] is None and not d["pending"] and len(d["rows"])==4650
        and d["whole_original_eta"] and d["full_original_primitive_tail"]
        and ident["source_sha256"]==OLD_SOURCE and ident["candidate_sha256"]==CANDIDATE
        and ident["object_sha256"]==OBJECT and ident["cap_cache_sha256"]==INTRINSIC_SHA
        and Fraction(ident["exact_eta_center"])==ETA
        and Fraction(ident["parameter_half_width"])==Fraction(1,10**9)
        and Fraction(ident["actual_alpha"])==ALPHA and Fraction(ident["actual_nu"])==NU
        and ident["modes"]==32 and Fraction(ident["left"])==POSITIVE_LEFT
        and Fraction(ident["right"])==RIGHT)
    cover(d["rows"],POSITIVE_LEFT,RIGHT,"original4650")
    doc["original_restoration"]={"manifest_sha256":EXPECTED["parts"],"container_sha256":OLD_NATIVE,
        "container_bytes":len(raw),"parts":receipts,"new_parts_created":False,
        "original_mathematics_executed":False}
    return d

def candidate_mean_part(root,doc):
    index=read(root/TOPIC/FILES["candidate_index"]);meta=index["metadata"]
    gate(doc,"original_ac1_exact_mean_slot_and_candidate_parameters",
        index["kind"]=="complete_lossless_radial_cubic_shards_v1"
        and index["polynomial_order"]=="numpy/scipy PPoly descending local powers"
        and index["coefficient_shape"]==[4,6144,65] and index["radial_nodes_count"]==6145
        and meta["object_sha256"]==OBJECT and meta["modes"]==32
        and meta["physical_frequency_factor"]==4 and meta["finite_state_angle"]=="moving phi"
        and Fraction(meta["exact_float_amplitude"])==ALPHA
        and Fraction(meta["exact_float_nu"])==NU)
    cursor=0;last=Fraction(0)
    for r in index["parts"]:
        lo,hi=Fraction.from_float(float(r["radial_left"])),Fraction.from_float(float(r["radial_right"]))
        if r["first_interval"]!=cursor or lo!=last or not lo<hi:
            raise ValueError("original candidate index has a gap or an altered interval ordering")
        cursor=r["last_interval_exclusive"];last=hi
    if cursor!=6144 or last!=RIGHT:raise ValueError("original candidate index is incomplete")
    part=index["parts"][4]
    if (len(index["parts"])!=5 or part["file"]!=PART_NAME
        or part["sha256"]!=EXPECTED["candidate_part004"] or part["bytes"]!=1532492
        or part["first_interval"]!=5384 or part["last_interval_exclusive"]!=6144):
        raise ValueError("the only original candidate shard needed here changed")
    raw=(root/TOPIC/FILES["candidate_part004"]).read_bytes()
    if len(raw)!=part["bytes"]:raise ValueError("candidate part004 byte count differs")
    with np.load(io.BytesIO(gzip.decompress(raw)),allow_pickle=False) as z:
        if set(z.files)!={"radial_nodes","piece_coefficients"}:
            raise ValueError("unexpected original candidate array schema")
        nodes=z["radial_nodes"].copy();coeff=z["piece_coefficients"].copy()
    if (nodes.dtype!=np.dtype("float64") or coeff.dtype!=np.dtype("float64")
        or nodes.shape!=(761,) or coeff.shape!=(4,760,65)
        or not np.isfinite(nodes).all() or not np.isfinite(coeff).all()):
        raise ValueError("original candidate part004 shape, type or finite gate differs")
    nodes=[Fraction.from_float(float(v)) for v in nodes]
    if (nodes[0]!=Fraction(25,32) or nodes[-1]!=RIGHT
        or any(not a<c for a,c in zip(nodes,nodes[1:]))):
        raise ValueError("candidate exact closed knots differ")
    # Read only the one original scalar mean slot into exact rational arithmetic.
    mean=[[Fraction.from_float(float(coeff[k,i,32])) for k in range(4)] for i in range(760)]
    gate(doc,"original_part004_contains_the_entire_true_cap_with_full_mean",
         nodes[0]<LEFT and nodes[-1]==RIGHT)
    doc["candidate_original_shards_read"]=1
    doc["candidate_original_part004_sha256"]=EXPECTED["candidate_part004"]
    doc["candidate_scalar_component_newly_enclosed"]=32
    return nodes,mean

def inputs(a,doc):
    for name,path in FILES.items():
        if sha(a.root/TOPIC/path)!=EXPECTED[name]:
            raise ValueError("immutable original input changed: "+name)
    positive=original_positive(a.root,doc)
    cap=read(a.root/TOPIC/FILES["cap"]);bg=read(a.root/TOPIC/FILES["background"])
    l1=read(a.root/TOPIC/FILES["L1_summary"]);process=read(a.root/TOPIC/FILES["L1_process"])
    gate(doc,"same_all_mode_cap_reference_and_complete_global_mode_envelopes",
        cap["kind"]=="actual_final_physical_cap_linear_module_v1" and cap["complete"] is True
        and cap["candidate_sha256"]==CANDIDATE and cap["object_sha256"]==OBJECT
        and cap["cap_cache_sha256"]==INTRINSIC_SHA
        and Fraction(cap["exact_alpha"])==ALPHA and Fraction(cap["exact_nu"])==NU
        and Fraction(cap["exact_eta_center"])==ETA
        and Fraction(cap["parameter_half_width"])==Fraction(1,10**9)
        and cap["whole_original_eta"] and cap["complete_primitive_tail"]
        and cap["complete_unknown_Fourier_modes"]
        and cap["exact_interval"]==["9/10","25/8"] and cap["candidate_modes"]==32
        and len(cap["reference_rows"])==cap["native_reference_rows"]==949
        and len(cap["closed_cover"])==cap["complete_closed_intersections"]==1346)
    cover(cap["reference_rows"],LEFT,RIGHT,"original949reference")
    cover(cap["closed_cover"],LEFT,RIGHT,"original1346closedcover")
    envelopes=cap["complete_coefficient_suprema"]
    if len(envelopes["Q_B_imaginary"])!=65 or len(envelopes["Q_C_real"])!=129:
        raise ValueError("the complete original two-sided coefficient lists differ")
    gate(doc,"same_continuous_repair_and_actual_inverse_angle_domain",
        bg["kind"]=="actual_continuous_repair_physical_cap_and_residual_conjugation_v1"
        and bg["complete"] is True and all(g["passed"] for g in bg["gates"])
        and bg["original_candidate_sha256"]==CANDIDATE
        and bg["derived_definition_sha256"]==DEFINITION and bg["object_sha256"]==OBJECT
        and bg["cap_input_sha256"]==CAP_SHA and bg["positive_input_sha256"]==OLD_NATIVE
        and bg["exact_interval"]==["9/10","25/8"]
        and bg["whole_original_eta_for_background_transfer"]
        and Fraction(bg["background_parameter_half_width"])==Fraction(1,10**9)
        and bg["real_continuous_repaired_centre"] and not bg["original_ac1_native_silently_relabelled"])
    gate(doc,"actual_completed_L1_process_summary_and_all12_gates_reused",
        process["kind"]=="actual_public_cached_cap_L1_reference_endpoint_process_v1"
        and process["repository"]=="Rogerhu12/math-research-public"
        and str(process["run_id"])=="43692857656" and str(process["run_attempt"])=="1"
        and process["actual_source_sha256"]==L1_SOURCE
        and process["input_manifest_sha256"]==L1_MANIFEST
        and process["actual_scientific_summary_sha256"]==EXPECTED["L1_summary"]
        and any(c["label"]=="cached_cap_L1_and_reference_endpoint_sources"
                and c.get("actual_returncode")==0 for c in process["children"])
        and l1["kind"]=="actual_cached_cap_L1_and_reference_endpoint_sources_v1"
        and l1["complete"] is True and l1["failure"] is None and l1["source_sha256"]==L1_SOURCE
        and len(l1["gates"])==12 and all(g["passed"] for g in l1["gates"])
        and l1["parameters"]["physical_eta"]==str(ETA)
        and l1["parameters"]["exact_alpha"]==str(ALPHA)
        and l1["parameters"]["exact_nu"]==str(NU)
        and l1["inputs"]["cap"]==CAP_SHA and l1["inputs"]["background"]==BACKGROUND_SHA
        and l1["original_complete_residual_rows"]==7296
        and l1["selected_cap_residual_rows"]==1341
        and l1["original_reference_closed_intersections"]==1346
        and l1["old_targets_residual_enclosures_reference_ODE_and_primitive_recomputed"]==0)
    nodes,mean=candidate_mean_part(a.root,doc)
    rows=[]
    for i,r in enumerate(positive["rows"]):
        lo,hi=map(Fraction,r["interval"])
        if hi<=LEFT or lo>=RIGHT:continue
        if (r["intrinsic_provenance"]["kind"]!="same_intrinsic_cap_v2"
            or not r["complete_mean_column_retained"]
            or not r["fields_are_moving_phi_not_physical_theta"]
            or r["complete_finite_modes"]!=32 or r["exact_local_band"]!=64):
            raise ValueError("selected cap row lost its original complete coefficient identity")
        piece=r["candidate_piece"]-5384
        if not 0<=piece<760:raise ValueError("selected cap row is outside original part004")
        germ=list(map(Fraction,r["actual_candidate_germ"]))
        if germ!=nodes[piece:piece+2] or not germ[0]<=lo<hi<=germ[1]:
            raise ValueError("the old row and original candidate germ do not agree")
        scalar=list(map(Fraction,r["actual_scalar_germ"]))
        if not scalar[0]<=lo<hi<=scalar[1]:raise ValueError("old true scalar germ is incomplete")
        rows.append({"interval":[str(max(lo,LEFT)),str(min(hi,RIGHT))],
                     "original_index":i,"row":r,"part_piece":piece})
    cover(rows,LEFT,RIGHT,"selected original4650cap")
    doc["inputs"]={**EXPECTED,"restored_complete_positive_native":OLD_NATIVE}
    doc["original_complete_positive_rows"]=4650
    doc["selected_positive_cap_rows"]=len(rows)
    doc["original_reference_rows"]=949
    doc["original_reference_closed_intersections"]=1346
    return rows,cap,bg,l1,nodes,mean

def mean_Bernstein(mean,nodes,piece,left,right):
    """Exact binary64 cubic, first affine-restricted, then exact cubic Bernstein."""
    if not nodes[piece]<=left<right<=nodes[piece+1]:
        raise ValueError("new mean scalar domain crossed its exact old cubic piece")
    c3,c2,c1,c0=mean[piece];x=left-nodes[piece];h=right-left
    d0=c0+c1*x+c2*x*x+c3*x*x*x
    d1=h*(c1+2*c2*x+3*c3*x*x)
    d2=h*h*(c2+3*c3*x);d3=h*h*h*c3
    controls=(d0,d0+d1/3,d0+2*d1/3+d2/3,d0+d1+d2+d3)
    q=max(abs(x) for x in controls)*abs(ALPHA)
    return exact(q).upper(),[str(x) for x in controls]

def physical_constants(bg,doc):
    v={k:b(r) for k,r in bg["bounds"].items()}
    hstar=v["actual_inverse_displacement_A_1over64"].upper()
    # The pinned original producer constructs U and V on moving width1/32;
    # their output names describe the subsequently allowed physical width.
    E=v["repair_joint_A_1over32"].upper()
    U=v["physical_U_A_1over64"].upper();V=v["physical_v_A_1over64"].upper()
    K=v["actual_K_abs"].upper()
    gate(doc,"same_joint_raw_width_repair_and_inverse_composition_margin",
        hstar>=0 and hstar+exact(SIGMA)<exact(Fraction(1,64))
        and E>=0 and E<exact(Fraction(4832,10**21))
        and U>=0 and U<exact(Fraction(1,50)) and V>=0 and V<6 and K>0)
    dB=(2*E).upper()
    dC=(2*U*E+E*E+K*(2*V*E+E*E)).upper()
    const={"hstar":hstar,"sigma":exact(SIGMA),"moving_required_width":(hstar+exact(SIGMA)).upper(),
           "repair_joint_A_1over32":E,"raw_joint_U_A_1over32_bound":U,
           "raw_joint_v_A_1over32_bound":V,"global_K_abs":K,
           "weighted_Q_B_repair_fee":dB,"weighted_Q_C_repair_fee":dC}
    doc["physical_and_repair_constants"]=records(const)
    return const

def weighted_rows(rows,cap,nodes,mean,const,doc):
    refs=cap["reference_rows"]
    pleft=[Fraction(r["interval"][0]) for r in rows]
    rleft=[Fraction(r["interval"][0]) for r in refs]
    edges=sorted({LEFT,RIGHT,
        *[Fraction(x) for r in rows for x in r["interval"]],
        *[Fraction(x) for r in refs for x in r["interval"]],
        *[Fraction(x) for r in cap["closed_cover"] for x in r["interval"]],
        *[x for x in nodes if LEFT<x<RIGHT]})
    qb=[up(b(x)) for x in cap["complete_coefficient_suprema"]["Q_B_imaginary"]]
    qc=[up(b(x)) for x in cap["complete_coefficient_suprema"]["Q_C_real"]]
    if not all(x.is_finite() and x>=0 for x in qb+qc):
        raise ValueError("the original global per-mode envelope is invalid")
    maxima=[[arb(0) for _ in qb],[arb(0) for _ in qc]]
    maximizing=[[-1]*len(qb),[-1]*len(qc)]
    suffix=arb(0);saved=[]
    for i in range(len(edges)-2,-1,-1):
        left,right=edges[i],edges[i+1]
        ip,ir=bisect_right(pleft,left)-1,bisect_right(rleft,left)-1
        pr,rr=rows[ip],refs[ir];r=pr["row"]
        if not (Fraction(pr["interval"][0])<=left<right<=Fraction(pr["interval"][1])
            and Fraction(rr["interval"][0])<=left<right<=Fraction(rr["interval"][1])):
            raise ValueError("common exact cap cell crossed an original closed row")
        U=up(b(r["bounds"]["U_A0"]));Vne=up(b(r["bounds"]["V_nonmean_A0"]))
        K=up(b(r["intrinsic"]["K"]));Cref=b(r["intrinsic"]["Cref"])
        sc=b(rr["bounds"]["C_rate"]).lower()
        if not Cref<0 or not sc>0:raise ValueError("old exact positive damping or reference sign failed")
        mean_bound,controls=mean_Bernstein(mean,nodes,pr["part_piece"],left,right)
        Dv=(mean_bound+Vne).upper()
        s=up(1/Cref)
        LB=(2*U).upper()
        LC=(U*U+K*(2*s*Dv+Dv*Dv)).upper()
        w=(-2*suffix).exp().upper()
        for channel,(envelopes,total) in enumerate(((qb,LB),(qc,LC))):
            for k,global_bound in enumerate(envelopes):
                candidate=(w*min(global_bound,total)).upper()
                if candidate>maxima[channel][k]:
                    maxima[channel][k]=candidate;maximizing[channel][k]=i
        saved.append({"index":i,"interval":[str(left),str(right)],
            "original_positive_index":pr["original_index"],"original_reference_index":ir,
            "original_candidate_piece":r["candidate_piece"],
            "actual_candidate_germ":r["actual_candidate_germ"],"actual_scalar_germ":r["actual_scalar_germ"],
            "exact_normalized_mean_Bernstein_controls":controls,
            "bounds":records({"C_rate_lower":sc,"S_at_right_lower":suffix,
                 "w_at_right_upper":w,"new_abs_alpha_mean":mean_bound,
                 "old_U_A0":U,"old_V_nonmean_A0":Vne,"old_abs_Cref_inverse":s,
                 "old_K_abs":K,"full_Dv_A0":Dv,"Q_B_row_total":LB,"Q_C_row_total":LC})})
        suffix=(suffix+sc*exact(right-left)).lower()
    saved.reverse()
    cover(saved,LEFT,RIGHT,"new exact common weighted partition")
    mode_records=[];raw=[]
    for channel,(first,label,global_bounds) in enumerate(((-32,"Q_B",qb),(-64,"Q_C",qc))):
        total=arb(0);modes=[]
        for offset,value in enumerate(maxima[channel]):
            k=first+offset
            weight=(abs(4*k)*const["moving_required_width"]).exp().upper()
            contribution=(value*weight).upper();total+=contribution
            modes.append({"label":k,"physical_frequency":4*k,
                "maximizing_common_index":maximizing[channel][offset],
                "bounds":records({"global_raw_envelope":global_bounds[offset],
                    "weighted_radial_mode_upper":value,"angular_weight":weight,
                    "weighted_joint_contribution":contribution})})
        raw.append(total.upper());mode_records.append({"channel":label,"modes":modes})
    repaired=[(raw[0]+const["weighted_Q_B_repair_fee"]).upper(),
              (raw[1]+const["weighted_Q_C_repair_fee"]).upper()]
    doc["common_weighted_rows"]=saved
    doc["per_mode_radial_maxima_before_angular_sum"]=mode_records
    doc["complete_common_cap_cells"]=len(saved)
    doc["new_scalar_mean_Bernstein_domains"]=len(saved)
    doc["bounds"]=records({"raw_weighted_Q_B_after_same_inverse":raw[0],
        "raw_weighted_Q_C_after_same_inverse":raw[1],
        "repaired_physical_weighted_Q_B_A_sigma":repaired[0],
        "repaired_physical_weighted_Q_C_A_sigma":repaired[1],
        "maximum_repaired_physical_weighted_Q_A_sigma":max(repaired).upper(),
        "new_common_integrated_C_rate_lower":suffix})
    gate(doc,"complete_per_mode_radial_max_before_full_two_sided_sum",
        len(mode_records[0]["modes"])==65 and len(mode_records[1]["modes"])==129
        and all(v.is_finite() and v>=0 for v in raw+repaired))
    return repaired

def scalar_compatibility(cap,l1,repaired,doc):
    cb={k:b(v) for k,v in cap["bounds"].items()}
    old={k:b(v) for k,v in l1["bounds"].items()}
    Tdc=old["reference_C_R_from_right_d_gain"].upper()
    T=cb["triangular_coupling"].upper();q=cb["q_upper"].upper();KC=cb["K_C"].upper()
    Ke=(Tdc*T+(1+q*Tdc)*KC).upper()
    doc["bounds"].update(records({"actual_original_Tdc_reused":Tdc,
        "actual_original_triangular_coupling":T,"actual_original_q_upper":q,
        "actual_original_K_C":KC,"complete_unweighted_Q_endpoint_gain":Ke}))
    gate(doc,"full_reference_Q_endpoint_gain_below5_without_new_reference_solve",Ke<5)
    factor=(384*exact(SIGMA)).exp().upper()
    finite_endpoint_factor=(512*exact(SIGMA)).exp().upper()
    gate(doc,"finite_known_source_small_strip_factors_only",
        factor<exact(Fraction(21,20)) and finite_endpoint_factor<exact(Fraction(16,15)))
    outer=[r for r in l1["candidate_larger_outer_ball_diagnostics"]
           if r["Z_radius"]=="1/1000000000"]
    gate(doc,"same_actual_complete_larger_outer_ball_and_mean_derivatives",
        len(outer)==1 and outer[0]["true_long_background_domain_and_image_passed"]
        and outer[0]["full_even_Cmean_retained"])
    ob={k:b(v) for k,v in outer[0]["bounds"].items()}
    TZ=ob["D_Z_d"].upper();chi=ob["complete_body_linear_and_outer_coefficient"].upper()
    gate(doc,"same_complete_outer_derivative_and_body_scalar_margins",
        TZ<exact(Fraction(6,1000)) and chi<exact(Fraction(879,1000))
        and Tdc*TZ<exact(Fraction(1,200)))
    doc["bounds"].update(records({"small_strip_known_source_factor":factor,
        "small_strip_finite_endpoint_factor":finite_endpoint_factor,
        "reused_complete_outer_DZ_d":TZ,"reused_complete_body_linear_and_outer_coefficient":chi}))
    # Additional endpoint-tail scalar checks are filled from the pinned theorem;
    # no new endpoint moments, Fourier samples or source integration is executed.
    scalar_endpoint_tail(cap,l1,old,cb,factor,finite_endpoint_factor,Ke,repaired,doc)
    gate(doc,"actual_repaired_weighted_physical_Q_joint_gate_below_1e_minus5",
        max(repaired)<exact(Fraction(1,100000)))

def scalar_endpoint_tail(cap,l1,old,cb,factor,finite_endpoint_factor,Ke,repaired,doc):
    """Only scalar consequences of original F9--20 and the completed L1 run."""
    original_strip=exact(Fraction(1,8));old_U=exact(Fraction(1643190,10**15))
    old_P=exact(Fraction(1480385,10**17));mean_gap=exact(Fraction(29,5))
    d=(original_strip-old_P).lower()
    x=(-4*(d-exact(SIGMA))).exp().upper()
    gate(doc,"same_original_F12_analytic_tail_has_positive_shifted_strip",
         d>exact(SIGMA) and x>0 and x<exact(Fraction(2,3)))
    J=128
    tail_C=(8*old_P/mean_gap*x**(J+1)*((J+1)-J*x)/(1-x)**2).upper()
    tail_B=(2*old_U/mean_gap*x**(J+1)/(1-x)).upper()
    gate(doc,"complete_both_physical_Fourier_tails_at_small_sigma_below_1e_minus30",
         tail_B>=0 and tail_C>=0 and tail_B+tail_C<exact(Fraction(1,10**30)))
    # Original total bounds already include all finite alias and multiplier fees.
    # Applying the finite weight to the whole old total only overcounts old tails.
    # New full tails are additionally retained, never obtained by subtraction.
    old_regular=exact(Fraction(1256750,10**21))
    old_Z=exact(Fraction(2532986,10**19))
    comparison=cb["historical_to_current_outer_q_comparison"].upper()
    gate(doc,"original_actual_regular_multiplier_comparison_retained",comparison<arb(2)**-500)
    regular_sigma=(finite_endpoint_factor*old_regular+tail_B+tail_C
                   +comparison*(finite_endpoint_factor*old_Z+tail_C)).upper()
    raw_Z_sigma=(finite_endpoint_factor*old_Z+tail_C).upper()
    const={k:b(v) for k,v in doc["physical_and_repair_constants"].items()}
    physical={k:b(v) for k,v in l1["physical_source_constants"].items()}
    E=const["repair_joint_A_1over32"].upper()
    C,B,Ct,Bt=[physical[k].upper() for k in ("C","B","Ctheta","Btheta")]
    # Complete first differential D_Psi along the already enclosed repair path.
    # Current reflection makes its weighted primitive constant exactly zero;
    # the independent even mean is retained below.
    delta_B=((C+B*C+Bt*C/4)*E).upper()
    delta_C=((C*C+Ct*C/4)*E).upper()
    bg=read(Path(doc["_input_root"])/TOPIC/FILES["background"])
    delta_Cmean=up(b(bg["bounds"]["outer_even_mean_change"]))
    Z0=(raw_Z_sigma+delta_C).upper()
    zsmall=exact(Fraction(1,10**12));height=arb(2)**-60;eps=arb(2)**-256
    rf=10*(zsmall+height);F=rf+height;kappa=36*(arb(2)**12)*F
    image=9*zsmall+eps*height+9*(arb(2)**12)*F*F
    gate(doc,"same_smaller_true_long_graph_contains_repaired_small_strip_endpoint",
         Z0<zsmall and kappa<1 and image<rf and 2*F<arb(2)**-25 and 6*F<arb(2)**-20)
    # S10--13/F18--20 are Banach-algebra and diagonal-kernel statements.
    # The same positive angular weight keeps their complete modes and means.
    true_long_d=(eps*zsmall+eps*height+(arb(2)**14)*F*F).upper()
    true_long_Cmean=((arb(2)**11)*F*F).upper()
    rD=(regular_sigma+delta_B+delta_C+true_long_d).upper()
    rC0=(exact(Fraction(6055,10**46))+delta_Cmean+true_long_Cmean).upper()
    gate(doc,"complete_true_repaired_R_loads_and_independent_even_mean_at_small_sigma",
         Z0<exact(Fraction(3,10**13)) and rD<exact(Fraction(2,10**15))
         and rC0<exact(Fraction(205,10**21)))
    gamma=exact(Fraction(1,10**9))
    Tdc=old["reference_C_R_from_right_d_gain"].upper()
    HD=cb["outer_nonzero_d_port"].upper();HC=cb["inner_C_port"].upper()
    eta=(factor*old["unclosed_reference_body_pair"].upper()+HC*gamma+HD*rD+rC0).upper()
    endpoint=(factor*old["reference_C_nonmean_R_from_known_body"].upper()
              +old["reference_C_R_from_left_C_gain"].upper()*gamma+Tdc*rD).upper()
    gate(doc,"all_reused_sources_and_affine_ports_have_the_stated_small_strip_margins",
         HD<10 and HC<3 and eta<exact(Fraction(323,10**9))
         and endpoint<exact(Fraction(3,10**14)))
    rho=exact(Fraction(3,10**6));zeta=exact(Fraction(99,10**11))
    rZ=exact(Fraction(1,10**9));chi=exact(Fraction(879,1000))
    body_image=(exact(Fraction(323,10**9))+chi*rho+208*rho*rho).upper()
    body_lip=(chi+416*rho).upper()
    conditional_endpoint=(exact(Fraction(3,10**14))
        +exact(Fraction(1,10000))*rho+65*rho*rho+zeta/200).upper()
    actual_coefficient_endpoint=(endpoint+2*Ke*max(repaired)*rho
        +13*Ke*rho*rho+zeta/200).upper()
    gate(doc,"fixed_rational_conditional_body_and_endpoint_margins_with_both_means",
         Z0+zeta<rZ and body_image<exact(Fraction(99,100))*rho
         and body_lip<exact(Fraction(881,1000))
         and conditional_endpoint<exact(Fraction(9,10))*zeta)
    doc["bounds"].update(records({"original_endpoint_strip":original_strip,
        "original_endpoint_U_strip_upper":old_U,"original_endpoint_P_strip_upper":old_P,
        "original_endpoint_mean_abs_lower":mean_gap,"shifted_full_tail_ratio":x,
        "full_physical_B_tail_at_sigma":tail_B,"full_physical_C_tail_at_sigma":tail_C,
        "old_true_regular_line_at_sigma":regular_sigma,"raw_Z_at_sigma":raw_Z_sigma,
        "complete_repair_B_change_at_sigma":delta_B,"complete_repair_C_change_at_sigma":delta_C,
        "complete_repair_even_mean_change":delta_Cmean,
        "repaired_Z0_at_sigma":Z0,"complete_true_right_d_load_at_sigma":rD,
        "complete_true_right_Cmean_load":rC0,"complete_known_body_affine_at_sigma":eta,
        "complete_known_nonmean_endpoint_at_sigma":endpoint}))
    doc["scalar_conditional_margins"]={
        "conditional_on_actual_weighted_Q_gate":True,
        "full_nonlinear_cap_existence_claimed_by_this_consumer":False,
        "bounds":records({"rho":rho,"zeta":zeta,"true_outer_Z_radius":rZ,
            "body_image_upper":body_image,"body_Lipschitz_upper":body_lip,
            "conditional_endpoint_image_upper":conditional_endpoint,
            "endpoint_image_using_actual_weighted_coefficient":actual_coefficient_endpoint})}

def small_summary(doc):
    keep=("kind","complete","failure","source_sha256","parameters","inputs","seconds","gates",
        "original_complete_positive_rows","selected_positive_cap_rows","original_reference_rows",
        "original_reference_closed_intersections","candidate_original_shards_read",
        "candidate_original_part004_sha256","candidate_scalar_component_newly_enclosed",
        "complete_common_cap_cells","new_scalar_mean_Bernstein_domains",
        "physical_and_repair_constants","bounds","scalar_conditional_margins","scope",
        "old_target_and_full_coefficient_convolutions_recomputed","old_L1_integrals_recomputed",
        "old_reference_Riccati_recomputed","new_recomputable_data_persisted")
    out={k:doc[k] for k in keep if k in doc}
    if "per_mode_radial_maxima_before_angular_sum" in doc:
        out["largest_mode_contributions"]=[]
        for group in doc["per_mode_radial_maxima_before_angular_sum"]:
            selected=sorted(group["modes"],key=lambda r:up(b(r["bounds"]["weighted_joint_contribution"])),
                            reverse=True)[:6]
            out["largest_mode_contributions"].append({"channel":group["channel"],
                "modes":[{"label":r["label"],"maximizing_common_index":r["maximizing_common_index"],
                          "weighted_joint_contribution":r["bounds"]["weighted_joint_contribution"]}
                         for r in selected]})
    return out

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root",type=Path,required=True);p.add_argument("--out",type=Path,required=True)
    p.add_argument("--summary",type=Path,required=True)
    a=p.parse_args();ctx.prec=PARAMETERS["bits"];ctx.cap=6
    if a.out.exists() or a.summary.exists():raise FileExistsError("preserve every actual mathematical attempt")
    start=time.monotonic()
    d={"kind":KIND,"complete":False,"failure":None,"source_sha256":sha(__file__),
       "parameters":PARAMETERS,"gates":[],
       "old_target_and_full_coefficient_convolutions_recomputed":0,
       "old_L1_integrals_recomputed":0,"old_reference_Riccati_recomputed":0,
       "new_recomputable_data_persisted":False,
       "scope":{"fixed_eta0":True,"fixed_repaired_M32_delta0":True,
           "full_even_mean":True,"full_two_sided_known_coefficient_support":True,
           "per_mode_radial_max_before_sum":True,"same_repaired_inverse_angle":True,
           "unknown_Fourier_modes_truncated":False,"raw_ac1_relabelled_as_repaired":False,
           "only_weighted_coefficient_and_scalar_compatibility_gates":True,
           "complete_nonlinear_endpoint_invariance_proved":False,
           "complete_nonlinear_cap_solution_proved":False,"whole_infinite_BVP_inverse_proved":False}}
    try:
        d["_input_root"]=str(a.root)
        rows,cap,bg,l1,nodes,mean=inputs(a,d)
        constants=physical_constants(bg,d)
        repaired=weighted_rows(rows,cap,nodes,mean,constants,d)
        scalar_compatibility(cap,l1,repaired,d)
        d["complete"]=True
    except Exception as e:
        d["failure"]={"type":type(e).__name__,"message":str(e),"traceback":traceback.format_exc()}
    finally:
        d.pop("_input_root",None)
        d["seconds"]=time.monotonic()-start;save(a.out,d)
        s=small_summary(d);s["temporary_full_output_sha256"]=sha(a.out)
        s["temporary_full_output_bytes"]=a.out.stat().st_size
        raw=(json.dumps(s,indent=2,allow_nan=False)+"\n").encode()
        if len(raw)>60000:raise ValueError("genuine weighted cap conclusion exceeds60000 UTF8 bytes")
        save(a.summary,s);print(json.dumps(s,allow_nan=False),flush=True)
    if not d["complete"]:raise RuntimeError("actual new weighted cap gate failed; small evidence retained")

if __name__=="__main__":main()
