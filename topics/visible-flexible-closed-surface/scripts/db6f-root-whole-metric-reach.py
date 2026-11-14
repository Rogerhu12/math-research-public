#!/usr/bin/env python3
"""Exact scalar closure of reviewed whole-surface metric and reach bounds.

This program composes certificates for one explicitly identified finite map.
The analytic validity and independent review of their inputs are separate
proof dependencies. No fixed-g convergence or README completion is inferred.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def check(ok, message):
    if not ok:
        raise ValueError(message)


def resolve(parent, name):
    p = Path(name)
    if p.exists():
        return p
    p = parent/Path(name).name
    check(p.exists(), 'Missing bound input: '+name)
    return p


def record(q):
    q = Q(q)
    f = float(q)
    lo = math.nextafter(f, -math.inf) if Q(f) > q else f
    hi = math.nextafter(f, math.inf) if Q(f) < q else f
    return {'exact': str(q), 'lower_display': lo, 'upper_display': hi}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for key in ['closed-budget', 'tail-certificate', 'out']:
        ap.add_argument('--'+key, type=Path, required=True)
    args = ap.parse_args()
    budget = json.loads(args.closed_budget.read_text())
    tail = json.loads(args.tail_certificate.read_text())
    inputs = {}
    for key, item in budget['inputs'].items():
        p = resolve(args.closed_budget.parent, item['file'])
        check(sha(p) == item['sha256'], 'Changed closed-map input: '+key)
        inputs[key] = p
    meta = json.loads(inputs['geometry'].read_text())
    geometry = json.loads(inputs['geometry_certificate'].read_text())
    check(geometry['geometry_sha256'] == sha(inputs['geometry']),
          'Prefix geometry certificate belongs to another map')
    check(meta['tail_manifest_sha256'] == tail['manifest_sha256'],
          'Tail curvature belongs to another finite map')
    manifest = resolve(args.tail_certificate.parent, tail['manifest'])
    check(sha(manifest) == tail['manifest_sha256'], 'Changed finite tail manifest')
    packet = resolve(args.tail_certificate.parent, tail['packet'])
    check(sha(packet) == tail['packet_sha256'], 'Changed background packet')
    packet_meta = json.loads(packet.read_text())
    check(packet_meta['finite_tail_manifest_sha256'] == tail['manifest_sha256'],
          'Background packet belongs to another grid')
    data = resolve(packet.parent, packet_meta['data_file'])
    check(sha(data) == packet_meta['data_sha256'] == tail['packet_data_sha256'],
          'Changed background packet arrays')
    rows = resolve(args.tail_certificate.parent, tail['row_data_file'])
    check(sha(rows) == tail['row_data_sha256'], 'Changed continuous tail rows')
    check(tail['entire_finite_tail_and_collar_covered'] is True and
          tail['collar_included'] is True and
          tail['checked_packet_intervals'] == tail['packet_intervals'] and
          tail['curvature_all_checked_intervals_resolved'] is True and
          tail['metric_immersion_certified_on_checked_intervals'] is True,
          'Incomplete continuous tail proof')
    check(budget['embedding_all_phases_follows_from_support_given_reviewed_assembly'] and
          budget['rigid_noncongruence_follows_from_moment_given_reviewed_assembly'],
          'Closed-map assembly hypotheses fail')
    # The cap curvature 10/3 is the separately proved R16 exact polynomial
    # graph bound. The cap target is its own fixed induced metric.
    prefix_metric = Q(budget['corrected_prefix_exact_target_metric_upper']['exact'])
    tail_metric = Q(tail['metric_operator_upper'])
    prefix_curvature = Q(geometry['principal_curvature_upper'])
    tail_curvature = Q(tail['principal_curvature_upper'])
    cap_curvature = Q(10, 3)
    metric = max(prefix_metric, tail_metric, Q(0))
    curvature = max(prefix_curvature, tail_curvature, cap_curvature)
    support = Q(budget['whole_surface_support_lower']['exact'])
    diameter = Q(budget['diameter_upper']['exact'])
    check(support > 0 and diameter > 0 and curvature > 0, 'Invalid global bounds')
    reach = min(support, 1/curvature)
    reach_ratio = reach/diameter
    held = Q(budget['held_region_diameter_lower']['exact'])
    displacement_ratio = Q(budget['hold_over_diameter_lower']['exact'])
    check(metric <= Q(1, 10**6), 'Whole metric threshold fails')
    check(reach_ratio >= Q(3, 100), 'Whole reach threshold fails')
    check(held >= diameter/5 and displacement_ratio >= Q(1, 20),
          'Held-region or displacement threshold fails')
    check(Q(budget['unmarked_volume_moment_real_lower']['exact']) > 0 and
          Q(budget['centered_third_tensor_norm_squared_change_lower']['exact']) > 0,
          'Strict Euclidean noncongruence input fails')
    report = {
        'status': 'exact-scalar-whole-finite-map-threshold-closure-pending-independent-review',
        'script_sha256': sha(__file__),
        'closed_budget': str(args.closed_budget), 'closed_budget_sha256': sha(args.closed_budget),
        'tail_certificate': str(args.tail_certificate), 'tail_certificate_sha256': sha(args.tail_certificate),
        'geometry_sha256': sha(inputs['geometry']), 'tail_manifest_sha256': sha(manifest),
        'packet_sha256': sha(packet), 'packet_data_sha256': sha(data),
        'tail_rows_sha256': sha(rows),
        'prefix_metric_upper': record(prefix_metric), 'tail_metric_upper': record(tail_metric),
        'whole_metric_operator_upper': record(metric),
        'prefix_curvature_upper': record(prefix_curvature),
        'tail_curvature_upper': record(tail_curvature), 'cap_curvature_upper': record(cap_curvature),
        'whole_principal_curvature_upper': record(curvature),
        'whole_support_lower': record(support), 'diameter_upper': record(diameter),
        'whole_reach_lower_by_R10': record(reach), 'whole_reach_over_diameter_lower': record(reach_ratio),
        'held_region_diameter_over_diameter_lower': record(held/diameter),
        'hold_over_diameter_lower': record(displacement_ratio),
        'all_phases_by_R17_rotation_and_material_action': True,
        'README_geometric_and_metric_thresholds_1_2_3_4_6_paid_given_reviewed_inputs': True,
        'fixed_g_convergence_gate_5_paid': False, 'final_mesh_delivery_paid': False,
        'README_complete': False,
        'proof_dependencies': [
            'R17 actual common-cut C2 closed map, held set, embedding and moment noncongruence',
            'R16 fixed cap curvature and metric definition',
            'R10 positive support and actual curvature imply global reach',
            'Reviewed exact finite-source background, alpha, primitive and polynomial suppliers',
            'Reviewed complete packet assembly and continuous finite-tail metric/curvature formulas',
            'Separate independent full replays of all bound certificate components']}
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({key: report[key] for key in
                     ['whole_metric_operator_upper', 'whole_principal_curvature_upper',
                      'whole_reach_over_diameter_lower', 'README_complete']}, indent=2))


if __name__ == '__main__':
    main()
