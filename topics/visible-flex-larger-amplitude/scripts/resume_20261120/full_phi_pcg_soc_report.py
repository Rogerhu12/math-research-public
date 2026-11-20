#!/usr/bin/env python3
"""Actions-only JSON attribution for the declared complete PCG + SOC reports.

Reads existing report JSON, never field/direction arrays or numerical modules.
The original ray, the uncorrected main-QP iterate, and an actual SOC correction
are separate objects.  A SOC-accepted record has overwritten model fields;
only its explicitly saved uncorrected_direction_model belongs to ray trials.
This consumer checks reported schema/source contracts, not whole source bodies.
The launcher's complete source binder remains the source-authentication step.
"""
import argparse
from collections import Counter
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys


SCHEMA = 'returned-complete-full-Phi-PCG-SOC-attribution-v1'
BOTTLENECK_SHA = '930d832f92cf61021f394b835fb9ab0e14ae0d1ce3ca4a72f597a65e09bab0b0'
SCALAR_SHA = '9124229786200659f1c9dc73620eecd75dda6493990f684149471d7003263b9d'
SOC_DERIVER_SHA = '805823e49970246bf532b65a0caefd88244b414ee52f8f555ff28b745d2fd30a'
SOC_HELPER_SHA = '5bc50d6b18223685da8ea355d179191234ad83b5e92fd6313f4070b7e02127c7'
COMPOSITE_SHA = '40e8c42b8c66424d06ff08af8dff8d1505eff2b4f48ba905c9ae405000d2357e'
AUGMENTER_SHA = 'f96cb48933d1356b97b5a687d25cc05cd33188b08c14cd0b439f170b027fce18'
FRAME_SHA = '324513a115a61800e105f340bd070eb50931bbe16dd66d3a8643bfe11298f2da'
MOMENTS_SHA = 'da083ae9b20674a29121c25d5b57ef867fba442559a50791b7fc0b43d4db5719'
V4_SHA = 'dd59510599334843cf79159cafe5d2548818ab8b7fdf6813f164ee811247ad3b'
V3_SHA = 'fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4'
V2_SHA = 'c131b45649e87be2e7f71088d817edb6402a74a4cb50a6b13018e252217f88f7'
TAIL_SHA = '2e0219c50543d859a9c649553bc4dde863df24daab26ffa75e5112baa4a90216'
BASES = {
    'original': '5ef7e26834b55d97d2c2dfc2d82f0113b2e072b2f46d3d54f04978177ce0629a',
    'R671': 'b1b0725acffde7958d9a4ad245057ea243d4319bde15bd9a7778ade3b0f844e8',
}
QP_SCHEMAS = {
    'fullspace-feasible-active-set-cg-early-release-v2': V2_SHA,
    'fullspace-feasible-active-set-cg-reliable-update-v3': V3_SHA,
    'fullspace-feasible-active-set-fixed-PCG-v4': V4_SHA,
}
MODEL_FIELDS = ('direction_sha256', 'coordinate_norm', 'projected_endpoint_error',
    'half_objective_slope', 'quadratic_predicted_actual_change',
    'quadratic_predicted_actual_objective', 'nodal_jet_step_max_by_Y_U_A',
    'height_step', 'maximum_selected_linear_product', 'selected_linear_products')


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS', '').lower() != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Consume the actual scientific report JSON in public repository Actions')


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def load_stdlib(name, path, digest):
    if sha(path) != digest:
        raise ValueError('Use the exact declared stdlib report consumer: '+str(path))
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def divide(a, b):
    return a/b if number(a) and number(b) and b > 0 else None


def difference(a, b):
    return a-b if number(a) and number(b) else None


def summary_numbers(values):
    finite = [v for v in values if number(v)]
    return dict(count=len(values), finite_count=len(finite),
        minimum=min(finite, default=None), maximum=max(finite, default=None),
        maximum_absolute=max((abs(v) for v in finite), default=None))


def selected(value, keys):
    return {key:value.get(key) for key in keys}


def at(values, index):
    return values[index] if isinstance(values, list) and 0 <= index < len(values) else None


