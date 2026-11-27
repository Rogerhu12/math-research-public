#!/usr/bin/env python3
"""NEW whole QQ[m]/(m^3-4m^2-6m+18) original K7 finite return.
All three conjugate weights are retained. The prior C3^2 ideal certificate
is an INPUT theorem, not recomputed. Build the entire original Gram anew,
then the genuine 48x35 degree-four rows, targeting 1,D,D^2.
Only if necessary, add the complete two-value moment consequence F6 and
a NEW degree-six 181x84 input. Every finite-algebra inverse multiplies to1;
every nonunit splits both whole factors. No numerical root choice.
180 seconds /4 GiB; only source, fixed parameters and small receipt.
"""
import json,time,hashlib,signal,resource
from pathlib import Path
from flint import fmpq_poly,fmpq
start=time.perf_counter();signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
P=lambda v=():fmpq_poly([fmpq(x) for x in v])
def coeffs(p):return [str(p[j]) for j in range(max(0,p.degree()+1))]
def say(**r):
 r['seconds']=time.perf_counter()-start
 print(json.dumps(r,separators=(',',':')),flush=True)
def digest(x):
 b=json.dumps(x,separators=(',',':')).encode()
 return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
class Nonunit(Exception):
 def __init__(self,g,why):self.g=g;self.why=why
class PhysicalZero(Exception):
 def __init__(self,name):self.name=name
