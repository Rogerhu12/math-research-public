#!/usr/bin/env python3
"""R153: one D0 raw-rational probe reusing the published 42-by-42 pivot.

No old response is reconstructed or individually evaluated.  Evaluate the
new D0, solve against the old modular pivot, and evaluate one raw original
linear combination.  A nonzero residue certifies nonmembership over Q;
modular zero never certifies membership.
"""
from __future__ import annotations
import argparse
import copy
from fractions import Fraction as F
import gzip
import json
import os
from pathlib import Path
import resource
import time

import literature_h_axis_sharp_coefficient as axis

layer=axis.layer
first,static,old=axis.first,axis.static,axis.old
colored,exact,formal=axis.colored,axis.exact,axis.formal
poly,dual=layer.poly,layer.dual
canonical,sha=axis.canonical,axis.sha
MODES=axis.MODES
SCHEMA="visible-flex-D0-fixed-pivot-original-residual-v1"
REPOSITORY=axis.REPOSITORY
TOPIC=axis.TOPIC
PRIME=2147483647
D0_RUN="43657526246"
D0_COMMIT="0d5df1843fd829e7c09b17afdead930ec4395f34"
D0_DRIVER={"filename":"literature_h_axis_sharp_coefficient.py","bytes":31222,
    "sha256":"7f4ee057a16a620e089102ea9c84fccafd922306e8febf8b73391b478e4a4a0b"}
D0_MAIN={"bytes":17542,"sha256":"e0007757b7d113a34b5c2ec594a607d380855f5652042f67fe3f32c1c81397f0"}
D0_RECEIPT={"bytes":36161,"sha256":"1d635cdbe80251339d1157cee579c6838cad8975310a80959ef92b171f2458ea"}
D0_EXPORT={"filename":"h-axis-sharp-original-expressions.json.gz","stored_bytes":14497,
    "stored_sha256":"ecd9edf2d461f6d4f6b9355e17e210ad435b20c53bc16baeda412258b8b3fabd",
    "raw_bytes":80444,"raw_sha256":"2d0433a628b22f223a0f8700cebad02e70305699ff39a65e075de81dad5ceed0"}
D0_HASH={"-4":"1236f94a788454870d655dda499714eacccfee730cba582e22fb2c0b4d892f7f",
         "-2":"ce6e1dd221080cd0a4961f2cf81b9a1be1f8a276d587b0cd34e0dd884fd83c5f"}
J_COMPLETE={"filename":"acceleration-layer-mixed-complete-report.json.gz","stored_bytes":43071,
    "stored_sha256":"af242f353bfb3e038615a8bc1f9d28752b75233be58f7f1a8ad8f89713110891",
    "raw_bytes":175927,"raw_sha256":"a106c8a0162ef7c51ca8ad03546ef2d7607f2dabe34a00169acad97c9ed9c9b4"}
OLD_PIVOT_SHA="f0965e518249763e99e4d9770831bf147db401be9fc4bfe73c389e6cb7f307e5"
OLD_PIVOT_DETERMINANT=602105349
OLD_LABELS_SHA="6873c1135af382e8edd49832070ab4e31ce51fa465a921f39005865f87d21143"


def source_identity():
    previous=axis.source_identity()
    if previous.get("driver")!=D0_DRIVER:
        raise ValueError("the completed D0 producer is frozen")
    return {"driver":static.identity(__file__),"published_D0_and_original_interfaces":previous}


def bind_response_arguments(args):
    args.response_order=3;args.response_run=axis.RESPONSE_RUN;args.response_commit=axis.RESPONSE_COMMIT
    args.response_lane="g_translation_successor";args.response_report_sha256=axis.RESPONSE_MAIN_SHA
    args.response_publication_sha256=axis.RESPONSE_RECEIPT_SHA


def expected_labels(points=24):
    return [{"t":str(F(j,points+1)),"xi":str(2+F(j,points+1)),
             "mode":m,"component":part}
            for j in range(1,points+1) for m in MODES
            for part in ("real","imaginary")]


def scalar_value(modes,label):
    if label["mode"] not in MODES or label["component"] not in ("real","imaginary"):
        raise ValueError("unknown real two-mode query")
    t=F(label["t"])
    if F(label["xi"])!=2+t or not 0<t<1:
        raise ValueError("changed physical query or support")
    return modes[label["mode"]].value(t)[0 if label["component"]=="real" else 1]


