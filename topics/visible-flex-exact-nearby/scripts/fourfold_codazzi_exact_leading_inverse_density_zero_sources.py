#!/usr/bin/env python3
"""New exact leading inverse-column bounds for three complete density0 sources.

Only a new negative-radius restriction, exact-column angular majorants and
three whole-term comparisons are computed. Original fold, inverse, column
calibration, directed words, source rows and radial integrals are read.
"""
from __future__ import annotations
import argparse,hashlib,json,math,os,platform,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy,scipy
from flint import arb,ctx
import fourfold_codazzi_factored_transport_companion_sources as old

PUBLIC,TOPIC,RUNTIME=old.PUBLIC,old.TOPIC,old.RUNTIME
KIND="actual_exact_leading_inverse_density_zero_sources_v1"
CONTRACT="5374f2b092c3c142c02bc754b78903576384f59b203a636166a28ae8dda8fdfb"
FACTORED_SOURCE="a705c2b4c64393e3ba1ae1e043d0fbd62f516a7a80e03e47ce11820626373ee7"
AJ_SOURCE="32c45b335639a48b0d32541d03924246023e5e3f19deec1bcd8cf0549e955f03"
AJ_MANIFEST="871240a7a97011d837025aad7f9ca1707d69c17b6dec3c1f510f6415c278b74d"
AJ_EXEC="58462f96a486dede07873c4fc6aade100539f9f28ef49b49567a4acf7c2e8706"
DG_SOURCE="7d28ab5f16bfec72faf898118781a5df0af9bc610e80d11bc9d67b8e0527e594"
DG_MANIFEST="cbb0f2acedd715220fc90b43bacd3dd571092b7dacd2da0cc4c554160fffe833"
DG_EXEC="48ca7d65c1abd9575c7be6e4e8ae4594cb6f4e1cf3d415cf119e2f2de3ebe425"
M_SOURCE="b4bc768e149f01591102a9bcc8c16b166bd8ba97fd0c0c245ba3073ba3382496"
M_MANIFEST="1055c8231c7646acb5b37e7c876a62321436192927ba9616ad7a1d08a24cb1e2"
M_EXEC="b858853023fd93bfefbac5f8e18471c93c88d90c051999bcf35dd9bc0df8aa4e"
FOLD_SOURCE="410675cf78dd30d97ff052558df1a819977291d40c628211fcf623ffc0b5f783"
INVERSE_SOURCE="9596ebee08e95939cf1b8a9d46a9f32053bd4706cc77e2263a80d09ede99294c"
H,ROOTS,PIECE,RG,SG,SB,N=old.H,old.ROOTS,old.PIECE,old.RG,old.SG,old.SB,old.N
HI=Q(1,20000)
sha,ex,rb,up,gap,rec=old.sha,old.ex,old.rb,old.up,old.gap,old.rec
read,save,unpack,encode,payload_sha=old.read,old.save,old.unpack,old.encode,old.payload_sha
mul,cauchy=old.mul,old.cauchy
FIRST=("density0_complete_SV","density0_old_mean_V0")
MEAN=("density0_complete_uJB_w",)

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
        potential_original_complex_z_square_halfwidth="1/9409",
        inverse_column_frequency_domain="physical input n=4*abs(j)>=388, both signs",
        independent_complex_frequency_inverse_claimed=False,angular_derivative_orders=[0,1,2,3],
        exact_inverse_column="G*(-i*epsilon*x,-y)-n^-2*V*G*y^2/Delta*(-i*epsilon*x,y)",
        exact_G_angle_identity="G_phi=(T_phi/T)*G/4",
        exact_input_correction_weight="1/n^2",minimum_input_weight_denominator=388,
        changed_complete_terms=list(FIRST+MEAN),unchanged_complete_term_count=28,
        accepted_baseline_run="43721735003/1",original_radial_integrals_recomputed=0,
        complete_mean_and_both_genuine_columns_retained=True)

