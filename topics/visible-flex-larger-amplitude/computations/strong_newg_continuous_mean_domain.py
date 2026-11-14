#!/usr/bin/env python3
"""Actual full-prefix continuous Frenet domain for the repair homotopy.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Consumes every original physical quintic interval and every actual binary
background piece. Angular boxes cover the entire circle. These are interval
enclosures, not spatial samples. The original aligned exact-real background
and the explicitly C2-repaired comparison, with all saved state repairs,
are enclosed simultaneously. Mean integration, original libm/evaluation
rounding, coordinate alignment and target-g changes remain unpaid.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import json
from math import factorial
from pathlib import Path
import resource
import time
import numpy as np
from flint import arb,ctx

PINS={
 'background':'a3f57c4efdbd5170183cd97ffe4d2828c57c6a2c13c5f603fd1ed144f99db60f',
 'state_repair':'d848f7a1996e7cb620275e86d336faa0d22d84c1e44f5a2ee707c1e29a337dda',
 'radial':'2d4993d9d5735e5acafe563cbec6def27718d5b0764ad182c3588f8fedf2a83d',
 'table':'0a6bb86d0b492ba47ff5d34a4ef63419686aef316cacdec62ed1781f48da621d',
 'background_source':'483b784c9c7aabde360aa04a06eea063b7dee8b1dadd0f0ae81f8be0d7f14e08',
}
NEG=-np.inf;POS=np.inf


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
 p=Path(p);b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)
def dy(z):return F(int(z[0]))*F(2)**int(z[1])
def rat(z):return F(int(z['numerator']),int(z['denominator']))
def binary(z):return F.from_float(float(z))
def aq(q):
 q=F(q);return arb(q.numerator)/q.denominator
def down(x):return np.nextafter(x,NEG)
def up(x):return np.nextafter(x,POS)
def ai(x):return np.array([down(float(x.lower())),up(float(x.upper()))])
def qi(q):return ai(aq(q))
def const(q):
 q=np.asarray(q,dtype=float);return np.array([q,q])
def add(a,b):return np.array([down(a[0]+b[0]),up(a[1]+b[1])])
def neg(a):return np.array([-a[1],-a[0]])
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 vals=np.asarray([a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1]])
 return np.array([down(np.min(vals,axis=0)),up(np.max(vals,axis=0))])
def div(a,b):
 if np.any(b[0]<=0):raise ArithmeticError('Strictly positive divisor required')
 return mul(a,np.array([down(1/b[1]),up(1/b[0])]))
def square(a):
 lo=np.where((a[0]<=0)&(a[1]>=0),0.,np.minimum(a[0]*a[0],a[1]*a[1]))
 return np.array([np.maximum(0,down(lo)),up(np.maximum(a[0]*a[0],a[1]*a[1]))])
def absmax(a):return np.maximum(abs(a[0]),abs(a[1]))
def widen(a,e):return add(a,np.array([-e,e]))
def isum(a):
 """Enclose any IEEE binary64 summation order of the first axis."""
 n=a.shape[1];u=F(1,1<<53);g=F(max(0,n-1))*u/(1-F(max(0,n-1))*u)
 gamma=up(float(g));one_minus=down(1-gamma)
 bounds=[]
 for k in range(2):
  s=np.sum(a[k],axis=0);t=np.sum(abs(a[k]),axis=0)
  T=up(t/one_minus);err=up(gamma*T)
  bounds.append(down(s-err) if k==0 else up(s+err))
 return np.array(bounds)
def dot(coef,angular):return isum(mul(coef[:,:,None],angular))
def horner(coeff,x):
 z=qi(coeff[-1])
 for c in reversed(coeff[:-1]):z=add(mul(z,x),qi(c))
 return z
def sincos_small(x,A):
 if np.any(absmax(x)>1):raise ArithmeticError('Small-angle Taylor range exceeded')
 z=square(x)
 sn=mul(x,horner([F((-1)**j,factorial(2*j+1)) for j in range(7)],z))
 cs=horner([F((-1)**j,factorial(2*j)) for j in range(8)],z)
 return widen(sn,up(float(A**15/factorial(15)))),widen(cs,up(float(A**16/factorial(16))))
def norm2(v):
 out=square(v[0])
 for a in v[1:]:out=add(out,square(a))
 return out
def cross(a,b):return [sub(mul(a[1],b[2]),mul(a[2],b[1])),sub(mul(a[2],b[0]),mul(a[0],b[2])),sub(mul(a[0],b[1]),mul(a[1],b[0]))]


def main():
 p=argparse.ArgumentParser(description=__doc__)
 for name in ('background','state-repair','radial','table','background-source','out'):
  p.add_argument('--'+name,type=Path,required=True)
 p.add_argument('--angular-start',type=int,default=512)
 p.add_argument('--angular-max',type=int,default=8192)
 p.add_argument('--radial-limit',type=int,default=0,help='Explicit partial development run only')
 a=p.parse_args();start=time.monotonic();ctx.prec=256;ctx.threads=1
 if a.out.exists():raise FileExistsError('Fresh continuous domain output required')
 if a.angular_start<128 or a.angular_start&(a.angular_start-1) or a.angular_max<a.angular_start:
  raise ValueError('Ordered powers-of-two angular covers required')
 for k,want in PINS.items():
  if sha(getattr(a,k))!=want:raise ValueError('Frozen actual input changed: '+k)
 bg,state,manifest,table=map(read,(a.background,a.state_repair,a.radial,a.table))
 primary=manifest['input_identity']['primary_sha256'];saved=manifest['input_identity']
 profile=next(r for r in bg['profiles'] if r['accepted_primary_sha256']==primary)
 if not bg['all_gates'] or not state['all_gates'] or state['input_identity']['primary_sha256']!=primary:
  raise ValueError('Complete matching repaired field required')
 if not manifest['finished'] or not manifest['all_original_intervals_covered'] or not manifest['all_radial_state_jets_exactly_enclosed']:
  raise ValueError('Every original quintic interval is required')
 M=manifest['modes'];n=3*M+1;gauge=binary(saved['gauge']);L=binary(saved['meridian_length'])
 if M!=28 or n!=manifest['complete_state_count'] or not gauge>0:raise ValueError('Actual q106 full M28 input required')
 spec=importlib.util.spec_from_file_location('continuous_domain_binary_background',a.background_source)
 helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
 table_nodes=[aq(rat(r['actual_binary_gu'])) for r in table['root_weight_rows']]
 table_weights=[aq(rat(r['actual_normalized_binary_weight'])) for r in table['root_weight_rows']]
 pieces=[]
 for j,row in enumerate(profile['piece_rows']):
  record=profile['comparison_definition']['actual_binary_segments'][row['segment']];seg=record['original_binary_segment']
  s0=binary(record['physical_start_binary']);h=binary(record['physical_end_binary'])-s0;ctorL=binary(seg['length'])
  pp=None;norm=None
  if seg['kind']!='hermite':
   pp=helper.phase_pieces(seg)[row['phase_piece']]
   norm=helper.affine_poly(pp[2],pp[0],pp[1]-pp[0])
  pieces.append(dict(row=row,seg=seg,s0=s0,h=h,L=ctorL,piece=pp,norm=norm,
   left=rat(row['physical_interval'][0]),right=rat(row['physical_interval'][1]),
   a_left=helper.interval(dy(row['left_value_first_second'][0][0]),dy(row['left_value_first_second'][0][1])),
   error0=dy(row['quintic_repair_uniform_C0_C1_C2_upper'][0]),error1=dy(row['quintic_repair_uniform_C0_C1_C2_upper'][1])))
 if pieces[0]['left']!=0 or pieces[-1]['right']!=L or any(x['right']!=y['left'] for x,y in zip(pieces,pieces[1:])):
  raise ValueError('Actual background cover changed')
 def background_box(piece,slo,shi):
  seg=piece['seg'];h=piece['h'];ctorL=piece['L'];u0=(slo-piece['s0'])/h;u1=(shi-piece['s0'])/h
  if seg['kind']=='hermite':
   b=binary(seg['k0'])*ctorL;V=binary(seg['v1']);c=3*V-2*b;d=b-2*V
   poly=[binary(seg['a0']),F(0),ctorL*b/2,ctorL*c/3,ctorL*d/4]
   exact_left=sum((v*u0**k for k,v in enumerate(poly)),F(0))
   exact_right=sum((v*u1**k for k,v in enumerate(poly)),F(0))
   radius=helper.interval(exact_left,exact_right)
   ap=helper.polyeval([F(0),b,c,d],helper.interval(u0,u1))*aq(ctorL/h)
  else:
   lo,hi,_=piece['piece'];span=hi-lo;t0=(u0-lo)/span;t1=(u1-lo)/span
   tt=helper.interval(t0,t1);total=arb(0)
   for node,weight in zip(table_nodes,table_weights):
    total+=weight*tt*helper.polyeval(piece['norm'],tt*node).sin()
   radius=piece['a_left']+aq(ctorL*span)*total
   phase=helper.polyeval(piece['norm'],tt)
   err=dy(piece['row']['Gauss_derivative_comparison_first_second_upper'][0])
   ap=phase.sin()*aq(ctorL/h)+arb(0,aq(err))
  radius=radius+arb(0,aq(piece['error0']));ap=ap+arb(0,aq(piece['error1']))
  return ai(radius),ai(ap)
 # Complete angular boxes of all original frequencies. Never sample endpoints
 # and infer signs in between: Arb evaluates sin/cos on each full interval.
 cache={};qref=[binary(v) for v in saved['chart_reference_coefficients']];freq=saved['chart_reference_frequencies']
 A=sum((abs((1-m*m)*q)/m for q,m in zip(qref,freq)),F(0))
 if not A<1:raise ArithmeticError('Actual small chart phase required')
 def angular(N):
  if N in cache:return cache[N]
  ss=np.empty((2,M,N));cc=ss.copy()
  for j in range(N):
   psi=2*arb.pi()*helper.interval(F(j,N),F(j+1,N))
   for k in range(M):
    arg=(2*k+2)*psi;ss[:,k,j]=ai(arg.sin());cc[:,k,j]=ai(arg.cos())
  q=np.array([qi(q) for q in qref]).T;idx=np.array([m//2-1 for m in freq]);mm=np.array(freq,dtype=float)
  vals=mul(q,const(1-mm*mm));Q=dot(div(vals,const(mm)),ss[:,idx]);qp=dot(vals,cc[:,idx]);qpp=neg(dot(mul(vals,const(mm)),ss[:,idx]))
  cache[N]=(ss,cc,Q,qp,qpp);return cache[N]
 repair=np.array([up(float(dy(r['global_correction_C0_C1_C2'][0]))) for r in state['state_bounds']])
 modes=const(2*np.arange(1,M+1,dtype=float));m2=const((2*np.arange(1,M+1,dtype=float))**2)
 def domain(Y,radius,ap,slo,shi,N):
  sn,cs,Q,qp,qpp=angular(N)
  def weight(s):
   x=s/L;return 1-x**3*(10-15*x+6*x*x)
  b=np.array([qi(weight(shi))[0],qi(weight(slo))[1]])
  omb=sub(const(1),b);phase=mul(b,Q);sphi,cphi=sincos_small(phase,A)
  rho=add(const(1),mul(b,qp));rhoc=add(const(1),qp);rp=mul(b,qpp)
  U=[neg(mul(mul(omb,rho),sphi)),add(mul(mul(omb,rho),cphi),mul(b,rhoc)),np.zeros((2,N))]
  V=[sub(mul(omb,neg(add(mul(square(rho),cphi),mul(rp,sphi)))),mul(b,rhoc)),
     add(mul(omb,sub(mul(rp,cphi),mul(square(rho),sphi))),mul(b,qpp)),np.zeros((2,N))]
  R=Y[:,1:M+1];T=Y[:,M+1:2*M+1];Z=Y[:,2*M+1:];R0=Y[:,0]
  du=[neg(dot(add(mul(modes,R),T),sn)),add(R0[:,None],dot(add(R,mul(modes,T)),cs)),neg(dot(mul(modes,Z),sn))]
  dv=[neg(add(R0[:,None],dot(add(mul(add(m2,const(1)),R),mul(const(2),mul(modes,T))),cs))),
      neg(dot(add(mul(add(m2,const(1)),T),mul(const(2),mul(modes,R))),sn)),neg(dot(mul(m2,Z),cs))]
  factor=div(qi(gauge),radius)
  U=[add(u,mul(factor,d)) for u,d in zip(U,du)];V=[add(v,mul(factor,d)) for v,d in zip(V,dv)]
  P=norm2(U);W=norm2(cross(U,V));D=sub(W,mul(square(ap),mul(square(P),P)))
  positive=min(float(radius[0]),float(np.min(rho[0])),float(np.min(P[0])),float(np.min(W[0])),float(np.min(D[0])))>0
  margin=div(D,W) if np.all(W[0]>0) else np.array([np.full(N,-np.inf),np.full(N,np.inf)])
  return positive,dict(radius_lower=float(radius[0]),speed_absolute_upper=float(absmax(ap)),
   chart_rho_lower=float(np.min(rho[0])),normalized_P_lower=float(np.min(P[0])),normalized_P_upper=float(np.max(P[1])),
   normalized_W_lower=float(np.min(W[0])),normalized_W_upper=float(np.max(W[1])),normalized_D_lower=float(np.min(D[0])),
   normalized_D_upper=float(np.max(D[1])),frenet_margin_lower=float(np.min(margin[0])),
   normalized_u_absolute_upper=[float(np.max(absmax(z))) for z in U],normalized_v_absolute_upper=[float(np.max(absmax(z))) for z in V])
 rows=[];failures=[];intervals=0;atoms=0;cursor=F(0);piece_index=0;inputids={str(getattr(a,k)):sha(getattr(a,k)) for k in PINS}
 for chunk in manifest['radial_chunks']:
  path=Path(chunk['path'])
  if sha(path)!=chunk['sha256']:raise ValueError('Original radial chunk changed')
  data=read(path);inputids[str(path)]=sha(path)
  if data['input_identity_sha256']!=manifest['input_identity_sha256']:raise ValueError('Radial identity changed')
  for row in data['rows']:
   if a.radial_limit and intervals>=a.radial_limit:break
   if row['original_interval']!=intervals:raise ArithmeticError('Original interval omitted')
   s0,s1=map(F,row['s_interval'])
   if s0!=cursor:raise ArithmeticError('Physical cover has a gap')
   Y=np.array([[down(float(dy(z[0]))),up(float(dy(z[1])))] for z in row['state_jet_intervals'][0]]).T
   if Y.shape!=(2,n):raise ValueError('Incomplete original states')
   Y=widen(Y,repair);left=s0
   while left<s1:
    while pieces[piece_index]['right']<=left:piece_index+=1
    piece=pieces[piece_index];right=min(s1,piece['right'])
    if not piece['left']<=left<right<=piece['right']:raise ArithmeticError('Background/state interface coverage')
    radius,ap=background_box(piece,left,right);N=a.angular_start
    while True:
     passed,bounds=domain(Y,radius,ap,left,right,N)
     if passed or N>=a.angular_max:break
     N*=2
    item=dict(original_interval=intervals,background_piece=piece_index,s_interval=[str(left),str(right)],
     angular_intervals=N,whole_radial_angular_and_repair_homotopy_enclosed=True,positive_domain=passed,**bounds)
    rows.append(item);atoms+=1
    if not passed:failures.append(item)
    left=right
   intervals+=1;cursor=s1
   if intervals%64==0:print(json.dumps({'event':'continuous_mean_domain_rows','complete_original_intervals':intervals,'atoms':atoms,'failed_atoms':len(failures),'angular_covers_precomputed':sorted(cache),'rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}),flush=True)
  if a.radial_limit and intervals>=a.radial_limit:break
 complete=intervals==manifest['original_physical_intervals'] and cursor==L
 if not a.radial_limit and not complete:raise ArithmeticError('Complete original field was not consumed')
 out=dict(schema='actual-complete-prefix-repair-homotopy-Frenet-domain-v1',scope=__doc__,
  author='geometry_audit (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),input_sha256=inputids,
  primary_sha256=primary,background_comparison_definition_sha256=profile['comparison_definition_sha256'],
  state_comparison_definition_sha256=state['comparison_field_definition_sha256'],
  all_domain_gates=complete and not failures,complete_original_interval_cover=complete,original_intervals=intervals,
  continuous_product_atoms=atoms,failed_atoms=len(failures),rows=rows,
  normalized_definitions={'u':'X_psi/a','v':'X_psipsi/a','P':'|u|^2','W':'|u cross v|^2','D':'W-a_s^2 P^3','original_frenet_margin':'D/W'},
  interval_arithmetic='Binary64 nextafter elementary enclosures; summation gamma_(n-1) with outward absolute-mass bound; Arb256 exact-input angular and background intervals; exact Taylor remainders for sin/cos of small chart phase.',
  all_full_state_radial_suprema_used_before_angle_enclosure=True,
  mean_value_derivatives_quadrature_floating_evaluator_and_alignment_certified=False,
  original_g_or_accepted_candidate_modified=False,new_ODE_Node_Newton_or_spatial_sampling_calls=0,
  elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 a.out.parent.mkdir(parents=True,exist_ok=True);payload=(json.dumps(out,separators=(',',':'))+'\n').encode()
 if a.out.suffix=='.gz':
  with a.out.open('wb') as f:
   with gzip.GzipFile(filename='',mode='wb',fileobj=f,mtime=0) as g:g.write(payload)
 else:a.out.write_bytes(payload)
 print(json.dumps({'event':'continuous_mean_domain_finished','path':str(a.out),'sha256':sha(a.out),'all_domain_gates':out['all_domain_gates'],'intervals':intervals,'failed_atoms':len(failures),'elapsed_seconds':out['elapsed_seconds'],'peak_rss_kib':out['peak_rss_kib']}),flush=True)


if __name__=='__main__':main()
