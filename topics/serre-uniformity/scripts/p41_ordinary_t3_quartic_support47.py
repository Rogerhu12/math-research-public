#!/usr/bin/env python3
"""Actual T3 support for an irreducible quartic kernel over the ordinary base.

Every branch uses actual raw determinant3 level and the original zeta.
Since the kernel and cyclotomic fields intersect, first interpolate raw
products in the formal kernel variable; only then take the20-term trace
coefficientwise.  Tracing one geometric target would give the wrong divisor.
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
    kernel_coefficients = [-A*A*pow(3, -1, Q) % Q, 4*B % Q, 2*A % Q, 0, 1]
    factorization = nmod_poly(kernel_coefficients, P).factor()[1]
    factor_degrees = sorted((f.degree(), e) for f, e in factorization)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    assert sum(d*e for d, e in factor_degrees) == 4
    assert factor_degrees == [(4, 1)], "This executor is for the irreducible quartic case"
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
    root0s = sorted(FK([x % P for x in kernel_coefficients]).roots(multiplicities=False),
                   key=lambda x: tuple(int(c) for c in x.to_list()))
    assert len(root0s) == 4
    roots = []
    for rr in root0s:
        root = K([int(c) for c in rr.to_list()])
        for _ in range(2):
            root = root-(3*root**4+6*A*root*root+12*B*root-A*A)/(12*root**3+12*A*root+12*B)
        assert 3*root**4+6*A*root*root+12*B*root-A*A == 0
        assert root.frobenius(4) == root and root.frobenius(2) != root
        assert (root**3+A*root+B)*(root**3+A*root+B).inverse() == 1
        roots.append(root)
    assert sum(roots, K(0)) == 0
    for i in range(4):
        for j in range(i):
            difference = roots[i]-roots[j]
            assert difference*difference.inverse() == 1
    model_path = args.script_dir/'data/p41_makdisi47_certificate.json.gz'
    model = read(model_path)
    hecke_path = args.script_dir/'data/p41_hecke47_full_saved.json.gz'
    hecke = read(hecke_path)['operators']['3']
    target_necklace = hecke['necklace_transport_1based'][rec['necklace_1based']-1]
    g = model['sl2_representatives'][target_necklace-1]
    # With raw phi(P),phi(Q), labels (a,b/3) give the original pairing zeta.
    # The transported necklace is diag(1,3) acting on the source necklace.
    # No raw 41-level basis is discarded or replaced in the saved certificate.
    inverse3mod41 = pow(3, -1, 41)
    g = [list(g[0]), [(inverse3mod41*x) % 41 for x in g[1]]]
    assert (g[0][0]*g[1][1]-g[0][1]*g[1][0]) % 41 == inverse3mod41
    gh = [[[sum(g[s][u]*h[u][t] for u in range(2)) % 41 for t in range(2)] for s in range(2)]
          for h in model['sl2_normalizer_mod_signs']]
    output = {'level': 41, 'auxiliary_prime': P, 'precision': 4, 'modulus': Q,
              'source_disk_id': 'ORD_j'+str(args.j).zfill(2), 'source_curve': [A, B],
              'target_coordinate_ring': 'R2[r]/(r^4+2*A*r^2+4*B*r-A^2/3)',
              'kernel_polynomial_ascending': kernel_coefficients,
              'kernel_factor_degrees_mod47': factor_degrees,
              'all_four_kernel_roots_in_original_field': [x.to_list() for x in roots],
              'raw_target_pairing_exponent': 3, 'raw_level_determinant_mod41': 3,
              'target_A_coefficients_ascending': [-9*A % Q, 0, -30 % Q, 0],
              'target_B_coefficients_ascending': [-27*B % Q, -42*A % Q, 0, -70 % Q],
              'source_necklace_1based': rec['necklace_1based'], 'source_necklace': rec['necklace'],
              'target_normalized_necklace_1based': target_necklace,
              'evaluation_vector_matrix_from_raw_basis': g,
              'evaluation_pairing_and_trace_coefficient': 'Original zeta; raw formal-r interpolation then20-term trace coefficientwise over R2',
              'complete_actual_T3_support': False, 'branch_records': [],
              'input_sha256': {args.ordinary_lifts.name: sha(args.ordinary_lifts), model_path.name: sha(model_path)},
              'source_sha256': sha(__file__)}
    scale = 20*pow(K.k, -1, Q) % Q
    raw_products = []
    for branch, root in enumerate(roots):
        t = 2*(3*root*root+A)
        v = 4*(root**3+A*root+B)

        def velu(T):
            inverse = (T[0]-root).inverse()
            return T[0]+t*inverse+v*inverse*inverse, T[1]*(1-t*inverse*inverse-2*v*inverse**3)

        D = Curve.__new__(Curve)
        D.K, D.A, D.B, D.f = K, A-5*t, B-7*(v+root*t), C.f
        D.P, D.Q = velu(C.P), velu(C.Q)
        assert D.on_curve(D.P) and D.on_curve(D.Q)
        assert D.mul(D.P, 41) is None and D.mul(D.Q, 41) is None
        assert D.pairing() == zeta**3
        assert D.A == -9*A-30*root*root and D.B == -27*B-42*A*root-70*root**3
        assert (4*D.A**3+27*D.B**2)*(4*D.A**3+27*D.B**2).inverse() == 1
        ev = D.eisenstein()
        products = []
        for row, (v, w) in enumerate(model['basis_pairs']):
            total = K(0)
            for h in gh:
                def index(v):
                    return (h[0][0]*v[0]+h[0][1]*v[1]) % 41+41*((h[1][0]*v[0]+h[1][1]*v[1]) % 41)
                total += ev[index(v)]*ev[index(w)]
            total *= C.f*zeta
            assert total.frobenius(40) == total
            products.append(total)
        raw_products.append(products)
        output['branch_records'].append({'branch_0based': branch, 'kernel_root_in_original_field': root.to_list(),
                                        'raw_target_P': [x.to_list() for x in D.P],
                                        'raw_target_Q': [x.to_list() for x in D.Q],
                                        'actual_raw_basis_products_in_original_field': [x.to_list() for x in products],
                                        'all73_products_Frobenius40_fixed': True,
                                        'actual_pairing_and_41_torsion_verified': True})
        save(args.output, output)
        print('PASS actual ordinary T3 branch', args.j, branch+1, '/4',
              'seconds', round(time.monotonic()-start, 3), flush=True)
    # The complete split algebra over K is evaluated at all four roots.
    # Lagrange reconstruction is done before tracing, so Frobenius acts on
    # source/cyclotomic coefficients while the formal kernel variable stays fixed.
    lagrange = []
    for branch in range(4):
        pol, denominator = [K(1)], K(1)
        for other in range(4):
            if other == branch:
                continue
            nxt = [K(0) for _ in range(len(pol)+1)]
            for k, x in enumerate(pol):
                nxt[k] -= roots[other]*x
                nxt[k+1] += x
            pol = nxt
            denominator *= roots[branch]-roots[other]
        pol = [x/denominator for x in pol]
        for other in range(4):
            value = sum((pol[k]*roots[other]**k for k in range(4)), K(0))
            assert value == int(branch == other)
        lagrange.append(pol)
    values = [[] for _ in range(4)]
    witness = []
    all_raw_coefficients = []
    for row in range(73):
        coefficients = [sum((lagrange[b][k]*raw_products[b][row] for b in range(4)), K(0)) for k in range(4)]
        all_raw_coefficients.append([x.to_list() for x in coefficients])
        for branch in range(4):
            recovered = sum((coefficients[k]*roots[branch]**k for k in range(4)), K(0))
            assert recovered == raw_products[branch][row]
        for k, value in enumerate(coefficients):
            assert value.frobenius(40) == value
            pair = [value.trace()*scale % Q, -(ii*value).trace()*scale % Q]
            values[k].append(pair)
            if row == 0:
                relative, current = K(0), value
                for _ in range(20):
                    relative += current
                    current = current.frobenius(2)
                assert current == value and relative == pair[0]+ii*pair[1]
                witness.append(relative.to_list())
    W = [rowmul(value, model['basis_inverse']) for value in values]
    output.update({'W_coefficients_ascending_in_kernel_root': W,
                   'actual_basis_value_coefficients_ascending_in_kernel_root': values,
                   'raw_basis_product_coefficients_before_cyclotomic_trace': all_raw_coefficients,
                   'all_four_actual_branches_interpolated_before_cyclotomic_trace': True,
                   'lagrange_coefficients_in_original_field': [[x.to_list() for x in pol] for pol in lagrange],
                   'trace_coordinate_scale': scale,
                   'four_full20_term_relative_trace_witnesses_for_first_basis_row': witness,
                   'all292_raw_coefficients_Frobenius40_fixed': True})
    save(args.output, output)
    a = ActualModel(args.script_dir)
    np = a.np
    ww = [r.from_json([x]) for x in W]

    def pmul(x, y):
        result = [r.zeros(1, max(x[0][0].shape[1], y[0][0].shape[1])) for _ in range(7)]
        for i in range(4):
            for j in range(4):
                result[i+j] = r.add(result[i+j], r.mul(x[i], y[j]))
        for k in [6, 5, 4]:
            for j in range(4):
                result[k-4+j] = r.sub(result[k-4+j], a.scale(result[k], kernel_coefficients[j]))
        return result[:4]

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
    T3 = r.from_json(hecke['canonical_operator'])
    fullT3 = r.from_json(hecke['weight2_operator'])
    total = r.sub(r.sub(a.scale(ww[0], 4), a.scale(ww[2], 4*A)), a.scale(ww[3], 12*B))
    source = r.from_json([rec['W_mod47four']])
    full_lhs = a.scale(total, pow(3, -1, Q))
    full_rhs = r.mm(source, fullT3)
    lhs = r.mm(full_lhs, a.K1)
    rhs = r.mm(r.mm(source, a.K1), T3)
    output.update({'T3_canonical_trace_left': r.to_json(lhs), 'T3_canonical_trace_right': r.to_json(rhs),
                   'T3_full_weight2_trace_left': r.to_json(full_lhs), 'T3_full_weight2_trace_right': r.to_json(full_rhs),
                   'all2701_actual_quadratic_products_verified': True,
                   'all73_quartic_coefficient_semilinear_descent_verified': True,
                   'V2_coefficients_ascending_in_kernel_root': [r.to_json(v)[0] for v in V2]})
    output['input_sha256'].update(a.inputs)
    output['input_sha256'][hecke_path.name] = sha(hecke_path)
    save(args.output, output)
    assert r.equal(full_lhs, full_rhs), 'actual ordinary T3 full weight2 normalization mismatch'
    assert r.equal(lhs, rhs), 'actual ordinary T3 canonical normalization mismatch'
    output.update({'complete_actual_T3_support': True, 'all54_canonical_T3_trace_identity_verified': True,
                   'all73_full_weight2_T3_trace_identity_verified': True,
                   'total_target_degree': 4, 'all53_local_QC_heights_complete': False})
    save(args.output, output)
    print('PASS ACTUAL ORDINARY T3 SUPPORT', args.j, 'all73 and54 traces,2701 products SHA', sha(args.output),
          'seconds', round(time.monotonic()-start, 3), flush=True)


if __name__ == '__main__':
    main()
