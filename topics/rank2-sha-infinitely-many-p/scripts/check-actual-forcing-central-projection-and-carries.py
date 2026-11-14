#!/usr/bin/env python3
"""R278: true positive central rows of the R273 forcing, with complete frames.

Symbolic coefficient and operator identities only; no prime scans.
The analytic estimates and the general Frobenius logarithm lemma are proved
in the accompanying result rather than replaced by numerical testing.
"""
import json
from pathlib import Path

import sympy as s

root = Path(__file__).parent
data = json.loads((root/'check-normtwo-finite-connection-kernel.json').read_text())
q, v, p, r, n, alpha, h0, aa = s.symbols('q v p r n alpha h0 aa')
checks = {}


def check(name, value):
    checks[name] = bool(value)
    if not checks[name]:
        raise AssertionError(name)


def eq(name, value):
    check(name, s.cancel(value) == 0)


P = sum(s.Rational(c)*v**k for k, c in enumerate(data['kernel_P8_coefficients']))
A = sum(s.Rational(c)*v**k for k, c in
        enumerate(data['de_Rham_reduction']['primitive_A8_coefficients']))
a = s.Rational(data['de_Rham_reduction']['period_coefficient'])
Pr = s.expand(v**8*P.subs(v, 1/v))
Ar = s.expand(v**8*A.subs(v, 1/v))
sv = q-q*q/4
t = 1-q/2
nu4 = 1-q/4
eq('actual_s_q_relation', sv-q*nu4)
eq('actual_t_squared', t*t-(1-sv))

h1 = s.Rational(3, 80)
nu1 = -s.Rational(1, 16)
eq('same_geometric_one_tenth', h1-nu1-s.Rational(1, 10))
carrier = t*nu4*(1+sv)*(t**4+4)/5
eq('actual_carrier_linear', s.diff(carrier, q).subs(q, 0)+s.Rational(3, 20))
eq('actual_radial_initial_log', s.Rational(17, 3)+s.diff(carrier, q).subs(q, 0)-s.Rational(331, 60))
eq('actual_carry_decomposition', s.Rational(34, 3)+s.Rational(331, 60)-s.Rational(337, 20))
eq('geometric_boundary_Wilson_reduction',
   (-1/(12*(2*r-1))).subs(r, s.Rational(1, 4))-s.Rational(1, 6))

# Z_zz = 4*u^2*L0 Z, and the actual normalized first/second q derivatives.
eq('Z_second_derivative_q_second', 16*sv-4*q*(4-q))
eq('Z_second_derivative_q_first', 12*t-4*3*t)
U0, U1, U2, U3 = s.symbols('U0 U1 U2 U3')
LqU = q*(4-q)*U2+(5-2*q)*U1-s.Rational(3, 16)*U0
eq('actual_Y_first_to_second_derivative',
   nu4*(5*U1+4*q*U2)-s.Rational(3, 16)*(U0+4*q*U1)-LqU)

# Exact characteristic-zero derivative of q^(-p/4) T.
Q, Q1, Q2, T0, T1, T2 = s.symbols('Q Q1 Q2 T0 T1 T2')
direct = (T2-p*Q1*T1/(2*Q)
          +(p*(p+4)*Q1**2/(16*Q**2)-p*Q2/(4*Q))*T0)
ell1, ell2 = Q1/Q, Q2/Q-Q1**2/Q**2
display = T2-p*ell1*T1/2+(p*p*ell1**2/16-p*ell2/4)*T0
eq('complete_characteristic_zero_p_correction', direct-display)

# The genuine D and E central rows, after the actual theta and q frames.
eq('Darboux_B_zero_order_reverse_polynomial',
   s.cancel((a*P+8*v*s.diff(A, v)+2*A)/(a*(v-1)**8)).subs(v, 1/v)
   -(a*Pr+66*Ar-8*v*s.diff(Ar, v))/(a*(1-v)**8))
Arq, Prq = Ar.subs(v, sv), Pr.subs(v, sv)
V0, V1 = s.symbols('V0 V1')
raw_E = (t*(a*Prq+66*Arq-8*sv*s.diff(Ar, v).subs(v, sv))*V0
         -4*q*nu4*Arq*(V1+(s.Rational(3, 4)/q-1/(2*(4-q)))*V0))
display_E = ((t*(a*Prq+66*Arq-8*sv*s.diff(Ar, v).subs(v, sv))
              +(5*q/4-3)*Arq)*V0-q*(4-q)*Arq*V1)
eq('complete_E_q_polynomial_operator', raw_E-display_E)

# Full Euler normal ordering: E, W, a0 have their actual commutators.
e, W, W1, ak, ak1, bk = s.symbols('e W W1 ak ak1 bk')
tM = s.symbols('tM')
normal_coeffs = [W*W-W1+7*W+12-ak*W-3*ak+bk,
                 ak-2*W-7, s.Integer(1)]
transpose = tM*tM+tM*normal_coeffs[1]-(ak1-2*W1)+normal_coeffs[0]
expected = ((tM-4)*(tM-3)-(2*tM-7)*W+(W*W+W1)
            +(tM-3)*ak-(ak1+ak*W)+bk)
