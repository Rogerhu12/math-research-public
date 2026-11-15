#!/usr/bin/env python3
"""Exact normalized p columns and ten complete h-dependent source terms.

Only a new ordered B_j p(w0) column and its h source bounds are evaluated.
The genuine p(w1V) jets, inverse gaps, full column coefficients, complete
directed words, original source rows and all radial integrals are read.
"""
from __future__ import annotations
import argparse,hashlib,json,math,os,platform,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy,scipy
from flint import arb,ctx
import fourfold_codazzi_factored_transport_companion_sources as old

PUBLIC,TOPIC,RUNTIME=old.PUBLIC,old.TOPIC,old.RUNTIME
KIND="actual_exact_normalized_p_columns_complete_h_sources_v1"
CONTRACT="8101e7e6afc187bf6a0ba80fbba756ed4555bb8a9f9e204c40f219aa42da53d2"
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
H,ROOTS,PIECE,RG,SG,N=old.H,old.ROOTS,old.PIECE,old.RG,old.SG,old.N
SB,HI=Q(1,64),Q(1,20000)
sha,ex,rb,up,gap,rec=old.sha,old.ex,old.rb,old.up,old.gap,old.rec
read,save,unpack,encode,payload_sha=old.read,old.save,old.unpack,old.encode,old.payload_sha
FIRST=("complete_SQ","complete_RQ_JL_h","old_mean_rQ")
MEAN=("complete_uJL_h","complete_u_h")
CHANGED=tuple("density"+str(i)+"_"+name for i in (0,1) for name in FIRST+MEAN)

def bound(v,label="complete upper"):return old.bound(v,label)

def accepted(path,run,source,manifest,digest,ngates,gate):
    if sha(path)!=digest:raise ValueError("accepted execution bytes changed")
    r=old.receipt(path,run,source,manifest,gate)
    if len(r["gates"])!=ngates:raise ValueError("accepted mathematical gate count changed")
    return r

def params():
    return dict(arithmetic_bits=320,physical_piece=2549,fixed_intrinsic_parameter="eta_0",
        physical_frequency="4j",cutoff_abs_j=97,exact_negative_cover=[str(PIECE[0]),str(ROOTS[1])],
        exact_root_interval=list(map(str,ROOTS)),exact_original_whole_cover=str(H),
        exact_negative_rho_cover=str(ROOTS[1]-PIECE[0]),original_fold_radius=str(RG),
        original_fold_strip=str(SG),accepted_inverse_radius=str(HI),accepted_inverse_strip=str(SB),
        complete_complex_delta_square_halfwidth="1/100000000",
        potential_complete_complex_z_square_halfwidth="1/9409",
        inverse_uses_physical_input_labels=True,independent_complex_frequency_inverse_claimed=False,
        exact_input_rank_weight="1/150544",density_zero_column="B_j*p_j(w0)",
        density_one_column="p_j(w1V)",exact_h_amplitude="p_j(w)/eta",
        density_zero_derivative_orders=[0,1,2,3],density_one_saved_derivative_orders=[0,1,2],
        genuine_amplitude_identity="w1V=free_w1+(T*b0,a0)*B(T)",
        input_window="H^(-4/3), both genuine columns and both signs",
        density_zero_word_window="H^(-8/3) -> H^(-5/3)",
        density_one_word_window="H^(-5/3) -> H^(-2/3)",
        common_column_envelope="abs(rho)^(-1/4)",
        changed_complete_terms=list(CHANGED),unchanged_complete_term_count=21,
        accepted_baseline_run="43724817779/1",accepted_inverse_column_run="43722805762/1",
        accepted_genuine_p_run="43720766795/1",accepted_negative_image_run="43719681982/1",
        original_radial_integrals_recomputed=0,new_amplitude_Taylor_derivatives_computed=0,
        complete_mean_and_both_genuine_columns_retained=True)

