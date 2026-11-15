#!/usr/bin/env python3
"""New waist scalar fees from two saved first rows; no old scientific calls."""
from __future__ import annotations
import argparse
import gzip
import hashlib
import importlib.metadata
import json
import platform
import time
import traceback
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx

PUBLIC="Rogerhu12/math-research-public"
REL="topics/visible-flex-exact-nearby/"
PRODUCER=REL+"scripts/fourfold_codazzi_waist_normalizer_coefficients.py"
KIND="actual_waist_normalizer_coefficients_and_two_window_gates_v1"
MANIFEST_KIND="waist_normalizer_coefficients_public_inputs_v1"
RUNTIME={"Python":"3.12.14","python_flint":"0.9.0"}
GATE_COUNT=20
CANDIDATE="ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413"
CENTRE="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
DIRECTION="6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
RESPONSE="ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6"
OBJECT="91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848"
BODY_SOURCE="1651f6cf73af9f3c16061767cc5acff0c452ada183422f7efb983ec8a6d4eb07"
BODY_OPERATOR="09807e405455b58c043a5ff26b7ff5e4e1569a96c81ecd860125552bfba95a3b"
FOURIER_NORMS="18de4ef746eed069a9a92ba783d54e2f394887866d60cbb286502b9c55cb17c5"
BODY_SHA="feb3bbf9294dc995b88f5dc7c1e2ba866d3bd8c22dc84834dda7591cc9f644f0"
BODY_BYTES=8201
RAW_SHA="6f52030b7954f049a8e42a5a513a1f69b553819065b0c8b2245fa173e514cbb1"
RAW_BYTES=4592623
RAW_SOURCE="24ec0bf2b9d2b03ebfa07f4b39b8fdee3277f8e4b2aa14385c267122e6b8e81f"
RAW_PRODUCER="98eb7034038d76a341e112927cff4bcb7bfd425bc56698305803a689060ac31e"
D_SOURCE="827fcb237a79b48c095872b61c370ff2ceafc143a8dc6a1774021188ff3ea320"
SP_SOURCE="9d6ef721338e47e2cae8d179ce84976881df91762050d2a77d83b5399f6ba69a"
PINNED={
 "d_execution":"6956c214240cd85e6263331b33e0c7efcf6abc3e71190d46ff3eabddecd35071",
 "sp_execution":"a3a02969178e5e8b3b040fafd51d08b25d75b3f3922f2ae2e9ee0d4a8ab18a12",
 "body_manifest":"c214f800a5094c905c554e9053c52567d5ae5d76be41ac2e3fe9d673b396d784",
 "sp_manifest":"c77e969bd02ef95d30f16b53ae0a0d3854f596412151e9242ffa0485bd142210",
 "raw_manifest":"0705cb80101f25105d74181aafdf9daaf5a65baeece2d41e8a25b4589259cdad"}
ALPHA=Fraction(6890507429876859,9007199254740992)
NU=Fraction(-2572625729470897,72057594037927936)
ETA=Fraction(-7789843107295549,4611686018427387904)
DELTA=Fraction(1,10**8)
PARAMETERS={
 "arithmetic_bits":320,"runtime":RUNTIME,"exact_waist":"0",
 "radial_trace_side":"right","exact_delta_half_width":str(DELTA),
 "exact_amplitude":str(ALPHA),"exact_eta0":str(ETA),"exact_nu0":str(NU),
 "exact_compact_support":["1/20","9/50"],
 "fixed_test_cutoffs":[97,268435456],"sufficient_cutoff_kind":"first dyadic satisfying WT30",
 "physical_frequency_factor":4,"independent_mean_coordinates":2,
 "background_pair_A0":"7","background_pair_angle_A0":"6",
 "response_pair_A0":"19","response_pair_angle_A0":"83",
 "background_residual_amplitude_count":1,"response_residual_amplitude_count":0,
 "original_background_rows":7296,"original_background_interfaces":6143,
 "original_body_selected_indices":[0,1],"original_body_part_bytes":BODY_BYTES,
 "original_body_parameter_half_width":"1/1000000000",
 "original_background_parameter_half_width":"0",
 "ordinary_angular_norm":"sum of complete component Wiener A0 norms, original moving phi",
 "raw_response_nonmean_field":"uncorrected_response_nonmean.A0_sup",
 "raw_response_mean_field":"response_mean_residual",
 "state_bandwidth":96,"S_bandwidth":192,"S2_bandwidth":384,
 "old_scientific_calls":0,"old_integrals_recomputed":0,
 "strict_fivepart_native_restored":False,"expected_gate_count":GATE_COUNT,
 "new_array_artifact_or_Release":False,
 "interval_inverse_or_finite_Schur_or_unknown_solution_claimed":False}

