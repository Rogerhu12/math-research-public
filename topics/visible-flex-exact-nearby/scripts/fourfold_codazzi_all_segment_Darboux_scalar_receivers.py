#!/usr/bin/env python3
"""New all-segment Darboux error functionals and complete strict-cut scalar receivers.

Every old profile, positive calibration, amplitude derivative and canonical
potential budget is read from a complete immutable successful small receipt.
Only new scalar coefficient products, the new three-phase gap and the exact
all-tau majorant of IN are evaluated. No old scientific module is imported.
This first receiver does not claim the final physical C_Dar or incoming inverse.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,math,os,platform,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy,scipy
from flint import arb,ctx

PUBLIC="Rogerhu12/math-research-public"
TOPIC="topics/visible-flex-exact-nearby/"
KIND="actual_all_segment_Darboux_error_and_strict_cut_scalar_receivers_v1"
CONTRACT="d4ac47aabbaa6869553ec33b87d2234c66e8a76e70c19f3f3d76817ccfb9bd75"
RUNTIME=dict(python="3.12.14",python_flint="0.9.0",numpy="2.3.5",scipy="1.17.0")
ROOTS=(Q(1191984371497,5000000000000),Q(2383968743003,10000000000000))
RCUT=Q(76285779072683,320000000000000)
H=Q(893368603925465506687,21990232555520000000000000)
RG=Q(3,8000);SG=Q(3,128);SB=Q(1,64);N=388;J0=97
BRANCHES=("central","positive_characteristic","negative_characteristic")
COMPONENTS=("a","a_phi","a_phiphi","b","b_phi","b_phiphi")
EXPECTED={
    "potential_execution": [
        "43685624307",
        "042713687b7d2d561ba25678a76ae9dbd95e042ec1d57bf4a0caa89310063fe7",
        "44555290b424807278c933aaa5cc26c8a8e198ef1ff02ebdc7728c4ad6810437",
        "d4c48d613cad95a3ad67ccb965acc2e76dc4e7786634a6234850667607ea08e9",
        16
    ],
    "accepted_RV_execution": [
        "43719681982",
        "d59893af66b8829d924d75686fb0ecd6e6d25f9b72b70a0fac6564c4e96fdf60",
        "4718b4b818ec5d72537aa3a93e5825747a586ece87a086c7578ec6ec4c3b9ded",
        "0781239c0753785d2b196b77cc90c0eb343d52cc73226d84d7f8f6bb23136473",
        27
    ],
    "accepted_SV_execution": [
        "43722805762",
        "44021afbf608638e7e08f584a5574acdc76738c5985d72ca0f2b036c8f7d2dc0",
        "5306e66c5102e358caba5946b3c651dda11fb98a18848f8fe27f779f775d73cf",
        "ba96a4832017144ea3ccd59902e8bcb8f1b0acd1c722edadc44b763dfac6c0d0",
        23
    ],
    "accepted_HP_execution": [
        "43726426053",
        "bacbc58b43d7b5463996377802ff700a6ff1abf9dc23dce835541ef934f6a6e6",
        "12f93b005f06a5df4342e25cf814b8eed39571e36594401d3194a6a08a37e5cd",
        "01d9990041478c1a81a6413909d388038af43395578054fd71be2e83a4f8b036",
        25
    ],
    "accepted_BG_execution": [
        "43726985545",
        "f3f3737931bfa528f57a8f23c0c00043c6027b7ec0d2157ec2a05fb2985d27e4",
        "77fd42dd62ba5007cca008e8c868f61d7ed317176f0290818aae091f4e1c62b1",
        "7736f33c74ccfc84cd8d00108f8035d6cc5d3f16cd9878f885a17481b8d17927",
        24
    ],
    "accepted_DG_execution": [
        "43720766795",
        "7d28ab5f16bfec72faf898118781a5df0af9bc610e80d11bc9d67b8e0527e594",
        "cbb0f2acedd715220fc90b43bacd3dd571092b7dacd2da0cc4c554160fffe833",
        "48ca7d65c1abd9575c7be6e4e8ae4594cb6f4e1cf3d415cf119e2f2de3ebe425",
        27
    ],
    "accepted_RJ_execution": [
        "43728317408",
        "c1ed2857915498a4f301f3ad3bd6caaeea99232b97e0b1e7f87d08e89beb23a8",
        "e0a36c82ed4f2a7aa0ea9bbbcccee8ab3aee06ccbc78ed113a08e9f353eb93d8",
        "042031e1e0baaa53ef062d87918c7ede09eb1f6b4c12bc1d4e4a2ee19ad6a084",
        27
    ],
    "complete_genuine_execution": [
        "43702688640",
        "b0648a3bc244e6671176ac096c759b3e70e57d8c04b75bd4dd74442bfcaf95c0",
        "8465759dfe9101bb7e20275cec1a5b98e23efb4dbe643e492fb8189250b005b9",
        "bca0f97d7c610f8f2572e61d1e1442a8b9c256a4c5429253682b6d803e3a21c3",
        17
    ],
    "Taylor_execution": [
        "43694458725",
        "a0f12f84d55c4735507e71e40d35cd343777d00dad4b5ec5c2e73804230198be",
        "11e993bae75adf3a667ba7f7d8c28f9fb38f3fde8d12e34df938c82baef2ea65",
        "777e681b85beb3317853d05d1c39a35703133a7cd49c81286571d21a89fa5dd1",
        9
    ],
    "accepted_PC_execution": [
        "43740173506",
        "da6864cd790162759d5a78d40a67d0f3b4aa91b60614d947cca1a92371d6940b",
        "13d92e7d2bfb8e3fd57e417676c58d6a649c7f353bcd54fef19af8cc66e123e5",
        "75f780f60446bd2a47fe286e72ca24fad929e3486c12d9ecbea42f42b9b1a817",
        30
    ]
}
PARAMETERS=json.loads("{\"arithmetic_bits\":320,\"physical_root_piece\":2549,\"exact_root_interval\":[\"1191984371497/5000000000000\",\"2383968743003/10000000000000\"],\"exact_strict_cut\":\"76285779072683/320000000000000\",\"cutoff_abs_j\":97,\"physical_frequency\":\"n=4|j|\",\"exact_real_delta_radius\":\"1/100000000\",\"fixed_intrinsic_parameter\":\"eta_0\",\"exact_original_profile_cover\":\"893368603925465506687/21990232555520000000000000\",\"exact_original_fold_radius\":\"3/8000\",\"exact_original_fold_strip\":\"3/128\",\"exact_genuine_inverse_strip\":\"1/64\",\"common_potential_radial_case\":\"1/6000\",\"exact_potential_complex_z_halfwidth\":\"1/9409\",\"exact_reference_terminal_T\":\"1/2000\",\"both_reference_columns_and_both_carriers\":true,\"all_output_modes_and_means\":true,\"tau_integration\":\"exact integral of tau^(-1/2) on [0,1] equals 2\",\"profile_pieces\":27,\"input_window\":\"H^(-4/3)\",\"error_profile_output_window\":\"old-angle L2\",\"density_zero_raw_scalar_output_window\":\"old-angle H^(-1), full mean retained\",\"density_one_scalar_output_window\":\"old-angle L2\",\"extra_differential_source_window\":\"old-angle H^(-5/3)\",\"old_profile_calibration_or_amplitude_calls\":0,\"old_numerical_integration_calls\":0,\"full_physical_C_Dar_claimed\":false,\"full_incoming_inverse_or_strong_return_claimed\":false}")

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def payload_sha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
def read(p):return json.loads(Path(p).read_text(encoding="utf-8"))
def save(p,x,compressed=False):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
    b=gzip.compress(raw,mtime=0) if compressed else raw
    t=p.with_name(p.name+".tmp");t.write_bytes(b);t.replace(p)
def ex(x):
    x=Q(x);return arb(x.numerator)/arb(x.denominator)
def rb(v):
    if isinstance(v,arb):return v
    if isinstance(v,(int,Q)):return ex(v)
    if isinstance(v,str):return arb(v)
    return arb(v["ball"])
def up(v):
    a=rb(v)
    if not a.is_finite() or a.lower()<0:raise ValueError("invalid complete nonnegative budget")
    return a.upper()
def gap(v,label):
    a=rb(v).lower()
    if not a.is_finite() or not a>0:raise ValueError("unproved strict positive gap: "+label)
    return a
def pw(x,p):return (rb(x).log()*ex(p)).exp()
def rec(x):return dict(ball=rb(x).str(52))
def encode(x):
    if isinstance(x,arb):return rec(x)
    if isinstance(x,Q):return str(x)
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [encode(v) for v in x]
    return x
def add(*v,k=2):
    if not v or min(map(len,v))<=k:raise ValueError("missing complete angular derivative")
    return [up(sum((a[i] for a in v),arb(0))) for i in range(k+1)]
def scale(a,c):return [up(x*rb(c)) for x in a]
def mul(a,b,k=2):
    if min(len(a),len(b))<=k:raise ValueError("missing complete product derivative")
    return [up(sum((math.comb(q,j)*a[j]*b[q-j] for j in range(q+1)),arb(0))) for q in range(k+1)]
def product(*v,k=2):
    z=[arb(1)]+[arb(0)]*k
    for a in v:z=mul(z,a,k)
    return z
def vector(x,k):
    if len(x)!=2 or any(len(a)!=k+1 for a in x):raise ValueError("saved vector derivative order changed")
    return [[up(v) for v in a] for a in x]
def deriv(v):return [a[1:] for a in v]
def accepted(path,identity,gate):
    run,source,manifest,digest,ngates=identity
    e=read(path);r=e.get("actual_scientific_receipt",{})
    gate("accepted complete run "+run+"/1 retains immutable success and its exact runtime",
        sha(path)==digest and str(e.get("run_id"))==run and str(e.get("run_attempt"))=="1"
        and e.get("complete") is True and e.get("actual_returncode")==0 and e.get("actual_failure") is None
        and e.get("source_budget_source_sha256")==source and e.get("input_manifest_sha256")==manifest
        and r.get("source_sha256")==source and r.get("input_manifest_sha256")==manifest
        and r.get("complete") is True and r.get("proved") is True and r.get("actual_returncode")==0
        and r.get("failure") is None and r.get("runtime")==RUNTIME
        and len(r.get("gates",[]))==ngates and all(g.get("passed") is True for g in r["gates"]))
    return r

def saved_columns(R,gate):
    sv=R["accepted_SV_execution"]["complete_exact_inverse_column_conclusion"]
    hp=R["accepted_HP_execution"]["complete_normalized_p_zero_conclusion"]
    bg=R["accepted_BG_execution"]["complete_normalized_g_zero_conclusion"]
    dg=R["accepted_DG_execution"]["complete_genuine_derivative_conclusion"]
    dt=R["accepted_DG_execution"]["complete_direct_physical_transport_conclusion"]
    rv=R["accepted_RV_execution"]["complete_negative_Taylor_conclusion"]
    rj=R["accepted_RJ_execution"]["complete_new_density_one_column_conclusion"]
    raw=dict(w0=[sv["complete_inverse_column_first_angular_upper"],sv["complete_inverse_column_second_angular_upper"]],
        p0=hp["complete_normalized_p_zero_angular_derivative_upper"],
        g0=bg["complete_normalized_g_zero_angular_derivative_upper"],
        w1=[dg["complete_a1_value_derivative_upper"],dg["accepted_b1_value_derivative_upper"]],
        p1=rj["complete_physical_p_angular_derivative_upper"],g1=dt["complete_g_angular_derivative_upper"])
    gate("the six complete saved columns retain their original derivative orders, signs and physical means",
        all(len(raw[k])==2 and all(len(v)==4 for v in raw[k]) for k in ("w0","p0","g0","w1"))
        and all(len(raw[k])==2 and all(len(v)==3 for v in raw[k]) for k in ("p1","g1"))
        and dg["accepted_b1_value_derivative_upper"]==rv["retained_complete_b1_value_derivative_upper"]
        and bg["accepted_complete_normalized_p_zero_angular_derivative_upper"]==raw["p0"]
        and sv["full_radial_G_and_all_output_means_retained"]
        and hp["full_radial_W_and_all_output_means_retained"]
        and bg["full_radial_principal_and_all_means_retained"]
        and dt["full_amplitude_means_and_signed_carriers_retained"]
        and rj["all_amplitude_means_both_components_and_both_signs_retained"])
    cols={k:vector(v,3 if k in ("w0","p0","g0","w1") else 2) for k,v in raw.items()}
    summary=dict(complete_saved_columns_payload_sha256=payload_sha(raw),
        exact_saved_derivative_counts={k:[len(v) for v in x] for k,x in raw.items()},
        density_zero_columns_are_Bw0_Bp0_Bg0_in_that_order=True,
        density_one_columns_are_w1V_p1_g1_without_extra_inverse=True,
        density_one_g_is_DG_complete_signed_disk_not_a_positive_reuse_of_negative_row_max=True,
        p0_equals_eta_times_h0_and_p1_equals_eta_times_h1=True,
        radial_eta_inverse_is_reserved_for_the_next_physical_receiver=True,
        all_output_modes_and_full_means_retained=True)
    return cols,summary

def original_positive_coefficients(R,gate):
    r=R["complete_genuine_execution"]
    rows=r["complete_positive_linear_operator_conclusion"]
    p=r["mathematical_parameters"]
    gate("all eighteen read coefficients bound the same original positive algorithm and fixed three branches",
        len(rows)==3 and [x["branch"] for x in rows]==list(BRANCHES)
        and all(x["exact_input_component_order"]==list(COMPONENTS) for x in rows)
        and all(len(x["complete_positive_linear_coefficients"])==len(x["selected_inputs"])==6 for x in rows)
        and all(o["component"]==i and o["denominator_is_lower_for_bound_number_only"] is True
            and gap(o["positive_budget_parameter_lower"],"original algorithm-input number")>0
            for x in rows for i,o in enumerate(x["selected_inputs"]))
        and p["cutoff_abs_j"]==97 and p["physical_frequency"]=="4j"
        and p["exact_physical_cover"]==str(H) and p["original_fold_radius"]==str(RG)
        and p["original_fold_phi_strip"]==str(SG) and p["genuine_inverse_phi_strip"]==str(SB)
        and p["fixed_intrinsic_parameter"]=="eta_0" and p["real_parameter_values_only"] is True)
    kappa=[[up(v) for v in row["complete_positive_linear_coefficients"]] for row in rows]
    profiles=[]
    for name,a in zip(BRANCHES,kappa):
        # IN.17b: each accepted kappa bounds the same underlying positive
        # coefficient. The original positive tail participates in c_der>4.
        pv=[up(min(4*a[0],a[2]/4)),up(a[1]/8),up(a[0]/4)]
        qv=[up(min(4*a[3],a[5]/4)),up(a[4]/8),up(a[3]/4)]
        profiles.append(dict(branch=name,height=pv,derivative=qv))
    pp=add(*(x["height"] for x in profiles));qq=add(*(x["derivative"] for x in profiles))
    sums=[up(sum((a[i] for a in kappa),arb(0))) for i in range(6)]
    summary=dict(accepted_positive_calibration_payload_sha256=payload_sha(rows),
        complete_recovered_original_profile_triples=encode(profiles),
        complete_height_profile_sum=encode(pp),complete_derivative_profile_sum=encode(qq),
        exact_input_component_order=list(COMPONENTS),
        common_rho_minus_quarter_removed_from_original_coefficients=True,
        all_candidates_bound_same_positive_coefficient=True,
        no_old_profile_or_positive_calibration_called=True,
        no_positive_tail_discarded_or_upper_bound_subtracted=True)
    return sums,pp,qq,summary

def common_strict_domain(R,gate):
    pc=R["accepted_PC_execution"]["complete_positive_domain_conclusion"]
    ppm=R["accepted_PC_execution"]["mathematical_parameters"]
    sv=R["accepted_SV_execution"]["complete_exact_inverse_column_conclusion"]
    hp=R["accepted_HP_execution"]["complete_normalized_p_zero_conclusion"]
    bg=R["accepted_BG_execution"]["complete_normalized_g_zero_conclusion"]
    dg=R["accepted_DG_execution"]["complete_genuine_derivative_conclusion"]
    gd=R["accepted_DG_execution"]["complete_direct_physical_transport_conclusion"]
    rv=R["accepted_RV_execution"]["complete_domain_conclusion"]
    rj=R["accepted_RJ_execution"]["complete_retained_radial_coefficient_conclusion"]
    wd=R["Taylor_execution"]["complete_domain_conclusion"]
    h=Q(rv["exact_negative_rho_cover"])
    gate("the reused cut columns and fold constants retain the complete same real family and signed disk",
        ppm["exact_root_interval"]==list(map(str,ROOTS)) and ppm["fixed_intrinsic_parameter"]=="eta_0"
        and ppm["exact_real_delta_radius"]=="1/100000000"
        and Q(pc["exact_reused_signed_radius"])==h
        and all(Q(x["exact_negative_rho_cover"])==h for x in (sv,hp,bg,dg,gd,rj))
        and all(Q(x["exact_original_fold_radius"])==RG and Q(x["exact_original_fold_strip"])==SG
            for x in (sv,hp,bg,rj))
        and Q(rv["exact_original_whole_cover"])==H
        and sv["same_full_complex_delta_and_old_angle_domains_retained"]
        and hp["same_full_SG_zero_order_moduli_and_SB_inverse_used"]
        and rj["inverse_uses_physical_input_labels"]
        and rj["full_radial_Q_V_and_all_amplitude_means_retained"]
        and pc["same_complete_terminal_solution_and_root_shear"]
        and pc["all_six_required_holomorphic_domains_checked"]
        and Q(wd["exact_whole_physical_piece_cover_radius"])==H)
    cases=[c for c in R["potential_execution"]["cases"] if c["exact_complex_radial_radius"]=="1/6000"]
    if len(cases)!=1:raise ValueError("the accepted common potential case is not unique")
    pot=cases[0];image=gap(pot["reference_image"]["complete_image_disk_radius_lower"],"same potential T disk")
    vp=[up(pot["complete_modulus_upper"][k]) for k in ("V","V_T","V_TT")]
    ell=[up(x) for x in wd["complete_Fuchsian_integral_T_derivative_modulus_upper"]]
    ell34=[up(x) for x in rv["complete_additional_Fuchsian_derivatives_3_4"]]
    gate("the entire segment uses original canonical V and Fuchsian bounds without new old quotient evaluation",
        pot["complete"] and pot["proved"] and pot["failure"] is None
        and pot["both_carrier_signs_retained"] and pot["whole_complex_bilinear_family"]
        and pot["exact_complex_delta_square_halfwidth"]=="1/100000000"
        and pot["exact_complex_z_square_halfwidth"]=="1/9409"
        and pot["fixed_intrinsic_parameter"]=="eta_0"
        and Q(pot["reference_image"]["old_fold_original_radius"])==RG
        and Q(pot["reference_image"]["old_fold_phi_width"])==SG
        and len(ell)==3 and len(ell34)==2
        and wd["original_potential_execution_sha256"]==EXPECTED["potential_execution"][3]
        and wd["same_complex_delta_and_z_squares"] and wd["same_reference_T_not_old_r_substituted"]
        and rv["original_full_mean_gauge_retained"] and not rv["original_potential_and_fold_producers_called"]
        and rj["accepted_RV_domain_conclusion_sha256"]==payload_sha(rv))
    ell+=ell34
    rho0=ROOTS[0]-RCUT;rho1=ROOTS[1]-RCUT
    Am=gap(pc["Am"],"original full fold A lower");Ap=up(pc["Ap"])
    t0=gap(ex(rho0)*pw(Am,Q(2,3)),"strict negative T modulus lower")
    t1=up(ex(rho1)*pw(Ap,Q(2,3)))
    oldTh=up(rv["new_complete_negative_T_image_upper"])
    X=[up(v) for v in sv["complete_X_angular_derivative_upper"]]
    Y=[up(v) for v in sv["complete_Y_angular_derivative_upper"]]
    Qjet=[up(v) for v in rj["complete_Q_angular_derivative_upper"]]
    xm=up(sv["complete_x_minus_one_upper"])
    gate("P22 lies strictly in the original root piece and every tauT lies in the paid canonical product",
        0<rho0<=rho1<Q(4,10**6)<h<H<RG
        and t0>0 and t0<t1 and t1<oldTh<image and oldTh<ex(Q(1,2000))
        and len(X)==len(Y)==len(Qjet)==4 and xm<1
        and gap(rv["new_complete_potential_T_margin_lower"],"accepted original RV margin")>0
        and gap(sv["accepted_complete_determinant_gap"],"same physical-input genuine inverse")>0
        and Q(sv["exact_accepted_inverse_strip"])==SB
        and Q(hp["exact_accepted_inverse_strip"])==Q(bg["exact_accepted_inverse_strip"])==SB)
    # All derivatives below are real-circle bounds at this actual negative cut.
    # omega=2*(-T)^(3/2)/3, y=T_phi. The lower T modulus belongs to this cut.
    om1=up(t1.sqrt()*Y[0])
    om2=up(Y[0]*Y[0]/(2*t0.sqrt())+t1.sqrt()*Y[1])
    om3=up(3*Y[0]*Y[1]/(2*t0.sqrt())+Y[0]**3/(4*pw(t0,Q(3,2)))+t1.sqrt()*Y[2])
    m3=gap(1-xm-3*om1,"new common phase X plus c omega, abs(c)<=3")
    f23=up(X[1]+3*om2);f33=up(X[2]+3*om3)
    gate("the new all27-piece phase gap is strictly positive and retains both physical input signs",
        m3>0 and f23.is_finite() and f33.is_finite()
        and m3<=1 and t1<image and all(v.is_finite() for v in (om1,om2,om3)))
    gate("the complete nonzero root matrix keeps the analytic16384 strong multiplier qualification",
        vp[0]<276 and vp[1]<27000 and ell[0]<276 and ell[1]<9000
        and N==388 and N*N>52**3
        and pc["same_complete_terminal_solution_and_root_shear"] is True)
    hp1=up(ell[3]+vp[1]*ell[0]+vp[0]*ell[1])
    hp2=up(ell[4]+vp[2]*ell[0]+2*vp[1]*ell[1]+vp[0]*ell[2])
    Hjet=[up(ell[2]+vp[0]*ell[0]),up(hp1*Y[0]),up(hp2*Y[0]*Y[0]+hp1*Y[1])]
    gate("the complete new H=BTT+VB retains every canonical derivative and all-segment chain factor",
        len(Hjet)==3 and all(v.is_finite() and v>=0 for v in Hjet)
        and len(vp)==3 and len(ell)==5 and t1<oldTh<image)
    d=dict(rho0=rho0,rho1=rho1,T=[t1,Y[0],Y[1]],Tmin=t0,Tmax=t1,
        X=X,Y=Y,Q=Qjet,m3=m3,F2=f23,F3=f33,H=Hjet,
        common_potential_image=image,accepted_negative_T_image=oldTh)
    summary=dict(exact_strict_cut=str(RCUT),exact_rho_interval=[str(rho0),str(rho1)],
        exact_signed_disk_radius=str(h),exact_old_profile_cover=str(H),
        accepted_PC_fold_domain_payload_sha256=payload_sha(pc),
        accepted_SV_column_payload_sha256=payload_sha(sv),
        accepted_RV_domain_payload_sha256=payload_sha(rv),
        accepted_RJ_coefficient_payload_sha256=payload_sha(rj),
        accepted_canonical_Fuchsian_0_4_payload_sha256=payload_sha(
            wd["complete_Fuchsian_integral_T_derivative_modulus_upper"]+rv["complete_additional_Fuchsian_derivatives_3_4"]),
        complete_T_modulus_lower=rec(t0),complete_T_modulus_upper=rec(t1),
        accepted_complete_T_segment_radius_upper=rv["new_complete_negative_T_image_upper"],
        accepted_common_potential_T_image_lower=pot["reference_image"]["complete_image_disk_radius_lower"],
        complete_omega_angular_derivative_upper=encode([om1,om2,om3]),
        complete_new_three_phase_gap_lower=rec(m3),
        complete_new_three_phase_second_derivative_upper=rec(f23),
        complete_new_three_phase_third_derivative_upper=rec(f33),
        complete_H_angular_derivative_upper=encode(Hjet),
        exact_root_matrix_strong_multiplier_upper="16384",
        actual_fixed_cut_all_tau_segments=True,inner_profiles_use_outer_A_at_effective_tau_rho=True,
        no_old_one_phase_gap_relabelled_as_three_phase_gap=True,
        no_real_angle_jet_promoted_to_complex_strip=True,
        no_beta_n_zero_substitution_or_Hilbert_Schmidt_root_diagonal=True,
        all_complete_physical_means_and_both_reference_columns_retained=True)
    return d,summary

class NewFunctionals:
    """Six new coefficients in each window; no original profile is evaluated."""
    def __init__(self,kappa,p,q,d,gate):
        r=up(pw(ex(d["rho0"]),Q(-1,4)))
        self.weak=[up(r*v) for v in kappa]
        self.zero=[up(4*v) for v in self.weak]
        self.strong_factor=up(2*pw(ex(N),Q(-2,3)))
        self.integral=[];self.error=[];self.applications=0
        pref=up(2*arb.pi()*pw(ex(d["rho0"]),Q(-3,4)))
        m=d["m3"];f=d["F2"]
        for ell in range(6):
            a=[arb(0)]*3;b=[arb(0)]*3
            (a if ell<3 else b)[ell%3]=arb(1)
            profile=add(mul(p,a),mul(q,b))
            z=scale(product(d["T"],d["H"],profile,p,q),pref)
            c=up((z[0]+arb.pi()**2/48*(z[2]/m**2+z[1]*f/m**3))/m.sqrt())
            self.integral.append(c)
            self.error.append(up(16384*self.zero[ell]+self.strong_factor*c))
        gate("the six new all-tau coefficients retain the exact factor2 and the full root plus integral error",
            all(len(x)==6 and all(v.is_finite() and v>0 for v in x)
                for x in (self.weak,self.zero,self.integral,self.error))
            and len(p)==len(q)==3 and self.strong_factor>0)
    def apply(self,v,kind="error"):
        if len(v)!=2 or min(map(len,v))<3:raise ValueError("missing receiver angular triple")
        coeff=getattr(self,kind);inp=v[0][:3]+v[1][:3]
        self.applications+=1
        return up(sum((coeff[i]*inp[i] for i in range(6)),arb(0)))
    def conclusion(self):
        return dict(exact_input_component_order=list(COMPONENTS),
            complete_original_weak_positive_functional_coefficients=encode(self.weak),
            complete_zero_order_functional_coefficients=encode(self.zero),
            complete_all_tau_integral_functional_coefficients=encode(self.integral),
            complete_strong_Darboux_error_functional_coefficients=encode(self.error),
            complete_n_minus_two_strong_multiplier_upper=rec(self.strong_factor),
            exact_tau_integral="2",all27_phase_products_and_complete_binomial_factors=True,
            root_diagonal_is_an_input_multiplier_not_a_columnwise_HS_sum=True,
            old_positive_coefficients_only_read_new_cut_radial_weight_applied=True,
            zero_order_output_window="L2",integral_output_window="L2 before input n^(-2)",
            Darboux_error_window="H^(-4/3) to old-angle L2",
            weak_free_profile_window="H^(-4/3) to old-angle H^(-5/3)",
            all_output_means_and_both_reference_column_inputs_retained=True)

def complete_scalar_receivers(cols,d,A,gate):
    z=[arb(0)]*3
    dz={};one={};extraT={};Tamps={}
    # Density zero has n times the normalized S_E row. IN.24 performs the
    # old primitive before estimating it; its extra inhomogeneous row remains.
    for name in ("w0","p0","g0"):
        v=cols[name]
        value=A.apply(v);phi=A.apply(deriv(v))
        amp=product(d["H"],d["Y"],v[1])
        te=up(A.strong_factor*A.apply([z,amp],"zero"))
        dz[name]=dict(complete_normalized_column_error_L2_upper=rec(value),
            complete_normalized_column_derivative_error_L2_upper=rec(phi),
            complete_inhomogeneous_primitive_error_L2_upper=rec(te),
            complete_raw_scalar_Hminus1_upper=rec(up(value+phi+te)))
        extraT[name]=te;Tamps[name]=amp
    for name in ("w1","p1","g1"):
        one[name]=dict(complete_scalar_error_L2_upper=rec(A.apply(cols[name])))
    # H_V has exact second row (y,i epsilon x). This recovers only the
    # needed second component from already accepted normalized columns.
    # It does not replace or discard the V-containing first row elsewhere.
    X=d["X"];Y=d["Y"];QX=mul(d["Q"],X)
    wsecond=add(mul(Y,cols["w0"][0]),mul(X,cols["w0"][1]))
    psecond=add(mul(Y,cols["p0"][0]),mul(X,cols["p0"][1]))
    omega0=add(mul(QX,wsecond),mul(Y,psecond))
    omega1=add(mul(QX,cols["w1"][1]),mul(Y,cols["p1"][1]))
    amps=[mul(d["H"],omega0),mul(d["H"],omega1)]
    exD=[up(A.apply([z,amps[0]],"weak")/N),up(A.apply([z,amps[1]],"weak")/(N*N))]
    gate("all six scalar receivers and both exact inhomogeneous source rows retain their separate windows",
        len(dz)==len(one)==len(extraT)==3 and len(exD)==2
        and A.applications==14 and all(v.is_finite() and v>=0 for v in exD)
        and all(v.is_finite() and v>=0 for row in amps for v in row))
    return dict(density_zero=dz,density_one=one,
        complete_inhomogeneous_primitive_amplitude_angular_upper=encode(Tamps),
        complete_inhomogeneous_differential_amplitude_angular_upper=encode(amps),
        complete_inhomogeneous_differential_source_Hminus5_3_upper=encode(exD),
        exact_differential_source_input_weights=["1/n","1/n^2"],
        exact_primitive_extra_input_weight="1/n^2",
        normalized_second_row_recovery_identity="Q*x*(y*Zw_a+i*epsilon*x*Zw_b)-y*(y*Zp_a+i*epsilon*x*Zp_b)",
        complete_HV_first_row_retained_in_other_saved_columns=True,
        density_zero_w0_p0_g0_include_all_output_means=True,
        density_one_w1V_p1_g1_include_all_output_means=True,
        p_rows_have_not_yet_been_multiplied_by_radial_eta_inverse=True,
        physical_J_L_B_n_g_Tq_and_free_R2_R3_not_yet_composed=True,
        raw_Hminus1_not_renamed_raw_L2=True,
        final_physical_C_Dar_not_claimed=True,full_incoming_inverse_not_claimed=True,
        full_strong_return_R0_not_claimed=True)

def render_conclusion(doc):
    out={k:doc[k] for k in ("kind","complete","proved","actual_returncode","failure","source_sha256",
        "input_manifest_sha256","runtime","arithmetic_bits","run_id","run_attempt","actual_mathematical_wall_seconds") if k in doc}
    out["passed_gates"]=sum(g["passed"] for g in doc["gates"]);out["total_gates"]=len(doc["gates"])
    out["mathematical_parameters"]=doc["mathematical_parameters"]
    for k in ("complete_strict_cut_domain_conclusion","complete_new_functional_conclusion",
            "complete_scalar_receiver_conclusion","scope"):
        if k in doc:out[k]=doc[k]
    return "\n".join(["# All-segment Darboux error and strict-cut scalar receivers","",
        "These are complete scalar receiver bounds at the original P22 cut.",
        "Physical J/L/B and radial frame factors, free R2/R3, the incoming inverse and the complete return remain separate.",
        "",chr(96)*3+"json",json.dumps(out,sort_keys=True,indent=2,ensure_ascii=False,allow_nan=False),chr(96)*3,""])

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("repo-root","manifest","workdir","process","conclusion","out"):
        p.add_argument("--"+name,type=Path,required=True)
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("new scientific arithmetic is permitted only on the public repository Actions runner")
    runtime=dict(python=platform.python_version(),python_flint=flint.__version__,numpy=numpy.__version__,scipy=scipy.__version__)
    if runtime!=RUNTIME:raise RuntimeError("the frozen public scientific runtime changed")
    ctx.prec=320;a.workdir.mkdir(parents=True,exist_ok=True);started=time.monotonic()
    doc=dict(kind=KIND,complete=False,proved=False,actual_returncode=1,failure=None,gates=[],
        source_sha256=sha(__file__),input_manifest_sha256=sha(a.manifest),runtime=runtime,arithmetic_bits=320,
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),actual_scientific_checkout_commit=os.environ.get("ACTUAL_CHECKOUT_COMMIT"),
        mathematical_parameters=PARAMETERS,original_successful_small_receipts_read=0,
        original_positive_linear_coefficients_read=0,saved_complete_column_derivative_bounds_read=0,
        new_profile_budget_number_recoveries=0,new_three_phase_gap_closures=0,
        new_complete_H_angular_derivative_bounds=0,new_positive_functional_coefficients=0,
        new_complete_positive_functional_evaluations=0,new_density_zero_scalar_receivers=0,
        new_density_one_scalar_receivers=0,new_complete_inhomogeneous_source_receivers=0,
        old_numerical_enclosures_recomputed=0,old_profiles_or_frequency_partitions_recomputed=0,
        old_positive_calibration_recomputed=0,old_amplitude_derivatives_or_Taylor_tails_recomputed=0,
        old_potential_Fuchsian_or_inverse_closures_recomputed=0,old_rows_words_or_integrals_recomputed=0,
        old_PC_PW_SP_or_other_completed_producers_called=0,
        new_tau_quadrature_or_truncation_used=False,original_natural_stage_bytes_modified=False,
        final_physical_C_Dar_claimed=False,full_incoming_inverse_claimed=False,full_strong_return_R0_evaluated=False,
        temporary_native_is_not_published=True,reproducible_outputs_published_to_repository=False,
        reproducible_outputs_uploaded_to_Releases=False,new_reproducible_data_artifact_uploaded=False)
    def gate(name,truth):
        passed=bool(truth);doc["gates"].append(dict(name=name,passed=passed))
        if not passed:raise ValueError("actual IN scalar gate failed: "+name)
    try:
        manifest=read(a.manifest)
        gate("the immutable new manifest fixes the same source, IN contract, runtime and scalar parameters",
            manifest["source_sha256"]==sha(__file__) and manifest["contract_sha256"]==CONTRACT
            and manifest["runtime"]==RUNTIME and manifest["mathematical_parameters"]==PARAMETERS
            and len({e["path"] for e in manifest["files"]})==len(manifest["files"]))
        for e in manifest["files"]:
            q=a.repo_root/e["path"]
            if not q.is_file() or q.stat().st_size!=e["bytes"] or sha(q)!=e["sha256"]:
                raise ValueError("immutable input changed: "+e["path"])
        paths={k:a.repo_root/v for k,v in manifest["input_paths"].items()}
        gate("all inputs are immutable small text conclusions or primary identity evidence, with zero old imports",
            set(EXPECTED)<=set(paths) and sha(paths["contract"])==CONTRACT
            and manifest["all_inputs_are_current_small_texts"] is True
            and manifest["old_successful_scientific_calls_allowed"]==0
            and all(not e["path"].endswith((".gz",".npz",".zip")) for e in manifest["files"]))
        R={k:accepted(paths[k],identity,gate) for k,identity in EXPECTED.items()}
        doc["original_successful_small_receipts_read"]=len(R)
        cols,con=saved_columns(R,gate);doc["complete_saved_columns_conclusion"]=con
        doc["saved_complete_column_derivative_bounds_read"]=44
        kapp,pv,qv,con=original_positive_coefficients(R,gate)
        doc["complete_recovered_profile_conclusion"]=con
        doc["original_positive_linear_coefficients_read"]=18;doc["new_profile_budget_number_recoveries"]=18
        d,con=common_strict_domain(R,gate);doc["complete_strict_cut_domain_conclusion"]=con
        doc["new_three_phase_gap_closures"]=1;doc["new_complete_H_angular_derivative_bounds"]=3
        A=NewFunctionals(kapp,pv,qv,d,gate);doc["complete_new_functional_conclusion"]=A.conclusion()
        doc["new_positive_functional_coefficients"]=24
        doc["complete_scalar_receiver_conclusion"]=complete_scalar_receivers(cols,d,A,gate)
        doc["new_complete_positive_functional_evaluations"]=A.applications
        doc["new_density_zero_scalar_receivers"]=3;doc["new_density_one_scalar_receivers"]=3
        doc["new_complete_inhomogeneous_source_receivers"]=5
        doc["scope"]=dict(complete_original_P22_cut=True,full_real_delta_family=True,
            same_physical_input_frequency_and_both_reference_columns=True,all_output_modes_and_means=True,
            new_three_phase_gap_not_old_one_phase_gap=True,whole_tau_interval_with_exact_integral2=True,
            common_profile_inputs_and_accepted_bound_numbers_only=True,
            complete_nonzero_root_beta_and_two_state_matrix_retained=True,
            complete_density_zero_and_density_one_receivers_separate=True,
            two_exact_inhomogeneous_identities_not_replaced_by_homogeneous_ones=True,
            strong_S_error_is_Hminus4_3_to_L2=True,
            density_zero_raw_scalar_is_only_Hminus1=True,
            differential_extra_sources_are_Hminus5_3=True,
            radial_eta_inverse_J_L_B_n_g_and_Tq_not_yet_composed=True,
            free_R2_R3_not_yet_composed=True,
            stable_trial_trace_finite_border_and_both_means_not_discarded=True,
            no_final_physical_C_Dar_incoming_or_complete_return_claim=True)
        gate("all new scalar conclusions are complete in their stated windows and every old producer remains unused",
            doc["original_successful_small_receipts_read"]==10
            and doc["original_positive_linear_coefficients_read"]==doc["new_profile_budget_number_recoveries"]==18
            and doc["saved_complete_column_derivative_bounds_read"]==44
            and doc["new_positive_functional_coefficients"]==24
            and doc["new_complete_positive_functional_evaluations"]==14
            and doc["new_density_zero_scalar_receivers"]==doc["new_density_one_scalar_receivers"]==3
            and doc["new_complete_inhomogeneous_source_receivers"]==5
            and all(doc[k]==0 for k in ("old_numerical_enclosures_recomputed",
                "old_profiles_or_frequency_partitions_recomputed","old_positive_calibration_recomputed",
                "old_amplitude_derivatives_or_Taylor_tails_recomputed","old_potential_Fuchsian_or_inverse_closures_recomputed",
                "old_rows_words_or_integrals_recomputed","old_PC_PW_SP_or_other_completed_producers_called")))
        native=dict(kind=KIND,source_sha256=sha(__file__),input_manifest_sha256=sha(a.manifest),
            mathematical_parameters=PARAMETERS,complete_new_domain=encode(d),
            complete_new_functionals=doc["complete_new_functional_conclusion"],
            complete_scalar_receiver_conclusion=doc["complete_scalar_receiver_conclusion"],
            complete=True,proved=True,actual_returncode=0,failure=None)
        save(a.out,native,compressed=True)
        doc["temporary_native_sha256"]=sha(a.out);doc["temporary_native_bytes"]=a.out.stat().st_size
        doc.update(complete=True,proved=True,actual_returncode=0)
    except BaseException as error:
        doc["failure"]=dict(type=type(error).__name__,message=str(error))
        raise
    finally:
        doc["actual_mathematical_wall_seconds"]=time.monotonic()-started
        # The complete science is atomically retained before any formatter.
        save(a.process,doc);a.conclusion.parent.mkdir(parents=True,exist_ok=True)
        a.conclusion.write_text(render_conclusion(doc),encoding="utf-8")
        print(json.dumps(dict(complete=doc["complete"],proved=doc["proved"],failure=doc["failure"],
            actual_returncode=doc["actual_returncode"],gates=len(doc["gates"]),
            functionals=doc["new_positive_functional_coefficients"],
            seconds=doc["actual_mathematical_wall_seconds"])),flush=True)
if __name__=="__main__":main()
