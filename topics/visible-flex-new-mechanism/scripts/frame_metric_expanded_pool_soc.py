#!/usr/bin/env python3
"""One expanded-pool, same-failed-trial SOC, with explicit model identities.

New interface only. Scientific and developer execution belongs to public Actions.
The ordinary geometry, selected scalar derivatives, physical model, SOC arrays,
and actual acceptance gates are inherited unchanged.
"""
from __future__ import annotations
import copy
from dataclasses import dataclass
from fractions import Fraction as Q
import hashlib
from pathlib import Path
import time
import numpy as np
from scipy.optimize import linprog

from frame_height_null_coordinates import digest
from frame_entry_body_subspace import FullGridValues, array_digest
from frame_entry_tail_height_blocks import (
    N, P, build_correction, scale_mapped_correction, correction_independent_step)
from frame_metric_entry_tail_height159 import (
    selected_model, inherited_proposal_floor_report)
from frame_metric_height159_soc_hold import model_binding
from frame_metric_budget_recovery import EvaluationBudgetReached
from frame_metric_norm_direction_memory import RememberingCompleteObjective

POLICY = "same159-expanded-pool-rebound-SOC-v1"


def original_model_constants(cfg):
    """Read the unchanged source cfg; do not add policy metadata to its hash."""
    names = ("linear_fraction_to_boundary_exact",
             "step_cost_physical_box_norm_coefficient_exact",
             "strip_proposal_floor_exact", "curvature_proposal_floor_exact",
             "SOC_physical_margin_retention_exact",
             "SOC_predicted_descent_retention_exact",
             "SOC_maximum_correction_relative_to_proposed_step_exact")
    result = {name: str(Q(cfg[name])) for name in names}
    result["linear_model_improvement_floor_binary64_exact"] = str(
        Q.from_float(float(cfg["linear_model_improvement_floor"])))
    return result


def definition():
    return {
        "policy": POLICY,
        "one_rebound_after_new_rows_on_first_full_primary_only": True,
        "same_accepted_center_and_same_actual_failed_trial": True,
        "new_pool_requires_new_base_J_primary_and_complete_model": True,
        "Jacobian_source": "accepted x, on the complete enlarged original ID pools",
        "SOC_residual_source": "frozen already-computed same y on both original grids",
        "actual_d_is_y_minus_x_and_apply_must_reproduce_y_bitwise": True,
        "original_SOC_scalar_budget_floors_scaling_and_true_gates_retained": True,
        "original_learning_records_never_erased_for_SOC_hold": True,
        "rebound_complete_models_separate_from_primary_models": True,
        "all_oracles_remain_in_total_cost_registry": True,
        "all_started_LPs_use_original_shared_ledger": True,
        "no_clock_radius_streak_capacity_or_value_budget_reset": True,
        "no_recursive_rebound_after_corrected_trial": True,
    }


def implementation_hashes():
    folder = Path(__file__).parent
    return {name: hashlib.sha256((folder/name).read_bytes()).hexdigest()
            for name in ("frame_metric_expanded_pool_soc.py",
                         "frame_metric_expanded_pool_soc_recovery.py",
                         "frame_metric_expanded_pool_soc_development.py")}


def _same(a, b):
    a, b = np.asarray(a), np.asarray(b)
    return a.shape == b.shape and a.dtype == b.dtype and a.tobytes() == b.tobytes()


def _frozen(a, dtype=float):
    result = np.array(a, dtype=dtype, copy=True)
    if dtype is float and not np.all(np.isfinite(result)):
        raise ValueError("finite frozen original array required")
    result.setflags(write=False)
    return result


def verify_initial_bank(bank, expected_sha, expected_entries):
    if (not isinstance(expected_sha, str) or len(expected_sha) != 64
            or any(ch not in "0123456789abcdef" for ch in expected_sha)
            or type(expected_entries) is not int or expected_entries < 1):
        raise ValueError("explicit original bank SHA256 and positive integer size required")
    report = bank.report()
    actual_sha = bank.state_digest()
    actual_entries = int(report["entries"])
    result = {
        "schema": POLICY+"-initial-bank-replay",
        "expected_state_sha256": expected_sha,
        "actual_state_sha256": actual_sha,
        "expected_entries": expected_entries,
        "actual_entries": actual_entries,
        "passed": actual_sha == expected_sha and actual_entries == expected_entries,
        "comparison_after_pending_original_events_before_first_LP": True,
        "no_old_numeric_cut_A_b_or_optimizer_reused": True,
    }
    if not result["passed"]:
        error = ValueError("original 21-event norm bank replay did not match declared state/size")
        error.bank_restore_record = result
        raise error
    return result


