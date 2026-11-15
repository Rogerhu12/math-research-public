#!/usr/bin/env python3
"""Retained radial coefficient jets and ten complete density-one source bounds.

All completed amplitudes, folds, inverse gaps, potentials, profile constants,
source rows and radial integrals are read. Only the new Q quotient, potential
chain rule, rank derivatives and complete ten-term comparison are evaluated.
"""
from __future__ import annotations
import argparse,hashlib,json,math,os,platform,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy,scipy
from flint import arb,ctx
import fourfold_codazzi_factored_transport_companion_sources as old

PUBLIC,TOPIC,RUNTIME=old.PUBLIC,old.TOPIC,old.RUNTIME
KIND="actual_retained_radial_coefficient_density_one_sources_v1"
CONTRACT="f63693dd37786555c58abb830661b3a990c8b9ba35b8ada701734b688aacabd3"
FACTORED_SOURCE="a705c2b4c64393e3ba1ae1e043d0fbd62f516a7a80e03e47ce11820626373ee7"
AJ_SOURCE="32c45b335639a48b0d32541d03924246023e5e3f19deec1bcd8cf0549e955f03"
AJ_MANIFEST="871240a7a97011d837025aad7f9ca1707d69c17b6dec3c1f510f6415c278b74d"
AJ_EXEC="58462f96a486dede07873c4fc6aade100539f9f28ef49b49567a4acf7c2e8706"
RV_SOURCE="d59893af66b8829d924d75686fb0ecd6e6d25f9b72b70a0fac6564c4e96fdf60"
RV_MANIFEST="4718b4b818ec5d72537aa3a93e5825747a586ece87a086c7578ec6ec4c3b9ded"
RV_EXEC="0781239c0753785d2b196b77cc90c0eb343d52cc73226d84d7f8f6bb23136473"
DG_SOURCE="7d28ab5f16bfec72faf898118781a5df0af9bc610e80d11bc9d67b8e0527e594"
DG_MANIFEST="cbb0f2acedd715220fc90b43bacd3dd571092b7dacd2da0cc4c554160fffe833"
DG_EXEC="48ca7d65c1abd9575c7be6e4e8ae4594cb6f4e1cf3d415cf119e2f2de3ebe425"
SV_SOURCE="44021afbf608638e7e08f584a5574acdc76738c5985d72ca0f2b036c8f7d2dc0"
SV_MANIFEST="5306e66c5102e358caba5946b3c651dda11fb98a18848f8fe27f779f775d73cf"
SV_EXEC="ba96a4832017144ea3ccd59902e8bcb8f1b0acd1c722edadc44b763dfac6c0d0"
ER_SOURCE="5e1e33549c1495f5d65a68ce3755367eb4ddbd232ffd0b5e5b6923514980b652"
ER_MANIFEST="6b47f4a62c9d2cdcb6ed7b539c89816d142bc998c140e40002c205fe24cc0df6"
ER_EXEC="dedbfcad60efd024fddab17ca948ab5720c24e34a48dcde7e25af7a0aea641fc"
S1_SOURCE="09a2cb90b2d86d0f81a2ae0fae2cb3db1500878c6611ea142eae651d46d158d8"
S1_MANIFEST="ae9c1bbeccb5c2718ef98f3c0c473ab325861e7f67d5e77b3f4a3a9903f9f38e"
S1_EXEC="107845165a3fefa5b0fb6e244e4efd0eb90bfdddda2b93977bf8962b4636f649"
HP_SOURCE="bacbc58b43d7b5463996377802ff700a6ff1abf9dc23dce835541ef934f6a6e6"
HP_MANIFEST="12f93b005f06a5df4342e25cf814b8eed39571e36594401d3194a6a08a37e5cd"
HP_EXEC="01d9990041478c1a81a6413909d388038af43395578054fd71be2e83a4f8b036"
BG_SOURCE="f3f3737931bfa528f57a8f23c0c00043c6027b7ec0d2157ec2a05fb2985d27e4"
BG_MANIFEST="77fd42dd62ba5007cca008e8c868f61d7ed317176f0290818aae091f4e1c62b1"
BG_EXEC="7736f33c74ccfc84cd8d00108f8035d6cc5d3f16cd9878f885a17481b8d17927"
P_SOURCE="042713687b7d2d561ba25678a76ae9dbd95e042ec1d57bf4a0caa89310063fe7"
P_MANIFEST="44555290b424807278c933aaa5cc26c8a8e198ef1ff02ebdc7728c4ad6810437"
P_EXEC="d4c48d613cad95a3ad67ccb965acc2e76dc4e7786634a6234850667607ea08e9"
H,ROOTS,PIECE,RG,SG,N=old.H,old.ROOTS,old.PIECE,old.RG,old.SG,old.N
SB,HI=Q(1,64),Q(1,20000)
sha,ex,rb,up,gap,rec=old.sha,old.ex,old.rb,old.up,old.gap,old.rec
read,save,unpack,encode,payload_sha=old.read,old.save,old.unpack,old.encode,old.payload_sha
FIRST=("complete_RQ_J_g","complete_primitive","old_mean_transported","old_mean_vphi","complete_SQ","complete_RQ_JL_h","old_mean_rQ")
MEAN=("complete_uJ_g","complete_uJL_h","complete_u_h")
CHANGED=tuple("density1_"+name for name in FIRST+MEAN)

def bound(v,label="complete upper"):return old.bound(v,label)

def accepted(path,run,source,manifest,digest,ngates,gate):
    if sha(path)!=digest:raise ValueError("accepted execution bytes changed")
    r=old.receipt(path,run,source,manifest,gate)
    if len(r["gates"])!=ngates:raise ValueError("accepted mathematical gate count changed")
    return r

