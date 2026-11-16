#!/usr/bin/env python3
"""One different primary proposal using the last unspent direct-task LP.

This module neither reconstructs the unknown old proposed vector nor resets
any ledger. It only builds additional legal unit-ball supports at the exactly
restored MODEL28 and calls the frozen repaired-incumbent solver once.
All scientific and developer execution belongs to the public Actions lane.
"""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import math
import time
import numpy as np

from frame_height_null_coordinates import digest
from frame_entry_body_subspace import array_digest
from frame_metric_affine_spectral_model import N
from frame_metric_norm_direction_memory import (
    support_row, unit_ball_direction, solve_remembered_primary)
from frame_metric_direct_reference_epoch import SupplementalCompleteModel
from frame_metric_height159_soc_hold import model_binding

POLICY = "same159-paid-terminal-attainer-final-LP-slot-v1"
SOURCE = {
    "run_id": 43780594182, "job_id": 133016656592,
    "source_sha": "a0d71ea94446f0fcf64d1f69e4dbadd5910204ba",
    "raw_log_sha256": "ee418c296ab6af5cac1066a19811cc0393c53f7b576244b151183e09f1fe62c9",
    "MODEL28_json_plus_LF_sha256": "4177aefe47ee4675b4f4fc4ceadf3fcb300b0fe7c36450acef6aab5331cf78f1",
    "COMPLETE_json_plus_LF_sha256": "c9731defe5d0bc80b6f8aaad43e9a834a45e2a53618668c05ec8e06f93ce8c90",
}
SOURCE_MODEL = 28
SOURCE_TOTAL_LPS = 63
SOURCE_PRIMARY_LPS = 62
SOURCE_SOC_LPS = 1
SOURCE_VALUES = 58
SOURCE_SCIENCE_SECONDS = 257.595331213
LABELS = ("coarse", "fine")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def finite_number(value):
    return (not isinstance(value, (bool, np.bool_))
            and isinstance(value, (int, float, np.integer, np.floating))
            and math.isfinite(float(value)))


def definition():
    return {
        "policy": POLICY, "source": dict(SOURCE),
        "old_started_LPs": SOURCE_TOTAL_LPS, "old_shared_values": SOURCE_VALUES,
        "old_cumulative_scientific_seconds": SOURCE_SCIENCE_SECONDS,
        "unchanged_limits": {"LP": 64, "value": 160, "science_seconds": 1800,
                             "single_LP_seconds": 10},
        "maximum_new_primary_LPs": 1, "remaining_SOC_slots_after_new_primary": 0,
        "no_old_primary_or_development_reexecution": True,
        "old512_and_original4_supports_retained": True,
        "paid_attainers_choose_legal_normals_not_unknown_old_step_or_contact": True,
        "new_cut_required_before_any_new_LP": True,
        "full_original_affine_candidate_repair_and_actual_gates_retained": True,
        "new_restore_and_row_J_costs_use_remaining_original_task_clock": True,
        "no_stationarity_or_improvement_guarantee": True,
    }


def _ledger_guard(cfg, ledger):
    for name, value in (("max_linear_models", 64), ("max_physical_evaluations", 160),
                        ("max_seconds", 1800)):
        require(type(cfg.get(name)) is int and cfg[name] == value,
                "original direct-task resource limit differs: "+name)
    require(finite_number(cfg.get("linear_program_seconds"))
            and cfg["linear_program_seconds"] == 10,
            "original direct-task single-LP time limit differs")
    for name, value in (("linear_program_invocation_count", SOURCE_TOTAL_LPS),
                        ("primary_LP_invocation_count", SOURCE_PRIMARY_LPS),
                        ("correction_LP_invocation_count", SOURCE_SOC_LPS)):
        require(type(ledger.get(name)) is int and ledger[name] == value,
                "the actual inherited ledger is required: "+name)
    require(ledger.get("nonlinear_minimize_invocation_count", 0) == 0,
            "unexpected nonlinear optimizer calls")


