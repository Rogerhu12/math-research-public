#!/usr/bin/env python3
"""R257 exact rational maps, ordinary 2 generator and labeled finite symbols.

Python standard library only; imports the previously published R219 finite
field and elliptic-curve implementation.  The separate PARI script certifies
the class number.  This script never treats a saved bnfinit value as a proof.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

from verify_o6_single_real_norm_target import Fp2, EC


class RationalField:
    def __init__(self, coefficients):
        self.f = [Q(a) / Q(coefficients[-1]) for a in coefficients]
        self.n = len(self.f) - 1
        self.zero = [Q(0)] * self.n
        self.one = [Q(1)] + [Q(0)] * (self.n-1)
        self.x = [Q(0), Q(1)] + [Q(0)] * (self.n-2)

    def add(self, a, b):
        return [x+y for x, y in zip(a, b)]

    def scale(self, a, c):
        return [Q(c)*x for x in a]

    def mul(self, a, b):
        c = [Q(0)] * (2*self.n-1)
        for j, x in enumerate(a):
            for k, y in enumerate(b):
                c[j+k] += x*y
        for j in range(2*self.n-2, self.n-1, -1):
            for k in range(self.n):
                c[j-self.n+k] -= c[j]*self.f[k]
        return c[:self.n]

    def evaluate(self, coefficients, a):
        out = list(self.zero)
        for x in reversed(coefficients):
            out = self.mul(out, a)
            out[0] += Q(x)
        return out

    def trace(self, a):
        traces = [Q(self.n)]
        for r in range(1, self.n):
            traces.append(-sum(self.f[self.n-j]*traces[r-j]
                              for j in range(1, r))
                          -r*self.f[self.n-r])
        return sum(x*t for x, t in zip(a, traces))


def rational_element(data):
    return [Q(int(a), int(data['denominator']))
            for a in data['coefficients_ascending']]


def finite_element(F, data, a):
    den = int(data['denominator'])
    assert den % F.q != 0
    result = F.zero
    for c in reversed(data['coefficients_ascending']):
        result = F.add(F.mul(result, a), (int(c) % F.q, 0))
    return F.scale(result, pow(den, -1, F.q))


def finite_polynomial(F, coefficients, a):
    out = F.zero
    for c in reversed(coefficients):
        out = F.add(F.mul(out, a), (int(c) % F.q, 0))
    return out


def weighted(logs, n, denominator=1):
    k = Fp2(43)
    out = k.zero
    for j, a in enumerate(logs):
        if a is not None:
            out = k.add(out, k.scale(k.power((8, 25), n*j % 44), a))
    return list(k.scale(out, pow(denominator, -1, 43)))


def rank(matrix):
    a = [[x % 43 for x in row] for row in matrix]
    r = 0
    for c in range(len(a[0])):
        pivot = next((j for j in range(r, len(a)) if a[j][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inverse = pow(a[r][c], -1, 43)
        a[r] = [inverse*x % 43 for x in a[r]]
        for j in range(len(a)):
            if j != r:
                scale = a[j][c]
                a[j] = [(x-scale*y) % 43 for x, y in zip(a[j], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def determinant(matrix):
    a = [[x % 43 for x in row] for row in matrix]
    result = 1
    for c in range(len(a)):
        pivot = next((j for j in range(c, len(a)) if a[j][c]), None)
        if pivot is None:
            return 0
        if pivot != c:
            a[c], a[pivot] = a[pivot], a[c]
            result = -result
        result = result*a[c][c] % 43
        inverse = pow(a[c][c], -1, 43)
        for j in range(c+1, len(a)):
            scale = a[j][c]*inverse % 43
            a[j] = [(x-scale*y) % 43 for x, y in zip(a[j], a[c])]
    return result % 43


def psi11(F, x):
    # Division-polynomial recursions for y^2=x^3-x, retaining all signs.
    x2 = F.mul(x, x); x3 = F.mul(x2, x)
    x4 = F.mul(x2, x2); x6 = F.mul(x3, x3)
    v = F.scale(F.sub(x3, x), 4); v2 = F.mul(v, v)
    o3 = F.sub(F.sub(F.scale(x4, 3), F.scale(x2, 6)), F.one)
    e4 = F.scale(F.add(F.sub(F.sub(x6, F.scale(x4, 5)),
                            F.scale(x2, 5)), F.one), 2)
    o33 = F.power(o3, 3)
    o5 = F.sub(F.mul(v2, e4), o33)
    e6 = F.mul(o3, F.sub(o5, F.mul(e4, e4)))
    o7 = F.sub(F.mul(o5, o33), F.mul(v2, F.power(e4, 3)))
    return F.sub(F.mul(o7, F.power(o5, 3)),
                 F.mul(F.mul(v2, e4), F.power(e6, 3)))


def unshifted_robert(q, point):
    F = Fp2(q); E = EC(F, (q-1, 0), F.zero)
    point = tuple(tuple(map(int, row)) for row in point)
    first = point
    assert E.on(point) and E.mult(point, 43) is None
    def iP(P):
        return F.neg(P[0]), F.mul(F.i, P[1])
    zeta = F.neg(F.div(E.miller(point, iP(point), 43),
                      E.miller(iP(point), point, 43)))
    powers = {F.power(zeta, j): j for j in range(43)}
    assert len(powers) == 43 and F.power(zeta, 43) == F.one
    m = (q*q-1)//43
    U = []; zvalues = []; logs44 = []
    for j in range(44):
        T, phi = E.velu43(point)
        delta = F.scale(F.add(F.scale(F.power(T.a, 3), 4),
                             F.scale(F.power(T.b, 2), 27)), -16)
        value = F.power(F.scale(delta, pow(64, -1, q)), 10)
        product = F.one; R = point
        for _ in range(42):
            product = F.mul(product, psi11(F, R[0]))
            R = E.add(R, point)
        assert R is None and product != F.zero
        assert F.div((pow(64, 420, q), 0), product) == value
        U.append(value); logs44.append(powers[F.power(value, m)])
        t0 = phi((F.zero, F.zero)); tm = phi(((q-1, 0), F.zero))
        p4 = phi((F.i, (1, q-1)))
        zvalues.append(F.div(F.neg(F.mul(F.i, F.sub(p4[0], t0[0]))),
                             F.sub(tm[0], t0[0])))
        point = E.add(E.neg(point), E.mult(iP(point), 2))
    assert point == E.mult(first, 5)
    assert all(U[j] == U[(j+22) % 44] for j in range(44))
    T = [F.mul(U[j], U[j+11]) for j in range(11)]
    assert all(F.mul(U[j], U[(j+11) % 44]) == T[j % 11]
               for j in range(44))
    V = [F.div(T[j], T[(j+1) % 11]) for j in range(11)]
    logs = [powers[F.power(v, m)] for v in V]
    matrix = [[logs[(j+a) % 11] for j in range(11)] for a in range(11)]
    weights = [-42, 11, -17, 2, 18, 7, 7, 18, 2, -17, 11]
    assert sum(weights) == 0
    eta = Fp2(43).power((8, 25), 8)
    assert all(weights[j] % 43 == Fp2(43).power(eta, j)[0]
               for j in range(11))
    Tlogs = [powers[F.power(t, m)] for t in T]
    target_logs = [sum(weights[j]*Tlogs[(j+a) % 11] for j in range(11)) % 43
                   for a in range(11)]
    result = {
        'q': str(q), 'P': [[str(a) for a in row] for row in first],
        'z0': [str(a) for a in zvalues[0]],
        'zeta_Weil': [str(a) for a in zeta],
        'delta_norm_identity_branches_checked': 44,
        'unshifted_logs_44': logs44, 'ordinary_unit_logs_11': logs,
        'weighted_spectra_11': {str(n): weighted(logs, n)
                                for n in [4, 8, 12, 16, 20]},
        'circulant_symbol_matrix_11': matrix,
        'circulant_rank': rank(matrix),
        'first_10_by_10_determinant': determinant([r[:10] for r in matrix[:10]]),
        'T_logs_11': Tlogs, 'real_chi8_target_logs_11': target_logs,
    }
    return result, zvalues


def verify(certificate, small, r171, r219):
    raw = [Path(p).read_bytes() for p in [small, r171, r219]]
    C, A, D = [json.loads(x) for x in raw]
    assert [hashlib.sha256(x).hexdigest() for x in raw] == certificate['source_sha256']
    q = int(C['q']); assert q == int(A['q'])
    assert [[int(a) for a in row] for row in C['P']] == [
        [int(a) for a in row] for row in A['expected']['P']]
    assert list(map(int, C['zeta_Weil'])) == list(map(int, A['expected']['zeta_Weil']))
    G = certificate['small_field_arithmetic']
    f = list(map(int, G['reduced_polynomial_coefficients_ascending']))
    assert f == [6704, -4652, -1696, 2812, 100, -1159, 532, -13, -52, 19, -4, 1]
    old = RationalField(list(map(int, D['degree11_polynomial_coefficients_ascending'])))
    new = RationalField(f)
    s_new = rational_element(G['s_from_new'])
    y_old = rational_element(G['new_from_s'])
    assert new.evaluate(old.f, s_new) == new.zero
    assert old.evaluate(f, y_old) == old.zero
    assert old.evaluate(s_new, y_old) == old.x
    assert new.evaluate(y_old, s_new) == new.x
    g = rational_element(G['prime2_generator_new'])
    gs = rational_element(G['prime2_generator_s'])
    assert old.evaluate(g, y_old) == gs
    pg = list(map(int, G['prime2_generator_monic_polynomial_ascending']))
    assert len(pg) == 12 and pg[-1] == 1 and pg[0] == -2
    assert new.evaluate(pg, g) == new.zero and g != [g[0]]+[Q(0)]*10
    inverse = new.scale(new.evaluate(pg[1:], g), Q(1, 2))
    assert new.mul(g, inverse) == new.one
    trace = new.trace(new.scale(new.mul(inverse, inverse), 2))
    assert trace == Q(152857, 2) == Q(G['trace_two_over_generator_squared'])
    assert trace.denominator == 2

    aux, _ = unshifted_robert(859, [[209, 0], [591, 0]])
    main, zvalues = unshifted_robert(q, C['P'])
    assert aux == certificate['unshifted_robert']['aux_859']
    assert main == certificate['unshifted_robert']['q']
    assert aux['circulant_rank'] == 10 and aux['first_10_by_10_determinant'] != 0
    assert main['circulant_rank'] == 8
    assert main['weighted_spectra_11']['8'] == [0, 0]
    assert all(aux['weighted_spectra_11'][str(n)] != [0, 0]
               for n in [4, 8, 12, 16, 20])
    assert main['real_chi8_target_logs_11'] == [0]*11
    assert aux['real_chi8_target_logs_11'] != [0]*11
    assert main['zeta_Weil'] == C['zeta_Weil']
    F = Fp2(q)
    zeta = tuple(map(int, C['zeta_Weil']))
    powers = {F.power(zeta, j): j for j in range(43)}; m = (q*q-1)//43
    prime2logs = []; ss = []
    for z in zvalues:
        s = F.power(F.div(F.sub(z, F.one), F.add(z, F.one)), 4)
        ss.append(s)
        y = finite_element(F, G['new_from_s'], s)
        assert finite_polynomial(F, f, y) == F.zero
        a = finite_element(F, G['prime2_generator_s'], s)
        assert a == finite_element(F, G['prime2_generator_new'], y)
        assert finite_polynomial(F, pg, a) == F.zero
        prime2logs.append(powers[F.power(a, m)])
    assert len(set(ss)) == 11
    assert all(ss[j] == ss[j % 11] and prime2logs[j] == prime2logs[j % 11]
               for j in range(44))
    alpha_logs = []
    roots = [tuple(map(int, row)) for row in A['roots_y']]
    labels = A['expected']['root_labels']
    for j in range(44):
        y = roots[labels[j]]
        assert finite_polynomial(F, A['P'][::-1], y) == F.zero
        a = F.add(F.scale(y, int(A['b'])), F.one)
        if j == 0:
            assert a == F.zero
            alpha_logs.append(None)
        else:
            alpha_logs.append(powers[F.power(a, m)])
    assert alpha_logs == A['expected']['unit_logs']
    assert sum(alpha_logs[j] for j in [11, 22, 33]) % 43 == 0
    alpha11_logs = [0]+[sum(alpha_logs[j+11*r] for r in range(4)) % 43
                          for j in range(1, 11)]
    data = {
        'prime2_generator_logs_11': prime2logs[:11],
        'prime2_weighted_sums_11': {str(n): weighted(prime2logs[:11], n)
                                    for n in [4, 8, 12, 16, 20]},
        'alpha_weighted_sums_44': {str(n): weighted(alpha_logs, n)
                                   for n in [1, 4, 8, 12, 16, 20, 22]},
        'alpha11_uniformizer_unit_logs_11': alpha11_logs,
        'alpha11_chi8_projection': weighted(alpha11_logs, -8, 11),
        'prime2_generator_chi8_projection': weighted(prime2logs[:11], -8, 11),
        'prime2_ideal_chi8_ray_coordinate':
            list(Fp2(43).scale(tuple(weighted(prime2logs[:11], -8, 11)), 22)),
    }
    assert data == certificate['labeled_ray_symbols']
    assert data['alpha11_chi8_projection'] == [0, 0]
    assert data['prime2_generator_chi8_projection'] == [0, 41]
    assert data['prime2_ideal_chi8_ray_coordinate'] == [0, 42]
    return {
        'status': 'PASS', 'rational_maps_verified': True,
        'prime2_generator_norm': 2, 'trace_two_over_g_squared': str(trace),
        'elliptic_discriminant_norm_identities': 88,
        'auxiliary_unit_rank': 10, 'q_unit_rank': 8,
        'chi8_selflocal_projection': [0, 0],
        'prime2_chi8_ray_coordinate': [0, 42],
        'class_number_certification_repeated_by_this_script': False,
        'actual_norm_preimage_computed': False, 'actual_L_computed': False,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('certificate')
    parser.add_argument('small_target')
    parser.add_argument('r171')
    parser.add_argument('r219')
    args = parser.parse_args()
    certificate = json.loads(Path(args.certificate).read_text())
    print(json.dumps(verify(certificate, args.small_target, args.r171, args.r219),
                     ensure_ascii=False), flush=True)


if __name__ == '__main__':
    main()
