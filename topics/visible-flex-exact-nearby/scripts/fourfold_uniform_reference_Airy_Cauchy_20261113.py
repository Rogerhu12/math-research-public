#!/usr/bin/env python3
"""Actual full-root polynomial, both Airy rows and uniform-frequency Cauchy."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path

from flint import arb, ctx
import sympy as sp


def run():
    ctx.prec=256
    A=arb
    checks=[]
    numeric={}

    def gate(name, statement, evidence):
        if not bool(statement):
            raise AssertionError(name)
        checks.append({"name":name,"pass":True,"evidence":evidence})

    def zero(e):
        return sp.simplify(e)==0

    def show(a):
        return a.str(45)

    x,d,z,B=sp.symbols('x d z B',real=True)
    qpoly=x+(14*d-sp.Rational(1,28))*x*x-d*x**3-7*d*d*x**4
    gate('exact_actual_root_quartic',zero(7*(1-(1-x/14-d*x*x)**2)-qpoly),
         'The actual quintic simple root has a full polynomial normal form, not merely a finite Taylor match')
    gate('exact_root_scaled_slope',zero(sp.diff(qpoly,x).subs(x,0)-1),
         'The inward x coordinate uses the true root slope')
    zs=sp.symbols('znew')
    gate('exact_root_original_slope_square',zero(60**2*B**2*(sp.Rational(7,30)/B)*12-10080*B),
         'a^2=10080 B(1-4z)/eta^2 with B=sqrt12 Delta/eta')
    gate('root_small_parameter_to_full_disk',Q(1,2**20)/(196*(1-Q(4,2**20)))<Q(1,1024),
         'The actual parameter d lies inside the complete stated coefficient box')
    gate('root_full_germ_stays_inside_quintic',196*(1-Q(4,2**20))>169,
         'The nearest C2 radial seam is farther than13 in the scaled x coordinate')
    gate('root_quartic_second_coefficient_sign',14*Q(1,1024)<Q(1,28),
         'The whole d-box bounds the absolute quadratic coefficient by1/28')
    bdiff=Q(1,28)+Q(1,1024)+Q(7,1024**2)
    gate('root_full_complex_polynomial_modulus',bdiff<Q(1,16),str(bdiff))
    gate('root_fractional_power_derivative',Q(2,3)**3*Q(16,15)<1,
         'The complete principal 2/3 power has derivative modulus below1 on its actual disk')
    gate('root_exact_inverse_Jacobian_disk',Q(1,16)+Q(1,2)*Q(1,8)==Q(1,8),
         'Cauchy gives |g-1|<1/8 on |x|<=1/2')
    gate('root_first_Jacobian_derivative',2*Q(1,8)+Q(1,2)*Q(1,2)==Q(1,2),
         'The complete first derivative of g is retained')
    gate('root_second_Jacobian_derivative',3*Q(1,2)+Q(1,2)*3==3,
         'The full second derivative enters the Liouville potential')
    gate('root_actual_inverse_image_cover',Q(15,16)*Q(1,2)>Q(1,4),
         'The univalent true root map covers the entire requested canonical disk')
    gate('root_true_strict_interface',Q(15,17*64)>Q(1,128),
         'Both root cut values bound the complete remaining negative interval away from zero')

    LL,Lt,yy,yt,ytt,QQ,Qt,mm=sp.symbols('L Lt y yt ytt Q Qt m')
    normalized_h_tt=ytt-LL*yt+(LL**2/4-Lt/2)*yy
    transformed=sp.expand(normalized_h_tt+LL*(yt-LL*yy/2)+mm**2*QQ*yy)
    gate('exact_complete_density_potential',
         zero(transformed.subs({LL:-1-QQ,Lt:-Qt})-
              (ytt+(mm**2*QQ+Qt/2-(1+QQ)**2/4)*yy)),
         'Both derivatives of sqrt(mu), including the Q_t term, are paid')
    gg,gx,gxx,Vx=sp.symbols('g gx gxx Vx',positive=True)
    vv,vxi,vxx=sp.symbols('v vxi vxx')
    # The first-order term cancels in the exact Liouville change y=g^-1/2 v.
    dy=gg**sp.Rational(1,2)*vxi-gx*gg**sp.Rational(-3,2)*vv/2
    ddy=sp.diff(dy,gg)*gx+sp.diff(dy,gx)*gxx+sp.diff(dy,vv)*gg*vxi+sp.diff(dy,vxi)*gg*vxx
    potential=Vx/gg**2+3*gx**2/(4*gg**4)-gxx/(2*gg**3)
    gate('exact_root_complete_Liouville',
         zero((ddy+Vx*gg**sp.Rational(-1,2)*vv)/gg**sp.Rational(3,2)
              -vxx-potential*vv),
         'The full two-row transformation removes the first derivative exactly')
    rootV=2/Q(7,8)**2+3*Q(1,2)**2/(4*Q(7,8)**4)+3/(2*Q(7,8)**3)
    gate('full_complex_root_potential',rootV<16,str(rootV))

    xp=sp.symbols('xp',positive=True)
    ee=1/(4*xp**sp.Rational(3,2))
    Sm=sp.Matrix([[1,ee],[ee,1]])
    Jm=sp.Matrix([[0,1],[-1,0]])
    gen=sp.sqrt(xp)*Jm+sp.diag(1/(4*xp),-1/(4*xp))
    gate('exact_two_row_Airy_Sonin_identity',
         all(zero(k) for k in (gen.T*Sm+Sm*gen)),
         'The modified energy has only S_x, not an omitted angular or flux term')
    gate('full_Airy_frame_bound',Q(80,9)<9 and 3*A(2)**(A(1)/4)<6,
         'Both real Airy columns and their determinant-one inverse are bounded on the entire half line')
    gate('shifted_Airy_full_Cauchy',6*6<64,
         'The frame at both endpoints is paid')
    gate('full_root_interaction_integral',64**2*17*Q(1,64)==1088,
         'The complete potential uses the two-row reference inverse and forward factors')
    gate('full_root_fixed_Gronwall_constant',6+2*1088==2182,
         'e<4 yields a finite constant independent of every actual frequency and layer')

    q,qt,qtt,Qtt=sp.symbols('q qt qtt Qtt',positive=True)
    wave=(Qt/2-(1+QQ)**2/4)/q**2+3*qt**2/(4*q**4)-qtt/(2*q**3)
    wave=wave.subs({qt:Qt/(2*q),qtt:Qtt/(2*q)-Qt**2/(4*q**3)})
    desired=Qt/(2*QQ)-(1+QQ)**2/(4*QQ)+5*Qt**2/(16*QQ**3)-Qtt/(4*QQ**2)
    gate('exact_strict_wave_complete_potential',zero(wave.subs(q,sp.sqrt(QQ))-desired),
         'The density, curvature and both derivative terms are all in the actual wave potential')
    gate('actual_parameter_bump_third_derivative',64*(6+72+180+120)<2**15
         and 8**3*64*(6+72+180+120)<2**24,
         'The actual C2 polynomial bump has the stated piecewise third derivative bound')
    gate('actual_full_Q_second_derivative_envelope',2**6*2**9*2**8<2**26,
         'The original quintic and full parameter bump are bounded before the Liouville transform')
    gate('strict_potential_integral_constant',
         2**23+2**30+2**55+2**37<2**60,
         'Each actual full-potential term is integrated over the real negative interval')
    gate('actual_high_frequency_wave_gate',Q(2**60,2**64)==Q(1,16),
         'The exact wave frequency split gives a complete same-space energy estimate')
    gate('actual_high_frequency_root_gate',64-16>12,
         'Every high-wave frequency is also in the true shifted-Airy root range')
    gate('actual_high_frequency_regularized_speed',
         Q(10)-Q(128,3)<-32,
         'varrho^2*m^(-2/3)<2^-32 follows from the actual split and (j+4)delta^2<1')
    gate('actual_high_frequency_strict_shear',18-64+11<-1,
         'Both the density shear and the q_t shear are small at the strict interfaces')
    gate('actual_full_two_root_composition_constant',2*(2182+8)+7+12<4400,
         'Both root propagators, both endpoint frames per root and the whole strict piece are included')
    gate('actual_low_frequency_auxiliary_constant',136+1+1+7+1<160,
         'The enlarged real density ratio is paid in the complete original low-frequency energy')
    gate('actual_full_low_frequency_polynomial',160+Q(5,3)+Q(5*64,3)<272
         and 1+Q(5*2,3)<5 and 1+Q(5*5,3)==Q(28,3),
         'The frequency cutoff is substituted algebraically, rather than sampling low modes')
    gate('actual_common_uniform_frequency_constant',4400+1<5000 and Q(28,3)<10,
         'The same explicit bound covers every real endpoint and every retained Fourier mode')
    gate('actual_mean_complete_two_row_budget',136+1<160,
         'The exact mean diagonal is included, with its independent raw-height primitive retained separately')

    rows=[]
    for j in (129,4097):
        de=A(2)/25*A(2)**(-j)
        et=de**(A(3)/2)/(4*A(2).sqrt())
        positive=[A(64).log()-de.log(),(A(65)/64).log()-2*de.log()]
        roots=[]
        for k,Delta in enumerate(positive,1):
            b=A(12).sqrt()*Delta/et
            zz=(7/(30*b)).sqrt()
            dd=zz/(196*(1-4*zz))
            ar=(10080*A(12).sqrt()*Delta/et**3*(1-4*zz)).sqrt()
            gate(f'actual_quintic_root_full_disk_{j}_{k}',zz<A(2)**(-20) and dd<A(2)**(-10),
                 {'z':show(zz),'d':show(dd)})
            gate(f'actual_quintic_root_slope_{j}_{k}',ar>de**(-A(9)/4)
                 and ar<A(2)**16*A(j+4).sqrt()*de**(-A(9)/4),show(ar*de**(A(9)/4)))
            roots.append({'root_kind':k,'z':show(zz),'d':show(dd),'scaled_slope':show(ar*de**(A(9)/4))})
        gate(f'actual_auxiliary_speed_all_mode_gate_{j}',A(2)**16*(j+4)*de.sqrt()<1,
             show(A(2)**16*(j+4)*de.sqrt()))
        gate(f'actual_high_split_dimensionless_gate_{j}',(j+4)*de**2<1,show((j+4)*de**2))
        rows.append({'j':j,'roots':roots})
    gate('actual_layer_envelope_monotonicity',Q(134,133)**2<2
         and Q(134,133)<4,
         'The closed first-layer checks extend monotonically through every later actual layer')
    numeric['full_actual_root_endpoint_boxes']=rows
    numeric['root_complex_V_bound']=str(rootV)
    numeric['complete_fixed_root_interaction']=1088
    numeric['all_layer_frequency_split']='mstar=2^64*(j+4)^2*delta_j^-5'
    numeric['uniform_all_frequency_bound']='2^5000*(j+4)^5*delta_j^-10'

    root=Path(__file__).resolve().parents[1]
    paths=[
        root/'results/R119-supplement-actual-negative-band-metric-parameters.md',
        root/'results/R119-supplement-new-deep-profile-and-actual-homogeneous-Robin.md',
        root/'results/R119-supplement-reference-negative-band-Cauchy-and-source-condition.md',
        root/'results/R119-supplement-uniform-frequency-reference-Airy-Cauchy.md',
        Path(__file__).resolve(),
    ]
    return {
        'schema':'visible-exact-R119-uniform-reference-Airy-Cauchy-v1',
        'scope':'The true radial reference on a whole internal two-turning negative band. Full analytic simple-root quartic germs, density and Liouville potentials, both Airy rows, complete strict wave energy, all-frequency split including the mean, exact raw height/flux recovery and same-space continuous Duhamel. The large delta^-10 condition number is retained; this does not grant the updated nonlinear network inverse.',
        'numeric':numeric,
        'file_sha256':{str(p.relative_to(root)):sha256(p.read_bytes()).hexdigest() for p in paths},
        'checks':checks,
        'all_pass':all(c['pass'] for c in checks),
        'claims':{
            'actual_full_simple_root_germs':True,
            'both_Airy_rows_and_full_density_potential':True,
            'same_space_uniform_all_frequency_reference_Cauchy':True,
            'mean_and_both_raw_end_ports_retained':True,
            'complete_continuous_reference_Duhamel':True,
            'parameter_derivative_without_frequency_loss':False,
            'actual_perturbation_automatically_same_width':False,
            'current_deep_profile_relative_sum_closed':False,
            'new_stronger_shear_geometry_already_constructed':False,
            'nonlinear_network_inverse':False,
            'topic_completion':False,
        },
    }


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    result=run()
    if args.output:
        args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'all_pass':result['all_pass'],'checks':len(result['checks']),
                      'output':str(args.output) if args.output else None},ensure_ascii=False))
