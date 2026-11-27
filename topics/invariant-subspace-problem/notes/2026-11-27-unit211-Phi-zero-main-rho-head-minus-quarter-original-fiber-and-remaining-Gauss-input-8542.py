#!/usr/bin/env python3
"""NEW exact v=-1/4 original fiber and deflated saved main weight Gauss.
Read actual saved C6/C9, monic QQ R543, C71, and full old mod S1363.
No old determinant or resultant is repeated. H7=0 is NEVER subjected
to C6/C9. 120 seconds /1 GiB. 2026-11-28 Asia/Taipei.
"""
import time,json,hashlib,zlib,base64,signal,resource,math
from pathlib import Path
from flint import fmpq,fmpq_poly,nmod_poly
signal.alarm(120)
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
began=time.perf_counter()
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-began)
 print(json.dumps(kw,separators=(",",":")),flush=True)
def read(name,sha):
 raw=Path(__file__).with_name(name).read_bytes()
 assert hashlib.sha256(raw).hexdigest()==sha
 return json.loads(raw)
def unpack(rec):
 raw=zlib.decompress(base64.b64decode(rec["data"]))
 assert hashlib.sha256(raw).hexdigest()==rec["payloadSha256"]
 assert len(raw)==rec["uncompressedBytes"]
 return json.loads(raw)
def checkpoint(label,obj):
 raw=json.dumps(obj,separators=(",",":")).encode()
 data=base64.b64encode(zlib.compress(raw,9)).decode()
 assert zlib.decompress(base64.b64decode(data))==raw
 say("new_exact_checkpoint",label=label,uncompressedBytes=len(raw),
  payloadSha256=hashlib.sha256(raw).hexdigest(),data=data)