def normalized_p_zero_column(SV,DG,RV,AJ,gate):
    """HP.13--17, only new products of saved complete scalar conclusions."""
    v=SV["complete_exact_inverse_column_conclusion"]
    d=DG["complete_direct_physical_transport_conclusion"]
    r=RV["complete_domain_conclusion"]
    a=AJ["complete_domain_conclusion"]
    h=ROOTS[1]-PIECE[0]
    gate("the completed inverse fold and full SG physical image retain the identical negative product and physical labels",
        Q(v["exact_negative_rho_cover"])==Q(d["exact_negative_rho_cover"])==Q(r["exact_negative_rho_cover"])==h
        and Q(v["exact_original_fold_radius"])==Q(a["exact_original_fold_radius"])==RG
        and Q(v["exact_original_fold_strip"])==Q(a["exact_original_fold_strip"])==SG
        and Q(v["exact_accepted_inverse_radius"])==HI
        and Q(v["exact_accepted_inverse_strip"])==SB and 0<h<H<HI<RG and 0<SB<SG
        and v["exact_physical_input_n_minus_two_paid_once"]
        and not v["independent_complex_frequency_inverse_claimed"]
        and v["same_full_complex_delta_and_old_angle_domains_retained"]
        and v["potential_original_full_complex_z_modulus_read"]
        and v["full_radial_G_and_all_output_means_retained"]
        and not v["original_fold_inverse_AJ_or_DG_closures_called"]
        and a["physical_T_image_definition_read_from_frozen_producer"]
        and a["all_sT_segments_in_accepted_product"]
        and r["accepted_AJ_connection_angular_jets_read_without_recomputation"]
        and r["original_potential_and_fold_producers_called"] is False
        and v["accepted_complete_determinant_gap"]==d["accepted_complete_determinant_lower"]
        and gap(r["accepted_complete_deformed_determinant_lower"],"saved RV determinant rounding")>0)
    rawX=v["complete_X_angular_derivative_upper"];rawY=v["complete_Y_angular_derivative_upper"]
    rawG=v["complete_G_angular_derivative_upper"];rawZ=v["complete_zeta_angular_derivative_upper"]
    gate("all accepted real-angle jets and full-strip zero-order moduli retain their exact complete arrays",
        len(rawX)==len(rawY)==len(rawG)==4 and len(rawZ)==3
        and rawY[0]==v["complete_quadratic_y_upper"]
        and rawZ[0]==v["complete_removable_y_over_T_upper"]
        and len(d["complete_principal_Q_derivative_upper"])==4
        and d["exact_rank_identity"]=="(Q*V/Delta)*(-i*epsilon*x,y)^t*(i*epsilon*y*a+x*b)"
        and d["reaction_vartheta_not_inserted_in_transport_rank"]
        and d["full_amplitude_means_and_signed_carriers_retained"])
    X=[bound(x,"saved complete X jet") for x in rawX]
    Y=[bound(x,"saved complete Y jet") for x in rawY]
    Z=[bound(x,"saved complete zeta jet") for x in rawZ]
    Q0=bound(d["complete_principal_Q_derivative_upper"][0],"saved full Q modulus")
    G0=bound(rawG[0],"saved full G modulus")
    T=bound(r["new_complete_negative_T_image_upper"],"saved full SG negative T image")
    V=bound(v["accepted_complete_V_modulus"],"saved complete V modulus")
    Delta=gap(v["accepted_complete_determinant_gap"],"saved physical-label determinant gap")
    W0=up(Q0*G0)
    W=[W0,up(W0*Z[0]/4),up(W0*(Z[0]**2/16+Z[1]/4)),
        up(W0*(Z[0]**3/64+3*Z[0]*Z[1]/16+Z[2]/4))]
    F=[up(T*Y[0]),up(Y[0]**2+T*Y[1]),
        up(3*Y[0]*Y[1]+T*Y[2]),up(3*Y[1]**2+4*Y[0]*Y[2]+T*Y[3])]
    principal=[old.mul(W,F,3),old.mul(W,X,3)]
    Bp=up(X[0]**2+T*Y[0]**2);q=ex(Q(1,N*N))
    Ca=up(V*W0*Y[0]**3*(T*Bp+q*V*(2*X[0]**2+T*Y[0]**2))/(Delta*Delta))
    Cb=up(V*W0*Y[0]**2*X[0]*(Bp+q*V*Y[0]**2)/(Delta*Delta))
    correction=[old.cauchy(Ca,SB,3),old.cauchy(Cb,SB,3)]
    column=[[up(principal[i][k]+q*correction[i][k]) for k in range(4)] for i in range(2)]
    gate("the new complete normalized p column retains both ordered correction entries and all four angular orders",
        len(column)==2 and all(len(row)==4 for row in column)
        and all(z.is_finite() and z.lower()>=0 for row in column+principal+correction for z in row)
        and all(z.is_finite() and z.lower()>=0 for z in W+F)
        and N==388 and Delta>0)
    return column,dict(exact_negative_rho_cover=str(h),exact_original_fold_radius=str(RG),
        exact_original_fold_strip=str(SG),exact_accepted_inverse_radius=str(HI),
        exact_accepted_inverse_strip=str(SB),exact_column="B_j*p_j(w0)",
        exact_W_angular_identity="W_phi=-zeta*W/4",
        complete_W_angular_derivative_upper=encode(W),
        complete_T_y_angular_derivative_upper=encode(F),
        complete_Bplus_modulus_upper=rec(Bp),
        complete_principal_angular_derivative_upper=encode(principal),
        complete_unweighted_correction_modulus_upper=encode([Ca,Cb]),
        complete_normalized_p_zero_angular_derivative_upper=encode(column),
        accepted_negative_T_image=r["new_complete_negative_T_image_upper"],
        accepted_complete_V_modulus=v["accepted_complete_V_modulus"],
        accepted_complete_determinant_gap=v["accepted_complete_determinant_gap"],
        accepted_SV_column_conclusion_sha256=payload_sha(v),
        accepted_DG_physical_transport_conclusion_sha256=payload_sha(d),
        accepted_RV_domain_conclusion_sha256=payload_sha(r),
        same_full_SG_zero_order_moduli_and_SB_inverse_used=True,
        W_zero_order_holomorphic_strip=str(SG),W_positive_order_bounds_are_real_circle_derivatives=True,
        no_real_circle_supremum_promoted_to_positive_strip=True,
        full_radial_W_and_all_output_means_retained=True,
        physical_input_n_minus_two_prefactor_paid_once=True,
        independent_complex_frequency_inverse_claimed=False,
        original_fold_inverse_or_image_closures_called=False)

