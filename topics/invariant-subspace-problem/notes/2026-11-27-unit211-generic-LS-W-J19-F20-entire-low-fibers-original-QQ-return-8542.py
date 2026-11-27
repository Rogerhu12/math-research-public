#!/usr/bin/env python3
"""W/J19: entire F20 original norm-zero k fibers: degrees 2,2,3,5,8.
New exact QQ finite original Gram return to 1, physical D or D^2.
The complete F20 comes from the successful partition before the frozen 4acc
API error. C15 contributes degrees 2,2,3,5; the additional norm fiber has degree8.
Every nonunit in either finite constant algebra is split, with both factors
retained. Only an actual identically-zero named original paid unit excludes
a branch. No old J19 generic computation, C9 computation or modular test runs.
180 seconds / 4 GiB, self-contained, only small certificates/hashes.
"""
import json,time,hashlib,signal,resource
from pathlib import Path
from flint import fmpq_poly,fmpq
start=time.perf_counter();signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
P=lambda v=():fmpq_poly([fmpq(x) for x in v])
def coeffs(pp):return [str(c) for c in pp.coeffs()]
def say(**r):r['seconds']=time.perf_counter()-start;print(json.dumps(r),flush=True)
def digest(obj):
 bb=json.dumps(obj,separators=(',',':')).encode()
 return dict(bytes=len(bb),sha256=hashlib.sha256(bb).hexdigest())
class BaseNonunit(Exception):
 def __init__(self,g):self.g=g
class ENonunit(Exception):
 def __init__(self,g,q,why,paid=None):self.g=g;self.q=q;self.why=why;self.paid=paid
class PhysicalZero(Exception):
 def __init__(self,name):self.name=name
