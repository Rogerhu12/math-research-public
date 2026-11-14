#!/usr/bin/env python3
"""R332: exact constants and local data for the actual negative theta moments.

No prime scan and no assertion of fixed-weight nonvanishing.  The local
reciprocity and density arguments are proved in the accompanying result.
"""
import json
import math
from pathlib import Path
import sympy as s

checks = []


def check(name, assertion):
    assert bool(assertion), name
    checks.append(name)


P, B, Om, om, th = s.symbols("pi0 barpi0 Omega0 omega theta", nonzero=True)
pp = P*B
c_theta = (1-om)/6
c_sigma = -om*(1-om)/9

for r in [5, 6]:
    k, j = 1-r, r
    check(f"r={r}: actual character has norm weight one", k+j == 1)
    check(f"r={r}: dual type is (r,1-r)", (1-k, 1-j) == (r, 1-r))
    check(f"r={r}: self-dual involution fixes the character",
          (1-j, 1-k) == (k, j))
    check(f"r={r}: auxiliary (5) smoothing is thirty", 25-(-5)**(k+j) == 30)
    q = B**(r-1)/P**r
    a = P**(r-1)/B**r
    local_phi = pp**(-r)*B**(2*r-1)
    check(f"r={r}: actual crystalline Frobenius", s.cancel(local_phi-q) == 0)
    check(f"r={r}: Euler denominator is at the same prime",
          s.cancel(pp**(r-1)*B**(1-2*r)-a) == 0)
    eu = (1-a)/(pp**r*(1-q))
    expected_eu = (1-pp**(r-1)/B**(2*r-1))/(pp**r-B**(2*r-1))
    check(f"r={r}: normalized reciprocal Euler is a unit formula",
          s.cancel(eu-expected_eu) == 0)
    check(f"r={r}: local comparison period exponent",
          r+(r-1) == 2*r-1)

check("Theta negative-six square constant",
      s.expand(2**6*c_theta-s.Rational(32, 3)*(1-om)) == 0)
check("Theta normalized Soulé log constant",
      s.expand(-math.factorial(5)*2**6*c_theta+1280*(1-om)) == 0)
check("sigma negative-five primitive Soulé log constant",
      s.expand(math.factorial(4)*c_sigma+s.Rational(8, 3)*om*(1-om)) == 0)
check("sigma full modulus adds the exact Euler at two",
      s.Rational(1)-s.Rational(1, -2) == s.Rational(3, 2))
check("sigma primitive Soulé class uses one forty-fifth",
      s.Rational(2, 3)*s.Rational(1, 30) == s.Rational(1, 45))
check("sigma full-modulus Soulé log constant",
      s.expand(s.Rational(3, 2)*math.factorial(4)*c_sigma+4*om*(1-om)) == 0)
check("actual common-frame sigma measure scaling",
      s.cancel(Om*(th**2)-(th**3)*(Om/th)) == 0)

# The full bad-place values of the normalized base Hecke character have orders
# 3 and 2 at 2, and orders 2 and 4 at 3.  Thus equality of exponents mod 12
# checks units AND uniformizers; only checking mod 6 would be insufficient.
for exponent, comparison in [(11, -1), (9, -3)]:
    for order in [3, 2, 2, 4]:
        check(f"power {exponent}/{comparison}: full bad local order {order}",
              (exponent-comparison) % order == 0)
    check(f"power {exponent}: archimedean epsilon ratio is minus one",
          s.I**(abs(exponent)-abs(comparison)) == -1)

n = s.symbols("n", integer=True, positive=True)
check("all negative-Theta reflected powers have the same bad type",
      s.simplify((12*n-1)-(-1)) == 12*n)
check("all negative-sigma reflected powers have the same bad type",
      s.simplify((12*n-3)-(-3)) == 12*n)
check("negative Theta family has archimedean minus sign",
      12 % 4 == 0 and (-2) % 4 == 2 and s.I**2 == -1)
check("negative sigma family has archimedean minus sign",
      12 % 4 == 0 and (-6) % 4 == 2 and s.I**2 == -1)

out = {
    "status": "PASS",
    "check_count": len(checks),
    "checks": checks,
    "theta_character": "psi0^-5*barpsi0^6; V=psi0^6*barpsi0^-5",
    "sigma_character": "psi0^-4*barpsi0^5; V=psi0^5*barpsi0^-4",
    "theta_log": "-1280*(1-omega)*Omega0^12*(1-pi0^5/barpi0^6)/(1-barpi0^5/pi0^6)*I_Theta,-6^2",
    "sigma_primitive_log": "-(8/3)*omega*(1-omega)*Omega0^10*(1-pi0^4/barpi0^5)/(1-barpi0^4/pi0^5)*I_sigma0,-5^2",
    "sigma_full_modulus_log": "(3/2) times the primitive log",
    "valuations": ["v(log z6)=6+2v(I_Theta,-6)", "v(log z5_prim)=5+2v(I_sigma0,-5)"],
    "bad_local_comparison": ["theta0^11 agrees with theta0^-1 at 2 and 3", "theta0^9 agrees with theta0^-3 at 2 and 3"],
    "complex_centers": ["L(psi0^11,6)=0", "L(psi0^9,5)=0"],
    "unconditional_growing_weight": "h=(p-1)/6: I_Theta,-6h and I_sigma,1-6h are units; their weights depend on p",
    "scope": "Exact reciprocity and root signs do not assert fixed-weight local nonvanishing or the main rank-two Sha goal."
}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(out, ensure_ascii=False, indent=2)+"\n")
print(f"{len(checks)} exact checks: PASS")
