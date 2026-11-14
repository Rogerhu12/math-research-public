#!/usr/bin/env python3
"""Pay both actual-conjugacy-defect corrections to the true R31 twist.

The hypotheses on E and E_phi are explicit.  The final full transport
certificate has not been silently supplied by a fitted residual.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_codazzi_phase_scalar_cache_jets import read
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record,save,sha

INPUT='67d3dcbfa415173db552286cabac03f4c9daba521fff3b68d4af9d28eed478da'


def b(x):return box_from_record(x)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--input',type=Path,default=Path('notes/2026-11-14-R133-complete-correlated-first-phase-parameter-native.json.gz'))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=320
    if args.out.exists():raise FileExistsError('preserve each actual twist budget')
    if sha(args.input)!=INPUT:raise ValueError('the complete correlated actual parameter field changed')
    d=read(args.input)
    if not d['complete'] or not d['positive_twist_if_conjugacy_defect_zero']:
        raise ValueError('the complete same-family positive first functional is required')
    eps0=exact_arb(Fraction(1,1000000));eps1=exact_arb(Fraction(1,10000))
    H1=b(d['exact_H_derivative_minus_one_A0']).upper();H2=b(d['exact_H_second_derivative_A0']).upper()
    eA=b(d['true_label_derivative_minus_one_Linfty']).upper()
    L=b(d['proved_real_one_leg_drift_Lipschitz_integral']).upper()
    DA=b(d['complete_d_first_Astrip_integrals']['0'][0]).upper()
    D2=b(d['complete_d_first_L2_integral']).upper();CA=b(d['complete_absolute_c_first_integral']).upper()
    Hmax=(1+H1).upper();Hmin=(1-H1).lower();eta=(eps1/Hmin).upper()
    P1=(2*(2*L).exp()*(DA+CA)).upper()
    transport_error=((1+eA)**2*eta/(1-eta)*2*(D2+CA)).upper()
    coordinate_error=(eps0*H2*Hmax*P1/Hmin).upper()
    twist=(b(d['complete_zero_conjugacy_defect_twist_enclosure']).lower()-transport_error-coordinate_error).lower()
    target=exact_arb(Fraction(1,600))
    tests=[
        ('the exact initial H is a real orientation preserving diffeomorphism',Hmin>0),
        ('the genuine endpoint Jacobian defect denominator is positive',eta<1),
        ('both complete two-leg parameter source contributions are retained',D2>=0 and CA>=0),
        ('the actual mean-preserving two-ray weighting correction is finite',transport_error.is_finite()),
        ('the true R31 output coordinate correction is paid',coordinate_error.is_finite()),
        ('the physical parameter twist remains above1/600 under the stated true E gates',twist>target),
        ('the normalized2pi-circle parameter twist remains above1/150',4*twist>4*target),
    ]
    out=dict(kind='actual_first_phase_parameter_transversality_with_explicit_defect_gates',
        complete=all(bool(ok) for _,ok in tests),source_sha256=sha(__file__),input_sha256=INPUT,
        explicit_direction_definition_sha256=d['explicit_direction_definition_sha256'],
        actual_affine_parameter='eta_0',exact_affine_offset='0',whole_original_eta=False,
        exact_physical_phase_defect_upper='1/1000000',exact_physical_phase_derivative_defect_upper='1/10000',
        genuine_return_parameter_derivative_sup=record(P1),
        complete_endpoint_relative_Jacobian_defect=record(eta),
        complete_two_ray_weight_correction=record(transport_error),
        complete_R31_coordinate_correction=record(coordinate_error),
        complete_physical_R31_parameter_twist_lower=record(twist),
        complete_normalized2pi_R31_parameter_twist_lower=record((4*twist).lower()),
        physical_circle_period='pi/2',normalization='x=4*phi; H0_x(x)=4*H_inverse(x/4)',
        actual_final_full_transport_defect_consumed=False,conditional_on_displayed_actual_E_Ephi_gates=True,
        fitted_residual_used_as_interval_value=False,exact_PDE_solution_branch_assumed=False,
        full_R31_smallness_and_parameter_domain_gates_proved=False,
        gates=[dict(name=n,passed=bool(x)) for n,x in tests])
    save(args.out,out)
    print(dict(complete=out['complete'],ray_error=transport_error.str(16),coordinate_error=coordinate_error.str(16),
        physical_twist=twist.str(16),normalized_twist=(4*twist).str(16)),flush=True)
    if not out['complete']:raise RuntimeError('a full actual parameter-twist correction gate failed')


if __name__=='__main__':main()