def exact_column_jets(f,Hr,h,gate):
    """SV.7--SV.14: same exact B_j w0, no generic inverse-times-column bound."""
    hi=Hr["old_circle_inverse"]
    gate("the completed old-angle inverse and potential image contain the new negative product for every physical high input label",
        0<h<H<HI<RG and 0<SB<SG
        and Q(hi["exact_old_rho_radius"])==HI
        and Q(hi["exact_original_fold_radius"])==RG
        and Q(hi["exact_original_fold_phi_strip"])==SG
        and Q(hi["exact_inverse_phi_strip"])==SB
        and Q(hi["exact_Wiener_phi_strip"])==Q(1,128)
        and Q(hi["exact_full_physical_root_cover"])==H
        and hi["full_physical_root_piece_covered"]
        and not hi["physical_other_cubic_identity_claimed"]
        and hi["final_complex_old_circle_inverse_matrix_paid"]
        and hi["full_mean_output_retained"] and hi["physical_primitive_projection_retained"]
        and hi["actual_reference_seam_jumps_retained"]
        and not hi["full_complex_angle_reference_column_norm_paid"]
        and not hi["full_strong_return_or_high_BVP_inverse_paid"]
        and gap(hi["actual_common_potential_image_radius_lower"],"accepted potential image")
            >bound(hi["old_fold_image_modulus_upper"],"accepted whole inverse image"))
    lower_A=gap(f["Am"],"original full divided phase")
    Delta=gap(hi["complete_deformed_determinant_modulus_lower"],"accepted full old-angle determinant")
    V=bound(hi["complete_composed_V_angular_derivative_bounds"][0],"accepted complete potential modulus")
    G0=bound(f["G"],"original full radial gauge")
    tau=ex(h/RG)
    jh=up(tau*bound(f["j"],"original x minus one"))
    yh=up(tau*tau*bound(f["BT"],"original quadratic T_phi"))
    zh=up(ex(Q(2,3))*tau*bound(f["BA"],"original A_phi")/lower_A)
    X=cauchy(jh,SG,3);X[0]=up(1+jh)
    Y=cauchy(yh,SG,3);Z=cauchy(zh,SG,2)
    G=[G0]
    for k in range(3):
        G.append(up(sum((math.comb(k,l)*Z[l]*G[k-l] for l in range(k+1)),arb(0))/4))
    principal=[mul(G,X,3),mul(G,Y,3)]
    ra=up(V*G0*(1+jh)*yh*yh/Delta)
    rbv=up(V*G0*yh*yh*yh/Delta)
    correction=[cauchy(ra,SB,3),cauchy(rbv,SB,3)]
    # n^-2 is a physical input-label multiplier. It is paid once, outside
    # the old-angle Cauchy bound for each actual n. No complex-z gap is inferred.
    complete=[[up(principal[i][k]+correction[i][k]/ex(N*N))
        for k in range(4)] for i in range(2)]
    gate("the exact leading inverse column keeps its quadratic and cubic corrections and all four complete angular orders",
        len(complete)==2 and all(len(v)==4 for v in complete)
        and all(v.is_finite() and v.lower()>=0
            for row in complete+principal+correction for v in row)
        and all(v.is_finite() and v.lower()>=0 for v in G+X+Y+Z)
        and h==ROOTS[1]-PIECE[0] and N==388)
    conclusion=dict(exact_negative_rho_cover=str(h),exact_original_fold_radius=str(RG),
        exact_original_fold_strip=str(SG),exact_accepted_inverse_radius=str(HI),
        exact_accepted_inverse_strip=str(SB),complete_x_minus_one_upper=rec(jh),
        complete_quadratic_y_upper=rec(yh),complete_removable_y_over_T_upper=rec(zh),
        complete_G_angular_derivative_upper=encode(G),
        complete_X_angular_derivative_upper=encode(X),
        complete_Y_angular_derivative_upper=encode(Y),
        complete_zeta_angular_derivative_upper=encode(Z),
        complete_principal_first_component_angular_upper=encode(principal[0]),
        complete_principal_second_component_angular_upper=encode(principal[1]),
        complete_unweighted_correction_first_modulus=rec(ra),
        complete_unweighted_correction_second_modulus=rec(rbv),
        complete_inverse_column_first_angular_upper=encode(complete[0]),
        complete_inverse_column_second_angular_upper=encode(complete[1]),
        accepted_complete_V_modulus=hi["complete_composed_V_angular_derivative_bounds"][0],
        accepted_complete_determinant_gap=hi["complete_deformed_determinant_modulus_lower"],
        exact_physical_input_n_minus_two_paid_once=True,
        independent_complex_frequency_inverse_claimed=False,
        same_full_complex_delta_and_old_angle_domains_retained=True,
        potential_original_full_complex_z_modulus_read=True,
        full_radial_G_and_all_output_means_retained=True,
        original_fold_inverse_AJ_or_DG_closures_called=False)
    return complete,conclusion

