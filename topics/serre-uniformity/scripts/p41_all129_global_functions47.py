#!/usr/bin/env python3
"""Assemble real center constants and global QC polynomials, retaining gaps.

Each new ordinary input is accepted only with its completed signed actual
multiplication and independently checked formal logarithm.  This program
does not manufacture local Poincare heights or common-root certificates.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys

Q = 47**4
Q3 = 47**3


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def save(path, data):
    raw = (json.dumps(data, sort_keys=True, separators=(',', ':'))+'\n').encode()
    tmp = path.with_suffix(path.suffix+'.new')
    tmp.write_bytes(gzip.compress(raw, mtime=0))
    tmp.replace(path)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir', type=Path, required=True)
    ap.add_argument('--known113', type=Path, required=True)
    ap.add_argument('--tiny', type=Path, required=True)
    ap.add_argument('--polynomials', type=Path, required=True)
    ap.add_argument('--ordinary-workdir', type=Path, action='append', required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    sys.path.insert(0, str(args.script_dir.resolve()))
    from p41_three_ordinary_CM_anchors47 import global_series
    known, tiny, poly = [read(p) for p in (args.known113, args.tiny, args.polynomials)]
    assert known['complete_113_actual_global_QC_polynomials']
    assert tiny['complete_all129_tiny_Abel_integrals'] and poly['complete_global_polynomials']
    assert known['input_sha256'][args.tiny.name] == sha(args.tiny)
    assert known['input_sha256'][args.polynomials.name] == sha(args.polynomials)
    expected = known['remaining16_ordinary_center_constant_disk_ids']
    points = {r['disk_id']: r for r in known['actual_113_rational_disk_global_polynomials']}
    charts = {}
    for ch in tiny['charts']:
        for row, disk_id in enumerate(ch['disk_ids']):
            charts[disk_id] = (ch, row)
    assert len(charts) == 129 and len(points) == 113 and len(expected) == 16
    inputs = {p.name: sha(p) for p in (args.known113, args.tiny, args.polynomials)}
    missing, accepted = [], []
    for disk_id in expected:
        matches = [directory/(disk_id+'_Abel47.json.gz') for directory in args.ordinary_workdir
                   if (directory/(disk_id+'_Abel47.json.gz')).exists()]
        if not matches:
            missing.append(disk_id)
            continue
        path = matches[0]
        data = read(path)
        assert data['disk_id'] == disk_id and data['complete_actual_center_Abel_constant']
        assert data['all54_cyclic_coordinates_rational'] and data['cyclic_to_Lie_roundtrip_verified']
        assert data['input_sha256'][args.tiny.name] == sha(args.tiny)
        multiplication_path = path.parent/(disk_id+'_multiply47.json.gz')
        assert data['input_sha256'][multiplication_path.name] == sha(multiplication_path)
        multiple = read(multiplication_path)
        assert multiple['disk_id'] == disk_id and multiple['bits_done'] == multiple['target_bits'] == 304
        assert multiple['magnitude'] == multiple['target_multiplier'] == data['target_multiplier']
        assert 'zero_test_mod47' in multiple and len(multiple['steps']) == 454
        assert multiple['point_sha256'] == data['actual_multiple_point_sha256']
        a0 = data['actual_center_C_cyclic_coordinates_mod47cubed']
        assert len(a0) == 54 and all(0 <= x < Q3 for x in a0)
        ch, row = charts[disk_id]
        coeffs = [cc[row] for cc in ch['cyclic_coordinate_tiny_coefficients_1to3_in_y_mod47cubed']]
        aa = [a0]+coeffs
        series = [{'n': p['n'], 'coefficients_0to4_in_y_mod47four': global_series(p, aa)}
                  for p in poly['directions']]
        assert disk_id not in points
        points[disk_id] = {'disk_id': disk_id, 'actual_center_C_cyclic_coordinates_mod47cubed': a0,
                           'cyclic_C_coefficients_0to3_in_y_mod47cubed': aa, 'global_polynomials': series,
                           'constant_method': 'Actual m*(P_center-b), three formal group charts, calibrated canonical differential logarithm'}
        inputs[path.name], inputs[multiplication_path.name] = sha(path), sha(multiplication_path)
        accepted.append(disk_id)
    assert set(points).issubset(charts) and len(points)+len(missing) == 129
    out = {'level': 41, 'auxiliary_prime': 47, 'precision': 4, 'modulus': Q,
           'complete_all129_Abel_constants': not missing,
           'complete_all129_global_QC_polynomials': not missing,
           'complete_local_QC_heights': False, 'complete_common_roots': False,
           'completed_rational_disk_count': len(points),
           'global_direction_count': 53, 'global_polynomial_degree': 4,
           'parameter_convention': 'y=z/47 with z the genuine centered rational projective parameter of R228/R231',
           'coordinate_basis': poly['coordinate_basis'],
           'global_polynomial_formula': poly['based_formula'],
           'component_order': poly['component_order'], 'component_vectors': poly['component_vectors'],
           'accepted_additional_ordinary_disk_ids': accepted,
           'missing_ordinary_center_constant_disk_ids': missing,
           'actual_rational_disk_global_polynomials': [points[k] for k in sorted(points)],
           'input_sha256': inputs, 'source_sha256': sha(__file__),
           'global_series_module_sha256': sha(sys.modules['p41_three_ordinary_CM_anchors47'].__file__)}
    save(args.output, out)
    print('Actual global functions', len(points), '*53; remaining ordinary constants', len(missing),
          'SHA', sha(args.output), flush=True)


if __name__ == '__main__':
    main()
