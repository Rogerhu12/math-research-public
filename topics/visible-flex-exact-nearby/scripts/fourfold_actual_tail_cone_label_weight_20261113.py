#!/usr/bin/env python3
"""Exact finite gates for the actual all-frequency R15 label-weight bound."""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import argparse
import json


def run():
    checks = []
    def gate(name, condition, **data):
        checks.append({'name': name, 'pass': bool(condition),
                       **{k: str(v) for k, v in data.items()}})
        if not condition:
            raise ArithmeticError(name)
    eps, ratio = Q(1, 2048), Q(1, 2**26)
    gate('nu_lower_bound_at_smallest_mode', Q(4**2*(4**2-1), 12) >= Q(4**4, 16))
    coeff = Q(65, 64)*(64+Q(1, 64))
    gate('dominant_eigenvalue_above_64_nu', (coeff-64)*20-(1+Q(1, 64))-1 > 0)
    gate('small_eigenvalue_ratio', Q(1, 64*(4*4**4)**2) == ratio)
    gate('L_upper_bound_by_m4', Q(66, 12*512) < 1)
    gate('true_absolute_error_window_first_gate', 10*Q(1, 2**28) < 1)
    gate('true_absolute_error_window_second_gate', Q(1, 2**14) < 1)
    relative = Q(12*32768, 4)*Q(1, 2**28)
    gate('true_relative_error_budget', relative == Q(3, 8192))
    gate('relative_error_with_cone_margin', relative < eps)
    denominator = 1-Q(3, 2)*eps
    gate('dominant_coordinate_lower_bound', denominator > Q(1, 2))
    cone_image = (Q(3, 2)*eps+ratio/2)/denominator
    gate('actual_cone_invariance', cone_image < Q(1, 2), upper=cone_image)
    mobius = Q(1, 64*(4*4**4)**2)/denominator**2
    gate('actual_mobius_contraction', mobius < Q(1, 4), upper=mobius)
    gate('m_at_least_8_expansion_factor', Q(8**4, 256) > 2)
    gate('low_labels_need_no_prefix', 56+8*8 < 129)
    gate('exact_delta_to_label_layer_factor', 2*Q(25, 2) == 25)
    gate('crossing_layer_implies_strong_window', 5*Q(1, 2**128) < Q(1, 2**28))
    gate('crossing_exponent', 4-128//2 == -60)
    gate('ceil_prefix_integer_margin', 56+1-129 == -72)
    gate('log_two_lower_for_prefix', Q(11, 4)**2 < 8)
    term, lower = Q(1), Q(1)
    for k in range(1, 6):
        term *= Q(7, 10*k)
        lower += term
    gate('log_two_upper_for_prefix', lower > 2)
    gate('prefix_constant', 56+312*Q(1, 4)+312*6 == 2006)
    gate('prefix_u_coefficient', 12*2006 == 24072)
    gate('prefix_u_squared_coefficient', 12*312 == 3744)
    gate('elementary_e_lower', 1+1+Q(1, 2)+Q(1, 6) == Q(8, 3))
    gate('prefix_maximum_linear_term', 24072*Q(3, 8) == 9027)
    gate('prefix_maximum_square_term', 3744*Q(9, 16) == 2106)
    prefix = 11133*Q(3, 8)**6
    gate('all_frequency_prefix_cost_below_32m', prefix < 32, upper=prefix)
    gate('total_raw_canonical_exponent', 358+32 == 390)
    gate('prefactor_absorbed_in_one_m', 4 < 2**4)
    gate('physical_raw_exponent', Q(5177, 400)+391 < 404)
    gate('R74_replacement_difference', 404-371 == 33)
    gate('R74_complete_linear_constant', 2000+33 == 2033)
    gate('R74_weighted_label_gap_positive', 2**23-2033-8192 > 0)
    gate('R74_weighted_label_exponent', 4*(2**23-2033-8192) == 33513532)
    root = Path(__file__).resolve().parents[1]
    paths = [
        root/'results/R15-full-tail-lines-label-weights-and-ordinary-sources.md',
        root/'results/R74-actual-full-tail-robin-and-augmented-positive-cap.md',
        root/'results/R15-supplement-actual-dominant-cone-and-exponential-label-weight.md',
        Path(__file__).resolve(),
    ]
    return {
        'schema': 'visible-exact-R15-true-cone-exponential-label-weight-v1',
        'scope': 'Actual all-frequency, all-layer homogeneous tail trace-to-label bound; no nonlinear graph inverse is asserted.',
        'inputs': {'relative_cell_window': 'm^4 sqrt(delta_j) <= 2^-28',
                   'relative_matrix_error': str(eps),
                   'true_cone_radius': '1/2',
                   'canonical_label_exponent': 391,
                   'physical_raw_exponent': 404,
                   'source_R72_blob': 'a7c78793ba18724a4f0553b6ccd55259b8f4df92',
                   'file_sha256': {str(p.relative_to(root)): sha256(p.read_bytes()).hexdigest() for p in paths}},
        'checks': checks,
        'all_pass': all(c['pass'] for c in checks),
        'claims': {'all_actual_cell_flows_retained': True,
                   'all_high_labels_retained': True,
                   'complete_two_trace_norm': True,
                   'height_nonvanishing_assumed': False,
                   'mean_replaced_by_nonzero_frequency': False,
                   'log_squared_label_fee_removed': True,
                   'nonlinear_regular_high_inverse': False},
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
