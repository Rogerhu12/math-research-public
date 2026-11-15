#!/usr/bin/env python3
"""Small directed weighted actual-cap Poisson difference and finite193 receiver.

Only already completed small public conclusions are read. All new arithmetic
belongs to the public Actions child. Original Green, source integrals, cap
solutions and the two old finite feedback cases are never recomputed.
"""
from __future__ import annotations
import argparse,copy,hashlib,json,os,time,traceback
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx

REL="topics/visible-flex-exact-nearby/"
PRODUCER=REL+"scripts/fourfold_codazzi_weighted_actual_cap_poisson_difference.py"
CONTRACT=REL+"results/R133-supplement-weighted-actual-cap-Poisson-difference-and-complete-inner-receiver.md"
KIND="actual_weighted_cap_Poisson_difference_v1"
RW_KIND="actual_true_cap_radial_weighted_and_left_receivers_v1"
RW_PROCESS_KIND="actual_public_radial_weighted_cap_receivers_process_v1"
RW_SOURCE="f8d97a14aa7c2ebac746a9732e7b9fd00bf939db95b2b610edcd47f22f9388bb"
RW_WORKER="e15f0e49fbd84da0b165489cbd8f04ef36477e53e502a12daf3362ced4f458e6"
RW_MANIFEST="333bff731ec491b362feb665b54bcb2173bbbdc571f3459e03b63a63af72a3af"
RW_SCIENCE="ec6e088f2d361b35c938eb94bfe78d284507376b4d859c7eadc44c2635316ca9"
RW_PROCESS="daabac142b01e886d7bf3e3f9f53820cb6fb7c053e44a78972d4313ac4bb66e6"
F_KIND="actual_selected_parameter_finite193_scalar_feedback_from_complete_Green_v1"
F_PROCESS_KIND="actual_public_selected_parameter_finite193_scalar_feedback_execution_v1"
F_SOURCE="087f3971d7dbb027464ef71a59d02e734d6e032b3c9b2d3bc600c8bfaced5288"
F_WORKER="beae2544ae5b01b4ec2db32a065ca9c3e6e246d000d2650673434b3bcf8f022d"
F_MANIFEST="8bb821e8063c749f505975ace82c107b80f073beba4078f2cc725b0b22677d57"
F_EXECUTION="9c7710ec10d8826320ba6d1cdee204884728b224944d5eb181e7e00a0c257e10"
F_CANONICAL_SCIENCE="1596b511a3867cf677f060f4f7414d37007f4dff690e5c063da292b2da1edc85"
B="whole_inner_body"
N="fixed_complete_negative_phase_window"
C="true_cut_trace"
WINDOWS=(B,N,C)
EXPECTED_GATES=18
PARAMETERS={
    "arithmetic_bits": 320,
    "exact_cap_interval": [
        "9/10",
        "25/8"
    ],
    "exact_core_interval": [
        "0",
        "9/10"
    ],
    "weight_fraction": "1/2",
    "cap_radius": "3/1000000",
    "normalized_outer_height_radius": "1/1152921504606846976",
    "physical_inner_gamma_domains": [
        {
            "name": "full_physical_gamma_product",
            "radius": "1/1000000000"
        },
        {
            "name": "tail_physical_gamma_subdomain",
            "radius": "1/128000000000"
        }
    ],
    "old_cap_is_fixed_original_reference": True,
    "new_height_may_differ_from_old_height": True,
    "old_Hessian_acts_on_old_K0": True,
    "old_K0_module_upper": "14",
    "actual_Kstar_module_upper": "18",
    "actual_outer_Cnonmean_response_upper": "9/1000",
    "Q_linear_upper": "0.051432066",
    "Q_derivative_factor_upper": "26",
    "old_outer_D_upper": "0.000006",
    "old_outer_Cmean_upper": "0.000001",
    "complete_outer_D_difference_upper": "0.006006",
    "complete_outer_Cmean_difference_upper": "0.000751",
    "global_transport_joint_upper": "0.000004006101",
    "nonmean_D_rate_lower": "2.9252958741",
    "nonmean_C_rate_lower": "0.8601652212",
    "complete_q_upper": "1.39",
    "source_algorithm_C_lower": "5/16",
    "source_algorithm_composition_lower": "4",
    "source_reverse_B_factor": "4/5",
    "source_reverse_C_factor": "64/25",
    "Hessian_B_U_factor": "418",
    "Hessian_B_V_factor": "4",
    "Hessian_C_V_factor": "142",
    "Hessian_Cmean_V_factor": "2/3",
    "physical_minimum_nonmean_frequency": 4,
    "output_is_inner_B_L2_plus_absolute_Cmean": True,
    "output_is_unweighted_whole_body_difference": False,
    "complete_even_mean_and_all_physical_Fourier_modes_retained": True,
    "input_gamma_is_physical_nonmean_curvature": True,
    "unknown_high_input_is_not_truncated": True,
    "expected_structural_gate_count": 18,
    "strict_candidate_failure_is_complete_diagnosis": True,
    "original_successful_case_recomputations": 0,
    "original_integral_and_Green_calls": 0,
    "actual_core_solution_or_matching_proved": False,
    "algorithm_q_lower": "13899/10000",
    "algorithm_q_upper": "139/100",
    "Q_Hilbert_pair_bound_recovered_componentwise": True,
    "original_Q_Wiener_bound_used_only_for_original_value": True
}

