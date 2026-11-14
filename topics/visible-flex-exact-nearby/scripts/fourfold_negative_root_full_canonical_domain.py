#!/usr/bin/env python3
"""Actual fixed-xi complex domain through the root-to-physical-cut collar."""
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
    p.add_argument('--real-cut',type=Path,default=Path('notes/2026-11-13-negative-canonical-full-real-cut.json'))
    p.add_argument('--frequency',type=Path,default=Path('notes/2026-11-13-negative-cancellation-R43-window8.json'))
    p.add_argument('--height',type=Fraction,default=Fraction(1,4000))
    p.add_argument('--canonical-angle-strip',type=Fraction,default=Fraction(1,40000))
    p.add_argument('--canonical-radial-halo',type=Fraction,default=Fraction(1,100000))
    p.add_argument('--bits',type=int,default=320)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise ValueError('new full canonical-domain report required')
    ctx.prec=a.bits;tick=time.monotonic()
    d=checked(a.potential,'fourfold_negative_root_complete_potential_density.py')
    if sha(d['input_path'])!=d['input_sha256']:
        raise ValueError('actual complete seven-field input changed')
    cut=checked(a.real_cut,'fourfold_negative_canonical_full_real_cut.py')
    q=checked(a.frequency,'fourfold_negative_collar_cancellation_R43.py')
    if not d['identity']==cut['identity']==q['identity']:
        raise ValueError('actual complete root families differ')
    R=exact_arb(Fraction(d['rho_radius']))
    S1=exact_arb(Fraction(d['physical_characteristic_start_strip']))
    L,sigma,eps=map(exact_arb,(a.height,a.canonical_angle_strip,a.canonical_radial_halo))
    M={k:stored(v).upper() for k,v in d['complete_moduli'].items()}
    C,Q,U=M['C'],M['q'],M['U0'];Ulo=stored(d['U0_real_lower']).lower()
    e=M['Delta_minus_one'];CR=C*R
    Ptheta=(2*Ulo*(1-e)).lower()
    Jlo=(2*Ulo*(-arb(7)/3*CR).exp()).lower()
    # Full Delta error on the S1 strip, differentiated only on its half strip.
    Xtheta=(R*arb(2)/3/(1-e)**(arb(1)/3)*(2*e/S1)).upper()
    P_rho=(2*Q*U*CR.exp()+R.sqrt()*e).upper()
    rho_phi=(Xtheta/Jlo).upper()
    theta_phi=((1+rho_phi*P_rho)/Ptheta).upper()
    rho_xi=(arb(4)/3*CR).exp().upper()
    theta_xi=(P_rho/Jlo).upper()
    initial_rho=(L*(arb(2)/3*CR).exp()).upper()
    movement_rho=(rho_phi*sigma+rho_xi*eps).upper()
    movement_theta=(theta_phi*sigma+theta_xi*eps).upper()
    real_rectangle=(R*(-arb(2)/3*CR).exp()).lower()
    gates=[]
    def gate(name,ok):
        gates.append(dict(name=name,passed=bool(ok)))
        if not ok:raise ValueError(name)
    gate('all earlier complete characteristic gates hold',all(g['passed'] for g in d['gates']))
    gate('the complete real rectangle contains the full requested canonical collar',0<L<real_rectangle)
    gate('the actual strict physical cut graph is strictly inside the requested collar',
        stored(cut['actual_physical_cut_canonical_graph_range'][1]).upper()<L)
    gate('the complex inverse angular derivative and Jacobian are separated',Ptheta>0 and Jlo>0)
    gate('full inverse path lifting stays inside the complete physical radial disk',initial_rho+movement_rho<R)
    gate('full inverse path lifting stays inside the paid half angular strip',movement_theta<S1/2)
    V=M['full_canonical_potential_pullback'];W=M['full_shifted_5050_residual_pullback']
    contraction=(L*L*W/2).upper()
    gate('full-frequency shifted-Airy height Volterra is a contraction',contraction<arb(1)/40)
    qlo=stored(q['actual_quarter_circle_frequency'][0]).lower()
    qhi=stored(q['actual_quarter_circle_frequency'][1]).upper()
    gate('same actual full canonical quarter-period frequency retained',qlo>4 and qhi>=qlo)
    out=dict(kind='actual_complete_negative_root_fixed_canonical_domain',
        complete=True,proved=True,source_sha256=sha(__file__),bits=a.bits,
        inputs={str(p):sha(p) for p in (a.potential,a.real_cut,a.frequency)},identity=d['identity'],
        canonical_real_height=str(a.height),canonical_complex_angle_strip=str(a.canonical_angle_strip),
        canonical_complex_radial_halo=str(a.canonical_radial_halo),
        canonical_domain='dist(xi,[0,height])<=radial_halo; |Im phi|<=angle_strip; full actual quarter-period circle',
        actual_quarter_circle_frequency=[record(qlo),record(qhi)],
        inverse_path_bounds={k:record(v) for k,v in dict(
            physical_rho_radius=R,physical_half_angle_strip=S1/2,
            complex_phi_theta_lower=Ptheta,complex_Jacobian_modulus_lower=Jlo,
            complex_xi_theta_modulus=Xtheta,complex_phi_rho_modulus=P_rho,
            inverse_rho_phi=rho_phi,inverse_theta_phi=theta_phi,
            inverse_rho_xi=rho_xi,inverse_theta_xi=theta_xi,
            initial_real_rho_upper=initial_rho,full_complex_rho_movement=movement_rho,
            full_complex_theta_movement=movement_theta,
            remaining_physical_radial_margin=R-initial_rho-movement_rho,
            remaining_physical_angular_margin=S1/2-movement_theta).items()},
        full_canonical_V_modulus=record(V),full_canonical_Vxi_modulus=record((V/eps).upper()),
        full_canonical_V_bound_domain='the entire canonical product domain, including its radial halo',
        full_canonical_Vxi_bound_domain='real xi in [0,height], |Im phi|<=angle_strip; no derivative claim at the radial halo boundary',
        full_canonical_shifted_5050_residual_modulus=record(W),
        full_height_L2_Volterra_norm=record(contraction),
        full_height_L2_Volterra_resolvent=record((1/(1-contraction)).upper()),
        all_actual_Fourier_modes_mean_and_parameter_values_retained=True,
        full_physical_cut_graph_contained=True,mean_reference='cos(sqrt(5050)*xi) and sin(sqrt(5050)*xi)/sqrt(5050)',
        nonzero_reference='Ai(-|q*n|^(2/3)*xi-5050*|q*n|^(-4/3)), Bi of the same full negative argument',
        gates=gates,complete_high_Sobolev_Airy_frame_bound_proved=False,
        full_graph_trace_strong_gluing_proved=False,full_returned_Rstar_proved=False,
        scope='A complete canonical product neighborhood with a full V bound; V_xi is bounded on the real radial segment [0,height] and the same complex angle strip. The all-frequency L2 height Volterra contraction is complete. Higher Sobolev, full momentum, ordinary-source, graph trace and normal-form bounds need their explicit consumers.',
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_negative_canonical_cancellation_chart.py','fourfold_negative_collar_root_fourier_budget.py',
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_root_fourier_fit.py')},
        seconds=time.monotonic()-tick)
    save(a.out,out)
    print(dict(complete=True,out=str(a.out),sha256=sha(a.out),path=out['inverse_path_bounds'],
        V=out['full_canonical_V_modulus'],Vxi=out['full_canonical_Vxi_modulus'],
        height_Volterra=out['full_height_L2_Volterra_norm']),flush=True)

if __name__=='__main__':main()
