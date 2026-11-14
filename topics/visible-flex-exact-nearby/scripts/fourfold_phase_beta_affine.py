#!/usr/bin/env python3
"""Actual beta for an exact R57 affine graph, without float materialization.

The saved direction is applied in Arb to each raw phase coefficient and mean
amplitude before multiplying by the fixed physical base powers. The original
frozen native collar and directed bulk engines remain unchanged.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time
import numpy as np
from flint import arb, acb, ctx
from fourfold_phase_beta_interval import BallTarget, NativeSpline, ball_record
from fourfold_phase_beta_bulk_interval import BulkTarget, exact_arb, real_interval
from fourfold_phase_beta_bulk_box import FastBulkTarget


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_definition(path):
    path = Path(path)
    definition = json.loads(path.read_text())
    if definition.get("kind") != "exact_affine_symmetric_infinite_R33_graph":
        raise ValueError("unsupported affine object definition")
    topic = Path(__file__).resolve().parents[1]
    origin = topic/definition["origin_inputs"]["path"]
    direction = topic/definition["direction"]["path"]
    if sha(origin) != definition["origin_inputs"]["sha256"] or sha(direction) != definition["direction"]["sha256"]:
        raise ValueError("frozen affine origin or direction hash mismatch")
    entry = definition["delta_fraction"]
    delta = Fraction(int(entry["numerator"]), int(entry["denominator"]))
    return definition, origin, direction, delta


def apply_affine(target, object_path, definition, direction_path, delta):
    with np.load(direction_path, allow_pickle=False) as saved:
        raw_direction = saved["phase_direction_coefficients"].copy()
        mean_direction = saved["alpha_direction"].copy()
    base = target.frozen["phase_coefficients"]
    if raw_direction.shape != base.shape or mean_direction.shape != target.frozen["alpha"].shape:
        raise ValueError("affine direction dimensions differ from the origin")
    parameter = exact_arb(delta)
    coefficients = np.empty(base.shape, object)
    for index in np.ndindex(base.shape):
        coefficients[index] = arb(float(base[index]))+parameter*arb(float(raw_direction[index]))
    target.raw = NativeSpline([arb(float(x)) for x in target.frozen["phase_knots"]], coefficients, 5, converted=True)
    target.alpha = [arb(float(a))+parameter*arb(float(v))
                    for a, v in zip(target.frozen["alpha"], mean_direction)]
    target.affine_definition = definition
    target.affine_object_sha256 = sha(object_path)
    target.affine_delta = delta


class AffineBallTarget(BallTarget):
    def __init__(self, object_path, nodes, angles):
        definition, origin, direction, delta = load_definition(object_path)
        super().__init__(origin, nodes, angles)
        apply_affine(self, object_path, definition, direction, delta)


class AffineBulkTarget(BulkTarget):
    def __init__(self, object_path, nodes, angles, *radii):
        definition, origin, direction, delta = load_definition(object_path)
        super().__init__(origin, nodes, angles, *radii)
        apply_affine(self, object_path, definition, direction, delta)


class AffineFastBulkTarget(FastBulkTarget):
    def __init__(self, object_path, nodes, angles, *radii):
        definition, origin, direction, delta = load_definition(object_path)
        super().__init__(origin, nodes, angles, *radii)
        apply_affine(self, object_path, definition, direction, delta)


def provenance(target, object_path):
    here = Path(__file__).parent
    return {"object_path": str(object_path), "object_sha256": target.affine_object_sha256,
        "origin_inputs_sha256": target.affine_definition["origin_inputs"]["sha256"],
        "direction_sha256": target.affine_definition["direction"]["sha256"],
        "exact_delta_fraction": str(target.affine_delta), "source_sha256": sha(__file__),
        "dependency_sha256": {name: sha(here/name) for name in
            ("fourfold_phase_beta_interval.py", "fourfold_phase_beta_bulk_interval.py", "fourfold_phase_beta_bulk_box.py")},
        "affine_arithmetic": "Arb encloses c0+exact_delta*v and alpha0+exact_delta*w before all fixed base weights"}


def run_collar(args):
    ctx.prec, ctx.cap = args.bits, args.precision
    started = time.monotonic()
    target = AffineBallTarget(args.object, args.quarter_nodes, args.angles)
    certificate = json.loads(args.root_certificate.read_text())
    if (not certificate.get("proved")
            or certificate["origin_inputs_sha256"] != target.affine_definition["origin_inputs"]["sha256"]
            or certificate["frozen_direction_sha256"] != target.affine_definition["direction"]["sha256"]
            or Fraction(certificate["exact_delta_fraction"]) != target.affine_delta):
        raise ValueError("root certificate belongs to a different exact affine graph")
    left, right = certificate["root_interval"]
    root = arb(float(left)).union(arb(float(right)))
    scale = exact_arb(Fraction(1, 4096))
    cut = (Fraction.from_float(float(certificate["root_center"]))-Fraction(1, 4096)
           if args.fixed_cut is None else Fraction(args.fixed_cut))
    for key, values in target.frozen.items():
        if key.endswith("_knots"):
            for x in values:
                if cut < abs(Fraction.from_float(float(x))) < Fraction.from_float(float(right)):
                    raise ValueError("physical affine collar crosses an exact scalar knot")
    budget = target.analytic_input_budget(root, arb(".003"), arb(".32"), arb(".0025"))
    root, trace = target.refine_certified_root(root, scale, budget, 3)
    eta = root-exact_arb(cut)
    R, sigma = arb(args.radial_radius), arb(args.sigma)
    if not 0 < eta < R:
        raise ValueError("affine collar does not lie in its complex disk")
    coefficients, diagnostics = target.root_density_taylor(root, scale, args.degree, budget)
    polynomial = sum((coefficients[n]*eta**(arb(n)-arb(3)/2)/(arb(n)-arb(3)/2)
                      for n in range(args.degree+1)), arb(0))
    report = {"kind": "exact_affine_directed_root_collar", "complete": False, **provenance(target, args.object),
        "root_certificate_sha256": sha(args.root_certificate), "root": ball_record(root), "root_newton_trace": trace,
        "fixed_cut": str(cut), "eta": ball_record(eta), "bits": args.bits, "quarter_nodes": args.quarter_nodes,
        "angles": args.angles, "degree": args.degree, "series_precision": args.precision,
        "coefficients": [ball_record(x) for x in coefficients], "coefficient_diagnostics": diagnostics,
        "polynomial_finite_part": ball_record(polynomial),
        "input_budget": {key: ([ball_record(x) for x in value] if isinstance(value, list) else ball_record(value))
                         for key, value in budget.items()},
        "limitations": ["This collar belongs to the exact affine point above, not its rounded export",
                        "Full beta, the full actual return-map phase, and the nonlinear family are not asserted"]}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    def save():
        report["wall_seconds"] = time.monotonic()-started
        args.out.write_text(json.dumps(report, indent=2)+"\n")
    save()
    print(json.dumps({"stage": "affine coefficients", "g0": coefficients[0].str(22), "g1": coefficients[1].str(22)}), flush=True)
    bound, domain = target.collar_domain_bound(root, scale, R, sigma, budget)
    tail = bound*eta**(arb(args.degree)-arb(1)/2)/((arb(args.degree)-arb(1)/2)*R**(args.degree+1)*(1-eta/R))
    angular_mean = 2*bound*(-sigma*args.angles).exp()/(1-(-sigma*args.angles).exp())
    angular = 2*angular_mean*eta**(-arb(3)/2)/(1-eta/R)
    value = polynomial+arb(0, (tail+angular).upper())
    report.update({"complete": True, "domain": domain, "radial_radius": ball_record(R), "sigma": ball_record(sigma),
        "radial_tail_error": ball_record(tail.upper()), "angular_error": ball_record(angular.upper()),
        "collar_integral": ball_record(value)})
    save()
    print(json.dumps({"stage": "complete affine collar", "integral": value.str(25)}), flush=True)


def run_bulk(args):
    ctx.prec, ctx.cap = args.bits, 4
    cls = AffineFastBulkTarget if args.engine == "box" else AffineBulkTarget
    target = cls(args.object, args.quarter_nodes, args.angles, arb(".003"), arb(".0025"), arb(".32"))
    collar = json.loads(args.collar.read_text())
    if not collar["complete"] or collar["object_sha256"] != target.affine_object_sha256:
        raise ValueError("affine bulk and complete collar have different exact objects")
    cut, waist = Fraction(collar["fixed_cut"]), Fraction(1, 1048576)
    knots = {Fraction(0), cut}
    for key, values in target.frozen.items():
        if key.endswith("_knots"):
            knots.update(q for q in (abs(Fraction.from_float(float(x))) for x in values) if 0 < q < cut)
    if not waist < sorted(knots)[1]:
        raise ValueError("affine waist crosses a scalar knot")
    knots.add(waist)
    points = sorted(knots)
    cells = [(a, b) for a, b in zip(points, points[1:]) if a >= waist]
    report = {"kind": "exact_affine_directed_phase_bulk", "complete": False, **provenance(target, args.object),
        "collar_sha256": sha(args.collar), "fixed_cut": str(cut), "waist_width": str(waist),
        "bits": args.bits, "quarter_nodes": args.quarter_nodes, "angles": args.angles, "sigma": args.sigma,
        "engine": args.engine, "radial_cells_total": len(cells), "start_cell": args.start_cell,
        "per_original_cell_tolerance": args.absolute_tolerance, "accepted_cells": [], "failed_cells": [],
        "subdivision_count": 0, "limitations": ["A partial exact affine cover is not a complete beta certificate"]}
    started = time.monotonic()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    def save():
        report["wall_seconds"] = time.monotonic()-started
        report["callback_evaluations"] = target.evaluations
        report["failed_analytic_evaluations"] = target.failed_analytic_evaluations
        args.out.write_text(json.dumps(report, indent=2)+"\n")
    if args.start_cell == 0:
        cap, bound = target.waist_cap(waist)
        report["waist_integral"], report["waist_density_bound"] = ball_record(cap), ball_record(bound)
        save()
    tolerance, sigma = arb(args.absolute_tolerance), arb(args.sigma)
    stop = len(cells) if args.max_cells is None else min(len(cells), args.start_cell+args.max_cells)
    for index in range(args.start_cell, stop):
        base_left, base_right = cells[index]
        target.set_cell(base_left, base_right)
        pending = [(base_left, base_right, 0)]
        while pending:
            left, right, depth = pending.pop()
            before, length = target.evaluations, exact_arb(right-left)
            local_tolerance = tolerance*length/exact_arb(base_right-base_left)
            try:
                bound, angular = target.angular_domain(left, right, sigma)
                if not length*angular < local_tolerance/2:
                    raise ValueError("full affine angular fee exceeds cell budget")
                whole = target.mean_callback(acb(real_interval(left, right)), False)
                direct = whole.real*length+arb(0, (length*angular).upper())
                if direct.is_finite() and direct.rad() < local_tolerance:
                    value, method = direct, "continuous_interval_range"
                else:
                    integral = acb.integral(target.mean_callback, acb(exact_arb(left)), acb(exact_arb(right)),
                        abs_tol=local_tolerance/2, rel_tol=arb("1e-10"), eval_limit=args.eval_limit,
                        deg_limit=32, depth_limit=20)
                    if not integral.is_finite() or not integral.real.rad() < local_tolerance/2:
                        raise ValueError("validated affine quadrature did not meet cell budget")
                    value, method = integral.real+arb(0, (length*angular).upper()), "Arb_validated_complex_integration"
                report["accepted_cells"].append({"index": index, "left": str(left), "right": str(right), "depth": depth,
                    "integral": ball_record(value), "method": method, "complex_angle_density_bound": ball_record(bound),
                    "angular_integral_error": ball_record((length*angular).upper()), "evaluations": target.evaluations-before})
                print(json.dumps({"stage": "affine cell", "index": index, "depth": depth,
                                  "integral": value.str(16)}), flush=True)
            except Exception as exc:
                if depth < args.cell_depth:
                    mid = (left+right)/2
                    pending.extend([(mid, right, depth+1), (left, mid, depth+1)])
                    report["subdivision_count"] += 1
                    report["latest_subdivision"] = {"index": index, "left": str(left), "right": str(right), "reason": repr(exc)}
                else:
                    report["failed_cells"].append({"index": index, "left": str(left), "right": str(right), "error": repr(exc)})
            save()
    report["complete"] = args.start_cell == 0 and stop == len(cells) and not report["failed_cells"] and "waist_integral" in report
    save()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="command", required=True)
    cp = sub.add_parser("collar")
    bp = sub.add_parser("bulk")
    for parser in (cp, bp):
        parser.add_argument("--object", type=Path, required=True)
        parser.add_argument("--out", type=Path, required=True)
        parser.add_argument("--bits", type=int, default=192 if parser is cp else 128)
        parser.add_argument("--quarter-nodes", type=int, default=512 if parser is cp else 256)
        parser.add_argument("--angles", type=int, default=2048 if parser is cp else 1024)
        parser.add_argument("--sigma", default=".02")
    cp.add_argument("--root-certificate", type=Path, required=True)
    cp.add_argument("--fixed-cut")
    cp.add_argument("--degree", type=int, default=24)
    cp.add_argument("--precision", type=int, default=72)
    cp.add_argument("--radial-radius", default=".0006")
    bp.add_argument("--collar", type=Path, required=True)
    bp.add_argument("--engine", choices=("box", "arb"), default="box")
    bp.add_argument("--absolute-tolerance", default=".0002")
    bp.add_argument("--eval-limit", type=int, default=64)
    bp.add_argument("--cell-depth", type=int, default=10)
    bp.add_argument("--start-cell", type=int, default=0)
    bp.add_argument("--max-cells", type=int)
    args = ap.parse_args()
    if args.command == "collar":
        run_collar(args)
    else:
        run_bulk(args)


if __name__ == "__main__":
    main()