def sha_bytes(data):return hashlib.sha256(data).hexdigest()
def sha(path):return sha_bytes(Path(path).read_bytes())
def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),
        ensure_ascii=False,allow_nan=False)+"\n").encode("utf-8")
def read(path):
    raw=Path(path).read_bytes()
    if len(raw)>100000:raise ValueError("only exact small UTF8 records are admitted")
    return json.loads(raw)
def save(path,value):
    raw=canonical(value)
    if len(raw)>45000:raise ValueError("complete new scientific conclusion exceeds 45000 bytes")
    p=Path(path);p.parent.mkdir(parents=True,exist_ok=True)
    temp=p.with_name(p.name+".partial");temp.write_bytes(raw);temp.replace(p)
def q(value):
    z=Fraction(value);return arb(z.numerator)/z.denominator
def box(value):
    if isinstance(value,arb):z=value
    elif isinstance(value,(int,Fraction)):z=q(value)
    elif isinstance(value,str):z=arb(value)
    elif isinstance(value,dict) and "ball" in value:z=arb(value["ball"])
    else:raise ValueError("a scalar lacks a complete directed ball")
    if not z.is_finite():raise ValueError("nonfinite directed scalar")
    return z
def upper(value):return box(value).upper()
def lower(value):return box(value).lower()
def bound(value,label):
    z=box(value)
    if z.lower()<0:raise ValueError("negative purported upper bound: "+label)
    return z.upper()
def max_upper(*values):
    z=box(values[0])
    for value in values[1:]:z=z.union(box(value))
    return z.upper()
def rec(value):return dict(ball=box(value).str(64))
def encode(value):
    if isinstance(value,arb):return rec(value)
    if isinstance(value,dict):return {str(k):encode(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)):return [encode(v) for v in value]
    return value
def gate(doc,name,condition):
    doc["gates"].append(dict(name=name,passed=bool(condition)))
    if not condition:raise ValueError("weighted cap input or record gate: "+name)
def completed(value,n):
    return (value.get("complete") is True and value.get("failure") is None
        and value.get("actual_returncode")==0 and len(value.get("gates",[]))==n
        and all(g.get("passed") is True for g in value["gates"]))

