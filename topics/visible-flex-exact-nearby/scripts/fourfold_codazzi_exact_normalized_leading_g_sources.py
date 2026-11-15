#!/usr/bin/env python3
"""Exact inverse leading-transport column and five complete density-zero sources.

Saved W and normalized p columns are read unchanged. Only the new principal,
complete resolvent/rank angular bounds and five whole source terms are computed.
All original source rows, positive coefficients and radial integrals are read.
"""
from __future__ import annotations
import argparse,hashlib,json,math,os,platform,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy,scipy
from flint import arb,ctx
import fourfold_codazzi_factored_transport_companion_sources as old

PUBLIC,TOPIC,RUNTIME=old.PUBLIC,old.TOPIC,old.RUNTIME
KIND="actual_exact_normalized_leading_g_sources_v1"
CONTRACT="f634f95cd7fe17949995d7c6f50a27633e9061b156f5b882aab67bcded91acf3"
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
H,ROOTS,PIECE,RG,SG,N=old.H,old.ROOTS,old.PIECE,old.RG,old.SG,old.N
SB,HI=Q(1,64),Q(1,20000)
sha,ex,rb,up,gap,rec=old.sha,old.ex,old.rb,old.up,old.gap,old.rec
read,save,unpack,encode,payload_sha=old.read,old.save,old.unpack,old.encode,old.payload_sha
FIRST=("density0_complete_RQ_J_g","density0_complete_primitive","density0_old_mean_transported","density0_old_mean_vphi")
MEAN=("density0_complete_uJ_g",)

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
        complete_complex_z_square_halfwidth="1/9409",
        saved_W_derivative_orders=[0,1,2,3],saved_normalized_p_derivative_orders=[0,1,2,3],
        new_zeta_derivative_orders=[3],new_Bplus_derivative_orders=[1,2,3],
        new_normalized_g_derivative_orders=[0,1,2,3],
        exact_normalized_column="B_j*g_j(w0)",
        exact_principal_identity="(W/2)*(i*epsilon*(cT*Bplus+y^2),x*zeta-Bplus*Xi)",
        input_window="H^(-4/3), both genuine columns and both signs",
        density_window="H^(-8/3)",intermediate_word_window="H^(-5/3)",
        common_column_envelope="abs(rho)^(-1/4)",
        correction_input_weight="1/150544",additional_input_frequency_weight_inserted=False,
        changed_complete_terms=list(FIRST+MEAN),unchanged_complete_term_count=26,
        accepted_baseline_run="43726426053/1",original_radial_integrals_recomputed=0,
        accepted_W_p_column_or_fold_closures_recomputed=False,
        complete_positive_functional_evaluations=20,
        complete_mean_and_both_genuine_columns_retained=True)

