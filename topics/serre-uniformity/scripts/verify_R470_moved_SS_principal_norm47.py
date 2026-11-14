#!/usr/bin/env python3
"""R470-block independent exact replay of the complete moved principal expression and its F2 Norm.

All arithmetic below is Python integer arithmetic. The archived geometric
sections and independently audited initial flips are inputs; this is not a
second RR, formal extraction or scalar-chain execution.
"""
import argparse,json
from pathlib import Path
import verify_moved_SS_F2_clearing_frame47 as v

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ['script-dir','source-dir','qc-dir','chain-dir','transport-dir','based-points','moving-audit','t2-support','derivative','output']:
  ap.add_argument('--'+k,type=Path,required=True)
 ap.add_argument('--disk-id',required=True);args=ap.parse_args();d=args.disk_id;A=args.qc_dir;D=args.script_dir/'data'
 files={'based':args.based_points,'moving_audit':args.moving_audit,'manifest':args.transport_dir/'transport_manifest47.json',
  'multiply':args.chain_dir/(d+'_multiply47.json.gz'),'Abel':args.chain_dir/(d+'_Abel47.json.gz'),
  'second':A/(d+'_actual_second_kind_integrals47.json.gz'),'principal':A/(d+'_principal_expression47.json.gz'),
  'T2_support':args.t2_support,'T2_norm':A/(d+'_actual_T2_principal_norm47.json.gz'),
  'full_norm':A/(d+'_actual_F2_first_variable_norm47.json.gz'),'derivative':args.derivative,
  'known_Abel':D/'p41_three_ordinary_CM_anchors_and_113_global_functions47.json.gz',
  'known_nu':D/'p41_rational_SS_second_kind_integrals47_complete.json.gz'}
 x={k:v.read(p) for k,p in files.items()};flat=x['principal'];man=x['manifest'];fn=x['full_norm'];mult=x['multiply'];ab=x['Abel'];second=x['second']
 sources={'second':'p41_moved_SS_second_kind_from_principal47.py','principal':'p41_moved_principal_chain_flatten47.py',
  'T2_norm':'p41_moved_SS_T2_norm47.py','full_norm':'p41_moved_SS_F2_full_canonical_norm_clearing_frame47.py',
  'manifest':'p41_j9_extended_Abel_with_transports47.py'}
 for k,name in sources.items():assert x[k]['source_sha256']==v.sha(args.source_dir/name),(k,name)
 assert all(x[k]['disk_id']==d for k in ['second','principal','T2_norm','full_norm','multiply','Abel','manifest'])
 assert x['T2_support']['source_disk_id']==d
 edges=[]
 for s,t in [('Abel','multiply'),('second','Abel'),('second','multiply'),('second','based'),('principal','second'),('principal','manifest'),('T2_norm','principal'),('T2_norm','T2_support'),('full_norm','T2_norm'),('full_norm','principal'),('full_norm','second'),('full_norm','multiply'),('full_norm','based'),('full_norm','derivative')]:
  found=[h for p,h in x[s]['input_sha256'].items() if Path(p).name==files[t].name];assert found and set(found)=={v.sha(files[t])},(s,t);edges.append([s,t])
 assert mult['input_sha256']==v.sha(args.based_points) and mult['bits_done']==mult['target_bits']==304 and len(mult['steps'])==454
 assert len(man['functions'])==459 and man['nonformal_principal_function_count']==457 and man['complete_two_actual_initial_moving_flips']
 assert man['completed_Abel_sha256']==v.sha(files['Abel']) and man['multiplication_sha256']==v.sha(files['multiply'])
 allfunctions={}
 for f in man['functions']:
  p=args.transport_dir/f['filename'];assert v.sha(p)==f['sha256'] and p.stat().st_size==f['bytes'];allfunctions[f['filename']]=v.read(p)
 functions=[]
 for f in flat['section_factors']:
  p=args.transport_dir/f['source_function_filename'];assert v.sha(p)==f['source_function_sha256'];functions.append(allfunctions[p.name])
 assert len(functions)==457 and sum(f['line_bundle_power']==2 for f in functions)==3 and sum(f['line_bundle_power']==3 for f in functions)==454
 point=next(z for z in x['based']['records'] if z['disk_id']==d);tr=point['initial_moving_transport'];ff=tr['first_flip'];fmove,hmove=functions[:2]
 assert [fmove['phase'],hmove['phase']]==['initial_moving_first','initial_moving_second']
 assert fmove['numerator_coefficients']==ff['f_V2_coefficients'] and hmove['numerator_coefficients']==tr['second_flip_h_V2_coefficients']
 assert fmove['initial_moving_geometry_based_points_sha256']==hmove['initial_moving_geometry_based_points_sha256']==v.sha(args.based_points)
 assert man['initial_node']['point_sha256']==tr['original_point_sha256'] and fmove['input_nodes']==[man['initial_node']]
 assert fmove['output_node']['point_sha256']==ff['residual_point_sha256'] and fmove['output_node']['scalar_coefficient_of_C']==-1
 assert hmove['input_nodes']==[fmove['output_node']] and hmove['output_node']==man['multiplication_start_node']
 assert point['point_sha256']==man['multiplication_start_node']['point_sha256']==mult['input_point_sha256']
 assert fmove['sole_nonunit_source_rows_0based']==[point['original_source_is_exact_evaluation_row_0based']] and not fmove['unit_on_all820_source_points']
 assert hmove['unit_on_all820_source_points'] and hmove['sole_nonunit_source_rows_0based']==[]
 assert fmove['unit_on_all108_Abel_family_points'] and hmove['unit_on_all108_Abel_family_points']
 ma=x['moving_audit'];assert ma['result']=='R470' and ma['all_selected_initial_moving_transports_independently_replayed'] and ma['selected_disk_count']==4 and d in ma['selected_disk_ids']
 assert v.sha(args.based_points) in ma['input_sha256'].values()
 mr=next(z for z in ma['records'] if z['disk_id']==d)
 assert mr['actual_evaluation_row_0based']==point['original_source_is_exact_evaluation_row_0based'] and mr['chart_leading_unit_at_P']==tr['initial_function_chart_leading_unit_at_P']
 first,last=[man[k]['point_sha256'] for k in ['initial_node','final_node']]
 exponents={first:{'fb':1,'fc':-1}};scalars={first:1}
 for f in functions:
  e={f['label']:1,'fc':-f['line_bundle_power']};s=0
  for node in f['input_nodes']:
   k=node['point_sha256'];assert scalars[k]==node['scalar_coefficient_of_C'];s-=scalars[k];v.expadd(e,exponents[k],-1)
  k=f['output_node']['point_sha256'];assert s==f['output_node']['scalar_coefficient_of_C'];scalars[k]=s;exponents[k]=e
 m=fn['actual_integer_scale'];assert m==scalars[last]==ab['target_multiplier'] and m%47==9
 expr=v.expadd({'v1':1,'FP':1,'GQ':-1,'fc':-1},exponents[last],-1)
 ep=flat['combined_function_to_actual_A1_t'];expected={f['label']:f['signed_integer_exponent'] for f in flat['section_factors']}
 v.expadd(expected,{'fb':ep['f_b_integer_exponent'],'fc':ep['f0_integer_exponent'],'v1':1,'FP':1,'GQ':-1});expected={k:e for k,e in expected.items() if e}
 assert expr==expected and expr.get('fc',0)==0 and expr[fmove['label']]==m and expr[hmove['label']]==-m
 weights={f['label']:f['line_bundle_power'] for f in functions};weights.update(fb=1,fc=1,v1=1,FP=2,GQ=2);assert sum(weights[k]*e for k,e in expr.items())==0
 t2,n=v.replay_split(x['T2_norm'],functions,man,expr);assert n==1371 and t2==(x['T2_norm']['actual_norm_Phi_T2_P_mod47four'],0)
 assert v.log(t2)==(x['T2_norm']['actual_log_norm_Phi_T2_P_mod47four'],0)
 fixed=v.replay_fixed(fn['fixed_and_collision_part'],functions,man,expr,m)
 vals={z['label']:z['norm_mod47four'] for z in fn['full106_canonical_part']['all462_evaluated_section_polynomials_and_norms']};assert len(vals)==462
 high=1
 for k,e in expr.items():high=high*pow(vals[k],e,v.Q)%v.Q
 assert high==fn['full106_canonical_part']['norm_mod47four'] and v.log((high,0))[0]==fn['full_canonical_degree106_log_norm']
 finite=v.Z
 for row in fn['fixed_and_collision_part']['rows']:
  ll=row.get('log_leading_unit_in_j_mod47four',row.get('log_value_mod47four'));finite=v.add(finite,v.scale(ll,row['second_divisor_weight']))
 assert finite==tuple(fn['fixed_and_collision_part']['weighted_actual_log_in_j'])
 total=(finite[0]+4*v.log((high,0))[0]+27*v.log(t2)[0])%v.Q
 assert finite[1]==0 and total==fn['actual_log_norm_Phi_on_F2_second_divisor_mod47four']
 actualnu=v.flatten(second['actual54_second_kind_integrals_of_C_mod47four'])
 knownnu=next(z for z in x['known_nu']['rational_SS_center_integrals'] if z['disk_id']==d)
 assert [z%v.q for z in actualnu]==v.flatten(knownnu['C_original_nu_coordinates_mod47cubed'])
 knownabel=next(z for z in x['known_Abel']['actual_113_rational_disk_global_polynomials'] if z['disk_id']==d)
 assert v.flatten(ab['actual_center_C_cyclic_coordinates_mod47cubed'])==v.flatten(knownabel['actual_center_C_cyclic_coordinates_mod47cubed'])
 grad=v.flatten(ep['log_norm_derivative_at_family2_mod47four']);tiny=v.flatten(second['endpoint']['actual_second_kind_tiny_integrals_at_family1_mod47four'])
 assert [(z+w)%v.Q for z,w in zip(grad,tiny)]==[m*z%v.Q for z in actualnu]
 out={'result':'R470','disk_id':d,'complete_actual_moved_principal_and_F2_Norm_audit':True,'checked_nested_hash_edges':edges,
  'retained_functions_verified':459,'nonformal_integer_SLP_relations_replayed':457,'actual_V2_functions':3,'actual_V3_functions':454,
  'two_initial_move_functions_bound_to_complete_geometric_audit':True,'initial_function_order_and_leading_unit_at_P':{'order':-1,'unit':mr['chart_leading_unit_at_P']},
  'actual_signed_multiplier':m,'moving_f_exponent':m,'moving_h_exponent':-m,'final_fc_exponent':0,'total_section_weight':0,
  'T2_Weierstrass_relation_count':n,'fixed_and_collision_Weierstrass_replay':fixed,
  'full106_evaluated_section_norms_recombined':462,'T2_norm':t2[0],'T2_log':v.log(t2)[0],'full106_norm':high,'full106_log':v.log((high,0))[0],
  'actual_weighted_finite_log_in_j':finite[0],'actual_complete_F2_second_divisor_Norm_log':total,
  'all108_actual_integrals_match_independent_Hecke_solution_mod47cubed':True,'all54_principal_derivatives_plus_terminal_tiny_equal_m_times_original_nu':True,
  'input_sha256':{str(p):v.sha(p) for p in files.values()},'dependency_sources_sha256':{str(args.source_dir/n):v.sha(args.source_dir/n) for n in sources.values()},
  'independent_replay_helper_sha256':v.sha(v.__file__),'source_sha256':v.sha(__file__),
  'scope':'Independent Python integer replay of saved459 functions, all457 exact integer SLP relations, all1371 T2 and10968 fixed/collision Weierstrass relations, all462 high canonical Norm factors, j tangent units and108 independent first-layer constants. No duplicate RR, torsion or long chain; no local height, disk exclusion or full Serre uniformity claim.'}
 args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print('PASS R470 actual moved principal/Norm audit',d,total,v.sha(args.output),flush=True)
if __name__=='__main__':main()
