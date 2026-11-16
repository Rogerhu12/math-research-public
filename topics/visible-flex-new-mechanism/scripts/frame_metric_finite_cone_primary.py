#!/usr/bin/env python3
"""Draft finite Lorentz primary adapter; no entry point or default science budget.

Only the new assembly/call/return interface lives here.  The caller must supply
an authenticated latest checkpoint, the true frozen model, all retained support
rows and a separately authorized new-task budget.  No old LP is called.
All development and scientific execution belongs to public Actions.
"""
from __future__ import annotations
import copy
from fractions import Fraction as Q
from importlib.metadata import version
import math
import time
import numpy as np
from scipy import sparse

from frame_height_null_coordinates import digest
from frame_metric_affine_spectral_model import N, _cut_lp, _candidate, phi, array_digest
from frame_complete_affine_metric_oracle import CompleteGridAffineModel
from frame_height_affine_gate import EvaluationBudgetReached
from frame_metric_budget_recovery import require_public_research_environment

POLICY = "same159-finite-lorentz-affine-primary-v1"
DRAFT_SCHEMA = POLICY+"-unexecuted-adapter"
BACKEND_VERSION = "0.11.1"
KNOWN_CANDIDATE_STATUSES = frozenset(("Solved", "AlmostSolved"))
LABELS = ("coarse", "fine")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def finite_number(value):
    return (not isinstance(value, (bool, np.bool_))
            and isinstance(value, (int, float, np.integer, np.floating))
            and math.isfinite(float(value)))


def finite_array(value, shape, name):
    a = np.asarray(value, float)
    require(a.shape == shape and np.all(np.isfinite(a)), name+" shape/nonfinite")
    return a


def scalar(value, name):
    require(finite_number(value), name+" must be finite")
    return float(value)


def readonly(value):
    out = np.array(value, float, copy=True)
    out.setflags(write=False)
    return out


def snapshot_binding(primary, model, cfg):
    require(isinstance(model, CompleteGridAffineModel) and model.primary is primary
            and primary.affine_spectral_model is model,
            "the final live complete model and original primary must coincide")
    model.oracle._assert_context()
    require(digest(cfg) == model.oracle.config_sha256
            and model.target == float(Q(cfg["fixed_metric_budget_exact"]))
            and model.epsilon == float(Q(cfg["metric_proposal_epsilon_exact"])),
            "caller cfg, target or epsilon differs from the frozen original oracle")
    require(digest(model.binding) == model.binding_sha256
            and digest(model.oracle.binding) == model.oracle.binding_sha256
            and digest(model.selected_model.binding) == model.selected_model.binding_sha256,
            "current complete/oracle/selected bindings changed")
    require(np.asarray(primary.c).shape == (N+2,)
            and np.asarray(primary.A).ndim == 2
            and np.asarray(primary.A).shape[1] == N+2,
            "original159+rho+norm primary required")
    return {
        "configuration_sha256": digest(cfg),
        "complete_model_binding_sha256": model.binding_sha256,
        "oracle_binding_sha256": model.oracle.binding_sha256,
        "selected_binding_sha256": model.selected_model.binding_sha256,
        "primary_final_signature": primary.information["radius_independent_model_sha256"],
        "primary_A_sha256": array_digest(np.asarray(primary.A)),
        "primary_b_sha256": array_digest(np.asarray(primary.b)),
        "primary_c_sha256": array_digest(np.asarray(primary.c)),
        "lower_sha256": array_digest(np.asarray(primary.lower)),
        "upper_sha256": array_digest(np.asarray(primary.upper)),
        "step_scale_sha256": array_digest(np.asarray(primary.step_scale)),
        "guard_sha256": digest(primary.information.get("curvature_defect_guard")),
        "original_target_exact": model.target_exact,
        "original_epsilon_exact": str(Q(model.oracle.cfg["metric_proposal_epsilon_exact"])),
    }


