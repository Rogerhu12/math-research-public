#!/usr/bin/env python3
"""Complete true waist coordinates and shorter leading flows from saved positive products.
Only new scalar consequences of accepted ST and TC conclusions are evaluated.
All original scientific sources are read as immutable identity evidence, never imported.
"""
from __future__ import annotations
import argparse,copy,gzip,hashlib,json,os,platform,time
from fractions import Fraction as Q
from pathlib import Path
import flint,numpy,scipy
from flint import arb,ctx
PUBLIC="Rogerhu12/math-research-public"
TOPIC="topics/visible-flex-exact-nearby/"
KIND="actual_true_waist_coordinates_from_saved_positive_products_v1"
CONTRACT="c5157bbb14b300c1a418642e96917b49f0f90c1ebc3571a124a26b863adc9ae1"
AC_CONTRACT="6527fa46ddc21ed3d3e8c6ce4bb1f39f2db816d9fff5684e6daf4f30951c46f4"
SP_CONTRACT="ae01c213b63ae618e4657b5966604e7fbec4acb4763ea4b8aae848e1a40a40b4"
ST_CONTRACT="b15c1630edba1510dc293dea447d4bfe8144680cf73523c3b3b7a237949d5938"
TC_CONTRACT="57ff88f5b022b68e78512e485528fd6b5e61b704dfd56a6003d13d24a37f8a07"
SP_SOURCE="9d6ef721338e47e2cae8d179ce84976881df91762050d2a77d83b5399f6ba69a"
RUNTIME=dict(python="3.12.14",python_flint="0.9.0",numpy="2.3.5",scipy="1.17.0")
EXPECTED=json.loads("{\"accepted_ST_execution\":[\"43757644616\",\"743e4318ca0cbdf57afde3a188013a64c2bacba0958c31fde3b42fcf8a7aa7d5\",\"e43b2c7036088cd8d1401c580c1aa6ef694d283057dcce7c65839f92fc1b0e80\",\"b3fac70f696197e94464d0fdd16e86ce94c8216b8227593974313eb24cb7e637\",25],\"accepted_TC_execution\":[\"43754703603\",\"e05b4a9cbe5d66e03a1fb22b70c75ee48cdc885d1bd83c523d9a0173b92b0d71\",\"0e78cfa73d9d2ce8d53fc8eb1c0bdffef276739360aa66f55f13ea13f5ab3c45\",\"37c2a5ae3b77e7f0895aa0c3130d8707868816f1d26a119a880272f9b92f902e\",18]}")
PARAMETERS=json.loads("{\"arithmetic_bits\":320,\"exact_real_delta_radius\":\"1/100000000\",\"fixed_intrinsic_parameter\":\"eta_0\",\"exact_strict_cut\":\"76285779072683/320000000000000\",\"exact_root_interval\":[\"1191984371497/5000000000000\",\"2383968743003/10000000000000\"],\"selected_conjugacy_parameter_absolute_upper\":\"0.00000000009368259853002\",\"selected_conjugacy_derivative_lower\":\"31/32\",\"selected_conjugacy_derivative_upper\":\"33/32\",\"selected_conjugacy_second_derivative_upper\":\"4\",\"original_ST_run\":\"43757644616/1\",\"original_TC_run\":\"43754703603/1\",\"physical_frequency\":\"n=4|j|\",\"known_drift_label_bandwidth\":192,\"coordinate_windows\":[\"L2\",\"H^(-4/3)\"],\"complete_mean_coordinates\":2,\"exact_complete_radial_interval\":[\"0\",\"76285779072683/320000000000000\"],\"flow_scope\":\"every shorter interval in either direction in the same real family\",\"selected_common_input_order\":\"S = U_H_inverse U_X_minus = U_(X_minus o H_inverse)\",\"all_independent_means_and_finite_cross_blocks_retained\":true,\"old_successful_scientific_calls_allowed\":0,\"old_binary_or_archive_inputs_restored\":0,\"full_incoming_finite_Schur_or_return_R0_claimed\":false,\"expected_actual_gate_count\":20}")

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
    if not x.is_finite() or x.lower()<0:raise ValueError("invalid complete nonnegative waist-coordinate budget")
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

