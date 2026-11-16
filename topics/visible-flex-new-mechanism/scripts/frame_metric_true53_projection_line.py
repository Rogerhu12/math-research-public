#!/usr/bin/env python3
"""One legal-interval full affine spectral line after a new true53 direction.

Only the already charged final direction's e/f/de/df arrays are used. The
physical alpha-zero baseline is never replaced by a positive legal endpoint.
"""
from __future__ import annotations

import copy
from fractions import Fraction as Q
import hashlib
import math
from pathlib import Path
import time

from frame_height_null_coordinates import digest
from frame_entry_body_subspace import array_digest
from frame_metric_p32_line_envelope import (
    LineMethodLedger, ScalarLineEnvelope)
from frame_metric_complete_maximin_projection import (
    POLICY, ProjectionLedger, require)

SEARCH_CEILING = 62
INTERVAL_WIDTH_STOP = 2.0**-40


def implementation_hashes():
    from frame_metric_complete_maximin_projection import implementation_hashes as core_hashes
    out = core_hashes()
    p = Path(__file__)
    out[p.name] = hashlib.sha256(p.read_bytes()).hexdigest()
    return out


class _SharedLineLedger(LineMethodLedger):
    """Only a protocol adapter: all original query work debits the new shared clock."""
    def __init__(self, owner):
        require(isinstance(owner, ProjectionLedger), "the actual new projection ledger required")
        self.owner = owner
        super().__init__(owner.started, science_limit=600, query_limit=64)

    def check(self):
        return self.owner.check()

    def charge_session(self):
        self.scalar_sessions = self.owner.charge("scalar_sessions")

    def charge_query(self, event):
        self.query_count = self.owner.charge("scalar_queries")
        event.update(query_number=self.query_count, charged_before_evaluation=True,
                     shared_projection_scientific_clock=True)
        self.query_events.append(event)

    def charge_build(self, event):
        raise RuntimeError("the final projection direction arrays must be reused, not rebuilt")

    def charge_grid(self):
        raise RuntimeError("the final projection direction arrays must be reused, not rebuilt")

    def charge_trial(self):
        raise RuntimeError("actual trial debit belongs to the explicitly bound new outer")

    def charge_actual_value(self, label, physical_sha):
        raise RuntimeError("actual geometry debit belongs to the explicitly bound new outer")

    def report(self):
        return {
            "schema": POLICY+"-shared-line-ledger",
            "scalar_sessions": self.scalar_sessions, "queries": self.query_count,
            "shared_projection_ledger": self.owner.report(),
            "no_old_p32_or_cone_or_LP_account_reopened": True,
        }


