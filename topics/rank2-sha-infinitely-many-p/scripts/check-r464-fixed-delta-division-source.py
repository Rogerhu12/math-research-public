#!/usr/bin/env python3
"""Exact fixed delta division source, its norm, trace, and full b scaling.

This certificate uses the original C13/C15 coefficients. It links the
complete degree-102 source polynomials to the independent characteristic-zero
CM7 matrix certificate. It does not scan target primes.
"""
from pathlib import Path
import json
import sympy as s

X, x, y, b, u = s.symbols("X x y b u")
Q = s.Rational
checks = []


def check(label, value):
    assert value, label
    checks.append(label)


vectors = {
    "A13": [0, Q(10880, 14847), -Q(13504, 14847), Q(6269, 9898),
            -Q(6523, 59388), -Q(37, 33936)],
    "A15": [0, Q(923, 1470), Q(107, 5880), Q(11399, 15680),
            -Q(15919, 94080), -Q(37, 53760)],
}
u_delta = -(x**3 + 4*b)/(3*x**3)
r_delta = -24*b*y/(x*(x**3 + 4*b))
check("exact logarithmic derivative", s.cancel(2*y*s.diff(u_delta, x)/u_delta-r_delta) == 0)
x_delta = -(x**3 + 4*b)/(3*x**2)
check("division ratio x(delta z)/x(z)", s.cancel(x_delta/x-u_delta) == 0)

# The three x-coordinates over a generic target with x=u.
fiber = x**3 + 3*u*x**2 + 4*b
check("actual degree-three x fiber", s.cancel((x_delta-u)*(-3*x**2)-fiber) == 0)
# Product of the three roots is -4b. Thus Norm(x)=-4b and Norm(u_delta)=-u^3/(4b).
norm_x = -4*b
norm_u = -u**3/(4*b)
check("exact norm ratio", s.cancel(u**3/norm_x-norm_u) == 0)

# R_delta(x_i)/delta = 8b*y_target/[u*(u*x_i^2+4b)].
inverse = s.invert(u*x**2+4*b, fiber, x)
ip = s.Poly(inverse, x)
root_traces = [3, -3*u, 9*u**2]
trace_inverse = s.cancel(sum(ip.nth(i)*root_traces[i] for i in range(3)))
check("entire fiber logarithmic trace", trace_inverse == Q(3, 4)/b)
check("trace R_delta/delta = 6y/x", s.cancel(8*b*y/u*trace_inverse-6*y/u) == 0)

matrix_path = Path(__file__).with_name("check-r464-degree102-cm7-exact.json")
matrix_data = json.loads(matrix_path.read_text())
matrix_sources = {a["label"]: a for a in matrix_data["sources"]}
out = {}

for label, P in vectors.items():
    c = P[5]/b
    polynomial = s.Poly(s.expand(
        8*3**16*b*(X+b)*(X-8*b)
        *sum(P[j]*b**(4-j)*Q(-1, 27)**j*X**(10-2*j)*(X+4*b)**(3*j-1)
             for j in range(1, 6))), X)
    # Direct original sigma/coordinate pullback, divided by delta.
    pull_poly = sum(P[j]*b**(4-j)*x_delta**(3*j) for j in range(1, 6))
    direct = (-24*b/(x*(x**3+4*b)))*(-3)**17*x**34 \
        *((x**3+b)*(x**3-8*b)/(9*x**3))*pull_poly
    check(label+" exact original pullback polynomial",
          s.cancel(direct-polynomial.as_expr().subs(X, x**3)) == 0)
    check(label+" degree sixteen and original z^6 coefficient",
          polynomial.degree() == 16 and s.cancel(polynomial.LC()+24*b*c) == 0)
    for j in range(17):
        check(label+f" full b weight coefficient {j}",
              s.cancel(polynomial.nth(j)-polynomial.nth(j).subs(b, 1)*b**(16-j)) == 0)
    coeffs_b1 = [str(polynomial.nth(j).subs(b, 1)) for j in range(18)]
    check(label+" complete CM7 input agrees",
          coeffs_b1 == matrix_sources[label]["polynomial_coefficients_ascending"])
    trace_poly = s.Poly(s.expand(
        6*(X+b)*sum(P[j]*b**(4-j)*X**(j-1) for j in range(1, 6))), X)
    check(label+" exact full trace mass", s.cancel(trace_poly.nth(5)-6*c) == 0)
    arith = matrix_sources[label]["arithmetic_components"]
    check(label+" arithmetic projection mass",
          sum(s.Rational(a["coefficient"][0]) for a in arith[1:]) == P[5])
    out[label] = {
        "C_coefficients": [str(q) for q in P],
        "C_prime_at_zero": str(-c),
        "A_polynomial_b1_ascending": coeffs_b1,
        "A_polynomial_b1_factored": str(s.factor(polynomial.as_expr().subs(b, 1))),
        "A_scaling": "A_C,b(z)=b^(-1)*A_C,1(b^(1/6)*z)",
        "A_leading_z6": str(s.factor(polynomial.LC())),
        "trace_basis": "sigma^34*x^2*(1,X,...,X^5)",
        "trace_coefficients_b1_ascending": [str(trace_poly.nth(j).subs(b, 1)) for j in range(6)],
        "trace_mass": str(6*c),
        "arithmetic_projection_coefficients_b1": [a["coefficient"][0] for a in arith],
    }

denominator_lcm = s.Integer(1)
for part in ("real", "delta"):
    for row in matrix_data["matrix"][part]:
        for value in row:
            denominator_lcm = s.ilcm(denominator_lcm, s.Rational(value).q)
for item in out.values():
    for key in ("C_coefficients", "A_polynomial_b1_ascending",
                "trace_coefficients_b1_ascending",
                "arithmetic_projection_coefficients_b1"):
        for value in item[key]:
            denominator_lcm = s.ilcm(denominator_lcm, s.Rational(value).q)
fixed_bad_integer = denominator_lcm * 2*3*5*7*17*37*667*1279
report = {
    "status": "all exact original delta identities passed",
    "norm_x": str(norm_x),
    "norm_u_delta": str(norm_u),
    "trace_inverse_mod_fiber": str(inverse),
    "trace_logarithmic_derivative": "Tr_delta(R_delta)/delta = 6*y/x",
    "fixed_denominator_lcm": str(denominator_lcm),
    "fixed_bad_integer_in_addition_to_R460": str(fixed_bad_integer),
    "sources": out,
    "checks": checks,
    "check_count": len(checks),
}
Path(__file__).with_suffix(".json").write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n")
print(json.dumps({"status": report["status"], "check_count": len(checks)}))