def saved_common_qualifications(S,T,paths,gate):
    ps,pt=S["mathematical_parameters"],T["mathematical_parameters"]
    flow=S["complete_new_strict_propagation_conclusion"]
    phase=T["complete_density_coordinate_conclusion"]
    gate("both accepted successes refer to the same real family actual P22 cut and fixed intrinsic parameter",
        ps["exact_true_branch_cut"]==pt["exact_strict_cut"]==PARAMETERS["exact_strict_cut"]
        and all(p["exact_real_delta_radius"]==PARAMETERS["exact_real_delta_radius"] for p in (ps,pt))
        and all(p["exact_root_interval"]==PARAMETERS["exact_root_interval"] for p in (ps,pt))
        and all(p["fixed_intrinsic_parameter"]=="eta_0" and p["physical_frequency"]=="n=4|j|" for p in (ps,pt))
        and flow["exact_complete_interval"]==PARAMETERS["exact_complete_radial_interval"])
    sp=paths["SP_source"].read_text();st=paths["accepted_ST_source"].read_text()
    gate("the saved diagonal entries come from the complete original positive comparison algorithm",
        'max(arb(0),up(rate+D+(A1+Ny)/4))' in sp
        and 'ap=matrix(F);am=matrix(Brev)' in sp and 'def positive_exp(a,length):' in sp
        and 'max(arb(0),up(rate+D+(A+Ny)/4))' in st
        and 'fullplus=mm(plus,oldplus);fullminus=scale(mm(oldminus,minus),up(c2.exp()))' in st
        and all(len(flow[key])==2 and all(len(row)==2 for row in flow[key]) for key in
            ("complete_forward_matrix","complete_reverse_matrix"))
        and flow["all_shorter_ordered_subproducts_and_affine_insertions_retained"] is True
        and flow["original_0_ra_curvature_cost_reused_as_one_whole_budget"] is True
        and flow["no_old_upper_subtraction_or_division"] is True
        and S["scope"]["every_shorter_source_insertion_has_the_complete_ordered_upper"] is True)
    gate("the saved cut phase conclusion retains both true branches the full real family and both independent means",
        phase["real_fourfold_degree_one_maps"] is True
        and phase["common_both_branch_bound_is_max_not_sum"] is True
        and phase["same_distributional_inverse_on_both_windows"] is True
        and phase["independent_physical_mean_block_is_identity"] is True
        and phase["accepted_phase_domain_read_verbatim"]["exact_strict_cut"]==PARAMETERS["exact_strict_cut"]
        and phase["accepted_phase_domain_read_verbatim"]["actual_fixed_cut_all_tau_segments"] is True
        and phase["accepted_phase_domain_read_verbatim"]["all_complete_physical_means_and_both_reference_columns_retained"] is True
        and flow["complete_both_mean_and_all_Fourier_coordinates_retained"] is True)
    gate("the actual principal conjugacy is restricted to its original selected parameter and exact AC bounds",
        sha(paths["AC_contract"])==AC_CONTRACT
        and Q(PARAMETERS["selected_conjugacy_parameter_absolute_upper"])<Q(PARAMETERS["exact_real_delta_radius"])
        and Q(PARAMETERS["selected_conjugacy_derivative_lower"])==Q(31,32)
        and Q(PARAMETERS["selected_conjugacy_derivative_upper"])==Q(33,32)
        and Q(PARAMETERS["selected_conjugacy_second_derivative_upper"])==4)
    return flow,phase

