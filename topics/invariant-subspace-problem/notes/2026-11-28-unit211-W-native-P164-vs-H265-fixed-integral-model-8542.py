#!/usr/bin/env python3
"""NEW fixed integral model to distinguish the whole-W native P164 curve
from the irreducible H265 head curve. Not an emptiness test.
Rebuild ONLY two already-defined small input prefixes. Never execute the
95-second QQ determinant, the failed H-open gate or fifteen-head loop.
At fixed p=1009,k=3, compute the NEW 6x6 determinant in Fp[e], divide by
the exact specialized H, and multiply the quotient identity back.
A nonzero remainder disproves QQ divisibility via the primitive Gauss
lemma. It cannot prove any multivariate QQ ideal empty.
180 seconds /4 GiB; only small definitions, hashes and receipt.
"""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
from flint import nmod_poly
start=time.perf_counter();deadline=start+180
signal.alarm(180);resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**r):
 r['seconds']=time.perf_counter()-start
 print(json.dumps(r,separators=(',',':')),flush=True)
def digest(obj):
 raw=json.dumps(obj,separators=(',',':')).encode()
 return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
here=Path(__file__).resolve().parent
def prefix_input(basename,full_sha,marker,prefix_sha):
 p=here/basename;raw=p.read_bytes()
 assert hashlib.sha256(raw).hexdigest()==full_sha
 assert raw.count(marker)==1
 part=raw.split(marker)[0]
 assert hashlib.sha256(part).hexdigest()==prefix_sha
 ns={'__file__':str(p),'__name__':'necessary_definition_only_for_NEW_integral_model'}
 with contextlib.redirect_stdout(io.StringIO()):
  exec(compile(part,str(p),'exec'),ns)
 signal.alarm(max(1,math.ceil(deadline-time.perf_counter())))
 return ns
native=prefix_input(
 '2026-11-28-unit211-W-entire-native-NSPS-y-t-fixed-six-original-determinant-8542.py',
 'eca419501bf348518fe4f36582d417784235cc7c35872f1a1eb180c88b1e537d',
 b'\n# A NEW fixed native-coordinate determinant',
 '1dbb8a70ac77f5d531339ca26b5a60b8b3c3cc9a37e41eb54808063c11490878')
M=native['rows']
assert len(M)==6 and all(len(r)==6 for r in M)
native_profile=native['rows_digest'](M)
assert native_profile==dict(bytes=1728830,sha256='e5b3bc078fecd6d472d62bcba5ec831e10a2f88a8feaf51beb15ba816a9da9cf')
head=prefix_input(
 '2026-11-28-unit211-W-first-binary-head-open-original-low-value-six-coordinate-return-8542.py',
 'ffa9634230009c3f949e2f9a4e051f891f0ad28769e971bc393cc560da8ffb66',
 b'\n# EXPLICIT conditional chart.',
 '2450ac6ed522c28146882179170ab6de6a4085692fc28098a6a89a6d9852e0c0')
H=head['H']
assert head['prof'](H)['sha256']=='b7f6ab4da28caa429f15fdb73034135568d8e73428aa1e813ee8cca292ba35c3'
assert list(map(int,H.degrees()[:2]))==[16,23] and int(H.total_degree())==30
# The full paid stripping product U is a product of divisors of these
# actual atoms. Each has degree <30, whereas H is QQ irreducible of
# total degree 30. Thus gcd_QQ(H,U)=1, with no factor of H hidden in U.
paid_atom_degrees=[]
for name,atom in native['paid_atoms']:
 assert atom and int(atom.total_degree())<30
 paid_atom_degrees.append([name,int(atom.total_degree())])
# These fixed choices are made before any determinant or ideal output.
p=1009;k0=3
checked_coefficients=0
def mod_q(c):
 global checked_coefficients
 ss=str(c).split('/')
 a=int(ss[0]);b=int(ss[1]) if len(ss)==2 else 1
 assert b%p!=0
 checked_coefficients+=1
 return (a%p)*pow(b%p,p-2,p)%p
def specialize_weight_poly(poly):
 d=poly.to_dict()
 assert all(all(mm[j]==0 for j in range(2,len(mm))) for mm in d)
 degree=max((int(mm[0]) for mm in d),default=-1)
 arr=[0]*(degree+1)
 for mm,c in d.items():
  i,j=int(mm[0]),int(mm[1])
  arr[i]=(arr[i]+mod_q(c)*pow(k0,j,p))%p
 return nmod_poly(arr,p)
