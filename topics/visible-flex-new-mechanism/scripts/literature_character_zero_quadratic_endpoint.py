#!/usr/bin/env python3
"""One new R236 degree-two principal-part gate for the already-paid R234 H_E.

Only seven necessary original inputs are restored: C2 and old R126 columns
0,1,2,3,4,10.  No old seventeen first layers, cubic tail normalization, pure
queries, full H0, other weights, profile evaluation or response comparison.
Actual research is restricted to this public repository's GitHub Actions.
"""
from __future__ import annotations
from fractions import Fraction as F
import argparse
import json
import os
from pathlib import Path
import resource
import time

import literature_character_zero_endpoint_layer as first
import literature_endpoint_quadratic_principal as quadratic

pure,zero,head,literal=first.pure,first.zero,first.head,first.literal
colored,exact,formal,blocks=first.colored,first.exact,first.formal,first.blocks
canonical,sha=first.canonical,first.sha
REPOSITORY,TOPIC=first.REPOSITORY,first.TOPIC
SCHEMA="visible-flex-character-zero-quadratic-endpoint-principal-v1"
SOURCE_FIRST={"filename":"literature_character_zero_endpoint_layer.py","bytes":29604,
    "sha256":"bb7be8fc3fa6b98f3f69aca96e5145c6df1f3d581ea85d14aa7fb6ccfefe6a94"}
SOURCE_QUADRATIC={"filename":"literature_endpoint_quadratic_principal.py","bytes":21175,
    "sha256":"01efa75bbb691c802e211ddf08fc3804d657af73d53ce428f51ae8b1ef365215"}
OLD_COLUMNS=(0,1,2,3,4,10)
HE_COMBINATION={0:F(-1,8),1:F(-1,64),2:F(13,32),
                3:F(1,48),4:F(5,64),10:F(-1,32)}
HE_MIXED_SHA="346ea2a14c74e4a6d831b05288533609b08bf7776782c0964dd66ece9eda96b6"
R234={"run":"43699241372","commit":"ee9e2098c62392ddb709e7db26467bc225642d54",
    "lane":"character_zero_endpoint_layer",
    "receipt":{"filename":"receipt.json","bytes":49168,
        "sha256":"ea5c31ce431cff1f1765f04dd00ec14b26e6e624230d516485e7e994ea46a62c"},
    "result":{"filename":"character-zero-endpoint-layer.json","bytes":38943,
        "sha256":"577157ad38ca9744411167bd0fe865838df0360ee2564421b598a82f76fea26b"},
    "development":{"filename":"character-zero-endpoint-layer-development.json","bytes":8580,
        "sha256":"5e1f237e6c3ca3fb95149199449a95507682875f123afcbbbd84390637085403"},
    "old_in_memory_certificate":{"bytes":94085,
        "sha256":"bda761d579684cb2e28c0df7644bb244264094543c43e71079275a21f12062f0",
        "persisted":False},
    "published_first_layer_zero_sha256":
        "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
}


def source_identity():
    data=first.source_identity()
    if data.get("driver")!=SOURCE_FIRST:
        raise ValueError("the completed original endpoint input/helper source changed")
    data["completed_first_layer_driver"]=data.pop("driver")
    found=literal.identity(quadratic.__file__)
    if found!=SOURCE_QUADRATIC:
        raise ValueError("the reviewed new quadratic-principal helper changed")
    data["new_quadratic_principal_helper"]=found
    data["driver"]=literal.identity(__file__)
    return data


