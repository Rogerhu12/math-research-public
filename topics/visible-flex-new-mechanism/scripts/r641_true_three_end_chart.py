#!/usr/bin/env python3
"""R638/R641: actual scalar P root, exact amplitude/length chain, 256 shapes.

No original end is assigned a zero value. All ten are reconstructed from
the same full densities. The root and algebraic graph are numerical inputs
to the original BVP; continuous integral error is not certified by them.
"""
from __future__ import annotations

from collections import defaultdict
import math
import time

import numpy as np

import r636_polynomial_background_kinetic_chart as background
import r632_adaptive_polynomial_boxes as adaptive

legacy, reduced, original, paid = background.legacy, background.reduced, background.original, background.paid
LD, Jet = background.LD, background.Jet
IntegralGrid, identity, ld_text = background.IntegralGrid, background.identity, background.ld_text
COUNTS = defaultdict(float)


class ScalarRootPending(RuntimeError):
    def __init__(self, record):
        super().__init__("Actual scalar P root remains unfinished, not zero or infeasible")
        self.record = record


class DependentEndsPending(RuntimeError):
    def __init__(self, record):
        super().__init__("Actual eliminated original ends exceed their unchanged original tolerance")
        self.record = record


def sigma(x, derivative=0):
    x = np.asarray(x, dtype=LD)
    answer = np.zeros(x.shape, dtype=LD)
    selected = x >= LD(1)/4
    coefficients = np.polynomial.polynomial.polyder(np.asarray([0,0,0,10,-15,6], dtype=LD), m=derivative)
    answer[selected] = np.polynomial.polynomial.polyval((4*x[selected]-1)/3, coefficients)*(LD(4)/3)**derivative
    return answer


class BackgroundPolynomialBoxes(adaptive.AdaptivePolynomialBoxes):
    def physical_coefficients(self, graph, extended, alpha, length):
        h = adaptive.affine_coefficients(graph.extended_h_coeff, extended, graph.background_h_coeff)
        kappa = adaptive.affine_coefficients(graph.extended_k_coeff, extended, graph.background_k_coeff)
        return {"h":h, "k":adaptive.positive_scale(kappa, alpha),
            "gamma":adaptive.positive_divide(adaptive.derivative(h, self.knots), length),
            "upsilon":adaptive.positive_divide(adaptive.positive_scale(
                adaptive.derivative(kappa, self.knots), alpha), length)}