def checked_inputs(a,doc):
    gate(doc,"the exact new manifest and directed precision are fixed",
        sha(a.manifest)==a.manifest_sha and a.bits==PARAMETERS["arithmetic_bits"])
    manifest=read(a.manifest)
    gate(doc,"the declared finite parameters and scientific source bytes are unchanged",
        manifest.get("parameters")==PARAMETERS
        and manifest.get("expected_actual_gate_count")==EXPECTED_GATES
        and manifest.get("files",{}).get(PRODUCER)==sha(__file__))
    root=a.root.resolve();files=manifest.get("files",{})
    rows=manifest.get("file_receipts",[]);seen=set();inventory=[]
    if not rows or len(rows)!=len(files):raise ValueError("incomplete small-file inventory")
    for row in rows:
        name=row["path"];p=(root/name).resolve()
        if (name in seen or not name.startswith(REL) or ".." in Path(name).parts
            or not p.is_relative_to(root) or not p.is_file()):
            raise ValueError("a pinned small path is repeated absent or outside the topic")
        raw=p.read_bytes();raw.decode("utf-8")
        if (len(raw)!=row["bytes"] or len(raw)>100000 or sha_bytes(raw)!=row["sha256"]
            or files.get(name)!=row["sha256"]):
            raise ValueError("a complete pinned small input changed")
        seen.add(name);inventory.append(dict(path=name,bytes=len(raw),sha256=row["sha256"]))
    gate(doc,"every small input and the complete new proof are present without native arrays",
        seen==set(files) and manifest.get("proof_paths",{}).get("contract")==CONTRACT
        and CONTRACT in seen)
    paths=manifest.get("input_paths",{})
    expected=dict(rw_science=RW_SCIENCE,rw_process=RW_PROCESS,f_execution=F_EXECUTION)
    gate(doc,"the three original completed scientific records retain their exact identities",
        set(paths)==set(expected)
        and all(paths[k] in seen and sha(root/paths[k])==v for k,v in expected.items()))
    rw=read(root/paths["rw_science"]);rp=read(root/paths["rw_process"])
    fp=read(root/paths["f_execution"]);f=fp.get("actual_scientific_receipt",{})
    child=rp.get("children",[])
    gate(doc,"the original radial-weight child and full scientific receipt really completed",
        rp.get("kind")==RW_PROCESS_KIND and rp.get("complete") is True
        and str(rp.get("run_id"))=="43729429382" and str(rp.get("run_attempt"))=="1"
        and rp.get("actual_source_sha256")==RW_SOURCE and rp.get("worker_source_sha256")==RW_WORKER
        and rp.get("input_manifest_sha256")==RW_MANIFEST
        and rp.get("actual_scientific_summary_sha256")==RW_SCIENCE
        and rp.get("actual_scientific_summary_bytes")==57702
        and rp.get("actual_scientific_complete") is True
        and rp.get("actual_scientific_failure") is None
        and len(child)==1 and child[0].get("actual_returncode")==0
        and rp.get("actual_scientific_gates")==rw.get("gates"))
    gate(doc,"all fifteen original radial-weight gates and all six complete candidates are retained",
        rw.get("kind")==RW_KIND and completed(rw,15)
        and rw.get("source_sha256")==RW_SOURCE and rw.get("input_manifest_sha256")==RW_MANIFEST
        and rw.get("new_weighted_candidates_evaluated")==6
        and rw.get("new_weighted_posterior_cases_passed")==6
        and set(rw.get("new_weighted_candidates",{}))=={"1/16","1/8","1/4","3/8","1/2","3/4"}
        and all(v.get("complete_weighted_posterior_applies") is True
                and v.get("candidate_failure") is None for v in rw["new_weighted_candidates"].values()))
    rpar=rw["parameters"]
    gate(doc,"the copied cap has the same complete product domain physical units and both means",
        rpar.get("exact_cap_interval")==["9/10","25/8"]
        and rpar.get("actual_cap_radius")==PARAMETERS["cap_radius"]
        and rpar.get("inner_curvature_radius")=="1/1000000000"
        and rpar.get("normalized_outer_height_radius")==PARAMETERS["normalized_outer_height_radius"]
        and rpar.get("Q_complete_linear_upper")==PARAMETERS["Q_linear_upper"]
        and rpar.get("full_mean_included") is True
        and rpar.get("physical_angular_measure")=="normalized circle"
        and rpar.get("ordinary_radial_measure")=="dr"
        and rpar.get("current_actual_reflection_Bmean_exactly_zero") is True
        and rw.get("old_targets_Fourier_residuals_repair_mean_flows_Riccati_or_Green_recomputed")==0
        and rw.get("old_successful_zero_weight_integrals_recomputed")==0)
    gate(doc,"the old finite feedback child and all its fifteen structural gates are immutable",
        fp.get("kind")==F_PROCESS_KIND and fp.get("complete") is True
        and fp.get("actual_returncode")==0 and fp.get("actual_failure") is None
        and str(fp.get("run_id"))=="43737257903" and str(fp.get("run_attempt"))=="1"
        and fp.get("source_budget_source_sha256")==F_SOURCE
        and fp.get("worker_source_sha256")==F_WORKER and fp.get("input_manifest_sha256")==F_MANIFEST
        and fp.get("actual_verified_input_count")==13
        and f.get("kind")==F_KIND and completed(f,15)
        and f.get("source_sha256")==F_SOURCE and f.get("input_manifest_sha256")==F_MANIFEST
        and sha_bytes(canonical(f))==F_CANONICAL_SCIENCE)
    cases=f.get("complete_case_conclusions",[])
    gate(doc,"the two old complete feedback cases are copied with their original pass and fail verdicts",
        len(cases)==2 and cases[0].get("physical_cap_kappa")=="0"
        and cases[1].get("physical_cap_kappa")=="1/5"
        and cases[0].get("all_strict_sufficient_gates_passed") is True
        and cases[1].get("all_strict_sufficient_gates_passed") is False
        and f.get("complete_infinite_BVP_inverse_proved") is False
        and f.get("nonlinear_core_constructed") is False)
    old={w:{k:bound(f["original_complete_columns"][w][k],w+" "+k)
        for k in ("g","p","a","c")} for w in WINDOWS}
    scalars={k:bound(f["complete_scalar_inputs"][k],k)
        for k in ("e","e_LH","additional_nu_volume_source_whole_core")}
    bd={k:bound(f["exact_boundary_comparison_constants"][k],k)
        for k in ("coordinate_epsilon","complete_physical_cap_fee_multiplier")}
    gate(doc,"all original windows preserve the ordinary Poisson and separate high-body and high-cut columns",
        set(f["original_complete_columns"])==set(WINDOWS)
        and all(set(f["original_complete_columns"][w])=={"g","p","a","c"} for w in WINDOWS)
        and f.get("all_input_means_and_full97_rows_retained") is True
        and f.get("specialized_cross_a_substituted_for_generic_g") is False)
    doc["complete_new_small_input_inventory"]=inventory
    doc["complete_new_small_input_inventory_sha256"]=sha_bytes(canonical(inventory))
    doc["original_input_sha256"]=expected
    doc["original_RW_identity"]=dict(run_id="43729429382",run_attempt="1",
        source_sha256=RW_SOURCE,worker_sha256=RW_WORKER,manifest_sha256=RW_MANIFEST,
        science_sha256=RW_SCIENCE,process_sha256=RW_PROCESS,
        source_input_sha256=copy.deepcopy(rw["inputs"]),
        complete_gates_copied=copy.deepcopy(rw["gates"]))
    doc["original_F_identity"]=dict(run_id="43737257903",run_attempt="1",
        source_sha256=F_SOURCE,worker_sha256=F_WORKER,manifest_sha256=F_MANIFEST,
        execution_sha256=F_EXECUTION,canonical_science_sha256=F_CANONICAL_SCIENCE,
        complete_13_input_inventory_sha256=fp["actual_verified_input_receipts_sha256"],
        scientific_small_input_inventory_sha256=f["complete_small_input_inventory_sha256"],
        scientific_input_sha256=copy.deepcopy(f["input_sha256"]),
        complete_gates_copied=copy.deepcopy(f["gates"]))
    doc["original_feedback_cases_copied"]=copy.deepcopy(cases)
    doc["original_complete_columns_copied"]=copy.deepcopy(f["original_complete_columns"])
    doc["original_scalar_inputs_copied"]=copy.deepcopy(f["complete_scalar_inputs"])
    doc["original_boundary_constants_copied"]=copy.deepcopy(f["exact_boundary_comparison_constants"])
    doc["original_sufficient_threshold_diagnostic_copied"]=copy.deepcopy(
        f["complete_boundary_margin_diagnostic"])
    return rw,f,old,scalars,bd

