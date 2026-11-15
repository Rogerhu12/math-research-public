#!/usr/bin/env python3
"""R281: exact rational RP1 phase covers for existing continuous pair gates.

Two closed charts [-1,1] cover the whole phase circle. Each accepted interval
uses exact Sturm root counting, not sampling, for one of distance, moving-end,
fixed-end or joint-end positivity. The original full-circle alternatives stay
available. A finite resource failure is unresolved, never geometric rejection.
All certificate arithmetic runs only in the named public repository's Actions.
"""
from __future__ import annotations

import argparse
from collections import deque
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import os
from pathlib import Path

SCHEMA = "R281-exact-rational-two-chart-phase-cover-v1"
R280_NAME = "geometry_20261115_joint_phase_normal_balls.py"
R280_SHA256 = "c5548f28bfe56a283403a7d16e1879c1c1243d0a0bc80761586fe50e1aec1466"
R62_NAME = "root_mixed_phase_normal_balls.py"
R62_SHA256 = "ecea0ef58aa5755270807596da5512552ac52fab27e90492fcf85fab095716c6"
GATE_ORDER = ("distance", "moving", "fixed", "joint")
PROOF = "R281-exact-rational-phase-disjunction-and-finite-cover.md"


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Run only in Rogerhu12/math-research-public Actions")


def load_sources():
    here = Path(__file__).resolve().parent
    for name, expected in ((R280_NAME, R280_SHA256), (R62_NAME, R62_SHA256)):
        if sha((here/name).read_bytes()) != expected:
            raise ValueError("A frozen phase-certificate source differs: " + name)
    spec = importlib.util.spec_from_file_location("_r281_r280", here/R280_NAME)
    if spec is None or spec.loader is None:
        raise RuntimeError("Cannot load the frozen R280 entry")
    previous = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(previous)
    return previous, previous.load_kernel()


def pad_four(poly):
    poly = [F(value) for value in poly]
    if not poly or len(poly) > 5:
        raise ValueError("A degree-at-most-four polynomial is required")
    return poly + [F(0)] * (5-len(poly))


def value_at(poly, x):
    result = F(0)
    for coefficient in reversed(poly):
        result = result*x + coefficient
    return result


def catalog_for(row, base, kernel):
    original = base["original_R62_record"]
    A, B, C = map(F, original["distance_coefficients"])
    tau = kernel.rational(row["tau"])
    e = (kernel.rational(row["moving_position_radius"])
         + kernel.rational(row["fixed_position_radius"]))
    U = [F(1), F(0), F(1)]
    V = [A-2*B, -4*C, A+2*B]
    distance = kernel.add(kernel.mul(U, V),
                         kernel.scaled(kernel.mul(U, U), -(2*tau+e)**2))
    endpoints = {item["endpoint"]: item for item in original["endpoints"]}
    polynomials = {
        "distance": pad_four(distance),
        "moving": pad_four(endpoints["moving"]["quartic_ascending_coefficients"]),
        "fixed": pad_four(endpoints["fixed"]["quartic_ascending_coefficients"]),
        "joint": pad_four(base["joint_endpoint_certificate"]["quartic_ascending_coefficients"]),
    }
    existing_t_sturm = {
        "moving": endpoints["moving"]["sturm"],
        "fixed": endpoints["fixed"]["sturm"],
        "joint": base["joint_endpoint_certificate"]["sturm"],
    }
    catalog = {}
    for chart in ("t", "u"):
        entries = {}
        for gate in GATE_ORDER:
            # Homogenize to degree four before reversing. Do not reverse a
            # trimmed polynomial: that would lose the phase-pi value at u=0.
            poly = polynomials[gate] if chart == "t" else list(reversed(polynomials[gate]))
            record = (existing_t_sturm[gate] if chart == "t" and gate in existing_t_sturm
                      else kernel.sturm(kernel.trim(poly)))
            entries[gate] = {
                "ascending_coefficients_padded_to_degree_four": [str(v) for v in poly],
                "sturm": record,
            }
        catalog[chart] = entries
    return catalog


def strict_interval(poly, sequence, a, b, kernel):
    if not a <= b:
        raise ValueError("An ordered closed rational interval is required")
    left, right = value_at(poly, a), value_at(poly, b)
    record = {
        "left_value": str(left), "right_value": str(right),
        "closed_interval": [str(a), str(b)],
        "strict_positive": False,
        "left_variations": None, "right_variations": None,
        "distinct_roots_in_open_interval": None,
    }
    if left <= 0 or right <= 0:
        record["reason"] = "a_closed_endpoint_is_not_strictly_positive"
        return record
    left_signs = [kernel.sign(value_at(item, a)) for item in sequence]
    right_signs = [kernel.sign(value_at(item, b)) for item in sequence]
    va, vb = kernel.variations(left_signs), kernel.variations(right_signs)
    count = va-vb
    if count < 0:
        raise AssertionError("Invalid exact Sturm variation order")
    record.update(left_variations=va, right_variations=vb,
                  distinct_roots_in_open_interval=count,
                  strict_positive=count == 0,
                  reason=("strict_endpoints_and_no_interior_root" if count == 0
                          else "an_interior_root_prevents_strict_positivity"))
    return record


