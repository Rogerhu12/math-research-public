#!/usr/bin/env python3
"""R150 S=0,h=k,2lambda^2=1: original full nine conditions on both roots.
A polynomial scaled Gram matrix avoids every artificial norm denominator.
Use the already closed S=Af=0,L!=0 layer; never invert a P1 coefficient.
"""
import argparse,hashlib,itertools,json,os,resource,signal,time
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpq_mpoly_ctx
started=time.perf_counter()
ap=argparse.ArgumentParser()
ap.add_argument('--seconds',type=int,default=int(os.environ.get('ISP_S0_SECONDS','1200')))
args=ap.parse_args()
def say(o):
 o['elapsedSeconds']=round(time.perf_counter()-started,6)
 print(json.dumps(o,sort_keys=True),flush=True)
def alarm_handler(signum,frame):
 say({'status':'timeout_unknown','claimExcluded':False})
 raise SystemExit(124)
signal.signal(signal.SIGALRM,alarm_handler);signal.alarm(args.seconds)
source_sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
ctx=fmpq_mpoly_ctx.get(('b','q'),'lex')
bp,qp=ctx.gens();zz=ctx.constant(0);oo=ctx.constant(1)
def poly(v):return v if hasattr(v,'to_dict') else ctx.constant(v)
def profile(v):
 dd=v.to_dict()
 return {'degrees':[max((int(m[i]) for m in dd),default=-1) for i in range(2)],'terms':len(dd)}
