#!/usr/bin/env python3
"""R601: actual complete analytic projection and saved-RHS C1 defects.

This observer owns the original finish calls of one actual R580 and one
actual R596 object, both attached to the SAME R575/R553 field.  It adds the
physical-angle derivative of their complete reference defect.  It neither
queries the field/target again nor reruns a DFT, FFT, solver, DFS or clock.
Every new scalar bound operation uses the existing budget callback, and
all such arithmetic belongs to the named public GitHub Actions.
Author: ChatGPT /root (AI), 2026-11-16.
"""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import hashlib
import json
import os
from pathlib import Path
import sys
import traceback

REPOSITORY = "Rogerhu12/math-research-public"
HERE = Path(__file__).resolve().parent
SCHEMA = "R601-actual-analytic-projection-saved-RHS-world-C1-defect-v1"
ANALYTIC_NAME = "geometry_20261116_same_evaluation_analytic_angle_projection.py"
ANALYTIC_SHA = "0abe4629415a0e9219a50cf248f30bdceb9819b4338189b811101bdadf3d543f"
ANALYTIC_SCHEMA = "R580-same-evaluation-analytic-angle-projection-v1"
SAVED_NAME = "geometry_20261116_actual_saved_RHS_reference_defect.py"
SAVED_SHA = "8a242686845844df64d248b7b9fd47096ff2c7a8c2044346c85fc9b7425afb3f"
SAVED_SCHEMA = "R596-actual-saved-RHS-complete-finite-DFT-and-cell-defect-v1"
PHYSICAL_LAYOUT = "r0..rM,t1..tM,z0..zM"
ORDINARY = (ArithmeticError, ValueError, TypeError, KeyError, IndexError,
            AttributeError, OSError)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
            "All bound arithmetic belongs to the named public Actions")


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
    path = Path(path).resolve(strict=True)
    raw = path.read_bytes()
    return dict(file=str(path), bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())


def actual_module(obj, name, sha, class_name, schema):
    module = sys.modules.get(type(obj).__module__)
    require(module is not None and getattr(module, "__file__", None) is not None,
            "The actual defining module is unavailable")
    row = source_identity(module.__file__)
    require(Path(row["file"]).parent == HERE
            and Path(row["file"]).name == name and row["sha256"] == sha
            and module.SCHEMA == schema
            and getattr(module, class_name, None) is type(obj),
            "Use the frozen actual loaded class, not a same-name replacement")
    return module, row


def exact(value):
    require(not isinstance(value, (bool, float))
            and isinstance(value, (Q, int, str)),
            "Use exact rational bound words, not bool or a floating approximation")
    return Q(value)


def error_record(error, pending):
    return dict(type=type(error).__name__, message=str(error),
                traceback=traceback.format_exc(),
                actual_unfinished_operation=copy.deepcopy(pending))