def check_square_payload(matrix,rows,labels,prime,expected_size,expected_sha):
    if (len(matrix)!=expected_size or any(len(row)!=expected_size for row in matrix)
        or len(rows)!=expected_size or len(set(rows))!=len(rows)
        or any(not isinstance(i,int) or not 0<=i<len(labels) for i in rows)
        or any(not isinstance(x,int) or not 0<=x<prime for row in matrix for x in row)
        or sha(canonical(matrix))!=expected_sha):
        raise ValueError("the saved original square pivot is incomplete or changed")
    return [labels[i] for i in rows]


def load_D0(args,ring,report):
    main=layer.read_bound_json(args.D0_report,D0_MAIN)
    publication=layer.read_bound_json(args.D0_publication,D0_RECEIPT)
    metadata=main.get("portable_axis_expression_export") or {}
    if (main.get("schema")!=axis.SCHEMA or main.get("completion")!="complete"
        or main.get("github_repository")!=REPOSITORY
        or str(main.get("github_run_id"))!=D0_RUN or main.get("github_sha")!=D0_COMMIT
        or main.get("source_hashes")!=axis.source_identity()
        or main.get("checkpoint",{}).get("outcome")!="undecided_sound_remainder"
        or main.get("axis_target",{}).get("original_D0_sha256")!=D0_HASH
        or main.get("axis_target",{}).get("ungraded_weights")!={"-4":[-2],"-2":[-2]}
        or main.get("consumed_control_summary",{}).get("true_dimension")!=42
        or main.get("consumed_control_summary",{}).get("original_column_labels_sha256")!=OLD_LABELS_SHA
        or any(metadata.get(k)!=v for k,v in D0_EXPORT.items())):
        raise ValueError("the completed, unchanged two-mode D0 target is required")
    binding=layer.check_publication(publication,run=D0_RUN,commit=D0_COMMIT,lane="h_axis_sharp",
        driver=D0_DRIVER,main_name=args.D0_report.name,main_info=D0_MAIN,export_info=metadata)
    data=layer.read_bound_export(args.D0_export,metadata)
    if (data.get("schema")!=axis.SCHEMA+"-original-expressions"
        or data.get("content_scope")!="one-complete-h-axis-D0-K0-and-two-unreduced-N2-contractions"
        or data.get("source_hashes")!=main["source_hashes"]
        or str(data.get("github_run_id"))!=D0_RUN or data.get("github_sha")!=D0_COMMIT
        or data.get("axis_target")!=main["axis_target"]):
        raise ValueError("the original D0 portable scope changed")
    names={m:f"D0_{m}" for m in MODES}
    roots=axis.subset_decode(ring,data,names.values())
    modes={m:roots[names[m]] for m in MODES}
    if {str(m):ring.digest(x) for m,x in modes.items()}!=D0_HASH:
        raise ValueError("original D0 root hashes changed")
    report["D0_input"]={"main":D0_MAIN,"receipt":D0_RECEIPT,"publication":binding,
        "complete_export":metadata,"original_mode_sha256":D0_HASH,
        "N2_or_velocity_target_recomputed":False,"K0_evaluated":False}
    return modes


