#!/usr/bin/env python3
"""Current59a4: one actual field, new mean reference and complete C0/C1/K.

Only exact f60 may reuse this q's paid16149 physical observation. A different
realization receives all original fine physical gates on that SAME object.
Every continuous bound and the complete same-mean reference are newly paid.
No material label, old delta/alpha or old mean-reference reach is transferred.
"""
import argparse
from collections import defaultdict
from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import time
from types import SimpleNamespace

BINDINGS={
 'r582_a237_normal_curvature_reach_20261127.py':'577211e39b11d3102cee6154bd209ada0a41a6138bedb7c69a56a67ca6f911ae',
 'r623_finite_vertical_primitive_curvature_20261127.py':'43762578fd236233ccb44e8cd38bbfef44863b05b3fce26844bcd2f0febde80d',
 'r622_long_near_reach_from_complete_bounds_20261127.py':'3ae74691e4588b0636406941119ccc49542dedecc87b0e12bc4685fac7cdbad8',
 'r582_physical_epigraph_continuation_20261127.py':'c0c5c1c82808ea7b54ad68cc5bfee0a921726dc2bf8dfa2ac725600859133e02',
}
for filename,expected in BINDINGS.items():
 if hashlib.sha256(Path(__file__).with_name(filename).read_bytes()).hexdigest()!=expected:
  raise RuntimeError('bound actual-field geometry dependency differs: '+filename)
import r582_a237_normal_curvature_reach_20261127 as prior
import r582_physical_epigraph_continuation_20261127 as physical
from r623_finite_vertical_primitive_curvature_20261127 import (
 same_cell_angular_data,radial_curvature_with_finite_vertical_primitive,
)
from r604_rotating_frame_continuous_norms_20261127 import norm,absolute,sqrt_i
from r622_long_near_reach_from_complete_bounds_20261127 import long_near_consequence

backend,I=prior.backend,prior.I
SCHEMA='r623-current59a4-one-actual-field-new-reference-C0-C1-K-v1'
Q_SHA='59a4ba766a9450509bcbd539639503e8a67d9dc0a98c6c3b63f59879c29a7b45'
PAID_MESH='f60be03b0af36d5d182f21860fe69cef80439c12bb23562d63dc2b57648bf52c'
NORM_NAMES=('C0_upper','C1_difference_upper','R623_principal_curvature_upper',
            'reference_covariant_C2_difference_upper')


def emit(tag,value):
 print('R623_CURRENT_'+tag+' '+json.dumps(value,sort_keys=True,separators=(',',':'),allow_nan=False),flush=True)


def bound_file(repository,relative,size,sha):
 data=(repository/relative).read_bytes()
 if len(data)!=size or hashlib.sha256(data).hexdigest()!=sha:
  raise ValueError('exact necessary input file differs: '+relative)
 return json.loads(data)


