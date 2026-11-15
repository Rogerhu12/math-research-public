#!/usr/bin/env python3
"""Carry unit-ball norm directions, rebuild supporting rows at each new center.

All scientific/development execution is restricted to the public Actions lane.
The bank contains original grid/row IDs and normals, never old numeric A/b.
"""
from __future__ import annotations
from collections import OrderedDict
import copy
from fractions import Fraction as Q
import hashlib
import math
from pathlib import Path
import time
import numpy as np
from frame_height_null_coordinates import digest
from frame_metric_affine_spectral_model import (
    N, MAX_INNER_PRIMARY_LPS, array_digest, frozen_solve_primary, _cut_lp, _candidate)
from frame_complete_affine_metric_oracle import CompleteGridAffineModel
from frame_metric_height159_complete_affine import (
    CompleteAffineHeight159Objective, attach_complete_model_reports)

POLICY = "same159-complete-affine-cross-center-unit-normal-memory-v1"
MAX_NORMALS = 512


def unit_ball_direction(e, f, epsilon):
    e, f, epsilon = float(e), float(f), float(epsilon)
    if not all(math.isfinite(x) for x in (e, f, epsilon)) or epsilon <= 0:
        raise ValueError("finite e/f and positive original epsilon required")
    r = math.hypot(e, 2*f, epsilon)
    n = [e/r, 2*f/r, epsilon/r]
    adjustments = 0
    while sum((Q.from_float(x)**2 for x in n), Q()) > 1:
        if adjustments >= 8:
            raise ArithmeticError("rounded direction did not enter exact binary64 unit ball")
        n = [math.nextafter(x, 0.) for x in n]
        adjustments += 1
    return tuple(n), adjustments


def support_row(row, normal, group, epsilon, target, step_scale):
    n = tuple(float(x) for x in normal)
    if len(n) != 3 or any(not math.isfinite(x) for x in n):
        raise ValueError("finite three-dimensional normal required")
    if sum((Q.from_float(x)**2 for x in n), Q()) > 1:
        raise ValueError("normal is outside the exact binary64 unit ball")
    if type(group) is not int or group not in (0, 1):
        raise ValueError("original plus/minus group required")
    pe = .5*((1. if group == 0 else -1.)+n[0])
    pf = n[1]
    de, df = np.asarray(row["de"], float), np.asarray(row["df"], float)
    scale = np.asarray(step_scale, float)
    if de.shape != (N,) or df.shape != (N,) or scale.shape != (N,):
        raise ValueError("current original159 derivative/scale shape differs")
    gradient = pe*de+pf*df
    intercept = pe*float(row["e"])+pf*float(row["f"])+.5*n[2]*float(epsilon)
    A = np.zeros(N+2)
    A[:N], A[N] = gradient*scale, -1.
    b = float(target)-intercept
    if not np.all(np.isfinite(A)) or not math.isfinite(b):
        raise FloatingPointError("nonfinite rebuilt norm support")
    return A, b


def memory_context(model):
    oracle = model.oracle
    return {
        "coordinate_definition_sha256": oracle.binding["coordinate_definition_sha256"],
        "height_reference_definition_sha256": oracle.binding["height_reference_definition_sha256"],
        "factorization_definition_sha256": oracle.binding["factorization_definition_sha256"],
        "epsilon_binary64_exact": str(Q.from_float(float(model.epsilon))),
        "original_grids": {
            label: oracle.grid_binding[label]["rational_grid_definition_sha256"]
            for label in ("coarse", "fine")},
        "original_point_counts": {
            label: int(oracle.grids[label].point_count) for label in ("coarse", "fine")}}


