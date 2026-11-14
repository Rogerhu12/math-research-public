#!/usr/bin/env python3
"""R311 finite normalization checks, not a q-Euler-product evaluator.

All arithmetic here is integer or finite-field arithmetic.  The membership
of the displayed radical in L is a theorem in the accompanying manuscript.
This program does NOT compute that radical, an upper-field determinant, or L.
"""

import argparse
import json
from pathlib import Path

P = 43
Q = int("225196170077769188459647075003723446506290334538374935594311805764766375462943717166814768844511612408106442292450018627544384538312646994045716899229168141998348680872046002490066651342968053955905931120521143569132718008762168959999")
ZETA = (
    int("33192256431478777534772693342490161012373414464785401361122186710744426145385242337610237454110224901337816657644112419076529202192170583323034154623583921171355558078026293450555526527706963402223792490590954972636538127057395769163"),
    int("171023583398532679386711239941267784062765623696689858645290077011642199651646324646676955701988625242095153878295365334133068324314695282660741691934130921957519553782994262401615031914521307989634726996409007549972082490092007345950"),
)
OMEGA = (8, 25)
WEIGHTS = [15,-9,13,2,19,1,-3,-6,-7,-20,-12,0,12,20,7,6,3,-1,-19,-2,-13,9,-15,9,-13,-2,-19,-1,3,6,7,20,12,0,-12,-20,-7,-6,-3,1,19,2,13,-9]


def add(x, y, ell):
    return ((x[0] + y[0]) % ell, (x[1] + y[1]) % ell)


def mul(x, y, ell):
    return ((x[0]*y[0] - x[1]*y[1]) % ell,
            (x[0]*y[1] + x[1]*y[0]) % ell)


def power(x, exponent, ell):
    result = (1, 0)
    while exponent:
        if exponent & 1:
            result = mul(result, x, ell)
        x = mul(x, x, ell)
        exponent >>= 1
    return result


def build_certificate():
    assert Q % (4*P) == 4*P-1
    m = (Q*Q-1)//P
    assert P*m == Q*Q-1
    assert m % P == 21
    assert (Q+1)//P % P == 11
    assert power(ZETA, P, Q) == (1, 0) and ZETA != (1, 0)
    assert power(ZETA, Q, Q) == power(ZETA, P-1, Q)
    b = power(ZETA, 41, Q)
    assert (21*41) % P == 1
    assert power(b, m, Q) == ZETA
    assert power(b, P, Q) == (1, 0) and b != (1, 0)
    assert power(b, Q, Q) == power(b, P-1, Q)

    assert power(OMEGA, 44, P) == (1, 0)
    assert all(power(OMEGA, d, P) != (1, 0) for d in (1,2,4,11,22))
    assert power(OMEGA, 11, P) == (0, 1)
    powers = [power(OMEGA, j, P) for j in range(44)]
    recomputed = [((15*x[0]+21) % P)-21 for x in powers]
    assert recomputed == WEIGHTS
    assert sum(WEIGHTS) == 0
    assert all(WEIGHTS[-j % 44] == WEIGHTS[j] for j in range(44))
    assert all(WEIGHTS[(j+22) % 44] == -WEIGHTS[j] for j in range(44))
    spectra = []
    for k in range(44):
        value = (0, 0)
        for j in range(44):
            value = add(value, mul((WEIGHTS[j] % P, 0), powers[k*j % 44], P), P)
        spectra.append(list(value))
    assert spectra[1] == spectra[43] == [29,0]
    assert all(spectra[k] == [0,0] for k in range(44) if k not in (1,43))

    derivative = [j if j <= 21 else j-P for j in range(P)]
    assert sum(derivative) == 0
    assert all(derivative[-j % P] == -derivative[j] for j in range(P))
    assert all((derivative[j]-j) % P == 0 for j in range(P))
    difference = [derivative[(j-1) % P]-derivative[j] for j in range(P)]
    assert difference == [-1 if j != 22 else 42 for j in range(P)]

    coefficient_plus = mul((0,32), (0,15), P)
    coefficient_minus = mul((0,-32), (0,-15), P)
    assert coefficient_plus == coefficient_minus == (36,0)
    assert (36+7) % P == 0
    assert 7*37 - P*6 == 1

    return {
        "result": "R311",
        "status": "finite normalization checks only; exact radical membership proved in manuscript",
        "p": P,
        "q": str(Q),
        "q_bits": Q.bit_length(),
        "q_congruence_mod_4p": Q % (4*P),
        "m_q": str(m),
        "m_q_mod_43": m % P,
        "q_ray_robert_product_factor_count": str(42*m),
        "q_ray_robert_product_factor_count_bits": (42*m).bit_length(),
        "fixed_weil_root": [str(x) for x in ZETA],
        "q_CM_gamma_scalar": [str(x) for x in b],
        "q_CM_gamma_scalar_expression": "zeta_Weil^41",
        "q_CM_gamma_scalar_power_m_equals_fixed_weil_root": True,
        "q_CM_gamma_scalar_order": 43,
        "omega": list(OMEGA),
        "ordinary_projection_weights": WEIGHTS,
        "projection_spectra": spectra,
        "centered_derivative_weights": derivative,
        "gamma_minus_one_derivative": difference,
        "normalized_raw_derivative_coefficient": 36,
        "radicand_base_U_exponent": 7,
        "radical_norm_U_exponent": 7,
        "final_X_radical_exponent": 37,
        "final_X_denominator_U_exponent": 6,
        "7_times_37_minus_43_times_6": 1,
        "q_robert_product_evaluated": False,
        "upper_norm_preimage_coordinates_computed": False,
        "R305_norm_determinant_of_X_computed": False,
        "q_residue_phases_computed": False,
        "actual_L_computed": False,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path)
    parser.add_argument("--write", type=Path)
    args = parser.parse_args()
    data = build_certificate()
    if args.certificate:
        assert json.loads(args.certificate.read_text()) == data
    if args.write:
        args.write.write_text(json.dumps(data, indent=2, ensure_ascii=False)+"\n")
    print("PASS: fixed q/Weil tame generator; all 44 projection modes; centered derivative; 36=-7; 7*37-43*6=1")
    print("NOT EVALUATED: q-Robert product, upper X coordinates, Norm determinant, q phases, canonical L")


if __name__ == "__main__":
    main()
