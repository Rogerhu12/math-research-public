#!/usr/bin/env python3
"""Unconditional exact verification of R243; Python standard library only.

The PARI discovery computation and its conditional class number are not used.
Ordinary units are certified by monic integral annihilators with constant +/-1.
Their 43-saturation follows from a recomputed nonzero finite-symbol determinant.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
from verify_o6_single_real_norm_target import Field44, Fp2, EC


def load_element(d):
    assert len(d['numerators_ascending']) == 44
    return tuple((int(a), 0) for a in d['numerators_ascending']) + (int(d['common_denominator']),)


def rref(A):
    A = [[v % 43 for v in row] for row in A]
    n = len(A[0]); r = 0; pivots = []
    for c in range(n):
        index = next((j for j in range(r, len(A)) if A[j][c]), None)
        if index is None:
            continue
        A[r], A[index] = A[index], A[r]
        inverse = pow(A[r][c], -1, 43)
        A[r] = [v * inverse % 43 for v in A[r]]
        for j in range(len(A)):
            if j != r:
                scale = A[j][c]
                A[j] = [(x-scale*y) % 43 for x, y in zip(A[j], A[r])]
        pivots.append(c); r += 1
        if r == len(A):
            break
    return A, pivots


def kernel(A):
    R, pivots = rref(A); result = []
    for free in range(len(A[0])):
        if free in pivots:
            continue
        v = [0] * len(A[0]); v[free] = 1
        for j, pivot in enumerate(pivots):
            v[pivot] = -R[j][free] % 43
        result.append(v)
    return result


def determinant(A):
    A = [[v % 43 for v in row] for row in A]; result = 1
    for c in range(len(A)):
        index = next((j for j in range(c, len(A)) if A[j][c]), None)
        if index is None:
            return 0
        if index != c:
            A[c], A[index] = A[index], A[c]; result = -result
        result = result * A[c][c] % 43
        inverse = pow(A[c][c], -1, 43)
        for j in range(c+1, len(A)):
            scale = A[j][c] * inverse % 43
            for k in range(c, len(A)):
                A[j][k] = (A[j][k]-scale*A[c][k]) % 43
    return result % 43


def solve(A, b):
    R, pivots = rref([row + [value] for row, value in zip(A, b)])
    assert pivots == list(range(len(A)))
    return [row[-1] for row in R]


def prime(n):
    return n >= 2 and all(n % a for a in range(2, math.isqrt(n)+1))


def trim(a):
    while a and a[-1] == 0:
        a.pop()
    return a


def poly_remainder(a, b, p):
    a = trim([v % p for v in a]); b = trim([v % p for v in b])
    assert b
    inverse = pow(b[-1], -1, p)
    while len(a) >= len(b):
        scale = a[-1] * inverse % p; offset = len(a)-len(b)
        for k, v in enumerate(b):
            a[offset+k] = (a[offset+k]-scale*v) % p
        trim(a)
    return a


def poly_gcd(a, b, p):
    a = trim([v % p for v in a]); b = trim([v % p for v in b])
    while b:
        a, b = b, poly_remainder(a, b, p)
    if not a:
        return []
    inverse = pow(a[-1], -1, p)
    return [v * inverse % p for v in a]


class FiniteQuotient:
    def __init__(self, p, f):
        assert f[-1] == 1
        self.p = p; self.f = f; self.d = len(f)-1
        self.zero = (0,) * self.d
        self.one = (1,) + (0,) * (self.d-1)
        self.x = (0, 1) + (0,) * (self.d-2)

    def mul(self, a, b):
        out = [0] * (2*self.d-1)
        for j, x in enumerate(a):
            for k, y in enumerate(b):
                out[j+k] += x*y
        for j in range(2*self.d-2, self.d-1, -1):
            value = out[j] % self.p
            for k, c in enumerate(self.f[:-1]):
                out[j-self.d+k] -= value*c
        return tuple(c % self.p for c in out[:self.d])

    def power(self, a, n):
        result = self.one
        while n:
            if n & 1:
                result = self.mul(result, a)
            n //= 2
            if n:
                a = self.mul(a, a)
        return result

    def evaluate(self, coefficients, x=None):
        if x is None:
            x = self.x
        result = self.zero
        for c in reversed(coefficients):
            result = list(self.mul(result, x))
            result[0] = (result[0]+c) % self.p
            result = tuple(result)
        return result

    def certify_field(self):
        assert prime(self.p)
        assert self.power(self.x, self.p**self.d) == self.x
        for divisor in range(2, self.d+1):
            if self.d % divisor == 0 and prime(divisor):
                v = list(self.power(self.x, self.p**(self.d//divisor)))
                v[1] = (v[1]-1) % self.p
                assert poly_gcd(v, self.f, self.p) == [1]


def verify(source, r219_source, r239_source, certificate, progress=False):
    def report(text):
        if progress:
            print(text, flush=True)

    raw = Path(source).read_bytes(); C = json.loads(raw)
    raw219 = Path(r219_source).read_bytes(); old = json.loads(raw219)
    raw239 = Path(r239_source).read_bytes(); short = json.loads(raw239)
    data = json.loads(Path(certificate).read_text())
    assert data['schema'] == 'r243_h_units_43_saturation_and_full_field_norm_kernel_v1'
    assert data['source_sha256'] == hashlib.sha256(raw).hexdigest()
    assert data['r219_sha256'] == hashlib.sha256(raw219).hexdigest()
    assert data['r239_sha256'] == hashlib.sha256(raw239).hexdigest()
    assert old['source_sha256'] == short['source_sha256'] == data['source_sha256']
    fz = list(map(int, C['factors'][0]['coefficients'])); K = Field44(fz)
    rows = data['ordinary_units']; assert len(rows) == 22
    units, inverses = [], []
    for index, row in enumerate(rows):
        assert row['index'] == index
        u = load_element(row['element'])
        assert K.normalize(u[:-1], u[-1]) == u
        ann = list(map(int, row['integral_annihilator_ascending']))
        assert len(ann) == 45 and ann[-1] == 1 and abs(ann[0]) == 1
        tail = K.evaluate(ann[1:], u)
        inverse = K.mul(K.scalar(-ann[0]), tail)
        assert K.mul(u, inverse) == K.one
        units.append(u); inverses.append(inverse)
    report('22 exact monic integral unit certificates verified')

    def product(exponents):
        assert len(exponents) in (22, 23)
        value = K.one
        for u, inverse, exponent in zip(units, inverses, exponents[:22]):
            if exponent:
                value = K.mul(value, K.power(u if exponent > 0 else inverse, abs(exponent)))
        if len(exponents) == 23 and exponents[22] % 2:
            value = K.mul(value, K.scalar(-1))
        return value

    epsilon = data['quadratic_pell_unit']
    square_root = load_element(epsilon['sqrt43_element_in_z'])
    assert K.power(square_root, 2) == K.scalar(43)
    assert 3482**2 - 43*531**2 == 1
    eps_value = K.add(K.scalar(3482), K.mul(K.scalar(531), square_root))
    assert eps_value == load_element(epsilon['element'])
    eps_exponents = list(map(int, epsilon['unit_exponents']))
    assert product(eps_exponents) == eps_value
    V = data['short_target_V42']; V_exponents = list(map(int, V['unit_exponents']))
    assert product(V_exponents) == load_element(V['element'])
    source_V = next(row for row in short['chosen_targets'] if row['c'] == 42)['target_V_in_t']
    xi = load_element(short['fourth_root_t_in_old_z'])
    assert K.power(xi, 4) == K.z
    assert K.compose(load_element(source_V), xi) == load_element(V['element'])
    third = data['third_kernel_unit']; W_exponents = list(map(int, third['unit_exponents']))
    assert len(W_exponents) == 22
    assert product(W_exponents) == load_element(third['element'])
    assert third['character_j'] == 8 and third['T_eigenvalue'] == 22
    report('Pell, V42, and third ordinary unit identities verified')

    sigma = old['labeled_sigma_exact']
    sigma_coefficients = [tuple(map(int, row)) for row in sigma['Gaussian_numerators_ascending']]
    sigma_denominator = int(sigma['common_denominator'])

    def finite_value(F, z, element):
        value = F.zero
        for c in reversed(element['numerators_ascending']):
            value = F.add(F.mul(value, z), (int(c) % F.q, 0))
        denominator = int(element['common_denominator'])
        assert denominator % F.q
        value = F.scale(value, pow(denominator, -1, F.q))
        assert value != F.zero
        return value

    def sigma_value(F, z):
        value = F.zero
        for a, b in reversed(sigma_coefficients):
            value = F.add(F.mul(value, z), (a % F.q, b % F.q))
        assert sigma_denominator % F.q
        return F.scale(value, pow(sigma_denominator, -1, F.q))

    def symbol_rows(F, z0, zeta):
        assert F.power(zeta, 43) == F.one and zeta != F.one
        logarithms = {F.power(zeta, j): j for j in range(43)}
        assert len(logarithms) == 43
        z = z0; roots = []; matrix = []
        for j in range(44):
            roots.append(z)
            val = F.zero
            for c in reversed(fz):
                val = F.add(F.mul(val, z), (c % F.q, 0))
            assert val == F.zero
            matrix.append([logarithms[F.power(finite_value(F, z, row['element']),
                                             (F.q*F.q-1)//43)] for row in rows])
            z = sigma_value(F, z)
            if F.q > 10**10 and j % 11 == 10:
                report('q symbol rows recomputed: '+str(j+1))
        assert len(set(roots)) == 44 and z == z0
        return roots, matrix, logarithms

    q = int(C['q']); assert q % 172 == 171 and (q+1) % (43*43) != 0
    F = Fp2(q); curve = EC(F, (q-1, 0), F.zero)
    P = tuple(tuple(map(int, v)) for v in C['P'])
    assert curve.on(P) and curve.mult(P, 43) is None
    P4 = (F.i, (1, q-1)); target, phi = curve.velu43(P)
    zero = phi((F.zero, F.zero)); minus = phi(((q-1, 0), F.zero)); p4 = phi(P4)
    z0 = F.div(F.neg(F.mul(F.i, F.sub(p4[0], zero[0]))), F.sub(minus[0], zero[0]))
    zeta = tuple(map(int, C['zeta_Weil']))
    q_roots, q_matrix, q_logs = symbol_rows(F, z0, zeta)
    assert [q_logs[F.power(z, (q*q-1)//43)] for z in q_roots] == old['z_power_residue_logs']
    assert q_matrix == data['q_log_matrix_44_by_22']
    assert q_matrix[0] == q_matrix[22] == [0]*22
    assert all(q_matrix[-j % 44] == [-a % 43 for a in q_matrix[j]] for j in range(44))
    assert len(rref(q_matrix)[1]) == data['q_log_matrix_rank'] == 19
    basis = kernel(q_matrix)
    assert basis == data['q_kernel_rref_basis'] and len(basis) == 3

    aux = data['aux859']; assert aux['prime'] == 859 and prime(859) and 859 % 4 == 3
    aux_roots, r859, _ = symbol_rows(Fp2(859), tuple(aux['z0']), tuple(aux['zeta']))
    assert r859 == aux['unit_log_rows_44_by_22']
    d = data['aux173']; assert d['prime'] == 173 and prime(173)
    Q = FiniteQuotient(173, d['factor_ascending']); Q.certify_field()
    assert Q.d == d['factor_degree'] == 22 and Q.evaluate(fz) == Q.zero
    mu = d['zeta']; assert mu != 1 and pow(mu, 43, 173) == 1
    logs173 = {pow(mu, j, 173): j for j in range(43)}
    i = d['i']; assert i*i % 173 == 172
    inverse = pow(sigma_denominator, -1, 173)
    plus = Q.evaluate([(a+i*b)*inverse % 173 for a,b in sigma_coefficients])
    minus = Q.evaluate([(a-i*b)*inverse % 173 for a,b in sigma_coefficients])
    assert Q.evaluate(fz, plus) == Q.evaluate(fz, minus) == Q.zero

    def row173(x):
        result = []
        for row in rows:
            element = row['element']; den = int(element['common_denominator'])
            assert den % 173
            den = pow(den, -1, 173)
            value = Q.evaluate([int(c)*den % 173 for c in element['numerators_ascending']], x)
            value = Q.power(value, (173**Q.d-1)//43)
            assert all(c == 0 for c in value[1:])
            result.append(logs173[value[0]])
        return result

    r173, rplus, rminus = row173(Q.x), row173(plus), row173(minus)
    assert r173 == d['unit_log_row']
    assert rplus == d['sigma_plus_unit_log_row']
    assert rminus == d['sigma_minus_unit_log_row']
    T173 = [(a+b) % 43 for a,b in zip(rplus, rminus)]
    assert T173 == [-2*a % 43 for a in r173]
    report('all auxiliary finite fields and power symbols verified')

    labels = ([{'prime':'q','index':j} for j in range(1,20)] +
              [{'prime':859,'index':0},{'prime':859,'index':1},{'prime':173,'index':0}])
    minor = q_matrix[1:20] + [r859[0], r859[1], r173]
    assert labels == data['saturation_minor_row_labels']
    assert determinant(minor) == data['saturation_minor_determinant_mod43'] == 12
    assert len(rref(q_matrix+[r859[0], r859[1], r173])[1]) == 22
    auxiliary = [r859[0], r859[1], r173]
    Tauxiliary = [[(a+b)%43 for a,b in zip(r859[1],r859[43])],
                  [(a+b)%43 for a,b in zip(r859[2],r859[0])], T173]
    dot = lambda a,b: sum(x*y for x,y in zip(a,b)) % 43
    A = [[dot(row, v) for v in basis] for row in auxiliary]
    B = [[dot(row, v) for v in basis] for row in Tauxiliary]
    columns = [solve(A, [row[j] for row in B]) for j in range(3)]
    T = [[columns[j][i] for j in range(3)] for i in range(3)]
    assert T == data['T_on_q_kernel_rref_basis'] == [[41,10,12],[0,16,0],[0,0,22]]
    finite = Fp2(43); omega = (8,25); characters = []
    for j in range(1,23):
        eigenvalue = 2*finite.power(omega,j)[0] % 43
        matrix = [[(T[r][c]-(eigenvalue if r==c else 0)) % 43 for c in range(3)] for r in range(3)]
        if kernel(matrix):
            assert len(kernel(matrix)) == 1
            characters.append(j)
    assert characters == data['kernel_character_indices'] == [1,8,22]
    generators = [eps_exponents[:22], V_exponents[:22], W_exponents]
    values = [[dot(row, exponents) for exponents in generators] for row in auxiliary]
    assert values == data['explicit_kernel_generators_aux_value_matrix'] == [[0,20,16],[0,19,8],[15,0,0]]
    assert determinant(values) == 33
    for exponents, eigenvalue in zip(generators, [41,16,22]):
        assert all(dot(row, exponents) == 0 for row in q_matrix)
        assert all(dot(trow, exponents) == eigenvalue*dot(row, exponents) % 43
                   for row,trow in zip(auxiliary,Tauxiliary))
    assert data['full_field_norm_subgroup_index_power_of_43'] == 19
    for flag in ['unit_generation_43_saturation_used_GRH','class_number_used',
                 'actual_norm_preimage_computed','actual_L_computed']:
        assert data[flag] is False
    return {'status':'PASS','ordinary_units_verified':22,
            'saturation_minor_determinant_mod43':12,'q_symbol_rank':19,
            'global_field_norm_kernel_dimension_mod43':3,
            'kernel_character_indices':[1,8,22],
            'explicit_kernel_generator_aux_determinant':33,
            'conditional_class_number_used':False,
            'actual_norm_preimage_computed':False,'actual_L_computed':False}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('source'); parser.add_argument('r219_source')
    parser.add_argument('r239_source'); parser.add_argument('certificate')
    parser.add_argument('--progress', action='store_true')
    args = parser.parse_args()
    print(json.dumps(verify(args.source,args.r219_source,args.r239_source,
                            args.certificate,args.progress),
                     ensure_ascii=False,separators=(',',':')))


if __name__ == '__main__':
    main()
