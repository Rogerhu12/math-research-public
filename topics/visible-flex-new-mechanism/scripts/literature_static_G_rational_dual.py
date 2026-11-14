#!/usr/bin/env python3
"""R117: one original static coefficient G against its complete weight-one R8.

Consumes the existing raw local export and published eight-column spanning
certificate. No word reduction, forcing compile, W restore or old NF target.
Only rank 7 plus a nonzero 8x8 rational minor is a negative certificate.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
import os
from pathlib import Path
import resource
import time

import literature_constrained_static_fourth as static

old=static.old
dual=static.dual
poly=dual.poly
colored=static.colored
exact=static.exact
formal=static.formal
blocks=static.blocks
SCHEMA="visible-flex-R117-static-G-original-rational-dual-v1"
STATIC_HELPER_SHA="814e1338679914b32542f8b360978281002ee02a2c4e8c03912aa40c876786f4"
POLY_SHA="6bf16dd5c6cc8157fd53b20b58b504a5c3ea56ade9db9b62a30d385e5e69fd22"
BLOCK_SHA="57d8a80b8344f42cd8594e7d117d29098991d1c392d3101264195eeb1a8533c4"
BLOCK_BYTES=13499
GEOMETRY_KEY=(1,3,0,0,0,0,0,0)
TARGET_HASHES={
    -4:"4608912701e99a514cff0dcb93b896200beeb6e3cbead9a70547b78e00d18c7a",
    -2:"042fc6bef63ef5e1c49b1403c88e4f3d728b9bcce183741a298b2fb2619bcd50"}
EXPECTED_PAIRS=((1,7),(1,17),(2,1),(2,12),(2,16),(2,35),(7,7),(7,17))
KEPT=(0,1,2,3,4,5,7)
ZERO_SHA="4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945"
MODES=(-4,-2)

def sha(data):
    return hashlib.sha256(data).hexdigest()

def sources():
    answer=static.current_sources()
    if answer["driver"]["sha256"]!=STATIC_HELPER_SHA:
        raise ValueError("explicitly rebind the finite input/report helper")
    answer["static_input_and_report_helper"]=answer.pop("driver")
    answer["driver"]=static.identity(__file__)
    answer["polynomial_evaluator"]=static.identity(poly.__file__)
    if answer["polynomial_evaluator"]["sha256"]!=POLY_SHA:
        raise ValueError("original rational evaluator changed")
    return answer

def load_G_and_bound(args,ring,report):
    templates,all_targets=static.load_bound_input(args,ring,report)
    raw=static.checked_bytes(args.block_receipt,100000)
    if len(raw)!=BLOCK_BYTES or sha(raw)!=BLOCK_SHA:
        raise ValueError("the exact public weight-one spanning report changed")
    receipt=json.loads(raw)
    if (receipt.get("schema")!=old.SCHEMA+"-block" or receipt.get("weight")!=1
        or receipt.get("github_sha")!=args.source_commit
        or receipt.get("source_hashes")!=report["source_hashes"]["original_producer_dependencies"]
        or receipt.get("true_response_dimension_upper_bound")!=7):
        raise ValueError("weight-one report scope/source mismatch")
    publication=json.loads(static.checked_bytes(args.publication_receipt,100000))
    entries=[x for x in publication.get("outputs",[]) if x.get("path")==args.block_receipt.name]
    if len(entries)!=1 or any(entries[0].get(k)!=v for k,v in (
        ("bytes",len(raw)),("sha256",sha(raw)),("raw_bytes",len(raw)),("raw_sha256",sha(raw)))):
        raise ValueError("the terminal publisher did not bind this exact block")
    labels=receipt["response_columns"]
    if len(labels)!=8 or [(x["quadratic_index"],x["third_index"]) for x in labels]!=list(EXPECTED_PAIRS):
        raise ValueError("all complete homogeneous control columns must be retained")
    enumerated=[(i,j) for i,wi in enumerate(blocks.PARAMETER_WEIGHTS)
        for j,wj in enumerate(blocks.THIRD_WEIGHTS) if wi+wj==1]
    if enumerated!=list(EXPECTED_PAIRS):
        raise ValueError("the true full-E8/W36 scaling decomposition changed")
    for label in labels:
        if (label["v2_original_third_index"]!=blocks.EXPECTED_KEPT[label["third_index"]]
            or label["third_original_sha256"]!=ring.digest(templates[label["third_index"]])):
            raise ValueError("an original bound third template changed")
    relations=receipt["verified_original_response_dependencies"]
    if (len(relations)!=1 or relations[0]["column"]!=6
        or relations[0]["coefficients"]!=[[1,"-1"],[3,"1"]]
        or relations[0]["fresh_original_zeros"]!={str(mode):ZERO_SHA for mode in MODES}):
        raise ValueError("the proved eight-to-seven original spanning relation changed")
    row=next((x for x in receipt["unresolved_geometry_coefficients"]
        if tuple(x["geometry_key"])==GEOMETRY_KEY),None)
    if row is None or row["original_modes_sha256"]!={str(k):v for k,v in TARGET_HASHES.items()}:
        raise ValueError("the exact G original identity was not published")
    grade=blocks.ScalingGrading(ring)
    targets={mode:grade.project(all_targets[mode].terms.get(GEOMETRY_KEY,ring.number(0)),1)
        for mode in MODES}
    if {mode:ring.digest(value) for mode,value in targets.items()}!=TARGET_HASHES:
        raise ValueError("original G differs from its published weight-one root")
    regularity=dual.reachable_jet_bound(ring,list(targets.values())+
        [templates[EXPECTED_PAIRS[i][1]] for i in KEPT])
    if regularity["maximum_input_jet"]>6:
        raise ValueError("raise the proven regularity scope explicitly before using higher jets")
    report["original_G"]={"geometry_key":list(GEOMETRY_KEY),
        "profile_affine_weight":1,"raw_target_sha256":{str(k):v for k,v in TARGET_HASHES.items()},
        "block_receipt":{"filename":args.block_receipt.name,"bytes":len(raw),"sha256":sha(raw)},
        "all_eight_original_columns":labels,"kept_original_column_indices":list(KEPT),
        "exact_spanning_relation":"column6=-column1+column3",
        "true_homogeneous_response_dimension_upper_bound":7,
        "original_relation_not_recompiled":True,"input_regularity":regularity,
        "only_linear_true_weight_projection_used":True,"word_rewriting_used":False}
    return templates,targets,labels

def evaluate_G(args,ring,templates,targets,labels,context,report):
    _,_,report["fixed_profiles"]=dual.fixed_profiles(context,args.bump_power)
    evaluator=poly.RawExpressionEvaluator(ring.p,context,context.colors)
    values={mode:evaluator.expression(value) for mode,value in targets.items()}
    points=[F(j,args.points+1) for j in range(1,args.points+1)]
    row_labels=[{"t":str(t),"xi":str(context.left+context.width*t),
        "mode":mode,"component":component}
        for t in points for mode in MODES for component in ("real","imaginary")]
    def rows_of(modes):
        return [v for t in points for mode in MODES for v in modes[mode].value(t)]
    target_values=rows_of(values)
    quadratics=exact.operator_basis(context)
    columns=[];column_report=[]
    for index in KEPT:
        ai,ti=EXPECTED_PAIRS[index]
        third=poly.EvaluatedThirdOperator(ring.p,context,templates[ti])
        # Direct original right primitives and complete outer/inner slot formula.
        response=blocks.full_response(context,third,quadratics[ai])
        columns.append(rows_of(response))
        column_report.append({"original_column_index":index,"quadratic_index":ai,
            "third_basis_index":ti,"v2_third_index":blocks.EXPECTED_KEPT[ti],
            "original_third_sha256":ring.digest(templates[ti]),
            "evaluated_mode_polynomials":{str(mode):{"sha256":response[mode].digest(),
                "degree":len(response[mode].coefficients)-1} for mode in MODES}})
        report["checkpoint"]={"completed_original_columns":len(columns),"total_original_columns":7,
            "negative_certificate_available":False}
        context.check(0)
    rows=[[column[i] for column in columns] for i in range(len(row_labels))]
    witness=poly.full_column_dual(rows,target_values,context.prime)
    if witness["rational_nonmembership_certified"]:
        witness["selected_evaluation_labels"]=[row_labels[i] for i in witness["selected_augmented_rows"]]
    return {"all_evaluation_labels":row_labels,"same_fixed_pair_for_every_column_and_mode":True,
        "matrix_rows":len(rows),"matrix_columns":7,
        "matrix_modular_values_sha256":sha(dual.canonical(rows)),
        "target_modular_values_sha256":sha(dual.canonical(target_values)),
        "target_mode_polynomials":{str(mode):{"sha256":values[mode].digest(),
            "degree":len(values[mode].coefficients)-1} for mode in MODES},
        "original_control_evaluation":column_report,"dual_certificate":witness}

def artificial_toys():
    answer={"rational_evaluator":poly.small_toys(),"static_input_and_report":static.small_toy()}
    limits=exact.Limits(seconds=30,nodes=5000,atoms=1000,terms=3000,rewrites=5000,memory_mib=256)
    ring=colored.ColoredRing(limits)
    a,b,c=(ring.color(x) for x in ("a","b","c"))
    template=a*(b.D()*c+b*c.D())
    context=poly.PolynomialContext(101,2,5,seconds=30,max_degree=40)
    x=context.x()
    context.colors={"q":x*x+context.number((0,1))*x,
                    "qbar":x*x-context.number((0,1))*x}
    third=poly.EvaluatedThirdOperator(ring.p,context,template)
    literal=lambda outer,first,second:outer*(first.D()*second+first*second.D())
    actual=blocks.full_response(context,third,lambda p,q:p*q)
    expected=blocks.reference_response(context,literal,lambda p,q:p*q)
    if any(actual[mode].key()!=expected[mode].key() for mode in MODES):
        raise AssertionError("artificial complete-phase formula and asymmetric exterior slot")
    answer["original_exterior_inner_slots_and_two_mode_factors"]=True
    answer["all_passed"]=True
    answer["research_target_or_profile_evaluated"]=False
    answer["public_DAG_consumed"]=False
    return answer

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only",action="store_true")
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
    parser.add_argument("--points",type=int,default=24)
    parser.add_argument("--bump-power",type=int,default=8)
    parser.add_argument("--prime",type=int,default=2147483647)
    parser.add_argument("--max-seconds",type=float,default=120)
    parser.add_argument("--memory-mib",type=int,default=1024)
    parser.add_argument("--max-degree",type=int,default=256)
    parser.add_argument("--max-operations",type=int,default=10000000)
    parser.add_argument("--max-main-bytes",type=int,default=90000)
    parser.add_argument("--max-full-report-bytes",type=int,default=2500000)
    args=parser.parse_args()
    if min(args.points,args.max_seconds,args.memory_mib,args.max_degree,args.max_operations,
        args.max_main_bytes,args.max_full_report_bytes)<=0 or args.bump_power<8:
        parser.error("positive bounded resources and bump power at least eight required")
    if args.points+1>=args.prime or args.prime%4!=3:
        parser.error("choose a prime congruent to 3 mod 4 larger than all evaluation denominators")
    if args.max_main_bytes<10000 or args.max_main_bytes>=100000:
        parser.error("main text must reserve 10000..99999 bytes")
    if args.max_main_bytes+args.max_full_report_bytes>static.TOTAL_BYTES:
        parser.error("reserve compressed report and main inside total published byte limit")
    if not args.toy_only and not(os.environ.get("GITHUB_ACTIONS")=="true"
        and os.environ.get("GITHUB_REPOSITORY")==static.REPOSITORY):
        parser.error("all genuine original-profile evaluation must run in this public Actions repository")
    start=time.monotonic();context=None;code=0
    report={"schema":SCHEMA,"completion":"started","phase":"source_binding",
        "scope":"original G weight-one universal operator membership, not all profiles or an exact flexible surface",
        "github_repository":os.environ.get("GITHUB_REPOSITORY"),
        "github_run_id":os.environ.get("GITHUB_RUN_ID"),"github_sha":os.environ.get("GITHUB_SHA"),
        "source_hashes":{},"completed_blocks":[],
        "limits":{"seconds":args.max_seconds,"memory_polling_mib":args.memory_mib,
            "polynomial_degree":args.max_degree,"operations":args.max_operations,
            "main_bytes":args.max_main_bytes,"complete_compressed_report_bytes":args.max_full_report_bytes},
        "all_derivative_weights_computed":False,"complete_U4_equals_R8_proved":False,
        "U4_quotient_nonzero_proved":False,"P0_or_ruling_paid":False,
        "finite_isometric_family_constructed":False,"rational_nonmembership_certified":False,
        "three_moments_imposed_on_the_test_pair":False,"all_circles_excluded":False,
        "fixed_pair_all_other_affine_weights_excluded":False,
        "word_rewriting_used_to_evaluate_values":False}
    try:
        report["source_hashes"]=sources()
        if args.toy_only:
            report["phase"]="small_artificial_interfaces"
            report["toy"]=artificial_toys();report["completion"]="toy_passed"
        else:
            limits=exact.Limits(args.max_seconds,400000,100000,150000,100000,args.memory_mib,8192)
            ring=colored.ColoredRing(limits)
            report["phase"]="bound_original_G_and_homogeneous_spanning_certificate"
            templates,targets,labels=load_G_and_bound(args,ring,report)
            remaining=args.max_seconds-(time.monotonic()-start)
            if remaining<=0:
                raise poly.PolynomialBudgetExceeded("budget exhausted before original evaluation")
            context=poly.PolynomialContext(args.prime,2,3,seconds=remaining,
                max_degree=args.max_degree,memory_mib=args.memory_mib,max_operations=args.max_operations)
            report["phase"]="seven_original_control_columns_and_rational_separating_minor"
            report["evaluation"]=evaluate_G(args,ring,templates,targets,labels,context,report)
            witness=report["evaluation"]["dual_certificate"]
            certified=witness["rational_nonmembership_certified"]
            report["rational_nonmembership_certified"]=certified
            report["checkpoint"]={"rational_nonmembership_certified":certified,
                "full_homogeneous_response_upper_bound":7,"dual_certificate":witness,
                "old_word_remainder_used_as_certificate":False,
                "universal_G_not_in_full_R8_by_true_weight_decomposition":certified,
                "fixed_test_pair_other_weights_excluded":False}
            report["interpretation"]=(
                "Only a nonzero 7/8 rational minor proves universal G not in the complete weight-one response and hence not in the graded universal R8. The exact characteristic-zero functional is defined from the original rational matrix by Cramer/cofactors, not by promoting printed modular coefficients. No such minor means inconclusive. The one finite-regularity polynomial pair is not a three-moment circle; other-weight cancellations on that fixed pair are not excluded.")
            report["completion"]="complete"
    except (formal.CompilationBudgetExceeded,poly.PolynomialBudgetExceeded) as error:
        report["completion"]="resource_limit";report["error"]=str(error);code=2
    except Exception as error:
        report["completion"]="implementation_check_failed"
        report["error"]={"type":type(error).__name__,"message":str(error)};code=1
        report["rational_nonmembership_certified"]=False
    report["elapsed_seconds"]=time.monotonic()-start
    report["peak_rss_mib"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    if context is not None:
        report["coefficient_arithmetic"]=context.coefficient_report()
    written=static.publish_report(args.output,report,args.max_main_bytes,args.max_full_report_bytes)
    if written["completion"]=="output_limit":
        code=2
    print(json.dumps({"output":str(args.output),**written}),flush=True)
    return code

if __name__=="__main__":
    raise SystemExit(main())