def canonical(x):
    return (json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(",",":"),
                       allow_nan=False)+"\n").encode("utf-8")
def sha_bytes(x):return hashlib.sha256(x).hexdigest()
def sha(path):return sha_bytes(Path(path).read_bytes())
def read(path):return json.loads(Path(path).read_text())
def q(x):
    x=Fraction(x)
    return arb(x.numerator)/x.denominator
def box(x):
    if isinstance(x,dict):
        if "lower" in x and "upper" in x:
            z=arb(x["lower"]).lower().union(arb(x["upper"]).upper())
        elif "ball" in x:z=arb(x["ball"])
        else:raise ValueError("saved scalar lacks a complete interval")
    else:z=arb(str(x))
    if not z.is_finite():raise ValueError("nonfinite saved or new scalar")
    return z
def up(x):
    z=box(x) if isinstance(x,dict) else arb(x)
    if not z.is_finite():raise ValueError("nonfinite upper bound")
    return z.upper()
def lo(x):
    z=box(x) if isinstance(x,dict) else arb(x)
    if not z.is_finite():raise ValueError("nonfinite lower bound")
    return z.lower()
def nn(x):
    z=up(x)
    if not z>=0:raise ValueError("nonnegative bound is not nonnegative")
    return z
def absup(x):return up(abs(box(x)))
def sqrtup(x):
    z=nn(x)
    return up(z.sqrt())
def powup(x,p):
    z=nn(x)
    if z==0:return arb(0)
    return up((z.log()*q(p)).exp())
def record(x):
    z=box(x)
    return {"ball":z.str(72)}
def upper_record(x):return record(up(x))
def gate(doc,name,ok):
    doc["gates"].append({"name":name,"passed":bool(ok)})
    if not ok:raise ValueError("waist-normalizer gate failed: "+name)
def complete(x,n):
    return (x.get("complete") is True and x.get("failure") is None
            and len(x.get("gates",[]))==n
            and all(g.get("passed") is True for g in x["gates"]))
def saved_execution(x,rid,n,source):
    s=x.get("actual_scientific_receipt",{})
    ok=(str(x.get("run_id"))==str(rid) and x.get("complete") is True
        and x.get("actual_returncode")==0 and complete(s,n)
        and s.get("source_sha256")==source)
    return ok,s

