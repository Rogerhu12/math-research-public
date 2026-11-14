#!/usr/bin/env python3
"""Actual fine53 point readout, intersected with finite R159 point reweighting.
Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
"""
import argparse,gzip,hashlib,json
from pathlib import Path
from fractions import Fraction as F
from flint import arb,ctx

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):
 with (gzip.open(p,'rt') if p.suffix=='.gz' else p.open()) as stream:return json.load(stream)
def ex(v):
 if isinstance(v,list):return F(int(v[0]))*F(2)**int(v[1])
 if 'upper' in v:return ex(v['upper'])
 if 'mantissa' in v:return F(int(v['mantissa']))*F(2)**int(v['binary_exponent'])
 return F(int(v['numerator']),int(v['denominator']))
def packup(v):
 z=v if isinstance(v,arb) else arb(v.numerator)/v.denominator
 if not z.is_finite() or z.lower()<0:raise ArithmeticError('finite positive point bound')
 if z==0:return ['0',0]
 m,e=map(int,z.upper().man_exp());shift=max(0,m.bit_length()-160)
 if shift:m,e=(m+(1<<shift)-1)>>shift,e+shift
 if not arb(m)*arb(2)**e>=z.upper():raise ArithmeticError('outward point readout')
 return [str(m),e]
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--primary',type=Path,required=True);p.add_argument('--primary-sha256',required=True);p.add_argument('--resource',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 if a.out.exists():raise FileExistsError(a.out)
 if sha(a.primary)!=a.primary_sha256:raise ArithmeticError('Frozen actual primary SHA')
 ctx.prec,ctx.threads=256,1;d,u=map(read,(a.primary,a.resource));gates={}
 def gate(k,b):
  if not b:raise ArithmeticError(k)
  gates[k]=True
 gate('same_actual_fine53_producer',d['source_sha256']=='2042372ccd985c92b0962aa79ab3855ed6a1f3c39a68af8730c49fb084467233' and d['schema']=='same-P1-complete-shift040-fine53-finite-posterior-v1')
 gate('complete_owned_posterior',d['all_gates'] and all(d['gates'].values()) and d['steps']==32 and u['exitcode']==0 and u['termination_signal'] is None and u['peak_rss_kib']<98304)
 parentrec=d['input_identities']['parent'];parentpath=Path(parentrec['path'])
 gate('actual_parent13_pin',sha(parentpath)==parentrec['sha256']=='8eb18cc6a39c3836bcf1eece10cf6590e35b6eb2f9e50fb8321731a4c7099c22')
 parent=read(parentpath)
 gate('same_complex_P1_domain',d['domain']==parent['domain'] and d['only_same_existing_complex_P1_field'] and d['domain']['name']=='R156_actual_full_cut_posterior')
 gate('same_point_exact_shift040',ex(d['angular_weight_translation'])==F(2,5) and ex(d['head_strip'])==ex(d['head_strip_original'])+F(2,5) and d['same_original617_units']==parent['same_original617_units'])
 gate('complete_mean_inverse_far_and_infinity',d['complete_mean_inverse_far'] and not d['old_infinite_reweighted'] and d['no_new_ODE_or_integral'] and not d['new_fixedpoint_claimed'])
 gate('all_nested_mass_constraints_retained',d['all_parent13_and_near_rest_mass_constraints_retained'] and d['low_quadratic_tail_uses_all46_separate_modes'])
 windows=d['windows'];head=d['translated_head_band_masses'];caps=d['translated_head_window_masses']
 gate('exact_53_partition',windows==[[m,m] for m in range(94,185,2)]+[[186,192],[194,256],[258,512],[514,1024],[1026,2048],[2050,4096],[4098,8190]] and len(head)==3 and len(caps)==53)
 gate('all_positive_point_readouts',all(ex(v)>0 for v in head+caps) and all(c==r['actual_translated_head'] and ex(c)<=ex(r['wholecell']) and ex(c)<=ex(r['previous_point_parent']) for c,r in zip(caps,d['head_window_readout'])))
 gate('same_positive_point_conversion',ex(d['point_physical_epsilon_prime'])>0 and d['point_physical_epsilon_prime']==parent['point_physical_epsilon_prime'])
 gate('head_bands_no_larger_than_parent',all(ex(x)<=ex(y) for x,y in zip(head,parent['translated_head_band_masses'])))
 tail=d['complete_tail34816_at040'];gate('positive_complete_subtail',0<ex(tail)<=ex(head[2]) and ex(tail)<=ex(parent['complete_tail34816_at040']))
 pointrec=parent['input_identities']['original_point'];pointresource=parent['input_identities']['original_point_resource']
 gate('R159_original_true_point_pin',sha(Path(pointrec['path']))==pointrec['sha256']=='f4e16254dfaff8373f6abf179114b63717fac4ce7c68f41396638a2df34556d2' and sha(Path(pointresource['path']))==pointresource['sha256'])
 point=read(Path(pointrec['path']));pr=read(Path(pointresource['path']))
 gate('R159_actual_same_point_domain',point['all_gates'] and point['complete_mean_inverse_far'] and point['domain']==d['domain'] and ex(point['head_strip'])==ex(d['head_strip_original']) and point['windows']==d['parent_windows'] and pr['exitcode']==0 and pr['termination_signal'] is None)
 old_primary_caps=caps;readout=[];caps=[]
 for w,((lo,hi),oldcap) in enumerate(zip(windows,old_primary_caps)):
  g=d['parent_window_of_fine'][w];pl,ph=point['windows'][g]
  gate('finite_child_contained_in_original_point_parent_'+str(w),pl<=lo<=hi<=ph<8192)
  original=point['actual_R100_head_window_masses'][g]
  z=ex(original);rew=packup(arb(z.numerator)/z.denominator*(arb(2)*hi/5).exp());chosen=min(oldcap,rew,key=ex);caps.append(chosen)
  readout.append(dict(window=[lo,hi],original_parent_window=[pl,ph],primary_window_upper=oldcap,original_width_parent_point_upper=original,finite_reweight_upper=rew,chosen_point_upper=chosen,exponent_numerator=2*hi,exponent_denominator=5))
 old_primary_head=head;head=[]
 for region,inds in enumerate((range(46),range(46,53))):
  total=packup(sum((ex(caps[w]) for w in inds),F(0)));head.append(min(old_primary_head[region],total,key=ex))
 head.append(old_primary_head[2]);groups=[]
 for g,window in enumerate(d['parent_windows']):
  inds=[j for j,p in enumerate(d['parent_window_of_fine']) if p==g]
  total=packup(sum((ex(caps[w]) for w in inds),F(0)))
  groups.append(dict(parent_window=window,fine_indices=inds,shared_mass=min(parent['translated_head_window_masses'][g],total,key=ex)))
 gate('all_refined_caps_no_larger',all(0<ex(x)<=ex(y) for x,y in zip(caps,old_primary_caps)) and all(0<ex(x)<=ex(y) for x,y in zip(head,old_primary_head)))
 obj=dict(schema='same-R100-P1-complete040-fine53-head-export-v2',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',all_gates=all(gates.values()),gates=gates,
  domain=d['domain'],head_strip=d['head_strip_original'],translated_head_strip=d['head_strip'],angular_weight_translation=d['angular_weight_translation'],
  head_bands=d['head_bands'],windows=windows,actual_R100_head_band_masses=d['actual_R100_head_band_masses'],translated_head_band_masses=head,translated_head_window_masses=caps,
  retained_parent13_point_constraints=groups,finite_point_refined_readout=readout,original_point=pointrec,original_point_resource=pointresource,original_primary_translated_head_band_masses=old_primary_head,point_readout_rule='Each finite child uses the original R159 parent point mass times exp(child_hi*2/5), then min with the new fine53 wholecell/point cap. Complete8192-up is not widened. Primary key paths below name the conservative primary candidates; export caps also use this recorded finite readout.',readout_position='Same original physical node12: outer endpoint of innercell12, input to outercell11.',
  point_physical_epsilon_prime=d['point_physical_epsilon_prime'],same_original617_units=d['same_original617_units'],
  primary=dict(path=str(a.primary),sha256=sha(a.primary)),resource=dict(path=str(a.resource),sha256=sha(a.resource)),
  primary_key_paths=dict(head='translated_head_band_masses',windows='translated_head_window_masses',point='point_physical_epsilon_prime',domain='domain',width='head_strip'),
  shift040_tail_split=dict(physical_mode_bands=[[8192,34814],[34816,None]],upper_masses=[head[2],tail],parent_shared_mass_at040=head[2],original_parent_band=[8192,None],meaning='The subcaps share the single complete8192-up parent mass. Both belong to the already proved same actual P1 field; no old infinite cap is widened.'),
  complete_mean_inverse_far=True,complete_infinite_repaid=True,source_sha256=sha(Path(__file__)),actual_posterior_source_sha256=d['source_sha256'],identity=d['input_identities'],source_parts=d['source_parts'],
  scope='Actual same complex P1 field, full fine53 point readout at tau+2/5, with exact finite child reweighting of the same original R159 point. Subsequent outer propagation is a separate consumer.')
 a.out.write_text(json.dumps(obj,indent=2)+'\n')
 print(json.dumps(dict(all_gates=True,gate_count=len(gates),path=str(a.out),sha256=sha(a.out),resource_sha256=sha(a.resource),head=[str(float(ex(v))) if ex(v)>F(1,10**300) else 'strictly positive exact dyadic' for v in head],point184=str(float(ex(caps[45]))))))
if __name__=='__main__':main()