def phase_cover(catalog, max_depth, max_cells, kernel):
    prepared = {
        chart: {
            gate: (
                [F(x) for x in entry["ascending_coefficients_padded_to_degree_four"]],
                [[F(x) for x in polynomial] for polynomial in entry["sturm"]["sequence"]],
            )
            for gate, entry in entries.items()
        }
        for chart, entries in catalog.items()
    }
    queue = deque((chart, "", F(-1), F(1), 0) for chart in ("t", "u"))
    leaves, splits = [], []
    processed = 0
    maximum_depth_seen = 0
    while queue:
        if processed >= max_cells:
            for chart, path, a, b, depth in queue:
                leaves.append(dict(chart=chart, path=path, depth=depth,
                    closed_interval=[str(a), str(b)], certified=False,
                    selected_gate=None, exact_gate_tests=None,
                    reason="cell_budget_exhausted_before_testing"))
            queue.clear()
            break
        chart, path, a, b, depth = queue.popleft()
        processed += 1
        maximum_depth_seen = max(maximum_depth_seen, depth)
        tests = {gate: strict_interval(*prepared[chart][gate], a, b, kernel)
                 for gate in GATE_ORDER}
        passing = [gate for gate in GATE_ORDER if tests[gate]["strict_positive"]]
        if passing:
            leaves.append(dict(chart=chart, path=path, depth=depth,
                closed_interval=[str(a), str(b)], certified=True,
                selected_gate=passing[0], passing_gates=passing,
                exact_gate_tests=tests,
                reason="one_original_geometric_alternative_holds_on_the_entire_closed_interval"))
        elif depth >= max_depth:
            leaves.append(dict(chart=chart, path=path, depth=depth,
                closed_interval=[str(a), str(b)], certified=False,
                selected_gate=None, exact_gate_tests=tests,
                reason="maximum_dyadic_depth_reached"))
        else:
            midpoint = (a+b)/2
            splits.append(dict(chart=chart, path=path, depth=depth,
                closed_interval=[str(a), str(b)], midpoint=str(midpoint),
                exact_gate_tests=tests, child_paths=[path+"0", path+"1"]))
            queue.append((chart, path+"0", a, midpoint, depth+1))
            queue.append((chart, path+"1", midpoint, b, depth+1))
    unresolved = [leaf for leaf in leaves if not leaf["certified"]]
    return {
        "performed": True,
        "complete_strict_phase_cover": not unresolved,
        "chart_roots": {"t": ["-1", "1"], "u": ["-1", "1"]},
        "closed_chart_overlap": "t=u=1 and t=u=-1; overlap is deliberately covered twice",
        "processed_cells": processed,
        "split_cells": len(splits),
        "terminal_leaves": len(leaves),
        "certified_leaves": len(leaves)-len(unresolved),
        "unresolved_leaves": len(unresolved),
        "maximum_processed_depth": maximum_depth_seen,
        "max_depth_budget": max_depth, "max_cells_budget": max_cells,
        "complete_terminal_partition": leaves,
        "complete_split_records": splits,
        "unresolved_means_geometric_failure": False,
        "phase_sampling_used": False,
    }


