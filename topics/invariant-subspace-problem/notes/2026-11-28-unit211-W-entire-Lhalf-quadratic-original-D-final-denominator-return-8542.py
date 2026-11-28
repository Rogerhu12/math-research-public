#!/usr/bin/env python3
"""NEW whole Lhalf weight curve, six-row actual original D return.
Work in the COMPLETE quadratic algebra E=QQ(k)[e]/Lhalf, not a selected
root and not a numerical fibre. The simultaneously column-cancelled
native six matrix is invertible over E by the already established
complete Pprime/Lhalf coprimality. Solve the actual row target dprime,
return every original coordinate, clear ONLY final reduced coefficient
denominators, and lift modulo the primitive Lhalf polynomial.
All finite k poles, quadratic ramification and original Lhalf fibres
are retained. Intermediate Gaussian poles are recovered by the final
polynomial identity, not declared physical units.
No seven-row e-module, native QQ determinant, norm projection, old
modular primary, or prior family gate is rerun.
180s /4GiB; small sources/parameters/hashes/receipts only.
"""
import json,time,hashlib,signal,resource,contextlib,io,math,itertools
from pathlib import Path
from flint import fmpq,fmpq_poly
START=time.perf_counter();DEADLINE=START+180
signal.alarm(180);resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**kw):
 kw['seconds']=time.perf_counter()-START
 print(json.dumps(kw,separators=(',',':')),flush=True)
def digest(obj):
 raw=json.dumps(obj,separators=(',',':')).encode()
 return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
path=Path(__file__).with_name('2026-11-28-unit211-W-entire-native-NSPS-y-t-fixed-six-original-determinant-8542.py')
raw=path.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='eca419501bf348518fe4f36582d417784235cc7c35872f1a1eb180c88b1e537d'
mark=b'\n# A NEW fixed native-coordinate determinant'
assert raw.count(mark)==1
prefix=raw.split(mark)[0]
assert len(prefix)==8074
assert hashlib.sha256(prefix).hexdigest()=='1dbb8a70ac77f5d531339ca26b5a60b8b3c3cc9a37e41eb54808063c11490878'
native={'__file__':str(path),'__name__':'new_D_target_original_rows_only'}
oa=signal.alarm;ot=signal.setitimer
def timer(which,seconds,interval=0.0):
 if which!=signal.ITIMER_REAL:return ot(which,seconds,interval)
 assert not interval
 left=max(.001,DEADLINE-time.perf_counter())
 return ot(which,min(left,float(seconds) if seconds>0 else left),0.0)
def alarm(seconds):return math.ceil(timer(signal.ITIMER_REAL,seconds)[0])
signal.alarm=alarm;signal.setitimer=timer
try:
 with contextlib.redirect_stdout(io.StringIO()):
  exec(compile(prefix,str(path)+'#new_D_target_prefix','exec'),native)
