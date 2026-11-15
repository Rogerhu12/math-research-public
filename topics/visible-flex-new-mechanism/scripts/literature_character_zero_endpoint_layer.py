#!/usr/bin/env python3
"""One new weight-zero universal first-endpoint-layer gate (R230).

Restore only missing R126 mixed roots, extract the same normalized static C2,
and form the already-proved pure-zero H. Map only local degree one; normalize
only its cubic true-tail coefficients. Consume three STORED R116 values to
also compare against the pure kernel inside weight zero.
No actual circle, independent tail assignment, old full NF or profile query.
Scientific execution is restricted to this public repository's Actions.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as F
import json
import os
from pathlib import Path
import resource
import time

import literature_character_zero_pure_readout as pure
import literature_endpoint_first_layer as endpoint

zero,head,literal=pure.zero,pure.head,pure.literal
colored,exact,formal,blocks=pure.colored,pure.exact,pure.formal,pure.blocks
canonical,sha=pure.canonical,pure.sha
REPOSITORY,TOPIC=pure.REPOSITORY,pure.TOPIC
SCHEMA="visible-flex-character-zero-first-endpoint-layer-v1"
SOURCE_PURE={"filename":"literature_character_zero_pure_readout.py","bytes":29283,
    "sha256":"8d99414bda0a9bf61925f74e5378bfe80532fc8d9b9d35d6cc73625f8f15f7d1"}
SOURCE_ENDPOINT={"filename":"literature_endpoint_first_layer.py","bytes":11829,
    "sha256":"cf14e26c215bd93feb43dc4b56b8ecdcf9f9013084236e772229404eb9401b69"}
C2_MIXED_SHA="b2112caa38759e16999c782934dadf09f11770f4deb24938b22ae21e9640702f"
H_COMBINATION={0:F(1,48),2:F(11,64),3:F(-13,96)}
R201={
    "run":"43683171512","commit":"8c1ab4bab5763273e1004734a9582e3e9d697f9a",
    "lane":"character_zero_pure_readout","receipt_bytes":45729,
    "receipt_sha256":"0d926d181f6e607af71a59f62cb83cb187e7a9b705508308ffb56adf16472d4f",
    "result_name":"character-zero-pure-readout.json","result_bytes":24340,
    "result_sha256":"1fd475ffeaf62258132ac7d938b4f563f7401f2db0c38e78403f4c9de39b239b",
}
M8={
    "run":"43646543691","commit":"f0652a013fe546778300f0213e659f63ab96ed07",
    "lane":"full_m8_tail_response_projection","schema":"visible-flex-full-m8-pure-tail-R8-projection-v1",
    "main":{"filename":"full-m8-tail-response.json","bytes":9591,
        "sha256":"7237cadaac3c4581862d8aee86b94692f0e2436ab7fdb7e393c7b721125d61a7"},
    "receipt":{"filename":"receipt.json","bytes":31399,
        "sha256":"640bf2e0f17bfa635dc688581a192855f372bc7aa840c0ad97614d8696e59de1"},
    "artifact":{"filename":"full-m8-tail-response-certificate.json.gz",
        "stored_bytes":44576,"stored_sha256":"b0859868f2db2a08ca1b2831e5ab010840eed8e7ebda01fca49d598822d147a4",
        "raw_bytes":274274,"raw_sha256":"a8b5577903e419d2eabe2c327c2c721401acea2d0845017f86c260b2ddb8c36c"},
    "driver":{"filename":"literature_full_m8_tail_response_projection.py","bytes":32096,
        "sha256":"e66bf0d2f41570526d5e6b05aedc28118a18a492a299e097d341cc71e804e345"},
}
PURE_ROWS=((0,32),(1,31),(2,30))


def source_identity():
    data=pure.source_identity()
    if data["driver"]!=SOURCE_PURE:
        raise ValueError("the completed pure identity source changed")
    data["published_pure_identity_driver"]=data.pop("driver")
    found=literal.identity(endpoint.__file__)
    if found!=SOURCE_ENDPOINT:
        raise ValueError("the new first-layer module differs from the reviewed source")
    data["new_first_layer_module"]=found
    data["driver"]=literal.identity(__file__)
    return data


def bind_pure_identity(directory,report):
    spec={"bytes":R201["receipt_bytes"],"sha256":R201["receipt_sha256"]}
    receipt,_=literal.read_small(directory/"receipt.json",spec)
    if (receipt.get("schema")!="visible-new-mechanism-actions-metadata-only-v2"
        or receipt.get("repository")!=REPOSITORY
        or str(receipt.get("run_id"))!=R201["run"]
        or receipt.get("source_commit")!=R201["commit"]
        or receipt.get("lane")!=R201["lane"]
        or receipt.get("output_payloads_committed_or_uploaded") is not False
        or receipt.get("release_assets_created") is not False
        or receipt.get("machine_certificates_saved") is not False):
        raise ValueError("published R201 metadata-only source changed")
    path="topics/visible-flex-new-mechanism/scripts/"+SOURCE_PURE["filename"]
    if receipt.get("source_files",{}).get(path)!={k:SOURCE_PURE[k] for k in ("bytes","sha256")}:
        raise ValueError("R201 receipt does not bind its actual source")
    rows=[r for r in receipt.get("outputs",[]) if r.get("path")==R201["result_name"]]
    wanted={"bytes":R201["result_bytes"],"sha256":R201["result_sha256"],
            "raw_bytes":R201["result_bytes"],"raw_sha256":R201["result_sha256"],
            "payload_published":False}
    if len(rows)!=1 or any(rows[0].get(k)!=v for k,v in wanted.items()):
        raise ValueError("R201 result identity changed")
    report["inputs"]["R201_pure_identity"]={**R201,
        "identity_from_published_R201_not_from_metadata_alone":True,
        "H_C2_plus_old_response_coefficients":[[i,str(v)] for i,v in sorted(H_COMBINATION.items())],
        "H_universal_pure_zero_already_proved":True,"H_lambda_plus":"1",
        "old_pure_identity_recomputed":False}


def bind_stored_pure_rows(directory,labels,report):
    main,raw=literal.read_small(directory/M8["main"]["filename"],M8["main"])
    receipt,_=literal.read_small(directory/"receipt.json",M8["receipt"])
    # This exact legacy main had no github_repository key; its fixed bytes and
    # the real publisher receipt provide the repository identity, not a fake field.
    if (main.get("schema")!=M8["schema"] or main.get("completion")!="complete"
        or str(main.get("github_run_id"))!=M8["run"] or main.get("github_sha")!=M8["commit"]
        or main.get("source_hashes",{}).get("driver")!=M8["driver"]
        or main.get("complete_certificate")!=M8["artifact"]):
        raise ValueError("completed old m8 response main changed")
    if (receipt.get("schema")!="visible-new-mechanism-actions-v1"
        or receipt.get("repository")!=REPOSITORY or str(receipt.get("run_id"))!=M8["run"]
        or receipt.get("source_commit")!=M8["commit"] or receipt.get("lane")!=M8["lane"]):
        raise ValueError("completed m8 publisher identity changed")
    key="topics/visible-flex-new-mechanism/scripts/"+M8["driver"]["filename"]
    if receipt.get("source_files",{}).get(key)!={k:M8["driver"][k] for k in ("bytes","sha256")}:
        raise ValueError("m8 publisher source differs")
    outputs=literal.publication_outputs(receipt)
    for name,wanted in (
        (M8["main"]["filename"],{"bytes":len(raw),"sha256":sha(raw),
             "raw_bytes":len(raw),"raw_sha256":sha(raw)}),
        (M8["artifact"]["filename"],{"bytes":M8["artifact"]["stored_bytes"],
             "sha256":M8["artifact"]["stored_sha256"],"raw_bytes":M8["artifact"]["raw_bytes"],
             "raw_sha256":M8["artifact"]["raw_sha256"]})):
        if any(outputs.get(name,{}).get(k)!=v for k,v in wanted.items()):
            raise ValueError("old m8 output size/hash binding changed")
    data=literal.checked_gzip(directory/M8["artifact"]["filename"],M8["artifact"])
    block=data.get("exact_weight_blocks",{}).get("0",{})
    if (data.get("schema")!=M8["schema"]+"-certificate"
        or data.get("source_hashes")!=main["source_hashes"]
        or len(data.get("columns",[]))!=288
        or block.get("exact_rank_over_Q")!=3
        or tuple(tuple(r["pivot"]) for r in block.get("pivot_records",[]))!=PURE_ROWS):
        raise ValueError("the completed three old weight-zero pivots changed")
    columns=data["columns"];values=[];bindings=[]
    for old_index,label in zip(zero.R0_KEEP,labels):
        matches=[row for row in columns
            if row["quadratic_index"]==label["quadratic_index"]
            and row["original_third_sha256"]==label["third_original_sha256"]]
        if len(matches)!=1:
            raise ValueError("old pure coordinates must match the actual original W hash")
        row=matches[0]
        if (row["response_weight"]!=0 or row["third_index"]!=label["third_index"]
            or row["quadratic_name"]!=label["quadratic_name"]
            or row["index"]!=8*row["third_index"]+row["quadratic_index"]
            or sha(canonical(row["complete_polynomial"]))!=row["complete_polynomial_sha256"]):
            raise ValueError("old response label/polynomial identity changed")
        poly={(r["c_power"],r["r_power"]):F(r["coefficient"]) for r in row["complete_polynomial"]}
        values.append([poly.get(k,F(0)) for k in PURE_ROWS])
        bindings.append({"R126_old_column":old_index,"R116_global_column":row["index"],
            "original_third_sha256":row["original_third_sha256"],
            "old_complete_polynomial_sha256":row["complete_polynomial_sha256"],
            "stored_pure_coordinates":[str(poly.get(k,F(0))) for k in PURE_ROWS]})
    report["inputs"]["three_stored_pure_queries"]={**M8,
        "rows":[list(k) for k in PURE_ROWS],"column_bindings":bindings,
        "all_values_read_from_the_completed_certificate":True,
        "no_polynomial_profile_evaluation":True,"old_elimination_repeated":False,
        "sufficient_on_weight_zero_R_only_by_R116_and_R201":True}
    return values


def restore_C2_and_W(ring,data,labels,report):
    records=data["local_roots"]
    if Counter(r["mode"] for r in records)!=Counter({-4:197,-2:197}):
        raise ValueError("complete static source coverage changed")
    rows=[r for r in records if r["mode"]==-2]
    states=[]
    for row in rows:
        state,jets=head.split_key(row["geometry_key"])
        if any(jets):
            raise ValueError("static input unexpectedly contains a geometric derivative")
        states.append(state)
    if len(set(states))!=197:
        raise ValueError("duplicate static state key")
    coordinates,reference=head.constrained.reference_coordinates()
    weights=pure.combine_normalization_rows(rows,states,coordinates,
        {2:(0,2,0,0)},head.constrained.BASIS_STATES)[2]
    needed_W=sorted({r["third_index"] for r in labels})
    names=set(weights)|{"W"+str(j) for j in needed_W}
    roots=head.subset_decode(ring,data,names)
    raw=sum((c*roots[name] for name,c in sorted(weights.items())),ring.number(0))
    C2=blocks.ScalingGrading(ring).project(raw,0)
    if ring.digest(C2)!=C2_MIXED_SHA:
        raise ValueError("the same Gamma-normalized C2 mixed root differs from R196 stdout")
    report["C2_original_restore"]={
        "normal_index":2,"family":"F0","state_key":[0,2,0,0],"true_weight":0,
        "mode":-2,"same_Gamma_as_R196":True,"original_mode_sha256":ring.digest(C2),
        "original_terms":len(C2.terms),"raw_combination_sha256":ring.digest(raw),
        "raw_static_combination":[[name,str(c)] for name,c in sorted(weights.items())],
        "reference_data_sha256":sha(canonical(reference)),"new_projected_static_sums":1,
        "other_196_normal_roots_recomputed":False,"pure_root_recomputed":False}
    return C2,{j:roots["W"+str(j)] for j in needed_W}


def mixed_response(ring,third,quadratic):
    """Only the -2 raw component of frozen R78 blocks.full_response."""
    q,qb=ring.color("q"),ring.color("qbar")
    a,c=quadratic(q,q),quadratic(qb,qb)
    taqq=third(a,q,q);tqqa=third(q,q,a);tqqq=third(q,q,q)
    aq_tqqq=quadratic(q,tqqq)
    return (-taqq/4-third(c,q,q)/8-third(a,qb,qb)/8
        +(third(q,qb,a)+third(qb,q,a)-tqqa-third(q,q,c)
          +aq_tqqq+quadratic(q,third(q,qb,qb))
          -quadratic(q,third(qb,q,q))-quadratic(qb,tqqq))/4)


def restore_old_mixed(ring,W,labels,budget,report):
    quadratics=exact.operator_basis(ring)
    result=[];records=[]
    for old_index,label in zip(zero.R0_KEEP,labels):
        j,a=label["third_index"],label["quadratic_index"]
        if (not 0<=j<36 or not 0<=a<8 or label["quadratic_name"]!=exact.PARAMETERS[a]
            or blocks.THIRD_WEIGHTS[j]+blocks.PARAMETER_WEIGHTS[a]!=0
            or ring.digest(W[j])!=label["third_original_sha256"]):
            raise ValueError("the missing R0 original input label changed")
        value=mixed_response(ring,colored.ThirdOperator(ring,W[j]),quadratics[a])
        if ring.digest(value)!=label["original_mode_sha256"]["-2"]:
            raise ValueError("restored mixed R126 original hash mismatch at old "+str(old_index))
        result.append(value)
        records.append({"old_column":old_index,"quadratic":label["quadratic_name"],
            "W_index":j,"original_mixed_sha256":ring.digest(value),"original_terms":len(value.terms)})
        report["progress"]={"phase":"restore_missing_old_mixed_inputs","completed":len(result),"required":16}
        budget.check()
    report["old_mixed_input_restore"]={"columns":16,"records":records,
        "all_old_raw_mode_hashes_matched":True,"pure_roots_restored":0,
        "new_response_targets":0,"old_full_NF_or_rank_repeated":False,
        "old_actual_profile_evaluations_repeated":False,
        "reason":"R126 had no portable original response DAG; later metadata-only runs archived no roots"}
    return result


def add_row(row,source,amount):
    for k,v in source.items():
        endpoint.sparse_add(row,k,amount*v)


def map_columns(ring,columns,args,budget,report):
    first=endpoint.FirstLayer(ring,budget,args.max_terms,args.max_cache_entries)
    tail=endpoint.CubicTailMap(ring,budget,args.max_IBP_calls,args.max_terms,args.max_cache_entries)
    vectors=[];conversions=[]
    for index,expression in enumerate(columns):
        for monomial in expression.terms:
            degrees=Counter()
            for atom in monomial[1]:
                degrees.update(ring.atom_color_degree(atom))
            if set(degrees)-{"q","qbar"} or sum(degrees.values())!=4:
                raise ValueError("new target is not a complete canonical quartic root")
        start_records=len(tail.records)
        pair=first.expression(expression)
        value=tail.layer(pair)
        vectors.append(value)
        conversions.append({"column":index,"original_mixed_sha256":ring.digest(expression),
            "original_terms":len(expression.terms),"raw_linear_operator_terms":len(pair[1]),
            "raw_linear_coefficients_sha256":endpoint.digest(endpoint.expression_rows(pair[1],ring)),
            "first_layer_word_rows":len(value),"first_layer_sha256":endpoint.digest(endpoint.vector_rows(value)),
            "new_cubic_coefficient_records":[start_records,len(tail.records)],
            "raw_zero_degree_polynomial_sha256":endpoint.digest(endpoint.expression_rows(pair[0],ring)),
            "degree_zero_tail_bound_from_existing_canonical_theory_not_new_NF":True})
        report["progress"]={"phase":"new_exact_endpoint_layers","completed":index+1,"required":len(columns),
            "new_cubic_normalizations":len(tail.records)}
        budget.check()
    report["new_first_layer_map"]={"columns":len(columns),"conversions":conversions,
        "raw_mapper_statistics":first.stats,"cubic_tail_statistics":tail.stats,
        "cubic_word_statistics":dict(tail.words.stats),
        "cubic_coefficients_recorded":len(tail.records),"old_quartic_NF_repeated":False}
    return vectors,first,tail,conversions


def numeric_vectors(vectors,pure_values=None):
    labels=sorted(set().union(*(set(v) for v in vectors)))
    if pure_values is not None:
        labels += [("stored_pure_query",)+key for key in PURE_ROWS]
    index={key:i for i,key in enumerate(labels)}
    numeric=[{index[k]:c for k,c in value.items()} for value in vectors]
    if pure_values is not None:
        for column,values in zip(numeric[:-1],pure_values):
            for key,c in zip(PURE_ROWS,values):
                if c:
                    column[index[("stored_pure_query",)+key]]=c
        # The target H is already universally pure zero by R201.
    return numeric,labels


def serialize_decision(result,row_labels,column_labels):
    member="coefficients" in result
    out={"outcome":"member" if member else "nonmember",
         "comparison_rank":result["comparison_rank"],"augmented_rank":result["augmented_rank"],
         "scope":"new universal endpoint table in true weight zero only"}
    if member:
        coefficients=result["coefficients"]
        out["H_layer_equals_response_combination"]=[
            {"column":i,"R126_old_column":column_labels[i]["old_column"],"coefficient":str(c)}
            for i,c in sorted(coefficients.items())]
        out["exact_sum_of_all_new_column_representatives_zero"]=True
    else:
        out["exact_universal_row_dual"]=[
            {"row_id":i,"row_label":row_labels[i],"coefficient":str(c)}
            for i,c in sorted(result["dual"].items())]
        out["dual_values_all_17_original_columns"]=list(map(str,result["dual_values_all_columns"]))
        out["dual_support_bound"]=result["dual_support_bound"]
        out["not_a_fixed_circle_tau_evaluation"]=True
    return out


def actual(args,report):
    budget=literal.Budget(args.max_seconds,args.memory_mib,args.integer_bits)
    limits=exact.Limits(seconds=args.max_seconds,nodes=350000,atoms=100000,
        terms=args.max_terms,rewrites=args.max_IBP_calls,memory_mib=args.memory_mib,
        rational_bits=args.integer_bits)
    ring=colored.ColoredRing(limits)
    report["phase"]="bind_completed_sources_and_old_coordinates"
    pure.bind_head_receipt(args.head_directory,report)
    bind_pure_identity(args.pure_identity_directory,report)
    labels=zero.read_R0_definition(args.R0_directory,report)
    old_pure=bind_stored_pure_rows(args.stored_pure_directory,labels,report)
    _,data=head.bind_input("static",args.static_directory,report)
    C2,W=restore_C2_and_W(ring,data,labels,report);del data
    controls=restore_old_mixed(ring,W,labels,budget,report);del W
    old_to_new={old:i for i,old in enumerate(zero.R0_KEEP)}
    H=C2+sum((c*controls[old_to_new[i]] for i,c in H_COMBINATION.items()),ring.number(0))
    columns=controls+[H]
    column_labels=[{"kind":"weight_zero_response","old_column":i} for i in zero.R0_KEEP]
    column_labels.append({"kind":"R201_H","universal_pure_zero":True,"lambda_plus":"1"})
    report["column_order"]=column_labels
    report["H_original"]={"mode":-2,"sha256":ring.digest(H),"terms":len(H.terms),
        "definition":"C2 + R(old0)/48 + 11 R(old2)/64 - 13 R(old3)/96",
        "pure_identity_used_from_R201_not_recomputed":True}
    report["phase"]="new_first_layer_only"
    vectors,first,tail,conversions=map_columns(ring,columns,args,budget,report)
    wide,wide_labels=numeric_vectors(vectors)
    narrow,narrow_labels=numeric_vectors(vectors,old_pure)
    wide_result=pure.decide_projection(wide,budget)
    narrow_result=pure.decide_projection(narrow,budget)
    decisions={"all_weight_zero_responses":serialize_decision(wide_result,wide_labels,column_labels),
        "weight_zero_pure_kernel":serialize_decision(narrow_result,narrow_labels,column_labels)}
    calls=tail.words.run_primitive_calls
    fresh_cache={}
    for name,result in (("all_weight_zero_responses",wide_result),("weight_zero_pure_kernel",narrow_result)):
        if "coefficients" not in result:
            continue
        coefficients=result["coefficients"];key=tuple(sorted(coefficients.items()))
        if key not in fresh_cache:
            difference=H-sum((c*controls[i] for i,c in coefficients.items()),ring.number(0))
            remaining=args.max_IBP_calls-calls
            if remaining<=0:
                raise literal.Limit("total new cubic rewrite budget before fresh difference")
            fresh,fmapper,ftail,_=endpoint.original_first_layer(
                ring,difference,args,budget,calls=remaining)
            calls+=ftail.words.run_primitive_calls
            if fresh:
                raise AssertionError("fresh ORIGINAL endpoint-layer difference did not vanish")
            fresh_cache[key]={"original_mixed_difference_sha256":ring.digest(difference),
                "original_mixed_difference_terms":len(difference.terms),
                "fresh_endpoint_layer_exact_zero":True,
                "fresh_endpoint_layer_zero_sha256":endpoint.digest([]),
                "fresh_cubic_conversion_records_sha256":endpoint.digest(ftail.records),
                "fresh_cubic_word_statistics":dict(ftail.words.stats)}
        decisions[name]["fresh_original_difference"]=fresh_cache[key]
        if name=="weight_zero_pure_kernel":
            residual=[sum((c*old_pure[i][j] for i,c in coefficients.items()),F(0)) for j in range(3)]
            if any(residual):
                raise AssertionError("fresh stored pure-query sum is nonzero")
            decisions[name]["exact_three_stored_pure_sums"]=["0","0","0"]
            decisions[name]["H_minus_combination_universal_pure_zero"]=True
            decisions[name]["H_minus_combination_lambda_plus"]="1"
            decisions[name]["first_layer_alone_cannot_read_lambda_on_U0"]=True
    report["decisions"]=decisions
    report["H_universal_first_layer_zero"]=not vectors[-1]
    certificate={"schema":SCHEMA+"-in-memory-proof","source_hashes":report["source_hashes"],
        "input_bindings":report["inputs"],"column_order":column_labels,"conversions":conversions,
        "complete_new_layer_vectors":[endpoint.vector_rows(v) for v in vectors],
        "complete_new_cubic_conversion_records":tail.records,"decisions":decisions,
        "old_pure_coordinates":[list(map(str,row)) for row in old_pure],
        "all_actual_profile_and_tail_values_left_unevaluated":True}
    raw=canonical(certificate)
    if len(raw)>args.max_certificate_bytes:
        raise literal.Limit("in-memory first-layer proof byte ceiling")
    report["reproducible_certificate"]={"bytes":len(raw),"sha256":sha(raw),"persisted":False}
    report.update(completion="complete",phase="complete_weight_zero_universal_first_endpoint_layer",
        new_mixed_endpoint_columns=17,old_full_quartic_targets_or_head_kernels_repeated=False,
        old_profile_evaluations_repeated=0,new_profile_evaluations=0,
        new_N_contractions=0,old_pure_queries_reevaluated=0,
        complete_H0_kernel_recomputed=False,total_new_cubic_primitive_calls=calls,
        exact_integer_operations=budget.operations,maximum_integer_bits=budget.maximum_bits,
        specific_analytic_circle_supplied=False,fixed_circle_tau_values_evaluated=False,
        other_weights_excluded=False,full_period_or_joint_ruling_paid=False,task_complete=False)


def laurent_add(out,source,scale=F(1)):
    for key,value in source.items():
        endpoint.sparse_add(out,key,scale*value)


def artificial_rational_elimination():
    # New proof interface on p=exp(-1/t): no real profile integral or coefficient.
    def D(a):
        return {j-1:j*c for j,c in a.items() if j and c}
    def lam(a):
        return {j-2:c for j,c in a.items()}
    def step(A,bs):
        out=D(A);laurent_add(out,lam(A));new={}
        for j,b in bs.items():
            laurent_add(out,{n+j:c for n,c in b.items()})
            db=D(b)
            if db:
                new[j]=db
        return out,new
    A,bs={}, {0:{2:F(1)}}
    for _ in range(3):
        A,bs=step(A,bs)
    return not bs and A=={0:F(6),-1:F(4),-2:F(1)}


def toy_only(args):
    budget=literal.Budget(args.max_seconds,args.memory_mib,args.integer_bits)
    limits=exact.Limits(seconds=args.max_seconds,nodes=15000,atoms=3000,
        terms=6000,rewrites=10000,memory_mib=args.memory_mib,rational_bits=args.integer_bits)
    ring=colored.ColoredRing(limits)
    checks=endpoint.artificial_checks(ring,budget,args)
    checks["finite_L_elimination_of_nonconstant_R_coefficient"]=artificial_rational_elimination()
    wide=pure.decide_projection([{0:F(2)}, {0:F(3)}],budget)
    narrow=pure.decide_projection([{0:F(2),1:F(1)}, {0:F(3)}],budget)
    checks["old_pure_constraint_can_change_the_new_endpoint_member_gate"]=(
        "coefficients" in wide and "dual" in narrow
        and narrow["dual_values_all_columns"]==[F(0),F(1)])
    # Only a new artificial response formula comparison, no old E8 or W data.
    quadratic=lambda a,b:F(3,5)*a*b
    third=lambda a,b,c:F(-7,11)*a*b*c
    mixed=mixed_response(ring,third,quadratic)
    reference=blocks.reference_response(ring,third,quadratic)[-2]
    checks["mixed_only_input_restore_formula_matches_literal_artificial_R78"]=not (mixed-reference).terms
    v={("linear","d",0,0,0,((0,(("q",0),("q",0),("qbar",0))),)):F(2)}
    numer,labels=numeric_vectors([v,dict(v)],[[F(4),F(5),F(6)]])
    checks["stored_pure_rows_append_only_to_response_not_proved_pure_zero_target"]=(
        len(numer[0])==4 and len(numer[1])==1 and len(labels)==4)
    if not all(checks.values()):
        raise AssertionError("new endpoint interfaces failed: "+str(checks))
    return {"checks":checks,"all_passed":True,"real_inputs_read":False,
            "old_development_suites_repeated":False,"scientific_endpoint_target_evaluated":False}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only",action="store_true")
    parser.add_argument("--output",type=Path,help="runner temporary summary only; never publish payload")
    parser.add_argument("--static-directory",type=Path,default=TOPIC/"notes"/head.INPUTS["static"]["directory"])
    parser.add_argument("--R0-directory",type=Path,default=TOPIC/"notes/actions-43649525432-1-g_first_translation")
    parser.add_argument("--head-directory",type=Path,default=TOPIC/"notes/actions-43681388902-1-character_head_zero")
    parser.add_argument("--pure-identity-directory",type=Path,default=TOPIC/"notes/actions-43683171512-1-character_zero_pure_readout")
    parser.add_argument("--stored-pure-directory",type=Path,default=TOPIC/"notes/actions-43646543691-1-full_m8_tail_response_projection")
    parser.add_argument("--max-seconds",type=float,default=240)
    parser.add_argument("--memory-mib",type=int,default=1024)
    parser.add_argument("--integer-bits",type=int,default=8192)
    parser.add_argument("--max-terms",type=int,default=100000)
    parser.add_argument("--max-IBP-calls",type=int,default=300000)
    parser.add_argument("--max-cache-entries",type=int,default=250000)
    parser.add_argument("--max-summary-bytes",type=int,default=95000)
    parser.add_argument("--max-certificate-bytes",type=int,default=8000000)
    args=parser.parse_args()
    if min(args.max_seconds,args.memory_mib,args.integer_bits,args.max_terms,args.max_IBP_calls,
           args.max_cache_entries,args.max_certificate_bytes)<=0 or not 16000<=args.max_summary_bytes<100000:
        parser.error("positive budgets and 16KB..below100KB summary required")
    if not args.toy_only and not (os.environ.get("GITHUB_ACTIONS")=="true"
                                  and os.environ.get("GITHUB_REPOSITORY")==REPOSITORY):
        parser.error("new actual endpoint research runs only in this public repository Actions")
    started=time.monotonic()
    report={"schema":SCHEMA,"completion":"started","phase":"source_binding",
        "github_repository":os.environ.get("GITHUB_REPOSITORY"),
        "github_run_id":os.environ.get("GITHUB_RUN_ID"),"github_sha":os.environ.get("GITHUB_SHA"),
        "inputs":{},"scope":"H against weight-zero responses in the universal first endpoint layer",
        "recomputable_payload_publication_permitted":False}
    code=0
    try:
        report["source_hashes"]=source_identity()
        if args.toy_only:
            report["development"]=toy_only(args)
            report.update(completion="complete",phase="new_artificial_endpoint_interfaces_only")
        else:
            actual(args,report)
    except (literal.Limit,formal.CompilationBudgetExceeded,MemoryError) as error:
        report.update(completion="resource_limit",error=str(error),
            complete_endpoint_gate=False,partial_is_not_a_member_decision=True,
            partial_state_persistence_claimed=False)
        code=2
    except Exception as error:
        report.update(completion="implementation_check_failed",
            error={"type":type(error).__name__,"message":str(error)},complete_endpoint_gate=False)
        code=1
    report["elapsed_seconds"]=time.monotonic()-started
    report["peak_rss_mib"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    body=canonical(report)+b"\n"
    if len(body)>args.max_summary_bytes:
        report={"schema":SCHEMA,"completion":"summary_output_limit",
            "full_summary_bytes":len(body),"full_summary_sha256":sha(body),
            "github_run_id":report["github_run_id"],"github_sha":report["github_sha"],
            "source_hashes":report.get("source_hashes"),"complete_endpoint_gate":False,
            "payload_saved":False}
        body=canonical(report)+b"\n";code=2
    if len(body)>args.max_summary_bytes:
        raise ValueError("minimal endpoint summary exceeds its declared cap")
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_bytes(body)
    if report.get("completion")=="complete" and "decisions" in report:
        print("MATHEMATICAL_RESULT "+json.dumps({
            "scope":"universal weight zero, not a fixed circle",
            "H_first_layer_zero":report["H_universal_first_layer_zero"],
            "all_weight_zero_responses":report["decisions"]["all_weight_zero_responses"],
            "weight_zero_pure_kernel":report["decisions"]["weight_zero_pure_kernel"]},
            sort_keys=True,separators=(",",":")),flush=True)
    print(body.decode().rstrip(),flush=True)
    print(json.dumps({"summary_bytes":len(body),"summary_sha256":sha(body),
                      "payload_publication_permitted":False},sort_keys=True),flush=True)
    raise SystemExit(code)


if __name__=="__main__":
    main()
