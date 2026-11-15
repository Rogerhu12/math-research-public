#!/usr/bin/env python3
"""Observed group8 defects change only the next ordinary primary proposal.

All development/scientific execution is confined to the public Actions lane.
The two coefficients are empirical, not error bounds. Frozen actual gates,
SOC RHS, source configuration, original Jacobians and solver budgets remain.
"""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import hashlib
import math
from pathlib import Path
import time
import numpy as np

from frame_height_null_coordinates import digest
from frame_entry_body_subspace import array_digest
from frame_metric_entry_tail_height159 import selected_model as frozen_selected_model
from frame_metric_norm_direction_memory import RememberingCompleteObjective
import frame_metric_covered_soft_growth as covered
import frame_metric_soc_pair_reservation as allocation
import frame_metric_expanded_layout_hold as inherited_hold
import frame_metric_expanded_pool_soc as expanded
import frame_metric_height159_soc_hold as old_hold

POLICY = "same159-observed-curvature-defect-primary-guard-v1"
N = 159
CHECKPOINT_BANK_ENTRIES = 375
LABELS = ("coarse", "fine")
GROUP = 8
PAID_SOURCE = {
    "run_id": "43762868037", "job_id": "132961344492",
    "source_sha": "4f1365300b70831550d544df119d738b2531eff5",
}


def implementation_hashes():
    result = covered.implementation_hashes()
    p = Path(__file__)
    result[p.name] = hashlib.sha256(p.read_bytes()).hexdigest()
    return result


def definition():
    return {
        "policy": POLICY, "group": GROUP, "grids": list(LABELS),
        "observation": "min_i(actual_i(y)-base_i(x)-J_i(x)*(actual_y-actual_x))",
        "normalizer": "max(body,8*tail,height/4) from original M, physical widths, actual159 displacement",
        "learning": "maximum nonnegative observed loss divided by actual common-body norm squared",
        "primary_target": "max(original_target, original_curvature_floor + gamma_grid*B**2)",
        "only_original_selected_in_domain_group8_rows_change": True,
        "ordinary_primary_only_rebound_and_SOC_RHS_are_frozen": True,
        "same_model_coefficients_and_targets_frozen_until_next_primary": True,
        "first_full_ordinary_trial_only": True,
        "not_a_cross_center_or_whole_grid_error_bound": True,
        "no_clipping_of_original_signed_defect_record": True,
        "no_extra_LP_J_JVP_geometry_or_value_call": True,
        "source_cfg_and_norm_memory_context_unchanged": True,
        "zero_J_rows_are_not_removed": True,
        "guard_infeasibility_uses_original_paid_failure_and_shrink": True,
        "no_free_unguarded_resolve": True,
        "legacy_signature_key_is_B_dependent_for_this_new_primary": True,
        "radius_mapped_witness_not_invoked_or_claimed": True,
        "initial_checkpoint_bank_entries": CHECKPOINT_BANK_ENTRIES,
        "paid_initial_source": dict(PAID_SOURCE),
    }


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def _number(value):
    return (not isinstance(value, (bool, np.bool_))
            and isinstance(value, (int, float, np.integer, np.floating))
            and math.isfinite(float(value)))


def _sha(value, name):
    _require(isinstance(value, str) and len(value) == 64
             and all(c in "0123456789abcdef" for c in value), name+" must be SHA256")
    return value


def _vector(value, name):
    a = np.asarray(value, float)
    _require(a.shape == (N,) and np.all(np.isfinite(a)), "finite actual159 "+name+" required")
    return a


def decode_exact159(values):
    _require(isinstance(values, list) and len(values) == N
             and all(isinstance(v, str) for v in values), "159 exact binary64 strings required")
    out = []
    for value in values:
        q = Q(value)
        z = float(q)
        _require(math.isfinite(z) and Q.from_float(z) == q, "stored coordinate is not exact binary64")
        out.append(z)
    return np.asarray(out, float)


