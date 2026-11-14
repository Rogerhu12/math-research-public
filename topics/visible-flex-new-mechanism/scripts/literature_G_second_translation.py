#!/usr/bin/env python3
"""R128: only the second true translation derivative of G modulo full R8.

Consume the published R126 certificate and frozen original G/W expressions.
No old weight-zero response or separation is recomputed.  Only the new
weight-minus-one block is evaluated, with the same real coefficients in both
modes.  A failed word representative is never a nonmembership certificate.
"""
from __future__ import annotations

import argparse
import copy
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
SCHEMA="visible-flex-G-second-translation-original-v1"
FIRST_DRIVER_BYTES=26885
FIRST_DRIVER_SHA="331fea2c1aef154c4d5866e4708f067c555f9fb61f02a11ee32a7f44d25f01f5"
FIRST_MAIN_BYTES=23923
FIRST_MAIN_SHA="9926a1f7026064c95c297b34da60ed5f1b345bc37753a23e75295cf44792fe82"
FIRST_PUBLICATION_BYTES=33085
FIRST_PUBLICATION_SHA="06e5d82a7e7db8922d42347920609c83a3ad0114050cdbbdafc72084c3e25bec"
FIRST_RUN="43649525432"
FIRST_COMMIT="5852d7d4400859e53dde789b4d63f200d0e0acce"
FIRST_DIR=Path(first.__file__).resolve().parents[1]/"notes"/("actions-"+FIRST_RUN+"-1-g_first_translation")
FIRST_NG_SHA={
    "-4":"de54f551a028ca45ece143f661df99ab4f7541b1ec39cab7add66fc60dd0e130",
    "-2":"2eb0fe581f521b2e6f0e520b2ac5f91e09da0349cf71994852369dfeef7409e4",
}
FIRST_RETAINED=[0,1,2,3,4,5,7,8,9,10,11,12,13,15,17,19]
FIRST_DEPENDENCIES_SHA="1fc11b2b550b4554021be768ff1db9854c218e8bebb2983709c915b910f08e72"

def source_identity():
    value=first.source_identity()
    if value["driver"]!={"filename":"literature_G_first_translation.py",
                         "bytes":FIRST_DRIVER_BYTES,"sha256":FIRST_DRIVER_SHA}:
        raise ValueError("explicitly rebind the frozen completed first-translation producer")
    value["completed_first_translation_producer"]=value.pop("driver")
    value["driver"]=static.identity(__file__)
    return value