def checked_inputs(a,doc):
    actual={"Python":platform.python_version(),
            "python_flint":importlib.metadata.version("python-flint")}
    gate(doc,"pinned public runtime and320-bit directed arithmetic",
         actual==RUNTIME and a.bits==320)
    doc["runtime"]=actual
    manifest=read(a.manifest)
    paths={r:Path(getattr(a,r)) for r in PINNED}
    gate(doc,"same manifest source parameters and five complete mathematical inputs",
         sha(a.manifest)==a.manifest_sha and manifest.get("kind")==MANIFEST_KIND
         and manifest.get("repository")==PUBLIC and manifest.get("parameters")==PARAMETERS
         and manifest.get("mathematical_input_sha256")==PINNED
         and manifest.get("source_sha256")==sha(__file__)
         and all(sha(paths[r])==v for r,v in PINNED.items()))
    de=read(a.d_execution);ok,ds=saved_execution(de,43713242980,12,D_SOURCE)
    gate(doc,"complete original D state conclusion and unchanged continuous definitions",
         ok and ds.get("derived_continuous_centre_definition_sha256")==CENTRE
         and ds.get("derived_continuous_response_definition_sha256")==DIRECTION
         and ds.get("complete_original_rows_verified")==7721
         and ds.get("exact_original_eta_and_nu",{}).get("exact_alpha")==str(ALPHA)
         and ds.get("exact_original_eta_and_nu",{}).get("exact_nu")==str(NU))
    names=("background_pair_A0","background_pair_angle_A0",
           "response_pair_A0","response_pair_angle_A0")
    values=(7,6,19,83)
    dstate=ds["verified_global_state_bounds"]
    gate(doc,"complete fixed raw-plus-repair state bounds reused without enlarging D parameter fees",
         all(nn(dstate[n])<v for n,v in zip(names,values))
         and ds["parameters"]["delta_half_width"]=="1/10000000000"
         and ds["complete_response_repair_including_mean"]==
             {"A0":"0.0000000000000002292","angular_multiplier":384})
    se=read(a.sp_execution);ok,ss=saved_execution(se,43731464771,20,SP_SOURCE)
    gate(doc,"complete original SP waist conclusion and unchanged source identity",
         ok and ss.get("input_manifest_sha256")==PINNED["sp_manifest"]
         and ss.get("kind")=="actual_complete_primitive_mean_strict_propagation_v1")
    fam=ss["exact_family_identity"];sp=read(a.sp_manifest)
    sparam=ss["mathematical_parameters"]
    gate(doc,"same complete real selected family physical frequencies and two waist means",
         fam.get("continuous_centre_definition_sha256")==CENTRE
         and fam.get("continuous_response_definition_sha256")==DIRECTION
         and fam.get("original_candidate_sha256")==CANDIDATE
         and fam.get("original_object_sha256")==OBJECT
         and fam.get("exact_alpha")==str(ALPHA) and fam.get("exact_nu_centre")==str(NU)
         and fam.get("fixed_current_eta")=="eta_0"
         and list(map(Fraction,fam["exact_selected_nu_interval"]))==[NU-DELTA,NU+DELTA]
         and fam.get("original_eta_half_width")=="1/1000000000"
         and fam.get("complete_original_eta_enclosures_restricted_without_recomputation") is True
         and sparam.get("exact_real_delta_radius")==str(DELTA)
         and sparam.get("physical_frequency_factor")==4
         and sparam.get("complete_mean_coordinates")==2
         and sp.get("mathematical_parameters")==sparam)
    bm=read(a.body_manifest);ident=bm["row_identity"]
    full=ident["full_trials"]["response"]
    deps=ident["dependencies"]
    gate(doc,"same original body identity full raw193 response and complete dependency hashes",
         bm.get("total_common_cells")==7721
         and bm.get("residual_kind")=="actual_full_regular_joint_radial_polynomial_residual_rows_v1"
         and ident.get("source_sha256")==BODY_SOURCE and ident.get("candidate_sha256")==CANDIDATE
         and ident.get("object_sha256")==OBJECT and ident.get("exact_alpha")==str(ALPHA)
         and ident.get("exact_nu")==str(NU)
         and ident.get("original_parameter_half_width")=="1/1000000000"
         and full.get("sha256")==RESPONSE
         and full["metadata"].get("modes")==96
         and full["metadata"].get("finite_head_mean_was_not_removed_from_the_solve") is True
         and deps.get("fourfold_codazzi_nu_full_adjoint_kernel.py")==BODY_OPERATOR
         and deps.get("fourfold_codazzi_correlated_radial_Fourier.py")==FOURIER_NORMS)
    doc.update(input_sha256=PINNED,
       copied_complete_fixed_state_bounds=dstate,
       copied_D_state_and_repair_parameters={k:ds["parameters"][k] for k in
            ("background_pair_A0","background_pair_angle_A0","response_pair_A0",
             "response_pair_angle_A0","response_continuous_repair_A_1over64")},
       copied_SP_family_identity=fam,
       copied_complete_SP_waist_factors=ss["complete_endpoint_readout_conclusion"][
           "waist_complete_radial_factors"],
       body_identity_sha256=sha_bytes(canonical(ident)),
       original_D_delta_fee_radius_not_extended=True,
       original_SP_source_and_manifest_sha256=[SP_SOURCE,PINNED["sp_manifest"]])
    return manifest,bm,ss

