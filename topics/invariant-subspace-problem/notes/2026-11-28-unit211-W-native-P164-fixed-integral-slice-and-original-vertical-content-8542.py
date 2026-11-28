#!/usr/bin/env python3
"""NEW P164 component prerequisites for a later original weight elimination.
Only the fixed native six ORIGINAL rows are reconstructed. Never execute
the old two-parameter QQ determinant, C8 norm, or lambda resultant.
(1) Fixed p=1009,k=3: prove whether stripping exactly the original paid
supports preserves all 97 e-degrees of the true QQ P164.
(2) Fixed QQ e=2,3,5 slices: remove only common PURE-k paid divisors;
use degree-preserving integral univariate Bezout to test the remaining
common vertical support. No arbitrary multivariate modular emptiness.
180 seconds /4GiB. Source, definitions, hashes and small receipts only.
"""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
from flint import fmpq,fmpq_poly,nmod_poly
started=time.perf_counter();deadline=started+180
signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
prime=1009;fixed_k=3;fixed_e_values=(2,3,5)
def say(**kw):
 kw['seconds']=time.perf_counter()-started
 print(json.dumps(kw,separators=(',',':')),flush=True)
def digest(obj):
 raw=json.dumps(obj,separators=(',',':')).encode()
 return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
def qprofile(p):
 return dict(degree=int(p.degree()),**digest([str(c) for c in p.coeffs()]))
def mprofile(p):
 return dict(degree=int(p.degree()),**digest([int(c) for c in p.coeffs()]))
def rational_parts(c):
 ss=str(c).split('/')
 return int(ss[0]),(int(ss[1]) if len(ss)==2 else 1)
def vp_integer(n):
 assert n
 n=abs(n);v=0
 while n%prime==0:n//=prime;v+=1
 return v
def coefficient_valuation(c):
 a,b=rational_parts(c);assert a
 return vp_integer(a)-vp_integer(b)
def pscale(v):
 return fmpq(1,prime**v) if v>=0 else fmpq(prime**(-v))
integral_checks=0
def residue(c):
 global integral_checks
 a,b=rational_parts(c);assert b%prime
 integral_checks+=1
 return (a%prime)*pow(b%prime,prime-2,prime)%prime
def primitive_mod_univariate(p):
 if not p:return nmod_poly([],prime),dict(zero=True)
 v=min(coefficient_valuation(c) for c in p.coeffs() if c)
 scale=pscale(v);scaled=p*scale
 assert scaled==p*scale
 out=nmod_poly([residue(c) for c in scaled.coeffs()],prime)
 assert out
 return out,dict(zero=False,rationalPValuation=v,
   allScaledCoefficientsPIntegral=True,scaledPolynomialPPrimitive=True,
   degreePreserved=(out.degree()==p.degree()),
   QQDefinition=qprofile(p),modDefinition=mprofile(out))
def prefix_input(basename,fullsha,marker,nbytes,presha):
 path=Path(__file__).with_name(basename);raw=path.read_bytes()
 assert hashlib.sha256(raw).hexdigest()==fullsha
 assert raw.count(marker)==1
 prefix=raw.split(marker)[0]
 assert len(prefix)==nbytes and hashlib.sha256(prefix).hexdigest()==presha
 ns={'__file__':str(path),'__name__':'new_P164_component_prerequisite_only'}
 saved_alarm=signal.alarm;saved_setitimer=signal.setitimer
 def bounded_setitimer(which,seconds,interval=0.0):
  if which!=signal.ITIMER_REAL:return saved_setitimer(which,seconds,interval)
  assert not interval
  remaining=max(.001,deadline-time.perf_counter())
  requested=float(seconds) if seconds>0 else remaining
  return saved_setitimer(which,min(remaining,requested),0.0)
 def bounded_alarm(seconds):
  previous=bounded_setitimer(signal.ITIMER_REAL,seconds)
  return math.ceil(previous[0])
 signal.alarm=bounded_alarm;signal.setitimer=bounded_setitimer
 try:
  with contextlib.redirect_stdout(io.StringIO()):
   exec(compile(prefix,str(path)+'#new_integral_component_input','exec'),ns)
 finally:
  signal.alarm=saved_alarm;signal.setitimer=saved_setitimer
 saved_setitimer(signal.ITIMER_REAL,max(.001,deadline-time.perf_counter()))
 return ns
