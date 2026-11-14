#!/usr/bin/env python3
"""One true translation successor of G modulo the complete R8 response space.

The default task is order three.  A later order requires an explicitly rebound
immediately preceding, published, original-expression nonmembership certificate.
Only the requested new weight block is compiled/evaluated.  Earlier response
columns and separations are consumed, not repeated.  An original membership
identity ends the translation chain; a nonzero word remainder is not a proof.
"""
from __future__ import annotations

import argparse
import copy
import gzip
import tempfile
import json
import os
from pathlib import Path
import resource
import time
from fractions import Fraction as F

import literature_G_first_translation as first

seed=first.seed
static=first.static
dual=first.dual
poly=first.poly
colored=first.colored
exact=first.exact
formal=first.formal
blocks=first.blocks
MODES=first.MODES
canonical=first.canonical
sha=first.sha
SCHEMA="visible-flex-G-translation-successor-original-v1"
SECOND_SCHEMA="visible-flex-G-second-translation-original-v1"
FIRST_DRIVER_BYTES=26885
FIRST_DRIVER_SHA="331fea2c1aef154c4d5866e4708f067c555f9fb61f02a11ee32a7f44d25f01f5"
DEFAULT_PREVIOUS={
    "order":2,
    "run":"43651413950",
    "commit":"ba3a19be3ef851fbeb29ff491618e18622064f12",
    "lane":"g_second_translation",
    "main_bytes":41062,
    "main_sha256":"2828278fa8f881fbb53a2c6518a63d3067521c9860f07652c7e0080696cc5723",
    "publication_bytes":33699,
    "publication_sha256":"3abf0890dd897cfb2d4b1fa6ec2daef7c3f26a230613a48827cf7e2a8018ac68",
    "driver_filename":"literature_G_second_translation.py",
    "driver_bytes":24396,
    "driver_sha256":"3c37aeae4b39ecf68932a069878b41d890afbe2fd4ee9d8675195edc4e5d6bc1",
    "target_sha256":{
        "-4":"2f4985b03d739f86dfb97a6aa688afcb4c52a21a8c632ab3950cd36900d81c8e",
        "-2":"c40b69eef9041cf7c381c95a1d6061910d9cbc99c82f541db576ff6c4f69abd3"},
}
DEFAULT_PREVIOUS_DIR=Path(first.__file__).resolve().parents[1]/"notes"/(
    "actions-"+DEFAULT_PREVIOUS["run"]+"-1-"+DEFAULT_PREVIOUS["lane"])

def source_identity():
    value=first.source_identity()
    if value["driver"]!={"filename":"literature_G_first_translation.py",
                         "bytes":FIRST_DRIVER_BYTES,"sha256":FIRST_DRIVER_SHA}:
        raise ValueError("explicitly rebind the frozen original-expression translation helpers")
    value["frozen_first_translation_helpers"]=value.pop("driver")
    value["driver"]=static.identity(__file__)
    return value

def previous_spec(args):
    return {"order":args.order-1,"run":args.previous_run,"commit":args.previous_commit,
        "lane":args.previous_lane,"main_bytes":args.previous_report_bytes,
        "main_sha256":args.previous_report_sha256,
        "publication_bytes":args.previous_publication_bytes,
        "publication_sha256":args.previous_publication_sha256,
        "driver_filename":args.previous_driver_filename,
        "driver_bytes":args.previous_driver_bytes,"driver_sha256":args.previous_driver_sha256,
        "target_sha256":{"-4":args.previous_target_minus_four_sha256,
                         "-2":args.previous_target_minus_two_sha256}}

def prior_target_hashes(value,order):
    field=value.get("checkpoint",{}).get("original_translation_target",{})
    return field.get("original_N2G_sha256") if order==2 else field.get("original_target_sha256")

