#!/usr/bin/env python3
"""Replay the R106 same-object strict-core field diagnostic with directed balls.

This is a finite set of actual radial/angular points, uniform in the stated
real parameter interval. It is NOT a continuous angular cover, a ray integral,
a Fourier coefficient certificate or a PDE inverse.
"""
from __future__ import annotations
import argparse
from bisect import bisect_right
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time
from flint import arb, acb, ctx
from fourfold_phase_beta_parameter_germ import ParameterGermBulkTarget, provenance
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_subprincipal_ray_fields import fields_from_true_geometry, ray_terms


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def record(z):
    z = acb(z)
    return {"real": ball_record(z.real), "imag": ball_record(z.imag)}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--object", type=Path, default=Path(
        "data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json"))
    ap.add_argument("--half-width", type=Fraction, default=Fraction(1, 10**9))
    ap.add_argument("--radial", type=Fraction, default=Fraction(1, 8))
    ap.add_argument("--nodes", type=int, default=512)
    ap.add_argument("--bits", type=int, default=192)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    if args.nodes % 8:
        raise ValueError("the exact eight-angle indices require nodes divisible by 8")
    ctx.prec, ctx.cap = args.bits, 5
    start = time.monotonic()
    target = ParameterGermBulkTarget(args.object, args.half_width,
        args.nodes, args.nodes, arb(".002"), arb(".0015"), arb(".32"))
    knots = sorted(set(abs(Fraction.from_float(float(x)))
        for key, values in target.frozen.items() if key.endswith("_knots")
        for x in values))
    i = bisect_right(knots, args.radial)-1
    left, right = knots[i], knots[i+1]
    if not left <= args.radial < right:
        raise ValueError("actual radial point has no common right-hand germ")
    target.set_cell(left, right)
    radial = acb(exact_arb(args.radial))
    coefficient, curvature, curvature_r, budget = target.complete_data(radial)
    geometric = target.physical_fields(coefficient, budget)
    legacy = target.density_values(radial)
    entries = []
    for j in range(8):
        index = j*args.nodes//8
        fields = fields_from_true_geometry(
            F=geometric[0,0][index], Fr=geometric[1,0][index],
            Frr=geometric[2,0][index], Ftheta=geometric[0,1][index],
            Frtheta=geometric[1,1][index], Fthetatheta=geometric[0,2][index],
            K0=curvature, K0_r=curvature_r)
        delta = fields["reduced_density"]-legacy[index]
        if not delta.real.contains(0) or not delta.imag.contains(0):
            raise ValueError("actual reduced density does not overlap frozen beta source")
        branches = {}
        for sigma in (-1, 1):
            terms = ray_terms(fields, 1, sigma)
            speed = terms["angle_rhs"]
            residual = (fields["angular_log_mu_flux"]
                -speed*fields["radial_log_mu_flux"]
                -sigma*(fields["log_mu_r"]+speed*fields["log_mu_theta"]))
            if not residual.real.contains(0) or not residual.imag.contains(0):
                raise ValueError("the exact characteristic flux identity failed")
            branches[str(sigma)] = {
                "initial_label_J": "1",
                "instantaneous_terms_only": {key: record(value) for key,value in terms.items()},
                "characteristic_flux_identity_residual": record(residual)}
        entries.append({"physical_angle": f"pi*{j}/16",
            "fields": {key:record(value) for key,value in fields.items()},
            "legacy_reduced_density_difference": record(delta), "branches": branches})
    primitive_budget = {}
    for key,value in budget.items():
        if isinstance(value, bool):
            primitive_budget[key] = value
        elif isinstance(value, list):
            primitive_budget[key] = [ball_record(x) for x in value]
        else:
            primitive_budget[key] = ball_record(value)
    here = Path(__file__).parent
    report = {"kind": "R106_actual_uniform_parameter_finite_point_fields",
        "finite_point_computation_complete": True,
        "continuous_angle_cover_proved": False, "true_ray_integral_proved": False,
        "full_nonmean_phase_proved": False,
        "source_sha256": sha(__file__),
        "kernel_sha256": sha(here/"fourfold_subprincipal_ray_fields.py"),
        "actual_target": provenance(target,args.object),
        "radial": str(args.radial), "common_germ": [str(left),str(right)],
        "bits":args.bits,"primitive_nodes":args.nodes,"series_cap":5,
        "curvature":record(curvature),"curvature_r":record(curvature_r),
        "primitive_budget":primitive_budget,"entries":entries,
        "wall_seconds":time.monotonic()-start,
        "limits":["No interpolation between the eight angles is certified.",
            "The shown J=1 is an initial instantaneous evaluation, not a transported ray Jacobian.",
            "The whole parameter interval is preserved through complete affine scalar germs."]}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({"complete":True,"out":str(args.out),"sha256":sha(args.out),
                      "wall_seconds":report["wall_seconds"]}),flush=True)


if __name__ == "__main__":
    main()