def restore_body(a,bm,ss,doc):
    raw=Path(a.body_row).read_bytes()
    expected={"bytes":BODY_BYTES,"indices":[0,1],"sha256":BODY_SHA}
    gate(doc,"exact original bodyrow0 bytes and prior SP successful restoration receipt",
         len(raw)==BODY_BYTES and sha_bytes(raw)==BODY_SHA
         and ss["original_body_prefix_part_receipts"][0]==expected)
    d=json.loads(gzip.decompress(raw))
    gate(doc,"complete original one-row natural part without requiring global completion",
         d.get("kind")==bm["residual_kind"] and d.get("identity")==bm["row_identity"]
         and d.get("source_sha256")==BODY_SOURCE and d.get("selected_indices")==[0,1]
         and d.get("selected_cells_complete") is True and d.get("failure") is None
         and len(d.get("rows",[]))==1)
    r=d["rows"][0];l,h=map(Fraction,r["interval"]);gl,gh=map(Fraction,r["actual_scalar_germ"])
    oldl,oldh=map(Fraction,r["actual_original_scalar_germ"])
    gate(doc,"true right-waist bodycell in original scalar germs and outside nu support",
         r.get("common_row")==0 and l==0 and l<h<=Fraction(1,20)
         and gl<=l<h<=gh and oldl<=l<h<=oldh
         and r.get("full_output_support")==160
         and r.get("complete_angular_grid")==512)
    doc["original_body_first_row_receipt"]={
       **expected,"source_sha256":d["source_sha256"],"interval":r["interval"],
       "actual_scalar_germ":r["actual_scalar_germ"],
       "actual_original_scalar_germ":r["actual_original_scalar_germ"],
       "full_output_support":160,"complete_angular_grid":512,
       "intrinsic_whole_third_jets":r["intrinsic_whole_third_jets"],
       "raw_response_nonmean_A0_sup":r["uncorrected_response_nonmean"]["A0_sup"],
       "raw_response_mean_residual":r["response_mean_residual"],
       "raw_response_full_trial_mean":r["response_full_trial_mean"],
       "later_mean_completion_used":False}
    return r