def bind_R234(directory,report):
    receipt,_=literal.read_small(directory/"receipt.json",R234["receipt"])
    if (receipt.get("schema")!="visible-new-mechanism-actions-metadata-only-v2"
        or receipt.get("repository")!=REPOSITORY
        or str(receipt.get("run_id"))!=R234["run"]
        or receipt.get("source_commit")!=R234["commit"]
        or receipt.get("lane")!=R234["lane"]
        or receipt.get("output_payloads_committed_or_uploaded") is not False
        or receipt.get("release_assets_created") is not False
        or receipt.get("machine_certificates_saved") is not False):
        raise ValueError("published completed R234 metadata-only receipt changed")
    for item in (SOURCE_FIRST,first.SOURCE_ENDPOINT):
        path="topics/visible-flex-new-mechanism/scripts/"+item["filename"]
        if receipt.get("source_files",{}).get(path)!={k:item[k] for k in ("bytes","sha256")}:
            raise ValueError("R234 publication does not bind its actual input/layer implementation")
    for spec in (R234["result"],R234["development"]):
        rows=[r for r in receipt.get("outputs",[]) if r.get("path")==spec["filename"]]
        expected={"bytes":spec["bytes"],"sha256":spec["sha256"],
            "raw_bytes":spec["bytes"],"raw_sha256":spec["sha256"],
            "payload_published":False}
        if len(rows)!=1 or any(rows[0].get(k)!=v for k,v in expected.items()):
            raise ValueError("the published old R234 output metadata changed")
    report["inputs"]["proved_R234_HE"]={**R234,
        "the_mathematical_identity_is_in_published_R234_not_inferred_from_metadata_alone":True,
        "C2_coefficient":"1",
        "old_R126_coefficients":[[j,str(HE_COMBINATION[j])] for j in OLD_COLUMNS],
        "whole_pure_zero_already_proved":True,"lambda_plus":"1",
        "specified_universal_first_layer_already_proved_zero":True,
        "first_layer_scope":"true weight0, canonical mixed -2, first f-up/g0 flat germ",
        "old_seventeen_first_layers_recomputed":False,
        "old_cubic_tail_normalization_repeated":False}


def restore_six_old_mixed(ring,W,selected,budget,report):
    quadratics=exact.operator_basis(ring)
    result={}
    records=[]
    for old_index,label in selected:
        j,a=label["third_index"],label["quadratic_index"]
        if (not 0<=j<36 or not 0<=a<8
            or label["quadratic_name"]!=exact.PARAMETERS[a]
            or blocks.THIRD_WEIGHTS[j]+blocks.PARAMETER_WEIGHTS[a]!=0
            or ring.digest(W[j])!=label["third_original_sha256"]):
            raise ValueError("a selected old response label or true weight changed")
        value=first.mixed_response(ring,colored.ThirdOperator(ring,W[j]),quadratics[a])
        if ring.digest(value)!=label["original_mode_sha256"]["-2"]:
            raise ValueError("necessary old mixed root failed its original R126 hash")
        result[old_index]=value
        records.append({"old_column":old_index,"quadratic":label["quadratic_name"],
            "W_index":j,"original_mixed_sha256":ring.digest(value),
            "original_terms":len(value.terms)})
        report["progress"]={"phase":"necessary_six_old_mixed_inputs",
            "completed":len(result),"required":6}
        budget.check()
    report["necessary_input_restore"]={"old_response_columns":6,"records":records,
        "C2_static_sum":1,"total_selected_complete_original_roots":7,
        "all_old_mixed_original_hashes_matched":True,"new_response_targets":0,
        "other_ten_R0_original_roots_restored":False,
        "pure_original_roots_restored":0,"old_original_profile_evaluations_repeated":False,
        "reason":"the old R126 portable DAG was not saved and metadata-only R234 archived no original roots"}
    return result


