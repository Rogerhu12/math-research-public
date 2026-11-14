#!/usr/bin/env python3
"""Rebudget every complete physical H1 source with the actual Bessel Q bounds.

The strict, canonical, tilted and positive source maps are the previously
proved full maps.  Only the same-model word norms, exact final Q norm and
specified high inverse are replaced by the new complete bounds.  No field
or source is truncated and no native geometry is recomputed.
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
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--old-source',type=Path,default=Path('notes/2026-11-13-actual-return-Hone-source.json'))
    ap.add_argument('--new-return',type=Path,default=Path('notes/2026-11-13-actual-return-Bessel-rebudget.json'))
    ap.add_argument('--Q-budget',type=Path,default=Path('notes/2026-11-13-actual-density-Q-Bessel-budget-v2.json'))
    ap.add_argument('--bits',type=int,default=320)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args()
    if a.out.exists():raise ValueError('a fresh complete H1 source report is required')
    ctx.prec=a.bits;tick=time.monotonic()
    old=checked(a.old_source,'fourfold_actual_return_Hone_source.py')
    ret=checked(a.new_return,'fourfold_actual_return_Bessel_rebudget.py')
    qb=checked(a.Q_budget,'fourfold_actual_density_Q_Bessel_budget.py')
    if not (old['identity']==ret['identity']==qb['identity']
            and old['scale']==ret['scale']==qb['scale']
            and old['actual_parameter_scope']==ret['actual_parameter_scope']):
        raise ValueError('the same actual complete old realization is required')
    if ret['inputs'].get(str(a.Q_budget))!=sha(a.Q_budget):
        raise ValueError('the complete returned operator used another Q certificate')
    for path in set(old['inputs']).intersection(ret['inputs']):
        if old['inputs'][path]!=ret['inputs'][path]:
            raise ValueError('an original complete physical source input changed: '+path)
    N=int(old['scale']);rb=ret['bounds'];ob=old['bounds']
    T=up(rb['complete_model_half_word_and_full_antidiagonal_transfer'])
    RS=up(rb['unchanged_actual_strong_scattering_error'])
    capR=up(rb['unchanged_actual_full_cap_remainder'])
    if not (stored(rb['unchanged_actual_strong_scattering_error'])
            -stored(ob['full_scattering_strong_four_thirds'])).contains(0):
        raise ValueError('the actual strong scattering error changed')
    raw0={k:up(v) for k,v in old['complete_near_endpoint_raw_base_columns'].items()}
    raw1={k:up(v) for k,v in old['complete_near_endpoint_raw_HN1_columns'].items()}
    s0={k:up(v) for k,v in old['original_affine_base_columns'].items()}
    s1={k:up(v) for k,v in old['original_affine_HN1_columns'].items()}
    for k in raw0:s1[k]=(max(arb(1),T)*raw1[k]+RS*raw0[k]).upper()
    q0=up(rb['actual_final_Q_base']);q2=up(rb['actual_final_Q_plus_minus_two'])
    q1=(q0*q2).sqrt().upper();toH1=(N*q1).upper()
    triangle=(1+T).upper();correction=(triangle*capR+RS).upper()
    final0={k:(2*q0*s0[k]).upper() for k in s0}
    final1={k:(toH1*(triangle*s1[k]+correction*s0[k])).upper() for k in s0}
    def five(v):
        return (v['strict_core']**2+2*v['either_canonical_root']**2
                +2*v['either_tilted_graph']**2).sqrt().upper()
    final0['negative_five_space_direct_sum']=five(final0)
    final1['negative_five_space_direct_sum']=five(final1)
    hi=ret['high_inverse'];K=up(hi['bound'])
    reconstruction=up(rb['complete_physical_base_reconstruction'])
    high_cols={k:(K*v).upper() for k,v in final1.items()}
    physical_cols={k:(reconstruction*v).upper() for k,v in high_cols.items()}
    improvements={k:(stored(old['full_final_source_H1_columns'][k]).lower()/v).lower()
                  for k,v in final1.items()}
    gates=[]
    def gate(name,ok):
        gates.append(dict(name=name,passed=bool(ok)))
        if not ok:raise ValueError(name)
    gate('the stronger actual source maps preserve every physical column',
         old['all_four_branches_both_means_regular_rows_and_all_high_head_crossings_retained'])
    gate('the new word preserves every original mean, head crossing and regular port',
         ret['all_four_branches_both_means_regular_ports_and_head_crossings_retained'])
    gate('new full model bound is valid at the needed Sobolev index one',
         T<up(ob['same_model_HN1_norm']))
    gate('new Q certificate includes full inverse, adjoint and complete means',
         (stored(rb['actual_final_Q_base'])
          -stored(qb['rows']['actual_final_circle']['complete_unscaled_L2_Q_inverse_and_adjoints'])).contains(0)
         and (stored(rb['actual_final_Q_plus_minus_two'])
          -stored(qb['rows']['actual_final_circle']['full_Q_inverse_and_adjoints_plus_minus_two'])).contains(0))
    gate('same actual arithmetic high inverse includes index zero',
         hi['unweighted_index_interval']==['-4/3','0'] and K<16)
    gate('all complete final H1 columns strictly improve their former bound',
         all(v>1 for v in improvements.values()))
    out=dict(kind='actual_complete_return_Bessel_Hone_source_and_explicit_Ltwo_high_particular',
        complete=True,proved=True,source_sha256=sha(__file__),bits=a.bits,
        identity=old['identity'],actual_parameter_scope=old['actual_parameter_scope'],scale=N,
        geometric_and_local_source_bounds_uniform_in_original_whole_parameter_box=True,
        inputs={str(p):sha(p) for p in (a.old_source,a.new_return,a.Q_budget)},
        native_geometry_recomputed=0,
        exact_complete_original_source_maps_reused=True,
        source_units=old['source_units'],
        negative_source_partition=old['full_negative_source_partition'],
        exact_near_endpoint_affine_source=old['exact_near_endpoint_affine_source'],
        source_reflection=old['source_reflection'],
        ordered_complete_final_source=old['ordered_complete_final_source'],
        exact_ordered_expansion=old['exact_ordered_expansion'],
        source_HN1_estimate='||s||_HN1 <= T_* ||g||_HN1 + R_S ||g||_L2',
        final_H1_estimate='N0 sqrt(q0 q2) [(1+T_*) ||s||_HN1 + ((1+T_*) Ccap+R_S) ||s||_L2]',
        stronger_source_to_original_base_source_embeddings_have_norm_one=True,
        all_four_branches_both_means_independent_regular_ports_and_all_head_crossings_retained=True,
        full_positive_Piola_height_gradient_and_mean_charge_retained=True,
        independent_boundary_vector_trace_not_bounded_by_bulk_vector_norm=True,
        bounds={k:record(v) for k,v in dict(
            same_complete_model_HN1=T,unchanged_actual_strong_scattering_error=RS,
            unchanged_actual_full_cap_remainder=capR,model_left_triangle_HN1=triangle,
            triangle_cap_and_scattering_base_to_HN1_correction=correction,
            actual_final_Q_L2=q0,actual_final_Q_HN2=q2,actual_final_Q_HN1=q1,
            complete_final_Q_then_HN1_to_unscaled_H1=toH1,
            exact_high_inverse_H1_to_L2=K,
            full_physical_boundary_amplitude_reconstruction_L2=reconstruction).items()},
        complete_near_endpoint_raw_base_columns=old['complete_near_endpoint_raw_base_columns'],
        complete_near_endpoint_raw_HN1_columns=old['complete_near_endpoint_raw_HN1_columns'],
        original_affine_base_columns=old['original_affine_base_columns'],
        original_affine_HN1_columns={k:record(v) for k,v in s1.items()},
        full_final_source_L2_columns={k:record(v) for k,v in final0.items()},
        full_final_source_H1_columns={k:record(v) for k,v in final1.items()},
        strict_improvement_factors_over_original_H1_columns={k:record(v) for k,v in improvements.items()},
        cutoff_exact=hi['cutoff_exact'],full_head_complex_dimension_exact=hi['full_head_complex_dimension_exact'],
        zero_final_head_high_L2_particular_columns={k:record(v) for k,v in high_cols.items()},
        reconstructed_physical_boundary_amplitude_L2_columns_for_that_particular={k:record(v) for k,v in physical_cols.items()},
        high_projection=old['high_projection'],
        exact_nonzero_head_equation=old['exact_nonzero_head_equation'],
        exact_full_Schur=hi['exact_full_Schur'],
        zero_final_head_does_not_mean_zero_physical_head=True,
        high_particular_is_not_a_solution_of_the_unpaid_finite_head_equations=True,
        full_finite_head_inverse_proved=False,full_feedback_inverse_proved=False,
        full_Ctwo_surface_reconstructed=False,positive_fixed_angular_weight_proved=False,
        new_deep_tail_profile_transfer_proved=False,numerically_tractable_cutoff_proved=False,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_root_fourier_fit.py','fourfold_negative_collar_root_fourier_budget.py',
            'fourfold_negative_canonical_cancellation_chart.py')},
        gates=gates,seconds=time.monotonic()-tick)
    save(a.out,out)
    print(dict(complete=True,H1_core=final1['strict_core'].str(12),
        H1_root=final1['either_canonical_root'].str(12),
        H1_negative_direct_sum=final1['negative_five_space_direct_sum'].str(12),
        H1_positive_ordinary=final1['paired_positive_local_ordinary'].str(12),
        cutoff=hi['cutoff_exact'],high_inverse=K.str(12),out=str(a.out),sha256=sha(a.out)),flush=True)


if __name__=='__main__':main()
