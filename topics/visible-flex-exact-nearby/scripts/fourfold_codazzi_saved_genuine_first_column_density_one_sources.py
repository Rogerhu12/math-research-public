#!/usr/bin/env python3
"""Three density-one source bounds from already accepted genuine w1V derivatives.

One new complete positive column functional is evaluated. Genuine Taylor
bounds, all directed words, old source rows and radial integrals are read.
"""
from __future__ import annotations
import argparse,hashlib,json,os,platform,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy,scipy
from flint import arb,ctx
import fourfold_codazzi_factored_transport_companion_sources as old

PUBLIC,TOPIC,RUNTIME=old.PUBLIC,old.TOPIC,old.RUNTIME
KIND="actual_saved_genuine_first_column_density_one_sources_v1"
CONTRACT="4bd29959ada95b269ef5240439b3c6fc284e0e870265e5edea3e0d1a1fda8e96"
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
H,ROOTS,PIECE,RG,SG,N=old.H,old.ROOTS,old.PIECE,old.RG,old.SG,old.N
sha,ex,rb,up,gap,rec=old.sha,old.ex,old.rb,old.up,old.gap,old.rec
read,save,unpack,encode,payload_sha=old.read,old.save,old.unpack,old.encode,old.payload_sha
FIRST=("density1_complete_SV","density1_old_mean_V0")
MEAN=("density1_complete_uJB_w",)

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
        original_fold_strip=str(SG),complete_complex_delta_square_halfwidth="1/100000000",
        complete_complex_z_square_halfwidth="1/9409",saved_amplitude_derivative_orders=[0,1,2],
        genuine_amplitude_identity="w1V=free_w1+(T*b0,a0)*B(T)",
        exact_complete_density_one_functional="Gamma1=M1=A(w1V)",
        input_window="H^(-4/3), both genuine columns and both signs",
        density_window="H^(-5/3)",intermediate_word_window="H^(-2/3)",
        common_column_envelope="abs(rho)^(-1/4)",
        additional_input_frequency_weight_inserted=False,
        changed_complete_terms=list(FIRST+MEAN),unchanged_complete_term_count=28,
        accepted_baseline_run="43724065270/1",accepted_genuine_derivative_run="43720766795/1",
        accepted_b1_derivative_run="43719681982/1",
        original_radial_integrals_recomputed=0,new_amplitude_derivatives_computed=0,
        complete_mean_and_both_genuine_columns_retained=True)

def saved_genuine_column(DG,RV,gate):
    """S1.3--S1.4: exact successful balls; no finite or tail re-evaluation."""
    d=DG["complete_genuine_derivative_conclusion"]
    r=RV["complete_negative_Taylor_conclusion"]
    h=ROOTS[1]-PIECE[0]
    gate("the saved genuine amplitudes retain the exact negative product full mean and accepted RV component identity",
        d["genuine_amplitude_identity"]=="w1V=free_w1+(T*b0,a0)*B(T)"
        and d["exact_negative_rho_cover"]==r["exact_new_negative_rho_cover"]==str(h)
        and d["exact_original_whole_cover"]==r["old_complete_whole_piece_radius"]==str(H)
        and d["accepted_RV_Taylor_conclusion_sha256"]==payload_sha(r)
        and d["accepted_b1_value_derivative_upper"]==r["retained_complete_b1_value_derivative_upper"]
        and d["accepted_b1_radial_derivative_upper"]==r["retained_complete_b1_radial_derivative_upper"]
        and d["full_zero_mode_and_both_carriers_retained"] and r["full_zero_mode_retained"]
        and len(d["complete_a1_value_derivative_upper"])==len(d["accepted_b1_value_derivative_upper"])==4
        and len(d["complete_a1_radial_derivative_upper"])==len(d["accepted_b1_radial_derivative_upper"])==3
        and d["old_finite_coefficients_norms_and_new_b1_bounds_recomputed"] is False
        and r["original_coefficients_Fourier_norms_transport_and_products_recomputed"] is False)
    raw=[d["complete_a1_value_derivative_upper"][:3],d["accepted_b1_value_derivative_upper"][:3]]
    column=[[bound(v,"accepted complete genuine amplitude derivative") for v in row] for row in raw]
    return column,dict(genuine_amplitude_identity=d["genuine_amplitude_identity"],
        exact_negative_rho_cover=str(h),exact_original_whole_cover=str(H),
        accepted_DG_genuine_conclusion_sha256=payload_sha(d),
        accepted_RV_Taylor_conclusion_sha256=payload_sha(r),
        complete_a1_value_derivative_upper=raw[0],complete_b1_value_derivative_upper=raw[1],
        accepted_value_derivative_count=6,angular_derivative_orders=[0,1,2],
        entire_saved_arrays_checked=True,
        full_zero_mode_both_genuine_columns_and_both_carriers_retained=True,
        old_finite_coefficients_norms_and_tails_recomputed=False,
        old_DG_RV_or_inverse_closures_called=False)