def load_pivot(args,report):
    main=layer.read_bound_json(args.J_report,axis.J_MAIN)
    publication=layer.read_bound_json(args.J_publication,axis.J_RECEIPT)
    metadata=main.get("complete_report_file") or {}
    if any(metadata.get(k)!=v for k,v in J_COMPLETE.items()):
        raise ValueError("the completed R136 full report is required")
    binding=layer.check_publication(publication,run=axis.J_RUN,commit=axis.J_COMMIT,
        lane="acceleration_layer_mixed",driver=axis.LAYER_DRIVER,
        main_name=args.J_report.name,main_info=axis.J_MAIN,export_info=metadata)
    data=layer.read_bound_export(args.J_complete_report,metadata)
    if (data.get("schema")!=layer.SCHEMA or data.get("completion")!="complete"
        or data.get("github_sha")!=axis.J_COMMIT
        or str(data.get("github_run_id"))!=axis.J_RUN
        or data.get("source_hashes")!=layer.source_identity()
        or data.get("checkpoint",{}).get("original_target_sha256")!=axis.J_HASH):
        raise ValueError("the old pivot full report changed identity")
    evaluation=data.get("new_original_evaluation") or {}
    witness=evaluation.get("dual_certificate") or {}
    compact=main.get("checkpoint",{}).get("dual_certificate") or {}
    labels=evaluation.get("all_evaluation_labels")
    matrix=witness.get("modular_augmented_matrix")
    rows=witness.get("selected_augmented_rows")
    if (labels!=expected_labels() or not evaluation.get("original_right_integrals_used")
        or evaluation.get("word_representatives_evaluated")
        or not evaluation.get("same_fixed_pair_for_all_controls_and_modes")
        or witness.get("control_columns")!=41 or witness.get("modular_control_rank")!=41
        or not witness.get("rational_nonmembership_certified")
        or witness.get("modular_augmented_determinant")!=OLD_PIVOT_DETERMINANT
        or rows!=compact.get("selected_augmented_rows")
        or compact.get("original_modular_augmented_matrix")!={"columns":42,"rows":42,
            "sha256":OLD_PIVOT_SHA,"full_matrix_in_complete_report":True}
        or data.get("coefficient_checkpoint",{}).get("prime")!=PRIME
        or not data.get("coefficient_checkpoint",{}).get("all_encountered_rational_denominators_invertible")):
        raise ValueError("the published rationally nonsingular 42-column pivot is required")
    selected=check_square_payload(matrix,rows,labels,PRIME,42,OLD_PIVOT_SHA)
    report["fixed_pivot_input"]={"publication":binding,"complete_report":metadata,
        "old_original_matrix_rows_available":42,"old_query_labels_available":len(labels),
        "missing_old_query_rows":len(labels)-42,
        "old_all_query_matrix_values_present":False,
        "selected_old_global_row_indices":rows,"selected_evaluation_labels":selected,
        "matrix_sha256":OLD_PIVOT_SHA,"matrix_mod_p":matrix,
        "determinant_mod_p_from_published_proof":OLD_PIVOT_DETERMINANT,
        "fixed_profiles":evaluation["fixed_profiles"],
        "old_denominator_certificate":data["coefficient_checkpoint"],
        "old_separation_or_determinant_recomputed":False,
        "meaning_of_old_augmented_column":"J is now comparison column 41"}
    return matrix,selected,evaluation["fixed_profiles"],data["response_input"]


def build_combination(ring,controls,coefficients):
    if len(controls)!=len(coefficients):
        raise ValueError("coefficient count differs from original columns")
    answer={m:ring.number(0) for m in MODES}
    for coefficient,modes in zip(coefficients,controls):
        if coefficient:
            for m in MODES:
                answer[m]+=int(coefficient)*modes[m]
    return answer


def append_published_J(controls,labels,J):
    # layer exposes its label list in the original publication record too.
    # Appending in place would silently change that already-bound 41-column
    # record before the full old pivot comparison.
    return [*controls,J],[*labels,{"role":"published_J","candidate_id":0,
                                  "original_mode_sha256":axis.J_HASH}]


def solve_new_coordinates(matrix,values,prime):
    coefficients=poly.solve(matrix,values,prime)
    if any((sum(a*b for a,b in zip(row,coefficients))-value)%prime
           for row,value in zip(matrix,values)):
        raise AssertionError("the old-pivot new-column solve failed")
    return coefficients


def nonzero_polynomial_query(modes):
    """At most degree+1 distinct rational points for one nonzero component."""
    for m in MODES:
        value=modes[m]
        for part,component in (("real",0),("imaginary",1)):
            coefficients=[pair[component] for pair in value.coefficients]
            while coefficients and not coefficients[-1]:
                coefficients.pop()
            if not coefficients:
                continue
            degree=len(coefficients)-1
            if degree+2>=value.context.prime:
                raise ValueError("finite distinct query grid would meet the characteristic")
            for j in range(1,degree+2):
                t=F(j,degree+2)
                residue=value.value(t)[component]
                if residue:
                    return {"label":{"t":str(t),"xi":str(2+t),"mode":m,"component":part},
                        "residue":residue,"component_degree":degree,
                        "distinct_query_bound":degree+1,"queries_tried":j,
                        "grid":"j/(component_degree+2), 1<=j<=component_degree+1"}
            raise AssertionError("a nonzero polynomial vanished at more than its degree")
    return None