def actual(args,report):
    budget=literal.Budget(args.max_seconds,args.memory_mib,args.integer_bits)
    limits=exact.Limits(seconds=args.max_seconds,nodes=350000,atoms=100000,
        terms=args.max_terms,rewrites=args.max_IBP_calls,memory_mib=args.memory_mib,
        rational_bits=args.integer_bits)
    ring=colored.ColoredRing(limits)
    report["phase"]="bind_completed_input_sources_and_proved_HE"
    pure.bind_head_receipt(args.head_directory,report)
    bind_R234(args.first_layer_directory,report)
    all_labels=zero.read_R0_definition(args.R0_directory,report)
    lookup=dict(zip(zero.R0_KEEP,all_labels))
    if any(j not in lookup for j in OLD_COLUMNS):
        raise ValueError("the selected six columns are absent from the actual old basis")
    selected=[(j,lookup[j]) for j in OLD_COLUMNS]
    _,data=head.bind_input("static",args.static_directory,report)
    C2,W=first.restore_C2_and_W(ring,data,[label for _,label in selected],report)
    del data
    controls=restore_six_old_mixed(ring,W,selected,budget,report)
    del W
    HE=C2+sum((HE_COMBINATION[j]*controls[j] for j in OLD_COLUMNS),ring.number(0))
    if ring.digest(HE)!=HE_MIXED_SHA or len(HE.terms)!=2694:
        raise ValueError("the exact original H_E differs from R234's fresh difference")
    report["HE_original"]={"mode":-2,"true_weight":0,"original_terms":len(HE.terms),
        "original_sha256":ring.digest(HE),
        "definition":"C2 - R0/8 - R1/64 + 13R2/32 + R3/48 + 5R4/64 - R10/32",
        "old_R126_column_numbering":True,
        "pure_zero_first_layer_zero_and_lambda_one_inherited_from_R234":True}
    report["phase"]="one_new_quadratic_layer_and_finite_principal_part"
    value,mapper,tails,series,scan=quadratic.compute_one(ring,HE,args,budget)
    rows=quadratic.vector_rows(value)
    raw_series=mapper.original_rows(series)
    is_zero=not value
    report["actual_reachable_DAG"]=scan
    report["proved_finite_precision"]=mapper.plan
    report["new_quadratic_layer"]={
        "raw_principal_coefficient_count":len(series),
        "raw_principal_coefficients_sha256":quadratic.digest(raw_series),
        "raw_mapper_statistics":mapper.stats,
        "true_quadratic_tail_statistics":tails.stats,
        "new_quadratic_word_statistics":dict(tails.words.stats),
        "true_quadratic_conversion_count":len(tails.records),
        "true_quadratic_conversion_records_sha256":quadratic.digest(tails.records)}
    report["principal_part"]={
        "definition":"pp_(t<0) of t^4 times the p^-2 local-degree-two coefficient of this H_E",
        "exact_zero":is_zero,"complete_row_count":len(rows),
        "complete_row_sha256":quadratic.digest(rows),
        "row_order":["negative_t_power","c_integer_power","sorted_b_Taylor_indices",
                     "anchor_x_power","true_negative_right_primitive_word"],
        "exact_nonzero_witness":None if is_zero else rows[0],
        "all_words_use_actual_coupled_q_qbar_tails":True,
        "all_exterior_anchor_profile_jets_zero_only_after_word_normalization":True,
        "fixed_circle_tail_values_evaluated":False,
        "principal_part_representative_is_not_a_full_period_value":True}
    # A compact full vector is included in stdout when it fits; a larger vector
    # remains in the in-memory proof. One exact nonzero row already decides the
    # stated one-target universal coefficient test, not a response-class test.
    if len(canonical(rows))<=24000:
        report["principal_part"]["complete_small_row_vector"]=rows
    else:
        report["principal_part"]["complete_small_row_vector"]=None
        report["principal_part"]["full_vector_in_memory_certificate_only"]=True
    report["decision"]={
        "outcome":"universal_quadratic_principal_part_zero" if is_zero
                  else "this_representative_has_a_nonzero_universal_principal_part",
        "one_target_only":"published R234 H_E, true-weight0 canonical mixed -2",
        "quadratic_germ_gate_paid_for_every_declared_germ_if_platform_passes":is_zero,
        "raw_platform_P2_second_derivative_evaluated":False,
        "specific_legal_analytic_circle_supplied":False,
        "other_endpoint_or_internal_range_conditions_evaluated":False,
        "lambda_plus_factorization_proved":False,
        "whole_response_affine_class_excluded":False,
        "nonzero_result_excludes_a_fixed_circle":False,
        "other_weights_compared":False,
        "scope":"first f-up/g0 only; c>0 and universal finite log-amplitude jets; no independent tail assignment"}
    certificate={"schema":SCHEMA+"-in-memory-proof","source_hashes":report["source_hashes"],
        "input_bindings":report["inputs"],"HE_original":report["HE_original"],
        "actual_reachable_DAG":scan,"finite_precision":mapper.plan,
        "original_principal_coefficient_records":raw_series,
        "all_new_quadratic_tail_conversion_records":tails.records,
        "complete_principal_part_rows":rows,"decision":report["decision"]}
    raw=canonical(certificate)
    if len(raw)>args.max_certificate_bytes:
        raise literal.Limit("new in-memory quadratic principal-part proof byte ceiling")
    report["reproducible_certificate"]={"bytes":len(raw),"sha256":sha(raw),"persisted":False}
    report.update(completion="complete",phase="complete_one_HE_quadratic_endpoint_principal_part",
        complete_quadratic_gate=True,
        new_scientific_targets=1,new_degree_two_targets=1,
        old_seventeen_first_layers_recomputed=False,old_cubic_normalizations_repeated=0,
        old_pure_queries_reevaluated=0,new_profile_evaluations=0,new_N_contractions=0,
        complete_H0_kernel_recomputed=False,new_response_comparison_performed=False,
        exact_integer_operations=budget.operations,maximum_integer_bits=budget.maximum_bits,
        all_full_period_and_joint_ruling_goals_remain_unpaid=True,task_complete=False)


