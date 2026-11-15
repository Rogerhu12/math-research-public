#!/usr/bin/env python3
"""Recover positive accepted budget parts and pay a new full Taylor tail.

All original coefficients, Fourier norms, forcing, profiles, source rows and
radial integrals are restored. Only a new amplitude product, six complete
tails, two positive-addend comparisons and scalar ledger updates are computed.
Complete intermediate data remain temporary on the public Actions runner.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,math,os,platform,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy,scipy
from flint import arb,ctx

PUBLIC="Rogerhu12/math-research-public"
TOPIC="topics/visible-flex-exact-nearby/"
KIND="actual_positive_budget_separation_and_refined_first_local_Taylor_tail_v1"
CONTRACT="fedf17ff38a0ed7fca1647e016b5fe0144705194d254c36de3c828c121001470"
MAJORANTS="29ee1093b7644143c693283f774294c176a7f0989b42c004d384a856d5be5144"
APROC="9e8f1f92660c1b44aa3c5c389a2c621a14aa65611cb0cf4c3a98daac1613a89b"
APUB="0cfbfcd3866c4fda4fd31020efa630c8e3b5e7e24fc6fafe1219a2e84a3efe3c"
LEGACY_SOURCE="f553b1506dde1b1d80119fb77b084a43ee19e08e17f32f7139a4a1dddf53a739"
LEGACY_HELPER="1860872f56baf809517693473bb43cb3e897c2c082c5b2e6b7b38cfeaa59eb53"
LEGACY_MANIFEST="76cf792e1e223e4b45487f90c9a44dd64fcaf32e46c0f1a0a46f442eb4faa18a"
S_EXEC="3896925b758840c4bbf2ce910141ca8a93d725d56bf22b5002e9c0b2486004af"
S_SOURCE="564759dceb4b38dd37fdd275d0fa3e22cdf2efa271cd9ef1049c6cfa4ff121f6"
S_MANIFEST="a6fbb28de8a85bd6f71054df0056a869285f131cc4c4702c66e5434deb7061cf"
C_EXEC="bca0f97d7c610f8f2572e61d1e1442a8b9c256a4c5429253682b6d803e3a21c3"
C_SOURCE="b0648a3bc244e6671176ac096c759b3e70e57d8c04b75bd4dd74442bfcaf95c0"
C_MANIFEST="8465759dfe9101bb7e20275cec1a5b98e23efb4dbe643e492fb8189250b005b9"
D_EXEC="2c5cba2e7351267e090d0ca6c06cfecbb21309c039a7844937ee64026254f1d0"
D_SOURCE="1aa46093bba5150d636cc7c6ef4f5b080447fc2c75d7438b2e52ae5fa6b5d0af"
D_MANIFEST="5ce9aceb3be46e795696c09028f39091fdc9a4f969dba0e0b317408974083e9b"
RG=Q(3,8000);SG=Q(3,128);CW=Q(1,32)
RT=Q(3,5000);SA=Q(13,2048);SX=Q(1,128);DX=Q(1,1024)
RS=Q(1,8000);SS=Q(3,512);RF=Q(3,20000);SF=Q(1,64)
R0=Q(1,6000);RA=Q(3,40000);SIGMA0=Q(1,128);LAM=Q(9,2)
W_EXEC="777e681b85beb3317853d05d1c39a35703133a7cd49c81286571d21a89fa5dd1"
W_SOURCE="a0f12f84d55c4735507e71e40d35cd343777d00dad4b5ec5c2e73804230198be"
W_MANIFEST="11e993bae75adf3a667ba7f7d8c28f9fb38f3fde8d12e34df938c82baef2ea65"
G_EXEC="1fe8a528ec5e22dedc0803a129591de2fd3f25d148c5e57cb1c619cc06463bc1"
G_SOURCE="617bf821e9cff5847b4257e448fe8556eda63acf5c018105a2dff32ac452cf8a"
G_MANIFEST="aadf3e2bcf02d818e12c8950b4b4eb523345a4a63777a16d39720f98040a5e3f"
L_EXEC="8cc43eb17f28b6b3fd82b9a220e8db86c7eb53fa7c491d0de7f8feda70bfc926"
L_SOURCE="c479aaec9438a80340e425223b2eac0ed9b5707583c6a8125553e59ccd189048"
L_MANIFEST="8113b0d7e73c220a766947c198c09b6e66bd3a83210539fed6b4d6d5285e8e3f"
H=Q(893368603925465506687,21990232555520000000000000)
ROOTS=(Q(1191984371497,5000000000000),Q(2383968743003,10000000000000))
PIECE=(Q(2147184947341121,9007199254740992),Q(4295308144604611,18014398509481984))
BRANCHES=("central","positive_characteristic","negative_characteristic")
RUNTIME=dict(python="3.12.14",python_flint="0.9.0",numpy="2.3.5",scipy="1.17.0")

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ex(x):
    v=Q(x);return arb(v.numerator)/arb(v.denominator)
def rb(v):
    if isinstance(v,arb):return v
    if isinstance(v,(int,Q)):return ex(v)
    if isinstance(v,str):return arb(v)
    return arb(v["ball"])
def up(v):return abs(rb(v)).upper()
def gap(v,label):
    v=rb(v).lower()
    if not v.is_finite() or not v>0:raise ValueError("missing complete positive gap: "+label)
    return v
def bound(v,label):
    v=rb(v)
    if not v.is_finite() or v.lower()<0:raise ValueError("invalid complete upper bound: "+label)
    return v.upper()
def powr(v,p):return (rb(v).log()*ex(p)).exp()
def rec(v):return dict(ball=rb(v).str(64))
def unpack(v):
    if isinstance(v,dict):
        if set(v)=={"ball"}:return arb(v["ball"])
        return {k:unpack(x) for k,x in v.items()}
    if isinstance(v,list):return [unpack(x) for x in v]
    return v
def encode(v):
    if isinstance(v,arb):return rec(v)
    if isinstance(v,Q):return str(v)
    if isinstance(v,dict):return {str(k):encode(x) for k,x in v.items()}
    if isinstance(v,(tuple,list)):return [encode(x) for x in v]
    return v
def read(p):
    p=Path(p);b=p.read_bytes()
    return json.loads(gzip.decompress(b) if p.suffix==".gz" else b)
def payload_sha(v):
    return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(",",":"),
        ensure_ascii=False,allow_nan=False).encode()).hexdigest()
def save(p,v,compressed=False):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    b=(json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
    t=p.with_name(p.name+".partial");t.write_bytes(gzip.compress(b,mtime=0) if compressed else b);t.replace(p)
def receipt(path,run,source,manifest,gate):
    e=read(path);r=e.get("actual_scientific_receipt",{})
    gate("accepted complete run "+run+"/1 is restored with its exact scientific identity",
        str(e.get("run_id"))==run and str(e.get("run_attempt"))=="1"
        and e.get("complete") is True and e.get("actual_returncode")==0 and e.get("actual_failure") is None
        and e.get("source_budget_source_sha256")==source and e.get("input_manifest_sha256")==manifest
        and r.get("complete") is True and r.get("proved") is True and r.get("actual_returncode")==0
        and r.get("failure") is None and r.get("source_sha256")==source
        and r.get("input_manifest_sha256")==manifest and r.get("runtime")==RUNTIME
        and r.get("gates") and all(g.get("passed") is True for g in r["gates"]))
    return r


def nonnegative_lower(v,label):
    """A lower bound for an accepted nonnegative numerical budget, never for a function."""
    v=rb(v)
    if not v.is_finite() or v.upper()<0:raise ValueError("invalid positive budget: "+label)
    return max(arb(0),v.lower())

def positive_difference_upper(total,lower,label):
    """B3: subtract a certified lower of the identical positive arithmetic addend."""
    total=bound(total,label+" total");lower=rb(lower)
    if not lower.is_finite() or lower.lower()<0:raise ValueError("invalid subtracted lower: "+label)
    value=(total-lower.lower()).upper()
    if not value.is_finite() or value.lower()<0:
        raise ValueError("same-positive-addend consistency failed: "+label)
    return value

def complete_amplitude_product(f,m,S,gate):
    """A genuinely new product; the original forcing and fold are only read."""
    sd=S["complete_domain_conclusion"]
    gT=gap(sd["canonical_inverse_radial_gap"],"accepted complete T/rho gap")
    image=gap(sd["common_T_image"],"accepted common radial T image")
    Aplus=bound(f["Ap"],"accepted original A modulus")
    B=bound(f["B"],"accepted inverse angle displacement")
    if m["chi"][1:]!=[str(RG),str(SG)]:
        raise ValueError("the complete rooted angle displacement product changed")
    chi=bound(m["chi"][0],"complete original chi")
    preimage=(ex(RT)/gT).upper()
    Timage=(ex(RS)*powr(Aplus,Q(2,3))).upper()
    Ximage=(ex(SS)+ex(RS/RG)*chi).upper()
    optical=(ex(Q(2,3))*powr(ex(RT),Q(3,2))).upper()
    margins=dict(whole_physical_radius=(ex(RS-H)).lower(),
        forcing_preimage=(ex(RF)-preimage).lower(),
        original_inverse_radius=ex(LAM*RG/2-RT).lower(),
        forcing_angle=(ex(SF-SX)-B).lower(),
        common_potential_image=(image-ex(RT)).lower(),
        complete_regular_ray=(ex(SX-SA-DX)-optical).lower(),
        old_product_T_image=(ex(RT)-Timage).lower(),
        old_product_X_image=(ex(SA)-Ximage).lower())
    gate("the new complete amplitude product and both regular paths fit the identical accepted forcing and inverse domains",
        H<RS<RF<RG and RT>Q(1,2000) and SS>SIGMA0/2
        and 0<SA<SX<SF and all(v.is_finite() and v>0 for v in margins.values()))
    M=bound(f["M"],"complete canonical leading coefficient")
    B2=bound(f["B2"],"complete canonical b0 over T squared")
    Bi=bound(f["Bi"],"complete inverse leading branch")
    Fa=bound(S["complete_forcing_conclusion"]["raw_fa"],"accepted complete raw fa")
    Fb=bound(S["complete_forcing_conclusion"]["raw_fb"],"accepted complete raw fb")
    rt=ex(RT);dx=ex(DX)
    bstar=(M+B2*powr(rt,Q(5,2))).upper()
    common=(bstar*Bi).upper()
    aa=(common*rt*Fa/2+(common*rt*rt/(2*dx)
        +B2*Bi*(1+common/6)*rt**3)*Fb).upper()
    bb=(common*Fb+(common*rt*rt/(5*dx)
        +B2*Bi*(ex(Q(1,2))+common/7)*rt**3)*Fa).upper()
    gate("the same regular normalized correction has finite complete moduli on the new product",
        all(v.is_finite() and v.lower()>=0 for v in (aa,bb))
        and S["complete_amplitude_conclusion"]["exact_regular_root_normalization_retained"]
        and S["complete_amplitude_conclusion"]["full_raw_forcing_used"])
    conclusion=dict(exact_new_canonical_radius=str(RT),exact_new_canonical_strip=str(SA),
        exact_new_old_rho_radius=str(RS),exact_new_old_phi_strip=str(SS),
        exact_forcing_old_rho_radius=str(RF),exact_forcing_old_phi_strip=str(SF),
        exact_canonical_forcing_strip=str(SX),exact_quotient_Cauchy_width=str(DX),
        exact_full_physical_cover=str(H),complete_domain_gaps=encode(margins),
        complete_old_product_T_image_upper=rec(Timage),complete_old_product_X_image_upper=rec(Ximage),
        complete_inverse_preimage_radius_upper=rec(preimage),
        accepted_same_T_over_rho_gap=rec(gT),accepted_common_T_image=rec(image),
        complete_new_amplitude_modulus=dict(a1=rec(aa),b1=rec(bb)),
        all_sT_paths_in_same_paid_domain=True,root_normalization_and_all_means_unchanged=True,
        original_forcing_and_fold_recomputed=False)
    return dict(a1=aa,b1=bb),conclusion,dict(bstar=rec(bstar),common=rec(common))

def radial_tail_expression(M,R,p):
    """Unrounded interval expression for the entire n>=13 tail, not an old norm call."""
    if p!=2 or not 0<H<R:raise ValueError("only the six declared second-derivative comparisons are paid")
    t=ex(H/R);d=1-t
    gap(d,"infinite radial tail margin")
    kernel=t**11*(156/d+26*t/(d*d)+2*t*t/(d*d*d))
    return rb(M)*ex(R**(-2))*kernel

def angular_tail_expression(width,q):
    """Both Fourier signs; q=0 includes the exact zero mode."""
    if not Q(width)>0 or q not in (0,1,2):
        raise ValueError("the complete Fourier tail needs its declared positive strip")
    r=(-4*ex(width)).exp();d=1-r
    gap(d,"infinite Fourier tail margin")
    if q==0:return (1+r)/d
    if q==1:return 8*r/(d*d)
    return 32*r*(1+r)/(d*d*d)

def second_derivative_rows(receipt,whole):
    cases=[c for c in receipt["cases"] if Q(c["exact_output_old_phi_width"])==0]
    if len(cases)!=1:raise ValueError("the accepted real-circle amplitude table is not unique")
    case=cases[0]
    cover=case["exact_whole_piece_cover_radius" if whole else "exact_whole_physical_cover_radius"]
    if Q(cover)!=H:raise ValueError("the complete physical root-piece cover changed")
    if whole and not (case["complete"] and case["proved"]):
        raise ValueError("the original complete Taylor case did not succeed")
    out={}
    for name in ("a1","b1"):
        fields=[f for f in case["fields"] if f["field"]==name]
        if len(fields)!=1:raise ValueError("the accepted amplitude field is not unique")
        field=fields[0]
        if not (Q(field["exact_output_old_phi_width"])==0
            and field["joint_sum_of_radial_coefficient_suprema"]
            and field["amplitude_mean_is_not_independent_physical_even_mean"]):
            raise ValueError("the accepted complete amplitude norm or mean convention changed")
        if whole and not (field["finite_signed_addition_precedes_modulus_and_sum"]
            and field["full_output_zero_mode_retained"] and Q(field["old_tail_radius"])==R0
            and Q(field["added_term_tail_radius"])==RA and Q(field["common_outer_angle_strip"])==SIGMA0):
            raise ValueError("the original signed finite sum or exact positive tail recipe changed")
        if not whole and not (field["original_complete_bound_only_read"]
            and field["full_radial_and_Fourier_tails_retained"]):
            raise ValueError("the accepted scalar output omitted a complete tail")
        rows=[r for r in field["complete_mixed_derivative_rows"] if r["radial_derivative_order"]==2]
        if len(rows)!=1 or rows[0]["angular_derivative_orders"]!=[0,1,2,3]:
            raise ValueError("the accepted ordinary derivative row changed")
        vals=rows[0]["complete_joint_Wiener_upper"]
        if len(vals)!=4:raise ValueError("the complete angular derivative row is truncated")
        out[name]=vals[:3]
    return out

def recover_and_replace_tails(W,S,moduli,gate):
    """Six old positive addend lowers; no old coefficient or finite norm is recomputed."""
    old=second_derivative_rows(W,True);scalar=second_derivative_rows(S,False)
    tails=W["complete_tail_conclusion"]
    gate("the saved whole Taylor total is the original finite sum plus its two positive complete tails",
        tails["first_omitted_Taylor_degree"]==13 and Q(tails["old_radius"])==R0
        and Q(tails["new_added_term_radius"])==RA and Q(tails["outer_old_phi_strip"])==SIGMA0
        and tails["exact_delta_a1_radial_zero_order"]==3
        and tails["no_radius_scaling_applied_to_other_terms"]
        and tails["no_uncomputed_finite_coefficient_was_set_to_zero"]
        and tails["angular_tails_from_joint_double_Cauchy"])
    selected={};published=[];temporary=[]
    for name in ("a1","b1"):
        mold=nonnegative_lower(tails["unchanged_original_full_product_modulus"][name],name+" old positive modulus")
        madd=nonnegative_lower(tails["complete_added_term_full_product_modulus"][name],name+" added positive modulus")
        selected[name]=[]
        for q in (0,1,2):
            # All arithmetic before lower() is a full ball expression. The old
            # algorithm rounded these positive factors up, so this is a lower
            # for its actual numerical tail addend, not an error lower bound.
            previous_tail=(radial_tail_expression(mold,R0,2)+radial_tail_expression(madd,RA,2)
                )*angular_tail_expression(SIGMA0,q)
            lower=nonnegative_lower(previous_tail,name+" identical old tail addend")
            finite=positive_difference_upper(old[name][q],lower,name+" finite p2 q"+str(q))
            fresh_tail=(radial_tail_expression(moduli[name],RS,2)*angular_tail_expression(SS,q)).upper()
            candidate=(finite+fresh_tail).upper()
            complete=min(candidate,bound(old[name][q],"old complete Taylor bound"),
                bound(scalar[name][q],"old complete scalar bound")).upper()
            if not complete.is_finite() or complete.lower()<0:
                raise ValueError("a new complete Taylor derivative comparison failed")
            selected[name].append(complete)
            published.append(dict(field=name,ordinary_radial_derivative_order=2,physical_angle_derivative_order=q,
                complete_joint_Wiener_upper=rec(complete),
                strictly_smaller_than_accepted_scalar_budget=bool(complete<rb(scalar[name][q]).lower()),
                full_zero_mode_in_q0_retained=(q==0),first_omitted_degree=13))
            temporary.append(dict(field=name,q=q,accepted_complete_total=old[name][q],
                lower_for_same_algorithm_positive_tail=rec(lower),recovered_positive_finite_budget_upper=rec(finite),
                new_complete_infinite_tail_upper=rec(fresh_tail),new_unintersected_complete_upper=rec(candidate),
                accepted_scalar_complete_upper=scalar[name][q]))
    gate("exactly six whole-piece derivatives retain all finite coefficients and the entire new radial and Fourier tail",
        len(published)==6 and all(v.is_finite() and v.lower()>=0
            for values in selected.values() for v in values))
    return selected,scalar,published,temporary

def read_positive_coefficients(C,gate):
    rows=C["complete_positive_linear_operator_conclusion"]
    gate("the eighteen accepted positive coefficients retain the identical complete profile branches and input ordering",
        len(rows)==3 and [r["branch"] for r in rows]==list(BRANCHES)
        and all(r["exact_input_component_order"]==["a","a_phi","a_phiphi","b","b_phi","b_phiphi"]
            and len(r["complete_positive_linear_coefficients"])==6
            and len(r["selected_inputs"])==6
            and all(v["denominator_is_lower_for_bound_number_only"] for v in r["selected_inputs"]) for r in rows)
        and C["scope"]["both_genuine_columns_and_both_carrier_signs"]
        and C["scope"]["all_input_abs_j_at_least97"]
        and C["scope"]["budget_parameter_lower_is_not_true_amplitude_lower"])
    return [[rb(v) for v in r["complete_positive_linear_coefficients"]] for r in rows]

def recover_complete_rest(C,G,coeff,old_inputs,new_inputs,gate):
    """B17--20: a common positive addend for both sides of the exact old minimum."""
    rows=G["operator_rows"]
    if not (len(rows)==4 and [r["radial_derivative_order"] for r in rows]==[0,0,1,2]
        and all(r["mean_output_included"] and r["actual_radial_measure"] for r in rows)
        and rows[3]["only_amplitude_radial_derivative"]
        and rows[3]["original_complete_amplitude_table_recomputed"] is False):
        raise ValueError("the accepted complete w1rr operator identity changed")
    known=rows[3]["complete_rho_minus_quarter_operator_coefficient"]
    oldvec=[v for name in ("a1","b1") for v in old_inputs[name]]
    newvec=[v for name in ("a1","b1") for v in new_inputs[name]]
    coefflo=[[nonnegative_lower(v,"accepted positive coefficient") for v in row] for row in coeff]
    coeffhi=[[bound(v,"accepted positive coefficient") for v in row] for row in coeff]
    oldlo=[nonnegative_lower(v,"old C numerical w1rr input") for v in oldvec]
    lower_linear=sum((sum((row[i]*oldlo[i] for i in range(6)),arb(0))
        for row in coefflo),arb(0)).lower()
    lower_common=min(lower_linear,nonnegative_lower(known,"accepted complete w1rr budget")).lower()
    local=C["complete_local_vector_conclusion"]
    if not (local["raw_numerator_not_divided_by_mu"] and local["original_complete_w1rr_operator_reused"]
        and local["exact_input_weights"]==["1","1/388","1/150544"]
        and local["raw_complete_operator_coefficients"][0]==local["input_weighted_complete_operator_coefficients"][0]):
        raise ValueError("the accepted complete first-local raw-unit identity changed")
    total=local["raw_complete_operator_coefficients"][0]
    rest=positive_difference_upper(total,lower_common,"complete first-local rest")
    newop=sum((sum((row[i]*newvec[i] for i in range(6)),arb(0))
        for row in coeffhi),arb(0)).upper()
    retained=min(newop,bound(known,"accepted complete w1rr operator")).upper()
    complete=(rest+retained).upper()
    gate("both branches of the old complete local minimum share the recovered positive w1rr addend",
        lower_common.is_finite() and lower_common>0 and lower_common<=bound(total,"complete local total")
        and all(v.is_finite() and v.lower()>=0 for v in (rest,newop,retained,complete)))
    conclusion=dict(accepted_complete_first_local_budget=total,
        lower_for_same_positive_wrr_budget_addend=rec(lower_common),
        complete_original_rest_operator_upper=rec(rest),
        new_complete_wrr_operator_upper=rec(newop),
        retained_complete_wrr_operator_upper=rec(retained),
        new_complete_first_local_operator_upper=rec(complete),
        lower_is_for_algorithm_budget_numbers_not_functions=True,
        common_positive_addend_proved_for_both_old_minimum_branches=True,
        complete_old_rest_including_Piola_E12_and_mean_retained=True,
        old_profile_or_old_operator_recomputed=False,
        common_pointwise_radial_envelope="abs(rho)^(-1/4)")
    return complete,conclusion,dict(complete_positive_coefficient_lower=encode(coefflo),
        old_positive_wrr_input_lower=encode(oldlo),complete_linear_addend_lower=rec(lower_linear),
        accepted_wrr_operator=known)

def choose_complete(old,new):
    if up(new)<up(old):return rec(up(new)),bool(up(new)<rb(old).lower())
    return old,False

def compare_and_combine(C,D,L,value,gate):
    local=C["complete_local_vector_conclusion"]
    if D["accepted_complete_local_vector_conclusion"]!=local:
        raise ValueError("the complete C local budget changed in the directed ledger")
    original=D["complete_source_conclusion"];current=L["complete_source_conclusion"]
    terms0=original["complete_first_source_term_L2_upper"];termsP=current["complete_first_source_term_L2_upper"]
    stable=("actual_dr_measure","exact_negative_physical_cover","both_density_windows_retained",
        "one_sided_uncertain_root_band_retained","outer_J_window","input_window","first_output_window",
        "independent_even_mean_window","total_squared_envelope_radial_weight_upper",
        "nonlocal_total_L2_upper","mean_L2_upper","complete_independent_mean_term_L2_upper")
    gate("the accepted first-local update preserves the complete old directed ledger and actual source measure",
        len(terms0)==len(termsP)==21 and all(original[k]==current[k] for k in stable)
        and all(v==termsP[k] for k,v in terms0.items() if k!="local_raw_1")
        and current["only_complete_first_local_vector_replaced"]
        and current["all_other_source_terms_and_mean_balls_read_verbatim"]
        and current["old_source_row_or_radial_integral_recomputed"] is False)
    beta=gap(local["raw_complete_operator_coefficients"][0],"same old complete algorithm coefficient")
    ratio=min(arb(1),(value/beta).upper()).upper()
    candidate=(ratio*bound(terms0["local_raw_1"],"original directed local1 integral")).upper()
    retained,improved=choose_complete(termsP["local_raw_1"],candidate)
    result=dict(current);terms=dict(termsP);terms["local_raw_1"]=retained
    result["complete_first_source_term_L2_upper"]=terms
    local_sum=sum((bound(terms["local_raw_"+str(j)],"complete local term") for j in (1,2,3)),arb(0)).upper()
    result["local_L2_upper"],ilocal=choose_complete(current["local_L2_upper"],local_sum)
    first=(bound(result["local_L2_upper"],"local sum")+bound(current["nonlocal_total_L2_upper"],"nonlocal sum")).upper()
    result["first_L2_upper"],ifirst=choose_complete(current["first_L2_upper"],first)
    pair=(bound(result["first_L2_upper"],"first output")**2+bound(current["mean_L2_upper"],"complete mean")**2).sqrt().upper()
    result["combined_L2_upper"],ipair=choose_complete(current["combined_L2_upper"],pair)
    result["all_other_source_terms_and_mean_balls_read_verbatim"]=True
    result["only_complete_first_local_vector_replaced"]=True
    result["old_source_row_or_radial_integral_recomputed"]=False
    result["accepted_regular_transport_first_local_result_retained"]=True
    result["strictly_smaller_complete_aggregates"]=dict(local=ilocal,first=ifirst,combined=ipair)
    comparison=dict(positive_lower_for_same_old_local_budget=rec(beta),
        new_complete_first_local_operator_upper=rec(value),complete_uniform_comparison_factor=rec(ratio),
        original_directed_complete_local_raw_1_L2=terms0["local_raw_1"],
        accepted_regular_transport_local_raw_1_L2=termsP["local_raw_1"],
        retained_complete_local_raw_1_L2=retained,strict_complete_term_improvement=improved,
        original_six_rows_outer_J_dr_and_uncertain_root_band_retained=True,
        comparison_denominator_is_not_a_function_lower=True)
    return result,comparison

def render(doc):
    lines=["# Actual positive-budget separation and complete first-local Taylor-tail comparison","",
        "This is an actual public-run conclusion. All old coefficients, norms, forcing, profiles, operator words and radial integrals were restored.","",
        "- Complete: "+str(doc["complete"]),
        "- Actual scientific return code: "+str(doc["actual_returncode"]),
        "- Actual failure: "+str(doc["failure"]),
        "- Source SHA256: "+doc["source_sha256"],
        "- Input manifest SHA256: "+doc["input_manifest_sha256"],
        "- Run: "+str(doc["run_id"])+"/"+str(doc["run_attempt"]),
        "- New scalar mathematical seconds: "+str(doc.get("actual_mathematical_wall_seconds")),
        "- Old numerical enclosures recomputed: 0","",
        "The entire original root piece, both signs and genuine columns, full means and true seams are retained. The source update changes only local_raw_1; the other twenty first-output and ten physical-mean terms remain the accepted balls.",""]
    if "complete_domain_conclusion" in doc:
        d=doc["complete_domain_conclusion"]
        lines+=["## New complete product","",
            "| Quantity | Exact value or certified bound |","|---|---|"]
        for name in ("exact_new_canonical_radius","exact_new_canonical_strip","exact_new_old_rho_radius",
            "exact_new_old_phi_strip","exact_forcing_old_rho_radius","exact_forcing_old_phi_strip",
            "exact_canonical_forcing_strip","exact_quotient_Cauchy_width","exact_full_physical_cover"):
            lines.append("| "+name+" | "+d[name]+" |")
        for name,value in d["complete_domain_gaps"].items():lines.append("| "+name+" | "+value["ball"]+" |")
        for name,value in d["complete_new_amplitude_modulus"].items():lines.append("| full "+name+" modulus | "+value["ball"]+" |")
        lines+=["","Every inverse image and regular sT path remains inside the original accepted forcing and reference domains. The new bound identifies the same normalized analytic solution on the overlap.",""]
    if "complete_wrr_derivative_conclusion" in doc:
        lines+=["## Complete second radial derivative bounds","",
            "All omitted degrees n >= 13 and both Fourier tails are included. The q=0 row includes the full Fourier mean; it is not the separate physical mean equation.","",
            "| Field | Physical angle derivative | Complete joint Wiener upper | Strict improvement over accepted scalar budget |",
            "|---|---:|---|---|"]
        for v in doc["complete_wrr_derivative_conclusion"]:
            lines.append("| "+v["field"]+" | "+str(v["physical_angle_derivative_order"])+" | "+
                v["complete_joint_Wiener_upper"]["ball"]+" | "+
                str(v["strictly_smaller_than_accepted_scalar_budget"])+" |")
        lines+=["","The finite-part recovery subtracts a strict lower for the identical old positive numerical tail addend. It does not subtract two unrelated error upper bounds, and no old coefficient or norm is recalculated.",""]
    if "complete_rest_and_local_conclusion" in doc:
        d=doc["complete_rest_and_local_conclusion"]
        lines+=["## Complete operator comparison","",
            "| Quantity | Certified numerical bound |","|---|---|"]
        for name in ("accepted_complete_first_local_budget","lower_for_same_positive_wrr_budget_addend",
            "complete_original_rest_operator_upper","new_complete_wrr_operator_upper",
            "retained_complete_wrr_operator_upper","new_complete_first_local_operator_upper"):
            lines.append("| "+name+" | "+d[name]["ball"]+" |")
        lines+=["","The lower concerns the old algorithm's budget numbers, not a function lower bound. Both branches of the old minimum contain this same positive addend. Every other old raw local term, including Piola, E12, potential and mean terms, remains in the recovered complete rest.",""]
    if "complete_comparison_conclusion" in doc:
        d=doc["complete_comparison_conclusion"]
        lines+=["## Same integrated source ledger","",
            "| Quantity | Certified bound |","|---|---|"]
        for name in ("complete_uniform_comparison_factor","original_directed_complete_local_raw_1_L2",
            "accepted_regular_transport_local_raw_1_L2","retained_complete_local_raw_1_L2"):
            lines.append("| "+name+" | "+d[name]["ball"]+" |")
        c=doc["complete_source_conclusion"]
        for name in ("local_L2_upper","nonlocal_total_L2_upper","first_L2_upper","mean_L2_upper","combined_L2_upper"):
            lines.append("| "+name+" | "+c[name]["ball"]+" |")
        lines+=["","The ratio acts on the complete same-term norm already integrated with its six original rows, outer J factors, true dr and uncertain-root band. The complete accepted P first-local result is retained through a minimum. Neither an old radial weight nor an old source integral is recomputed.",""]
    lines+=["## Actual gates","","| Gate | Passed |","|---|---|"]
    lines +=["| "+g["name"]+" | "+str(g["passed"])+" |" for g in doc["gates"]]
    lines+=["","## Scope","",
        "This is a complete physical negative volume-source comparison on the fixed original root piece. It preserves both source windows, all old-circle terms, independent physical mean equations, ordinary-source ports and actual jumps. It does not establish a full high BVP inverse, positive graph feedback or strong-return smallness. Complete intermediate tables remain temporary; only this small conclusion and execution identity are published.",""]
    return "\n".join(lines)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo",type=Path,required=True);p.add_argument("--manifest",type=Path,required=True)
    p.add_argument("--manifest-sha",required=True);p.add_argument("--out-dir",type=Path,required=True)
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("all new scalar arithmetic is restricted to the public Actions runner")
    ctx.prec=320;ctx.cap=8
    runtime=dict(python=platform.python_version(),python_flint=flint.__version__,numpy=numpy.__version__,scipy=scipy.__version__)
    if runtime!=RUNTIME:raise ValueError("the accepted scientific runtime changed")
    a.out_dir.mkdir(parents=True,exist_ok=True);source=sha(__file__);started=time.monotonic()
    doc=dict(kind=KIND,public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=source,input_manifest_sha256=a.manifest_sha,runtime=runtime,arithmetic_bits=320,
        complete=False,proved=False,actual_returncode=1,failure=None,gates=[],
        original_complete_fold_stages_read=0,original_successful_small_receipts_read=0,
        original_positive_linear_coefficients_read=0,original_complete_source_terms_read=0,
        new_complete_amplitude_product_budgets=0,new_positive_Taylor_tail_lower_comparisons=0,
        new_positive_finite_budget_recoveries=0,new_complete_infinite_Taylor_tail_bounds=0,
        new_complete_wrr_derivative_bounds=0,new_complete_rest_budget_recoveries=0,
        new_fixed_positive_operator_comparisons=0,new_complete_uniform_factors=0,new_complete_scalar_recombinations=0,
        old_numerical_enclosures_recomputed=0,old_finite_Taylor_coefficients_or_Fourier_norms_recomputed=0,
        old_forcing_fold_transport_RF_or_profile_recomputed=0,
        old_operator_words_or_positive_calibration_recomputed=0,old_source_rows_or_radial_integrals_recomputed=0,
        original_natural_stage_bytes_modified=0,full_physical_negative_volume_source_paid=False,
        full_high_inverse_claimed=False,reproducible_outputs_published_to_repository=False,
        reproducible_outputs_uploaded_to_Releases=False,new_reproducible_data_artifact_uploaded=False)
    temporary={}
    def gate(name,condition):
        doc["gates"].append(dict(name=name,passed=bool(condition)))
        if not condition:raise ValueError(name)
    try:
        manifest=read(a.manifest)
        params=dict(cutoff_abs_j=97,physical_frequency="4j",physical_root_piece=2549,
            exact_full_physical_cover=str(H),exact_negative_cover=[str(PIECE[0]),str(ROOTS[1])],
            exact_root_interval=list(map(str,ROOTS)),original_fold_radius=str(RG),original_fold_phi_strip=str(SG),
            accepted_forcing_old_rho_radius=str(RF),accepted_forcing_old_phi_strip=str(SF),
            new_canonical_radius=str(RT),new_canonical_amplitude_strip=str(SA),
            canonical_forcing_strip=str(SX),quotient_Cauchy_width=str(DX),
            new_amplitude_old_rho_radius=str(RS),new_amplitude_old_phi_strip=str(SS),
            old_Taylor_tail_radius=str(R0),old_added_term_tail_radius=str(RA),
            old_Taylor_outer_phi_strip=str(SIGMA0),first_omitted_Taylor_degree=13,
            new_ordinary_radial_derivative_orders=[2],new_physical_angle_derivative_orders=[0,1,2],
            output_old_phi_strip="0",complete_complex_delta_square_halfwidth="1/100000000",
            complete_complex_z_square_halfwidth="1/9409",fixed_intrinsic_parameter="eta_0",
            input_window="H^(-4/3) both genuine columns and both signs",
            first_source_window="ordinary L2_r H^(-2/3)",independent_mean_window="ordinary L2_r constants",
            baseline_complete_source_run="43709396175/1",original_directed_source_run="43703879926/1",
            original_positive_calibration_run="43702688640/1",old_radial_integrations_recomputed=0,
            real_parameter_values_for_final_operator_only=True,arithmetic_bits=320)
        doc["mathematical_parameters"]=params
        gate("the new source and manifest retain their exact reviewed identities and declared products",
            sha(a.manifest)==a.manifest_sha and manifest["public_repository"]==PUBLIC
            and manifest["scientific_source_sha256"]==source and manifest["mathematical_parameters"]==params)
        pins={e["path"]:e for e in manifest["files"]}
        if len(pins)!=len(manifest["files"]):raise ValueError("duplicate immutable input")
        for e in manifest["files"]:
            rel=Path(e["path"]);f=a.repo/rel
            if rel.is_absolute() or ".." in rel.parts or not str(rel).startswith(TOPIC):raise ValueError("input outside topic")
            if not f.is_file() or f.stat().st_size!=e["bytes"] or sha(f)!=e["sha256"]:
                raise ValueError("changed exact input "+str(rel))
        if any(v not in pins for v in manifest["input_paths"].values()):raise ValueError("unpinned required role")
        paths={k:a.repo/v for k,v in manifest["input_paths"].items()}
        expected=dict(contract=CONTRACT,old_fold_majorants_stage=MAJORANTS,adjacent_process=APROC,adjacent_publication=APUB,
            amplitude_execution=S_EXEC,whole_Taylor_execution=W_EXEC,operator_execution=G_EXEC,
            complete_genuine_execution=C_EXEC,directed_source_execution=D_EXEC,first_local_execution=L_EXEC,
            complete_genuine_source=C_SOURCE,directed_source_algorithm=D_SOURCE,
            original_scalar_algorithm=S_SOURCE,original_whole_Taylor_algorithm=W_SOURCE,
            original_operator_algorithm=G_SOURCE,original_first_local_algorithm=L_SOURCE)
        gate("all six successful scientific receipts and their frozen positive algorithms are byte-exact",
            all(sha(paths[k])==v for k,v in expected.items()))
        ms=read(paths["old_fold_majorants_stage"]);ap=read(paths["adjacent_process"]);au=read(paths["adjacent_publication"])
        mr=next(v for v in au["files"] if v["file"]=="consumers/stages/complete-original-reference-holomorphic-majorants.json.gz")
        gate("the complete old fold and holomorphic majorants retain their exact legacy publication identity",
            ms["complete"] and ms["name"]==ms["stage"]=="complete-original-reference-holomorphic-majorants"
            and ms["source_sha256"]==LEGACY_SOURCE and ms["algebra_sha256"]==LEGACY_HELPER
            and ms["input_manifest_sha256"]==LEGACY_MANIFEST and ms["runtime"]==runtime
            and mr["bytes"]==4501 and mr["sha256"]==MAJORANTS and ap["actual_returncode"]==0
            and ap["mathematical_complete"] and ap["mathematical_proved"] and ap["mathematical_failure"] is None
            and au["complete"] and ms["payload"]["majorants"]["A"][1:]==[str(RG),str(SG)])
        old=unpack(ms["payload"]);fold=old["fold"];majorants=old["majorants"]
        doc["original_complete_fold_stages_read"]=1
        S=receipt(paths["amplitude_execution"],"43698106023",S_SOURCE,S_MANIFEST,gate)
        W=receipt(paths["whole_Taylor_execution"],"43694458725",W_SOURCE,W_MANIFEST,gate)
        G=receipt(paths["operator_execution"],"43700281022",G_SOURCE,G_MANIFEST,gate)
        C=receipt(paths["complete_genuine_execution"],"43702688640",C_SOURCE,C_MANIFEST,gate)
        D=receipt(paths["directed_source_execution"],"43703879926",D_SOURCE,D_MANIFEST,gate)
        L=receipt(paths["first_local_execution"],"43709396175",L_SOURCE,L_MANIFEST,gate)
        doc["original_successful_small_receipts_read"]=6
        sd=S["complete_domain_conclusion"];sa=S["complete_amplitude_conclusion"]
        sf=S["complete_forcing_conclusion"];ds=D["complete_source_conclusion"]
        gate("the genuine correction, full complex squares, fixed root and complete negative source cover are unchanged",
            sd["exact_original_physical_piece_interval"]==list(map(str,PIECE))
            and sd["exact_original_true_root_interval"]==list(map(str,ROOTS))
            and sd["true_physical_root_piece_radius"]==str(H)
            and sd["same_potential_T_segment_proved"] and sd["actual_inverseimage_and_both_regular_paths_proved"]
            and S["scope"]["original_root_piece_2549_only"] and S["scope"]["full_complex_delta_square"]
            and S["scope"]["full_z_square_all_abs_j_ge97"] and S["scope"]["both_carrier_signs"]
            and Q(sf["exact_new_old_rho_radius"])==RF and Q(sf["exact_new_old_angle_strip"])==SF
            and sa["canonical_radius"]=="1/2000" and sa["canonical_strip"]=="3/512"
            and sa["exact_regular_root_normalization_retained"]
            and S["original_accepted_target_FFT_intrinsic_fold_or_transport_recomputed"]==0
            and S["original_signed_Taylor_coefficients_recomputed"]==0
            and W["scope"]["same_T_actual_composition_not_same_old_r_substitution"]
            and W["scope"]["independent_physical_even_mean_equation_retained"]
            and W["scope"]["all_actual_physical_and_reference_seam_jumps_retained"]
            and W["exact_branch_identity"]["same_complex_delta_without_conjugation"]
            and W["exact_branch_identity"]["both_original_reference_columns_and_all_output_modes_retained"]
            and len(W["gates"])==9 and len(S["gates"])==26 and len(G["gates"])==16
            and len(C["gates"])==17 and len(D["gates"])==12 and len(L["gates"])==13
            and ds["exact_negative_physical_cover"]==[str(PIECE[0]),str(ROOTS[1])]
            and ds["actual_dr_measure"] and ds["one_sided_uncertain_root_band_retained"]
            and ds["both_density_windows_retained"] and ds["old_nine_word_and_five_physical_mean_counts"]==[9,5]
            and L["old_numerical_enclosures_recomputed"]==0)
        moduli,domain,amplitude_temp=complete_amplitude_product(fold,majorants,S,gate)
        doc["new_complete_amplitude_product_budgets"]=1;doc["complete_domain_conclusion"]=domain
        vals,oldvals,conclusion,tail_temp=recover_and_replace_tails(W,S,moduli,gate)
        doc.update(new_positive_Taylor_tail_lower_comparisons=6,new_positive_finite_budget_recoveries=6,
            new_complete_infinite_Taylor_tail_bounds=6,new_complete_wrr_derivative_bounds=6,
            complete_wrr_derivative_conclusion=conclusion)
        coeff=read_positive_coefficients(C,gate);doc["original_positive_linear_coefficients_read"]=18
        value,local_conclusion,rest_temp=recover_complete_rest(C,G,coeff,oldvals,vals,gate)
        doc["new_complete_rest_budget_recoveries"]=1;doc["new_fixed_positive_operator_comparisons"]=1
        doc["complete_rest_and_local_conclusion"]=local_conclusion
        result,comparison=compare_and_combine(C,D,L,value,gate)
        doc.update(new_complete_uniform_factors=1,new_complete_scalar_recombinations=3,
            original_complete_source_terms_read=31,
            complete_comparison_conclusion=comparison,complete_source_conclusion=result)
        base=L["complete_source_conclusion"]
        gate("only local_raw_1 changes and every other accepted first-row and physical-mean ball remains verbatim",
            len(result["complete_first_source_term_L2_upper"])==21
            and len(result["complete_independent_mean_term_L2_upper"])==10
            and all(v==result["complete_first_source_term_L2_upper"][k]
                for k,v in base["complete_first_source_term_L2_upper"].items() if k!="local_raw_1")
            and result["complete_independent_mean_term_L2_upper"]==base["complete_independent_mean_term_L2_upper"]
            and result["mean_L2_upper"]==base["mean_L2_upper"]
            and result["nonlocal_total_L2_upper"]==base["nonlocal_total_L2_upper"]
            and up(comparison["complete_uniform_comparison_factor"])<=1
            and rb(comparison["complete_uniform_comparison_factor"]).lower()>=0)
        gate("the complete source conclusions are finite on the identical true dr measure and outer J window",
            all(bound(result[k],k).is_finite() for k in
                ("local_L2_upper","nonlocal_total_L2_upper","first_L2_upper","mean_L2_upper","combined_L2_upper"))
            and result["actual_dr_measure"] and result["one_sided_uncertain_root_band_retained"]
            and result["outer_J_window"]==base["outer_J_window"])
        doc["scope"]=dict(D["scope"])
        doc["scope"].update(new_complete_amplitude_product_gates_actually_verified=True,
            positive_old_tail_addend_lower_not_error_lower=True,
            finite_Taylor_budget_recovered_without_coefficient_or_norm_recomputation=True,
            full_n_ge13_radial_and_two_signed_Fourier_tails_paid=True,
            full_zero_frequency_in_amplitude_norm_retained=True,
            complete_original_local_rest_retained=True,
            same_complete_positive_addend_in_both_old_local_minimum_branches=True,
            accepted_regular_transport_first_local_result_retained=True,
            original_18_positive_coefficients_recomputed=False,
            original_96_directed_comparisons_recomputed=False,
            original_source_rows_and_actual_radial_integrals_recomputed=False,
            physical_to_wave_readout_paid=False,full_negative_BVP_inverse_paid=False,
            positive_growing_column_operator_paid=False,cutoff97_strong_return_contraction_paid=False)
        temporary.update(new_amplitude_product_internal=amplitude_temp,
            six_positive_tail_comparisons=tail_temp,positive_complete_local_rest_comparison=rest_temp,
            accepted_eighteen_coefficients_payload_sha256=payload_sha(C["complete_positive_linear_operator_conclusion"]))
        doc["full_physical_negative_volume_source_paid"]=True
        doc.update(complete=True,proved=True,actual_returncode=0)
    except BaseException as error:
        doc["failure"]=dict(type=type(error).__name__,message=str(error))
    finally:
        doc["actual_mathematical_wall_seconds"]=time.monotonic()-started
        temporary.update(kind=KIND,source_sha256=source,input_manifest_sha256=a.manifest_sha,complete_conclusions=doc)
        native=a.out_dir/"temporary-positive-budget-first-local-Taylor-tail.json.gz"
        save(native,temporary,True)
        doc["temporary_native_sha256"]=sha(native);doc["temporary_native_bytes"]=native.stat().st_size
        doc["temporary_native_is_not_published"]=True;actual=doc["actual_returncode"]
        try:
            text=render(doc)
            data=(json.dumps(doc,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
            if len(data)>60000 or len(text.encode())>60000:raise ValueError("small final conclusion exceeded60000 bytes")
            save(a.out_dir/"process.json",doc);(a.out_dir/"conclusion.md").write_text(text)
        except BaseException as error:
            small={k:v for k,v in doc.items() if k not in
                ("complete_domain_conclusion","complete_wrr_derivative_conclusion",
                 "complete_rest_and_local_conclusion","complete_comparison_conclusion","complete_source_conclusion")}
            small["actual_scientific_returncode"]=actual
            small["formatting_failure"]=dict(type=type(error).__name__,message=str(error))
            small.update(complete=False,proved=False,actual_returncode=1)
            save(a.out_dir/"process.json",small)
            (a.out_dir/"conclusion.md").write_text("# Actual first-local Taylor-tail formatting failure\n\n"
                "The original scientific child code was "+str(actual)+". Formatting is separate from mathematics.\n"
                "Temporary native SHA256: "+doc["temporary_native_sha256"]+"\n")
            actual=1
        print(json.dumps(dict(complete=doc["complete"],actual_returncode=actual,
            new_complete_Taylor_tail_bounds=doc["new_complete_infinite_Taylor_tail_bounds"],
            old_numerical_enclosures_recomputed=0,old_radial_integrals_recomputed=0,
            reproducible_data_published=False)),flush=True)
    return actual
if __name__=="__main__":raise SystemExit(main())
