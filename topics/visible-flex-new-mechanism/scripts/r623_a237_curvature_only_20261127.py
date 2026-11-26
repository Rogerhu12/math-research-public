#!/usr/bin/env python3
"""Pay only a new complete K for the already-certified exact a237 material.

The complete same-q reference rho/D and global delta/alpha are consumed from
one exact original FINAL. They are not rescanned. The unsaved endpoint field
and exact analytic-height prefix must be reconstructed once for the new K
queries; this necessary work is charged. A complete new K alone may feed the
same-bound R604/R622 scalar consequences. No optimizer/fine/Jac diagnostics.
"""
import argparse
from collections import defaultdict
import hashlib
import json
import math
import os
from pathlib import Path
import struct
import sys
import time
from types import SimpleNamespace

BINDINGS={
    'r582_a237_normal_curvature_reach_20261127.py':
        '577211e39b11d3102cee6154bd209ada0a41a6138bedb7c69a56a67ca6f911ae',
    'r623_finite_vertical_primitive_curvature_20261127.py':
        '43762578fd236233ccb44e8cd38bbfef44863b05b3fce26844bcd2f0febde80d',
    'r622_long_near_reach_from_complete_bounds_20261127.py':
        '3ae74691e4588b0636406941119ccc49542dedecc87b0e12bc4685fac7cdbad8',
}
for filename,expected in BINDINGS.items():
    if hashlib.sha256(Path(__file__).with_name(filename).read_bytes()).hexdigest()!=expected:
        raise RuntimeError('declared curvature-only dependency differs: '+filename)
import r582_a237_normal_curvature_reach_20261127 as prior
from r623_finite_vertical_primitive_curvature_20261127 import (
    same_cell_angular_data,radial_curvature_with_finite_vertical_primitive,
)
from r622_long_near_reach_from_complete_bounds_20261127 import long_near_consequence

backend,I=prior.backend,prior.I
SCHEMA='r623-a237-paid-reference-C0-C1-new-complete-curvature-v1'
Q_SHA='a2377220dacda9eefe63f25a2000441f0169a0db5de9bc23840f90e5037a895e'
MESH_SHA='0d222bd12ce8a61d0c88264c6fb5c82066f0ca058855b5bf7a670a53b483a991'


def emit(tag,value):
    print('R623_CURVATURE_'+tag+' '+json.dumps(value,sort_keys=True,
        separators=(',',':'),allow_nan=False),flush=True)


