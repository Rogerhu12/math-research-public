#!/usr/bin/env python3
"""R150: original S=0,h=1 collision, both lambda roots, p=1.
Return the five exactly observed b factors to the original equations over QQ(d).
Both d^2=-7 roots and all correlations of b with d are retained.
"""
import argparse,hashlib,itertools,json,os,resource,signal,time
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpq_mpoly_ctx
started=time.perf_counter()
ap=argparse.ArgumentParser()
ap.add_argument('--seconds',type=int,default=int(os.environ.get('ISP_S0_SECONDS','300')))
args=ap.parse_args()
def say(o):
 o['elapsedSeconds']=round(time.perf_counter()-started,6)
 print(json.dumps(o,sort_keys=True),flush=True)
def alarm_handler(signum,frame):
 say({'status':'timeout_unknown','claimExcluded':False})
 raise SystemExit(124)
signal.signal(signal.SIGALRM,alarm_handler);signal.alarm(args.seconds)
ctx=fmpq_mpoly_ctx.get(('b','q'),'lex')
bp,qp=ctx.gens();zz=ctx.constant(0);oo=ctx.constant(1)
def poly(v):return v if hasattr(v,'to_dict') else ctx.constant(v)
class R:
 def __init__(self,n=0,d=None,reduce=True):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  n=poly(n);d=oo if d is None else poly(d)
  assert d
  if not n:self.n=zz;self.d=oo;return
  if reduce:
   g=n.gcd(d);n=n/g;d=d/g
  lc=d.coefficient(0);self.n=n/lc;self.d=d/lc
 def __bool__(self):return bool(self.n)
 def __add__(self,o):
  o=R(o)
  if not self:return o
  if not o:return self
  g=self.d.gcd(o.d);a=self.d/g;b=o.d/g
  return R(self.n*b+o.n*a,a*o.d)
 __radd__=__add__
 def __neg__(self):return R(-self.n,self.d,False)
 def __sub__(self,o):return self+-R(o)
 def __rsub__(self,o):return R(o)+-self
 def __mul__(self,o):
  o=R(o)
  if not self or not o:return R()
  g=self.n.gcd(o.d);h=o.n.gcd(self.d)
  return R((self.n/g)*(o.n/h),(self.d/h)*(o.d/g),False)
 __rmul__=__mul__
 def __truediv__(self,o):
  o=R(o);assert o
  return self*R(o.d,o.n,False)
 def __rtruediv__(self,o):return R(o)/self
 def __pow__(self,n):
  if n<0:assert self;return R(self.d**(-n),self.n**(-n),False)
  return R(self.n**n,self.d**n,False)
 def __eq__(self,o):
  o=R(o);return self.n*o.d==o.n*self.d