def save_new_roots(args,ring,target,combination,residual,coefficients,report):
    path=args.output.with_name(args.output.stem+"-original-residual.json.gz")
    info={"filename":path.name,"persisted":False,"supplemental_not_a_math_gate":True}
    report["portable_new_residual_export"]=info
    names={}
    for m in MODES:
        names[f"D0_{m}"]=target[m]
        names[f"old_modular_lift_combination_{m}"]=combination[m]
        names[f"residual_with_integer_lifts_{m}"]=residual[m]
    data={"schema":SCHEMA+"-original-expressions",
        "content_scope":"D0-and-one-old-root-combination-with-explicit-modular-integer-lifts",
        "github_repository":report["github_repository"],"github_run_id":report["github_run_id"],
        "github_sha":report["github_sha"],"source_hashes":report["source_hashes"],
        "prime":PRIME,"integer_lift_coefficients":coefficients,
        "coefficients_are_not_claimed_to_be_rational_pivot_coordinates":True,
        "original_control_labels":report["comparison_space"]["original_column_labels"],
        **old.serialize_expressions(ring,names)}
    raw=canonical(data);packed=gzip.compress(raw,mtime=0)
    info.update({"stored_bytes":len(packed),"stored_sha256":sha(packed),
        "raw_bytes":len(raw),"raw_sha256":sha(raw),"root_count":len(names),
        "content_scope":data["content_scope"]})
    if len(packed)>args.max_export_bytes or len(raw)>layer.MAX_RAW_INPUT:
        info["reason"]="supplemental ceiling; existing mathematical status remains valid"
        return
    path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(packed)
    info["persisted"]=True


