"""Exact symbolic certificate for R272; no target-prime enumeration."""
import json
from pathlib import Path
import sympy as s

q, p, j, m = s.symbols("q p j m")
r = (p + 1) / 4
checks = {}
data = {}


def zero(name, value):
    value = s.factor(value)
    assert value == 0, (name, value)
    checks[name] = True


v0, v1, v2 = s.symbols("V Vprime Vsecond")
original = (
    q * (4 - q) * (v2 + 2 * r * v1 / q + r * (r - 1) * v0 / q**2)
    + 3 * (1 - q / 2) * (v1 + r * v0 / q)
)
claimed = (
    q * (4 - q) * v2 + (5 - 2 * q) * v1 - s.Rational(3, 16) * v0
    + p * ((2 - q / 2) * v1 + r * v0 / q - (p + 4) * v0 / 16)
)
for var in (v0, v1, v2):
    zero("exact_conjugacy_" + str(var), s.expand(original - claimed).coeff(var))

ratio = (4 * j + 3) * (4 * j + 1) / (16 * (j + 1) * (4 * j + 5))
n = r + j
force = (n * (n + s.Rational(1, 2)) - (n + 1) * (4 * n + 3) * ratio) / p
expected = (80 * j**2 + 20 * j * p + 136 * j + 17 * p + 53) / (
    64 * (j + 1) * (4 * j + 5)
)
zero("all_interior_forcing_coefficients", force - expected)
zero("last_forcing_coefficient", (2 * r - 1) * (2 * r - s.Rational(1, 2)) / p - (2 * r - 1) / 2)
zero("homogeneous_inner_recurrence", (j + 1) * (4 * j + 5) * ratio - j * (j + 1) - s.Rational(3, 16))
zero("homogeneous_last_coefficient_is_p_multiple", -(r * (r - 1) + s.Rational(3, 16)) + p * (p - 2) / 16)
data["forcing_interior_over_a0_hj"] = str(s.factor(force))
data["forcing_endpoint_over_a0_hlast"] = str(s.factor((2 * r - 1) / 2))

alpha = (
    s.Rational(1, 5) * (1 - q / 2) * (1 - q / 4) *
    (1 + q - q**2 / 4) * ((1 - q / 2)**4 + 4)
)
assert s.degree(alpha, q) == 8
checks["actual_carrier_degree_eight"] = True
zero("carrier_constant_one", alpha.subs(q, 0) - 1)
zero("carrier_zero_at_four", alpha.subs(q, 4))
zero("carrier_derivative_at_four", s.diff(alpha, q).subs(q, 4) - s.Rational(1, 4))
zero("carrier_log_linear_coefficient", s.diff(alpha, q).subs(q, 0) + s.Rational(3, 20))
ap = s.diff(alpha, q)
app = s.diff(alpha, q, 2)
logforcing = s.cancel(q * (4 - q) * (app * alpha - ap**2) / alpha**2 + 3 * (1 - q / 2) * ap / alpha)
zero("full_fixed_pole_residue", s.limit((q - 4) * logforcing, q, 4) - 1)
numerator = s.cancel(alpha**2 * logforcing)
assert s.denom(numerator).is_number and s.degree(numerator, q) <= 16
checks["full_fixed_pole_numerator_degree"] = True
data["actual_carrier"] = str(s.factor(alpha))
data["carrier_forcing"] = str(s.factor(logforcing))

rr, av, aq, aqq, h, l1, l2 = s.symbols("r A Aprime Asecond h Lprime Lsecond")
D = rr * av + q * aq
Dp = (rr + 1) * aq + q * aqq
D2 = q**2 * aqq + 2 * rr * q * aq + rr * (rr - 1) * av
zero("second_hensel_derivative", D2 - q * Dp - (rr - 1) * D)
k = -D2 * h**2 / (2 * D)
zero("hensel_second_order", D * k + D2 * h**2 / 2)
B = 1 + q * l1
Bp = l1 + q * l2
K = j + m * B
direct_first = h * (j + m + m * q * l1)
direct_second = (
    k * K + h**2 / 2 * (
        (j + m) * (j + m - 1) +
        2 * (j + m) * m * q * l1 + m * q**2 * l2 +
        m**2 * q**2 * l1**2
    )
)
operator_second = h**2 / 2 * (K**2 + m * q * Bp - (rr + q * Dp / D) * K)
zero("general_monomial_first_order", direct_first - h * K)
zero("general_monomial_second_order", direct_second - operator_second)

UU, Up, DD, Dprime = s.symbols("U Uprime D Dprime")
hh = UU / DD
hprime = Up / DD - UU * Dprime / DD**2
forward_E2 = hh**2 / 2
forward_E1 = -hh**2 / 2 * (rr + q * Dprime / DD)
inverse_E2 = hh**2 / 2
inverse_E1 = q * UU * Up / DD**2 + hh**2 / 2 * (rr - q * Dprime / DD)
zero("inverse_second_derivative_coefficient", forward_E2 + inverse_E2 - hh**2)
zero("inverse_first_derivative_coefficient", forward_E1 + inverse_E1 - hh * q * hprime)
zero("inverse_has_no_division_by_U", inverse_E1 - (hh * q * hprime + hh**2 / 2 * (rr + q * Dprime / DD)))
data["source_second_order"] = "h^2/2 * (E^2 - (r+q D'/D) E)"
data["inverse_first_derivative_second_order"] = str(inverse_E1)

result = {
    "result": "R272",
    "method": "symbolic rational identities in free parameters; no target-prime samples",
    "check_count": len(checks),
    "all_passed": all(checks.values()),
    "checks": checks,
    "exact_data": data,
}
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"result": "R272", "check_count": len(checks), "all_passed": True}))