class NewTaskConeLedger:
    """Explicit new-task solver account; never imports the old64 as new calls.

    This owns solver starts and the science clock only.  The actual objective's
    wall callback must also enforce the separately authorized true-value cap.
    Legacy LP/SOC entry points, if later authorized, must update these same
    total counters before starting.  This module has no such entry point.
    """
    def __init__(self, *, limits, scientific_started, global_scientific_deadline,
                 ancestor_receipt):
        names = {"max_new_solver_calls", "max_new_cone_calls",
                 "max_new_legacy_LP_calls", "max_new_actual_values",
                 "max_scientific_seconds", "max_single_solver_seconds"}
        require(isinstance(limits, dict) and set(limits) == names,
                "all independent new-task limits required; no defaults")
        for key in ("max_new_solver_calls", "max_new_cone_calls",
                    "max_new_legacy_LP_calls", "max_new_actual_values"):
            require(type(limits[key]) is int and limits[key] >= 0,
                    "nonnegative true integer new-task count required: "+key)
        require(limits["max_new_cone_calls"] <= limits["max_new_solver_calls"]
                and limits["max_new_legacy_LP_calls"] <= limits["max_new_solver_calls"],
                "subcall limits exceed the declared total")
        for key in ("max_scientific_seconds", "max_single_solver_seconds"):
            require(finite_number(limits[key]) and limits[key] > 0,
                    "finite positive explicit time limit required: "+key)
        require(finite_number(scientific_started) and scientific_started <= time.monotonic(),
                "clock must start before this task's input preparation")
        require(isinstance(ancestor_receipt, dict) and ancestor_receipt,
                "complete paid ancestor-cost provenance required")
        self.limits = copy.deepcopy(limits)
        self.scientific_started = float(scientific_started)
        require(finite_number(global_scientific_deadline),
                "finite original global scientific deadline required")
        self.global_scientific_deadline = float(global_scientific_deadline)
        self.ancestor_receipt = copy.deepcopy(ancestor_receipt)
        self.total_started = self.cone_started = self.legacy_LP_started = 0
        self.events = []

    def remaining_seconds(self):
        now = time.monotonic()
        return min(float(self.limits["max_scientific_seconds"])-(now-self.scientific_started),
                   self.global_scientific_deadline-now)

    def check_clock(self):
        remaining = self.remaining_seconds()
        if not math.isfinite(remaining) or remaining <= 0:
            raise EvaluationBudgetReached("new finite-cone or original global scientific clock exhausted")
        return remaining

    def _counts(self):
        require(self.total_started == self.cone_started+self.legacy_LP_started
                and all(type(v) is int and v >= 0 for v in (
                    self.total_started, self.cone_started, self.legacy_LP_started)),
                "new-task solver accounting identity changed")

    def charge_cone(self, event, *, absolute_primary_ceiling):
        self._counts()
        require(type(absolute_primary_ceiling) is int
                and 0 <= absolute_primary_ceiling <= self.limits["max_new_solver_calls"],
                "explicit current primary ceiling inside the new total required")
        if (self.total_started >= absolute_primary_ceiling
                or self.total_started >= self.limits["max_new_solver_calls"]
                or self.cone_started >= self.limits["max_new_cone_calls"]):
            raise EvaluationBudgetReached("new finite-cone task solver allocation exhausted")
        remaining = self.check_clock()
        limit = min(float(self.limits["max_single_solver_seconds"]), remaining)
        self.total_started += 1
        self.cone_started += 1
        event.update(
            new_total_solver_ordinal=self.total_started,
            new_cone_solver_ordinal=self.cone_started,
            time_limit_seconds=limit, charged_before_backend_constructor=True,
            old_direct_task_LP_ledger_not_modified=True)
        self.events.append(event)
        self._counts()
        return limit

    def report(self):
        self._counts()
        return {
            "policy": POLICY, "limits": copy.deepcopy(self.limits),
            "new_solver_calls_started": self.total_started,
            "new_cone_calls_started": self.cone_started,
            "new_legacy_LP_calls_started": self.legacy_LP_started,
            "new_scientific_seconds": time.monotonic()-self.scientific_started,
            "remaining_scientific_seconds_in_intersection": self.remaining_seconds(),
            "time_limit_includes_original_global_deadline": True,
            "ancestor_receipt": copy.deepcopy(self.ancestor_receipt),
            "original64_not_restarted_or_relabelled_as_new_calls": True,
            "true_value_cap_owned_by_the_actual_objective_wall": True,
        }


