#!/usr/bin/env python3
"""Actual Hermite-query domain rows and a projected damped warm interface.

This independent module changes no original mathematical source.  A domain
row differentiates the original fixed-physical-angle beta^2 through both
actual nodal RHS values, their complete physical/scalar Jacobians, and the
exact inlet/constant-state coordinate chart.  It is an optimizer row, not
an extra equation or an acceptance certificate.

The optional projected LSMR interface uses [A P C^-1; lambda P C^-1].
Its recovered scaled direction is z=P C^-1 v.  C is any supplied positive
diagonal; the convenience choice below uses the ORIGINAL UNPROJECTED
column norms and is not labelled the projected operator's exact norm.

The CLI only checks a chosen actual query on an unaccepted saved warm.
It does not construct a new warm, call Node, or claim a BVP/tail solution.
All numerical use of this CLI is restricted to this public repo's Actions.
"""
from __future__ import annotations

import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"

import argparse
import copy
import hashlib
import json
from pathlib import Path
import time

import numpy as np
from scipy.interpolate import CubicHermiteSpline
from scipy.sparse.linalg import LinearOperator

from geometry_20261114_constrained_collocation import CompleteResidual
import geometry_20261114_constrained_trust_warm as warm_driver


HERE = Path(__file__).resolve().parent
SCHEMA = "actual-Hermite-RMS-domain-tangent-interface-v1"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def hermite_weights(fraction):
    t = float(fraction)
    if not 0 <= t <= 1:
        raise ValueError("A domain query must lie in its declared original interval")
    return (1 + 2*t)*(1-t)**2, t*(1-t)**2, t*t*(3-2*t), t*t*(t-1)


def point_margin(flow, station, physical, parameters, angle_index):
    """Original normal-vector beta^2 at one fixed original phi grid point.

No absolute value, real cast, conjugation, clipping or sqrt(beta^2) is
used.  Complex inputs therefore retain the complete local analytic chain.
The separate scalar admissibility and rho guards remain the original
solver's job; this function is not a replacement for any of them.
"""
    if not 0 <= angle_index < flow.q.N:
        raise ValueError("The fixed angle index must use the actual original q.N")
    _, first, second = flow.q.jet(np.asarray(physical))
    d, e = first[angle_index], second[angle_index]
    lam2 = np.sum(d*d)
    tangent = d/np.sqrt(lam2)
    normal = e - np.sum(e*tangent)*tangent
    curvature = np.sqrt(np.sum(normal*normal))/lam2
    jets = flow.scalar_jets(np.array([station]), np.asarray(parameters)[:, None])[0]
    a, nu = jets[:2]
    return 1 - (nu/(a*curvature))**2


def linear_jet_rows(probe, angle_index):
    """Obtain the actual q.jet linear maps, including its rotating frame.

The frozen FFT implementation is applied to each unit coefficient.  This
does not replace it by a separately rounded trigonometric synthesizer.
The resulting row is checked below against direct nonlinear complex
evaluation at the real saved state.
"""
    n = probe.n
    first, second = np.empty((3, n)), np.empty((3, n))
    unit = np.zeros(n)
    for j in range(n):
        unit[j] = 1.
        _, d, dd = probe.jet(unit)
        first[:, j], second[:, j] = d[angle_index], dd[angle_index]
        unit[j] = 0.
    return first, second


def local_margin_gradient(flow, station, physical, parameters, angle_index):
    """Full point gradient, without dividing by nu or a scalar derivative.

nu is the original returned a-prime field.  The calculation makes no
assumption that a separate finite quadrature for a has derivative nu.
"""
    physical, parameters = np.asarray(physical), np.asarray(parameters)
    _, first, second = flow.q.jet(physical)
    d, e = first[angle_index], second[angle_index]
    cross = np.cross(d, e)
    Q, W = np.sum(d*d), np.sum(cross*cross)
    a, nu = flow.scalar_jets(np.array([station]), parameters[:, None])[0, :2]
    if not all(np.isfinite(v) for v in (Q, W, a, nu)) or min(Q, W, a) <= 0:
        raise FloatingPointError("The actual local curve or scalar domain is invalid")
    factor = nu*nu/(a*a)
    gd = -6*factor*Q**2*d/W + 2*factor*Q**3*np.cross(e, cross)/W**2
    ge = 2*factor*Q**3*np.cross(cross, d)/W**2
    ga = 2*nu*nu*Q**3/(a**3*W)
    gnu = -2*nu*Q**3/(a*a*W)
    drow, erow = linear_jet_rows(flow.q, angle_index)
    gy = drow.T@gd + erow.T@ge
    scalar_rows = np.asarray(flow.profile.control_jets(station))
    gp = ga*scalar_rows[0] + gnu*scalar_rows[1]
    original_value = point_margin(flow, station, physical, parameters, angle_index)
    cross_value = 1 - factor*Q**3/W
    return gy, gp, dict(original_beta_squared=float(original_value),
        algebraically_equal_cross_beta_squared=float(cross_value),
        evaluation_difference=float(cross_value-original_value),
        a=float(a), returned_ap=float(nu), phi=float(2*np.pi*angle_index/flow.q.N),
        angular_grid_size=int(flow.q.N), angle_index=int(angle_index),
        squared_speed=float(Q), squared_cross_product=float(W),
        direct_scalar_gradient=gp.tolist(), no_division_by_returned_ap=True,
        returned_ap_is_not_assumed_to_differentiate_a=True)