def study(args,report,started):
    limits=exact.Limits(args.max_seconds,500000,100000,120000,500000,args.memory_mib,8192)
    ring=colored.ColoredRing(limits)
    report["phase"]="read_only_completed_D0_and_existing_original_comparison_block"
    target=load_D0(args,ring,report)
    J,j_response=axis.load_J(args,ring,report)
    controls,labels=layer.load_response_block(args,ring,report)
    if (len(controls)!=41 or report["response_input"]["weight"]!=-2
        or j_response["retained_original_control_labels"]!=report["response_input"]["retained_original_control_labels"]
        or j_response["publication"]!=report["response_input"]["publication"]):
        raise ValueError("old 41 original columns differ from the completed J certificate")
    controls,labels=append_published_J(controls,labels,J)
    if sha(canonical(labels))!=OLD_LABELS_SHA:
        raise ValueError("the 42-column order differs from D0's completed comparison")
    matrix,pivot_queries,profiles,pivot_response=load_pivot(args,report)
    if pivot_response!=report["response_input"]:
        raise ValueError("the complete old matrix and loaded original columns differ")
    report["comparison_space"]={"true_dimension":42,"R8_weight_minus_two":40,"G_orbit":1,"J":1,
        "original_column_labels":labels,"same_real_coefficients_for_both_modes":True,
        "old_upper_bound_and_independence_consumed_not_recomputed":True,
        "original_labels_sha256":OLD_LABELS_SHA,
        "individual_old_column_evaluations":0,"old_response_compositions":0}
    report["input_regularity"]=dual.reachable_jet_bound(ring,list(target.values())+
        [value for modes in controls for value in modes.values()])
    if report["input_regularity"]["maximum_input_jet"]>7:
        raise ValueError("the old C7 fixed pair does not meet this new target's jet bound")
    remaining=args.max_seconds-(time.monotonic()-started)
    if remaining<=0:
        raise poly.PolynomialBudgetExceeded("time before the new raw target")
    context=poly.PolynomialContext(PRIME,2,3,seconds=remaining,max_degree=args.max_degree,
        memory_mib=args.memory_mib,max_operations=args.max_operations)
    try:
        _,_,actual_profiles=dual.fixed_profiles(context,8)
        if actual_profiles!=profiles:
            raise ValueError("the old rational profile pair or right anchor changed")
        evaluator=poly.RawExpressionEvaluator(ring.p,context,context.colors)
        report["phase"]="only_new_D0_raw_polynomial_and_old_pivot_solve"
        evaluated={m:evaluator.expression(target[m]) for m in MODES}
        values=[scalar_value(evaluated,label) for label in pivot_queries]
        coefficients=solve_new_coordinates(matrix,values,PRIME)
        report["new_pivot_solve"]={"D0_pivot_values_mod_p":values,
            "modular_candidate_coordinates":coefficients,"integer_lift_interval":[0,PRIME-1],
            "true_Q_coordinates_not_computed":True,
            "matrix_times_candidate_equals_new_column":True,
            "new_target_mode_polynomials":{str(m):{"sha256":p.digest(),
                "degree":len(p.coefficients)-1} for m,p in evaluated.items()}}
        combination=build_combination(ring,controls,coefficients)
        residual={m:target[m]-combination[m] for m in MODES}
        report["phase"]="one_original_old_root_linear_combination_evaluation"
        # One combined polynomial per mode. Never evaluate each old control.
        combined_values={m:evaluator.expression(combination[m]) for m in MODES}
        residual_values={m:evaluated[m]-combined_values[m] for m in MODES}
        pivot_residues=[scalar_value(residual_values,label) for label in pivot_queries]
        if any(pivot_residues):
            raise AssertionError("combined old roots do not match their saved pivot values")
        report["combined_original_check"]={
            "all_saved_pivot_residuals_zero":True,"pivot_residues":pivot_residues,
            "old_column_polynomials_individually_evaluated":False,
            "word_normal_forms_used":False,"response_or_N2_reconstructed":False,
            "combination_original_mode_sha256":{str(m):ring.digest(x) for m,x in combination.items()},
            "residual_original_mode_sha256":{str(m):ring.digest(x) for m,x in residual.items()},
            "combined_mode_polynomials":{str(m):{"sha256":p.digest(),
                "degree":len(p.coefficients)-1} for m,p in combined_values.items()},
            "residual_modular_polynomial_coefficients":{str(m):p.coefficients
                for m,p in residual_values.items()},
            "residual_mode_polynomials":{str(m):{"sha256":p.digest(),
                "degree":len(p.coefficients)-1} for m,p in residual_values.items()}}
        query=nonzero_polynomial_query(residual_values)
        if query is None:
            report["checkpoint"]={"outcome":"undecided_modular_fixed_pair_residual_zero",
                "rational_nonmembership_certified":False,"original_membership_certified":False,
                "a_modular_zero_is_not_a_rational_identity":True,
                "other_profiles_or_coefficients_tested":False}
        else:
            label=query["label"]
            if label in pivot_queries:
                raise AssertionError("the selected nonzero row is a saved zero pivot row")
            residue=query["residue"]
            augmented=OLD_PIVOT_DETERMINANT*residue%PRIME
            if not augmented:
                raise AssertionError("unit old pivot times nonzero Schur residue vanished")
            report["checkpoint"]={"outcome":"D0_original_nonmembership_certified",
                "rational_nonmembership_certified":True,"original_membership_certified":False,
                "comparison_space_true_dimension":42,
                "same_fixed_pair_for_pivot_and_new_query":True,
                "old_pivot_determinant_mod_p":OLD_PIVOT_DETERMINANT,
                "new_augmented_order":43,
                "new_augmented_determinant_mod_p_by_Schur_identity":augmented,
                "functional_D0_value_mod_p":residue,"extra_query":query,
                "D0_at_extra_query_mod_p":scalar_value(evaluated,label),
                "combined_old_roots_at_extra_query_mod_p":scalar_value(combined_values,label),
                "functional_over_Q":"ev_extra - row_extra(U) * inverse(A_Q) * ev_pivot",
                "why_modular_lifts_suffice":"A_Q is a unit over Z_(p), so its unique Q coordinates reduce to c; ev(D0-sum(lift(c_j)U_j)) mod p is Lambda_Q(D0) mod p",
                "all_42_original_controls_annihilated_over_Q_by_definition":True,
                "modular_coordinates_are_not_reported_as_Q_coefficients":True,
                "true_whole_function_span_upper_bound_source":"R131 and R136",
                "outside_R8_plus_G_orbit_plus_J_at_weight_minus_two":True,
                "signed_cost_or_full_ruling_paid":False}
        report["phase"]="save_only_new_original_residual_and_complete_proof"
        save_new_roots(args,ring,target,combination,residual,coefficients,report)
        report["completion"]="complete";report["phase"]="complete"
    finally:
        report["coefficient_checkpoint"]=context.coefficient_report()