results=[];splits=[]
def run_fiber(F,label,hdata=None):
 F=F/F[F.degree()];inverse_count=0
 class K:
  def __init__(self,v=0):
   if isinstance(v,K):self.p=v.p;return
   if not isinstance(v,fmpq_poly):v=P([v])
   qq,rr=divmod(v,F);assert qq*F+rr==v;self.p=rr
  def __bool__(self):return bool(self.p)
  def __neg__(self):return K(-self.p)
  def __add__(self,v):return K(self.p+K(v).p)
  __radd__=__add__
  def __sub__(self,v):return K(self.p-K(v).p)
  def __rsub__(self,v):return K(v)-self
  def __mul__(self,v):return K(self.p*K(v).p)
  __rmul__=__mul__
  def __eq__(self,v):return self.p==K(v).p
  def inv(self):
   nonlocal inverse_count
   assert self
   if self==1:return K(1)
   g,s,t=self.p.xgcd(F);assert s*self.p+t*F==g
   if g.degree()>0:raise BaseNonunit(g/g[g.degree()])
   ans=K(s/g[0]);assert self*ans==1;inverse_count+=1;return ans
  def __truediv__(self,v):return self*K(v).inv()
  def __rtruediv__(self,v):return K(v)*self.inv()
  def __pow__(self,n):
   if n<0:return self.inv()**(-n)
   out=K(1);v=self
   while n:
    if n&1:out=out*v
    v=v*v;n//=2
   return out
  def data(self):return coeffs(self.p)
 class U:
  def __init__(self,v=()):
   if isinstance(v,U):self.c=v.c[:];return
   if isinstance(v,(K,int,fmpq)):v=[v]
   self.c=[K(z) for z in v]
   while self.c and not self.c[-1]:self.c.pop()
  def __bool__(self):return bool(self.c)
  def degree(self):return len(self.c)-1
  def __neg__(self):return U([-z for z in self.c])
  def __add__(self,v):
   v=U(v);n=max(len(self.c),len(v.c))
   return U([(self.c[j] if j<len(self.c) else K())+(v.c[j] if j<len(v.c) else K()) for j in range(n)])
  __radd__=__add__
  def __sub__(self,v):return self+-U(v)
  def __rsub__(self,v):return U(v)+-self
  def __mul__(self,v):
   v=U(v)
   if not self or not v:return U()
   w=[K() for _ in range(len(self.c)+len(v.c)-1)]
   for i,a in enumerate(self.c):
    for j,b in enumerate(v.c):w[i+j]=w[i+j]+a*b
   return U(w)
  __rmul__=__mul__
  def scale(self,v):return U([z*K(v) for z in self.c])
  def __eq__(self,v):return self.c==U(v).c
  def data(self):return [z.data() for z in self.c]
 def dr(a,b):
  a,b=U(a),U(b);assert b
  q=U();r=U(a);li=b.c[-1].inv()
  while r and r.degree()>=b.degree():
   shift=r.degree()-b.degree();cf=r.c[-1]*li
   term=U([K()]*shift+[cf]);q=q+term;r=r-term*b
  assert q*b+r==a and (not r or r.degree()<b.degree())
  return q,r
 def xg(a,b):
  a,b=U(a),U(b);r0,r1=a,b;s0,s1=U(1),U();t0,t1=U(),U(1)
  while r1:
   q,r=dr(r0,r1);r0,r1=r1,r;s0,s1=s1,s0-q*s1;t0,t1=t1,t0-q*t1
  if r0:
   iv=r0.c[-1].inv();r0=r0.scale(iv);s0=s0.scale(iv);t0=t0.scale(iv)
  assert s0*a+t0*b==r0
  return r0,s0,t0
 kv=K(P([0,1]))
 fcoeff=[-kv**5-10*kv**4-40*kv**3-104*kv*kv-160*kv-128,
         -2*kv**5-14*kv**4-12*kv**3-128,
         -kv**5-8*kv**4+24*kv**3+64*kv*kv+192*kv,
         -8*kv**4-16*kv**3-96*kv*kv,16*kv**3]
 jraw=U(fcoeff);jmonic=jraw.scale(fcoeff[-1].inv())
 assert jmonic.scale(fcoeff[-1])==jraw and jmonic.degree()==4
 H=jmonic if hdata is None else U([K(P(v)) for v in hdata])
 H=H.scale(H.c[-1].inv());assert H.c[-1]==1 and H.degree()>0
 qj,rj=dr(jmonic,H);assert not rj and qj*H==jmonic
 n=H.degree()
 class A:
  def __init__(self,v=0):
   if isinstance(v,A):self.c=v.c[:];return
   v=U(v);cc=v.c[:]
   for j in range(len(cc)-1,n-1,-1):
    lead=cc[j]
    if lead:
     for h in range(n):cc[j-n+h]=cc[j-n+h]-lead*H.c[h]
    cc[j]=K()
   assert not any(cc[n:]);self.c=cc[:n]+[K()]*(n-min(n,len(cc)))
  def __bool__(self):return any(self.c)
  def __neg__(self):return A([-c for c in self.c])
  def __add__(self,v):v=A(v);return A([a+b for a,b in zip(self.c,v.c)])
  __radd__=__add__
  def __sub__(self,v):return self+-A(v)
  def __rsub__(self,v):return A(v)+-self
  def __mul__(self,v):
   v=A(v);out=[K() for _ in range(2*n-1)]
   for i,a in enumerate(self.c):
    if not a:continue
    for j,b in enumerate(v.c):
     if b:out[i+j]=out[i+j]+a*b
   return A(out)
  __rmul__=__mul__
  def __eq__(self,v):return self.c==A(v).c
  def inv(self,why='actual original inverse',paid=None):
   nonlocal inverse_count
   if not self:
    if paid is not None:raise PhysicalZero(paid)
    raise ZeroDivisionError(why)
   g,s,t=xg(U(self.c),H)
   assert s*U(self.c)+t*H==g
   if g.degree()>0:
    q,r=dr(H,g);assert not r and q*g==H and 0<g.degree()<H.degree()
    raise ENonunit(g.data(),q.data(),why,paid)
   ans=A(s);assert self*ans==1;inverse_count+=1;return ans
  def __truediv__(self,v):return self*A(v).inv()
  def __rtruediv__(self,v):return A(v)*self.inv()
  def __pow__(self,n0):
   if n0<0:return self.inv()**(-n0)
   out=A(1);v=self
   while n0:
    if n0&1:out=out*v
    v=v*v;n0//=2
   return out
  def json(self):return [c.data() for c in self.c]
 def unit(name,v):
  v=A(v)
  if not v:raise PhysicalZero(name)
  iv=v.inv('named already paid original weight '+name,paid=name)
  assert v*iv==1
 k=A(kv);e=A([0,1])
 for name,v in [('k',k),('k+1',k+1),('k+2',k+2),('k+4',k+4),('e',e)]:unit(name,v)
 u=e+1;Q=e*k;V=u*k+2;d=1-Q
 for name,v in [('u',u),('Q',Q),('V',V),('1-Q',d),('u-Q',u-Q),('2e+1',2*e+1)]:unit(name,v)
 ell=u*((k+2)**2-2*e*k)/(k*V)
 for name,v in [('ell',ell),('ell-u',ell-u),('Q-2',Q-2)]:unit(name,v)
 bc=(ell*ell-(u-ell)**2/d)/4;unit('bc',bc)
 V2=2*u-ell*Q;T0=V2-2*u*u;P02=(2-3*u)*V2-Q*u+2*u**3
 J=2*u*(1-u)+ell*Q;Phi=T0+4*u-4+Q;Pf=T0*(J-Q);M=ell*V2-u*u
 Hpaid=4*e*k-k*k-4*k-8
 C9=4*e*e*k*k-e*(k**4+9*k**3+20*k*k+16*k)+k**3+10*k*k+24*k+16
 for name,v in [('P02',P02),('Phi',Phi),('T0',T0),('J-Q',J-Q),('H',Hpaid),('C9',C9)]:unit(name,v)
 assert M==4*bc*d and Phi*(J-2*u*Q)-Pf==0
 assert sum((A(fcoeff[j])*e**j for j in range(5)),A())==0
 say(stage='new_J19_F20_finite_original_weight_algebra',path=label,kDegree=int(F.degree()),eDegree=n,QQDimension=int(F.degree())*n,allActualPaidUnitInverseProductsOne=True,allNormZeroBranchesRetained=True,claimExcluded=False)
 class Mpoly:
  def __init__(self,v=0):
   if isinstance(v,Mpoly):self.terms=v.terms.copy();return
   c=A(v);self.terms={(0,0,0):c} if c else {}
  @staticmethod
  def variable(j):
   p=Mpoly();m=[0,0,0];m[j]=1;p.terms[tuple(m)]=A(1);return p
  @staticmethod
  def from_terms(ts):
   p=Mpoly();p.terms={m:c for m,c in ts if c};return p
  def __bool__(self):return bool(self.terms)
  def __add__(self,v):
   v=Mpoly(v);p=Mpoly(self)
   for m,c in v.terms.items():
    z=p.terms.get(m,A())+c
    if z:p.terms[m]=z
    elif m in p.terms:del p.terms[m]
   return p
  __radd__=__add__
  def __neg__(self):return Mpoly.from_terms((m,-c) for m,c in self.terms.items())
  def __sub__(self,v):return self+-Mpoly(v)
  def __rsub__(self,v):return Mpoly(v)+-self
  def __mul__(self,v):
   v=Mpoly(v);p=Mpoly()
   for ma,ca in self.terms.items():
    for mb,cb in v.terms.items():
     m=tuple(ma[j]+mb[j] for j in range(3));z=p.terms.get(m,A())+ca*cb
     if z:p.terms[m]=z
     elif m in p.terms:del p.terms[m]
   return p
  __rmul__=__mul__
  def scale(self,c):
   c=A(c);return Mpoly.from_terms((m,v*c) for m,v in self.terms.items())
  def __pow__(self,n):
   p=Mpoly(1)
   for i in range(n):p=p*self
   return p
  def __eq__(self,v):return not(self-Mpoly(v))
  def degree(self):return max((sum(m) for m in self.terms),default=-1)
  def json(self):return [[list(m),c.json()] for m,c in sorted(self.terms.items())]
 class E:
  def __init__(self,a=0,b=0):
   if isinstance(a,E):self.a=a.a;self.b=a.b;return
   self.a=Mpoly(a);self.b=Mpoly(b)
  def __bool__(self):return bool(self.a) or bool(self.b)
  def __add__(self,v):v=E(v);return E(self.a+v.a,self.b+v.b)
  __radd__=__add__
  def __neg__(self):return E(-self.a,-self.b)
  def __sub__(self,v):return self+-E(v)
  def __rsub__(self,v):return E(v)+-self
  def __mul__(self,v):v=E(v);return E(self.a*v.a+(self.b*v.b).scale(d),self.a*v.b+self.b*v.a)
  __rmul__=__mul__
  def __pow__(self,n):
   out=E(1)
   for i in range(n):out=out*self
   return out
  def conj(self):return E(self.a,-self.b)
  def __eq__(self,v):v=E(v);return self.a==v.a and self.b==v.b
 b=E(Mpoly(ell/2),Mpoly((u-ell)/(2*d)));c=b.conj();p=E(1,1);q=p.conj();a=1-ell
 assert b*c==E(Mpoly(bc)) and b*p+c*q==E(Mpoly(u))
 x,y,t=[Mpoly.variable(j) for j in range(3)];X=E(x,y);Y=X.conj()
 f=(x.scale(u)+y.scale(u-ell*Q)-Mpoly(T0/2)).scale(1/(2*u))
 W2=x.scale(V2)+y.scale(2*u-u*Q-ell*Q)
 lam=(W2-Mpoly(u*T0)-f.scale(V2+2*u*u)+t.scale(bc*Q)).scale(1/P02)
 T=((lam.scale(P02)-Mpoly((1-u)*T0)).scale(T0)-f.scale(Pf)-t.scale(Phi*bc*Q)).scale(1/(Q*P02))-Mpoly(ell)
 rg=X-p*E(Mpoly(a))-c*E(t);sg=Y-q*E(Mpoly(a))-b*E(t)
 ag=E(f.scale(2))-2*b*X-2*c*Y+E(t.scale(2*bc))
 zz=E();oo=E(1);gram=[[zz,zz,p,q],[zz,ag,rg,sg],[p,rg,zz,E(t)],[q,sg,E(t),zz]];unitvec=[oo,zz,oo,oo]
 def va(v,z):return [a+b for a,b in zip(v,z)]
 def vs(v,z):return [v*a for a in z]
 def vm(v,z):return [v[0]*z[0],v[0]*z[1]+v[1]*z[0],v[2]*z[2],v[3]*z[3]]
 def tau(v):return E(Mpoly(a))*v[0]+v[1]+b*v[2]+c*v[3]
 def DK(v):return [tau(vm(row,v)) for row in gram]
 dv=DK(unitvec);F2=tau(dv);Kd=DK(dv)
 assert F2==E(f.scale(2))
 def mean(j):
  first=2*tau(vm(gram[0],gram[1])) if j==1 else tau(vm(gram[j],gram[j]))
  return first-2*Kd[j]-2*vm(dv,dv)[j]+2*F2*dv[j]
 assert not mean(0)
 def N4(v):return 2*tau(vm(dv,vm(v,v)))-F2*tau(vm(v,v))-4*tau(v)*tau(vm(dv,v))+2*F2*tau(v)**2+tau(vm(v,DK(v)))
 def P2(v):
  cv=va(v,vs(-tau(v),unitvec));return tau(vm(vm(cv,cv),cv))
 vc=va(gram[0],vs(-tau(gram[0]),unitvec));zc=va(gram[1],vs(-tau(gram[1]),unitvec));Pj=3*tau(vm(vm(vc,vc),zc))
 assert N4(gram[0])==E(lam.scale(2*P02)) and Pj==E((lam-1-T).scale(3*P02)) and P2(gram[0])==E(Mpoly(P02))
 N1=N4(va(gram[0],gram[1]))-N4(gram[0])-N4(gram[1])-E(lam.scale(A(4)/3))*Pj
 A2=2*lam**2-2*lam+1;B3=4*lam**3-6*lam**2+3*lam-1
 NS=b*N4(gram[2])+c*N4(gram[3])-E((lam*(Mpoly(ell)+2*T+A2)).scale(2*P02))
 PS=b*P2(gram[2])+c*P2(gram[3])-E((Mpoly(ell)+3*T+3*A2+B3).scale(P02))
 E1,EB,EC=mean(1),mean(2),mean(3)
 assert not E1.b and EB.conj()==EC and not N1.b and not NS.b and not PS.b
 original=[E1.a,EB.a,EB.b,N1.a,NS.a,PS.a];names=['E1','EBe','EBo','N1','NS','PS']

 D=A2.scale(ell)-T*T
 mons=sorted([(i,j,h) for i in range(5) for j in range(5-i) for h in range(5-i-j)],key=lambda z:(sum(z),z[1],z[0],z[2]),reverse=True)
 assert len(mons)==35 and mons[-1]==(0,0,0)
 rawrows=[];labels=[];basis=[];tags=[];pivots=[]
 def vector(pp):return [pp.terms.get(m,A()) for m in mons]
 def subrow(a,b,cf):return [a[j]-cf*b[j] for j in range(35)]
 for ni,pp in enumerate(original):
  assert pp.degree()<=([2,2,2,2,3,3][ni])
  for mm in sorted([m for m in mons if sum(m)<=4-[2,2,2,2,3,3][ni]],key=lambda z:(sum(z),z[1],z[0],z[2])):
   product=pp*Mpoly.from_terms([(mm,A(1))]);assert product.degree()<=4
   rawrows.append(vector(product));labels.append([names[ni],mm])
 assert len(rawrows)==48
 for idx,initial in enumerate(rawrows):
  row=initial[:];tag={idx:A(1)}
  for brow,pv,bt in zip(basis,pivots,tags):
   cf=row[pv]
   if not cf:continue
   row=subrow(row,brow,cf)
   for j,v in bt.items():tag[j]=tag.get(j,A())-cf*v
  if not any(row):continue
  pv=next(j for j,v in enumerate(row) if v);iv=row[pv].inv('actual original Macaulay pivot')
  row=[v*iv for v in row];tag={j:v*iv for j,v in tag.items() if v}
  assert row[pv]==1 and all(not row[j] for j in pivots)
  basis.append(row);tags.append(tag);pivots.append(pv)
  if len(basis)==35:break
 returned=None;combination={};target=None
 for exponent,pp in [(0,Mpoly(1)),(1,D),(2,D*D)]:
  target0=vector(pp);rem=target0[:];actual={}
  for brow,pv,bt in zip(basis,pivots,tags):
   cf=rem[pv]
   if not cf:continue
   rem=subrow(rem,brow,cf)
   for j,v in bt.items():actual[j]=actual.get(j,A())+cf*v
  if any(rem):continue
  for j in range(35):assert sum((cf*rawrows[i][j] for i,cf in actual.items()),A())==target0[j]
  returned=exponent;combination=actual;target=target0;break
 cert=dict(kModulus=coeffs(F),eModulus=H.data(),originalLabels=labels,rank=len(basis),pivots=pivots,Dpower=returned,combination={str(j):v.json() for j,v in combination.items()},target=[v.json() for v in target] if target is not None else None)
 return dict(path=label,kModulus=coeffs(F),eModulus=H.data(),kDegree=int(F.degree()),eDegree=n,QQDimension=int(F.degree())*n,allOriginalE0N0P1MeanN1WeightedNPActuallyRebuilt=True,originalRows=48,columns=35,rank=len(basis),DpowerReturned=returned,allOriginalThirtyFiveColumnCombinationProductsActuallyVerified=returned is not None,physicalDSource='D+ell*HA/u^2=bc*(hU-kU)^2; same original distinct singleton values',actualInverseProducts=inverse_count,certificate=digest(cert),excluded=returned is not None)