def reported_contract(report):
    schema = report.get('schema')
    candidates = {
        'fullclosed-gauss-'+model+suffix: (model, composite)
        for model in BASES for suffix, composite in (
            ('-parent-row-SOC-v1', False), ('-coarse-PCG-parent-row-SOC-v1', True))}
    if schema not in candidates:
        raise ValueError('Unknown complete SOC report schema; do not guess overwritten model semantics')
    model, composite = candidates[schema]
    lineage = report.get('soc_derivation', {})
    roles = report.get('source_sha256_by_role', {})
    if (lineage.get('schema') != 'frozen-full-driver-exact-locations-parent-row-SOC-derivation-v1'
            or lineage.get('model') != model
            or lineage.get('frozen_driver_sha256') != BASES[model]
            or lineage.get('derivation_source_sha256') != SOC_DERIVER_SHA
            or lineage.get('helper_sha256') != SOC_HELPER_SHA
            or roles.get('soc') != SOC_HELPER_SHA):
        raise ValueError('Reported SOC semantics do not match the frozen 805/5bc contract')
    if report.get('objective') != 'spectral':
        raise ValueError('This consumer analyzes the actual spectral Phi, not another objective')
    if composite:
        chain = report.get('pcg_soc_derivation', {})
        expected = dict(coarse_frame=FRAME_SHA, coarse_moments=MOMENTS_SHA,
                        qp=V4_SHA, coarse_qp_v3=V3_SHA)
        if (chain.get('schema') != 'frozen-full-driver-exact-locations-SOC-current-coarse-PCG-v1'
                or chain.get('model') != model
                or chain.get('composite_derivation_source_sha256') != COMPOSITE_SHA
                or chain.get('coarse_PCG_augmentation_source_sha256') != AUGMENTER_SHA
                or chain.get('SOC_lineage') != lineage
                or chain.get('numerical_component_sha256s') != expected
                or any(roles.get(key) != value for key, value in expected.items())
                or report.get('coarse_preconditioner_setup', {}).get('enabled') is not True):
            raise ValueError('Reported PCG+SOC contract differs from the declared complete source chain')
    elif roles.get('qp') not in (V2_SHA, V3_SHA, V4_SHA):
        raise ValueError('Unknown pure-SOC inner solver source; do not infer its iteration semantics')
    context = report.get('exact_tail_context', {})
    final_context = report.get('exact_tail_context_final', {})
    if model == 'R671':
        definition = context.get('definition')
        if (roles.get('exact_tail') != TAIL_SHA or not isinstance(definition, dict)
                or definition.get('source_sha256') != TAIL_SHA):
            raise ValueError('R671 report lacks its actual canonical field representation')
        if final_context and final_context.get('definition') != definition:
            raise ValueError('This returned batch changed its declared R671 canonical model')
    elif context or final_context:
        raise ValueError('An original-lift report cannot silently carry an R671 model')
    return dict(reported_schema=schema, physical_model=model, composite_PCG_SOC=composite,
        actual_driver_sha256_from_report=report.get('source_sha256'),
        reported_source_sha256_by_role=roles,
        frozen_base_driver_sha256=BASES[model],
        composite_deriver_sha256=COMPOSITE_SHA if composite else None,
        model_identity_sha256=context.get('model_identity_sha256'),
        canonical_model_definition=context.get('definition'),
        final_model_identity_sha256=final_context.get('model_identity_sha256'),
        reported_schema_and_component_contract_matched=True,
        entire_actual_source_body_authenticated_by_this_consumer=False,
        source_scope='Report-only interpretation. The launch-time whole-body binder authenticates actual source bytes; this consumer does not replace it.')


def original_ray_view(direction):
    """Analysis-only scalar view, never a rewritten report or saved direction."""
    kind = direction.get('accepted_update_kind')
    if kind not in ('original_ray', 'parent_row_soc'):
        raise ValueError('Unknown accepted update kind in this frozen SOC contract')
    soc = direction.get('soc') or {}
    corrected_accepted = kind == 'parent_row_soc'
    if corrected_accepted:
        if direction.get('accepted') is not True or soc.get('accepted') is not True:
            raise ValueError('SOC-overwritten model fields have no matching actual acceptance')
        old = direction.get('uncorrected_direction_model')
        if not isinstance(old, dict) or any(key not in old for key in MODEL_FIELDS):
            raise ValueError('Cannot attribute original trials without the complete saved uncorrected model')
        if old['direction_sha256'] != soc.get('original_direction_sha256'):
            raise ValueError('The uncorrected model and SOC original direction identities differ')
        if direction.get('direction_sha256') != soc.get('direction_sha256'):
            raise ValueError('Accepted corrected direction identity differs from its SOC record')
        trial = soc.get('trial') or {}
        for key in ('half_objective_slope', 'quadratic_predicted_actual_change',
                    'quadratic_predicted_actual_objective'):
            if direction.get(key) != trial.get(key):
                raise ValueError('Accepted corrected model does not match its actual SOC trial: '+key)
        view = dict(direction)
        view.update(old)
        # The ray itself was rejected. Do not feed corrected acceptance into
        # the original R673 saved-ray follow-up or QP energy identities.
        view.update(accepted=False, accepted_alpha=None, new_merit=None)
        source = 'direction.uncorrected_direction_model'
    else:
        if soc.get('accepted') is True:
            raise ValueError('Accepted SOC has not been identified as the actual update')
        view = dict(direction)
        source = 'direction original model fields, not overwritten by an accepted SOC'
    return view, source


def model_energy(old, slope, change, norm, damping, reported_energy=None):
    energy = change-2*slope if number(change) and number(slope) else None
    norm2 = norm*norm if number(norm) else None
    mu2 = damping*damping if number(damping) else None
    regularization = mu2*norm2 if number(mu2) and number(norm2) else None
    predicted = old+change if number(old) and number(change) else None
    total = energy+regularization if number(energy) and number(regularization) else None
    return dict(old_Phi=old, half_Phi_directional_slope=slope,
        actual_Phi_directional_derivative=2*slope if number(slope) else None,
        data_Hessian_direction_energy=energy, recorded_data_Hessian_direction_energy=reported_energy,
        recorded_energy_discrepancy=difference(energy, reported_energy),
        coordinate_norm=norm, coordinate_norm_squared=norm2, damping=damping,
        regularization_direction_energy=regularization,
        damping_to_data_energy_ratio=divide(regularization, energy),
        data_direction_Rayleigh=divide(energy, norm2),
        regularized_direction_Rayleigh=divide(total, norm2),
        predicted_full_Phi_change=change, predicted_full_Phi=predicted,
        objective_scope='Actual-Phi Taylor model uses 2*v^T*A*z+||A*z||^2. The QP regularizer is reported separately; virtual RHS norm is not actual Phi.')


