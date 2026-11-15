#!/usr/bin/env python3
"""Read the original raw response mean; correct only retained collar cases.

No target, Fourier, polynomial residual, scalar mean flow or old Green
routine is imported or evaluated.  Old successful receipts are immutable.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,time,traceback
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx

PUBLIC="Rogerhu12/math-research-public"
KIND="actual_raw_response_mean_and_corrected_collar_source_v1"
MANIFEST_KIND="immutable_raw_response_mean_collar_fee_inputs_v1"
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
    raw_mean_field="response_mean_residual",new_source_angular_degree=0,
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
    if not ok:raise ValueError("raw mean source gate failed: "+name)

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
    return m,original,accepted,old

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

def window_mean(rows,left,right,label,audit):
    total=arb(0);unscaled=arb(0);sup=arb(0);psup=arb(0)
    signed_lo=None;signed_hi=None;edge=left;count=0
    for row in rows:
        l,r=map(Fraction,row["interval"]);lo=max(left,l);hi=min(right,r)
        if not lo<hi:continue
        if lo!=edge:raise ValueError("a genuine raw mean interval is missing")
        edge=hi;count+=1
        mean=ball(row["response_mean_residual"]);R=abs(mean).upper()
        K=ball(row["intrinsic_whole_third_jets"]["K"])
        if not K.lower()>0:raise ValueError("the complete old positive K gap is absent")
        kp=K.upper();p2=kp.sqrt().upper();length=q(hi-lo)
        # P e2=K^(1/4)e2, so the squared norm uses sqrt(K).
        total=up(total+length*p2*R*R);unscaled=up(unscaled+length*R*R)
        sup=max(sup,R).upper();psup=max(psup,up(p2.sqrt()*R)).upper()
        signed_lo=mean.lower() if signed_lo is None else min(signed_lo,mean.lower()).lower()
        signed_hi=mean.upper() if signed_hi is None else max(signed_hi,mean.upper()).upper()
        audit.write(compact(dict(domain=label,common_row=row["common_row"],
            original_interval=row["interval"],intersection=[str(lo),str(hi)],
            exact_intersection_length=str(hi-lo),original_raw_mean=rec(mean),
            original_K=rec(K),new_scaled_mean_square_integral=rec(length*p2*R*R))))
    if edge!=right or count==0:raise ValueError("the original rows do not cover the whole new domain")
    return dict(exact_interval=[str(left),str(right)],exact_radial_measure=str(right-left),
        original_closed_rows_consumed=count,raw_mean_signed_lower=rec(signed_lo),
        raw_mean_signed_upper=rec(signed_hi),raw_mean_sup=rec(sup),
        raw_mean_L2=rec(unscaled.sqrt().upper()),P_scaled_raw_mean_sup=rec(psup),
        P_scaled_raw_mean_L2=rec(total.sqrt().upper()),
        complete_scaled_square_integral=rec(total),
        exact_P_squared_second_component="sqrt(K)",
        raw_mean_normalization_factor="1",alpha_applied=False,
        angular_positive_derivatives_exactly_zero=True)

def correct_case(case,mean_fee):
    c=case["coefficients"];s=case["source_species"];e=q(case["ell"])
    fee=up(q(PARAMETERS["delta_half_width"])*mean_fee)
    AN=up(nonnegative(c["AN"])+fee);CE=nonnegative(c["CE_sharp"])
    p=nonnegative(c["P_upper"]);c2=nonnegative(c["c2_sharp"]);c3=nonnegative(c["c3_sharp"])
    nonlinear=up(2*CE*CE*c2*AN+4*CE*CE*CE*c3*AN*AN)
    readout=up(2*p*CE*e.sqrt()*AN)
    amin=ball(c["principal_speed_lower"]).lower()
    if not amin>0:raise ValueError("the retained genuine principal-speed lower bound changed")
    cp=up(2/amin);drift=nonnegative(c["drift_upper"])
    cr=up(1+2*drift/amin);M=up(nonnegative(c["M0"])+nonnegative(c["eta"]))
    A1=up(nonnegative(c["alpha"])+5*nonnegative(c["b"])*M*M)
    L=nonnegative(c["speed_log_derivative"])
    gain=up(p*(cp/e.sqrt()+e.sqrt()*cr*(1+cp*(A1+L+2/e))))
    gates=dict(positive_actual_speed=case["gates"]["positive_actual_speed"],
        low_start=case["gates"]["low_start"],complete_linear=case["gates"]["complete_linear"],
        complete_nonlinear=bool(nonlinear<=q("1/8")),
        factorial_readout=bool(readout<=arb(2)**1024))
    passed=all(gates.values())
    old_case_sha=hashlib.sha256(compact(case)).hexdigest()
    return dict(raw_C0_pair_radius=case["raw_C0_pair_radius"],ell=case["ell"],
        exact_interval=case["exact_interval"],original_complete_case_sha256=old_case_sha,
        new_P_scaled_raw_mean_L2=rec(mean_fee),new_mean_source_fee=rec(fee),
        corrected_source_value=rec(up(nonnegative(s["ordinary_value"])+fee)),
        corrected_source_angle=s["ordinary_angle"],
        corrected_source_factorial=rec(up(nonnegative(s["finite_factorial"])+fee)),
        previous_S0_only_b0_bound=s["S0"],corrected_complete_s0_bound=rec(up(nonnegative(s["S0"])+mean_fee)),
        corrected_AN=rec(AN),unchanged_start=case["scalar_gates"]["low_start"],
        unchanged_linear=case["scalar_gates"]["complete_linear"],
        corrected_nonlinear=rec(nonlinear),corrected_factorial_prefactor=rec(readout),
        mean_value_to_H1_gain=rec(gain),
        corrected_comparison_H1_cut_upper=rec(up(nonnegative(case["comparison_H1_cut_upper"])+gain*fee)),
        corrected_base_centre_H1_cut_upper=rec(up(nonnegative(case["base_centre_H1_cut_upper"])+gain*fee)),
        numerical_gates=gates,passed=passed,
        high_trace_conclusion=dict(order=8193,
            selected_reference_difference_bound_2_power_377903=passed,
            base_centre_difference_bound_2_power_377904=passed,
            base_centre_difference_bound_2_power_393000=passed,
            hypothesis="one real continuous two-sided H1 solution of the full PDE in the stated raw C0 pair ball"),
        old_false_low_entry_verdict_preserved=True,
        no_actual_unknown_low_trace_or_core_existence_claim=True)

def run(a,doc):
    m,original,accepted,old=inputs(a,doc)
    rows=original_rows(a,doc,original,accepted)
    windows={}
    p=Path(a.temporary_rows);p.parent.mkdir(parents=True,exist_ok=True)
    if p.exists():raise FileExistsError("preserve every earlier actual temporary audit")
    with p.open("wb") as audit:
        for label,pair in (("whole_available_positive_collar",PARAMETERS["available_collar"]),
                           ("retained_complete_case_collar",PARAMETERS["retained_interval"])):
            windows[label]=window_mean(rows,*map(Fraction,pair),label,audit)
    gate(doc,"both new mean restrictions use exact intersections and full closed-row ranges",
        all(x["exact_radial_measure"]==str(Fraction(x["exact_interval"][1])-Fraction(x["exact_interval"][0]))
            for x in windows.values()))
    fee=nonnegative(windows["retained_complete_case_collar"]["P_scaled_raw_mean_L2"])
    corrected={r:correct_case(old["best_complete_case_per_radius"][r],fee)
               for r in PARAMETERS["retained_radii"]}
    gate(doc,"all five retained complete cases receive the mean fee with their original thresholds",
        set(corrected)==set(PARAMETERS["retained_radii"])
        and all(x["corrected_source_angle"]==old["best_complete_case_per_radius"][r]["source_species"]["ordinary_angle"]
            for r,x in corrected.items()))
    passed=sum(x["passed"] for x in corrected.values())
    doc.update(complete=True,proved=True,actual_returncode=0,
        complete_corrected_source_budgets_proved=True,
        complete_raw_mean_windows=windows,corrected_retained_cases=corrected,
        corrected_cases_evaluated=5,corrected_cases_passed=passed,
        corrected_conditional_high_trace_domain_exists=bool(passed),
        old_cases_evaluated=91,old_recorded_cases_passed=15,
        old_91_records_changed=False,other_old_ten_passing_cases_reauthorized=False,
        raw_source_and_completed_mean_source_not_identified=True,
        independent_raw_mean_and_continuity_repair_both_paid=True,
        original_mean_flow_resolved_again=False,
        old_numerical_enclosures_recomputed=0,
        old_target_Fourier_cubic_mean_residual_integral_or_Green_calls=0,
        all_original_natural_part_bytes_modified=0,
        complete_finite193_transferred_inverse_proved=False,
        complete_infinite_BVP_inverse_proved=False,true_parameter_Schur_proved=False,
        no_core_existence_or_low_gamma_selfmap_claim=True,
        new_recomputable_outputs_persisted=False,
        temporary_mean_row_audit=dict(bytes=p.stat().st_size,sha256=sha(p),persisted=False))

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("manifest","original-manifest","response-summary","intrinsic-execution",
                 "collar-conclusion","collar-process","temporary-rows","out"):
        p.add_argument("--"+name,type=Path,required=True)
    p.add_argument("--manifest-sha",required=True)
    p.add_argument("--parts",type=Path,nargs="+",required=True)
    p.add_argument("--bits",type=int,default=320)
    a=p.parse_args();ctx.prec=a.bits;started=time.monotonic()
    if a.out.exists():raise FileExistsError("preserve every actual source correction result")
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
        corrected_cases_passed=doc.get("corrected_cases_passed"),
        corrected_conditional_high_trace_domain_exists=doc.get("corrected_conditional_high_trace_domain_exists"))),flush=True)
    return 0 if doc["complete"] else 1

if __name__=="__main__":raise SystemExit(main())
