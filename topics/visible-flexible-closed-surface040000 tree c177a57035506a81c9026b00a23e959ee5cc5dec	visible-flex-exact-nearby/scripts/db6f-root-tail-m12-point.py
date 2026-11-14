#!/usr/bin/env python3
"""A point lower bound for the exact finite M12 map of reviewed R21.

This deliberately binds one map and its reviewed fixed-g background. It does
not relax the older M8 command's input-checkpoint guard for arbitrary inputs.
The point formulas and interval arithmetic are imported without modification.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
NOTES = ROOT / 'notes'
EXPECTED = {
    'point': ('scripts/db6f-root-tail-metric-point.py',
              'cde5264c884d261450add564b818cd9f863937c703017f1bc4df9b2443b0f7cc'),
    'manifest': ('notes/2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json',
                 'cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104'),
    'geometry': ('notes/2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json',
                 '253179d585d4ac0e59206d4e579de5663943f126473668c45a3bbda665c9c8f2'),
    'packet': ('notes/2026-11-09-db6f-audit-transfer-lowmetric-final-m12-critical-r01.json',
               '791e3bfda7bac4f356f34718a9731e5db7cfe5dd402525261e4b123914523d59'),
    'whole': ('notes/2026-11-09-db6f-root-whole-metric-reach-m12-critical-r01-lowmetric.json',
              'f329aaea39722b02b48ce98fe11e4232ae2c60b57a94789b071dfb5c915f49c5'),
    'old_witness': ('notes/2026-11-09-db6f-root-tail-m8-point-metric-witness.json',
                    'ff72e2e79b9595deb560237c14149708d4b42fbee1f2a1e2762923682dc6c7c6'),
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--span', type=int, default=17148)
    ap.add_argument('--neighbor-spans', type=int, default=0)
    ap.add_argument('--threshold', default='2e-9')
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    if args.out.exists():
        raise FileExistsError(args.out)
    threshold = Q(args.threshold)
    assert threshold > 0 and args.neighbor_spans >= 0
    started = time.monotonic()
    paths = {key: ROOT / row[0] for key, row in EXPECTED.items()}
    for key, path in paths.items():
        assert sha(path) == EXPECTED[key][1], ('frozen input changed', key)
    data = {key: json.loads(path.read_text())
            for key, path in paths.items() if key != 'point'}
    old = data['old_witness']
    definitions = data['packet']['background_definition_hashes']
    assert definitions == old['background_definition_hashes'] and definitions
    for item in definitions.values():
        assert sha(ROOT / item['file']) == item['sha256']
    for name, digest in old['source_sha256'].items():
        assert sha(ROOT / 'scripts' / name) == digest
    manifest_sha = EXPECTED['manifest'][1]
    assert data['geometry']['tail_manifest_sha256'] == manifest_sha
    assert data['whole']['tail_manifest_sha256'] == manifest_sha
    assert data['whole']['geometry_sha256'] == EXPECTED['geometry'][1]
    assert data['packet']['finite_tail_manifest_sha256'] == manifest_sha
    assert data['packet']['new_manifest_sha256'] == manifest_sha
    assert data['packet']['old_manifest_sha256'] == old['manifest_sha256']
    assert data['packet']['all_other_parameters_identical'] is True
    assert data['whole']['separate_tail_metric_certificate']['packet_sha256'] == EXPECTED['packet'][1]

    spec = importlib.util.spec_from_file_location('db6f_m12_point_formula', paths['point'])
    point = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = point
    spec.loader.exec_module(point)
    primitive, calibrations = ROOT / old['primitive'], ROOT / old['calibrations']
    assert sha(primitive) == old['primitive_sha256']
    assert sha(calibrations) == old['calibrations_sha256']
    geom = point.stream.StreamingExactIntegratedTail(paths['manifest'])
    bg = point.supplier.supplier.Background(primitive, calibrations)
    assert bg.data['inputs'] == definitions
    assert geom.N == 18552 and 0 <= args.span < geom.N
    selected, checked = None, 0
    for index in range(max(0, args.span - args.neighbor_spans),
                       min(geom.N, args.span + args.neighbor_spans + 1)):
        for local in (Q(1, 4), Q(1, 2), Q(3, 4)):
            radius = geom.rq[index] + local * geom.lq[index]
            supplied, detail = point.supplier.point_enclosure(bg, radius, radius)
            w = point.I(float(supplied.lo), float(supplied.hi))
            for quarter in range(4):
                result = point.point_metric(geom, index, local, quarter, w)
                checked += 1
                if selected is None or result['relative_operator_lower'] > selected['relative_operator_lower']:
                    selected = {**result, 'background_point_detail': detail}
    lower = Q(selected['relative_operator_lower'])
    report = dict(
        status='exact-finite-R21-map-point-lower-bound-conditional-on-reviewed-background',
        script_sha256=sha(Path(__file__)),
        inputs={key: dict(file=row[0], sha256=row[1]) for key, row in EXPECTED.items()},
        source_sha256=old['source_sha256'],
        background_definition_hashes=definitions,
        primitive_sha256=sha(primitive), calibrations_sha256=sha(calibrations),
        center_span=args.span, neighbor_spans=args.neighbor_spans,
        checked_points=checked, selected_witness=selected,
        whole_actual_metric_error_lower_exact=str(lower),
        requested_lower_exact=str(threshold), requested_lower_proved=lower > threshold,
        whole_surface_upper_bound=False, fixed_g_convergence_gate_5_paid=False,
        README_complete=False,
        proof_scope='R21 identifies this exact finite tail in the closed map and the same fixed g. '
                    'Its full-height reflection and vertical translation preserve the metric. '
                    'At theta=q*pi/6 the rotating Fourier factors are exact 0 or +/-1; '
                    'the reviewed outward interval formula gives a point lower bound. '
                    'No new solution, whole-surface upper bound, or convergence is asserted.',
        seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False) + '\n')
    print(json.dumps(dict(checked_points=checked, span=selected['span'],
                         lower_display=float(lower), lower_exact=str(lower),
                         requested_lower_proved=lower > threshold)))


if __name__ == '__main__':
    main()