def validate_release(source_model, cfg, ledger):
    """Only the already-paid unfinished terminal branch is eligible."""
    _ledger_guard(cfg, ledger)
    require(isinstance(source_model, dict) and source_model.get("number") == SOURCE_MODEL,
            "the original terminal MODEL28 is required")
    require(source_model.get("result") == "no-evaluated-affine-spectral-improvement",
            "source terminal result differs")
    require(source_model.get("trials") == [] and source_model.get("corrections") == [],
            "a source trial or correction makes this release ineligible")
    lp = source_model["linear_program"]
    require(lp.get("returned_candidate") is False
            and lp.get("returned_epigraph_gap_met") is False
            and lp.get("returned_inexact_cut_model") is True
            and lp.get("proposal_rejected_before_geometry") ==
                "no-evaluated-affine-model-improvement-above-original-floor",
            "source did not stop before geometry with an inexact non-improving candidate")
    require(lp.get("status") == "new-task-pair-allocation-primary-ceiling-reached"
            and lp.get("new_task_shared_LP_limit_exhausted") is False,
            "source stopped for another reason")
    require(lp.get("inner_call_count") == 1 and len(lp.get("inner_LPs", [])) == 1,
            "source last scoped primary must contain exactly one paid LP")
    event = lp["inner_LPs"][0]
    require(event.get("shared_LP_ordinal") == SOURCE_TOTAL_LPS
            and event.get("status") == "evaluated-affine-candidate"
            and event.get("gap_met") is False,
            "source paid candidate event differs")
    for key in ("raw_epigraph_gap", "gap_tolerance", "evaluated_model_improvement"):
        require(finite_number(event.get(key)), "finite source "+key+" required")
    require(event["gap_tolerance"] >= 0
            and event["raw_epigraph_gap"] > event["gap_tolerance"],
            "a completed epigraph model cannot use this release")
    floor = cfg.get("linear_model_improvement_floor")
    require(finite_number(floor) and floor >= 0
            and finite_number(lp.get("predicted_slack_improvement"))
            and lp["predicted_slack_improvement"] <= floor,
            "source already has an improving returned candidate")
    a = lp["primary_SOC_pair_allocation"]
    require(a.get("shared_LP_limit") == 64
            and a.get("started_shared_LPs_before_primary") == 62
            and a.get("remaining_shared_LPs_before_primary") == 2
            and a.get("primary_inner_calls_granted") == 1
            and a.get("scoped_primary_absolute_ceiling") == 63
            and a.get("charged_primary_LPs") == 1
            and a.get("remaining_shared_LPs_after_primary") == 1
            and a.get("source_cfg_unchanged") is True,
            "source allocation or closed scope differs")
    require(len(lp.get("cut_rounds", [])) == 1
            and lp["cut_rounds"][0].get("rows") == 516
            and lp.get("initial_rebuilt_memory_rows") == 516
            and lp.get("total_new_cut_rows") == 516,
            "this release only covers the source initial512+4/no-separation-cut branch")
    return {
        "schema": POLICY+"-eligibility", "eligible": True,
        "source_model_number": SOURCE_MODEL, "source_paid_LP_ordinal": SOURCE_TOTAL_LPS,
        "source_original_allocation": copy.deepcopy(a),
        "released_shared_LP_ordinal": 64, "maximum_new_primary_LPs": 1,
        "unused_SOC_reservation_is_explicitly_reassigned": True,
        "new_candidate_has_no_SOC_budget": True,
        "source_trial_and_correction_counts": [0, 0],
        "old_terminal_status_remains_in_the_source_record": True,
    }


