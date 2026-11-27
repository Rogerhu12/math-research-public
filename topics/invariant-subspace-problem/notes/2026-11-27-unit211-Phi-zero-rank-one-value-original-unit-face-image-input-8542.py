#!/usr/bin/env python3
"""New actual 1069 residual Gauss input, followed by scalar-image input
for the remaining mod32 support: exact QQ
intersection of the original necessary curves with low-degree images of
already-paid original unit faces. This does NOT redo exclusion of those
faces and does NOT make their lambda images units. Fraction-free rho
pseudo-remainders preserve every leading-zero fiber. Small univariate QQ
Bezout/factor products identify exact next lambda domains. No full QQ
large resultant. The known mod68 coefficients are used for selection ONLY.
120s/1GiB.
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
for name,left,right,target,sha in specs:
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
F,G,S,T=[cores[name] for name in ("F_cross_E1_EC","G_principal_N1_ell","S_principal_E1","T_cross_E1_EB")]
assert F.gcd(G).total_degree()==0
from flint import fmpq_poly
zeroQ=fmpq_poly([]);oneQ=fmpq_poly([1])
prime=1009

# New actual 1069 residual: the QQ divisor below is justified by the
# six-phi theorem plus the already-paid explicit r^2 Sylvester dual for
# H4^4*H20. No QQ local determinant is rerun here.
mctx=nmod_mpoly_ctx.get(("lam","rho"),prime,"lex")
def fixed_mod_resultant(aa,bb,label):
 def mm(pp):
  dd={}
  for ex,vv in pp.to_dict().items():
   vv=fmpq(vv);assert vv.denominator==1
   dd[tuple(map(int,ex))]=int(vv.numerator)%prime
  out=mctx.from_dict(dd)
  assert int(out.degrees()[1])==int(pp.degrees()[1])
  return out
 am,bm=mm(aa),mm(bb)
 rr=am.resultant(bm,"rho")
 assert all(int(ex[1])==0 for ex in rr.to_dict())
 cc=[0]*(int(rr.degrees()[0])+1) if rr else []
 for ex,vv in rr.to_dict().items():cc[int(ex[0])]=int(vv)
 zz=nmod_poly(cc,prime)
 say("fixed_original_full_projection_for_1069",
     name=label,fixedRhoDegrees=[int(aa.degrees()[1]),int(bb.degrees()[1])],
     fixedSylvesterOrder=int(aa.degrees()[1]+bb.degrees()[1]),
     fullModDegree=int(zz.degree()),
     fullModSha256=hashlib.sha256(str(zz).encode()).hexdigest(),
     trueFixedQQDeterminantReduction=True,
     allOriginalLeadingZeroFibersRetained=True)
 return zz
m_R=fixed_mod_resultant(F,G,"R27")
m_P=fixed_mod_resultant(S,G,"P28")
m_PB=fixed_mod_resultant(T,G,"PB28")
m_newH4=[1,-7,16,-24,16]
m_newH20=[5,-86,751,-4320,18035,-57032,138416,-253716,
         325848,-204088,-230340,876048,-1346992,1230656,
         -511168,-330880,752576,-647168,325376,-94208,12288]
m_factors=[
 ("A2",[1,-2,2],111),("B3_linear",[-1,1],117),
 ("B3_quadratic",[1,-2,4],110),("Snum",[2,-5,4],24),
 ("lambda_half",[-1,2],145),("c_half_quadratic",[1,-2,3],44),
 ("H4",m_newH4,4),("H20",m_newH20,1)]
m_Q=nmod_poly([1],prime)
for label,coeffs,power in m_factors:
 phi_bar=nmod_poly(coeffs,prime)
 phi_bar*=pow(int(phi_bar.leading_coefficient()),-1,prime)
 m_Q*=phi_bar**power
assert m_Q.degree()==876
m_quot,m_rem=divmod(m_R,m_Q)
assert not m_rem and m_quot*m_Q==m_R
m_quot*=pow(int(m_quot.leading_coefficient()),-1,prime)
assert m_quot.degree()==1069
m_g1,m_a1,m_b1=m_quot.xgcd(m_P)
assert m_a1*m_quot+m_b1*m_P==m_g1
m_g2,m_a2,m_b2=m_g1.xgcd(m_PB)
m_tags=[m_a2*m_a1,m_a2*m_b1,m_b2]
assert sum((tt*ff for tt,ff in zip(m_tags,[m_quot,m_P,m_PB])),
           nmod_poly([],prime))==m_g2
new_residual_bound=int(m_g2.degree())
say("actual_new_1069_residual_full_original_Bezout",
    previouslyPaidQQDivisorDegree=840,newExplicitDualDivisorDegree=36,
    exactQQMonicCoverDegree=1069,
    actualResidualDegree=int(m_quot.degree()),
    actualResidualSha256=hashlib.sha256(str(m_quot).encode()).hexdigest(),
    actualDivisorSha256=hashlib.sha256(str(m_Q).encode()).hexdigest(),
    actualResidualGcdDivisorDegree=int(m_quot.gcd(m_Q).degree()),
    inputDegrees=[int(m_quot.degree()),int(m_P.degree()),int(m_PB.degree())],
    firstGcdDegree=int(m_g1.degree()),finalGcdDegree=new_residual_bound,
    finalGcdCoefficientsAscending=[int(aa) for aa in m_g2],
    finalGcdSha256=hashlib.sha256(str(m_g2).encode()).hexdigest(),
    actualFullBezoutTagDegrees=[int(tt.degree()) for tt in m_tags],
    actualFullBezoutTagSha256=hashlib.sha256(
      json.dumps([[int(aa) for aa in tt] for tt in m_tags]).encode()).hexdigest(),
    fullDivisionAndAllThreeBezoutProductsMultipliedBack=True,
    trueOriginalDistinctLambdaRhoPointBound=new_residual_bound,
    trueOriginalDistinctLambdaRhoEllTripleBound=2*new_residual_bound,
    proofUsesPaidQQMonic1069AndAllOriginalVandermondeKernelMultiplicities=True,
    noInferenceFromFormalDivisionOfOldGcd=True,
    claimEntirePhiFaceExcluded=False)
def qprofile(pp):
 return {"degree":int(pp.degree()),
         "sha256":hashlib.sha256(str(pp).encode()).hexdigest()}
def rho_coeffs(pp):
 if not pp:return []
 dl,dr=map(int,pp.degrees())
 cc=[[fmpq(0)]*(dl+1) for _ in range(dr+1)]
 for ex,aa in pp.to_dict().items():cc[int(ex[1])][int(ex[0])]=fmpq(aa)
 return [fmpq_poly(a) for a in cc]
def trim(cc):
 while cc and not cc[-1]:cc.pop()
 return cc
def addpoly(a,b):
 cc=[zeroQ]*max(len(a),len(b))
 for i,vv in enumerate(a):cc[i]+=vv
 for i,vv in enumerate(b):cc[i]+=vv
 return trim(cc)
def mulpoly(a,b):
 if not a or not b:return []
 cc=[zeroQ]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):cc[i+j]+=x*y
 return trim(cc)
def scale_poly(a,s):return trim([aa*s for aa in a])
def pseudorem_full_return(original,qq):
 a=qq[-1];n=len(qq)-1
 rem=list(original);quot=[];scale=oneQ;power=0;checks=0
 while rem and len(rem)-1>=n:
  shift=len(rem)-1-n;lc=rem[-1]
  new=scale_poly(rem,a)
  for j,cc in enumerate(qq):new[j+shift]-=lc*cc
  new=trim(new)
  quot=addpoly(scale_poly(quot,a),[zeroQ]*shift+[lc])
  scale*=a;power+=1
  rem=new
  expected=addpoly(mulpoly(quot,qq),rem)
  assert expected==scale_poly(original,scale)
  checks+=len(expected)
 assert len(rem)<=n
 return rem,power,checks
# Immutable prior actual mod68 factor data; reconstruct and check its full hash.
# It chooses new exact inputs, and does not prove any QQ divisibility.
modfactors=[
 ([344,1],1),([757,1],1),([623,1],4),([704,1],4),([734,1],4),
 ([705,1007,1],4),([158,43,778,1],4),([419,54,189,187,1],4),
 ([869,817,152,448,1],1),([860,812,727,690,766,1],1),
 ([337,768,493,851,657,239,108,512,368,1],1)]
g68=nmod_poly([1],prime)
for cc,pp in modfactors:g68*=nmod_poly(cc,prime)**pp
assert g68.degree()==68
assert hashlib.sha256(str(g68).encode()).hexdigest()=="51ff3c9fba943f174369ce7beff7b81cd6b6505be5f3180f4de966b1bfe542a6"
H4=[1,-7,16,-24,16]
H20=[5,-86,751,-4320,18035,-57032,138416,-253716,
     325848,-204088,-230340,876048,-1346992,1230656,
     -511168,-330880,752576,-647168,325376,-94208,12288]
remaining=g68
for cc in (H4,H20):
 hh=nmod_poly(cc,prime)
 while True:
  gg=remaining.gcd(hh)
  if gg.degree()==0:break
  quot,rem=divmod(remaining,gg);assert not rem and quot*gg==remaining
  remaining=quot
assert remaining.degree()==32
assert hashlib.sha256(str(remaining).encode()).hexdigest()=="a97d9ceb641c3c5162af051160864103b4dc8d6a0431a740e3c932378d4f9dec"
def to_mod_q(pp):
 cc=[]
 for a in pp:
  a=fmpq(a);assert int(a.denominator)%prime
  cc.append(int(a.numerator)%prime*pow(int(a.denominator)%prime,-1,prime)%prime)
 return nmod_poly(cc,prime)
curves={"F":F,"G":G,"S":S,"T":T}
actualunits=[("ell",ell),("u",v["u"]),("u_minus_ell",v["u"]-ell),("b",b)]
all_summaries=[]
for uname,uv in actualunits:
 ua,ub=uv.coefficients
 norm=ua*ua-alpha*ua*ub+beta*ub*ub
 adj=K2([ua-alpha*ub,-ub])
 assert uv*adj==K2(norm)
 coefficient_audit(norm)
 qcore,removed=paid_core(norm.n)
 qpoly,qscale=integer_core(qcore)
 qq=rho_coeffs(qpoly)
 say("new_paid_unit_face_scalar_image_input",actualUnit=uname,
     purpose="exact image intersection input, not re-excluding the paid unit face",
     normProfile=profile(norm.n),normDenominator=profile(norm.d),
     exactScalarImage=profile(qpoly),rhoDegree=len(qq)-1,
     onlyBaseUnitsRemoved=removed,allNormAndIntegerProductsMultipliedBack=True,
     normNeverInverted=True,claimImageIsOriginalUnit=False)
 if len(qq)!=3:
  say("nonquadratic_scalar_image_not_used",actualUnit=uname,
      rhoDegree=len(qq)-1,claimExcluded=False)
  continue
 c0,b0,a0=qq
 remainders={}
 for label,curve in curves.items():
  rem,power,checks=pseudorem_full_return(rho_coeffs(curve),qq)
  vv=rem[0] if rem else zeroQ
  uu=rem[1] if len(rem)>1 else zeroQ
  remainders[label]=(vv,uu)
  say("exact_fraction_free_original_image_remainder",actualUnit=uname,
      originalCurve=label,leadingPower=power,
      remainderProfiles=[qprofile(vv),qprofile(uu)],
      fullQQCoefficientReturns=checks,
      allLeadingZeroFibersRetained=True,claimExcluded=False)
 # All original finite rho intersections are common roots of the following
 # exact univariate necessary inputs, even where a0 or any new head is zero.
 necessary=[]
 for label,(vv,uu) in remainders.items():
  necessary.append(("quad_norm_"+label,a0*vv*vv-b0*uu*vv+c0*uu*uu))
 labels=list(remainders)
 for i,l in enumerate(labels):
  vl,ul=remainders[l]
  for r in labels[i+1:]:
   vr,ur=remainders[r]
   necessary.append(("same_rho_minor_"+l+"_"+r,ul*vr-ur*vl))
 gg=zeroQ;tags=[];allinputs=[];used=[]
 for label,pp in necessary:
  if not pp:continue
  new,aa,bb=gg.xgcd(pp)
  assert aa*gg+bb*pp==new
  tags=[aa*t for t in tags]+[bb];allinputs.append(pp);used.append(label)
  assert sum((t*f for t,f in zip(tags,allinputs)),zeroQ)==new
  gg=new
  if gg.degree()==0:break
 assert gg
 content,factors=gg.factor()
 product=fmpq_poly([content])
 for ff,power in factors:product*=ff**power
 assert product==gg
 factor_data=[]
 for ff,power in factors:
  # Reduction is only selection among the proven mod32 support.
  fm=to_mod_q(ff)
  hit=remaining.gcd(fm)
  repeated=0
  while hit.degree()>0:
   quot,rem=divmod(remaining,hit);assert not rem and quot*hit==remaining
   repeated+=int(hit.degree());remaining=quot
   hit=remaining.gcd(fm)
  factor_data.append({"coefficientsAscending":[str(a) for a in ff],
                      "degree":int(ff.degree()),"power":int(power),
                      "sha256":qprofile(ff)["sha256"],
                      "selectedRemainingModSupportDegree":repeated})
 summary={"actualUnit":uname,"exactQQImageCoverDegree":int(gg.degree()),
          "QQFactorContent":str(content),"QQFactors":factor_data,
          "actualUnivariateInputNames":used,
          "actualUnivariateInputDegrees":[int(x.degree()) for x in allinputs],
          "fullQQBezoutTagDegrees":[int(t.degree()) for t in tags],
          "fullQQBezoutTagSha256":hashlib.sha256(
             json.dumps([[str(a) for a in t] for t in tags]).encode()).hexdigest(),
          "allQQBezoutAndFactorProductsMultipliedBack":True,
          "remainingModSupportDegree":int(remaining.degree()),
          "noLambdaImageHasBeenDeclaredAnOriginalUnit":True,
          "wholeOriginalLambdaFibersStillRequireReturn":True}
 all_summaries.append(summary);say("new_exact_unit_face_image_intersection",**summary)
 if remaining.degree()==0:break
say("new_exact_original_unit_image_selection_complete",summaries=all_summaries,
    remainingModSupportDegree=int(remaining.degree()),
    remainingModCoefficients=[int(a) for a in remaining],
    trueOriginalPointBoundFromNewResidual=new_residual_bound,
    claimAnyNewWholeLambdaFiberExcluded=False,ordinaryISPClaim=False)