def validate_previous_payloads(value,publication,report_name,spec):
    """Validate a fully bound predecessor; no old algebra or row evaluation here."""
    order=spec["order"]
    checkpoint=value.get("checkpoint",{})
    witness=checkpoint.get("dual_certificate",{})
    upper=checkpoint.get("response_upper_bound",{})
    previous=checkpoint.get("original_translation_target",{})
    coefficient=value.get("coefficient_checkpoint") or {}
    expected_schema=SECOND_SCHEMA if order==2 else SCHEMA
    nonmember_field=("universal_N2G_nonmember_in_full_R8" if order==2
                     else "universal_target_nonmember_in_full_R8")
    count=witness.get("control_columns")
    original=upper.get("original_columns")
    retained=upper.get("retained_original_columns")
    if (not isinstance(order,int) or order<2 or
        value.get("schema")!=expected_schema or value.get("completion")!="complete"
        or value.get("github_repository")!=static.REPOSITORY
        or value.get("github_run_id")!=spec["run"] or value.get("github_sha")!=spec["commit"]
        or value.get("source_hashes",{}).get("driver")!={
            "filename":spec["driver_filename"],"bytes":spec["driver_bytes"],
            "sha256":spec["driver_sha256"]}
        or checkpoint.get("outcome")!="nonmember_certified"
        or not checkpoint.get(nonmember_field)
        or checkpoint.get("orbit_dimension_lower_bound")!=order+1
        or checkpoint.get("orbit_dimension_exact") is not None
        or not witness.get("rational_nonmembership_certified")
        or not isinstance(count,int) or count<1
        or witness.get("modular_control_rank")!=count
        or not witness.get("modular_pivot_determinant")
        or not witness.get("modular_augmented_determinant")
        or not witness.get("modular_functional_target_value")
        or not isinstance(original,int) or original<count
        or not isinstance(retained,list) or len(retained)!=count
        or len(set(retained))!=count or any(not isinstance(j,int) or not 0<=j<original for j in retained)
        or upper.get("proved_true_response_dimension_upper_bound")!=count
        or upper.get("verified_original_dependency_count")!=original-count
        or not isinstance(upper.get("verified_original_dependencies_sha256"),str)
        or len(upper["verified_original_dependencies_sha256"])!=64
        or previous.get("order")!=order
        or prior_target_hashes(value,order)!=spec["target_sha256"]
        or not coefficient.get("all_encountered_rational_denominators_invertible")
        or not coefficient.get("prime_checked_by_trial_division")):
        raise ValueError("a fully published original nonmembership proof for exactly order-1 is required")
    if (publication.get("schema")!="visible-new-mechanism-actions-v1"
        or publication.get("repository")!=static.REPOSITORY
        or str(publication.get("run_id"))!=spec["run"]
        or publication.get("source_commit")!=spec["commit"]
        or publication.get("lane")!=spec["lane"]):
        raise ValueError("predecessor terminal-publication provenance")
    outputs=[x for x in publication.get("outputs",[]) if x.get("path")==report_name]
    if len(outputs)!=1 or any(outputs[0].get(k)!=v for k,v in (
        ("bytes",spec["main_bytes"]),("sha256",spec["main_sha256"]),
        ("raw_bytes",spec["main_bytes"]),("raw_sha256",spec["main_sha256"]))):
        raise ValueError("predecessor main is not bound by terminal publication")
    key="topics/visible-flex-new-mechanism/scripts/"+spec["driver_filename"]
    if publication.get("source_files",{}).get(key)!={
            "bytes":spec["driver_bytes"],"sha256":spec["driver_sha256"]}:
        raise ValueError("predecessor source identity in publication")
    return {"order":order,"run":spec["run"],"commit":spec["commit"],"lane":spec["lane"],
        "main":{"filename":report_name,"bytes":spec["main_bytes"],"sha256":spec["main_sha256"]},
        "driver":{"filename":spec["driver_filename"],"bytes":spec["driver_bytes"],
                  "sha256":spec["driver_sha256"]},
        "original_target_sha256":spec["target_sha256"],
        "completed_nonmembership_consumed":True,"old_response_columns":original,
        "old_retained_original_columns":count,"old_original_dependencies":original-count,
        "old_response_columns_recompiled":False,"old_separations_repeated":False,
        "old_dependencies_recomputed":False}

def bind_previous_certificate(args,report):
    spec=previous_spec(args)
    raw=static.checked_bytes(args.previous_report,100000)
    publication_raw=static.checked_bytes(args.previous_publication,100000)
    if (len(raw)!=spec["main_bytes"] or sha(raw)!=spec["main_sha256"]
        or len(publication_raw)!=spec["publication_bytes"]
        or sha(publication_raw)!=spec["publication_sha256"]):
        raise ValueError("explicitly bound predecessor main/publication bytes changed")
    binding=validate_previous_payloads(json.loads(raw),json.loads(publication_raw),
                                      args.previous_report.name,spec)
    binding["publication"]={"filename":args.previous_publication.name,
        "bytes":spec["publication_bytes"],"sha256":spec["publication_sha256"]}
    report["completed_previous_translation_input"]=binding
    return spec

def portable_payload(ring,target,columns,labels,report):
    if len(columns)!=len(labels):
        raise ValueError("a portable block cannot omit its declared original columns")
    named={f"target_{mode}":value for mode,value in target.items()}
    records=[]
    for index,(column,label) in enumerate(zip(columns,labels)):
        roots={str(mode):f"column_{index:03d}_{mode}" for mode in MODES}
        named.update({roots[str(mode)]:column[mode] for mode in MODES})
        records.append({"index":index,"label":label,"roots":roots,
            "original_mode_sha256":{str(mode):ring.digest(column[mode]) for mode in MODES}})
    return {"schema":SCHEMA+"-original-expressions",
        "github_repository":report.get("github_repository"),
        "github_run_id":report.get("github_run_id"),"github_sha":report.get("github_sha"),
        "source_hashes":report.get("source_hashes",{}),
        "content_scope":("one-translation-target-and-complete-new-response-block"
                         if columns else "zero-target-only"),
        "translation":report.get("translation",{}),
        "completed_previous_translation_input":report.get("completed_previous_translation_input"),
        "response_coverage":report.get("response_coverage"),
        "target_roots":{str(mode):f"target_{mode}" for mode in MODES},
        "column_records":records,"all_compiled_original_columns_included":True,
        "proofs_must_be_read_from_separate_completed_main_or_full_report":True,
        "export_is_not_a_membership_or_rank_certificate":True,
        **static.old.serialize_expressions(ring,named)}

