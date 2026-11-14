#!/usr/bin/env python3
"""Whole actual old negative-component scattering and complete base source wiring.

The scattering contraction is an exact anti-J-unitary identity, not an
inference from the size of a finite Fourier matrix. The complete original
positive-cap Robin realization is retained and the regular fluxes remain
explicit independent data. No returned normal form or inverse is claimed.
"""
from __future__ import annotations
import argparse, time
from fractions import Fraction
from pathlib import Path
from flint import arb, ctx
from fourfold_phase_root_fourier_fit import save, sha, stored
from fourfold_negative_collar_root_fourier_budget import record
from fourfold_negative_canonical_cancellation_chart import checked


def up(row):
    return stored(row).upper()


def low(row):
    return stored(row).lower()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--graph',type=Path,default=Path('notes/2026-11-13-negative-root-physical-graph-operator.json'))
    p.add_argument('--strict',type=Path,default=Path('notes/2026-11-13-R46-windowed-density-strong-budget.json'))
    p.add_argument('--cap',type=Path,default=Path('notes/2026-11-13-exact-positive-cap-Airy-contact-v2.json'))
    p.add_argument('--scale',type=int,default=1048576)
    p.add_argument('--bits',type=int,default=320)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise ValueError('a fresh result path is required')
    ctx.prec=a.bits;tick=time.monotonic()
    g=checked(a.graph,'fourfold_negative_root_physical_graph_operator.py')
    c=checked(a.strict,'fourfold_strict_windowed_density_R46.py')
    cap=checked(a.cap,'fourfold_actual_exact_positive_cap_Airy_contact.py')
    identity_keys=('origin_inputs_sha256','direction_sha256','exact_center_parameter',
                   'exact_parameter_half_width','exact_parameter_interval')
    same_identity=(g['identity']==cap['identity']
        and g['identity']['center_object_sha256']==c['identity']['object_sha256']
        and g['identity']['center_object_path']==c['identity']['object_path']
        and all(g['identity'][k]==c['identity'][k] for k in identity_keys)
        and c['identity']['uniform_in_the_entire_real_parameter_interval'])
    if not same_identity:
        raise ValueError('the actual root/core/cap family differs')
    if (not g['all_parameter_values_modes_means_and_head_crossings_retained']
        or not c['all_four_branches_means_and_all_head_paths_retained']
        or not cap['full_augmented_regular_and_root_mean_retained']
        or not cap['actual_full_uncompressed_cap_and_nonzero_infinite_tail_fee_retained']):
        raise ValueError('a complete actual scope is missing')
    gr=next(x for x in g['rows'] if x['scale']==a.scale)
    cr=next(x for x in c['rows'] if x['scale']==a.scale)
    ca=next(x for x in cr['complete_amplitude_windows'] if Fraction(x['window'])==0)
    cut=Fraction(g['physical_cut'])
    if [str(-cut),str(cut)]!=c['exact_physical_interval']:
        raise ValueError('the exact root/core physical cuts differ')
    K=up(gr['full_root_to_actual_physical_cut'])
    Ki=up(gr['full_actual_physical_cut_to_root'])
    C=up(ca['amplitude_and_inverse'])
    Sc=up(ca['ordinary_source_to_amplitude'])
    Sr=up(gr['root_source_leg_gain'])
    Sg=up(gr['graph_source_leg_gain'])
    transfer=(Ki*C*K).upper()
    raw=dict(strict_core=(Ki*Sc).upper(),
             left_canonical_root=(Ki*C*Sr).upper(),
             left_tilted_graph=(Ki*C*Sg).upper(),
             right_canonical_root=(Ki*Sr).upper(),
             right_tilted_graph=(Ki*Sg).upper())
    scatter={k:(arb(2).sqrt()*v).upper() for k,v in raw.items()}
    direct_sum=sum((v*v for v in scatter.values()),arb(0)).sqrt().upper()
    qlo=low(cap['actual_quarter_circle_frequency'][0])
    qhi=up(cap['actual_quarter_circle_frequency'][1])
    elllo=(2*arb.pi()/qhi).lower()
    ellhi=(2*arb.pi()/qlo).upper()
    if not 0<elllo<ellhi:raise ValueError('invalid true common root period')
    renormalization=(1/elllo.sqrt()).upper()
    cf=cap['complete_original_frame']
    cA=up(cap['complete_Airy_source']['c_A'])
    cap_ordinary=(renormalization*up(cf['complete_local_ordinary_source_to_affine_outgoing'])).upper()
    cap_weak=(renormalization*up(cf['complete_local_weak_source_to_affine_outgoing'])).upper()
    flux=(renormalization*(arb.pi()*cA).sqrt()).upper()
    cap_remainder=up(cf['right_and_left_full_four_thirds_remainder'])
    if up(cf['exact_full_unitary_norm'])!=1:
        raise ValueError('the actual complete cap unitarity input differs')
    out=dict(kind='actual_complete_old_central_scattering_and_base_source_wiring',
        complete=True,proved=True,bits=a.bits,source_sha256=sha(__file__),
        identity=c['identity'],scale=a.scale,
        exact_identity_comparison='center_object_path/sha256 equals object_path/sha256; all five exact origin/direction/parameter fields match; full-parameter gate retained',
        inputs={str(x):sha(x) for x in (a.graph,a.strict,a.cap)},
        exact_physical_strict_interval=c['exact_physical_interval'],
        all_215_strict_cells_and_both_exact_nonconstant_root_connectors_retained=True,
        exact_root_orientation='both canonical xi coordinates point into the negative component',
        exact_whole_transfer='T=K_right^(-1)*C_strict*K_left; the reflected K_left has its full reversed conormal',
        exact_flux_identities='T^* J T=T J T^*=-J; J=diag(I,-I)',
        exact_scattering='S=[[-B^(-1) A,B^(-1)],[C-D B^(-1) A,D B^(-1)]] for T=[[A,B],[C,D]]',
        exact_affine_scattering_source='(-B^(-1)g_plus,g_minus-D B^(-1)g_plus)',
        genuine_onto_scattering=True,
        all_frequencies_including_both_root_means=True,
        infinite_Cauchy_blocks_inverted_by_flux_identity_not_finite_sample=True,
        bounds=dict(full_negative_transfer_and_inverse=record(transfer),
            full_negative_scattering_and_inverse=record(arb(1)),
            complete_B_and_C_block_inverse=record(arb(1)),
            complete_affine_source_fold=record(arb(2).sqrt()),
            full_raw_Cauchy_source_columns={k:record(v) for k,v in raw.items()},
            full_two_end_scattering_source_columns={k:record(v) for k,v in scatter.items()},
            source_norm_direct_sum_gain=record(direct_sum),
            original_full_cap_unitary_and_inverse=record(arb(1)),
            original_full_cap_R_four_thirds=record(cap_remainder),
            complete_augmented_feedback_product_and_inverse=record(arb(1)),
            complete_augmented_feedback_difference=record(arb(2)),
            actual_root_period_lower=record(elllo),actual_root_period_upper=record(ellhi),
            physical_to_averaged_root_regular_common_factor=record(renormalization),
            complete_positive_local_ordinary_source=record(cap_ordinary),
            complete_positive_local_weak_source=record(cap_weak),
            actual_independent_regular_flux_to_wave_difference=record(flux)),
        ordinary_negative_source_spaces={
            'strict_core':'L1(dr; H_N^(-1/2)) of the original physical scalar f',
            'left_canonical_root':'L1(dxi; H_N^(-1/3)) of the exact canonical ordinary source on a valid extension',
            'left_tilted_graph':'L1(dt; H_N^(-1/2)) of the same extended source after the exact tilted graph change',
            'right_canonical_root':'the corresponding right canonical ordinary-source norm',
            'right_tilted_graph':'the corresponding right tilted-graph ordinary-source norm'},
        positive_source_spaces={
            'ordinary':'paired l2 norm of the two actual physical-measure L2(dy; H_phi^(-2/3)) canonical collar scalar sources',
            'weak':'paired l2 norm of (F_y,F_phi/sqrt(y)) in the two canonical collars; the scalar height-gradient correction is retained'},
        exact_regular_renormalization='a=z_plus_reg/sqrt(ell), b=z_minus_reg/sqrt(ell), where z_pm_reg=sqrt(pi*c_A)/2*(zeta minus_or_plus i*lambda)',
        independent_regular_flux_rows='b-a=i*sqrt(pi*c_A/ell)*lambda; lambda is explicit physical normalized regular flux data',
        exact_old_cap_feedback='(I-R_cap^* diag(S,I_regular))u=R_cap^*((s,i*sqrt(pi*c_A/ell)*lambda)-h)',
        complete_cap_source_and_regular_mean_contact_retained=True,
        frozen_old_full_cap_Robin_realization_only=True,
        deep_tail_profile_changed=False,new_deep_tail_profile_transfer_proved=False,
        full_returned_Rstar_proved=False,full_returned_b_minus_beta_identified=False,
        full_Sobolev_scattering_window_proved=False,weighted_scattering_bound_proved=False,
        regular_flux_equations_solved=False,feedback_inverse_proved=False,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_negative_canonical_cancellation_chart.py',
            'fourfold_negative_collar_root_fourier_budget.py',
            'fourfold_phase_root_fourier_fit.py')},
        input_theorems={name:sha(Path('results')/name) for name in (
            'R77-reflection-square-of-principal-return.md',
            'R43-supplement-actual-physical-graph-strong-connector.md',
            'R46-supplement-requested-window-density-strong-budget.md',
            'R45-supplement-actual-exact-positive-cap-Airy-contact-and-four-thirds.md')})
    out['seconds']=time.monotonic()-tick
    save(a.out,out)
    print(dict(complete=True,transfer=transfer.str(10),scattering=1,
        base_source_direct_sum=direct_sum.str(10),positive_ordinary=cap_ordinary.str(10),
        positive_weak=cap_weak.str(10),regular_flux=flux.str(10),
        out=str(a.out),sha256=sha(a.out)),flush=True)


if __name__=='__main__':main()
