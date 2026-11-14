#!/usr/bin/env python3
"""Independent standard-library actual F3 Norm, fiber, global term and joint-root audit."""
import argparse
import importlib.util
from pathlib import Path
import json


def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for n in ['script-dir','source-dir','poly-source','center','polynomial','full-norm','t3-support','t3-norm','principal','second-kind','transport-directory','f2-norm','f2-polynomial','f2-audit','output']:ap.add_argument('--'+n,type=Path,required=True)
 ap.add_argument('--disk-id',required=True);ap.add_argument('--result-id',required=True)
 args=ap.parse_args();helper=args.source_dir/'verify_selected_SS_F2_principal47.py'
 spec=importlib.util.spec_from_file_location('saved_exact_principal_audit',helper);h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
 Q,q,O,Z=h.Q,h.q,h.O,h.Z;read,sha,add,mul,inv,log,power,scale=h.read,h.sha,h.add,h.mul,h.inv,h.log,h.power,h.scale
 names={k:getattr(args,k) for k in ['center','polynomial','full_norm','t3_support','t3_norm','principal','second_kind','f2_norm','f2_polynomial','f2_audit']}
 names.update(helper=helper,center_source=args.source_dir/'p41_selected_SS_F3_connection47.py',poly_source=args.poly_source,global_forms=args.script_dir/'data/p41_global_qc_polynomials47_complete.json.gz',manifest=args.transport_directory/'transport_manifest47.json')
 x={k:read(p) for k,p in names.items() if k not in ['helper','center_source','poly_source']}
 center,poly,full,t3,support,flat,second,f2,f2norm,audit=[x[k] for k in ['center','polynomial','full_norm','t3_norm','t3_support','principal','second_kind','f2_polynomial','f2_norm','f2_audit']]
 d=args.disk_id
 for k in ['center','polynomial','full_norm','t3_norm','principal','second_kind','f2_norm','f2_polynomial','f2_audit']:assert x[k]['disk_id']==d
 assert support['source_disk_id']==d
 assert center['source_sha256']==sha(names['center_source']) and poly['source_sha256']==sha(names['poly_source'])
 edges=[]
 def edge(s,t):
  values=[v for k,v in x[s]['input_sha256'].items() if Path(k).name==names[t].name];assert values and set(values)=={sha(names[t])},(s,t);edges.append([s,t])
 for s,t in [('center','second_kind'),('center','principal'),('center','t3_support'),('center','full_norm'),('polynomial','center'),('polynomial','f2_polynomial'),('polynomial','f2_audit'),('t3_norm','principal'),('t3_norm','second_kind'),('t3_norm','t3_support'),('full_norm','t3_norm'),('full_norm','f2_norm'),('full_norm','principal'),('full_norm','second_kind'),('f2_audit','f2_polynomial')]:edge(s,t)
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
 for row in full['reused_P_and_b_in_the_same_j_tangents']:assert row==collisions[row['label']]
 cl=f2norm['full_canonical_degree106_log_norm'];assert cl==full['reused_canonical_degree106_log_norm']
 bP=[collisions[k] for k in ['P_minus3',d]]
 normlog=(lf[0]+2*sum(row['log_leading_unit_in_j_mod47four'][0] for row in bP)+2*cl+9*log(nT)[0])%Q
 assert normlog==full['actual_log_norm_Phi_on_F3_second_divisor_mod47four']==center['first_variable_principal_log_norm_mod47four']
 ab,apoint=[row['j_tangent']['g1_differential_over_dj'][0] for row in bP]
 assert [ab,apoint]==center['actual_g1_over_dj_at_base_and_center']
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
 alpha=tuple(bP[1]['j_tangent']['dz_over_dj']);assert alpha[1]==0
 az=apoint*pow(alpha[0],-1,Q)%Q;sigmaz=pow(2,-9,Q)*pow(ab*pow(az,-1,Q)%Q,2,Q)%Q
 normz=(normlog-2*m*log(alpha)[0])%Q
 assert (log((sigmaz,0))[0]+pow(m,-1,Q)*(normz+tinyD))%Q==height
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
 assert targets==poly['F3_bad_targets_in_same_component_order']
 f2coeff=f2['actual_QC_F2_coefficients_0to4_in_y_mod47four'];tests=[];remaining=[]
 for candidate in audit['simple_single_F2_root_candidates_to_available_precision']:
  y=candidate['y_mod47cubed'];assert sum(v*pow(y,k,Q) for k,v in enumerate(f2coeff))%Q==0 and candidate['derivative_mod47']%47
  value=sum(v*pow(y,k,Q) for k,v in enumerate(qc))%Q;components=[]
  for label,target in zip(labels,targets):
   difference=(value-target)%Q;components.append({'bad_component_label':label,'QC_F3_minus_target_mod47four':difference,'excluded':difference!=0})
   if difference==0:remaining.append({'y_mod47cubed':y,'bad_component_label':label})
  tests.append({'F2_y_mod47cubed':y,'F3_QC_value_mod47four':value,'same_bad_component_tests':components})
 assert tests==poly['actual_F2_candidates_checked_at_full_available_precision'] and remaining==poly['remaining_F2_F3_candidate_and_component_pairs']
 assert poly['entire_disk_excluded_by_F2_and_F3_for_all_four_bad_components']==(not remaining)
 assert poly.get('eta_B_fraction_replacement')==f2.get('eta_B_fraction_replacement')
 eta_audit_source=args.source_dir/'verify_selected_SS_F2_all_unit_fractions47.py'
 es=importlib.util.spec_from_file_location('saved_exact_eta_fraction_audit',eta_audit_source);eh=importlib.util.module_from_spec(es);es.loader.exec_module(eh)
 eta_audit=eh.audit_eta_B_fraction(args,poly)
 names['eta_B_fraction_audit_source']=eta_audit_source
 out={'result':args.result_id,'disk_id':d,'input_sha256':{str(p):sha(p) for p in names.values()},'source_sha256':sha(__file__),
 'nested_input_hash_edges_checked':edges,'actual_T3_four_kernel_roots_and_raw_det3_verified':True,
 'T3_actual_saved_Weierstrass_relations_replayed':cT,'fixed31_actual_saved_Weierstrass_relations_replayed':cF,
 'actual_T3_norm':nT[0],'actual_T3_norm_log':log(nT)[0],'fixed31_weighted_norm':nf[0],'fixed31_weighted_norm_log':lf[0],
 'same_true_Phi_canonical106_and_P_b_tangents_reused_by_hash_identity':True,
 'canonical_sigma_with_base_factor_2power_minus9':sigma,'canonical_sigma_log':logsigma,'second_divisor_tiny':tinyD,
 'full_first_norm_log':normlog,'actual_center_height':height,'j_z_tangent_change_cancels_in_actual_height':True,
 'all_actual_tiny_integrals_independently_reassembled':tiny,'actual_local_polynomial':hp,
 'global_F3_independently_reassembled_from_all54_coordinates_and_published_direction':gp,'QC_F3':qc,
 'actual_same_component_root_tests':tests,'remaining_pairs':remaining,'entire_disk_excluded':not remaining,
 'eta_B_fraction_cross_audit':eta_audit,
 'scope':'Independent exact replay of actual saved principal factors and unit Norms, same-function checks, tiny integration, normalized fiber and height, all54 global quadratic assembly, and all four same-component candidate tests; no second RR or torsion execution.'}
 args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
 print('PASS independent actual SS F3 audit',d,'height',height,'remaining',remaining,'SHA',sha(args.output))

if __name__=='__main__':main()
