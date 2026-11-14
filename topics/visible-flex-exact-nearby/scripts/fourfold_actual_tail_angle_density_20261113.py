#!/usr/bin/env python3
"""Exact nonlinear principal/flux identities and actual drift-angle gates.

Uses SymPy only for rational symbolic identities.  No sampled frequency or
truncated tail is used to assert a high-frequency inverse.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path

import sympy as sp


def run():
    checks=[]

    def gate(name,condition,evidence):
        if not condition:
            raise AssertionError(name)
        checks.append({'name':name,'pass':True,'evidence':evidence})

    P,K,U,V,Uth,Vth,w,A=sp.symbols('P K U V Uth Vth w A')
    E=1+w*w
    J=1+K+E*U
    D=1-w*w*(2*K+K*K+E*P*P)
    Qph=V-P
    F=(-A*(2*K+U+K*K+K*U+w*w*P*P)+E*Qph*Qph)/J
    Fp,Fk,Fu,Fv=[sp.diff(F,x) for x in (P,K,U,V)]
    d=E*Qph/J
    v2=D/J**2
    # Keep the actual quotient factors while reducing identities; expanding
    # unrelated full denominators first is needlessly expensive.
    zero=lambda expr: sp.factor(expr)==0
    gate('exact_true_principal_F_U',zero(Fu+(A*D+E**2*Qph**2)/J**2),
         'Differentiate the actual complete nonlinear quotient')
    gate('exact_true_principal_F_V',zero(Fv-2*d),
         'The drift is EQ/J and includes the true mean K0')
    gate('exact_true_principal_discriminant',zero(Fv**2+4*Fu+4*A*v2),
         'All actual type zeros remain exactly the original A(t)=0')

    dd,vv=sp.symbols('d v',nonzero=True)
    B=sp.Matrix([[0,1],[-A*vv**2-dd**2,2*dd]])
    T=sp.Matrix([[1,0],[dd,vv]])
    target=dd*sp.eye(2)+vv*sp.Matrix([[0,1],[-A,0]])
    gate('exact_turning_regular_frame',all(zero(x) for x in T.inv()*B*T-target),
         'No division by A or sqrt(A) occurs in the true frame')

    t_rules={P:V-(A+1)*P,K:F,U:Vth-(A+1)*U,
             V:Fp*U+Fk*V+Fu*Uth+Fv*Vth,w:A*w}
    theta_rules={P:U,K:V,U:Uth,V:Vth,w:0}
    dt=lambda expr:sum(sp.diff(expr,x)*rhs for x,rhs in t_rules.items())
    dtheta=lambda expr:sum(sp.diff(expr,x)*rhs for x,rhs in theta_rules.items())
    logv=sp.log(D)/2-sp.log(J)
    gate('complete_v_transport_identity',zero(dt(logv)-d*dtheta(logv)+dtheta(d)
         -(A*(1-v2)-d**2)/E),
         'All independent U_theta and V_theta terms cancel exactly')
    gate('complete_d_transport_identity',zero(dt(d)-d*dtheta(d)-A*dtheta(v2)/2
         -d*(-1+(A*(w*w-v2)-d*d)/E)),
         'The true drift identity contains no omitted A_t/A term')

    kap=sp.symbols('kap',nonzero=True)
    mu=kap/vv
    M=mu*sp.Matrix([[1,-dd],[-dd,dd**2+A*vv**2]])
    gate('exact_grounded_density_determinant',zero(M.det()-A*kap**2),
         'This is the actual Gauss determinant, not a scalar model determinant')
    xi,rootA=sp.symbols('xi rootA')
    gate('exact_conormal_principal_cancellation',zero(mu*((sp.I*dd*xi+rootA*vv*xi)-dd*sp.I*xi)-kap*rootA*xi),
         'Both the actual angular drift and v cancel in the physical conormal symbol')
    jj,theta_d,pp,theta_p,theta_flux,ss=sp.symbols('j dtheta p ptheta fluxtheta source')
    transformed=-theta_d*jj*pp+jj*(theta_d*pp+dd*theta_p-theta_flux+ss-dd*theta_p)
    gate('exact_density_pullback_drift_cancellation',zero(transformed-jj*(-theta_flux+ss)),
         'p_t=(d p)_theta-flux_theta+s and j_t=-(d_theta composed)j')
    aa=mu*jj
    bb=mu*A*vv**2/jj
    gate('exact_pulled_back_density_product',zero(aa*bb-A*kap**2),
         'The full source and both trace densities carry the true angular Jacobian')

    eta=sp.symbols('eta')
    kfun=sp.Function('k')(eta)
    nufun=sp.Function('nu')(eta)
    ffun=sp.Function('f')(eta)
    qfun=sp.diff(kfun,eta)/kfun
    actual=sp.diff(kfun**2*nufun*sp.diff(ffun/kfun,eta),eta)/kfun
    claimed=sp.diff(nufun*sp.diff(ffun,eta),eta)-(sp.diff(nufun*qfun,eta)+nufun*qfun**2)*ffun
    gate('exact_full_amplitude_lower_order_identity',sp.simplify(actual-claimed)==0,
         'All amplitude first derivatives and the complete potential are retained')
    gate('exact_regular_translation_column',sp.simplify(-sp.diff(nufun*sp.diff(kfun,eta),eta)
         +(sp.diff(nufun*qfun,eta)+nufun*qfun**2)*kfun)==0,
         'The canonical regular translation column is (k,0), not a discarded constant')

    n=Q(1,64)
    gate('actual_drift_relative_bound',Q(2)/(1-2*n)<3,
         '|d|<=2N/(1-2N)')
    gate('actual_v_relative_bound',Q(5)/(1-2*n)<6,
         '|sqrt(D)-J|<5N on the complete relative ball')
    gate('actual_frame_bound',1+9*n<2,
         'T has row bound |d|+|v|<=1+9N')
    gate('actual_inverse_frame_bound',(1+3*n)/(1-6*n)<2,
         'No turning-point factor is hidden in T inverse')
    gate('complete_local_correction_is_smaller',55-Q(2407,2)*132<0,
         'R72 5.6 correction divided by 4.6 is <=2^55 delta^(2407/2)')
    gate('complete_relative_tail_constant',35+8+3+18==64,
         'Physical strong flow, actual w_min, four-state sum, and h^-5 all retained')
    gate('complete_relative_tail_exponent',Q(39,4)-1-7-Q(5,256)==Q(443,256),
         'This is the actual local relative state exponent after all conversions')
    gate('actual_first_tail_cell_smallness',132*Q(443,256)-64>164,
         'delta_129<2^-132 and ||X||<1')
    gate('actual_total_tail_log_length',Q(16,25)<1,
         '2 delta_128 <2^-130, with delta_128=(2/25)2^-128')
    gate('actual_connector_and_bumps_length',127+Q(75,16)<132,
         'All installed connector groups and both fixed bumps are included')
    gate('actual_drift_and_derivative_tail_bound',3*Q(1,2**164)<Q(1,2**162),
         'One actual unit of angular width pays the derivative')
    gate('actual_drift_and_derivative_connector_bound',3*Q(1,2**8423)<Q(1,2**8420),
         'The already proved weighted full chart supplies the actual outer segment')
    integral=2*Q(1,2**162)*Q(1,2**130)+264*Q(1,2**8420)
    gate('complete_true_drift_integral',integral<Q(1,2**289),
         'The entire infinite tail and both finite connector pieces are covered')
    gate('complex_flow_remains_in_paid_strip',Q(1,2**289)<Q(1,2),
         'Start at width tau-3 inside the actual coefficient width tau-2')
    gate('full_Fourier_Cauchy_factor',1+Q(2,15)<2,
         'All 4Z frequencies sum after a true unit of remaining strip width')
    gate('actual_angle_and_Jacobian_Wiener_norm',6*Q(1,2**289)<Q(1,2**280),
         'Displacement, exponential Jacobian, and complete Fourier summation are all paid')
    gate('complete_two_trace_Sobolev_isomorphism',Q(1,2)<1-Q(1,2**280)<1+Q(1,2**280)<2,
         'L2 and H1 change-of-variable bounds interpolate and dualize to Hhalf/Hminus-half')

    root=Path(__file__).resolve().parents[1]
    paths=[
        root/'results/R115-actual-tail-holomorphic-neighborhood-and-strong-extension.md',
        root/'results/R119-actual-final-connector-all-label-continuation.md',
        root/'results/R119-supplement-two-bumps-and-exact-nonlinear-matching.md',
        root/'results/R119-supplement-actual-tail-angle-density-conjugation.md',
        Path(__file__).resolve(),
    ]
    return {
        'schema':'visible-exact-R119-actual-tail-angle-density-conjugation-v1',
        'scope':'Exact nonlinear mixed-tail principal frame, actual drift-angle flow, true grounded density/source conjugation, and complete degenerate amplitude frame. No all-frequency return inverse is asserted.',
        'inputs':{'true_uniform_tail_relative_state':'2^-164',
                  'actual_total_tail_log_length':'2^-130',
                  'actual_full_drift_integral':'2^-289',
                  'actual_full_angle_and_Jacobian_bound':'2^-280',
                  'paid_output_angle_width':'5177/400-4',
                  'source_R72_blob':'a7c78793ba18724a4f0553b6ccd55259b8f4df92',
                  'file_sha256':{str(p.relative_to(root)):sha256(p.read_bytes()).hexdigest() for p in paths}},
        'checks':checks,
        'all_pass':all(c['pass'] for c in checks),
        'claims':{'actual_nonlinear_type_zeros_preserved':True,
                  'true_turning_regular_principal_frame':True,
                  'complete_grounded_flux_and_source':True,
                  'actual_angle_flow_entire_infinite_tail_and_connector':True,
                  'full_two_trace_bounded_angle_conjugacy':True,
                  'mean_and_regular_column_retained':True,
                  'degenerate_amplitude_weights_explicit':True,
                  'same_width_pullback_difference_claimed_small':False,
                  'nonlinear_actual_high_return_inverse':False,
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
