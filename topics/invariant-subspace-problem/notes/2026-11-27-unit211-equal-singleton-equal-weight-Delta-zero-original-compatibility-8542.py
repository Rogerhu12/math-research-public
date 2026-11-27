#!/usr/bin/env python3
"""New Delta=0 original equal-weight h=k face: both affine compatibility rows.
No Delta inverse and no old D!=0 equal-weight theorem. Keep all leading-zero
fibers and return fixed QQ Q-projections of the ORIGINAL compatibility ideal.
180s/4GiB. This is a new boundary input, not a replay of Delta!=0 resultants.
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

# Exact ORIGINAL affine rows in the unknowns (1,f,t).
rowP=[Pc,Pf,bc*Q*Phi]
rowN=[NC,NF,bc*Q*S*xi]
assert [S*xi*rowP[j]-Phi*rowN[j] for j in range(3)]==[F,-Delta,R()]
assert [Pf*rowN[j]-NF*rowP[j] for j in range(3)]==[Tnum,R(),-bc*Q*Delta]
say("new_equal_value_equal_weight_Delta_zero_original_affine_compatibility",
    originalRowP=["Pc","Pf","bc*Q*Phi"],
    originalRowN=["NC","NF","bc*Q*S*xi"],
    fullBothCoefficientIdentitiesActuallyReturned=True,
    necessaryOriginalRows=["Delta","F","Tnum"],
    noDeltaT0PfOrNormInverse=True,oldDNonzeroTheoremNotImported=True)
def profile(pp):
 ss=str(pp).encode()
 return dict(degrees_lambda_Q=list(map(int,pp.degrees())),
             totalDegree=int(pp.total_degree()),terms=len(pp.to_dict()),
             bytes=len(ss),sha256=hashlib.sha256(ss).hexdigest())
base_atoms=[("A2",A.n),("B3",B.n),("Q",Qp),("rho_squared",disc.n)]
paid_atoms=base_atoms+[("lambda",Lp),("original_bc",bc.n),
                      ("original_P02",P02.n),("previous_whole_S_zero_excluded",S.n)]
def audit_den(pp):
 rr=pp
 for name,atom in base_atoms:
  while rr:
   gg=rr.gcd(atom)
   if gg.total_degree()==0:break
   out=rr/gg;assert out*gg==rr;rr=out
 assert rr.total_degree()==0
def primitive(pp):
 rr=pp;product=oneP;removed=[]
 for name,atom in paid_atoms:
  count=0
  while rr:
   gg=rr.gcd(atom)
   if gg.total_degree()==0:break
   out=rr/gg;assert out*gg==rr;rr=out;product*=gg;count+=1
  if count:removed.append(dict(originalUnit=name,gcdLoops=count))
 assert rr*product==pp
 if rr:
  scalar=rr.coefficient(0);rr=rr/scalar
  assert rr*scalar*product==pp
 return rr,removed
def factored(pp):
 if not pp:return dict(zero=True)
 content,factors=pp.factor();back=ctx.constant(content);data=[]
 for ff,power in factors:
  back*=ff**int(power);item=dict(power=int(power),profile=profile(ff))
  ss=str(ff)
  if len(ss.encode())<=8192:item["polynomial"]=ss
  data.append(item)
 assert back==pp
 return dict(content=str(content),factors=data,fullQQProductVerified=True)
cores={}
for name,rr in [("Delta",Delta),("F",F),("Tnum",Tnum)]:
 audit_den(rr.d);cc,removed=primitive(rr.n);cores[name]=cc
 say("new_Delta_zero_equal_weight_original_compatibility_core",
     name=name,rawNumerator=profile(rr.n),primitive=profile(cc),
     factorization=factored(cc),onlyPaidOriginalRemoval=removed,
     originalDeltaWasNotRemoved=True,claimExcluded=False)
gall=cores["Delta"].gcd(cores["F"]).gcd(cores["Tnum"])
say("new_Delta_zero_equal_weight_original_curve_gcd",
    profile=profile(gall),factorization=factored(gall),
    noEmptinessFromMultivariateGcd=True,claimExcluded=False)
from flint import fmpq_poly
qzero=fmpq_poly([]);qone=fmpq_poly([1])
def univariate(pp):
 assert all(int(m[1])==0 for m in pp.to_dict())
 cc=[fmpq(0)]*(int(pp.degrees()[0])+1) if pp else []
 for m,a0 in pp.to_dict().items():cc[int(m[0])]=fmpq(a0)
 return fmpq_poly(cc)
def qprofile(pp):
 co=[str(cc) for cc in pp.coeffs()]
 bb=json.dumps(co,separators=(",",":")).encode()
 ans=dict(degree=int(pp.degree()),bytes=len(bb),sha256=hashlib.sha256(bb).hexdigest())
 if len(bb)<=8192:ans["coefficients"]=co
 return ans
def coeffq(pp,j):
 return ctx.from_dict({(int(m[0]),0):v for m,v in pp.to_dict().items() if int(m[1])==j})
def sylvester(aa,bb):
 m,n=int(aa.degrees()[1]),int(bb.degrees()[1])
 assert m>0 and n>0
 rows=[]
 for pp,degree,shifts in [(aa,m,n),(bb,n,m)]:
  coeffs=[coeffq(pp,j) for j in range(degree+1)]
  assert sum((v*Qp**j for j,v in enumerate(coeffs)),zeroP)==pp
  for s in range(shifts):
   row=[zeroP]*(m+n)
   for j,v in enumerate(coeffs):row[j+s]=v
   assert sum((v*Qp**j for j,v in enumerate(row)),zeroP)==pp*Qp**s
   rows.append(row)
 assert len(rows)==m+n
 return m+n
cover=qzero;tags=[];inputs=[];labels=[]
def add_input(label,rr):
 global cover,tags
 cc,removed=primitive(rr);pp=univariate(cc)
 gg,aa,bb=cover.xgcd(pp)
 assert aa*cover+bb*pp==gg
 tags=[aa*t for t in tags]+[bb];inputs.append(pp);labels.append(label)
 assert sum((t*f for t,f in zip(tags,inputs)),qzero)==gg
 cover=gg
 say("new_Delta_zero_equal_weight_actual_QQ_compatibility_cover",
     label=label,input=qprofile(pp),onlyPaidOriginalRemoval=removed,
     currentCover=qprofile(cover),allUnivariateBezoutProductsVerified=True,
     noOriginalParameterLeadingZeroFiberDiscarded=True,claimExcluded=False)
for name,pp in cores.items():
 if pp and int(pp.degrees()[1])==0:
  add_input("original_scalar_"+name,pp)
  if cover.degree()==0:break
if cover.degree()!=0:
 for na,nb in [("Delta","F"),("Delta","Tnum"),("F","Tnum")]:
  aa,bb=cores[na],cores[nb]
  if not aa or not bb or min(int(aa.degrees()[1]),int(bb.degrees()[1]))<=0:continue
  common=aa.gcd(bb)
  if common.total_degree()>0:
   say("new_Delta_zero_equal_weight_pair_common_curve_retained",
       pair=[na,nb],common=profile(common),claimExcluded=False);continue
  order=sylvester(aa,bb)
  say("new_Delta_zero_equal_weight_fixed_QQ_projection_begin",
      pair=[na,nb],fixedOrder=order,allOriginalRowsReconstructed=True,
      allLeadingZeroFibersRetained=True,claimExcluded=False)
  rr=aa.resultant(bb,"Q");assert rr
  say("new_Delta_zero_equal_weight_fixed_QQ_projection_complete",
      pair=[na,nb],fixedOrder=order,rawProjection=qprofile(univariate(rr)),
      noUncomputedOriginalCoefficientCertificateClaim=True,claimExcluded=False)
  add_input("Res_Q_"+na+"_"+nb,rr)
  if cover.degree()==0:break
factor_data=[]
if cover:
 cover=cover/cover[cover.degree()]
 ct,factors=cover.factor();back=fmpq_poly([ct])
 for ff,power in factors:
  back*=ff**int(power);factor_data.append(dict(power=int(power),profile=qprofile(ff)))
 assert back==cover
signal.alarm(0)
say("new_Delta_zero_equal_weight_original_compatibility_input_complete",
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    actualOriginalDomain="h=k!=1,b=c,Delta=0",
    lambdaCover=qprofile(cover),fullQQFactors=factor_data,
    actualProjectionNames=labels,allOriginalAffineHeadsRetained=True,
    entireOriginalDeltaZeroEqualWeightExcluded=bool(cover) and cover.degree()==0,
    fullMeanAndHighestReturnStillNeededIfNonconstantCover=bool(cover) and cover.degree()>0,
    noFullOriginalFinitePointExclusionUnlessUnitReturned=True,
    ordinaryISPClaim=False,peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
