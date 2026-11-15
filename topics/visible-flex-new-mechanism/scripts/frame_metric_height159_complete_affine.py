#!/usr/bin/env python3
"""Same159 frozen affine/SOC recovery with complete-grid model separation.

The previous outer recovery and primary cut solver are called unchanged.
The explicit subclass supplies selected functions plus four original-grid
maximum functions; all real geometry, pools, hard gates and budgets remain
owned by the frozen implementation. No module is monkeypatched.
"""
from __future__ import annotations

import copy
from fractions import Fraction as Q
import hashlib
from pathlib import Path

import numpy as np

from frame_height_null_coordinates import digest
from frame_selected_row_radial_jacobian import array_hash, _same_bytes
import frame_metric_height159_affine_spectral as frozen
from frame_metric_affine_spectral_model import POLICY as SELECTED_POLICY
from frame_complete_affine_metric_oracle import (
    POLICY, definition, CompleteDirectionalMetricOracle, CompleteGridAffineModel,
    implementation_hashes as oracle_hashes)

N = 159


def implementation_hashes():
    result = frozen.implementation_hashes()
    result.update(oracle_hashes())
    p = Path(__file__)
    result[p.name] = hashlib.sha256(p.read_bytes()).hexdigest()
    return result


def configuration(base):
    frozen.retention_definition(base)
    if base.get('affine_ef_spectral_primary_policy') != SELECTED_POLICY:
        raise ValueError('a completed frozen affine-e/f stage configuration is required')
    if 'complete_grid_affine_metric_policy' in base:
        raise ValueError('the new complete-grid policy is installed once')
    cfg = copy.deepcopy(base)
    cfg.update(
        complete_grid_affine_metric_policy=POLICY,
        complete_grid_affine_metric_definition=definition(),
        optimizer_objective='complete original two-grid norm of affine e/f, then unchanged physical step norm',
        complete_directional_scan_counts_in_original_active_time=True,
        complete_directional_scan_is_not_a_new_ordinary_physical_value=True,
        predicted_attainer_rows_never_mutate_actual_learning_pools=True,
        old_selected_soft_cut_functions_retained=True,
        complete_model_initial_slack_is_read_from_all_original_grid_values=True,
        no_added_physical_parameter_or_basis=True,
        no_new_capacity_reservation=True)
    return cfg


def retention_definition(cfg):
    result = frozen.retention_definition(cfg)
    result['inherited_selected_affine_base_total_prediction'] = result['base_total_prediction']
    result.update(
        base_total_prediction='complete coarse/fine maximum of phi_sigma(e+de*(z-x),f+df*(z-x)), with original exterior floor',
        same_seventeen_retention_conditions_with_explicit_complete_model_prediction=True,
        full_model_original_center_and_both_grids_are_bound_in_signature=True,
        original_SOC_scalar_RHS_and_correction_LP_unchanged=True)
    return result


