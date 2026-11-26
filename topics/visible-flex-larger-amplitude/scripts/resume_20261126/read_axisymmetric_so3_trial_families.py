#!/usr/bin/env python3
"""Read every recorded 606 trial's actual constraint family and literal address.

This is a new pure reader of complete existing reports. It first executes the
unchanged, whole-source-bound 6d54 report validator, then extracts only recorded
scalar facts and selected witness addresses. It never evaluates F, J, roots,
geometry, QP or a scientific array, and never presumes a failure is reach.
"""
import argparse
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys

SCHEMA = 'actual-complete-606-all-trial-constraint-family-attribution-v1'
TOPIC = 'topics/visible-flex-larger-amplitude'
READER_PATH = 'scripts/resume_20261126/read_axisymmetric_so3_report.py'
READER_SHA = '6d54cbba7ff998bc98b0f39c6a26ae33c16957fb0b9dc0fffced1037212455eb'
DRIVER_SHA = '606e00485be3625378916cfa66f6da1803b82005ba14959610bb1a4be7cfb1f9'
AMPLITUDE_FAMILIES = ('body_diameter', 'distance_plus', 'distance_minus',
    'cap_diameter', 'height_floor')


def sha(path):
    value = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            value.update(block)
    return value.hexdigest()


def record(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path), bytes=path.stat().st_size)


