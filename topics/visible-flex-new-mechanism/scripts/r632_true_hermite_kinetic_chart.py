#!/usr/bin/env python3
"""R632 true Hermite shape, kinetic amplitude, and complete integral chain.

There are no independent eta/A/rho coordinates. Values retain longdouble;
the dense prefix derivative product is evaluated in binary64, the precision
of the Newton matrix. Every derivative column and every prefix term remains.
The original scalar field expressions and full potential are unchanged.
"""
from __future__ import annotations

from collections import defaultdict
import hashlib
import json
import time

import numpy as np

import r620_free_center_full_feedback_bvp_agent as legacy
import r612_r614_reduced_function_map_agent as reduced

original, paid = reduced.original, reduced.original.paid
LD, Jet = original.LD, original.Jet
COUNTS = defaultdict(float)


def identity(value):
    raw = json.dumps(value, separators=(",", ":"), allow_nan=False).encode()
    return {"json_bytes":len(raw), "json_sha256":hashlib.sha256(raw).hexdigest()}


def ld_text(value):
    return np.format_float_scientific(LD(value), precision=24, unique=False, trim="k")


class IntegralGrid(legacy.ObservedIntegralGrid):
    """Same complete prefix; LD values and all-column binary64 Newton chain."""
    def __init__(self, panels, order, observations, clock):
        super().__init__(panels, order, observations, clock)
        self.prefix64 = np.asarray(self.prefix, float)

    def integrate(self, rows):
        self.clock.check("before_R632_complete_prefix")
        started = time.monotonic()
        try:
            n, width = len(rows), len(rows[0])
            dim = len(rows[0][0].derivative)
            values = np.asarray([[v.value for v in row] for row in rows], dtype=LD)
            result = self.prefix@values
            if dim:
                derivatives = np.asarray([[v.derivative for v in row] for row in rows], float)
                chain = (self.prefix64@derivatives.reshape(n, width*dim)).reshape(n, width, dim)
            else:
                chain = np.zeros((n, width, 0))
            COUNTS["complete_prefix_calls"] += 1
            COUNTS["complete_prefix_value_entries"] += n*width
            COUNTS["complete_prefix_derivative_entries"] += n*width*dim
            answer = [[Jet(result[i, j], chain[i, j]) for j in range(width)] for i in range(n)]
            self.clock.check("after_R632_complete_prefix")
            return answer
        finally:
            COUNTS["complete_prefix_seconds"] += time.monotonic()-started


def physical_attainers(geometry, x, length):
    """All actual fields and all original bounds, without an early generic error."""
    values = np.asarray([[v.value for v in row] for row in geometry], dtype=LD)
    answer = {"points":len(x), "physical_length":float(length), "fields":{},
              "finite_sample_is_not_a_continuous_certificate":True}
    feasible = bool(np.all(np.isfinite(values)))
    for j, (name, lo, hi) in enumerate((
            ("h", LD(".8"), LD(3)), ("k", LD(-2), LD(2)),
            ("eta", LD(-1), LD(1)), ("gamma", LD(-6), LD(6)),
            ("upsilon", LD(-6), LD(6)))):
        imin, imax = int(np.argmin(values[:, j])), int(np.argmax(values[:, j]))
        minimum, maximum = values[imin, j], values[imax, j]
        good = bool(np.isfinite(minimum) and np.isfinite(maximum) and minimum > lo and maximum < hi)
        answer["fields"][name] = {
            "minimum":float(minimum), "minimum_x":float(x[imin]), "minimum_index":imin,
            "maximum":float(maximum), "maximum_x":float(x[imax]), "maximum_index":imax,
            "original_open_bounds":[float(lo), float(hi)], "within_original_box":good,
            "lower_excess":float(max(LD(0), lo-minimum)),
            "upper_excess":float(max(LD(0), maximum-hi))}
        feasible &= good
    answer["all_sampled_original_physical_fields_in_box"] = feasible
    return answer


