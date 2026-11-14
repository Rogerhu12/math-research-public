#!/usr/bin/env python3
"""Recover quartic normalized isogeny models from constant de Rham data.

The connection, pullback identity, and coefficient uniqueness are proved in
R218.  Every node is computed directly from the original source: large kernel
quotient algebras are needed only for the already certified constant DAG.
"""
import argparse
from pathlib import Path
import time

from p41_coprime_kernel_dag47 import (
    Q, R, Jets, digest, read, save, ks, lift_edge_quartic,
)


def derivative(series):
    return tuple(R.scale(series[k+1], k+1) for k in range(len(series)-1))


def connection(A, B):
    """Return a,b,c with nabla omega=a omega+b eta, nabla eta=c omega-a eta."""
    size = len(A)-1
    J = Jets(R, size)
    a, b = tuple(A[:size]), tuple(B[:size])
    da, db = derivative(A), derivative(B)
    delta = J.add(J.scale(J.power(a, 3), 4), J.scale(J.power(b, 2), 27))
    inv = J.inverse(delta)
    aa = J.neg(J.mul(J.add(J.mul(J.mul(a, a), da),
                    J.scale(J.mul(b, db), 9*pow(2, -1, Q))), inv))
    bb = J.mul(J.sub(J.scale(J.mul(b, da), 9*pow(2, -1, Q)),
                    J.scale(J.mul(a, db), 3)), inv)
    cc = J.scale(J.mul(a, bb), pow(3, -1, Q))
    return aa, bb, cc


def ode_quartic(source_A, source_B, target_A0, target_B0, degree, u0):
    """Uniquely solve the actual normalized-isogeny connection to order four."""
    assert degree % 47
    J = Jets(R, 4)
    aa, bb, cc = connection(source_A, source_B)
    bs = J.scale(bb, pow(degree, -1, Q))
    As = tuple(source_A[:4])
    A = [tuple(target_A0)]+[R.zero]*4
    B = [tuple(target_B0)]+[R.zero]*4
    u = [tuple(u0)]+[R.zero]*4
    for k in range(4):
        a, b, uu = tuple(A[:4]), tuple(B[:4]), tuple(u[:4])
        at = J.add(aa, J.mul(uu, bs))
        da = J.add(J.scale(J.mul(a, at), -4), J.scale(J.mul(b, bs), 6))
        db = J.sub(J.scale(J.mul(b, at), -6),
                   J.scale(J.mul(J.mul(a, a), bs), 4*pow(3, -1, Q)))
        # u' = n*c_source - c_target - (a_source+a_target)*u.
        du = J.sub(J.sub(J.scale(cc, degree),
                        J.scale(J.mul(a, bs), pow(3, -1, Q))),
                   J.mul(J.add(aa, at), uu))
        inv_k = pow(k+1, -1, Q)
        A[k+1], B[k+1], u[k+1] = (R.scale(v[k], inv_k) for v in (da, db, du))
    A, B, u = tuple(A), tuple(B), tuple(u)
    at, bt, ct = connection(A, B)
    assert bt == bs
    assert at == J.add(aa, J.mul(tuple(u[:4]), bs))
    assert derivative(u) == J.sub(J.sub(J.scale(cc, degree), ct),
                                    J.mul(J.add(aa, at), tuple(u[:4])))
    assert tuple(R.scale(v, degree) for v in ks(A, B)) == ks(source_A, source_B)
    return {'A': A, 'B': B, 'u': u}


def constant_pullbacks(data):
    """Compute phi*eta=n*eta-u*omega for every constant normalized isogeny."""
    out = {'1': R.zero}
    keys = sorted(data['nodes'], key=lambda k: (len(data['nodes'][k]['path']), k))
    for key in keys:
        if key == '1':
            continue
        node = data['nodes'][key]
        # For odd ell the polynomial lists one representative of each +/- pair.
        sum_roots = R.neg(tuple(node['kernel'][-2]))
        edge_u = sum_roots if node['ell'] == 2 else R.scale(sum_roots, 2)
        out[key] = R.add(R.scale(out[node['parent']], node['ell']), edge_u)
    return out


def recover(data, dag_path, outpath, direct_checks=False):
    started = time.monotonic()
    V = Jets(R)
    source = data['nodes']['1']
    A = V.constant(tuple(source['A']))
    B = (tuple(source['B']), R.one, R.zero, R.zero, R.zero)
    u0 = constant_pullbacks(data)
    jets = {}
    for key, node in data['nodes'].items():
        jets[key] = ode_quartic(A, B, node['A'], node['B'], node['degree'], u0[key])
    out = {
        'scope': 'Actual quartic normalized target models and de Rham pullbacks; no heights',
        'curve': data['curve'], 'order': data['order'], 'modulus': Q,
        'series_modulus': 't^5', 'source_A': A, 'source_B': B,
        'constant_dag_sha256': digest(dag_path),
        'source_sha256': digest(__file__),
        'kernel_engine_sha256': digest(Path(__file__).with_name('p41_coprime_kernel_dag47.py')),
        'complete': True, 'node_count': len(jets), 'completed_count': len(jets),
        'connection_checks_per_node': 'a,b,c pullback plus u derivative, coefficients t^0..t^3',
        'jets': jets,
    }
    save(outpath, out)
    print('GM quartic saved', data['curve'], len(jets),
          'seconds', round(time.monotonic()-started, 3), flush=True)
    if direct_checks:
        checks = []
        # These compare against implicit division-polynomial lifting, not the ODE.
        selected = [k for k, n in data['nodes'].items() if n['degree'] in (2,3,4,6)]
        for ell in (43,89):
            first = next(k for k,n in data['nodes'].items() if n['degree'] == ell)
            selected.append(first)
        for key in selected:
            node = data['nodes'][key]
            parent = jets[node['parent']]
            At, Bt = lift_edge_quartic(node, parent['A'], parent['B'])
            assert At == jets[key]['A'] and Bt == jets[key]['B'], key
            checks.append({'node':key, 'degree':node['degree'],
                           'division_polynomial_quartic_matches':True})
            print('direct implicit comparison', key, flush=True)
        out['independent_implicit_checks'] = checks
        save(outpath, out)
    print('COMPLETE', digest(outpath), 'seconds', round(time.monotonic()-started, 3), flush=True)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--constant-dag', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    ap.add_argument('--direct-checks', action='store_true')
    args = ap.parse_args()
    data = read(args.constant_dag)
    assert data['modulus'] == Q
    recover(data, args.constant_dag, args.output, args.direct_checks)


if __name__ == '__main__':
    main()
