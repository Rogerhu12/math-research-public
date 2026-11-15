#!/usr/bin/env python3
"""Request188: same-path nested closed-step accurate Hermite query domains.

Reuse the exact published84af R354 endpoint implementation in an independent
module; only explicit source identity and main orchestration strings change.
All scientific arithmetic runs in public Actions after the real original37
model/FD attempt. No original RHS/J/QR/model/FD call is added here.
All629 original full453 gap pairs remain before any query-angle visit.
After a direct strict closed-interval proof, smaller intervals of that SAME
accurate query/angle/path inherit its domain by set inclusion, not by a
claim that their different remainder boxes are nested or directly evaluated.
"""
from __future__ import annotations
import gzip
import hashlib
import json
import os
from pathlib import Path
import sys
import types

REPOSITORY="Rogerhu12/math-research-public"
BASE_NAME="exact_20261115_R354_thirty_seven_endpoint_remainder.py"
BASE_SHA="84af1e250b8a52d9b1691dd5dbeea4ff674ee79949fd72737e16c3f1b2fa018a"
BASE_BYTES=75046
CAPTURE_NAME="geometry_20261115_R354_thirty_seven_query_scalar_capture.py"
CAPTURE_SHA="0a8f4920d5f4c080c64f5e9ea6aedd203c90a475d99c4e73d5ddce6e7a9d5a90"
CAPTURE_SCHEMA="R354-original37-complete-query-scalar-cache-capture-v1"
SCHEMA="R398-original37-nested-closed-Hermite-query-domain-enclosures-v1"
DESIGN_NAME="2026-11-15-request175-complete-Hermite-query-domain-design.md"
DESIGN_SHA="b3094ad14bf332cfb6e891faf1d45eb4774075fe9cea7958788cc2f1474286a2"
DESIGN_BYTES=14877
INCLUSION_PROOF_NAME="R398-same-Hermite-path-nested-closed-domain-inheritance.md"
INCLUSION_PROOF_BYTES=11337
INCLUSION_PROOF_SHA="be828511c22ec7fe6c0e9dcefa1637b2b2587d5e634407d8e25ddb9e7ca82ba7"
PARENT_CONSUMER_NAME="exact_20261115_R354_thirty_seven_closed_query_domain.py"
PARENT_CONSUMER_BYTES=36928
PARENT_CONSUMER_SHA="cf4fa7b33bfcc13cd68193c3abc9b2da8edae4b90e64c16bcfbcce863a095d89"
HERE=Path(__file__).resolve().parent
R=None
STATE={"families":[],"pair_states":[],"bindings":[],"query_angle_cursor":None,
    "angle_commit_active":False,"deferred_external_signals":[]}


def require(ok,message):
    if not ok:raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def initial_query_result():
    return dict(
        schema="R398-complete37-same-path-nested-closed-domain-v1",
        declared_queries=37,declared_angles=2048,declared_steps=17,
        complete_augmented_components=453,physical_components=338,
        constant_RHS_components=115,complete_two_mean_rows=[0,225],
        complete_P_coefficient_count=15,highest_P_degree=14,
        scalar_degree_at_most_one_from_all_constant_RHS_rows=True,
        true_Hermite_path_not_claimed_a_fixed_quadratic=True,
        pointwise_coefficient_family_encloses_every_true_path_point=True,
        differentiating_remainder_family_as_fixed_coefficients=False,
        accurate_query_scalar_from_actual_singleton_cache=True,
        literal_scalar_baseline_not_inferred_from_rounded_value=True,
        original_explicit_B_controls_and_actual_cache_controls_separate=True,
        closed_steps_include_zero_and_both_endpoints=True,
        every_possible_endpoint_A_chunk_kept=True,
        query_scalar_cache_binding_complete=False,
        full453_uniform_gap_pairs_completed=0,
        full453_uniform_gap_pairs_available=0,
        query_angle_records_committed=0,
        query_angle_step_responsibilities_committed=0,
        query_angle_step_direct_evaluations_committed=0,
        query_angle_step_inclusion_inheritances_committed=0,
        query_angle_step_direct_strict_proofs=0,
        query_angle_step_inherited_strict_proofs=0,
        first_direct_strict_parent_trial_histogram=[0]*17,
        same_query_angle_and_accurate_Hermite_path_required=True,
        child_remainder_box_inclusion_not_required_or_claimed=True,
        unresolved_or_refuted_parent_never_inherited=True,
        all629_original_full453_gap_attempts_retained_before_query_phase=True,
        controlled_SIGTERM_SIGINT_deferred_across_whole_angle_commit=True,
        query_angle_step_strictly_proved=0,
        query_angle_step_rigorously_refuted=0,
        query_angle_step_unresolved=0,
        missing_endpoint_bound_pairs=0,
        complete_accurate_query_domain_on_all_closed_steps=False,
        complete_IEEE_query_execution_error_on_closed_steps_certified=False,
        whole699_node698_midpoint_RMS_checks_paid=False,
        continuous_angle_or_station_certificate=False,
        native_fullDN_final338_or_physical_audit_paid=False,
        direct_method_complete_coarse_closed_step_Bernstein=True,
        inherited_method_same_path_closed_interval_set_inclusion=True,
        all_requested_direct_step_range_evaluations_performed=False,
        no_adaptive_subdivision_or_hidden_extra_query_angles=True,
        original_model_FD_or_native_acceptance_gate_changed=False,
        actual_query_scalar_bindings=[],all_original_scalar_cache_returns=[],
        query_step_results=[],unvisited_or_unavailable_scopes=[],
        all_requested_query_angle_step_responsibilities_accounted_for=False)


