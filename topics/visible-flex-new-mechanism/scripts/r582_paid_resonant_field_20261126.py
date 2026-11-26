#!/usr/bin/env python3
"""The paid actual R582 flat direction, sampled for a new finite nonround input.

No new inner DtN calculation and no old three-seed comparison is performed.
One NEW dense outward transfer is paid because the old logs saved mouth jets,
not an interior dense field. Endpoint jets define one common C2 Hermite
numerical material field; its actual polynomial derivatives are used.
Its numerical inner-tail omission and interpolation error are explicit.
The numerical seed has a zero suffix. The intended mathematical reference
is the infinite flat kernel; these are not asserted to be the same C2
function or to differ by a certified C2 error. All science is in Actions.
"""
from collections import defaultdict
import hashlib
import math
from pathlib import Path
import time

import numpy as np
from scipy.integrate import solve_ivp

BINDINGS = {
    "r582_actual_circle_seed_and_return_20261126.py":
        "fd4bd864c3e9e96d741b7bc896a1bf6f9d50ba54eda0c02bd898f21bd42427a4",
    "r582_continuous_mean_profile_20261126.py":
        "35060aa3e862c4852b30396493be37d1bd688281b4a093bd1e532d964e562631",
    "r582_true_core_shooting_20261126.py":
        "c7f445b98cc948fb7fc920c910aed25bd60e9b14af5971de62d3c9bc3301f534",
}
for filename, expected in BINDINGS.items():
    if hashlib.sha256(Path(__file__).with_name(filename).read_bytes()).hexdigest() != expected:
        raise RuntimeError("resonant field source binding differs: " + filename)
import r582_actual_circle_seed_and_return_20261126 as paid_source
from r582_continuous_mean_profile_20261126 import ContinuousMean
from r582_true_core_shooting_20261126 import TrueShoot

SCHEMA = "paid-r582-new-dense-flat-field-and-exact-core-matching-v1"
LENGTH, CORE_END, ELL = paid_source.LENGTH, paid_source.CORE_END, paid_source.ELL
ClockCheckpoint = paid_source.ClockCheckpoint
REFERENCE_CONTROL = np.array([-.040019082162222074, -.048942275258064924])
PAID_REFINED_NORMALIZATION = 7.136787019826327
BLEND_LEFT, BLEND_RIGHT = .78, .80
REFERENCE_CORE_RADIUS = .38
MATERIAL_KNOT_MERGE_TOLERANCE = 1e-13


def material_knots_with_interfaces(candidates, interfaces):
    """Merge numerical near-duplicates while preserving each named interface.

    Integration and u-to-s conversion can represent the same endpoint by
    neighboring binary64 numbers. Such an artificial one-ulp interval would
    amplify unrelated endpoint roundoff through its Hermite derivatives.
    Named interfaces win; every other retained point is separated from its
    neighbors by the explicit new sampling tolerance. No old scientific
    geometry or accepted constraint node is being coarsened here.
    """
    protected = np.asarray(sorted(set(float(x) for x in interfaces)), dtype=float)
    if np.any(np.diff(protected) <= MATERIAL_KNOT_MERGE_TOLERANCE):
        raise ValueError("distinct named material interfaces are too close")
    retained = list(protected)
    last = -np.inf
    for point in np.sort(np.asarray(candidates, dtype=float).ravel()):
        if not np.isfinite(point) or not 0 <= point <= LENGTH:
            raise ValueError("nonfinite or out-of-domain material knot")
        if np.min(abs(protected - point)) <= MATERIAL_KNOT_MERGE_TOLERANCE:
            continue
        if point - last > MATERIAL_KNOT_MERGE_TOLERANCE:
            retained.append(float(point))
            last = float(point)
    result = np.asarray(sorted(retained), dtype=float)
    if np.any(np.diff(result) <= MATERIAL_KNOT_MERGE_TOLERANCE):
        raise ArithmeticError("material near-duplicate merge left a short interval")
    return result