class HermiteDomainRow:
    """Sparse-support covector on the complete exact-coordinate chart."""
    def __init__(self, problem, state, interval, fraction, angle_index):
        self.problem, self.chart = problem, problem.chart
        self.interval, self.fraction, self.angle_index = int(interval), float(fraction), int(angle_index)
        if not 0 <= self.interval < self.chart.m - 1:
            raise ValueError("Use one actual original mesh interval")
        j, flow, n = self.interval, problem.flow, self.chart.n
        self.left, self.right = float(problem.x[j]), float(problem.x[j+1])
        self.h = self.right-self.left
        self.station = self.left + self.fraction*self.h
        h00, h10, h01, h11 = hermite_weights(self.fraction)
        y, f = state["y"], state["f"]
        if not state["finite"]:
            raise FloatingPointError("Only differentiate a currently valid complete warm")
        parameters = y[j, flow.parameter_slice]
        if not np.array_equal(parameters, y[j+1, flow.parameter_slice]):
            raise ValueError("The exact global-control chart was lost")
        # Match the actual original RMS interpolation.  A single local cell
        # uses the same neighboring values/RHS as the complete spline.
        spline = CubicHermiteSpline(problem.x[j:j+2], y[j:j+2], f[j:j+2], axis=0)
        query = spline(self.station)
        gy, gp_direct, self.local = local_margin_gradient(flow, self.station,
            query[:n], query[flow.parameter_slice], self.angle_index)
        if self.local["original_beta_squared"] <= 0:
            raise FloatingPointError("The protected actual query is not in the original positive domain")
        jac = flow.jac(problem.x[j:j+2], y[j:j+2].T)
        JL, JR = jac[:n, :n, 0], jac[:n, :n, 1]
        PL, PR = jac[:n, flow.parameter_slice, 0], jac[:n, flow.parameter_slice, 1]
        if (np.any(jac[:n, flow.core_slice, :] != 0)
                or not np.all(np.isfinite(jac))):
            raise ValueError("The original local RHS no longer has its declared finite constant-core structure")
        self.left_row = h00*gy + self.h*h10*(JL.T@gy)
        self.right_row = h01*gy + self.h*h11*(JR.T@gy)
        self.parameter_row = self.h*(h10*(PL.T@gy) + h11*(PR.T@gy)) + gp_direct
        # The whole global core appears through its exact inlet chart.
        # For a later local interval this explicit local core row is zero;
        # it remains free in the complete collocation optimization.
        self.core_row = self.chart.inlet.T@self.left_row if j == 0 else np.zeros(self.chart.free)
        self.coefficient_row = np.zeros(self.chart.size)
        if j > 0:
            self.coefficient_row[(j-1)*n:j*n] += self.left_row
        self.coefficient_row[j*n:(j+1)*n] += self.right_row
        begin = self.chart.physical_size
        self.coefficient_row[begin:begin+self.chart.free] += self.core_row
        self.coefficient_row[begin+self.chart.free:] += self.parameter_row
        self.scaled_row = self.coefficient_row/self.chart.scale
        if not np.all(np.isfinite(self.scaled_row)):
            raise FloatingPointError("The actual complete domain covector is nonfinite")
        # Independent Hermite value identity, not used to replace the
        # original spline's actual query or its domain value.
        algebraic = h00*y[j] + self.h*h10*f[j] + h01*y[j+1] + self.h*h11*f[j+1]
        self.description = dict(schema=SCHEMA, interval=j, left=self.left, right=self.right,
            fraction=self.fraction, station=self.station, local=self.local,
            physical_rows=n, exact_coordinate_dimension=self.chart.size,
            Hermite_weights=[h00, h10, h01, h11],
            original_spline_vs_hermite_value_max=float(np.max(abs(query-algebraic))),
            actual_nodal_physical_and_global_parameter_J_included=True,
            scalar_query_direct_parameter_gradient_included=True,
            exact_inlet_core_chain_included=True,
            fixed_physical_angle_not_a_differentiated_argmin=True,
            source_domain_check_replaced=False, new_scientific_acceptance_gate=False,
            left_row=self.left_row.tolist(), right_row=self.right_row.tolist(),
            free_core_row=self.core_row.tolist(), global_parameter_row=self.parameter_row.tolist(),
            scaled_covector_norm=float(np.linalg.norm(self.scaled_row)))

    def apply(self, coefficient_direction):
        return float(self.coefficient_row@np.asarray(coefficient_direction))

    def apply_scaled(self, scaled_direction):
        return float(self.scaled_row@np.asarray(scaled_direction))

    def original_value(self, augmented):
        """Recompute the REAL original nodal RHS before interpolating.

Complex augmented states are permitted for derivative checks.  They must
be obtained by lifting a real exact-coordinate direction, not by passing
complex coordinates through the chart's intentionally real expand().
"""
        flow, j = self.problem.flow, self.interval
        rhs = flow(self.problem.x, np.asarray(augmented).T).T
        if not np.all(np.isfinite(rhs)) or not np.all(np.isfinite(augmented)):
            return np.nan
        spline = CubicHermiteSpline(self.problem.x, augmented, rhs, axis=0)
        query = spline(self.station)
        return point_margin(flow, self.station, query[:flow.n],
            query[flow.parameter_slice], self.angle_index)

    def verify(self, state, steps=(2e-6, 1e-6, 5e-7)):
        rng = np.random.default_rng(26220261114)
        tests = []
        for kind in ("two-physical-endpoints", "global-core-and-controls", "all-exact-coordinates"):
            scaled = np.zeros(self.chart.size)
            if kind == "two-physical-endpoints":
                n, j = self.chart.n, self.interval
                start = max(0, (j-1)*n)
                scaled[start:(j+1)*n] = rng.standard_normal((j+1)*n-start)
            elif kind == "global-core-and-controls":
                scaled[self.chart.physical_size:] = rng.standard_normal(self.chart.free+self.chart.k)
            else:
                scaled[:] = rng.standard_normal(self.chart.size)
            coefficient = scaled/self.chart.scale
            lifted = self.chart.lift_direction(coefficient)
            predicted = self.apply(coefficient)
            complex_value = self.original_value(state["y"].astype(complex)+1j*1e-25*lifted)
            analytic = float(np.imag(complex_value)/1e-25)
            complex_finite = bool(np.isfinite(complex_value) and np.isfinite(predicted)
                and np.isfinite(analytic))
            relative = (abs(predicted-analytic)/max(1., abs(predicted), abs(analytic))
                if complex_finite else None)
            levels = []
            for step in steps:
                with np.errstate(invalid="ignore", divide="ignore", over="ignore"):
                    plus = self.original_value(state["y"]+step*lifted)
                    minus = self.original_value(state["y"]-step*lifted)
                finite = bool(np.isfinite(plus) and np.isfinite(minus))
                if finite:
                    difference = float((plus-minus)/(2*step))
                    levels.append(dict(step=step, finite=True, derivative=difference,
                        relative_error=abs(difference-predicted)/max(1., abs(difference), abs(predicted))))
                else:
                    levels.append(dict(step=step, finite=False))
            tests.append(dict(kind=kind, complete_gradient_action=predicted,
                original_complex_action=analytic if complex_finite else None,
                complex_finite=complex_finite, relative_error=relative, centered_levels=levels))
        finite = all(t["complex_finite"] for t in tests)
        maximum = max(t["relative_error"] for t in tests) if finite else None
        return dict(actual_original_query_gradient_checks=tests,
            maximum_complex_direction_relative_error=maximum,
            implementation_threshold=5e-5, implementation_check_passed=bool(finite and maximum < 5e-5),
            complete_original_nodal_RHS_recomputed=True,
            complex_chart_expand_not_used=True, native_tail_called=False,
            new_BVP_or_domain_acceptance_claimed=False)


