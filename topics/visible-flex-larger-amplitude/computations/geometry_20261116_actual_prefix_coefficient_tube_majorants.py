#!/usr/bin/env python3
"""R553 actual complete prefix coefficient tubes and finite Frenet majorants.

This optional observer reads the already bound accurate field's complete
rational Hermite coefficients.  It never accepts caller-invented tube bounds,
selects a C root, invokes a solver, changes a metric predicate or deletes raw
data.  Every numerical operation belongs to the named public Actions.
The original metric traversal decides all splitting and retirement.
Author: geometry agent (AI), 2026-11-16.
"""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from math import comb
import os
from pathlib import Path
import sys

REPOSITORY = "Rogerhu12/math-research-public"
HERE = Path(__file__).resolve().parent
SCHEMA = "R553-actual-complete-prefix-coefficient-tube-majorants-v1"
MAJORANT_NAME = "geometry_20261116_finite_frenet_tube_residual_majorants.py"
MAJORANT_SHA = "4217bf9a30ade1934c473146131067de2ff778ea62bc0b7811b55356a7cd71ad"
MAJORANT_SCHEMA = "R521-complete-finite-frenet-tube-majorants-v1"
ACTIVE_NAME = "geometry_20261115_shared_active_interval_balls.py"
ACTIVE_SHA = "675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b"
BLOCKS = ("y", "A", "nu", "mu")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
            "Evaluate actual coefficient tubes only in the named public Actions")


def exact(value):
    if isinstance(value, bool) or isinstance(value, float):
        raise TypeError("Use an exact rational or an original exact lift")
    if isinstance(value, (Q, int, str)):
        return Q(value)
    raise TypeError("An exact rational word is required")


def pair(value):
    require(isinstance(value, (tuple, list)) and len(value) == 2,
            "Use both original closed endpoints")
    lo, hi = (exact(x) for x in value)
    require(lo <= hi, "Closed interval endpoints are reversed")
    return lo, hi


