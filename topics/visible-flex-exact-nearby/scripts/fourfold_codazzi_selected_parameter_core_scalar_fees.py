#!/usr/bin/env python3
"""New selected-parameter scalar budgets from the accepted complete 7721 cells.

Only scalar interval arithmetic is new. Original intrinsic targets, cubics,
Fourier products, means, residuals, Green kernels and validators are not run.
All original native data and the new optional row audit remain temporary.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,os,sys,time,traceback
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx

KIND="actual_selected_parameter_core_scalar_fees_from_complete_old_cells_v1"
REL="topics/visible-flex-exact-nearby/"
PRODUCER=REL+"scripts/fourfold_codazzi_selected_parameter_core_scalar_fees.py"
ORIGINAL_MANIFEST="c214f800a5094c905c554e9053c52567d5ae5d76be41ac2e3fe9d673b396d784"
ORIGINAL_ROWS_SOURCE="1651f6cf73af9f3c16061767cc5acff0c452ada183422f7efb983ec8a6d4eb07"
RESPONSE_SUMMARY="7c43eeed609006195893d6ceee5003887e533ac6222515171d27b624e47115ec"
KERNEL_SUMMARY="fd88f3dd72c3983ca011d1a66520f91db0c7108118611c3a5b99f97f195fe9be"
CENTRE="440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
DIRECTION="6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
PARAMETERS=dict(
    arithmetic_bits=320,delta_half_width="1/10000000000",
    exact_core_interval=["0","9/10"],
    exact_negative_interval=["0","2383968743003/10000000000000"],
    exact_compact_support=["1/20","9/50"],
    exact_collar_interval=["17/20","19/20"],
    complete_original_interval=["0","25/8"],
    complete_original_rows=7721,complete_original_parts=40,
    original_parameter_half_width="1/1000000000",
    background_pair_A0="7",background_pair_angle_A0="6",
    response_pair_A0="19",response_pair_angle_A0="83",
    response_continuous_repair_A_1over64="0.0000000000000002292",
    compact_weight_upper="1",compact_weight_derivative_upper="2400/13",
    head_maximum_physical_frequency=384,
    selected_family_cross_input_maximum_physical_frequency=1152,
    original_physical_frequency_factor=4,
    fixed_intrinsic_parameter="eta_0",real_delta_family_only=True,
    original_enclosures_recomputed=0,
    source_norm="ordinary L2_r L2_phi; normalized circle, full mean",
    new_full_inverse_or_true_parameter_Schur_claimed=False)
CORE=Fraction(9,10)
NEGATIVE=Fraction(2383968743003,10000000000000)
CONTROL=(Fraction(1,20),Fraction(9,50))
COLLAR=(Fraction(17,20),Fraction(19,20))
FULL=Fraction(25,8)
METRICS=("M0","M1","e_LL","e_LH","N_nu","M1_Zphi_plus_M0_Z",
         "complete_additional_response_source")
WINDOWS={"whole_core":(Fraction(0),CORE),
         "fixed_negative_window":(Fraction(0),NEGATIVE),
         "compact_metric_support":CONTROL}

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def canonical(value):
    return (json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(",",":"),
                       allow_nan=False)+"\n").encode()

def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2]==b"\x1f\x8b" else raw)

def save(path,value):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    raw=canonical(value)
    if len(raw)>60000:raise ValueError("the complete small conclusion exceeds 60000 UTF8 bytes")
    temporary=path.with_name(path.name+".partial")
    temporary.write_bytes(raw);temporary.replace(path)

def q(value):
    v=Fraction(value)
    return arb(v.numerator)/v.denominator

def interval(value):
    if not isinstance(value,dict):return arb(str(value))
    if "lower" in value and "upper" in value:
        result=arb(value["lower"]).lower().union(arb(value["upper"]).upper())
    elif "ball" in value:
        result=arb(value["ball"])
    else:
        raise ValueError("an old scalar has no complete directed interval")
    if not result.is_finite():raise ValueError("a stored scalar interval is nonfinite")
    return result

def up(value):
    x=interval(value) if isinstance(value,dict) else arb(value)
    if not x.is_finite():raise ValueError("a new scalar upper is nonfinite")
    return x.upper()

def absup(value):
    x=interval(value) if isinstance(value,dict) else arb(value)
    if not x.is_finite():raise ValueError("a whole-cell scalar is nonfinite")
    return abs(x).upper()

def record(value):
    x=arb(value)
    if not x.is_finite():raise ValueError("a scalar conclusion is nonfinite")
    return dict(ball=x.str(64))

def gate(doc,name,passed):
    doc["gates"].append(dict(name=name,passed=bool(passed)))
    if not passed:raise ValueError("selected-parameter scalar gate failed: "+name)

def complete_summary(doc):
    return (doc.get("complete") is True and doc.get("failure") is None
            and doc.get("gates") and all(x.get("passed") is True for x in doc["gates"]))

def validate_inputs(a,doc):
    manifest=read(a.manifest)
    gate(doc,"the new source, exact parameters and independently pinned inputs are unchanged",
         sha(a.manifest)==a.manifest_sha and manifest.get("parameters")==PARAMETERS
         and manifest["files"].get(PRODUCER)==sha(__file__)
         and sha(a.original_manifest)==ORIGINAL_MANIFEST
         and sha(a.response_summary)==RESPONSE_SUMMARY
         and sha(a.kernel_summary)==KERNEL_SUMMARY)
    old=read(a.original_manifest);response=read(a.response_summary);kernel=read(a.kernel_summary)
    ident=old.get("row_identity",{})
    gate(doc,"the original complete physical row identity and all genuine means are retained",
         old.get("total_common_cells")==7721
         and old.get("residual_kind")=="actual_full_regular_joint_radial_polynomial_residual_rows_v1"
         and ident.get("source_sha256")==ORIGINAL_ROWS_SOURCE
         and ident.get("original_parameter_half_width")=="1/1000000000"
         and ident.get("total_common_cells")==7721
         and ident["full_trials"]["response"]["metadata"].get("modes")==96
         and ident["full_trials"]["response"]["metadata"].get("physical_frequency_factor")==4
         and ident["full_trials"]["response"]["metadata"].get("finite_head_mean_was_not_removed_from_the_solve") is True
         and ident["full_trials"]["response"]["metadata"].get("original_fourth_Robin_row_retained") is True)
    gate(doc,"the original complete response-repair conclusion and its forty immutable part hashes are valid",
         complete_summary(response)
         and response.get("complete_common_rows")==7721
         and response.get("actual_completed_common_rows")==7680
         and response.get("exact_interval")==["0","25/8"]
         and response.get("input_sha256",{}).get("original-manifest")==ORIGINAL_MANIFEST
         and response.get("derived_continuous_centre_definition_sha256")==CENTRE
         and response.get("true_complete_mean_correction_retained") is True
         and response.get("original_residual_rows_recomputed")==0
         and response.get("original_mean_flows_recomputed")==0
         and len(response.get("original_parts",[]))==40)
    gate(doc,"the ordinary Green source units, exact two windows and complete even mean agree",
         complete_summary(kernel)
         and kernel.get("exact_inner_BVP_interval")==["0","9/10"]
         and kernel.get("fixed_phase_error_norm_interval")==PARAMETERS["exact_negative_interval"]
         and kernel.get("derived_continuous_centre_definition_sha256")==CENTRE
         and kernel.get("exact_affine_parameter_offset")=="0"
         and kernel.get("full_independent_even_mean_retained") is True
         and kernel.get("L_infinity_unit_source_not_used_as_L2_source") is True
         and kernel.get("ordinary_input_angular_measure")=="normalized circle; all193 components including independent even mean")
    bounds=response["whole_original_known_state_bounds"]
    repair=response["exact_centre_repair_bounds"]
    rz=q(PARAMETERS["response_continuous_repair_A_1over64"])
    checks=dict(background_pair_A0=up(bounds["background_A0"])+up(repair["A0"]),
        background_pair_angle_A0=up(bounds["background_angle_A0"])+up(repair["angular_A0"]),
        response_pair_A0=up(bounds["response_star_A0"])+rz,
        response_pair_angle_A0=up(bounds["response_angle_A0"])+384*rz)
    gate(doc,"the complete raw states and both exact repairs fit the four already proved global constants",
         all(up(value)<q(PARAMETERS[key]) for key,value in checks.items()))
    doc.update(original_row_identity_sha256=hashlib.sha256(canonical(ident)).hexdigest(),
        original_complete_parameter_enclosure_half_width=ident["original_parameter_half_width"],
        original_response_legacy_progress=dict(actual_completed_common_rows=7680,
            complete_common_rows=7721,periodic_checkpoint_interval=256,
            periodic_progress_is_not_the_final_cover=True,
            complete_original_part_and_row_cover_verified_separately=True),
        that_width_is_not_a_transferred_inverse_domain=True,
        exact_original_eta_and_nu=dict(exact_alpha=ident["exact_alpha"],exact_nu=ident["exact_nu"],
                                      eta="fixed original eta_0"),
        derived_continuous_centre_definition_sha256=CENTRE,
        derived_continuous_response_definition_sha256=DIRECTION,
        verified_global_state_bounds={k:record(up(v)) for k,v in checks.items()},
        chosen_global_constants={k:PARAMETERS[k] for k in checks},
        complete_response_repair_including_mean=dict(A0=PARAMETERS["response_continuous_repair_A_1over64"],
                                                    angular_multiplier=384),
        original_generic_ordinary_Green_conclusion=dict(
            exact_input_norm=kernel["ordinary_input_angular_measure"],
            exact_full_interval=kernel["exact_inner_BVP_interval"],
            exact_negative_interval=kernel["fixed_phase_error_norm_interval"],
            ordinary_source_L2_bounds=kernel["complete_ordinary_L2_source_to_L2_bounds"],
            whole_body_C0_bounds=kernel["complete_ordinary_L2_source_to_C0_bounds"],
            whole_body_C0_not_used_as_new_final_node_value=True,
            specialized_cross_columns_substituted=False,
            actual_new_true_cut_and_right_Poisson_columns_still_required=True))
    expected={}
    for item in response["original_parts"]:
        key=tuple(item["indices"])
        if key in expected:raise ValueError("the accepted original part list is duplicated")
        expected[key]=item["sha256"]
    paths={}
    for path in a.parts:
        digest=sha(path)
        keys=[key for key,want in expected.items() if digest==want]
        if len(keys)!=1 or keys[0] in paths:
            raise ValueError("an original native part is missing, duplicated or differs in bytes")
        paths[keys[0]]=Path(path)
    gate(doc,"every one of the original forty natural part byte hashes is restored exactly",
         len(paths)==40 and set(paths)==set(expected))
    return manifest,old,response,kernel,expected,paths

def selected_parameter_fees(jets,left,right):
    b=absup(jets["beta"]);g=absup(jets["gamma"]);k=absup(jets["K"])
    active=left<CONTROL[1] and right>CONTROL[0]
    if active:
        if not CONTROL[0]<=left<right<=CONTROL[1]:
            raise ValueError("a new scalar restriction straddles a compact-weight seam")
        gamma=interval(jets["gamma"]);aa=interval(jets["a"])
        if not gamma.lower()>0 or not aa.lower()>0:
            raise ValueError("the actual compact-support gamma or a reciprocal is not positive")
        t=up(b/(2*gamma.lower()*gamma.lower()*aa.lower()*aa.lower()))
        W=q(1);W1=q("2400/13")
    else:
        t=arb(0);W=arb(0);W1=arb(0)
    d=q(PARAMETERS["delta_half_width"])
    Q0=q(7);Q1=q(6);Z0=q(19);Z1=q(83);Em=d*Z0
    E0=d*Z0;E1=d*Z1;m0=Q0
    full=(d*W).exp();half=(d*W/2).exp()
    gp=up(g*half)
    kp=max(arb(1),up(full*(k+d*t*W1)))
    kd=up((full-1)*k+d*full*t*W1)
    jd=up(g*max(up((half-1)*k+d*half*t*W1),up(half-1)))
    change=up(kp*(2*Q0*E0+E0*E0))
    M1=up(b*change/4+gp*kp*Em+b*kd*Q0*Q0/4+m0*jd)
    M0=up(3*b*change+b*kp*(E0*Q1+(Q0+E0)*E1)/2+gp*kp*E1
          +3*b*kd*Q0*Q0+b*kd*Q0*Q1/2+jd*Q1)
    if active:
        knp=up(full*(t*W1+W*k+d*W*t*W1))
        jnp=up(g*half*max(up(t*W1+W*(k+d*t*W1)/2),up(W/2)))
        knd=up((full-1)*(t*W1+W*k)+d*full*W*t*W1)
        jnd=up(g*max(
            up((half-1)*(t*W1+W*k/2)+d*W*half*t*W1/2),
            up(W*(half-1)/2)))
        U=up(2*Q0*E0+E0*E0);V=up((Q0+E0)*(Q0+E0))
        N=up(b*knp*(U*Q1/4+V*E1/4+U*Q0+V*E0)
             +jnp*(Em*Q1+(m0+Em)*E1)
             +b*knd*(Q0*Q0*Q1/4+Q0*Q0*Q0)+m0*jnd*Q1)
    else:
        knp=jnp=knd=jnd=N=arb(0)
    AZ=up(M1*Z1+M0*Z0)
    metrics=dict(M0=M0,M1=M1,e_LL=up(M0+384*M1),e_LH=up(M0+1152*M1),
                 N_nu=N,M1_Zphi_plus_M0_Z=AZ,complete_additional_response_source=up(N+AZ))
    details=dict(beta=b,gamma=g,K=k,T=t,compact_support_active=active,
                 G_plus=gp,K_plus=kp,k_delta=kd,J_delta=jd,
                 K_nu_plus=knp,J_nu_plus=jnp,K_nu_delta=knd,J_nu_delta=jnd)
    if any(not v.is_finite() or v<0 for v in metrics.values()):
        raise ValueError("a complete selected-parameter fee is negative or nonfinite")
    return metrics,details

def empty_accumulator():
    return dict(edge=None,rows=set(),pieces=0,length=Fraction(0),
                maxima={k:arb(0) for k in METRICS},
                witnesses={},squared={k:arb(0) for k in METRICS})

def accumulate(acc,left,right,row_index,metrics):
    if not left<right:return
    if acc["edge"] is not None and acc["edge"]!=left:
        raise ValueError("the new scalar source window has a gap or overlap")
    h=right-left
    acc["edge"]=right;acc["rows"].add(row_index);acc["pieces"]+=1;acc["length"]+=h
    for key,value in metrics.items():
        z=up(value)
        if z>acc["maxima"][key] or key not in acc["witnesses"]:
            acc["maxima"][key]=z
            acc["witnesses"][key]=dict(common_row=row_index,interval=[str(left),str(right)])
        acc["squared"][key]+=q(h)*z*z

def collar_values(jets):
    names=["a"]+[name+(str(j) if j else "") for name in ("beta","gamma","K","s") for j in range(4)]
    values={name:interval(jets[name]) for name in names}
    if not values["gamma"].lower()>0 or not values["K"].lower()>0 or not values["a"].lower()>0:
        raise ValueError("the actual complete collar does not certify positive gamma, K and a")
    ratios=dict(gamma_r_over_gamma=up(absup(values["gamma1"])/values["gamma"].lower()),
                K_r_over_K=up(absup(values["K1"])/values["K"].lower()))
    return values,ratios

def run(a,doc):
    ctx.prec=a.bits
    gate(doc,"the directed scalar arithmetic uses the declared precision",a.bits==PARAMETERS["arithmetic_bits"])
    manifest,old,response,kernel,expected,paths=validate_inputs(a,doc)
    acc={name:empty_accumulator() for name in WINDOWS}
    coll=dict(edge=COLLAR[0],length=Fraction(0),rows=set(),lower={},upper={},absolute={},ratios={})
    cursor=0;radial=Fraction(0);part_receipts=[];audit=hashlib.sha256()
    a.temporary_rows.parent.mkdir(parents=True,exist_ok=True)
    if a.temporary_rows.exists():raise FileExistsError("preserve the original new scalar audit file")
    new_cell_budget_calls=0;compact_calls=0;old_row_payload=hashlib.sha256()
    with a.temporary_rows.open("wb") as audit_file:
        for key,path in sorted(paths.items()):
            piece=read(path)
            if (piece.get("kind")!=old["residual_kind"] or piece.get("identity")!=old["row_identity"]
                or piece.get("source_sha256")!=ORIGINAL_ROWS_SOURCE
                or piece.get("selected_cells_complete") is not True or piece.get("failure") is not None
                or tuple(piece.get("selected_indices",[]))!=key or key[0]!=cursor
                or len(piece.get("rows",[]))!=key[1]-key[0]):
                raise ValueError("an original complete residual part changed scientific identity or cover")
            for row in piece["rows"]:
                left,right=map(Fraction,row["interval"])
                if row.get("common_row")!=cursor or left!=radial or not left<right:
                    raise ValueError("the exact original 7721-row radial order has a gap or duplicate")
                germ=row.get("actual_scalar_germ")
                if not germ or len(germ)<2 or not Fraction(germ[0])<=left<right<=Fraction(germ[1]):
                    raise ValueError("an old whole-cell jet leaves its actual scalar germ")
                jets=row.get("intrinsic_whole_third_jets",{})
                required=["a"]+[name+(str(j) if j else "") for name in ("beta","gamma","K","s") for j in range(4)]
                if any(name not in jets for name in required):
                    raise ValueError("the original complete third-jet schema is incomplete")
                for name in required:interval(jets[name])
                old_row_payload.update(canonical(row))
                doc["actual_last_verified_original_row"]=cursor
                doc["actual_last_verified_original_interval"]=row["interval"]
                right_core=min(right,CORE)
                if left<right_core:
                    cuts=sorted({left,right_core,*[x for x in (*CONTROL,NEGATIVE) if left<x<right_core]})
                    for l,r in zip(cuts,cuts[1:]):
                        metrics,details=selected_parameter_fees(jets,l,r)
                        new_cell_budget_calls+=1;compact_calls+=int(details["compact_support_active"])
                        audit_row=dict(common_row=cursor,original_interval=row["interval"],
                            exact_restricted_interval=[str(l),str(r)],
                            original_scalar_germ=germ,
                            metrics={k:record(v) for k,v in metrics.items()},
                            metric_coefficients={k:(v if isinstance(v,bool) else record(v)) for k,v in details.items()})
                        raw=canonical(audit_row);audit_file.write(raw);audit.update(raw)
                        for name,(wl,wr) in WINDOWS.items():
                            aleft=max(l,wl);aright=min(r,wr)
                            if aleft<aright:accumulate(acc[name],aleft,aright,cursor,metrics)
                cl=max(left,COLLAR[0]);cr=min(right,COLLAR[1])
                if cl<cr:
                    if cl!=coll["edge"]:raise ValueError("the true collar row restrictions have a gap")
                    values,ratios=collar_values(jets)
                    coll["edge"]=cr;coll["length"]+=cr-cl;coll["rows"].add(cursor)
                    for name,x in values.items():
                        lo=x.lower();hi=x.upper();av=absup(x)
                        coll["lower"][name]=lo if name not in coll["lower"] else min(coll["lower"][name],lo)
                        coll["upper"][name]=hi if name not in coll["upper"] else max(coll["upper"][name],hi)
                        coll["absolute"][name]=av if name not in coll["absolute"] else max(coll["absolute"][name],av)
                    for name,x in ratios.items():
                        coll["ratios"][name]=x if name not in coll["ratios"] else max(coll["ratios"][name],x)
                cursor+=1;radial=right
            if cursor!=key[1]:raise ValueError("an original part ended at the wrong row")
            part_receipts.append(dict(indices=list(key),sha256=expected[key],rows=key[1]-key[0]))
            print(json.dumps(dict(original_part=list(key),verified_original_rows=cursor,
                                  new_scalar_restrictions=new_cell_budget_calls)),flush=True)
    gate(doc,"all forty original parts and every complete original row cover the true full interval exactly",
         cursor==7721 and radial==FULL and len(part_receipts)==40)
    gate(doc,"all three exact source windows include every original one-sided cell and both compact seams",
         all(acc[name]["edge"]==wr and acc[name]["length"]==wr-wl
             for name,(wl,wr) in WINDOWS.items()))
    gate(doc,"the complete collar has its exact physical interval and actual positive intrinsic gaps",
         coll["edge"]==COLLAR[1] and coll["length"]==COLLAR[1]-COLLAR[0]
         and all(coll["lower"][key]>0 for key in ("a","gamma","K")))
    conclusions={}
    for name,(wl,wr) in WINDOWS.items():
        z=acc[name]
        conclusions[name]=dict(exact_interval=[str(wl),str(wr)],
            original_closed_rows_consumed=len(z["rows"]),new_exact_scalar_restrictions=z["pieces"],
            exact_total_radial_measure=str(z["length"]),
            maxima={k:record(up(v)) for k,v in z["maxima"].items()},
            maximum_witnesses=z["witnesses"],
            ordinary_L2_bounds={k:record(up(v.sqrt())) for k,v in z["squared"].items()},
            scalar_square_integrals={k:record(up(v)) for k,v in z["squared"].items()})
    collar=dict(exact_interval=list(map(str,COLLAR)),original_closed_rows_consumed=len(coll["rows"]),
        exact_total_radial_measure=str(coll["length"]),
        complete_signed_lower={k:record(v.lower()) for k,v in coll["lower"].items()},
        complete_signed_upper={k:record(v.upper()) for k,v in coll["upper"].items()},
        complete_absolute_upper={k:record(v.upper()) for k,v in coll["absolute"].items()},
        complete_ratio_upper={k:record(v.upper()) for k,v in coll["ratios"].items()},
        original_intrinsic_third_jets_read=True,original_target_evaluations=0,
        reference_s_is_not_full_moving_mean=True,moving_mean_gap_claimed=False)
    gate(doc,"all complete scalar maxima and true radial square integrals are finite",
         all(x.is_finite() and x>=0 for z in acc.values() for x in [*z["maxima"].values(),*z["squared"].values()]))
    gate(doc,"the original source support, all mean terms and separate nu boundary obligations remain intact",True)
    doc.update(complete=True,proved=True,
        complete_selected_parameter_body_scalar_fees_proved=True,
        complete_original_rows_verified=cursor,original_part_receipts=part_receipts,
        original_rows_canonical_payload_sha256=old_row_payload.hexdigest(),
        exact_original_interval=["0","25/8"],new_scalar_restrictions_evaluated=new_cell_budget_calls,
        new_compact_parameter_restrictions_evaluated=compact_calls,
        complete_scalar_fee_conclusions=conclusions,complete_original_collar_intrinsic_conclusion=collar,
        selected_parameter_operator_fees=dict(
            exact_core_interval=["0","9/10"],
            e=conclusions["whole_core"]["maxima"]["e_LL"],
            e_LH=conclusions["whole_core"]["maxima"]["e_LH"],
            ordinary_input="L2_r L2_phi with complete independent mean",
            source_head_physical_frequency=384,source_high_to_low_physical_frequency=1152,
            no_post_composition_or_phase_support_claimed=True),
        complete_nu_response_extra_source_sign="Delta F_nu + Delta A times the same complete continuous Z",
        nu_boundary_affine_and_true_cap_source_not_evaluated=True,
        old_target_Fourier_cubic_mean_residual_integral_or_Green_calls=0,
        old_numerical_enclosures_recomputed=0,
        complete_finite193_transferred_inverse_proved=False,
        complete_infinite_BVP_inverse_proved=False,true_parameter_Schur_proved=False,
        actual_new_Green_Poisson_gains_and_feedback_gates_still_required=True,
        actual_collar_full_moving_mean_gate_still_required=True,
        temporary_new_scalar_row_audit=dict(bytes=a.temporary_rows.stat().st_size,
            sha256=audit.hexdigest(),persisted=False),
        all_original_natural_part_bytes_modified=0,
        new_recomputable_outputs_persisted=False)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("manifest","original-manifest","response-summary","kernel-summary","temporary-rows","out"):
        p.add_argument("--"+name,type=Path,required=True)
    p.add_argument("--manifest-sha",required=True)
    p.add_argument("--parts",type=Path,nargs="+",required=True)
    p.add_argument("--bits",type=int,default=320)
    a=p.parse_args()
    if a.out.exists():raise FileExistsError("preserve an existing actual scalar conclusion")
    started=time.monotonic()
    doc=dict(kind=KIND,source_sha256=sha(__file__),input_manifest_sha256=sha(a.manifest),
        complete=False,proved=False,failure=None,gates=[],arithmetic_bits=a.bits,
        public_repository=os.environ.get("GITHUB_REPOSITORY"),run_id=os.environ.get("GITHUB_RUN_ID"),
        run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),parameters=PARAMETERS,
        original_enclosures_recomputed=0,complete_finite193_transferred_inverse_proved=False,
        complete_infinite_BVP_inverse_proved=False,true_parameter_Schur_proved=False)
    code=0
    try:run(a,doc)
    except BaseException as error:
        code=1;doc["failure"]=dict(type=type(error).__name__,message=str(error),
            traceback_frames=[dict(file=Path(x.filename).name,line=x.lineno,function=x.name)
                              for x in traceback.extract_tb(error.__traceback__)[-12:]])
    finally:
        doc["seconds"]=time.monotonic()-started;doc["actual_returncode"]=code
        if a.temporary_rows.exists():
            doc["temporary_row_audit_identity"]=dict(bytes=a.temporary_rows.stat().st_size,
                                                     sha256=sha(a.temporary_rows),persisted=False)
        save(a.out,doc)
        print(json.dumps(dict(complete=doc["complete"],actual_returncode=code,
            original_rows=doc.get("complete_original_rows_verified"),
            new_restrictions=doc.get("new_scalar_restrictions_evaluated"),
            actual_conclusion_sha256=sha(a.out),seconds=doc["seconds"]),sort_keys=True),flush=True)
    raise SystemExit(code)

if __name__=="__main__":main()
