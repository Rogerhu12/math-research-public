#!/usr/bin/env python3
"""R259 diagnostic on the original complete scalar family and original mesh.

Construct the circular *collocation* reference by its scalar recurrence,
then retain the three low-mode two-by-two collocation tangent systems.
The full saved true T112 zero slope Jacobian is read and measured.  All
112 right residuals of the low-mode trial are reported; high-core Schur
elimination is not silently omitted when the saved J has off-diagonal
coupling.  Optional three-equation Newton work is only a candidate search
for the straight lambda homotopy, never a full BVP or an existence proof.

No app is used as a derivative of a finite-Gauss radius.  The actual source
circle satisfies R'=ap*R/a.  The source radius a, its independently returned
ap, the circle R, and the exact declared scalar-expression enclosure are
kept distinct.  Every nonlinear continuation and original acceptance gate
remains to be computed after any useful candidate is found.
"""
from __future__ import annotations

import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"

import argparse
from fractions import Fraction
import json
from pathlib import Path
import time
import traceback

import numpy as np

import geometry_20261114_full_dn_solve as original
from geometry_20261114_constrained_trust_warm import EXPECTED, setup, write
from geometry_20261114_constrained_collocation import CompleteResidual
from geometry_20261114_lifted_modes_profile import scalar_spec, field_spec
from geometry_20261114_full_prefix_operator import (
    export_scalar_descriptor, ScalarExpression, Q)

HERE = Path(__file__).resolve().parent
SCHEMA = "R259-original-circle-collocation-low-three-resonance-diagnostic-v1"


