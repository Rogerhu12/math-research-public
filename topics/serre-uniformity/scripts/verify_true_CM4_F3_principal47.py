#!/usr/bin/env python3
"""Independent true-CM4 F3 Norm, joint-Laurent and same-component root audit.

Retain the original integer Norm, fiber, tangent, tiny-integral and global
54-coordinate checks. Replace only the R435 regular-j block by the same
R554 j/eta_B joint cancellation, exactly one half of its F2 combination.
No second RR, torsion, or long group-chain computation is performed.
"""
import argparse
import importlib.util
from pathlib import Path
import json


def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for n in ['script-dir','source-dir','poly-source','center-source','norm-source','derivative','ramified-j-certificate','ramified-j-audit','center','polynomial','full-norm','t3-support','t3-norm','principal','second-kind','transport-directory','f2-norm','f2-polynomial','f2-audit','output']:ap.add_argument('--'+n,type=Path,required=True)
 ap.add_argument('--disk-id',required=True);ap.add_argument('--result-id',required=True)
 args=ap.parse_args();helper=args.source_dir/'verify_true_CM4_F2_principal47.py'
 spec=importlib.util.spec_from_file_location('saved_exact_principal_audit',helper);h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
 Q,q,O,Z=h.Q,h.q,h.O,h.Z;read,sha,add,mul,inv,log,power,scale=h.read,h.sha,h.add,h.mul,h.inv,h.log,h.power,h.scale
 names={k:getattr(args,k) for k in ['center','polynomial','full_norm','t3_support','t3_norm','principal','second_kind','f2_norm','f2_polynomial','f2_audit']}
 names.update(helper=helper,center_source=args.center_source,poly_source=args.poly_source,norm_source=args.norm_source,derivative=args.derivative,ramified_j_certificate=args.ramified_j_certificate,ramified_j_audit=args.ramified_j_audit,global_forms=args.script_dir/'data/p41_global_qc_polynomials47_complete.json.gz',manifest=args.transport_directory/'transport_manifest47.json',fixed_support=args.script_dir/'data/p41_T3_fixed_divisor47.json.gz',source_cubic=args.script_dir/'data/p41_source_cubic47_full_saved.json.gz',abel_bases=args.script_dir/'data/p41_hecke3_abel_bases_checkpoint.json.gz',flat_constraint_source=args.script_dir/'p41_finite_flat_divisor_constraints47.py')
 x={k:read(p) for k,p in names.items() if k!='helper' and not k.endswith('_source')}
 center,poly,full,t3,support,flat,second,f2,f2norm,audit=[x[k] for k in ['center','polynomial','full_norm','t3_norm','t3_support','principal','second_kind','f2_polynomial','f2_norm','f2_audit']]
 d=args.disk_id
 assert d in ['SS_j36_06','SS_j36_02']
 assert audit['source_sha256']==sha(helper)
 assert audit['true_CM4_joint_Laurent_correction_bound_to_independent_R554']
 for k in ['center','polynomial','full_norm','t3_norm','principal','second_kind','f2_norm','f2_polynomial','f2_audit']:assert x[k]['disk_id']==d
 assert support['source_disk_id']==d
 assert center['source_sha256']==sha(names['center_source']) and poly['source_sha256']==sha(names['poly_source'])
 assert full['source_sha256']==sha(names['norm_source'])
 edges=[]
 def edge(s,t):
  values=[v for k,v in x[s]['input_sha256'].items() if Path(k).name==names[t].name];assert values and set(values)=={sha(names[t])},(s,t);edges.append([s,t])
 for s,t in [('center','second_kind'),('center','principal'),('center','t3_support'),('center','full_norm'),('polynomial','center'),('polynomial','f2_polynomial'),('polynomial','f2_audit'),('t3_norm','principal'),('t3_norm','second_kind'),('t3_norm','t3_support'),('full_norm','t3_norm'),('full_norm','f2_norm'),('full_norm','principal'),('full_norm','second_kind'),('f2_audit','f2_polynomial')]:edge(s,t)
 for src in ['center','polynomial','full_norm']:edge(src,'derivative')
 edge('polynomial','ramified_j_certificate')
 derivative=x['derivative']
 assert derivative['result']=='R554' and derivative['both_true_rational_CM4_disks_complete']
 assert sha(args.derivative)==sha(args.ramified_j_certificate)
 edge('f2_audit','ramified_j_certificate');edge('f2_audit','ramified_j_audit')
 edge('f2_polynomial','ramified_j_certificate')
 for target in ['fixed_support','source_cubic','abel_bases','flat_constraint_source']:edge('center',target)
 edge('full_norm','fixed_support')
 assert center['explicit_derivative_sha256']==poly['explicit_derivative_sha256']==sha(args.derivative)
 m=full['actual_integer_scale'];assert m==f2norm['actual_integer_scale']==center['actual_integer_scale'] and m%47==9
 assert full['first_function']==f2norm['first_function']
 manifest=x['manifest'];assert len(manifest['functions'])==457
 functions=[]
 for factor in flat['section_factors']:
  path=args.transport_directory/factor['source_function_filename'];assert sha(path)==factor['source_function_sha256'];functions.append(read(path))
 assert len(functions)==455
 ep=flat['combined_function_to_actual_A1_t'];expression={f['label']:f['signed_integer_exponent'] for f in flat['section_factors']}
 h.expadd(expression,{'fb':ep['f_b_integer_exponent'],'fc':ep['f0_integer_exponent'],'v1':1,'FP':1,'GQ':-1});expression={k:v for k,v in expression.items() if v}
 assert expression.get('fc',0)==0
 # The helper replays every monic factor quotient, forward unit DAG, and
 # independent exact integer-exponent product on these additional points.
 nT,cT=h.replay_split(t3,functions,manifest,expression)
 assert nT==(t3['actual_norm_Phi_T3_P_mod47four'],0) and log(nT)==(t3['actual_log_norm_Phi_T3_P_mod47four'],0)
 unused,cF=h.replay_split({'charts':full['fixed31_charts']},functions,manifest,expression)
 assert len(full['fixed31_rows'])==31
 counts={};nf=O;lf=Z
 expected_weights={'Z12':-9,'Z0fix':-9,'c11':-18,'v':27}
 for row in full['fixed31_rows']:
  group=row['group'];weight=expected_weights[group];assert row['second_divisor_weight']==weight
  counts[group]=counts.get(group,0)+1;nf=mul(nf,power(row['actual_Phi_value'],weight));lf=add(lf,scale(row['actual_log_Phi_value'],weight))
 assert counts=={'Z12':22,'Z0fix':7,'c11':1,'v':1}
 assert nf[1]==lf[1]==0 and log(nf)==lf
 assert nf[0]==full['fixed31_weighted_norm_mod47four'] and lf[0]==full['fixed31_weighted_log_norm_mod47four']
 collisions={v['label']:v for v in f2norm['fixed_and_collision_part']['rows']}
 for row in full['reused_P_and_b_in_prescribed_unit_parameters']:assert row==collisions[row['label']]
 cl=f2norm['full_canonical_degree106_log_norm'];assert cl==full['reused_canonical_degree106_log_norm']
 bP=[collisions[k] for k in ['P_minus3',d]]
 normlog=(lf[0]+2*sum(row['log_leading_unit_in_prescribed_parameter_mod47four'][0] for row in bP)+2*cl+9*log(nT)[0])%Q
 assert normlog==full['actual_log_norm_Phi_on_F3_second_divisor_mod47four']==center['first_variable_principal_log_norm_mod47four']
 ab,apoint=[row['parameter_tangent']['g1_differential_over_parameter'][0] for row in bP]
 assert [ab,apoint]==center['actual_g1_over_prescribed_parameters_at_base_and_center']
 sigma=pow(2,-9,Q)*pow(ab*pow(apoint,-1,Q)%Q,2,Q)%Q;logsigma=log((sigma,0))[0]
 assert sigma==center['canonical_sigma_fibre_coordinate_mod47four'] and logsigma==center['canonical_sigma_coordinate_log_mod47four']
 assert center['fixed_base_self_intersection_unit_factor']==pow(2,-9,Q)
 parameters=[tuple(v) for v in center['physical_family1_parameters'][0]];tiny={}
 assert h.flatten(center['physical_family1_parameters'])==h.flatten(ep['actual_A1_physical_parameters'])
 for name,coeff in center['integrand_coefficients_0to2'].items():
  ans=Z
  for n,cs in enumerate(coeff,1):
   for t,c in zip(parameters,cs):ans=add(ans,scale(mul(power(t,n),c[0]),pow(n,-1,Q)))
  assert ans[1]==0;tiny[name]=ans[0]
 assert tiny==center['all_actual_tiny_integrals_mod47four']
 weights={'T3C':9,'C':2,'v_minus_b':54,'Z12_minus22b':-9,'Z0fix_minus8b':-9,'c11_minus_b':-18,'K_g1_minus106b':2}
 assert center['second_divisor_connection_weights']==weights
 tinyD=sum(weights[k]*tiny[k] for k in weights)%Q;assert tinyD==center['second_divisor_tiny_integral_mod47four']
 height=(logsigma+pow(m,-1,Q)*(normlog+tinyD))%Q;assert height==center['actual_local_sigma_F3_height_mod47four']
 assert bP[0]['parameter_tangent']['parameter']=='j_minus_jb'
 assert bP[1]['parameter_tangent']['parameter']=='original_R228_z'
 assert bP[1]['parameter_tangent']['dz_over_parameter']==[1,0]
 assert center['base_parameter']=='j_minus_jb' and center['center_parameter']=='original_R228_z'
 assert full['reused_source_parameter_chart']['frame']==center['original_center_frame']
 assert full['reused_source_parameter_chart']['coordinate']==center['original_center_coordinate']
 # Changing the source unit parameter z to 2z must cancel in the same height.
 ap_t=apoint*pow(2,-1,Q)%Q
 sigma_t=pow(2,-9,Q)*pow(ab*pow(ap_t,-1,Q)%Q,2,Q)%Q
 norm_t=(normlog-2*m*log((2,0))[0])%Q
 assert (log((sigma_t,0))[0]+pow(m,-1,Q)*(norm_t+tinyD))%Q==height
 assert support['raw_level_determinant_mod41']==3 and support['total_target_degree']==4
 A,B=map(tuple,support['actual_source_model']);kernel=[scale(power(A,2),-1),scale(B,12),scale(A,6),Z,(3,0)]
 assert kernel==list(map(tuple,support['kernel_polynomial_ascending']))
 for branch in support['branch_records']:
  raw=branch['actual_saved_full_level_record'];mat=raw['raw_level_matrix_mod41']
  assert raw['ell']==raw['degree']==raw['determinant_mod41']==3
  assert (mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0])%41==3
  root=scale(raw['kernel'][0],-1);value=Z
  for c in reversed(kernel):value=add(mul(value,root),c)
  assert value==Z
 rc=x['ramified_j_certificate'];ra=x['ramified_j_audit']
 assert rc['result']==ra['result']=='R554'
 assert ra['certificate_sha256']==sha(args.ramified_j_certificate)
 for key in ['all876_projective_ODE_entries_replayed','all7336_V2_V3_section_entries_reconstructed','all_homogeneous_invariants_reconstructed_by_exact_directional_derivative','both_actual_coarse_j_series_and_unit_tangents_replayed','both_actual_eta_B_simple_poles_and_joint_cancellation_replayed','both_all54_tiny_differentials_match_original_coordinate']:
  assert ra[key],key
 assert rc['both_true_rational_CM4_disks_complete']
 reg=poly['true_CM4_Laurent_regularization']
 assert reg['certificate_sha256']==sha(args.ramified_j_certificate)
 assert reg['true_CM4_pole_jointly_cancelled'] and reg['actual_eta_B_residue_one']
 assert reg['original_frame_and_coordinate_retained']
 assert reg['only_proved_formal_z_powers_removed']
 assert 'ramified_j_regularization' not in poly
 jc=next(c for c in rc['charts'] if d in c['disk_ids']);jr=jc['disk_ids'].index(d)
 assert jc['frame']==center['original_center_frame'] and jc['coordinate']==center['original_center_coordinate']
 assert jc['original_R228_coordinate_unchanged']
 assert jc['actual_eta_B_simple_pole_and_residue_one'] and jc['eta_B_residue']==1
 assert jc['no_nonunit_inversion_or_division_by47'] and jc['exact_formal_v_and_Bv3_orders']==[1,2]
 assert jc['Av_v_over_z_Bv3_over_z2_all_units'] and jc['jprime_and_j_units_in_original_z']
 def scalarrow(values,k):return tuple(values[k][jr][0])
 jj=[scalarrow(jc['j_coefficients_0to4'],k) for k in range(5)]
 eta_regular=[scalarrow(jc['eta_B_regular_coefficients_0to2_mod47cubed'],k) for k in range(3)]
 assert jj[0]==(1728,0) and center['actual_j_at_SS_center_mod47four']==1728
 assert jj[1][0]%47 or jj[1][1]%47
 auditrow=next(v for v in ra['records'] if v['disk_id']==d)
 assert auditrow['actual_residue_eta_B']==1 and auditrow['joint_polar_coefficient']==0
 assert auditrow['j_coefficients_0to4']==[list(v) for v in jj]
 assert auditrow['eta_B_regular_coefficients']==[list(v) for v in eta_regular]
 # Replay the saved complete flat degree-six pole conditions. This uses
 # actual saved jets and integer-pair dots only, not another geometry run.
 t3connection=center['actual_connections']['T3C']
 flat6=t3connection['actual_finite_flat_degree6_pole_constraints']
 assert flat6['degree']==flat6['unit_rank_mod47']==6
 assert flat6['all_constraints_integral_and_full_four_digit_precision']
 assert t3connection['T3P_and_b_and_v_constraint_rank']==6
 assert t3connection['actual_T3_target_pole_constraints']
 assert t3connection['all_actual_trace_equations_verified'] and t3connection['common_good_rows']>504
 assert t3connection['complete_cusp_field_equations'] and t3connection['Frobenius']
 assert t3connection['original_C_all54_family2_calibration_retained']
 def dot(row,col):
  z=Z
  for a,b in zip(row,col):z=add(z,mul(tuple(a),tuple(b)))
  return z
 def unit(v):return bool(v[0]%47 or v[1]%47)
 def rank_pivots(rows):
  mat=[[tuple(c%47 for c in v) for v in row] for row in rows];piv=[];rr=0
  for col in range(len(mat[0])):
   pivot=next((j for j in range(rr,len(mat)) if unit(mat[j][col])),None)
   if pivot is None:continue
   mat[rr],mat[pivot]=mat[pivot],mat[rr]
   iv=inv(mat[rr][col]);mat[rr]=[tuple(c%47 for c in mul(v,iv)) for v in mat[rr]]
   for j in range(rr+1,len(mat)):
    factor=mat[j][col]
    mat[j]=[tuple(c%47 for c in add(v,scale(mul(factor,w),-1))) for v,w in zip(mat[j],mat[rr])]
   piv.append(col);rr+=1
   if rr==len(mat):break
  return rr,piv
 fixed=x['fixed_support']
 b_points=[p['W_mod47four'] for p in fixed['groups']['Z0fix']['points'] if p['is_basepoint_b']]
 v_points=[p['W_mod47four'] for p in fixed['groups']['v']['points']]
 assert len(b_points)==len(v_points)==1
 poles=support['actual_T3_targets_fc_normalized']+b_points+v_points
 assert len(poles)==6 and all(len(row)==73 for row in poles)
 frame=[tuple(v[0]) for v in jc['frame']]
 assert all(dot(row,frame)==O for row in poles)
 recreated=[];accounted=[];residue_keys=[];pair_count=0
 for rec in flat6['records']:
  indices=rec['indices_0based'];assert len(indices) in [1,2]
  assert all(isinstance(i,int) and 0<=i<6 for i in indices)
  accounted+=indices
  first=[tuple(v) for v in poles[indices[0]]]
  residue_keys.append(tuple(tuple(c%47 for c in v) for v in first))
  if len(indices)==1:
   assert rec['kind']=='single_actual_evaluation'
   recreated.append(first);continue
  pair_count+=1
  assert rec['kind']=='integral_divided_difference_pair'
  second_point=[tuple(v) for v in poles[indices[1]]]
  assert rec['actual_first_W_fc_normalized']==[poles[indices[0]]]
  assert rec['actual_second_W_fc_normalized']==[poles[indices[1]]]
  assert rec['frame']==jc['frame']
  coord=[tuple(v[0]) for v in rec['coordinate']]
  delta=tuple(rec['actual_coordinate_difference'][0][0])
  assert delta==add(dot(second_point,coord),scale(dot(first,coord),-1))
  assert all(c%47==0 for c in delta)
  jets=[[tuple(v) for v in row[0]] for row in rec['actual_first_W_jets_0to4']]
  assert len(jets)==5 and jets[0]==first and all(len(row)==73 for row in jets)
  restored=[Z]*73;divided_row=[Z]*73
  for row in reversed(jets):restored=[add(mul(v,delta),w) for v,w in zip(restored,row)]
  for row in reversed(jets[1:]):divided_row=[add(mul(v,delta),w) for v,w in zip(divided_row,row)]
  assert restored==second_point
  assert [list(v) for v in divided_row]==rec['integral_divided_difference_row_mod47four'][0]
  assert [add(v,scale(w,-1)) for v,w in zip(second_point,first)]==[mul(delta,v) for v in divided_row]
  assert dot(divided_row,coord)==O and dot(divided_row,frame)==Z
  assert rec['all73_second_coordinates_reconstructed'] and rec['all73_difference_equals_delta_times_divided_row']
  assert rec['divided_row_coordinate_value_is_one'] and rec['division_by_nonunit_or47_used'] is False
  recreated.extend([first,divided_row])
 assert sorted(accounted)==list(range(6)) and len(set(residue_keys))==len(residue_keys)
 assert [[list(v) for v in row] for row in recreated]==flat6['flat_constraint_rows_mod47four']
 rank,pivots=rank_pivots(recreated)
 assert rank==6 and pivots==flat6['unit_minor_columns_0based']
 qT=[tuple(v[0]) for v in t3connection['denominator_linear_coefficients_mod47four']]
 assert len(qT)==73
 assert all(dot(row,qT)==Z for row in recreated+poles)
 source_point=jc['W_coefficients_0to6'][0][jr]
 assert source_point==support['actual_source_W_fc_normalized']
 assert unit(dot(source_point,qT)) and t3connection['trace_denominator_unit_at_actual_source']
 cubic=x['source_cubic'];bases=x['abel_bases']
 assert cubic['precision']==4 and cubic['point_indices_1based']==list(range(1,821))
 assert cubic['source_sha256']['p41_makdisi47_certificate.json.gz']==ra['model_input_sha256']['p41_makdisi47_certificate.json.gz']
 Wsource=cubic['evaluation_coefficients'][0]
 assert len(Wsource)==820
 I1,I2=[[i-1 for i in family['points_1based']] for family in bases['families']]
 assert len(I1)==len(I2)==54
 assert all(unit(dot(Wsource[i],qT)) for i in I1)
 assert t3connection['trace_denominator_unit_at_all_family1_tiny_points']
 nonunits=[i for i in I2 if not unit(dot(Wsource[i],qT))]
 assert nonunits==t3connection['actual_family2_nonunit_denominator_indices_0based']
 assert isinstance(t3connection['new_denominator_unit_at_all108_calibration_rows'],bool)
 assert t3connection['new_denominator_unit_at_all108_calibration_rows']==(not nonunits)
 actualC_gradient=h.flatten(center['actual_gradients_original_nu_mod47cubed']['C'])
 assert len(actualC_gradient)==108
 assert actualC_gradient==[v%q for v in h.flatten(second['actual54_second_kind_integrals_of_C_mod47four'])]
 assert 'T3C' not in poly.get('fixed_connection_fraction_replacements',{})
 def invseries(v):
  ans=[inv(v[0])]
  for n in range(1,3):
   z=Z
   for k in range(1,n+1):z=add(z,mul(v[k],ans[n-k]))
   ans.append(scale(mul(ans[0],z),-1))
  return ans
 def product(a,b):
  out=[]
  for n in range(3):
   z=Z
   for k in range(n+1):z=add(z,mul(a[k],b[n-k]))
   out.append(z)
  return out
 # Only j, jprime and J=(j-1728)/z have unit constant terms. Never
 # invert j-1728 or the genuine eta_B denominator at its pole.
 jp=[scale(jj[k+1],k+1) for k in range(3)]
 jpp=[scale(jj[k+2],(k+2)*(k+1)) for k in range(3)]
 junit=jj[1:]
 jup=[scale(junit[k+1],k+1) for k in range(3)]
 logp=product(jpp,invseries(jp))
 logj=product(jp,invseries(jj))
 logu=product(jup,invseries(junit))
 assert [list((v[0]%q,v[1]%q)) for v in logu]==[list(scalarrow(jc['dlog_jminus1728_over_z_coefficients_0to2_mod47cubed'],k)) for k in range(3)]
 actualC=[]
 for k in range(3):
  v=add(add(scale(logp[k],-4),scale(logj[k],8*pow(3,-1,Q))),scale(add(logu[k],scale(eta_regular[k],-1)),2))
  actualC.append((v[0]%q,v[1]%q))
 assert actualC==[scalarrow(jc['regular_F2_combination_coefficients_0to2_mod47cubed'],k) for k in range(3)]
 assert auditrow['regular_F2_combination_coefficients']==[list(v) for v in actualC]
 halfC=[((v[0]*pow(2,-1,q))%q,(v[1]*pow(2,-1,q))%q) for v in actualC]
 assert halfC==[scalarrow(jc['regular_F3_combination_coefficients_0to2_mod47cubed'],k) for k in range(3)]
 expectedC=[[[list(v)]] for v in halfC]
 pieces=poly['differential_pieces_coefficients_mod47cubed']
 assert pieces['combined_regular_true_CM4_j_and_eta_B_correction']==expectedC
 assert f2['differential_pieces_coefficients_mod47cubed']['combined_regular_true_CM4_j_and_eta_B_correction']==[[[list(v)]] for v in actualC]
 assert all(key not in pieces for key in ['minus_eta_B','minus2_eta_B','four_thirds_dlog_j','4_self_regular_j','dlog_j_minus1728','two_dlog_j_minus1728','eight_thirds_dlog_j','8_self_regular_j','combined_regular_ramified_j_correction'])
 assert '4_self_regular_z' in pieces and '8_self_regular_z' not in pieces
 assert reg['all_combined_coefficients_equal_half_R554']
 diff=[]
 for k in range(3):
  z=Z
  for terms in pieces.values():z=add(z,terms[k][0][0])
  diff.append((z[0]%q,z[1]%q))
 assert [list(z) for z in diff]==[v[0][0] for v in poly['local_differential_coefficients_0to2_in_z_mod47cubed']]
 assert all(z[1]==0 for z in diff)
 hp=poly['canonical_local_sigma_F3_height_coefficients_0to3_in_y_mod47four'];assert hp[0]==height
 dcoeff=[h.flatten(x)[0] for x in poly['local_differential_coefficients_0to2_in_z_mod47cubed']]
 assert hp[1:]==[v*47**(i+1)*pow(i+1,-1,Q)%Q for i,v in enumerate(dcoeff)]
 aa=poly['actual_cyclic_C_coefficients_0to3_in_y_mod47cubed'];assert aa==f2['actual_cyclic_C_coefficients_0to3_in_y_mod47cubed']
 globaldata=x['global_forms'];F=next(v for v in globaldata['directions'] if v['n']==3)
 assert F['F_Tn_coefficient']==9 and F['F_identity_coefficient']==2
 based=F['based_C'];gp=[0]*7
 assert all(v%47==0 for v in based['linear_vector_mod47four'])
 for k in range(4):gp[k]+=sum(u*v for u,v in zip(based['linear_vector_mod47four'],aa[k]))
 gp[0]+=based['constant_mod47four'];off=0
 for block in based['quadratic_blocks_mod47four']:
  n=len(block);assert all(v%47==0 for row in block for v in row)
  for k in range(4):
   for ell in range(4):gp[k+ell]+=sum(aa[k][off+i]*block[i][j]*aa[ell][off+j] for i in range(n) for j in range(n))
  off+=n
 assert off==54;gp=[v%Q for v in gp];assert gp[5:]==[0,0];gp=gp[:5]
 assert gp==poly['global_F3_coefficients_0to4_in_y_mod47four']
 qc=[(v-800*(hp[k] if k<4 else 0))%Q for k,v in enumerate(gp)]
 assert qc==poly['actual_QC_F3_coefficients_0to4_in_y_mod47four'] and all(v%47==0 for v in qc)
 labels=globaldata['component_order'];assert labels==[0,3,28,32]
 fi=globaldata['direction_indices'].index(3);targets=[v['QC_defect_target_mod47four'][fi] for v in globaldata['component_vectors']]
 assert targets==poly['F3_bad_targets_in_same_component_order']==[0,0,2621472,2621472]
 f2coeff=f2['actual_QC_F2_coefficients_0to4_in_y_mod47four'];tests=[];remaining=[]
 assert all(v%47==0 for v in f2coeff)
 divided=[v//47 for v in f2coeff];red=[v%47 for v in divided]
 roots=[y for y in range(47) if sum(c*pow(y,k,47) for k,c in enumerate(red))%47==0]
 assert red==f2['QC_divided_by47_reduction_coefficients_mod47']
 assert roots==f2['residual_QC_roots']==audit['residual_roots']
 lifted=[];singular=[]
 for y0 in roots:
  derivative_value=sum(k*c*pow(y0,k-1,47) for k,c in enumerate(divided) if k)%47
  if not derivative_value:
   value=sum(c*pow(y0,k,47**2) for k,c in enumerate(divided))%(47**2)
   possible=[y0+47*t for t in range(47) if sum(c*pow(y0+47*t,k,47**2) for k,c in enumerate(divided))%(47**2)==0]
   singular.append({'root_mod47':y0,'derivative_mod47':0,'QC_div47_value_mod47square':value,'all47_second_digits_checked':True,'lifts_mod47square':possible,'excluded':not possible})
   assert not possible,('unresolved multiple F2 root',y0,possible)
   continue
  y=y0;mod=47;digits=[y0]
  for _ in range(2):
   value=sum(c*pow(y,k,mod*47) for k,c in enumerate(divided))%(mod*47)
   assert value%mod==0
   digit=-(value//mod)*pow(derivative_value,-1,47)%47
   y+=mod*digit;digits.append(digit);mod*=47
  assert sum(c*pow(y,k,Q) for k,c in enumerate(f2coeff))%Q==0
  lifted.append({'y_mod47cubed':y,'z_mod47four':47*y,'y_base47_digits':digits,'derivative_mod47':derivative_value})
 assert lifted==audit['simple_single_F2_root_candidates_to_available_precision']
 assert singular==audit['multiple_F2_residual_branch_certificates']
 assert len(lifted)+len(singular)==len(roots) and audit['all_F2_residual_branches_accounted_for']
 for candidate in audit['simple_single_F2_root_candidates_to_available_precision']:
  y=candidate['y_mod47cubed'];assert sum(v*pow(y,k,Q) for k,v in enumerate(f2coeff))%Q==0 and candidate['derivative_mod47']%47
  value=sum(v*pow(y,k,Q) for k,v in enumerate(qc))%Q;components=[]
  for label,target in zip(labels,targets):
   difference=(value-target)%Q;components.append({'bad_component_label':label,'QC_F3_minus_target_mod47four':difference,'excluded':difference!=0})
   if difference==0:remaining.append({'y_mod47cubed':y,'bad_component_label':label})
  tests.append({'F2_y_mod47cubed':y,'F3_QC_value_mod47four':value,'same_bad_component_tests':components})
 assert tests==poly['actual_F2_candidates_checked_at_full_available_precision'] and remaining==poly['remaining_F2_F3_candidate_and_component_pairs']
 assert poly['entire_disk_excluded_by_F2_and_F3_for_all_four_bad_components']==(not remaining)
 assert poly.get('eta_B_fraction_replacement') is None and f2.get('eta_B_fraction_replacement') is None
 eta_audit_source=args.source_dir/'verify_selected_SS_F2_all_unit_fractions47.py'
 es=importlib.util.spec_from_file_location('saved_exact_eta_fraction_audit',eta_audit_source);eh=importlib.util.module_from_spec(es);es.loader.exec_module(eh)
 eta_audit=eh.audit_eta_B_fraction(args,poly)
 # Augment only the pole-support metadata from its already bound true source.
 # The original numerator, denominator, center value and all other data remain.
 import copy
 center_for_fraction_audit=copy.deepcopy(center)
 if 'T3C' in poly.get('fixed_connection_fraction_replacements',{}):
  edge('polynomial','t3_support')
  rec=poly['fixed_connection_fraction_replacements']['T3C']
  assert rec['T3_support_sha256']==sha(args.t3_support)
  actual_poles=support['actual_T3_targets_fc_normalized']+center['actual_connections']['v_minus_b']['finite_pole_coordinates_fc_normalized']
  assert len(actual_poles)==6 and rec['actual_unchanged_pole_support']==actual_poles
  center_for_fraction_audit['actual_connections']['T3C']['finite_pole_coordinates_fc_normalized']=actual_poles
 fixed_audit=eh.audit_fractions(args,center_for_fraction_audit,poly)
 names['eta_B_fraction_audit_source']=eta_audit_source
 out={'result':args.result_id,'disk_id':d,'input_sha256':{str(p):sha(p) for p in names.values()},'source_sha256':sha(__file__),
 'nested_input_hash_edges_checked':edges,'actual_T3_four_kernel_roots_and_raw_det3_verified':True,
 'T3_actual_saved_Weierstrass_relations_replayed':cT,'fixed31_actual_saved_Weierstrass_relations_replayed':cF,
 'actual_T3_norm':nT[0],'actual_T3_norm_log':log(nT)[0],'fixed31_weighted_norm':nf[0],'fixed31_weighted_norm_log':lf[0],
 'same_true_Phi_canonical106_and_P_b_tangents_reused_by_hash_identity':True,
 'canonical_sigma_with_base_factor_2power_minus9':sigma,'canonical_sigma_log':logsigma,'second_divisor_tiny':tinyD,
 'full_first_norm_log':normlog,'actual_center_height':height,'source_unit_parameter_change_cancels_in_actual_height':True,'R554_half_joint_Laurent_combination_replayed_from_original_j_and_eta_B':True,
 'R554_original_coarse_certificate_and_independent_audit_bound':True,
 'genuine_eta_B_pole_jointly_cancelled_without_fraction_replacement':True,
 'all_actual_F2_Hensel_and_obstructed_multiple_branches_replayed':True,
 'actual_T3_degree6_flat_constraints_replayed_mod47four':True,
 'actual_T3_flat_constraint_rank_mod47':rank,
 'actual_T3_integral_pair_records_replayed':pair_count,
 'actual_T3_denominator_unit_at_source_and_all_I1':True,
 'actual_T3_family2_nonunit_indices_0based':nonunits,
 'original_C_all54_family2_calibration_retained':True,
 'all_actual_tiny_integrals_independently_reassembled':tiny,'actual_local_polynomial':hp,
 'global_F3_independently_reassembled_from_all54_coordinates_and_published_direction':gp,'QC_F3':qc,
 'actual_same_component_root_tests':tests,'remaining_pairs':remaining,'entire_disk_excluded':not remaining,
 'eta_B_fraction_cross_audit':eta_audit,
 'fixed_fraction_cross_audit':fixed_audit,
 'scope':'Independent exact replay of actual saved principal factors and unit Norms, same-function checks, original R554 half joint j/eta_B Laurent correction, tiny integration, normalized fiber and height, all54 global quadratic assembly, complete F2 Hensel branches, and all four same-component candidate tests; no second RR, torsion or long group-chain execution.'}
 args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
 print('PASS independent actual true CM4 F3 audit',d,'height',height,'remaining',remaining,'SHA',sha(args.output))

if __name__=='__main__':main()
