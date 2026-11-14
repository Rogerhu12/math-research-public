#!/usr/bin/env python3
"""Consume the complete new derivative factors on the exact m8 pure tail.

The full original L2 and L4 factors are retained, including unreduced N2.
The already published R124 matrix-induced correction is added in full.
Only the new pure substitutions and new N responses are evaluated; old W
responses are imported and reused whenever their original hashes coincide.
"""
from __future__ import annotations

import argparse
import gzip
from fractions import Fraction as F
import json
import os
from pathlib import Path
import resource
import time

import literature_local_fourth_derivative_factors as factors
import literature_constrained_static_m8_tail as constraint

first, projection, old = constraint.first, constraint.projection, constraint.old
exact, colored = first.exact, first.colored
SCHEMA = "visible-flex-complete-derivative-m8-tail-quotient-v1"
REPOSITORY = first.REPOSITORY
TOPIC = Path(__file__).resolve().parents[1]
FACTOR_DRIVER_SHA = "02785c34bfe35993094cb30cc8508a9695f78116bd4423b3ab5ae4b438295abf"
CONSTRAINT_DRIVER_SHA = "8b075b222a1c8ea5579645905f9f3c3efc57a1b286a393cdcd597f384db50417"
CORRECTION_DIRECTORY = TOPIC/"notes/actions-43649160345-1-constrained_static_m8_tail_quotient"
CORRECTION_RUN = "43649160345"
CORRECTION_COMMIT = "c69562728ce9d0f5115ad2710d45bcff15762693"
CORRECTION_MAIN = {"bytes":7892,"sha256":"297c6716a7cf23d1c6006a273f251640bc4c0da878da07d68ef981af43ba65b7"}
CORRECTION_RECEIPT = {"bytes":32633,"sha256":"8b8e3aff681ccbb15a879040d4a69aad94900b00eadae0130571c36b9b18679e"}
CORRECTION_EXPORT = {
    "filename":"constrained-static-m8-tail-certificate.json.gz",
    "stored_bytes":57845,
    "stored_sha256":"022cd4f767d40b5ad21089e4cf88f7f6d4e6e051b7d730c038e87ab0e0961175",
    "raw_bytes":489034,
    "raw_sha256":"ced7357546b2c85610cf200e961c4e568a7a8f53407bf8da033eee8b9cb86ed7"}
MAX_CERTIFICATE_STORED_BYTES = 4500000
canonical, sha, identity = first.canonical, first.sha, first.identity
add_sparse = first.add_sparse
Packet = constraint.Packet


def dependencies():
    derivative = factors.dependencies()
    if derivative["driver"]["sha256"] != FACTOR_DRIVER_SHA:
        raise ValueError("explicitly bind the successful complete derivative-factor producer")
    normalized = constraint.dependencies()
    if normalized["driver"]["sha256"] != CONSTRAINT_DRIVER_SHA:
        raise ValueError("do not mutate the successful matrix-constraint consumer")
    return {"driver":identity(__file__),
            "derivative_factor_dependencies":derivative,
            "matrix_constraint_dependencies":normalized}


def read_explicit_main(path, expected_sha):
    raw=first.projection.checked_bytes(path,95000)
    if sha(raw)!=expected_sha:
        raise ValueError("explicit compact source report SHA mismatch")
    return json.loads(raw),raw


def bind_publication(receipt, *, run, commit, lane, main_name, main_bytes, main_sha, export, driver):
    if (receipt.get("schema")!="visible-new-mechanism-actions-v1"
        or receipt.get("repository")!=REPOSITORY or str(receipt.get("run_id"))!=run
        or receipt.get("source_commit")!=commit or receipt.get("lane")!=lane):
        raise ValueError("real public publication identity mismatch")
    source_key="topics/visible-flex-new-mechanism/scripts/"+driver["filename"]
    if receipt.get("source_files",{}).get(source_key)!={"bytes":driver["bytes"],"sha256":driver["sha256"]}:
        raise ValueError("publication does not bind the exact input source")
    expected=(
        (main_name,{"bytes":main_bytes,"sha256":main_sha,"raw_bytes":main_bytes,"raw_sha256":main_sha}),
        (export["filename"],{"bytes":export["stored_bytes"],"sha256":export["stored_sha256"],
                             "raw_bytes":export["raw_bytes"],"raw_sha256":export["raw_sha256"]}))
    for name,wanted in expected:
        observed=constraint.one_output(receipt,name)
        if any(observed.get(key)!=value for key,value in wanted.items()):
            raise ValueError("publication complete output metadata mismatch")
    return {"source_run":run,"source_commit":commit,"lane":lane,
            "producer_driver":driver,"matched_outputs":[main_name,export["filename"]]}


