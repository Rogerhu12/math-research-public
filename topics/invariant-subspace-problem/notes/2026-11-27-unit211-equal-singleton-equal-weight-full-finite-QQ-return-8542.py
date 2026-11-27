#!/usr/bin/env python3
"""New full QQ return on the four actual lambda factors of h=k,b=c,Delta!=0.
Use the complete constant quotient for every factor, true scalar QQ inverses,
all original eight rows and complete polynomial Bezout return. Every nonunit
constant factor is split into BOTH branches; no norm face is dropped.
180s/4GiB; no previous resultant calculation is rerun.
"""
import json,time,hashlib,signal,resource
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx
signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
start=time.perf_counter()
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-start)
 print(json.dumps(kw),flush=True)
ctx=fmpq_mpoly_ctx.get(("lam","Q"),"lex")
Lp,Qp=ctx.gens();zeroP=ctx.constant(0);oneP=ctx.constant(1)
def poly(x):return x if hasattr(x,'to_dict') else ctx.constant(x)
class R:
 def __init__(self,n=0,d=None,reduce=True):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  n=poly(n);d=oneP if d is None else poly(d);assert d
  if not n:self.n=zeroP;self.d=oneP;return
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
 def __truediv__(self,o):o=R(o);assert o;return self*R(o.d,o.n,False)
 def __rtruediv__(self,o):return R(o)/self
 def __pow__(self,n):
  return R(self.d**(-n),self.n**(-n),False) if n<0 else R(self.n**n,self.d**n,False)
 def __eq__(self,o):
  o=R(o)
  if self.n==o.n and self.d==o.d:return True
  return self.n*o.d==o.n*self.d

def cooperate(fn):
 def wrapped(self,other):
  if getattr(other,"_isp_quotient_level",0)>0:return NotImplemented
  return fn(self,other)
 return wrapped
for name in ("__add__","__radd__","__sub__","__rsub__","__mul__","__rmul__",
             "__truediv__","__rtruediv__","__eq__"):
 setattr(R,name,cooperate(getattr(R,name)))
lam,Q=map(R,(Lp,Qp));disc=1-Q
class E:
 _isp_quotient_level=1
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
  o=E(o);return E(self.a*o.a+disc*self.b*o.b,self.a*o.b+self.b*o.a)
 __rmul__=__mul__
 def __truediv__(self,o):
  assert not isinstance(o,E)
  o=R(o);assert o
  return E(self.a/o,self.b/o)
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  ans,cur=E(1),self
  while n:
   if n&1:ans=ans*cur
   n>>=1
   if n:cur=cur*cur
  return ans
 def __eq__(self,o):o=E(o);return self.a==o.a and self.b==o.b
 def conj(self):return E(self.a,-self.b)
A=2*lam*lam-2*lam+1;B=4*lam**3-6*lam*lam+3*lam-1
xi=B/A;ell=A**3/(B*B);u=ell;T=A*A/B;w=lam-1-T
hh=1+xi;S=2*xi+3-2*lam;eta=xi+3-2*lam
p=E(1,1);q=p.conj()
b=E(ell/2,(u-ell)/(2*disc));c=b.conj();a=E(1-ell)
assert not b.b and b==c and u==ell
bc=(ell*ell-(u-ell)**2/disc)/4
assert b+c==E(ell) and b*p+c*q==E(u) and b*c==E(bc)
assert p*q==E(Q) and (p-q)**2==E(4*disc)
V2=2*u-ell*Q;T0=V2-2*u*u;J=2*u*(1-u)+ell*Q
Phi=T0+4*u-4+Q
P02=(2-3*u)*V2-Q*u+2*u**3
Pf=T0*(J-Q);G=lam*P02-(1-u)*T0
Pc=Q*P02*(ell+T)-G*T0
NF=(3-4*lam)*Q+J*xi*eta
NC=eta*(-G*xi+Q*w*u)
Delta=Phi*NF-S*xi*Pf
F=S*xi*Pc-Phi*NC;Tnum=Pf*NC-Pc*NF
assert Pf*F+Phi*Tnum+Pc*Delta==0
assert NF*F+S*xi*Tnum+NC*Delta==0
H=bc*Delta;fnum=bc*F;tnum=Tnum/Q
W1P=T0*Delta/2+2*u*F
W2P=(u*T0+lam*P02)*Delta+(V2+2*u*u)*F-Tnum
ivdiff=E(0,-1/(2*disc))
assert ivdiff*(q-p)==1
Xnum=c*q*ivdiff*(q*W1P-E(W2P))/Q
Ynum=b*p*ivdiff*(E(W2P)-p*W1P)/Q
assert b*p*(q-p)*Xnum==E(bc)*(q*W1P-E(W2P))
assert c*q*(q-p)*Ynum==E(bc)*(E(W2P)-p*W1P)
rg=Xnum-a*p*H-c*tnum
sg=Ynum-a*q*H-b*tnum
AA=2*E(fnum)-2*b*Xnum-2*c*Ynum+E(2*bc*tnum)
rows=[[E(),E(),p*H,q*H],[E(),AA,rg,sg],
      [p*H,rg,E(),E(tnum)],[q*H,sg,E(tnum),E()]]
