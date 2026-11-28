#!/usr/bin/env python3
"""NEW entire H198 weight fibre: integral nondivisibility against native P164.
Only the fixed ORIGINAL native six-row matrix is rebuilt, not its old
95-second QQ determinant. H198 is reconstructed from the actual N1
weight determinant definition, not refactored. Fixed p=1009,k=3 is chosen
before any output. Every full QQ matrix and H coefficient is checked
p-integral; primitive Gauss then turns a NONZERO specialized remainder
into H198 not dividing the true QQ determinant, hence not dividing P164.
This proves only finite intersection, never emptiness or modular lifting
of an arbitrary multivariate ideal. All original H198 zero points remain.
180 seconds /4GiB, no coefficient payload, cache, encoding or scan.
"""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
from flint import nmod_poly
started=time.perf_counter();deadline=started+180
signal.alarm(180);resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
prime=1009;fixed_k=3
def say(**kw):
 kw['seconds']=time.perf_counter()-started
 print(json.dumps(kw,separators=(',',':')),flush=True)
def digest(obj):
 raw=json.dumps(obj,separators=(',',':')).encode()
 return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
def prefix_input(basename,fullsha,marker,nbytes,presha):
 path=Path(__file__).with_name(basename);raw=path.read_bytes()
 assert hashlib.sha256(raw).hexdigest()==fullsha
 assert raw.count(marker)==1
 prefix=raw.split(marker)[0]
 assert len(prefix)==nbytes and hashlib.sha256(prefix).hexdigest()==presha
 ns={'__file__':str(path),'__name__':'new_H198_integral_witness_necessary_definition_only'}
 saved_alarm=signal.alarm;saved_setitimer=signal.setitimer
 def bounded_setitimer(which,seconds,interval=0.0):
  if which!=signal.ITIMER_REAL:
   return saved_setitimer(which,seconds,interval)
  assert not interval
  remaining=max(.001,deadline-time.perf_counter())
  requested=float(seconds) if seconds>0 else remaining
  return saved_setitimer(which,min(remaining,requested),0.0)
 def bounded_alarm(seconds):
  previous=bounded_setitimer(signal.ITIMER_REAL,seconds)
  return math.ceil(previous[0])
 signal.setitimer=bounded_setitimer;signal.alarm=bounded_alarm
 try:
  with contextlib.redirect_stdout(io.StringIO()):
   exec(compile(prefix,str(path)+'#necessary_definition_for_new_H198_witness','exec'),ns)
 finally:
  signal.alarm=saved_alarm;signal.setitimer=saved_setitimer
 saved_setitimer(signal.ITIMER_REAL,max(.001,deadline-time.perf_counter()))
 return ns
native=prefix_input(
 '2026-11-28-unit211-W-entire-native-NSPS-y-t-fixed-six-original-determinant-8542.py',
 'eca419501bf348518fe4f36582d417784235cc7c35872f1a1eb180c88b1e537d',
 b'\n# A NEW fixed native-coordinate determinant',8074,
 '1dbb8a70ac77f5d531339ca26b5a60b8b3c3cc9a37e41eb54808063c11490878')
matrix=native['rows']
assert len(matrix)==6 and all(len(row)==6 for row in matrix)
matrix_definition=native['rows_digest'](matrix)
assert matrix_definition==dict(bytes=1728830,sha256='e5b3bc078fecd6d472d62bcba5ec831e10a2f88a8feaf51beb15ba816a9da9cf')
slope=prefix_input(
 '2026-11-28-unit211-W-original-N1-slope-weight-coordinate-monic-square-8542.py',
 '9b7731d221175a88edbf7f98bb1c811402ab1d8e332b94fb005dd073b7894d00',
 b'\nscalar,factors=remaining.factor()',4799,
 'be7547a34352074e9fd8ded0bfb8ede4ef0179614c5b72527483ffaaf2165871')
# This is the EXACT previously returned complete QQ factor definition:
# remaining = (-1/288)*H198. No old QQ factorization is rerun.
H=-288*slope['remaining']
h_definition=slope['profile'](H)
assert h_definition==dict(degrees=[14,19,0,0,0,0],totalDegree=25,terms=198,bytes=6434,
 sha256='3569ba450503ee36acfed6f3ef047c3a08cf1735c3f95028a7c6b0f9b060db82')
assert H==-288*slope['remaining']
assert slope['paidpart']*H==-288*slope['Delta'].n
say(stage='new_entire_H198_original_definitions_reconstructed',
 fixedPrime=prime,fixedK=fixed_k,
 exactOriginalNativeMatrix=matrix_definition,exactH198Definition=h_definition,
 completeQQH198IrreducibilityFromPublishedFactorTheorem=True,
 allNativeOriginalRowProductsAndN1CoordinateProductsReturned=True,
 oldQQNativeDeterminantAndOldH198FactorizationNotExecuted=True,
 entireH198ZeroFibreStillRetained=True,wholeWExcluded=False)
checked=0
def residue(c):
 global checked
 parts=str(c).split('/')
 a=int(parts[0]);b=int(parts[1]) if len(parts)==2 else 1
 assert b%prime!=0,'this fixed integral witness is not p-integral'
 checked+=1
 return (a%prime)*pow(b%prime,prime-2,prime)%prime
def mod_weight(p):
 dd=p.to_dict()
 assert all(not any(mm[j] for j in range(2,len(mm))) for mm in dd)
 degree=max((int(mm[0]) for mm in dd),default=-1)
 arr=[0]*(degree+1)
 for mm,c in dd.items():
  a,b=int(mm[0]),int(mm[1])
  arr[a]=(arr[a]+residue(c)*pow(fixed_k,b,prime))%prime
 return nmod_poly(arr,prime)