native=prefix_input(
 '2026-11-28-unit211-W-entire-native-NSPS-y-t-fixed-six-original-determinant-8542.py',
 'eca419501bf348518fe4f36582d417784235cc7c35872f1a1eb180c88b1e537d',
 b'\n# A NEW fixed native-coordinate determinant',8074,
 '1dbb8a70ac77f5d531339ca26b5a60b8b3c3cc9a37e41eb54808063c11490878')
matrix=native['rows'];atoms=native['paid_atoms']
assert len(matrix)==6 and all(len(row)==6 for row in matrix)
definition=native['rows_digest'](matrix)
assert definition==dict(bytes=1728830,sha256='e5b3bc078fecd6d472d62bcba5ec831e10a2f88a8feaf51beb15ba816a9da9cf')
for row in matrix:
 for po in row:
  assert all(not any(mm[j] for j in range(2,len(mm))) for mm in po.to_dict())
say(stage='new_P164_original_matrix_component_definitions',
 matrixDefinition=definition,fixedPrime=prime,fixedK=fixed_k,
 fixedQQESlices=list(fixed_e_values),
 oldQQDeterminantDegrees=[195,268],publishedP164Degrees=[97,123],
 oldQQDeterminantAndAnyOldLambdaNormOrResultantNotExecuted=True,
 allSixOriginalRowSourcesReconstructed=True,wholeWExcluded=False)
def mod_k_slice(po,make_primitive=False):
 dd=po.to_dict()
 assert all(not any(mm[j] for j in range(2,len(mm))) for mm in dd)
 scale=fmpq(1);v=0
 if make_primitive and dd:
  v=min(coefficient_valuation(c) for c in dd.values() if c)
  scale=pscale(v)
 coeffs=[0]*(max((int(mm[0]) for mm in dd),default=-1)+1)
 for mm,c in dd.items():
  ie,ik=int(mm[0]),int(mm[1])
  coeffs[ie]=(coeffs[ie]+residue(c*scale)*pow(fixed_k,ik,prime))%prime
 return nmod_poly(coeffs,prime),v
def exact_det(mm,zero,one):
 mm=[row[:] for row in mm];n=len(mm);previous=one;sign=1;products=0
 assert all(len(row)==n for row in mm)
 if n==0:return one,0
 for j in range(n-1):
  if not mm[j][j]:
   sw=next((i for i in range(j+1,n) if mm[i][j]),None)
   if sw is None:return zero,products
   mm[j],mm[sw]=mm[sw],mm[j];sign=-sign
  pivot=mm[j][j]
  for i in range(j+1,n):
   for k in range(j+1,n):
    numerator=mm[i][k]*pivot-mm[i][j]*mm[j][k]
    value,remainder=divmod(numerator,previous)
    assert not remainder and value*previous==numerator
    mm[i][k]=value;products+=1
   mm[i][j]=zero
  previous=pivot
 return (mm[-1][-1] if sign==1 else -mm[-1][-1]),products
mz=nmod_poly([],prime);mo=nmod_poly([1],prime)
mm=[[mod_k_slice(p)[0] for p in row] for row in matrix]
dn,products=exact_det(mm,mz,mo)
matrix_integral_checks=integral_checks
mod_atoms=[];all_atom_slices_nonzero=True;atom_definitions=[]
for name,atom in atoms:
 aa,valuation=mod_k_slice(atom,True)
 all_atom_slices_nonzero=all_atom_slices_nonzero and bool(aa)
 mod_atoms.append((name,aa))
 atom_definitions.append(dict(name=name,pPrimitiveNormalizationValuation=valuation,
   modSlice=mprofile(aa),sliceNonzero=bool(aa)))
residual=dn;removed=mo;strip_hist=[]
if dn and all_atom_slices_nonzero:
 for name,atom in mod_atoms:
  ct=0
  while residual and atom.degree()>0:
   gg=residual.gcd(atom)
   if gg.degree()<=0:break
   qq,rr=divmod(residual,gg);assert not rr and qq*gg==residual
   residual=qq;removed*=gg;ct+=1
  if ct:strip_hist.append([name,ct])
 assert residual*removed==dn