def load_factors(args, source_ring, report):
    required=(args.factor_report,args.factor_report_sha256,args.factor_publication_receipt,
              args.factor_publication_sha256,args.factor_export,args.factor_export_sha256,
              args.factor_source_run,args.factor_source_commit)
    if not all(required):
        raise ValueError("a full published factor report, receipt, export and source binding is required")
    main,raw=read_explicit_main(args.factor_report,args.factor_report_sha256)
    if (main.get("schema")!=factors.SCHEMA or main.get("completion")!="complete"
        or str(main.get("github_run_id"))!=args.factor_source_run
        or main.get("github_sha")!=args.factor_source_commit
        or main.get("source_hashes")!=factors.dependencies()
        or main.get("factored_L2_and_L4_complete") is not True
        or main.get("original_v2_v4_both_modes_present") is not True):
        raise ValueError("a completed full two-mode derivative-factor source is required")
    metadata=main.get("portable_complete_factor_export")
    if (not metadata or metadata.get("stored_sha256")!=args.factor_export_sha256
        or metadata.get("content_scope")!="unreduced-N0-N2-and-complete-two-mode-v2-v4"):
        raise ValueError("N-only output cannot replace the complete derivative factors")
    publication_raw=projection.checked_bytes(args.factor_publication_receipt,95000)
    if sha(publication_raw)!=args.factor_publication_sha256:
        raise ValueError("explicit factor publication receipt SHA mismatch")
    publication=json.loads(publication_raw)
    binding=bind_publication(publication,run=args.factor_source_run,commit=args.factor_source_commit,
        lane="local_fourth_derivative_factors",main_name=args.factor_report.name,
        main_bytes=len(raw),main_sha=sha(raw),export=metadata,driver=main["source_hashes"]["driver"])
    data=first.read_bound_gzip(args.factor_export,metadata)
    if (data.get("schema")!=factors.SCHEMA+"-original-expressions"
        or data.get("content_scope")!=metadata["content_scope"]
        or data.get("source_hashes")!=main["source_hashes"]
        or str(data.get("github_run_id"))!=args.factor_source_run
        or data.get("github_sha")!=args.factor_source_commit
        or data.get("geometry_names")!=list(factors.GEOMETRY_NAMES)
        or data.get("pointwise_matrix_coordinate_order")!=list(exact.PARAMETERS)
        or data.get("real_s_derivatives_before_history_zero") is not True
        or data.get("potential_two_assumed_in_W") is not False):
        raise ValueError("complete original factor scope, jets or source identity mismatch")
    roots=old.decode_expressions(source_ring,data)
    if len(roots)!=metadata["root_count"] or len(data["profile_atoms"])!=metadata["profile_atom_count"]:
        raise ValueError("full factor root or atom coverage changed")
    potential={0:[],2:[]};generators={mode:{2:[],4:[]} for mode in (-4,-2)}
    used=set();seen=set()
    for row in data["potential_records"]:
        weight,key,name=row["geometry_derivative_weight"],tuple(row["geometry_key"]),row["root"]
        if (weight not in potential or len(key)!=10 or factors.geometry_weight(key)!=weight
            or name in used or name not in roots or ("N",weight,key) in seen):
            raise ValueError("original potential record malformed")
        expression=roots[name]
        if any(degree!=(("a",1),("b",1),("c",1)) for degree in source_ring.color_degrees(expression)):
            raise ValueError("complete N lost the real exterior/inner slots")
        potential[weight].append((key,name,expression))
        used.add(name);seen.add(("N",weight,key))
    for row in data["local_generator_records"]:
        mode,weight,key,name=(row["mode"],row["geometry_derivative_weight"],
                              tuple(row["geometry_key"]),row["root"])
        if (mode not in generators or weight not in generators[mode] or len(key)!=10
            or factors.geometry_weight(key)!=weight or name in used or name not in roots
            or ("v",mode,weight,key) in seen):
            raise ValueError("complete local generator record malformed")
        expression=roots[name]
        if any(source_ring.p.weight(m)!=4 for m in expression.terms):
            raise ValueError("full local v lost its fourth profile degree")
        if mode==-4:
            first.require_pure_fourth(source_ring,expression)
        generators[mode][weight].append((key,name,expression))
        used.add(name);seen.add(("v",mode,weight,key))
    if used!=set(roots):
        raise ValueError("every original factor root must have its declared complete role")
    matrix={0:[{} for _ in range(8)],2:[{} for _ in range(8)]}
    if len(data["pointwise_matrix_original_coefficients"])!=8:
        raise ValueError("the complete eight pointwise matrix coordinates are required")
    for index,rows in enumerate(data["pointwise_matrix_original_coefficients"]):
        for row in rows:
            key,weight=tuple(row["geometry_key"]),row["geometry_derivative_weight"]
            value=F(row["coefficient"])
            if (len(key)!=10 or weight not in matrix or factors.geometry_weight(key)!=weight
                or key in matrix[weight][index] or not value):
                raise ValueError("original complete matrix factor record malformed")
            matrix[weight][index][key]=value
    report["new_factor_input"]={
        "publication":binding,"publication_receipt_sha256":sha(publication_raw),
        "compact_main_sha256":sha(raw),"complete_export":metadata,
        "all_original_root_hashes_verified":True,
        "raw_N0_coefficients":len(potential[0]),"raw_N2_coefficients":len(potential[2]),
        "v_derivative_coefficients":{str(mode):{str(w):len(rows) for w,rows in parts.items()}
                                     for mode,parts in generators.items()},
        "geometry_names":data["geometry_names"],"mixed_original_roots_retained_in_source":True,
        "mixed_mode_profile_evaluations":0,"N2_dropped_or_assumed_in_W":False,
        "original_compilers_called":False}
    return potential,generators[-4],matrix