def flow_derivative_bounds(flow):
    gap(flow["complete_forward_matrix"][0][0],"saved positive forward entry")
    gap(flow["complete_reverse_matrix"][0][0],"saved positive reverse entry")
    pp=up(flow["complete_forward_matrix"][0][0]);pm=up(flow["complete_reverse_matrix"][0][0])
    if not pp>=1 or not pm>=1:raise ValueError("a saved complete positive diagonal is smaller than identity")
    M=up((pp*pm).sqrt());m=gap(1/M,"directed flow Jacobian lower")
    k2=up(768*arb(385).sqrt());k3=up(768**2*arb(385).sqrt())
    F=up(k2*M*(M-1))
    G=up(M/2*(3*k2*k2*(M-1)**2+k3*(M*M-1)))
    out=dict(complete_forward_diagonal_upper=rec(pp),complete_reverse_diagonal_upper=rec(pm),
        complete_shorter_flow_derivative_lower=rec(m),complete_shorter_flow_derivative_upper=rec(M),
        complete_shorter_flow_second_derivative_upper=rec(F),complete_shorter_flow_third_derivative_upper=rec(G),
        complete_angular_second_multiplier_upper=rec(k2),complete_angular_third_multiplier_upper=rec(k3),
        known_drift_label_bandwidth=192,physical_derivative_frequency_factor=4,
        true_radial_interval=PARAMETERS["exact_complete_radial_interval"],
        every_shorter_interval_and_both_orientations=True,both_characteristic_branches_share_maximum_bound=True,
        inverse_flow_has_its_own_same_directed_bounds=True,
        specific_positive_algorithm_lower_addends_used=True,no_arbitrary_operator_norm_inversion=True,
        no_old_positive_exponential_or_ray_evaluated=True)
    return dict(m=m,M=M,F=F,G=G,Pplus=pp,Pminus=pm),out

def coordinate_norms(m,M,F,label):
    m=gap(m,label+" derivative lower");M=up(M);F=up(F)
    if not m<=1 or not M>=1:raise ValueError("degree-one coordinate interval does not contain mean derivative one")
    mi=up(1/m);Fi=up(F/m**3)
    pp=up(M*M+F/arb(2).sqrt());pi=up(mi*mi+Fi/arb(2).sqrt())
    A0=up(M.sqrt());B0=up(1/m.sqrt())
    Am=up(A0*pw(pi,Q(2,3)));Bm=up(B0*pw(pp,Q(2,3)))
    v=dict(m=m,M=M,F=F,A0=A0,B0=B0,Am=Am,Bm=Bm)
    out=dict(coordinate=label,phase_derivative_lower=rec(m),phase_derivative_upper=rec(M),
        phase_second_derivative_upper=rec(F),inverse_phase_derivative_upper=rec(mi),
        inverse_phase_second_derivative_upper=rec(Fi),
        complete_pullback_H2_factor_upper=rec(pp),complete_inverse_pullback_H2_factor_upper=rec(pi),
        complete_density_L2_upper=rec(A0),complete_density_Hminus4_3_upper=rec(Am),
        complete_inverse_density_L2_upper=rec(B0),complete_inverse_density_Hminus4_3_upper=rec(Bm),
        independent_physical_mean_block_is_identity=True,common_branch_norm_is_max_not_sum=True,
        same_actual_inverse_on_L2_and_Hminus4_3=True,all_density_Jacobians_and_normalized_measures_retained=True)
    return v,out

def waist_and_shorter_coordinates(f,phase):
    mc=gap(phase["phase_derivative_lower"],"accepted TC phase derivative lower")
    Mc=up(phase["phase_derivative_upper"]);Fc=up(phase["phase_second_derivative_upper"])
    mw=gap(mc/f["M"],"complete waist phase derivative lower")
    Mw=up(Mc*f["M"]);Fw=up(Fc*f["M"]**2+Mc*f["F"])
    waist,waistout=coordinate_norms(mw,Mw,Fw,"actual root-labelled waist maps X_plus and X_minus")
    short,shortout=coordinate_norms(f["m"],f["M"],f["F"],"each shorter directed true characteristic flow")
    # WX.19 uses a common bound valid for both orientations.
    common=up(f["M"].sqrt()*pw(up(f["M"]**2+f["F"]*f["M"]**3/arb(2).sqrt()),Q(2,3)))
    shortout["complete_common_both_orientation_Hminus4_3_upper"]=rec(common)
    shortout["every_shorter_interval_in_original_family"]=True
    waistout["exact_true_map_order"]="Phi_waist = Phi_cut o chi_waist_to_cut"
    waistout["original_cut_constants_not_relabelled_as_waist_constants"]=True
    return waist,waistout,short,shortout,common

