#!/usr/bin/env python3
"""Project published static local -4 density into the published m8 response quotient.

This consumer imports original expressions and complete response polynomials.
It never recompiles W, lower fields, fourth forcing, or any old response column.
The local target already is the complete -4 phase coefficient; no /16 is added.
Only this public repository's Actions may evaluate the research inputs.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
import gzip
import io
import json
import os
from pathlib import Path
import resource
import time

import literature_full_m8_tail_response_projection as projection
import literature_local_fourth_quotient as local4
import literature_colored_profile_algebra as colored
import literature_full_phase_rational_dual as dual
import literature_pure_bulk_exact_membership as exact
import literature_total_P1_scaling_blocks as blocks

SCHEMA = "visible-flex-static-local-m8-tail-response-quotient-v1"
REPOSITORY = projection.REPOSITORY
TOPIC = Path(__file__).resolve().parents[1]
LOCAL_DIRECTORY = TOPIC/"notes/actions-43645177423-1-local_fourth_quotient"
RESPONSE_DIRECTORY = TOPIC/"notes/actions-43646543691-1-full_m8_tail_response_projection"
MAX_REPORT_BYTES = 95000
MAX_RAW_BYTES = 40000000
MAX_STORED_BYTES = 4800000
LOCAL_RUN = "43645177423"
LOCAL_COMMIT = "2f1b809c0b0abb7a26303d36940edc203815f872"
RESPONSE_RUN = "43646543691"
RESPONSE_COMMIT = "f0652a013fe546778300f0213e659f63ab96ed07"
LOCAL_DRIVER_SHA = "9aa5b1360032bfebeb379d965873dc5b877c41885d8834fc1945d44d44a4dcf0"
RESPONSE_DRIVER_SHA = "e66bf0d2f41570526d5e6b05aedc28118a18a492a299e097d341cc71e804e345"
LOCAL_MAIN = {"bytes": 3982, "sha256": "19228a0aecf40416cf7ba7b8a7fa4e0180ed924a4bd04435b0e6e6e4a0b1b28a"}
LOCAL_RECEIPT = {"bytes": 31846, "sha256": "c9206d68c786613e84e4f080d2a6899b46333979e88b16f0d5306a6c88e8c0ba"}
LOCAL_EXPORT = {
    "filename": "local-fourth-quotient-original-expressions.json.gz",
    "stored_bytes": 657195,
    "stored_sha256": "ea8ba97319ef3fa43ff8cacc7f98b106b13280aef4641b969f5f820194aebace",
    "raw_bytes": 3518194,
    "raw_sha256": "d74e87790a00a246e01438c54575c3190389e3adbdefed0cec233b6ec9a664d1"}
RESPONSE_MAIN = {"bytes": 9591, "sha256": "7237cadaac3c4581862d8aee86b94692f0e2436ab7fdb7e393c7b721125d61a7"}
RESPONSE_RECEIPT = {"bytes": 31399, "sha256": "640bf2e0f17bfa635dc688581a192855f372bc7aa840c0ad97614d8696e59de1"}
RESPONSE_EXPORT = {
    "filename": "full-m8-tail-response-certificate.json.gz",
    "stored_bytes": 44576,
    "stored_sha256": "b0859868f2db2a08ca1b2831e5ab010840eed8e7ebda01fca49d598822d147a4",
    "raw_bytes": 274274,
    "raw_sha256": "a8b5577903e419d2eabe2c327c2c721401acea2d0845017f86c260b2ddb8c36c"}
G_GEOMETRY_KEY = (1, 3, 0, 0, 0, 0, 0, 0)
G_WEIGHT = 1
G_PROJECTED_ORIGINAL_SHA = "4608912701e99a514cff0dcb93b896200beeb6e3cbead9a70547b78e00d18c7a"

canonical = projection.canonical
sha = projection.sha
identity = projection.identity
add_sparse = projection.add_sparse


def dependencies():
    original = projection.dependencies()
    if original["driver"]["sha256"] != RESPONSE_DRIVER_SHA:
        raise ValueError("rebind the frozen successful response consumer explicitly")
    if original["portable_expression_producer"]["sha256"] != LOCAL_DRIVER_SHA:
        raise ValueError("rebind the original local expression producer explicitly")
    result = dict(original)
    result["complete_response_projection"] = result.pop("driver")
    result["driver"] = identity(__file__)
    return result


def read_bound_json(path, expected):
    raw = projection.checked_bytes(path, MAX_STORED_BYTES)
    if len(raw) != expected["bytes"] or sha(raw) != expected["sha256"]:
        raise ValueError("published input bytes or SHA-256 changed: "+path.name)
    return json.loads(raw)


def read_bound_gzip(path, expected):
    stored = projection.checked_bytes(path, MAX_STORED_BYTES)
    if len(stored) != expected["stored_bytes"] or sha(stored) != expected["stored_sha256"]:
        raise ValueError("published complete gzip bytes changed: "+path.name)
    with gzip.GzipFile(fileobj=io.BytesIO(stored)) as stream:
        raw = stream.read(MAX_RAW_BYTES+1)
    if (len(raw) > MAX_RAW_BYTES or len(raw) != expected["raw_bytes"]
            or sha(raw) != expected["raw_sha256"]):
        raise ValueError("published complete uncompressed bytes changed: "+path.name)
    return json.loads(raw)


def require_export_metadata(observed, expected):
    if not observed or any(observed.get(k) != v for k, v in expected.items()):
        raise ValueError("main report does not bind the exact complete exported file")


def verify_response_receipt(receipt, source_report):
    if (receipt.get("schema") != "visible-new-mechanism-actions-v1"
            or receipt.get("repository") != REPOSITORY
            or str(receipt.get("run_id")) != RESPONSE_RUN
            or receipt.get("source_commit") != RESPONSE_COMMIT
            or receipt.get("lane") != "full_m8_tail_response_projection"):
        raise ValueError("response publication receipt source or lane mismatch")
    producer = source_report["source_hashes"]["driver"]
    key = "topics/visible-flex-new-mechanism/scripts/"+producer["filename"]
    if receipt.get("source_files", {}).get(key) != {
            "bytes": producer["bytes"], "sha256": producer["sha256"]}:
        raise ValueError("response receipt does not bind the real source")
    wanted = (
        ("full-m8-tail-response.json", RESPONSE_MAIN["bytes"], RESPONSE_MAIN["sha256"],
         RESPONSE_MAIN["bytes"], RESPONSE_MAIN["sha256"]),
        (RESPONSE_EXPORT["filename"], RESPONSE_EXPORT["stored_bytes"], RESPONSE_EXPORT["stored_sha256"],
         RESPONSE_EXPORT["raw_bytes"], RESPONSE_EXPORT["raw_sha256"]))
    for name, count, digest, raw_count, raw_digest in wanted:
        matches = [row for row in receipt.get("outputs", []) if row.get("path") == name]
        if len(matches) != 1 or any(matches[0].get(k) != v for k, v in (
                ("bytes", count), ("sha256", digest),
                ("raw_bytes", raw_count), ("raw_sha256", raw_digest))):
            raise ValueError("response receipt output identity mismatch")
    return {"source_run": RESPONSE_RUN, "source_commit": RESPONSE_COMMIT,
            "receipt_sha256": RESPONSE_RECEIPT["sha256"],
            "source_driver_sha256": producer["sha256"]}


def polynomial_rows(value):
    return [{"c_power": a, "r_power": b, "coefficient": str(v)}
            for (a, b), v in sorted(value.items()) if v]


def polynomial_from_rows(rows):
    value = {}
    for row in rows:
        key = row["c_power"], row["r_power"]
        coefficient = F(row["coefficient"])
        if (any(type(n) is not int or n < 0 for n in key)
                or key in value or not coefficient):
            raise ValueError("malformed published complete polynomial")
        value[key] = coefficient
    return value


def split_weights(value):
    result = {}
    for key, coefficient in value.items():
        result.setdefault(sum(key)-32, {})[key] = coefficient
    return result


def reduce_target(span, value, ring):
    """Return original-column coefficients and the whole polynomial remainder."""
    remaining, coefficients = dict(value), {}
    if span is not None:
        for pivot in sorted(span.basis):
            factor = remaining.get(pivot, F(0))
            if factor:
                row, original = span.basis[pivot]
                add_sparse(remaining, row, -factor, ring)
                add_sparse(coefficients, original, factor, ring)
    difference = dict(value)
    if span is not None:
        for index, coefficient in coefficients.items():
            add_sparse(difference, span.original[index], -coefficient, ring)
    add_sparse(difference, remaining, F(-1), ring)
    if difference:
        raise AssertionError("new target complete polynomial reconstruction failed")
    return coefficients, remaining


def require_pure_fourth(source_ring, expression):
    degrees = source_ring.color_degrees(expression)
    if degrees and degrees != {(("q", 4),)}:
        raise ValueError("the selected -4 root contains an unexpected actual color or profile degree")


def load_response(args, ring, report):
    source = read_bound_json(args.response_report, RESPONSE_MAIN)
    receipt = read_bound_json(args.response_publication_receipt, RESPONSE_RECEIPT)
    if (source.get("schema") != projection.SCHEMA or source.get("completion") != "complete"
            or str(source.get("github_run_id")) != RESPONSE_RUN
            or source.get("github_sha") != RESPONSE_COMMIT
            or source.get("source_hashes") != projection.dependencies()
            or source.get("total_original_columns") != 288
            or not source.get("all_projected_dependency_differences_zero")):
        raise ValueError("the successful complete response source is required")
    publication = verify_response_receipt(receipt, source)
    require_export_metadata(source.get("complete_certificate"), RESPONSE_EXPORT)
    data = read_bound_gzip(args.response_certificate, RESPONSE_EXPORT)
    if (data.get("schema") != projection.SCHEMA+"-certificate"
            or data.get("source_hashes") != source["source_hashes"]
            or data.get("exact_weight_blocks", {}).keys() != source["exact_weight_blocks"].keys()
            or data.get("exact_full_projection_rank") != 31
            or data.get("exact_four_block_projection_rank") != 15
            or data.get("template_input") != source["template_input"]):
        raise ValueError("complete response certificate and published main disagree")
    records = data["columns"]
    if len(records) != 288 or [row["index"] for row in records] != list(range(288)):
        raise ValueError("all original response column identities are required")
    polynomials, supports = {}, {}
    for item in records:
        index, weight = item["index"], item["response_weight"]
        ai, ti = index % 8, index // 8
        if (item["quadratic_index"] != ai or item["third_index"] != ti
                or item["v2_original_third_index"] != blocks.EXPECTED_KEPT[ti]
                or weight != blocks.PARAMETER_WEIGHTS[ai]+blocks.THIRD_WEIGHTS[ti]
                or sha(canonical(item["complete_polynomial"])) != item["complete_polynomial_sha256"]):
            raise ValueError("published original response column metadata changed")
        value = polynomial_from_rows(item["complete_polynomial"])
        if any(sum(key) != 32+weight for key in value):
            raise ValueError("published response homogeneous degree mismatch")
        polynomials[index] = value
        supports.setdefault(weight, set()).update(value)
    spans = {}
    for label, summary in sorted(data["exact_weight_blocks"].items(), key=lambda item: int(item[0])):
        weight = int(label)
        compact = source["exact_weight_blocks"][label]
        selected = summary["independent_original_columns"]
        if (selected != compact["independent_original_columns"]
                or len(selected) != compact["exact_rank_over_Q"]):
            raise ValueError("published independent-column list changed")
        span = projection.ExactProjectedSpan(ring)
        # Factorize only the 31 already published basis columns for the NEW targets.
        # Do not reevaluate the response formula or repeat 257 old dependencies.
        for index in selected:
            if records[index]["response_weight"] != weight:
                raise ValueError("response basis column in wrong homogeneous block")
            span.add(index, polynomials[index])
        if (span.independent != selected or span.dependencies
                or span.pivot_records != summary["pivot_records"]):
            raise ValueError("the imported basis factorization disagrees with its certificate")
        spans[weight] = span
    full_support = sorted({key for support in supports.values() for key in support})
    if (full_support != [tuple(key) for key in data["all_monomial_rows"]]
            or len(full_support) != 45):
        raise ValueError("complete published response support mismatch")
    report["response_input"] = {
        "publication": publication, "main": RESPONSE_MAIN, "complete_export": RESPONSE_EXPORT,
        "published_projection_rank": 31, "published_four_block_rank": 15,
        "original_polynomials_loaded": 288, "published_basis_columns_factorized": 31,
        "old_response_formula_evaluations": 0, "old_dependency_checks_repeated": 0,
        "scope": "complete m8 pure right-tail response projection, not full operator relations"}
    return spans, supports, data["template_input"]["bound_W"]


def load_local(args, source_ring, report, response_W_binding):
    source = read_bound_json(args.local_report, LOCAL_MAIN)
    receipt = read_bound_json(args.local_publication_receipt, LOCAL_RECEIPT)
    if source.get("schema") != local4.SCHEMA or source.get("source_hashes") != local4.dependencies():
        raise ValueError("frozen original local source identity mismatch")
    metadata = source.get("portable_original_expression_export")
    require_export_metadata(metadata, LOCAL_EXPORT)
    publication = projection.verify_publication_binding(receipt,
        source_run=LOCAL_RUN, source_commit=LOCAL_COMMIT,
        report_name="local-fourth-quotient.json", report_bytes=LOCAL_MAIN["bytes"],
        report_sha=LOCAL_MAIN["sha256"], export_record=metadata,
        driver_identity=source["source_hashes"]["driver"])
    data = read_bound_gzip(args.local_export, LOCAL_EXPORT)
    if (data.get("schema") != local4.SCHEMA+"-original-expressions"
            or data.get("source_hashes") != source["source_hashes"]
            or data.get("content_scope") != "W-and-local-static-density"
            or data.get("projection") != "derivative weight zero"
            or data.get("geometry_names") != list(local4.local.NAMES)):
        raise ValueError("complete static local export scope or sources changed")
    roots = local4.decode_expressions(source_ring, data)
    if len(roots) != 430 or len(data["profile_atoms"]) != 3319:
        raise ValueError("complete original local export coverage changed")
    third_receipt = dual.read_receipt(args.third_receipt)
    retained = third_receipt["pre_response_reduction"]["retained_original_indices"]
    if retained != blocks.EXPECTED_KEPT:
        raise ValueError("bound true W36 retained indices changed")
    wanted = [third_receipt["all_original_control_templates"][j]["original_template_sha256"]
              for j in retained]
    got = [source_ring.digest(roots["W"+str(j)]) for j in range(36)]
    binding = data["bound_W"]
    if (binding.get("receipt_sha256") != dual.RECEIPT_SHA
            or binding.get("retained_original_indices") != retained
            or binding.get("original_152_hashes_matched") is not True
            or binding.get("raw_template_hashes") != wanted or got != wanted
            or response_W_binding.get("raw_template_hashes") != got):
        raise ValueError("local and response exports must use the same 36 true original roots")
    pure_records, seen, names = [], set(), set()
    for entry in data["local_roots"]:
        mode, key, name = entry["mode"], tuple(entry["geometry_key"]), entry["root"]
        if (mode not in (-4, -2) or len(key) != 8 or any(type(n) is not int for n in key)
                or local4.jet_weight(key) or (mode, key) in seen
                or name in names or name not in roots or name.startswith("W")):
            raise ValueError("original static geometry coefficient record malformed")
        seen.add((mode, key))
        names.add(name)
        if mode == -4:
            require_pure_fourth(source_ring, roots[name])
            pure_records.append((key, name, roots[name]))
    if names | {"W"+str(j) for j in range(36)} != set(roots):
        raise ValueError("every original exported root must have its complete declared role")
    report["local_input"] = {
        "publication": publication, "publication_receipt": LOCAL_RECEIPT,
        "main": LOCAL_MAIN, "main_completion": source.get("completion"),
        "complete_export": LOCAL_EXPORT, "content_scope": data["content_scope"],
        "geometry_names": data["geometry_names"], "total_original_roots": len(roots),
        "total_local_geometry_roots": len(names), "pure_minus_four_roots": len(pure_records),
        "all_original_root_hashes_verified": True, "same_true_W36_as_response": True,
        "raw_geometry_derivative_weight": 0,
        "local_forcing_recompiled": False, "W_recompiled": False,
        "mixed_minus_two_roots_evaluated": False,
        "local_phase_already_minus_four_no_extra_division": True}
    return sorted(pure_records), roots


def write_gzip(path, value):
    raw = canonical(value)
    if len(raw) > MAX_RAW_BYTES:
        raise RuntimeError("complete new quotient certificate exceeds raw byte budget")
    stored = gzip.compress(raw, mtime=0)
    if len(stored) > MAX_STORED_BYTES:
        raise RuntimeError("complete new quotient certificate exceeds packed byte budget")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(stored)
    return {"filename": path.name, "stored_bytes": len(stored), "stored_sha256": sha(stored),
            "raw_bytes": len(raw), "raw_sha256": sha(raw)}


def actual(args, report):
    if (os.environ.get("GITHUB_ACTIONS", "").lower() != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise RuntimeError("actual local tail projection only in this public repository Actions")
    started = time.monotonic()
    ring = projection.TailRing(args.max_seconds, args.memory_mib, args.max_operations)
    limits = exact.Limits(seconds=args.max_seconds, nodes=300000, atoms=60000,
                          terms=80000, rewrites=1000, memory_mib=args.memory_mib)
    source_ring = colored.ColoredRing(limits)
    response_spans, supports, W_binding = load_response(args, ring, report)
    local_records, _ = load_local(args, source_ring, report, W_binding)
    evaluator = projection.OriginalTailEvaluator(source_ring.p, ring, {"q": ring.power_tail(8)})
    quotient_spans, component_records, target_records = {}, [], []
    counts, outside, G = {}, {}, None
    for target_index, (geometry_key, name, original) in enumerate(local_records):
        value = evaluator.expression(original)
        components = split_weights(value.terms)
        target_records.append({
            "target_index": target_index, "source_root": name, "geometry_key": list(geometry_key),
            "original_sha256": source_ring.digest(original),
            "complete_polynomial": value.rows(),
            "complete_polynomial_sha256": sha(canonical(value.rows())),
            "weights_after_exact_substitution": sorted(components)})
        for weight, polynomial in sorted(components.items()):
            span = response_spans.get(weight)
            coefficients, remainder = reduce_target(span, polynomial, ring)
            index = len(component_records)
            quotient_spans.setdefault(weight, projection.ExactProjectedSpan(ring)).add(index, remainder)
            beyond = {key: v for key, v in remainder.items() if key not in supports.get(weight, set())}
            stats = counts.setdefault(weight, Counter())
            stats["nonzero_target_components"] += 1
            stats["members_of_published_tail_response"] += not remainder
            stats["nonzero_quotient_remainders"] += bool(remainder)
            stats["remainders_with_rows_outside_response_support"] += bool(beyond)
            outside.setdefault(weight, set()).update(beyond)
            record = {
                "component_index": index, "target_index": target_index,
                "source_root": name, "geometry_key": list(geometry_key), "weight": weight,
                "total_degree": 32+weight, "complete_polynomial": polynomial_rows(polynomial),
                "original_response_column_coefficients": [[j, str(v)] for j, v in sorted(coefficients.items())],
                "complete_remainder": polynomial_rows(remainder),
                "outside_response_support": polynomial_rows(beyond),
                "complete_polynomial_decomposition_difference_zero": True,
                "belongs_to_published_tail_projection": not remainder}
            component_records.append(record)
        if geometry_key == G_GEOMETRY_KEY:
            projected = blocks.ScalingGrading(source_ring).project(original, G_WEIGHT)
            digest = source_ring.digest(projected)
            if digest != G_PROJECTED_ORIGINAL_SHA:
                raise ValueError("R117 G original homogeneous coefficient identity mismatch")
            G_polynomial = components.get(G_WEIGHT, {})
            coefficients, remainder = reduce_target(response_spans.get(G_WEIGHT), G_polynomial, ring)
            G = {
                "source_geometry_key": list(geometry_key), "source_root": name,
                "true_profile_weight": G_WEIGHT, "projected_original_sha256": digest,
                "complete_m8_pure_polynomial": polynomial_rows(G_polynomial),
                "original_response_column_coefficients": [[j, str(v)] for j, v in sorted(coefficients.items())],
                "complete_remainder": polynomial_rows(remainder),
                "belongs_to_published_rank_one_weight_one_projection": not remainder,
                "original_complete_two_mode_membership_asserted": False,
                "original_complete_two_mode_nonmembership_test_repeated": False}
        report["completed_pure_local_roots"] = target_index+1
        ring.guard()
    if G is None:
        raise ValueError("the specifically bound R117 G geometry coefficient is required")
    summaries = {}
    for weight in sorted(set(response_spans) | set(quotient_spans)):
        base = response_spans.get(weight)
        quotient = quotient_spans.get(weight)
        response_rank = len(base.independent) if base else 0
        quotient_rank = len(quotient.independent) if quotient else 0
        summaries[str(weight)] = {
            "response_rank_imported": response_rank,
            "new_static_local_quotient_rank": quotient_rank,
            "combined_response_and_static_local_rank": response_rank+quotient_rank,
            **dict(counts.get(weight, {})),
            "independent_new_remainder_components": quotient.independent if quotient else [],
            "outside_response_support_rows": [list(key) for key in sorted(outside.get(weight, set()))]}
    quotient_rank = sum(len(span.independent) for span in quotient_spans.values())
    closed_quotient_rank = sum(len(span.independent) for weight, span in quotient_spans.items() if weight % 2 == 0)
    certificate = {
        "schema": SCHEMA+"-certificate", "source_hashes": report["source_hashes"],
        "github_run_id": report["github_run_id"], "github_sha": report["github_sha"],
        "local_input": report["local_input"], "response_input": report["response_input"],
        "profile": "q=(c-xi)^8 with r=c-xi and the same actual right anchor c",
        "phase": "the original local -4 phase coefficient; no extra /16",
        "geometry_names": list(local4.local.NAMES),
        "targets": target_records, "homogeneous_components": component_records,
        "weight_summaries": summaries,
        "exact_quotient_bases": {str(weight): span.summary() for weight, span in sorted(quotient_spans.items())},
        "R117_G_pure_projection": G,
        "all_new_complete_polynomial_decompositions_verified": True,
        "new_static_coefficient_quotient_rank": quotient_rank,
        "even_total_degree_quotient_rank": closed_quotient_rank,
        "actual_period_or_geometric_obstruction_asserted": False}
    exported = write_gzip(args.out.with_name(args.out.stem+"-certificate.json.gz"), certificate)
    report.update(
        completion="complete", complete_certificate=exported,
        new_static_pure_local_roots_evaluated=len(target_records),
        nonzero_projected_local_roots=sum(bool(row["complete_polynomial"]) for row in target_records),
        new_homogeneous_target_components=len(component_records),
        new_static_coefficient_quotient_rank=quotient_rank,
        even_total_degree_quotient_rank=closed_quotient_rank,
        weight_summaries=summaries, R117_G_pure_projection=G,
        all_new_complete_polynomial_decomposition_differences_zero=True,
        polynomial_operations=ring.operations, linear_operations=ring.linear_operations,
        raw_original_atoms_evaluated=ring.raw_atoms_evaluated,
        raw_original_monomials_evaluated=ring.raw_monomials_evaluated,
        maximum_intermediate_terms=ring.maximum_terms,
        elapsed_seconds=time.monotonic()-started,
        peak_rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024,
        geometry_derivative_weights_two_and_four_evaluated=False,
        true_M0_geometry_constraints_applied=False,
        actual_baseline_cost_evaluated=False, actual_period_nonmembership_claimed=False,
        whole_U4_or_complete_operator_quotient_dimension_claimed=False,
        complete_m8_tail_period_paid=False, mixed_mode_or_ruling_paid=False,
        old_forcing_recompiled=False, old_response_columns_recomputed=False, task_complete=False)
    return report


def toy_only():
    ring = projection.TailRing(40, 256, 100000)
    span = projection.ExactProjectedSpan(ring)
    span.add(7, {(1, 0): F(1), (0, 1): F(1)})
    value = {(1, 0): F(3), (0, 1): F(3)}
    coefficients, residual = reduce_target(span, value, ring)
    member = coefficients == {7: F(3)} and not residual
    coefficients, residual = reduce_target(span, {(1, 0): F(1)}, ring)
    inside_not_member = bool(residual) and all(key in span.original[7] for key in residual)
    coefficients, residual = reduce_target(span, {(2, 0): F(5)}, ring)
    outside_not_member = not coefficients and residual == {(2, 0): F(5)}
    empty = reduce_target(span, {}, ring) == ({}, {})
    parts = split_weights({(1, 1): F(2), (0, 3): F(-5), (2, 0): F(3)})
    recovered = {}
    for part in parts.values():
        add_sparse(recovered, part, F(1), ring)
    homogeneous = (set(parts) == {-30, -29}
        and recovered == {(1, 1): F(2), (0, 3): F(-5), (2, 0): F(3)})
    limits = exact.Limits(seconds=40, nodes=10000, atoms=10000, terms=10000,
                          rewrites=10000, memory_mib=256)
    source = colored.ColoredRing(limits)
    q, qb = source.color("q"), source.color("qbar")
    require_pure_fourth(source, q*q*q*q)
    mixed_rejected = False
    try:
        require_pure_fourth(source, q*q*q*qb)
    except ValueError:
        mixed_rejected = True
    checks = {
        "new_target_exact_member_coefficients": member,
        "new_target_nonmember_even_inside_the_old_row_support": inside_not_member,
        "new_target_outside_support_is_retained": outside_not_member,
        "zero_target_has_zero_remainder": empty,
        "homogeneous_decomposition_keeps_every_term": homogeneous,
        "pure_mode_color_gate_rejects_mixed_root": mixed_rejected,
        "no_research_input_read_or_actual_m8_profile_evaluated": True}
    if not all(checks.values()):
        raise AssertionError("new artificial target-reduction check failed")
    return {"completion": "complete", "mode": "small_artificial_development_only",
            "checks": checks, "all_passed": True, "task_complete": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--toy-only", action="store_true")
    parser.add_argument("--local-report", type=Path, default=LOCAL_DIRECTORY/"local-fourth-quotient.json")
    parser.add_argument("--local-publication-receipt", type=Path, default=LOCAL_DIRECTORY/"receipt.json")
    parser.add_argument("--local-export", type=Path, default=LOCAL_DIRECTORY/LOCAL_EXPORT["filename"])
    parser.add_argument("--response-report", type=Path, default=RESPONSE_DIRECTORY/"full-m8-tail-response.json")
    parser.add_argument("--response-publication-receipt", type=Path, default=RESPONSE_DIRECTORY/"receipt.json")
    parser.add_argument("--response-certificate", type=Path, default=RESPONSE_DIRECTORY/RESPONSE_EXPORT["filename"])
    parser.add_argument("--third-receipt", type=Path, default=dual.DEFAULT_RECEIPT)
    parser.add_argument("--max-seconds", type=float, default=240)
    parser.add_argument("--memory-mib", type=int, default=1024)
    parser.add_argument("--max-operations", type=int, default=10000000)
    args = parser.parse_args()
    started = time.monotonic()
    report = {"schema": SCHEMA, "completion": "started",
        "github_run_id": os.environ.get("GITHUB_RUN_ID"),
        "github_sha": os.environ.get("GITHUB_SHA"), "task_complete": False}
    failed = False
    try:
        report["source_hashes"] = dependencies()
        report.update(toy_only() if args.toy_only else actual(args, report))
    except Exception as error:
        failed = True
        report.update(completion="incomplete", error_type=type(error).__name__, error=str(error),
                      new_mathematical_conclusion_published=False, task_complete=False)
    report["wall_seconds"] = time.monotonic()-started
    raw = canonical(report)+b"\n"
    if len(raw) > MAX_REPORT_BYTES:
        full = write_gzip(args.out.with_name(args.out.stem+"-full-report.json.gz"), report)
        report = {k: report[k] for k in ("schema", "completion", "github_run_id", "github_sha",
                  "source_hashes", "wall_seconds", "task_complete", "complete_certificate",
                  "local_input", "response_input", "new_static_pure_local_roots_evaluated",
                  "new_homogeneous_target_components", "new_static_coefficient_quotient_rank",
                  "even_total_degree_quotient_rank", "R117_G_pure_projection",
                  "error_type", "error") if k in report}
        report.update(compact_fallback=True, complete_report=full)
        raw = canonical(report)+b"\n"
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_bytes(raw)
    print(json.dumps({"filename": args.out.name, "bytes": len(raw), "sha256": sha(raw)}, sort_keys=True), flush=True)
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