def params():
    return json.loads(r'''{
  "arithmetic_bits": 320,
  "physical_piece": 2549,
  "fixed_intrinsic_parameter": "eta_0",
  "physical_frequency": "4j",
  "cutoff_abs_j": 97,
  "exact_negative_cover": [
    "2147184947341121/9007199254740992",
    "2383968743003/10000000000000"
  ],
  "exact_root_interval": [
    "1191984371497/5000000000000",
    "2383968743003/10000000000000"
  ],
  "exact_original_whole_cover": "893368603925465506687/21990232555520000000000000",
  "exact_negative_rho_cover": "125978014066294748203/10995116277760000000000000",
  "original_fold_radius": "3/8000",
  "original_fold_strip": "3/128",
  "accepted_inverse_radius": "1/20000",
  "accepted_inverse_strip": "1/64",
  "potential_radial_case": "1/6000",
  "complete_complex_delta_square_halfwidth": "1/100000000",
  "potential_complete_complex_z_square_halfwidth": "1/9409",
  "original_coefficient_rows_keep_their_proved_real_parameter_range": true,
  "inverse_uses_physical_input_labels": true,
  "independent_complex_frequency_inverse_claimed": false,
  "exact_input_rank_weight": "1/150544",
  "exact_Q_identity": "W/G",
  "exact_QT_derivative_identity": "(Q*T)_phi=Q*y/2",
  "exact_VTTT_budget_source": "7*upper(saved_RV_additional_Fuchsian_derivatives_3_4[0])",
  "exact_rank_identity": "(Q*V/Delta)*(-i*epsilon*x,y)^t*(i*epsilon*y*a+x*b)",
  "exact_genuine_g_identity": "G0w+n^-2*partial_phi R(w)",
  "exact_genuine_p_identity": "-i*epsilon*Q*K*w-n^-2*R(w)",
  "genuine_amplitude_identity": "w1V=free_w1+(T*b0,a0)*B(T)",
  "input_window": "H^(-4/3), both genuine columns and both signs",
  "density_one_word_window": "H^(-5/3) -> H^(-2/3)",
  "first_output_window": "ordinary L2_r H^(-2/3)",
  "independent_mean_window": "ordinary L2_r constant",
  "common_column_envelope": "abs(rho)^(-1/4)",
  "accepted_baseline_run": "43726985545/1",
  "accepted_W_run": "43726426053/1",
  "accepted_Bplus_run": "43726985545/1",
  "accepted_amplitude_run": "43720766795/1",
  "accepted_negative_image_run": "43719681982/1",
  "saved_amplitude_derivative_count": 14,
  "new_amplitude_derivative_count": 0,
  "new_source_angular_orders": [
    0,
    1,
    2
  ],
  "new_rank_angular_orders": [
    0,
    1,
    2,
    3
  ],
  "changed_complete_terms": [
    "density1_complete_RQ_J_g",
    "density1_complete_primitive",
    "density1_old_mean_transported",
    "density1_old_mean_vphi",
    "density1_complete_SQ",
    "density1_complete_RQ_JL_h",
    "density1_old_mean_rQ",
    "density1_complete_uJ_g",
    "density1_complete_uJL_h",
    "density1_complete_u_h"
  ],
  "unchanged_complete_term_count": 21,
  "original_radial_integrals_recomputed": 0,
  "new_radial_integrals": 0,
  "complete_mean_and_both_genuine_columns_retained": true
}''')

COUNTER_KEYS=["original_successful_small_receipts_read","original_complete_fold_stages_read","original_complete_coefficient_rows_read","original_selected_coefficient_rows_read","original_positive_linear_coefficients_read","original_complete_source_terms_read","original_complete_word_maxima_read","original_complete_word_maxima_consumed","accepted_complete_amplitude_derivative_bounds_read","accepted_HP_W_derivative_bounds_read","accepted_SV_X_Y_G_derivative_bounds_read","accepted_BG_Bplus_derivative_bounds_read","new_inverse_G_positive_derivative_bounds","new_Q_positive_derivative_bounds","new_QT_derivative_bounds","new_V_positive_angular_derivative_bounds","new_V_TTT_positive_budget_recoveries","new_inverse_Delta_derivative_bounds","new_complete_transport_rank_bounds","new_complete_p_source_bounds","new_complete_row_g_source_bounds","new_complete_positive_functional_evaluations","new_complete_source_row_budgets","new_complete_uniform_comparisons","new_complete_scalar_recombinations","old_numerical_enclosures_recomputed","old_target_FFT_intrinsic_repair_fold_transport_or_Taylor_recomputed","old_amplitude_derivatives_finite_sums_or_tails_recomputed","old_inverse_word_or_positive_calibration_recomputed","old_W_G_Bplus_or_V_potential_derivatives_recomputed","old_AJ_DG_RV_SV_ER_S1_HP_BG_or_companion_source_closures_called","old_source_row_or_radial_integral_recomputed","new_radial_integrals_computed","original_natural_stage_bytes_modified"]


def saved_amplitudes(DG,RV,gate):
    """Read the successful fourteen genuine amplitudes; no derivative producer."""
    d=DG["complete_genuine_derivative_conclusion"]
    r=RV["complete_negative_Taylor_conclusion"]
    h=ROOTS[1]-PIECE[0]
    raw=[d["complete_a1_value_derivative_upper"],d["complete_a1_radial_derivative_upper"],
         d["accepted_b1_value_derivative_upper"],d["accepted_b1_radial_derivative_upper"]]
    gate("all fourteen genuine value and mixed derivatives are read with their complete same-T identity",
        [len(x) for x in raw]==[4,3,4,3]
        and d["exact_negative_rho_cover"]==r["exact_new_negative_rho_cover"]==str(h)
        and d["genuine_amplitude_identity"]=="w1V=free_w1+(T*b0,a0)*B(T)"
        and d["accepted_RV_Taylor_conclusion_sha256"]==payload_sha(r)
        and raw[2]==r["retained_complete_b1_value_derivative_upper"]
        and raw[3]==r["retained_complete_b1_radial_derivative_upper"]
        and d["full_zero_mode_and_both_carriers_retained"]
        and not d["old_finite_coefficients_norms_and_new_b1_bounds_recomputed"])
    vals=[[bound(v,"saved complete genuine derivative") for v in row] for row in raw]
    return dict(a=vals[0],ar=vals[1],b=vals[2],br=vals[3]),dict(
        accepted_DG_genuine_conclusion_sha256=payload_sha(d),
        accepted_RV_Taylor_conclusion_sha256=payload_sha(r),
        saved_value_orders=[0,1,2,3],saved_radial_orders=[0,1,2],
        saved_complete_amplitude_bounds_read=14,new_amplitude_derivatives_computed=0,
        exact_negative_rho_cover=str(h),exact_radial_derivative="partial_r=-partial_old_rho",
        genuine_amplitude_identity=d["genuine_amplitude_identity"],
        full_zero_mode_both_components_and_both_carriers_retained=True)

def reciprocal_jets(value_jets,inverse_zero,degree):
    """Differentiate f*f^-1=1; all arguments are complete positive budgets."""
    if len(value_jets)<degree+1:raise ValueError("incomplete reciprocal derivative input")
    inv=[bound(inverse_zero,"complete zeroth reciprocal bound")]
    for k in range(1,degree+1):
        inv.append(up(inv[0]*sum((math.comb(k,l)*value_jets[l]*inv[k-l]
            for l in range(1,k+1)),arb(0))))
    return inv