one=[E(1),E(),E(1),E(1)]
def va(x,y):return [a+b for a,b in zip(x,y)]
def vs(a,x):return [a*b for b in x]
def vm(x,y):return [x[0]*y[0],x[0]*y[1]+x[1]*y[0],x[2]*y[2],x[3]*y[3]]
def tau(x):return a*x[0]+x[1]+b*x[2]+c*x[3]
def DK(x):return [tau(vm(row,x)) for row in rows]
dv=DK(one);F2=tau(dv);Kd=DK(dv)
assert F2==E(2*fnum)
def mean(j):
 ee=2*tau(vm(rows[0],rows[1])) if j==1 else tau(vm(rows[j],rows[j]))
 return ee-2*Kd[j]-2*vm(dv,dv)[j]+2*F2*dv[j]
def N4(x):
 tv=tau(x)
 return (2*tau(vm(dv,vm(x,x)))-F2*tau(vm(x,x))
         -4*tv*tau(vm(dv,x))+2*F2*tv**2+tau(vm(x,DK(x))))
def P2(x):
 cc=va(x,vs(-tau(x),one));return tau(vm(vm(cc,cc),cc))
V=[E(1),E(w),E(hh),E(hh)]
assert tau(V)==E(lam)
assert tau(vm(V,V))==E(2*lam*lam)
assert tau(vm(vm(V,V),V))==E(4*lam**3)
assert N4(V)==0
assert mean(0)==0
H3=H**3
assert P2(rows[0])==E(P02*H3)
assert N4(rows[0])==E(2*lam*P02*H3)
x,y=rows[0],rows[1]
xc=va(x,vs(-tau(x),one));yc=va(y,vs(-tau(y),one))
Pj=3*tau(vm(vm(xc,xc),yc))
assert Pj==E(3*w*P02*H3)
Nv=N4(va(x,y))-N4(x)-N4(y)
n1=Nv-E(4*lam/3)*Pj
E1=mean(1);EB=mean(2);EC=mean(3)
NB=N4(rows[2])-E(2*lam*P02*hh*hh*H3)
NCrow=N4(rows[3])-E(2*lam*P02*hh*hh*H3)
PB=P2(rows[2])-E(P02*hh**3*H3)
PC=P2(rows[3])-E(P02*hh**3*H3)
assert not E1.b and not n1.b
assert EB.conj()==EC and NB.conj()==NCrow and PB.conj()==PC
say("new_equal_singleton_invariant_weight_original_system",
    parameters=["lambda","Q"],newOriginalFace="b=c, u=ell inside h=k and Delta!=0",quadraticSymbol="rho^2=1-Q",
    originalScale="H=bc*Delta",oldMomentParameterizationOnlyReused=True,
    E0N0P1AndOriginalNVActuallyVerified=True,
    sameOriginalBothSingletonHighestAndGradientTargets=True,
    bothOriginalRowsUsedForEachCoefficientPair=True,
    coefficientZeroEquivalenceUsesTwoActualRowsAndRhoNonzero=True,
    noDOrT0PfSNormInverse=True,claimExcluded=False)