def _same_current_model(primary, model, source_model, cfg):
    require(isinstance(model, SupplementalCompleteModel) and primary is model.primary,
            "the actual current complete512+4 model is required")
    model.oracle._assert_context()
    old = source_model["complete_model"]
    require(model.binding_sha256 == old["summary"]["binding_sha256"]
            and digest(model.binding) == model.binding_sha256,
            "restored complete two-factory binding differs")
    require(model.oracle.binding_sha256 == old["oracle"]["binding_sha256"]
            and digest(model.oracle.binding) == model.oracle.binding_sha256,
            "restored full-grid oracle center differs")
    guard = source_model["curvature_defect_guard"]
    require(digest(cfg) == guard["source_configuration_sha256"]
            and float(primary.trust) == float(source_model["trust_before_model"])
            and str(Q.from_float(float(primary.trust))) == guard["B_binary64_exact"],
            "source cfg, B or exact B changed")
    actual = model_binding(
        primary, primary.state, source_model["linearized_at_physical_sha256"],
        (source_model["coarse_pool_version"], source_model["fine_pool_version"]))
    require(actual == source_model["SOC_hold_model_binding"]
            == guard["final_model_binding"]
            == source_model["ordinary_covered_context"]["final_model_binding"],
            "same physical point, M, widths, ordered pools or final signature differs")
    for name, expected in guard["unchanged_array_sha256"].items():
        require(array_digest(np.asarray(getattr(primary, name))) == expected,
                "restored primary array differs: "+name)
    require(array_digest(np.asarray(primary.b)) == guard["guarded_rhs_sha256"]
            and array_digest(np.asarray(primary.targets)) == guard["guarded_targets_sha256"],
            "frozen guarded RHS or targets differ")
    current_guard = primary.information["curvature_defect_guard"]
    for key in ("frozen_learning_state_sha256", "frozen_coefficients",
                "guarded_scalar_signature_before_observable_factories",
                "guarded_rhs_sha256", "guarded_targets_sha256", "B_binary64_exact"):
        require(current_guard[key] == guard[key], "restored frozen guard differs: "+key)
    require(model.bank.state_digest() == old["norm_direction_memory"]["state_sha256"]
            and len(model.bank.entries) == 512,
            "the complete original ordered512 bank changed")
    require(len(model.supplemental_normals) == 4
            and digest(model.supplemental_normals) ==
                old["supplemental_paid_normals"]["source_sha256"],
            "the original four supplemental supports changed")
    require(model.summary()["epsilon_exact"] == old["summary"]["epsilon_exact"]
            and model.summary()["target_exact"] == old["summary"]["target_exact"],
            "original metric epsilon or target differs")
    return {
        "complete_model_binding_sha256": model.binding_sha256,
        "oracle_center_binding_sha256": model.oracle.binding_sha256,
        "final_model_binding": actual,
        "source_cfg_sha256": digest(cfg),
        "frozen_guarded_rhs_sha256": guard["guarded_rhs_sha256"],
        "frozen_guarded_targets_sha256": guard["guarded_targets_sha256"],
        "frozen_learning_state_sha256": guard["frozen_learning_state_sha256"],
        "bank_state_sha256": model.bank.state_digest(),
        "source_initial_support_count": 516,
    }


def append_distinct_supports(A0, b0, Anew, bnew):
    """Keep the whole old sequence, including duplicates; append distinct new rows."""
    A0, b0, Anew, bnew = map(lambda x: np.asarray(x, float), (A0, b0, Anew, bnew))
    require(A0.ndim == Anew.ndim == 2 and A0.shape[1] == Anew.shape[1]
            and b0.shape == (len(A0),) and bnew.shape == (len(Anew),),
            "matching support matrix/row shapes required")
    require(all(np.all(np.isfinite(x)) for x in (A0, b0, Anew, bnew)),
            "nonfinite original or new support")
    seen = {array_digest(np.r_[a, b]) for a, b in zip(A0, b0)}
    kept, duplicate = [], []
    for j, (a, b) in enumerate(zip(Anew, bnew)):
        key = array_digest(np.r_[a, b])
        if key in seen:
            duplicate.append(j)
        else:
            kept.append(j)
            seen.add(key)
    extra = np.asarray(kept, np.int64)
    A, b = np.vstack([A0, Anew[extra]]), np.r_[b0, bnew[extra]]
    require(np.array_equal(A[:len(b0)], A0) and np.array_equal(b[:len(b0)], b0),
            "an old support was changed or deleted")
    return A, b, {
        "original_rows_retained_in_order": len(b0), "new_input_rows": len(bnew),
        "distinct_new_rows": len(kept), "kept_new_indices": kept,
        "duplicate_new_indices": duplicate, "combined_rows": len(b),
        "original_A_sha256": array_digest(A0), "original_b_sha256": array_digest(b0),
        "combined_A_sha256": array_digest(A), "combined_b_sha256": array_digest(b),
        "same_row_different_normal_is_not_a_replacement": True,
    }