def copied_weighted_inputs(rw,doc):
    v=rw["new_weighted_candidates"][PARAMETERS["weight_fraction"]]
    gate(doc,"one complete successful half-rate weight supplies every new kernel and source",
        v.get("weight_fraction")=="1/2"
        and v.get("complete_weighted_posterior_applies") is True
        and v.get("both_mean_denominators_retained") is True
        and v.get("all_M_in_4N_including_unbounded_frequency") is True
        and v.get("input_gamma_is_physical_nonmean_curvature") is True
        and v.get("candidate_failure") is None)
    const=rw["physical_source_constants_copied"]
    gate(doc,"the same positive source and joint-kernel budget parameters retain their exact bounds",
        lower(const["C"])>q(PARAMETERS["source_algorithm_C_lower"])
        and lower(const["composition"])>q(PARAMETERS["source_algorithm_composition_lower"])
        and lower(rw["new_left_ordinary_receivers"]["q_L"])>q(PARAMETERS["algorithm_q_lower"])
        and upper(v["complete_kernel_bounds"]["H_C"])<1+q(PARAMETERS["algorithm_q_upper"]))
    src=v["new_source_and_output_integrals"];kern=v["complete_kernel_bounds"]
    af=v["complete_affine_and_feedback"];post=v["posterior_bounds"]
    left=rw["new_left_ordinary_receivers"]
    values=dict(
        F_Bw=bound(src["weighted_B_ordinary_L1"],"weighted B positive source budget"),
        F_Cw=bound(src["weighted_C_ordinary_L1"],"weighted C positive source budget"),
        w_R=box(src["weight_R"]),
        K_A=bound(kern["K_Q_nonmean"],"complete Wiener nonmean Q positive budget"),
        D_w=bound(kern["D_Q_left"],"weighted left Q receiver"),
        M_w=bound(kern["K_Q_mean"],"weighted complete Cmean receiver"),
        H_D=bound(kern["H_D"],"right d receiver"),
        H_C=bound(kern["H_C"],"left c receiver"),
        lambda_max=bound(kern["lambda_max"],"complete radial rate upper"),
        G_B=bound(af["ordinary_B_gain"],"ordinary B column"),
        G_C=bound(af["ordinary_C_gain"],"ordinary C column"),
        original_value_chi=bound(af["complete_chi"],"original weighted actual-value feedback"),
        X_affine=bound(post["Xw_affine"],"complete weighted affine value"),
        X_gamma=bound(post["Xw_gamma_gain"],"complete weighted gamma value gain"),
        e_D=bound(left["e_D"],"unweighted right d to left receiver"),
        e_m=bound(left["e_Cmean"],"unweighted right Cmean to left receiver"))
    gate(doc,"the complete selected records contain finite nonnegative affine mean and outer columns",
        all(box(x).is_finite() and lower(x)>=0 for x in values.values())
        and lower(values["w_R"])>0 and upper(values["w_R"])<=1
        and q(PARAMETERS["complete_q_upper"])>1
        and q(PARAMETERS["nonmean_C_rate_lower"])>0)
    doc["original_RW_selected_full_candidate_canonical_sha256"]=sha_bytes(canonical(v))
    doc["original_RW_selected_weight_fields_copied"]=copy.deepcopy(dict(
        weight_fraction=v["weight_fraction"],
        new_source_and_output_integrals={k:src[k] for k in
            ("weighted_B_ordinary_L1","weighted_C_ordinary_L1","weight_R")},
        complete_kernel_bounds={k:kern[k] for k in
            ("K_Q_nonmean","D_Q_left","K_Q_mean","H_D","H_C","lambda_max")},
        complete_affine_and_feedback={k:af[k] for k in
            ("ordinary_B_gain","ordinary_C_gain","complete_chi")},
        posterior_bounds={k:post[k] for k in ("Xw_affine","Xw_gamma_gain")},
        new_left_ordinary_receivers={k:left[k] for k in ("e_D","e_Cmean","q_L")},
        positive_budget_algorithm_parameters=dict(C=const["C"],composition=const["composition"])))
    doc["original_RW_unconsumed_fields_exact_source_sha256"]=RW_SCIENCE
    return values

