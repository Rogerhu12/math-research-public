#!/usr/bin/env python3
"""R119 exact finite gates for the actual R69 terminal connector group.

Standard-library rational/polynomial verification only.  This verifies the
finite constants in the accompanying proof, not an independent numerical
solution of the full PDE or a regular-port graph inverse.
"""
from fractions import Fraction as Q
from hashlib import sha256
from math import factorial
from pathlib import Path
import argparse
import json


def pow2(n):
    return Q(2**n) if n >= 0 else Q(1, 2**(-n))


def run():
    checks = []

    def gate(name, condition, **values):
        checks.append(dict(name=name, pass_=bool(condition),
                           **{k: str(v) for k, v in values.items()}))
        if not condition:
            raise ArithmeticError(name)

    n = Q(1, 64)
    eta = pow2(-24)
    tau = Q(5177, 400)
    d = Q(9, 400)
    den = 1 - 2*n
    log_bound = Q(1, 8) - Q(1, 128) + Q(1, 1536)
    gate('actual_final_group_length_below_one_eighth', log_bound+2*eta < Q(1, 8),
         upper=log_bound+2*eta)
    e_upper = sum((Q(1, factorial(k)) for k in range(9)), Q(0))
    e_upper += Q(1, factorial(9)) / (1-Q(1, 10))
    gate('elementary_e_upper', e_upper < Q(11, 4), upper=e_upper)
    gate('reaction_growth_below_64', Q(11, 4)**4 < 64)
    gate('reference_radius_below_3', 2/(1-Q(1, 8)) < 3)
    gate('slope_ratio_below_3', Q(11, 4) < 3)
    gate('source_absolute_width_is_original', tau == Q(5177, 400))
    sigma0 = tau-d/4
    sigma1_lower = sigma0-2
    sigma2_lower = sigma1_lower-Q(1, 4)
    sigma_out, sigma_g = tau-3, tau-4
    gate('raw_trace_has_half_width_spare', sigma2_lower-sigma_out > Q(1, 2),
         spare=sigma2_lower-sigma_out)
    gate('ground_trace_has_half_width_spare', sigma1_lower-sigma_g > Q(1, 2))
    gate('no_ungranted_angular_width', 0 < sigma_g < sigma_out < sigma0 < tau)
    gate('physical_body_window_is_smaller', Q(1, 512) < sigma_g)
    gate('F_majorant', (14+9*n)/den < 15, upper=(14+9*n)/den)
    gate('F_P_majorant_per_state', 18/den < 19)
    gate('F_K_includes_denominator_derivative', (14+14*n+15*n)/den < 15)
    gate('F_U_includes_denominator_derivative', (7*(1+n)+30*n)/den < 8)
    gate('F_V_majorant_per_state', 4/den < 5)
    gate('reaction_column_P', 21 < 32)
    gate('reaction_column_K', 15 < 32)
    gate('reaction_column_U', 21+19*n < 32)
    gate('reaction_column_V', 31 < 32)
    gate('principal_V_derivative', 1+5*n < 8)
    gate('chosen_angular_speed_has_margin', 8 < 16)
    gate('quadratic_remainder_coefficient', 16/den < 32)
    gate('source_plus_angular_derivative', 32*(1+2) < 2**7)
    gate('actual_tail_relative_scale_exponent', 7-Q(131*15, 4) < -484)
    gate('input_relative_five_norm', 96*Q(800, 9) < 2**14)
    gate('mean_included_in_four_norm', 2+12*n < 3)
    gate('full_initial_four_norm', 3*2**14 < 2**16)
    gate('whole_label_state_below_one', Q(13, 4)*Q(1, 4) < 1)
    gate('propagated_relative_ball', pow2(22)*pow2(-484) <= pow2(-462))
    gate('propagated_ball_closes', pow2(-462) < n)
    gate('initial_mean_quadratic_fee', 12*2**28 < 2**32)
    gate('duhamel_quadratic_fee', 64*Q(1, 8)*2**7*2**44 == 2**54)
    gate('initial_mean_plus_forcing_fee', 2**38+2**54 < 2**55)
    gate('complete_relative_quadratic_remainder',
         pow2(22)*pow2(-60)+pow2(55)*pow2(-484) < pow2(-37))
    gate('height_trace_quadratic_remainder',
         pow2(-60)+Q(9, 8)*pow2(-37) < pow2(-35))
    gate('radial_trace_quadratic_remainder', 3*pow2(-37) < pow2(-35))
    gate('height_trace_linear_bound', 1+Q(9, 8)*2**22 < 2**24)
    gate('radial_trace_linear_bound', 3*2**22 < 2**24)
    gate('fourth_angular_derivative_half_gap', (Q(4)/(2*Q(1, 2)))**4 == 2**8)
    gate('second_angular_derivative_half_gap', (Q(2)/(2*Q(1, 2)))**2 == 4)
    gate('complete_raw_trace_remainder', (256+5+2)*pow2(-35) < pow2(-26))
    gate('label_quadratic_trace_remainder', Q(13, 4)**2*pow2(-26) < pow2(-22))
    gate('complete_raw_trace_bound', (256+5+2)*2**24*Q(13, 4) < 2**35)
    gate('first_label_derivative_remainder', 4*pow2(-22) == pow2(-20))
    gate('second_label_derivative_remainder', 24**2*Q(1, 6)**2 == 16)
    gate('second_label_derivative_fee', 16*pow2(-22) == pow2(-18))
    gate('eighth_angular_weight', 17**8 < 2**40)
    gate('grounded_background_relative_jets', 3*2**40*pow2(-462) < pow2(-420))
    gate('grounded_input_label_derivative_jets', 2*6*2**24*2**40 < 2**68)
    gate('grounded_small_geometric_ratio', Q(9)*Q(20, 17) < 16)
    gate('grounded_geometric_ratio_exponent', 4-131*6 == -782)
    gate('grounded_complete_trace_fee',
         pow2(32)*(pow2(-420)+pow2(-782))*pow2(68) < pow2(-310))
    gate('reference_second_jet_fee', 22*3*2**22 < 2**30)
    gate('physical_scaling_exponent', Q(56+440+2)-Q(131*39, 4) < -778)
    gate('support_after_translation_and_correction',
         Q(19, 20)-Q(1, 20)-pow2(-778)/4 > Q(17, 20))

    # Exact sparse polynomials in (A,K,U,V,P,z), where z=w^2.
    nv = 6
    zero = (0,)*nv

    def c(a):
        return {} if a == 0 else {zero: Q(a)}

    def var(i):
        p = [0]*nv
        p[i] = 1
        return {tuple(p): Q(1)}

    def add(a, b):
        out = dict(a)
        for k, v in b.items():
            out[k] = out.get(k, Q(0))+v
            if not out[k]:
                del out[k]
        return out

    def neg(a):
        return {k: -v for k, v in a.items()}

    def sub(a, b):
        return add(a, neg(b))

    def mul(a, b):
        out = {}
        for ka, va in a.items():
            for kb, vb in b.items():
                k = tuple(x+y for x, y in zip(ka, kb))
                out[k] = out.get(k, Q(0))+va*vb
                if not out[k]:
                    del out[k]
        return out

    def scale(a, s):
        return mul(a, c(s))

    def power(a, n):
        out = c(1)
        for _ in range(n):
            out = mul(out, a)
        return out

    A, K, U, V, P, z = [var(i) for i in range(nv)]
    E = add(c(1), z)
    B = add(add(c(1), K), mul(E, U))
    square = power(sub(V, P), 2)
    old = add(neg(mul(A, add(K, U))), mul(E, square))
    old = add(old, mul(mul(A, z), sub(mul(K, U), power(P, 2))))
    old = sub(old, mul(mul(A, K), B))
    linear = add(scale(K, 2), U)
    inside = add(add(add(linear, power(K, 2)), mul(K, U)), mul(z, power(P, 2)))
    numerator = add(neg(mul(A, inside)), mul(E, square))
    gate('physical_to_relative_PDE_identity', old == numerator)
    rem = add(numerator, mul(mul(A, linear), B))
    rem_inside = sub(add(add(power(K, 2), scale(mul(mul(E, K), U), 2)),
                         mul(E, power(U, 2))), mul(z, power(P, 2)))
    expected_rem = add(mul(E, square), mul(A, rem_inside))
    gate('complete_quadratic_residual_identity', rem == expected_rem)
    compat = add(mul(add(c(1), A), P), sub(V, mul(add(A, c(1)), P)))
    gate('height_compatibility_including_slope_derivative', compat == V)
    x = var(0)
    def smoothstep(a):
        return add(sub(scale(power(a, 3), 10), scale(power(a, 4), 15)),
                   scale(power(a, 5), 6))
    gate('actual_quintic_reversal',
         add(smoothstep(x), smoothstep(sub(c(1), x))) == c(1))

    root = Path(__file__).resolve().parents[1]
    paths = [
        root/'results/R69-actual-closed-approximate-exterior-and-two-held-disks.md',
        root/'results/R11-matched-mode-four-physical-tail-connector.md',
        root/'results/R115-actual-tail-holomorphic-neighborhood-and-strong-extension.md',
        root/'results/R119-actual-final-connector-all-label-continuation.md',
        Path(__file__).resolve(),
    ]
    return {
        'schema': 'visible-exact-R119-installed-final-connector-v1',
        'scope': 'Exact rational gates for the proved all-label continuation on the actual R69 final connector group; not a full regular-port inverse.',
        'inputs': {
            'tail_cut': 128,
            'source_tau': str(tau),
            'source_sigma0': str(sigma0),
            'raw_output_sigma': str(sigma_out),
            'grounded_output_sigma': str(sigma_g),
            'final_group_length_upper': '1/8',
            'short_quintic_length': str(eta),
            'source_R72_blob': 'a7c78793ba18724a4f0553b6ccd55259b8f4df92',
            'source_R25_blob': 'be20257721fed270c59a4024427042fc76ee0073',
            'file_sha256': {str(p.relative_to(root)): sha256(p.read_bytes()).hexdigest() for p in paths},
        },
        'checks': checks,
        'all_pass': all(x['pass_'] for x in checks),
        'claims': {
            'same_installed_final_group': True,
            'all_internal_labels': True,
            'all_high_outputs': True,
            'mean_and_holonomy_retained': True,
            'exact_C2_match_to_infinite_tail': True,
            'actual_grounded_momentum': True,
            'larger_initial_angular_strip_used': False,
            'full_connector_continuation': False,
            'regular_high_incoming_inverse': False,
            'global_exact_visible_family': False,
        },
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path)
    args = parser.parse_args()
    report = run()
    encoded = json.dumps(report, ensure_ascii=False, indent=2)+'\n'
    if args.out:
        args.out.write_text(encoded)
        print(json.dumps({'all_pass': report['all_pass'], 'checks': len(report['checks']),
                          'out': str(args.out)}, ensure_ascii=False))
    else:
        print(encoded, end='')
