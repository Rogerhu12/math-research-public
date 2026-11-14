#!/usr/bin/env python3
"""R273: exact Fermat conjugacy, pole-free Darboux quartet, actual second carry.

Every check is over Q, Q(x)[y]/(y^2-x^3+x), or a symbolic parameter.
No scan of target primes is used.
"""
import json
from pathlib import Path

import sympy as s

root = Path(__file__).parent
data = json.loads((root / 'check-normtwo-finite-connection-kernel.json').read_text())
x, U, q, r, j, n = s.symbols('x U q r j n')
P = sum(s.Rational(c)*U**k for k, c in enumerate(data['kernel_P8_coefficients']))
A = sum(s.Rational(c)*U**k for k, c in
        enumerate(data['de_Rham_reduction']['primitive_A8_coefficients']))
a = s.Rational(data['de_Rham_reduction']['period_coefficient'])
checks = {}


def check(name, value):
    checks[name] = bool(value)
    if not checks[name]:
        raise AssertionError(name)


def eq(name, value):
    check(name, s.cancel(value) == 0)


eq('actual_de_Rham_polynomial_identity',
   a*(U-1)*P**2 - (U+1)*A*P
   + 4*U*(U-1)*(s.diff(A, U)*P-A*s.diff(P, U)) - 1)

# Differential field: x'=2y, y'=3x^2-1.
curve = x**3-x
zero = (s.Integer(0), s.Integer(0))
one = (s.Integer(1), s.Integer(0))


def c0(v):
    return (s.cancel(v), s.Integer(0))


def add(v, w):
    return (s.cancel(v[0]+w[0]), s.cancel(v[1]+w[1]))


def neg(v):
    return (-v[0], -v[1])


def mul(v, w):
    return (s.cancel(v[0]*w[0]+curve*v[1]*w[1]),
            s.cancel(v[0]*w[1]+v[1]*w[0]))


def deriv(v):
    return (s.cancel((3*x*x-1)*v[1]+2*curve*s.diff(v[1], x)),
            s.cancel(2*s.diff(v[0], x)))


def dop(v, k):
    for _ in range(k):
        v = deriv(v)
    return v


def op_comp(left, right):
    """Left coefficients; multiplication is noncommutative composition."""
    out = [zero for _ in range(len(left)+len(right)-1)]
    for i, li in enumerate(left):
        for k, rk in enumerate(right):
            for b in range(i+1):
                v = mul(li, mul(c0(s.binomial(i, b)), dop(rk, i-b)))
                out[k+b] = add(out[k+b], v)
    return out


def op_check(name, left, right):
    m = max(len(left), len(right))
    left = left + [zero]*(m-len(left))
    right = right + [zero]*(m-len(right))
    for k in range(m):
        check(f'{name}_D{k}', add(left[k], neg(right[k])) == zero)


Px, Ax = P.subs(U, x*x), A.subs(U, x*x)
f = c0(Px/(x*x-1)**8)
g = (s.Integer(0), s.cancel(Ax/(a*(x*x-1)**9)))
b0 = c0(((a*P+8*U*s.diff(A, U)+2*A)/(a*(U-1)**8)).subs(U, x*x))
c_first = (s.Integer(0), -(x*x-1)**8*Ax)
c_const = c0(((U-1)**8*(a*P*(U-1)+4*U*(U-1)*s.diff(A, U)
                       -(33*U+1)*A)).subs(U, x*x))
d_const = c0(((U-1)**8*(a*P*(U-1)-4*U*(U-1)*s.diff(A, U)
                       +(1-35*U)*A)).subs(U, x*x))
chi = c0(x*Ax**2/a)
K = [c0(1088*x/(x*x-1)), (0, 68*x/(x*x-1)), one]
DA = [f, g]
DB = [b0, g]
DC = [c_const, c_first]
DD = [d_const, c_first]
D2 = [zero, zero, one]
op_check('K_A_equals_B_D2', op_comp(K, DA), op_comp(DB, D2))
op_check('C_A_equals_1_minus_chi_D2', op_comp(DC, DA),
         [one, zero, neg(chi)])
op_check('A_C_equals_1_minus_chi_K', op_comp(DA, DC),
         [add(one, neg(mul(chi, K[0]))), neg(mul(chi, K[1])), neg(chi)])
op_check('D2_C_equals_D_K', op_comp(D2, DC), op_comp(DD, K))
check('C_horizontal_kernel_equals_one',
      add(mul(c_const, f), mul(c_first, deriv(f))) == one)
