#!/usr/bin/env python3
"""Actions-only scalar analysis of already returned complete-Phi QP reports.

No field arrays, geometric evaluations, J/J* products, eigenvalue experiments,
or additional fixtures are used.  The formulas use scalars already recorded
by fullclosed_gauss_inequality_qp.py.  Floating evaluations of theoretical
inequalities are diagnostics, not outward optimality/reach certificates.
"""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024*1024), b''):
            h.update(block)
    return h.hexdigest()


def finite_number(value):
    return isinstance(value, (int, float)) and math.isfinite(value)


def division(numerator, denominator):
    return numerator/denominator if finite_number(numerator) and finite_number(denominator) and denominator > 0 else None


def analyze_direction(direction, parent_stats, report):
    qp = direction.get('qp', {})
    needed = ('damping', 'coordinate_norm', 'half_objective_slope',
              'quadratic_predicted_actual_change')
    missing = [key for key in needed if not finite_number(direction.get(key))]
    if missing:
        return dict(index=direction.get('index'), complete_scalar_input=False, missing=missing)
    mu, norm = direction['damping'], direction['coordinate_norm']
    slope = direction['half_objective_slope']
    predicted_change = direction['quadratic_predicted_actual_change']
    mu2, norm2 = mu*mu, norm*norm
    data_energy = predicted_change-2*slope
    regularization_energy = mu2*norm2
    q0 = qp.get('initial_data_objective')
    qdata = qp.get('final_data_objective')
    qreg = qp.get('final_regularized_objective')
    from_data = 2*(qdata-q0-slope) if all(finite_number(x) for x in (qdata,q0)) else None
    achieved = q0-qreg if all(finite_number(x) for x in (q0,qreg)) else None
    pg = qp.get('final_face_projected_gradient_norm')
    face_error = pg*pg/(2*mu2) if finite_number(pg) and mu2 > 0 else None
    face_distance = pg/mu2 if finite_number(pg) and mu2 > 0 else None
    alpha_data = -slope/data_energy if slope < 0 and data_energy > 0 else None
    total_energy = data_energy+regularization_energy
    alpha_regularized = -slope/total_energy if slope < 0 and total_energy > 0 else None
    bounds = qp.get('normalized_bounds', [])
    row_values = qp.get('normalized_row_values', [])
    literal_rows_present = len(bounds) == len(row_values) and bool(bounds)
    zero_feasible = literal_rows_present and all(finite_number(x) and x >= 0 for x in bounds)
    linear_ratios = [(bound/value, i) for i, (bound, value) in enumerate(zip(bounds, row_values))
                     if finite_number(bound) and finite_number(value) and value > 0]
    limiting = min(linear_ratios, default=None)
    alpha_linear = limiting[0] if limiting is not None else None
    alpha_model_capped = None
    if zero_feasible and alpha_data is not None:
        alpha_model_capped = min(alpha_data, alpha_linear) if alpha_linear is not None else alpha_data
    blocks = direction.get('quadratic_model', {}).get('bridge', {}).get('blocks', {})
    eigen_min, eigen_max = blocks.get('minimum_eigenweight'), blocks.get('maximum_eigenweight')
    initial_gradient_norm = qp.get('initial_gradient_norm')
    atol, rtol = report.get('qp_atol'), report.get('qp_rtol')
    declared_tolerance = (atol+rtol*initial_gradient_norm
        if all(finite_number(x) for x in (atol,rtol,initial_gradient_norm)) else None)
    effective_peak_mass = None
    spectral = parent_stats.get('spectral', {})
    maximum = parent_stats.get('max_relative_gram')
    if all(finite_number(x) for x in (maximum, blocks.get('epsilon'), blocks.get('scale'), blocks.get('p'))):
        eps, scale, k = blocks['epsilon'], blocks['scale'], int(blocks['p'])//2
        zero_eigen_loss = (eps*eps/(scale*scale))**k
        max_eigen_loss = ((maximum*maximum+eps*eps)/(scale*scale))**k
        phi = spectral.get('phi_normalized', direction.get('old_merit'))
        effective_peak_mass = division(phi-2*zero_eigen_loss, 2*(max_eigen_loss-zero_eigen_loss))
    result = dict(index=direction.get('index'), complete_scalar_input=True,
        normalized_mean_Phi_damping=mu, damping_squared=mu2,
        coordinate_norm_squared=norm2, data_Hessian_ray_energy=data_energy,
        data_Hessian_ray_energy_from_QP_objectives=from_data,
        regularization_ray_energy=regularization_energy,
        damping_to_data_ray_energy_ratio=division(regularization_energy,data_energy),
        damping_fraction_of_total_ray_energy=division(regularization_energy,total_energy),
        data_Hessian_ray_Rayleigh=division(data_energy,norm2),
        damped_Hessian_ray_Rayleigh=division(total_energy,norm2),
        nominal_Hessian_smallest_eigenvalue=mu2,
        kernel_coordinate_dimension_lower=max(0,report.get('augmented_variables',0)-report.get('original_variables',0)),
        kernel_scope='All coordinate ker(T) directions are also killed by J T and geometric C=G T. Exact zero-start CG/row projections stay in their orthogonal complement; nominal conditioning is not effective Krylov conditioning.',
        achieved_regularized_quadratic_drop=achieved,
        fixed_current_face_remaining_drop_bound_float=face_error,
        fixed_current_face_distance_bound_float=face_distance,
        fixed_face_bound_relative_to_achieved_drop=division(face_error,achieved),
        fixed_face_bound_scope='||P g||^2/(2 mu^2); exact algebra on the same active affine face, evaluated here from ordinary floating reports. It is not a bound for releasing inequalities or the nonlinear Phi.',
        face_projected_gradient_norm=pg,
        computed_gradient_tolerance=qp.get('gradient_tolerance'),
        reconstructed_gradient_tolerance=declared_tolerance,
        absolute_tolerance_share=division(atol,declared_tolerance),
        Frobenius_residual_block_eigenweight_minimum=eigen_min,
        Frobenius_residual_block_eigenweight_maximum=eigen_max,
        Frobenius_residual_block_condition_ratio=division(eigen_max,eigen_min),
        residual_block_condition_is_full_Hessian_condition=False,
        parent_equivalent_peak_loss_mass=effective_peak_mass,
        equivalent_peak_loss_mass_scope='(Phi-Phi0)/(2*(ell(maxGram)-ell(0))); a normalized peak-equivalent loss mass, not a measured support fraction or a rank estimate.',
        initial_half_Phi_ray_slope=slope, unregularized_quadratic_ray_minimum_alpha=alpha_data,
        regularized_quadratic_ray_minimum_alpha=alpha_regularized,
        actual_recorded_bounds_zero_feasible=zero_feasible,
        selected_linear_ray_upper_alpha=alpha_linear,
        selected_linear_ray_upper_unbounded=literal_rows_present and limiting is None,
        selected_linear_limiting_row=None if limiting is None else limiting[1],
        geometry_capped_quadratic_ray_alpha=alpha_model_capped,
        ray_bound_scope='Only these selected first-order inequalities. Every permanent point and the actual fixed Phi must still be reread on every trial.',
        accepted=direction.get('accepted'), accepted_alpha=direction.get('accepted_alpha'),
        minimum_raw_multiplier=qp.get('minimum_multiplier'),
        release_events=sum(item.get('kind','').startswith('release_negative_multiplier')
                           for item in qp.get('transitions',[])),
        scalar_followup=('If a full step really passed, the computed data-ray alpha exceeds 1, and the finite linear bound allows extension, '
            'pay one fresh directional JVP at that actual accepted field to measure the true Phi slope along the saved ray. '
            'Only a negative fresh slope with strictly positive known-point margins gives the local true-descent argument. '
            'Do not infer it from this base quadratic or add another long CG budget automatically.'))
    return result