def original_input(raw):
    source=json.loads(raw)
    expected={'run_id':45895935112,'job_id':140169696746,
        'source_commit':'ac528e756d9e8f601f9a2c2a8623e2f77c212d94',
        'runtime_pull_commit':'ac528e756d9e8f601f9a2c2a8623e2f77c212d94',
        'raw_stdout_bytes':182044,
        'raw_stdout_sha256':'efc8b74fa6db80a635ac36e969c1e4d0c1edb3ead7700bd06c8b2c622a2659f7',
        'FINAL_JSON_bytes':18157,
        'FINAL_JSON_sha256':'fe8bf5e7b9051907a80bfa76799d680fb19128bb45df15e7976cd292a9f4b431',
        'FIELD_JSON_bytes':5672,
        'FIELD_JSON_sha256':'490e5e88dd830a4be058f892d716aacc4575db7a209feb19ab712195f4c5b301'}
    if source.get('schema')!='r623-a237-one-paid-complete-input-new-K-v1' or source['origin']!=expected:
        raise ValueError('one exact original complete geometry input required')
    values={}
    for name in ('FINAL','FIELD'):
        encoded=source['original_'+name+'_JSON'].encode()
        if len(encoded)!=expected[name+'_JSON_bytes'] or hashlib.sha256(encoded).hexdigest()!=expected[name+'_JSON_sha256']:
            raise ValueError('original '+name+' bytes differ')
        values[name]=json.loads(encoded)
    final,field=values['FINAL'],values['FIELD']
    reference=final['new_reference'];nonround=final['nonround_continuous_geometry']
    if (final['schema']!='r582-actual-a237-new-mean-circle-normal-projected-reach-v1'
            or final['failure'] is not None or final['actual_q_binary64_sha256']!=Q_SHA
            or final['material_mesh_binary64_sha256']!=MESH_SHA
            or not reference['complete_new_reference'] or reference['pending_cells']!=0
            or reference['first_unresolved']
            or not nonround['complete_nonround_norm_coverage']
            or nonround['pending_cells']!=0 or nonround['first_unresolved']
            or not nonround['all_theta_enclosed_by_same_core_and_original_complete_mode_fields']
            or not nonround['central_cylinder_same_material_z_core_extension']
            or not nonround['both_complete_Cartesian_caps_included']
            or not nonround['lower_body_is_the_original_orthogonal_reflection']
            or not nonround['R604_consequence']['established']):
        raise ValueError('source is not a complete same-q closed geometry certificate')
    repository=Path(__file__).resolve().parents[3]
    request_path=repository/'topics/visible-flex-new-mechanism/computations/request-r582-a237-normal-curvature-20261127.json'
    request_bytes=request_path.read_bytes()
    if (len(request_bytes)!=18337 or hashlib.sha256(request_bytes).hexdigest()!=
            'a156c7f369a0a64aa2ba60221ea4255c7c583c1f04ccb6122667ac4091110fe2'):
        raise ValueError('actual q/paid seed ancestry request changed')
    previous_source=json.loads(json.loads(request_bytes)['lanes']['actual-a237-normal-curvature']['source_state_json'])
    q=previous_source['actual_retained_q']
    if (len(q)!=97 or prior.identity(q)!=Q_SHA or previous_source['p']!=.181
            or previous_source['material_mesh_sha256']!=MESH_SHA
            or final['same_material_receipt']['actual_q_binary64_sha256']!=Q_SHA
            or field['field_receipt']['material_mesh_binary64_sha256']!=MESH_SHA
            or final['same_material_receipt']['mesh']['material_mesh_binary64_sha256']!=MESH_SHA):
        raise ValueError('current/reference/material identities do not agree')
    bounds=nonround['uniform_bounds']
    inherited={'delta':bounds['C0_upper'],'alpha':bounds['C1_difference_upper'],
        'reference_reach_lower':reference['reach_lower_if_complete'],
        'reference_diameter_upper':reference['diameter_upper_if_complete'],
        'old_curvature_upper':bounds['R621_principal_curvature_upper'],
        'old_whole_surface_reach_lower':nonround['R604_consequence']['whole_surface_reach_lower'],
        'old_whole_surface_reach_over_D_lower':nonround['R604_consequence']['whole_surface_reach_over_D_lower']}
    if (not all(math.isfinite(x) for x in inherited.values())
            or inherited['delta']<0 or not 0<=inherited['alpha']<1
            or min(inherited['reference_reach_lower'],inherited['reference_diameter_upper'])<=0):
        raise ValueError('complete inherited scalar bounds are invalid')
    core={k:I(*v) for k,v in field['core_bounds'].items()}
    if core['rho'].lo<=0 or core['a0'].lo<=0:
        raise ValueError('paid same-core complete angular bounds unavailable')
    return source,previous_source,final,core,inherited