def process(F,label,hdata=None):
 t0=time.perf_counter()
 try:
  r=run_fiber(F,label,hdata);r['wallSeconds']=time.perf_counter()-t0
  results.append(r);say(stage='new_J19_F20_entire_finite_original_QQ_return',**r,wholeJ19Excluded=False)
 except BaseNonunit as ex:
  q,rr=divmod(F,ex.g);assert not rr and q*ex.g==F and 0<ex.g.degree()<F.degree()
  rec=dict(path=label,kFactor=coeffs(ex.g),kComplement=coeffs(q),bothBranchesRetained=True,productActuallyVerified=True)
  splits.append(rec);say(stage='new_J19_F20_actual_QQ_k_nonunit_split',**rec,claimExcluded=False)
  process(ex.g,label+'/ka',hdata);process(q,label+'/kb',hdata)
 except ENonunit as ex:
  rec=dict(path=label,eFactor=ex.g,eComplement=ex.q,reason=ex.why,paidUnitZeroOnFirstFactor=ex.paid,bothFactorsActuallyMultipliedBack=True,allOriginalFibersRetained=True)
  splits.append(rec);say(stage='new_J19_F20_actual_QQ_e_nonunit_split',**rec,claimExcluded=False)
  if ex.paid is not None:
   r=dict(path=label+'/ea',kModulus=coeffs(F),eModulus=ex.g,paidOriginalWeightIdenticallyZero=ex.paid,zeroFollowsActualGcdDivisionProduct=True,excluded=True)
   results.append(r);say(stage='new_J19_F20_named_original_paid_unit_zero',**r)
  else:process(F,label+'/ea',ex.g)
  process(F,label+'/eb',ex.q)
 except PhysicalZero as ex:
  r=dict(path=label,kModulus=coeffs(F),eModulus=hdata,paidOriginalWeightIdenticallyZero=ex.name,allOriginalFibersRetained=True,excluded=True)
  results.append(r);say(stage='new_J19_F20_named_original_paid_unit_zero',**r)