results=[];splits=[]
def run_fiber(F,label):
 F=F/F[F.degree()];inverse_count=0;reduction_count=0
 class A:
  def __init__(self,v=0):
   nonlocal reduction_count
   if isinstance(v,A):self.p=v.p;return
   if not isinstance(v,fmpq_poly):v=P([v])
   qq,rr=divmod(v,F);assert qq*F+rr==v
   self.p=rr;reduction_count+=1
  def __bool__(self):return bool(self.p)
  def __neg__(self):return A(-self.p)
  def __add__(self,v):return A(self.p+A(v).p)
  __radd__=__add__
  def __sub__(self,v):return A(self.p-A(v).p)
  def __rsub__(self,v):return A(v)-self
  def __mul__(self,v):return A(self.p*A(v).p)
  __rmul__=__mul__
  def __eq__(self,v):return self.p==A(v).p
  def inv(self,why='actual finite original algebra inverse',paid=None):
   nonlocal inverse_count
   if not self:
    if paid is not None:raise PhysicalZero(paid)
    raise ZeroDivisionError(why)
   g,s,t=self.p.xgcd(F);assert s*self.p+t*F==g
   if g.degree()>0:raise Nonunit(g/g[g.degree()],why)
   out=A(s/g[0]);assert self*out==1
   inverse_count+=1;return out
  def __truediv__(self,v):return self*A(v).inv()
  def __rtruediv__(self,v):return A(v)*self.inv()
  def __pow__(self,n):
   if n<0:return self.inv()**(-n)
   out=A(1);v=self
   while n:
    if n&1:out=out*v
    v=v*v;n//=2
   return out
  def json(self):return coeffs(self.p)
 def unit(name,v):
  v=A(v)
  iv=v.inv('previously paid original quantity '+name,paid=name)
  assert v*iv==1
 m=A(P([0,1]));AA=m*m-6*m+6;BB=m*m-4*m+6;CC=m**3-10*m*m+36*m-36
 for name,v in [('complete_K7_parameter_m',m),('complete_K7_parameter_A',AA),('complete_K7_parameter_B',BB)]:unit(name,v)
 e=CC/(6*AA);k=2*AA/m;u=e+1;Q=e*k;V=u*k+2;d=1-Q
 assert 12*e*e*k*k-e*k**3+8*e*k*k-k**3-4*k*k-16*k-16==0
 theta=2*(m*m-6)/m
 assert theta*theta==(k+12)**2-96
 assert (theta+k+12)/4==m and m*(k+12-theta)/24==1
 for name,v in [('e',e),('k',k),('u',u),('Q',Q),('V',V),('1-Q',d)]:unit(name,v)
 ell=u*((k+2)**2-2*e*k)/(k*V)
 for name,v in [('ell',ell),('ell-u',ell-u)]:unit(name,v)
 bc=(ell*ell-(u-ell)**2/d)/4;unit('bc',bc)
 V2=2*u-ell*Q;T0=V2-2*u*u;P02=(2-3*u)*V2-Q*u+2*u**3
 J=2*u*(1-u)+ell*Q;Phi=T0+4*u-4+Q;Pf=T0*(J-Q);M=ell*V2-u*u
 for name,v in [('P02',P02),('Phi',Phi)]:unit(name,v)
 assert M==4*bc*d and Phi*(J-2*u*Q)-Pf==0
 assert m**3-4*m*m-6*m+18==0
 say(stage='new_K7_entire_cubic_original_weight_algebra',
     label=label,modulus=coeffs(F),QQDimension=int(F.degree()),
     allActualUnitInverseProductsOne=True,wholeConjugateFiberPreserved=True,
     noOld242DeterminantOr107BezoutReplayed=True,claimExcluded=False)
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
 def macaulay(equations,degree,targets,label0):
  # Each row is a literal monomial multiple of one of these ORIGINAL
  # equations or the explicitly proved complete HA/HB consequence F6.
  mons=sorted([(i,j,h) for i in range(degree+1) for j in range(degree+1-i)
               for h in range(degree+1-i-j)],key=lambda z:(sum(z),z[1],z[0],z[2]),reverse=True)
  assert mons[-1]==(0,0,0)
  n=len(mons);rawrows=[];rawproducts=[];labels=[];basis=[];tags=[];pivots=[]
  def vector(pp):
   assert pp.degree()<=degree
   return [pp.terms.get(mm,A()) for mm in mons]
  for name0,pp,bound in equations:
   assert pp.degree()<=bound
   for mm in sorted([m0 for m0 in mons if sum(m0)<=degree-bound],key=lambda z:(sum(z),z[1],z[0],z[2])):
    product=pp*Mpoly.from_terms([(mm,A(1))])
    rawproducts.append(product);rawrows.append(vector(product));labels.append([name0,list(mm)])
  say(stage='new_K7_cubic_original_Macaulay_input',path=label,label=label0,
      QQDimension=int(F.degree()),degree=degree,rows=len(rawrows),columns=n,
      allRowsAreOriginalProducts=True,claimExcluded=False)
  for idx,initial in enumerate(rawrows):
   row=initial[:];tag={idx:A(1)}
   for br,pv,bt in zip(basis,pivots,tags):
    cf=row[pv]
    if not cf:continue
    row=[row[j]-cf*br[j] for j in range(n)]
    for j,v in bt.items():tag[j]=tag.get(j,A())-cf*v
   if not any(row):continue
   pv=next(j for j,v in enumerate(row) if v)
   iv=row[pv].inv('actual full original Macaulay pivot')
   row=[v*iv for v in row];tag={j:v*iv for j,v in tag.items() if v}
   assert row[pv]==1 and all(not row[j] for j in pivots)
   basis.append(row);tags.append(tag);pivots.append(pv)
   if len(basis)==n:break
  returned=None;combination={};target=None;targetpoly=None
  for exponent,pp in targets:
   target0=vector(pp);rem=target0[:];actual={}
   for br,pv,bt in zip(basis,pivots,tags):
    cf=rem[pv]
    if not cf:continue
    rem=[rem[j]-cf*br[j] for j in range(n)]
    for j,v in bt.items():actual[j]=actual.get(j,A())+cf*v
   if any(rem):continue
   for j in range(n):
    assert sum((cf*rawrows[i][j] for i,cf in actual.items()),A())==target0[j]
   polynomial=sum((rawproducts[i].scale(cf) for i,cf in actual.items()),Mpoly())
   assert polynomial==pp
   returned=exponent;combination=actual;target=target0;targetpoly=pp;break
  cert=dict(modulus=coeffs(F),originalLabels=labels,rank=len(basis),pivots=pivots,
            Dpower=returned,combination={str(j):v.json() for j,v in combination.items()},
            target=[v.json() for v in target] if target is not None else None)
  record=dict(path=label,input=label0,QQDimension=int(F.degree()),rows=len(rawrows),columns=n,
              rank=len(basis),DpowerReturned=returned,
              allOriginalColumnProductsActuallyVerified=returned is not None,
              fullPolynomialCombinationActuallyVerified=returned is not None,
              actualInverseProducts=inverse_count,actualFiniteReductionProducts=reduction_count,
              certificate=digest(cert),excluded=returned is not None)
  say(stage='new_K7_cubic_entire_original_QQ_Macaulay_return',**record,wholeK7Excluded=False)
  return record
 equations=[(name,pp,deg) for name,pp,deg in zip(names,original,[2,2,2,2,3,3])]
 r=macaulay(equations,4,[(0,Mpoly(1)),(1,D),(2,D*D)],'four_original_quadratics_two_original_cubics')
 assert r['rows']==48 and r['columns']==35
 if r['excluded']:return r
 # Genuinely NEW input only if the original degree-four target is unresolved:
 # the complete original two-value moments, without choosing a norm inverse.
 w=u-ell;Kval=B3.scale(ell*ell)-(T*A2).scale(3*ell)+2*T**3
 F6=(Kval*Kval).scale(M)-(D**3).scale(4*w*w)
 # Exact polynomials in the auxiliary s=(ell*zeta-T)/u. Their coefficients
 # are three-variable original Gram polynomials over the ENTIRE cubic.
 def pa(a,b):
  n=max(len(a),len(b))
  return [(a[j] if j<len(a) else Mpoly())+(b[j] if j<len(b) else Mpoly()) for j in range(n)]
 def pn(a):return [-v for v in a]
 def pm(a,b):
  out=[Mpoly() for _ in range(len(a)+len(b)-1)]
  for i,x0 in enumerate(a):
   for j,y0 in enumerate(b):out[i+j]=out[i+j]+x0*y0
  return out
 def ps(a,c):return [v*c for v in a]
 def peq(a,b):
  n=max(len(a),len(b))
  return all((a[j] if j<len(a) else Mpoly())==(b[j] if j<len(b) else Mpoly()) for j in range(n))
 zeta=[T.scale(1/ell),Mpoly(u/ell)]
 v0=[T.scale(1/ell),Mpoly(w/ell)]
 v1=[Mpoly(),Mpoly(-1)]
 HA=pa(pa(ps(pm(zeta,zeta),Mpoly(ell*M)),ps(zeta,T.scale(-2*M))),
       [(T*T).scale(V2)-A2.scale(u*u)])
 HB=ps(pa(pa([B3],ps(v0,A2.scale(-2))),
          ps(pa(pm(v0,v0),pn(ps(pm(v1,v1),Mpoly(d)))),T)),Mpoly(u*u))
 q1=[-D,Mpoly(),Mpoly(M)]
 q2=[Kval,D.scale(-2*w)]
 assert peq(ps(q1,Mpoly(u*u)),ps(HA,Mpoly(ell)))
 assert peq(ps(q2,Mpoly(u*u)),pa(ps(HA,T.scale(ell)),ps(HB,Mpoly(ell*ell))))
 product=pa(ps(pm(q2,[Kval,D.scale(2*w)]),Mpoly(M)),
            ps(q1,(D*D).scale(4*w*w)))
 assert peq(product,[F6])
 assert F6.degree()<=6
 say(stage='new_K7_cubic_complete_original_HAHB_moment_consequence',
     exactConsequence='M*Kval^2-4*(u-ell)^2*D^3',
     allAuxiliarySOriginalHAHBAndEliminationProductsVerified=True,
     noDOrNormInverseUsedInConstruction=True,claimExcluded=False)
 r2=macaulay(equations+[('complete_HAHB_F6',F6,6)],6,
              [(0,Mpoly(1)),(1,D),(2,D*D),(3,D**3)],'new_complete_two_value_moment_input')
 assert r2['rows']==181 and r2['columns']==84
 return r2