def retained_coefficient_jets(fold,HP,BG,SV,DG,RV,P,rv_source,gate):
    """RJ7--18; saved W/G/Bplus and a saved positive Cauchy budget."""
    h=ROOTS[1]-PIECE[0]
    hp=HP["complete_normalized_p_zero_conclusion"]
    bg=BG["complete_normalized_g_zero_conclusion"]
    sv=SV["complete_exact_inverse_column_conclusion"]
    dg=DG["complete_direct_physical_transport_conclusion"]
    rv=RV["complete_domain_conclusion"]
    gate("the saved W G Bplus and determinant products retain the complete physical-label domains",
        hp["exact_negative_rho_cover"]==bg["exact_negative_rho_cover"]==sv["exact_negative_rho_cover"]
            ==dg["exact_negative_rho_cover"]==rv["exact_negative_rho_cover"]==str(h)
        and hp["exact_original_fold_radius"]==bg["exact_original_fold_radius"]==sv["exact_original_fold_radius"]==str(RG)
        and hp["exact_original_fold_strip"]==bg["exact_original_fold_strip"]==sv["exact_original_fold_strip"]==str(SG)
        and hp["exact_accepted_inverse_radius"]==bg["exact_accepted_inverse_radius"]==str(HI)
        and hp["exact_accepted_inverse_strip"]==bg["exact_accepted_inverse_strip"]==str(SB)
        and 0<h<H<HI<RG and 0<SB<SG
        and hp["W_zero_order_holomorphic_strip"]==str(SG)
        and hp["W_positive_order_bounds_are_real_circle_derivatives"]
        and bg["accepted_HP_normalized_p_zero_conclusion_sha256"]==payload_sha(hp)
        and bg["accepted_SV_column_conclusion_sha256"]==payload_sha(sv)
        and bg["accepted_RV_domain_conclusion_sha256"]==payload_sha(rv)
        and bg["accepted_complete_W_angular_derivative_upper"]==hp["complete_W_angular_derivative_upper"]
        and bg["accepted_complete_determinant_gap"]==hp["accepted_complete_determinant_gap"]
            ==sv["accepted_complete_determinant_gap"]==dg["accepted_complete_determinant_lower"]
        and hp["accepted_negative_T_image"]==rv["new_complete_negative_T_image_upper"]
        and hp["no_real_circle_supremum_promoted_to_positive_strip"]
        and not hp["independent_complex_frequency_inverse_claimed"]
        and not bg["independent_complex_frequency_inverse_claimed"]
        and sv["same_full_complex_delta_and_old_angle_domains_retained"]
        and sv["potential_original_full_complex_z_modulus_read"]
        and gap(rv["accepted_complete_deformed_determinant_lower"],"accepted RV printed gap")>0)
    rawW=hp["complete_W_angular_derivative_upper"];rawG=sv["complete_G_angular_derivative_upper"]
    rawX=sv["complete_X_angular_derivative_upper"];rawY=sv["complete_Y_angular_derivative_upper"]
    rawBp=bg["complete_Bplus_angular_derivative_upper"]
    gate("all completed scalar derivative arrays and the original scalar Gi bound keep their exact roles",
        len(rawW)==len(rawG)==len(rawX)==len(rawY)==len(rawBp)==4
        and len(dg["complete_principal_Q_derivative_upper"])==4
        and bg["only_new_Bplus_derivatives_one_through_three_computed"]
        and not bg["saved_W_Bplus_zero_and_normalized_p_closures_recomputed"]
        and dg["exact_rank_identity"]=="(Q*V/Delta)*(-i*epsilon*x,y)^t*(i*epsilon*y*a+x*b)"
        and dg["exact_input_rank_weight"]=="1/150544"
        and dg["reaction_vartheta_not_inserted_in_transport_rank"]
        and bound(fold["Gi"],"original scalar G inverse")>0)
    cases=[x for x in P["cases"] if Q(x["exact_complex_radial_radius"])==Q(1,6000)]
    if len(cases)!=1:raise ValueError("the original complete potential case is not unique")
    pc=cases[0]
    gate("the original complete common-potential image and RV Cauchy budget retain the same parameter product",
        pc["complete"] and pc["proved"] and pc["failure"] is None
        and Q(pc["exact_complex_delta_square_halfwidth"])==Q(1,10**8)
        and Q(pc["exact_complex_z_square_halfwidth"])==Q(1,9409)
        and pc["fixed_intrinsic_parameter"]=="eta_0" and pc["whole_complex_bilinear_family"]
        and pc["both_carrier_signs_retained"] and pc["independent_even_mean_equation_retained"]
        and pc["actual_reference_seam_jumps_retained"]
        and len(rv["complete_additional_Fuchsian_derivatives_3_4"])==2
        and gap(rv["new_complete_potential_T_margin_lower"],"saved potential margin")>0
        and gap(rv["original_complete_potential_T_image_lower"],"saved common image")>0
        and not rv["original_potential_and_fold_producers_called"]
        and 'dt=gap(image-Th,"same potential positive image margin")' in rv_source
        and 'ell.extend([up(vp[2]/(7*dt)),up(2*vp[2]/(9*dt*dt))])' in rv_source
        and 'vp=[bound(pc["complete_modulus_upper"][k]) for k in ("V","V_T","V_TT")]' in rv_source)
    W,G,X,Y,Bp=([bound(v,"saved complete angular derivative") for v in row]
        for row in (rawW,rawG,rawX,rawY,rawBp))
    Gi=bound(fold["Gi"],"original complete scalar G inverse")
    IG=reciprocal_jets(G,Gi,3)
    QQ=[bound(dg["complete_principal_Q_derivative_upper"][0],"saved complete Q modulus")]
    for k in range(1,4):
        QQ.append(up(sum((math.comb(k,l)*W[l]*IG[k-l] for l in range(k+1)),arb(0))))
    Th=bound(hp["accepted_negative_T_image"],"saved full negative T image")
    QY=old.mul(QQ,Y,2)
    QT=[up(QQ[0]*Th)]+[up(v/2) for v in QY]
    vp=[bound(pc["complete_modulus_upper"][k],"saved full potential derivative") for k in ("V","V_T","V_TT")]
    U3=bound(rv["complete_additional_Fuchsian_derivatives_3_4"][0],"saved positive RV Cauchy budget")
    P3=up(7*U3)
    VV=[vp[0],up(vp[1]*Y[0]),up(vp[1]*Y[1]+vp[2]*Y[0]**2),
        up(vp[1]*Y[2]+3*vp[2]*Y[0]*Y[1]+P3*Y[0]**3)]
    Delta=gap(sv["accepted_complete_determinant_gap"],"accepted physical-label determinant gap")
    vy2=old.product(VV,Y,Y,k=3);q=ex(Q(1,N*N))
    DJ=[arb(0)]+[up(Bp[k]+q*vy2[k]) for k in range(1,4)]
    ID=reciprocal_jets(DJ,up(1/Delta),3)
    gate("the new reciprocal and chain-rule jets are finite on the complete saved domain without promoting real-angle bounds",
        all(v.is_finite() and v.lower()>=0 for row in (IG,QQ,QT,VV,ID) for v in row)
        and P3.is_finite() and P3>0 and Delta>0 and N==388)
    values=dict(Q=QQ,QT=QT,V=VV,inverse_Delta=ID,X=X,Y=Y,T=[Th]+Y[:3])
    conclusion=dict(exact_negative_rho_cover=str(h),exact_original_fold_radius=str(RG),
        exact_original_fold_strip=str(SG),exact_accepted_inverse_radius=str(HI),
        exact_accepted_inverse_strip=str(SB),exact_potential_radial_case="1/6000",
        exact_Q_identity="W/G",exact_QT_first_derivative_identity="(Q*T)_phi=Q*y/2",
        complete_Q_angular_derivative_upper=encode(QQ),
        complete_QT_angular_derivative_upper=encode(QT),
        complete_composed_V_angular_derivative_upper=encode(VV),
        complete_inverse_Delta_angular_derivative_upper=encode(ID),
        complete_V_TTT_Cauchy_budget_upper=rec(P3),
        accepted_scalar_G_inverse_upper=rec(Gi),
        accepted_V_TTT_positive_budget=rv["complete_additional_Fuchsian_derivatives_3_4"][0],
        accepted_potential_T_margin_lower=rv["new_complete_potential_T_margin_lower"],
        accepted_negative_T_image=hp["accepted_negative_T_image"],
        accepted_complete_determinant_gap=sv["accepted_complete_determinant_gap"],
        accepted_HP_column_conclusion_sha256=payload_sha(hp),
        accepted_BG_column_conclusion_sha256=payload_sha(bg),
        accepted_SV_column_conclusion_sha256=payload_sha(sv),
        accepted_RV_domain_conclusion_sha256=payload_sha(rv),
        accepted_potential_case_payload_sha256=payload_sha(pc),
        VTTT_is_read_from_exact_positive_budget_not_inferred_from_a_function_bound=True,
        Bplus_zero_reencoding_is_bound_by_BG_payload_not_string_equality_to_HP=True,
        all_positive_derivative_bounds_are_real_circle_only=True,
        original_analytic_column_and_real_row_parameter_products_distinguished=True,
        inverse_uses_physical_input_labels=True,independent_complex_frequency_inverse_claimed=False,
        full_radial_Q_V_and_all_amplitude_means_retained=True,
        cT_Xi_and_all_old_scalar_closures_called=False)
    return values,conclusion