def save_portable_block(args,ring,target,columns,labels,report):
    """Supplemental export failure never replaces an existing mathematical result."""
    path=args.output.with_name(args.output.stem+"-original-expressions.json.gz")
    info={"filename":path.name,"persisted":False,"supplemental_to_mathematical_certificate":True,
        "requested_order":args.order,"requested_weight":1-args.order,
        "compiled_original_columns":len(columns),"all_compiled_original_columns_included":False}
    report["portable_new_block_expression_export"]=info
    # Bound serialization itself before allocating a large redundant roots table.
    total_terms=sum(len(value.terms) for value in target.values())+sum(
        len(value.terms) for column in columns for value in column.values())
    info["original_root_term_count"]=total_terms
    if total_terms>300000:
        info["reason"]="supplemental original-root serialization term ceiling"
        return info
    try:
        data=portable_payload(ring,target,columns,labels,report)
        raw=canonical(data)
        info.update({"raw_bytes":len(raw),"raw_sha256":sha(raw),
            "root_count":len(data["roots"]),"profile_atom_count":len(data["profile_atoms"]),
            "content_scope":data["content_scope"]})
        if len(raw)>args.max_export_raw_bytes:
            info["reason"]="supplemental portable raw byte ceiling"
            return info
        packed=gzip.compress(raw,mtime=0)
        info.update({"stored_bytes":len(packed),"stored_sha256":sha(packed)})
        if len(packed)>args.max_export_bytes:
            info["reason"]="supplemental portable compressed byte ceiling"
            return info
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_bytes(packed)
        info["persisted"]=True
        info["all_compiled_original_columns_included"]=True
        info["contains_original_expression_not_only_hashes"]=True
    except Exception as error:
        info["reason"]="supplemental export failed; keep the independent mathematical report"
        info["error"]={"type":type(error).__name__,"message":str(error)}
    return info

