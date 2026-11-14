#!/usr/bin/env python3
"""Noncertifying P1 positive-map reconnaissance for a new strip space.

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Float output chooses candidates only. All strict claims need a new actual
outward consumer; this script never imports a pre-existing infinite cap.
"""
import argparse,gzip,hashlib,json,resource,sys,time
from pathlib import Path
import numpy as np
from flint import arb,ctx
BASE=Path('/workspace/scratch/d1aa462cfc02');TOP=BASE/'math-research/topics/visible-flex-larger-amplitude'
def read(p):
 with (gzip.open(p,'rt') if str(p).endswith('.gz') else open(p)) as f:return json.load(f)
def ab(v):
 if isinstance(v,list):return arb(int(v[0]))*arb(2)**int(v[1])
 if 'upper' in v:return ab(v['upper'])
 if 'mantissa' in v:return arb(int(v['mantissa']))*arb(2)**int(v['binary_exponent'])
 return arb(int(v['numerator']))/int(v['denominator'])
def fl(v):return float(ab(v))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out-prefix',type=Path,required=True);args=p.parse_args()
 ctx.prec=256;ctx.threads=1;start=time.monotonic();sys.path.insert(0,str(TOP/'computations'))
 from closure_split_joint_io_v2 import read_field,iter_array,metadata_without_array
 modalpath=BASE/'exact-work/inner-P1-shift040-modal-r1.json.gz';sourcepath=BASE/'exact-work/inner-P1-shift040-source-r1-summary.json'
 modal,source=read(modalpath),read(sourcepath)
 if not(modal['all_gates'] and source['all_gates']):raise ArithmeticError('Actual finite inputs required')
 density=read(TOP/'notes/2026-11-12-tail-r42-strong-same-tau-r1-density.json.gz')
 lp=TOP/'notes/2026-11-12-closure-strong-same-tau-four-green-r1.json.gz'
 sp=TOP/'notes/2026-11-12-tail-r42-strong-same-tau-r1-split.json.gz';split=metadata_without_array(sp,'gamma_rows')
 jp=TOP/'notes/2026-11-12-closure-strong-parameter-jacobian-r1.json.gz';jm=metadata_without_array(jp,'rows')
 W=np.array([fl(v) for v in jm['metric_weights']]);S=257/256;Z=arb(2)**-2200;ratio=2.**40
 C=np.array([fl(r['Cs_common_cap']) for r in modal['rows']]);L=np.array([fl(r['Lambda_common_cap_on_domain']) for r in modal['rows']]);B=np.array([fl(r['Cs_plus_Lambda_common_cap']) for r in modal['rows']]);aa=np.array([S*fl(r['V_over_w_upper']) for r in density['rows']])
 gl=np.array([[S*fl(v) for v in row] for row in read_field(lp,'base')]);gf=np.array([float(S*S*ab(v)/Z) for v in read_field(lp,'far_z_source_upper')['base']])
 gh={g:np.zeros((213,213)) for g in ('near','rest')}
 for k,row in enumerate(iter_array(sp,'gamma_rows')):
  for n,r in enumerate(row['sources'],k):
   for g in gh:gh[g][k,n]=S*fl(r[g+'_gamma'])
 gi=S*fl(density['gamma_high']);fb=np.zeros(641);fd=np.zeros(641)
 for g,off in [('near',213),('rest',426)]:
  for n,r in enumerate(split['cells']):
   f=fl(r['far_boundary_'+g])/S;fb[off+n]=f*ratio**2;fd[off+n]=4*f*ratio
 f=fl(split['deep_high_boundary'])/S;fb[639]=f*ratio**2;fd[639]=4*f*ratio
 for row in iter_array(jp,'rows'):
  i=row['index']
  if i<213 or i==640:
   z=next((ab([m,e]) for j,m,e in row['coefficients'] if j==640),arb(0))
   # Jbar already contains W similarity. Changing only far derivative,
   # target V'=S Vs divides field rows by S; far target is unchanged.
   fd[i]=float(z*ab(jm['metric_weights'][i])/ab(jm['metric_weights'][640])*ratio/(S if i<213 else 1))
 q={g:np.array([fl(r['source_common_mass']['common_d'][band]) for r in source['rows']]) for g,band in [('near','near94to184'),('rest','rest186to8190'),('infinite','infinite8192up')]}
 pure=np.zeros(641)
 pure[213:426]=gh['near']@q['near'];pure[426:639]=gh['rest']@q['rest'];pure[639]=gi*sum(q['infinite']);pure[640]=float(ab(modal['far_common_on_domain'])/Z)
 def mapv(v):
  lo,ne,re,hi=v[:213],v[213:426],v[426:639],v[639]
  t=lo+ne+re+hi;var=L+t
  sl=(23/9)*C*(L+lo+ne)+(23/18)*var*var+270*aa*(C+var)*(C*var+var*var/2)
  sq=(23/18)*t*t;tt=270*aa*(B+t)*(B*t+t*t/2)
  h={'near':(23/9)*B*(lo+ne+re)+sq+tt,'rest':(23/9)*B*(ne+re+hi)+sq+tt,'infinite':(23/9)*B*(re+hi)+sq+tt}
  out=pure+fb
  out[:213]=gl@sl+fd[:213]*v[640]
  out[213:426]+=gh['near']@h['near'];out[426:639]+=gh['rest']@h['rest'];out[639]+=gi*sum(h['infinite'])
  out[640]+=gf@sl+fd[640]*v[640]
  return out
 def jmul(v,w):
  lo,ne,re,hi=v[:213],v[213:426],v[426:639],v[639];t=lo+ne+re+hi;var=L+t
  d=w[:213]+w[213:426]+w[426:639]+w[639]
  dl=(23/9)*C*(w[:213]+w[213:426])+(23/9)*var*d+270*aa*(C*C+3*C*var+1.5*var*var)*d
  rem=(23/9)*t*d+270*aa*(B*B+3*B*t+1.5*t*t)*d
  out=fd*w[640]
  out[:213]+=gl@dl;out[640]+=gf@dl
  out[213:426]+=gh['near']@((23/9)*B*(w[:213]+w[213:426]+w[426:639])+rem)
  out[426:639]+=gh['rest']@((23/9)*B*(w[213:426]+w[426:639]+w[639])+rem)
  out[639]+=gi*sum((23/9)*B*(w[426:639]+w[639])+rem)
  return out
 v=np.zeros(641);events=[]
 for it in range(1,2001):
  nxt=mapv(v);t=nxt[:213]+nxt[213:426]+nxt[426:639]+nxt[639]
  if it&(it-1)==0 or it==2000:
   ev=dict(step=it,max_t=float(max(t)),max_t_cell=int(np.argmax(t))+12,far_scaled=float(nxt[640]),head_near=float(nxt[213]),head_rest=float(nxt[426]),high=float(nxt[639]),relative_change=float(max(np.abs(nxt-v)/np.maximum(nxt,1e-300))))
   print(json.dumps(ev),flush=True);events.append(ev)
  v=nxt
  if not np.isfinite(v).all() or max(t)>1e-5:break
  if it>10 and max(np.abs(mapv(v)-v)/np.maximum(v,1e-300))<1e-12:break
 r=2*v;z=W.copy();specr=[]
 for it2 in range(1,201):
  zz=jmul(r,z);ratios=zz/np.maximum(z,1e-300);scale=max(zz/W)
  if not np.isfinite(scale) or scale<=0:break
  z=zz/scale
  if it2 in (1,2,4,8,16,32,64,128,200):specr.append(dict(step=it2,maximum_ratio=float(max(ratios)),minimum_ratio=float(min(ratios)),scale=float(scale)))
 out=dict(schema='noncertifying-new-shifted641-recon-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),certified=False,new_fixedpoint_claimed=False,
   input_sha256={str(p):sha(p) for p in (modalpath,sourcepath)},events=events,steps=it,spectral_iteration=specr,
   candidate_radius=r.tolist(),candidate_distance_weight=z.tolist(),max_new_error=float(max(r[:213]+r[213:426]+r[426:639]+r[639])),
   elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 path=Path(str(args.out_prefix)+'.json');path.write_text(json.dumps(out,separators=(',',':'))+'\n');print(json.dumps({k:out[k] for k in ('steps','spectral_iteration','max_new_error','elapsed_seconds','peak_rss_kib')}),flush=True)
if __name__=='__main__':main()