def load_correction(args, columns, ring, report):
    main=first.read_bound_json(args.correction_report,CORRECTION_MAIN)
    publication=first.read_bound_json(args.correction_publication_receipt,CORRECTION_RECEIPT)
    if (main.get("schema")!=constraint.SCHEMA or main.get("completion")!="complete"
        or str(main.get("github_run_id"))!=CORRECTION_RUN or main.get("github_sha")!=CORRECTION_COMMIT
        or main.get("source_hashes")!=constraint.dependencies()
        or main.get("full_matrix_constraint_and_induced_weight_two_accounted_for") is not True):
        raise ValueError("the published complete R124 matrix correction is required")
    first.require_export_metadata(main.get("complete_certificate"),CORRECTION_EXPORT)
    binding=bind_publication(publication,run=CORRECTION_RUN,commit=CORRECTION_COMMIT,
        lane="constrained_static_m8_tail_quotient",main_name="constrained-static-m8-tail.json",
        main_bytes=CORRECTION_MAIN["bytes"],main_sha=CORRECTION_MAIN["sha256"],
        export=CORRECTION_EXPORT,driver=main["source_hashes"]["driver"])
    data=first.read_bound_gzip(args.correction_certificate,CORRECTION_EXPORT)
    if (data.get("schema")!=constraint.SCHEMA+"-certificate"
        or data.get("source_hashes")!=main["source_hashes"]
        or str(data.get("github_run_id"))!=CORRECTION_RUN or data.get("github_sha")!=CORRECTION_COMMIT):
        raise ValueError("full R124 correction certificate source mismatch")
    records=data["groups"]["induced_derivative_two_correction"]["geometry_coefficients"]
    if len(records)!=18:
        raise ValueError("all eighteen published correction packets are required")
    answer={}
    for row in records:
        key=factors.extend_key(tuple(row["geometry_key"]))
        if key in answer or factors.geometry_weight(key)!=2:
            raise ValueError("R124 derivative correction geometry record malformed")
        coefficients={index:F(value) for index,value in row["original_response_coefficients"]}
        packet=Packet(first.polynomial_from_rows(row["complete_polynomial"]),coefficients,
                      first.polynomial_from_rows(row["complete_remainder"]))
        packet.verify(columns,ring)
        answer[key]=packet
    report["induced_correction_input"]={
        "publication":binding,"main":CORRECTION_MAIN,"complete_certificate":CORRECTION_EXPORT,
        "all_eighteen_complete_packets_retained":True,"old_profile_substitutions_recomputed":False,
        "original_L2_was_not_replaced_by_this_correction":True}
    return answer