def study(args,report,started):
    limits=exact.Limits(args.max_seconds,500000,100000,120000,500000,args.memory_mib,8192)
    ring=colored.ColoredRing(limits)
    weight=1-args.order
    report["phase"]="bound_original_G_and_immediate_predecessor"
    first.bind_G_certificate(args,report)
    spec=bind_previous_certificate(args,report)
    templates,original,_=seed.load_G_and_bound(args,ring,report)
    generator=first.TranslationGenerator(ring)
    degree_bound=max(generator.degree(v) for v in original.values())
    if args.order>degree_bound+1:
        raise ValueError("the requested order lies beyond the first guaranteed zero; do not skip it")
    previous=original
    for _ in range(args.order-1):
        previous={mode:generator.expression(value) for mode,value in previous.items()}
    if {str(m):ring.digest(v) for m,v in previous.items()}!=spec["target_sha256"]:
        raise AssertionError("reconstructed preceding original target differs from the completed report")
    target={mode:generator.expression(value) for mode,value in previous.items()}
    grade=blocks.ScalingGrading(ring)
    if any(set(grade.split(value))-{weight} for value in target.values()):
        raise AssertionError("the true translation must lower scaling weight by exactly one")
    report["translation"]={"order":args.order,"weight":weight,
        "rule":"N(x)=1; N(jets)=0; N(I F)=I(N F)",
        "common_right_anchor_transport_explicit":True,
        "full_xi_derivative_used_as_translation":False,
        "original_G_sha256":{str(m):ring.digest(v) for m,v in original.items()},
        "bound_previous_original_target_sha256":{str(m):ring.digest(v) for m,v in previous.items()},
        "original_target_sha256":{str(m):ring.digest(v) for m,v in target.items()},
        "finite_coordinate_degree_upper_bound":degree_bound,
        "new_raw_terms":{str(m):len(v.terms) for m,v in target.items()},
        "preceding_target_reconstructed_only_to_verify_raw_hash":True,
        "earlier_response_columns_recomputed":False}
    normalizer=colored.ColoredNormalizer(ring)
    target_vector=colored.vector_from_modes(target,normalizer)
    report["target_word_representative"]={"terms":len(target_vector),
        "sha256":colored.vector_digest(target_vector),"independence_not_assumed":True}
    if not target_vector:
        save_portable_block(args,ring,target,[],[],report)
        report["checkpoint"]={"outcome":"target_zero_verified",
            "fresh_original_checks":first.fresh_zero(ring,target,[],{}),
            "orbit_dimension_exact":args.order,"further_translation_orders_needed":False}
        report["completion"]="complete"
        return

    labels=[]
    for i,wi in enumerate(blocks.PARAMETER_WEIGHTS):
        for j,wj in enumerate(blocks.THIRD_WEIGHTS):
            if wi+wj==weight:
                labels.append({"quadratic_index":i,"quadratic_name":exact.PARAMETERS[i],
                    "third_index":j,"third_weight":wj,
                    "v2_original_third_index":blocks.EXPECTED_KEPT[j],
                    "third_original_sha256":ring.digest(templates[j])})
    if not labels:
        raise AssertionError("a nonzero target has no enumerated complete response block")
    report["all_original_response_columns"]=labels
    report["response_coverage"]={"full_E8":True,"all_W36":True,
        "weight":weight,"columns":len(labels),"physical_seven_dimensional_subspace_not_substituted":True}
    template_checks=[]
    for j in sorted({x["third_index"] for x in labels}):
        difference=templates[j]-grade.project(templates[j],blocks.THIRD_WEIGHTS[j])
        proof=normalizer.word.expression(difference)
        if proof.terms:
            raise AssertionError("bound true third basis weight changed")
        template_checks.append({"third_index":j,"zero_sha256":proof.digest()})
    report["template_weight_checks"]=template_checks
    quadratics=exact.operator_basis(ring)
    columns=[]
    vectors=[]
    report["phase"]="complete_requested_weight_original_responses"
    for index,label in enumerate(labels):
        third=colored.ThirdOperator(ring,templates[label["third_index"]])
        value=blocks.full_response(ring,third,quadratics[label["quadratic_index"]])
        vector=colored.vector_from_modes(value,normalizer)
        columns.append(value);vectors.append(vector)
        label["original_mode_sha256"]={str(m):ring.digest(v) for m,v in value.items()}
        label["word_terms"]=len(vector);label["word_sha256"]=colored.vector_digest(vector)
        report["checkpoint"]={"completed_original_columns":len(columns),"total_columns":len(labels),
            "identity_or_nonmembership_proved":False}
        ring.substitution_cache.clear()
        limits.formal.time_check()
        print(json.dumps({"phase":report["phase"],"columns":len(columns),"of":len(labels)}),flush=True)

    report["phase"]="portable_complete_new_original_block"
    save_portable_block(args,ring,target,columns,labels,report)
    regularity=dual.reachable_jet_bound(ring,list(target.values())+
        [value for modes in columns for value in modes.values()])
    report["input_regularity"]=regularity
    if regularity["maximum_input_jet"]>args.bump_power-1:
        raise ValueError("increase the fixed bump power before using this higher-jet block")
    report["phase"]="sound_original_response_upper_bound"
    span=colored.JointSpan(vectors,limits)
    retained=span.independent
    dependencies=[]
    for index,vector in enumerate(vectors):
        if index in retained:
            continue
        coefficients,remainder=span.reduce(vector)
        if remainder or not set(coefficients).issubset(retained):
            raise AssertionError("retained original spanning certificate")
        target_relation=columns[index]
        checks=first.fresh_zero(ring,target_relation,columns,coefficients)
        dependencies.append({"discarded_original_column":index,
            "retained_original_coefficients":[[j,str(c)] for j,c in sorted(coefficients.items())],
            "fresh_original_checks":checks})
    report["response_upper_bound"]={"original_columns":len(labels),
        "retained_original_columns":retained,
        "proved_true_response_dimension_upper_bound":len(retained),
        "verified_original_dependencies":dependencies,
        "representative_rank_not_promoted_to_independence":True}
    coefficients,remainder=span.reduce(target_vector)
    report["word_remainder"]={"terms":len(remainder),"sha256":colored.vector_digest(remainder),
        "nonmembership_claimed_from_remainder":False}
    report["candidate_coefficients"]=[[j,str(c)] for j,c in sorted(coefficients.items())]
    if not remainder:
        checks=first.fresh_zero(ring,target,columns,coefficients)
        report["checkpoint"]={"outcome":"member_identity_verified",
            "same_coefficients_for_both_modes":[[j,str(c)] for j,c in sorted(coefficients.items())],
            "fresh_original_checks":checks,"orbit_dimension_exact":args.order,
            "further_translation_orders_needed":False}
        report["completion"]="complete"
        return

    report["phase"]="original_rational_requested_weight_evaluation"
    remaining=args.max_seconds-(time.monotonic()-started)
    if remaining<=0:
        raise poly.PolynomialBudgetExceeded("time budget before original rational evaluation")
    report["checkpoint"]={"completed_original_columns":len(labels),
        "proved_response_upper_bound":len(retained),"original_evaluated_columns":0}
    report["original_evaluation"]=first.raw_evaluation(args,ring,target,templates,labels,retained,
                                                report,remaining)
    witness=report["original_evaluation"]["dual_certificate"]
    certified=witness["rational_nonmembership_certified"]
    report["checkpoint"]={"outcome":"nonmember_certified" if certified else "undecided",
        "proved_response_upper_bound":len(retained),"dual_certificate":witness,
        "universal_target_nonmember_in_full_R8":certified,
        "orbit_dimension_lower_bound":args.order+1 if certified else args.order,
        "orbit_dimension_exact":None,"further_translation_orders_computed":False,
        "fixed_test_pair_all_other_weights_excluded":False}
    report["completion"]="complete"