degree_preserving_slice=bool(dn and dn.degree()==195
 and all_atom_slices_nonzero and residual.degree()==97
 and removed.degree()==98)
slice_monic=residual*(pow(int(residual[residual.degree()]),prime-2,prime)) if residual else mz
say(stage='new_P164_exact_degree_preserving_mod_slice_test',
 fixedPrime=prime,fixedK=fixed_k,
 allFullQQMatrixCoefficientsPIntegral=True,
 matrixRationalCoefficientChecks=matrix_integral_checks,
 actualDeterminant=mprofile(dn),exactBareissProducts=products,
 originalPaidSupportSlices=atom_definitions,allPaidAtomSlicesNonzero=all_atom_slices_nonzero,
 strippedSupportHist=strip_hist,removed=mprofile(removed),remaining=mprofile(residual),
 monicRemaining=mprofile(slice_monic),
 removedTimesRemainingActuallyReturned=(bool(dn) and all_atom_slices_nonzero),
 exactTrueP164MonicSpecializationCertified=degree_preserving_slice,
 proofIfCertified='Gauss: D=U*P, degrees_e(D,U,P)=195,98,97. Nonzero leading degree195 preserves both; paid support removal covers U, and exact removed degree98 leaves no P factor removed.',
 modStripNeverUsedAsAnUnprovedQQFactorization=True,
 trueP164IdentificationOnlyUnderAllCertifiedDegreeConditions=True,
 noWeightOrGeometricPointExcluded=True,wholeWExcluded=False)

# A genuinely new QQ vertical-content test. Only PURE-k factors of the
# very same native paid atoms may be removed, never all their e slices.
qz=fmpq_poly([]);qo=fmpq_poly([1])
def qmonic(p):
 return p*(fmpq(1)/p[p.degree()]) if p else p
def atom_pure_k_content(po):
 by_e={}
 for mm,c in po.to_dict().items():
  assert not any(mm[j] for j in range(2,len(mm)))
  ie,ik=int(mm[0]),int(mm[1])
  by_e.setdefault(ie,{})[ik]=c
 cs=[]
 for ie,dd in sorted(by_e.items()):
  cc=[fmpq(0)]*(max(dd,default=-1)+1)
  for ik,value in dd.items():cc[ik]=value
  cs.append((ie,fmpq_poly(cc)))
 gg=qz
 for ie,cc in cs:gg=gg.gcd(cc)
 gg=qmonic(gg);assert gg
 # Each exact e coefficient is divisible, so this is a genuine
 # global pure-k divisor of the paid atom, not just a slice factor.
 for ie,cc in cs:
  qq,rr=divmod(cc,gg);assert not rr and qq*gg==cc
 return gg
pure_atoms=[(name,atom_pure_k_content(atom)) for name,atom in atoms]
say(stage='new_global_paid_pure_k_support',
 definitions=[dict(name=name,content=qprofile(cc)) for name,cc in pure_atoms],
 everyGlobalECoefficientDivisionActuallyReturned=True,
 noSpecializedNonverticalPaidAtomUsedAsVerticalUnit=True,
 wholeWExcluded=False)
def qq_e_slice(po,evalue):
 dd=po.to_dict()
 out=[fmpq(0)]*(max((int(mm[1]) for mm in dd),default=-1)+1)
 for mm,c in dd.items():out[int(mm[1])]+=c*(evalue**int(mm[0]))
 return fmpq_poly(out)
dqq=[]
for evalue in fixed_e_values:
 mm=[[qq_e_slice(po,evalue) for po in row] for row in matrix]
 det,nproducts=exact_det(mm,qz,qo);dqq.append(det)
 say(stage='new_fixed_QQ_native_vertical_slice_returned',
     fixedE=evalue,definition=qprofile(det),
     exactBareissProducts=nproducts,
     allExactDivisionProductsReturned=True,
     transientPivotZeroFibresPreservedByPolynomialIdentity=True,
     oldTwoParameterDeterminantNotExecuted=True,wholeWExcluded=False)
first=next((j for j,poly in enumerate(dqq) if poly),None)
vertical_certified=False
if first is None:
 say(stage='accurate_new_vertical_model_all_three_fixed_slices_zero',
     allThreeFixedSlicesRetained=True,noQQVerticalComponentClaim=True,
     noAdditionalESliceScan=True,wholeWExcluded=False)
