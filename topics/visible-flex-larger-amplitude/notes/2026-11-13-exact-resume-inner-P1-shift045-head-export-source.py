#!/usr/bin/env python3
"""Actual45-to40 strip descent, including the complete34816-up head tail.
Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
"""
import argparse,gzip,hashlib,json,resource,time
from pathlib import Path
from fractions import Fraction as F
from flint import arb,ctx
BASE=Path('/workspace/scratch/d1aa462cfc02');E=BASE/'exact-work'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes())
def ex(v):
 if isinstance(v,F):return v
 if isinstance(v,list):return F(int(v[0]))*F(2)**int(v[1])
 if 'upper' in v:return ex(v['upper'])
 if 'mantissa' in v:return F(int(v['mantissa']))*F(2)**int(v['binary_exponent'])
 return F(int(v['numerator']),int(v['denominator']))
def ab(v):
 v=ex(v);return arb(v.numerator)/v.denominator
def pack(z):
 t=z.upper()
 if not(t.is_finite() and t>=0):raise ArithmeticError('Finite nonnegative complete head cap')
 if t==0:return ['0',0]
 m,e=map(int,t.man_exp());q=max(0,m.bit_length()-160)
 if q:m,e=(m+(1<<q)-1)>>q,e+q
 x=[str(m),e]
 if not ab(x)>=t:raise ArithmeticError('Exact outward head descent')
 return x
def up(z):return ab(pack(z))
def rat(v):return dict(numerator=str(v.numerator),denominator=str(v.denominator))
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True);a=p.parse_args();ctx.prec=256;ctx.threads=1;start=time.monotonic()
 if a.out.exists():raise FileExistsError('Fresh actual head readout')
 paths={
 'certificate':(E/'inner-P1-shift045-641-cert-r1.json.gz','c0803d2c3752a567fa1719b3eb8393cdbea54e4dc177bf379f560ca8422fef5a'),
 'certificate_resource':(E/'inner-P1-shift045-641-cert-run1-resource.json','e22e2c33e7feb1f88a3ede05d30b03d0c29d803b7dfa80bab1d21f52933c360e'),
 'head040':(E/'inner-P1-shift040-head-export-r1.json','b07f5da957fae36f1edf5a083552e4e78dd45d459488a880fb3eb10d24ba115e'),
 'head040_resource':(E/'inner-P1-shift040-head-export-run1-resource.json','812c87cb9bfa5771cb7a812a3fa5069e3490e7f2dbb6da724f51f871274ea699'),
 'original_point':(E/'inner-full641-bootstrap-r1.json.gz','143828de5eeac3148becd09467c6fa5ffb04a70c896d6f09614cd6d64b7b4fd3')}
 for path,pin in paths.values():
  if sha(path)!=pin:raise ArithmeticError('Immutable same-field head input')
 cert,usage,old,ou,norm=(read(paths[k][0]) for k in ('certificate','certificate_resource','head040','head040_resource','original_point'))
 if not(cert['all_gates'] and all(cert['gates'].values()) and cert['same_original_full_field_identified'] and cert['new_complete_fixedpoint_proved'] and old['all_gates'] and cert['domain']==old['domain']):raise ArithmeticError('Both widths have the same actual complete field')
 if not(all(u['exitcode']==0 and u['termination_signal'] is None for u in (usage,ou)) and ex(cert['angular_weight_translation'])==F(9,20) and ex(old['angular_weight_translation'])==F(2,5)):raise ArithmeticError('Actual45 and40 completed inputs')
 tau=ex(norm['head_strip']);eps=ab(norm['point_physical_epsilon_prime']);rows=[];wide=[];target=[];narrow=[]
 for k,idx in enumerate((213,426,639)):
  lo,hi=norm['head_bands'][k];hw=up(ab(cert['complete_image'][idx])*eps);direct=up(hw*(-lo*arb(1)/20).exp());at40=min(direct,ab(old['translated_head_band_masses'][k]));at0=min(up(hw*(-lo*arb(9)/20).exp()),ab(old['actual_R100_head_band_masses'][k]))
  if not(hw>0 and at40>0 and at0>0 and all(z.is_finite() for z in (hw,at40,at0))):raise ArithmeticError('No dropped complete band')
  wide.append(pack(hw));target.append(pack(at40));narrow.append(pack(at0));rows.append(dict(band=[lo,hi],primary_index=idx,wide045=pack(hw),direct045to040=pack(direct),old040=old['translated_head_band_masses'][k],intersection040=pack(at40),original_strip=pack(at0)))
 fullhigh=ab(wide[2]);midhigh=up(fullhigh*(-8192*arb(1)/20).exp());high=up(fullhigh*(-34816*arb(1)/20).exp())
 if not(0<high<midhigh<fullhigh):raise ArithmeticError('Strict full infinite descent at physical support minima')
 obj=dict(schema='same-R100-P1-complete045-to040-head-and-infinite-export-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',all_gates=True,
  gates=dict(same_original_field_uniform_P1=True,actual_new045_full641_proved=True,only_downward_new_strip_transfer=True,complete_mean_inverse_far_retained=True,all_m_ge34816_no_truncation=True,same_actual_point_epsilon_prime=True),
  domain=cert['domain'],head_bands=norm['head_bands'],head_strip=norm['head_strip'],actual_R100_head_band_masses=narrow,
  translated_head_strip=rat(tau+F(2,5)),translated_head_band_masses=target,certified_wider_head_strip=rat(tau+F(9,20)),certified_wider_head_band_masses=wide,
  shift040_tail_split=dict(physical_mode_bands=[[8192,34814],[34816,None]],upper_masses=[pack(midhigh),pack(high)],
    original_parent_band=[8192,None],parent_shared_mass_at045=wide[2],parent_shared_mass_at040=target[2],
    meaning='Each projection obeys its displayed descent. The same full8192-up parent mass remains shared; the two projections are not independent data.'),
  rows=rows,primary=dict(path=str(paths['certificate'][0]),sha256=paths['certificate'][1]),resource=dict(path=str(paths['certificate_resource'][0]),sha256=paths['certificate_resource'][1]),
  primary_key_paths=['complete_image[213]','complete_image[426]','complete_image[639]'],point_physical_epsilon_prime=norm['point_physical_epsilon_prime'],
  complete_mean_inverse_far=True,complete_infinite_repaid=True,same_original617_units=old['same_original617_units'],
  input_identities={k:dict(path=str(v[0]),sha256=v[1]) for k,v in paths.items()},source_sha256=sha(__file__),
  scope='Same P1 inner field. New45 norm is independently proved; outputs descend to40 or0. No outer11/10 transfer is assumed.',
  elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 a.out.write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(dict(all_gates=True,path=str(a.out),sha256=sha(a.out),head040=list(map(lambda x:str(ab(x)),target)),infinite34816_at040=str(high),finite8192to34814_at040=str(midhigh),elapsed_seconds=obj['elapsed_seconds'],peak_rss_kib=obj['peak_rss_kib'])),flush=True)
if __name__=='__main__':main()