def setup_response(args, ring, report):
    columns,weights,pivots,ranks=constraint.load_response_columns(args,report)
    spans={weight:projection.ExactProjectedSpan(ring) for weight in ranks}
    for index in sorted(columns):
        spans[weights[index]].add(index,columns[index])
    found={tuple(item["pivot"]) for span in spans.values() for item in span.pivot_records}
    if found!=pivots or sum(len(s.independent) for s in spans.values())!=31:
        raise ValueError("new-target basis factorization differs from the published 31 pivots")
    data=first.read_bound_gzip(args.response_certificate,first.RESPONSE_EXPORT)
    known={}
    for row in data["columns"]:
        key=(row["original_third_sha256"],row["quadratic_index"])
        polynomial=first.polynomial_from_rows(row["complete_polynomial"])
        if key in known and known[key][0]!=polynomial:
            raise ValueError("one original third/operator pair has inconsistent published polynomials")
        known[key]=(polynomial,row["index"])
    report["input_response"]["basis_refactorizations"]=1
    report["input_response"]["basis_factorization_purpose"]="only the new original derivative targets"
    report["input_response"]["old_W_response_hash_reuse_map_columns"]=288
    return columns,weights,pivots,spans,known


def add_geometry_polynomial(target,key,polynomial,amount,ring):
    key=factors.extend_key(key)
    value=target.setdefault(key,{})
    add_sparse(value,polynomial,amount,ring)
    if not value:
        target.pop(key,None)


def new_pure_density(potential,generators,matrix,source_ring,ring,known,report):
    q=ring.power_tail(8)
    evaluator=projection.OriginalTailEvaluator(source_ring.p,ring,{"q":q})
    density={2:{},4:{}}
    v_records=[]
    for weight,rows in generators.items():
        for key,name,expression in rows:
            value=evaluator.expression(expression)
            add_geometry_polynomial(density[weight],key,value.terms,F(1),ring)
            v_records.append({"weight":weight,"geometry_key":list(key),"original_root":name,
                              "complete_polynomial":value.rows()})
    quadratics=[projection.CachedQuadratic(op) for op in exact.operator_basis(ring)]
    thirds={};cache={};response_records=[]
    new_count=reused_count=0
    for target_weight,matrix_weight,potential_weight in ((2,0,2),(2,2,0),(4,2,2)):
        for nkey,name,expression in potential[potential_weight]:
            digest=source_ring.digest(expression)
            for index,scalar_terms in enumerate(matrix[matrix_weight]):
                if not scalar_terms:
                    continue
                token=(digest,index)
                if token not in cache:
                    if token in known:
                        value,old_index=known[token]
                        cache[token]=dict(value)
                        reused_count+=1
                        reused=old_index
                    else:
                        if digest not in thirds:
                            thirds[digest]=projection.OriginalTailThird(source_ring.p,ring,expression)
                        third=thirds[digest]
                        value=projection.tail.pure_fourth_response(quadratics[index],third,q)/16
                        cache[token]=dict(value.terms)
                        new_count+=1
                        reused=None
                    response_records.append({
                        "original_third_sha256":digest,"source_root":name,"quadratic_index":index,
                        "complete_minus_four_response":first.polynomial_rows(cache[token]),
                        "reused_old_R116_original_column":reused})
                for mkey,amount in scalar_terms.items():
                    key=tuple(a+b for a,b in zip(nkey,mkey))
                    if factors.geometry_weight(key)!=target_weight:
                        raise AssertionError("complete B_m(N) geometric weight mismatch")
                    add_geometry_polynomial(density[target_weight],key,cache[token],-amount,ring)
            ring.guard()
    report["new_pure_evaluation"]={
        "new_local_v2_v4_roots_evaluated":len(v_records),
        "distinct_N_response_pairs_needed":len(cache),
        "new_original_N_response_evaluations":new_count,
        "identical_old_W_response_columns_reused":reused_count,
        "old_W_response_formulas_recomputed":0,
        "complete_formula_L2":"v2-B_m0(N2)-B_m2(N0)",
        "complete_formula_L4":"v4-B_m2(N2)",
        "raw_potential_representative_kept":True,"outer_inner_slots_preserved":True,
        "same_actual_right_anchor":True,"original_I_equals_minus_J":True,
        "full_pure_response_division":16,"local_v_phase_not_divided_again":True}
    return density,{"new_v_polynomials":v_records,"N_response_polynomials":response_records}


