#!/usr/bin/env python3
"""Complete direct genuine first local source from accepted mixed Taylor budgets.

Only ten new mixed-derivative restrictions, two fourth-angle conversions and
one complete physical local numerator are computed. All earlier successful
mathematical producers, profiles, calibrations and source integrals are read.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,math,os,platform,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy,scipy
from flint import arb,ctx

PUBLIC="Rogerhu12/math-research-public"
TOPIC="topics/visible-flex-exact-nearby/"
KIND="actual_direct_genuine_first_local_mixed_jets_v1"
CONTRACT="7a17ff8830d94d96a4c435c7965befc4469da0d623182973a5f1eadafd1eaa2f"
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
SIGMAP=Q(1,512)
RECEIPTS={
 "Taylor_execution":("43694458725","a0f12f84d55c4735507e71e40d35cd343777d00dad4b5ec5c2e73804230198be","11e993bae75adf3a667ba7f7d8c28f9fb38f3fde8d12e34df938c82baef2ea65","777e681b85beb3317853d05d1c39a35703133a7cd49c81286571d21a89fa5dd1",9),
 "refined_local_execution":("43711480764","e0541949f521e0852bb4a8b204b51281f7d83e0ed2a7a1afbb259ca73362e92a","5e2618c446288cd8d84fcbf4bb7955f56f7a1041f823e05213d043d20b5aeaaf","20422f41645c2a4544bb8a0d79eddf771b45ff0386cc81b3ee97a32849586ef2",19),
 "positive_execution":("43702688640","b0648a3bc244e6671176ac096c759b3e70e57d8c04b75bd4dd74442bfcaf95c0","8465759dfe9101bb7e20275cec1a5b98e23efb4dbe643e492fb8189250b005b9","bca0f97d7c610f8f2572e61d1e1442a8b9c256a4c5429253682b6d803e3a21c3",17),
 "directed_execution":("43703879926","1aa46093bba5150d636cc7c6ef4f5b080447fc2c75d7438b2e52ae5fa6b5d0af","5ce9aceb3be46e795696c09028f39091fdc9a4f969dba0e0b317408974083e9b","2c5cba2e7351267e090d0ca6c06cfecbb21309c039a7844937ee64026254f1d0",12),
 "potential_execution":("43685624307","042713687b7d2d561ba25678a76ae9dbd95e042ec1d57bf4a0caa89310063fe7","44555290b424807278c933aaa5cc26c8a8e198ef1ff02ebdc7728c4ad6810437","d4c48d613cad95a3ad67ccb965acc2e76dc4e7786634a6234850667607ea08e9",16),
 "AJ_execution":("43718112378","32c45b335639a48b0d32541d03924246023e5e3f19deec1bcd8cf0549e955f03","871240a7a97011d837025aad7f9ca1707d69c17b6dec3c1f510f6415c278b74d","58462f96a486dede07873c4fc6aade100539f9f28ef49b49567a4acf7c2e8706",29),
 "RV_execution":("43719681982","d59893af66b8829d924d75686fb0ecd6e6d25f9b72b70a0fac6564c4e96fdf60","4718b4b818ec5d72537aa3a93e5825747a586ece87a086c7578ec6ec4c3b9ded","0781239c0753785d2b196b77cc90c0eb343d52cc73226d84d7f8f6bb23136473",27),
 "baseline_execution":("43720766795","7d28ab5f16bfec72faf898118781a5df0af9bc610e80d11bc9d67b8e0527e594","cbb0f2acedd715220fc90b43bacd3dd571092b7dacd2da0cc4c554160fffe833","48ca7d65c1abd9575c7be6e4e8ae4594cb6f4e1cf3d415cf119e2f2de3ebe425",27)
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
def add(*args,k=2):
    return [up(sum((a[q] for a in args),arb(0))) for q in range(k+1)]
def scale(a,s,k=2):return [up(ex(s)*a[q]) for q in range(k+1)]
def mul(a,b,k=2):
    return [up(sum((math.comb(q,j)*a[j]*b[q-j] for j in range(q+1)),arb(0))) for q in range(k+1)]
def product(*args,k=2):
    out=[arb(1)]+[arb(0)]*k
    for a in args:out=mul(out,a,k)
    return out
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

def fourier_tail_number(width,q):
    if not Q(width)>0 or q not in (0,1,2,3):raise ValueError("complete angular tail order")
    v=(-4*ex(width)).exp();d=1-v;gap(d,"complete angular tail")
    if q==0:return (1+v)/d
    if q==1:return 8*v/d**2
    if q==2:return 32*v*(1+v)/d**3
    return 128*v*(1+4*v+v*v)/d**4


def parameters():
    return dict(arithmetic_bits=320,physical_piece=2549,cutoff_abs_j=97,physical_frequency="4j",
        exact_negative_cover=[str(PIECE[0]),str(ROOTS[1])],exact_root_interval=list(map(str,ROOTS)),
        exact_original_whole_cover=str(H),exact_negative_rho_cover=str(ROOTS[1]-PIECE[0]),
        original_fold_radius=str(RG),original_fold_strip=str(SG),
        original_Taylor_radius=str(R0),original_added_Taylor_radius=str(RA),original_Taylor_strip=str(SIGMA0),
        accepted_amplitude_radius=str(RS),accepted_amplitude_strip=str(SS),
        fourth_angle_positive_width=str(SIGMAP),complete_leading_E_strip=str(SP),
        original_physical_coefficient_strip=str(CW),
        complex_delta_square_halfwidth="1/100000000",complex_z_square_halfwidth="1/9409",
        fixed_intrinsic_parameter="eta_0",first_omitted_Taylor_degree=13,
        new_mixed_bounds_per_field=["p2q0","p2q1","p2q2","p1q3","p0q3_width1/512"],
        accepted_low_derivatives_read=14,new_mixed_derivatives=10,new_fourth_angle_conversions=2,
        new_changed_terms=["local_raw_1"],exact_input_weight="1",full_mean_and_both_input_signs=True,
        accepted_baseline_run="43720766795/1",accepted_b1_run="43719681982/1",
        common_column_envelope="abs(rho)^(-1/4)",old_radial_integrals_recomputed=0)

def radial_tail_number(M,R,h,p):
    if p not in (0,1,2) or not 0<h<R:
        raise ValueError("the complete mixed derivative tail left its paid product")
    t=ex(h/R);d=1-t;gap(d,"complete radial tail")
    if p==0:v=t**13/d
    elif p==1:v=t**12*(13/d+t/(d*d))
    else:v=t**11*(156/d+26*t/(d*d)+2*t*t/(d*d*d))
    return rb(M)*ex(R**(-p))*v

def complete_mixed_jets(W,B,RV,DG,h,gate):
    bywidth={}
    for width in (Q(0),SIGMAP):
        cases=[v for v in W["cases"] if Q(v["exact_output_old_phi_width"])==width]
        if len(cases)!=1:raise ValueError("a required original Taylor width is not unique")
        case=cases[0];fields={v["field"]:v for v in case["fields"]}
        bywidth[width]={name:{row["radial_derivative_order"]:row["complete_joint_Wiener_upper"]
            for row in fields[name]["complete_mixed_derivative_rows"]} for name in ("a1","b1")}
        if not (case["complete"] and case["proved"] and Q(case["exact_whole_piece_cover_radius"])==H
            and all(fields[name]["finite_signed_addition_precedes_modulus_and_sum"]
                and fields[name]["joint_sum_of_radial_coefficient_suprema"]
                and fields[name]["full_output_zero_mode_retained"]
                and fields[name]["amplitude_mean_is_not_independent_physical_even_mean"]
                and Q(fields[name]["exact_output_old_phi_width"])==width
                and Q(fields[name]["old_tail_radius"])==R0
                and Q(fields[name]["added_term_tail_radius"])==RA
                and Q(fields[name]["common_outer_angle_strip"])==SIGMA0
                and all(r["angular_derivative_orders"]==[0,1,2,3]
                    for r in fields[name]["complete_mixed_derivative_rows"])
                for name in ("a1","b1"))):
            raise ValueError("the complete signed Taylor field identity changed")
    tail=W["complete_tail_conclusion"]
    gate("the two accepted Taylor widths retain complete signed genuine fields all radial orders and both old tails",
        tail["first_omitted_Taylor_degree"]==13 and Q(tail["old_radius"])==R0
        and Q(tail["new_added_term_radius"])==RA and Q(tail["outer_old_phi_strip"])==SIGMA0
        and tail["exact_delta_a1_radial_zero_order"]==3 and tail["no_radius_scaling_applied_to_other_terms"]
        and tail["angular_tails_from_joint_double_Cauchy"] and tail["no_uncomputed_finite_coefficient_was_set_to_zero"]
        and W["scope"]["new_reference_first_correction_identified_by_exact_integral"]
        and W["scope"]["same_T_actual_composition_not_same_old_r_substitution"]
        and W["scope"]["old_first_correction_relabelled_as_new"] is False
        and W["exact_branch_identity"]["first_correction_a1_minus"]=="-a1_plus"
        and W["exact_branch_identity"]["first_correction_b1_minus"]=="b1_plus"
        and all(set(rows)=={0,1,2} for fields in bywidth.values() for rows in fields.values()))
    bd=B["complete_domain_conclusion"];rd=RV["complete_negative_Taylor_conclusion"]
    dd=DG["complete_genuine_derivative_conclusion"]
    gate("the successful DG a1 and RV b1 low derivatives are read verbatim on the identical negative product",
        0<h<H<RA<RS<R0<RG and 0<SIGMAP<SS<SIGMA0
        and Q(bd["exact_new_old_rho_radius"])==RS and Q(bd["exact_new_old_phi_strip"])==SS
        and Q(bd["exact_full_physical_cover"])==H and bd["all_sT_paths_in_same_paid_domain"]
        and bd["root_normalization_and_all_means_unchanged"]
        and Q(rd["exact_new_negative_rho_cover"])==Q(dd["exact_negative_rho_cover"])==h
        and Q(rd["old_complete_whole_piece_radius"])==Q(dd["exact_original_whole_cover"])==H
        and dd["exact_new_a1_bound_count"]==dd["accepted_b1_bound_count"]==7
        and dd["full_zero_mode_and_both_carriers_retained"]
        and dd["accepted_RV_Taylor_conclusion_sha256"]==payload_sha(rd)
        and dd["accepted_b1_value_derivative_upper"]==rd["retained_complete_b1_value_derivative_upper"]
        and dd["accepted_b1_radial_derivative_upper"]==rd["retained_complete_b1_radial_derivative_upper"]
        and len(dd["complete_a1_value_derivative_upper"])==len(dd["accepted_b1_value_derivative_upper"])==4
        and len(dd["complete_a1_radial_derivative_upper"])==len(dd["accepted_b1_radial_derivative_upper"])==3)
    v={0:[[bound(x) for x in dd["complete_a1_value_derivative_upper"]],
            [bound(x) for x in dd["accepted_b1_value_derivative_upper"]]],
        1:[[bound(x) for x in dd["complete_a1_radial_derivative_upper"]],
            [bound(x) for x in dd["accepted_b1_radial_derivative_upper"]]],
        2:[[],[]]}
    details=[];wide={}
    for i,name in enumerate(("a1","b1")):
        mo=lower(tail["unchanged_original_full_product_modulus"][name],"original positive modulus")
        ma=lower(tail["complete_added_term_full_product_modulus"][name],"added positive modulus")
        M=bound(bd["complete_new_amplitude_modulus"][name],"accepted genuine amplitude product")
        for p,q,width in ((2,0,Q(0)),(2,1,Q(0)),(2,2,Q(0)),(1,3,Q(0)),(0,3,SIGMAP)):
            prior=bywidth[width][name][p][q];total=bound(prior,"saved complete mixed derivative")
            same=(radial_tail_number(mo,R0,H,p)+radial_tail_number(ma,RA,H,p))*fourier_tail_number(SIGMA0-width,q)
            lo=lower(same,"identical old numerical tail addend")
            finite=(total-lo).upper()
            if not finite.is_finite() or finite.lower()<0:
                raise ValueError("same positive-tail recovery is negative or nonfinite; no clipping")
            fresh=up(radial_tail_number(M,RS,h,p)*fourier_tail_number(SS-width,q))
            complete=min(total,up(finite+fresh)).upper()
            if p==0:wide[name]=complete;v[0][i].append(up(complete/ex(SIGMAP)))
            else:v[p][i].append(complete)
            details.append(dict(field=name,p=p,q=q,output_angle_width=str(width),
                original_complete_total=prior,identical_old_positive_tail_lower=rec(lo),
                retained_unscaled_finite_budget_upper=rec(finite),new_complete_tail_upper=rec(fresh),
                complete_new_mixed_derivative_upper=rec(complete)))
    gate("exactly ten new mixed restrictions and two positive-width fourth-angle conversions retain all infinite tails",
        len(details)==10 and len(wide)==2 and all(len(x)==5 for x in v[0])
        and all(len(x)==4 for x in v[1]) and all(len(x)==3 for x in v[2])
        and all(x.is_finite() and x.lower()>=0 for pair in v.values() for row in pair for x in row))
    conclusion=dict(exact_negative_rho_cover=str(h),exact_original_whole_cover=str(H),
        accepted_low_derivatives_read=14,new_complete_mixed_derivatives=10,
        new_fourth_angle_conversions=2,exact_fourth_angle_width=str(SIGMAP),
        exact_genuine_identity="w1V=free_w1+(T*b0,a0)*B(T)",
        complete_new_second_radial_derivative_upper=encode(v[2]),
        complete_new_first_radial_third_angle_upper=encode([row[3] for row in v[1]]),
        complete_new_positive_width_third_angle_upper=encode([wide["a1"],wide["b1"]]),
        complete_new_fourth_angle_upper=encode([row[4] for row in v[0]]),
        accepted_DG_derivative_conclusion_sha256=payload_sha(dd),
        accepted_RV_derivative_conclusion_sha256=payload_sha(rd),
        finite_signed_sums_not_rescaled=True,full_zero_modes_and_both_carriers_retained=True,
        lower_is_for_same_positive_algorithm_parameter_not_function=True,
        no_original_signed_coefficient_norm_transport_or_lower_derivative_recomputed=True)
    return v,conclusion,details

def direct_coefficient_closure(f,c,P,AJ,RV,DG,h,gate):
    rv=RV["complete_domain_conclusion"];ad=AJ["complete_domain_conclusion"]
    aj=AJ["complete_AJ_angular_derivative_conclusion"];dg=DG["complete_direct_physical_transport_conclusion"]
    cases=[v for v in P["cases"] if Q(v["exact_complex_radial_radius"])==R0]
    if len(cases)!=1:raise ValueError("the complete common potential case is not unique")
    pc=cases[0]
    Th=bound(rv["new_complete_negative_T_image_upper"],"accepted full SG negative image")
    image=gap(pc["reference_image"]["complete_image_disk_radius_lower"],"same full potential image")
    gate("the accepted RV leading X modulus and AJ holomorphic Xi have their complete common physical domains",
        Q(rv["exact_negative_rho_cover"])==h and Q(rv["exact_original_whole_cover"])==H
        and rv["original_full_mean_gauge_retained"] and rv["original_potential_and_fold_producers_called"] is False
        and gap(rv["complete_leading_T_margin_lower"],"original leading T margin")>0
        and gap(rv["complete_leading_X_margin_lower"],"original leading X margin")>0
        and len(rv["complete_leading_X_derivative_moduli"])==2
        and Q(ad["exact_original_fold_radius"])==RG and Q(ad["exact_original_fold_strip"])==SG
        and Q(ad["exact_physical_phi_strip"])==SP and Q(ad["exact_full_physical_cover"])==H
        and ad["physical_T_image_definition_read_from_frozen_producer"] and ad["full_mean_and_radial_G_scalar_retained"]
        and aj["accepted_order_zero_domain_read_verbatim"]==ad
        and aj["exact_mu_identity"]=="Q^2*(x^2+T*y^2)"
        and aj["exact_radial_mean_identity"]=="T0=t(r)+5*d_phi"
        and pc["complete"] and pc["proved"] and pc["failure"] is None
        and pc["whole_complex_bilinear_family"] and pc["both_carrier_signs_retained"]
        and Q(pc["exact_complex_delta_square_halfwidth"])==Q(1,10**8)
        and Q(pc["exact_complex_z_square_halfwidth"])==Q(1,9409)
        and pc["fixed_intrinsic_parameter"]=="eta_0" and image>Th)
    MV=bound(pc["complete_modulus_upper"]["V"]);MVT=bound(pc["complete_modulus_upper"]["V_T"])
    mm=bound(f["M"]);B2=bound(f["B2"]);QQ=bound(f["Q"])
    muM=up(QQ*QQ*(bound(f["E"])**2+bound(f["TM"])*bound(f["BT"])**2))
    ax=bound(rv["complete_leading_X_derivative_moduli"][0],"accepted RV sP leading a0_X")
    xi=bound(ad["complete_Xi_holomorphic_upper"],"accepted holomorphic Xi, not real order-zero jet")
    Em=up(muM*(MV*(2*ax+xi*mm+B2*Th)+MVT*B2*Th*Th))
    Ejet=cauchy(Em,SP,2)
    D=[bound(x) for x in c["D"]];Dr=[bound(x) for x in c["Dr"]]
    if len(D)<4 or len(Dr)<3:raise ValueError("the original full drift jets are incomplete")
    T0=[bound(c["T0"]),up(5*D[2]),up(5*D[3])]
    V0=cauchy(c["V0"],CW,2);theta=cauchy(c["vartheta"],CW,2)
    muV=cauchy(up(muM*MV),SG,2)
    k=up(bound(c["ep"])**2*min(bound(c["K"]),up(ex(h)*bound(c["kp"]))))
    QT=[bound(x) for x in dg["complete_principal_QT_derivative_upper"][:3]]
    Qjet=[bound(x) for x in dg["complete_principal_Q_derivative_upper"][:3]]
    gate("the new complete physical multiplier closure reads original drift and DG principal jets and keeps the entire E first row",
        Q(dg["exact_negative_rho_cover"])==h and dg["full_amplitude_means_and_signed_carriers_retained"]
        and dg["exact_radial_derivative"]=="partial_r=-partial_old_rho"
        and len(QT)==len(Qjet)==3 and len(Ejet)==3 and muM.is_finite() and muM.lower()>0
        and all(v.is_finite() and v.lower()>=0 for arr in (D,Dr,T0,V0,theta,muV,Ejet,QT,Qjet) for v in arr)
        and k.is_finite() and k.lower()>=0)
    out=dict(D=D,Dr=Dr,T0=T0,V0=V0,theta=theta,muV=muV,eta2K=k,QT=QT,Q=Qjet,E=Ejet)
    conclusion=dict(exact_negative_rho_cover=str(h),exact_complete_mu_strip=str(SG),
        exact_complete_E_strip=str(SP),complete_mu_holomorphic_upper=rec(muM),
        complete_muV_holomorphic_upper=rec(up(muM*MV)),complete_E_holomorphic_upper=rec(Em),
        complete_E_first_component_angular_upper=encode(Ejet),complete_E_second_component_exact_zero=True,
        accepted_RV_a0X_modulus=rv["complete_leading_X_derivative_moduli"][0],
        accepted_AJ_holomorphic_Xi_modulus=ad["complete_Xi_holomorphic_upper"],
        accepted_negative_T_image=rv["new_complete_negative_T_image_upper"],
        accepted_full_potential_image_lower=pc["reference_image"]["complete_image_disk_radius_lower"],
        complete_restricted_eta_squared_K_modulus=rec(k),
        accepted_DG_principal_QT_jet=dg["complete_principal_QT_derivative_upper"][:3],
        accepted_DG_principal_Q_jet=dg["complete_principal_Q_derivative_upper"][:3],
        full_radial_gauge_and_all_means_retained=True,
        no_old_fold_negative_geometry_AJ_or_potential_closure_called=True)
    return out,conclusion

def complete_direct_local_vector(w,C):
    D=C["D"];Dr=C["Dr"];T0=C["T0"]
    phiC=add(mul(D,D[1:]),Dr,mul(T0,D))
    phi2C=add(mul(D,D),[C["eta2K"],arb(0),arb(0)])
    valueC=add(C["V0"],C["muV"])
    groups={key:[[],[]] for key in ("genuine_wrr","mixed_drift",
        "first_angle_coefficients","second_angle_coefficients","radial_T0",
        "complete_zeroth_order","complete_offdiagonal_reaction","leading_E_row")}
    for i in range(2):
        groups["genuine_wrr"][i]=list(w[2][i])
        groups["mixed_drift"][i]=scale(mul(D,w[1][i][1:]),2)
        groups["first_angle_coefficients"][i]=mul(phiC,w[0][i][1:])
        groups["second_angle_coefficients"][i]=mul(phi2C,w[0][i][2:])
        groups["radial_T0"][i]=mul(T0,w[1][i])
        groups["complete_zeroth_order"][i]=mul(valueC,w[0][i])
        groups["complete_offdiagonal_reaction"][i]=product(C["theta"],C["QT"] if i==0 else C["Q"],w[0][1-i])
        groups["leading_E_row"][i]=list(C["E"]) if i==0 else [arb(0)]*3
    full=[add(*(v[i] for v in groups.values())) for i in range(2)]
    return full,groups

def compare_and_combine(C,D,RV,DG,value,gate):
    local=C["complete_local_vector_conclusion"];original=D["complete_source_conclusion"]
    base=DG["complete_source_conclusion"];rv=RV["complete_source_conclusion"]
    stable=("actual_dr_measure","exact_negative_physical_cover","one_sided_uncertain_root_band_retained",
        "both_density_windows_retained","outer_J_window","input_window","first_output_window",
        "independent_even_mean_window","total_squared_envelope_radial_weight_upper","original_temporary_row_payload_sha256")
    gate("the current DG ledger keeps RV local1 and the identical original positive local constant six intersections and true measure",
        D["accepted_complete_local_vector_conclusion"]==local
        and len(base["complete_first_source_term_L2_upper"])==21
        and len(base["complete_independent_mean_term_L2_upper"])==10
        and all(base[k]==rv[k]==original[k] for k in stable)
        and all(base["complete_first_source_term_L2_upper"]["local_raw_"+str(i)]==
            rv["complete_first_source_term_L2_upper"]["local_raw_"+str(i)] for i in (1,2,3))
        and base["exact_negative_physical_cover"]==[str(PIECE[0]),str(ROOTS[1])]
        and local["raw_numerator_not_divided_by_mu"] and local["exact_input_weights"]==["1","1/388","1/150544"])
    beta=gap(local["raw_complete_operator_coefficients"][0],"same original positive local1 numerical constant")
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
    for key in ("complete_local_budget_read_unchanged","only_two_complete_local_vectors_replaced",
        "all_other_twenty_nine_term_balls_read_verbatim","current_genuine_amplitude_bounds_and_all_mean_factors_unchanged"):
        result.pop(key,None)
    result.update(only_complete_local_raw1_replaced=True,all_other_thirty_term_balls_read_verbatim=True,
        old_source_row_or_radial_integral_recomputed=False,
        strictly_smaller_complete_aggregates=dict(local=a,first=b,combined=c))
    comparison=dict(source_term="local_raw_1",new_complete_raw_operator_upper=rec(value),
        same_original_positive_budget_lower=rec(beta),complete_uniform_comparison_factor=rec(ratio),
        complete_original_term_L2_upper=oldterm,latest_DG_complete_term_L2_upper=prior,
        retained_complete_term_L2_upper=selected,strict_complete_term_improvement=better,
        comparison_denominator_is_not_function_lower=True)
    gate("only one complete local term changes and the other thirty source and mean balls remain byte identical",
        all(v==base["complete_first_source_term_L2_upper"][k] for k,v in terms.items() if k!="local_raw_1")
        and result["complete_independent_mean_term_L2_upper"]==base["complete_independent_mean_term_L2_upper"]
        and result["nonlocal_total_L2_upper"]==base["nonlocal_total_L2_upper"]
        and result["mean_L2_upper"]==base["mean_L2_upper"] and all(result[k]==base[k] for k in stable))
    return result,comparison

def render(doc):
    lines=["# Direct genuine first local residual: actual mixed-jet comparison","",
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
        j=doc["complete_mixed_derivative_conclusion"];c=doc["complete_coefficient_conclusion"]
        op=doc["complete_local_operator_conclusion"];cp=doc["complete_comparison_conclusion"]
        lines.extend(["","## New complete mixed derivatives","",
            "All values include the full degree13 tail and both Fourier signs. The fourteen successful DG/RV low derivatives are read only.",
            "","| Field | Ordinary derivative | Complete upper |","| --- | --- | --- |"])
        for i,name in enumerate(("a1V","b1V")):
            for q,v in enumerate(j["complete_new_second_radial_derivative_upper"][i]):
                lines.append("| "+name+" | r2 phi"+str(q)+" | "+v["ball"]+" |")
            lines.append("| "+name+" | r1 phi3 | "+j["complete_new_first_radial_third_angle_upper"][i]["ball"]+" |")
            lines.append("| "+name+" | phi3 at width1/512 | "+j["complete_new_positive_width_third_angle_upper"][i]["ball"]+" |")
            lines.append("| "+name+" | phi4 at real angle | "+j["complete_new_fourth_angle_upper"][i]["ball"]+" |")
        lines.extend(["","## Complete physical local operator","",
            "- New complete raw1 operator: "+op["complete_first_local_raw_operator_upper"]["ball"],
            "- The common column envelope remains abs(rho)^(-1/4).",
            "- The numerator has not been divided by mu; raw1 input weight remains1.",
            "- Complete holomorphic E first row: "+c["complete_E_holomorphic_upper"]["ball"],
            "- E second component is exactly zero; all physical mean and rank equations remain in the retained full ledger.",
            "","| Complete summand diagnostic | Upper |","| --- | --- |"])
        for k,v in op["complete_summand_operator_upper"].items():lines.append("| "+k+" | "+v["ball"]+" |")
        lines.extend(["","## Same-term positive comparison","",
            "- New complete factor against the original numerical budget: "+cp["complete_uniform_comparison_factor"]["ball"],
            "- Latest DG local1: "+cp["latest_DG_complete_term_L2_upper"]["ball"],
            "- Retained complete local1: "+cp["retained_complete_term_L2_upper"]["ball"],
            "- Strict improvement: "+str(cp["strict_complete_term_improvement"]),
            "- The denominator is an original positive budget number, not a function lower bound.",
            "","## Complete retained negative source",""])
        result=doc["complete_source_conclusion"]
        for k in ("local_L2_upper","nonlocal_total_L2_upper","first_L2_upper","mean_L2_upper","combined_L2_upper"):
            lines.append("- "+k+": "+result[k]["ball"])
        lines.extend(["","| Full first source term | Complete L2 upper |","| --- | --- |"])
        for k,v in sorted(result["complete_first_source_term_L2_upper"].items()):lines.append("| "+k+" | "+v["ball"]+" |")
        lines.extend(["","| Independent physical mean term | Complete L2 upper |","| --- | --- |"])
        for k,v in sorted(result["complete_independent_mean_term_L2_upper"].items()):lines.append("| "+k+" | "+v["ball"]+" |")
    lines.extend(["","## Scope","",
        "Only the original negative part of physical piece2549 is compared. Both genuine columns, both input signs, the two source windows, all means, true dr, six original intersections and uncertain-root charge remain. Only local_raw_1 may change; the other30 terms are copied.",
        "The original potential, fold, signed Taylor coefficients, transport, column profiles, positive calibration, source rows and radial integrals are not recomputed.",
        "Summand diagnostics are bounds, not lower bounds for true error. This result does not prove a high BVP inverse, positive growing-column estimate or strong return contraction.",
        "All native and intermediate arrays are temporary. Only this small conclusion and actual execution metadata are published.",""])
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
        accepted_complete_low_derivative_bounds_read=0,accepted_DG_principal_derivatives_read=0,
        new_same_positive_tail_lower_recoveries=0,new_complete_mixed_derivative_bounds=0,
        new_fourth_angle_conversions=0,new_complete_physical_coefficient_closures=0,
        new_complete_first_local_vectors=0,new_complete_local_operator_bounds=0,
        new_complete_summand_diagnostics=0,new_complete_uniform_term_comparisons=0,
        new_complete_scalar_recombinations=0,old_numerical_enclosures_recomputed=0,
        old_target_FFT_intrinsic_repair_fold_or_Taylor_recomputed=0,
        old_signed_coefficients_Fourier_norms_potential_or_transport_recomputed=0,
        old_DG_a1_RV_b1_or_principal_jets_recomputed=0,
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
            original_Taylor_algorithm=RECEIPTS["Taylor_execution"][1],
            original_positive_algorithm=RECEIPTS["positive_execution"][1],
            original_RV_algorithm=RECEIPTS["RV_execution"][1],
            original_DG_algorithm=RECEIPTS["baseline_execution"][1],
            original_RV_manifest=RECEIPTS["RV_execution"][2],
            original_DG_manifest=RECEIPTS["baseline_execution"][2])
        gate("all accepted algorithms manifests executions and the single natural fold stage keep their immutable hashes",
            all(sha(paths[k])==v for k,v in expected.items())
            and all(sha(paths[k])==identity[3] for k,identity in RECEIPTS.items()))
        data=read_original_fold(paths,gate);f=data["fold"];c=data["coefficients"]
        doc["original_complete_fold_stages_read"]=1
        receipts={k:accepted(paths[k],identity,gate) for k,identity in RECEIPTS.items()}
        doc["original_successful_small_receipts_read"]=len(receipts)
        W=receipts["Taylor_execution"];B=receipts["refined_local_execution"]
        C=receipts["positive_execution"];D=receipts["directed_execution"]
        P=receipts["potential_execution"];AJ=receipts["AJ_execution"]
        RV=receipts["RV_execution"];DG=receipts["baseline_execution"]
        rm=read(paths["original_RV_manifest"]);dm=read(paths["original_DG_manifest"])
        gate("all successful objects preserve the same genuine correction fixed intrinsic parameter and independent mean scope",
            rm["scientific_source_sha256"]==RECEIPTS["RV_execution"][1]
            and dm["scientific_source_sha256"]==RECEIPTS["baseline_execution"][1]
            and W["scope"]["same_original_rho_orientation_and_input_frequency"]
            and C["scope"]["original_fixed_intrinsic_parameter"]=="eta_0"
            and C["scope"]["physical_J_only_on_its_proved_reflected_parity_domain"]
            and DG["scope"]["density_one_is_genuine_w1V_not_old_free_w1"]
            and DG["scope"]["full_amplitude_means_and_independent_physical_even_mean_retained"]
            and DG["scope"]["all_three_local_terms_read_verbatim"]
            and RV["full_physical_negative_volume_source_paid"] and DG["full_physical_negative_volume_source_paid"]
            and not RV["full_high_inverse_claimed"] and not DG["full_high_inverse_claimed"])
        ws=paths["original_Taylor_algorithm"].read_text();rs=paths["original_RV_algorithm"].read_text()
        fs=paths["original_fold_algorithm"].read_text();cs=paths["original_positive_algorithm"].read_text()
        gate("the signed genuine coefficient positive-tail recipe full fold modulus and original ordered local operator are frozen",
            'a1=[old["a1"][n]+da[n] for n in range(count)]' in ws
            and 'b1=[old["b1"][n]+db[n] for n in range(count)]' in ws
            and "fulltail=oldtail+newtail" in ws and "tail=fulltail*angular_sum(SIGMA-width,q)" in ws
            and "vals.append(rec(up(finite+tail)))" in ws
            and "M=(G*(E*E+TM*BT*BT)).upper()" in fs
            and "ax=up(2*(M-1)*Th/(marginT*marginX))" in rs
            and 'Th=up(ex(h/H)*bound(accepted["accepted_complete_physical_T_image"]))' in rs
            and "return [allv[1],zeros(2)]" in cs
            and "L1=vadd(w1[2],rest,k=2)" in cs)
        w,jets,details=complete_mixed_jets(W,B,RV,DG,h,gate)
        doc.update(accepted_complete_low_derivative_bounds_read=14,new_same_positive_tail_lower_recoveries=10,
            new_complete_mixed_derivative_bounds=10,new_fourth_angle_conversions=2,
            complete_mixed_derivative_conclusion=jets)
        coeff,closure=direct_coefficient_closure(f,c,P,AJ,RV,DG,h,gate)
        doc.update(accepted_DG_principal_derivatives_read=6,new_complete_physical_coefficient_closures=1,
            complete_coefficient_conclusion=closure)
        vector,groups=complete_direct_local_vector(w,coeff)
        gate("the new first local numerator contains all eight complete physical summands with the leading E only in its first component",
            len(groups)==8 and all(len(row)==3 for row in vector)
            and all(len(row)==3 for pair in groups.values() for row in pair)
            and all(v.is_finite() and v.lower()>=0 for row in vector for v in row)
            and all(v==0 for v in groups["leading_E_row"][1]))
        positive=read_positive_coefficients(C,gate);value=positive_operator(positive,vector)
        groupvalues={k:positive_operator(positive,v) for k,v in groups.items()}
        doc.update(original_positive_linear_coefficients_read=18,new_complete_first_local_vectors=1,
            new_complete_local_operator_bounds=1,new_complete_summand_diagnostics=8,
            complete_local_operator_conclusion=dict(complete_first_local_raw_operator_upper=rec(value),
                exact_input_weight="1",raw_numerator_not_divided_by_mu=True,
                common_column_envelope="abs(rho)^(-1/4)",
                complete_summand_operator_upper=encode(groupvalues),
                original_genuine_profiles_and_positive_calibration_read_only=True,
                genuine_finite_signed_coefficients_not_split=True))
        result,comparison=compare_and_combine(C,D,RV,DG,value,gate)
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
            same_genuine_first_correction_and_root_gauge=True,finite_signed_coefficients_before_modulus=True,
            original_DG_a1_RV_b1_and_DG_principal_jets_read_verbatim=True,
            complete_leading_E_row_retained_before_absolute_bounds=True,
            leading_a0_T_not_inserted_into_E12=True,original_full_radial_mean_gauge_retained=True,
            only_local_raw1_replaced=True,all_other_thirty_term_balls_unchanged=True,
            full_amplitude_mean_and_independent_physical_even_mean_retained=True,
            both_J_windows_true_dr_and_uncertain_root_charge_retained=True,
            physical_J_only_on_its_proved_reflected_parity_domain=True,
            original_physical_seams_reference_jumps_forcing_and_positive_ports_retained=True,
            original_target_intrinsic_fold_Taylor_transport_profile_or_source_producer_called=False,
            intermediate_arrays_published=False,physical_to_wave_readout_changed=False,
            full_negative_BVP_inverse_paid=False,positive_growing_column_operator_paid=False,
            cutoff97_strong_return_contraction_paid=False)
        temporary.update(complete_new_tail_details=details,complete_new_mixed_jets=encode(w),
            complete_new_coefficient_jets=encode(coeff),complete_summand_vectors=encode(groups),
            complete_first_local_vector=encode(vector),
            accepted_positive_coefficients_payload_sha256=payload_sha(C["complete_positive_linear_operator_conclusion"]))
        doc.update(complete=True,proved=True,actual_returncode=0,full_physical_negative_volume_source_paid=True)
    except BaseException as error:
        doc["failure"]=dict(type=type(error).__name__,message=str(error))
    finally:
        doc["actual_mathematical_wall_seconds"]=time.monotonic()-started
        temporary.update(kind=KIND,source_sha256=source,input_manifest_sha256=a.manifest_sha,complete_conclusions=doc)
        native=a.out_dir/"temporary-direct-genuine-first-local-mixed-jets.json.gz"
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
                ("complete_mixed_derivative_conclusion","complete_coefficient_conclusion","complete_local_operator_conclusion",
                 "complete_comparison_conclusion","complete_source_conclusion")}
            small["actual_scientific_returncode"]=actual
            small["formatting_failure"]=dict(type=type(error).__name__,message=str(error))
            small.update(complete=False,proved=False,actual_returncode=2)
            save(a.out_dir/"process.json",small)
            (a.out_dir/"conclusion.md").write_text("# New mixed-jet local consumer: formatter failure\n\n"+json.dumps(small,ensure_ascii=False)+"\n")
            raise SystemExit(2)
    if doc["actual_returncode"]!=0:raise SystemExit(doc["actual_returncode"])

if __name__=="__main__":main()
