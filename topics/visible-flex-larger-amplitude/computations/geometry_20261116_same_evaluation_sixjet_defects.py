#!/usr/bin/env python3
"""R519 same-evaluation six-jet diagnostics for an accurately defined field.

Pure rational-endpoint arithmetic for cells which an existing metric consumer
has already evaluated. This helper does not evaluate a field, query C, solve
an ODE, scan a domain, integrate a defect, or change a scientific gate.

The two Frenet velocities are algebraic reference constructions. Neither is
identified with the original worker's selected root or floating RHS. Their
defects and Gram majorants are optional local enclosures, not a solver-error
estimate or a whole-domain tolerance floor.

Author: exact_refinement agent (AI), 2026-11-16.
"""
from __future__ import annotations

import copy
from fractions import Fraction as Q
import math

SCHEMA = "R519-same-evaluation-sixjet-local-defect-v1"
CONTEXT_SCHEMA = "R519-same-evaluation-target-context-v1"
SUMMARY_SCHEMA = "R519-same-evaluation-sixjet-local-diagnostic-summary-v1"
JET_NAMES = ("value", "x", "q", "xx", "xq", "qq")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def rational(value):
    require(type(value) in (int, str, Q),
            "Use the already bound exact rational endpoints, never a float midpoint")
    return Q(value)


def interval(value):
    require(isinstance(value, (tuple, list)) and len(value) == 2,
            "An interval must retain both endpoints")
    lo, hi = map(rational, value)
    require(lo <= hi, "An interval endpoint pair is reversed")
    return lo, hi


def encode(value):
    return None if value is None else [str(value[0]), str(value[1])]


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def negate(a):
    return -a[1], -a[0]


def subtract(a, b):
    return add(a, negate(b))


def multiply(a, b):
    products = (a[0]*b[0], a[0]*b[1], a[1]*b[0], a[1]*b[1])
    return min(products), max(products)


def scale(a, value):
    return multiply(a, (value, value))


def divide_positive(a, b):
    require(b[0] > 0, "The optional diagnostic denominator is not strictly isolated")
    return multiply(a, (1/b[1], 1/b[0]))


def square(a):
    lo = Q(0) if a[0] <= 0 <= a[1] else min(a[0]*a[0], a[1]*a[1])
    return lo, max(a[0]*a[0], a[1]*a[1])


def absolute_upper(a):
    return max(abs(a[0]), abs(a[1]))