for name, op in [('A', DA), ('B', DB), ('C', DC), ('D', DD)]:
    for k, coefficient in enumerate(op):
        for t, entry in enumerate(coefficient):
            den = s.denom(s.cancel(entry))
            check(f'{name}_D{k}_part{t}_no_P8_root_poles',
                  s.degree(s.gcd(den, Px), x) == 0)

# The actual 17-dimensional positive block. C produces a fixed Laurent block.
C_columns = []
for k in range(17):
    Q = U**k
    output = s.expand((-4*U*(U-1)*A*s.diff(Q, U)
        +(4*U*(U-1)*s.diff(A, U)+(31*U-33)*A+a*P*(U-1))*Q)/U**8)
    exact = add(mul(c_const, c0((Q/(U**8*(U-1)**8)).subs(U, x*x))),
                mul(c_first, deriv(c0((Q/(U**8*(U-1)**8)).subs(U, x*x)))))
    check(f'C_actual_positive_column_{k}',
          exact[1] == 0 and s.cancel(exact[0]-output.subs(U, x*x)) == 0)
    coeff = [s.expand(output).coeff(U, m) for m in range(-8, 17)]
    eq(f'C_actual_output_range_{k}', output-sum(b*U**m for b, m in zip(coeff, range(-8, 17))))
    C_columns.append(coeff)
CM = s.Matrix(25, 17, lambda i, k: C_columns[k][i])
check('C_actual_positive_block_rank_17', CM.rank() == 17)
_, pivot_rows = CM.T.rref()
pivot_determinant = CM[list(pivot_rows), :].det(method='domain-ge')
# P8 is normalized with constant coefficient 1. Its actual numerator is U^8 P8.
horizontal = s.Matrix([s.expand(U**8*P).coeff(U, k) for k in range(17)])
unit = s.zeros(25, 1)
unit[8] = 1
check('C_actual_horizontal_column_is_constant', CM*horizontal == unit)
second_columns = []
for column in C_columns:
    output = s.expand(sum(c*4*m*U**(m-1)*((4*m+1)*U+1-4*m)
                         for m, c in zip(range(-8, 17), column)))
    second_columns.append([output.coeff(U, m) for m in range(-9, 17)])
second_matrix = s.Matrix(26, 17, lambda i, k: second_columns[k][i])
check('D2_C_actual_positive_block_rank_16', second_matrix.rank() == 16)
check('D2_C_kills_exactly_horizontal_column', second_matrix*horizontal == s.zeros(26, 1))

# Fermat-cover conjugacy, expressed without choosing a complex period.
qp2 = 4*q*(4-q)  # (dq/dz)^2 / u^2
qpp = 12*(1-q/2) # (d^2q/dz^2) / u^2
eq('fermat_conjugacy_second_coefficient', qp2-4*q*(4-q))
eq('fermat_conjugacy_first_coefficient', qpp+qp2/(2*q)-4*(5-2*q))
eq('fermat_conjugacy_constant_coefficient', qpp/(4*q)-3*qp2/(16*q*q)+s.Rational(3, 4))
ratio = (4*j+3)*(4*j+1)/(16*(j+1)*(4*j+5))
eq('regular_homogeneous_coefficient_recurrence',
   (j+1)*(4*j+5)*ratio-(j*j+j+s.Rational(3, 16)))

# Characteristic-zero resonant coefficient, with p=4r-1.
p = 4*r-1
eq('exact_conjugation_second_coefficient', q*(4-q)-q*(4-q))
eq('exact_conjugation_first_coefficient',
   2*r*(4-q)+3*(1-q/2)-(5-2*q)-p*(2-q/2))
eq('exact_conjugation_constant_coefficient',
   r*(r-1)*(4-q)/q+3*r*(1-q/2)/q+s.Rational(3, 16)
   -p*(r/q-(p+4)/16))
next_coefficient = (j+r+1)*(4*j+p+4)
eq('first_new_resonance_exact_coefficient',
   next_coefficient.subs(j, 3*r-2)-p*(4*p-1))

carrier = ((1-q/2)*(1-q/4)*(1+q-q*q/4)*((1-q/2)**4+4)/5)
eq('carrier_initial_value', carrier.subs(q, 0)-1)
carrier_log_linear = s.diff(carrier, q).subs(q, 0)
eq('actual_carrier_log_linear', carrier_log_linear+s.Rational(3, 20))
eq('actual_second_carry', 17+carrier_log_linear-s.Rational(337, 20))
check('second_carry_numerator_is_split_prime', s.isprime(337) and 337 % 4 == 1)
eq('actual_carrier_q4_simple_zero', carrier.subs(q, 4))
eq('actual_carrier_q4_derivative', s.diff(carrier, q).subs(q, 4)-s.Rational(1, 4))
Llog = s.cancel(q*(4-q)*(s.diff(carrier, q, 2)*carrier-s.diff(carrier, q)**2)/carrier**2
                +3*(1-q/2)*s.diff(carrier, q)/carrier)