def reduce_density(density,spans,columns,ring):
    answer={}
    for key,polynomial in density.items():
        packet=Packet(polynomial)
        for weight,part in first.split_weights(polynomial).items():
            coefficients,remainder=first.reduce_target(spans.get(weight),part,ring)
            add_sparse(packet.coefficients,coefficients,F(1),ring)
            add_sparse(packet.remainder,remainder,F(1),ring)
        packet.verify(columns,ring)
        answer[key]=packet
    return answer


def add_correction(target,correction,ring):
    out={key:packet.copy() for key,packet in target.items()}
    for key,packet in correction.items():
        out.setdefault(key,Packet()).add(packet,F(1),ring)
    return {key:packet for key,packet in out.items() if not packet.empty()}


def summarize(name,target,columns,weights,pivots,ring,allowed_geometry_weights):
    raw=projection.ExactProjectedSpan(ring);even=projection.ExactProjectedSpan(ring)
    graded={};records=[];components=[]
    for index,(key,packet) in enumerate(sorted(target.items())):
        if len(key)!=10 or factors.geometry_weight(key) not in allowed_geometry_weights:
            raise ValueError("new complete derivative geometry record in a wrong part")
        packet.verify(columns,ring)
        if any(m in pivots for m in packet.remainder):
            raise AssertionError("new canonical remainder retains a response pivot")
        raw.add(index,packet.remainder)
        even.add(index,projection.four_block_projection(packet.remainder))
        records.append({"geometry_coefficient_index":index,"geometry_key":list(key),**packet.rows()})
        for weight,component in constraint.packet_components(packet,weights).items():
            component.verify(columns,ring)
            index_part=len(components)
            graded.setdefault(weight,projection.ExactProjectedSpan(ring)).add(index_part,component.remainder)
            components.append({"component_index":index_part,"geometry_coefficient_index":index,
                "geometry_key":list(key),"true_profile_weight":weight,**component.rows()})
        ring.guard()
    summary={
        "name":name,"geometry_derivative_weights":sorted(allowed_geometry_weights),
        "full_geometry_coefficients":len(records),
        "nonzero_full_remainders":sum(bool(row["complete_remainder"]) for row in records),
        "raw_coefficient_quotient_rank":len(raw.independent),
        "graded_coefficient_quotient_rank":sum(len(span.independent) for span in graded.values()),
        "even_raw_quotient_rank":len(even.independent),
        "even_graded_quotient_rank":sum(len(span.independent) for w,span in graded.items() if w%2==0),
        "independent_raw_geometry_keys":[records[index]["geometry_key"] for index in raw.independent],
        "per_true_profile_weight":{str(w):{"rank":len(span.independent),
            "independent_components":span.independent} for w,span in sorted(graded.items())},
        "all_complete_new_polynomial_differences_zero":True}
    complete={"summary":summary,"geometry_coefficients":records,"homogeneous_components":components,
        "raw_quotient_basis":raw.summary(),"even_raw_quotient_basis":even.summary(),
        "graded_quotient_bases":{str(w):span.summary() for w,span in sorted(graded.items())}}
    return summary,complete



def write_complete_certificate(path,data):
    raw=canonical(data)
    if len(raw)>first.MAX_RAW_BYTES:
        raise RuntimeError("complete derivative certificate exceeds the declared raw byte limit")
    stored=gzip.compress(raw,mtime=0)
    if len(stored)>MAX_CERTIFICATE_STORED_BYTES:
        raise RuntimeError("complete derivative certificate exceeds the reserved stored byte limit")
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_bytes(stored)
    return {"filename":path.name,"stored_bytes":len(stored),"stored_sha256":sha(stored),
            "raw_bytes":len(raw),"raw_sha256":sha(raw)}