class TangentProjector:
    """Orthogonal projection onto the retained optimizer-domain tangent rows.

The explicit small-row numerical rank policy affects only this temporary
optimization subspace.  It neither deletes an original collocation row nor
certifies a geometric rank.  One nonzero row needs no numerical rank choice.
"""
    def __init__(self, rows, dimension, relative_rank_threshold=1e-12):
        self.dimension = int(dimension)
        values = np.asarray(rows, float)
        if values.size == 0:
            values = np.empty((0, self.dimension))
        if values.ndim != 2 or values.shape[1] != self.dimension or len(values) > 8:
            raise ValueError("Supply at most eight complete scaled optimizer covectors")
        if not np.all(np.isfinite(values)) or not 0 < relative_rank_threshold < 1:
            raise ValueError("The optimizer rows and explicit rank policy must be finite")
        norms = np.linalg.norm(values, axis=1)
        nonzero = norms > 0
        self.rows = values
        normalized = values[nonzero]/norms[nonzero, None]
        if len(normalized) == 0:
            self.basis = np.empty((0, self.dimension)); singular = np.empty(0)
        elif len(normalized) == 1:
            self.basis = normalized.copy(); singular = np.array([1.])
        else:
            _, singular, vectors = np.linalg.svd(normalized, full_matrices=False)
            self.basis = vectors[singular > relative_rank_threshold*singular[0]]
        self.description = dict(input_rows=len(values), nonzero_rows=int(np.count_nonzero(nonzero)),
            tangent_codimension=len(self.basis), row_norms=norms.tolist(),
            normalized_row_singular_values=singular.tolist(),
            relative_rank_threshold=float(relative_rank_threshold),
            rank_policy_scope="Temporary optimizer subspace only; no original equation is removed",
            projection="P=I-Q.T@Q with orthonormal retained row basis Q",
            all_original_equations_and_acceptance_retained=True)

    def __call__(self, value):
        value = np.asarray(value)
        if value.shape != (self.dimension,):
            raise ValueError("A projected vector must retain all exact coordinates")
        return value - self.basis.T@(self.basis@value)

    def normalized_row_leak(self, value):
        value = np.asarray(value)
        if len(self.rows) == 0:
            return 0.
        scale = np.linalg.norm(self.rows, axis=1)*np.linalg.norm(value)
        return float(np.max(np.divide(abs(self.rows@value), scale,
            out=np.zeros(len(scale)), where=scale > 0)))


