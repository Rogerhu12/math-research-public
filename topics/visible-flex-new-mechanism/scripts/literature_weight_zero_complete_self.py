#!/usr/bin/env python3
"""R316: one complete self gate on the whole true weight-zero pure kernel.

Restore only the sixteen missing mixed input roots and the same C2/Gamma sum.
Consume three STORED pure coordinates to form the complete thirteen-dimensional
response pure kernel. Map its thirteen basis elements plus the known pure-zero
H to the full ordered matrix and faithful local Euler coordinates. No old
pure/profile evaluation, H0 rank, endpoint layer, or 3974 forcing is rerun.
Only public Actions may execute this new development or actual entry point.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import json
import os
from pathlib import Path
import resource
import time

import literature_character_zero_endpoint_layer as prior
import literature_full_self_euler_coordinates as selfmap

pure, zero, head, literal = prior.pure, prior.zero, prior.head, prior.literal
colored, exact, formal = prior.colored, prior.exact, prior.formal
canonical, sha = prior.canonical, prior.sha
REPOSITORY, TOPIC = prior.REPOSITORY, prior.TOPIC
SCHEMA = "visible-flex-weight-zero-complete-self-gate-v1"
FROZEN_READER = {
    "filename": "literature_character_zero_endpoint_layer.py", "bytes": 29604,
    "sha256": "bb7be8fc3fa6b98f3f69aca96e5145c6df1f3d581ea85d14aa7fb6ccfefe6a94",
}
SELF_HELPER = {
    "filename": "literature_full_self_euler_coordinates.py", "bytes": 10966,
    "sha256": "95ec818ce1fdf815b0390aaf2ad4f976a0dfc7bd0b5218899acd4f4bc271f9ba",
}
PURE_BASIS_OLD = (0, 2, 3)
H_SHA = "3be041da7463195066061c4fea47881cedb8c65e69fc65b063748dc7264de325"


def source_identity():
    value = prior.source_identity()
    if value["driver"] != FROZEN_READER:
        raise ValueError("the frozen R234 input reader changed")
    value["frozen_R234_input_reader"] = value.pop("driver")
    found = literal.identity(selfmap.__file__)
    if found != SELF_HELPER:
        raise ValueError("the new full-self helper changed")
    value["new_full_self_helper"] = found
    value["driver"] = literal.identity(__file__)
    return value


def kernel_coordinates(values, pivots, budget):
    """Recover coordinates in an ALREADY PROVED three-column pure basis.

    This is a three-by-three change of coordinates, not a repeated old rank.
    Every returned kernel vector has its own unique nonpivot coefficient one.
    """
    if len(pivots) != 3 or len(set(pivots)) != 3:
        raise ValueError("three distinct published pure basis columns are required")
    if any(len(row) != 3 for row in values) or any(not 0 <= j < len(values) for j in pivots):
        raise ValueError("three stored pure coordinates per old column are required")
    matrix = [[F(values[pivots[j]][i]) for j in range(3)] for i in range(3)]
    inverse_columns = [
        pure.exact_square_solve(matrix, [F(i == k) for i in range(3)], budget)
        for k in range(3)
    ]
    result = []
    for index, row in enumerate(values):
        if index in pivots:
            continue
        coefficient = [
            sum((inverse_columns[k][j]*F(row[k]) for k in range(3)), F(0))
            for j in range(3)
        ]
        if any(sum((matrix[i][j]*coefficient[j] for j in range(3)), F(0)) != F(row[i])
               for i in range(3)):
            raise AssertionError("fresh stored pure coordinate reconstruction failed")
        combination = {index: F(1)}
        for pivot, value in zip(pivots, coefficient):
            if value:
                combination[pivot] = -value
        if any(sum((c*F(values[j][k]) for j, c in combination.items()), F(0))
               for k in range(3)):
            raise AssertionError("the constructed response combination is not in the stored pure kernel")
        result.append((index, combination))
    return result


def combination_rows(combination, labels):
    return [[labels[i], str(c)] for i, c in sorted(combination.items()) if c]


def signature_vectors(results):
    labels = sorted(set().union(*(set(item["coordinates"]) for item in results)))
    positions = {key: i for i, key in enumerate(labels)}
    return [{positions[key]: value for key, value in item["coordinates"].items()}
            for item in results], labels


def public_column(index, label, result):
    return {
        "index": index, "label": label,
        "original_mixed_sha256": result["original_mixed_sha256"],
        "original_mixed_terms": result["original_mixed_terms"],
        "global_diagonal_sha256": result["global_diagonal_sha256"],
        "global_diagonal_terms": result["global_diagonal_terms"],
        "whole_word_sha256": result["whole_word_sha256"],
        "whole_word_terms": result["whole_word_terms"],
        "self_word_sha256": result["self_word_sha256"],
        "self_word_terms": result["self_word_terms"],
        "ordered_matrix_T": [[str(v) for v in row] for row in result["matrix"]],
        "complete_local_density": selfmap.local_rows(result["local"]),
        "complete_Euler_coefficients": selfmap.local_rows(result["euler"]),
        "local_density_sha256": result["local_density_sha256"],
        "Euler_sha256": result["Euler_sha256"],
        "faithful_coordinate_sha256": result["coordinate_sha256"],
        "bilocal_exactly_nine_true_kernels": True,
        "whole_word_reconstruction_from_T_and_L_exact_zero": result["complete_reconstruction_zero"],
        "full_self_function_zero": result["full_self_function_zero"],
        "true_cost_weight": 0, "observed_self_weight": -2,
        "original_same_right_anchor_and_nested_increments_retained": True,
    }


def actual(args, report):
    budget = literal.Budget(args.max_seconds, args.memory_mib, args.integer_bits)
    limits = exact.Limits(
        seconds=args.max_seconds, nodes=350000, atoms=100000,
        terms=args.max_terms, rewrites=args.max_IBP_calls,
        memory_mib=args.memory_mib, rational_bits=args.integer_bits,
    )
    ring = colored.ColoredRing(limits)
    report["phase"] = "bind_existing_originals_and_stored_pure_coordinates"
    pure.bind_head_receipt(args.head_directory, report)
    prior.bind_pure_identity(args.pure_identity_directory, report)
    labels = zero.read_R0_definition(args.R0_directory, report)
    pure_values = prior.bind_stored_pure_rows(args.stored_pure_directory, labels, report)
    _, data = head.bind_input("static", args.static_directory, report)
    C2, W = prior.restore_C2_and_W(ring, data, labels, report)
    del data
    original_controls = prior.restore_old_mixed(ring, W, labels, budget, report)
    del W
    old_to_new = {old: i for i, old in enumerate(zero.R0_KEEP)}
    pivots = tuple(old_to_new[i] for i in PURE_BASIS_OLD)
    specifications = kernel_coordinates(pure_values, pivots, budget)
    if len(original_controls) != 16 or len(specifications) != 13:
        raise ValueError("the bound complete weight-zero response block changed")
    kernels, kernel_records = [], []
    for index, combination in specifications:
        value = sum((c*original_controls[j] for j, c in sorted(combination.items())), ring.number(0))
        kernels.append(value)
        kernel_records.append({
            "nonpivot_old_column": zero.R0_KEEP[index],
            "original_R126_combination": combination_rows(combination, zero.R0_KEEP),
            "exact_three_stored_pure_sums": ["0", "0", "0"],
            "original_mixed_sha256": ring.digest(value), "original_mixed_terms": len(value.terms),
        })
    H = C2 + sum((c*original_controls[old_to_new[j]]
                  for j, c in sorted(prior.H_COMBINATION.items())), ring.number(0))
    if ring.digest(H) != H_SHA:
        raise ValueError("the same full R201/R234 H original mixed root changed")
    column_labels = [{"kind": "complete_weight_zero_response_pure_kernel",
                      "nonpivot_R126_old_column": row["nonpivot_old_column"]}
                     for row in kernel_records]
    column_labels.append({"kind": "R201_H", "pure_zero": True, "lambda_plus": "1"})
    report["complete_response_pure_kernel"] = {
        "old_full_response_dimension_from_R126_R196": 16,
        "old_pure_dimension_from_R201": 3, "published_pure_basis_old_columns": list(PURE_BASIS_OLD),
        "pure_query_rows_read_not_evaluated": [list(row) for row in prior.PURE_ROWS],
        "kernel_dimension": 13, "new_kernel_coordinate_columns": kernel_records,
        "independence": "each has coefficient one on its distinct nonpivot of the proved full R0 basis",
        "all_pure_kernel_branches_in_this_weight_included": True,
        "old_rank_or_pure_normalization_repeated": False,
    }
    report["H_original"] = {"definition": "C2+Rold0/48+11 Rold2/64-13 Rold3/96",
                            "mixed_sha256": ring.digest(H), "terms": len(H.terms),
                            "pure_zero_from_R201": True, "lambda_plus": "1"}
    columns = kernels + [H]
    mapper = selfmap.SelfMapper(ring, args.max_IBP_calls, args.max_terms, args.max_cache_entries)
    results = []
    report["phase"] = "fourteen_new_complete_self_coordinates"
    report["columns"] = []
    for index, (value, label) in enumerate(zip(columns, column_labels)):
        result = mapper.expression(value, true_cost_weight=0)
        results.append(result)
        report["columns"].append(public_column(index, label, result))
        report["progress"] = {"new_complete_self_columns": index+1, "required": 14}
        budget.check()
    vectors, coordinate_labels = signature_vectors(results)
    decision_raw = pure.decide_projection(vectors, budget)
    decision = {
        "comparison_space": "Q(R^(true weight 0) intersect ker universal pure), all 13 response directions",
        "target": "Q(H), with H from R201",
        "comparison_self_rank": decision_raw["comparison_rank"],
        "augmented_self_rank": decision_raw["augmented_rank"],
        "coordinate_rows": len(coordinate_labels),
        "faithfulness": "R314 actual ordered matrix plus complete local Euler polynomial",
        "other_true_weights_compared": False,
        "whole_U0_self_image_computed": False,
        "lambda_plus_factorization_on_all_U_claimed": False,
        "actual_signed_cost_control_claimed": False,
    }
    calls = mapper.words.run_primitive_calls
    fresh_record = None
    if "coefficients" in decision_raw:
        coefficients = decision_raw["coefficients"]
        old_combination = {}
        for i, value in coefficients.items():
            for old_position, amount in specifications[i][1].items():
                selfmap.add(old_combination, old_position, value*amount)
        if any(sum((c*pure_values[j][k] for j, c in old_combination.items()), F(0))
               for k in range(3)):
            raise AssertionError("fresh combined original response pure queries do not vanish")
        difference = H - sum((c*original_controls[j] for j, c in sorted(old_combination.items())),
                             ring.number(0))
        remaining = args.max_IBP_calls-calls
        if remaining <= 0:
            raise literal.Limit("total new primitive budget before fresh original full-self difference")
        report["phase"] = "fresh_original_composite_self_verification"
        fresh_mapper = selfmap.SelfMapper(ring, remaining, args.max_terms, args.max_cache_entries)
        fresh = fresh_mapper.expression(difference, true_cost_weight=0)
        calls += fresh_mapper.words.run_primitive_calls
        if fresh["coordinates"] or not fresh["complete_reconstruction_zero"]:
            raise AssertionError("fresh original composite T/Euler verification failed")
        fresh_record = {
            "original_mixed_difference_sha256": ring.digest(difference),
            "original_mixed_difference_terms": len(difference.terms),
            "fresh_global_diagonal_sha256": fresh["global_diagonal_sha256"],
            "fresh_whole_word_sha256": fresh["whole_word_sha256"],
            "fresh_self_word_sha256": fresh["self_word_sha256"],
            "fresh_self_word_terms": len(fresh["self_words"]),
            "fresh_self_word_is_literal_zero": not fresh["self_words"],
            "fresh_whole_word_reconstruction_exact_zero": fresh["complete_reconstruction_zero"],
            "fresh_T_and_complete_Euler_exact_zero": True,
            "full_self_zero_by_R314_faithful_Euler_not_required_NF_zero": True,
            "independent_new_word_mapper": True,
            "fresh_mapper_statistics": dict(fresh_mapper.words.stats),
        }
        representative = dict(prior.H_COMBINATION)
        for position, coefficient in old_combination.items():
            selfmap.add(representative, zero.R0_KEEP[position], -coefficient)
        decision.update(
            outcome="MEMBER",
            coefficients_in_thirteen_pure_kernel_columns=combination_rows(
                coefficients, [row["nonpivot_old_column"] for row in kernel_records]),
            response_in_original_sixteen_columns=combination_rows(old_combination, zero.R0_KEEP),
            new_representative={"definition": "C2 plus the following complete original responses",
                                "original_response_coefficients":
                                    [[j, str(c)] for j, c in sorted(representative.items())],
                                "universal_pure_zero": True, "whole_universal_self_zero": True,
                                "lambda_plus": "1"},
            fresh_original_verification=fresh_record,
            exact_three_stored_pure_sums=["0", "0", "0"],
        )
    else:
        dual = decision_raw["dual"]
        decision.update(
            outcome="NONMEMBER_WITHIN_COMPLETE_WEIGHT_ZERO_RESPONSE_PURE_KERNEL",
            exact_dual=[[selfmap.coordinate_label(coordinate_labels[i]), str(c)]
                        for i, c in sorted(dual.items())],
            exact_dual_values_on_all_fourteen_columns=
                [str(v) for v in decision_raw["dual_values_all_columns"]],
            exact_dual_support_bound=decision_raw["dual_support_bound"],
            full_Q_nonzero_class_proved_not_merely_nonzero_normal_form=True,
        )
    report["decision"] = decision
    report["shared_mapper_statistics"] = dict(mapper.words.stats)
    proof = {
        "schema": SCHEMA+"-in-memory-proof", "source_hashes": report["source_hashes"],
        "inputs": report["inputs"], "complete_response_pure_kernel": report["complete_response_pure_kernel"],
        "old_pure_coordinate_values": [[str(x) for x in row] for row in pure_values],
        "column_order": column_labels,
        "complete_new_self_words": [selfmap.word_rows(item["self_words"]) for item in results],
        "complete_local_densities": [selfmap.local_rows(item["local"]) for item in results],
        "complete_Euler_polynomials": [selfmap.local_rows(item["euler"]) for item in results],
        "all_faithful_coordinates": [selfmap.coordinate_rows(item["coordinates"]) for item in results],
        "columns": report["columns"], "decision": decision,
    }
    raw = canonical(proof)
    if len(raw) > args.max_certificate_bytes:
        raise literal.Limit("complete new in-memory proof exceeds its declared byte ceiling")
    report["reproducible_certificate"] = {"bytes": len(raw), "sha256": sha(raw), "persisted": False}
    report.update(
        completion="complete", phase="complete_weight_zero_full_self_gate",
        complete_self_gate=True, new_complete_self_targets=14,
        old_mixed_inputs_restored=16, old_static_C2_input_restored=1,
        old_pure_queries_reevaluated=0, old_full_H0_rank_recomputed=False,
        old_endpoint_targets_recomputed=0, old_forcing_recompiled=False,
        new_profile_evaluations=0, new_N_responses=0, new_response_generators=0,
        total_new_primitive_calls=calls,
        literal_monitor_operations=budget.operations,
        literal_monitor_maximum_integer_bits=budget.maximum_bits,
        literal_monitor_is_not_total_DAG_arithmetic=True,
        fixed_profile_circle_evaluated=False, full_period_or_joint_ruling_paid=False,
        full_actual_cost_semigroup_solved=False,
    )


def toy_only(args):
    """Twelve NEW interface fixtures; no published mathematical input is read."""
    limits = exact.Limits(seconds=args.max_seconds, nodes=10000, atoms=4000,
                          terms=args.max_terms, memory_mib=args.memory_mib,
                          rational_bits=args.integer_bits)
    ring = colored.ColoredRing(limits)
    q, qb, x = ring.color("q"), ring.color("qbar"), ring.x()
    v, r, s = q.D(), q.D().D(), q.D().D().D()
    records = []

    def run(name, function):
        try:
            details = function()
            records.append({"name": name, "passed": True, "details": details})
        except Exception as error:
            records.append({"name": name, "passed": False,
                            "error": {"type": type(error).__name__, "message": str(error)}})

    def mapper():
        return selfmap.SelfMapper(ring, args.max_IBP_calls, args.max_terms, args.max_cache_entries)

    def zero_euler():
        base = {(1, (0, 0, 0, 1)): F(1)}
        value = selfmap.euler(selfmap.derivative(base, limits), limits)
        assert not value
        return "the complete Euler operator kills the displayed quartic total derivative"

    def nonzero_euler():
        value = selfmap.euler({(0, (2, 2, 3, 3)): F(1)}, limits)
        assert value[(0, (2, 2, 6))] == -2
        return "the u6 coefficient is exactly -2*(u2)^2, with all other terms retained"

    def nine_matrix():
        matrix = [[F(3*i+j+1) for j in range(3)] for i in range(3)]
        result = selfmap.split_self(selfmap.matrix_words(matrix), limits)
        assert result["matrix"] == matrix and not result["local"] and not result["euler"]
        assert result["matrix"][0][1] != result["matrix"][1][0]
        return "all nine ordered entries survive, without symmetrizing the two slots"

    def j2_normalization():
        matrix = [[F(0) for j in range(3)] for i in range(3)]
        matrix[2][2] = F(1)
        words = selfmap.matrix_words(matrix)
        assert sorted(words.values()) == [F(1), F(2), F(2), F(4)]
        result = selfmap.split_self(words, limits)
        assert result["matrix"] == matrix
        return "the complete j2 is x^2*r^2+2*v^2 on both slots"

    def global_diagonal():
        result = mapper().expression(x*x*(q*q*qb*qb).I())
        assert result["local"] == {(0, (0, 0, 0, 0)): F(1)}
        assert result["euler"] == {(0, (0, 0, 0)): F(4)}
        return "both colors inside the original integral become the same real profile"

    def nested_increment():
        raw = (x*(q**4).I()).I()
        instance = mapper()
        result = instance.expression(raw)
        assert result["local"] == {(0, (0, 0, 0, 0)): F(1, 2)}
        actual_derivative = instance.words.expression(raw.D().D())
        second = selfmap.left_coefficient(actual_derivative, 0, F(-1, 2), maximum_power=0)
        assert second == result["self_words"]
        return "I(x I(u^4)) gives half int(u^4); D^2 is taken before the outer zero restriction"

    def triangle_boundary():
        raw = (q*r*(r*r).I()).I() + (v*v*(r*r).I()).I()
        result = mapper().expression(-x*x*raw)
        assert result["nonlocal_matrix_zero"]
        assert result["local"] == {(0, (0, 1, 2, 2)): F(1)}
        return "the triangle diagonal retains exactly int(u*u1*(u2)^2)"

    def bad_bilocal():
        letter = selfmap.colored_letter(0, (0, 0))
        try:
            selfmap.split_self({(letter, letter): F(1)}, limits)
        except ValueError as error:
            assert "nine true moment kernels" in str(error)
            return "a quadratic bilocal outside the true moment matrix is rejected"
        raise AssertionError("an unproved bilocal remainder was silently discarded")

    def bad_length():
        letter = selfmap.colored_letter(0, (0,))
        try:
            selfmap.split_self({(letter, letter, letter, letter): F(1)}, limits)
        except ValueError as error:
            assert "double-integral class" in str(error)
            return "a longer quartic word is rejected rather than truncated"
        raise AssertionError("an extra word was silently discarded")

    def scaling():
        raw = x*x*(q*q*v*r).I()
        result = mapper().expression(raw, true_cost_weight=0)
        assert result["coordinates"]
        try:
            mapper().expression(raw, true_cost_weight=1)
        except ValueError as error:
            assert "scaling weight" in str(error)
            return "cost weight zero gives self weight -2, and a wrong shift is rejected"
        raise AssertionError("a wrong true-weight tag was accepted")

    def pure_coordinates():
        budget = literal.Budget(args.max_seconds, args.memory_mib, args.integer_bits)
        values = [[1, 0, 0], [2, 3, 4], [0, 1, 0], [0, 0, 1], [-1, 0, 2]]
        result = kernel_coordinates(values, (0, 2, 3), budget)
        assert result == [(1, {1: F(1), 0: F(-2), 2: F(-3), 3: F(-4)}),
                          (4, {4: F(1), 0: F(1), 3: F(-2)})]
        return "only a known three-coordinate basis is inverted; every new kernel vector is checked"

    def fresh_difference():
        first = x*x*(q*q*r*r).I()
        extra = x*x*(q**4).D().I()
        one = mapper().expression(first)
        two = mapper().expression(first+extra)
        assert one["coordinates"] == two["coordinates"]
        fresh = mapper().expression((first+extra)-first)
        assert not fresh["coordinates"] and not fresh["self_words"]
        return "an independently remapped original difference has exact complete self zero"

    for name, function in (
        ("complete_Euler_null_Lagrangian", zero_euler),
        ("complete_Euler_highest_jet_not_dropped", nonzero_euler),
        ("ordered_nine_matrix_reconstruction", nine_matrix),
        ("true_third_moment_includes_two_u1_squared", j2_normalization),
        ("global_color_identification_inside_original_tail", global_diagonal),
        ("raw_nested_right_integral_increment_and_Fourier_sign", nested_increment),
        ("triangle_diagonal_local_boundary_is_retained", triangle_boundary),
        ("unpaid_bilocal_is_not_a_zero_decision", bad_bilocal),
        ("longer_word_is_not_truncated", bad_length),
        ("self_true_weight_shift", scaling),
        ("known_pure_basis_to_complete_kernel_coordinates", pure_coordinates),
        ("fresh_original_composite_self_difference", fresh_difference),
    ):
        run(name, function)
    return {"checks": records, "count": len(records),
            "all_passed": len(records) == 12 and all(row["passed"] for row in records),
            "published_profiles_roots_queries_or_old_suites_executed": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only", action="store_true")
    parser.add_argument("--output", type=Path, help="runner-temporary summary only")
    parser.add_argument("--static-directory", type=Path, default=TOPIC/"notes"/head.INPUTS["static"]["directory"])
    parser.add_argument("--R0-directory", type=Path, default=TOPIC/"notes/actions-43649525432-1-g_first_translation")
    parser.add_argument("--head-directory", type=Path, default=TOPIC/"notes/actions-43681388902-1-character_head_zero")
    parser.add_argument("--pure-identity-directory", type=Path, default=TOPIC/"notes/actions-43683171512-1-character_zero_pure_readout")
    parser.add_argument("--stored-pure-directory", type=Path, default=TOPIC/"notes/actions-43646543691-1-full_m8_tail_response_projection")
    parser.add_argument("--max-seconds", type=float, default=240)
    parser.add_argument("--memory-mib", type=int, default=1024)
    parser.add_argument("--integer-bits", type=int, default=8192)
    parser.add_argument("--max-terms", type=int, default=100000)
    parser.add_argument("--max-IBP-calls", type=int, default=300000)
    parser.add_argument("--max-cache-entries", type=int, default=250000)
    parser.add_argument("--max-summary-bytes", type=int, default=95000)
    parser.add_argument("--max-certificate-bytes", type=int, default=8000000)
    args = parser.parse_args()
    if min(args.max_seconds, args.memory_mib, args.integer_bits, args.max_terms,
           args.max_IBP_calls, args.max_cache_entries, args.max_certificate_bytes) <= 0:
        parser.error("all resource budgets must be positive")
    if not 16000 <= args.max_summary_bytes < 100000:
        parser.error("a summary cap from 16KB to below100KB is required")
    if not (os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY):
        parser.error("all NEW development and research execution is restricted to public repository Actions")
    started = time.monotonic()
    report = {
        "schema": SCHEMA, "completion": "started", "phase": "source_binding",
        "github_repository": os.environ.get("GITHUB_REPOSITORY"),
        "github_run_id": os.environ.get("GITHUB_RUN_ID"), "github_sha": os.environ.get("GITHUB_SHA"),
        "inputs": {}, "scope": "fourteen new complete self targets in true weight zero",
        "recomputable_payload_publication_permitted": False,
    }
    code = 0
    try:
        report["source_hashes"] = source_identity()
        if args.toy_only:
            report["development"] = toy_only(args)
            passed = report["development"]["all_passed"]
            report.update(completion="complete" if passed else "new_development_failed",
                          phase="new_complete_self_interfaces_only")
            code = 0 if passed else 1
        else:
            actual(args, report)
    except (literal.Limit, formal.CompilationBudgetExceeded, MemoryError) as error:
        report.update(completion="resource_limit", error=str(error),
                      complete_self_gate=False, partial_is_not_a_decision=True,
                      resumable_cursor_or_partial_completion_claimed=False)
        code = 2
    except Exception as error:
        report.update(completion="implementation_check_failed",
                      error={"type": type(error).__name__, "message": str(error)},
                      complete_self_gate=False)
        code = 1
    report["elapsed_seconds"] = time.monotonic()-started
    report["peak_rss_mib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    body = canonical(report)+b"\n"
    if len(body) > args.max_summary_bytes:
        report = {
            "schema": SCHEMA, "completion": "summary_output_limit",
            "full_summary_bytes": len(body), "full_summary_sha256": sha(body),
            "github_run_id": report["github_run_id"], "github_sha": report["github_sha"],
            "source_hashes": report.get("source_hashes"), "complete_self_gate": False,
            "no_completed_decision_published_from_a_truncated_summary": True,
        }
        body = canonical(report)+b"\n"
        code = 2
    if len(body) > args.max_summary_bytes:
        raise ValueError("minimal output exceeds the declared cap")
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(body)
    if report.get("completion") == "complete" and "decision" in report:
        print("MATHEMATICAL_RESULT "+canonical(report["decision"]).decode(), flush=True)
        for column in report["columns"]:
            print("SELF_COLUMN "+canonical(column).decode(), flush=True)
    print("COMPLETE_REPORT "+body.decode().rstrip(), flush=True)
    print(canonical({"summary_bytes": len(body), "summary_sha256": sha(body),
                     "payload_publication_permitted": False}).decode(), flush=True)
    raise SystemExit(code)


if __name__ == "__main__":
    main()