def normalized_g_zero_column(SV,HP,RV,AJ,gate):
    """BG: exact B_V G0w0 first, then both complete q corrections."""
    v=SV["complete_exact_inverse_column_conclusion"]
    hp=HP["complete_normalized_p_zero_conclusion"]
    r=RV["complete_domain_conclusion"]
    aj=AJ["complete_AJ_angular_derivative_conclusion"]
    domain=AJ["complete_domain_conclusion"]
    h=ROOTS[1]-PIECE[0]
    gate("the saved normalized p column fold and connection jets have one identical complete physical product",
        Q(v["exact_negative_rho_cover"])==Q(hp["exact_negative_rho_cover"])==Q(r["exact_negative_rho_cover"])==h
        and Q(hp["exact_original_fold_radius"])==Q(v["exact_original_fold_radius"])==Q(aj["exact_original_fold_radius"])==RG
        and Q(hp["exact_original_fold_strip"])==Q(v["exact_original_fold_strip"])==Q(aj["exact_original_fold_strip"])==SG
        and Q(hp["exact_accepted_inverse_radius"])==Q(v["exact_accepted_inverse_radius"])==HI
        and Q(hp["exact_accepted_inverse_strip"])==Q(v["exact_accepted_inverse_strip"])==SB
        and 0<h<H<HI<RG and 0<SB<SG
        and hp["accepted_complete_determinant_gap"]==v["accepted_complete_determinant_gap"]
        and gap(r["accepted_complete_deformed_determinant_lower"],"accepted separately rounded RV determinant")>0
        and hp["accepted_complete_V_modulus"]==v["accepted_complete_V_modulus"]
        and hp["accepted_negative_T_image"]==r["new_complete_negative_T_image_upper"]
        and hp["accepted_SV_column_conclusion_sha256"]==payload_sha(v)
        and hp["accepted_RV_domain_conclusion_sha256"]==payload_sha(r)
        and hp["same_full_SG_zero_order_moduli_and_SB_inverse_used"]
        and Q(hp["W_zero_order_holomorphic_strip"])==SG
        and hp["W_positive_order_bounds_are_real_circle_derivatives"]
        and hp["no_real_circle_supremum_promoted_to_positive_strip"]
        and not hp["original_fold_inverse_or_image_closures_called"]
        and not hp["independent_complex_frequency_inverse_claimed"]
        and v["same_full_complex_delta_and_old_angle_domains_retained"]
        and v["potential_original_full_complex_z_modulus_read"]
        and domain["physical_T_image_definition_read_from_frozen_producer"]
        and aj["accepted_order_zero_domain_read_verbatim"]==domain
        and aj["exact_mu_identity"]=="Q^2*(x^2+T*y^2)"
        and gap(aj["complete_positive_Bplus_modulus"],"accepted principal Bplus gap")>0)
    rawX=v["complete_X_angular_derivative_upper"];rawY=v["complete_Y_angular_derivative_upper"]
    rawZ=v["complete_zeta_angular_derivative_upper"]
    rawW=hp["complete_W_angular_derivative_upper"]
    rawF=hp["complete_T_y_angular_derivative_upper"]
    rawP=hp["complete_normalized_p_zero_angular_derivative_upper"]
    rawC=aj["complete_cT_angular_derivative_upper"]
    rawXi=aj["complete_Xi_angular_derivative_upper"]
    gate("the complete saved coordinate connection and normalized p derivative arrays are read without regeneration",
        len(rawX)==len(rawY)==len(rawW)==len(rawF)==len(rawC)==len(rawXi)==4
        and len(rawZ)==3 and len(rawP)==2 and all(len(row)==4 for row in rawP)
        and hp["exact_column"]=="B_j*p_j(w0)"
        and hp["physical_input_n_minus_two_prefactor_paid_once"]
        and hp["full_radial_W_and_all_output_means_retained"]
        and v["full_radial_G_and_all_output_means_retained"]
        and r["accepted_AJ_connection_angular_jets_read_without_recomputation"])
    X=[bound(a,"saved complete X derivative") for a in rawX]
    Y=[bound(a,"saved complete Y derivative") for a in rawY]
    W=[bound(a,"saved complete QG derivative") for a in rawW]
    F=[bound(a,"saved complete Ty derivative") for a in rawF]
    Z=[bound(a,"saved complete zeta derivative") for a in rawZ]
    Z.append(up(6*Z[0]/ex(SG**3)))
    C=[bound(a,"saved complete cT derivative") for a in rawC]
    Xi=[bound(a,"saved complete Xi derivative") for a in rawXi]
    XiH=bound(domain["complete_Xi_holomorphic_upper"],"saved complete full-SG Xi modulus")
    T=bound(hp["accepted_negative_T_image"],"saved complete full-SG T image")
    V=bound(hp["accepted_complete_V_modulus"],"saved complete V modulus")
    Delta=gap(hp["accepted_complete_determinant_gap"],"saved complete physical-label determinant gap")
    Bp=[bound(hp["complete_Bplus_modulus_upper"],"saved complete Bplus modulus")]
    for k in range(1,4):
        Bp.append(up(sum((math.comb(k,l)*(X[l]*X[k-l]+F[l]*Y[k-l])
            for l in range(k+1)),arb(0))))
    y2=old.mul(Y,Y,3)
    ctB=old.mul(C,Bp,3)
    xz=old.mul(X,Z,3);bxi=old.mul(Bp,Xi,3)
    first=[up(ctB[k]+y2[k]) for k in range(4)]
    second=[up(xz[k]+bxi[k]) for k in range(4)]
    principal=[[up(a/2) for a in old.mul(W,first,3)],
        [up(a/2) for a in old.mul(W,second,3)]]
    tbH=up(W[0]*(X[0]*Z[0]+Bp[0]*XiH)/2)
    q=ex(Q(1,N*N))
    coefficient=up(V*Y[0]/Delta)
    Ccorr=[up(coefficient*X[0]*tbH),up(coefficient*Y[0]*tbH)]
    Rfactor=up(W[0]*V*Bp[0]/Delta)
    Rhol=[up(Rfactor*X[0]*Y[0]),up(Rfactor*Y[0]**2)]
    Bhol=[[up(X[0]/Delta),up((T+q*V)*Y[0]/Delta)],
        [up(Y[0]/Delta),up(X[0]/Delta)]]
    BR=[up(sum((Bhol[i][j]*Rhol[j] for j in range(2)),arb(0))) for i in range(2)]
    correction0=[[up(math.factorial(k)*Ccorr[i]/ex(SB**k)) for k in range(4)] for i in range(2)]
    correction1=[[up(ex(Q(math.factorial(k+2),2))*BR[i]/ex(SB**(k+1)))
        for k in range(4)] for i in range(2)]
    column=[[up(principal[i][k]+q*(correction0[i][k]+correction1[i][k]))
        for k in range(4)] for i in range(2)]
    pcolumn=[[bound(a,"saved complete B_j p(w0) derivative") for a in row] for row in rawP]
    gate("the new normalized g column keeps the radial principal part both rank corrections and their full ordered Leibniz factors",
        all(a.is_finite() and a.lower()>=0 for rows in (principal,correction0,correction1,column,pcolumn)
            for row in rows for a in row)
        and all(a.is_finite() and a.lower()>=0 for a in Z+Bp+Ccorr+Rhol+BR)
        and Delta>0 and N==388)
    return column,pcolumn,dict(
        exact_negative_rho_cover=str(h),exact_original_fold_radius=str(RG),
        exact_original_fold_strip=str(SG),exact_accepted_inverse_radius=str(HI),
        exact_accepted_inverse_strip=str(SB),exact_normalized_g_column="B_j*g_j(w0)",
        exact_principal_identity="(W/2)*(i*epsilon*(cT*Bplus+y^2),x*zeta-Bplus*Xi)",
        exact_correction_identity="n^-2*(V*y/Delta*(-i*epsilon*x,y)^t*t_b+B_j*partial_phi R0)",
        exact_R0_identity="-W*V*Bplus/Delta*(x*y,i*epsilon*y^2)",
        complete_new_zeta_third_derivative_upper=rec(Z[3]),
        complete_Bplus_angular_derivative_upper=encode(Bp),
        accepted_complete_W_angular_derivative_upper=rawW,
        accepted_complete_normalized_p_zero_angular_derivative_upper=rawP,
        complete_principal_normalized_g_angular_derivative_upper=encode(principal),
        complete_principal_second_component_holomorphic_upper=rec(tbH),
        complete_unweighted_first_correction_modulus_upper=encode(Ccorr),
        complete_R0_holomorphic_modulus_upper=encode(Rhol),
        complete_Bj_holomorphic_entry_modulus_upper=encode(Bhol),
        complete_unweighted_second_correction_modulus_product_upper=encode(BR),
        complete_first_rank_correction_angular_derivative_upper=encode(correction0),
        complete_second_rank_correction_angular_derivative_upper=encode(correction1),
        complete_normalized_g_zero_angular_derivative_upper=encode(column),
        accepted_principal_Bplus_modulus_lower=aj["complete_positive_Bplus_modulus"],
        accepted_complete_V_modulus=hp["accepted_complete_V_modulus"],
        accepted_complete_determinant_gap=hp["accepted_complete_determinant_gap"],
        accepted_HP_normalized_p_zero_conclusion_sha256=payload_sha(hp),
        accepted_SV_column_conclusion_sha256=payload_sha(v),
        accepted_AJ_connection_conclusion_sha256=payload_sha(aj),
        accepted_RV_domain_conclusion_sha256=payload_sha(r),
        new_zeta_third_derivative_is_Cauchy_from_full_SG_modulus=True,
        only_new_Bplus_derivatives_one_through_three_computed=True,
        new_second_rank_Cauchy_factor="(k+2)!/(2*SB^(k+1))",
        saved_W_Bplus_zero_and_normalized_p_closures_recomputed=False,
        physical_input_n_minus_two_prefactor_paid_once=True,
        reaction_vartheta_not_inserted_in_transport_rank=True,
        full_radial_principal_and_all_means_retained=True,
        independent_complex_frequency_inverse_claimed=False)

