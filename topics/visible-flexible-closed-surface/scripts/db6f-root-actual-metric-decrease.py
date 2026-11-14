#!/usr/bin/env python3
"""Exact comparison of one old-map lower bound and a new whole-map upper.

Analytic validity comes from the independently reviewed point and continuous
certificates. This script checks fixed-target bindings and scalar arithmetic;
it does not replace those proofs or claim convergence to an exact solution.
"""
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTES = ROOT/'notes'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    names = dict(
        old_geometry='db6f-root-flat17-common-cut-m8s32',
        new_geometry='db6f-root-flat17-common-cut-m12-critical-r01',
        old_bridge='db6f-root-exact-bridge', new_bridge='db6f-root-exact-bridge-m12',
        old_witness='db6f-root-tail-m8-point-metric-witness',
        new_whole='db6f-root-whole-metric-reach-m12-critical-r01-lowmetric',
        independent_new_whole='db6f-audit-whole-metric-reach-m12-critical-lowmetric',
        new_packet='db6f-audit-transfer-lowmetric-final-m12-critical-r01')
    paths = {key: NOTES/('2026-11-09-'+name+'.json') for key, name in names.items()}
    data = {key: json.loads(path.read_text()) for key, path in paths.items()}
    old, new = data['old_geometry'], data['new_geometry']
    geometry_equal = ['frozen_profile', 'chart', 'warp_reference_q', 'ell',
                      'profile_loader_sha256', 'profile_implementation_sha256']
    assert all(old[key] == new[key] for key in geometry_equal)
    bridge_equal = ['script_sha256', 'physical_cut_radius_exact',
                    'physical_cut_slope_exact', 'physical_cut_second_derivative_exact',
                    'exact_pt', 'exact_ps', 'exact_L', 'gap_at_left', 'gap_at_right',
                    'gap_derivative_lower_exact', 'unique_root_in_box',
                    'arclength_rescale', 'phase_upper']
    assert all(data['old_bridge'][key] == data['new_bridge'][key] for key in bridge_equal)
    assert data['old_bridge']['unique_root_in_box'] is True
    assert old['bridge_parameter_certificate_sha256'] == sha(paths['old_bridge'])
    assert new['bridge_parameter_certificate_sha256'] == sha(paths['new_bridge'])
    witness, whole = data['old_witness'], data['new_whole']
    assert witness['manifest_sha256'] == old['tail_manifest_sha256']
    assert whole['geometry_sha256'] == sha(paths['new_geometry'])
    assert whole['tail_manifest_sha256'] == new['tail_manifest_sha256']
    assert whole['separate_tail_metric_certificate']['packet_sha256'] == sha(paths['new_packet'])
    assert bool(witness['background_definition_hashes'])
    assert witness['background_definition_hashes'] == data['new_packet']['background_definition_hashes']
    for item in witness['background_definition_hashes'].values():
        assert sha(ROOT/item['file']) == item['sha256']
    exact_fields = [key for key, value in whole.items()
                    if isinstance(value, dict) and 'exact' in value]
    assert all(whole[key] == data['independent_new_whole'][key] for key in exact_fields)
    lower = Q(witness['selected_witness']['relative_operator_lower'])
    upper = Q(whole['whole_metric_operator_upper']['exact'])
    assert lower > Q('2.02348e-7') and upper < Q('2.57212e-8')
    assert upper*Q(393, 50) < lower
    assert Q(whole['whole_reach_over_diameter_lower']['exact']) > Q('0.0301447870162247')
    report = dict(
        status='PASS-fixed-target-and-exact-actual-error-decrease-comparison',
        script_sha256=sha(Path(__file__)),
        inputs={key: dict(file=str(path.relative_to(ROOT)), sha256=sha(path))
                for key, path in paths.items()},
        unchanged_prefix_definition_fields=geometry_equal,
        unchanged_exact_bridge_definition_and_unique_root_fields=bridge_equal,
        same_nonempty_tail_background_definition_hashes=True,
        independent_whole_exact_scalar_fields_equal=exact_fields,
        cap_metric_reason='R16 uses the same radius and bump functions; vertical translation '
                          'of each cap does not change its intrinsic metric.',
        old_whole_error_lower_exact=str(lower),
        new_whole_error_upper_exact=str(upper),
        ratio_old_lower_over_new_upper_exact=str(lower/upper),
        ratio_display_approx=float(lower/upper),
        new_actual_error_strictly_less_than_old_actual_error_divided_by='393/50',
        old_error_exceeds_decimal='2.02348e-7',
        new_error_below_decimal='2.57212e-8',
        fixed_g_convergence_gate_5_paid=False, README_complete=False,
        proof_scope='Composes reviewed old-point lower and new-whole upper certificates. '
                    'The exact finite maps differ and both target the same fixed metric. '
                    'One strict refinement improvement is not an infinite convergence theorem.')
    output = NOTES/'2026-11-09-db6f-root-actual-metric-decrease.json'
    output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({key: report[key] for key in
                     ['status', 'ratio_display_approx', 'new_error_below_decimal', 'README_complete']}))


if __name__ == '__main__':
    main()