class TerminalPaidSupportModel(SupplementalCompleteModel):
    """Same full model; only its initial supporting-row bundle is extended."""
    def __init__(self, original, A, b, record):
        self.__dict__.update(original.__dict__)
        self.terminal_paid_A = np.array(A, float, copy=True)
        self.terminal_paid_b = np.array(b, float, copy=True)
        self.terminal_paid_A.setflags(write=False)
        self.terminal_paid_b.setflags(write=False)
        self.terminal_paid_support_record = copy.deepcopy(record)
        self.terminal_initial_support_reads = 0
        self.new_candidate_step_record = None

    def evaluated(self, step):
        result = super().evaluated(step)
        p = np.asarray(step, float)
        self.new_candidate_step_record = {
            "exact_binary64_independent_step": [str(Q.from_float(float(x))) for x in p],
            "array_sha256": array_digest(p),
            "original_oracle_direction_sha256": result["complete_maxima"]["direction_sha256"],
            "source_is_only_the_new_candidate_not_the_unknown_paid_step": True,
            "no_additional_evaluation_or_JVP": True}
        return result

    def initial_cuts(self):
        self.oracle._assert_context()
        require(array_digest(self.terminal_paid_A) ==
                    self.terminal_paid_support_record["append"]["combined_A_sha256"]
                and array_digest(self.terminal_paid_b) ==
                    self.terminal_paid_support_record["append"]["combined_b_sha256"],
                "prepared terminal supports changed")
        self.terminal_initial_support_reads += 1
        return (self.terminal_paid_A, self.terminal_paid_b,
                copy.deepcopy(self.terminal_paid_support_record))

    def complete_report(self):
        result = super().complete_report()
        result["terminal_paid_supports"] = copy.deepcopy(self.terminal_paid_support_record)
        result["terminal_paid_supports"]["prepared_bundle_reads"] = self.terminal_initial_support_reads
        result["terminal_new_candidate_step"] = copy.deepcopy(self.new_candidate_step_record)
        return result


