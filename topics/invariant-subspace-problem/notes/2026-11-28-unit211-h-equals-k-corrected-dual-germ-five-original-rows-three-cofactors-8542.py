#!/usr/bin/env python3
"""NEW corrected dual-germ h=k original five-row input.
Use the corrected seven-variable R2 identity and full original N4(V).
Only the named A*B*Q*(1-Q)*Pf coordinate chart is used. No old
Delta, m, Phi, u+Q-1, scalar head or weight exclusion is imported.
All same-z rows and original scalar cofactor products are returned.
180 seconds / 4 GiB, self-contained. Old wrong sources stay frozen.
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
say("corrected_equal_singleton_true_original_coordinate_input",
 variables=["lambda","u","Q"],freeOriginalCoordinate="z=Q*t",
 fFromOriginalP1=True,NVExactAffineRow=True,
 actualNVIdentity="Pf*NV=Tnum-bc*Delta*z",
 PfOnlyNamedCoordinateChart=True,
 noDeltaInverse=True,allDeltaZeroFibersRetained=True,
 correctedOriginalIdentitySHA256="a7f1db4305a58c2e733c573158f746d5b4adc312090472de25e472c96ddfeaae",
 noOldGramOrProjectionReplayed=True,claimExcluded=False)

# Exact scalar forms after rho^2=1-Q and rho*(b-c)=u-ell.
# The paid scaling is R2/(2rho), W4/(4rho^2), O8/rho, and N1*.
I=(4*Q*(f-u)*(vn-Q*f)+bc*z*z+z*(4*bc*u*Q-ell*vn))
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


# Direct moment and full N4(V) returns; V=(1,w,h,h), h=1+xi.
# These use the original dual multiplication, not an E1 quotient.
assert a+w+ell*hh==lam
assert a+2*w+ell*hh*hh==2*lam*lam
assert a+3*w+ell*hh**3==4*lam**3
VV=vn/Q
tau_d_V=2*f+u*w+xi*VV
tau_d_V2=2*f+2*u*w+(2*xi+xi*xi)*VV
tau_V_DKV=2*f+2*xi*VV+2*hh*u*w+2*bc*xi*xi*z/Q
full_N4V=2*tau_d_V2-4*lam*tau_d_V+tau_V_DKV
assert Q*full_N4V==2*nv
# Direct centered third trace, using E0 and the true original N0.
Pj_over_3=(2*ell*Q*f+(T0-Q)*VV+(1-u)*T0-a*P02
           +bc*(4*u-4+2*Q)*z/Q)
assert Q*(Pj_over_3-w*P02)==Pf*f+Pc+bc*Phi*z
assert Pf*f+Pc+bc*Phi*z==U()
say("corrected_h_equals_k_complete_original_value_recovery",
    normalizationMomentsReturned=[1,2,3],
    trueFullN4VReturn="Q*N4(V)=2*NV",
    trueCenteredP1Return="Q*(Pj/3-w*P02)=Pf*f+Pc+bc*Phi*z",
    originalJetProductUsed=True,oldWrongRbarNotUsed=True,
    noAdditionalPaidWeightAssumption=True)

base_atoms=[("A",A.n),("B",B.n),("Q",Q.n),
            ("1-Q",disc.n),("Pf",Pf.n)]
assert all(p0 for _,p0 in base_atoms)
exact_divisions=0
def divide_exact(p0,q0):
 global exact_divisions
 v,r=divmod(p0,q0);assert not r and v*q0==p0
 exact_divisions+=1
 return v
def remove_named_base(p0):
 original=p0;removed=oneP;history=[]
 if not p0:return p0,removed,history
 for name,atom in base_atoms:
  count=0
  while True:
   g=p0.gcd(atom)
   if int(g.total_degree())==0:break
   p0=divide_exact(p0,g);removed*=g;count+=1
  if count:history.append({"coordinateUnit":name,"passes":count})
 assert p0*removed==original
 return p0,removed,history
seen_den=set()
def check_den(p0):
 key=str(p0)
 if key in seen_den:return
 rem,_,_=remove_named_base(p0)
 assert rem and int(rem.total_degree())==0,("outside_named_chart",str(rem))
 seen_den.add(key)
def info(p0,small=False):
 data=[[list(map(int,e)),str(c)] for e,c in sorted(p0.to_dict().items())]
 raw=json.dumps(data,separators=(",",":")).encode()
 value={"degrees_lambda_u_Q":list(map(int,p0.degrees())),
        "totalDegree":int(p0.total_degree()),"terms":len(data),
        "bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest()}
 if small and len(data)<=120:value["polynomial"]=str(p0)
 return value
def factor_back(p0):
 if not p0:return {"zero":True}
 scalar,factors=p0.factor();back=poly(scalar);records=[]
 for factor,power in factors:
  back*=factor**int(power)
  records.append({"multiplicity":int(power),**info(factor,True)})
 assert back==p0
 return {"scalar":str(scalar),"factors":records,"wholeProductReturned":True}
rows={}
def original_row(name,rr):
 assert len(rr.c)<=3
 den=oneP
 for cc in rr.c:
  check_den(cc.d)
  den=divide_exact(den,den.gcd(cc.d))*cc.d
 check_den(den)
 nums=[cc.n*divide_exact(den,cc.d) for cc in rr.c]
 nums+=[zeroP]*(3-len(nums))
 if any(nums):
  common=next(p0 for p0 in nums if p0)
  for p0 in nums:common=common.gcd(p0)
  _,removed,history=remove_named_base(common)
  out=[divide_exact(p0,removed) for p0 in nums]
  scalar=next(p0 for p0 in out if p0).coefficient(0)
  out=[p0/scalar for p0 in out];removed*=scalar
 else:
  removed=oneP;history=[];out=nums
 assert U([R(p0*removed,den) for p0 in out])==rr
 rows[name]=out
 say("corrected_h_equals_k_complete_same_z_row",
     name=name,columns=["1","z","z^2"],
     originalCoefficients=[info(p0) for p0 in out],
     finalClearingDenominator=info(den),
     removedOnlyNamedCoordinateUnits=history,
     wholeOriginalRowReturned=True,
     noOldDeltaOrHeadOrWeightUnitUsed=True)
for name,value in [("Rtrue",compact_R),("W",compact_W),("O",compact_O),
                   ("N1",compact_N),("NV",nv)]:
 original_row(name,value)
say("corrected_h_equals_k_all_five_original_rows",
    allSameOriginalZ=True,actualOriginalReconstructionReturns=15,
    allCoordinateDenominatorsReturned=True,
    originalMeanNecessityUsesTrueJetSquare=True)
all_results=[]
for names in [("Rtrue","W","O"),("Rtrue","W","N1"),("NV","Rtrue","W")]:
 aa,bb,cc=[rows[name] for name in names]
 tags=[bb[1]*cc[2]-bb[2]*cc[1],
       cc[1]*aa[2]-cc[2]*aa[1],
       aa[1]*bb[2]-aa[2]*bb[1]]
 det=sum((tag*row[0] for tag,row in zip(tags,(aa,bb,cc))),zeroP)
 assert all(sum((tag*row[j] for tag,row in zip(tags,(aa,bb,cc))),zeroP)
            ==(det if j==0 else zeroP) for j in range(3))
 core,removed,history=remove_named_base(det)
 if core:
  scalar=core.coefficient(0);core/=scalar;removed*=scalar
 assert core*removed==det
 record={"sourceRows":list(names),"allThreeOriginalCofactorProductsReturned":True,
         "determinant":info(det),"retainedNecessaryPolynomial":info(core),
         "onlyNamedCoordinateUnitRemoval":history,
         "cofactorDefinitions":[info(v) for v in tags],
         "entireDeltaZeroFibreRetained":True,
         "wholeCoordinateChartExcluded":bool(core) and int(core.total_degree())==0}
 say("corrected_h_equals_k_original_scalar_cofactor",**record)
 record["factorization"]=factor_back(core)
 say("corrected_h_equals_k_necessary_polynomial_exact_factors",
     sourceRows=list(names),**record["factorization"])
 all_results.append(record)
say("corrected_h_equals_k_five_rows_and_three_scalar_returns_finished",
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    sourceRows=["Rtrue","W","O","N1","NV"],
    coordinateChartOnly=["A","B","Q","1-Q","Pf"],
    wholeNamedChartExcluded=any(x["wholeCoordinateChartExcluded"] for x in all_results),
    allDeltaZeroAndOtherWeightZerosRetained=True,
    originalNecessaryScalarCount=sum(1 for x in all_results if x["determinant"]["terms"]),
    actualExactDivisionReturns=exact_divisions,
    noOldWrongSystemReplayed=True,noOldHeadUnitImported=True,
    noRecomputableCoefficientPayloadSaved=True,ordinaryISPClaim=False,
    peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
