"""Four original polynomial boxes and the fixed physical A_r row on R641."""
from __future__ import annotations

import numpy as np

import r641_true_three_end_chart as source
from r636_adaptive_background_center_chart import sparse_affine_coefficients

adaptive, LD = source.adaptive, source.LD


class PhysicalBoxes(source.BackgroundPolynomialBoxes):
    def physical_coefficients(self, graph, extended, alpha, length):
        height = sparse_affine_coefficients(graph.extended_h_coeff, extended, graph.background_h_coeff)
        kappa = sparse_affine_coefficients(graph.extended_k_coeff, extended, graph.background_k_coeff)
        return {
            "h": height,
            "k": adaptive.positive_scale(kappa, alpha),
            "gamma": adaptive.positive_divide(adaptive.derivative(height, self.knots), length),
            "upsilon": adaptive.positive_divide(
                adaptive.positive_scale(adaptive.derivative(kappa, self.knots), alpha), length),
        }


class PhysicalChart(source.ThreeEndChart):
    def __init__(self, knots, grid, clock, args, weight, paid_root=None):
        super().__init__(knots, grid, clock, args.height_control_radius,
            args.scalar_root_tolerance, args.scalar_root_width, args.scalar_root_iterations,
            args.physical_bound_nodes, args.physical_bound_depth, args.end_tol)
        self.boxes = PhysicalBoxes(knots, clock, args.physical_bound_nodes, args.physical_bound_depth)
        self.weight = LD(weight)
        self.paid_root = paid_root
        self.center_distance = args.center_activity_distance
        self.length_distance = args.length_activity_distance

    def _height_bracket(self, q, lo, hi, report):
        records = report["continuous_height_on_scalar_control_bracket"] = []
        for control in (lo, hi):
            interval = sparse_affine_coefficients(self.extended_h_coeff,
                np.r_[q, control], self.background_h_coeff)
            qualification, _ = self.boxes.certify_field("h", interval)
            records.append({"control_LD_decimal": source.ld_text(control), "qualification": qualification})
            if qualification["state"] == "pending":
                raise adaptive.PolynomialPhysicalPending(qualification)
            if qualification["state"] != "certified_represented_polynomial":
                raise FloatingPointError("The selected P-control bracket leaves the original h box")

    def scalar_root(self, q):
        paid = self.paid_root
        if paid is None or not np.array_equal(q, np.asarray(paid["shape_parameters"], dtype=LD)):
            return super().scalar_root(q)
        self.latest_scalar_root = {**paid, "same_source_scalar_root_reused": True,
                                  "source_seconds_are_prior_cost": True}
        self.latest_geometry["scalar_P_root"] = self.latest_scalar_root
        source.COUNTS["source_closed_scalar_root_reuses"] += 1
        return LD(paid["actual_control_LD_decimal"]), self.latest_scalar_root

    def evaluate(self, *args, **kwargs):
        curve = super().evaluate(*args, **kwargs)
        terminal = curve["history"][-1][4]
        curve["reduced_end"] = [terminal * self.weight]
        report = curve["physical_attainers"]
        report["fixed_source_A_r_weight_LD_decimal"] = source.ld_text(self.weight)
        report["true_physical_A_r_LD_decimal"] = source.ld_text(terminal.value)
        report["fixed_weighted_A_r_LD_decimal"] = source.ld_text(curve["reduced_end"][0].value)
        return curve