def normalized_zero_window(column,A):
    if len(column)!=2 or any(len(row)!=4 for row in column):
        raise ValueError("the normalized leading source requires both complete four-jet columns")
    ordinary=A(column);mean=A([row[1:] for row in column])
    return up(ordinary+mean),up(mean)

def complete_g_zero_comparisons(rows,words,column,pcolumn,A,W2,baseline,gate):
    """Same complete five density-zero terms; no generic inverse norm is reinserted."""
    if len(rows)!=6:raise ValueError("the complete source requires all six original rows")
    weight=bound(W2,"accepted complete squared-envelope radial weight").sqrt().upper()
    KR=bound(words["C_RQJ_directed"],"accepted complete RQJ word")
    KP=bound(words["C_primitive_directed"],"accepted complete primitive word")
    KU=bound(words["C_uJ_directed"],"accepted complete independent-mean uJ word")
    Gg,Mg=normalized_zero_window(column,A)
    maxima={};details=[]
    for row in rows:
        c=unpack(row["bounds"])
        V=[bound(a,"complete original physical v derivative") for a in c["V"]]
        if len(V)<5:raise ValueError("the complete physical background lacks its fourth derivative")
        J=bound(c["C_J_scalar"],"original complete outer scalar J")
        cb=bound(c["cB"],"original complete mean prefactor")
        mt=bound(c["m0_T0"],"original complete transported mean")
        ef=bound(c["exact_nonlocal_even_mean_row_factor"],"original independent physical mean factor")
        y=old.pair_mul(V,pcolumn,3)
        q=old.pair_add(old.pair_mul(V,column,3),old.pair_mul(V[1:],pcolumn,3),3)
        Gq,Mq=normalized_zero_window(q,A);My=up(A([v[1:] for v in y]))
        primitive_mean=up(cb*V[1]*V[0]*Mg/4)
        T0_mean=up(mt*Mg)
        values=dict(density0_complete_RQ_J_g=up(J*KR*Gg),
            density0_complete_primitive=up(J*KP*Gq),
            density0_old_mean_transported=up(J*(primitive_mean+T0_mean)),
            density0_old_mean_vphi=up(J*cb*V[1]*My),
            density0_complete_uJ_g=up(ef*KU*Gg))
        if any(not a.is_finite() or a.lower()<0 for a in values.values()):
            raise ValueError("invalid complete new normalized g source coefficient")
        for name,value in values.items():
            maxima[name]=value if name not in maxima else max(maxima[name],value).upper()
        details.append(dict(common_row=row["common_row"],exact_original_interval=row["interval"],
            exact_original_row_payload_sha256=payload_sha(row),
            complete_coefficients=encode(values),
            complete_window_operators=encode(dict(Gamma_g=Gg,M_g=Mg,Gamma_q=Gq,M_q=Mq,
                M_y=My,primitive_mean_before_outer_J=primitive_mean,
                transported_mean_before_outer_J=T0_mean)),
            normalized_q_complete_angular_derivative_upper=encode(q),
            normalized_y_complete_angular_derivative_upper=encode(y)))
    terms=dict(baseline["complete_first_source_term_L2_upper"])
    means=dict(baseline["complete_independent_mean_term_L2_upper"]);evidence=[]
    for name in FIRST+MEAN:
        target=terms if name in FIRST else means
        prior=target[name];candidate=up(weight*maxima[name])
        retained,improved=old.selected_total(prior,candidate);target[name]=retained
        evidence.append(dict(source_term=name,output="first" if name in FIRST else "independent_physical_mean",
            same_original_complete_row_count=6,complete_uniform_row_coefficient_upper=rec(maxima[name]),
            accepted_complete_L2_upper=prior,new_complete_L2_upper=rec(candidate),
            selected_complete_L2_upper=retained,strictly_smaller_complete_term=improved,
            complete_original_word_contains_all_inner_factors=True,
            generic_inverse_norm_reinserted=False,additional_input_frequency_weight_inserted=False,
            original_radial_integral_recomputed=False))
    gate("five complete leading g source comparisons preserve both original windows every mean and all twenty-six other terms",
        len(maxima)==len(evidence)==5 and len(terms)==21 and len(means)==10
        and all(v==terms[k] for k,v in baseline["complete_first_source_term_L2_upper"].items() if k not in FIRST)
        and all(v==means[k] for k,v in baseline["complete_independent_mean_term_L2_upper"].items() if k not in MEAN))
    return terms,means,evidence,dict(
        density=0,exact_column="B_j*g_j(w0)",Gamma_g=rec(Gg),M_g=rec(Mg),
        exact_density_zero_functionals="Gamma=A(Z)+A(partial_phi Z), M=A(partial_phi Z)",
        complete_g_q_y_positive_functional_evaluations=20,
        all_eighteen_positive_coefficients_summed=True,
        complete_physical_mean_and_two_genuine_columns_retained=True,
        q_identity="v*(B_j*g)-v_phi*(B_j*p)",y_identity="v*(B_j*p)",
        original_physical_input_label_and_order_retained=True,
        generic_inverse_norm_reinserted=False),details