def compact_checkpoint_dual(report,threshold=16000):
    """Keep complete raw matrices in the full report; bound the small main."""
    checkpoint=report.get("checkpoint",{})
    witness=checkpoint.get("dual_certificate")
    if not witness or "modular_augmented_matrix" not in witness:
        return
    matrix=witness["modular_augmented_matrix"]
    if len(canonical(matrix))<=threshold:
        return
    copied=copy.deepcopy(witness)
    del copied["modular_augmented_matrix"]
    copied["original_modular_augmented_matrix"]={
        "rows":len(matrix),"columns":len(matrix[0]) if matrix else 0,
        "sha256":sha(canonical(matrix)),"complete_matrix_in_full_report":True}
    checkpoint["dual_certificate"]=copied

def artificial_previous_payloads(spec):
    order=spec["order"]
    target_key="original_N2G_sha256" if order==2 else "original_target_sha256"
    nonmember_key=("universal_N2G_nonmember_in_full_R8" if order==2
                   else "universal_target_nonmember_in_full_R8")
    checkpoint={"outcome":"nonmember_certified",nonmember_key:True,
        "orbit_dimension_lower_bound":order+1,"orbit_dimension_exact":None,
        "dual_certificate":{"rational_nonmembership_certified":True,"control_columns":2,
            "modular_control_rank":2,"modular_pivot_determinant":5,
            "modular_augmented_determinant":7,"modular_functional_target_value":9},
        "response_upper_bound":{"original_columns":3,"retained_original_columns":[0,2],
            "proved_true_response_dimension_upper_bound":2,
            "verified_original_dependency_count":1,
            "verified_original_dependencies_sha256":"a"*64},
        "original_translation_target":{"order":order,target_key:spec["target_sha256"]}}
    value={"schema":SECOND_SCHEMA if order==2 else SCHEMA,"completion":"complete",
        "github_repository":static.REPOSITORY,"github_run_id":spec["run"],
        "github_sha":spec["commit"],
        "source_hashes":{"driver":{"filename":spec["driver_filename"],
                                  "bytes":spec["driver_bytes"],"sha256":spec["driver_sha256"]}},
        "checkpoint":checkpoint,"coefficient_checkpoint":{
            "all_encountered_rational_denominators_invertible":True,
            "prime_checked_by_trial_division":True}}
    publication={"schema":"visible-new-mechanism-actions-v1","repository":static.REPOSITORY,
        "run_id":spec["run"],"source_commit":spec["commit"],"lane":spec["lane"],
        "outputs":[{"path":"artificial.json","bytes":spec["main_bytes"],
                    "sha256":spec["main_sha256"],"raw_bytes":spec["main_bytes"],
                    "raw_sha256":spec["main_sha256"]}],
        "source_files":{"topics/visible-flex-new-mechanism/scripts/"+spec["driver_filename"]:
                        {"bytes":spec["driver_bytes"],"sha256":spec["driver_sha256"]}}}
    return value,publication

