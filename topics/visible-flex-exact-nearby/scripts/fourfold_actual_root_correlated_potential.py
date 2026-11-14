#!/usr/bin/env python3
"""Complete same-root potential bound after exact first-order correlation.

Uses all degree-80/K650 seven-field coefficients, their complete true-family
errors and closed joint boundary cells.  No coefficient uncertainty is
silently set to zero: true first two root identities justify deflation and
the full analytic error of that operation is paid explicitly.
"""
from __future__ import annotations
import argparse, math, time
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import acb, arb, ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_bulk_box import CBox, zeros, DirectedFFT, arb_box
from fourfold_phase_root_fourier_fit import save, sha, stored
from fourfold_subprincipal_root_parameter_transfer import load_transferred
from fourfold_negative_collar_root_fourier_budget import record
from fourfold_negative_canonical_cancellation_chart import checked


def modulus(z):
    return arb(float(np.max(z.magnitude_upper()))).upper()


def falling(n, order):
    return math.factorial(n)//math.factorial(n-order)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--fields',type=Path,default=Path('notes/2026-11-13-R106-seven-field-full-parameter-transfer.json'))
    ap.add_argument('--old-potential',type=Path,default=Path('notes/2026-11-13-negative-root-complete-potential-density.json'))
    ap.add_argument('--two-sided-domain',type=Path,default=Path('notes/2026-11-13-root-twosided-canonical-domain.json'))
    ap.add_argument('--rho-radius',type=Fraction,default=Fraction(27,100000))
    ap.add_argument('--physical-strip',type=Fraction,default=Fraction(11,5000))
    ap.add_argument('--start-strip',type=Fraction,default=Fraction(3,2000))
    ap.add_argument('--radial-angles',type=int,default=128)
    ap.add_argument('--angles',type=int,default=2048)
    ap.add_argument('--bits',type=int,default=320)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args()
    if a.out.exists():
        raise ValueError('new actual correlated-potential output required')
    ctx.prec=a.bits
    tick=time.monotonic()
    d,rows,scale=load_transferred(a.fields)
    old=checked(a.old_potential,'fourfold_negative_root_complete_potential_density.py')
    domain=checked(a.two_sided_domain,'fourfold_root_twosided_canonical_domain.py')
    if old['input_path']!=str(a.fields) or old['input_sha256']!=sha(a.fields):
        raise ValueError('old exact removable quotient uses different full fields')
    if domain['inputs'].get(str(a.old_potential))!=sha(a.old_potential):
        raise ValueError('two-sided chart is not the same exact root chart')
    for key in ('center_object_sha256','origin_inputs_sha256','direction_sha256',
                'exact_center_parameter','exact_parameter_interval'):
        if not d['identity'][key]==old['identity'][key]==domain['identity'][key]:
            raise ValueError('whole actual root family differs: '+key)
    if d['root']!=old['root'] or d['root']!=domain['true_root']:
        raise ValueError('true moving root differs')
    if not old['removable_order_two']:
        raise ValueError('already proved actual root removability is required')
    R,S,S1=map(exact_arb,(a.rho_radius,a.physical_strip,a.start_strip))
    R0=exact_arb(Fraction(d['working_rho_radius']))
    S0=exact_arb(Fraction(d['working_physical_angle_strip']))
    if not 0<R<R0 or not 0<S1<S<S0:
        raise ValueError('complete analytic coefficient margins are missing')
    Nr,Nt=a.radial_angles,a.angles
    if Nr&(Nr-1) or Nt&(Nt-1) or Nr<=d['degree']+1 or Nt<=2*d['K']:
        raise ValueError('insufficient full finite evaluation grids')
    errors={name:stored(d['complete_approximant_errors'][name]['complete_sup_error']).upper()
            for name in ('G','q','Sreg','Ltheta','U0','U1')}
    # W=G+U0/8+rho*U1/4 has true zero constant and linear Taylor terms.
    # Keep the entire finite polynomial of degree degree+1, then deflate.
    # Its approximate constant/linear coefficients are discarded only with
    # the full error bound for E-E(0)-rho*E_rho(0).
    wrows=[]
    max_degree=max(len(rows['G']),len(rows['U0']),len(rows['U1'])+1)
    for n in range(max_degree):
        row={}
        for name,factor,index in (('G',acb(1),n),('U0',acb(1)/8,n),
                                  ('U1',acb(scale)/4,n-1)):
            if 0<=index<len(rows[name]):
                for k,c in rows[name][index].items():
                    row[k]=row.get(k,acb(0))+factor*c
        wrows.append(row)
    rows['W2']=[{k:c/(scale*scale) for k,c in row.items()} for row in wrows[2:]]
    error_w=(errors['G']+errors['U0']/8+R0*errors['U1']/4).upper()
    errors['W2']=(error_w/(R0*R0*(1-R/R0))).upper()
    specs=(
        ('W2','W2',0,0),('q','q',0,0),('q_rho','q',1,0),
        ('q_theta','q',0,1),('q_rho_theta','q',1,1),('q_theta_theta','q',0,2),
        ('S_theta','Sreg',0,1),('Lt','Ltheta',0,0),('Lt_theta','Ltheta',0,1),
        ('U','U0',0,0),('U_rho','U0',1,0),('U_theta','U0',0,1),
        ('U_rho_rho','U0',2,0),('U_rho_theta','U0',1,1),('U_theta_theta','U0',0,2),
        ('U1','U1',0,0),('U1_rho','U1',1,0),('U1_theta','U1',0,1))
    radial_gap=arb.pi()/Nr
    angular_gap=arb.pi()/Nt
    fft=DirectedFFT()
    fields={}
    movement={}
    tails={}
    # One field at a time keeps the shared executor's peak allocation small.
    for name,base,ar,at in specs:
        data=zeros((Nr,Nt))
        fee=arb(0)
        for n,row in enumerate(rows[base]):
            if n<ar:
                continue
            radial=(R/scale)**n*falling(n,ar)/(R**ar)
            for k,c in row.items():
                k=int(k)
                z=c*radial*(-4*k*S).exp()*(acb(0,4*k)**at)
                data[(n-ar)%Nr,k%Nt]=CBox.from_acb(z)
                fee+=abs(z).upper()*((n-ar)*radial_gap+abs(k)*angular_gap)
        tail=(errors[base]*math.factorial(ar)*math.factorial(at)
              /((R0-R)**ar*(S0-S)**at))
        data=fft.fft(data,inverse=True)*Nr
        data=fft.fft(data,axis=1,inverse=True)*Nt
        fields[name]=data.pad(arb_box((fee+tail).upper()))
        movement[name]=fee.upper()
        tails[name]=tail.upper()
        print(dict(field=name,elapsed_seconds=time.monotonic()-tick),flush=True)
    U,Ur,Ut,Urr,Urt,Utt=(fields[n] for n in
        ('U','U_rho','U_theta','U_rho_rho','U_rho_theta','U_theta_theta'))
    q,qr,qt,qrt,qtt=(fields[n] for n in
        ('q','q_rho','q_theta','q_rho_theta','q_theta_theta'))
    U1,U1r,U1t=(fields[n] for n in ('U1','U1_rho','U1_theta'))
    Ulo=arb(float(np.min(U.real.lo))).lower()
    if not Ulo>0:
        raise ValueError('true U0 real part is not separated on the full boundary')
    k=1/(2*U)
    kt=-Ut/(2*U*U)
    C=-(Ur+q*Ut)/U-qt
    Cr=-(Urr+qr*Ut+q*Urt)/U+(Ur+q*Ut)*Ur/(U*U)-qrt
    Ct=-(Urt+qt*Ut+q*Utt)/U+(Ur+q*Ut)*Ut/(U*U)-qtt
    T=fields['S_theta']-U1r/2-(qt*U1+q*U1t)/2
    D=kt*fields['Lt']+k*fields['Lt_theta']
    MC,MCr,MCt,Mq,Mk,MU,MW2,MT,MD=map(modulus,
        (C,Cr,Ct,q,k,U,fields['W2'],T,D))
    gates=[]
    def gate(name,ok):
        gates.append(dict(name=name,passed=bool(ok)))
        if not ok:
            raise ValueError(name)
    movement_flow=(2*Mq*R+arb(2)/3*Mk*R**(arb(3)/2)).upper()
    margin=(S-S1-movement_flow).lower()
    gate('all nested signed and common true paths stay in the full coefficient bidisk',margin>0)
    CR=MC*R
    e=(CR.exp()-1).upper()
    gate('both signed characteristic products and the true Delta logarithm are separated',e<arb(1)/4)
    I2=((MCr+Mq*MCt)/2+arb(2)/5*Mk*MCt*R.sqrt()).upper()
    EF=(CR.exp()*I2+(CR.exp()-1-CR)/(R*R)).upper()
    ED=(arb(3)/7*EF+arb(6)/35*Mq*MCt).upper()
    P2=(2*EF*(1+R*MC)+MC*MC+R*R*EF*EF).upper()
    D2=(2*ED+arb(9)/25*MC*MC+arb(6)/5*R*MC*ED+R*R*ED*ED).upper()
    ER=((2*CR).exp()*(D2+(1+arb(4)/5*R*MC)*P2+arb(8)/5*MC*MC)).upper()
    EH=(Mk*MW2+MCr/4+Mk*MT+R*Mk*MD/2).upper()
    ratio=(4*CR).exp().upper()
    numerator2=(EH*ratio+MC*MC/5+(R*MC/4+arb(5)/16)*ER).upper()
    MV=(numerator2/(1-e)**(arb(4)/3)).upper()
    MW=(MV+5050).upper()
    path=domain['inverse_path_bounds']
    initial=stored(path['initial_real_absolute_rho_upper']).upper()
    radial_move=stored(path['full_complex_rho_movement']).upper()
    angular_move=stored(path['full_complex_theta_movement']).upper()
    gate('same exact two-sided fixed canonical inverse fits inside the new smaller physical disk',initial+radial_move<R)
    gate('same exact two-sided inverse angular lift lies in the paid new characteristic strip',angular_move<S1)
    H=exact_arb(Fraction(domain['canonical_real_half_height']))
    eps=exact_arb(Fraction(domain['canonical_complex_radial_halo']))
    eta=(MW*H*H/2).upper()
    gate('complete shifted-Airy negative height Volterra remains a contraction',eta<1)
    dirichlet_fee=(MV*H*H/arb.pi()**2).upper()
    gate('actual positive finite-collar zero-two-trace form remains coercive',dirichlet_fee<1)
    oldV=stored(old['complete_moduli']['full_canonical_potential_pullback']).upper()
    out=dict(kind='actual_complete_root_correlated_first_order_potential',
        complete=True,proved=True,source_sha256=sha(__file__),bits=a.bits,
        inputs={str(p):sha(p) for p in (a.fields,a.old_potential,a.two_sided_domain)},
        identity=d['identity'],root=d['root'],
        rho_radius=str(a.rho_radius),physical_field_strip=str(a.physical_strip),
        physical_characteristic_start_strip=str(a.start_strip),
        radial_phase_cells=Nr,angular_cells=Nt,
        exact_original_radial_degree=d['degree'],exact_W_radial_degree=max_degree-1,
        exact_deflated_W_radial_degree=len(rows['W2'])-1,
        complete_positive_fourier_modes=d['K'],
        exact_root_identities=[
            'F_sigma=1+rho*C0+rho^2*E_sigma',
            'Delta=1+(3/5)*rho*C0+rho^2*E_Delta',
            'Delta^2/(F_plus*F_minus)=1-(4/5)*rho*C0+rho^2*E_ratio',
            'W=G+U0/8+rho*U1/4 has W(0)=W_rho(0)=0 for the true complete fields',
            'H=rho*C0/4+rho^2*E_H',
            'N/rho^2=E_H*Delta^2/(F_plus*F_minus)-C0^2/5+(rho*C0/4+5/16)*E_ratio'],
        exact_H_remainder='(H-rho*C0/4)/rho^2=k*W/rho^2+(C-C0)/(4*rho)+k*T+(rho/2)*k*(k*Ltheta)_theta',
        true_zero_identity_justification='The already proved exact local canonical analyticity gives N_rho(0)=0; the independently derived characteristic first jets give H_rho(0)=C0/4 and hence W_rho(0)=0. This is a qualitative exact identity, not use of the new numerical bound.',
        W_deflation=dict(complete_original_approximation_error=record(error_w),
            complete_deflated_error=record(errors['W2']),
            formula='epsilon_W/[R0^2*(1-R/R0)], obtained by subtracting both Taylor coefficients of the complete analytic error',
            arbitrary_coefficient_ball_set_to_zero=False),
        complete_field_moduli={name:record(value) for name,value in dict(
            C=MC,C_rho=MCr,C_theta=MCt,q=Mq,kstar=Mk,U0=MU,
            W_over_rho_squared=MW2,T=MT,D=MD).items()},
        complete_correlated_bounds={name:record(value) for name,value in dict(
            logarithmic_F_second_remainder=I2,F_second_remainder=EF,
            Delta_second_remainder=ED,Fproduct_second_remainder=P2,
            Delta_squared_second_remainder=D2,ratio_second_remainder=ER,
            H_second_remainder=EH,Delta_minus_one=e,ratio_modulus=ratio,
            full_numerator_over_rho_squared=numerator2,
            full_canonical_potential=MV,full_shifted_5050_residual=MW,
            previous_potential_bound=oldV,improvement_factor=oldV/MV).items()},
        U0_real_lower=record(Ulo),
        nested_characteristic_angle_movement=record(movement_flow),
        complete_characteristic_angle_margin=record(margin),
        full_Cauchy_derivative_tails={name:record(v) for name,v in tails.items()},
        full_finite_cell_movements={name:record(v) for name,v in movement.items()},
        exact_complete_canonical_domain=domain['canonical_domain'],
        canonical_real_half_height=domain['canonical_real_half_height'],
        canonical_complex_angle_strip=domain['canonical_complex_angle_strip'],
        canonical_complex_radial_halo=domain['canonical_complex_radial_halo'],
        new_domain_margins=dict(radial=record((R-initial-radial_move).lower()),
                               characteristic_angle=record((S1-angular_move).lower())),
        actual_quarter_circle_frequency=domain['actual_quarter_circle_frequency'],
        canonical_potential_derivative=dict(bound=record((MV/eps).upper()),
            domain='real xi in [-height,height], full paid complex angle strip; no claim on the radial halo boundary'),
        complete_negative_height_Volterra=dict(norm=record(eta),
            resolvent=record((1/(1-eta)).upper()),
            reference='5050, both full shifted-Airy columns and independent mean cosine/sine'),
        complete_positive_finite_zero_two_trace=dict(relative_fee=record(dirichlet_fee),
            gradient_coercivity=record((1-dirichlet_fee).lower()),
            ordinary_L2_inverse=record((H*H/arb.pi()**2/(1-dirichlet_fee)).upper())),
        all_modes_mean_and_true_parameters_retained=True,
        full_closed_joint_cells_and_all_analytic_errors_retained=True,
        original_source_Piola_height_and_conormal_unchanged=True,
        different_target_or_reference_used=False,
        full_returned_Rstar_recomputed=False,finite_head_inverse_proved=False,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_subprincipal_root_parameter_transfer.py',
            'fourfold_subprincipal_root_regularized_fft_v2.py',
            'fourfold_phase_beta_bulk_box.py','fourfold_phase_beta_bulk_interval.py',
            'fourfold_phase_root_fourier_fit.py','fourfold_negative_collar_root_fourier_budget.py',
            'fourfold_negative_canonical_cancellation_chart.py')},
        gates=gates,
        scope='Complete same-family correlated root potential on the already proved full two-sided canonical product domain. The old physical source, height, conormal, all mean and regular port conventions remain exact. No returned Rstar, finite head, or full nearby surface existence is inferred.',
        seconds=time.monotonic()-tick)
    save(a.out,out)
    print(dict(complete=True,out=str(a.out),sha256=sha(a.out),
        moduli=out['complete_field_moduli'],bounds=out['complete_correlated_bounds'],
        seconds=out['seconds']),flush=True)


if __name__=='__main__':
    main()