def _immutable_context(objective):
    width, _, _ = objective.subspace.scales(objective.physical_lower, objective.physical_upper)
    return {
        "source_cfg_sha256": digest(objective.cfg),
        "coordinate_definition_sha256": objective.subspace.coordinates.definition_sha256,
        "subspace_definition_sha256": objective.subspace.definition_sha256,
        "physical_map_array_sha256": array_digest(objective.subspace.M),
        "original_physical_width_array_sha256": array_digest(width),
        "curvature_scale_exact": str(Q(objective.cfg["curvature_scale_exact"])),
        "fixed_zeta_binary64_exact": str(Q.from_float(float(objective.fixed_zeta))),
        "fixed_hard_curvature_cap_exact": str(Q(objective.cfg["fixed_hard_curvature_cap_exact"])),
        "grids": {g.label: {"definition_sha256": g.definition_sha256,
                            "point_count": g.point_count} for g in objective.row_grids},
        "norm_memory_context_sha256": digest(objective.direction_bank.context),
        "units": "unchanged original scaled PSD determinant group8 row units",
    }, np.asarray(width, float)


def _bound_source(objective, source_model, trial, base, context):
    """Old pool identity is checked against OLD context, never against the new pool."""
    immutable, width = _immutable_context(objective)
    _require(context.get("available") is True, "paid final factory context is unavailable")
    old = source_model["SOC_hold_model_binding"]
    _require(old == context.get("final_model_binding"),
             "historical hold/context final bindings differ")
    for key in ("coordinate_definition_sha256", "subspace_definition_sha256",
                "physical_map_array_sha256", "original_physical_width_array_sha256"):
        _require(old.get(key) == immutable[key], "immutable historical "+key+" differs")
    _require(context.get("source_cfg_sha256") == immutable["source_cfg_sha256"],
             "historical source configuration differs")
    _require(old.get("coarse_fine_pool_versions") == context.get("old_pool_versions"),
             "historical pool versions disagree within the old sample")
    _require(isinstance(context.get("old_ID_counts"), list)
             and len(context["old_ID_counts"]) == 2
             and all(type(v) is int and v >= 0 for v in context["old_ID_counts"]),
             "historical selected row counts required")
    # The signature binds the historical row mapping/J. Rebuilding either is forbidden.
    _sha(old["active_original_row_mapping_sha256"], "historical active row map")
    _sha(old["radius_independent_model_sha256"], "historical final model")
    _sha(context["complete_model_binding_sha256"], "historical complete model")
    _require(trial.get("kind") == "primary-metric-short-step" and trial.get("alpha_exact") == "1",
             "only the first complete ordinary primary sample is allowed")
    _require(type(source_model.get("number")) is int
             and type(base.get("accepted_index")) is int
             and source_model.get("linearized_at_accepted_index") == base["accepted_index"],
             "actual source accepted-index link differs")
    x = decode_exact159(base["exact_binary64_independent_coordinates"])
    y = decode_exact159(trial["exact_binary64_independent_coordinates"])
    base_sha = digest(objective.problem.identity(x))
    y_sha = digest(objective.problem.identity(y))
    _require(base_sha == base["physical_state_sha256"]
             == source_model["linearized_at_physical_sha256"]
             == context["base_physical_state_sha256"] == old["base_physical_state_sha256"],
             "actual historical x physical identities differ")
    _require(y_sha == trial["physical_state_sha256"], "actual historical y physical identity differs")
    _require(array_digest(x) == old["base_independent_array_sha256"]
             == context["base_independent_array_sha256"],
             "actual historical x array identity differs")
    _require(_number(source_model.get("trust_before_model"))
             and source_model["trust_before_model"] > 0, "positive source model B required")
    return x, y, width, immutable