def scaled_components(values, log_scale):
    values = np.asarray(values, dtype=float)
    result = np.zeros_like(values)
    active = values != 0
    logarithms = np.log(abs(values[active])) + log_scale
    if np.any(logarithms > np.log(np.finfo(float).max)):
        raise FloatingPointError("new dense resonant field scaling overflow")
    with np.errstate(under="ignore"):
        result[active] = np.sign(values[active]) * np.exp(logarithms)
    return result


# Exact rational endpoint Hermite basis, never fitted or expanded into
# data-dependent global-power coefficients. The six rows represent endpoint
# value/first/second data at left, then right.
HERMITE_COEFFICIENTS = np.array([
    [1., 0., 0., -10., 15., -6.],
    [0., 1., 0., -6., 8., -3.],
    [0., 0., .5, -1.5, 1.5, -.5],
    [0., 0., 0., 10., -15., 6.],
    [0., 0., 0., -4., 7., -3.],
    [0., 0., 0., .5, -1., .5],
])


def endpoint_hermite(knots, endpoint_jets, positions):
    """Value and actual first/second derivatives of one common C2 spline."""
    x = np.atleast_1d(np.asarray(positions, dtype=float))
    if np.any(x < knots[0]) or np.any(x > knots[-1]):
        raise ValueError("material Hermite query outside its complete interval")
    index = np.clip(np.searchsorted(knots, x, side="right") - 1, 0, len(knots) - 2)
    width = knots[index + 1] - knots[index]
    t = (x - knots[index]) / width
    left, right = endpoint_jets[index], endpoint_jets[index + 1]
    data = np.stack((left[:, :, 0], width[:, None] * left[:, :, 1],
        width[:, None] ** 2 * left[:, :, 2], right[:, :, 0],
        width[:, None] * right[:, :, 1], width[:, None] ** 2 * right[:, :, 2]), axis=1)
    coefficients = HERMITE_COEFFICIENTS.copy()
    output = np.empty((len(x), 2, 3))
    for order in range(3):
        basis = np.stack([np.polynomial.polynomial.polyval(t, c) for c in coefficients], axis=1)
        output[:, :, order] = np.einsum("ij,ijk->ik", basis, data) / width[:, None] ** order
        coefficients = coefficients[:, 1:] * np.arange(1, coefficients.shape[1])
    return output.reshape(len(x), 6)


