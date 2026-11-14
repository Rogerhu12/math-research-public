#!/usr/bin/env python3
"""Choose a faithful Serre clearing section on all 126 rational disks outside the three actual elliptic coarse points.

The published 52-dimensional clearing space is unchanged.  Only its chosen
section changes, with exact cubic identities and the same meromorphic
derivation checked on all 820 faithful points.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import random
import sys


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    scripts = args.script_dir.resolve()
    sys.path.insert(0, str(scripts))
    import p41_r2_matrix as r
    from p41_actual_differentials47 import ActualModel, Q
    from p41_projective_jet_frames47 import install_exact_float_mm
    install_exact_float_mm(r)
    a = ActualModel(scripts)
    M, np = a.M, a.np
    old_name = 'p41_cleared_serre_derivative47_complete.json.gz'
    old = a.read(old_name)
    K = r.from_json(old['elliptic_kernel_coefficients'])
    cm3 = a.read('p41_cm3_makdisi47_certificate.json')
    E = r.from_json(a.cm4['coarse_point_values'] + [cm3['coarse_evaluation_coefficients'][0]])
    assert len(r.rank_pivots(E)[0]) == 21
    assert len(r.rank_pivots(K)[0]) == 52 and r.iszero(r.mm(E, K))
    atlas = a.read('p41_rational_SS_residue_atlas47_complete.json.gz')
    ordinary = a.read('p41_ordinary_point_lifts47.json.gz')
    points, labels, js = [], [], []
    j_by_disk = {x['disk_id']: x['j_mod47'] for x in atlas['SS_disk_records']}
    for chart in atlas['charts']:
        points.extend(chart['W_coefficients_0to3'][0])
        labels.extend(chart['disk_ids'])
        js.extend(j_by_disk[d] for d in chart['disk_ids'])
    for point in ordinary['points']:
        points.append(point['W_mod47four'])
        labels.append('ORD_j' + str(point['j_mod47']).zfill(2))
        js.append(point['j_mod47'])
    assert len(points) == len(set(labels)) == 129
    excluded = {'SS_j0_10', 'SS_j36_02', 'SS_j36_06'}
    assert excluded.issubset(set(labels))
    wanted = [i for i, label in enumerate(labels) if label not in excluded]
    assert len(wanted) == 126
    W = r.from_json(points)
    rng = random.Random(435470)
    rejected = []
    for attempt in range(10000):
        seed = r.column([[rng.randrange(47), rng.randrange(47)] for _ in range(52)])
        v0 = r.mm(K, seed)
        v = r.add(v0, r.mm(M['A1'], r.conjugate(v0)))
        source_values = r.mm(M['W'], v)
        disk_values = r.mm(W, v)
        bad_source = np.flatnonzero(~r.units(source_values)[:, 0]).tolist()
        bad_disk = [i for i in wanted if not r.units(disk_values)[i, 0]]
        if not bad_source and not bad_disk:
            break
        rejected.append({'attempt': attempt, 'nonunit_source_count': len(bad_source),
                         'nonunit_disk_labels': [labels[i] for i in bad_disk]})
    else:
        raise AssertionError('No clearing section found')
    assert r.iszero(r.mm(E, v))
    assert r.equal(r.mm(M['A1'], r.conjugate(v)), v)
    jets = a.read('p41_evaluation_jets47_checkpoint.json.gz')
    WD = r.from_json(jets['evaluation_derivatives'])
    delta = r.add(a.scale(WD, -27652 * pow(3, -1, Q)), a.scale(M['W'], 96))
    values = r.mul(source_values, delta)
    G = r.rows(values, M['P3'])
    assert r.equal(r.mm(M['V3'], G), values)
    assert r.equal(r.mm(M['A3'], r.conjugate(G)), r.mm(G, M['A1']))
    Av = r.rows(source_values, M['P3'])
    assert r.equal(r.mm(M['V3'], Av), source_values)
    oldv = r.from_json(old['chosen_clearing_section'])
    oldG = r.from_json(old['cleared_derivative_coefficients'])
    oldvalues = r.mm(M['W'], oldv)
    assert r.equal(r.mul(oldvalues, r.mm(M['V3'], G)),
                   r.mul(source_values, r.mm(M['V3'], oldG)))
    out = {
        'result': 'R435', 'level': 41, 'auxiliary_prime': 47, 'precision': 4,
        'modulus': Q, 'status': 'complete faithful replacement clearing section',
        'chosen_attempt': attempt, 'chosen_clearing_seed': r.to_json(seed),
        'chosen_clearing_section': r.to_json(v),
        'cleared_derivative_coefficients': r.to_json(G),
        'Av_cubic_coefficients': r.to_json(Av),
        'elliptic_kernel_coefficients': r.to_json(K),
        'elliptic_restriction_rank': 21, 'clearing_space_rank': 52,
        'chosen_clearing_all_820_units': True,
        'all126_requested_rational_disks_unit': True,
        'requested_rational_disk_count': len(wanted),
        'actual_requested_disk_values': [
            {'disk_id': labels[i], 'j_mod47': js[i],
             'value_mod47four': r.to_json(disk_values)[i][0]} for i in wanted],
        'excluded_actual_coarse_elliptic_disks': [labels[i] for i in range(129) if i not in wanted],
        'all820_cubic_derivative_equalities': True,
        'all820_cubic_Av_equalities': True,
        'all820_old_new_derivation_cross_equalities': True,
        'Frobenius': True, 'rejected_candidates': rejected,
        'formula': 'delta(W)=W_derivative/beta0+96W; G=v*delta(W), beta0=-3/27652',
        'input_sha256': a.inputs,
        'previous_derivative_sha256': sha(scripts / 'data' / old_name),
        'source_sha256': sha(__file__),
        'actual_height_or_Norm_computed': False,
    }
    raw = (json.dumps(out, sort_keys=True, separators=(',', ':')) + '\n').encode()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(gzip.compress(raw, mtime=0))
    print('PASS R435 actual clearing frame', attempt, 'rational disks', len(wanted),
          'all820 exact cubic and cross identities', sha(args.output), flush=True)


if __name__ == '__main__':
    main()
