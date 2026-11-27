#!/usr/bin/env python3
"""New COMPLETE exact H8 constant-fiber original algebra.
Work in QQ[lambda]/H8 with every coefficient inverse returned by QQ xgcd;
obtain the actual same-rho F/G gcd, remove only rho,rho+-1 original poles,
then retain original monic ell2 and ALL E1/EB/EC/N1/NB/PB/NC/PC rows.
The complete finite algebra ideal is spanned by basis multiples of the
eight rows. A returned power of a TRUE same-point original unit excludes
the whole H8 fiber. No separate vanishing of extension coefficients.
No mod emptiness is promoted. 120s/1GiB.
"""
import os,json,time,hashlib,signal,resource
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx
signal.alarm(120)
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
start=time.perf_counter()
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-start)
 print(json.dumps(kw),flush=True)
def load_helper(env,name,sha):
 pp=Path(os.environ.get(env,str(Path(__file__).with_name(name))))
 ss=pp.read_text();assert hashlib.sha256(ss.encode()).hexdigest()==sha
 exec(compile(ss,str(pp),"exec"),globals())
load_helper("ISP_MONIC_SIX_HELPER",
 "2026-11-27-unit211-monic-six-explicit-geometric-localization-helper-8542.py",
 "5e162fa3adc0737bb152de5635e6956ca03267d055a6b33cea93c957628c96d6")
load_helper("ISP_RANK_ONE_GRAM_HELPER",
 "2026-11-27-unit211-rank-one-centered-value-original-gram-helper-8542.py",
 "41459fea3ff0419d8c9230a2f6093cc0b1bc5f528b6f2d2e714a4469f11e5c3e")
ctx=fmpq_mpoly_ctx.get(('lam','rho'),'lex')
Lp,rhop=ctx.gens();zeroP=ctx.constant(0);oneP=ctx.constant(1)
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

lam,rho=R(Lp),R(rhop)
p,q=1+rho,1-rho;Q=1-rho*rho
A2=2*lam*lam-2*lam+1
B3=4*lam**3-6*lam*lam+3*lam-1
gamma=A2**3/(B3*B3)
Snum=4*lam*lam-5*lam+2
# Base units: A2,B3 follow from the original h=1, D!=0 collision;
# Snum follows from the already-paid whole S=0 branch.
unit_atoms=[("lambda",lam.n),("rho",rho.n),("p",p.n),("q",q.n),
            ("A2",A2.n),("B3",B3.n),("S_original",Snum.n)]
paid_cache=set()
def strip_unit_product(pp):
 assert pp
 key=str(pp)
 if key in paid_cache:return
 r=pp
 for name,atom in unit_atoms:
  while r:
   g=r.gcd(atom)
   if g.total_degree()==0:break
   new=r/g;assert new*g==r;r=new
 assert r.total_degree()==0,("unpaid base denominator",str(r))
 paid_cache.add(key)
def coefficient_audit(rr):
 rr=R(rr);strip_unit_product(rr.d)
def base_inverse(rr):
 rr=R(rr);strip_unit_product(rr.n);strip_unit_product(rr.d)
 answer=1/rr;assert answer*rr==1
 return answer
C1=8*p*gamma*rho+6*p-Q
C0=-8*gamma*gamma*rho*rho-12*gamma*rho-4+Q
alpha=-C1/(2*p*p);beta=-C0/(2*p*p)
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
ell=K2([0,1])
v=original_rank_one_values(ell,lam,rho)
assert v["Phi"]==0
assert (-2*p*p*ell*ell+C1*ell+C0)==0
assert v["c"]==gamma and v["k"]==1+B3/A2
assert v["S"]==Snum/A2
assert v["b"]*0==0
# These are the exact original moments on the old collision chart, not a
# newly asserted exclusion of that chart.
a,b,c=(v[x] for x in ("a","b","c"))
w,k=v["w"],v["k"]
assert a+w+b+c*k==lam
assert a+2*w+b+c*k*k==2*lam*lam
assert a+3*w+b+c*k**3==4*lam**3
assert ell*A2-v["T"]**2==b*A2
Pf,Pc,NF,NC=(v[x] for x in ("Pf","Pc","NF","NC"))
f0=-Pc
t0=-(NF*f0+NC*Pf)*base_inverse(c*Q*v["S"]*v["zeta"])
assert Pf*f0+Pc*Pf==0
assert NF*f0+c*Q*v["S"]*v["zeta"]*t0+NC*Pf==0