# A complete moment cover, with no division by l or by the mean.
xx=fmpq_poly([0,1]);av=2*xx*xx-2*xx+1;vv=xx-fmpq(1,2)
lambda_cover=(2*xx-1)*(2*xx*xx-1)
assert 4*xx**3-3*xx+2-av*(vv+2)==lambda_cover/2
assert lambda_cover.gcd(vv-1).degree()==0
say({'stage':'complete_original_equal_value_moment_cover_verified','lambdaPolynomial':str(lambda_cover),'completeThreeRootMomentCoverVerified':True,'lambdaHalfSeparatelyClosed':True,'claimExcluded':False})
def run_case(case):
 delta=0 if case=='lambda_half' else 2
 class E:
  def __init__(self,a0=0,b0=0):
   if isinstance(a0,E):self.a=a0.a;self.b=a0.b;return
   self.a=poly(a0);self.b=poly(b0)
  def __bool__(self):return bool(self.a) or bool(self.b)
  def __add__(self,o):o=E(o);return E(self.a+o.a,self.b+o.b)
  __radd__=__add__
  def __neg__(self):return E(-self.a,-self.b)
  def __sub__(self,o):return self+-E(o)
  def __rsub__(self,o):return E(o)+-self
  def __mul__(self,o):o=E(o);return E(self.a*o.a+delta*self.b*o.b,self.a*o.b+self.b*o.a)
  __rmul__=__mul__
  def __pow__(self,n):
   out=E(1);v=self
   while n:
    if n&1:out=out*v
    v=v*v;n//=2
   return out
  def __eq__(self,o):o=E(o);return self.a==o.a and self.b==o.b
  def conj(self):return E(self.a,-self.b)
  def norm(self):return self.a*self.a-delta*self.b*self.b
 half=fmpq(1,2)
 if case=='lambda_half':
  lam=E(half);l=E(half);w=E();h=E()
 else:
  lam=E(0,half);l=8*(5+lam)*fmpq(1,49);w=(3*lam+1)*fmpq(1,7);h=lam-half
  assert 2*lam*lam==1
 b=E(bp);c=l-b;a=1-l;p=E(1);q=E(qp);k=h
 assert 2*h+1==2*lam
 assert a+w+l*h==lam
 assert a+2*w+l*h*h==2*lam*lam
 assert a+3*w+l*h**3==4*lam**3
 assert h!=1
 u=b+c*q;V2=b+c*q*q;P02=b+c*q**3-3*u*V2+2*u**3
 D=2*b*c*q*(q-1)
 class P:
  def __init__(self,co=None):self.co={ij:E(v) for ij,v in (co or {}).items() if E(v)}
  def __bool__(self):return bool(self.co)
  def __add__(self,o):
   if not isinstance(o,P):o=cp(o)
   dd=dict(self.co)
   for ij,v in o.co.items():dd[ij]=dd.get(ij,E())+v
   return P(dd)
  __radd__=__add__
  def __neg__(self):return P({ij:-v for ij,v in self.co.items()})
  def __sub__(self,o):return self+-o
  def __rsub__(self,o):return cp(o)+-self
  def __mul__(self,o):
   if not isinstance(o,P):return scale(E(o),self)
   dd={}
   for ij,v in self.co.items():
    for kl,vv in o.co.items():
     key=(ij[0]+kl[0],ij[1]+kl[1]);dd[key]=dd.get(key,E())+v*vv
   return P(dd)
  __rmul__=__mul__
  def __pow__(self,n):
   out=cp(1)
   for _ in range(n):out=out*self
   return out
 def cp(v):return P({(0,0):E(v)})
 def scale(v,pp):return P({ij:E(v)*vv for ij,vv in pp.co.items()})
 fp=P({(1,0):E(1)});tp=P({(0,1):E(1)});zero=P()
 one=[cp(1),zero,cp(1),cp(1)]
 def va(v,z0):return [x+y for x,y in zip(v,z0)]
 def vs(v0,v):return [v0*x for x in v]
 def vm(v,z0):return [v[0]*z0[0],v[0]*z0[1]+v[1]*z0[0],v[2]*z0[2],v[3]*z0[3]]
 def tau(v):return scale(a,v[0])+v[1]+scale(b,v[2])+scale(c,v[3])
 T0=V2-2*u*u
 W1=cp(T0*half)+scale(2*u,fp)
 W2=cp(u*T0+lam*P02)+scale(V2+2*u*u,fp)-scale(b*c*q,tp)
 # D*X and D*Y, with D=2bcq(q-1), are polynomial identities.
 Xhat=scale(2*c*q,scale(q,W1)-W2)
 Yhat=scale(2*b,W2-W1)
 rhat=Xhat-cp(D*a)-scale(D*c,tp)
 shat=Yhat-cp(D*a*q)-scale(D*b,tp)
 Ahat=scale(2*D,fp)-scale(2*b,Xhat)-scale(2*c,Yhat)+scale(2*D*b*c,tp)
 rows=[[zero,zero,cp(D),cp(D*q)],[zero,Ahat,rhat,shat],[cp(D),rhat,zero,scale(D,tp)],[cp(D*q),shat,scale(D,tp),zero]]
 def DK(v):return [tau(vm(row,v)) for row in rows]
 d=DK(one);F2=tau(d);DKd=DK(d);dd=vm(d,d)
 assert not (F2-scale(2*D,fp))
 def P2(v):
  cen=va(v,vs(-tau(v),one))
  return tau(vm(vm(cen,cen),cen))
 def N4(v):
  return scale(E(2),tau(vm(d,vm(v,v))))-F2*tau(vm(v,v))-scale(E(4),tau(v)*tau(vm(d,v)))+scale(E(2),F2*tau(v)**2)+tau(vm(v,DK(v)))
 def Pjet2(v,z0):
  v0=va(v,vs(-tau(v),one));z1=va(z0,vs(-tau(z0),one))
  return scale(E(3),tau(vm(vm(v0,v0),z1)))
 def Njet4(v,z0):return N4(va(v,z0))-N4(v)-N4(z0)
 def mean(jj):
  ev=scale(E(2),tau(vm(rows[0],rows[1]))) if jj==1 else tau(vm(rows[jj],rows[jj]))
  return ev-scale(E(2),DKd[jj])-scale(E(2),dd[jj])+scale(E(2),F2*d[jj])
 scaledP02=D**3*P02
 assert not mean(0) and not (P2(rows[0])-cp(scaledP02))
 assert not (N4(rows[0])-cp(2*lam*scaledP02))
 VV=[cp(1),cp(w),cp(h),cp(k)]
 assert not P2(VV)
 NV=N4(VV)
 assert set(NV.co).issubset({(1,0),(0,0)})
 raw=[mean(1),mean(2),mean(3),Pjet2(rows[0],rows[1])-cp(3*w*scaledP02),P2(rows[2])-cp(h**3*scaledP02),P2(rows[3])-cp(k**3*scaledP02),Njet4(rows[0],rows[1])-cp(4*lam*w*scaledP02),N4(rows[2])-cp(2*lam*h*h*scaledP02),N4(rows[3])-cp(2*lam*k*k*scaledP02)]
 names=['E1','EB','EC','P1','PB','PC','N1','NB','NC']
 hh=hashlib.sha256()
 for name,po in zip(names+['NV'],raw+[NV]):
  for ij,v in sorted(po.co.items()):
   hh.update((name+str(ij)+str(sorted(v.a.to_dict().items()))+'/'+str(sorted(v.b.to_dict().items()))+'\n').encode())
 inputsha=hh.hexdigest()
 say({'stage':'full_original_scaled_Gram_nine_and_Nvalue_generated','case':case,'sourceSha256':source_sha,'inputSha256':inputsha,'ftDegrees':[max((sum(ij) for ij in po.co),default=-1) for po in raw],'allPhysicalParameterConjugatesRetained':True,'claimExcluded':False})
 # Exact division by an actual original nonzero E-polynomial. Its norm is used
 # only to compute a polynomial quotient, NEVER assumed nonzero at a point.
 quotient_checks=0
 def exact_div(v,atom,norm):
  nonlocal quotient_checks
  na=v.a*atom.a-delta*v.b*atom.b
  nb=v.b*atom.a-v.a*atom.b
  gg=norm.gcd(na).gcd(nb)
  if gg.total_degree()!=norm.total_degree():return None
  out=E(na/norm,nb/norm)
  assert out*atom==v
  quotient_checks+=1
  return out
 atomdata=[]
 for label,v in [('b',b),('c',c),('q',q),('q-1',q-1),('q+1',q+1)]:
  atomdata.append((label,v,v.norm()))
 def strip_coefficients(vv):
  vv=list(vv)
  for label,atom,norm in atomdata:
   if norm.total_degree()==0:continue
   while any(vv):
    out=[exact_div(v,atom,norm) for v in vv]
    if any(v is None for v in out):break
    vv=out
  return vv
 nvline=strip_coefficients([NV.co.get((1,0),E()),NV.co.get((0,0),E())])
 Af,Cf=nvline
 assert Af
 # L=(q-1)(h-1) is nonzero on both complete collision fibers.
 # The entire S=Af=0,L!=0 layer is already closed (51d84b503698...).
 # Thus the actual NV f coefficient is a paid unit; no norm is paid.
 atomdata.append(('actual_NV_f_coefficient',Af,Af.norm()))
 clear_cache={}
 def get_poly(index):
  if index in clear_cache:return clear_cache[index]
  po=raw[index]
  m=max((ij[0] for ij in po.co),default=0)
  nt=max((ij[1] for ij in po.co),default=-1)
  out=[E() for _ in range(nt+1)]
  for (i,j0),v in po.co.items():out[j0]=out[j0]+v*((-Cf)**i)*(Af**(m-i))
  out=strip_coefficients(out)
  while out and not out[-1]:out.pop()
  clear_cache[index]=out
  say({'stage':'original_f_replacement_without_norm_inversion','case':case,'name':names[index],'tDegree':len(out)-1,'coefficientProfiles':[{'even':profile(v.a),'odd':profile(v.b)} for v in out],'claimExcluded':False})
  return out
 # Verify the substituted original NV exactly, with its own f-degree one.
 assert NV.co.get((1,0),E())*(-Cf)+NV.co.get((0,0),E())*Af==0
 def determinant(mm):
  n=len(mm)
  if n==0:return E(1)
  if n==1:return mm[0][0]
  out=E()
  for j0 in range(n):
   if mm[0][j0]:out=out+((-1)**j0)*mm[0][j0]*determinant([row[:j0]+row[j0+1:] for row in mm[1:]])
  return out
 def resultant(pp,qq):
  if not pp or not qq:return E()
  n=len(pp)-1;m=len(qq)-1
  if n==0:return pp[0]**m if m else pp[0]
  if m==0:return qq[0]**n
  mat=[]
  for i in range(m):mat.append([E()]*i+pp[::-1]+[E()]*(m-1-i))
  for i in range(n):mat.append([E()]*i+qq[::-1]+[E()]*(n-1-i))
  return determinant(mat)
 line=get_poly(3);assert len(line)<=2
 projections=[];labels=[]
 for index in [0,1,2,6,4,5,7,8]:
  projections.append(strip_coefficients([resultant(line,get_poly(index))])[0])
  labels.append(['P1',names[index]])
 for ii,jj in [(0,1),(0,2),(1,2)]:
  projections.append(strip_coefficients([resultant(get_poly(ii),get_poly(jj))])[0])
  labels.append([names[ii],names[jj]])
 base_units=[bp,qp,qp-1,qp+1]
 def strip_base(v):
  if not v:return v
  for atom in base_units:
   while True:
    gg=v.gcd(atom)
    if gg.total_degree()==0:break
    v=v/gg
  return v
 necessaries=[];necessary_labels=[]
 for i,rr in enumerate(projections):
  nn=strip_base(rr.a if not rr.b else rr.norm())
  if nn:necessaries.append(nn);necessary_labels.append({'kind':'same_lambda_original_resultant','pair':labels[i]})
 anchor=projections[0]
 for i,rr in enumerate(projections[1:],1):
  nn=strip_base(anchor.a*rr.b-anchor.b*rr.a)
  if nn:necessaries.append(nn);necessary_labels.append({'kind':'same_lambda_cross_identity','pairs':[labels[0],labels[i]]})
 if not necessaries:
  return {'case':case,'excluded':False,'status':'all_original_projection_polynomials_zero','inputSha256':inputsha,'polynomialQuotientIdentitiesChecked':quotient_checks}
 say({'stage':'all_same_lambda_original_resultants_generated','case':case,'polynomialQuotientIdentitiesChecked':quotient_checks,'profiles':[{'label':label,'polynomial':profile(v),'sha256':hashlib.sha256(str(sorted(v.to_dict().items())).encode()).hexdigest()} for label,v in zip(necessary_labels,necessaries)],'claimExcluded':False})
 common=necessaries[0]
 for v in necessaries[1:]:common=common.gcd(v)
 if common.total_degree()>0:
  return {'case':case,'excluded':False,'status':'original_projection_curve_remains','inputSha256':inputsha,'curve':str(common),'curveProfile':profile(common),'polynomialQuotientIdentitiesChecked':quotient_checks}
 anchor_poly=necessaries[0];bgcd=zz;proj_history=[]
 for i,nn in enumerate(necessaries[1:],1):
  ee=anchor_poly.resultant(nn,'q')
  if not ee:continue
  assert all(int(m[1])==0 for m in ee.to_dict())
  bgcd=strip_base(ee if not bgcd else bgcd.gcd(ee))
  entry={'equationIndex':i,'bResultant':profile(ee),'commonB':profile(bgcd)}
  proj_history.append(entry)
  say({'stage':'exact_QQ_original_equal_value_collision_b_projection','case':case,'projection':entry,'claimExcluded':False})
  if bgcd.total_degree()==0:break
 if not bgcd:
  for seed in range(1,int(anchor_poly.total_degree())+3):
   nn=zz
   for i,v in enumerate(necessaries[1:]):nn=nn+(seed**i)*v
   if anchor_poly.gcd(nn).total_degree()==0:
    bgcd=strip_base(anchor_poly.resultant(nn,'q'));assert bgcd;break
 assert bgcd
 closed=bgcd.total_degree()==0
 out={'case':case,'excluded':closed,'status':'entire_original_collision_fiber_excluded' if closed else 'finite_original_collision_b_candidates_remain','inputSha256':inputsha,'projectionHistory':proj_history,'remainingB':profile(bgcd),'polynomialQuotientIdentitiesChecked':quotient_checks}
 if not closed:
  cs={int(m[0]):v for m,v in bgcd.to_dict().items()}
  up=fmpq_poly([cs.get(i,fmpq(0)) for i in range(max(cs)+1)])
  sf=up/up.gcd(up.derivative());sf=sf/sf.leading_coefficient()
  co,fac=sf.factor(monic=True)
  out['remainingSquarefreeB']=str(sf)
  out['remainingBFactors']=[{'factor':str(v),'degree':int(v.degree()),'multiplicity':int(e)} for v,e in fac]
 return out
reports=[]
for case in ['lambda_square_half']:
 report=run_case(case);reports.append(report)
 say({'stage':'complete_equal_value_original_collision_fiber_return','report':report,'claimWholeS0LayerEmpty':False})
closed=all(r['excluded'] for r in reports)
signal.alarm(0)
say({'status':'S0_h_equals_k_nonhalf_collision_excluded' if closed else 'original_equal_value_collision_candidates_remain','sourceSha256':source_sha,'reports':reports,'claimExcluded':closed,'claimWholeS0LayerEmpty':False,'scope':'only S=0,h=k,2lambda^2=1; lambda=1/2 separately excluded by original means and the full-five-column physical Gram bound','ordinaryISPClaim':False,'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss})
raise SystemExit(0 if closed else 2)