def restore_raw_first(a,doc):
    m=read(a.raw_manifest)
    gate(doc,"exact complete raw7296 index and three original byte parts",
         m.get("kind")=="complete_native_lossless_container_binary_parts_v2"
         and m.get("native_complete") is True and m.get("native_failure") is None
         and m.get("complete_native_rows")==7296 and m.get("original_bytes")==RAW_BYTES
         and m.get("original_sha256")==RAW_SHA and m.get("original_source_sha256")==RAW_SOURCE
         and m.get("candidate_sha256")==CANDIDATE and len(m.get("parts",[]))==3)
    chunks=[];cursor=0
    for i,r in enumerate(m["parts"]):
        if r["index"]!=i or r["offset"]!=cursor or Path(r["file"]).name!=r["file"]:
            raise ValueError("original byte-part sequence changed")
        raw=(a.raw_manifest.parent/r["file"]).read_bytes()
        if len(raw)!=r["compressed_bytes"] or sha_bytes(raw)!=r["compressed_sha256"]:
            raise ValueError("original compressed byte part changed")
        payload=gzip.decompress(raw)
        if len(payload)!=r["bytes"] or sha_bytes(payload)!=r["sha256"]:
            raise ValueError("original decompressed byte part changed")
        chunks.append(payload);cursor+=len(payload)
    raw=b"".join(chunks)
    gate(doc,"full original compressed raw container restored byte for byte",
         len(raw)==RAW_BYTES and sha_bytes(raw)==RAW_SHA)
    d=json.loads(gzip.decompress(raw))
    gate(doc,"same raw candidate amplitude nu and complete primitive residual object",
         d.get("kind")=="complete_actual_moving_residual_all_closed_rows_and_interfaces"
         and d.get("complete") is True and d.get("failure") is None
         and d.get("source_sha256")==RAW_SOURCE and d.get("original_producer_sha256")==RAW_PRODUCER
         and d.get("candidate_sha256")==CANDIDATE and d.get("object_sha256")==OBJECT
         and Fraction(d["exact_amplitude"])==ALPHA and Fraction(d["exact_nu"])==NU
         and Fraction(d["common_parameter_half_width"])==0
         and d.get("all_7296_closed_rows_reused_without_recomputation") is True
         and d.get("all_6143_actual_interfaces_paid") is True
         and d.get("complete_original_primitive_tail") is True
         and d.get("complete_residual_support")==96 and d.get("interval")==["0","25/8"])
    rows=d["rows"];cursor=Fraction(0);partition=[]
    for i,r in enumerate(rows):
        l,h=map(Fraction,r["interval"])
        if r.get("index")!=i or l!=cursor or not l<h:
            raise ValueError("original whole raw partition changed")
        if r.get("exact_angular_support_index")!=96:
            raise ValueError("original raw residual support changed")
        partition.append([str(l),str(h)]);cursor=h
    ph=sha_bytes(json.dumps(partition).encode())
    gate(doc,"complete original7296 partition and6143 interfaces checked without new integration",
         len(rows)==7296 and cursor==Fraction(25,8)
         and ph==d.get("exact_full_partition_sha256")
         and len(d.get("complete_interface_jumps",[]))==6143)
    r=rows[0];l,h=map(Fraction,r["interval"]);gl,gh=map(Fraction,r["actual_scalar_germ"])
    gate(doc,"actual first raw closed row contains the true right waist and complete residual",
         r.get("index")==0 and l==0 and l<h<=Fraction(1,20)
         and gl<=l<h<=gh and r.get("candidate_piece")==0
         and r.get("exact_angular_support_index")==96)
    doc["original_raw_first_row_receipt"]={
       "manifest_sha256":PINNED["raw_manifest"],"original_container_bytes":RAW_BYTES,
       "original_container_sha256":RAW_SHA,"original_parts":m["parts"],
       "original_partition_sha256":ph,"complete_original_rows":7296,
       "complete_original_interfaces":6143,"index":0,"interval":r["interval"],
       "candidate_piece":r["candidate_piece"],"actual_scalar_germ":r["actual_scalar_germ"],
       "complete_residual_A0":r["complete_residual_A0"],
       "original_residual_support":96,"old_integral_recomputed":False}
    return r

