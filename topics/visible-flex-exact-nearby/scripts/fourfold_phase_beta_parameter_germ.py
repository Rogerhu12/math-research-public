#!/usr/bin/env python3
"""Preserve the affine parameter through complete scalar spline germs.

Origin and direction are differentiated as exact scalar polynomials first.
Only then is their affine combination enclosed. This avoids replacing one
shared parameter by independent interval errors at all B-spline controls.
The underlying family and all primitive/geometry formulas are unchanged.
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
from fourfold_phase_beta_interval import BallTarget, NativeSpline, ball_record, series_constant
from fourfold_phase_beta_bulk_interval import BulkTarget, exact_arb
from fourfold_phase_beta_bulk_box import FastBulkTarget
from fourfold_phase_beta_affine import load_definition
from fourfold_phase_beta_combine import stored_ball
from fourfold_phase_beta_parameter_root import certified_initial_root


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


class ParameterGermMixin:
    def initialize_parameter(self, object_path, half_width, definition, direction, center):
        half_width = Fraction(half_width)
        if not half_width > 0:
            raise ValueError("parameter half width must be positive")
        with np.load(direction, allow_pickle=False) as saved:
            raw = saved["phase_direction_coefficients"].copy()
            alpha = saved["alpha_direction"].copy()
        if raw.shape != self.frozen["phase_coefficients"].shape or alpha.shape != self.frozen["alpha"].shape:
            raise ValueError("origin and direction dimensions differ")
        self.raw_direction = NativeSpline(self.frozen["phase_knots"], raw, 5)
        self.alpha_direction = [arb(float(x)) for x in alpha]
        self.parameter_definition = definition
        self.parameter_center_object_sha256 = sha(object_path)
        self.parameter_center, self.parameter_half_width = center, half_width
        self.parameter_interval = center-half_width, center+half_width
        self.parameter_ball = exact_arb(self.parameter_interval[0]).union(exact_arb(self.parameter_interval[1]))

    def direction_scalars(self, center, direction):
        if isinstance(self, BulkTarget):
            plus = lambda sp: self.explicit_germ(sp, center, direction, 1)
            minus = lambda sp: self.explicit_germ(sp, center, direction, -1)
        else:
            plus = lambda sp: sp.germ(center, direction)
            minus = lambda sp: sp.germ(-acb(center), -acb(direction))
        bp, bm = plus(self.base), minus(self.base)
        vp, vm = plus(self.raw_direction), minus(self.raw_direction)
        beta, gamma = np.empty(self.modes, object), np.empty(self.modes, object)
        for j in range(self.modes):
            beta[j] = (vp[j, 0]*bp**3+vm[j, 0]*bm**3)/2
            gamma[j] = (vp[j, 1]*bp**2-vm[j, 1]*bm**2)/2
        radius, height = series_constant(0), series_constant(0)
        for weight, spline in zip(self.alpha_direction, self.means):
            radius += weight*(plus(spline)+minus(spline))/2
        for weight, spline in zip(self.alpha_direction, self.height_integrals[1:]):
            height += weight*(plus(spline)-minus(spline))/2
        return beta, gamma, radius, height

    def scalars(self, center, direction):
        origin = super().scalars(center, direction)
        derivative = self.direction_scalars(center, direction)
        result = []
        for value, change in zip(origin, derivative):
            if isinstance(value, np.ndarray):
                row = np.empty(value.shape, object)
                for index in np.ndindex(value.shape):
                    row[index] = value[index]+self.parameter_ball*change[index]
                result.append(row)
            else:
                result.append(value+self.parameter_ball*change)
        return tuple(result)


class ParameterGermBallTarget(ParameterGermMixin, BallTarget):
    def __init__(self, object_path, half_width, nodes, angles):
        definition, origin, direction, center = load_definition(object_path)
        super().__init__(origin, nodes, angles)
        self.initialize_parameter(object_path, half_width, definition, direction, center)


class ParameterGermBulkTarget(ParameterGermMixin, BulkTarget):
    def __init__(self, object_path, half_width, nodes, angles, *radii):
        definition, origin, direction, center = load_definition(object_path)
        super().__init__(origin, nodes, angles, *radii)
        self.initialize_parameter(object_path, half_width, definition, direction, center)


class ParameterGermFastBulkTarget(ParameterGermMixin, FastBulkTarget):
    def __init__(self, object_path, half_width, nodes, angles, *radii):
        definition, origin, direction, center = load_definition(object_path)
        super().__init__(origin, nodes, angles, *radii)
        self.initialize_parameter(object_path, half_width, definition, direction, center)


def provenance(target, object_path):
    here = Path(__file__).parent
    return {
        "center_object_path": str(object_path), "center_object_sha256": target.parameter_center_object_sha256,
        "origin_inputs_sha256": target.parameter_definition["origin_inputs"]["sha256"],
        "direction_sha256": target.parameter_definition["direction"]["sha256"],
        "exact_center_parameter": str(target.parameter_center),
        "exact_parameter_half_width": str(target.parameter_half_width),
        "exact_parameter_interval": [str(x) for x in target.parameter_interval],
        "source_sha256": sha(__file__),
        "dependency_sha256": {name: sha(here/name) for name in (
            "fourfold_phase_beta_interval.py", "fourfold_phase_beta_bulk_interval.py",
            "fourfold_phase_beta_bulk_box.py", "fourfold_phase_beta_affine.py",
            "fourfold_phase_beta_combine.py", "fourfold_phase_beta_parameter_root.py")},
        "semantics": "exact origin and direction scalar germs first; one shared real affine parameter applied afterwards"
    }


def run_root(args):
    ctx.prec, ctx.cap = args.bits, 8
    started = time.monotonic()
    target = ParameterGermBallTarget(args.center_object, args.half_width, args.quarter_nodes, args.quarter_nodes)
    initial = certified_initial_root(target, args.common_root_certificate)
    budget = target.analytic_input_budget(initial, arb(".003"), arb(".32"), arb(".0025"))
    root, trace = target.refine_certified_root(initial, exact_arb(Fraction(1,4096)), budget, 4)
    report = {
        "kind": "uniform_affine_germ_Arb_root", "proved": True, **provenance(target, args.center_object),
        "common_root_certificate_sha256": sha(args.common_root_certificate),
        "initial_root": ball_record(initial), "root": ball_record(root), "root_newton_trace": trace,
        "bits": args.bits, "quarter_nodes": args.quarter_nodes,
        "input_budget": {key: ([ball_record(x) for x in value] if isinstance(value, list) else ball_record(value))
                         for key, value in budget.items()},
        "wall_seconds": time.monotonic()-started,
        "justification": "the common certificate gives every parameter its unique initial root; each mean-value interval Newton intersection retains it",
        "limitations": ["root only, not a beta enclosure", "this explicit parameter box is not asserted to be the final KAM box"]
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"root": root.str(35), "wall_seconds": report["wall_seconds"]}), flush=True)


def run_collar(args):
    ctx.prec, ctx.cap = args.bits, args.precision
    started = time.monotonic()
    box = json.loads(args.root_box_report.read_text())
    center = json.loads(args.center_collar.read_text())
    if (box.get("kind") != "uniform_affine_germ_Arb_root" or not box.get("proved")
            or box["source_sha256"] != sha(__file__)
            or box["center_object_sha256"] != sha(args.center_object)):
        raise ValueError("the germ root certificate differs from the current source or center")
    for name, digest in box["dependency_sha256"].items():
        if sha(Path(__file__).parent/name) != digest:
            raise ValueError(f"dependency changed: {name}")
    if not center.get("complete") or center["object_sha256"] != sha(args.center_object):
        raise ValueError("center collar is incomplete or belongs to a different object")
    target = ParameterGermBallTarget(args.center_object, Fraction(box["exact_parameter_half_width"]),
                                    args.quarter_nodes, args.angles)
    current = provenance(target, args.center_object)
    for key in ("origin_inputs_sha256", "direction_sha256", "exact_center_parameter",
                "exact_parameter_half_width", "exact_parameter_interval"):
        if current[key] != box[key]:
            raise ValueError(f"parameter identity differs: {key}")
    root, cut = stored_ball(box["root"]), Fraction(center["fixed_cut"])
    for key, values in target.frozen.items():
        if key.endswith("_knots"):
            for value in values:
                q = abs(Fraction.from_float(float(value)))
                if q > cut and not exact_arb(q) > root.upper():
                    raise ValueError("the uniform physical collar could cross a scalar knot")
    scale = exact_arb(Fraction(1,4096))
    budget = target.analytic_input_budget(root, arb(".003"), arb(".32"), arb(".0025"))
    root, trace = target.refine_certified_root(root, scale, budget, 3)
    eta, radius, sigma = root-exact_arb(cut), arb(args.radial_radius), arb(args.sigma)
    if not 0 < eta < radius:
        raise ValueError("the uniform collar is outside its common complex disk")
    coefficients, diagnostics = target.root_density_taylor(root, scale, args.degree, budget)
    polynomial = sum((coefficients[n]*eta**(arb(n)-arb(3)/2)/(arb(n)-arb(3)/2)
                      for n in range(args.degree+1)), arb(0))
    report = {
        "kind": "uniform_exact_affine_germ_collar", "complete": False, **current,
        "root_box_report_sha256": sha(args.root_box_report), "center_collar_sha256": sha(args.center_collar),
        "root": ball_record(root), "root_newton_trace": trace, "fixed_cut": str(cut), "eta": ball_record(eta),
        "bits": args.bits, "quarter_nodes": args.quarter_nodes, "angles": args.angles,
        "degree": args.degree, "series_precision": args.precision,
        "coefficients": [ball_record(x) for x in coefficients], "coefficient_diagnostics": diagnostics,
        "polynomial_finite_part": ball_record(polynomial),
        "input_budget": {key: ([ball_record(x) for x in value] if isinstance(value, list) else ball_record(value))
                         for key, value in budget.items()},
        "limitations": ["uniform collar only; whole bulk on the identical parameter box is still required",
                        "this parameter box is not asserted to be the final KAM box"]
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)

    def save():
        report["wall_seconds"] = time.monotonic()-started
        args.out.write_text(json.dumps(report, indent=2)+"\n")

    save()
    print(json.dumps({"stage":"germ collar coefficients","polynomial":polynomial.str(25)}),flush=True)
    bound, domain = target.collar_domain_bound(root, scale, radius, sigma, budget)
    tail = bound*eta**(arb(args.degree)-arb(1)/2)/(
        (arb(args.degree)-arb(1)/2)*radius**(args.degree+1)*(1-eta/radius))
    angle_mean = 2*bound*(-sigma*args.angles).exp()/(1-(-sigma*args.angles).exp())
    angular = 2*angle_mean*eta**(-arb(3)/2)/(1-eta/radius)
    value = polynomial+arb(0,(tail+angular).upper())
    report.update({"complete":True,"domain":domain,
        "radial_radius":ball_record(radius),"sigma":ball_record(sigma),
        "radial_tail_error":ball_record(tail.upper()),"angular_error":ball_record(angular.upper()),
        "collar_integral":ball_record(value)})
    save()
    print(json.dumps({"stage":"complete uniform germ collar","integral":value.str(30)}),flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    subs = parser.add_subparsers(dest="command", required=True)
    rp, cp = subs.add_parser("root"), subs.add_parser("collar")
    for part in (rp, cp):
        part.add_argument("--center-object", type=Path, required=True)
        part.add_argument("--out", type=Path, required=True)
        part.add_argument("--bits", type=int, default=160 if part is rp else 192)
        part.add_argument("--quarter-nodes", type=int, default=256 if part is rp else 512)
    rp.add_argument("--half-width", type=Fraction, required=True)
    rp.add_argument("--common-root-certificate", type=Path, required=True)
    cp.add_argument("--root-box-report", type=Path, required=True)
    cp.add_argument("--center-collar", type=Path, required=True)
    cp.add_argument("--angles", type=int, default=2048)
    cp.add_argument("--degree", type=int, default=24)
    cp.add_argument("--precision", type=int, default=72)
    cp.add_argument("--radial-radius", default=".0006")
    cp.add_argument("--sigma", default=".02")
    args = parser.parse_args()
    (run_root if args.command == "root" else run_collar)(args)


if __name__ == "__main__":
    main()