def actual_failed_step(subspace, x, y):
    x, y = _frozen(x), _frozen(y)
    if x.shape != (N,) or y.shape != (N,):
        raise ValueError("actual independent159 x and y required")
    step = _frozen(y-x)
    recreated = subspace.apply(x, step[subspace.columns])
    if not _same(np.asarray(recreated, float), y):
        raise ValueError("actual y-x does not bitwise recreate the same failed y")
    if not np.any(step):
        raise ValueError("zero actual failed displacement has no SOC target")
    return step


def freeze_full_views(views):
    if len(views) != 2 or [v.grid.label for v in views] != ["coarse", "fine"]:
        raise ValueError("ordered original coarse/fine full views required")
    frozen = []
    for v in views:
        mean = None if v.mean_Xs is None else _frozen(v.mean_Xs)
        item = FullGridValues(v.grid, _frozen(v.rows), _frozen(v.eta),
                              _frozen(v.b), _frozen(v.tolerances), mean)
        for key in ("rows", "eta", "b", "tolerances", "mean_Xs"):
            value = getattr(item, key)
            if isinstance(value, np.ndarray):
                value.setflags(write=False)
        frozen.append(item)
    if not _same(frozen[0].b, frozen[1].b):
        raise ValueError("same failed y must retain the same common current height")
    return tuple(frozen)


@dataclass(frozen=True)
class FailedTrial:
    x: np.ndarray
    y: np.ndarray
    step: np.ndarray
    views: tuple
    old_ids: tuple
    new_ids: tuple
    old_versions: tuple
    new_versions: tuple
    original_primary: object
    original_binding: dict
    model_number: int
    primary_trial_index: int
    report: dict


@dataclass(frozen=True)
class ReboundContext:
    primary: object
    affine: object
    base: np.ndarray
    J: np.ndarray
    groups: np.ndarray
    tolerances: np.ndarray
    versions: tuple
    binding: dict
    failed: FailedTrial
    trial_rows: np.ndarray
    record: dict


def capture_failed_trial(objective, primary, x, y, old_versions, original_binding,
                         model_number, primary_trial_index, trial, cfg):
    if (trial.get("kind") != "primary-metric-short-step"
            or trial.get("alpha_exact") != "1"
            or trial.get("accepted_as_next_iterate") is not False
            or trial.get("fine_decision") is None
            or trial.get("coarse_decision") is None):
        raise ValueError("one completed unaccepted full primary trial required")
    for label in ("coarse", "fine"):
        flags = trial[label+"_decision"]
        if not flags.get("regularity_screen_pass", False):
            raise ValueError("both actual primary grids must be regular")
    x, y = _frozen(x), _frozen(y)
    step = actual_failed_step(objective.subspace, x, y)
    if not _same(np.asarray(primary.state, float), x):
        raise ValueError("primary state is not the exact accepted x")
    x_sha, y_sha = (digest(objective.problem.identity(q)) for q in (x, y))
    if y_sha != trial.get("physical_state_sha256"):
        raise ValueError("trial's canonical physical y SHA differs")
    if model_binding(primary, x, x_sha, old_versions) != original_binding:
        raise ValueError("original accepted model binding differs")
    old_ids = tuple(_frozen(s.ids, np.int64) for s in primary.selections)
    new_ids = (_frozen(objective.pool, np.int64),
               _frozen(objective.fine_pool, np.int64))
    versions = (int(objective.pool_version), int(objective.fine_pool_version))
    if versions == tuple(old_versions):
        raise ValueError("no pool layout change to rebind")
    if not any(len(b) > len(a) for a, b in zip(old_ids, new_ids)):
        raise ValueError("rebound requires at least one genuinely added original ID")
    for a, b in zip(old_ids, new_ids):
        if not np.all(np.isin(a, b)) or len(np.unique(b)) != len(b):
            raise ValueError("new pools must retain every original distinct ID")
    # full_views itself checks both current caches equal this actual y.
    views = freeze_full_views(objective.full_views(y))
    report = {
        "schema": POLICY+"-same-failed-y",
        "unchanged_original_model_constants": original_model_constants(cfg),
        "status": "same-y-captured-before-restoring-x",
        "model_number": int(model_number),
        "primary_trial_index": int(primary_trial_index),
        "base_independent_array_sha256": array_digest(x),
        "failed_independent_array_sha256": array_digest(y),
        "actual_y_minus_x_array_sha256": array_digest(step),
        "base_physical_state_sha256": x_sha,
        "failed_physical_state_sha256": y_sha,
        "old_pool_versions": list(map(int, old_versions)),
        "new_pool_versions": list(versions),
        "old_pool_ids_sha256": [array_digest(v) for v in old_ids],
        "new_pool_ids_sha256": [array_digest(v) for v in new_ids],
        "old_counts": [len(v) for v in old_ids],
        "new_counts": [len(v) for v in new_ids],
        "frozen_trial": [
            {"grid_definition_sha256": v.grid.definition_sha256,
             "all_rows_sha256": array_digest(v.rows),
             "common_b_sha256": array_digest(v.b)}
            for v in views],
        "original_learning_counts_preserved": {
            key: trial.get(key) for key in
            ("new_coarse_rows", "new_fine_rows",
             "coarse_omitted_hard_rows", "fine_omitted_hard_rows")},
        "apply_actual_y_minus_x_reproduces_y_bitwise": True,
        "no_new_geometry_call_in_capture": True,
    }
    return FailedTrial(x, y, step, views, old_ids, new_ids, tuple(old_versions),
                       versions, primary, copy.deepcopy(original_binding),
                       int(model_number), int(primary_trial_index), report)