def coefficients(body,raw,doc):
    j=body["intrinsic_whole_third_jets"];w=doc["copied_complete_SP_waist_factors"]
    gm=lo(j["gamma"]);gp=absup(j["gamma"]);g1=absup(j["gamma1"])
    b=absup(j["beta"]);b1=absup(j["beta1"])
    k=max(arb(1),absup(j["K"]))
    k1=absup(j["K1"]);k2=absup(j["K2"])
    mm=lo(w["complete_absolute_mean_lower"]);mp=nn(w["complete_absolute_mean_upper"])
    qm=lo(w["q_lower"]);qp=nn(w["q_upper"])
    gate(doc,"complete waist mean curvature and intrinsic-speed directed lower gates",
         gm>0 and mm>0 and qm>0 and mp>=mm and qp>=qm)
    ru=nn(raw["complete_residual_A0"]["U"])
    rv=nn(raw["complete_residual_A0"]["V"])
    rn=nn(body["uncorrected_response_nonmean"]["A0_sup"])
    rm=absup(body["response_mean_residual"])
    gate(doc,"all four raw residual species finite with full response mean and one base amplitude",
         all(v.is_finite() and v>=0 for v in (ru,rv,rn,rm)))
    B=up(b*k);G=up(gp*k);M=arb(7);P=arb(6);dd=q(DELTA)
    c0=up(169*B+6*G);c1=up(49*B/4+7*G)
    rq=up(b*M+B*(M**3+M*M*P/4)+G*M*P+q(ALPHA)*(ru+rv))
    rz=up(c0*19+c1*83+rn+rm)
    md=up(M+19*dd);pd=up(P+83*dd);rd=up(rq+dd*rz)
    em=lo(gm*mm);ep=up(gp*mp);e1=up(g1*mp+gp*rd)
    d0=up(B*md*md/4);d1=up(B*md*md)
    q1=up(k1/(2*qm));q2=up(k2/(2*qm)+k1*k1/(4*qm**3))
    w0=up(md+qp*md);wp=up(pd+qp*pd);wr=up(rd+qp*rd+q1*md)
    am=lo(em*qm);ap=up(ep*qp);a1=up(e1*qp+ep*q1)
    bs=up(q1/(2*qm)+b*(1+w0*w0));bp=up(2*b*w0*wp)
    br=up(q2/(2*qm)+q1*q1/(2*qm*qm)+b1*(1+w0*w0)+2*b*w0*wr)
    ss=up(bs/(2*am));sphi=up(bp/(2*am))
    sr=up(br/(2*am)+bs*a1/(2*am*am))
    es=up(bp+b*wp*w0+(d0+ap)*sphi+sr+ss*d1)
    s2=up(es/(2*am))
    vals={"beta_abs":b,"beta_r_abs":b1,"K_abs_or_one":k,"K_r_abs":k1,"K_rr_abs":k2,
      "gamma_lower":gm,"gamma_abs_upper":gp,"gamma_r_abs":g1,
      "B":B,"G":G,"raw_U_residual":ru,"raw_V_residual":rv,
      "raw_response_nonmean_A0":rn,"raw_response_mean_abs":rm,
      "raw_response_complete_A0":up(rn+rm),"response_A0_zero_order":c0,
      "response_A0_first_order":c1,"background_right_derivative_pair":rq,
      "response_right_derivative_pair":rz,"selected_pair_A0":md,"selected_pair_angle_A0":pd,
      "selected_right_derivative_pair":rd,"U0":md,"V0":md,"U1":pd,"V1":pd,"Ur":rd,"Vr":rd,
      "complete_abs_mean_lower":mm,"complete_abs_mean_upper":mp,"q_lower":qm,"q_upper":qp,
      "eta_lower":em,"eta_upper":ep,"eta_r_abs":e1,"D0":d0,"D1":d1,
      "q_r_abs":q1,"q_rr_abs":q2,"W0":w0,"Wphi":wp,"Wr":wr,
      "a_lower":am,"a_upper":ap,"a_r_abs":a1,
      "B_star":bs,"Bphi_star":bp,"Br_star":br,"S_star":ss,"Sphi_star":sphi,
      "Sr_star":sr,"E_star":es,"S2_star":s2}
    gate(doc,"complete right-waist wide coefficients finite with all radial and mean terms",
         all(v.is_finite() and v>=0 for v in vals.values()) and am>0)
    doc["complete_waist_coefficient_bounds"]={n:record(v) for n,v in vals.items()}
    doc["new_coefficient_scope"]={
       "exact_delta_half_width":str(DELTA),"radial_point":"0","radial_side":"right",
       "ordinary_derivatives_not_factorial_jets":True,
       "background_residual_alpha_paid_once":True,"raw_response_alpha_paid":False,
       "both_canonical_piece_constant_radial_derivatives_zero":True,
       "mean_completed_surrogate_used":False,"whole_core_D_delta_fee_extended":False,
       "all_true_means_retained":True,"unknown_state_or_PDE_solution_assumed":False}
    return nn(doc["complete_waist_coefficient_bounds"]["S_star"]),nn(
        doc["complete_waist_coefficient_bounds"]["S2_star"])

