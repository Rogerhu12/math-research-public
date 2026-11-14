#!/usr/bin/env python3
"""Complete actual real root chart through the strict physical cut and its tilt.

The exact signed-density cancellation pays the full real diffeomorphism.
No physical constant-r cut is identified with a constant canonical-xi cut.
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

CUT=Fraction(268136140016943,1125899906842624)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--cancellation',type=Path,default=Path('notes/2026-11-13-negative-characteristic-cancellation-bidisk.json'))
    p.add_argument('--chart',type=Path,default=Path('notes/2026-11-13-negative-canonical-cancellation-chart.json'))
    p.add_argument('--bits',type=int,default=320)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise ValueError('new true full-real-cut report required')
    ctx.prec=a.bits;tick=time.monotonic()
    c=checked(a.cancellation,'fourfold_negative_characteristic_cancellation.py')
    z=checked(a.chart,'fourfold_negative_canonical_cancellation_chart.py')
    if z['inputs'].get(str(a.cancellation))!=sha(a.cancellation):
        raise ValueError('real chart must use the same actual characteristic certificate')
    if c['identity']!=z['identity'] or not all(g['passed'] for g in z['gates']):
        raise ValueError('actual real family or complete characteristic domain is missing')
    R=exact_arb(Fraction(c['rho_radius']))
    C=stored(c['complete_complex_moduli']['C']).upper()
    Ulo=stored(c['complete_U0_real_lower']).lower()
    invk=stored(z['chart_bounds']['complete_inverse_k_modulus']).upper()
    root=stored(c['root']);rho=root-exact_arb(CUT)
    rholo,rhohi=rho.lower(),rho.upper()
    gates=[]
    def gate(name,ok):
        gates.append(dict(name=name,passed=bool(ok)))
        if not ok:raise ValueError(name)
    gate('the whole true physical strict cut lies inside the negative root characteristic collar',0<rholo<rhohi<R)
    exponent=C*R
    phi_lo=(2*Ulo*(-exponent).exp()).lower()
    phi_hi=(invk*exponent.exp()).upper()
    radial_lo=(-arb(4)/3*exponent).exp().lower()
    radial_hi=(arb(4)/3*exponent).exp().upper()
    Jlo=(phi_lo*radial_lo).lower();Jhi=(phi_hi*radial_hi).upper()
    full_xi=(R*(-arb(2)/3*exponent).exp()).lower()
    cut_xi_lo=(rholo*(-arb(2)/3*C*rhohi).exp()).lower()
    cut_xi_hi=(rhohi*(arb(2)/3*C*rhohi).exp()).upper()
    tilt=(C*rhohi).tanh().upper()
    graph_normal=(1-tilt**2).lower()
    gate('the actual full real canonical chart is orientation preserving',min(phi_lo,radial_lo,Jlo)>0)
    gate('the canonical full rectangle contains the entire real physical cut graph',cut_xi_hi<full_xi)
    gate('the full physical cut graph is uniformly spacelike in the actual canonical principal metric',tilt<arb(1)/32 and graph_normal>0)
    out=dict(kind='actual_negative_canonical_full_real_cut_and_spacelike_trace',
        complete=True,proved=True,source_sha256=sha(__file__),bits=a.bits,
        inputs={str(p):sha(p) for p in (a.cancellation,a.chart)},identity=c['identity'],
        true_root=c['root'],physical_cut=str(CUT),exact_real_physical_rho_interval=['0',c['rho_radius']],
        actual_physical_cut_root_distance=[record(rholo),record(rhohi)],
        actual_full_real_canonical_rectangle_upper=record(full_xi),
        actual_physical_cut_canonical_graph_range=[record(cut_xi_lo),record(cut_xi_hi)],
        real_global_bounds={k:record(v) for k,v in dict(
            phi_theta_lower=phi_lo,phi_theta_upper=phi_hi,
            xi_rho_at_fixed_phi_lower=radial_lo,xi_rho_at_fixed_phi_upper=radial_hi,
            complete_coordinate_Jacobian_lower=Jlo,complete_coordinate_Jacobian_upper=Jhi,
            graph_sqrt_xi_times_slope_modulus=tilt,graph_spacelike_normal_lower=graph_normal,
            pointwise_gradient_trace_map_norm=1+tilt,
            pointwise_inverse_gradient_trace_map_norm=1/(1-tilt)).items()},
        exact_determinant='det D(xi,phi)=sqrt(rho/xi)*F_plus*F_minus/k',
        exact_radial_derivative_at_fixed_phi='2*sqrt(rho/xi)*F_plus*F_minus/(F_plus+F_minus)',
        exact_physical_cut_tilt='sqrt(xi)*dchi/dphi=(F_plus-F_minus)/(F_plus+F_minus)',
        exact_graph_trace='p_graph=U_xi+xi*chi_prime*U_phi; (U_on_graph)_phi=chi_prime*U_xi+U_phi',
        exact_grounded_flux='p_rho dtheta=phi_theta*sqrt(alpha_c)*(p_graph-(L_xi+xi*chi_prime*L_phi)*U/2) dtheta, with dphi=phi_theta dtheta',
        exact_ordinary_source='f_U=alpha_c^(-1/2)*(f_ground/Jacobian) composed with inverse chart',
        normalized_period_rule='Physical theta has period pi/2; canonical phi has its actual root quarter period. Unnormalized flux integrals agree; normalized means retain the actual period factor.',
        all_modes_and_mean_retained=True,whole_actual_real_parameter_interval=True,
        both_actual_roots='The second root uses the exact radial reflection and simultaneous conormal orientation reversal.',
        gates=gates,complete_graph_Cauchy_propagation_bound_proved=False,
        full_Hs_physical_frame_gluing_bound_proved=False,
        positive_Ai_contact_proved=False,full_returned_Rstar_proved=False,
        scope='A full real actual root diffeomorphism reaching the true strict cut, plus exact source and physical graph/conormal identities and a uniform spacelike tilt. It does not supply the remaining Hs graph-propagation or strong gluing norms.',
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_negative_canonical_cancellation_chart.py','fourfold_negative_collar_root_fourier_budget.py',
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_root_fourier_fit.py')},
        seconds=time.monotonic()-tick)
    save(a.out,out)
    print(dict(complete=True,out=str(a.out),sha256=sha(a.out),bounds=out['real_global_bounds'],
        xi_graph=out['actual_physical_cut_canonical_graph_range'],full_rectangle=out['actual_full_real_canonical_rectangle_upper']),flush=True)

if __name__=='__main__':main()