class CircleReference:
    def __init__(self, profile, mesh, true_slope_jacobian, target, height_sign, cut_scale):
        self.profile = profile
        self.x = np.asarray(mesh, float)
        self.h = np.diff(self.x)
        self.mid = .5*(self.x[:-1]+self.x[1:])
        self.base = np.asarray([profile.base_jet(s) for s in self.x])[:, :2]
        self.base_mid = np.asarray([profile.base_jet(s) for s in self.mid])[:, :2]
        self.controls = np.asarray([profile.control_jets(s) for s in self.x])[:, :2]
        self.controls_mid = np.asarray([profile.control_jets(s) for s in self.mid])[:, :2]
        self.J = np.asarray(true_slope_jacobian)
        self.target = np.asarray(target)
        self.eh, self.gamma = height_sign, cut_scale
        self.M = profile.M
        if self.J.shape != (self.M, self.M) or self.target.shape != (3,):
            raise ValueError("Retain all native slope rows and exactly the declared three target entries")
        self.offdiagonal = self.J.copy()
        np.fill_diagonal(self.offdiagonal, 0.)
        self.exactly_diagonal = bool(np.count_nonzero(self.offdiagonal) == 0)
        self.frequency = np.array([2., 4., 6.])

    def matrix(self, ratio, radius, speed, vertical):
        k2 = self.frequency**2
        answer = np.empty((len(radius), 3, 2, 2), dtype=np.result_type(radius, speed))
        answer[:, :, 0, 0] = ratio[:, None]*(1-k2)
        answer[:, :, 0, 1] = -vertical[:, None]*k2/radius[:, None]
        answer[:, :, 1, 0] = (speed*ratio/vertical)[:, None]*(k2-1)
        answer[:, :, 1, 1] = ratio[:, None]*k2
        return answer

    def evaluate(self, parameters):
        parameters = np.asarray(parameters)
        if parameters.shape != (3,):
            raise ValueError("Keep all three actual scalar controls")
        nodes = self.base+np.einsum("mjk,k->mj", self.controls, parameters)
        middle = self.base_mid+np.einsum("mjk,k->mj", self.controls_mid, parameters)
        real = np.isrealobj(parameters)
        if real and (np.any(~np.isfinite(nodes)) or np.any(~np.isfinite(middle))
                or np.min(nodes[:, 0]) <= 0 or np.min(middle[:, 0]) <= 0
                or np.max(abs(nodes[:, 1])) >= 1 or np.max(abs(middle[:, 1])) >= 1):
            raise FloatingPointError("Original node/mid scalar domain failed; no interval claim is made by this test")
        q, qm = nodes[:, 1]/nodes[:, 0], middle[:, 1]/middle[:, 0]
        h = self.h
        left = -1-h*(q[:-1]+2*qm)/6-h*h*qm*q[:-1]/12
        right = 1-h*(q[1:]+2*qm)/6+h*h*qm*q[1:]/12
        if np.any(right == 0) or np.any(~np.isfinite(right)):
            raise FloatingPointError("The original circle radius cell cannot be eliminated")
        radius = np.empty(len(self.x), dtype=np.result_type(parameters, float))
        radius[0] = 1.
        for j in range(len(h)):
            radius[j+1] = -left[j]*radius[j]/right[j]
        radius_mid = .5*(radius[:-1]+radius[1:])-h*(q[1:]*radius[1:]-q[:-1]*radius[:-1])/8
        speed, speed_mid = q*radius, qm*radius_mid
        margin, margin_mid = 1-speed*speed, 1-speed_mid*speed_mid
        if real and (np.any(~np.isfinite(radius)) or np.any(~np.isfinite(radius_mid))
                or np.min(radius) <= 0 or np.min(radius_mid) <= 0
                or np.min(margin) <= 0 or np.min(margin_mid) <= 0):
            raise FloatingPointError("The actual source circle left R>0 or 1-(ap*R/a)^2>0")
        vertical, vertical_mid = np.sqrt(margin), np.sqrt(margin_mid)
        height = np.r_[0., np.cumsum(h*(vertical[:-1]+vertical[1:]+4*vertical_mid)/6)]
        B = self.matrix(q, radius, speed, vertical)
        Bm = self.matrix(qm, radius_mid, speed_mid, vertical_mid)
        identity = np.eye(2)
        hh = h[:, None, None, None]
        L = -identity-hh*(B[:-1]+2*Bm)/6-hh*hh*(Bm@B[:-1])/12
        R = identity-hh*(B[1:]+2*Bm)/6+hh*hh*(Bm@B[1:])/12
        modes = np.zeros((len(self.x), 3, 2), dtype=radius.dtype)
        modes[0, :, 0] = 1.
        for j in range(len(h)):
            rhs = np.einsum("kij,kj->ki", L[j], modes[j])
            modes[j+1] = np.linalg.solve(R[j], -rhs[..., None])[..., 0]
        velocity = np.einsum("mkij,mkj->mki", B, modes)
        if np.any(~np.isfinite(modes)) or np.any(~np.isfinite(velocity)):
            raise FloatingPointError("The low-mode original transfer is nonfinite; use a two-end linear BVP instead")
        native = np.zeros(self.M, dtype=radius.dtype)
        native[:3] = self.eh*self.target*modes[-1, :, 1]
        full = -self.gamma*(self.J@native)
        full[:3] += self.target*velocity[-1, :, 1]
        unit_diagonal = velocity[-1, :, 1]-self.gamma*self.eh*np.diag(self.J)[:3]*modes[-1, :, 1]
        return dict(parameters=parameters, scalar_nodes=nodes, scalar_middle=middle,
            radius=radius, radius_mid=radius_mid, radius_rhs=speed,
            height=height, height_rhs=vertical, ratio=q, ratio_mid=qm,
            vertical_mid=vertical_mid, margin=margin, margin_mid=margin_mid,
            modes=modes, velocity=velocity, L=L, R=R, B=B, Bmid=Bm,
            radius_left=left, radius_right=right, full_right=full,
            native_first_order_height=native, low_right=full[:3],
            unit_diagonal_defect=unit_diagonal,
            equation=(unit_diagonal if self.exactly_diagonal else full[:3]))

    def jacobian(self, parameters):
        step = 1e-25
        columns = []
        for j in range(3):
            p = np.asarray(parameters, complex)
            p[j] += 1j*step
            columns.append(self.evaluate(p)["equation"].imag/step)
        return np.stack(columns, axis=1)

    def description(self, state):
        residual = (np.einsum("mkij,mkj->mki", state["L"], state["modes"][:-1])
            + np.einsum("mkij,mkj->mki", state["R"], state["modes"][1:]))
        conditions = np.linalg.cond(state["R"])
        J = self.jacobian(state["parameters"])
        singular = np.linalg.svd(J, compute_uv=False)
        levels = []
        for step in (2e-5, 1e-5, 5e-6):
            errors = []
            valid = True
            for j in range(3):
                d = np.zeros(3); d[j] = step
                try:
                    numerical = (self.evaluate(state["parameters"]+d)["equation"]
                        - self.evaluate(state["parameters"]-d)["equation"])/(2*step)
                    errors.append(float(np.max(abs(numerical-J[:, j])))/max(1., float(np.max(abs(J[:, j])))))
                except FloatingPointError:
                    valid = False
                    break
            levels.append(dict(step=step, valid=valid, maximum_relative_error=max(errors) if valid else None))
        return dict(parameters=state["parameters"].tolist(),
            full_first_order_native_height=state["native_first_order_height"].tolist(),
            complete_first_order_right_residual=state["full_right"].tolist(),
            unit_diagonal_defects=state["unit_diagonal_defect"].tolist(),
            low_equations_used=state["equation"].tolist(),
            low_equations_definition=("unit d_j; actual full J measured exactly diagonal" if self.exactly_diagonal
                else "full three low rows with actual off-diagonal J; free high-core Schur elimination unresolved"),
            source_target_first_three=self.target.tolist(), target_zero_indices=np.flatnonzero(self.target == 0).tolist(),
            three_unit_resonances_are_necessary_for_these_straight_targets=bool(
                self.exactly_diagonal and np.all(self.target != 0)),
            zero_tail_slope_J=dict(shape=list(self.J.shape),
                maximum_absolute_offdiagonal=float(np.max(abs(self.offdiagonal))),
                nonzero_offdiagonal_entries=int(np.count_nonzero(self.offdiagonal)),
                all_entries_consumed=True, exactly_diagonal_as_recorded=self.exactly_diagonal,
                ready_linear_graph_used=False),
            high_right_leak_max=float(np.max(abs(state["full_right"][3:]), initial=0)),
            high_free_core_Schur_elimination_computed=False,
            high_mode_nonresonance_proved=False,
            scalar_node_and_mid_minimum_radius=float(min(np.min(state["scalar_nodes"][:, 0]),
                np.min(state["scalar_middle"][:, 0]))),
            source_circle_node_and_mid_minimum_radius=float(min(state["radius"].min(), state["radius_mid"].min())),
            source_circle_node_and_mid_minimum_beta2=float(min(state["margin"].min(), state["margin_mid"].min())),
            actual_circle_R_minus_supplied_a_node_max=float(np.max(abs(state["radius"]-state["scalar_nodes"][:, 0]))),
            radius_cell_denominator_minimum_absolute=float(np.min(abs(state["radius_right"]))),
            low_two_by_two_right_condition_max_by_mode=conditions.max(axis=0).tolist(),
            low_mode_trajectory_max_by_mode=np.max(abs(state["modes"]), axis=(0, 2)).tolist(),
            low_original_collocation_tangent_residual_max=float(np.max(abs(residual))),
            three_by_three_parameter_jacobian=J.tolist(), singular_values=singular.tolist(),
            numerical_parameter_condition=float(singular[0]/singular[-1]) if singular[-1] else None,
            numerical_singular_values_are_not_a_transversality_proof=True,
            independent_real_parameter_difference_checks=levels,
            scalar_and_circle_queries_are_not_whole_interval_bounds=True)


