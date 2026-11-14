#!/usr/bin/env python3
"""Exact new R605 rational-kernel reduction; no torsion orbit is rerun."""
import hashlib
import json
from pathlib import Path
import sympy as s

base = Path(__file__).resolve().parent
source = base / 'data' / 'R595_actual_c1_CM_coefficients.recovered.json'
data = json.loads(source.read_text())['kernel']
x, t = s.symbols('x t')
Delta = sum(s.Integer(a) * x**i for i, a in enumerate(data['Delta_coefficients_ascending']))
A0, A1, A2 = [sum(s.Integer(a) * x**i for i, a in data[name])
              for name in ['A0_nonzero', 'A1_nonzero', 'A2_nonzero']]
N = x**2 * (x**6 + 34*x**3 - 8)
R = N / Delta
V = s.diff(N, x)*Delta - N*s.diff(Delta, x)
correct = s.expand(4*(x**3-1)*(s.diff(V,x)*Delta-2*V*s.diff(Delta,x))
                   + 6*x**2*V*Delta - 2*A2)
assert correct == 0
wrong = s.expand(4*(x**3-1)*(s.diff(V,x)*Delta-2*V*s.diff(Delta,x))
                 + 6*x**2*V*s.diff(Delta,x) - 2*A2)
assert wrong != 0

# H1/C0 = E*D(R) + F.  The heat equation fixes dF/dx, and F(O)=-2.
c = s.symbols('c0:7')
P = sum(c[i] * x**(3*i) for i in range(7))
F = P / Delta**2
equation = s.together(s.diff(F,x) - x*s.diff(R,x) - A1/(2*Delta**3))
eqs = s.Poly(s.fraction(equation)[0], x).all_coeffs() + [c[6]+2]
solution = s.solve(eqs, c, dict=True)
assert len(solution) == 1 and len(solution[0]) == 7
F = s.cancel(F.subs(solution[0]))
A = s.cancel(F+x*R)
J = s.cancel(A0/(2*Delta**3) + x*F/2)
assert s.cancel(s.diff(F,x)-x*s.diff(R,x)-A1/(2*Delta**3)) == 0

# Expand 1/4 D²(E²R)+1/2 D(E A)+J with DE=-x, Dy=3x².
# E² coefficient = D²R/4; E coefficient = -x DR-y R+DA/2;
# constant = x²R/2-x A/2+J.
assert s.cancel((4*(x**3-1)*s.diff(R,x,2)+6*x**2*s.diff(R,x))/4
                - A2/(2*Delta**3)) == 0
assert s.cancel(-2*x*s.diff(R,x)-R+s.diff(A,x)-A1/(2*Delta**3)) == 0
assert s.cancel(x**2*R/2-x*A/2+J-A0/(2*Delta**3)) == 0

def rational_record(f):
    n,d = s.fraction(s.cancel(f))
    return {'numerator_ascending': [int(a) for a in reversed(s.Poly(n,x).all_coeffs())],
            'denominator_ascending': [int(a) for a in reversed(s.Poly(d,x).all_coeffs())],
            'expression': str(f)}

record = {
    'result':'R605-working-rational-reduction',
    'input_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'D': {'Dx':'2y','Dy':'3x^2','DE':'-x'},
    'R595_595_10_correct_remainder':str(correct),
    'R595_595_10_old_displayed_formula_is_false':bool(wrong != 0),
    'F': rational_record(F), 'A': rational_record(A), 'J': rational_record(J),
    'identity':'H2/C0 = (1/4)*D^2(E^2*R_minus) + (1/2)*D(E*A) + J',
    'all_three_E_coefficients_exact':True,
    'no_torsion_orbit_or_prime_grid':True,
    'coefficient_reduction_scope':'R605 proof of p-adic extraction still separate from this rational identity'
}
out = base/'R605_rational_kernel_reduction.json'
out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':'PASS','F':str(F),'A':str(A),'J':str(J),
                  'output':str(out),'sha256':hashlib.sha256(out.read_bytes()).hexdigest()},indent=2))