def projected_regularized_operator(operator, column_norm_squared, damping, projector):
    """Return [A P C^-1; damping P C^-1], C and its declared meaning.

Recover the scaled direction ONLY as projector(solution[0]/diagonal).
No damping I is substituted for damping P.  LSMR itself must use damp=0.
"""
    rows, columns = operator.shape
    norms = np.asarray(column_norm_squared)
    if (norms.shape != (columns,) or np.any(norms < 0) or not np.all(np.isfinite(norms))
            or not np.isfinite(damping) or damping <= 0 or projector.dimension != columns):
        raise ValueError("Use finite complete original column norms and positive damping")
    diagonal = np.sqrt(norms+damping*damping)

    def matvec(value):
        z = projector(np.asarray(value)/diagonal)
        return np.r_[operator@z, damping*z]

    def rmatvec(dual):
        dual = np.asarray(dual)
        return projector(operator.rmatvec(dual[:rows])+damping*dual[rows:])/diagonal

    result = LinearOperator((rows+columns, columns), dtype=float, matvec=matvec, rmatvec=rmatvec)
    description = dict(formula="[A P C^-1; damping P C^-1]",
        adjoint="C^-1 P (A.T w_top + damping w_bottom)",
        recovered_scaled_direction="z=P C^-1 v", LSMR_damp_argument=0.,
        penalty="damping^2 * ||z||^2; z=Pz",
        column_preconditioner="Positive diagonal sqrt(original UNPROJECTED column norms squared + damping^2)",
        projected_exact_column_norm_claimed=False,
        ambient_nullspace_is_redundant_parameterization=True,
        all_original_final_acceptance_gates_retained=True)
    return result, diagonal, description