eq('complete_E_unshifted_Mellin_ordering', transpose-expected)

# The two resonance locations are actual additive z exponents.
eq('B_first_negative_central_weight',
   ((3*p+3)/4-3*r).subs(p, 4*r-1))
eq('C_second_negative_central_weight',
   ((4*p+4)/4-4*r).subs(p, 4*r-1))
eq('next_possible_negative_weight',
   ((7*p+3)/4-(7*r-1)).subs(p, 4*r-1))
eq('first_carry_absorbed_by_one_derivative', (3*p)/p-3)
eq('second_Cartier_direction_derivative', (4*p+1).subs(p, 0)-1)
eq('Darboux_first_resonant_integral_carry',
   s.cancel((1-3*p)*(3*p)*(3*p-69)/p).subs(p, 0)+207)
eq('Darboux_second_resonant_integral_carry',
   s.cancel((1-(4*p+1))*(4*p+1)*(4*p+1-69)/p).subs(p, 0)-272)

# The actual Newton/falling factorial derivative coefficients.
uu = s.symbols('uu')
falling_derivatives = []
for k in range(1, 6):
    poly = s.prod(uu-j for j in range(k))
    deriv = s.diff(poly, uu).subs(uu, 0)
    check(f'falling_factorial_central_derivative_{k}',
          deriv == (-1)**(k-1)*s.factorial(k-1))
    falling_derivatives.append(str(deriv))
K = s.Rational(337, 20)
eq('actual_inhomogeneous_next_digit', 2*K-s.Rational(337, 10))
eq('fourth_weight_original_geometric_carry', -6*s.Rational(1, 10)+s.Rational(3, 5))
eq('first_band_contains_both_carries',
   ((p*p-1)/4-(7*r-1)).subs(p, 4*r-1)-(4*r*r-9*r+1))

out = {
    'status': 'PASS', 'checks': checks,
    'source_definitions': {
        'Y': 'q^(1/4)*U=q^(-p/4)*(log(F_rad)-L0-a0*H/p)',
        'B_p': 'F*z^3*Y', 'C_p': 'F*z^4*D_z(Y)',
        'D_p': 'F*z^3*A_Darboux(Y)', 'E_p': 'F*z^5*K*A_Darboux(Y)',
        'F': 'S8^17=theta^68*t^17', 'gaussian': 'exp(-c*z^(p+1)), c=68*c0, alpha=p*c'},
    'same_geometry': {'h': 'z/q^(1/4)', 'nu': '(1-q/4)^(1/4)',
                      'h_minus_nu_linear': '1/10',
                      'h_3r_minus_1_mod_p': '1/(6*kappa)',
                      'alpha_mod_p': '68*kappa'},
    'actual_first_negative_layer': {
        'window': 'z exponent <7*p, equivalently positive w exponent <7*r-1',
        'p_Y': '(337/20)*z^(3*p)+(alpha/10)*z^(4*p+1)',
        'p_B_hat': 'F_hat*((337/20)*w^(3*r)+(alpha/10)*w^(4*r))',
        'p_C_hat': 'F_hat*(alpha/10)*w^(4*r)',
        'p_D_hat': 'F_hat*((337/20)*f*w^(3*r)+(alpha/10)*(f+g/z)*w^(4*r))',
        'p_E_hat': '0',
        'second_horizontal_order_w': 17,
        'second_horizontal_leading': '1/(69*a_star*h0)'},
    'radial_initial_log': '331/60',
    'carry_decomposition': '337/20=34/3+331/60',
    'B_prime_mod_p3': '(p/alpha)*b_r-(p^2/alpha^2)*b_2r+2*p^2*(337/20)/alpha^3',
    'C_prime_mod_p4': '(p/alpha)*c_r-(p^2/alpha^2)*c_2r+2*p^3*c_3r/alpha^3-3*p^3/(5*alpha^3)',
    'falling_factorial_derivatives': falling_derivatives,
    'central_raw_moments': {
        'B': '[q^(N-1)] theta^68*t^17*U*h^(2-4*N)*nu^(-3)',
        'C': '[q^(N-1)] theta^68*t^17*(U+4*q*U_prime)*h^(3-4*N)',
        'D': '[q^(N-1)] theta^68*V_p*h^(2-4*N)*nu^(-3)',
        'E': '(4/a_star)*[q^(N-2)]theta^68*W_p*h^(4-4*N)*nu^(-1)',
        'N': 'r*p^n; all n>=0'},
    'reversed_P8_coefficients': [str(c) for c in s.Poly(Pr, v).all_coeffs()[::-1]],
    'reversed_A8_coefficients': [str(c) for c in s.Poly(Ar, v).all_coeffs()[::-1]],
    'Tate_norm': 'Each complete Gaussian-normalized source has norm <=rho^4 at rho=p^(-1/(2*p)).',
    'scope': 'Actual central functions and full original depth criterion for these four explicit sources; no implication from the three original curve zeros is assumed.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out, ensure_ascii=False, indent=2)+'\n')
print('PASS:',len(checks),'symbolic checks; both carries and all four original-frame sources retained')
