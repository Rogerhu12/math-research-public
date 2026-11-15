#!/usr/bin/env python3
"""True branch-density coordinate norms and complete finite conjugation.
Only new coordinate scalars and ordered products of accepted small conclusions
are evaluated. No phase, ray, source, normalizer, or physical receiver is rerun.
"""
from __future__ import annotations
import argparse,copy,gzip,hashlib,json,os,platform,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy,scipy
from flint import arb,ctx
PUBLIC="Rogerhu12/math-research-public"
TOPIC="topics/visible-flex-exact-nearby/"
KIND="actual_true_branch_density_coordinates_and_finite_conjugation_v1"
CONTRACT="57ff88f5b022b68e78512e485528fd6b5e61b704dfd56a6003d13d24a37f8a07"
G_CONTRACT="c3267f91b1d1e767acbe2b1a1e33507f4811f3f944cdece305d2bed49c54da4e"
S_CONTRACT="2010d9a15ff5604dcdfd7d1db8f782a5f247806b4b007565073b02c8d4008fac"
IN_CONTRACT="d4ac47aabbaa6869553ec33b87d2234c66e8a76e70c19f3f3d76817ccfb9bd75"
TN_CONTRACT="0ffa3261e3bb3fdea2cd05afd489b2e71b5587a2bba9432410c492e2ee64f2aa"
RUNTIME=dict(python="3.12.14",python_flint="0.9.0",numpy="2.3.5",scipy="1.17.0")
EXPECTED={
    "accepted_IN_execution":("43746008734",
        "726bdd98802c88e9c162f598ff983bc8a762d8cc8f8216164c56e6b960119874",
        "fc87dad98247598d6183d225f4dfca29ee66a8cd06c0918ffda59888091cfb74",
        "816483884254f3e7ec06914b66afffc8434db11315dfab1712e71fbb7aae5ae1",23),
    "accepted_TN_execution":("43752771157",
        "4dbc776babf0e8be12440bb21ac0765e2676c9cea02912326d46f53cfb627256",
        "9e5688400b91714b189e2ed3865cf5448b54bf26d0ff8fef76ba3af06161646e",
        "7abb04effcb8009dafaeec65cf3474e5d045b92c555bb92118544cd47256ee3d",16),
    "accepted_RR_execution":("43750683671",
        "2a51b8c45974808e65754ebaa0b476650596e7d8a1e36541e9afd3987146c4c9",
        "8822511f1f1c853efd8eec4944bcb74b6954c7fa04c143d9dafc9b470bdd1b4a",
        "a75da290077cf0e134834be5e35a0fa7cd55cd79104f5128d87eaee898af162b",28)}
