#!/usr/bin/env python3
"""Independently verify the actual j1728 divisor and B_minus4 of R112."""
from functools import lru_cache
import gzip
import hashlib
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
from verify_p41_local47_torsion import Curve
from verify_p41_cm3_makdisi47 import FastRing, Jets, JetCurve
from verify_p41_makdisi47 import index, mm2, inv2, power_traces, qmul, qmatmul, qdet
from verify_p41_cusp_divisors47 import kernel, conjugate, identity, select, zero_matrix


class FamilyCurve(JetCurve):
    def __init__(self, jets):
        super().__init__(jets, jets.one)

    def on_curve(self, P):
        if P is None:
            return True
        j = self.j
        x, y = P
        return j.mul(y, y) == j.add(j.add(j.power(x, 3), x), j.parameter)


def eisenstein(j, P, Q):
    curve = FamilyCurve(j)
    Ps, Qs = [P], [Q]
    for _ in range(39):
        Ps.append(curve.add(Ps[-1], P))
        Qs.append(curve.add(Qs[-1], Q))
    numerator, denominator = [], []
    for base, multiples in ((P, Ps), (Q, Qs)):
        for k in range(39):
            if k == 0:
                numerator.append(j.add(j.scale(j.mul(base[0], base[0]), 3), j.one))
                denominator.append(j.scale(base[1], 2))
            else:
                numerator.append(j.sub(multiples[k][1], base[1]))
                denominator.append(j.sub(multiples[k][0], base[0]))
    for x, y in Ps:
        for xx, yy in Qs:
            numerator.append(j.sub(yy, y))
            denominator.append(j.sub(xx, x))
    prefix, product = [], j.one
    for d in denominator:
        assert any(x % 47 for x in d[0])
        prefix.append(product)
        product = j.mul(product, d)
    inverse = j.inverse(product)
    slopes = [None]*len(denominator)
    for k in range(len(slopes)-1, -1, -1):
        slopes[k] = j.mul(numerator[k], j.mul(inverse, prefix[k]))
        inverse = j.mul(inverse, denominator[k])
    assert inverse == j.one
    def total(values):
        out = j.zero
        for value in values:
            out = j.add(out, value)
        return out
    ep = j.scale(total(slopes[:39]), pow(41, -1, j.q))
    eq = j.scale(total(slopes[39:78]), pow(41, -1, j.q))
    pe, qe = [ep], [eq]
    for k in range(39):
        pe.append(j.sub(j.add(pe[-1], ep), slopes[k]))
        qe.append(j.sub(j.add(qe[-1], eq), slopes[k+39]))
    assert pe[-1] == j.scale(ep, -1) and qe[-1] == j.scale(eq, -1)
    values = [j.zero]*1681
    for a in range(1, 41):
        values[index(a, 0)] = pe[a-1]
        values[index(0, a)] = qe[a-1]
    for a in range(1, 41):
        for b in range(1, 41):
            values[index(a, b)] = j.sub(j.add(pe[a-1], qe[b-1]), slopes[78+40*(a-1)+b-1])
    for a in range(41):
        for b in range(41):
            assert values[index(-a, -b)] == j.scale(values[index(a, b)], -1)
    return values


def geometry(U, F, model, data):
    ns = model['necklaces']
    lookup = {tuple(ne): n for n, ne in enumerate(ns)}
    def act(A, n):
        a, e = ns[n]
        R = [[a, (e-a*a) % 41], [1, -a % 41]]
        T = mm2(mm2(A, R), inv2(A))
        scale = pow(T[1][0], -1, 41)
        a = T[0][0]*scale % 41
        e = (a*a+scale*T[0][1]) % 41
        return lookup[a, e]
    fixed = [n for n in range(820) if act(U, n) == n]
    assert len(fixed) == 20 and [n+1 for n in fixed] == data['elliptic_necklace_indices_1based']
    tau = [fixed.index(act(F, n)) for n in fixed]
    assert [n+1 for n in tau] == data['elliptic_frobenius_permutation_1based']
    assert sum(n == k for n, k in enumerate(tau)) == 2
    assert all(tau[tau[n]] == n for n in range(20))
    return fixed, tau


