#!/usr/bin/env python3
"""Whole bulk enclosure for one exact affine parameter box, using correlated germs.

The integrator proves each real-parameter member at once. A larger adjustable
error budget is distributed toward the fixed root collar; it controls only
the requested accuracy and is never used as a bound for an uncomputed error.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time
from flint import arb, acb, ctx
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_bulk_interval import exact_arb, real_interval
from fourfold_phase_beta_combine import stored_ball
from fourfold_phase_beta_parameter_germ import ParameterGermFastBulkTarget, provenance


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--center-object", type=Path, required=True)
    parser.add_argument("--collar", type=Path, required=True)
    parser.add_argument("--bits", type=int, default=128)
    parser.add_argument("--quarter-nodes", type=int, default=256)
    parser.add_argument("--angles", type=int, default=1024)
    parser.add_argument("--sigma", default=".02")
    parser.add_argument("--base-cell-tolerance", default=".0002")
    parser.add_argument("--extra-total-tolerance", default=".04")
    parser.add_argument("--eval-limit", type=int, default=64)
    parser.add_argument("--cell-depth", type=int, default=12)
    parser.add_argument("--start-cell", type=int, default=0)
    parser.add_argument("--max-cells", type=int)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    ctx.prec, ctx.cap = args.bits, 4
    collar = json.loads(args.collar.read_text())
    here = Path(__file__).parent
    if (collar.get("kind") != "uniform_exact_affine_germ_collar"
            or not collar.get("complete")
            or collar["source_sha256"] != sha(here/"fourfold_phase_beta_parameter_germ.py")
            or collar["center_object_sha256"] != sha(args.center_object)):
        raise ValueError("uniform collar source, center, or completeness mismatch")
    for name, digest in collar["dependency_sha256"].items():
        if sha(here/name) != digest:
            raise ValueError(f"collar dependency changed: {name}")
    target = ParameterGermFastBulkTarget(args.center_object,
        Fraction(collar["exact_parameter_half_width"]), args.quarter_nodes, args.angles,
        arb(".003"), arb(".0025"), arb(".32"))
    current = provenance(target, args.center_object)
    for key in ("origin_inputs_sha256", "direction_sha256", "exact_center_parameter",
                "exact_parameter_half_width", "exact_parameter_interval"):
        if current[key] != collar[key]:
            raise ValueError(f"parameter-box identity differs: {key}")
    cut, waist = Fraction(collar["fixed_cut"]), Fraction(1,1048576)
    knots = {Fraction(0), cut}
    for key, values in target.frozen.items():
        if key.endswith("_knots"):
            knots.update(q for q in
                (abs(Fraction.from_float(float(x))) for x in values) if 0 < q < cut)
    if not waist < sorted(knots)[1]:
        raise ValueError("waist crosses an exact scalar knot")
    knots.add(waist)
    points = sorted(knots)
    cells = [(a,b) for a,b in zip(points,points[1:]) if a >= waist]
    root_floor = stored_ball(collar["root"]).lower()
    if not root_floor > exact_arb(cut):
        raise ValueError("the fixed bulk cut is not below every root")
    power = -arb(3)/2
    weight_normalizer = (root_floor-exact_arb(cut))**power-root_floor**power
    base, extra = arb(args.base_cell_tolerance), arb(args.extra_total_tolerance)
    if not base > 0 or not extra >= 0:
        raise ValueError("invalid numerical accuracy budgets")
    tolerances = []
    for left,right in cells:
        weight = ((root_floor-exact_arb(right))**power
                  -(root_floor-exact_arb(left))**power)/weight_normalizer
        tolerance = (base+extra*weight).lower()
        if not tolerance > 0:
            raise ValueError("nonpositive allocated cell tolerance")
        tolerances.append(tolerance)
    started = time.monotonic()
    report = {
        "kind": "uniform_exact_affine_germ_phase_bulk", "complete": False, **current,
        "source_sha256": sha(__file__),
        "parameter_engine_sha256": current["source_sha256"],
        "collar_sha256": sha(args.collar), "fixed_cut": str(cut), "waist_width": str(waist),
        "bits": args.bits, "quarter_nodes": args.quarter_nodes, "angles": args.angles,
        "sigma": args.sigma, "radial_cells_total": len(cells), "start_cell": args.start_cell,
        "base_cell_tolerance": args.base_cell_tolerance,
        "extra_total_tolerance": args.extra_total_tolerance,
        "tolerance_root_floor": ball_record(root_floor),
        "allocated_original_cell_tolerances": [ball_record(x) for x in tolerances],
        "accepted_cells": [], "failed_cells": [], "subdivision_count": 0,
        "limitations": ["a partial parameter cover is not a uniform beta certificate",
                        "the chosen explicit parameter box is not asserted to be the final KAM box"]}
    args.out.parent.mkdir(parents=True, exist_ok=True)

    def save():
        report["wall_seconds"] = time.monotonic()-started
        report["callback_evaluations"] = target.evaluations
        report["failed_analytic_evaluations"] = target.failed_analytic_evaluations
        args.out.write_text(json.dumps(report,indent=2)+"\n")

    if args.start_cell == 0:
        cap,bound = target.waist_cap(waist)
        report["waist_integral"],report["waist_density_bound"] = ball_record(cap),ball_record(bound)
        save()
    sigma = arb(args.sigma)
    stop = len(cells) if args.max_cells is None else min(len(cells),args.start_cell+args.max_cells)
    for index in range(args.start_cell,stop):
        base_left,base_right = cells[index]
        target.set_cell(base_left,base_right)
        pending = [(base_left,base_right,0)]
        while pending:
            left,right,depth = pending.pop()
            length,before = exact_arb(right-left),target.evaluations
            local_tolerance = tolerances[index]*length/exact_arb(base_right-base_left)
            try:
                bound,angular = target.angular_domain(left,right,sigma)
                if not length*angular < local_tolerance/2:
                    raise ValueError("uniform angular fee exceeds allocated accuracy")
                whole = target.mean_callback(acb(real_interval(left,right)),False)
                direct = whole.real*length+arb(0,(length*angular).upper())
                if direct.is_finite() and direct.rad() < local_tolerance:
                    value,method = direct,"continuous_interval_range"
                else:
                    integral = acb.integral(target.mean_callback,
                        acb(exact_arb(left)),acb(exact_arb(right)),
                        abs_tol=local_tolerance/2,rel_tol=arb("1e-10"),
                        eval_limit=args.eval_limit,deg_limit=32,depth_limit=20)
                    if not integral.is_finite() or not integral.real.rad() < local_tolerance/2:
                        raise ValueError("uniform validated quadrature did not meet allocated accuracy")
                    value,method = integral.real+arb(0,(length*angular).upper()),"Arb_validated_complex_integration"
                report["accepted_cells"].append({
                    "index":index,"left":str(left),"right":str(right),"depth":depth,
                    "integral":ball_record(value),"method":method,
                    "allocated_tolerance":ball_record(local_tolerance),
                    "complex_angle_density_bound":ball_record(bound),
                    "angular_integral_error":ball_record((length*angular).upper()),
                    "evaluations":target.evaluations-before})
                print(json.dumps({"stage":"uniform germ cell","index":index,"depth":depth,
                    "integral":value.str(18)}),flush=True)
            except Exception as exc:
                if depth < args.cell_depth:
                    mid=(left+right)/2
                    pending.extend([(mid,right,depth+1),(left,mid,depth+1)])
                    report["subdivision_count"]+=1
                    report["latest_subdivision"]={"index":index,"left":str(left),"right":str(right),"reason":repr(exc)}
                else:
                    report["failed_cells"].append({"index":index,"left":str(left),"right":str(right),"error":repr(exc)})
            save()
    report["complete"]=(args.start_cell==0 and stop==len(cells)
        and not report["failed_cells"] and "waist_integral" in report)
    save()


if __name__ == "__main__":
    main()