def prepare_terminal_support_model(primary, model, source_model, cfg, ledger, *, wall, progress):
    """Called once after necessary restoration; no LP and no old-direction JVP."""
    require(callable(wall) and isinstance(progress, dict), "wall/progress callbacks required")
    eligibility = validate_release(source_model, cfg, ledger)
    progress["terminal_slot_release"] = copy.deepcopy(eligibility)
    progress["terminal_slot_release"]["status"] = "checking-restored-current-model"
    started = time.monotonic()
    try:
        wall()
        binding = _same_current_model(primary, model, source_model, cfg)
        events = source_model["complete_model"]["oracle"]["direction_events"]
        require(isinstance(events, list) and len(events) == 1,
                "exactly one paid terminal direction event required")
        event = events[0]
        require(event.get("ordinal") == 1 and event.get("status") == "complete"
                and event.get("phase") == "primary-inner"
                and event.get("center_binding_sha256") == model.oracle.binding_sha256,
                "paid attainer event is not the same complete original center")
        attainers = event["attainers"]
        require(isinstance(attainers, list) and len(attainers) == 4,
                "the four paid complete-grid branch attainers are required")
        A0, b0, base_record = model.initial_cuts()
        old_record = source_model["linear_program"]["cut_rounds"][0]
        require(len(b0) == 516 and array_digest(A0) == old_record["A_sha256"]
                and array_digest(b0) == old_record["b_sha256"],
                "the restored original512+4 supporting rows differ")
        bank_before = model.bank.state_digest()
        rows, rhs, witnesses, seen = [], [], [], set()
        tolerance = float(cfg["value_Jacobian_replay_relative_tolerance"])
        require(math.isfinite(tolerance) and tolerance >= 0, "finite original replay tolerance required")
        for index, attainer in enumerate(attainers):
            wall()
            tag = attainer["original_row"]
            require(isinstance(tag, dict) and tag.get("grid") in LABELS
                    and type(tag.get("flat_row_id")) is int
                    and type(tag.get("group")) is int and tag["group"] in (0, 1),
                    "original integer metric row tag required")
            label, flat, group = tag["grid"], tag["flat_row_id"], tag["group"]
            grid = model.oracle.grids[label]
            require(grid.coordinate(flat) == tag, "paid original row does not belong to this grid")
            branch = (label, group)
            require(branch not in seen, "duplicate complete-grid branch")
            seen.add(branch)
            for key in ("affine_e", "affine_f", "base_e", "base_f"):
                require(finite_number(attainer.get(key)), "finite paid "+key+" required")
            pos = model.selected_point_lookup.get((label, flat % grid.point_count))
            if pos is None:
                row = model.oracle.original_row(label, flat)
                row_source = "new-current-metric-row-J"
            else:
                selected = model.selected_model
                row = {"e": selected.e[pos], "f": selected.f[pos],
                       "de": selected.de[pos], "df": selected.df[pos]}
                row_source = "existing-current-selected-observables"
            error = max(abs(float(row["e"])-attainer["base_e"]),
                        abs(float(row["f"])-attainer["base_f"]))
            scale = max(1., abs(float(row["e"])), abs(float(row["f"])),
                        abs(attainer["base_e"]), abs(attainer["base_f"]))
            require(math.isfinite(error) and error <= tolerance*scale,
                    "paid attainer base e/f differs from restored current center")
            normal, adjustments = unit_ball_direction(
                attainer["affine_e"], attainer["affine_f"], model.epsilon)
            a, b = support_row(row, normal, group, model.epsilon, model.target, primary.step_scale)
            rows.append(a); rhs.append(b)
            witnesses.append({
                "paid_attainer_index": index, "original_row": copy.deepcopy(tag),
                "normal_exact_binary64": [str(Q.from_float(float(x))) for x in normal],
                "normal_squared_norm_exact": str(sum((Q.from_float(float(x))**2
                                                     for x in normal), Q())),
                "inward_adjustments": adjustments, "row_source": row_source,
                "base_e_f_max_absolute_difference": error,
                "source_direction_sha256": event["direction_sha256"],
                "unknown_paid_step_not_reconstructed": True,
                "old_step_contact_not_claimed": True})
        require(seen == {(label, group) for label in LABELS for group in (0, 1)},
                "all four paid branches required")
        require(model.bank.state_digest() == bank_before,
                "building supplemental supports must not replace old bank normals")
        A, b, appended = append_distinct_supports(
            A0, b0, np.asarray(rows, float).reshape(4, N+2), np.asarray(rhs, float))
        record = {
            "schema": POLICY+"-prepared-supports", "rows": len(b),
            "binding": binding, "append": appended,
            "original512_plus4_record": copy.deepcopy(base_record),
            "paid_direction_sha256": event["direction_sha256"],
            "paid_attainers_sha256": digest(attainers),
            "witnesses": witnesses,
            "same_original_affine_objective_and_frozen_guard": True,
            "no_old_direction_or_old_primary_reexecution": True,
            "no_old_numeric_A_b_restored_without_current_rebuild": True,
            "floating_assembly_is_not_an_interval_certificate": True}
        progress["terminal_slot_release"].update(
            status="new-supports-prepared" if appended["distinct_new_rows"] else "no-distinct-new-support",
            current_binding=copy.deepcopy(binding), append=copy.deepcopy(appended))
        wall()
        if not appended["distinct_new_rows"]:
            progress.update(status="terminal-release-no-distinct-new-support",
                            returned_candidate=False, inner_LPs=[], inner_call_count=0,
                            proposal_rejected_before_geometry="no-new-paid-support-no-new-LP")
            return None
        return TerminalPaidSupportModel(model, A, b, record)
    except Exception as error:
        progress["terminal_slot_release"].update(
            status="terminal-support-preparation-raised",
            error={"type": type(error).__name__, "message": str(error)})
        raise
    finally:
        progress["terminal_slot_release"]["preparation_seconds"] = time.monotonic()-started


