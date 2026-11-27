#!/usr/bin/env python3
"""New exact QQ infinity-local degree certificate for the fixed original
27x27 rho Sylvester matrix. No QQ resultant coefficients are computed.
The already executed fixed original modular resultant has degree1945; its
full elementary degree bound is2051. Extract infinity valuation106 by
constant QQ kernel row replacements, with every division multiplied back.
120s /1GiB. The modular source is prior evidence, not rerun here.
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


from flint import fmpq_poly,fmpq_mat
z=fmpq_poly([0,1]);zeroz=fmpq_poly([])
n=27;fixed_upper=2051;prior_mod_degree=1945;target=106
assert fixed_upper-prior_mod_degree==target
assert list(map(int,F.degrees()))==[77,14]
assert list(map(int,G.degrees()))==[75,13]
def reversed_lambda_coefficients(pp,lambda_bound,rho_bound):
 out=[zeroz for _ in range(rho_bound+1)]
 by_rho=[{} for _ in range(rho_bound+1)]
 for mm,aa in pp.to_dict().items():
  dl,dr=map(int,mm);assert dl<=lambda_bound and dr<=rho_bound
  by_rho[dr][lambda_bound-dl]=fmpq(aa)
 for j,dd in enumerate(by_rho):
  out[j]=fmpq_poly([dd.get(k,fmpq(0)) for k in range(max(dd,default=-1)+1)])
 # Whole coefficient reversal is checked back before any determinant step.
 rebuilt=ctx.from_dict({(lambda_bound-i,j):a for j,zz in enumerate(out)
                        for i,a in enumerate(zz) if a})
 assert rebuilt==pp
 return out
fc=reversed_lambda_coefficients(F,77,14)
gc=reversed_lambda_coefficients(G,75,13)
M=[]
for shift in range(13):M.append([zeroz]*shift+fc+[zeroz]*(12-shift))
for shift in range(14):M.append([zeroz]*shift+gc+[zeroz]*(13-shift))
assert len(M)==n and all(len(rr)==n for rr in M)
divisions=0;trace=hashlib.sha256()
def dividechecked(pp,qq):
 global divisions
 a,b=divmod(pp,qq);assert a*qq+b==pp
 divisions+=1
 return a,b
def valuation(pp):
 if not pp:return 10**9
 ans=next(i for i,a in enumerate(pp) if a)
 qq,rr=dividechecked(pp,z**ans)
 assert not rr and qq[0]
 return ans
cost=[[valuation(pp) for pp in row] for row in M]
E,permutation,du, dv=minimum_assignment(cost)
assert all(cost[i][permutation[i]]<10**9 for i in range(n))
assert E<=target
for i in range(n):
 for j in range(n):
  pp=M[i][j];power=du[i]+dv[j]
  if not pp:continue
  if power>=0:
   qq,rem=dividechecked(pp,z**power);assert not rem;M[i][j]=qq
  else:
   qq=pp*z**(-power);assert dividechecked(qq,z**(-power))==(pp,zeroz)
   M[i][j]=qq
Tprec=target+1
N=Tprec-E
for i in range(n):
 for j in range(n):M[i][j]=dividechecked(M[i][j],z**N)[1]
say("new_original_infinity_exact_matrix",
    originalFixedRhoDegrees=[14,13],matrixSize=n,
    originalIntegerCoreHashes=[profile(F)["sha256"],profile(G)["sha256"]],
    determinantIdentity="det Mhat(z)=z^2051 Res_rho(F,G)(1/z)",
    priorModularSourceSha256="60c2a406c48174d8a537ccf363369fc4abe7a0f39b8c00af85a071806200fafc",
    priorModularRun=45994627867,priorModularDegree=prior_mod_degree,
    targetInfinityValuation=target,initialQQValuationLowerBound=E,
    fullMatching=permutation,fullIntegralDualRows=du,fullIntegralDualColumns=dv,
    everyDualEntryInequalityVerified=True,
    remainingPrecision=N,wholeCoefficientReversalVerified=True,
    noQQResultantComputed=True,claimExcluded=False)
rounds=[]
full_rank=False
while E<target:
 data=[[pp[0] for pp in row] for row in M]
 AA=fmpq_mat(data);rr,rank=AA.transpose().rref()
 rank=int(rank)
 if rank==n:
  det0=AA.det();assert det0
  full_rank=True
  say("QQ_full_rank_before_modular_target",extracted=E,target=target,
      actualQQDegree=fixed_upper-E,
      constantDeterminantSha256=hashlib.sha256(str(det0).encode()).hexdigest(),
      modularLeadingWasNotAUnit=True,claimExcluded=False)
  break
 pivots=[]
 for i in range(rank):
  pivot=next(j for j in range(n) if rr[i,j]);assert rr[i,pivot]==1;pivots.append(pivot)
 free=[j for j in range(n) if j not in pivots]
 assert free
 basis=[]
 for jj in free:
  vv=[fmpq(0)]*n;vv[jj]=fmpq(1)
  for i,k in enumerate(pivots):vv[k]=-rr[i,jj]
  check=fmpq_mat([vv])*AA
  assert all(check[0,j]==0 for j in range(n))
  assert all(vv[k]==(1 if k==jj else 0) for k in free)
  basis.append((jj,vv))
 # P changes exactly rows free. Its restriction to columns free is I.
 # Thus P=I+N0 with N0^2=0 and det P=1 over QQ[z].
 updated={}
 for index,vv in basis:
  row=[]
  for j in range(n):
   combination=sum((M[i][j]*a for i,a in enumerate(vv) if a),zeroz)
   quotient,rem=dividechecked(combination,z)
   assert not rem
   row.append(quotient)
  updated[index]=row
  trace.update(str((index,list(map(str,vv)))).encode())
 for index,row in updated.items():M[index]=row
 previousN=N
 E+=len(free);assert E<=target
 N=Tprec-E
 assert N<=previousN-1
 # After division one loses at most one old precision. The smaller N
 # maintains E+N=target+1; all discarded multiples are multiplied back.
 for i in range(n):
  for j in range(n):M[i][j]=dividechecked(M[i][j],z**N)[1]
 rec=dict(round=len(rounds)+1,actualQQRank=rank,actualQQKernelDimension=len(free),
          selectedRows=free,extractedTotal=E,remainingPrecision=N,
          determinantRowOperation="P=I+N0; N0^2=0; detP=1",
          allKernelAndDivisionIdentitiesVerified=True,divisionChecks=divisions)
 rounds.append(rec)
 say("new_original_infinity_QQ_kernel_extraction",**rec,claimExcluded=False)
answer=dict(provedInfinityValuationLowerBound=E,
            modularValuationUpperBound=target,
            exactQQValuation=E if E==target or full_rank else None,
            exactQQDegree=fixed_upper-E if E==target or full_rank else None,
            degree1945Paid=(E==target),
            originalIntegerCoreHashes=[profile(F)["sha256"],profile(G)["sha256"]],
            fullRounds=rounds,divisionIdentities=divisions,
            kernelTraceSha256=trace.hexdigest(),
            noQQResultantComputed=True,noFiniteFiberRemoved=True,
            claimExcluded=False,ordinaryISPClaim=False)
say("complete_original_infinity_degree_certificate",**answer)