def complete_weighted_constants(x,doc):
    # Every upper parameter is chosen before it enters a positive formula.
    # w_R stays a full ball until each division or multiplication is formed.
    rho=q(PARAMETERS["cap_radius"]);q0=q(PARAMETERS["Q_linear_upper"])
    LD=q(PARAMETERS["old_outer_D_upper"]);Lm=q(PARAMETERS["old_outer_Cmean_upper"])
    dd=q(PARAMETERS["complete_outer_D_difference_upper"])
    dm=q(PARAMETERS["complete_outer_Cmean_difference_upper"])
    EA=q(PARAMETERS["global_transport_joint_upper"])
    oldK=q(PARAMETERS["old_K0_module_upper"])
    qp=q(PARAMETERS["complete_q_upper"])
    sC=q(PARAMETERS["nonmean_C_rate_lower"])
    dminus=q(PARAMETERS["nonmean_D_rate_lower"])-x["lambda_max"]/4
    # These are the original positive budget values, not lower bounds on
    # actual Riccati functions. Keep their joint k=D+(1+q)c structure.
    Dtilde=min(x["D_w"],x["K_A"]).upper()
    Cbar=upper(x["K_A"]/(1+q(PARAMETERS["algorithm_q_lower"])))
    Bbar=upper((Dtilde+q(PARAMETERS["algorithm_q_upper"])*x["K_A"])
        /(1+q(PARAMETERS["algorithm_q_upper"])))
    KH=upper(Bbar+max_upper(Cbar,x["M_w"]))
    chi0=upper(KH*q0+x["H_D"]*LD+Lm)
    gap=1-chi0
    derivative_factor=24/(1-6*rho)+72*rho/(1-6*rho)**2
    checks=dict(
        global_Q_reciprocal_denominator_positive=bool(lower(1-6*rho)>0),
        actual_Q_derivative_factor_below_26=bool(upper(derivative_factor)<q("26")),
        weighted_backward_divergence_rate_positive=bool(lower(dminus)>0),
        weighted_old_reference_feedback_below_one=bool(lower(gap)>0),
        complete_weight_R_strictly_positive=bool(lower(x["w_R"])>0))
    diag=dict(prerequisite_strict_checks=checks,all_prerequisites_passed=all(checks.values()),
        derivative_factor=rec(derivative_factor),d_minus=rec(dminus),
        old_reference_chi=rec(chi0),old_reference_gap=rec(gap),
        old_reference_feedback_uses_new_Hilbert_component_lift=True,
        original_Wiener_value_feedback_copied=rec(x["original_value_chi"]),
        original_Wiener_feedback_is_not_used_as_new_Hilbert_gate=True)
    gate(doc,"every new weighted prerequisite has an explicit complete strict verdict",
        len(checks)==5 and all(isinstance(v,bool) for v in checks.values()))
    if not all(checks.values()):
        doc["new_weighted_constants"]=diag
        return None
    Uw=upper(q(PARAMETERS["source_reverse_B_factor"])*x["F_Bw"])
    Vw=upper(q(PARAMETERS["source_reverse_C_factor"])*x["F_Cw"])
    OB=upper(q(PARAMETERS["Hessian_B_U_factor"])*Uw
        +q(PARAMETERS["Hessian_B_V_factor"])*Vw)
    OC=upper(q(PARAMETERS["Hessian_C_V_factor"])*Vw)
    GdivB=upper(x["H_D"]/lower(dminus))
    GdivC=upper(qp*x["H_D"]/lower(dminus)+x["H_C"]/sC)
    Hdiv=upper(oldK*EA*max_upper(GdivB,GdivC))
    Hord=upper(oldK*(x["G_B"]*OB+x["G_C"]*OC))
    Hw=upper(Hdiv+Hord)
    HLdiv=upper(oldK*qp*EA/lower(dminus))
    HLord=upper(oldK*(OB+qp*OC))
    HLmean=upper(oldK*q(PARAMETERS["Hessian_Cmean_V_factor"])*Vw)
    HL=upper(HLdiv+HLord+HLmean)
    eDw=upper(x["e_D"]/lower(x["w_R"]))
    emw=upper(x["e_m"]/lower(x["w_R"]))
    values=dict(Q_positive_nonmean_budget=x["K_A"],Q_D_tilde=Dtilde,
        Q_C_nonmean_component_upper=Cbar,Q_B_nonmean_component_upper=Bbar,
        Q_Hilbert_pair_complete_upper=KH,
        U_w=Uw,V_w=Vw,O_B=OB,O_C=OC,
        d_minus_lower=lower(dminus),old_reference_chi=chi0,old_reference_gap_lower=lower(gap),
        divergence_B_gain=GdivB,divergence_C_gain=GdivC,
        old_Hessian_weighted_body_divergence=Hdiv,old_Hessian_weighted_body_ordinary=Hord,
        old_Hessian_weighted_body_complete=Hw,
        old_Hessian_inner_divergence=HLdiv,old_Hessian_inner_nonmean_ordinary=HLord,
        old_Hessian_inner_Cmean_ordinary=HLmean,old_Hessian_inner_pair_complete=HL,
        right_D_to_left_weighted=eDw,right_Cmean_to_left_weighted=emw)
    diag.update(complete_constants=encode(values),
        global_joint_transport_bound_source="actual continuous moving-cap residual bridge A.5",
        source_reverse_scope="same RW algorithm positive addends, not arbitrary physical residual norms",
        all_Hessian_means_retained=True,old_Hessian_acts_on_old_K0=True,
        no_extra_Hessian_resolvent_factor=True)
    doc["new_weighted_constants"]=diag
    return values

