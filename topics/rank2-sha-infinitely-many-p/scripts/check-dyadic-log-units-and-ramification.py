#!/usr/bin/env python3
"""Exact certificates for R256; no target-prime sampling."""
import json
from pathlib import Path

import sympy as s

t, x, y, a, A = s.symbols('t x y a A')
I = s.I
checks = {}


def check(name, value):
    checks[name] = bool(value)
    if not checks[name]:
        raise AssertionError(name)


fp = t**4 + 4*I*t**3 + 2*t**2 - 4*I*t + 1
fm = fp.xreplace({I: -I})
f8 = t**8 + 20*t**6 - 26*t**4 + 20*t**2 + 1
check('eight_value_polynomial', s.expand(fp*fm-f8) == 0)
check('quartic_discriminant', s.discriminant(fp, t) == -2**16)
check('eight_value_discriminant', s.discriminant(f8, t) == 2**64)

gb = s.groebner([A**2-2*a+2, a**2-2], A, a, extension=I)


def red(expr):
    return gb.reduce(s.expand(expr))[1]


quadratics = (t**2-2*I*(a-1)*t-1)*(t**2+2*I*(a+1)*t-1)
check('two_quadratic_factors',
      all(red(c) == 0 for c in s.Poly(s.expand(quadratics-fp), t).all_coeffs()))
u = A + I*(a-1)
uinv = A - I*(a-1)
B = A*(a+1)
v = -I*(a+1+B)
vinv = I*(a+1-B)
check('B_squared', red(B**2-2*a-2) == 0)
check('A_times_B', red(A*B-2) == 0)
check('u_inverse', red(u*uinv-1) == 0)
check('v_inverse', red(v*vinv-1) == 0)
for label, root in [('u', u), ('minus_u_inverse', -uinv),
                    ('v', v), ('minus_v_inverse', -vinv)]:
    check('quartic_root_'+label, red(fp.subs(t, root)) == 0)
check('u_recovers_a', red(u-uinv+2*I-2*I*a) == 0)
tau_u = u.subs({a: -a, A: I*B}, simultaneous=True)
check('tau_u_is_minus_v_inverse', red(tau_u+vinv) == 0)
tau_A2 = (I*B).subs({a: -a, A: I*B}, simultaneous=True)
check('tau_squared_A', red(tau_A2-A) == 0)

x_of_t = (1+t)/(1-t)
dup = (x**2+1)**2/(4*x*(x**2-1))
check('actual_duplication_in_r', s.cancel(
    dup.subs(x, x_of_t)-(1+t**2)**2/(4*t*(1-t**2))) == 0)
check('quarter_diagonal_plus_i', s.cancel(
    4*t*(1-t**2)*(dup.subs(x, x_of_t)-I)-fp) == 0)

beta = 4-I
K = beta*x**8+(-12+20*I)*x**6+(28+10*I)*x**4+(-20-12*I)*x**2-I
reverse = s.expand(y**8*K.subs(x, 1/y))
eisenstein = y**8+I*beta*((-4-4*I)*y**6+(6+4*I)*y**4+(-4+4*I)*y**2+1)
check('monic_beta_eisenstein_identity', s.expand(I*reverse-eisenstein) == 0)
check('beta_prime_norm', s.expand(beta*s.conjugate(beta)) == 17)
check('eisenstein_constant', s.expand(eisenstein.subs(y, 0)-I*beta) == 0)

valuation_matrix = s.Matrix([
    [2, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 1, -1, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, -1],
])
check('five_s_unit_valuation_rank', valuation_matrix.det() == 8)

result = {
    'result': 'PASS', 'checks': checks,
    'quartic': str(fp), 'eight_value_polynomial': str(f8),
    'quartic_discriminant': str(-2**16),
    'eight_value_discriminant': str(2**64),
    'beta_eisenstein_polynomial': str(s.expand(eisenstein)),
    's_unit_valuation_matrix': [list(map(str, row)) for row in valuation_matrix.tolist()],
    'proof_scope': 'Exact identities only. Multiplicative independence and ramification separation are proved in R256.'
}
output = Path(__file__).with_suffix('.json')
output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
print(f"PASS: {len(checks)} exact checks; {output.name}")