def require_current_layout(objective, failed):
    if (int(objective.pool_version), int(objective.fine_pool_version)) != failed.new_versions:
        raise ValueError("current enlarged pool versions changed again")
    for a, b in zip((objective.pool, objective.fine_pool), failed.new_ids):
        if not _same(np.asarray(a, np.int64), b):
            raise ValueError("current enlarged pool ID order changed again")


def validate_rebuilt_primary(old, new, failed):
    if not _same(np.asarray(new.state, float), failed.x):
        raise ValueError("rebuilt primary moved the accepted center")
    if new.trust != old.trust:
        raise ValueError("rebinding changed the original body radius")
    for key in ("original_lower", "original_upper", "width", "qscale", "K", "step_scale"):
        if not _same(np.asarray(getattr(old, key)), np.asarray(getattr(new, key))):
            raise ValueError("rebinding changed physical boxes/scales: "+key)
    if (old.subspace.definition_sha256 != new.subspace.definition_sha256
            or not _same(np.asarray(old.subspace.M), np.asarray(new.subspace.M))):
        raise ValueError("rebinding changed159-to163 physical map")
    for s, ids, actual in zip(new.selections, failed.new_ids, failed.views):
        if (not _same(np.asarray(s.ids, np.int64), ids)
                or s.full.grid.definition != actual.grid.definition):
            raise ValueError("rebuilt IDs or complete-grid definition differ")
    if old.information["physical_norm_weight_exact"] != new.information["physical_norm_weight_exact"]:
        raise ValueError("rebuilt primary changed its recorded physical objective weight")
    return True


def _detached_rebound_factory(objective, primary, record):
    """Reuse the real factory, keep oracle costs, remove only its extra model."""
    nm, no = len(objective.complete_models), len(objective.complete_oracles)
    prefix = tuple(objective.complete_models)
    complete = None
    try:
        complete = RememberingCompleteObjective.primary_observable_model(objective, primary)
        if (len(objective.complete_models) != nm+1
                or objective.complete_models[-1] is not complete
                or len(objective.complete_oracles) != no+1
                or objective.complete_oracles[-1] is not complete.oracle):
            raise ArithmeticError("real complete factory append contract changed")
        record.update(complete_model_binding_sha256=complete.binding_sha256,
                      oracle_index=no, status="rebound-complete-model-ready")
        return complete
    except Exception as error:
        record.update(status="rebound-factory-failed",
                      error={"type": type(error).__name__, "message": str(error)})
        raise
    finally:
        # Never erase oracle costs, even when a partially built model fails.
        record["retained_oracle_indices"] = list(range(no, len(objective.complete_oracles)))
        if len(objective.complete_models) < nm or any(
                a is not b for a, b in zip(objective.complete_models[:nm], prefix)):
            raise ArithmeticError("real complete factory modified an earlier primary model")
        del objective.complete_models[nm:]


