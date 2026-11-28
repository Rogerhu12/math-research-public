#!/usr/bin/env python3
"""Outward Bernstein subdivision for the unchanged four polynomial boxes.

The represented original quintic basis coefficients and q define the curve.
Derivatives are enclosed from those SAME coefficients, not treated as new
independent rounded derivative polynomials. Alpha and L are the represented
physical scalars of this target evaluation. This does not enclose quadrature,
the original mother coefficients, eta, A, rho, or the complete BVP residual.
"""
from __future__ import annotations

from collections import defaultdict
import heapq
import time

import numpy as np

from r632_true_hermite_kinetic_chart import LD, ld_text

COUNTS = defaultdict(float)
BOUNDS = {"h":(LD(".8"), LD(3)), "k":(LD(-2), LD(2)),
          "gamma":(LD(-6), LD(6)), "upsilon":(LD(-6), LD(6))}


def down(value):
    return np.nextafter(np.asarray(value, dtype=LD), LD(-np.inf))


def up(value):
    return np.nextafter(np.asarray(value, dtype=LD), LD(np.inf))


def affine_coefficients(basis, q, offset=None):
    """Enclose every exact linear combination of represented finite inputs."""
    basis, q = np.asarray(basis, dtype=LD), np.asarray(q, dtype=LD)
    lo = np.zeros(basis.shape[:-1], dtype=LD) if offset is None else np.asarray(offset, dtype=LD).copy()
    hi = lo.copy()
    for j, value in enumerate(q):
        if value == 0:
            continue
        product = basis[..., j]*value
        lo, hi = down(lo+down(product)), up(hi+up(product))
    if not np.all(np.isfinite(lo)) or not np.all(np.isfinite(hi)):
        raise FloatingPointError("Nonfinite exact-input polynomial coefficient enclosure")
    COUNTS["affine_coefficient_all_column_calls"] += 1
    COUNTS["affine_coefficient_columns_retained"] += len(q)
    return lo, hi


def positive_scale(interval, value):
    value = LD(value)
    if not value > 0 or not np.isfinite(value):
        raise ValueError("Positive finite physical scalar required")
    lo, hi = interval
    return down(lo*value), up(hi*value)


def positive_divide(interval, value):
    value = np.asarray(value, dtype=LD)
    if not np.all(value > 0) or not np.all(np.isfinite(value)):
        raise ValueError("Positive finite physical divisor required")
    lo, hi = interval
    return down(lo/value), up(hi/value)


def derivative(interval, knots):
    """Exact derivative of the enclosed quintic on its physical x cells."""
    lo, hi = interval
    degree = len(lo)-1
    # Source knots are represented dyadic multiples of 1/64. Their
    # differences below are exact; reject other meshes rather than invent
    # an unregistered interval-denominator convention.
    knots = np.asarray(knots, dtype=LD)
    widths = knots[1:]-knots[:-1]
    if (not np.all(widths == LD(1)/64) or len(widths) != 64):
        raise ValueError("This paid continuation uses the actual uniform 65-knot source")
    difference = (down(lo[1:]-hi[:-1]), up(hi[1:]-lo[:-1]))
    return positive_divide(positive_scale(difference, degree), widths)


def split(interval):
    """de Casteljau at exactly 1/2, with outward arithmetic throughout."""
    lo, hi = (np.asarray(a, dtype=LD) for a in interval)
    floor, ceiling = np.min(lo), np.max(hi)
    left_lo, left_hi, right_lo, right_hi = [lo[0]], [hi[0]], [lo[-1]], [hi[-1]]
    while len(lo) > 1:
        lo = np.maximum(floor, down(down(lo[:-1]+lo[1:])/2))
        hi = np.minimum(ceiling, up(up(hi[:-1]+hi[1:])/2))
        left_lo.append(lo[0]); left_hi.append(hi[0])
        right_lo.append(lo[-1]); right_hi.append(hi[-1])
    COUNTS["de_Casteljau_subdivisions"] += 1
    return ((np.asarray(left_lo, dtype=LD), np.asarray(left_hi, dtype=LD)),
            (np.asarray(right_lo[::-1], dtype=LD), np.asarray(right_hi[::-1], dtype=LD)))


def restrict(interval, path, depth):
    result = interval
    for bit in range(depth-1, -1, -1):
        result = split(result)[(path >> bit) & 1]
    return result


