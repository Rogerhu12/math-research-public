#!/usr/bin/env python3
"""R620 fixed-width, free-center original nineteen-state implicit BVP.

This is a new input and center chart, not a replay of the R605 mass solve or
the R616 finite-function continuation. Every scientific operation belongs
to this repository's public Actions. Initial A/rho are true integrals;
every accepted state also gets a separate actual-curve/history readout.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path

import numpy as np
from scipy.interpolate import BPoly, CubicSpline
from scipy.sparse import coo_matrix, diags
from scipy.sparse.linalg import lsmr, splu

import r620_original_center_time_jets_agent as center_map
import r625_tail_flat_compatible_input_agent as compatible_input

reduced, original = center_map.reduced, center_map.original
base, previous, paid = original.base, original.previous, original.paid
LD, Jet, emit = original.LD, original.Jet, original.emit


def identity(payload):
    raw = json.dumps(payload, separators=(",", ":"), allow_nan=False).encode()
    return {"json_bytes":len(raw), "json_sha256":hashlib.sha256(raw).hexdigest()}


class ClockCheckpoint(RuntimeError):
    """A declared public science boundary, distinct from a numerical rejection."""
    def __init__(self, record):
        self.record = record
        super().__init__("Public science clock checkpoint at "+record["where"])


class ScienceClock:
    def __init__(self, started, maximum_seconds, final_reserve_seconds):
        if not (maximum_seconds>final_reserve_seconds+60 and final_reserve_seconds>=30):
            raise ValueError("The declared science clock must retain its final output/readout reserve.")
        self.started = started
        self.maximum = float(maximum_seconds)
        self.reserve = float(final_reserve_seconds)
        self.phase = "ordinary_science"
        self.checks = 0
        self.events = []

    def elapsed(self):
        return time.monotonic()-self.started

    def remaining_total(self):
        return self.maximum-self.elapsed()

    def check(self, where):
        self.checks += 1
        limit = self.maximum if self.phase == "final_readout" else self.maximum-self.reserve
        elapsed = self.elapsed()
        if elapsed>=limit:
            record = {"where":where, "phase":self.phase, "elapsed_seconds":elapsed,
                      "declared_boundary_seconds":limit,
                      "maximum_science_seconds":self.maximum,
                      "final_reserve_seconds":self.reserve,
                      "last_accepted_state_is_preserved":True,
                      "not_a_mathematical_or_README_completion":True}
            self.events.append(record)
            emit("R620_PUBLIC_CLOCK_CHECKPOINT", record)
            raise ClockCheckpoint(record)

    def record(self):
        return {"maximum_science_seconds":self.maximum, "final_reserve_seconds":self.reserve,
                "ordinary_science_boundary_seconds":self.maximum-self.reserve,
                "checks":self.checks, "events":self.events,
                "elapsed_seconds":self.elapsed()}


class ClockedOriginalCoefficients:
    """Only deadline checks around the unchanged original coefficient calls."""
    def __init__(self, source, clock):
        self.source, self.clock = source, clock

    def __getattr__(self, name):
        return getattr(self.source, name)

    def evaluate_jets(self, *args):
        self.clock.check("before_original_coefficient_jet")
        result = self.source.evaluate_jets(*args)
        self.clock.check("after_original_coefficient_jet")
        return result

    def evaluate(self, *args):
        self.clock.check("before_original_coefficient_value")
        result = self.source.evaluate(*args)
        self.clock.check("after_original_coefficient_value")
        return result


class ClockedOriginalPotential:
    """Keep the exact original potential expression, with public boundaries."""
    def __init__(self, source, clock):
        self.source, self.clock = source, clock

    def __getattr__(self, name):
        return getattr(self.source, name)

    def center_difference(self, *args):
        self.clock.check("before_original_full_potential_difference")
        result = self.source.center_difference(*args)
        self.clock.check("after_original_full_potential_difference")
        return result


class CountedInterruptedFullHistory(original.FullHistory):
    """Include partially completed calls in elapsed cost; no formula changes."""
    def evaluate(self, curve):
        started, previous_seconds = time.monotonic(), self.seconds
        try:
            return super().evaluate(curve)
        finally:
            self.seconds = previous_seconds+time.monotonic()-started


class ObservedIntegralGrid:
    """The same polynomial Gauss prefix, including specified observation nodes.

    Observation nodes have zero quadrature weight. No interpolated history
    or trapezoid prefix substitutes for the true integral in a readout.
    """
    def __init__(self, panels, order, observations, clock):
        reduced.require_public_science()
        self.clock = clock
        self.clock.check("before_true_integral_grid")
        self.panels, self.order = int(panels), int(order)
        nodes, weights = np.polynomial.legendre.leggauss(order)
        local = (nodes+1)/2
        gauss = np.concatenate([(j+local)/panels for j in range(panels)])
        observations = np.asarray(observations, float)
        self.x = np.unique(np.r_[0., gauss, observations, 1.])
        self.observation_indices = np.searchsorted(self.x, observations)
        self.weights = np.zeros(len(self.x), dtype=LD)
        selected = np.searchsorted(self.x, gauss)
        self.weights[selected] = np.tile(weights/(2*panels), panels)
        leg = np.polynomial.legendre.legvander(nodes, order-1)
        coefficients = ((2*np.arange(order)+1)[:, None]/2
                        *leg.T*weights[None, :])
        self.prefix = np.zeros((len(self.x), len(self.x)), dtype=LD)
        for i, value in enumerate(self.x):
            self.clock.check("true_integral_prefix_row")
            if value == 1.:
                self.prefix[i] = self.weights
                continue
            panel = min(int(np.floor(value*panels)), panels-1)
            self.prefix[i, selected[:panel*order]] = self.weights[selected[:panel*order]]
            position = 2*(value*panels-panel)-1
            basis = np.polynomial.legendre.legvander(position, order)[0]
            antiderivative = np.zeros(order)
            antiderivative[0] = position+1
            for degree in range(1, order):
                antiderivative[degree] = (basis[degree+1]-basis[degree-1])/(2*degree+1)
            self.prefix[i, selected[panel*order:(panel+1)*order]] = (
                antiderivative@coefficients/(2*panels))
        self.clock.check("after_true_integral_grid")

    def integrate(self, rows):
        self.clock.check("before_original_polynomial_prefix_integration")
        result = original.IntegralGrid.integrate(self, rows)
        self.clock.check("after_original_polynomial_prefix_integration")
        return result




class ActualC2StateCurve:
    """One actual C2 curve through nodal h,k and their physical velocities.

    Shared nodal second derivatives define quintic Hermite pieces. They
    come from the nodal velocity splines, not the potentially enormous
    off-solution feedback accelerations. The center h''=a0,k''=0 is exact.
    The original equations and higher center jets are measured on this
    actual curve; interpolation never makes them true by declaration.
    """
    def __init__(self, x, states, parameters):
        reduced.require_public_science()
        self.length = float(parameters[-1])
        self.points = 0
        h, k, _, gamma, upsilon = np.asarray(states[:5], float)
        acceleration = CubicSpline(x, gamma).derivative()(x)/self.length
        curvature_acceleration = CubicSpline(x, upsilon).derivative()(x)/self.length
        acceleration[0], curvature_acceleration[0] = parameters[6], 0.
        self.h = BPoly.from_derivatives(x, np.column_stack((
            h, self.length*gamma, self.length**2*acceleration)))
        self.k = BPoly.from_derivatives(x, np.column_stack((
            k, self.length*upsilon, self.length**2*curvature_acceleration)))

    def shape(self, x):
        x = np.asarray(x, float).reshape(-1)
        self.points += len(x)
        return np.column_stack((self.h(x), self.k(x), self.h(x, 1),
                                self.k(x, 1), self.h(x, 2), self.k(x, 2)))

    def center_jets(self):
        return [float(self.h(0., 2)/self.length**2),
                float(self.k(0., 3)/self.length**3),
                float(self.h(0., 4)/self.length**4)]


class ActualHistoryReadouts:
    """Full true eta, A, rho and original ruling for one actual h/k curve."""
    def __init__(self, coefficients, potential, clock):
        self.clock = clock
        self.full = CountedInterruptedFullHistory(coefficients, potential)
        self.calls = self.points = 0
        self.completed = self.true_M_points = self.ruling_reassembly_rows = 0
        self.seconds = 0.

    def evaluate(self, model, chart, grid, stored=None):
        reduced.require_public_science()
        started = time.monotonic()
        self.calls += 1
        try:
            self.clock.check("before_actual_curve_true_history_readout")
            shape = model.shape(grid.x)
            self.points += len(grid.x)
            self.clock.check("after_actual_curve_shape")
            if not np.all(np.isfinite(shape)):
                raise FloatingPointError("The actual C2 shape is nonfinite.")
            rows = [[Jet(value, np.zeros(0)) for value in row] for row in shape]
            length = Jet(chart["physical_length"].value, np.zeros(0))
            eta = grid.integrate([[row[3]/(2*row[0])] for row in rows])
            geometry, acceleration = [], []
            for i, (h, k, hx, kx, hxx, kxx) in enumerate(rows):
                self.clock.check("actual_curve_geometry_point")
                geometry.append([h, k, eta[i][0], hx/length, kx/length])
                acceleration.append([hxx/length**2, kxx/length**2])
            actual_g = np.asarray([[value.value for value in row] for row in geometry], dtype=LD)
            if not (np.min(actual_g[:, 0])>LD('.8') and np.max(actual_g[:, 0])<3
                    and np.max(np.abs(actual_g[:, 1]))<2 and np.max(np.abs(actual_g[:, 2]))<1
                    and np.max(np.abs(actual_g[:, 3:5]))<6):
                raise FloatingPointError("The actual integrated C2 curve left the original physical box.")
            density_rows = []
            for row in geometry:
                self.clock.check("actual_curve_true_M_point")
                density_rows.append([length*value for value in paid.density(row)])
                self.true_M_points += 1
            primitive = grid.integrate(density_rows)
            center_a = [Jet(value.value, np.zeros(0)) for value in chart["center_history"]]
            history = [[center_a[j]+row[j] for j in range(8)] for row in primitive]
            curve = {"geometry":geometry, "history":history, "acceleration":acceleration,
                     "length":length, "grid":grid}
            data = self.full.evaluate(curve)
            physical_gauge = [Jet(value.value, np.zeros(0)) for value in chart["global_gauge"]]
            original_rows = []
            for i, (value, design) in enumerate(zip(data["base_ruling"], data["design"])):
                self.clock.check("actual_curve_original_ruling_reassembly")
                geo = geometry[i//2]
                delta0 = physical_gauge[0]-data["zeta0"]
                value = (value-2*paid.weights(geo)[0]*delta0
                         -design[0]*physical_gauge[1]-design[1]*physical_gauge[2])
                original_rows.append(value.value)
                self.ruling_reassembly_rows += 1
            actual_a = np.asarray([[value.value for value in row] for row in history], dtype=LD)
            actual_rho = np.asarray([[value.value for value in row] for row in data["rho"]], dtype=LD)
            actual_state = np.column_stack((actual_g, actual_a, actual_rho)).T
            at_nodes = actual_state[:, grid.observation_indices]
            end = np.r_[actual_a[-1], actual_g[-1, 3:5]]
            total = primitive[-1]
            H = chart["center_geometry"][0].value
            four = [total[1]/length, (8*total[3]+2*total[1])/length,
                    8*H**2*total[4]/length, 4*H**2*total[6]/length]
            op0 = np.asarray(original.jets_values(data["outputs"][0][0]), dtype=LD)
            center_E = op0[16:19]
            center_r = op0[12:15].copy()/4
            center_r[0] -= op0[15]*H
            nubar = np.asarray([value.value for value in physical_gauge], dtype=LD)
            nubar[0] -= H**2*nubar[2]
            mismatch = None if stored is None else {
                "eta":float(np.max(np.abs(at_nodes[2]-stored[2]))),
                "eight_A":float(np.max(np.abs(at_nodes[5:13]-stored[5:13]))),
                "six_rho":float(np.max(np.abs(at_nodes[13:19]-stored[13:19])))}
            higher = model.center_jets()
            report = {
                "actual_curve_type":type(model).__name__,
                "panels":grid.panels, "gauss_order":grid.order,
                "actual_curve_points":len(grid.x), "observation_nodes":len(grid.observation_indices),
                "all_eight_actual_terminal_A":np.asarray(actual_a[-1], float).tolist(),
                "all_six_actual_terminal_rho":np.asarray(actual_rho[-1], float).tolist(),
                "actual_terminal_velocities":np.asarray(actual_g[-1, 3:5], float).tolist(),
                "all_ten_actual_terminal_max":float(np.max(np.abs(end))),
                "four_original_even_integrals":[float(value.value) for value in four],
                "actual_original_ruling_max":float(np.max(np.abs(original_rows))),
                "actual_original_ruling_rms":float(np.sqrt(np.mean(np.asarray(original_rows, dtype=LD)**2))),
                "sampled_geometry_ranges":[[float(value.min()), float(value.max())] for value in actual_g.T],
                "true_history_minus_stored_at_same_nodes":mismatch,
                "actual_curve_center_a_j_f":higher,
                "center_chart_a_j_f":np.asarray(chart["parameters"][[6, 7, 8]], float).tolist(),
                "actual_center_E":np.asarray(center_E, float).tolist(),
                "actual_center_r":np.asarray(center_r, float).tolist(),
                "actual_global_zeta":np.asarray(chart["gauge_value"], float).tolist(),
                "actual_nubar":np.asarray(nubar, float).tolist(),
                "actual_nuhat":np.asarray(nubar-2*center_E, float).tolist(),
                "actual_original_nu":np.asarray(nubar-2*center_r, float).tolist(),
                "same_center_and_global_gauges_used_on_whole_curve":True,
                "all_history_fields_integrated_not_refitted":True,
                "sampled_values_are_not_continuous_error_bounds":True,
                "original_root_or_README_completion_claim":False,
                "seconds":time.monotonic()-started}
            self.clock.check("after_actual_curve_true_history_readout")
            self.completed += 1
            return {"states_at_observations":np.asarray(at_nodes, float), "report":report,
                    "model":model, "chart":chart}
        finally:
            self.seconds += time.monotonic()-started


class FullFeedbackCollocation:
    """All nineteen original ODEs; exact left-center elimination; ten end rows.

    No independent acceleration coordinates or history boundary projection
    are used. Stored histories remain collocation unknowns and must pay
    their differential equations plus the separate true-integral readout.
    """
    def __init__(self, x, coefficients, potential, clock):
        reduced.require_public_science()
        self.clock = clock
        self.x = np.asarray(x, float)
        self.intervals = (len(x)-1)//2
        self.h = self.x[2::2]-self.x[:-2:2]
        self.coefficients, self.potential = coefficients, potential
        self.size = 19*(len(x)-1)+10
        self.evaluations = self.jacobians = self.feedback_points = self.feedback_derivative_points = 0
        self.center_charts = self.center_time_coefficient_calls = 0
        self.center_chart_failures = 0
        self.center_seconds = self.feedback_seconds = 0.
        self.linear_attempts = self.linear_lsmr_iterations = 0
        self.linear_seconds = 0.

    def pack(self, states, parameters):
        return np.r_[np.asarray(states[:, 1:], float).ravel(order="F"), np.asarray(parameters, float)]

    def chart(self, parameters):
        # A single open branch of the exact R620 chart. These small numerical
        # margins protect its two denominators; they are not new root claims.
        self.clock.check("before_full_original_center_chart")
        H, v, _, _, _, _, a, _, _, _ = parameters
        if v>=-.05 or a-H*v*v/4<=.05:
            raise FloatingPointError("Outside this declared v<-.05, beta_second>.05 center branch.")
        self.center_charts += 1
        started = time.monotonic()
        try:
            result = center_map.build_center_chart(parameters, self.coefficients, self.potential, True)
            self.center_time_coefficient_calls += result["receipt"]["coefficient_time_parameter_evaluations"]
            self.clock.check("after_full_original_center_chart")
            return result
        except Exception:
            self.center_chart_failures += 1
            raise
        finally:
            self.center_seconds += time.monotonic()-started

    def evaluate(self, z):
        self.evaluations += 1
        parameters = np.asarray(z[-10:], float)
        chart = self.chart(parameters)
        states = np.column_stack((np.asarray(chart["initial_value"], float),
                                  np.asarray(z[:-10], float).reshape(19, len(self.x)-1, order="F")))
        rhs = center_map.FullPhysicalFeedback(chart, self.coefficients, self.potential)
        outputs = []
        try:
            for state in states.T:
                self.clock.check("before_original_feedback_point")
                outputs.append(rhs.evaluate(state, False))
                self.clock.check("after_original_feedback_point")
        finally:
            self.feedback_points += rhs.evaluations
            self.feedback_seconds += rhs.seconds
        flow = np.asarray([row["value"] for row in outputs], dtype=LD).T
        mid = (states[:, 1::2]-(states[:, :-2:2]+states[:, 2::2])/2
               +self.h*(flow[:, 2::2]-flow[:, :-2:2])/8)/self.h
        total = ((states[:, 2::2]-states[:, :-2:2])/self.h
                 -(flow[:, :-2:2]+4*flow[:, 1::2]+flow[:, 2::2])/6)
        differential = np.column_stack([np.r_[mid[:, i], total[:, i]]
                                       for i in range(self.intervals)]).ravel(order="F")
        terminal, _ = rhs.terminal_rows(states[:, -1])
        residual = np.r_[differential, terminal]
        if not np.all(np.isfinite(residual)):
            raise FloatingPointError("Nonfinite original full-feedback BVP residual.")
        return {"z":np.asarray(z, float).copy(), "states":states, "parameters":parameters,
                "chart":chart, "rhs":rhs, "flow":flow, "outputs":outputs,
                "differential":differential, "terminal":terminal,
                "residual":residual, "norm":float(np.linalg.norm(residual)),
                "component_max":np.maximum(np.max(np.abs(mid), axis=1),
                                            np.max(np.abs(total), axis=1))}

    def jacobian(self, current):
        self.jacobians += 1
        rhs = current["rhs"]
        before_calls, before_seconds = rhs.evaluations, rhs.seconds
        outputs = []
        try:
            for state in current["states"].T:
                self.clock.check("before_original_feedback_Jacobian_point")
                outputs.append(rhs.evaluate(state, True))
                self.clock.check("after_original_feedback_Jacobian_point")
        finally:
            calls = rhs.evaluations-before_calls
            self.feedback_points += calls
            self.feedback_derivative_points += calls
            self.feedback_seconds += rhs.seconds-before_seconds
        fy = np.asarray([row["state_jacobian"] for row in outputs], float)
        fp = np.asarray([row["parameter_jacobian"] for row in outputs], float)
        center_jac = np.asarray(current["chart"]["initial_parameter_jacobian"], float)
        rows, columns, values = [], [], []
        parameter_column = self.size-10

        def block(row, col, matrix):
            rr, cc = np.indices(matrix.shape)
            rows.extend((row+rr.ravel()).tolist())
            columns.extend((col+cc.ravel()).tolist())
            values.extend(matrix.ravel().tolist())

        def node_block(row, node, state_coefficient, flow_coefficient):
            state_matrix = state_coefficient*np.eye(19)+flow_coefficient*fy[node]
            if node == 0:
                block(row, parameter_column, state_matrix@center_jac+flow_coefficient*fp[node])
            else:
                block(row, 19*(node-1), state_matrix)
                block(row, parameter_column, flow_coefficient*fp[node])

        for interval, width in enumerate(self.h):
            self.clock.check("original_global_Jacobian_interval")
            left, middle, right = 2*interval, 2*interval+1, 2*interval+2
            row = 38*interval
            node_block(row, left, -.5/width, -.125)
            node_block(row, middle, 1/width, 0.)
            node_block(row, right, -.5/width, .125)
            node_block(row+19, left, -1/width, -1/6)
            node_block(row+19, middle, 0., -2/3)
            node_block(row+19, right, 1/width, -1/6)
        _, end_selector = rhs.terminal_rows(current["states"][:, -1])
        block(38*self.intervals, 19*(len(self.x)-2), np.asarray(end_selector, float))
        matrix = coo_matrix((values, (rows, columns)), shape=(self.size, self.size)).tocsc()
        matrix.eliminate_zeros()
        if not np.all(np.isfinite(matrix.data)):
            raise FloatingPointError("Nonfinite complete original nineteen-state Jacobian.")
        return matrix

    def newton_direction(self, current, matrix, damping):
        started = time.monotonic()
        self.linear_attempts += 1
        try:
            self.clock.check("before_original_global_linear_solve")
            result = self._newton_direction_core(current, matrix, damping)
            self.linear_lsmr_iterations += result[1]["lsmr_iterations"]
            self.clock.check("after_original_global_linear_solve")
            return result
        finally:
            self.linear_seconds += time.monotonic()-started

    def _newton_direction_core(self, current, matrix, damping):
        """Every full Newton direction pays the original ten linear end rows.

        A shortened trial reduces those rows by the same fraction. This is
        a step constraint, not an initial A(L)=0 projection. LU/LSMR row and
        column scaling is linear preconditioning only; merit stays unscaled.
        """
        end_indices = np.asarray([*range(5, 13), 3, 4])+19*(len(self.x)-2)
        free = np.ones(self.size, dtype=bool)
        free[end_indices] = False
        known = -np.asarray(current["terminal"], float)
        ode = matrix[:-10]
        target = -np.asarray(current["differential"], float)-ode[:, end_indices]@known
        reduced_matrix = ode[:, free].tocsc()
        row_scale = 1/np.maximum(1.e-30, np.asarray(abs(reduced_matrix).max(axis=1).toarray()).ravel())
        scaled = diags(row_scale)@reduced_matrix
        column_scale = 1/np.maximum(1.e-30, np.asarray(abs(scaled).max(axis=0).toarray()).ravel())
        equilibrated = (scaled@diags(column_scale)).tocsc()
        started = time.monotonic()
        method, iterations, linear_error = "sparse_lu", 0, None
        try:
            factor = splu(equilibrated)
            solution = factor.solve(row_scale*target)
            if not np.all(np.isfinite(solution)):
                raise FloatingPointError("Nonfinite equilibrated original Newton solution.")
        except (RuntimeError, ValueError, FloatingPointError) as error:
            method, linear_error = "damped_lsmr_after_lu_failure", type(error).__name__+":"+str(error)
            result = lsmr(equilibrated, row_scale*target, damp=np.sqrt(damping),
                          atol=1.e-11, btol=1.e-11, maxiter=1600)
            solution, iterations = result[0], int(result[2])
        direction = np.zeros(self.size)
        direction[free] = column_scale*solution
        direction[end_indices] = known
        if not np.all(np.isfinite(direction)):
            raise FloatingPointError("The full original Newton step is nonfinite.")
        remainder = matrix@direction+np.asarray(current["residual"], float)
        return direction, {"method":method, "lsmr_iterations":iterations,
                           "linear_error":linear_error,
                           "original_linear_remainder_max":float(np.max(np.abs(remainder))),
                           "unscaled_direction_infinity_norm":float(np.max(np.abs(direction))),
                           "all_ten_linear_end_rows_paid":True,
                           "seconds":time.monotonic()-started}


def collocation_converged(current, args):
    """Only the original nineteen collocation rows and ten stored end rows."""
    return bool(np.max(np.abs(current["differential"]))<=args.ode_tol
                and np.max(np.abs(current["terminal"]))<=args.end_tol)


def actual_converged(current, actual, args):
    report = actual["report"]
    mismatch = report["true_history_minus_stored_at_same_nodes"]
    return bool(collocation_converged(current, args)
                and report["all_ten_actual_terminal_max"]<=args.end_tol
                and report["actual_original_ruling_max"]<=args.ruling_tol
                and mismatch is not None and max(mismatch.values())<=args.ode_tol)


def checkpoint(system, current, actual, iteration, reason, counters, trust, damping):
    payload = {"parameters":current["parameters"].tolist(), "x":system.x.tolist(),
               "original_nineteen_states":current["states"].tolist()}
    cached = [value for row in current["outputs"] for value in row["cached_original_ruling_reassembly"]]
    emit("R620_FULL_FEEDBACK_STATE", {
        "iteration":iteration, "reason":reason, "state":payload,
        "state_identity":identity(payload), "unknowns":system.size,
        "original_differential_max":float(np.max(np.abs(current["differential"]))),
        "all_nineteen_original_differential_component_max":np.asarray(current["component_max"], float).tolist(),
        "all_ten_original_terminal_rows":np.asarray(current["terminal"], float).tolist(),
        "unscaled_original_merit_norm":current["norm"],
        "cached_feedback_ruling_reassembly_max":float(np.max(np.abs(cached))),
        "cached_reassembly_is_not_actual_curve_or_error_certificate":True,
        "center_chart":current["chart"]["receipt"],
        "actual_C2_curve_with_true_histories":actual["report"],
        "counters":dict(counters), "trust":trust, "damping":damping,
        "full_original_root_or_README_completion_claim":False})


def fixed_curve_refinement(retained, histories, args, clock):
    """Use the final reserve only when a concrete previous cost allows entry.

    The estimate is not an upper-bound proof: every field call still checks
    the total deadline. A partial fine readout is marked pending and never
    replayed during this process.
    """
    current, actual, system = retained["current"], retained["actual"], retained["system"]
    estimate = max(30., 3*actual["report"]["seconds"])
    enough = clock.remaining_total()>estimate+15.
    record = {"state":"pending", "attempted":False, "entry_considered":True,
              "physical_parameter_identity":identity(current["parameters"].tolist()),
              "remaining_science_seconds":clock.remaining_total(),
              "estimated_readout_seconds":estimate,
              "estimate_is_not_a_rigorous_time_bound":True,
              "reason":"pending_final_fixed_curve_readout" if enough else "insufficient_declared_final_reserve"}
    retained["fixed_refinement"] = record
    if not enough:
        emit("R620_FIXED_REFINEMENT_PENDING", record)
        return None
    record["attempted"] = True
    previous_phase = clock.phase
    clock.phase = "final_readout"
    try:
        clock.check("before_fixed_actual_curve_refinement")
        panels = len(system.x)-1
        fine_x = np.linspace(0., 1., 2*panels+1)
        fine_grid = ObservedIntegralGrid(panels, args.order, fine_x, clock)
        refined = histories.evaluate(actual["model"], current["chart"], fine_grid)
        clock.check("after_fixed_actual_curve_refinement")
        record.update(state="completed", reason="same_curve_same_center_same_three_gauges",
                      actual_fine_report=refined["report"])
        emit("R620_FIXED_ACTUAL_CURVE_REFINEMENT", {
            "physical_parameters_held":current["parameters"].tolist(),
            "physical_global_zeta_held":np.asarray(current["chart"]["gauge_value"], float).tolist(),
            "coarse":actual["report"], "fine":refined["report"],
            "length_center_or_global_gauges_refitted":False,
            "continuous_or_README_completion_claim":False})
        return fine_x, fine_grid, refined
    except ClockCheckpoint as error:
        record.update(state="pending", reason="public_clock_during_fixed_fine_readout",
                      checkpoint=error.record)
        emit("R620_FIXED_REFINEMENT_PENDING", record)
        raise
    except Exception as error:
        record.update(state="pending", reason="fixed_fine_readout_exception",
                      error=type(error).__name__+":"+str(error))
        emit("R620_FIXED_REFINEMENT_PENDING", record)
        raise
    finally:
        clock.phase = previous_phase


def solve(system, states, parameters, histories, grid, args, retained, level=0):
    started = time.monotonic()
    counters = {"accepted":0, "rejected":0, "complete_trials":0, "trial_attempts":0,
                "domain_or_chart_rejections":0, "actual_curve_rejections":0,
                "linear_solves":0, "lsmr_iterations":0}
    current = system.evaluate(system.pack(states, parameters))
    if "current" not in retained:
        retained.update(system=system, current=current, counters=counters)
        retained["fixed_refinement"] = {"state":"pending", "attempted":False,
                                         "reason":"new_original_BVP_state"}
    curve = ActualC2StateCurve(system.x, current["states"], current["parameters"])
    actual = histories.evaluate(curve, current["chart"], grid, current["states"])
    retained.update(system=system, current=current, actual=actual, counters=counters)
    retained["fixed_refinement"] = {"state":"pending", "attempted":False,
                                     "reason":"new_complete_original_BVP_state"}
    trust, damping = args.trust, args.damping
    checkpoint(system, current, actual, 0, "new_original_feedback_BVP_entry", counters, trust, damping)
    status = "original_feedback_iteration_budget_reached"
    iteration = 0
    for iteration in range(1, args.iterations+1):
        system.clock.check("before_original_BVP_iteration")
        if collocation_converged(current, args):
            status = ("original_feedback_and_true_integral_discrete_gates_met"
                      if actual_converged(current, actual, args) else
                      "original_collocation_converged_actual_curve_gates_pending")
            break
        matrix = system.jacobian(current)
        direction, linear = system.newton_direction(current, matrix, damping)
        counters["linear_solves"] += 1
        counters["lsmr_iterations"] += linear["lsmr_iterations"]
        initial_fraction = min(1., trust/max(1.e-30, np.max(np.abs(direction))))
        accepted = False
        for backtrack in range(args.trials):
            system.clock.check("before_original_BVP_backtrack")
            fraction = initial_fraction*2.**-backtrack
            trial_info = {"level":level, "iteration":iteration, "backtrack":backtrack,
                          "fraction":fraction, "linear":linear if backtrack == 0 else None}
            counters["trial_attempts"] += 1
            retained["inflight_trial"] = {"level":level, "iteration":iteration,
                "backtrack":backtrack, "fraction":fraction,
                "phase":"original_full_field_evaluation",
                "physical_parameters":(current["parameters"]+fraction*direction[-10:]).tolist()}
            try:
                trial = system.evaluate(current["z"]+fraction*direction)
                counters["complete_trials"] += 1
            except (FloatingPointError, ValueError, OverflowError) as error:
                counters["rejected"] += 1
                counters["domain_or_chart_rejections"] += 1
                emit("R620_FULL_FEEDBACK_TRIAL", {**trial_info, "accepted":False,
                     "reason":"original_field_or_chart_domain", "error":type(error).__name__+":"+str(error)})
                retained.pop("inflight_trial", None)
                continue
            old_end = float(np.max(np.abs(current["terminal"])))
            new_end = float(np.max(np.abs(trial["terminal"])))
            good = (trial["norm"]<current["norm"]*(1-1.e-4*fraction)
                    and new_end<=old_end+1.e-13*max(1., old_end))
            trial_actual = None
            if good:
                retained["inflight_trial"]["phase"] = "actual_curve_true_history_readout"
                try:
                    candidate_curve = ActualC2StateCurve(system.x, trial["states"], trial["parameters"])
                    trial_actual = histories.evaluate(candidate_curve, trial["chart"], grid, trial["states"])
                except (FloatingPointError, ValueError, OverflowError) as error:
                    good = False
                    counters["actual_curve_rejections"] += 1
                    trial_info["actual_curve_error"] = type(error).__name__+":"+str(error)
            emit("R620_FULL_FEEDBACK_TRIAL", {**trial_info, "accepted":good,
                 "unscaled_original_merit_norm":trial["norm"],
                 "original_differential_max":float(np.max(np.abs(trial["differential"]))),
                 "all_ten_original_terminal_max":new_end,
                 "actual_curve_ruling_max":None if trial_actual is None else trial_actual["report"]["actual_original_ruling_max"]})
            retained.pop("inflight_trial", None)
            if good:
                previous_norm = current["norm"]
                current, actual = trial, trial_actual
                counters["accepted"] += 1
                accepted = True
                if backtrack == 0 and current["norm"]<.8*previous_norm:
                    trust = min(args.maximum_trust, 1.5*trust)
                elif backtrack:
                    trust = max(args.minimum_trust, .5*trust)
                damping = max(1.e-12, damping/3)
                retained.update(system=system, current=current, actual=actual, counters=counters)
                retained["fixed_refinement"] = {"state":"pending", "attempted":False,
                                                 "reason":"new_accepted_original_BVP_state"}
                checkpoint(system, current, actual, iteration, "accepted_original_feedback_merit", counters, trust, damping)
                break
            counters["rejected"] += 1
        if not accepted:
            trust *= .25
            damping = min(1.e12, 10*damping)
            if trust<args.minimum_trust:
                status = "original_feedback_current_input_stalled"
                break
    if collocation_converged(current, args):
        status = ("original_feedback_and_true_integral_discrete_gates_met"
                  if actual_converged(current, actual, args) else
                  "original_collocation_converged_actual_curve_gates_pending")
    checkpoint(system, current, actual, iteration, status, counters, trust, damping)
    summary = {"status":status, "level":level, "counters":dict(counters),
               "original_collocation_and_stored_end_gate":collocation_converged(current, args),
               "all_actual_curve_and_true_history_gates":actual_converged(current, actual, args),
               "actual_last_trust":trust, "actual_last_damping":damping,
               "seconds":time.monotonic()-started}
    emit("R620_FULL_FEEDBACK_LEVEL_FINAL", summary)
    return current, actual, summary


def main():
    reduced.require_public_science()
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--intervals", type=int, default=32)
    parser.add_argument("--order", type=int, default=16)
    parser.add_argument("--iterations", type=int, default=60)
    parser.add_argument("--trials", type=int, default=8)
    parser.add_argument("--trust", type=float, default=.25)
    parser.add_argument("--maximum-trust", type=float, default=1.)
    parser.add_argument("--minimum-trust", type=float, default=1.e-8)
    parser.add_argument("--damping", type=float, default=1.e-6)
    parser.add_argument("--ode-tol", type=float, default=1.e-7)
    parser.add_argument("--end-tol", type=float, default=1.e-8)
    parser.add_argument("--ruling-tol", type=float, default=1.e-7)
    parser.add_argument("--maximum-science-seconds", type=float, default=3300.)
    parser.add_argument("--final-reserve-seconds", type=float, default=180.)
    args = parser.parse_args()
    request = json.loads(Path(args.input).read_text())
    started = time.monotonic()
    clock = ScienceClock(started, args.maximum_science_seconds, args.final_reserve_seconds)
    emit("R620_DECLARED_PUBLIC_CLOCK", clock.record())
    coefficients = potential = histories = model = None
    input_progress = {}
    systems, summaries, retained = [], [], {}
    status, exception = "not_initialized", None
    try:
        clock.check("before_necessary_original_definition")
        labels, rows = previous.rebuild_known_rows()
        clock.check("after_necessary_original_definition")
        mother = base.WideReferenceGrid(192, 8, 5.)
        clock.check("after_necessary_original_mother")
        coefficients = ClockedOriginalCoefficients(base.CountedCoefficients(labels, rows, mother), clock)
        clock.check("after_necessary_original_coefficient_table")
        potential = ClockedOriginalPotential(previous.FactoredPotential(mother), clock)
        clock.check("after_necessary_original_full_Gram")
        emit("R620_NECESSARY_SAME_MOTHER", {"coefficients":coefficients.stats,
             "full_positive_Gram":potential.stats, "graph":mother.graph_info,
             "full_positive_potential_coefficient":1,
             "old_identity_directional_or_quadrature_comparison_replayed":False})
        histories = ActualHistoryReadouts(coefficients, potential, clock)
        x = np.linspace(0., 1., 2*args.intervals+1)
        grid = ObservedIntegralGrid(args.intervals, args.order, x, clock)
        model = compatible_input.TailFlatCompatibleFreeCenterInput(clock, input_progress)
        system = FullFeedbackCollocation(x, coefficients, potential, clock)
        systems.append(system)
        chart = system.chart(model.parameters)
        seed = histories.evaluate(model, chart, grid)
        emit("R620_TRUE_FREE_CENTER_INPUT", {
            "physical_parameters":model.parameters.tolist(),
            "R625_unique_tail_flat_input":model.input_receipt,
            "parameter_identity":identity(model.parameters.tolist()),
            "complete_analytic_input_formula":request["actual_initial_state"]["analytic_curve"],
            "center_chart":chart["receipt"], "actual_true_history_seed":seed["report"],
            "initial_history_boundary_projection_performed":False,
            "old_guide_fit_or_optimizer_checkpoint_replayed":False,
            "old_R616_state_is_not_claimed_as_this_input":True,
            "original_scope":"full nineteen-state ODE with all eight A and two velocity end rows"})
        current, actual, summary = solve(system, seed["states_at_observations"], model.parameters,
                                         histories, grid, args, retained)
        summaries.append(summary)
        status = summary["status"]
        refined_result = fixed_curve_refinement(retained, histories, args, clock)
        # Once this mesh's original collocation problem is solved, a finer
        # original BVP may address the observed actual-curve/history defect.
        # The full actual-curve root gate remains separately unchanged.
        if collocation_converged(current, args) and refined_result is not None:
            clock.check("before_conditional_second_original_BVP_mesh")
            fine_x, fine_grid, refined = refined_result
            emit("R620_CONDITIONAL_MESH_REFINEMENT", {
                "original_collocation_and_stored_end_gate":True,
                "all_actual_curve_and_true_history_gates":actual_converged(current, actual, args),
                "reason":"resolve_or_measure_actual_curve_discretization_defect",
                "physical_parameters_held_for_new_initial_state":current["parameters"].tolist(),
                "new_initial_histories_are_true_fixed_curve_integrals":True,
                "root_standard_lowered":False})
            system2 = FullFeedbackCollocation(fine_x, coefficients, potential, clock)
            systems.append(system2)
            current, actual, summary = solve(system2, refined["states_at_observations"],
                current["parameters"], histories, fine_grid, args, retained, level=1)
            summaries.append(summary)
            status = summary["status"]
            fixed_curve_refinement(retained, histories, args, clock)
    except ClockCheckpoint as error:
        status = "public_clock_checkpoint_with_last_accepted_state_preserved"
        exception = {"type":type(error).__name__, "message":str(error), "record":error.record}
    except Exception as error:
        status = "new_original_feedback_input_failed_with_last_state_preserved"
        exception = {"type":type(error).__name__, "message":str(error)}
        emit("R620_FULL_FEEDBACK_EXCEPTION", {**exception,
             "latest_finite_accepted_state_retained":bool(retained.get("current"))})
    # After an ordinary-work checkpoint, use only the declared final reserve.
    # A started or failed fine readout is never replayed in this process.
    if (histories is not None and "actual" in retained
            and retained.get("fixed_refinement", {}).get("state")!="completed"
            and not retained.get("fixed_refinement", {}).get("entry_considered", False)):
        try:
            fixed_curve_refinement(retained, histories, args, clock)
        except ClockCheckpoint as error:
            status = "public_clock_checkpoint_with_last_accepted_state_preserved"
            if exception is None:
                exception = {"type":type(error).__name__, "message":str(error), "record":error.record}
        except Exception as error:
            if exception is None:
                exception = {"type":type(error).__name__, "message":str(error)}
    last_state = None if "current" not in retained else {
        "parameters":retained["current"]["parameters"].tolist(),
        "x":retained["system"].x.tolist(),
        "original_nineteen_states":retained["current"]["states"].tolist()}
    final = {
        "status":status, "exception":exception, "summaries":summaries,
        "new_input_evaluation":input_progress,
        "analytic_input_shape_points":None if model is None else model.points,
        "actual_last_full_state":last_state,
        "actual_last_full_state_identity":None if last_state is None else identity(last_state),
        "actual_last_parameters":None if "current" not in retained else retained["current"]["parameters"].tolist(),
        "actual_last_original_differential_max":None if "current" not in retained else float(np.max(np.abs(retained["current"]["differential"]))),
        "actual_last_original_terminal_rows":None if "current" not in retained else np.asarray(retained["current"]["terminal"], float).tolist(),
        "actual_last_true_curve_report":None if "actual" not in retained else retained["actual"]["report"],
        "retained_counters":retained.get("counters"),
        "inflight_trial_at_checkpoint":retained.get("inflight_trial"),
        "actual_last_collocation_and_stored_end_gate":None if "current" not in retained else collocation_converged(retained["current"], args),
        "actual_last_all_true_curve_gates":None if "actual" not in retained else actual_converged(retained["current"], retained["actual"], args),
        "fixed_actual_curve_refinement_status":retained.get("fixed_refinement", {
            "state":"pending", "attempted":False, "reason":"no_complete_actual_curve_retained"}),
        "public_science_clock":clock.record(),
        "coefficient_jet_calls":None if coefficients is None else coefficients.jet_calls,
        "coefficient_value_calls":None if coefficients is None else coefficients.value_calls,
        "center_chart_calls":sum(system.center_charts for system in systems),
        "center_chart_failures":sum(system.center_chart_failures for system in systems),
        "center_time_coefficient_calls":sum(system.center_time_coefficient_calls for system in systems),
        "center_chart_seconds":sum(system.center_seconds for system in systems),
        "full_feedback_state_points":sum(system.feedback_points for system in systems),
        "full_feedback_derivative_state_points":sum(system.feedback_derivative_points for system in systems),
        "full_feedback_seconds":sum(system.feedback_seconds for system in systems),
        "collocation_evaluations":sum(system.evaluations for system in systems),
        "complete_Jacobian_evaluations":sum(system.jacobians for system in systems),
        "all_linear_solve_attempts":sum(system.linear_attempts for system in systems),
        "all_linear_solve_seconds":sum(system.linear_seconds for system in systems),
        "all_known_lsmr_iterations":sum(system.linear_lsmr_iterations for system in systems),
        "actual_true_history_readouts":None if histories is None else histories.calls,
        "completed_actual_true_history_readouts":None if histories is None else histories.completed,
        "actual_true_history_points":None if histories is None else histories.points,
        "actual_true_M_points":None if histories is None else histories.true_M_points,
        "actual_original_ruling_reassembly_rows":None if histories is None else histories.ruling_reassembly_rows,
        "actual_true_history_seconds":None if histories is None else histories.seconds,
        "full_history_calls":None if histories is None else histories.full.evaluations,
        "full_history_seconds":None if histories is None else histories.full.seconds,
        "new_science_seconds":time.monotonic()-started,
        "raw_tables_trajectories_artifacts_or_releases_saved":False,
        "prior_R601_R605_R616_costs_not_erased":request["prior_cost_ledger"],
        "root_or_README_completion_claim":False}
    emit("R620_FULL_FEEDBACK_FINAL", final)


if __name__ == "__main__":
    main()