def short_near_consequence(inherited,curvature):
    d,n=I(inherited['delta']),I(inherited['alpha'])
    lam=I((1+n).hi);K=I(curvature)
    rho=I(inherited['reference_reach_lower'])
    lo,hi=0.,.75
    for _ in range(32):
        middle=(lo+hi)/2
        if (2*lam*rho*prior.artanh_upper(I(middle))).hi <= (3/(2*K)).lo:
            lo=middle
        else:
            hi=middle
    threshold=I((2*rho*I(lo)).lo)
    result={'schema':'r623-new-K-same-paid-input-R604-short-near-v1',
        'near_pair_threshold_lower':threshold.lo,'pi_lower_bound_used':3,
        'artanh_positive_terms':64,'scalar_path_enclosure_calls':32,
        'new_curvature_upper':curvature,'same_paid_delta_alpha_reference':True}
    if threshold.lo<=(2*d).hi:
        result.update(established=False,reason='far displacement budget not positive')
        return result
    near=1/K
    far=(threshold-2*d)**2/(threshold**2/rho+2*n*threshold+4*d)
    tau=min(near.lo,far.lo)
    diameter=I(inherited['reference_diameter_upper'])+2*d
    ratio=I(tau)/diameter
    result.update(established=tau>0,near_pair_reach_lower=near.lo,
        far_pair_reach_lower=far.lo,whole_surface_reach_lower=tau,
        whole_surface_diameter_upper=diameter.hi,
        whole_surface_reach_over_D_lower=ratio.lo,
        reach_ratio_point03_met=ratio.lo>=(I(3)/100).hi)
    return result


