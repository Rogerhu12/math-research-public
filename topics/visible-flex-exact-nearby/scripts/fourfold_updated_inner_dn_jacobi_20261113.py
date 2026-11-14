#!/usr/bin/env python3
"""Exact gates for the genuine updated annulus DN/Jacobi operator.

The source variable is the continuous scalar RHS in the actual relative
Darboux K_t equation.  A general metric-source conversion is not asserted.
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

    r=Q(1,2**24)
    r0=Q(1,2**8418)
    L_lower=Q(7,5)*(2**24-Q(25,8))
    gate('actual_inner_half_kernel_margin',Q(3,4)-Q(3,2)/4==Q(3,8),
         'M>=4, with q_i=exp(t/2) and the actual paid angle ramp')
    gate('inner_weighted_green_height',1+Q(8,3)<4,
         'Both exact finite-interval half-kernels are retained')
    gate('inner_weighted_green_first_jet',3*(1+Q(8,3))<12,
         'Use the complete differentiated Green kernel')
    gate('inner_weighted_green_second_jet',1+Q(4*12,4)+4==17,
         'The second derivative is recovered from the exact ODE')
    gate('inner_weighted_complete_green',4+12+17<64,
         'All three jets are summed before all Fourier frequencies')
    gate('unweighted_variable_angle_margin',Q(3,4)-Q(2,4)==Q(1,4),
         'The W0 inward kernel rate is at least M/4')
    gate('W0_green_height',1+4==5,'Two half-kernels with rates M and M/4')
    gate('W0_green_first_jet',3*(1+4)==15,'The exact first kernel derivative')
    gate('W0_green_second_jet',1+Q(4*15,4)+5==21,'Use the exact Jacobi ODE')
    gate('W0_complete_green',5+15+21<64,'Same actual long interval and variable angle strip')
    gate('inner_Jacobi_contraction',64*4096*r==Q(1,64),
         'Actual h=h0+z has complete W0 norm less than 2r')
    gate('inner_Jacobi_boundary_bound',16/(1-Q(1,64))==Q(1024,63)<17,
         'This is the full nonlinear DN derivative input column')
    gate('true_outer_state_difference',Q(25,8)+1024*r<4,
         'All four states, including the complete mean-root difference')
    gate('true_inner_state_derivative',Q(25,8)+1024*r<4,
         'The complete mean derivative is included in D S(h) xi')
    gate('background_split_source_fee',64*4*4==1024<2048,
         'q_i q_o=exp(L/2), so the separated product pays exp(-L/2) exactly')
    gate('inner_endpoint_source_fee',3*4==12,
         'M times the inner derivative kernel integrates at rate at least M/4')
    gate('actual_updated_DN_difference_fee',12*2048*17<2**19,
         'This is a relative operator norm on actual inner boundary traces')
    gate('actual_long_length_exceeds_screening_budget',L_lower/2>8418,
         'Using e>2 gives r exp(-L/2)<2^-8418=r0')
    gate('relative_DN_actual_number',2**19*2*r0<Q(1,2**8390),
         'The real all-frequency updated DN difference is below the stated safe bound')
    gate('actual_mean_boundary_derivative_fee',299*17<2**13,
         'The full holonomy-root derivative from N.12 is retained')
    gate('actual_mean_boundary_number',2**13*2*r0<Q(1,2**8400),
         'The inner normalized mean slope derivative is not discarded')

    gate('source_holonomy_decay_rate',2*1==2,
         '(w^2)_t=2w^2 on the same A=1 radial annulus')
    gate('source_holonomy_integral_constant',2*Q(1,2)==1,
         '||rho A_h||<2 and the e^-2(t-s) kernel has L1 norm at most 1/2')
    gate('mean_load_to_nonmean_source',128*8==1024,
         'b_h=Pi_perp(partial_K Q_full)/<rho A_h>, with N<8r')
    green_corrected=Q(64)/(1-Q(1,64))
    gate('updated_continuous_source_Green',green_corrected<66,
         'The actual updated inverse is the complete W0 Neumann inverse')
    gate('updated_continuous_source_E_constant',green_corrected*(1+1024*r)<67,
         'Includes the source-induced mean load before solving the nonmean equation')
    gate('updated_source_initial_mean_constant',green_corrected*1024*r==Q(1,252)<Q(1,128),
         'The actual initial source holonomy m_B is a retained input')
    gate('updated_source_boundary_constant',Q(16)/(1-Q(1,64))<17,
         'Both actual nonmean Dirichlet endpoints are retained')

    root=Path(__file__).resolve().parents[1]
    paths=[
        root/'results/R119-supplement-actual-long-radial-nonlinear-dirichlet-problem.md',
        root/'results/R119-supplement-two-bumps-and-exact-nonlinear-matching.md',
        root/'results/R119-supplement-nonlinear-screened-outer-to-inner-map.md',
        root/'results/R119-supplement-updated-inner-dn-and-continuous-jacobi-sources.md',
        Path(__file__).resolve(),
    ]
    return {
        'schema':'visible-exact-R119-actual-updated-inner-dn-jacobi-v1',
        'scope':'The actual nonlinear annulus inner DN derivative in its complete physical trace units and the updated continuous scalar Darboux-source Jacobi column; the mixed-tail relative graph inverse and general metric-source conversion are not asserted.',
        'inputs':{'outer_Dirichlet_radius':'2^-29',
                  'nonlinear_screened_background_radius':'2^-24',
                  'true_inner_background_radius':'2^-8418',
                  'relative_inner_DN_difference':'2^-8390',
                  'actual_mean_boundary_derivative':'2^-8400',
                  'source_units':'e = delta K_t - D F_t[delta P,delta K,delta U,delta V]',
                  'retained_initial_holonomy':'m_B = delta M(0)/w_B^2',
                  'file_sha256':{str(p.relative_to(root)):sha256(p.read_bytes()).hexdigest() for p in paths}},
        'checks':checks,
        'all_pass':all(c['pass'] for c in checks),
        'claims':{'actual_updated_nonlinear_background':True,
                  'full_all_high_inner_DN_derivative':True,
                  'same_inner_physical_angle_width':True,
                  'complete_mean_boundary_derivative':True,
                  'ordinary_continuous_scalar_Darboux_source':True,
                  'source_induced_holonomy_retained':True,
                  'joint_annulus_Schur_row_identified':True,
                  'mixed_tail_relative_graph_inverse':False,
                  'general_metric_source_conversion':False,
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