def cutoff_row(J,S,S2,selection):
    jj=arb(J)
    def ms(t):
        if t==0:return S
        return up(powup(1+arb(192)/jj,abs(t))*sqrtup(385)*S)
    def m2(t):
        if t==0:return S2
        return up(powup(1+arb(384)/jj,abs(t))*sqrtup(769)*S2)
    t1z=upper_record(S/(4*jj));t2z=upper_record(S2/(4*jj)**2)
    t1n=upper_record(ms(Fraction(-4,3))/(4*jj))
    t2n=upper_record(m2(Fraction(-4,3))/(4*jj)**2)
    tau={"tau1_L2":t1z,"tau2_L2":t2z,"tau1_Hminus4third":t1n,"tau2_Hminus4third":t2n}
    checks=[{"name":k+" strictly below one","passed":bool(nn(v)<1)} for k,v in tau.items()]
    passed=all(v["passed"] for v in checks)
    lam=sqrtup(1+16*jj*jj);gam=up(lam/(4*jj))
    # The denominator is a lower-directed positive power of the exact integer.
    pre=up(gam*gam/lo((lo(arb(1+16*J*J)).log()/3).exp()))
    finite=up(2*sqrtup(17)/4*S*powup(sqrtup(1+16*(J+191)**2),Fraction(1,3)))
    forward=up((1+nn(t1z))*pre*m2(Fraction(2,3)))
    row={"J":J,"selection":selection,"physical_minimum_frequency":4*J,
         "all_four_strict_tests":checks,"strict_tests_passed":sum(v["passed"] for v in checks),
         "strict_tests_total":4,"inverse_on_both_windows_proved":passed,
         "tau":tau,"first_symbol_finite_support_label":J+191,
         "two_factor_finite_support_label":J+575,
         "first_symbol_finite_strong_fee":upper_record(finite),
         "forward_complete_strong_remainder":upper_record(forward),
         "forward_operator_L2":upper_record((1+nn(t1z))*(1+nn(t2z))),
         "forward_operator_Hminus4third":upper_record((1+nn(t1n))*(1+nn(t2n))),
         "same_inverse_two_window_bounds":None,"inverse_complete_strong_remainder":None,
         "finite_complement_and_two_means_identity":True}
    if passed:
        iz=up(1/lo((1-nn(t1z))*(1-nn(t2z))))
        inn=up(1/lo((1-nn(t1n))*(1-nn(t2n))))
        rn=up(pre/lo(1-nn(t1n))*
              (ms(Fraction(2,3))*ms(Fraction(-1,3))+m2(Fraction(2,3))/lo(1-nn(t2z))))
        row["same_inverse_two_window_bounds"]={
           "L2":upper_record(iz),"Hminus4third":upper_record(inn)}
        row["inverse_complete_strong_remainder"]=upper_record(rn)
    return row