def returned_ap(expression, interval, branch, middle):
    """The independently returned ap expression; never a Gauss derivative."""
    b, B = expression.b, expression.boundaries
    kind, index = branch
    s = interval
    if kind == "initial":
        law = expression.geometry["initial_law"]
        length, speed, k0 = (Q(float(law[key])) for key in ("length", "velocity", "k0"))
        if middle >= length:
            value = s*0+b(speed)
        else:
            u = s/b(length)
            c0, c1, c2 = k0*length, 3*speed-2*k0*length, k0*length-2*speed
            value = b(c0)*u+b(c1)*u*u+b(c2)*u**3
    elif kind == "prefix":
        width = expression.x[index+1]-expression.x[index]
        u = (s-b(expression.x[index]))/b(width)
        value = s*0
        coefficients = expression.coefficients[index]
        for j in reversed(range(1, len(coefficients))):
            value = value*u+b(j*coefficients[j]/width)
    elif kind == "turn":
        u = (s-b(B["prefix_end"]))/b(expression.turn["length"])
        um = (middle-B["prefix_end"])/expression.turn["length"]
        panel = 0 if um < expression.turn["ei"] else (1 if um <= 1-expression.turn["eo"] else 2)
        value = expression.angle_phase(u, panel).sin()
    elif kind == "coast":
        value = s*0-b(expression.speed)
    elif kind == "bridge":
        seg = expression.segments[index]
        um = (middle-B["bridge_start"]-seg["s0"])/seg["length"]
        if um <= 0:
            u, um = s*0, Fraction(0)
        elif um >= 1:
            u, um = s*0+1, Fraction(1)
        else:
            u = (s-b(B["bridge_start"]+seg["s0"]))/b(seg["length"])
        if "turn_ramp" in seg:
            panel = 0 if um < seg["turn_ramp"] else (1 if um <= 1-seg["turn_ramp"] else 2)
        else:
            panel = 0
        value = expression.bridge_phase(seg, u, panel).sin()
    else:
        raise AssertionError("Unknown original scalar branch")
    for control, parameter in zip(expression.controls, expression.parameters):
        if parameter and control["left"] < middle < control["left"]+control["stored_width"]:
            width = b(control["stored_width"])
            u = (s-b(control["left"]))/width
            value += b(parameter)*width*64*(3*u*u-12*u**3+15*u**4-6*u**5)
    return value