def process(F,label):
 try:
  r=run_fiber(F,label);results.append(r)
 except Nonunit as ex:
  q,rem=divmod(F,ex.g)
  assert not rem and q*ex.g==F and 0<ex.g.degree()<F.degree()
  record=dict(path=label,factor=coeffs(ex.g),complement=coeffs(q),reason=ex.why,
              completeProductMultipliedBack=True,bothEntireFactorsRetained=True)
  splits.append(record);say(stage='new_K7_cubic_actual_nonunit_full_split',**record)
  process(ex.g,label+'/a');process(q,label+'/b')
 except PhysicalZero as ex:
  r=dict(path=label,modulus=coeffs(F),originalPaidQuantityIdenticallyZero=ex.name,
         wholeFiniteAlgebraIdentityVerified=True,excluded=True)
  results.append(r);say(stage='new_K7_cubic_original_paid_zero_entire_component',**r)
C3=P([18,-6,-4,1])
assert C3.degree()==3 and C3[3]==1
# Original cover supplied by the prior successful 148.816-second certificate.
say(stage='new_K7_entire_cubic_exact_input',
    polynomialAscending=[18,-6,-4,1],priorWholeK7IdealCover='C3(m)^2',
    priorRun=46075250765,priorSourceSHA256='0f9413d3cee49a1feacf46992cfbefd91c3c3f1ff41e1954cd0bd9795b2e78bf',
    allThreeComplexConjugatesRetained=True,oldCertificateNotReplayed=True,claimExcluded=False)
process(C3,'whole_C3')
closed=bool(results) and all(r['excluded'] for r in results)
say(stage='new_K7_entire_cubic_original_QQ_return_finished',
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    allFiniteReturns=results,allActualNonunitSplits=splits,
    fullCubicFiberExcluded=closed,
    physicalDUnitScope='current W distinct singleton value domain: D+ell*HA/u^2=bc*(hU-kU)^2',
    allWholeK7OriginalPointsExcluded=closed,
    priorC3SquareAndNewCubicReturnTogetherUsed=True,
    noModularLiftOrNumericalRootChoice=True,noDataCacheWritten=True,
    peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)
