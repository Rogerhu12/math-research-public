#!/usr/bin/env python3
"""Use the R470 additional-j9 moved representatives with unchanged scalar/formal engines."""
import argparse
from pathlib import Path
import sys

import p41_ordinary_Abel_multiply47 as frozen

read, save, sha = frozen.read, frozen.save, frozen.sha
multiply, extract_Abel = frozen.multiply, frozen.extract_Abel


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ['script-dir', 'SS-atlas', 'common-based-points', 'based-points', 'workdir']:
        ap.add_argument('--'+name, type=Path, required=True)
    ap.add_argument('--disk', action='append', required=True)
    ap.add_argument('--max-bits', type=int, default=304)
    ap.add_argument('--tiny', type=Path)
    ap.add_argument('--prepare-only', action='store_true')
    args = ap.parse_args()
    sys.path.insert(0, str(args.script_dir.resolve()))
    from p41_actual_differentials47 import ActualModel
    from p41_projective_jet_frames47 import install_exact_float_mm
    from p41_native_r2_linear47 import install
    from p41_formal47_multiply import point_hash
    import p41_r2_matrix as r
    install_exact_float_mm(r)
    args.workdir.mkdir(parents=True, exist_ok=True)
    linear = install(r, args.workdir/'native-build')
    a = ActualModel(args.script_dir)
    a.linear_manifest = linear
    points = read(args.based_points)
    assert points['result'] == 'R470' and points['complete_selected_SS_actual_based_points']
    assert points['unchanged_original820_V2_V3_bases_and_P2_P3_normalizations']
    assert len(set(args.disk)) == len(args.disk) and set(args.disk).issubset(points['selected_disks'])
    assert points['input_sha256'][args.SS_atlas.name] == sha(args.SS_atlas)
    assert points['input_sha256'][args.common_based_points.name] == sha(args.common_based_points)
    for disk in args.disk:
        point = next(p for p in points['records'] if p['disk_id'] == disk)
        K, A = r.from_json(point['point_coordinates']), r.from_json(point['point_frobenius'])
        assert point_hash(K, A) == point['point_sha256']
        assert r.equal(r.mm(K, A), r.mm(a.M['A2'], r.conjugate(K)))
        assert a.np.all(a.np.any(r.units(r.mm(a.M['V2'], K)), axis=1))
        tr = point['initial_moving_transport']
        assert tr['moving_ratio_divisor'] == 'div(h/f)=E_moved-E'
        assert tr['initial_principal_function'] == 'f_b*h/(f_c*f)'
        if args.prepare_only:
            continue
        checkpoint = args.workdir/(disk+'_multiply47.json.gz')
        data = multiply(a, point, args.based_points, checkpoint, args.max_bits)
        if data['bits_done'] == 304 and args.tiny is not None:
            output = args.workdir/(disk+'_Abel47.json.gz')
            if output.exists():
                old = read(output)
                assert old['complete_actual_center_Abel_constant']
                assert old['input_sha256'][checkpoint.name] == sha(checkpoint)
            else:
                extract_Abel(a, data, checkpoint, args.tiny, output)


if __name__ == '__main__':
    main()
