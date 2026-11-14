#!/usr/bin/env python3
"""Consume actual Riemann barriers, prove signs, then check exact frame embedding.

The argument uses the whole PDE characteristics to preserve p<0<q.  It
therefore bounds A by k*M rather than by 2*k*M*M divided by a small gap.
All frame and cylindrical-coordinate bounds concern the actual solution.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
from pathlib import Path
from flint import arb, ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_two_jet_newton_source import record, save
from fourfold_codazzi_piecewise_barrier import read_json, up, down


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def exact_parameter(value):
    if isinstance(value, dict):
        return Fraction(int(value["numerator"]), int(value["denominator"]))
    return Fraction(value)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--barrier", type=Path, required=True)
    parser.add_argument("--native", type=Path, required=True)
    parser.add_argument("--initial", type=Path, default=Path(
        "notes/2026-11-13-Codazzi-target-coefficients-r0-to-0p001-native.json"))
    parser.add_argument("--bits", type=int, default=256)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = args.bits
    if args.out.exists():
        raise FileExistsError("refusing to overwrite an embedding certificate")
    barrier = read_json(args.barrier)
    native = read_json(args.native)
    initial = read_json(args.initial)
    if not barrier["continuation_certified"] or not barrier["piecewise_barrier"]["passed"]:
        raise ValueError("actual continuous PDE existence has not been certified")
    if sha(args.native) != barrier["native_sha256"]:
        raise ValueError("native residual input differs from the continuation certificate")
    if not native["complete"] or not native["whole_affine_parameter_interval"]:
        raise ValueError("incomplete native target family")
    if (not initial["complete"] or not initial["complete_initial_angular_circle"]
            or not initial["whole_parameter_interval"]
            or initial["object_sha256"] != native["object_sha256"]
            or exact_parameter(initial["exact_center_parameter"])
               != exact_parameter(native["exact_center_parameter"])
            or Fraction(initial["exact_parameter_half_width"])
               != Fraction(native["parameter_half_width"])):
        raise ValueError("initial exact waist does not have the certified target identity")
    if not up(initial["initial_C_derivative_ranges"][0]["upper_bound"]) < 0:
        raise ValueError("initial true C is not negative")
    initial_C = up(initial["initial_C_derivative_absolute_bounds"][0])
    initial_k = down(native["initial_error"]["k"])
    initial_sign = (initial_k/initial_C).lower()
    rows = []
    accumulated_source = arb(0)
    displacement = arb(0)
    turn_X = arb(0)
    turn_Y = arb(0)
    turn_normal = arb(0)
    a_lower = None
    sqrtE_lower = None
    max_curvature = arb(0)
    native_rows = native["rows"]
    barrier_rows = barrier["piecewise_barrier"]["rows"]
    if len(native_rows) != len(barrier_rows):
        raise ValueError("different residual and barrier covers")
    for index, (nr, br) in enumerate(zip(native_rows, barrier_rows)):
        if nr["interval"] != br["interval"] or br["native_row"] != index:
            raise ValueError("residual/barrier interval identity failed")
        if not all(br["gates"].values()):
            raise ValueError("an actual continuation barrier gate failed")
        left, right = map(Fraction, nr["interval"])
        h = exact_arb(right-left)
        bnd = nr["bounds"]
        coeff = nr["true_target_coefficients"]
        M = (up(bnd["Mhat"])+up(br["final"][0])).upper()
        beta, kappa = up(bnd["beta"]), up(bnd["kappa"])
        f = (beta*M*(1+M*M)+2*kappa*M).upper()
        accumulated_source = (accumulated_source+h*f).upper()
        sign = (initial_sign-accumulated_source).lower()
        if not sign > 0:
            raise ValueError(f"box {index}: actual characteristic sign budget failed")
        # With x=-p>0 and y=q>0, A=2*k*x*y/(x+y)<=k*M and |B|<=k.
        k = up(coeff["k"])
        sqrtE = up(coeff["E"]).sqrt().upper()
        A = (k*M).upper()
        B = k
        C = (2*k/down(br["actual_gap_lower"])).upper()
        displacement = (displacement+h*sqrtE).upper()
        turn_X = (turn_X+h*sqrtE*A).upper()
        turn_Y = (turn_Y+h*sqrtE*B).upper()
        turn_normal = (turn_normal+h*sqrtE*(A*A+B*B).sqrt()).upper()
        # Gershgorin is only a conservative real principal-curvature bound.
        curvature = (max(A, C)+B).upper()
        max_curvature = max(max_curvature, curvature).upper()
        al = down(coeff["a"])
        el = down(coeff["E"]).sqrt().lower()
        a_lower = al if a_lower is None else min(a_lower, al).lower()
        sqrtE_lower = el if sqrtE_lower is None else min(sqrtE_lower, el).lower()
        rows.append(dict(
            interval=nr["interval"], actual_Riemann_absolute_upper=record(M),
            characteristic_zero_order_upper=record(f),
            accumulated_characteristic_change_upper=record(accumulated_source),
            negative_p_and_positive_q_margin=record(sign),
            A_absolute_upper=record(A), B_absolute_upper=record(B),
            C_absolute_upper=record(C), principal_curvature_upper=record(curvature)))
    support = arb(1)/2
    radius = arb(13)/10
    radius_upper = (radius+displacement).upper()
    radius_lower = (support-displacement).lower()
    angular = (support-displacement-radius*turn_Y).lower()
    normal_support = (support-displacement-radius*turn_normal).lower()
    argument_derivative = (a_lower*angular/(radius_upper*radius_upper)).lower()
    cylindrical_Jacobian = (sqrtE_lower*a_lower*normal_support
                            /(radius_upper*radius_upper)).lower()
    Xz = (1-turn_X*turn_X/2).lower()
    gates = dict(
        complete_actual_characteristic_signs=bool(initial_sign > accumulated_source),
        nonzero_horizontal_radius=bool(radius_lower > 0),
        positive_fixed_r_argument_derivative=bool(argument_derivative > 0),
        positive_cylindrical_Jacobian=bool(cylindrical_Jacobian > 0),
        positive_height_derivative=bool(Xz > 0),
    )
    values = dict(
        initial_Riemann_sign_lower=initial_sign,
        accumulated_characteristic_change_upper=accumulated_source,
        final_uniform_Riemann_sign_margin=initial_sign-accumulated_source,
        displacement_from_initial_curve_upper=displacement,
        radial_frame_X_change_upper=turn_X, radial_frame_Y_change_upper=turn_Y,
        normal_change_upper=turn_normal, horizontal_radius_lower=radius_lower,
        horizontal_radius_upper=radius_upper, angular_numerator_lower=angular,
        horizontal_normal_support_lower=normal_support,
        argument_theta_lower=argument_derivative,
        cylindrical_Jacobian_lower=cylindrical_Jacobian,
        vertical_tangent_component_lower=Xz,
        actual_principal_curvature_absolute_upper=max_curvature)
    out = dict(
        kind="actual_Codazzi_signed_Riemann_frame_embedding",
        source_sha256=sha(__file__), bits=args.bits,
        barrier_path=str(args.barrier), barrier_sha256=sha(args.barrier),
        native_path=str(args.native), native_sha256=sha(args.native),
        initial_path=str(args.initial), initial_sha256=sha(args.initial),
        object_sha256=native["object_sha256"],
        exact_center_parameter=native["exact_center_parameter"],
        parameter_half_width=native["parameter_half_width"],
        whole_real_angular_circle=True, whole_affine_parameter_interval=True,
        complete=True, embedding_certified=all(gates.values()),
        certified_positive_interval=native["exact_requested_interval"],
        reflected_interval=["-"+native["exact_requested_interval"][1],
                            native["exact_requested_interval"][1]],
        rows=rows, gates=gates, bounds={key: record(value) for key, value in values.items()},
        geometric_reference_theorems={name: sha(Path("results")/name) for name in
            ("R123-separated-correction-budgets-and-normal-Hessian.md",
             "R128-quantitative-embedding-of-the-exact-waist-annulus.md")},
        closed_surface_complete=False)
    save(args.out, out)
    print("embedding_certified", out["embedding_certified"])
    for key, value in values.items():
        print(key, value.str(14))


if __name__ == "__main__":
    main()