def sqrt_point(value, bits):
    require(value >= 0, "A squared-norm endpoint must be nonnegative")
    denominator = 1 << bits
    integer = math.isqrt((value.numerator << (2*bits))//value.denominator)
    lo = Q(integer, denominator)
    return lo, lo if lo*lo == value else Q(integer+1, denominator)


def sqrt_interval(a, bits):
    require(a[0] >= 0, "An outward squared-norm lower endpoint is negative")
    return sqrt_point(a[0], bits)[0], sqrt_point(a[1], bits)[1]


def dot(a, b):
    answer = (Q(0), Q(0))
    for x, y in zip(a, b):
        answer = add(answer, multiply(x, y))
    return answer


def norm_squared(a):
    answer = (Q(0), Q(0))
    for x in a:
        answer = add(answer, square(x))
    return answer


def cross(a, b):
    return tuple(subtract(multiply(a[i], b[j]), multiply(a[j], b[i]))
                 for i, j in ((1, 2), (2, 0), (0, 1)))


def gram_majorant(delta, q, bits):
    """R514's positive 2 by 2 comparison matrix; no direct Gram replacement."""
    a = 2*delta+delta*delta
    b = delta*(1+q)
    c = 2*q+q*q
    root = sqrt_point((a-c)*(a-c)+4*b*b, bits)[1]
    return (a+c+root)/2


def unavailable(reason, scope, **extra):
    return dict(scope=scope, reason=reason, original_direct_Gram_still_authoritative=True, **extra)


def diagnose(jets, context, sqrt_bits):
    """Consume one actual six-jet result and its same-call target.

    jets is a 6 by 3 list in JET_NAMES order, each entry an exact endpoint
    pair obtained from the original field interval API. Only x,q,xq,qq enter
    these formulas. All six are supplied without another evaluation.

    A prefix context supplies a_s in the true scalar-length coordinate.
    Its actual coordinate derivative is A_x = a_s*sqrt(g11): x=s_numeric
    at base phase and x=public_u for the common-material phase queries.
    A radial context has A=r, A_x=1 and g11=the same complete-C E enclosure.
    Phi_q is independent of x in the bound material construction.
    """
    require(type(sqrt_bits) is int and 32 <= sqrt_bits <= 8192,
            "Use the existing declared metric square-root precision")
    require(isinstance(jets, (tuple, list)) and len(jets) == 6
            and all(isinstance(row, (tuple, list)) and len(row) == 3 for row in jets),
            "Keep the actual complete Cartesian six-jet layout")
    values = tuple(tuple(interval(value) for value in row) for row in jets)
    require(isinstance(context, dict) and context.get("schema") == CONTEXT_SCHEMA,
            "Use a source-bound same-evaluation target context")
    require(context.get("coordinate") in ("prefix_numeric_s", "prefix_public_u", "radial_r"),
            "Do not confuse the prefix numerical and common-public coordinates")
    require(context.get("angular_map_independent_of_radial_coordinate") is True,
            "This conditional identity uses the actual fixed material map")
    A = interval(context["radius"])
    mu2 = interval(context["radial_metric"])
    theta = interval(context["angular_density"])
    derivative_rule = context["radius_derivative_rule"]
    require(derivative_rule in ("accurate_a_s_times_positive_sqrt_g11", "radial_identity"),
            "Retain the original accurate scalar derivative rule")
    report = dict(schema=SCHEMA, coordinate=context["coordinate"],
        jet_order=list(JET_NAMES), consumed_components=["x", "q", "xq", "qq"],
        same_existing_field_evaluation=True, same_existing_target_evaluation=True,
        full_six_jet_payload_copied=False, extra_field_or_C_query_count=0,
        sqrt_bits=sqrt_bits, angular_ratio_available=False,
        radial_angular_defect_available=False, algebraic_reference_velocities_available=False,
        unpaid=[], reference_branches=[],
        target_bounds=dict(radius=encode(A), radial_metric=encode(mu2), angular_density=encode(theta)),
        no_original_worker_branch_or_IEEE_RHS_error_claim=True,
        no_BC_anchor_or_radial_integral_or_stability_bound_formed=True,
        no_native_RMS_to_metric_tolerance_floor_claim=True,
        original_direct_Gram_not_replaced=True)
    if A[0] <= 0:
        report["unpaid"].append(unavailable("positive_target_radius_not_isolated", "angular_and_Frenet"))
    if theta[0] <= 0:
        report["unpaid"].append(unavailable("positive_bound_material_density_not_isolated", "angular"))
    if mu2[0] <= 0:
        report["unpaid"].append(unavailable("positive_target_radial_metric_not_isolated", "Frenet"))
    if A[0] <= 0 or theta[0] <= 0:
        return report
    vx, d, mixed, e = values[1], values[2], values[4], values[5]
    q2 = norm_squared(d)
    dnorm = sqrt_interval(q2, sqrt_bits)
    angular_target_scale = multiply(A, theta)
    h = divide_positive(dnorm, angular_target_scale)
    h_minus_one = subtract(h, (Q(1), Q(1)))
    angular_error = absolute_upper(h_minus_one)
    report.update(angular_ratio_available=True, angular_ratio_interval=encode(h),
        angular_ratio_minus_one=encode(h_minus_one),
        angular_ratio_error_upper=str(angular_error),
        current_angular_squared_norm=encode(q2),
        h_definition="|F_q|/(A*Phi_q)")
    if mu2[0] <= 0:
        return report
    mu = sqrt_interval(mu2, sqrt_bits)
    if mu[0] <= 0:
        report["unpaid"].append(unavailable(
            "positive_target_square_root_lower_unresolved_at_declared_precision", "radial_and_Frenet",
            positive_radial_metric_already_bound=True, outward_sqrt_interval=encode(mu)))
        return report
    if derivative_rule == "accurate_a_s_times_positive_sqrt_g11":
        require(context["coordinate"] in ("prefix_numeric_s", "prefix_public_u"),
                "The scalar-length pullback belongs to the actual prefix coordinate")
        A_x = multiply(interval(context["accurate_radius_first_derivative"]), mu)
    else:
        require(context["coordinate"] == "radial_r", "Only the original radial coordinate has A_x=1")
        A_x = Q(1), Q(1)
    report["target_bounds"]["radial_speed"] = encode(mu)
    report["target_bounds"]["radius_coordinate_derivative"] = encode(A_x)
    if dnorm[0] > 0:
        numerator = subtract(dot(d, mixed), multiply(divide_positive(A_x, A), q2))
        tau = divide_positive(numerator, multiply(angular_target_scale, dnorm))
        report.update(radial_angular_defect_available=True,
            radial_angular_defect_interval=encode(tau),
            radial_angular_defect_absolute_upper=str(absolute_upper(tau)),
            tau_definition="(F_q.F_xq-(A_x/A)*|F_q|^2)/(A*Phi_q*|F_q|)",
            tau_is_h_x_under_the_bound_radial_independent_material_map=True)
    else:
        report["unpaid"].append(unavailable(
            "positive_current_angular_norm_lower_not_isolated", "radial_angular_defect",
            outward_current_norm=encode(dnorm)))
    c = cross(d, e)
    w = norm_squared(c)
    if w[0] <= 0:
        report["unpaid"].append(unavailable("positive_Frenet_cross_norm_squared_not_isolated", "Frenet",
            closed_cross_norm_squared=encode(w)))
        return report
    q3 = multiply(square(q2), q2)
    p = subtract(multiply(multiply(square(A), mu2), w), multiply(square(A_x), q3))
    if p[0] <= 0:
        report["unpaid"].append(unavailable("positive_Frenet_discriminant_not_isolated", "Frenet",
            closed_discriminant=encode(p),
            no_original_solver_guard_or_target_counterexample_inferred=True))
        return report
    root_p = sqrt_interval(p, sqrt_bits)
    de = dot(d, e)
    bend = tuple(subtract(multiply(q2, ee), multiply(de, dd)) for ee, dd in zip(e, d))
    denominator = multiply(A, w)
    for sigma in (-1, 1):
        velocity = tuple(divide_positive(
            subtract(scale(multiply(root_p, cc), Q(sigma)), multiply(multiply(A_x, q2), bb)),
            denominator) for cc, bb in zip(c, bend))
        defect = tuple(subtract(xx, vv) for xx, vv in zip(vx, velocity))
        delta = sqrt_interval(norm_squared(defect), sqrt_bits)[1]/mu[0]
        report["reference_branches"].append(dict(sigma=sigma, normalized_velocity_defect_upper=str(delta),
            local_relative_Gram_majorant_upper=str(gram_majorant(delta, angular_error, sqrt_bits)),
            accurate_algebraic_constraints="|V|=mu; F_q.V=0; F_qq.V=-(A_x/A)*|F_q|^2",
            reference_is_not_identified_with_original_worker_RHS=True))
    report["algebraic_reference_velocities_available"] = True
    report["Frenet_discriminant"] = encode(p)
    report["Frenet_cross_norm_squared"] = encode(w)
    report["pointwise_branch_choice_does_not_define_a_global_smooth_solver_branch"] = True
    return report


class Collector:
    """Small metadata; every completed observation remains in the actual ledger.

    Counts include repeated evaluations after an actual live-C refinement.
    They do not certify any unvisited cell, pending subtree, or full domain.
    """
    def __init__(self, enabled):
        require(type(enabled) is bool, "The optional diagnostic flag must be a literal bool")
        self.enabled = enabled
        self.counts = dict(observations_started=0, observations_completed=0,
            original_target_unavailable=0, diagnostic_errors=0,
            angular_ratio_available=0, radial_angular_defect_available=0,
            algebraic_reference_velocities_available=0)
        self.by_kind = {}
        self.reasons = {}
        self.maxima = {}
        self.last_started = self.last_completed = None
        self.first_unpaid = self.last_unpaid = None

    def start(self, address):
        self.counts["observations_started"] += 1
        index = self.counts["observations_started"]-1
        self.last_started = dict(observation_index=index, address=copy.deepcopy(address))
        return index

    def complete(self, index, address, report):
        self.counts["observations_completed"] += 1
        kind = address.get("kind", "unspecified")
        self.by_kind[kind] = self.by_kind.get(kind, 0)+1
        self.last_completed = dict(observation_index=index, address=copy.deepcopy(address))
        for key in ("angular_ratio_available", "radial_angular_defect_available",
                    "algebraic_reference_velocities_available"):
            self.counts[key] += int(report.get(key) is True)
        if report.get("original_target_unavailable"):
            self.counts["original_target_unavailable"] += 1
        if report.get("diagnostic_error"):
            self.counts["diagnostic_errors"] += 1
        for row in report.get("unpaid", []):
            key = row["scope"]+":"+row["reason"]
            self.reasons[key] = self.reasons.get(key, 0)+1
        if report.get("unpaid") or report.get("diagnostic_error"):
            point = dict(observation_index=index, address=copy.deepcopy(address),
                reasons=copy.deepcopy(report.get("unpaid", [])),
                diagnostic_error=copy.deepcopy(report.get("diagnostic_error")))
            if self.first_unpaid is None:
                self.first_unpaid = point
            self.last_unpaid = point
        values = {}
        if report.get("angular_ratio_available"):
            values["angular_ratio_error_upper"] = report["angular_ratio_error_upper"]
        if report.get("radial_angular_defect_available"):
            values["radial_angular_defect_absolute_upper"] = report["radial_angular_defect_absolute_upper"]
        for row in report.get("reference_branches", []):
            suffix = "_sigma_"+str(row["sigma"])
            values["normalized_velocity_defect_upper"+suffix] = row["normalized_velocity_defect_upper"]
            values["local_relative_Gram_majorant_upper"+suffix] = row["local_relative_Gram_majorant_upper"]
        for key, text in values.items():
            value = rational(text)
            if key not in self.maxima or value > rational(self.maxima[key]["upper"]):
                self.maxima[key] = dict(upper=str(value), observation_index=index, address=copy.deepcopy(address))

    def summary(self, *, original_coverage, ledger_receipts):
        return dict(schema=SUMMARY_SCHEMA, enabled=self.enabled, counts=copy.deepcopy(self.counts),
            evaluation_kinds=copy.deepcopy(self.by_kind), unpaid_reason_counts=copy.deepcopy(self.reasons),
            largest_observed_local_upper_bounds=copy.deepcopy(self.maxima),
            last_started=copy.deepcopy(self.last_started), last_completed=copy.deepcopy(self.last_completed),
            first_unpaid=copy.deepcopy(self.first_unpaid), last_unpaid=copy.deepcopy(self.last_unpaid),
            every_completed_observation_in_original_temporary_ledgers=copy.deepcopy(ledger_receipts),
            original_complete_coverage_and_pending=copy.deepcopy(original_coverage),
            count_scope="Actual same-call local observations, including live-C repeats; not a covering proof",
            full_unpaid_observation_rows_in_ledgers_not_all_returned_in_this_summary=True,
            no_unvisited_or_inflight_diagnostic_claimed_complete=True,
            no_same_worker_branch_or_ODE_RMS_to_metric_floor_claim=True,
            no_BC_anchor_or_radial_integration_or_new_stability_bound=True,
            direct_metric_decisions_and_original_acceptance_unchanged=True)