def direct_rank_and_p(C,w,gate):
    """Exact ordered rank, RJ17--20, through third order before input n^-2."""
    U=old.add(old.mul(C["Y"],w["a"],3),old.mul(C["X"],w["b"],3),k=3)
    pref=old.product(C["Q"],C["V"],C["inverse_Delta"],k=3)
    R=[old.product(pref,C["X"],U,k=3),old.product(pref,C["Y"],U,k=3)]
    principal=[old.mul(C["QT"],w["b"],3),old.mul(C["Q"],w["a"],3)]
    q=ex(Q(1,N*N))
    pp=[[up(principal[i][k]+q*R[i][k]) for k in range(3)] for i in range(2)]
    gate("the complete new physical p column and ordered rank preserve both signs all means and the single external input weight",
        len(pp)==len(R)==2 and all(len(x)==3 for x in pp) and all(len(x)==4 for x in R)
        and all(v.is_finite() and v.lower()>=0 for row in pp+R+principal for v in row))
    return dict(p=pp,R=R,principal=principal),dict(
        exact_rank_identity="(Q*V/Delta)*(-i*epsilon*x,y)^t*(i*epsilon*y*a+x*b)",
        exact_genuine_p_identity="-i*epsilon*Q*K*w-n^-2*R(w)",
        exact_input_rank_weight="1/150544",
        complete_unweighted_rank_angular_derivative_upper=encode(R),
        complete_physical_p_angular_derivative_upper=encode(pp),
        reaction_vartheta_not_inserted=True,
        all_amplitude_means_both_components_and_both_signs_retained=True,
        input_weight_not_added_again_after_positive_column_functional=True)

