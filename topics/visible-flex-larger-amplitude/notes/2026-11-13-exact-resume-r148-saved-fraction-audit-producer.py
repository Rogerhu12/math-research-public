#!/usr/bin/env python3
"""Independent Fraction consumption of the saved R148 posterior and cut data.
No imported producer math, no source polynomial rerun, no ODE or integration.
The full-source formula and zero-mode placement are separately read in the proof.
"""
from pathlib import Path
from fractions import Fraction as F
import gzip,hashlib,json,resource,time
B=Path('/workspace/scratch/d1aa462cfc02')
P=B/'root-work/r127/sparse-complete-low-r1.json.gz'
R=B/'root-work/r127/sparse-complete-low-r1-resource.json'
SRC=B/'root-work/sparse-complete-low-inputs/root_sparse_complete_low_posterior.py'
MF=B/'root-work/sparse-complete-low-inputs/input-manifest.json'
OUT=B/'exact-work/r148-saved-fraction-audit-r1.json'

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
 with (gzip.open(p,'rt') if str(p).endswith('.gz') else open(p)) as f:return json.load(f)
def q(v):
 if isinstance(v,int):return F(v)
 if isinstance(v,list):return F(int(v[0]))*F(2)**int(v[1])
 if 'upper' in v:return q(v['upper'])
 if 'numerator' in v:return F(int(v['numerator']),int(v['denominator']))
 return F(int(v['mantissa']))*F(2)**int(v['binary_exponent'])
def rat(v):return {'numerator':str(v.numerator),'denominator':str(v.denominator)}

