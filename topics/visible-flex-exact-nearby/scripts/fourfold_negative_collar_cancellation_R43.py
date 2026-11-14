#!/usr/bin/env python3
"""Complete R43 consumer for the actual cancellation-enlarged negative chart."""
from __future__ import annotations
import argparse,time
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_root_fourier_fit import read,save,sha,stored
from fourfold_negative_collar_root_fourier_budget import (
    record,validate_root,root_moment,analytic_moment)
from fourfold_negative_canonical_cancellation_chart import checked


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--v0',type=Path,default=Path('notes/2026-11-12-ci-canonical-v0-scaled-Wiener.json'))
    ap.add_argument('--v1',type=Path,default=Path('notes/2026-11-12-ci-canonical-v1-scaled-Wiener.json'))
    ap.add_argument('--chart',type=Path,default=Path('notes/2026-11-13-negative-canonical-cancellation-chart.json'))
    ap.add_argument('--collar-dyadic-power',type=int,default=129)
    ap.add_argument('--bits',type=int,default=320)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args()
    if a.out.exists() or a.collar_dyadic_power<1:raise ValueError('new output and positive dyadic power required')
    ctx.prec=a.bits;tick=time.monotonic()
    d0,c0=validate_root(a.v0,0);d1,c1=validate_root(a.v1,1)
    chart=checked(a.chart,'fourfold_negative_canonical_cancellation_chart.py')
    if (chart['kind']!='actual_negative_canonical_chart_from_characteristic_cancellation' or
        not chart['exact_negative_characteristic_coordinates'] or not all(g['passed'] for g in chart['gates'])):
        raise ValueError('complete exact negative canonical inverse is required')
    for key in ('center_object_sha256','origin_inputs_sha256','direction_sha256',
                'exact_center_parameter','exact_parameter_interval'):
        if not chart['identity'][key]==d0['identity'][key]==d1['identity'][key]:
            raise ValueError('actual root traces and complete chart are different '+key)
    fit=read(d0['fit_path'])
    qmin=(4*stored(fit['true_frequency']).lower()).lower()
    qmax=(4*stored(fit['true_frequency']).upper()).upper()
    if not qmin>4:raise ValueError('true quarter-period normalization missing')
    r=stored(chart['full_analytic_potential_radial_disk']).lower()
    b=stored(chart['complete_potential_analytic_strip']).lower()
    M=stored(chart['chart_bounds']['full_complex_potential_modulus_before_root_Taylor']).upper()
    delta=arb(2)**(-a.collar_dyadic_power)
    if not 0<delta<r/2:raise ValueError('actual collar is outside the proved potential disk')
    z=delta/r;tail0=(M*z*z/(1-z)).upper();tail1=(M/r*z*(2-z)/(1-z)**2).upper()
    decay=(qmin*b).lower()
    powers={'K':Fraction(31,3),'B':Fraction(19,2),'W':Fraction(32,3)}
    budgets={};full={}
    for name,p in powers.items():
        V0,b0=root_moment(d0,c0,p,0);V1,b1=root_moment(d1,c1,p,1)
        t0=analytic_moment(p,tail0,decay);t1=analytic_moment(p,tail1,decay)
        V=(V0+delta*V1+t0).upper();Vxi=(V1+t1).upper()
        budgets[name]=dict(power=str(p),complete_root_v0=b0,complete_root_v1=b1,
            complete_radial_V_fee=record(t0),complete_radial_Vxi_fee=record(t1),
            complete_V_weighted_l1=record(V),complete_Vxi_weighted_l1=record(Vxi))
        full[name]=(V,Vxi)
    K0=(100*arb.pi()*2**(exact_arb(powers['K'])/2)*full['K'][0]).upper()
    B1=(100*arb.pi()*2**(exact_arb(powers['B'])/2)*full['B'][0]).upper()
    if not delta*K0<arb(1)/10:raise ValueError('full intermediate Airy-Volterra shortness failed')
    W=(2**(arb(14)/3)*(full['W'][0]+full['W'][1])).upper()
    Cq=(4*(50*arb.pi()+5)*qmin**(-arb(4)/3)+150*arb.pi()+3/qmin).upper()
    R43=(2*Cq*W+2*(arb(1)/10).exp()*delta*B1*B1).upper()
    Ai0=1/(arb(3)**(arb(2)/3)*(arb(2)/3).gamma())
    minAip0=1/(arb(3)**(arb(1)/3)*(arb(1)/3).gamma())
    ca=(Ai0/minAip0).sqrt()
    source=(5*arb(2).sqrt()*arb.pi()/ca*(arb(1)/10).exp()).upper()
    out=dict(kind='actual_negative_R43_cancellation_chart_complete_root_Fourier',
        complete=True,proved=True,source_sha256=sha(__file__),bits=a.bits,
        inputs={str(p):sha(p) for p in (a.v0,a.v1,a.chart)},identity=chart['identity'],
        exact_negative_collar_height=str(Fraction(1,2**a.collar_dyadic_power)),
        Sobolev_output_window=[-8,8],paid_intermediate_window=10,
        actual_quarter_circle_frequency=[record(qmin),record(qmax)],
        full_potential_radial_disk=record(r),full_potential_angle_strip=record(b),
        complete_radial_V_remainder_modulus=record(tail0),
        complete_radial_Vxi_remainder_modulus=record(tail1),
        complete_root_and_radial_Fourier_budgets=budgets,
        R43_constants={k:record(v) for k,v in dict(K0=K0,delta_K0=delta*K0,B1=B1,W=W,Cq=Cq,
            full_four_thirds_remainder=R43,homogeneous_forward_and_inverse=(arb(1)/10).exp(),
            canonical_ordinary_L1_source_to_amplitude=source).items()},
        all_modes_all_parameters_and_mean_retained=True,
        both_amplitudes_and_all_frequency_cones_retained=True,
        complete_projected_L2_error_kept_correlated=True,
        complete_actual_root_and_radial_tails_retained=True,
        full_returned_Rstar_proved=False,positive_Ai_contact_proved=False,
        physical_frame_source_gluing_proved=False,finite_Schur_inverse_proved=False,
        README_completion_proved=False,
        scope='Actual full negative-collar R43 on the stated finite Sobolev window. The real enlarged chart and all root/radial tails are retained; this is not a completed return, final cutoff, or nonlinear theorem.',
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_negative_collar_root_fourier_budget.py',
            'fourfold_negative_canonical_cancellation_chart.py',
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_root_fourier_fit.py')},
        seconds=time.monotonic()-tick)
    save(a.out,out)
    print(dict(complete=True,out=str(a.out),sha256=sha(a.out),constants=out['R43_constants']),flush=True)

if __name__=='__main__':main()