gram=original_rank_one_cleared_gram(v,f0,t0,Pf)
assert gram["P1Residual"]==0
def profile(pp):
 return dict(degrees=list(map(int,pp.degrees())),terms=len(pp.to_dict()),
             totalDegree=int(pp.total_degree()),
             sha256=hashlib.sha256(str(sorted(pp.to_dict().items())).encode()).hexdigest())
say("original_Phi0_zn0_full_monic_ell_chart",
    previousChart="R150 original U-value atlas section 2.2, h=1 or k=1",
    baseParameters=["lambda","rho"],originalMonicVariable="ell",
    paidMonicLeading="-2*(1+rho)^2",
    oldParameterizationIsNotNew=True,
    collisionLabelsBothCoveredByOriginalBCExchange=True,
    originalMoments=True,originalP1=True,originalNVLine=True,
    oneActualGramScale="H=b*Pf",
    scaleUnitSource="original b!=0 and published T0*(J-Q)!=0",
    noNormInverse=True,noUnpaidInverse=True,statistics=dict(stats))
rows={}
def clear_original_row(name,kk):
 rr=list(K2(kk).coefficients)
 den=oneP
 for r in rr:
  coefficient_audit(r)
  gg=den.gcd(r.d);den=(den/gg)*r.d
 strip_unit_product(den)
 nums=[]
 for r in rr:
  quotient=den/r.d;assert quotient*r.d==den
  nums.append(r.n*quotient)
 removed=[]
 if any(nums):
  for uname,atom in unit_atoms:
   count=0
   while True:
    gg=nums[0].gcd(nums[1]).gcd(atom)
    if gg.total_degree()==0:break
    new=[n/gg for n in nums]
    assert all(a*gg==b for a,b in zip(new,nums))
    nums=new;count+=1
   if count:removed.append([uname,count])
  first=next(n for n in nums if n)
  scalar=first.coefficient(0)
  before_normalization=nums
  nums=[n/scalar for n in nums]
  assert all(n*scalar==a for n,a in zip(nums,before_normalization))
 say("same_original_ell_linear_row",name=name,
     coefficients=[profile(n) for n in nums],denominator=profile(den),
     paidBaseFactorsRemoved=removed,
     originalScalePower=2 if name in ("E1","EB","EC") else 3,
     noLeadingCoefficientDivided=True)
 return K2([R(n) for n in nums])
for name,raw in gram["equations"]():
 rows[name]=clear_original_row(name,raw)
say("all_eight_original_rows_complete",rows=list(rows),
    statistics=dict(stats),claimExcluded=False)
# Multiplication by the SAME ell preserves each actual original vanishing row.
# No assertion of freeness of the original solution scheme is needed.
for name in ("E1","EB","N1","NB","PB"):
 rows["ell:"+name]=ell*rows[name]
def paid_core(pp):
 removed=[]
 if not pp:return pp,removed
 for uname,atom in unit_atoms:
  count=0
  while True:
   gg=pp.gcd(atom)
   if gg.total_degree()==0:break
   new=pp/gg;assert new*gg==pp;pp=new;count+=1
  if count:removed.append([uname,count])
 scalar=pp.coefficient(0)
 normalized=pp/scalar;assert normalized*scalar==pp
 return normalized,removed

def actual_pair_core(left,right,target):
 aa,bb=rows[left].coefficients,rows[right].coefficients
 tt=target.coefficients
 det=aa[0]*bb[1]-aa[1]*bb[0]
 assert det
 na,nb=tt[0]*bb[1]-tt[1]*bb[0],aa[0]*tt[1]-aa[1]*tt[0]
 ca,cb=na/det,nb/det
 assert ca*det==na and cb*det==nb
 gd=ca.d.gcd(cb.d)
 den=(ca.d/gd)*cb.d
 qa,qb=den/ca.d,den/cb.d
 assert qa*ca.d==den and qb*cb.d==den
 tagA,tagB=ca.n*qa,cb.n*qb
 assert K2(R(den))*target==K2(R(tagA))*rows[left]+K2(R(tagB))*rows[right]
 core,removed=paid_core(den)
 return core