def actual_trial(trial, *, old, slope, energy, alpha, accepted, model_source, report):
    merit = trial.get('merit')
    geometry = trial.get('curvature_points') or {}
    raw_filter = trial.get('curvature_filter')
    evaluated = isinstance(raw_filter, dict)
    point_filter = raw_filter or {}
    product = point_filter.get('necessary_reach_product')
    safety = report.get('numerical_reach_safety_factor')
    curvature = point_filter.get('sampled_curvature')
    absolute_cap = report.get('sampled_curvature_cap')
    reasons = []
    if trial.get('finite') is not True:
        reasons.append('nonfinite_metric_or_arithmetic')
    elif trial.get('feasible') is not True:
        reasons.append('sampled_field_domain')
    elif trial.get('descent') is not True:
        reasons.append('true_Phi_descent_or_Armijo')
    elif evaluated and point_filter.get('passed') is not True:
        if geometry.get('complete') is not True:
            reasons.append('incomplete_or_singular_true_geometry_read')
        if number(product) and number(safety) and product > safety:
            reasons.append('true_known_point_product_above_algorithm_margin')
        if number(curvature) and number(absolute_cap) and curvature > absolute_cap:
            reasons.append('additional_absolute_curvature_cap')
        if not reasons:
            reasons.append('reported_true_geometry_filter_failed')
    elif accepted:
        reasons.append('accepted')
    else:
        reasons.append('not_recorded_as_accepted')
    predicted = (old+2*alpha*slope+alpha*alpha*energy
        if all(number(v) for v in (old, alpha, slope, energy)) else None)
    actual_drop = difference(old, merit)
    predicted_drop = difference(old, predicted)
    stats = trial.get('statistics') or {}
    return dict(index=trial.get('index'), alpha=alpha, Phi=merit,
        finite=trial.get('finite'), feasible=trial.get('feasible'), descent=trial.get('descent'),
        accepted=bool(accepted), attribution_reasons=reasons,
        curvature_feasible_recorded=trial.get('curvature_feasible'),
        geometry_evaluated=evaluated, geometry_complete=geometry.get('complete') if evaluated else None,
        geometry_passed=point_filter.get('passed') if evaluated else None,
        geometry_not_evaluated_is_not_pass=True,
        true_known_point_product=product, numerical_margin=safety,
        product_margin_remaining=difference(safety, product),
        product_below_one=(product < 1) if number(product) else None,
        sampled_curvature=curvature,
        reference_diameter_point_lower=point_filter.get('reference_diameter_lower_bound'),
        applied_curvature_cap=point_filter.get('applied_curvature_cap'),
        worst_geometry_location=geometry.get('worst'),
        worst_grid_location=geometry.get('observation_grid_worst'),
        maximum_radius_location=geometry.get('maximum_radius_point'),
        declared_additional_witness_count=geometry.get('additional_witness_point_count'),
        max_gram=stats.get('max_relative_gram'),
        original_weighted_sse=stats.get('radial_weighted_frobenius_sse'),
        model_source=model_source, same_alpha_predicted_Phi=predicted,
        actual_Phi_drop=actual_drop, same_alpha_predicted_Phi_drop=predicted_drop,
        actual_to_same_alpha_predicted_drop=divide(actual_drop, predicted_drop),
        new_permanent_curvature_locations=trial.get('new_permanent_curvature_locations', []),
        new_permanent_radius_locations=trial.get('new_permanent_radius_locations', []),
        arithmetic_error=trial.get('arithmetic_error'),
        continuous_curvature_or_reach_inferred=False)


