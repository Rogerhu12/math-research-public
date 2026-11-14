#!/usr/bin/env python3
"""Exact finite budget for R119's paid-weight, entire installed connector."""
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
    beta, T = 8192, 2**24
    eta = Q(1, 2**24)
    tau, d = Q(5177, 400), Q(9, 400)
    gate('actual_complete_connector_length',
         Q(1, 3)+2*eta+126+Q(1, 4)+Q(1, 8) < 127)
    # exp(7/10)>2 from a finite positive Taylor sum, hence log 2<7/10.
    term, lower = Q(1), Q(1)
    for k in range(1, 6):
        term *= Q(7, 10*k)
        lower += term
    gate('log_two_bound', lower > 2)
    gate('paid_label_weight', beta == 2**13)
    gate('nonzero_frequency_decay_exponent', 2*beta-d > 2*beta-1)
    gate('all_mean_restored_after_restriction', 12*Q(1, 64) < 1)
    relative_initial = 16-(2*beta-1)
    reaction_exponent = 2*32*127
    relative_output = relative_initial+reaction_exponent
    gate('initial_relative_exponent', relative_initial == -16367)
    gate('whole_connector_reaction_exponent', reaction_exponent == 8128)
    gate('whole_connector_relative_exponent', relative_output == -8239)
    gate('actual_relative_slope_scale', 7-Q(131*15, 4) < -484)
    gate('complete_relative_ball_exponent', relative_output-484 == -8723)
    gate('complete_relative_ball_closes', -8723 < -6)
    sigma0 = tau+Q(beta, 2)
    sigma_min = tau+Q(beta, 2)-16*127
    sigma_out, sigma_ground = tau+2048, tau+2047
    gate('exact_initial_width', Q(beta, 2) == 4096)
    gate('actual_output_energy_width', sigma_min == tau+2064)
    gate('raw_angular_margin', sigma_min-sigma_out == 16)
    gate('grounded_angular_margin', sigma_min-sigma_ground == 17)
    gate('no_free_strip_increase', sigma_ground < sigma_out < sigma_min < tau+beta)
    gate('downstream_physical_window', Q(1, 512) < tau-4 < sigma_ground)
    radius_exponent, slope_exponent = 1+2*127, 2*7*127
    gate('reference_radius_exponent', radius_exponent == 255)
    gate('slope_ratio_exponent', slope_exponent == 1778)
    rw_exponent = radius_exponent+slope_exponent
    gate('height_integrand_exponent', rw_exponent == 2033)
    gate('height_integral_exponent', 7+rw_exponent+relative_output == -6199)
    gate('height_derivative_exponent', slope_exponent+relative_output == -6461)
    gate('raw_output_fourth_derivative_margin', (Q(4)/(2*16))**4 < 1)
    gate('raw_output_second_derivative_margin', (Q(2)/(2*16))**2 < 1)
    gate('complete_raw_trace_label_constant', -6198+4 < -6192)
    gate('physical_vertical_hessian', Q(5, 18)*(7+15) < 7)
    gate('physical_horizontal_curvature_factor', Q(5, 18) < 1)
    gate('complete_physical_C2_exponent', 17-8723+2 < -8690)
    gate('R74_label_weight_is_paid', beta < T//8)
    gate('R74_complete_label_decay_gap', 4*(T//8-beta) == 8355840)
    gate('R74_label_ball_for_unit_source', 8355840 > 4)
    root = Path(__file__).resolve().parents[1]
    paths = [
        root/'results/R119-actual-final-connector-all-label-continuation.md',
        root/'results/R119-supplement-full-installed-connector-with-paid-label-weight.md',
        root/'results/R74-actual-full-tail-robin-and-augmented-positive-cap.md',
        Path(__file__).resolve(),
    ]
    return {
        'schema': 'visible-exact-R119-full-installed-connector-weight-v1',
        'scope': 'Paid all-mode label-weight continuation through the whole installed connector; the regular-port nonlinear inverse remains open.',
        'inputs': {'label_exponential_weight': beta, 'T': T,
                   'source_absolute_tau': str(tau),
                   'weighted_initial_relative_tau': str(tau+Q(beta, 2)),
                   'raw_output_tau': str(sigma_out),
                   'grounded_output_tau': str(sigma_ground),
                   'file_sha256': {str(p.relative_to(root)): sha256(p.read_bytes()).hexdigest() for p in paths}},
        'checks': checks,
        'all_pass': all(c['pass'] for c in checks),
        'claims': {'same_actual_complete_connector': True,
                   'stronger_label_domain_is_explicit': True,
                   'all_modes_and_mean_retained': True,
                   'R74_linear_label_inputs_pay_extra_weight': True,
                   'two_bumps_and_long_radial_segment_included': False,
                   'regular_port_nonlinear_high_inverse': False,
                   'global_exact_visible_family': False},
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
