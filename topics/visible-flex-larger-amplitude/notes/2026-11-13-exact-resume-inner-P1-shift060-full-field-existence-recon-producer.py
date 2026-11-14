#!/usr/bin/env python3
"""NONCERTIFYING fine53 conditional-nonlow candidate, actual LF and far fixed.

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
 'DQ':(E/'inner-actual-LF-shift060-DQ-r1/certificate.json.gz','f652efba56708c9b0efe0230a52838abe106967266273a48740c2f09ccbdad18'),
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
 C=np.array([fl(r['finite_LF_common_cap']) for r in lf['rows']]);aa=np.array([fl(r['physical_Amax']) for r in lf['rows']]);tau=np.array([fl(r['translated_tau_outer_lower']) for r in lf['rows']]);gi=257/256*fl(den['gamma_high'])
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
 records_events=[];success=False;reason='not_started';v=np.zeros(11290);r=None;distance=None;proposed_q=None
 try:
  for it in range(1,513):
   nxt=mat(v)
   if not np.all(np.isfinite(nxt)):raise ArithmeticError('Nonfinite candidate image')
   change=np.max(np.abs(nxt-v)/np.maximum(nxt,1e-300));v=nxt
   if it&(it-1)==0:records_events.append(event('zero_iteration',it,v));rss()
   t=v[:-1].reshape(213,53).sum(axis=1)+v[-1]
   if np.max(aa*(C+t))>=1/256:raise ArithmeticError('Candidate physical bound exceeded1/256')
   if it>8 and change<1e-11:break
  margin=np.maximum(v/64,1e-300);r=np.maximum(v,1e-300)
  for inflate in range(1,513):
   nxt=mat(r)+margin;change=np.max(np.abs(nxt-r)/np.maximum(nxt,1e-300));r=nxt
   if inflate&(inflate-1)==0:records_events.append(event('radius_iteration',inflate,r));rss()
   if np.max(aa*(C+r[:-1].reshape(213,53).sum(axis=1)+r[-1]))>=1/256:raise ArithmeticError('Candidate inflated physical bound exceeded1/256')
   if change<1e-12:break
  image_ratio=float(np.max(mat(r)/r))
  for q in (.5,.75,.9,.95):
   z=r.copy();converged=False
   for jj in range(1,513):
    nz=r+mat(r,z)/q
    if not np.all(np.isfinite(nz)) or np.max(nz/np.maximum(r,1e-300))>1e100:break
    change=np.max(np.abs(nz-z)/np.maximum(nz,1e-300));z=nz
    if change<1e-11:converged=True;break
   if converged:
    distance=z;proposed_q=float(np.max(mat(r,z)/z));break
  success=image_ratio<1 and distance is not None and proposed_q<1
  reason='candidate_found' if success else 'radius_or_distance_not_proposed'
 except (FloatingPointError,ArithmeticError,MemoryError) as e:reason=type(e).__name__+': '+str(e)
 final=event('final',0,v);records_events.append(final)
 out=dict(schema='noncertifying-actual-LF-shift060-conditional-nonlow-recon-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',certified=False,new_fixedpoint_claimed=False,reason=reason,candidate_found=success,source_sha256=sha(__file__),input_identities={k:dict(path=str(p),sha256=s) for k,(p,s) in PINS.items()},domain=lf['domain'],angular_weight_translation=lf['angular_weight_translation'],actual_LF_and_far_fixed=True,unknown_infinite_never_reweighted=True,windows=WIN,events=records_events,candidate_radius=None if r is None else r.tolist(),candidate_distance=None if distance is None else distance.tolist(),proposed_image_ratio=None if r is None else (image_ratio if 'image_ratio' in locals() else None),proposed_distance_ratio=proposed_q,initial_constant=mat(np.zeros(11290)).tolist(),Gamma_chunks=greg,DQ_chunks=records,elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 if out['peak_rss_kib']>=98304:out['resource_requirement_met']=False
 else:out['resource_requirement_met']=True
 data=(json.dumps(out,separators=(',',':'),allow_nan=False)+'\n').encode();args.out.write_bytes(gzip.compress(data,mtime=0));print(json.dumps(dict(path=str(args.out),sha256=sha(args.out),candidate_found=success,reason=reason,elapsed_seconds=out['elapsed_seconds'],peak_rss_kib=out['peak_rss_kib'])),flush=True)
 if not success:sys.exit(1)
if __name__=='__main__':main()