def linear_details(qp, report, history_module):
    schema = qp.get('schema')
    if schema not in QP_SCHEMAS:
        raise ValueError('Unknown actual inner-QP schema; do not attribute corrected KKT values')
    declared = report.get('source_sha256_by_role', {}).get('qp')
    actual = QP_SCHEMAS[schema]
    if declared != actual and not (declared == V4_SHA and actual == V3_SHA):
        raise ValueError('Actual QP schema differs from its declared source or literal v4-to-v3 fallback')
    if schema == 'fullspace-feasible-active-set-fixed-PCG-v4':
        if qp.get('implementation_source_sha256') != V4_SHA:
            raise ValueError('Actual v4 report names another implementation')
    linear = history_module.linear_history(qp, report)
    history = qp.get('history', [])
    replacements = qp.get('residual_replacements', [])
    restarts = qp.get('restarts', [])
    linear.update(actual_QP_schema=schema, numerical_implementation_sha256=QP_SCHEMAS[schema],
        diagnostic_point='The returned uncorrected main-QP augmented iterate d',
        diagnostics_transferred_to_SOC_point=False,
        Euclidean_projected_gradient=True,
        actual_linear_residual_relative_defect=qp.get('final_actual_linear_residual_relative_defect'),
        final_normalized_bounds=qp.get('normalized_bounds'),
        final_normalized_row_values=qp.get('normalized_row_values'),
        final_normalized_slack=qp.get('normalized_final_slack'),
        reliable_update=qp.get('reliable_update'),
        recorded_residual_replacements=replacements,
        recorded_replacement_count=len(replacements),
        forced_replacement_restart_count=sum(v.get('forces_restart') is True for v in replacements),
        replacement_projected_relative_defect_summary=summary_numbers(
            [v.get('projected_gradient_relative_defect') for v in replacements]),
        recorded_restarts=restarts,
        restart_reason_counts=dict(Counter(v.get('reason', 'missing_reason') for v in restarts)),
        reported_longest_same_face_advances=qp.get('longest_same_face_advances'),
        direction_kind_counts=dict(Counter(v.get('direction_kind', 'not_reported') for v in history)),
        history_restart_reason_counts=dict(Counter(v.get('restart_reason') for v in history
                                                   if v.get('restart_reason') is not None)),
        conjugacy_defect_summary=summary_numbers(
            [v.get('previous_direction_H_conjugacy_relative') for v in history
             if 'previous_direction_H_conjugacy_relative' in v]),
        last_history_record=history[-1] if history else None,
        QP_seconds=qp.get('seconds'),
        nominal_tolerance_is_not_a_causal_explanation=True)
    return linear


def preconditioner_details(direction):
    construction = direction.get('coarse_preconditioner') or {}
    qp = direction.get('qp') or {}
    fixed = qp.get('fixed_preconditioner') or {}
    application = fixed.get('applications') or {}
    frame = construction.get('frame') or {}
    moments = construction.get('current_coarse_data_Gram') or {}
    small = construction.get('fixed_metadata') or {}
    construct_seconds = construction.get('construction_seconds')
    apply_seconds = application.get('seconds')
    components = [frame.get('setup_seconds'), moments.get('elapsed_seconds'), small.get('setup_seconds')]
    component_sum = sum(components) if all(number(v) for v in components) else None
    return dict(enabled_in_direction=construction.get('enabled', False),
        construction_status=construction.get('status', 'no_coarse_augmentation'),
        fallback_to_frozen_v3=construction.get('fallback_to_frozen_v3'),
        construction_failure=construction.get('failure'), construction_seconds=construct_seconds,
        frame_seconds=components[0], moment_assembly_seconds=components[1], small_SPD_seconds=components[2],
        construction_component_sum=component_sum,
        construction_other_seconds=difference(construct_seconds, component_sum),
        construction_and_application_seconds=(construct_seconds+apply_seconds
            if number(construct_seconds) and number(apply_seconds) else None),
        timing_scope='Construction total includes its frame/moments/small-SPD parts. Apply time is inside QP seconds; neither subset is added a second time to wall time.',
        actual_direction_damping=construction.get('actual_direction_damping'),
        background_inverse_scale=construction.get('background_inverse_scale'),
        counted_additional_operator_calls=construction.get('additional_counted_operator_calls'),
        declared_additional_J_calls=construction.get('additional_J_calls'),
        declared_additional_JT_calls=construction.get('additional_JT_calls'),
        unit_column_probes=construction.get('unit_column_probes'),
        actual_QP_schema=qp.get('schema'), actual_QP_status=qp.get('status'),
        construction_record_QP_schema=construction.get('actual_QP_schema'),
        construction_record_QP_status=construction.get('actual_QP_status'),
        fixed_B_enabled_in_actual_QP=fixed.get('enabled', False),
        apply_calls=application.get('applications', 0), apply_seconds=apply_seconds,
        apply_failure_count=len(application.get('failures', [])),
        apply_failures=application.get('failures', []),
        last_successful_apply=application.get('last_success'),
        completed_Euclidean_release_starters=application.get('euclidean_release_starters_completed'),
        application_failure_truncated_status=qp.get('status') == 'fixed_preconditioner_application_failed',
        automatic_application_failure_retry=construction.get('automatic_application_failure_retry'),
        solver_replaced_preconditioner=fixed.get('solver_replaced_preconditioner'),
        frame_K_difference_from_identity=frame.get('K_float_maximum_difference_from_identity'),
        frame_K_cholesky_diagonal_minimum=frame.get('K_cholesky_diagonal_minimum'),
        frame_gram_cholesky_diagonal_minimum=frame.get('frame_cholesky_diagonal_minimum'),
        small_Hc_cholesky_diagonal_minimum=small.get('small_Hc_cholesky_diagonal_minimum'),
        small_hessian_metadata=small.get('small_hessian'),
        moment_assembly_metadata={key: value for key, value in moments.items()
            if key not in ('source_and_input_provenance', 'provenance')},
        release_before_SOC=dict(
            dense_Gram=construction.get('dense_Gram_reference_released_before_solve'),
            frame_and_factor=construction.get('frame_and_factor_released_after_solve')),
        unchanged_objective_and_mother_norm=construction.get('unchanged_original_QP'),
        SPD_success_not_inferred_from_source_identity=True)