def validate_previous_payloads(value,publication,report_name):
    checkpoint=value.get("checkpoint",{})
    witness=checkpoint.get("dual_certificate",{})
    upper=checkpoint.get("response_upper_bound",{})
    previous=checkpoint.get("original_translation_target",{})
    if (value.get("schema")!=first.SCHEMA or value.get("completion")!="complete"
        or value.get("github_repository")!=static.REPOSITORY
        or value.get("github_run_id")!=FIRST_RUN or value.get("github_sha")!=FIRST_COMMIT
        or value.get("source_hashes",{}).get("driver",{}).get("sha256")!=FIRST_DRIVER_SHA
        or checkpoint.get("outcome")!="nonmember_certified"
        or not checkpoint.get("universal_NG_nonmember_in_full_R8")
        or checkpoint.get("orbit_dimension_lower_bound")!=2
        or not witness.get("rational_nonmembership_certified")
        or witness.get("control_columns")!=16
        or witness.get("modular_pivot_determinant")!=775740714
        or witness.get("modular_augmented_determinant")!=172056171
        or witness.get("modular_functional_target_value")!=548771152
        or upper.get("original_columns")!=20
        or upper.get("retained_original_columns")!=FIRST_RETAINED
        or upper.get("proved_true_response_dimension_upper_bound")!=16
        or upper.get("verified_original_dependency_count")!=4
        or upper.get("verified_original_dependencies_sha256")!=FIRST_DEPENDENCIES_SHA
        or previous.get("order")!=1
        or previous.get("original_NG_sha256")!=FIRST_NG_SHA):
        raise ValueError("the completed R126 true first-translation certificate is required")
    if (publication.get("schema")!="visible-new-mechanism-actions-v1"
        or publication.get("repository")!=static.REPOSITORY
        or str(publication.get("run_id"))!=FIRST_RUN
        or publication.get("source_commit")!=FIRST_COMMIT
        or publication.get("lane")!="g_first_translation"):
        raise ValueError("first-translation terminal-publication provenance")
    outputs=[x for x in publication.get("outputs",[]) if x.get("path")==report_name]
    if len(outputs)!=1 or any(outputs[0].get(k)!=v for k,v in (
        ("bytes",FIRST_MAIN_BYTES),("sha256",FIRST_MAIN_SHA),
        ("raw_bytes",FIRST_MAIN_BYTES),("raw_sha256",FIRST_MAIN_SHA))):
        raise ValueError("first-translation main is not bound by terminal publication")
    key="topics/visible-flex-new-mechanism/scripts/literature_G_first_translation.py"
    if publication.get("source_files",{}).get(key)!={
            "bytes":FIRST_DRIVER_BYTES,"sha256":FIRST_DRIVER_SHA}:
        raise ValueError("first-translation source identity in publisher receipt")
    return {"run":FIRST_RUN,"commit":FIRST_COMMIT,
        "main":{"filename":report_name,"bytes":FIRST_MAIN_BYTES,"sha256":FIRST_MAIN_SHA},
        "original_NG_sha256":FIRST_NG_SHA,
        "completed_nonmembership_consumed":True,
        "old_twenty_response_columns_recompiled":False,
        "old_sixteen_control_evaluations_repeated":False,
        "old_four_dependencies_recomputed":False}

def bind_first_certificate(args,report):
    raw=static.checked_bytes(args.first_report,100000)
    publication_raw=static.checked_bytes(args.first_publication,100000)
    if (len(raw)!=FIRST_MAIN_BYTES or sha(raw)!=FIRST_MAIN_SHA
        or len(publication_raw)!=FIRST_PUBLICATION_BYTES
        or sha(publication_raw)!=FIRST_PUBLICATION_SHA):
        raise ValueError("frozen R126 main/publication bytes changed")
    binding=validate_previous_payloads(json.loads(raw),json.loads(publication_raw),
                                      args.first_report.name)
    binding["publication"]={"filename":args.first_publication.name,
        "bytes":FIRST_PUBLICATION_BYTES,"sha256":FIRST_PUBLICATION_SHA}
    report["completed_NG_input"]=binding

