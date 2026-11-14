#!/usr/bin/env python3
"""Standard-library verification of actual cusps and divisor ideals in R110."""
import gzip
import hashlib
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
from verify_p41_cm3_makdisi47 import FastRing
from verify_p41_makdisi47 import mm2, inv2, qmul, qinv, qmatmul, qdet


def conjugate(M, q):
    return [[[a, -b % q] for a, b in row] for row in M]


def identity(n):
    return [[[int(i == j), 0] for j in range(n)] for i in range(n)]


def select(M, rows, cols=None):
    return [[M[i-1][j-1] for j in cols] for i in rows] if cols is not None else [M[i-1] for i in rows]


def kernel(n, cols, free, block):
    assert sorted(cols + free) == list(range(1, n+1))
    assert len(set(cols)) == len(cols) and len(block) == len(cols)
    K = [[[0, 0] for _ in free] for _ in range(n)]
    for j, k in enumerate(free):
        K[k-1][j] = [1, 0]
    for k, row in zip(cols, block):
        assert len(row) == len(free)
        K[k-1] = row
    return K


def zero_matrix(M):
    return all(all(not any(c) for c in row) for row in M)


def field_qmatmul(A, B, r, ii):
    """Multiply an R80 matrix by an R2 matrix, using integer dot products."""
    br = list(zip(*[[c[0] for c in row] for row in B]))
    bi = list(zip(*[[c[1] for c in row] for row in B]))
    out = []
    for row in A:
        coefficients = list(zip(*row))
        target = []
        for cr, ci in zip(br, bi):
            real = tuple(sum(a*b for a, b in zip(v, cr)) % r.q for v in coefficients)
            imag = tuple(sum(a*b for a, b in zip(v, ci)) % r.q for v in coefficients)
            target.append(r.add(real, r.mul(ii, imag)))
        out.append(target)
    return out


def fielddet(M, r):
    A = [[r.element(c) for c in row] for row in M]
    n = len(A)
    det = r.one
    for k in range(n):
        candidates = [j for j in range(k, n) if A[j][k] != r.zero]
        assert candidates, ('singular field minor', k)
        j = candidates[0]
        if j != k:
            A[k], A[j] = A[j], A[k]
            det = r.scale(det, -1)
        det = r.mul(det, A[k][k])
        inverse = r.inverse(A[k][k])
        for j in range(k+1, n):
            scalar = r.mul(A[j][k], inverse)
            for h in range(k+1, n):
                A[j][h] = r.sub(A[j][h], r.mul(scalar, A[k][h]))
    return det


def cusp_geometry(data, model):
    ns = model['necklaces']
    lookup = {tuple(c): i for i, c in enumerate(ns)}
    def action(M, n):
        a, e = ns[n]
        R = [[a, (e-a*a) % 41], [1, -a % 41]]
        T = mm2(mm2(M, R), inv2(M))
        scale = pow(T[1][0], -1, 41)
        a = T[0][0]*scale % 41
        e = (a*a+T[0][1]*scale) % 41
        return lookup[a, e]
    U, F = [[1, 0], [1, 1]], [[1, 0], [0, 6]]
    orbit = [-1]*820
    reps = []
    for n in range(820):
        if orbit[n] >= 0:
            continue
        reps.append(n)
        m, count = n, 0
        while orbit[m] < 0:
            orbit[m] = len(reps)-1
            count += 1
            m = action(U, m)
        assert m == n and count == 41
    rho = [orbit[action(F, n)] for n in reps]
    assert len(reps) == 20
    assert [n+1 for n in reps] == data['cusp_representatives_1based']
    assert [n+1 for n in orbit] == data['necklace_to_cusp_1based']
    assert [n+1 for n in rho] == data['cusp_frobenius_permutation_1based']
    cycle, n = [], 0
    while n not in cycle:
        cycle.append(n)
        n = rho[n]
    assert n == 0 and len(cycle) == 20
    return reps, rho