def scalar_domain(profile, specification, output, bits, maximum_depth):
    """Enclose the complete declared real a/ap expression, not samples."""
    import geometry_20261114_direct_operator_cell as primitive
    primitive.ctx.prec = bits
    descriptor = export_scalar_descriptor(profile, specification, origin="unspecified-runtime-object")
    expression = ScalarExpression(specification, descriptor, primitive)
    rows, failed, totals = [], [], dict(leaf_count=0, split_cells=0)
    def visit(left, right, depth):
        middle = (left+right)/2
        branch = expression.branch(middle)
        interval = primitive.arb(str(middle), str((right-left)/2))
        radius = expression.value(interval, branch, middle)
        speed = returned_ap(expression, interval, branch, middle)
        good = bool(radius.is_finite() and speed.is_finite()
            and radius.lower() > 0 and speed.abs_upper() < 1)
        definitely_bad = bool(radius.is_finite() and speed.is_finite()
            and (radius.upper() <= 0 or speed.lower() >= 1 or speed.upper() <= -1))
        if not good and not definitely_bad and depth < maximum_depth:
            totals["split_cells"] += 1
            visit(left, middle, depth+1); visit(middle, right, depth+1)
            return
        totals["leaf_count"] += 1
        record = dict(interval=[str(left), str(right)], branch=list(branch), depth=depth,
            radius_enclosure=primitive.ball_record(radius), returned_ap_enclosure=primitive.ball_record(speed),
            strict_positive_radius_and_abs_ap_lt_one=good,
            definite_scalar_domain_failure=definitely_bad)
        rows.append(record)
        if not good:
            failed.append(record)
    for left, right in zip(expression.breakpoints[:-1], expression.breakpoints[1:]):
        visit(left, right, 0)
    result = dict(schema="R259-complete-declared-scalar-domain-enclosure-v1",
        descriptor=descriptor, covered_interval=[str(expression.breakpoints[0]), str(expression.breakpoints[-1])],
        bits=bits, maximum_depth=maximum_depth, **totals,
        complete_declared_real_expression_domain_certified=not failed,
        unresolved_leaf_count=len(failed), leaves=rows,
        source_returned_ap_used=True, returned_ap_identified_with_derivative_of_finite_Gauss_a=False,
        exact_prefix_scalar_and_complete_stored_finite_Gauss_expression=True,
        literal_binary64_evaluation_roundoff_enclosed=False,
        exact_scalar_derivative_compatibility_or_C2_interface_certificate=False,
        source_circle_R_and_full_Frenet_domain_covered_by_this_scalar_bound=False)
    write(output/"complete-scalar-domain.json.gz", result)
    return {key: value for key, value in result.items() if key not in ("leaves", "descriptor")}


