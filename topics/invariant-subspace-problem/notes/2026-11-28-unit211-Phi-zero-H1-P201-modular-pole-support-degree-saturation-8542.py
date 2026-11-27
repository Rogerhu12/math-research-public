#!/usr/bin/env python3
"""NEW arithmetic target: the complete mod-1009 reduction of the unknown P201.

Scope: the published Phi=0, physical D!=0, whole H1 original Dixon graph.
The old exact QQ calculation already gives its unique q=Dixon8^{-1} e0
and the squarefree pole cover C256=C55*P201, deg(P201)=201. This source
does NOT execute that QQ Gaussian calculation or republish the unit target.
It reconstructs only the necessary fixed original 8-by-8 matrix and solves
its NEW mod-1009 image over F_1009(u)[Q]/g4, returning every coordinate.

Arithmetic justification. Let V be the p-Gauss valuation ring of QQ(u).
The fixed matrix entries are checked in the finite free V-algebra V[Q]/g4.
If its reduction is invertible, the actual QQ q is V-integral and its
reduction is the uniquely returned modular vector. Let P* be a p-primitive
scaling of the old monic P201. A sufficiently large power of
u(u-1) C55* P* clears every QQ coordinate denominator of q; its product
with q is then in QQ[u] intersect V = Z_(p)[u]. Hence the squarefree
support of the reduced q's denominators, after removing the known
u(u-1) C55* support, divides the nonzero reduction of P*.
Only if its degree is EXACTLY 201 do we conclude that the old P201 is
monic p-integral and its complete reduction is this squarefree polynomial.
A smaller degree is INCONCLUSIVE; no characteristic-zero factor or point
exclusion follows merely from modular factors.

Existing historical inputs are read only inside the runner. No coefficient
payload, encoded/split data, or recomputable polynomial artifact is emitted.
120 seconds / 1 GiB. 2026-11-28 Asia/Taipei.
"""
import os,time,json,hashlib,signal,resource
from pathlib import Path
from flint import fmpq,fmpq_poly,nmod_poly
START=time.perf_counter()
signal.alarm(120)
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
p=1009
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,separators=(",",":")),flush=True)
class Nonunit(Exception):pass
BASE_NAME="2026-11-28-unit211-Phi-zero-whole-H1-original-biquadratic-Dixon-unit-target-syntax-fix-8542.py"
BASE_SHA="ef9e285512e1eddcbac0512f853f0b2ac58b57546f9a4bfa7e5621a9eaf8ddcc"
PREFIX_SHA="891828ba3b65989ed1f254e864f68b49d48b3c2bef090f343662ba659401b3b8"
base_path=Path(os.environ.get("ISP_H1_ORIGINAL_DIXON_SOURCE",str(Path(__file__).with_name(BASE_NAME))))
base=base_path.read_text()
assert hashlib.sha256(base.encode()).hexdigest()==BASE_SHA
marker="\n# All Gaussian rational parameter poles may cancel."
assert base.count(marker)==1
prefix=base.split(marker,1)[0]
assert hashlib.sha256(prefix.encode()).hexdigest()==PREFIX_SHA
say("new_P201_modular_pole_target_input",
 prime=p,oldQQGaussianReplayed=False,
 originalFullSourceSHA256=BASE_SHA,necessaryPrefixSHA256=PREFIX_SHA,
 newTarget="degree-201 saturation of the primitive P201 reduction",
 historicalParameterFilesReadOnlyInsideRunner=True,
 coefficientPayloadTransmitted=False)
scope={"__name__":"isp_original_H1_Dixon_prefix","__file__":str(base_path)}
exec(compile(prefix,str(base_path)+":necessary-Dixon-construction","exec"),scope)
signal.alarm(max(1,120-int(time.perf_counter()-START)))
Dqq=scope["Dmatrix"];g=scope["g"];Sqq=scope["source_cover"]
assert len(Dqq)==8 and all(len(row)==8 for row in Dqq)
assert Sqq.degree()==418
qexact=scope["exact"];qmonic=scope["monic"]
one=fmpq_poly([1]);up=fmpq_poly([0,1])
# This known source support is needed as an input to the NEW pole comparison.
# No factorization/value-fiber return or old C256/q construction is executed.
C55=qmonic(qexact(Sqq,Sqq.gcd(Sqq.derivative())))
removed=[]
for factor in [up,up-1]:
 qq,rr=divmod(C55,factor)
 assert qq*factor+rr==C55
 if not rr:
  C55=qq;removed.append(str(factor))