class FiniteConePrimary:
    """Same161 original model with whole branch cones for explicit original rows."""

    def __init__(self, primary, model, cfg, original_tags, *,
                 retained_A, retained_b, retained_record,
                 expected_current_binding, wall):
        require(callable(wall), "authoritative time/value wall callback required")
        wall()
        self.primary, self.model, self.cfg, self.wall = primary, model, cfg, wall
        self.binding = snapshot_binding(primary, model, cfg)
        require(self.binding == expected_current_binding,
                "caller must bind the final two-factory current model exactly")
        scale = finite_array(primary.step_scale, (N,), "physical step scale")
        require(np.all(scale > 0), "strictly positive original physical step scale required")
        self.scale = readonly(scale)
        A = np.asarray(retained_A, float)
        b = np.asarray(retained_b, float)
        require(A.ndim == 2 and A.shape[1] == N+2 and b.shape == (len(A),)
                and np.all(np.isfinite(A)) and np.all(np.isfinite(b)),
                "complete current retained support matrix required")
        require(isinstance(retained_record, dict)
                and retained_record.get("rows") == len(b)
                and retained_record.get("A_sha256") == array_digest(A)
                and retained_record.get("b_sha256") == array_digest(b)
                and retained_record.get("all_actual_source_supports_retained") is True
                and isinstance(retained_record.get("source_manifest_sha256"), str),
                "explicit full support-provenance and rebuilt-array receipt required")
        self.retained_A, self.retained_b = readonly(A), readonly(b)
        self.retained_record = copy.deepcopy(retained_record)
        self.linear = _cut_lp(primary, [self.retained_A], [self.retained_b],
                              [self.retained_record])
        require(np.array_equal(self.linear.A[:len(primary.b)], primary.A)
                and np.array_equal(self.linear.b[:len(primary.b)], primary.b)
                and np.array_equal(self.linear.c, primary.c)
                and np.array_equal(self.linear.lower, primary.lower)
                and np.array_equal(self.linear.upper, primary.upper),
                "an original row, target, objective or bound was changed")
        require(isinstance(original_tags, (list, tuple)) and original_tags,
                "explicit nonempty finite original-row cone set required")
        self.tags, self.rows, self.row_sources = [], [], []
        seen = set()
        started = time.monotonic()
        for given in original_tags:
            wall()
            require(isinstance(given, dict), "full original row tag required")
            label, flat = given.get("grid"), given.get("flat_row_id")
            require(label in LABELS and type(flat) is int and type(given.get("group")) is int,
                    "true integer original metric row/group required")
            grid = model.oracle.grids[label]
            require(0 <= flat < 2*grid.point_count and given == grid.coordinate(flat)
                    and given["group"] == flat//grid.point_count,
                    "original grid coordinate/metric branch differs")
            key = (label, flat)
            if key in seen:
                continue
            seen.add(key)
            selected = model.selected_full_row_lookup.get(key)
            if selected is None:
                # Reuse another selected branch at the same physical point if available.
                selected = next((j for j, tag in enumerate(model.selected_model.tags)
                    if tag["grid"] == label
                    and tag["flat_row_id"] % grid.point_count == flat % grid.point_count), None)
            if selected is None:
                raw = model.oracle.original_row(label, flat)
                source = raw["source"]
            else:
                old = model.selected_model
                raw = {"e": old.e[selected], "f": old.f[selected],
                       "de": old.de[selected], "df": old.df[selected]}
                source = "existing-current-selected-original-point"
            row = {
                "e": scalar(raw["e"], "current e"), "f": scalar(raw["f"], "current f"),
                "de": readonly(finite_array(raw["de"], (N,), "physical de")),
                "df": readonly(finite_array(raw["df"], (N,), "physical df")),
                "group": int(given["group"]), "target": float(model.target),
            }
            self.tags.append(copy.deepcopy(given))
            self.rows.append(row)
            self.row_sources.append(source)
        self.original_row_preparation_seconds = time.monotonic()-started
        self._assert_current()
        self._assemble()
        self._assert_current()
        wall()

    def _assert_current(self):
        require(snapshot_binding(self.primary, self.model, self.cfg) == self.binding,
                "a center/grid/pool/J/guard/final-factory binding changed")
        require(array_digest(self.retained_A) == self.retained_record["A_sha256"]
                and array_digest(self.retained_b) == self.retained_record["b_sha256"],
                "the retained support matrix changed")

    def _assemble(self):
        started = time.monotonic()
        lp = self.linear
        c = finite_array(lp.c, (N+2,), "original objective")
        A = finite_array(lp.A, (len(lp.b), N+2), "original linear rows plus supports")
        b = finite_array(lp.b, (len(lp.b),), "original linear RHS")
        lower, upper = np.asarray(lp.lower, float), np.asarray(lp.upper, float)
        require(lower.shape == upper.shape == (N+2,)
                and not np.any(np.isnan(lower)) and not np.any(np.isnan(upper))
                and not np.any(lower == np.inf) and not np.any(upper == -np.inf)
                and np.all(lower <= upper), "original finite/infinite bound contract differs")
        bound_rows, bound_rhs = [], []
        for j in range(N+2):
            if math.isfinite(float(upper[j])):
                row = np.zeros(N+2); row[j] = 1.
                bound_rows.append(row); bound_rhs.append(float(upper[j]))
            if math.isfinite(float(lower[j])):
                row = np.zeros(N+2); row[j] = -1.
                bound_rows.append(row); bound_rhs.append(-float(lower[j]))
        blocks = [sparse.csc_matrix(A)]
        rhs = [b.copy()]
        if bound_rows:
            blocks.append(sparse.csc_matrix(np.asarray(bound_rows)))
            rhs.append(np.asarray(bound_rhs, float))
        self.linear_cone_rows = len(b)+len(bound_rhs)
        epsilon = scalar(self.model.epsilon, "original epsilon")
        require(epsilon > 0, "original strictly positive epsilon required")
        for row in self.rows:
            sign = 1. if row["group"] == 0 else -1.
            de = row["de"]*self.scale
            df = row["df"]*self.scale
            block = np.zeros((4, N+2))
            block[0, :N], block[0, N] = sign*de, -2.
            block[1, :N], block[2, :N] = -de, -2*df
            blocks.append(sparse.csc_matrix(block))
            rhs.append(np.array([2*row["target"]-sign*row["e"],
                                 row["e"], 2*row["f"], epsilon]))
        self.P = sparse.csc_matrix((N+2, N+2), dtype=float)
        self.A = sparse.vstack(blocks, format="csc")
        self.b = np.concatenate(rhs)
        self.c = c.copy()
        self.assembly_seconds = time.monotonic()-started
        self.assembly_record = {
            "schema": POLICY+"-finite-cone-assembly",
            "physical_columns": N, "total_variables": N+2,
            "original_linear_rows": len(self.primary.b),
            "retained_support_rows": len(self.retained_b),
            "finite_bound_rows": len(bound_rhs), "linear_cone_rows": self.linear_cone_rows,
            "lorentz4_cones": len(self.tags), "assembled_rows": len(self.b),
            "A_csc_nnz": int(self.A.nnz),
            "A_data_sha256": array_digest(self.A.data),
            "A_indices_sha256": array_digest(self.A.indices),
            "A_indptr_sha256": array_digest(self.A.indptr),
            "b_sha256": array_digest(self.b), "c_sha256": array_digest(self.c),
            "zero_quadratic_objective": True, "original_binding": copy.deepcopy(self.binding),
            "original_cone_tags": copy.deepcopy(self.tags),
            "row_sources": list(self.row_sources),
            "retained_support_receipt": copy.deepcopy(self.retained_record),
            "original_row_preparation_seconds": self.original_row_preparation_seconds,
            "assembly_seconds": self.assembly_seconds,
            "physical_de_df_multiplied_by_step_scale_exactly_once": True,
            "no_old_support_row_deleted": True,
            "finite_rows_do_not_claim_complete_grid_coverage": True,
        }

    def cone_residual(self, variables):
        x = finite_array(variables, (N+2,), "original161 candidate")
        raw = np.asarray(self.b-self.A@x)
        values = raw[self.linear_cone_rows:].reshape(len(self.rows), 4)
        signed = np.hypot(np.hypot(values[:, 1], values[:, 2]), values[:, 3])-values[:, 0]
        p = self.scale*x[:N]
        direct = np.array([
            float(phi([r["e"]+float(r["de"]@p)],
                      [r["f"]+float(r["df"]@p)],
                      [r["group"]], self.model.epsilon)[0])-r["target"]-float(x[N])
            for r in self.rows])
        require(np.all(np.isfinite(signed)) and np.all(np.isfinite(direct)),
                "nonfinite original-unit cone residual")
        return {
            "maximum_signed_cone_residual": float(np.max(signed)),
            "maximum_signed_half_cone_metric_residual": float(np.max(signed/2)),
            "maximum_signed_direct_metric_residual": float(np.max(direct)),
            "maximum_metric_violation": max(0., float(np.max(signed/2)),
                                            float(np.max(direct))),
            "direct_vs_half_assembly_max_abs_difference": float(np.max(abs(direct-signed/2))),
            "cone_metric_relation_factor": 2,
            "signed_values_not_clipped_or_labelled_exact": True,
        }