def small_toy():
    checks={}
    artificial_args=argparse.Namespace()
    bind_response_arguments(artificial_args)
    if (artificial_args.response_report_sha256!=axis.RESPONSE_MAIN_SHA
        or artificial_args.response_publication_sha256!=axis.RESPONSE_RECEIPT_SHA
        or artificial_args.response_order!=3):
        raise AssertionError("the published response-reader argument interface changed")
    checks["existing_response_reader_argument_names_bound"]=True
    old_controls=["U0","U1"];old_labels=[{"id":0},{"id":1}]
    old_report={"retained_original_control_labels":old_labels}
    extended_controls,extended_labels=append_published_J(old_controls,old_labels,"J")
    if (old_controls!=["U0","U1"] or len(old_report["retained_original_control_labels"])!=2
        or len(extended_controls)!=3 or len(extended_labels)!=3
        or extended_labels is old_labels):
        raise AssertionError("adding J changed the frozen original publication label list")
    checks["append_J_preserves_shared_original_publication_labels"]=True
    prime=103
    matrix=[[2,1],[1,3]]
    values=[1,4]
    cs=solve_new_coordinates(matrix,values,prime)
    checks["new_column_solve_on_fixed_artificial_pivot"]=cs==[41,22]
    if not checks["new_column_solve_on_fixed_artificial_pivot"]:
        raise AssertionError("artificial fixed-pivot solution")
    exact_cs=[F(-1,5),F(7,5)]
    if any((a.numerator*pow(a.denominator,prime-2,prime))%prime!=b
           for a,b in zip(exact_cs,cs)):
        raise AssertionError("rational coordinate reduction")
    checks["integer_lifts_distinguished_from_Q_coordinates"]=cs!=exact_cs
    extra=[3,4];new_value=7
    residue=(new_value-sum(x*y for x,y in zip(extra,cs)))%prime
    augmented=poly.determinant([matrix[0]+[values[0]],matrix[1]+[values[1]],extra+[new_value]],prime)
    if augmented!=poly.determinant(matrix,prime)*residue%prime or not residue:
        raise AssertionError("artificial Schur complement")
    checks["Schur_nonzero_with_single_combined_extra_row"]=True
    labels=[{"t":"1/4","xi":"9/4","mode":-4,"component":"real"},
            {"t":"1/2","xi":"5/2","mode":-2,"component":"imaginary"}]
    check_square_payload(matrix,[0,1],labels,prime,2,sha(canonical(matrix)))
    checks["complete_pivot_shape_and_hash_bound"]=True
    try:
        check_square_payload(matrix,[0,0],labels,prime,2,sha(canonical(matrix)))
    except ValueError:
        checks["duplicate_pivot_query_rejected"]=True
    else:
        raise AssertionError("duplicate pivot accepted")
    try:
        check_square_payload(matrix,[0,1],labels,prime,2,"0"*64)
    except ValueError:
        checks["changed_pivot_values_rejected"]=True
    else:
        raise AssertionError("wrong matrix hash")
    ctx=poly.PolynomialContext(prime,2,3,seconds=10,max_degree=16,memory_mib=256,max_operations=10000)
    t=ctx.variable()
    modes={-4:ctx.number(0),-2:ctx.number((0,1))*t*(1-t)*(t-F(1,2))}
    query=nonzero_polynomial_query(modes)
    if not query or query["label"]["mode"]!=-2 or query["label"]["component"]!="imaginary":
        raise AssertionError("imaginary component query")
    checks["finite_degree_grid_finds_nonzero_imaginary_mode"]=True
    if nonzero_polynomial_query({m:ctx.number(0) for m in MODES}) is not None:
        raise AssertionError("modular zero promoted to nonzero")
    checks["modular_zero_retains_undecided_gate"]=True
    try:
        scalar_value(modes,{"t":"1/3","xi":"8/3","mode":-2,"component":"imaginary"})
    except ValueError:
        checks["changed_xi_t_correspondence_rejected"]=True
    else:
        raise AssertionError("wrong xi accepted")
    limits=exact.Limits(20,10000,1000,1000,10000,256,8192)
    ring=colored.ColoredRing(limits)
    q,qb=ring.color("q"),ring.color("qbar")
    controls=[{-4:q*q*q*q,-2:q*qb*qb*qb},
              {-4:(q*q).I()*q*qb,-2:(q*qb).I()*q*q}]
    combination=build_combination(ring,controls,[5,7])
    if any((combination[m]-5*controls[0][m]-7*controls[1][m]).terms for m in MODES):
        raise AssertionError("original linear combination")
    checks["same_real_coefficients_for_two_artificial_modes"]=True
    context=poly.PolynomialContext(prime,2,3,seconds=10,max_degree=32,memory_mib=256,max_operations=10000)
    x=context.variable();context.colors={"q":x+context.number((0,1)),"qbar":x-context.number((0,1))}
    evaluator=poly.RawExpressionEvaluator(ring.p,context,context.colors)
    integrated=evaluator.expression((q*q).I())
    if integrated.value(F(1))!=(0,0):
        raise AssertionError("right anchor")
    checks["raw_right_primitive_has_actual_common_zero_anchor"]=True
    for m in MODES:
        left=evaluator.expression(combination[m])
        right=5*evaluator.expression(controls[0][m])+7*evaluator.expression(controls[1][m])
        if left.coefficients!=right.coefficients:
            raise AssertionError("combined raw evaluation is not linear")
    checks["one_combined_evaluation_matches_artificial_linear_identity"]=True
    portable=old.serialize_expressions(ring,{f"comb_{m}":x for m,x in combination.items()})
    decoded=old.decode_expressions(ring,portable)
    if any((decoded[f"comb_{m}"]-combination[m]).terms for m in MODES):
        raise AssertionError("portable residual")
    checks["portable_two_mode_original_residual_round_trip"]=True
    return {"checks":checks,"all_passed":all(checks.values()),
        "published_reports_or_roots_read":False,"research_profile_evaluated":False,
        "D0_or_research_residual_evaluated":False,"old_research_column_evaluated":False}


