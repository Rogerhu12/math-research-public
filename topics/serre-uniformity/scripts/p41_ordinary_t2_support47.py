#!/usr/bin/env python3
"""Actual degree-three T2 support over an ordinary rational center.

The existing degree840 unramified 41-torsion field already contains the
irreducible cubic2-kernel.  Raw phi(P),phi(Q) retain pairing zeta^2.
Coordinates are extracted in R2[r]/(r^3+A*r+B) by the exact trace duality.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys
import time

P, Q = 47, 47**4


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(path, data):
    raw = (json.dumps(data, sort_keys=True, separators=(',', ':'))+'\n').encode()
    temp = path.with_suffix(path.suffix+'.new')
    temp.write_bytes(gzip.compress(raw, mtime=0))
    temp.replace(path)


def inverse3(M):
    a = [[int(x) % Q for x in row]+[int(i == j) for j in range(3)] for i, row in enumerate(M)]
    for k in range(3):
        pivot = next(j for j in range(k, 3) if a[j][k] % P)
        a[k], a[pivot] = a[pivot], a[k]
        inv = pow(a[k][k], -1, Q)
        a[k] = [x*inv % Q for x in a[k]]
        for j in range(3):
            if j == k:
                continue
            z = a[j][k]
            a[j] = [(x-z*y) % Q for x, y in zip(a[j], a[k])]
    assert [row[:3] for row in a] == [[int(i == j) for j in range(3)] for i in range(3)]
    return [row[3:] for row in a]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir', type=Path, required=True)
    ap.add_argument('--ordinary-lifts', type=Path, required=True)
    ap.add_argument('--j', type=int, default=5)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    sys.path.insert(0, str(args.script_dir.resolve()))
    from flint import nmod_poly, fq_default_poly_ctx
    from p41_ordinary_point_lifts47 import Ring, rowmul
    from p41_ordinary_residue_points47 import Curve
    import p41_r2_matrix as r
    from p41_projective_jet_frames47 import install_exact_float_mm, ProjectiveJetFrames
    from p41_actual_differentials47 import ActualModel
    install_exact_float_mm(r)
    start = time.monotonic()
    lifts = read(args.ordinary_lifts)
    rec = next(x for x in lifts['points'] if x['j_mod47'] == args.j)
    A, B = rec['curve_A'], rec['curve_B']
    kernel = nmod_poly([B, A, 0, 1], P)
    factors = kernel.factor()[1]
    assert len(factors) == 1 and factors[0][0].degree() == 3 and factors[0][1] == 1
    K = Ring(rec['x_field_polynomial_ascending'])
    assert K.k % 120 == 0
    C = Curve.__new__(Curve)
    C.K, C.A, C.B = K, A, B
    C.P, C.Q = (K(rec['P_x']), K(1)), (K(rec['Q_x']), K(rec['Q_y_over_P_y']))
    C.f = C.P[0]**3+A*C.P[0]+B
    assert C.on_curve(C.P) and C.on_curve(C.Q)
    assert C.mul(C.P, 41) is None and C.mul(C.Q, 41) is None
    zeta, ii = K(rec['weil_pairing']), K(rec['sqrt_minus_one'])
    assert ii*ii == -1 and ii.frobenius() == -ii
    assert C.pairing() == zeta
    FK = fq_default_poly_ctx(K.rf)
    roots = FK([B, A, 0, 1]).roots(multiplicities=False)
    assert len(roots) == 3
    root0 = min(roots, key=lambda x: tuple(int(c) for c in x.to_list()))
    root = K([int(c) for c in root0.to_list()])
    for _ in range(2):
        root = root-(root**3+A*root+B)/(3*root*root+A)
    assert root**3+A*root+B == 0 and root.frobenius(3) == root
    assert root.frobenius() != root
    assert sum((root.frobenius(j) for j in range(3)), K(0)) == 0
    u = 3*root*root+A
    At, Bt = A-5*u, B-7*root*u

    def velu(T):
        inv = (T[0]-root).inverse()
        return T[0]+u*inv, T[1]*(1-u*inv*inv)

    D = Curve.__new__(Curve)
    D.K, D.A, D.B, D.f = K, At, Bt, C.f
    D.P, D.Q = velu(C.P), velu(C.Q)
    assert D.on_curve(D.P) and D.on_curve(D.Q)
    assert D.mul(D.P, 41) is None and D.mul(D.Q, 41) is None
    assert D.pairing() == zeta**2
    assert At == -4*A-15*root*root and Bt == 22*B+14*A*root
    print('PASS actual ordinary raw2-isogeny, full41 torsion and pairing determinant2', args.j,
          'seconds', round(time.monotonic()-start, 3), flush=True)
    model_path = args.script_dir/'data/p41_makdisi47_certificate.json.gz'
    model = read(model_path)
    out = {'level': 41, 'auxiliary_prime': P, 'precision': 4, 'modulus': Q,
           'source_disk_id': 'ORD_j'+str(args.j).zfill(2),
           'source_curve': [A, B], 'target_coordinate_ring': 'R2[r]/(r^3+A*r+B)',
           'kernel_polynomial_ascending': [B, A, 0, 1],
           'kernel_root_in_original_field': root.to_list(),
           'raw_target_P': [x.to_list() for x in D.P], 'raw_target_Q': [x.to_list() for x in D.Q],
           'raw_target_pairing_exponent': 2, 'raw_level_determinant_mod41': 2,
           'target_A_coefficients_ascending': [-4*A % Q, 0, -15 % Q],
           'target_B_coefficients_ascending': [22*B % Q, 14*A % Q, 0],
           'source_necklace_1based': rec['necklace_1based'],
           'source_necklace': rec['necklace'],
           'actual_pairing_and_41_torsion_verified': True,
           'complete_actual_T2_support': False,
           'input_sha256': {args.ordinary_lifts.name: sha(args.ordinary_lifts), model_path.name: sha(model_path)},
           'source_sha256': sha(__file__)}
    save(args.output, out)
    ev = D.eisenstein()
    g = model['sl2_representatives'][rec['necklace_1based']-1]
    gh = [[[sum(g[s][u]*h[u][t] for u in range(2)) % 41 for t in range(2)] for s in range(2)]
          for h in model['sl2_normalizer_mod_signs']]
    gram = [[3, 0, -2*A], [0, -2*A, -3*B], [-2*A, -3*B, 2*A*A]]
    gram_inverse = inverse3(gram)
    scale = 60*pow(K.k, -1, Q) % Q
    powers = [K(1), root, root*root]
    values = [[], [], []]
    trace_witness = None
    for row, (v, w) in enumerate(model['basis_pairs']):
        total = K(0)
        for h in gh:
            def index(v):
                return (h[0][0]*v[0]+h[0][1]*v[1]) % 41+41*((h[1][0]*v[0]+h[1][1]*v[1]) % 41)
            total += ev[index(v)]*ev[index(w)]
        total *= C.f*zeta**2
        assert total.frobenius(120) == total
        real, imag = [], []
        for power in powers:
            product = power*total
            real.append(product.trace()*scale % Q)
            imag.append(-(ii*product).trace()*scale % Q)
        rr = [sum(x*y for x, y in zip(line, real)) % Q for line in gram_inverse]
        ri = [sum(x*y for x, y in zip(line, imag)) % Q for line in gram_inverse]
        for k in range(3):
            values[k].append([rr[k], ri[k]])
        if row == 0:
            relative, value = K(0), total
            for _ in range(20):
                relative += value
                value = value.frobenius(6)
            assert value == total
            recovered = sum((powers[k]*(rr[k]+ii*ri[k]) for k in range(3)), K(0))
            assert relative == recovered
            trace_witness = relative.to_list()
    W = [rowmul(value, model['basis_inverse']) for value in values]
    out.update({'W_coefficients_ascending_in_kernel_root': W,
                'raw_basis_values_coefficients_ascending_in_kernel_root': values,
                'trace_coordinate_scale': scale, 'cubic_trace_Gram': [[x % Q for x in row] for row in gram],
                'cubic_trace_Gram_inverse': gram_inverse,
                'one_full20_term_relative_trace_witness': trace_witness,
                'all73_products_Frobenius120_fixed': True})
    save(args.output, out)
    print('PASS exact cubic trace extraction, actual73 target coordinates', args.j,
          'seconds', round(time.monotonic()-start, 3), flush=True)
    a = ActualModel(args.script_dir)
    np = a.np
    ww = [r.from_json([x]) for x in W]
    zero = lambda width: [r.zeros(1, width) for _ in range(3)]
    def pmul(x, y):
        result = [r.zeros(1, max(x[0][0].shape[1], y[0][0].shape[1])) for _ in range(5)]
        for i in range(3):
            for j in range(3):
                result[i+j] = r.add(result[i+j], r.mul(x[i], y[j]))
        for k in [4, 3]:
            result[k-2] = r.sub(result[k-2], a.scale(result[k], A))
            result[k-3] = r.sub(result[k-3], a.scale(result[k], B))
        return result[:3]
    def pmat(x, M):
        return [r.mm(y, M) for y in x]
    def pcols(x, I):
        return [r.cols(y, I) for y in x]
    V2 = pmat(pmul(pcols(ww, a.a2), pcols(ww, a.b2)), a.C2)
    pa, pb = zip(*[(i, j) for i in range(73) for j in range(i, 73)])
    actual_products = pmul(pcols(ww, pa), pcols(ww, pb))
    source_products = r.mul(r.cols(a.M['W'], pa), r.cols(a.M['W'], pb))
    product_coeff = r.rows(source_products, a.M['P2'])
    assert r.equal(r.mm(a.M['V2'], product_coeff), source_products)
    assert all(r.equal(x, y) for x, y in zip(pmat(V2, product_coeff), actual_products))
    helper = ProjectiveJetFrames(a)
    assert all(not np.any(r.mm(w, helper.candidates)[1]) for w in ww)
    hecke_path = args.script_dir/'data/p41_hecke47_compact.json.gz'
    hecke = read(hecke_path)
    T2 = r.from_json(hecke['operators']['2']['canonical_operator'])
    total = r.sub(a.scale(ww[0], 3), a.scale(ww[2], 2*A))
    source = r.from_json([rec['W_mod47four']])
    lhs = a.scale(r.mm(total, a.K1), pow(2, -1, Q))
    rhs = r.mm(r.mm(source, a.K1), T2)
    out.update({'T2_canonical_trace_left': r.to_json(lhs), 'T2_canonical_trace_right': r.to_json(rhs),
                'all2701_actual_quadratic_products_verified': True,
                'all73_cubic_coefficient_semilinear_descent_verified': True,
                'V2_coefficients_ascending_in_kernel_root': [r.to_json(v)[0] for v in V2]})
    out['input_sha256'].update(a.inputs)
    out['input_sha256'][hecke_path.name] = sha(hecke_path)
    save(args.output, out)
    assert r.equal(lhs, rhs), 'actual ordinary T2 canonical normalization mismatch'
    out.update({'complete_actual_T2_support': True, 'all54_canonical_T2_trace_identity_verified': True,
                'total_target_degree': 3, 'all53_local_QC_heights_complete': False})
    save(args.output, out)
    print('PASS ACTUAL ORDINARY T2 SUPPORT', args.j, 'all54 trace and2701 products SHA', sha(args.output),
          'seconds', round(time.monotonic()-start, 3), flush=True)


if __name__ == '__main__':
    main()