def main():
 if OUT.exists():raise FileExistsError('Preserve actual audit output')
 start=time.monotonic();g={}
 def ck(name,test):
  if not test:raise ArithmeticError(name)
  g[name]=True
 ck('primary_fixed_SHA',sha(P)=='0c7e11319c9f9d4e705a7f3ed742ab0f4239529e7117a4fbaf5b2cd33a15c56f')
 ck('producer_fixed_SHA',sha(SRC)=='df57523d9c303b298f376bbc3fc8648aabc74912c90845f8e07e5b5a6f0dbd50')
 d=read(P);res=read(R);ids=read(MF)
 ck('actual_primary_formal_zero',res['exitcode']==0 and res['termination_signal'] is None and res['resource_wrapper_sha256']=='bbf6c8ac8cb32cbc0f5c1e1c1c1e110ca1744c7839de0f272c172837a4ba3f59')
 ck('input_manifest_identity',sha(MF)==d['input_manifest_sha256'] and ids==d['inputs'])
 ck('original_mathematical_gates',d['all_gates'] and all(d['gates'].values()))
 dat={}
 for name,r in ids.items():
  ck('input_identity_'+name,sha(r['path'])==r['sha256']);dat[name]=read(r['path'])
 old,centre,ball0,budget,axes,beta,prof,full=[dat[k] for k in ['old_projected','centre','ball','budget','axes','full_true_beta','old_profile','full_cut']]
 modes=list(range(2,93,2));r0=q(old['common_joint_error_radius']);V0=q(d['original_V0']);S=q(d['original_S'])
 ck('exact_original_radius_and_small_domain',q(d['common_original_h_radius'])==r0 and V0==F(1,2**40) and S==8 and q(old['Vmax'])==V0 and q(old['normalized_total_radius'])==S and q(d['original_sigma'])==F(1,64))
 ck('precise_parameter_domain_Sunit_T1over32',q(beta['domain']['S_product_radius'])==1 and q(beta['domain']['T_l1_radius'])==F(1,32))
 ck('all46_complete_modes',centre['modes']==modes==[z['mode'] for z in d['rows']]==[z['mode'] for z in beta['mode_rows']]==[z['mode'] for z in prof['rows']])
 ck('same_low_high_zero_split',all(q(centre['true_linear_norms'][str(m)][c])==0 for m in modes[20:] for c in ['P','K']))
 ck('same_original_reference_zero42up',all(q(r[k][side])==0 for r in centre['cut_rows'][20:] for k in ['linear_cut_Q','original_cut_Q'] for side in [0,1]) and all(q(r['original_centre'])==0 for r in axes['rows'][20:]))
 G=[];bd=[];ckernel=[];chead=[]
 for j,m in enumerate(modes):
  b=budget['mode_rows'][j];br=beta['mode_rows'][j];pr=prof['rows'][j]
  weak=next(t for t in b['densities'] if t['density']=='weak_candidate_cap')
  axis=q(axes['rows'][j]['chosen_axis'])
  ck('unchanged_original_axis_'+str(m),axis>0 and axis==q(pr['original_axis']))
  boundary=q(b['complete_weighted_inner_K_trace_to_field_norm'])*q(br['Wsigma1']['chosen_complete'])
  for c in ['P','K']:G.append(q(weak[c+'_sup'])/F(17,16)**2);bd.append(boundary)
  ckernel.append(q(weak['canonical_cut_absolute_mode_bound'])/(F(17,16)**2*axis))
  chead.append(min(q(pr['true_head_including_far']),q(b['inner_K_trace_to_canonical_cut_absolute'])*q(br['Kbar']['chosen_complete'])/axis,q(br['original_cut_weighted_beta_bound'])))
  ck('positive_complete_operators_'+str(m),boundary>0 and ckernel[-1]>0 and chead[-1]>0 and all(x>0 for x in G[-2:]))
 prev=[q(x) for x in old['rounds'][-1]['caps']];initial=prev[:];summaries=[]
 ck('initial_92_caps_inside_same_radius',len(prev)==92 and all(0<x<=r0 for x in prev))
 ck('actual_13_rounds',len(d['rounds'])==13)
 for n,row in enumerate(d['rounds'],1):
  ck('round_index_'+str(n),row['round']==n)
  tail=q(row['shared_inverse_tail_once']);finite=list(map(q,row['finite_polynomial_pairs_low46']));pair=list(map(q,row['complete_source_low46_pairs']))
  ck('round_complete_source_'+str(n),len(finite)==len(pair)==46 and tail>0 and q(row['full_zero_before_output_projection'])>0 and 0<q(row['inverse_leading_mass'])<F(1,2))
  ck('round_common_radius_'+str(n),q(row['common_original_h_radius_retained'])==r0)
  for j,m in enumerate(modes):ck(f'round_{n}_full_pair_{m}',pair[j]==finite[j]+tail and finite[j]>=0)
  saved=list(map(q,row['caps']));improved=0
  for i in range(92):
   exact=min(prev[i],bd[i]+G[i]*pair[i//2])
   ck(f'round_{n}_exact_component_{i}',saved[i]==exact and 0<saved[i]<=prev[i]<=r0)
   improved+=saved[i]<prev[i]
  ck('round_improvement_count_'+str(n),row['improved_components_this_step']==improved)
  summaries.append({'round':n,'changed':improved,'mode92_K':rat(saved[-1]),'shared_tail':rat(tail)})
  prev=saved
 ck('last_stable_caps',summaries[-1]['changed']==0 and [q(x) for x in d['all92_component_caps']]==prev)
 fs=d['final_source'];deg=d['inverse_polynomial_degree'];fp=list(map(q,fs['all_finite_polynomial_pairs']));tail=q(fs['shared_complete_inverse_tail'])
 ck('full_geometric_support_and_tail',deg==16 and len(fp)==828 and fs['polynomial_support_max_mode']==1656 and tail>0 and all(x>=0 for x in fp))
 ck('mean_only_zero_and_full_zero_preserved',fs['mean_only_at_zero'] and q(fs['full_zero_before_projection'])>0 and q(fs['normalized_mean_zero_cap'])>=4*V0*S*S and 0<q(fs['leading_inverse_mass'])<F(1,2) and all(q(x)>0 for x in fs['two_material_numerator_zero_caps']))
 needed=['C_low','low_squared','low_middle','middle_squared','middle_high','high_squared','complete_T']
 fc=full['final_cut'];cm=fc['component_mode_caps'];ck('all_seven_nonlow_components',set(cm)==set(needed))
 outrows=[]
 for j,m in enumerate(modes):
  row=d['rows'][j];oldmap=q(prof['rows'][j]['projected_map_value']);pair=fp[j]+tail
  ck('saved_final_source_pair_'+str(m),q(row['complete_source_pair_cap'])==pair)
  ck('saved_old_and_new_field_caps_'+str(m),q(row['old_P_error_cap'])==initial[2*j] and q(row['old_K_error_cap'])==initial[2*j+1] and q(row['new_P_error_cap'])==prev[2*j] and q(row['new_K_error_cap'])==prev[2*j+1])
  ck('saved_field_and_cut_operators_'+str(m),q(row['field_boundary_cap_each_component'])==bd[2*j] and q(row['true_head_cut'])==chead[j] and q(row['original_source_to_cut'])==ckernel[j])
  direct=ckernel[j]*pair+chead[j] if m>=42 else None
  ck('saved_direct_zero_reference_cut_'+str(m),row['direct_full_N_cut_bound_for_zero_linear_reference'] is None if direct is None else q(row['direct_full_N_cut_bound_for_zero_linear_reference'])==direct)
  value=min(oldmap,direct) if direct is not None else oldmap
  delta=max(q(fc['mode_caps'][j]),sum((q(cm[k][j]) for k in needed),F(0)))
  ck('exact_final_projected_min_'+str(m),q(row['old_projected_map_bound'])==oldmap and q(row['new_projected_map_bound'])==value and value<=oldmap)
  ck('same_complete_nonlow_delta_'+str(m),delta>0 and q(row['original_complete_nonlow_correction'])==delta)
  ck('same_final_fixedpoint_bound_'+str(m),q(row['same_original_full_fixed_point_coordinate_bound'])==value+delta and q(row['old_complete_fixed_point_coordinate_bound'])==oldmap+delta)
  outrows.append({'mode':m,'projected':rat(value),'complete_nonlow':rat(delta),'same_full_fixedpoint':rat(value+delta)})
 ck('shared_T_paid_once_not_replaced_by_sum',d['same_original_T_shared_projected_map_bound']==prof['T_projected_map'] and d['no_shared_T_or_far_mass_resummed_per_mode'])
 ck('retained_old_axes_K_nonlow_and_complete_terms',d['old_original_axes_and_R143_K_unchanged'] and d['R141_nonlow_feedback_bound_unchanged'] and d['complete_mean_inverse_and_positive_far_retained'] and d['no_full_wider_field_or_outer9_continuation_claimed'])
 ck('actual_improvement_totals',d['improved_field_component_count']==sum(x<y for x,y in zip(prev,initial))==49 and d['improved_projected_cut_coordinate_count']==sum(q(z['new_projected_map_bound'])<q(z['old_projected_map_bound']) for z in d['rows'])==22)
 result={'schema':'independent-R148-saved-Fraction-audit-v1','author':'exact_closure (GPT-6 Astra Pro, AI-assisted)','source_sha256':sha(__file__),'input_primary':str(P),'input_primary_sha256':sha(P),'input_resource':str(R),'input_resource_sha256':sha(R),'producer_sha256':sha(SRC),'input_manifest_sha256':sha(MF),'all_gates':True,'gate_count':len(g),'gates':g,'exact_valid_domain':{'S_product_radius':rat(F(1)),'T_l1_radius':rat(F(1,32)),'also_valid_on_R141_expanded_subset':True},'scope':'Independent exact saved 13x92 min updates, complete finite-pair+positive shared tail, original axes/zero references, all46 cut positive sums and unchanged sharedT. Source polynomial not recomputed; complete formula and mean only zero reviewed separately.','rounds':summaries,'cut_rows':outrows,'elapsed_seconds':time.monotonic()-start,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
 OUT.write_text(json.dumps(result,separators=(',',':'))+'\n')
 print(json.dumps({'all_gates':True,'gates':len(g),'sha256':sha(OUT),'seconds':result['elapsed_seconds'],'peak_rss_kib':result['peak_rss_kib']}),flush=True)
if __name__=='__main__':main()
