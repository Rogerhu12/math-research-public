#!/usr/bin/env python3
"""Independent original-Lagrange check of two new central sigma zeros.

Public Actions only. Fixed targets:
  p=227: f_18, g_18, new q_2 factor f_17, and adaptive f_24, g_12 at h=151.
  p=857: f_71, g_70, new q_2 factors f_69, g_71, and P_444=P_412 at h=445.
The already computed p=857 h=445 sigma pair is reused, not recalculated.
No other prime, full trace, upper-end coefficient, or earlier window is run.

R698's ORIGINAL u=x^(-1/2), w=u^6 give dz=C du, z=uZ,
sigma^6=u^6 T, F=u^4 T and G=uT/C. Residue change of variable gives
f_i=[w^i] T C Z^(-(6i+5)), g_j=[w^j] T Z^(-(6j+2)).
This does not solve the original-z energy equation or import that consumer.
"""

import argparse
from hashlib import sha256
import json
from math import comb
import os
from pathlib import Path


CENTRAL_SOURCE = {
    "run": "44719847377",
    "job": "136232493369",
    "source_commit": "1f394d300f92824f3bb1253af1f44ca7c1652501",
    "output_sha256": "32f320938f5e5f43541e7c7e7c93967ad26faab63fab21d22fc4cc6d91a03023",
}
THIRD_LEGENDRE_SOURCE = {
    "run": "44718206366",
    "job": "136226900472",
    "source_commit": "cfa323577937abf5f80652bacab6bd81971db2d6",
    "output_sha256": "f4e7416026c5cf358f6b473185cabf1d105998e8db2e79f2c457cecb7996400a",
    "scope": "all 203 allowed selected-third factors through 10000 are nonzero",
}


def canonical_sha(value):
    return sha256(json.dumps(value, sort_keys=True,
                             separators=(",", ":")).encode()).hexdigest()


def multiply(left, right, degree, p):
    result = [0] * (degree+1)
    for i, a in enumerate(left[:degree+1]):
        for j, b in enumerate(right[:degree-i+1]):
            result[i+j] = (result[i+j] + a*b) % p
    return result


def inverse_unit(series, degree, p):
    inverse_constant = pow(series[0], -1, p)
    inverse = [inverse_constant]
    for n in range(1, degree+1):
        inverse.append(-inverse_constant
                       * sum(series[j]*inverse[n-j] for j in range(1, n+1)) % p)
    return inverse


def integer_power(series, exponent, degree, p):
    if exponent < 0:
        series = inverse_unit(series, degree, p)
        exponent = -exponent
    result = [1] + [0]*degree
    while exponent:
        if exponent & 1:
            result = multiply(result, series, degree, p)
        series = multiply(series, series, degree, p)
        exponent //= 2
    return result


def original_algebraic_series(p, degree):
    # Work entirely inside the proven R698 integral cutoff, not an infinite reduction.
    assert 0 <= degree <= (p-5)//6
    assert 6*degree+1 < p
    c, h = [1], [1]
    for n in range(1, degree+1):
        c.append(c[-1]*(2*n-1)*pow(2*n, -1, p) % p)
        h.append(h[-1]*(6*n-4)*pow(6*n-1, -1, p) % p)
    z = [c[n]*pow(6*n+1, -1, p) % p for n in range(degree+1)]
    t = [1]
    for n in range(1, degree+1):
        t.append(sum(h[j]*t[n-j] for j in range(1, n+1))*pow(n, -1, p) % p)

    # Independent identities in the original algebraic parameter.
    w_zeta = [1] + [-c[n]*pow(6*n-1, -1, p) % p for n in range(1, degree+1)]
    assert multiply(c, w_zeta, degree, p) == h
    c_squared = multiply(c, c, degree, p)
    assert [(c_squared[n] - (c_squared[n-1] if n else 0)) % p
            for n in range(degree+1)] == [1]+[0]*degree
    assert [(6*n+1)*z[n] % p for n in range(degree+1)] == c
    assert all((n*t[n] - sum(h[j]*t[n-j] for j in range(1, n+1))) % p == 0
               for n in range(1, degree+1))
    return c, z, h, t


def one_sigma_coefficient(kind, index, p, c, z, t, expected=None):
    exponent = -(6*index + (5 if kind == "f" else 2))
    z_power = integer_power(z[:index+1], exponent, index, p)
    # Check the full differential equation Z S'=exponent Z' S independently
    # of the unit inversion and binary multiplication used to construct S.
    for n in range(1, index+1):
        residual = sum(((n-k)-exponent*k)*z[k]*z_power[n-k]
                       for k in range(n+1))
        assert residual % p == 0
    base = multiply(t, c, index, p) if kind == "f" else t[:index+1]
    summands = [base[k]*z_power[index-k] % p for k in range(index+1)]
    value = sum(summands) % p
    return {
        "kind": kind,
        "index": index,
        "z_power_exponent": exponent,
        "value": value,
        "central_previous_value": expected,
        "central_reproduction_matches": None if expected is None else value == expected,
        "finite_summands": summands,
        "finite_summands_integer_sum": sum(summands),
        "finite_summands_sha256": canonical_sha(summands),
        "z_power_sha256": canonical_sha(z_power),
        "full_z_power_differential_equation_verified": True,
    }