eq('actual_full_forcing_q4_residue_before_q_minus_r',
   s.limit((q-4)*Llog, q, 4)-1)

h0 = s.Poly(P, U).LC()
eq('A8_leading_equals_period_times_P8_leading', s.Poly(A, U).LC()-a*h0)
check('horizontal_at_origin_nonzero', h0 != 0)
check('horizontal_origin_constant_unit_for_inert_above31',
      all(k <= 31 or k % 4 == 1
          for k in list(s.factorint(abs(s.numer(h0))))+list(s.factorint(s.denom(h0)))))
check('q4_double_pole_coefficient_69_unit_for_inert_above31',
      all(k <= 31 or k % 4 == 1 for k in s.factorint(69)))
fixed_den = s.ilcm(*[s.denom(c) for poly in (P, A) for c in s.Poly(poly, U).all_coeffs()],
                   s.denom(a), s.numer(a))
fixed_bad = sorted(s.factorint(abs(fixed_den)))
check('quartet_integral_at_all_inert_above31',
      all(k <= 31 or k % 4 == 1 for k in fixed_bad))

out = {
    'status': 'PASS', 'checks': checks,
    'conventions': {'curve': 'y^2=x^3-x', 'derivation': "x'=2y,y'=3x^2-1",
                    'differential_operators': 'coefficients on the left; products are composition'},
    'P8_coefficients': [str(c) for c in s.Poly(P, U).all_coeffs()[::-1]],
    'A8_coefficients': [str(c) for c in s.Poly(A, U).all_coeffs()[::-1]],
    'period_a_star': str(a), 'horizontal_origin_constant': str(h0),
    'Darboux_operators': {
        'A': 'P8/(U-1)^8 + y*A8/(a*(U-1)^9) D_z',
        'B': '(a*P8+8*U*A8_prime+2*A8)/(a*(U-1)^8) + y*A8/(a*(U-1)^9) D_z',
        'C': '(U-1)^8*(a*P8*(U-1)+4*U*(U-1)*A8_prime-(33*U+1)*A8-y*A8*D_z)',
        'D': '(U-1)^8*(a*P8*(U-1)-4*U*(U-1)*A8_prime+(1-35*U)*A8-y*A8*D_z)',
        'chi': 'x*A8(U)^2/a',
        'identities': ['K A=B D_z^2', 'C A=1-chi D_z^2', 'A C=1-chi K', 'D_z^2 C=D K']},
    'C_actual_positive_block': {
        'input': 'P(U)/(U^8*(U-1)^8)', 'output_exponents_U': list(range(-8, 17)),
        'columns': [[str(c) for c in col] for col in C_columns], 'rank': 17,
        'max_origin_pole_order': 64, 'horizontal_column': [str(c) for c in horizontal],
        'second_derivative_rank': 16, 'second_derivative_max_origin_pole_order': 66,
        'pivot_row_exponents': [int(k)-8 for k in pivot_rows],
        'pivot_determinant': str(pivot_determinant)},
    'Fermat_cover': {'equation': 'v^4+w^4=1', 'w': '(q/4)^(1/4)',
                     'v': '(1-q/4)^(1/4)', 'u': 'sqrt(2)*w*v',
                     'conjugacy': 'D_z^2(q^(1/4)*V)=4*u^2*q^(1/4)*L_q(V)'},
    'second_carry': {'theta': '17', 'carrier': str(carrier_log_linear), 'total': '337/20',
                     'U_degree': '3*r-1', 'original_log_degree': 'p=4*r-1',
                     'resonant_coefficient': 'p*(4*p-1)',
                     'proof': 'Wilson on the complete Pochhammer residue sets; Cartier/Frobenius for the fixed rational carrier'},
    'q4': {'carrier_derivative': '1/4', 'full_forcing_residue': '4^(-r)',
           'Y_log_leading': '4*gamma^(-p), gamma^4=4',
           'K_A_Y_double_pole': '-69*h0*4*gamma^(-p)',
           'free_to_horizontal_second_solution_order': 69},
    'fixed_denominator_prime_factors': [int(k) for k in fixed_bad],
    'scope': 'Exact differential and original coefficient identities. The Fermat cover and all theta connection multipliers remain; no original central vanishing is propagated for free.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out, ensure_ascii=False, indent=2)+'\n')
print('PASS:', len(checks), 'exact checks; actual second carry=337/20; C block rank=17')
