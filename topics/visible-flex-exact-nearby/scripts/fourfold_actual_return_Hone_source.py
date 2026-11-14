#!/usr/bin/env python3
"""Complete actual H1 returned source and its explicit high particular.

Consumes the unchanged whole old cap, strict/root/graph and actual
transmission normal form. No native geometry is recomputed. All negative
ordinary source legs, positive ordinary/weak loads, and independent
regular fluxes remain separate with their original physical units.
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


def up(v):return stored(v).upper()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--normal-form',type=Path,default=Path('notes/2026-11-13-actual-two-cone-density-normal-form.json'))
    p.add_argument('--word',type=Path,default=Path('notes/2026-11-13-actual-central-strong-word.json'))
    p.add_argument('--strict',type=Path,default=Path('notes/2026-11-13-R46-windowed-density-strong-budget.json'))
    p.add_argument('--graph',type=Path,default=Path('notes/2026-11-13-negative-root-physical-graph-operator.json'))
    p.add_argument('--base-source',type=Path,default=Path('notes/2026-11-13-actual-central-scattering-and-source.json'))
    p.add_argument('--short-source',type=Path,default=Path('notes/2026-11-13-actual-central-scattering-reflected-source.json'))
    p.add_argument('--cap',type=Path,default=Path('notes/2026-11-13-exact-positive-cap-Airy-contact-v2.json'))
    p.add_argument('--cap-strong-source',type=Path,default=Path('notes/2026-11-13-actual-cap-stronger-source-window.json'))
    p.add_argument('--high-inverse',type=Path,default=Path('notes/2026-11-13-R104-actual-return-explicit-high-cutoff.json'))
    p.add_argument('--bits',type=int,default=320)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise ValueError('a fresh actual returned source report is required')
    ctx.prec=a.bits;tick=time.monotonic()
    nf=checked(a.normal_form,'fourfold_actual_return_symmetric_density_normal_form.py')
    word=checked(a.word,'fourfold_actual_central_strong_word.py')
    strict=checked(a.strict,'fourfold_strict_windowed_density_R46.py')
    graph=checked(a.graph,'fourfold_negative_root_physical_graph_operator.py')
    base=checked(a.base_source,'fourfold_actual_central_scattering_and_source.py')
    short=checked(a.short_source,'fourfold_actual_central_scattering_reflected_source.py')
    cap=checked(a.cap,'fourfold_actual_exact_positive_cap_Airy_contact.py')
    cs=checked(a.cap_strong_source,'fourfold_actual_cap_stronger_source_window.py')
    high=checked(a.high_inverse,'fourfold_actual_return_explicit_high_cutoff.py')
    if not (nf['identity']==word['identity']==strict['identity']==base['identity']
            ==short['identity']==high['identity']):
        raise ValueError('the actual strict/return family changed')
    if not (graph['identity']==cap['identity']==cs['identity']):
        raise ValueError('the complete source/canonical family changed')
    for parent,paths in (
        (nf,(a.word,a.strict,a.graph,a.base_source,a.short_source,a.cap)),
        (word,(a.strict,a.graph,a.base_source,a.short_source,a.cap)),
        (base,(a.strict,a.graph,a.cap)),
        (short,(a.base_source,a.strict,a.graph)),
        (cs,(a.cap,)),(high,(a.normal_form,))):
        for path in paths:
            if parent['inputs'].get(str(path))!=sha(path):
                raise ValueError('an upstream actual complete consumer used another input '+str(path))
    for path,digest in nf['extra_exact_inputs'].items():
        if sha(path)!=digest:raise ValueError('the exact final-circle input changed '+path)
    if (sha(Path('results/R77-reflection-square-of-principal-return.md'))
        !=short['actual_reflection_theorem_sha256']):
        raise ValueError('the same exact physical radial reflection is required')
    N=int(nf['scale'])
    if not N==int(word['scale'])==int(base['scale'])==int(short['scale']):
        raise ValueError('the existing complete norm scales differ')
    gr=next(x for x in graph['rows'] if int(x['scale'])==N)
    st=next(x for x in strict['rows'] if int(x['scale'])==N)
    windows={Fraction(x['window']):x for x in st['complete_amplitude_windows']}
    w0,w4=windows[Fraction(0)],windows[Fraction(4,3)]
    C1=(up(w0['amplitude_and_inverse'])**(arb(1)/4)
        *up(w4['amplitude_and_inverse'])**(arb(3)/4)).upper()
    Sc1=(up(w0['ordinary_source_to_amplitude'])**(arb(1)/4)
         *up(w4['ordinary_source_to_amplitude'])**(arb(3)/4)).upper()
    Ki=up(gr['full_actual_physical_cut_to_root'])
    Sr=up(gr['root_source_leg_gain']);Sg=up(gr['graph_source_leg_gain'])
    Shalf=up(short['complete_half_core_L1_HNminus_half_to_amplitude'])
    raw0=dict(strict_core=(Ki*Shalf).upper(),
              either_canonical_root=(Ki*Sr).upper(),
              either_tilted_graph=(Ki*Sg).upper())
    raw1=dict(strict_core=(Ki*Sc1).upper(),
              either_canonical_root=(Ki*Sr).upper(),
              either_tilted_graph=(Ki*Sg).upper())
    norms=word['norms']
    T1=(up(norms['full_negative_transfer_word_L2'])**(arb(1)/4)
        *up(norms['full_negative_transfer_word_HN_plus_minus_four_thirds'])**(arb(3)/4)).upper()
    RS=up(norms['complete_scattering_word_error_both_base_windows'])
    s1={k:(max(arb(1),T1)*raw1[k]+RS*raw0[k]).upper() for k in raw0}
    sb=short['bounds'];bb=base['bounds']
    s0=dict(strict_core=up(sb['strict_core_source']),
            either_canonical_root=up(sb['either_canonical_root_source']),
            either_tilted_graph=up(sb['either_tilted_graph_source']))
    cap0=next(x for x in cs['rows'] if Fraction(x['order'])==0)
    cap1=next(x for x in cs['rows'] if Fraction(x['order'])==1)
    s0.update(paired_positive_local_ordinary=up(bb['complete_positive_local_ordinary_source']),
              paired_positive_local_weak=up(bb['complete_positive_local_weak_source']),
              two_independent_physical_regular_fluxes=up(bb['actual_independent_regular_flux_to_wave_difference']))
    s1.update(paired_positive_local_ordinary=up(cap1['averaged_root_and_regular_outgoing_ordinary']),
              paired_positive_local_weak=up(cap1['averaged_root_and_regular_outgoing_weak']),
              two_independent_physical_regular_fluxes=s0['two_independent_physical_regular_fluxes'])
    capR=up(cap['complete_original_frame']['right_and_left_full_four_thirds_remainder'])
    triangle=(1+T1).upper()
    correction=(triangle*capR+RS).upper()
    qc=nf['final_root_label_bounds']
    q0=up(qc['exact_unscaled_base_Q_and_inverse'])
    q2=up(qc['complete_Q_and_inverse_plus_minus_two'])
    q1=(q0*q2).sqrt().upper()
    toH1=(N*q1).upper()
    final0={k:(2*q0*s0[k]).upper() for k in s0}
    final1={k:(toH1*(triangle*s1[k]+correction*s0[k])).upper() for k in s0}
    def five(v):
        return (v['strict_core']**2+2*v['either_canonical_root']**2
                +2*v['either_tilted_graph']**2).sqrt().upper()
    final0['negative_five_space_direct_sum']=five(final0)
    final1['negative_five_space_direct_sum']=five(final1)
    high_bound=up(high['complete_high_inverse_bound'])
    reconstruction=up(nf['bounds']['complete_physical_reconstruction_L2'])
    high_cols={k:(high_bound*v).upper() for k,v in final1.items()}
    physical_cols={k:(reconstruction*v).upper() for k,v in high_cols.items()}
    gates=[]
    def gate(name,ok):
        gates.append(dict(name=name,passed=bool(ok)))
        if not ok:raise ValueError(name)
    gate('the complete actual original scattering is onto',
         base['genuine_onto_scattering'] and up(bb['full_negative_scattering_and_inverse'])==1)
    gate('all final means, finite head crossings and regular rows were retained',
         nf['all_four_branches_both_means_independent_regular_rows_and_head_paths_retained'])
    gate('same full physical-to-averaged root normalization at source order zero',
         (stored(cap0['averaged_root_and_regular_outgoing_ordinary'])
          -stored(bb['complete_positive_local_ordinary_source'])).contains(0)
         and (stored(cap0['averaged_root_and_regular_outgoing_weak'])
          -stored(bb['complete_positive_local_weak_source'])).contains(0))
    gate('full cap reflection and both strong source endpoints are present',
         cap['full_augmented_regular_and_root_mean_retained']
         and cs['full_root_mean_and_regular_mean_charge_retained']
         and cs['interpolation_interval']==['0','4/3'])
    gate('old high inverse genuinely includes s zero',
         high['paid_unweighted_index_interval']==['-4/3','0'])
    gate('same actual parameter scope for the normal form and high inverse',
         high['actual_parameter_scope']==nf['actual_parameter_scope'])
    out=dict(kind='actual_full_old_return_Hone_source_and_explicit_high_Ltwo_particular',
        complete=True,proved=True,source_sha256=sha(__file__),bits=a.bits,
        identity=nf['identity'],actual_parameter_scope=nf['actual_parameter_scope'],
        geometric_and_local_source_bounds_uniform_in_original_whole_parameter_box=True,
        scale=N,cutoff_exact=high['cutoff_exact'],cutoff_integer=high['cutoff_integer'],
        inputs={str(x):sha(x) for x in (a.normal_form,a.word,a.strict,a.graph,
            a.base_source,a.short_source,a.cap,a.cap_strong_source,a.high_inverse)},
        native_geometry_recomputed=0,all_215_strict_cells_both_root_connectors_and_full_caps_reused=True,
        full_negative_source_partition='f=f*1_(r<0)+f*1_(r>=0); their L1 radial norms sum exactly to the original whole-core norm',
        exact_near_endpoint_affine_source=['(g_minus,0)-S*(g_plus,0)',
                                          '(0,g_minus)-S*(0,g_plus)'],
        model_scattering='S0=[[0,U],[V,0]]; both U,V use the same complete actual strong-word model',
        source_reflection='the exact physical radial reflection preserves theta and the full canonical root angle; inward conormal and the complete branch permutation are retained',
        high_window_scattering_source='norm_HN1(s)<=T1*norm_HN1(g)+RS*norm_L2(g); all input and output modes retained',
        ordered_complete_final_source='unitary_cone_rotation_reflection * diag(Q_C,I,I_regular) * L_e * R_cap^* * ((s_neg,i*sqrt(pi*c_A/ell)*lambda)-h_cap)',
        exact_ordered_expansion='L_e*R_cap^*=L_m*(-I+(R_cap^*+I))+(L_e-L_m)*R_cap^*; only the last R_cap^* uses base unitarity',
        source_units=dict(
            strict_core='L1(dr; H_N^(1/2)) of the original physical scalar source, normalized physical angle x=4theta',
            either_canonical_root='L1(dxi; H_N^(2/3)) of the exact canonical ordinary source on the same valid extension',
            either_tilted_graph='L1(dt; H_N^(1/2)) of the corresponding exact density f_t=(L-chi)*f_c/q on that same extension',
            paired_positive_local_ordinary='paired l2 norm of physical-measure L2(dy; H_phi^(1/3)) canonical collar scalars',
            paired_positive_local_weak='paired l2 norm of (F_y,F_phi/sqrt(y)) in physical-measure L2(dy;(H_phi^1)^2), with the original weak load convention',
            two_independent_physical_regular_fluxes='Euclidean norm of the two independent physical normalized scalar regular fluxes'),
        stronger_source_to_original_base_source_embeddings_have_norm_one=True,
        full_positive_Piola_height_gradient_and_mean_charge_retained=True,
        independent_boundary_vector_trace_not_bounded_by_bulk_vector_norm=True,
        bounds={k:record(v) for k,v in dict(
            strict_HN1_Cauchy_amplitude_and_inverse=C1,
            strict_L1_HNhalf_source_to_HN1_amplitude=Sc1,
            same_model_HN1_norm=T1,full_scattering_strong_four_thirds=RS,
            model_left_triangle_HN1=triangle,
            triangle_cap_and_scattering_base_to_HN1_correction=correction,
            actual_final_Q_HN1=q1,complete_final_Q_then_HN1_to_unscaled_H1=toH1,
            exact_high_inverse_H1_to_L2=high_bound,
            full_physical_boundary_amplitude_reconstruction_L2=reconstruction).items()},
        complete_near_endpoint_raw_base_columns={k:record(v) for k,v in raw0.items()},
        complete_near_endpoint_raw_HN1_columns={k:record(v) for k,v in raw1.items()},
        original_affine_base_columns={k:record(v) for k,v in s0.items()},
        original_affine_HN1_columns={k:record(v) for k,v in s1.items()},
        full_final_source_L2_columns={k:record(v) for k,v in final0.items()},
        full_final_source_H1_columns={k:record(v) for k,v in final1.items()},
        zero_final_head_high_L2_particular_columns={k:record(v) for k,v in high_cols.items()},
        reconstructed_physical_boundary_amplitude_L2_columns_for_that_particular={k:record(v) for k,v in physical_cols.items()},
        high_projection=high['complete_high_projection'],
        exact_nonzero_head_equation='u_H=A_H^-1*(P_H*g-A_HL*u_L); all head equations and Schur terms remain',
        zero_final_head_does_not_mean_zero_physical_head=True,
        high_particular_is_not_a_solution_of_the_unpaid_finite_head_equations=True,
        all_four_branches_both_means_regular_rows_and_all_high_head_crossings_retained=True,
        full_finite_head_inverse_proved=False,full_feedback_inverse_proved=False,
        full_Ctwo_surface_reconstructed=False,positive_fixed_angular_weight_proved=False,
        new_deep_tail_profile_transfer_proved=False,numerically_tractable_cutoff_proved=False,
        gates=gates,dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_root_fourier_fit.py',
            'fourfold_negative_collar_root_fourier_budget.py','fourfold_negative_canonical_cancellation_chart.py')},
        seconds=time.monotonic()-tick)
    save(a.out,out)
    print(dict(complete=True,H1_core=final1['strict_core'].str(12),
        H1_root=final1['either_canonical_root'].str(12),
        H1_positive_ordinary=final1['paired_positive_local_ordinary'].str(12),
        high_inverse=high_bound.str(12),out=str(a.out),sha256=sha(a.out)),flush=True)


if __name__=='__main__':main()

