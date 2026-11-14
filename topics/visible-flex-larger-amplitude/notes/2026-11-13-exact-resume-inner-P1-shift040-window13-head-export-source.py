#!/usr/bin/env python3
"""Actual same-P1 translated13-window point head: exact saved readout.
Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
"""
import argparse,gzip,hashlib,json
from pathlib import Path
from fractions import Fraction as F
E=Path('/workspace/scratch/d1aa462cfc02/exact-work')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes())
def ex(v):
 if isinstance(v,list):return F(int(v[0]))*F(2)**int(v[1])
 if 'upper' in v:return ex(v['upper'])
 if 'mantissa' in v:return F(int(v['mantissa']))*F(2)**int(v['binary_exponent'])
 return F(int(v['numerator']),int(v['denominator']))
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 if a.out.exists():raise FileExistsError(a.out)
 pp=E/'inner-P1-shift040-window13-r2.json.gz';rp=E/'inner-P1-shift040-window13-run2-resource.json';hp=E/'inner-P1-shift045-head-export-r1.json'
 if sha(pp)!='8eb18cc6a39c3836bcf1eece10cf6590e35b6eb2f9e50fb8321731a4c7099c22' or sha(hp)!='3ea0049fd53e094687c0d5cfafe857b74d7df9132c6c20939bd04b5858e984de':raise ArithmeticError('Immutable actual head packets')
 d,u,h=map(read,(pp,rp,hp))
 if not(d['all_gates'] and all(d['gates'].values()) and d['gate_count']==850655 and u['exitcode']==0 and u['termination_signal'] is None and u['peak_rss_kib']<98304):raise ArithmeticError('Actual complete owned posterior required')
 if not(d['domain']==h['domain'] and ex(d['angular_weight_translation'])==F(2,5) and ex(d['head_strip'])==ex(d['head_strip_original'])+F(2,5) and d['same_original617_units']==h['same_original617_units']):raise ArithmeticError('Exact domain point strip and units')
 if not(d['complete_mean_inverse_far'] and not d['old_infinite_reweighted'] and d['finite_old_modes_only_reweighted'] and d['new_045_infinite_only_lowered']):raise ArithmeticError('Complete nonlinear field and legal width transfer')
 head=d['translated_head_band_masses'];windows=d['translated_head_window_masses']
 if not(len(head)==3 and len(windows)==13 and all(ex(v)>0 for v in head+windows) and ex(head[1])<F(1,10**48)):raise ArithmeticError('Complete positive head and actual rest target')
 parent=head[2];split=h['shift040_tail_split'];tops=[min(v,parent,key=ex) for v in split['upper_masses']]
 obj=dict(schema='same-R100-P1-complete040-window13-head-export-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',all_gates=True,
  gates=dict(actual_complete_posterior_owned0=True,all850655_math_gates=True,same_complex_P1_domain=True,same_original_node12_point=True,actual_rest_less_than1e48=True,complete_mean_inverse_far=True,no_old_infinite_reweight=True),
  domain=d['domain'],head_strip=d['head_strip_original'],translated_head_strip=d['head_strip'],angular_weight_translation=d['angular_weight_translation'],
  head_bands=d['head_bands'],windows=d['windows'],actual_R100_head_band_masses=d['actual_R100_head_band_masses'],translated_head_band_masses=head,translated_head_window_masses=windows,
  readout_position='Same original physical node12: outer endpoint of innercell12, input to outercell11.',
  point_physical_epsilon_prime=d['point_physical_epsilon_prime'],same_original617_units=d['same_original617_units'],
  primary=dict(path=str(pp),sha256=sha(pp)),resource=dict(path=str(rp),sha256=sha(rp)),
  primary_key_paths=dict(head='translated_head_band_masses',windows='translated_head_window_masses',point='point_physical_epsilon_prime',domain='domain',width='head_strip'),
  shift040_tail_split=dict(physical_mode_bands=[[8192,34814],[34816,None]],upper_masses=tops,parent_shared_mass_at040=parent,original_parent_band=[8192,None],
   meaning='Same complete parent8192-up mass; projected subcaps are not independent masses. Only actual45-to40 descent was used.'),
  complete_mean_inverse_far=True,complete_infinite_repaid=True,source_sha256=sha(Path(__file__)),actual_posterior_source_sha256=d['source_sha256'],
  identity=d['input_identities'],source_parts=d['source_parts'],scope='True existing same-P1 inner point head at tau+.4. Outer transport is not asserted by this export.')
 a.out.write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(dict(all_gates=True,path=str(a.out),sha256=sha(a.out),resource_sha256=sha(rp),head=[str(float(ex(v))) if ex(v)>F(1,10**300) else 'positive very small, exact dyadic in file' for v in head])))
if __name__=='__main__':main()
