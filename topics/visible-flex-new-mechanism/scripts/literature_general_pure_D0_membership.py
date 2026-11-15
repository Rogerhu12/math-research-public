#!/usr/bin/env python3
"""One new general-profile D0 pure target against R151's archived nine bases.

Consume the completed nine pure original roots AND their archived exact
word representatives. Do not normalize the old forty roots or recompute
their thirty-one dependencies. Normalize only D0_-4, solve over Q, then
test one freshly formed original difference with the same right anchor.
A nonzero sound remainder is undecided; no profile evaluation is available.
Real research is restricted to the named public repository's Actions.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import json
import os
from pathlib import Path
import resource
import time

import literature_D0_pivot_residual_probe as target_io
import literature_general_pure_J_membership as archived

axis, layer = target_io.axis, target_io.layer
pure, static, old = archived.pure, archived.static, archived.old
exact, colored, blocks = archived.exact, archived.colored, archived.blocks
formal, quotient = archived.formal, archived.quotient

SCHEMA = "visible-flex-general-pure-D0-archived-basis-membership-v1"
REPOSITORY = "Rogerhu12/math-research-public"
TOPIC = target_io.TOPIC
WEIGHT = -2
PURE_MODE = -4
TARGET_READER_SHA = "e6a4c15bfe95c587c4cde0cae26b33cf0bf4f54f0ea7b9cfb5c83026c98afbcd"
BASIS_DRIVER = {
    "filename": "literature_general_pure_J_membership.py", "bytes": 37092,
    "sha256": "1a84590f8b6f0c35a1df5f251a8ffa0e9f4da65ea2cc3bd777e752482ef05bcc"}
BASIS_RUN = "43657785023"
BASIS_COMMIT = "c606688a842bd811106ff2844e1161a4f34c159e"
BASIS_LANE = "general_pure_J_membership"
BASIS_MAIN = {"filename": "general-pure-J-membership.json", "bytes": 45019,
    "sha256": "98442251ed15b708a70e3fcbbdb2ae6cf76c8c1873aa21345354a5a320a9cfac"}
BASIS_RECEIPT = {"filename": "receipt.json", "bytes": 35841,
    "sha256": "31d6380160437b0098d33d35e4b722c79cd780d351f614a4e48901100a9d0fa4"}
BASIS_EXPORT = {
    "filename": "general-pure-J-membership-certificate.json.gz",
    "stored_bytes": 84283,
    "stored_sha256": "af46437f676716a20051bf3bad5a96235398dcf8a45c179d1395bc1f9d84712e",
    "raw_bytes": 456216,
    "raw_sha256": "9859368ec20e0923cc168199a7ecb82eff0beac5fa191f1b6388e67cfd1aa550"}
BASIS_SCOPE = "one J and the complete weight-minus-two pure response membership question"
BASIS_POSITIONS = (0, 1, 2, 3, 8, 9, 10, 12, 19)
BASIS_GLOBAL = (0, 48, 88, 112, 41, 73, 81, 193, 170)
DEPENDENCIES_SHA = "bdd01870f261b98a4f63c38789ccbe81b96084e71c25ef0831c3893718536a69"


def source_identity():
    target = target_io.source_identity()
    previous = archived.sources()
    if target["driver"]["sha256"] != TARGET_READER_SHA:
        raise ValueError("the completed D0 original-root input helper changed")
    if previous["driver"] != BASIS_DRIVER:
        raise ValueError("the completed nine-basis producer changed")
    return {"driver": static.identity(__file__),
        "completed_D0_input_helper": target,
        "completed_pure_basis_producer": previous}


def selected_records(records, positions, *, count):
    """Portable positions are independent of full-block and global IDs."""
    if (len(records) != count or len(set(positions)) != len(positions)
        or any(type(i) is not int or not 0 <= i < count for i in positions)):
        raise ValueError("invalid archived representative count or selected positions")
    indexed = {}
    for row in records:
        index = row.get("original_position")
        if type(index) is not int or not 0 <= index < count or index in indexed:
            raise ValueError("duplicate or absent archived representative index")
        indexed[index] = row
    if set(indexed) != set(range(count)):
        raise ValueError("the archived representative array is incomplete")
    return [indexed[i] for i in positions]


def bind_word_row(normalizer, row, original_sha, original_name):
    if (row.get("original_sha256") != original_sha
        or row.get("original_root") != original_name):
        raise ValueError("archived representative does not bind its original root")
    value = archived.decode_word_rows(normalizer.word, row["word_rows"])
    if normalizer.word.summary(value) != row.get("word_summary"):
        raise ValueError("archived pure representative SHA or shape changed")
    return value


def load_nine_basis(args, ring, normalizer, report):
    directory = args.basis_directory
    main = layer.read_bound_json(directory/BASIS_MAIN["filename"], BASIS_MAIN)
    publication = layer.read_bound_json(directory/BASIS_RECEIPT["filename"], BASIS_RECEIPT)
    expected_sources = report["source_hashes"]["completed_pure_basis_producer"]
    upper = main.get("pure_response_upper_bound") or {}
    result = main.get("result") or {}
    metadata = main.get("portable_original_certificate") or {}
    if (main.get("schema") != archived.SCHEMA
        or main.get("completion") != "complete"
        or main.get("github_repository") != REPOSITORY
        or str(main.get("github_run_id")) != BASIS_RUN
        or main.get("github_sha") != BASIS_COMMIT
        or main.get("source_hashes") != expected_sources
        or not result.get("general_pure_J_member_proved")
        or result.get("profile_affine_weight") != WEIGHT
        or result.get("pure_mode") != PURE_MODE
        or upper.get("input_true_full_basis_columns") != 40
        or upper.get("proved_true_pure_dimension_upper_bound") != 9
        or upper.get("new_original_pure_dependencies_verified") != 31
        or upper.get("unresolved_proposed_pure_dependencies_retained") != 0
        or upper.get("new_dependency_proofs_sha256") != DEPENDENCIES_SHA
        or not upper.get("original_pure_span_is_covered")
        or not upper.get("all_new_original_dependencies_in_certificate")
        or tuple(upper.get("retained_original_positions", [])) != BASIS_POSITIONS
        or tuple(upper.get("retained_global_R116_columns", [])) != BASIS_GLOBAL
        or metadata.get("input_original_columns_recompiled") is not False
        or metadata.get("content_scope") != BASIS_SCOPE
        or metadata.get("original_root_count") != 73
        or metadata.get("new_pure_column_representatives") != 40
        or any(metadata.get(k) != v for k, v in BASIS_EXPORT.items())):
        raise ValueError("the completed exact nine-dimensional pure cover changed")
    binding = layer.check_publication(publication, run=BASIS_RUN,
        commit=BASIS_COMMIT, lane=BASIS_LANE, driver=BASIS_DRIVER,
        main_name=BASIS_MAIN["filename"], main_info=BASIS_MAIN, export_info=metadata)
    data = layer.read_bound_export(directory/BASIS_EXPORT["filename"], metadata)
    if (data.get("schema") != archived.SCHEMA+"-original-expressions"
        or data.get("content_scope") != BASIS_SCOPE
        or data.get("github_repository") != REPOSITORY
        or str(data.get("github_run_id")) != BASIS_RUN
        or data.get("github_sha") != BASIS_COMMIT
        or data.get("source_hashes") != expected_sources
        or data.get("pure_response_upper_bound") != upper
        or data.get("input_basis") != main.get("input_basis")
        or data.get("mathematical_result") != result
        or len(data.get("roots", {})) != 73):
        raise ValueError("the archived original/representative certificate changed")
    proofs = data.get("new_pure_dependency_proofs") or []
    if (len(proofs) != 31 or not all(p.get("original_identity_proved") for p in proofs)
        or pure.sha(pure.data_bytes(proofs)) != DEPENDENCIES_SHA):
        raise ValueError("the old complete pure upper-bound evidence is absent")
    rows = selected_records(data.get("pure_column_representatives") or [],
        BASIS_POSITIONS, count=40)
    old_labels = main["input_basis"]["retained_original_labels"]
    if len(old_labels) != 40:
        raise ValueError("the archived full-basis labels changed")
    names = ["original_pure_column_%02d" % i for i in BASIS_POSITIONS]
    originals = axis.subset_decode(ring, data, names)
    values, vectors, labels = [], [], []
    grading = blocks.ScalingGrading(ring)
    for local_index, (position, global_id, name, row) in enumerate(
            zip(BASIS_POSITIONS, BASIS_GLOBAL, names, rows)):
        label = old_labels[position]
        if (label.get("position") != position
            or label.get("global_R116_column") != global_id
            or label.get("weight_block_original_column") != position):
            raise ValueError("selected original/full-block/global index mismatch")
        value = originals[name]
        digest = ring.digest(value)
        if digest != label.get("original_pure_sha256"):
            raise ValueError("the selected true pure basis root changed")
        pure.require_degree(ring, value, "q", 4)
        if set(grading.split(value)) != {WEIGHT}:
            raise ValueError("an archived pure basis root has changed weight")
        vector = bind_word_row(normalizer, row, digest, name)
        values.append(value)
        vectors.append(vector)
        labels.append({"new_index": local_index, "archived_original_position": position,
            "weight_block_original_column": label["weight_block_original_column"],
            "global_R116_column": global_id,
            "quadratic_index": label["quadratic_index"],
            "third_index": label["third_index"],
            "third_original_sha256": label["third_original_sha256"],
            "original_root": name, "original_pure_sha256": digest,
            "word_summary": normalizer.word.summary(vector)})
    report["input_pure_basis"] = {"publication": binding, "main": BASIS_MAIN,
        "receipt": BASIS_RECEIPT, "complete_certificate": metadata,
        "old_true_pure_span_upper_bound": 9, "true_independence_source": "R151 section 3",
        "old_original_pure_dependencies_consumed": 31,
        "old_original_pure_dependencies_recomputed": 0,
        "old_pure_roots_renormalized": 0,
        "archived_original_roots_decoded": 9,
        "archived_word_representatives_decoded": 9,
        "original_positions": list(BASIS_POSITIONS),
        "global_R116_columns": list(BASIS_GLOBAL), "labels": labels}
    return values, vectors, labels, rows


def solve_once(ring, normalizer, target, originals, vectors, limits, args):
    span = quotient.ExactWordSpan(vectors, limits)
    if span.independent != list(range(len(originals))):
        raise ValueError("the source-bound pure basis representatives lost independence")
    target_vector = normalizer.expression(target)
    coefficients, remainder = span.reduce(target_vector)
    fresh = quotient.ProfileNormalizer(ring, args.max_IBP_calls, args.max_terms)
    difference, reduced, proof = archived.original_proposal(
        ring, target, originals, coefficients, fresh)
    proof.update({"target_word_summary": normalizer.word.summary(target_vector),
        "target_word_rows": pure.word_rows(target_vector),
        "word_solve_remainder": normalizer.word.summary(remainder),
        "word_solve_remainder_rows": pure.word_rows(remainder),
        "fresh_original_remainder_rows": pure.word_rows(reduced),
        "fresh_original_difference_checked_even_if_word_solve_unresolved": True,
        "coefficients_are_exact_Q_not_modular_lifts": True})
    statistics = {
        "only_new_target": {"right_IBP": normalizer.legacy.stats,
            "word": normalizer.word.stats},
        "one_new_original_difference": {"right_IBP": fresh.legacy.stats,
            "word": fresh.word.stats}}
    return coefficients, difference, proof, span.summary(), statistics


def save_certificate(args, report, ring, named, certificate):
    payload = {"schema": SCHEMA+"-original-expressions",
        "content_scope": "one-original-D0-pure-solve-against-nine-archived-originals",
        "github_repository": report["github_repository"],
        "github_run_id": report["github_run_id"], "github_sha": report["github_sha"],
        "source_hashes": report["source_hashes"], "phase": report["phase"],
        "input_D0": report.get("D0_input"), "input_pure_basis": report.get("input_pure_basis"),
        "mathematical_result": report.get("result"), **certificate,
        **old.serialize_expressions(ring, named)}
    path = args.output.with_name(args.output.stem+"-certificate.json.gz")
    metadata = pure.store_gzip(path, payload, args.max_certificate_bytes)
    metadata.update({"content_scope": payload["content_scope"],
        "original_root_count": len(named), "old_dependencies_recomputed": False})
    report["portable_original_certificate"] = metadata


def run_research(args, report):
    limits = exact.Limits(args.max_seconds, args.max_nodes, args.max_atoms,
        args.max_terms, args.max_IBP_calls, args.memory_mib, args.max_rational_bits)
    ring = colored.ColoredRing(limits)
    normalizer = quotient.ProfileNormalizer(ring, args.max_IBP_calls, args.max_terms)
    report["phase"] = "consume_completed_D0_original_hashes"
    targets = target_io.load_D0(args, ring, report)
    target = targets[PURE_MODE]
    pure.require_degree(ring, target, "q", 4)
    if set(blocks.ScalingGrading(ring).split(target)) != {WEIGHT}:
        raise ValueError("the complete D0 pure root has changed true weight")
    report["original_D0_pure"] = {"mode": PURE_MODE, "profile_affine_weight": WEIGHT,
        "original_sha256": ring.digest(target), "original_terms": len(target.terms),
        "mixed_root_only_source_bound_not_normalized_or_evaluated": True}
    report["phase"] = "decode_nine_archived_true_pure_bases_and_word_representatives"
    originals, vectors, labels, rows = load_nine_basis(args, ring, normalizer, report)
    report["input_regularity"] = archived.dual.reachable_jet_bound(ring, [target]+originals)
    if report["input_regularity"]["colors"] != ["q"]:
        raise ValueError("a mixed color entered the one pure target")
    named = {"original_D0_minus4": target}
    named.update({"archived_original_pure_column_%02d" % p: value
        for p, value in zip(BASIS_POSITIONS, originals)})
    certificate = {"archived_selected_word_representatives": rows,
        "archived_selected_labels": labels,
        "normalizer_sound_but_not_complete": True,
        "old_research_or_profile_evaluation_repeated": False}
    save_certificate(args, report, ring, named, certificate)
    report["phase"] = "one_new_Q_solve_and_fresh_original_difference"
    coefficients, difference, proof, span, statistics = solve_once(
        ring, normalizer, target, originals, vectors, limits, args)
    proof["original_difference_root"] = "one_D0_proposed_original_difference"
    named[proof["original_difference_root"]] = difference
    proof["coefficients_in_original_global_columns"] = [
        [labels[i]["global_R116_column"], str(value)] for i, value in sorted(coefficients.items())]
    certificate["one_D0_proposal"] = proof
    report["one_D0_proposal"] = {k:v for k,v in proof.items() if not k.endswith("_rows")}
    report["nine_archived_representative_span"] = span
    positive = proof["original_identity_proved"]
    report["result"] = {"status": "general_pure_D0_member_identity_proved"
            if positive else "undecided_sound_original_remainder",
        "general_pure_D0_member_proved": positive,
        "general_pure_D0_nonmember_proved": False,
        "complete_two_mode_D0_member_proved": False,
        "all_general_pure_costs_in_response_proved": False,
        "actual_cost_sign_or_signed_control_claimed": False,
        "profile_affine_weight": WEIGHT, "pure_mode": PURE_MODE}
    report["normalizer_statistics"] = statistics
    report["coefficient_arithmetic"] = {"field": "Q",
        "profile_atoms": len(ring.p.atoms),
        "coefficient_nodes": len(ring.algebra.c.nodes), "limits_check_calls": limits.calls}
    report["phase"] = "complete_one_D0_general_pure_membership_question"
    report["completion"] = "complete"
    save_certificate(args, report, ring, named, certificate)


def artificial_toys():
    """Only the new archive-selection/solve/proof boundary; no actual inputs."""
    checks = {}
    records = [{"original_position": i, "marker": i} for i in range(3)]
    if [r["marker"] for r in selected_records(records, (2, 0), count=3)] != [2, 0]:
        raise AssertionError("archived basis selection order")
    for rows, positions in ((records, (0,0)),
        ([records[0],records[0],records[2]], (0,2)), (records, (3,))):
        try:
            selected_records(rows, positions, count=3)
        except ValueError:
            continue
        raise AssertionError("invalid archived position accepted")
    checks["archived_index_order_and_duplicate_missing_rejection"] = True
    limits = exact.Limits(seconds=30,nodes=8000,atoms=4000,terms=8000,
        rewrites=20000,memory_mib=512)
    ring = colored.ColoredRing(limits)
    q,x = ring.jet(),ring.x()
    originals = [q**4, q*q*q.D()*q.D()]
    producer = quotient.ProfileNormalizer(ring,20000,8000)
    vectors = [producer.expression(value) for value in originals]
    archive = [{"original_position":i,"original_root":"toy_%d"%i,
        "original_sha256":ring.digest(value),
        "word_summary":producer.word.summary(vector),"word_rows":pure.word_rows(vector)}
        for i,(value,vector) in enumerate(zip(originals,vectors))]
    consumer = quotient.ProfileNormalizer(ring,20000,8000)
    decoded = [bind_word_row(consumer,row,ring.digest(value),"toy_%d"%i)
        for i,(row,value) in enumerate(zip(archive,originals))]
    if any(a.digest()!=b.digest() for a,b in zip(decoded,vectors)):
        raise AssertionError("archived word representative changed")
    if consumer.legacy.stats["primitive_calls"] or consumer.word.stats["primitive_calls"]:
        raise AssertionError("decoding archived representatives normalized old originals")
    checks["portable_basis_decode_has_no_old_normalization"] = True
    for bad in ({**archive[0],"original_sha256":"0"*64},
        {**archive[0],"original_root":"wrong"},
        {**archive[0],"word_summary":{**archive[0]["word_summary"],"sha256":"0"*64}}):
        try:
            bind_word_row(consumer,bad,ring.digest(originals[0]),"toy_0")
        except ValueError:
            continue
        raise AssertionError("an archive binding change was accepted")
    checks["changed_original_or_word_binding_rejected"] = True
    tiny = argparse.Namespace(max_IBP_calls=20000,max_terms=8000)
    target = F(3,7)*originals[0]+F(5,11)*originals[1]
    coefficients,difference,proof,_,_ = solve_once(
        ring,consumer,target,originals,decoded,limits,tiny)
    if (coefficients!={0:F(3,7),1:F(5,11)}
        or not proof["original_identity_proved"]
        or not proof["coefficients_are_exact_Q_not_modular_lifts"]):
        raise AssertionError("new rational target original proof")
    checks["one_new_target_Q_solve_and_fresh_original_zero"] = True
    consumer2 = quotient.ProfileNormalizer(ring,20000,8000)
    decoded2 = [bind_word_row(consumer2,row,ring.digest(value),"toy_%d"%i)
        for i,(row,value) in enumerate(zip(archive,originals))]
    _,bad_difference,bad_proof,_,_ = solve_once(
        ring,consumer2,target+x**3*q**4,originals,decoded2,limits,tiny)
    if bad_proof["original_identity_proved"] or not bad_proof["nonzero_representative_is_not_nonmembership"]:
        raise AssertionError("nonzero sound remainder was promoted")
    checks["unresolved_original_remainder_is_not_nonmembership"] = True
    named={"new_target":target,"proposed_difference":difference,
        "unresolved_difference":bad_difference}
    payload=old.serialize_expressions(ring,named)
    restored=old.decode_expressions(ring,json.loads(pure.data_bytes(payload)))
    if any(ring.digest(restored[k])!=ring.digest(v) for k,v in named.items()):
        raise AssertionError("new portable original certificate")
    checks["new_original_roots_round_trip"] = True
    return {"checks":checks,"all_passed":all(checks.values()),
        "published_reports_or_roots_read":False,
        "research_profile_or_geometry_evaluated":False,
        "old_forty_basis_or_thirty_one_relations_recomputed":False,
        "new_response_or_forcing_compiled":False}


def write_main(args,report):
    raw=pure.data_bytes(report,pretty=True)
    if len(raw)>args.max_main_bytes:
        path=args.output.with_name(args.output.stem+"-complete-report.json.gz")
        metadata=pure.store_gzip(path,report,args.max_full_report_bytes)
        compact={k:v for k,v in report.items() if k not in
            ("D0_input","input_pure_basis","normalizer_statistics")}
        compact["complete_report_file"]=metadata
        raw=pure.data_bytes(compact,pretty=True)
        if len(raw)>args.max_main_bytes:
            compact={k:report.get(k) for k in (
                "schema","completion","phase","scope","github_repository",
                "github_run_id","github_sha","source_hashes","result","error",
                "elapsed_seconds","peak_rss_mib","portable_original_certificate")}
            compact["complete_report_file"]=metadata
            compact["full_result_preserved"]=True
            raw=pure.data_bytes(compact,pretty=True)
        if len(raw)>args.max_main_bytes:
            raise ValueError("source-bound compact main exceeded the output budget")
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_bytes(raw)
    return {"filename":args.output.name,"bytes":len(raw),"sha256":pure.sha(raw),
        "completion":report["completion"]}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only",action="store_true")
    parser.add_argument("--output",type=Path,required=True)
    ddir=TOPIC/("notes/actions-"+target_io.D0_RUN+"-1-h_axis_sharp")
    bdir=TOPIC/("notes/actions-"+BASIS_RUN+"-1-"+BASIS_LANE)
    parser.add_argument("--D0-report",type=Path,default=ddir/"h-axis-sharp.json")
    parser.add_argument("--D0-publication",type=Path,default=ddir/"receipt.json")
    parser.add_argument("--D0-export",type=Path,default=ddir/target_io.D0_EXPORT["filename"])
    parser.add_argument("--basis-directory",type=Path,default=bdir)
    parser.add_argument("--max-seconds",type=float,default=180)
    parser.add_argument("--memory-mib",type=int,default=1024)
    parser.add_argument("--max-nodes",type=int,default=500000)
    parser.add_argument("--max-atoms",type=int,default=100000)
    parser.add_argument("--max-terms",type=int,default=120000)
    parser.add_argument("--max-IBP-calls",type=int,default=500000)
    parser.add_argument("--max-rational-bits",type=int,default=8192)
    parser.add_argument("--max-main-bytes",type=int,default=90000)
    parser.add_argument("--max-certificate-bytes",type=int,default=1500000)
    parser.add_argument("--max-full-report-bytes",type=int,default=2000000)
    args=parser.parse_args()
    if min(args.max_seconds,args.memory_mib,args.max_nodes,args.max_atoms,
        args.max_terms,args.max_IBP_calls,args.max_rational_bits,
        args.max_certificate_bytes,args.max_full_report_bytes)<=0:
        parser.error("positive resource bounds required")
    if not 10000<=args.max_main_bytes<100000:
        parser.error("reserve 10000..99999 bytes for the source-bound main")
    if args.max_main_bytes+args.max_certificate_bytes+args.max_full_report_bytes>pure.TOTAL_OUTPUT_BYTES:
        parser.error("declared output exceeds the reserved total byte bound")
    if not args.toy_only and not (os.environ.get("GITHUB_ACTIONS")=="true"
        and os.environ.get("GITHUB_REPOSITORY")==REPOSITORY):
        parser.error("the new D0 pure target is public-repository-Actions-only")
    started,code=time.monotonic(),0
    report={"schema":SCHEMA,"completion":"started","phase":"bind_frozen_input_helpers",
        "scope":"only D0 pure against nine archived true bases and exact representatives",
        "github_repository":os.environ.get("GITHUB_REPOSITORY"),
        "github_run_id":os.environ.get("GITHUB_RUN_ID"),"github_sha":os.environ.get("GITHUB_SHA"),
        "source_hashes":{},
        "work_scope":{"new_general_pure_targets":1,"new_response_formulas":0,
            "old_basis_roots_renormalized":0,"old_pure_dependencies_recomputed":0,
            "old_mixed_or_profile_evaluations":0,"new_profile_evaluations":0,
            "old_N2_v4_forcing_recompiled":0,"modular_lifts_used_as_Q_coefficients":False},
        "limits":{"seconds":args.max_seconds,"memory_polling_mib":args.memory_mib,
            "nodes":args.max_nodes,"atoms":args.max_atoms,"terms":args.max_terms,
            "IBP_calls_per_normalizer":args.max_IBP_calls,
            "rational_bits_in_span":args.max_rational_bits,
            "main_bytes":args.max_main_bytes,"certificate_bytes":args.max_certificate_bytes,
            "full_report_bytes":args.max_full_report_bytes}}
    try:
        report["source_hashes"]=source_identity()
        if args.toy_only:
            report["phase"]="new_archive_and_single_target_artificial_interfaces"
            report["toy"]=artificial_toys()
            report["completion"]="toy_passed"
        else:
            run_research(args,report)
    except formal.CompilationBudgetExceeded as error:
        report["completion"],report["error"],code="resource_limit",str(error),2
    except Exception as error:
        report["completion"],code="implementation_check_failed",1
        report["error"]={"type":type(error).__name__,"message":str(error)}
    report["elapsed_seconds"]=time.monotonic()-started
    report["peak_rss_mib"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    written=write_main(args,report)
    print(json.dumps({"output":str(args.output),**written}),flush=True)
    return code


if __name__=="__main__":
    raise SystemExit(main())
