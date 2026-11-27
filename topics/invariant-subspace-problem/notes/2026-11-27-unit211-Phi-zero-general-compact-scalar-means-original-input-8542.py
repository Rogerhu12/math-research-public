#!/usr/bin/env python3
"""NEW general Phi=0 monic rho-two input: two COMPACT scalar means.
This does not assemble the failed uniformly cleared original Gram.
The exact universal raw-Gram identities were already actually returned
in pure V8 BigInt source b770f2f4 (85a0057e git blob), in 12 ms:
 R2+rho Q^2(E1-b EB-c EC)-Q^2((b-c)t-a rho)E0=0;
 W4-8bc rho^2 Q^2(b EB+c EC)-4Q^2 E0 Corr+ell Q^2 E0^2=0.
Only the named original units Pf1 and Lnum are inverted.  Both compact
rows retain the same actual rho.  No norm inverse, full Gram expansion,
old cofactor, old resultant, or old failure replay occurs.
120 seconds / 1 GiB. Completed rows and every new core are saved exactly.
"""
import os,sys,json,time,hashlib,signal,resource,zlib,base64
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx
signal.alarm(120)
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
start=time.perf_counter()
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-start)
 print(json.dumps(kw),flush=True)
helper_path=Path(os.environ.get("ISP_MONIC_SIX_HELPER",
 str(Path(__file__).with_name("2026-11-27-unit211-monic-six-explicit-geometric-localization-helper-8542.py"))))
helper_text=helper_path.read_text()
assert hashlib.sha256(helper_text.encode()).hexdigest()=="5e162fa3adc0737bb152de5635e6956ca03267d055a6b33cea93c957628c96d6"
exec(compile(helper_text,str(helper_path),"exec"),globals())
ctx=fmpq_mpoly_ctx.get(("lam","x","y"),"lex")
Lp,xp,yp=ctx.gens();zeroP=ctx.constant(0);oneP=ctx.constant(1)
def poly(x):return x if hasattr(x,"to_dict") else ctx.constant(x)
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

lam,x,y=map(R,(Lp,xp,yp))
A2=2*lam*lam-2*lam+1;B3=4*lam**3-6*lam*lam+3*lam-1
b=(B3-A2*y)/(x*x*(x-y));c=(A2*x-B3)/(y*y*(x-y))
ell=b+c;diff=b-c;a=1-ell;bc=b*c
T=b*x+c*y;S=x+y+3-2*lam;ww=lam-1-T
Ahead=ell-1-2*diff*diff
Bhead=2*diff*(3-2*ell)
Chead=-(ell-1)*(2*ell-3)
assert b*x*x+c*y*y==A2
assert b*x*x*x+c*y*y*y==B3
assert ell*A2-T*T==bc*(x-y)**2
unit_atoms=[("x",x.n),("y",y.n),("x-y",(x-y).n),
 ("explicit_open_rho_head",Ahead.n),("b",b.n),("c",c.n),
 ("ell",ell.n),("b-c",diff.n),("S",S.n),("lambda",lam.n)]
paid_cache=set()
def strip_unit_product(pp):
 assert pp
 key=str(pp)
 if key in paid_cache:return
 rr=pp
 for name,atom in unit_atoms:
  while rr:
   gg=rr.gcd(atom)
   if gg.total_degree()==0:break
   nn=rr/gg;assert nn*gg==rr;rr=nn
 assert rr.total_degree()==0,("unpaid base denominator",str(rr))
 paid_cache.add(key)
def coefficient_audit(rr):
 rr=R(rr);strip_unit_product(rr.d)
alpha=Bhead/Ahead;beta=Chead/Ahead
coefficient_audit(alpha);coefficient_audit(beta)
stats=dict(multiplications=0,original_difference_coefficients=0)
cooperate_parameter_ring(R)
class K2:
 _isp_quotient_level=1
 __slots__=("coefficients",)
 def __init__(self,value=0):
  if isinstance(value,K2):self.coefficients=value.coefficients;return
  if isinstance(value,(list,tuple)):
   assert len(value)<=2
   cc=[R(z) for z in value]+[R(0)]*(2-len(value))
  else:cc=[R(value),R(0)]
  for z in cc:coefficient_audit(z)
  self.coefficients=tuple(cc)
 @classmethod
 def internal(cls,c0,c1):
  obj=object.__new__(cls);obj.coefficients=(c0,c1);return obj
 def __bool__(self):return any(z!=0 for z in self.coefficients)
 def __add__(self,o):
  if getattr(o,"_isp_quotient_level",0)>1:return NotImplemented
  o=K2(o);return K2.internal(*(a+b for a,b in zip(self.coefficients,o.coefficients)))
 __radd__=__add__
 def __neg__(self):return K2.internal(*(-a for a in self.coefficients))
 def __sub__(self,o):return self+-K2(o)
 def __rsub__(self,o):return K2(o)+-self
 def __mul__(self,o):
  if getattr(o,"_isp_quotient_level",0)>1:return NotImplemented
  o=K2(o);a,b=self.coefficients;c,d=o.coefficients
  raw0,raw1,raw2=a*c,a*d+b*c,b*d
  out0,out1=raw0-raw2*beta,raw1-raw2*alpha
  assert raw0-out0-raw2*beta==0
  assert raw1-out1-raw2*alpha==0
  assert raw2-raw2==0
  stats["multiplications"]+=1;stats["original_difference_coefficients"]+=3
  return K2.internal(out0,out1)
 __rmul__=__mul__
 def __truediv__(self,o):
  if isinstance(o,int) and o!=0:
   return K2.internal(*(z/o for z in self.coefficients))
  raise TypeError("Only explicit base original-unit inverses are allowed")
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  ans,cur=K2(1),self
  while n:
   if n&1:ans=ans*cur
   n>>=1
   if n:cur=cur*cur
  return ans
 def __eq__(self,o):
  if getattr(o,"_isp_quotient_level",0)>1:return NotImplemented
  o=K2(o);return all(a==b for a,b in zip(self.coefficients,o.coefficients))
