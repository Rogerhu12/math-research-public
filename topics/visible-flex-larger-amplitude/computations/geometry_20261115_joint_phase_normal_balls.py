#!/usr/bin/env python3
"""R280: a joint two-endpoint alternative for continuous all-phase pair covers.

This is conditional exact-rational certificate arithmetic, not a surface solver.
It preserves both frozen R62 single-endpoint alternatives and adds their joint
squared-cross-product alternative by OR. No complete field, enclosure, embedding,
curvature, reach, metric, held displacement or Euclidean gap is certified here.
All arithmetic execution is restricted to this repository's public Actions.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import importlib.util
import json
import os
from pathlib import Path

SCHEMA = "R280-joint-all-phase-continuous-normal-balls-v1"
KERNEL_NAME = "root_mixed_phase_normal_balls.py"
KERNEL_SHA256 = "ecea0ef58aa5755270807596da5512552ac52fab27e90492fcf85fab095716c6"
PROOF = "R280-joint-endpoint-all-phase-normal-balls-and-finite-cover.md"


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Run certificate arithmetic only in Rogerhu12/math-research-public Actions")


def load_kernel():
    path = Path(__file__).resolve().parent / KERNEL_NAME
    raw = path.read_bytes()
    if sha(raw) != KERNEL_SHA256:
        raise ValueError("The frozen R62 exact-arithmetic kernel differs")
    spec = importlib.util.spec_from_file_location("_r280_original_r62", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("Cannot load the frozen R62 source")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def evaluate_joint(row, sqrt_bits, kernel):
    """Add one certificate; never replace either old endpoint certificate."""
    original = kernel.evaluate(row, sqrt_bits)
    endpoints = original["endpoints"]
    if [entry["endpoint"] for entry in endpoints] != ["moving", "fixed"]:
        raise ValueError("The frozen endpoint order changed")

    polynomials = [
        [Fraction(value) for value in entry["quartic_ascending_coefficients"]]
        for entry in endpoints
    ]
    joint_poly = kernel.add(polynomials[0], polynomials[1])
    joint_pi = sum((Fraction(entry["phase_pi_margin"]) for entry in endpoints),
                   Fraction(0))
    leading = joint_poly[4] if len(joint_poly) == 5 else Fraction(0)
    if leading != joint_pi or len(joint_poly) > 5:
        raise AssertionError("Half-angle polynomial lost its phase-pi value")
    joint_sturm = kernel.sturm(joint_poly)
    joint_pass = (
        joint_pi > 0
        and joint_poly[0] > 0
        and joint_sturm["distinct_real_roots"] == 0
    )

    old_pass = original["all_phase_no_double_normal_pass"]
    if old_pass != any(entry["all_phase_non_normal_pass"] for entry in endpoints):
        raise AssertionError("The original single-endpoint OR changed")
    combined_pass = old_pass or joint_pass
    threshold_squares = [
        Fraction(entry["cross_threshold_upper"]) ** 2 for entry in endpoints
    ]
    return {
        "name": row.get("name"),
        "original_R62_record": original,
        "joint_endpoint_certificate": {
            "formula": (
                "(|n0|^2+|m0|^2)|d0(phi)|^2"
                "-(d0(phi).R_phi(n0))^2-(d0(phi).m0)^2"
                "-(e+eta_n*D)^2-(e+eta_m*D)^2"
            ),
            "same_frozen_position_and_normal_budgets": True,
            "squared_error_thresholds": [str(value) for value in threshold_squares],
            "joint_squared_error_threshold": str(sum(threshold_squares, Fraction(0))),
            "quartic_ascending_coefficients": [str(value) for value in joint_poly],
            "phase_zero_margin": str(joint_poly[0]),
            "phase_pi_margin": str(joint_pi),
            "sturm": joint_sturm,
            "strict_all_phase_joint_pass": joint_pass,
            "strict_boundary_equality_accepted": False,
            "all_phase_same_endpoint_required": False,
        },
        "original_single_endpoint_OR": old_pass,
        "joint_endpoint_pass": joint_pass,
        "all_phase_no_double_normal_pass": combined_pass,
        "new_joint_passes_where_both_old_endpoints_fail": joint_pass and not old_pass,
        "all_phase_distance_or_no_double_normal_pass": (
            original["all_phase_continuous_distance_pass"] or combined_pass
        ),
        "original_normal_chord_pass_retained_separately": (
            original["all_phase_continuous_normal_chord_pass"]
        ),
        "normal_chord_inequality_alone_used_to_claim_embedding": False,
        "phase_sampling_used": False,
        "complete_continuous_balls_are_required": True,
        "continuous_ball_hypotheses_certified_here": False,
        "complete_pair_cover_certified_here": False,
        "full_surface_certified": False,
        "actual_reach_certified": False,
    }


def reject_nonfinite_literal(value):
    raise ValueError("Nonstandard nonfinite JSON literal: " + value)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--sqrt-bits", type=int, default=128)
    args = parser.parse_args()
    require_actions()
    if args.out.exists():
        raise ValueError("Use a fresh output file")
    if not 16 <= args.sqrt_bits <= 4096:
        raise ValueError("Use the original explicit 16..4096-bit square-root budget")
    raw = args.input.read_bytes()
    incoming = json.loads(raw, parse_constant=reject_nonfinite_literal)
    if not isinstance(incoming, dict) or not isinstance(incoming.get("cases"), list):
        raise ValueError("Use the original input object with its complete cases list")
    if not incoming["cases"] or not all(isinstance(row, dict) for row in incoming["cases"]):
        raise ValueError("At least one complete conditional pair case is required")
    kernel = load_kernel()
    records = [evaluate_joint(row, args.sqrt_bits, kernel) for row in incoming["cases"]]
    source_sha = sha(Path(__file__).read_bytes())
    result = {
        "schema": SCHEMA,
        "proof": PROOF,
        "source_sha256": source_sha,
        "frozen_R62_source_sha256": KERNEL_SHA256,
        "input_sha256": sha(raw),
        "input_bytes": len(raw),
        "sqrt_bits": args.sqrt_bits,
        "complete_case_count": len(records),
        "complete_records": records,
        "combination": "old-moving OR old-fixed OR new-joint",
        "all_arithmetic_exact_rational_except_proved_upward_dyadic_roots": True,
        "complete_original_R62_records_retained": True,
        "phase_pi_checked_explicitly": True,
        "phase_sampling_used": False,
        "adaptive_precision_or_spatial_or_phase_refinement_performed": False,
        "finite_budget_failure_does_not_prove_geometric_failure": True,
        "scientific_surface_or_native_solver_calls": 0,
        "new_field_generated": False,
        "original_metric_changed": False,
        "full_surface_certified": False,
        "actual_reach_certified": False,
        "additional_solver_acceptance_gate_created": False,
        "output_policy": (
            "Runner-temporary conditional certificate only; publish source, input "
            "recipe, run identifier, output SHA and a compact conclusion under Rule15."
        ),
    }
    encoded = (json.dumps(result, indent=2, allow_nan=False) + "\n").encode()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_bytes(encoded)
    print(json.dumps({
        "schema": SCHEMA,
        "source_sha256": source_sha,
        "input_sha256": sha(raw),
        "output_sha256": sha(encoded),
        "output_bytes": len(encoded),
        "case_count": len(records),
        "old_endpoint_pass_count": sum(row["original_single_endpoint_OR"] for row in records),
        "joint_pass_count": sum(row["joint_endpoint_pass"] for row in records),
        "combined_pass_count": sum(row["all_phase_no_double_normal_pass"] for row in records),
        "strict_extension_case_count": sum(
            row["new_joint_passes_where_both_old_endpoints_fail"] for row in records),
        "full_surface_certified": False,
        "actual_reach_certified": False,
    }, allow_nan=False), flush=True)


if __name__ == "__main__":
    main()