def encoded(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, dict):
        return {key: encoded(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [encoded(item) for item in value]
    return value


def canonical(value):
    return (json.dumps(encoded(value), sort_keys=True, separators=(",", ":"),
        ensure_ascii=False, allow_nan=False)+"\n").encode("utf-8")


def value_identity(value):
    raw = canonical(value)
    return dict(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())


def source_identity(path):
    path = Path(path).resolve()
    raw = path.read_bytes()
    return dict(file=str(path), bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())


def actual_module(method, expected_name, expected_sha):
    """Use the method's actual defining module, never the first matching path."""
    function = getattr(method, "__func__", method)
    module = sys.modules.get(getattr(function, "__module__", ""))
    require(module is not None and getattr(module, "__file__", None) is not None,
            "The actual complete coefficient method has no source owner")
    row = source_identity(module.__file__)
    require(Path(row["file"]).parent == HERE and Path(row["file"]).name == expected_name
            and row["sha256"] == expected_sha,
            "Keep the actual original full-prefix coefficient implementation")
    return row


def load_majorants():
    path = HERE/MAJORANT_NAME
    row = source_identity(path)
    require(row["sha256"] == MAJORANT_SHA, "The complete R521 source differs")
    name = "_r553_actual_r521_"+MAJORANT_SHA
    module = sys.modules.get(name)
    if module is None:
        spec = importlib.util.spec_from_file_location(name, path)
        require(spec is not None and spec.loader is not None, "Cannot load the actual majorant source")
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        try:
            spec.loader.exec_module(module)
        except BaseException:
            sys.modules.pop(name, None)
            raise
    require(Path(module.__file__).resolve() == path.resolve()
            and module.SCHEMA == MAJORANT_SCHEMA, "The actual R521 module identity differs")
    return module, row


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def neg(a):
    return -a[1], -a[0]


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    values = (a[0]*b[0], a[0]*b[1], a[1]*b[0], a[1]*b[1])
    return min(values), max(values)


def scale(a, factor):
    value = exact(factor)
    return mul(a, (value, value))


def square(a):
    lower = Q(0) if a[0] <= 0 <= a[1] else min(a[0]*a[0], a[1]*a[1])
    return lower, max(a[0]*a[0], a[1]*a[1])


def absolute(a):
    return max(abs(a[0]), abs(a[1]))


def norm_squared(vector):
    result = (Q(0), Q(0))
    for component in vector:
        result = add(result, square(component))
    return result


def cross(left, right):
    return (sub(mul(left[1], right[2]), mul(left[2], right[1])),
            sub(mul(left[2], right[0]), mul(left[0], right[2])),
            sub(mul(left[0], right[1]), mul(left[1], right[0])))


def polynomial_range(coefficients, left, right):
    """Exact Bernstein enclosure of one original normalized polynomial."""
    coefficients = tuple(exact(x) for x in coefficients)
    require(coefficients, "A complete nonempty polynomial is required")
    left, right = exact(left), exact(right)
    require(0 <= left <= right <= 1, "Keep the original complete Hermite cell")
    degree = len(coefficients)-1
    width = right-left
    shifted = tuple(sum((coefficients[j]*comb(j, k)*left**(j-k)*width**k
                          for j in range(k, degree+1)), Q(0))
                    for k in range(degree+1))
    bernstein = tuple(sum((Q(comb(k, j), comb(degree, j))*shifted[j]
                           for j in range(k+1)), Q(0))
                      for k in range(degree+1))
    return (min(bernstein), max(bernstein)), bernstein


def derivative(coefficients, length):
    h = exact(length)
    require(h > 0, "The actual full Hermite span must be positive")
    if len(coefficients) == 1:
        return (Q(0),)
    return tuple(j*exact(coefficients[j])/h for j in range(1, len(coefficients)))


def complete_coefficient_box(field, piece, radial, budget_check):
    """Read all 3*M+2 actual quintic polynomials, including both means."""
    lo, hi = pair(radial)
    index = piece["prefix_span"]
    require(type(index) is int and 0 <= index < len(field.x)-1,
            "The actual prefix span is absent")
    x0, x1 = exact(field.x[index]), exact(field.x[index+1])
    require(x0 <= lo <= hi <= x1, "The original closed cell crossed an unlisted prefix span")
    h = x1-x0
    require(h > 0 and piece["kind"] == "prefix", "Use the actual nonempty prefix piece")
    budget_check()
    coefficients = field.prefix_coefficients(index)
    size = 3*field.M+2
    require(len(coefficients) == size and all(len(row) == 6 for row in coefficients),
            "Retain every original physical coefficient and all six Hermite powers")
    unit = ((lo-x0)/h, (hi-x0)/h)
    boxes, first_boxes, second_boxes, bernstein_rows = [], [], [], []
    for row in coefficients:
        budget_check()
        original = tuple(exact(x) for x in row)
        first = derivative(original, h)
        second = derivative(first, h)
        box, bernstein = polynomial_range(original, *unit)
        first_box, _ = polynomial_range(first, *unit)
        second_box, _ = polynomial_range(second, *unit)
        boxes.append(box); first_boxes.append(first_box); second_boxes.append(second_box)
        bernstein_rows.append(bernstein)
    return dict(prefix_span=index, full_span=(x0, x1), radial=(lo, hi),
        normalized_subinterval=unit, field_modes=field.M, physical_size=size,
        actual_all_six_power_coefficients_identity=value_identity(coefficients),
        actual_all_bernstein_coefficients_identity=value_identity(bernstein_rows),
        actual_all_first_derivative_boxes_identity=value_identity(first_boxes),
        actual_all_second_derivative_boxes_identity=value_identity(second_boxes),
        complete_coefficient_box=tuple(boxes),
        coefficient_prime_infinity_upper=max(absolute(v) for v in first_boxes),
        coefficient_second_infinity_upper=max(absolute(v) for v in second_boxes),
        exact_definition="R675 complete rational quintic Hermite from actual binary64 nodal 0/1/2 data",
        original_saved_solver_cubic_or_rounded_PPoly_not_substituted=True,
        both_means_and_every_frequency_retained=True)


def complete_angular_box(active, coefficient_box, angular, field_modes, budget_check):
    """Independent coefficient box, full closed physical-angle cell, all modes.

    Vectors are expressed in the rotating cylindrical orthonormal frame.
    Their Euclidean norms and cross-product norms equal those in world axes.
    The actual common SE2 registration and whole lower reflection preserve
    these quantities. No sampled trigonometric values replace interval ranges.
    """
    boxes = tuple(pair(value) for value in coefficient_box)
    m = field_modes
    require(len(boxes) == 3*m+2, "Use the whole actual physical coefficient box")
    q = pair(angular)
    require(Q(0) <= q[0] <= q[1] <= Q(1), "Use the original closed physical-angle cell")
    budget_check()
    phi = (2*active.arb.pi())*active.interval(*q)
    zero = (Q(0), Q(0))
    d = [zero, boxes[0], zero]
    e = [neg(boxes[0]), zero, zero]
    trig_records = []
    for j in range(1, m+1):
        budget_check()
        frequency = 2*j
        co = pair(active.bounds((frequency*phi).cos()))
        si = pair(active.bounds((frequency*phi).sin()))
        r, t, z = boxes[j], boxes[m+j], boxes[2*m+1+j]
        d[0] = sub(d[0], mul(add(scale(r, frequency), t), si))
        d[1] = add(d[1], mul(add(scale(t, frequency), r), co))
        d[2] = sub(d[2], mul(scale(z, frequency), si))
        e[0] = sub(e[0], mul(add(scale(r, frequency*frequency+1), scale(t, 2*frequency)), co))
        e[1] = sub(e[1], mul(add(scale(t, frequency*frequency+1), scale(r, 2*frequency)), si))
        e[2] = sub(e[2], mul(scale(z, frequency*frequency), co))
        trig_records.append(dict(frequency=frequency, cos=co, sin=si))
    return dict(angular=q, physical_angle="phi=2*pi*q",
        complete_frequency_count=m, frequencies=[2*j for j in range(1, m+1)],
        actual_complete_trigonometric_ranges_identity=value_identity(trig_records),
        d=tuple(d), e=tuple(e),
        interval_scope="Every independent coefficient vector in the recorded box and every angle in this closed cell",
        current_material_map_not_used_as_the_physical_angle=True)


class BoundPrefixTubes:
    """Optional actual observer; only original DFS retirement fixes its cover."""
    def __init__(self, current, *, angular_count, sqrt_bits, budget_check,
                 actual_checkpoint, actual_expression):
        actions()
        self.current, self.field, self.Active = current, current.field, current.Active
        self.budget_check, self.sqrt_bits = budget_check, sqrt_bits
        self.M = int(self.field.M)
        require(type(angular_count) is int and angular_count > 0,
                "Use the actual checkpoint's angular quadrature")
        require(type(sqrt_bits) is int and sqrt_bits > 0, "Keep the original square-root work precision")
        self.N = angular_count
        self.api, self.majorant_source = load_majorants()
        self.coefficient_source = actual_module(self.field.prefix_coefficients, ACTIVE_NAME, ACTIVE_SHA)
        self.binding = dict(schema=SCHEMA+"-binding", source=source_identity(__file__),
            majorant_source=self.majorant_source, original_coefficient_source=self.coefficient_source,
            actual_checkpoint=copy.deepcopy(actual_checkpoint),
            actual_expression=copy.deepcopy(actual_expression),
            field_modes=self.M, angular_count=self.N, physical_size=3*self.M+2,
            coordinate="Original numeric prefix s and physical phi=2*pi*q",
            data_source="The already loaded actual full field and the same target-range return",
            new_BVP_native_metric_acceptance_predicate=False,
            solver_RMS_to_complete_metric_floor_bound=False)
        self.observed_prefix_cells = self.committed_prefix_cells = 0
        self.terminal_prefix_leaves = self.positive_terminal_leaves = 0
        self.unpaid_terminal_leaves = self.split_prefix_cells = 0
        self.maxima = {key: Q(0) for key in BLOCKS}
        self.max_second = Q(0)
        self.minima = None
        self.first_unpaid = self.last_unpaid = None
        self.last_observed_address = None

    def inspect(self, cell, actual_scalar_context):
        """No target/field resampling; context is copied from that same return."""
        self.budget_check()
        address = copy.deepcopy(cell)
        self.observed_prefix_cells += 1
        self.last_observed_address = address
        record = dict(schema=SCHEMA+"-cell", original_cell=address, available=False,
            coefficient_tube=None, angular_box=None, scalar_box=None,
            joint_invariants=None, synthesis=None, finite_rhs_majorants=None,
            reasons=[], error=None,
            original_metric_decision_not_changed=True,
            accurate_quintic_not_original_cubic=True,
            original_FFT_or_nominal_RHS_rounding_error_not_proved=True,
            original_comparison_curve_membership_not_proved=True)
        try:
            piece = self.field.pieces[cell["piece_index"]]
            require(piece["kind"] == "prefix", "This actual finite coefficient model is prefix-only")
            require(isinstance(actual_scalar_context, dict)
                    and actual_scalar_context.get("schema") == SCHEMA+"-same-target-return",
                    "The same actual prefix target return is unavailable")
            a = pair(actual_scalar_context["radius"])
            derivative_a = pair(actual_scalar_context["accurate_arc_derivative"])
            g11 = pair(actual_scalar_context["numeric_s_radial_metric"])
            record["scalar_box"] = dict(actual_same_target_return=copy.deepcopy(actual_scalar_context),
                A=a, A_accurate_arc_derivative=derivative_a, g11=g11,
                mu=None, nu=None)
            if a[0] <= 0:
                record["reasons"].append("same_return_radius_positive_lower_unpaid")
            if g11[0] <= 0:
                record["reasons"].append("same_return_numeric_radial_metric_positive_lower_unpaid")
            if record["reasons"]:
                return encoded(record)
            mu = (self.api.sqrt_bounds(g11[0], self.sqrt_bits)[0],
                  self.api.sqrt_bounds(g11[1], self.sqrt_bits)[1])
            nu = mul(derivative_a, mu)
            record["scalar_box"].update(mu=mu, nu=nu,
                nu_rule="nu=dA/ds_numeric=a_s*(L_exact/L_numeric); mu=L_exact/L_numeric",
                same_C_correlations_only_enlarged_never_midpoint_selected=True)
            self.api.validate_modes(self.M, self.N)
            tube = complete_coefficient_box(self.field, piece, cell["radial"], self.budget_check)
            record["coefficient_tube"] = tube
            angular = complete_angular_box(self.Active, tube["complete_coefficient_box"],
                cell["angular"], self.M, self.budget_check)
            record["angular_box"] = angular
            q = norm_squared(angular["d"])
            cross_box = cross(angular["d"], angular["e"])
            w = norm_squared(cross_box)
            q3 = mul(square(q), q)
            p = sub(mul(mul(square(a), square(mu)), w), mul(square(nu), q3))
            record["joint_invariants"] = dict(d_squared=q, cross=cross_box,
                W=w, P=p, A_times_W=mul(a, w),
                entire_independent_d_e_A_nu_mu_box_used=True)
            if p[0] <= 0:
                record["reasons"].append("whole_joint_box_P_positive_lower_unpaid")
                return encoded(record)
            abs_bounds = tuple(absolute(value) for value in tube["complete_coefficient_box"])
            synthesis = self.api.fourier_synthesis_majorants(abs_bounds, self.M, self.N, self.sqrt_bits)
            domain = dict(A_lower=a[0], A_upper=a[1],
                mu_lower=mu[0], mu_upper=mu[1], nu_abs_upper=absolute(nu),
                P_lower=p[0], W_lower=w[0])
            self.budget_check()
            majorants = self.api.finite_rhs_majorants(domain, synthesis, self.sqrt_bits)
            record["synthesis"] = {key: value for key, value in synthesis.items()
                                   if key != "runtime_only_coefficient_bounds"}
            record["finite_rhs_majorants"] = majorants
            record["available"] = True
            record["conditions"] = dict(
                full_actual_quintic_coefficients=True,
                full_original_closed_angular_cell=True,
                all_physical_modes_and_both_means=True,
                entire_coefficient_box_and_entire_scalar_box=True,
                independent_box_enlargement_only=True,
                fixed_reference_sigma_branch_required=True,
                same_upper_bounds_for_either_fixed_sigma=True,
                original_worker_root_sigma_not_identified_here=True,
                original_comparison_curve_membership_not_proved=True)
            return encoded(record)
        except (ArithmeticError, ValueError, TypeError, KeyError, IndexError) as error:
            record["error"] = dict(type=type(error).__name__, message=str(error))
            record["reasons"].append("actual_prefix_tube_evaluation_unpaid")
            return encoded(record)

    def commit_original_retirement(self, cell, diagnostic, *, split):
        """Pure metadata attached to the original record before its write."""
        piece = self.field.pieces[cell["piece_index"]]
        if piece["kind"] != "prefix":
            return None
        self.committed_prefix_cells += 1
        if split:
            self.split_prefix_cells += 1
            return dict(original_prefix_cell_split=True,
                terminal_tube_responsibility_passed_to_all_original_children=True)
        self.terminal_prefix_leaves += 1
        available = (isinstance(diagnostic, dict)
                     and diagnostic.get("schema") == SCHEMA+"-cell"
                     and diagnostic.get("original_cell") == cell
                     and diagnostic.get("available") is True)
        commit_error = None
        if available:
            try:
                majorants = diagnostic["finite_rhs_majorants"]
                maxima = {key: exact(majorants["block_lipschitz"][key]) for key in BLOCKS}
                second = exact(majorants["state_second_direction_upper"])
                scalar, invariant = diagnostic["scalar_box"], diagnostic["joint_invariants"]
                found = dict(A=pair(scalar["A"])[0], mu=pair(scalar["mu"])[0],
                    P=pair(invariant["P"])[0], W=pair(invariant["W"])[0])
                require(all(value >= 0 for value in maxima.values()) and second >= 0
                        and all(value > 0 for value in found.values()),
                        "The actual paid-tube scalar record is inconsistent")
            except (ArithmeticError, ValueError, TypeError, KeyError, IndexError) as error:
                available = False
                commit_error = dict(type=type(error).__name__, message=str(error))
        if not available:
            self.unpaid_terminal_leaves += 1
            row = dict(original_cell=copy.deepcopy(cell),
                reasons=(["same_cell_diagnostic_not_returned"] if not isinstance(diagnostic, dict)
                         else copy.deepcopy(diagnostic.get("reasons"))),
                evaluation_error=None if not isinstance(diagnostic, dict) else copy.deepcopy(diagnostic.get("error")),
                retirement_record_error=commit_error,
                terminal_tube_paid=False)
            if self.first_unpaid is None:
                self.first_unpaid = row
            self.last_unpaid = row
            return row
        self.positive_terminal_leaves += 1
        for key in BLOCKS:
            self.maxima[key] = max(self.maxima[key], maxima[key])
        self.max_second = max(self.max_second, second)
        self.minima = found if self.minima is None else {
            key: min(self.minima[key], value) for key, value in found.items()}
        return dict(original_cell=copy.deepcopy(cell), terminal_tube_paid=True,
            actual_finite_RHS_record_identity=value_identity(majorants),
            actual_joint_input_identity=value_identity(dict(
                coefficient_tube=diagnostic["coefficient_tube"],
                angular_box=diagnostic["angular_box"], scalar_box=diagnostic["scalar_box"])))

    def summary(self, *, original_coverage, complete_cell_ledger, original_error,
                original_stop, close_errors):
        # This conservative all-DFS criterion deliberately does not infer an
        # early prefix completion from the rank ordering of a partial sweep.
        complete = (original_coverage.get("completed_all_DFS_work") is True
                    and self.terminal_prefix_leaves > 0
                    and self.unpaid_terminal_leaves == 0
                    and self.positive_terminal_leaves == self.terminal_prefix_leaves
                    and original_error is None and original_stop is None and not close_errors)
        return encoded(dict(schema=SCHEMA+"-necessary", binding=self.binding,
            observed_prefix_cells=self.observed_prefix_cells,
            committed_prefix_cells=self.committed_prefix_cells,
            split_prefix_cells=self.split_prefix_cells,
            terminal_prefix_leaves=self.terminal_prefix_leaves,
            positive_joint_box_terminal_leaves=self.positive_terminal_leaves,
            unpaid_prefix_terminal_leaves=self.unpaid_terminal_leaves,
            complete_prefix_constant_cover=complete,
            global_prefix_finite_RHS_majorants=(dict(block_lipschitz=self.maxima,
                state_second_direction_upper=self.max_second,
                positive_domain_lower=self.minima) if complete else None),
            observed_paid_leaf_extrema=dict(block_lipschitz=self.maxima,
                state_second_direction_upper=self.max_second,
                positive_domain_lower=self.minima,
                these_are_not_global_when_complete_prefix_constant_cover_is_false=True),
            first_unpaid_terminal=self.first_unpaid, last_unpaid_terminal=self.last_unpaid,
            last_observed_cell=self.last_observed_address,
            complete_original_cell_ledger=complete_cell_ledger,
            original_coverage_object_in_same_result="coverage",
            actual_current_frontier_and_all_unvisited_roots_retained_by_original_coverage=True,
            complete_each_retired_prefix_input_error_and_result_is_in_original_cell_ledger=True,
            ledger_rows_not_relabelled_as_fully_transported_in_this_necessary_summary=True,
            all_prefix_physical_angles_and_both_reflected_sheets_required=True,
            finite_RHS_scope="Base-field reference 3*M+2 physical coefficient operator on each covered local tube; global bound at the actual accurate quintic states, with every fixed sigma branch",
            finite_comparison_path_scope="A comparison path needs actual inclusion in the common local boxes for every relevant angle; no such inclusion is inferred here",
            whole_time_metric_scope="The original exact common-material congruence proof remains the reason for the full-t metric bound",
            unconnected_roles=["tail/collar/native-cut-patch Frenet coefficient model",
                "fixed-cap Frenet coefficient model", "original solver literal cubic",
                "rounded FFT/RHS/norm formation error", "original root/sigma identification",
                "actual comparison-path membership", "original solver tolerance to relative-metric floor"],
            original_BVP_native_FD_fullDN_and_metric_predicates_changed=False,
            original_metric_split_decision_does_not_read_this_diagnostic=True,
            no_second_domain_sweep_or_t_grid_started=True,
            no_independent_clock_or_subprocess_started=True))
