#!/usr/bin/env python3
"""R424: exact full polynomial identity for the original half-period kernel.

Uses SymPy over QQ. No sampling, truncation, or target-prime computation.
"""

import json
import sympy as sp

x, z, b = sp.symbols("x z b")
X, Z = x**3, z**3
s = x**2*(X+1)*(X-8)*(X**2-sp.Rational(4, 7)*X+sp.Rational(16, 7))
l = z*(Z**2+20*Z-8)*(Z+4)*(Z**3-96*Z**2+48*Z+64)
ps, pl = sp.Poly(s, x), sp.Poly(l, z)
sh = sp.Poly(sum(c*(2-x)**i[0]*(x+1)**(17-i[0])
                 for i, c in ps.terms()), x)
lh = sp.Poly(sum(c*(2-z)**i[0]*(z+1)**(19-i[0])
                 for i, c in pl.terms()), z)
# This exact congruence filter is the sum over all three actual e^3=-1 roots.
three_root_sum = sum(sp.Rational(1, 3**17)*a*c*x**i[0]*z**j[0]
                     for i, a in sh.terms() for j, c in lh.terms()
                     if (i[0]+j[0]) % 3 == 0)
original_half_sum = sp.Poly(-sp.Rational(1, 2)*(s*l+three_root_sum), x, z)

M0 = sp.Matrix([[512, -128, 224], [-128, -832, 1024], [224, 1024, 206]])
M12 = sp.Matrix([[-2432, -256, 16], [-256, 1144, -4], [16, -4, 7]])
vectors_x = [sp.Matrix([x**k for k in range(r, 9, 3)]) for r in range(3)]
vectors_z = [sp.Matrix([z**k for k in range(r, 9, 3)]) for r in range(3)]
B = ((vectors_x[0].T*M0*vectors_z[0])[0]
     +(vectors_x[1].T*M12*vectors_z[2])[0]
     +(vectors_x[2].T*M12.T*vectors_z[1])[0])
g = x*(X+1)*(X-8)
r = Z**2+20*Z-8
expected = sp.Poly(-sp.Rational(2, 21)*g*r*(z-x)*z*(Z-8)*B, x, z)
assert original_half_sum == expected
assert sp.Poly(B, x, z) == sp.Poly(B.xreplace({x: z, z: x}), x, z)
assert sp.Poly(B, x, z).degree(x) == sp.Poly(B, x, z).degree(z) == 8

# Restore every coefficient over general y^2=x^3+b by its exact weight.
Bb = sum(c*b**(5-(i+j)//3)*x**i*z**j
         for (i, j), c in sp.Poly(B, x, z).terms())
fx = x*(x**6-sp.Rational(4, 7)*b*x**3+sp.Rational(16, 7)*b*b)
fz = z*(z**6-sp.Rational(4, 7)*b*z**3+sp.Rational(16, 7)*b*b)
gx = x**9-30*b*x**6-144*b*b*x**3-32*b**3
gz = z**9-30*b*z**6-144*b*b*z**3-32*b**3
assert sp.expand((z-x)*Bb-7*(fx*gz-gx*fz)) == 0
M0b = sp.Matrix([[M0[i, j]*b**(5-i-j) for j in range(3)] for i in range(3)])
M12b = sp.Matrix([[M12[i, j]*b**(4-i-j) for j in range(3)] for i in range(3)])
assert sp.factor(M0b.det()) == -2**15*3**9*b**9
assert sp.factor(M12b.det()) == -2**10*3**9*b**6
full = sp.zeros(9)
for i in range(3):
    for j in range(3):
        full[3*i, 3*j] = M0b[i, j]
        full[1+3*i, 2+3*j] = M12b[i, j]
        full[2+3*j, 1+3*i] = M12b[i, j]
assert sp.factor(full.det()) == 2**35*3**27*b**21
assert sp.expand(sp.Poly(Bb, z).coeff_monomial(z**8)
                 - x*(7*x**6-4*b*x**3+16*b*b)) == 0

first_y_jet = sp.Poly(original_half_sum.as_expr(), x).coeff_monomial(x**16)
expected_y_jet = sp.Rational(2, 3)*z*z*(Z-8)*(Z**2+20*Z-8)*(Z**2-sp.Rational(4, 7)*Z+sp.Rational(16, 7))
assert sp.expand(first_y_jet-expected_y_jet) == 0

report = {
    "scope": "Complete exact polynomial source identity; no sampling or target-prime scan.",
    "half_period_normalization": "c_t^72=(3e^2)^(-18), e^3=-b",
    "full_source_identity": True,
    "symmetric_kernel": True,
    "exact_two_source_bezout_identity": True,
    "kernel_bidegree_in_x_coordinates": [8, 8],
    "kernel_theta_degrees": [16, 16],
    "M0_at_b1": [[int(c) for c in row] for row in M0.tolist()],
    "M12_at_b1": [[int(c) for c in row] for row in M12.tolist()],
    "M0_determinant": "-2^15*3^9*b^9",
    "M12_determinant": "-2^10*3^9*b^6",
    "full_B_determinant": "2^35*3^27*b^21",
    "B_general_terms": [{"x_degree": i, "z_degree": j, "coefficient": str(c)}
                        for (i, j), c in sp.Poly(Bb, x, z).terms()],
    "first_boundary": "-(2/21)*Theta(y)*sigma(gamma7*y)*sigma(gamma7_bar*y)",
    "first_even_mixed_jet_verified": True,
    "central_scope": "No inference of vanishing for restricted mixed domains."
}
print(json.dumps(report, indent=2))