def publish(args,report):
    full_raw=canonical(report)
    full_path=args.output.with_name(args.output.stem+"-complete-report.json.gz")
    full_info={"filename":full_path.name,"persisted":False,"raw_bytes":len(full_raw),
        "raw_sha256":sha(full_raw)}
    packed=gzip.compress(full_raw,mtime=0)
    full_info.update({"stored_bytes":len(packed),"stored_sha256":sha(packed)})
    if len(packed)<=args.max_full_report_bytes:
        full_path.parent.mkdir(parents=True,exist_ok=True);full_path.write_bytes(packed)
        full_info["persisted"]=True
    else:
        full_info["reason"]="complete-report supplemental ceiling"
    compact=copy.deepcopy(report)
    if "fixed_pivot_input" in compact:
        compact["fixed_pivot_input"].pop("matrix_mod_p",None)
        compact["fixed_pivot_input"]["old_matrix_in_complete_report"]=full_info["persisted"]
    if "comparison_space" in compact:
        compact["comparison_space"].pop("original_column_labels",None)
    if "combined_original_check" in compact:
        coefficients=compact["combined_original_check"].pop("residual_modular_polynomial_coefficients",None)
        if coefficients is not None:
            compact["combined_original_check"]["residual_coefficients_in_complete_report"]=full_info["persisted"]
            compact["combined_original_check"]["residual_coefficients_sha256"]=sha(canonical(coefficients))
    for field in ("response_input","J_input"):
        if field in compact:
            compact[field].pop("retained_original_control_labels",None)
    compact["complete_report_file"]=full_info
    raw=canonical(compact)
    if len(raw)>args.max_main_bytes:
        keep=("schema","github_repository","github_run_id","github_sha","source_hashes","completion","phase",
              "error","elapsed_seconds","peak_rss_mib","checkpoint","D0_input","portable_new_residual_export",
              "coefficient_checkpoint","complete_report_file","limits","toy")
        compact={k:compact[k] for k in keep if k in compact}
        compact["details_in_complete_report"]=full_info["persisted"]
        raw=canonical(compact)
    if len(raw)>args.max_main_bytes:
        raise ValueError("small main report unexpectedly exceeds the fixed ceiling")
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_bytes(raw)
    return {"filename":args.output.name,"bytes":len(raw),"sha256":sha(raw),
        "completion":report["completion"],"full_report":full_info}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only",action="store_true")
    parser.add_argument("--output",type=Path,required=True)
    ddir=TOPIC/"notes"/("actions-"+D0_RUN+"-1-h_axis_sharp")
    jdir=TOPIC/"notes"/("actions-"+axis.J_RUN+"-1-acceleration_layer_mixed")
    rdir=TOPIC/"notes"/("actions-"+axis.RESPONSE_RUN+"-1-g_translation_successor")
    parser.add_argument("--D0-report",type=Path,default=ddir/"h-axis-sharp.json")
    parser.add_argument("--D0-publication",type=Path,default=ddir/"receipt.json")
    parser.add_argument("--D0-export",type=Path,default=ddir/D0_EXPORT["filename"])
    parser.add_argument("--J-report",type=Path,default=jdir/"acceleration-layer-mixed.json")
    parser.add_argument("--J-publication",type=Path,default=jdir/"receipt.json")
    parser.add_argument("--J-export",type=Path,default=jdir/axis.J_EXPORT["filename"])
    parser.add_argument("--J-complete-report",type=Path,default=jdir/J_COMPLETE["filename"])
    parser.add_argument("--response-report",type=Path,default=rdir/"G-third-translation.json")
    parser.add_argument("--response-publication",type=Path,default=rdir/"receipt.json")
    parser.add_argument("--response-export",type=Path,default=rdir/"G-third-translation-original-expressions.json.gz")
    parser.add_argument("--max-seconds",type=float,default=180)
    parser.add_argument("--memory-mib",type=int,default=1024)
    parser.add_argument("--max-degree",type=int,default=256)
    parser.add_argument("--max-operations",type=int,default=20000000)
    parser.add_argument("--max-main-bytes",type=int,default=90000)
    parser.add_argument("--max-full-report-bytes",type=int,default=2000000)
    parser.add_argument("--max-export-bytes",type=int,default=1500000)
    args=parser.parse_args()
    bind_response_arguments(args)
    if min(args.max_seconds,args.memory_mib,args.max_degree,args.max_operations,
           args.max_main_bytes,args.max_full_report_bytes,args.max_export_bytes)<=0:
        parser.error("positive finite budgets required")
    if (args.max_main_bytes>=100000
        or args.max_main_bytes+args.max_full_report_bytes+args.max_export_bytes>static.TOTAL_BYTES):
        parser.error("small main and total published byte ceiling required")
    if not args.toy_only and (os.environ.get("GITHUB_ACTIONS")!="true"
                            or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY):
        parser.error("the real D0 profile evaluation runs only in the named public repository Actions")
    started=time.monotonic()
    report={"schema":SCHEMA,"github_repository":os.environ.get("GITHUB_REPOSITORY"),
        "github_run_id":os.environ.get("GITHUB_RUN_ID"),"github_sha":os.environ.get("GITHUB_SHA"),
        "scope":"only one complete D0 and one old-root combination; no old column evaluation",
        "limits":{"seconds":args.max_seconds,"memory_soft_polling_mib":args.memory_mib,
            "max_degree":args.max_degree,"max_operations":args.max_operations,
            "main_bytes":args.max_main_bytes,"full_report_bytes":args.max_full_report_bytes,
            "new_export_bytes":args.max_export_bytes},"completion":"not_started","phase":"source_binding"}
    code=0
    try:
        report["source_hashes"]=source_identity()
        if args.toy_only:
            report["phase"]="small_artificial_fixed_pivot_and_original_linear_combination"
            report["toy"]=small_toy();report["completion"]="toy_passed"
        else:
            study(args,report,started)
    except (formal.CompilationBudgetExceeded,poly.PolynomialBudgetExceeded) as error:
        report["completion"]="resource_limit";report["error"]=str(error);code=2
    except Exception as error:
        report["completion"]="implementation_check_failed"
        report["error"]={"type":type(error).__name__,"message":str(error)};code=1
    report["elapsed_seconds"]=time.monotonic()-started
    report["peak_rss_mib"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    info=publish(args,report)
    print(json.dumps({"output":str(args.output),**info}),flush=True)
    return code


if __name__=="__main__":
    raise SystemExit(main())