atoms=[("A2",A.n),("B3",B.n),("Q",Qp),("rho_squared",disc.n)]
def audit_den(pp):
 assert pp;rr=pp
 for name,atom in atoms:
  while True:
   gg=rr.gcd(atom)
   if gg.total_degree()==0:break
   qq=rr/gg;assert qq*gg==rr;rr=qq
 assert rr.total_degree()==0,("unpaid coefficient denominator",str(rr))
def profile(pp):
 ss=str(pp).encode()
 return dict(degrees_lambda_Q=list(map(int,pp.degrees())),
             totalDegree=int(pp.total_degree()),terms=len(pp.to_dict()),
             bytes=len(ss),sha256=hashlib.sha256(ss).hexdigest())
physical_atoms=atoms+[("lambda",Lp),("original_bc",bc.n),
                      ("original_P02",P02.n),("chart_Delta_nonzero",Delta.n),("previous_whole_S_zero_excluded",S.n)]
def primitive(rr):
 rr=R(rr);audit_den(rr.d);pp=rr.n
 if not pp:return pp,[]
 original=pp;prod=oneP;hist=[]
 for name,atom in physical_atoms:
  count=0
  while True:
   gg=pp.gcd(atom)
   if gg.total_degree()==0:break
   old=pp;pp=pp/gg;assert pp*gg==old;prod=prod*gg;count+=1
  if count:hist.append(dict(name=name,count=count))
 scalar=pp.coefficient(0);pp=pp/scalar
 assert pp*scalar*prod==original
 return pp,hist
actual=[("E1",E1.a),("EBe",EB.a),("EBo",EB.b),("N1",n1.a),
        ("NBe",NB.a),("NBo",NB.b),("PBe",PB.a),("PBo",PB.b)]
allcores={}
for name,rr in actual:
 core,removed=primitive(rr);allcores[name]=core
 say("new_invariant_weight_complete_original_scalar_row",
     name=name,rawNumerator=profile(rr.n),primitive=profile(core),
     paidOnlyRemoval=removed,fullScaleProductVerified=True,
     allOriginalValuePairsRetained=True,claimExcluded=False)
Lmean=(u-ell)*EB.a+ell*disc*EB.b
Lcore,Lremoved=primitive(Lmean)
say("new_invariant_weight_actual_linear_mean_combination",
    originalCombination="(u-ell)*EBe+ell*(1-Q)*EBo",
    primitive=profile(Lcore),paidOnlyRemoval=Lremoved,
    noNonlinearTraceReplaced=True,claimExcluded=False)


CASES=[{"name":"lambda_factor_0","coefficients":["1","-2","3"],"power":1},{"name":"lambda_factor_1","coefficients":["1","-7","30","-90","208","-379","529","-548","380","-168","48"],"power":1},{"name":"lambda_factor_2","coefficients":["-1","1","1"],"power":2},{"name":"lambda_factor_3","coefficients":["-3","52","-392","1470","-414","-29126","199932","-829326","2534173","-6080694","11783324","-18678024","24316352","-25940944","22500320","-15651136","8547840","-3547392","1058304","-202752","18432"],"power":4}]

from flint import fmpq_poly
def QQ(v=()):return fmpq_poly([fmpq(x) for x in v])
QZ=QQ();QO=QQ([1])
class ConstantSplit(Exception):
 def __init__(self,g,h):self.g=g;self.h=h
