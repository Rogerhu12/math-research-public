#!/usr/bin/env python3
"""Actual complete negative scattering and cap feedback against a full operator word.

Preserves the original R43 phase, every R46 branch and every mean input.
The exact anti-J identities turn the strong Cauchy error into a strong
two-ended scattering error without another high-order Cauchy factor.
This full word is not yet the R104 scalar first-order normal form.
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
from fourfold_negative_root_physical_graph_operator import mult


def up(row):return stored(row).upper()
def lo(row):return stored(row).lower()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--graph',type=Path,default=Path('notes/2026-11-13-negative-root-physical-graph-operator.json'))
    p.add_argument('--strict',type=Path,default=Path('notes/2026-11-13-R46-windowed-density-strong-budget.json'))
    p.add_argument('--base',type=Path,default=Path('notes/2026-11-13-R46-strict-two-base-four-thirds.json'))
    p.add_argument('--cap',type=Path,default=Path('notes/2026-11-13-exact-positive-cap-Airy-contact-v2.json'))
    p.add_argument('--scattering',type=Path,default=Path('notes/2026-11-13-actual-central-scattering-and-source.json'))
    p.add_argument('--short-source',type=Path,default=Path('notes/2026-11-13-actual-central-scattering-reflected-source.json'))
    p.add_argument('--scale',type=int,default=1048576)
    p.add_argument('--bits',type=int,default=320)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise ValueError('a fresh output is required')
    ctx.prec=a.bits;tick=time.monotonic()
    g=checked(a.graph,'fourfold_negative_root_physical_graph_operator.py')
    c=checked(a.strict,'fourfold_strict_windowed_density_R46.py')
    b=checked(a.base,'fourfold_strict_base_four_thirds.py')
    cap=checked(a.cap,'fourfold_actual_exact_positive_cap_Airy_contact.py')
    sc=checked(a.scattering,'fourfold_actual_central_scattering_and_source.py')
    ss=checked(a.short_source,'fourfold_actual_central_scattering_reflected_source.py')
    if not c['identity']==b['identity']==sc['identity']==ss['identity']:
        raise ValueError('strict/scattering actual identities differ')
    if (sc['inputs'].get(str(a.graph))!=sha(a.graph)
        or sc['inputs'].get(str(a.cap))!=sha(a.cap)
        or sc['inputs'].get(str(a.strict))!=sha(a.strict)
        or b['inputs'].get(str(a.strict))!=sha(a.strict)
        or ss['inputs'].get(str(a.scattering))!=sha(a.scattering)):
        raise ValueError('the same whole graph, cap, strict and source realizations are required')
    N=a.scale
    if not N==b['scale']==sc['scale']==ss['scale']:raise ValueError('norm scales differ')
    gr=next(x for x in g['rows'] if x['scale']==N)
    cr=next(x for x in c['rows'] if x['scale']==N)
    amp={Fraction(x['window']):x for x in cr['complete_amplitude_windows']}
    wkb={Fraction(x['strong_window']):x for x in cr['complete_strong_windows']}
    rb={Fraction(x['input_order']):x for x in b['rows']}
    gain=Fraction(4,3)
    G=up(gr['complete_physical_GH_and_inverse'])
    Wg=up(gr['full_graph_W0'])
    Phi=up(g['complete_bounds']['complete_Airy_interface_model'])
    K=up(gr['full_root_to_actual_physical_cut'])
    Rk=up(gr['full_root_to_physical_cut_R4over3'])
    qlo=lo(cap['actual_quarter_circle_frequency'][0]);qhi=up(cap['actual_quarter_circle_frequency'][1])
    cAlo=lo(cap['complete_Airy_source']['c_A']);cAhi=up(cap['complete_Airy_source']['c_A'])
    kappa_lo=(8/(arb.pi()*cAhi*qhi)).lower()
    kappa_hi=(8/(arb.pi()*cAlo*qlo)).upper()
    ik=(1/kappa_lo).upper()
    L=exact_arb(Fraction(cap['actual_canonical_positive_height']))
    sigma=exact_arb(Fraction(cap['actual_canonical_angle_strip']))
    V=up(cap['complete_Airy_source']['potential_modulus'])
    phase=(V*L.sqrt()/qlo).upper()
    Bnorm=mult(N,gain,phase,qlo*sigma)
    # Purify only two finite mean matrices. D4-2I has norm 2 on the
    # output mean; Phi_mean-Phi_pure_mean is a pure input/output mean.
    M=(2*G*Wg*Phi*(1+Bnorm)).upper()
    mean_correction=(M+4*Phi).upper()
    Rkp=(Rk+mean_correction).upper()
    C0=up(amp[Fraction(0)]['amplitude_and_inverse'])
    Ws0=up(wkb[Fraction(0)]['full_W0_bound'])
    Wsg=up(wkb[gain]['full_W0_bound'])
    Rp=up(rb[Fraction(0)]['full_strict_four_thirds'])
    Rm=up(rb[-gain]['full_strict_four_thirds'])
    # The first term uses the true Cauchy at L2 only. The middle term
    # uses the explicitly paid positive or opposite base residual.
    shared=(Rkp*C0*K+M*Wsg*Rkp).upper()
    RTp=(ik*(shared+M*Rp*K)).upper()
    RTm=(ik*(shared+M*Rm*K)).upper()
    RT=max(RTp,RTm).upper()
    MT0=(ik*M*M*Ws0).upper();MTg=(ik*M*M*Wsg).upper()
    RS=(3*RT).upper()
    capR=up(cap['complete_original_frame']['right_and_left_full_four_thirds_remainder'])
    Ep=(capR+RS).upper()
    Em=(capR*max(arb(1),MTg+RS)+RS).upper()
    L0=(1+MT0).upper();Lg=(1+MTg).upper()
    reduced_p=(Lg*Ep*L0).upper();reduced_m=(L0*Em*Lg).upper()
    source=ss['bounds'];cb=sc['bounds']
    source_cols=dict(strict_core=L0*up(source['strict_core_source']),
        either_canonical_root=L0*up(source['either_canonical_root_source']),
        either_tilted_graph=L0*up(source['either_tilted_graph_source']),
        negative_five_space_direct_sum=L0*up(source['five_space_direct_sum_source']),
        paired_positive_local_ordinary=L0*up(cb['complete_positive_local_ordinary_source']),
        paired_positive_local_weak=L0*up(cb['complete_positive_local_weak_source']),
        two_independent_physical_regular_fluxes=L0*up(cb['actual_independent_regular_flux_to_wave_difference']))
    vals=dict(root_first_symmetric_phase_modulus=phase,
        root_first_symmetric_phase_HN_multiplier=Bnorm,
        positive_root_cut_flux_factor_lower=kappa_lo,positive_root_cut_flux_factor_upper=kappa_hi,
        reciprocal_root_cut_flux_factor=ik,
        complete_pure_antidiagonal_root_cut_model=M,
        complete_two_finite_mean_model_corrections=mean_correction,
        complete_purified_root_cut_four_thirds=Rkp,
        true_strict_L2_amplitude=C0,true_strict_four_thirds_forward=Rp,true_strict_four_thirds_opposite=Rm,
        full_negative_transfer_word_L2=MT0,full_negative_transfer_word_HN_plus_minus_four_thirds=MTg,
        full_negative_transfer_word_error_forward=RTp,full_negative_transfer_word_error_opposite=RTm,
        complete_scattering_word_error_both_base_windows=RS,
        complete_augmented_feedback_word_error_forward=Ep,
        complete_augmented_feedback_word_error_opposite=Em,
        complete_exact_triangular_preconditioner_and_reconstruction_L2=L0,
        complete_exact_triangular_preconditioner_and_reconstruction_HN_plus_minus_four_thirds=Lg,
        complete_single_return_word_remainder_forward=reduced_p,
        complete_single_return_word_remainder_opposite=reduced_m)
    out=dict(kind='actual_complete_central_strong_scattering_and_single_return_word',
        complete=True,proved=True,bits=a.bits,source_sha256=sha(__file__),identity=c['identity'],scale=N,
        inputs={str(x):sha(x) for x in (a.graph,a.strict,a.base,a.cap,a.scattering,a.short_source)},
        base_windows=[['0','4/3'],['-4/3','0']],native_cells_recomputed=0,
        root_cut_exact_flux='K_R^* J K_R=-kappa J; K_L=branch_swap*K_R; K_L^* J K_L=kappa J; kappa=4 gamma0^2=8/(pi*c_A*q)',
        exact_root_cut_inverse='K_R^(-1)=-kappa^(-1) J K_R^* J',
        root_cut_model='M_R=2 diag(Q_H,Q_H) W_graph branch_swap Phi_pure (I+B_original); M_L=branch_swap M_R',
        Phi_pure_mean='gamma0 diag(exp(i*pi/4),exp(-i*pi/4)); all nonzero entries equal the original Phi_app',
        complete_negative_transfer_word='M_T=-kappa^(-1) J M_R^* J W_strict M_L; it is exactly amplitude-antidiagonal',
        complete_scattering_word='S0=[[0,(M_T)12^*],[(M_T)21,0]]',
        exact_extra_flux_identities=['B^(-1) A=D^* (C^*)^(-1)','D B^(-1)=(C^*)^(-1) A^*',
            'B^(-1)=B^*-D^* D B^(-1)','B^(-*)=B-A A^* B^(-*)'],
        complete_cap_feedback='A=I-R_cap^* diag(S,I_regular)=I+diag(S0,I_regular)+E',
        exact_triangular_reduction='L=[[I,-U],[0,I]], R=[[I,0],[-V,I]], U=(M_T)12^*, V=(M_T)21; L*A*R=diag(I-U*V,I,2I_regular)+Rword',
        norms={k:record(v.upper() if k!='positive_root_cut_flux_factor_lower' else v.lower()) for k,v in vals.items()},
        full_transformed_ordinary_and_contact_source_columns={k:record(v.upper()) for k,v in source_cols.items()},
        both_original_Airy_rows_and_original_first_phase_retained=True,
        full_independent_regular_rows_and_sources_retained=True,full_mean_and_all_finite_head_paths_retained=True,
        actual_complete_strong_word_model_proved=True,
        R104_scalar_first_order_normal_form_identified=False,
        full_returned_Rstar_proved=False,full_returned_b_minus_beta_identified=False,
        weighted_same_width_bound_proved=False,feedback_inverse_proved=False,
        frozen_old_full_cap_Robin_realization_only=True,new_deep_tail_profile_transfer_proved=False,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_root_fourier_fit.py',
            'fourfold_negative_collar_root_fourier_budget.py',
            'fourfold_negative_canonical_cancellation_chart.py','fourfold_negative_root_physical_graph_operator.py')},
        seconds=time.monotonic()-tick)
    save(a.out,out)
    print(dict(complete=True,root_model=M.str(10),T_error_positive=RTp.str(10),
        T_error_opposite=RTm.str(10),scattering_error=RS.str(10),
        feedback_error=Ep.str(10),single_return_word_error=reduced_p.str(10),
        out=str(a.out),sha256=sha(a.out)),flush=True)


if __name__=='__main__':main()