def _call_final_slot(cfg, ledger, progress, invoke):
    """Small accounting boundary, also used by isolated new stub fixtures."""
    _ledger_guard(cfg, ledger)
    require(callable(invoke) and isinstance(progress, dict), "explicit current call/progress required")
    release = progress.get("terminal_slot_release")
    require(isinstance(release, dict) and release.get("eligible") is True
            and release.get("status") == "new-supports-prepared"
            and release.get("append", {}).get("distinct_new_rows", 0) > 0,
            "a fresh distinct-support preparation is required before consuming the last slot")
    cfg_sha = digest(cfg)
    before = {key: ledger[key] for key in (
        "linear_program_invocation_count", "primary_LP_invocation_count", "correction_LP_invocation_count")}
    release.update(status="last-slot-call-entered", source_cfg_sha256=cfg_sha,
                   before_ledger=copy.deepcopy(before), new_SOC_opportunities=0)
    try:
        return invoke()
    except Exception as error:
        release["error"] = {"type": type(error).__name__, "message": str(error)}
        raise
    finally:
        after = {key: ledger[key] for key in before}
        total = after["linear_program_invocation_count"]-before["linear_program_invocation_count"]
        primary = after["primary_LP_invocation_count"]-before["primary_LP_invocation_count"]
        correction = after["correction_LP_invocation_count"]-before["correction_LP_invocation_count"]
        release.update(after_ledger=after, new_started_primary_LPs=primary,
                       new_started_SOC_LPs=correction, original_shared_slots_left=64-after["linear_program_invocation_count"],
                       source_cfg_unchanged=digest(cfg) == cfg_sha,
                       status="last-slot-call-ended",
                       actual_trial_acceptance_not_implied=True)
        require(total in (0, 1) and primary == total and correction == 0,
                "one-call release changed the original ledger incorrectly")
        require(digest(cfg) == cfg_sha, "last-slot release changed source cfg")


def solve_terminal_last_slot(primary, model, cfg, ledger, *, wall, remaining_seconds, progress):
    """No allocation reset: frozen solver sees the actual shared63/64 ledger."""
    require(isinstance(model, TerminalPaidSupportModel) and model.primary is primary,
            "prepared terminal paid-support model required")
    require(callable(wall) and callable(remaining_seconds), "original budget callbacks required")
    require(model.terminal_initial_support_reads == 0, "prepared bundle was already consumed")
    before_binding = model.binding_sha256

    def invoke():
        wall()
        require(model.binding_sha256 == before_binding, "complete model binding changed before LP")
        return solve_remembered_primary(
            primary, model, cfg, ledger, progress=progress, wall=wall,
            remaining_seconds=remaining_seconds)

    result = _call_final_slot(cfg, ledger, progress, invoke)
    progress["terminal_slot_release"].update(
        returned_candidate=progress.get("returned_candidate", False),
        returned_inexact_cut_model=progress.get("returned_inexact_cut_model"),
        inherited_solver_status=progress.get("status"),
        original_candidate_repair_used=True,
        no_SOC_budget_after_a_started_final_primary=ledger["linear_program_invocation_count"] == 64)
    return result
