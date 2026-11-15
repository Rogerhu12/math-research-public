#!/usr/bin/env python3
"""Complete pure weight -6 image, consuming published original expressions.

Only the missing pure diagonal potential contractions and the new complete
fourteen-family pure word matrix are computed.  The 3974 producer, W, all
mixed roots/responses, old evaluations and old normal forms are not rerun.
Actual research is restricted to this public repository's GitHub Actions.
New recomputable payloads remain in memory; only bounded summaries and their
hashes may be emitted under the current root README section 15.
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
layer, old, static = head.layer, head.old, head.static
colored, exact, blocks, formal = head.colored, head.exact, head.blocks, head.formal
Field = head.Field
canonical, sha = head.canonical, head.sha
REPOSITORY, TOPIC = head.REPOSITORY, head.TOPIC
SCHEMA = "visible-flex-complete-pure-minus6-projection-v1"
WEIGHT = -6
ZERO = (0, 0, 0, 0)
R_KEEP = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 15, 16, 17)
ZERO_DRIVER = {"filename": "literature_character_head_zero.py", "bytes": 42361,
    "sha256": "337966b4fb9a417ed62d650cac87ffc4c41bedc9938e11c1520fe1136b53dee4"}
R_INPUT = {
    "run": "43655713308", "commit": "d21c87a4d9341369a3dee35598ed88fb666cb99d",
    "lane": "g_translation_successor", "schema": "visible-flex-G-translation-successor-original-v1",
    "main": {"filename": "G-seventh-translation.json", "bytes": 26745,
        "sha256": "f5e514164cede76ba91786833d455b4638a45a3ee82cd2b7cadbcd76ee18ff15"},
    "receipt": {"filename": "receipt.json", "bytes": 35234,
        "sha256": "d1a5b9d8aa03553dfcf45731cbbbbb7861fbcbb496e90fb960e723e1597c3389"},
    "artifact": {"filename": "G-seventh-translation-original-expressions.json.gz",
        "stored_bytes": 15427,
        "stored_sha256": "936a19bd60b49b236343cdea9466f8a2bbbfbf108b3163ffe6b25e99eb66a664",
        "raw_bytes": 80081,
        "raw_sha256": "cffc0109bccd0a2aeb4e6e23e400c2de94e0bde68c57b41f08df724cd37a9dcb"},
    "driver": {"filename": "literature_G_translation_successor.py", "bytes": 39670,
        "sha256": "a4583ea776facd4ec4d92a121fed2e79af8de20d57bffc5fa22e47a8026ef406"},
}
R_DEPENDENCIES_SHA = "e91fc2506262b7b9e5b0ddb19864a123e4a037acc3a8bf0f5bae6ea6d28d4b2e"


def source_identity():
    found = static.identity(zero.__file__)
    if found != ZERO_DRIVER:
        raise ValueError("frozen cache/geometry helper changed")
    value = zero.source_identity()
    value["frozen_zero_helper"] = value.pop("driver")
    value["driver"] = static.identity(__file__)
    return value


def check_pure(ring, value, degree=4, weight=None, grade=None):
    if any(d != (("q", degree),) for d in ring.color_degrees(value)):
        raise ValueError("a selected pure root contains another color or profile degree")
    if weight is not None:
        grade = grade or blocks.ScalingGrading(ring)
        if any(grade.monomial(m) != weight for m in value.terms):
            raise ValueError("selected root has the wrong true affine weight")


def subset_decode(ring, data, names, allowed_colors, report=None, label=None):
    """Decode only the reachable selected DAG, retaining every original hash.

    Unlike the old portable reader, this does not register unused mixed atoms.
    A primitive's children must precede that primitive in the published DAG.
    No renormalization or right-constant reset occurs during import.
    """
    names = sorted(set(names))
    atoms = data["profile_atoms"]
    roots, hashes = data["roots"], data["original_root_sha256"]
    if not set(names).issubset(roots) or not set(names).issubset(hashes):
        raise ValueError("missing selected original root/hash")
    needed, stack = set(), []

    def monomial(raw, ceiling):
        if not isinstance(raw, (tuple, list)) or len(raw) != 2:
            raise ValueError("portable monomial shape")
        power, indices = raw
        if (type(power) is not int or power < 0 or not isinstance(indices, (list, tuple))
            or any(type(i) is not int or not 0 <= i < ceiling for i in indices)
            or list(indices) != sorted(indices)):
            raise ValueError("portable monomial index/order")
        return power, tuple(indices)

    for name in names:
        for row in roots[name]:
            if not isinstance(row, (list, tuple)) or len(row) != 3:
                raise ValueError("portable root row")
            stack.extend(monomial(row[0], len(atoms))[1])
    while stack:
        i = stack.pop()
        if i in needed:
            continue
        needed.add(i)
        atom = atoms[i]
        if not isinstance(atom, (list, tuple)) or not atom:
            raise ValueError("portable atom shape")
        if atom[0] == "jet":
            if (len(atom) != 3 or atom[1] not in allowed_colors
                or type(atom[2]) is not int or atom[2] < 0):
                raise ValueError("selected DAG has an undeclared jet color/order")
        elif atom[0] == "int_right":
            if len(atom) != 2:
                raise ValueError("portable primitive shape")
            stack.extend(monomial(atom[1], i)[1])
        else:
            raise ValueError("portable atom kind")
        ring.limits.check()
    translated = {}
    for i in sorted(needed):
        atom = atoms[i]
        if atom[0] == "jet":
            translated[i] = ring.p.jet(atom[1], atom[2])[1][0]
        else:
            power, indices = monomial(atom[1], i)
            key = (power, tuple(sorted(translated[j] for j in indices)))
            if not ring.p.weight(key):
                raise ValueError("a right primitive must have positive profile degree")
            translated[i] = ring.p.primitive(key)[1][0]
    answer = {}
    for name in names:
        terms = {}
        for raw, numerator, denominator in roots[name]:
            if (type(numerator) is not int or type(denominator) is not int
                or denominator <= 0 or numerator == 0):
                raise ValueError("portable rational coefficient")
            power, indices = monomial(raw, len(atoms))
            key = (power, tuple(sorted(translated[i] for i in indices)))
            value = F(numerator, denominator)
            if key in terms or value.numerator != numerator or value.denominator != denominator:
                raise ValueError("duplicate or unreduced original coefficient")
            terms[key] = value
        answer[name] = exact.Expr(ring, terms)
        if ring.digest(answer[name]) != hashes[name]:
            raise ValueError("selected original root SHA changed: " + name)
    if report is not None:
        report.setdefault("selected_DAG_imports", []).append({
            "source": label, "selected_roots": len(names), "reachable_atoms": len(needed),
            "published_atoms": len(atoms), "all_selected_original_hashes_matched": True,
            "unused_mixed_atoms_registered": False,
            "selection_sha256": sha(canonical([[n, hashes[n]] for n in names])),
        })
    return answer


def bind_R(ring, directory, report):
    main, raw = literal.read_small(directory / R_INPUT["main"]["filename"], R_INPUT["main"])
    receipt, _ = literal.read_small(directory / "receipt.json", R_INPUT["receipt"])
    checkpoint = main.get("checkpoint") or {}
    metadata = checkpoint.get("portable_new_block_expression_export") or {}
    literal.verify_publication(receipt, main, raw, R_INPUT, metadata)
    upper = checkpoint.get("response_upper_bound") or {}
    dual = checkpoint.get("dual_certificate") or {}
    if (checkpoint.get("requested_order") != 7 or checkpoint.get("requested_weight") != WEIGHT
        or upper.get("original_columns") != 20
        or upper.get("proved_true_response_dimension_upper_bound") != 16
        or upper.get("retained_original_columns") != list(R_KEEP)
        or upper.get("verified_original_dependency_count") != 4
        or upper.get("verified_original_dependencies_sha256") != R_DEPENDENCIES_SHA
        or dual.get("modular_control_rank") != 16 or not dual.get("modular_pivot_determinant")
        or dual.get("rational_nonmembership_certified") is not True):
        raise ValueError("the published complete true R_-6 span/basis identity changed")
    data = literal.checked_gzip(directory / metadata["filename"], metadata)
    coverage = data.get("response_coverage") or {}
    if (data.get("schema") != R_INPUT["schema"] + "-original-expressions"
        or data.get("source_hashes") != main.get("source_hashes")
        or str(data.get("github_run_id")) != R_INPUT["run"]
        or data.get("github_sha") != R_INPUT["commit"]
        or data.get("content_scope") != "one-translation-target-and-complete-new-response-block"
        or data.get("all_compiled_original_columns_included") is not True
        or coverage.get("full_E8") is not True or coverage.get("all_W36") is not True
        or coverage.get("columns") != 20 or coverage.get("weight") != WEIGHT):
        raise ValueError("complete old response export scope/source changed")
    records = data.get("column_records") or []
    if len(records) != 20 or [r["index"] for r in records] != list(range(20)):
        raise ValueError("old twenty response column identities changed")
    selected = [records[i] for i in R_KEEP]
    roots = subset_decode(ring, data, [r["roots"]["-4"] for r in selected], {"q"}, report, "R144-pure")
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
    report["inputs"]["R6"] = {k: R_INPUT[k] for k in ("run", "commit", "lane", "main", "receipt", "artifact", "driver")}
    report["old_response_span"] = {"full_two_mode_dimension_already_proved": 16,
        "retained_old_columns": list(R_KEEP), "old_four_dependencies_sha256": R_DEPENDENCIES_SHA,
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
                (0, 2, 3, 0, 0, 0, 0, 1, 0, 0),
                (0, 2, 4, 0, 0, 0, 0, 1, 0, 0),
                (0, 2, 5, 0, 0, 0, 0, 1, 0, 0)):
                raise ValueError("undeclared logarithmic quotient representative")
            logarithms.append(row)
            continue
        selected.append(row)
    expected = {(0, -6): 2, (0, -5): 11, (0, -4): 13, (0, -3): 14,
                (2, -6): 27, (2, -5): 24, (2, -4): 19, (2, -3): 12}
    if Counter((r["geometry_derivative_weight"], zero.geometry_index(r["geometry_key"]))
               for r in selected) != Counter(expected) or len(logarithms) != 3:
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
    if counts != Counter({2: 103, 4: 197}) or Counter(r[0] for r in vrows) != Counter({2: 103, 4: 160}):
        raise ValueError("complete new pure v2/v4 support changed")
    return selected, logarithms, vrows


def diagonal_response(ring, tau, quadratic):
    """Exactly R78's -4 component; no mixed or slot response is compiled."""
    q = ring.color("q")
    return (ring.variation(tau, quadratic(q, q)) - 2 * quadratic(q, tau)) / 8


