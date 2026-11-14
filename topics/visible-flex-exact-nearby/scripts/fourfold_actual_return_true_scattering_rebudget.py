#!/usr/bin/env python3
"""Consume the smaller genuine scattering error in the complete original return.

Includes the separately proved full complex cross-cone errors, the entire
head-preserving arithmetic gauge, and every final base/H1 physical source.
No old geometry, exact first phase, ordinary source or mean is replaced.
"""
from __future__ import annotations
import argparse,time
from pathlib import Path
from flint import arb,ctx
from fourfold_phase_root_fourier_fit import save,sha,stored
from fourfold_negative_collar_root_fourier_budget import record
from fourfold_negative_canonical_cancellation_chart import checked


def up(v):return stored(v).upper()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--scattering',type=Path,default=Path('notes/2026-11-13-actual-root-cut-true-strong-rebudget.json'))
    p.add_argument('--prior-return',type=Path,default=Path('notes/2026-11-13-actual-return-Bessel-rebudget.json'))
    p.add_argument('--cross',type=Path,default=Path('notes/2026-11-13-R106-even-Taylor-complete-cross-cone.json'))
    p.add_argument('--normal-form',type=Path,default=Path('notes/2026-11-13-actual-two-cone-density-normal-form.json'))
    p.add_argument('--old-high',type=Path,default=Path('notes/2026-11-13-R104-actual-return-explicit-high-cutoff.json'))
    p.add_argument('--old-source',type=Path,default=Path('notes/2026-11-13-actual-return-Hone-source.json'))
    p.add_argument('--prior-Hone',type=Path,default=Path('notes/2026-11-13-actual-return-Bessel-Hone-source.json'))
    p.add_argument('--bits',type=int,default=384)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise ValueError('fresh complete return report required')
    ctx.prec=a.bits;tick=time.monotonic()
    sc=checked(a.scattering,'fourfold_actual_root_cut_strong_rebudget.py')
    rb=checked(a.prior_return,'fourfold_actual_return_Bessel_rebudget.py')
    cx=checked(a.cross,'fourfold_actual_real_jet_positive_complex_strip.py')
    nf=checked(a.normal_form,'fourfold_actual_return_symmetric_density_normal_form.py')
    ar=checked(a.old_high,'fourfold_actual_return_explicit_high_cutoff.py')
    hs=checked(a.old_source,'fourfold_actual_return_Hone_source.py')
    ph=checked(a.prior_Hone,'fourfold_actual_return_Bessel_Hone_source.py')
    rows=(sc,rb,cx,nf,ar,hs,ph)
    if any(z['identity']!=rb['identity'] for z in rows) or any(
            z['scale']!=rb['scale'] for z in (sc,rb,cx,nf,hs,ph)):
        raise ValueError('identical actual complete old return and norm scale required')
    if any(z['actual_parameter_scope']!=rb['actual_parameter_scope'] for z in (sc,cx,nf,hs,ph)):
        raise ValueError('identical actual selected parameter scope required')
    for parent,path in ((sc,a.prior_return),(sc,a.old_source),(rb,a.normal_form),
        (ar,a.normal_form),(ph,a.prior_return),(ph,a.old_source)):
        if parent['inputs'].get(str(path))!=sha(path):
            raise ValueError('the complete operator input has changed: '+str(path))
    for i,z in enumerate(rows):
        for w in rows[:i]:
            for path in set(z['inputs']).intersection(w['inputs']):
                if z['inputs'][path]!=w['inputs'][path]:
                    raise ValueError('shared complete realization differs: '+path)
    if not cx['complete_opposite_cones_mean_rows_columns_and_adjoint_windows_retained']:
        raise ValueError('full mean/cross/adjoint permission is missing')
    N=int(rb['scale']);r=rb['bounds'];s=sc['bounds']
    T=up(r['complete_model_half_word_and_full_antidiagonal_transfer'])
    P=up(r['complete_word_product'])
    phases=rb['phase_factor_budget']
    sumA=sumA1=sumX=sumO=arb(0)
    for name,z in phases.items():
        count=z['count'];sumA+=count*up(z['same_order'])
        sumA1+=count*up(z['gain_one']);sumX+=count*up(z['cross_and_mean_gain_two'])
        if name in ('graph','strict'):sumO+=count*up(z['ordering_gain_two'])
    errors={name:up(z['error']) for name,z in nf['Q_factor_budget'].items()}
    for name in ('strict','actual_final_circle'):
        if not (stored(cx[name]['prior_cross_error'])
                -stored(nf['Q_factor_budget'][name]['error'])).contains(0):
            raise ValueError('the precise cross-cone factor is different')
        errors[name]=up(cx[name]['full_cross_and_adjoint_gain_two'])
    sumE=sum((nf['Q_factor_budget'][name]['count']*v for name,v in errors.items()),arb(0))
    elementary=(8*P*(sumE+sumO+sumX)).upper()
    quadratic=(P*sumA1**2).upper();covariance=(P*sumA*sumE).upper()
    ordering=up(nf['bounds']['final_full_phase_left_to_symmetric_ordering'])
    calculus=(elementary+quadratic+covariance+ordering).upper()
    RS=up(s['complete_actual_strong_scattering_error_both_windows'])
    capR=up(r['unchanged_actual_full_cap_remainder'])
    Eplus=(capR+RS).upper();Eminus=(max(arb(1),T)*capR+3*RS).upper()
    replacement=((1+T)*RS).upper()
    Wplus=(2*(1+T)*Eplus+6*RS+replacement).upper()
    Wminus=(2*(1+T)*Eminus+6*RS+replacement).upper()
    q0=up(r['actual_final_Q_base']);q2=up(r['actual_final_Q_plus_minus_two'])
    Rplus=(q2*q0*Wplus+calculus).upper()
    Rminus=(q2*q0*Wminus+calculus).upper()
    Rscaled=max(Rplus,Rminus).upper()
    R=(arb(N)**(arb(4)/3)*Rscaled).upper()
    if ar['exact_diagonal_gap']!='7/(110*j), every j>=1' or ar['cohomological_gap']!='2/(5*abs(l)), every nonzero integer l':
        raise ValueError('the original all-frequency arithmetic identity is required')
    M=up(nf['bounds']['full_b_analytic_modulus']);beta=up(ar['beta_abs_upper']);gap=arb(7)/110
    S0,S1,S2,S3,S4=[up(z) for z in ar['complete_geometric_moments']]
    def evaluate(e):
        cutoff=arb(2)**e
        A0=(5*M*(S1+2*S2/cutoff+S3/cutoff**2)).upper()
        A1=(5*M*(S2+2*S3/cutoff+S4/cutoff**2)).upper()
        B0=(beta+2*M*(S0+2*S1/cutoff+S2/cutoff**2)).upper()
        B1=(2*M*(S1+2*S2/cutoff+S3/cutoff**2)).upper()
        g0=A0/cutoff;g1=(A0+A1/cutoff)/cutoff
        z=dict(exponent=e,A0=A0,A1=A1,B0=B0,B1=B1,q0=g0,q1=g1)
        if not g1<1:return z
        commutator=((A0*(B0+B1/cutoff)+beta*(A0+A1/cutoff))/cutoff).upper()
        strong=(R*(1+g0)/(1+cutoff*cutoff)**(arb(1)/6)).upper()
        kappa=((commutator+strong)/(gap*(1-g1))).upper()
        inv=((1+g0)/(gap*(1-g1)*(1-kappa))).upper() if kappa<1 else None
        z.update(E=commutator,complete_strong_term=strong,kappa=kappa,inverse=inv)
        return z
    passes=lambda z:'kappa' in z and z['kappa']<arb(1)/64
    low=0;high=1
    while not passes(evaluate(high)):
        low=high;high*=2
        if high>16384:raise ValueError('explicit high cutoff bracket exceeded')
    while high-low>1:
        middle=(high+low)//2
        if passes(evaluate(middle)):high=middle
        else:low=middle
    chosen=evaluate(high);previous=evaluate(high-1);K=chosen['inverse']
    # All base/strong physical columns are the same actual realizations.
    # The new negative legs are copied from the complete root/cut proof.
    raw0={k:up(v) for k,v in sc['full_negative_near_endpoint_raw_base_columns'].items()}
    raw1={k:up(v) for k,v in sc['full_negative_near_endpoint_raw_HN1_columns'].items()}
    source0={k:up(v) for k,v in hs['original_affine_base_columns'].items()}
    source1={k:up(v) for k,v in hs['original_affine_HN1_columns'].items()}
    for k in raw0:
        source0[k]=up(sc['full_negative_original_affine_base_columns'][k])
        source1[k]=(max(arb(1),T)*raw1[k]+RS*raw0[k]).upper()
    q1=(q0*q2).sqrt().upper();toH1=(N*q1).upper()
    triangle=(1+T).upper();correction=(triangle*capR+RS).upper()
    final0={k:(2*q0*source0[k]).upper() for k in source0}
    final1={k:(toH1*(triangle*source1[k]+correction*source0[k])).upper() for k in source0}
    def five(columns):
        return (columns['strict_core']**2+2*columns['either_canonical_root']**2
                +2*columns['either_tilted_graph']**2).sqrt().upper()
    for cols in (final0,final1):cols['negative_five_space_direct_sum']=five(cols)
    high_source={k:(K*v).upper() for k,v in final1.items()}
    physical_source={k:(2*q0*v).upper() for k,v in high_source.items()}
    improvements={k:(stored(ph['full_final_source_H1_columns'][k]).lower()/v).lower() for k,v in final1.items()}
    gates=[]
    def gate(name,ok):
        gates.append(dict(name=name,passed=bool(ok)))
        if not ok:raise ValueError(name)
    gate('the genuine complete scattering error is smaller',RS<up(r['unchanged_actual_strong_scattering_error']))
    gate('the separately proved full analytic cross errors improve the same factors',
         all(errors[k]<up(nf['Q_factor_budget'][k]['error']) for k in ('strict','actual_final_circle')))
    gate('the complete order-two word calculus improves',calculus<up(r['complete_order_two_word_calculus']))
    gate('both complete returned strong windows improve',Rplus<up(r['full_R4over3_forward']) and Rminus<up(r['full_R4over3_opposite']))
    gate('all-frequency gauge and the new explicit inverse meet their strict gates',passes(chosen) and not passes(previous) and K<16)
    gate('the new specified cutoff is strictly smaller',high<rb['high_inverse']['chosen']['exponent'])
    gate('the original full means, regular rows and all head crossings remain',
         sc['original_mean_matrices_both_regular_ports_and_every_head_path_retained']
         and hs['all_four_branches_both_means_regular_rows_and_all_high_head_crossings_retained'])
    gate('every final complete physical H1 column improves',all(v>1 for v in improvements.values()))
    def packed(z):
        return {k:v if k=='exponent' else None if v is None else record(v.upper()) for k,v in z.items()}
    out=dict(kind='actual_complete_return_true_scattering_rebudget_full_sources_and_explicit_high_inverse',
        complete=True,proved=True,source_sha256=sha(__file__),bits=a.bits,identity=rb['identity'],scale=N,
        actual_parameter_scope=rb['actual_parameter_scope'],
        geometric_and_local_source_bounds_uniform_in_original_whole_parameter_box=True,
        inputs={str(p):sha(p) for p in (a.scattering,a.prior_return,a.cross,a.normal_form,a.old_high,a.old_source,a.prior_Hone)},
        native_geometry_recomputed=0,all_exact_original_operator_words_and_first_phases_unchanged=True,
        exact_original_b_nonmean_and_beta_unchanged=True,exact_original_actual_triangular_preconditioner_unchanged=True,
        exact_model_half_word=rb['exact_model_half_word'],half_word_factor_counts=rb['half_word_factor_counts'],
        full_updated_coordinate_errors={k:record(v) for k,v in errors.items()},
        coordinate_error_counts={k:z['count'] for k,z in nf['Q_factor_budget'].items()},
        true_positive_real_complex_domain_separately_paid=True,
        exact_strong_windows=[['0','4/3'],['-4/3','0']],
        bounds={k:record(v) for k,v in dict(
            complete_model_half_word_and_full_antidiagonal_transfer=T,
            complete_word_product=P,complete_masks_means_ordering_and_adjoints=elementary,
            complete_multiple_phase_terms=quadratic,complete_symmetric_covariance=covariance,
            final_full_phase_left_to_symmetric_ordering=ordering,complete_order_two_word_calculus=calculus,
            complete_actual_strong_scattering_error=RS,unchanged_actual_full_cap_remainder=capR,
            actual_feedback_error_forward=Eplus,actual_feedback_error_opposite=Eminus,
            exact_true_transmission_model_replacement=replacement,
            preconditioned_word_forward=Wplus,preconditioned_word_opposite=Wminus,
            full_R4over3_forward=Rplus,full_R4over3_opposite=Rminus,full_scaled_R4over3=Rscaled,
            corresponding_unscaled_full_R4over3=R,
            prior_unscaled_full_R4over3=up(r['corresponding_unscaled_full_R4over3']),
            actual_final_Q_base=q0,actual_final_Q_window_two=q2,actual_final_Q_HN1=q1,
            complete_Q_then_scaled_to_unscaled_H1=toH1,
            complete_physical_base_reconstruction=2*q0,complete_model_triangle_HN1=triangle,
            actual_triangle_cap_base_to_HN1_correction=correction).items()},
        source_units=hs['source_units'],base_negative_source_units=sc['complete_base_physical_source_units'],
        negative_source_partition=hs['full_negative_source_partition'],source_reflection=hs['source_reflection'],
        exact_near_endpoint_affine_source=hs['exact_near_endpoint_affine_source'],
        ordered_complete_final_source=hs['ordered_complete_final_source'],exact_ordered_expansion=hs['exact_ordered_expansion'],
        complete_near_endpoint_raw_base_columns={k:record(v) for k,v in raw0.items()},
        complete_near_endpoint_raw_HN1_columns={k:record(v) for k,v in raw1.items()},
        original_affine_base_columns={k:record(v) for k,v in source0.items()},
        original_affine_HN1_columns={k:record(v) for k,v in source1.items()},
        full_final_source_L2_columns={k:record(v) for k,v in final0.items()},
        full_final_source_H1_columns={k:record(v) for k,v in final1.items()},
        strict_improvement_factors_over_previous_H1={k:record(v) for k,v in improvements.items()},
        high_inverse=dict(cutoff_exact=f'2^{high}',cutoff_decimal_digits=len(str(1<<high)),
            chosen=packed(chosen),preceding_dyadic=packed(previous),
            full_head_complex_dimension_exact=f'2^{high+2}',bound=record(K),
            unweighted_index_interval=['-4/3','0'],
            zero_final_head_high_L2_particular_columns={k:record(v) for k,v in high_source.items()},
            reconstructed_physical_boundary_amplitude_L2_columns_for_that_particular={k:record(v) for k,v in physical_source.items()},
            exact_full_Schur=rb['high_inverse']['exact_full_Schur']),
        exact_nonzero_head_equation=hs['exact_nonzero_head_equation'],high_projection=hs['high_projection'],
        full_b_analytic_modulus=nf['bounds']['full_b_analytic_modulus'],full_b_analytic_strip=nf['full_b_analytic_strip'],
        actual_beta_interval=ar['actual_beta_interval'],exact_quadratic=ar['exact_quadratic'],
        all_original_nonmean_cohomological_gauge_and_arithmetic_terms_retained=True,
        full_positive_Piola_height_gradient_and_mean_charge_retained=True,
        independent_boundary_vector_trace_not_bounded_by_bulk_vector_norm=True,
        stronger_source_to_original_base_source_embeddings_have_norm_one=True,
        all_four_branches_both_means_independent_regular_ports_and_head_crossings_retained=True,
        zero_final_head_does_not_mean_zero_physical_head=True,
        high_particular_is_not_a_solution_of_the_unpaid_finite_head_equations=True,
        finite_head_assembled=False,finite_head_inverse_proved=False,numerically_tractable_cutoff_proved=False,
        full_feedback_inverse_proved=False,full_Ctwo_surface_reconstructed=False,
        positive_fixed_angular_weight_proved=False,new_deep_tail_profile_transfer_proved=False,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_root_fourier_fit.py','fourfold_negative_collar_root_fourier_budget.py',
            'fourfold_negative_canonical_cancellation_chart.py')},
        gates=gates,seconds=time.monotonic()-tick)
    save(a.out,out)
    print(dict(complete=True,Rstar=R.str(12),calculus=calculus.str(12),
        cutoff=f'2^{high}',inverse=K.str(12),H1_negative=final1['negative_five_space_direct_sum'].str(12),
        H1_positive=final1['paired_positive_local_ordinary'].str(12),
        out=str(a.out),sha256=sha(a.out)),flush=True)


if __name__=='__main__':main()
