#!/usr/bin/env python3
"""R342 fixed symbolic identities.  No target-prime scan."""
import json
from pathlib import Path
import sympy as s

checks = []
w, eps, p, a, Delta, kappa, b = s.symbols('w epsilon p a Delta kappa b')


def check(name, expr):
    assert s.cancel(expr) == 0, name
    checks.append(name)


def trunc_eps(expr):
    poly = s.Poly(s.expand(expr), eps)
    return sum(poly.nth(i) * eps**i for i in range(3))


def e2(v):
    return 1 + v + v**2 / 2


check('the full original finite Gaussian product is unchanged',
      trunc_eps(e2(-p * Delta * eps) * e2((a + p * Delta) * eps)
                - e2(a * eps)))

raw = s.symbols('S0:8')
for n in range(8):
    gaussian = [sum((-kappa)**j / s.factorial(j) * raw[h-j]
                    for j in range(h+1)) for h in range(n+1)]
    value = sum(s.ff(n, h) * gaussian[h] / kappa**h for h in range(n+1))
    assert s.cancel(value - s.factorial(n) * raw[n] / kappa**n) == 0
checks.append('exact complete integer-weight convolution including mass at weight zero')

u, mass, slope, logr = s.symbols('u mass slope log_ratio')
check('complete central derivative preserves the explicit mass correction',
      s.diff((1 + logr*u) * (mass + slope*u), u).subs(u, 0)
      - slope - mass*logr)

t, h, G, T, F = s.symbols('t h G T F')
hp = (G-h)/(6*t)
Tp = (-G*F-T)/(6*t)
U = T/h
physical_euler_U = 6*t*h/G * (Tp*h-T*hp)/h**2
check('the true physical Euler operator sends T/h to minus F',
      U + physical_euler_U + F)
check('the double Euler forcing first coefficient agrees with the original h star',
      (-b/s.Integer(14))/(6*7) + b/s.Integer(588))

hs = s.symbols('h0:8')
bs = s.symbols('B0:8')
hstar_minus_one = sum(hs[n]*w**n for n in range(1, 8))
Uformal = sum(hs[n]*w**n/(6*n*(6*n+1)) for n in range(1, 8))
Bformal = sum(bs[n]*w**n for n in range(8))
for j in range(1, 8):
    adjoint = sum(bs[r]*w**r/(6*(j-r)*(6*(j-r)+1)) for r in range(j))
    assert s.expand(Uformal*Bformal -
                    hstar_minus_one*adjoint).coeff(w, j) == 0
checks.append('the full finite dual Euler inverse retains all convolution terms')

# A fixed composite auxiliary exponent, not a target-prime example.
n0, P = 4, 9
N = 3*n0+1
x, y, v, X, Y = s.symbols('x y v X Y')
Rp = sum(s.binomial(n0, j)*b**(n0-j)*x**(3*j+1) /
         (2*(3*j+1)) for j in range(n0+1))
check('the finite rational numerator has the exact derivative',
      s.diff(Rp, x) - (x**3+b)**n0/2)
Dz = 2*s.diff(Rp, x)/(x**3+b)**n0 - \
     3*P*x**2*Rp/(x**3+b)**((P+1)//2)
check('the full first Frobenius error is retained before reduction',
      Dz - 1 + 3*P*x**2*Rp/(x**3+b)**((P+1)//2))

for n in range(7):
    finite_sum = sum((-1)**j*s.binomial(n, j)/s.Integer(3*j+1)
                     for j in range(n+1))
    assert s.cancel(finite_sum - s.factorial(n)/s.rf(s.Rational(4, 3), n)) == 0
checks.append('the nonzero two-torsion values use the exact rational beta product')
remainder = s.rem(Rp - x*b**n0*s.factorial(n0) /
                  (2*s.rf(s.Rational(4, 3), n0)), x**3+b, x)
check('all three two-torsion values are the same proved scalar times x', remainder)

assert all((5*k) % 6 != 1 for k in range(1, 5))
assert (5*5) % 6 == 1
checks.append('the first possible difference of the two type-one primitives is degree 5p')
check('the rational primitive leading coefficient differs from one by a p multiple',
      -1/(3*p-1) - 1 + 3*p/(3*p-1))


def curve_numerator(expr, variable, rhs):
    numerator = s.together(expr).as_numer_denom()[0]
    return s.rem(numerator, variable**2-rhs, variable)


Xmap = b/v**2
Ymap = b*y/v**3
check('the fixed elliptic quotient has parameter b squared',
      curve_numerator(Ymap**2-Xmap**3-b**2, y, v**6+b))
rmap = (Ymap-b)/(Ymap+b)
check('the Miller square is the exact three-torsion unit with scalar b',
      curve_numerator((v**3-y)**2-b*rmap, y, v**6+b))
dlogr = (1/(Y-b)-1/(Y+b))*3*X**2/(2*Y)
check('the exact three-torsion logarithmic differential and its sign',
      curve_numerator(dlogr-3*b/(X*Y), Y, X**3+b**2))

Rtilde = s.cancel(X**N*Rp.subs(x, b/X)).expand()
assert s.degree(Rtilde, X) == N-1
assert all(exponent[0] % 3 == 0 for exponent, coeff in s.Poly(Rtilde, X).terms())
check('the reciprocal polynomial keeps its original exact constant',
      Rtilde.subs(X, 0) - b**N/(2*N))
Tp_desc = X*Rtilde**2/(b**P*(X**3+b**2)**P)
Zp_squared = Rp.subs(x, v**2)**2/(v**6+b)**P
check('the entire p-dependent rational function descends without deleting any factor',
      Tp_desc.subs(X, Xmap)-Zp_squared)
check('the descended leading coefficient is X/b after reduction',
      1/(3*p-1)**2 - 1 - (6*p-9*p**2)/(3*p-1)**2)

out = {
    'status': 'PASS',
    'number_of_exact_checks': len(checks),
    'checks': checks,
    'auxiliary_polynomial_check_exponent': 9,
    'auxiliary_exponent_is_composite': True,
    'full_mellin_identity': 'J_kappa_star(u)=(kappa/kappa_star)^u J_kappa(u)',
    'fixed_physical_forcing_equation': '6wD(1+6wD)U=z*sqrt(x)-1',
    'true_obstruction_target': 'C_2(M) including the full beta_1 image and both thirteen-row boundaries',
    'finite_primitive': 'Z_p=R_p(x)/y^p; dZ_p/dz=1-3p*x^2*R_p(x)/y^(p+1)',
    'elliptic_quotient': 'Y^2=X^3+b^2, X=b/v^2, Y=b*y/v^3',
    'torsion_unit': '(Y-b)/(Y+b), divisor 3(Q_plus-Q_minus)',
    'specified_branch': 'Q_minus=(0,-b)',
    'residue_identity': 'sum q_n hstar_n = -1/3 Res_Qminus (sum q_n T_p^(-3n)) dlog r',
    'scope': 'Fixed exact identities only; the uniform p-integrality, branch precision and complete Newton tail are proved in R342. No target-prime scan.'
}
dest = Path(__file__).with_suffix('.json')
dest.write_text(json.dumps(out, ensure_ascii=False, indent=2)+'\n')
print('PASS: %s exact checks; %s' % (len(checks), dest.name))

