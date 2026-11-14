#!/usr/bin/env python3
"""Uniform directed root collar on one explicit exact-affine parameter box.

All interval operations are pointwise uniform in the one real parameter.
The true-root identity K(t(parameter), parameter)=0 is used only in the
existing deflated Taylor formula.  No derivative of a frozen root is taken.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time
from flint import arb, ctx
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_combine import stored_ball
from fourfold_phase_beta_parameter_root import ParameterBallTarget, provenance


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--center-object", type=Path, required=True)
    parser.add_argument("--root-box-report", type=Path, required=True)
    parser.add_argument("--center-collar", type=Path, required=True)
    parser.add_argument("--bits", type=int, default=192)
    parser.add_argument("--quarter-nodes", type=int, default=512)
    parser.add_argument("--angles", type=int, default=2048)
    parser.add_argument("--degree", type=int, default=24)
    parser.add_argument("--precision", type=int, default=72)
    parser.add_argument("--radial-radius", default=".0006")
    parser.add_argument("--sigma", default=".02")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    ctx.prec, ctx.cap = args.bits, args.precision
    started = time.monotonic()
    box = json.loads(args.root_box_report.read_text())
    center = json.loads(args.center_collar.read_text())
    here = Path(__file__).parent
    if (box.get("kind") != "uniform_native_Arb_root_for_exact_affine_parameter_box"
            or not box.get("proved")
            or box["center_object_sha256"] != sha(args.center_object)
            or box["source_sha256"] != sha(here/"fourfold_phase_beta_parameter_root.py")):
        raise ValueError("the uniform root report does not match its current source or center")
    for name, digest in box["dependency_sha256"].items():
        if sha(here/name) != digest:
            raise ValueError(f"uniform root dependency changed: {name}")
    if (not center.get("complete") or center["object_sha256"] != sha(args.center_object)):
        raise ValueError("the complete center collar has a different center")
    half_width = Fraction(box["exact_parameter_half_width"])
    target = ParameterBallTarget(args.center_object, half_width, args.quarter_nodes, args.angles)
    current = provenance(target, args.center_object)
    for key in ("origin_inputs_sha256", "direction_sha256", "exact_center_parameter",
                "exact_parameter_half_width", "exact_parameter_interval"):
        if current[key] != box[key]:
            raise ValueError(f"parameter-box identity changed: {key}")
    root, cut = stored_ball(box["root"]), Fraction(center["fixed_cut"])
    scale = exact_arb(Fraction(1, 4096))
    # The physical collar is required to stay in one exact scalar span for
    # every parameter.  Tiny neighboring binary knots are not merged.
    for key, values in target.frozen.items():
        if key.endswith("_knots"):
            for value in values:
                q = abs(Fraction.from_float(float(value)))
                if q > cut and not exact_arb(q) > root.upper():
                    raise ValueError("the uniform physical collar could cross a scalar knot")
    budget = target.analytic_input_budget(root, arb(".003"), arb(".32"), arb(".0025"))
    root, trace = target.refine_certified_root(root, scale, budget, 3)
    eta = root-exact_arb(cut)
    radius, sigma = arb(args.radial_radius), arb(args.sigma)
    if not 0 < eta < radius:
        raise ValueError("the complete parameter collar is outside its common complex disk")
    coefficients, diagnostics = target.root_density_taylor(root, scale, args.degree, budget)
    polynomial = sum((coefficients[n]*eta**(arb(n)-arb(3)/2)/(arb(n)-arb(3)/2)
                      for n in range(args.degree+1)), arb(0))
    report = {
        "kind": "uniform_exact_affine_parameter_collar",
        "complete": False, **current,
        "source_sha256": sha(__file__),
        "parameter_source_sha256": current["source_sha256"],
        "root_box_report_sha256": sha(args.root_box_report),
        "center_collar_sha256": sha(args.center_collar),
        "root": ball_record(root), "root_newton_trace": trace,
        "fixed_cut": str(cut), "eta": ball_record(eta),
        "bits": args.bits, "quarter_nodes": args.quarter_nodes,
        "angles": args.angles, "degree": args.degree, "series_precision": args.precision,
        "coefficients": [ball_record(x) for x in coefficients],
        "coefficient_diagnostics": diagnostics,
        "polynomial_finite_part": ball_record(polynomial),
        "input_budget": {key: ([ball_record(x) for x in value]
            if isinstance(value, list) else ball_record(value)) for key, value in budget.items()},
        "limitations": [
            "This is the collar only; a uniform beta still requires the whole bulk on the identical parameter box",
            "The parameter interval is explicit and has not been asserted to be the final KAM interval",
            "No beta derivative is computed by freezing the moving root"
        ]}
    args.out.parent.mkdir(parents=True, exist_ok=True)

    def save():
        report["wall_seconds"] = time.monotonic()-started
        args.out.write_text(json.dumps(report, indent=2)+"\n")

    save()
    print(json.dumps({"stage": "uniform collar coefficients",
        "root": root.str(25), "polynomial": polynomial.str(25)}), flush=True)
    bound, domain = target.collar_domain_bound(root, scale, radius, sigma, budget)
    tail = bound*eta**(arb(args.degree)-arb(1)/2)/(
        (arb(args.degree)-arb(1)/2)*radius**(args.degree+1)*(1-eta/radius))
    angle_mean = 2*bound*(-sigma*args.angles).exp()/(1-(-sigma*args.angles).exp())
    angular = 2*angle_mean*eta**(-arb(3)/2)/(1-eta/radius)
    value = polynomial+arb(0, (tail+angular).upper())
    report.update({"complete": True, "domain": domain,
        "radial_radius": ball_record(radius), "sigma": ball_record(sigma),
        "radial_tail_error": ball_record(tail.upper()), "angular_error": ball_record(angular.upper()),
        "collar_integral": ball_record(value)})
    save()
    print(json.dumps({"stage": "complete uniform collar", "integral": value.str(30)}), flush=True)


if __name__ == "__main__":
    main()