class NormDirectionBank:
    def __init__(self, maximum=MAX_NORMALS):
        if type(maximum) is not int or maximum != MAX_NORMALS:
            raise ValueError("declared512-direction bank required")
        self.maximum, self.entries, self.context = maximum, OrderedDict(), None
        self.insertions = self.evictions = self.rounding_adjustments = 0
        self.rebuild_events = []

    def bind(self, model):
        current = memory_context(model)
        if self.context is None:
            self.context = current
        elif current != self.context:
            raise ValueError("memory crosses an original grid/coordinate/reference binding")

    def remember(self, model, tag, e, f, source_binding=None):
        self.bind(model)
        label, flat, group = tag["grid"], int(tag["flat_row_id"]), int(tag["group"])
        count = self.context["original_point_counts"].get(label)
        if count is None or flat < 0 or flat >= 2*count or group != flat//count:
            raise ValueError("original soft row ID and branch disagree")
        normal, adjusted = unit_ball_direction(e, f, model.epsilon)
        key = (label, flat)
        self.entries.pop(key, None)
        self.entries[key] = {"original_row": copy.deepcopy(tag), "normal": normal,
                             "source_center_binding_sha256": source_binding or model.binding_sha256}
        self.insertions += 1
        self.rounding_adjustments += adjusted
        while len(self.entries) > self.maximum:
            self.entries.popitem(last=False)
            self.evictions += 1

    def rebuilt(self, model):
        self.bind(model)
        started = time.monotonic()
        rows, rhs, ids = [], [], []
        selected, new_rows = 0, 0
        for item in tuple(self.entries.values()):
            model.oracle.wall()
            tag = item["original_row"]
            label, flat = tag["grid"], int(tag["flat_row_id"])
            count = self.context["original_point_counts"][label]
            point_key = (label, flat % count)
            pos = model.selected_point_lookup.get(point_key)
            if pos is None:
                row = model.oracle.original_row(label, flat)
                new_rows += 1
            else:
                original = model.selected_model
                row = {"e": original.e[pos], "f": original.f[pos],
                       "de": original.de[pos], "df": original.df[pos]}
                selected += 1
            A, b = support_row(row, item["normal"], flat//count,
                               model.epsilon, model.target, model.primary.step_scale)
            rows.append(A)
            rhs.append(b)
            ids.append(copy.deepcopy(tag))
        A = np.asarray(rows, float).reshape(len(rows), N+2)
        b = np.asarray(rhs, float)
        record = {
            "schema": POLICY+"-rebuilt-inherited-support",
            "rows": len(rhs), "original_rows": ids,
            "bank_state_sha256": self.state_digest(),
            "current_center_binding_sha256": model.binding_sha256,
            "A_sha256": array_digest(A), "b_sha256": array_digest(b),
            "selected_current_derivatives_reused": selected,
            "original_current_row_derivative_requests": new_rows,
            "all_normal_squared_norms_at_most_one_as_exact_binary64_rationals": True,
            "old_numeric_A_or_b_reused": False,
            "elapsed_seconds_in_original_active_clock": time.monotonic()-started,
            "floating_cut_assembly_not_an_interval_certificate": True}
        self.rebuild_events.append(copy.deepcopy(record))
        return A, b, record

    def state_digest(self):
        return digest({"context": self.context, "entries": list(self.entries.values())})

    def report(self):
        return {"schema": POLICY+"-bank", "maximum": self.maximum,
                "entries": len(self.entries), "state_sha256": self.state_digest(),
                "insertions": self.insertions, "evictions": self.evictions,
                "normal_inward_binary64_adjustments": self.rounding_adjustments,
                "selection": "latest direction per original grid/branch row, least recently inserted evicted",
                "stored_old_numeric_A_b": False,
                "rebuild_events": copy.deepcopy(self.rebuild_events)}


