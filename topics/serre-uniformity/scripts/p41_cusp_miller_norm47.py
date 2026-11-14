#!/usr/bin/env python3
"""Evaluate the saved B chain at the actual degree20 cusp with q41 tangent.

The published degree80 unramified field is used without changing its basis.
Every inverse is a unit inverse.  Frobenius^20 fixes each logarithm and the
field trace divided by4 is the logarithm of the actual degree20 norm.
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
PIN = {
    'p41_makdisi47_certificate.json.gz': 'c6ea2f89f4f64eec78039c5b14b6835295b045ea24ae26f885c4047b21e96222',
    'p41_cusp_divisors47_certificate.json.gz': 'ae902f25e6d3674b6d474a70ee12a925c0934c198eff94581cfd5dbba30023fb',
    'p41_cm4_divisor47_certificate.json': 'f98b13cbc7afb3ed5d8b2f9249fbe815198b478b23559c319c5ba56b6bd83540',
    'p41_group47_checkpoint.json.gz': '4f982a4801332f9eff196ff9e9f866883b01014579896c20e65d044530b8b655',
    'p41_local47_torsion_certificate.json': '6384cdce4d6c885f3d2cf706eda2d9af0a8a85d103da42ec6535977aaddc2253',
    'p41_hecke3_abel_bases_checkpoint.json.gz': '2c0c16acee560af04582de86e345fe3ded57c8c0d5f8c5f56b2631aaf00e3a8d',
    'p41_miller_completion47_compact.json.gz': '69a33e8c944447e439804a842f418ea2f4e04b03ca5ccc8691a396e96036ffa0',
    'p41_miller_all54_slp110_fixed.json.gz': 'be8e694fcf63200e77e8f4f3c5a27cff2cf1d73c3afb3e5ff9ae4f102aa7da33',
    'p41_poincare_miller_jets47_saved.json.gz': '2e24db934bf136b7280385c20dd8d1c4bfd97f850cad4b32b4705ba05b8546ed',
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir', type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--prefix110', action='store_true')
    args = parser.parse_args()
    folder = args.script_dir.resolve()
    sys.path.insert(0, str(folder))
    import numpy as np
    import p41_r2_matrix as r
    from p41_group_operations47 import load_sources, make_model
    from p41_cm4_divisor47 import kernel
    from p41_formal47_multiply import point_hash
    started = time.monotonic()
    inputs = {}

    def read(name):
        raw = (folder/'data'/name).read_bytes()
        h = hashlib.sha256(raw).hexdigest()
        assert h == PIN[name], name
        inputs[name] = h
        return json.loads(gzip.decompress(raw) if name.endswith('.gz') else raw)

    sources, hashes = load_sources(folder/'data')
    for name, h in hashes.items():
        assert h == PIN[name]
    inputs.update(hashes)
    model, cusp, cm4, group = sources
    M = make_model(sources)
    torsion = read('p41_local47_torsion_certificate.json')
    bases = read('p41_hecke3_abel_bases_checkpoint.json.gz')
    completion = read('p41_miller_completion47_compact.json.gz')
    slp = read('p41_miller_all54_slp110_fixed.json.gz' if args.prefix110 else 'p41_poincare_miller_jets47_saved.json.gz')
    assert len(slp['steps']) == (165 if args.prefix110 else 454)
    assert slp['bits_done'] == (110 if args.prefix110 else 304)
    assert point_hash(r.from_json(slp['point_coordinates']), r.from_json(slp['point_frobenius'])) == slp['point_sha256']
    fpoly = np.asarray(torsion['field_polynomial_ascending'], dtype=np.int64)
    N = len(fpoly)-1
    assert N == 80 and fpoly[-1] == 1
    assert 80*(Q-1)**2 < 2**63
    ii = np.asarray(model['sqrt_minus_one_lift'], dtype=np.int64)

    def zero():
        return np.zeros(N, dtype=np.int64)

    def one():
        a = zero()
        a[0] = 1
        return a

    def mul(a, b):
        out = np.convolve(a, b) % Q
        for k in range(2*N-2, N-1, -1):
            c = int(out[k])
            if c:
                out[k-N:k] = (out[k-N:k]-c*fpoly[:-1]) % Q
        return out[:N]

    def power(a, e):
        out = one()
        while e:
            if e & 1:
                out = mul(out, a)
            e >>= 1
            if e:
                a = mul(a, a)
        return out

    def unit(a):
        return bool(np.any(a % P))

    def inverse(a):
        assert unit(a)
        out = power(a, (P**N-1)*P**3-1)
        assert np.array_equal(mul(a, out), one())
        return out

    def batch_inverse(values):
        pref = []
        a = one()
        for v in values:
            assert unit(v)
            pref.append(a)
            a = mul(a, v)
        b = inverse(a)
        out = [None]*len(values)
        for j in range(len(values)-1, -1, -1):
            out[j] = mul(b, pref[j])
            b = mul(b, values[j])
        assert np.array_equal(b, one())
        return out

    def flat(c):
        return [v[0] if len(v) == 1 else v for v in c]

    def dot(fields, coefficients):
        a = np.asarray(fields, dtype=np.int64)
        co = np.asarray(flat(coefficients), dtype=np.int64)
        assert len(co) == len(a) <= 820
        return ((co[:, 0]@a) % Q+mul(ii, (co[:, 1]@a) % Q)) % Q

    def row_matrix(fields, matrix):
        a = np.asarray(fields, dtype=np.int64)
        re, im = matrix
        assert a.shape[0] == re.shape[0] <= 820
        rr, ri = re.T@a % Q, im.T@a % Q
        return [(x+mul(ii, y)) % Q for x, y in zip(rr, ri)]

    K1 = r.from_json(kernel(73, cusp['cusp_rank_columns_1based'], cusp['cusp_free_columns_1based'], cusp['canonical_kernel_block']))
    fc = r.mm(K1, r.column(cusp['canonical_coefficients']))
    f = r.mm(M['W'], fc)
    ifP2 = r.inverse_values((f[0][M['P2']].T, f[1][M['P2']].T))
    C = r.rows(r.mul(r.mul(f, M['V2']), ifP2), [n-1 for n in group['cubic_extra_rows_1based']])
    cw = np.asarray(cusp['cusp_values'][0], dtype=np.int64)
    assert not np.any(dot(cw, r.to_json(fc)))
    raw2 = [mul(cw[a-1], cw[b-1]) for a, b in cusp['square_basis_monomials_1based']]
    v2 = row_matrix(raw2, r.from_json(cusp['square_basis_inverse']))
    raw3 = [mul(cw[a-1], v2[b-1]) for a, b in group['cubic_selected_pairs_1based']]
    extra = row_matrix(raw3, r.from_json(group['cubic_extra_inverse']))
    v3 = [(-x) % Q for x in row_matrix(extra, C)]+extra
    negative = r.mm(M['B'], r.column(group['negative_flip_section_seeds_and_coefficients'][0][1]))
    endpoints = {
        'f0_leading': np.asarray(cusp['canonical_cusp_leading_values'][0], dtype=np.int64),
        'negative': dot(v2, r.to_json(negative)),
        'v0': dot(cw, bases['families'][0]['v_coefficients']),
        'old': dot(v2, completion['endpoint_transfer']['old_section_coefficients']),
        'new': dot(v2, completion['endpoint_transfer']['new_section_coefficients']),
    }
    cs = []
    for step in slp['steps']:
        enc = step['principal_section_coefficients']
        assert hashlib.sha256(json.dumps(enc, separators=(',', ':')).encode()).hexdigest() == step['principal_coefficient_sha256']
        cs.append(r.column(flat(enc)))
    values = row_matrix(v3, r.hcat(*cs))
    assert all(unit(v) for v in list(endpoints.values())+values)
    inverses = batch_inverse(list(endpoints.values())+values)
    ifc, ineg, iv0, iold, inew = inverses[:5]
    iv = inverses[5:]
    f3, if3 = power(endpoints['f0_leading'], 3), power(ifc, 3)
    minus = mul(power(endpoints['f0_leading'], 2), ineg)
    minus_inverse = mul(endpoints['negative'], power(ifc, 2))
    assert np.array_equal(mul(minus, minus_inverse), one())
    g = mul(mul(endpoints['new'], iold), mul(endpoints['f0_leading'], iv0))
    gi = mul(mul(endpoints['old'], inew), mul(endpoints['v0'], ifc))
    u, ui, e, order, prefix = one(), one(), 1, 0, None
    for k, step in enumerate(slp['steps']):
        F, Fi = mul(values[k], if3), mul(iv[k], f3)
        sign = 1 if e > 0 else -1
        if step['operation'] == 'double':
            nu, nui = mul(mul(ui, ui), Fi), mul(mul(u, u), F)
            e, order = -2*e, 3-2*order
        else:
            assert step['operation'] == 'add'
            v, vi = (one(), one()) if sign == 1 else (minus, minus_inverse)
            nu, nui = mul(mul(ui, vi), Fi), mul(mul(u, v), F)
            e, order = -(e+sign), 3-order-(0 if sign == 1 else 2)
        u, ui = nu, nui
        assert (1 if e > 0 else -1) == step['sign'] and order == 1-e
        if k == 164:
            assert e == -840890532437241886729500926334771
            prefix = u.copy()
    assert e == int(slp['sign'])*int(slp['magnitude'])
    assert np.array_equal(mul(u, ui), one())
    orbit, j = [], 0
    while j not in orbit:
        orbit.append(j)
        j = cusp['cusp_frobenius_permutation_1based'][j]-1
    assert j == 0 and len(orbit) == 20
    h = np.asarray(torsion['frobenius_lift'], dtype=np.int64)

    def subst(a, b):
        out = zero()
        for k in range(N-1, -1, -1):
            out = mul(out, b)
            out[0] = (out[0]+a[k]) % Q
        return out

    phi20 = zero()
    phi20[1] = 1
    for _ in range(20):
        phi20 = subst(phi20, h)
    trace_basis = [N]
    for k in range(1, N):
        total = k*int(fpoly[N-k])
        for j in range(1, k):
            total += int(fpoly[N-j])*trace_basis[k-j]
        trace_basis.append(-total % Q)
    E = P**N-1

    def log_norm20(a):
        z = (power(a, E)-one()) % Q
        assert not np.any(z % P)
        z2 = mul(z, z)
        z3 = mul(z2, z)
        log = ((z-z2*pow(2, -1, Q)+z3*pow(3, -1, Q)) % Q)*pow(E % Q, -1, Q) % Q
        assert np.array_equal(subst(log, phi20), log)
        tr = sum(int(x)*t for x, t in zip(log, trace_basis)) % Q
        return {'log_R80': log.tolist(), 'log_norm20': tr*pow(4, -1, Q) % Q, 'phi20_fixed': True}

    targets = {name: log_norm20(a) for name, a in [('U', u), ('prefix110_U', prefix), ('endpoint_g', g), ('negative_U', minus)]}
    assert targets['prefix110_U']['log_norm20'] == 1104782
    assert targets['endpoint_g']['log_norm20'] == 2255295
    assert targets['negative_U']['log_norm20'] == 2328615
    complete = not args.prefix110
    final = None
    if complete:
        assert e == int(slp['target_multiplier']) and slp['point_sha256'] == completion['old_point_sha256']
        unit = mul(u, gi)
        final = log_norm20(unit)
        final['unit_leading_R80'] = unit.tolist()
        final['cusp_order'] = str(order-1)
        assert order-1 == -int(slp['target_multiplier'])
        assert final['log_norm20'] == (targets['U']['log_norm20']-targets['endpoint_g']['log_norm20']) % Q
    out = {'level': 41, 'auxiliary_prime': 47, 'precision': 4, 'modulus': Q,
           'bits': slp['bits_done'], 'steps': len(slp['steps']), 'exponent': str(e), 'cusp_order': str(order),
           'cusp_frobenius_orbit_1based': [j+1 for j in orbit], 'all_actual_section_values_units': True,
           'u': u.tolist(), 'u_inverse': ui.tolist(), 'g': g.tolist(), 'negative_U': minus.tolist(),
           'targets': targets, 'complete_full_chain': complete, 'final_f_B_cusp_norm': final,
           'tangent': 'q41', 'input_sha256': inputs,
           'generating_source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'normalization': 'f_B=U_m/(ssnew*f0/(ssold*v0)); trace_R80(log)/4 is the actual cusp degree20 log norm'}
    raw = (json.dumps(out, indent=2, sort_keys=True)+'\n').encode()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(gzip.compress(raw, mtime=0) if args.output.name.endswith('.gz') else raw)
    print(json.dumps({'complete': complete, 'log_norm20': None if final is None else final['log_norm20'],
                      'targets': {k: v['log_norm20'] for k, v in targets.items()},
                      'source_sha256': out['generating_source_sha256'],
                      'output_sha256': hashlib.sha256(args.output.read_bytes()).hexdigest(), 'seconds': time.monotonic()-started}), flush=True)


if __name__ == '__main__':
    main()