def original_input(raw):
 source=json.loads(raw)
 if source.get('schema')!='r623-current59a4-single-actual-field-input-v1':
  raise ValueError('current59a4 actual source input required')
 repository=Path(__file__).resolve().parents[3]
 owner=source['actual_state_request']
 request=bound_file(repository,
  'topics/visible-flex-new-mechanism/computations/request-r582-physical-normal311-resume-20261127.json',
  owner['bytes'],owner['sha256'])
 payload=json.loads(request['lanes']['actual-59a4-f60-normal311']['source_state_json'])
 encoded=payload['complete_original_FINAL_JSON'].encode()
 if (len(encoded)!=479059 or hashlib.sha256(encoded).hexdigest()!=
     '8b6f57b0a4d0f212fe378c10ec563e350efa7ca2b0e7d958912715e25ce42e15'
     or payload['origin']['run_id']!=45901312947 or payload['origin']['job_id']!=140187488430):
  raise ValueError('one actual normal298 complete source FINAL required')
 terminal=json.loads(encoded);retained=terminal['actual_retained_state'];q=retained['q']
 scan=retained['scan']
 if (prior.identity(q)!=Q_SHA or len(q)!=97 or retained['p']!=.181
     or retained['q_identity']!={'entries':97,'binary64_sha256':Q_SHA}
     or terminal['field_receipt']['material_mesh_binary64_sha256']!=PAID_MESH
     or not retained['qualified_on_this_fine_grid'] or not scan['complete_fine_scan']
     or scan['eta_max']!=3.838285782595128e-05
     or scan['geometry_violation_max']!=0. or scan['working_geometry_violation_max']!=0.
     or scan['theta_nodes']!=3072 or scan['radial_grid_identity']!={'entries':16149,
      'binary64_sha256':'2bfc3537692283311887978a96fba44fc95dfd6bb2fea6cdaae80440d1cd2e31'}
     or physical.identity(terminal['actual_fine_radial_nodes'])!={'entries':16167,
      'binary64_sha256':'4240c3ba1d2959ea4c5f81139ead8a1a6e1f218f6b903df1eca94156361c71fd'}):
  raise ValueError('actual59a4/f60 paid physical qualification identity differs')
 recipe_request=bound_file(repository,
  'topics/visible-flex-new-mechanism/computations/request-r582-a237-normal-curvature-20261127.json',
  18337,'a156c7f369a0a64aa2ba60221ea4255c7c583c1f04ccb6122667ac4091110fe2')
 recipe=json.loads(recipe_request['lanes']['actual-a237-normal-curvature']['source_state_json'])
 paid_text=recipe['paid_seed_json']
 if hashlib.sha256(paid_text.encode()).hexdigest()!=recipe['paid_seed_json_sha256']:
  raise ValueError('necessary frozen material seed recipe changed')
 # Reuse only the unchanged p=.181 angular core proof, never a237 global
 # norms or its old mean circle. Its actual source FIELD is retained verbatim.
 core_request=bound_file(repository,
  'topics/visible-flex-new-mechanism/computations/request-r623-a237-curvature-only-20261127.json',
  37687,'a0568ce02685af4347353df8b70704c57ad10dee4406546c865a9062ffbea431')
 core_payload=json.loads(core_request['lanes']['same-a237-new-K']['source_state_json'])
 core_text=core_payload['original_FIELD_JSON'].encode()
 if (len(core_text)!=5672 or hashlib.sha256(core_text).hexdigest()!=
     '490e5e88dd830a4be058f892d716aacc4575db7a209feb19ab712195f4c5b301'
     or recipe['p']!=retained['p']):
  raise ValueError('same p and original complete angular core proof required')
 core={key:I(*value) for key,value in json.loads(core_text)['core_bounds'].items()}
 fine_args=SimpleNamespace(**request['common_parameters'])
 if (fine_args.mean_E_floor!=.25 or fine_args.det_floor!=.1 or fine_args.geometry_margin!=.001
     or fine_args.feasibility_tolerance!=1e-8 or fine_args.material_observation_threshold!=1e-12
     or fine_args.scan_radial_block!=128 or fine_args.theta_nodes!=1536):
  raise ValueError('all original fine physical qualification parameters must remain')
 return source,terminal,recipe,core,fine_args