def restore_missing_factors(ring, grade, factors, cache_data, report):
    matrix = head.read_matrix(factors)
    selected, logarithms, vrows = select_factor_rows(factors, matrix)
    lookup = zero.old_projection_index(cache_data)
    old_names, new_names, descriptions = set(), set(), []
    for row in selected:
        weight = zero.geometry_index(row["geometry_key"])
        reuse = row["geometry_derivative_weight"] == 2 and weight == -3
        bound = lookup.get((row["root"], weight)) if reuse else None
        if reuse:
            if (bound is None or bound["original_sha256"] != factors["original_root_sha256"][row["root"]]
                or bound["geometry_key"] != row["geometry_key"] or bound["derivative_weight"] != 2):
                raise ValueError("the already-completed -3 input projection is not the same factor")
            old_names.add(bound["input_root"])
        else:
            new_names.add(row["root"])
        descriptions.append((row, weight, bound))
    if len([r for r in descriptions if r[2] is not None]) != 12 or len(new_names) != 110:
        raise ValueError("exact twelve reused / 110 new potential projection coverage changed")
    decoded = subset_decode(ring, factors, new_names | {r[3] for r in vrows},
                            {"a", "b", "c", "q"}, report, "new-pure-factors-only")
    archived = subset_decode(ring, cache_data, old_names, {"a", "b", "c"}, report, "old-twelve-projected-inputs")
    q, nrows, identities = ring.color("q"), [], []
    for row, weight, bound in descriptions:
        typed = archived[bound["input_root"]] if bound else decoded[row["root"]]
        if any(d != (("a", 1), ("b", 1), ("c", 1)) for d in ring.color_degrees(typed)):
            raise ValueError("typed N lost its exterior/inner slots")
        if bound and ring.digest(typed) != bound["sha256"]:
            raise ValueError("archived projected input original SHA changed")
        diagonal = ring.substitute(typed, {"a": q, "b": q, "c": q})
        value = diagonal if bound else grade.project(diagonal, weight)
        check_pure(ring, value, degree=3, weight=weight, grade=grade)
        state, jets = head.split_key(row["geometry_key"])
        signature = ring.digest(value)
        identities.append({"root": row["root"], "geometry_key": row["geometry_key"],
            "third_weight": weight, "unprojected_sha256": factors["original_root_sha256"][row["root"]],
            "saved_projection_root": bound["input_root"] if bound else None,
            "saved_projection_sha256": bound["sha256"] if bound else None,
            "pure_diagonal_sha256": signature, "pure_diagonal_terms": len(value.terms)})
        if not value.terms:
            continue
        base = {"root": row["root"] + "@" + str(weight), "third_weight": weight,
            "geometry_derivative_weight": row["geometry_derivative_weight"],
            "state": state, "velocity": jets[:2], "factor": F(1),
            "value": value, "input_sha256": signature}
        nrows.append(base)
        if row["geometry_derivative_weight"] == 0:
            # R190 cocycle: every nonzero-weight N0 representative is based at S*.
            # At S*=(1,1,1), each selected zero-log state monomial equals one.
            nrows.append({**base, "root": base["root"] + ":reference-subtraction",
                          "state": ZERO, "factor": F(-1)})
    groups = {2: {}, 4: {}}
    for dw, tag, state, name in vrows:
        field = groups[dw].setdefault(tag, {})
        if state in field:
            raise ValueError("duplicate selected v state")
        value = grade.project(decoded[name], WEIGHT)
        check_pure(ring, value, weight=WEIGHT, grade=grade)
        field[state] = value
    report["new_factor_work"] = {
        "new_potential_diagonal_projections": 110, "saved_projected_inputs_reused": 12,
        "selected_potential_records": len(selected), "nonzero_diagonals": sum(bool(r["pure_diagonal_terms"]) for r in identities),
        "zero_log_N0_reference_constants_retained": True,
        "discarded_log_records_are_W_valued_by_covariance_not_literal_zero": [r["root"] for r in logarithms],
        "new_v2_raw_projections": 103, "new_v4_beta_C_Q_raw_projections": 160,
        "old_A_H_recompiled": False, "input_projection_identities_sha256": sha(canonical(identities)),
        "mixed_profile_roots_decoded": 0, "old_3974_producer_recompiled": False,
    }
    return matrix, nrows, groups, identities


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
    if (len(data.get("family_records", [])) != 314 or len(rows) != 58
        or Counter(r["family"] for r in rows) != Counter({"A_hh": 16, "A_hk": 12, "A_kk": 9, "H1": 12, "H2": 9})
        or any(r["profile_weights"] != [WEIGHT] for r in rows)):
        raise ValueError("complete published weight -6 five-family support changed")
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
    if len(plan) > 205:
        raise ValueError("declared at-most-205 new pure contractions exceeded")
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