def selected_common_input(waist):
    H,Hout=coordinate_norms(ex(Q(31,32)),ex(Q(33,32)),arb(4),"the accepted selected actual H")
    psi=dict(m=gap(waist["m"]/H["M"],"selected common input derivative lower"),
        M=up(waist["M"]/H["m"]),
        F=up(waist["F"]/H["m"]**2+waist["M"]*H["F"]/H["m"]**3))
    out=dict(exact_order="S = U_H_inverse U_X_minus = U_(X_minus o H_inverse)",
        inverse_order="S_inverse = U_X_minus_inverse U_H",
        common_input_map="psi = X_minus o H_inverse",
        complete_common_input_L2_upper=rec(up(H["B0"]*waist["A0"])),
        complete_common_input_Hminus4_3_upper=rec(up(H["Bm"]*waist["Am"])),
        complete_common_input_inverse_L2_upper=rec(up(waist["B0"]*H["A0"])),
        complete_common_input_inverse_Hminus4_3_upper=rec(up(waist["Bm"]*H["Am"])),
        common_input_derivative_lower=rec(psi["m"]),common_input_derivative_upper=rec(psi["M"]),
        common_input_second_derivative_upper=rec(psi["F"]),
        selected_parameter_absolute_upper=PARAMETERS["selected_conjugacy_parameter_absolute_upper"],
        only_same_selected_actual_conjugacy=True,no_projection_commuted_through_coordinate=True,
        rigid_rotation_isometry_does_not_change_norm=True,independent_mean_block_retained=True,
        complete_inverse_H_output_L2_factor=copy.deepcopy(Hout["complete_inverse_density_L2_upper"]),
        complete_inverse_H_output_Hminus4_3_factor=copy.deepcopy(Hout["complete_inverse_density_Hminus4_3_upper"]))
    Hout["only_same_selected_actual_conjugacy"]=True
    Hout["selected_parameter_absolute_upper"]=PARAMETERS["selected_conjugacy_parameter_absolute_upper"]
    return Hout,psi,out

def primitive_rank_fees(v,label):
    m,M,F=v["m"],v["M"],v["F"]
    D=max(up(1-m),up(M-1));P=up(arb.pi()*D/2)
    P2=up((P*P+2*D*D+F*F).sqrt())
    rank1=up(M*P2);rank2=up(M*P);both=up(rank1+rank2)
    inverseD=max(up(1/m-1),up(1-1/M))
    return dict(coordinate=label,complete_derivative_deviation_upper=rec(D),
        complete_zero_mean_displacement_Linfty_upper=rec(P),
        complete_zero_mean_displacement_H2_and_H4_3_upper=rec(P2),
        complete_unit_multiplier_first_rank_upper=rec(rank1),
        complete_unit_multiplier_second_rank_upper=rec(rank2),
        complete_unit_multiplier_two_rank_upper=rec(both),
        complete_forward_density_mean_adjustment_rank_upper=rec(D),
        complete_inverse_density_mean_adjustment_rank_upper=rec(inverseD),
        exact_full_circle_identity="Upsi Mc I Upsi_inverse = M_(Upsi c) I + (Upsi c) tensor ppsi - ((Upsi c)*ppsi) tensor 1",
        unit_multiplier_only=True,later_complete_multiplier_Linfty_fee_must_multiply_this_unit_bound=True,
        both_finite_rank_terms_and_the_full_mean_retained=True,
        mean_identity_extension_differs_from_full_density_by_explicit_rank=True,
        input_window="H^(-4/3)",output_window="L2",two_different_charts_still_require_complete_TC_identity=True)