def _read_defects(diagnostic):
    _require(diagnostic.get("reference_kind") == "accepted-basepoint-plus-J-total-step"
             and diagnostic.get("same_cached_state_no_additional_geometry_or_value_call") is True,
             "original same-actual-step selected-row diagnostic required")
    grids = diagnostic.get("grids")
    _require(isinstance(grids, dict) and set(grids) <= set(LABELS)
             and "coarse" in grids, "original coarse/fine diagnostic labels required")
    _require(("fine" in grids) == (diagnostic.get("fine_actual_available") is True),
             "fine availability and diagnostic rows differ")
    result = {}
    for label in LABELS:
        if label not in grids:
            continue
        rows = grids[label].get("groups")
        _require(isinstance(rows, list), "original group diagnostic list required")
        selected = [r for r in rows if type(r.get("group")) is int and r["group"] == GROUP]
        _require(len(selected) <= 1, "duplicate group8 source summary")
        if not selected:
            continue
        row = selected[0]
        _require(type(row.get("selected_count")) is int and row["selected_count"] > 0,
                 "positive original group8 selected count required")
        _require(_number(row.get("minimum_actual_minus_prediction")),
                 "finite original signed group8 defect required")
        result[label] = copy.deepcopy(row)
    return result


class CurvatureDefectMemory:
    """Only two empirical coefficients; each pending observation retains provenance."""
    def __init__(self, context):
        self.context = copy.deepcopy(context)
        self.coefficients = {label: 0. for label in LABELS}
        self.maximizers = {label: None for label in LABELS}
        self.events, self.pending, self.commits = [], [], []

    def state_record(self):
        state = {"context": copy.deepcopy(self.context),
                 "coefficients": dict(self.coefficients),
                 "coefficient_binary64_exact": {k: str(Q.from_float(v))
                                                for k, v in self.coefficients.items()},
                 "maximizing_event_indices": copy.deepcopy(self.maximizers)}
        return dict(state, state_sha256=digest(state))

    def queue(self, *, actual_step_norm, defect_rows, source, norm_record):
        event = {
            "index": len(self.events), "source": copy.deepcopy(source),
            "actual_common_body_norm": float(actual_step_norm) if _number(actual_step_norm) else None,
            "actual_physical_norm_record": copy.deepcopy(norm_record),
            "original_signed_group_summaries": copy.deepcopy(defect_rows),
            "coefficients_observed": {}, "status": "pending",
            "committed": False, "first_consuming_model_number": None,
        }
        b = actual_step_norm
        if not _number(b) or b <= 0 or not _number(float(b)*float(b)) or float(b)*float(b) <= 0:
            event.update(status="not-learned-zero-or-nonfinite-actual-norm",
                         pending=False)
        else:
            for label, original in defect_rows.items():
                _require(label in LABELS, "unknown curvature memory bucket")
                delta = float(original["minimum_actual_minus_prediction"])
                observed = max(0., -delta)/(float(b)*float(b))
                if not math.isfinite(observed):
                    event.update(status="not-learned-nonfinite-normalized-defect", pending=False)
                    event["coefficients_observed"] = {}
                    break
                event["coefficients_observed"][label] = observed
            else:
                event["pending"] = bool(event["coefficients_observed"])
                if not event["pending"]:
                    event["status"] = "not-learned-no-observed-group8"
        self.events.append(event)
        if event.get("pending"):
            self.pending.append(event["index"])
        return copy.deepcopy(event)

    def commit(self, reason, next_model_number=None):
        before = self.state_record()
        indices = list(self.pending)
        changes = []
        for index in indices:
            event = self.events[index]
            for label, value in event["coefficients_observed"].items():
                if value > self.coefficients[label]:
                    changes.append({"grid": label, "old": self.coefficients[label],
                                    "new": value, "source_event_index": index})
                    self.coefficients[label] = value
                    self.maximizers[label] = index
            event.update(status="committed", pending=False, committed=True,
                         commit_reason=reason, first_consuming_model_number=next_model_number)
        self.pending = []
        record = {"reason": reason, "committed_event_indices": indices,
                  "next_primary_model_number": next_model_number, "changes": changes,
                  "before_sha256": before["state_sha256"],
                  "after_sha256": self.state_record()["state_sha256"]}
        if indices:
            self.commits.append(record)
        return copy.deepcopy(record)

    def checkpoint(self):
        return {
            "schema": POLICY+"-learning-checkpoint",
            **self.state_record(), "events": copy.deepcopy(self.events),
            "pending_event_indices": list(self.pending),
            "commits": copy.deepcopy(self.commits),
            "empirical_not_a_nonlinear_error_certificate": True,
        }