case_results=[];split_records=[];inverse_count=0;division_count=0
def process_case(phi,label):
 global inverse_count,division_count
 phi=phi/phi[phi.degree()]
 class C:
  def __init__(self,v=0):
   if isinstance(v,C):self.p=v.p;return
   if isinstance(v,fmpq_poly):pp=v
   elif isinstance(v,(list,tuple)):pp=QQ(v)
   else:pp=QQ([v])
   qq,rr=divmod(pp,phi);assert qq*phi+rr==pp
   self.p=rr
  def __bool__(self):return bool(self.p)
  def __neg__(self):return C(-self.p)
  def __add__(self,v):return C(self.p+C(v).p)
  __radd__=__add__
  def __sub__(self,v):return self+-C(v)
  def __rsub__(self,v):return C(v)+-self
  def __mul__(self,v):return C(self.p*C(v).p)
  __rmul__=__mul__
  def __eq__(self,v):return self.p==C(v).p
  def inv(self):
   global inverse_count
   assert self
   gg,ss,tt=self.p.xgcd(phi)
   assert ss*self.p+tt*phi==gg
   if gg.degree()>0:
    qq,rr=divmod(phi,gg);assert not rr and qq*gg==phi
    assert 0<gg.degree()<phi.degree()
    raise ConstantSplit(gg,qq)
   out=C(ss/gg[0]);assert self*out==C(1);inverse_count+=1
   return out
  def data(self):return [str(v) for v in self.p.coeffs()]
 z=C();one=C(1)
 def trim(pp):
  while pp and not pp[-1]:pp.pop()
  return pp
 def add(aa,bb):
  cc=[z]*max(len(aa),len(bb))
  for j,v in enumerate(aa):cc[j]=cc[j]+v
  for j,v in enumerate(bb):cc[j]=cc[j]+v
  return trim(cc)
 def neg(aa):return [-v for v in aa]
 def sub(aa,bb):return add(aa,neg(bb))
 def mul(aa,bb):
  if not aa or not bb:return []
  cc=[z]*(len(aa)+len(bb)-1)
  for i,v in enumerate(aa):
   for j,w in enumerate(bb):cc[i+j]=cc[i+j]+v*w
  return trim(cc)
 def scale(aa,v):return trim([cc*v for cc in aa])
 def divrem(aa,bb):
  global division_count
  assert bb
  rr=aa[:];qq=[z]*max(0,len(aa)-len(bb)+1);iv=bb[-1].inv()
  while rr and len(rr)>=len(bb):
   shift=len(rr)-len(bb);cf=rr[-1]*iv
   qq[shift]=qq[shift]+cf
   for j,v in enumerate(bb):rr[j+shift]=rr[j+shift]-cf*v
   rr=trim(rr)
  qq=trim(qq);assert add(mul(qq,bb),rr)==aa;division_count+=1
  return qq,rr
 def xgcd(aa,bb):
  r0,r1=aa[:],bb[:];s0,s1=[one],[];t0,t1=[],[one]
  while r1:
   q0,r2=divrem(r0,r1)
   r0,r1=r1,r2;s0,s1=s1,sub(s0,mul(q0,s1));t0,t1=t1,sub(t0,mul(q0,t1))
   assert add(mul(s0,aa),mul(t0,bb))==r0
   assert add(mul(s1,aa),mul(t1,bb))==r1
  if not r0:return [],[],[]
  iv=r0[-1].inv();gg,ss,tt=scale(r0,iv),scale(s0,iv),scale(t0,iv)
  assert add(mul(ss,aa),mul(tt,bb))==gg
  return gg,ss,tt
 def from_mpoly(pp):
  if not pp:return []
  out=[z]*(int(pp.degrees()[1])+1)
  byq={}
  for ex,cc in pp.to_dict().items():
   il,iq=map(int,ex)
   if iq not in byq:byq[iq]=[fmpq(0)]*(int(pp.degrees()[0])+1)
   byq[iq][il]=fmpq(cc)
  for iq,cc in byq.items():out[iq]=C(QQ(cc))
  return trim(out)
 def pdata(pp):return [cc.data() for cc in pp]
 def small_profile(pp):
  blob=json.dumps(pdata(pp),separators=(",",":")).encode()
  r=dict(Qdegree=len(pp)-1,bytes=len(blob),sha256=hashlib.sha256(blob).hexdigest())
  if len(blob)<=8192:r["coefficients_Q_then_lambda"]=pdata(pp)
  return r
 try:
  unit_rows=[(name,from_mpoly(atom)) for name,atom in physical_atoms]
  for name,pp in unit_rows:
   if not pp:
    out=dict(case=label,lambdaDegree=int(phi.degree()),excluded=True,
             reason="an original physical unit is identically zero",
             originalUnit=name,allLambdaRootsRetained=True)
    case_results.append(out);say("new_equal_weight_whole_constant_factor_return",**out)
    return
  order=["EBo","N1","E1","EBe","NBo","NBe","PBo","PBe"]
  original={name:from_mpoly(allcores[name]) for name in order}
  gg=[];tags=[];used=[]
  for name in order:
   new,aa,bb=xgcd(gg,original[name])
   tags=[mul(aa,tt) for tt in tags]+[bb];used.append(name);gg=new
   actual=[]
   for tt,nn in zip(tags,used):actual=add(actual,mul(tt,original[nn]))
   assert actual==gg
   say("new_equal_weight_original_whole_factor_QQ_Bezout",
       case=label,lambdaDegree=int(phi.degree()),newOriginalRow=name,
       currentQDegree=len(gg)-1,allOriginalCoefficientProductsReturned=True,
       allLambdaRootsAndAllQHeadsRetained=True,claimExcluded=False)
   if len(gg)==1:break
  if not gg:
   out=dict(case=label,lambdaDegree=int(phi.degree()),excluded=False,
            reason="all returned original rows vanish in this full constant factor")
   case_results.append(out);say("new_equal_weight_whole_constant_factor_return",**out);return
  remaining=gg[:];removed=[];product=[one]
  for name,atom in unit_rows:
   loops=0
   while len(remaining)>1:
    common,_,_=xgcd(remaining,atom)
    if len(common)<=1:break
    quotient,rem=divrem(remaining,common);assert not rem
    atom_quot,atom_rem=divrem(atom,common);assert not atom_rem
    assert mul(common,quotient)==remaining and mul(common,atom_quot)==atom
    remaining=quotient;product=mul(product,common);loops+=1
   if loops:removed.append(dict(originalUnit=name,gcdLoops=loops))
  assert mul(product,remaining)==gg
  excluded=len(remaining)==1
  if excluded:assert remaining[0]*remaining[0].inv()==one
  cert=dict(lambdaFactor=[str(c0) for c0 in phi.coeffs()],
            originalRows={name:pdata(original[name]) for name in used},
            originalBezoutTags=[pdata(tt) for tt in tags],
            returnedGcd=pdata(gg),unitFactorProduct=pdata(product),
            retainedQPolynomial=pdata(remaining),paidRemoval=removed)
  blob=json.dumps(cert,separators=(",",":")).encode()
  out=dict(case=label,lambdaDegree=int(phi.degree()),excluded=excluded,
           originalRowsActuallyUsed=used,originalGcd=small_profile(gg),
           retainedQPolynomial=small_profile(remaining),paidUnitRemoval=removed,
           wholeOriginalCombinationAndUnitProductActuallyReturned=True,
           allLambdaRootsRetained=True,noScalarNormInvertedWithoutBezout=True,
           certificateBytes=len(blob),certificateSHA256=hashlib.sha256(blob).hexdigest())
  case_results.append(out);say("new_equal_weight_whole_constant_factor_return",**out)
 except ConstantSplit as ex:
  assert ex.g*ex.h==phi
  rec=dict(case=label,left=[str(c0) for c0 in ex.g.coeffs()],
           right=[str(c0) for c0 in ex.h.coeffs()],
           fullProductVerified=True,bothBranchesRetained=True)
  split_records.append(rec);say("new_equal_weight_actual_nonunit_constant_complete_split",**rec)
  process_case(ex.g,label+"/left");process_case(ex.h,label+"/right")
for case in CASES:process_case(QQ(case["coefficients"]),case["name"])
signal.alarm(0)
say("new_equal_value_equal_weight_all_finite_QQ_returns_complete",
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    cases=case_results,allConstantSplits=split_records,
    actualScalarInverseCount=inverse_count,actualQDivisionCount=division_count,
    entireOriginalEqualWeightDeltaNonzeroExcluded=bool(case_results) and all(r["excluded"] for r in case_results),
    actualDomain="h=k!=1,b=c,Delta!=0",DeltaZeroStillOpen=True,
    noOldDNonzeroWeightExclusionImported=True,ordinaryISPClaim=False,
    peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