def certify_curvature(design,mean,core,inherited,args,clock,started):
    suffix=design.hermite.exact_zero_suffix
    zero_start=None if suffix is None else max(suffix,backend.BACKGROUND_END)
    partition=list(design.initial_partition())
    if zero_start is not None:
        partition=sorted(set([x for x in partition if x<=zero_start]
            +[x for x in design.named_interfaces if x>=zero_start]+[zero_start,backend.L]))
    # The exact same core/collar is the extrusion of the already-bound core:
    # curvature is 1/rho_core and 0. Reuse that paid angular input directly.
    partition=sorted(set([x for x in partition if x>=backend.C]+[backend.C,backend.L]))
    if partition[0]!=backend.C or partition[-1]!=backend.L:
        raise ValueError('new body K partition does not cover [C,L]')
    core_K=(1/core['rho']).hi
    stack=[(a,b,0) for a,b in zip(partition[:-1],partition[1:])]
    maximum=core_K;attainer={'region':'complete_open_core_and_constant_core_collar',
        'interval':[0.,backend.C],'same_paid_core_radius_of_curvature':[core['rho'].lo,core['rho'].hi],
        'curvature_upper':core_K}
    digest=hashlib.sha256();accepted=examined=exceeded=0
    unresolved=[];capacity=False
    while stack:
        if time.monotonic()>=clock.deadline:
            unresolved.append({'reason':'new_complete_K_clock','remaining_cells':len(stack)})
            break
        left,right,depth=stack.pop();examined+=1
        bound=None;reason=None
        try:
            angular=same_cell_angular_data(design,left,right,core)
            means=mean.boxes(left,right,core['a0'])
            bound=radial_curvature_with_finite_vertical_primitive(
                means['current'],means['reference'],angular,
                difference=means['difference'],inherited_alpha_upper=inherited['alpha'])
            value=bound['R623_principal_curvature_upper']
            if not math.isfinite(value) or value<0:
                raise ArithmeticError('invalid complete same-cell K enclosure')
            within=value<=args.principal_curvature_budget
        except backend.original.ClockCheckpoint as exc:
            unresolved.append({'interval':[left,right],'depth':depth,'reason':str(exc)})
            break
        except ArithmeticError as exc:
            bound=None;within=False;reason=str(exc)
        refine=depth<args.curvature_refinement_depth and examined<args.maximum_curvature_cells
        if bound is not None and (within or not refine):
            accepted+=1
            if not within:
                exceeded+=1;capacity|=examined>=args.maximum_curvature_cells
            digest.update((json.dumps([left,right,bound],sort_keys=True,separators=(',',':'))+'\n').encode())
            if value>maximum:
                maximum=value;attainer={'interval':[left,right],'same_cell_bounds':bound}
        elif refine:
            middle=left+(right-left)/2
            if middle in (left,right):
                unresolved.append({'interval':[left,right],'reason':'split resolution exhausted'})
                break
            stack.extend(((left,middle,depth+1),(middle,right,depth+1)))
        else:
            unresolved.append({'interval':[left,right],'depth':depth,'reason':reason or 'undefined K'})
            break
        if examined%2000==0:
            emit('PROGRESS',{'examined':examined,'accepted':accepted,'pending':len(stack),
                'new_K_upper_so_far':maximum,'seconds':time.monotonic()-started})
    complete=not stack and not unresolved
    result={'complete_new_K_coverage':complete,'new_principal_curvature_upper':maximum if complete else None,
        'initial_body_intervals':len(partition)-1,'examined_cells':examined,
        'accepted_cells':accepted,'pending_cells':len(stack),'first_unresolved':unresolved,
        'remaining_body_proof_intervals':[[a,b,depth] for a,b,depth in stack],
        'partial_maximum_on_processed_regions_only':maximum,
        'pending_queue_and_current_unresolved_cell_preserved_for_continuation':True,
        'budget_exceeding_valid_bound_cells':exceeded,'refinement_capacity_reached':capacity,
        'curvature_budget_is_not_a_clipped_value_or_acceptance_gate':True,
        'same_cell_coefficients_read_once_for_uv_and_finite_primitive':True,
        'complete_original_four_mode_and_normalization_remainder_angular_coverage':True,
        'core_and_constant_collar_curvature_upper_from_paid_complete_core':core_K,
        'central_cylinder_same_original_material_z':True,
        'lower_body_original_orthogonal_reflection':True,
        'both_complete_Cartesian_caps_curvature_zero':True,
        'zero_suffix_coalescing_keeps_exact_original_material':True,
        'seed_exact_zero_suffix_start':zero_start,'attainer':attainer,
        'accepted_leaf_stream_sha256':digest.hexdigest(),'leaf_tables_saved':False,
        'new_reference_or_global_C0_C1_certificate_claim':False}
    if complete:
        short=short_near_consequence(inherited,maximum)
        long=None
        if short.get('reach_ratio_point03_met',False):
            long_decision='skipped_short_certificate_already_meets_point03'
        elif (short.get('established',False)
                and short['far_pair_reach_lower']>=short['near_pair_reach_lower']):
            # The complete short result is already limited by 1/K. The
            # longer certificate has the smaller near radius .9/K, so
            # no new scalar execution can improve this complete result.
            long_decision='skipped_short_curvature_radius_is_limiting'
        else:
            long_decision='evaluated_short_unestablished_or_far_limited_below_point03'
            long=long_near_consequence(delta=inherited['delta'],nu=inherited['alpha'],
                derivative_upper=(I(1)+I(inherited['alpha'])).hi,
                curvature_upper=maximum,reference_reach_lower=inherited['reference_reach_lower'],
                reference_diameter_upper=inherited['reference_diameter_upper'])
        complete_results=[('original_paid_R621_R604',inherited['old_whole_surface_reach_lower'],
                           inherited['old_whole_surface_reach_over_D_lower'])]
        for name,certificate in (('new_K_R604',short),('new_K_R622',long)):
            if certificate is not None and certificate.get('established'):
                complete_results.append((name,certificate['whole_surface_reach_lower'],
                                         certificate['whole_surface_reach_over_D_lower']))
        selected=max(complete_results,key=lambda row:row[2])
        result.update(R604_short_near_consequence=short,R622_long_near_consequence=long,
            R622_consumption_decision=long_decision,
            selected_complete_certificate=selected[0],whole_surface_reach_lower=selected[1],
            whole_surface_reach_over_D_lower=selected[2],
            reach_ratio_point03_met=selected[2]>=(I(3)/100).hi,
            complete_certificates_compared_without_mixing_near_far_terms=True)
    return result


