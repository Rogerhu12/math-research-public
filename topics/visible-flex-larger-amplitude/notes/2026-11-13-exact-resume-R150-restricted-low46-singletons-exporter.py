#!/usr/bin/env python3
"""Export the actual restricted R150 beta in original R123/R131 units.
Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
"""
import argparse,gzip,hashlib,json,resource,time
from fractions import Fraction as F
from pathlib import Path

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
 raw=Path(p).read_bytes();return json.loads(gzip.decompress(raw) if str(p).endswith('.gz') else raw)
def ex(v):
 if isinstance(v,list):return F(int(v[0]))*F(2)**int(v[1])
 if 'upper' in v:return ex(v['upper'])
 if 'mantissa' in v:return F(int(v['mantissa']))*F(2)**int(v['binary_exponent'])
 return F(int(v['numerator']),int(v['denominator']))
def main():
 ap=argparse.ArgumentParser(description=__doc__)
 for k in ('primary','resource','source-summary','source-resource','out'):ap.add_argument('--'+k,type=Path,required=True)
 a=ap.parse_args();start=time.monotonic()
 if a.out.exists():raise FileExistsError(a.out)
 d=read(a.primary);r=read(a.resource);s=read(a.source_summary);sr=read(a.source_resource)
 gates={}
 def gate(k,v):
  if not v:raise ArithmeticError(k)
  gates[k]=True
 gate('actual_primary_pin',sha(a.primary)=='31958f41d78459723a79a0ed61949f7fb2650d8261ba0a0f84a5511eb290b415')
 gate('actual_source_pin',sha(a.source_summary)=='8c1a71d6bb538cf7eba93767c11c2287fa5288de1fc817521044301c3bc80552')
 gate('actual_primary_complete',d['all_gates'] and all(d['gates'].values()) and d['complete_mean_inverse_far'])
 gate('actual_source_complete',s['all_gates'] and all(s['gates'].values()) and s['all213_original_cells'])
 gate('formal_primary_zero',r['exitcode']==0 and r['termination_signal'] is None and r['peak_rss_kib']<98304)
 gate('formal_source_zero',sr['exitcode']==0 and sr['termination_signal'] is None and sr['peak_rss_kib']<98304)
 gate('same_restricted_actual_domain',d['domain']==s['domain'] and d['domain']['name']=='R148_actual_full_cut_posterior' and ex(d['domain']['S_product_radius'])==F(3,8) and ex(d['domain']['T_l1_radius'])==F(1,64))
 gate('same_actual_source_field_pins',d['input_identities']['source_summary']['sha256']==sha(a.source_summary) and d['input_identities']['field']['sha256']=='28e2aaf17c0094c1aaac49750c1e98d1e066eea6846267c77438c3a0a441d333')
 gate('all46_mode_order',[q['mode'] for q in d['mode_rows']]==list(range(2,93,2)))
 rows=[]
 for q in d['mode_rows']:
  m=q['mode'];gate('mode_%02d_complete_positive'%m,all(ex(q[k]['chosen_complete'])>0 for k in ('Kbar','Wsigma1','Whead1')))
  gate('mode_%02d_subset_parent_min'%m,all(ex(q[k]['chosen_complete'])<=ex(q[k]['new_complete_with_true_far']) and ex(q[k]['chosen_complete'])<=ex(q[k]['old_parent_domain_complete']) for k in ('Kbar','Wsigma1','Whead1')))
  rows.append(dict(mode=m,complete_true_beta_cosine_K_coefficient=q['Kbar']['chosen_complete'],complete_true_beta_Wsigma1=q['Wsigma1']['chosen_complete'],complete_true_beta_Wtau_b1=q['Whead1']['chosen_complete'],original_R100_cut_weighted_beta_bound=q['original_cut_weighted_beta_bound'],new_Wsigma1_positive_nonfar_pieces=q['Wsigma1']['nonfar_pieces']))
 gate('shared_T_no_larger_than_sum_singletons',ex(d['common_bounds']['T_cut']['chosen_complete'])<=sum((ex(q['original_cut_weighted_beta_bound']) for q in d['mode_rows'][6:]),F(0)))
 gate('original_sigma',ex(d['sigma'])==F(1,64))
 gate('complete_true_far_positive',ex(d['complete_true_far_common_at_reference_width2'])>0)
 gate('display_T_outward',ex(d['common_bounds']['T_cut']['chosen_complete'])<F('8.966829e-17'))
 gate('display_m92_Kbar_outward',ex(rows[-1]['complete_true_beta_cosine_K_coefficient'])<F('5.393742e-102'))
 gate('display_m92_Wsigma_outward',ex(rows[-1]['complete_true_beta_Wsigma1'])<F('2.111891e-99'))
 gate('display_m92_cut_outward',ex(rows[-1]['original_R100_cut_weighted_beta_bound'])<F('4.052193e-26'))
 ids={k:{'path':str(getattr(a,k)),'bytes':getattr(a,k).stat().st_size,'sha256':sha(getattr(a,k))} for k in ('primary','resource','source_summary','source_resource')}
 out=dict(schema='same-R100-R150-actual-posterior-low46-true-beta-compatible-export-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',all_gates=True,gates=gates,gate_count=len(gates),source_sha256=sha(__file__),actual_inputs=ids,parent_and_field_input_identities=d['input_identities'],domain=d['domain'],sigma=d['sigma'],head_strip=d['head_strip'],all46_mode_rows=rows,T_head_complete_in_original_cut_norm=d['common_bounds']['T_cut']['chosen_complete'],whole46_true_beta_Wsigma1=d['common_bounds']['Wsigma1']['chosen_complete'],whole46_true_beta_Wtau_b1=d['common_bounds']['Whead1']['chosen_complete'],whole46_complete_beta_to_original_field_norm=d['common_bounds']['field']['chosen_complete'],complete_true_far_common_at_reference_width2=d['complete_true_far_common_at_reference_width2'],source_primary_keys={'raw_Kbar':'mode_rows[*].Kbar.chosen_complete','Wsigma1':'mode_rows[*].Wsigma1.chosen_complete','Whead1':'mode_rows[*].Whead1.chosen_complete','shared_T':'common_bounds.T_cut.chosen_complete'},same_original_R123_raw_K_and_R100_axis_units=True,additional_2_or_w_or_S_or_one_plus_m_fee=False,complete_mean_inverse_infinite_far=True,same_existing_original_R100_field=True,not_valid_on_unrestricted_unit_domain=True,no_new_fixedpoint_new_g_or_outer_extension=True,elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 a.out.write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(dict(all_gates=True,gate_count=len(gates),sha256=sha(a.out),bytes=a.out.stat().st_size,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,elapsed_seconds=time.monotonic()-start)),flush=True)
if __name__=='__main__':main()