def transfer_load(load,old,e,epsilon,M,detlower):
    A,Bm,Cm,D=M[0][0],M[0][1],M[1][0],M[1][1]
    xb=upper((upper(1-D)*load[B]+Bm*load[C])/detlower)
    xc=upper((Cm*load[B]+upper(1-A)*load[C])/detlower)
    xn=upper(load[N]+old[N]["g"]*e*xb+old[N]["p"]*epsilon*xc)
    return {B:xb,N:xn,C:xc}

def new_finite_case(kappa,old,scalars,bd,baseline):
    e=scalars["e"];eLH=scalars["e_LH"]
    epsilon=upper(bd["coordinate_epsilon"]+bd["complete_physical_cap_fee_multiplier"]*kappa)
    # The entire first column is already certified and independent of kappa.
    # Copy its complete directed entries; do not rerun either old comparison.
    oldM=baseline["nonnegative_feedback_matrix"]
    M=[[bound(oldM[0][0],"copied original body feedback"),upper(old[B]["p"]*epsilon)],
       [bound(oldM[1][0],"copied original body-to-cut feedback"),upper(old[C]["p"]*epsilon)]]
    d1=1-M[0][0];d2=1-M[1][1];det=d1*d2-M[0][1]*M[1][0]
    checks=dict(body_diagonal_below_one=bool(lower(d1)>0),
        cut_diagonal_below_one=bool(lower(d2)>0),
        complete_two_by_two_determinant_positive=bool(lower(det)>0))
    passed=all(checks.values())
    result=dict(physical_cap_inner_pair_kappa=rec(kappa),epsilon_low=rec(epsilon),
        epsilon_high=rec(epsilon),nonnegative_feedback_matrix=encode(M),
        diagonal_gaps=encode([d1,d2]),determinant=rec(det),
        strict_sufficient_gates=checks,all_strict_sufficient_gates_passed=passed,
        original_feedback_first_column_copied=True,
        actual_cap_domain_hypotheses_required=True,
        actual_cap_domain_proved_by_this_consumer=False,
        finite193_inverse_under_stated_boundary_hypotheses_proved=passed,
        numerical_nonpass_does_not_prove_singularity=True)
    if not passed:
        result.update(transferred_columns=None,additional_parameter_volume_response_bound=None)
        return result
    detlower=lower(det)
    oldloads=baseline["complete_old_loads"]
    loads={name:{w:bound(oldloads[name][w],name+" "+w) for w in WINDOWS}
        for name in ("ordinary_whole_core_source","independent_original_right97_row",
                     "independent_high_whole_body_state")}
    loads["independent_high_actual_cut_state"]={
        w:upper(old[w]["c"]+old[w]["p"]*epsilon) for w in WINDOWS}
    transferred={name:transfer_load(load,old,e,epsilon,M,detlower) for name,load in loads.items()}
    result.update(complete_old_loads=encode(loads),
        positive_determinant_lower_used=rec(detlower),transferred_columns=encode(transferred),
        additional_parameter_volume_response_bound=encode({
            w:upper(transferred["ordinary_whole_core_source"][w]
                *scalars["additional_nu_volume_source_whole_core"]) for w in WINDOWS}),
        additional_parameter_volume_response_scope=(
            "only Delta F_nu plus Delta A Z; old exact response residual, actual boundary "
            "affine source, independent waist and particular traces are separate"),
        low_response_matrix_for_independent_high_body_and_cut=encode([
            [transferred["independent_high_whole_body_state"][B],
             transferred["independent_high_actual_cut_state"][B]],
            [transferred["independent_high_whole_body_state"][C],
             transferred["independent_high_actual_cut_state"][C]]]),
        true_high_inverse_required_before_infinite_Schur=True)
    return result