def small_toy():
    limits=exact.Limits(seconds=30,nodes=10000,atoms=5000,terms=5000,
                        rewrites=10000,memory_mib=256)
    ring=colored.ColoredRing(limits)
    q,qb,x=ring.color("q"),ring.color("qbar"),ring.x()
    N=first.TranslationGenerator(ring)
    checks={}
    def same(a,b,label):
        if (a-b).terms:
            raise AssertionError(label)
        checks[label]=True
    A=(q.D()*q.D()).I()
    value=x*x*x*A+(x*x*x*q.D()*q.D()).I()
    current=value
    for _ in range(3):
        current=N.expression(current)
    same(current,12*A,"third_translation_pays_outer_and_inner_coordinates")
    same(N.expression(current),ring.number(0),"artificial_chain_has_exact_zero_successor")
    grade=blocks.ScalingGrading(ring)
    if set(grade.split(value))!={2} or set(grade.split(current))!={-1}:
        raise AssertionError("three successive true weight decrements")
    checks["third_translation_lowers_weight_by_three"]=True
    nested=(x*(x*(x*q*qb).I()).I()).I()
    current_nested=nested
    for _ in range(3):
        current_nested=N.expression(current_nested)
    same(current_nested,6*(q*qb).I().I().I(),
         "three_nested_primitives_preserve_all_coordinate_product_terms")
    difference=sum((amount*first.ExactShift(ring,t).expression(value)
                    for t,amount in ((3,1),(2,-3),(1,3),(0,-1))),ring.number(0))
    same(difference,current,"independent_exact_third_forward_difference")
    primitive=value.I()
    for _ in range(3):
        primitive=N.expression(primitive)
    same(primitive,current.I(),"successor_commutes_with_common_right_primitive")
    spec=copy.deepcopy(DEFAULT_PREVIOUS)
    value0,publication=artificial_previous_payloads(spec)
    validate_previous_payloads(value0,publication,"artificial.json",spec)
    checks["second_to_third_predecessor_interface_accepted"]=True
    later=copy.deepcopy(spec)
    later.update({"order":3,"driver_filename":"artificial-successor.py"})
    later_value,later_publication=artificial_previous_payloads(later)
    validate_previous_payloads(later_value,later_publication,"artificial.json",later)
    checks["generic_successor_schema_accepted_only_for_immediate_order"]=True
    for label,mutate in (
        ("changed_bound_target_hash_rejected",
         lambda z:z["checkpoint"]["original_translation_target"]["original_N2G_sha256"].update({"-4":"bad"})),
        ("incomplete_predecessor_rejected",lambda z:z.update({"completion":"resource_limit"})),
        ("already_positive_predecessor_stops_chain",
         lambda z:z["checkpoint"].update({"outcome":"member_identity_verified","orbit_dimension_exact":2})),
        ("representative_rank_without_true_minor_rejected",
         lambda z:z["checkpoint"]["dual_certificate"].update({"rational_nonmembership_certified":False})),
        ("skipped_translation_order_rejected",
         lambda z:z["checkpoint"]["original_translation_target"].update({"order":1})),
        ("missing_original_denominator_gate_rejected",
         lambda z:z["coefficient_checkpoint"].update({"all_encountered_rational_denominators_invertible":False})),
    ):
        damaged=copy.deepcopy(value0);mutate(damaged)
        try:
            validate_previous_payloads(damaged,publication,"artificial.json",spec)
        except ValueError:
            checks[label]=True
        else:
            raise AssertionError(label)
    damaged=copy.deepcopy(publication)
    damaged["source_files"]["topics/visible-flex-new-mechanism/scripts/"+spec["driver_filename"]]["sha256"]="bad"
    try:
        validate_previous_payloads(value0,damaged,"artificial.json",spec)
    except ValueError:
        checks["publication_source_mismatch_rejected"]=True
    else:
        raise AssertionError("publication source mismatch")
    matrix=[[1,2],[3,4]]
    witness={"rational_nonmembership_certified":True,"modular_augmented_matrix":matrix}
    artificial={"original_evaluation":{"dual_certificate":witness},
                "checkpoint":{"dual_certificate":witness}}
    compact_checkpoint_dual(artificial,threshold=1)
    if (artificial["original_evaluation"]["dual_certificate"]["modular_augmented_matrix"]!=matrix
        or "modular_augmented_matrix" in artificial["checkpoint"]["dual_certificate"]
        or artificial["checkpoint"]["dual_certificate"]["original_modular_augmented_matrix"]["sha256"]!=sha(canonical(matrix))):
        raise AssertionError("small output does not preserve the complete original matrix")
    checks["compact_main_preserves_full_original_matrix_and_digest"]=True
    artificial_target={-4:q*q*q*q,-2:q*q*q*qb}
    artificial_columns=[{-4:value,-2:value+q*qb}]
    artificial_labels=[{"quadratic_index":0,"third_index":0,"artificial":True}]
    artificial_report={"source_hashes":{"driver":{"sha256":"artificial"}},
        "translation":{"order":3,"weight":-2},"response_coverage":{"columns":1}}
    payload=portable_payload(ring,artificial_target,artificial_columns,artificial_labels,artificial_report)
    restored=static.old.decode_expressions(ring,payload)
    expected={"target_-4":artificial_target[-4],"target_-2":artificial_target[-2],
              "column_000_-4":artificial_columns[0][-4],"column_000_-2":artificial_columns[0][-2]}
    if set(restored)!=set(expected):
        raise AssertionError("portable target and complete artificial mode columns")
    for name,expression in expected.items():
        if (restored[name]-expression).terms:
            raise AssertionError("portable original round trip")
    checks["portable_both_modes_all_columns_original_round_trip"]=True
    with tempfile.TemporaryDirectory(prefix="G-successor-toy-") as temporary:
        toyargs=argparse.Namespace(output=Path(temporary)/"artificial.json",order=3,
                                  max_export_bytes=1,max_export_raw_bytes=40000000)
        limited={"completion":"mathematical_artificial_result","source_hashes":{}}
        info=save_portable_block(toyargs,ring,artificial_target,artificial_columns,artificial_labels,limited)
        if info["persisted"] or limited["completion"]!="mathematical_artificial_result":
            raise AssertionError("supplemental export ceiling replaced the mathematical status")
        if (Path(temporary)/info["filename"]).exists():
            raise AssertionError("over-budget portable output must not be written")
        toyargs.max_export_bytes=2000000
        success={"completion":"mathematical_artificial_result","source_hashes":{}}
        saved=save_portable_block(toyargs,ring,artificial_target,artificial_columns,artificial_labels,success)
        stored=(Path(temporary)/saved["filename"]).read_bytes()
        raw=gzip.decompress(stored)
        if (not saved["persisted"] or len(stored)!=saved["stored_bytes"]
            or sha(stored)!=saved["stored_sha256"] or len(raw)!=saved["raw_bytes"]
            or sha(raw)!=saved["raw_sha256"]):
            raise AssertionError("portable compressed and raw byte binding")
        again=static.old.decode_expressions(ring,json.loads(raw))
        if set(again)!=set(expected) or any((again[name]-value).terms for name,value in expected.items()):
            raise AssertionError("saved portable source expressions changed")
    checks["supplemental_export_limit_preserves_mathematical_status"]=True
    checks["saved_export_raw_compressed_hashes_and_original_roots_verified"]=True
    return {"checks":checks,"all_passed":all(checks.values()),
        "original_G_or_previous_target_read":False,"research_profile_evaluated":False,
        "old_or_new_research_response_columns_compiled":False}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only",action="store_true")
    parser.add_argument("--order",type=int,choices=tuple(range(3,11)),default=3)
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--source-report",type=Path,default=static.DEFAULT_DIR/"local-fourth-quotient.json")
    parser.add_argument("--source-report-sha256",default=static.REPORT_SHA)
    parser.add_argument("--source-run",default=static.SOURCE_RUN)
    parser.add_argument("--source-commit",default=static.SOURCE_COMMIT)
    parser.add_argument("--publication-receipt",type=Path,default=static.DEFAULT_DIR/"receipt.json")
    parser.add_argument("--publication-receipt-sha256",default=static.PUBLICATION_SHA)
    parser.add_argument("--input-export",type=Path,default=static.DEFAULT_DIR/"local-fourth-quotient-original-expressions.json.gz")
    parser.add_argument("--export-sha256",default=static.EXPORT_SHA)
    parser.add_argument("--third-receipt",type=Path,default=dual.DEFAULT_RECEIPT)
    parser.add_argument("--block-receipt",type=Path,default=static.DEFAULT_DIR/"local-fourth-quotient-weight-+1.json")
    parser.add_argument("--G-report",type=Path,default=first.G_DIR/"static-G-rational-dual.json")
    parser.add_argument("--G-publication",type=Path,default=first.G_DIR/"receipt.json")
    parser.add_argument("--previous-report",type=Path,default=DEFAULT_PREVIOUS_DIR/"G-second-translation.json")
    parser.add_argument("--previous-publication",type=Path,default=DEFAULT_PREVIOUS_DIR/"receipt.json")
    for name,key in (("previous-run","run"),("previous-commit","commit"),("previous-lane","lane"),
                     ("previous-report-sha256","main_sha256"),
                     ("previous-publication-sha256","publication_sha256"),
                     ("previous-driver-filename","driver_filename"),
                     ("previous-driver-sha256","driver_sha256")):
        parser.add_argument("--"+name,default=DEFAULT_PREVIOUS[key])
    for name,key in (("previous-report-bytes","main_bytes"),
                     ("previous-publication-bytes","publication_bytes"),
                     ("previous-driver-bytes","driver_bytes")):
        parser.add_argument("--"+name,type=int,default=DEFAULT_PREVIOUS[key])
    parser.add_argument("--previous-target-minus-four-sha256",default=DEFAULT_PREVIOUS["target_sha256"]["-4"])
    parser.add_argument("--previous-target-minus-two-sha256",default=DEFAULT_PREVIOUS["target_sha256"]["-2"])
    parser.add_argument("--max-seconds",type=float,default=240)
    parser.add_argument("--memory-mib",type=int,default=1024)
    parser.add_argument("--max-degree",type=int,default=256)
    parser.add_argument("--max-operations",type=int,default=10000000)
    parser.add_argument("--points",type=int,default=24)
    parser.add_argument("--bump-power",type=int,default=8)
    parser.add_argument("--prime",type=int,default=2147483647)
    parser.add_argument("--max-export-bytes",type=int,default=2000000)
    parser.add_argument("--max-export-raw-bytes",type=int,default=40000000)
    parser.add_argument("--max-main-bytes",type=int,default=90000)
    parser.add_argument("--max-full-report-bytes",type=int,default=2500000)
    args=parser.parse_args()
    if (min(args.max_seconds,args.memory_mib,args.max_degree,args.max_operations,args.points,
            args.max_main_bytes,args.max_full_report_bytes,args.max_export_bytes,args.max_export_raw_bytes,
            args.previous_report_bytes,
            args.previous_publication_bytes,args.previous_driver_bytes)<=0 or args.bump_power<8):
        parser.error("positive bounded budgets and bump power at least eight")
    if args.prime%4!=3 or args.points+1>=args.prime:
        parser.error("the checked prime must be 3 mod 4 and exceed query denominators")
    if not 10000<=args.max_main_bytes<100000:
        parser.error("small main report must reserve 10000..99999 bytes")
    if args.max_main_bytes+args.max_full_report_bytes+args.max_export_bytes>static.TOTAL_BYTES:
        parser.error("total published output ceiling")
    if not args.toy_only and not(os.environ.get("GITHUB_ACTIONS")=="true"
                                 and os.environ.get("GITHUB_REPOSITORY")==static.REPOSITORY):
        parser.error("genuine original-expression research only in this public repository Actions")
    started=time.monotonic()
    report={"schema":SCHEMA,"completion":"started","phase":"source_binding",
        "github_repository":os.environ.get("GITHUB_REPOSITORY"),
        "github_run_id":os.environ.get("GITHUB_RUN_ID"),"github_sha":os.environ.get("GITHUB_SHA"),
        "source_hashes":{},"completed_blocks":[],
        "scope":"exactly one requested true translation; complete new weight 1-order response block",
        "requested_order":args.order,"requested_weight":1-args.order,
        "limits":{"seconds":args.max_seconds,"memory_polling_mib":args.memory_mib,
            "max_degree":args.max_degree,"max_operations":args.max_operations,
            "main_bytes":args.max_main_bytes,"complete_report_bytes":args.max_full_report_bytes,
            "supplemental_export_bytes":args.max_export_bytes,
            "supplemental_export_raw_bytes":args.max_export_raw_bytes,
            "total_published_bytes":static.TOTAL_BYTES},
        "old_forcing_recompiled":False,"W_recompiled":False,"local_density_recompiled":False,
        "old_separations_reevaluated":False,"old_response_blocks_recomputed":False,
        "automatic_translation_chain_run":False,"full_fourth_cost_paid":False,
        "ruling_paid":False,"finite_isometric_family_constructed":False}
    code=0
    try:
        report["source_hashes"]=source_identity()
        if args.toy_only:
            report["phase"]="small_artificial_successor_and_predecessor_interfaces"
            report["toy"]=small_toy();report["completion"]="toy_passed"
        else:
            study(args,report,started)
    except (formal.CompilationBudgetExceeded,poly.PolynomialBudgetExceeded) as error:
        report["completion"]="resource_limit";report["error"]=str(error);code=2
    except Exception as error:
        report["completion"]="implementation_check_failed"
        report["error"]={"type":type(error).__name__,"message":str(error)};code=1
    checkpoint=report.setdefault("checkpoint",{})
    checkpoint["requested_order"]=args.order
    checkpoint["requested_weight"]=1-args.order
    checkpoint["automatic_translation_chain_run"]=False
    if "translation" in report:
        checkpoint["original_translation_target"]=report["translation"]
    if "response_upper_bound" in report:
        upper=report["response_upper_bound"]
        checkpoint["response_upper_bound"]={
            "original_columns":upper["original_columns"],
            "retained_original_columns":upper["retained_original_columns"],
            "proved_true_response_dimension_upper_bound":upper["proved_true_response_dimension_upper_bound"],
            "verified_original_dependency_count":len(upper["verified_original_dependencies"]),
            "verified_original_dependencies_sha256":sha(canonical(upper["verified_original_dependencies"])),
            "complete_original_dependency_proofs_in_full_report":True}
    for field in ("completed_G_input","completed_previous_translation_input","input_regularity",
                  "portable_new_block_expression_export"):
        if field in report:
            checkpoint[field]=report[field]
    positive=checkpoint.get("same_coefficients_for_both_modes")
    if positive is not None and len(canonical(positive))>16000:
        report["positive_identity_coefficients"]=positive
        del checkpoint["same_coefficients_for_both_modes"]
        checkpoint["positive_coefficients"]={
            "count":len(positive),"sha256":sha(canonical(positive)),
            "complete_rational_coefficients_in_full_report":True}
    compact_checkpoint_dual(report)
    report["elapsed_seconds"]=time.monotonic()-started
    report["peak_rss_mib"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    exported=report.get("portable_new_block_expression_export") or {}
    published=exported.get("stored_bytes",0) if exported.get("persisted") else 0
    written=static.publish_report(args.output,report,args.max_main_bytes,args.max_full_report_bytes,
                                  already_published=published)
    if written["completion"]=="output_limit":
        code=2
    print(json.dumps({"output":str(args.output),**written}),flush=True)
    return code

if __name__=="__main__":
    raise SystemExit(main())