class ExpandedPoolSOCObjective(RememberingCompleteObjective):
    def __init__(self, *args, initial_direction_records=(),
                 expanded_pool_policy,
                 expected_initial_bank_state_sha256,
                 expected_initial_bank_entries, **kwargs):
        if expanded_pool_policy != POLICY:
            raise ValueError("explicit expanded-pool same-trial SOC policy required")
        self.expanded_pool_policy = expanded_pool_policy
        if type(expected_initial_bank_entries) is not int or expected_initial_bank_entries != 9:
            raise ValueError("the completed original nine-entry bank is required")
        self.expected_initial_bank_state_sha256 = expected_initial_bank_state_sha256
        self.expected_initial_bank_entries = expected_initial_bank_entries
        self.initial_bank_replay = {
            "schema": POLICY+"-initial-bank-replay", "passed": False,
            "status": "pending-first-complete-model-no-LP-yet"}
        self.rebound_models = []
        self.rebound_records = []
        super().__init__(*args, initial_direction_records=initial_direction_records, **kwargs)
        self.evaluation_definition["expanded_pool_same_trial_SOC"] = definition()
        self.evaluation_definition["expected_initial_bank"] = {
            "state_sha256": expected_initial_bank_state_sha256,
            "entries": expected_initial_bank_entries}
        self.evaluation_sha256 = digest(self.evaluation_definition)

    def primary_observable_model(self, primary):
        model = super().primary_observable_model(primary)
        if not self.initial_bank_replay.get("passed", False):
            try:
                self.initial_bank_replay = verify_initial_bank(
                    self.direction_bank, self.expected_initial_bank_state_sha256,
                    self.expected_initial_bank_entries)
                self.initial_bank_replay["status"] = "original-bank-exactly-replayed-before-first-LP"
            except ValueError as error:
                self.initial_bank_replay = copy.deepcopy(getattr(
                    error, "bank_restore_record", {"passed": False, "error": str(error)}))
                raise
        return model

    def rebuild_failed_context(self, failed, trust, cfg):
        self._wall()
        require_current_layout(self, failed)
        if failed.report["unchanged_original_model_constants"] != original_model_constants(cfg):
            raise ValueError("rebinding changed the original fraction/floors/weights/retention")
        if not self.initial_bank_replay.get("passed") or self.pending_initial_directions:
            raise ValueError("initial original bank must already be completely replayed")
        record = copy.deepcopy(failed.report)
        record.update(status="rebound-base-J-started", revision=1)
        self.rebound_records.append(record)
        started = time.monotonic()
        try:
            self.assert_context(failed.x)
            self.evaluate(self.vector(failed.x))
            self.fine_decision(failed.x)
            base, J, groups, tols = self.linear_rows(self.vector(failed.x))
            require_current_layout(self, failed)
            primary = selected_model(self, failed.x, base, J, groups, tols, trust, cfg)
            validate_rebuilt_primary(failed.original_primary, primary, failed)
            record.update(
                scalar_primary_signature_before_complete_factory=
                    primary.information["radius_independent_model_sha256"],
                new_all_selected_base_sha256=array_digest(np.asarray(base)),
                new_all_selected_J_sha256=array_digest(np.asarray(J)),
                new_all_selected_groups_sha256=array_digest(np.asarray(groups)),
                new_all_selected_tolerances_sha256=array_digest(np.asarray(tols)),
                status="rebound-base-J-ready")
            model = _detached_rebound_factory(self, primary, record)
            model.oracle.set_post_primary_phase()
            record["rebound_oracle_prediction_phase"] = "actual-total-step-prediction"
            record["no_primary_LP_is_solved_for_this_rebound_model"] = True
            # Both selected and complete factories extend the primary signature.
            # Bind only after their final update, exactly as for an original primary.
            binding = model_binding(primary, failed.x,
                                    failed.report["base_physical_state_sha256"],
                                    failed.new_versions)
            record["rebound_model_binding"] = copy.deepcopy(binding)
            rows = _frozen(np.concatenate([
                v.rows.reshape(-1)[ids] for v, ids in zip(failed.views, failed.new_ids)]))
            result = ReboundContext(primary, model, _frozen(base), _frozen(J),
                                    _frozen(groups, np.int64), _frozen(tols),
                                    failed.new_versions, binding, failed, rows, record)
            self.rebound_models.append(result)
            record.update(status="rebound-context-ready",
                          rebound_context_index=len(self.rebound_models)-1,
                          both_actual_y_residual_rows_sha256=array_digest(rows),
                          original_primary_registry_count=len(self.complete_models))
            self._wall()
            return result
        except Exception as error:
            record.update(status="rebound-construction-failed",
                          error={"type": type(error).__name__, "message": str(error)})
            raise
        finally:
            record["rebind_started_work_seconds"] = time.monotonic()-started

    def snapshot(self):
        result = super().snapshot()
        result["expanded_pool_same_trial_SOC_definition"] = definition()
        result["original_bank_replay"] = copy.deepcopy(self.initial_bank_replay)
        result["expanded_pool_rebound_records"] = copy.deepcopy(self.rebound_records)
        result["rebound_complete_models"] = [
            {"model_number": q.failed.model_number, "revision": 1,
             "binding_sha256": q.affine.binding_sha256,
             "model_binding": copy.deepcopy(q.binding),
             "complete_report": q.affine.complete_report()}
            for q in self.rebound_models]
        return result