fibers=[('B2',[8,5,1]),('C2',[2,5,1]),('C15_F8',[-1024,-3712,-4640,-3128,-1304,-334,-39,4,1]),('G8',[512,512,144,1152,2128,1540,548,98,7])]
full_low=P([1])
for label,arr in fibers:full_low*=P(arr)
full_low=full_low/full_low[full_low.degree()]
assert full_low.degree()==20
assert digest(coeffs(full_low))['sha256']=='e9e95ffbded65cad45b8571d3f2807d9f6ba3cb5b1ae0dca6e20b6633c5ff83c'
say(stage='new_J19_complete_F20_original_norm_cover',coefficients=coeffs(full_low),QQDegree=20,exactPartitionSourceSHA256='4acc723381e1915bbfcc7d5c58cde813e2066f1fc08d4bc8f5d937423aada1fb',partitionRun=45994625232,partitionWasBeforeUnrelatedAPIError=True,allOriginalNormZeroFibersIncluded=True,claimExcluded=False)
for label,arr in fibers:
 ff=P(arr);cc,factors=ff.factor();back=P([cc])
 for factor,multiplicity in factors:back*=factor**int(multiplicity)
 assert back==ff
 say(stage='new_J19_F20_exact_entire_QQ_factor_cover',label=label,polynomial=arr,factors=[dict(coefficients=coeffs(f),multiplicity=int(m)) for f,m in factors],completeProductActuallyVerified=True,claimExcluded=False)
 for j,(factor,multiplicity) in enumerate(factors):process(factor,label+'/'+str(j))
closed=bool(results) and all(r['excluded'] for r in results)
signal.alarm(0)
say(stage='new_J19_F20_all_remaining_low_original_QQ_fibers_return_complete',sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),entireInitialNormZeroFibers=fibers,completeActualSplits=splits,originalFiniteReturns=results,allF20OriginalNormZeroFibersExcluded=closed,allNonunitBranchesRetained=True,originalDOnlyUsedAfterExactQQCombinationReturn=True,noModularMembershipLift=True,wholeJ19Excluded=False,claimExcluded=closed,peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