def soc_details(direction, report):
    soc = direction.get('soc')
    if not isinstance(soc, dict):
        return dict(attempted=bool(direction.get('soc_attempted')), returned_detail_present=False,
                    proposal_available=False, accepted=False)
    proposal = soc.get('proposal') or {}
    if (proposal.get('schema') != 'full-Phi-parent-row-one-SOC-proposal-v1'
            or proposal.get('source_sha256') != SOC_HELPER_SHA):
        raise ValueError('Unknown actual SOC proposal semantics')
    row_meta = (direction.get('active_geometry') or {}).get('rows', [])
    selected_indices = proposal.get('correction_parent_row_indices', [])
    values = proposal.get('full_trial_fixed_parent_rows') or {}
    corrected_values = proposal.get('corrected_fixed_parent_rows') or {}
    initial_values = {r.get('index'): r for r in values.get('rows', [])}
    end_values = {r.get('index'): r for r in corrected_values.get('rows', [])}
    selected_rows = []
    for local, index in enumerate(selected_indices):
        if isinstance(index, bool) or not isinstance(index, int) or not 0 <= index < len(row_meta):
            raise ValueError('SOC selected parent row index is outside the actual row metadata')
        row = row_meta[index]
        selected_rows.append(dict(parent_row=index, curvature_point=row.get('curvature_point'),
            radius_point=row.get('radius_point'), parent_gradient_norm=row.get('gradient_coordinate_norm'),
            parent_product=row.get('current_product'), normalized_bound=row.get('normalized_bound'),
            original_Cd=at(proposal.get('original_normalized_row_values'), index),
            original_slack=at(proposal.get('original_slack'), index),
            full_trial_fixed_row=initial_values.get(index),
            nonlinear_minus_parent_linear=at(proposal.get('actual_nonlinear_minus_parent_linear'), index),
            right_hand_side=at(proposal.get('right_hand_side'), local),
            correction_Ce=at(proposal.get('correction_normalized_row_values'), index),
            correction_equation_residual=at(proposal.get('equality_residual'), local),
            corrected_Cz=at(proposal.get('corrected_normalized_row_values'), index),
            corrected_slack=at(proposal.get('corrected_slack'), index),
            corrected_fixed_row=end_values.get(index)))
    qr = proposal.get('qr') or {}
    old_rows_keys = ('normalized_bounds', 'original_normalized_row_values', 'original_slack',
        'original_maximum_linear_violation', 'correction_normalized_row_values',
        'corrected_normalized_row_values', 'corrected_slack', 'corrected_maximum_linear_violation',
        'old_physical_linear_products', 'corrected_physical_linear_products',
        'actual_physical_margin_allowance_from_numerical_tolerance',
        'literal_Cd_plus_Ce_discrepancy_max_abs', 'all_old_rows_rechecked')
    result = dict(attempted=bool(direction.get('soc_attempted')),
        returned_detail_present=True, helper_attempted=proposal.get('attempted'),
        proposal_available=proposal.get('proposal_available'), accepted=soc.get('accepted'),
        proposal_reason=proposal.get('reason'), proposal_complete=proposal.get('complete'),
        correction_source_sha256=proposal.get('source_sha256'), identity=proposal.get('identity'),
        original_direction_sha256=soc.get('original_direction_sha256'),
        corrected_direction_sha256=soc.get('direction_sha256'),
        corrected_direction_path_from_report=soc.get('direction_path'),
        original_coordinate_norm=proposal.get('coordinate_norm'),
        correction_norm=proposal.get('correction_norm'),
        correction_over_original_norm=proposal.get('correction_over_original_norm'),
        corrected_coordinate_norm=proposal.get('corrected_coordinate_norm'),
        cubic_tau=soc.get('tau'), cubic_inward_scalar=proposal.get('cubic_inward_scalar'),
        tau_is_algorithm_parameter_not_certified_threshold=True,
        full_trial_fixed_rows_complete=values.get('complete'),
        full_trial_positive_fixed_row_count=(len(values.get('positive_normalized_rows', []))
            if values.get('complete') is True else None),
        fixed_parent_rows_read=len(values.get('rows', [])),
        corrected_fixed_rows_complete=corrected_values.get('complete'),
        corrected_positive_fixed_row_count=(len(corrected_values.get('positive_normalized_rows', []))
            if corrected_values.get('complete') is True else None),
        fixed_parent_nonlinear_reads=dict(full_trial=values or None,
                                         corrected_trial=corrected_values or None),
        selection_performed='correction_parent_row_indices' in proposal,
        selected_parent_row_indices=selected_indices,
        selected_parent_row_count=(len(selected_indices)
            if 'correction_parent_row_indices' in proposal else None),
        selected_parent_rows=selected_rows,
        rank_tolerance=proposal.get('rank_tolerance'),
        feasibility_tolerance=proposal.get('feasibility_tolerance'),
        QR=selected(qr, ('convention', 'method', 'selected_rows', 'retained_prefix_rank',
            'rejected_parent_row', 'full_numerical_row_rank', 'constraints_dropped',
            'orthogonality_max_abs_error', 'right_inverse_norm_diagnostic',
            'triangular_diagonal', 'triangular_singular_values', 'rows')),
        selected_equality_residual=proposal.get('equality_residual'),
        selected_equality_residual_max_abs=proposal.get('equality_residual_max_abs'),
        all_original_linear_rows=selected(proposal, old_rows_keys),
        old_slack_summary=summary_numbers(proposal.get('original_slack', [])),
        corrected_slack_summary=summary_numbers(proposal.get('corrected_slack', [])),
        seconds=soc.get('seconds'), additional_cost=soc.get('additional_cost'),
        additional_operator_counts=soc.get('additional_operator_counts'),
        main_QP_diagnostics_recomputed_at_correction=False,
        corrected_KKT_status=None, corrected_Pg_norm=None,
        corrected_QP_scope='No main-QP solve or KKT residual was performed at d+e. Do not transfer d diagnostics to the correction.',
        fallback_scope=proposal.get('fallback'),
        absence_of_positive_fixed_rows_does_not_prove_a_new_peak_cause=True)
    trial = soc.get('trial')
    if isinstance(trial, dict):
        slope = trial.get('half_objective_slope')
        change = trial.get('quadratic_predicted_actual_change')
        energy = trial.get('model_direction_energy')
        old = direction.get('old_merit')
        norm = proposal.get('corrected_coordinate_norm')
        result['corrected_model'] = model_energy(old, slope, change, norm,
                                               direction.get('damping'), energy)
        result['actual_trial'] = actual_trial(trial, old=old, slope=slope, energy=energy,
            alpha=trial.get('corrected_direction_alpha'), accepted=soc.get('accepted') is True,
            model_source='direction.soc.trial actual parent A(d+e)', report=report)
        result['recorded_corrected_prediction'] = trial.get('quadratic_predicted_actual_objective')
        result['recorded_corrected_ratio'] = trial.get('actual_to_same_corrected_step_predicted_decrease')
        result['corrected_prediction_discrepancy'] = difference(
            result['corrected_model']['predicted_full_Phi'], result['recorded_corrected_prediction'])
    return result


