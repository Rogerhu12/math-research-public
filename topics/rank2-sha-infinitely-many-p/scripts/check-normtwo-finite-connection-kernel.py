#!/usr/bin/env python3
"""Exact finite-source operator, kernel, cokernel and saturation certificate (R264)."""
import json
from pathlib import Path

import sympy as s

U = s.symbols('U')
D = U**8*(U-1)**8
checks = {}


def check(name, value):
    checks[name] = bool(value)
    if not checks[name]:
        raise AssertionError(name)


def Q(P):
    return s.expand(16*U**2*(U-1)*s.diff(P, U, 2)
                    + 4*U*(61-55*U)*s.diff(P, U)
                    - (320*U+1056)*P)


def original(P):
    h = P/D
    return s.cancel(4*U*D*(4*U*(U-1)*s.diff(h, U, 2)
                           + (73*U-3)*s.diff(h, U)
                           + 272*h/(U-1)))


M = s.zeros(17)
for n in range(17):
    M[n, n] = -(n-8)*(4*n-33)
    if n < 16:
        M[n+1, n] = (n-16)*(4*n+5)
    expected = 4*((n-16)*(4*n+5)*U**(n+1)-(n-8)*(4*n-33)*U**n)
    check(f'actual_operator_column_{n}', original(U**n) == Q(U**n))
    check(f'bidiagonal_column_{n}', s.expand(Q(U**n)-expected) == 0)

v = s.Matrix([0]*8 + [1341153, -132327096, 2712705468,
    -22194862920, 90629023590, -202245821064, 250608952188,
    -161768741624, 42399065345])
ell = s.Matrix([14221350, -46930455, 70569499, -58161675,
    27633375, -7456625, 1057485, -65637, 1105] + [0]*8)
check('right_kernel', M*v == s.zeros(17, 1))
check('left_kernel', ell.T*M == s.zeros(1, 17))
check('primitive_right_kernel', s.igcd(*v) == 1)
check('primitive_left_kernel', s.igcd(*ell) == 1)

P8 = sum(v[j+8]*U**j for j in range(9))/1341153
hyper = sum(s.rf(-8,j)*s.rf(s.Rational(37,4),j)
            /s.rf(s.Rational(3,4),j)/s.factorial(j)*U**j for j in range(9))
check('hypergeometric_polynomial', s.expand(P8-hyper) == 0)
check('polynomial_kernel_ODE', s.expand(4*U*(U-1)*s.diff(P8,U,2)
      +(9*U-3)*s.diff(P8,U)-296*P8) == 0)

minor = M.minor_submatrix(8, 8).det()
c = s.cancel(minor/(v[8]*ell[8]))
check('nonzero_integral_adjugate_scalar', c.is_Integer and c != 0)
check('complete_adjugate', M.adjugate() == c*v*ell.T)


def bezout(vec):
    coeff = [s.Integer(0)]*len(vec)
    current = s.Integer(0)
    for j, value in enumerate(vec):
        if not value:
            continue
        a, b, g = s.gcdex(current, value)
        coeff = [a*q for q in coeff]
        coeff[j] += b
        current = g
        if current == 1:
            break
    assert current == 1
    return s.Matrix(coeff)


a, b = bezout(v), bezout(ell)
check('right_Bezout', (a.T*v)[0] == 1)
check('left_Bezout', (ell.T*b)[0] == 1)
border = M.row_join(b).col_join(a.T.row_join(s.zeros(1, 1)))
check('bordered_determinant', border.det() == -c)
factors = {str(int(p)): int(e) for p,e in s.factorint(abs(c)).items()}
check('only_bad_prime_above_19_is_29',
      {int(p) for p in factors if int(p) > 19} == {29})

# A zero-mass preimage has p_16=0. Backward substitution divides only by
# (n-16)(4n+5), n=0,...,15. All prime divisors above 19 split in Q(i).
inverse_denominator = s.prod((n-16)*(4*n+5) for n in range(16))
inverse_factors = s.factorint(abs(inverse_denominator))
check('backward_inverse_has_no_inert_denominator_above_19',
      all(p % 4 == 1 for p in inverse_factors if p > 19))
