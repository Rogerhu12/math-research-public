#!/usr/bin/env python3
"""Actual enlarged negative canonical inverse using the exact F_sigma cancellation.

Consumes complete seven-field/cancellation and grounded log-density inputs.
Every bound is uniform in the true moving root and the entire parameter box.
The complete potential disk is a chart input, not a full return inverse.
"""
from __future__ import annotations
import argparse,time
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_root_fourier_fit import read,save,sha,stored
from fourfold_negative_collar_root_fourier_budget import record


def checked(path,source_name):
    d=read(path)
    if not d.get('complete') or not d.get('proved'):
        raise ValueError('complete actual geometry certificate required '+str(path))
    if d['source_sha256']!=sha(Path(__file__).with_name(source_name)):
        raise ValueError('actual scientific producer changed '+source_name)
    for name,digest in d.get('dependencies',{}).items():
        if sha(Path(__file__).with_name(name))!=digest:
            raise ValueError('actual scientific dependency changed '+name)
    for name,digest in d.get('inputs',{}).items():
        if sha(name)!=digest:raise ValueError('actual scientific input changed '+name)
    return d


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--cancellation',type=Path,default=Path('notes/2026-11-13-negative-characteristic-cancellation-bidisk.json'))
    ap.add_argument('--fields',type=Path,default=Path('notes/2026-11-13-R106-seven-field-full-parameter-transfer.json'))
    ap.add_argument('--log-density',type=Path,default=Path('notes/2026-11-13-negative-canonical-log-density-bidisk.json.gz'))
    ap.add_argument('--inverse-radius',type=Fraction,default=Fraction(1,60000))
    ap.add_argument('--physical-start-strip',type=Fraction,default=Fraction(3,2000))
    ap.add_argument('--bits',type=int,default=320)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args()
    if a.out.exists():raise ValueError('new actual chart output required')
    ctx.prec=a.bits;tick=time.monotonic()
    c=checked(a.cancellation,'fourfold_negative_characteristic_cancellation.py')
    g=checked(a.log_density,'fourfold_negative_canonical_log_density.py')
    f=checked(a.fields,'fourfold_subprincipal_root_parameter_transfer.py')
    if c['inputs'].get(str(a.fields))!=sha(a.fields):
        raise ValueError('cancellation and U0 modulus must use the same actual fields')
    for key in ('center_object_sha256','origin_inputs_sha256','direction_sha256',
                'exact_center_parameter','exact_parameter_interval'):
        if not c['identity'][key]==g['identity'][key]==f['identity'][key]:
            raise ValueError('actual moving-root families differ '+key)
    R,S=exact_arb(Fraction(c['rho_radius'])),exact_arb(Fraction(c['physical_angle_strip']))
    M={k:stored(v).upper() for k,v in c['complete_complex_moduli'].items()}
    C,Q,K=M['C'],M['q'],M['kstar']
    U=stored(f['complete_true_moduli_on_working_bidisk']['U0']).upper()
    logU=stored(g['complete_true_moduli']['logU']).upper()
    m=stored(c['root_Y0_prime_real_lower']).lower()
    r=exact_arb(a.inverse_radius);theta=exact_arb(a.physical_start_strip)
    gates=[]
    def gate(name,ok):
        gates.append(dict(name=name,passed=bool(ok)))
        if not ok:raise ValueError(name)
    gate('whole transferred U0 modulus contains the cancellation bidisk',
         R<=exact_arb(Fraction(f['working_rho_radius'])) and S<=exact_arb(Fraction(f['working_physical_angle_strip'])))
    gate('actual grounded logarithm contains the complete characteristic chart',
         R<=exact_arb(Fraction(g['rho_radius'])) and S<=exact_arb(Fraction(g['physical_angle_strip'])))
    movement=(2*Q*R+arb(2)/3*K*R**(arb(3)/2)).upper()
    margin=(S-theta-movement).lower()
    gate('all nested common and signed characteristic paths remain inside the true coefficient bidisk',margin>0)
    eR=(C*R).exp()-1
    e2=(2*C*r).exp()-1
    gate('full deflated root quotient has its actual positive logarithm',eR<arb(1)/4)
    gate('inverse search domain lies inside the complete characteristic disk',0<2*r<R)
    b=(m*theta/4).lower()
    gate('true root-angle inverse target strip is positive',b>0)
    # Exact derivative, with F_sigma=k*T_sigma,theta and |F_sigma-1| <= exp(C|rho|)-1.
    Mphi=(2*Q*U*(2*C*r).exp()+(2*r).sqrt()*e2).upper()
    Ephi=(2*r*Mphi).upper()
    phi_row=(2*r*Mphi/b).upper()
    # Delta-1 vanishes at rho=0. Complete outer-disk Cauchy gives this derivative.
    Deltar=(eR/R/(1-2*r/R)**2).upper()
    power_diff=(arb(2)/3*e2/(1-e2)**(arb(1)/3)).upper()
    power_derivative=(arb(2)/3/(1-e2)**(arb(1)/3)).upper()
    Ex=(2*r*power_diff).upper()
    # Radial derivative plus angular Cauchy on the full 4b -> 2b strip.
    xi_row=(2*power_diff+2*r*power_derivative*Deltar).upper()
    kappa=max(phi_row,xi_row)
    gate('global holomorphic inverse weighted derivative contraction',kappa<arb(1)/2)
    gate('global inverse fixed point preserves its radial disk',Ex<r)
    gate('global inverse fixed point preserves its angular disk',Ephi<b)
    ML=(logU/2-(1-e2).log()/3).upper()
    rV=r/2;sV=b/2
    MV=(ML*(4+ML)*(1/r**2+rV/b**2)).upper()
    report=dict(kind='actual_negative_canonical_chart_from_characteristic_cancellation',
        complete=True,proved=True,source_sha256=sha(__file__),bits=a.bits,
        inputs={str(p):sha(p) for p in (a.cancellation,a.fields,a.log_density)},
        identity=c['identity'],root=c['root'],exact_negative_characteristic_coordinates=True,
        characteristic_definition='D_sigma=partial_s+(2*s*q-2*sigma*s*s*k)*partial_theta; T_sigma(0)=Y0; Delta=3*(T_plus-T_minus)/(4*s^3); xi=rho*Delta^(2/3); phi=(T_plus+T_minus)/2',
        exact_negative_cancellation='D_sigma(k*T_sigma_theta)=2*s*C*(k*T_sigma_theta), with initial value 1',
        exact_phi_radial_derivative='phi_rho=-q*(F_plus+F_minus)/(2*k)+(sqrt(rho)/2)*(F_plus-F_minus)',
        analytic_domain={'inverse_target_rho_radius':str(a.inverse_radius),
                         'physical_start_strip':str(a.physical_start_strip)},
        full_analytic_potential_radial_disk=record(rV),
        complete_potential_analytic_strip=record(sV),
        larger_real_negative_collar_height=record(rV/2),
        larger_real_collar_true_V_bound=record(MV),
        larger_real_collar_true_Vxi_bound=record((2*MV/rV).upper()),
        chart_bounds={k:record(v) for k,v in dict(
            characteristic_rho_radius=R,physical_start_strip=theta,
            nested_characteristic_angle_movement=movement,remaining_complete_angle_margin=margin,
            complete_C_modulus=C,complete_q_modulus=Q,complete_k_modulus=K,
            complete_inverse_k_modulus=2*U,full_deflated_difference_error=eR,
            inverse_search_deflated_difference_error=e2,
            full_search_phi_rho_modulus=Mphi,full_search_Delta_rho_modulus=Deltar,
            full_search_phi_minus_Y_modulus=Ephi,full_search_xi_minus_rho_modulus=Ex,
            inverse_xi_row_norm=xi_row,inverse_phi_row_norm=phi_row,
            root_angle_real_derivative_lower=m,
            canonical_inverse_target_radial_disk=r,canonical_inverse_target_angle_strip=b,
            canonical_inverse_contraction=kappa,log_canonical_density_modulus=ML,
            full_complex_potential_modulus_before_root_Taylor=MV).items()},
        gates=gates,all_modes_all_parameters_and_all_closed_cells_retained=True,
        both_characteristic_branches_and_the_mean_retained=True,
        all_radial_and_angular_tails_retained=True,
        full_negative_R43_operator_bound_proved=False,
        complete_returned_R_star_proved=False,positive_Ai_contact_proved=False,
        physical_source_frame_gluing_proved=False,README_completion_proved=False,
        scope='A complete enlarged actual negative canonical inverse and full analytic potential disk. Operator propagation, physical source/frame gluing, and the full returned inverse require their separate consumers.',
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_root_fourier_fit.py',
            'fourfold_negative_collar_root_fourier_budget.py')},
        seconds=time.monotonic()-tick)
    save(a.out,report)
    print(dict(complete=True,out=str(a.out),sha256=sha(a.out),bounds=report['chart_bounds']),flush=True)

if __name__=='__main__':main()
