#!/usr/bin/env python3
"""New short coefficients for the complete marked weight-ten double-Hecke block.

Run mathematical arithmetic only in this repository's public GitHub Actions.
The proof contract is notes/weight10-double-Hecke-packet.md.
This computes W[q^5], W[q^20], Z[q^15], and B2[q^25], together with
their conjugate-marking double-step identities. The two old R920 T5 input
rows are reused as constants; no supersingular trace or prime scan is run.

Elements [a,b] mean a+b*s in Z[s]/(s^2+3). All power-series coefficient
lists are in increasing degree. The final JSON is deterministic.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import pathlib


ZERO = (0, 0)
ONE = (1, 0)


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def neg(a):
    return (-a[0], -a[1])


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    return (a[0] * b[0] - 3 * a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def conjugate(a):
    return (a[0], -a[1])


def coefficient(a, n):
    return a[n] if 0 <= n < len(a) else ZERO


def series_mul(a, b, cutoff):
    out = [ZERO] * cutoff
    for i, x in enumerate(a[:cutoff]):
        if x == ZERO:
            continue
        for j, y in enumerate(b[: cutoff - i]):
            if y != ZERO:
                out[i + j] = add(out[i + j], mul(x, y))
    return out


def eta_product(step, exponent, shift, cutoff):
    out = [ONE] + [ZERO] * (cutoff - shift - 1)
    for n in range(1, (cutoff - shift - 1) // step + 1):
        degree = step * n
        factor = [ZERO] * (cutoff - shift)
        for j in range(min(exponent, (cutoff - shift - 1) // degree) + 1):
            factor[j * degree] = ((-1) ** j * math.comb(exponent, j), 0)
        out = series_mul(out, factor, cutoff - shift)
    return [ZERO] * shift + out


def divide_by_unit(numerator, denominator, cutoff):
    if denominator[0] != ONE:
        raise ArithmeticError("the original V4/q denominator is not normalized to one")
    quotient = [ZERO] * cutoff
    for n in range(cutoff):
        correction = ZERO
        for j in range(1, n + 1):
            correction = add(correction, mul(coefficient(denominator, j), quotient[n - j]))
        quotient[n] = sub(coefficient(numerator, n), correction)
    if series_mul(denominator, quotient, cutoff) != [
        coefficient(numerator, n) for n in range(cutoff)
    ]:
        raise ArithmeticError("the full formal quotient identity failed")
    return quotient


def dot(a, b):
    out = ZERO
    for x, y in zip(a, b):
        out = add(out, mul(x, y))
    return out


def calculate():
    cutoff = 26
    f4 = eta_product(3, 8, 1, cutoff)
    eta12 = eta_product(6, 12, 3, cutoff)
    v4 = list(f4)
    # -16*zeta^2 = 8(1+s), with the unchanged original zeta=(-1+s)/2.
    for n in range(1, (cutoff - 1) // 4 + 1):
        v4[4 * n] = add(v4[4 * n], mul((8, 8), f4[n]))
    e4 = [ZERO] * cutoff
    e4[0] = ONE
    for n in range(1, (cutoff - 1) // 6 + 1):
        sigma3 = sum(d**3 for d in range(1, n + 1) if n % d == 0)
        e4[6 * n] = (240 * sigma3, 0)

    # W=q^2 * E4^2*(eta12/q^3)/(V4/q); no pole or rational coefficient is hidden.
    quotient_cutoff = 19
    numerator = series_mul(series_mul(e4, e4, quotient_cutoff), eta12[3:], quotient_cutoff)
    denominator = v4[1:]
    w_over_q2 = divide_by_unit(numerator, denominator, quotient_cutoff)
    w = [ZERO, ZERO] + w_over_q2
    b2 = series_mul(v4, eta12, cutoff)
    z = series_mul(e4, eta12, cutoff)
    w5, w20 = coefficient(w, 5), coefficient(w, 20)
    b2_25, z15 = coefficient(b2, 25), coefficient(z, 15)

    # These are the already proved R920 input rows, not new computations.
    old_r920_row = [(0, -4032), (8, 0)]
    bar_b1_q4 = (0, -8)
    forward_w_column_in_bar_basis = [w5, sub(w20, mul(bar_b1_q4, w5))]
    reverse_wbar_column_in_original_basis = [conjugate(x) for x in forward_w_column_in_bar_basis]
    rho = dot(old_r920_row, reverse_wbar_column_in_original_basis)
    z_square = mul(z15, z15)
    block = [
        [mul(reverse_wbar_column_in_original_basis[i], old_r920_row[j]) for j in range(2)]
        for i in range(2)
    ]
    for i in range(2):
        for j in range(2):
            if dot(block[i], [block[k][j] for k in range(2)]) != mul(rho, block[i][j]):
                raise ArithmeticError("the exact rank-one double-step identity failed")
    cm_vector = [ONE, (0, 504)]
    if dot(old_r920_row, cm_vector) != ZERO:
        raise ArithmeticError("the unchanged original CM vector is not in the old row kernel")
    # The new phase diagnostic checks the conjugate target, not the rejected single-space arrow.
    if b2_25 != mul(old_r920_row[1], conjugate(w5)):
        raise ArithmeticError("the new q^25 phase diagnostic does not match the conjugate arrow")

    return {
        "contract": "weight10-double-Hecke-packet.md",
        "ring": "Z[s]/(s^2+3)",
        "original_phase": "zeta=(-1+s)/2; V4=F4-16*zeta^2*F4(q^4)",
        "space": "complete four-dimensional marked H6 weight-ten pullback",
        "not_the_entire_Gamma0_36_space": True,
        "single_T5_target": "conjugate marked H6 space",
        "double_T5_target": "original marked H6 space",
        "normalization": "5^(k/2-1) sum slash M_i; a_(5m)+5^(k-1)*a_(m/5)",
        "new_coefficients": {
            "W_q5": w5,
            "W_q20": w20,
            "Wbar_q5": conjugate(w5),
            "Wbar_q20": conjugate(w20),
            "B2_q25_phase_diagnostic": b2_25,
            "Z_q15": z15,
        },
        "reused_R920_T5_q2_row": old_r920_row,
        "T5_W_column_in_bar_B1_bar_B2": forward_w_column_in_bar_basis,
        "T5_Wbar_column_in_B1_B2": reverse_wbar_column_in_original_basis,
        "T5_squared_B_block_rows": block,
        "T5_squared_nonzero_scalar_on_B_image_and_W": rho,
        "T5_squared_scalar_on_Z": z_square,
        "rho_factorization": {"2": 14, "3": 2},
        "minus_Z_eigenvalue_factorization": {"2": 1, "3": 2, "37": 1},
        "cm_kernel_vector_in_B1_B2": cm_vector,
        "formal_quotient_identity_mod_q19_verified": True,
        "W_over_q2_coefficients_through_q18": w_over_q2,
        "V4_over_q_coefficients_used": denominator[:quotient_cutoff],
        "W_numerator_coefficients_used": numerator,
        "full_B2_series_through_q25": b2,
        "full_Z_series_through_q25": z,
        "high_weight_theta_saturation_proved": False,
        "all_prime_full_SS_trace_nonvanishing_proved": False,
        "Q_prime_source_comparison_proved": False,
        "execution_location_required": "Rogerhu12/math-research-public public GitHub Actions",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=pathlib.Path, required=True)
    args = parser.parse_args()
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise SystemExit("New arithmetic is permitted only in public repository Actions.")
    result = calculate()
    payload = (json.dumps(result, sort_keys=True, indent=2) + "\n").encode()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(payload)
    print(json.dumps(result["new_coefficients"], sort_keys=True))
    print(json.dumps({
        "T5_W_column_in_conjugate_basis": result["T5_W_column_in_bar_B1_bar_B2"],
        "rho": result["T5_squared_nonzero_scalar_on_B_image_and_W"],
        "Z_square": result["T5_squared_scalar_on_Z"],
        "output_bytes": len(payload),
        "sha256": hashlib.sha256(payload).hexdigest(),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