def apply_primary_guard(primary, frozen_learning, cfg):
    """Only the two group8 target/RHS subsets change before the two factories."""
    values = np.asarray(primary.active_values, float)
    groups = np.asarray(primary.active_groups)
    targets = np.asarray(primary.targets, float)
    _require(values.ndim == 1 and groups.shape == values.shape
             and groups.dtype.kind in "iu" and targets.shape == values.shape,
             "original finite active primary layout required")
    _require(np.all(np.isfinite(values)) and np.all(np.isfinite(targets))
             and np.asarray(primary.active_J).shape == (len(values), N),
             "original primary values/J/targets required")
    rows = primary.information["active_original_rows"]
    _require(len(rows) == len(values), "original active row tags required")
    B = float(primary.trust)
    floor = float(Q(cfg["curvature_proposal_floor_exact"]))
    _require(math.isfinite(B) and B > 0 and floor >= 0 and math.isfinite(floor),
             "positive original B and finite original floor required")
    coeff = frozen_learning["coefficients"]
    _require(set(coeff) == set(LABELS)
             and all(_number(v) and v >= 0 for v in coeff.values()),
             "two finite nonnegative frozen coefficients required")
    unchanged = {name: array_digest(np.asarray(getattr(primary, name)))
                 for name in ("A", "c", "lower", "upper", "active_values", "active_J",
                              "active_groups", "active_tolerances", "state", "step_scale")}
    before_b = np.asarray(primary.b, float).copy()
    old_targets = targets.copy()
    new_targets = targets.copy()
    per_grid = {}
    for label in LABELS:
        positions = [i for i, tag in enumerate(rows) if tag.get("grid") == label and groups[i] == GROUP]
        mask = np.asarray(positions, np.int64)
        for i in positions:
            tag = rows[i]
            _require(type(tag.get("group")) is int and tag["group"] == GROUP
                     and type(tag.get("flat_row_id")) is int,
                     "original integer group8 tags required")
        allowance = float(coeff[label])*B*B
        _require(math.isfinite(allowance), "nonfinite empirical primary allowance")
        if len(mask):
            new_targets[mask] = np.maximum(old_targets[mask], floor+allowance)
        changed = [i for i in positions if new_targets[i] != old_targets[i]]
        per_grid[label] = {
            "observed_coefficient": float(coeff[label]), "B_squared_allowance": allowance,
            "eligible_original_row_count": len(positions), "modified_row_count": len(changed),
            "modified_original_rows": [copy.deepcopy(rows[i]) for i in changed],
            "maximum_target_increment": float(np.max(new_targets[mask]-old_targets[mask], initial=0.)),
            "zero_J_rows_kept": sum(bool(np.all(np.asarray(primary.active_J)[i] == 0)) for i in positions),
        }
    _require(np.all(np.isfinite(new_targets)), "nonfinite guarded primary targets")
    new_b = before_b.copy()
    affected = np.flatnonzero(new_targets != old_targets)
    new_b[affected] = values[affected]-new_targets[affected]
    _require(np.all(np.isfinite(new_b)), "nonfinite guarded primary RHS")
    primary.b = new_b
    primary.targets = new_targets
    for name, old_hash in unchanged.items():
        _require(array_digest(np.asarray(getattr(primary, name))) == old_hash,
                 "guard changed frozen primary "+name)
    scalar = primary.information["radius_independent_model_sha256"]
    record = {
        "schema": POLICY+"-ordinary-primary-guard",
        "frozen_learning_state_sha256": frozen_learning["state_sha256"],
        "frozen_coefficients": copy.deepcopy(coeff),
        "B_binary64_exact": str(Q.from_float(B)), "B": B,
        "original_floor_exact": str(Q(cfg["curvature_proposal_floor_exact"])),
        "inherited_unguarded_scalar_signature": scalar,
        "before_targets_sha256": array_digest(old_targets),
        "guarded_targets_sha256": array_digest(new_targets),
        "before_rhs_sha256": array_digest(before_b), "guarded_rhs_sha256": array_digest(new_b),
        "unchanged_array_sha256": unchanged, "per_grid": per_grid,
        "modified_row_count": len(affected), "original_SOC_RHS_unchanged": True,
        "only_pre_factory_ordinary_primary_rhs_and_targets_changed": True,
        "legacy_signature_key_is_B_dependent": True,
        "radius_mapped_witness_not_used": True,
    }
    signature = digest({"policy": POLICY, "unguarded_scalar": scalar,
                        "learning": frozen_learning["state_sha256"],
                        "B": record["B_binary64_exact"],
                        "targets": record["guarded_targets_sha256"], "rhs": record["guarded_rhs_sha256"]})
    primary.information["curvature_defect_guard"] = copy.deepcopy(record)
    primary.information["radius_independent_model_sha256"] = signature
    primary.information["guarded_B_dependent_scalar_model_sha256"] = signature
    record["guarded_scalar_signature_before_observable_factories"] = signature
    primary.information["curvature_defect_guard"] = copy.deepcopy(record)
    return record