def toy_only(args):
    budget=literal.Budget(args.max_seconds,args.memory_mib,args.integer_bits)
    limits=exact.Limits(seconds=args.max_seconds,nodes=25000,atoms=5000,terms=10000,
        rewrites=20000,memory_mib=args.memory_mib,rational_bits=args.integer_bits)
    ring=colored.ColoredRing(limits)
    checks=quadratic.artificial_checks(ring,budget,args)
    if not all(checks.values()):
        raise AssertionError("new quadratic endpoint artificial interfaces failed: "+str(checks))
    return {"checks":checks,"all_passed":True,"real_inputs_read":False,
        "old_development_suites_repeated":False,"scientific_HE_evaluated":False,
        "only_new_degree_two_series_tail_and_precision_interfaces":True}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only",action="store_true")
    parser.add_argument("--output",type=Path,help="runner temporary summary only, no payload publication")
    parser.add_argument("--static-directory",type=Path,default=TOPIC/"notes"/head.INPUTS["static"]["directory"])
    parser.add_argument("--R0-directory",type=Path,default=TOPIC/"notes/actions-43649525432-1-g_first_translation")
    parser.add_argument("--head-directory",type=Path,default=TOPIC/"notes/actions-43681388902-1-character_head_zero")
    parser.add_argument("--first-layer-directory",type=Path,default=TOPIC/"notes/actions-43699241372-1-character_zero_endpoint_layer")
    parser.add_argument("--max-seconds",type=float,default=240)
    parser.add_argument("--memory-mib",type=int,default=1024)
    parser.add_argument("--integer-bits",type=int,default=8192)
    parser.add_argument("--max-profile-jet",type=int,default=8)
    parser.add_argument("--max-terms",type=int,default=100000)
    parser.add_argument("--max-IBP-calls",type=int,default=300000)
    parser.add_argument("--max-cache-entries",type=int,default=250000)
    parser.add_argument("--max-summary-bytes",type=int,default=95000)
    parser.add_argument("--max-certificate-bytes",type=int,default=8000000)
    args=parser.parse_args()
    if min(args.max_seconds,args.memory_mib,args.integer_bits,args.max_profile_jet,
           args.max_terms,args.max_IBP_calls,args.max_cache_entries,args.max_certificate_bytes)<=0:
        parser.error("all declared budgets must be positive")
    if not 16000<=args.max_summary_bytes<100000:
        parser.error("summary budget must be at least16KB and below100KB")
    if not args.toy_only and not (os.environ.get("GITHUB_ACTIONS")=="true"
                                  and os.environ.get("GITHUB_REPOSITORY")==REPOSITORY):
        parser.error("actual endpoint research runs only in this public repository Actions")
    started=time.monotonic()
    report={"schema":SCHEMA,"completion":"started","phase":"source_binding",
        "github_repository":os.environ.get("GITHUB_REPOSITORY"),
        "github_run_id":os.environ.get("GITHUB_RUN_ID"),"github_sha":os.environ.get("GITHUB_SHA"),
        "inputs":{},"scope":"one H_E degree-two endpoint principal part, not a response or fixed-circle membership test",
        "recomputable_payload_publication_permitted":False}
    code=0
    try:
        report["source_hashes"]=source_identity()
        if args.toy_only:
            report["development"]=toy_only(args)
            report.update(completion="complete",phase="new_artificial_quadratic_endpoint_interfaces_only")
        else:
            actual(args,report)
    except (literal.Limit,formal.CompilationBudgetExceeded,MemoryError) as error:
        if "decision" in report:
            report["uncertified_partial_decision_diagnostic"]=report.pop("decision")
        report.update(completion="resource_limit",error=str(error),
            complete_quadratic_gate=False,partial_is_not_a_zero_decision=True,
            partial_state_persistence_claimed=False)
        code=2
    except Exception as error:
        if "decision" in report:
            report["uncertified_partial_decision_diagnostic"]=report.pop("decision")
        report.update(completion="implementation_check_failed",
            error={"type":type(error).__name__,"message":str(error)},
            complete_quadratic_gate=False)
        code=1
    report["elapsed_seconds"]=time.monotonic()-started
    report["peak_rss_mib"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    body=canonical(report)+b"\n"
    if len(body)>args.max_summary_bytes:
        # The exact decision/witness remains readable even when provenance text
        # hits the user-set output cap. No vector or scientific work is rerun.
        complete_before_output_limit=(report.get("completion")=="complete" and report.get("decision") is not None)
        report={"schema":SCHEMA,"completion":"summary_output_limit",
            "scientific_computation_complete_before_summary_limit":complete_before_output_limit,
            "full_summary_bytes":len(body),"full_summary_sha256":sha(body),
            "github_run_id":report["github_run_id"],"github_sha":report["github_sha"],
            "source_hashes":report.get("source_hashes"),
            "decision":report.get("decision"),"principal_part":report.get("principal_part"),
            "actual_reachable_DAG":report.get("actual_reachable_DAG"),
            "proved_finite_precision":report.get("proved_finite_precision"),
            "elapsed_seconds":report["elapsed_seconds"],"peak_rss_mib":report["peak_rss_mib"],
            "reproducible_certificate":report.get("reproducible_certificate"),
            "payload_saved":False}
        if isinstance(report.get("principal_part"),dict):
            report["principal_part"].pop("complete_small_row_vector",None)
        body=canonical(report)+b"\n"
        code=2
    if len(body)>args.max_summary_bytes:
        raise ValueError("minimal quadratic summary exceeds the declared cap")
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_bytes(body)
    if report.get("decision") is not None:
        print("MATHEMATICAL_RESULT "+json.dumps({
            "decision":report["decision"],"principal_part":report["principal_part"],
            "actual_reachable_DAG":report["actual_reachable_DAG"],
            "finite_precision":report["proved_finite_precision"]},
            sort_keys=True,separators=(",",":")),flush=True)
    print(body.decode().rstrip(),flush=True)
    print(json.dumps({"summary_bytes":len(body),"summary_sha256":sha(body),
        "payload_publication_permitted":False},sort_keys=True),flush=True)
    raise SystemExit(code)


if __name__=="__main__":
    main()
