#!/usr/bin/env python3
"""New entire Delta=0 h=1 collision input, with the paid monic ell cubic.
Keep the original compatibility and the free original Gram pairing t.
One cleared Gram returns all original values; true H^3 targets retain
all temporary scalar pivot-zero fibers. Only the four-second necessary prefix; exact new curve factors. 120 seconds / 1 GiB.
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
ctx=fmpq_mpoly_ctx.get(('ell','lam','rho','t'),'lex')
ep,Lp,rp,tp=ctx.gens();zeroP=ctx.constant(0);oneP=ctx.constant(1)
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

er,lam,rho,tfree=map(R,(ep,Lp,rp,tp))
vr=original_rank_one_values(er,lam,rho)
A,B,p,q,S,xi=(vr[k] for k in ("A2","B3","p","q","S","xi"))
base_units=[("lambda",lam),("rho",rho),("p",p),("q",q),
            ("A2",A),("B3",B),("S_original",S)]
base_atoms=[(name,R(val).n) for name,val in base_units]
den_cache=set()
def strip_base(pp):
 assert pp
 key=str(pp)
 if key in den_cache:return
 rr=pp
 for name,atom in base_atoms:
  while rr:
   gg=rr.gcd(atom)
   if gg.total_degree()==0:break
   quotient=rr/gg;assert quotient*gg==rr
   atomq=atom/gg;assert atomq*gg==atom
   rr=quotient
 assert rr.total_degree()==0,("unpaid base denominator",str(rr))
 den_cache.add(key)
def coefficient_audit(rr):
 rr=R(rr)
 assert all(mm[0]==0 for mm in rr.n.to_dict())
 assert all(mm[0]==0 and mm[3]==0 for mm in rr.d.to_dict())
 strip_base(rr.d)
def base_inverse(rr):
 rr=R(rr);coefficient_audit(rr);strip_base(rr.n)
 ans=1/rr;assert ans*rr==1;return ans
def profile(pp):
 txt=str(pp).encode()
 return dict(degrees_ell_lambda_rho_t=list(map(int,pp.degrees())),
             terms=len(pp.to_dict()),totalDegree=int(pp.total_degree()),
             bytes=len(txt),sha256=hashlib.sha256(txt).hexdigest())
def extract_ell_coeffs(rr,n):
 rr=R(rr)
 assert all(mm[0]==0 and mm[3]==0 for mm in rr.d.to_dict())
 out=[zeroP for _ in range(n+1)]
 for mm,cf in rr.n.to_dict().items():
  assert int(mm[0])<=n
  small=list(mm);small[0]=0
  out[int(mm[0])]+=ctx.from_dict({tuple(small):cf})
 cc=[R(pp,rr.d) for pp in out]
 assert sum((cc[j]*er**j for j in range(n+1)),R())==rr
 for c0 in cc:coefficient_audit(c0)
 return cc
delta_raw=vr["determinant"]
dc=extract_ell_coeffs(delta_raw,3)
expected=-2*S*xi*p**5/rho
assert dc[3]==expected
leading_inverse=base_inverse(dc[3])
rel=[cc*leading_inverse for cc in dc[:3]]
assert sum((rel[j]*er**j for j in range(3)),R())+er**3==delta_raw*leading_inverse
say("new_entire_h_one_Delta_zero_monic_ell_cubic",
 oldCollisionChartReused=True,baseParameters=["lambda","rho"],
 originalGramFreeVariable="t",originalRelation="Phi*NF-S*zeta*Pf",
 paidLeading="-2*S*xi*p^5/rho",
 allFourOriginalRelationCoefficientsVerified=True,
 coefficients=[dict(numerator=profile(z.n),denominator=profile(z.d)) for z in rel],
 wholeLeadingZeroCoveragePaid=True,noNormInverse=True,claimExcluded=False)
stats=dict(multiplications=0,full_original_difference_coefficients=0)
cooperate_parameter_ring(R)
class K3:
 _isp_quotient_level=1
 __slots__=("coefficients",)
 def __init__(self,value=0):
  if isinstance(value,K3):self.coefficients=value.coefficients;return
  if isinstance(value,(list,tuple)):
   assert len(value)<=3
   cc=[R(z) for z in value]+[R(0)]*(3-len(value))
  else:cc=[R(value),R(0),R(0)]
  for z in cc:coefficient_audit(z)
  self.coefficients=tuple(cc)
 @classmethod
 def internal(cls,cc):
  obj=object.__new__(cls);obj.coefficients=tuple(cc);return obj
 def __bool__(self):return any(z!=0 for z in self.coefficients)
 def __add__(self,o):
  if getattr(o,"_isp_quotient_level",0)>1:return NotImplemented
  o=K3(o);return K3.internal([a+b for a,b in zip(self.coefficients,o.coefficients)])
 __radd__=__add__
 def __neg__(self):return K3.internal([-z for z in self.coefficients])
 def __sub__(self,o):return self+-K3(o)
 def __rsub__(self,o):return K3(o)+-self
 def __mul__(self,o):
  if getattr(o,"_isp_quotient_level",0)>1:return NotImplemented
  o=K3(o);raw=[R(0) for _ in range(5)]
  for i,a in enumerate(self.coefficients):
   for j,b in enumerate(o.coefficients):raw[i+j]=raw[i+j]+a*b
  out=raw[:];quot=[R(0),R(0)]
  for degree in (4,3):
   lead=out[degree];quot[degree-3]=lead
   for j in range(3):out[degree-3+j]=out[degree-3+j]-lead*rel[j]
   out[degree]=R(0)
  rebuilt=out[:]
  for i,a in enumerate(quot):
   for j in range(4):
    rebuilt[i+j]=rebuilt[i+j]+a*(rel[j] if j<3 else R(1))
  assert all(a==b for a,b in zip(raw,rebuilt))
  stats["multiplications"]+=1;stats["full_original_difference_coefficients"]+=5
  return K3.internal(out[:3])
 __rmul__=__mul__
 def __truediv__(self,o):
  assert isinstance(o,int) and o!=0
  return K3.internal([z/o for z in self.coefficients])
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  ans,cur=K3(1),self
  while n:
   if n&1:ans=ans*cur
   n>>=1
   if n:cur=cur*cur
  return ans
 def __eq__(self,o):
  if getattr(o,"_isp_quotient_level",0)>1:return NotImplemented
  o=K3(o);return all(a==b for a,b in zip(self.coefficients,o.coefficients))
ell=K3([0,1,0])
v=original_rank_one_values(ell,lam,rho)
assert v["determinant"]==0
b,c,Q,Pf,Pc,Phi,NF,NC,zeta=(v[k] for k in
 ("b","c","Q","Pf","Pc","Phi","NF","NC","zeta"))
compat=Phi*NC-S*zeta*Pc
f0=-Pc-b*c*Q*Phi*tfree
t0=b*Pf*tfree
assert Pf*f0+c*Q*Phi*t0+Pc*Pf==0
nline=NF*f0+c*Q*S*zeta*t0+NC*Pf
assert Phi*nline==Pf*compat
gram=original_rank_one_cleared_gram(v,f0,t0,Pf)
assert gram["P1Residual"]==0
say("new_entire_Delta_zero_h_one_same_cleared_Gram",
 scale="H=b*Pf, original point unit",
 originalF="(-Pc-bcQ*Phi*t)/Pf",originalT="free original t",
 originalP1Zero=True,originalNVIdentity="Phi*nline=Pf*compatibility",
 PhiPointUnitReason="Delta=0 and Pf*S*zeta nonzero",
 noPhiOrPfAlgebraInverse=True,allOriginalPhysicalConditionsRetained=True,
 statistics=dict(stats),claimExcluded=False)

def clear_original_row(label,rr):
 rr=K3(rr)
 if not rr:
  say("new_original_row_identically_zero",name=label,wholeFiberRetained=True)
  return rr
 den=oneP
 for cc in rr.coefficients:
  coefficient_audit(cc)
  den=den*(cc.d/den.gcd(cc.d))
 strip_base(den)
 nums=[cc.n*(den/cc.d) for cc in rr.coefficients]
 common=zeroP
 for pp in nums:common=common.gcd(pp)
 removed=oneP;removed_names=[]
 for name,atom in base_atoms:
  count=0
  while common:
   gg=common.gcd(atom)
   if gg.total_degree()==0:break
   common=common/gg;removed=removed*gg;count+=1
  if count:removed_names.append(dict(name=name,count=count))
 nums=[pp/removed for pp in nums]
 scalar=next(pp.coefficient(0) for pp in nums if pp)
 nums=[pp/scalar for pp in nums]
 out=K3([R(pp) for pp in nums])
 assert K3(den)*rr==K3(removed*scalar)*out
 say("new_complete_original_three_column_row",name=label,
     baseDenominator=profile(den),paidOnlyRemoval=removed_names,
     coefficients=[profile(pp) for pp in nums],
     allThreeOriginalScaleProductsVerified=True,
     noEllOrTDependentFactorStripped=True,claimExcluded=False)
 return out

def det3(rows):
 a,b,c=rows
 return (a[0]*(b[1]*c[2]-b[2]*c[1])
        -a[1]*(b[0]*c[2]-b[2]*c[0])
        +a[2]*(b[0]*c[1]-b[1]*c[0]))

original_rows={"C":clear_original_row("original_compatibility",compat)}
original_rows["ell:C"]=ell*original_rows["C"]
original_rows["ell2:C"]=ell**2*original_rows["C"]
target=gram["H"]**3
returned=[]
def actual_unit_return(labels):
 rr=[original_rows[name] for name in labels]
 mat=[list(row.coefficients) for row in rr]
 determinant=det3(mat)
 if not determinant:
  say("new_original_three_row_pivot_identically_zero",rows=labels,
      wholeTemporaryPivotZeroRetained=True,claimExcluded=False)
  return
 coefficients=[]
 for i in range(3):
  mm=[row[:] for row in mat];mm[i]=list(target.coefficients)
  coefficients.append(det3(mm)/determinant)
 # Only scalar rational arithmetic occurred; no inverse of an algebra element.
 # Do not insert temporary scalar fractions into the paid coefficient algebra.
 denominator=oneP
 for cc in coefficients:denominator*=cc.d/denominator.gcd(cc.d)
 tags=[cc.n*(denominator/cc.d) for cc in coefficients]
 assert all(tags[i]*coefficients[i].d==coefficients[i].n*denominator for i in range(3))
 assert sum((rr[i]*R(tags[i]) for i in range(3)),K3())==target*R(denominator)
 # The identity before this stripping is polynomial in lambda,rho,t after
 # multiplication by the already paid base denominators. It holds also at
 # every temporary determinant zero, with the original ell cubic retained.
 core=denominator;paid=[]
 for name,atom in base_atoms:
  count=0
  while core:
   gg=core.gcd(atom)
   if gg.total_degree()==0:break
   qq=core/gg;assert qq*gg==core
   core=qq;count+=1
  if count:paid.append(dict(name=name,count=count))
 core=core/core.coefficient(0)
 assert all(mm[0]==0 for mm in core.to_dict())
 entry=dict(rows=labels,target="H^3=(b*Pf)^3, true original point unit",
  clearedFullScalarDenominator=profile(denominator),
  necessaryOriginalParameterPolynomial=profile(core),
  onlyActuallyPaidBaseFactorsRemoved=paid,
  allThreeFinalPolynomialCoefficientsVerified=True,
  originalEllCubicRetained=True,
  temporaryDeterminantZeroFibersRetained=True,
  noNormAlgebraInverse=True,claimExcluded=core.total_degree()==0)
 if len(str(core).encode())<=8192:entry["corePolynomial"]=str(core)
 returned.append(entry)
 say("new_full_original_unit_three_row_return",**entry)
 return core,tags,denominator

# This first new necessary curve is independent of the free original t.
cover49,cover_tags,cover_denominator=actual_unit_return(["C","ell:C","ell2:C"])

# New input: all exact QQ components of the previously returned F49 curve.
content,factors=cover49.factor()
rebuilt=ctx.constant(content)
factor_records=[]
for i,(ff,multiplicity) in enumerate(factors):
 multiplicity=int(multiplicity);rebuilt*=ff**multiplicity
 entry=dict(index=i,multiplicity=multiplicity,profile=profile(ff),
            entireQQFactorRetained=True,claimExcluded=False)
 if len(str(ff).encode())<=16384:entry["polynomial"]=str(ff)
 factor_records.append(entry)
 say("new_Delta_zero_h_one_exact_F49_component",**entry)
assert rebuilt==cover49
cc=original_rows["C"].coefficients
assert all(z.d==oneP for z in cc)
common=zeroP
for z in cc:common=common.gcd(z.n)
common=common/common.coefficient(0)
primitive=[z.n/common for z in cc]
assert all(common*primitive[i]==cc[i].n for i in range(3))
common_content,common_factors=common.factor()
back=ctx.constant(common_content)
for ff,mm in common_factors:back*=ff**int(mm)
assert back==common
say("new_Delta_zero_h_one_compatibility_common_parameter_factor",
 common=profile(common),polynomial=str(common) if len(str(common).encode())<=16384 else None,
 originalThreeCoefficientsFactorActuallyVerified=True,
 primitiveCoefficients=[dict(profile=profile(pp),
 polynomial=str(pp) if len(str(pp).encode())<=16384 else None) for pp in primitive],
 allCommonFactorZeroFibersRetained=True,noCommonFactorGlobalInverse=True,
 claimExcluded=False)
signal.alarm(0)
say("new_Delta_zero_h_one_exact_original_curve_factorization_complete",
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 originalCover=profile(cover49),completeQQProductActuallyReturned=True,
 factors=factor_records,noFactorsPaidByFactorization=True,
 oldEightRowsAndOtherSevenTargetsNotRerun=True,
 fullOriginalCubicAndCompatibilityStillRequired=True,
 claimExcluded=False,peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
