#!/usr/bin/env python3
"""Same R632 actual 257-dimensional curve and true chain, refined boxes.

The copied evaluate body preserves every integral and derivative operation.
Only the sufficient unrefined polynomial guard and affine height cap change.
Unresolved continuous polynomial checks propagate as pending, never rejected.
"""
from __future__ import annotations
import time
import numpy as np
import r632_true_hermite_kinetic_chart as base
import r632_adaptive_polynomial_boxes as adaptive
from r632_true_hermite_kinetic_chart import (
    LD, Jet, reduced, paid, COUNTS, identity, ld_text, physical_attainers,
    IntegralGrid, legacy, original)


class AdaptiveTrueHermiteKineticChart(base.TrueHermiteKineticChart):
    def __init__(self, knots, grid, center_kappa_x, clock,
                 maximum_nodes=32768, maximum_depth=40):
        super().__init__(knots, grid, center_kappa_x, clock)
        self.boxes = adaptive.AdaptivePolynomialBoxes(knots, clock, maximum_nodes, maximum_depth)

    def height_fraction(self, q, direction, maximum=1., safety=.95):
        return self.boxes.height_fraction(self, q, direction, maximum, safety)

    def evaluate(self, parameters, derivatives=True, fixed_alpha=None, fixed_center=None,
                 enforce_box=True):
        reduced.require_public_science()
        start = time.monotonic()
        self.evaluations += 1
        self.jet_evaluations += int(derivatives)
        q = np.asarray(parameters, float).copy()
        self.last_parameters = q
        if q.shape != (self.dimension,) or not np.all(np.isfinite(q)) or not 2.1 <= q[-1] <= 7.9:
            raise ValueError("The complete true shape and unchanged original L box are required")
        self.clock.check("before_R632_true_geometry_and_global_amplitude")
        dimension = self.dimension if derivatives else 0
        unit = np.eye(self.dimension, dtype=LD) if derivatives else None
        length = Jet(q[-1], unit[-1] if derivatives else np.zeros(0))
        h = [basis@np.asarray(q, dtype=LD) for basis in self.h_basis]
        k = [off+basis@np.asarray(q, dtype=LD) for off, basis in zip(self.k_offset, self.k_basis)]
        rows = []
        for i in range(len(self.grid.x)):
            if not h[0][i] > 0:
                raise FloatingPointError("R632 requires positive actual h before true integrals")
            rows.append([Jet(h[j][i], self.h_basis[j][i] if derivatives else np.zeros(0)) for j in range(3)]
                        +[Jet(k[j][i], self.k_basis[j][i] if derivatives else np.zeros(0)) for j in range(3)])
        zero = rows[0][0]*0
        U, K = zero, zero
        for weight, (hv, hx, _, kv, _, _) in zip(self.grid.weights, rows):
            U += weight*(hx/hv)**2
            K += weight*kv*kv
        if not U.value > 0 or not K.value > 0:
            raise FloatingPointError("Outside the R632 U>0,K_kappa>0 amplitude graph")
        alpha = ((1+U/length**2)/K)**LD(".5") if fixed_alpha is None else Jet(LD(fixed_alpha), np.zeros(dimension))
        eta_kappa = self.grid.integrate([[row[4]/(2*row[0])] for row in rows])
        geometry, acceleration = [], []
        for row, eta in zip(rows, eta_kappa):
            hv, hx, hxx, kv, kx, kxx = row
            geometry.append([hv, alpha*kv, alpha*eta[0], hx/length, alpha*kx/length])
            acceleration.append([hxx/length**2, alpha*kxx/length**2])
        report = physical_attainers(geometry, self.grid.x, length.value)
        hc = np.einsum("ijk,k->ij", self.h_coeff[0], np.asarray(q, dtype=LD))
        kc = self.k_coeff_offset[0]+np.einsum("ijk,k->ij", self.k_coeff[0], np.asarray(q, dtype=LD))
        hg = np.einsum("ijk,k->ij", self.h_coeff[1], np.asarray(q, dtype=LD))/length.value
        kg = (self.k_coeff_offset[1]+np.einsum("ijk,k->ij", self.k_coeff[1], np.asarray(q, dtype=LD)))*alpha.value/length.value
        bounds = {name:[float(np.min(value)), float(np.max(value))] for name, value in
                  (("h", hc), ("k", alpha.value*kc), ("gamma", hg), ("upsilon", kg))}
        hull_okay = bool(np.min(hc)>LD(".8") and np.max(hc)<3 and
                         np.max(np.abs(alpha.value*kc))<2 and np.max(np.abs(hg))<6 and np.max(np.abs(kg))<6)
        report.update(Bernstein_polynomial_hull_bounds=bounds,
            actual_shape_parameter_identity=identity(q.tolist()),
            polynomial_hull_is_sufficient_not_necessary_for_physical_box=True,
            polynomial_hull_float_arithmetic_is_not_interval_certification=True,
            all_polynomial_hull_fields_in_original_box=hull_okay,
            U=float(U.value), K_kappa=float(K.value), alpha=float(alpha.value),
            alpha_LD_decimal=ld_text(alpha.value), actual_K=float(alpha.value**2*K.value),
            actual_kinetic_identity=float(alpha.value**2*K.value-1-U.value/length.value**2),
            fixed_center_kappa_x=ld_text(self.c), physical_center_v=float(geometry[0][4].value),
            physical_center_a=float(acceleration[0][0].value),
            physical_center_beta=float(acceleration[0][0].value-geometry[0][0].value*geometry[0][4].value**2/4))
        report["coarse_unsubdivided_polynomial_hull_passed"] = hull_okay
        report["all_polynomial_hull_fields_in_original_box"] = False
        report["old_float_hull_flag_describes_only_unrefined_display_bounds"] = True
        self.latest_geometry = report
        if enforce_box and not report["all_sampled_original_physical_fields_in_box"]:
            report["adaptive_polynomial_qualification"] = {
                "state":"not_run_after_actual_sampled_physical_violation",
                "finite_sample_failure_is_not_a_full_continuous_certificate":True}
            raise FloatingPointError("Actual true field sample leaves the original physical box")
        qualification = self.boxes.certify(self, q, alpha.value, length.value)
        report["adaptive_polynomial_qualification"] = qualification
        certified = qualification["state"] == "all_four_represented_polynomial_fields_certified"
        report["all_polynomial_hull_fields_in_original_box"] = certified
        if enforce_box and qualification["state"] == "pending":
            raise adaptive.PolynomialPhysicalPending(qualification)
        if enforce_box and not certified:
            raise FloatingPointError("Actual polynomial point enclosure leaves an original open physical box")
        density = [[length*v for v in paid.density(row)] for row in geometry]
        primitive = self.grid.integrate(density)
        total = primitive[-1]
        if fixed_center is None:
            history = [[row[j]-total[j] if j in original.ODD else row[j] for j in range(8)] for row in primitive]
        else:
            center = [Jet(LD(v), np.zeros(dimension)) for v in fixed_center]
            history = [[center[j]+row[j] for j in range(8)] for row in primitive]
        height = geometry[0][0]
        end = [total[1]/length, (8*total[3]+2*total[1])/length,
               8*height**2*total[4]/length, 4*height**2*total[6]/length]
        curve = {"shape_parameters":q, "parameters":q, "geometry":geometry,
            "acceleration":acceleration, "history":history, "total_integral":total,
            "end":end, "reduced_end":[end[i] for i in (0, 2, 3)],
            "length":length, "grid":self.grid, "alpha":alpha,
            "physical_attainers":report, "knots":self.knots,
            "independent_memory_coordinates":0,
            "fixed_physical_alpha_and_center":fixed_alpha is not None}
        self.latest_curve = curve
        COUNTS["true_curve_evaluations"] += 1
        COUNTS["true_curve_seconds"] += time.monotonic()-start
        self.clock.check("after_R632_true_geometry_memory_and_end_chain")
        return curve
