#!/usr/bin/env python3
"""Join complete actual center/whole-box chronological data to R31.

A partial prefix is rejected before any return/KAM computation.  The input
uniform accumulator may use the proved center-g1/uniform-g2 hybrid, but its
reported bounds and finite C,D must describe that same choice.  This runner
keeps every finite endpoint product frequency and pays true sup/Hardy fees.
The frozen hybrid schema retains center 2J11 and explicitly excludes uniform
2J11; both flags and its proved real-parameter transfer are required.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from pathlib import Path
import time
import traceback

from flint import arb,acb,ctx
from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_saved_circle_field_multidomain_budget import read,upper
from fourfold_phase_field_time_turn_collar import PiTime
from fourfold_phase_unified_scalar_time_circle import exact_time
from fourfold_retarget_reference_segment_package import load_package
from fourfold_half_return_predictor import endpoint
from fourfold_forward_endpoint_bound_v3 import add,norm,product
from fourfold_forward_density_pipeline_Q1024_v3 import decode_ball,encode_ball,save
from fourfold_parameter_endpoint_kam import (
    load_H,finite_H_constants,half_return_data,hardy,r31_gates,
)
from fourfold_parameter_endpoint_spatial_v2 import endpoint_three_orders_spatial
from fourfold_parameter_sharp_spatial import sharp_half_spatial_bounds,square_sharp_half_bounds


def records(value):
    if isinstance(value,arb):return ball_record(value)
    if isinstance(value,acb):return encode_ball(value)
    if isinstance(value,dict):return {k:records(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)):return [records(v) for v in value]
    return value


def local_terms_contract(report,scope):
    if report.get('every_local_retained_2J11_included') is True:
        return True
    if scope!='uniform' or report.get('kind')!='actual_hybrid_parameter_chronological_prefix':
        return False
    transfer=report.get('real_parameter_transfer',{})
    return (report.get('every_center_local_2J11_retained') is True
            and report.get('uniform_local_2J11_not_used') is True
            and transfer.get('proved') is True and transfer.get('orders')==[0,1,2])


def load_chronological(path,descriptor_sha,delta,scope):
    report=read(path);identity=report['identity']
    if (not report.get('proved') or not report.get('complete')
        or not report.get('whole_forward_leg') or report.get('completed_segments')!=550
        or identity['retarget_descriptor_sha256']!=descriptor_sha
        or Fraction(identity['target_exact_delta_fraction'])!=delta
        or not identity.get('fixed_reference_independent_of_parameter')
        or not report.get('all_cross_segment_g1_g1_and_g0_g2_terms_retained')
        or not local_terms_contract(report,scope)):
        raise ValueError('complete same-object actual '+scope+' chronological data required')
    initial=PiTime(Fraction(0),Fraction(-1,2));final=PiTime(Fraction(0),Fraction(1,2))
    if (exact_time(identity['exact_begin'])!=initial or exact_time(identity['exact_end'])!=final):
        raise ValueError('chronological data do not span the exact whole forward interval')
    eta=Fraction(identity['exact_parameter_half_width'])
    if ((scope=='center' and eta!=0) or (scope=='uniform' and
        (eta<=0 or not identity.get('whole_real_parameter_tube')))):
        raise ValueError('center/whole-parameter scope differs')
    if list(map(Fraction,identity['exact_parameter_interval']))!=[delta-eta,delta+eta]:
        raise ValueError('the exact real parameter box differs from its stated center')
    candidates=list(Path(__file__).parent.glob('fourfold_parameter*accumulat*.py'))
    if report['source_sha256'] not in {sha(p) for p in candidates}:
        raise ValueError('chronological source is absent or has changed')
    for name,digest in report['dependency_sha256'].items():
        if sha(Path(__file__).with_name(name))!=digest:
            raise ValueError('chronological dependency changed: '+name)
    link=report['coefficients'];coefficient_path=Path(link['path'])
    if sha(coefficient_path)!=link['sha256']:
        raise ValueError('complete chronological coefficients changed')
    coefficients=read(coefficient_path)
    if coefficients.get('identity')!=identity:
        raise ValueError('chronological coefficients and their bounds have different identities')
    C=[[decode_ball(z) for z in row] for row in coefficients['C']]
    D=[[decode_ball(z) for z in row] for row in coefficients['D']]
    if len(C)!=3 or len(D)!=3 or any(not row for row in C+D):
        raise ValueError('all six complete chronological Fourier rows are required')
    W=[add((1,c),(1,d)) for c,d in zip(C,D)]
    majorants=[[upper(v) for v in row] for row in
               report['spatial_integrated_common_source_sup_moduli_by_parameter_order']]
    errors=[[upper(v) for v in row[:2]] for row in
            report['spatial_integrated_source_approximation_sup_errors_by_parameter_order']]
    fees=[upper(v) for v in report['omitted_local_integral_fees_A_inner']]
    return report,W,majorants,errors,fees


def main():
    p=argparse.ArgumentParser(description=__doc__)
    base=Path('data/phase_ring_continuation')
    p.add_argument('--package',type=Path,default=base/'step5_forward549_exact_reference_package.npz.gz')
    p.add_argument('--H',type=Path,default=base/'type_fixed_step02_d5_exact_affine_step5_dyadic_H.json')
    p.add_argument('--center',type=Path,required=True)
    p.add_argument('--uniform',type=Path,required=True)
    p.add_argument('--half-outer-width',default='5/2048')
    p.add_argument('--half-derivative-width',default='9/4096')
    p.add_argument('--full-width',default='1/512')
    p.add_argument('--kam-start-width',default='3/2048')
    p.add_argument('--kam-width-step',default='1/4096')
    p.add_argument('--inverse-radius',default='1/1000')
    p.add_argument('--bits',type=int,default=320)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();ctx.prec=args.bits;ctx.cap=24;started=time.monotonic()
    report=dict(kind='actual_complete_parameter_endpoint_and_full_return_KAM',
        source_sha256=sha(__file__),actual_R31_accepted=False,
        complete_true_center_return=False,complete_true_uniform_parameter_box=False,
        bits=args.bits,stage='checking_complete_input',
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_parameter_endpoint_spatial_v2.py','fourfold_parameter_endpoint_kam.py',
            'fourfold_parameter_sharp_spatial.py','fourfold_forward_endpoint_bound_v3.py',
            'fourfold_half_return_predictor.py','fourfold_retarget_reference_segment_package.py',
            'fourfold_spatial_derivative_defect_budget.py','fourfold_parameter_ordered_defect.py')})
    try:
        package=load_package(args.package)
        descriptor=package['documents']['descriptor']['document']
        descriptor_sha=package['documents']['descriptor']['sha256']
        # The exact target parameter is part of the selected retarget descriptor.
        delta=Fraction(descriptor['target_exact_delta_fraction'])
        center,Wc,Mc,Ec,Jc=load_chronological(args.center,descriptor_sha,delta,'center')
        uniform,Wu,Mu,Eu,Ju=load_chronological(args.uniform,descriptor_sha,delta,'uniform')
        ci,ui=center['identity'],uniform['identity']
        for key in ('label_strip','inner_strip','spatial_strip'):
            if Fraction(ci[key])!=Fraction(ui[key]):
                raise ValueError('center and uniform spatial strips differ')
        sigma,sd=map(lambda key:exact_arb(Fraction(ci[key])),('inner_strip','spatial_strip'))
        a,b,S,s0,step,r=map(lambda v:exact_arb(Fraction(v)),
                          (args.half_outer_width,args.half_derivative_width,args.full_width,
                           args.kam_start_width,args.kam_width_step,args.inverse_radius))
        if not 0<S<b<a<sigma<sd:
            raise ValueError('strict actual endpoint and return strip nesting required')
        eta=exact_arb(Fraction(ui['exact_parameter_half_width']))
        Hdoc,h,q=load_H(args.H)
        if sha(args.H)!=package['documents']['target_H']['sha256']:
            raise ValueError('the endpoint package fixes a different exact H')
        U=endpoint(package);d=arb.pi()*(15121+arb(5).sqrt())/27422
        constants=finite_H_constants(h,q,a,r)
        report.update(stage='complete_endpoint_composition',descriptor_sha256=descriptor_sha,
            exact_delta_fraction=str(delta),exact_parameter_half_width=ui['exact_parameter_half_width'],
            package_path=str(args.package),package_sha256=sha(args.package),H_sha256=sha(args.H),
            center_input=dict(path=str(args.center),sha256=sha(args.center)),
            uniform_input=dict(path=str(args.uniform),sha256=sha(args.uniform)),
            widths=dict(flow=str(Fraction(ci['inner_strip'])),spatial=str(Fraction(ci['spatial_strip'])),
                        half_outer=args.half_outer_width,half_derivative=args.half_derivative_width,
                        full=args.full_width,kam_start=args.kam_start_width,kam_step=args.kam_width_step))
        epc=endpoint_three_orders_spatial(U,Wc,Mc,Ec,Jc,sd,sigma)
        epu=endpoint_three_orders_spatial(U,Wu,Mu,Eu,Ju,sd,sigma)
        Hfactor=hardy(sigma-a)
        Pg=(norm(epu['periodic_rows'][1],a)+Hfactor*epu['sup_errors'][1]).upper()
        Tg=(norm(epu['periodic_rows'][2],a)+Hfactor*epu['sup_errors'][2]).upper()
        half=half_return_data(epc,h,q,constants,d,a,sigma)
        # The twist is a real-circle mean.  It need not pay the narrower
        # Hardy loss required for complex-strip P/Q norms.
        real_constants=finite_H_constants(h,q,arb(0),r)
        half_real=half_return_data(epc,h,q,real_constants,d,arb(0),sigma)
        half_twist=max(half['half_twist_lower'],half_real['half_twist_lower'])
        # Before deriving any full-box inverse derivative bound, prove inverse
        # existence uniformly by the real parameter MVT at the endpoint.
        Ebox=(half['center_endpoint_error']+eta*Pg).upper()
        if not constants['inverse_Hprime']*Ebox<=constants['radius']/2:
            raise ValueError('the full real box fails the R63 inverse gate')
        P=(constants['perturbed_inverse']*Pg).upper()
        T=(constants['perturbed_inverse']*(Tg+constants['Hsecond']*P*P)).upper()
        shifted_q=[z*(acb(0,k)*d).exp() for k,z in enumerate(q)]
        L=product(epc['periodic_rows'][1],shifted_q)
        Pcenter=(norm(L,a)+half['complete_half_twist_error']).upper()
        tightening=[]
        for iteration in range(8):
            P=min(P,(Pcenter+eta*T).upper())
            T=min(T,(constants['perturbed_inverse']*(Tg+constants['Hsecond']*P*P)).upper())
            tightening.append(dict(P=P,T=T))
        Ubox=min((constants['inverse_displacement_factor']*Ebox).upper(),
                 (half['center_half_error']+eta*P).upper())
        if not Ubox>=half['center_half_error']:
            # This is only normalization of two independently valid upper
            # bounds, ensuring the declared uniform envelope includes its
            # recorded center envelope as required by the next API.
            Ubox=half['center_half_error']
        sharp=sharp_half_spatial_bounds(epc['periodic_rows'][1],q,d,half['complete_half_twist_error'],
            center_u=half['center_half_error'],uniform_u=Ubox,uniform_T=T,
            parameter_radius=eta,outer_width=a,inner_width=b)
        if not half_twist>0:
            raise ValueError('the complete true half-return signed twist is not separated')
        squared=square_sharp_half_bounds(sharp,full_width=S,half_twist_lower=half_twist)
        if not squared['twist_lower']>0:
            raise ValueError('the full square loses the actual signed twist')
        gates=r31_gates(**{key:squared[key] for key in ('epsilon','P','Q','T','B','twist_lower')},
            K=arb(3)/2,s0=s0,delta0=step,S=S,parameter_radius=eta)
        polynomial_path=args.out.with_name(args.out.stem.replace('.json','')+'_finite_endpoints.json.gz')
        save(polynomial_path,dict(kind='complete_center_and_uniform_finite_endpoint_rows',
            descriptor_sha256=descriptor_sha,H_sha256=sha(args.H),
            center_rows=[[encode_ball(z) for z in row] for row in epc['periodic_rows']],
            uniform_rows=[[encode_ball(z) for z in row] for row in epu['periodic_rows']],
            all_product_frequencies_retained=True))
        epc.pop('periodic_rows');epu.pop('periodic_rows');sharp.pop('finite_Cp_row')
        report.update(stage='complete',complete_true_center_return=True,
            complete_true_uniform_parameter_box=True,finite_H_constants=records(constants),
            center_endpoint=records(epc),uniform_endpoint=records(epu),half=records(half),
            half_real_mean=records(half_real),real_inverse_constants=records(real_constants),
            accepted_half_twist_lower=ball_record(half_twist),
            uniform_inverse_gate=dict(passed=True,endpoint_error=ball_record(Ebox)),
            uniform_first_and_second_endpoint_bounds=records([Pg,Tg]),
            true_uniform_parameter_tightening=records(tightening),
            sharp_half=records(sharp),full_square=records(squared),R31=records(gates),
            actual_R31_accepted=bool(gates['arithmetic_gates_passed']),
            finite_endpoint_coefficients=dict(path=str(polynomial_path),sha256=sha(polynomial_path)),
            scope='Actual whole forward flow and full real parameter box; R77 square and R31. No full PDE/nonlinear inverse inferred.')
    except Exception as exc:
        report.update(failure=type(exc).__name__+': '+str(exc),traceback=traceback.format_exc())
    report['wall_seconds']=time.monotonic()-started;save(args.out,report)
    print({k:report.get(k) for k in ('stage','actual_R31_accepted','failure','wall_seconds')},flush=True)
    if report['actual_R31_accepted']:return 0
    return 2

if __name__=='__main__':raise SystemExit(main())