finally:
 signal.alarm=oa;signal.setitimer=ot
 ot(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
ns=native['ns'];R=native['R'];ctx=native['ctx']
zero,one=native['zero'],native['one'];ep,kp=ns['ep'],ns['kp']
basis=native['basis'];variables=native['variables']
mats=native['matrices'];errors=native['errors']
original=native['original'];verify=native['verify']
paid_poly=native['paid_poly'];paid_scalar=native['paid_scalar']
baseM=[r[:] for r in native['rows']];baseTags=[r[:] for r in native['traces']]
assert native['rows_digest'](baseM)==dict(bytes=1728830,sha256='e5b3bc078fecd6d472d62bcba5ec831e10a2f88a8feaf51beb15ba816a9da9cf')
L=4*kp*ep**2-(kp**2+4*kp+8)*ep-(kp**2+6*kp+8)
assert L
qq_divisions=0;coefficient_checks=0;mod_divisions=0;mod_inverse_count=0
def exact(poly,divisor):
 global qq_divisions
 q=poly/divisor
 assert q*divisor==poly
 qq_divisions+=1;return q
def profile(poly):
 return dict(degrees=list(map(int,poly.degrees()[:2])),
 totalDegree=int(poly.total_degree()),terms=len(poly.to_dict()),
 **digest([[[int(z) for z in m],str(c)] for m,c in sorted(poly.to_dict().items())]))
def rowprofile(row):return dict(
 degrees=[max(int(q.degrees()[i]) for q in row) for i in [0,1]],
 terms=sum(len(q.to_dict()) for q in row),
 **digest([[[[int(z) for z in m],str(c)] for m,c in sorted(q.to_dict().items())] for q in row]))
def transform(row):
 return [row[0]+row[1]/2+row[2]/2+row[4]/4,row[1],row[2],row[3],row[4],row[5]]
def deflate(row):
 transformed=transform(row)
 out=[exact(transformed[0],L),exact(transformed[1],L)]+transformed[2:]
 # Actual forward and reverse constant-coordinate products.
 assert transformed==[out[0]*L,out[1]*L]+out[2:]
 reverse=[out[0]*L-out[1]*L/2-out[2]/2-out[4]/4,
          out[1]*L,out[2],out[3],out[4],out[5]]
 assert reverse==row
 return out
# Original D is a quadratic geometry polynomial; take its true
# four-mean reduction, including the complete original multiplier.
drow,dtag=ns['reduce_six'](ns['symbolic']['Dphysical'])
assert not dtag[4] and not dtag[5]
for c in drow:paid_scalar(c)
for c in dtag:paid_poly(c.d)
den=one
for c in drow:den=exact(den,den.gcd(c.d))*c.d
paid_poly(den)
dpoly=[c.n*exact(den,c.d) for c in drow]
dtrace=[R(den)*c for c in dtag]
assert all(R(dpoly[i])==R(den)*drow[i] for i in range(6))
verify(sum((R(dpoly[i])*basis[i] for i in range(6)),R())-R(den)*ns['symbolic']['Dphysical'],dtrace)
dprime=deflate(dpoly)
baseN=[deflate(row) for row in baseM]
say(stage='necessary_same_D_columns_for_new_whole_Lhalf_curve',
 originalKernelColumns=[[1,'1/2','1/2',0,'1/4',0],[0,1,0,0,0,0]],
 constantColumnTransformationDeterminant=1,
 exactLhalf='4*k*e^2-(k^2+4*k+8)*e-(k^2+6*k+8)',
 allBaseRowsAndOriginalDTargetForwardReverseProductsReturned=True,
 QQExactColumnDivisionReturns=qq_divisions,
 originalDTargetMeanTraceReturned=True,
 DTargetPaidDenominator=profile(den),
 deflatedDTarget=rowprofile(dprime),
 deflatedBaseRowProfiles=[rowprofile(r) for r in baseN],
 universalOriginalCofactorIdentity='det(N)*d=dprime*adj(N)*M',
 noLhalfInverse=True,entireLhalfZeroRetained=True,
 noH198OrOtherNewHeadInverse=True,
 originalDTargetValidOnEntireCurrentW=True,
 oldQQNativeDeterminantNotReplayed=True,wholeWExcluded=False)
division_count=0;weight_inverse_count=0
def pp(value):
 return value if isinstance(value,fmpq_poly) else fmpq_poly([value])
def qdiv(a,b):
 global division_count
 q,r=divmod(a,b);assert not r and q*b==a
 division_count+=1;return q
class F:
 __slots__=('n','d')
 def __init__(self,n=0,d=None):
  if isinstance(n,F):
   assert d is None;self.n=n.n;self.d=n.d;return
  n=pp(n);d=pp(1) if d is None else pp(d);assert d
  if not n:self.n=pp(0);self.d=pp(1);return
  g=n.gcd(d);n=qdiv(n,g);d=qdiv(d,g);c=d[d.degree()]
  self.n=n/c;self.d=d/c
 def __bool__(self):return bool(self.n)
 def __neg__(self):return F(-self.n,self.d)
 def __add__(self,other):
  other=F(other)
  if not self:return other
  if not other:return self
  return F(self.n*other.d+other.n*self.d,self.d*other.d)
 __radd__=__add__
 def __sub__(self,other):return self+-F(other)
 def __rsub__(self,other):return F(other)+-self
 def __mul__(self,other):
  other=F(other)
  if not self or not other:return F()
  return F(self.n*other.n,self.d*other.d)
 __rmul__=__mul__
 def __truediv__(self,other):
  other=F(other);assert other
  return F(self.n*other.d,self.d*other.n)
 def __rtruediv__(self,other):return F(other)/self
 def __pow__(self,n):
  if n<0:return F(self.d**(-n),self.n**(-n))
  return F(self.n**n,self.d**n)
 def __eq__(self,other):
  other=F(other);return self.n*other.d==other.n*self.d
 def data(self):return [[str(v) for v in self.n.coeffs()],[str(v) for v in self.d.coeffs()]]
kF=F(fmpq_poly([0,1]))
r1=(kF*kF+4*kF+8)/(4*kF)
r0=(kF*kF+6*kF+8)/(4*kF)
class W:
 __slots__=('a','b')
 def __init__(self,a=0,b=0):
  if isinstance(a,W):
   assert b==0;self.a=a.a;self.b=a.b;return
  self.a=F(a);self.b=F(b)
 def __bool__(self):return bool(self.a) or bool(self.b)
 def __neg__(self):return W(-self.a,-self.b)
 def __add__(self,other):
  other=W(other);return W(self.a+other.a,self.b+other.b)
 __radd__=__add__
 def __sub__(self,other):return self+-W(other)
 def __rsub__(self,other):return W(other)+-self
 def __mul__(self,other):
  other=W(other)
  return W(self.a*other.a+r0*self.b*other.b,
           self.a*other.b+self.b*other.a+r1*self.b*other.b)
 __rmul__=__mul__
 def inv(self):
  global weight_inverse_count
  # Multiplication norm in the WHOLE monic quadratic algebra.
  norm=self.a*self.a+r1*self.a*self.b-r0*self.b*self.b
  if not norm:
   say(stage='new_whole_Lhalf_unexpected_generic_pivot_nonunit',
       elementDefinition=digest(self.data()),wholeQuadraticAlgebraNormReturnedZero=True,
       noWholeCurveExclusionOrFinalCoverClaim=True,wholeWExcluded=False)
   raise ArithmeticError('new pivot is not a unit in the complete Lhalf quadratic algebra')
  out=W((self.a+r1*self.b)/norm,-self.b/norm)
  assert self*out==W(1) and out*self==W(1)
  weight_inverse_count+=1;return out
 def __truediv__(self,other):return self*W(other).inv()
 def __rtruediv__(self,other):return W(other)*self.inv()
 def __pow__(self,n):
  if n<0:return self.inv()**(-n)
  out=W(1);base=self
  while n:
   if n&1:out=out*base
   n//=2
   if n:base=base*base
  return out
 def __eq__(self,other):
  other=W(other);return self.a==other.a and self.b==other.b
 def data(self):return [self.a.data(),self.b.data()]

eW=W(0,1);ewpowers=[W(1)]
assert 4*W(kF)*eW*eW-W(kF*kF+4*kF+8)*eW-W(kF*kF+6*kF+8)==W()
kpoly=fmpq_poly([0,1]);O=fmpq_poly([1]);Z=fmpq_poly([])
disc=(kpoly*kpoly+4*kpoly+8)**2+16*kpoly*(kpoly*kpoly+6*kpoly+8)
assert disc==fmpq_poly([64,192,128,24,1])
assert disc-(kpoly*kpoly+12*kpoly+8)**2==-32*kpoly*kpoly
# In QQ(k), a polynomial square with leading coefficient1 is a
# polynomial square. Its k3 and k1 coefficients force k^2+12k+8,
# whose k2 coefficient is160, whereas the discriminant has128.
# Hence the generic quadratic is irreducible. All finite
# ramification fibres nevertheless stay in the eventual polynomial identity.
def weightpoly(poly):
 dd=poly.to_dict();by_e={}
 for mon,cc in dd.items():
  assert not any(mon[j] for j in range(2,len(mon)))
  ie,ik=int(mon[0]),int(mon[1])
  row=by_e.setdefault(ie,{})
  row[ik]=row.get(ik,fmpq(0))+cc
 maxe=max(by_e,default=0)
 while len(ewpowers)<=maxe:ewpowers.append(ewpowers[-1]*eW)
 out=W()
 for ie,coeffs in by_e.items():
  arr=[fmpq(0)]*(max(coeffs,default=-1)+1)
  for ik,c in coeffs.items():arr[ik]=c
  out=out+ewpowers[ie]*W(F(fmpq_poly(arr)))
 return out

assert weightpoly(L)==W()
N_E=[[weightpoly(x) for x in row] for row in baseN]
d_E=[weightpoly(x) for x in dprime]
def wprofile(x):
 return dict(aNumeratorDegree=int(x.a.n.degree()),aDenominatorDegree=int(x.a.d.degree()),
             bNumeratorDegree=int(x.b.n.degree()),bDenominatorDegree=int(x.b.d.degree()),
             **digest(x.data()))
def wcost(x):
 if not x:return -1
 return sum(max(0,int(q.degree())) for q in [x.a.n,x.a.d,x.b.n,x.b.d])
say(stage='new_entire_Lhalf_complete_quadratic_original_D_input',
 field='QQ(k)[e]/(4*k*e^2-(k^2+4*k+8)*e-(k^2+6*k+8))',
 wholeQuadraticAlgebraUsed=True,allQuadraticRelationProductsReturned=True,
 genericDiscriminantCoefficientsAscending=[64,192,128,24,1],
 genericIrreducibilityByQuadraticSquareCoefficientComparison=True,
 discriminantNotInverted=True,
 originalSixMatrixDefinition=digest([[x.data() for x in row] for row in N_E]),
 actualOriginalDTargetDefinition=digest([x.data() for x in d_E]),
 previousCoprimalityUsed='full p1009,k3 Pprime/Lhalf Bezout with monic integral lifting',
 noSelectedRootOrNumericalSubstitution=True,
 allFiniteKPoleAndRamificationFibresRetained=True,wholeWExcluded=False)
# Solve N_E^transpose * solution = d_E. Only final solution
# denominators determine the retained k cover. Intermediate row
# pivots are coefficient-field operations; they are not physical units.
aug=[[N_E[j][i] for j in range(6)]+[d_E[i]] for i in range(6)]
row_coordinate_returns=0
def primitive_coefficient_row(row):
 global row_coordinate_returns
 den=O
 for x in row:
  for f in [x.a,x.b]:
   g=den.gcd(f.d);new=qdiv(den,g)*f.d
   assert new*g==den*f.d;den=new
 nums=[]
 for x in row:
  nums.extend([x.a.n*qdiv(den,x.a.d),x.b.n*qdiv(den,x.b.d)])
 content=Z
 for x in nums:
  if x:content=x if not content else content.gcd(x)
 assert content
 nr=[W(F(qdiv(nums[2*j],content)),F(qdiv(nums[2*j+1],content))) for j in range(7)]
 factor=F(den,content)
 for j in range(7):
  assert nr[j]==row[j]*W(factor);row_coordinate_returns+=1
 return nr
aug=[primitive_coefficient_row(row) for row in aug]
pivots=[];inverses=[]
for j in range(6):
 eligible=[i for i in range(j,6) if aug[i][j]]
 assert eligible,'new whole quadratic matrix lost expected rank'
 i=min(eligible,key=lambda z:(wcost(aug[z][j]),z))
 if i!=j:aug[j],aug[i]=aug[i],aug[j]
 pivot=aug[j][j];inverse=pivot.inv()
 assert pivot*inverse==W(1) and inverse*pivot==W(1)
 inverses.append(inverse);pivots.append(dict(column=j,rowSwap=i,pivot=wprofile(pivot)))
 for h in range(j+1,6):
  entry=aug[h][j]
  if not entry:continue
  factor=entry*inverse;oldrow=aug[h][:]
  newrow=[oldrow[c]-factor*aug[j][c] for c in range(7)]
  assert not newrow[j]
  for c in range(7):
   assert newrow[c]+factor*aug[j][c]==oldrow[c];row_coordinate_returns+=1
  aug[h]=primitive_coefficient_row(newrow)
 say(stage='new_whole_Lhalf_actual_original_quadratic_pivot',
     pivot=j,actualTrueNormInverseCount=weight_inverse_count,
     actualRowCoordinateReturns=row_coordinate_returns,
     exactQQkPolynomialDivisionReturns=division_count,
     remainingMaximumCoefficientDegree=max(
      (max(int(y.degree()) for y in [x.a.n,x.a.d,x.b.n,x.b.d])
       for row in aug[j:] for x in row),default=-1),
     pivotDefinition=pivots[-1],
     noFinalCoverOrWholeCurveExclusionClaim=True,wholeWExcluded=False)
solution=[W() for _ in range(6)]
for j in range(5,-1,-1):
 rhs=aug[j][6]-sum((aug[j][h]*solution[h] for h in range(j+1,6)),W())
 solution[j]=rhs*inverses[j]
 assert aug[j][j]*solution[j]==rhs
for j in range(6):
 assert sum((solution[i]*N_E[i][j] for i in range(6)),W())==d_E[j]
say(stage='new_complete_original_D_target_return_in_whole_Lhalf_quadratic_algebra',
 allSixOriginalTargetCoordinatesReturned=True,
 originalRowCoefficientDefinition=digest([x.data() for x in solution]),
 actualTrueNormInverseCount=weight_inverse_count,
 actualQQkExactPolynomialDivisionReturns=division_count,
 noDInverseUsed=True,noSelectedQuadraticRoot=True,
 intermediatePivotZerosNotDiscarded=True,
 finalCoefficientDenominatorsNotYetCleared=True,wholeWExcluded=False)
# Clear only the FINAL, fully reduced source coefficients.
G=O
for x in solution:
 for f in [x.a,x.b]:
  gg=G.gcd(f.d);new=qdiv(G,gg)*f.d
  assert new*gg==G*f.d;G=new
assert G
G=G/G[G.degree()]
def embed(poly):
 return ctx.from_dict({(0,j,0,0,0,0,0,0):c for j,c in enumerate(poly.coeffs()) if c})
multipliers=[];mult_E=[]
for x in solution:
 aa=x.a.n*qdiv(G,x.a.d);bb=x.b.n*qdiv(G,x.b.d)
 ff=embed(aa)+ep*embed(bb)
 ww=W(F(aa),F(bb))
 assert ww==W(F(G))*x
 assert weightpoly(ff)==ww
 multipliers.append(ff);mult_E.append(ww)
for j in range(6):
 assert sum((mult_E[i]*N_E[i][j] for i in range(6)),W())==W(F(G))*d_E[j]
def pp_profile(poly):
 # Only a parameter definition, degree and SHA are retained. Even
 # small recomputable exact cover arrays are not printed or cached.
 cc=[str(c) for c in poly.coeffs()]
 return dict(degree=int(poly.degree()),**digest(cc))
say(stage='new_whole_Lhalf_original_D_polynomial_final_coefficient_cover',
 finalPureKDenominator=pp_profile(G),
 allTwelveFinalPolynomialCoefficientReturns=True,
 allSixClearedWholeQuadraticCoordinatesReturned=True,
 originalIdentity='G*dprime - sum f_i*N_i belongs to (Lhalf) in QQ[e,k]^6',
 polynomialDivisibilityReason='Lhalf primitive in QQ[k][e], exact whole quadratic residues zero, Gauss',
 originalPhysicalConsequence='G(k)*D belongs to I6+(Lhalf) after original native weight localization',
 wholeLhalfNonzeroGOriginalFibresExcluded=True,
 allGZeroFiniteFibresRetained=True,
 allIntermediatePivotZeroFibresRecoveredByFinalCoefficients=True,
 quadraticDiscriminantZeroFibresRetained=True,
 originalTargetIsSameDFromSimultaneousColumnIdentity=True,
 noExpandedOriginalTraceRequiredForThisEstablishedConsequence=True,
 wholeWExcluded=False)
# Return an explicit polynomial lift as well. This is supplementary
# to the complete cleared-coefficient identity above, which already
# has the primitive-polynomial Gauss proof; it is not a new theorem gate.
Gmp=embed(G);lift_profiles=[]
for j in range(6):
 difference=sum((multipliers[i]*baseN[i][j] for i in range(6)),zero)-Gmp*dprime[j]
 quotient=exact(difference,L)
 assert quotient*L==difference
 lift_profiles.append(profile(quotient))
 say(stage='new_whole_Lhalf_original_D_explicit_polynomial_lift_coordinate',
     coordinate=j,actualExactLhalfDivisionReturned=True,
     quotientDefinition=lift_profiles[-1],wholeWExcluded=False)
# Remove only actual already-paid pure-k factors; keep all others
# and all multiplicities. The exact original D identity still applies.
cover=G;paid=O;paid_history=[]
for label,atom in [('k',kpoly),('k+1',kpoly+1),('k+2',kpoly+2),('k+4',kpoly+4)]:
 count=0
 while True:
  gg=cover.gcd(atom)
  if int(gg.degree())==0:break
  cover=qdiv(cover,gg);paid=paid*gg;count+=1
 if count:paid_history.append([label,count])
assert cover*paid==G
cover=cover/cover[cover.degree()]
say(stage='new_entire_Lhalf_original_D_finite_k_return_complete',
 finalUnpaidKCover=pp_profile(cover),
 allOriginalMultiplicityRetained=True,
 removedOnlyOriginalPaidKFactors=paid_history,
 allSixExplicitLhalfPolynomialDivisionProductsReturned=True,
 actualWholeQuadraticTargetProducts=6,
 actualClearedCoefficientTargetProducts=6,
 actualTrueNormInverseCount=weight_inverse_count,
 exactQQkPolynomialDivisionReturns=division_count,
 exactQQWeightPolynomialDivisionReturns=qq_divisions,
 rowCoordinateReturns=row_coordinate_returns,
 temporaryGaussianPivotsDoNotEnterFinalCover=True,
 noDiscriminantInverse=True,noNativeWeightNormDeclaredGloballyPaid=True,
 wholeLhalfOriginalPhysicalBranchExcluded=(int(cover.degree())==0),
 allFiniteKCoverZerosStillOpen=(int(cover.degree())>0),
 wholeWExcluded=False,ordinaryISPClaim=False,
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 noRecomputableLargeCoefficientCacheEncodedOrSplitPayload=True,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.setitimer(signal.ITIMER_REAL,0);signal.alarm(0)
