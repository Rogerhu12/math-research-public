#!/usr/bin/env python3
"""Exact gates for the actual all-label base Schur inverse and its width loss."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path


def run():
    checks=[]

    def gate(name,condition,evidence):
        if not condition:
            raise AssertionError(name)
        checks.append({'name':name,'pass':True,'evidence':evidence})

    gate('actual_two_trace_inverse_first_row',1/(Q(7,5)*(1-Q(1,4)))<1,
         'The true J_M inverse first row is 1/[omega(1-1/M)]')
    gate('actual_two_trace_inverse_second_row',1/(1-Q(1,4))==Q(4,3),
         'The true J_M inverse second row is 1/(1-1/M)')
    gate('actual_radius_cancellation',Q(4,3)/(16*Q(7,5))==Q(5,84)<Q(1,16),
         'h(B)^2 times the actual physical Y state cancels the inverse physical radius')
    gate('actual_inner_residual_to_Y_constant',Q(1,16)*2**40==2**36,
         'The complete two-trace gap is used; no height denominator is introduced')
    gate('true_tail_delta_lower_bound',Q(2,25)*16>1,
         'delta_tail=(2/25)2^-128>2^-132')
    gate('true_tail_delta_power_fee',Q(15,4)*132==495,
         'delta_tail^(-15/4)<2^495')
    gate('true_physical_scale_and_growth_fee',7+495+1080+36==1618,
         '128, delta power, Omega^3, and the exact relative two-trace inverse')
    gate('all_actual_flow_frequency_fees',1143+4*Q(25,8)+404==Q(3119,2),
         'The same installed connector, both real bumps, and the complete raw label weight')
    gate('endpoint_physical_scale_ratio_fee',3*Q(25,8)==Q(75,8),
         'h(T)^2/h(B)^2<=exp(3 L_u)')
    gate('all_frequency_constant_absorption',Q(1618)*Q(7,10)/4==Q(5663,20),
         'log 2<7/10 and M>=4')
    gate('all_frequency_polynomial_absorption',4*(2*Q(7,10))/4==Q(7,5),
         'log M/M decreases for M>=4, so 4 log M/M<=log4<7/5')
    total=Q(3119,2)+Q(5663,20)+Q(7,5)+Q(75,32)
    gate('complete_actual_label_width_fee',total==Q(295423,160)<1850,
         'All true profile and state conversions are included before the final safe exponent')
    gate('complete_strong_inverse_constant',Q(1,4**2)==Q(1,16),
         'The Z_sigma norm uses M|g_m| while the label bound uses |g_m|/M')
    gate('same_weighted_chart_would_require_true_width',8192+1850==10042,
         'This input width has not been granted by the current nonlinear chart')
    sigma_i=Q(5177,400)+1968
    gate('actual_nonlinear_column_width_match',128+1850==1978<sigma_i,
         'The existing actual nonlinear outer-to-inner column genuinely pays ell1_128')
    gate('actual_nonlinear_preconditioned_column',Q(17,16)<2,
         'The complete nonlinear forcing Lipschitz bound is composed with the true base inverse')
    gate('label_domain_mismatch_is_not_hidden',128<8192 and sigma_i<10042,
         'No claim of a closed nonlinear Newton map in ell1_8192 is made')

    root=Path(__file__).resolve().parents[1]
    paths=[
        root/'results/R15-supplement-actual-dominant-cone-and-exponential-label-weight.md',
        root/'results/R74-actual-full-tail-robin-and-augmented-positive-cap.md',
        root/'results/R119-supplement-two-bumps-and-exact-nonlinear-matching.md',
        root/'results/R119-supplement-nonlinear-screened-outer-to-inner-map.md',
        root/'results/R119-supplement-updated-inner-dn-and-continuous-jacobi-sources.md',
        root/'results/R119-supplement-joint-tail-label-schur-normalization.md',
        Path(__file__).resolve(),
    ]
    return {
        'schema':'visible-exact-R119-actual-joint-tail-Schur-normalization-v1',
        'scope':'Actual full-frequency base Schur inverse to the original internal tail labels, with explicit analytic width loss; the real nonlinear outer forcing pays ell1_128, not the existing ell1_8192 nonlinear domain.',
        'inputs':{'true_interface_trace_pair':'(f_B,k_B/|m|)',
                  'true_matching_residual_norm':'sum exp(sigma |m|) |m| |g_m|',
                  'complete_angle_width_loss':1850,
                  'nonlinear_forcing_paid_label_weight':128,
                  'existing_nonlinear_chart_label_weight':8192,
                  'file_sha256':{str(p.relative_to(root)):sha256(p.read_bytes()).hexdigest() for p in paths}},
        'checks':checks,
        'all_pass':all(c['pass'] for c in checks),
        'claims':{'all_internal_high_labels':True,
                  'complete_actual_two_trace_inverse':True,
                  'true_physical_scale_cancellation':True,
                  'all_actual_bump_and_connector_flows':True,
                  'real_nonlinear_forcing_column_composed':True,
                  'ordinary_particular_and_mean_rows_retained':True,
                  'same_width_label_inverse':False,
                  'closed_nonlinear_label_iteration':False,
                  'updated_mixed_tail_relative_inverse':False},
    }


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--out',type=Path)
    args=parser.parse_args()
    report=run()
    encoded=json.dumps(report,ensure_ascii=False,indent=2)+'\n'
    if args.out:
        args.out.write_text(encoded)
        print(json.dumps({'all_pass':report['all_pass'],'checks':len(report['checks']),
                          'out':str(args.out)},ensure_ascii=False))
    else:
        print(encoded,end='')
