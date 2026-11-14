#!/usr/bin/env python3
"""Evaluate the saved B Miller chain at actual CM16 or CM36 points.

The global derivation reconstructs integral rational-coordinate jets.  Every
nonunit section is prepared as a whole disc using R159.  No group operation
is recomputed.  Both source divisors avoid these discs; all actual end factors are retained.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys
import time

P = 47
Q = P**4
ZERO = (0, 0)
ONE = (1, 0)
PIN = {
    'p41_cm16_hecke47_verified.json.gz': 'a387489a44357abc78811de1bace6af2d4e42b77c3561f2ef18269e32996bcc2',
    'p41_cm36_hecke47_raw.json.gz': '3ea9d90b3889ef835fc0254673b9358841ee597d37e2a38622906356ed4bd495',
    'p41_makdisi47_certificate.json.gz': 'c6ea2f89f4f64eec78039c5b14b6835295b045ea24ae26f885c4047b21e96222',
    'p41_cusp_divisors47_certificate.json.gz': 'ae902f25e6d3674b6d474a70ee12a925c0934c198eff94581cfd5dbba30023fb',
    'p41_cm4_divisor47_certificate.json': 'f98b13cbc7afb3ed5d8b2f9249fbe815198b478b23559c319c5ba56b6bd83540',
    'p41_group47_checkpoint.json.gz': '4f982a4801332f9eff196ff9e9f866883b01014579896c20e65d044530b8b655',
    'p41_evaluation_jets47_checkpoint.json.gz': 'a4ff695e00a7dc7d662f3db0d675549852bc7f3490b5c34d3a18dd98a7528b5d',
    'p41_hecke3_abel_bases_checkpoint.json.gz': '2c0c16acee560af04582de86e345fe3ded57c8c0d5f8c5f56b2631aaf00e3a8d',
    'p41_miller_completion47_compact.json.gz': '69a33e8c944447e439804a842f418ea2f4e04b03ca5ccc8691a396e96036ffa0',
    'p41_miller_all54_slp110_fixed.json.gz': 'be8e694fcf63200e77e8f4f3c5a27cff2cf1d73c3afb3e5ff9ae4f102aa7da33',
    'p41_poincare_miller_jets47_saved.json.gz': '2e24db934bf136b7280385c20dd8d1c4bfd97f850cad4b32b4705ba05b8546ed',
}


def add(a, b):
    return ((a[0]+b[0]) % Q, (a[1]+b[1]) % Q)


def sub(a, b):
    return ((a[0]-b[0]) % Q, (a[1]-b[1]) % Q)


def mul(a, b):
    return ((a[0]*b[0]-a[1]*b[1]) % Q, (a[0]*b[1]+a[1]*b[0]) % Q)


def inverse(a):
    v = pow((a[0]*a[0]+a[1]*a[1]) % Q, -1, Q)
    return (a[0]*v % Q, -a[1]*v % Q)


def power(a, e):
    if e < 0:
        return power(inverse(a), -e)
    out = ONE
    while e:
        if e & 1:
            out = mul(out, a)
        a = mul(a, a)
        e >>= 1
    return out


def conjugate(a):
    return (a[0], -a[1] % Q)


def norm(values):
    out = ONE
    for v in values:
        out = mul(out, v)
    assert out[1] == 0
    return out


def logarithm(a):
    assert a[1] == 0
    z = sub(power(a, 46), ONE)
    assert all(x % P == 0 for x in z)
    z2 = mul(z, z)
    z3 = mul(z2, z)
    return mul(add(sub(z, mul(z2, (pow(2, -1, Q), 0))),
                   mul(z3, (pow(3, -1, Q), 0))), (pow(46, -1, Q), 0))


def polynomial_product(a, b):
    out = [ZERO]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] = add(out[i+j], mul(x, y))
    return out


def polynomial_division(a, b):
    b = [tuple(v) for v in b]
    assert b[-1] == ONE
    a = [tuple(v) for v in a]
    e = len(b)-1
    if len(a) < len(b):
        return [ZERO], a
    out = [ZERO]*(len(a)-e)
    for k in range(len(a)-1, e-1, -1):
        out[k-e] = a[k]
        for j in range(e+1):
            a[k-e+j] = sub(a[k-e+j], mul(out[k-e], b[j]))
    return out, a[:e]


def exact_quotient(a, b):
    out, rem = polynomial_division(a, b)
    assert all(v == ZERO for v in rem), 'actual distinguished divisor mismatch'
    return out


def flat(c):
    return [a[0] if len(a) == 1 else a for a in c]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--prefix110', action='store_true')
    parser.add_argument('--conductor', type=int, choices=[2, 3], required=True)
    parser.add_argument('--coordinate-seed', type=int, default=0)
    args = parser.parse_args()
    folder = args.script_dir.resolve()
    sys.path.insert(0, str(folder))
    import numpy as np
    import p41_r2_matrix as r
    from p41_cm4_divisor47 import kernel
    from p41_group_operations47 import load_sources, make_model
    from p41_weierstrass_unit47 import prepare_unit
    from p41_formal47_multiply import point_hash
    started = time.monotonic()
    inputs = {}

    def read(name):
        raw = (folder/'data'/name).read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        assert digest == PIN[name], ('input SHA', name)
        inputs[name] = digest
        return json.loads(gzip.decompress(raw) if name.endswith('.gz') else raw)

    sources, hashes = load_sources(folder/'data')
    for name, digest in hashes.items():
        assert digest == PIN[name]
    inputs.update(hashes)
    model, cusp, cm4, group = sources
    M = make_model(sources)
    derivatives = read('p41_evaluation_jets47_checkpoint.json.gz')
    bases = read('p41_hecke3_abel_bases_checkpoint.json.gz')
    completion = read('p41_miller_completion47_compact.json.gz')
    slp = read('p41_miller_all54_slp110_fixed.json.gz' if args.prefix110 else
               'p41_poincare_miller_jets47_saved.json.gz')
    assert len(slp['steps']) == (165 if args.prefix110 else 454)
    assert slp['bits_done'] == (110 if args.prefix110 else 304)
    assert point_hash(r.from_json(slp['point_coordinates']), r.from_json(slp['point_frobenius'])) == slp['point_sha256']
    K1 = r.from_json(kernel(73, cusp['cusp_rank_columns_1based'], cusp['cusp_free_columns_1based'], cusp['canonical_kernel_block']))
    fc = r.mm(K1, r.column(cusp['canonical_coefficients']))
    f = r.mm(M['W'], fc)
    dW = r.from_json(derivatives['evaluation_derivatives'])
    df = r.mm(dW, fc)
    ibeta = -27652*pow(3, -1, Q) % Q
    Hv = tuple(x*ibeta % Q for x in r.sub(r.mul(dW, f), r.mul(M['W'], df)))
    H = r.rows(Hv, M['P3'])
    assert r.equal(r.mm(M['V3'], H), Hv)
    hsha = hashlib.sha256(json.dumps(r.to_json(H), separators=(',', ':')).encode()).hexdigest()
    assert hsha == '475ebf071503f2f12285a041c88dfc5ab290a7953aba72df9df2cf43cf5f0988'
    c = r.cols(M['A1'], [args.coordinate_seed])
    c[0][args.coordinate_seed, 0] = (c[0][args.coordinate_seed, 0]+1) % Q
    assert r.equal(r.mm(M['A1'], r.conjugate(c)), c)
    if args.conductor == 2:
        target = read('p41_cm16_hecke47_verified.json.gz')
        weight_values = target['weight2_values']
        tau = [i-1 for i in target['target_frobenius_permutation_1based']]
    else:
        target = read('p41_cm36_hecke47_raw.json.gz')
        weight_values = [row for record in target['records'] for row in record['weight2_values']]
        tau = [20*b+i-1 for b, record in enumerate(target['records']) for i in record['target_frobenius_permutation_1based']]
    number = len(weight_values)
    assert number == 20*args.conductor-20
    W0 = r.from_json(weight_values)
    f0 = r.mm(W0, fc)
    assert np.all(r.units(f0))
    ws = [r.mul(W0, r.inverse_values(f0))]
    v2, v3, hs, hc, hi = [], [], [], [], []
    aa2, bb2 = zip(*[(a-1, b-1) for a, b in cusp['square_basis_monomials_1based']])
    aa3, bb3 = zip(*[(a-1, b-1) for a, b in group['cubic_selected_pairs_1based']])
    C2 = r.from_json(cusp['square_basis_inverse'])
    extra_inverse = r.from_json(group['cubic_extra_inverse'])
    oldrows = [M['P2'][b] for b in bb3]
    lam = r.mul((M['W'][0][oldrows, aa3][None, :], M['W'][1][oldrows, aa3][None, :]),
                r.inverse_values((f[0][oldrows].T, f[1][oldrows].T)))
    ifP2 = r.inverse_values((f[0][M['P2']].T, f[1][M['P2']].T))
    C = r.rows(r.mul(r.mul(f, M['V2']), ifP2), [n-1 for n in group['cubic_extra_rows_1based']])
    order = 24
    for n in range(order+1):
        raw = r.zeros(number, 199)
        for k in range(n+1):
            raw = r.add(raw, r.mul(r.cols(ws[k], aa2), r.cols(ws[n-k], bb2)))
        v2.append(r.mm(raw, C2))
        raw = r.zeros(number, 126)
        for k in range(n+1):
            raw = r.add(raw, r.mul(r.cols(ws[k], aa3), r.cols(v2[n-k], bb3)))
        raw = r.sub(raw, r.mul(r.cols(v2[n], bb3), lam))
        extra = r.mm(raw, extra_inverse)
        v3.append(r.hcat(r.sub(r.mul(v2[n], ifP2), r.mm(extra, C)), extra))
        hs.append(r.mm(v3[n], H))
        hc.append(r.mm(hs[n], c))
        if n == 0:
            assert np.all(r.units(hc[0]))
            hi.append(r.inverse_values(hc[0]))
        else:
            t = r.zeros(number, 1)
            for k in range(1, n+1):
                t = r.add(t, r.mul(hc[k], hi[n-k]))
            hi.append(r.neg(r.mul(t, hi[0])))
        if n < order:
            t = r.zeros(number, 73)
            for k in range(n+1):
                t = r.add(t, r.mul(hs[k], hi[n-k]))
            t = tuple(x*pow(n+1, -1, Q) % Q for x in t)
            assert r.iszero(r.mm(t, fc))
            target = r.column([[int(n == 0), 0]]*number)
            assert r.equal(r.mm(t, c), target)
            ws.append(t)
    negative = r.mm(M['B'], r.column(group['negative_flip_section_seeds_and_coefficients'][0][1]))
    negativeK = r.from_json(kernel(199, group['negative_rank_columns_1based'], group['negative_free_columns_1based'], group['negative_kernel_block']))
    endK = r.from_json(slp['point_coordinates'])
    step_coefficients = []
    for rec in slp['steps']:
        encoded = rec['principal_section_coefficients']
        digest = hashlib.sha256(json.dumps(encoded, separators=(',', ':')).encode()).hexdigest()
        assert digest == rec['principal_coefficient_sha256']
        step_coefficients.append(r.column(flat(encoded)))
    coeff = r.hcat(*step_coefficients)
    allsteps = [r.to_json(r.mm(v, coeff)) for v in v3]
    fixed = {'negative': (v2, negative),
             'old': (v2, r.column(flat(completion['endpoint_transfer']['old_section_coefficients']))),
             'new': (v2, r.column(flat(completion['endpoint_transfer']['new_section_coefficients']))),
             'v0': (ws, r.column(flat(bases['families'][0]['v_coefficients'])))}
    fixedvalues = {key: [r.to_json(r.mm(v, co)) for v in js] for key, (js, co) in fixed.items()}
    ideals = {key: [r.to_json(r.mm(v, K)) for v in v2] for key, K in [('initial', M['B']), ('negative', negativeK), ('current', endK)]}
    initialW = [ONE]
    records = []

    def germ(values, point, column):
        return [tuple(row[point][column]) for row in values]

    def check_ideal(values, point, polynomial):
        witness = None
        degree = len(polynomial)-1
        for col in range(73):
            g = germ(values, point, col)
            assert all(v == ZERO for v in polynomial_division(g, polynomial)[1])
            e = next((n for n, a in enumerate(g) if (a[0]*a[0]+a[1]*a[1]) % P), None)
            if e == degree and witness is None:
                witness = col+1
        assert witness is not None
        return witness

    for point in range(number):
        prepared = {key: prepare_unit(germ(vals, point, 0)) for key, vals in fixedvalues.items()}
        minusW = exact_quotient(prepared['negative']['weierstrass_coefficients'], initialW)
        minusU = inverse(tuple(prepared['negative']['unit_constant']))
        initial_witness = check_ideal(ideals['initial'], point, initialW)
        negative_witness = check_ideal(ideals['negative'], point, minusW)
        currentW, u, e = initialW, ONE, 1
        histogram = {}
        prefix = None
        for k, step in enumerate(slp['steps']):
            sec = prepare_unit(germ(allsteps, point, k))
            histogram[sec['degree']] = histogram.get(sec['degree'], 0)+1
            sign = 1 if e > 0 else -1
            if step['operation'] == 'double':
                otherW, otherU = currentW, u
                e = -2*e
            else:
                assert step['operation'] == 'add'
                otherW, otherU = (initialW, ONE) if sign == 1 else (minusW, minusU)
                e = -(e+sign)
            currentW = exact_quotient(sec['weierstrass_coefficients'], polynomial_product(currentW, otherW))
            u = inverse(mul(mul(u, otherU), tuple(sec['unit_constant'])))
            assert (1 if e > 0 else -1) == step['sign']
            if k == 164:
                assert e == -840890532437241886729500926334771 and currentW == [ONE]
                prefix = {'unit': u, 'exponent': str(e)}
        assert e == int(slp['sign'])*int(slp['magnitude'])
        current_witness = check_ideal(ideals['current'], point, currentW)
        gunit = mul(tuple(prepared['new']['unit_constant']), inverse(mul(tuple(prepared['old']['unit_constant']), tuple(prepared['v0']['unit_constant']))))
        complete = not args.prefix110
        final = None
        if complete:
            assert e == int(slp['target_multiplier']) and slp['point_sha256'] == completion['old_point_sha256']
            assert polynomial_product(prepared['new']['weierstrass_coefficients'], currentW) == polynomial_product(prepared['old']['weierstrass_coefficients'], prepared['v0']['weierstrass_coefficients'])
            unit_z = mul(u, inverse(gunit))
            final = {'unit': unit_z, 'order': 0}
        records.append({'point_1based': point+1, 'negative_W': minusW, 'negative_unit': minusU,
                        'current_W': currentW, 'current_unit': u, 'endpoint_g_unit': gunit,
                        'initial_ideal_witness': initial_witness, 'negative_ideal_witness': negative_witness,
                        'current_ideal_witness': current_witness, 'prefix110': prefix,
                        'section_degree_histogram': histogram, 'complete': complete, 'final': final})
        if (point+1) % 5 == 0:
            print('CM'+str(4*args.conductor**2), point+1, 'of'+str(number)+'; max section degree', max(histogram), flush=True)
    for j, k in enumerate(tau):
        for field in ['current_unit', 'negative_unit', 'endpoint_g_unit']:
            assert records[k][field] == conjugate(records[j][field])
        for field in ['current_W', 'negative_W']:
            assert records[k][field] == [conjugate(v) for v in records[j][field]]
        assert records[k]['prefix110']['unit'] == conjugate(records[j]['prefix110']['unit'])
    norms = {'U': norm([a['current_unit'] for a in records]),
             'prefix110_U': norm([a['prefix110']['unit'] for a in records]),
             'negative_U': norm([a['negative_unit'] for a in records]),
             'endpoint_g': norm([a['endpoint_g_unit'] for a in records])}
    logs = {k: logarithm(v) for k, v in norms.items()}
    if args.coordinate_seed == 0:
        expected = {2: (513569, 4296928, 3475650), 3: (446970, 4746248, 1846865)}[args.conductor]
        assert tuple(logs[k][0] for k in ['prefix110_U', 'negative_U', 'endpoint_g']) == expected
    final = None
    if not args.prefix110:
        ff = norm([a['final']['unit'] for a in records])
        final = {'norm': ff, 'log_norm': logarithm(ff)}
        assert final['log_norm'] == sub(logs['U'], logs['endpoint_g'])
    source = Path(__file__).read_bytes()
    out = {'level': 41, 'auxiliary_prime': 47, 'precision': 4, 'modulus': Q,
           'bits': slp['bits_done'], 'steps': len(slp['steps']), 'multiplier': str(slp['target_multiplier']),
           'coordinate_seed': args.coordinate_seed, 'coordinate_coefficients': r.to_json(c),
           'jet_order': order, 'global_derivation_entries_checked': 59860,
           'global_derivation_coefficients_sha256': hsha, 'conductor': args.conductor, 'CM_discriminant': -4*args.conductor**2, 'number_of_points': number,
           'local_certificates': records, 'norms': norms, 'logarithms': logs,
           'Frobenius': True, 'all_actual_ideal_columns_checked': 73,
           'complete_full_chain': not args.prefix110, 'final_f_B_CM_norm': final,
           'input_sha256': inputs, 'generating_source_sha256': hashlib.sha256(source).hexdigest(),
           'normalization': 'Actual CM points; all initial, negative and final distinguished factors verified; f_B=U_m/g'
           , 'reconstruction_provenance': 'After environment reset, adapted from root p41_cm4_miller_norm47.py; independently matches all pre-reset pure-JS110bit values'
           , 'root_engine_sha256': 'a286000cf2110878124f09af0995612adb0d35fe03ef07069f48a7e9d8600beb'}
    raw = (json.dumps(out, indent=2, sort_keys=True)+'\n').encode()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(gzip.compress(raw, mtime=0) if args.output.name.endswith('.gz') else raw)
    print(json.dumps({'complete': out['complete_full_chain'], 'logarithms': logs, 'final': final,
                      'output_sha256': hashlib.sha256(args.output.read_bytes()).hexdigest(), 'seconds': time.monotonic()-started}), flush=True)


if __name__ == '__main__':
    main()