def trace_evaluations(values, r, ew, ii, model, fixed):
    reps, signed = [], [0]*1681
    for k in range(1, 1681):
        neg = index(-(k % 41), -(k//41))
        if k < neg:
            reps.append(k)
            signed[k], signed[neg] = len(reps), -len(reps)
    assert len(reps) == 840
    E0 = [values[k][0] for k in reps]
    E1 = [values[k][1] for k in reps]
    traces = [x % r.q for x in power_traces(r.f, 237)]
    ew_i = r.mul(ii, ew)
    quarter = pow(4, -1, r.q)
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
    for n in fixed:
        gh = [mm2(model['sl2_representatives'][n], h) for h in model['sl2_normalizer_mod_signs']]
        row0, row1 = [], []
        for v, w in model['basis_pairs']:
            a0, b0, a1, b1 = 0, 0, 0, 0
            for h in gh:
                vindex = signed[index(h[0][0]*v[0]+h[0][1]*v[1], h[1][0]*v[0]+h[1][1]*v[1])]
                windex = signed[index(h[0][0]*w[0]+h[0][1]*w[1], h[1][0]*w[0]+h[1][1]*w[1])]
                sign = 1 if vindex*windex > 0 else -1
                a, b = sorted((abs(vindex)-1, abs(windex)-1))
                const, deriv = pair(a, b)
                a0 += sign*const[0]
                b0 += sign*const[1]
                a1 += sign*deriv[0]
                b1 += sign*deriv[1]
            row0.append([a0 % r.q, b0 % r.q])
            row1.append([a1 % r.q, b1 % r.q])
        raw0.append(row0)
        raw1.append(row1)
    assert zero_matrix(raw0)
    return qmatmul(raw1, model['basis_inverse'], r.q)


def main(path):
    encoded = path.read_bytes()
    data = json.loads(encoded)
    assert (data['level'], data['auxiliary_prime'], data['precision'], data['curve_A'], data['curve_B']) == (41, 47, 4, 1, 0)
    q = data['modulus']
    assert q == 47**4
    sources = {}
    for name, digest in data['source_sha256'].items():
        raw = path.with_name(name).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == digest
        sources[name] = json.loads(gzip.decompress(raw) if name.endswith('.gz') else raw)
    torsion = sources['p41_local47_torsion_certificate.json']
    model = sources['p41_makdisi47_certificate.json.gz']
    divisors = sources['p41_cusp_divisors47_certificate.json.gz']
    r = FastRing(torsion['field_polynomial_ascending'], q)
    ii = r.element(model['sqrt_minus_one_lift'])
    phi = r.element(torsion['frobenius_lift'])
    reference = next(c for c in torsion['curves'] if c['label'] == 'Makdisi_j9_fibre')
    ew = r.element(reference['weil_pairing'])
    P0 = tuple(r.element(c) for c in data['P_constant'])
    Qold = tuple(r.element(c) for c in data['Q_old_constant'])
    cold = Curve(r, 1, 0)
    assert cold.on_curve(P0) and cold.on_curve(Qold)
    assert cold.mul(P0, 41) is None and cold.mul(Qold, 41) is None
    assert tuple(r.evaluate(c, phi) for c in P0) == Qold
    assert tuple(r.evaluate(c, phi) for c in Qold) == cold.mul(P0, -47)
    wold = r.element(data['old_Weil_pairing'])
    direct = r.scale(r.mul(cold.miller(P0, Qold, 41), r.inverse(cold.miller(Qold, P0, 41))), -1)
    assert direct == wold
    adjustment = data['pairing_adjustment']
    assert adjustment == 30 and r.power(wold, adjustment) == ew
    Q0 = cold.mul(Qold, adjustment)
    U, F = data['CM_unit_matrix'], data['frobenius_torsion_matrix']
    assert U == [[28, 21], [29, 13]] and F == [[0, 25], [26, 0]]
    assert mm2(U, U) == [[40, 0], [0, 40]]
    assert mm2(F, F) == [[35, 0], [0, 35]]
    assert mm2(F, U) == [[-c % 41 for c in row] for row in mm2(U, F)]
    for col, T in enumerate((P0, Q0)):
        expected = cold.add(cold.mul(P0, U[0][col]), cold.mul(Q0, U[1][col]))
        assert expected == (r.scale(T[0], -1), r.mul(ii, T[1]))
    j = Jets(r, 2)
    P = tuple(tuple(r.element(c) for c in coordinate) for coordinate in data['P_jets'])
    Q = tuple(tuple(r.element(c) for c in coordinate) for coordinate in data['Q_jets'])
    curve = FamilyCurve(j)
    assert tuple(c[0] for c in P) == P0 and tuple(c[0] for c in Q) == Q0
    assert curve.on_curve(P) and curve.on_curve(Q)
    assert curve.mul(P, 41) is None and curve.mul(Q, 41) is None
    def frobenius(T):
        return tuple(tuple(r.evaluate(c, phi) for c in coordinate) for coordinate in T)
    assert curve.mul(frobenius(P), adjustment) == Q
    assert frobenius(Q) == curve.mul(P, 35*adjustment)
    Pneg = tuple(j.rescale_parameter(c, r.element(-1)) for c in P)
    Qneg = tuple(j.rescale_parameter(c, r.element(-1)) for c in Q)
    for col, T in enumerate((P, Q)):
        expected = curve.add(curve.mul(Pneg, U[0][col]), curve.mul(Qneg, U[1][col]))
        assert expected == (j.scale(T[0], -1), j.mul(j.constant(ii), T[1]))
    fixed, tau = geometry(U, F, model, data)
    print('Actual41-torsion, Weil calibration, the family unit action and all20 elliptic points verified.', flush=True)
    values = eisenstein(j, P, Q)
    coarse = trace_evaluations(values, r, ew, ii, model, fixed)
    assert coarse == data['coarse_point_values']
    assert qmatmul(coarse, model['frobenius_basis_matrix'], q) == conjugate([coarse[n] for n in tau], q)
    for row in coarse:
        assert any((a*a+b*b) % 47 for a, b in row)
    print('All20 actual coarse CM4 point values reconstructed by mixed trace Gram matrices.', flush=True)

    K1 = kernel(73, divisors['cusp_rank_columns_1based'], divisors['cusp_free_columns_1based'], divisors['canonical_kernel_block'])
    KI = kernel(199, divisors['K_rank_columns_1based'], divisors['K_free_columns_1based'], divisors['K_kernel_block'])
    fcoeff = qmatmul(K1, [[c] for c in divisors['canonical_coefficients']], q)
    fvalues = [row[0] for row in qmatmul(coarse, fcoeff, q)]
    assert fvalues == data['canonical_point_values']
    assert all((a*a+b*b) % 47 for a, b in fvalues)
    pairs = divisors['square_basis_monomials_1based']
    C2 = divisors['square_basis_inverse']
    cm2 = qmatmul([[qmul(row[a-1], row[b-1], q) for a, b in pairs] for row in coarse], C2, q)
    restriction = qmatmul(cm2, KI, q)
    minor = select(restriction, data['restriction_rank_rows_1based'], data['restriction_rank_columns_1based'])
    determinant = qdet([[[a % 47, b % 47] for a, b in row] for row in minor], 47)
    assert list(determinant) == data['restriction_unit_minor_mod47'] == [34, 31]
    assert sum(c*c for c in determinant) % 47 == 2
    KZ = kernel(93, data['restriction_rank_columns_1based'], data['restriction_free_columns_1based'], data['point_kernel_block'])
    assert len(KZ[0]) == 73 and zero_matrix(qmatmul(restriction, KZ, q))
    Bcoords = qmatmul(KI, KZ, q)
    free = [divisors['K_free_columns_1based'][n-1] for n in data['restriction_free_columns_1based']]
    assert free == data['point_free_coordinates_1based']
    assert select(Bcoords, free) == identity(73)
    assert zero_matrix(qmatmul(cm2, Bcoords, q))
    W = model['evaluation_matrix']
    V2 = qmatmul([[qmul(row[a-1], row[b-1], q) for a, b in pairs] for row in W], C2, q)
    FrobV2 = conjugate(select(V2, model['frobenius_permutation_1based']), q)
    A2 = select(FrobV2, divisors['square_pivot_rows_1based'])
    assert qmatmul(V2, A2, q) == FrobV2
    FB = data['point_frobenius_basis_matrix']
    assert qmatmul(Bcoords, FB, q) == qmatmul(A2, conjugate(Bcoords, q), q)
    assert qmatmul(FB, conjugate(FB, q), q) == identity(73)
    assert data['Jacobian_class_convention'] == '[effective_divisor - base_divisor] = B_minus4'
    print('The genuine integral class B_minus4 and its full73-dimensional descended divisor space verified.', flush=True)
    print('SHA256', hashlib.sha256(encoded).hexdigest(), flush=True)


if __name__ == '__main__':
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else
         Path(__file__).with_name('data')/'p41_cm4_divisor47_certificate.json')