def study(args,report,started):
    limits=exact.Limits(args.max_seconds,500000,100000,120000,500000,args.memory_mib,8192)
    ring=colored.ColoredRing(limits)
    report["phase"]="bound_original_G_and_completed_first_translation"
    first.bind_G_certificate(args,report)
    bind_first_certificate(args,report)
    templates,original,_=seed.load_G_and_bound(args,ring,report)
    generator=first.TranslationGenerator(ring)
    previous={mode:generator.expression(value) for mode,value in original.items()}
    if {str(m):ring.digest(v) for m,v in previous.items()}!=FIRST_NG_SHA:
        raise AssertionError("reconstructed original NG differs from the published frozen target")
    target={mode:generator.expression(value) for mode,value in previous.items()}
    grade=blocks.ScalingGrading(ring)
    if any(set(grade.split(value))-{-1} for value in target.values()):
        raise AssertionError("the second true translation of G must have weight minus one")
    report["translation"]={"order":2,"rule":"N(x)=1; N(jets)=0; N(I F)=I(N F)",
        "common_right_anchor_transport_explicit":True,
        "full_xi_derivative_used_as_translation":False,
        "original_G_sha256":{str(m):ring.digest(v) for m,v in original.items()},
        "bound_original_NG_sha256":{str(m):ring.digest(v) for m,v in previous.items()},
        "original_N2G_sha256":{str(m):ring.digest(v) for m,v in target.items()},
        "finite_coordinate_degree_upper_bound":max(generator.degree(v) for v in original.values()),
        "new_raw_terms":{str(m):len(v.terms) for m,v in target.items()}}
    normalizer=colored.ColoredNormalizer(ring)
    target_vector=colored.vector_from_modes(target,normalizer)
    report["target_word_representative"]={"terms":len(target_vector),
        "sha256":colored.vector_digest(target_vector),"independence_not_assumed":True}
    if not target_vector:
        report["checkpoint"]={"outcome":"target_zero_verified",
            "fresh_original_checks":first.fresh_zero(ring,target,[],{}),
            "orbit_dimension_exact":2,"further_translation_orders_needed":False}
        report["completion"]="complete"
        return

    labels=[]
    for i,wi in enumerate(blocks.PARAMETER_WEIGHTS):
        for j,wj in enumerate(blocks.THIRD_WEIGHTS):
            if wi+wj==-1:
                labels.append({"quadratic_index":i,"quadratic_name":exact.PARAMETERS[i],
                    "third_index":j,"third_weight":wj,
                    "v2_original_third_index":blocks.EXPECTED_KEPT[j],
                    "third_original_sha256":ring.digest(templates[j])})
    if len(labels)!=36:
        raise AssertionError("the complete E8 x W36 weight-minus-one block must have 36 columns")
    report["all_original_response_columns"]=labels
    report["response_coverage"]={"full_E8":True,"all_W36":True,
        "weight":-1,"columns":len(labels),"physical_seven_dimensional_subspace_not_substituted":True}
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
    report["phase"]="complete_weight_minus_one_original_responses"
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
            "fresh_original_checks":checks,"orbit_dimension_exact":2,
            "further_translation_orders_needed":False}
        report["completion"]="complete"
        return

    report["phase"]="original_rational_weight_minus_one_evaluation"
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
        "universal_N2G_nonmember_in_full_R8":certified,
        "orbit_dimension_lower_bound":3 if certified else 2,
        "orbit_dimension_exact":None,"further_translation_orders_computed":False,
        "fixed_test_pair_all_other_weights_excluded":False}
    report["completion"]="complete"


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
    value=x*x*(q.D()*q.D()).I()+(x*x*q.D()*q.D()).I()
    n1=N.expression(value);n2=N.expression(n1)
    same(n2,4*(q.D()*q.D()).I(),"two_original_translations_include_outer_and_inner_coordinate")
    same(N.expression(n2),ring.number(0),"artificial_second_derivative_stops_after_next_step")
    grade=blocks.ScalingGrading(ring)
    if set(grade.split(value))!={1} or set(grade.split(n2))!={-1}:
        raise AssertionError("new block weight minus one")
    checks["second_translation_maps_weight_one_to_minus_one"]=True
    nested=(x*(x*q*qb).I()).I()
    same(N.expression(N.expression(nested)),2*(q*qb).I().I(),
         "two_nested_original_primitives_pay_both_product_terms")
    shifted=(first.ExactShift(ring,2).expression(value)
             +first.ExactShift(ring,-2).expression(value)-2*value)/4
    same(shifted,n2,"independent_exact_shift_second_difference_matches_N_squared")
    same(N.expression(N.expression(value.I())),n2.I(),
         "two_translations_commute_with_the_common_right_primitive")

    checkpoint={"outcome":"nonmember_certified","universal_NG_nonmember_in_full_R8":True,
        "orbit_dimension_lower_bound":2,
        "dual_certificate":{"rational_nonmembership_certified":True,"control_columns":16,
            "modular_pivot_determinant":775740714,"modular_augmented_determinant":172056171,
            "modular_functional_target_value":548771152},
        "response_upper_bound":{"original_columns":20,"retained_original_columns":FIRST_RETAINED,
            "proved_true_response_dimension_upper_bound":16,
            "verified_original_dependency_count":4,
            "verified_original_dependencies_sha256":FIRST_DEPENDENCIES_SHA},
        "original_translation_target":{"order":1,"original_NG_sha256":FIRST_NG_SHA}}
    value0={"schema":first.SCHEMA,"completion":"complete",
        "github_repository":static.REPOSITORY,"github_run_id":FIRST_RUN,
        "github_sha":FIRST_COMMIT,"source_hashes":{"driver":{"sha256":FIRST_DRIVER_SHA}},
        "checkpoint":checkpoint}
    publication={"schema":"visible-new-mechanism-actions-v1","repository":static.REPOSITORY,
        "run_id":FIRST_RUN,"source_commit":FIRST_COMMIT,"lane":"g_first_translation",
        "outputs":[{"path":"artificial.json","bytes":FIRST_MAIN_BYTES,"sha256":FIRST_MAIN_SHA,
                    "raw_bytes":FIRST_MAIN_BYTES,"raw_sha256":FIRST_MAIN_SHA}],
        "source_files":{"topics/visible-flex-new-mechanism/scripts/literature_G_first_translation.py":
                        {"bytes":FIRST_DRIVER_BYTES,"sha256":FIRST_DRIVER_SHA}}}
    validate_previous_payloads(value0,publication,"artificial.json")
    checks["artificial_previous_completion_and_source_binding_accepted"]=True
    for label,mutate in (
        ("changed_frozen_NG_hash_rejected",
         lambda z:z["checkpoint"]["original_translation_target"]["original_NG_sha256"].update({"-4":"bad"})),
        ("incomplete_previous_research_rejected",lambda z:z.update({"completion":"resource_limit"})),
        ("old_representative_rank_without_true_minor_rejected",
         lambda z:z["checkpoint"]["dual_certificate"].update({"rational_nonmembership_certified":False})),
    ):
        damaged=copy.deepcopy(value0);mutate(damaged)
        try:
            validate_previous_payloads(damaged,publication,"artificial.json")
        except ValueError:
            checks[label]=True
        else:
            raise AssertionError(label)
    return {"checks":checks,"all_passed":all(checks.values()),
        "original_G_or_NG_read":False,"research_profile_evaluated":False,
        "old_or_new_research_response_columns_compiled":False}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only",action="store_true")
    parser.add_argument("--order",type=int,choices=(2,),default=2)
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
    parser.add_argument("--first-report",type=Path,default=FIRST_DIR/"G-first-translation.json")
    parser.add_argument("--first-publication",type=Path,default=FIRST_DIR/"receipt.json")
    parser.add_argument("--max-seconds",type=float,default=240)
    parser.add_argument("--memory-mib",type=int,default=1024)
    parser.add_argument("--max-degree",type=int,default=256)
    parser.add_argument("--max-operations",type=int,default=10000000)
    parser.add_argument("--points",type=int,default=24)
    parser.add_argument("--bump-power",type=int,default=8)
    parser.add_argument("--prime",type=int,default=2147483647)
    parser.add_argument("--max-main-bytes",type=int,default=90000)
    parser.add_argument("--max-full-report-bytes",type=int,default=2500000)
    args=parser.parse_args()
    if (min(args.max_seconds,args.memory_mib,args.max_degree,args.max_operations,args.points,
            args.max_main_bytes,args.max_full_report_bytes)<=0 or args.bump_power<8):
        parser.error("positive bounded budgets and bump power at least eight")
    if args.prime%4!=3 or args.points+1>=args.prime:
        parser.error("the checked prime must be 3 mod 4 and exceed query denominators")
    if not 10000<=args.max_main_bytes<100000:
        parser.error("small main report must reserve 10000..99999 bytes")
    if args.max_main_bytes+args.max_full_report_bytes>static.TOTAL_BYTES:
        parser.error("total published output ceiling")
    if not args.toy_only and not(os.environ.get("GITHUB_ACTIONS")=="true"
                                 and os.environ.get("GITHUB_REPOSITORY")==static.REPOSITORY):
        parser.error("genuine original-expression research only in this public repository Actions")
    started=time.monotonic()
    report={"schema":SCHEMA,"completion":"started","phase":"source_binding",
        "github_repository":os.environ.get("GITHUB_REPOSITORY"),
        "github_run_id":os.environ.get("GITHUB_RUN_ID"),"github_sha":os.environ.get("GITHUB_SHA"),
        "source_hashes":{},"completed_blocks":[],
        "scope":"only original order-two translation; complete new weight-minus-one response block",
        "limits":{"seconds":args.max_seconds,"memory_polling_mib":args.memory_mib,
            "max_degree":args.max_degree,"max_operations":args.max_operations,
            "main_bytes":args.max_main_bytes,"complete_report_bytes":args.max_full_report_bytes},
        "old_forcing_recompiled":False,"W_recompiled":False,"local_density_recompiled":False,
        "old_G_separation_reevaluated":False,"old_NG_separation_reevaluated":False,
        "old_weight_zero_columns_recomputed":False,"full_fourth_cost_paid":False,
        "ruling_paid":False,"finite_isometric_family_constructed":False}
    code=0
    try:
        report["source_hashes"]=source_identity()
        if args.toy_only:
            report["phase"]="small_artificial_order_two_and_previous_receipt_interfaces"
            report["toy"]=small_toy();report["completion"]="toy_passed"
        else:
            study(args,report,started)
    except (formal.CompilationBudgetExceeded,poly.PolynomialBudgetExceeded) as error:
        report["completion"]="resource_limit";report["error"]=str(error);code=2
    except Exception as error:
        report["completion"]="implementation_check_failed"
        report["error"]={"type":type(error).__name__,"message":str(error)};code=1
    if "translation" in report:
        report.setdefault("checkpoint",{})["original_translation_target"]=report["translation"]
    if "response_upper_bound" in report:
        upper=report["response_upper_bound"]
        report.setdefault("checkpoint",{})["response_upper_bound"]={
            "original_columns":upper["original_columns"],
            "retained_original_columns":upper["retained_original_columns"],
            "proved_true_response_dimension_upper_bound":upper["proved_true_response_dimension_upper_bound"],
            "verified_original_dependency_count":len(upper["verified_original_dependencies"]),
            "verified_original_dependencies_sha256":sha(canonical(upper["verified_original_dependencies"])),
            "complete_original_dependency_proofs_in_full_report":True}
    if "completed_G_input" in report:
        report.setdefault("checkpoint",{})["completed_G_input"]=report["completed_G_input"]
    if "completed_NG_input" in report:
        report.setdefault("checkpoint",{})["completed_NG_input"]=report["completed_NG_input"]
    if "input_regularity" in report:
        report.setdefault("checkpoint",{})["input_regularity"]=report["input_regularity"]
    positive=(report.get("checkpoint") or {}).get("same_coefficients_for_both_modes")
    if positive is not None and len(canonical(positive))>16000:
        report["positive_identity_coefficients"]=positive
        del report["checkpoint"]["same_coefficients_for_both_modes"]
        report["checkpoint"]["positive_coefficients"]={
            "count":len(positive),"sha256":sha(canonical(positive)),
            "complete_rational_coefficients_in_full_report":True}
    report["elapsed_seconds"]=time.monotonic()-started
    report["peak_rss_mib"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    written=static.publish_report(args.output,report,args.max_main_bytes,args.max_full_report_bytes)
    if written["completion"]=="output_limit":
        code=2
    print(json.dumps({"output":str(args.output),**written}),flush=True)
    return code

if __name__=="__main__":
    raise SystemExit(main())