def reduce_column(vector, index, basis, budget):
    denominator = 1
    for value in vector.values():
        denominator = lcm(denominator, value.denominator)
        budget.check((denominator,))
    raw = {i: int(c * denominator) for i, c in vector.items()}
    raw, combination = literal.normalize_integer_pair(raw, {index: denominator})
    budget.check(raw.values())
    while raw and min(raw) in basis:
        raw, combination = literal.exact_reduce_step(raw, combination, basis, budget)
    return raw, combination


def square_solve(matrix, rhs, budget):
    n = len(matrix)
    if len(rhs) != n or any(len(row) != n for row in matrix):
        raise ValueError("square original pivot minor required")
    rows = [[F(a) for a in row] + [F(b)] for row, b in zip(matrix, rhs)]
    for j in range(n):
        pivot = next((i for i in range(j, n) if rows[i][j]), None)
        if pivot is None:
            raise AssertionError("selected independent word minor is singular")
        rows[j], rows[pivot] = rows[pivot], rows[j]
        amount = rows[j][j]
        rows[j] = [a / amount for a in rows[j]]
        for i in range(n):
            if i != j and rows[i][j]:
                amount = rows[i][j]
                rows[i] = [a - amount * b for a, b in zip(rows[i], rows[j])]
                budget.check(rows[i])
    answer = [row[-1] for row in rows]
    if any(sum((F(a)*b for a, b in zip(row, answer)), F(0)) != F(rhs[i]) for i, row in enumerate(matrix)):
        raise AssertionError("fresh exact dual matrix multiplication failed")
    return answer