class TrueHermiteKineticChart:
    """65-node member has 257 real shape coordinates, including physical L.

    Order: h values; interior h_x; h_xx(0); noncentral kappa values;
    interior kappa_x; L. Fixed kappa_x(0)=c<0 removes amplitude redundancy.
    All h/k second derivatives are the source spline-velocity recipe, with
    the same center replacements. This is the source actual C2 space.
    """
    def __init__(self, knots, grid, center_kappa_x, clock):
        reduced.require_public_science()
        self.knots = np.asarray(knots, float).copy()
        self.grid, self.clock = grid, clock
        # scipy's defining Hermite coefficients use binary64; declare c at
        # that same exact input value before retaining it in LD arithmetic.
        self.c = LD(float(center_kappa_x))
        n = len(self.knots)
        if n < 3 or self.c >= 0 or self.knots[0] != 0 or self.knots[-1] != 1:
            raise ValueError("R632 needs the actual mesh and a fixed nonzero negative central derivative")
        self.n, self.dimension = n, 4*n-3
        self.h_values = slice(0, n)
        self.h_slopes = slice(n, 2*n-2)
        self.h_center_second = 2*n-2
        self.k_values = slice(2*n-1, 3*n-2)
        self.k_slopes = slice(3*n-2, 4*n-4)
        self.length_index = 4*n-4
        self.evaluations = self.jet_evaluations = 0
        self.latest_geometry = self.latest_curve = None
        self.last_parameters = None
        start = time.monotonic()
        clock.check("before_R632_complete_Hermite_basis")
        derivative = legacy.CubicSpline(self.knots, np.eye(n), axis=0).derivative()(self.knots)
        hd = np.zeros((n, 3, self.dimension))
        hd[:, 0, self.h_values] = np.eye(n)
        hd[1:-1, 1, self.h_slopes] = np.eye(n-2)
        hd[:, 2, :] = derivative@hd[:, 1, :]
        hd[0, 2, :] = 0
        hd[0, 2, self.h_center_second] = 1
        kd = np.zeros_like(hd)
        kd[1:, 0, self.k_values] = np.eye(n-1)
        kd[1:-1, 1, self.k_slopes] = np.eye(n-2)
        kd[:, 2, :] = derivative@kd[:, 1, :]
        kd[0, 2, :] = 0
        offset = np.zeros((n, 3))
        offset[0, 1] = float(self.c)
        offset[:, 2] = derivative@offset[:, 1]
        offset[0, 2] = 0
        hp = legacy.BPoly.from_derivatives(self.knots, hd)
        kp = legacy.BPoly.from_derivatives(self.knots, kd)
        ko = legacy.BPoly.from_derivatives(self.knots, offset)
        self.h_basis = [np.asarray(hp(grid.x, j), dtype=LD) for j in range(3)]
        self.k_basis = [np.asarray(kp(grid.x, j), dtype=LD) for j in range(3)]
        self.k_offset = [np.asarray(ko(grid.x, j), dtype=LD) for j in range(3)]
        self.h_coeff = [np.asarray(hp.derivative(j).c, dtype=LD) for j in (0, 1)]
        self.k_coeff = [np.asarray(kp.derivative(j).c, dtype=LD) for j in (0, 1)]
        self.k_coeff_offset = [np.asarray(ko.derivative(j).c, dtype=LD) for j in (0, 1)]
        COUNTS["Hermite_basis_constructions"] += 1
        COUNTS["Hermite_basis_seconds"] += time.monotonic()-start
        clock.check("after_R632_complete_Hermite_basis")

    def source_parameters(self, payload):
        states = np.asarray(payload["original_nineteen_states"], float)
        p = np.asarray(payload["parameters"], float)
        q = np.zeros(self.dimension)
        q[self.h_values] = states[0]
        q[self.h_slopes] = p[-1]*states[3, 1:-1]
        q[self.h_center_second] = p[-1]**2*p[6]
        q[self.k_values] = states[1, 1:]
        q[self.k_slopes] = p[-1]*states[4, 1:-1]
        q[self.length_index] = p[-1]
        return q

    def height_fraction(self, q, direction, maximum=1., safety=.95):
        """Exact affine Bernstein height/L prefix cap, no dropped field row."""
        coeff = np.einsum("ijk,k->ij", self.h_coeff[0], np.asarray(q, dtype=LD))
        change = np.einsum("ijk,k->ij", self.h_coeff[0], np.asarray(direction, dtype=LD))
        cap = LD(maximum)
        for positive, margin in ((change, LD(3)-coeff), (-change, coeff-LD(".8"))):
            mask = positive > 0
            if np.any(mask):
                cap = min(cap, LD(safety)*np.min(margin[mask]/positive[mask]))
        dL, length = LD(direction[-1]), LD(q[-1])
        if dL > 0:
            cap = min(cap, LD(safety)*(LD("7.9")-length)/dL)
        elif dL < 0:
            cap = min(cap, LD(safety)*(length-LD("2.1"))/-dL)
        return max(0., float(cap))

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
        self.latest_geometry = report
        if enforce_box and (not report["all_sampled_original_physical_fields_in_box"] or not hull_okay):
            raise FloatingPointError("R632 true physical fields or sufficient polynomial hull leave original box")
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