else:
 remaining=dqq[first];paid=qo;hist=[]
 for name,atom in pure_atoms:
  ct=0
  while atom.degree()>0 and remaining:
   gg=remaining.gcd(atom)
   if gg.degree()<=0:break
   qq,rr=divmod(remaining,gg);assert not rr and qq*gg==remaining
   remaining=qq;paid*=gg;ct+=1
  if ct:hist.append([name,ct])
 assert paid*remaining==dqq[first]
 common_paid=qmonic(paid)
 for poly in dqq:common_paid=common_paid.gcd(poly)
 common_paid=qmonic(common_paid);assert common_paid
 # Prove its support is paid by actual division, independently of
 # the gcd algorithm choosing a smaller global common divisor.
 test=common_paid;paid_product=qo
 for name,atom in pure_atoms:
  while atom.degree()>0 and test:
   gg=test.gcd(atom)
   if gg.degree()<=0:break
   qq,rr=divmod(test,gg);assert not rr and qq*gg==test
   test=qq;paid_product*=gg
 assert test.degree()==0 and test*paid_product==common_paid
 quotients=[]
 for poly in dqq:
  qq,rr=divmod(poly,common_paid);assert not rr and qq*common_paid==poly
  quotients.append(qq)
 mods=[];primitive_records=[]
 for poly in quotients:
  mm,info=primitive_mod_univariate(poly);mods.append(mm);primitive_records.append(info)
 degree_ok=all(info.get('zero') or info['degreePreserved'] for info in primitive_records)
 # Full univariate Bezout, including zero slices if any.
 gg=mz;comb=[mz,mz,mz]
 for i,poly in enumerate(mods):
  if not gg and not poly:continue
  gnew,ss,tt=gg.xgcd(poly)
  assert ss*gg+tt*poly==gnew
  comb=[ss*c for c in comb];comb[i]+=tt;gg=gnew
 assert sum((comb[i]*mods[i] for i in range(3)),mz)==gg
 if gg and gg.degree()==0:
  scale=pow(int(gg[0]),prime-2,prime)
  comb=[scale*c for c in comb];gg*=scale
  assert gg==mo and sum((comb[i]*mods[i] for i in range(3)),mz)==mo
 vertical_certified=bool(degree_ok and gg==mo)
 say(stage='new_P164_vertical_common_support_integral_return',
     commonPaidQQDivisor=qprofile(common_paid),
     commonDivisorTimesAllThreeQQQuotientsActuallyReturned=True,
     itsCompleteGlobalPureKSupportPaidByActualDivisions=True,
     allThreePrimitiveQQQuotients=primitive_records,
     allNonzeroQuotientKDegreesPreserved=degree_ok,
     actualModCommonDivisor=mprofile(gg),
     fullThreeTermModBezoutReturned=True,
     BezoutDefinition=digest([[int(c) for c in pp.coeffs()] for pp in comb]),
     allQQCommonVerticalDivisorsAreOriginallyPaid=vertical_certified,
     trueP164HasNoNonconstantQQPureKContent=vertical_certified,
     proofIfCertified='A nonconstant QQ common divisor of the three quotients remains nonconstant mod p by Gauss and degree preservation, contrary to the returned Bezout1. Any pure-k factor of P divides all three D slices, hence the paid common divisor, impossible since native P was stripped of exactly these original atom supports.',
     anyUnprovedCommonVerticalSupportRetained=not vertical_certified,
     noExtraPrimeOrSliceScan=True,noMultivariateQQEmptinessClaim=True,
     wholeWExcluded=False)
say(stage='new_P164_component_prerequisites_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 fixedP164DegreePreservingModelProved=degree_preserving_slice,
 globalQQPureKContentExcluded=vertical_certified,
 noNewWeightCurveOrResultantYet=True,
 noOriginalPointOrEntireWExclusionClaim=True,
 noOldGateReplayed=True,noCoefficientCacheOrEncodedSplitPayloadWritten=True,
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 ordinaryISPClaim=False)
signal.setitimer(signal.ITIMER_REAL,0);signal.alarm(0)
