#!/usr/bin/env python3
"""Reconsume the complete actual root/cut connector and genuine scattering.

The paired potential, full two-row Airy change and exact full Bessel Q norms
replace earlier upper bounds for the same maps. Every original graph/strict
source, mean correction and actual strong error remains present. No native
field, complete chart or physical source realization is recomputed.
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
from fourfold_negative_root_full_Airy_operator import triangle,lag_moment
from fourfold_actual_return_symmetric_density_normal_form import phase_bounds
from fourfold_negative_root_physical_graph_operator import mult


def up(z):return stored(z).upper()
def lo(z):return stored(z).lower()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--graph',type=Path,default=Path('notes/2026-11-13-negative-root-physical-graph-operator.json'))
    p.add_argument('--potential',type=Path,default=Path('notes/2026-11-13-actual-root-common-flow-potential.json'))
    p.add_argument('--Airy-change',type=Path,default=Path('notes/2026-11-13-actual-root-sharp-Airy-frames.json'))
    p.add_argument('--Q-budget',type=Path,default=Path('notes/2026-11-13-actual-density-Q-Bessel-budget-v2.json'))
    p.add_argument('--word',type=Path,default=Path('notes/2026-11-13-actual-central-strong-word.json'))
    p.add_argument('--return-budget',type=Path,default=Path('notes/2026-11-13-actual-return-Bessel-rebudget.json'))
    p.add_argument('--old-Hone-source',type=Path,default=Path('notes/2026-11-13-actual-return-Hone-source.json'))
    p.add_argument('--bits',type=int,default=384)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise ValueError('fresh complete actual connector budget required')
    ctx.prec=a.bits;tick=time.monotonic()
    g=checked(a.graph,'fourfold_negative_root_physical_graph_operator.py')
    v=checked(a.potential,'fourfold_actual_root_common_flow_potential.py')
    ch=checked(a.Airy_change,'fourfold_actual_root_sharp_Airy_frames.py')
    q=checked(a.Q_budget,'fourfold_actual_density_Q_Bessel_budget.py')
    w=checked(a.word,'fourfold_actual_central_strong_word.py')
    rb=checked(a.return_budget,'fourfold_actual_return_Bessel_rebudget.py')
    hs=checked(a.old_Hone_source,'fourfold_actual_return_Hone_source.py')
    if not g['identity']==v['identity']==ch['identity']:
        raise ValueError('same complete canonical/root/graph family required')
    if not q['identity']==w['identity']==rb['identity']==hs['identity']:
        raise ValueError('same complete original strict/return family required')
    for key in ('origin_inputs_sha256','direction_sha256','exact_center_parameter','exact_parameter_interval'):
        if g['identity'][key]!=w['identity'][key]:raise ValueError('the underlying geometric family differs')
    for parent,path in ((q,a.graph),(w,a.graph),(rb,a.word),(rb,a.Q_budget),(rb,a.potential)):
        if parent['inputs'].get(str(path))!=sha(path):raise ValueError('a complete original map input differs')
    op=Path('notes/2026-11-13-negative-root-full-Airy-operator-additional-scale.json')
    root=checked(op,'fourfold_negative_root_full_Airy_operator.py')
    if g['inputs'].get(str(op))!=sha(op) or root['identity']!=g['identity']:
        raise ValueError('same original complete shifted-Airy reference required')
    N=int(w['scale'])
    if not N==int(q['scale'])==int(rb['scale'])==int(hs['scale']):
        raise ValueError('same complete finite norm scale required')
    gr=next(z for z in g['rows'] if int(z['scale'])==N)
    oldroot=next(z for z in root['rows'] if int(z['scale'])==N)
    L=exact_arb(Fraction(v['canonical_real_half_height']))
    sigma=exact_arb(Fraction(v['canonical_complex_angle_strip']))
    if str(Fraction(v['canonical_real_half_height']))!=root['exact_canonical_height']:
        raise ValueError('same actual real collar required')
    qlo=lo(v['actual_quarter_circle_frequency'][0])
    V=up(v['bounds']['full_canonical_potential'])
    Vxi=up(v['bounds']['full_real_segment_radial_derivative'])
    W=up(v['bounds']['full_shifted_5050_residual'])
    change=up(ch['bounds']['complete_full_frame_change_and_inverse'])
    decay=(qlo*sigma).lower();eta=L*L/2
    derivatives=[W]+[(arb(j).fac()*V/decay**j).upper() for j in range(1,4)]
    _,_,M,RH=triangle(N,derivatives,eta)
    MM=max(M).upper();RR=max(RH).upper()
    ref=root['reference_bounds']
    CD=up(ref['CD']);CG=up(ref['CG']);Gamma=up(ref['ordinary_source_to_reference_amplitude'])
    Cq=up(ref['Cq'])
    Cshift=(1+Gamma*L*MM*RR*arb(2).sqrt()*CD).upper()
    Sshift=(Gamma*(1+L*MM*RR*CG)).upper()
    Croot=(change**2*Cshift).upper();Sroot=(change*Sshift).upper()
    Bgain=(100*arb.pi()*max(M[:3])).upper()
    higher=(2*Croot*L*Bgain**2).upper()
    rootR={};rootfirst={}
    for s in (Fraction(0),Fraction(-4,3)):
        power=(abs(s+Fraction(4,3)).numerator+abs(s+Fraction(4,3)).denominator-1)//abs(s+Fraction(4,3)).denominator
        lag,_,_=lag_moment(N,decay,power)
        first=(2*Cq*(V+Vxi)*lag).upper()
        rootfirst[str(s)]=first;rootR[str(s)]=(first+higher).upper()
    Rroot=max(rootR.values()).upper()
    phase=(V*L.sqrt()/qlo).upper()
    root_phase=phase_bounds(N,phase,decay)
    Broot=up(rb['phase_factor_budget']['root']['same_order'])
    # Same complete root phase; this record was produced with the paired V.
    if not (stored(rb['phase_factor_budget']['root']['same_order'])
            -root_phase['same_order']).contains(0):
        raise ValueError('new actual root phase norm does not match the same return')
    gb=g['complete_bounds']
    Phi=up(gb['full_Airy_to_strict_matrix'])
    Phi_inv=up(gb['full_inverse_Airy_to_strict_matrix'])
    Phi_model=up(gb['complete_Airy_interface_model'])
    Cgraph=up(gr['full_graph_amplitude_and_inverse'])
    Sgraph=up(gr['full_graph_ordinary_source'])
    Rgraph=up(gr['full_graph_R2'])
    Rphi=up(gr['entire_Airy_interface_R2'])
    RG=up(gr['physical_GH_minus_diagonal_QH_R2'])
    Qp0=up(q['rows']['physical_cut']['complete_unscaled_L2_Q_inverse_and_adjoints'])
    Qp2=up(q['rows']['physical_cut']['full_Q_inverse_and_adjoints_plus_minus_two'])
    Qg0=up(q['rows']['graph']['complete_unscaled_L2_Q_inverse_and_adjoints'])
    Qg2=up(q['rows']['graph']['full_Q_inverse_and_adjoints_plus_minus_two'])
    Qs0=up(q['rows']['strict']['complete_unscaled_L2_Q_inverse_and_adjoints'])
    Qs2=up(q['rows']['strict']['full_Q_inverse_and_adjoints_plus_minus_two'])
    # Exact full G_H is Hadamard diag(Q_H,Q_H^{-*}) Hadamard, including mean.
    # Compressed graph/strict model branches use the exact same phase factors.
    hg=up(rb['phase_factor_budget']['graph']['same_order'])
    hstrict=up(rb['phase_factor_budget']['strict']['same_order'])
    Wg0=max(arb(1),(Qg0*(1+hg)).upper())
    Wg2=max(arb(1),(Qg2*(1+hg)).upper())
    Ws0=max(arb(1),(Qs0*(1+hstrict)).upper())
    Ws2=max(arb(1),(Qs2*(1+hstrict)).upper())
    K0=(4*Qp0*Cgraph*Phi*Croot).upper()
    Ki0=(Croot*Phi_inv*Cgraph*Qp0).upper()
    K2=(4*Qp2*Cgraph*Phi*Croot).upper()
    Ki2=(Croot*Phi_inv*Cgraph*Qp2).upper()
    Rk=(4*(Qp2*Rgraph*Phi*Croot+Qp2*Wg2*Rphi*Croot
           +RG*Wg2*Phi_model*Croot+Qp2*Wg2*Phi_model*Rroot)).upper()
    Sr0=(4*Qp0*Cgraph*Phi*Sroot).upper();Sg0=(4*Qp0*Sgraph).upper()
    Sr2=(4*Qp2*Cgraph*Phi*Sroot).upper();Sg2=(4*Qp2*Sgraph).upper()
    # The same finite mean purification as the original complete word:
    # its error is a proved finite-rank correction, not a change of the PDE.
    model0=(2*Qp0*Wg0*Phi_model*(1+Broot)).upper()
    model2=(2*Qp2*Wg2*Phi_model*(1+Broot)).upper()
    meanfee=(model2+4*Phi_model).upper()
    Rkp=(Rk+meanfee).upper()
    wn=w['norms'];Cstrict=up(wn['true_strict_L2_amplitude'])
    Rp=up(wn['true_strict_four_thirds_forward']);Rm=up(wn['true_strict_four_thirds_opposite'])
    ik=up(wn['reciprocal_root_cut_flux_factor'])
    # All outside Sobolev orders are between -4/3 and 4/3.
    shared=(Rkp*Cstrict*K2+model2*Ws2*Rkp).upper()
    RTp=(ik*(shared+model2*Rp*K2)).upper()
    RTm=(ik*(shared+model2*Rm*K2)).upper()
    RS=(3*max(RTp,RTm)).upper()
    # Complete near-endpoint source rows, retaining original source units.
    oldKi=up(gr['full_actual_physical_cut_to_root'])
    Sc1=up(hs['bounds']['strict_L1_HNhalf_source_to_HN1_amplitude'])
    # Use the original exact reflected-source theorem directly.
    sp=Path('notes/2026-11-13-actual-central-scattering-reflected-source.json')
    short=checked(sp,'fourfold_actual_central_scattering_reflected_source.py')
    if w['inputs'].get(str(sp))!=sha(sp):raise ValueError('same original affine source required')
    Shalf=up(short['complete_half_core_L1_HNminus_half_to_amplitude'])
    raw0=dict(strict_core=(Ki0*Shalf).upper(),
        either_canonical_root=(Ki0*Sr0).upper(),either_tilted_graph=(Ki0*Sg0).upper())
    raw1=dict(strict_core=(Ki2*Sc1).upper(),
        either_canonical_root=(Ki2*Sr2).upper(),either_tilted_graph=(Ki2*Sg2).upper())
    s0={k:(arb(2).sqrt()*z).upper() for k,z in raw0.items()}
    s0['negative_five_space_direct_sum']=(s0['strict_core']**2+
        2*s0['either_canonical_root']**2+2*s0['either_tilted_graph']**2).sqrt().upper()
    gates=[]
    def gate(name,ok):
        gates.append(dict(name=name,passed=bool(ok)))
        if not ok:raise ValueError(name)
    gate('the full scalar height Volterra diagonal is paid',eta*W<arb(1)/40)
    gate('the same complete root amplitude and source bounds improve',
         Croot<up(oldroot['original_R39_full_amplitude_propagation_and_inverse'])
         and Sroot<up(oldroot['original_R39_full_ordinary_source']))
    gate('the same exact full physical angle operator uses the paid Bessel norm',
         Qp2<up(gr['complete_physical_GH_and_inverse']))
    gate('the same complete graph and strict model norms improve',
         Wg2<up(gr['full_graph_W0']) and Ws2<up(wn['full_negative_transfer_word_HN_plus_minus_four_thirds']))
    gate('the complete actual root/cut connector improves in both directions',
         K2<up(gr['full_root_to_actual_physical_cut']) and Ki2<oldKi)
    gate('the complete actual strong scattering error improves',
         RS<up(wn['complete_scattering_word_error_both_base_windows']))
    out=dict(kind='actual_complete_root_cut_and_true_strong_scattering_rebudget',
        complete=True,proved=True,source_sha256=sha(__file__),bits=a.bits,
        identity=w['identity'],root_identity=g['identity'],scale=N,
        actual_parameter_scope=rb['actual_parameter_scope'],
        entire_original_real_parameter_box_for_all_local_geometry=True,
        inputs={str(p):sha(p) for p in (a.graph,a.potential,a.Airy_change,a.Q_budget,
            a.word,a.return_budget,a.old_Hone_source,op,sp)},
        native_geometry_recomputed=0,all_original_realization_maps_and_first_phases_unchanged=True,
        exact_full_physical_angle='G_H=Hadamard diag(Q_H,Q_H^{-*}) Hadamard; complete mean included',
        root_Cauchy_and_source_window=['-2','2'],
        root_source_space='L1(dxi; H_N^(s-1/3)) to original R39 E_N^s, |s|<=2; same valid extension',
        root_height_integer_levels=[0,1,2,3],
        graph_energy_and_source_realization_reused_unchanged=True,
        physical_cut=str(g['physical_cut']),
        exact_both_strong_windows=[['0','4/3'],['-4/3','0']],
        complete_root_derivative_majorants=[record(x) for x in derivatives],
        complete_root_multiplier_bounds=[record(x) for x in M],
        complete_root_height_resolvent_bounds=[record(x) for x in RH],
        complete_root_first_Dyson_remainders={k:record(x) for k,x in rootfirst.items()},
        complete_root_four_thirds_remainders={k:record(x) for k,x in rootR.items()},
        bounds={k:record(x) for k,x in dict(
            root_original_frame_Cauchy_and_inverse=Croot,root_original_frame_ordinary_source=Sroot,
            root_both_four_thirds_remainders=Rroot,
            root_complete_second_and_higher_Dyson=higher,
            exact_full_physical_angle_base=Qp0,exact_full_physical_angle_window_two=Qp2,
            graph_same_model_base=Wg0,graph_same_model_window_two=Wg2,
            strict_same_model_base=Ws0,strict_same_model_window_two=Ws2,
            root_to_physical_cut_base=K0,physical_cut_to_root_base=Ki0,
            root_to_physical_cut_window_two=K2,physical_cut_to_root_window_two=Ki2,
            root_to_physical_cut_full_four_thirds=Rk,
            root_ordinary_source_leg_base=Sr0,graph_ordinary_source_leg_base=Sg0,
            root_ordinary_source_leg_window_two=Sr2,graph_ordinary_source_leg_window_two=Sg2,
            purified_root_cut_same_model_base=model0,purified_root_cut_same_model_window_two=model2,
            full_finite_mean_purification_fee=meanfee,purified_root_cut_full_four_thirds=Rkp,
            unchanged_true_strict_L2_Cauchy=Cstrict,
            unchanged_true_strict_four_thirds_forward=Rp,unchanged_true_strict_four_thirds_opposite=Rm,
            unchanged_reciprocal_true_flux_factor=ik,
            complete_negative_transfer_error_forward=RTp,complete_negative_transfer_error_opposite=RTm,
            complete_actual_strong_scattering_error_both_windows=RS,
            prior_actual_strong_scattering_error=up(wn['complete_scattering_word_error_both_base_windows'])).items()},
        full_negative_near_endpoint_raw_base_columns={k:record(z) for k,z in raw0.items()},
        full_negative_near_endpoint_raw_HN1_columns={k:record(z) for k,z in raw1.items()},
        full_negative_original_affine_base_columns={k:record(z) for k,z in s0.items()},
        complete_base_physical_source_units=dict(
            strict_core='L1(dr; H_N^(-1/2)) of the original physical scalar, x=4theta',
            either_canonical_root='L1(dxi; H_N^(-1/3)) of the exact canonical scalar on the same permitted extension',
            either_tilted_graph='L1(dt; H_N^(-1/2)) of f_t=(L-chi)*f_c/q on that same extension'),
        complete_stronger_physical_source_units=hs['source_units'],
        source_partition=hs['full_negative_source_partition'],
        exact_source_reflection=hs['source_reflection'],
        exact_actual_scattering_is_still_onto_unitary=True,
        original_mean_matrices_both_regular_ports_and_every_head_path_retained=True,
        full_returned_Rstar_recomputed=False,finite_head_inverse_proved=False,
        full_feedback_inverse_proved=False,new_deep_tail_profile_transfer_proved=False,
        gates=gates,dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_root_fourier_fit.py',
            'fourfold_negative_collar_root_fourier_budget.py','fourfold_negative_canonical_cancellation_chart.py',
            'fourfold_negative_root_full_Airy_operator.py','fourfold_actual_return_symmetric_density_normal_form.py',
            'fourfold_negative_root_physical_graph_operator.py')},
        seconds=time.monotonic()-tick)
    save(a.out,out)
    print(dict(complete=True,root=Croot.str(12),K=K2.str(12),Ki=Ki2.str(12),
        Rk=Rk.str(12),RS=RS.str(12),out=str(a.out),sha256=sha(a.out)),flush=True)


if __name__=='__main__':main()

