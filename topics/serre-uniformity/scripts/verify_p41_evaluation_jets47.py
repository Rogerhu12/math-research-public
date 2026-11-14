#!/usr/bin/env python3
"""Standard-library reconstruction of all820 actual first evaluation jets."""
from functools import lru_cache
import gzip
import hashlib
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
from verify_p41_cm3_makdisi47 import FastRing, Jets, JetCurve
from verify_p41_cm4_divisor47 import eisenstein
from verify_p41_makdisi47 import index, mm2, power_traces, qmatmul


def trace_evaluations(values, r, ew, ii, model):
    reps, signed = [], [0]*1681
    for k in range(1, 1681):
        neg = index(-(k % 41), -(k//41))
        if k < neg:
            reps.append(k)
            signed[k], signed[neg] = len(reps), -len(reps)
    assert len(reps) == 840
    E0, E1 = ([values[k][j] for k in reps] for j in (0, 1))
    traces = [x % r.q for x in power_traces(r.f, 237)]
    ew_i, quarter = r.mul(ii, ew), pow(4, -1, r.q)
    h0 = [sum(ew[j]*traces[k+j] for j in range(80))*quarter % r.q for k in range(159)]
    h1 = [-sum(ew_i[j]*traces[k+j] for j in range(80))*quarter % r.q for k in range(159)]
    def transform(E, h):
        return [[sum(e[k]*h[j+k] for k in range(80)) % r.q for j in range(80)] for e in E]
    E00, E01 = transform(E0, h0), transform(E0, h1)
    E10, E11 = transform(E1, h0), transform(E1, h1)
    @lru_cache(maxsize=None)
    def pair(a, b):
        const = [sum(x*y for x, y in zip(E00[a], E0[b])) % r.q,
                 sum(x*y for x, y in zip(E01[a], E0[b])) % r.q]
        deriv = [(sum(x*y for x, y in zip(E10[a], E0[b]))+
                  sum(x*y for x, y in zip(E00[a], E1[b]))) % r.q,
                 (sum(x*y for x, y in zip(E11[a], E0[b]))+
                  sum(x*y for x, y in zip(E01[a], E1[b]))) % r.q]
        return const, deriv
    raw0, raw1 = [], []
    for n in range(820):
        gh = [mm2(model['sl2_representatives'][n], h) for h in model['sl2_normalizer_mod_signs']]
        row0, row1 = [], []
        for v, w in model['basis_pairs']:
            out0, out1 = [0, 0], [0, 0]
            for g in gh:
                iv = signed[index(g[0][0]*v[0]+g[0][1]*v[1], g[1][0]*v[0]+g[1][1]*v[1])]
                iw = signed[index(g[0][0]*w[0]+g[0][1]*w[1], g[1][0]*w[0]+g[1][1]*w[1])]
                sign = 1 if iv*iw > 0 else -1
                a, b = sorted((abs(iv)-1, abs(iw)-1))
                c, d = pair(a, b)
                for j in range(2):
                    out0[j] += sign*c[j]
                    out1[j] += sign*d[j]
            row0.append([x % r.q for x in out0])
            row1.append([x % r.q for x in out1])
        raw0.append(row0)
        raw1.append(row1)
        if (n+1) % 100 == 0:
            print('Independent mixed traces', n+1, '/820', flush=True)
    return qmatmul(raw0, model['basis_inverse'], r.q), qmatmul(raw1, model['basis_inverse'], r.q)


def main(path):
    encoded = path.read_bytes()
    data = json.loads(gzip.decompress(encoded))
    assert (data['level'], data['auxiliary_prime'], data['precision'], data['modulus']) == (41, 47, 4, 47**4)
    sources = {}
    for name, digest in data['source_sha256'].items():
        raw = path.with_name(name).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == digest
        sources[name] = json.loads(gzip.decompress(raw) if name.endswith('.gz') else raw)
    torsion, model = sources['p41_local47_torsion_certificate.json'], sources['p41_makdisi47_certificate.json.gz']
    reference = next(c for c in torsion['curves'] if c['label'] == 'Makdisi_j9_fibre')
    r = FastRing(torsion['field_polynomial_ascending'], 47**4)
    j = Jets(r, 2)
    P, Q = (tuple(tuple(r.element(c) for c in coordinate) for coordinate in data[key]) for key in ('P_jets', 'Q_jets'))
    assert tuple(c[0] for c in P) == tuple(r.element(c) for c in reference['P'])
    assert tuple(c[0] for c in Q) == tuple(r.element(c) for c in reference['Q'])
    curve = JetCurve(j, j.one)
    B = j.add(j.constant(r.element(32)), j.parameter)
    for x, y in (P, Q):
        assert j.mul(y, y) == j.add(j.add(j.power(x, 3), x), B)
    assert curve.mul(P, 41) is None and curve.mul(Q, 41) is None
    phi = r.element(torsion['frobenius_lift'])
    def frobenius(T):
        return tuple(tuple(r.evaluate(c, phi) for c in coordinate) for coordinate in T)
    assert frobenius(P) == Q and frobenius(Q) == curve.mul(P, 35)
    print('Actual evaluation-fibre41-torsion jets and Frobenius verified independently.', flush=True)
    values = eisenstein(j, P, Q)
    print('All1680 actual first-order weight-one values reconstructed.', flush=True)
    W, derivative = trace_evaluations(values, r, r.element(reference['weil_pairing']),
                                     r.element(model['sqrt_minus_one_lift']), model)
    assert W == model['evaluation_matrix'] and derivative == data['evaluation_derivatives']
    tau = model['frobenius_permutation_1based']
    expected = [[[a, -b % r.q] for a, b in derivative[n-1]] for n in tau]
    assert qmatmul(derivative, model['frobenius_basis_matrix'], r.q) == expected
    print('All820x73 actual evaluation derivatives and complete descent PASS.', flush=True)
    print('SHA256', hashlib.sha256(encoded).hexdigest(), flush=True)


if __name__ == '__main__':
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else
         Path(__file__).with_name('data')/'p41_evaluation_jets47_checkpoint.json.gz')