C55=qmonic(C55)
craw=json.dumps([str(c) for c in C55.coeffs()],separators=(",",":")).encode()
assert C55.degree()==55
assert hashlib.sha256(craw).hexdigest()=="29e6fcb5e775a86c83594e6886e61fc8640066f3d6f859702cf719f5d2a71ebf"
say("new_P201_known_source_support_reconstructed_as_input",
 sourcePoleDegree=int(Sqq.degree()),knownSquarefreeSupportDegree=55,
 knownSupportSHA256=hashlib.sha256(craw).hexdigest(),
 onlyPreviouslyPaidLinearFactorsRemoved=removed,
 oldC55FactorizationAndValueFibresReplayed=False,
 oldQQGaussianReplayed=False)
def integer_valuation(n):
 n=abs(int(n));assert n
 e=0
 while n%p==0:n//=p;e+=1
 return e
def gauss_valuation(poly):
 cc=[fmpq(c) for c in poly.coeffs() if c]
 if not cc:return None
 return min(integer_valuation(c.numerator)-integer_valuation(c.denominator) for c in cc)
def pscale(exponent):
 return fmpq(p**exponent) if exponent>=0 else fmpq(1,p**(-exponent))
def modular_profile(poly):
 raw=json.dumps([int(c) for c in poly.coeffs()],separators=(",",":")).encode()
 return dict(degree=int(poly.degree()),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
def mp(v=()):
 if isinstance(v,nmod_poly):return v
 if isinstance(v,fmpq_poly):v=v.coeffs()
 if isinstance(v,(int,fmpq)):v=[v]
 out=[]
 for co in v:
  c=fmpq(co);den=int(c.denominator)%p
  if not den:raise Nonunit("a p-Gauss-normalized coefficient is not 1009-integral")
  out.append(int(c.numerator)%p*pow(den,-1,p)%p)
 return nmod_poly(out,p)
mz=mp();mo=mp(1);mg=[mp(c) for c in g]
def mexact(a,b):
 q,r=divmod(a,b);assert q*b+r==a and not r
 return q
def mreduce(cc):
 cc=list(cc)
 while len(cc)<4:cc.append(mz)
 original=cc[:];quot=[mz for _ in range(max(0,len(cc)-4))]
 for j in range(len(cc)-1,3,-1):
  co=cc[j];quot[j-4]=quot[j-4]+co
  for k in range(4):cc[j-4+k]=cc[j-4+k]-co*mg[k]
  cc[j]=mz
 returned=cc[:]
 for j,co in enumerate(quot):
  for k in range(5):returned[j+k]=returned[j+k]+co*mg[k]
 assert returned==original
 return cc[:4]
def mdet(mat):
 aa=[row[:] for row in mat];n=len(aa);prev=mo;sign=1
 if not n:return mo
 for j in range(n-1):
  if not aa[j][j]:
   sw=next((i for i in range(j+1,n) if aa[i][j]),None)
   if sw is None:return mz
   aa[j],aa[sw]=aa[sw],aa[j];sign=-sign
  pivot=aa[j][j]
  for i in range(j+1,n):
   for k in range(j+1,n):
    aa[i][k]=mexact(aa[i][k]*pivot-aa[i][j]*aa[j][k],prev)
   aa[i][j]=mz
  prev=pivot
 return sign*aa[-1][-1]
cache={}
class MA:
 def __init__(self,v=0,d=None):
  if isinstance(v,MA) and d is None:self.n=v.n[:];self.d=v.d;return
  nn=mreduce([mp(co) for co in v] if isinstance(v,(tuple,list)) else [mp(v)])
  dd=mo if d is None else mp(d);assert dd
  gg=dd
  for co in nn:gg=gg.gcd(co)
  dd=mexact(dd,gg);nn=[mexact(co,gg) for co in nn]
  inv=pow(int(dd[dd.degree()]),-1,p)
  self.n=[co*inv for co in nn];self.d=dd*inv
 def __bool__(self):return any(self.n)
 def __neg__(self):return MA([-co for co in self.n],self.d)
 def __add__(self,v):
  v=MA(v);gg=self.d.gcd(v.d);l=mexact(v.d,gg);r=mexact(self.d,gg)
  return MA([a*l+b*r for a,b in zip(self.n,v.n)],self.d*l)
 __radd__=__add__
 def __sub__(self,v):return self+-MA(v)
 def __rsub__(self,v):return MA(v)+-self
 def __mul__(self,v):
  v=MA(v);cc=[mz for _ in range(7)]
  for i,a in enumerate(self.n):
   for j,b in enumerate(v.n):
    if a and b:cc[i+j]=cc[i+j]+a*b
  return MA(cc,self.d*v.d)
 __rmul__=__mul__
 def __eq__(self,v):
  v=MA(v);return self.n==v.n and self.d==v.d
 def regular_numerator(self):
  cols=[mreduce([mz]*j+self.n[:]) for j in range(4)]
  return [[cols[j][i] for j in range(4)] for i in range(4)]
 def inverse(self):
  key=tuple(tuple(int(c) for c in n.coeffs()) for n in self.n)+(tuple(int(c) for c in self.d.coeffs()),)
  if key in cache:return cache[key]
  mat=self.regular_numerator();de=mdet(mat)
  if not de:raise Nonunit("actual whole Q4 modular Dixon pivot is a nonunit")
  nums=[]
  for j in range(4):
   co=mdet([[mat[r][c] for c in range(4) if c!=j] for r in range(1,4)])
   nums.append(((-1)**j)*co*self.d)
  out=MA(nums,de);assert self*out==1
  cache[key]=out;return out
 def __pow__(self,n):
  assert n>=0
  out=MA(1);a=self
  while n:
   if n&1:out=out*a
   n//=2
   if n:a=a*a
  return out

def mmonic(poly):
 assert poly
 return poly*pow(int(poly[poly.degree()]),-1,p)
def modular_entry(co,label):
 vd=gauss_valuation(co.d);assert vd is not None
 for nn in co.n:
  vn=gauss_valuation(nn)
  if vn is not None and vn<vd:
   raise Nonunit(label+": original fixed matrix entry is not p-Gauss-integral")
 scale=pscale(-vd)
 den=co.d*scale
 nums=[nn*scale for nn in co.n]
 assert gauss_valuation(den)==0
 for nn in nums:assert gauss_valuation(nn) is None or gauss_valuation(nn)>=0
 denbar=mp(den);assert denbar
 return MA([mp(nn) for nn in nums],denbar),vd
def main():
 # C55 is already known from exact QQ source support. Its reduction is
 # used only for removing a known support from a LOWER-bound polynomial.
 # No original modular geometric fiber is discarded by this subtraction.
 if gauss_valuation(C55)!=0:
  raise Nonunit("known monic C55 is not p-integral at this fixed prime")
 Cbar=mp(C55);assert Cbar.degree()==55
 Dbar=[];valuations=[]
 for i,row in enumerate(Dqq):
  out=[]
  for j,co in enumerate(row):
   outco,vd=modular_entry(co,"Dixon[%d,%d]"%(i,j))
   out.append(outco);valuations.append(vd)
  Dbar.append(out)
 say("new_P201_fixed_original_matrix_Gauss_integral",
  wholeQAlgebraRank=4,originalMatrixShape=[8,8],
  all64EntriesReturnedInGaussIntegerRing=True,
  denominatorGaussValuationMinimum=min(valuations),
  denominatorGaussValuationMaximum=max(valuations),
  knownC55ReductionDegree=55,knownC55Reduction=modular_profile(Cbar),
  noParameterSpecialization=True)
 # The eight actual whole-algebra unit pivots below are ONLY an arithmetic
 # way to prove this fixed matrix invertible over the residue function
 # field. Their parameter zero loci are not geometric units.
 work=[row[:]+[MA(1 if i==0 else 0)] for i,row in enumerate(Dbar)]
 pivot_receipts=[]
 for j in range(8):
  pivot_row=None;inverse=None;nonunit_rows=[]
  for i in range(j,8):
   if not work[i][j]:continue
   try:
    iv=work[i][j].inverse()
   except Nonunit:
    nonunit_rows.append(i);continue
   assert work[i][j]*iv==1
   pivot_row=i;inverse=iv;break
  if pivot_row is None:
   say("new_P201_modular_pivot_not_returned",
    completedPivots=j,column=j,nonunitRows=nonunit_rows,
    allOriginalWeightFibresRetained=True,
    P201ReductionIdentified=False,noNewQQExclusion=True)
   return False
  if pivot_row!=j:work[j],work[pivot_row]=work[pivot_row],work[j]
  work[j]=[co*inverse for co in work[j]]
  assert work[j][j]==1
  for i in range(8):
   if i==j:continue
   a=work[i][j]
   if a:work[i]=[x-a*y for x,y in zip(work[i],work[j])]
   assert not work[i][j]
  rec=dict(column=j,chosenOriginalCurrentRow=pivot_row,
           allFourPivotInverseCoordinatesReturned=True,
           exactInvertibleRowOperation=True,
           currentMaximumNumeratorDegree=max(
            int(nn.degree()) for row in work for co in row for nn in co.n),
           currentMaximumDenominatorDegree=max(
            int(co.d.degree()) for row in work for co in row))
  pivot_receipts.append(rec)
  say("new_P201_modular_Dixon_pivot",**rec)
 assert all(work[i][j]==(1 if i==j else 0) for i in range(8) for j in range(8))
 qbar=[work[i][8] for i in range(8)]
 for i in range(8):
  assert sum((Dbar[i][j]*qbar[j] for j in range(8)),MA())==(1 if i==0 else 0)
 # Full 8x4 coefficient multiplication return, together with eight actual
 # invertible row operations, proves qbar is the reduction of the old q.
 den=mo
 for co in qbar:
  den=mmonic(den*mexact(co.d,den.gcd(co.d)))
 for co in qbar:
  quo=mexact(den,co.d)
  assert quo*co.d==den
  common=co.d
  for nn in co.n:common=common.gcd(nn)
  assert common.degree()==0
 unit,factors=den.factor()
 product=mp(int(unit));rad=mo;factor_profiles=[]
 for ff,ee in factors:
  ee=int(ee)
  assert ee>=1
  product=product*ff**ee
  rad=rad*mmonic(ff)
  factor_profiles.append(dict(**modular_profile(ff),multiplicity=ee))
 assert product==den
 rad=mmonic(rad)
 assert rad.gcd(rad.derivative()).degree()==0
 known=mp([0,1])*mp([-1,1])*Cbar
 shared=rad.gcd(known)
 support=mmonic(mexact(rad,shared))
 assert support*shared==rad
 assert support.gcd(known).degree()==0
 degree=int(support.degree())
 # A degree larger than the paid QQ degree cannot be a valid reduction
 # lower bound. Stop with an assertion, never reinterpret it as success.
 assert degree<=201
 target_achieved=(degree==201)
 support_factors=[]
 if target_achieved:
  uu,fac=support.factor();returned=mp(int(uu))
  for ff,ee in fac:
   assert int(ee)==1
   returned=returned*ff
   support_factors.append(dict(**modular_profile(ff),multiplicity=1))
  assert returned==support
 say("new_P201_primitive_reduction_degree_saturation",
  prime=p,actualMatrixInvertibilityReturned=True,
  originalModularSolveAll32CoordinatesReturned=True,
  oldExactQQPoleCover="C256=C55*P201; deg(P201)=201",
  commonActualModularDenominator=modular_profile(den),
  squarefreeActualModularPoleSupport=modular_profile(rad),
  knownClosedSupportIntersection=modular_profile(shared),
  lowerBoundForPrimitiveP201Reduction=modular_profile(support),
  finalDenominatorFactors=factor_profiles,
  exactDegree201Saturation=target_achieved,
  monicP201InZlocalizedAtPrimeProved=target_achieved,
  fullP201ReductionIdentified=target_achieved,
  P201SquarefreeReductionProved=target_achieved,
  P201ReductionFactors=(support_factors if target_achieved else []),
  incompleteWhenDegreeBelow201=(not target_achieved),
  noCharacteristicZeroFactorIdentification=True,
  noOriginalWeightOrValueExclusionClaim=True,
  coefficientPayloadTransmitted=False,encodedOrSplitPayloadCreated=False)
 return target_achieved
try:
 completed=main()
except Nonunit as exc:
 say("new_P201_fixed_prime_eligibility_not_returned",
  reason=str(exc),allOriginalWeightFibresRetained=True,
  P201ReductionIdentified=False,noNewQQExclusion=True)
 completed=False
say("new_P201_modular_pole_input_finished",
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 originalFullSourceSHA256=BASE_SHA,necessaryPrefixSHA256=PREFIX_SHA,
 degreeSaturationTargetReturned=completed,
 oldQQGaussianReplayed=False,oldQConstantTargetRepublished=False,
 oldC256OrC55ValueGateReplayed=False,
 ordinaryISPClaim=False,wholeH1Excluded=False,
 coefficientPayloadTransmitted=False,encodedOrSplitPayloadCreated=False,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)