def analyze(path):
    value = json.loads(path.read_text())
    parent = value.get('initial', {})
    analyses = []
    for direction in value.get('directions', []):
        analyses.append(analyze_direction(direction, parent, value))
        if direction.get('accepted'):
            for trial in direction.get('trials', []):
                if trial.get('alpha') == direction.get('accepted_alpha'):
                    parent = trial.get('statistics', parent)
                    break
    return dict(report=str(path), report_sha256=sha(path),
        parent_bundle_sha256=value.get('bundle_sha256'),
        final_bundle_sha256=value.get('final_bundle_sha256'),
        source_sha256=value.get('source_sha256'),
        safety=value.get('numerical_reach_safety_factor'), directions=analyses)


def sanitize(value):
    if isinstance(value,float) and not math.isfinite(value):
        return dict(nonfinite_value=repr(value))
    if isinstance(value,dict):
        return {key:sanitize(item) for key,item in value.items()}
    if isinstance(value,list):
        return [sanitize(item) for item in value]
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', type=Path, action='append', required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if os.environ.get('GITHUB_ACTIONS') != 'true':
        raise SystemExit('New scalar diagnostics are scheduled in public GitHub Actions; this source has not been run locally.')
    if args.out.exists():
        raise FileExistsError(args.out)
    result = sanitize(dict(schema='already-returned-full-Phi-QP-scalar-diagnostics-v1',
        source_sha256=sha(__file__), github_run_id=os.environ.get('GITHUB_RUN_ID'),
        reports=[analyze(path.resolve()) for path in args.report],
        new_field_evaluations=0, new_J_or_Jtranspose_calls=0, new_fixtures=0,
        computation='Scalar arithmetic from already-returned actual report values only',
        outward_certification=False, continuous_reach_claimed=False))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    print(json.dumps(result), flush=True)


if __name__ == '__main__':
    main()