class PaidDenseTail:
    def __init__(self, paid, args, deadline, counts):
        self.paid, self.args, self.deadline, self.counts = paid, args, deadline, counts
        self.actual = paid_source.ActualTail(paid_source.SOURCE_Q, deadline)
        last = paid["compact_seed_inputs"][-1]
        if last["M"] != 169 or last["tolerance_factor"] != 8:
            raise ValueError("the actual paid M169/factor8 terminal is required")
        inner, self.mouth = last["inner"], last["outer"]
        self.alpha = float(inner["alpha160"])
        self.log_normalization = (math.log(PAID_REFINED_NORMALIZATION)
                                  - self.mouth["canonical_to_mouth_C2_log_scale"])
        self.segments = []
        self.last_completed, self.last_partial = None, None
        state, high, log_scale = np.array([1., inner["z_alpha160"]]), self.alpha, 0.
        low_goal = float(self.mouth["mouth_u"])
        centers = np.pi / 2 + 2 * np.pi * np.arange(paid_source.FIRST_PEAK + 1)
        stops = np.r_[np.sort(centers[(centers < high) & (centers > low_goal)])[::-1], low_goal]
        self.counts["new_dense_tail_transfers"] += 1
        for low in stops:
            self.check()
            self.last_partial = {"high_u": float(high), "low_u": float(low),
                "normalized_initial_y_z": state.tolist(), "canonical_log_scale_before": log_scale,
                "not_a_completed_dense_field": True}
            sol = self.actual.integrate(float(high), float(low), state, args, dense=True, factor=8)
            self.counts["new_dense_tail_RHS"] += int(sol.nfev)
            self.counts["new_dense_tail_segments"] += 1
            self.segments.append((float(low), float(high), sol, log_scale))
            outgoing = sol.y[:, -1]
            scale = float(np.max(abs(outgoing)))
            if not scale > 0 or not np.isfinite(scale):
                raise ArithmeticError("new dense tail transfer lost its projective scale")
            state, high = outgoing / scale, float(low)
            log_scale += math.log(scale)
            self.last_completed = {"u": high, "normalized_y_z": state.tolist(),
                "canonical_log_scale": log_scale, "completed_segments": len(self.segments),
                "new_dense_tail_RHS": self.counts["new_dense_tail_RHS"]}
        self.last_partial = None
        self.mouth_jets = self.evaluate(np.array([float(self.mouth["mouth_s"])]))[0]
        expected = PAID_REFINED_NORMALIZATION * np.asarray(self.mouth["normalized_jets_A_As_Ass_C_Cs_Css"])
        self.mouth_difference = (self.mouth_jets - expected).tolist()

    def check(self):
        if time.monotonic() >= self.deadline:
            raise ClockCheckpoint("clock while building or sampling the new dense tail field")

    def evaluate(self, positions):
        self.check()
        s = np.atleast_1d(np.asarray(positions, dtype=float))
        if np.any(s < self.mouth["mouth_s"] - 2e-15) or np.any(s > LENGTH):
            raise ValueError("dense tail query left its actual suffix")
        self.counts["dense_tail_radial_queries"] += s.size
        result = np.zeros((len(s), 6))
        active = s < LENGTH
        u = np.full(len(s), np.inf)
        u[active] = (ELL / (LENGTH - s[active])) ** 2
        omitted = active & (u >= self.alpha)
        self.counts["uncomputed_inner_tail_query_points"] += int(np.sum(omitted))
        remaining = active & ~omitted
        for low, high, sol, logarithm in self.segments:
            selected = remaining & (u >= low - 1e-12) & (u <= high + 1e-12)
            for index in np.flatnonzero(selected):
                value = min(high, max(low, float(u[index])))
                state = sol.sol(value)
                jets = self.actual.field_jets(value, state)
                result[index] = scaled_components(jets, logarithm + self.log_normalization)
                self.counts["underflowed_nonzero_jet_components"] += int(
                    np.sum((jets != 0) & (result[index] == 0)))
            remaining[selected] = False
        if np.any(remaining):
            raise ArithmeticError("new dense tail field did not cover every requested finite u")
        return result

    def receipt(self):
        return {"schema": SCHEMA, "paid_M": 169, "paid_tolerance_factor": 8,
            "new_inner_DtN_transfers": 0, "new_old_three_seed_comparisons": 0,
            "new_dense_outward_transfer_because_old_logs_did_not_store_interior_field": True,
            "new_dense_tail_RHS": self.counts["new_dense_tail_RHS"],
            "new_dense_tail_segments": self.counts["new_dense_tail_segments"],
            "same_paid_refined_normalization": PAID_REFINED_NORMALIZATION,
            "new_dense_mouth_minus_paid_normalized_six_jets": self.mouth_difference,
            "numerical_uncomputed_inner_tail_starts_u": self.alpha,
            "numerical_uncomputed_inner_tail_starts_s": LENGTH - ELL / math.sqrt(self.alpha),
            "intended_mathematical_reference_is_the_R582_infinite_flat_kernel": True,
            "numerical_representation_omits_inner_tail_and_has_zero_seed_suffix": True,
            "numerical_Hermite_seed_is_not_identified_with_the_infinite_kernel": True,
            "infinite_reference_minus_numerical_seed_C2_error_certified": False,
            "finite_DtN_and_numeric_ODE_error_not_certified": True,
            "numerical_inner_tail_value_omission_not_a_rigorous_error_bound": True,
            "canonical_alpha160_to_mouth_C2_log_scale": self.mouth["canonical_to_mouth_C2_log_scale"]}