class CompleteAffineHeight159Objective(frozen.AffineSpectralHeight159Objective):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.cfg.get('complete_grid_affine_metric_policy') != POLICY:
            raise ValueError('explicit complete original-grid model configuration required')
        self.complete_models = []
        self.complete_oracles = []
        inherited = self.evaluation_sha256
        self.evaluation_definition.update(
            complete_original_grid_affine_metric=definition(),
            inherited_selected_affine_evaluation_sha256=inherited,
            new_source_sha256=implementation_hashes(),
            successful_SOC_radius_retention=retention_definition(self.cfg),
            original_geometry_full_values_and_every_actual_gate_are_frozen=True)
        self.evaluation_sha256 = digest(self.evaluation_definition)

    def primary_observable_model(self, primary):
        self._wall()
        selected = super().primary_observable_model(primary)
        state = np.asarray(primary.state, float)
        if (state.shape != (N,)
                or not _same_bytes(np.asarray(self.geometry_cache['state'], float), state)
                or not _same_bytes(np.asarray(self.fine_cache['state'], float), state)):
            raise ValueError('complete model requires both ordinary caches at this accepted center')
        bounds, grids = {}, {}
        for label, selection, theta, data in (
                ('coarse', primary.selections[0], self.theta, self.geometry_cache),
                ('fine', primary.selections[1], self.fine_theta, self.fine_cache['data'])):
            if selection.full.grid.label != label:
                raise ValueError('the original coarse-then-fine grid order changed')
            bounds[label] = self.factorized.bind_ordinary(
                state, self.radial, theta, data, owner=label+'-current-cache')
            grids[label] = selection.full.grid
        oracle = CompleteDirectionalMetricOracle(
            self.factorized, state, bounds, grids, self.cfg, wall=self._wall)
        self.complete_oracles.append(oracle)
        model = CompleteGridAffineModel(selected, oracle)
        self.complete_models.append(model)
        self._wall()
        return model

    def actual_metric_error(self, model, candidate, *, fine_present):
        if not isinstance(model, CompleteGridAffineModel):
            raise ValueError('the original accepted-center complete affine model is required')
        # The old four terms remain attached to the old selected rows, not the
        # four maximum-function indices used only by the new inner separator.
        original = super().actual_metric_error(
            model.selected_model, candidate, fine_present=fine_present)
        old_no_call = original.pop('no_extra_geometry_J_LP_or_value_call', None)
        model.oracle.set_post_primary_phase()
        before = model.oracle.statistics['new_full_direction_evaluations']
        step = np.asarray(candidate, float)-np.asarray(model.primary.state, float)
        evaluated = model.oracle.evaluate(step)
        rho = max(0., model.outside, float(np.max(evaluated['phi']))-model.target)
        calls = model.oracle.statistics['new_full_direction_evaluations']-before
        answer = dict(original)
        answer['inherited_selected_error_schema'] = original.get('schema')
        answer['schema'] = POLICY+('-complete-actual-error' if fine_present else '-coarse-only-actual-error')
        answer['inherited_selected_no_extra_call_label'] = old_no_call
        answer['no_additional_ordinary_geometry_LP_or_physical_value_call'] = True
        answer['new_analytic_directional_evaluations_for_full_prediction'] = calls
        answer['full_prediction_binding_sha256'] = model.binding_sha256
        answer['accepted_base_total_step_sha256'] = array_hash(step)
        answer['complete_affine_smooth_slack'] = rho
        answer['complete_affine_four_maxima'] = [float(v) for v in evaluated['phi']]
        answer['complete_affine_attainers'] = copy.deepcopy(evaluated['attainers'])
        if not fine_present:
            answer.update(
                full_model_prediction_available_even_without_fine_actual=True,
                complete_actual_difference_terms_not_inferred_from_missing_fine=True)
            return answer
        rho_S = float(original['selected_affine_ef_spectral_slack'])
        rho_A = float(original['selected_actual_smooth_slack'])
        rho_F = float(original['complete_actual_smooth_slack'])
        rho_T = float(original['complete_actual_true_slack'])
        coverage = rho-rho_S
        nonlinear = rho_F-rho
        smooth = rho_T-rho_F
        selected_nonlinear = rho_A-rho_S
        actual_omitted = rho_F-rho_A
        if not np.all(np.isfinite([rho, rho_S, rho_A, rho_F, rho_T, coverage, nonlinear])):
            raise FloatingPointError('nonfinite complete affine error decomposition')
        answer['complete_model_difference_terms'] = {
            'full_affine_minus_original_selected_affine': coverage,
            'complete_actual_smooth_minus_complete_affine': nonlinear,
            'complete_true_minus_complete_actual_smooth': smooth,
            'full_actual_ef_error_from_old_terms': selected_nonlinear+actual_omitted-coverage,
            'two_term_total_identity_absolute_error': abs((rho_T-rho)-(nonlinear+smooth)),
            'old_terms_to_full_identity_absolute_error': abs(
                nonlinear-(selected_nonlinear+actual_omitted-coverage)),
            'raw_floating_values_not_clipped': True,
            'no_sign_assumption_on_full_actual_ef_nonlinearity': True}
        return answer

    def snapshot(self):
        result = super().snapshot()
        result['complete_original_grid_affine_metric_definition'] = definition()
        result['successful_SOC_radius_retention'] = retention_definition(self.cfg)
        result['complete_original_grid_oracle_progress'] = [
            oracle.report() for oracle in self.complete_oracles]
        result['new_prediction_rows_do_not_change_real_pools_or_capacity'] = True
        return result