rho=K2([0,1]);p=1+rho;q=1-rho;Q=1-rho*rho
u=K2(ell)+K2(diff)*rho
V2=2*u-ell*Q;T0=V2-2*u*u;J=2*u*(1-u)+ell*Q
Phi=T0+4*u-4+Q
assert Phi==0
assert Ahead*rho*rho+Bhead*rho+Chead==0
assert T0==-Q-4*(u-1) and J-Q==-4*(u-1)**2
P02=(2-3*u)*V2-Q*u+2*u**3
assert P02==2*(u-1)*ell*Q
G=lam*P02+(u-1)*T0
Pf=T0*(J-Q)
Pc=Q*P02*(ell+T)-G*T0
Pf1=-4*(u-1)*T0
Pc1=2*ell*Q*Q*(ell+T)-(2*lam*ell*Q+T0)*T0
assert Pf==(u-1)*Pf1 and Pc==(u-1)*Pc1
Lnum=p*y-q*x
NF2r=2*rho*(3-4*lam)*Q+S*(2*u*Q*(x-y)+Lnum*J)
NT2r=bc*Q*S*Lnum
NC2r=(-G*S*Lnum+S*Q*T0*(x-y)/2+
 Q*ww*(2*rho*u*(3-2*lam+(x+y)/2)+(u-ell*Q)*(x-y)))

# Companion separate-factor wrapper also works for this two-dimensional K2.
atoms_path=Path(os.environ.get("ISP_MONIC_SIX_ATOMS_HELPER",
 str(Path(__file__).with_name("2026-11-27-unit211-monic-six-separate-geometric-exponents-helper-8542.py"))))
atoms_text=atoms_path.read_text()
assert hashlib.sha256(atoms_text.encode()).hexdigest()=="8fef06d13684d0a6ab9a463c38287cabc2793c9f92cd43dd43544a7c8f7d3408"
exec(compile(atoms_text,str(atoms_path),"exec"),globals())
class Adapter:pass
alg=Adapter();alg.K6=K2
def inverse_parameter(name,value):
 rr=R(value);assert rr
 strip_unit_product(rr.n);strip_unit_product(rr.d)
 return K2(R(1)/rr)
alg.inverse_parameter=inverse_parameter
loc=make_atom_localization(alg,[
 ("Pf1",Pf1,"Original Pf=(u-1)*Pf1; original Pf and u-1 are paid units"),
 ("Lnum",Lnum,"Lnum=2*rho*zeta; original rho and zeta are paid units")])
F=loc.Fraction
def profile(pp):
 return dict(degrees=list(map(int,pp.degrees())),terms=len(pp.to_dict()),
 totalDegree=int(pp.total_degree()),
 sha256=hashlib.sha256(str(sorted(pp.to_dict().items())).encode()).hexdigest())
def saved_polynomial(pp,label):
 payload=json.dumps({"variables":["lambda","x","y"],
  "terms":[[list(map(int,ex)),str(cc)] for ex,cc in sorted(pp.to_dict().items())]},
  separators=(",",":")).encode()
 compressed=zlib.compress(payload,9)
 dec=json.loads(zlib.decompress(compressed))
 assert ctx.from_dict({tuple(ex):fmpq(v) for ex,v in dec["terms"]})==pp
 say("new_exact_recoverable_polynomial",label=label,profile=profile(pp),
  encoding="base64+zlib+json",uncompressedBytes=len(payload),
  compressedBytes=len(compressed),payloadSha256=hashlib.sha256(payload).hexdigest(),
  data=base64.b64encode(compressed).decode(),
  completeReconstructionMultipliedBack=True)
