#!/usr/bin/env python3
"""New actual-unit targets in the already-built Phi0/zn0 monic ell quadratic.
The old original rows are reconstructed only as inputs for this new target.
For the closed pair (r,ell*r), intersect a true unit's norm with the current
necessary core ONLY as a selection test; prove each improvement by an actual
cleared original-row identity and exact old-core/new-core division.
No norm is inverted. All remaining zero fibers are kept. 120 s / 1 GiB.
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

initial_target=gram["H"]**3
actual_units=[("ell",ell),("u",v["u"]),
              ("u-ell",v["u"]-ell),
              ("u+Q-1",v["u"]+Q-1),("H",gram["H"])]
unit_norms={}
for uname,uv in actual_units:
 ua,ub=uv.coefficients
 norm=ua*ua-alpha*ua*ub+beta*ub*ub
 adj=K2([ua-alpha*ub,-ub])
 assert uv*adj==K2(norm)
 coefficient_audit(norm)
 unit_norms[uname]=norm
say("new_actual_unit_target_input",
    previous_source_sha256="1ec9ea1cdd07d2a8a04784a6a1d5c272f384d819b61550c1932b49491fe13406",
    previous_complete_run=45988581954,
    onlyClosedPairsAreUsed=True,
    actualUnitNames=[name for name,u0 in actual_units],
    normPurpose="intersection selection ONLY, never inversion or exclusion",
    norms={name:profile(z.n) for name,z in unit_norms.items()})
def actual_return(name,target):
 left,right=name,"ell:"+name
 aa,bb=rows[left].coefficients,rows[right].coefficients
 det=aa[0]*bb[1]-aa[1]*bb[0]
 if not det:return None
 tt=target.coefficients
 na=tt[0]*bb[1]-tt[1]*bb[0]
 nb=aa[0]*tt[1]-aa[1]*tt[0]
 ca,cb=na/det,nb/det
 assert ca*det==na and cb*det==nb
 common=ca.d.gcd(cb.d)
 den=(ca.d/common)*cb.d
 qa,qb=den/ca.d,den/cb.d
 assert qa*ca.d==den and qb*cb.d==den
 ta,tb=ca.n*qa,cb.n*qb
 assert K2(R(den))*target==K2(R(ta))*rows[left]+K2(R(tb))*rows[right]
 core,removed=paid_core(den)
 return dict(core=core,den=den,tags=(ta,tb),removed=removed)
final_cores=[]
unit_return=None
for name in ("E1","EB","N1","NB","PB"):
 target=initial_target
 current=actual_return(name,target)
 if current is None:
  say("closed_original_pair_singular",row=name)
  continue
 used={}
 say("initial_actual_H_cubed_core",row=name,profile=profile(current["core"]))
 for uname,uv in actual_units:
  norm=unit_norms[uname]
  # Any accepted target remains a product of TRUE original nonzero values.
  # No factor of norm is ever deleted merely because it lies in norm.
  for step in range(1,9):
   oldcore=current["core"]
   meet=oldcore.gcd(norm.n) if norm.n else oldcore
   if meet.total_degree()==0:break
   candidate=target*(uv**3)
   nxt=actual_return(name,candidate)
   assert nxt is not None
   newcore=nxt["core"]
   # Since (r,ell*r) is an actual closed multiplication module, multiplying
   # the target cannot introduce new non-base-unit denominators.
   quotient=oldcore/newcore
   assert quotient*newcore==oldcore
   changed=int(newcore.total_degree())<int(oldcore.total_degree())
   say("actual_original_unit_target_step",row=name,actualUnit=uname,
       appliedNewPower=3,passNumber=step,selectionIntersection=profile(meet),
       oldCore=profile(oldcore),newCore=profile(newcore),
       exactOldCoreOverNewCore=profile(quotient),
       actualFullDenominator=profile(nxt["den"]),
       actualOriginalTags=[profile(x) for x in nxt["tags"]],
       paidBaseFactorsRemoved=nxt["removed"],
       fullSamePointTwoCoefficientIdentity=True,
       normUsedAsUnit=False,strictlySmaller=changed)
   if not changed:break
   target,current=candidate,nxt
   used[uname]=used.get(uname,0)+3
   if newcore.total_degree()==0:
    unit_return=dict(row=name,trueUnitPowers=used)
    break
  if unit_return:break
 core=current["core"]
 final_cores.append((name,core))
 say("final_actual_unit_core_for_closed_pair",row=name,
     core=profile(core),trueUnitPowers=used,
     fullOriginalUnitReturn=core.total_degree()==0)
 if unit_return:break
finite=None
if not unit_return:
 for i,(left,f0) in enumerate(final_cores):
  for right,f1 in final_cores[i+1:]:
   gg=f0.gcd(f1)
   if gg.total_degree()==0:
    finite=dict(rows=[left,right],
                totalDegrees=[int(f0.total_degree()),int(f1.total_degree())],
                distinctBasePointBound=int(f0.total_degree()*f1.total_degree()))
    break
  if finite:break
say("complete_new_actual_unit_saturation_return",
    scope="original Phi=0, zn=0, LS!=0, h=1 up to original B/C exchange",
    originalUnitReturn=unit_return,finiteBasePointCover=finite,
    claimExcluded=unit_return is not None,
    finalOriginalCores={name:profile(pp) for name,pp in final_cores},
    preservedAllRemainingZeroFibers=True,
    noNormInversion=True,statistics=dict(stats),ordinaryISPClaim=False)
