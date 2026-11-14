#!/usr/bin/env python3
"""Apply the full M=0 matrix constraint to published static m8 tail polynomials.

The old pure profile substitutions and response polynomials are read, not rerun.
The static normalization and its compulsory geometry-weight-two correction are
both retained. No claim is made that the original weight-two/four density was
computed or that a real zero-matrix path was evaluated.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import json
import os
from pathlib import Path
import resource
import time

import literature_static_m8_tail_quotient as first
import literature_constrained_static_fourth as constrained

projection = first.projection
old = first.local4
SCHEMA = "visible-flex-constrained-static-m8-tail-quotient-v1"
REPOSITORY = first.REPOSITORY
TOPIC = Path(__file__).resolve().parents[1]
SOURCE_DIRECTORY = TOPIC/"notes/actions-43648433010-1-static_m8_tail_quotient"
SOURCE_RUN = "43648433010"
SOURCE_COMMIT = "df535c0c42d76040903b1e89c6d08d13ea360ad2"
SOURCE_DRIVER_SHA = "ea95f138a22b6f81654ebbc73eecee3f3c0042f4ec527f6ff9699e6ac78bb826"
CONSTRAINT_HELPER_SHA = "814e1338679914b32542f8b360978281002ee02a2c4e8c03912aa40c876786f4"
SOURCE_MAIN = {"bytes": 10305, "sha256": "f48539fb8e38fda987aa97bbdf22b940ebe5525261b989e4afedcba628e96dcc"}
SOURCE_RECEIPT = {"bytes": 32674, "sha256": "c21fc44371341f514e685842c2addee903ebb9fe338e3669e195cdd4b0c66bdd"}
SOURCE_EXPORT = {
    "filename": "static-m8-tail-quotient-certificate.json.gz",
    "stored_bytes": 47339,
    "stored_sha256": "28e4e42ab2ee7c53b26b2df43d18c3622e2798424958656fbb9ecab647089305",
    "raw_bytes": 318551,
    "raw_sha256": "8e9722de44643fe8d12ce18ce1637341b2df31e4318fadbf76280865d97a8f53"}
canonical, sha, identity = first.canonical, first.sha, first.identity
add_sparse = first.add_sparse


def dependencies():
    source = first.dependencies()
    if source["driver"]["sha256"] != SOURCE_DRIVER_SHA:
        raise ValueError("do not mutate the successful raw static tail consumer")
    helper = identity(constrained.__file__)
    if helper["sha256"] != CONSTRAINT_HELPER_SHA:
        raise ValueError("explicitly rebind the frozen R114 geometry interface")
    result = dict(source)
    result["static_tail_projection"] = result.pop("driver")
    result["geometry_constraint_interface"] = helper
    result["driver"] = identity(__file__)
    return result


class Packet:
    """A full polynomial P, its already proved response coefficients A, and R."""
    def __init__(self, polynomial=None, coefficients=None, remainder=None):
        self.polynomial = dict(polynomial or {})
        self.coefficients = dict(coefficients or {})
        self.remainder = dict(remainder or {})

    def add(self, other, amount, ring):
        add_sparse(self.polynomial, other.polynomial, amount, ring)
        add_sparse(self.coefficients, other.coefficients, amount, ring)
        add_sparse(self.remainder, other.remainder, amount, ring)
        return self

    def copy(self):
        return Packet(self.polynomial, self.coefficients, self.remainder)

    def empty(self):
        return not (self.polynomial or self.coefficients or self.remainder)

    def verify(self, columns, ring):
        difference = dict(self.polynomial)
        add_sparse(difference, self.remainder, F(-1), ring)
        for index, value in self.coefficients.items():
            if index not in columns:
                raise ValueError("packet uses a non-basis original response column")
            add_sparse(difference, columns[index], -value, ring)
        if difference:
            raise AssertionError("complete new polynomial identity P=sum A_j P_j+R failed")

    def rows(self):
        return {
            "complete_polynomial": first.polynomial_rows(self.polynomial),
            "original_response_coefficients": [[j, str(v)] for j, v in sorted(self.coefficients.items())],
            "complete_remainder": first.polynomial_rows(self.remainder),
            "complete_polynomial_difference_zero": True}


def one_output(receipt, name):
    rows = [row for row in receipt.get("outputs", []) if row.get("path") == name]
    if len(rows) != 1:
        raise ValueError("exactly one bound publication output is required")
    return rows[0]


def bind_static_source(args, report):
    main = first.read_bound_json(args.source_report, SOURCE_MAIN)
    receipt = first.read_bound_json(args.source_publication_receipt, SOURCE_RECEIPT)
    if (main.get("schema") != first.SCHEMA or main.get("completion") != "complete"
            or str(main.get("github_run_id")) != SOURCE_RUN or main.get("github_sha") != SOURCE_COMMIT
            or main.get("source_hashes") != first.dependencies()
            or main.get("new_static_pure_local_roots_evaluated") != 197
            or main.get("new_homogeneous_target_components") != 254
            or main.get("all_new_complete_polynomial_decomposition_differences_zero") is not True):
        raise ValueError("bind the successful complete original static pure projection")
    if (receipt.get("schema") != "visible-new-mechanism-actions-v1"
            or receipt.get("repository") != REPOSITORY
            or str(receipt.get("run_id")) != SOURCE_RUN
            or receipt.get("source_commit") != SOURCE_COMMIT
            or receipt.get("lane") != "static_m8_tail_quotient"):
        raise ValueError("static publication source/run/lane mismatch")
    driver = main["source_hashes"]["driver"]
    path = "topics/visible-flex-new-mechanism/scripts/"+driver["filename"]
    if receipt.get("source_files", {}).get(path) != {
            "bytes": driver["bytes"], "sha256": driver["sha256"]}:
        raise ValueError("static publication does not bind its actual driver")
    for name, expected in (
            ("static-m8-tail-quotient.json", {
                "bytes": SOURCE_MAIN["bytes"], "sha256": SOURCE_MAIN["sha256"],
                "raw_bytes": SOURCE_MAIN["bytes"], "raw_sha256": SOURCE_MAIN["sha256"]}),
            (SOURCE_EXPORT["filename"], {
                "bytes": SOURCE_EXPORT["stored_bytes"], "sha256": SOURCE_EXPORT["stored_sha256"],
                "raw_bytes": SOURCE_EXPORT["raw_bytes"], "raw_sha256": SOURCE_EXPORT["raw_sha256"]})):
        found = one_output(receipt, name)
        if any(found.get(k) != v for k, v in expected.items()):
            raise ValueError("static publication output bytes disagree")
    first.require_export_metadata(main.get("complete_certificate"), SOURCE_EXPORT)
    data = first.read_bound_gzip(args.source_certificate, SOURCE_EXPORT)
    if (data.get("schema") != first.SCHEMA+"-certificate"
            or data.get("source_hashes") != main["source_hashes"]
            or str(data.get("github_run_id")) != SOURCE_RUN or data.get("github_sha") != SOURCE_COMMIT
            or data.get("local_input") != main["local_input"]
            or data.get("response_input") != main["response_input"]
            or data.get("all_new_complete_polynomial_decompositions_verified") is not True
            or data.get("geometry_names") != list(old.local.NAMES)):
        raise ValueError("complete static certificate scope or provenance mismatch")
    report["input_static_projection"] = {
        "source_run": SOURCE_RUN, "source_commit": SOURCE_COMMIT,
        "main": SOURCE_MAIN, "publication_receipt": SOURCE_RECEIPT,
        "complete_certificate": SOURCE_EXPORT,
        "original_expression_evaluations_repeated": 0,
        "old_raw_static_graded_rank_recomputed": False}
    return data


def load_response_columns(args, report):
    main = first.read_bound_json(args.response_report, first.RESPONSE_MAIN)
    receipt = first.read_bound_json(args.response_publication_receipt, first.RESPONSE_RECEIPT)
    if (main.get("schema") != projection.SCHEMA or main.get("completion") != "complete"
            or str(main.get("github_run_id")) != first.RESPONSE_RUN
            or main.get("github_sha") != first.RESPONSE_COMMIT
            or main.get("source_hashes") != projection.dependencies()):
        raise ValueError("bind the complete successful old response source")
    publication = first.verify_response_receipt(receipt, main)
    first.require_export_metadata(main.get("complete_certificate"), first.RESPONSE_EXPORT)
    data = first.read_bound_gzip(args.response_certificate, first.RESPONSE_EXPORT)
    if (data.get("schema") != projection.SCHEMA+"-certificate"
            or data.get("source_hashes") != main["source_hashes"]
            or data.get("exact_full_projection_rank") != 31):
        raise ValueError("complete old response polynomial certificate mismatch")
    records = data["columns"]
    if len(records) != 288 or [item["index"] for item in records] != list(range(288)):
        raise ValueError("old response original column coverage changed")
    selected, pivots, weights, ranks = set(), set(), {}, {}
    for label, block in data["exact_weight_blocks"].items():
        weight = int(label)
        indices = block["independent_original_columns"]
        if indices != main["exact_weight_blocks"][label]["independent_original_columns"]:
            raise ValueError("old response basis list differs from compact main")
        selected.update(indices)
        ranks[weight] = len(indices)
        for entry in block["pivot_records"]:
            pivots.add(tuple(entry["pivot"]))
        for index in indices:
            weights[index] = weight
    columns = {}
    for index in sorted(selected):
        row = records[index]
        if (row["response_weight"] != weights[index]
                or sha(canonical(row["complete_polynomial"])) != row["complete_polynomial_sha256"]):
            raise ValueError("old original basis polynomial metadata changed")
        columns[index] = first.polynomial_from_rows(row["complete_polynomial"])
    if len(columns) != 31 or len(pivots) != 31:
        raise ValueError("31 published independent columns and pivots are required")
    report["input_response"] = {
        "publication": publication, "main": first.RESPONSE_MAIN,
        "complete_certificate": first.RESPONSE_EXPORT,
        "basis_polynomials_read": 31, "response_formula_evaluations": 0,
        "basis_refactorizations": 0, "old_dependency_checks_repeated": 0}
    return columns, weights, pivots, ranks


def restore_packets(data, ring, columns, weights, pivots):
    rows = data["targets"]
    if len(rows) != 197 or [row["target_index"] for row in rows] != list(range(197)):
        raise ValueError("all 197 original pure static roots are required")
    by_index, names, target = {}, {}, {}
    for row in rows:
        key = tuple(row["geometry_key"])
        if (len(key) != 8 or old.jet_weight(key) or key in target
                or sha(canonical(row["complete_polynomial"])) != row["complete_polynomial_sha256"]):
            raise ValueError("original complete static polynomial record changed")
        packet = Packet(first.polynomial_from_rows(row["complete_polynomial"]))
        target[key] = packet
        by_index[row["target_index"]] = (key, packet)
        names[row["target_index"]] = row["source_root"]
    components = data["homogeneous_components"]
    if len(components) != 254 or [row["component_index"] for row in components] != list(range(254)):
        raise ValueError("all already certified raw homogeneous decompositions are required")
    covered_polynomials = {i: {} for i in by_index}
    for row in components:
        index = row["target_index"]
        key, packet = by_index[index]
        if tuple(row["geometry_key"]) != key or row["source_root"] != names[index]:
            raise ValueError("old homogeneous target identity mismatch")
        polynomial = first.polynomial_from_rows(row["complete_polynomial"])
        remainder = first.polynomial_from_rows(row["complete_remainder"])
        if (any(sum(m)-32 != row["weight"] for m in polynomial)
                or any(sum(m)-32 != row["weight"] or m in pivots for m in remainder)):
            raise ValueError("published canonical remainder is in the wrong weight or pivot")
        coefficients = {}
        for j, raw in row["original_response_column_coefficients"]:
            if j in coefficients or j not in columns or weights[j] != row["weight"]:
                raise ValueError("published coefficient references a wrong old basis column")
            coefficients[j] = F(raw)
        add_sparse(packet.coefficients, coefficients, F(1), ring)
        add_sparse(packet.remainder, remainder, F(1), ring)
        add_sparse(covered_polynomials[index], polynomial, F(1), ring)
    for index, (_, packet) in by_index.items():
        if covered_polynomials[index] != packet.polynomial:
            raise ValueError("published homogeneous components do not cover their complete root")
    return target


def evaluate_packets(target, state, ring):
    answer = Packet()
    for key, packet in target.items():
        amount = constrained.geometry_value(key, state)
        if amount:
            answer.add(packet, amount, ring)
    return answer


def geometry_coordinates(ring):
    static, info = constrained.reference_coordinates()
    inverse = [[F(value) for value in row] for row in info["inverse"]]
    matrix = old.pointwise_matrix()
    derivative = []
    for i in range(8):
        terms = {}
        for j in range(8):
            for key, value in matrix[j].terms.items():
                if old.jet_weight(key) == 2:
                    add_sparse(terms, {key: value}, inverse[i][j], ring)
                elif old.jet_weight(key) != 0:
                    raise ValueError("the published matrix must have geometry derivative weights 0 and 2")
        derivative.append(terms)
    reference = [[F(value) for value in row] for row in info["matrix_columns_are_reference_states"]]
    for weight, coordinates in ((0, static), (2, derivative)):
        for j in range(8):
            reconstructed = {}
            for i in range(8):
                add_sparse(reconstructed, coordinates[i], reference[j][i], ring)
            expected = {key: value for key, value in matrix[j].terms.items()
                        if old.jet_weight(key) == weight}
            if reconstructed != expected:
                raise AssertionError("all eight complete matrix-coordinate identities must hold")
    info.update({
        "coordinate_static_geometry_terms": [
            [[list(key), str(value)] for key, value in sorted(terms.items())] for terms in static],
        "coordinate_derivative_two_geometry_terms": [
            [[list(key), str(value)] for key, value in sorted(terms.items())] for terms in derivative],
        "full_matrix_has_only_derivative_weights_zero_and_two": True,
        "both_weight_parts_exactly_reconstructed": True,
        "integral_static_matrix_part_assumed_zero": False})
    return static, derivative, info


def normalize_packets(target, reference_values, coordinates, ring, keep_original):
    out = {key: packet.copy() for key, packet in target.items()} if keep_original else {}
    for coefficients, value in zip(coordinates, reference_values):
        for key, amount in coefficients.items():
            out.setdefault(key, Packet()).add(value, -amount, ring)
    return {key: packet for key, packet in out.items() if not packet.empty()}


def packet_components(packet, weights):
    polynomials = first.split_weights(packet.polynomial)
    remainders = first.split_weights(packet.remainder)
    coefficients = {}
    for index, value in packet.coefficients.items():
        coefficients.setdefault(weights[index], {})[index] = value
    return {weight: Packet(polynomials.get(weight), coefficients.get(weight), remainders.get(weight))
            for weight in sorted(set(polynomials) | set(coefficients) | set(remainders))}


def summarize_group(name, target, columns, weights, pivots, ring, derivative_weight):
    raw_span = projection.ExactProjectedSpan(ring)
    even_raw_span = projection.ExactProjectedSpan(ring)
    graded = {}
    records, component_records = [], []
    for index, (key, packet) in enumerate(sorted(target.items())):
        if old.jet_weight(key) != derivative_weight:
            raise AssertionError("the new geometry coefficient is in the wrong derivative part")
        packet.verify(columns, ring)
        if any(m in pivots for m in packet.remainder):
            raise AssertionError("linear constraint normalization changed the canonical complement")
        raw_span.add(index, packet.remainder)
        even_raw_span.add(index, projection.four_block_projection(packet.remainder))
        records.append({"geometry_coefficient_index": index, "geometry_key": list(key), **packet.rows()})
        for weight, component in packet_components(packet, weights).items():
            component.verify(columns, ring)
            component_index = len(component_records)
            graded.setdefault(weight, projection.ExactProjectedSpan(ring)).add(
                component_index, component.remainder)
            component_records.append({
                "component_index": component_index, "geometry_coefficient_index": index,
                "geometry_key": list(key), "true_profile_weight": weight, **component.rows()})
        ring.guard()
    per_weight = {
        str(weight): {
            "quotient_rank": len(span.independent),
            "independent_component_indices": span.independent,
            "nonzero_remainder_components": sum(
                bool(row["complete_remainder"]) for row in component_records
                if row["true_profile_weight"] == weight)}
        for weight, span in sorted(graded.items())}
    summary = {
        "name": name, "geometry_derivative_weight": derivative_weight,
        "geometry_coefficient_packets": len(records),
        "nonzero_full_polynomials": sum(bool(row["complete_polynomial"]) for row in records),
        "nonzero_full_remainders": sum(bool(row["complete_remainder"]) for row in records),
        "raw_ungraded_coefficient_quotient_rank": len(raw_span.independent),
        "graded_coefficient_quotient_rank": sum(len(span.independent) for span in graded.values()),
        "even_raw_ungraded_quotient_rank": len(even_raw_span.independent),
        "even_graded_quotient_rank": sum(
            len(span.independent) for weight, span in graded.items() if weight % 2 == 0),
        "independent_raw_geometry_keys": [records[j]["geometry_key"] for j in raw_span.independent],
        "per_true_profile_weight": per_weight,
        "all_new_complete_polynomial_identities_verified": True}
    complete = {
        "summary": summary, "geometry_coefficients": records,
        "homogeneous_components": component_records,
        "raw_ungraded_quotient_basis": raw_span.summary(),
        "even_raw_ungraded_quotient_basis": even_raw_span.summary(),
        "graded_quotient_bases": {str(w): span.summary() for w, span in sorted(graded.items())}}
    return summary, complete


def actual(args, report):
    if (os.environ.get("GITHUB_ACTIONS", "").lower() != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise RuntimeError("the actual constrained target runs only in this public repository Actions")
    started = time.monotonic()
    ring = projection.TailRing(args.max_seconds, args.memory_mib, args.max_operations)
    static_data = bind_static_source(args, report)
    columns, weights, pivots, ranks = load_response_columns(args, report)
    target = restore_packets(static_data, ring, columns, weights, pivots)
    coordinates0, coordinates2, coordinate_info = geometry_coordinates(ring)
    reference_values = [evaluate_packets(target, state, ring) for state in constrained.BASIS_STATES]
    normalized = normalize_packets(target, reference_values, coordinates0, ring, True)
    induced2 = normalize_packets({}, reference_values, coordinates2, ring, False)
    for state in constrained.BASIS_STATES:
        check = evaluate_packets(normalized, state, ring)
        if not check.empty():
            raise AssertionError("the complete normalized static packet must vanish at all eight reference states")
    # Recover the old target from the NEW normalized object and its removed matrix part.
    recovered = {key: value.copy() for key, value in normalized.items()}
    for coefficients, value in zip(coordinates0, reference_values):
        for key, amount in coefficients.items():
            recovered.setdefault(key, Packet()).add(value, amount, ring)
    for key in set(recovered) | set(target):
        check = recovered.get(key, Packet()).copy().add(target.get(key, Packet()), F(-1), ring)
        if not check.empty():
            raise AssertionError("new full static normalization reconstruction failed")
    raw = projection.ExactProjectedSpan(ring)
    raw_even = projection.ExactProjectedSpan(ring)
    for i, (key, packet) in enumerate(sorted(target.items())):
        raw.add(i, packet.remainder)
        raw_even.add(i, projection.four_block_projection(packet.remainder))
    summaries, completed = {}, {}
    for name, value, derivative_weight in (
            ("normalized_static", normalized, 0),
            ("induced_derivative_two_correction", induced2, 2)):
        summary, complete = summarize_group(name, value, columns, weights, pivots, ring, derivative_weight)
        summaries[name], completed[name] = summary, complete
    certificate = {
        "schema": SCHEMA+"-certificate", "source_hashes": report["source_hashes"],
        "github_run_id": report["github_run_id"], "github_sha": report["github_sha"],
        "input_static_projection": report["input_static_projection"],
        "input_response": report["input_response"],
        "geometry_names": list(old.local.NAMES), "matrix_coordinates": coordinate_info,
        "reference_static_profile_packets": [
            {"basis_state": [str(x) for x in state], **value.rows()}
            for state, value in zip(constrained.BASIS_STATES, reference_values)],
        "groups": completed,
        "raw_ungraded_static_quotient": raw.summary(),
        "raw_even_ungraded_static_quotient": raw_even.summary(),
        "constraint_formula": "L - sum_i a_i(m^[0]+m^[2]) L^[0](S_i*)",
        "known_parts": "L^[0]-sum a_i(m^[0])F_i and -sum a_i(m^[2])F_i",
        "unknown_parts_retained": "the original L^[2] and L^[4]",
        "actual_zero_matrix_path_evaluated": False,
        "complete_period_or_complete_quotient_claimed": False}
    exported = first.write_gzip(args.out.with_name(args.out.stem+"-certificate.json.gz"), certificate)
    report.update(
        completion="complete", complete_certificate=exported, groups=summaries,
        raw_ungraded_static_quotient_rank=len(raw.independent),
        raw_even_ungraded_static_quotient_rank=len(raw_even.independent),
        matrix_coordinates={
            "basis_states": coordinate_info["basis_states_h_k_omega"],
            "both_weight_parts_exactly_reconstructed": True,
            "eight_normalized_reference_packets_exactly_zero": True,
            "integral_static_matrix_part_assumed_zero": False},
        full_matrix_constraint_and_induced_weight_two_accounted_for=True,
        original_derivative_two_density_evaluated=False,
        original_derivative_four_density_evaluated=False,
        actual_M0_geometry_evaluated=False,
        actual_period_or_cost_cone_obstruction_claimed=False,
        complete_operator_quotient_dimension_claimed=False,
        old_profile_substitutions_recomputed=False, old_response_formulas_recomputed=False,
        polynomial_operations=ring.operations, linear_operations=ring.linear_operations,
        elapsed_seconds=time.monotonic()-started,
        peak_rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024,
        task_complete=False)
    return report


def toy_only():
    ring = projection.TailRing(40, 256, 100000)
    columns = {3: {(1, 0): F(1), (0, 1): F(1)}}
    weights = {3: -31}
    p = Packet({(1, 0): F(2), (0, 1): F(2), (0, 2): F(5)}, {3: F(2)}, {(0, 2): F(5)})
    p.verify(columns, ring)
    q = Packet().add(p, F(-3), ring)
    q.verify(columns, ring)
    expected = q.polynomial == {(1, 0): F(-6), (0, 1): F(-6), (0, 2): F(-15)}
    pieces = packet_components(p, weights)
    combined = Packet()
    for piece in pieces.values():
        piece.verify(columns, ring)
        combined.add(piece, F(1), ring)
    split_ok = (combined.polynomial == p.polynomial and combined.coefficients == p.coefficients
                and combined.remainder == p.remainder)
    zero, x = (0,)*8, (0,1,0,0,0,0,0,0)
    # Two hand-built interpolation points k=0,1; no research matrix or m8 input.
    target = {zero: p.copy(), x: q.copy()}
    values = [p.copy(), p.copy().add(q, F(1), ring)]
    coords = [{zero: F(1), x: F(-1)}, {x: F(1)}]
    normalized = normalize_packets(target, values, coords, ring, True)
    interpolation_zero = not normalized
    jet = (0,0,0,2,0,0,0,0)
    correction = normalize_packets({}, values, [{jet:F(2)}, {}], ring, False)
    induced_sign = correction[jet].remainder == {(0,2):F(-10)}
    bad_rejected = False
    try:
        Packet({(1,0):F(1)}, {3:F(1)}, {}).verify(columns, ring)
    except AssertionError:
        bad_rejected = True
    checks = {
        "packet_linear_combinations_keep_full_identity": expected,
        "whole_packet_true_weight_split_reconstructs_all_fields": split_ok,
        "artificial_two_state_normalization_is_exact": interpolation_zero,
        "induced_derivative_correction_has_the_required_minus_sign": induced_sign,
        "incorrect_complete_decomposition_is_rejected": bad_rejected,
        "no_old_research_inputs_or_actual_m8_profile_evaluated": True}
    if not all(checks.values()):
        raise AssertionError("new constrained-consumer artificial check failed")
    return {"completion":"complete", "mode":"small_artificial_development_only",
            "checks":checks, "all_passed":True, "task_complete":False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--toy-only", action="store_true")
    parser.add_argument("--source-report", type=Path, default=SOURCE_DIRECTORY/"static-m8-tail-quotient.json")
    parser.add_argument("--source-publication-receipt", type=Path, default=SOURCE_DIRECTORY/"receipt.json")
    parser.add_argument("--source-certificate", type=Path, default=SOURCE_DIRECTORY/SOURCE_EXPORT["filename"])
    parser.add_argument("--response-report", type=Path, default=first.RESPONSE_DIRECTORY/"full-m8-tail-response.json")
    parser.add_argument("--response-publication-receipt", type=Path, default=first.RESPONSE_DIRECTORY/"receipt.json")
    parser.add_argument("--response-certificate", type=Path, default=first.RESPONSE_DIRECTORY/first.RESPONSE_EXPORT["filename"])
    parser.add_argument("--max-seconds", type=float, default=240)
    parser.add_argument("--memory-mib", type=int, default=1024)
    parser.add_argument("--max-operations", type=int, default=10000000)
    args = parser.parse_args()
    started = time.monotonic()
    report = {"schema":SCHEMA, "completion":"started",
              "github_run_id":os.environ.get("GITHUB_RUN_ID"),
              "github_sha":os.environ.get("GITHUB_SHA"), "task_complete":False}
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
    if len(raw)>first.MAX_REPORT_BYTES:
        full=first.write_gzip(args.out.with_name(args.out.stem+"-full-report.json.gz"), report)
        report={key:report[key] for key in ("schema","completion","github_run_id","github_sha",
            "source_hashes","wall_seconds","complete_certificate","input_static_projection",
            "input_response","raw_ungraded_static_quotient_rank","raw_even_ungraded_static_quotient_rank",
            "error_type","error","task_complete") if key in report}
        report.update(compact_fallback=True, complete_report=full)
        raw=canonical(report)+b"\n"
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_bytes(raw)
    print(json.dumps({"filename":args.out.name,"bytes":len(raw),"sha256":sha(raw)},sort_keys=True),flush=True)
    if failed:
        raise SystemExit(1)


if __name__=="__main__":
    main()
