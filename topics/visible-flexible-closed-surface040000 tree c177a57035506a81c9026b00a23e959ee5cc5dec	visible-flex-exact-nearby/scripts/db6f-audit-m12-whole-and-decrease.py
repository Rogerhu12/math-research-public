#!/usr/bin/env python3
"""Independent finite-file/Fraction audit of the M12 whole-map descent claim.

This rederives scalar closure and checks the actual fixed target identities.
It uses the independently reviewed geometric, interval and point certificates
as inputs; it neither solves the BVP nor claims fixed-g convergence to zero.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
NOTES = TOPIC/'notes'


def check(ok, message):
    if not ok:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def locate(path):
    p = Path(path)
    return p if p.exists() else NOTES/p.name


def exact(record):
    return Q(record['exact'])


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--proof', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    stems = dict(old_geometry='root-flat17-common-cut-m8s32',
        new_geometry='root-flat17-common-cut-m12-critical-r01',
        old_bridge='root-exact-bridge', new_bridge='root-exact-bridge-m12',
        witness='root-tail-m8-point-metric-witness',
        new_metric='audit-tail-m12-critical-lowmetric-full',
        old_curvature='audit-tail-m12-critical-tight-full',
        new_budget='root-closed-budget-m12-critical-r01',
        root_whole='root-whole-metric-reach-m12-critical-r01-lowmetric',
        peer_whole='audit-whole-metric-reach-m12-critical-lowmetric',
        author_comparison='root-actual-metric-decrease')
    paths = {k: NOTES/('2026-11-09-db6f-'+v+'.json') for k, v in stems.items()}
    data = {k: json.loads(p.read_text()) for k, p in paths.items()}
    old, new = data['old_geometry'], data['new_geometry']
    prefix_fields = ['frozen_profile', 'chart', 'warp_reference_q', 'ell',
                     'profile_loader_sha256', 'profile_implementation_sha256']
    for key in prefix_fields:
        check(old[key] == new[key], 'Different exact prefix definition '+key)
    bridge_fields = ['script_sha256', 'physical_cut_radius_exact', 'physical_cut_slope_exact',
                     'physical_cut_second_derivative_exact', 'exact_pt', 'exact_ps', 'exact_L',
                     'gap_at_left', 'gap_at_right', 'phase_upper', 'gap_derivative_lower_exact',
                     'unique_root_in_box', 'arclength_rescale', 'uniform_radius_difference_upper',
                     'relative_target_metric_difference_upper']
    for key in bridge_fields:
        check(data['old_bridge'][key] == data['new_bridge'][key], 'Different exact bridge definition '+key)
    check(data['old_bridge']['unique_root_in_box'] is True, 'Root uniqueness missing')
    manifests = []
    for label, geometry in [('old', old), ('new', new)]:
        bridge_path, bridge = paths[label+'_bridge'], data[label+'_bridge']
        check(geometry['bridge_parameter_certificate_sha256'] == sha(bridge_path), 'Unbound bridge certificate')
        check(sha(locate(geometry['bridge_parameter_certificate'])) == sha(bridge_path), 'Different bridge path contents')
        check(bridge['geometry_sha256'] == geometry['base_geometry_sha256'], 'Bridge refers to a different source prefix')
        manifest_path = locate(geometry['tail_manifest'])
        check(sha(manifest_path) == geometry['tail_manifest_sha256'], 'Changed tail manifest')
        manifest = json.loads(manifest_path.read_text())
        check(Q(manifest['parameters']['rCut']) == Q(bridge['physical_cut_radius_exact'])
              and Q(manifest['parameters']['wCut']) == Q(bridge['physical_cut_slope_exact']), 'Different physical cut')
        manifests.append(manifest)
    # The actual two manifests change only these already reviewed numerical
    # controls. An unknown physical or numerical difference rejects here.
    numerical_changes = {'auditSteps', 'depth', 'farPadding', 'initialCheckpoint', 'maxIterations',
                         'modes', 'physicalDepth', 'quadrature', 'shootingParts', 'steps', 'traceFile'}
    p0, p1 = [m['parameters'] for m in manifests]
    changed = {key for key in set(p0)|set(p1) if p0.get(key) != p1.get(key)}
    check(changed <= numerical_changes, 'An unreviewed parameter changed')
    for k in ['rCut', 'rCuff', 'wCut', 'calibrationSteps', 'protectCell']:
        check(p0[k] == p1[k], 'Changed background parameter '+k)
    metric, curvature, witness = data['new_metric'], data['old_curvature'], data['witness']
    check(metric['manifest_sha256'] == curvature['manifest_sha256'] == new['tail_manifest_sha256'],
          'The new metric and curvature concern different maps')
    check(witness['manifest_sha256'] == old['tail_manifest_sha256'], 'Old lower witness belongs to another map')
    packets = []
    for report in [metric, curvature]:
        path = locate(report['packet'])
        check(sha(path) == report['packet_sha256'], 'Changed bound packet')
        packet = json.loads(path.read_text())
        payload = locate(packet['data_file'])
        check(sha(payload) == packet['data_sha256'] == report['packet_data_sha256'], 'Changed packet array data')
        rows = locate(report['row_data_file'])
        check(sha(rows) == report['row_data_sha256'], 'Changed completed rows')
        check(report['entire_finite_tail_and_collar_covered'] is True
              and report['collar_included'] is True
              and report['checked_packet_intervals'] == report['packet_intervals'], 'Incomplete tail certificate')
        packets.append(packet)
    definitions = witness['background_definition_hashes']
    check(isinstance(definitions, dict) and definitions and
          definitions == packets[0]['background_definition_hashes'] == packets[1]['background_definition_hashes'],
          'Different exact background definitions')
    for name, item in definitions.items():
        check(sha(locate(item['file'])) == item['sha256'], 'Changed exact background dependency '+name)
    budget = data['new_budget']
    for key, item in budget['inputs'].items():
        check(sha(locate(item['file'])) == item['sha256'], 'Changed closed-map input '+key)
    check(budget['inputs']['geometry']['sha256'] == sha(paths['new_geometry']), 'Closed budget belongs to another map')
    geometry_report = json.loads(locate(budget['inputs']['geometry_certificate']['file']).read_text())
    eps_p = exact(budget['corrected_prefix_exact_target_metric_upper'])
    eps_t = Q(metric['metric_operator_upper'])
    eps = max(eps_p, eps_t, Q(0))
    K = max(Q(geometry_report['principal_curvature_upper']), Q(curvature['principal_curvature_upper']), Q(10, 3))
    sigma, D = exact(budget['whole_surface_support_lower']), exact(budget['diameter_upper'])
    reach = min(sigma, 1/K)/D
    check(eps == eps_p and eps_t == Q(7055251261315967, 302231454903657293676544), 'Unexpected continuous metric upper')
    check(K == Q(4763997235009095, 562949953421312) and sigma > 1/K, 'Unexpected reach inputs')
    check(D == Q(98, 25) and reach == Q(1407374883553280, 46687172903089131), 'Incorrect diameter/reach combination')
    decimal_lower_claims = {
        'whole_surface_support_lower': '.7370435198982138',
        'held_region_diameter_lower': '3.542609695989968',
        'hausdorff_hold_lower': '.1998911434256142',
        'hold_over_diameter_lower': '.0509926386289832',
        'unmarked_volume_moment_real_lower': '.4401644538270965',
        'centered_third_tensor_norm_squared_change_lower': '2.281812528639668e-10'}
    for key, bound in decimal_lower_claims.items():
        check(exact(budget[key]) > Q(bound), 'Unsafe displayed lower bound '+key)
    check(eps < Q('2.57212e-8') and K < Q('8.462560') and reach > Q('.0301447870162247'), 'Unsafe whole-map threshold')
    selected = witness['selected_witness']
    check(selected['span'] == 4304 and selected['local_exact'] == '1/2'
          and selected['angle_multiple_of_pi_over_six'] == 2
          and Q(selected['radius_exact']) == Q(15658549336557037, 36028797018963968), 'Unexpected old-map witness')
    L = Q(selected['normalized_component_intervals'][0][0])
    check(L > 0 and L == Q(selected['relative_operator_lower']), 'The old lower bound is not its radial diagonal lower')
    check(L > Q('2.02348e-7') and Q(393, 50)*eps < L, 'No strict actual-error separation')
    recomputed = dict(whole_metric_operator_upper=eps, whole_principal_curvature_upper=K,
                      whole_reach_over_diameter_lower=reach)
    for key, value in recomputed.items():
        check(exact(data['root_whole'][key]) == exact(data['peer_whole'][key]) == value,
              'Independent whole-map recombination differs '+key)
    comparison = data['author_comparison']
    check(Q(comparison['old_whole_error_lower_exact']) == L
          and Q(comparison['new_whole_error_upper_exact']) == eps
          and Q(comparison['ratio_old_lower_over_new_upper_exact']) == L/eps, 'Author comparison differs')
    result = dict(status='PASS-independent-fixed-target-whole-map-and-actual-decrease-arithmetic',
        scope=__doc__, script_sha256=sha(__file__), proof=str(args.proof), proof_sha256=sha(args.proof),
        inputs={key: dict(file=str(path), sha256=sha(path)) for key, path in paths.items()},
        unchanged_prefix_fields=prefix_fields, unchanged_bridge_fields=bridge_fields,
        actual_changed_tail_parameters=sorted(changed), same_nonempty_background_definitions=definitions,
        recomputed_exact={key: str(value) for key, value in recomputed.items()},
        old_point_radial_diagonal_lower_exact=str(L), new_tail_metric_upper_exact=str(eps_t),
        strict_actual_error_ratio_exact=str(L/eps), safe_improvement_factor_exact='393/50',
        all_printed_strict_decimal_thresholds_verified=True,
        old_curvature_certificate_retained_without_modification=True,
        full_Fourier_Bernstein_recomputed_here=False,
        fixed_g_convergence_gate_5_paid=False, final_independent_end_to_end_completed=False)
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(status=result['status'], safe_improvement_factor='393/50',
                         whole_metric_bound_approx=float(eps), reach_ratio_bound_approx=float(reach))))


if __name__ == '__main__':
    main()
