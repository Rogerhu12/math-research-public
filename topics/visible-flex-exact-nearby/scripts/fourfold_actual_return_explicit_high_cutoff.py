#!/usr/bin/env python3
"""An explicit all-frequency high inverse for the original complete return.

This is an enormous but specified cutoff in the already paid unweighted
base window. It does not solve or approximate the complete finite head.
"""
from __future__ import annotations
import argparse,time
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_root_fourier_fit import read,save,sha,stored
from fourfold_negative_collar_root_fourier_budget import record
from fourfold_negative_canonical_cancellation_chart import checked


def up(v):return stored(v).upper()
def lo(v):return stored(v).lower()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--normal-form',type=Path,default=Path('notes/2026-11-13-actual-two-cone-density-normal-form.json'))
    p.add_argument('--arithmetic',type=Path,default=Path('notes/2026-11-13-R104-polynomial-diagonal-native-replay.json'))
    p.add_argument('--phase',type=Path,default=Path('notes/2026-11-12-R102-nearby-quadratic-phase.json'))
    p.add_argument('--target-kappa',type=Fraction,default=Fraction(1,64))
    p.add_argument('--bits',type=int,default=384)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if a.out.exists() or not 0<a.target_kappa<Fraction(1,2):
        raise ValueError('a fresh output and a strict target below one half are required')
    ctx.prec=a.bits;tick=time.monotonic()
    nf=checked(a.normal_form,'fourfold_actual_return_symmetric_density_normal_form.py')
    ar=read(a.arithmetic);ph=read(a.phase)
    if (not nf['same_actual_operator_b_identification_proved']
        or not nf['entire_unweighted_base_Rstar_proved']
        or not nf['all_four_branches_both_means_independent_regular_rows_and_head_paths_retained']
        or not ar['complete_scalar_arithmetic'] or not all(g['pass'] for g in ar['gates'])
        or not ph['complete_arithmetic'] or not ph['all_positive_frequency_pure_phase_gap_proved']
        or ph['exception_count']!=0 or ar['exact_quadratic']!=ph['exact_quadratic']
        or ar['actual_beta_interval']!=ph['inputs']['beta_interval']
        or ar['all_modes']['complex_diagonal_modulus_lower']!='7/(110*j)'):
        raise ValueError('complete actual normal form and all-frequency arithmetic are required')
    for report,name in ((ar,'fourfold_polynomial_diagonal_and_cutoff_exact.mjs'),
                        (ph,'fourfold_nearby_quadratic_phase_exact.mjs')):
        if report['provenance']['source_sha256']!=sha(Path(__file__).with_name(name)):
            raise ValueError('the exact original arithmetic source changed')
        for z in report['provenance']['input_files']:
            if sha(Path(z['path']))!=z['sha256']:
                raise ValueError('a complete arithmetic input changed')
    if not any(z['path']==str(a.phase) and z['sha256']==sha(a.phase)
               for z in ar['provenance']['input_files']):
        raise ValueError('fresh polynomial diagonal uses a different phase certificate')
    quad=ar['exact_quadratic']
    if not quad['golden_tail'] or max(quad['prefix'])>8 or not quad['matrix_polynomial_identity_verified']:
        raise ValueError('the complete cohomological small-divisor bound is unavailable')
    R=up(nf['bounds']['corresponding_unscaled_full_R4over3'])
    M=up(nf['bounds']['full_b_analytic_modulus'])
    strip=exact_arb(Fraction(nf['full_b_analytic_strip']))
    beta=max(abs(exact_arb(Fraction(z))).upper() for z in ar['actual_beta_interval'])
    c=arb(7)/110;target=exact_arb(a.target_kappa)
    q=(-strip).exp()
    # Exact complete positive-frequency geometric moments; no tail truncation.
    S=[q/(1-q),q/(1-q)**2,q*(1+q)/(1-q)**3,
       q*(1+4*q+q*q)/(1-q)**4,
       q*(1+11*q+11*q*q+q**3)/(1-q)**5]
    def evaluate(exponent):
        N=arb(2)**exponent
        A0=(5*M*(S[1]+2*S[2]/N+S[3]/N**2)).upper()
        A1=(5*M*(S[2]+2*S[3]/N+S[4]/N**2)).upper()
        B0=(beta+2*M*(S[0]+2*S[1]/N+S[2]/N**2)).upper()
        B1=(2*M*(S[1]+2*S[2]/N+S[3]/N**2)).upper()
        q0=(A0/N).upper();q1=((A0+A1/N)/N).upper()
        ans=dict(exponent=exponent,A0=A0,A1=A1,B0=B0,B1=B1,q0=q0,q1=q1)
        if not q1<1:return ans
        E=((A0*(B0+B1/N)+beta*(A0+A1/N))/N).upper()
        rem=(R*(1+q0)/(1+N*N)**(arb(1)/6)).upper()
        kap=((E+rem)/(c*(1-q1))).upper()
        K=((1+q0)/(c*(1-q1)*(1-kap))).upper() if kap<1 else None
        ans.update(E=E,complete_strong_term=rem,kappa=kap,inverse=K)
        return ans
    def passed(z):return 'kappa' in z and z['kappa']<target
    left=0;right=1;calls=0
    while True:
        trial=evaluate(right);calls+=1
        if passed(trial):break
        left=right;right*=2
        if right>16384:raise ValueError('declared finite cutoff search range exceeded')
    while right-left>1:
        mid=(left+right)//2;z=evaluate(mid);calls+=1
        if passed(z):right=mid
        else:left=mid
    accepted=evaluate(right);previous=evaluate(right-1)
    if not passed(accepted) or passed(previous):
        raise ValueError('the explicit dyadic cutoff is not correctly bracketed')
    if 'kappa' in previous and not previous['kappa']>target:
        raise ValueError('the preceding dyadic bound has no strict directed comparison')
    N=1<<right;K=accepted['inverse']
    if K is None or not K<16:raise ValueError('the actual one-loss high inverse is not below sixteen')
    source={k:record((K*up(v)).upper())
            for k,v in nf['full_final_ordinary_and_contact_source_columns_L2'].items()}
    def packed(z):
        return {k:(v if k=='exponent' else None if v is None else record(v)) for k,v in z.items()}
    out=dict(kind='actual_complete_original_return_explicit_unweighted_high_inverse',
        complete=True,proved=True,source_sha256=sha(__file__),bits=a.bits,
        identity=nf['identity'],actual_parameter_scope=nf['actual_parameter_scope'],
        inputs={str(z):sha(z) for z in (a.normal_form,a.arithmetic,a.phase)},
        native_geometry_recomputed=0,original_full_normal_form_reused=True,
        full_b_analytic_modulus=record(M),full_b_analytic_strip=str(Fraction(nf['full_b_analytic_strip'])),
        actual_beta_interval=ar['actual_beta_interval'],beta_abs_upper=record(beta),
        exact_quadratic=quad,cohomological_gap='2/(5*abs(l)), every nonzero integer l',
        exact_diagonal_gap='7/(110*j), every j>=1',
        full_unscaled_strong_remainder=record(R),
        paid_unweighted_index_interval=['-4/3','0'],
        multiplier_power_majorant='(1+abs(l)/N)^2, which bounds every required abs(s)<=4/3',
        complete_geometric_moments=[record(z.upper()) for z in S],
        target_kappa=str(a.target_kappa),chosen=packed(accepted),preceding_dyadic=packed(previous),
        cutoff_exact=f'2^{right}',cutoff_integer=str(N),cutoff_decimal_digits=len(str(N)),
        first_dyadic_passing_these_complete_monotone_majorants=True,evaluations=calls,
        both_first_root_cones_and_both_second_root_high_cones_included=True,
        second_root_high_model='identity; its inverse times D^-1 has norm <=1/N <=110/7',
        complete_high_projection='abs(n)>=N on both root-circle copies; zero on both independent regular slots',
        high_inverse_domain='P H^(s+1) -> P H^s, -4/3<=s<=0, zero fixed angular weight',
        complete_high_inverse_bound=record(K),
        finite_head_exact_complex_dimension=str(4*N),finite_head_dimension_formula='4*N',
        finite_head_contents=['first-root mean and both first-root modes 1<=j<N',
            'second-root mean and all second-root modes 1<=abs(n)<N',
            'both independent regular slots'],
        every_low_to_high_and_high_to_low_entry_retained=True,
        exact_full_Schur='S_L=A_LL-A_LH*A_H^-1*A_HL; u_L=S_L^-1(g_L-A_LH*A_H^-1*g_H); u_H=A_H^-1(g_H-A_HL*u_L)',
        source_scope='Only the high particular for prescribed zero head is bounded here; at s=-1 the original complete L2 source columns give H^-1 normalized high amplitudes. All head equations and all nonzero-head drives remain exact.',
        complete_original_L2_sources_to_high_Hminus1_particular=source,
        complete_finite_head_matrix_assembled=False,finite_head_inverse_proved=False,
        numerically_tractable_cutoff_proved=False,full_feedback_inverse_proved=False,
        stronger_positive_source_window_proved=False,positive_fixed_angular_weight_proved=False,
        new_deep_tail_profile_transfer_proved=False,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_root_fourier_fit.py',
            'fourfold_negative_collar_root_fourier_budget.py','fourfold_negative_canonical_cancellation_chart.py')},
        seconds=time.monotonic()-tick)
    save(a.out,out)
    print(dict(complete=True,N=f'2^{right}',decimal_digits=len(str(N)),
        kappa=accepted['kappa'].str(16),previous_kappa=previous.get('kappa',arb(0)).str(16),
        high_inverse=K.str(16),full_finite_head_dimension=f'2^{right+2}',
        out=str(a.out),sha256=sha(a.out)),flush=True)


if __name__=='__main__':main()