def bind_query_scalar_caches(domain,angular,packets,np,result,budget):
    qr=result["query_domain_188"]
    for index in sorted(angular):
        budget.check(phase="bind-every-original-query-scalar-cache",angular_return_index=index)
        row=angular[index];data=packets.get(row["packet"])
        cache=row.get("scalar_cache")
        require(isinstance(cache,dict),"Original query scalar cache receipt is required")
        require(cache.get("original_scalar_jets_source_sha256")==R.AUGMENTED_SHA and
            cache.get("copied_existing_cache_after_original_scalar_return") is True and
            cache.get("no_new_profile_RHS_J_or_scalar_call") is True and
            cache.get("not_reconstructed_from_returned_rounded_scalar") is True,
            "Copy only the actual original scalar cache")
        stations=data["scalar_cache_stations"]
        baseline=data["scalar_cache_baseline"];controls=data["scalar_cache_controls"]
        require(stations.dtype.str=="<f8" and stations.shape==(1,) and
            stations.tobytes()==bytes.fromhex(row["station_float64le"]),
            "Literal singleton query station, including sign of zero")
        require(baseline.shape==(1,3) and controls.shape==(1,3,3) and
            baseline.dtype.str=="<f8" and controls.dtype.str=="<f8" and
            np.all(np.isfinite(baseline)) and np.all(np.isfinite(controls)),
            "All three scalar jets and all nine control entries are retained")
        for name,value in (("stations",stations),("baseline",baseline),("controls",controls)):
            require(R.np_identity(value)==cache[name],"Complete query cache words match receipt")
        qr["all_original_scalar_cache_returns"].append(dict(
            angular_return_index=index,context=row["context"],
            station_float64le=row["station_float64le"],packet=row["packet"],
            original_cache_identity=cache,
            original_rounded_scalar_identity=row["packet"]["arrays"]["scalar"],
            no_claim_that_rounded_scalar_equals_accurate_b_plus_Cp=True))
    answer=[]
    for q,query in enumerate(domain["queries"]):
        index=domain["angular_return_indices"][q]
        row=angular[index];data=packets.get(row["packet"])
        qp=packets.get(query["packet"])
        require(row["context"].get("kind")=="domain-build" and
            row["station_float64le"]==query["station_float64le"] and
            data["query"].tobytes()==qp["query"].tobytes(),
            "Bind the actual base-domain query to its own returned scalar cache")
        explicit=packets.get(domain["matched_query_controls"][q]["packet"])["controls"]
        same=(explicit.tobytes()==data["scalar_cache_controls"][0].tobytes())
        binding=dict(query_index=q,kind=query["kind"],interval=query["interval"],
            original_angular_return_index=index,station_float64le=row["station_float64le"],
            singleton_scalar_cache=row["scalar_cache"],
            original_explicit_B_control_identity=query["original_explicit_scalar_control_identity"],
            actual_cache_controls_byte_equal_explicit_B_controls=same,
            inequality_not_a_new_original_gate=True,packet=row["packet"])
        qr["actual_query_scalar_bindings"].append(binding)
        answer.append(dict(baseline=data["scalar_cache_baseline"][0],
            controls=data["scalar_cache_controls"][0],binding=binding))
    qr["query_scalar_cache_binding_complete"]=True
    STATE["bindings"]=answer
    return answer


