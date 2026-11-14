#!/usr/bin/env python3
"""Reconsume the same complete return with full Bessel-Q and paired-root bounds.

The exact old half words are estimated factor by factor after the root flux
scalar cancels.  The old genuine scattering error is retained unchanged.
Every mean, ordinary source, independent regular slot and Schur block remains.
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
from fourfold_actual_return_symmetric_density_normal_form import phase_bounds


def up(v):return stored(v).upper()
def lo(v):return stored(v).lower()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--normal-form',type=Path,default=Path('notes/2026-11-13-actual-two-cone-density-normal-form.json'))
    ap.add_argument('--Q-budget',type=Path,default=Path('notes/2026-11-13-actual-density-Q-Bessel-budget-v2.json'))
    ap.add_argument('--potential',type=Path,default=Path('notes/2026-11-13-actual-root-common-flow-potential.json'))
    ap.add_argument('--old-high',type=Path,default=Path('notes/2026-11-13-R104-actual-return-explicit-high-cutoff.json'))
    ap.add_argument('--bits',type=int,default=384)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args()
    if a.out.exists():raise ValueError('new complete returned bound required')
    ctx.prec=a.bits;tick=time.monotonic()
    nf=checked(a.normal_form,'fourfold_actual_return_symmetric_density_normal_form.py')
    qb=checked(a.Q_budget,'fourfold_actual_density_Q_Bessel_budget.py')
    pv=checked(a.potential,'fourfold_actual_root_common_flow_potential.py')
    old=checked(a.old_high,'fourfold_actual_return_explicit_high_cutoff.py')
    if (qb['inputs'].get(str(a.normal_form))!=sha(a.normal_form)
        or old['inputs'].get(str(a.normal_form))!=sha(a.normal_form)
        or qb['identity']!=nf['identity'] or qb['scale']!=nf['scale']):
        raise ValueError('same complete old return and norm scale required')
    # Root and strict metadata have different record layouts. Check the exact
    # physical origin, direction and original real parameter interval.
    for k in ('origin_inputs_sha256','direction_sha256','exact_center_parameter','exact_parameter_interval'):
        if pv['identity'][k]!=nf['identity'][k]:raise ValueError('actual whole parameter family differs: '+k)
    if not nf['entire_unweighted_base_Rstar_proved']:
        raise ValueError('the original complete normal-form proof is required')
    N=nf['scale'];qlo=lo(pv['actual_quarter_circle_frequency'][0])
    L=exact_arb(Fraction(pv['canonical_real_half_height']))
    strip=exact_arb(Fraction(pv['canonical_complex_angle_strip']))
    phases={name:{k:up(v) for k,v in z.items() if k!='count'}
            for name,z in nf['phase_factor_budget'].items()}
    counts={name:z['count'] for name,z in nf['phase_factor_budget'].items()}
    root_phase=(up(pv['bounds']['full_canonical_potential'])*L.sqrt()/qlo).upper()
    phases['root']=phase_bounds(N,root_phase,qlo*strip)
    qnorm={name:up(z['full_Q_inverse_and_adjoints_plus_minus_two'])
           for name,z in qb['rows'].items()}
    qbase=up(qb['rows']['actual_final_circle']['complete_unscaled_L2_Q_inverse_and_adjoints'])
    qC=qnorm['actual_final_circle']
    # Exact D.25 half words: two physical-cut, two graph, one strict map;
    # two of each root/Airy/graph phase, one strict phase. Unit Airy
    # translations and original Fourier projections have norm one.
    Tmodel=qnorm['physical_cut']**2*qnorm['graph']**2*qnorm['strict']
    for name,z in phases.items():
        if counts[name]%2:raise ValueError('original two-half word factor count differs')
        Tmodel*=(1+z['same_order'])**(counts[name]//2)
    Tmodel=Tmodel.upper()
    Pq=up(qb['summary']['full_Q_word_factor_product'])
    Pphase=arb(1);sumA=sumA1=sumX=sumO=arb(0)
    for name,z in phases.items():
        count=counts[name]
        Pphase*=(1+z['same_order'])**count
        sumA+=count*z['same_order'];sumA1+=count*z['gain_one']
        sumX+=count*z['cross_and_mean_gain_two']
        if name in ('graph','strict'):sumO+=count*z['ordering_gain_two']
    sumE=sum((z['count']*up(z['error']) for z in nf['Q_factor_budget'].values()),arb(0))
    P=(Pq*Pphase).upper()
    elementary=(8*P*(sumE+sumO+sumX)).upper()
    quadratic=(P*sumA1**2).upper()
    covariance=(P*sumA*sumE).upper()
    ordering=up(nf['bounds']['final_full_phase_left_to_symmetric_ordering'])
    calculus=(elementary+quadratic+covariance+ordering).upper()
    word_path=Path('notes/2026-11-13-actual-central-strong-word.json')
    word=checked(word_path,'fourfold_actual_central_strong_word.py')
    cap_path=Path('notes/2026-11-13-exact-positive-cap-Airy-contact-v2.json')
    cap=checked(cap_path,'fourfold_actual_exact_positive_cap_Airy_contact.py')
    if nf['inputs'].get(str(word_path))!=sha(word_path) or nf['inputs'].get(str(cap_path))!=sha(cap_path):
        raise ValueError('original complete scattering/cap realization changed')
    RS=up(word['norms']['complete_scattering_word_error_both_base_windows'])
    capR=up(cap['complete_original_frame']['right_and_left_full_four_thirds_remainder'])
    Ea_p=(capR+RS).upper()
    Ea_m=(max(arb(1),Tmodel)*capR+3*RS).upper()
    replacement=((1+Tmodel)*RS).upper()
    Wp=(2*(1+Tmodel)*Ea_p+6*RS+replacement).upper()
    Wm=(2*(1+Tmodel)*Ea_m+6*RS+replacement).upper()
    Rp=(qC*qbase*Wp+calculus).upper()
    Rm=(qC*qbase*Wm+calculus).upper()
    Rscaled=max(Rp,Rm).upper()
    R=(arb(N)**(arb(4)/3)*Rscaled).upper()
    SC=Path('notes/2026-11-13-actual-central-scattering-and-source.json')
    SS=Path('notes/2026-11-13-actual-central-scattering-reflected-source.json')
    sc=checked(SC,'fourfold_actual_central_scattering_and_source.py')
    ss=checked(SS,'fourfold_actual_central_scattering_reflected_source.py')
    for pp in (SC,SS):
        if nf['inputs'].get(str(pp))!=sha(pp):raise ValueError('original complete physical source changed')
    sb=ss['bounds'];cb=sc['bounds']
    physical=dict(strict_core=up(sb['strict_core_source']),
        either_canonical_root=up(sb['either_canonical_root_source']),
        either_tilted_graph=up(sb['either_tilted_graph_source']),
        negative_five_space_direct_sum=up(sb['five_space_direct_sum_source']),
        paired_positive_local_ordinary=up(cb['complete_positive_local_ordinary_source']),
        paired_positive_local_weak=up(cb['complete_positive_local_weak_source']),
        two_independent_physical_regular_fluxes=up(cb['actual_independent_regular_flux_to_wave_difference']))
    source={k:(2*qbase*v).upper() for k,v in physical.items()}
    if (old['exact_diagonal_gap']!='7/(110*j), every j>=1'
        or old['cohomological_gap']!='2/(5*abs(l)), every nonzero integer l'):
        raise ValueError('all-frequency arithmetic identities differ')
    M=up(nf['bounds']['full_b_analytic_modulus'])
    beta=up(old['beta_abs_upper']);c=arb(7)/110
    moments=[up(z) for z in old['complete_geometric_moments']]
    S0,S1,S2,S3,S4=moments
    def evaluate(e):
        cutoff=arb(2)**e
        A0=(5*M*(S1+2*S2/cutoff+S3/cutoff**2)).upper()
        A1=(5*M*(S2+2*S3/cutoff+S4/cutoff**2)).upper()
        B0=(beta+2*M*(S0+2*S1/cutoff+S2/cutoff**2)).upper()
        B1=(2*M*(S1+2*S2/cutoff+S3/cutoff**2)).upper()
        q0=A0/cutoff;q1=(A0+A1/cutoff)/cutoff
        z=dict(exponent=e,A0=A0,A1=A1,B0=B0,B1=B1,q0=q0,q1=q1)
        if not q1<1:return z
        E=((A0*(B0+B1/cutoff)+beta*(A0+A1/cutoff))/cutoff).upper()
        remainder=(R*(1+q0)/(1+cutoff*cutoff)**(arb(1)/6)).upper()
        kappa=((E+remainder)/(c*(1-q1))).upper()
        inv=((1+q0)/(c*(1-q1)*(1-kappa))).upper() if kappa<1 else None
        z.update(E=E,complete_strong_term=remainder,kappa=kappa,inverse=inv)
        return z
    passed=lambda z:'kappa' in z and z['kappa']<arb(1)/64
    low=0;high=1
    while not passed(evaluate(high)):
        low=high;high*=2
        if high>16384:raise ValueError('finite cutoff bracket exceeded')
    while high-low>1:
        mid=(low+high)//2
        if passed(evaluate(mid)):high=mid
        else:low=mid
    chosen=evaluate(high);previous=evaluate(high-1)
    gates=[]
    def gate(name,ok):
        gates.append(dict(name=name,passed=bool(ok)))
        if not ok:raise ValueError(name)
    gate('same full exact model half-word improves the former root-frame product',
         Tmodel<up(word['norms']['full_negative_transfer_word_HN_plus_minus_four_thirds']))
    gate('same complete two-cone strong remainder improves the original bound',
         R<up(nf['bounds']['corresponding_unscaled_full_R4over3']))
    gate('new explicit full high inverse has the intended strict gap',
         passed(chosen) and not passed(previous) and chosen['inverse']<16)
    gate('new cutoff is explicitly smaller than the previous complete cutoff',
         high<old['chosen']['exponent'])
    def pack(z):return {k:v if k=='exponent' else None if v is None else record(v.upper()) for k,v in z.items()}
    out=dict(kind='actual_complete_return_Bessel_density_and_paired_root_rebudget',
        complete=True,proved=True,source_sha256=sha(__file__),bits=a.bits,identity=nf['identity'],scale=N,
        inputs={str(p):sha(p) for p in (a.normal_form,a.Q_budget,a.potential,a.old_high,word_path,cap_path,SC,SS)},
        actual_parameter_scope=nf['actual_parameter_scope'],
        exact_original_b_and_beta_unchanged=True,
        exact_original_two_cone_word_and_every_mean_correction_unchanged=True,
        exact_model_half_word='U=p^* W_minus^* q, V=p^* W_plus q, with the original p,q and strict models; (2*gamma0)^2 cancels exactly against kappa',
        half_word_factor_counts=dict(physical_cut=2,graph=2,strict=1,unit_Airy_translation=2,
            root_phase=2,graph_phase=2,Airy_phase=2,strict_phase=1),
        old_true_scattering_error_reused_unchanged=True,
        phase_factor_budget={name:dict(count=counts[name],**{k:record(v) for k,v in z.items()}) for name,z in phases.items()},
        bounds={k:record(v.upper()) for k,v in dict(
            root_first_symmetric_phase_modulus=root_phase,
            complete_model_half_word_and_full_antidiagonal_transfer=Tmodel,
            complete_Q_factor_product=Pq,complete_one_plus_phase_product=Pphase,complete_word_product=P,
            complete_masks_means_ordering_and_adjoints=elementary,complete_multiple_phase_terms=quadratic,
            complete_symmetric_covariance= covariance,complete_order_two_word_calculus=calculus,
            unchanged_actual_strong_scattering_error=RS,unchanged_actual_full_cap_remainder=capR,
            actual_feedback_error_forward=Ea_p,actual_feedback_error_opposite=Ea_m,
            exact_true_transmission_model_replacement=replacement,
            preconditioned_word_forward=Wp,preconditioned_word_opposite=Wm,
            full_R4over3_forward=Rp,full_R4over3_opposite=Rm,full_scaled_R4over3=Rscaled,
            corresponding_unscaled_full_R4over3=R,prior_unscaled_full_R4over3=up(nf['bounds']['corresponding_unscaled_full_R4over3']),
            actual_final_Q_base=qbase,actual_final_Q_plus_minus_two=qC,
            complete_physical_base_reconstruction=2*qbase).items()},
        full_final_original_L2_source_columns={k:record(v) for k,v in source.items()},
        source_units='Exactly the old complete physical ordinary/contact direct sums; no weak-to-ordinary relabeling, no omission of independent regular fluxes.',
        high_inverse=dict(cutoff_exact=f'2^{high}',cutoff_decimal_digits=len(str(1<<high)),
            chosen=pack(chosen),preceding_dyadic=pack(previous),
            full_head_complex_dimension_exact=f'2^{high+2}',
            bound=record(chosen['inverse']),unweighted_index_interval=['-4/3','0'],
            zero_final_head_L2_source_to_high_Hminus1={k:record((chosen['inverse']*v).upper()) for k,v in source.items()},
            exact_full_Schur=old['exact_full_Schur']),
        full_b_analytic_modulus=nf['bounds']['full_b_analytic_modulus'],
        full_b_analytic_strip=nf['full_b_analytic_strip'],actual_beta_interval=old['actual_beta_interval'],
        exact_quadratic=old['exact_quadratic'],all_original_arithmetic_and_nonmean_gauge_terms_reused=True,
        all_four_branches_both_means_regular_ports_and_head_crossings_retained=True,
        finite_head_assembled=False,finite_head_inverse_proved=False,
        numerically_tractable_cutoff_proved=False,full_feedback_inverse_proved=False,
        higher_fixed_angular_weight_proved=False,new_tail_profile_transfer_proved=False,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_root_fourier_fit.py',
            'fourfold_negative_collar_root_fourier_budget.py','fourfold_negative_canonical_cancellation_chart.py',
            'fourfold_actual_return_symmetric_density_normal_form.py')},
        gates=gates,
        scope='Same actual complete old return with smaller fully explicit base strong remainder, original physical L2 sources, and a smaller specified high inverse cutoff. The complete finite head and all nonzero-head drives remain unsolved exact Schur obligations.',
        seconds=time.monotonic()-tick)
    save(a.out,out)
    print(dict(complete=True,out=str(a.out),sha256=sha(a.out),
        half_word=Tmodel.str(12),scaled_R=Rscaled.str(12),unscaled_R=R.str(12),
        cutoff=f'2^{high}',high_inverse=chosen['inverse'].str(12),seconds=out['seconds']),flush=True)


if __name__=='__main__':main()

