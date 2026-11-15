#!/usr/bin/env python3
"""Complete pure weight -4 image from published originals.

This is the last possible pure positive-character weight after R207.  Consume
R139's forty saved pure response roots and the original complete local factors.
Reuse the archived -2 input projections; restore only seventy intermediate
pure diagonals whose R207 execution could not persist under root README 15.
No -6 target, old full/mixed response, old profile evaluation, or old NF is run.
Actual research is Actions-only; reproducible payloads remain in memory.
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

import literature_complete_pure_minus6_projection as previous

zero,head,literal,priority=previous.zero,previous.head,previous.literal,previous.priority
layer,old,static=previous.layer,previous.old,previous.static
colored,exact,blocks,formal=previous.colored,previous.exact,previous.blocks,previous.formal
Field=previous.Field
canonical,sha=previous.canonical,previous.sha
REPOSITORY,TOPIC=previous.REPOSITORY,previous.TOPIC
subset_decode=previous.subset_decode
check_pure=previous.check_pure
diagonal_response=previous.diagonal_response
reduce_column=previous.reduce_column
square_solve=previous.square_solve
SCHEMA="visible-flex-complete-pure-minus4-projection-v1"
WEIGHT=-4
ZERO=(0,0,0,0)
R_KEEP=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,
        21,22,23,24,26,27,28,29,30,32,34,35,36,37,41,42,43,44,45,49)
R_COUNT=len(R_KEEP)
PREVIOUS_DRIVER={"filename":"literature_complete_pure_minus6_projection.py","bytes":51380,
    "sha256":"c57776cfc75ed437bf3b7f8cbcae45072b295892ecee6c93c6297519eee22c2e"}
R_INPUT={
    "run":"43654534244","commit":"1177f251dc3d9455adf88b585e4c0e4bd6f7e69b",
    "lane":"g_translation_successor","schema":"visible-flex-G-translation-successor-original-v1",
    "main":{"filename":"G-fifth-translation.json","bytes":24966,
        "sha256":"faf6c2a0019ce614bb8d6f28b049f0a38a6c2f6e2e00930a1beab17e6c86f93e"},
    "receipt":{"filename":"receipt.json","bytes":34625,
        "sha256":"e8f37f37ba85f822e6eacc17167fb6941017dc05ec7670b8fafa7b450dc4d24d"},
    "artifact":{"filename":"G-fifth-translation-original-expressions.json.gz",
        "stored_bytes":76352,"stored_sha256":"b266eebf27d001ef90fcc94f8b49b9f9984ed5d3f7a047d9b5cef5ddffd2423b",
        "raw_bytes":427950,"raw_sha256":"6e19e56d879eed7f7d741957526679521f65f06b92c42b4cb29f39fb2c2276e4"},
    "driver":{"filename":"literature_G_translation_successor.py","bytes":39670,
        "sha256":"a4583ea776facd4ec4d92a121fed2e79af8de20d57bffc5fa22e47a8026ef406"},
}
R_DEPENDENCIES_SHA="866e724012d102537c7ff1da010c5deb5d94d1ab19cffb601552248043f8f0ab"


def source_identity():
    if static.identity(previous.__file__)!=PREVIOUS_DRIVER:
        raise ValueError("frozen pure import/diagonal/integer helpers changed")
    value=previous.source_identity()
    value["frozen_minus6_generic_helpers"]=value.pop("driver")
    value["driver"]=static.identity(__file__)
    return value



def bind_R(ring, directory, report):
    main, raw = literal.read_small(directory / R_INPUT["main"]["filename"], R_INPUT["main"])
    receipt, _ = literal.read_small(directory / "receipt.json", R_INPUT["receipt"])
    checkpoint = main.get("checkpoint") or {}
    metadata = checkpoint.get("portable_new_block_expression_export") or {}
    literal.verify_publication(receipt, main, raw, R_INPUT, metadata)
    upper = checkpoint.get("response_upper_bound") or {}
    dual = checkpoint.get("dual_certificate") or {}
    if (checkpoint.get("requested_order") != 5 or checkpoint.get("requested_weight") != WEIGHT
        or upper.get("original_columns") != 50
        or upper.get("proved_true_response_dimension_upper_bound") != R_COUNT
        or upper.get("retained_original_columns") != list(R_KEEP)
        or upper.get("verified_original_dependency_count") != 10
        or upper.get("verified_original_dependencies_sha256") != R_DEPENDENCIES_SHA
        or dual.get("modular_control_rank") != R_COUNT or not dual.get("modular_pivot_determinant")
        or dual.get("rational_nonmembership_certified") is not True):
        raise ValueError("the published complete true R_-4 span/basis identity changed")
    data = literal.checked_gzip(directory / metadata["filename"], metadata)
    coverage = data.get("response_coverage") or {}
    if (data.get("schema") != R_INPUT["schema"] + "-original-expressions"
        or data.get("source_hashes") != main.get("source_hashes")
        or str(data.get("github_run_id")) != R_INPUT["run"]
        or data.get("github_sha") != R_INPUT["commit"]
        or data.get("content_scope") != "one-translation-target-and-complete-new-response-block"
        or data.get("all_compiled_original_columns_included") is not True
        or coverage.get("full_E8") is not True or coverage.get("all_W36") is not True
        or coverage.get("columns") != 50 or coverage.get("weight") != WEIGHT):
        raise ValueError("complete old response export scope/source changed")
    records = data.get("column_records") or []
    if len(records) != 50 or [r["index"] for r in records] != list(range(50)):
        raise ValueError("old fifty response column identities changed")
    selected = [records[i] for i in R_KEEP]
    roots = subset_decode(ring, data, [r["roots"]["-4"] for r in selected], {"q"}, report, "R139-pure")
    result, labels = [], []
    for old_index, row in zip(R_KEEP, selected):
        label = row["label"]
        a = label["quadratic_index"]
        value = roots[row["roots"]["-4"]]
        if (not 0 <= a < 8 or label["quadratic_name"] != exact.PARAMETERS[a]
            or label["third_weight"] + blocks.PARAMETER_WEIGHTS[a] != WEIGHT
            or ring.digest(value) != row["original_mode_sha256"]["-4"]
            or row["original_mode_sha256"] != label["original_mode_sha256"]):
            raise ValueError("retained original response label/hash changed")
        check_pure(ring, value, weight=WEIGHT)
        result.append(value)
        labels.append({"old_column": old_index, "quadratic": label["quadratic_name"],
                       "W_index": label["third_index"], "pure_sha256": ring.digest(value)})
    report["inputs"]["R4"] = {k: R_INPUT[k] for k in ("run", "commit", "lane", "main", "receipt", "artifact", "driver")}
    report["old_response_span"] = {"full_two_mode_dimension_already_proved": R_COUNT,
        "retained_old_columns": list(R_KEEP), "old_ten_dependencies_sha256": R_DEPENDENCIES_SHA,
        "pure_dimension_assumed": False, "old_responses_reconstructed": 0,
        "old_full_word_or_profile_evaluations_repeated": 0, "labels": labels}
    return result


def select_factor_rows(factors, matrix):
    if (factors.get("geometry_names") != list(layer.factors.GEOMETRY_NAMES)
        or factors.get("real_s_derivatives_before_history_zero") is not True
        or factors.get("potential_two_assumed_in_W") is not False):
        raise ValueError("complete original factor semantics changed")
    potential = factors.get("potential_records") or []
    if Counter(r["geometry_derivative_weight"] for r in potential) != Counter({0: 79, 2: 93}):
        raise ValueError("all 172 original potential records required")
    selected, logarithms = [], []
    seen = set()
    for row in potential:
        dw, key = row["geometry_derivative_weight"], row["geometry_key"]
        state, jets = head.split_key(key)
        if any(jets[2:]) or sum(jets[:2]) != dw or (dw, tuple(key)) in seen:
            raise ValueError("potential derivative support or uniqueness changed")
        seen.add((dw, tuple(key)))
        if dw == 2:
            eligible = {WEIGHT - blocks.PARAMETER_WEIGHTS[a] for a in range(8)
                        if matrix[0][a] or matrix[2][a]}
        else:
            eligible = {WEIGHT - blocks.PARAMETER_WEIGHTS[a] for a in range(8) if matrix[2][a]}
        kappa = zero.geometry_index(key)
        if kappa not in eligible:
            continue
        if state[3]:
            # R190 finite scaling cocycle, not an unproved literal root zero.
            if dw != 0 or tuple(key) not in (
                (0, 2, 1, 0, 0, 0, 0, 1, 0, 0),
                (0, 2, 2, 0, 0, 0, 0, 1, 0, 0),
                (0, 2, 3, 0, 0, 0, 0, 1, 0, 0),
                (0, 2, 4, 0, 0, 0, 0, 1, 0, 0)):
                raise ValueError("undeclared logarithmic quotient representative")
            logarithms.append(row)
            continue
        selected.append(row)
    expected = {(0, -4): 13, (0, -3): 14, (0, -2): 12, (0, -1): 10,
                (2, -5): 24, (2, -4): 19, (2, -3): 12, (2, -2): 7, (2, -1): 3}
    if Counter((r["geometry_derivative_weight"], zero.geometry_index(r["geometry_key"]))
               for r in selected) != Counter(expected) or len(logarithms) != 4:
        raise ValueError("complete selected geometric potential inventory changed")
    records = factors.get("local_generator_records") or []
    if Counter((r["mode"], r["geometry_derivative_weight"]) for r in records) != Counter(
        {(-4, 2): 665, (-2, 2): 665, (-4, 4): 1236, (-2, 4): 1236}):
        raise ValueError("complete 3802 local generator inventory changed")
    patterns2 = {(0, 0, 1, 0, 0, 0): "p", (0, 0, 0, 1, 0, 0): "q",
        (2, 0, 0, 0, 0, 0): "q20", (1, 1, 0, 0, 0, 0): "q11", (0, 2, 0, 0, 0, 0): "q02"}
    vrows, counts = [], Counter()
    for row in records:
        if row["mode"] != -4 or zero.geometry_index(row["geometry_key"]) != WEIGHT:
            continue
        dw = row["geometry_derivative_weight"]
        state, jets = head.split_key(row["geometry_key"])
        counts[dw] += 1
        if dw == 2:
            tag = patterns2[jets]
        else:
            tag, found = layer.shape(tuple(row["geometry_key"]))
            if tuple(found) != state:
                raise ValueError("v4 state key convention changed")
            if tag in ("A_hh", "A_hk", "A_kk"):
                continue
            if tag == "velocity_quartic_not_consumed":
                tag = "q4_" + str(jets[0])
        vrows.append((dw, tag, state, row["root"]))
    if counts != Counter({2: 62, 4: 97}) or Counter(r[0] for r in vrows) != Counter({2: 62, 4: 78}):
        raise ValueError("complete new pure v2/v4 support changed")
    return selected, logarithms, vrows


def archived_request(row):
    """Exactly the requests covered by the old complete 1139-entry plan.

    For this target, N0 weights -1/-2 and N2 weights -1/-2/-3 were
    computed there.  An absent nonzero-cache entry in this declared subset
    is an archived exact empty projection, not a missing request.
    """
    weight=zero.geometry_index(row["geometry_key"])
    return weight in ((-1,-2) if row["geometry_derivative_weight"]==0 else (-1,-2,-3))


def restore_missing_factors(ring,grade,factors,cache_data,report):
    matrix=head.read_matrix(factors)
    selected,logarithms,vrows=select_factor_rows(factors,matrix)
    lookup=zero.old_projection_index(cache_data)
    old_names,new_names,descriptions,empty=set(),set(),[],[]
    for row in selected:
        weight=zero.geometry_index(row["geometry_key"])
        reuse=archived_request(row)
        bound=lookup.get((row["root"],weight)) if reuse else None
        wanted=factors["original_root_sha256"][row["root"]]
        if reuse and bound is None:
            empty.append({"root":row["root"],"third_weight":weight,"raw_sha256":wanted,
                "proof":"same-raw-factor-complete-old-1139-request-plan-exact-empty"})
            continue
        if reuse:
            if (bound["original_sha256"]!=wanted or bound["geometry_key"]!=row["geometry_key"]
                or bound["derivative_weight"]!=row["geometry_derivative_weight"]):
                raise ValueError("archived nonzero projection is not the same original factor")
            old_names.add(bound["input_root"])
        else:
            new_names.add(row["root"])
        descriptions.append((row,weight,bound))
    if (len([r for r in descriptions if r[2] is not None])!=35
        or len(empty)!=9 or len(new_names)!=70):
        raise ValueError("exact 44 archived requests / seventy dependency restores changed")
    decoded=subset_decode(ring,factors,new_names|{r[3] for r in vrows},
        {"a","b","c","q"},report,"required-pure-factors-only")
    archived=subset_decode(ring,cache_data,old_names,{"a","b","c"},report,"old-complete-projected-inputs")
    q,nrows,identities=ring.color("q"),[],[]
    for row,weight,bound in descriptions:
        typed=archived[bound["input_root"]] if bound else decoded[row["root"]]
        if any(d!=(("a",1),("b",1),("c",1)) for d in ring.color_degrees(typed)):
            raise ValueError("typed N lost its exterior/inner slots")
        if bound and ring.digest(typed)!=bound["sha256"]:
            raise ValueError("archived projected input original SHA changed")
        diagonal=ring.substitute(typed,{"a":q,"b":q,"c":q})
        value=diagonal if bound else grade.project(diagonal,weight)
        check_pure(ring,value,degree=3,weight=weight,grade=grade)
        state,jets=head.split_key(row["geometry_key"])
        signature=ring.digest(value)
        identities.append({"root":row["root"],"geometry_key":row["geometry_key"],
            "third_weight":weight,"unprojected_sha256":factors["original_root_sha256"][row["root"]],
            "saved_projection_root":bound["input_root"] if bound else None,
            "saved_projection_sha256":bound["sha256"] if bound else None,
            "dependency_restored_from_raw_because_R207_intermediates_not_persisted":bound is None,
            "pure_diagonal_sha256":signature,"pure_diagonal_terms":len(value.terms)})
        if not value.terms:continue
        base={"root":row["root"]+"@"+str(weight),"third_weight":weight,
            "geometry_derivative_weight":row["geometry_derivative_weight"],
            "state":state,"velocity":jets[:2],"factor":F(1),
            "value":value,"input_sha256":signature}
        nrows.append(base)
        if row["geometry_derivative_weight"]==0:
            nrows.append({**base,"root":base["root"]+":reference-subtraction",
                "state":ZERO,"factor":F(-1)})
    groups={2:{},4:{}}
    for dw,tag,state,name in vrows:
        field=groups[dw].setdefault(tag,{})
        if state in field:raise ValueError("duplicate selected v state")
        value=grade.project(decoded[name],WEIGHT)
        check_pure(ring,value,weight=WEIGHT,grade=grade)
        field[state]=value
    report["new_factor_work"]={
        "selected_potential_records":len(selected),"archived_projection_requests_consumed":44,
        "archived_nonzero_projected_uses":35,"archived_exact_empty_uses":empty,
        "unpersisted_pure_dependency_diagonal_projections_restored":70,
        "dependency_restore_reason":"R207 could not persist recomputable intermediates under root README15",
        "R207_matrix_or_old_response_targets_repeated":False,
        "nonzero_diagonals":sum(bool(r["pure_diagonal_terms"]) for r in identities),
        "zero_log_N0_reference_constants_retained":True,
        "discarded_log_records_are_W_valued_not_literal_zero":[r["root"] for r in logarithms],
        "new_v2_raw_projections":62,"new_v4_beta_C_Q_raw_projections":78,
        "new_static_pure_raw_projections":197,"old_A_H_recompiled":False,
        "input_projection_identities_sha256":sha(canonical(identities)),
        "mixed_profile_roots_decoded":0,"old_3974_producer_recompiled":False}
    return matrix,nrows,groups,{"projected_inputs":identities,"archived_empty_inputs":empty}



def restore_static(ring, grade, data, report):
    rows = data.get("local_roots") or []
    if (Counter(r["mode"] for r in rows) != Counter({-4: 197, -2: 197})
        or data.get("projection") != "derivative weight zero"):
        raise ValueError("complete published static original density changed")
    rows = [r for r in rows if r["mode"] == -4]
    roots = subset_decode(ring, data, [r["root"] for r in rows], {"q"}, report, "old-static-pure")
    terms = {}
    for row in rows:
        state, jets = head.split_key(row["geometry_key"])
        if any(jets) or state in terms:
            raise ValueError("static source is not a unique state polynomial")
        terms[state] = grade.project(roots[row["root"]], WEIGHT)
        check_pure(ring, terms[state], weight=WEIGHT, grade=grade)
    return Field(ring, terms)


def restore_acceleration(ring, data, report):
    rows = [r for r in data.get("family_records", []) if WEIGHT in r["profile_weights"]]
    if (len(data.get("family_records", [])) != 314 or len(rows) != 29
        or Counter(r["family"] for r in rows) != Counter({"A_hh": 9, "A_hk": 6, "A_kk": 4, "H1": 6, "H2": 4})
        or any(r["profile_weights"] != [WEIGHT] for r in rows)):
        raise ValueError("complete published weight -4 five-family support changed")
    roots = subset_decode(ring, data, [r["roots"]["-4"] for r in rows], {"q"}, report, "old-five-normal-families-pure")
    out = {family: {} for family in layer.FAMILIES}
    for row in rows:
        family, state = row["family"], tuple(row["state_key"])
        value = roots[row["roots"]["-4"]]
        if state in out[family] or ring.digest(value) != row["original_mode_sha256"]["-4"]:
            raise ValueError("published acceleration root/hash or alias changed")
        check_pure(ring, value, weight=WEIGHT)
        out[family][state] = value
    return {family: Field(ring, terms) for family, terms in out.items()}


def contraction_plan(nrows, matrix):
    plan = {}
    for row in nrows:
        for a in range(8):
            available = matrix[2][a] if row["geometry_derivative_weight"] == 0 else (matrix[0][a] or matrix[2][a])
            if not available or row["third_weight"] + blocks.PARAMETER_WEIGHTS[a] != WEIGHT:
                continue
            token = (a, row["input_sha256"])
            item = plan.setdefault(token, {"parameter": a, "input": row["value"], "uses": []})
            if item["input"].terms != row["value"].terms:
                raise ValueError("pure diagonal hash collision")
            item["uses"].append(row["root"])
    if len(plan) > 164:
        raise ValueError("declared at-most-164 new pure contractions exceeded")
    return plan


def subtract_responses(fields, degree, nrows, nweight, matrix, mweight, cache):
    for row in nrows:
        if row["geometry_derivative_weight"] != nweight:
            continue
        for a, scalar in enumerate(matrix[mweight]):
            if not scalar or row["third_weight"] + blocks.PARAMETER_WEIGHTS[a] != WEIGHT:
                continue
            token = (a, row["input_sha256"])
            if token not in cache:
                raise ValueError("a missing contraction is not a zero response")
            for (mstate, mvelocity), coefficient in scalar.items():
                velocity = tuple(x + y for x, y in zip(row["velocity"], mvelocity))
                if sum(velocity) != degree:
                    raise ValueError("contraction derivative weight changed")
                state = tuple(x + y for x, y in zip(row["state"], mstate))
                head.add_term(fields[velocity[0]], state, -row["factor"] * coefficient * cache[token])


def assemble(ring, groups, nrows, matrix, coordinates, cache, static_field, acceleration):
    references = [head.evaluate_field(static_field, s) for s in head.constrained.BASIS_STATES]
    q2 = {i: dict(f.terms) for i, f in head.normalize_v2(groups[2], ring).items()}
    q4 = {i: dict(f.terms) for i, f in head.normalize_v4_quartic(groups[4], ring).items()}
    subtract_responses(q2, 2, nrows, 2, matrix, 0, cache)
    subtract_responses(q2, 2, nrows, 0, matrix, 2, cache)
    subtract_responses(q4, 4, nrows, 2, matrix, 2, cache)
    f0 = static_field
    for i, value in enumerate(references):
        f0 = f0.add(head.scalar_times(head.coefficient_scalar(coordinates[0], i, (0, 0)), value), -1)
        for j in range(3):
            correction = head.scalar_times(head.coefficient_scalar(coordinates[2], i, (j, 2-j)), value)
            for key, term in correction.terms.items():
                head.add_term(q2[j], key, -term)
    if any(head.evaluate_field(f0, s).terms for s in head.constrained.BASIS_STATES):
        raise ValueError("same eight-reference static normalization failed")
    families = {"F0": f0, **{"Q2_" + str(i): Field(ring, q2[i]) for i in range(3)},
                **acceleration, **{"Q4_" + str(i): Field(ring, q4[i]) for i in range(5)}}
    if set(families) != set(head.FAMILIES):
        raise ValueError("all fourteen complete normal families are required")
    return families, references


def collect_normal(ring, families):
    """Exact literal proportionality only; no function relation is assumed."""
    values, hashes, lookup, aliases = [], [], {}, []
    counts = {}
    for family_index, family in enumerate(head.FAMILIES):
        counts[family] = len(families[family].terms)
        for state, value in sorted(families[family].terms.items()):
            check_pure(ring, value, weight=WEIGHT)
            scale = value.terms[min(value.terms)]
            unit = value / scale
            signature = ring.digest(unit)
            index = lookup.get(signature)
            if index is None:
                index = len(values)
                lookup[signature] = index
                values.append(unit)
                hashes.append(signature)
            elif values[index].terms != unit.terms:
                raise ValueError("normalized original hash collision")
            aliases.append([family_index, list(state), index, str(scale)])
    return values, hashes, aliases, counts


def whole_pure_matrix(ring, columns, args, budget, report, r_count=R_COUNT):
    mapper = priority.PriorityWords(ring, max_calls=args.max_IBP_calls, max_terms=args.max_terms,
        max_shuffle_entries=args.max_cache_entries, max_cache_entries=args.max_cache_entries)
    dictionary, labels, vectors, conversions = {}, [], [], []
    basis, independent, coordinates, relations = {}, [], [], []
    first_nonmember, R_rank, R_pivots, R_independent = None, None, None, None
    for index, expression in enumerate(columns):
        check_pure(ring, expression, weight=WEIGHT)
        word = mapper.expression(expression)
        if not all(priority.is_remainder_letter(letter) for local, letters in word.terms for letter in letters):
            raise ValueError("new pure representative is outside R179 grammar")
        vector = {}
        for key, coefficient in sorted(word.terms.items()):
            if key not in dictionary:
                if len(labels) >= args.max_terms:
                    raise literal.Limit("new complete pure word row ceiling")
                dictionary[key] = len(labels)
                labels.append(key)
            vector[dictionary[key]] = coefficient
        vectors.append(vector)
        conversion = {"column": index, "original_sha256": ring.digest(expression),
            "original_terms": len(expression.terms), "word_sha256": priority.digest(priority.rows(word)),
            "word_terms": len(word.terms), "proved_remainder_grammar": True}
        conversions.append(conversion)
        reduced, combination = reduce_column(vector, index, basis, budget)
        if reduced:
            pivot = min(reduced)
            basis[pivot] = {"vector": reduced, "combination": combination}
            independent.append(index)
            coordinates.append({index: F(1)})
            if index >= r_count and first_nonmember is None:
                first_nonmember = {"column": index, "pivot": pivot}
        else:
            if not combination.get(index):
                raise AssertionError("triangular relation lost the current original column")
            coefficients = {i: -F(c, combination[index]) for i, c in combination.items() if i != index and c}
            if not set(coefficients).issubset(independent):
                raise AssertionError("relation includes a previously dependent original column")
            fresh = dict(vector)
            original_difference = expression
            for i, c in coefficients.items():
                literal.add_fraction_row(fresh, vectors[i], -c)
                original_difference = original_difference - c * columns[i]
            if fresh:
                raise AssertionError("independent sum of complete transported original words is nonzero")
            coordinates.append(coefficients)
            relations.append({"column": index, "coefficients": literal.serial_fraction_row(coefficients),
                "original_difference_sha256": ring.digest(original_difference),
                "original_difference_terms": len(original_difference.terms),
                "transported_complete_word_sum_sha256": sha(canonical([])),
                "transported_complete_word_sum_exact_zero": True})
        if index == r_count-1:
            R_rank, R_pivots, R_independent = len(basis), sorted(basis), list(independent)
        report["progress"] = {"completed_pure_columns": index + 1, "total_columns": len(columns),
                              "current_true_word_rank": len(basis)}
        budget.check()
    if R_rank is None:
        raise ValueError("all declared complete old responses must precede normal columns")
    dual = None
    if first_nonmember is not None:
        target = first_nonmember["column"]
        selected_rows = sorted(R_pivots + [first_nonmember["pivot"]])
        selected_columns = R_independent + [target]
        transposed = [[vectors[i].get(row, F(0)) for row in selected_rows] for i in selected_columns]
        weights = square_solve(transposed, [F(i == target) for i in selected_columns], budget)
        functional = {row: c for row, c in zip(selected_rows, weights) if c}
        evaluated = [sum((c * vector.get(row, F(0)) for row, c in functional.items()), F(0))
                     for vector in vectors[:r_count] + [vectors[target]]]
        if evaluated != [F(0)] * r_count + [F(1)]:
            raise AssertionError("new pure quotient dual fails original response/target checks")
        dual = {"target_global_column": target, "values_on_all_old_R_and_target": list(map(str, evaluated)),
            "word_coefficient_functional": [[labels[row][0], labels[row][1], str(c)] for row, c in sorted(functional.items())],
            "support_at_most_response_rank_plus_one": len(functional) <= R_rank + 1,
            "all_other_affine_weights_or_positive_costs_annihilated": False}
    report["new_pure_word_map"] = {"mapped_columns": len(columns), "dictionary_rows": len(labels),
        "conversions_sha256": sha(canonical(conversions)), "all_same_anchor_conversions_sound": True,
        "all_remainders_in_R179_injective_grammar": True, "statistics": mapper.stats,
        "new_original_profile_evaluations": 0, "old_two_mode_matrix_repeated": False}
    certificate = {"schema": SCHEMA + "-in-memory-complete-proof", "dictionary": labels,
        "vectors": [literal.serial_fraction_row(v) for v in vectors], "conversions": conversions,
        "relations": relations, "independent_global_columns": independent,
        "coordinates": [literal.serial_fraction_row(v) for v in coordinates], "nonmember_dual": dual}
    decision = {"complete_fourteen_family_pure_image": True,
        "pure_response_rank": R_rank, "complete_pure_U_rank": len(basis),
        "pure_quotient_dimension": len(basis) - R_rank,
        "pure_U_minus4_equals_pure_R_minus4": first_nonmember is None,
        "independent_global_columns": independent,
        "verified_original_transport_relations": len(relations),
        "relation_proof": "sum exact same-anchor R178 column identities; R179 makes the shared word kernel the true function kernel",
        "fresh_original_difference_normalization_repeated": False,
        "nonmember_dual": dual,
        "complete_normalized_column_coordinates": [literal.serial_fraction_row(v) for v in coordinates[r_count:]],
        "old_response_coordinates": [literal.serial_fraction_row(v) for v in coordinates[:r_count]],
        "pure_positive_character_at_minus4_excluded_by_response_lineality": first_nonmember is None,
        "nonzero_quotient_implies_positive_character": False,
        "other_weights_mixed_period_ruling_or_main_task_complete": False}
    return decision, certificate


def actual(args, report):
    budget = literal.Budget(args.max_seconds, args.memory_mib, args.integer_bits)
    limits = exact.Limits(seconds=args.max_seconds, nodes=500000, atoms=150000,
        terms=args.max_terms, rewrites=args.max_IBP_calls, memory_mib=args.memory_mib,
        rational_bits=args.integer_bits)
    ring, proof = colored.ColoredRing(limits), {}
    grade = blocks.ScalingGrading(ring)
    report["phase"] = "bind_existing_complete_original_inputs"
    controls = bind_R(ring, args.R4_directory, report)
    _, factors = head.bind_input("factors", args.factor_directory, report)
    cache_main, cache_data, binding = literal.consume_bound(args.cache_directory, literal.HEAD)
    zero.check_cached_head(cache_main, cache_data)
    report["inputs"]["old_projection_cache"] = binding
    report["phase"] = "restore_required_diagonals_and_new_minus4_v_coefficients"
    matrix, nrows, groups, proof["potential_projections"] = restore_missing_factors(ring, grade, factors, cache_data, report)
    del factors, cache_data, cache_main
    _, static_data = head.bind_input("static", args.static_directory, report)
    static_field = restore_static(ring, grade, static_data, report)
    del static_data
    _, acceleration_data = head.bind_input("acceleration", args.acceleration_directory, report)
    acceleration = restore_acceleration(ring, acceleration_data, report)
    del acceleration_data
    plan = contraction_plan(nrows, matrix)
    quadratics, cache, contraction_identities = exact.operator_basis(ring), {}, []
    report["phase"] = "only_missing_pure_diagonal_responses"
    report["planned_new_pure_contractions"] = len(plan)
    for token, entry in sorted(plan.items()):
        a, signature = token
        value = diagonal_response(ring, entry["input"], quadratics[a])
        check_pure(ring, value, weight=WEIGHT, grade=grade)
        cache[token] = value
        contraction_identities.append({"parameter": a, "pure_input_sha256": signature,
            "response_sha256": ring.digest(value), "response_terms": len(value.terms), "uses": entry["uses"]})
        report["progress"] = {"completed_new_pure_contractions": len(cache), "planned": len(plan)}
        budget.check()
    proof["new_pure_contractions"] = contraction_identities
    report["completed_new_pure_contractions"] = len(cache)
    report["new_pure_contractions_sha256"] = sha(canonical(contraction_identities))
    _, reference = head.constrained.reference_coordinates()
    inverse = [[F(v) for v in row] for row in reference["inverse"]]
    coordinates = head.coordinate_polynomials(matrix, inverse)
    report["phase"] = "complete_fourteen_pure_families_same_Gamma"
    families, references = assemble(ring, groups, nrows, matrix, coordinates, cache, static_field, acceleration)
    normal, normal_hashes, aliases, counts = collect_normal(ring, families)
    report["normal_presentation"] = {
        "family_order": list(head.FAMILIES), "state_key_order": ["h", "k", "omega", "logh"],
        "family_nonzero_raw_coefficients": counts, "coefficient_alias_count": len(aliases),
        "literal_proportionality_unique_columns": len(normal),
        "aliases_format": "[family_index,state_key,normalized_original_column_id,rational_scale]",
        "all_aliases": aliases, "normalized_original_sha256": normal_hashes,
        "response_columns_precede_normalized_originals": R_COUNT,
        "global_normal_column_index": str(R_COUNT) + " + normalized_original_column_id",
        "same_eight_reference_Gamma_m0_and_Gamma_m2_kept": True,
        "reference_inverse_sha256": sha(canonical(reference["inverse"])),
        "reference_static_root_sha256": [ring.digest(v) for v in references],
        "N_representatives_changed_only_mod_W_and_normal_generators_only_mod_R": True,
    }
    proof["normal_presentation"] = report["normal_presentation"]
    report["phase"] = "new_complete_pure_function_kernel"
    decision, proof["complete_word_matrix"] = whole_pure_matrix(ring, controls + normal, args, budget, report)
    proof["inputs"] = report["inputs"]
    proof["source_hashes"] = report["source_hashes"]
    raw = canonical(proof)
    if len(raw) > args.max_certificate_bytes:
        raise literal.Limit("in-memory complete proof byte ceiling")
    budget.check()
    report["decision"] = decision
    report["reproducible_in_memory_proof"] = {"bytes": len(raw), "sha256": sha(raw), "persisted": False}
    report.update(completion="complete", phase="complete_pure_minus4_image_decided",
        exact_integer_operations=budget.operations, maximum_integer_bits=budget.maximum_bits,
        mixed_responses_compiled=0, old_response_roots_reconstructed=0,
        old_forcing_or_W_or_3974_producer_recompiled=False,
        new_profile_evaluations=0, positivity_LP_or_translation_head_computed=False,
        main_research_goal_complete=False)


def toy_only(args):
    """Only the newly retargeted cache partition and complete matrix interface."""
    checks=[]
    def record(name,truth):
        if not truth:raise AssertionError("new artificial check failed: "+name)
        checks.append({"name":name,"passed":True})
    def row(dw,weight):
        return {"geometry_derivative_weight":dw,
            "geometry_key":[weight-dw,0,0,dw,0,0,0,0,0,0]}
    record("old saved projection eligibility distinguishes N0 and N2 at third weight minus3",
        not archived_request(row(0,-3)) and archived_request(row(2,-3))
        and archived_request(row(0,-2)) and not archived_request(row(2,-4)))
    ring=colored.ColoredRing(exact.Limits(seconds=30,nodes=20000,atoms=5000,
        terms=10000,rewrites=20000,memory_mib=512,rational_bits=2048))
    q=ring.color("q");x=ring.monomial((1,()))
    u,v,w=q**2*q.D().D()**2,q.D()**4,x*q*q.D()*q.D().D()**2
    budget=literal.Budget(30,512,2048)
    decision,proof=whole_pure_matrix(ring,[2*u,3*u,v,u+v,w],args,budget,{},r_count=3)
    record("variable-size complete response block gives exact new pure quotient and all coordinates",
        decision["pure_response_rank"]==2 and decision["complete_pure_U_rank"]==3
        and decision["nonmember_dual"]["target_global_column"]==4
        and decision["nonmember_dual"]["values_on_all_old_R_and_target"]==["0","0","0","1"]
        and len(proof["coordinates"])==5)
    decision,proof=whole_pure_matrix(ring,[2*u,3*u,v,u+v,2*u-3*v],args,budget,{},r_count=3)
    record("retargeted complete membership branch has no spurious new direction",
        decision["pure_U_minus4_equals_pure_R_minus4"] and decision["pure_quotient_dimension"]==0
        and all(r["transported_complete_word_sum_exact_zero"] for r in proof["relations"]))
    matrix={0:[{} for _ in range(8)],2:[{} for _ in range(8)]}
    matrix[2][7][((0,0,0,0),(2,0))]=F(3)
    nrows=[{"geometry_derivative_weight":0,"third_weight":-4,"root":"toy",
        "state":(-4,2,0,0),"velocity":(0,0),"factor":F(1),"input_sha256":"toy"},
        {"geometry_derivative_weight":0,"third_weight":-4,"root":"toy:reference",
        "state":ZERO,"velocity":(0,0),"factor":F(-1),"input_sha256":"toy"}]
    out={i:{} for i in range(3)}
    subtract_responses(out,2,nrows,0,matrix,2,{(7,"toy"):u})
    record("minus4 contraction keeps the fixed reference subtraction and correct target weight",
        out[2][(-4,2,0,0)].terms==(-3*u).terms and out[2][ZERO].terms==(3*u).terms)
    return {"all_passed":True,"checks":checks,"count":len(checks),
        "real_old_inputs_loaded":False,"old_minus6_artificial_suite_repeated":False,
        "research_projections_or_responses_computed":False}



def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only", action="store_true")
    parser.add_argument("--output", type=Path, help="ephemeral runner summary only; do not publish payload")
    for flag, which in (("factor", "factors"), ("static", "static"), ("acceleration", "acceleration")):
        parser.add_argument("--" + flag + "-directory", type=Path,
                            default=TOPIC / "notes" / head.INPUTS[which]["directory"])
    parser.add_argument("--cache-directory", type=Path,
                        default=TOPIC / "notes" / "actions-43665345551-1-character_head_minus2")
    parser.add_argument("--R4-directory", type=Path,
                        default=TOPIC / "notes" / "actions-43654534244-1-g_translation_successor")
    parser.add_argument("--max-seconds", type=float, default=240)
    parser.add_argument("--memory-mib", type=int, default=1024)
    parser.add_argument("--integer-bits", type=int, default=8192)
    parser.add_argument("--max-terms", type=int, default=150000)
    parser.add_argument("--max-IBP-calls", type=int, default=600000)
    parser.add_argument("--max-cache-entries", type=int, default=300000)
    parser.add_argument("--max-summary-bytes", type=int, default=95000)
    parser.add_argument("--max-certificate-bytes", type=int, default=8000000)
    args = parser.parse_args()
    if (min(args.max_seconds, args.memory_mib, args.integer_bits, args.max_terms,
            args.max_IBP_calls, args.max_cache_entries, args.max_certificate_bytes) <= 0
        or not 20000 <= args.max_summary_bytes < 100000):
        parser.error("positive budgets and a 20KB to under-100KB summary are required")
    if not args.toy_only and not (os.environ.get("GITHUB_ACTIONS") == "true"
                                  and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY):
        parser.error("actual research runs only in this public repository's GitHub Actions")
    started = time.monotonic()
    report = {"schema": SCHEMA, "completion": "started", "phase": "source_binding",
        "github_repository": os.environ.get("GITHUB_REPOSITORY"),
        "github_run_id": os.environ.get("GITHUB_RUN_ID"), "github_sha": os.environ.get("GITHUB_SHA"),
        "inputs": {}, "target_weight": WEIGHT, "only_pure_mode": -4,
        "recomputable_payload_publication_permitted": False}
    code = 0
    try:
        report["source_hashes"] = source_identity()
        if args.toy_only:
            report["development"] = toy_only(args)
            report.update(completion="complete", phase="new_artificial_interfaces_only")
        else:
            actual(args, report)
    except (literal.Limit, formal.CompilationBudgetExceeded, MemoryError) as error:
        report.update(completion="resource_limit", error=str(error),
            complete_fourteen_family_pure_image=False, partial_is_not_a_complete_image_verdict=True)
        code = 2
    except Exception as error:
        report.update(completion="implementation_check_failed",
            error={"type": type(error).__name__, "message": str(error)},
            complete_fourteen_family_pure_image=False)
        code = 1
    report["elapsed_seconds"] = time.monotonic() - started
    report["peak_rss_mib"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
    # Keep direct references to the full mathematical rows before compacting
    # the temporary summary.  The bounded publisher does not retain payloads;
    # every new coordinate and alias must remain readable in the job stdout.
    display_coordinates = report.get("decision", {}).get("complete_normalized_column_coordinates", [])
    display_aliases = report.get("normal_presentation", {}).get("all_aliases", [])
    display_hashes = report.get("normal_presentation", {}).get("normalized_original_sha256", [])
    body = canonical(report) + b"\n"
    if len(body) > args.max_summary_bytes:
        # The verdict and a separating original witness remain observable.  A
        # large complete coordinate table is reproducible by this exact run;
        # neither a hidden payload nor a misleading incomplete verdict is used.
        original_bytes, original_sha = len(body), sha(body)
        presentation = report.get("normal_presentation")
        if presentation is not None:
            for key in ("all_aliases", "normalized_original_sha256"):
                value = presentation.pop(key, None)
                if value is not None:
                    presentation[key + "_summary"] = {"count": len(value), "sha256": sha(canonical(value))}
        decision = report.get("decision")
        if decision is not None:
            value = decision.pop("complete_normalized_column_coordinates", None)
            if value is not None:
                decision["complete_coordinates_summary"] = {"rows": len(value), "sha256": sha(canonical(value)),
                    "all_rows_verified_in_this_run": True}
        report["compact_summary"] = {"full_bytes": original_bytes, "full_sha256": original_sha,
            "no_payload_persisted": True, "exact_rank_verdict_and_nonmember_witness_retained": True}
        body = canonical(report) + b"\n"
    if len(body) > args.max_summary_bytes:
        raise ValueError("bounded verdict summary still exceeds the declared byte cap")
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(body)
    if args.toy_only:
        print("DEVELOPMENT_RESULT " + json.dumps(report.get("development", {}),
              sort_keys=True, separators=(",", ":")), flush=True)
    elif report.get("decision", {}).get("complete_fourteen_family_pure_image"):
        decision = report["decision"]
        key_result = {k: v for k, v in decision.items()
                      if k not in ("complete_normalized_column_coordinates", "old_response_coordinates")}
        key_result["weight"] = WEIGHT
        key_result["old_response_order"] = list(R_KEEP)
        key_result["family_order"] = list(head.FAMILIES)
        print("MATHEMATICAL_RESULT " + json.dumps(key_result, sort_keys=True, separators=(",", ":")), flush=True)
        aliases_by_column = {}
        for family, state, column, scale in display_aliases:
            aliases_by_column.setdefault(column, []).append([family, state, scale])
        for i, coordinates in enumerate(display_coordinates):
            row = {"normalized_original_column": i, "global_column": R_COUNT+i,
                "original_sha256": display_hashes[i],
                "exact_coordinates_in_independent_global_original_columns": coordinates,
                "all_family_aliases": aliases_by_column.get(i, [])}
            print("MATHEMATICAL_COLUMN " + json.dumps(row, sort_keys=True, separators=(",", ":")), flush=True)
        print("OLD_RESPONSE_PURE_COORDINATES " + json.dumps(decision["old_response_coordinates"],
              separators=(",", ":")), flush=True)
        print("CERTIFICATE_METADATA " + json.dumps(report["reproducible_in_memory_proof"],
              sort_keys=True, separators=(",", ":")), flush=True)
    print("EXECUTION_STATUS " + json.dumps({k: report[k] for k in (
        "completion", "phase", "error", "progress", "elapsed_seconds", "peak_rss_mib",
        "planned_new_pure_contractions", "completed_new_pure_contractions",
        "exact_integer_operations", "maximum_integer_bits") if k in report},
        sort_keys=True, separators=(",", ":")), flush=True)
    print("REPORT_METADATA " + json.dumps({"summary_bytes": len(body), "summary_sha256": sha(body),
        "source": report.get("source_hashes", {}).get("driver"),
        "payload_publication_permitted": False}, sort_keys=True), flush=True)
    raise SystemExit(code)


if __name__ == "__main__":
    main()