class GuardedLineEnvelope(ScalarLineEnvelope):
    def __init__(self, model, handle, ledger):
        require(handle["qualified"], "a rounded fully separated positive direction required")
        scan = handle["scan"]
        require(scan["model_binding_sha256"] == model.binding_sha256
                and array_digest(handle["direction"]) == scan["direction_sha256"],
                "the line must use the final actual rounded direction cache")
        self.physical_interval = copy.deepcopy(
            handle["interval"]["original_numeric_tolerance_interval"])
        require(self.physical_interval["nonempty"], "no scalar solve on an empty legal interval")
        self.model = model
        self.owner = ledger
        self.true_zero_baseline_from_new_complete_first_order_base = float(model.phi0)
        binding = {
            "schema": POLICY+"-legal-line",
            "complete_first_order_model_binding_sha256": model.binding_sha256,
            "original_direction_sha256": scan["direction_sha256"],
            "source_physical_state_sha256": model.binding["physical_state_sha256"],
            "physical_alpha_interval": copy.deepcopy(self.physical_interval),
            "original_target_interval": copy.deepcopy(
                handle["interval"]["exact_original_target_interval"]),
            "configuration_sha256": model.cfg_sha256,
            "epsilon": model.epsilon, "target": model.target,
            "base_phi": model.phi0,
            "arrays_reused_from_last_qualified_direction_without_JVP": True,
            "array_sha256": {label: {key: array_digest(value) for key, value in row.items()}
                             for label, row in scan["arrays"].items()}}
        super().__init__(
            scan["arrays"], epsilon=model.epsilon, target=model.target,
            ledger=_SharedLineLedger(ledger), binding=binding, row_grids=model.grids)

    def full_record(self):
        record = super().full_record()
        record["inherited_scalar_cache_implementation_schema"] = record["schema"]
        record["schema"] = POLICY+"-complete-final-direction-line-cache"
        record["cache_coefficients_reused_no_second_direction_build"] = True
        record["source_true_zero_baseline"] = self.true_zero_baseline_from_new_complete_first_order_base
        return record

    def query(self, alpha, *, purpose="legal-interval-search"):
        require(type(purpose) is str and purpose in (
            "physical-zero-baseline", "legal-interval-search", "untried-actual-fallback"),
            "explicit physical query purpose required")
        alpha = float(alpha)
        if purpose == "physical-zero-baseline":
            require(alpha == 0., "baseline means original physical zero only")
        else:
            require(self.physical_interval["lower"] <= alpha <= self.physical_interval["upper"],
                    "new scalar query is outside the original guard-compatible interval")
        record = super().query(alpha)
        record["inherited_scalar_query_schema"] = record["schema"]
        record["schema"] = POLICY+"-whole-line-query"
        record["purpose"] = purpose
        record["raw_metric_phi"] = record["phi"]
        # The exact old target is an explicit constant branch of the new model.
        if record["raw_metric_phi"] < self.target:
            record["phi"] = self.target
            record["floating_left_slope"] = record["floating_right_slope"] = 0.
            record["constant_original_target_is_active"] = True
        elif record["raw_metric_phi"] == self.target:
            record["floating_left_slope"] = min(0., record["floating_left_slope"])
            record["floating_right_slope"] = max(0., record["floating_right_slope"])
            record["constant_original_target_is_active"] = True
        else:
            record["constant_original_target_is_active"] = False
        record["physical_alpha_exact_binary64"] = str(Q.from_float(alpha))
        record["original_alpha_zero_baseline"] = self.true_zero_baseline_from_new_complete_first_order_base
        record["observed_model_gain_from_true_zero"] = (
            self.true_zero_baseline_from_new_complete_first_order_base-record["phi"])
        record["legal_interval_has_not_replaced_the_zero_baseline"] = True
        return record


