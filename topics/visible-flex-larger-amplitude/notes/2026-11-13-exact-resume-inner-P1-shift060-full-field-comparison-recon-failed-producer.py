#!/usr/bin/env python3
"""NONCERTIFYING lower-width conditional comparison, same actual LF and far fixed.

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
All numerical existence statements require a separate outward certificate.
No old unknown infinite mass is reweighted. Q preserves window support;
complete T and the true fixed finite-z nonlinear far graph remain.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,gzip,hashlib,json,time,resource,sys
import numpy as np
from flint import arb,ctx
B=Path('/workspace/scratch/d1aa462cfc02');E=B/'exact-work';TOP=B/'math-research/topics/visible-flex-larger-amplitude'
PINS={
 'LF':(E/'inner-actual-LF-shift060-r1.json.gz','ff1df29ff5f24ffd6ed13dbc80c9f4a96d0e3084bacf03ebce41343d2d0ac811'),
 'source':(E/'inner-actual-LF-shift060-source-r1-summary.json','9f9ba881882e14f633a59fbd1111c7fd0ade9657fee36822f14ad8c495052b38'),
 'DQ':(E/'inner-actual-LF-comparison040-DQ-r1/certificate.json.gz','cf71d17144a18b0c4debc2d00d793ba23f19a8e75d18e741997769e890e42d0a'),
 'density':(TOP/'notes/2026-11-12-tail-r42-strong-same-tau-r1-density.json.gz','e640e3e693ca198460de902fc8d9bb1bd909c2a7051ec099aa930a86789e0700'),
 'split':(TOP/'notes/2026-11-12-tail-r42-strong-same-tau-r1-split.json.gz','b31ba4868bf825fe19981af820f92d798161df027519992b9380a4b9f7f6b5dd'),
 'Gamma':(B/'geometry-work/inner-window-gamma-r1/output/certificate.json','3033c330ed219a1e87420818df8dd3d7bca44c246afe4f661d68870a783847b1'),
}
WIN=[[m,m] for m in range(94,185,2)]+[[186,192],[194,256],[258,512],[514,1024],[1026,2048],[2050,4096],[4098,8190]]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
 with (gzip.open(p,'rt') if str(p).endswith('.gz') else open(p)) as f:return json.load(f)
def ab(v):
 if isinstance(v,list):return arb(int(v[0]))*arb(2)**int(v[1])
 if 'upper' in v:return ab(v['upper'])
 if 'mantissa' in v:return arb(int(v['mantissa']))*arb(2)**int(v['binary_exponent'])
 return arb(int(v['numerator']))/int(v['denominator'])
def fl(v):return float(ab(v))
def rss():
 if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>=98304:raise MemoryError('Owned96MiB guard')
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
 if args.out.exists():raise FileExistsError('Fresh output required')
 ctx.prec,ctx.threads=256,1;start=time.monotonic();np.seterr(over='raise',invalid='raise')
 for k,(p,s) in PINS.items():
  if sha(p)!=s:raise ArithmeticError('Pin '+k)
 lf=read(PINS['LF'][0]);src=read(PINS['source'][0]);dq=read(PINS['DQ'][0]);den=read(PINS['density'][0]);gg=read(PINS['Gamma'][0])
 if not all(x['all_gates'] for x in (lf,src,dq)):raise ArithmeticError('Actual inputs required')
 if not(lf['finite_LF_is_actual_projection_of_same_existing_field'] and lf['no_unknown_infinite_reweight'] and dq['input_identities']['modal']['sha256']==PINS['LF'][1] and src['input_hashes'][str(PINS['LF'][0])]==PINS['LF'][1]):raise ArithmeticError('Same actual LF input')
 C=np.array([fl(r['known_Cs_plus_Lambda_common_at040'])+fl(r['known_complete_e_low_common_at040']) for r in lf['rows']]);aa=np.array([fl(r['physical_Amax']) for r in lf['rows']]);tau=np.array([fl(r['translated_tau_outer_lower'])-.2 for r in lf['rows']]);gi=257/256*fl(den['gamma_high'])
 K=np.empty((213,53,54));records=[]
 for i,rec in enumerate(dq['chunk_records']):
  p=Path(rec['path'])
  if sha(p)!=rec['sha256']:raise ArithmeticError('DQ chunk pin')
  row=read(p);K[i]=[[fl(v) for v in row['kernels_s_upper'][w][1:]] for w in range(53)];records.append(rec);del row;rss()
 G=[];groups=[];greg=[]
 for rec in gg['files']:
  p=PINS['Gamma'][0].parent/rec['path']
  if sha(p)!=rec['sha256']:raise ArithmeticError('Gamma chunk pin')
  M=np.zeros((213,213));d=read(p)
  for k,n,m,e in d['entries']:M[k-12,n-12]=fl([m,e])
  G.append(M);groups.append([w for w,(lo,hi) in enumerate(WIN) if rec['first_mode']<=lo<=hi<=rec['last_mode']]);greg.append(dict(path=str(p),sha256=rec['sha256']));del d
 qref=np.zeros((213,53));qhi=np.array([fl(r['source_common_mass']['common_d']['infinite8192up']) for r in src['rows']]);tails=qhi.copy();which={m:w for w,(lo,hi) in enumerate(WIN) for m in range(lo,hi+1,2)}
 for rec in src['source_parts']:
  p=Path(rec['path'])
  if sha(p)!=rec['sha256']:raise ArithmeticError('Complete source pin')
  with gzip.open(p,'rt') as stream:
   for line in stream:
    row=json.loads(line);n=row['cell']-12
    for pair in row['high_polynomial_pair_rows']:qref[n,which[pair['mode']]]+=fl(pair['common_d'])
 qref+=tails[:,None]
 for n,row in enumerate(src['rows']):
  q=row['source_common_mass']['common_d'];qref[n,:46]=np.minimum(qref[n,:46],fl(q['near94to184']));qref[n,46:]=np.minimum(qref[n,46:],fl(q['rest186to8190']))
 sys.path.insert(0,str(TOP/'computations'))
 from closure_split_joint_io_v2 import metadata_without_array
 sp=metadata_without_array(PINS['split'][0],'gamma_rows')
 ratio=ab(lf['fixed_far_parameter']['new_actual_upper'])/(arb(2)**-2200)
 far=np.array([[float(ab(row['far_boundary_near' if w<46 else 'far_boundary_rest'])*ratio**2/(arb(257)/256)) for w in range(53)] for row in sp['cells']]);hfar=float(ab(sp['deep_high_boundary'])*ratio**2/(arb(257)/256))
 # Each membership is exact for even integer windows. In particular equality
 # at a support boundary is retained, and the infinite input is never cut off.
 ms=np.zeros((53,53,53));md=np.zeros_like(ms);mh=np.zeros((53,53));cross=np.zeros((213,53,53))
 decay=np.exp(-2*tau[:,None]*np.array([lo for lo,hi in WIN])[None,:]);decayh=np.exp(-16384*tau)
 for w,(lo,hi) in enumerate(WIN):
  for a,(al,ah) in enumerate(WIN):
   if ah>=8192-hi:cross[:,w,a]=np.exp(-2*max(al,8192-hi)*tau)
   for b,(bl,bh) in enumerate(WIN):
    if max(al+bl,lo)<=min(ah+bh,hi):ms[w,a,b]=5/8
    if a<b and max(bl-ah,lo)<=min(bh-al,hi):md[w,a,b]=5/4
    if a==b and ah-al>=lo:md[w,a,b]=5/4
    if ah+bh>=8192:mh[a,b]=5/8
 def green(s):
  out=np.empty((213,53))
  for M,ix in zip(G,groups):out[:,ix]=M@s[:,ix]
  return out
 def Q(x,h,dx=None,dh=None):
  if dx is None:
   out=np.einsum('na,wab,nb->nw',x,ms,x,optimize=True)+np.einsum('na,wab,nb->nw',x*decay,md,x,optimize=True)
   out+=(5/4)*h*np.einsum('nwa,na->nw',cross,x,optimize=True)+(5/4)*h*h*decayh[:,None]
   high=np.einsum('na,ab,nb->n',x,mh,x,optimize=True)+(23/9)*np.sum(x,axis=1)*h+(23/18)*h*h
  else:
   out=2*np.einsum('na,wab,nb->nw',x,ms,dx,optimize=True)+np.einsum('na,wab,nb->nw',dx*decay,md,x,optimize=True)+np.einsum('na,wab,nb->nw',x*decay,md,dx,optimize=True)
   out+=(5/4)*(h*np.einsum('nwa,na->nw',cross,dx,optimize=True)+dh*np.einsum('nwa,na->nw',cross,x,optimize=True))+(5/2)*h*dh*decayh[:,None]
   high=2*np.einsum('na,ab,nb->n',x,mh,dx,optimize=True)+(23/9)*(np.sum(dx,axis=1)*h+np.sum(x,axis=1)*dh+h*dh)
  return out,high
 def mat(v,d=None):
  x=v[:-1].reshape(213,53);h=v[-1];t=np.sum(x,axis=1)+h
  if d is None:
   sq,hsq=Q(x,h);rem=270*aa*(C+t)*(C*t+t*t/2)
   lin=np.einsum('nwi,ni->nw',K,np.concatenate([x,np.full((213,1),h)],axis=1),optimize=True)
   out=green(qref+lin+sq+rem[:,None])+far
   hout=gi*np.sum(qhi+(23/9)*C*(x[:,-1]+h)+hsq+rem)+hfar
  else:
   dx=d[:-1].reshape(213,53);dh=d[-1];dt=np.sum(dx,axis=1)+dh;sq,hsq=Q(x,h,dx,dh);rem=270*aa*(C*C+3*C*t+1.5*t*t)*dt
   lin=np.einsum('nwi,ni->nw',K,np.concatenate([dx,np.full((213,1),dh)],axis=1),optimize=True)
   out=green(lin+sq+rem[:,None]);hout=gi*np.sum((23/9)*C*(dx[:,-1]+dh)+hsq+rem)
  return np.concatenate([out.ravel(),[hout]])
 def event(phase,it,v):
  x=v[:-1].reshape(213,53);t=x.sum(axis=1)+v[-1];a=dict(phase=phase,iteration=it,max_nonlow=float(max(t)),max_cell=int(np.argmax(t))+12,max_physical=float(max(aa*(C+t))),head94=float(x[0,0]),head184=float(x[0,45]),headrest=float(sum(x[0,46:])),infinite=float(v[-1]),elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss);print(json.dumps(a),flush=True);return a
 oldpath=E/'inner-fine53-posterior-r2.json.gz';newpath=E/'inner-actual-LF-shift060-conditional-recon-r1.json.gz'
 if sha(oldpath)!='3053e9cba77da784dfe3760451530c15a53d0366abda9b082276ec9e749ab9a5' or sha(newpath)!='4fd35e00520ebf07713593c5249f7dae26756e71606ea70c19f4a298f5b18772':raise ArithmeticError('Comparison parent identity')
 old=read(oldpath);new=read(newpath)
 if not old['all_gates'] or not new['candidate_found']:raise ArithmeticError('Known parent and proposed new radius required')
 olds=np.array([[fl(z) for z in row['window_caps']] for row in old['rows']]);oldh=fl(old['complete_infinite_cap'])
 newr=np.array(new['candidate_radius'])*(1048577/1048576);nr=newr[:-1].reshape(213,53)
 drops=np.exp(-.2*np.array([lo for lo,hi in WIN]));r=np.concatenate([np.maximum(olds,nr*drops[None,:]).ravel(),[max(oldh,0.0)]])
 r=np.maximum(r,1e-300);events=[event('comparison_box',0,r)];success=False;distance=None;rate=None
 if np.max(aa*(C+r[:-1].reshape(213,53).sum(axis=1)+r[-1]))>=1/128:raise ArithmeticError('Whole comparison physical domain')
 for q in (.5,.75,.9,.95):
  w=r.copy();converged=False
  for step in range(1,513):
   nw=r+mat(r,w)/q
   if not np.all(np.isfinite(nw)) or np.max(nw/r)>1e100:break
   change=np.max(np.abs(nw-w)/np.maximum(nw,1e-300));w=nw
   if step&(step-1)==0:events.append(dict(phase='distance',q=q,step=step,maximum_ratio=float(np.max(mat(r,w)/w))))
   if change<1e-11:converged=True;break
  if converged:distance=w;rate=float(np.max(mat(r,w)/w));success=rate<1;break
 out=dict(schema='noncertifying-actual-LF-comparison040-conditional-recon-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',certified=False,comparison_identification_claimed=False,candidate_found=success,source_sha256=sha(__file__),input_identities={k:dict(path=str(p),sha256=z) for k,(p,z) in PINS.items()},old_whole_field=dict(path=str(oldpath),sha256=sha(oldpath)),new_radius_proposal=dict(path=str(newpath),sha256=sha(newpath)),domain=lf['domain'],comparison_translation=dict(numerator='2',denominator='5'),windows=WIN,events=events,candidate_radius=r.tolist(),candidate_distance=None if distance is None else distance.tolist(),proposed_distance_ratio=rate,old_infinite_radius=old['complete_infinite_cap'],new_infinite_down_factor_for_final_exact_consumer='exp(-8192/5)',source_and_far_constants_not_used_by_comparison=True,elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 rss();args.out.write_bytes(gzip.compress((json.dumps(out,separators=(',',':'),allow_nan=False)+'\n').encode(),mtime=0));print(json.dumps(dict(path=str(args.out),sha256=sha(args.out),candidate_found=success,proposed_distance_ratio=rate,elapsed_seconds=out['elapsed_seconds'],peak_rss_kib=out['peak_rss_kib'])),flush=True)
 if not success:sys.exit(1)
if __name__=='__main__':main()