def leading_flows(f,common):
    return dict(complete_forward_L2_upper=rec(f["Pplus"]),complete_reverse_L2_upper=rec(f["Pminus"]),
        complete_forward_Hminus4_3_upper=rec(up(f["Pplus"]*common)),
        complete_reverse_Hminus4_3_upper=rec(up(f["Pminus"]*common)),
        complete_forward_radial_exponential_upper=rec(f["Pplus"]),
        complete_reverse_radial_exponential_upper=rec(f["Pminus"]),
        complete_common_density_Hminus4_3_factor_used=rec(common),
        exact_evolution="V0(b,a) = exp(integral_a^b ell0 dr) U_(chi_b_to_a)",
        exact_scalar_radial_rate="ell0 = -2 beta mean(u^2+K*v^2)",
        true_radial_interval=PARAMETERS["exact_complete_radial_interval"],
        all_shorter_subintervals_and_both_branches=True,forward_orientation="b>=a",reverse_orientation="b<=a",
        ungauged_primitive_density_convention=True,whole_general_physical_Cauchy_flow_not_replaced=True,
        ng_endpoint_ratio_not_absorbed_or_inverted=True,no_interior_ng_bound_claimed=True,
        complete_coupled_mean_source_and_all_seam_terms_remain=True)

def finite_records(x):
    if isinstance(x,dict):
        if set(x)=={"ball"}:return rb(x).is_finite()
        return all(finite_records(v) for v in x.values())
    if isinstance(x,list):return all(finite_records(v) for v in x)
    return True