def certify_current_reference(mean,q,args,clock,started):
 if not all(abs(prior.exact(v))<Fraction(3,5) for v in q[64:80]):
  raise ValueError('current full mean violates the R608 analytic-tail coefficient hypothesis')
 if not q[-1]>backend.original.CORE_HALF:
  raise ValueError('complete cap/central-cylinder height ordering changed')
 tail_rho=I(6072)/100000;target=1/tail_rho
 tail_start=I(backend.L)-I(backend.ELL)*2/25
 compact_end=backend.up(tail_start.hi)
 points={backend.C,compact_end,backend.BACKGROUND_END,backend.CONTROL_LEFT,backend.CONTROL_RIGHT}
 points.update(backend.C+(compact_end-backend.C)*k/65 for k in range(1,65))
 points.update(backend.C+(backend.L-backend.C)*k for k in (1/3,2/3))
 points=sorted(x for x in points if backend.C<=x<=compact_end)
 stack=[(a,b,0) for a,b in zip(points[:-1],points[1:])]
 extrema={'a_min':math.inf,'a_max':0.,'z_s_min':math.inf,'speed_min':math.inf,'curvature_max':0.}
 examined=accepted=wide=0;unresolved=[];peak=None;digest=hashlib.sha256()
 while stack:
  if time.monotonic()>=clock.deadline:
   unresolved.append({'reason':'new_reference_clock','remaining_cells':len(stack)});break
  left,right,depth=stack.pop();examined+=1;row=None;reason=None
  try:
   row=prior.new_reference_jets(mean,left,right,clock)
   finite=all(math.isfinite(v.lo) and math.isfinite(v.hi) for v in row.values())
   # Absolute curvature is nonnegative; remove only possible rounded
   # negative lower endpoints, never reduce the upper enclosure.
   curvature=I(max(0.,row['curvature'].lo),row['curvature'].hi)
   row['curvature']=curvature
   geometric=(finite and row['a'].lo>=backend.RC and row['z_s'].lo>0)
   tight=(curvature.hi<=target.lo or
          (curvature.lo>0 and curvature.hi<=(curvature*I(1002)/1000).lo))
   reason='positive radius/height-speed or finite curvature enclosure unresolved'
  except backend.original.ClockCheckpoint as exc:
   unresolved.append({'interval':[left,right],'depth':depth,'reason':str(exc)});break
  except ArithmeticError as exc:
   row=None;geometric=tight=False;reason=str(exc)
  refine=depth<args.maximum_depth and examined<args.maximum_reference_cells
  if row is not None and geometric and (tight or not refine):
   accepted+=1;wide+=int(not tight)
   digest.update((json.dumps([left,right,{k:[v.lo,v.hi] for k,v in row.items()}],sort_keys=True,separators=(',',':'))+'\n').encode())
   for name,key in (('a_min','a'),('z_s_min','z_s'),('speed_min','speed')):
    extrema[name]=min(extrema[name],row[key].lo)
   extrema['a_max']=max(extrema['a_max'],row['a'].hi)
   if curvature.hi>extrema['curvature_max']:
    extrema['curvature_max']=curvature.hi;peak=[left,right]
  elif refine:
   middle=left+(right-left)/2
   if middle in (left,right):
    unresolved.append({'interval':[left,right],'depth':depth,'reason':'reference bisection exhausted'});break
   stack.extend(((left,middle,depth+1),(middle,right,depth+1)))
  else:
   unresolved.append({'interval':[left,right],'depth':depth,'reason':reason,
    'jets':None if row is None else {k:[v.lo,v.hi] for k,v in row.items()}});break
  if examined%1000==0:
   emit('REFERENCE_PROGRESS',{'examined':examined,'accepted':accepted,'pending':len(stack),'seconds':time.monotonic()-started})
 complete=not stack and not unresolved;rho=diameter=None
 if complete:
  # R608 pays the complete omitted analytic tail at rho=.06072. R599 is
  # monotone in a smaller tau: a>=RC>=tau and |kappa_m|<=1/tau still hold.
  whole_meridian=max(extrema['curvature_max'],target.hi)
  rho=I(min(tail_rho.lo,(1/I(whole_meridian)).lo))
  if not 0<rho.lo<=backend.RC:
   raise ArithmeticError('complete reference reach radius is invalid')
  ar=max(extrema['a_max'],.38,.237)
  diameter=2*backend.sqrt_i(I(ar)**2+I(q[-1])**2)
 return {'complete_new_reference':complete,'uses_exact_current_mean64_80_and_height96':True,
  'old_a237_or_f1_reference_leaves_rho_D_not_used':True,
  'compact_interval':[backend.C,compact_end],
  'exact_R608_tail_start_enclosure':[tail_start.lo,tail_start.hi],
  'R608_full_infinite_tail_coefficient_hypotheses_checked':True,
  'R599_closed_side_caps_core_mirror_hypotheses_paid_if_complete':complete,
  'reach_lower_if_complete':None if rho is None else rho.lo,
  'diameter_upper_if_complete':None if diameter is None else diameter.hi,
  'fixed_rho_is_quality_target_not_clipped_curvature_or_acceptance_gate':True,
  'positive_kappa_lower_required_for_relative_width_test':True,
  'valid_wide_cells_at_refinement_limit':wide,
  'examined_cells':examined,'accepted_cells':accepted,'pending_cells':len(stack),
  'remaining_reference_intervals':[[a,b,d] for a,b,d in stack],'first_unresolved':unresolved,
  'extrema':{k:v if math.isfinite(v) else None for k,v in extrema.items()},
  'curvature_attaining_cell':peak,'accepted_leaf_stream_sha256':digest.hexdigest(),'leaf_tables_saved':False}