def damping_details(direction, next_direction, report):
    before = direction.get('damping')
    accepted = direction.get('accepted') is True
    alpha = direction.get('accepted_alpha')
    ratio = direction.get('actual_to_full_step_predicted_decrease')
    after = None
    if number(before):
        if not accepted:
            after = before*4
            rule = 'No accepted actual step: multiply mu by 4'
        elif alpha == 1 and number(ratio) and ratio > .75:
            after = max(1e-8, before/2)
            rule = 'Accepted full actual direction with actual/predicted ratio > .75: halve mu'
        else:
            after = before
            rule = 'Accepted direction does not meet frozen full-step reduction rule: retain mu'
    else:
        rule = 'Missing finite recorded damping'
    recorded_after = direction.get('damping_after_direction')
    next_value = next_direction.get('damping') if next_direction is not None else report.get('final_damping')
    return dict(before=before, expected_after_from_frozen_actual_rule=after,
        recorded_after=recorded_after, recorded_after_matches=(after == recorded_after) if after is not None else None,
        next_direction_or_final_damping=next_value,
        next_matches=(after == next_value) if after is not None and next_value is not None else None,
        accepted_update_kind=direction.get('accepted_update_kind'),
        actual_accepted_alpha=alpha, actual_accepted_full_step_ratio=ratio, rule=rule,
        ratio_uses_corrected_model=direction.get('accepted_update_kind') == 'parent_row_soc',
        changed_update_rule=False)