def density_zero_window(column,A,gate):
    At=A(column)
    Mt=A([row[1:] for row in column])
    Gamma=up(At+Mt);Mean=up(Mt)
    gate("the original density derivative identity keeps both genuine branches the full old mean and the complete input-label weight",
        all(v.is_finite() and v.lower()>=0 for v in (At,Gamma,Mean))
        and len(column)==2 and all(len(row)==4 for row in column))
    return Gamma,Mean,dict(density=0,exact_column="B_j*w0",
        complete_column_operator_upper=rec(At),complete_derivative_operator_upper=rec(Mt),
        Gamma_w0=rec(Gamma),M_w0=rec(Mean),
        exact_density_mean_identity="Pi T(w0)=-Pi S(partial_phi(B_j*w0))",
        input_window="H^(-4/3), both genuine columns and both signs |j|>=97",
        density_window="H^(-8/3)",intermediate_column_window="H^(-5/3)",
        common_column_envelope="abs(rho)^(-1/4)",
        all_eighteen_positive_coefficients_summed=True,full_physical_even_mean_retained=True)

def complete_comparisons(rows,words,Gamma,Mean,W2,baseline,gate):
    if len(rows)!=6:raise ValueError("the complete source requires all six original rows")
    weight=bound(W2,"accepted complete squared-envelope radial weight").sqrt().upper()
    KSV=bound(words["C_SV_directed"],"accepted complete SV word")
    KUB=bound(words["C_uJB_directed"],"accepted complete independent-mean uJB word")
    maxima={};details=[]
    for row in rows:
        c=unpack(row["bounds"])
        J=bound(c["C_J_scalar"],"complete original outer scalar J")
        V0=bound(c["m0_V0"],"complete original old mean V0")
        ef=bound(c["exact_nonlocal_even_mean_row_factor"],"complete original independent-mean prefactor")
        values=dict(density0_complete_SV=up(J*KSV*Gamma),
            density0_old_mean_V0=up(J*V0*Mean),
            density0_complete_uJB_w=up(ef*KUB*Gamma))
        if any(not v.is_finite() or v.lower()<0 for v in values.values()):
            raise ValueError("invalid complete new source coefficient")
        for name,value in values.items():
            maxima[name]=value if name not in maxima else max(maxima[name],value).upper()
        details.append(dict(common_row=row["common_row"],exact_original_interval=row["interval"],
            exact_original_row_payload_sha256=payload_sha(row),complete_coefficients=encode(values)))
    terms=dict(baseline["complete_first_source_term_L2_upper"])
    means=dict(baseline["complete_independent_mean_term_L2_upper"])
    evidence=[]
    for name in FIRST+MEAN:
        target=terms if name in FIRST else means
        prior=target[name];candidate=up(weight*maxima[name])
        retained,improved=old.selected_total(prior,candidate);target[name]=retained
        evidence.append(dict(source_term=name,output="first" if name in FIRST else "independent_physical_mean",
            same_original_complete_row_count=6,
            complete_uniform_row_coefficient_upper=rec(maxima[name]),
            accepted_complete_L2_upper=prior,new_complete_L2_upper=rec(candidate),
            selected_complete_L2_upper=retained,strictly_smaller_complete_term=improved,
            complete_original_word_contains_all_inner_factors=True,
            original_radial_integral_recomputed=False))
    gate("three whole source comparisons preserve all original rows complete words true measure and twenty-eight other terms",
        len(maxima)==len(evidence)==3 and len(terms)==21 and len(means)==10
        and all(v==terms[k] for k,v in baseline["complete_first_source_term_L2_upper"].items() if k not in FIRST)
        and all(v==means[k] for k,v in baseline["complete_independent_mean_term_L2_upper"].items() if k not in MEAN))
    return terms,means,evidence,details