class RememberingCompleteModel(CompleteGridAffineModel):
    def __init__(self, complete, bank):
        if not isinstance(complete, CompleteGridAffineModel):
            raise ValueError("original complete model required")
        self.__dict__.update(complete.__dict__)
        self.bank = bank
        self.bank.bind(self)

    def cuts(self, step, function_indices):
        A, b, record = super().cuts(step, function_indices)
        # The inherited cut path has already evaluated these same base-model rows.
        observed = self.oracle.evaluate(step)
        for index in np.asarray(function_indices, np.int64):
            if int(index) < self.selected_count:
                pos = int(index)
                original = self.selected_model
                e = original.e[pos]+float(original.de[pos]@step)
                f = original.f[pos]+float(original.df[pos]@step)
                tag = original.tags[pos]
            else:
                value = observed["attainers"][int(index)-self.selected_count]
                e, f, tag = value["affine_e"], value["affine_f"], value["original_row"]
            self.bank.remember(self, tag, e, f)
        record["direction_memory_after_this_cut_sha256"] = self.bank.state_digest()
        return A, b, record

    def initial_cuts(self):
        return self.bank.rebuilt(self)

    def complete_report(self):
        result = super().complete_report()
        result["inherited_scope_labels"] = {
            "old_frozen_inner_solver_and_all_shared_budgets_are_unchanged":
                result.pop("old_frozen_inner_solver_and_all_shared_budgets_are_unchanged")}
        result["explicit_memory_seeded_inner_solver"] = POLICY
        result["original_shared_budgets_unchanged"] = True
        result["norm_direction_memory"] = self.bank.report()
        return result


class RememberingCompleteObjective(CompleteAffineHeight159Objective):
    def __init__(self, *args, initial_direction_records=(), **kwargs):
        self.pending_initial_directions = copy.deepcopy(list(initial_direction_records))
        super().__init__(*args, **kwargs)
        self.direction_bank = NormDirectionBank()
        self.evaluation_definition["cross_center_norm_memory"] = {
            "policy": POLICY, "maximum": MAX_NORMALS,
            "only_original_IDs_and_unit_ball_normals_are_carried": True}
        self.evaluation_sha256 = digest(self.evaluation_definition)

    def primary_observable_model(self, primary):
        original = super().primary_observable_model(primary)
        model = RememberingCompleteModel(original, self.direction_bank)
        for item in self.pending_initial_directions:
            self.direction_bank.remember(model, item["original_row"],
                item["affine_e"], item["affine_f"], item["source_center_binding_sha256"])
        self.pending_initial_directions = []
        self.complete_models[-1] = model
        primary.affine_spectral_model = model
        return model

    def snapshot(self):
        result = super().snapshot()
        if hasattr(self, "direction_bank"):
            result["cross_center_norm_memory"] = self.direction_bank.report()
        return result


