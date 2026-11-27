#!/usr/bin/env python3
"""New invariant weight-coordinate original system on h=k!=1, Delta!=0.
All eight original conditions are paired through the TWO actual singleton
rows; no single quadratic-field equation is split into coefficients.
H=bc*Delta, no D, T0, Pf, S or norm inverse. 180s/4GiB.
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
ctx=fmpq_mpoly_ctx.get(("lam","u","Q"),"lex")
Lp,up,Qp=ctx.gens();zeroP=ctx.constant(0);oneP=ctx.constant(1)
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
lam,u,Q=map(R,(Lp,up,Qp));disc=1-Q
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
xi=B/A;ell=A**3/(B*B);T=A*A/B;w=lam-1-T
hh=1+xi;S=2*xi+3-2*lam;eta=xi+3-2*lam
p=E(1,1);q=p.conj()
b=E(ell/2,(u-ell)/(2*disc));c=b.conj();a=E(1-ell)
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
    parameters=["lambda","u","Q"],quadraticSymbol="rho^2=1-Q",
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
 return dict(degrees_lambda_u_Q=list(map(int,pp.degrees())),
             totalDegree=int(pp.total_degree()),terms=len(pp.to_dict()),
             bytes=len(ss),sha256=hashlib.sha256(ss).hexdigest())
physical_atoms=atoms+[("lambda",Lp),("original_bc",bc.n),
                      ("original_P02",P02.n),("chart_Delta_nonzero",Delta.n)]
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
say("complete_equal_singleton_invariant_weight_original_input",
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    eightScalarRows={name:profile(pp) for name,pp in allcores.items()},
    linearMeanCombination=profile(Lcore),
    DeltaZeroRetainedSeparatelyByOriginalMonicQuartic=True,
    allOtherOriginalWeightFacesRetained=True,
    ordinaryISPClaim=False,claimExcluded=False,
    peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
