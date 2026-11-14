#!/usr/bin/env python3
"""Independently replay the new clearing identities using Python integers.

The already published actual model reconstructs the geometry.  All dot
products below are separate integer complex-pair arithmetic, without its
matrix multiplication implementation.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys

Q = 47**4


def read(p):
    b = Path(p).read_bytes()
    return json.loads(gzip.decompress(b) if str(p).endswith('.gz') else b)


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def dot(x, y):
    re = im = 0
    for (a, b), (c, d) in zip(x, y):
        re += a*c-b*d
        im += a*d+b*c
    return [re % Q, im % Q]


def mul(x, y):
    a, b = x
    c, d = y
    return [(a*c-b*d) % Q, (a*d+b*c) % Q]


def conj(x):
    return [x[0], -x[1] % Q]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir', type=Path, required=True)
    ap.add_argument('--certificate', type=Path, required=True)
    ap.add_argument('--generator', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    S = args.script_dir.resolve()
    x = read(args.certificate)
    assert x['result'] == 'R379' and x['modulus'] == Q
    assert x['source_sha256'] == sha(args.generator)
    oldp = S/'data/p41_cleared_serre_derivative47_complete.json.gz'
    assert x['previous_derivative_sha256'] == sha(oldp)
    sys.path.insert(0, str(S))
    from p41_actual_differentials47 import ActualModel
    a = ActualModel(S)
    W, V3, A1, A3 = [a.r.to_json(a.M[n]) for n in ('W', 'V3', 'A1', 'A3')]
    jets = read(S/'data/p41_evaluation_jets47_checkpoint.json.gz')
    WD = jets['evaluation_derivatives']
    v = [row[0] for row in x['chosen_clearing_section']]
    G = x['cleared_derivative_coefficients']
    Av = [row[0] for row in x['Av_cubic_coefficients']]
    assert len(v) == 73 and len(G) == len(Av) == 325
    assert all(len(row) == 73 for row in G)
    cols = [list(col) for col in zip(*G)]
    beta_inv = -27652 * pow(3, -1, Q) % Q
    for i in range(820):
        vv = dot(W[i], v)
        assert vv[0] % 47 or vv[1] % 47
        assert dot(V3[i], Av) == vv
        for j in range(73):
            delta = [(beta_inv*WD[i][j][k]+96*W[i][j][k]) % Q for k in (0, 1)]
            assert dot(V3[i], cols[j]) == mul(vv, delta), (i, j)
    print('PASS independent integer evaluation: all59860 cubic derivative entries and820 Av entries', flush=True)
    cm3 = read(S/'data/p41_cm3_makdisi47_certificate.json')
    cm4 = read(S/'data/p41_cm4_divisor47_certificate.json')
    E = cm4['coarse_point_values'] + [cm3['coarse_evaluation_coefficients'][0]]
    assert len(E) == 21 and all(dot(w, v) == [0, 0] for w in E)
    assert all(dot(row, [conj(z) for z in v]) == value for row, value in zip(A1, v))
    acols = [list(col) for col in zip(*A1)]
    for i in range(325):
        for j in range(73):
            assert dot(A3[i], [conj(z) for z in cols[j]]) == dot(G[i], acols[j]), (i, j)
    print('PASS independent integer Frobenius and all21 true elliptic vanishing conditions', flush=True)
    atlas = read(S/'data/p41_rational_SS_residue_atlas47_complete.json.gz')
    ordinary = read(S/'data/p41_ordinary_point_lifts47.json.gz')
    jmap = {z['disk_id']: z['j_mod47'] for z in atlas['SS_disk_records']}
    points = []
    for chart in atlas['charts']:
        points += list(zip(chart['disk_ids'], chart['W_coefficients_0to3'][0]))
    for z in ordinary['points']:
        label = 'ORD_j'+str(z['j_mod47']).zfill(2)
        points.append((label, z['W_mod47four']))
        jmap[label] = z['j_mod47']
    assert len(points) == 129
    recorded = []
    for label, w in points:
        if jmap[label] in (0, 1728 % 47):
            continue
        value = dot(w, v)
        assert value[0] % 47 or value[1] % 47
        recorded.append({'disk_id': label, 'j_mod47': jmap[label], 'value_mod47four': value})
    assert recorded == x['actual_nonelliptic_disk_values']
    assert len(recorded) == x['nonelliptic_rational_disk_count'] == 85
    out = {
        'result': 'R379', 'certificate_sha256': sha(args.certificate),
        'generator_sha256': sha(args.generator), 'source_sha256': sha(__file__),
        'all59860_derivative_cubic_evaluations_replayed_with_Python_integers': True,
        'all820_Av_evaluations_replayed_with_Python_integers': True,
        'all820_source_clearing_values_unit': True,
        'all21_true_elliptic_vanishing_conditions': True,
        'complete_v_and_G_Frobenius_replayed_with_Python_integers': True,
        'all85_nonelliptic_rational_disk_values_verified_and_unit': True,
        'scope': 'Geometry reconstructed from published actual model; all new dot products, source equalities, Frobenius and unit values independently replayed using Python integer complex pairs.',
        'actual_height_or_Norm_computed': False,
        'model_input_sha256': a.inputs,
    }
    args.output.write_text(json.dumps(out, ensure_ascii=False, indent=2)+'\n')
    print('PASS R379 independent arithmetic', sha(args.output), flush=True)


if __name__ == '__main__':
    main()
