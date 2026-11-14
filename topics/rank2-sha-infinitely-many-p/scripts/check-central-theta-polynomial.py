#!/usr/bin/env python3
"""An independent exact cumulant check of the polynomial 13*d_12.

The finite-field calculation is in check-central-theta-p13.py.  This file
checks its symbolic polynomial without using its C_n or sparse derivation
implementation.  It derives w/sigma(w) from the Weierstrass equation and
expands the logarithm of w*Theta directly.  Requires SymPy; no floating point.
"""

from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
from math import factorial
from pathlib import Path
import json

import sympy as s


U, X, Y, w = s.symbols("U X Y w")
relation = s.Poly(Y**2-X**3+17*X, Y)


def reduced(f):
    return s.Poly(s.rem(s.Poly(s.expand(f), Y), relation).as_expr(), U, X, Y)


def deriv(f):
    f = f.as_expr() if isinstance(f, s.Poly) else f
    return reduced(-X*s.diff(f, U)+2*Y*s.diff(f, X)
                   +(3*X**2-17)*s.diff(f, Y))


# wp=w^-2+sum a_n w^(4*n-2); wp''=6*wp^2-34 and g_3=0.
a = [s.Integer(1)]
for n in range(1, 4):
    rhs = 6*sum(a[j]*a[n-j] for j in range(1, n))
    if n == 1:
        rhs -= 34
    a.append(rhs/s.Integer((4*n-2)*(4*n-3)-12))
log_q = {4*n: a[n]/s.Integer(4*n*(4*n-1)) for n in range(1, 4)}
q = [s.Integer(1)]
for n in range(1, 14):
    q.append(s.cancel(sum(k*c*q[n-k] for k, c in log_q.items()
                          if k <= n)/s.Integer(n)))
assert q[4] == s.Rational(17, 60)
assert q[8] == s.Rational(5491, 50400)
assert q[12] == s.Rational(50019253, 1297296000)

# log(w*Theta(z,w))=sum D^(k-1)U(z)*w^k/k!+log(w/sigma(w)).
du = [reduced(U)]
for _ in range(12):
    du.append(deriv(du[-1]))
log_coeff = {k: du[k-1].as_expr()/s.factorial(k)+log_q.get(k, 0)
             for k in range(1, 14)}
b = [reduced(1)]
for n in range(1, 14):
    b.append(reduced(sum(k*log_coeff[k]*b[n-k].as_expr()
                         for k in range(1, n+1))/s.Integer(n)))
answer = b[13]
for _ in range(12):
    answer = deriv(answer)
answer = reduced(13*answer.as_expr()/s.factorial(12))
got = {key: Fraction(int(value.p), int(value.q))
       for key, value in answer.terms()}

# Read only the sibling's pure polynomial block; no field or point calculations
# execute here.  Keeping this comparison separate preserves the independent
# cumulant construction above.
reference = Path(__file__).with_name("check-central-theta-p13.py").read_text()
block = reference.split("# Polynomial arithmetic in Z[U,X,Y]", 1)[1]
block = block.split("\n", 1)[1].split("\nW_mod = {", 1)[0]
namespace = {"defaultdict": defaultdict, "Fraction": Fraction,
             "factorial": factorial}
exec(compile(block, "p13-pure-polynomial-reference", "exec"), namespace)
assert got == namespace["W_rat"], "different exact rational polynomials"
assert len(got) == 66
assert all(c.denominator % 13 for c in got.values())
canonical = [[list(k), c.numerator, c.denominator]
             for k, c in sorted(got.items())]
digest = sha256(json.dumps(canonical, separators=(",", ":")).encode()).hexdigest()
print(json.dumps({
    "status": "exact equality",
    "method": "logarithmic cumulants; independent SymPy quotient reduction",
    "wp_coefficients": list(map(str, a)),
    "q12": str(q[12]),
    "monomials": len(got),
    "maximum_total_degree": max(sum(k) for k in got),
    "all_denominators_are_13_units": True,
    "canonical_polynomial_sha256": digest,
}, indent=2))