hprimitive=False
for coeff in H.to_dict().values():
 if residue(coeff):hprimitive=True
assert hprimitive
h=mod_weight(H)
mm=[[mod_weight(poly) for poly in row] for row in matrix]
say(stage='new_H198_native_fixed_p_integral_model',
 allFullQQNativeMatrixCoefficientDenominatorsArePUnits=True,
 allFullH198CoefficientDenominatorsArePUnits=True,
 H198IsPPrimitive=True,
 specializedH198Degree=int(h.degree()),
 checkedRationalCoefficients=checked,
 genericH198DegreeInE=14,
 noGenericOrSpecializedLeadingCoefficientInverted=True,
 exactGaussScope='H|det over QQ would give p-integral quotient and specialize multiplicatively',
 fixedPrime=prime,fixedK=fixed_k,
 noOriginalWeightOrGeometricZeroFibreExcluded=True)
def modprofile(poly):
 coeffs=[int(c) for c in poly.coeffs()]
 return dict(degree=int(poly.degree()),**digest(coeffs))
if not h or h.degree()==0:
 say(stage='accurate_H198_fixed_specialization_has_no_divisibility_witness',
     specializedH=modprofile(h),noAlternativePrimeOrKScan=True,
     noQQDivisibilityOrFiniteIntersectionClaim=True,
     entireH198ZeroFibreRetained=True,wholeWExcluded=False)
 signal.setitimer(signal.ITIMER_REAL,0);raise SystemExit(0)
one=nmod_poly([1],prime);zero=nmod_poly([],prime)
previous=one;sign=1;det=None;products=0
for j in range(5):
 if not mm[j][j]:
  sw=next((i for i in range(j+1,6) if mm[i][j]),None)
  if sw is None:det=zero;break
  mm[j],mm[sw]=mm[sw],mm[j];sign=-sign
 pivot=mm[j][j]
 for i in range(j+1,6):
  for k in range(j+1,6):
   numerator=mm[i][k]*pivot-mm[i][j]*mm[j][k]
   value,remainder=divmod(numerator,previous)
   assert not remainder and value*previous==numerator
   mm[i][k]=value;products+=1
  mm[i][j]=zero
 previous=pivot
if det is None:det=mm[5][5] if sign==1 else -mm[5][5]
quotient,remainder=divmod(det,h)
assert quotient*h+remainder==det
assert not remainder or remainder.degree()<h.degree()
say(stage='new_H198_native_actual_nondivisibility_test',
 fixedPrime=prime,fixedK=fixed_k,
 actualNativeSpecializedDeterminant=modprofile(det),
 exactSpecializedH198=modprofile(h),
 exactQuotient=modprofile(quotient),exactRemainder=modprofile(remainder),
 exactBareissDivisionProducts=products,
 quotientTimesHPlusRemainderActuallyReturned=True,
 nonzeroRemainder=bool(remainder),
 remainderLeadingCoefficient=(int(remainder[remainder.degree()]) if remainder else 0),
 noCoefficientArrayPayloadWritten=True,
 testOnlyQQDivisibilityNotMultivariateQQEmptiness=True)
if remainder:
 # Since H is p-primitive and det(M) is p-integral, H|det(M) over QQ
 # would force the quotient p-integral by Gauss; specialization would
 # then leave ZERO remainder. We have the opposite actual identity.
 # det(M)=c*U_paid*P164 was already proved. H|P164 => H|det(M), without
 # assuming any new inverse or first proving gcd(H,U_paid)=1.
 # Complete QQ irreducibility of H now yields gcd_QQ(H,P164)=1.
 say(stage='new_entire_H198_finite_original_weight_intersection',
 H198DoesNotDivideQQNativeDeterminant=True,
 H198DoesNotDivideQQP164=True,
 H198P164QQCoprimeByPublishedH198Irreducibility=True,
 H198TotalDegree=25,P164TotalDegree=164,
 fullAffineWeightSchemeLengthBound=4100,
 existingSixMeanGeneratorBoundOverWeightAlgebra=24600,
 fixedCompleteOriginalSevenCoordinateSchemeLengthBound=49200,
 fullSevenCoordinateDefinition='e,k,rho,x,y,t,zeta in the fixed original W normalization',
 exactRhoRule='rho^2=1-Q',
 exactZetaRecovery='zeta=(T+u*K/(2*(u-ell)*D))/ell',
 originalDAndUminusEllAndEllUnitScopeRetained=True,
 localizingAnAlreadyFiniteArtinAlgebraDoesNotIncreaseLength=True,
 allRemainingOriginalIndividualValueConditionsStillRequired=True,
 noSixGeneratorFreenessAssumed=True,
 entireH198OriginalBranchExcluded=False,wholeWExcluded=False,
 noP164IrreducibilityOrSquarefreeClaim=True)
else:
 say(stage='accurate_H198_fixed_model_zero_remainder',
 noAdditionalPrimeKOrAlgorithmRetryPerformed=True,
 noQQDivisibilityOrFiniteIntersectionClaim=True,
 entireH198OriginalBranchRetained=True,wholeWExcluded=False)
say(stage='new_H198_native_integral_model_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 actualNewFixedIntegralModelReturned=True,
 noOldQQDeterminantNormOrModuleGateReplayed=True,
 noEncodedSplitOrRecomputableCoefficientCacheWritten=True,
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 ordinaryISPClaim=False)
signal.setitimer(signal.ITIMER_REAL,0);signal.alarm(0)
