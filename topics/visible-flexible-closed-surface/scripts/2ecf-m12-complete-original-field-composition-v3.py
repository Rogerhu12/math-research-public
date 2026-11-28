#!/usr/bin/env python3
"""Compose one actual original-g closed field's complete metric and geometry.

This does not solve or sample a new field.  It takes the maximum of complete
same-field continuous regions, then uses the established R17/R21/R226/R253
closed-map, phase-orbit and fixed-metric refinement results.  Recomputable
receipts and meshes stay outside the repository.
"""
import argparse
import hashlib
import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path


FIELD = '5778bee4c19c6f878e2039876a9b250e940b7b4d0d9f949b1982bf6cebf5a5b8'
B = F(1, 500000000)
L12 = F(370012576184137, 18889465931478580854784)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def require(value, message):
    if not value:
        raise ValueError(message)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('scripts', 'data', 'grid', 'field', 'result', 'correction-bounds',
                'prefix', 'prefix-transfer', 'tail', 'two-jet', 'geometry', 'mesh-manifest', 'out'):
        parser.add_argument('--' + key, type=Path, required=True)
    args = parser.parse_args()
    require(not args.out.exists(), 'Use a new composition output')
    inputs = {key: sha(getattr(args, key))
              for key in ('data', 'grid', 'field', 'result', 'correction_bounds')}
    require(inputs['field'] == FIELD, 'This composition is for the declared actual G12 field')
    result = read(args.result)
    correction = read(args.correction_bounds)
    prefix, tail = read(args.prefix), read(args.tail)
    prefix_transfer = read(args.prefix_transfer)
    two, geometry = read(args.two_jet), read(args.geometry)
    mesh = read(args.mesh_manifest)

    for flag in ('original_exact_metric_unchanged', 'true_flat_cuff_included',
                 'full_half_including_finite_tail_and_deep_collar',
                 'finite_space_at_least_C2', 'full_declared_knots_consumed'):
        require(result[flag], 'Actual source or complete C2 space missing: ' + flag)
    require(not result['source'].get('source_regularization')
            and not result.get('source_regularization'), 'The actual source must remain Q-free')
    require(correction['script_sha256'] ==
            '81003432a6823b3c86859be226c9a099012ed7fa21e46165ac12091d86727e80',
            'The original R226 two-jet/central-reference proof is required')
    require(correction['continuous_all_knots_and_all_angles']
            and all(correction['exact_zero_endpoint_jets'])
            and correction['relative_to_original_exact_common_cut_baseline']
            and correction['central_reference_change_included'],
            'Original source and exact endpoint two-jets must be retained')

    prefix_keys = {'data': 'data_sha256', 'grid': 'grid_sha256',
                   'field': 'field_sha256', 'result': 'solver_result_sha256',
                   'correction_bounds': 'correction_bounds_sha256'}
    for key, expected in inputs.items():
        require(prefix[prefix_keys[key]] == expected and tail['inputs'][key] == expected,
                'Continuous regions belong to different actual fields: ' + key)
    require(prefix['complete_original_prefix'] and prefix['complete_elements'] == 158
            and prefix['all_elements_below_B'], 'Complete original prefix is required')
    require(tail['true_whole_tail_covered'] and tail['all_original_finite_source_cells_covered']
            and tail['finite_source_cells_covered'] == 18552
            and tail['finite_source_ranges'] == [[0, 18552]]
            and not tail['missing_source_ranges']
            and tail['same_actual_field_original_source_and_g']
            and tail['all_angles_and_original_phase_orbit'],
            'Complete original finite tail and true inner collar are required')
    require(F(prefix['requested_B_exact']) == B, 'Original solver tolerance differs')
    up_proxy = F(prefix['maximum_relative_metric_upper_exact'])
    up = F(prefix_transfer['actualEntirePrefixGramUpper'])
    ut = F(tail['tail_metric_upper_exact'])
    upper = max(up, ut)  # the central trace, unchanged cuffs and fixed caps have zero error
    require(0 <= upper <= B, 'The actual full field has not reached the original tolerance')

    notes = args.scripts.parent / 'notes'
    meta_path = notes / '2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json'
    bridge_path = notes / '2026-11-09-db6f-root-exact-bridge-m12.json'
    manifest_path = notes / '2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json'
    require(prefix['meta_sha256'] == sha(meta_path) == correction['common_meta_sha256'],
            'The common exact metric differs')
    require(prefix['bridge_sha256'] == sha(bridge_path) == correction['bridge_sha256'],
            'The original exact bridge differs')
    require(tail['manifest_sha256'] == sha(manifest_path) == correction['tail_manifest_sha256'],
            'The original finite tail differs')
    meta, bridge, manifest = read(meta_path), read(bridge_path), read(manifest_path)
    profile = meta['frozen_profile']
    offset = sum(F(profile['delta']) / (F(profile[v]) * (1-F(profile['ramp'])))
                 for v in ('vu', 'vd'))
    slo, shi = [offset + F(bridge['exact_L'][edge]) for edge in ('lo', 'hi')]
    width = F(.6) - F(.15)
    require(list(map(F, prefix['common_q_endpoint_interval'])) == [slo, shi]
            and list(map(F, prefix['common_z_endpoint_interval'])) ==
            [slo/(slo+width), shi/(shi+width)], 'Prefix/common-tail interface differs')
    transfer_source = args.scripts / '2ecf-m12-prefix-actual-cuff-length-transfer.py'
    require(sha(transfer_source) == prefix_transfer['entrySHA256'] ==
            'cf4242f7483d5141c70cb6707cb96335ef61981bb929d8a2b538eb887334be62'
            and prefix_transfer['prefixSHA256'] == sha(args.prefix)
            and prefix_transfer['correctionSHA256'] == inputs['correction_bounds']
            and prefix_transfer['manifestSHA256'] == sha(manifest_path),
            'The exact original-cuff chart transfer differs')
    spec = importlib.util.spec_from_file_location('actual_cuff_prefix_transfer', transfer_source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    transfer_values = module.transfer(prefix, correction, manifest)
    require(all(prefix_transfer[key] == value for key,value in transfer_values.items()),
            'The complete exact rational chart transfer was not retained')
    cut, cuff = [F.from_float(manifest['parameters'][key]) for key in ('rCut','rCuff')]
    require(cut == F(manifest['radialGeometry']['outerAnchor']) == F(.6)
            and cuff == F(prefix_transfer['actualCuff'])
            and list(map(F,prefix_transfer['actualCommonCutUnitInterval'])) ==
            [slo/(slo+cut-cuff), shi/(shi+cut-cuff)]
            and up == up_proxy + F(prefix_transfer['relativeGramPerturbationUpper']),
            'The actual prefix and tail must use the same original physical chart')

    geometry_keys = {'grid': 'grid_sha256', 'field': 'field_sha256',
                     'result': 'solver_result_sha256',
                     'correction_bounds': 'correction_receipt_sha256'}
    for key, name in geometry_keys.items():
        require(two[name] == inputs[key] and geometry[name] == inputs[key],
                'Geometry belongs to a different actual field: ' + key)
    require(geometry['actual_two_jet_report_sha256'] == sha(args.two_jet)
            and geometry['script_sha256'] ==
            '0b62fcd84c7e19155197d6a2719ecd7484ecf515ca5f469fe4d56e52ea921296',
            'The complete same-field R253 geometry is required')
    for flag in ('same_original_Q_free_source_and_g', 'same_actual_saved_field_no_refit',
                 'all_prefix_spans_and_all_angles_continuously_covered',
                 'tail_uses_complete_inherited_global_p',
                 'entire_phase_interval_by_original_orbit_structure',
                 'whole_geometry_conditions'):
        require(geometry[flag], 'Whole geometry premise missing: ' + flag)
    quantities = geometry['rational_quantities']
    diameter = F(quantities['diameter']['upper_exact'])
    curvature = F(quantities['whole_curvature']['upper_exact'])
    reach_ratio = F(quantities['reach_over_D']['lower_exact'])
    held_ratio = F(quantities['held_over_D']['lower_exact'])
    support = F(quantities['support']['lower_exact'])
    fixed_ratio = F(two['rational_quantities']['fixed_cap_diameter_ratio']['lower_exact'])
    activity_loss = F(two['rational_quantities']['activity_third_moment_loss']['upper_exact'])
    require(reach_ratio == 1/(curvature*diameter) and reach_ratio >= F(3,100)
            and held_ratio >= F(1,20) and fixed_ratio >= F(1,5)
            and support > 1/curvature and activity_loss < F(44016,100000),
            'The actual complete geometric inequalities are insufficient')

    for key, name in (('data','dataSHA256'), ('grid','gridSHA256'),
                      ('field','fieldSHA256'), ('result','resultSHA256')):
        require(mesh[name] == inputs[key], 'Mesh belongs to a different field: ' + key)
    require(mesh['continuousRegionalGeometryReportSHA256'] == sha(args.geometry)
            and mesh['sameOriginalMetricAndSameSavedField']
            and mesh['completeCentralPrefixBridgeFiniteTailDeepCollarAndBothCaps']
            and mesh['fixedCapsBitwiseIdenticalInSerializedFloat32'],
            'Actual complete same-field mesh receipt is required')
    require(mesh['topology']['EulerCharacteristic'] == 2
            and mesh['topology']['allEdgesHaveTwoOppositeIncidences']
            and mesh['topology']['allVerticesUsed']
            and mesh['topology']['connectedBySuccessiveRingStripsAndBothPoleFans'],
            'Actual closed connected mesh topology differs')
    require({F(row['timeExact']) for row in mesh['meshFiles']} == {F(0),F(1,4),F(1,2)},
            'The declared three actual phases differ')
    for row in mesh['meshFiles']:
        path = args.mesh_manifest.parent / row['file']
        require(path.stat().st_size == row['bytes'] < 5000000 and sha(path) == row['sha256'],
                'Saved mesh bytes differ: ' + row['file'])

    require(L12 > F(195883,20000)*B >= F(195883,20000)*upper,
            'The original exact actual-decrease comparison failed')
    output = {
        'schema': '2ecf-original-G12-whole-closed-field-continuous-composition-v3',
        'script_sha256': sha(__file__), 'inputs': inputs,
        'receipts': {key:sha(getattr(args,key)) for key in
                     ('prefix','prefix_transfer','tail','two_jet','geometry','mesh_manifest')},
        'complete_original_prefix': True, 'complete_original_finite_tail': True,
        'complete_true_inner_collar': True,
        'central_trace_fixed_cuffs_and_caps_by_original_exact_identity': True,
        'continuous_C2_original_ports_and_saved_C2_correction': True,
        'whole_phase_interval_by_original_orbit_with_pointwise_fixed_caps': True,
        'same_original_exact_g_and_physical_parameters': True,
        'prefix_proxy_upper_exact': str(up_proxy),
        'prefix_actual_original_cuff_chart_transferred': True,
        'prefix_upper_exact': str(up), 'tail_upper_exact': str(ut),
        'whole_relative_metric_upper_exact': str(upper),
        'whole_relative_metric_upper_display': float(upper),
        'original_solver_tolerance_exact': str(B),
        'below_original_solver_tolerance': True,
        'old_actual_M12_lower_exact': str(L12),
        'certified_actual_decrease_exceeds': '195883/20000',
        'original_actual_M8_M12_h_frequency_sequence_used': True,
        'refinement_source': 'notes/2026-11-10-78718-fixed-g-refinement-composition.md',
        'diameter_upper_exact': str(diameter),
        'reach_over_D_lower_exact': str(reach_ratio),
        'held_over_D_lower_exact': str(held_ratio),
        'diamH_over_D_lower_exact': str(fixed_ratio),
        'noncongruence_including_reflections_by_original_activity_transfer': True,
        'meshes': mesh['meshFiles'],
        'base_README_numerical_conditions_composed': True,
        'exact_isometry_existence_proved': False,
        'infinite_refinement_C2_limit_proved': False,
        'stronger_proportion_targets_completed': False,
        'mesh_existing_historical_false_refinement_flags_not_rewritten': True,
    }
    args.out.write_text(json.dumps(output, indent=2, allow_nan=False)+'\n')
    print(json.dumps({'output':str(args.out),'sha256':sha(args.out),
                      'whole_metric_upper':float(upper),'reach_over_D':float(reach_ratio),
                      'held_over_D':float(held_ratio),'base_numerical_composition':True}))


if __name__ == '__main__':
    main()