def rebound_budget(context, cfg):
    from frame_entry_tail_height_blocks import predicted_slack
    scalar0 = float(context.primary.information["initial_selected_and_constant_metric_slack"])
    scalar1 = float(predicted_slack(context.primary, context.failed.step))
    full0 = float(context.affine.rho0)
    full1 = float(context.affine.slack(context.failed.step))
    retention = float(Q(cfg["SOC_predicted_descent_retention_exact"]))
    values = [scalar0, scalar1, full0, full1, retention]
    finite = bool(np.all(np.isfinite(values)))
    floor = float(cfg["linear_model_improvement_floor"])
    ok = finite and scalar0-scalar1 > floor and full0-full1 > floor
    scalar_rhs = scalar0-retention*(scalar0-scalar1) if finite else None
    full_rhs = full0-retention*(full0-full1) if finite else None
    result = {
        "schema": POLICY+"-same-actual-d-budget",
        "new_scalar_initial_slack": scalar0, "new_scalar_slack_at_actual_d": scalar1,
        "new_full_initial_slack": full0, "new_full_slack_at_actual_d": full1,
        "scalar_gain": scalar0-scalar1 if finite else None,
        "full_gain": full0-full1 if finite else None,
        "finite_and_both_original_positive_gain_gates": ok,
        "original_scalar_SOC_rhs": scalar_rhs,
        "hypothetical_full_SOC_rhs_not_used": full_rhs,
        "scalar_rhs_not_above_full_rhs_in_reported_floats":
            bool(scalar_rhs <= full_rhs) if finite else None,
        "no_old_primary_LP_auxiliary_used": True,
        "rebound_complete_model_binding_sha256": context.affine.binding_sha256,
        "actual_y_minus_x_array_sha256": array_digest(context.failed.step),
        "SOC_RHS_source": "original build_correction on new selected IDs and actual d",
    }
    context.record["budget"] = result
    return result


def charged_solver_call(ledger, cfg, progress, wall, remaining_seconds, invoke):
    """The callback is the sole actual solver call; charge before it can throw."""
    wall()
    if ledger["linear_program_invocation_count"] >= int(cfg["max_linear_models"]):
        progress.update(LP_invoked=False, proposal_rejected_before_LP="original shared LP budget")
        return None
    remaining = float(remaining_seconds())
    if not np.isfinite(remaining) or remaining <= 0:
        raise EvaluationBudgetReached("original active time exhausted before rebound SOC")
    limit = min(float(cfg["linear_program_seconds"]), remaining)
    ledger["linear_program_invocation_count"] += 1
    ledger["correction_LP_invocation_count"] += 1
    progress.update(LP_invoked=True,
                    shared_LP_ordinal=ledger["linear_program_invocation_count"],
                    LP_started_before_solver_call=True, time_limit_seconds=limit)
    started = time.monotonic()
    try:
        return invoke(limit)
    except Exception as error:
        progress["solver_error"] = {"type": type(error).__name__, "message": str(error)}
        raise
    finally:
        progress["elapsed_seconds"] = time.monotonic()-started