def complete_reference_check(model, state, profile, flow, boundary, output, source, source_sha):
    """Actual original FFT/node/mid/RMS evaluation, without a native call."""
    boundary.target = np.zeros(3)
    y = np.zeros((len(model.x), flow.dimension))
    y[:, 0] = state["radius"]
    y[:, boundary.iz] = state["height"]
    y[:, flow.parameter_slice] = state["parameters"]
    problem = CompleteResidual(model.x, flow, boundary)
    actual = problem.evaluate(problem.chart.pack(y), require_rms=True)
    if not actual["finite"]:
        write(output/"circle-original-domain.json", actual["report"])
        return dict(original_full_reference_finite=False, actual_domain=actual["report"])
    derivative_checks = []
    for node in sorted(set((0, len(model.x)//2, len(model.x)-1))):
        R, q = state["radius"][node], state["ratio"][node]
        W = state["height_rhs"][node]
        for j, k in enumerate(model.frequency):
            U, H = state["modes"][node, j]
            tangent = ((1-k*k)*R-U)/k
            direction = np.zeros(flow.n)
            direction[j+1] = U
            direction[flow.M+1+j] = tangent
            direction[boundary.iz+j+1] = H
            expected = np.zeros(flow.n)
            expected[j+1], expected[boundary.iz+j+1] = state["velocity"][node, j]
            expected[flow.M+1+j] = q*(k*U+tangent)+k*W*H/R
            direct = flow.point_rhs(model.x[node], y[node, :flow.n].astype(complex)
                + 1j*1e-25*direction, state["parameters"]).imag/1e-25
            derivative_checks.append(dict(node=node, station=float(model.x[node]), mode=j+1,
                actual_full_FFT_direction_relative_error=float(np.max(abs(direct-expected)))/max(1., float(np.max(abs(expected)))),
                all_physical_rows_compared=True))
    specification = scalar_spec(profile, source["complete_scalar_profile"]["complete_original_port"],
        state["parameters"], EXPECTED["accepted"])
    reference = dict(schema=SCHEMA, scope=__doc__, M=flow.M, N=flow.q.N,
        mesh=model.x.tolist(), states=actual["y"].tolist(), rhs=actual["f"].tolist(),
        complete_scalar_profile=specification, field_representation=field_spec(flow.M, flow.q.N),
        fixed_core_targets=[0., 0., 0.], original_large_core_targets_retained=False,
        source_prepared_sha256=source_sha, full_native_tail_at_nonzero_height_computed=False,
        success=False, new_coupled_finite_acceptance=False, complete_closed_surface=False,
        actual_original_residual_and_domain=actual["report"],
        original_full_FFT_tangent_checks=derivative_checks,
        low_three_unit_modes_UH=state["modes"].tolist(),
        low_three_unit_modes_rhs_UH=state["velocity"].tolist())
    write(output/"circle-reference.json.gz", reference)
    return dict(original_full_reference_finite=True, actual_domain=actual["report"],
        original_full_FFT_tangent_checks=derivative_checks,
        reference_file="circle-reference.json.gz", reference_sha256=original.sha(output/"circle-reference.json.gz"),
        reference_is_not_a_nonzero_parent=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("accepted", "prepared", "tail-anchor", "tail-config", "out"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--parameters", type=float, nargs=3, default=[0., 0., 0.])
    parser.add_argument("--newton-steps", type=int, default=0)
    parser.add_argument("--backtracks", type=int, default=12)
    parser.add_argument("--candidate-resonance-tolerance", type=float, default=1e-8)
    parser.add_argument("--interval-bits", type=int, default=160)
    parser.add_argument("--interval-depth", type=int, default=14)
    args = parser.parse_args()
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("All numerical work belongs to the public repository's own Actions")
    if not 0 <= args.newton_steps <= 12 or not 1 <= args.backtracks <= 20:
        raise ValueError("Keep the optional candidate search explicitly bounded")
    for name, digest in EXPECTED.items():
        if original.sha(getattr(args, name)) != digest:
            raise ValueError("Retain the complete original actual input: "+name)
    args.out.mkdir(parents=True, exist_ok=True)
    if any(args.out.iterdir()):
        raise ValueError("Use a fresh diagnostic output directory")
    source, accepted, anchor = [original.read(path) for path in (args.prepared, args.accepted, args.tail_anchor)]
    profile, flow, boundary = setup(accepted, source, anchor, 4096, 1)
    J = np.asarray(anchor["heightJetJacobian"]).reshape(3*flow.M+2, flow.M)[:flow.M]
    target = np.asarray(accepted["core"]["coefficients"])[:3]
    model = CircleReference(profile, source["mesh"], J, target, boundary.eh, boundary.cut_scale)
    names = (Path(__file__).name, "geometry_20261114_constrained_trust_warm.py",
        "geometry_20261114_constrained_collocation.py", "geometry_20261114_full_dn_augmented.py",
        "geometry_20261114_full_dn_boundary.py", "geometry_20261114_physical_test_boundary.py",
        "geometry_20261114_lifted_modes_profile.py", "geometry_20261114_full_prefix_operator.py",
        "geometry_20261114_direct_operator_cell.py")
    status = dict(schema=SCHEMA, scope=__doc__, phase="starting",
        input_sha256=EXPECTED, consumed_source_sha256={name: original.sha(HERE/name) for name in names},
        same_complete_original_scalar_formula_and_three_supports=True,
        original_mesh_nodes=len(model.x), field_and_tail_modes=flow.M,
        low_modes_diagnosed=[1, 2, 3], complete_zero_slope_J_retained=True,
        native_nonlinear_solver_called=False, original_Gauss_app_used_as_a_derivative=False,
        original_full_BVP_or_large_amplitude_acceptance_claimed=False,
        straight_homotopy_only=True, weighted_lambda_j_homotopies_not_excluded=True,
        searches=[], success=False)
    start = time.monotonic()
    try:
        parameters = np.asarray(args.parameters)
        state = model.evaluate(parameters)
        status["initial"] = model.description(state)
        write(args.out/"resonance-status.json", status)
        if args.newton_steps and (not model.exactly_diagonal or np.any(target == 0)):
            raise ValueError("This optional diagonal three-equation search cannot replace high-core Schur or a zero-target expansion")
        for iteration in range(args.newton_steps):
            residual = state["equation"]
            if np.max(abs(residual)) <= args.candidate_resonance_tolerance:
                break
            derivative = model.jacobian(parameters)
            direction = np.linalg.solve(derivative, -residual)
            before = .5*float(residual@residual)
            slope = float(residual@(derivative@direction))
            row = dict(iteration=iteration, parameters=parameters.tolist(),
                residual=residual.tolist(), derivative=derivative.tolist(),
                true_model_merit_slope=slope, trials=[], accepted=False)
            status["searches"].append(row)
            if not np.isfinite(slope) or slope >= 0:
                row["reason"] = "No finite strict descent of the actual low-mode equations"
                break
            for trial in range(args.backtracks):
                alpha = 2.**(-trial)
                item = dict(alpha=alpha, accepted=False)
                row["trials"].append(item)
                try:
                    candidate = model.evaluate(parameters+alpha*direction)
                    value = candidate["equation"]
                    merit = .5*float(value@value)
                    item.update(actual_merit=merit, merit_before=before)
                    if merit <= before+.2*alpha*slope:
                        parameters = parameters+alpha*direction
                        state = candidate
                        item["accepted"] = row["accepted"] = True
                        break
                except (FloatingPointError, np.linalg.LinAlgError) as error:
                    item["domain_or_cell_error"] = repr(error)
            write(args.out/"resonance-status.json", status)
            if not row["accepted"]:
                break
        status["final"] = model.description(state)
        specification = scalar_spec(profile, source["complete_scalar_profile"]["complete_original_port"],
            parameters, EXPECTED["accepted"])
        status["complete_scalar_domain"] = scalar_domain(profile, specification, args.out,
            args.interval_bits, args.interval_depth)
        status["original_complete_circle_check"] = complete_reference_check(model, state, profile, flow,
            boundary, args.out, source, EXPECTED["prepared"])
        small = bool(np.max(abs(state["full_right"])) <= args.candidate_resonance_tolerance)
        status.update(phase="diagnostic-completed", diagnostic_completed=True,
            candidate_resonance_tolerance=args.candidate_resonance_tolerance,
            low_mode_candidate_has_small_full_recorded_right_residual=small,
            this_candidate_threshold_is_not_an_original_BVP_acceptance_gate=True,
            full_nonlinear_nonzero_lambda_solution_computed=False,
            high_mode_nonresonance_or_interval_transversality_proved=False)
        return 0
    except Exception as error:
        status.update(phase="exception", exception=repr(error), traceback=traceback.format_exc())
        raise
    finally:
        status["seconds"] = time.monotonic()-start
        write(args.out/"resonance-status.json", status)


if __name__ == "__main__":
    raise SystemExit(main())