def same_cell_bounds(design,mean,core,left,right):
 angular=same_cell_angular_data(design,left,right,core)
 means=mean.boxes(left,right,core['a0'])
 bound=radial_curvature_with_finite_vertical_primitive(
  means['current'],means['reference'],angular,difference=means['difference'])
 # DeltaPhi=(da er+dz ez)+a P(DeltaT). Orthogonal horizontal/vertical
 # primitive components can be combined before taking the triangle bound.
 primitive=norm(I(bound['R623_horizontal_primitive_bounds_upper'][0]),
                I(bound['R623_complete_vertical_primitive_bounds_upper'][0]))
 difference=means['difference'];current=means['current']
 bound['C0_upper']=(norm(difference['a'],difference['z'])+absolute(current['a'])*primitive).hi
 bound['C1_difference_upper']=bound['R623_local_C1_upper_before_inherited_cap']
 blocks=[I(x) for x in bound['R623_full_covariant_blocks_upper']]
 bound['reference_covariant_C2_difference_upper']=norm(blocks[0],blocks[1],blocks[1],blocks[2]).hi
 if right<=backend.C:
  # Exact same core extrusion, independent of q's flat-at-core corrections.
  bound['R623_principal_curvature_upper']=min(bound['R623_principal_curvature_upper'],(1/core['rho']).hi)
  bound['same_complete_core_extrusion_curvature_used']=True
 return bound


def scalar_reach(maxima,reference):
 delta,alpha=I(maxima['C0_upper']),I(maxima['C1_difference_upper'])
 K=I(maxima['R623_principal_curvature_upper']);lam=I((1+alpha).hi)
 rho=I(reference['reach_lower_if_complete']);lo,hi=0.,.75
 for _ in range(32):
  middle=(lo+hi)/2
  if (2*lam*rho*prior.artanh_upper(I(middle))).hi<=(3/(2*K)).lo:lo=middle
  else:hi=middle
 threshold=I((2*rho*I(lo)).lo)
 short={'schema':'r623-current59a4-complete-new-bounds-short-near-v1',
  'near_pair_threshold_lower':threshold.lo,'new_same_scope_delta_alpha_K_reference':True,
  'artanh_positive_terms':64,'scalar_bisections':32,'pi_lower_bound_used':3}
 if threshold.lo<=(2*delta).hi:
  short.update(established=False,reason='far displacement budget not positive')
 else:
  near=1/K;far=(threshold-2*delta)**2/(threshold**2/rho+2*alpha*threshold+4*delta)
  tau=min(near.lo,far.lo);diameter=I(reference['diameter_upper_if_complete'])+2*delta
  ratio=(I(tau)/diameter).lo
  short.update(established=tau>0,near_pair_reach_lower=near.lo,far_pair_reach_lower=far.lo,
   whole_surface_reach_lower=tau,whole_surface_diameter_upper=diameter.hi,
   whole_surface_reach_over_D_lower=ratio,reach_ratio_point03_met=ratio>=(I(3)/100).hi)
 long=None
 if short.get('reach_ratio_point03_met',False):decision='skipped_short_already_meets_point03'
 elif short.get('established',False) and short['far_pair_reach_lower']>=short['near_pair_reach_lower']:
  decision='skipped_short_curvature_radius_is_limiting'
 else:
  decision='evaluated_short_unestablished_or_far_limited_below_point03'
  long=long_near_consequence(delta=delta.hi,nu=alpha.hi,derivative_upper=lam.hi,
   curvature_upper=K.hi,reference_reach_lower=rho.lo,
   reference_diameter_upper=reference['diameter_upper_if_complete'])
 candidates=[(name,row) for name,row in [('new_R604',short),('new_R622',long)]
             if row is not None and row.get('established',False)]
 selected=max(candidates,key=lambda x:x[1]['whole_surface_reach_over_D_lower']) if candidates else None
 return {'R604_short':short,'R622_long':long,'R622_consumption_decision':decision,
  'selected_complete_certificate':None if selected is None else selected[0],
  'whole_surface_reach_lower':None if selected is None else selected[1]['whole_surface_reach_lower'],
  'whole_surface_reach_over_D_lower':None if selected is None else selected[1]['whole_surface_reach_over_D_lower'],
  'reach_ratio_point03_met':False if selected is None else selected[1]['reach_ratio_point03_met'],
  'old_other_q_or_material_certificates_not_compared_or_combined':True,
  'complete_near_far_certificate_terms_are_not_mixed':True}