def actual(args,report):
    if (os.environ.get("GITHUB_ACTIONS","").lower()!="true"
        or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY):
        raise RuntimeError("the complete new derivative target only runs in public repository Actions")
    started=time.monotonic()
    ring=projection.TailRing(args.max_seconds,args.memory_mib,args.max_operations)
    limits=exact.Limits(seconds=args.max_seconds,nodes=500000,atoms=100000,
                        terms=100000,rewrites=1000,memory_mib=args.memory_mib)
    source_ring=colored.ColoredRing(limits)
    columns,weights,pivots,spans,known=setup_response(args,ring,report)
    correction=load_correction(args,columns,ring,report)
    potential,generators,matrix=load_factors(args,source_ring,report)
    density,evaluations=new_pure_density(potential,generators,matrix,source_ring,ring,known,report)
    L2=reduce_density(density[2],spans,columns,ring)
    L4=reduce_density(density[4],spans,columns,ring)
    corrected2=add_correction(L2,correction,ring)
    combined={key:packet.copy() for key,packet in corrected2.items()}
    for key,packet in L4.items():
        combined.setdefault(key,Packet()).add(packet,F(1),ring)
    groups={};full_groups={}
    for name,target,allowed in (
        ("original_L2",L2,{2}),("matrix_normalized_L2",corrected2,{2}),
        ("original_L4",L4,{4}),("complete_remaining_derivative_density",combined,{2,4})):
        groups[name],full_groups[name]=summarize(name,target,columns,weights,pivots,ring,allowed)
    certificate={
        "schema":SCHEMA+"-certificate","source_hashes":report["source_hashes"],
        "github_run_id":report["github_run_id"],"github_sha":report["github_sha"],
        "new_factor_input":report["new_factor_input"],
        "induced_correction_input":report["induced_correction_input"],
        "input_response":report["input_response"],
        "geometry_names":list(factors.GEOMETRY_NAMES),
        "new_pure_evaluation":report["new_pure_evaluation"],**evaluations,"groups":full_groups,
        "full_remaining_formula":"L2+R124_Delta2+L4 modulo the published complete m8 pure response space",
        "raw_N_vs_static_representative_difference":"pointwise W difference; complete R8 response difference retained in quotient",
        "geometric_integration_by_parts_applied":False,"actual_M0_path_evaluated":False,
        "actual_period_sign_or_reachability_asserted":False}
    exported=write_complete_certificate(args.out.with_name(args.out.stem+"-certificate.json.gz"),certificate)
    report.update(completion="complete",complete_certificate=exported,groups=groups,
        original_L2_and_L4_fully_included_in_pure_projection=True,
        induced_R124_correction_fully_included=True,
        static_normalized_part_recomputed=False,complete_mixed_projection_evaluated=False,
        geometric_integration_by_parts_applied=False,actual_geometry_evaluated=False,
        actual_period_sign_or_reachability_asserted=False,
        polynomial_operations=ring.operations,linear_operations=ring.linear_operations,
        raw_atoms_evaluated=ring.raw_atoms_evaluated,raw_monomials_evaluated=ring.raw_monomials_evaluated,
        maximum_intermediate_terms=ring.maximum_terms,
        elapsed_seconds=time.monotonic()-started,
        peak_rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024,task_complete=False)
    return report


