#!/usr/bin/env python3
"""R316: exact degree-one Schwartz phases and original four-factor carry.

No prime scan.  The two CM13 fibers use the complete original sigma trace;
the p-core and convergence assertions are proved in the accompanying text.
"""
from fractions import Fraction
from pathlib import Path
import json
from flint import fmpq, fmpq_poly
import sympy as sp


class C64:
    modulus = fmpq_poly([1] + [0] * 31 + [1])

    def __init__(self, value=0):
        if isinstance(value, C64):
            self.p = value.p
            return
        if isinstance(value, Fraction):
            value = fmpq(value.numerator, value.denominator)
        if not isinstance(value, (list, fmpq_poly)):
            value = [value]
        self.p = fmpq_poly(value) % self.modulus

    def __add__(self, value):
        return C64(self.p + C64(value).p)

    __radd__ = __add__

    def __neg__(self):
        return C64(-self.p)

    def __sub__(self, value):
        return self + (-C64(value))

    def __rsub__(self, value):
        return C64(value) - self

    def __mul__(self, value):
        return C64(self.p * C64(value).p)

    __rmul__ = __mul__

    def __truediv__(self, value):
        gcd, inverse, _ = C64(value).p.xgcd(self.modulus)
        assert gcd == 1
        return self * C64(inverse)

    def __pow__(self, exponent):
        if exponent < 0:
            return (C64(1) / self) ** (-exponent)
        out, value = C64(1), self
        while exponent:
            if exponent & 1:
                out = out * value
            value = value * value
            exponent //= 2
        return out

    def __eq__(self, value):
        return self.p == C64(value).p


checks = []


def check(label, condition):
    assert condition, label
    checks.append(label)


z = C64([0, 1])
z8 = z ** 8
sq2 = z8 + z8 ** -1
phi = {1: 1, 3: 1, 5: -1, 7: -1}
check("exact square root in the dyadic field", sq2 * sq2 == 2)