def certify_current_nonround(design,mean,core,reference,args,clock,started):
 suffix=design.hermite.exact_zero_suffix
 zero_start=None if suffix is None else max(suffix,backend.BACKGROUND_END)
 partition=list(design.initial_partition())
 if zero_start is not None:
  partition=sorted(set([x for x in partition if x<=zero_start]+
   [x for x in design.named_interfaces if x>=zero_start]+[zero_start,backend.L]))
 # The exact Hermite core is checked across all its cells in one query.
 partition=sorted(set([0.,backend.C,backend.L]+[x for x in partition if x>backend.C]))
 if partition[0]!=0. or partition[-1]!=backend.L:
  raise ValueError('actual full material domain is not completely covered')
 stack=[(a,b,0) for a,b in zip(partition[:-1],partition[1:])]
 maxima={name:0. for name in NORM_NAMES};attainers={};examined=accepted=wide=0
 digest=hashlib.sha256();unresolved=[]
 limits={'C0_upper':args.norm_C0_budget,'C1_difference_upper':args.norm_C1_budget,
         'R623_principal_curvature_upper':args.principal_curvature_budget}
 while stack:
  if time.monotonic()>=clock.deadline:
   unresolved.append({'reason':'new_full_geometry_clock','remaining_cells':len(stack)});break
  left,right,depth=stack.pop();examined+=1;bound=None;reason=None
  try:
   bound=same_cell_bounds(design,mean,core,left,right)
   if any(not math.isfinite(bound[k]) or bound[k]<0 for k in NORM_NAMES):
    raise ArithmeticError('invalid complete same-cell enclosure')
   within=all(bound[k]<=value for k,value in limits.items())
  except backend.original.ClockCheckpoint as exc:
   unresolved.append({'interval':[left,right],'depth':depth,'reason':str(exc)});break
  except ArithmeticError as exc:
   bound=None;within=False;reason=str(exc)
  refine=depth<args.norm_refinement_depth and examined<args.maximum_norm_cells
  if bound is not None and (within or not refine):
   accepted+=1;wide+=int(not within)
   digest.update((json.dumps([left,right,bound],sort_keys=True,separators=(',',':'))+'\n').encode())
   for key in NORM_NAMES:
    if bound[key]>maxima[key]:maxima[key]=bound[key];attainers[key]={'interval':[left,right],'same_cell_bounds':bound}
  elif refine:
   middle=left+(right-left)/2
   if middle in (left,right):
    unresolved.append({'interval':[left,right],'depth':depth,'reason':'material bisection exhausted'});break
   stack.extend(((left,middle,depth+1),(middle,right,depth+1)))
  else:
   unresolved.append({'interval':[left,right],'depth':depth,'reason':reason or 'undefined norm'});break
  if examined%2000==0:
   emit('GEOMETRY_PROGRESS',{'examined':examined,'accepted':accepted,'pending':len(stack),
     'partial_bounds_only':maxima,'seconds':time.monotonic()-started})
 complete=not stack and not unresolved
 cap=mean.cap_disk_difference();maxima['C0_upper']=max(maxima['C0_upper'],cap['C0_upper'])
 result={'complete_same_field_C0_C1_K_coverage':complete,'all_theta_covered_without_angular_sampling':True,
  'same_single_cell_coefficients_and_mean_jets_read_once_for_all_bounds':True,
  'old_global_delta_alpha_not_inherited_or_capped':True,
  'central_cylinder_same_material_z_core_extension':True,'lower_body_original_orthogonal_reflection':True,
  'both_full_Cartesian_caps_included':True,'cap_C0_upper':cap['C0_upper'],
  'exact_original_zero_suffix_coalescing_preserves_material_definition':True,'zero_suffix_start':zero_start,
  'initial_proof_intervals':len(partition)-1,'examined_cells':examined,'accepted_cells':accepted,
  'pending_cells':len(stack),'remaining_proof_intervals':[[a,b,d] for a,b,d in stack],
  'first_unresolved':unresolved,'valid_budget_exceeding_cells':wide,
  'budgets_are_refinement_targets_not_clipped_bounds_or_physical_pass_gates':True,
  'uniform_bounds':maxima if complete else None,'partial_processed_region_maxima':maxima,
  'attainers':attainers,'accepted_leaf_stream_sha256':digest.hexdigest(),'leaf_tables_saved':False}
 result['reach_consequence']=scalar_reach(maxima,reference) if complete else None
 return result


