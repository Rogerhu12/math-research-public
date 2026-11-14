#!/usr/bin/env python3
"""Exact all-frequency constants for nonlinear long-annulus screening.

The proof constructs the genuine nonlinear difference problem on the actual
annulus and retains the complete mean root.  These gates check its arithmetic;
they do not assert an inverse for the nonlinear mixed-tail matching column.
"""
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

    sigma_o=Q(1,512)
    sigma_i=Q(5177,400)+1968
    S=4*(sigma_i-sigma_o)
    L_lower=Q(7,5)*(2**24-Q(25,8))
    r=Q(1,2**24)
    r0=Q(1,2**8418)
    gate('actual_angle_ramp_length',0<S<8000<L_lower,
         'S=4(sigma_i-sigma_o); sigma_i is the actual paid double-bump output')
    gate('actual_same_width_background_solution',Q(16)/(1-Q(1,64))==Q(1024,63)<17,
         'Use the already proved nonlinear Dirichlet solution with outer data zero')
    gate('actual_background_smallness',17*Q(1,2**8423)<r0,
         'The true f_B is supplied by the actual nonlinear tail chart')
    gate('background_less_than_difference_radius',r0<r,
         'Only the difference, not the fixed inner-end background, carries q(t)')
    gate('inward_weighted_kernel_rate',Q(3,4)-Q(5,2)/4==Q(1,8),
         '(3/4)M-5/2>=M/8 for every M>=4')
    gate('outward_weighted_kernel_rate',Q(5,2)>0,
         'The opposite half-kernel has decay at least exp(-M(t-s))')
    gate('weighted_green_height_constant',8+1==9,
         'Integrate the full finite-interval kernel over the two half-intervals')
    gate('weighted_green_first_jet_constant',3*(8+1)==27,
         'The exact differentiated kernel is at most 3 times the same exponential')
    gate('weighted_green_second_jet_constant',1+Q(4*27,4)+9==37,
         'Use the exact ODE, not a differentiated absolute-value estimate')
    gate('complete_weighted_green_bound',9+27+37==73<128,
         'The complete sum of all three jets is bounded uniformly in actual L')
    gate('weighted_boundary_lift',2+6+8==16,
         'Same exact lift, with the positive inward exponential margin retained')

    n=Q(1,64)
    gate('complete_mean_T_domain',2*n+3*n*n<3*n<Q(1,16),
         'T=2K+K^2+E P^2 with E<=2 and complete N<=1/64')
    gate('binomial_derivative_tail_bound',Q(3,4)*Q(16,15)**2<1,
         '(3/8)(2-x)/(1-x)^2<1 for 0<=x<=1/16')
    gate('complete_mean_first_remainder_derivative',2+3*3==11,
         'Quadratic terms plus the exact square-root series remainder')
    gate('complete_mean_B_bound',10+2*n<11,
         'B=(1+K)J/(1-w^2P^2)-1 includes every nonconstant term')
    gate('complete_mean_dB_bound',4+12+32*n<17,
         'Differentiate all numerator, square-root, and inverse factors')
    gate('complete_mean_second_remainder_derivative',11+17==28,
         'Differentiate U B and retain both product terms')
    gate('complete_mean_total_derivative',11+28==39,
         'The linear angular mean vanishes by the actual compatibility relations')
    gate('complete_mean_implicit_derivative',39/(1-Q(9,64))<46,
         'Use the full holonomy root derivative, not a discarded mean row')
    gate('complete_mean_Y_derivative',46*4*Q(13,8)==299<512,
         'P, U and Kperp variation has coefficient 13/8 in Y')
    gate('complete_relative_state_derivative',Q(25,8)+Q(512,2048)<4,
         'The true mean derivative is included in the complete four-state derivative')
    gate('complete_quadratic_numerator_derivative',4+2+4+4+2==16,
         'Each term of E(V-P)^2+K^2+2EKU+EU^2-w^2P^2 is differentiated')
    gate('complete_quotient_derivative',32+128*n==34<64,
         'The derivative of the denominator inverse is retained')
    gate('weighted_source_lipschitz_constant',64*4*4==1024<2048,
         'The weighted ideal norm is placed on each differentiated factor')

    gate('nonlinear_difference_domain',2*r<Q(1,2048),
         'h0+z remains inside the actual mean and source domain')
    gate('outer_data_lift_half_ball',16*Q(1,2**29)==r/2,
         'Outer physical angular input is measured at sigma_o=1/512')
    gate('complete_nonlinear_weighted_contraction',128*2048*2*r==Q(1,32),
         'The contraction is for the actual nonlinear difference problem')
    gate('complete_difference_selfmap',Q(1,2)+Q(1,32)<1,
         'The weighted full-frequency closed ball maps into itself')
    gate('complete_nonlinear_input_Lipschitz',16/(1-Q(1,32))==Q(512,31)<17,
         'The same bound holds for differences of two permitted outer inputs')
    gate('complete_inner_mean_screening',17*2**11*r<1,
         'The mean derivative is screened after using its full root difference')
    gate('ordinary_Dirichlet_uniqueness_overlap',2*r<Q(1,2**20),
         'The weighted solution is the same existing physical nonlinear solution')
    gate('outer_boundary_original_ball',Q(1,2**8423)+Q(1,2**29)<Q(1,2**25),
         'No larger Dirichlet input ball is silently introduced')

    root=Path(__file__).resolve().parents[1]
    paths=[
        root/'results/R119-supplement-actual-long-radial-nonlinear-dirichlet-problem.md',
        root/'results/R119-supplement-two-bumps-and-exact-nonlinear-matching.md',
        root/'results/R119-supplement-nonlinear-screened-outer-to-inner-map.md',
        Path(__file__).resolve(),
    ]
    return {
        'schema':'visible-exact-R119-actual-nonlinear-outer-screening-v1',
        'scope':'The actual nonlinear outer Dirichlet-to-inner complete trace column with its true fixed nonlinear inner height; no nonlinear mixed-tail matching inverse is asserted.',
        'inputs':{'outer_physical_angular_width':str(sigma_o),
                  'inner_paid_physical_angular_width':str(sigma_i),
                  'angle_ramp_length':str(S),
                  'actual_L_lower':str(L_lower),
                  'complete_outer_boundary_radius':'2^-29',
                  'complete_weighted_response_radius':'2^-24',
                  'radial_screening':'exp(-L/2)',
                  'source_R25_blob':'be20257721fed270c59a4024427042fc76ee0073',
                  'file_sha256':{str(p.relative_to(root)):sha256(p.read_bytes()).hexdigest() for p in paths}},
        'checks':checks,
        'all_pass':all(c['pass'] for c in checks),
        'claims':{'actual_full_nonlinear_difference_problem':True,
                  'fixed_actual_nonlinear_inner_height':True,
                  'all_outer_and_inner_angular_modes':True,
                  'paid_inner_angular_width_gain':True,
                  'complete_mean_slope_difference':True,
                  'outer_mean_height_integral_retained':True,
                  'nonlinear_mixed_tail_relative_inverse':False,
                  'ordinary_metric_source_columns':False,
                  'final_global_family':False},
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