def _correct_frozen_scope_labels(record, replacements):
    inherited = record.setdefault('inherited_frozen_scope_labels', {})
    for key, value in replacements.items():
        if key in record:
            inherited.setdefault(key, copy.deepcopy(record[key]))
        record[key] = value


def attach_complete_model_reports(result, objective):
    """Metadata only: original statuses, errors, LPs, gates and controller stay.

    The frozen execution still labels its generic model selected-only and
    declares zero inner Jacobians. These old literal labels are preserved
    before replacement by the actual new oracle records.
    """
    solver = result.get('solver')
    if not isinstance(solver, dict):
        raise ValueError('original frozen recovery solver result missing')
    _correct_frozen_scope_labels(solver, {'method': POLICY})
    models = solver.get('models', [])
    if len(models) > len(objective.complete_models):
        raise ArithmeticError('frozen outer models cannot outnumber installed complete models')
    for model_record, model in zip(models, objective.complete_models):
        complete = model.complete_report()
        lp = model_record.get('linear_program')
        if not isinstance(lp, dict):
            raise ValueError('original outer model lost the primary progress dictionary')
        events = complete['oracle']['direction_events']
        rows = complete['oracle']['new_original_row_J_events']
        inner_events = [x for x in events if x.get('phase') == 'primary-inner']
        inner_rows = [x for x in rows if x.get('phase') == 'primary-inner']
        _correct_frozen_scope_labels(lp, {
            'policy': POLICY,
            'physical_values_or_Jacobians_inside_inner_solver': {
                'ordinary_geometry_values': 0,
                'full_directional_JVP_started': len(inner_events),
                'original_selected_metric_row_J_started': len(inner_rows)},
            'returned_prediction_source': 'all original coarse/fine affine-e/f spectral norms with unchanged exterior floor'})
        lp['complete_original_grid_model'] = complete
        lp['all_original_selected_functions_and_frozen_primary_rows_retained'] = True
        lp['all_oracle_and_added_row_J_costs_use_the_original_active_clock'] = True
        lp['original_primary_inner_cap_and_shared_LP_budget_not_changed'] = True
        for correction in model_record.get('corrections', []):
            comparison = correction.get('linear_program', {}).get(
                'same_step_scalar_and_affine_budget_comparison')
            if isinstance(comparison, dict):
                comparison['affine_model_scope'] = 'complete original two grids at the same actual primary step'
                comparison['selected_initial_slack_retained'] = model.rho0_selected
                comparison['full_initial_slack_retained'] = model.rho0
                comparison['original_scalar_RHS_was_not_replaced_by_a_new_full_model_RHS'] = True
        diagnostic = model_record.get('accepted_SOC_base_total_step_diagnostic')
        if isinstance(diagnostic, dict):
            old_no_call = diagnostic.pop('no_extra_geometry_J_LP_or_value_call', None)
            diagnostic.setdefault('inherited_frozen_scope_labels', {})[
                'no_extra_geometry_J_LP_or_value_call'] = old_no_call
            diagnostic.update(
                prediction_policy=POLICY,
                no_extra_ordinary_geometry_LP_or_physical_value_call=True,
                directional_JVP_cache_and_costs_are_reported_in_complete_original_grid_model=True)
    result['inherited_selected_affine_spectral_primary_definition'] = copy.deepcopy(
        result.get('affine_ef_spectral_primary_definition'))
    result['complete_original_grid_affine_metric_definition'] = definition()
    result['successful_SOC_radius_retention'] = retention_definition(objective.cfg)
    result['complete_original_grid_oracle_progress'] = [
        oracle.report() for oracle in objective.complete_oracles]
    result['frozen_outer_recovery_function_was_called_without_monkeypatch'] = True
    result['unchanged_original_true_gates_and_LP_value_time_limits'] = True
    return result


def run_complete_affine_recovery(objective, initial, *, known_metric_locations=(),
                                 restored_controller=None,
                                 artificial_inputs_only=False, evaluate_only=False):
    if not isinstance(objective, CompleteAffineHeight159Objective):
        raise ValueError('the explicit complete original-grid objective is required')
    result = frozen.run_affine_spectral_recovery(
        objective, initial, known_metric_locations=known_metric_locations,
        restored_controller=restored_controller,
        artificial_inputs_only=artificial_inputs_only, evaluate_only=evaluate_only)
    return attach_complete_model_reports(result, objective)