# Every QQ coefficient in the FULL matrix definition is checked integral.
# H is p-primitive: at least one entire bivariate coefficient is a p-unit.
h_primitive=any(mod_q(c) for c in H.to_dict().values())
assert h_primitive
h=specialize_weight_poly(H)
assert h.degree()==16
# Preserve the exact known leading identity [e^16]H=k^13*(k+3).
assert int(h[16])==pow(k0,13,p)*(k0+3)%p
mm=[[specialize_weight_poly(c) for c in row] for row in M]
original=[[v for v in row] for row in mm]
say(stage='new_P164_H265_fixed_integral_model_inputs',
 prime=p,fixed_k=k0,
 allFullQQMatrixCoefficientDenominatorsCheckedPUnits=True,
 fullHQQCoefficientsCheckedPIntegral=True,
 HPrimitiveAtPrime=True,HVariableEDegreePreserved=16,
 fullQQHIsIrreducibleByPublishedWholeFactorTheorem=True,
 allPaidAtomsHaveDegreeLessThanIrreducibleH=paid_atom_degrees,
 QQHAndEntirePaidStrippingProductCoprime=True,
 checkedRationalCoefficients=checked_coefficients,
 originalMatrixDefinition=native_profile,
 exactHDefinitionSHA256='b7f6ab4da28caa429f15fdb73034135568d8e73428aa1e813ee8cca292ba35c3',
 oldFullQQDeterminantExecuted=False,oldHOpenGateExecuted=False,
 noNumericalRootOrGeometricSaturationUsed=True)
one=nmod_poly([1],p);zero=nmod_poly([],p)
previous=one;sign=1;det=None;products=0
for j in range(5):
 if not mm[j][j]:
  sw=next((i for i in range(j+1,6) if mm[i][j]),None)
  if sw is None:
   det=zero;break
  mm[j],mm[sw]=mm[sw],mm[j];sign=-sign
 pivot=mm[j][j]
 for i in range(j+1,6):
  for k in range(j+1,6):
   num=mm[i][k]*pivot-mm[i][j]*mm[j][k]
   val,rem=divmod(num,previous)
   assert not rem and val*previous==num
   mm[i][k]=val;products+=1
  mm[i][j]=zero
 previous=pivot
if det is None:det=mm[5][5] if sign==1 else -mm[5][5]
quo,rem=divmod(det,h)
assert quo*h+rem==det and (not rem or rem.degree()<h.degree())
# The exact mod polynomial multiplication below supplies a small witness.
hcoeff=[int(c) for c in h.coeffs()]
rcoeff=[int(c) for c in rem.coeffs()]
say(stage='new_P164_H265_actual_fixed_polynomial_division',
 prime=p,fixed_k=k0,
 fullNativeDeterminantDegree=int(det.degree()),
 specializedH_degree=int(h.degree()),remainder_degree=int(rem.degree()),
 allDeterminantExactDivisionProducts=products,
 quotientTimesHPlusRemainderActuallyReturned=True,
 specializedH=hcoeff,smallRemainder=rcoeff,
 determinantDefinition=digest([int(c) for c in det.coeffs()]),
 quotientDefinition=digest([int(c) for c in quo.coeffs()]),
 remainderDefinition=digest(rcoeff),
 nonzeroRemainder=bool(rem),
 counterexampleToQQDivisibilityOnly=True,
 multivariateQQEmptinessNotInferred=True)
if rem:
 # H primitive in Z_(p)[e,k] and det(M) integral imply:
 # H | det(M) over QQ[e,k] => quotient in Z_(p)[e,k].
 # Reduction and k=3 would force rem=0. Thus H does not divide det(M).
 # Since det(M)=nonzero rational * paid weight product * P, H cannot
 # divide P. H is QQ irreducible, so gcd(H,P)=1. No mod emptiness step.
 say(stage='new_entire_H265_original_weight_points_are_finite',
 QQHeadDoesNotDivideFullNativeDeterminant=True,
 QQHeadDoesNotDivideP164=True,
 QQGcdHAndPIsOneByPublishedHQQIrreducibility=True,
 HTotalDegree=30,PTotalDegree=164,
 distinctComplexWeightPointBound=4920,
 affineWeightAlgebraLengthBound=4920,
 completeOriginalMeanSixGeneratorEnvironmentBound=29520,
 originalPhysicalLocalizationsOnlyDeleteArtinComponents=True,
 noFreeSixGeneratorClaim=True,
 H265EntireOriginalFibreExcluded=False,
 wholeWExcluded=False,
 noClaimAboutP164IrreducibilityOrSquarefreeness=True)
else:
 say(stage='accurate_new_fixed_model_no_nondivisibility_witness',
 fixedPrimeAndKRetained=True,
 noAdditionalPrimeOrKScanPerformed=True,
 noQQDivisibilityOrFiniteIntersectionClaim=True,
 H265EntireOriginalFibreRetained=True,wholeWExcluded=False)
say(stage='new_fixed_integral_head_vs_native_curve_model_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 actualSmallOriginalModelReturned=True,
 noFormerQQDeterminantFactorOrFailedGateReplayed=True,
 noEncodedOrChunkedDataOrRecomputableCoefficientCacheWritten=True,
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 ordinaryISPClaim=False)
signal.alarm(0)