def complete_density_one_comparisons(rows,words,C,w,source,A,W2,baseline,gate):
    """RJ21--27; seven first terms and three independent physical-mean terms."""
    if len(rows)!=6:raise ValueError("the original complete six intersections are required")
    keys=("C_RQJ_directed","C_primitive_directed","C_uJ_directed",
          "C_SQ_directed","C_RQJL_directed","C_uJL_directed")
    word={k:bound(words[k],"complete original directed word") for k in keys}
    weight=bound(W2,"complete saved squared-envelope measure").sqrt().upper()
    pp=source["p"];rank=source["R"];principal=source["principal"];q=ex(Q(1,N*N))
    Gp=A(pp);maxima={};details=[];glo=[[arb(0) for _ in range(3)] for _ in range(2)]
    for row in rows:
        c=unpack(row["bounds"])
        D=[bound(v,"saved physical drift derivative") for v in c["D"]]
        V=[bound(v,"saved physical background v derivative") for v in c["V"]]
        U=[bound(v,"saved physical background u derivative") for v in c["U"]]
        if len(D)<3 or len(V)<4 or len(U)<3:raise ValueError("missing original coefficient derivative")
        gg=[]
        for i,(value,radial) in enumerate(((w["a"],w["ar"]),(w["b"],w["br"]))):
            drift=old.mul(D,value[1:],2)
            gg.append([up(radial[k]+drift[k]+principal[i][k+1]+q*rank[i][k+1]) for k in range(3)])
        qq=[old.add(old.mul(V,gg[i],2),old.mul(V[1:],pp[i],2),k=2) for i in range(2)]
        yy=[old.mul(V,pp[i],2) for i in range(2)]
        uu=[old.mul(U,pp[i],2) for i in range(2)]
        Gg=A(gg);Gq=A(qq);My=A(yy);Mu=A(uu)
        eta=gap(c["eta_lower"],"original complete radial eta gap")
        Gh=up(Gp/eta);Muh=up(Mu/eta)
        J=bound(c["C_J_scalar"]);cb=bound(c["cB"]);mt=bound(c["m0_T0"])
        rQ=bound(c["m0_rQ"]);ef=bound(c["exact_nonlocal_even_mean_row_factor"])
        vals=dict(
            density1_complete_RQ_J_g=up(J*word["C_RQJ_directed"]*Gg),
            density1_complete_primitive=up(J*word["C_primitive_directed"]*Gq),
            density1_old_mean_transported=up(J*(cb*V[1]*V[0]*Gg/4+mt*Gg)),
            density1_old_mean_vphi=up(J*cb*V[1]*My),
            density1_complete_SQ=up(J*word["C_SQ_directed"]*Gh),
            density1_complete_RQ_JL_h=up(J*word["C_RQJL_directed"]*Gh),
            density1_old_mean_rQ=up(J*rQ*Gh),
            density1_complete_uJ_g=up(ef*word["C_uJ_directed"]*Gg),
            density1_complete_uJL_h=up(ef*word["C_uJL_directed"]*Gh),
            density1_complete_u_h=up(ef*Muh))
        if any(not v.is_finite() or v.lower()<0 for v in vals.values()):
            raise ValueError("invalid complete density-one row source")
        for name,value in vals.items():
            maxima[name]=value if name not in maxima else max(maxima[name],value).upper()
        for i in range(2):
            for k in range(3):glo[i][k]=max(glo[i][k],gg[i][k]).upper()
        details.append(dict(common_row=row["common_row"],exact_original_interval=row["interval"],
            exact_original_row_payload_sha256=payload_sha(row),complete_g=encode(gg),complete_q=encode(qq),
            complete_y=encode(yy),complete_u_p=encode(uu),complete_coefficients=encode(vals),
            Gamma_g=rec(Gg),M_g=rec(Gg),Gamma_q=rec(Gq),M_q=rec(Gq),M_y=rec(My),
            Gamma_h=rec(Gh),M_h=rec(Gh),M_u_h=rec(Muh)))
    terms=dict(baseline["complete_first_source_term_L2_upper"])
    means=dict(baseline["complete_independent_mean_term_L2_upper"]);comparisons=[]
    for name in FIRST+MEAN:
        key="density1_"+name;target=terms if name in FIRST else means
        prior=target[key];candidate=up(weight*maxima[key])
        selected,better=old.selected_total(prior,candidate);target[key]=selected
        comparisons.append(dict(source_term=key,
            output="first" if name in FIRST else "independent_physical_mean",
            accepted_complete_L2_upper=prior,new_complete_L2_upper=rec(candidate),
            selected_complete_L2_upper=selected,strictly_smaller_complete_term=better,
            complete_uniform_row_coefficient_upper=rec(maxima[key]),
            same_original_complete_row_count=6,original_radial_integral_recomputed=False,
            complete_original_word_contains_all_inner_factors=True,
            radial_eta_inverse_and_complete_physical_means_preserved=True))
    gate("ten complete density-one comparisons retain all six rows both windows all means and twenty-one other term objects",
        len(maxima)==len(comparisons)==10 and len(terms)==21 and len(means)==10
        and all(v==terms[k] for k,v in baseline["complete_first_source_term_L2_upper"].items() if k not in CHANGED)
        and all(v==means[k] for k,v in baseline["complete_independent_mean_term_L2_upper"].items() if k not in CHANGED))
    conclusion=dict(complete_p_positive_operator_upper=rec(Gp),
        complete_rowwise_g_angular_derivative_maxima=encode(glo),
        these_maxima_are_not_substituted_for_the_sharper_rowwise_functionals=True,
        same_complete_column_envelope="abs(rho)^(-1/4)",density=1,
        input_window="H^(-4/3)",column_output_window="H^(-5/3)",
        outer_J_window="H^(-5/3) -> H^(-2/3)",
        complete_original_source_row_count=6,complete_positive_coefficient_count=18,
        exact_G0_identity="(a_r-d*a_phi+i*epsilon*(Q*T*b)_phi,b_r-d*b_phi+i*epsilon*(Q*a)_phi)",
        exact_q_identity="v*g-v_phi*p",exact_y_identity="v*p",exact_h_identity="p/eta",
        Gamma_equals_M_for_density_one=True,
        density_zero_inverse_not_inserted=True,full_physical_independent_mean_retained=True)
    return terms,means,comparisons,conclusion,details


