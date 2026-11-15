#!/usr/bin/env python3
"""New AJ angular-jet closure and complete companion-source comparison.

Only the new scalar AJ closure and its complete source consequences are
evaluated. The accepted factored-source cT/Xi/breg moduli, inverse remainder,
all31 source terms, original profile coefficients and radial weight are read.
No accepted source pipeline, fold, target, transport or integral is rerun.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,math,os,platform,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy,scipy
from flint import arb,ctx
import fourfold_codazzi_factored_transport_companion_sources as old

PUBLIC=old.PUBLIC
TOPIC=old.TOPIC
KIND="actual_angular_jets_retained_radial_part_complete_sources_v1"
CONTRACT="afeab1525bbb505432269005040107378d50741bfe5ca2c0494effcafe3f6d5a"
FACTORED_CONTRACT=old.CONTRACT
FACTORED_SOURCE="a705c2b4c64393e3ba1ae1e043d0fbd62f516a7a80e03e47ce11820626373ee7"
FACTORED_MANIFEST="bbfbdbc206f4d724288f8ecb5d9613523f5103ae7c1276ff59f2aaa055476665"
FACTORED_EXECUTION="5e5f414a53404f122fbe7c5f5ae073a86402305a7485a6afd44cda940ca5902c"
FACTORED_RUN="43714194714"
H,RG,SG,SP,SB,SW,RT,SA,N=old.H,old.RG,old.SG,old.SP,old.SB,old.SW,old.RT,old.SA,old.N
ROOTS,PIECE,RUNTIME=old.ROOTS,old.PIECE,old.RUNTIME
sha,ex,rb,up,gap,bound,powr,rec=old.sha,old.ex,old.rb,old.up,old.gap,old.bound,old.powr,old.rec
read,save,unpack,encode,payload_sha=old.read,old.save,old.unpack,old.encode,old.payload_sha
add,scale,mul,product,cauchy=old.add,old.scale,old.mul,old.product,old.cauchy

def recurrence(initial,zeta,factor,order):
    """Ordinary derivatives of an exact first-order angular identity."""
    values=[bound(initial,"complete angular recurrence order zero")]
    for n in range(order):
        values.append(up(ex(factor)*sum(
            (math.comb(n,j)*values[j]*zeta[n-j] for j in range(n+1)),arb(0))))
    return values

def complete_min(a,b):
    # Both arguments bound the same complete scalar derivative.
    return min(bound(a,"complete scalar comparison"),bound(b,"complete scalar comparison")).upper()

def angular_closure(f,c,accepted,gate):
    """AJ.13--25, with distinct inner and full-radius reciprocal-Q jets."""
    domain=accepted["complete_domain_conclusion"]
    gate("the accepted scalar domain and complete old order-zero moduli are read without rerunning their producer",
        Q(domain["exact_full_physical_cover"])==H
        and Q(domain["exact_original_fold_radius"])==RG
        and Q(domain["exact_original_fold_strip"])==SG
        and Q(domain["exact_physical_phi_strip"])==SP
        and Q(domain["exact_accepted_canonical_radius"])==RT
        and Q(domain["exact_accepted_canonical_strip"])==SA
        and domain["exact_regular_root_condition"]=="B(0,X)=fb(0,X)"
        and domain["all_sT_segments_in_accepted_product"]
        and domain["physical_T_image_definition_read_from_frozen_producer"]
        and domain["full_mean_and_radial_G_scalar_retained"]
        and domain["old_image_fold_forcing_and_amplitude_enclosures_recomputed"] is False)
    Am=gap(f["Am"],"the complete original A modulus")
    Ap=bound(f["Ap"],"the complete original A upper")
    amin=gap(c["am"],"the complete nonzero characteristic a modulus")
    principal=gap(f["gap"],"the saved complete Bplus modulus lower")
    margin=gap(ex(RG-H),"the full outer-to-inner radial Cauchy margin")
    if len(c["D"])<5:raise ValueError("the complete drift table omits an angular derivative")
    D=[bound(c["D"][j],"complete drift derivative "+str(j)) for j in range(5)]
    t0=bound(c["T0"],"complete T0, hence its retained radial mean")
    tau=ex(H/RG)
    smallx=up(tau*bound(f["j"],"complete x minus one"))
    Y0=up(tau*tau*bound(f["BT"],"complete y root-zero coefficient"))
    Zouter=up(ex(Q(2,3))*bound(f["BA"],"complete A_phi")/Am)
    Zinner=up(tau*Zouter)
    X=cauchy(smallx,SG,4);X[0]=up(1+smallx)
    Y=cauchy(Y0,SG,4)
    Z=cauchy(Zinner,SG,4);Zbar=cauchy(Zouter,SG,4)
    T=[bound(domain["accepted_complete_physical_T_image"],"accepted whole-strip T image")]+Y[:4]
    F0=up(powr(Ap,Q(1,3))/amin)
    F=recurrence(F0,Z,Q(1,2),4)
    Fbar=recurrence(F0,Zbar,Q(1,2),3)
    L=[]
    for n in range(4):
        drift=sum((math.comb(n,j)*D[j]*F[n-j+1] for j in range(n+1)),arb(0))
        mean_drift=sum((math.comb(n,j)*D[j+1]*F[n-j] for j in range(n+1)),arb(0))
        L.append(up(Fbar[n]/margin+drift+t0*F[n]+4*mean_drift))
    Bplus=add(mul(X,X,4),product(T,Y,Y,k=4),k=4)
    invB=[up(1/principal)]
    for n in range(1,5):
        invB.append(up(sum((math.comb(n,j)*Bplus[j]*invB[n-j]
                           for j in range(1,n+1)),arb(0))/principal))
    numerator_c=add(mul(L,X,3),scale(mul(Y,Y,3),Q(1,2),3),k=3)
    numerator_xi=add(mul(L,Y,3),scale(mul(X,Z,3),Q(1,2),3),k=3)
    old_c=bound(domain["complete_cT_holomorphic_upper"],"accepted complete cT modulus")
    old_xi=bound(domain["complete_Xi_holomorphic_upper"],"accepted complete Xi modulus")
    old_breg=bound(domain["complete_regular_breg_modulus"],"accepted complete regular quotient modulus")
    old_C=cauchy(old_c,SG,3);old_E=cauchy(old_xi,SG,3)
    C=[complete_min(old_c,up(numerator_c[0]/principal))]
    E=[complete_min(old_xi,up(numerator_xi[0]/principal))]
    new_uncompared_C=[up(numerator_c[0]/principal)]
    new_uncompared_E=[up(numerator_xi[0]/principal)]
    for n in range(1,4):
        cn=up((numerator_c[n]+sum(
            (math.comb(n,j)*Bplus[j]*C[n-j] for j in range(1,n+1)),arb(0)))/principal)
        en=up((numerator_xi[n]+sum(
            (math.comb(n,j)*Bplus[j]*E[n-j] for j in range(1,n+1)),arb(0)))/principal)
        new_uncompared_C.append(cn);new_uncompared_E.append(en)
        C.append(complete_min(cn,old_C[n]));E.append(complete_min(en,old_E[n]))
    q0=bound(f["Q"],"complete original Q")
    g0=bound(f["G"],"complete original G with its full radial mean integral")
    # Q and G are needed in the unchanged rank/principal identities.
    q=recurrence(q0,Z,Q(1,2),4)
    g=recurrence(g0,Z,Q(1,4),4)
    prefactor=recurrence(up(q0*g0/2),Z,Q(1,4),4)
    invG=recurrence(bound(f["Gi"],"complete inverse G"),Z,Q(1,4),3)
    factor=mul(prefactor,Bplus,4)
    diagonal=add(mul(X,X,3),product(T,Y,Y,k=3),k=3)
    lower=scale(mul(X,Y,3),2,3)
    upper=scale(product(T,X,Y,k=3),2,3)
    common=product(invG,invB,invB,k=3)
    inv_diag=mul(common,diagonal,3)
    inverse=[[inv_diag,mul(common,upper,3)],[mul(common,lower,3),list(inv_diag)]]
    breg=cauchy(old_breg,SP,3)
    result=dict(x=X,y=Y,zeta=Z,T=T,Q=q,G=g,Bplus=Bplus,factor=factor,
        cT=C,Xi=E,breg=breg,M_inverse=inverse,complete_T_modulus=T[0])
    gate("the AJ closure retains the radial mean outer reciprocal jets and full nonradial inverse in the actual product",
        0<H<RG and 0<SP<SB<SG
        and len(F)==5 and len(Fbar)==4 and len(D)==5
        and all(v.is_finite() and v.lower()>=0 for arr in
            (X,Y,Z,Zbar,T,F,Fbar,L,Bplus,invB,C,E,q,g,prefactor,invG,factor,breg)
            for v in arr)
        and all(v.is_finite() and v.lower()>=0 for row in inverse for arr in row for v in arr))
    conclusion=dict(
        exact_original_fold_radius=str(RG),exact_original_fold_strip=str(SG),
        exact_full_physical_cover=str(H),exact_physical_phi_strip=str(SP),
        accepted_factored_source_run=FACTORED_RUN+"/1",
        accepted_order_zero_domain_read_verbatim=domain,
        complete_positive_A_modulus=rec(Am),complete_positive_characteristic_a_modulus=rec(amin),
        complete_positive_Bplus_modulus=rec(principal),complete_radial_Cauchy_margin=rec(margin),
        exact_mu_identity="Q^2*(x^2+T*y^2)",
        exact_radial_mean_identity="T0=t(r)+5*d_phi",
        exact_reciprocal_identity="F_phi=F*zeta/2",
        complete_cT_angular_derivative_upper=encode(C),
        complete_Xi_angular_derivative_upper=encode(E),
        complete_scalar_derivative_comparisons_only=True,
        all_inverse_matrix_entries_and_means_retained=True,
        old_regular_quotient_or_inverse_remainder_recomputed=False,
        old_fold_coefficient_or_original_pipeline_recomputed=False)
    temporary=dict(inner_F=F,outer_F=Fbar,outer_zeta=Zbar,full_L_numerators=L,
        cT_numerator=numerator_c,Xi_numerator=numerator_xi,
        unselected_complete_cT_derivative_upper=new_uncompared_C,
        unselected_complete_Xi_derivative_upper=new_uncompared_E,
        full_Bplus_inverse=invB,complete_prefactor_before_Bplus=prefactor,
        complete_inverse_G=invG,new_complete_supporting_coefficients=result)
    return result,conclusion,temporary

def read_inverse_remainder(accepted,gate):
    value=accepted["complete_inverse_remainder_conclusion"]
    derivative=value["complete_real_remainder_derivative_upper"]
    gate("the identified complete inverse-remainder conclusion is read verbatim without recovering the old minimum again",
        value["exact_Wiener_phi_strip"]==str(SW)
        and value["exact_constant_minus_i_epsilon_identity_retained"]
        and value["branch_lower_is_algorithm_number_not_function_lower"]
        and value["original_inverse_or_Fourier_conversion_recomputed"] is False
        and len(derivative)==4)
    return [bound(v,"accepted inverse remainder angular derivative") for v in derivative],value

def params():
    p=old.params()
    p.update(baseline_complete_source_run=FACTORED_RUN+"/1",
        new_AJ_contract_sha256=CONTRACT,new_AJ_scalar_closures=1,
        inner_reciprocal_Q_derivative_orders=[0,1,2,3,4],
        full_radius_reciprocal_Q_derivative_orders=[0,1,2,3],
        complete_Bplus_inverse_derivative_orders=[0,1,2,3,4],
        complete_cT_and_Xi_derivative_orders=[0,1,2,3],
        complete_leading_matrix_inverse_derivative_orders=[0,1,2,3],
        accepted_cT_Xi_breg_and_inverse_remainder_read_without_recomputation=True,
        accepted_source_pipeline_or_radial_integrals_rerun=False)
    return p

FACTOR_CONTRACT=old.FACTOR_CONTRACT
MAJORANTS=old.MAJORANTS
APROC=old.APROC
APUB=old.APUB
LEGACY_SOURCE=old.LEGACY_SOURCE
LEGACY_HELPER=old.LEGACY_HELPER
LEGACY_MANIFEST=old.LEGACY_MANIFEST
S_EXEC=old.S_EXEC
S_SOURCE=old.S_SOURCE
S_MANIFEST=old.S_MANIFEST
C_EXEC=old.C_EXEC
C_SOURCE=old.C_SOURCE
C_MANIFEST=old.C_MANIFEST
D_EXEC=old.D_EXEC
D_SOURCE=old.D_SOURCE
D_MANIFEST=old.D_MANIFEST
G_EXEC=old.G_EXEC
G_SOURCE=old.G_SOURCE
G_MANIFEST=old.G_MANIFEST
P_EXEC=old.P_EXEC
P_SOURCE=old.P_SOURCE
P_MANIFEST=old.P_MANIFEST
B_EXEC=old.B_EXEC
B_SOURCE=old.B_SOURCE
B_MANIFEST=old.B_MANIFEST
H_EXEC=old.H_EXEC
H_SOURCE=old.H_SOURCE
H_MANIFEST=old.H_MANIFEST
OLD_NATIVE=old.OLD_NATIVE
OLD_PROCESS=old.OLD_PROCESS
OLD_SOURCE=old.OLD_SOURCE
OLD_MANIFEST=old.OLD_MANIFEST
ROOT_SHA=old.ROOT_SHA
FORCE_SHA=old.FORCE_SHA
RF=old.RF
receipt=old.receipt
checked_accepted_rows=old.checked_accepted_rows
read_positive_coefficients=old.read_positive_coefficients
PositiveOperator=old.PositiveOperator
read_real_jets=old.read_real_jets
complete_factored_sources=old.complete_factored_sources
complete_companion_comparisons=old.complete_companion_comparisons
combine=old.combine

def render(doc):
    text=old.render(doc).replace(
        "# Actual factored transport and companion complete-source comparison",
        "# Actual retained-radial angular jets and complete source bounds")
    angular=doc.get("complete_AJ_angular_derivative_conclusion")
    if angular:
        text+="\n## New AJ scalar derivative conclusions\n\n"
        text+="The old radial mean, full principal inverse, original root branch and all means are retained.\n\n"
        text+="| Ordinary angular derivative | Complete cT upper | Complete Xi upper |\n|---|---|---|\n"
        for i,(c,x) in enumerate(zip(angular["complete_cT_angular_derivative_upper"],
                                    angular["complete_Xi_angular_derivative_upper"])):
            text+="| "+str(i)+" | "+c["ball"]+" | "+x["ball"]+" |\n"
        text+="\nThe old zero-order quotient and inverse-remainder conclusions were read; their successful algorithms were not rerun.\n"
        text+="All local terms and all undeclared terms are unchanged from run "+FACTORED_RUN+"/1.\n"
    return text

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo",type=Path,required=True);p.add_argument("--manifest",type=Path,required=True)
    p.add_argument("--manifest-sha",required=True);p.add_argument("--out-dir",type=Path,required=True)
    a=p.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("all new mathematical arithmetic requires this public Actions repository")
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
        original_complete_coefficient_rows_read=0,original_selected_coefficient_rows_read=0,
        original_positive_linear_coefficients_read=0,original_complete_source_terms_read=0,
        original_complete_word_maxima_read=0,original_complete_word_maxima_consumed=0,
        new_supporting_factor_jet_closures=0,new_complete_regular_quotient_budgets=0,
        new_complete_factored_density_source_budgets=0,new_identified_inverse_remainder_recoveries=0,
        new_complete_companion_row_budgets=0,new_complete_window_evaluations=0,
        new_complete_uniform_comparisons=0,new_complete_scalar_recombinations=0,
        old_numerical_enclosures_recomputed=0,old_target_FFT_intrinsic_repair_fold_transport_or_Taylor_recomputed=0,
        old_RF_forcing_amplitude_or_profile_enclosures_recomputed=0,
        old_inverse_word_or_positive_calibration_recomputed=0,old_source_row_or_radial_integral_recomputed=0,
        new_radial_integrals_computed=0,original_natural_stage_bytes_modified=0,
        new_AJ_angular_jet_closures=0,
        accepted_regular_quotient_order_zero_recomputed=0,
        accepted_inverse_remainder_recovery_repeated=0,
        accepted_factored_source_pipeline_invocations=0,
        full_physical_negative_volume_source_paid=False,full_high_inverse_claimed=False,
        reproducible_outputs_published_to_repository=False,reproducible_outputs_uploaded_to_Releases=False,
        new_reproducible_data_artifact_uploaded=False)
    temporary={}
    def gate(name,condition):
        doc["gates"].append(dict(name=name,passed=bool(condition)))
        if not condition:raise ValueError(name)
    try:
        manifest=read(a.manifest);parameters=params();doc["mathematical_parameters"]=parameters
        if sha(old.__file__)!=FACTORED_SOURCE:
            raise ValueError("the imported completed scalar recipe changed")
        gate("the source manifest exact products and new-only scalar scope have their reviewed identities",
            sha(a.manifest)==a.manifest_sha and manifest["public_repository"]==PUBLIC
            and manifest["scientific_source_sha256"]==source and manifest["mathematical_parameters"]==parameters)
        pins={e["path"]:e for e in manifest["files"]}
        if len(pins)!=len(manifest["files"]):raise ValueError("duplicate immutable input")
        for e in manifest["files"]:
            rel=Path(e["path"]);f=a.repo/rel
            if rel.is_absolute() or ".." in rel.parts or not str(rel).startswith(TOPIC):
                raise ValueError("an immutable input left the topic")
            if not f.is_file() or f.stat().st_size!=e["bytes"] or sha(f)!=e["sha256"]:
                raise ValueError("changed exact input "+str(rel))
        if any(v not in pins for v in manifest["input_paths"].values()):raise ValueError("an input role is not pinned")
        paths={k:a.repo/v for k,v in manifest["input_paths"].items()}
        expected=dict(contract=CONTRACT,factor_contract=FACTOR_CONTRACT,
            factored_contract=FACTORED_CONTRACT,original_factored_algorithm=FACTORED_SOURCE,
            original_factored_manifest=FACTORED_MANIFEST,accepted_factored_execution=FACTORED_EXECUTION,
            old_fold_majorants_stage=MAJORANTS,adjacent_process=APROC,adjacent_publication=APUB,
            amplitude_execution=S_EXEC,operator_execution=G_EXEC,complete_genuine_execution=C_EXEC,
            directed_source_execution=D_EXEC,first_local_execution=P_EXEC,
            refined_first_local_execution=B_EXEC,columns_execution=H_EXEC,
            original_norm_native=OLD_NATIVE,original_norm_process=OLD_PROCESS,
            original_scalar_algorithm=S_SOURCE,original_operator_algorithm=G_SOURCE,
            complete_genuine_source=C_SOURCE,directed_source_algorithm=D_SOURCE,
            original_first_local_algorithm=P_SOURCE,refined_first_local_algorithm=B_SOURCE,
            original_inverse_algorithm=H_SOURCE,
            directed_process="00afd54464db46f110ecff8c1968b158deedac719a363590fc366038b47fedb8",
            original_fold_algorithm="410675cf78dd30d97ff052558df1a819977291d40c628211fcf623ffc0b5f783")
        gate("all seven accepted scientific receipts and every frozen source and legacy byte identity are exact",
            all(sha(paths[k])==v for k,v in expected.items()))
        prior_manifest=read(paths["original_factored_manifest"])
        gate("every original factored-source manifest pin remains unchanged in the new input closure",
            all(pins.get(e["path"])==e for e in prior_manifest["files"])
            and len(prior_manifest["files"])==44
            and prior_manifest["scientific_source_sha256"]==FACTORED_SOURCE)
        ms=read(paths["old_fold_majorants_stage"]);ap=read(paths["adjacent_process"]);au=read(paths["adjacent_publication"])
        publication=[v for v in au["files"] if v["file"]=="consumers/stages/complete-original-reference-holomorphic-majorants.json.gz"]
        if len(publication)!=1:raise ValueError("the original natural fold receipt is not unique")
        mr=publication[0]
        gate("the complete fold and physical background retain their exact legacy payload and successful publication",
            ms["complete"] and ms["name"]==ms["stage"]=="complete-original-reference-holomorphic-majorants"
            and ms["source_sha256"]==LEGACY_SOURCE and ms["algebra_sha256"]==LEGACY_HELPER
            and ms["input_manifest_sha256"]==LEGACY_MANIFEST and ms["runtime"]==runtime
            and mr["bytes"]==4501 and mr["sha256"]==MAJORANTS
            and ap["actual_returncode"]==0 and ap["mathematical_complete"] and ap["mathematical_proved"]
            and ap["mathematical_failure"] is None and au["complete"]
            and all(ms["payload"]["majorants"][k][1:]==[str(RG),str(SG)] for k in ("A","chi")))
        saved_fold=unpack(ms["payload"]);fold=saved_fold["fold"];coefficient=saved_fold["coefficients"]
        doc["original_complete_fold_stages_read"]=1
        S=receipt(paths["amplitude_execution"],"43698106023",S_SOURCE,S_MANIFEST,gate)
        G=receipt(paths["operator_execution"],"43700281022",G_SOURCE,G_MANIFEST,gate)
        C=receipt(paths["complete_genuine_execution"],"43702688640",C_SOURCE,C_MANIFEST,gate)
        D=receipt(paths["directed_source_execution"],"43703879926",D_SOURCE,D_MANIFEST,gate)
        P=receipt(paths["first_local_execution"],"43709396175",P_SOURCE,P_MANIFEST,gate)
        B=receipt(paths["refined_first_local_execution"],"43711480764",B_SOURCE,B_MANIFEST,gate)
        Hr=receipt(paths["columns_execution"],"43688459733",H_SOURCE,H_MANIFEST,gate)
        accepted=receipt(paths["accepted_factored_execution"],FACTORED_RUN,FACTORED_SOURCE,FACTORED_MANIFEST,gate)
        doc["original_successful_small_receipts_read"]=8
        gate("the completed factored source retains all25 gates its full31-term result and zero old recomputation",
            len(accepted["gates"])==25 and accepted["full_physical_negative_volume_source_paid"]
            and accepted["old_numerical_enclosures_recomputed"]==0
            and accepted["old_source_row_or_radial_integral_recomputed"]==0
            and accepted["new_radial_integrals_computed"]==0
            and accepted["new_complete_uniform_comparisons"]==10
            and accepted["scope"]["both_complete_directed_word_windows_retained"]
            and accepted["scope"]["all_actual_physical_seams_and_reference_matching_sources_retained"]
            and accepted["full_high_inverse_claimed"] is False)
        sd=S["complete_domain_conclusion"];family=C["scope"];base=B["complete_source_conclusion"]
        gate("the full original complex squares fixed intrinsic root genuine signs and physical mean are unchanged",
            sd["exact_original_physical_piece_interval"]==list(map(str,PIECE))
            and sd["exact_original_true_root_interval"]==list(map(str,ROOTS))
            and Q(sd["true_physical_root_piece_radius"])==H
            and sd["same_potential_T_segment_proved"] and sd["actual_inverseimage_and_both_regular_paths_proved"]
            and S["scope"]["original_root_piece_2549_only"] and S["scope"]["full_complex_delta_square"]
            and S["scope"]["full_z_square_all_abs_j_ge97"] and S["scope"]["both_carrier_signs"]
            and family["original_fixed_intrinsic_parameter"]=="eta_0"
            and family["same_original_real_explicit_family"]
            and family["both_genuine_columns_and_both_carrier_signs"] and family["all_input_abs_j_at_least97"]
            and family["output_mean_and_complete_original_primitive_retained"]
            and family["physical_J_only_on_its_proved_reflected_parity_domain"]
            and [len(r["gates"]) for r in (S,G,C,D,P,B,Hr)]==[26,16,17,12,13,19,16]
            and C["full_physical_negative_volume_source_paid"] and not C["full_high_inverse_claimed"])
        stable=("actual_dr_measure","exact_negative_physical_cover","one_sided_uncertain_root_band_retained",
            "both_density_windows_retained","outer_J_window","input_window","first_output_window",
            "independent_even_mean_window","total_squared_envelope_radial_weight_upper",
            "nonlocal_total_L2_upper","mean_L2_upper","complete_independent_mean_term_L2_upper")
        ledgers=[r["complete_source_conclusion"] for r in (D,P,B)]
        gate("the latest refined local ledger is retained with all original nonlocal terms and source windows",
            len(base["complete_first_source_term_L2_upper"])==21
            and len(base["complete_independent_mean_term_L2_upper"])==10
            and all(ledgers[0][k]==ledgers[1][k]==ledgers[2][k] for k in stable)
            and all(v==base["complete_first_source_term_L2_upper"][k]
                ==ledgers[1]["complete_first_source_term_L2_upper"][k]
                for k,v in ledgers[0]["complete_first_source_term_L2_upper"].items() if k!="local_raw_1")
            and base["old_nine_word_and_five_physical_mean_counts"]==[9,5]
            and base["exact_negative_physical_cover"]==[str(PIECE[0]),str(ROOTS[1])]
            and base["only_complete_first_local_vector_replaced"]
            and B["new_complete_wrr_derivative_bounds"]==6
            and B["old_numerical_enclosures_recomputed"]==0)
        previous_base=base;base=accepted["complete_source_conclusion"]
        changed={v["source_term"] for v in accepted["complete_comparison_conclusions"]}
        stable_keys=("actual_dr_measure","exact_negative_physical_cover",
            "one_sided_uncertain_root_band_retained","both_density_windows_retained",
            "outer_J_window","input_window","first_output_window","independent_even_mean_window",
            "total_squared_envelope_radial_weight_upper","original_temporary_row_payload_sha256",
            "local_L2_upper","old_nine_word_and_five_physical_mean_counts")
        gate("the latest complete factored ledger preserves the three local terms all means and exact six-row measure",
            len(changed)==10 and len(base["complete_first_source_term_L2_upper"])==21
            and len(base["complete_independent_mean_term_L2_upper"])==10
            and all(base[k]==previous_base[k] for k in stable_keys)
            and all(base["complete_first_source_term_L2_upper"][k]==v
                for k,v in previous_base["complete_first_source_term_L2_upper"].items() if k not in changed)
            and all(base["complete_independent_mean_term_L2_upper"][k]==v
                for k,v in previous_base["complete_independent_mean_term_L2_upper"].items() if k not in changed))
        # Bind the claimed domain to the exact frozen producer statements. This
        # is textual provenance checking, not reevaluation of their arithmetic.
        ps=paths["original_first_local_algorithm"].read_text()
        fs=paths["original_fold_algorithm"].read_text()
        bs=paths["refined_first_local_algorithm"].read_text()
        gate("the saved T image uses the whole SG fold modulus and M Bi B2 share the accepted canonical inverse product",
            'imageT=up(ex(H)*powr(Ap,Q(2,3)))' in ps
            and 'Ap=bound(f["Ap"],"old A modulus")' in ps
            and 'exact_canonical_radius=str(LAM*R/2),exact_canonical_width=str(SF)' in fs
            and 'SG=Q(3,128);SF=Q(1,64)' in fs and 'LAM=Q(9,2)' in fs
            and 'M=bound(f["M"],"complete canonical leading coefficient")' in bs
            and 'Bi=bound(f["Bi"],"complete inverse leading branch")' in bs
            and RT<Q(9,4)*RG and SA<SB
            and rb(B["complete_domain_conclusion"]["complete_domain_gaps"]["original_inverse_radius"]).lower()>0
            and saved_fold["majorants"]["A"][1:]==[str(RG),str(SG)])
        rows,words=checked_accepted_rows(paths,C,D,accepted,gate)
        doc.update(original_complete_coefficient_rows_read=1328,original_selected_coefficient_rows_read=6,
            original_complete_word_maxima_read=8,original_complete_word_maxima_consumed=3,
            original_complete_source_terms_read=31)
        positive=read_positive_coefficients(C,gate);A=PositiveOperator(positive)
        doc["original_positive_linear_coefficients_read"]=18
        jets=read_real_jets(S,G,gate)
        factors,angular,aj_temporary=angular_closure(fold,coefficient,accepted,gate)
        doc.update(new_supporting_factor_jet_closures=1,new_AJ_angular_jet_closures=1,
            new_complete_regular_quotient_budgets=0,
            complete_domain_conclusion=accepted["complete_domain_conclusion"],
            complete_AJ_angular_derivative_conclusion=angular)
        sources,factor_temp=complete_factored_sources(factors,jets,Hr,gate)
        doc["new_complete_factored_density_source_budgets"]=2
        delta,remainder=read_inverse_remainder(accepted,gate)
        doc.update(new_identified_inverse_remainder_recoveries=0,complete_inverse_remainder_conclusion=remainder)
        terms,means,comparisons,operators,row_temp=complete_companion_comparisons(
            rows,sources,A,delta,words,base["total_squared_envelope_radial_weight_upper"],base,gate)
        doc.update(new_complete_companion_row_budgets=12,new_complete_window_evaluations=26,
            new_complete_uniform_comparisons=10,complete_comparison_conclusions=comparisons,
            complete_transport_operator_conclusions=operators)
        result=combine(base,terms,means)
        doc.update(new_complete_scalar_recombinations=4,complete_source_conclusion=result,
            strictly_smaller_complete_term_bounds=sum(int(v["strictly_smaller_complete_term"]) for v in comparisons))
        gate("only the ten declared whole terms may change and the thirteen other first terms eight other means and full local aggregate remain verbatim",
            result["local_L2_upper"]==base["local_L2_upper"]
            and all(result["complete_first_source_term_L2_upper"]["local_raw_"+str(i)]
                ==base["complete_first_source_term_L2_upper"]["local_raw_"+str(i)] for i in (1,2,3))
            and sum(k not in {v["source_term"] for v in comparisons} for k in terms)==13
            and sum(k not in {v["source_term"] for v in comparisons} for k in means)==8
            and len(row_temp)==6 and len(comparisons)==10
            and result["total_squared_envelope_radial_weight_upper"]==base["total_squared_envelope_radial_weight_upper"]
            and result["original_temporary_row_payload_sha256"]==base["original_temporary_row_payload_sha256"])
        gate("the complete new negative volume source is finite with both density windows true dr and independent physical mean",
            all(bound(result[k],k).is_finite() for k in
                ("local_L2_upper","nonlocal_total_L2_upper","first_L2_upper","mean_L2_upper","combined_L2_upper"))
            and result["actual_dr_measure"] and result["one_sided_uncertain_root_band_retained"]
            and result["both_density_windows_retained"] and result["outer_J_window"]==base["outer_J_window"])
        doc["scope"]=dict(complete_radial_mean_of_T0_retained=True,
            positive_angle_radial_derivative_uses_outer_F_jet=True,
            full_Bplus_inverse_and_leading_matrix_inverse_differentiated=True,
            QG_correlation_retained_before_derivative_bounds=True,
            old_factored_source_pipeline_invoked=False,
            accepted_regular_quotient_order_zero_read_verbatim=True,
            accepted_inverse_remainder_derivatives_read_verbatim=True,
            latest_complete_factored_31_term_ledger_retained=True,
            original_physical_root_piece_2549_only=True,original_fixed_intrinsic_parameter="eta_0",
            same_original_real_explicit_family=True,full_complex_delta_and_z_squares_in_supporting_bounds=True,
            final_operators_restrict_to_original_real_parameters=True,
            both_genuine_columns_and_both_carrier_signs=True,all_input_abs_j_at_least97=True,
            negative_side_only=True,density_zero_amplitude="w0",density_one_amplitude="w1=MZ",
            exact_signed_factorization_before_absolute_bounds=True,
            exact_regular_B_root_condition_and_all_sT_paths_retained=True,
            complete_genuine_rank_and_exact_input_n_minus_two_retained=True,
            q_is_v_Dw_minus_angle_derivative_of_vp_not_D_of_vw=True,
            all_old_h_amplitude_source_terms_retained_verbatim=True,
            full_G_radial_scalar_and_all_amplitude_means_retained=True,
            output_mean_and_complete_original_primitive_retained=True,
            both_complete_directed_word_windows_retained=True,
            no_duplicate_inner_word_or_physical_mean_factors=True,
            physical_J_only_on_its_proved_reflected_parity_domain=True,
            latest_refined_first_local_result_and_all_local_terms_retained=True,
            inverse_remainder_read_from_identified_frozen_minimum_branch=True,
            new_supporting_factor_jets_distinct_from_original_ordered_closure=True,
            all_actual_physical_seams_and_reference_matching_sources_retained=True,
            original_positive_graph_and_outer_source_ports_retained=True,
            original_eighteen_positive_coefficients_only_read=True,
            original_source_rows_and_all_radial_integrals_only_read=True,
            complete_row_and_derivative_arrays_published=False,
            physical_to_wave_readout_paid=False,full_negative_BVP_inverse_paid=False,
            positive_growing_column_operator_paid=False,cutoff97_strong_return_contraction_paid=False)
        temporary.update(new_AJ_closure=encode(aj_temporary),factored_supporting_data=factor_temp,complete_companion_rows=row_temp,
            accepted_positive_coefficients_payload_sha256=payload_sha(C["complete_positive_linear_operator_conclusion"]))
        doc["temporary_complete_companion_row_payload_sha256"]=payload_sha(row_temp)
        doc["temporary_complete_companion_row_count"]=len(row_temp)
        doc["full_physical_negative_volume_source_paid"]=True
        doc.update(complete=True,proved=True,actual_returncode=0)
    except BaseException as error:
        doc["failure"]=dict(type=type(error).__name__,message=str(error))
    finally:
        doc["actual_mathematical_wall_seconds"]=time.monotonic()-started
        temporary.update(kind=KIND,source_sha256=source,input_manifest_sha256=a.manifest_sha,complete_conclusions=doc)
        native=a.out_dir/"temporary-angular-jets-retained-radial-source.json.gz"
        save(native,temporary,True)
        doc["temporary_native_sha256"]=sha(native);doc["temporary_native_bytes"]=native.stat().st_size
        doc["temporary_native_is_not_published"]=True;actual=doc["actual_returncode"]
        try:
            text=render(doc)
            raw=(json.dumps(doc,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
            if len(raw)>60000 or len(text.encode())>60000:raise ValueError("small conclusion or process exceeded60000 bytes")
            save(a.out_dir/"process.json",doc);(a.out_dir/"conclusion.md").write_text(text)
        except BaseException as error:
            small={k:v for k,v in doc.items() if k not in ("complete_domain_conclusion",
                "complete_inverse_remainder_conclusion","complete_transport_operator_conclusions",
                "complete_comparison_conclusions","complete_source_conclusion")}
            small["actual_scientific_returncode"]=actual
            small["formatting_failure"]=dict(type=type(error).__name__,message=str(error))
            small.update(complete=False,proved=False,actual_returncode=1)
            save(a.out_dir/"process.json",small)
            (a.out_dir/"conclusion.md").write_text("# Actual AJ-source formatting failure\n\n"
                "The original scientific child code was "+str(actual)+". Formatting is separate from mathematics.\n"
                "Temporary native SHA256: "+doc["temporary_native_sha256"]+"\n")
            actual=1
        print(json.dumps(dict(complete=doc["complete"],actual_returncode=actual,
            new_complete_comparisons=doc["new_complete_uniform_comparisons"],
            old_numerical_enclosures_recomputed=0,new_radial_integrals_computed=0,
            reproducible_data_published=False)),flush=True)
    return actual
if __name__=="__main__":raise SystemExit(main())