def physical_qualification_same_object(field,terminal,q,fine_args,clock):
 actual=field.material_mesh_sha256
 if actual==PAID_MESH:
  return {'reused_identical_q_field_paid_physical_scan':True,'actual_material_mesh_sha256':actual,
   'actual_q_binary64_sha256':Q_SHA,'scan':terminal['actual_retained_state']['scan'],
   'qualified':True,'new_scientific_geometry_value_calls':0,
   'scope_is_original16149_not_current16167':True}
 # A genuinely different realization receives all ORIGINAL physical gates
 # on this exact object. Streaming aggregates the same complete_scan outputs,
 # avoiding unneeded whole-grid field arrays or a second material constructor.
 np=physical.np
 material_nodes,material_report=physical.observation_nodes(field,fine_args)
 original_fine=np.asarray(terminal['actual_fine_radial_nodes'],dtype=float)
 coarse=np.asarray(terminal['actual_constraint_radial_nodes'],dtype=float)
 nodes=np.unique(np.r_[original_fine,material_nodes,coarse,(coarse[:-1]+coarse[1:])/2])
 if not np.all(np.isin(original_fine,nodes)):
  raise ArithmeticError('new actual-field qualification lost an original fine coordinate')
 model=physical.Model(physical.parameters(.181),nodes,3072,field)
 lower,upper=model.bounds();box=float(max(0.,np.max(lower-np.asarray(q)),np.max(np.asarray(q)-upper)))
 report=None;attainers={};minimum={'mean_E_min','det_min','z_min','area_min'}
 maximum={'mean_E_max','ball_radius_max','abs_y_max'};blocks=0;started=time.monotonic()
 for first in range(0,len(nodes),fine_args.scan_radial_block):
  if time.monotonic()>=clock.deadline:
   return {'reused_identical_q_field_paid_physical_scan':False,
    'actual_material_mesh_sha256':actual,'actual_q_binary64_sha256':Q_SHA,
    'qualified':False,'complete_fine_scan':False,'full_requested_grid_identity':physical.identity(nodes),
    'completed_radial_points':first,'next_unprocessed_radial_index':first,
    'partial_processed_report_only':report,'partial_geometry_attainers':attainers,
    'new_completed_fine_blocks':blocks,'remaining_fine_work_not_claimed_complete':True}
  stop=min(first+fine_args.scan_radial_block,len(nodes))
  block=physical.sliced_model(model,slice(first,stop))
  item,fields,eta=physical.hard.complete_scan(block,q,fine_args.mean_E_floor,fine_args.det_floor)
  if report is None:report=dict(item)
  else:
   for name in minimum:report[name]=min(report[name],item[name])
   for name in maximum:report[name]=max(report[name],item[name])
   report['eta_max']=max(report['eta_max'],item['eta_max'])
  for name in fields:
   candidate=dict(item['geometry_attainers'][name]);candidate['radial_index']+=first
   if name not in attainers or candidate['value']<attainers[name]['value']:attainers[name]=candidate
  for name in ('eta_attainer','curvature_attainer'):
   candidate=dict(item[name]);candidate['radial_index']+=first
   if first==0 or candidate['value']>report[name]['value']:report[name]=candidate
  physical.COUNTS['complete_fine_radial_blocks']+=1
  physical.COUNTS['fine_radial_points_evaluated']+=stop-first;blocks+=1
  del block,fields,eta
 worst=min(attainers,key=lambda name:attainers[name]['value'])
 working={name:max(0.,-(v['value']-(0. if name=='positive_height' else fine_args.geometry_margin)))
          for name,v in attainers.items()}
 report.update(radial_nodes=len(nodes),theta_nodes=3072,radial_grid_identity=physical.identity(nodes),
  geometry_attainers=attainers,worst_geometry_group=worst,
  geometry_violation_max=max(0.,-attainers[worst]['value']),
  working_geometry_violation_by_group=working,working_geometry_violation_max=max(working.values()),
  physical_box_violation=box,complete_fine_scan=True,finite_grid_only=True,
  continuous_radial_or_angular_coverage_certified=False,scan_seconds=time.monotonic()-started)
 physical.COUNTS['complete_fine_scans']+=1
 qualified=(box<=1e-12 and report['geometry_violation_max']<=fine_args.feasibility_tolerance
            and report['working_geometry_violation_max']<=fine_args.feasibility_tolerance)
 return {'reused_identical_q_field_paid_physical_scan':False,'actual_material_mesh_sha256':actual,
  'actual_q_binary64_sha256':Q_SHA,'scan':report,'qualified':bool(qualified),
  'all_original_required_fine_coordinates_retained':True,
  'new_material_observation':{k:v for k,v in material_report.items() if k!='finite_material_observation_nodes'},
  'original_complete_scan_and_all_eight_physical_groups_unchanged':True,
  'single_material_object_used_without_second_reconstruction':True,
  'new_completed_fine_blocks':blocks,'no_optimizer_or_AD_or_old_diagnostic':True}