def render(doc):
    lines=["# Actual retained radial coefficient jets and complete density-one sources","",
        "Ten complete density-one terms are compared on the original six intersections.",
        "Fourteen complete genuine amplitude derivatives, W, G, Bplus, inverse gaps, potentials,",
        "directed whole words and the original radial measure are read from successful receipts.",
        "New arithmetic is confined to the coefficient chain rules, ordered rank and ten complete comparisons.","",
        "- Scientific child code: "+str(doc.get("actual_returncode")),
        "- Mathematical complete: "+str(doc.get("complete")),
        "- New complete comparisons: "+str(doc.get("new_complete_uniform_comparisons",0)),
        "- Saved complete amplitude bounds read: "+str(doc.get("accepted_complete_amplitude_derivative_bounds_read",0)),
        "- Old numerical enclosures recomputed: 0","- New radial integrals: 0",""]
    if doc.get("failure"):lines+=["## Actual failure","",json.dumps(doc["failure"],ensure_ascii=False),""]
    result=doc.get("complete_source_conclusion")
    if result:
        lines+=["## Complete ordinary source bounds","","| Quantity | Complete bound |","|---|---|"]
        for k in ("local_L2_upper","nonlocal_total_L2_upper","first_L2_upper","mean_L2_upper","combined_L2_upper"):
            lines.append("| "+k+" | "+result[k]["ball"]+" |")
        lines+=["","## Ten complete comparisons","",
            "| Term | Accepted | New | Retained | Improved |","|---|---|---|---|---|"]
        for row in doc["complete_comparison_conclusions"]:
            lines.append("| "+row["source_term"]+" | "+row["accepted_complete_L2_upper"]["ball"]
                +" | "+row["new_complete_L2_upper"]["ball"]+" | "+row["selected_complete_L2_upper"]["ball"]
                +" | "+str(row["strictly_smaller_complete_term"])+" |")
        c=doc["complete_retained_radial_coefficient_conclusion"]
        lines+=["","## Complete retained radial coefficient jets","",
            "| Quantity | Angular order | Complete bound |","|---|---|---|"]
        for name,key in (("Q","complete_Q_angular_derivative_upper"),("QT","complete_QT_angular_derivative_upper"),
                         ("V(T)","complete_composed_V_angular_derivative_upper"),
                         ("Delta inverse","complete_inverse_Delta_angular_derivative_upper")):
            for k,v in enumerate(c[key]):lines.append("| "+name+" | "+str(k)+" | "+v["ball"]+" |")
        lines+=["","- Complete V_TTT Cauchy budget: "+c["complete_V_TTT_Cauchy_budget_upper"]["ball"],
            "- This bound is seven times the saved positive RV budget; no function-bound inversion is used.",
            "- Positive-order coefficient jets are real-circle bounds on the complete retained parameter domains.","",
            "## Complete ordered rank and p column","",
            "| Column | Component | Angular order | Complete bound |","|---|---|---|---|"]
        col=doc["complete_new_density_one_column_conclusion"]
        for label,key in (("unweighted rank R","complete_unweighted_rank_angular_derivative_upper"),
                          ("physical p","complete_physical_p_angular_derivative_upper")):
            for i,row in enumerate(col[key]):
                for k,v in enumerate(row):lines.append("| "+label+" | "+str(i)+" | "+str(k)+" | "+v["ball"]+" |")
        o=doc["complete_density_one_operator_conclusion"]
        lines+=["","- Complete p-column positive functional: "+o["complete_p_positive_operator_upper"]["ball"],
            "- Each g, q, y and u-p functional is paid on its original complete row.",
            "- The six detailed row arrays are temporary and are identified by their payload SHA256.","",
            "## Complete 31-term ledger","","| First-row term | Complete L2 bound |","|---|---|"]
        for k,v in result["complete_first_source_term_L2_upper"].items():
            lines.append("| "+k+" | "+v["ball"]+" |")
        lines+=["","| Independent physical mean term | Complete L2 bound |","|---|---|"]
        for k,v in result["complete_independent_mean_term_L2_upper"].items():
            lines.append("| "+k+" | "+v["ball"]+" |")
    lines+=["","## Actual gates",""]
    for item in doc["gates"]:lines.append("- "+("PASS" if item["passed"] else "FAIL")+": "+item["name"])
    lines+=["","## Identity and scope","",
        "- Source SHA256: "+doc["source_sha256"],
        "- Manifest SHA256: "+doc["input_manifest_sha256"],
        "- Run: "+str(doc["run_id"])+"/"+str(doc["run_attempt"]),
        "- Actual mathematical wall seconds: "+str(doc.get("actual_mathematical_wall_seconds")),
        "- Temporary native SHA256: "+str(doc.get("temporary_native_sha256")),
        "- Temporary complete-row payload SHA256: "+str(doc.get("temporary_complete_source_row_payload_sha256")),
        "- All density-zero terms, all three local terms, and twenty-one other term balls are retained verbatim.",
        "- All fourteen completed genuine amplitude bounds are read; no amplitude producer or old source closure is called.",
        "- Both original source windows, all physical means, the true dr measure, and the root band are retained.",
        "- Source-to-wave readout, positive growing columns, strong return and a high BVP inverse remain separate.",""]
    return "\n".join(lines)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo",type=Path,required=True);p.add_argument("--manifest",type=Path,required=True)
    p.add_argument("--manifest-sha",required=True);p.add_argument("--out-dir",type=Path,required=True)
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("all new mathematical arithmetic requires this public Actions repository")
    ctx.prec=320;ctx.cap=8
    runtime=dict(python=platform.python_version(),python_flint=flint.__version__,numpy=numpy.__version__,scipy=scipy.__version__)
    if runtime!=RUNTIME:raise ValueError("accepted scientific runtime changed")
    a.out_dir.mkdir(parents=True,exist_ok=True);source=sha(__file__);started=time.monotonic()
    doc=dict(kind=KIND,public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=source,input_manifest_sha256=a.manifest_sha,runtime=runtime,arithmetic_bits=320,
        complete=False,proved=False,actual_returncode=1,failure=None,gates=[],
        full_physical_negative_volume_source_paid=False,full_high_inverse_claimed=False,
        reproducible_outputs_published_to_repository=False,reproducible_outputs_uploaded_to_Releases=False,
        new_reproducible_data_artifact_uploaded=False)
    doc.update({k:0 for k in COUNTER_KEYS})
    temporary={}
    def gate(name,condition):
        doc["gates"].append(dict(name=name,passed=bool(condition)))
        if not condition:raise ValueError(name)
    try:
        manifest=read(a.manifest);parameters=params();doc["mathematical_parameters"]=parameters
        if sha(old.__file__)!=FACTORED_SOURCE:raise ValueError("the imported complete scalar recipe changed")
        gate("the new-only source manifest exact parameter products and frozen imported recipe are byte checked",
            sha(a.manifest)==a.manifest_sha and manifest["public_repository"]==PUBLIC
            and manifest["scientific_source_sha256"]==source and manifest["mathematical_parameters"]==parameters)
        pins={e["path"]:e for e in manifest["files"]}
        if len(pins)!=len(manifest["files"]):raise ValueError("duplicate immutable pin")
        for e in manifest["files"]:
            rel=Path(e["path"]);f=a.repo/rel
            if rel.is_absolute() or ".." in rel.parts or not str(rel).startswith(TOPIC):
                raise ValueError("an immutable input left the topic")
            if not f.is_file() or f.stat().st_size!=e["bytes"] or sha(f)!=e["sha256"]:
                raise ValueError("changed exact input "+str(rel))
        if any(v not in pins for v in manifest["input_paths"].values()):raise ValueError("unlisted immutable input role")
        paths={k:a.repo/v for k,v in manifest["input_paths"].items()}
        expected=dict(contract=CONTRACT,original_factored_algorithm=FACTORED_SOURCE,
            original_RV_algorithm=RV_SOURCE,original_RV_manifest=RV_MANIFEST,accepted_RV_execution=RV_EXEC,
            original_DG_algorithm=DG_SOURCE,original_DG_manifest=DG_MANIFEST,accepted_DG_execution=DG_EXEC,
            original_SV_algorithm=SV_SOURCE,original_SV_manifest=SV_MANIFEST,accepted_SV_execution=SV_EXEC,
            original_HP_algorithm=HP_SOURCE,original_HP_manifest=HP_MANIFEST,accepted_HP_execution=HP_EXEC,
            original_BG_algorithm=BG_SOURCE,original_BG_manifest=BG_MANIFEST,accepted_BG_execution=BG_EXEC,
            potential_execution=P_EXEC,complete_genuine_execution=old.C_EXEC,directed_source_execution=old.D_EXEC,
            old_fold_majorants_stage=old.MAJORANTS,adjacent_process=old.APROC,adjacent_publication=old.APUB,
            original_fold_algorithm="410675cf78dd30d97ff052558df1a819977291d40c628211fcf623ffc0b5f783",
            original_norm_native=old.OLD_NATIVE,original_norm_process=old.OLD_PROCESS,
            directed_process="00afd54464db46f110ecff8c1968b158deedac719a363590fc366038b47fedb8")
        gate("all successful receipts original scalar algorithms and natural fold bytes retain their exact identities",
            all(sha(paths[k])==v for k,v in expected.items()))
        prior=read(paths["original_BG_manifest"])
        gate("all eighty-seven original BG pins are unchanged in the new scientific closure",
            len(prior["files"])==87 and prior["scientific_source_sha256"]==BG_SOURCE
            and all(pins.get(e["path"])==e for e in prior["files"]))
        ms=read(paths["old_fold_majorants_stage"]);ap=read(paths["adjacent_process"]);au=read(paths["adjacent_publication"])
        prs=[v for v in au["files"] if v["file"]=="consumers/stages/complete-original-reference-holomorphic-majorants.json.gz"]
        if len(prs)!=1:raise ValueError("the original fold publication receipt is not unique")
        fs=paths["original_fold_algorithm"].read_text()
        gate("the original scalar G inverse retains its complete fold source runtime publication and positive-width domain",
            ms["complete"] and ms["name"]==ms["stage"]=="complete-original-reference-holomorphic-majorants"
            and ms["source_sha256"]==old.LEGACY_SOURCE and ms["algebra_sha256"]==old.LEGACY_HELPER
            and ms["input_manifest_sha256"]==old.LEGACY_MANIFEST and ms["runtime"]==runtime
            and prs[0]["bytes"]==4501 and prs[0]["sha256"]==old.MAJORANTS
            and ap["actual_returncode"]==0 and ap["mathematical_complete"] and ap["mathematical_proved"]
            and ap["mathematical_failure"] is None and au["complete"]
            and all(ms["payload"]["majorants"][k][1:]==[str(RG),str(SG)] for k in ("A","chi"))
            and "Gi=(powr(esmax/ksmin,Q(1,6))*powr(Am,Q(-1,6))*powr(c[" in fs
            and "hEG.exp()).upper()" in fs)
        saved=unpack(ms["payload"]);fold=saved["fold"];doc["original_complete_fold_stages_read"]=1
        C=accepted(paths["complete_genuine_execution"],"43702688640",old.C_SOURCE,old.C_MANIFEST,old.C_EXEC,17,gate)
        D=accepted(paths["directed_source_execution"],"43703879926",old.D_SOURCE,old.D_MANIFEST,old.D_EXEC,12,gate)
        RV=accepted(paths["accepted_RV_execution"],"43719681982",RV_SOURCE,RV_MANIFEST,RV_EXEC,27,gate)
        DG=accepted(paths["accepted_DG_execution"],"43720766795",DG_SOURCE,DG_MANIFEST,DG_EXEC,27,gate)
        SV=accepted(paths["accepted_SV_execution"],"43722805762",SV_SOURCE,SV_MANIFEST,SV_EXEC,23,gate)
        HP=accepted(paths["accepted_HP_execution"],"43726426053",HP_SOURCE,HP_MANIFEST,HP_EXEC,25,gate)
        BG=accepted(paths["accepted_BG_execution"],"43726985545",BG_SOURCE,BG_MANIFEST,BG_EXEC,24,gate)
        P=accepted(paths["potential_execution"],"43685624307",P_SOURCE,P_MANIFEST,P_EXEC,16,gate)
        doc["original_successful_small_receipts_read"]=8
        gate("the original genuine columns physical means and real coefficient-row parameter range remain unchanged",
            C["scope"]["original_fixed_intrinsic_parameter"]=="eta_0"
            and C["scope"]["both_genuine_columns_and_both_carrier_signs"]
            and C["scope"]["all_input_abs_j_at_least97"]
            and C["scope"]["output_mean_and_complete_original_primitive_retained"]
            and C["scope"]["physical_J_only_on_its_proved_reflected_parity_domain"]
            and all(r["full_physical_negative_volume_source_paid"] and not r["full_high_inverse_claimed"]
                and r["old_numerical_enclosures_recomputed"]==0 for r in (RV,DG,SV,HP,BG))
            and HP["scope"]["other_twenty_one_complete_terms_read_verbatim"]
            and len(HP["complete_comparison_conclusions"])==10
            and len(BG["complete_comparison_conclusions"])==5)
        base=BG["complete_source_conclusion"];hpbase=HP["complete_source_conclusion"]
        bgchanges={"density0_complete_RQ_J_g","density0_complete_primitive",
            "density0_old_mean_transported","density0_old_mean_vphi","density0_complete_uJ_g"}
        stable=("actual_dr_measure","exact_negative_physical_cover","one_sided_uncertain_root_band_retained",
            "both_density_windows_retained","outer_J_window","input_window","first_output_window",
            "independent_even_mean_window","total_squared_envelope_radial_weight_upper",
            "original_temporary_row_payload_sha256","old_nine_word_and_five_physical_mean_counts","local_L2_upper")
        gate("the latest successful BG ledger retains every HP h improvement all three local terms and the original cover",
            len(base["complete_first_source_term_L2_upper"])==21
            and len(base["complete_independent_mean_term_L2_upper"])==10
            and all(base[k]==hpbase[k] for k in stable)
            and {x["source_term"] for x in BG["complete_comparison_conclusions"]}==bgchanges
            and all(base["complete_first_source_term_L2_upper"][k]==v
                for k,v in hpbase["complete_first_source_term_L2_upper"].items() if k not in bgchanges)
            and all(base["complete_independent_mean_term_L2_upper"][k]==v
                for k,v in hpbase["complete_independent_mean_term_L2_upper"].items() if k not in bgchanges)
            and base["exact_negative_physical_cover"]==[str(PIECE[0]),str(ROOTS[1])]
            and base["old_nine_word_and_five_physical_mean_counts"]==[9,5])
        amp,ampcon=saved_amplitudes(DG,RV,gate)
        doc.update(accepted_complete_amplitude_derivative_bounds_read=14,
            complete_saved_amplitude_conclusion=ampcon)
        coef,coefcon=retained_coefficient_jets(fold,HP,BG,SV,DG,RV,P,
            paths["original_RV_algorithm"].read_text(),gate)
        doc.update(accepted_HP_W_derivative_bounds_read=4,accepted_SV_X_Y_G_derivative_bounds_read=12,
            accepted_BG_Bplus_derivative_bounds_read=4,new_inverse_G_positive_derivative_bounds=3,
            new_Q_positive_derivative_bounds=3,new_QT_derivative_bounds=4,
            new_V_positive_angular_derivative_bounds=3,new_V_TTT_positive_budget_recoveries=1,
            new_inverse_Delta_derivative_bounds=4,complete_retained_radial_coefficient_conclusion=coefcon)
        source_arrays,columncon=direct_rank_and_p(coef,amp,gate)
        doc.update(new_complete_transport_rank_bounds=8,new_complete_p_source_bounds=6,
            complete_new_density_one_column_conclusion=columncon)
        rows,words=old.checked_accepted_rows(paths,C,D,BG,gate)
        doc.update(original_complete_coefficient_rows_read=1328,original_selected_coefficient_rows_read=6,
            original_complete_word_maxima_read=8,original_complete_word_maxima_consumed=6,
            original_complete_source_terms_read=31)
        positive=old.read_positive_coefficients(C,gate);A=old.PositiveOperator(positive)
        doc["original_positive_linear_coefficients_read"]=18
        terms,means,comparisons,operators,row_details=complete_density_one_comparisons(
            rows,words,coef,amp,source_arrays,A,base["total_squared_envelope_radial_weight_upper"],base,gate)
        result=old.combine(base,terms,means)
        doc.update(new_complete_row_g_source_bounds=36,new_complete_positive_functional_evaluations=25,
            new_complete_source_row_budgets=6,new_complete_uniform_comparisons=10,new_complete_scalar_recombinations=4,
            complete_density_one_operator_conclusion=operators,
            complete_comparison_conclusions=comparisons,complete_source_conclusion=result,
            strictly_smaller_complete_term_bounds=sum(int(v["strictly_smaller_complete_term"]) for v in comparisons))
        gate("all twenty-one other complete term balls including every density-zero and local term remain byte identical",
            result["local_L2_upper"]==base["local_L2_upper"]
            and all(result["complete_first_source_term_L2_upper"][k]==v
                for k,v in base["complete_first_source_term_L2_upper"].items() if k not in CHANGED)
            and all(result["complete_independent_mean_term_L2_upper"][k]==v
                for k,v in base["complete_independent_mean_term_L2_upper"].items() if k not in CHANGED)
            and sum(k not in CHANGED for k in terms)==14 and sum(k not in CHANGED for k in means)==7
            and result["total_squared_envelope_radial_weight_upper"]==base["total_squared_envelope_radial_weight_upper"]
            and result["original_temporary_row_payload_sha256"]==base["original_temporary_row_payload_sha256"])
        gate("the complete new ordinary negative-volume source is finite in both original windows with independent physical mean",
            all(bound(result[k],k).is_finite() for k in
                ("local_L2_upper","nonlocal_total_L2_upper","first_L2_upper","mean_L2_upper","combined_L2_upper"))
            and result["actual_dr_measure"] and result["one_sided_uncertain_root_band_retained"]
            and result["both_density_windows_retained"] and result["old_nine_word_and_five_physical_mean_counts"]==[9,5])
        doc["scope"]=dict(original_physical_root_piece_2549_only=True,original_fixed_intrinsic_parameter="eta_0",
            same_original_real_explicit_family=True,
            original_analytic_columns_and_real_coefficient_row_parameter_products_distinguished=True,
            complete_original_potential_z_and_delta_products_retained=True,
            all_positive_order_coefficient_jets_are_real_circle_bounds=True,
            independent_complex_frequency_inverse_claimed=False,final_column_operators_use_physical_input_labels=True,
            both_genuine_columns_and_both_carrier_signs=True,all_input_abs_j_at_least97=True,
            same_genuine_w1V_not_free_first_correction=True,
            all_fourteen_completed_amplitude_derivatives_read_verbatim=True,
            new_Q_quotient_from_saved_W_and_G=True,
            VTTT_from_original_positive_budget_not_actual_Bthird_function_bound=True,
            full_radial_Q_V_and_removable_root_factors_retained=True,
            cT_Xi_quotient_and_fixed_X_derivatives_not_used=True,
            row_radial_eta_inverse_and_full_scalar_u_Leibniz_mean_retained=True,
            all_eighteen_positive_column_coefficients_summed=True,
            all_density_zero_and_all_three_local_terms_read_verbatim=True,
            other_twenty_one_complete_terms_read_verbatim=True,
            full_amplitude_means_and_independent_physical_even_mean_retained=True,
            complete_original_primitive_and_both_directed_J_windows_retained=True,
            no_duplicate_wholeword_inner_factors=True,physical_J_only_on_its_proved_reflected_parity_domain=True,
            all_actual_physical_seams_and_reference_matching_sources_retained=True,
            original_positive_graph_and_outer_source_ports_retained=True,
            complete_row_arrays_published=False,physical_to_wave_readout_paid=False,
            full_negative_BVP_inverse_paid=False,positive_growing_column_operator_paid=False,
            cutoff97_strong_return_contraction_paid=False)
        temporary.update(complete_new_source_rows=row_details,complete_new_coefficient_arrays=encode(coef),
            accepted_positive_coefficients_payload_sha256=payload_sha(C["complete_positive_linear_operator_conclusion"]))
        doc["temporary_complete_source_row_payload_sha256"]=payload_sha(row_details)
        doc["temporary_complete_source_row_count"]=len(row_details)
        doc.update(complete=True,proved=True,actual_returncode=0,full_physical_negative_volume_source_paid=True)
    except BaseException as error:
        doc["failure"]=dict(type=type(error).__name__,message=str(error))
    finally:
        doc["actual_mathematical_wall_seconds"]=time.monotonic()-started
        temporary.update(kind=KIND,source_sha256=source,input_manifest_sha256=a.manifest_sha,complete_conclusions=doc)
        native=a.out_dir/"temporary-retained-radial-density-one-sources.json.gz"
        save(native,temporary,True)
        doc["temporary_native_sha256"]=sha(native);doc["temporary_native_bytes"]=native.stat().st_size
        doc["temporary_native_is_not_published"]=True;actual=doc["actual_returncode"]
        try:
            report=render(doc)
            raw=(json.dumps(doc,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
            if len(raw)>60000 or len(report.encode())>60000:raise ValueError("small conclusion or process exceeded60000 bytes")
            save(a.out_dir/"process.json",doc);(a.out_dir/"conclusion.md").write_text(report)
        except BaseException as error:
            small={k:v for k,v in doc.items() if k not in ("complete_saved_amplitude_conclusion",
                "complete_retained_radial_coefficient_conclusion","complete_new_density_one_column_conclusion",
                "complete_density_one_operator_conclusion","complete_comparison_conclusions","complete_source_conclusion")}
            small["actual_scientific_returncode"]=actual
            small["formatting_failure"]=dict(type=type(error).__name__,message=str(error))
            small.update(complete=False,proved=False,actual_returncode=1)
            save(a.out_dir/"process.json",small)
            (a.out_dir/"conclusion.md").write_text("# Actual retained-radial source formatting failure\n\n"
                "Original scientific child code: "+str(actual)+". Formatting is separate from mathematics.\n"
                "Temporary native SHA256: "+doc["temporary_native_sha256"]+"\n")
            actual=1
        print(json.dumps(dict(complete=doc["complete"],actual_returncode=actual,
            new_complete_comparisons=doc["new_complete_uniform_comparisons"],
            old_numerical_enclosures_recomputed=0,new_radial_integrals_computed=0,
            reproducible_data_published=False)),flush=True)
    return actual
if __name__=="__main__":raise SystemExit(main())