def interval_record(interval):
    return {"lo":[ld_text(v) for v in interval[0]],
            "hi":[ld_text(v) for v in interval[1]]}


class PolynomialPhysicalPending(RuntimeError):
    def __init__(self, record):
        super().__init__("Original physical polynomial bounds remain unresolved; no infeasibility claim")
        self.record = record


class AdaptivePolynomialBoxes:
    def __init__(self, knots, clock, maximum_nodes=32768, maximum_depth=40):
        self.knots, self.clock = np.asarray(knots, dtype=LD), clock
        self.maximum_nodes, self.maximum_depth = int(maximum_nodes), int(maximum_depth)
        self.latest_record = self.latest_height_fraction = None
        self.active_polynomial_field = None
        if np.finfo(LD).nmant < 63:
            raise RuntimeError("The declared Linux longdouble enclosure arithmetic is unavailable")

    def check(self, phase, nodes):
        if nodes % 64 < 2:
            self.clock.check("R632_adaptive_polynomial_"+phase)

    def physical_coefficients(self, graph, q, alpha, length):
        h = affine_coefficients(graph.h_coeff[0], q)
        kappa = affine_coefficients(graph.k_coeff[0], q, graph.k_coeff_offset[0])
        return {"h":h, "k":positive_scale(kappa, alpha),
                "gamma":positive_divide(derivative(h, self.knots), length),
                "upsilon":positive_divide(positive_scale(derivative(kappa, self.knots), alpha), length)}

    def point_violation(self, interval, lower, upper, cell, depth, path):
        lo, hi = interval
        for j, side in ((0, 0), (-1, 1)):
            if lo[j] >= upper or hi[j] <= lower:
                x = self.knots[cell]+(self.knots[cell+1]-self.knots[cell])*LD(path+side)/(LD(2)**depth)
                return {"cell":cell, "depth":depth, "path":path, "side":side,
                    "x_LD_decimal":ld_text(x), "value_enclosure":[ld_text(lo[j]), ld_text(hi[j])],
                    "outside_original_open_bound":True}
        return None

    def certify_field(self, name, coefficients, capture_leaves=False):
        lower, upper = BOUNDS[name]
        lo, hi = coefficients
        stack = [(j, 0, 0, (lo[:, j], hi[:, j])) for j in range(lo.shape[1]-1, -1, -1)]
        nodes, maximum_depth, closed = 0, 0, []
        total_lo, total_hi = LD(np.inf), LD(-np.inf)
        record = {"state":"pending", "field":name,
            "original_open_bounds":[float(lower), float(upper)],
            "coarse_outward_hull":[ld_text(np.min(lo)), ld_text(np.max(hi))],
            "maximum_nodes":self.maximum_nodes, "maximum_depth":self.maximum_depth}
        self.active_polynomial_field = record
        while stack:
            if nodes >= self.maximum_nodes:
                record.update(state="pending", processed_nodes=nodes,
                    certified_leaves=len(closed), reached_depth=maximum_depth,
                    certified_leaf_paths=[[c, d, p] for c, d, p, _ in closed],
                    unresolved_frontier=[{"cell":c, "depth":d, "path":p,
                        "coefficients":interval_record(v)} for c, d, p, v in stack],
                    remaining_frontier_is_not_closed_or_infeasible=True)
                COUNTS["unresolved_polynomial_budget_events"] += 1
                return record, None
            try:
                self.check(name, nodes)
            except Exception:
                record.update(state="pending", processed_nodes=nodes,
                    certified_leaves=len(closed), reached_depth=maximum_depth,
                    certified_leaf_paths=[[c, d, p] for c, d, p, _ in closed],
                    unresolved_frontier=[{"cell":c, "depth":d, "path":p,
                        "coefficients":interval_record(v)} for c, d, p, v in stack],
                    remaining_frontier_is_not_closed_or_infeasible=True)
                raise
            cell, depth, path, interval = stack.pop()
            clo, chi = interval
            nodes += 1; maximum_depth = max(maximum_depth, depth)
            COUNTS["polynomial_nodes_visited_including_partial"] += 1
            minimum, maximum = np.min(clo), np.max(chi)
            if minimum > lower and maximum < upper:
                total_lo, total_hi = min(total_lo, minimum), max(total_hi, maximum)
                closed.append((cell, depth, path, interval))
                continue
            violation = self.point_violation(interval, lower, upper, cell, depth, path)
            if violation is not None:
                record.update(state="actual_point_violation", witness=violation,
                    processed_nodes=nodes, certified_leaves=len(closed), reached_depth=maximum_depth)
                COUNTS["actual_polynomial_point_violations"] += 1
                return record, None
            if nodes >= self.maximum_nodes or depth >= self.maximum_depth:
                frontier = [(cell, depth, path, interval)]+stack
                record.update(state="pending", processed_nodes=nodes,
                    certified_leaves=len(closed), reached_depth=maximum_depth,
                    certified_leaf_paths=[[c, d, p] for c, d, p, _ in closed],
                    unresolved_frontier=[{"cell":c, "depth":d, "path":p,
                        "coefficients":interval_record(v)} for c, d, p, v in frontier],
                    remaining_frontier_is_not_closed_or_infeasible=True)
                COUNTS["unresolved_polynomial_budget_events"] += 1
                return record, None
            left, right = split(interval)
            stack.append((cell, depth+1, 2*path+1, right))
            stack.append((cell, depth+1, 2*path, left))
        record.update(state="certified_represented_polynomial", processed_nodes=nodes,
            certified_leaves=len(closed), reached_depth=maximum_depth,
            continuous_outward_bound_LD_decimal=[ld_text(total_lo), ld_text(total_hi)],
            continuous_outward_bound_float_for_display_only=[float(total_lo), float(total_hi)])
        COUNTS["closed_polynomial_fields"] += 1
        COUNTS["closed_polynomial_nodes"] += nodes
        return record, closed if capture_leaves else None

    def certify(self, graph, q, alpha, length):
        started = time.monotonic()
        report = self.latest_record = {"state":"pending", "fields":{},
            "same_represented_quintic_basis_q_alpha_and_L":True,
            "physical_limits_relaxed":False,
            "floating_derivative_coefficients_not_treated_as_exact_derivative":True,
            "original_coefficients_and_integrals_not_interval_enclosed_by_this_operation":True,
            "eta_continuous_qualification_not_inferred_from_sampled_eta":True}
        try:
            all_coefficients = self.physical_coefficients(graph, q, alpha, length)
            for name, coefficients in all_coefficients.items():
                current, _ = self.certify_field(name, coefficients)
                report["fields"][name] = current
                if current["state"] != "certified_represented_polynomial":
                    report["state"] = current["state"]
                    report["unevaluated_fields"] = [v for v in all_coefficients if v not in report["fields"]]
                    return report
            report["state"] = "all_four_represented_polynomial_fields_certified"
            return report
        finally:
            if (self.active_polynomial_field is not None
                    and self.active_polynomial_field["state"] == "pending"):
                report["inflight_polynomial_field"] = self.active_polynomial_field
            report["seconds"] = time.monotonic()-started
            COUNTS["all_field_calls"] += 1
            COUNTS["all_field_seconds"] += report["seconds"]

    @staticmethod
    def leaf_caps(current, direction, target):
        """Sufficient all-coefficient cap and necessary endpoint cap."""
        clo, chi = current; dlo, dhi = direction
        lower, upper = BOUNDS["h"]
        safe, possible = LD(target), LD(target)
        positive, negative = dhi > 0, dlo < 0
        if np.any(positive):
            safe = min(safe, np.min(down(down(upper-chi[positive])/dhi[positive])))
        if np.any(negative):
            safe = min(safe, np.min(down(down(clo[negative]-lower)/(-dlo[negative]))))
        for j in (0, -1):
            if dlo[j] > 0:
                possible = min(possible, up(up(upper-clo[j])/dlo[j]))
            if dhi[j] < 0:
                possible = min(possible, up(up(chi[j]-lower)/(-dhi[j])))
        return max(LD(0), safe), max(LD(0), possible)

    def height_fraction(self, graph, q, direction, maximum=1., safety=.95):
        """Same-tree current/direction subdivision; no coarse height wall."""
        started = time.monotonic()
        report = self.latest_height_fraction = {"state":"pending",
            "all_original_height_and_L_bounds_retained":True,
            "current_and_direction_use_identical_cell_subdivisions":True,
            "actual_rounded_trial_is_rechecked_before_any_acceptance":True}
        try:
            q, direction = np.asarray(q, dtype=LD), np.asarray(direction, dtype=LD)
            target = up(LD(maximum)/LD(safety))
            length, change = q[-1], direction[-1]
            if change > 0:
                target = min(target, down(down(LD("7.9")-length)/change))
            elif change < 0:
                target = min(target, down(down(length-LD("2.1"))/(-change)))
            if target <= 0:
                report.update(state="original_L_active_no_outward_fraction", fraction=0.)
                return 0.
            current_coeff = affine_coefficients(graph.h_coeff[0], q)
            direction_coeff = affine_coefficients(graph.h_coeff[0], direction)
            current_report, leaves = self.certify_field("h", current_coeff, capture_leaves=True)
            report["current_height"] = current_report
            if leaves is None:
                report.update(state="pending", reason="current_height_not_closed")
                raise PolynomialPhysicalPending(report)
            queue, serial, possible = [], 0, target
            for cell, depth, path, current in leaves:
                delta = restrict((direction_coeff[0][:, cell], direction_coeff[1][:, cell]), path, depth)
                safe, point_cap = self.leaf_caps(current, delta, target)
                possible = min(possible, point_cap)
                heapq.heappush(queue, (safe, serial, cell, depth, path, current, delta)); serial += 1
            nodes, deepest = len(queue), max(v[3] for v in queue)
            while True:
                try:
                    self.check("height_fraction", nodes)
                except Exception:
                    report.update(state="pending", reason="clock_with_affine_height_frontier",
                        processed_nodes=nodes, reached_depth=deepest,
                        unresolved_frontier=[{"cell":v[2], "depth":v[3], "path":v[4],
                            "current":interval_record(v[5]), "direction":interval_record(v[6])} for v in queue])
                    raise
                safe, _, cell, depth, path, current, delta = queue[0]
                if safe >= target or safe >= LD(".99")*possible:
                    fraction = min(LD(maximum), down(LD(safety)*safe))
                    answer = float(fraction)
                    if LD(answer) > fraction:
                        answer = float(np.nextafter(answer, -np.inf))
                    report.update(state="safe_affine_height_fraction", fraction=max(0., answer),
                        certified_safe_cap_LD_decimal=ld_text(safe),
                        necessary_endpoint_cap_LD_decimal=ld_text(possible),
                        processed_nodes=nodes, reached_depth=deepest,
                        simultaneous_height_family_enclosed_before_trial_rounding=True)
                    return max(0., answer)
                if nodes+2 > self.maximum_nodes or depth >= self.maximum_depth:
                    report.update(state="pending", reason="affine_height_fraction_refinement_budget",
                        processed_nodes=nodes, reached_depth=deepest,
                        safe_cap_LD_decimal=ld_text(safe), possible_cap_LD_decimal=ld_text(possible),
                        unresolved_frontier=[{"cell":v[2], "depth":v[3], "path":v[4],
                            "current":interval_record(v[5]), "direction":interval_record(v[6])} for v in queue],
                        current_q=[float(v) for v in q], direction=[float(v) for v in direction],
                        pending_is_not_infeasibility_or_a_rejected_full_trial=True)
                    raise PolynomialPhysicalPending(report)
                heapq.heappop(queue)
                current_children, direction_children = split(current), split(delta)
                COUNTS["affine_height_leaf_refinements_including_partial"] += 1
                for side in (0, 1):
                    child, dchild = current_children[side], direction_children[side]
                    child_safe, point_cap = self.leaf_caps(child, dchild, target)
                    possible = min(possible, point_cap)
                    heapq.heappush(queue, (child_safe, serial, cell, depth+1, 2*path+side, child, dchild))
                    serial += 1; nodes += 1; deepest = max(deepest, depth+1)
        finally:
            if report["state"] == "pending":
                report["current_q"] = [float(v) for v in q]
                report["direction"] = [float(v) for v in direction]
                if self.active_polynomial_field is not None:
                    report["current_height_including_partial"] = self.active_polynomial_field
            report["seconds"] = time.monotonic()-started
            COUNTS["adaptive_height_fraction_calls"] += 1
            COUNTS["adaptive_height_fraction_seconds"] += report["seconds"]
