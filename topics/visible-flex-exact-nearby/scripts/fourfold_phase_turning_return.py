#!/usr/bin/env python3
"""Phase-checkpoint type scan and moving-turn principal return diagnostic.

Uses consistent derivatives of the saved phase candidate's finite primitive.
The exact infinite unit-tangent field is kept distinct and given analytic
FFT-tail/alias budgets at stated radial samples, excluding roundoff.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.optimize import brentq

from fourfold_phase_geometry import (
    load_phase, raw_phase_data, raw_modified_phase_data, preflight)
from fourfold_turning_return import TurnGeometry, mean_directions


def scan(geometry, solver, xs, theta):
    output = []
    for x in xs:
        data = raw_phase_data(geometry, solver, np.full_like(theta, x), theta)
        det = -data["delta"]/data["area"]**2
        normal_n = data["n"]/data["area"]
        target = geometry.radial_target_metric([x])
        output.append(dict(
            x=float(x), detII_min=float(det.min()), detII_max=float(det.max()),
            N_min=float(normal_n.min()), N_max=float(normal_n.max()),
            area_min=float(data["area"].min()),
            target_radial_metric_K=float(target["K"][0]),
            target_radial_metric_detII=float(-target["target_discriminant"][0]),
            target_radial_metric_E=float(target["E"][0]),
            all_hyperbolic_sample=bool(det.max() < 0),
            all_elliptic_sample=bool(det.min() > 0),
            all_N_negative_sample=bool(normal_n.max() < 0)))
    return output


def bracket_from_scan(rows):
    first_elliptic = next((j for j, row in enumerate(rows)
                           if row["all_elliptic_sample"]), None)
    if first_elliptic is None:
        return None
    positive = [row["x"] for row in rows[:first_elliptic]
                if row["all_hyperbolic_sample"]]
    if not positive:
        return None
    return [max(positive), rows[first_elliptic]["x"]]


class RadialTargetTurns(TurnGeometry):
    """The R37 modified operator has radial turns, recomputed from its target."""

    def __init__(self, geometry, solver, bracket):
        self.radial_root = brentq(
            lambda x: float(geometry.radial_target_metric([x])[
                "target_discriminant"][0]), *bracket, xtol=5e-14)
        super().__init__(geometry, solver, bracket=bracket,
                         raw_evaluator=raw_modified_phase_data)
        self.initial_turn_range = [self.radial_root, self.radial_root]

    def turn(self, theta):
        theta = np.asarray(theta, dtype=float)
        root = np.full_like(theta, self.radial_root)
        data = self.raw(self.candidate, self.solver, root, theta,
                        columns=self.with_variations)
        target = self.candidate.radial_target_metric(
            root, with_variations=self.with_variations)
        self.maximum_root_residual = max(
            self.maximum_root_residual, float(np.max(np.abs(data["delta"]))))
        data["t_theta"] = np.zeros_like(theta)
        if self.with_variations:
            data["t_columns"] = -target["discriminant_columns"]/(
                target["target_discriminant_x"][None, :])
        return root, data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkpoint", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--directions", type=Path)
    parser.add_argument("--quarter-nodes", type=int)
    parser.add_argument("--scan-angles", type=int, default=128)
    parser.add_argument("--scan-radial", type=int, default=121)
    parser.add_argument("--xmax", type=float, default=.6)
    parser.add_argument("--scan-only", action="store_true")
    parser.add_argument("--operator", choices=("true", "modified"), default="true")
    parser.add_argument("--central-core-only", action="store_true",
                        help="explicitly allow outer hyperbolic components; do not claim a global return")
    parser.add_argument("--rays", type=int, default=16)
    parser.add_argument("--tolerance", type=float, default=5e-7)
    args = parser.parse_args()
    digest = hashlib.sha256(args.checkpoint.read_bytes()).hexdigest()
    directions, direction_metadata = None, None
    if args.directions:
        with np.load(args.directions, allow_pickle=False) as saved:
            direction_metadata = json.loads(str(saved["metadata"]))
            if direction_metadata["checkpoint_sha256"] != digest:
                raise ValueError("Schur directions belong to a different checkpoint")
            directions = saved["directions"]
    geometry, solver, vector, metadata = load_phase(
        args.checkpoint, args.quarter_nodes, directions)
    print(json.dumps({"progress": "phase geometry loaded", "sha256": digest}),
          flush=True)
    direction_check = None
    if directions is not None:
        direction_check = preflight(geometry, solver, vector)
        print(json.dumps({"progress": "Schur geometry derivative preflight",
                          "checks": direction_check}), flush=True)
    theta = np.arange(args.scan_angles)*(np.pi/2)/args.scan_angles
    rows = scan(geometry, solver, np.linspace(0., args.xmax, args.scan_radial), theta)
    bracket = bracket_from_scan(rows)
    sign_changes = [
        dict(left=left["x"], right=right["x"],
             K_left=left["target_radial_metric_K"], K_right=right["target_radial_metric_K"])
        for left, right in zip(rows[:-1], rows[1:])
        if left["target_radial_metric_K"]*right["target_radial_metric_K"] < 0]
    budgets = []
    for x in (0., .1, .2, .24, .3, .5):
        options = []
        for sigma in (.025, .04, .06, .08, .1, .15, .2, .25):
            try:
                option = geometry.strip_budget(x, sigma)
                options.append(option)
            except (OverflowError, ValueError):
                pass
        if options:
            budgets.append(min(options, key=lambda entry:
                               max(entry["geometry_tail_alias_bounds"].values())))
    report = dict(
        kind="floating_phase_finite_primitive_actual_type_and_principal_return",
        checkpoint=args.checkpoint.name, sha256=digest, quarter_nodes=geometry.nodes,
        scan=rows, sampled_common_turn_bracket=bracket,
        primitive_third_jet_budgets_at_stated_radial_points=budgets,
        actual_parameter_columns=("bare circumference/mean-height parameters"
                                  if directions is None else
                                  "finite-L2 Schur-corrected phase directions"),
        direction_metadata=direction_metadata,
        direction_geometry_check=direction_check,
        principal_operator=args.operator,
        target_sign_change_brackets=sign_changes,
        central_core_only=args.central_core_only,
        global_two_turn_geometry_asserted=False,
        modified_operator_formula=("raw_Delta_hat=(-K0)*G_actual^2; "
                                   "G_actual=|Fx cross Ftheta|^2; G0=E*a^2 distinct"),
        parameter_target_convention=(
            "synchronous radial target family g0(p)=E(p)dx^2+a(p)^2dtheta^2; "
            "columns include delta g0 and are not derivatives at one frozen target"),
        limitations=[
            "ordinary floating arithmetic and finite radial/angular samples",
            "actual curvature of one consistent finite primitive, not mean-metric K",
            "FFT strip budgets omit rounding and are only at stated radial points",
            "turn uniqueness and continuous transversality are not certified",
            "principal geometric return excludes amplitudes, phase corrections, elliptic DtN",
            "parameter columns do not define an already existing exact PDE family",
            "no exact closed surface, visibility, or reach certificate"])
    args.out.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"progress": "phase type scan finished", "turn_bracket": bracket,
                      "waist": rows[0],
                      "all_sampled_N_negative": all(row["all_N_negative_sample"] for row in rows),
                      "maximum_selected_third_jet_tail_alias_bound": max(
                          max(entry["geometry_tail_alias_bounds"].values())
                          for entry in budgets)}), flush=True)
    if args.scan_only:
        return
    if bracket is None or not rows[0]["all_hyperbolic_sample"]:
        raise ValueError("actual phase sample does not support the required two-turn core")
    if args.operator == "true":
        actual_turn = TurnGeometry(geometry, solver, bracket=bracket,
                                   raw_evaluator=raw_phase_data)
    else:
        crossings = [(left["x"], right["x"]) for left, right in zip(rows[:-1], rows[1:])
                     if left["target_radial_metric_K"] < 0 < right["target_radial_metric_K"]]
        if len(crossings) != 1 and not args.central_core_only:
            raise ValueError("sampled radial target does not have exactly one positive-side turn")
        if not crossings:
            raise ValueError("no central hyperbolic-to-elliptic target turn found")
        if len(sign_changes) > 1:
            report["limitations"].append(
                "outer hyperbolic annuli remain; the reported map covers only the central component")
        actual_turn = RadialTargetTurns(geometry, solver, crossings[0])
    initial = np.arange(args.rays)*(np.pi/2)/args.rays
    returned, jacobian, columns = actual_turn.round_trip(initial, args.tolerance)
    columns = columns.T
    shift = returned-initial
    result = dict(
        angular_period=float(np.pi/2), initial_angles=initial.tolist(),
        returned_angles=returned.tolist(), jacobian=jacobian.tolist(),
        mean_columns=columns.tolist(),
        operator_turn_range=actual_turn.initial_turn_range,
        displacement_min=float(shift.min()), displacement_max=float(shift.max()),
        jacobian_min=float(jacobian.min()), jacobian_max=float(jacobian.max()),
        mean_column_min=columns.min(axis=0).tolist(),
        mean_column_max=columns.max(axis=0).tolist(),
        minimum_sampled_transversality=actual_turn.minimum_denominator,
        minimum_sampled_qbar=actual_turn.minimum_qbar,
        maximum_float_turn_residual=actual_turn.maximum_root_residual,
        ode_rtol=args.tolerance, rhs_calls=actual_turn.calls)
    result.update(mean_directions(solver, columns))
    result["mean_waist_radius_column_meaning"] = "circumference radius"
    report["principal_return"] = result
    args.out.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({key: value for key, value in result.items()
                      if key not in ("initial_angles", "returned_angles",
                                     "jacobian", "mean_columns")}), flush=True)


if __name__ == "__main__":
    main()
