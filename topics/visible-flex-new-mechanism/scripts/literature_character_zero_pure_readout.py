#!/usr/bin/env python3
"""One exact pure readout gate for the published true weight-zero head.

Test C2_pure in span(R0_pure, C4_pure, C6_pure).  Only restore the sixteen
missing old pure response roots, and extract three static roots with the
same eight-reference Gamma.  No mixed calculation, N response, old profile
evaluation, full H0 kernel or power-tail target is performed.

The outcome concerns universal pure operators restricted to U0.  It is not
a fixed-profile readout on all U.  Actual research is Actions-only.  All
recomputable certificates remain in memory; stdout is bounded.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as F
import json
from math import lcm
import os
from pathlib import Path
import resource
import time

import literature_character_head_zero as zero

head, literal, priority = zero.head, zero.literal, zero.priority
layer, old, static = zero.layer, zero.old, zero.static
colored, exact, blocks, formal = zero.colored, zero.exact, zero.blocks, zero.formal
canonical, sha = zero.canonical, zero.sha
REPOSITORY, TOPIC = zero.REPOSITORY, zero.TOPIC
SCHEMA = "visible-flex-character-zero-pure-readout-v1"
ZERO_DRIVER = {
    "filename": "literature_character_head_zero.py", "bytes": 42361,
    "sha256": "337966b4fb9a417ed62d650cac87ffc4c41bedc9938e11c1520fe1136b53dee4",
}
HEAD_ORIGIN = {
    "run": "43681388902", "commit": "7872857e7750e1b5091560b6362e52dd952bc6fa",
    "lane": "character_head_zero",
    "receipt_bytes": 45501,
    "receipt_sha256": "7919e2406650d394b1128d7014585dbdb830a87adb7979e74f6b2e752e484abf",
    "result_name": "character-head-zero-result.json", "result_bytes": 25121,
    "result_sha256": "838266c7b4b86b137482127e7e874d8d3eb014aa5745b9be6fceb2d9d3dc7fa4",
}
STATIC_TARGETS = {
    2: {"state": (0, 2, 0, 0),
        "pure_sha256": "ad4cd7fcdcbac89c55309c6906b6cb3a6d869ad37834e4a32fe8cad1b6e33393"},
    4: {"state": (0, 4, 0, 0),
        "pure_sha256": "5d70abb9d4000f457beb9d5d6d0adbf08f19becb953818f362c62b5c04dbb3e9"},
    6: {"state": (1, 1, 1, 0),
        "pure_sha256": "c074cfef87ff0f7b9435092bfce4615b7de12d2cbe4a0eabcb1a457d17b01044"},
}


def source_identity():
    value = zero.source_identity()
    if value["driver"] != ZERO_DRIVER:
        raise ValueError("published complete H0 source changed")
    value["frozen_complete_zero_head_driver"] = value.pop("driver")
    value["driver"] = static.identity(__file__)
    return value


def check_head_receipt(receipt):
    if (receipt.get("schema") != "visible-new-mechanism-actions-metadata-only-v2"
        or receipt.get("repository") != REPOSITORY
        or str(receipt.get("run_id")) != HEAD_ORIGIN["run"]
        or receipt.get("source_commit") != HEAD_ORIGIN["commit"]
        or receipt.get("lane") != HEAD_ORIGIN["lane"]
        or receipt.get("output_payloads_committed_or_uploaded") is not False
        or receipt.get("release_assets_created") is not False
        or receipt.get("machine_certificates_saved") is not False):
        raise ValueError("complete H0 metadata-only origin changed")
    source_name = "topics/visible-flex-new-mechanism/scripts/" + ZERO_DRIVER["filename"]
    found = receipt.get("source_files", {}).get(source_name)
    if found != {k: ZERO_DRIVER[k] for k in ("bytes", "sha256")}:
        raise ValueError("H0 receipt binds a different frozen driver")
    rows = [row for row in receipt.get("outputs", [])
            if row.get("path") == HEAD_ORIGIN["result_name"]]
    if len(rows) != 1:
        raise ValueError("unique published H0 summary identity required")
    row = rows[0]
    if (row.get("bytes") != HEAD_ORIGIN["result_bytes"]
        or row.get("sha256") != HEAD_ORIGIN["result_sha256"]
        or row.get("raw_bytes") != HEAD_ORIGIN["result_bytes"]
        or row.get("raw_sha256") != HEAD_ORIGIN["result_sha256"]
        or row.get("payload_published") is not False):
        raise ValueError("H0 stdout summary identity changed")


def bind_head_receipt(directory, report):
    raw = static.checked_bytes(directory / "receipt.json", 100000)
    if len(raw) != HEAD_ORIGIN["receipt_bytes"] or sha(raw) != HEAD_ORIGIN["receipt_sha256"]:
        raise ValueError("published H0 receipt size/hash changed")
    receipt = json.loads(raw)
    check_head_receipt(receipt)
    report["inputs"]["proved_H0"] = {
        **HEAD_ORIGIN, "driver": ZERO_DRIVER,
        "mathematics_from_published_R196_not_from_hash_metadata_alone": True,
        "summary_payload_was_not_archived": True,
        "basis_R16_plus_C2_C4_C6_from_complete_true_kernel": True,
        "lambda_plus_on_this_basis": ["0"] * 16 + ["1", "0", "0"],
    }


def normalized_static_weights(records, coordinates):
    """Combine old static roots BEFORE projecting: only three new sums."""
    rows = [row for row in records if row["mode"] == -4]
    if Counter(row["mode"] for row in records) != Counter({-4: 197, -2: 197}):
        raise ValueError("bound complete static coefficient coverage changed")
    states = []
    for row in rows:
        state, jets = head.split_key(row["geometry_key"])
        if any(jets):
            raise ValueError("static input contains geometric derivatives")
        states.append(state)
    if len(set(states)) != 197 or len({row["root"] for row in rows}) != 197:
        raise ValueError("duplicate old static coefficient key/root")
    return combine_normalization_rows(rows, states, coordinates,
                                      {i: d["state"] for i, d in STATIC_TARGETS.items()},
                                      head.constrained.BASIS_STATES)


def combine_normalization_rows(rows, states, coordinates, targets, references):
    result = {}
    coordinate_states = []
    for terms in coordinates:
        state_terms = {}
        for key, coefficient in terms.items():
            state, jets = head.split_key(key)
            if any(jets):
                raise ValueError("static Gamma coordinates must have derivative weight zero")
            state_terms[state] = state_terms.get(state, F(0)) + coefficient
        coordinate_states.append(state_terms)
    if len(coordinate_states) != len(references):
        raise ValueError("Gamma reference number mismatch")
    for index, state in targets.items():
        reference_coefficients = [terms.get(state, F(0)) for terms in coordinate_states]
        weights = {}
        for row, original_state in zip(rows, states):
            coefficient = F(original_state == state) - sum(
                (a * head.state_value(original_state, s)
                 for a, s in zip(reference_coefficients, references)), F(0))
            if coefficient:
                weights[row["root"]] = coefficient
        result[index] = weights
    return result


def restore_static_targets_and_W(ring, grade, data, labels, report):
    coordinates, reference = head.constrained.reference_coordinates()
    weights = normalized_static_weights(data["local_roots"], coordinates)
    needed_W = sorted({row["third_index"] for row in labels})
    names = set().union(*(set(w) for w in weights.values()))
    names.update("W" + str(j) for j in needed_W)
    roots = head.subset_decode(ring, data, names)
    targets, descriptions = {}, []
    for index, spec in STATIC_TARGETS.items():
        raw = sum((c * roots[name] for name, c in sorted(weights[index].items())),
                  ring.number(0))
        value = grade.project(raw, 0)
        if ring.digest(value) != spec["pure_sha256"]:
            raise ValueError("C%d pure root differs from completed H0 identity" % index)
        targets[index] = value
        descriptions.append({
            "normal_index": index, "family": "F0", "state_key": list(spec["state"]),
            "pure_original_sha256": ring.digest(value), "pure_original_terms": len(value.terms),
            "raw_static_combination": [[name, str(c)] for name, c in sorted(weights[index].items())],
            "raw_combination_sha256": ring.digest(raw), "same_Gamma_as_R196": True,
        })
    report["three_static_roots"] = {
        "records": descriptions, "reference_inverse_sha256": sha(canonical(reference)),
        "new_projected_raw_sums": 3, "old_all_197_projected_columns_repeated": False,
        "old_mixed_roots_decoded": False, "decoded_old_W_indices": needed_W,
    }
    return targets, {j: roots["W" + str(j)] for j in needed_W}


def pure_response(ring, third, quadratic):
    """Exactly the -4 component of frozen R78 blocks.full_response."""
    q = ring.color("q")
    a = quadratic(q, q)
    taqq = third(a, q, q)
    tqqa = third(q, q, a)
    tqqq = third(q, q, q)
    return taqq / 8 + tqqa / 4 - quadratic(q, tqqq) / 4


def restore_old_pure_responses(ring, W, labels, budget, report):
    quadratics = exact.operator_basis(ring)
    result = []
    for old_index, label in zip(zero.R0_KEEP, labels):
        j, a = label["third_index"], label["quadratic_index"]
        if (not 0 <= j < 36 or not 0 <= a < 8
            or label["quadratic_name"] != exact.PARAMETERS[a]
            or blocks.PARAMETER_WEIGHTS[a] + blocks.THIRD_WEIGHTS[j] != 0
            or ring.digest(W[j]) != label["third_original_sha256"]):
            raise ValueError("old pure R0 source label or original W root changed")
        value = pure_response(ring, colored.ThirdOperator(ring, W[j]), quadratics[a])
        if ring.digest(value) != label["original_mode_sha256"]["-4"]:
            raise ValueError("restored R0 pure hash mismatch at old column %d" % old_index)
        result.append(value)
        report["progress"] = {"old_pure_roots_restored": len(result), "old_pure_roots_needed": 16}
        budget.check()
    if len(result) != 16:
        raise ValueError("all sixteen old pure roots required")
    report["old_pure_restore"] = {
        "columns": 16, "original_indices": list(zero.R0_KEEP),
        "all_sixteen_old_pure_hashes_matched": True,
        "old_mixed_roots_rebuilt": 0, "new_response_columns": 0,
        "old_16_full_modes_or_four_dependencies_reevaluated": False,
        "old_profile_evaluations_repeated": 0,
        "reason": "R126 never archived raw DAG; R196 metadata-only run did not archive mapped rows",
    }
    return result


def map_pure_columns(ring, columns, args, budget, report):
    mapper = priority.PriorityWords(ring, max_calls=args.max_IBP_calls, max_terms=args.max_terms,
        max_shuffle_entries=args.max_cache_entries, max_cache_entries=args.max_cache_entries)
    dictionary, labels, vectors, conversions = {}, [], [], []
    for index, expression in enumerate(columns):
        for monomial in expression.terms:
            colors = Counter()
            for atom in monomial[1]:
                colors.update(ring.atom_color_degree(atom))
            if colors != Counter({"q": 4}):
                raise ValueError("this new target must remain q-only and quartic")
        word = mapper.expression(expression)
        if not all(priority.is_remainder_letter(letter)
                   for local, letters in word.terms for letter in letters):
            raise ValueError("pure word is outside the proved R179 grammar")
        vector = {}
        for key, coefficient in sorted(word.terms.items()):
            if key not in dictionary:
                if len(dictionary) >= args.max_terms:
                    raise literal.Limit("new pure dictionary row ceiling")
                dictionary[key] = len(labels)
                labels.append(key)
            vector[dictionary[key]] = coefficient
        vectors.append(vector)
        conversions.append({
            "column": index, "original_pure_sha256": ring.digest(expression),
            "original_pure_terms": len(expression.terms),
            "word_sha256": priority.digest(priority.rows(word)),
            "word_terms": len(word.terms), "R178_sound_R179_grammar": True,
        })
        report["progress"] = {"new_pure_mapped_columns": index + 1, "total_columns": len(columns)}
        budget.check()
    report["new_pure_map"] = {
        "mapped_columns": len(columns), "dictionary_rows": len(labels),
        "conversions": conversions, "conversions_sha256": sha(canonical(conversions)),
        "mapper_statistics": mapper.stats,
        "scope": "new pure projection gate; not a repeated joint H0 kernel",
        "old_pure_rows_were_not_archived": True,
    }
    return vectors, labels, mapper


def fraction_row(row):
    return [[i, str(c)] for i, c in sorted(row.items()) if c]


def reduce_column(vector, index, basis, budget):
    denominator = 1
    for coefficient in vector.values():
        denominator = lcm(denominator, coefficient.denominator)
        budget.check((denominator,))
    raw = {row: int(coefficient * denominator) for row, coefficient in vector.items()}
    raw, combination = literal.normalize_integer_pair(raw, {index: denominator})
    budget.check(raw.values())
    while raw and min(raw) in basis:
        raw, combination = literal.exact_reduce_step(raw, combination, basis, budget)
    return raw, combination


def exact_square_solve(matrix, rhs, budget):
    size = len(matrix)
    if size != len(rhs) or any(len(row) != size for row in matrix):
        raise ValueError("new dual requires an exactly square pivot system")
    rows = [[F(x) for x in row] + [F(b)] for row, b in zip(matrix, rhs)]
    for column in range(size):
        pivot = next((i for i in range(column, size) if rows[i][column]), None)
        if pivot is None:
            raise AssertionError("independent pure columns lost their pivot minor")
        rows[column], rows[pivot] = rows[pivot], rows[column]
        amount = rows[column][column]
        rows[column] = [x / amount for x in rows[column]]
        for i in range(size):
            if i != column and rows[i][column]:
                amount = rows[i][column]
                rows[i] = [x - amount * y for x, y in zip(rows[i], rows[column])]
                budget.check(q for x in rows[i] for q in (x.numerator, x.denominator))
        budget.check(q for x in rows[column] for q in (x.numerator, x.denominator))
    answer = [row[-1] for row in rows]
    if any(sum((F(a) * x for a, x in zip(row, answer)), F(0)) != F(b)
           for row, b in zip(matrix, rhs)):
        raise AssertionError("fresh exact dual multiplication failed")
    return answer


def decide_projection(vectors, budget):
    if len(vectors) < 1:
        raise ValueError("one target is required")
    target = len(vectors) - 1
    basis, independent = {}, []
    for index, vector in enumerate(vectors[:-1]):
        reduced, combination = reduce_column(vector, index, basis, budget)
        if reduced:
            pivot = min(reduced)
            basis[pivot] = {"vector": reduced, "combination": combination}
            independent.append(index)
    reduced, combination = reduce_column(vectors[-1], target, basis, budget)
    comparison_rank = len(basis)
    if not reduced:
        if not combination.get(target):
            raise AssertionError("target coefficient lost in a membership relation")
        coefficients = {i: -F(c, combination[target])
                        for i, c in combination.items() if i != target and c}
        fresh = dict(vectors[-1])
        for i, c in coefficients.items():
            literal.add_fraction_row(fresh, vectors[i], -c)
        if fresh:
            raise AssertionError("fresh sum of original mapped columns is nonzero")
        return {
            "outcome": "pure_member_lambda_plus_does_not_factor_on_U0",
            "comparison_rank": comparison_rank, "augmented_rank": comparison_rank,
            "coefficients": coefficients,
            "pure_transport_sum_exact_zero": True,
        }
    pivot = min(reduced)
    independent.append(target)
    rows = sorted(list(basis) + [pivot])
    transposed = [[vectors[i].get(row, F(0)) for row in rows] for i in independent]
    values = [F(i == target) for i in independent]
    weights = exact_square_solve(transposed, values, budget)
    dual = {row: c for row, c in zip(rows, weights) if c}
    evaluations = [sum((c * vector.get(row, F(0)) for row, c in dual.items()), F(0))
                   for vector in vectors]
    if evaluations != [F(0)] * target + [F(1)]:
        raise AssertionError("word dual does not have exact values on every original column")
    return {
        "outcome": "pure_nonmember_lambda_plus_factors_on_U0",
        "comparison_rank": comparison_rank, "augmented_rank": comparison_rank + 1,
        "dual": dual, "dual_values_all_columns": evaluations,
        "dual_support_bound": len(independent), "dual_all_original_columns_verified": True,
    }


def new_mapper(ring, args, remaining_calls):
    if remaining_calls <= 0:
        raise literal.Limit("fresh original difference exceeds the total new primitive-call budget")
    return priority.PriorityWords(ring, max_calls=remaining_calls, max_terms=args.max_terms,
        max_shuffle_entries=args.max_cache_entries, max_cache_entries=args.max_cache_entries)


def actual(args, report):
    budget = literal.Budget(args.max_seconds, args.memory_mib, args.integer_bits)
    limits = exact.Limits(seconds=args.max_seconds, nodes=350000, atoms=80000,
        terms=args.max_terms, rewrites=args.max_IBP_calls, memory_mib=args.memory_mib,
        rational_bits=args.integer_bits)
    ring = colored.ColoredRing(limits)
    grade = blocks.ScalingGrading(ring)
    report["phase"] = "bind_old_originals_and_completed_H0_theorem"
    bind_head_receipt(args.head_directory, report)
    labels = zero.read_R0_definition(args.R0_directory, report)
    _, data = head.bind_input("static", args.static_directory, report)
    targets, W = restore_static_targets_and_W(ring, grade, data, labels, report)
    del data
    report["phase"] = "restore_only_sixteen_missing_old_pure_roots"
    controls = restore_old_pure_responses(ring, W, labels, budget, report)
    del W
    # The target has lambda value one; all eighteen comparison columns have value zero.
    columns = controls + [targets[4], targets[6], targets[2]]
    column_labels = [{"kind": "old_R0", "old_column": i} for i in zero.R0_KEEP]
    column_labels += [{"kind": "normal", "index": i} for i in (4, 6, 2)]
    report["column_order"] = column_labels
    report["phase"] = "new_single_pure_projection_gate"
    vectors, dictionary, mapper = map_pure_columns(ring, columns, args, budget, report)
    decision = decide_projection(vectors, budget)
    certificate = {
        "schema": SCHEMA + "-in-memory-proof", "column_labels": column_labels,
        "original_pure_sha256": [ring.digest(v) for v in columns],
        "conversions": report["new_pure_map"]["conversions"],
        "decision": {k: v for k, v in decision.items() if k not in ("coefficients", "dual", "dual_values_all_columns")},
    }
    if "coefficients" in decision:
        coefficients = decision.pop("coefficients")
        difference = targets[2] - sum((c * columns[i] for i, c in coefficients.items()),
                                     ring.number(0))
        remaining = args.max_IBP_calls - mapper.run_primitive_calls
        fresh = new_mapper(ring, args, remaining).expression(difference)
        if fresh.terms:
            raise AssertionError("independent fresh raw pure difference did not vanish")
        relation = [[column_labels[i], str(c)] for i, c in sorted(coefficients.items())]
        decision.update(
            C2_pure_equals_comparison_combination=relation,
            original_difference_sha256=ring.digest(difference),
            original_difference_terms=len(difference.terms),
            fresh_original_pure_word_terms=0,
            fresh_original_pure_zero_sha256=priority.digest(priority.rows(fresh)),
            actual_U0_vector_H="C2 - displayed comparison combination",
            lambda_plus_H="1", H_pure_exact_zero=True,
            H_nonzero_in_complete_U0_by_published_lambda=True,
            universal_pure_readout_of_lambda_plus_impossible=True,
            actual_zero_pure_cost_constructed=False,
        )
        certificate["exact_original_relation"] = relation
    else:
        dual = decision.pop("dual")
        values = decision.pop("dual_values_all_columns")
        rows = []
        for row, coefficient in sorted(dual.items()):
            local, word = dictionary[row]
            rows.append({"row_id": row, "local": local, "word": word, "coefficient": str(coefficient)})
        if len(rows) > 19:
            raise AssertionError("new dual support exceeds the proved nineteen-column bound")
        decision.update(
            exact_word_dual=rows, dual_values_all_columns=list(map(str, values)),
            functional_definition="sum coefficient * the specified R178/R179 pure-word coefficient",
            lambda_plus_equals_this_dual_on_pure_U0=True,
            point_profile_evaluation_claimed=False,
            other_true_weights_annihilated_by_this_word_dual_proved=False,
            fixed_profile_all_U_readout_proved=False,
        )
        certificate["exact_word_dual"] = rows
    raw = canonical(certificate)
    if len(raw) > args.max_certificate_bytes:
        raise literal.Limit("in-memory new proof byte ceiling")
    report["decision"] = decision
    report["reproducible_certificate"] = {"bytes": len(raw), "sha256": sha(raw),
                                        "persisted": False}
    report.update(
        completion="complete", phase="complete_single_U0_pure_readout_gate",
        exact_integer_operations=budget.operations, maximum_integer_bits=budget.maximum_bits,
        mixed_roots_evaluated=0, new_response_columns=0, old_N_contractions_recomputed=0,
        old_N_projections_recomputed=0, full_H0_kernel_recomputed=False,
        old_profile_evaluations_repeated=0, power_tail_queries_performed=0,
        fixed_profile_period_or_gauge_paid=False, task_complete=False,
    )


def toy_only(args):
    """New toy matrices/normalization/pure formula; no real source inputs."""
    checks = {}
    budget = literal.Budget(args.max_seconds, args.memory_mib, args.integer_bits)
    # Dependent comparisons, with exact rational target coefficients.
    member_vectors = [{0: F(2)}, {0: F(3)}, {1: F(5)},
                      {0: F(7, 3), 1: F(-2, 7)}]
    member = decide_projection(member_vectors, budget)
    checks["new_member_with_dependent_comparisons_and_fractions"] = (
        member["comparison_rank"] == 2 and member["augmented_rank"] == 2
        and member["pure_transport_sum_exact_zero"])
    nonmember_vectors = member_vectors[:3] + [{0: F(1, 3), 1: F(2, 5), 2: F(7, 11)}]
    nonmember = decide_projection(nonmember_vectors, budget)
    checks["new_nonmember_exact_dual_all_original_columns"] = (
        nonmember["comparison_rank"] == 2 and nonmember["augmented_rank"] == 3
        and nonmember["dual_values_all_columns"] == [F(0), F(0), F(0), F(1)])
    # An earlier inserted pivot can be larger than the next pivot.
    shuffled = [{7: F(3)}, {1: F(2), 7: F(1)}, {4: F(5), 7: F(-2)}]
    decided = decide_projection(shuffled, budget)
    checks["new_dual_handles_nonmonotone_pivot_insertion"] = (
        decided["augmented_rank"] == 3 and len(decided["dual"]) <= 3)
    zero_target = decide_projection([{0: F(2)}, {}], budget)
    checks["new_zero_target_is_membership_not_rank_one"] = (
        zero_target["outcome"].startswith("pure_member") and not zero_target["coefficients"])
    # Invented one-reference static normalization, including a real log term.
    k0 = (0, 0, 0, 0, 0, 0, 0, 0)
    k2 = (0, 2, 0, 0, 0, 0, 0, 0)
    kl = (0, 0, 0, 0, 0, 0, 0, 1)
    rows = [{"root": "a"}, {"root": "b"}, {"root": "log"}]
    states = [(0, 0, 0, 0), (0, 2, 0, 0), (0, 0, 0, 1)]
    weights = combine_normalization_rows(rows, states, [{k0: F(1), k2: F(3)}],
        {5: (0, 2, 0, 0)}, [(F(1), F(1), F(2))])
    checks["new_static_Gamma_combination_keeps_reference_and_log_rules"] = (
        weights[5] == {"a": F(-3), "b": F(-2)})
    limits = exact.Limits(seconds=args.max_seconds, nodes=5000, atoms=1000,
        terms=2000, rewrites=3000, memory_mib=args.memory_mib, rational_bits=args.integer_bits)
    ring = colored.ColoredRing(limits)
    # Artificial multiplication operators: no archived W or real E8 direction.
    quadratic = lambda a, b: F(2, 3) * a * b
    third = lambda a, b, c: F(-5, 7) * a * b * c
    pure = pure_response(ring, third, quadratic)
    q = ring.color("q")
    checks["new_pure_only_formula_on_artificial_multiplication_operators"] = (
        not (pure + F(5, 84) * q * q * q * q).terms)
    # Independent fresh difference machinery only on an invented elementary identity.
    p = q.D()
    raw = (q * p).I() - q * q / 2
    reduced = priority.PriorityWords(ring, max_calls=1000, max_terms=2000).expression(raw)
    checks["new_raw_relation_fresh_pure_word_zero"] = not reduced.terms
    if not all(checks.values()):
        raise AssertionError("new artificial readout interface failed: " + str(checks))
    return {"checks": checks, "all_passed": True, "real_inputs_read": False,
            "old_toy_suites_repeated": False, "research_projection_performed": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only", action="store_true")
    parser.add_argument("--output", type=Path, help="ephemeral runner summary; do not publish payload")
    parser.add_argument("--static-directory", type=Path,
        default=TOPIC / "notes" / head.INPUTS["static"]["directory"])
    parser.add_argument("--R0-directory", type=Path,
        default=TOPIC / "notes" / "actions-43649525432-1-g_first_translation")
    parser.add_argument("--head-directory", type=Path,
        default=TOPIC / "notes" / "actions-43681388902-1-character_head_zero")
    parser.add_argument("--max-seconds", type=float, default=120)
    parser.add_argument("--memory-mib", type=int, default=512)
    parser.add_argument("--integer-bits", type=int, default=8192)
    parser.add_argument("--max-terms", type=int, default=80000)
    parser.add_argument("--max-IBP-calls", type=int, default=150000)
    parser.add_argument("--max-cache-entries", type=int, default=150000)
    parser.add_argument("--max-summary-bytes", type=int, default=95000)
    parser.add_argument("--max-certificate-bytes", type=int, default=2000000)
    args = parser.parse_args()
    if min(args.max_seconds, args.memory_mib, args.integer_bits, args.max_terms,
           args.max_IBP_calls, args.max_cache_entries, args.max_summary_bytes,
           args.max_certificate_bytes) <= 0 or args.max_summary_bytes >= 100000:
        parser.error("positive budgets and summary below 100KB required")
    if not args.toy_only and not (os.environ.get("GITHUB_ACTIONS") == "true"
                                  and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY):
        parser.error("the actual pure readout gate runs only in this public repository Actions")
    started = time.monotonic()
    report = {
        "schema": SCHEMA, "completion": "started", "phase": "source_binding",
        "github_repository": os.environ.get("GITHUB_REPOSITORY"),
        "github_run_id": os.environ.get("GITHUB_RUN_ID"), "github_sha": os.environ.get("GITHUB_SHA"),
        "inputs": {}, "scope": "one universal-pure readout gate on the completed U0",
        "recomputable_payload_publication_permitted": False,
    }
    code = 0
    try:
        report["source_hashes"] = source_identity()
        if args.toy_only:
            report["development"] = toy_only(args)
            report.update(completion="complete", phase="new_artificial_readout_interfaces_only")
        else:
            actual(args, report)
    except (literal.Limit, formal.CompilationBudgetExceeded, MemoryError) as error:
        report.update(completion="resource_limit", error=str(error),
                      complete_new_pure_gate=False, partial_is_not_membership_or_nonmembership=True)
        code = 2
    except Exception as error:
        report.update(completion="implementation_check_failed",
                      error={"type": type(error).__name__, "message": str(error)},
                      complete_new_pure_gate=False)
        code = 1
    report["elapsed_seconds"] = time.monotonic() - started
    report["peak_rss_mib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
    body = canonical(report) + b"\n"
    if len(body) > args.max_summary_bytes:
        report = {"schema": SCHEMA, "completion": "summary_output_limit",
            "full_summary_bytes": len(body), "full_summary_sha256": sha(body),
            "github_run_id": report["github_run_id"], "github_sha": report["github_sha"],
            "source_hashes": report.get("source_hashes"),
            "no_payload_saved": True, "complete_new_pure_gate": False}
        body = canonical(report) + b"\n"
        code = 2
    if len(body) > args.max_summary_bytes:
        raise ValueError("minimal summary exceeds the declared byte cap")
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(body)
    print(body.decode().rstrip(), flush=True)
    print(json.dumps({"summary_bytes": len(body), "summary_sha256": sha(body),
                     "payload_publication_permitted": False}, sort_keys=True), flush=True)
    raise SystemExit(code)


if __name__ == "__main__":
    main()