check('cokernel_initial_coordinate_is_inert_unit_above_19',
      all(p % 4 == 1 for p in s.factorint(ell[0]) if p > 19))
check('kernel_top_coordinate_is_inert_unit_above_19',
      all(p % 4 == 1 for p in s.factorint(v[16]) if p > 19))

prior = json.loads(Path(__file__).with_name(
    'check-normtwo-compensation-and-conductor17-trace.json').read_text())
Gamma = s.Matrix([s.sympify(t) for t in
    prior['conductor17_sparse_rankone_operators']['adjacent']['image_polynomial']])
gamma = s.expand((ell.T*Gamma)[0])
check('actual_CM_compensator_pairing',
      gamma == 5479905460224-3786459611136*s.I)
gamma_gcd = s.igcd(s.re(gamma), s.im(gamma))
check('actual_CM_compensator_unit_at_all_inert_primes_above_19',
      gamma_gcd == 98304)

period_a = -s.Rational(583401555, 4294967296)
A8 = sum(s.Rational(c)*U**j for j,c in enumerate([
    '-3711565741/4294967296', '493313525001/10737418240',
    '-1453654847931/2147483648', '122613573291325/27917287424',
    '-443895314554125/29662117888', '61762229127375/2147483648',
    '-67351754727173/2147483648', '38873419988235/2147483648',
    '-18443593425075/4294967296']))
de_rham_identity = s.expand(period_a*(U-1)*P8**2-(U+1)*A8*P8
    +4*U*(U-1)*(s.diff(A8,U)*P8-A8*s.diff(P8,U))-1)
check('complete_de_Rham_reduction', de_rham_identity == 0)
check('de_Rham_period_nonzero', period_a != 0)
check('kernel_P8_simple_roots', s.degree(s.gcd(P8,s.diff(P8,U)),U)==0)
check('kernel_P8_nonzero_at_zero_and_one', P8.subs(U,0)*P8.subs(U,1)!=0)
period_num_factors = s.factorint(abs(s.numer(period_a)))
check('inert_period_numerator_exceptions_above_19',
      {int(p) for p in period_num_factors if p>19 and p%4==3} == {23,31})

result = {
    'status': 'PASS', 'checks': checks,
    'normalization': 'M=one quarter of the actual source differential operator',
    'matrix': [[int(x) for x in row] for row in M.tolist()],
    'right_kernel': list(map(int, v)), 'left_kernel': list(map(int, ell)),
    'right_Bezout': list(map(int, a)), 'left_Bezout': list(map(int, b)),
    'adjugate_scalar': str(c), 'adjugate_scalar_factorization': factors,
    'bordered_determinant': str(-c),
    'kernel_P8_coefficients': [str(P8.coeff(U,j)) for j in range(9)],
    'backward_inverse_denominator_factorization':
        {str(int(p)):int(e) for p,e in inverse_factors.items()},
    'actual_CM_compensator_polynomial': list(map(str,Gamma)),
    'actual_CM_compensator_pairing': str(gamma),
    'actual_CM_pairing_real_imag_gcd': str(gamma_gcd),
    'de_Rham_reduction': {
        'period_coefficient':str(period_a),
        'period_numerator_factorization':
            {str(int(p)):int(e) for p,e in period_num_factors.items()},
        'primitive_A8_coefficients':[str(A8.coeff(U,j)) for j in range(9)],
        'identity':'1=a*(U-1)*P8^2-(U+1)*A8*P8+4*U*(U-1)*(A8_prime*P8-A8*P8_prime)',
        'inert_numerator_exceptions_above_19':[23,31]
    },
    'scope': 'Exact fixed source sequence; no assertion of Mellin equivariance or central nonvanishing.'
}
output=Path(__file__).with_suffix('.json')
output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('PASS:',len(checks),'checks; c=',c,'; factors=',factors)
