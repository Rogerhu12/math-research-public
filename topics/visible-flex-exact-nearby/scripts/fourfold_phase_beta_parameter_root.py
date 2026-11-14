#!/usr/bin/env python3
"""Uniform native-Arb objects and roots on an exact affine parameter box.

This does not integrate beta.  It prepares the same infinite primitive on a
closed rational parameter interval, initialized by the existing R57 uniform
simple-root certificate.  A parameter interval is never materialized to a
rounded coefficient file.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time
import numpy as np
from flint import arb, ctx
from fourfold_phase_beta_interval import BallTarget, NativeSpline, ball_record
from fourfold_phase_beta_bulk_interval import BulkTarget, exact_arb
from fourfold_phase_beta_bulk_box import FastBulkTarget
from fourfold_phase_beta_affine import load_definition


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def apply_parameter_box(target, object_path, definition, direction_path, center, half_width):
    half_width = Fraction(half_width)
    if not half_width > 0:
        raise ValueError("the parameter half width must be positive")
    lower, upper = center-half_width, center+half_width
    parameter = exact_arb(lower).union(exact_arb(upper))
    with np.load(direction_path, allow_pickle=False) as source:
        raw_direction = source["phase_direction_coefficients"].copy()
        mean_direction = source["alpha_direction"].copy()
    base = target.frozen["phase_coefficients"]
    if base.shape != raw_direction.shape or mean_direction.shape != target.frozen["alpha"].shape:
        raise ValueError("affine origin and direction have different dimensions")
    coefficients = np.empty(base.shape, object)
    for index in np.ndindex(base.shape):
        coefficients[index] = arb(float(base[index]))+parameter*arb(float(raw_direction[index]))
    target.raw = NativeSpline([arb(float(x)) for x in target.frozen["phase_knots"]],
                             coefficients, 5, converted=True)
    target.alpha = [arb(float(a))+parameter*arb(float(v))
                    for a, v in zip(target.frozen["alpha"], mean_direction)]
    target.parameter_definition = definition
    target.parameter_center_object_sha256 = sha(object_path)
    target.parameter_center = center
    target.parameter_half_width = half_width
    target.parameter_interval = lower, upper


class ParameterBallTarget(BallTarget):
    def __init__(self, object_path, half_width, nodes, angles):
        definition, origin, direction, center = load_definition(object_path)
        super().__init__(origin, nodes, angles)
        apply_parameter_box(self, object_path, definition, direction, center, half_width)


class ParameterBulkTarget(BulkTarget):
    def __init__(self, object_path, half_width, nodes, angles, *radii):
        definition, origin, direction, center = load_definition(object_path)
        super().__init__(origin, nodes, angles, *radii)
        apply_parameter_box(self, object_path, definition, direction, center, half_width)


class ParameterFastBulkTarget(FastBulkTarget):
    def __init__(self, object_path, half_width, nodes, angles, *radii):
        definition, origin, direction, center = load_definition(object_path)
        super().__init__(origin, nodes, angles, *radii)
        apply_parameter_box(self, object_path, definition, direction, center, half_width)


def provenance(target, object_path):
    here = Path(__file__).parent
    return {
        "center_object_path": str(object_path),
        "center_object_sha256": target.parameter_center_object_sha256,
        "origin_inputs_sha256": target.parameter_definition["origin_inputs"]["sha256"],
        "direction_sha256": target.parameter_definition["direction"]["sha256"],
        "exact_center_parameter": str(target.parameter_center),
        "exact_parameter_half_width": str(target.parameter_half_width),
        "exact_parameter_interval": [str(x) for x in target.parameter_interval],
        "source_sha256": sha(__file__),
        "dependency_sha256": {name: sha(here/name) for name in (
            "fourfold_phase_beta_interval.py",
            "fourfold_phase_beta_bulk_interval.py",
            "fourfold_phase_beta_bulk_box.py",
            "fourfold_phase_beta_affine.py")},
        "semantics": "one shared real affine parameter before fixed base weights, symmetry, and infinite R33 primitive"}


def certified_initial_root(target, certificate_path):
    certificate = json.loads(Path(certificate_path).read_text())
    if (certificate.get("kind") != "directed_common_simple_root_for_exact_real_affine_R57_family"
            or not certificate.get("proved")
            or not all(certificate["conditions"].values())
            or certificate["origin_inputs_sha256"] != target.parameter_definition["origin_inputs"]["sha256"]
            or certificate["frozen_direction_sha256"] != target.parameter_definition["direction"]["sha256"]):
        raise ValueError("the common root certificate has a different family or an unpaid gate")
    allowed = [Fraction.from_float(float(x)) for x in certificate["exact_parameter_interval"]]
    if not allowed[0] <= target.parameter_interval[0] <= target.parameter_interval[1] <= allowed[1]:
        raise ValueError("the parameter box is outside the certified family")
    lower, upper = certificate["root_bracket"]
    return arb(float(lower)).union(arb(float(upper)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--center-object", type=Path, required=True)
    parser.add_argument("--half-width", type=Fraction, required=True)
    parser.add_argument("--common-root-certificate", type=Path, required=True)
    parser.add_argument("--quarter-nodes", type=int, default=256)
    parser.add_argument("--bits", type=int, default=160)
    parser.add_argument("--newton-steps", type=int, default=4)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    ctx.prec, ctx.cap = args.bits, 8
    started = time.monotonic()
    target = ParameterBallTarget(args.center_object, args.half_width,
                                 args.quarter_nodes, args.quarter_nodes)
    initial = certified_initial_root(target, args.common_root_certificate)
    budget = target.analytic_input_budget(initial, arb(".003"), arb(".32"), arb(".0025"))
    scale = exact_arb(Fraction(1, 4096))
    root, trace = target.refine_certified_root(initial, scale, budget, args.newton_steps)
    report = {
        "kind": "uniform_native_Arb_root_for_exact_affine_parameter_box",
        "proved": True, **provenance(target, args.center_object),
        "common_root_certificate_sha256": sha(args.common_root_certificate),
        "bits": args.bits, "quarter_nodes": args.quarter_nodes,
        "initial_root": ball_record(initial), "root": ball_record(root),
        "root_newton_trace": trace,
        "input_budget": {key: ([ball_record(x) for x in value]
            if isinstance(value, list) else ball_record(value)) for key, value in budget.items()},
        "wall_seconds": time.monotonic()-started,
        "justification": "each parameter already has its unique root in the initial bracket; every interval Newton intersection retains that root by the real mean value theorem",
        "limitations": [
            "This is a uniform root result only, not a beta integral or beta derivative bound",
            "The chosen parameter box has not been asserted to be the final KAM box",
            "Complex domains and the complete bulk/collar must still be verified on this same box"
        ]}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"root": root.str(35), "parameter": report["exact_parameter_interval"],
                      "wall_seconds": report["wall_seconds"]}), flush=True)


if __name__ == "__main__":
    main()
