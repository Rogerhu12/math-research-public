#!/usr/bin/env python3
"""Same R636 polynomial-background curve; exact-structure-zero interval sums.

No represented q, basis coefficient, background, physical limit, or integral
is changed. Only terms with a zero FACTOR are skipped by the enclosure sum.
A product of two nonzero factors that underflows to zero is still enclosed.
"""
from __future__ import annotations

import heapq
import time
import numpy as np

import r636_polynomial_background_kinetic_chart as base
import r632_adaptive_polynomial_boxes as adaptive
from r636_polynomial_background_kinetic_chart import (
    LD, Jet, reduced, paid, COUNTS, identity, ld_text, physical_attainers,
    IntegralGrid, legacy, original, BACKGROUND)
from r632_adaptive_polynomial_boxes import (
    down, up, restrict, split, interval_record, PolynomialPhysicalPending)


def sparse_affine_coefficients(basis, q, offset=None):
    """Enclose exact sums of represented inputs without rounding exact zeros.

    Masking uses basis==0 or q==0, never product==0. Thus multiplication
    underflow between two nonzero factors retains the outward enclosure.
    """
    basis, q = np.asarray(basis,dtype=LD), np.asarray(q,dtype=LD)
    lo = np.zeros(basis.shape[:-1],dtype=LD) if offset is None else np.asarray(offset,dtype=LD).copy()
    hi = lo.copy()
    paid_terms = 0
    for j,value in enumerate(q):
        if value == 0:
            continue
        nonzero_factor = basis[...,j] != 0
        if not np.any(nonzero_factor):
            continue
        product = basis[...,j][nonzero_factor]*value
        lo[nonzero_factor] = down(lo[nonzero_factor]+down(product))
        hi[nonzero_factor] = up(hi[nonzero_factor]+up(product))
        paid_terms += int(np.count_nonzero(nonzero_factor))
    if not np.all(np.isfinite(lo)) or not np.all(np.isfinite(hi)):
        raise FloatingPointError("Nonfinite exact-input background polynomial coefficient enclosure")
    adaptive.COUNTS["structure_zero_affine_calls"] += 1
    adaptive.COUNTS["structure_zero_affine_all_columns_retained"] += len(q)
    adaptive.COUNTS["nonzero_factor_products_outward_enclosed"] += paid_terms
    return lo,hi


class BackgroundPolynomialBoxes(adaptive.AdaptivePolynomialBoxes):
    def physical_coefficients(self,graph,q,alpha,length):
        h = sparse_affine_coefficients(graph.h_coeff[0],q,graph.background_h_coeff[0])
        kappa = sparse_affine_coefficients(graph.k_coeff[0],q,graph.background_k_coeff[0])
        return {"h":h,"k":adaptive.positive_scale(kappa,alpha),
            "gamma":adaptive.positive_divide(adaptive.derivative(h,self.knots),length),
            "upsilon":adaptive.positive_divide(adaptive.positive_scale(
                adaptive.derivative(kappa,self.knots),alpha),length)}

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
            current_coeff = sparse_affine_coefficients(graph.h_coeff[0], q, graph.background_h_coeff[0])
            direction_coeff = sparse_affine_coefficients(graph.h_coeff[0], direction)
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
                adaptive.COUNTS["affine_height_leaf_refinements_including_partial"] += 1
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
            adaptive.COUNTS["adaptive_height_fraction_calls"] += 1
            adaptive.COUNTS["adaptive_height_fraction_seconds"] += report["seconds"]

class AdaptiveBackgroundChart(base.PolynomialBackgroundChart):
    def __init__(self,knots,grid,clock,maximum_nodes=32768,maximum_depth=40):
        super().__init__(knots,grid,clock)
        self.boxes = BackgroundPolynomialBoxes(knots,clock,maximum_nodes,maximum_depth)

    def height_fraction(self,q,direction,maximum=1.,safety=.95):
        return self.boxes.height_fraction(self,q,direction,maximum,safety)

    def evaluate(self, parameters, derivatives=True, fixed_alpha=None, fixed_center=None,
                 enforce_box=True):
        reduced.require_public_science()
        if (derivatives and fixed_alpha is None and fixed_center is None and enforce_box
                and self.cache_parameters is not None
                and np.array_equal(np.asarray(parameters,float),self.cache_parameters)):
            COUNTS["R636_same_shape_complete_chain_cache_reuses"]+=1
            self.latest_geometry=self.cache_curve["physical_attainers"]
            self.latest_curve=self.cache_curve
            return self.cache_curve
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
        h = [offset+basis@np.asarray(q, dtype=LD) for offset,basis in zip(self.background_h,self.h_basis)]
        k = [off+basis@np.asarray(q, dtype=LD) for off,basis in zip(self.background_k,self.k_basis)]
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
        hc = self.background_h_coeff[0]+np.einsum("ijk,k->ij", self.h_coeff[0], np.asarray(q, dtype=LD))
        kc = self.background_k_coeff[0]+np.einsum("ijk,k->ij", self.k_coeff[0], np.asarray(q, dtype=LD))
        hg = (self.background_h_coeff[1]+np.einsum("ijk,k->ij", self.h_coeff[1], np.asarray(q, dtype=LD)))/length.value
        kg = (self.background_k_coeff[1]+np.einsum("ijk,k->ij", self.k_coeff[1], np.asarray(q, dtype=LD)))*alpha.value/length.value
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
            fixed_center_kappa_x=ld_text(self.c), fixed_polynomial_background=BACKGROUND,
            shape_coordinates_are_perturbations_about_exact_R636_background=True, physical_center_v=float(geometry[0][4].value),
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
            "fixed_physical_alpha_and_center":fixed_alpha is not None,
            "fixed_polynomial_background":BACKGROUND}
        self.latest_curve = curve
        if derivatives and fixed_alpha is None and fixed_center is None and enforce_box:
            self.cache_parameters=q.copy()
            self.cache_curve=curve
        COUNTS["true_curve_evaluations"] += 1
        COUNTS["true_curve_seconds"] += time.monotonic()-start
        self.clock.check("after_R632_true_geometry_memory_and_end_chain")
        return curve
