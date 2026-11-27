#!/usr/bin/env python3
"""NEW full h=k chart: compact original means and N1, same free z=Q*t.
Use the proved complete scalar identities, not the old scaled Gram.
Pf is now a paid original unit, so solve P1 for f and keep original NV
as an affine z row. Delta is NEVER inverted: its whole zero face remains.
Fixed 3-column original polynomial cofactors keep every geometry head zero.
180 seconds / 4 GiB; no old projection or original Gram gate replay.
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
A=2*lam*lam-2*lam+1;B=4*lam**3-6*lam*lam+3*lam-1
xi=B/A;ell=A**3/(B*B);T=A*A/B;w=lam-1-T
hh=1+xi;S=2*xi+3-2*lam;eta=xi+3-2*lam
m=u-ell;a=1-ell;bc=(ell*ell-m*m/disc)/4
V2=2*u-ell*Q;T0=V2-2*u*u;J=2*u*(1-u)+ell*Q
Phi=T0+4*u-4+Q
P02=(2-3*u)*V2-Q*u+2*u**3
Pf=T0*(J-Q);G=lam*P02-(1-u)*T0
Pc=Q*P02*(ell+T)-G*T0
NF=(3-4*lam)*Q+J*xi*eta
NC=eta*(-G*xi+Q*w*u)
Delta=Phi*NF-S*xi*Pf
Tnum=Pf*NC-Pc*NF

def trim(v):
 while v and not v[-1]:v.pop()
 return v
class U:
 _isp_quotient_level=1
 def __init__(self,v=0):
  if isinstance(v,U):self.c=v.c[:];return
  self.c=trim([R(c) for c in v]) if isinstance(v,(list,tuple)) else ([R(v)] if R(v) else [])
 def __bool__(self):return bool(self.c)
 def __add__(self,v):
  v=U(v);n=max(len(self.c),len(v.c))
  return U([(self.c[j] if j<len(self.c) else R())+(v.c[j] if j<len(v.c) else R()) for j in range(n)])
 __radd__=__add__
 def __neg__(self):return U([-c for c in self.c])
 def __sub__(self,v):return self+-U(v)
 def __rsub__(self,v):return U(v)+-self
 def __mul__(self,v):
  v=U(v)
  if not self or not v:return U()
  out=[R() for _ in range(len(self.c)+len(v.c)-1)]
  for i,x in enumerate(self.c):
   for j,y in enumerate(v.c):out[i+j]=out[i+j]+x*y
  return U(out)
 __rmul__=__mul__
 def __truediv__(self,v):
  assert not isinstance(v,U);v=R(v);assert v
  return U([x/v for x in self.c])
 def __pow__(self,n):
  assert n>=0
  out=U(1)
  for j in range(n):out=out*self
  return out
 def __eq__(self,v):
  v=U(v)
  return len(self.c)==len(v.c) and all(x==y for x,y in zip(self.c,v.c))
z=U([0,1]);f=-(U(Pc)+bc*Phi*z)/Pf
assert Pf*f+bc*Phi*z+Pc==U()
nv=NF*f+bc*S*xi*z+NC
assert Pf*nv==U(Tnum)-bc*Delta*z
vn=J*f-G+bc*z
Wstar=T0+4*u*f;N=Q*Wstar-2*vn
say("new_equal_singleton_compact_original_full_chart_input",
 variables=["lambda","u","Q"],freeOriginalCoordinate="z=Q*t",
 fFromOriginalP1=True,NVExactAffineRow=True,
 actualNVIdentity="Pf*NV=Tnum-bc*Delta*z",
 PfPaidByEntireOriginalT0AndJQExclusions=True,
 noDeltaInverse=True,allDeltaZeroFibersRetained=True,
 compactOriginalIdentitySHA256="9ab0270fe53a0a6f169755f92f731e6cf636f1d9b7a9e12364ef487a01cdea6e",
 noOldGramOrProjectionReplayed=True,claimExcluded=False)

# Exact scalar forms after rho^2=1-Q and rho*(b-c)=u-ell.
# The paid scaling is R2/(2rho), W4/(4rho^2), O8/rho, and N1*.
I=((vn+a*u*Q)**2-2*u*Q*vn+2*a*u*u*Q*Q-4*a*u*Q*Q*f
   +bc*z*z+z*(4*bc*u*Q-ell*vn))
compact_R=I+(m/(2*disc))*z*N
compact_W=(2*bc*Q*Q*ell*T0-ell*vn*vn-(ell/(4*disc))*N*N
 +(m/disc)*vn*N+8*bc*Q*f*vn+4*bc*bc*z*z
 +8*bc*bc*Q*(u-1)*z-2*bc*ell*z*vn+(bc*m/disc)*z*N)
Sred=2*ell*vn-(m/disc)*N;Dred=-2*m*vn+ell*N
compact_O=(32*bc*bc*a*Q*Q*disc*(u-1)+4*bc*Q*disc*Sred
 +32*bc*bc*Q*disc*vn-64*bc*bc*Q*Q*disc*f
 +4*bc*Q*(1-u+2*f)*Dred-Sred*Dred
 -8*bc*bc*m*z*z-16*bc*bc*Q*z*(m*(u-1)+ell*disc)+8*bc*bc*z*N)
alpha=ell*(1-u)-m;beta_rho=ell*disc-m*(1-u)
Av=(2*u-1)*ell+3*m;Bu_rho=(2*u-1)*m+3*ell*disc
compact_N=(alpha*(4*disc*vn*vn+N*N)+4*beta_rho*vn*N
 +8*bc*disc*Q*vn*Wstar-24*bc*disc*Q*Q*f*Wstar
 +16*a*bc*disc*Q*Q*(u-1)*Wstar+64*bc*disc*Q*Q*u*f*f
 -32*bc*disc*Q*u*f*vn+16*bc*disc*Q*Q*(1+a)*T0*f
 +16*bc*disc*Q*(a*Q-T0)*vn+4*bc*disc*Av*z*vn
 -2*bc*Bu_rho*z*N+16*bc*bc*disc*Q*z*(2*f+T0-a*Q)
 -8*u*bc*bc*disc*z*z-16*bc*disc*Q*Q*lam*w*P02)
assert all(len(v.c)<=3 for v in [compact_R,compact_W,compact_O,compact_N])
assert len(nv.c)<=2

paid_atoms=[
 ("A",A.n),("B",B.n),("Q",Q.n),("rho_squared",disc.n),
 ("lambda",lam.n),("u",u.n),("u_minus_one",(u-1).n),
 ("bc",bc.n),("ell",ell.n),("u_minus_ell",m.n),
 ("P02",P02.n),("S",S.n),("T0",T0.n),
 ("J_minus_Q",(J-Q).n),("Phi",Phi.n),
 ("u_plus_Q_minus_one",(u+Q-1).n)
]
assert all(pp for _,pp in paid_atoms)
denominator_cache=set()
def strip_paid(pp):
 original=pp;product=oneP;records=[]
 if not pp:return pp,product,records
 for name,atom in paid_atoms:
  count=0
  while True:
   gg=pp.gcd(atom)
   if gg.total_degree()==0:break
   nn=pp/gg;assert nn*gg==pp;pp=nn;product*=gg;count+=1
  if count:records.append(dict(originalUnit=name,gcdLoops=count))
 assert pp*product==original
 return pp,product,records
def audit_den(pp):
 key=str(pp)
 if key in denominator_cache:return
 assert pp
 rem,product,records=strip_paid(pp)
 assert rem.total_degree()==0,("unpaid denominator",str(rem))
 denominator_cache.add(key)
def profile(pp,small=False):
 data=[[list(map(int,mm)),str(cc)] for mm,cc in sorted(pp.to_dict().items())]
 raw=json.dumps(data,separators=(",",":")).encode()
 out=dict(degrees_lambda_u_Q=list(map(int,pp.degrees())),
          totalDegree=int(pp.total_degree()),terms=len(data),
          bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
 if small and len(raw)<=8192:out["coefficients"]=data
 return out
rows={}
def primitive_row(name,rr):
 for cc in rr.c:audit_den(cc.d)
 den=oneP
 for cc in rr.c:
  gg=den.gcd(cc.d);den=(den/gg)*cc.d
 audit_den(den)
 nums=[]
 for cc in rr.c:
  mul0=den/cc.d;assert mul0*cc.d==den;nums.append(cc.n*mul0)
 nums+= [zeroP]*(3-len(nums))
 if not any(nums):
  rows[name]=nums
  say("new_compact_h_equals_k_zero_original_row",name=name,
      allDeltaZeroFibersRetained=True,claimExcluded=False)
  return
 common=next(p for p in nums if p)
 for pp in nums:common=common.gcd(pp)
 residual,removed,history=strip_paid(common)
 nums2=[pp/removed for pp in nums]
 assert all(x*removed==y for x,y in zip(nums2,nums))
 scalar=next(p for p in nums2 if p).coefficient(0)
 nums2=[pp/scalar for pp in nums2];removed*=scalar
 rebuilt=U([R(pp*removed,den) for pp in nums2])
 assert rebuilt==rr
 rows[name]=nums2
 say("new_compact_h_equals_k_complete_original_three_column_row",
     name=name,columns=["1","z","z^2"],
     sameOriginalVariable="z=Q*t",coefficientProfiles=[profile(p,True) for p in nums2],
     originalDenominator=profile(den),paidRemoved=history,
     allOriginalReconstructionProductsReturned=True,
     noDeltaOrGeometryNormInverse=True,claimExcluded=False)
for name,value in [("R",compact_R),("W",compact_W),("O",compact_O),
                   ("N1",compact_N),("NV",nv)]:
 primitive_row(name,value)
say("new_compact_h_equals_k_all_original_mean_N1_NV_rows_complete",
    fourOriginalQuadraticsAndOriginalNV=True,
    allThreeIndividualMeansEquivalentByPaidBcQRhoEll=True,
    noIndividualSpectralNPExhaustionClaim=True,
    actualDistinctCoefficientDenominators=len(denominator_cache),
    allDeltaZeroAndLeadingZeroFibersRetained=True,claimExcluded=False)
def cofactor(names):
 aa,bb,cc=[rows[name] for name in names]
 tags=[bb[1]*cc[2]-bb[2]*cc[1],
       cc[1]*aa[2]-cc[2]*aa[1],
       aa[1]*bb[2]-aa[2]*bb[1]]
 det=sum((tag*row[0] for tag,row in zip(tags,[aa,bb,cc])),zeroP)
 assert all(sum((tag*row[j] for tag,row in zip(tags,[aa,bb,cc])),zeroP)
            ==(det if j==0 else zeroP) for j in range(3))
 say("new_compact_h_equals_k_original_three_column_product_returned",
     originalRows=names,allThreeConstantColumnsActuallyReturned=True,
     rawDeterminant=profile(det),claimExcluded=False)
 if not det:
  say("new_compact_h_equals_k_identically_zero_original_cofactor",
      originalRows=names,originalRowsRetained=True,claimExcluded=False)
  return None
 core,removed,history=strip_paid(det)
 scalar=core.coefficient(0);core=core/scalar;removed*=scalar
 assert core*removed==det
 say("new_compact_h_equals_k_complete_global_necessary_polynomial",
     originalRows=names,necessaryPolynomial=profile(core,True),
     paidOnlyRemovals=history,allOriginalProductsAndRemovalsActuallyReturned=True,
     includesEntireDeltaZeroFiber=True,noNewHeadInverse=True,
     wholeCurrentHEqualsKChartExcluded=(core.total_degree()==0))
 # Store only small exact new parameters; larger reconstructible certificates
 # are identified by the frozen source and digest, not retained as matrices.
 tagraw=json.dumps([[[list(map(int,mm)),str(cc)] for mm,cc in sorted(pp.to_dict().items())]
                   for pp in tags],separators=(",",":")).encode()
 say("new_compact_h_equals_k_original_three_column_certificate",
     originalRows=names,bytes=len(tagraw),sha256=hashlib.sha256(tagraw).hexdigest(),
     fullCoefficientProductsAlreadyReturned=True)
 return core
profiles=[]
for names in [["R","W","O"],["R","W","N1"],["NV","R","W"]]:
 core=cofactor(names)
 profiles.append(dict(originalRows=names,profile=None if core is None else profile(core)))
signal.alarm(0)
say("new_complete_h_equals_k_global_compact_original_three_column_return",
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    originalParameterSpace=["lambda","u","Q"],
    necessaryPolynomials=profiles,allOriginalSameZ=True,
    DeltaNeverInverted=True,allDeltaZeroFibersRetained=True,
    noOldScaledGramOrProjectionReplayed=True,
    remainingIndividualNPAndOtherValueConditionsStillRequired=True,
    noFiniteCandidateOrWholeExclusionClaim=True,ordinaryISPClaim=False,
    peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