def saved_p_one_column(DG,RV,SV,gate):
    d=DG["complete_direct_physical_transport_conclusion"]
    g=DG["complete_genuine_derivative_conclusion"]
    r=RV["complete_negative_Taylor_conclusion"]
    raw=d["complete_p_angular_derivative_upper"];h=ROOTS[1]-PIECE[0]
    gate("the entire accepted genuine physical p column is read with its exact rank input weight and no density-zero inverse",
        len(raw)==2 and all(len(row)==3 for row in raw)
        and d["exact_genuine_p_identity"]=="-i*epsilon*Q*K*w-n^-2*R(w)"
        and d["exact_input_rank_weight"]=="1/150544"
        and d["reaction_vartheta_not_inserted_in_transport_rank"]
        and d["full_amplitude_means_and_signed_carriers_retained"]
        and d["physical_angle_orders"]==[0,1,2]
        and d["original_fold_inverse_and_connection_producers_called"] is False
        and d["exact_negative_rho_cover"]==g["exact_negative_rho_cover"]==r["exact_new_negative_rho_cover"]==str(h)
        and g["genuine_amplitude_identity"]=="w1V=free_w1+(T*b0,a0)*B(T)"
        and g["accepted_RV_Taylor_conclusion_sha256"]==payload_sha(r)
        and g["accepted_b1_value_derivative_upper"]==r["retained_complete_b1_value_derivative_upper"]
        and g["accepted_b1_radial_derivative_upper"]==r["retained_complete_b1_radial_derivative_upper"]
        and d["accepted_complete_determinant_lower"]==SV["complete_exact_inverse_column_conclusion"]["accepted_complete_determinant_gap"])
    column=[[bound(v,"accepted complete p(w1V) derivative") for v in row] for row in raw]
    return column,dict(exact_negative_rho_cover=str(h),exact_column="p_j(w1V)",
        complete_saved_p_one_angular_derivative_upper=raw,accepted_p_derivative_count=6,
        accepted_DG_physical_transport_conclusion_sha256=payload_sha(d),
        accepted_DG_genuine_conclusion_sha256=payload_sha(g),
        accepted_RV_Taylor_conclusion_sha256=payload_sha(r),
        full_zero_mode_both_genuine_columns_and_both_carriers_retained=True,
        density_zero_inverse_column_inserted=False,additional_frequency_factor_inserted=False,
        original_p_amplitude_derivatives_or_tails_recomputed=False)