class CurvatureDefectGuardObjective(covered.CoveredSoftGrowthObjective):
    """Direct375 constructor; never calls the frozen hardcoded59 constructor."""
    def __init__(self, *args, initial_bank_context, initial_bank_entries,
                 expected_initial_bank_state_sha256, expected_initial_bank_entries,
                 curvature_defect_guard_policy, initial_curvature_defect_samples,
                 initial_direction_records=(), **kwargs):
        _require(curvature_defect_guard_policy == POLICY, "explicit empirical curvature policy required")
        _require(type(expected_initial_bank_entries) is int
                 and expected_initial_bank_entries == CHECKPOINT_BANK_ENTRIES,
                 "current completed375-entry bank required")
        _require(not initial_direction_records, "direct checkpoint cannot replay norm events")
        _require(not any(k in kwargs for k in ("covered_soft_growth_policy", "expanded_pool_policy",
                    "expanded_layout_hold_policy", "soc_pair_reservation_policy")),
                 "inherited policies are fixed internally")
        self.curvature_defect_guard_policy = POLICY
        self.covered_soft_growth_policy = covered.POLICY
        self.soc_pair_reservation_policy = allocation.POLICY
        self.expanded_layout_hold_policy = inherited_hold.POLICY
        self.expanded_pool_policy = expanded.POLICY
        self.expected_initial_bank_state_sha256 = expected_initial_bank_state_sha256
        self.expected_initial_bank_entries = expected_initial_bank_entries
        self.initial_bank_replay = {
            "schema": POLICY+"-initial-checkpoint-bank-bound",
            "passed": False, "status": "pending-first-complete-model-no-LP-yet"}
        self.rebound_models, self.rebound_records = [], []
        self.ordinary_covered_contexts = []
        self.covered_growth_bookkeeping = {
            "context_registrations": 0, "context_seconds": 0.,
            "controller_updates": 0, "controller_seconds": 0.}
        self.curvature_guard_records = []
        self.curvature_guard_bookkeeping = {
            "primary_builds": 0, "primary_bookkeeping_seconds": 0.,
            "sample_attempts": 0, "sample_bookkeeping_seconds": 0.,
            "new_LP_J_JVP_geometry_or_value_calls": 0}
        RememberingCompleteObjective.__init__(self, *args, initial_direction_records=(), **kwargs)
        allocation.primary_allocation(self.cfg, {"linear_program_invocation_count": 0})
        self.checkpoint_bank_input = inherited_hold.restore_checkpoint_bank(
            self.direction_bank, initial_bank_context, initial_bank_entries,
            expected_initial_bank_state_sha256, expected_initial_bank_entries)
        self.unchanged_source_cfg_sha256 = digest(self.cfg)
        immutable, _ = _immutable_context(self)
        self.curvature_defect_memory = CurvatureDefectMemory(immutable)
        _require(isinstance(initial_curvature_defect_samples, list)
                 and [s.get("source_model", {}).get("number") for s in initial_curvature_defect_samples] == [2, 6],
                 "exactly the two paid first-primary source samples2/6 required")
        self.paid_curvature_sample_receipts = []
        for sample in initial_curvature_defect_samples:
            self.paid_curvature_sample_receipts.append(self._import_paid_sample(sample))
        self.curvature_defect_memory.commit("paid-initial-samples-before-first-new-primary", 1)
        self.paid_curvature_sample_receipts = [
            copy.deepcopy(self.curvature_defect_memory.events[item["index"]])
            for item in self.paid_curvature_sample_receipts]
        self.initial_curvature_learning_state = self.curvature_defect_memory.state_record()
        self.evaluation_definition["expanded_pool_same_trial_SOC"] = expanded.definition()
        self.evaluation_definition["covered_expanded_pool_SOC_radius_retention"] = inherited_hold.definition()
        self.evaluation_definition["primary_SOC_pair_allocation"] = allocation.definition()
        self.evaluation_definition["covered_soft_ordinary_growth"] = covered.definition()
        self.evaluation_definition["curvature_defect_primary_guard"] = definition()
        self.evaluation_definition["expected_initial_bank"] = {
            "state_sha256": expected_initial_bank_state_sha256, "entries": expected_initial_bank_entries,
            "source": "complete ordered375 current-best checkpoint, no event replay"}
        self.evaluation_sha256 = digest(self.evaluation_definition)

    def _import_paid_sample(self, sample):
        _require(sample.get("schema") == POLICY+"-paid-first-primary-sample", "paid sample schema differs")
        source = sample.get("source", {})
        _require(all(source.get(k) == v for k, v in PAID_SOURCE.items()), "paid sample source differs")
        _sha(source.get("log_sha256"), "paid log")
        _sha(source.get("complete_record_sha256"), "paid complete record")
        x, y, width, immutable = _bound_source(
            self, sample["source_model"], sample["source_trial"],
            sample["source_base_point"], sample["source_final_factory_context"])
        _require(immutable == self.curvature_defect_memory.context, "paid sample immutable context differs")
        diagnostic = sample["source_trial"]["curvature_nonlinear_defect_diagnostic"]
        _require(diagnostic.get("fine_actual_available") is True, "both paid original grids required")
        rows = _read_defects(diagnostic)
        _require(set(rows) == set(LABELS), "both paid group8 summaries required")
        norm = self.subspace.step_norms(y-x, width)
        provenance = {
            "kind": "paid-first-primary", "source": copy.deepcopy(source),
            "model_number": sample["source_model"]["number"],
            "source_model_B": sample["source_model"]["trust_before_model"],
            "source_sample_sha256": digest(sample),
            "actual_x_array_sha256": array_digest(x), "actual_y_array_sha256": array_digest(y),
            "actual_y_minus_x_sha256": array_digest(y-x),
            "old_final_model_binding": copy.deepcopy(sample["source_model"]["SOC_hold_model_binding"]),
            "old_context": copy.deepcopy(sample["source_final_factory_context"]),
            "historical_pool_identity_only_compared_inside_historical_sample": True,
            "no_old_J_geometry_LP_or_value_reconstruction": True,
        }
        return self.curvature_defect_memory.queue(
            actual_step_norm=norm["common_body_radius_norm"], defect_rows=rows,
            source=provenance, norm_record=norm)

    def guarded_primary(self, state, base, J, groups, tols, trust, cfg, model_number):
        started = time.monotonic()
        try:
            self._wall()
            _require(digest(self.cfg) == self.unchanged_source_cfg_sha256, "source cfg mutated")
            context, _ = _immutable_context(self)
            _require(context == self.curvature_defect_memory.context, "curvature learning context changed")
            commit = self.curvature_defect_memory.commit("next-ordinary-primary", int(model_number))
            frozen = self.curvature_defect_memory.state_record()
            primary = frozen_selected_model(self, state, base, J, groups, tols, trust, cfg)
            record = apply_primary_guard(primary, frozen, cfg)
            record.update(model_number=int(model_number), pending_commit_before_model=commit,
                          status="guarded-scalar-awaiting-both-observable-factories")
            self.curvature_guard_records.append(record)
            primary.information["curvature_defect_guard_record_index"] = len(self.curvature_guard_records)-1
            self.curvature_guard_bookkeeping["primary_builds"] += 1
            return primary
        finally:
            self.curvature_guard_bookkeeping["primary_bookkeeping_seconds"] += time.monotonic()-started

    def bind_guarded_primary(self, primary, complete, model):
        index = primary.information["curvature_defect_guard_record_index"]
        record = self.curvature_guard_records[index]
        _require(complete.primary is primary and primary.affine_spectral_model is complete,
                 "final original complete factory object required")
        final = old_hold.model_binding(primary, primary.state,
            digest(self.problem.identity(primary.state)),
            (self.pool_version, self.fine_pool_version))
        _require(final == model["SOC_hold_model_binding"], "post-two-factory guarded binding differs")
        record.update(status="both-observable-factories-final-bound",
                      final_model_binding=copy.deepcopy(final),
                      complete_model_binding_sha256=complete.binding_sha256,
                      source_configuration_sha256=self.unchanged_source_cfg_sha256)
        model["curvature_defect_guard"] = copy.deepcopy(record)

    def observe_first_primary_defect(self, primary, model, trial, candidate, base, J, groups, versions):
        if trial.get("kind") != "primary-metric-short-step" or trial.get("alpha_exact") != "1":
            return
        _require("curvature_defect_sample_event_index" not in model, "duplicate first-primary defect sample")
        started = time.monotonic()
        self.curvature_guard_bookkeeping["sample_attempts"] += 1
        try:
            x, y = _vector(primary.state, "x"), _vector(candidate, "y")
            _require(tuple(map(int, versions)) == (self.pool_version, self.fine_pool_version),
                     "live sample must precede pool learning")
            _require(digest(self.cfg) == self.unchanged_source_cfg_sha256, "source cfg mutated at sample")
            context = model.get("ordinary_covered_context", {})
            _require(context.get("available") is True
                     and context.get("final_model_binding") == model["SOC_hold_model_binding"],
                     "same final ordinary context required for new defect learning")
            current = old_hold.model_binding(primary, x, digest(self.problem.identity(x)), versions)
            _require(current == model["SOC_hold_model_binding"], "current primary binding changed")
            _require(context["complete_model_binding_sha256"] == primary.affine_spectral_model.binding_sha256,
                     "ordinary complete model identity changed")
            # Verify the full selected diagnostic stack maps to this active primary.
            raw_values = np.asarray(base, float)
            raw_J = np.asarray(J, float)
            raw_groups = np.asarray(groups)
            count = sum(len(s.ids) for s in primary.selections)
            _require(raw_values.shape == (count,) and raw_J.shape == (count, N)
                     and raw_groups.shape == (count,) and raw_groups.dtype.kind in "iu",
                     "same raw original selected stack required")
            masks, offset = [], 0
            for selection, pool in zip(primary.selections, (self.pool, self.fine_pool)):
                ids = covered._integer_ids(pool, "live original pool")
                _require(np.array_equal(ids, selection.ids), "old selected IDs changed before sample")
                n = len(ids)
                _require(np.array_equal(raw_groups[offset:offset+n], ids//selection.full.grid.point_count),
                         "raw diagnostic labels changed original ID groups")
                masks.extend((offset+np.flatnonzero(selection.parts["variable"])).tolist())
                offset += n
            masks = np.asarray(masks, np.int64)
            _require(np.array_equal(raw_values[masks], primary.active_values)
                     and np.array_equal(raw_J[masks], primary.active_J)
                     and np.array_equal(raw_groups[masks], primary.active_groups),
                     "raw diagnostic rows/J differ from the frozen guarded primary")
            _require(array_digest(y) == array_digest(decode_exact159(trial["exact_binary64_independent_coordinates"]))
                     and digest(self.problem.identity(y)) == trial["physical_state_sha256"],
                     "actual y differs from the stored trial")
            rows = _read_defects(trial["curvature_nonlinear_defect_diagnostic"])
            norm = self.subspace.step_norms(y-x, primary.width)
            provenance = {
                "kind": "new-run-first-primary", "model_number": model["number"],
                "actual_x_array_sha256": array_digest(x), "actual_y_array_sha256": array_digest(y),
                "actual_y_minus_x_sha256": array_digest(y-x),
                "source_model_B": float(primary.trust),
                "final_model_binding": copy.deepcopy(current),
                "complete_model_binding_sha256": primary.affine_spectral_model.binding_sha256,
                "raw_selected_values_sha256": array_digest(raw_values),
                "raw_selected_J_sha256": array_digest(raw_J),
                "original_selected_IDs_sha256": [array_digest(s.ids) for s in primary.selections],
                "same_model_learning_state_is_still_frozen": True,
                "no_new_geometry_J_JVP_LP_or_value_call": True,
            }
            event = self.curvature_defect_memory.queue(
                actual_step_norm=norm["common_body_radius_norm"], defect_rows=rows,
                source=provenance, norm_record=norm)
            model["curvature_defect_sample_event_index"] = event["index"]
            trial["curvature_defect_guard_sample"] = copy.deepcopy(event)
        finally:
            self.curvature_guard_bookkeeping["sample_bookkeeping_seconds"] += time.monotonic()-started

    def finalize_curvature_guard_learning(self):
        return self.curvature_defect_memory.commit("run-finalization-no-retroactive-model-change", None)

    def snapshot(self):
        result = super().snapshot()
        if hasattr(self, "curvature_defect_memory"):
            result["curvature_defect_guard_learning_checkpoint"] = self.curvature_defect_memory.checkpoint()
            result["curvature_defect_guard_primary_records"] = copy.deepcopy(self.curvature_guard_records)
            result["curvature_defect_guard_bookkeeping"] = copy.deepcopy(self.curvature_guard_bookkeeping)
        return result


def attach_guard_reports(result, objective):
    memory = objective.curvature_defect_memory
    for model in result.get("solver", {}).get("models", []):
        index = model.get("curvature_defect_sample_event_index")
        if index is not None:
            event = copy.deepcopy(memory.events[index])
            model["curvature_defect_sample_final_record"] = event
            for trial in model.get("trials", []):
                old = trial.get("curvature_defect_guard_sample")
                if isinstance(old, dict) and old.get("index") == index:
                    trial["curvature_defect_guard_sample"] = copy.deepcopy(event)
    records = objective.curvature_guard_records
    result["curvature_defect_guard_definition"] = definition()
    result["curvature_defect_guard_learning_checkpoint"] = memory.checkpoint()
    result["curvature_defect_guard_observation"] = {
        "paid_initial_sample_count": len(objective.paid_curvature_sample_receipts),
        "paid_initial_samples": copy.deepcopy(objective.paid_curvature_sample_receipts),
        "initial_learning_state": copy.deepcopy(objective.initial_curvature_learning_state),
        "ordinary_primary_builds": len(records),
        "models_with_modified_targets": sum(r["modified_row_count"] > 0 for r in records),
        "total_modified_target_rows_counted_per_model": sum(r["modified_row_count"] for r in records),
        "live_first_primary_sample_count": sum(e["source"]["kind"] == "new-run-first-primary" for e in memory.events),
        "completed_commit_count": len(memory.commits),
        "pending_event_count": len(memory.pending),
        "final_learning_state": memory.state_record(),
        "bookkeeping": copy.deepcopy(objective.curvature_guard_bookkeeping),
        "old_SOC_RHS_and_all_actual_gates_preserved": True,
        "no_extra_LP_J_JVP_geometry_or_value_call": True,
        "empirical_guard_not_a_continuous_or_cross_center_error_certificate": True,
        "guard_may_reduce_feasible_proposals_and_consume_original_budget": True,
    }
    return result