from math import gcd,lcm
from flint import nmod_poly,nmod_mpoly_ctx
H3=gram["H"]**3
specs=[
 ("F_cross_E1_EC","E1","EC",H3,
 "10868a19c5de665f9c4dc56a2f6e2c7196081de1e2a0fd9f74b3c1dbbc18ac23"),
 ("G_principal_N1_ell","N1","ell:N1",H3*(ell**3),
 "d23259f5b889511937e4b6d034a0eebccdae9e4f4f5f007e8d4dac89500ba879"),
 ("S_principal_E1","E1","ell:E1",H3,
 "e101f6ac2515d05096d8a0e23c14e427685d507d8a33b8ad59480f1482a088a9"),
 ("T_cross_E1_EB","E1","EB",H3,
 "1b9f8c1bb31a9c87d538b40e82134b7834d03aad87774ee07463e7936dec5c48")
]
def integer_core(pp):
 dd=1
 for aa in pp.to_dict().values():dd=lcm(dd,int(fmpq(aa).denominator))
 integral={}
 common=0
 for m,aa in pp.to_dict().items():
  xx=fmpq(aa)*dd;assert xx.denominator==1
  z=int(xx.numerator);integral[tuple(map(int,m))]=z;common=gcd(common,abs(z))
 assert common
 out=ctx.from_dict({m:fmpq(z//common) for m,z in integral.items()})
 scale=fmpq(dd,common)
 if out.coefficient(0)<0:out=-out;scale=-scale
 assert out==scale*pp
 assert all(fmpq(z).denominator==1 for z in out.to_dict().values())
 return out,scale
def coefficient_at(pp,index,exponent):
 return ctx.from_dict({tuple(0 if j==index else int(m[j]) for j in range(2)):a
                       for m,a in pp.to_dict().items() if int(m[index])==exponent})
cores={}
for name,left,right,target,sha in specs[:2]:
 cc=actual_pair_core(left,right,target)
 assert profile(cc)["sha256"]==sha
 zz,scale=integer_core(cc);cores[name]=zz
 lead=coefficient_at(zz,0,int(zz.degrees()[0]))
 say("fixed_original_integer_core",name=name,QQCore=profile(cc),
     integerCore=profile(zz),rationalScale=str(scale),
     scalarIdentityMultipliedBack=True,
     maximumIntegerCoefficientBits=max(abs(int(a)).bit_length() for a in zz.to_dict().values()),
     leadingLambdaPolynomialTerms=[[list(map(int,m)),str(a)] for m,a in sorted(lead.to_dict().items())],
     claimExcluded=False)
F,G=[cores[name] for name in ("F_cross_E1_EC","G_principal_N1_ell")]
from flint import fmpq_poly
import sys
H8_integer=fmpq_poly([1,-2,-4,25,-44,32,16,-48,32])
phi=H8_integer/32
assert phi.degree()==8 and phi.leading_coefficient()==1
QQzero=fmpq_poly([]);QQone=fmpq_poly([1])
counts={"QQ_phi_division_returns":0,"QQ_coefficient_inverse_returns":0,
        "rho_polynomial_division_returns":0,"rho_original_gcd_steps":0}
def qred(pp):
 qq,rr=divmod(pp,phi)
 assert qq*phi+rr==pp
 counts["QQ_phi_division_returns"]+=1
 return rr
class C:
 __slots__=("v",)
 def __init__(self,z=0):
  if isinstance(z,C):self.v=z.v
  elif isinstance(z,fmpq_poly):self.v=qred(z)
  else:self.v=fmpq_poly([fmpq(z)])
 def __bool__(self):return bool(self.v)
 def __add__(self,o):o=C(o);return C(self.v+o.v)
 __radd__=__add__
 def __neg__(self):return C(-self.v)
 def __sub__(self,o):return self+-C(o)
 def __rsub__(self,o):return C(o)+-self
 def __mul__(self,o):o=C(o);return C(self.v*o.v)
 __rmul__=__mul__
 def inverse(self):
  assert self
  if self.v.degree()==0:
   out=C(1/self.v[0]);assert out*self==1
   counts["QQ_coefficient_inverse_returns"]+=1
   return out
  gg,ss,tt=self.v.xgcd(phi)
  assert ss*self.v+tt*phi==gg
  assert gg.degree()==0,("nonunit exact H8 coefficient",str(gg))
  out=C(ss/gg[0]);assert out*self==1
  counts["QQ_coefficient_inverse_returns"]+=1
  return out
 def __truediv__(self,o):return self*C(o).inverse()
 def __rtruediv__(self,o):return C(o)*self.inverse()
 def __pow__(self,n):
  assert n>=0
  out=C(1);base=self
  while n:
   if n&1:out=out*base
   n//=2
   if n:base=base*base
  return out
 def __eq__(self,o):return self.v==C(o).v
def trim(cc):
 while cc and not cc[-1]:cc.pop()
 return cc
def padd(aa,bb):
 cc=[C(0) for _ in range(max(len(aa),len(bb)))]
 for i,vv in enumerate(aa):cc[i]=cc[i]+vv
 for i,vv in enumerate(bb):cc[i]=cc[i]+vv
 return trim(cc)
def pneg(aa):return [-cc for cc in aa]
def psub(aa,bb):return padd(aa,pneg(bb))
def pscale(aa,cc):return trim([vv*cc for vv in aa])
def pmul(aa,bb):
 if not aa or not bb:return []
 cc=[C(0) for _ in range(len(aa)+len(bb)-1)]
 for i,vv in enumerate(aa):
  for j,ww in enumerate(bb):cc[i+j]=cc[i+j]+vv*ww
 return trim(cc)
def pdiv(aa,bb):
 assert bb
 rr=list(aa);qq=[C(0) for _ in range(max(0,len(aa)-len(bb)+1))]
 inv=bb[-1].inverse()
 while rr and len(rr)>=len(bb):
  shift=len(rr)-len(bb);cc=rr[-1]*inv;qq[shift]=qq[shift]+cc
  for j,vv in enumerate(bb):rr[j+shift]=rr[j+shift]-cc*vv
  trim(rr)
 qq=trim(qq)
 assert padd(pmul(qq,bb),rr)==aa
 counts["rho_polynomial_division_returns"]+=1
 return qq,rr
def pmod(aa,bb):return pdiv(aa,bb)[1] if len(aa)>=len(bb) else list(aa)
def peval(aa,cc):
 out=C(0)
 for vv in reversed(aa):out=out*cc+vv
 return out
def pxgcd(aa,bb,verbose=False):
 rr0,rr1=list(aa),list(bb)
 ss0,ss1=[C(1)],[]
 tt0,tt1=[],[C(1)]
 step=0
 while rr1:
  qq,rr=pdiv(rr0,rr1)
  rr0,rr1=rr1,rr
  ss0,ss1=ss1,psub(ss0,pmul(qq,ss1))
  tt0,tt1=tt1,psub(tt0,pmul(qq,tt1))
  assert padd(pmul(ss0,aa),pmul(tt0,bb))==rr0
  step+=1
  if verbose:
   counts["rho_original_gcd_steps"]+=1
   say("new_H8_actual_rho_gcd_step",step=step,currentDegrees=[len(rr0)-1,len(rr1)-1],
       allQQAndExtensionProductsMultipliedBack=True,counts=dict(counts))
 inv=rr0[-1].inverse()
 gg,ss,tt=pscale(rr0,inv),pscale(ss0,inv),pscale(tt0,inv)
 assert padd(pmul(ss,aa),pmul(tt,bb))==gg
 return gg,ss,tt
def from_mpoly(pp):
 if not pp:return []
 dl,dr=map(int,pp.degrees())
 cc=[[fmpq(0)]*(dl+1) for _ in range(dr+1)]
 for ex,aa in pp.to_dict().items():cc[int(ex[1])][int(ex[0])]=fmpq(aa)
 return trim([C(fmpq_poly(aa)) for aa in cc])
def plist(aa):return [[str(c) for c in vv.v] for vv in aa]
fpoly,gpoly=from_mpoly(F),from_mpoly(G)
assert fpoly and gpoly
rho_gcd,fg_tag0,fg_tag1=pxgcd(fpoly,gpoly,True)
assert not pdiv(fpoly,rho_gcd)[1] and not pdiv(gpoly,rho_gcd)[1]
original_rho_gcd=list(rho_gcd)
removed=[]
for point in (0,1,-1):
 pp=[C(-point),C(1)];n=0
 while len(rho_gcd)>1 and not peval(rho_gcd,C(point)):
  qq,rem=pdiv(rho_gcd,pp);assert not rem
  rho_gcd=qq;n+=1
 removed.append([point,n])
say("new_H8_full_original_same_rho_gcd",
    exactH8IntegerCoefficientsAscending=[1,-2,-4,25,-44,32,16,-48,32],
    originalRhoGcdDegree=len(original_rho_gcd)-1,
    keptRhoGcdDegree=len(rho_gcd)-1,
    keptRhoGcdCoefficientsInLambda=plist(rho_gcd),
    originalUnitRhoFactorsRemoved=removed,
    fullSameOriginalFGBEzoutAndDivisionsMultipliedBack=True,
    allEightLambdaEmbeddingsRetained=True,counts=dict(counts))
if len(rho_gcd)==1:
 say("complete_H8_original_fiber_exclusion",
     reason="all original F/G common rho roots lie in original excluded rho poles",
     wholeComplexH8FiberExcluded=True,ordinaryISPClaim=False)
 sys.exit(0)
d=len(rho_gcd)-1
if d>4:
 say("new_H8_gcd_complete_finite_algebra_not_started",
     rhoDimension=d,maximumPlannedRhoDimension=4,
     wholeComplexH8FiberExcluded=False,ordinaryISPClaim=False)
 sys.exit(0)
class A:
 __slots__=("c",)
 def __init__(self,z=0):
  if isinstance(z,A):self.c=z.c;return
  cc=list(z) if isinstance(z,(list,tuple)) else [C(z)]
  cc=pmod(trim([C(vv) for vv in cc]),rho_gcd)
  self.c=tuple(cc+[C(0)]*(d-len(cc)))
 def __bool__(self):return any(self.c)
 def __add__(self,o):o=A(o);return A([a+b for a,b in zip(self.c,o.c)])
 __radd__=__add__
 def __neg__(self):return A([-cc for cc in self.c])
 def __sub__(self,o):return self+-A(o)
 def __rsub__(self,o):return A(o)+-self
 def __mul__(self,o):o=A(o);return A(pmul(trim(list(self.c)),trim(list(o.c))))
 __rmul__=__mul__
 def __pow__(self,n):
  assert n>=0
  out=A(1);base=self
  while n:
   if n&1:out=out*base
   n//=2
   if n:base=base*base
  return out
 def __eq__(self,o):return self.c==A(o).c
def a_inverse_paid(aa,label):
 aa=A(aa)
 gg,ss,tt=pxgcd(trim(list(aa.c)),rho_gcd)
 assert len(gg)==1 and gg[0],("original base denominator still has forbidden rho part",label)
 out=A(pscale(ss,gg[0].inverse()))
 assert aa*out==1
 return out
eval_cache={}
def evalpoly(pp):
 key=str(pp)
 if key not in eval_cache:eval_cache[key]=A(from_mpoly(pp))
 return eval_cache[key]
denom_cache={}
def evalr(rr):
 rr=R(rr);coefficient_audit(rr)
 nn=evalpoly(rr.n)
 if rr.d==oneP:return nn
 key=str(rr.d)
 if key not in denom_cache:
  denom_cache[key]=a_inverse_paid(evalpoly(rr.d),"already-audited original base denominator")
 return nn*denom_cache[key]
aa,bb=evalr(alpha),evalr(beta)
class B:
 __slots__=("c",)
 def __init__(self,z=0):
  if isinstance(z,B):self.c=z.c
  elif isinstance(z,(list,tuple)):
   self.c=tuple([A(vv) for vv in z]+[A(0)]*(2-len(z)))
  else:self.c=(A(z),A(0))
 def __bool__(self):return any(self.c)
 def __add__(self,o):o=B(o);return B([x+y for x,y in zip(self.c,o.c)])
 __radd__=__add__
 def __neg__(self):return B([-x for x in self.c])
 def __sub__(self,o):return self+-B(o)
 def __rsub__(self,o):return B(o)+-self
 def __mul__(self,o):
  o=B(o);x,y=self.c;z,w=o.c
  return B([x*z-bb*y*w,x*w+y*z-aa*y*w])
 __rmul__=__mul__
 def __pow__(self,n):
  assert n>=0
  out=B(1);base=self
  while n:
   if n&1:out=out*base
   n//=2
   if n:base=base*base
  return out
 def __eq__(self,o):return self.c==B(o).c
 def vector(self):return list(self.c[0].c)+list(self.c[1].c)
def eval_original_k2(kk):
 kk=K2(kk)
 return B([evalr(rr) for rr in kk.coefficients])
rhoA=A([0,1]);ellB=B([0,1])
assert ellB*ellB+B(aa)*ellB+B(bb)==0
basis=[B(rhoA**i) for i in range(d)]+[ellB*B(rhoA**i) for i in range(d)]
original_names=["E1","EB","EC","N1","NB","PB","NC","PC"]
original_values={name:eval_original_k2(rows[name]) for name in original_names}
gens=[];gen_names=[]
for name in original_names:
 for j,base in enumerate(basis):
  gens.append(base*original_values[name]);gen_names.append([name,j])
N=len(gens);dimension=2*d
matrix=[gg.vector() for gg in gens]
tags=[[C(int(i==j)) for j in range(N)] for i in range(N)]
rank=0;pivots=[]
for col in range(dimension):
 pivot=next((i for i in range(rank,N) if matrix[i][col]),None)
 if pivot is None:continue
 matrix[rank],matrix[pivot]=matrix[pivot],matrix[rank]
 tags[rank],tags[pivot]=tags[pivot],tags[rank]
 inv=matrix[rank][col].inverse()
 matrix[rank]=[cc*inv for cc in matrix[rank]]
 tags[rank]=[cc*inv for cc in tags[rank]]
 for i in range(N):
  if i==rank or not matrix[i][col]:continue
  coeff=matrix[i][col]
  matrix[i]=[a-coeff*b for a,b in zip(matrix[i],matrix[rank])]
  tags[i]=[a-coeff*b for a,b in zip(tags[i],tags[rank])]
 pivots.append(col);rank+=1
 say("new_H8_all_original_finite_ideal_pivot",
     rank=rank,extensionDimension=dimension,fullQQDimension=8*dimension,
     generatorCount=N,pivotColumn=col,
     onlyVerifiedH8ConstantCoefficientUnitsInverted=True,counts=dict(counts))
 if rank==dimension:break
# Verify the complete multiplication-ideal row source after Gaussian operations.
for j in range(rank):
 returned=B(0)
 for coeff,generator in zip(tags[j],gens):returned=returned+B(A(coeff))*generator
 assert returned.vector()==matrix[j]
unit_factors=[
 ("H",gram["H"]),("ell",ell),("u",v["u"]),("u_minus_ell",v["u"]-ell),
 ("b",b),("u_plus_Q_minus1",v["u"]+Q-1)]
unit=B(1)
for label,value in unit_factors:unit=unit*eval_original_k2(value)
closed=False;target=B(1)
for power in range(1,dimension+1):
 target=target*unit
 remainder=target.vector();combination=[C(0) for _ in range(N)]
 for j,col in enumerate(pivots):
  coeff=remainder[col]
  if coeff:
   remainder=[a-coeff*b for a,b in zip(remainder,matrix[j])]
   combination=[a+coeff*b for a,b in zip(combination,tags[j])]
 if not any(remainder):
  returned=B(0)
  for coeff,generator in zip(combination,gens):returned=returned+B(A(coeff))*generator
  assert returned==target
  closed=True
  say("new_H8_complete_same_point_original_unit_return",
      power=power,unitNames=[name for name,unused in unit_factors],
      allFactorsArePreviouslyPaidActualUnits=True,
      fullOriginalGeneratorTags=gen_names,
      fullTagSha256=hashlib.sha256(json.dumps(plist(combination)).encode()).hexdigest(),
      completeOriginalFiniteAlgebraIdentityMultipliedBack=True,
      extensionIdealRank=rank,extensionAlgebraDimension=dimension,
      wholeComplexH8FiberExcluded=True,ordinaryISPClaim=False)
  break
say("new_H8_full_original_finite_algebra_complete",
    originalRhoGcdDegree=len(original_rho_gcd)-1,keptRhoDegree=d,
    finiteAlgebraDimensionOverExactH8=dimension,fullQQDimension=8*dimension,
    originalIdealRank=rank,fullOriginalEightRowsRetained=True,
    wholeComplexH8FiberExcluded=closed,
    trueH8QQResultantMultiplicityNotClaimed=True,
    claimEntirePhiFaceExcluded=False,ordinaryISPClaim=False,counts=dict(counts))