def analyze(path, scalar_module, history_module):
    require_actions()
    report = json.loads(Path(path).read_text())
    contract = reported_contract(report)
    parent = report.get('initial', {})
    parent_origin = 'report.initial'
    details, public = [], {}
    source_directions = report.get('directions', [])
    for position, direction in enumerate(source_directions):
        qp = direction.get('qp') or {}
        view, ray_model_source = original_ray_view(direction)
        scalars = scalar_module.analyze_direction(view, parent, report)
        # Kernel-invariance wording in frozen R673 is for ordinary CG. Retain
        # the dimension fact without importing that assertion into fixed B.
        if qp.get('fixed_preconditioner', {}).get('enabled'):
            scalars['kernel_scope'] = ('ker(T) is killed by J*T and C. This scalar consumer does not '
                'check whether actual fixed B preserves that kernel and its Euclidean complement; '
                'ordinary-CG invariant-subspace wording is not automatically inherited.')
        linear = linear_details(qp, report, history_module)
        preconditioner = preconditioner_details(direction)
        ray_energy = scalars.get('data_Hessian_ray_energy')
        rays = []
        original_accepted = direction.get('accepted') is True and direction.get('accepted_update_kind') == 'original_ray'
        for trial in direction.get('trials', []):
            rays.append(actual_trial(trial, old=direction.get('old_merit'),
                slope=view.get('half_objective_slope'), energy=ray_energy, alpha=trial.get('alpha'),
                accepted=original_accepted and trial.get('alpha') == direction.get('accepted_alpha'),
                model_source=ray_model_source, report=report))
        soc = soc_details(direction, report)
        next_direction = source_directions[position+1] if position+1 < len(source_directions) else None
        damping = damping_details(direction, next_direction, report)
        final_release = qp.get('final_normalized_release_diagnostics') or {}
        pg, tol = qp.get('final_face_projected_gradient_norm'), qp.get('gradient_tolerance')
        gain, gain_threshold = final_release.get('largest_normalized_descent_gain'), final_release.get('actual_release_threshold')
        geometry_rejections = [t for t in rays if t['finite'] is True and t['feasible'] is True
            and t['descent'] is True and t['geometry_evaluated'] and t['geometry_passed'] is not True]
        full_ray = next((t for t in rays if t['alpha'] == 1.), None)
        accepted_trial = (soc.get('actual_trial') if direction.get('accepted_update_kind') == 'parent_row_soc'
                          else next((t for t in rays if t['accepted']), None))
        indicators = dict(Euclidean_projected_tolerance_met=(pg <= tol) if number(pg) and number(tol) else None,
            unit_release_gain_above_threshold=(gain > gain_threshold)
                if number(gain) and number(gain_threshold) else None,
            main_QP_iteration_limit=qp.get('status') == 'iteration_limit',
            preconditioner_construction_fallback=preconditioner['fallback_to_frozen_v3'],
            preconditioner_application_failure=preconditioner['application_failure_truncated_status'],
            true_descent_geometry_rejected_ray_count=len(geometry_rejections),
            original_full_ray_true_geometry_rejection=bool(full_ray in geometry_rejections) if full_ray else False,
            SOC_attempted=soc['attempted'], SOC_proposal_available=soc['proposal_available'],
            SOC_accepted=soc['accepted'],
            accepted_half_or_smaller_original_ray=bool(original_accepted and number(direction.get('accepted_alpha'))
                                                       and direction['accepted_alpha'] <= .5),
            frozen_mu_retained_after_acceptance=bool(direction.get('accepted')
                and damping['expected_after_from_frozen_actual_rule'] == direction.get('damping')),
            raw_negative_multiplier_used_as_causal_indicator=False,
            linear_and_nonlinear_bottlenecks_are_separate=True)
        entry = dict(index=direction.get('index'), accepted=direction.get('accepted'),
            accepted_update_kind=direction.get('accepted_update_kind'),
            accepted_alpha=direction.get('accepted_alpha'), accepted_bundle_sha256=direction.get('accepted_bundle_sha256'),
            old_Phi=direction.get('old_merit'), new_Phi=direction.get('new_merit'),
            parent_statistics_source=parent_origin,
            main_QP=linear, preconditioner=preconditioner,
            original_ray=dict(model_source=ray_model_source,
                direction_sha256=view.get('direction_sha256'),
                field_direction_or_saved_array_loaded=False,
                scalar_analysis=scalars, trials=rays,
                trial_count=len(rays), all_recorded_ray_trials_retained=True,
                trial_reason_counts=dict(Counter(reason for t in rays for reason in t['attribution_reasons'])),
                accepted=original_accepted), SOC=soc, accepted_actual_trial=accepted_trial,
            damping=damping, evidence_indicators=indicators,
            costs=dict(direction_seconds=direction.get('seconds'),
                preparation_and_linear_seconds=direction.get('preparation_and_linear_seconds'),
                QP_seconds=qp.get('seconds'),
                preconditioner_construction_seconds=preconditioner['construction_seconds'],
                preconditioner_apply_seconds=preconditioner['apply_seconds'],
                SOC_seconds=soc.get('seconds'),
                counted_inner_operator_calls=direction.get('inner_counts'),
                outside_inner_calls=direction.get('outside_inner_calls'),
                costs_are_nested_not_additive=True),
            no_corrected_QP_status_fabricated=True,
            no_new_saved_ray_or_directional_derivative_evaluation=True)
        details.append(entry)
        key = 'd'+str(direction.get('index', position)).zfill(3)
        if key in public:
            raise ValueError('Repeated actual direction index')
        accepted_info = accepted_trial or {}
        public[key] = dict(index=direction.get('index'), mu=direction.get('damping'),
            old_Phi=entry['old_Phi'], new_Phi=entry['new_Phi'], accepted=entry['accepted'],
            accepted_kind=entry['accepted_update_kind'], accepted_alpha=entry['accepted_alpha'],
            accepted_product=accepted_info.get('true_known_point_product'),
            accepted_max_gram=accepted_info.get('max_gram'),
            accepted_same_alpha_ratio=accepted_info.get('actual_to_same_alpha_predicted_drop'),
            QP_schema=qp.get('schema'), QP_status=qp.get('status'), advances=qp.get('advances'),
            main_QP_Pg=pg, main_QP_tolerance=tol, main_QP_Pg_over_tolerance=divide(pg, tol),
            release_count=linear['release_count'], face_additions=linear['successful_face_additions'],
            longest_same_face=qp.get('longest_same_face_advances'),
            final_unit_release_gain=gain, final_unit_release_threshold=gain_threshold,
            QP_seconds=qp.get('seconds'), preconditioner_status=preconditioner['construction_status'],
            preconditioner_construction_seconds=preconditioner['construction_seconds'],
            preconditioner_apply_calls=preconditioner['apply_calls'],
            preconditioner_apply_seconds=preconditioner['apply_seconds'],
            preconditioner_apply_failures=preconditioner['apply_failure_count'],
            original_ray_geometry_rejections=len(geometry_rejections),
            original_ray_data_energy=ray_energy,
            original_ray_mu_to_data_energy=scalars.get('damping_to_data_ray_energy_ratio'),
            SOC_attempted=soc['attempted'], SOC_available=soc['proposal_available'], SOC_accepted=soc['accepted'],
            SOC_reason=soc.get('proposal_reason'), SOC_selected_rows=soc.get('selected_parent_row_count'),
            SOC_correction_norm=soc.get('correction_norm'), SOC_norm_ratio=soc.get('correction_over_original_norm'),
            SOC_QR_rank=(soc.get('QR') or {}).get('retained_prefix_rank'),
            SOC_QR_full_rank=(soc.get('QR') or {}).get('full_numerical_row_rank'),
            SOC_old_slack_minimum=(soc.get('corrected_slack_summary') or {}).get('minimum'),
            SOC_actual_product=(soc.get('actual_trial') or {}).get('true_known_point_product'),
            SOC_actual_Phi=(soc.get('actual_trial') or {}).get('Phi'),
            SOC_seconds=soc.get('seconds'), next_mu=damping['recorded_after'],
            damping_replay_matches=damping['recorded_after_matches'])
        if direction.get('accepted'):
            if direction.get('accepted_update_kind') == 'parent_row_soc':
                parent = direction['soc']['trial']['statistics']
                parent_origin = 'directions['+str(position)+'].soc.trial.statistics'
            else:
                candidates = [t for t in direction.get('trials', [])
                    if t.get('alpha') == direction.get('accepted_alpha')]
                if len(candidates) != 1:
                    raise ValueError('Accepted original ray has no unique actual statistics record')
                parent = candidates[0]['statistics']
                parent_origin = 'directions['+str(position)+'].trials accepted original ray statistics'
    return dict(report=str(Path(path).resolve()), report_sha256=sha(path), contract=contract,
        report_complete=report.get('complete'),
        input_bundle_sha256=report.get('bundle_sha256'), final_bundle_sha256=report.get('final_bundle_sha256'),
        observation_carrier_sha256=report.get('observation_carrier_sha256'),
        initial_damping=report.get('initial_damping'), final_damping=report.get('final_damping'),
        numerical_safety=report.get('numerical_reach_safety_factor'), active_band=report.get('active_band'),
        requested_reach_ratio=report.get('requested_reach_ratio'),
        actual_direction_count=len(details),
        final_known_point_filter=report.get('final_curvature_filter'),
        coarse_setup=report.get('coarse_preconditioner_setup'),
        status_counts=dict(Counter(v['main_QP']['qp_status'] for v in details)),
        accepted_kind_counts=dict(Counter(v['accepted_update_kind'] for v in details if v['accepted'])),
        preconditioner_status_counts=dict(Counter(v['preconditioner']['construction_status'] for v in details)),
        SOC_attempts=sum(v['SOC']['attempted'] for v in details),
        accepted_SOC=sum(v['SOC']['accepted'] is True for v in details),
        scalar_summary=public, directions=details,
        interpretation='Descriptive attribution from returned scalars, not a causal ranking or a new solver budget. Inner linear nonconvergence, geometric rejection, and numerical component failure remain distinct.',
        permanent_points_or_rows_removed=False, continuous_geometry_or_reach_claimed=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', type=Path, action='append', required=True)
    parser.add_argument('--scalar-source', type=Path)
    parser.add_argument('--history-source', type=Path)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    require_actions()
    if args.out.exists():
        raise FileExistsError('Use a new output path; retain the actual previous attribution')
    here = Path(__file__).resolve().parent
    scalar_path = (args.scalar_source or here/'full_phi_qp_scalar_diagnostics.py').resolve()
    history_path = (args.history_source or here/'full_phi_qp_bottleneck_report.py').resolve()
    scalar = load_stdlib('pcg_soc_frozen_R673_scalars', scalar_path, SCALAR_SHA)
    history = load_stdlib('pcg_soc_frozen_R677_history', history_path, BOTTLENECK_SHA)
    result = scalar.sanitize(dict(schema=SCHEMA, source_sha256=sha(__file__),
        scalar_source_sha256=sha(scalar_path), history_source_sha256=sha(history_path),
        github_run_id=os.environ.get('GITHUB_RUN_ID'), github_sha=os.environ.get('GITHUB_SHA'),
        reports=[analyze(path.resolve(), scalar, history) for path in args.report],
        field_evaluations=0, J_or_Jtranspose_calls=0, field_or_direction_arrays_read=0,
        new_fixtures=0, strict_outward_arithmetic=False,
        input='Actual returned JSON reports only; the two imported frozen dependencies are stdlib scalar/history readers',
        old_930d_source_changed=False, reported_schema_is_not_source_authentication=True))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, separators=(',', ':'), allow_nan=False)+'\n')
    print(json.dumps(dict(schema=SCHEMA, report=str(args.out.resolve()), report_sha256=sha(args.out),
        reports=len(result['reports']), directions=sum(v['actual_direction_count'] for v in result['reports']),
        field_evaluations=0, J_or_Jtranspose_calls=0, arrays_read=0, new_fixtures=0)), flush=True)


if __name__ == '__main__':
    main()