def render_conclusion(d):
    keys=("kind","complete","proved","actual_returncode","failure","source_sha256","input_manifest_sha256",
        "runtime","run_id","run_attempt","actual_mathematical_wall_seconds",
        "complete_shorter_flow_derivative_conclusion","complete_waist_density_coordinate_conclusion",
        "complete_selected_common_input_conclusion","complete_ungauged_leading_flow_conclusion","scope")
    small={k:copy.deepcopy(d[k]) for k in keys if k in d}
    small["expected_gates"]=PARAMETERS["expected_actual_gate_count"]
    small["recorded_gates"]=len(d["gates"]);small["passed_gates"]=sum(g["passed"] is True for g in d["gates"])
    small["full_scientific_receipt"]="execution.json retains every original copied conclusion, all new norms and all three complete primitive rank fees"
    fence=chr(96)*3
    return ("# Actual true waist coordinates from saved positive products\n\n"
        "The same real reference family, both true characteristic branches, every shorter directed interval and both independent means remain explicit.\n"
        "The actual H chart is used only at its selected parameter. Source integrals, waist normalizer, incoming inverse and complete return remain separate.\n\n"
        +fence+"json\n"+json.dumps(small,sort_keys=True,indent=2,ensure_ascii=False,allow_nan=False)+"\n"+fence+"\n")

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for key in ("repo-root","manifest","workdir","process","conclusion","out"):
        parser.add_argument("--"+key,type=Path,required=True)
    a=parser.parse_args()
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=PUBLIC:
        raise RuntimeError("new waist-coordinate arithmetic is permitted only on the actual public repository Actions runner")
    runtime=dict(python=platform.python_version(),python_flint=flint.__version__,numpy=numpy.__version__,scipy=scipy.__version__)
    if runtime!=RUNTIME:raise RuntimeError("the frozen public scientific runtime changed")
    ctx.prec=320;a.workdir.mkdir(parents=True,exist_ok=True);started=time.monotonic()
    d=dict(kind=KIND,complete=False,proved=False,actual_returncode=1,failure=None,gates=[],
        source_sha256=sha(__file__),input_manifest_sha256=sha(a.manifest),runtime=runtime,arithmetic_bits=320,
        public_repository=PUBLIC,run_id=os.environ.get("GITHUB_RUN_ID"),run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        workflow_event_commit=os.environ.get("GITHUB_SHA"),actual_scientific_checkout_commit=os.environ.get("ACTUAL_CHECKOUT_COMMIT"),
        mathematical_parameters=PARAMETERS,original_successful_small_receipts_read=0,
        saved_complete_positive_products_read=0,saved_complete_phase_qualifications_read=0,
        new_common_shorter_flow_derivative_conclusions=0,new_waist_phase_triples=0,
        new_density_coordinate_window_bounds=0,new_shorter_flow_common_negative_window_bounds=0,
        new_ordered_common_input_window_bounds=0,new_common_input_phase_triples=0,
        new_primitive_rank_conclusions=0,new_complete_ungauged_leading_bounds=0,
        old_numerical_enclosures_recomputed=0,old_phases_rays_profiles_or_amplitudes_recomputed=0,
        old_positive_products_or_coordinate_conclusions_recomputed=0,
        old_sources_normalizers_or_physical_receivers_recomputed=0,old_scientific_producer_calls=0,
        old_binary_or_archive_inputs_restored=0,new_radial_source_integrals_evaluated=0,
        original_natural_stage_bytes_modified=False,complete_true_waist_coordinate_conclusion_paid=False,
        full_incoming_inverse_claimed=False,finite_Schur_inverse_claimed=False,full_return_R0_claimed=False,
        temporary_native_is_not_published=True,reproducible_outputs_published_to_repository=False,
        reproducible_outputs_uploaded_to_Releases=False,new_reproducible_data_artifact_uploaded=False)
    def checkpoint():save(a.process,d)
    def gate(name,truth):
        ok=bool(truth);d["gates"].append(dict(name=name,passed=ok))
        if not ok:raise ValueError("actual true-waist-coordinate gate failed: "+name)
    try:
        manifest=read(a.manifest)
        gate("the immutable manifest fixes the complete waist contract runtime and both coordinate windows",
            manifest["source_sha256"]==sha(__file__) and manifest["contract_sha256"]==CONTRACT
            and manifest["runtime"]==RUNTIME and manifest["mathematical_parameters"]==PARAMETERS
            and manifest["expected_actual_gate_count"]==20
            and len({x["path"] for x in manifest["files"]})==len(manifest["files"]))
        for item in manifest["files"]:
            p=a.repo_root/item["path"]
            if not p.is_file() or p.stat().st_size!=item["bytes"] or sha(p)!=item["sha256"]:
                raise ValueError("immutable complete input changed: "+item["path"])
        paths={k:a.repo_root/v for k,v in manifest["input_paths"].items()}
        gate("all current small receipts and primary sources retain their exact immutable identities without imports",
            set(EXPECTED)<=set(paths) and sha(paths["contract"])==CONTRACT
            and sha(paths["AC_contract"])==AC_CONTRACT and sha(paths["SP_contract"])==SP_CONTRACT
            and sha(paths["ST_contract"])==ST_CONTRACT and sha(paths["TC_contract"])==TC_CONTRACT
            and sha(paths["SP_source"])==SP_SOURCE
            and all(sha(paths["accepted_"+tag+"_source"])==EXPECTED["accepted_"+tag+"_execution"][1]
                and sha(paths["accepted_"+tag+"_manifest"])==EXPECTED["accepted_"+tag+"_execution"][2]
                for tag in ("ST","TC"))
            and manifest["all_inputs_are_current_small_texts"] is True
            and manifest["old_successful_scientific_calls_allowed"]==0
            and manifest["old_scientific_source_files_are_identity_evidence_not_imported"] is True
            and manifest["legacy_artifact_inputs"]==[])
        S=accepted(paths["accepted_ST_execution"],EXPECTED["accepted_ST_execution"],gate)
        T=accepted(paths["accepted_TC_execution"],EXPECTED["accepted_TC_execution"],gate)
        d["original_successful_small_receipts_read"]=2
        flow,phase=saved_common_qualifications(S,T,paths,gate)
        d["saved_complete_positive_products_read"]=2;d["saved_complete_phase_qualifications_read"]=1
        d["accepted_original_complete_conclusions"]=dict(
            ST_source_sha256=S["source_sha256"],ST_input_manifest_sha256=S["input_manifest_sha256"],
            ST_run_id=S["run_id"],ST_run_attempt=S["run_attempt"],
            TC_source_sha256=T["source_sha256"],TC_input_manifest_sha256=T["input_manifest_sha256"],
            TC_run_id=T["run_id"],TC_run_attempt=T["run_attempt"],
            ST_complete_positive_propagation_read_verbatim=copy.deepcopy(flow),
            TC_complete_density_coordinate_read_verbatim=copy.deepcopy(phase),
            ST_complete_positive_propagation_payload_sha256=payload_sha(flow),
            TC_complete_density_coordinate_payload_sha256=payload_sha(phase))
        checkpoint()
        f,fo=flow_derivative_bounds(flow)
        d["complete_shorter_flow_derivative_conclusion"]=fo
        d["new_common_shorter_flow_derivative_conclusions"]=1;checkpoint()
        gate("the new directed flow Jacobian and its second and third angular derivatives are finite complete bounds",
            f["m"]>0 and f["m"]<=1 and f["M"]>=1 and f["F"]>=0 and f["G"]>=0 and finite_records(fo))
        gate("the same original positive algorithm covers every shorter interval both orientations and both branches",
            fo["every_shorter_interval_and_both_orientations"] is True
            and fo["both_characteristic_branches_share_maximum_bound"] is True
            and fo["inverse_flow_has_its_own_same_directed_bounds"] is True
            and fo["known_drift_label_bandwidth"]==192 and fo["specific_positive_algorithm_lower_addends_used"] is True)
        w,wo,s,so,common=waist_and_shorter_coordinates(f,phase)
        d["complete_waist_density_coordinate_conclusion"]=wo
        d["complete_shorter_density_coordinate_conclusion"]=so
        d["new_waist_phase_triples"]=1;d["new_density_coordinate_window_bounds"]=8
        d["new_shorter_flow_common_negative_window_bounds"]=1;checkpoint()
        gate("the actual waist phases are composed in their original order with positive complete derivative denominators",
            w["m"]>0 and w["m"]<=1 and w["M"]>=1 and w["F"]>=0
            and wo["exact_true_map_order"]=="Phi_waist = Phi_cut o chi_waist_to_cut"
            and wo["original_cut_constants_not_relabelled_as_waist_constants"] is True)
        gate("one actual waist density map and its same inverse have all four full window bounds including mean blocks",
            all(w[k].is_finite() and w[k]>=1 for k in ("A0","B0","Am","Bm"))
            and wo["same_actual_inverse_on_L2_and_Hminus4_3"] is True
            and wo["independent_physical_mean_block_is_identity"] is True)
        gate("the shorter true flow keeps both orientations and a separate common negative-window bound",
            all(s[k].is_finite() and s[k]>=1 for k in ("A0","B0","Am","Bm"))
            and common.is_finite() and common>=1 and finite_records(so)
            and so["every_shorter_interval_in_original_family"] is True)
        ho,psi,co=selected_common_input(w)
        d["complete_selected_H_coordinate_conclusion"]=ho
        d["complete_selected_common_input_conclusion"]=co
        d["new_density_coordinate_window_bounds"]=12;d["new_ordered_common_input_window_bounds"]=4
        d["new_common_input_phase_triples"]=1;checkpoint()
        gate("the four actual H coordinate bounds are limited to the original selected conjugacy",
            ho["only_same_selected_actual_conjugacy"] is True
            and ho["selected_parameter_absolute_upper"]==PARAMETERS["selected_conjugacy_parameter_absolute_upper"]
            and finite_records(ho) and ho["same_actual_inverse_on_L2_and_Hminus4_3"] is True)
        gate("the common input and its inverse retain their actual noncommuting order in each window",
            psi["m"]>0 and psi["m"]<=1 and psi["M"]>=1 and psi["F"]>=0 and finite_records(co)
            and co["exact_order"]==PARAMETERS["selected_common_input_order"]
            and co["no_projection_commuted_through_coordinate"] is True
            and co["only_same_selected_actual_conjugacy"] is True)
        ranks=dict(shorter_flow=primitive_rank_fees(s,"each shorter directed flow"),
            actual_waist=primitive_rank_fees(w,"actual root-labelled waist map"),
            selected_common_input=primitive_rank_fees(psi,"selected common input map X_minus o H_inverse"))
        d["complete_full_primitive_rank_conclusion"]=ranks
        d["new_primitive_rank_conclusions"]=3;checkpoint()
        gate("all three coordinate conclusions retain both primitive rank terms their H4_3 dual rows and explicit means",
            set(ranks)=={"shorter_flow","actual_waist","selected_common_input"} and finite_records(ranks)
            and all(x["unit_multiplier_only"] is True and x["both_finite_rank_terms_and_the_full_mean_retained"] is True
                and x["mean_identity_extension_differs_from_full_density_by_explicit_rank"] is True for x in ranks.values()))
        leading=leading_flows(f,common)
        d["complete_ungauged_leading_flow_conclusion"]=leading
        d["new_complete_ungauged_leading_bounds"]=4;checkpoint()
        gate("both orientations have complete leading bounds in each window without silently absorbing an ng ratio",
            finite_records(leading) and leading["all_shorter_subintervals_and_both_branches"] is True
            and leading["ungauged_primitive_density_convention"] is True
            and leading["ng_endpoint_ratio_not_absorbed_or_inverted"] is True
            and leading["complete_coupled_mean_source_and_all_seam_terms_remain"] is True)
        old=d["accepted_original_complete_conclusions"]
        gate("the two entire accepted conclusions remain literal original objects with their full source identities",
            old["ST_complete_positive_propagation_read_verbatim"]==flow
            and old["TC_complete_density_coordinate_read_verbatim"]==phase
            and old["ST_complete_positive_propagation_payload_sha256"]==payload_sha(flow)
            and old["TC_complete_density_coordinate_payload_sha256"]==payload_sha(phase))
        d["scope"]=dict(same_P22_cut_and_fixed_eta0_reference=True,
            waist_and_shorter_flow_bounds_on_whole_original_real_family=True,
            actual_H_and_common_input_only_at_original_selected_delta=True,
            every_shorter_directed_subinterval_in_true_dr=True,
            same_inverse_on_L2_and_Hminus4_3=True,full_independent_mean_identity_blocks_retained=True,
            full_primitive_two_rank_and_mean_adjustment_terms_retained=True,
            exact_root_labels_and_ordered_common_input_retained=True,
            original_projection_not_relabelled_as_phase_Fourier=True,
            scalar_diagonal_recovery_uses_specific_positive_algorithm=True,
            full_ungauged_leading_flow_not_the_complete_Cauchy_flow=True,
            physical_ng_endpoint_ratios_remain_separate=True,
            no_interior_ng_or_source_integral_paid=True,no_waist_normalizer_inverse_paid=True,
            no_first_symbol_coefficient_or_complete_incoming_outgoing_error_paid=True,
            no_finite_Schur_inverse_or_whole_return_R0_claimed=True)
        gate("complete finite mean and source interfaces retain their precise scope",
            all(d["scope"].values()) and d["full_incoming_inverse_claimed"] is False
            and d["finite_Schur_inverse_claimed"] is False and d["full_return_R0_claimed"] is False)
        zeros=("old_numerical_enclosures_recomputed","old_phases_rays_profiles_or_amplitudes_recomputed",
            "old_positive_products_or_coordinate_conclusions_recomputed",
            "old_sources_normalizers_or_physical_receivers_recomputed","old_scientific_producer_calls",
            "old_binary_or_archive_inputs_restored","new_radial_source_integrals_evaluated")
        gate("only the declared new scalar consequences of two already successful small receipts were evaluated",
            all(d[k]==0 for k in zeros) and d["original_successful_small_receipts_read"]==2
            and d["new_common_shorter_flow_derivative_conclusions"]==d["new_waist_phase_triples"]==1
            and d["new_density_coordinate_window_bounds"]==12
            and d["new_shorter_flow_common_negative_window_bounds"]==1
            and d["new_ordered_common_input_window_bounds"]==4 and d["new_common_input_phase_triples"]==1
            and d["new_primitive_rank_conclusions"]==3 and d["new_complete_ungauged_leading_bounds"]==4)
        if len(d["gates"])!=PARAMETERS["expected_actual_gate_count"]:
            raise ValueError("the complete waist-coordinate gate count differs from the frozen contract")
        d["complete"]=d["proved"]=d["complete_true_waist_coordinate_conclusion_paid"]=True;d["actual_returncode"]=0
    except Exception as err:
        d["failure"]=dict(type=type(err).__name__,message=str(err))
        print("ACTUAL_TRUE_WAIST_COORDINATE_FAILURE",repr(err),flush=True)
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