class ResonantField:
    def __init__(self, paid, prior_chart, args, deadline):
        self.args, self.deadline = args, deadline
        self.counts = defaultdict(int)
        self.cache = {}
        if (prior_chart["continuous_positive_z_s_chart_established"] is not True
                or prior_chart["scope_s"][0] != CORE_END
                or prior_chart["scope_s"][1] < .82
                or not prior_chart["scope_nu"][0] <= REFERENCE_CONTROL[1] <= prior_chart["scope_nu"][1]):
            raise ValueError("the paid continuous positive chart does not cover the frozen reference")
        self.chart = prior_chart
        self.tail = PaidDenseTail(paid, args, deadline, self.counts)
        self.mean = ContinuousMean(deadline, self.counts)
        self.shooter = TrueShoot(self.mean, self.tail.mouth, args, self.counts, deadline)
        self.shooter.chart = prior_chart

        def integrate(left, right, initial, key):
            self.counts[key + "_calls"] += 1
            def rhs(s, y):
                self.check()
                self.counts[key + "_RHS"] += 1
                M, _, _, _ = self.shooter.matrix(float(s), REFERENCE_CONTROL)
                return M @ y
            sol = solve_ivp(rhs, (left, right), np.asarray(initial), method="DOP853",
                rtol=args.rtol / 8, atol=args.atol / 8, max_step=.005, dense_output=True)
            if not sol.success:
                raise ArithmeticError("new s-field transfer failed: " + sol.message)
            return sol

        self.core_forward = integrate(CORE_END, .82, [.5, 0.], "new_exact_core_forward")
        tail_initial = self.tail.mouth_jets[[0, 3]]
        self.tail_backward = integrate(.82, BLEND_LEFT, tail_initial, "new_short_tail_backward")
        self.core_to_paid_mouth_difference = (self.core_forward.y[:, -1] - tail_initial).tolist()

        # The new finite geometry uses a single C2 Hermite material field.
        # ODE dense output is used only to supply its endpoint data; arbitrary
        # point derivatives below are derivatives of the Hermite polynomial.
        tail_knots = np.concatenate([LENGTH - ELL / np.sqrt(item[2].t)
                                     for item in self.tail.segments])
        interfaces = np.r_[0., CORE_END, LENGTH, BLEND_LEFT, BLEND_RIGHT, .82,
            paid_source.CONTROL_LEFT, paid_source.CONTROL_RIGHT,
            CORE_END + (LENGTH - CORE_END) * np.array([1/3, 2/3])]
        candidates = np.r_[
            np.linspace(CORE_END, .82, 257),
            self.core_forward.t, self.tail_backward.t, tail_knots]
        self.material_knots = material_knots_with_interfaces(candidates, interfaces)
        self.counts["material_raw_knot_candidates"] = len(candidates) + len(interfaces)
        if (np.any(np.diff(self.material_knots) <= 0)
                or np.any((self.material_knots[:-1] > 0)
                          & (self.material_knots[1:] > 2 * self.material_knots[:-1]))):
            raise ArithmeticError("material knot widths left the exact-subtraction range")
        # Sterbenz: every positive adjacent subtraction here is exact;
        # the sole left=0 interval has width equal to its exact right endpoint.
        values = np.empty((len(self.material_knots), 6))
        tail_nodes = self.material_knots >= .82
        values[tail_nodes] = self.tail.evaluate(self.material_knots[tail_nodes])
        for index in np.flatnonzero(~tail_nodes):
            values[index] = self.ode_one(float(self.material_knots[index]))
        if not np.all(np.isfinite(values)):
            raise FloatingPointError("nonfinite material endpoint jets")
        self.material_endpoint_jets = values.reshape(-1, 2, 3)
        self.counts["new_material_Hermite_endpoints"] = len(self.material_knots)
        self.material_mesh_sha256 = hashlib.sha256(
            self.material_knots.tobytes() + values.tobytes()).hexdigest()

    def check(self):
        if time.monotonic() >= self.deadline:
            raise ClockCheckpoint("clock in new resonant field evaluation")

    def ode_jets(self, solution, s):
        field = solution.sol(float(s))
        M, _, Ms, _ = self.shooter.matrix(float(s), REFERENCE_CONTROL)
        first = M @ field
        second = Ms @ field + M @ first
        return np.array([field[0], first[0], second[0], field[1], first[1], second[1]])

    def ode_one(self, s):
        self.check()
        self.counts["resonant_field_queries"] += 1
        s = float(s)
        if s in self.cache:
            self.counts["resonant_field_cache_hits"] += 1
            return self.cache[s].copy()
        if not 0 <= s <= LENGTH:
            raise ValueError("resonant field query outside [0,L]")
        if s <= CORE_END:
            value = np.array([.5, 0., 0., 0., 0., 0.])
        elif s >= .82:
            value = self.tail.evaluate([s])[0]
        elif s <= BLEND_LEFT:
            value = self.ode_jets(self.core_forward, s)
        elif s >= BLEND_RIGHT:
            value = self.ode_jets(self.tail_backward, s)
        else:
            core = self.ode_jets(self.core_forward, s).reshape(2, 3)
            tail = self.ode_jets(self.tail_backward, s).reshape(2, 3)
            chi, comp, first, second = (float(x[0]) for x in
                ContinuousMean.step_jets(np.array([s]), BLEND_LEFT, BLEND_RIGHT))
            delta = tail - core
            value = core.copy()
            value[:, 0] += chi * delta[:, 0]
            value[:, 1] += chi * delta[:, 1] + first * delta[:, 0]
            value[:, 2] += chi * delta[:, 2] + 2 * first * delta[:, 1] + second * delta[:, 0]
            value = value.ravel()
        self.cache[s] = value.copy()
        return value

    def evaluate(self, positions):
        self.check()
        self.counts["material_Hermite_radial_queries"] += np.asarray(positions).size
        return endpoint_hermite(self.material_knots, self.material_endpoint_jets, positions)

    def angular_radial_jets(self, positions, bg_comp, bg_first, bg_second):
        s = np.asarray(positions, dtype=float)
        jets = self.evaluate(s)
        mean, _ = self.mean.jets(s, REFERENCE_CONTROL)
        a, a1, a2 = mean[:3]
        def quotient(start, factor):
            v, v1, v2 = jets[:, start:start + 3].T
            return factor * np.stack((v/a, v1/a-v*a1/a**2,
                v2/a-2*v1*a1/a**2-v*a2/a**2+2*v*a1*a1/a**3), axis=1)
        uj, vj = quotient(0, 1.5), quotient(3, -2.)
        core_derivative = 3 / (4 * REFERENCE_CORE_RADIUS)
        uj[:, 0] -= np.asarray(bg_comp).ravel() * core_derivative
        uj[:, 1] += np.asarray(bg_first).ravel() * core_derivative
        uj[:, 2] += np.asarray(bg_second).ravel() * core_derivative
        return uj, vj

    def receipt(self):
        return {"schema": SCHEMA, "reference_mean_control": REFERENCE_CONTROL.tolist(),
            "prior_continuous_chart_reused_for_the_identical_frozen_reference_only": self.chart,
            "core_field_exact_boundary_data_A_C": [.5, 0.],
            "core_forward_minus_new_dense_tail_at_mouth_A_C": self.core_to_paid_mouth_difference,
            "complete_two_jet_blend_support_s": [BLEND_LEFT, BLEND_RIGHT],
            "blend_defect_remains_in_the_actual_nonlinear_metric_residual": True,
            "material_field_evaluator": "common-endpoint C2 piecewise quintic Hermite",
            "actual_value_first_second_derivatives_use_the_same_endpoint_basis": True,
            "all_positive_segment_widths_exact_by_Sterbenz": True,
            "material_Hermite_endpoints": len(self.material_knots),
            "material_near_duplicate_merge_tolerance": MATERIAL_KNOT_MERGE_TOLERANCE,
            "named_interfaces_preserved_before_near_duplicate_merge": True,
            "material_mesh_binary64_sha256": self.material_mesh_sha256,
            "ODE_only_generates_endpoint_data_not_arbitrary_material_derivatives": True,
            "ODE_and_Hermite_interpolation_error_not_interval_certified": True,
            "numerical_Hermite_seed_has_zero_suffix_and_differs_from_infinite_reference": True,
            "infinite_reference_minus_numerical_seed_C2_error_certified": False,
            "tail": self.tail.receipt(), "new_counts": dict(self.counts),
            "old_paid_cost_is_not_part_of_these_new_counts": True,
            "fixed_metric_refinement_or_finite_family_proof": False}
