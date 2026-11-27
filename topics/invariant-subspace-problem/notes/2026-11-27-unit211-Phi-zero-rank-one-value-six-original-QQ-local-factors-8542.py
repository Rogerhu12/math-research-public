#!/usr/bin/env python3
"""New exact QQ local divisibilities of the original degree1945 R27 cover.
Six explicit linear/quadratic phi are handled in their actual QQ fields.
Targets are COMPLETE multiplicities of the same original R mod1009, not
multiplicities of a modular gcd. Only native QQ kernel row replacements
and exact polynomial divisions are used. No QQ resultant is expanded.
argv1 selects all (default) or one named phi.120s/1GiB.
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

def minimum_assignment(cost):
    """Hungarian minimization, returning a matching and feasible integral dual."""
    n = len(cost)
    assert n and all(len(row) == n for row in cost)
    inf = 10**15
    u, v, matching, way = ([0] * (n + 1) for _ in range(4))
    for row in range(1, n + 1):
        matching[0] = row
        col = 0
        reduced_min = [inf] * (n + 1)
        used = [False] * (n + 1)
        while True:
            used[col] = True
            active_row = matching[col]
            delta, next_col = inf, 0
            for j in range(1, n + 1):
                if not used[j]:
                    reduced = cost[active_row - 1][j - 1] - u[active_row] - v[j]
                    if reduced < reduced_min[j]:
                        reduced_min[j], way[j] = reduced, col
                    if reduced_min[j] < delta:
                        delta, next_col = reduced_min[j], j
            assert next_col and delta < inf
            for j in range(n + 1):
                if used[j]:
                    u[matching[j]] += delta
                    v[j] -= delta
                else:
                    reduced_min[j] -= delta
            col = next_col
            if matching[col] == 0:
                break
        while True:
            next_col = way[col]
            matching[col] = matching[next_col]
            col = next_col
            if col == 0:
                break
    permutation = [None] * n
    for j in range(1, n + 1):
        permutation[matching[j] - 1] = j - 1
    assert sorted(permutation) == list(range(n))
    assert all(cost[i][j] >= u[i + 1] + v[j + 1]
               for i in range(n) for j in range(n))
    objective = sum(cost[i][j] for i, j in enumerate(permutation))
    assert objective == sum(u[1:]) + sum(v[1:])
    assert all(cost[i][j] == u[i + 1] + v[j + 1]
               for i, j in enumerate(permutation))
    return objective, permutation, u[1:], v[1:]


import sys
from flint import fmpq_poly,fmpq_mat
prime=1009
mctx=nmod_mpoly_ctx.get(("lam","rho"),prime,"lex")
def scalar_mod(aa):
 aa=fmpq(aa);dd=int(aa.denominator)%prime;assert dd
 return int(aa.numerator)%prime*pow(dd,-1,prime)%prime
def modpoly(pp):
 return mctx.from_dict({tuple(map(int,m)):scalar_mod(a) for m,a in pp.to_dict().items()})
ma,mb=modpoly(F),modpoly(G)
assert list(map(int,ma.degrees()))==[77,14] and list(map(int,mb.degrees()))==[75,13]
out=ma.resultant(mb,"rho")
modcoeff=[0]*(int(out.degrees()[0])+1)
for mm,aa in out.to_dict().items():
 assert int(mm[1])==0;modcoeff[int(mm[0])]=int(aa)
Rbar=nmod_poly(modcoeff,prime)
assert Rbar.degree()==1945
assert hashlib.sha256(str(Rbar).encode()).hexdigest()=="e3312d0f8b9a52dd7f59435e7ed2a8d4592fcaa8743e65051dae2ece669c797f"
defs=[
 ("A2",["1/2","-1","1"]),
 ("B3_linear",["-1","1"]),
 ("B3_quadratic",["1/4","-1/2","1"]),
 ("Snum",["1/2","-5/4","1"]),
 ("lambda_half",["-1/2","1"]),
 ("c_half_quadratic",["1/3","-2/3","1"])
]
selected=sys.argv[1] if len(sys.argv)>1 else "all"
assert selected=="all" or selected in [name for name,_ in defs]
zeroz=fmpq_poly([])
def lambda_coefficients(pp,rhodegree):
 cs=[]
 dd=pp.to_dict()
 for j in range(rhodegree+1):
  terms={int(m[0]):a for m,a in dd.items() if int(m[1])==j}
  cs.append(fmpq_poly([terms.get(k,fmpq(0)) for k in range(max(terms,default=-1)+1)]))
 rebuilt=ctx.from_dict({(i,j):aa for j,po in enumerate(cs) for i,aa in enumerate(po) if aa})
 assert rebuilt==pp
 return cs
fc=lambda_coefficients(F,14);gc=lambda_coefficients(G,13)
originalM=[[zeroz]*s+fc+[zeroz]*(12-s) for s in range(13)]
originalM+=[[zeroz]*s+gc+[zeroz]*(13-s) for s in range(14)]
n=27
assert len(originalM)==n and all(len(row)==n for row in originalM)
class FE:
 def __init__(self,field,v=0):
  self.field=field
  if isinstance(v,FE):assert v.field is field;self.p=v.p;return
  pp=v if isinstance(v,fmpq_poly) else fmpq_poly([v])
  self.p=divmod(pp,field.mod)[1]
 def __bool__(self):return bool(self.p)
 def __add__(self,o):o=FE(self.field,o);return FE(self.field,self.p+o.p)
 __radd__=__add__
 def __neg__(self):return FE(self.field,-self.p)
 def __sub__(self,o):return self+-FE(self.field,o)
 def __rsub__(self,o):return FE(self.field,o)+-self
 def __mul__(self,o):o=FE(self.field,o);return FE(self.field,self.p*o.p)
 __rmul__=__mul__
 def __eq__(self,o):o=FE(self.field,o);return self.p==o.p
 def inverse(self):
  assert self
  gg,aa,bb=self.p.xgcd(self.field.mod)
  assert self.p*aa+self.field.mod*bb==gg and gg.degree()==0
  rr=FE(self.field,aa/gg[0]);assert self*rr==1
  self.field.inverses+=1
  return rr
class Field:
 def __init__(self,phi):
  self.mod=phi;self.inverses=0
  assert phi.leading_coefficient()==1
  assert phi.degree()==1 or (phi.degree()==2 and phi[1]**2-4*phi[0]<0)
 def __call__(self,v=0):return FE(self,v)
def mod_univariate(phi):
 return nmod_poly([scalar_mod(a) for a in phi],prime)
def mod_valuation(pp,phi):
 count=0
 while True:
  quot,rem=divmod(pp,phi)
  if rem:break
  assert quot*phi==pp;pp=quot;count+=1
 return count
all_phi=[]
for name,coeff in defs:
 phi=fmpq_poly([fmpq(x) for x in coeff])
 for _,earlier in all_phi:
  gg,aa,bb=phi.xgcd(earlier)
  assert phi*aa+earlier*bb==gg and gg.degree()==0
 all_phi.append((name,phi))
say("six_explicit_pairwise_coprime_QQ_phi",
    selected=selected,phi=[dict(name=name,coefficientsAscending=list(map(str,po))) for name,po in all_phi],
    fullQQBezoutProductsVerified=True,originalResultantDegree=1945,
    exactDegreeSourceSha256="c3e74aad554242a0a4dbe386f3a1808c4529033613e0061cbc482ee1345691dc",
    allMonicPhi1009Integral=True,noZeroFiberExclusionAssumed=True,claimExcluded=False)
completed=[];globalTrace=hashlib.sha256()
for name,phi in all_phi:
 if selected!="all" and name!=selected:continue
 d=phi.degree();field=Field(phi)
 phibar=mod_univariate(phi);assert phibar.degree()==d and phibar.leading_coefficient()==1
 target=mod_valuation(Rbar,phibar)
 assert target=={"A2":111,"B3_linear":117,"B3_quadratic":110,"Snum":24,"lambda_half":145,"c_half_quadratic":44}[name]
 M=[row[:] for row in originalM]
 divisions=0;trace=hashlib.sha256()
 def dividechecked(pp,qq):
  global divisions
  a,b=divmod(pp,qq);assert a*qq+b==pp
  divisions+=1
  return a,b
 costs=[]
 for row in M:
  cc=[]
  for pp in row:
   if not pp:cc.append(10**9);continue
   val=0
   while True:
    quot,rem=dividechecked(pp,phi)
    if rem:break
    pp=quot;val+=1
   cc.append(val)
  costs.append(cc)
 E,perm,du,dv=minimum_assignment(costs)
 assert E<=target and all(costs[i][perm[i]]<10**9 for i in range(n))
 for i in range(n):
  for j in range(n):
   pp=M[i][j];power=du[i]+dv[j]
   if not pp:continue
   if power>=0:
    quot,rem=dividechecked(pp,phi**power);assert not rem;M[i][j]=quot
   else:
    qq=pp*phi**(-power)
    assert dividechecked(qq,phi**(-power))==(pp,zeroz);M[i][j]=qq
 Tprecision=target+1;N=Tprecision-E
 for i in range(n):
  for j in range(n):M[i][j]=dividechecked(M[i][j],phi**N)[1]
 say("new_original_QQ_phi_local_start",name=name,
     phi=list(map(str,phi)),degree=d,actualPrimaryRModularTarget=target,
     initialActualQQValuation=E,precision=N,
     fullMatching=perm,fullDualRows=du,fullDualColumns=dv,
     originalMatrixSize=n,QQRegularRepresentationSize=n*d,claimExcluded=False)
 rounds=[];fullrank=False
 while E<target:
  M0=[[dividechecked(pp,phi)[1] for pp in row] for row in M]
  dim=n*d;data=[[fmpq(0)]*dim for _ in range(dim)]
  for i in range(n):
   for j in range(n):
    if not M0[i][j]:continue
    for a in range(d):
     pp=dividechecked(M0[i][j]*fmpq_poly([0]*a+[1]),phi)[1]
     for b,coef in enumerate(pp):data[i*d+a][j*d+b]=coef
  AA=fmpq_mat(data);rr,rank=AA.transpose().rref();rank=int(rank)
  assert rank%d==0
  if rank==dim:
   det0=AA.det();assert det0;fullrank=True
   say("QQ_phi_full_rank_below_modular_target",name=name,
       exactQQMultiplicity=E,modularMultiplicity=target,
       residueNormDeterminantSha256=hashlib.sha256(str(det0).encode()).hexdigest(),
       targetReached=False,claimExcluded=False)
   break
  pivots=[]
  for i in range(rank):
   jj=next(j for j in range(dim) if rr[i,j]);assert rr[i,jj]==1;pivots.append(jj)
  free=[j for j in range(dim) if j not in pivots];basis=[]
  for jj in free:
   vec=[fmpq(0)]*dim;vec[jj]=fmpq(1)
   for i,j in enumerate(pivots):vec[j]=-rr[i,jj]
   checked=fmpq_mat([vec])*AA
   assert all(checked[0,j]==0 for j in range(dim))
   kv=[field(fmpq_poly(vec[i*d:(i+1)*d])) for i in range(n)]
   for pivot,bvec in basis:
    fact=kv[pivot]
    if fact:kv=[a-fact*b for a,b in zip(kv,bvec)]
   lead=next((j for j,a in enumerate(kv) if a),None)
   if lead is None:continue
   inv=kv[lead].inverse();kv=[inv*a for a in kv]
   for k,(pivot,bvec) in enumerate(basis):
    fact=bvec[lead]
    if fact:basis[k]=(pivot,[a-fact*b for a,b in zip(bvec,kv)])
   basis.append((lead,kv));basis.sort(key=lambda z:z[0])
  assert basis and len(basis)*d==len(free)
  chosen=[i for i,_ in basis]
  for i,vv in basis:
   assert all(vv[j]==(1 if i==j else 0) for j in chosen)
   for j in range(n):
    checked=sum((aa.p*M0[k][j] for k,aa in enumerate(vv) if aa),zeroz)
    assert not dividechecked(checked,phi)[1]
  updated={}
  for i,vv in basis:
   row=[]
   for j in range(n):
    pp=sum((aa.p*M[k][j] for k,aa in enumerate(vv) if aa),zeroz)
    quot,rem=dividechecked(pp,phi);assert not rem;row.append(quot)
   updated[i]=row
   trace.update(str((i,[[str(a) for a in aa.p] for aa in vv])).encode())
  # Identity on chosen columns lifts literally to QQ[lambda], so P=I+N0,
  # N0^2=0, detP=1 even though the other entries are phi-residue polynomials.
  for i,row in updated.items():M[i]=row
  E+=len(updated);assert E<=target
  N=Tprecision-E
  for i in range(n):
   for j in range(n):M[i][j]=dividechecked(M[i][j],phi**N)[1]
  rec=dict(round=len(rounds)+1,actualQQRank=rank,
           actualFieldKernelDimension=len(updated),selectedRows=chosen,
           extractedTotal=E,remainingPrecision=N,
           allKernelAndDivisionIdentitiesVerified=True)
  rounds.append(rec)
  say("new_original_QQ_phi_kernel_extraction",name=name,**rec,claimExcluded=False)
 result=dict(name=name,phiQQCoefficientsAscending=list(map(str,phi)),
             completePrimaryRModularMultiplicity=target,provedQQMultiplicityLowerBound=E,
             exactQQMultiplicity=E if E==target or fullrank else None,
             targetReached=(E==target),rounds=rounds,
             QQFieldInverseProducts=field.inverses,
             exactDivisionProducts=divisions,kernelTraceSha256=trace.hexdigest(),
             noOriginalZeroFiberExclusionByThisCertificate=True)
 completed.append(result);globalTrace.update(trace.digest())
 say("complete_one_original_QQ_phi_certificate",**result,claimExcluded=False)
 # Each successful factor is a complete new result even if a later case
 # reaches the fixed resource cap; earlier records remain valid.
productQQ=fmpq_poly([1]);productMod=nmod_poly([1],prime)
for rec in completed:
 phi=fmpq_poly([fmpq(a) for a in rec["phiQQCoefficientsAscending"]])
 exponent=rec["provedQQMultiplicityLowerBound"]
 productQQ*=phi**exponent;productMod*=mod_univariate(phi)**exponent
assert mod_univariate(productQQ)==productMod
residual,rem=divmod(Rbar,productMod);assert not rem and residual*productMod==Rbar
say("complete_selected_original_QQ_phi_divisibility",
    selected=selected,completedFactors=completed,
    provedQQMonicProductDegree=productQQ.degree(),
    monicProduct1009Integral=True,pairwiseQQCoprimalityPaid=True,
    productModMultipliedBack=True,
    resultingTrueQQResidualDegree=1945-productQQ.degree(),
    actualResidualModDegree=residual.degree(),
    residualDegreePreserved=(residual.degree()==1945-productQQ.degree()),
    residualModSha256=hashlib.sha256(str(residual).encode()).hexdigest(),
    globalKernelTraceSha256=globalTrace.hexdigest(),
    noQQResultantExpanded=True,noActualZeroFiberDiscarded=True,
    claimExcluded=False,ordinaryISPClaim=False)