def interval_jet(coefficients,trig):
    """All338 coefficients, exact sums of outward product endpoints."""
    require(len(coefficients)==453 and len(trig)==112,"Full augmented Fourier coefficient box")
    I=R.Interval;S=R.SCALE
    low=[0]*6;high=[0]*6
    r0=coefficients[0]
    low[1]+=r0.lo*S;high[1]+=r0.hi*S
    low[3]+=-r0.hi*S;high[3]+=-r0.lo*S
    for k,(sine,cosine) in enumerate(trig,1):
        f=2*k;r=coefficients[k];t=coefficients[112+k];z=coefficients[225+k]
        signals=(-(r*f+t),r+t*f,-z*f,
            -(r*(f*f+1)+t*(2*f)),-(r*(2*f)+t*(f*f+1)),-z*(f*f))
        for component,(signal,weight) in enumerate(zip(signals,
                (sine,cosine,sine,cosine,sine,cosine))):
            lo,hi=R.product_integer_bounds(signal,weight)
            low[component]+=lo;high[component]+=hi
    values=[I(lo//S,-((-hi)//S)) for lo,hi in zip(low,high)]
    return values[:3],values[3:]


def projected_remainder_jet_envelope(trig,radius):
    """Image bound of the full projection-pattern box, not a discarded column.

Mean coefficient radii are radius, all nonmean physical radii2*radius.
The z mean is retained in the full453 gap but has zero angular jet.
"""
    S=R.SCALE;upper=[0,S,0,S,0,0]
    for k,(sine,cosine) in enumerate(trig,1):
        f=2*k;ss=sine.absolute_upper();cc=cosine.absolute_upper()
        upper[0]+=2*(f+1)*ss
        upper[1]+=2*(f+1)*cc
        upper[2]+=2*f*ss
        upper[3]+=2*(f+1)*(f+1)*cc
        upper[4]+=2*(f+1)*(f+1)*ss
        upper[5]+=2*f*f*cc
    out=[]
    for value in upper:
        bound=-((-radius*value)//S)
        out.append(R.Interval(-bound,bound))
    return out[:3],out[3:]


def coefficients_on_unit_interval(poly,lo,hi):
    """Translate the whole polynomial; all coefficients are used."""
    I=R.Interval;degree=len(poly)-1
    L=I(lo);W=I(hi-lo)
    lp=[I.integer(1)];wp=[I.integer(1)]
    for _ in range(degree):
        lp.append(lp[-1]*L);wp.append(wp[-1]*W)
    out=[]
    for j in range(degree+1):
        value=R.IZERO
        for k in range(j,degree+1):
            value=value+poly[k]*R.math.comb(k,j)*lp[k-j]*wp[j]
        out.append(value)
    return out


def complete_range(poly,lo,hi):
    if lo==hi:return R.p_value(poly,R.Interval(lo))
    shifted=coefficients_on_unit_interval(poly,lo,hi)
    return R.p_bernstein(shifted,R.Interval.integer(1)).intersect(
        R.p_value(poly,R.Interval(lo,hi)))


def query_polynomials(d0,d1,d2,e0,e1,e2,scalar0,scalar1):
    d=[[d0[k],d1[k],d2[k]] for k in range(3)]
    e=[[e0[k],e1[k],e2[k]] for k in range(3)]
    a=[scalar0[0],scalar1[0]];nu=[scalar0[1],scalar1[1]]
    Q=R.p_dot(d,d);C=R.p_cross(d,e);W=R.p_dot(C,C)
    P=R.p_add(R.p_mul(R.p_mul(a,a),W),
        R.p_mul(R.p_mul(nu,nu),R.p_mul(R.p_mul(Q,Q),Q)),-1)
    require(len(Q)==5 and len(W)==9 and len(P)==15,
        "Keep complete degree14 P; no inherited degree8 truncation")
    return dict(a=a,nu=nu,Q=Q,W=W,P=P)


def contradiction(values):
    if values["a"].hi<=0:return "accurate-radius-upper-nonpositive"
    if values["P"].hi<=0:return "accurate-P-upper-nonpositive"
    if values["nu"].lo>=R.SCALE:return "accurate-nu-entire-box-at-or-above-one"
    if values["nu"].hi<=-R.SCALE:return "accurate-nu-entire-box-at-or-below-minus-one"
    return None


def classify_closed_polynomial(poly,j):
    hi=R.SCALE >> j
    values={k:complete_range(poly[k],0,hi) for k in ("a","nu","Q","W","P")}
    why=contradiction(values)
    common=dict(closed_alpha_interval=[R.Interval(0).record(),R.Interval(hi).record()],
        all15_P_coefficients=[v.record() for v in poly["P"]],
        scalar_a_coefficients=[v.record() for v in poly["a"]],
        scalar_nu_coefficients=[v.record() for v in poly["nu"]],
        all_Q_coefficients=[v.record() for v in poly["Q"]],
        all_W_coefficients=[v.record() for v in poly["W"]],
        complete_closed_bounds={k:v.record() for k,v in values.items()},
        no_IEEE_execution_error_enclosure=True,
        no_derivative_of_the_variable_remainder_family_taken=True)
    if why:
        return dict(common,status="rigorously-refuted-on-whole-closed-interval",
            refutation_reason=why)
    if (values["a"].lo>0 and values["P"].lo>0 and
            values["nu"].lo>-R.SCALE and values["nu"].hi<R.SCALE):
        return dict(common,status="strictly-proved-on-whole-closed-interval",
            positive_Q_W_follows_also_from_exact_norm_and_P_identity=True)
    # A point refutation refutes the full closed-domain proposition, without
    # asserting that every point of the interval fails.
    for t in (0,hi):
        point={k:R.p_value(poly[k],R.Interval(t)) for k in ("a","nu","Q","W","P")}
        reason=contradiction(point)
        if reason:
            return dict(common,status="rigorously-refuted-at-a-closed-endpoint",
                refutation_reason=reason,accurate_alpha_witness=R.Interval(t).record(),
                complete_point_bounds={k:v.record() for k,v in point.items()},
                whole_interval_pointwise_failure_not_claimed=True)
    return dict(common,status="unresolved",
        unresolved_conditions=dict(a=values["a"].lo<=0,P=values["P"].lo<=0,
            nu=values["nu"].lo<=-R.SCALE or values["nu"].hi>=R.SCALE),
        interval_width_or_dependency_not_claimed_a_refutation=True)


def scalar_coefficients(binding,H0,H1):
    I=R.Interval;zero=R.IZERO
    ans=[]
    for row in range(3):
        a0=I.floating(binding["baseline"][row]);a1=zero
        for column in range(3):
            c=I.floating(binding["controls"][row,column])
            a0=a0+c*H0[450+column];a1=a1+c*H1[450+column]
        ans.append((a0,a1))
    return [v[0] for v in ans],[v[1] for v in ans]


def full_coefficient_summary(vectors):
    return {name:R.interval_vector_summary(values) for name,values in vectors.items()}



def endpoint_second_upper(variant,j):
    if variant.get("reference") is None or variant.get("closed") is None:return None
    row=variant["closed"][j]
    if row["complete_angle_rows"]!=R.ANGLES or row["strict_regular_count"]!=R.ANGLES:
        return None
    return row["_M"]


def fresh_pair_record(q,query,j,slots,query_variants):
    return dict(query_index=q,kind=query["kind"],interval=query["interval"],
        station_float64le=query["station_float64le"],
        trial_index=j,alpha_float64le=R.word(2.0**(-j)),
        original_trial_visited=slots[j]["original_trial_visited"],
        endpoint_variants=list(query_variants[q]),
        closed_alpha=[R.Interval(0).record(),R.Interval(R.SCALE>>j).record()],
        full453_uniform_gap_attempt_accounted=False,
        full453_uniform_gap_available=False,
        complete_closed_query_angle_rows=0,strictly_proved_angle_count=0,
        direct_angle_evaluations_committed=0,inherited_angle_proofs_committed=0,
        direct_strictly_proved_angle_count=0,inherited_strictly_proved_angle_count=0,
        direct_strict_angle_ranges=[],inherited_strict_angle_ranges=[],
        rigorously_refuted_angle_count=0,unresolved_angle_count=0,
        strict_angle_ranges=[],rigorously_refuted_angle_ranges=[],
        unresolved_angle_ranges=[],unvisited_angle_ranges=[[0,R.ANGLES-1]],
        complete_accurate_query_domain_proved=False,
        original_IEEE_query_program_domain_not_certified=True,
        missing_endpoint_bound_reason=None)


def prepare_complete_families(domain,query_state,variants,query_variants,bindings,
        slots,budget,ledger,result):
    """Pay every full453 uniform gap before any query-angle subdivision."""
    qr=result["query_domain_188"];I=R.Interval
    STATE["families"]=[None]*37
    STATE["pair_states"]=[
        fresh_pair_record(q,query,j,slots,query_variants)
        for q,query in enumerate(domain["queries"]) for j in range(17)]
    qr["query_step_results"]=STATE["pair_states"]
    for q,query in enumerate(domain["queries"]):
        budget.check(phase="prepare-complete453-closed-Hermite-family",query_index=q)
        item=query_state[q];left,right=(variants[i] for i in query_variants[q])
        if left.get("reference") is None or right.get("reference") is None:
            for j in range(17):
                row=STATE["pair_states"][q*17+j]
                row["full453_uniform_gap_attempt_accounted"]=True
                row["missing_endpoint_bound_reason"]="full453 accurate endpoint reference unavailable"
                qr["full453_uniform_gap_pairs_completed"]+=1
                qr["missing_endpoint_bound_pairs"]+=1
            continue
        h=I.dyadic(item["h"]);wl=I.dyadic(item["weights"][1]);wr=I.dyadic(item["weights"][3])
        G0=[];G1=[]
        for k in range(453):
            G0.append(I.dyadic(item["delta0"][k])+h*(
                wl*left["reference"]["e0"][k]+wr*right["reference"]["e0"][k]))
            G1.append(I.dyadic(item["delta1"][k])+h*(
                wl*left["reference"]["e1"][k]+wr*right["reference"]["e1"][k]))
        H0=[I.floating(item["q0"][k])+G0[k] for k in range(453)]
        H1=[I.floating(item["q1"][k])+G1[k] for k in range(453)]
        scalar0,scalar1=scalar_coefficients(bindings[q],H0,H1)
        family=dict(G0=G0,G1=G1,H0=H0,H1=H1,scalar0=scalar0,
            scalar1=scalar1,radius_by_step=[None]*17)
        ledger.write(dict(kind="complete453-accurate-Hermite-family-base",
            query_index=q,endpoint_variants=list(query_variants[q]),
            G0=[v.record() for v in G0],G1=[v.record() for v in G1],
            H0=[v.record() for v in H0],H1=[v.record() for v in H1],
            exact_literal_q0_words=[R.word(v) for v in item["q0"]],
            formed_literal_q1_words=[R.word(v) for v in item["q1"]],
            scalar_a_nu_mu_constant=[v.record() for v in scalar0],
            scalar_a_nu_mu_linear=[v.record() for v in scalar1],
            actual_singleton_scalar_binding=bindings[q]["binding"],
            all115_constant_RHS_rows_retained=True,
            no_rounded_scalar_to_baseline_reconstruction=True))
        STATE["families"][q]=family
        for j in range(17):
            budget.check(trial_index=j)
            row=STATE["pair_states"][q*17+j]
            Ml=endpoint_second_upper(left,j);Mr=endpoint_second_upper(right,j)
            if Ml is None or Mr is None:
                row["full453_uniform_gap_attempt_accounted"]=True
                row["missing_endpoint_bound_reason"]="at least one endpoint lacks its full2048 closed second-derivative bound"
                qr["full453_uniform_gap_pairs_completed"]+=1
                qr["missing_endpoint_bound_pairs"]+=1
                continue
            # Exact projection norms give the mean/nonmean1:2 pattern. The
            # outer interval makes the common mean radius an outward bound.
            coefficient=h*(wl*I(-Ml,Ml)+wr*I(-Mr,Mr))/2
            radius=coefficient.absolute_upper()
            G2=[I(-radius,radius) if k in R.MEAN_ROWS else
                I(-2*radius,2*radius) if k<338 else R.IZERO for k in range(453)]
            hi=R.SCALE>>j
            gap=[complete_range([G0[k],G1[k],G2[k]],0,hi) for k in range(453)]
            path=[complete_range([H0[k],H1[k],G2[k]],0,hi) for k in range(453)]
            scalar_bounds=[complete_range([scalar0[k],scalar1[k]],0,hi) for k in range(3)]
            ledger.write(dict(kind="complete453-whole-closed-Hermite-gap",
                query_index=q,trial_index=j,
                closed_alpha=[I(0).record(),I(hi).record()],
                all453_remainder_coefficient_boxes=[v.record() for v in G2],
                all453_uniform_gap_boxes=[v.record() for v in gap],
                all453_true_Hermite_path_boxes=[v.record() for v in path],
                endpoint_second_derivative_upper=dict(left=R.upper_record(Ml),right=R.upper_record(Mr)),
                mean_remainder_coefficient_radius=R.upper_record(radius),
                scalar_a_nu_mu_closed_bounds=[v.record() for v in scalar_bounds],
                pointwise_family_not_claimed_a_fixed_polynomial_path=True,
                every_parameter_second_remainder_exact_zero=True))
            family["radius_by_step"][j]=radius
            row.update(full453_uniform_gap_attempt_accounted=True,
                full453_uniform_gap_available=True,
                uniform_gap_summary=R.interval_vector_summary(gap),
                complete_Hermite_path_summary=R.interval_vector_summary(path),
                endpoint_second_derivative_upper=dict(left=R.upper_record(Ml),right=R.upper_record(Mr)),
                mean_remainder_coefficient_radius=R.upper_record(radius),
                scalar_a_nu_mu_closed_bounds=[v.record() for v in scalar_bounds],
                no_IEEE_execution_error_certificate=True)
            qr["full453_uniform_gap_pairs_completed"]+=1
            qr["full453_uniform_gap_pairs_available"]+=1


def defer_external_stop(signum):
    """Only the short metadata/ledger commit defers the original raising handler."""
    if STATE["angle_commit_active"]:
        STATE["deferred_external_signals"].append(signum)
        return True
    return False


def inherited_closed_outcome(parent,q,angle,j):
    """Proof transfer for the identical actual path; no child polynomial range."""
    k=parent["trial_index"]
    require(parent["query_index"]==q and parent["angle_index"]==angle and
        parent["status"]=="strictly-proved-on-whole-closed-interval" and
        0<=k<j<17 and (R.SCALE>>j)<=(R.SCALE>>k),
        "Only a direct strict same-query/angle proof may cover this dyadic child")
    return dict(status="strictly-proved-by-containing-closed-step",
        proof_method="same-accurate-Hermite-path-closed-interval-inclusion",
        directly_classified_child_coefficient_family=False,
        source_direct_trial_index=k,
        source_direct_outcome=dict(bytes=parent["outcome_bytes"],
            sha256=parent["outcome_sha256"],
            reference="same atomic all17 angle record; all_alpha_results at source trial"),
        source_query_index=q,source_angle_index=angle,
        containing_closed_alpha=[R.Interval(0).record(),R.Interval(R.SCALE>>k).record()],
        closed_alpha_interval=[R.Interval(0).record(),R.Interval(R.SCALE>>j).record()],
        all_three_query_scalar_jets_and_full453_parent_path_identical=True,
        actual_pointwise_Hermite_path_restricted_not_replaced=True,
        no_claim_of_nesting_between_remainder_coefficient_boxes=True,
        no_IEEE_execution_error_enclosure=True,
        inclusion_proof=dict(file=INCLUSION_PROOF_NAME,sha256=INCLUSION_PROOF_SHA))


def visit_complete_query_angles(domain,trig,budget,ledger,result):
    """One committed17-step record; direct ranges and inherited proofs are distinct."""
    qr=result["query_domain_188"]
    for q,query in enumerate(domain["queries"]):
        family=STATE["families"][q]
        if family is None or all(v is None for v in family["radius_by_step"]):
            continue
        for angle in range(R.ANGLES):
            budget.check(phase="R398-nested-closed-query-domain",
                query_index=q,angle_index=angle,trial_index=None)
            STATE["query_angle_cursor"]=dict(query_index=q,angle_index=angle,
                next_trial_index=0,whole_angle_record_committed=False)
            table=trig.row(angle)
            d0,e0=interval_jet(family["H0"],table)
            d1,e1=interval_jet(family["H1"],table)
            outcomes=[];parent=None
            for j,radius in enumerate(family["radius_by_step"]):
                STATE["query_angle_cursor"]["next_trial_index"]=j
                if radius is None:
                    outcomes.append(dict(trial_index=j,status="not-computed-endpoint-bound-unavailable"))
                    continue
                budget.check(trial_index=j)
                if parent is not None:
                    outcome=inherited_closed_outcome(parent,q,angle,j)
                else:
                    d2,e2=projected_remainder_jet_envelope(table,radius)
                    poly=query_polynomials(d0,d1,d2,e0,e1,e2,
                        family["scalar0"],family["scalar1"])
                    outcome=classify_closed_polynomial(poly,j)
                    outcome["proof_method"]="direct-complete-coefficient-range"
                    outcome["directly_classified_child_coefficient_family"]=True
                record=dict(trial_index=j,**outcome)
                outcomes.append(record)
                if (parent is None and
                        outcome["status"]=="strictly-proved-on-whole-closed-interval"):
                    raw=R.canonical(record)
                    parent=dict(query_index=q,angle_index=angle,trial_index=j,
                        status=outcome["status"],outcome_bytes=len(raw),
                        outcome_sha256=sha(raw))
            # Original84af SIGTERM/SIGINT handlers raise immediately. The
            # explicit private-main callback records them during this short
            # commit, including signals delivered through another OS thread.
            # Byte-cap exceptions occur before counter changes. An OS hard kill
            # or I/O failure is not a claim of complete transport/commit.
            STATE["angle_commit_active"]=True
            try:
                ledger.write(dict(kind="all17-complete-closed-Hermite-query-angle",
                    query_index=q,kind_of_query=query["kind"],interval=query["interval"],
                    original_angle_index=angle,declared_angle_count=R.ANGLES,
                    complete_physical_synthesis_coefficients=338,
                    complete_augmented_state_components=453,
                    all_alpha_results=outcomes,
                    all_three_query_scalar_jets_retained=True,
                    true_Hermite_path_enclosed_by_pointwise_coefficient_family=True,
                    direct_and_inherited_steps_distinct=True,
                    first_direct_strict_parent_trial=None if parent is None else parent["trial_index"],
                    inclusion_references_only_same_complete_angle_record=True))
                for outcome in outcomes:
                    j=outcome["trial_index"]
                    if outcome["status"]=="not-computed-endpoint-bound-unavailable":
                        continue
                    row=STATE["pair_states"][q*17+j]
                    row["complete_closed_query_angle_rows"]+=1
                    qr["query_angle_step_responsibilities_committed"]+=1
                    status=outcome["status"]
                    inherited=(status=="strictly-proved-by-containing-closed-step")
                    if inherited:
                        row["inherited_angle_proofs_committed"]+=1
                        qr["query_angle_step_inclusion_inheritances_committed"]+=1
                    else:
                        row["direct_angle_evaluations_committed"]+=1
                        qr["query_angle_step_direct_evaluations_committed"]+=1
                    if status in ("strictly-proved-on-whole-closed-interval",
                            "strictly-proved-by-containing-closed-step"):
                        row["strictly_proved_angle_count"]+=1
                        qr["query_angle_step_strictly_proved"]+=1
                        R.ranges_add(row["strict_angle_ranges"],angle)
                        if inherited:
                            row["inherited_strictly_proved_angle_count"]+=1
                            qr["query_angle_step_inherited_strict_proofs"]+=1
                            R.ranges_add(row["inherited_strict_angle_ranges"],angle)
                        else:
                            row["direct_strictly_proved_angle_count"]+=1
                            qr["query_angle_step_direct_strict_proofs"]+=1
                            R.ranges_add(row["direct_strict_angle_ranges"],angle)
                    elif status.startswith("rigorously-refuted-"):
                        row["rigorously_refuted_angle_count"]+=1
                        qr["query_angle_step_rigorously_refuted"]+=1
                        R.ranges_add(row["rigorously_refuted_angle_ranges"],angle)
                    else:
                        require(status=="unresolved","Every committed angle has an explicit outcome")
                        row["unresolved_angle_count"]+=1
                        qr["query_angle_step_unresolved"]+=1
                        R.ranges_add(row["unresolved_angle_ranges"],angle)
                    row["unvisited_angle_ranges"]=([] if angle+1==R.ANGLES else [[angle+1,R.ANGLES-1]])
                if parent is not None:
                    qr["first_direct_strict_parent_trial_histogram"][parent["trial_index"]]+=1
                qr["query_angle_records_committed"]+=1
                STATE["query_angle_cursor"].update(next_trial_index=17,whole_angle_record_committed=True)
            finally:
                STATE["angle_commit_active"]=False
            if STATE["deferred_external_signals"]:
                raise R.ResourceStop("external signal(s) "+
                    repr(STATE["deferred_external_signals"])+
                    " deferred only until this complete angle ledger/counter commit")


def finalize_query(result):
    """JSON/metadata only; no unvisited arithmetic is done in finalization."""
    qr=result["query_domain_188"]
    pairs=STATE["pair_states"]
    qr["unvisited_or_unavailable_scopes"]=[]
    if not pairs:
        qr["unvisited_or_unavailable_scopes"]=[dict(query_range=[0,36],
            trial_range=[0,16],angle_range=[0,2047],augmented_component_range=[0,452],
            reason="query-family phase not reached",
            earlier_actual_phase=result.get("stop_reason"))]
    for row in pairs:
        count=row["complete_closed_query_angle_rows"]
        row["complete_accurate_query_domain_proved"]=(
            row["full453_uniform_gap_available"] and count==R.ANGLES and
            row["strictly_proved_angle_count"]==R.ANGLES)
        row["any_accurate_query_angle_rigorously_refuted"]=row["rigorously_refuted_angle_count"]>0
        row["unvisited_angle_ranges"]=([] if count==R.ANGLES else [[count,R.ANGLES-1]])
        if count<R.ANGLES:
            qr["unvisited_or_unavailable_scopes"].append(dict(
                query_index=row["query_index"],kind=row["kind"],interval=row["interval"],
                trial_index=row["trial_index"],angle_range=[count,R.ANGLES-1],
                full453_uniform_gap_available=row["full453_uniform_gap_available"],
                reason=row["missing_endpoint_bound_reason"] or
                    "explicit resource/exception stop before complete query-angle visit",
                no_missing_angle_replaced_by_zero=True))
    qr["complete_accurate_query_domain_on_all_closed_steps"]=(
        len(pairs)==37*17 and all(x["complete_accurate_query_domain_proved"] for x in pairs))
    qr["all_requested_query_angle_step_responsibilities_accounted_for"]=(
        len(pairs)==37*17 and all(x["full453_uniform_gap_available"] and
            x["complete_closed_query_angle_rows"]==R.ANGLES for x in pairs))
    qr["all_requested_direct_step_range_evaluations_performed"]=(
        qr["all_requested_query_angle_step_responsibilities_accounted_for"] and
        qr["query_angle_step_inclusion_inheritances_committed"]==0 and
        qr["query_angle_step_direct_evaluations_committed"]==37*17*R.ANGLES)
    qr["committed_method_counts_consistent"]=(
        qr["query_angle_step_responsibilities_committed"]==
            qr["query_angle_step_direct_evaluations_committed"]+
            qr["query_angle_step_inclusion_inheritances_committed"] and
        qr["query_angle_step_strictly_proved"]==
            qr["query_angle_step_direct_strict_proofs"]+
            qr["query_angle_step_inherited_strict_proofs"])
    qr["all_requested_scopes_explicitly_accounted_for"]=(
        len(pairs)==37*17 or bool(qr["unvisited_or_unavailable_scopes"]))
    qr["full453_uniform_gap_available_on_all_steps"]=(
        len(pairs)==37*17 and all(x["full453_uniform_gap_available"] for x in pairs))
    qr["any_accurate_query_angle_rigorously_refuted"]=qr["query_angle_step_rigorously_refuted"]>0
    qr["last_query_angle_transaction"]=STATE["query_angle_cursor"]
    qr["actual_deferred_external_signals"]=list(STATE["deferred_external_signals"])
    qr["angle_commit_active_at_finalization"]=STATE["angle_commit_active"]
    result["scope"]["complete_true_Hermite_query_angular_domain_transfer_paid"]=(
        qr["complete_accurate_query_domain_on_all_closed_steps"])
    result["scope"]["whole_alpha_uniform_Hermite_gap_enclosure_computed"]=(
        qr["full453_uniform_gap_available_on_all_steps"])
    result["scope"]["old_pointwise_Hermite_transfer_kept_separately"]=True
    result["scope"]["whole_closed_gap_scope_remains_original175_not_old_pointwise170"]=True
    result["scope"]["same_path_set_inclusion_is_independent188_query_domain_method"]=True
    result["scope"]["original175_uncomputed_scope_not_filled_by_this_new_run"]=True


def compact_query(result):
    qr=result["query_domain_188"]
    keys=("schema","declared_queries","declared_angles","declared_steps",
        "query_scalar_cache_binding_complete","full453_uniform_gap_pairs_completed",
        "full453_uniform_gap_pairs_available","query_angle_records_committed",
        "query_angle_step_responsibilities_committed",
        "query_angle_step_direct_evaluations_committed","query_angle_step_inclusion_inheritances_committed",
        "query_angle_step_direct_strict_proofs","query_angle_step_inherited_strict_proofs",
        "query_angle_step_strictly_proved","committed_method_counts_consistent",
        "all_requested_direct_step_range_evaluations_performed",
        "query_angle_step_rigorously_refuted","query_angle_step_unresolved",
        "missing_endpoint_bound_pairs","complete_accurate_query_domain_on_all_closed_steps",
        "full453_uniform_gap_available_on_all_steps","all_requested_query_angle_step_responsibilities_accounted_for",
        "all_requested_scopes_explicitly_accounted_for",
        "any_accurate_query_angle_rigorously_refuted",
        "complete_IEEE_query_execution_error_on_closed_steps_certified",
        "native_fullDN_final338_or_physical_audit_paid",
        "direct_method_complete_coarse_closed_step_Bernstein",
        "inherited_method_same_path_closed_interval_set_inclusion",
        "first_direct_strict_parent_trial_histogram",
        "actual_deferred_external_signals","angle_commit_active_at_finalization",
        "last_query_angle_transaction")
    return {k:qr.get(k) for k in keys}


def query_extension(domain,query_state,variants,query_variants,angular,slots,
        packets,np,trig,budget,large,ledgers,bank,maximum,result):
    bindings=bind_query_scalar_caches(domain,angular,packets,np,result,budget)
    families=R.Ledger(large/"complete453-closed-query-families.jsonl.gz",maximum,bank)
    ledgers.append(families)
    try:
        prepare_complete_families(domain,query_state,variants,query_variants,bindings,
            slots,budget,families,result)
    finally:
        R.close_ledger(families)
    angles=R.Ledger(large/"complete17-closed-query-domain-angles.jsonl.gz",maximum,bank)
    ledgers.append(angles)
    try:
        visit_complete_query_angles(domain,trig,budget,angles,result)
    finally:
        R.close_ledger(angles)
    finalize_query(result)
    return 0 if result["query_domain_188"]["complete_accurate_query_domain_on_all_closed_steps"] else 3



def emit_summary(out,summary,scientific_code):
    """Only bounded summaries go to the watcher; complete JSON stays in-job."""
    complete=R.safe_write(out/"summary-complete.json",summary)
    summary["complete_summary_file"]=complete
    summary["pending_reference_scope_count"]=len(summary.pop("pending_reference_scopes",[]))
    summary["pending_Hermite_transfer_pair_count"]=len(summary.pop("pending_Hermite_transfer_pairs",[]))
    summary["complete_pending_ranges_are_in_actual_result"]=True
    summary["summary_complete"]=True;summary["transport_complete"]=True
    event=dict(event="request188_post_model_R354_returned",**summary)
    raw=R.canonical(event)
    if len(raw)>88000:
        # This is solely a transport error, never a different model/FD outcome.
        # Both original full JSON documents remain for same-job readback.
        summary=dict(schema=SCHEMA,request=188,result=summary["result"],
            complete_summary_file=complete,summary_complete=False,transport_complete=False,
            transport_error="bounded-summary-exceeds88000bytes",
            original_summary_bytes=len(raw),original_summary_sha256=sha(raw),
            original_scientific_exit_code=scientific_code,process_exit_code=70,
            complete_scalar_and_pending_metadata_retained_for_same_job=True,
            original_model_and_FD_gates_not_changed=True)
        raw=R.canonical(dict(event="request188_post_model_R354_returned",**summary))
        require(len(raw)<=88000,"The fixed transport-failure record is bounded")
        R.safe_write(out/"summary.json",summary)
        sys.stdout.write(raw.decode("ascii"));sys.stdout.flush()
        return 70
    R.safe_write(out/"summary.json",summary)
    sys.stdout.write(raw.decode("ascii"));sys.stdout.flush()
    return scientific_code


SOURCE_REPLACEMENTS=[
    dict(label="independent-description",old="\"\"\"Request170: R354 complete finite endpoint reference and Hermite bounds.",new="\"\"\"Request188: nested closed-Hermite query domains using the published endpoint kernel.",count=1),
    dict(label="independent-schema",old="SCHEMA=\"R354-original37-finite-endpoint-and-Hermite-enclosures-v1\"",new="SCHEMA=\"R398-original37-nested-closed-Hermite-query-domain-enclosures-v1\"",count=1),
    dict(label="query-cache-capture-schema",old="CAPTURE_SCHEMA=\"R354-original37-endpoint-literal-cache-capture-v1\"",new="CAPTURE_SCHEMA=\"R354-original37-complete-query-scalar-cache-capture-v1\"",count=1),
    dict(label="query-cache-capture-file",old="CAPTURE_NAME=\"geometry_20261115_R354_thirty_seven_literal_endpoint_capture.py\"",new="CAPTURE_NAME=\"geometry_20261115_R354_thirty_seven_query_scalar_capture.py\"",count=1),
    dict(label="query-cache-capture-source",old="CAPTURE_SHA=\"74fc383db1b00c564ccab9709b1de5f500674914a5efef83997960c867950c4c\"",new="CAPTURE_SHA=\"0a8f4920d5f4c080c64f5e9ea6aedd203c90a475d99c4e73d5ddce6e7a9d5a90\"",count=1),
    dict(label="result-request-number",old="result=dict(schema=SCHEMA,request=170,run_id=os.environ.get(\"GITHUB_RUN_ID\"),",new="result=dict(schema=SCHEMA,request=188,run_id=os.environ.get(\"GITHUB_RUN_ID\"),",count=1),
    dict(label="initialize-new-result",old="    slots=[];packets=None;trig=None;exit_code=2\n",new="    slots=[];packets=None;trig=None;exit_code=2\n    result[\"query_domain_188\"]=_R188_INITIAL()\n    result[\"explicit_published_source_adaptation\"]=_R188_ADAPTATION\n",count=1),
    dict(label="new-query-domain-after-original-endpoint-work",old="        close_ledger(transfer)\n        result[\"scientific_completed\"]=True\n        result[\"stop_reason\"]=\"all-declared-independent-computations-visited\"\n        exit_code=0 if all(v[\"accurate_reference_pointwise_Hermite_bound_available\"]\n            for v in result[\"Hermite_transfer\"]) else 3\n",new="        close_ledger(transfer)\n        exit_code=_R188_EXTENSION(domain,query_state,variants,query_variants,angular,slots,\n            packets,np,trig,budget,large,ledgers,bank,args.max_ledger_bytes,result)\n        result[\"scientific_completed\"]=result[\"query_domain_188\"][\"all_requested_query_angle_step_responsibilities_accounted_for\"]\n        result[\"stop_reason\"]=(\"all-declared-endpoint-and-query-responsibilities-accounted\"\n            if result[\"scientific_completed\"] else \"nested-closed-query-dependency-unavailable\")\n",count=1),
    dict(label="defer-control-signal-only-during-angle-commit",old="    def external_stop(signum,frame):\n        raise ResourceStop(\"external signal \"+str(signum)+\" interrupted the independent diagnostic\")\n",new="    def external_stop(signum,frame):\n        if _R188_DEFER_SIGNAL(signum):return\n        raise ResourceStop(\"external signal \"+str(signum)+\" interrupted the independent diagnostic\")\n",count=1),
    dict(label="complete-suffix-and-scope-finalization",old="        signal.signal(signal.SIGTERM,signal.SIG_IGN);signal.signal(signal.SIGINT,signal.SIG_IGN)\n        for ledger in ledgers:",new="        signal.signal(signal.SIGTERM,signal.SIG_IGN);signal.signal(signal.SIGINT,signal.SIG_IGN)\n        _R188_FINALIZE(result)\n        for ledger in ledgers:",count=1),
    dict(label="actual-query-domain-result-flag",old="        result[\"complete_true_Hermite_query_angle_domain_certified\"]=False\n",new="        result[\"complete_true_Hermite_query_angle_domain_certified\"]=result[\"query_domain_188\"][\"complete_accurate_query_domain_on_all_closed_steps\"]\n",count=1),
    dict(label="summary-request-number",old="        summary=dict(schema=SCHEMA,request=170,result=result_receipt,",new="        summary=dict(schema=SCHEMA,request=188,result=result_receipt,",count=1),
    dict(label="actual-query-domain-summary-flag",old="            complete_true_Hermite_query_angle_domain_certified=False,\n",new="            complete_true_Hermite_query_angle_domain_certified=result[\"complete_true_Hermite_query_angle_domain_certified\"],\n            query_domain_188=_R188_COMPACT(result),\n",count=1),
    dict(label="bounded-summary-transport-with-full-retained-json",old="        safe_write(args.out/\"summary.json\",summary)\n        print(json.dumps(dict(event=\"request170_post_model_R354_returned\",**summary),\n            ensure_ascii=True,separators=(\",\",\":\")),flush=True)\n",new="        exit_code=_R188_EMIT_SUMMARY(args.out,summary,exit_code)\n",count=1)
]


def load_published_endpoint_module():
    """Every public source replacement is exact, unique and openly identified."""
    global R
    source_path=HERE/BASE_NAME
    raw=source_path.read_bytes()
    require(len(raw)==BASE_BYTES and sha(raw)==BASE_SHA,
        "The final published positive-sine84af source is the sole endpoint baseline")
    design_path=HERE.parent/"notes"/DESIGN_NAME
    design=design_path.read_bytes()
    require(len(design)==DESIGN_BYTES and sha(design)==DESIGN_SHA,
        "The selected actual98 request175 design remains bound as published")
    parent_path=HERE/PARENT_CONSUMER_NAME
    parent=parent_path.read_bytes()
    require(len(parent)==PARENT_CONSUMER_BYTES and sha(parent)==PARENT_CONSUMER_SHA,
        "The original175 source remains an immutable provenance baseline, not executed")
    proof_path=HERE.parent/"results"/INCLUSION_PROOF_NAME
    proof=proof_path.read_bytes()
    require(len(proof)==INCLUSION_PROOF_BYTES and sha(proof)==INCLUSION_PROOF_SHA,
        "Bind the published same-path inclusion statement without adding a numerical gate")
    text=raw.decode("utf-8")
    receipts=[]
    for item in SOURCE_REPLACEMENTS:
        actual=text.count(item["old"])
        require(actual==item["count"],
            "Explicit unique source anchor: "+item["label"])
        text=text.replace(item["old"],item["new"],item["count"])
        receipts.append(dict(label=item["label"],required_count=item["count"],
            actual_count=actual,old_utf8_sha256=sha(item["old"].encode("utf-8")),
            new_utf8_sha256=sha(item["new"].encode("utf-8"))))
    generated=text.encode("utf-8")
    # No file in the public source checkout is changed. __file__ names this
    # actual independent producer, while compile's filename names the private
    # generated orchestration for a truthful traceback.
    module=types.ModuleType("_request188_published84af_endpoint")
    module.__file__=str(Path(__file__).resolve())
    module.__package__=None
    module.__dict__.update(
        _R188_INITIAL=initial_query_result,_R188_EXTENSION=query_extension,
        _R188_FINALIZE=finalize_query,_R188_COMPACT=compact_query,
        _R188_EMIT_SUMMARY=emit_summary,_R188_DEFER_SIGNAL=defer_external_stop,
        _R188_ADAPTATION=dict(
            schema="request188-explicit-published84af-source-adaptation-v1",
            published_source=dict(file=BASE_NAME,bytes=len(raw),sha256=sha(raw)),
            independent_source=dict(file=Path(__file__).name,
                bytes=Path(__file__).stat().st_size,sha256=sha(Path(__file__).read_bytes())),
            published_selected_design=dict(file=DESIGN_NAME,bytes=len(design),sha256=sha(design)),
            original175_parent_source=dict(file=PARENT_CONSUMER_NAME,
                bytes=len(parent),sha256=sha(parent),not_executed=True),
            same_path_inclusion_proof=dict(file=INCLUSION_PROOF_NAME,
                bytes=len(proof),sha256=sha(proof)),
            generated_private_module=dict(bytes=len(generated),sha256=sha(generated),
                only_in_memory_not_public_source_mutation=True),
            complete_explicit_replacements=receipts,
            all_original_numerical_function_bodies_unchanged=True,
            original170_main_scientific_order_retained_before_new_query_phase=True,
            old_negative_sine_draft_not_used=True))
    sys.modules[module.__name__]=module
    exec(compile(text,str(HERE/("_generated188_"+BASE_NAME)),"exec"),module.__dict__)
    R=module
    return module


def main():
    require(os.environ.get("GITHUB_ACTIONS")=="true" and
        os.environ.get("GITHUB_REPOSITORY")==REPOSITORY,
        "Scientific imports and all new arithmetic run only in public Actions")
    return load_published_endpoint_module().main()


if __name__=="__main__":
    raise SystemExit(main())