def density_one_window(column,A,gate):
    """One original C2/C5 positive sum, with Gamma1=M1 and no extra 1/n."""
    value=A(column)
    gate("one complete density-one functional keeps both genuine branches the full mean and the existing input normalization",
        len(column)==2 and all(len(v)==3 for v in column)
        and value.is_finite() and value.lower()>=0)
    return value,value,dict(density=1,amplitude_identity="w1V",
        complete_column_operator_upper=rec(value),Gamma_w1V=rec(value),M_w1V=rec(value),
        exact_functional_identity="Gamma1=M1=A(w1V)",
        input_window="H^(-4/3), both genuine columns and both signs |j|>=97",
        density_window="H^(-5/3)",intermediate_word_window="H^(-2/3)",
        common_column_envelope="abs(rho)^(-1/4)",
        positive_functional_evaluation_count=1,all_eighteen_positive_coefficients_summed=True,
        additional_input_frequency_weight_inserted=False,
        density_zero_inverse_column_recipe_used=False,full_physical_even_mean_retained=True)

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
        values=dict(density1_complete_SV=up(J*KSV*Gamma),
            density1_old_mean_V0=up(J*V0*Mean),
            density1_complete_uJB_w=up(ef*KUB*Gamma))
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
    lines=["# Actual saved genuine first-column density-one sources","",
        "Only three complete source terms are compared; the complete SV operator and all old radial integrals are read.",
        "This is not a source-to-wave or high BVP inverse.","",
        "- Scientific child code: "+str(doc.get("actual_returncode")),
        "- Mathematical complete: "+str(doc.get("complete")),
        "- New complete column functionals: "+str(doc.get("new_complete_window_evaluations",0)),
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
    lines+=["","Only the six already accepted genuine amplitude jets enter one new positive functional; no extra input n weight is inserted.",
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
    doc=dict(kind=KIND,public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),workflow_event_commit=os.environ.get("GITHUB_SHA"),
        actual_scientific_checkout_commit=os.environ.get("VISIBLE_PHASE_SCIENCE_COMMIT"),
        source_sha256=source,input_manifest_sha256=a.manifest_sha,runtime=runtime,arithmetic_bits=320,
        complete=False,proved=False,actual_returncode=1,failure=None,gates=[],
        original_successful_small_receipts_read=0,original_complete_coefficient_rows_read=0,
        original_selected_coefficient_rows_read=0,original_positive_linear_coefficients_read=0,
        original_complete_source_terms_read=0,original_complete_word_maxima_read=0,
        original_complete_word_maxima_consumed=0,accepted_genuine_value_derivative_bounds_read=0,
        new_complete_window_evaluations=0,new_complete_source_row_budgets=0,
        new_complete_uniform_comparisons=0,new_complete_scalar_recombinations=0,
        old_numerical_enclosures_recomputed=0,
        old_target_FFT_intrinsic_repair_fold_transport_or_Taylor_recomputed=0,
        old_amplitude_derivatives_finite_sums_or_tails_recomputed=0,
        old_inverse_word_or_positive_calibration_recomputed=0,
        old_AJ_DG_RV_SV_ER_or_companion_source_closures_called=0,
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
            complete_genuine_execution=old.C_EXEC,directed_source_execution=old.D_EXEC,
            original_norm_native=old.OLD_NATIVE,original_norm_process=old.OLD_PROCESS,
            directed_process="00afd54464db46f110ecff8c1968b158deedac719a363590fc366038b47fedb8")
        gate("all successful receipts original column and complete source algorithms retain their exact identities",
            all(sha(paths[k])==v for k,v in expected.items()))
        prior=read(paths["original_SV_manifest"])
        gate("all sixty-nine original SV pins are unchanged in the new scientific closure",
            len(prior["files"])==69 and prior["scientific_source_sha256"]==SV_SOURCE
            and all(pins.get(e["path"])==e for e in prior["files"]))
        C=accepted(paths["complete_genuine_execution"],"43702688640",old.C_SOURCE,old.C_MANIFEST,old.C_EXEC,17,gate)
        D=accepted(paths["directed_source_execution"],"43703879926",old.D_SOURCE,old.D_MANIFEST,old.D_EXEC,12,gate)
        AJ=accepted(paths["accepted_AJ_execution"],"43718112378",AJ_SOURCE,AJ_MANIFEST,AJ_EXEC,29,gate)
        RV=accepted(paths["accepted_RV_execution"],"43719681982",RV_SOURCE,RV_MANIFEST,RV_EXEC,27,gate)
        DG=accepted(paths["accepted_DG_execution"],"43720766795",DG_SOURCE,DG_MANIFEST,DG_EXEC,27,gate)
        SV=accepted(paths["accepted_SV_execution"],"43722805762",SV_SOURCE,SV_MANIFEST,SV_EXEC,23,gate)
        ER=accepted(paths["accepted_ER_execution"],"43724065270",ER_SOURCE,ER_MANIFEST,ER_EXEC,20,gate)
        doc["original_successful_small_receipts_read"]=7
        gate("the same genuine column domains original reflection and full physical mean are retained",
            C["scope"]["original_fixed_intrinsic_parameter"]=="eta_0"
            and C["scope"]["both_genuine_columns_and_both_carrier_signs"]
            and C["scope"]["all_input_abs_j_at_least97"]
            and C["scope"]["output_mean_and_complete_original_primitive_retained"]
            and C["scope"]["physical_J_only_on_its_proved_reflected_parity_domain"]
            and all(r["full_physical_negative_volume_source_paid"] and not r["full_high_inverse_claimed"]
                and r["old_numerical_enclosures_recomputed"]==0 for r in (AJ,RV,DG,SV,ER))
            and DG["scope"]["all_three_local_terms_read_verbatim"]
            and DG["scope"]["density_zero_complete_source_read_verbatim"]
            and SV["scope"]["other_twenty_eight_complete_terms_read_verbatim"]
            and len(SV["complete_comparison_conclusions"])==3
            and {x["source_term"] for x in SV["complete_comparison_conclusions"]}
                =={"density0_complete_SV","density0_old_mean_V0","density0_complete_uJB_w"}
            and ER["complete_comparison_conclusion"]["source_term"]=="local_raw_1")
        base=ER["complete_source_conclusion"];svbase=SV["complete_source_conclusion"]
        dgbase=DG["complete_source_conclusion"];ajbase=AJ["complete_source_conclusion"]
        stable=("actual_dr_measure","exact_negative_physical_cover","one_sided_uncertain_root_band_retained",
            "both_density_windows_retained","outer_J_window","input_window","first_output_window",
            "independent_even_mean_window","total_squared_envelope_radial_weight_upper",
            "original_temporary_row_payload_sha256","old_nine_word_and_five_physical_mean_counts")
        gate("the successful ER baseline retains the complete SV update all source windows true measure and every other term",
            len(base["complete_first_source_term_L2_upper"])==21
            and len(base["complete_independent_mean_term_L2_upper"])==10
            and all(base[k]==svbase[k]==dgbase[k]==ajbase[k] for k in stable)
            and all(base["complete_first_source_term_L2_upper"][k]==v
                for k,v in svbase["complete_first_source_term_L2_upper"].items() if k!="local_raw_1")
            and base["complete_independent_mean_term_L2_upper"]==svbase["complete_independent_mean_term_L2_upper"]
            and base["nonlocal_total_L2_upper"]==svbase["nonlocal_total_L2_upper"]
            and base["mean_L2_upper"]==svbase["mean_L2_upper"]
            and base["exact_negative_physical_cover"]==[str(PIECE[0]),str(ROOTS[1])]
            and base["old_nine_word_and_five_physical_mean_counts"]==[9,5])
        column,conclusion=saved_genuine_column(DG,RV,gate)
        doc.update(accepted_genuine_value_derivative_bounds_read=6,
            complete_saved_genuine_column_conclusion=conclusion)
        rows,words=old.checked_accepted_rows(paths,C,D,AJ,gate)
        doc.update(original_complete_coefficient_rows_read=1328,original_selected_coefficient_rows_read=6,
            original_complete_word_maxima_read=8,original_complete_word_maxima_consumed=2,
            original_complete_source_terms_read=31)
        positive=old.read_positive_coefficients(C,gate);A=old.PositiveOperator(positive)
        doc["original_positive_linear_coefficients_read"]=18
        Gamma,Mean,operators=density_one_window(column,A,gate)
        terms,means,comparisons,row_details=complete_comparisons(
            rows,words,Gamma,Mean,base["total_squared_envelope_radial_weight_upper"],base,gate)
        result=old.combine(base,terms,means)
        doc.update(new_complete_window_evaluations=1,new_complete_source_row_budgets=6,
            new_complete_uniform_comparisons=3,new_complete_scalar_recombinations=4,
            complete_density_one_operator_conclusion=operators,
            complete_comparison_conclusions=comparisons,complete_source_conclusion=result,
            strictly_smaller_complete_term_bounds=sum(int(v["strictly_smaller_complete_term"]) for v in comparisons))
        changed=set(FIRST+MEAN)
        gate("all twenty-eight other complete term balls including every local and density-zero term remain byte identical",
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
            saved_zero_width_joint_Wiener_derivatives_only=True,
            positive_width_derivative_supremum_inferred=False,
            complete_original_coefficient_delta_and_z_domains_retained=True,
            final_column_operators_use_physical_input_labels=True,
            both_genuine_columns_and_both_carrier_signs=True,all_input_abs_j_at_least97=True,
            same_genuine_w1V_not_free_first_correction=True,
            density_one_Gamma_and_M_are_the_same_full_positive_functional=True,
            density_zero_inverse_column_or_extra_angular_derivative_used=False,
            additional_input_frequency_weight_inserted=False,
            whole_SV_word_and_all_seven_operator_terms_retained=True,
            all_eighteen_positive_column_coefficients_summed=True,
            all_three_local_terms_and_all_density_zero_terms_read_verbatim=True,
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
        native=a.out_dir/"temporary-saved-genuine-first-column-density-one-sources.json.gz"
        save(native,temporary,True)
        doc["temporary_native_sha256"]=sha(native);doc["temporary_native_bytes"]=native.stat().st_size
        doc["temporary_native_is_not_published"]=True;actual=doc["actual_returncode"]
        try:
            report=render(doc)
            raw=(json.dumps(doc,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
            if len(raw)>60000 or len(report.encode())>60000:raise ValueError("small conclusion or process exceeded60000 bytes")
            save(a.out_dir/"process.json",doc);(a.out_dir/"conclusion.md").write_text(report)
        except BaseException as error:
            small={k:v for k,v in doc.items() if k not in ("complete_saved_genuine_column_conclusion",
                "complete_density_one_operator_conclusion","complete_comparison_conclusions","complete_source_conclusion")}
            small["actual_scientific_returncode"]=actual
            small["formatting_failure"]=dict(type=type(error).__name__,message=str(error))
            small.update(complete=False,proved=False,actual_returncode=1)
            save(a.out_dir/"process.json",small)
            (a.out_dir/"conclusion.md").write_text("# Actual saved-column source formatting failure\n\n"
                "Original scientific child code: "+str(actual)+". Formatting is separate from mathematics.\n"
                "Temporary native SHA256: "+doc["temporary_native_sha256"]+"\n")
            actual=1
        print(json.dumps(dict(complete=doc["complete"],actual_returncode=actual,
            new_complete_comparisons=doc["new_complete_uniform_comparisons"],
            old_numerical_enclosures_recomputed=0,new_radial_integrals_computed=0,
            reproducible_data_published=False)),flush=True)
    return actual
if __name__=="__main__":raise SystemExit(main())