def toy_only():
    ring=projection.TailRing(40,256,100000)
    columns={0:{(1,0):F(1)},1:{(0,1):F(1)}}
    weights={0:-31,1:-31}
    span=projection.ExactProjectedSpan(ring)
    for index,polynomial in columns.items():
        span.add(index,polynomial)
    jet2=(0,0,0,2,0,0,0,0,0,0)
    jet4=(0,0,0,1,0,0,0,0,1,0)
    density={jet2:{(1,0):F(3),(0,2):F(5)}}
    result=reduce_density(density,{-31:span},columns,ring)
    correction={jet2:Packet({(0,2):F(-5)},{},{(0,2):F(-5)})}
    corrected=add_correction(result,correction,ring)
    corrected[jet2].verify(columns,ring)
    target={}
    add_geometry_polynomial(target,jet4,{(0,2):F(4)},F(-3),ring)
    checks={
        "new_raw_density_reduction_retains_whole_polynomial":result[jet2].remainder=={(0,2):F(5)},
        "complete_old_induced_correction_is_added_not_substituted":(
            corrected[jet2].polynomial=={(1,0):F(3)} and not corrected[jet2].remainder),
        "geometric_third_jets_survive_full_weight_four_assembly":(
            target[jet4]=={(0,2):F(-12)} and factors.geometry_weight(jet4)==4),
        "legacy_eight_coordinate_keys_only_append_two_zeros":(
            factors.extend_key((1,2,3,0,0,0,0,0))==(1,2,3,0,0,0,0,0,0,0)),
        "no_research_data_or_actual_m8_profile_evaluated":True}
    if not all(checks.values()):
        raise AssertionError("new derivative consumer artificial check failed")
    return {"completion":"complete","mode":"small_artificial_development_only",
            "checks":checks,"all_passed":True,"task_complete":False}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out",required=True,type=Path)
    parser.add_argument("--toy-only",action="store_true")
    parser.add_argument("--factor-report",type=Path)
    parser.add_argument("--factor-report-sha256")
    parser.add_argument("--factor-publication-receipt",type=Path)
    parser.add_argument("--factor-publication-sha256")
    parser.add_argument("--factor-export",type=Path)
    parser.add_argument("--factor-export-sha256")
    parser.add_argument("--factor-source-run")
    parser.add_argument("--factor-source-commit")
    parser.add_argument("--correction-report",type=Path,default=CORRECTION_DIRECTORY/"constrained-static-m8-tail.json")
    parser.add_argument("--correction-publication-receipt",type=Path,default=CORRECTION_DIRECTORY/"receipt.json")
    parser.add_argument("--correction-certificate",type=Path,default=CORRECTION_DIRECTORY/CORRECTION_EXPORT["filename"])
    parser.add_argument("--response-report",type=Path,default=first.RESPONSE_DIRECTORY/"full-m8-tail-response.json")
    parser.add_argument("--response-publication-receipt",type=Path,default=first.RESPONSE_DIRECTORY/"receipt.json")
    parser.add_argument("--response-certificate",type=Path,default=first.RESPONSE_DIRECTORY/first.RESPONSE_EXPORT["filename"])
    parser.add_argument("--max-seconds",type=float,default=600)
    parser.add_argument("--memory-mib",type=int,default=1024)
    parser.add_argument("--max-operations",type=int,default=10000000)
    args=parser.parse_args()
    started=time.monotonic()
    report={"schema":SCHEMA,"completion":"started","github_run_id":os.environ.get("GITHUB_RUN_ID"),
            "github_sha":os.environ.get("GITHUB_SHA"),"task_complete":False}
    failed=False
    try:
        report["source_hashes"]=dependencies()
        report.update(toy_only() if args.toy_only else actual(args,report))
    except Exception as error:
        failed=True
        report.update(completion="incomplete",error_type=type(error).__name__,error=str(error),
                      new_mathematical_conclusion_published=False,task_complete=False)
    report["wall_seconds"]=time.monotonic()-started
    raw=canonical(report)+b"\n"
    if len(raw)>first.MAX_REPORT_BYTES:
        full=first.write_gzip(args.out.with_name(args.out.stem+"-full-report.json.gz"),report)
        report={key:report[key] for key in ("schema","completion","github_run_id","github_sha",
            "source_hashes","wall_seconds","complete_certificate","new_factor_input",
            "induced_correction_input","new_pure_evaluation","input_response",
            "error_type","error","task_complete") if key in report}
        report.update(compact_fallback=True,complete_report=full)
        raw=canonical(report)+b"\n"
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_bytes(raw)
    print(json.dumps({"filename":args.out.name,"bytes":len(raw),"sha256":sha(raw)},sort_keys=True),flush=True)
    if failed:
        raise SystemExit(1)


if __name__=="__main__":
    main()