def cusp_raw(reps, model, q):
    """Compute Tate coefficients as integer cyclotomic polynomials, not field slopes."""
    constants = {}
    for d in range(1, 41):
        v = [0]*41
        v[0] = -41
        for k in range(1, 41):
            v[-d*k % 41] -= 2*k
        constants[d] = v
    weights = [pow(36, j, 41) for j in range(20)]
    scalars = [pow(35, j, 41) for j in range(20)]

    def add_constant(out, c, d, exponent, factor):
        if c:
            out[exponent % 41] += factor*(41-2*c)
        else:
            for k, value in enumerate(constants[d]):
                out[(exponent+k) % 41] += factor*value

    raw0, raw1 = [], []
    for n in reps:
        gh = [mm2(model['sl2_representatives'][n], h) for h in model['sl2_normalizer_mod_signs']]
        row0, row1 = [], []
        for v, w in model['basis_pairs']:
            a0, a1 = [0]*41, [0]*41
            for h in gh:
                cv = (h[0][0]*v[0]+h[0][1]*v[1]) % 41
                dv = (h[1][0]*v[0]+h[1][1]*v[1]) % 41
                cw = (h[0][0]*w[0]+h[0][1]*w[1]) % 41
                dw = (h[1][0]*w[0]+h[1][1]*w[1]) % 41
                assert cv or cw
                for scalar, exponent in zip(scalars, weights):
                    c, d, cc, dd = [scalar*x % 41 for x in (cv, dv, cw, dw)]
                    if c:
                        add_constant(a0, cc, dd, exponent, 41-2*c)
                    else:
                        add_constant(a0, c, d, exponent, 41-2*cc)
                    if c in (1, 40):
                        sign = 1 if c == 1 else -1
                        add_constant(a1, cc, dd, exponent-sign*d, sign)
                    if cc in (1, 40):
                        sign = 1 if cc == 1 else -1
                        add_constant(a1, c, d, exponent-sign*dd, sign)
            row0.append([(x-a0[40])*pow(82*82, -1, q) % q for x in a0[:40]])
            row1.append([(x-a1[40])*pow(82, -1, q) % q for x in a1[:40]])
        raw0.append(row0)
        raw1.append(row1)
    return raw0, raw1


def normalize_cyclotomic(raw, C, powers, r, ii):
    realC = list(zip(*[[c[0] for c in row] for row in C]))
    imagC = list(zip(*[[c[1] for c in row] for row in C]))
    power_columns = list(zip(*powers))
    out = []
    for row in raw:
        coefficients = list(zip(*row))
        normalized = []
        for cr, ci in zip(realC, imagC):
            real = [sum(a*b for a, b in zip(v, cr)) % r.q for v in coefficients]
            imag = [sum(a*b for a, b in zip(v, ci)) % r.q for v in coefficients]
            rr = tuple(sum(a*b for a, b in zip(real, col)) % r.q for col in power_columns)
            im = tuple(sum(a*b for a, b in zip(imag, col)) % r.q for col in power_columns)
            normalized.append(r.add(rr, r.mul(ii, im)))
        out.append(normalized)
    return out


