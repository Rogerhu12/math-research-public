#!/usr/bin/env python3
"""R610: actual R601 defects, true prefix anchor, and relative Gram transport.

Attach to the same R553 retirement sequence. Consume an already returned
R601 summary without calling its finish again. Every scientific operation
uses the original public Actions context and existing budget callback.
There is no new target/field query, DFT, solver, split, clock or acceptance.
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
SCHEMA = "R610-actual-prefix-anchor-and-R601-relative-metric-transport-v1"
CONTINUOUS_NAME = "geometry_20261116_actual_analytic_saved_RHS_C1_defect.py"
CONTINUOUS_SHA = "12450be1cbdd289b69f74535d98fa42586506709244ed066b338c98cd494490d"
CONTINUOUS_SCHEMA = "R601-actual-analytic-projection-saved-RHS-world-C1-defect-v1"
ACTIVE_NAME = "geometry_20261115_shared_active_interval_balls.py"
ACTIVE_SHA = "675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b"
KERNEL_NAME = "geometry_20261115_shared_field_relative_metric.py"
KERNEL_SHA = "a601e5b5dca3c7d87ea7b78a4eb0cebf0b7884d9d4663570f262d6cda578ed17"
SAVED_KERNEL_NAME = "geometry_20261114_large_core_saved_prefix.py"
SAVED_KERNEL_SHA = "51eab8cdc878e22ad2c57bab129b1ef31463799596fcc40399fd8b0714ccbea0"
TUBE_SCHEMA = "R553-actual-complete-prefix-coefficient-tube-majorants-v1"
ORDINARY = (ArithmeticError, ValueError, TypeError, KeyError, IndexError,
            AttributeError, OSError)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY,
            "All scientific work belongs to the named public Actions")


def exact(value):
    require(not isinstance(value, (bool, float))
            and isinstance(value, (Q, int, str)),
            "Use exact bound words or an original exact binary64 lift")
    return Q(value)


def pair(value):
    require(isinstance(value, (tuple, list)) and len(value) == 2,
            "Keep both closed rational endpoints")
    lo, hi = map(exact, value)
    require(lo <= hi, "A closed interval is reversed")
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
    path = Path(path).resolve(strict=True)
    raw = path.read_bytes()
    return dict(file=str(path), bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())


def checked_module(module, name, digest):
    require(module is not None and getattr(module, "__file__", None) is not None,
            "The actual defining module is unavailable")
    row = source_identity(module.__file__)
    require(Path(row["file"]).parent == HERE and Path(row["file"]).name == name
            and row["sha256"] == digest,
            "Keep the actual complete source: "+name)
    return row


def error_record(error, pending):
    return dict(type=type(error).__name__, message=str(error),
                traceback=traceback.format_exc(),
                actual_unfinished_operation=copy.deepcopy(pending))


class BoundPrefixMetricTransport:
    """No supplied rho, A, mu, anchor, length, residual or numerical threshold.

    The original caller first retires its R553 cell, then calls retire with
    the SAME complete diagnostic and original split decision before writing
    the original ledger row. At finish it calls R601 once and supplies that
    actual returned whole object here. This class never invokes R601.summary.
    """
    def __init__(self, continuous_rhs_defect, *, metric_kernel):
        actions()
        self.continuous = continuous_rhs_defect
        module = sys.modules.get(type(continuous_rhs_defect).__module__)
        continuous_source = checked_module(module, CONTINUOUS_NAME, CONTINUOUS_SHA)
        require(module.SCHEMA == CONTINUOUS_SCHEMA
                and type(continuous_rhs_defect) is module.BoundContinuousRHSDefect,
                "Use the actual already bound R601 class")
        self.C = module
        self.tubes = continuous_rhs_defect.tubes
        self.field = continuous_rhs_defect.field
        self.current = continuous_rhs_defect.current
        self.saved = continuous_rhs_defect.saved
        self.api = continuous_rhs_defect.api
        self.check = continuous_rhs_defect.check
        self.M, self.N = continuous_rhs_defect.M, continuous_rhs_defect.N
        self.n, self.sqrt_bits = 3*self.M+2, continuous_rhs_defect.sqrt_bits
        self.Active = self.current.Active
        self.Kernel = metric_kernel
        active_source = checked_module(self.Active, ACTIVE_NAME, ACTIVE_SHA)
        kernel_source = checked_module(metric_kernel, KERNEL_NAME, KERNEL_SHA)
        self.check()
        # In the actual accurate-cut subclass these five methods are inherited.
        # The complete cut patch is separate; no claim about its prefix analogue
        # is inferred from its name or from the unchanged prefix coefficients.
        for name in ("prefix_coefficients", "prefix", "registered_world", "material_angle", "evaluate"):
            method = getattr(self.field, name)
            require(getattr(method, "__func__", None)
                    is getattr(self.Active.ExactFiniteField, name),
                    "The actual unpatched complete prefix method differs: "+name)
        require(self.tubes.field is self.field and self.saved.field is self.field
                and self.current.field is self.field
                and self.saved.check is self.check
                and self.tubes.budget_check is self.check,
                "Keep the identical actual field and original budget callback")
        require(len(self.field.core) == self.M and len(self.field.density) == self.M,
                "Use all actual material-core modes")
        self.numeric_length = exact(self.field.x[-1])
        require(exact(self.field.x[0]) == 0 and self.numeric_length > 0
                and self.numeric_length == exact(self.current.target.numeric_length),
                "The full actual numeric prefix chart must be [0,L_numeric]")
        saved_loader = sys.modules.get(type(self.field.saved).__module__)
        require(saved_loader is not None and getattr(saved_loader, "__file__", None) is not None,
                "The actual saved-prefix loader is unavailable")
        saved_loader_source = source_identity(saved_loader.__file__)
        saved_sources = self.field.saved.source_sha256
        require(saved_sources.get(Path(saved_loader_source["file"]).name)
                    == saved_loader_source["sha256"],
                "The actual saved loader must be in its checked complete source closure")
        saved_kernel_source = checked_module(self.field.saved._kernel,
            SAVED_KERNEL_NAME, SAVED_KERNEL_SHA)
        require(saved_sources.get(SAVED_KERNEL_NAME) == SAVED_KERNEL_SHA,
                "Keep the checked original complete material-density kernel")
        self.rho_lower = exact(self.field.rho_lower)
        require(self.rho_lower > 0
                and self.rho_lower == exact(self.field.saved.rho_lower_exact),
                "Use the actual loader's already paid full-core R237 lower bound")
        self.binding = dict(schema=SCHEMA+"-binding", source=source_identity(__file__),
            actual_R601_source=continuous_source,
            actual_R601_binding_identity=value_identity(continuous_rhs_defect.describe()),
            actual_R553_binding=copy.deepcopy(self.tubes.binding),
            actual_active_source=active_source,
            actual_metric_kernel=kernel_source,
            actual_saved_loader_source=saved_loader_source,
            actual_saved_material_kernel=saved_kernel_source,
            actual_saved_complete_source_closure_identity=value_identity(saved_sources),
            actual_checkpoint=copy.deepcopy(self.saved.binding["actual_checkpoint"]),
            actual_complete_array_words=copy.deepcopy(
                self.saved.binding["actual_complete_array_words"]),
            actual_field_expression_identity=value_identity(
                self.saved.binding["actual_full_675_expression"]),
            actual_target_binding_identity=value_identity(self.current.target.binding),
            field_modes=self.M, angular_count=self.N, physical_size=self.n,
            physical_layout="r0..rM,t1..tM,z0..zM",
            radial_coordinate="actual numeric prefix s",
            derivative_coordinate="physical phi in radians",
            original_metric_q_coordinate="q=phi/(2*pi), theta_q=2*pi*rho",
            numeric_length=self.numeric_length,
            actual_complete_material_density_lower=self.rho_lower,
            rho_lower_source="The actual checked complete-core R237 bound already paid by this field's original saved loader",
            no_midpoint_target_no_old_M96_numeric_bound_reuse=True,
            original_R601_finish_remains_owned_by_original_caller=True,
            no_new_field_target_grid_DFT_solver_or_clock=True)
        self.retired = self.split = self.terminal = 0
        self.unpaid = self.entry_cells = 0
        self.entry_range = None
        self.first_entry = self.last_entry = None
        self.first_unpaid = self.last_unpaid = None
        self.last_retired = None
        self.retirement_chain = hashlib.sha256()
        self.finish_started = False
        self.summary_calls = 0
        self.pending = None
        self.last_complete_bound = None
        self.last_formation_error = None

    def describe(self):
        return encoded(copy.deepcopy(self.binding))

    def work(self, operation, **position):
        self.pending = dict(operation=operation, position=copy.deepcopy(position))
        self.check()

    def up(self, value, operation):
        self.work(operation)
        return self.continuous.A.relative_dyadic_bounds(value, self.sqrt_bits)[1]

    def retire(self, cell, diagnostic, *, split):
        """Same original retirement, no evaluation, root choice or split decision."""
        actions()
        piece = self.field.pieces[cell["piece_index"]]
        if piece["kind"] != "prefix":
            return None
        require(not self.finish_started and type(split) is bool,
                "Retire an original cell once, before the original finish")
        self.retired += 1
        self.split += int(split)
        self.terminal += int(not split)
        self.last_retired = copy.deepcopy(cell)
        record = dict(schema=SCHEMA+"-original-retirement", original_cell=copy.deepcopy(cell),
            original_split=split, original_retirement_index=self.retired,
            complete_same_R553_diagnostic_identity=value_identity(diagnostic),
            complete_same_R553_diagnostic_not_repeated=True,
            paid=False, entry_anchor_candidate=False, entry_radius_enclosure=None,
            actual_same_target_return_identity=None, reasons=[], error=None,
            original_metric_decision_not_changed=True)
        try:
            require(self.retired == self.tubes.committed_prefix_cells
                    and self.split == self.tubes.split_prefix_cells
                    and self.terminal == self.tubes.terminal_prefix_leaves
                    and self.tubes.last_observed_address == cell,
                    "Follow the same actual R553 retirement immediately")
            require(isinstance(diagnostic, dict)
                    and diagnostic.get("schema") == TUBE_SCHEMA+"-cell"
                    and diagnostic.get("original_cell") == cell,
                    "Use the actual complete diagnostic for this original cell")
            if split:
                record["paid"] = True
                record["responsibility_passed_to_all_original_children"] = True
            else:
                require(diagnostic.get("available") is True,
                        "An unpaid terminal tube cannot supply a positive target or anchor")
                scalar = diagnostic["scalar_box"]
                context = scalar["actual_same_target_return"]
                require(context["schema"] == TUBE_SCHEMA+"-same-target-return"
                        and pair(context["original_numeric_s_interval"]) == pair(cell["radial"])
                        and pair(context["radius"]) == pair(scalar["A"]),
                        "Use that same complete original target return, not a second query")
                radial = pair(cell["radial"])
                require(exact(piece["left"]) <= radial[0] <= radial[1] <= exact(piece["right"]),
                        "The actual closed prefix cell is inside its defining span")
                a = pair(scalar["A"])
                require(a[0] > 0, "The same terminal target has no positive lower bound")
                if radial[0] == 0:
                    require(piece["prefix_span"] == 0,
                            "Only the actual first closed prefix span contains the anchor")
                    candidate = (a if self.entry_range is None else
                        (max(self.entry_range[0], a[0]), min(self.entry_range[1], a[1])))
                    require(candidate[0] <= candidate[1],
                            "Enclosures of the identical entry radius contradict")
                    # This is intersection of valid full-cell enclosures of A(0).
                    # No interval midpoint becomes a geometry or target coefficient.
                    self.entry_range = candidate
                    self.entry_cells += 1
                    witness = dict(original_cell=copy.deepcopy(cell),
                        actual_same_target_return_identity=copy.deepcopy(
                            context["actual_target_return_identity"]),
                        entire_original_cell_radius_enclosure=a)
                    if self.first_entry is None:
                        self.first_entry = copy.deepcopy(witness)
                    self.last_entry = copy.deepcopy(witness)
                    record.update(entry_anchor_candidate=True,
                        entry_radius_enclosure=a,
                        actual_same_target_return_identity=copy.deepcopy(
                            context["actual_target_return_identity"]))
                record["paid"] = True
        except ORDINARY as error:
            record["error"] = error_record(error, None)
            record["reasons"].append("same_original_retirement_or_entry_target_unpaid")
        if not record["paid"]:
            self.unpaid += 1
            if self.first_unpaid is None:
                self.first_unpaid = copy.deepcopy(record)
            self.last_unpaid = copy.deepcopy(record)
        self.retirement_chain.update(canonical(record))
        return encoded(record)

    def validate_completed_return(self, returned, original_coverage, complete_cell_ledger):
        c = self.continuous
        require(isinstance(returned, dict)
                and returned.get("schema") == CONTINUOUS_SCHEMA+"-necessary"
                and canonical(returned["binding"]) == canonical(c.describe())
                and returned["original_summary_call_count"] == c.summary_calls == 1
                and c.finish_started is True and c.pending is None
                and returned["recovery_metadata_only"] is False
                and returned["actual_unfinished_operation"] is None
                and returned["formation_error"] is None
                and returned["last_formation_error"] is None
                and c.last_formation_error is None,
                "Consume the actual first completed R601 return, never a stopped or stale one")
        require(returned["complete_prefix_physical_RHS_C0_and_world_C1_bound"] is True
                and returned["both_complete_original_prefix_bounds_returned"] is True
                and canonical(returned["actual_R580_summary"]) == canonical(c.analytic_summary)
                and canonical(returned["actual_R596_summary"]) == canonical(c.saved_summary)
                and canonical(returned["complete_prefix_bound"]) == canonical(c.last_completed_composition),
                "The complete original summaries and bound differ from the actual R601 objects")
        require(returned["original_error"] is None and returned["original_stop"] is None
                and not returned["close_errors"]
                and original_coverage.get("completed_all_DFS_work") is True
                and returned["original_coverage_identity"] == value_identity(original_coverage)
                and complete_cell_ledger is not None
                and canonical(returned["complete_original_cell_ledger"]) == canonical(complete_cell_ledger),
                "Keep the actual full original coverage and complete ledger")
        c.validate_complete_originals(original_coverage, complete_cell_ledger)
        require(self.retired == self.tubes.committed_prefix_cells
                == self.tubes.observed_prefix_cells
                and self.split == self.tubes.split_prefix_cells
                and self.terminal == self.tubes.terminal_prefix_leaves
                == self.tubes.positive_terminal_leaves
                and self.terminal > 0 and self.unpaid == 0
                and self.tubes.unpaid_terminal_leaves == 0
                and self.entry_cells > 0 and self.entry_range is not None,
                "Every original terminal prefix path and its actual entry anchor must be paid")

    def complete_anchor(self):
        self.work("read_complete_original_entry_and_core_words")
        # These bytes were fully checked against the actual checkpoint and
        # all actual Hermite Y/DY arrays by this SAME R596 object.
        S = self.continuous.S
        ywords = S.row_words(self.saved.raw["physical"], 0, self.n)
        cwords = S.row_words(self.saved.raw["core"], 0, self.M)
        y = tuple(S.exact_word(word) for word in ywords)
        core = tuple(S.exact_word(word) for word in cwords)
        require(len(y) == self.n and core == tuple(map(exact, self.field.core))
                and core == tuple(self.Active.exact(v) for v in self.field.saved.core),
                "Retain every original entry and material-core word")
        require(all(self.Active.exact(self.field.nodal[0][0, j]) == y[j]
                    for j in range(self.n)),
                "The actual first Hermite position no longer equals the checked full state")
        rho_plus = Q(1)
        br, bt0, bz = Q(0), abs(y[0]-1), Q(0)
        rows = []
        for j in range(1, self.M+1):
            self.work("complete_original_entry_mode", mode=j, full_modes=self.M)
            n = 2*j
            r, t, z = y[j], y[self.M+j], y[2*self.M+1+j]
            bc, btv = core[j-1]-r, t+n*r
            density = (1-n*n)*core[j-1]
            require(density == exact(self.field.density[j-1]),
                    "The actual complete material expression differs")
            rho_plus += abs(density)
            br += abs(btv)
            bt0 += (n*n-1)*abs(bc)+n*abs(btv)
            bz += n*abs(z)
            rows.append(dict(mode=j, physical_frequency=n, b_t=btv,
                b_c=bc, z=z, exact_density=density))
        require(self.rho_lower == exact(self.field.rho_lower)
                == exact(self.field.saved.rho_lower_exact) and self.rho_lower > 0,
                "The original complete rho lower certificate changed")
        a0lo, a0hi = self.entry_range
        require(a0lo > 0, "The actual entry radius must be uniformly positive")
        a0gap = max(abs(1-a0lo), abs(1-a0hi))
        bt = bt0+a0gap*rho_plus
        self.work("actual_R521_complete_entry_residual_sqrt")
        numerator_square = br*br+bt*bt+bz*bz
        numerator = self.api.sqrt_bounds(numerator_square, self.sqrt_bits)[1]
        q0 = self.up(numerator/(a0lo*self.rho_lower),
                     "round_complete_entry_angular_length_anchor")
        return encoded(dict(
            schema=SCHEMA+"-actual-complete-entry-anchor",
            full_physical_entry_word_count=self.n, complete_core_word_count=self.M,
            actual_entry_words_sha256=hashlib.sha256(self.saved.raw["physical"][:8*self.n]).hexdigest(),
            actual_core_words_sha256=hashlib.sha256(self.saved.raw["core"]).hexdigest(),
            complete_exact_mode_residuals_identity=value_identity(rows),
            all_M_modes_and_both_means_read=True,
            radial_mean_exact=y[0], vertical_mean_exact=y[2*self.M+1],
            vertical_mean_phi_derivative_exact_zero=True,
            boundary_r0_minus_one=y[0]-1, B_r=br,
            B_t_without_radius_difference=bt0, B_t=bt, B_z=bz,
            full_material_density_lower=self.rho_lower,
            full_material_density_upper=rho_plus,
            actual_entry_radius_enclosure=self.entry_range,
            actual_max_abs_one_minus_entry_radius=a0gap,
            actual_entry_radius_candidates=self.entry_cells,
            first_entry_target_witness=self.first_entry,
            last_entry_target_witness=self.last_entry,
            complete_entry_vector_defect_squared_upper=numerator_square,
            complete_entry_vector_defect_upper=numerator,
            complete_entry_relative_angular_length_error_upper=q0,
            exact_formula="sqrt(B_r^2+B_t^2+B_z^2)/(A0_lower*rho_lower)",
            actual_core_minus_entry_r_not_assumed_zero=True,
            all_actual_entry_height_modes_not_assumed_zero=True,
            A0_not_assumed_equal_one=True,
            no_rounded_BC_residual_or_old_mode_bound_substituted=True,
            identity_is_for_reproducibility_not_a_claim_of_transported_coefficient_rows=True))

    def form_bound(self, returned, original_coverage, complete_cell_ledger):
        self.work("validate_actual_complete_R601_return_and_same_retirement")
        self.validate_completed_return(returned, original_coverage, complete_cell_ledger)
        p = returned["complete_prefix_bound"]
        require(p["radial_coordinate"] == "the actual numeric prefix s"
                and p["derivative_coordinate"] == "physical phi in radians"
                and p["component_frame"] == "real Cartesian world frame"
                and p["finite_reference_sigma"] == 1
                and (p["field_modes"], p["angular_count"], p["physical_size"])
                    == (self.M, self.N, self.n),
                "Retain the actual physical derivative units and complete field")
        bounds = self.tubes.minima
        require(isinstance(bounds, dict) and set(bounds) == {"A", "mu", "P", "W"},
                "Use the original complete paid R553 positive-domain extrema")
        lower = {key: exact(value) for key, value in bounds.items()}
        require(all(value > 0 for value in lower.values()),
                "Every original global target/domain lower bound is strictly positive")
        b0 = exact(p["complete_prefix_unprojected_physical_RHS_defect_upper"])
        b1 = exact(p["complete_prefix_unprojected_physical_RHS_world_phi_derivative_upper"])
        require(b0 >= 0 and b1 >= 0, "Complete actual defects are nonnegative")
        anchor = self.complete_anchor()
        q0 = exact(anchor["complete_entry_relative_angular_length_error_upper"])
        delta = self.up(b0/lower["mu"], "round_complete_relative_radial_defect")
        tau = self.up(b1/(lower["A"]*self.rho_lower),
                      "round_complete_physical_angle_length_transport_rate")
        transport = self.up(self.numeric_length*tau,
                            "round_complete_actual_numeric_radial_integral")
        q = self.up(q0+transport, "round_complete_relative_angular_length_error")
        a = self.up(2*delta+delta*delta, "round_normalized_Gram_radial_diagonal_bound")
        b = self.up(delta*(1+q), "round_normalized_Gram_off_diagonal_bound")
        c = self.up(2*q+q*q, "round_normalized_Gram_angular_diagonal_bound")
        self.work("actual_R521_complete_Gram_spectral_sqrt")
        root = self.api.sqrt_bounds((a-c)*(a-c)+4*b*b, self.sqrt_bits)[1]
        eta = self.up((a+c+root)/2, "round_complete_prefix_relative_operator_bound")
        result = encoded(dict(schema=SCHEMA+"-complete-prefix-relative-metric-bound",
            actual_R601_complete_bound_identity=value_identity(p),
            actual_R553_complete_positive_domain_lower=lower,
            actual_complete_original_cell_ledger=copy.deepcopy(complete_cell_ledger),
            actual_complete_retirement_chain=dict(rows=self.retired,
                sha256=self.retirement_chain.hexdigest(),
                all_full_rows_kept_in_the_original_temporary_ledger=True),
            actual_complete_anchor=anchor,
            complete_unprojected_RHS_C0_upper=b0,
            complete_unprojected_RHS_world_phi_C1_upper=b1,
            complete_relative_radial_defect_upper=delta,
            complete_abs_angular_length_radial_derivative_upper=tau,
            actual_numeric_prefix_radial_length=self.numeric_length,
            complete_radial_transport_integral_upper=transport,
            complete_relative_angular_length_error_upper=q,
            normalized_Gram_absolute_entry_upper=dict(radial=a, mixed=b, angular=c),
            complete_prefix_relative_Gram_operator_upper=eta,
            relative_operator_formula="(a+c+sqrt((a-c)^2+4*b^2))/2",
            transport_formula="q0 + L_numeric*B1/(A_lower*rho_lower)",
            radial_defect_formula="B0/mu_lower",
            coordinate="numeric s and physical phi in radians",
            target="mu(s)^2 ds^2 + A(s)^2 rho(phi)^2 dphi^2",
            every_closed_prefix_span_angle_and_seam_endpoint_covered=True,
            complete_R601_and_original_DFS_required_not_partial_extrema=True,
            current_full_rho_is_radially_constant=True,
            actual_complete_R237_density_lower_consumed=True,
            world_registration_is_the_original_constant_proper_SE2=True,
            same_Gram_bound_under_original_whole_lower_reflection=True,
            reflected_velocity_branch_is_negative_original_upper_branch=True,
            no_two_pi_factor_lost_or_applied_twice=True,
            numeric_and_true_lengths_not_identified=True,
            no_radial_sampling_or_new_field_target_evaluation=True,
            no_unknown_exact_solution_or_BVP_inverse_required=True,
            no_q_less_than_one_extra_premise=True,
            all_rounding_is_outward_bound_formation=True,
            actual_common_first_material_and_full_phase_application_not_performed_here=True,
            original_direct_metric_or_native_acceptance_not_replaced=True,
            closed_surface_metric_or_machine_floor_or_refinement_not_claimed=True))
        self.pending = None
        return result

    def summary(self, actual_R601_summary, *, original_coverage,
                complete_cell_ledger, original_error, original_stop, close_errors):
        actions()
        halted = original_error is not None or original_stop is not None or bool(close_errors)
        require(not self.finish_started or halted,
                "Do not repeat scientific bound formation; recovery needs the actual original stop")
        self.finish_started = True
        self.summary_calls += 1
        bound = None
        formation_error = None
        eligible = (not halted and isinstance(actual_R601_summary, dict)
            and actual_R601_summary.get("complete_prefix_physical_RHS_C0_and_world_C1_bound") is True
            and original_coverage.get("completed_all_DFS_work") is True
            and complete_cell_ledger is not None)
        if eligible:
            try:
                bound = self.form_bound(actual_R601_summary, original_coverage, complete_cell_ledger)
                self.last_complete_bound = copy.deepcopy(bound)
            except ORDINARY as error:
                formation_error = error_record(error, self.pending)
                self.last_formation_error = copy.deepcopy(formation_error)
                self.pending = None
        elif not halted:
            self.pending = None
        # RuntimeError (the caller's ResourceStop) and MemoryError propagate.
        # A later stopped metadata call never reforms the anchor or Gram bound.
        return encoded(dict(schema=SCHEMA+"-necessary", binding=self.binding,
            actual_original_R601_summary=copy.deepcopy(actual_R601_summary),
            original_coverage_identity=value_identity(original_coverage),
            complete_original_cell_ledger=copy.deepcopy(complete_cell_ledger),
            original_error=copy.deepcopy(original_error),
            original_stop=copy.deepcopy(original_stop), close_errors=copy.deepcopy(close_errors),
            original_R601_finish_called_here=False,
            original_summary_call_count=self.summary_calls,
            recovery_metadata_only=halted,
            observed_retired_prefix_cells=self.retired,
            original_split_prefix_cells=self.split,
            original_terminal_prefix_cells=self.terminal,
            unpaid_original_retirements=self.unpaid,
            entry_radius_candidate_cells=self.entry_cells,
            observed_entry_radius_enclosure=self.entry_range,
            first_unpaid_retirement=self.first_unpaid,
            last_unpaid_retirement=self.last_unpaid,
            last_retired_prefix_cell=self.last_retired,
            actual_retirement_chain=dict(rows=self.retired, sha256=self.retirement_chain.hexdigest()),
            original_R601_complete_flag_and_original_cover_returned=eligible,
            actual_R601_binding_and_complete_transport_consumed=bound is not None,
            complete_prefix_relative_metric_bound=bound is not None,
            complete_prefix_bound=bound,
            formation_error=formation_error,
            last_formation_error=copy.deepcopy(self.last_formation_error),
            actual_unfinished_operation=copy.deepcopy(self.pending),
            previous_completed_bound_not_current_after_a_stop=(
                copy.deepcopy(self.last_complete_bound) if halted else None),
            all_original_R601_unknown_errors_and_partial_scopes_retained=True,
            original_all_field_node_and_full_source_receipts_retained=True,
            ledger_rows_not_claimed_fully_transported_in_necessary=True,
            ordinary_observer_failure_does_not_reject_original_field=True,
            no_new_original_DFS_metric_FD_fullDN_or_acceptance_predicate=True,
            no_new_clock_child_owner_or_cleanup_permission=True,
            unpaid=["actual common first-material/whole-phase application of this bound",
                "actual tail/collar/accurate-cut-patch continuous defect and its cuff anchor",
                "all original closed-surface seams and cap binding",
                "full closed-surface relative metric floor and actual same-target refinement",
                "reach, held-image amplitude, reflection-inclusive nonrigidity and full diameter"]))


def bind_loaded_prefix_metric_transport(continuous_rhs_defect, *, metric_kernel):
    return BoundPrefixMetricTransport(continuous_rhs_defect, metric_kernel=metric_kernel)
