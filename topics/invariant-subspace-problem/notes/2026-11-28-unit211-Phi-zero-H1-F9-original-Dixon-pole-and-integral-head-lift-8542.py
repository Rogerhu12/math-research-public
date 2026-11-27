#!/usr/bin/env python3
"""NEW exact F9 specialization of the original Dixon8 constant target.

Reconstruct only the original head/norm definitions and the original fixed
Dixon8 matrix. No old QQ(u) Gaussian, norm-resultant driver or head-zero
value gate is run. Over the complete QQ[u]/F9, recover the true linear
head-zero Q root and its QQ Bezout identity using the ACTUAL head,
so no unproved residue inverse of its paid-factor product is used. The new target is a left
annihilator w D=0 with w e0=1, showing that the known unique generic
D^{-1}e0 must have an F9 pole when the original source poles are regular.
Actual p-integrality and the complete F9bar factor pattern connect this
new rational divisor to the existing completed original Q blocks.
120 seconds /1 GiB. Small receipts only, no coefficient payload.
"""
import time,json,hashlib,signal,resource,contextlib,io
from pathlib import Path
from flint import fmpq,fmpq_poly,nmod_poly
START=time.perf_counter();DEADLINE=START+120;PRIME=1009
signal.alarm(120)
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,separators=(",",":")),flush=True)
def restore_deadline():
 signal.setitimer(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
def digest(obj):
 raw=json.dumps(obj,separators=(",",":")).encode()
 return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
def pdigest(poly):
 d=digest([str(c) for c in poly.coeffs()]);d["degree"]=int(poly.degree());return d
def mpdigest(poly):
 d=digest([int(c) for c in poly.coeffs()]);d["degree"]=int(poly.degree());return d
def load_prefix(name,sha,marker,label):
 path=Path(__file__).with_name(name)
 raw=path.read_bytes();assert hashlib.sha256(raw).hexdigest()==sha
 source=raw.decode();assert source.count(marker)==1
 prefix=source.split(marker,1)[0]
 env={"__file__":str(path),"__name__":"__new_F9_necessary_original_"+label+"__"}
 with contextlib.redirect_stdout(io.StringIO()):
  exec(compile(prefix,str(path)+":necessary-"+label,"exec"),env)
 restore_deadline()
 say("new_F9_necessary_original_definition",
  input=name,inputSHA256=sha,prefixBytes=len(prefix.encode()),
  prefixSHA256=hashlib.sha256(prefix.encode()).hexdigest(),
  oldStandaloneTargetDriverExecuted=False)
 return env
headenv=load_prefix(
 "2026-11-28-unit211-Phi-zero-H1-original-three-head-paid-factor-and-zero-fibers-8542.py",
 "41f0ff6e5148fc51f29421bdf56147bffc66cfa5b4826622ddd72685b26ec1bc",
 "\nhp,hs=read_source(","head")
F9s=[ff for ff,e in headenv["factors"] if ff.degree()==9]
assert len(F9s)==1
F9=F9s[0];head=headenv["original_head"]
assert pdigest(F9)["sha256"]=="30a60a6e2188e060f610ae64e0df7543dec5cce437c7c355d5987bf5a8fb7e39"
original=load_prefix(
 "2026-11-28-unit211-Phi-zero-whole-H1-original-biquadratic-Dixon-unit-target-syntax-fix-8542.py",
 "ef9e285512e1eddcbac0512f853f0b2ac58b57546f9a4bfa7e5621a9eaf8ddcc",
 "\n# All Gaussian rational parameter poles may cancel.","Dixon8")
Dqq=original["Dmatrix"];Sqq=original["source_cover"]
assert Sqq.degree()==418
one=fmpq_poly([1]);zero=fmpq_poly([]);up=fmpq_poly([0,1])
def exact(a,b):
 q,r=divmod(a,b);assert q*b+r==a and not r;return q
def monic(a):
 assert a;return a/a[a.degree()]
C55=monic(exact(Sqq,Sqq.gcd(Sqq.derivative())))
for ff in [up,up-1]:
 q,r=divmod(C55,ff);assert q*ff+r==C55
 if not r:C55=q
C55=monic(C55)
assert C55.degree()==55
assert pdigest(C55)["sha256"]=="29e6fcb5e775a86c83594e6886e61fc8640066f3d6f859702cf719f5d2a71ebf"
common=F9.gcd(Sqq)
say("new_F9_original_source_pole_regular_test",
 originalF9=pdigest(F9),knownSourceSupport=pdigest(C55),
 gcdWithEntireOriginalSourcePolesDegree=int(common.degree()),
 actualOriginalDixonShape=[8,8],oldQQGaussianExecuted=False)
if common.degree()!=0:
 say("INCONCLUSIVE_F9_ORIGINAL_SOURCE_POLE",
  originalSourcePoleShared=True,F9DividesP201Proved=False,
  allCurrentBlocksRetained=True)
 signal.setitimer(signal.ITIMER_REAL,0);raise SystemExit(0)

counts={"fieldReductionProducts":0,"fieldInverseProducts":0,
        "QPolynomialDivisionProducts":0,"DixonRowOperations":0}
cache={}
class K:
 __slots__=("p",)
 def __init__(self,v=0):
  if isinstance(v,K):self.p=v.p;return
  if not isinstance(v,fmpq_poly):v=fmpq_poly([fmpq(v)])
  q,r=divmod(v,F9);assert q*F9+r==v
  self.p=r;counts["fieldReductionProducts"]+=1
 def __bool__(self):return bool(self.p)
 def __eq__(self,v):return self.p==K(v).p
 def __neg__(self):return K(-self.p)
 def __add__(self,v):return K(self.p+K(v).p)
 __radd__=__add__
 def __sub__(self,v):return self+-K(v)
 def __rsub__(self,v):return K(v)+-self
 def __mul__(self,v):return K(self.p*K(v).p)
 __rmul__=__mul__
 def inverse(self):
  assert self
  key=tuple(str(c) for c in self.p.coeffs())
  if key in cache:return cache[key]
  gg,aa,bb=self.p.xgcd(F9);assert aa*self.p+bb*F9==gg
  assert gg.degree()==0
  out=K(aa/gg[0]);assert self*out==1
  cache[key]=out;counts["fieldInverseProducts"]+=1
  return out
 def __truediv__(self,v):return self*K(v).inverse()
 def __rtruediv__(self,v):return K(v)*self.inverse()
 def __pow__(self,n):
  assert n>=0
  ans=K(1);base=self
  while n:
   if n&1:ans=ans*base
   n//=2
   if n:base=base*base
  return ans
def trim(a):
 a=list(a)
 while a and not a[-1]:a.pop()
 return a
def pa(a,b):
 return trim([(a[i] if i<len(a) else K())+(b[i] if i<len(b) else K())
              for i in range(max(len(a),len(b)))])
def ps(a,c):return trim([x*c for x in a])
def pm(a,b):
 if not a or not b:return []
 out=[K() for _ in range(len(a)+len(b)-1)]
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]=out[i+j]+x*y
 return trim(out)
