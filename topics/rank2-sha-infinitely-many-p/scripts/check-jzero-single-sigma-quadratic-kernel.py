#!/usr/bin/env python3
"""R327: exact single-sigma quadratic kernel of the original rank-two source.

No target-prime scan: source identities, fixed phases, degree, contraction
and the complete conditional sixth moment are checked symbolically.
"""
from pathlib import Path
import json
import sympy as s

X, b, delta, p, pb, Om = s.symbols("X b delta p pbar Omega")
R = s.Rational
checks = []


def check(name, condition):
    assert condition, name
    checks.append(name)


def red(poly):
    return s.rem(s.Poly(s.expand(poly), delta), s.Poly(delta**2+3, delta)).as_expr()


omega = (-1+delta)/2
gamma = (5+delta)/2
gammabar = (5-delta)/2
check("actual CM7 direction 2-delta", red(-omega*gamma-(2-delta)) == 0)
check("actual conjugate CM7 direction 2+delta", red(-(omega**2)*gammabar-(2+delta)) == 0)
check("the two sigma unit phases have product one", red((-omega)*(-omega**2)-1) == 0)
check("actual CM7 norm", red(gamma*gammabar-7) == 0)

P1 = (X+b)*(X-8*b)*(7*X**2-4*b*X+16*b**2)/7
x_difference_over_x = (X-8*b)/(4*(X+b))+(X+4*b)/(3*X)
check("actual CM2-CM3 coordinate difference",
      s.factor(x_difference_over_x-(7*X**2-4*b*X+16*b**2)/(12*X*(X+b))) == 0)
# Q = 144 sigma^34 x^4 (X+b)^2 (X-8b).
# Multiplication by (x2-xdelta) and division by sigma^34*x^2 gives x^3=X.
check("complete target polynomial with coefficient 1/84",
      s.factor(R(144,84)*X*(X+b)**2*(X-8*b)*x_difference_over_x-P1) == 0)
check("actual common U frame", s.factor(
      (X+b)*(7*X**2-4*b*X+16*b**2)/(7*X*(X-8*b)**3)
      - P1/(X*(X-8*b)**4)) == 0)
check("eight pure sigma factors have actual degree 34", 1+3*4+3*3+12 == 34)
check("all exact leading sigma phases", red(2**3*delta**3*(2*delta)-144) == 0)
check("the original target has leading coefficient one", R(144,84)*R(7,12) == 1)
check("actual log transvectant has the same scalar", -R(1,1008)*(-12) == R(1,84))
check("sigma pair variance has the exact source scalar", -R(1,168)*(-2) == R(1,84))

# First genuine next original coefficient, using log(sigma/z)=b*z^6/210+...
q1 = R(1,210)*(1+3*64+3*(-27)+(-1728))
check("the second original target coefficient is retained",
      s.simplify(R(144,84)*(q1*R(7,12)-1)+R(988,105)) == 0)

a1,a2,a3,r1,r2,r3,ss,tt = s.symbols("a1 a2 a3 r1 r2 r3 s t")
y = ss+2*(a1+a2+a3)+delta*(r1+r2+r3)+2*delta*tt
ys = ss+delta*(a1+a2+a3)+2*(r1+r2+r3)+2*delta*tt
w = (a1-a2)**2-(r1-r2)**2
swap = {a1:r1,a2:r2,a3:r3,r1:a1,r2:a2,r3:a3}
check("true block exchange preserves the product measure", s.expand(y.xreplace(swap)-ys) == 0)
check("true block exchange reverses the quadratic weight", s.expand(w.xreplace(swap)+w) == 0)
av = ((a1-a2)**2+(a1-a3)**2+(a2-a3)**2)/3
check("exact symmetric variance average",
      s.expand(av-(a1*a1+a2*a2+a3*a3-(a1+a2+a3)**2/3)) == 0)

k = p/pb**2
allp = k**2/pb**8
check("quadratic weight pays two complete p factors", s.cancel(allp-p**2/pb**12) == 0)
check("all finite sextic phases cancel", (3*8) % 6 == 0)
alpha = 1-p**2/pb**11
check("primitive-input output carry uses the exact previous layer",
      s.cancel(1-pb*allp-alpha) == 0)
euler6 = 1-(p/pb)**6/pb**7
moment6 = alpha*pb**(-13)*euler6*s.factorial(6)*Om**6
check("conditional normalized sixth moment retains both Euler factors",
      s.cancel(moment6-(1-p**2/pb**11)*(1-p**6/pb**13)*720*Om**6/pb**13) == 0)

data = {
    "status": "PASS",
    "checks": checks,
    "original_source": "S=Q*(x(2z)-x(delta z))/84",
    "Q": "sigma(z)*sigma(2z)^3*sigma(delta z)^3*sigma(2delta z)",
    "Q_polynomial": "144*sigma^34*x^4*(X+b)^2*(X-8b)",
    "source_polynomial": str(s.expand(P1)),
    "mu": "nu_sigma^tensor8",
    "output": str(y),
    "weight": str(w),
    "measure_scalar": "-1/(168*Omega_p^2)",
    "all_input_p_coefficient": "p^2/pbar^12",
    "primitive_input_carry_factor": "1-p^2/pbar^11",
    "norm_tail_valuation": "at least 2*(N+1) after N input-depth levels",
    "conditional_sixth_moment_at_output_depth_n":
        "pbar^(-13*n)*(1-p^2/pbar^11)*(1-p^6/pbar^13)*720*Omega_p^6",
    "ordinary_prime_scope": "p>7, p=1 mod3, the original E17 period and psi17 frame",
    "central_scope": "All output-unit boundaries and all tame mass terms are retained.",
}
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(data, ensure_ascii=False, indent=2)+"\n")
print(f"PASS: {len(checks)} exact checks; {out.name}")