def whole_pure_matrix(ring, columns, args, budget, report):
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
            if index >= 16 and first_nonmember is None:
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
        if index == 15:
            R_rank, R_pivots, R_independent = len(basis), sorted(basis), list(independent)
        report["progress"] = {"completed_pure_columns": index + 1, "total_columns": len(columns),
                              "current_true_word_rank": len(basis)}
        budget.check()
    if R_rank is None:
        raise ValueError("the sixteen complete old responses must precede normal columns")
    dual = None
    if first_nonmember is not None:
        target = first_nonmember["column"]
        selected_rows = sorted(R_pivots + [first_nonmember["pivot"]])
        selected_columns = R_independent + [target]
        transposed = [[vectors[i].get(row, F(0)) for row in selected_rows] for i in selected_columns]
        weights = square_solve(transposed, [F(i == target) for i in selected_columns], budget)
        functional = {row: c for row, c in zip(selected_rows, weights) if c}
        evaluated = [sum((c * vector.get(row, F(0)) for row, c in functional.items()), F(0))
                     for vector in vectors[:16] + [vectors[target]]]
        if evaluated != [F(0)] * 16 + [F(1)]:
            raise AssertionError("new pure quotient dual fails original response/target checks")
        dual = {"target_global_column": target, "values_on_old16_and_target": list(map(str, evaluated)),
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
        "pure_U_minus6_equals_pure_R_minus6": first_nonmember is None,
        "independent_global_columns": independent,
        "verified_original_transport_relations": len(relations),
        "relation_proof": "sum exact same-anchor R178 column identities; R179 makes the shared word kernel the true function kernel",
        "fresh_original_difference_normalization_repeated": False,
        "nonmember_dual": dual,
        "complete_normalized_column_coordinates": [literal.serial_fraction_row(v) for v in coordinates[16:]],
        "old_response_coordinates": [literal.serial_fraction_row(v) for v in coordinates[:16]],
        "pure_positive_character_at_minus6_excluded_by_response_lineality": first_nonmember is None,
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
    controls = bind_R(ring, args.R6_directory, report)
    _, factors = head.bind_input("factors", args.factor_directory, report)
    cache_main, cache_data, binding = literal.consume_bound(args.cache_directory, literal.HEAD)
    zero.check_cached_head(cache_main, cache_data)
    report["inputs"]["old_projection_cache"] = binding
    report["phase"] = "new_pure_diagonal_projections_and_missing_v_coefficients"
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
        "response_columns_precede_normalized_originals": 16,
        "global_normal_column_index": "16 + normalized_original_column_id",
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
    report.update(completion="complete", phase="complete_pure_minus6_image_decided",
        exact_integer_operations=budget.operations, maximum_integer_bits=budget.maximum_bits,
        mixed_responses_compiled=0, old_response_roots_reconstructed=0,
        old_forcing_or_W_or_3974_producer_recompiled=False,
        new_profile_evaluations=0, positivity_LP_or_translation_head_computed=False,
        main_research_goal_complete=False)


def toy_only(args):
    """Only artificial interfaces new in this consumer; no research input load."""
    checks = []
    def record(name, truth):
        if not truth:
            raise AssertionError("artificial check failed: " + name)
        checks.append({"name": name, "passed": True})

    ring = colored.ColoredRing(exact.Limits(seconds=30, nodes=20000, atoms=5000,
        terms=10000, rewrites=20000, memory_mib=512, rational_bits=2048))
    q, a, b, c = (ring.color(name) for name in ("q", "a", "b", "c"))
    x = ring.monomial((1, ()))
    value = q * (x * q.D().D() ** 2).I().I()
    package = old.serialize_expressions(ring, {"selected": value, "unused": ring.color("qbar").D()})
    unused = next(i for i, node in enumerate(package["profile_atoms"]) if node[:2] == ["jet", "qbar"])
    package["profile_atoms"][unused] = ["unused-unselected-not-decoded"]
    target = colored.ColoredRing(ring.limits)
    imported = subset_decode(target, package, ["selected"], {"q"})["selected"]
    record("selected transitive right-DAG retains original hash and skips unused mixed branch",
           target.digest(imported) == ring.digest(value)
           and all(node[0] != "jet" or node[1] == "q" for node in target.p.atoms))
    bad = json.loads(json.dumps(package))
    used_primitive = next(i for i, node in enumerate(bad["profile_atoms"]) if node[0] == "int_right")
    bad["profile_atoms"][used_primitive] = ["int_right", [0, [used_primitive]]]
    caught = False
    try:
        subset_decode(target, bad, ["selected"], {"q"})
    except ValueError:
        caught = True
    record("used forward or cyclic primitive is rejected before construction", caught)

    typed = a * b.D() * c.D() + x * a.D() * (b.D() * c.D()).I()
    third = colored.ThirdOperator(ring, typed)
    tau = ring.substitute(typed, {"a": q, "b": q, "c": q})
    quadratic = lambda u, v: u.D() * v.D() + (u.D().D() * v.D().D()).I()
    eq = quadratic(q, q)
    three_slots = third(eq, q, q) / 8 + third(q, q, eq) / 4 - quadratic(q, third(q, q, q)) / 4
    record("pure diagonal Frechet formula equals the full three-slot phase formula on an asymmetric exterior toy",
           not (diagonal_response(ring, tau, quadratic) - three_slots).terms)
    grade = blocks.ScalingGrading(ring)
    mixed_weights = typed + a * b * c
    diagonal_first = grade.project(ring.substitute(mixed_weights, {"a": q, "b": q, "c": q}), -2)
    project_first = ring.substitute(grade.project(mixed_weights, -2), {"a": q, "b": q, "c": q})
    record("simultaneous pure diagonal commutes with true weight projection", not (diagonal_first-project_first).terms)

    nrows = [{"geometry_derivative_weight": 0, "third_weight": -6, "root": "toy",
        "state": (-6, 2, 0, 0), "velocity": (0, 0), "factor": F(1), "input_sha256": "toy"},
        {"geometry_derivative_weight": 0, "third_weight": -6, "root": "toy:reference",
        "state": ZERO, "velocity": (0, 0), "factor": F(-1), "input_sha256": "toy"}]
    matrix = {0: [{} for _ in range(8)], 2: [{} for _ in range(8)]}
    matrix[2][7][((0, 0, 0, 0), (2, 0))] = F(3)
    fields = {i: {} for i in range(3)}
    response = q ** 4
    subtract_responses(fields, 2, nrows, 0, matrix, 2, {(7, "toy"): response})
    record("nonzero-weight N0 reference subtraction survives the full m2 contraction",
           fields[2][(-6, 2, 0, 0)].terms == (-3*response).terms
           and fields[2][ZERO].terms == (3*response).terms)
    failed = False
    try:
        subtract_responses({i: {} for i in range(3)}, 2, nrows, 0, matrix, 2, {})
    except ValueError:
        failed = True
    record("an incomplete new response cache is rejected, never treated as zero", failed)

    budget = literal.Budget(30, 512, 2048)
    basis = {}
    original = [{0: F(2), 1: F(4)}, {0: F(3), 1: F(6)}, {1: F(5)}]
    independent = []
    relation = None
    for i, vector in enumerate(original):
        reduced, combination = reduce_column(vector, i, basis, budget)
        if reduced:
            basis[min(reduced)] = {"vector": reduced, "combination": combination}
            independent.append(i)
        else:
            relation = combination
    fresh = {}
    for i, coefficient in relation.items():
        literal.add_fraction_row(fresh, original[i], F(coefficient))
    record("triangular exact columns distinguish a true dependency from a new quotient direction",
           independent == [0, 2] and not fresh)
    dual = square_solve([[F(2), F(4)], [F(0), F(5)]], [F(0), F(1)], budget)
    record("new quotient dual is checked on the original pivot matrix",
           dual == [F(-2, 5), F(1, 5)])
    u, v = q * q.D().D() ** 3, q.D() ** 2 * q.D().D() ** 2
    fake_columns = [2*u, 3*u] + [ring.number(0)]*14 + [u, v, u+v]
    decision, proof = whole_pure_matrix(ring, fake_columns, args, budget, {})
    record("complete artificial sixteen-response gate reports a new quotient with every coordinate checked",
           decision["pure_response_rank"] == 1 and decision["complete_pure_U_rank"] == 2
           and decision["nonmember_dual"]["target_global_column"] == 17
           and len(proof["coordinates"]) == 19
           and all(r["transported_complete_word_sum_exact_zero"] for r in proof["relations"]))
    return {"all_passed": True, "checks": checks, "count": len(checks),
        "real_old_inputs_loaded": False, "research_projections_or_responses_computed": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only", action="store_true")
    parser.add_argument("--output", type=Path, help="ephemeral runner summary only; do not publish payload")
    for flag, which in (("factor", "factors"), ("static", "static"), ("acceleration", "acceleration")):
        parser.add_argument("--" + flag + "-directory", type=Path,
                            default=TOPIC / "notes" / head.INPUTS[which]["directory"])
    parser.add_argument("--cache-directory", type=Path,
                        default=TOPIC / "notes" / "actions-43665345551-1-character_head_minus2")
    parser.add_argument("--R6-directory", type=Path,
                        default=TOPIC / "notes" / "actions-43655713308-1-g_translation_successor")
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
            row = {"normalized_original_column": i, "global_column": 16+i,
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
