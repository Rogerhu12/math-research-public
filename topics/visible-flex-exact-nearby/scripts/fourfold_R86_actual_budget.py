#!/usr/bin/env python3
"""Bind R86 to completed actual inputs; keep full-leg forecasts conditional.

The actual conclusions are a finite completed g0 prefix and the local flow
jet of segment 419 starting with the identity.  Forecasts do not certify
the uncomputed part of the forward leg or any R31 hypothesis.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import json
from pathlib import Path

from flint import arb,ctx
from fourfold_spatial_derivative_defect_budget import (
    sha,read,exact,upper,record,certify,spatial_ordered_tails,density_spatial_budget)
from fourfold_circle_preconjugacy_width_budget import gate


def serialize(value):
    if isinstance(value,arb):return record(value)
    if isinstance(value,dict):return {k:serialize(v) for k,v in value.items()}
    if isinstance(value,(tuple,list)):return [serialize(v) for v in value]
    return value


def reference_identity(data):
    return data['identity']['reference']


def same_family(a,b):
    keys=('retarget_descriptor_sha256','leg','target_exact_delta_fraction',
          'target_object_sha256','target_root_sha256','branch_sign')
    if any(a[k]!=b[k] for k in keys):
        raise ValueError('actual input families or branch conventions differ')


def old_parameter_tail(A,B1,B2,R):
    q=2*A/R
    if not q<1:raise ValueError('old R82 smallness condition fails')
    e=arb(1).exp()
    return (4*e*(A*A*B2+(2*e-1)*A*B1*B1)/(R*R*(1-q))).upper()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--prefix-stop',type=int,default=12,
                   help='fixed completed prefix [0,stop), not a live-index count')
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--bits',type=int,default=192)
    args=p.parse_args();ctx.prec=args.bits
    if args.prefix_stop<1:raise ValueError('empty completed prefix')
    base=Path('data/phase_ring_continuation')
    d=Fraction(7,2048);sigma=Fraction(3,1024);S=Fraction(1,256)
    p0=base/'step5_forward_density_pipeline_pilot0/forward_0000_ef134f2a18.json.gz'
    p419=base/'step5_forward_density_pipeline_pilot419_Q1024/forward_0419_ef134f2a18.json.gz'
    spatial_path=base/'type_fixed_step02_d5_step5_parameter_spatial_norms419.json.gz'
    local_path=base/'type_fixed_step02_d5_step5_parameter_local_integrals419.json.gz'
    parameter_spatial=read(spatial_path);local=read(local_path)
    parameter_path=Path(parameter_spatial['parameter_report_path'])
    parameter=read(parameter_path);g0=read(p419)
    if (not parameter_spatial.get('complete') or not local.get('complete')
        or not parameter.get('complete_continuous_signed_parameter_densities_proved')
        or sha(parameter_path)!=parameter_spatial['parameter_report_sha256']
        or local['parameter_report_sha256']!=sha(parameter_path)
        or local['g0_report_sha256']!=sha(p419)
        or parameter['reference_certificate_sha256']!=sha(p419)):
        raise ValueError('completed parameter/source integral identities do not match')
    if any(reference_identity(doc)!=reference_identity(g0)
           for doc in (parameter_spatial,local,parameter)):
        raise ValueError('different actual reference segments were mixed')
    if not parameter_spatial['no_center_to_uniform_parameter_transfer']:
        raise ValueError('central parameter scope must remain explicit')
    g0spatial=density_spatial_budget(p419,d,exact_rectangle=True)
    A=list(map(upper,g0spatial['common_true_and_finite_integrated_derivative_bounds']))
    E0=list(map(upper,g0spatial['integrated_continuous_derivative_errors']))[:2]
    orders={int(row['actual_parameter_order']):row for row in parameter_spatial['orders']}
    for j in (1,2):
        row=orders[j]
        if (not row.get('proved') or Fraction(row['source_error_strip'])!=S
            or Fraction(row['finite_spatial_norm_strip'])!=d
            or not row['normalized_label_frequencies_k']
            or not row['physical_angle_factor_four_not_used']
            or row['whole_real_parameter_tube']):
            raise ValueError('parameter spatial norm contract differs')
    B,C=[list(map(upper,orders[j]['true_integrated_spatial_derivative_SUP_moduli'])) for j in (1,2)]
    errors=[E0]+[list(map(upper,orders[j]['actual_error_derivative_fees']))[:2] for j in (1,2)]
    finite=list(map(upper,local['remaining_local_J0_J1_J2_fees']))
    point=certify(A,B,C,errors,trajectory_strip_gap=exact(d-sigma),finite_output_fees=finite)
    R=exact(S-sigma)
    oldB0,oldC0=[upper(row['central_true_integrated_modulus']) for row in parameter['density']]
    oldA=upper(g0['R72_inputs']['common_integrated_majorant_A'])
    oldT2=old_parameter_tail(oldA,oldB0,oldC0,R)
    point_record=dict(actual_central_parameter_only=True,whole_forward_leg=False,
        initial_state='identity local flow at the left endpoint of segment 419',
        exact_reference_identity=reference_identity(g0),input_strip=str(S),
        derivative_strip=str(d),output_sup_strip=str(sigma),
        A=A,B=B,C=C,source_error_integrals=errors,
        finite_output_definition='three first integrals; retain 2 B(g1,g1) in parameter order two; pay other local terms',
        finite_integral_coefficients_path=str(local_path),finite_integral_coefficients_sha256=sha(local_path),
        budgets=point,old_R82_true_parameter_second_tail=oldT2,
        old_over_R86_second_tail=(oldT2/point['tails'][2]).upper())
    prefix=[];total=[arb(0)]*3;total_errors=[arb(0)]*3
    prefix_R72=[arb(0)]*3
    for i in range(args.prefix_stop):
        path=p0 if i==0 else base/f'step5_forward_density_complete/forward_{i:04d}_ef134f2a18.json.gz'
        raw=read(path)
        same_family(reference_identity(raw),reference_identity(g0))
        if (reference_identity(raw)['segment']!=i
            or reference_identity(raw)['normalized_subspan']!=['0','1']):
            raise ValueError('completed prefix is not one whole leaf per segment')
        budget=density_spatial_budget(path,d,exact_rectangle='density_exact_rectangle' in raw)
        for j in range(3):
            total[j]+=upper(budget['common_true_and_finite_integrated_derivative_bounds'][j])
            total_errors[j]+=upper(budget['integrated_continuous_derivative_errors'][j])
        keys=('common_integrated_majorant_A','integrated_approximation_error_E',
              'omitted_local_second_integral_bound_on_inner_strip')
        for j,key in enumerate(keys):prefix_R72[j]+=upper(raw['R72_inputs'][key])
        prefix.append(budget)
    total=[v.upper() for v in total];prefix_R72=[v.upper() for v in prefix_R72]
    # This number bounds only the flow-certificate contribution, assuming
    # completed full-leg inputs of the displayed hypothetical magnitudes.
    hardy=(1+4/(2*exact(Fraction(1,2048))).expm1()).sqrt()
    transfer=(2*arb('3.520011')/(1-arb('.057575')/2)*hardy*(1+4*arb('.346732178'))).upper()
    scenarios=[]
    mean=[v*550/args.prefix_stop for v in prefix_R72]
    diagnostic=[upper(g0['R72_inputs'][k])*550 for k in (
        'common_integrated_majorant_A','integrated_approximation_error_E',
        'omitted_local_second_integral_bound_on_inner_strip')]
    for label,(aa,ee,jj) in [('repeat_prefix_average',mean),('repeat_segment419',diagnostic)]:
        tail=(aa**3/(2*(R-aa)**2)).upper()
        flow=(ee*(1+aa/R)+jj+tail).upper()
        scenarios.append(dict(unproved_remaining_leaf_assumption=label,
            assumed_full_A=aa,assumed_full_E=ee,assumed_full_omitted_local_J=jj,
            R72_state_tail=tail,conditional_coordinate_error=flow,
            conditional_flow_part_of_preconjugacy_error=(transfer*flow).upper(),
            actual_finite_endpoint_residual_not_included=True))
    repeatedABC=[[550*v for v in row] for row in (A,B,C)]
    repeated=spatial_ordered_tails(*repeatedABC)
    old_repeat=old_parameter_tail(550*oldA,550*oldB0,550*oldC0,R)
    proxy_path=Path('notes/2026-11-12-D5-exact-affine-step3-preconjugacy-cost.json')
    proxy=read(proxy_path);gates=[]
    for row in proxy['prospective_gate_scenarios']:
        out=gate(row['preconjugated'],Fraction(1,4096))
        gates.append(dict(T_multiplier=row['assumed_T_multiplier_of_selected_ray_maximum'],
            exact_conditional_epsilon=str(out['epsilon']),display=float(out['epsilon'])))
    result=dict(kind='R86_actual_local_flow_and_completed_prefix_with_separate_layout_forecast',
        complete=True,source_sha256=sha(__file__),helper_sha256=sha(Path(__file__).with_name('fourfold_spatial_derivative_defect_budget.py')),
        actual_single_leaf=point_record,
        completed_g0_prefix=dict(segments=args.prefix_stop,whole_forward_leg=False,
            derivative_strip=str(d),common_integrated_derivatives=total,
            integrated_source_derivative_errors=total_errors,R72_A_E_localJ=prefix_R72,
            all_prefix_rows=prefix),
        not_a_full_leg_certificate=True,
        layout_only=dict(state_scenarios=scenarios,endpoint_flow_transfer_factor=transfer,
            repeated419_parameter_derivative_inputs=repeatedABC,
            repeated419_R86_parameter_tails=repeated['tails'],
            repeated419_old_R82_second_parameter_tail=old_repeat,
            old_delta3_unproved_R31_proxy_gates=gates,proxy_report_sha256=sha(proxy_path),
            cautions=['Uncomputed leaves have not been bounded by either forecast.',
              'The old delta3 P,Q,T,twist proxies do not certify delta5.',
              'The finite endpoint residual and actual parameter-box R31 bounds remain separate inputs.',
              'The endpoint cubic Taylor remainder and chosen-coefficient fees are not included in the displayed flow contribution.',
              'The completed local parameter sources are central only.']),
        inputs=[dict(path=str(pth),sha256=sha(pth)) for pth in (p419,spatial_path,local_path,parameter_path)])
    args.out.write_text(json.dumps(serialize(result),indent=2)+'\n')
    print(json.dumps(dict(point_tails=[float(z) for z in point['tails']],
        point_total=[float(z) for z in point['total_errors']],
        point_tail_improvement=float(oldT2/point['tails'][2]),prefix_segments=args.prefix_stop,
        prefix_spatial=[float(z) for z in total],
        forecast_R86_T2=float(repeated['tails'][2]),forecast_old_T2=float(old_repeat),
        report_sha256=sha(args.out))),flush=True)


if __name__=='__main__':main()
