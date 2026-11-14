#!/usr/bin/env python3
"""True same-P1 full-field head after actual+.6 conditional identification.

Only finite saved point caps are translated; the full infinite head comes
from the newly proved+.6 full field. Coarse rest budget is retained honestly.
Author: exact_closure (GPT-6 Astra Pro; AI-assisted),2026-11-13.
"""
import argparse,json,gzip,hashlib,resource,time
from pathlib import Path
from fractions import Fraction as F
from flint import arb,ctx
E=Path('/workspace/scratch/d1aa462cfc02/exact-work')
PINS={
 'new':(E/'inner-actual-LF-shift060-conditional-existence-r1.json.gz','e793121cbc201297960a35bbaa427fe395fb17ba34c7dd96c8a02fd4a1fa4e66'),
 'new_resource':(E/'inner-actual-LF-shift060-conditional-assemble-run1-resource.json','87cd7bd9719b20b64bae524a72fc9c9dd955c3f7ad0f962d31165c7f267098f9'),
 'comparison':(E/'inner-actual-LF-shift060-samefield-r2.json.gz','f8563471233891b8edc6651b7eb375ad94d1c031ebf1a150325a11897e3db710'),
 'comparison_resource':(E/'inner-actual-LF-comparison040-assemble-run2-resource.json','3ffd7eb5fba7c1624f800480070229fd033f3aaee75b822e52803414368f598d'),
 'old_point':(E/'inner-fine53-logr-point-r1.json','1905c047655b246283c3374eff763566c8e707e5bd5fc084b480e5d2dc0b2f69'),
 'old_field':(E/'inner-fine53-posterior-r2.json.gz','3053e9cba77da784dfe3760451530c15a53d0366abda9b082276ec9e749ab9a5')}
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def rd(p):
 with (gzip.open(p,'rt') if str(p).endswith('.gz') else open(p)) as f:return json.load(f)
def ex(v):
 if isinstance(v,list):return F(int(v[0]))*F(2)**int(v[1])
 if 'mantissa' in v:return F(int(v['mantissa']))*F(2)**int(v['binary_exponent'])
 return F(int(v['numerator']),int(v['denominator']))
def ab(v):
 z=ex(v);return arb(z.numerator)/z.denominator
def pack(v):
 if not(v.is_finite() and v>=0):raise ArithmeticError('finite positive bound')
 if v==0:return ['0',0]
 m,e=map(int,v.upper().man_exp());sh=max(0,m.bit_length()-160)
 if sh:m,e=(m+(1<<sh)-1)>>sh,e+sh
 if not arb(m)*arb(2)**e>=v.upper():raise ArithmeticError('outward readout')
 return [str(m),e]
