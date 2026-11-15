"""Actions-only arithmetic on the eight saved actual85 3x3 LM models.

Read the genuine completed status, without importing the original mathematical
modules or evaluating a field, RHS, Jacobian, tail, finite difference, candidate
trial or optimizer. SVD is applied directly to each stored scaled Jacobian, not
obtained by subtracting eta^2 from augmented singular values. Alternative eta
values are predictions of the same saved linear model only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import struct
import sys
import traceback

for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'

HERE = Path(__file__).resolve().parent
SCHEMA = 'R259-saved-actual85-three-by-three-direction-spectrum-v1'
STATUS_BYTES = 54251
STATUS_SHA256 = '72397df159924d54bfcf7892b0f22d0a6b9e796238b5d29f8802e22120fb1a0a'
PARENT_SCHEMA = 'R259-original-three-equation-column-scaled-LM-resume-v1'
SOURCE_PINS = {
    'geometry_20261115_small_core_damped_resume.py': 'ec9a56fd184ff7d68fd1caadc9d350312b075172d20dabdee5203ce5b491ad1a',
    'geometry_20261115_small_core_damped_search.py': '1691c7d9aad782f9f1a6308ca16fa9630a44988a1b99decdca594a412cdb1728',
    'geometry_20261114_small_core_resonance.py': '3b9c45abed425a92be662c3547d088a3074ebcc5923c23ac2ef7aaf003124bd5',
}
INPUT_PINS = {
    'accepted': 'b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff',
    'prepared': '0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714',
    'tail_anchor': 'e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51',
    'tail_config': '01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5',
}
ACTUAL85 = dict(
    run_id=43667636063, source_commit='c9daab1a9f7b1330c6099450bd018bfab9026b0d',
    job_id=132670464205, artifact_id=14143056682, artifact_bytes=268505,
    artifact_zip_sha256='708ce51fb634552d376013d05b57e4f42cdc07d699e25753a2af0a2ea36e5775',
    artifact_transport_is_not_repeated_by_this_consumer=True,
    scientific_step_conclusion='success', publisher_step_conclusion='failure')


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def cleaned(value):
    if isinstance(value, dict):
        return {key: cleaned(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [cleaned(item) for item in value]
    if isinstance(value, float) and not math.isfinite(value):
        return dict(nonfinite_repr=repr(value), binary64_be=struct.pack('>d', value).hex())
    return value


def write(path, value):
    raw = (json.dumps(cleaned(value), indent=2, ensure_ascii=False, allow_nan=False) + '\n').encode()
    path.write_bytes(raw)
    return dict(file=path.name, bytes=len(raw), sha256=sha(raw))


def same_bits(left, right):
    if isinstance(left, list) or isinstance(right, list):
        return (isinstance(left, list) and isinstance(right, list)
                and len(left) == len(right)
                and all(same_bits(a, b) for a, b in zip(left, right)))
    if isinstance(left, bool) or isinstance(right, bool):
        return left is right
    if not isinstance(left, (float, int)) or not isinstance(right, (float, int)):
        return left == right
    return struct.pack('>d', float(left)) == struct.pack('>d', float(right))


def validate(raw):
    if len(raw) != STATUS_BYTES or sha(raw) != STATUS_SHA256:
        raise ValueError('Require the exact complete original actual85 status bytes')
    status = json.loads(raw)
    if (status.get('schema') != PARENT_SCHEMA or status.get('phase') != 'diagnostic-completed'
            or status.get('diagnostic_completed') is not True or status.get('success') is not False
            or status.get('native_nonlinear_solver_called') is not False
            or status.get('full_nonlinear_nonzero_lambda_solution_computed') is not False):
        raise ValueError('Retain actual85 completed-candidate scope, never a solved nonzero field')
    if (status.get('source_sha256') != SOURCE_PINS['geometry_20261115_small_core_damped_resume.py']
            or status.get('direction_engine_source_sha256') != SOURCE_PINS['geometry_20261115_small_core_damped_search.py']
            or status.get('original_diagnostic_source_sha256') != SOURCE_PINS['geometry_20261114_small_core_resonance.py']
            or status.get('input_sha256') != INPUT_PINS):
        raise ValueError('Bind the original producer, direction engine, model and four input identities')
    if (status.get('damping_cli_text') != '0.1' or status.get('damping_binary64') != .1
            or status.get('candidate_iteration_budget') != 8
            or status.get('original_backtrack_budget') != 20
            or status.get('original_armijo_coefficient') != .2
            or status.get('candidate_resonance_tolerance') != 1e-8):
        raise ValueError('Do not relabel the original eta, eight directions, twenty trials or original criteria')
    consumed = status.get('consumed_source_sha256', {})
    if len(consumed) != 11 or any(consumed.get(name) != digest for name, digest in SOURCE_PINS.items()):
        raise ValueError('Require all eleven original consumed-source identities')
    sources = []
    for name, digest in consumed.items():
        if Path(name).name != name:
            raise ValueError('Consumed sources must be local basenames')
        data = (HERE / name).read_bytes()
        if sha(data) != digest:
            raise ValueError('Frozen mathematical source changed: ' + name)
        sources.append(dict(file=name, bytes=len(data), sha256=digest, imported_or_executed=False))
    rows = status.get('searches', [])
    if len(rows) != 8:
        raise ValueError('Keep all eight actual85 directions')
    for index, row in enumerate(rows):
        model = row.get('direction_model', {})
        trials = row.get('trials', [])
        if (row.get('iteration') != index or row.get('accepted') is not True
                or len(trials) != 1 or trials[0].get('alpha') != 1.
                or trials[0].get('accepted') is not True):
            raise ValueError('The pinned actual85 history has eight full accepted steps')
        if (model.get('schema') != 'original-three-equation-column-scaled-LM-direction-v1'
                or model.get('positive_damping') != .1
                or model.get('normal_equations_formed') is not False
                or model.get('row_equations_reweighted') is not False
                or model.get('damping_added_to_original_nonlinear_residual') is not False
                or not same_bits(row['residual'], model['unscaled_equation'])
                or not same_bits(row['derivative'], model['unscaled_jacobian'])):
            raise ValueError('Preserve the same recorded original equation/J and direction semantics')
    return status, sources


def array(np, value, shape, name):
    result = np.asarray(value, dtype=np.float64)
    if result.shape != shape or not np.all(np.isfinite(result)):
        raise ValueError('Nonfinite or wrong-shaped pinned array: ' + name)
    return result


def aidentity(np, value):
    arr = np.asarray(value, dtype='<f8')
    return dict(shape=list(arr.shape), dtype='little-endian-float64',
                bytes=int(arr.nbytes), sha256=sha(arr.tobytes(order='C')),
                origin='binary64 values parsed from the original JSON, not an independently exported raw array')


def norms(np, value):
    value = np.asarray(value)
    return dict(L2=float(np.linalg.norm(value.ravel())),
                Linf=float(np.max(np.abs(value), initial=0.)))


def analyze(np, row, next_residual, comparison_eta):
    report = row['direction_model']
    r = array(np, row['residual'], (3,), 'r')
    J = array(np, row['derivative'], (3, 3), 'J')
    D = array(np, report['coordinate_scale'], (3,), 'D')
    A = array(np, report['scaled_jacobian'], (3, 3), 'A')
    z = array(np, report['scaled_direction'], (3,), 'saved z')
    direction = array(np, report['recovered_original_parameter_direction'], (3,), 'saved direction')
    action = array(np, report['original_jacobian_times_recovered_direction'], (3,), 'saved Jd')
    augmented = array(np, report['augmented_matrix'], (6, 3), 'original augmented matrix')
    rhs = array(np, report['augmented_rhs'], (6,), 'original augmented rhs')
    after = array(np, next_residual, (3,), 'next original residual')
    if not np.all(D > 0):
        raise ValueError('The original coordinate scales must be positive')
    eta = report['positive_damping']
    # Direct SVD of the original 3x3 A; no subtraction of nearly equal squares.
    U, sigma, Vh = np.linalg.svd(A, full_matrices=False)
    xi = U.T @ r
    Az = A @ z
    Jd = J @ direction
    model_residual = r + Az
    stationary = A.T @ model_residual + eta * eta * z
    checks = dict(
        A_minus_J_over_D=norms(np, A - J / D[None, :]),
        original_augmented_top_minus_A=norms(np, augmented[:3] - A),
        original_augmented_bottom_minus_eta_I=norms(np, augmented[3:] - eta * np.eye(3)),
        original_augmented_rhs_minus_declared=norms(np, rhs - np.r_[-r, np.zeros(3)]),
        saved_parameter_direction_minus_z_over_D=norms(np, direction - z / D),
        saved_action_minus_J_times_saved_direction=norms(np, action - Jd),
        A_times_z_minus_saved_action=norms(np, Az - action),
        original_saved_stationarity=norms(np, stationary),
        SVD_reconstruction=norms(np, (U * sigma[None, :]) @ Vh - A),
        U_orthogonality=norms(np, U.T @ U - np.eye(3)),
        V_orthogonality=norms(np, Vh @ Vh.T - np.eye(3)),
        all_numerical_checks_are_readouts_not_acceptance_gates=True)
    predictions = []
    for eta_text, value in [('0.1', eta), *comparison_eta]:
        denominator = sigma * sigma + value * value
        removal = sigma * sigma / denominator
        retention = value * value / denominator
        gain = sigma / denominator
        candidate_z = -(Vh.T @ (gain * xi))
        candidate_d = candidate_z / D
        candidate_Az = A @ candidate_z
        candidate_Jd = J @ candidate_d
        predicted_residual = r + candidate_Jd
        slope_by_equation = r * candidate_Jd
        original_linear_decrease_by_equation = -slope_by_equation - .5 * candidate_Jd * candidate_Jd
        original_linear_decrease = float(np.sum(original_linear_decrease_by_equation))
        scaled_A_linear_decrease = float(-r @ candidate_Az - .5 * (candidate_Az @ candidate_Az))
        penalty = .5 * value * value * float(candidate_z @ candidate_z)
        output = dict(
            damping_cli_text=eta_text, damping_binary64=value,
            scope='Saved fixed linear model only; no actual nonlinear/domain evaluation or acceptance',
            actual_nonlinear_trial_performed=False, nonlinear_acceptance_claimed=False,
            residual_removed_filter=removal.tolist(), residual_retained_filter=retention.tolist(),
            direction_filter=gain.tolist(), singular_residual_coordinates_before=xi.tolist(),
            singular_residual_coordinates_after=(retention * xi).tolist(),
            predicted_half_squared_residual_by_singular_direction=(.5 * (retention * xi)**2).tolist(),
            scaled_direction=candidate_z.tolist(), parameter_direction=candidate_d.tolist(),
            original_J_times_direction=candidate_Jd.tolist(),
            scaled_A_times_z_minus_original_J_times_direction=norms(np, candidate_Az - candidate_Jd),
            original_linear_residual=predicted_residual.tolist(),
            original_merit_directional_slope_by_equation=slope_by_equation.tolist(),
            original_merit_directional_slope=float(np.sum(slope_by_equation)),
            original_linear_merit_decrease_by_equation=original_linear_decrease_by_equation.tolist(),
            original_linear_merit_decrease=original_linear_decrease,
            stored_A_linear_merit_decrease=scaled_A_linear_decrease,
            scaled_damping_penalty=penalty,
            damped_quadratic_decrease=scaled_A_linear_decrease - penalty,
            stationary_readback=norms(np, A.T @ (r + candidate_Az) + value * value * candidate_z))
        if eta_text == '0.1':
            output['comparison_with_saved_actual_direction'] = dict(
                scaled_direction_difference=norms(np, candidate_z - z),
                parameter_direction_difference=norms(np, candidate_d - direction),
                original_action_difference=norms(np, candidate_Jd - action),
                comparison_does_not_replace_original_direction=True)
        predictions.append(output)
    identities = {name: aidentity(np, value) for name, value in
                  [('r', r), ('J', J), ('D', D), ('A', A), ('z', z),
                   ('parameter_direction', direction), ('Jd', action),
                   ('augmented_matrix', augmented), ('augmented_rhs', rhs)]}
    return dict(
        iteration=row['iteration'], original_status_pointer='searches/' + str(row['iteration']),
        parameters=row['parameters'], original_array_identities=identities,
        original_equation=r.tolist(), original_jacobian=J.tolist(),
        original_coordinate_scale=D.tolist(), original_scaled_jacobian=A.tolist(),
        original_saved_direction_model=report,
        original_true_model_merit_slope=row['true_model_merit_slope'],
        original_trials=row['trials'], original_next_equation=after.tolist(),
        original_augmented_rank_is_not_original_J_rank=True,
        new_direct_A_SVD=dict(U=U.tolist(), singular_values=sigma.tolist(), Vh=Vh.tolist(),
            residual_coordinates=xi.tolist(),
            half_squared_residual_by_singular_direction=(.5 * xi * xi).tolist(),
            condition_if_smallest_nonzero=(float(sigma[0] / sigma[-1]) if sigma[-1] != 0 else None),
            numerical_SVD_is_not_rigorous_rank_or_transversality=True,
            signs_and_bases_in_multiple_singular_spaces_are_not_canonical=True),
        original_saved_direction_readback=dict(
            original_action=action.tolist(), original_linear_residual=(r + action).tolist(),
            original_merit_slope_by_equation=(r * action).tolist(),
            original_linear_merit_decrease_by_equation=(-r * action - .5 * action * action).tolist(),
            actual_saved_after_minus_linear_prediction=(after - r - action).tolist(),
            actual_saved_half_squared_decrease_by_equation=(.5 * (r * r - after * after)).tolist(),
            actual_saved_merit_before=row['trials'][0]['merit_before'],
            actual_saved_merit_after=row['trials'][0]['actual_merit'],
            original_acceptance_not_redecided=True),
        consistency_readbacks=checks, local_model_predictions=predictions)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--status', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--comparison-damping', nargs='*', default=[],
                        help='Explicit optional saved-model-only values: 0.01 and/or 0.001')
    args = parser.parse_args()
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('All SVD, filters and model arithmetic belong to this public repository Actions')
    if (len(set(args.comparison_damping)) != len(args.comparison_damping)
            or any(value not in ('0.01', '0.001') for value in args.comparison_damping)):
        raise ValueError('Use only the explicitly declared 0.01/0.001 local-model comparisons')
    args.out.mkdir(parents=True, exist_ok=True)
    if any(args.out.iterdir()):
        raise ValueError('Preserve original files; require a fresh independent analysis directory')
    result = dict(schema=SCHEMA, phase='starting', diagnostic_completed=False,
        source_sha256=sha(Path(__file__).read_bytes()), actual85=ACTUAL85,
        original_status=dict(file=args.status.name, expected_bytes=STATUS_BYTES, expected_sha256=STATUS_SHA256),
        comparisons_requested=args.comparison_damping,
        field_RHS_J_tail_FD_or_optimizer_called=False,
        original_status_modified=False, original_criteria_modified=False,
        projective_or_geometric_normalization_performed=False,
        new_candidate_accepted=False, existence_or_transversality_proved=False,
        original_actual85_candidate_success=False, rows=[])
    exit_code = 1
    try:
        raw = args.status.read_bytes()
        status, sources = validate(raw)
        (args.out / 'actual85-original-status.json').write_bytes(raw)
        result['verified_original_status'] = dict(file='actual85-original-status.json', bytes=len(raw), sha256=sha(raw))
        result['verified_consumed_sources'] = sources
        result['original_input_bindings'] = status['input_sha256']
        result['binding_scope'] = 'The complete status and eleven original source payloads are verified; the four original large input payloads are not read again'
        import numpy as np
        result['runtime'] = dict(python=sys.version, numpy=np.__version__,
                                OPENBLAS_NUM_THREADS=os.environ['OPENBLAS_NUM_THREADS'])
        comparison_eta = [(text, float(text)) for text in args.comparison_damping]
        for index, row in enumerate(status['searches']):
            after = (status['searches'][index + 1]['residual'] if index + 1 < len(status['searches'])
                     else status['final']['low_equations_used'])
            result['rows'].append(analyze(np, row, after, comparison_eta))
        copied = ('parameters', 'unit_diagonal_defects', 'singular_values', 'numerical_parameter_condition',
                  'low_mode_trajectory_max_by_mode', 'low_two_by_two_right_condition_max_by_mode',
                  'radius_cell_denominator_minimum_absolute', 'source_circle_node_and_mid_minimum_beta2',
                  'independent_real_parameter_difference_checks')
        result['copied_original_final_description'] = {key: status['final'][key] for key in copied}
        result['interpretation_limits'] = [
            'Augmented rank three follows from positive eta and does not prove original J rank.',
            'Direct A singular values and residual projections describe this recorded finite local model, not rigorous parameter transversality.',
            'Large parameter sensitivity of the third equation is not itself large third-mode trajectory amplitude.',
            'Original maximum relative coordinate-FD errors do not separately certify a weak singular-direction derivative.',
            'Alternative eta predictions have no scalar/circle-domain, nonlinear merit, unit-threshold or full112 acceptance.',
            'No original nonlinear step is repeated and no original acceptance is reconsidered.']
        result.update(phase='diagnostic-completed', diagnostic_completed=True)
        exit_code = 0
    except Exception as error:
        result.update(phase='exception', error=repr(error), traceback=traceback.format_exc())
        (args.out / 'saved-direction-error.txt').write_text(result['traceback'])
    finally:
        full_directory = args.out / 'large-arrays'
        full_directory.mkdir(exist_ok=True)
        descriptor = write(full_directory / 'saved-direction-analysis.json', result)
        descriptor['file'] = 'large-arrays/saved-direction-analysis.json'
        summary_rows = []
        for row in result['rows']:
            summary_rows.append(dict(iteration=row['iteration'], parameters=row['parameters'],
                original_equation=row['original_equation'],
                singular_values=row['new_direct_A_SVD']['singular_values'],
                residual_coordinates=row['new_direct_A_SVD']['residual_coordinates'],
                half_squared_residual_by_singular_direction=row['new_direct_A_SVD']['half_squared_residual_by_singular_direction'],
                original_saved_direction_readback=row['original_saved_direction_readback'],
                consistency_readbacks=row['consistency_readbacks'],
                local_model_predictions=[{key: item[key] for key in (
                    'damping_cli_text', 'residual_removed_filter', 'residual_retained_filter',
                    'singular_residual_coordinates_after', 'original_linear_residual',
                    'original_merit_directional_slope', 'original_linear_merit_decrease',
                    'stored_A_linear_merit_decrease', 'scaled_damping_penalty', 'damped_quadratic_decrease',
                    'stationary_readback', 'actual_nonlinear_trial_performed', 'nonlinear_acceptance_claimed')}
                    for item in row['local_model_predictions']]))
        summary = {key: value for key, value in result.items() if key not in ('rows', 'traceback')}
        summary.update(full_analysis=descriptor, rows=summary_rows,
                       summary_is_saved_array_arithmetic_not_a_candidate_gate=True)
        write(args.out / 'saved-direction-summary.json', summary)
        print(json.dumps(dict(phase=result['phase'], diagnostic_completed=result['diagnostic_completed'],
                              rows=len(result['rows']), full_analysis=descriptor), allow_nan=False), flush=True)
    return exit_code


if __name__ == '__main__':
    raise SystemExit(main())