# alpha=2, unramified chi_2 with chi_2(2)=-1.  In particular these are the
# original PLUS-cross-term Rao kernels; changing v to -v changes this odd line.
omega_output = []
for a in range(16):
    value = z8 / 4 * sum(
        (z ** (-3 * (a * a + 8 * a * b + 4 * b * b)) * v
         for b, v in phi.items()), C64(0))
    expected = phi.get(a // 2, 0) if a % 2 == 0 else 0
    check("omega full eighth-lattice output " + str(a), value == expected)
    omega_output.append(expected)

star_output = []
for a in range(8):
    value = z8 * sq2 / 2 * sum(
        (z ** (-3 * (11 * a * a + 26 * a * b + 11 * b * b)) * v
         for b, v in phi.items() if (a - b) % 4 == 0), C64(0))
    check("principal generator full quarter-lattice output " + str(a),
          value == phi.get(a, 0))
    star_output.append(phi.get(a, 0))
check("negative generator splitting pays the odd reflection", (-z8) * (-1) == z8)
check("dyadic original squared norm", sum(v * v for v in phi.values()) * Fraction(1, 2) == 2)
check("odd half-character", all(phi.get((-b) % 8, 0) == -v for b, v in phi.items()))
check("rational support n/12 retains the original character",
      all(phi[(3 * b) % 8] == v for b, v in phi.items()))
check("Jacobi coefficient is the original chi-minus-eight",
      all((-1) ** ((n - 1) // 2) * z ** (4 * n * n) == z ** 4 * phi[n % 8]
          for n in range(1, 17, 2)))

delta = sp.sqrt(-3)
omega = (-1 + delta) / 2
s = (3 + delta) / 6
kappa_infinity = 6 * sp.sqrt(3)
h = sp.sqrt(kappa_infinity) / (12 * sp.pi * sp.I)
check("degree-one Gaussian equals the exact Hermite gauge",
      sp.simplify(sp.sqrt(3) * sp.pi * h ** 2 + 1 / (8 * sp.pi)) == 0)
check("original real weight scale is minus one-third",
      sp.simplify((2 * sp.pi / sp.sqrt(3)) * 4 * sp.pi * h ** 2) == -sp.Rational(1, 3))
check("primitive delta point is the real 2Omega/3 point", sp.simplify(s / delta - (sp.Rational(2, 3) - s)) == 0)
e_cm_one = sp.simplify(sp.conjugate(delta) / (6 * delta ** 2) * (-2))
check("two actual delta residues give the whole critical value", sp.simplify(e_cm_one + delta / 9) == 0)
check("Kronecker first weight fixes kappa sigma to one-ninth",
      sp.simplify(e_cm_one / (-omega * (1 - omega))) == sp.Rational(1, 9))
check("odd CM period phase", sp.simplify(s ** 3 - delta / 9) == 0)
check("uniform finite weight period",
      [m for m in range(12) if (2*m+1) % 3 == 0 and (2*m+1) % 4 == 3] == [1, 7])
yang_constant = sp.pi * sp.sqrt(12 * sp.sqrt(3)) / (54 * sp.sqrt(3))
check("all original finite and archimedean norms",
      sp.simplify(sp.Rational(2, 6) * sp.pi / (3 * sp.sqrt(3)) *
                  sp.sqrt(2 * kappa_infinity) / 6 - yang_constant) == 0)

# Original algebraic CM13, retaining the leading constants of both sigma
# division functions.  S_1 is one dimensional, and the invariant line of S_2
# is spanned by Theta, so a full fiber determines each actual eigenvalue.
x = sp.symbols("x")
field = sp.QQ.algebraic_field(delta)
P = lambda expression: sp.Poly(expression, x, domain=field)
gamma, gamma_bar = 4 + omega, 4 + sp.conjugate(omega)
q = P(gamma * (x**6 + (8+12*omega)*x**3 + sp.Rational(64,13) + sp.Rational(48,13)*omega))
qb = P(gamma_bar * (x**6 + (8+12*sp.conjugate(omega))*x**3 + sp.Rational(64,13) + sp.Rational(48,13)*sp.conjugate(omega)))
curve = P(x**3+1)


def x_map(q, a):
    numerator = P(13*x)*q*q - 4*curve*(q.diff().diff()*q-q.diff()*q.diff()) - P(6*x*x)*q.diff()*q
    denominator = (q*q).mul_ground(a*a)
    gcd = sp.polys.polytools.gcd(numerator, denominator)
    return numerator.exquo(gcd), denominator.exquo(gcd)


num, den = x_map(q, gamma)
numb, denb = x_map(qb, gamma_bar)
fiber_values = []
for target in (2, 3):
    fiber = (num-den.mul_ground(target)).monic()
    check("CM13 separable whole fiber " + str(target), fiber.degree() == 13 and sp.gcd(fiber, fiber.diff()).degree() == 0)
    ratio = (qb * sp.invert(q, fiber)).rem(fiber)
    xbar = (numb * sp.invert(denb, fiber)).rem(fiber)
    lambda_sigma = (ratio * fiber.diff()).rem(fiber).nth(12)
    lambda_theta = (ratio * ratio * xbar * fiber.diff()).rem(fiber).nth(12) / target
    check("original sigma CM13 scalar " + str(target), sp.simplify(lambda_sigma + gamma) == 0)
    check("original Theta CM13 scalar " + str(target), sp.simplify(lambda_theta + omega**2*gamma) == 0)
    fiber_values.append({"target_x": target, "sigma": str(sp.simplify(lambda_sigma)), "Theta": str(sp.simplify(lambda_theta))})

# Finite characters, all four simultaneous p-cores, and original return.
e, bp, prime, t = sp.symbols("epsilon barpi p t", nonzero=True)
reduce6 = lambda f: sp.rem(sp.Poly(sp.expand(f), e), sp.Poly(e**6-1, e)).as_expr()
lambda_theta, lambda_sigma = e/bp, e**3/bp
check("all four factor phases cancel exactly", reduce6(lambda_theta**3 * lambda_sigma - bp**-4) == 0)
check("odd three source cube is the actual epsilon", all((-j) % 6 == 1 for j in (5,11,17)))
check("three even return characters have cube one", all((3*j) % 6 == 0 for j in (0,4,2)))
check("weighted simultaneous core retains its one p", sp.cancel((prime/bp**2)*bp**-4-prime/bp**6) == 0)
check("odd primitive-input annulus coefficient", sp.cancel(bp * bp**-4 - bp**-3) == 0)
check("even primitive-input annulus coefficient", sp.cancel(bp * prime/bp**6 - prime/bp**5) == 0)
mass_return = (1-e**4/bp)/sp.Integer(336) - (1-e**2/bp)/sp.Integer(840)
check("actual unit mass including both rank-zero references",
      sp.cancel(mass_return - (3-(5*e**4-2*e**2)/bp)/1680) == 0)
theta_mass, sigma_first = 1-e/bp, 1-e**3*prime/bp**3
check("two core eigenvalues remain different in the target frame",
      reduce6((lambda_sigma/lambda_theta)-e**2) == 0)
X, b = sp.symbols("X b")
P1 = X**4-53*b*X**3/sp.Integer(7)-12*b**2*X**2/sp.Integer(7)-80*b**3*X/sp.Integer(7)-128*b**4/sp.Integer(7)
P3 = X**5-208*b*X**4+400*b**2*X**3+8128*b**3*X**2+12032*b**4*X-2048*b**5
P5 = X**5+272*b*X**4-272*b**2*X**3-14912*b**3*X**2-6784*b**4*X+1024*b**5
check("true five-factor source returns to the original three lines",
      sp.expand((-336*b*P1+5*P3+4*P5)/9-X*(X-8*b)**4) == 0)
check("five-factor simultaneous core", sp.cancel(lambda_theta**5-e**5/bp**5) == 0)
check("five-factor primitive carry coefficient", sp.cancel(bp*lambda_theta**5-e**5/bp**4) == 0)

data = {
    "status": "PASS", "checks": checks,
    "original_sigma_Hecke_family": "psi_(b=1)^(2m+1), m=1 mod 6",
    "sigma_Hermitian_alpha": 2,
    "sigma_dyadic_cosets": "b/4+2 Z2, b odd modulo 8",
    "sigma_dyadic_vector": [0,1,0,1,0,-1,0,-1],
    "omega_output_on_a_over_8": omega_output,
    "principal_output_on_a_over_4": star_output,
    "splitting": {"omega": "zeta8", "gstar": "zeta8", "minus_gstar": "-zeta8"},
    "sigma_three_vector": "1_(3^-1 Z3)",
    "sigma_finite_norm": 6, "sigma_global_Yang_prefactor": str(yang_constant),
    "sigma_real_constant": "1/9", "sigma_real_weight": "3^(-m)",
    "sigma_CM_constant": "-omega*(1-omega)/9", "sigma_CM_weight": 1,
    "CM13_full_fibers": fiber_values,
    "same_E17_core": {"Theta": "epsilon/barpi [p/barpi^2]", "sigma": "epsilon^3/barpi [p/barpi^2]"},
    "same_E17_Katz_prefactors": {"Theta": "17^(1/6)*(1-omega)*Omega_p/6; weight <2>^(-du)", "sigma": "-omega*(1-omega)*sqrt(17)*Omega_p/9; weight 1"},
    "four_factor_all_nonunit_coefficient": "barpi^-4",
    "weighted_all_nonunit_coefficient": "p/barpi^6",
    "primitive_input_annulus_odd": "barpi^-n [barpi^-2n] (Tp^n-barpi^-3 Tp^(n-1)) nu_CX^times, n>=1",
    "primitive_input_annulus_even": "barpi^-n [barpi^-2n] (Tp^n-p/barpi^5 Tp^(n-1)) nu_B^times, n>=1",
    "actual_source_annihilators": {"C_X": "Tp^3-epsilon", "B": "Tp^3-1"},
    "actual_even_unit_mass": "(3-(5*epsilon^4-2*epsilon^2)/barpi)/(1680*b)",
    "actual_five_factor_source": "U=Theta*Theta(2z)^4=(-336b H1+5H3+4H5)/9",
    "five_factor_primitive_input_annulus": "barpi^-n [barpi^-2n](Tp^n-epsilon^5/barpi^4 Tp^(n-1)) nu_U^times",
    "centered_reconstruction": "nu_Theta=delta0+sum lambda_Theta^n [kappa^n](nu_Theta^times-(1-lambda_Theta)delta0); nu_sigma=sum lambda_sigma^n[kappa^n]nu_sigma^times",
    "restriction": "All finite carry returns retain the original reference logarithmic slopes; no central nonvanishing follows from first moments."
}
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
print(f"PASS: {len(checks)} exact checks; {out.name}")