def attach_rebound_reports(result, objective):
    """Called AFTER the original primary-only attach, so wrong inherited rho0 is replaced."""
    result["expanded_pool_same_trial_SOC_definition"] = definition()
    result["original_bank_replay"] = copy.deepcopy(objective.initial_bank_replay)
    result["expanded_pool_rebound_records"] = copy.deepcopy(objective.rebound_records)
    index = {}
    for context in objective.rebound_models:
        key = (context.failed.model_number, 1)
        if key in index:
            raise ArithmeticError("more than one rebound per original primary model")
        index[key] = context
    for model in result.get("solver", {}).get("models", []):
        for correction in model.get("corrections", []):
            revision = correction.get("expanded_pool_rebound_revision")
            if revision is None:
                continue
            key = (int(model["number"]), int(revision))
            context = index.get(key)
            if context is None or correction.get("rebound_model_binding") != context.binding:
                raise ArithmeticError("rebound correction lost its exact model registry")
            lp = correction["linear_program"]
            comparison = lp.setdefault("same_step_scalar_and_affine_budget_comparison", {})
            inherited = comparison.setdefault("inherited_primary_attach_metadata", {})
            for name in ("selected_initial_slack_retained", "full_initial_slack_retained",
                         "affine_model_scope"):
                if name in comparison:
                    inherited[name] = comparison[name]
            comparison.update(
                affine_model_scope="rebound complete original two grids at the same actual y-x",
                selected_initial_slack_retained=float(context.affine.rho0_selected),
                full_initial_slack_retained=float(context.affine.rho0),
                rebound_complete_model_binding_sha256=context.affine.binding_sha256,
                original_scalar_RHS_was_not_replaced_by_a_new_full_model_RHS=True,
                original_primary_metadata_not_used_for_this_correction=True)
            correction["rebound_complete_original_grid_model"] = context.affine.complete_report()
    for model in result.get("solver", {}).get("models", []):
        diagnostic = model.get("accepted_rebound_SOC_base_total_step_diagnostic")
        if isinstance(diagnostic, dict):
            old = diagnostic.pop("no_extra_geometry_J_LP_or_value_call", None)
            diagnostic.setdefault("inherited_frozen_scope_labels", {})[
                "no_extra_geometry_J_LP_or_value_call"] = old
            diagnostic.update(
                no_extra_ordinary_geometry_LP_or_physical_value_call=True,
                directional_JVP_costs_reported_in_the_explicit_rebound_oracle=True,
                not_a_same_layout_SOC_hold_witness=True)
    result["complete_original_grid_oracle_progress"] = [
        oracle.report() for oracle in objective.complete_oracles]
    result["primary_and_rebound_report_mapping_is_explicit"] = True
    result["solver"].setdefault("inherited_scope_labels", {})["method_before_rebound"] = result["solver"]["method"]
    result["solver"]["method"] = POLICY
    return result