def up(v):return ab(pack(v))
def rat(v):return dict(numerator=str(v.numerator),denominator=str(v.denominator))
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
 if a.out.exists():raise FileExistsError('fresh export')
 ctx.prec,ctx.threads=256,1;start=time.monotonic();g={};d={}
 def gate(k,b):
  if not b:raise ArithmeticError(k)
  g[k]=True
 for k,(p,s) in PINS.items():gate('pin_'+k,sha(p)==s);d[k]=rd(p)
 for k in ('new_resource','comparison_resource'):gate('actual0_'+k,d[k]['exitcode']==0 and d[k]['termination_signal'] is None and d[k]['peak_rss_kib']<98304)
 n,c,o,f=d['new'],d['comparison'],d['old_point'],d['old_field'];gate('same_actual_identified_field',n['all_gates'] and c['all_gates'] and n['new_conditional_nonlow_exists'] and c['lower_width_same_field_identified'] and c['input_identities']['new_existence']['sha256']==PINS['new'][1] and c['input_identities']['old_field']['sha256']==PINS['old_field'][1] and o['all_gates'] and f['all_gates'] and f['only_same_existing_complex_P1_field'])
 gate('same_domain_and_units',n['domain']==c['domain']==o['domain']==f['domain'] and o['same_original617_units']==f['same_original617_units'] and n['windows']==o['windows']==f['windows'] and ex(n['angular_weight_translation'])==F(3,5) and ex(o['angular_weight_translation'])==F(2,5))
 eps=ab(f['point_physical_epsilon_prime']);windows=n['windows'];vals=[];rows=[]
 for w,(lo,hi) in enumerate(windows):
  old=up(ab(o['translated_head_window_masses'][w])*(arb(hi)/5).exp());wide=up(eps*ab(n['rows'][0]['radius'][w]));z=min(old,wide);gate('every_finite_positive_head_'+str(w),z>0 and z<=wide and z<=old);vals.append(z);rows.append(dict(window=[lo,hi],known_finite_point_translated=pack(old),new_full_field_wholecell_readout=pack(wide),chosen=pack(z)))
 h=up(eps*ab(n['infinite_radius']));gate('full_infinite_new_space_repaid',h>0 and n['complete_mean_inverse_Q_T_and_infinite'] and n['unknown_infinite_never_reweighted'])
 head=[up(sum(vals[:46],arb(0))),up(sum(vals[46:],arb(0))),h];oldbands=[];original=[]
 for lo,start0,end0 in [(94,0,46),(186,46,53)]:
  lower=up(sum((z*(-arb(windows[w][0])/5).exp() for w,z in enumerate(vals) if start0<=w<end0),arb(0)));oldbands.append(min(lower,ab(o['translated_head_band_masses'][len(oldbands)])))
  raw=up(sum((z*(-arb(3*windows[w][0])/5).exp() for w,z in enumerate(vals) if start0<=w<end0),arb(0)));original.append(min(raw,ab(o['actual_R100_head_band_masses'][len(original)])))
 oldbands.append(up(h*(-arb(8192)/5).exp()));original.append(min(up(h*(-arb(3*8192)/5).exp()),ab(o['actual_R100_head_band_masses'][2])))
 sigma=ex(o['head_strip']);gate('same_true_node12_readout',o['readout_position'] and eps>0 and n['rows'][0]['cell']==12)
 out=dict(schema='same-P1-shift060-conditional-fullfield-point-head-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),all_gates=all(g.values()),gates=g,gate_count=len(g),input_identities={k:dict(path=str(p),sha256=s) for k,(p,s) in PINS.items()},domain=n['domain'],head_strip=rat(sigma),translated_head_strip=rat(sigma+F(3,5)),angular_weight_translation=rat(F(3,5)),windows=windows,head_bands=o['head_bands'],same_original617_units=o['same_original617_units'],readout_position=o['readout_position'],point_physical_epsilon_prime=pack(eps),translated_head_window_masses=list(map(pack,vals)),translated_head_band_masses=list(map(pack,head)),actual_R100_head_band_masses=list(map(pack,original)),head_at040_band_masses=list(map(pack,oldbands)),rows=rows,shift060_tail_split=dict(cutoff=34816,complete_8192up_at060=pack(h),complete_34816up_at060=pack(h),complete_8192up_at040=pack(oldbands[2]),complete_34816up_at040=pack(up(h*(-arb(34816)/5).exp()))),complete_mean_inverse_far=True,complete_infinite_repaid=True,same_original_full_field_identified=True,finite_old_point_only_reweighted=True,old_infinite_never_reweighted=True,outer_new_width_not_claimed=True,physical_units_not_changed=True,coarse_rest_budget_not_claimed_sufficient=True,precision_bits=256,elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 gate('owned_RSS96MiB',out['peak_rss_kib']<98304);out['gate_count']=len(g);a.out.write_text(json.dumps(out,separators=(',',':'))+'\n');print(json.dumps(dict(all_gates=True,sha256=sha(a.out),head=list(map(str,head)),gate_count=len(g),elapsed_seconds=out['elapsed_seconds'],peak_rss_kib=out['peak_rss_kib'])),flush=True)
if __name__=='__main__':main()