def normalized_windows(columns,A,gate):
    zero,one=columns
    A0=A(zero);D0=A([v[1:] for v in zero]);A1=A(one)
    gamma=[up(A0+D0),up(A1)];mean=[up(D0),up(A1)]
    gate("the two different complete h windows preserve their original density derivative and all means before radial eta",
        len(zero)==len(one)==2 and all(len(v)==4 for v in zero) and all(len(v)==3 for v in one)
        and all(v.is_finite() and v.lower()>=0 for v in gamma+mean))
    return gamma,mean,dict(density_zero_column="B_j*p_j(w0)",density_one_column="p_j(w1V)",
        complete_zero_column_operator_upper=rec(A0),complete_zero_derivative_operator_upper=rec(D0),
        complete_one_column_operator_upper=rec(A1),
        Gamma_before_eta_inverse=encode(gamma),M_before_eta_inverse=encode(mean),
        exact_h_zero_mean="eta^-1*A(partial_phi(B_j*p_j(w0)))",
        exact_h_one_mean="eta^-1*A(p_j(w1V))",
        rowwise_radial_eta_inverse_still_required=True,
        all_eighteen_positive_coefficients_summed=True,
        full_mean_and_both_genuine_columns_retained=True,
        input_window="H^(-4/3)",density_windows=["H^(-8/3)","H^(-5/3)"],
        intermediate_windows=["H^(-5/3)","H^(-2/3)"],
        common_column_envelope="abs(rho)^(-1/4)")

def complete_comparisons(rows,words,columns,Gamma,Mean,A,W2,baseline,gate):
    """HP.19--23: new h and u*h functionals, complete whole words, true old dr."""
    if len(rows)!=6:raise ValueError("the complete source requires all six original rows")
    weight=bound(W2,"accepted complete squared-envelope radial weight").sqrt().upper()
    KSQ=bound(words["C_SQ_directed"],"accepted complete SQ word")
    KRL=bound(words["C_RQJL_directed"],"accepted complete RQJL word")
    KUL=bound(words["C_uJL_directed"],"accepted complete independent-mean uJL word")
    maxima={};details=[]
    for row in rows:
        c=unpack(row["bounds"])
        eta=gap(c["eta_lower"],"original row radial eta gap")
        U=[bound(v,"complete original scalar u jet") for v in c["U"]]
        if len(U)<4:raise ValueError("the full background u lacks its third angular derivative")
        J=bound(c["C_J_scalar"],"complete original outer scalar J")
        rQ=bound(c["m0_rQ"],"complete original old mean rQ")
        ef=bound(c["exact_nonlocal_even_mean_row_factor"],"complete original independent-mean prefactor")
        values={};operators=[]
        for i in (0,1):
            Gh=up(Gamma[i]/eta);Mh=up(Mean[i]/eta)
            Uh=old.pair_mul(U,columns[i],3 if i==0 else 2)
            Muh=up(A([v[1:] for v in Uh] if i==0 else Uh)/eta)
            operators.append(dict(density=i,Gamma_h=Gh,M_h=Mh,M_u_h=Muh,
                radial_eta_lower=eta,complete_u_product_before_mean=Uh))
            prefix="density"+str(i)+"_"
            values.update({prefix+"complete_SQ":up(J*KSQ*Gh),
                prefix+"complete_RQ_JL_h":up(J*KRL*Gh),
                prefix+"old_mean_rQ":up(J*rQ*Mh),
                prefix+"complete_uJL_h":up(ef*KUL*Gh),
                prefix+"complete_u_h":up(ef*Muh)})
        if any(not v.is_finite() or v.lower()<0 for v in values.values()):
            raise ValueError("invalid complete new h source coefficient")
        for name,value in values.items():
            maxima[name]=value if name not in maxima else max(maxima[name],value).upper()
        details.append(dict(common_row=row["common_row"],exact_original_interval=row["interval"],
            exact_original_row_payload_sha256=payload_sha(row),
            complete_h_operators=encode(operators),complete_coefficients=encode(values)))
    terms=dict(baseline["complete_first_source_term_L2_upper"])
    means=dict(baseline["complete_independent_mean_term_L2_upper"]);evidence=[]
    for i in (0,1):
        for name in FIRST+MEAN:
            key="density"+str(i)+"_"+name;target=terms if name in FIRST else means
            prior=target[key];candidate=up(weight*maxima[key])
            retained,improved=old.selected_total(prior,candidate);target[key]=retained
            evidence.append(dict(source_term=key,output="first" if name in FIRST else "independent_physical_mean",
                same_original_complete_row_count=6,complete_uniform_row_coefficient_upper=rec(maxima[key]),
                accepted_complete_L2_upper=prior,new_complete_L2_upper=rec(candidate),
                selected_complete_L2_upper=retained,strictly_smaller_complete_term=improved,
                complete_original_word_contains_all_inner_factors=True,
                radial_eta_inverse_and_background_u_mean_preserved=True,
                original_radial_integral_recomputed=False))
    gate("ten whole h source comparisons preserve both windows all original rows mean factors and twenty-one other terms",
        len(maxima)==len(evidence)==10 and len(terms)==21 and len(means)==10
        and all(v==terms[k] for k,v in baseline["complete_first_source_term_L2_upper"].items() if k not in CHANGED)
        and all(v==means[k] for k,v in baseline["complete_independent_mean_term_L2_upper"].items() if k not in CHANGED))
    return terms,means,evidence,details

