#!/usr/bin/env python3
"""Actual same-field head export in original and newly certified wide strips.
Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
"""
import argparse,gzip,hashlib,json,resource,time
from pathlib import Path
from fractions import Fraction as F
from flint import arb,ctx
BASE=Path('/workspace/scratch/d1aa462cfc02');TOP=BASE/'math-research/topics/visible-flex-larger-amplitude'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes())
def ex(v):
 if isinstance(v,list):return F(int(v[0]))*F(2)**int(v[1])
 if 'upper' in v:return ex(v['upper'])
 if 'mantissa' in v:return F(int(v['mantissa']))*F(2)**int(v['binary_exponent'])
 return F(int(v['numerator']),int(v['denominator']))
def ab(v):
 z=v if isinstance(v,F) else ex(v);return arb(z.numerator)/z.denominator
def pack(z):
 t=z.upper()
 if not(t.is_finite() and t>=0):raise ArithmeticError('Finite positive endpoint mass')
 if t==0:return ['0',0]
 m,e=map(int,t.man_exp());q=max(0,m.bit_length()-160)
 if q:m,e=(m+(1<<q)-1)>>q,e+q
 v=[str(m),e]
 if not ab(v)>=t:raise ArithmeticError('Outward endpoint rounding')
 return v
def rat(v):return dict(numerator=str(v.numerator),denominator=str(v.denominator))
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True);a=p.parse_args();ctx.prec=256;ctx.threads=1;start=time.monotonic()
 if a.out.exists():raise FileExistsError('Fresh same-field head export')
 paths={
  'certificate':(BASE/'exact-work/inner-P1-shift040-641-cert-r1.json.gz','ade2693eeb64007fdde072a855b7e65c3f125ba294793eb7e78975bd9ccc79c0'),
  'certificate_resource':(BASE/'exact-work/inner-P1-shift040-641-cert-run1-resource.json','e2caf4e9019a011f00cb5f0ec0067dd1e13598508a07bbb506656c1b67d5c6c7'),
  'original_point_normalization':(BASE/'exact-work/inner-full641-bootstrap-r1.json.gz','143828de5eeac3148becd09467c6fa5ffb04a70c896d6f09614cd6d64b7b4fd3'),
  'original617_units':(TOP/'notes/2026-11-13-root-r100-source-reweight-r1.json','617987048c3a599acb42bcafe8dba99155c5cde82d252706769d5e24340ce1b9')}
 for k,(path,pin) in paths.items():
  if sha(path)!=pin:raise ArithmeticError('Pinned head normalization '+k)
 cert,usage,old=(read(paths[k][0]) for k in ('certificate','certificate_resource','original_point_normalization'))
 if not(cert['all_gates'] and all(cert['gates'].values()) and cert['new_complete_fixedpoint_proved'] and cert['same_original_full_field_identified'] and usage['exitcode']==0 and usage['termination_signal'] is None):raise ArithmeticError('Same actual complete infinite field must be proved first')
 if not old['all_gates']:raise ArithmeticError('Original actual point Vprime/w normalization')
 delta=ex(cert['angular_weight_translation']);tau=ex(old['head_strip']);eps=ab(old['point_physical_epsilon_prime'])
 bands=[[94,184],[186,8190],[8192,None]];rows=[];wide=[];narrow=[]
 for i,(lo,hi) in zip((213,426,639),bands):
  wh=ab(cert['complete_image'][i])*eps;de=(-lo*ab(delta)).exp();na=wh*de
  if not(wh.is_finite() and na.is_finite() and 0<na<wh):raise ArithmeticError('Complete endpoint and genuine strip descent')
  wide.append(pack(wh));narrow.append(pack(na));rows.append(dict(band=[lo,hi],primary_index=i,whole_cell_image=cert['complete_image'][i],point_Vprime_over_w=old['point_physical_epsilon_prime'],shift_descent_factor=pack(de),translated_endpoint_mass=pack(wh),original_endpoint_mass=pack(na)))
 out=dict(schema='same-R100-P1-new-complete-strip-head-export-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',all_gates=True,
  gates=dict(actual_same_full_field_before_endpoint=True,all_three_full_bands=True,full_infinite_band_no_cutoff=True,actual_point_normalization=True,mean_inverse_far_retained=True,only_downward_strip_transfer=True),
  domain=cert['domain'],actual_R100_head_band_masses=narrow,translated_head_band_masses=wide,head_strip=old['head_strip'],translated_head_strip=rat(tau+delta),angular_weight_translation=cert['angular_weight_translation'],head_bands=bands,
  primary=dict(path=str(paths['certificate'][0]),sha256=paths['certificate'][1]),resource=dict(path=str(paths['certificate_resource'][0]),sha256=paths['certificate_resource'][1]),
  primary_key_paths=['complete_image[213]','complete_image[426]','complete_image[639]'],readout_formula='translated=complete_image[index]*(actual Vprime12(b)/w(b)); original=translated*exp(-physical_band_minimum*2/5)',
  rows=rows,complete_mean_inverse_far=True,complete_infinite_repaid=True,same_original617_units=dict(sha256=paths['original617_units'][1],units='Original R100 balanced physical P/K strong pair head mass at declared head_strip; translated array has the identical physical convention at head_strip+2/5.'),
  input_identities={k:dict(path=str(v[0]),sha256=v[1]) for k,v in paths.items()},source_sha256=sha(__file__),
  scope='Whole-cell-to-actual-point upper readout for the same P1 field. This coarse export does not replace tighter old-width endpoint caps, and does not claim outer11/10 propagation.',
  elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(dict(all_gates=True,path=str(a.out),sha256=sha(a.out),wide=list(map(lambda z:str(ab(z)),wide)),original=list(map(lambda z:str(ab(z)),narrow)),elapsed_seconds=out['elapsed_seconds'],peak_rss_kib=out['peak_rss_kib'])),flush=True)
if __name__=='__main__':main()
