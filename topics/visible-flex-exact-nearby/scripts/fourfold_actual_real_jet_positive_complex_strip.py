#!/usr/bin/env python3
"""Actual positive-real complex derivative strips from even Taylor parity.

Real complete jets are used only through the exact Schwarz-reflection parity
of H'(x+iy); the analytic tail is paid from the unchanged full complex strip.
This is a new justified complex permission, not substitution of real norms.
"""
from __future__ import annotations
import argparse,math,time
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_root_fourier_fit import save,sha,stored
from fourfold_negative_collar_root_fourier_budget import record
from fourfold_negative_canonical_cancellation_chart import checked
from fourfold_actual_return_symmetric_density_normal_form import Q_cross_and_adjoint


def up(z):return stored(z).upper()
def lo(z):return stored(z).lower()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--new-jets',type=Path,default=Path('notes/2026-11-13-R106-full-relative-real-log-jets.json.gz'))
    p.add_argument('--old-jets',type=Path,default=Path('notes/2026-11-13-R106-full-relative-real-ray-jets.json.gz'))
    p.add_argument('--normal-form',type=Path,default=Path('notes/2026-11-13-actual-two-cone-density-normal-form.json'))
    p.add_argument('--high',type=Path,default=Path('notes/2026-11-13-actual-fixed-label-high-density-Volterra.json'))
    p.add_argument('--bits',type=int,default=320)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise ValueError('fresh justified complex-strip certificate required')
    ctx.prec=a.bits;tick=time.monotonic()
    nj=checked(a.new_jets,'fourfold_actual_relative_ray_log_jets.py')
    oj=checked(a.old_jets,'fourfold_actual_relative_ray_real_jets.py')
    nf=checked(a.normal_form,'fourfold_actual_return_symmetric_density_normal_form.py')
    h=checked(a.high,'fourfold_actual_label_high_density_volterra.py')
    if (not nj['identity']==oj['identity']==nf['identity']==h['identity']
        or nj['inputs'].get(str(a.old_jets))!=sha(a.old_jets)
        or oj['inputs'].get(str(a.high))!=sha(a.high)):
        raise ValueError('the same complete actual label maps are required')
    H={z['order']:up(z['accepted_complete_relative_derivative'])
       for z in oj['whole_time_relative_derivative_bounds']}
    for z in nj['accepted_real_derivative_bounds']:
        H[z['order']]=min(H[z['order']],up(z['accepted_complete_relative_derivative']))
    Cr=up(nj['accepted_relative_first_derivative'])
    M=up(h['true_relative_complex_derivative']);S=lo(h['unchanged_normalized_complex_flow_strip'])
    m=(1/Cr).lower();N=int(nf['scale'])
    # Cauchy coefficients of H' about each real center are bounded by M/S^k.
    # Odd powers contribute no real part. The five paid real odd H-jets
    # improve coefficients of powers y^2 through y^10.
    coefficient=[min(M,(H[2*k+1]*S**(2*k)/math.factorial(2*k)).upper()).upper()
                 for k in range(1,6)]
    def fee(t):
        return (sum((coefficient[k-1]*t**(2*k) for k in range(1,6)),arb(0))
                +M*t**12/(1-t*t)).upper()
    left=Fraction(0);right=Fraction(1,2)
    for _ in range(96):
        middle=(left+right)/2
        if fee(exact_arb(middle))<m/2:left=middle
        else:right=middle
    t=exact_arb(left);s=(S*t).lower();loss=fee(t);c=(m-loss).lower()
    es,decay=Q_cross_and_adjoint(N,s,c,M)
    strict=dict(original_full_complex_strip=record(S),unchanged_complex_derivative_modulus=record(M),
        original_real_derivative_lower=record(m),real_to_complex_ratio_exact=str(left),
        even_Taylor_normalized_coefficients=[record(z) for z in coefficient],
        even_tail_start_power=12,full_even_Taylor_loss=record(loss),
        new_positive_real_complex_strip=record(s),new_complex_derivative_real_lower=record(c),
        full_cross_and_adjoint_gain_two=record(es),full_cross_decay=record(decay),
        prior_cross_error=nf['Q_factor_budget']['strict']['error'],
        prior_cross_decay=nf['Q_factor_budget']['strict']['decay'],
        cross_improvement=record((lo(nf['Q_factor_budget']['strict']['error'])/es).lower()),
        bounds_apply_to_all_relative_times_and_inverses=True)
    f=nf['final_root_label_bounds']
    FC=lo(f['real_derivative_lower']);FM=up(f['complex_derivative_modulus'])
    FS=exact_arb(Fraction(f['original_complex_strip']))
    # Universal complete even Taylor sum M t^2/(1-t^2), without inserting
    # any new real derivative or claiming analytic control for the inverse.
    Ft=((FC/(2*FM+FC)).sqrt()*(1-arb(2)**-40)).lower()
    Fs=(FS*Ft).lower();Floss=(FM*Ft**2/(1-Ft**2)).upper();Fc=(FC-Floss).lower()
    ec,cd=Q_cross_and_adjoint(N,Fs,Fc,FM)
    final=dict(original_full_complex_strip=record(FS),unchanged_complex_derivative_modulus=record(FM),
        original_real_derivative_lower=record(FC),universal_complete_even_loss=record(Floss),
        new_positive_real_complex_strip=record(Fs),new_complex_derivative_real_lower=record(Fc),
        full_cross_and_adjoint_gain_two=record(ec),full_cross_decay=record(cd),
        prior_cross_error=nf['Q_factor_budget']['actual_final_circle']['error'],
        prior_cross_decay=nf['Q_factor_budget']['actual_final_circle']['decay'],
        cross_improvement=record((lo(nf['Q_factor_budget']['actual_final_circle']['error'])/ec).lower()),
        inverse_companion_error_paid_by_exact_E_inverse_equals_minus_E_adjoint=True)
    gates=[]
    def gate(name,ok):
        gates.append(dict(name=name,passed=bool(ok)))
        if not ok:raise ValueError(name)
    gate('strict complete complex derivative real part exceeds half its real lower bound',c>m/2)
    gate('final-circle complete complex derivative real part exceeds half its real lower bound',Fc>FC/2)
    gate('both subdomains remain inside the unchanged original analytic strips',s<S and Fs<FS)
    gate('both complete cross-and-adjoint bounds improve',es<lo(strict['prior_cross_error']) and ec<lo(final['prior_cross_error']))
    out=dict(kind='actual_even_Taylor_positive_real_strips_and_complete_cross_cone_bounds',
        complete=True,proved=True,source_sha256=sha(__file__),bits=a.bits,
        identity=nf['identity'],actual_parameter_scope=nf['actual_parameter_scope'],scale=N,
        inputs={str(p):sha(p) for p in (a.new_jets,a.old_jets,a.normal_form,a.high)},
        native_geometry_recomputed=0,
        exact_parity='H is real on the real circle, so every odd Taylor term of Hprime(x+i*y) is purely imaginary',
        strict=strict,actual_final_circle=final,
        original_domains_moduli_and_exact_maps_unchanged=True,
        real_jets_not_silently_used_as_complex_derivative_bounds=True,
        complete_opposite_cones_mean_rows_columns_and_adjoint_windows_retained=True,
        full_cross_windows=[['0','2'],['-2','0']],
        separate_true_scattering_error_not_improved=True,
        complete_returned_Rstar_recomputed=False,full_feedback_inverse_proved=False,
        gates=gates,dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_root_fourier_fit.py',
            'fourfold_negative_collar_root_fourier_budget.py','fourfold_negative_canonical_cancellation_chart.py',
            'fourfold_actual_return_symmetric_density_normal_form.py')},
        seconds=time.monotonic()-tick)
    save(a.out,out)
    print(dict(complete=True,strict_strip=s.str(15),strict_error=es.str(15),
        final_strip=Fs.str(15),final_error=ec.str(15),out=str(a.out),sha256=sha(a.out)),flush=True)


if __name__=='__main__':main()