def render(doc):
    lines=["# Actual exact normalized p columns and complete h-source bounds","",
        "Ten complete h-dependent terms are compared on the original six intersections.",
        "The saved p(w1V), full inverse gaps, directed whole words and radial integrals are read.",
        "This is an ordinary negative-source conclusion, not a high BVP inverse.","",
        "- Scientific child code: "+str(doc.get("actual_returncode")),
        "- Mathematical complete: "+str(doc.get("complete")),
        "- New complete ordered columns: "+str(doc.get("new_complete_ordered_p_columns",0)),
        "- New complete comparisons: "+str(doc.get("new_complete_uniform_comparisons",0)),
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
        lines+=["","## Complete normalized columns","",
            "| Column | Component | Derivative | Complete bound |","|---|---|---|---|"]
        c0=doc["complete_normalized_p_zero_conclusion"]["complete_normalized_p_zero_angular_derivative_upper"]
        c1=doc["complete_saved_p_one_conclusion"]["complete_saved_p_one_angular_derivative_upper"]
        for label,column in (("B_j p_j(w0)",c0),("p_j(w1V)",c1)):
            for i,row in enumerate(column):
                for k,v in enumerate(row):lines.append("| "+label+" | "+str(i)+" | "+str(k)+" | "+v["ball"]+" |")
        lines+=["","## Complete W = QG derivatives","",
            "| Angular order | Complete bound |","|---|---|"]
        for k,v in enumerate(doc["complete_normalized_p_zero_conclusion"]["complete_W_angular_derivative_upper"]):
            lines.append("| "+str(k)+" | "+v["ball"]+" |")
        lines+=["","## Complete 31-term ledger","","| First-row term | Complete L2 bound |","|---|---|"]
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
        "- Complete raw rows and new row arrays remain temporary.",
        "- All three local terms, the accepted SV/S1 improvements, and twenty-one other term balls remain unchanged.",
        "- Both original source windows, all physical means, the true dr measure, and the root band are retained.",
        "- No source-to-wave, positive growing-column, strong return, or high BVP inverse is asserted.",""]
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
        original_successful_small_receipts_read=0,original_complete_coefficient_rows_read=0,
        original_selected_coefficient_rows_read=0,original_positive_linear_coefficients_read=0,
        original_complete_source_terms_read=0,original_complete_word_maxima_read=0,
        original_complete_word_maxima_consumed=0,
        accepted_SV_coordinate_derivative_bounds_read=0,accepted_genuine_p_derivative_bounds_read=0,
        saved_complete_p_columns_read=0,new_complete_ordered_p_columns=0,
        new_complete_W_angular_bounds=0,new_complete_normalized_p_zero_angular_bounds=0,
        new_complete_global_window_evaluations=0,new_complete_row_mean_functionals=0,
        new_complete_positive_functional_evaluations=0,new_complete_source_row_budgets=0,
        new_complete_uniform_comparisons=0,new_complete_scalar_recombinations=0,
        old_numerical_enclosures_recomputed=0,
        old_target_FFT_intrinsic_repair_fold_transport_or_Taylor_recomputed=0,
        old_amplitude_derivatives_finite_sums_or_tails_recomputed=0,
        old_inverse_word_or_positive_calibration_recomputed=0,
        old_AJ_DG_RV_SV_ER_S1_or_companion_source_closures_called=0,
        old_source_row_or_radial_integral_recomputed=0,new_radial_integrals_computed=0,
        original_natural_stage_bytes_modified=0,full_physical_negative_volume_source_paid=False,
        full_high_inverse_claimed=False,reproducible_outputs_published_to_repository=False,
        reproducible_outputs_uploaded_to_Releases=False,new_reproducible_data_artifact_uploaded=False)
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
            original_AJ_algorithm=AJ_SOURCE,original_AJ_manifest=AJ_MANIFEST,accepted_AJ_execution=AJ_EXEC,
            original_RV_algorithm=RV_SOURCE,original_RV_manifest=RV_MANIFEST,accepted_RV_execution=RV_EXEC,
            original_DG_algorithm=DG_SOURCE,original_DG_manifest=DG_MANIFEST,accepted_DG_execution=DG_EXEC,
            original_SV_algorithm=SV_SOURCE,original_SV_manifest=SV_MANIFEST,accepted_SV_execution=SV_EXEC,
            original_ER_algorithm=ER_SOURCE,original_ER_manifest=ER_MANIFEST,accepted_ER_execution=ER_EXEC,
            original_S1_algorithm=S1_SOURCE,original_S1_manifest=S1_MANIFEST,accepted_S1_execution=S1_EXEC,
            complete_genuine_execution=old.C_EXEC,directed_source_execution=old.D_EXEC,
            original_norm_native=old.OLD_NATIVE,original_norm_process=old.OLD_PROCESS,
            directed_process="00afd54464db46f110ecff8c1968b158deedac719a363590fc366038b47fedb8")
        gate("all successful receipts original column and complete source algorithms retain their exact identities",
            all(sha(paths[k])==v for k,v in expected.items()))
        prior=read(paths["original_S1_manifest"])
        gate("all seventy-seven original S1 pins are unchanged in the new scientific closure",
            len(prior["files"])==77 and prior["scientific_source_sha256"]==S1_SOURCE
            and all(pins.get(e["path"])==e for e in prior["files"]))
        C=accepted(paths["complete_genuine_execution"],"43702688640",old.C_SOURCE,old.C_MANIFEST,old.C_EXEC,17,gate)
        D=accepted(paths["directed_source_execution"],"43703879926",old.D_SOURCE,old.D_MANIFEST,old.D_EXEC,12,gate)
        AJ=accepted(paths["accepted_AJ_execution"],"43718112378",AJ_SOURCE,AJ_MANIFEST,AJ_EXEC,29,gate)
        RV=accepted(paths["accepted_RV_execution"],"43719681982",RV_SOURCE,RV_MANIFEST,RV_EXEC,27,gate)
        DG=accepted(paths["accepted_DG_execution"],"43720766795",DG_SOURCE,DG_MANIFEST,DG_EXEC,27,gate)
        SV=accepted(paths["accepted_SV_execution"],"43722805762",SV_SOURCE,SV_MANIFEST,SV_EXEC,23,gate)
        ER=accepted(paths["accepted_ER_execution"],"43724065270",ER_SOURCE,ER_MANIFEST,ER_EXEC,20,gate)
        S1=accepted(paths["accepted_S1_execution"],"43724817779",S1_SOURCE,S1_MANIFEST,S1_EXEC,21,gate)
        doc["original_successful_small_receipts_read"]=8
        gate("the same genuine column domains original reflection and full physical mean are retained",
            C["scope"]["original_fixed_intrinsic_parameter"]=="eta_0"
            and C["scope"]["both_genuine_columns_and_both_carrier_signs"]
            and C["scope"]["all_input_abs_j_at_least97"]
            and C["scope"]["output_mean_and_complete_original_primitive_retained"]
            and C["scope"]["physical_J_only_on_its_proved_reflected_parity_domain"]
            and all(r["full_physical_negative_volume_source_paid"] and not r["full_high_inverse_claimed"]
                and r["old_numerical_enclosures_recomputed"]==0 for r in (AJ,RV,DG,SV,ER,S1))
            and DG["scope"]["all_three_local_terms_read_verbatim"]
            and DG["scope"]["density_zero_complete_source_read_verbatim"]
            and SV["scope"]["other_twenty_eight_complete_terms_read_verbatim"]
            and len(SV["complete_comparison_conclusions"])==3
            and {x["source_term"] for x in SV["complete_comparison_conclusions"]}
                =={"density0_complete_SV","density0_old_mean_V0","density0_complete_uJB_w"}
            and ER["complete_comparison_conclusion"]["source_term"]=="local_raw_1"
            and S1["scope"]["other_twenty_eight_complete_terms_read_verbatim"]
            and len(S1["complete_comparison_conclusions"])==3
            and {x["source_term"] for x in S1["complete_comparison_conclusions"]}
                =={"density1_complete_SV","density1_old_mean_V0","density1_complete_uJB_w"})
        base=S1["complete_source_conclusion"];erbase=ER["complete_source_conclusion"]
        svbase=SV["complete_source_conclusion"];dgbase=DG["complete_source_conclusion"]
        ajbase=AJ["complete_source_conclusion"]
        stable=("actual_dr_measure","exact_negative_physical_cover","one_sided_uncertain_root_band_retained",
            "both_density_windows_retained","outer_J_window","input_window","first_output_window",
            "independent_even_mean_window","total_squared_envelope_radial_weight_upper",
            "original_temporary_row_payload_sha256","old_nine_word_and_five_physical_mean_counts")
        gate("the successful S1 baseline retains the ER local improvement both SV updates and all original source windows",
            len(base["complete_first_source_term_L2_upper"])==21
            and len(base["complete_independent_mean_term_L2_upper"])==10
            and all(base[k]==erbase[k]==svbase[k]==dgbase[k]==ajbase[k] for k in stable)
            and all(erbase["complete_first_source_term_L2_upper"][k]==v
                for k,v in svbase["complete_first_source_term_L2_upper"].items() if k!="local_raw_1")
            and erbase["complete_independent_mean_term_L2_upper"]==svbase["complete_independent_mean_term_L2_upper"]
            and erbase["nonlocal_total_L2_upper"]==svbase["nonlocal_total_L2_upper"]
            and erbase["mean_L2_upper"]==svbase["mean_L2_upper"]
            and base["local_L2_upper"]==erbase["local_L2_upper"]
            and all(base["complete_first_source_term_L2_upper"][k]==v
                for k,v in erbase["complete_first_source_term_L2_upper"].items()
                if k not in ("density1_complete_SV","density1_old_mean_V0"))
            and all(base["complete_independent_mean_term_L2_upper"][k]==v
                for k,v in erbase["complete_independent_mean_term_L2_upper"].items() if k!="density1_complete_uJB_w")
            and base["exact_negative_physical_cover"]==[str(PIECE[0]),str(ROOTS[1])]
            and base["old_nine_word_and_five_physical_mean_counts"]==[9,5])
        zero,czero=normalized_p_zero_column(SV,DG,RV,AJ,gate)
        one,cone=saved_p_one_column(DG,RV,SV,gate)
        doc.update(accepted_SV_coordinate_derivative_bounds_read=15,accepted_genuine_p_derivative_bounds_read=6,
            saved_complete_p_columns_read=1,new_complete_ordered_p_columns=1,
            new_complete_W_angular_bounds=4,new_complete_normalized_p_zero_angular_bounds=8,
            complete_normalized_p_zero_conclusion=czero,complete_saved_p_one_conclusion=cone)
        rows,words=old.checked_accepted_rows(paths,C,D,AJ,gate)
        doc.update(original_complete_coefficient_rows_read=1328,original_selected_coefficient_rows_read=6,
            original_complete_word_maxima_read=8,original_complete_word_maxima_consumed=3,
            original_complete_source_terms_read=31)
        positive=old.read_positive_coefficients(C,gate);A=old.PositiveOperator(positive)
        doc["original_positive_linear_coefficients_read"]=18
        Gamma,Mean,operators=normalized_windows([zero,one],A,gate)
        terms,means,comparisons,row_details=complete_comparisons(
            rows,words,[zero,one],Gamma,Mean,A,base["total_squared_envelope_radial_weight_upper"],base,gate)
        result=old.combine(base,terms,means)
        doc.update(new_complete_global_window_evaluations=2,new_complete_row_mean_functionals=12,
            new_complete_positive_functional_evaluations=15,new_complete_source_row_budgets=6,
            new_complete_uniform_comparisons=10,new_complete_scalar_recombinations=4,
            complete_normalized_h_operator_conclusion=operators,
            complete_comparison_conclusions=comparisons,complete_source_conclusion=result,
            strictly_smaller_complete_term_bounds=sum(int(v["strictly_smaller_complete_term"]) for v in comparisons))
        gate("all twenty-one other complete term balls including every local and both accepted SV columns remain byte identical",
            result["local_L2_upper"]==base["local_L2_upper"]
            and all(result["complete_first_source_term_L2_upper"][k]==v
                for k,v in base["complete_first_source_term_L2_upper"].items() if k not in CHANGED)
            and all(result["complete_independent_mean_term_L2_upper"][k]==v
                for k,v in base["complete_independent_mean_term_L2_upper"].items() if k not in CHANGED)
            and sum(k not in CHANGED for k in terms)==15 and sum(k not in CHANGED for k in means)==6
            and result["total_squared_envelope_radial_weight_upper"]==base["total_squared_envelope_radial_weight_upper"]
            and result["original_temporary_row_payload_sha256"]==base["original_temporary_row_payload_sha256"])
        gate("the complete new ordinary negative volume source is finite in both original windows with independent physical mean",
            all(bound(result[k],k).is_finite() for k in
                ("local_L2_upper","nonlocal_total_L2_upper","first_L2_upper","mean_L2_upper","combined_L2_upper"))
            and result["actual_dr_measure"] and result["one_sided_uncertain_root_band_retained"]
            and result["both_density_windows_retained"] and result["old_nine_word_and_five_physical_mean_counts"]==[9,5])
        doc["scope"]=dict(original_physical_root_piece_2549_only=True,original_fixed_intrinsic_parameter="eta_0",
            same_original_real_explicit_family=True,
            original_positive_width_zero_order_moduli_and_saved_real_angle_jets_distinguished=True,
            complete_original_coefficient_delta_and_potential_z_domains_retained=True,
            independent_complex_frequency_inverse_claimed=False,
            final_column_operators_use_physical_input_labels=True,
            both_genuine_columns_and_both_carrier_signs=True,all_input_abs_j_at_least97=True,
            same_genuine_w1V_not_free_first_correction=True,
            exact_B_j_p_w0_product_before_absolute_majorants=True,
            leading_W_radial_part_and_cubic_quadratic_corrections_retained=True,
            saved_density_one_p_column_read_without_new_derivative_or_inverse=True,
            row_radial_eta_inverse_and_full_scalar_u_Leibniz_mean_retained=True,
            all_eighteen_positive_column_coefficients_summed=True,
            all_three_local_terms_and_both_accepted_SV_updates_read_verbatim=True,
            other_twenty_one_complete_terms_read_verbatim=True,
            full_amplitude_means_and_independent_physical_even_mean_retained=True,
            complete_original_primitive_and_both_directed_J_windows_retained=True,
            no_duplicate_wholeword_inner_factors=True,
            physical_J_only_on_its_proved_reflected_parity_domain=True,
            all_actual_physical_seams_and_reference_matching_sources_retained=True,
            original_positive_graph_and_outer_source_ports_retained=True,
            complete_row_arrays_published=False,physical_to_wave_readout_paid=False,
            full_negative_BVP_inverse_paid=False,positive_growing_column_operator_paid=False,
            cutoff97_strong_return_contraction_paid=False)
        temporary.update(complete_new_source_rows=row_details,
            accepted_positive_coefficients_payload_sha256=payload_sha(C["complete_positive_linear_operator_conclusion"]))
        doc["temporary_complete_source_row_payload_sha256"]=payload_sha(row_details)
        doc["temporary_complete_source_row_count"]=len(row_details)
        doc.update(complete=True,proved=True,actual_returncode=0,full_physical_negative_volume_source_paid=True)
    except BaseException as error:
        doc["failure"]=dict(type=type(error).__name__,message=str(error))
    finally:
        doc["actual_mathematical_wall_seconds"]=time.monotonic()-started
        temporary.update(kind=KIND,source_sha256=source,input_manifest_sha256=a.manifest_sha,complete_conclusions=doc)
        native=a.out_dir/"temporary-exact-normalized-p-columns-h-sources.json.gz"
        save(native,temporary,True)
        doc["temporary_native_sha256"]=sha(native);doc["temporary_native_bytes"]=native.stat().st_size
        doc["temporary_native_is_not_published"]=True;actual=doc["actual_returncode"]
        try:
            report=render(doc)
            raw=(json.dumps(doc,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
            if len(raw)>60000 or len(report.encode())>60000:raise ValueError("small conclusion or process exceeded60000 bytes")
            save(a.out_dir/"process.json",doc);(a.out_dir/"conclusion.md").write_text(report)
        except BaseException as error:
            small={k:v for k,v in doc.items() if k not in ("complete_normalized_p_zero_conclusion",
                "complete_saved_p_one_conclusion","complete_normalized_h_operator_conclusion",
                "complete_comparison_conclusions","complete_source_conclusion")}
            small["actual_scientific_returncode"]=actual
            small["formatting_failure"]=dict(type=type(error).__name__,message=str(error))
            small.update(complete=False,proved=False,actual_returncode=1)
            save(a.out_dir/"process.json",small)
            (a.out_dir/"conclusion.md").write_text("# Actual normalized-p source formatting failure\n\n"
                "Original scientific child code: "+str(actual)+". Formatting is separate from mathematics.\n"
                "Temporary native SHA256: "+doc["temporary_native_sha256"]+"\n")
            actual=1
        print(json.dumps(dict(complete=doc["complete"],actual_returncode=actual,
            new_complete_comparisons=doc["new_complete_uniform_comparisons"],
            old_numerical_enclosures_recomputed=0,new_radial_integrals_computed=0,
            reproducible_data_published=False)),flush=True)
    return actual
if __name__=="__main__":raise SystemExit(main())
