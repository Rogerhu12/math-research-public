#!/usr/bin/env python3
"""New complete physical density1 transport from seven new genuine a1 budgets.

Read the seven successful RV b1 bounds, original W totals, B product, fold,
inverse certificate, all18 positive coefficients, complete words and true
six-row radial measure. No accepted producer or original numerical enclosure
is reevaluated. All new arrays remain temporary in public Actions.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,math,os,platform,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy,scipy
from flint import arb,ctx
import fourfold_codazzi_factored_transport_companion_sources as old

PUBLIC,TOPIC,RUNTIME=old.PUBLIC,old.TOPIC,old.RUNTIME
KIND="actual_direct_physical_genuine_first_transport_v1"
CONTRACT="2b9f1a14e3fc223d850f4468442f3b4ca41c8208aad2fe8e5c0e5e3f0090c934"
FACTORED_SOURCE="a705c2b4c64393e3ba1ae1e043d0fbd62f516a7a80e03e47ce11820626373ee7"
AJ_SOURCE="32c45b335639a48b0d32541d03924246023e5e3f19deec1bcd8cf0549e955f03"
AJ_MANIFEST="871240a7a97011d837025aad7f9ca1707d69c17b6dec3c1f510f6415c278b74d"
AJ_EXEC="58462f96a486dede07873c4fc6aade100539f9f28ef49b49567a4acf7c2e8706"
W_SOURCE="a0f12f84d55c4735507e71e40d35cd343777d00dad4b5ec5c2e73804230198be"
W_MANIFEST="11e993bae75adf3a667ba7f7d8c28f9fb38f3fde8d12e34df938c82baef2ea65"
W_EXEC="777e681b85beb3317853d05d1c39a35703133a7cd49c81286571d21a89fa5dd1"
RV_RUN="43719681982"
RV_SOURCE="d59893af66b8829d924d75686fb0ecd6e6d25f9b72b70a0fac6564c4e96fdf60"
RV_MANIFEST="4718b4b818ec5d72537aa3a93e5825747a586ece87a086c7578ec6ec4c3b9ded"
RV_EXEC="0781239c0753785d2b196b77cc90c0eb343d52cc73226d84d7f8f6bb23136473"
H,ROOTS,PIECE,RG,SG,SB,N=old.H,old.ROOTS,old.PIECE,old.RG,old.SG,old.SB,old.N
R0=Q(1,6000);RA=Q(3,40000);SIGMA0=Q(1,128);RS=Q(1,8000);SS=Q(3,512)
sha,ex,rb,up,gap,rec=old.sha,old.ex,old.rb,old.up,old.gap,old.rec
read,save,unpack,encode,payload_sha=old.read,old.save,old.unpack,old.encode,old.payload_sha
add,scale,mul,product,cauchy=old.add,old.scale,old.mul,old.product,old.cauchy
def bound(v,label="complete upper"):return old.bound(v,label)

def accepted(path,run,source,manifest,digest,ngates,gate):
    if sha(path)!=digest:raise ValueError("accepted execution bytes changed")
    r=old.receipt(path,run,source,manifest,gate)
    if len(r["gates"])!=ngates:raise ValueError("accepted mathematical gate count changed")
    return r

def lower(v,label="positive budget number"):
    v=rb(v).lower()
    if not v.is_finite() or v<0:raise ValueError("invalid nonnegative lower "+label)
    return v

def radial_tail_number(M,R,h,p):
    if p not in (0,1) or not 0<h<R:raise ValueError("the complete radial tail left its fixed product")
    t=ex(h/R);d=1-t;gap(d,"complete radial tail")
    kernel=t**13/d if p==0 else t**12*(13/d+t/(d*d))
    return rb(M)*ex(R**(-p))*kernel

def fourier_tail_number(width,q):
    if not Q(width)>0 or q not in (0,1,2,3):raise ValueError("complete Fourier tail order")
    v=(-4*ex(width)).exp();d=1-v;gap(d,"complete Fourier tail")
    if q==0:return (1+v)/d
    if q==1:return 8*v/d**2
    if q==2:return 32*v*(1+v)/d**3
    return 128*v*(1+4*v+v*v)/d**4

def genuine_component_jets(W,B,RV,h,gate):
    """DG1--9: seven new a1 bounds; the seven complete RV b1 bounds only read."""
    cases=[v for v in W["cases"] if Q(v["exact_output_old_phi_width"])==0]
    if len(cases)!=1:raise ValueError("the original real Taylor case is not unique")
    case=cases[0];fields=[v for v in case["fields"] if v["field"]=="a1"]
    if len(fields)!=1:raise ValueError("the genuine a1 field changed")
    field=fields[0];tail=W["complete_tail_conclusion"]
    rows={r["radial_derivative_order"]:r for r in field["complete_mixed_derivative_rows"]}
    gate("the saved a1 totals are the same genuine first correction with signed finite sums complete tails and root normalization",
        case["complete"] and case["proved"] and Q(case["exact_whole_piece_cover_radius"])==H
        and Q(field["exact_output_old_phi_width"])==0
        and field["finite_signed_addition_precedes_modulus_and_sum"]
        and field["joint_sum_of_radial_coefficient_suprema"] and field["full_output_zero_mode_retained"]
        and field["amplitude_mean_is_not_independent_physical_even_mean"]
        and Q(field["old_tail_radius"])==R0 and Q(field["added_term_tail_radius"])==RA
        and Q(field["common_outer_angle_strip"])==SIGMA0
        and all(rows[p]["angular_derivative_orders"]==[0,1,2,3] for p in (0,1))
        and tail["first_omitted_Taylor_degree"]==13 and Q(tail["old_radius"])==R0
        and Q(tail["new_added_term_radius"])==RA and Q(tail["outer_old_phi_strip"])==SIGMA0
        and tail["exact_delta_a1_radial_zero_order"]==3
        and tail["no_radius_scaling_applied_to_other_terms"]
        and tail["no_uncomputed_finite_coefficient_was_set_to_zero"]
        and tail["angular_tails_from_joint_double_Cauchy"]
        and W["scope"]["new_reference_first_correction_identified_by_exact_integral"]
        and W["scope"]["same_T_actual_composition_not_same_old_r_substitution"]
        and W["scope"]["old_first_correction_relabelled_as_new"] is False
        and W["exact_branch_identity"]["first_correction_a1_minus"]=="-a1_plus"
        and W["exact_branch_identity"]["first_correction_b1_minus"]=="b1_plus")
    bd=B["complete_domain_conclusion"];rv=RV["complete_negative_Taylor_conclusion"]
    gate("the completed B product and RV b1 refer to the identical negative physical genuine amplitude",
        0<h<H<RS<RG and Q(bd["exact_new_old_rho_radius"])==RS
        and Q(bd["exact_new_old_phi_strip"])==SS and Q(bd["exact_full_physical_cover"])==H
        and bd["all_sT_paths_in_same_paid_domain"] and bd["root_normalization_and_all_means_unchanged"]
        and B["old_forcing_fold_transport_RF_or_profile_recomputed"]==0
        and Q(rv["exact_new_negative_rho_cover"])==h
        and Q(rv["old_complete_whole_piece_radius"])==H
        and rv["complete_derivatives_compared"]==13 and rv["full_zero_mode_retained"]
        and rv["complete_original_finite_budget_not_rescaled"]
        and rv["subtracted_lower_is_same_algorithm_tail_not_function_lower"]
        and rv["original_coefficients_Fourier_norms_transport_and_products_recomputed"] is False
        and len(rv["retained_complete_b1_value_derivative_upper"])==4
        and len(rv["retained_complete_b1_radial_derivative_upper"])==3)
    oldM=lower(tail["unchanged_original_full_product_modulus"]["a1"],"identical original positive modulus")
    addM=lower(tail["complete_added_term_full_product_modulus"]["a1"],"identical added positive modulus")
    modulus=bound(bd["complete_new_amplitude_modulus"]["a1"],"accepted complete genuine a1 product")
    aa={0:[],1:[]};details=[]
    for p,qlist in ((0,range(4)),(1,range(3))):
        for q in qlist:
            prior=rows[p]["complete_joint_Wiener_upper"][q]
            total=bound(prior,"old genuine a1 complete derivative")
            same=(radial_tail_number(oldM,R0,H,p)+radial_tail_number(addM,RA,H,p))*fourier_tail_number(SIGMA0,q)
            same_lower=lower(same,"identical old positive tail addend")
            finite=(total-same_lower).upper()
            if not finite.is_finite() or finite.lower()<0:
                raise ValueError("same positive-tail recovery inconsistent; no clipping")
            fresh=up(radial_tail_number(modulus,RS,h,p)*fourier_tail_number(SS,q))
            candidate=up(finite+fresh);complete=min(candidate,total).upper()
            aa[p].append(complete)
            details.append(dict(p=p,q=q,old_complete_total=prior,
                same_algorithm_positive_tail_lower=rec(same_lower),recovered_finite_budget_upper=rec(finite),
                new_complete_tail_upper=rec(fresh),complete_new_derivative_upper=rec(complete)))
    bb={0:[bound(v,"accepted RV genuine b1 value jet") for v in rv["retained_complete_b1_value_derivative_upper"]],
        1:[bound(v,"accepted RV genuine b1 radial jet") for v in rv["retained_complete_b1_radial_derivative_upper"]]}
    gate("only seven new a1 derivatives are evaluated and all seven successful RV b1 bounds are read complete",
        len(details)==7 and len(aa[0])==len(bb[0])==4 and len(aa[1])==len(bb[1])==3
        and all(v.is_finite() and v.lower()>=0 for c in (aa,bb) for row in c.values() for v in row))
    conclusion=dict(exact_negative_rho_cover=str(h),exact_original_whole_cover=str(H),
        genuine_amplitude_identity="w1V=free_w1+(T*b0,a0)*B(T)",
        exact_new_a1_bound_count=7,accepted_b1_bound_count=7,
        complete_a1_value_derivative_upper=encode(aa[0]),complete_a1_radial_derivative_upper=encode(aa[1]),
        accepted_b1_value_derivative_upper=rv["retained_complete_b1_value_derivative_upper"],
        accepted_b1_radial_derivative_upper=rv["retained_complete_b1_radial_derivative_upper"],
        accepted_RV_Taylor_conclusion_sha256=payload_sha(rv),
        full_zero_mode_and_both_carriers_retained=True,
        same_numerical_positive_tail_lower_not_function_lower=True,
        old_finite_coefficients_norms_and_new_b1_bounds_recomputed=False)
    return aa,bb,conclusion,details

def direct_physical_sources(f,c,AJ,Hr,aa,bb,h,gate):
    """DG10--21. Only density1; every returned source has ordinary jets0..2."""
    domain=AJ["complete_domain_conclusion"];hi=Hr["old_circle_inverse"]
    TH=bound(domain["accepted_complete_physical_T_image"],"accepted full SG physical T image")
    Q0=bound(f["Q"],"complete original characteristic Q")
    det=gap(hi["complete_deformed_determinant_modulus_lower"],"accepted complete genuine determinant")
    V0=bound(hi["complete_composed_V_angular_derivative_bounds"][0],"accepted complete composed V")
    gate("the direct physical derivatives and genuine rank share the unchanged full old parameter and angle domains",
        Q(domain["exact_full_physical_cover"])==H and Q(domain["exact_original_fold_radius"])==RG
        and Q(domain["exact_original_fold_strip"])==SG
        and domain["physical_T_image_definition_read_from_frozen_producer"]
        and domain["full_mean_and_radial_G_scalar_retained"]
        and Q(hi["exact_full_physical_root_cover"])==H and Q(hi["exact_old_rho_radius"])>=H
        and Q(hi["exact_inverse_phi_strip"])==SB and hi["full_mean_output_retained"]
        and hi["actual_reference_seam_jumps_retained"] and 0<h<H
        and len(c["D"])>=3 and SB<SG and N==388)
    d=[bound(c["D"][k],"complete drift derivative") for k in range(3)]
    m12=cauchy(up(Q0*TH),SG,3);m21=cauchy(Q0,SG,3)
    w=[aa[0],bb[0]];wr=[aa[1],bb[1]]
    direct=[];principal=[]
    for i,m in ((0,m12),(1,m21)):
        partner=w[1-i]
        drift=mul(d,w[i][1:],2)
        divergence=mul(m,partner,3)[1:4]
        direct.append(add(wr[i],drift,divergence,k=2))
        principal.append(mul(m,partner,2))
    tau=ex(H/RG);smallx=up(tau*bound(f["j"],"original rooted x-minus-one modulus"))
    y0=up(tau*tau*bound(f["BT"],"original second-order rooted y modulus"))
    x=cauchy(smallx,SG,3);x[0]=up(1+smallx)
    y=cauchy(y0,SG,3)
    pref=cauchy(up(Q0*V0/det),SB,3)
    inner=add(mul(y,w[0],3),mul(x,w[1],3),k=3)
    rank=[product(pref,x,inner,k=3),product(pref,y,inner,k=3)]
    weight=ex(Q(1,N*N))
    pp=[add(principal[i],scale(rank[i],weight,2),k=2) for i in range(2)]
    gg=[add(direct[i],scale(rank[i][1:],weight,2),k=2) for i in range(2)]
    gate("the complete density1 physical transport retains its radial sign drift full derivative rank and exact input weight",
        all(len(v)==3 for v in pp+gg)
        and all(len(v)==4 for v in rank)
        and all(v.is_finite() and v.lower()>=0 for row in pp+gg+rank for v in row))
    conclusion=dict(exact_negative_rho_cover=str(h),
        direct_identity="G0w=(a_r-d*a_phi+i*epsilon*(Q*T*b)_phi,b_r-d*b_phi+i*epsilon*(Q*a)_phi)",
        exact_radial_derivative="partial_r=-partial_old_rho",
        exact_genuine_p_identity="-i*epsilon*Q*K*w-n^-2*R(w)",
        exact_genuine_g_identity="G0w+n^-2*partial_phi R(w)",
        exact_rank_identity="(Q*V/Delta)*(-i*epsilon*x,y)^t*(i*epsilon*y*a+x*b)",
        reaction_vartheta_not_inserted_in_transport_rank=True,
        complete_principal_QT_derivative_upper=encode(m12),complete_principal_Q_derivative_upper=encode(m21),
        complete_direct_G0_angular_derivative_upper=encode(direct),
        complete_rank_angular_derivative_upper=encode(rank),
        complete_g_angular_derivative_upper=encode(gg),complete_p_angular_derivative_upper=encode(pp),
        accepted_complete_T_image=domain["accepted_complete_physical_T_image"],
        accepted_complete_determinant_lower=hi["complete_deformed_determinant_modulus_lower"],
        exact_input_rank_weight="1/150544",physical_angle_orders=[0,1,2],
        no_breg_or_cT_quotient_bound_used=True,no_second_radial_derivative_used=True,
        original_fold_inverse_and_connection_producers_called=False,
        full_amplitude_means_and_signed_carriers_retained=True)
    return dict(g=gg,p=pp),conclusion

def density_one_comparisons(rows,source,A,words,W2,baseline,gate):
    """DG22--26; density0 stays verbatim. Three ordinary jets, never the old k3 loop."""
    if len(rows)!=6:raise ValueError("the same six physical rows are required")
    g=source["g"];p=source["p"]
    if any(len(v)!=3 for v in g+p):raise ValueError("density1 requires exactly angular0..2")
    Gg=A(g);Mg=Gg
    KR=bound(words["C_RQJ_directed"],"complete RQJ word")
    KP=bound(words["C_primitive_directed"],"complete primitive word")
    KU=bound(words["C_uJ_directed"],"complete independent mean uJ word")
    radial=bound(W2,"accepted complete squared-envelope radial integral").sqrt().upper()
    maxima={};temporary=[]
    for row in rows:
        c=unpack(row["bounds"]);V=[bound(v,"original full background V jet") for v in c["V"]]
        if len(V)<4:raise ValueError("the original complete background omits an angular derivative")
        J=bound(c["C_J_scalar"],"complete outer J")
        cb=bound(c["cB"],"complete mean prefactor");mt=bound(c["m0_T0"],"complete transported mean")
        ef=bound(c["exact_nonlocal_even_mean_row_factor"],"complete independent physical mean normalization")
        yy=[mul(V,p[i],2) for i in range(2)]
        qq=[add(mul(V,g[i],2),mul(V[1:],p[i],2),k=2) for i in range(2)]
        Gq=A(qq);Gy=A(yy);My=Gy
        values=dict(
            density1_complete_RQ_J_g=up(J*KR*Gg),
            density1_complete_primitive=up(J*KP*Gq),
            density1_old_mean_transported=up(J*(cb*V[1]*V[0]*Mg/4+mt*Mg)),
            density1_old_mean_vphi=up(J*cb*V[1]*My),
            density1_complete_uJ_g=up(ef*KU*Gg))
        if any(not v.is_finite() or v.lower()<0 for v in values.values()):
            raise ValueError("a complete density1 row coefficient is invalid")
        for key,value in values.items():
            maxima[key]=value if key not in maxima else max(maxima[key],value).upper()
        temporary.append(dict(common_row=row["common_row"],interval=row["interval"],
            original_row_payload_sha256=payload_sha(row),complete_coefficients=encode(values),
            complete_q_angular_derivative_upper=encode(qq),complete_y_angular_derivative_upper=encode(yy),
            Gamma_g=rec(Gg),M_g=rec(Mg),Gamma_q=rec(Gq),M_q=rec(Gq),Gamma_y=rec(Gy),M_y=rec(My)))
    terms=dict(baseline["complete_first_source_term_L2_upper"])
    means=dict(baseline["complete_independent_mean_term_L2_upper"]);comparisons=[]
    for name in ("complete_RQ_J_g","complete_primitive","old_mean_transported","old_mean_vphi","complete_uJ_g"):
        key="density1_"+name;target=means if name=="complete_uJ_g" else terms
        candidate=up(radial*maxima[key]);prior=target[key]
        selected,better=old.selected_total(prior,candidate);target[key]=selected
        comparisons.append(dict(source_term=key,output="independent_physical_mean" if target is means else "first",
            same_original_row_count=6,complete_uniform_row_coefficient=rec(maxima[key]),
            accepted_complete_L2_upper=prior,new_complete_L2_upper=rec(candidate),
            selected_complete_L2_upper=selected,strictly_smaller_complete_term=better,
            original_radial_integral_recomputed=False,wholeword_contains_original_inner_factors=True))
    changed={x["source_term"] for x in comparisons}
    gate("only the five complete density1 terms change and every density0 local mean and true radial measure is retained",
        len(comparisons)==len(maxima)==5 and len(terms)==21 and len(means)==10
        and len(temporary)==6
        and all(terms[k]==v for k,v in baseline["complete_first_source_term_L2_upper"].items() if k not in changed)
        and all(means[k]==v for k,v in baseline["complete_independent_mean_term_L2_upper"].items() if k not in changed))
    operators=dict(density=1,Gamma_g=rec(Gg),M_g=rec(Mg),
        input_window="H^(-4/3)",column_output_window="H^(-5/3)",
        outer_J_window="H^(-5/3) -> H^(-2/3)",complete_independent_mean=True,
        same_complete_column_envelope="abs(rho)^(-1/4)",
        accepted_positive_profile_branches=3,accepted_positive_coefficients=18)
    return terms,means,comparisons,operators,temporary

def params():
    return dict(exact_original_root_interval=list(map(str,ROOTS)),exact_original_physical_piece=list(map(str,PIECE)),
        exact_original_whole_cover=str(H),exact_negative_rho_cover=str(ROOTS[1]-PIECE[0]),
        exact_old_Taylor_radius=str(R0),exact_added_Taylor_radius=str(RA),
        exact_old_Taylor_angle_strip=str(SIGMA0),exact_complete_amplitude_radius=str(RS),
        exact_complete_amplitude_angle_strip=str(SS),exact_fold_radius=str(RG),
        exact_fold_angle_strip=str(SG),exact_inverse_angle_strip=str(SB),
        fixed_intrinsic_parameter="eta_0",exact_complex_delta_square_halfwidth="1/100000000",
        exact_complex_z_square_halfwidth="1/9409",input_abs_j_lower=97,input_physical_frequency_lower=N,
        input_window="H^(-4/3)",density_one_column_window="H^(-5/3)",
        density_one_outer_J_window="H^(-5/3) -> H^(-2/3)",
        first_source_window="ordinary L2_r H^(-2/3)",independent_mean_window="ordinary L2_r constant",
        new_a1_orders=[[0,q] for q in range(4)]+[[1,q] for q in range(3)],
        accepted_RV_b1_orders_only_read=[[0,q] for q in range(4)]+[[1,q] for q in range(3)],
        accepted_RV_run=RV_RUN+"/1",accepted_AJ_run="43718112378/1",
        original_positive_coefficient_count=18,original_complete_row_count=1328,selected_row_count=6,
        original_complete_source_term_count=31,new_complete_density_one_term_count=5,
        density_zero_and_all_local_terms_read_verbatim=True,rank_input_weight="1/150544",
        exact_radial_sign="partial_r=-partial_old_rho",new_source_contract_sha256=CONTRACT,
        no_breg_fixed_X_conversion_or_old_G_pipeline=True,new_radial_integrals=0)

def render(doc):
    lines=["# Actual direct physical transport of the genuine first correction","",
        "This records only the new complete density1 scalar comparison on the unchanged negative root piece.",
        "The complete high inverse, source-to-wave map and physical/reference seam closure are separate.","",
        "- Scientific child code: "+str(doc.get("actual_returncode")),
        "- Mathematical complete: "+str(doc.get("complete")),
        "- New genuine a1 derivatives: "+str(doc.get("new_complete_a1_derivative_bounds",0)),
        "- Accepted RV b1 derivatives read: "+str(doc.get("accepted_complete_b1_derivative_bounds_read",0)),
        "- New complete comparisons: "+str(doc.get("new_complete_uniform_comparisons",0)),
        "- Old numerical enclosures recomputed: 0",
        "- New radial integrals: 0",""]
    if doc.get("failure"):lines+=["## Actual failure","",json.dumps(doc["failure"],ensure_ascii=False),""]
    result=doc.get("complete_source_conclusion")
    if result:
        lines+=["## Complete ordinary source bounds","",
            "| Quantity | Complete bound |","|---|---|"]
        for key in ("local_L2_upper","nonlocal_total_L2_upper","first_L2_upper","mean_L2_upper","combined_L2_upper"):
            lines.append("| "+key+" | "+result[key]["ball"]+" |")
        lines+=["","## Five whole-term comparisons","",
            "| Term | Accepted bound | New bound | Retained bound | Improved |","|---|---|---|---|---|"]
        for row in doc["complete_comparison_conclusions"]:
            lines.append("| "+row["source_term"]+" | "+row["accepted_complete_L2_upper"]["ball"]
                +" | "+row["new_complete_L2_upper"]["ball"]+" | "+row["selected_complete_L2_upper"]["ball"]
                +" | "+str(row["strictly_smaller_complete_term"])+" |")
        lines+=["","## Full unchanged-window ledger","",
            "| First-row term | Complete L2 bound |","|---|---|"]
        for key,value in result["complete_first_source_term_L2_upper"].items():
            lines.append("| "+key+" | "+value["ball"]+" |")
        lines+=["","| Independent physical mean term | Complete L2 bound |","|---|---|"]
        for key,value in result["complete_independent_mean_term_L2_upper"].items():
            lines.append("| "+key+" | "+value["ball"]+" |")
    lines+=["","The first correction is w1V, including its Fuchsian addition; it is not the old free w1.",
        "The ordered rank has its original input n^-2 factor. The amplitude mean and independent physical mean are retained separately.",
        "Original arrays and new row products exist only in the temporary runner workspace.",""]
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
    h=ROOTS[1]-PIECE[0]
    doc=dict(kind=KIND,public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=source,input_manifest_sha256=a.manifest_sha,runtime=runtime,arithmetic_bits=320,
        complete=False,proved=False,actual_returncode=1,failure=None,gates=[],
        original_complete_fold_stages_read=0,original_successful_small_receipts_read=0,
        original_complete_coefficient_rows_read=0,original_selected_coefficient_rows_read=0,
        original_positive_linear_coefficients_read=0,original_complete_source_terms_read=0,
        original_complete_word_maxima_read=0,original_complete_word_maxima_consumed=0,
        accepted_complete_b1_derivative_bounds_read=0,new_complete_a1_derivative_bounds=0,
        new_same_positive_tail_lower_recoveries=0,new_direct_physical_density_one_budgets=0,
        new_complete_companion_row_budgets=0,new_complete_window_evaluations=0,
        new_complete_uniform_comparisons=0,new_complete_scalar_recombinations=0,
        old_numerical_enclosures_recomputed=0,old_target_FFT_intrinsic_repair_fold_transport_or_Taylor_recomputed=0,
        old_RF_forcing_amplitude_or_profile_enclosures_recomputed=0,old_RV_b1_bounds_recomputed=0,
        old_inverse_word_or_positive_calibration_recomputed=0,old_source_row_or_radial_integral_recomputed=0,
        old_breg_cT_Xi_or_factored_source_pipeline_invocations=0,new_radial_integrals_computed=0,
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
            accepted_RV_execution=RV_EXEC,original_RV_algorithm=RV_SOURCE,original_RV_manifest=RV_MANIFEST,
            whole_Taylor_execution=W_EXEC,original_whole_Taylor_algorithm=W_SOURCE,
            amplitude_execution=old.S_EXEC,complete_genuine_execution=old.C_EXEC,
            directed_source_execution=old.D_EXEC,refined_first_local_execution=old.B_EXEC,
            columns_execution=old.H_EXEC,old_fold_majorants_stage=old.MAJORANTS,
            adjacent_process=old.APROC,adjacent_publication=old.APUB,
            original_norm_native=old.OLD_NATIVE,original_norm_process=old.OLD_PROCESS,
            original_first_local_algorithm=old.P_SOURCE,original_fold_algorithm="410675cf78dd30d97ff052558df1a819977291d40c628211fcf623ffc0b5f783",
            directed_process="00afd54464db46f110ecff8c1968b158deedac719a363590fc366038b47fedb8")
        gate("all accepted receipts original mathematical algorithms and natural stage bytes have their exact identities",
            all(sha(paths[k])==v for k,v in expected.items()))
        prior=read(paths["original_AJ_manifest"])
        gate("all fifty original AJ pins are unchanged in the new scientific closure",
            len(prior["files"])==50 and prior["scientific_source_sha256"]==AJ_SOURCE
            and all(pins.get(e["path"])==e for e in prior["files"]))
        ms=read(paths["old_fold_majorants_stage"]);ap=read(paths["adjacent_process"]);au=read(paths["adjacent_publication"])
        prs=[v for v in au["files"] if v["file"]=="consumers/stages/complete-original-reference-holomorphic-majorants.json.gz"]
        if len(prs)!=1:raise ValueError("the original fold publication receipt is not unique")
        gate("the complete fold and physical coefficients keep their actual successful source runtime and full majorants",
            ms["complete"] and ms["name"]==ms["stage"]=="complete-original-reference-holomorphic-majorants"
            and ms["source_sha256"]==old.LEGACY_SOURCE and ms["algebra_sha256"]==old.LEGACY_HELPER
            and ms["input_manifest_sha256"]==old.LEGACY_MANIFEST and ms["runtime"]==runtime
            and prs[0]["bytes"]==4501 and prs[0]["sha256"]==old.MAJORANTS
            and ap["actual_returncode"]==0 and ap["mathematical_complete"] and ap["mathematical_proved"]
            and ap["mathematical_failure"] is None and au["complete"]
            and all(ms["payload"]["majorants"][k][1:]==[str(RG),str(SG)] for k in ("A","chi")))
        saved=unpack(ms["payload"]);fold=saved["fold"];coefficient=saved["coefficients"]
        doc["original_complete_fold_stages_read"]=1
        S=accepted(paths["amplitude_execution"],"43698106023",old.S_SOURCE,old.S_MANIFEST,old.S_EXEC,26,gate)
        C=accepted(paths["complete_genuine_execution"],"43702688640",old.C_SOURCE,old.C_MANIFEST,old.C_EXEC,17,gate)
        D=accepted(paths["directed_source_execution"],"43703879926",old.D_SOURCE,old.D_MANIFEST,old.D_EXEC,12,gate)
        B=accepted(paths["refined_first_local_execution"],"43711480764",old.B_SOURCE,old.B_MANIFEST,old.B_EXEC,19,gate)
        Hr=accepted(paths["columns_execution"],"43688459733",old.H_SOURCE,old.H_MANIFEST,old.H_EXEC,16,gate)
        W=accepted(paths["whole_Taylor_execution"],"43694458725",W_SOURCE,W_MANIFEST,W_EXEC,9,gate)
        AJ=accepted(paths["accepted_AJ_execution"],"43718112378",AJ_SOURCE,AJ_MANIFEST,AJ_EXEC,29,gate)
        RV=accepted(paths["accepted_RV_execution"],RV_RUN,RV_SOURCE,RV_MANIFEST,RV_EXEC,27,gate)
        doc["original_successful_small_receipts_read"]=8
        gate("all accepted products retain the same intrinsic root parameter squares signed reference and complete physical means",
            S["scope"]["original_root_piece_2549_only"] and S["scope"]["full_complex_delta_square"]
            and S["scope"]["full_z_square_all_abs_j_ge97"] and S["scope"]["both_carrier_signs"]
            and S["complete_domain_conclusion"]["exact_original_physical_piece_interval"]==list(map(str,PIECE))
            and S["complete_domain_conclusion"]["exact_original_true_root_interval"]==list(map(str,ROOTS))
            and C["scope"]["original_fixed_intrinsic_parameter"]=="eta_0"
            and C["scope"]["both_genuine_columns_and_both_carrier_signs"]
            and C["scope"]["all_input_abs_j_at_least97"]
            and C["scope"]["output_mean_and_complete_original_primitive_retained"]
            and C["scope"]["physical_J_only_on_its_proved_reflected_parity_domain"]
            and W["scope"]["same_original_rho_orientation_and_input_frequency"]
            and AJ["full_physical_negative_volume_source_paid"] and RV["full_physical_negative_volume_source_paid"]
            and not AJ["full_high_inverse_claimed"] and not RV["full_high_inverse_claimed"]
            and AJ["old_numerical_enclosures_recomputed"]==RV["old_numerical_enclosures_recomputed"]==0)
        ajbase=AJ["complete_source_conclusion"];base=RV["complete_source_conclusion"]
        stable=("actual_dr_measure","exact_negative_physical_cover","one_sided_uncertain_root_band_retained",
            "both_density_windows_retained","outer_J_window","input_window","first_output_window",
            "independent_even_mean_window","total_squared_envelope_radial_weight_upper",
            "original_temporary_row_payload_sha256","old_nine_word_and_five_physical_mean_counts",
            "nonlocal_total_L2_upper","mean_L2_upper","complete_independent_mean_term_L2_upper")
        gate("the successful RV ledger preserves every AJ nonlocal density0 and mean term and changes only two complete local terms",
            len(base["complete_first_source_term_L2_upper"])==21
            and len(base["complete_independent_mean_term_L2_upper"])==10
            and all(base[k]==ajbase[k] for k in stable)
            and all(base["complete_first_source_term_L2_upper"][k]==v
                for k,v in ajbase["complete_first_source_term_L2_upper"].items()
                if k not in ("local_raw_1","local_raw_2"))
            and base["only_two_complete_local_vectors_replaced"]
            and base["all_other_twenty_nine_term_balls_read_verbatim"]
            and base["exact_negative_physical_cover"]==[str(PIECE[0]),str(ROOTS[1])]
            and RV["new_complete_negative_Taylor_derivative_bounds"]==13
            and RV["complete_original_free_budget_conclusion"]["actual_negative_rho_cover"]==str(h)
            and base["old_nine_word_and_five_physical_mean_counts"]==[9,5])
        ws=paths["original_whole_Taylor_algorithm"].read_text()
        ps=paths["original_first_local_algorithm"].read_text()
        fs=paths["original_fold_algorithm"].read_text()
        gate("the genuine W component identities positive old tail recipe and complete SG T image are bound to their exact frozen definitions",
            'a1=[old["a1"][n]+da[n] for n in range(count)]' in ws
            and 'b1=[old["b1"][n]+db[n] for n in range(count)]' in ws
            and 'tb=[coeff_product(leading["T"],leading["b0"],n) for n in range(count)]' in ws
            and 'db=[coeff_product(leading["a0"],bc,n) for n in range(count)]' in ws
            and "fulltail=oldtail+newtail" in ws and "tail=fulltail*angular_sum(SIGMA-width,q)" in ws
            and "vals.append(rec(up(finite+tail)))" in ws
            and 'imageT=up(ex(H)*powr(Ap,Q(2,3)))' in ps
            and 'Ap=bound(f["Ap"],"old A modulus")' in ps
            and "SG=Q(3,128);SF=Q(1,64)" in fs and "LAM=Q(9,2)" in fs)
        aa,bb,derivatives,tail_details=genuine_component_jets(W,B,RV,h,gate)
        doc.update(accepted_complete_b1_derivative_bounds_read=7,new_complete_a1_derivative_bounds=7,
            new_same_positive_tail_lower_recoveries=7,complete_genuine_derivative_conclusion=derivatives)
        source_arrays,physical=direct_physical_sources(fold,coefficient,AJ,Hr,aa,bb,h,gate)
        doc.update(new_direct_physical_density_one_budgets=1,complete_direct_physical_transport_conclusion=physical)
        rows,words=old.checked_accepted_rows(paths,C,D,AJ,gate)
        doc.update(original_complete_coefficient_rows_read=1328,original_selected_coefficient_rows_read=6,
            original_complete_word_maxima_read=8,original_complete_word_maxima_consumed=3,
            original_complete_source_terms_read=31)
        positive=old.read_positive_coefficients(C,gate);A=old.PositiveOperator(positive)
        doc["original_positive_linear_coefficients_read"]=18
        terms,means,comparisons,operators,row_details=density_one_comparisons(
            rows,source_arrays,A,words,base["total_squared_envelope_radial_weight_upper"],base,gate)
        result=old.combine(base,terms,means)
        doc.update(new_complete_companion_row_budgets=6,new_complete_window_evaluations=13,
            new_complete_uniform_comparisons=5,new_complete_scalar_recombinations=4,
            complete_transport_operator_conclusion=operators,complete_comparison_conclusions=comparisons,
            complete_source_conclusion=result,strictly_smaller_complete_term_bounds=sum(
                int(x["strictly_smaller_complete_term"]) for x in comparisons))
        changed={v["source_term"] for v in comparisons}
        gate("the complete retained ledger preserves all three local terms all density0 terms and the original true dr measure",
            result["local_L2_upper"]==base["local_L2_upper"]
            and all(result["complete_first_source_term_L2_upper"][k]==v
                for k,v in base["complete_first_source_term_L2_upper"].items() if k not in changed)
            and all(result["complete_independent_mean_term_L2_upper"][k]==v
                for k,v in base["complete_independent_mean_term_L2_upper"].items() if k not in changed)
            and sum(k not in changed for k in terms)==17 and sum(k not in changed for k in means)==9
            and result["total_squared_envelope_radial_weight_upper"]==base["total_squared_envelope_radial_weight_upper"]
            and result["original_temporary_row_payload_sha256"]==base["original_temporary_row_payload_sha256"])
        gate("the complete new negative volume source is finite with both genuine windows and independent physical mean",
            all(bound(result[k],k).is_finite() for k in
                ("local_L2_upper","nonlocal_total_L2_upper","first_L2_upper","mean_L2_upper","combined_L2_upper"))
            and result["actual_dr_measure"] and result["one_sided_uncertain_root_band_retained"]
            and result["both_density_windows_retained"] and result["old_nine_word_and_five_physical_mean_counts"]==[9,5])
        doc["scope"]=dict(original_physical_root_piece_2549_only=True,original_fixed_intrinsic_parameter="eta_0",
            same_original_real_explicit_family=True,full_complex_delta_and_z_squares_for_coefficient_bounds=True,
            final_operators_restrict_to_original_real_parameters=True,
            both_genuine_columns_and_both_carrier_signs=True,all_input_abs_j_at_least97=True,
            density_one_is_genuine_w1V_not_old_free_w1=True,accepted_RV_b1_derivatives_only_read=True,
            exact_physical_radial_derivative_sign_retained=True,
            exact_genuine_rank_input_n_minus_two_retained=True,rank_contains_no_reaction_vartheta=True,
            q_is_v_Dw_minus_angle_derivative_of_vp_not_D_of_vw=True,
            density_zero_complete_source_read_verbatim=True,all_three_local_terms_read_verbatim=True,
            full_amplitude_means_and_independent_physical_even_mean_retained=True,
            complete_original_primitive_and_both_directed_J_windows_retained=True,
            no_duplicate_inner_word_or_mean_normalization=True,physical_J_only_on_its_proved_reflected_parity_domain=True,
            all_actual_physical_seams_and_reference_matching_sources_retained=True,
            original_positive_graph_and_outer_source_ports_retained=True,
            complete_row_and_derivative_arrays_published=False,physical_to_wave_readout_paid=False,
            full_negative_BVP_inverse_paid=False,positive_growing_column_operator_paid=False,
            cutoff97_strong_return_contraction_paid=False)
        temporary.update(new_a1_positive_addend_details=tail_details,complete_companion_rows=row_details,
            accepted_positive_coefficients_payload_sha256=payload_sha(C["complete_positive_linear_operator_conclusion"]))
        doc["temporary_complete_companion_row_payload_sha256"]=payload_sha(row_details)
        doc["temporary_complete_companion_row_count"]=len(row_details)
        doc.update(complete=True,proved=True,actual_returncode=0,full_physical_negative_volume_source_paid=True)
    except BaseException as error:
        doc["failure"]=dict(type=type(error).__name__,message=str(error))
    finally:
        doc["actual_mathematical_wall_seconds"]=time.monotonic()-started
        temporary.update(kind=KIND,source_sha256=source,input_manifest_sha256=a.manifest_sha,complete_conclusions=doc)
        native=a.out_dir/"temporary-direct-physical-genuine-transport.json.gz"
        save(native,temporary,True)
        doc["temporary_native_sha256"]=sha(native);doc["temporary_native_bytes"]=native.stat().st_size
        doc["temporary_native_is_not_published"]=True;actual=doc["actual_returncode"]
        try:
            report=render(doc)
            raw=(json.dumps(doc,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
            if len(raw)>60000 or len(report.encode())>60000:raise ValueError("small conclusion or process exceeded60000 bytes")
            save(a.out_dir/"process.json",doc);(a.out_dir/"conclusion.md").write_text(report)
        except BaseException as error:
            small={k:v for k,v in doc.items() if k not in ("complete_genuine_derivative_conclusion",
                "complete_direct_physical_transport_conclusion","complete_transport_operator_conclusion",
                "complete_comparison_conclusions","complete_source_conclusion")}
            small["actual_scientific_returncode"]=actual
            small["formatting_failure"]=dict(type=type(error).__name__,message=str(error))
            small.update(complete=False,proved=False,actual_returncode=1)
            save(a.out_dir/"process.json",small)
            (a.out_dir/"conclusion.md").write_text("# Actual direct-physical source formatting failure\n\n"
                "Original scientific child code: "+str(actual)+". Formatting is separate from mathematics.\n"
                "Temporary native SHA256: "+doc["temporary_native_sha256"]+"\n")
            actual=1
        print(json.dumps(dict(complete=doc["complete"],actual_returncode=actual,
            new_complete_comparisons=doc["new_complete_uniform_comparisons"],
            old_numerical_enclosures_recomputed=0,new_radial_integrals_computed=0,
            reproducible_data_published=False)),flush=True)
    return actual
if __name__=="__main__":raise SystemExit(main())