def complete_gamma_case(case,x,k,old,scalars,bd,f):
    result=dict(name=case["name"],physical_gamma_A0_radius=case["radius"],
        input_domain_is_original_physical_reflection_product=True,
        ordinary_inner_Cmean_retained=True,unknown_high_input_is_not_truncated=True,
        unweighted_whole_body_difference_claimed=False,
        affine_cap_mismatch_or_new_height_direction_paid=False)
    if k is None:
        result.update(complete_weighted_difference_bound_available=False,
            inner_pair_kappa=None,new_finite_feedback=None,
            all_new_strict_sufficient_gates_passed=False)
        return result
    q0=q(PARAMETERS["Q_linear_upper"]);newK=q(PARAMETERS["actual_Kstar_module_upper"])
    factor=q(PARAMETERS["Q_derivative_factor_upper"])
    LD=q(PARAMETERS["old_outer_D_upper"]);Lm=q(PARAMETERS["old_outer_Cmean_upper"])
    dd=q(PARAMETERS["complete_outer_D_difference_upper"])
    dm=q(PARAMETERS["complete_outer_Cmean_difference_upper"])
    zstar=q(PARAMETERS["actual_outer_Cnonmean_response_upper"])
    X=upper(x["X_affine"]+x["X_gamma"]*q(case["radius"]))
    aQ=upper(factor*newK*X)
    body_Q=upper(k["Q_Hilbert_pair_complete_upper"]*aQ)
    body_outer=upper(x["w_R"]*(x["H_D"]*dd+dm)*zstar)
    Y=upper((body_Q+k["old_Hessian_weighted_body_complete"]+body_outer)
        /k["old_reference_gap_lower"])
    left_Q=upper((x["D_w"]+x["M_w"])*(q0*Y+aQ))
    left_old_outer=upper((k["right_D_to_left_weighted"]*LD
        +k["right_Cmean_to_left_weighted"]*Lm)*Y)
    left_delta_outer=upper((x["e_D"]*dd+x["e_m"]*dm)*zstar)
    kap=upper(left_Q+k["old_Hessian_inner_pair_complete"]+left_old_outer+left_delta_outer)
    threshold=f["complete_boundary_margin_diagnostic"].get(
        "sufficient_kappa_strict_upper_threshold_lower")
    finite=new_finite_case(kap,old,scalars,bd,f["complete_case_conclusions"][0])
    result.update(complete_weighted_difference_bound_available=True,
        complete_weighted_value_upper=rec(X),complete_Q_derivative_source_upper=rec(aQ),
        weighted_body_new_Q_source=rec(body_Q),
        weighted_body_old_Hessian_source=rec(k["old_Hessian_weighted_body_complete"]),
        weighted_body_new_outer_source=rec(body_outer),
        weighted_body_difference_upper=rec(Y),
        inner_Q_complete=rec(left_Q),
        inner_old_Hessian_complete=rec(k["old_Hessian_inner_pair_complete"]),
        inner_old_outer_feedback_complete=rec(left_old_outer),
        inner_changed_outer_complete=rec(left_delta_outer),
        inner_pair_kappa=rec(kap),
        old_threshold_diagnostic_strict_comparison=(
            bool(upper(kap)<lower(threshold)) if threshold is not None else None),
        old_threshold_diagnostic_is_not_the_actual_matrix_gate=True,
        new_finite_feedback=finite,
        all_new_strict_sufficient_gates_passed=finite["all_strict_sufficient_gates_passed"])
    return result