def verify_projected_operator(operator, diagonal, projector, original_operator, damping):
    """Implementation check to call with the ACTUAL complete A in a warm run."""
    rng = np.random.default_rng(262112)
    vector = rng.standard_normal(operator.shape[1])
    dual = rng.standard_normal(operator.shape[0])
    forward, adjoint = operator@vector, operator.rmatvec(dual)
    left, right = float(forward@dual), float(vector@adjoint)
    error = abs(left-right)/max(1., np.linalg.norm(forward)*np.linalg.norm(dual),
        np.linalg.norm(vector)*np.linalg.norm(adjoint))
    z = projector(vector/diagonal)
    expected = np.r_[original_operator@z, damping*z]
    action_error = float(np.linalg.norm(forward-expected)/max(1., np.linalg.norm(expected)))
    leak = projector.normalized_row_leak(z)
    return dict(normwise_adjoint_error=float(error), complete_projected_action_relative_error=action_error,
        normalized_original_domain_row_leak=leak,
        declared_retained_row_basis_leak=float(np.linalg.norm(projector.basis@z)/max(1., np.linalg.norm(z))),
        implementation_threshold=5e-12,
        implementation_check_passed=bool(error < 5e-12 and action_error < 5e-12),
        no_BVP_acceptance_claim=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("accepted", "prepared", "tail-anchor", "tail-config", "warm", "out"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--interval", type=int, default=473)
    parser.add_argument("--fraction", type=float, default=0.17267316464601146)
    parser.add_argument("--angle-index", type=int, default=0)
    parser.add_argument("--angles", type=int, default=4096)
    parser.add_argument("--jac-workers", type=int, default=2)
    args = parser.parse_args()
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("All scientific calculations run in the public repository's Actions")
    for name, expected in warm_driver.EXPECTED.items():
        if sha(getattr(args, name)) != expected:
            raise ValueError("Use the actual preserved original input: "+name)
    for name, expected in warm_driver.original.FROZEN_SOURCES.items():
        if sha(HERE/name) != expected:
            raise ValueError("An original mathematical source changed: "+name)
    read = warm_driver.original.read
    original, saved, accepted, anchor = (read(p) for p in
        (args.prepared, args.warm, args.accepted, args.tail_anchor))
    identity = saved.get("optimization_warm", {})
    scalar = copy.deepcopy(saved["complete_scalar_profile"])
    scalar["frozen_design_parameters"] = original["complete_scalar_profile"]["frozen_design_parameters"]
    if (identity.get("schema") != warm_driver.SCHEMA
            or identity.get("source_prepared_sha256") != warm_driver.EXPECTED["prepared"]
            or saved["mesh"] != original["mesh"]
            or saved["field_representation"] != original["field_representation"]
            or scalar != original["complete_scalar_profile"]
            or not np.array_equal(np.asarray(saved["states"])[-1, -3:],
                saved["complete_scalar_profile"]["frozen_design_parameters"])):
        raise ValueError("Use a genuine saved warm of the exact original complete problem")
    expected_producers = {
        "geometry_20261114_constrained_trust_warm.py",
        "geometry_20261114_constrained_collocation.py",
        "geometry_20261114_full_dn_solve.py",
        "geometry_20261114_full_dn_augmented.py",
        "geometry_20261114_separated_qr_bvp.py",
        "geometry_20261114_physical_test_boundary.py",
        "geometry_20261114_full_dn_boundary.py",
        "geometry_20261114_lifted_modes_profile.py",
        "geometry_20261114_r225_free_core_bvp.py"}
    if set(identity.get("source_sha256", {})) != expected_producers:
        raise ValueError("The complete original warm producer ledger is required")
    for name, expected in identity.get("source_sha256", {}).items():
        if sha(HERE/name) != expected:
            raise ValueError("The consumed warm producer changed: "+name)
    profile, flow, boundary = warm_driver.setup(accepted, saved, anchor, args.angles, args.jac_workers)
    problem = CompleteResidual(np.asarray(saved["mesh"]), flow, boundary)
    coordinates = problem.chart.pack(np.asarray(saved["states"]))
    start = time.monotonic()
    state = problem.evaluate(coordinates, require_rms=True)
    row = HermiteDomainRow(problem, state, args.interval, args.fraction, args.angle_index)
    verification = row.verify(state)
    projector = TangentProjector([row.scaled_row], problem.chart.size)
    report = dict(schema=SCHEMA, scope=__doc__, query=row.description,
        implementation_verification=verification, projector=projector.description,
        actual_original_domain=state["report"], input_warm_sha256=sha(args.warm),
        original_input_sha256={name:sha(getattr(args, name)) for name in warm_driver.EXPECTED},
        source_sha256=sha(__file__), consumed_producer_sha256=identity["source_sha256"],
        frozen_original_source_sha256={name:sha(HERE/name) for name in warm_driver.original.FROZEN_SOURCES},
        seconds=time.monotonic()-start, actual_complete_linearization_built=False,
        projected_LSMR_run=False, new_warm_created=False, native_tail_called=False,
        full_BVP_solved=False, new_coupled_finite_acceptance=False)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+"\n")
    print(json.dumps(dict(query=row.description["local"],
        verification=verification["maximum_complex_direction_relative_error"],
        implementation_check_passed=verification["implementation_check_passed"],
        seconds=report["seconds"])), flush=True)
    return 0 if verification["implementation_check_passed"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
