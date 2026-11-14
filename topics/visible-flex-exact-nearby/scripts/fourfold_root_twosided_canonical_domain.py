#!/usr/bin/env python3
"""The same exact root canonical chart on both real sides of the true root.

The negative-chart complete physical bidisk is consumed without recomputing
native fields.  A separate real-conjugacy argument, stated in the companion
proof, supplies the positive-side real inverse.  No negative-side Sonin or
Volterra estimate is transferred to the elliptic side.
"""
from __future__ import annotations
import argparse,time
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_root_fourier_fit import save,sha,stored
from fourfold_negative_collar_root_fourier_budget import record
from fourfold_negative_canonical_cancellation_chart import checked


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--potential',type=Path,default=Path('notes/2026-11-13-negative-root-complete-potential-density.json'))
    p.add_argument('--negative-domain',type=Path,default=Path('notes/2026-11-13-negative-root-full-canonical-domain.json'))
    p.add_argument('--log-density',type=Path,default=Path('notes/2026-11-13-negative-canonical-log-density-bidisk.json.gz'))
    p.add_argument('--height',type=Fraction,default=Fraction(1,4000))
    p.add_argument('--canonical-angle-strip',type=Fraction,default=Fraction(1,40000))
    p.add_argument('--canonical-radial-halo',type=Fraction,default=Fraction(1,100000))
    p.add_argument('--bits',type=int,default=320)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise ValueError('a new two-sided domain report is required')
    ctx.prec=a.bits;tick=time.monotonic()
    d=checked(a.potential,'fourfold_negative_root_complete_potential_density.py')
    old=checked(a.negative_domain,'fourfold_negative_root_full_canonical_domain.py')
    log=checked(a.log_density,'fourfold_negative_canonical_log_density.py')
    if sha(d['input_path'])!=d['input_sha256']:
        raise ValueError('actual complete seven-field input changed')
    for key in ('center_object_sha256','origin_inputs_sha256','direction_sha256',
                'exact_center_parameter','exact_parameter_interval'):
        if not d['identity'][key]==old['identity'][key]==log['identity'][key]:
            raise ValueError('whole actual root family differs: '+key)
    R,S1=map(exact_arb,(Fraction(d['rho_radius']),Fraction(d['physical_characteristic_start_strip'])))
    H,sigma,eps=map(exact_arb,(a.height,a.canonical_angle_strip,a.canonical_radial_halo))
    M={k:stored(v).upper() for k,v in d['complete_moduli'].items()}
    C,Q,U,e=M['C'],M['q'],M['U0'],M['Delta_minus_one']
    Ulo=stored(d['U0_real_lower']).lower();CR=C*R
    Ptheta=(2*Ulo*(1-e)).lower()
    Jlo=(2*Ulo*(-arb(7)/3*CR).exp()).lower()
    Xtheta=(R*arb(2)/3/(1-e)**(arb(1)/3)*(2*e/S1)).upper()
    P_rho=(2*Q*U*CR.exp()+R.sqrt()*e).upper()
    rho_phi=(Xtheta/Jlo).upper()
    theta_phi=((1+rho_phi*P_rho)/Ptheta).upper()
    rho_xi=(arb(4)/3*CR).exp().upper()
    theta_xi=(P_rho/Jlo).upper()
    # On the positive side F_minus is conjugate to F_plus, not an independent
    # positive exponential.  Use the full complex Delta error, not the sharper
    # positive-rho average inequality from the old real-negative consumer.
    real_rectangle=(R*(1-e)**(arb(2)/3)).lower()
    initial_rho=(H/(1-e)**(arb(2)/3)).upper()
    movement_rho=(rho_phi*sigma+rho_xi*eps).upper()
    movement_theta=(theta_phi*sigma+theta_xi*eps).upper()
    phi_hi=(2*U*CR.exp()).upper()
    radial_lo=(1/rho_xi).lower()
    radial_hi=((2*CR).exp()/(1-e)**(arb(4)/3)).upper()
    Jhi=(2*U*(2*CR).exp()/(1-e)**(arb(1)/3)).upper()
    ML=(stored(log['complete_true_moduli']['logU']).upper()/2
        -(1-e).log()/3).upper()
    alpha_lo=(-ML).exp().lower();alpha_hi=ML.exp().upper()
    tau_lo=(-ML/2).exp().lower();tau_hi=(ML/2).exp().upper()
    V=M['full_canonical_potential_pullback']
    # This is the zero-two-trace Dirichlet form on the finite positive collar.
    # It says nothing about exponentially growing positive Cauchy evolution.
    dirichlet_fee=(V*H*H/(arb.pi()**2)).upper()
    gates=[]
    def gate(name,ok):
        gates.append(dict(name=name,passed=bool(ok)))
        if not ok:raise ValueError(name)
    gate('all earlier complete characteristic gates hold',all(g['passed'] for g in d['gates']))
    gate('grounded density logarithm covers the complete physical bidisk',
         R<=exact_arb(Fraction(log['rho_radius'])) and
         exact_arb(Fraction(d['physical_field_strip']))<=exact_arb(Fraction(log['physical_angle_strip'])))
    gate('the actual real-conjugate chart has separated Delta and angular derivative',0<e<arb(1)/4 and Ptheta>0 and Jlo>0)
    gate('both full real canonical rectangles fit',0<H<real_rectangle)
    gate('the same complete inverse path lifting remains inside the physical radial disk',initial_rho+movement_rho<R)
    gate('the same complete inverse path lifting remains inside the physical half angular strip',movement_theta<S1/2)
    gate('the continued actual grounded height is positive on both real sides',alpha_lo>0 and tau_lo>0)
    gate('the complete positive-collar zero-two-trace form is coercive',dirichlet_fee<arb(1)/100)
    out=dict(kind='actual_same_exact_root_canonical_chart_on_both_sides',
        complete=True,proved=True,source_sha256=sha(__file__),bits=a.bits,
        inputs={str(q):sha(q) for q in (a.potential,a.negative_domain,a.log_density)},
        identity=d['identity'],true_root=d['root'],canonical_real_half_height=str(a.height),
        canonical_complex_angle_strip=str(a.canonical_angle_strip),canonical_complex_radial_halo=str(a.canonical_radial_halo),
        canonical_domain='dist(xi,[-height,height])<=radial_halo; |Im phi|<=angle_strip; the same actual quarter-period circle',
        positive_side_coordinates='s=r-t(p)=-rho; y=-xi; phi is the same even characteristic coordinate',
        actual_quarter_circle_frequency=old['actual_quarter_circle_frequency'],
        conjugacy='For real rho<0 and real theta, F_minus=conjugate(F_plus); phi and Delta are real by their even holomorphic series in s=sqrt(rho).',
        exact_principal_density='alpha_c diag(1,-xi), alpha_c=sqrt(Ucal)*Delta^(-1/3); on y=-xi this is alpha_c diag(1,y)',
        exact_positive_operator='P_positive=-d_y^2-y*d_phi^2-V(-y,phi), obtained from the same canonical height and the positive grounded form',
        exact_positive_source='For -div(B grad w)=f_ground and w=tau*U composed with Psi_plus, P_positive U=(tau/J_plus)*f_ground composed with Psi_plus_inverse; tau=alpha_c^(-1/2).',
        exact_root_canonical_outward_conormal='p_out=-U_y=U_xi; the grounded conormal additionally contains the true height shear and density',
        inverse_path_bounds={k:record(v) for k,v in dict(
            physical_rho_radius=R,physical_half_angle_strip=S1/2,
            complex_phi_theta_lower=Ptheta,complex_Jacobian_modulus_lower=Jlo,
            complex_xi_theta_modulus=Xtheta,complex_phi_rho_modulus=P_rho,
            inverse_rho_phi=rho_phi,inverse_theta_phi=theta_phi,
            inverse_rho_xi=rho_xi,inverse_theta_xi=theta_xi,
            symmetric_real_canonical_rectangle_half_height=real_rectangle,
            initial_real_absolute_rho_upper=initial_rho,
            full_complex_rho_movement=movement_rho,full_complex_theta_movement=movement_theta,
            remaining_physical_radial_margin=R-initial_rho-movement_rho,
            remaining_physical_angular_margin=S1/2-movement_theta).items()},
        complete_real_bounds={k:record(v) for k,v in dict(
            phi_theta_lower=Ptheta,phi_theta_upper=phi_hi,
            xi_rho_at_fixed_phi_lower=radial_lo,xi_rho_at_fixed_phi_upper=radial_hi,
            Jacobian_lower=Jlo,Jacobian_upper=Jhi,
            log_alpha_modulus=ML,alpha_lower=alpha_lo,alpha_upper=alpha_hi,
            tau_lower=tau_lo,tau_upper=tau_hi).items()},
        complete_potential_modulus=record(V),
        complete_potential_first_radial_derivative_modulus=record((V/eps).upper()),
        potential_domain='entire two-sided canonical product domain including its radial halo',
        potential_radial_derivative_domain='real xi in [-height,height] with the full complex phi strip; no derivative assertion on the radial halo boundary',
        finite_positive_zero_two_trace={
            'potential_relative_fee':record(dirichlet_fee),
            'gradient_coercivity':record((1-dirichlet_fee).lower()),
            'ordinary_L2_to_L2_Dirichlet_inverse':record((H*H/(arb.pi()**2)/(1-dirichlet_fee)).upper()),
            'domain':'only the actual finite positive collar [0,height], with zero trace at both ends; every angular mode and the mean'},
        gates=gates,all_actual_modes_and_whole_parameters_retained=True,
        finite_positive_approximate_chart_used=False,positive_Cauchy_growth_bound_claimed=False,
        full_positive_cap_Ai_reflection_proved=False,full_positive_cap_source_contact_proved=False,
        full_returned_Rstar_proved=False,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_negative_canonical_cancellation_chart.py','fourfold_negative_collar_root_fourier_budget.py',
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_root_fourier_fit.py')},
        scope='The same exact analytic canonical chart and height, now with a proved real positive-side inverse and a symmetric full product domain. The finite positive zero-two-trace Dirichlet form is coercive; full cap/contact, Ai reflection, exterior regular/mean coupling and returned strong inverse remain separate.',
        seconds=time.monotonic()-tick)
    save(a.out,out)
    print(dict(complete=True,out=str(a.out),sha256=sha(a.out),
        real=out['complete_real_bounds'],path=out['inverse_path_bounds'],
        finite_positive_Dirichlet=out['finite_positive_zero_two_trace']),flush=True)


if __name__=='__main__':main()