class BoundContinuousRHSDefect:
    """One original finalization; no user-supplied h, C, eta, rho or anchor.

    The caller replaces its separate R580/R596 finalization with this call.
    It keeps both returned original summaries in full.  A recovery call is
    allowed only with the actual original error/stop/close error.  Recovery
    calls the originals in their metadata-only stopped branch and never
    retries a global analytic or C1 bound.
    """

    def __init__(self, analytic_projection, saved_rhs_defect):
        actions()
        self.A, analytic_source = actual_module(analytic_projection,
            ANALYTIC_NAME, ANALYTIC_SHA, "BoundAnalyticProjection", ANALYTIC_SCHEMA)
        self.S, saved_source = actual_module(saved_rhs_defect,
            SAVED_NAME, SAVED_SHA, "BoundSavedRHSDefect", SAVED_SCHEMA)
        self.analytic, self.saved = analytic_projection, saved_rhs_defect
        self.reference = analytic_projection.reference
        require(self.reference is saved_rhs_defect.projection,
                "Both observers must own the identical actual R575 object")
        self.tubes, self.field, self.current = (analytic_projection.tubes,
            analytic_projection.field, analytic_projection.current)
        self.api = analytic_projection.api
        self.M, self.N = analytic_projection.M, analytic_projection.N
        self.sqrt_bits = analytic_projection.sqrt_bits
        self.check = analytic_projection.budget_check
        require(saved_rhs_defect.tubes is self.tubes
            and saved_rhs_defect.field is self.field
            and saved_rhs_defect.current is self.current
            and saved_rhs_defect.api is self.api
            and saved_rhs_defect.M == self.M and saved_rhs_defect.N == self.N
            and saved_rhs_defect.n == 3*self.M+2
            and saved_rhs_defect.sqrt_bits == self.sqrt_bits
            and saved_rhs_defect.check is self.check
            and self.reference.budget_check is self.check,
            "Keep the actual field, scalar, grid, precision and original callback")
        self.A.reference_grid(self.M, self.N)
        require(saved_rhs_defect.binding["finite_reference_sigma"] == 1,
                "This composition uses the actual positive finite FFT reference")
        require(self.reference.field is self.field and self.tubes.field is self.field,
                "The two complete summaries belong to another field")
        self.binding = dict(schema=SCHEMA+"-binding",
            source=source_identity(__file__),
            actual_R580_source=analytic_source, actual_R596_source=saved_source,
            actual_R580_binding_identity=value_identity(analytic_projection.describe()),
            actual_R596_binding_identity=value_identity(saved_rhs_defect.describe()),
            actual_common_R575_binding_identity=value_identity(self.reference.describe()),
            field_modes=self.M, angular_count=self.N, physical_size=3*self.M+2,
            physical_layout=PHYSICAL_LAYOUT,
            radial_coordinate="the actual numeric prefix s",
            derivative_coordinate="physical phi in radians",
            finite_reference_sigma=1,
            full_original_bindings_returned_inside_the_two_original_summaries=True,
            actual_objects_not_supplied_constants=True,
            same_original_budget_callback=True,
            original_finish_calls_owned_here_exactly_once=True,
            recovery_after_original_stop_is_metadata_only=True,
            no_new_angular_grid_field_target_clock_child_or_acceptance=True)
        self.finish_started = False
        self.summary_calls = 0
        self.pending = None
        self.analytic_summary = None
        self.saved_summary = None
        self.last_completed_composition = None
        self.last_formation_error = None

    def describe(self):
        return encoded(copy.deepcopy(self.binding))

    def work(self, operation, **position):
        self.pending = dict(operation=operation, position=copy.deepcopy(position))
        self.check()

    def up(self, value, operation):
        self.work(operation)
        return self.A.relative_dyadic_bounds(value, self.sqrt_bits)[1]

    def validate_complete_originals(self, original_coverage, complete_cell_ledger):
        a, b = self.analytic_summary, self.saved_summary
        require(isinstance(a, dict) and isinstance(b, dict),
                "Both actual original summaries must have returned")
        require(a["schema"] == ANALYTIC_SCHEMA+"-necessary"
            and b["schema"] == SAVED_SCHEMA+"-necessary"
            and canonical(a["binding"]) == canonical(self.analytic.describe())
            and canonical(b["binding"]) == canonical(self.saved.describe()),
            "The actual original complete binding changed")
        require(complete_cell_ledger is not None
            and canonical(a["complete_original_cell_ledger"]) == canonical(complete_cell_ledger)
            and canonical(b["complete_cell_ledger"]) == canonical(complete_cell_ledger)
            and canonical(b["original_complete_coverage"]) == canonical(original_coverage),
            "Use the same complete original ledger and coverage")
        require(a["complete_prefix_analytic_projection_bound"] is True
            and a["original_all_DFS_and_R553_complete"] is True
            and a["exact_original_retirement_counters_match"] is True
            and a["unpaid_terminal_analytic_strips"] == 0
            and a["actual_unfinished_operation"] is None
            and a["global_bound_formation_error"] is None
            and b["complete_prefix_finite_quintic_residual"] is True
            and b["complete_original_closed_DFS_responsibility_paid"] is True
            and b["original_R553_retirement_counters_match"] is True
            and b["actual_retirement_error_count"] == 0
            and b["actual_current_inflight_work"] is None,
            "Partial strips, residuals, or original coverage are not global bounds")
        values = (
            ("observed_prefix_cells", "observed_prefix_cells", self.analytic.observed, self.saved.observed),
            ("committed_prefix_cells", "committed_prefix_cells", self.analytic.committed, self.saved.committed),
            ("split_prefix_cells", "split_prefix_cells", self.analytic.split, self.saved.split),
            ("terminal_prefix_leaves", "terminal_prefix_cells", self.analytic.terminal, self.saved.terminal),
        )
        for ak, bk, av, bv in values:
            require(type(av) is int and type(bv) is int and av == bv
                and type(a[ak]) is int and type(b[bk]) is int and a[ak] == av and b[bk] == bv,
                "The two actual original retirement sequences differ")
        require(self.analytic.observed == self.analytic.committed
            and self.analytic.terminal > 0
            and self.analytic.paid == self.analytic.terminal
            and self.saved.paid_Q == self.saved.terminal,
            "Every original terminal prefix cell must be paid by both observers")

    def form_complete_bound(self, original_coverage, complete_cell_ledger):
        self.work("bind_actual_complete_original_summaries")
        self.validate_complete_originals(original_coverage, complete_cell_ledger)
        a, b = self.analytic_summary, self.saved_summary
        p = a["global_prefix_exact_reference_projection_bound"]
        require(p["schema"] == ANALYTIC_SCHEMA+"-conditional-uniform-bound"
            and (p["field_modes"], p["angular_count"], p["physical_size"])
                == (self.M, self.N, 3*self.M+2)
            and p["physical_layout"] == PHYSICAL_LAYOUT
            and p["complete_infinite_even_tail_and_all_integer_aliases_included"] is True
            and p["returned_bounds_include_all_directed_enclosure_rounding"] is True
            and p["both_R_and_Z_means_retained"] is True,
            "Use the actual complete signed-tail and all-alias reference")
        self.work("read_actual_positive_strip_and_residual_bounds")
        h, C = exact(p["strip_half_width"]), exact(p["complete_strip_vector_sup"])
        eta = exact(b["global_prefix_eta_Q_upper"])
        require(h == self.analytic.min_width == exact(a["global_strip_half_width"])
            and C == self.analytic.max_sup == exact(a["global_complex_vector_sup"])
            and eta == self.saved.max_Q and h > 0 and C >= 0 and eta >= 0,
            "The complete bounds must be the actual retired original extrema")
        maj = p["rational_exponential_majorant"]
        require(maj["enclosure_bits"] == self.sqrt_bits
            and maj["L"] == self.analytic.exponential_terms
            and maj["all_indices_included"] == [0, self.analytic.exponential_terms]
            and maj["exact_sum_is_defined_by_the_returned_h_and_L_not_an_unreturned_input"] is True,
            "Do not change the original exact positive-sum definition of r")
        rlo, rhi = map(exact, maj["r_enclosure"])
        glo, ghi = map(exact, maj["positive_one_minus_r_enclosure"])
        require(Q(0) < rlo <= rhi <= Q(1) and Q(0) < glo <= ghi,
                "The original positive gap is required even if r_upper equals one")
        powers = {}
        for row in maj["complete_power_sum_enclosures"]:
            exponent = row["exponent"]
            require(type(exponent) is int and exponent not in powers,
                    "Keep every unique original complete power-sum enclosure")
            powers[exponent] = row
        m = self.M
        require(set(powers) == {m+1, self.N//2-m, 2*m+1, self.N//2},
                "The complete original four exponent roles must be retained")
        plo, phi = map(exact, powers[m+1]["power"])
        require(Q(0) < plo <= phi <= Q(1),
                "Use the actual outward enclosure of r^(M+1)")
        alias = exact(p["alias_upper_used"])
        d0 = exact(p["uniform_reconstructed_projection_defect_upper"])
        finite0 = exact(b["global_reconstructed_finite_ODE_residual_upper"])
        c0 = exact(b["complete_coefficient_to_vector_synthesis_norm_upper"])
        require(alias >= 0 and d0 >= 0 and finite0 >= 0 and c0 >= 0
            and finite0 == self.saved.max_vector_Q and c0 == self.saved.reconstruction,
            "Use complete original nonnegative projection and synthesis bounds")
        # r is the SAME exact reciprocal Taylor sum already enclosed by R580.
        # Positive terms avoid cancellation in (M+1)-M*r.  r_upper==1 is
        # legitimate; the independently enclosed positive gap is retained.
        self.work("complete_weighted_infinite_derivative_tail")
        tail1_raw = 4*C*phi*((m+1)/glo + rhi/(glo*glo))
        tail1 = self.up(tail1_raw, "round_complete_derivative_tail_outward")
        alias1 = self.up(2*m*alias, "round_all_retained_alias_derivatives_outward")
        rotating1 = self.up(tail1+alias1, "round_rotating_projection_derivative_outward")
        # The real world frame E has E'=E*J, J(a,b,c)=(-b,a,0), ||J||=1.
        # Complex E is not assumed unitary.  d0 supplies the connection term.
        projection1 = self.up(rotating1+d0, "round_world_frame_connection_and_derivative_outward")
        self.work("complete_coefficient_world_derivative_weights")
        weights = (m*(m+2), (m+1)*(m+1), m*(m+1))
        norm_square = Q(sum(value*value for value in weights))
        self.work("actual_R521_complete_coefficient_derivative_norm_sqrt")
        c1 = self.api.sqrt_bounds(norm_square, self.sqrt_bits)[1]
        require(c1 >= 0, "The original square-root upper endpoint is nonnegative")
        finite1 = self.up(c1*eta, "round_complete_finite_residual_derivative_outward")
        defect0 = self.up(finite0+d0, "round_complete_unprojected_defect_outward")
        defect1 = self.up(finite1+projection1, "round_complete_unprojected_world_derivative_outward")
        result = dict(schema=SCHEMA+"-complete-prefix-bound",
            field_modes=m, angular_count=self.N, physical_size=3*m+2,
            physical_layout=PHYSICAL_LAYOUT,
            radial_coordinate="the actual numeric prefix s",
            derivative_coordinate="physical phi in radians",
            component_frame="real Cartesian world frame",
            finite_reference_sigma=1,
            actual_R580_summary_identity=value_identity(a),
            actual_R596_summary_identity=value_identity(b),
            actual_complete_original_cell_ledger=copy.deepcopy(complete_cell_ledger),
            full_exact_reference_definition="r=partial_s(S_M Q)-V_+(S_M Q; A, nu=A_s, mu)",
            actual_complete_strip_half_width=h,
            actual_complete_strip_vector_sup=C,
            actual_eta_Q_upper=eta,
            complete_coefficient_C0_norm_upper=c0,
            complete_coefficient_world_C1_component_weights=weights,
            complete_coefficient_world_C1_norm_upper=c1,
            complete_finite_residual_world_C0_upper=finite0,
            complete_finite_residual_world_C1_upper=finite1,
            actual_projection_world_C0_upper=d0,
            complete_rotating_derivative_tail_upper=tail1,
            complete_all_retained_alias_derivative_upper=alias1,
            complete_rotating_projection_derivative_upper=rotating1,
            complete_world_projection_derivative_upper=projection1,
            complete_prefix_unprojected_physical_RHS_defect_upper=defect0,
            complete_prefix_unprojected_physical_RHS_world_phi_derivative_upper=defect1,
            exact_derivative_tail_formula="4*C*r^(M+1)*((M+1)/(1-r)+r/(1-r)^2)",
            exact_world_projection_bound="T1 + 2*M*alias_used + D0",
            exact_coefficient_world_C1_norm="sqrt((M*(M+2))^2+((M+1)^2)^2+(M*(M+1))^2)",
            all_infinite_tail_and_all_integer_aliases_included=True,
            rotating_frame_connection_included=True,
            radial_mean_retained_in_world_derivative=True,
            vertical_mean_retained_although_its_phi_derivative_is_zero=True,
            full_vector_norm_not_multiplied_by_three=True,
            positive_gap_not_replaced_by_one_minus_rounded_r_upper=True,
            no_exponential_power_sum_grid_or_finite_DFT_recomputed=True,
            all_new_rounding_is_directed_bound_formation=True,
            finite_reference_formation_difference_is_the_actual_R596_total_gap=True,
            R514_transport_formula="abs(tau) <= abs(partial_phi r)/(A*rho)",
            actual_A_rho_denominator_anchor_and_radial_integral_not_formed_here=True,
            original_native_DtN_worker_sigma_not_identified=True,
            fixed_N_DFT_not_claimed_to_commute_with_arbitrary_phase=True,
            closed_surface_relative_metric_floor_not_claimed=True)
        self.pending = None
        return encoded(result)

    def summary(self, *, original_coverage, complete_cell_ledger, original_error,
                original_stop, close_errors):
        actions()
        halted = (original_error is not None or original_stop is not None or bool(close_errors))
        require(not self.finish_started or halted,
                "Do not repeat the original scientific finish; recovery needs the actual original stop/error")
        self.finish_started = True
        self.summary_calls += 1
        arguments = dict(original_coverage=original_coverage,
            complete_cell_ledger=complete_cell_ledger, original_error=original_error,
            original_stop=original_stop, close_errors=close_errors)
        # These are calls on the actual bound objects.  No caller-supplied
        # strip/eta summary is accepted.  With a real original stop/error,
        # R580's existing complete predicate is false and it does metadata
        # only.  R596 is called with no R575 composition argument, so it
        # performs no new finite reference or coefficient arithmetic here.
        if not halted:
            self.pending = dict(operation="original_R580_finish", position={})
        self.analytic_summary = self.analytic.summary(**arguments)
        if not halted:
            self.pending = dict(operation="original_R596_metadata_finish", position={})
        self.saved_summary = self.saved.summary(**arguments)
        composition = None
        formation_error = None
        both_complete = (not halted
            and original_coverage.get("completed_all_DFS_work") is True
            and complete_cell_ledger is not None
            and self.analytic_summary.get("complete_prefix_analytic_projection_bound") is True
            and self.saved_summary.get("complete_prefix_finite_quintic_residual") is True)
        if both_complete:
            try:
                composition = self.form_complete_bound(original_coverage, complete_cell_ledger)
                self.last_completed_composition = copy.deepcopy(composition)
            except ORDINARY as error:
                formation_error = error_record(error, self.pending)
                self.last_formation_error = copy.deepcopy(formation_error)
                self.pending = None
        elif not halted:
            self.pending = None
        # RuntimeError (the original ResourceStop) and MemoryError are NOT
        # caught above.  The original caller records the actual stop and
        # may then reenter this stopped metadata branch; no bound is retried.
        return encoded(dict(schema=SCHEMA+"-necessary", binding=self.binding,
            actual_R580_summary=copy.deepcopy(self.analytic_summary),
            actual_R596_summary=copy.deepcopy(self.saved_summary),
            original_coverage_identity=value_identity(original_coverage),
            complete_original_cell_ledger=copy.deepcopy(complete_cell_ledger),
            original_error=copy.deepcopy(original_error),
            original_stop=copy.deepcopy(original_stop), close_errors=copy.deepcopy(close_errors),
            original_summary_call_count=self.summary_calls,
            recovery_metadata_only=halted,
            both_complete_original_prefix_bounds_returned=both_complete,
            complete_prefix_physical_RHS_C0_and_world_C1_bound=composition is not None,
            complete_prefix_bound=composition,
            formation_error=formation_error,
            last_formation_error=copy.deepcopy(self.last_formation_error),
            actual_unfinished_operation=copy.deepcopy(self.pending),
            previous_completed_composition_not_current_after_a_stop=(
                copy.deepcopy(self.last_completed_composition) if halted else None),
            every_original_unknown_error_unpaid_and_coverage_field_retained_in_original_summaries=True,
            original_ledger_rows_not_claimed_fully_transported=True,
            global_bound_unavailable_does_not_reject_original_field=True,
            no_new_DFS_split_original_metric_FD_fullDN_or_acceptance_predicate=True,
            no_new_child_clock_ownership_or_cleanup_permission=True,
            unpaid=["actual A*rho positive global denominator for the chosen material coordinates",
                "original BC/cuff anchor and complete radial transport paths",
                "actual tail/collar/cut-patch/cap residual references",
                "native DtN worker branch and its own total formation defect",
                "actual full closed-surface relative metric floor",
                "actual same-target mesh/frequency/time refinement conclusions"]))


def bind_loaded_continuous_RHS_C1_defect(analytic_projection, saved_rhs_defect):
    """The caller supplies actual source-pinned objects, never inferred constants."""
    return BoundContinuousRHSDefect(analytic_projection, saved_rhs_defect)