def solve_finite_cone_once(prepared, *, ledger, absolute_primary_ceiling,
                          settings_parameters, candidate_statuses, progress):
    """One separately charged conic call, then the frozen complete-model repair.

    This does not select new rows, start another solve, change actual pools or
    evaluate physical geometry.  The outer must preserve each actual candidate
    and all original trial gates.  No default new budget or allowed status exists.
    """
    require_public_research_environment()
    require(isinstance(prepared, FiniteConePrimary)
            and isinstance(ledger, NewTaskConeLedger)
            and isinstance(progress, dict) and callable(prepared.wall),
            "explicit bound finite problem, independent ledger and progress required")
    def wall():
        prepared.wall()  # Original/caller physical-value and global-time gates.
        ledger.check_clock()  # This independent task deadline also binds the adapter.
    require(isinstance(candidate_statuses, (list, tuple)) and candidate_statuses
            and len(set(candidate_statuses)) == len(candidate_statuses)
            and set(candidate_statuses) <= KNOWN_CANDIDATE_STATUSES,
            "explicit reviewed Solved/AlmostSolved candidate policy required")
    required_settings = {"max_iter", "max_threads", "tol_gap_abs", "tol_gap_rel", "tol_feas"}
    require(isinstance(settings_parameters, dict) and set(settings_parameters) == required_settings,
            "all reviewed finite-cone settings required")
    require(type(settings_parameters["max_iter"]) is int and settings_parameters["max_iter"] > 0
            and type(settings_parameters["max_threads"]) is int
            and settings_parameters["max_threads"] == 1,
            "positive iteration cap and one thread required")
    for key in ("tol_gap_abs", "tol_gap_rel", "tol_feas"):
        require(finite_number(settings_parameters[key]) and settings_parameters[key] > 0,
                "positive explicitly reviewed backend tolerance required")
    wall()
    prepared._assert_current()
    require(version("clarabel") == BACKEND_VERSION, "pinned Clarabel backend version differs")
    import clarabel
    settings = clarabel.DefaultSettings()
    for key, value in settings_parameters.items():
        setattr(settings, key, value)
    settings.verbose = False
    cones = [clarabel.NonnegativeConeT(prepared.linear_cone_rows)]
    cones.extend(clarabel.SecondOrderConeT(4) for _ in prepared.rows)
    event = {
        "schema": POLICY+"-one-call", "backend": "clarabel", "backend_version": BACKEND_VERSION,
        "status": "preparing-backend", "settings": copy.deepcopy(settings_parameters),
        "allowed_candidate_statuses": list(candidate_statuses),
        "assembly": copy.deepcopy(prepared.assembly_record),
        "new_actual_geometry_calls_inside_adapter": 0,
        "old_LP_calls_inside_adapter": 0,
    }
    # Charge before the backend constructor, which may itself perform work.
    wall()
    try:
        settings.time_limit = ledger.charge_cone(
            event, absolute_primary_ceiling=absolute_primary_ceiling)
    except EvaluationBudgetReached as error:
        event.update(status="new-cone-call-not-started", reason=str(error))
        progress["last_unstarted_cone_attempt"] = event
        raise
    progress.setdefault("cone_calls", []).append(event)
    started = time.monotonic()
    try:
        # Public settings are read after all overrides, including the actual time limit.
        # No backend/default value is inferred from documentation or an old run.
        settings_record = {}
        for name in sorted(n for n in dir(settings) if not n.startswith("_")):
            value = getattr(settings, name)
            if callable(value):
                continue
            if value is None or isinstance(value, (bool, str, int)):
                settings_record[name] = value
            elif isinstance(value, float):
                settings_record[name] = value if math.isfinite(value) else repr(value)
            else:
                settings_record[name] = repr(value)
        event["actual_backend_settings_including_defaults"] = settings_record
        solver = clarabel.DefaultSolver(prepared.P, prepared.c, prepared.A,
                                        prepared.b, cones, settings)
        event["backend_constructor_seconds"] = time.monotonic()-started
        wall()
        solution = solver.solve()
        # Capture the actual finite vector before even ancillary backend metadata
        # is read; a status/timing getter failure must not lose a returned step.
        x = np.asarray(solution.x, float)
        finite = x.shape == (N+2,) and np.all(np.isfinite(x))
        event["finite_original161_vector"] = bool(finite)
        if finite:
            p = prepared.scale*x[:N]
            event["new_candidate_step_record"] = {
                "exact_binary64_independent_step": [str(Q.from_float(float(v))) for v in p],
                "array_sha256": array_digest(p),
                "source": "this new cone solver vector before any return filter",
                "not_a_reconstruction_of_any_unknown_old_step": True,
                "no_additional_geometry_or_JVP_for_capture": True,
            }
        event.update(
            status="backend-returned", backend_status=str(solution.status),
            backend_reported_solve_seconds=scalar(solution.solve_time, "backend solve_time"),
            elapsed_seconds=time.monotonic()-started)
        wall()
        prepared._assert_current()
        if not finite or str(solution.status) not in candidate_statuses:
            event["status"] = "backend-status-or-finite-vector-not-eligible"
            return None, event
        event["raw_original_linear_residual"] = prepared.linear.residual(x)
        event["raw_included_cone_residual"] = prepared.cone_residual(x)
        raw = event["raw_original_linear_residual"]
        if max(raw["maximum_original_linear_row_violation"],
               raw["maximum_original_linear_bound_violation"]) > prepared.cfg["linear_model_residual_limit"]:
            event["status"] = "raw-original-linear-or-bound-gate-failed"
            return None, event
        bridge = {
            "status": str(solution.status), "success": True,
            "solver_backend": "clarabel", "not_a_HiGHS_or_old_LP_report": True,
            "normalized_step_norm": float(x[N+1]),
            "predicted_metric_slack": float(x[N]),
            "primary_step_cost_diagnostic": {
                "backend_objective": float(prepared.c@x),
                "backend_epigraph": float(x[N]),
                "backend_norm_auxiliary": float(x[N+1])},
        }
        # This is the actual path used by the frozen model: slack(), not evaluated().
        # The new exact step was already captured above, with no extra call.
        wall()
        candidate = _candidate(prepared.linear, p, bridge, prepared.model, prepared.cfg)
        event["repaired_included_cone_residual"] = prepared.cone_residual(candidate["variables"])
        cone_limit = float(prepared.cfg["linear_model_residual_limit"])
        if event["repaired_included_cone_residual"]["maximum_metric_violation"] > cone_limit:
            event["status"] = "repaired-included-cone-original-unit-gate-failed"
            return None, event
        event.update(
            status="complete-affine-candidate-repaired",
            original_solver_rho=float(x[N]), complete_affine_rho=candidate["rho"],
            repaired_rho_auxiliary=candidate["repaired_rho_auxiliary"],
            retained_solver_norm_auxiliary=candidate["norm_auxiliary"],
            repaired_objective=candidate["objective"], raw_epigraph_gap=candidate["raw_epigraph_gap"],
            gap_tolerance=candidate["gap_tolerance"], gap_met=candidate["gap_met"],
            evaluated_model_gain=candidate["gain"],
            repaired_original_residual=copy.deepcopy(candidate["repaired_residual"]),
            candidate_positive_above_original_floor=
                bool(candidate["gain"] > prepared.cfg["linear_model_improvement_floor"]),
            exact_optimality_or_actual_physical_acceptance_claim=False)
        wall()
        prepared._assert_current()
        return candidate, event
    except Exception as error:
        event.update(status="started-conic-or-repair-call-raised",
                     error={"type": type(error).__name__, "message": str(error)},
                     elapsed_seconds=time.monotonic()-started)
        raise
    finally:
        event["complete_call_and_repair_elapsed_seconds"] = time.monotonic()-started
