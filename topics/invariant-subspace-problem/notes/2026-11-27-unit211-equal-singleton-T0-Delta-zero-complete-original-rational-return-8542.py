#!/usr/bin/env python3
"""New original h=k, T0=Delta=0 rational candidate, with free Gram f.
Original affine identities force lambda=1/3,u=125/123 on this entire face.
Rebuild every original row and return the complete univariate QQ ideal.
No Delta or NF inverse. 120s/1GiB.
"""
import json,time,hashlib,signal,resource
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx
signal.alarm(120)
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
start=time.perf_counter()
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-start)
 print(json.dumps(kw),flush=True)
ctx=fmpq_mpoly_ctx.get(("lam","u","f"),"lex")
Lp,up,fp=ctx.gens();zeroP=ctx.constant(0);oneP=ctx.constant(1)
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
lam,u,f=map(R,(Lp,up,fp))
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

# The two global lambda identities were already returned by source 46c5885.
lam=R(fmpq(1,3));u=R(fmpq(125,123))

A=2*lam*lam-2*lam+1;B=4*lam**3-6*lam*lam+3*lam-1
xi=B/A;ell=A**3/(B*B);T=A*A/B;w=lam-1-T
Q=2*u*(1-u)/ell;disc=1-Q
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
assert T0==0 and Pf==0 and NF==0 and Delta==0
assert ell==R(fmpq(125,196)) and T==R(fmpq(-25,42))
assert xi==R(fmpq(-14,15)) and S==R(fmpq(7,15))
assert eta==R(fmpq(7,5)) and w==R(fmpq(-1,14))
assert Q==R(fmpq(-784,15129)) and Phi==R(fmpq(200,15129))
assert P02==R(fmpq(27,98))*u*Q and NC==u*Q/50
assert 98*Phi+25*Q==0
assert Pc==Q*P02*(ell+T)
for name,rr in [("lambda",lam),("A",A),("B",B),("Q",Q),("rhoSquared",disc),
                ("bc",bc),("P02",P02),("S",S),("Phi",Phi),("uMinusEll",u-ell)]:
 assert rr and rr.n.total_degree()==0 and rr.d.total_degree()==0,name
H=R(1);fnum=f;tnum=-P02*(ell+T)/(bc*Phi)
assert Pc+Pf*fnum+bc*Q*Phi*tnum==0
assert NC+NF*fnum+bc*Q*S*xi*tnum==0
W1=T0/2+2*u*fnum
W2=u*T0+lam*P02+(V2+2*u*u)*fnum-bc*Q*tnum
ivdiff=E(0,-1/(2*disc))
assert ivdiff*(q-p)==1
Xnum=c*q*ivdiff*(q*W1-E(W2))/(bc*Q)
Ynum=b*p*ivdiff*(E(W2)-p*W1)/(bc*Q)
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

from flint import fmpq_poly
actual=[("E1",E1.a),("EBe",EB.a),("EBo",EB.b),("N1",n1.a),
        ("NBe",NB.a),("NBo",NB.b),("PBe",PB.a),("PBo",PB.b)]
def qqrow(rr):
 assert rr.d.total_degree()==0
 out=[fmpq(0)]*(int(rr.n.degrees()[2])+1) if rr else []
 for ex,cc in rr.n.to_dict().items():
  assert int(ex[0])==0 and int(ex[1])==0
  out[int(ex[2])]=fmpq(cc)/rr.d.coefficient(0)
 return fmpq_poly(out)
original=[(name,qqrow(rr)) for name,rr in actual]
say("new_original_collision_T0_Delta_zero_same_Gram_all_rows",
    lambdaValue="1/3",uValue="125/123",Qvalue="-784/15129",
    freeOriginalParameter="f",
    allOriginalMomentE0N0P1NVIdentitiesReturned=True,
    bothSingletonGradientAndHighestTargetsRetained=True,
    coefficientPairsUseBothActualRowsAndRhoNonzero=True,
    originalRows=[dict(name=name,degree=int(pp.degree()),
                      coefficientsAscending=[str(cc) for cc in pp.coeffs()]) for name,pp in original],
    noDeltaNFOrUnpaidNormInverse=True,claimExcluded=False)
gg=fmpq_poly([]);tags=[];used=[]
for name,pp in original:
 new,aa,bb=gg.xgcd(pp)
 assert aa*gg+bb*pp==new
 tags=[aa*tt for tt in tags]+[bb];used.append((name,pp));gg=new
 check=fmpq_poly([])
 for tt,(_,qq) in zip(tags,used):check+=tt*qq
 assert check==gg
 say("new_original_collision_T0_Delta_zero_free_f_Bezout",
     newOriginalRow=name,degree=int(gg.degree()),allOriginalProductsReturned=True)
 if gg.degree()==0:break
if gg:
 scalar=gg[gg.degree()];gg=gg/scalar;tags=[tt/scalar for tt in tags]
check=fmpq_poly([])
for tt,(_,pp) in zip(tags,used):check+=tt*pp
assert check==gg
cert=dict(rows=[dict(name=name,coefficients=[str(cc) for cc in pp.coeffs()]) for name,pp in used],
          tags=[[str(cc) for cc in tt.coeffs()] for tt in tags],
          commonPolynomial=[str(cc) for cc in gg.coeffs()])
bbcert=json.dumps(cert,separators=(",",":")).encode()
say("new_original_collision_T0_Delta_zero_full_return_complete",
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    originalDomain="h=k!=1,T0=0,Delta=0",
    uniqueBaseCandidate=dict(lambdaValue="1/3",uValue="125/123"),
    allEightOriginalRowsRebuilt=True,
    originalRowsUsed=[name for name,pp in used],
    finalFreeFPolynomial=[str(cc) for cc in gg.coeffs()],
    entireOriginalFaceExcluded=gg.degree()==0,
    fullCertificate=cert if len(bbcert)<=12000 else None,
    certificateBytes=len(bbcert),certificateSHA256=hashlib.sha256(bbcert).hexdigest(),
    genericT0DeltaNonzeroAndOtherEqualValueFacesRemainOpen=True,
    ordinaryISPClaim=False,peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)