def render(doc):
    lines=["# Actual exact normalized leading-g source comparison","",
        "Five complete density-zero source terms are compared on the original six-row physical cover.",
        "The complete current normalized-p ledger, radial integrals and all other twenty-six terms are read.","",
        "- Scientific child code: "+str(doc.get("actual_returncode")),
        "- Mathematical complete: "+str(doc.get("complete")),
        "- New complete comparisons: "+str(doc.get("new_complete_uniform_comparisons",0)),
        "- Old numerical enclosures recomputed: 0","- New radial integrals: 0",""]
    if doc.get("failure"):lines+=["## Actual failure","",json.dumps(doc["failure"],ensure_ascii=False),""]
    result=doc.get("complete_source_conclusion")
    if result:
        lines+=["## Complete ordinary source bounds","","| Quantity | Complete bound |","|---|---|"]
        for k in ("local_L2_upper","nonlocal_total_L2_upper","first_L2_upper","mean_L2_upper","combined_L2_upper"):
            lines.append("| "+k+" | "+result[k]["ball"]+" |")
        lines+=["","## Five complete comparisons","",
            "| Term | Accepted | New | Retained | Improved |","|---|---|---|---|---|"]
        for row in doc["complete_comparison_conclusions"]:
            lines.append("| "+row["source_term"]+" | "+row["accepted_complete_L2_upper"]["ball"]
                +" | "+row["new_complete_L2_upper"]["ball"]+" | "+row["selected_complete_L2_upper"]["ball"]
                +" | "+str(row["strictly_smaller_complete_term"])+" |")
        lines+=["","## Complete31-term ledger","","| First-row term | Complete L2 bound |","|---|---|"]
        for k,v in result["complete_first_source_term_L2_upper"].items():
            lines.append("| "+k+" | "+v["ball"]+" |")
        lines+=["","| Independent physical mean term | Complete L2 bound |","|---|---|"]
        for k,v in result["complete_independent_mean_term_L2_upper"].items():
            lines.append("| "+k+" | "+v["ball"]+" |")
    normalized=doc.get("complete_normalized_g_zero_conclusion")
    if normalized:
        lines+=["","## Complete new normalized leading-g derivatives","",
            "| Component | Angular order | Complete bound |","|---|---|---|"]
        for i,row in enumerate(normalized["complete_normalized_g_zero_angular_derivative_upper"]):
            for k,v in enumerate(row):lines.append("| "+str(i)+" | "+str(k)+" | "+v["ball"]+" |")
        lines+=["","The single new zeta third derivative is "+normalized["complete_new_zeta_third_derivative_upper"]["ball"]+".",
            "The saved W, Bplus zero order and normalized p column are not recomputed.",""]
    lines+=["## Actual gate record","","| Gate | Passed |","|---|---|"]
    for g in doc.get("gates",[]):lines.append("| "+g["name"].replace("|","/")+" | "+str(g["passed"])+" |")
    lines+=["","## Scope","",
        "The complete physical negative-piece volume source retains both genuine branches, both carrier signs,",
        "the independent physical even mean, the original two primitive windows and actual radial measure.",
        "No source-to-wave, positive growing-column, strong return or full high BVP inverse is claimed.",
        "New reproducible arrays remain temporary. The successful old targets, coefficients and integrals are not rerun.",""]
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
        original_complete_word_maxima_consumed=0,accepted_W_derivative_bounds_read=0,
        accepted_normalized_p_derivative_bounds_read=0,accepted_Bplus_zero_moduli_read=0,
        new_zeta_third_derivative_bounds=0,new_Bplus_positive_derivative_bounds=0,
        new_complete_normalized_g_columns=0,new_complete_normalized_g_derivative_bounds=0,
        new_complete_global_window_evaluations=0,new_complete_row_positive_functionals=0,
        new_complete_positive_functional_evaluations=0,new_complete_source_row_budgets=0,
        new_complete_uniform_comparisons=0,new_complete_scalar_recombinations=0,
        old_numerical_enclosures_recomputed=0,
        old_target_FFT_intrinsic_repair_fold_transport_or_Taylor_recomputed=0,
        old_amplitude_derivatives_finite_sums_or_tails_recomputed=0,
        old_inverse_word_or_positive_calibration_recomputed=0,
        old_W_recurrence_Bplus_zero_or_normalized_p_columns_recomputed=0,
        old_AJ_DG_RV_SV_ER_S1_HP_or_companion_source_closures_called=0,
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
            original_HP_algorithm=HP_SOURCE,original_HP_manifest=HP_MANIFEST,accepted_HP_execution=HP_EXEC,
            complete_genuine_execution=old.C_EXEC,directed_source_execution=old.D_EXEC,
            original_norm_native=old.OLD_NATIVE,original_norm_process=old.OLD_PROCESS,
            directed_process="00afd54464db46f110ecff8c1968b158deedac719a363590fc366038b47fedb8")
        gate("all successful receipts original column and complete source algorithms retain their exact identities",
            all(sha(paths[k])==v for k,v in expected.items()))
        prior=read(paths["original_HP_manifest"])
        gate("all eighty-two original HP pins are unchanged in the new scientific closure",
            len(prior["files"])==82 and prior["scientific_source_sha256"]==HP_SOURCE
            and all(pins.get(e["path"])==e for e in prior["files"]))
        C=accepted(paths["complete_genuine_execution"],"43702688640",old.C_SOURCE,old.C_MANIFEST,old.C_EXEC,17,gate)
        D=accepted(paths["directed_source_execution"],"43703879926",old.D_SOURCE,old.D_MANIFEST,old.D_EXEC,12,gate)
        AJ=accepted(paths["accepted_AJ_execution"],"43718112378",AJ_SOURCE,AJ_MANIFEST,AJ_EXEC,29,gate)
        RV=accepted(paths["accepted_RV_execution"],"43719681982",RV_SOURCE,RV_MANIFEST,RV_EXEC,27,gate)
        DG=accepted(paths["accepted_DG_execution"],"43720766795",DG_SOURCE,DG_MANIFEST,DG_EXEC,27,gate)
        SV=accepted(paths["accepted_SV_execution"],"43722805762",SV_SOURCE,SV_MANIFEST,SV_EXEC,23,gate)
        ER=accepted(paths["accepted_ER_execution"],"43724065270",ER_SOURCE,ER_MANIFEST,ER_EXEC,20,gate)
        S1=accepted(paths["accepted_S1_execution"],"43724817779",S1_SOURCE,S1_MANIFEST,S1_EXEC,21,gate)
        HP=accepted(paths["accepted_HP_execution"],"43726426053",HP_SOURCE,HP_MANIFEST,HP_EXEC,25,gate)
        doc["original_successful_small_receipts_read"]=9
        hp_changed={"density"+str(i)+"_"+n for i in (0,1)
            for n in ("complete_SQ","complete_RQ_JL_h","old_mean_rQ","complete_uJL_h","complete_u_h")}
        gate("the same genuine column domains original reflection and full physical mean are retained",
            C["scope"]["original_fixed_intrinsic_parameter"]=="eta_0"
            and C["scope"]["both_genuine_columns_and_both_carrier_signs"]
            and C["scope"]["all_input_abs_j_at_least97"]
            and C["scope"]["output_mean_and_complete_original_primitive_retained"]
            and C["scope"]["physical_J_only_on_its_proved_reflected_parity_domain"]
            and all(r["full_physical_negative_volume_source_paid"] and not r["full_high_inverse_claimed"]
                and r["old_numerical_enclosures_recomputed"]==0 for r in (AJ,RV,DG,SV,ER,S1,HP))
            and DG["scope"]["all_three_local_terms_read_verbatim"]
            and DG["scope"]["density_zero_complete_source_read_verbatim"]
            and SV["scope"]["other_twenty_eight_complete_terms_read_verbatim"]
            and ER["complete_comparison_conclusion"]["source_term"]=="local_raw_1"
            and S1["scope"]["other_twenty_eight_complete_terms_read_verbatim"]
            and HP["scope"]["other_twenty_one_complete_terms_read_verbatim"]
            and HP["scope"]["row_radial_eta_inverse_and_full_scalar_u_Leibniz_mean_retained"]
            and {x["source_term"] for x in HP["complete_comparison_conclusions"]}==hp_changed
            and len(HP["complete_comparison_conclusions"])==10)
        base=HP["complete_source_conclusion"];s1base=S1["complete_source_conclusion"]
        erbase=ER["complete_source_conclusion"];svbase=SV["complete_source_conclusion"]
        dgbase=DG["complete_source_conclusion"];ajbase=AJ["complete_source_conclusion"]
        stable=("actual_dr_measure","exact_negative_physical_cover","one_sided_uncertain_root_band_retained",
            "both_density_windows_retained","outer_J_window","input_window","first_output_window",
            "independent_even_mean_window","total_squared_envelope_radial_weight_upper",
            "original_temporary_row_payload_sha256","old_nine_word_and_five_physical_mean_counts")
        gate("the successful HP baseline retains the complete S1 ER SV updates and every unchanged source window",
            len(base["complete_first_source_term_L2_upper"])==21
            and len(base["complete_independent_mean_term_L2_upper"])==10
            and all(base[k]==s1base[k]==erbase[k]==svbase[k]==dgbase[k]==ajbase[k] for k in stable)
            and all(erbase["complete_first_source_term_L2_upper"][k]==v
                for k,v in svbase["complete_first_source_term_L2_upper"].items() if k!="local_raw_1")
            and erbase["complete_independent_mean_term_L2_upper"]==svbase["complete_independent_mean_term_L2_upper"]
            and all(s1base["complete_first_source_term_L2_upper"][k]==v
                for k,v in erbase["complete_first_source_term_L2_upper"].items()
                if k not in ("density1_complete_SV","density1_old_mean_V0"))
            and all(s1base["complete_independent_mean_term_L2_upper"][k]==v
                for k,v in erbase["complete_independent_mean_term_L2_upper"].items() if k!="density1_complete_uJB_w")
            and all(base["complete_first_source_term_L2_upper"][k]==v
                for k,v in s1base["complete_first_source_term_L2_upper"].items() if k not in hp_changed)
            and all(base["complete_independent_mean_term_L2_upper"][k]==v
                for k,v in s1base["complete_independent_mean_term_L2_upper"].items() if k not in hp_changed)
            and base["local_L2_upper"]==s1base["local_L2_upper"]==erbase["local_L2_upper"]
            and base["exact_negative_physical_cover"]==[str(PIECE[0]),str(ROOTS[1])]
            and base["old_nine_word_and_five_physical_mean_counts"]==[9,5])
        column,pcolumn,conclusion=normalized_g_zero_column(SV,HP,RV,AJ,gate)
        doc.update(accepted_W_derivative_bounds_read=4,accepted_normalized_p_derivative_bounds_read=8,
            accepted_Bplus_zero_moduli_read=1,new_zeta_third_derivative_bounds=1,
            new_Bplus_positive_derivative_bounds=3,new_complete_normalized_g_columns=1,
            new_complete_normalized_g_derivative_bounds=8,complete_normalized_g_zero_conclusion=conclusion)
        rows,words=old.checked_accepted_rows(paths,C,D,AJ,gate)
        doc.update(original_complete_coefficient_rows_read=1328,original_selected_coefficient_rows_read=6,
            original_complete_word_maxima_read=8,original_complete_word_maxima_consumed=3,
            original_complete_source_terms_read=31)
        positive=old.read_positive_coefficients(C,gate);A=old.PositiveOperator(positive)
        doc["original_positive_linear_coefficients_read"]=18
        terms,means,comparisons,operators,row_details=complete_g_zero_comparisons(
            rows,words,column,pcolumn,A,base["total_squared_envelope_radial_weight_upper"],base,gate)
        result=old.combine(base,terms,means)
        doc.update(new_complete_global_window_evaluations=1,new_complete_row_positive_functionals=18,
            new_complete_positive_functional_evaluations=20,new_complete_source_row_budgets=6,
            new_complete_uniform_comparisons=5,new_complete_scalar_recombinations=4,
            complete_normalized_g_operator_conclusion=operators,
            complete_comparison_conclusions=comparisons,complete_source_conclusion=result,
            strictly_smaller_complete_term_bounds=sum(int(v["strictly_smaller_complete_term"]) for v in comparisons))
        changed=set(FIRST+MEAN)
        gate("all twenty-six other complete term balls including all local density-one and accepted h terms remain byte identical",
            result["local_L2_upper"]==base["local_L2_upper"]
            and all(result["complete_first_source_term_L2_upper"][k]==v
                for k,v in base["complete_first_source_term_L2_upper"].items() if k not in changed)
            and all(result["complete_independent_mean_term_L2_upper"][k]==v
                for k,v in base["complete_independent_mean_term_L2_upper"].items() if k not in changed)
            and sum(k not in changed for k in terms)==17 and sum(k not in changed for k in means)==9
            and result["total_squared_envelope_radial_weight_upper"]==base["total_squared_envelope_radial_weight_upper"]
            and result["original_temporary_row_payload_sha256"]==base["original_temporary_row_payload_sha256"])
        gate("the complete new ordinary negative volume source is finite in both original windows with independent physical mean",
            all(bound(result[k],k).is_finite() for k in
                ("local_L2_upper","nonlocal_total_L2_upper","first_L2_upper","mean_L2_upper","combined_L2_upper"))
            and result["actual_dr_measure"] and result["one_sided_uncertain_root_band_retained"]
            and result["both_density_windows_retained"] and result["old_nine_word_and_five_physical_mean_counts"]==[9,5])
        doc["scope"]=dict(original_physical_root_piece_2549_only=True,original_fixed_intrinsic_parameter="eta_0",
            same_original_real_explicit_family=True,
            complete_original_coefficient_delta_and_z_domains_retained=True,
            final_column_operators_use_physical_input_labels=True,
            both_genuine_columns_and_both_carrier_signs=True,all_input_abs_j_at_least97=True,
            exact_signed_principal_inverse_cancellation_before_majorants=True,
            complete_resolvent_and_derivative_rank_terms_retained=True,
            physical_input_n_minus_two_prefactor_paid_once=True,
            reaction_vartheta_not_inserted_in_transport_rank=True,
            holomorphic_Xi_modulus_not_replaced_by_real_circle_value=True,
            positive_order_saved_jets_not_promoted_to_holomorphic_strip=True,
            complete_saved_W_Bplus_zero_and_normalized_p_columns_read_verbatim=True,
            generic_inverse_norm_not_reinserted_after_normalization=True,
            full_radial_principal_and_amplitude_means_retained=True,
            all_twenty_positive_functional_calls_complete=True,
            all_three_local_terms_and_all_density_one_terms_read_verbatim=True,
            all_ten_HP_h_source_terms_read_verbatim=True,
            other_twenty_six_complete_terms_read_verbatim=True,
            full_physical_even_mean_and_both_transported_mean_parts_retained=True,
            complete_original_primitive_and_both_directed_J_windows_retained=True,
            no_duplicate_wholeword_inner_factors=True,
            physical_J_only_on_its_proved_reflected_parity_domain=True,
            all_actual_physical_seams_and_reference_matching_sources_retained=True,
            original_positive_graph_and_outer_source_ports_retained=True,
            complete_row_and_derivative_arrays_published=False,physical_to_wave_readout_paid=False,
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
        native=a.out_dir/"temporary-exact-normalized-leading-g-sources.json.gz"
        save(native,temporary,True)
        doc["temporary_native_sha256"]=sha(native);doc["temporary_native_bytes"]=native.stat().st_size
        doc["temporary_native_is_not_published"]=True;actual=doc["actual_returncode"]
        try:
            report=render(doc)
            raw=(json.dumps(doc,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
            if len(raw)>60000 or len(report.encode())>60000:raise ValueError("small conclusion or process exceeded60000 bytes")
            save(a.out_dir/"process.json",doc);(a.out_dir/"conclusion.md").write_text(report)
        except BaseException as error:
            small={k:v for k,v in doc.items() if k not in ("complete_normalized_g_zero_conclusion",
                "complete_normalized_g_operator_conclusion","complete_comparison_conclusions","complete_source_conclusion")}
            small["actual_scientific_returncode"]=actual
            small["formatting_failure"]=dict(type=type(error).__name__,message=str(error))
            small.update(complete=False,proved=False,actual_returncode=1)
            save(a.out_dir/"process.json",small)
            (a.out_dir/"conclusion.md").write_text("# Actual normalized leading-g source formatting failure\n\n"
                "Original scientific child code: "+str(actual)+". Formatting is separate from mathematics.\n"
                "Temporary native SHA256: "+doc["temporary_native_sha256"]+"\n")
            actual=1
        print(json.dumps(dict(complete=doc["complete"],actual_returncode=actual,
            new_complete_comparisons=doc["new_complete_uniform_comparisons"],
            old_numerical_enclosures_recomputed=0,new_radial_integrals_computed=0,
            reproducible_data_published=False)),flush=True)
    return actual
if __name__=="__main__":raise SystemExit(main())