def pdiv(a,b):
 a=trim(a);b=trim(b);assert b
 rem=a[:];quo=[K() for _ in range(max(0,len(a)-len(b)+1))]
 inv=b[-1].inverse()
 while rem and len(rem)>=len(b):
  j=len(rem)-len(b);c=rem[-1]*inv;quo[j]=quo[j]+c
  for i,x in enumerate(b):rem[i+j]=rem[i+j]-c*x
  rem=trim(rem)
 quo=trim(quo)
 assert pa(pm(quo,b),rem)==a
 counts["QPolynomialDivisionProducts"]+=1
 return quo,rem
def xgcd(a,b):
 oldr,r=trim(a),trim(b);olds,s=[K(1)],[];oldt,t=[],[K(1)]
 while r:
  q,rem=pdiv(oldr,r)
  oldr,r=r,rem
  olds,s=s,pa(olds,ps(pm(q,s),K(-1)))
  oldt,t=t,pa(oldt,ps(pm(q,t),K(-1)))
 inv=oldr[-1].inverse()
 out,aa,bb=ps(oldr,inv),ps(olds,inv),ps(oldt,inv)
 assert pa(pm(aa,a),pm(bb,b))==out
 return out,aa,bb
g=[K(co) for co in original["g"]]
hh=[K(co) for co in head.n]
gh,bezg,bezh=xgcd(g,hh)
assert len(gh)==2 and gh[1]==1
qh=-gh[0]
def peval(a,q):
 out=K()
 for c in reversed(a):out=out*q+c
 return out
assert peval(g,qh)==0 and peval(hh,qh)==0
qprime=peval([g[i]*i for i in range(1,len(g))],qh)
assert qprime
def pint(poly):
 return all(int(fmpq(c).denominator)%PRIME for c in poly.coeffs())
integral_all=all(pint(poly) for poly in
 [F9,qh.p]+[c.p for c in bezg]+[c.p for c in bezh])
say("new_F9_exact_original_head_Q_linear_Bezout",
 originalF9=pdigest(F9),QGcdDegree=1,headZeroQCoordinate=pdigest(qh.p),
 originalG4AndHeadAtSameQQRootReturned=True,
 BezoutUsesActualUnstrippedOriginalHead=True,
 completeQQPolynomialBezoutReturned=True,
 BezoutIdentity=digest([[[str(c) for c in x.p.coeffs()] for x in a]
                       for a in [bezg,bezh,gh]]),
 prime=PRIME,wholeF9RootAndBezoutPIntegral=bool(integral_all),
 originalQDerivativeNonzeroOverQQ=True,
 noOldHeadZeroOriginalValueGateExecuted=True)