# Q*t has a smaller denominator than t.  Q itself is not inverted here.
# At an original point:
# f=-Pc1/Pf1,
# z=Q*t=(NF2r*Pc1-NC2r*Pf1)/(Pf1*bc*S*Lnum).
ff=F(-Pc1,(1,0))
znum=(NF2r*Pc1-NC2r*Pf1)*inverse_parameter("b*c*S",bc*S)
zz=F(znum,(1,1))
# These are the two actual original scalar line identities, not coefficient
# zero tests of a value at one rho.
assert F(Pf1)*ff+F(Pc1)==0
assert F(NF2r)*ff+F(bc*S*Lnum)*zz+F(NC2r)==0
say("new_compact_general_Phi0_actual_original_lines",
 rhoDimension=2,baseVariables=["lambda","x","y"],
 namedAtoms=loc.provenance,
 fPoleOrders=list(ff.pole_orders),QtPoleOrders=list(zz.pole_orders),
 sameActualOriginalP1AndNVLines=True,noUniformGramScale=True,
 noGeometricNormInverse=True,statistics=dict(stats))
# N0 and E0 give Q*(bX+cY)=J*f-G+bc*z at the same original point.
vn=J*ff-G+bc*zz
wn2=F(Q*T0)+4*Q*u*ff-2*vn
rows={}
def clear_actual_compact_row(name,value):
 assert isinstance(value,F)
 rr=list(value.numerator.coefficients);den=oneP
 for cc in rr:
  coefficient_audit(cc);gg=den.gcd(cc.d);den=(den/gg)*cc.d
 strip_unit_product(den)
 nums=[]
 for cc in rr:
  qq=den/cc.d;assert qq*cc.d==den;nums.append(cc.n*qq)
 removed=[]
 for label,atom in unit_atoms:
  count=0
  while any(nums):
   gg=nums[0].gcd(nums[1]).gcd(atom)
   if gg.total_degree()==0:break
   nn=[pp/gg for pp in nums]
   assert all(q*gg==p for q,p in zip(nn,nums))
   nums=nn;count+=1
  if count:removed.append([label,count])
 if any(nums):
  scale=next(p for p in nums if p).coefficient(0)
  before=nums;nums=[p/scale for p in nums]
  assert all(q*scale==p for q,p in zip(nums,before))
 say("new_compact_original_same_rho_mean_row",name=name,
  originalIdentity=("R2=-rho*Q^2*(E1-b*EB-c*EC) modulo E0 and N0"
                    if name=="R2" else
                    "W4=8*b*c*rho^2*Q^2*(b*EB+c*EC) modulo E0 and N0"),
  coefficientProfiles=[profile(p) for p in nums],
  poles=list(value.pole_orders),geometricAtoms=list(loc.names),
  paidCoefficientDenominator=profile(den),paidGcdSourceLabels=removed,
  sameActualRhoKept=True,coefficientsNotAssertedSeparatelyZero=True,
  noIndividualEBECOrN1Claim=True,statistics=dict(stats))
 for j,p in enumerate(nums):saved_polynomial(p,name+"_rho_coefficient_"+str(j))
 rows[name]=nums
 return nums
I=((vn+F(a*u*Q))**2-2*u*Q*vn+F(2*a*u*u*Q*Q)
   -4*a*u*Q*Q*ff+bc*zz**2
   +zz*(F(4*bc*u*Q)-ell*vn))
R2=2*rho*I+diff*zz*wn2
clear_actual_compact_row("R2",R2)
W4=(F(8*bc*rho*rho*Q*Q*ell*T0)-4*ell*rho*rho*vn**2
    -ell*wn2**2+4*diff*rho*vn*wn2
    +32*bc*rho*rho*Q*ff*vn
    +16*bc*bc*rho*rho*zz**2
    +32*bc*bc*rho*rho*Q*(u-1)*zz
    -8*bc*ell*rho*rho*zz*vn+4*bc*diff*rho*zz*wn2)
clear_actual_compact_row("W4",W4)
aa,bb=rows["R2"],rows["W4"]
det=aa[0]*bb[1]-aa[1]*bb[0]
assert det==aa[0]*bb[1]-aa[1]*bb[0]
if det:
 core=det;removed=[]
 for name,atom in unit_atoms:
  count=0
  while core:
   gg=core.gcd(atom)
   if gg.total_degree()==0:break
   qq=core/gg;assert qq*gg==core;core=qq;count+=1
  if count:removed.append([name,count])
 cc=core.coefficient(0);before=core;core=core/cc;assert core*cc==before
 say("new_compact_actual_same_rho_two_row_determinant",
  determinant=profile(det),necessaryCore=profile(core),
  fixedTwoColumnEvaluationVector=[1,"rho"],paidGcdSources=removed,
  originalTemporaryHeadZeroFibersRetained=True,
  entireOpenChartExcluded=(core.total_degree()==0),
  statistics=dict(stats))
 saved_polynomial(core,"compact_original_R2_W4_necessary_core")
else:
 say("new_compact_same_rho_two_row_determinant_identically_zero",
     individualRowsStillActualNecessary=True,noNewExclusionClaim=True)
say("complete_new_compact_general_Phi0_scalar_mean_input",
 originalRows=["R2","W4"],sameOriginalRho=True,
 originalE0N0AndP1NVUsed=True,noN1OrIndividualEBECExhaustionClaim=True,
 noUniformClearedGram=True,noOldFailureReplay=True,
 noAlgebraicNormInverse=True,statistics=dict(stats),
 entirePhiFaceClaim=False,ordinaryISPClaim=False)