def solve_rebound_correction(primary,actual_full,p,cfg,ledger,*,progress,wall,remaining_seconds):
    """Original mapped159 SOC mathematics; only a before-solver ledger hook is new."""
    report=progress
    report.update(LP_invoked=False, schema=POLICY+"-original-arrays-charged-SOC")
    wall()
    model,info=build_correction(primary,actual_full,p,
        physical_margin_retention_exact=cfg['SOC_physical_margin_retention_exact'],
        predicted_descent_retention_exact=cfg['SOC_predicted_descent_retention_exact'],
        correction_relative_radius_exact=cfg['SOC_maximum_correction_relative_to_proposed_step_exact'],
        strip_floor_exact=cfg['strip_proposal_floor_exact'],curvature_floor_exact=cfg['curvature_proposal_floor_exact'],
        improvement_floor=cfg['linear_model_improvement_floor'])
    report.update({'initial_metric_slack':info['initial_metric_slack'],
        'primary_predicted_metric_slack':info['primary_predicted_metric_slack'],
        'primary_predicted_slack_improvement':info['primary_predicted_improvement'],
        'primary_box_normalized_step_infinity_norm':info['primary_norms']['physical_infinity'],
        'primary_block_normalized_step_infinity_norm':info['primary_norms']['common_body_radius_norm'],
        'rho_out':info['rho_out'],'residual_source':'actual same y on both complete grids',
        'Jacobian_source':'last accepted x; original IDs and159 independent parameter columns',
        'constant_cap_and_external_hard_not_restored_by_false_zero_J_rows':True})
    if model is None:
        report['proposal_rejected_before_LP']=info['status'];return None,report
    trial=model.active_trial_values
    report.update(metric_slack_budget=info['metric_slack_budget'],
        maximum_box_normalized_correction_infinity_norm=model.radius,
        body_correction_radius=info['body_correction_radius'],tail_correction_radius=info['tail_correction_radius'],
        height_correction_radius=info['height_correction_radius'],
        rows=len(model.b),variables=len(model.c),matrix_bytes=model.A.nbytes,
        hard_margin_retention=float(Q(cfg['SOC_physical_margin_retention_exact'])),
        metric_budget_applied_to_actual_trial_rows_plus_old_Jacobian_correction=True,
        selected_metric_actual_minus_primary_linear_minimum=float(np.min(
            (trial-primary.active_values-primary.active_J@p)[primary.active_groups<2])))
    report.update(inherited_proposal_floor_report(primary,cfg,trial=trial))
    started=time.monotonic();scaled=scale_mapped_correction(model)
    report['SOC_reversible_scaling']=scaled.definition()
    report['SOC_scaling_prepare_seconds']=time.monotonic()-started
    report['SOC_solver_tolerances_are_in_scaled_units_not_original_residual_units']=True
    r=charged_solver_call(ledger,cfg,report,wall,remaining_seconds,
        lambda limit:linprog(scaled.objective,A_ub=scaled.A,b_ub=scaled.b,
            bounds=list(zip(scaled.lower,scaled.upper)),method='highs',
            options={'primal_feasibility_tolerance':cfg['linear_program_primal_tolerance'],
                'dual_feasibility_tolerance':cfg['linear_program_dual_tolerance'],
                'time_limit':limit}))
    if r is None:return None,report
    report.update(success=bool(r.success),status=int(r.status),message=str(r.message),nit=int(r.nit))
    report['SOC_solver_returned_finite_primal']=bool(r.x is not None and np.asarray(r.x).shape==scaled.objective.shape
        and np.all(np.isfinite(r.x)))
    report['SOC_original_unit_dual_diagnostics']=scaled.original_dual_diagnostics(r,model.original_row_group_labels)
    if not report['SOC_solver_returned_finite_primal']:return None,report
    x=scaled.to_original(r.x);w=correction_independent_step(model,x);res=model.residual(x)
    report['SOC_original_and_scaled_residuals']=scaled.original_residuals(r.x)
    linear=primary.active_values+primary.active_J@p;Jw=primary.active_J@w
    hard=primary.active_groups>=2;soft=~hard;outside=primary.information['rho_out']
    norms=primary.subspace.step_norms(w,primary.width);physical=primary.subspace.M@w
    report.update(maximum_linear_row_violation=res['maximum_original_linear_row_violation'],
        maximum_linear_bound_violation=res['maximum_original_linear_bound_violation'],
        maximum_absolute_correction=float(np.max(abs(physical))),correction_l2=float(np.linalg.norm(physical)),
        correction_box_normalized_infinity_norm=norms['physical_infinity'],
        correction_box_normalized_l1_norm=norms['physical_L1'],
        correction_block_normalized_infinity_norm=norms['common_body_radius_norm'],
        corrected_predicted_metric_slack=max(outside,0.,float(np.max(-(linear+Jw)[soft]))),
        corrected_actual_trial_linear_metric_slack=max(outside,0.,float(np.max(-(trial+Jw)[soft]))),
        basepoint_prediction_slack_is_only_for_parabolic_linear_bookkeeping=True,
        minimum_corrected_linear_hard_margin=float(np.min(trial[hard]+Jw[hard])) if np.any(hard) else None,
        corrected_affine_cap_margin=primary.information['cap_invariant']['affine_margin'])
    report.update(inherited_proposal_floor_report(primary,cfg,trial=trial,linear=trial+Jw))
    if not r.success or max(res['maximum_original_linear_row_violation'],res['maximum_original_linear_bound_violation'])>cfg['linear_model_residual_limit']:
        report['proposal_rejected_before_geometry']='SOC status or original-unit residual';return None,report
    return w,report