def run_guarded_line(model, final_handle, ledger, *, publish_cache,
                     emit_query=None, progress=None):
    """Return best record or None, JSON-safe progress, and same-process envelope."""
    require(isinstance(ledger, ProjectionLedger) and callable(publish_cache),
            "actual shared ledger and a once-only full-cache stdout publisher required")
    progress = {} if progress is None else progress
    require(isinstance(progress, dict) and not progress, "fresh legal-line report sink required")
    interval = final_handle["interval"]["original_numeric_tolerance_interval"]
    progress.update(
        schema=POLICY+"-legal-line-session", status="not-started",
        interval=copy.deepcopy(interval), base_phi=float(model.phi0),
        original_target_interval=copy.deepcopy(final_handle["interval"]["exact_original_target_interval"]),
        complete_query_record_numbers=[],
        no_geometry_JVP_selected_J_or_old_backend_inside_scalar_search=True)
    if not final_handle["qualified"] or not interval["nonempty"]:
        progress["status"] = "no-qualified-direction-or-empty-original-legal-interval"
        return None, progress, None
    ledger.check()
    envelope = GuardedLineEnvelope(model, final_handle, ledger)
    # This is one plain original stdout record, not API chunking or a Git blob.
    receipt = publish_cache(envelope.full_record())
    envelope.mark_full_cache_published(receipt)
    progress["line_cache_receipt"] = copy.deepcopy(receipt)
    ledger.check()
    envelope.ledger.charge_session()
    start = time.monotonic()
    progress["status"] = "started"
    observed = {}

    def query(alpha, purpose="legal-interval-search"):
        record = envelope.query(alpha, purpose=purpose)
        progress["complete_query_record_numbers"].append(record["query_number"])
        observed[float(alpha).hex()] = record
        if emit_query is not None:
            emit_query(record)
        ledger.check()
        return record

    best = None
    try:
        zero = query(0., "physical-zero-baseline")
        require(abs(zero["phi"]-model.phi0)
                <= float(model.cfg["value_Jacobian_replay_relative_tolerance"])*max(1., abs(model.phi0)),
                "same cached physical-zero spectral baseline changed")
        left, right = float(interval["lower"]), float(interval["upper"])
        progress["physical_zero_query_number"] = zero["query_number"]
        if left == right:
            item = observed.get(left.hex()) or query(left)
            candidates = [item]
            stopping = "one-real-allowed-point-not-an-interval-optimization"
        else:
            endpoint_left = observed.get(left.hex()) or query(left)
            endpoint_right = observed.get(right.hex()) or query(right)
            ratio = (math.sqrt(5.)-1.)/2.
            a, b = right-ratio*(right-left), left+ratio*(right-left)
            ra, rb = query(a), query(b)
            stopping = "declared-search-cap-two-real-fallback-queries-reserved"
            while ledger.counts["scalar_queries"] < SEARCH_CEILING:
                ledger.check()
                if right-left <= INTERVAL_WIDTH_STOP:
                    stopping = "declared-physical-alpha-width"
                    break
                if ra["phi"] <= rb["phi"]:
                    right, b, rb = b, a, ra
                    new_a = right-ratio*(right-left)
                    if new_a in (left, right, a, b):
                        stopping = "binary64-physical-alpha-no-progress"
                        break
                    a, ra = new_a, query(new_a)
                else:
                    left, a, ra = a, b, rb
                    new_b = left+ratio*(right-left)
                    if new_b in (left, right, a, b):
                        stopping = "binary64-physical-alpha-no-progress"
                        break
                    b, rb = new_b, query(new_b)
            candidates = [
                row for row in envelope.records if row.get("status") == "complete"
                and row["purpose"] != "physical-zero-baseline"
                and interval["lower"] <= row["alpha"] <= interval["upper"]]
        chosen = min(candidates, key=lambda row: (row["phi"], row["alpha"])) if candidates else None
        gain = float(model.phi0-chosen["phi"]) if chosen is not None else None
        qualified = bool(chosen is not None and chosen["alpha"] > 0
                         and gain > float(model.cfg["linear_model_improvement_floor"]))
        if qualified:
            best = chosen
        progress.update(
            status="complete", stopping_reason=stopping,
            final_physical_alpha_bracket=[left, right],
            selected_query_number=chosen["query_number"] if chosen is not None else None,
            selected_physical_alpha=chosen["alpha"] if chosen is not None else None,
            selected_complete_phi=chosen["phi"] if chosen is not None else None,
            observed_gain_from_true_zero=gain,
            eligible_untried_model_descent=qualified,
            actual_candidate_original_hard_and_exact163_box_still_required=True,
            scalar_queries_started=ledger.counts["scalar_queries"],
            remaining_shared_query_slots=ledger.limits["scalar_queries"]-ledger.counts["scalar_queries"],
            exact_scalar_optimality_or_no_descent_not_claimed=True)
        ledger.check()
    except Exception as error:
        progress.update(status="raised", error={
            "type": type(error).__name__, "message": str(error)})
        raise
    finally:
        progress["elapsed_seconds"] = time.monotonic()-start
        progress["all_query_records"] = copy.deepcopy(envelope.records)
        progress["shared_ledger_at_return"] = ledger.report()
    return best, progress, envelope
