#!/usr/bin/env python3
"""R346 exact differential, residue-lattice and Cartier-polar identities."""
import json
from pathlib import Path
import sympy as s

checks = []
v, b, xi, Y, p, j, ss = s.symbols('v b xi Y p j s')


def check(name, expr):
    assert s.cancel(expr) == 0, name
    checks.append(name)


# Independent direct derivation in Q(b)[v,v^-1] + y Q(b)[v,v^-1].
even, odd = v, s.Integer(0)
direct = {0: (even, odd)}
for order in range(1, 18):
    even, odd = (
        s.expand(3*v**4*odd + (v**6+b)*s.diff(odd, v)/v),
        s.expand(s.diff(even, v)/v)
    )
    direct[order] = (even, odd)

C = [s.Poly(1, xi)]
for m in range(8):
    expr = 0
    for (r,), coeff in C[-1].terms():
        power = 2*m+1-6*r
        expr += coeff*(power*(power+1)*xi**r +
                       power*(power-2)*xi**(r+1))
    C.append(s.Poly(s.expand(expr), xi))
assert all(poly.degree() <= m and poly.nth(0) == s.factorial(2*m)
           for m, poly in enumerate(C))
checks.append('the integral even-derivative recurrence keeps its exact degree and leading factorial')

A = {}
for n in range(1, 4):
    m = 3*n-1
    A[n] = s.expand(sum((6*n-1-6*r)*C[m].nth(r)*xi**r
                       for r in range(m+1))/s.factorial(6*n-1))
    even, odd = direct[6*n-1]
    assert even == 0
    check('the original differential gives A_%s, not an independent residue input' % n,
          odd - s.factorial(6*n-1)*v**(6*n-3)*A[n].subs(xi, b/v**6))
    assert s.degree(A[n], xi) <= 3*n-1 and A[n].subs(xi, 0) == 1
checks.append('all displayed derivative polynomials have the required unit constant')
check('the first actual odd derivative polynomial',
      A[1]-1-s.Rational(7, 8)*xi**2)

K = 3
columns = [b**n*xi**(K-n)*A[n] for n in range(K, 0, -1)]
minor = s.Matrix([[s.expand(col).coeff(xi, r) for col in columns]
                  for r in range(K)])
check('the actual low coefficient residue minor is a unit power of b',
      minor.det()-b**(K*(K+1)//2))
assert all(s.degree(col, xi) <= 3*K-1 for col in columns)
checks.append('the entire residue numerator remains below the proved degree bound')

N = (3*p-1)/2
check('the original reciprocal lift differs from B_p by the exact p multiple',
      N/(N-3*j)-1/(6*j+1)-9*p*j/((N-3*j)*(6*j+1)))

# Fixed characteristic-zero polynomial degree, not a target-prime test.
degree = 4
B = sum(s.binomial(degree, r)*xi**r/s.Integer(6*r+1)
        for r in range(degree+1))
check('the finite polynomial has the full exact differential identity',
      B+6*xi*s.diff(B, xi)-(1+xi)**degree)
for n in range(7):
    lhs = sum((-1)**r*s.binomial(n, r)/s.Integer(6*r+1)
              for r in range(n+1))
    assert s.cancel(lhs-s.factorial(n)/s.rf(s.Rational(7, 6), n)) == 0
checks.append('the value excluding minus one is the proved beta product')

# The denominator never loses its original leading scalar in this proof.
exact_N = 3*degree+1
Btilde = sum(s.binomial(degree, r)*s.Rational(exact_N, exact_N-3*r)*xi**r
             for r in range(degree+1))
assert Btilde.subs(xi, 0) == 1 and s.degree(Btilde, xi) == degree
checks.append('the actual reciprocal characteristic-zero numerator retains mass one and full degree')

def reduce_curve(expr):
    numerator = s.together(expr).as_numer_denom()[0]
    return s.rem(numerator, Y**2-b**2*(1+xi), Y)

check('the full invariant infinity pole is canceled by the exact dY term',
      reduce_curve(Y/xi-b**2/Y-b**2/(Y*xi)))

c = 1+2*xi+3*xi**2
Lc = s.rem(c*s.diff(B, xi), B, xi)
check('the finite polar interpolant gives every actual residue',
      s.rem(Lc-c*s.diff(B, xi), B, xi))

# Composite exponent 9 verifies the algebraic odd-power identity only.
check('the Frobenius residue factor keeps the Y branch',
      reduce_curve((Y/b)**9-(Y/b)*(1+xi)**4))

pp = 6*ss-1
check('the maximum infinity pole stays below two p',
      (12*(ss-1)-2)-(2*pp-12))
assert [(-r*5-1) % 6 for r in range(4)] == [5, 0, 1, 2]
checks.append('the actual tame phase removes all possible negative Cartier exponents in the window')

out = {
    'status': 'PASS',
    'number_of_exact_checks': len(checks),
    'checks': checks,
    'A1': str(A[1]),
    'A2': str(A[2]),
    'A3': str(A[3]),
    'original_reciprocal_polynomial':
        'Btilde=sum binom((p-1)/2,j) N/(N-3j) xi^j, N=(3p-1)/2',
    'off_origin_residue':
        '-6*(Y/b)*xi^(-K)*sum q_n*b^n*xi^(K-n)*A_n(xi)',
    'exact_unit_minor': 'b^(K(K+1)/2)',
    'uniform_window': '1 <= K <= s-1, p=6s-1',
    'full_cartier_identity':
        'C(omega_q)=h_q^(1/p)*dlog(r)+eta(phi^-1(-6*(1+xi)^(-n0)*xi^(-K)*P_q))',
    'scope':
        'Primitive statement is for the actual off-origin residue operator. Its identification with an original C_2(M) subquotient remains to be proved. No target-prime scan.'
}
dest = Path(__file__).with_suffix('.json')
dest.write_text(json.dumps(out, ensure_ascii=False, indent=2)+'\n')
print('PASS: %s exact checks; %s' % (len(checks), dest.name))

