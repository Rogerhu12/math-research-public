#!/usr/bin/env python3
"""Actual integral cancellation of the F2 j-ramification terms on 41 disks.

Every inverse is of a proved unit.  No value of A, B, j, j-1728 or j'
is inverted.  The output is a differential interface, not a height constant.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    b = Path(p).read_bytes()
    return json.loads(gzip.decompress(b) if str(p).endswith('.gz') else b)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for key in ['script-dir', 'derivative', 'work-dir', 'output']:
        ap.add_argument('--' + key, type=Path, required=True)
    args = ap.parse_args()
    S = args.script_dir.resolve()
    sys.path.insert(0, str(S))
    from p41_actual_differentials47 import ActualModel
    from p41_native_r2_linear47 import install
    from p41_projective_jet_frames47 import ProjectiveJetFrames
    from p41_elliptic_coarse_atlas47 import ClassicalInvariants, Series
    from types import SimpleNamespace
    a = ActualModel(S)
    r, np = a.r, a.np
    install(r, args.work_dir / 'native')
    frames = ProjectiveJetFrames(a)
    frame = read(args.derivative)
    assert frame['result'] == 'R435' and frame['all126_requested_rational_disks_unit']
    v = r.from_json(frame['chosen_clearing_section'])
    G = r.from_json(frame['cleared_derivative_coefficients'])
    inv = ClassicalInvariants(SimpleNamespace(a=a, r=r, v=v, G=G))
    atlas_path = S / 'data/p41_rational_SS_residue_atlas47_complete.json.gz'
    atlas = read(atlas_path)
    Q = r.Q
    S5, S4, S3 = [Series(a, n) for n in [5, 4, 3]]
    records = []
    for ch in atlas['charts']:
        if ch['reference_key'] not in ['0', '36']:
            continue
        W0 = r.from_json(ch['W_coefficients_0to3'][0])
        J = frames.local_jets(W0, r.from_json(ch['frame']), r.from_json(ch['coordinate']), order=4)
        for kind in ['W', 'V2', 'V3']:
            for n in range(4):
                assert r.equal(J[kind][n], r.from_json(ch[kind + '_coefficients_0to3'][n]))
        iv = inv.series(J['W'])
        assert np.all(r.units(iv['v'][0]))
        vi = S5.inverse(iv['v'])
        A = S5.mul(iv['Av'], vi)
        B = S5.mul(iv['Bv3'], S5.power(vi, 3))
        delta = S5.add(S5.scale(S5.power(A, 3), 4), S5.scale(S5.power(B, 2), 27))
        Ap = [a.scale(A[n+1], n+1) for n in range(4)]
        Bp = [a.scale(B[n+1], n+1) for n in range(4)]
        K = S4.sub(S4.scale(S4.mul(B[:4], Ap), 3), S4.scale(S4.mul(A[:4], Bp), 2))
        assert np.all(r.units(delta[0])) and np.all(r.units(K[0]))
        delta_p = [a.scale(delta[n+1], n+1) for n in range(3)]
        Kp = [a.scale(K[n+1], n+1) for n in range(3)]
        C = S3.sub(S3.scale(S3.mul(delta_p, S3.inverse(delta[:3])), 10*pow(3, -1, Q)),
                   S3.scale(S3.mul(Kp, S3.inverse(K[:3])), 4))
        assert all(not np.any(x[1]) for x in C)
        j = S5.scale(S5.mul(S5.power(A, 3), S5.inverse(delta)), 6912)
        jm = list(j)
        jm[0] = r.sub(jm[0], r.column([[1728, 0]] * len(ch['disk_ids'])))
        expected_jm = S5.scale(S5.mul(S5.power(B, 2), S5.inverse(delta)), -46656)
        assert all(r.equal(x, y) for x, y in zip(jm, expected_jm))
        jp = [a.scale(j[n+1], n+1) for n in range(4)]
        expected_jp = S4.scale(S4.mul(S4.mul(S4.mul(S4.power(A[:4], 2), B[:4]), K),
                                               S4.power(S4.inverse(delta[:4]), 2)), 186624)
        assert all(r.equal(x, y) for x, y in zip(jp, expected_jp))
        jpp = [a.scale(j[n+2], (n+2)*(n+1)) for n in range(3)]
        # This finite check complements the exact rational-function identity.
        left = S3.scale(S3.mul(S3.mul(S3.mul(C, jp[:3]), j[:3]), jm[:3]), 3)
        right = S3.add(S3.add(S3.scale(S3.mul(S3.mul(jpp, j[:3]), jm[:3]), -12),
                             S3.scale(S3.mul(S3.power(jp[:3], 2), jm[:3]), 8)),
                       S3.scale(S3.mul(S3.power(jp[:3], 2), j[:3]), 6))
        assert all(r.equal(x, y) for x, y in zip(left, right))
        degree = 3 if ch['reference_key'] == '0' else 2
        ramified_series = j if degree == 3 else jm
        assert all(not np.any(part % 47) for term in ramified_series[:degree] for part in term)
        assert np.all(r.units(ramified_series[degree]))
        rec = {'reference_key': ch['reference_key'], 'disk_ids': ch['disk_ids'],
               'ramification_index': degree, 'frame': ch['frame'], 'coordinate': ch['coordinate'],
               'W_coefficients_0to4': [r.to_json(x) for x in J['W']],
               'Hc_coefficients_0to3': [r.to_json(x) for x in J['Hc'][:4]],
               'v_coefficients_0to4': [r.to_json(x) for x in iv['v']],
               'Av_coefficients_0to4': [r.to_json(x) for x in iv['Av']],
               'Bv3_coefficients_0to4': [r.to_json(x) for x in iv['Bv3']],
               'A_coefficients_0to4': [r.to_json(x) for x in A],
               'B_coefficients_0to4': [r.to_json(x) for x in B],
               'delta_coefficients_0to4': [r.to_json(x) for x in delta],
               'K_coefficients_0to3': [r.to_json(x) for x in K],
               'j_coefficients_0to4': [r.to_json(x) for x in j],
               'regular_combined_differential_coefficients_0to2': [r.to_json(x) for x in C],
               'all_source_jets_equal_original_atlas_through_degree3': True,
               'all_v_delta_K_constant_terms_units': True,
               'actual_j_ramification_order_mod47_verified': True,
               'cleared_j_and_combined_differential_identities_verified': True}
        records.append(rec)
        print('PASS actual regular ramification terms', ch['reference_key'], len(ch['disk_ids']), flush=True)
    assert sum(len(x['disk_ids']) for x in records) == 41
    out = {'result': 'R435', 'level': 41, 'auxiliary_prime': 47, 'precision': 4, 'modulus': Q,
           'charts': records, 'all41_ordinary_level_points_above_elliptic_j_complete': True,
           'formula': 'Delta=4A^3+27B^2; K=3BAprime-2ABprime; C=(10/3)dlog(Delta)-4dlog(K)=-4dlog(jprime)+(8/3)dlog(j)+2dlog(j-1728)',
           'only_v_delta_K_units_inverted': True,
           'original_all129_atlas_coordinates_preserved': True,
           'actual_height_or_Norm_computed': False,
           'input_sha256': dict(a.inputs, **{str(atlas_path): sha(atlas_path), str(args.derivative.resolve()): sha(args.derivative)}),
           'source_sha256': sha(__file__)}
    raw = (json.dumps(out, sort_keys=True, separators=(',', ':')) + '\n').encode()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(gzip.compress(raw, mtime=0))
    print('PASS R435 integral j-ramification cancellation', sha(args.output), flush=True)


if __name__ == '__main__':
    main()