def evaluate_case(row, sqrt_bits, max_depth, max_cells, previous, kernel):
    base = previous.evaluate_joint(row, sqrt_bits, kernel)
    original = base["original_R62_record"]
    legacy = base["all_phase_distance_or_no_double_normal_pass"]
    legacy_gates = {
        "distance": original["all_phase_continuous_distance_pass"],
        "moving": original["endpoints"][0]["all_phase_non_normal_pass"],
        "fixed": original["endpoints"][1]["all_phase_non_normal_pass"],
        "joint": base["joint_endpoint_pass"],
    }
    if legacy != any(legacy_gates.values()):
        raise AssertionError("The preserved original full-circle OR differs")
    if legacy:
        catalog = None
        cover = {
            "performed": False,
            "complete_strict_phase_cover": False,
            "reason": "already_paid_by_an_original_full_circle_alternative",
            "processed_cells": 0, "split_cells": 0, "terminal_leaves": 0,
            "certified_leaves": 0, "unresolved_leaves": 0,
            "maximum_processed_depth": 0,
            "complete_terminal_partition": [], "complete_split_records": [],
            "unresolved_means_geometric_failure": False,
            "phase_sampling_used": False,
        }
    else:
        catalog = catalog_for(row, base, kernel)
        cover = phase_cover(catalog, max_depth, max_cells, kernel)
    passed = legacy or cover["complete_strict_phase_cover"]
    return {
        "name": row.get("name"), "exact_input": row,
        "complete_original_R280_record": base,
        "legacy_full_circle_alternatives": legacy_gates,
        "legacy_full_circle_certificate_pass": legacy,
        "polynomial_catalog": catalog,
        "phase_cover": cover,
        "all_phase_distance_or_no_double_normal_pass": passed,
        "new_phase_cover_succeeds_where_all_full_circle_alternatives_fail": (
            not legacy and cover["complete_strict_phase_cover"]),
        "normal_chord_inequality_alone_used_to_claim_embedding": False,
        "continuous_ball_hypotheses_certified_here": False,
        "complete_spatial_pair_cover_certified_here": False,
        "full_surface_certified": False, "actual_reach_certified": False,
    }


def reject_nonfinite_literal(value):
    raise ValueError("Nonstandard nonfinite JSON literal: " + value)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--sqrt-bits", type=int, default=128)
    parser.add_argument("--max-depth", type=int, default=16)
    parser.add_argument("--max-cells", type=int, default=8192)
    args = parser.parse_args()
    require_actions()
    if args.out.exists():
        raise ValueError("Use a fresh output file")
    if not 16 <= args.sqrt_bits <= 4096 or args.max_depth < 0 or args.max_cells < 2:
        raise ValueError("Use 16..4096 root bits, nonnegative depth and at least two cells")
    raw = args.input.read_bytes()
    incoming = json.loads(raw, parse_constant=reject_nonfinite_literal)
    if (not isinstance(incoming, dict) or not isinstance(incoming.get("cases"), list)
            or not incoming["cases"] or not all(isinstance(row, dict) for row in incoming["cases"])):
        raise ValueError("Use a nonempty complete cases array")
    previous, kernel = load_sources()
    records = [evaluate_case(row, args.sqrt_bits, args.max_depth, args.max_cells, previous, kernel)
               for row in incoming["cases"]]
    source_sha = sha(Path(__file__).read_bytes())
    result = {
        "schema": SCHEMA, "proof": PROOF, "source_sha256": source_sha,
        "frozen_R280_source_sha256": R280_SHA256,
        "frozen_R62_source_sha256": R62_SHA256,
        "input_sha256": sha(raw), "input_bytes": len(raw),
        "sqrt_bits": args.sqrt_bits, "max_depth": args.max_depth, "max_cells": args.max_cells,
        "complete_case_count": len(records), "complete_records": records,
        "all_interval_arithmetic_and_Sturm_tests_exact_rational": True,
        "fixed_normal_budgets_use_original_upward_dyadic_square_roots": True,
        "two_chart_homogeneous_degree": 4,
        "old_single_endpoints_and_joint_retained_by_OR": True,
        "original_non_strict_full_circle_distance_certificate_retained": True,
        "finite_budget_failure_does_not_prove_geometric_failure": True,
        "phase_sampling_used": False, "new_field_generated": False,
        "original_metric_changed": False,
        "scientific_surface_or_native_solver_calls": 0,
        "full_surface_certified": False, "actual_reach_certified": False,
        "additional_solver_acceptance_gate_created": False,
        "output_policy": (
            "Runner-temporary exact conditional result only; publish source, recipe, "
            "run, output SHA and compact conclusion, not recomputable raw data."
        ),
    }
    encoded = (json.dumps(result, indent=2, allow_nan=False)+"\n").encode()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_bytes(encoded)
    print(json.dumps(dict(
        schema=SCHEMA, source_sha256=source_sha, input_sha256=sha(raw),
        output_sha256=sha(encoded), output_bytes=len(encoded), case_count=len(records),
        legacy_pass_count=sum(r["legacy_full_circle_certificate_pass"] for r in records),
        new_cover_pass_count=sum(r["new_phase_cover_succeeds_where_all_full_circle_alternatives_fail"]
                                 for r in records),
        conditional_pair_pass_count=sum(r["all_phase_distance_or_no_double_normal_pass"] for r in records),
        unresolved_case_count=sum(not r["all_phase_distance_or_no_double_normal_pass"] for r in records),
        full_surface_certified=False, actual_reach_certified=False
    ), allow_nan=False), flush=True)


if __name__ == "__main__":
    main()