def compact(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Read actual whole scientific reports only in public Actions')


def bind_reader(repo):
    path = (Path(repo).resolve()/TOPIC/READER_PATH).resolve()
    if sha(path) != READER_SHA:
        raise ValueError('The original complete pure source changed')
    name = '_complete_original_606_pure_reader_for_trial_families'
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    for method in ('read_report', 'direction', 'geometric', 'statistic'):
        source = Path(getattr(module, method).__code__.co_filename).resolve()
        if source != path or sha(source) != READER_SHA:
            raise ValueError('No replacement for the original complete report/source guard')
    if module.DRIVER_SHA != DRIVER_SHA:
        raise ValueError('The pure reader must bind the complete actual 606 source')
    return module, record(path)


def finite_number(value):
    return (not isinstance(value, bool) and isinstance(value, (int, float))
        and math.isfinite(float(value)))


def address(value):
    """Only literal named physical addresses; no inferred grid interpretation."""
    if not isinstance(value, dict):
        return None
    result = {}
    for key in ('cell', 'stage', 'angle', 'branch'):
        if key in value:
            item = value[key]
            if (isinstance(item, bool) or not isinstance(item, (int, float))
                    or not math.isfinite(float(item)) or int(item) != item):
                raise ValueError('A recorded physical address index is malformed')
            result[key] = int(item)
    for key in ('u', 'phi'):
        if key in value:
            if not finite_number(value[key]):
                raise ValueError('A recorded physical address coordinate is nonfinite')
            result[key] = float(value[key])
            result[key+'_binary64_hex'] = float(value[key]).hex()
    if not all(key in result for key in ('cell', 'u', 'phi')):
        return dict(recorded_named_fields=result, complete_literal_address=False)
    return dict(result, complete_literal_address=True)


def candidate(value):
    if value is None:
        return None
    if not isinstance(value, dict):
        raise ValueError('A recorded geometric working candidate is not an object')
    return dict(score=value.get('score'), kind=value.get('kind'),
        location=address(value.get('location')))


def all_candidates(value):
    if value is None:
        return []
    if not isinstance(value, list):
        raise ValueError('The actual working candidate family is not a list')
    return [candidate(item) for item in value]


def family_geometry(value):
    if value is None:
        return dict(read=False, complete=None, passed=None, maximum_physical_g=None,
            family_g={}, positive_families=[], missing_family_values=['geometry_not_read'],
            necessary_reach_product=None, maximum_absolute_principal_curvature=None,
            diameter_point_lower=None, maximum_radius=None, current_height=None,
            farthest_radius_witness_scope='recorded maximum-radius witness; not asserted active for max(2, 2|H|, 2radius)',
            K_worst=None, farthest_radius_witness=None,
            body_candidates=[], paired_distance_candidates=[],
            all_permanent_read=None, both_witness_signs_read=None,
            current_full_point_sha256=None, error_type=None, error=None)
    if not isinstance(value, dict):
        raise ValueError('An actual full geometry record must be an object or null')
    amplitude = value.get('amplitude')
    if amplitude is None:
        amplitude = {}
    if not isinstance(amplitude, dict):
        raise ValueError('Malformed amplitude record')
    families = {'reach': value.get('reach_physical_g')}
    families.update({key: amplitude.get(key) for key in AMPLITUDE_FAMILIES})
    missing = [key for key, item in families.items() if not finite_number(item)]
    positive = [key for key, item in families.items() if finite_number(item) and item > 0]
    return dict(read=True, complete=value.get('complete'), passed=value.get('passed'),
        maximum_physical_g=value.get('maximum_physical_g'), family_g=families,
        positive_families=positive, missing_family_values=missing,
        necessary_reach_product=value.get('necessary_reach_product'),
        maximum_absolute_principal_curvature=value.get('maximum_absolute_principal_curvature'),
        diameter_point_lower=value.get('diameter_point_lower'),
        maximum_radius=value.get('maximum_radius'), current_height=value.get('current_height'),
        farthest_radius_witness_scope='recorded maximum-radius witness; not asserted active for max(2, 2|H|, 2radius)',
        current_full_point_sha256=value.get('current_full_point_sha256'),
        K_worst=address(value.get('worst')), farthest_radius_witness=address(value.get('farthest')),
        body_candidates=all_candidates(amplitude.get('radius_working_candidates')),
        paired_distance_candidates=all_candidates(amplitude.get('distance_working_candidates')),
        paired_distance_candidate_is_individual_sign_argmax=False,
        all_permanent_read=value.get('all_permanent_curvature_and_radius_locations_read'),
        both_witness_signs_read=value.get('both_witness_signs_read_at_every_point'),
        permanent_curvature_locations=value.get('permanent_curvature_locations'),
        permanent_radius_locations=value.get('permanent_radius_locations'),
        error_type=value.get('error_type'), error=value.get('error'))


def classify_trial(value, *, phase, direction_index, profile, objective_key, reader):
    geometry = family_geometry(value.get('full_geometry'))
    statistics = reader.statistic(value.get('statistics'), profile)
    failures, unread = [], []
    if value.get('actual_read_error') is not None:
        failures.append('actual_read_exception')
    if value.get('domain_feasible') is False:
        failures.append('metric_domain')
    elif value.get('domain_feasible') is not True:
        unread.append('metric_domain')
    if phase == 'metric':
        if value.get('actual_Phi_descent') is False:
            failures.append('same_objective_descent')
        elif value.get('actual_Phi_descent') is not True:
            unread.append('same_objective_descent')
    if value.get('full_true_geometry_read') is not True or geometry['read'] is not True:
        unread.append('complete_true_geometry')
    elif geometry['complete'] is not True:
        failures.append('incomplete_true_geometry')
    failures.extend('positive_'+family for family in geometry['positive_families'])
    if geometry['read']:
        unread.extend('geometry_family_'+name for name in geometry['missing_family_values'])
        if geometry['all_permanent_read'] is not True:
            unread.append('all_permanent_positions')
        if geometry['both_witness_signs_read'] is not True:
            unread.append('both_witness_signs')
    return dict(phase=phase, direction_index=direction_index, index=value['index'],
        alpha=value['alpha'], accepted=value['accepted'],
        domain_feasible=value.get('domain_feasible'),
        actual_Phi_descent=value.get('actual_Phi_descent'),
        Phi=None if statistics is None else statistics['Phi'],
        max_relative_gram=None if statistics is None else statistics['max_relative_gram'],
        objective_key=objective_key, actual_positive_physical_g=value.get('actual_positive_physical_g'),
        physically_feasible=value.get('physically_feasible'),
        full_true_geometry_read=value.get('full_true_geometry_read'),
        actual_read_error=value.get('actual_read_error'),
        actual_seconds=value.get('actual_seconds'),
        failure_classes=failures, unperformed_or_missing_checks=unread,
        geometry=geometry)


def small_location(value):
    if value is None:
        return None
    if value.get('complete_literal_address') is not True:
        return value
    return {key: value[key] for key in
        ('cell', 'u_binary64_hex', 'phi_binary64_hex', 'branch') if key in value}


def trial_summaries(value):
    g = value['geometry']
    families = dict(phase=value['phase'], direction=value['direction_index'],
        trial=value['index'], alpha=value['alpha'], accepted=value['accepted'],
        domain=value['domain_feasible'], Phi_descent=value['actual_Phi_descent'],
        Phi=value['Phi'], complete=g['complete'], g=g['maximum_physical_g'],
        families=g['family_g'], failures=value['failure_classes'],
        missing=value['unperformed_or_missing_checks'])
    locations = dict(phase=value['phase'], direction=value['direction_index'],
        trial=value['index'], alpha=value['alpha'], accepted=value['accepted'],
        point_sha=g['current_full_point_sha256'],
        D_lower=g['diameter_point_lower'], radius=g['maximum_radius'], height=g['current_height'],
        K_worst=small_location(g['K_worst']), farthest_radius_witness=small_location(g['farthest_radius_witness']))
    for key, source in (('body_candidate', 'body_candidates'),
            ('paired_distance_candidate', 'paired_distance_candidates')):
        entries = g[source]
        locations[key] = None if not entries else dict(score=entries[0]['score'],
            location=small_location(entries[0]['location']))
    return families, locations


def read_all(repo, report_path, *, verify_final_bundle=False):
    reader, reader_record = bind_reader(repo)
    before = record(report_path)
    validated = reader.read_report(repo, report_path, verify_final_bundle=verify_final_bundle)
    if validated['report_sha256'] != before['sha256']:
        raise ValueError('The report changed during the original complete read')
    report = json.loads(Path(report_path).read_text())
    if sha(report_path) != before['sha256']:
        raise ValueError('The same raw report changed before scalar attribution')
    profile = validated['fixed_scalar_metric_identity_sha256']
    objective_key = report['selected_scalar_objective_key']
    directions, all_families, all_locations = [], [], []
    total_trials = 0
    for phase in ('metric', 'restoration'):
        originals = report.get(phase+'_directions', [])
        bound = validated['actual_'+phase+'_directions']
        if len(originals) != len(bound):
            raise ValueError('Do not omit an actual original direction')
        for index, (original, pure) in enumerate(zip(originals, bound)):
            if original['index'] != pure['index'] or original['phase'] != phase:
                raise ValueError('The actual direction identity changed between reads')
            trials = [classify_trial(value, phase=phase, direction_index=original['index'],
                profile=profile, objective_key=objective_key, reader=reader)
                for value in original['trials']]
            if len(trials) != pure['trial_count']:
                raise ValueError('Retain every actual trial, accepted or rejected')
            family_rows, location_rows = [], []
            for value in trials:
                family_row, location_row = trial_summaries(value)
                family_rows.append(family_row)
                location_rows.append(location_row)
            all_families.extend(family_rows)
            all_locations.extend(location_rows)
            total_trials += len(trials)
            direction_readout = dict(pure)
            direction_readout['trials'] = trials
            direction_readout['all_actual_trial_families_json'] = compact(family_rows)
            direction_readout['all_actual_trial_locations_json'] = compact(location_rows)
            directions.append(direction_readout)
    result = dict(schema=SCHEMA, reader_sha256=sha(__file__),
        original_complete_reader=reader_record,
        report=before, complete_original_validation_returned=True,
        actual_driver_sha256=validated['actual_driver_sha256'],
        actual_source_commit=validated['actual_source_commit'],
        github_run_id=validated['github_run_id'], scientific_report_complete=validated['complete'],
        model_identity_sha256=validated['model_identity_sha256'],
        fixed_scalar_metric_identity_sha256=profile,
        actual_initial_bundle_sha256=validated['actual_new_initial_bundle_sha256'],
        actual_final_bundle_sha256=validated['actual_final_bundle_sha256'],
        initial=validated['initial'], final=validated['final'],
        actual_same_objective_change=validated['actual_same_objective_change'],
        coordinate_norm=validated['coordinate_norm'],
        final_damping=validated['final_damping'],
        actual_operator_counts=validated['actual_operator_counts'],
        initial_position_counts=validated['initial_position_counts'],
        final_position_counts=validated['final_position_counts'],
        actual_direction_count=len(directions), actual_trial_count=total_trials,
        directions=directions,
        all_actual_trial_families_json=compact(all_families),
        all_actual_trial_locations_json=compact(all_locations),
        all_actual_direction_solvers_json=compact([{key: item.get(key) for key in (
            'phase', 'index', 'serial', 'accepted', 'accepted_alpha', 'damping',
            'damping_after', 'qp_status', 'actual_advances',
            'final_face_projected_gradient_norm', 'qp_tolerance', 'active_face_rows',
            'maximum_linear_violation', 'original_geometry_rows', 'amplitude_rows',
            'total_rows', 'row_cache_bytes', 'actual_QP_seconds',
            'actual_QP_operator_counts', 'actual_complete_direction_operator_counts',
            'trial_count')} for item in directions]),
        all_actual_trials_retained=True, missing_values_replaced_with_zero=False,
        failed_family_assumed_before_read=False,
        addresses_recomputed_or_reinterpreted=False,
        paired_distance_candidate_is_individual_sign_argmax=False,
        actual_initial_geometry=family_geometry(report.get('initial_geometry')),
        actual_final_geometry=family_geometry(report.get('final_geometry')),
        field_evaluations=0, J_evaluations=0, Jtranspose_evaluations=0,
        root_solves=0, geometry_scans=0, QP_solves=0,
        scientific_arrays_recomputed=False, raw_report_contents_written=False,
        continuous_metric_or_geometry_certified=False,
        no_other_run_trial_values_inherited=True)
    if sha(report_path) != before['sha256']:
        raise ValueError('The original report changed during pure attribution')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('repo', 'report', 'output'):
        parser.add_argument('--'+key, type=Path, required=True)
    parser.add_argument('--verify-final-bundle', action='store_true')
    args = parser.parse_args()
    require_actions()
    args.repo, args.output = args.repo.resolve(), args.output.resolve()
    if args.output.exists() or args.output == args.repo or args.repo in args.output.parents:
        raise ValueError('Use a fresh output outside the repository')
    result = read_all(args.repo, args.report, verify_final_bundle=args.verify_final_bundle)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.output.with_name(args.output.name+'.partial')
    temporary.write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    temporary.replace(args.output)
    print(compact(dict(event='actual_complete_trial_families_read',
        source_sha256=result['reader_sha256'], report_sha256=result['report']['sha256'],
        output=record(args.output), actual_directions=result['actual_direction_count'],
        actual_trials=result['actual_trial_count'], field_evaluations=0,
        J_evaluations=0, root_solves=0)), flush=True)


if __name__ == '__main__':
    main()