def main():
 if os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public' or not os.environ.get('GITHUB_RUN_ID'):
  raise RuntimeError('declared public Actions only')
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--source-state-json',required=True);parser.add_argument('--source-state-sha256',required=True)
 parser.add_argument('--maximum-seconds',type=float,default=1800.)
 parser.add_argument('--maximum-reference-cells',type=int,default=100000)
 parser.add_argument('--maximum-norm-cells',type=int,default=250000)
 parser.add_argument('--maximum-depth',type=int,default=28)
 parser.add_argument('--norm-refinement-depth',type=int,default=6)
 parser.add_argument('--norm-C0-budget',type=float,default=.0025)
 parser.add_argument('--norm-C1-budget',type=float,default=.03)
 parser.add_argument('--principal-curvature-budget',type=float,default=18.)
 parser.add_argument('--height-width-target',type=float,default=1e-6)
 parser.add_argument('--height-maximum-cells',type=int,default=65536)
 args=parser.parse_args()
 if (not 60<args.maximum_seconds<=1800 or min(args.maximum_reference_cells,args.maximum_norm_cells)<1
     or not 0<=args.norm_refinement_depth<=10 or not 1<=args.maximum_depth<=32
     or min(args.norm_C0_budget,args.norm_C1_budget,args.principal_curvature_budget)<=0):
  raise ValueError('outside declared current-field geometry scope')
 raw=sys.stdin.buffer.read() if args.source_state_json=='@stdin' else args.source_state_json.encode()
 if hashlib.sha256(raw).hexdigest()!=args.source_state_sha256:
  raise ValueError('exact current-field source input differs')
 source,terminal,recipe,core,fine_args=original_input(raw)
 q=terminal['actual_retained_state']['q'];started=time.monotonic();clock=prior.Clock(started+args.maximum_seconds-30)
 counts=defaultdict(int);provider=mean=design=field=None
 reference=nonround=qualification=field_receipt=failure=None
 emit('DEFINITION',{'schema':SCHEMA,'source':source,'source_state_sha256':args.source_state_sha256,
  'arguments':{k:v for k,v in vars(args).items() if k!='source_state_json'},
  'actual_q_binary64_sha256':Q_SHA,'source_paid_material_mesh_sha256':PAID_MESH,
  'complete_new_mean_reference_and_global_C0_C1_K_all_paid':True,
  'only_exact_actual_f60_may_reuse_source16149_fine_observation':True,
  'different_material_uses_same_single_object_for_all_physical_and_continuous_work':True,
  'all_old_geometry_optimizer_failures_and_unknown_costs_preserved_in_original_receipts':True,
  'no_saved_arrays_that_were_never_output_are_fabricated':True})
 try:
  provider=backend.CompactGeometry({'mu':-.040019082162222074,'nu':-.048942275258064924},
   clock.deadline,counts,args.height_width_target,args.height_maximum_cells)
  mean=prior.SameFieldMeanGeometry(prior.MeanContext(q,clock),provider,reference_q=q)
  reference=certify_current_reference(mean,q,args,clock,started);emit('REFERENCE',reference)
  if not reference['complete_new_reference']:
   failure='new_complete_reference_unresolved_no_old_rho_D_transferred'
  else:
   field=prior.ReconstructedField.__new__(prior.ReconstructedField)
   field.__init__(json.loads(recipe['paid_seed_json']),recipe['paid_positive_chart'],
    SimpleNamespace(initial_epsilon=.001,rtol=2e-11,atol=2e-13,max_step=.15),clock.deadline)
   field_receipt=field.receipt();actual_mesh=field.material_mesh_sha256
   emit('FIELD',{'actual_material_mesh_sha256':actual_mesh,'same_as_source_f60':actual_mesh==PAID_MESH,
    'field_receipt':field_receipt,'seconds':time.monotonic()-started,
    'complete_unchanged_core_bounds':{k:[v.lo,v.hi] for k,v in core.items()}})
   qualification=physical_qualification_same_object(field,terminal,q,fine_args,clock)
   emit('PHYSICAL',qualification)
   clock.check()
   # Passing the actual hash defines the NEW field transparently. No inherited
   # delta/alpha/reference is used, regardless of whether this hash repeats.
   design=prior.SameFieldRadialDesign(field,q,.181,Q_SHA,actual_mesh,deadline=clock.deadline,backend=backend)
   mean=prior.SameFieldMeanGeometry(design,provider,reference_q=q)
   nonround=certify_current_nonround(design,mean,core,reference,args,clock,started)
 except Exception as exc:
  failure=type(exc).__name__+': '+str(exc)
 emit('FINAL',{'schema':SCHEMA,'failure':failure,'new_reference':reference,
  'nonround_continuous_geometry':nonround,'physical_qualification':qualification,
  'actual_q_binary64_sha256':Q_SHA,'source_paid_material_mesh_sha256':PAID_MESH,
  'actual_constructed_material_mesh_sha256':None if field is None else getattr(field,'material_mesh_sha256',None),
  'field_reconstruction_receipt':field_receipt,'same_material_receipt':None if design is None else design.receipt(),
  'mean_receipt':None if mean is None else mean.receipt(),
  'height_integral_receipt':None if provider is None else getattr(provider.height,'receipt',None),
  'interval_counts':dict(counts),'new_material_original_counts':dict(prior.paid_source.COUNTS),
  'new_stable_material_counts':dict(prior.STABLE_COUNTS),'new_physical_counts':dict(physical.COUNTS),
  'new_model_counts':dict(physical.MODEL_COUNTS),
  'new_actual_field_counts':None if field is None else dict(getattr(field,'counts',{})),
  'new_scientific_seconds':time.monotonic()-started,
  'old_delta_alpha_mean_reach_D_not_transferred':True,'unclosed_work_remains_in_elapsed_and_counts':True,
  'fixed_metric_family_macro_amplitude_or_README_completion_claim':False})


if __name__=='__main__':main()
