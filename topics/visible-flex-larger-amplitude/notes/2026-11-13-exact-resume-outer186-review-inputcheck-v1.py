#!/usr/bin/env python3
"""Independent finite identity/support checks for the restricted outer consumer.
Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
This is not a rerun of the full field or a claim that its cut closes.
"""
import argparse,ast,gzip,hashlib,json,time
from fractions import Fraction as F
from pathlib import Path

SOURCE_PINS={
'root_full_field_restricted_window_rebootstrap.py':'31adc4e8163ab69293fcfe3a8c7b134c36d0fdc4f41260babf11669a81c42a12',
'root_refined_window_cut_support.py':'3d4ac8d58f9fe7683a13d29519f379fd6eff15a4cb4a0da6721e02767626a025',
'root_outer_singleton_frequency_sources.py':'76c5a3ccb49d09a7b29af5e3eb430c3cf6b3e3e3935f5ce0290b9812c6c7ecc0'}

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
 p=Path(p)
 with (gzip.open(p,'rt') if p.suffix=='.gz' else p.open()) as f:return json.load(f)
def ex(z):
 if isinstance(z,int):return F(z)
 if isinstance(z,list):return F(int(z[0]))*F(2)**int(z[1])
 if 'upper' in z:return ex(z['upper'])
 if 'mantissa' in z:return F(int(z['mantissa']))*F(2)**int(z['binary_exponent'])
 return F(int(z['numerator']),int(z['denominator']))

def main():
 p=argparse.ArgumentParser(description=__doc__)
 for k in ('source-dir','inputs','out'):p.add_argument('--'+k,type=Path,required=True)
 a=p.parse_args();t=time.monotonic();counts={};identities=[]
 if a.out.exists():raise FileExistsError('Fresh independent review required')
 def check(k,v):
  if not v:raise ArithmeticError('Independent review check: '+k)
  counts[k]=counts.get(k,0)+1
 for name,wanted in SOURCE_PINS.items():
  q=a.source_dir/name;check('reviewed_source_sha',sha(q)==wanted);ast.parse(q.read_text())
  identities.append(dict(path=str(q),sha256=sha(q)))
 ids=read(a.inputs)
 for name,rec in ids.items():
  for row in rec if isinstance(rec,list) else [rec]:check('all_direct_actual_input_pins',sha(row['path'])==row['sha256'])
 def r(k):return read(ids[k]['path'])
 head,primary=r('new_head_export'),r('new_head_primary')
 check('exact_export_primary_and_resource',head['primary']['sha256']==ids['new_head_primary']['sha256'] and head['resource']['sha256']==ids['new_head_resource']['sha256'])
 check('same_complete_head_arrays',head['head_windows']==primary['windows'] and head['actual_R100_head_window_masses']==primary['actual_R100_head_window_masses'] and head['actual_R100_head_band_masses']==primary['actual_R100_head_band_masses'])
 check('same_head_strip_units_domain',head['head_strip']==primary['head_strip'] and head['domain']==primary['domain'] and head['same_original617_units']['sha256']=='617987048c3a599acb42bcafe8dba99155c5cde82d252706769d5e24340ce1b9')
 check('all13_inner_head_frequencies',[m for lo,hi in head['head_windows'] for m in range(lo,hi+1,2)]==list(range(94,8191,2)))
 projected,profile=r('projected_profile'),r('restricted_profile_lift')
 domains={d['name']:d for d in profile['domains']};working=domains['R133_working'];expanded=domains['expanded_profile']
 check('working_and_expanded_shared_domains',ex(working['S_linf_radius'])==F(1,2) and ex(working['T_l1_radius'])==F(1,36) and ex(expanded['S_linf_radius'])==F(3,4) and ex(expanded['T_l1_radius'])==F(1,32))
 for i in range(6,46):
  b=ex(projected['rows'][i]['projected_map_value'])
  check('each_exact_original_fine_axis',0<b and ex(working['original_normalized_T_coordinate_caps'][i])==2*b and ex(expanded['original_normalized_T_coordinate_caps'][i])==4*b)
 check('all_exact_head_profile_axes',list(map(ex,head['domain']['T_coordinate_caps_by_mode']))==list(map(ex,expanded['original_normalized_T_coordinate_caps'])))
 outer=r('original_outer_inputs');joint=read(outer['joint1200']['path']);seed=r('previous_full_bootstrap')
 check('seed_is_same_original_R127_field',seed['same_existing_R127_field'] and seed['same_parameter_domain']==joint['same_R100_parameter_domain'] and seed['inputs']['original_outer_inputs']['sha256']==ids['original_outer_inputs']['sha256'])
 interface=a.inputs.parent/'nonlow_interface.py'
 check('same_frozen_R127_nonlow_interface',sha(interface)==joint['inputs']['nonlow_interface']['sha256'])
 identities.append(dict(path=str(interface),sha256=sha(interface)))
 freq=r('frequency_operators');windows=freq['windows']
 check('all186_even_windows',[m for lo,hi in windows for m in range(lo,hi+1,2)]==list(range(94,34816,2)) and windows[:2]==[[94,94],[96,96]] and len(windows)==186)
 check('actual_frequency_producer_identity',freq['source_sha256']==SOURCE_PINS['root_outer_singleton_frequency_sources.py'])
 check('all25_source_blocks',len(freq['rows'])==25)
 for j,block in enumerate(freq['rows']):
  check('correct_source_and_two_output_ids',block['source_block']==j and [z['mode'] for z in block['rows']]==[94,96])
  for row in block['rows']:
   m=row['mode'];terms=row['C_and_u_times_middle'];modes=[z['middle_mode'] for z in terms]
   expected=list(range(96,187,2)) if m==94 else [94]+list(range(98,189,2))
   check('complete46_or47_distinct_linear_inputs',modes==expected and len(modes)==len(set(modes)))
   for term in terms:
    n=term['middle_mode'];k=term['low_mode'];w=term['input_window']
    check('actual_low_middle_support',k==abs(m-n) and k in range(2,93,2) and windows[w][0]<=n<=windows[w][1] and m in (k+n,n-k))
    check('complete_positive_source_columns',ex(term['C_coefficient'])>0 and ex(term['u_coefficient'])>0)
   pairs=[(z['left_window'],z['right_window']) for z in row['middle_difference_edges']]
   check('unique_difference_window_edges',len(pairs)==len(set(pairs)))
   for edge in row['middle_difference_edges']:
    w,z=edge['left_window'],edge['right_window'];lo,hi=windows[w];zlo,zhi=windows[z]
    check('complete_exact_difference_interval',edge['lower_source_mode']==max(lo,zlo-m) and edge['upper_source_mode']==min(hi,zhi-m) and edge['lower_source_mode']<=edge['upper_source_mode'])
   check('strict_positive_infinite_cancellation_tails',ex(row['middle_high_coefficient'])>0 and ex(row['high_squared_coefficient'])>0 and row['C_times_high_exactly_zero'] and row['u_times_high_exactly_zero'])
 result=dict(schema='independent-restricted-outer186-source-input-review-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',all_gates=True,gates={k:True for k in counts},gate_count=sum(counts.values()),gate_categories=counts,source_sha256=sha(__file__),input_manifest=dict(path=str(a.inputs),sha256=sha(a.inputs)),reviewed_sources=identities,full_field_run_or_cut_success_claimed=False,elapsed_seconds=time.monotonic()-t)
 a.out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(dict(path=str(a.out),sha256=sha(a.out),all_gates=True,gate_count=result['gate_count'],elapsed_seconds=result['elapsed_seconds'])))
if __name__=='__main__':main()