def sigma_case(p, targets):
    degree = max(index for _, index, _ in targets)
    c, z, h, t = original_algebraic_series(p, degree)
    rows = [one_sigma_coefficient(kind, index, p, c, z, t, expected)
            for kind, index, expected in targets]
    values = {(row["kind"], row["index"]): row["value"] for row in rows}
    return {
        "p": p,
        "computed_degree": degree,
        "R698_integral_cutoff": (p-5)//6,
        "series_sha256": canonical_sha({"C": c, "Z": z, "H": h, "T": t}),
        "H_equals_CW_verified": True,
        "C_squared_times_one_minus_w_verified": True,
        "Z_plus_6wZprime_equals_C_verified": True,
        "wTprime_equals_T_Hminus1_verified": True,
        "coefficients": rows,
    }, values


def new_legendre_at_857():
    p, h = 857, 445
    raw_degree = h-1
    degree = p-1-raw_degree
    assert raw_degree == 444 and degree == 412 and degree % 2 == 0
    x_squared = -pow(3, -1, p) % p
    # Exact finite polynomial formula, independent of the recurrence window.
    summands = [((-1)**j * comb(degree, j) * comb(2*degree-2*j, degree)
                 * pow(x_squared, degree//2-j, p)) % p
                for j in range(degree//2+1)]
    prefactor = pow(pow(2, degree, p), -1, p)
    value = prefactor*sum(summands) % p
    old_sigma_product = 187
    return {
        "p": p,
        "h": h,
        "original_degree": raw_degree,
        "reflected_degree": degree,
        "value": value,
        "prefactor_2_to_minus_degree": prefactor,
        "finite_summands_before_prefactor": summands,
        "finite_summands_integer_sum": sum(summands),
        "finite_summands_sha256": canonical_sha(summands),
        "already_proved_sigma_product": old_sigma_product,
        "sigma_pair_recomputed": False,
        "sigma_source": CENTRAL_SOURCE,
        "same_label_critical_product": value*old_sigma_product % p,
        "same_label_rescue_nonzero": value != 0 and old_sigma_product != 0,
        "zero_is_a_valid_new_result": True,
    }


def verify_targets():
    row227, values227 = sigma_case(227, [("f", 18, 0), ("g", 18, 136),
                                        ("f", 17, None),
                                        ("f", 24, None), ("g", 12, None)])
    row857, values857 = sigma_case(857, [("f", 71, 176), ("g", 70, 0),
                                        ("f", 69, None), ("g", 71, None)])
    new_sigma_product227 = values227[("f", 24)]*values227[("g", 12)] % 227
    adaptive227 = {
        "p": 227,
        "h": 151,
        "f_index": 24,
        "g_index": 12,
        "f_value": values227[("f", 24)],
        "g_value": values227[("g", 12)],
        "sigma_product": new_sigma_product227,
        "already_proved_legendre_nonzero": True,
        "legendre_recomputed": False,
        "legendre_source": THIRD_LEGENDRE_SOURCE,
        "same_label_rescue_nonzero": new_sigma_product227 != 0,
        "zero_is_a_valid_new_result": True,
    }
    central_reproduced = all(
        coefficient["central_reproduction_matches"] is not False
        for row in (row227, row857) for coefficient in row["coefficients"])
    return {
        "schema": "original-central-two-zeros-lagrange-v1",
        "arithmetic": "exact finite prime fields; stdlib integers only",
        "curve": "y^2=x^3-1",
        "differential": "dz=dx/(2y); x'=2y",
        "sigma_normalization": "c=0; sigma=z+O(z^7); (log sigma)''=-x",
        "f_formula": "f_i=[w^i] T C Z^(-(6i+5))",
        "g_formula": "g_j=[w^j] T Z^(-(6j+2))",
        "central_source": CENTRAL_SOURCE,
        "fixed_sigma_cases": [row227, row857],
        "all_four_central_values_reproduced": central_reproduced,
        "central_products": [
            {"p": 227, "h": 115,
             "product": values227[("f", 18)]*values227[("g", 18)] % 227},
            {"p": 857, "h": 433,
             "product": values857[("f", 71)]*values857[("g", 70)] % 857},
        ],
        "new_second_normal_coefficient_products": [
            {"p": 227, "h": 115, "normal_coefficient_index": 2,
             "f_index": 17, "g_index": 18,
             "product": values227[("f", 17)]*values227[("g", 18)] % 227,
             "same_label_equivalence_source": "R925(925.11-12); j=2, m=5",
             "zero_is_a_valid_new_result": True},
            {"p": 857, "h": 433, "normal_coefficient_index": 2,
             "f_index": 69, "g_index": 71,
             "product": values857[("f", 69)]*values857[("g", 71)] % 857,
             "same_label_equivalence_source": "R925(925.11-12); j=2, m=5",
             "zero_is_a_valid_new_result": True},
        ],
        "new_adaptive_sigma_at_227": adaptive227,
        "new_adaptive_legendre_at_857": new_legendre_at_857(),
        "full_trace_recomputed": False,
        "old_48_prime_window_repeated": False,
        "old_upper_end_coefficients_recomputed": False,
        "all_prime_nonvanishing_claimed": False,
        "source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path("/tmp/central-sigma-two-zeros-lagrange.json"))
    args = parser.parse_args()
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise SystemExit("New arithmetic is permitted only in public repository Actions.")
    report = verify_targets()
    encoded = (json.dumps(report, sort_keys=True, indent=2)+"\n").encode()
    args.output.write_bytes(encoded)
    print(json.dumps(report, sort_keys=True), flush=True)
    print("OUTPUT_SHA256="+sha256(encoded).hexdigest(), flush=True)
    if not report["all_four_central_values_reproduced"]:
        raise SystemExit("A central coefficient disagrees with the original-z source.")


if __name__ == "__main__":
    main()