def main():
    if os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public' or not os.environ.get('GITHUB_RUN_ID'):
        raise RuntimeError('new curvature science requires declared public Actions')
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-state-json',required=True)
    parser.add_argument('--source-state-sha256',required=True)
    parser.add_argument('--maximum-seconds',type=float,default=1800.)
    parser.add_argument('--maximum-curvature-cells',type=int,default=250000)
    parser.add_argument('--curvature-refinement-depth',type=int,default=6)
    parser.add_argument('--principal-curvature-budget',type=float,default=18.)
    parser.add_argument('--height-width-target',type=float,default=1e-6)
    parser.add_argument('--height-maximum-cells',type=int,default=65536)
    args=parser.parse_args()
    if (not 30<args.maximum_seconds<=1800 or not 0<=args.curvature_refinement_depth<=10
            or args.maximum_curvature_cells<1 or args.principal_curvature_budget<=0):
        raise ValueError('outside declared K-only scope')
    raw=sys.stdin.buffer.read() if args.source_state_json=='@stdin' else args.source_state_json.encode()
    if hashlib.sha256(raw).hexdigest()!=args.source_state_sha256:
        raise ValueError('complete new-K source input hash differs')
    source,old_source,old_final,core,inherited=original_input(raw)
    started=time.monotonic();clock=prior.Clock(started+args.maximum_seconds-30)
    counts=defaultdict(int);provider=mean=design=None
    result=field_receipt=failure=None
    emit('DEFINITION',{'schema':SCHEMA,'source':source,'source_state_sha256':args.source_state_sha256,
        'arguments':{k:v for k,v in vars(args).items() if k!='source_state_json'},
        'inherited_complete_same_q_inputs':inherited,
        'reference_and_global_C0_C1_not_rescanned':True,'paid_complete_core_angular_boxes_reused':True,
        'unserialized_height_prefix_and_exact_endpoint_field_necessarily_regenerated_and_charged':True,
        'same_actual_normalized_T_not_replaced_with_linear_v':True,
        'no_new_optimizer_fine_Jacobian_or_old_diagnostic':True,
        'prior_geometry_scientific_seconds':old_final['new_scientific_seconds']})
    try:
        provider=backend.CompactGeometry({'mu':-.040019082162222074,'nu':-.048942275258064924},
            clock.deadline,counts,args.height_width_target,args.height_maximum_cells)
        paid_text=old_source['paid_seed_json']
        if hashlib.sha256(paid_text.encode()).hexdigest()!=old_source['paid_seed_json_sha256']:
            raise ValueError('exact paid material input changed')
        field=prior.ReconstructedField(json.loads(paid_text),old_source['paid_positive_chart'],
            SimpleNamespace(initial_epsilon=.001,rtol=2e-11,atol=2e-13,max_step=.15),clock.deadline)
        field_receipt=field.receipt()
        design=prior.SameFieldRadialDesign(field,old_source['actual_retained_q'],old_source['p'],
            Q_SHA,MESH_SHA,deadline=clock.deadline,backend=backend)
        mean=prior.SameFieldMeanGeometry(design,provider,reference_q=old_source['actual_retained_q'])
        emit('FIELD',{'field_receipt':field_receipt,'seconds':time.monotonic()-started,
            'same_paid_core_bounds':{k:[v.lo,v.hi] for k,v in core.items()}})
        result=certify_curvature(design,mean,core,inherited,args,clock,started)
    except (backend.original.ClockCheckpoint,ArithmeticError,ValueError) as exc:
        failure=type(exc).__name__+': '+str(exc)
    emit('FINAL',{'schema':SCHEMA,'failure':failure,'new_curvature_certificate':result,
        'actual_q_binary64_sha256':Q_SHA,'material_mesh_binary64_sha256':MESH_SHA,
        'inherited_complete_same_q_inputs':inherited,
        'same_material_receipt':None if design is None else design.receipt(),
        'field_reconstruction_receipt':field_receipt,
        'mean_receipt':None if mean is None else mean.receipt(),
        'height_integral_receipt':None if provider is None else getattr(provider.height,'receipt',None),
        'interval_counts':dict(counts),'new_material_original_counts':dict(prior.paid_source.COUNTS),
        'new_stable_material_counts':dict(prior.STABLE_COUNTS),
        'new_scientific_seconds':time.monotonic()-started,
        'reference_and_global_C0_C1_not_recomputed':True,
        'all_old_geometry_optimizer_and_unknown_prior_costs_remain_paid':True,
        'new_fixed_g_macro_amplitude_or_README_completion_claim':False})


if __name__=='__main__':
    main()
