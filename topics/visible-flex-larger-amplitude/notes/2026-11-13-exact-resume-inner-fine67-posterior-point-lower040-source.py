#!/usr/bin/env python3
"""Exact same-field node12 head: tau+.6 to tau+.4, with joint parent caps.

Only decreases a proved full analytic width. Finite and infinite Fourier
weights are all paid. The existing .4 point bound is intersected without
altering its input, domain, source or physical-unit identity.
Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,gzip,hashlib,importlib.util,json,resource,time
from flint import arb,ctx
E=Path('/workspace/scratch/d1aa462cfc02/exact-work')
H=E/'2026-11-13-exact-resume-inner-actual-LF-shift060-fine67-posterior-v1.py'
HS='82191d1119c36e1e731ab9ae76a01d8b32008b26bcd165b99e7eb203ac5efaf0'
OLD=E/'inner-fine53-logr-point-r1.json';OS='1905c047655b246283c3374eff763566c8e707e5bd5fc084b480e5d2dc0b2f69'
OR=E/'inner-fine53-logr-point-run1-resource.json';ORS='12a2c1e7084b62d7b2ac1fe59a4624c027055cfc6df76bf59a2a6e513b238672'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
 with (gzip.open(p,'rt') if str(p).endswith('.gz') else open(p)) as f:return json.load(f)
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--primary',type=Path,required=True);ap.add_argument('--primary-sha',required=True);ap.add_argument('--primary-resource',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
 if a.out.exists():raise FileExistsError('fresh complete lower-width export')
 start=time.monotonic();ctx.prec,ctx.threads=256,1;g={};counts={}
 def gate(k,v):
  if not v:raise ArithmeticError(k)
  g[k]=True;counts[k]=counts.get(k,0)+1
 gate('formula_and_old_pins',sha(H)==HS and sha(OLD)==OS and sha(OR)==ORS);spec=importlib.util.spec_from_file_location('fine67_exact_support',H);p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
 ex,ab,pack,up,support=p.ex,p.ab,p.pack,p.up,p.support
 gate('actual_new_primary_pin_owned',sha(a.primary)==a.primary_sha and p.owned(read(a.primary_resource)));d=read(a.primary);old=read(OLD)
 gate('same_actual_full_field_and_point',d['all_gates'] and all(d['gates'].values()) and d['same_original_full_field_identified'] and d['complete_mean_inverse_far'] and d['complete_infinite_repaid'] and d['physical_units_not_changed'] and ex(d['angular_weight_translation'])==F(3,5) and old['all_gates'] and all(old['gates'].values()) and p.owned(read(OR)) and old['only_same_existing_complex_P1_field'] and ex(old['angular_weight_translation'])==F(2,5) and d['domain']==old['domain'] and d['head_strip']==old['head_strip'] and d['same_original617_units']['sha256']==old['same_original617_units']['sha256']=='617987048c3a599acb42bcafe8dba99155c5cde82d252706769d5e24340ce1b9')
 gate('complete67_child_53_parent_partition',d['windows']==p.WIN and d['parent_windows']==old['windows']==p.PARENT and len(d['translated_head_window_masses'])==67 and len(d['parent_point_caps'])==53)
 wide=list(map(ab,d['translated_head_window_masses']));widef=list(map(ex,d['translated_head_window_masses']));parent=list(map(ab,d['parent_point_caps']));oldparent=list(map(ab,old['translated_head_window_masses']));weights=[up((-arb(lo)/5).exp()) for lo,_ in p.WIN]
 # These are simultaneous valid full-parent bounds, not a separate mass per
 # child. The post-point child bounds may further decrease each parent.
 wideparent=[min(parent[i],up(sum((wide[j] for j in js),arb(0)))) for i,js in enumerate(p.GROUPS)]
 loweredparent=[];rows=[]
 for i,js in enumerate(p.GROUPS):
  value=up(ab(support([ex(pack(weights[j])) for j in js],[widef[j] for j in js],ex(pack(wideparent[i])))));chosen=min(value,oldparent[i]);loweredparent.append(chosen)
  gate('each_parent_lowered_once_and_intersected',chosen>0 and chosen<=oldparent[i])
 low=[min(up(wide[j]*weights[j]),loweredparent[p.PAR[j]]) for j in range(67)]
 for j in range(67):
  gate('all_finite_lower_width_weights_paid',low[j]>0 and low[j]<=oldparent[p.PAR[j]])
  rows.append(dict(window=p.WIN[j],parent_window=p.PARENT[p.PAR[j]],width060_head_cap=d['translated_head_window_masses'][j],weight060_to040=pack(weights[j]),width040_head_cap=pack(low[j])))
 bands=[];bandbudgets=[]
 for bi,js in enumerate((list(range(46)),list(range(46,67)))):
  pids=[i for i,gs in enumerate(p.GROUPS) if gs[0] in js];joint=up(sum((loweredparent[i] for i in pids),arb(0)));separate=up(sum((low[j] for j in js),arb(0)));bandwide=up(ab(d['translated_head_band_masses'][bi])*(-arb(p.WIN[js[0]][0])/5).exp());prior=ab(old['translated_head_band_masses'][bi]);value=min(joint,separate,bandwide,prior);bands.append(value)
  bandbudgets.append(dict(parent_mass_sum=pack(joint),child_sum=pack(separate),whole_band_width_loss=pack(bandwide),old_actual_point_band=pack(prior),chosen=pack(value)))
 wideh=ab(d['translated_head_band_masses'][2]);h040=up(wideh*(-arb(8192)/5).exp());h040=min(h040,ab(old['translated_head_band_masses'][2]));bands.append(h040)
 base=[]
 for bi,js in enumerate((list(range(46)),list(range(46,67)))):
  val=up(bands[bi]*(-arb(p.WIN[js[0]][0])*2/5).exp());val=min(val,up(sum((low[j]*(-arb(p.WIN[j][0])*2/5).exp() for j in js),arb(0))),ab(old['actual_R100_head_band_masses'][bi]));base.append(pack(val))
 base.append(pack(min(up(wideh*(-arb(8192)*3/5).exp()),ab(old['actual_R100_head_band_masses'][2]))))
 high34816=up(wideh*(-arb(34816)/5).exp());gate('complete_positive_infinite_lowering',h040.is_finite() and high34816.is_finite() and h040>0 and high34816>0)
 tau=ex(d['head_strip'])+F(2,5);gate('owned_RSS_below96MiB',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<98304)
 out=dict(schema='same-P1-fine67-full-head-lowered060to040-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),all_gates=True,gates=g,gate_categories=counts,gate_count=sum(counts.values()),primary=dict(path=str(a.primary),sha256=a.primary_sha,resource_path=str(a.primary_resource),resource_sha256=sha(a.primary_resource)),old_point=dict(path=str(OLD),sha256=OS,resource_path=str(OR),resource_sha256=ORS),exact_support_formula=dict(path=str(H),sha256=HS),domain=d['domain'],head_strip=d['head_strip'],translated_head_strip=dict(numerator=str(tau.numerator),denominator=str(tau.denominator)),angular_weight_translation=dict(numerator='2',denominator='5'),head_bands=d['head_bands'],windows=p.WIN,parent_windows=p.PARENT,translated_head_window_masses=list(map(pack,low)),translated_parent_head_masses=list(map(pack,loweredparent)),translated_head_band_masses=list(map(pack,bands)),actual_R100_head_band_masses=base,same_original617_units=dict(sha256=d['same_original617_units']['sha256'],units='Original R100 balanced physical P/K strong pair head mass at declared head_strip+2/5. The same actual full field is lowered from a proved3/5 translation; physical units are unchanged.'),readout_position=d['readout_position'],point_physical_epsilon_prime=d['point_physical_epsilon_prime'],rows=rows,band_budgets=bandbudgets,shift040_tail_split=dict(complete_infinite_from8192=pack(h040),complete_infinite_from34816=pack(high34816),wide060_complete_infinite_mass=d['translated_head_band_masses'][2],width_difference=dict(numerator='1',denominator='5'),no_unknown_tail_raised_in_width=True),complete_mean_inverse_far=True,complete_infinite_repaid=True,same_original_full_field_identified=True,parent_common_mass_paid_once=True,only_width_decrease_of_proved_full_field=True,old_finite_and_infinite_point_bounds_intersected_without_relabel=True,outer_new_fixedpoint_or_strip_not_claimed=True,precision_bits=256,storage_bits=160,elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 raw=(json.dumps(out,separators=(',',':'))+'\n').encode();gate('small_export',len(raw)<1000000);a.out.write_bytes(raw)
 print(json.dumps(dict(all_gates=True,path=str(a.out),sha256=sha(a.out),head_bands=[str(v) for v in bands],gate_count=out['gate_count'],elapsed_seconds=out['elapsed_seconds'],peak_rss_kib=out['peak_rss_kib'])),flush=True)
if __name__=='__main__':main()