Delta=R(-7)
class E:
 def __init__(self,a=0,b=0):
  if isinstance(a,E):self.a=a.a;self.b=a.b;return
  self.a=R(a);self.b=R(b)
 def __bool__(self):return bool(self.a) or bool(self.b)
 def __add__(self,o):o=E(o);return E(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return E(-self.a,-self.b)
 def __sub__(self,o):return self+-E(o)
 def __rsub__(self,o):return E(o)+-self
 def __mul__(self,o):
  o=E(o);return E(self.a*o.a+Delta*self.b*o.b,self.a*o.b+self.b*o.a)
 __rmul__=__mul__
 def __pow__(self,n):
  assert n>=0
  out=E(1);v=self
  while n:
   if n&1:out=out*v
   v=v*v;n//=2
  return out
 def __eq__(self,o):o=E(o);return self.a==o.a and self.b==o.b
 def conj(self):return E(self.a,-self.b)

half=E(fmpq(1,2))
lam=E(fmpq(5,8),fmpq(1,8))
b=E(bp);c=E(fmpq(1,28),fmpq(1,28));a=1-b-c
p=E(1);q=E(qp);h=E(1);k=2*lam-2
w=E(fmpq(-1,4),fmpq(5,28))
fbar=b*(2-lam)*half
assert 4*lam*lam-5*lam+2==0
assert h+k+1==2*lam
assert a+w+b*h+c*k==lam
assert a+2*w+b*h*h+c*k*k==2*lam*lam
assert a+3*w+b*h**3+c*k**3==4*lam**3
u=b+c*q;V2=b+c*q*q;P02=b+c*q**3-3*u*V2+2*u**3
ic=E(fmpq(7,2),fmpq(-7,2))
assert c*ic==1
ib=E(R(1,bp*(qp-1)));icq=ic*E(R(1,qp*(qp-1)))
assert ib*b*(q-1)==1 and icq*c*q*(q-1)==1
atoms=[bp,qp,qp-1,qp+1]
def strip_paid(p0):
 if not p0:return p0
 for atom in atoms:
  while True:
   gg=p0.gcd(atom)
   if gg.total_degree()==0:break
   p0=p0/gg
 return p0
den_seen=set()
def paid(v):
 for rr in [v.a,v.b]:
  key=str(sorted(rr.d.to_dict().items()))
  if key not in den_seen:
   assert strip_paid(rr.d).total_degree()==0
   den_seen.add(key)
def profile(v):
 dd=v.to_dict()
 return {'degrees':[max((int(m[i]) for m in dd),default=-1) for i in range(2)],'terms':len(dd)}
source_sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
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
 def conj(self):return P({ij:v.conj() for ij,v in self.co.items()})
def cp(v):return P({(0,0):E(v)})
def scale(v,pp):return P({ij:E(v)*vv for ij,vv in pp.co.items()})

fp=cp(fbar);tp=P({(0,1):E(1)});zero=P()
one=[cp(1),zero,cp(1),cp(1)]
def va(v,z0):return [x+y for x,y in zip(v,z0)]
def vs(v0,v):return [v0*x for x in v]
def vm(v,z0):return [v[0]*z0[0],v[0]*z0[1]+v[1]*z0[0],v[2]*z0[2],v[3]*z0[3]]
def tau(v):return scale(a,v[0])+v[1]+scale(b,v[2])+scale(c,v[3])
W1=cp(half*V2-u*u)+scale(2*u,fp)
W2=cp(u*V2-2*u**3+lam*P02)+scale(V2+2*u*u,fp)-scale(b*c*q,tp)
XX=scale(ib,scale(q,W1)-W2);YY=scale(icq,W2-W1)
r=XX-cp(a)-scale(c,tp);ss=YY-cp(a*q)-scale(b,tp)
Arow=scale(E(2),fp)-scale(2*b,XX)-scale(2*c,YY)+scale(2*b*c,tp)
rows=[[zero,zero,cp(1),cp(q)],[zero,Arow,r,ss],[cp(1),r,zero,tp],[cp(q),ss,tp,zero]]
def DK(v):return [tau(vm(row,v)) for row in rows]
d=DK(one);F2=tau(d);DKd=DK(d);dd=vm(d,d)
assert not (F2-scale(E(2),fp))
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
assert not mean(0) and not (P2(rows[0])-cp(P02)) and not (N4(rows[0])-cp(2*lam*P02))
VV=[cp(1),cp(w),cp(h),cp(k)]
assert not P2(VV) and not N4(VV)
raw=[mean(1),mean(2),mean(3),Pjet2(rows[0],rows[1])-cp(3*w*P02),P2(rows[2])-cp(h**3*P02),P2(rows[3])-cp(k**3*P02),Njet4(rows[0],rows[1])-cp(4*lam*w*P02),N4(rows[2])-cp(2*lam*h*h*P02),N4(rows[3])-cp(2*lam*k*k*P02)]
names=['E1','EB','EC','P1','PB','PC','N1','NB','NC']
hh=hashlib.sha256()
for name,po in zip(names,raw):
 assert all(ij[0]==0 for ij in po.co)
 for ij,v in sorted(po.co.items()):
  paid(v)
  for rr in [v.a,v.b]:hh.update((name+str(ij)+str(sorted(rr.n.to_dict().items()))+'/'+str(sorted(rr.d.to_dict().items()))+'\n').encode())
inputsha=hh.hexdigest()
say({'stage':'both_original_collision_lambda_roots_and_all_nine_equations_verified','sourceSha256':source_sha,'inputSha256':inputsha,'tDegrees':[max((ij[1] for ij in po.co),default=-1) for po in raw],'NvalueIdenticallyZero':True,'claimExcluded':False})
# Polynomial coefficients over QQ[d]/(d^2+7), with no parameter divisions.
class QE:
 def __init__(self,a0=0,b0=0):
  if isinstance(a0,QE):self.a=a0.a;self.b=a0.b;return
  self.a=poly(a0);self.b=poly(b0)
 def __bool__(self):return bool(self.a) or bool(self.b)
 def __add__(self,o):o=QE(o);return QE(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return QE(-self.a,-self.b)
 def __sub__(self,o):return self+-QE(o)
 def __rsub__(self,o):return QE(o)+-self
 def __mul__(self,o):o=QE(o);return QE(self.a*o.a-7*self.b*o.b,self.a*o.b+self.b*o.a)
 __rmul__=__mul__
 def __pow__(self,n):
  out=QE(1);v=self
  while n:
   if n&1:out=out*v
   v=v*v;n//=2
  return out
 def norm(self):return self.a*self.a+7*self.b*self.b
qzero=QE();qone=QE(1)
def trim(pp):
 pp=list(pp)
 while pp and not pp[-1]:pp.pop()
 return pp
clear_cache={}
def get_poly(index):
 if index in clear_cache:return clear_cache[index]
 po=raw[index]
 den=oo
 for vv in po.co.values():
  for rr in [vv.a,vv.b]:den=den*(rr.d/den.gcd(rr.d))
 degree=max((ij[1] for ij in po.co),default=-1)
 vv=[]
 for j0 in range(degree+1):
  v=po.co.get((0,j0),E())
  vv.append(QE(v.a.n*(den/v.a.d),v.b.n*(den/v.b.d)))
 for atom in atoms:
  while any(vv):
   gg=atom
   for v in vv:gg=gg.gcd(v.a).gcd(v.b)
   if gg.total_degree()==0:break
   vv=[QE(v.a/gg,v.b/gg) for v in vv]
 out=trim(vv);clear_cache[index]=out
 say({'stage':'original_collision_equation_cleared','name':names[index],'degree':len(out)-1,'coefficientProfiles':[{'even':profile(v.a),'odd':profile(v.b)} for v in out],'claimExcluded':False})
 return out
def determinant(mm):
 n=len(mm)
 if n==0:return qone
 if n==1:return mm[0][0]
 out=qzero
 for j0 in range(n):
  if mm[0][j0]:out=out+((-1)**j0)*mm[0][j0]*determinant([row[:j0]+row[j0+1:] for row in mm[1:]])
 return out
def resultant(pp,qq):
 pp=trim(pp);qq=trim(qq)
 if not pp or not qq:return qzero
 n=len(pp)-1;m=len(qq)-1
 if n==0:return pp[0]**m if m else pp[0]
 if m==0:return qq[0]**n
 mat=[]
 for i in range(m):mat.append([qzero]*i+pp[::-1]+[qzero]*(m-1-i))
 for i in range(n):mat.append([qzero]*i+qq[::-1]+[qzero]*(n-1-i))
 return determinant(mat)
class FE:
 def __init__(self,field,v=0):
  self.field=field
  if isinstance(v,FE):
   assert v.field is field;self.p=v.p;return
  pp=v if isinstance(v,fmpq_poly) else fmpq_poly([v])
  self.p=divmod(pp,field.mod)[1]
 def __bool__(self):return bool(self.p)
 def __add__(self,o):o=FE(self.field,o);return FE(self.field,self.p+o.p)
 __radd__=__add__
 def __neg__(self):return FE(self.field,-self.p)
 def __sub__(self,o):return self+-FE(self.field,o)
 def __rsub__(self,o):return FE(self.field,o)+-self
 def __mul__(self,o):o=FE(self.field,o);return FE(self.field,self.p*o.p)
 __rmul__=__mul__
 def __eq__(self,o):o=FE(self.field,o);return self.p==o.p
 def __pow__(self,n):
  assert n>=0
  out=FE(self.field,1);v=self
  while n:
   if n&1:out=out*v
   v=v*v;n//=2
  return out
 def inv(self):
  assert self
  gg,ss,tt=self.p.xgcd(self.field.mod)
  assert self.p*ss+self.field.mod*tt==gg
  assert gg and gg.degree()==0
  vv=FE(self.field,ss/gg[0]);assert self*vv==1
  self.field.inverses+=1
  return vv
class Field:
 def __init__(self,phi):
  self.mod=phi/phi.leading_coefficient();self.inverses=0
  self.zero=FE(self,0);self.one=FE(self,1)
 def __call__(self,v=0):return FE(self,v)
def ftrim(pp):
 pp=list(pp)
 while pp and not pp[-1]:pp.pop()
 return pp
def frem(pp,qq):
 pp=ftrim(pp);qq=ftrim(qq);assert qq
 iv=qq[-1].inv()
 while pp and len(pp)>=len(qq):
  sh=len(pp)-len(qq);co=pp[-1]*iv
  for j,v in enumerate(qq):pp[j+sh]=pp[j+sh]-co*v
  pp=ftrim(pp)
 return pp
def fgcd(pp,qq):
 pp=ftrim(pp);qq=ftrim(qq)
 while qq:pp,qq=qq,frem(pp,qq)
 if pp:
  iv=pp[-1].inv();pp=[iv*v for v in pp]
 return pp
def fquot(pp,qq):
 pp=ftrim(pp);qq=ftrim(qq);assert qq
 field=qq[-1].field
 out=[field.zero]*max(0,len(pp)-len(qq)+1);iv=qq[-1].inv()
 while pp and len(pp)>=len(qq):
  sh=len(pp)-len(qq);co=pp[-1]*iv;out[sh]=out[sh]+co
  for j,v in enumerate(qq):pp[j+sh]=pp[j+sh]-co*v
  pp=ftrim(pp)
 assert not pp
 return ftrim(out)

assert inputsha=='78efb0139e4e31423aa2dfb788488ae323a5864e2af522fb53b307777ee13b73'
# The complete finite b cover is the exact observed outcome of source727cbc68,
# run45825165838/job139927331594 (exit2 only because candidates remained).
# Its 490-second original b resultants are NOT repeated here.
field=Field(fmpq_poly([7,0,1]));dd=field(fmpq_poly([0,1]))
bbvals=[field(fmpq(1,2)),field(fmpq(3,4))+dd*fmpq(1,4),field(fmpq(3,4))-dd*fmpq(1,4),field(fmpq(13,28))+dd*fmpq(1,28),field(fmpq(13,28))-dd*fmpq(1,28)]
def fa(pp,qq):
 out=[field.zero]*max(len(pp),len(qq))
 for i,v in enumerate(pp):out[i]=out[i]+v
 for i,v in enumerate(qq):out[i]=out[i]+v
 return ftrim(out)
def fm(pp,qq):
 if not pp or not qq:return []
 out=[field.zero]*(len(pp)+len(qq)-1)
 for i,v in enumerate(pp):
  for j0,vv in enumerate(qq):out[i+j0]=out[i+j0]+v*vv
 return ftrim(out)
cover=[field.one]
for bv in bbvals:cover=fm(cover,[-bv,field.one])
expected=[fmpq(-11,98),fmpq(6,7),fmpq(-1009,392),fmpq(751,196),fmpq(-41,14),fmpq(1)]
assert len(cover)==len(expected) and all(v==vv for v,vv in zip(cover,expected))
for bv in bbvals:
 bv.inv()
 # c and the actual b values are numerical units on both conjugate roots.
field(fmpq_poly([fmpq(1,28),fmpq(1,28)])).inv()
say({'stage':'complete_observed_b_cover_returned_without_reprojection','inputSha256':inputsha,'parameterDimension':10,'bValues':[str(v.p) for v in bbvals],'allFiveFactorsAndBothLambdaRootsRetained':True,'claimExcluded':False})
qecache={}
def pair_resultant(ii,jj):
 key=tuple(sorted((ii,jj)))
 if key not in qecache:qecache[key]=resultant(get_poly(ii),get_poly(jj))
 return qecache[key]
def specialize_q(v,bv):
 terms_a=v.a.to_dict();terms_b=v.b.to_dict()
 degq=max([int(m[1]) for m in terms_a]+[int(m[1]) for m in terms_b],default=-1)
 out=[field.zero]*(degq+1)
 maxb=max([int(m[0]) for m in terms_a]+[int(m[0]) for m in terms_b],default=0)
 powers=[field.one]
 for _ in range(maxb):powers.append(powers[-1]*bv)
 for m,co in terms_a.items():out[int(m[1])]=out[int(m[1])]+field(co)*powers[int(m[0])]
 for m,co in terms_b.items():out[int(m[1])]=out[int(m[1])]+dd*field(co)*powers[int(m[0])]
 return ftrim(out)
def as_QE(v):
 return QE(v.a.n/v.a.d,v.b.n/v.b.d)
unit_qe=[('q',QE(qp)),('q-1',QE(qp-1)),('q+1',QE(qp+1)),('u',as_QE(u)),('P0',as_QE(P02)),('normalized_u_minus_one',as_QE(2*u-1-q))]
preferred=[(3,0),(3,1),(3,2),(3,6),(3,4),(3,5),(3,7),(3,8),(0,1),(0,2),(1,2)]
pairs=preferred+[(i,j0) for i in range(9) for j0 in range(i+1,9) if not any(set((i,j0))==set(pair) for pair in preferred)]
reports=[]
for number,bv in enumerate(bbvals):
 before=field.inverses
 unit_specs=[(label,specialize_q(v,bv)) for label,v in unit_qe]
 history=[];qqg=[];whole_unit_zero=None
 def strip_q(pp):
  for label,v in unit_specs:
   if not v:return [field.one],label
   while len(pp)>1:
    common=fgcd(pp,v)
    if len(common)<=1:break
    history.append({'removedOriginalUnit':label,'degree':len(common)-1})
    pp=fquot(pp,common)
  return pp,None
 for ii,jj in pairs:
  rr=specialize_q(pair_resultant(ii,jj),bv)
  if not rr:continue
  qqg=fgcd(qqg,rr) if qqg else rr
  qqg,newzero=strip_q(qqg)
  if newzero:whole_unit_zero=newzero
  history.append({'originalPair':[names[ii],names[jj]],'remainingQDegree':len(qqg)-1})
  if len(qqg)==1:break
 closed=len(qqg)==1
 report={'bValue':str(bv.p),'parameterRoots':2,'excluded':closed,'remainingQDegree':len(qqg)-1,'history':history,'wholeFiberOriginalUnitZero':whole_unit_zero,'fieldInverseIdentitiesChecked':field.inverses-before}
 if not closed:report['remainingQCoefficientsInDField']=[str(v.p) for v in qqg]
 reports.append(report)
 say({'stage':'complete_original_collision_parameter_fiber_return','number':number,'report':report,'claimWholeS0LayerEmpty':False})
closed=all(r['excluded'] for r in reports)
signal.alarm(0)
say({'status':'entire_S0_h1_and_symmetric_k1_collision_excluded' if closed else 'original_h1_parameter_candidates_remain','sourceSha256':source_sha,'inputSha256':inputsha,'reports':reports,'claimExcluded':closed,'claimWholeS0LayerEmpty':False,'scope':'complete S=0,h=1; k=1 by B/C relabeling; all original equations and every lambda/b conjugate retained','ordinaryISPClaim':False,'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss})
raise SystemExit(0 if closed else 2)
