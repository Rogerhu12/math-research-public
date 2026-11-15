#!/usr/bin/env python3
"""New complete leading E row with the original b0=T^2 b2 root factor.

Only a new physical image, canonical b2_T bound, three E angular budgets,
one E operator and one complete raw1 comparison are evaluated. Successful
mixed jets, seven other complete summands and all old producers are read.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,math,os,platform,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy,scipy
from flint import arb,ctx

PUBLIC="Rogerhu12/math-research-public"
TOPIC="topics/visible-flex-exact-nearby/"
KIND="actual_retained_leading_root_zero_complete_E_row_v1"
CONTRACT="be46d277cc8e136bbcb96febe327d0cba75938662eabe088078f90b53be4a61a"
RUNTIME=dict(python="3.12.14",python_flint="0.9.0",numpy="2.3.5",scipy="1.17.0")
ROOTS=(Q(1191984371497,5000000000000),Q(2383968743003,10000000000000))
PIECE=(Q(2147184947341121,9007199254740992),Q(4295308144604611,18014398509481984))
H=Q(893368603925465506687,21990232555520000000000000)
RG=Q(3,8000);SG=Q(3,128);SP=Q(1,256);CW=Q(1,32)
R0=Q(1,6000);RA=Q(3,40000);SIGMA0=Q(1,128)
RF=Q(3,20000);SF=Q(1,64);RS=Q(1,8000);SS=Q(3,512)
RC=Q(27,32000);SC=Q(1,64);N=388
BRANCHES=("central","positive_characteristic","negative_characteristic")
MAJORANTS="29ee1093b7644143c693283f774294c176a7f0989b42c004d384a856d5be5144"
APROC="9e8f1f92660c1b44aa3c5c389a2c621a14aa65611cb0cf4c3a98daac1613a89b"
APUB="0cfbfcd3866c4fda4fd31020efa630c8e3b5e7e24fc6fafe1219a2e84a3efe3c"
LEGACY_SOURCE="f553b1506dde1b1d80119fb77b084a43ee19e08e17f32f7139a4a1dddf53a739"
LEGACY_HELPER="1860872f56baf809517693473bb43cb3e897c2c082c5b2e6b7b38cfeaa59eb53"
LEGACY_MANIFEST="76cf792e1e223e4b45487f90c9a44dd64fcaf32e46c0f1a0a46f442eb4faa18a"
SE=Q(3,256)
RECEIPTS={
 "positive_execution":("43702688640","b0648a3bc244e6671176ac096c759b3e70e57d8c04b75bd4dd74442bfcaf95c0","8465759dfe9101bb7e20275cec1a5b98e23efb4dbe643e492fb8189250b005b9","bca0f97d7c610f8f2572e61d1e1442a8b9c256a4c5429253682b6d803e3a21c3",17),
 "directed_execution":("43703879926","1aa46093bba5150d636cc7c6ef4f5b080447fc2c75d7438b2e52ae5fa6b5d0af","5ce9aceb3be46e795696c09028f39091fdc9a4f969dba0e0b317408974083e9b","2c5cba2e7351267e090d0ca6c06cfecbb21309c039a7844937ee64026254f1d0",12),
 "potential_execution":("43685624307","042713687b7d2d561ba25678a76ae9dbd95e042ec1d57bf4a0caa89310063fe7","44555290b424807278c933aaa5cc26c8a8e198ef1ff02ebdc7728c4ad6810437","d4c48d613cad95a3ad67ccb965acc2e76dc4e7786634a6234850667607ea08e9",16),
 "AJ_execution":("43718112378","32c45b335639a48b0d32541d03924246023e5e3f19deec1bcd8cf0549e955f03","871240a7a97011d837025aad7f9ca1707d69c17b6dec3c1f510f6415c278b74d","58462f96a486dede07873c4fc6aade100539f9f28ef49b49567a4acf7c2e8706",29),
 "RV_execution":("43719681982","d59893af66b8829d924d75686fb0ecd6e6d25f9b72b70a0fac6564c4e96fdf60","4718b4b818ec5d72537aa3a93e5825747a586ece87a086c7578ec6ec4c3b9ded","0781239c0753785d2b196b77cc90c0eb343d52cc73226d84d7f8f6bb23136473",27),
 "mixed_execution":("43721735003","b4bc768e149f01591102a9bcc8c16b166bd8ba97fd0c0c245ba3073ba3382496","1055c8231c7646acb5b37e7c876a62321436192927ba9616ad7a1d08a24cb1e2","b858853023fd93bfefbac5f8e18471c93c88d90c051999bcf35dd9bc0df8aa4e",23),
 "baseline_execution":("43722805762","44021afbf608638e7e08f584a5574acdc76738c5985d72ca0f2b036c8f7d2dc0","5306e66c5102e358caba5946b3c651dda11fb98a18848f8fe27f779f775d73cf","ba96a4832017144ea3ccd59902e8bcb8f1b0acd1c722edadc44b763dfac6c0d0",23)
}

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ex(x):
    x=Q(x);return arb(x.numerator)/arb(x.denominator)
def rb(v):
    if isinstance(v,arb):return v
    if isinstance(v,(int,Q)):return ex(v)
    if isinstance(v,str):return arb(v)
    return arb(v["ball"])
def up(v):return abs(rb(v)).upper()
def bound(v,label="complete upper"):
    v=rb(v)
    if not v.is_finite() or v.lower()<0:raise ValueError("invalid "+label)
    return v.upper()
def lower(v,label="positive budget number"):
    v=rb(v).lower()
    if not v.is_finite() or v<0:raise ValueError("invalid nonnegative lower "+label)
    return v
def gap(v,label):
    v=lower(v,label)
    if not v>0:raise ValueError("missing positive gap "+label)
    return v
def rec(v):return dict(ball=rb(v).str(64))
def unpack(v):
    if isinstance(v,dict):
        if set(v)=={"ball"}:return arb(v["ball"])
        return {k:unpack(z) for k,z in v.items()}
    if isinstance(v,list):return [unpack(z) for z in v]
    return v
def encode(v):
    if isinstance(v,arb):return rec(v)
    if isinstance(v,Q):return str(v)
    if isinstance(v,dict):return {str(k):encode(x) for k,x in v.items()}
    if isinstance(v,(tuple,list)):return [encode(x) for x in v]
    return v
def read(p):
    p=Path(p);raw=p.read_bytes()
    return json.loads(gzip.decompress(raw) if p.suffix==".gz" else raw)
def payload_sha(v):
    return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def save(p,v,compressed=False):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
    temp=p.with_name(p.name+".partial")
    temp.write_bytes(gzip.compress(raw,mtime=0) if compressed else raw);temp.replace(p)
def cauchy(m,width,k):
    if not Q(width)>0:raise ValueError("nonpositive complete angular width")
    return [up(bound(m)*math.factorial(q)/ex(Q(width)**q)) for q in range(k+1)]
def choose_complete(old,new):
    if bound(new)<bound(old):return rec(bound(new)),bool(bound(new)<rb(old).lower())
    return old,False

def accepted(path,identity,gate):
    run,source,manifest,digest,ngates=identity
    e=read(path);r=e.get("actual_scientific_receipt",{})
    gate("accepted complete run "+run+"/1 retains source manifest all gates and actual child zero",
        sha(path)==digest and str(e.get("run_id"))==run and str(e.get("run_attempt"))=="1"
        and e.get("complete") is True and e.get("actual_returncode")==0 and e.get("actual_failure") is None
        and e.get("source_budget_source_sha256")==source and e.get("input_manifest_sha256")==manifest
        and r.get("source_sha256")==source and r.get("input_manifest_sha256")==manifest
        and r.get("complete") is True and r.get("proved") is True and r.get("actual_returncode")==0
        and r.get("failure") is None and r.get("runtime")==RUNTIME
        and r.get("gates") and all(g.get("passed") is True for g in r["gates"])
        and (ngates is None or len(r["gates"])==ngates))
    return r

def read_original_fold(paths,gate):
    ms=read(paths["old_fold_majorants_stage"]);p=read(paths["adjacent_process"]);u=read(paths["adjacent_publication"])
    entries=[e for e in u["files"] if e["file"]=="consumers/stages/complete-original-reference-holomorphic-majorants.json.gz"]
    gate("the original4501-byte fold and coefficient payload are read without rerunning their producers",
        sha(paths["old_fold_majorants_stage"])==MAJORANTS and sha(paths["adjacent_process"])==APROC
        and sha(paths["adjacent_publication"])==APUB and len(entries)==1
        and entries[0]["bytes"]==4501 and entries[0]["sha256"]==MAJORANTS
        and ms["complete"] and ms["stage"]==ms["name"]=="complete-original-reference-holomorphic-majorants"
        and ms["source_sha256"]==LEGACY_SOURCE and ms["algebra_sha256"]==LEGACY_HELPER
        and ms["input_manifest_sha256"]==LEGACY_MANIFEST and ms["runtime"]==RUNTIME
        and p["actual_returncode"]==0 and p["mathematical_complete"] and p["mathematical_proved"]
        and p["mathematical_failure"] is None and u["complete"]
        and all(ms["payload"]["majorants"][k][1:]==[str(RG),str(SG)] for k in ("A","chi")))
    return unpack(ms["payload"])

def read_positive_coefficients(C,gate):
    rows=C["complete_positive_linear_operator_conclusion"]
    gate("the same eighteen complete genuine-column coefficients include all three branches two signs and output means",
        len(rows)==3 and [r["branch"] for r in rows]==list(BRANCHES)
        and all(r["exact_input_component_order"]==["a","a_phi","a_phiphi","b","b_phi","b_phiphi"]
            and len(r["complete_positive_linear_coefficients"])==6
            and len(r["selected_inputs"])==6
            and all(v["denominator_is_lower_for_bound_number_only"] for v in r["selected_inputs"]) for r in rows)
        and C["scope"]["both_genuine_columns_and_both_carrier_signs"]
        and C["scope"]["all_input_abs_j_at_least97"])
    return [[bound(v) for v in r["complete_positive_linear_coefficients"]] for r in rows]

def positive_operator(coeff,vector):
    values=vector[0][:3]+vector[1][:3]
    return up(sum((sum((c*v for c,v in zip(row,values)),arb(0)) for row in coeff),arb(0)))

def parameters():
    return dict(arithmetic_bits=320,physical_piece=2549,cutoff_abs_j=97,physical_frequency="4j",
        exact_negative_cover=[str(PIECE[0]),str(ROOTS[1])],exact_root_interval=list(map(str,ROOTS)),
        exact_negative_rho_cover=str(ROOTS[1]-PIECE[0]),exact_original_whole_cover=str(H),
        exact_original_fold_radius=str(RG),exact_original_fold_strip=str(SG),
        exact_original_canonical_radius=str(RC),exact_original_canonical_strip=str(SC),
        exact_new_physical_E_strip=str(SE),original_potential_radius=str(R0),
        exact_input_weight="1",common_column_envelope="abs(rho)^(-1/4)",
        complex_delta_square_halfwidth="1/100000000",complex_z_square_halfwidth="1/9409",
        fixed_intrinsic_parameter="eta_0",root_identity="b0=T^2*b2",
        accepted_mixed_run="43721735003/1",accepted_baseline_run=RECEIPTS["baseline_execution"][0]+"/1",
        complete_M_non_E_summands_read=7,new_E_angular_orders=[0,1,2],
        new_changed_terms=["local_raw_1"],old_mixed_derivatives_recomputed=0,
        old_radial_integrals_recomputed=0,full_mean_and_both_input_signs=True)

def root_E_budget(f,P,AJ,RV,M,h,gate):
    """ER.7--ER.17: the derivative is canonical at fixed X, with b0=T^2 b2."""
    rv=RV["complete_domain_conclusion"];ad=AJ["complete_domain_conclusion"]
    aj=AJ["complete_AJ_angular_derivative_conclusion"];mc=M["complete_coefficient_conclusion"]
    cases=[v for v in P["cases"] if Q(v["exact_complex_radial_radius"])==R0]
    if len(cases)!=1:raise ValueError("the same complete scalar-potential case is not unique")
    pc=cases[0]
    Th=bound(rv["new_complete_negative_T_image_upper"],"accepted complete negative T image")
    dT=gap(rv["complete_leading_T_margin_lower"],"accepted canonical T derivative margin")
    image=gap(pc["reference_image"]["complete_image_disk_radius_lower"],"same full potential image")
    B2=bound(f["B2"],"original complete canonical b2 modulus")
    CT=bound(ad["complete_cT_holomorphic_upper"],"complete original SG connection modulus")
    mu=bound(mc["complete_mu_holomorphic_upper"],"M complete original SG mu modulus")
    gate("the original canonical inverse root factor connection and potential retain their entire accepted products",
        h==ROOTS[1]-PIECE[0] and 0<h<H<RG and 0<SE<SC<SG
        and Q(rv["exact_negative_rho_cover"])==h and Q(rv["exact_original_whole_cover"])==H
        and rv["original_full_mean_gauge_retained"] and rv["original_potential_and_fold_producers_called"] is False
        and Q(ad["exact_original_fold_radius"])==RG and Q(ad["exact_original_fold_strip"])==SG
        and Q(ad["exact_full_physical_cover"])==H and aj["accepted_order_zero_domain_read_verbatim"]==ad
        and ad["full_mean_and_radial_G_scalar_retained"] and ad["physical_T_image_definition_read_from_frozen_producer"]
        and ad["old_image_fold_forcing_and_amplitude_enclosures_recomputed"] is False
        and Q(mc["exact_complete_mu_strip"])==SG and Q(mc["exact_negative_rho_cover"])==h
        and mc["full_radial_gauge_and_all_means_retained"]
        and mc["no_old_fold_negative_geometry_AJ_or_potential_closure_called"]
        and mc["accepted_negative_T_image"]==rv["new_complete_negative_T_image_upper"]
        and pc["complete"] and pc["proved"] and pc["failure"] is None
        and pc["whole_complex_bilinear_family"] and pc["both_carrier_signs_retained"]
        and Q(pc["exact_complex_delta_square_halfwidth"])==Q(1,10**8)
        and Q(pc["exact_complex_z_square_halfwidth"])==Q(1,9409)
        and pc["fixed_intrinsic_parameter"]=="eta_0"
        and gap(f["Am"],"complete A gap")>0 and gap(f["mu"],"complete mu gap")>0
        and gap(f["gap"],"complete principal gap")>0
        and bound(f["row_r"],"original inverse radial row")<ex(Q(1,2))
        and bound(f["row_phi"],"original inverse angle row")<ex(Q(1,2)))
    # X(0,phi)=phi, and Xr is the already certified true physical derivative.
    Xr=bound(f["Xr"],"original full physical Xr")
    Ximage=up(ex(SE)+ex(h)*Xr)
    Xgap=gap(ex(SC)-Ximage,"new complete physical-to-canonical X margin")
    gate("the new physical strip maps strictly inside the same original canonical and potential products",
        Ximage<ex(SC) and Xgap>0 and Th<ex(RC) and image>Th
        and dT>0 and Q(SE)==Q(3,256))
    MV=bound(pc["complete_modulus_upper"]["V"])
    MVT=bound(pc["complete_modulus_upper"]["V_T"])
    b2T=up(B2/dT)
    b0=up(B2*Th*Th)
    tangent=up(4*Th*B2+2*Th*Th*b2T+CT*b0)
    Ehol=up(mu*(MV*tangent+MVT*b0))
    newjets=cauchy(Ehol,SE,2)
    prior=mc["complete_E_first_component_angular_upper"]
    if len(prior)!=3:raise ValueError("the accepted complete E derivative list changed")
    selected=[min(v,bound(old,"accepted complete E derivative")).upper() for v,old in zip(newjets,prior)]
    gate("the complete E row retains its second-order leading root factor fixed-X derivative all means and zero second component",
        B2.is_finite() and B2.lower()>=0 and b2T.is_finite() and b0.is_finite()
        and all(v.is_finite() and v.lower()>=0 for v in newjets+selected)
        and mc["complete_E_second_component_exact_zero"]
        and M["scope"]["complete_leading_E_row_retained_before_absolute_bounds"]
        and M["scope"]["leading_a0_T_not_inserted_into_E12"])
    conclusion=dict(exact_negative_rho_cover=str(h),exact_original_fold_radius=str(RG),
        exact_original_fold_strip=str(SG),exact_original_canonical_radius=str(RC),
        exact_original_canonical_strip=str(SC),exact_new_physical_E_strip=str(SE),
        accepted_negative_T_image=rv["new_complete_negative_T_image_upper"],
        accepted_canonical_T_margin=rv["complete_leading_T_margin_lower"],
        accepted_potential_image=pc["reference_image"]["complete_image_disk_radius_lower"],
        original_complete_Xr_modulus=rec(Xr),new_complete_X_image_upper=rec(Ximage),
        new_complete_X_margin_lower=rec(Xgap),original_complete_b2_modulus=rec(B2),
        accepted_complete_cT_holomorphic_modulus=ad["complete_cT_holomorphic_upper"],
        accepted_complete_mu_holomorphic_modulus=mc["complete_mu_holomorphic_upper"],
        accepted_complete_V_modulus=pc["complete_modulus_upper"]["V"],
        accepted_complete_VT_modulus=pc["complete_modulus_upper"]["V_T"],
        new_complete_b2T_modulus=rec(b2T),complete_b0_modulus=rec(b0),
        complete_two_b0T_plus_cT_b0_modulus=rec(tangent),
        new_complete_E_holomorphic_modulus=rec(Ehol),
        new_complete_E_first_component_angular_upper=encode(newjets),
        retained_complete_E_first_component_angular_upper=encode(selected),
        original_complete_M_E_first_component_angular_upper=prior,
        complete_E_second_component_exact_zero=True,
        exact_root_identity="b0=T^2*b2",canonical_derivative="partial_T_at_fixed_X",
        original_radial_gauge_all_means_and_two_carriers_retained=True,
        original_fold_inverse_potential_RV_AJ_or_M_closure_called=False)
    return selected,conclusion

NON_E=("genuine_wrr","mixed_drift","first_angle_coefficients","second_angle_coefficients",
       "radial_T0","complete_zeroth_order","complete_offdiagonal_reaction")

def recombine_local(M,positive,Ejets,gate):
    op=M["complete_local_operator_conclusion"]
    groups=op["complete_summand_operator_upper"]
    gate("seven complete M summand bounds are read unchanged and only the full E row is newly evaluated",
        set(groups)==set(NON_E)|{"leading_E_row"} and len(groups)==8
        and op["exact_input_weight"]=="1" and op["raw_numerator_not_divided_by_mu"]
        and op["common_column_envelope"]=="abs(rho)^(-1/4)"
        and op["original_genuine_profiles_and_positive_calibration_read_only"]
        and op["genuine_finite_signed_coefficients_not_split"]
        and len(Ejets)==3 and M["new_complete_summand_diagnostics"]==8)
    rawE=positive_operator(positive,[Ejets,[arb(0),arb(0),arb(0)]])
    selectedE,smallerE=choose_complete(groups["leading_E_row"],rawE)
    non_E=up(sum((bound(groups[k],"accepted complete non-E summand") for k in NON_E),arb(0)))
    value=up(non_E+bound(selectedE))
    return value,dict(complete_first_local_raw_operator_upper=rec(value),
        new_complete_E_operator_upper=rec(rawE),retained_complete_E_operator_upper=selectedE,
        accepted_complete_M_E_operator_upper=groups["leading_E_row"],
        strictly_smaller_complete_E_operator=smallerE,
        accepted_seven_complete_M_non_E_summands={k:groups[k] for k in NON_E},
        complete_non_E_sum_upper=rec(non_E),
        accepted_complete_M_whole_operator=op["complete_first_local_raw_operator_upper"],
        same_common_column_envelope="abs(rho)^(-1/4)",exact_input_weight="1",
        raw_numerator_not_divided_by_mu=True,
        separate_complete_summands_recombined_without_upper_subtraction=True,
        old_mixed_jets_or_summand_operator_calculations_recomputed=False)

def compare_and_combine(C,D,M,baseline,value,gate):
    local=C["complete_local_vector_conclusion"];original=D["complete_source_conclusion"]
    base=baseline["complete_source_conclusion"];ms=M["complete_source_conclusion"]
    stable=("actual_dr_measure","exact_negative_physical_cover","one_sided_uncertain_root_band_retained",
        "both_density_windows_retained","outer_J_window","input_window","first_output_window",
        "independent_even_mean_window","total_squared_envelope_radial_weight_upper","original_temporary_row_payload_sha256")
    allowed_first={"density0_complete_SV","density0_old_mean_V0"}
    allowed_mean={"density0_complete_uJB_w"}
    gate("the latest complete SV baseline preserves M local1 and all original source windows and radial measure",
        D["accepted_complete_local_vector_conclusion"]==local
        and len(base["complete_first_source_term_L2_upper"])==21
        and len(base["complete_independent_mean_term_L2_upper"])==10
        and all(base[k]==ms[k]==original[k] for k in stable)
        and all(base["complete_first_source_term_L2_upper"][k]==v
            for k,v in ms["complete_first_source_term_L2_upper"].items() if k not in allowed_first)
        and all(base["complete_independent_mean_term_L2_upper"][k]==v
            for k,v in ms["complete_independent_mean_term_L2_upper"].items() if k not in allowed_mean)
        and base["exact_negative_physical_cover"]==[str(PIECE[0]),str(ROOTS[1])]
        and local["raw_numerator_not_divided_by_mu"] and local["exact_input_weights"]==["1","1/388","1/150544"])
    beta=gap(local["raw_complete_operator_coefficients"][0],"same original positive local1 numerical budget")
    ratio=min(arb(1),up(value/beta)).upper()
    oldterm=original["complete_first_source_term_L2_upper"]["local_raw_1"]
    candidate=up(ratio*bound(oldterm));prior=base["complete_first_source_term_L2_upper"]["local_raw_1"]
    selected,better=choose_complete(prior,candidate)
    terms=dict(base["complete_first_source_term_L2_upper"]);terms["local_raw_1"]=selected
    result=dict(base);result["complete_first_source_term_L2_upper"]=terms
    local_sum=up(sum((bound(terms["local_raw_"+str(j)]) for j in (1,2,3)),arb(0)))
    result["local_L2_upper"],a=choose_complete(base["local_L2_upper"],local_sum)
    first=up(bound(result["local_L2_upper"])+bound(base["nonlocal_total_L2_upper"]))
    result["first_L2_upper"],b=choose_complete(base["first_L2_upper"],first)
    pair=up((bound(result["first_L2_upper"])**2+bound(base["mean_L2_upper"])**2).sqrt())
    result["combined_L2_upper"],c=choose_complete(base["combined_L2_upper"],pair)
    # Drop predecessor-only scope flags; the full ledger itself is retained.
    for key in ("only_three_complete_density_zero_terms_replaced","all_other_twenty_eight_term_balls_read_verbatim",
        "complete_local_budget_read_unchanged","only_two_complete_local_vectors_replaced",
        "all_other_twenty_nine_term_balls_read_verbatim","current_genuine_amplitude_bounds_and_all_mean_factors_unchanged"):
        result.pop(key,None)
    result.update(only_complete_local_raw1_replaced=True,all_other_thirty_term_balls_read_verbatim=True,
        accepted_SV_complete_improvements_retained=True,
        old_source_row_or_radial_integral_recomputed=False,
        strictly_smaller_complete_aggregates=dict(local=a,first=b,combined=c))
    comparison=dict(source_term="local_raw_1",new_complete_raw_operator_upper=rec(value),
        same_original_positive_budget_lower=rec(beta),complete_uniform_comparison_factor=rec(ratio),
        complete_original_term_L2_upper=oldterm,accepted_current_complete_term_L2_upper=prior,
        retained_complete_term_L2_upper=selected,strict_complete_term_improvement=better,
        comparison_denominator_is_not_function_lower=True)
    gate("only one whole local term changes and all thirty other current source and mean balls remain byte identical",
        all(v==base["complete_first_source_term_L2_upper"][k] for k,v in terms.items() if k!="local_raw_1")
        and result["complete_independent_mean_term_L2_upper"]==base["complete_independent_mean_term_L2_upper"]
        and result["nonlocal_total_L2_upper"]==base["nonlocal_total_L2_upper"]
        and result["mean_L2_upper"]==base["mean_L2_upper"] and all(result[k]==base[k] for k in stable))
    return result,comparison

def render(doc):
    lines=["# Retained leading root zero: actual complete local E row","",
        "- Public repository: "+PUBLIC,
        "- Run: "+str(doc.get("run_id"))+"/"+str(doc.get("run_attempt")),
        "- Script SHA256: "+doc["source_sha256"],
        "- Manifest SHA256: "+doc["input_manifest_sha256"],
        "- Actual mathematical return code: "+str(doc["actual_returncode"]),
        "- Complete/proved: "+str(doc["complete"])+"/"+str(doc["proved"]),
        "- Old numerical enclosures recomputed: 0.",
        "- Full high inverse claimed: false.","","## Actual gates",""]
    lines.extend("- "+g["name"]+": "+str(g["passed"]) for g in doc["gates"])
    if doc.get("failure"):
        lines.extend(["","## Actual failure","",json.dumps(doc["failure"],ensure_ascii=False)])
    if doc.get("complete"):
        c=doc["complete_root_E_conclusion"];op=doc["complete_local_operator_conclusion"]
        cp=doc["complete_comparison_conclusion"];result=doc["complete_source_conclusion"]
        lines.extend(["","## The same canonical root factor and new image","",
            "- b0=T^2*b2, with the derivative at fixed canonical X.",
            "- Physical E strip: "+c["exact_new_physical_E_strip"],
            "- Original canonical radius: "+c["exact_original_canonical_radius"],
            "- Original canonical X strip: "+c["exact_original_canonical_strip"],
            "- Accepted full negative T image: "+c["accepted_negative_T_image"]["ball"],
            "- Accepted fixed-X T derivative margin: "+c["accepted_canonical_T_margin"]["ball"],
            "- New complete X image: "+c["new_complete_X_image_upper"]["ball"],
            "- New positive canonical X margin: "+c["new_complete_X_margin_lower"]["ball"],
            "- Original full b2 modulus: "+c["original_complete_b2_modulus"]["ball"],
            "- New complete b2_T modulus: "+c["new_complete_b2T_modulus"]["ball"],
            "- Complete b0 modulus: "+c["complete_b0_modulus"]["ball"],
            "- Complete 2 b0_T+cT b0 modulus: "+c["complete_two_b0T_plus_cT_b0_modulus"]["ball"],
            "- New complete E holomorphic modulus: "+c["new_complete_E_holomorphic_modulus"]["ball"],
            "- The second E component is exactly zero; no physical mean equation is removed.",
            "","| Angle order | New complete E bound | Retained complete E bound |","| --- | --- | --- |"])
        for q in range(3):
            lines.append("| "+str(q)+" | "+c["new_complete_E_first_component_angular_upper"][q]["ball"]+" | "+
                c["retained_complete_E_first_component_angular_upper"][q]["ball"]+" |")
        lines.extend(["","## Complete operator recombination","",
            "- Accepted M E operator: "+op["accepted_complete_M_E_operator_upper"]["ball"],
            "- New complete E operator: "+op["new_complete_E_operator_upper"]["ball"],
            "- Retained complete E operator: "+op["retained_complete_E_operator_upper"]["ball"],
            "- Seven saved non-E whole summands: "+op["complete_non_E_sum_upper"]["ball"],
            "- New complete raw1 operator: "+op["complete_first_local_raw_operator_upper"]["ball"],
            "- No old upper bound is subtracted from another upper bound.",
            "- The common column envelope remains abs(rho)^(-1/4), with raw input weight1 and no mu division.",
            "","| Accepted M complete non-E summand | Unchanged bound |","| --- | --- |"])
        for k,v in op["accepted_seven_complete_M_non_E_summands"].items():
            lines.append("| "+k+" | "+v["ball"]+" |")
        lines.extend(["","## Same complete source comparison","",
            "- Current complete local1: "+cp["accepted_current_complete_term_L2_upper"]["ball"],
            "- Complete comparison factor: "+cp["complete_uniform_comparison_factor"]["ball"],
            "- Retained complete local1: "+cp["retained_complete_term_L2_upper"]["ball"],
            "- Strict improvement: "+str(cp["strict_complete_term_improvement"]),
            "- The positive denominator is an original algorithm budget number, not a function lower.",
            "","## Complete retained negative source",""])
        for k in ("local_L2_upper","nonlocal_total_L2_upper","first_L2_upper","mean_L2_upper","combined_L2_upper"):
            lines.append("- "+k+": "+result[k]["ball"])
        lines.extend(["","| Full first source term | Complete L2 upper |","| --- | --- |"])
        for k,v in sorted(result["complete_first_source_term_L2_upper"].items()):
            lines.append("| "+k+" | "+v["ball"]+" |")
        lines.extend(["","| Independent physical mean term | Complete L2 upper |","| --- | --- |"])
        for k,v in sorted(result["complete_independent_mean_term_L2_upper"].items()):
            lines.append("| "+k+" | "+v["ball"]+" |")
    lines.extend(["","## Scope","",
        "Only local_raw_1 on the original negative part of piece2549 may change. The latest SV improvements and every other30 term ball are retained.",
        "The original six physical intersections, uncertain-root charge, full means, both signs and columns, true dr and both source windows remain unchanged.",
        "No accepted mixed derivative, fold, potential, connection closure, profile, positive calibration, source row or radial integral is recomputed.",
        "A large or smaller upper bound is not a lower bound for true error. This does not prove a high BVP inverse, positive growing-column bound or strong return contraction.",
        "New native and intermediate arrays are temporary; only script parameters run hashes and bounded final conclusions are published.",""])
    return "\n".join(lines)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo",type=Path,required=True);p.add_argument("--manifest",type=Path,required=True)
    p.add_argument("--manifest-sha",required=True);p.add_argument("--out-dir",type=Path,required=True)
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("all new mathematics requires this public Actions repository")
    ctx.prec=320;ctx.cap=8
    runtime=dict(python=platform.python_version(),python_flint=flint.__version__,numpy=numpy.__version__,scipy=scipy.__version__)
    if runtime!=RUNTIME:raise ValueError("the accepted scientific runtime changed")
    a.out_dir.mkdir(parents=True,exist_ok=True);source=sha(__file__);started=time.monotonic()
    h=ROOTS[1]-PIECE[0]
    doc=dict(kind=KIND,public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=source,input_manifest_sha256=a.manifest_sha,runtime=runtime,arithmetic_bits=320,
        complete=False,proved=False,actual_returncode=1,failure=None,gates=[],
        original_complete_fold_stages_read=0,original_successful_small_receipts_read=0,
        original_positive_linear_coefficients_read=0,original_complete_source_terms_read=0,
        original_complete_M_non_E_summands_read=0,
        new_physical_image_and_margin_bounds=0,new_complete_b2T_bounds=0,
        new_complete_E_holomorphic_bounds=0,new_complete_E_angular_bounds=0,
        new_complete_E_operator_bounds=0,new_complete_non_E_scalar_sums=0,
        new_complete_local_operator_recombinations=0,new_complete_uniform_term_comparisons=0,
        new_complete_scalar_recombinations=0,old_numerical_enclosures_recomputed=0,
        old_target_FFT_intrinsic_repair_fold_or_Taylor_recomputed=0,
        old_signed_coefficients_Fourier_norms_potential_or_transport_recomputed=0,
        old_M_mixed_derivatives_or_local_summands_recomputed=0,
        old_SV_inverse_column_or_words_recomputed=0,
        old_RV_AJ_geometry_profile_or_calibration_recomputed=0,
        old_source_row_or_radial_integral_recomputed=0,new_radial_integrals_computed=0,
        original_natural_stage_bytes_modified=0,full_physical_negative_volume_source_paid=False,
        full_high_inverse_claimed=False,reproducible_outputs_published_to_repository=False,
        reproducible_outputs_uploaded_to_Releases=False,new_reproducible_data_artifact_uploaded=False)
    temporary={}
    def gate(name,condition):
        doc["gates"].append(dict(name=name,passed=bool(condition)))
        if not condition:raise ValueError(name)
    try:
        m=read(a.manifest);doc["mathematical_parameters"]=parameters()
        gate("the exact new-only manifest parameters and source identity are fixed",
            sha(a.manifest)==a.manifest_sha and m["public_repository"]==PUBLIC
            and m["scientific_source_sha256"]==source and m["mathematical_parameters"]==parameters())
        pins={e["path"]:e for e in m["files"]}
        if len(pins)!=len(m["files"]):raise ValueError("duplicate immutable input path")
        for e in m["files"]:
            rel=Path(e["path"]);f=a.repo/rel
            if rel.is_absolute() or ".." in rel.parts or not str(rel).startswith(TOPIC):
                raise ValueError("immutable input left the topic")
            if not f.is_file() or f.stat().st_size!=e["bytes"] or sha(f)!=e["sha256"]:
                raise ValueError("changed immutable input "+str(rel))
        if any(v not in pins for v in m["input_paths"].values()):raise ValueError("unlisted complete input role")
        paths={k:a.repo/v for k,v in m["input_paths"].items()}
        expected=dict(contract=CONTRACT,old_fold_majorants_stage=MAJORANTS,
            adjacent_process=APROC,adjacent_publication=APUB,
            original_fold_algorithm="410675cf78dd30d97ff052558df1a819977291d40c628211fcf623ffc0b5f783",
            original_factored_algorithm="a705c2b4c64393e3ba1ae1e043d0fbd62f516a7a80e03e47ce11820626373ee7",
            original_positive_algorithm=RECEIPTS["positive_execution"][1],
            original_M_algorithm=RECEIPTS["mixed_execution"][1],
            original_M_manifest=RECEIPTS["mixed_execution"][2],
            original_baseline_algorithm=RECEIPTS["baseline_execution"][1],
            original_baseline_manifest=RECEIPTS["baseline_execution"][2])
        gate("all accepted algorithms manifests executions and the single natural fold stage keep their immutable hashes",
            all(sha(paths[k])==v for k,v in expected.items())
            and all(sha(paths[k])==identity[3] for k,identity in RECEIPTS.items()))
        data=read_original_fold(paths,gate);f=data["fold"]
        doc["original_complete_fold_stages_read"]=1
        receipts={k:accepted(paths[k],identity,gate) for k,identity in RECEIPTS.items()}
        doc["original_successful_small_receipts_read"]=len(receipts)
        C=receipts["positive_execution"];D=receipts["directed_execution"]
        P=receipts["potential_execution"];AJ=receipts["AJ_execution"];RV=receipts["RV_execution"]
        M=receipts["mixed_execution"];baseline=receipts["baseline_execution"]
        mm=read(paths["original_M_manifest"]);bm=read(paths["original_baseline_manifest"])
        gate("the complete M summands and latest SV ledger keep the same genuine correction all means and original local weights",
            mm["scientific_source_sha256"]==RECEIPTS["mixed_execution"][1]
            and bm["scientific_source_sha256"]==RECEIPTS["baseline_execution"][1]
            and M["scope"]["original_fixed_intrinsic_parameter"]=="eta_0"
            and M["scope"]["same_genuine_first_correction_and_root_gauge"]
            and M["scope"]["full_amplitude_mean_and_independent_physical_even_mean_retained"]
            and M["scope"]["physical_J_only_on_its_proved_reflected_parity_domain"]
            and M["new_complete_mixed_derivative_bounds"]==10 and M["new_fourth_angle_conversions"]==2
            and M["old_numerical_enclosures_recomputed"]==0
            and M["full_physical_negative_volume_source_paid"] and baseline["full_physical_negative_volume_source_paid"]
            and not M["full_high_inverse_claimed"] and not baseline["full_high_inverse_claimed"])
        fs=paths["original_fold_algorithm"].read_text()
        gs=paths["original_factored_algorithm"].read_text();ms=paths["original_M_algorithm"].read_text()
        gate("the saved canonical b2 modulus full-SG connection and seven complete summands have their original meanings",
            'LAM=Q(9,2)' in fs and 'SF=Q(1,64)' in fs
            and 'B2=(ex(Q(4,5))*G*E*c["ap"]*D[2]*powr(Am,Q(-5,3))' in fs
            and 'exact_canonical_radius=str(LAM*R/2),exact_canonical_width=str(SF)' in fs
            and 'Xr=(D[0]*E+ex(Q(2,3))*c["ap"]*r*r*BA).upper()' in fs
            and 'ct=cauchy(c0,SG,3)' in gs
            and 'groups["leading_E_row"][i]=list(C["E"]) if i==0 else [arb(0)]*3' in ms
            and 'groupvalues={k:positive_operator(positive,v) for k,v in groups.items()}' in ms)
        Ejets,closure=root_E_budget(f,P,AJ,RV,M,h,gate)
        doc.update(new_physical_image_and_margin_bounds=2,new_complete_b2T_bounds=1,
            new_complete_E_holomorphic_bounds=1,new_complete_E_angular_bounds=3,
            complete_root_E_conclusion=closure)
        positive=read_positive_coefficients(C,gate)
        value,op=recombine_local(M,positive,Ejets,gate)
        doc.update(original_positive_linear_coefficients_read=18,original_complete_M_non_E_summands_read=7,
            new_complete_E_operator_bounds=1,new_complete_non_E_scalar_sums=1,
            new_complete_local_operator_recombinations=1,complete_local_operator_conclusion=op)
        result,comparison=compare_and_combine(C,D,M,baseline,value,gate)
        doc.update(original_complete_source_terms_read=31,new_complete_uniform_term_comparisons=1,
            new_complete_scalar_recombinations=3,complete_source_conclusion=result,
            complete_comparison_conclusion=comparison,
            strictly_smaller_complete_local_terms=int(comparison["strict_complete_term_improvement"]))
        gate("the complete resulting first and independent mean rows are finite and retain the same source windows",
            all(bound(result[k],k).is_finite() for k in
                ("local_L2_upper","nonlocal_total_L2_upper","first_L2_upper","mean_L2_upper","combined_L2_upper"))
            and result["actual_dr_measure"] and result["one_sided_uncertain_root_band_retained"]
            and result["both_density_windows_retained"] and result["old_nine_word_and_five_physical_mean_counts"]==[9,5])
        doc["scope"]=dict(original_physical_root_piece_2549_only=True,original_fixed_intrinsic_parameter="eta_0",
            full_complex_delta_and_z_squares_for_coefficient_bounds=True,
            final_operators_restrict_to_original_real_parameters=True,
            both_genuine_columns_and_both_carrier_signs=True,all_input_abs_j_at_least97=True,
            same_genuine_first_correction_and_root_gauge=True,
            exact_second_order_leading_root_factor_retained=True,
            fixed_X_canonical_derivative_not_old_radial_derivative=True,
            complete_E_first_row_and_exact_zero_second_component=True,
            original_full_radial_mean_gauge_retained=True,
            seven_complete_M_non_E_summands_read_verbatim=True,
            successful_M_mixed_derivatives_not_recomputed=True,
            accepted_SV_complete_improvements_retained=True,
            only_local_raw1_replaced=True,all_other_thirty_term_balls_unchanged=True,
            full_amplitude_mean_and_independent_physical_even_mean_retained=True,
            both_J_windows_true_dr_and_uncertain_root_charge_retained=True,
            physical_J_only_on_its_proved_reflected_parity_domain=True,
            original_physical_seams_reference_jumps_forcing_and_positive_ports_retained=True,
            original_target_intrinsic_fold_Taylor_transport_profile_or_source_producer_called=False,
            intermediate_arrays_published=False,physical_to_wave_readout_changed=False,
            full_negative_BVP_inverse_paid=False,positive_growing_column_operator_paid=False,
            cutoff97_strong_return_contraction_paid=False)
        temporary.update(complete_new_E_jet=encode(Ejets),
            accepted_seven_M_summand_payload_sha256=payload_sha(op["accepted_seven_complete_M_non_E_summands"]),
            accepted_positive_coefficients_payload_sha256=payload_sha(C["complete_positive_linear_operator_conclusion"]))
        doc.update(complete=True,proved=True,actual_returncode=0,full_physical_negative_volume_source_paid=True)
    except BaseException as error:
        doc["failure"]=dict(type=type(error).__name__,message=str(error))
    finally:
        doc["actual_mathematical_wall_seconds"]=time.monotonic()-started
        temporary.update(kind=KIND,source_sha256=source,input_manifest_sha256=a.manifest_sha,complete_conclusions=doc)
        native=a.out_dir/"temporary-retained-leading-root-zero-E-row.json.gz"
        save(native,temporary,True)
        doc["temporary_native_sha256"]=sha(native);doc["temporary_native_bytes"]=native.stat().st_size
        doc["temporary_native_is_not_published"]=True;actual=doc["actual_returncode"]
        try:
            report=render(doc)
            raw=(json.dumps(doc,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
            if len(raw)>60000 or len(report.encode())>60000:raise ValueError("small conclusion or process exceeded60000 bytes")
            save(a.out_dir/"process.json",doc);(a.out_dir/"conclusion.md").write_text(report)
        except BaseException as error:
            small={k:v for k,v in doc.items() if k not in
                ("complete_root_E_conclusion","complete_local_operator_conclusion",
                 "complete_comparison_conclusion","complete_source_conclusion")}
            small["actual_scientific_returncode"]=actual
            small["formatting_failure"]=dict(type=type(error).__name__,message=str(error))
            small.update(complete=False,proved=False,actual_returncode=2)
            save(a.out_dir/"process.json",small)
            (a.out_dir/"conclusion.md").write_text("# Root-factor E consumer: formatter failure\n\n"+json.dumps(small,ensure_ascii=False)+"\n")
            raise SystemExit(2)
    if doc["actual_returncode"]!=0:raise SystemExit(doc["actual_returncode"])

if __name__=="__main__":main()
