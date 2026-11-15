#!/usr/bin/env python3
"""Read saved raw nonmean norms; expose the three-band collar trace costs.

No target, Fourier, polynomial residual, scalar mean flow or old Green
routine is imported or evaluated.  Old successful receipts are immutable.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,time,traceback
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx

PUBLIC="Rogerhu12/math-research-public"
KIND="actual_saved_nonmean_restriction_and_three_band_trace_coefficients_v1"
MANIFEST_KIND="immutable_saved_nonmean_three_band_trace_inputs_v1"
ORIGINAL_MANIFEST="c214f800a5094c905c554e9053c52567d5ae5d76be41ac2e3fe9d673b396d784"
RESPONSE_SUMMARY="7c43eeed609006195893d6ceee5003887e533ac6222515171d27b624e47115ec"
ROW_SOURCE="1651f6cf73af9f3c16061767cc5acff0c452ada183422f7efb983ec8a6d4eb07"
ROW_IDENTITY="78a581852f8a8b126cd98c5461746dd3e8e36ad2a37fb24c8d6a0b1d1c082936"
ROWS_PAYLOAD="06fdb69708f63d27587fb91bb0760b50e23fa8d1719ed8b8903d8be6e922abe6"
D_EXECUTION="6956c214240cd85e6263331b33e0c7efcf6abc3e71190d46ff3eabddecd35071"
D_SOURCE="827fcb237a79b48c095872b61c370ff2ceafc143a8dc6a1774021188ff3ea320"
COLLAR="618bd148e7d75e82c49af5f434235b3792747652a3ff9fb98adc03f560ac2080"
COLLAR_PROCESS="dbe7fe24a53c265ab0e8103b576c722cde8a57d9df0235f585ffe49efae92974"
COLLAR_SOURCE="e39646a5430b062fc48c469439f5bba00a8a1a806777b43fd82d1aebea46ecee"
CENTRE="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
DIRECTION="6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
TRIAL="ed42a71ddeb0420428f0313df321dc1f9b10525521d399cb1d666ae98fe410f6"
PARAMETERS=dict(arithmetic_bits=320,delta_half_width="1/10000000000",
    exact_cut="9/10",available_collar=["17/20","19/20"],
    retained_ell="1/262144",retained_interval=["589819/655360","589829/655360"],
    retained_radii=["1/1048576","1/16777216","1/268435456","1/4294967296","1/68719476736"],
    angular_order=8193,original_rows=7721,original_parts=40,
    raw_nonmean_field="uncorrected_response_nonmean",reference_source_maximum_degree=288,finite_cut_degree=96,far_cut_degree=288,
    full_mean_normalization="normalized circle; coefficient has norm equal to its absolute value",
    original_source_arrays_or_verdicts_modified=False,
    old_numerical_enclosures_recomputed=0)

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def compact(value):return (json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)+"\n").encode()
def read(path):return json.loads(Path(path).read_bytes())
def read_part(path):
    with gzip.open(path,"rb") as stream:return json.loads(stream.read())
def q(value):
    x=value if isinstance(value,Fraction) else Fraction(str(value))
    return arb(x.numerator)/x.denominator
def ball(value):
    if not isinstance(value,dict):raise ValueError("a complete original directed record is required")
    if "lower" in value and "upper" in value:
        result=arb(str(value["lower"])).lower().union(arb(str(value["upper"])).upper())
        if "ball" in value:result=result.union(arb(str(value["ball"])))
        return result
    if "ball" in value:return arb(str(value["ball"]))
    raise ValueError("no complete signed ball")
def up(value):
    if isinstance(value,dict):return ball(value).upper()
    return arb(value).upper()
def low(value):return arb(value).lower()
def nonnegative(value):
    x=up(value)
    if not x>=0:raise ValueError("a positive upper budget became negative")
    return x
def rec(value):return dict(ball=arb(value).str(70))
def save(path,doc):
    p=Path(path);p.parent.mkdir(parents=True,exist_ok=True)
    t=p.with_name(p.name+".partial");t.write_bytes(compact(doc));t.replace(p)
def gate(doc,name,ok):
    doc["gates"].append(dict(name=name,passed=bool(ok)))
    if not ok:raise ValueError("three-band trace gate failed: "+name)

MC_EXECUTION="c5424be21b98cf5e195ea7246ccba46cf746d1f16d9c118042fda1fad433e408"
MC_SOURCE="7547ece2825854a18e59c27294b12e8dbdcb13671c8fb0d8fba6af218d86f7f2"

def inputs(a,doc):
    gate(doc,"the new directed precision and scalar parameters are fixed",a.bits==320)
    m=read(a.manifest)
    gate(doc,"the separate new manifest and scientific source are immutable",
        sha(a.manifest)==a.manifest_sha and m.get("kind")==MANIFEST_KIND
        and m.get("public_repository")==PUBLIC and m.get("parameters")==PARAMETERS
        and m["files"].get(m["input_paths"]["source"])==sha(__file__))
    original=read(a.original_manifest);accepted=read(a.response_summary)
    gate(doc,"the original raw193 row identity and full independent mean are unchanged",
        sha(a.original_manifest)==ORIGINAL_MANIFEST
        and original.get("residual_sha256")==ROW_SOURCE
        and original["row_identity"]["full_trials"]["response"]["sha256"]==TRIAL
        and original["row_identity"]["full_trials"]["response"]["metadata"].get("finite_head_mean_was_not_removed_from_the_solve") is True
        and original["row_identity"].get("total_common_cells")==7721
        and hashlib.sha256(compact(original["row_identity"])).hexdigest()==ROW_IDENTITY)
    gate(doc,"the old positive nonmean budget is identified without calling it the raw full source",
        sha(a.response_summary)==RESPONSE_SUMMARY and accepted.get("complete") is True
        and accepted.get("failure") is None
        and accepted.get("complete_common_rows")==7721
        and accepted.get("actual_completed_common_rows")==7680
        and len(accepted.get("gates",[]))==47 and all(x["passed"] for x in accepted["gates"])
        and len(accepted.get("original_parts",[]))==40
        and accepted.get("original_full_physical_response_trial_sha256")==TRIAL)
    dx=read(a.intrinsic_execution);dr=dx.get("actual_scientific_receipt",{})
    gate(doc,"the independent successful old forty-part receipt binds the same complete rows",
        sha(a.intrinsic_execution)==D_EXECUTION and str(dx.get("run_id"))=="43713242980"
        and dx.get("actual_returncode")==0
        and dr.get("complete") is True and dr.get("failure") is None
        and dr.get("source_sha256")==D_SOURCE and dr.get("actual_returncode")==0
        and len(dr.get("gates",[]))==12 and all(x["passed"] for x in dr["gates"])
        and dr.get("complete_original_rows_verified")==7721
        and dr.get("original_row_identity_sha256")==ROW_IDENTITY
        and dr.get("original_rows_canonical_payload_sha256")==ROWS_PAYLOAD)
    old=read(a.collar_conclusion);proc=read(a.collar_process)
    gate(doc,"the old successful 91-case execution and its qualified conclusion remain exact",
        sha(a.collar_conclusion)==COLLAR and sha(a.collar_process)==COLLAR_PROCESS
        and str(proc.get("run_id"))=="43714674603" and str(proc.get("run_attempt"))=="1"
        and proc.get("complete") is True and proc.get("actual_scientific_complete") is True
        and proc.get("children") and all(x.get("actual_returncode")==0 for x in proc["children"])
        and proc.get("actual_source_sha256")==COLLAR_SOURCE
        and old.get("source_sha256")==COLLAR_SOURCE and old.get("complete") is True
        and old.get("failure") is None and old.get("actual_evaluated_cases")==91
        and len(old.get("complete_grid",[]))==91
        and sum(x.get("passed") is True for x in old["complete_grid"])==15
        and len(old.get("gates",[]))==12 and all(x["passed"] for x in old["gates"])
        and old.get("derived_continuous_centre_definition_sha256")==CENTRE
        and old.get("derived_continuous_response_definition_sha256")==DIRECTION)
    best=old["best_complete_case_per_radius"]
    gate(doc,"only the five retained complete cases share the stated true narrow collar",
        set(best)==set(PARAMETERS["retained_radii"])
        and old["parameters"]["delta_half_width"]==PARAMETERS["delta_half_width"]
        and old["parameters"]["angular_order"]==8193
        and all(case.get("passed") is True
            and case.get("ell")==PARAMETERS["retained_ell"]
            and case.get("exact_interval")==PARAMETERS["retained_interval"]
            and case.get("raw_C0_pair_radius")==radius
            and all(case["gates"].values())
            for radius,case in best.items()))
    execution=read(a.corrected_mean_execution)
    corrected=execution.get("actual_scientific_receipt",{})
    gate(doc,"the successful complete raw mean correction is only consumed",
        sha(a.corrected_mean_execution)==MC_EXECUTION
        and str(execution.get("run_id"))=="43717700427"
        and execution.get("actual_returncode")==0
        and corrected.get("source_sha256")==MC_SOURCE
        and corrected.get("complete") is True and corrected.get("failure") is None
        and len(corrected.get("gates",[]))==12
        and all(x.get("passed") is True for x in corrected["gates"])
        and corrected.get("corrected_cases_evaluated")==5
        and corrected.get("corrected_cases_passed")==5
        and corrected.get("complete_corrected_source_budgets_proved") is True
        and corrected.get("independent_raw_mean_and_continuity_repair_both_paid") is True
        and corrected.get("original_rows_canonical_payload_sha256")==ROWS_PAYLOAD
        and set(corrected.get("corrected_retained_cases",{}))==set(PARAMETERS["retained_radii"])
        and all(v.get("passed") is True
            and v.get("ell")==PARAMETERS["retained_ell"]
            and v.get("exact_interval")==PARAMETERS["retained_interval"]
            and v.get("original_complete_case_sha256")==hashlib.sha256(compact(best[r])).hexdigest()
            and v["high_trace_conclusion"].get("selected_reference_difference_bound_2_power_377903") is True
            for r,v in corrected["corrected_retained_cases"].items()))
    return m,original,accepted,old,corrected

def original_rows(a,doc,original,accepted):
    expected={tuple(x["indices"]):x["sha256"] for x in accepted["original_parts"]}
    observed={};rows=[]
    for path in a.parts:
        part=read_part(path);pair=tuple(part.get("selected_indices",[]))
        if pair not in expected or pair in observed or sha(path)!=expected[pair]:
            raise ValueError("an original natural part is missing, repeated or changed")
        if (part.get("kind")!=original["residual_kind"]
            or part.get("identity")!=original["row_identity"]
            or part.get("source_sha256")!=ROW_SOURCE
            or part.get("selected_cells_complete") is not True or part.get("failure") is not None
            or [x["common_row"] for x in part["rows"]]!=list(range(*pair))):
            raise ValueError("the original complete raw row contract changed")
        rows.extend(part["rows"]);observed[pair]=dict(indices=list(pair),rows=len(part["rows"]),sha256=sha(path))
    rows.sort(key=lambda x:x["common_row"])
    gate(doc,"all original forty natural parts and every raw row are unchanged",
        set(observed)==set(expected) and len(rows)==7721
        and [x["common_row"] for x in rows]==list(range(7721)))
    edge=Fraction(0);digest=hashlib.sha256()
    for row in rows:
        left,right=map(Fraction,row["interval"])
        if left!=edge or not left<right:raise ValueError("the true old radial cover is not contiguous")
        edge=right
        value=ball(row["response_mean_residual"])
        if not value.is_finite():raise ValueError("the complete raw mean range is not finite")
        if "uncorrected_response_nonmean" not in row or "intrinsic_whole_third_jets" not in row:
            raise ValueError("a raw row is being replaced by its mean-completed successor")
        digest.update(compact(row))
    gate(doc,"the full raw signed mean fields retain the original zero-to-25/8 cover",
        edge==Fraction(25,8))
    gate(doc,"the exact canonical row payload agrees with the already successful independent receipt",
        digest.hexdigest()==ROWS_PAYLOAD)
    doc.update(complete_original_rows_verified=7721,
        original_part_receipts=[observed[k] for k in sorted(observed)],
        original_rows_canonical_payload_sha256=digest.hexdigest(),
        original_row_identity_sha256=ROW_IDENTITY)
    return rows


def exact_interval(value):
    """Original directed endpoints, when present, give the full signed range."""
    if not isinstance(value,dict):raise ValueError("a complete directed old record is required")
    if "lower" in value and "upper" in value:
        x=arb(str(value["lower"])).lower().union(arb(str(value["upper"])).upper())
    elif "ball" in value:x=arb(str(value["ball"]))
    else:raise ValueError("a signed old record is missing")
    if not x.is_finite():raise ValueError("nonfinite original range")
    return x

def window_nonmean(rows,left,right,label,audit):
    raw2=arb(0);weighted2=arb(0);raw_h12=arb(0);weighted_h12=arb(0)
    sup=arb(0);weighted_sup=arb(0);pmax=arb(0)
    edge=left;count=0
    for row in rows:
        l,r=map(Fraction,row["interval"]);lo=max(left,l);hi=min(right,r)
        if not lo<hi:continue
        if lo!=edge:raise ValueError("the genuine nonmean window has a gap")
        edge=hi;count+=1
        b=row["uncorrected_response_nonmean"]
        su=nonnegative(b["L2_sup"]);whole=nonnegative(b["L2_L2_radial"])
        hsu=nonnegative(b["H1_sup"]);hwhole=nonnegative(b["H1_L2_radial"])
        length=q(hi-lo)
        # A subinterval is bounded separately by uniform*length and by
        # the original complete-cell integral.  Never scale that integral
        # by the intersection fraction.
        local2=up(min(up(length*su*su),up(whole*whole)))
        localh12=up(min(up(length*hsu*hsu),up(hwhole*hwhole)))
        K=exact_interval(row["intrinsic_whole_third_jets"]["K"])
        if not K.lower()>0:raise ValueError("the full original positive K gap is missing")
        klo=K.lower();khi=K.upper()
        p2=up(max(up(khi.sqrt()),up(1/klo.sqrt())))
        raw2=up(raw2+local2);weighted2=up(weighted2+p2*local2)
        raw_h12=up(raw_h12+localh12);weighted_h12=up(weighted_h12+p2*localh12)
        sup=max(sup,su).upper();weighted_sup=max(weighted_sup,up(p2.sqrt()*su)).upper()
        pmax=max(pmax,p2.sqrt()).upper()
        audit.write(compact(dict(domain=label,common_row=row["common_row"],
            original_interval=row["interval"],intersection=[str(lo),str(hi)],
            exact_intersection_length=str(hi-lo),
            original_nonmean_L2_sup=b["L2_sup"],original_nonmean_whole_L2=b["L2_L2_radial"],
            original_nonmean_H1_sup=b["H1_sup"],original_nonmean_whole_H1=b["H1_L2_radial"],
            original_K=row["intrinsic_whole_third_jets"]["K"],
            new_restricted_square=rec(local2),new_P_squared_upper=rec(p2),
            new_scaled_square=rec(p2*local2),
            new_scaled_H1_square=rec(p2*localh12))))
    if edge!=right or count==0:raise ValueError("the complete new window is not covered")
    raw=raw2.sqrt().upper();scaled=weighted2.sqrt().upper()
    h1=raw_h12.sqrt().upper();ph1=weighted_h12.sqrt().upper()
    return dict(exact_interval=[str(left),str(right)],
        exact_radial_measure=str(right-left),original_closed_rows_consumed=count,
        raw_nonmean_L2=rec(raw),P_scaled_raw_nonmean_L2=rec(scaled),
        raw_nonmean_H1=rec(h1),P_scaled_raw_nonmean_H1=rec(ph1),
        raw_nonmean_angular_L2_upper=rec(min(up(640*raw),h1)),
        P_scaled_raw_nonmean_angular_L2_upper=rec(min(up(640*scaled),ph1)),
        complete_raw_nonmean_sup=rec(sup),complete_P_scaled_nonmean_sup=rec(weighted_sup),
        P_upper_on_old_intersecting_rows=rec(pmax),
        complete_scaled_square_integral=rec(weighted2),
        complete_scaled_H1_square_integral=rec(weighted_h12),
        true_radial_intersections=True,complete_cell_L2_not_rescaled_by_fraction=True,
        complete_nonmean_norm_used_before_high_projection=True,
        independent_raw_mean_recomputed=False,alpha_applied=False,
        original_nonmean_degree_upper=160)

def source_restriction(window,case,response):
    c=case["coefficients"];src=case["source_species"]
    p=nonnegative(c["P_upper"])
    length=q(Fraction(window["exact_interval"][1])-Fraction(window["exact_interval"][0]))
    repair=nonnegative(response["complete_repair_source_sup"]["complete_repair"])
    offset=nonnegative(src["response_offset_sup"])
    # MC monotonicity covers Delta A*q_raw, using the old enlarged H0.
    # Original independent raw mean is killed only by this high projection.
    fee=up(p*length.sqrt()*(repair+offset))
    local=up(nonnegative(window["P_scaled_raw_nonmean_L2"])+fee)
    local_phi=up(nonnegative(window["P_scaled_raw_nonmean_angular_L2_upper"])+640*fee)
    old=nonnegative(src["S0"])
    S=up(min(local,old))
    Sphi=up(min(local_phi,up(640*S)))
    d=q(PARAMETERS["delta_half_width"])
    T2=nonnegative(src["T2"]);T3=nonnegative(src["T3"])
    F96=up(d*S+d*d*T2+d*d*d*T3)
    F96phi=up(d*Sphi+896*d*d*T2+1152*d*d*d*T3)
    return dict(exact_interval=window["exact_interval"],
        old_complete_repair_sup=rec(repair),canonical_continuity_offset_sup=rec(offset),
        complete_scaled_repair_and_offset_fee=rec(fee),
        new_local_high_response_upper=rec(local),
        old_complete_positive_budget_upper=src["S0"],
        complete_S96_upper=rec(S),complete_S96_angular_upper=rec(Sphi),
        old_T2_reused=src["T2"],old_T3_reused=src["T3"],
        complete_known_F96_upper=rec(F96),complete_known_F96_angular_upper=rec(F96phi),
        complete_known_F288_exact_zero=True,complete_known_F288_angle_exact_zero=True,
        independent_mean_paid_by_corrected_execution=True,
        independent_raw_mean_high_projection_exactly_zero=True,
        original_base32_residual_degree_96=True,selected_reference_residual_degree_288=True,
        unknown_actual_H96_residual_still_required=True,
        unknown_actual_H288_residual_still_required=True)

def trace_coefficients(case,source):
    c=case["coefficients"];ell=q(case["ell"]);p=nonnegative(c["P_upper"])
    amin=ball(c["principal_speed_lower"]).lower()
    if not amin>0:raise ValueError("genuine actual principal speed is not positive")
    drift=nonnegative(c["drift_upper"]);L=nonnegative(c["speed_log_derivative"])
    b=nonnegative(c["b"]);g=nonnegative(c["g"]);alpha=nonnegative(c["alpha"])
    M0=nonnegative(c["M0"]);M1=nonnegative(c["M1"]);M2=nonnegative(c["M2"])
    eta=nonnegative(c["eta"]);M=up(M0+eta)
    cp=up(2/amin);cr=up(1+2*drift/amin);D1=up(2*b*M*M)
    A0=up(alpha+3*b*M*M+(b*M/2+g)*M1)
    Astar=up(alpha+3*b*M0*M0+(b*M0/2+g)*M1)
    Ad=up(b*eta*(3*M0+eta+M1/4))
    dd=up(b*(2*M0+eta)*eta/2)
    A1=up(alpha+5*b*M*M);B10=up(8*b*M*M1+(b*M/2+g)*M2)
    k96=up((1+q(Fraction(1,388**2))).sqrt())
    k288=up((1+q(Fraction(1,1156**2))).sqrt())
    la96=up(arb(1+384**2).sqrt());la288=up(arb(1+1152**2).sqrt())
    v96=up(p*(k96*cp*cr).sqrt());v288=up(p*(k288*cp*cr).sqrt())
    middle=up(la288.sqrt()*v96)
    e96L=up(A0+384*drift)
    e96H=up(A0+384*drift+D1+L+1/ell)
    farL=up(Ad+384*dd)
    farH=up(Astar+Ad+((1152*drift)**2+(1152*drift+D1+L+1/ell)**2).sqrt())
    known=up(middle*nonnegative(source["complete_known_F96_upper"]))
    low_radius=q(Fraction(63,320))*q(PARAMETERS["delta_half_width"])
    return dict(raw_C0_pair_radius=case["raw_C0_pair_radius"],
        ell=case["ell"],exact_interval=case["exact_interval"],
        actual_mean_and_rank_one_retained=True,
        all_body_variables_are_P_scaled=True,raw_body_to_scaled_upper=rec(p),
        complete_A0=rec(A0),complete_Astar=rec(Astar),complete_A1=rec(A1),
        complete_B10=rec(B10),complete_D1=rec(D1),
        complete_A_difference=rec(Ad),complete_d_difference=rec(dd),
        cp=rec(cp),cr=rec(cr),actual_speed_lower=rec(amin),
        unchanged_true_solution_speed_log_bound=c["speed_log_derivative"],
        kappa96=rec(k96),kappa288=rec(k288),
        E96_positive_linear_body_coefficients=dict(ZL=rec(e96L),ZH=rec(e96H)),
        E288_positive_linear_body_coefficients=dict(ZL=rec(farL),ZH=rec(farH)),
        E288_exact_three_band_coefficients=dict(
            ZH=rec(Astar),Zfull=rec(Ad),ZL=rec(384*dd),
            Zmiddle=rec(1152*drift),Zfar=rec(1152*drift+D1+L+1/ell)),
        half_trace_factors=dict(V96_per_E96=rec(v96),V288_per_E288=rec(v288)),
        finite_raw_cut_L2_to_H1=rec(la96),middle_H1_per_E96=rec(middle),
        far_high_interpolation=dict(power_numerator=16384,power_denominator=16385,
            complete_prefactor="2^24",same_state_H8193_bound="2^377903"),
        known_middle_source_additive_upper=rec(known),
        uniform_low_W_sufficient_H1_radius=rec(low_radius),
        residual_budget_after_known_middle_term=rec(low_radius-known),
        this_signed_budget_is_not_an_actual_state_gate=True,
        actual_unknown_cut_bound_supplied=False,
        actual_two_sided_unknown_body_bounds_supplied=False,
        actual_unknown_residual_or_true_solution_supplied=False,
        actual_low_curvature_entry_proved=False,
        no_unknown_body_value_replaced_by_C0_radius=True,
        direct_derivative_alternative=dict(
            complete_A1=rec(A1),complete_B10=rec(B10),
            angular_source_is_independent=True,
            use_exact_LT22_with_NJ_384_or_1152=True))

def run(a,doc):
    m,original,accepted,old,corrected=inputs(a,doc)
    rows=original_rows(a,doc,original,accepted)
    p=Path(a.temporary_rows);p.parent.mkdir(parents=True,exist_ok=True)
    if p.exists():raise FileExistsError("preserve every actual new restriction audit")
    windows={}
    with p.open("wb") as audit:
        for label,pair in (("whole_available_positive_collar",PARAMETERS["available_collar"]),
                           ("retained_complete_case_collar",PARAMETERS["retained_interval"])):
            windows[label]=window_nonmean(rows,*map(Fraction,pair),label,audit)
    gate(doc,"both new nonmean restrictions use complete whole-cell norms and true intersections",
        windows["whole_available_positive_collar"]["original_closed_rows_consumed"]==140
        and windows["retained_complete_case_collar"]["original_closed_rows_consumed"]==2
        and all(v["exact_radial_measure"]==str(Fraction(v["exact_interval"][1])-Fraction(v["exact_interval"][0]))
                for v in windows.values()))
    cases={}
    for radius in PARAMETERS["retained_radii"]:
        case=old["best_complete_case_per_radius"][radius]
        src=source_restriction(windows["retained_complete_case_collar"],case,accepted)
        cases[radius]=dict(source_restriction=src,
            complete_trace_coefficients=trace_coefficients(case,src),
            original_complete_case_sha256=hashlib.sha256(compact(case)).hexdigest(),
            corrected_high_window_authorization=corrected["corrected_retained_cases"][radius]["high_trace_conclusion"])
    gate(doc,"all five explicit trace tables retain the corrected high case and all unknown inputs",
        len(cases)==5 and all(v["source_restriction"]["complete_known_F288_exact_zero"]
            and v["complete_trace_coefficients"]["actual_low_curvature_entry_proved"] is False
            and v["complete_trace_coefficients"]["no_unknown_body_value_replaced_by_C0_radius"]
            for v in cases.values()))
    doc.update(complete=True,proved=True,actual_returncode=0,
        complete_new_nonmean_windows=windows,
        complete_retained_three_band_cases=cases,
        cases_evaluated=5,
        corrected_raw_mean_execution_sha256=MC_EXECUTION,
        corrected_raw_mean_windows_copied_without_recomputation=corrected["complete_raw_mean_windows"],
        complete_source_and_trace_coefficient_tables_proved=True,
        known_source_support_and_raw_mean_independence_preserved=True,
        whole_original_rows_verified=7721,original_parts_recomputed=0,
        old_numerical_enclosures_recomputed=0,
        old_target_Fourier_cubic_mean_residual_integral_or_Green_calls=0,
        original_mean_flow_resolved_again=False,
        successful_raw_mean_restrictions_recomputed=False,
        all_original_natural_part_bytes_modified=0,
        original_91_cases_or_five_corrected_verdicts_changed=False,
        complete_finite193_transferred_inverse_proved=False,
        complete_infinite_BVP_inverse_proved=False,true_parameter_Schur_proved=False,
        actual_core_solution_proved=False,actual_low_curvature_entry_proved=False,
        unknown_same_state_right_cap_body_still_required=True,
        genuine_cut_matching_not_removed=True,
        new_recomputable_outputs_persisted=False,
        temporary_nonmean_row_audit=dict(bytes=p.stat().st_size,sha256=sha(p),persisted=False))

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("manifest","original-manifest","response-summary","intrinsic-execution",
                 "collar-conclusion","collar-process","corrected-mean-execution","temporary-rows","out"):
        p.add_argument("--"+name,type=Path,required=True)
    p.add_argument("--manifest-sha",required=True)
    p.add_argument("--parts",type=Path,nargs="+",required=True)
    p.add_argument("--bits",type=int,default=320)
    a=p.parse_args();ctx.prec=a.bits;started=time.monotonic()
    if a.out.exists():raise FileExistsError("preserve every actual three-band restriction outcome")
    doc=dict(kind=KIND,complete=False,proved=False,failure=None,actual_returncode=None,gates=[],
        source_sha256=sha(__file__),input_manifest_sha256=a.manifest_sha,parameters=PARAMETERS,
        derived_continuous_centre_definition_sha256=CENTRE,
        derived_continuous_response_definition_sha256=DIRECTION)
    try:run(a,doc)
    except Exception as e:
        doc.update(complete=False,proved=False,actual_returncode=1,
            failure=dict(type=type(e).__name__,message=str(e)))
        traceback.print_exc()
    doc["seconds"]=time.monotonic()-started
    save(a.out,doc)
    print(json.dumps(dict(complete=doc["complete"],failure=doc["failure"],
        gates_passed=sum(x["passed"] for x in doc["gates"]),gates_total=len(doc["gates"]),
        cases_evaluated=doc.get("cases_evaluated"),
        actual_low_curvature_entry_proved=False)),flush=True)
    return 0 if doc["complete"] else 1

if __name__=="__main__":raise SystemExit(main())