def main(path):
    encoded = path.read_bytes()
    data = json.loads(gzip.decompress(encoded))
    assert data['level'] == 41 and data['auxiliary_prime'] == 47 and data['precision'] == 4
    q = data['modulus']
    assert q == 47**4
    sources = {}
    for name, digest in data['source_sha256'].items():
        raw = path.with_name(name).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == digest
        sources[name] = json.loads(gzip.decompress(raw) if name.endswith('.gz') else raw)
    torsion = sources['p41_local47_torsion_certificate.json']
    model = sources['p41_makdisi47_certificate.json.gz']
    cm = sources['p41_cm3_makdisi47_certificate.json']
    r = FastRing(torsion['field_polynomial_ascending'], q)
    rf = FastRing(torsion['field_polynomial_ascending'], 47)
    ii = r.element(model['sqrt_minus_one_lift'])
    ref = next(c for c in torsion['curves'] if c['label'] == 'Makdisi_j9_fibre')
    ew = r.element(ref['weil_pairing'])
    powers = [r.one]
    for _ in range(40):
        powers.append(r.mul(powers[-1], ew))
    assert r.mul(powers[-1], ew) == r.one and ew != r.one
    reps, rho = cusp_geometry(data, model)
    raw0, raw1 = cusp_raw(reps, model, q)
    M = normalize_cyclotomic(raw0, model['basis_inverse'], powers[:40], r, ii)
    assert M == [[r.element(c) for c in row] for row in data['cusp_values']]
    N = normalize_cyclotomic(raw1, model['basis_inverse'], powers[:40], r, ii)
    assert all(all(sum(M[n][k][h] for n in range(20)) % q == 0 for h in range(80)) for k in range(73))
    MA = field_qmatmul(M, model['frobenius_basis_matrix'], r, ii)
    phiM = normalize_cyclotomic(raw0, conjugate(model['basis_inverse'], q),
                               [powers[6*k % 41] for k in range(40)], r, ii)
    assert all(MA[rho[n]] == phiM[n] for n in range(20))
    determinant = fielddet(select(M, data['cusp_rank_rows_1based'], data['cusp_rank_columns_1based']), rf)
    assert determinant == tuple(data['cusp_unit_minor_mod47']) and determinant != rf.zero
    K = kernel(73, data['cusp_rank_columns_1based'], data['cusp_free_columns_1based'], data['canonical_kernel_block'])
    assert len(K[0]) == 54 and zero_matrix(field_qmatmul(M, K, r, ii))
    AK = data['canonical_frobenius_matrix']
    assert qmatmul(model['frobenius_basis_matrix'], conjugate(K, q), q) == qmatmul(K, AK, q)
    assert qmatmul(AK, conjugate(AK, q), q) == identity(54)
    coeff = data['canonical_coefficients']
    seed = data['canonical_trace_seed']
    trace = qmatmul(AK, conjugate([[c] for c in seed], q), q)
    assert coeff == [[(a+c[0][0]) % q, (b+c[0][1]) % q] for (a, b), c in zip(seed, trace)]
    fcoeff = qmatmul(K, [[c] for c in coeff], q)
    W = model['evaluation_matrix']
    fvalues = [row[0] for row in qmatmul(W, fcoeff, q)]
    assert all((a*a+b*b) % 47 for a, b in fvalues)
    cmvalue = qmatmul([cm['coarse_evaluation_coefficients'][0]], fcoeff, q)[0][0]
    assert cmvalue == data['canonical_CM_value'] and sum(x*x for x in cmvalue) % 47
    leading = [row[0] for row in field_qmatmul(N, fcoeff, r, ii)]
    assert leading == [r.element(c) for c in data['canonical_cusp_leading_values']]
    assert all(any(c % 47 for c in value) for value in leading)
    print('All20 actual cusps, Tate coefficients, residues, descent and the full canonical kernel verified.', flush=True)

    pairs = data['square_basis_monomials_1based']
    assert len(pairs) == 199
    V = [[qmul(row[i-1], row[j-1], q) for i, j in pairs] for row in W]
    pivotrows = data['square_pivot_rows_1based']
    C = data['square_basis_inverse']
    assert qmatmul(select(V, pivotrows), C, q) == identity(199)
    V2 = qmatmul(V, C, q)
    assert select(V2, pivotrows) == identity(199)
    M2raw = [[r.mul(row[i-1], row[j-1]) for i, j in pairs] for row in M]
    M2 = field_qmatmul(M2raw, C, r, ii)
    Ddet = fielddet(select(M2, data['D_rank_rows_1based'], data['D_rank_columns_1based']), rf)
    assert Ddet != rf.zero
    KD = kernel(199, data['D_rank_columns_1based'], data['D_free_columns_1based'], data['D_kernel_block'])
    assert len(KD[0]) == 179 and zero_matrix(field_qmatmul(M2, KD, r, ii))
    print('The full199-dimensional square space and the actual179-dimensional cusp divisor ideal verified.', flush=True)

    seedg = data['second_canonical_trace_seed']
    coeffg = data['second_canonical_coefficients']
    traceg = qmatmul(AK, conjugate([[c] for c in seedg], q), q)
    assert coeffg == [[(a+c[0][0]) % q, (b+c[0][1]) % q] for (a, b), c in zip(seedg, traceg)]
    gcoeff = qmatmul(K, [[c] for c in coeffg], q)
    gvalues = [row[0] for row in qmatmul(W, gcoeff, q)]
    ratio = [qmul(g, qinv(f, q), q) for f, g in zip(fvalues, gvalues)]
    scaled = [[qmul(t, c, q) for c in row] for t, row in zip(ratio, V2)]
    interpolated = qmatmul(V2, select(scaled, pivotrows), q)
    R = [[[(x-u) % q, (y-v) % q] for (x, y), (u, v) in zip(row, other)]
         for row, other in zip(scaled, interpolated)]
    minor = select(R, data['K_rank_rows_1based'], data['K_rank_columns_1based'])
    detK = qdet([[[a % 47, b % 47] for a, b in row] for row in minor], 47)
    assert list(detK) == data['K_unit_minor_mod47'] and detK != (0, 0)
    KI = kernel(199, data['K_rank_columns_1based'], data['K_free_columns_1based'], data['K_kernel_block'])
    assert len(KI[0]) == 93 and zero_matrix(qmatmul(R, KI, q))
    vcm = cm['coarse_evaluation_coefficients'][0]
    cm2 = qmatmul([[qmul(vcm[i-1], vcm[j-1], q) for i, j in pairs]], C, q)[0]
    assert cm2 == data['square_CM_values']
    assert any((a*a+b*b) % 47 for a, b in cm2)
    zerocoord = [[qmul(fvalues[n-1], w, q) for w in W[n-1]] for n in pivotrows]
    zeroeval = [[qmul(f, w, q) for w in row] for f, row in zip(fvalues, W)]
    assert qmatmul(V2, zerocoord, q) == [list(map(list, row)) for row in zeroeval]
    assert zero_matrix(qmatmul(R, zerocoord, q))
    assert zero_matrix(field_qmatmul(M2, zerocoord, r, ii))
    print('The actual93-dimensional canonical divisor ideal, CM condition and zero Jacobian representation verified.', flush=True)
    print('SHA256', hashlib.sha256(encoded).hexdigest(), flush=True)


if __name__ == '__main__':
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else
         Path(__file__).with_name('data')/'p41_cusp_divisors47_certificate.json.gz')