def solve_remembered_primary(primary, model, cfg, ledger, *, progress, wall,
                         remaining_seconds, solve_one=None):
    """At most three calls, all charged to the original caller's shared ledger.

    The optional solver is solely for the new labelled-array developer fixture.
    Production supplies None and calls the unchanged original HiGHS function.
    The progress dictionary is installed in the outer model before this call,
    so an exception/budget exit cannot erase already started inner calls.
    """
    if primary is not model.primary:
        raise ValueError('model belongs to a different original mapped LP')
    if not isinstance(progress, dict) or not callable(wall) or not callable(remaining_seconds):
        raise ValueError('explicit progress and original wall-budget callbacks required')
    solver = frozen_solve_primary if solve_one is None else solve_one
    if solve_one is not None and cfg.get('new_affine_array_fixture_only') is not True:
        raise ValueError('custom LP callback is restricted to the labelled new array fixture')
    progress.update(
        policy=POLICY, inner_LPs=[], cut_rounds=[],
        model=model.summary(), status='new-affine-primary-not-yet-solved',
        inner_call_count=0, best_candidate_inner_index=None,
        physical_values_or_Jacobians_inside_inner_solver=0,
        epigraph_status_is_floating_model_status_not_actual_feasibility=True)
    rows, rhs, records, seen = [], [], [], set()
    cut_A, cut_b, inherited = model.initial_cuts()
    if len(cut_b):
        rows.append(cut_A)
        rhs.append(cut_b)
        records.append(inherited)
        seen.update(array_digest(np.r_[a, b]) for a, b in zip(cut_A, cut_b))
    progress["initial_rebuilt_memory_rows"] = len(cut_b)
    progress["memory_seeded_before_first_original_LP"] = True
    progress["cut_rounds"] = copy.deepcopy(records)
    incumbent = None
    stop = None
    last_lp = primary
    for inner in range(MAX_INNER_PRIMARY_LPS):
        wall()
        if ledger['linear_program_invocation_count'] >= cfg['max_linear_models']:
            stop = 'original-shared-LP-budget-before-next-inner-call'
            break
        remaining = float(remaining_seconds())
        if not np.isfinite(remaining) or remaining <= 0:
            stop = 'original-shared-active-time-before-next-inner-call'
            break
        last_lp = _cut_lp(primary, rows, rhs, records)
        local = dict(cfg, linear_program_seconds=min(
            float(cfg['linear_program_seconds']), remaining))
        event = {
            'inner_index': inner,
            'shared_LP_ordinal': int(ledger['linear_program_invocation_count'])+1,
            'LP_rows': len(last_lp.b), 'LP_variables': len(last_lp.c),
            'LP_matrix_bytes': last_lp.A.nbytes,
            'supporting_cut_rows': sum(len(x) for x in rhs),
            'time_limit_seconds': local['linear_program_seconds'],
            'status': 'LP-call-started'}
        progress['inner_LPs'].append(event)
        # Charge before the actual call. A solver exception is still a started call.
        ledger['linear_program_invocation_count'] += 1
        ledger['primary_LP_invocation_count'] += 1
        progress['inner_call_count'] += 1
        started = time.monotonic()
        try:
            p, reported = solver(last_lp, local)
        except Exception as error:
            event.update(status='LP-call-raised',
                         elapsed_seconds=time.monotonic()-started,
                         error={'type': type(error).__name__, 'message': str(error)})
            raise
        event.update(status='LP-returned', elapsed_seconds=time.monotonic()-started,
                     inherited_scalar_LP_report=copy.deepcopy(reported))
        if p is None:
            stop = 'original-LP-or-residual-gate-failed'
            event['status'] = stop
            break
        current = _candidate(last_lp, p, reported, model, cfg)
        event.update(
            status='evaluated-affine-candidate',
            evaluated_affine_slack=current['rho'],
            inherited_LP_relaxation_slack=float(reported['predicted_metric_slack']),
            raw_epigraph_gap=current['raw_epigraph_gap'],
            nonnegative_reported_epigraph_gap=current['nonnegative_reported_epigraph_gap'],
            gap_tolerance=current['gap_tolerance'],
            gap_met=current['gap_met'],
            repaired_objective=current['objective'],
            repaired_residual=copy.deepcopy(current['repaired_residual']),
            evaluated_model_improvement=current['gain'])
        if incumbent is None or current['objective'] < incumbent['objective']:
            incumbent = current
            incumbent['inner_index'] = inner
            progress['best_candidate_inner_index'] = inner
        if current['gap_met']:
            stop = 'evaluated-affine-epigraph-gap-met'
            break
        if inner+1 >= MAX_INNER_PRIMARY_LPS:
            stop = 'declared-three-inner-primary-LP-cap'
            break
        if ledger['linear_program_invocation_count'] >= cfg['max_linear_models']:
            stop = 'original-shared-LP-budget-after-inner-call'
            break
        evaluated = model.evaluated(p)
        violation = evaluated['phi']-model.target-float(reported['predicted_metric_slack'])
        selected = np.flatnonzero(violation > current['gap_tolerance'])
        if not len(selected):
            stop = 'no-distinct-violated-original-soft-row'
            break
        cut_A, cut_b, record = model.cuts(p, selected)
        keep = []
        for i in range(len(selected)):
            key = array_digest(np.r_[cut_A[i], cut_b[i]])
            if key not in seen:
                keep.append(i)
                seen.add(key)
        if not keep:
            stop = 'all-violated-supporting-cuts-already-present'
            break
        keep = np.asarray(keep, np.int64)
        if len(keep) != len(selected):
            cut_A, cut_b, record = model.cuts(p, selected[keep])
        rows.append(cut_A)
        rhs.append(cut_b)
        records.append(record)
        progress['cut_rounds'] = copy.deepcopy(records)
    if stop is None:
        stop = 'declared-inner-loop-ended'
    progress['status'] = stop
    progress['total_new_cut_rows'] = sum(len(x) for x in rhs)
    progress['all_started_inner_LPs_charged_to_original_ledger'] = True
    if incumbent is None:
        progress.update(returned_candidate=False,
                        proposal_rejected_before_geometry='no_original_gate_qualified_repaired_candidate')
        return None, progress
    # Earlier incumbents also obey every later cut when rho is their full (11).
    final_lp = _cut_lp(primary, rows, rhs, records)
    final_residual = final_lp.residual(incumbent['variables'])
    if max(final_residual['maximum_original_linear_row_violation'],
           final_residual['maximum_original_linear_bound_violation']) > cfg['linear_model_residual_limit']:
        raise ArithmeticError('best repaired incumbent failed a later valid supporting cut')
    report = progress
    source_report = incumbent['inherited_report']
    physical_cost = copy.deepcopy(source_report.get('primary_step_cost_diagnostic', {}))
    physical_cost.update(
        inherited_cut_LP_objective=physical_cost.get('returned_weighted_objective'),
        inherited_cut_LP_slack=physical_cost.get('returned_predicted_metric_slack'),
        returned_weighted_objective=incumbent['objective'],
        returned_predicted_metric_slack=incumbent['rho'],
        predicted_metric_slack_improvement=incumbent['gain'],
        repaired_rho_auxiliary=incumbent['repaired_rho_auxiliary'],
        prediction_uses_evaluated_affine_spectral_norm=True)
    projection = copy.deepcopy(source_report.get('projection', {}))
    legacy_label = projection.pop('original163_geometry_J_still_computed_then159_independent_columns_returned', None)
    projection.update(
        inherited_frozen_projection_label_not_actual_new_J_path=legacy_label,
        original163_geometry_J_still_computed_then159_independent_columns_returned=False,
        selected_J_and_true_de_df_contracted_before_radial_expansion=True)
    report.update(
        returned_candidate=bool(incumbent['gain'] > cfg['linear_model_improvement_floor']),
        returned_inner_index=incumbent['inner_index'],
        returned_epigraph_gap_met=incumbent['gap_met'],
        returned_inexact_cut_model=not incumbent['gap_met'],
        predicted_metric_slack=incumbent['rho'],
        predicted_slack_from_rows_and_outside=incumbent['rho'],
        predicted_slack_improvement=incumbent['gain'],
        normalized_step_norm=incumbent['norm_auxiliary'],
        returned_repaired_objective=incumbent['objective'],
        repaired_rho_auxiliary=incumbent['repaired_rho_auxiliary'],
        returned_LP_status=source_report.get('status'),
        returned_LP_success=source_report.get('success'),
        primary_step_cost_diagnostic=physical_cost,
        projection=projection,
        maximum_linear_row_violation=final_residual['maximum_original_linear_row_violation'],
        maximum_linear_bound_violation=final_residual['maximum_original_linear_bound_violation'],
        exact_convex_optimality_claim=False,
        returned_prediction_source='all selected original affine-e/f spectral norms plus unchanged outside floor')
    if not report['returned_candidate']:
        report['proposal_rejected_before_geometry'] = 'no-evaluated-affine-model-improvement-above-original-floor'
        return None, report
    return incumbent['step'], report