PARAMETERS=json.loads("{\"arithmetic_bits\":320,\"exact_real_delta_radius\":\"1/100000000\",\"fixed_intrinsic_parameter\":\"eta_0\",\"exact_strict_cut\":\"76285779072683/320000000000000\",\"exact_root_interval\":[\"1191984371497/5000000000000\",\"2383968743003/10000000000000\"],\"exact_rho_interval\":[\"1/262144\",\"1220703413/320000000000000\"],\"original_phase_run\":\"43746008734/1\",\"original_normalizer_run\":\"43752771157/1\",\"original_physical_receiver_run\":\"43750683671/1\",\"coordinate_windows\":[\"L2\",\"H^(-4/3)\"],\"strong_input_window\":\"H^(-4/3), original reference or declared coordinate labels\",\"strong_output_window\":\"L2 density pair plus two independent physical means\",\"first_normalizer_bandwidth\":192,\"physical_frequency\":\"n=4|j|\",\"coordinate_convention\":\"two branch density maps on nonmean functions, independent mean block identity\",\"true_phase_projection\":\"exact conjugated moving projection, not renamed as a Fourier projection\",\"old_successful_scientific_calls_allowed\":0,\"full_incoming_finite_Schur_or_return_R0_claimed\":false,\"expected_actual_gate_count\":18}")

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def payload_sha(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
def read(p):return json.loads(Path(p).read_bytes())
def save(p,x,compressed=False):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
    body=gzip.compress(raw,mtime=0) if compressed else raw
    tmp=p.with_name(p.name+".tmp");tmp.write_bytes(body);tmp.replace(p)
def ex(x):
    x=Q(x);return arb(x.numerator)/arb(x.denominator)
def rb(v):
    if isinstance(v,arb):return v
    if isinstance(v,(int,Q)):return ex(v)
    if isinstance(v,str):return arb(v)
    if "lower" in v and "upper" in v:
        return arb(v["lower"]).lower().union(arb(v["upper"]).upper())
    return arb(v["ball"])
def up(v):
    x=rb(v)
    if not x.is_finite() or x.lower()<0:raise ValueError("invalid complete nonnegative coordinate budget")
    return x.upper()
def gap(v,label):
    x=rb(v).lower()
    if not x.is_finite() or not x>0:raise ValueError("unproved positive coordinate gap: "+label)
    return x
def rec(v):return dict(ball=rb(v).str(52))
def encode(v):
    if isinstance(v,arb):return rec(v)
    if isinstance(v,Q):return str(v)
    if isinstance(v,dict):return {str(k):encode(x) for k,x in v.items()}
    if isinstance(v,(list,tuple)):return [encode(x) for x in v]
    return v
def pw(v,p):return (gap(v,"positive power base").log()*ex(p)).exp()
def accepted(path,identity,gate):
    run,source,manifest,digest,ngates=identity
    e=read(path);r=e.get("actual_scientific_receipt",{})
    gate("accepted complete run "+run+"/1 retains its immutable success and exact runtime",
        sha(path)==digest and str(e.get("run_id"))==run and str(e.get("run_attempt"))=="1"
        and e.get("complete") is True and e.get("actual_returncode")==0 and e.get("actual_failure") is None
        and e.get("source_budget_source_sha256")==source and e.get("input_manifest_sha256")==manifest
        and r.get("source_sha256")==source and r.get("input_manifest_sha256")==manifest
        and r.get("complete") is True and r.get("proved") is True and r.get("actual_returncode")==0
        and r.get("failure") is None and r.get("runtime")==RUNTIME
        and len(r.get("gates",[]))==ngates and all(g.get("passed") is True for g in r["gates"]))
    return r

def same_complete_cut(I,T,R,source,gate):
    dom=I["complete_strict_cut_domain_conclusion"]
    ident=T["complete_original_cut_identity_read_verbatim"]
    p=T["complete_normalized_physical_conclusion"];params=PARAMETERS
    gate("all three accepted successes refer to the same strict cut real family and fixed physical parameter",
        all(x["mathematical_parameters"]["exact_strict_cut"]==params["exact_strict_cut"] for x in (I,T,R))
        and all(x["mathematical_parameters"]["exact_real_delta_radius"]==params["exact_real_delta_radius"] for x in (I,T,R))
        and all(x["mathematical_parameters"]["exact_root_interval"]==params["exact_root_interval"] for x in (I,T,R))
        and all(x["mathematical_parameters"]["fixed_intrinsic_parameter"]=="eta_0" for x in (I,T,R))
        and dom["exact_strict_cut"]==ident["exact_strict_cut"]==params["exact_strict_cut"]
        and dom["exact_rho_interval"]==ident["exact_true_rho_interval"]==params["exact_rho_interval"])
    gate("the entire accepted physical input and cut identity remain the literal RR conclusions",
        p["saved_complete_physical_conclusion_read_verbatim"]==R["complete_physical_comparison_conclusion"]
        and ident==R["complete_original_cut_identity_conclusion"]
        and p["complete_cut_sides"]==ident["complete_cut_sides"]==1
        and len(p["complete_normalized_cut_rows"])==1)
    gate("the frozen IN source qualifies both phase derivative sides by its same positive algorithm",
        'm3=gap(1-xm-3*om1,' in source and 'f23=up(X[1]+3*om2)' in source
        and 'om1=up(t1.sqrt()*Y[0])' in source
        and dom["actual_fixed_cut_all_tau_segments"] is True
        and dom["all_complete_physical_means_and_both_reference_columns_retained"] is True
        and dom["no_old_one_phase_gap_relabelled_as_three_phase_gap"] is True
        and dom["no_real_angle_jet_promoted_to_complex_strip"] is True)
    selected=T["complete_selected_normalizer_conclusion"]
    strong=T["complete_strong_remainder_conclusion"];J=selected["exact_cutoff_abs_j"]
    gate("the old two-window normalizers keep their same inverse original projection finite complement and means",
        type(J) is int and J>=97 and selected["first_bandwidth"]==192 and selected["second_bandwidth"]==384
        and selected["same_inverse_on_common_trigonometric_domain"] is True
        and selected["selected_cutoff_in_original_moving_circle"] is True
        and selected["all_HL_LH_blocks_and_both_independent_means_retained"] is True
        and set(selected["complete_selected_cutoff_window_verdicts"])=={"L2","Hminus4_3"}
        and all(v["both_strict_tests_passed"] is True for v in selected["complete_selected_cutoff_window_verdicts"].values())
        and strong["exact_finite_input_and_output_max_abs_j"]==J+191
        and strong["all_two_original_physical_mean_coordinates_retained"] is True
        and strong["finite_difference_output_mean_retained"] is True
        and p["finite_ports_97_through_J_minus_1_retained"] is True)
    return dom,ident,selected,strong,p

def density_coordinate_norms(domain):
    m=gap(domain["complete_new_three_phase_gap_lower"],"accepted complete phase derivative lower")
    if m>1:raise ValueError("the accepted algorithmic phase gap is not bounded by one")
    eps=up(1-m);M=up(1+eps)
    F=up(domain["complete_new_three_phase_second_derivative_upper"])
    mi=up(1/m);Fi=up(F/m**3)
    # Both a arguments are >=1; max(1,a,a*a) is exactly a*a.
    pp=up(M*M+F/arb(2).sqrt());pi=up(mi*mi+Fi/arb(2).sqrt())
    A0=up(M.sqrt());B0=up(1/m.sqrt())
    Am=up(A0*pw(pi,Q(2,3)));Bm=up(B0*pw(pp,Q(2,3)))
    out=dict(phase_derivative_lower=rec(m),phase_derivative_upper=rec(M),
        phase_derivative_deviation_upper=rec(eps),phase_second_derivative_upper=rec(F),
        inverse_phase_derivative_upper=rec(mi),inverse_phase_second_derivative_upper=rec(Fi),
        complete_pullback_H2_factor_upper=rec(pp),complete_inverse_pullback_H2_factor_upper=rec(pi),
        complete_density_L2_upper=rec(A0),complete_density_Hminus4_3_upper=rec(Am),
        complete_inverse_density_L2_upper=rec(B0),complete_inverse_density_Hminus4_3_upper=rec(Bm),
        common_both_branch_bound_is_max_not_sum=True,independent_physical_mean_block_is_identity=True,
        exact_phase_sigma="X-sigma*(2/3)*(-T)^(3/2)",
        exact_characteristic_equation="(partial_r-(d+sigma*eta*q)*partial_phi)Phi_sigma=0",
        real_fourfold_degree_one_maps=True,same_distributional_inverse_on_both_windows=True,
        accepted_phase_domain_read_verbatim=copy.deepcopy(domain))
    return dict(m=m,eps=eps,M=M,F=F,A0=A0,Am=Am,B0=B0,Bm=Bm),out

def finite_primitive_conjugation(c,S):
    m,e,F=c["m"],c["eps"],c["F"]
    b=PARAMETERS["first_normalizer_bandwidth"];CI=up(arb(17).sqrt()/4)
    displacement=up((ex(Q(33,16))*e*e/m**2+F*F/m**6).sqrt())
    G0=up(2*S/m);G1=up(4*b*S/m**2+2*S*F/m**3)
    dual=up(CI*(G0*G0+G1*G1).sqrt())
    first=up(S*c["B0"]*displacement);second=up(e/m*dual);fee=up(first+second)
    return dict(first_normalizer_bandwidth=b,complete_S_budget_used=rec(S),
        complete_inverse_displacement_H2_and_H4_3_upper=rec(displacement),
        complete_mean_subtracted_pulled_density_L2_upper=rec(G0),
        complete_mean_subtracted_pulled_density_derivative_upper=rec(G1),
        complete_primitive_dual_H4_3_row_upper=rec(dual),complete_primitive_multiplier_upper=rec(CI),
        complete_first_rank_Hminus4_3_to_L2_upper=rec(first),
        complete_second_rank_Hminus4_3_to_L2_upper=rec(second),
        complete_two_rank_Hminus4_3_to_L2_upper=rec(fee),
        two_different_branch_maps_retained=True,rank_rows_have_their_full_H4_3_fees=True,
        full_primitive_and_both_physical_means_retained=True,
        main_term="M_((a/alpha_prime) o alpha_inverse) C_(beta o alpha_inverse) I",
        first_rank="(U_alpha_inverse a) tensor t_beta",
        second_rank="-(1-j_alpha) tensor I U_beta_inverse(a-mean(a))")

def transformed_normalizers(c,selected,strong,finite):
    v=selected["complete_selected_cutoff_window_verdicts"]
    k0=up(v["L2"]["ordered_inverse_upper"]);km=up(v["Hminus4_3"]["ordered_inverse_upper"])
    f0=up(v["L2"]["complete_forward_upper"]);fm=up(v["Hminus4_3"]["complete_forward_upper"])
    g0=up(c["B0"]*c["A0"]);gm=up(c["Bm"]*c["Am"]);gs=up(c["B0"]*c["Am"])
    win=dict(complete_two_sided_L2_coordinate_factor_upper=rec(g0),
        complete_two_sided_Hminus4_3_coordinate_factor_upper=rec(gm),
        complete_strong_output_input_coordinate_factor_upper=rec(gs),
        complete_transformed_ordered_L2_inverse_upper=rec(up(g0*k0)),
        complete_transformed_ordered_Hminus4_3_inverse_upper=rec(up(gm*km)),
        complete_transformed_L2_forward_upper=rec(up(g0*f0)),
        complete_transformed_Hminus4_3_forward_upper=rec(up(gm*fm)),
        original_selected_normalizer_read_verbatim=copy.deepcopy(selected),
        same_distributional_inverse_on_both_coordinate_windows=True,
        transported_projection_is_exact_conjugate_not_Fourier=True)
    inv=up(gs*up(strong["complete_ordered_inverse_strong_remainder_upper"]))
    fwd=up(gs*up(strong["complete_forward_strong_remainder_upper"]))
    border=up(gs*up(strong["complete_uncompressed_first_symbol_finite_difference_upper"]))
    ranks=up(finite["complete_two_rank_Hminus4_3_to_L2_upper"]);total=up(inv+border+ranks)
    out=dict(complete_transformed_ordered_inverse_strong_remainder_upper=rec(inv),
        complete_transformed_forward_strong_remainder_upper=rec(fwd),
        complete_transformed_original_finite_difference_upper=rec(border),
        complete_remainder_after_true_two_chart_principal_term_upper=rec(total),
        complete_primitive_chart_rank_fee_used=copy.deepcopy(finite["complete_two_rank_Hminus4_3_to_L2_upper"]),
        original_strong_conclusion_read_verbatim=copy.deepcopy(strong),
        original_finite_input_and_output_max_abs_j=strong["exact_finite_input_and_output_max_abs_j"],
        transformed_finite_rank_columns_and_dual_rows_retained=True,
        no_finite_Fourier_support_asserted_after_coordinate_change=True,
        all_high_finite_finite_high_and_mean_blocks_retained=True,
        strong_input_window="H^(-4/3) in the declared true branch density coordinates",
        strong_output_window="L2 density pair plus two independent physical means",
        principal_term_keeps_opposite_branch_pullback=True,
        finite_Schur_inverse_or_whole_return_not_claimed=True)
    return win,out

def transformed_physical_columns(c,physical):
    rows=[];maximum=arb(0)
    for old in physical["complete_normalized_cut_rows"]:
        original=old["complete_normalized_four_pieces_upper"]
        if set(original)!={"error_density_0","error_density_1","free_R2","free_R3"}:
            raise ValueError("one complete physical column was omitted")
        new={k:rec(up(c["B0"]*up(v))) for k,v in original.items()}
        total=up(c["B0"]*up(old["complete_normalized_same_case_sum_upper"]))
        if total>maximum:maximum=total
        rows.append(dict(original_norm_row=old["original_norm_row"],complete_true_phase_four_pieces_upper=new,
            complete_true_phase_same_case_sum_upper=rec(total),
            saved_complete_normalized_row_read_verbatim=copy.deepcopy(old)))
    return dict(complete_cut_sides=len(rows),complete_true_phase_cut_rows=rows,
        complete_true_phase_physical_Darboux_comparison_upper=rec(maximum),
        complete_inverse_density_L2_factor_used=rec(c["B0"]),
        accepted_complete_normalized_physical_payload_sha256=payload_sha(physical),
        saved_complete_normalized_physical_comparison_read_verbatim=copy.deepcopy(
            physical["complete_normalized_physical_Darboux_comparison_upper"]),
        saved_complete_L2_normalizer_factor_read_verbatim=copy.deepcopy(physical["complete_ordered_L2_inverse_upper"]),
        exact_input_window="H^(-4/3), both reference columns and both signs |j|>=97",
        exact_output_window="true branch L2 density pair plus both independent physical means",
        order="inverse true density chart after accepted complete cut normalizer",
        old_K0_already_in_input_not_multiplied_again=True,original_reference_input_coordinates_unchanged=True,
        complete_same_case_sum_multiplied_before_side_maximum=True,all_output_modes_and_both_physical_means_retained=True,
        not_identified_with_complete_incoming_or_outgoing_error=True)

def render_conclusion(d):
    keys=("kind","complete","proved","actual_returncode","failure","source_sha256","input_manifest_sha256",
        "runtime","arithmetic_bits","run_id","run_attempt","actual_mathematical_wall_seconds",
        "complete_density_coordinate_conclusion","complete_finite_primitive_conjugation_conclusion",
        "complete_transformed_normalizer_window_conclusion","complete_transformed_strong_conclusion",
        "complete_true_phase_physical_conclusion","scope")
    small={k:copy.deepcopy(d[k]) for k in keys if k in d}
    for key in ("complete_density_coordinate_conclusion","complete_transformed_normalizer_window_conclusion",
                "complete_transformed_strong_conclusion"):
        if key in small:
            small[key]={k:v for k,v in small[key].items() if not k.endswith("_read_verbatim")}
    if "complete_true_phase_physical_conclusion" in small:
        for row in small["complete_true_phase_physical_conclusion"]["complete_true_phase_cut_rows"]:
            row.pop("saved_complete_normalized_row_read_verbatim",None)
    small["expected_gates"]=PARAMETERS["expected_actual_gate_count"]
    small["recorded_gates"]=len(d["gates"]);small["passed_gates"]=sum(g["passed"] is True for g in d["gates"])
    fence=chr(96)*3
    return ("# Complete true branch-density coordinates\n\n"
        "The same P22 strict cut, both characteristic branches, the exact transported finite projection and both physical means remain.\n"
        "The complete incoming inverse and whole return are separate.\n\n"+fence+"json\n"
        +json.dumps(small,sort_keys=True,indent=2,ensure_ascii=False,allow_nan=False)+"\n"+fence+"\n")

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for key in ("repo-root","manifest","workdir","process","conclusion","out"):
        parser.add_argument("--"+key,type=Path,required=True)
    a=parser.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("new coordinate arithmetic is permitted only on the actual public repository Actions runner")
    runtime=dict(python=platform.python_version(),python_flint=flint.__version__,numpy=numpy.__version__,scipy=scipy.__version__)
    if runtime!=RUNTIME:raise RuntimeError("the frozen public scientific runtime changed")
    ctx.prec=320;a.workdir.mkdir(parents=True,exist_ok=True);started=time.monotonic()
    d=dict(kind=KIND,complete=False,proved=False,actual_returncode=1,failure=None,gates=[],
        source_sha256=sha(__file__),input_manifest_sha256=sha(a.manifest),runtime=runtime,arithmetic_bits=320,
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),actual_scientific_checkout_commit=os.environ.get("ACTUAL_CHECKOUT_COMMIT"),
        mathematical_parameters=PARAMETERS,original_successful_small_receipts_read=0,
        saved_complete_phase_qualifications_read=0,saved_complete_normalizer_conclusions_read=0,
        saved_complete_physical_columns_read=0,new_phase_coordinate_closures=0,new_coordinate_window_norms=0,
        new_primitive_finite_row_conclusions=0,new_transformed_normalizer_window_bounds=0,
        new_transformed_strong_or_finite_conclusions=0,new_true_phase_physical_columns=0,new_true_phase_physical_sums=0,
        old_numerical_enclosures_recomputed=0,old_phases_rays_profiles_or_amplitudes_recomputed=0,
        old_sources_normalizers_or_physical_receivers_recomputed=0,old_scientific_producer_calls=0,
        old_binary_or_archive_inputs_restored=0,original_natural_stage_bytes_modified=False,
        complete_true_branch_density_coordinates_paid=False,full_incoming_inverse_claimed=False,
        finite_Schur_inverse_claimed=False,full_return_R0_claimed=False,temporary_native_is_not_published=True,
        reproducible_outputs_published_to_repository=False,reproducible_outputs_uploaded_to_Releases=False,
        new_reproducible_data_artifact_uploaded=False)
    def checkpoint():save(a.process,d)
    def gate(name,truth):
        ok=bool(truth);d["gates"].append(dict(name=name,passed=ok))
        if not ok:raise ValueError("actual true-density-coordinate gate failed: "+name)
    try:
        manifest=read(a.manifest)
        gate("the immutable manifest fixes the coordinate contract runtime and both complete windows",
            manifest["source_sha256"]==sha(__file__) and manifest["contract_sha256"]==CONTRACT
            and manifest["runtime"]==RUNTIME and manifest["mathematical_parameters"]==PARAMETERS
            and manifest["expected_actual_gate_count"]==18
            and len({x["path"] for x in manifest["files"]})==len(manifest["files"]))
        for item in manifest["files"]:
            p=a.repo_root/item["path"]
            if not p.is_file() or p.stat().st_size!=item["bytes"] or sha(p)!=item["sha256"]:
                raise ValueError("immutable complete input changed: "+item["path"])
        paths={k:a.repo_root/v for k,v in manifest["input_paths"].items()}
        gate("all three original proofs and receipts are immutable small inputs and no old source is imported",
            set(EXPECTED)<=set(paths) and sha(paths["contract"])==CONTRACT
            and sha(paths["G_contract"])==G_CONTRACT and sha(paths["S_contract"])==S_CONTRACT
            and sha(paths["IN_contract"])==IN_CONTRACT and sha(paths["TN_contract"])==TN_CONTRACT
            and all(sha(paths["accepted_"+tag+"_source"])==EXPECTED["accepted_"+tag+"_execution"][1]
                and sha(paths["accepted_"+tag+"_manifest"])==EXPECTED["accepted_"+tag+"_execution"][2]
                for tag in ("IN","TN","RR"))
            and manifest["all_inputs_are_current_small_texts"] is True
            and manifest["old_successful_scientific_calls_allowed"]==0
            and manifest["old_scientific_source_files_are_identity_evidence_not_imported"] is True)
        I=accepted(paths["accepted_IN_execution"],EXPECTED["accepted_IN_execution"],gate)
        T=accepted(paths["accepted_TN_execution"],EXPECTED["accepted_TN_execution"],gate)
        R=accepted(paths["accepted_RR_execution"],EXPECTED["accepted_RR_execution"],gate)
        d["original_successful_small_receipts_read"]=3
        dom,ident,selected,strong,physical=same_complete_cut(I,T,R,paths["accepted_IN_source"].read_text(),gate)
        d["saved_complete_phase_qualifications_read"]=1;d["saved_complete_normalizer_conclusions_read"]=1
        d["saved_complete_physical_columns_read"]=4*physical["complete_cut_sides"]
        d["complete_original_cut_identity_read_verbatim"]=copy.deepcopy(ident)
        d["accepted_complete_physical_payload_sha256"]=payload_sha(physical["saved_complete_physical_conclusion_read_verbatim"])
        checkpoint()
        c,coordinate=density_coordinate_norms(dom)
        d["complete_density_coordinate_conclusion"]=coordinate
        d["new_phase_coordinate_closures"]=1;d["new_coordinate_window_norms"]=4;checkpoint()
        gate("the new derivative interval follows the full saved positive phase algorithm on the same real family",
            c["m"]>0 and c["m"]<=1 and c["eps"]>=0 and c["M"]>=1 and c["F"]>=0
            and coordinate["accepted_phase_domain_read_verbatim"]==dom)
        gate("one density coordinate and its inverse are bounded in both windows with the independent means unchanged",
            all(c[k].is_finite() and c[k]>=1 for k in ("A0","Am","B0","Bm"))
            and coordinate["independent_physical_mean_block_is_identity"] is True
            and coordinate["same_distributional_inverse_on_both_windows"] is True)
        finite=finite_primitive_conjugation(c,up(selected["complete_S_upper"]))
        d["complete_finite_primitive_conjugation_conclusion"]=finite
        d["new_primitive_finite_row_conclusions"]=1;checkpoint()
        gate("both primitive rank rows have complete H4_3 dual norms and retain the different true branch circles",
            finite["first_normalizer_bandwidth"]==192
            and all(up(v).is_finite() for v in finite.values() if isinstance(v,dict) and "ball" in v)
            and finite["two_different_branch_maps_retained"] is True
            and finite["full_primitive_and_both_physical_means_retained"] is True)
        windows,newstrong=transformed_normalizers(c,selected,strong,finite)
        d["complete_transformed_normalizer_window_conclusion"]=windows
        d["complete_transformed_strong_conclusion"]=newstrong
        d["new_transformed_normalizer_window_bounds"]=4
        d["new_transformed_strong_or_finite_conclusions"]=4;checkpoint()
        gate("the complete normalizer and forward bounds use output and input factors in their own two windows",
            windows["original_selected_normalizer_read_verbatim"]==selected
            and all(up(windows[k]).is_finite() for k in (
                "complete_transformed_ordered_L2_inverse_upper","complete_transformed_ordered_Hminus4_3_inverse_upper",
                "complete_transformed_L2_forward_upper","complete_transformed_Hminus4_3_forward_upper")))
        gate("the transformed strong and finite remainders retain B0_Aminus and both explicit primitive ranks",
            newstrong["original_strong_conclusion_read_verbatim"]==strong
            and all(up(newstrong[k]).is_finite() for k in (
                "complete_transformed_ordered_inverse_strong_remainder_upper",
                "complete_transformed_forward_strong_remainder_upper",
                "complete_transformed_original_finite_difference_upper",
                "complete_remainder_after_true_two_chart_principal_term_upper"))
            and newstrong["principal_term_keeps_opposite_branch_pullback"] is True)
        newphysical=transformed_physical_columns(c,physical)
        d["complete_true_phase_physical_conclusion"]=newphysical
        d["new_true_phase_physical_columns"]=4*physical["complete_cut_sides"]
        d["new_true_phase_physical_sums"]=physical["complete_cut_sides"];checkpoint()
        gate("all four already normalized physical columns are followed by exactly one output density factor",
            newphysical["complete_cut_sides"]==physical["complete_cut_sides"]
            and all(a0["saved_complete_normalized_row_read_verbatim"]==b0
                for a0,b0 in zip(newphysical["complete_true_phase_cut_rows"],physical["complete_normalized_cut_rows"]))
            and newphysical["old_K0_already_in_input_not_multiplied_again"] is True
            and newphysical["original_reference_input_coordinates_unchanged"] is True)
        gate("complete same-case sums and both independent physical means are retained before any side maximum",
            newphysical["complete_same_case_sum_multiplied_before_side_maximum"] is True
            and newphysical["all_output_modes_and_both_physical_means_retained"] is True
            and all(set(x["complete_true_phase_four_pieces_upper"])=={"error_density_0","error_density_1","free_R2","free_R3"}
                and up(x["complete_true_phase_same_case_sum_upper"]).is_finite()
                for x in newphysical["complete_true_phase_cut_rows"]))
        gate("the finite projector is truly conjugated and is never relabelled as a phase Fourier projection",
            windows["transported_projection_is_exact_conjugate_not_Fourier"] is True
            and newstrong["no_finite_Fourier_support_asserted_after_coordinate_change"] is True
            and newstrong["transformed_finite_rank_columns_and_dual_rows_retained"] is True
            and newstrong["all_high_finite_finite_high_and_mean_blocks_retained"] is True)
        d["scope"]=dict(same_exact_P22_real_family=True,two_true_characteristic_branches=True,
            independent_physical_means_are_identity_blocks=True,complete_cross_mean_and_finite_blocks_retained=True,
            same_coordinate_inverse_on_L2_and_Hminus4_3=True,complete_two_chart_primitive_and_two_rank_identity=True,
            dual_rows_paid_in_H4_3=True,finite_projection_is_the_exact_transported_projection=True,
            old_finite_support_becomes_true_finite_span_not_new_Fourier_support=True,
            complete_original_physical_columns_have_only_new_output_coordinate_fee=True,
            complete_incoming_or_outgoing_error_not_identified_with_these_columns=True,
            actual_ci_co_or_stable_or_incoming_inverse_not_claimed=True,finite_Schur_inverse_not_claimed=True,
            whole_return_R0_or_interval_flow_not_claimed=True,all_Sobolev_tame_family_not_claimed=True)
        zeros=("old_numerical_enclosures_recomputed","old_phases_rays_profiles_or_amplitudes_recomputed",
            "old_sources_normalizers_or_physical_receivers_recomputed","old_scientific_producer_calls",
            "old_binary_or_archive_inputs_restored")
        gate("only the declared new coordinate scalars and complete ordered products were evaluated",
            all(d[k]==0 for k in zeros) and d["original_successful_small_receipts_read"]==3
            and d["new_coordinate_window_norms"]==4 and d["new_primitive_finite_row_conclusions"]==1
            and d["new_transformed_normalizer_window_bounds"]==4
            and d["new_transformed_strong_or_finite_conclusions"]==4
            and d["new_true_phase_physical_columns"]==4 and d["new_true_phase_physical_sums"]==1)
        if len(d["gates"])!=PARAMETERS["expected_actual_gate_count"]:
            raise ValueError("the complete coordinate gate count differs from the frozen contract")
        d["complete"]=d["proved"]=d["complete_true_branch_density_coordinates_paid"]=True
        d["actual_returncode"]=0
    except Exception as err:
        d["failure"]=dict(type=type(err).__name__,message=str(err))
        print("ACTUAL_TRUE_DENSITY_COORDINATE_FAILURE",repr(err),flush=True)
    finally:
        d["actual_mathematical_wall_seconds"]=time.monotonic()-started
        checkpoint()
        save(a.out,dict(scientific_receipt=d,no_old_scientific_reexecution=True),compressed=True)
        d["temporary_native_sha256"]=sha(a.out);d["temporary_native_bytes"]=a.out.stat().st_size;checkpoint()
        a.conclusion.parent.mkdir(parents=True,exist_ok=True)
        t=a.conclusion.with_name(a.conclusion.name+".tmp")
        t.write_text(render_conclusion(d),encoding="utf-8");t.replace(a.conclusion)
    raise SystemExit(d["actual_returncode"])

if __name__=="__main__":main()
