#!/usr/bin/env python3
"""Complete actual positive-cap source windows through angular order 4/3.

Uses the full old cap realization, the exact incoming Poisson adjoint,
and the already complete Airy trial residual. No global angular
coefficient differentiation or new native geometry is substituted.
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
def lo(v):return stored(v).lower()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--cap',type=Path,default=Path('notes/2026-11-13-exact-positive-cap-Airy-contact-v2.json'))
    p.add_argument('--bits',type=int,default=320)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise ValueError('a fresh actual full-cap output is required')
    ctx.prec=a.bits;tick=time.monotonic()
    cap=checked(a.cap,'fourfold_actual_exact_positive_cap_Airy_contact.py')
    if (not cap['full_augmented_regular_and_root_mean_retained']
        or not cap['actual_full_uncompressed_cap_and_nonzero_infinite_tail_fee_retained']
        or not cap['positive_negative_frequency_crossings_and_all_output_modes_retained']
        or not cap['true_root_height_shear_and_Piola_density_retained']):
        raise ValueError('the whole actual source and cap realization are required')
    aa=cap['complete_Airy_source'];ff=cap['complete_original_frame']
    Cs=up(cap['all_root_and_regular_contact']['full_ordinary_contact'])
    Cw=up(cap['all_root_and_regular_contact']['full_weak_contact'])
    H=exact_arb(Fraction(cap['actual_canonical_positive_height']))
    d=lo(cap['complete_height_gradient']['height_absorption'])
    c=up(aa['c']);cl=lo(aa['c']);cA=up(aa['c_A']);cAl=lo(aa['c_A'])
    Ai=up(aa['Ai_zero']);Aip=up(aa['minus_Aiprime_zero'])
    rq=up(aa['physical_frequency_ratio']);F=up(aa['full_trial_residual_times_L_four_thirds'])
    qlo=lo(cap['actual_quarter_circle_frequency'][0])
    qhi=up(cap['actual_quarter_circle_frequency'][1])
    chi1=up(aa['cutoff_first_derivative'])
    contact=up(ff['all_slots_contact_to_one_wave'])
    E=up(ff['right_and_left_full_four_thirds_remainder'])
    if not (d>0 and qlo>1 and up(ff['exact_full_unitary_norm'])==1):
        raise ValueError('the exact full unitary frame and height absorption are required')
    gates=[]
    def gate(name,ok):
        gates.append(dict(name=name,passed=bool(ok)))
        if not ok:raise ValueError(name)
    gate('complete nonzero height column is below the genuine root mean column',
         2*c*Ai*rq.sqrt()<cl)
    gate('complete regular height column is below the genuine root mean column',
         1/(arb.pi()*cAl).sqrt()<cl)
    P0=(2*c*Cs).upper();Pw0=(2*c*Cw).upper()
    CD=((4+H*H).sqrt()/d).upper()
    GD=(CD*CD).upper();GDw=(CD/d).upper()
    Z=(GD+P0*contact*Cs).upper()
    Zw=(GDw+Pw0*contact*Cs).upper()
    trial=(2*c*Aip*rq).upper()
    trialw=(2*c*((Ai*Aip).sqrt()+chi1*Aip/qlo**(arb(2)/3))).upper()
    Ptop=((trial+Z*F)**2+P0*P0).sqrt().upper()
    Pwtop=((trialw+Zw*F)**2+Pw0*Pw0).sqrt().upper()
    green=(arb.pi()*cA/2).upper()
    top=(green*(Ptop+E*P0)).upper()
    topw=(green*(Pwtop+E*Pw0)).upper()
    base=up(ff['complete_local_ordinary_source_to_affine_outgoing'])
    basew=up(ff['complete_local_weak_source_to_affine_outgoing'])
    elllo=(2*arb.pi()/qhi).lower();ellhi=(2*arb.pi()/qlo).upper()
    renorm=(1/elllo.sqrt()).upper()
    rows=[]
    for s in (Fraction(0),Fraction(1,2),Fraction(1),Fraction(4,3)):
        t=exact_arb(3*s/4)
        ordinary=(base**(1-t)*top**t).upper()
        weak=(basew**(1-t)*topw**t).upper()
        rows.append(dict(order=str(s),ordinary_source_angular_order=str(s-Fraction(2,3)),
            weak_source_angular_order=str(s),
            physical_full_augmented_outgoing_ordinary=record(ordinary),
            physical_full_augmented_outgoing_weak=record(weak),
            averaged_root_and_regular_outgoing_ordinary=record((renorm*ordinary).upper()),
            averaged_root_and_regular_outgoing_weak=record((renorm*weak).upper())))
    out=dict(kind='actual_full_old_cap_complete_stronger_local_source_windows',
        complete=True,proved=True,source_sha256=sha(__file__),bits=a.bits,
        identity=cap['identity'],whole_cap_parameter_interval=cap['whole_cap_parameter_interval'],
        inputs={str(a.cap):sha(a.cap)},native_geometry_recomputed=0,
        exact_positive_operator=cap['exact_operator'],canonical_collar_height=str(Fraction(cap['actual_canonical_positive_height'])),
        old_full_Robin_realization_and_independent_regular_constraint_retained=True,
        source_support='the same exact canonical collar 0<=y<=H; solution remains on the full original cap',
        ordinary_source='L2(dy;H_phi^(s-2/3)) canonical ordinary density f, unchanged physical dy dphi pairing',
        weak_source='(F_y,F_phi/sqrt(y)) in L2(dy;H_phi^s)^2 with the original canonical weak load convention',
        root_output='H_phi^s plus the independent balanced regular scalar, 0<=s<=4/3',
        genuine_source_operator_unchanged=True,
        exact_physical_source_conversion=cap['exact_grounded_source'],
        full_root_mean_and_regular_mean_charge_retained=True,
        zero_trace_Dirichlet_Green_uses_both_trace_constraints=True,
        exact_incoming_Poisson_identity='P Pi_nonzero=U_trial-Z F_trial; P Pi_rootmean_regular kept as a full finite-input/infinite-output column',
        exact_Green_pairing='R_cap^* h_(f,F) is a fixed unit-modulus sign times (pi*c_A/2) P^* applied to the full ordinary/weak load',
        high_output_smoothing_used_after_base_input='h=constant*(-g+(R_cap+I)g); the smoothing correction uses only the base bound for g',
        bounds={k:record(v) for k,v in dict(
            complete_Cs=Cs,complete_Cw=Cw,complete_height_absorption=d,
            homogeneous_incoming_Poisson_to_local_Htwo_thirds=P0,
            homogeneous_incoming_Poisson_to_local_energy_gradient=Pw0,
            zero_double_trace_source_to_sqrt_energy=CD,
            zero_double_trace_source_to_local_Htwo_thirds=GD,
            zero_double_trace_source_to_local_gradient=GDw,
            zero_incoming_ordinary_Green_to_local_Htwo_thirds=Z,
            zero_incoming_ordinary_Green_to_local_gradient=Zw,
            full_trial_Hminus_four_thirds_to_local_Hminus_two_thirds=trial,
            full_trial_gradient_Hminus_four_thirds_to_same_weight_gradient=trialw,
            incoming_Poisson_Hminus_four_thirds_to_local_Hminus_two_thirds=Ptop,
            incoming_Poisson_Hminus_four_thirds_to_local_Hminus_four_thirds_gradient=Pwtop,
            exact_Green_pairing_factor_modulus=green,
            original_complete_cap_R_four_thirds=E,
            complete_ordinary_top_Hfour_thirds_source=top,
            complete_weak_top_Hfour_thirds_source=topw,
            actual_root_period_lower=elllo,actual_root_period_upper=ellhi,
            common_physical_to_averaged_root_regular_factor=renorm).items()},
        rows=rows,gates=gates,interpolation_interval=['0','4/3'],
        separate_bare_boundary_load_not_bounded_by_a_bulk_vector_norm=True,
        higher_than_four_thirds_source_window_proved=False,
        fixed_positive_angular_weight_proved=False,new_deep_tail_profile_transfer_proved=False,
        full_feedback_inverse_proved=False,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_beta_bulk_interval.py','fourfold_phase_root_fourier_fit.py',
            'fourfold_negative_collar_root_fourier_budget.py','fourfold_negative_canonical_cancellation_chart.py')},
        seconds=time.monotonic()-tick)
    save(a.out,out)
    print(dict(complete=True,source_top=top.str(12),weak_top=topw.str(12),
        source_one=rows[2]['physical_full_augmented_outgoing_ordinary']['upper'],
        weak_one=rows[2]['physical_full_augmented_outgoing_weak']['upper'],
        out=str(a.out),sha256=sha(a.out)),flush=True)


if __name__=='__main__':main()