def render(doc):
    lines=["# Actual exact leading inverse-column density-zero sources","",
        "Only three complete source terms are compared; the complete SV operator and all old radial integrals are read.",
        "This is not a source-to-wave or high BVP inverse.","",
        "- Scientific child code: "+str(doc.get("actual_returncode")),
        "- Mathematical complete: "+str(doc.get("complete")),
        "- New exact inverse columns: "+str(doc.get("new_complete_exact_inverse_columns",0)),
        "- New complete comparisons: "+str(doc.get("new_complete_uniform_comparisons",0)),
        "- Old numerical enclosures recomputed: 0",
        "- New radial integrals: 0",""]
    if doc.get("failure"):lines+=["## Actual failure","",json.dumps(doc["failure"],ensure_ascii=False),""]
    result=doc.get("complete_source_conclusion")
    if result:
        lines+=["## Complete ordinary source bounds","","| Quantity | Complete bound |","|---|---|"]
        for k in ("local_L2_upper","nonlocal_total_L2_upper","first_L2_upper","mean_L2_upper","combined_L2_upper"):
            lines.append("| "+k+" | "+result[k]["ball"]+" |")
        lines+=["","## Three complete comparisons","",
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
    lines+=["","The exact inverse-column correction retains y squared and y cubed and pays the physical input n^-2 once.",
        "The original three branch sums, both density windows, amplitude means and independent physical means remain complete.",
        "All new arrays exist only in the temporary public runner workspace.",""]
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
        new_complete_negative_fold_restrictions=0,new_complete_exact_inverse_columns=0,
        new_complete_inverse_column_angular_bounds=0,new_complete_window_evaluations=0,
        new_complete_source_row_budgets=0,new_complete_uniform_comparisons=0,
        new_complete_scalar_recombinations=0,old_numerical_enclosures_recomputed=0,
        old_target_FFT_intrinsic_repair_fold_transport_or_Taylor_recomputed=0,
        old_inverse_word_or_positive_calibration_recomputed=0,
        old_AJ_DG_or_companion_source_closures_called=0,
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
            original_DG_algorithm=DG_SOURCE,original_DG_manifest=DG_MANIFEST,accepted_DG_execution=DG_EXEC,
            original_M_algorithm=M_SOURCE,original_M_manifest=M_MANIFEST,accepted_M_execution=M_EXEC,
            complete_genuine_execution=old.C_EXEC,directed_source_execution=old.D_EXEC,
            columns_execution=old.H_EXEC,old_fold_majorants_stage=old.MAJORANTS,
            adjacent_process=old.APROC,adjacent_publication=old.APUB,
            original_norm_native=old.OLD_NATIVE,original_norm_process=old.OLD_PROCESS,
            original_fold_algorithm=FOLD_SOURCE,original_inverse_algorithm=INVERSE_SOURCE,
            directed_process="00afd54464db46f110ecff8c1968b158deedac719a363590fc366038b47fedb8")
        gate("all successful receipts complete original algorithms and natural stage bytes retain exact identities",
            all(sha(paths[k])==v for k,v in expected.items()))
        prior=read(paths["original_DG_manifest"])
        gate("all fifty-nine original DG pins are unchanged in the new scientific closure",
            len(prior["files"])==59 and prior["scientific_source_sha256"]==DG_SOURCE
            and all(pins.get(e["path"])==e for e in prior["files"]))
        ms=read(paths["old_fold_majorants_stage"]);ap=read(paths["adjacent_process"]);au=read(paths["adjacent_publication"])
        prs=[v for v in au["files"] if v["file"]=="consumers/stages/complete-original-reference-holomorphic-majorants.json.gz"]
        if len(prs)!=1:raise ValueError("the original fold publication receipt is not unique")
        gate("the complete fold retains its successful source runtime and all original holomorphic majorants",
            ms["complete"] and ms["name"]==ms["stage"]=="complete-original-reference-holomorphic-majorants"
            and ms["source_sha256"]==old.LEGACY_SOURCE and ms["algebra_sha256"]==old.LEGACY_HELPER
            and ms["input_manifest_sha256"]==old.LEGACY_MANIFEST and ms["runtime"]==runtime
            and prs[0]["bytes"]==4501 and prs[0]["sha256"]==old.MAJORANTS
            and ap["actual_returncode"]==0 and ap["mathematical_complete"] and ap["mathematical_proved"]
            and ap["mathematical_failure"] is None and au["complete"]
            and all(ms["payload"]["majorants"][k][1:]==[str(RG),str(SG)] for k in ("A","chi")))
        fold=unpack(ms["payload"])["fold"];doc["original_complete_fold_stages_read"]=1
        C=accepted(paths["complete_genuine_execution"],"43702688640",old.C_SOURCE,old.C_MANIFEST,old.C_EXEC,17,gate)
        D=accepted(paths["directed_source_execution"],"43703879926",old.D_SOURCE,old.D_MANIFEST,old.D_EXEC,12,gate)
        Hr=accepted(paths["columns_execution"],"43688459733",old.H_SOURCE,old.H_MANIFEST,old.H_EXEC,16,gate)
        AJ=accepted(paths["accepted_AJ_execution"],"43718112378",AJ_SOURCE,AJ_MANIFEST,AJ_EXEC,29,gate)
        DG=accepted(paths["accepted_DG_execution"],"43720766795",DG_SOURCE,DG_MANIFEST,DG_EXEC,27,gate)
        M=accepted(paths["accepted_M_execution"],"43721735003",M_SOURCE,M_MANIFEST,M_EXEC,23,gate)
        doc["original_successful_small_receipts_read"]=6
        gate("the same genuine column domains original reflection and full physical mean are retained",
            C["scope"]["original_fixed_intrinsic_parameter"]=="eta_0"
            and C["scope"]["both_genuine_columns_and_both_carrier_signs"]
            and C["scope"]["all_input_abs_j_at_least97"]
            and C["scope"]["output_mean_and_complete_original_primitive_retained"]
            and C["scope"]["physical_J_only_on_its_proved_reflected_parity_domain"]
            and Hr["complex_old_circle_inverse_matrix_proved"]
            and Hr["original_mean_and_reference_interface_conditions_retained"]
            and AJ["full_physical_negative_volume_source_paid"] and DG["full_physical_negative_volume_source_paid"]
            and not AJ["full_high_inverse_claimed"] and not DG["full_high_inverse_claimed"]
            and AJ["old_numerical_enclosures_recomputed"]==DG["old_numerical_enclosures_recomputed"]==M["old_numerical_enclosures_recomputed"]==0
            and M["full_physical_negative_volume_source_paid"] and not M["full_high_inverse_claimed"]
            and DG["scope"]["all_three_local_terms_read_verbatim"]
            and DG["scope"]["density_zero_complete_source_read_verbatim"])
        base=M["complete_source_conclusion"];dgbase=DG["complete_source_conclusion"];ajbase=AJ["complete_source_conclusion"]
        stable=("actual_dr_measure","exact_negative_physical_cover","one_sided_uncertain_root_band_retained",
            "both_density_windows_retained","outer_J_window","input_window","first_output_window",
            "independent_even_mean_window","total_squared_envelope_radial_weight_upper",
            "original_temporary_row_payload_sha256","old_nine_word_and_five_physical_mean_counts")
        gate("the successful baseline retains the original density-zero ledger exact source windows and complete true measure",
            len(base["complete_first_source_term_L2_upper"])==21
            and len(base["complete_independent_mean_term_L2_upper"])==10
            and all(base[k]==dgbase[k]==ajbase[k] for k in stable)
            and all(base["complete_first_source_term_L2_upper"][k]==v
                for k,v in dgbase["complete_first_source_term_L2_upper"].items() if k!="local_raw_1")
            and base["complete_independent_mean_term_L2_upper"]==dgbase["complete_independent_mean_term_L2_upper"]
            and base["nonlocal_total_L2_upper"]==dgbase["nonlocal_total_L2_upper"]
            and base["mean_L2_upper"]==dgbase["mean_L2_upper"]
            and all(base["complete_first_source_term_L2_upper"][k]==v
                for k,v in ajbase["complete_first_source_term_L2_upper"].items() if k.startswith("density0_"))
            and all(base["complete_independent_mean_term_L2_upper"][k]==v
                for k,v in ajbase["complete_independent_mean_term_L2_upper"].items() if k.startswith("density0_"))
            and base["exact_negative_physical_cover"]==[str(PIECE[0]),str(ROOTS[1])]
            and base["old_nine_word_and_five_physical_mean_counts"]==[9,5])
        fs=paths["original_fold_algorithm"].read_text()
        hs=paths["original_inverse_algorithm"].read_text()
        gate("the frozen original scalar definitions retain the real frequency determinant and full first quadratic angular zeros",
            "j=(E-1).upper()" in fs and "BA=(ex(Q(3,5))*c[" in fs
            and "BT=(ex(Q(2,5))*c[" in fs
            and "n2=ex(N0*N0)" in hs and "N0=388" in hs
            and 'v=[up(rb(potential["complete_modulus_upper"][k])) for k in ("V","V_T","V_TT")]' in hs)
        column,conclusion=exact_column_jets(fold,Hr,h,gate)
        doc.update(new_complete_negative_fold_restrictions=1,new_complete_exact_inverse_columns=1,
            new_complete_inverse_column_angular_bounds=8,complete_exact_inverse_column_conclusion=conclusion)
        rows,words=old.checked_accepted_rows(paths,C,D,AJ,gate)
        doc.update(original_complete_coefficient_rows_read=1328,original_selected_coefficient_rows_read=6,
            original_complete_word_maxima_read=8,original_complete_word_maxima_consumed=2,
            original_complete_source_terms_read=31)
        positive=old.read_positive_coefficients(C,gate);A=old.PositiveOperator(positive)
        doc["original_positive_linear_coefficients_read"]=18
        Gamma,Mean,operators=density_zero_window(column,A,gate)
        terms,means,comparisons,row_details=complete_comparisons(
            rows,words,Gamma,Mean,base["total_squared_envelope_radial_weight_upper"],base,gate)
        result=old.combine(base,terms,means)
        doc.update(new_complete_window_evaluations=2,new_complete_source_row_budgets=6,
            new_complete_uniform_comparisons=3,new_complete_scalar_recombinations=4,
            complete_density_zero_operator_conclusion=operators,
            complete_comparison_conclusions=comparisons,complete_source_conclusion=result,
            strictly_smaller_complete_term_bounds=sum(int(v["strictly_smaller_complete_term"]) for v in comparisons))
        changed=set(FIRST+MEAN)
        gate("all twenty-eight other complete term balls including every local and density-one term remain byte identical",
            result["local_L2_upper"]==base["local_L2_upper"]
            and all(result["complete_first_source_term_L2_upper"][k]==v
                for k,v in base["complete_first_source_term_L2_upper"].items() if k not in changed)
            and all(result["complete_independent_mean_term_L2_upper"][k]==v
                for k,v in base["complete_independent_mean_term_L2_upper"].items() if k not in changed)
            and sum(k not in changed for k in terms)==19 and sum(k not in changed for k in means)==9
            and result["total_squared_envelope_radial_weight_upper"]==base["total_squared_envelope_radial_weight_upper"]
            and result["original_temporary_row_payload_sha256"]==base["original_temporary_row_payload_sha256"])
        gate("the complete new ordinary negative volume source is finite in both original windows with independent physical mean",
            all(bound(result[k],k).is_finite() for k in
                ("local_L2_upper","nonlocal_total_L2_upper","first_L2_upper","mean_L2_upper","combined_L2_upper"))
            and result["actual_dr_measure"] and result["one_sided_uncertain_root_band_retained"]
            and result["both_density_windows_retained"] and result["old_nine_word_and_five_physical_mean_counts"]==[9,5])
        doc["scope"]=dict(original_physical_root_piece_2549_only=True,original_fixed_intrinsic_parameter="eta_0",
            same_original_real_explicit_family=True,
            old_angle_and_delta_holomorphic_domains_retained=True,
            complete_potential_full_z_square_only_read=True,
            independent_complex_frequency_inverse_claimed=False,
            final_column_operators_use_physical_input_labels=True,
            both_genuine_columns_and_both_carrier_signs=True,all_input_abs_j_at_least97=True,
            exact_leading_inverse_column_not_constant_times_w0=True,
            exact_G_angle_identity_preserves_radial_mean=True,
            quadratic_and_cubic_rank_zeros_retained=True,
            physical_input_n_minus_two_paid_once=True,
            whole_SV_word_and_all_seven_operator_terms_retained=True,
            all_eighteen_positive_column_coefficients_summed=True,
            all_three_local_terms_and_all_density_one_terms_read_verbatim=True,
            other_twenty_eight_complete_terms_read_verbatim=True,
            full_amplitude_means_and_independent_physical_even_mean_retained=True,
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
        native=a.out_dir/"temporary-exact-leading-inverse-density-zero-sources.json.gz"
        save(native,temporary,True)
        doc["temporary_native_sha256"]=sha(native);doc["temporary_native_bytes"]=native.stat().st_size
        doc["temporary_native_is_not_published"]=True;actual=doc["actual_returncode"]
        try:
            report=render(doc)
            raw=(json.dumps(doc,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
            if len(raw)>60000 or len(report.encode())>60000:raise ValueError("small conclusion or process exceeded60000 bytes")
            save(a.out_dir/"process.json",doc);(a.out_dir/"conclusion.md").write_text(report)
        except BaseException as error:
            small={k:v for k,v in doc.items() if k not in ("complete_exact_inverse_column_conclusion",
                "complete_density_zero_operator_conclusion","complete_comparison_conclusions","complete_source_conclusion")}
            small["actual_scientific_returncode"]=actual
            small["formatting_failure"]=dict(type=type(error).__name__,message=str(error))
            small.update(complete=False,proved=False,actual_returncode=1)
            save(a.out_dir/"process.json",small)
            (a.out_dir/"conclusion.md").write_text("# Actual exact-column source formatting failure\n\n"
                "Original scientific child code: "+str(actual)+". Formatting is separate from mathematics.\n"
                "Temporary native SHA256: "+doc["temporary_native_sha256"]+"\n")
            actual=1
        print(json.dumps(dict(complete=doc["complete"],actual_returncode=actual,
            new_complete_comparisons=doc["new_complete_uniform_comparisons"],
            old_numerical_enclosures_recomputed=0,new_radial_integrals_computed=0,
            reproducible_data_published=False)),flush=True)
    return actual
if __name__=="__main__":raise SystemExit(main())
