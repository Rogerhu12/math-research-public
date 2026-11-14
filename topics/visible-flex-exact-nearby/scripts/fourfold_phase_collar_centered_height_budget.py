#!/usr/bin/env python3
"""Centered final-field enclosures for the actual wide positive collar.

This is a new evaluator, not a change to the frozen geometric object or to
fourfold_phase_collar_correlated_height.py.  At authoring time the native
executor was unavailable: no actual output of this source is claimed.

The retained finite output Taylor polynomial is evaluated after the
geometric cancellations.  Its two real-variable remainders are bounded by
the true whole-box mixed jets.  All infinite Fourier and native radial
Taylor errors of the imported frozen evaluator remain present.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import gc
import hashlib
import json
import math
from pathlib import Path
import time

from flint import arb, ctx

from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_parameter_germ import provenance
from fourfold_phase_canonical_collar_correlated_height import (
    CorrelatedOrdinaryGeometry, FortyTermGeometry, FiniteRootCoordinates,
    root_potential_coefficients, ordinary_canonical_operator,
    polynomial_height, gauged_operator, physical_polynomial_trial,
    trial_residual_coefficients, real_jet, jet_function, mul, align,
)
from fourfold_phase_canonical_collar_finite import (
    canonical_derivative, jet_summary,
)

FROZEN_WIDE_SHA = "3752ac63322bc4008a898e7309f6ac46e2647290d86f3c330467950fa5b2cb42"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def scalar_coefficient(value, i, j, scale, dr=0, dt=0):
    """Taylor coefficient of d_r^dr d_theta^dt value about its jet centre.

    The imported native time is w with r=r_c-scale*w.  In particular the
    sign (-1)^i is essential, and physical theta is not the index x=4theta.
    """
    if min(i, j, dr, dt) < 0 or i+dr >= value.m or j+dt >= value.n:
        raise ValueError("unknown true mixed coefficient requested")
    factor = (math.factorial(i+dr)//math.factorial(i)
              * (math.factorial(j+dt)//math.factorial(j)))
    return (value.coefficient(i+dr, j+dt).real*factor
            * (-1/scale)**(i+dr))


def rectangular_enclosure(whole, centre, scale, radius_r, radius_theta,
                          *, dr=0, dt=0, order_r=3, order_theta=4):
    """A real rectangular Taylor enclosure, with no analytic mixed-domain claim.

    Angular Taylor is applied first at each fixed r, then radial Taylor to
    each retained angular coefficient.  The input whole jet covers the
    complete same r/theta/parameter box.  Its coefficients are divided by
    the corresponding factorials.
    """
    radius_r, radius_theta = arb(radius_r).upper(), arb(radius_theta).upper()
    if radius_r < 0 or radius_theta < 0:
        raise ValueError("negative rectangle radius")
    m = min(int(order_r), whole.m-dr-1, centre.m-dr-1)
    n = min(int(order_theta), whole.n-dt-1, centre.n-dt-1)
    if min(m, n) < 1:
        raise ValueError("insufficient true derivatives for this remainder")
    ur, ut = arb(0, radius_r), arb(0, radius_theta)
    polynomial = arb(0)
    for j in range(n-1, -1, -1):
        row = arb(0)
        for i in range(m-1, -1, -1):
            row = row*ur+scalar_coefficient(centre, i, j, scale, dr, dt)
        polynomial = polynomial*ut+row
    angular_tail = (abs(scalar_coefficient(
        whole, 0, n, scale, dr, dt))*radius_theta**n).upper()
    radial_tail = arb(0)
    for j in range(n):
        radial_tail += (abs(scalar_coefficient(
            whole, m, j, scale, dr, dt))*radius_r**m*radius_theta**j).upper()
    radial_tail = radial_tail.upper()
    remainder = (angular_tail+radial_tail).upper()
    candidate = polynomial+arb(0, remainder)
    direct = scalar_coefficient(whole, 0, 0, scale, dr, dt)
    if not candidate.overlaps(direct):
        raise ValueError("whole and centred enclosures of the same field disagree")
    # Each choice is individually a true enclosure.  This comparison only
    # chooses between two valid bounds; it does not select a parameter.
    chosen = (candidate if candidate.rad().upper() < direct.rad().upper()
              else direct)
    return dict(value=chosen, centred=candidate, whole=direct,
                radial_tail=radial_tail, angular_tail=angular_tail,
                order_r=m, order_theta=n)


def root_bundles(args, angle_centre, angle_whole):
    """Return only small true root jets; release native primitive caches."""
    model = FortyTermGeometry(
        args.object, args.half_width, args.root_certificate, nodes=args.nodes)
    result = {}
    for name, angle in (("whole", angle_whole), ("centre", angle_centre)):
        principal = model.principal(angle, at_root=True)
        coordinates = FiniteRootCoordinates(principal, model.scale)
        values = root_potential_coefficients(principal, model.scale)
        chart = coordinates.positive(arb(0), model.m-1, model.n)
        op = ordinary_canonical_operator(principal, chart, model.scale)
        result[name] = dict(coordinates=coordinates, root_values=values,
                            height=op["height"])
    root, scale = arb(model.root), arb(model.scale)
    # No principal/native array is retained by FiniteRootCoordinates.
    del model, principal, chart, op
    gc.collect()
    return root, scale, result


def augmented_fields(values, root_values, offset, scale, include_trial):
    out = dict(values)
    y = values["y"]
    if not y.coefficient(0, 0).real > 0:
        raise ValueError("this ordinary far box must stay strictly beyond the root")
    inverse_y = jet_function(y, "inverse")
    inverse_sqrt_y = jet_function(jet_function(y, "log")*(-arb(1)/2), "exp")
    sqrt_y = jet_function(jet_function(y, "log")*(arb(1)/2), "exp")
    out["relative_cross_error"] = real_jet(mul(values["cross_error"], inverse_sqrt_y))
    out["relative_tangential_error"] = real_jet(mul(values["tangential_error"], inverse_y))
    inv_height = jet_function(values["height"], "inverse")
    gy = mul(canonical_derivative(values["height"], values, scale, "normal"),
             inv_height)
    gp = mul(canonical_derivative(values["height"], values, scale, "angle"),
             inv_height)
    out["height_normal_log"] = real_jet(gy)
    out["height_angle_log"] = real_jet(gp)
    out["height_weighted_angle_log"] = real_jet(mul(sqrt_y, gp))
    if include_trial:
        trial = physical_polynomial_trial(root_values, values, offset, scale)
        out.update(trial_residual_coefficients(values, trial, scale))
    return out


def ordinary_fields(model, radial_left, radial_right, angle, root, bundle,
                    *, actual_span=None, include_trial=True):
    # prepare_cell changes the base point.  Do not keep any inherited state
    # associated with a preceding centre, even if a future dependency starts
    # using this cache from principal().
    model._states.clear()
    model.prepare_cell(radial_left, radial_right, span=actual_span)
    principal = model.principal(angle)
    offset = model.center-root
    if not offset > 0:
        raise ValueError("ordinary wide rectangle meets an unresolved root")
    chart = bundle["coordinates"].positive(offset, model.m-1, model.n)
    height = polynomial_height(
        bundle["height"], offset, model.scale, chart["y"].m, chart["y"].n)
    op = gauged_operator(principal, chart, height, model.scale)
    values = augmented_fields(
        op, bundle["root_values"], offset, model.scale, include_trial)
    return values, dict(
        span=list(map(str, model.actual_span)), offset=ball_record(offset),
        correlated_native_budget=model.target.last_correlated_budget)


def records_for_fields(whole, centre, scale, radius_r, radius_theta, args):
    records, actual = {}, {}
    for name in sorted(set(whole).intersection(centre)):
        if not hasattr(whole[name], "coefficient"):
            continue
        try:
            r = rectangular_enclosure(
                whole[name], centre[name], scale, radius_r, radius_theta,
                order_r=args.order_r, order_theta=args.order_theta)
        except ValueError as exc:
            # Missing derivative orders are a recorded limitation; do not
            # replace an unknown coefficient by zero.
            if "insufficient true derivatives" not in str(exc):
                raise
            value = whole[name].coefficient(0, 0).real
            actual[name] = value
            records[name] = dict(
                value=ball_record(value), method="original whole-box jet",
                centred_remainder_unavailable=str(exc))
            continue
        actual[name] = r["value"]
        row = dict(
            value=ball_record(r["value"]),
            original_whole_box=ball_record(r["whole"]),
            centre_value=ball_record(centre[name].coefficient(0, 0).real),
            radial_remainder_upper=ball_record(r["radial_tail"]),
            angular_remainder_upper=ball_record(r["angular_tail"]),
            retained_orders=[r["order_r"], r["order_theta"]],
            physical_theta_derivative_upper=[])
        for j in (1, 2):
            try:
                d = rectangular_enclosure(
                    whole[name], centre[name], scale, radius_r, radius_theta,
                    dt=j, order_r=args.order_r, order_theta=args.order_theta)
                row["physical_theta_derivative_upper"].append(
                    ball_record(abs(d["value"]).upper()))
            except ValueError as exc:
                if "insufficient true derivatives" not in str(exc):
                    raise
                if j >= whole[name].n:
                    row["physical_theta_derivative_upper"].append(None)
                else:
                    v = abs(whole[name].coefficient(0, j).real)*math.factorial(j)
                    row["physical_theta_derivative_upper"].append(ball_record(v.upper()))
        records[name] = row
    return records, actual


def local_form_budget(actual):
    needed = ("normal_error", "relative_cross_error",
              "relative_tangential_error", "height",
              "height_normal_log", "height_weighted_angle_log")
    if any(k not in actual for k in needed):
        raise ValueError("incomplete true matrix/gauge output")
    e11 = abs(actual["normal_error"]).upper()
    e12 = abs(actual["relative_cross_error"]).upper()
    e22 = abs(actual["relative_tangential_error"]).upper()
    eps = (max(e11, e22)+e12).upper()
    h = actual["height"]
    if not h > 0:
        raise ValueError("root-matched height lost positivity")
    gy = abs(actual["height_normal_log"]).upper()
    gp = abs(actual["height_weighted_angle_log"]).upper()
    # All bases here are nonnegative.  Do not use interval **2 on a
    # sign-changing Arb interval.
    G = (gy*gy+gp*gp).sqrt().upper()
    result = dict(
        relative_matrix_norm_upper=ball_record(eps),
        height=ball_record(h),
        normalised_log_gradient_upper=ball_record(G),
        perturbation_less_than_one=bool(eps < 1),
        full_wide_cover_proved=False,
        full_gap_proved=False)
    if eps < 1:
        result["inverse_comparison_factor"] = ball_record(
            (h.upper()*h.upper()/(1-eps)).upper())
        result["matrix_comparison"] = (
            "(1-eps) diag(1,y) <= tau_*^2 A <= (1+eps) diag(1,y); "
            "A^-1 <= inverse_comparison_factor diag(1,1/y)")
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--object", type=Path, default=Path(
        "data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json"))
    p.add_argument("--root-certificate", type=Path, default=Path(
        "data/phase_ring_continuation/type_fixed_step02_d5_step5_local_parameter_root_jets_h5e7.json"))
    p.add_argument("--half-width", type=F, default=F(1, 10**9))
    p.add_argument("--radius", type=F, default=F(2423, 10000))
    p.add_argument("--radius-half-width", type=F, default=F(1, 65536))
    p.add_argument("--angle", type=F, default=F(1, 16))
    p.add_argument("--angle-half-width", type=F, default=F(1, 2048))
    p.add_argument("--native-order", type=int, default=48)
    p.add_argument("--native-radius", type=F, default=F(1, 128))
    p.add_argument("--radial-precision", type=int, default=8)
    p.add_argument("--angle-precision", type=int, default=12)
    p.add_argument("--order-r", type=int, default=3)
    p.add_argument("--order-theta", type=int, default=4)
    p.add_argument("--nodes", type=int, default=512)
    p.add_argument("--bits", type=int, default=256)
    p.add_argument("--without-trial-coefficients", action="store_true")
    p.add_argument("--emit-report", action="store_true",
                   help="emit the complete JSON after writing it, for immediate preservation")
    p.add_argument("--out", type=Path, required=True)
    a = p.parse_args()
    if min(a.radius_half_width, a.angle_half_width) < 0:
        raise ValueError("negative local width")
    if min(a.order_r, a.order_theta) < 1:
        raise ValueError("positive Taylor remainder orders required")
    frozen = Path(__file__).with_name("fourfold_phase_collar_correlated_height.py")
    if sha(frozen) != FROZEN_WIDE_SHA:
        raise ValueError("the imported frozen wide evaluator differs")
    ctx.prec, ctx.cap = a.bits, 32
    start = time.monotonic()
    centre_angle = exact_arb(a.angle)*arb.pi()
    radius_theta = (exact_arb(a.angle_half_width)*arb.pi()).upper()
    whole_angle = centre_angle+arb(0, radius_theta)
    root, scale, bundles = root_bundles(a, centre_angle, whole_angle)
    model = CorrelatedOrdinaryGeometry(
        a.object, a.half_width, nodes=a.nodes,
        radial_precision=a.radial_precision, angle_precision=a.angle_precision,
        native_order=a.native_order, native_radius=a.native_radius)
    if not model.scale == scale:
        raise ValueError("root and ordinary native radial scales disagree")
    whole, whole_meta = ordinary_fields(
        model, a.radius-a.radius_half_width, a.radius+a.radius_half_width,
        whole_angle, root, bundles["whole"],
        include_trial=not a.without_trial_coefficients)
    actual_span = model.actual_span
    centre, centre_meta = ordinary_fields(
        model, a.radius, a.radius, centre_angle, root, bundles["centre"],
        actual_span=actual_span, include_trial=not a.without_trial_coefficients)
    fields, actual = records_for_fields(
        whole, centre, scale, exact_arb(a.radius_half_width), radius_theta, a)
    form = local_form_budget(actual)
    output = dict(
        kind="actual-centred-final-field-wide-collar-local-enclosure",
        proved_specified_local_box=True,
        proved_complete_wide_collar=False, proved_full_cap_gap=False,
        source_sha256=sha(__file__), frozen_wide_source_sha256=FROZEN_WIDE_SHA,
        identity=provenance(model.target, a.object),
        root_certificate_sha256=sha(a.root_certificate),
        exact_parameter_half_width=str(a.half_width),
        physical_radial_interval=[
            str(a.radius-a.radius_half_width), str(a.radius+a.radius_half_width)],
        physical_angle_over_pi_interval=[
            str(a.angle-a.angle_half_width), str(a.angle+a.angle_half_width)],
        root=ball_record(root), native_scale=ball_record(scale),
        whole_evaluation=whole_meta, centre_evaluation=centre_meta,
        root_height_jet=jet_summary(
            bundles["centre"]["height"], max_radial=4, max_angle=2, scale=scale),
        fields=fields, actual_local_form=form,
        root_coordinate_degree=6, height_polynomial_degree=4,
        exact_object_changed=False,
        source_pullback="P_ground(tau_* U o Psi)=(J/tau_*) (P_* U) o Psi",
        retained_additional_weak_flux="E11 U_y",
        limitations=[
            "One specified continuous box only; no complete collar covering.",
            "No full-cap primal/dual gap, outer Wronskian, or feedback inverse.",
            "Reported theta derivatives hold at fixed physical r.",
            "Canonical log-gradient fields are explicitly differentiated in the true chart.",
            "No fixed-y analytic regularity is inferred from physical mixed jets.",
            "Physical polynomial trial fields are not the exact frozen-linear Airy trial.",
            "All mean and low modes remain in future full-source/contact work."],
        dependencies={name: sha(Path(__file__).with_name(name)) for name in (
            "fourfold_phase_canonical_collar_far.py",
            "fourfold_phase_canonical_collar_finite.py",
            "fourfold_phase_canonical_collar_bivariate_recovery.py",
            "fourfold_phase_beta_parameter_germ.py",
            "fourfold_phase_beta_interval.py",
            "fourfold_phase_beta_bulk_interval.py",
            "fourfold_time_angle_jets.py")},
        seconds=time.monotonic()-start)
    text = json.dumps(output, indent=2)+"\n"
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(text)
    if a.emit_report:
        print(text, end="")
    else:
        print(json.dumps(dict(
            local_box_proved=True, complete_collar=False,
            source_sha256=sha(__file__), report_sha256=sha(a.out),
            report_bytes=len(text.encode()),
            epsilon=str(actual["normal_error"]),
            relative_matrix_norm_upper=form["relative_matrix_norm_upper"],
            V=str(actual["V"]), seconds=output["seconds"])))


if __name__ == "__main__":
    main()