class ThreeEndChart:
    def __init__(self, knots, grid, clock, root_radius=.1, root_tolerance=1.e-13,
                 root_width=1.e-10, root_iterations=64, maximum_nodes=32768, maximum_depth=40,
                 original_end_tolerance=1.e-8):
        reduced.require_public_science()
        started = time.monotonic()
        self.base = background.PolynomialBackgroundChart(knots, grid, clock)
        self.n, self.dimension = self.base.n, self.base.dimension-1
        self.knots, self.grid, self.clock, self.c = self.base.knots, grid, clock, self.base.c
        self.root_radius, self.root_tolerance, self.root_width = LD(root_radius), LD(root_tolerance), LD(root_width)
        self.root_iterations = int(root_iterations)
        self.original_end_tolerance = LD(original_end_tolerance)
        self.evaluations = self.jet_evaluations = 0
        self.latest_geometry = self.latest_curve = self.last_parameters = None
        self.latest_scalar_root = self.last_control = None
        self.cache_parameters = self.cache_curve = None
        self.sigma = [sigma(grid.x, j) for j in range(3)]
        endpoint = np.zeros(self.dimension, dtype=LD)
        endpoint[self.n-1] = 1
        self.h_basis = [v[:, :self.dimension]-s[:, None]*endpoint[None, :]
                        for v, s in zip(self.base.h_basis, self.sigma)]
        self.k_basis = [v[:, :self.dimension] for v in self.base.k_basis]
        left, width = np.asarray(self.knots[:-1], dtype=LD), LD(1)/64
        sc = np.zeros((6, len(left)), dtype=LD)
        for j in range(6):
            term = sigma(left, j)*width**j/LD(math.factorial(j))
            for i in range(j, 6):
                sc[i] += (LD(math.comb(i,j))/math.comb(5,j))*term
        self.sigma_coeff = sc
        self.background_h_coeff = self.base.background_h_coeff[0]
        self.background_k_coeff = self.base.background_k_coeff[0]
        hc = self.base.h_coeff[0][:, :, :self.dimension]-sc[:, :, None]*endpoint[None, None, :]
        kc = self.base.k_coeff[0][:, :, :self.dimension]
        self.extended_h_coeff = np.concatenate((hc, sc[:, :, None]), axis=2)
        self.extended_k_coeff = np.concatenate((kc, np.zeros_like(sc[:, :, None])), axis=2)
        self.boxes = BackgroundPolynomialBoxes(knots, clock, maximum_nodes, maximum_depth)
        COUNTS["complete_256_shape_basis_constructions"] += 1
        COUNTS["complete_256_shape_basis_seconds"] += time.monotonic()-started

    def initial_parameters(self):
        return np.zeros(self.dimension)

    def height_fraction(self, q, direction, maximum=1., safety=.95):
        # b_h(q), L(q), and alpha(q) are nonlinear. An affine tangent cap
        # would not certify their actual trial. Full reconstructed trials
        # and their continuous polynomial bounds decide physical acceptance.
        COUNTS["nonlinear_graph_full_trial_line_searches"] += 1
        return float(maximum)

    def _base_map(self, q, control, mode):
        started = time.monotonic()
        COUNTS["base_P_"+mode+"_attempts_including_partial"] += 1
        try:
            return self._base_map_impl(q, control, mode)
        finally:
            COUNTS["base_P_"+mode+"_seconds_including_partial"] += time.monotonic()-started

    def _base_map_impl(self, q, control, mode):
        """mode scalar: one b derivative; full: q and b; value: no columns."""
        self.clock.check("before_R641_actual_base_P_map")
        started = time.monotonic()
        dimension = self.dimension+1 if mode == "full" else (1 if mode == "scalar" else 0)
        h = [off+basis@q+control*s for off,basis,s in
             zip(self.base.background_h, self.h_basis, self.sigma)]
        k = [off+basis@q for off,basis in zip(self.base.background_k,self.k_basis)]
        if not np.all(h[0] > 0) or not all(np.all(np.isfinite(v)) for v in h+k):
            raise FloatingPointError("Actual scalar P integrals require finite positive h")
        rows = []
        for i in range(len(self.grid.x)):
            if mode == "full":
                hd = [np.r_[v[i], s[i]] for v,s in zip(self.h_basis,self.sigma)]
                kd = [np.r_[v[i], LD(0)] for v in self.k_basis]
            elif mode == "scalar":
                hd = [np.asarray([s[i]], dtype=LD) for s in self.sigma]
                kd = [np.zeros(1, dtype=LD) for _ in range(3)]
            else:
                hd = kd = [np.zeros(0, dtype=LD) for _ in range(3)]
            rows.append([Jet(h[j][i],hd[j]) for j in range(3)]
                        +[Jet(k[j][i],kd[j]) for j in range(3)])
        eta = [v[0] for v in self.grid.integrate([[row[4]/(2*row[0])] for row in rows])]
        P = rows[0][0]*0
        for weight,row,ee in zip(self.grid.weights,rows,eta):
            P -= weight*row[3]*(row[0]*ee-row[3])
        COUNTS["actual_base_P_"+mode+"_calls"] += 1
        COUNTS["actual_base_P_"+mode+"_seconds"] += time.monotonic()-started
        COUNTS["actual_base_P_derivative_columns"] += dimension
        self.clock.check("after_R641_actual_base_P_map")
        return rows, eta, P

    def _height_bracket(self, q, lo, hi, report):
        # Same affine h family: continuous original h boxes at both bracket
        # endpoints imply them for every b in between, by convexity in b.
        records = report["continuous_height_on_scalar_control_bracket"] = []
        for control in (lo, hi):
            interval = adaptive.affine_coefficients(self.extended_h_coeff,
                np.r_[q, control], self.background_h_coeff)
            record, _ = self.boxes.certify_field("h", interval)
            records.append({"control_LD_decimal":ld_text(control), "qualification":record})
            if record["state"] == "pending":
                raise adaptive.PolynomialPhysicalPending(record)
            if record["state"] != "certified_represented_polynomial":
                raise FloatingPointError("Selected local P-control bracket leaves original h box")

    def scalar_root(self, q):
        started = time.monotonic()
        lo, hi = -self.root_radius, self.root_radius
        report = self.latest_scalar_root = {"state":"pending", "shape_parameters":[float(v) for v in q],
            "events":[], "root_P_tolerance":float(self.root_tolerance),
            "root_control_width_tolerance":float(self.root_width),
            "selected_local_derivative_upper_bound":-15/136,
            "numerical_bracket_is_not_a_continuous_integral_error_certificate":True,
            "continuous_root_or_global_uniqueness_not_claimed_by_floating_signs":True}
        if self.latest_geometry is not None:
            self.latest_geometry["scalar_P_root"] = report
        try:
            self._height_bracket(q, lo, hi, report)
            def evaluate(control, phase):
                _, _, P = self._base_map(q, control, "scalar")
                value, derivative = P.value, P.derivative[0]
                report["events"].append({"phase":phase, "control_LD_decimal":ld_text(control),
                    "P0_LD_decimal":ld_text(value), "actual_P0_b":float(derivative)})
                return value, derivative
            flo, dlo = evaluate(lo,"initial_left")
            fhi, dhi = evaluate(hi,"initial_right")
            if not flo > 0 or not fhi < 0:
                report.update(state="selected_local_root_bracket_unavailable",
                    bracket=[ld_text(lo),ld_text(hi)], values=[ld_text(flo),ld_text(fhi)],
                    no_original_global_infeasibility_claim=True)
                raise FloatingPointError("Actual P0 has no declared decreasing local sign bracket")
            control = LD(0)
            for iteration in range(self.root_iterations):
                self.clock.check("R641_actual_P_root_iteration")
                value, derivative = evaluate(control,"root_iteration")
                report.update(iteration=iteration, current_control_LD_decimal=ld_text(control),
                    current_P0_LD_decimal=ld_text(value), current_P0_b=float(derivative),
                    bracket=[ld_text(lo),ld_text(hi)], values=[ld_text(flo),ld_text(fhi)])
                if abs(value) <= self.root_tolerance:
                    if not derivative < -LD(15)/136:
                        report["state"] = "selected_nonzero_P_derivative_chart_unavailable"
                        raise FloatingPointError("Actual P0_b lost the selected R638 nonzero local branch")
                    left = max(lo, control-self.root_width/4)
                    right = min(hi, control+self.root_width/4)
                    fl, dl = evaluate(left,"tight_left")
                    fr, dr = evaluate(right,"tight_right")
                    if fl > 0 and fr < 0 and right-left <= self.root_width:
                        report.update(state="actual_quadrature_root_bracket_and_residual_closed",
                            actual_control_LD_decimal=ld_text(control),
                            actual_P0_LD_decimal=ld_text(value), actual_P0_b=float(derivative),
                            final_bracket=[ld_text(left),ld_text(right)],
                            final_bracket_values=[ld_text(fl),ld_text(fr)],
                            all_values_are_actual_integrals_not_assigned_zero=True)
                        COUNTS["actual_scalar_P_roots_closed"] += 1
                        return control, report
                if value > 0:
                    lo, flo = control, value
                elif value < 0:
                    hi, fhi = control, value
                else:
                    # The narrow sign bracket, not a rounded printed zero,
                    # remains necessary. Explore the current bracket midpoint.
                    control = (lo+hi)/2
                    continue
                proposed = control-value/derivative if derivative != 0 else (lo+hi)/2
                width = hi-lo
                control = proposed if lo+width/16 < proposed < hi-width/16 else (lo+hi)/2
            report.update(state="pending", final_bracket=[ld_text(lo),ld_text(hi)],
                final_bracket_values=[ld_text(flo),ld_text(fhi)], unfinished_root_is_not_zero=True)
            raise ScalarRootPending(report)
        finally:
            report["seconds"] = time.monotonic()-started
            COUNTS["actual_scalar_P_root_calls_including_partial"] += 1
            COUNTS["actual_scalar_P_root_seconds_including_partial"] += report["seconds"]

    def evaluate(self, parameters, derivatives=True, fixed_state=None, fixed_center=None, enforce_box=True):
        started = time.monotonic()
        COUNTS["three_end_curve_attempts_including_partial"] += 1
        try:
            return self._evaluate_impl(parameters, derivatives, fixed_state, fixed_center, enforce_box)
        finally:
            COUNTS["three_end_curve_seconds_including_partial"] += time.monotonic()-started

    def _evaluate_impl(self, parameters, derivatives=True, fixed_state=None, fixed_center=None, enforce_box=True):
        reduced.require_public_science()
        q = np.asarray(parameters,float).copy()
        if (fixed_state is None and fixed_center is None and derivatives and enforce_box
                and self.cache_parameters is not None and np.array_equal(q,self.cache_parameters)):
            self.latest_curve = self.cache_curve
            self.latest_geometry = self.cache_curve["physical_attainers"]
            COUNTS["same_shape_complete_true_chain_cache_reuses"] += 1
            return self.cache_curve
        self.evaluations += 1; self.jet_evaluations += int(derivatives)
        self.last_parameters = q
        started = time.monotonic()
        if q.shape != (self.dimension,) or not np.all(np.isfinite(q)):
            raise ValueError("All 256 actual shape parameters are required")
        self.latest_geometry = {"phase":"actual_three_end_shape_started",
            "actual_shape_parameter_identity":identity(q.tolist()),
            "physical_fields_or_graph_branch_not_yet_qualified":True}
        qld = np.asarray(q,dtype=LD)
        dimension = self.dimension if derivatives else 0
        if fixed_state is None:
            control, root_report = self.scalar_root(qld)
        else:
            if derivatives:
                raise ValueError("A fixed physical fine curve has no re-solved chart derivative")
            control = LD(fixed_state["height_control_LD_decimal"])
            root_report = {"state":"fixed_same_curve_control_not_resolved",
                "actual_control_LD_decimal":ld_text(control), "fine_scalar_P_root_recomputed":False}
        self.last_control = control
        rows, eta, P = self._base_map(qld,control,"full" if derivatives else "value")
        if derivatives:
            Pb = P.derivative[-1]
            if not Pb < -LD(15)/136:
                raise FloatingPointError("Full actual P chain leaves selected nonzero derivative branch")
            db = -P.derivative[:-1]/Pb
            def compose(v):
                return Jet(v.value,v.derivative[:-1]+v.derivative[-1]*db)
            rows = [[compose(v) for v in row] for row in rows]
            eta = [compose(v) for v in eta]
            P = compose(P)
        zero = rows[0][0]*0
        U = K = S2 = S4 = W = zero
        for weight,row,ee in zip(self.grid.weights,rows,eta):
            h,hx,hxx,k,kx,kxx = row
            d,v = h*ee-k,hx*ee-kx/2
            U += weight*(hx/h)**2
            K += weight*k*k
            S2 += weight*ee*d/h
            S4 += weight*ee*k*d*d/h
            W += weight*(v/h)**2
        D, N = U*S4-K*W, K*S2-S4
        self.latest_geometry.update(phase="actual_three_end_integrals_completed",
            actual_base_P0=float(P.value),U=float(U.value),K_kappa=float(K.value),
            S2=float(S2.value),S4=float(S4.value),W0=float(W.value),graph_D=float(D.value),graph_N=float(N.value),
            actual_height_control_LD_decimal=ld_text(control))
        if fixed_state is None:
            if not (U.value>0 and K.value>0 and D.value<0 and N.value<0):
                raise FloatingPointError("Actual R641 negative nondegenerate positive-length graph unavailable")
            z = N/D
            length = z**LD("-.5")
            amplitude_square = (1+U*z)/K
            alpha = amplitude_square**LD(".5")
        else:
            length = Jet(LD(fixed_state["physical_length_LD_decimal"]),np.zeros(dimension))
            alpha = Jet(LD(fixed_state["physical_alpha_LD_decimal"]),np.zeros(dimension))
            z = length**-2
            amplitude_square = alpha*alpha
        self.latest_geometry.update(actual_physical_length=float(length.value),actual_alpha=float(alpha.value))
        if not (LD("2.1") <= length.value <= LD("7.9")):
            raise FloatingPointError("Actual derived physical L leaves the original unchanged box")
        geometry, acceleration = [], []
        for row,ee in zip(rows,eta):
            h,hx,hxx,k,kx,kxx = row
            geometry.append([h,alpha*k,alpha*ee,hx/length,alpha*kx/length])
            acceleration.append([hxx/length**2,alpha*kxx/length**2])
        report = background.physical_attainers(geometry,self.grid.x,length.value)
        report.update(actual_shape_parameter_identity=identity(q.tolist()),
            fixed_center_kappa_x=ld_text(self.c), fixed_polynomial_background=background.BACKGROUND,
            shape_coordinates_are_all_256_R638_projected_h_and_original_kappa_directions=True,
            actual_height_control_LD_decimal=ld_text(control), scalar_P_root=root_report,
            U=float(U.value),K_kappa=float(K.value),S2=float(S2.value),S4=float(S4.value),W0=float(W.value),
            graph_D=float(D.value),graph_N=float(N.value),graph_z=float(z.value),
            alpha=float(alpha.value),alpha_LD_decimal=ld_text(alpha.value),
            physical_length_LD_decimal=ld_text(length.value),
            actual_kinetic_identity=float(amplitude_square.value*K.value-1-U.value*z.value),
            actual_s0_normalized_identity=float(amplitude_square.value*(amplitude_square.value*S4.value-S2.value-W.value*z.value)),
            actual_base_P0=float(P.value),
            physical_center_v=float(geometry[0][4].value),physical_center_a=float(acceleration[0][0].value),
            physical_center_beta=float(acceleration[0][0].value-geometry[0][0].value*geometry[0][4].value**2/4),
            all_polynomial_hull_fields_in_original_box=False,
            continuous_original_integral_error_not_certified_by_graph_algebra=True)
        self.latest_geometry = report
        if enforce_box and not report["all_sampled_original_physical_fields_in_box"]:
            raise FloatingPointError("Actual R641 field sample leaves an original physical box")
        qualification = self.boxes.certify(self,np.r_[qld,control],alpha.value,length.value)
        report["adaptive_polynomial_qualification"] = qualification
        good = qualification["state"] == "all_four_represented_polynomial_fields_certified"
        report["all_polynomial_hull_fields_in_original_box"] = good
        if enforce_box and qualification["state"] == "pending":
            raise adaptive.PolynomialPhysicalPending(qualification)
        if enforce_box and not good:
            raise FloatingPointError("Actual R641 polynomial point leaves an original physical box")
        density = [[length*v for v in paid.density(row)] for row in geometry]
        primitive = self.grid.integrate(density)
        total = primitive[-1]
        if fixed_center is None:
            history = [[row[j]-total[j] if j in original.ODD else row[j] for j in range(8)] for row in primitive]
        else:
            center = [Jet(LD(v),np.zeros(dimension)) for v in fixed_center]
            history = [[center[j]+row[j] for j in range(8)] for row in primitive]
        H = geometry[0][0]
        end = [total[1]/length,(8*total[3]+2*total[1])/length,
               8*H**2*total[4]/length,4*H**2*total[6]/length]
        dependent = np.asarray([history[-1][j].value for j in (1,3,6)], dtype=LD)
        report["actual_dependent_three_terminal_values"] = [float(v) for v in dependent]
        report["actual_dependent_three_terminal_max"] = float(np.max(np.abs(dependent)))
        report["unchanged_original_dependent_end_tolerance"] = float(self.original_end_tolerance)
        if fixed_state is None and np.max(np.abs(dependent)) > self.original_end_tolerance:
            raise DependentEndsPending({"state":"actual_dependent_original_ends_unclosed",
                "shape_parameters":q.tolist(), "physical_attainers":report,
                "remaining_r1_objective_does_not_hide_unpaid_dependent_rows":True})
        curve = {"shape_parameters":q,"parameters":q,"geometry":geometry,"acceleration":acceleration,
            "history":history,"total_integral":total,"end":end,"reduced_end":[end[2]],
            "length":length,"grid":self.grid,"alpha":alpha,"physical_attainers":report,
            "knots":self.knots,"height_control":control,"independent_memory_coordinates":0,
            "fixed_physical_alpha_length_height_control_and_center":fixed_state is not None,
            "fixed_polynomial_background":background.BACKGROUND,
            "dependent_three_end_values_are_actual_density_integrals_not_assigned_zero":True}
        self.latest_curve = curve
        if fixed_state is None and fixed_center is None and derivatives and enforce_box:
            self.cache_parameters,self.cache_curve = q.copy(),curve
        COUNTS["complete_three_end_curve_evaluations"] += 1
        COUNTS["complete_three_end_curve_seconds"] += time.monotonic()-started
        self.clock.check("after_R641_complete_true_three_end_curve")
        return curve