def cutoffs(S,S2,doc):
    fixed=[cutoff_row(J,S,S2,"fixed waist candidate") for J in PARAMETERS["fixed_test_cutoffs"]]
    a1=upper_record(sqrtup(385)*S);a2=upper_record(sqrtup(769)*S2)
    J=1
    for _ in range(4096):
        if J>=384 and J>=97 and arb(J)>=4*nn(a1) and arb(J*J)>=4*nn(a2):break
        J*=2
    else:raise ValueError("sufficient finite dyadic search limit exceeded")
    sufficient=cutoff_row(J,S,S2,"first sufficient dyadic under final retained upper budgets")
    doc["complete_fixed_cutoff_results"]=fixed
    doc["complete_sufficient_dyadic_result"]={
       "budget_A1":a1,"budget_A2":a2,"row":sufficient}
    gate(doc,"both fixed waist cutoffs retained and a separate complete sufficient dyadic test",
         len(fixed)==2 and [r["J"] for r in fixed]==PARAMETERS["fixed_test_cutoffs"]
         and all(r["strict_tests_total"]==4 for r in fixed)
         and sufficient["strict_tests_total"]==4
         and sufficient["inverse_on_both_windows_proved"] is True)
    doc["fixed_cutoff_inverse_success_count"]=sum(r["inverse_on_both_windows_proved"] for r in fixed)
    doc["fixed_cutoff_inverse_test_count"]=2

def run(a,doc):
    manifest,bm,ss=checked_inputs(a,doc)
    body=restore_body(a,bm,ss,doc)
    raw=restore_raw_first(a,doc)
    S,S2=coefficients(body,raw,doc)
    cutoffs(S,S2,doc)
    gate(doc,"only new waist scalar combinations with old fields means and finite ports preserved",
         PARAMETERS["old_scientific_calls"]==0 and PARAMETERS["old_integrals_recomputed"]==0
         and PARAMETERS["strict_fivepart_native_restored"] is False)
    if len(doc["gates"])!=GATE_COUNT:raise ValueError("unexpected structural gate count")
    doc.update(complete=True,proved=True,actual_returncode=0,
       complete_waist_coefficient_bounds_proved=True,
       fixed_cutoff_failures_are_retained_sufficient_test_failures=True,
       original_numerical_enclosures_recomputed=0,old_source_or_integral_calls=0,
       strict_fivepart_native_restored=False,
       new_recomputable_array_artifact_or_Release=False,
       interval_inverse_or_finite_Schur_or_unknown_solution_claimed=False)

def save(a,doc):
    raw=canonical(doc);a.out.parent.mkdir(parents=True,exist_ok=True)
    tmp=a.out.with_name(a.out.name+".partial");tmp.write_bytes(raw);tmp.replace(a.out)
    print("WT_SCIENTIFIC_CONCLUSION_V1_BEGIN",flush=True)
    print(json.dumps({"bytes":len(raw),"sha256":sha_bytes(raw)},sort_keys=True),flush=True)
    print(raw.decode("utf-8"),end="",flush=True)
    print("WT_SCIENTIFIC_CONCLUSION_V1_END",flush=True)
    if len(raw)>45000:raise ValueError("complete scientific conclusion exceeds45000 bytes")

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for r in PINNED:p.add_argument("--"+r.replace("_","-"),type=Path,required=True)
    p.add_argument("--body-row",type=Path,required=True)
    p.add_argument("--manifest",type=Path,required=True)
    p.add_argument("--manifest-sha",required=True)
    p.add_argument("--run-id",required=True);p.add_argument("--run-attempt",required=True)
    p.add_argument("--out",type=Path,required=True);p.add_argument("--bits",type=int,default=320)
    a=p.parse_args();ctx.prec=a.bits;t=time.monotonic()
    doc={"kind":KIND,"public_repository":PUBLIC,"source_sha256":sha(__file__),
       "input_manifest_sha256":a.manifest_sha,"run_id":a.run_id,"run_attempt":a.run_attempt,
       "parameters":PARAMETERS,"runtime":None,"arithmetic_bits":a.bits,
       "complete":False,"proved":False,"actual_returncode":1,"failure":None,"gates":[]}
    try:run(a,doc)
    except Exception as e:
        doc["failure"]={"type":type(e).__name__,"message":str(e)}
        traceback.print_exc()
    finally:
        doc["seconds"]=time.monotonic()-t
        save(a,doc)
    return doc["actual_returncode"]

if __name__=="__main__":
    raise SystemExit(main())