def profile(p):
 raw=json.dumps([str(c) for c in p.coeffs()],separators=(",",":")).encode()
 return dict(degree=int(p.degree()),rawBytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
spec=unpack(read(
 "2026-11-27-unit211-Phi-zero-main-rho-head-P6-P9-specialized-exact-input-8542.json",
 "83365529c18018b101f2c3fc2ad08fa921bc2155746062a68b5135c9d2315501"))
cover=unpack(read(
 "2026-11-27-unit211-Phi-zero-main-rho-head-monic-543-weight-cover-exact-input-8542.json",
 "0907f3ed6794ea36570f7c3c27b7822fdf6097e1fd4572bc7452e7422793d391"))
oldmod=unpack(read(
 "2026-11-27-unit211-Phi-zero-main-rho-head-C6-C71-modular-projection-exact-input-8542.json",
 "e55a5c4fc29442a47b26a378c02a1c2b12d9e571c37f7f646d5b067433e94eb4"))
oldc=read(
 "2026-11-27-unit211-Phi-zero-main-head-zero-C71-29-exact-input-8542.json",
 "9aba3e9a6bb845d4067b530d724d3f407a4687538dbe569066b7adfdb7e993d7")
cobj=unpack(oldc["polynomial"])
assert spec["variables"]==["v","lam"] and cobj["variables"]==["v","lam"]
R=fmpq_poly([fmpq(c) for c in cover["coefficientsAscending"]])
assert R.degree()==543 and R[543]==1
assert profile(R)["sha256"]=="f444ec14999509523a440d2a48410871f71c4e5c1b077db41c03c80773d8d952"
h7=fmpq_poly([1,2,-4,42,15,-12,36,48])
assert spec["unpaidH7Ascending"]==[str(c) for c in h7.coeffs()]
target=fmpq(-1,4)
def evalp(p,x):
 r=fmpq(0)
 for c in reversed(p.coeffs()):r=r*x+c
 return r
unit_values=[target,target-1,target+1,2*target+1,3*target+1,4*target**2+3*target+1]
assert all(unit_values) and evalp(h7,target)
def specialize(terms,expected_degree):
 cc=[fmpq(0) for _ in range(expected_degree+1)]
 seen=set()
 for i,j,c in terms:
  i,j=int(i),int(j);assert (i,j) not in seen and 0<=j<=expected_degree
  seen.add((i,j));cc[j]=cc[j]+fmpq(c)*target**i
 return fmpq_poly(cc)
polys=[specialize(spec["C6"],6),specialize(spec["C9"],9),specialize(cobj["terms"],29)]
say("new_minus_quarter_same_original_full_fiber",
 target=str(target),firstHeadH7Value=str(evalp(h7,target)),
 originalUnitValues=[str(x) for x in unit_values],
 originalInputNames=["C6","C9","C71"],
 fullSpecializedDegrees=[int(p.degree()) for p in polys],
 allOriginalLambdaLeadingZeroTermsRetained=True,
 C6C9UsedOnlyAfterActualH7Nonzero=True,
 wholeH7StillUnpaid=True,
 noOriginalProjectionReplayed=True)
g=fmpq_poly([]);tags=[fmpq_poly([]) for _ in range(3)]
steps=[]
for j in range(3):
 if not polys[j]:
  steps.append(dict(input=j,identicallyZeroOriginalFiberPolynomial=True));continue
 if not g:
  scale=1/polys[j][polys[j].degree()]
  g=polys[j]*scale;tags[j]=fmpq_poly([scale])
  assert tags[j]*polys[j]==g
  steps.append(dict(input=j,gcd=profile(g),firstNonzeroWholeInput=True));continue
 gg,a,b=g.xgcd(polys[j]);assert a*g+b*polys[j]==gg
 tags=[a*x for x in tags];tags[j]=tags[j]+b;g=gg
 assert sum((tags[k]*polys[k] for k in range(3)),fmpq_poly([]))==g
 steps.append(dict(input=j,gcd=profile(g),bezoutDegrees=[int(a.degree()),int(b.degree())]))
if not g:
 say("accurate_three_original_fiber_polynomials_identically_zero",
  targetV=str(target),steps=steps,strictPreviouslyProvedMainWeightBound=8,
  wholeMinusQuarterFiberExcluded=False,noTrueQQCoverDeflationUsed=True)
 signal.alarm(0);raise SystemExit(0)
lambda_power=0;originalg=g
while g.degree()>0 and not g[0]:
 quotient=fmpq_poly(list(g.coeffs())[1:])
 assert quotient*fmpq_poly([0,1])==g
 g=quotient;lambda_power+=1
fiber_closed=g.degree()==0
say("complete_new_minus_quarter_original_three_polynomial_return",
 fullQQGcd=profile(originalg),fullQQGcdAscending=[str(c) for c in originalg.coeffs()],
 steps=steps,completeThreeInputBezoutReturned=True,
 removedOnlyOriginalLambdaUnitPower=lambda_power,
 exactRemainingGcd=profile(g),
 entireMinusQuarterOriginalFiberExcluded=fiber_closed,
 noClaimOnOtherH7Fibers=True)
checkpoint("minus_quarter_original_full_fiber_polynomials_and_bezout",
 dict(variable="lambda",targetV=str(target),
 polynomials=[[str(c) for c in p.coeffs()] for p in polys],
 bezoutCoefficients=[[str(c) for c in p.coeffs()] for p in tags],
 fullGcd=[str(c) for c in originalg.coeffs()],
 removedOnlyLambdaPower=lambda_power))
q=fmpq_poly([fmpq(1,4),1]);rem=R;power=0
while True:
 qr,rr=divmod(rem,q)
 if rr:break
 assert qr*q==rem;rem=qr;power+=1
assert rem*q**power==R
say("new_saved_QQ543_actual_linear_candidate_division",
 exactCandidateAscending=[str(c) for c in q.coeffs()],
 actualMultiplicity=power,remainingDegree=int(rem.degree()),
 fullDivisionProductReturned=True,
 deflationAuthorizedOnlyIfWholeOriginalFiberExcluded=fiber_closed)
if not fiber_closed:
 say("accurate_new_minus_quarter_original_fiber_not_closed",
  strictPreviouslyProvedMainWeightBound=8,
  noTrueQQCoverDeflationUsed=True,wholeMainBranchExcluded=False)
 signal.alarm(0);raise SystemExit(0)
p=1009
assert oldmod["prime"]==p and oldmod["fixedOriginalLambdaDegrees"]==[6,29]
assert oldmod["fixedOriginalOrder"]==35
S=nmod_poly([int(c) for c in oldmod["coefficientsAscending"]],p)
assert S.degree()==1363
def reduceq(poly):
 cc=[]
 for c in poly.coeffs():
  den=int(c.denominator)%p;assert den
  inv=pow(den,-1,p);assert den*inv%p==1
  cc.append(int(c.numerator)%p*inv%p)
 out=nmod_poly(cc,p)
 assert out.degree()==poly.degree() and int(out[out.degree()])==1
 return out
assert rem and rem[rem.degree()]==1
Rm=reduceq(rem)
gg,a,b=Rm.xgcd(S)
assert a*Rm+b*S==gg
say("complete_new_true_QQ_main_cover_after_paid_fiber_Gauss",
 prime=p,trueRemainingQQCoverDegree=int(rem.degree()),
 actualRemovedQQLinearMultiplicity=power,
 newFullModGcdDegree=int(gg.degree()),
 newFullModGcdAscending=[int(c) for c in gg.coeffs()],
 fullBezoutDegrees=[int(a.degree()),int(b.degree())],
 fullBezoutProductReturned=True,
 sameSavedFixedOriginalSylvesterOrder=35,
 differentRemainingVWeightsOffH7AtMost=int(gg.degree()),
 fullH7Degree=7,
 strictDifferentMainVWeightsAtMost=7+int(gg.degree()),
 entireMainH7ComplementExcluded=not bool(gg.degree()),
 wholeH7OriginalFiberExcluded=False,wholeMainBranchExcluded=False,
 ordinaryISPClaim=False)
checkpoint("new_true_deflated_QQ_main_weight_cover",
 dict(variable="v",coefficientsAscending=[str(c) for c in rem.coeffs()],
 removedExactQQCandidateAscending=[str(c) for c in q.coeffs()],
 removedMultiplicity=power,wholeRemovedFiberActuallyExcluded=True,
 unpaidSeparateH7Ascending=[str(c) for c in h7.coeffs()]))
say("new_minus_quarter_exact_original_input_finished",
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 noOldProjectionOrFiniteModuleReplayed=True,ordinaryISPClaim=False)
signal.alarm(0)
