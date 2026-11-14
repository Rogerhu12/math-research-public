#!/usr/bin/env python3
"""Actual T2 support for every ordinary rational disk, including split kernels.

Irreducible cubic kernels use the sealed R254 executor.  For factor types
1+2 or 1+1+1 all three kernels are evaluated, with their actual determinant2
41-level structures, in the existing unramified torsion field.  Vandermonde
interpolation recovers the complete etale cubic algebra over R2.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import runpy
import sys
import time

P, Q = 47, 47**4


def read(path):
    data = Path(path).read_bytes()
    return json.loads(gzip.decompress(data) if str(path).endswith('.gz') else data)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(data, sort_keys=True, separators=(',', ':'))+'\n').encode()
    tmp = path.with_suffix(path.suffix+'.new')
    tmp.write_bytes(gzip.compress(raw, mtime=0))
    tmp.replace(path)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--script-dir', type=Path, required=True)
    ap.add_argument('--ordinary-lifts', type=Path, required=True)
    ap.add_argument('--j', type=int, required=True)
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
    factorization = nmod_poly([B, A, 0, 1], P).factor()[1]
    factor_degrees = sorted((f.degree(), e) for f, e in factorization)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    if factor_degrees == [(3, 1)]:
        import p41_ordinary_t2_support47 as sealed
        sys.argv = [sealed.__file__, '--script-dir', str(args.script_dir),
                    '--ordinary-lifts', str(args.ordinary_lifts), '--j', str(args.j),
                    '--output', str(args.output)]
        runpy.run_path(sealed.__file__, run_name='__main__')
        return
    assert factor_degrees in [[(1, 1), (2, 1)], [(1, 1), (1, 1), (1, 1)]]
    K = Ring(rec['x_field_polynomial_ascending'])
    assert K.k % 40 == 0
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
    root0s = sorted(FK([B, A, 0, 1]).roots(multiplicities=False),
                   key=lambda x: tuple(int(c) for c in x.to_list()))
    assert len(root0s) == 3
    roots, root_pairs = [], []
    for rr in root0s:
        root = K([int(c) for c in rr.to_list()])
        for _ in range(2):
            root = root-(root**3+A*root+B)/(3*root*root+A)
        assert root**3+A*root+B == 0 and root.frobenius(2) == root
        pair = [root.trace()*pow(K.k, -1, Q) % Q,
                -(ii*root).trace()*pow(K.k, -1, Q) % Q]
        assert root == pair[0]+ii*pair[1]
        roots.append(root)
        root_pairs.append(pair)
    assert sum(roots, K(0)) == 0
    for i in range(3):
        for j in range(i):
            difference = [root_pairs[i][k]-root_pairs[j][k] for k in range(2)]
            assert (difference[0]**2+difference[1]**2) % P
    model_path = args.script_dir/'data/p41_makdisi47_certificate.json.gz'
    model = read(model_path)
    g = model['sl2_representatives'][rec['necklace_1based']-1]
    gh = [[[sum(g[s][u]*h[u][t] for u in range(2)) % 41 for t in range(2)] for s in range(2)]
          for h in model['sl2_normalizer_mod_signs']]
    output = {'level': 41, 'auxiliary_prime': P, 'precision': 4, 'modulus': Q,
              'source_disk_id': 'ORD_j'+str(args.j).zfill(2), 'source_curve': [A, B],
              'target_coordinate_ring': 'R2[r]/(r^3+A*r+B)',
              'kernel_polynomial_ascending': [B, A, 0, 1],
              'kernel_factor_degrees_mod47': factor_degrees,
              'all_three_kernel_roots_in_R2': root_pairs,
              'raw_target_pairing_exponent': 2, 'raw_level_determinant_mod41': 2,
              'target_A_coefficients_ascending': [-4*A % Q, 0, -15 % Q],
              'target_B_coefficients_ascending': [22*B % Q, 14*A % Q, 0],
              'source_necklace_1based': rec['necklace_1based'], 'source_necklace': rec['necklace'],
              'complete_actual_T2_support': False, 'branch_records': [],
              'input_sha256': {args.ordinary_lifts.name: sha(args.ordinary_lifts), model_path.name: sha(model_path)},
              'source_sha256': sha(__file__)}
    scale = 20*pow(K.k, -1, Q) % Q
    Wtargets = []
    for branch, root in enumerate(roots):
        u = 3*root*root+A

        def velu(T):
            inverse = (T[0]-root).inverse()
            return T[0]+u*inverse, T[1]*(1-u*inverse*inverse)

        D = Curve.__new__(Curve)
        D.K, D.A, D.B, D.f = K, A-5*u, B-7*root*u, C.f
        D.P, D.Q = velu(C.P), velu(C.Q)
        assert D.on_curve(D.P) and D.on_curve(D.Q)
        assert D.mul(D.P, 41) is None and D.mul(D.Q, 41) is None
        assert D.pairing() == zeta**2
        assert D.A == -4*A-15*root*root and D.B == 22*B+14*A*root
        ev = D.eisenstein()
        values, witness = [], None
        for row, (v, w) in enumerate(model['basis_pairs']):
            total = K(0)
            for h in gh:
                def index(v):
                    return (h[0][0]*v[0]+h[0][1]*v[1]) % 41+41*((h[1][0]*v[0]+h[1][1]*v[1]) % 41)
                total += ev[index(v)]*ev[index(w)]
            total *= C.f*zeta**2
            assert total.frobenius(40) == total
            value = [total.trace()*scale % Q, -(ii*total).trace()*scale % Q]
            if row == 0:
                relative, current = K(0), total
                for _ in range(20):
                    relative += current
                    current = current.frobenius(2)
                assert current == total and relative == value[0]+ii*value[1]
                witness = relative.to_list()
            values.append(value)
        W = rowmul(values, model['basis_inverse'])
        Wtargets.append(W)
        output['branch_records'].append({'branch_0based': branch, 'kernel_root_in_R2': root_pairs[branch],
                                        'raw_target_P': [x.to_list() for x in D.P],
                                        'raw_target_Q': [x.to_list() for x in D.Q],
                                        'W_actual_values_in_R2': W, 'actual_basis_values_in_R2': values,
                                        'all73_products_Frobenius40_fixed': True,
                                        'actual_pairing_and_41_torsion_verified': True,
                                        'trace_coordinate_scale': scale,
                                        'one_full20_term_relative_trace_witness': witness})
        save(args.output, output)
        print('PASS actual ordinary etale2 branch', args.j, branch+1, '/3',
              'seconds', round(time.monotonic()-start, 3), flush=True)
    R = r.from_json([[x] for x in root_pairs])
    one = r.column([[1, 0]]*3)
    vandermonde = r.hcat(one, R, r.mul(R, R))
    ivandermonde = r.inverse_matrix(vandermonde)
    assert r.equal(r.mm(vandermonde, ivandermonde), r.eye(3))
    Wmatrix = r.mm(ivandermonde, r.from_json(Wtargets))
    assert r.equal(r.mm(vandermonde, Wmatrix), r.from_json(Wtargets))
    W = r.to_json(Wmatrix)
    output.update({'W_coefficients_ascending_in_kernel_root': W,
                   'all_three_actual_branches_interpolated_exactly': True,
                   'vandermonde': r.to_json(vandermonde), 'inverse_vandermonde': r.to_json(ivandermonde)})
    save(args.output, output)
    a = ActualModel(args.script_dir)
    np = a.np
    ww = [r.from_json([x]) for x in W]

    def pmul(x, y):
        result = [r.zeros(1, max(x[0][0].shape[1], y[0][0].shape[1])) for _ in range(5)]
        for i in range(3):
            for j in range(3):
                result[i+j] = r.add(result[i+j], r.mul(x[i], y[j]))
        for k in [4, 3]:
            result[k-2] = r.sub(result[k-2], a.scale(result[k], A))
            result[k-3] = r.sub(result[k-3], a.scale(result[k], B))
        return result[:3]

    pmat = lambda x, M: [r.mm(y, M) for y in x]
    pcols = lambda x, I: [r.cols(y, I) for y in x]
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
    T2 = r.from_json(read(hecke_path)['operators']['2']['canonical_operator'])
    total = r.sub(a.scale(ww[0], 3), a.scale(ww[2], 2*A))
    source = r.from_json([rec['W_mod47four']])
    lhs = a.scale(r.mm(total, a.K1), pow(2, -1, Q))
    rhs = r.mm(r.mm(source, a.K1), T2)
    output.update({'T2_canonical_trace_left': r.to_json(lhs), 'T2_canonical_trace_right': r.to_json(rhs),
                   'all2701_actual_quadratic_products_verified': True,
                   'all73_cubic_coefficient_semilinear_descent_verified': True,
                   'V2_coefficients_ascending_in_kernel_root': [r.to_json(v)[0] for v in V2]})
    output['input_sha256'].update(a.inputs)
    output['input_sha256'][hecke_path.name] = sha(hecke_path)
    save(args.output, output)
    assert r.equal(lhs, rhs), 'actual ordinary etale T2 canonical normalization mismatch'
    output.update({'complete_actual_T2_support': True, 'all54_canonical_T2_trace_identity_verified': True,
                   'total_target_degree': 3, 'all53_local_QC_heights_complete': False})
    save(args.output, output)
    print('PASS ACTUAL ORDINARY ETALE T2 SUPPORT', args.j, 'all54 trace and2701 products SHA', sha(args.output),
          'seconds', round(time.monotonic()-start, 3), flush=True)


if __name__ == '__main__':
    main()