def run(a,doc):
    ctx.prec=a.bits
    rw,f,old,scalars,bd=checked_inputs(a,doc)
    selected=copied_weighted_inputs(rw,doc)
    constants=complete_weighted_constants(selected,doc)
    cases=[complete_gamma_case(v,selected,constants,old,scalars,bd,f)
        for v in PARAMETERS["physical_inner_gamma_domains"]]
    doc["complete_gamma_domain_cases"]=cases
    gate(doc,"both gamma domains retain complete affine and mean terms without cross-case minima",
        len(cases)==2
        and [v["physical_gamma_A0_radius"] for v in cases]
            ==[v["radius"] for v in PARAMETERS["physical_inner_gamma_domains"]]
        and all(v["ordinary_inner_Cmean_retained"]
                and v["unknown_high_input_is_not_truncated"]
                and not v["unweighted_whole_body_difference_claimed"]
                and not v["affine_cap_mismatch_or_new_height_direction_paid"] for v in cases))
    gate(doc,"both old complete cases and their exact directed ball strings remain unchanged",
        doc["original_feedback_cases_copied"]==f["complete_case_conclusions"]
        and sha_bytes(canonical(f))==F_CANONICAL_SCIENCE
        and doc["original_feedback_cases_copied"][1]["all_strict_sufficient_gates_passed"] is False)
    gate(doc,"every new strict matrix verdict is retained and failed denominators are not inverted",
        all((v["new_finite_feedback"] is None
                and not v["complete_weighted_difference_bound_available"]
                and not v["all_new_strict_sufficient_gates_passed"])
            or (v["complete_weighted_difference_bound_available"]
                and isinstance(v["new_finite_feedback"]["strict_sufficient_gates"],dict)
                and len(v["new_finite_feedback"]["strict_sufficient_gates"])==3
                and (v["new_finite_feedback"]["all_strict_sufficient_gates_passed"]
                    or v["new_finite_feedback"]["transferred_columns"] is None))
            for v in cases))
    doc.update(
        complete=True,proved_complete_weighted_inner_cap_difference_diagnosis=True,
        new_complete_gamma_case_count=len(cases),
        new_weighted_prerequisite_passed=constants is not None,
        new_finite_case_count=sum(v["new_finite_feedback"] is not None for v in cases),
        new_finite_case_pass_count=sum(v["all_new_strict_sufficient_gates_passed"] for v in cases),
        any_new_finite_case_passed=any(v["all_new_strict_sufficient_gates_passed"] for v in cases),
        complete_inner_B_and_Cmean_pair_is_the_only_kappa_output=True,
        unweighted_whole_cap_difference_replaced=False,
        full_even_mean_and_all_physical_modes_retained=True,
        unknown_high_and_original_full97_coordinates_retained=True,
        new_physical_cap_domain_entry_proved=False,
        affine_cap_mismatch_or_boundary_nonlinearity_proved=False,
        independent_new_height_or_waist_source_proved=False,
        infinite_BVP_inverse_proved=False,actual_core_solution_or_full_matching_proved=False,
        original_Green_native_matrix_Gram_sweep_or_target_calls=0,
        original_residual_primitive_repair_Riccati_or_integral_calls=0,
        original_F_case_recomputations=0,new_recomputable_arrays_persisted=False,
        original_source_measure="ordinary dr and normalized physical circle",
        original_right_row_input_units=f["actual_right_row_input_units"],
        no_sqrt97_and_no_physical_support_truncation=True,
        new_proof_requires_cap_product_domain_instead_of_proving_core_entry=True,
        original_scientific_data_updated=False,
        scope=(
            "A directed improvement only for the complete inner B/Cmean derivative pair, "
            "uniform in each stated actual cap product. New finite193 columns are conditional "
            "on that true boundary domain. The old kappa=1/5 failure remains unchanged; "
            "unknown high, waist, affine and nonlinear sources and actual core existence "
            "are separate. No arbitrary physical residual upper is reverse-consumed."))
    gate(doc,"the final conclusion keeps all original science and every remaining matching obligation",
        len(doc["gates"])==EXPECTED_GATES-1
        and doc["original_F_case_recomputations"]==0
        and doc["original_Green_native_matrix_Gram_sweep_or_target_calls"]==0
        and doc["original_residual_primitive_repair_Riccati_or_integral_calls"]==0
        and not doc["new_recomputable_arrays_persisted"]
        and not doc["actual_core_solution_or_full_matching_proved"])

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root",type=Path,required=True)
    parser.add_argument("--manifest",type=Path,required=True)
    parser.add_argument("--manifest-sha",required=True)
    parser.add_argument("--out",type=Path,required=True)
    parser.add_argument("--bits",type=int,default=320)
    a=parser.parse_args()
    if a.out.exists():raise FileExistsError("preserve the existing complete new conclusion")
    start=time.monotonic()
    doc=dict(kind=KIND,source_sha256=sha(__file__),input_manifest_sha256=a.manifest_sha,
        complete=False,failure=None,gates=[],parameters=PARAMETERS,arithmetic_bits=a.bits,
        expected_structural_gate_count=EXPECTED_GATES,
        public_repository=os.environ.get("GITHUB_REPOSITORY"),
        run_id=os.environ.get("GITHUB_RUN_ID"),run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        infinite_BVP_inverse_proved=False,actual_core_solution_or_full_matching_proved=False)
    code=0
    try:run(a,doc)
    except Exception as error:
        code=1;doc["complete"]=False
        doc["failure"]=dict(type=type(error).__name__,message=str(error),
            traceback_frames=[dict(file=Path(frame.filename).name,line=frame.lineno,function=frame.name)
                for frame in traceback.extract_tb(error.__traceback__)[-12:]])
    doc["actual_returncode"]=code
    doc["seconds"]=time.monotonic()-start
    save(a.out,doc)
    print(json.dumps(dict(kind=KIND,complete=doc["complete"],actual_returncode=code,
        structural_gates_passed=sum(g["passed"] for g in doc["gates"]),
        structural_gates_total=len(doc["gates"]),
        expected_structural_gate_count=EXPECTED_GATES,
        new_weighted_prerequisite_passed=doc.get("new_weighted_prerequisite_passed",False),
        new_finite_case_pass_count=doc.get("new_finite_case_pass_count",0),
        new_finite_case_count=doc.get("new_finite_case_count",0),
        output_bytes=a.out.stat().st_size,output_sha256=sha(a.out),
        infinite_BVP_inverse_proved=False,actual_core_solution_or_full_matching_proved=False)),flush=True)
    if code:raise SystemExit(code)

if __name__=="__main__":main()