if not integral_all:
 say("INCONCLUSIVE_F9_FIXED_PRIME_BEZOUT_INTEGRALITY",
  noUnpaidCoefficientInverseTaken=True,
  allCurrentBlocksRetained=True,F9DividesP201Proved=False)
 # Continue the independent QQ pole-divisor target without claiming this bridge.
assert pint(F9)
def modpoly(poly):
 cc=[]
 for c in poly.coeffs():
  c=fmpq(c);den=int(c.denominator)%PRIME;assert den
  cc.append(int(c.numerator)%PRIME*pow(den,-1,PRIME)%PRIME)
 return nmod_poly(cc,PRIME)
bar=modpoly(F9)
assert bar.degree()==9 and int(bar[9])==1
assert bar.gcd(bar.derivative()).degree()==0
const,factors=bar.factor();product=nmod_poly([int(const)],PRIME)
profiles=[]
for ff,ee in factors:
 assert int(ee)==1
 product=product*ff
 profiles.append(mpdigest(ff))
assert product==bar
pattern=sorted(int(ff.degree()) for ff,ee in factors)
say("new_F9_complete_integral_squarefree_reduction",
 actualF9Bar=mpdigest(bar),factorDegrees=pattern,factors=profiles,
 completeFactorProductReturned=True,monicPrimeIntegral=True,
 squarefreeReduction=True,
 currentFourHeadZeroBlocksIdentifiedOnlyIfPattern1134=(pattern==[1,1,3,4]))

def eval_original(co):
 assert co.d.gcd(F9).degree()==0
 ans=K()
 for c in reversed(co.n):ans=ans*qh+K(c)
 out=ans/K(co.d)
 assert out*K(co.d)==ans
 return out
D=[[eval_original(co) for co in row] for row in Dqq]
assert len(D)==8 and all(len(row)==8 for row in D)
A=[row[:] for row in D]
U=[[K(int(i==j)) for j in range(8)] for i in range(8)]
rank=0
for col in range(8):
 pivot=next((i for i in range(rank,8) if A[i][col]),None)
 if pivot is None:continue
 if pivot!=rank:
  A[rank],A[pivot]=A[pivot],A[rank]
  U[rank],U[pivot]=U[pivot],U[rank]
 inv=A[rank][col].inverse()
 A[rank]=[c*inv for c in A[rank]]
 U[rank]=[c*inv for c in U[rank]]
 for i in range(8):
  if i==rank or not A[i][col]:continue
  c=A[i][col]
  A[i]=[x-c*y for x,y in zip(A[i],A[rank])]
  U[i]=[x-c*y for x,y in zip(U[i],U[rank])]
  counts["DixonRowOperations"]+=1
 rank+=1
 say("new_F9_exact_original_Dixon_specialization_pivot",
  column=col,actualRank=rank,wholeQQWeightDegree=9,
  noGenericQQUGaussianReplayed=True)
 if rank==8:break
assert all(sum((U[i][k]*D[k][j] for k in range(8)),K())==A[i][j]
           for i in range(8) for j in range(8))
witness=next((i for i in range(8) if not any(A[i]) and U[i][0]),None)
incompatible=witness is not None
detail={}
if incompatible:
 w=[c/U[witness][0] for c in U[witness]]
 assert w[0]==1
 assert all(sum((w[i]*D[i][j] for i in range(8)),K())==0 for j in range(8))
 detail=dict(exactOriginalLeftAnnihilatorIdentity=digest(
  [[str(c) for c in x.p.coeffs()] for x in w]),
  allEightOriginalColumnProductsZeroReturned=True,
  exactConstantTargetPairingOneReturned=True)
say("new_F9_original_Dixon_pole_divisor_finished",
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 actualQQSpecializedMatrixRank=rank,
 originalConstantTargetNotInRange=incompatible,
 originalSourceAllPolesRegularAtF9=True,
 actualLeftRowOperationMatrixFullyReturned=True,
 F9DividesOldP201Proved=incompatible,
 fixedPrimeWholeBezoutIntegral=bool(integral_all),actualF9BarFactorDegrees=pattern,
 previousFourCompletedBlocksEligibleForHeadZeroProof=(
  incompatible and integral_all and pattern==[1,1,3,4]),
 originalH1GraphExcluded=False,ordinaryISPClaim=False,
 oldGenericQQGaussianExecuted=False,
 old54DimensionalHeadZeroValueGateExecuted=False,
 noNormResultantOrOriginalQRankDriverExecuted=True,
 coefficientPayloadTransmitted=False,encodedOrSplitPayloadCreated=False,
 arithmeticCounts=counts,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,**detail)
signal.setitimer(signal.ITIMER_REAL,0);signal.alarm(0)
