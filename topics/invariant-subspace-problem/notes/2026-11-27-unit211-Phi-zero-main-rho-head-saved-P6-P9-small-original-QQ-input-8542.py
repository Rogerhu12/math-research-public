#!/usr/bin/env python3
"""NEW original D inputs on the main rho-head-zero Phi chart.
Use ONLY saved P6, saved P9 (five exact fragments), and saved C71.
Specialize u=1+v,Q=1-v,ell=1+2v. The entire first-head-zero septimic
remains separate. First compute a NEW fixed lambda resultant of
degrees at most6/9 (order at most15), over QQ. Only after its exact
return use a NEW fixed mod-prime C6/C71 projection and a full Bezout.
No old cofactor, F6 recurrence, C71 determinant, or frozen high-order
QQ projection is replayed. 120 seconds /1 GiB, all zero fibers retained.
2026-11-28 Asia/Taipei.
"""
import time,json,hashlib,zlib,base64,signal,resource,math
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpq_mpoly_ctx,nmod_poly,nmod_mpoly_ctx
signal.alarm(120);resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
began=time.perf_counter()
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-began)
 print(json.dumps(kw,separators=(",",":")),flush=True)
def dependency(name,sha):
 raw=Path(__file__).with_name(name).read_bytes()
 assert hashlib.sha256(raw).hexdigest()==sha,("wrong pinned original input",name)
 return json.loads(raw)
def checkpoint(label,obj):
 raw=json.dumps(obj,separators=(",",":")).encode()
 encoded=base64.b64encode(zlib.compress(raw,9)).decode()
 assert zlib.decompress(base64.b64decode(encoded))==raw
 pieces=[encoded[i:i+75000] for i in range(0,len(encoded),75000)]
 say("new_main_rho_head_exact_checkpoint",label=label,rawBytes=len(raw),
     rawSHA256=hashlib.sha256(raw).hexdigest(),
     encodedCharacters=len(encoded),chunks=len(pieces),maximumChunkCharacters=75000)
 for i,data in enumerate(pieces):
  say("new_main_rho_head_exact_checkpoint_chunk",label=label,index=i,total=len(pieces),data=data)
def unpack_record(rec):
 raw=zlib.decompress(base64.b64decode(rec["data"]))
 assert hashlib.sha256(raw).hexdigest()==rec["payloadSha256"]
 assert len(raw)==rec["uncompressedBytes"]
 return json.loads(raw)
P6input=dependency(
 "2026-11-27-unit211-Phi-zero-first-quadratic-head-actual-D-core-exact-input-8542.json",
 "7cc9dcf4c8f716055518324966cf8c156c961c5204dfb156ede054f63568765b")
manifest=dependency(
 "2026-11-27-unit211-Phi-zero-first-head-F6-D-exact-input-manifest-8542.json",
 "98f0a4d5af1fe650cacb56db3e11a90bd7d2426b2af670cdd41b0a3ca1b2f5e7")
record=manifest["records"]["polynomial"]
parts=[]
for rec in record["parts"]:
 ob=dependency(rec["name"],rec["sha256"])
 assert len(ob["dataChunk"])==rec["dataCharacters"]
 parts.append(ob["dataChunk"])
encoded="".join(parts)
assert len(encoded)==record["concatenatedBase64Characters"]
assert hashlib.sha256(encoded.encode()).hexdigest()==record["concatenatedBase64Sha256"]
p9raw=zlib.decompress(base64.b64decode(encoded))
assert len(p9raw)==record["metadata"]["uncompressedBytes"]
assert hashlib.sha256(p9raw).hexdigest()==record["metadata"]["payloadSha256"]
P9obj=json.loads(p9raw);P6obj=unpack_record(P6input["polynomial"])
Cinput=dependency(
 "2026-11-27-unit211-Phi-zero-main-head-zero-C71-29-exact-input-8542.json",
 "9aba3e9a6bb845d4067b530d724d3f407a4687538dbe569066b7adfdb7e993d7")
Cobj=unpack_record(Cinput["polynomial"])
assert P6obj["variables"]==P9obj["variables"]==["u","Q","lambda"]
assert len(P6obj["terms"])==3101 and len(P9obj["terms"])==17389
assert Cobj["variables"]==["v","lam"]
ctx=fmpq_mpoly_ctx.get(("v","lam"),"lex")
zero=fmpq_poly([]);one=fmpq_poly([1]);v=fmpq_poly([0,1])
u=1+v;Q=1-v;ell=1+2*v
assert ell*Q==Q-2*(u-1)*(u-2)
assert 2*u-ell*Q-2*u*u==-1-3*v
assert 2*u*(1-u)+ell*Q-Q==-4*v*v
up=[u**i for i in range(74)];qp=[Q**j for j in range(42)]
C71=ctx.from_dict({(int(i),int(j)):fmpq(c) for i,j,c in Cobj["terms"]})
assert list(map(int,C71.degrees()))==[71,29] and len(C71.to_dict())==2111
assert hashlib.sha256(str(sorted(C71.to_dict().items())).encode()).hexdigest()=="d99036cca8046c43f5c4215a78aa46543bab1f8bf587b7aa6de32864e22ac1df"
def profile(p):
 return dict(degrees=list(map(int,p.degrees())),terms=len(p.to_dict()),
  sha256=hashlib.sha256(str(sorted(p.to_dict().items())).encode()).hexdigest())
def pprofile(p):
 raw=json.dumps([str(c) for c in p.coeffs()],separators=(",",":")).encode()
 return dict(degree=int(p.degree()),rawBytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
def from_lambda_coefficients(cc):
 return ctx.from_dict({(i,j):p[i] for j,p in enumerate(cc)
                       for i in range(p.degree()+1) if p[i]})
# Every factor below is a paid ORIGINAL unit on this same main chart.
# M=v*(4v^2+3v+1), u+Q-1=1, T0=-(3v+1).
atoms=[("1-Q or u-1 or u-ell: v",v),
       ("Q: v-1",v-1),("u: v+1",v+1),
       ("ell: 2v+1",2*v+1),("T0: 3v+1",3*v+1),
       ("M/(1-Q): 4v^2+3v+1",4*v*v+3*v+1)]
def specialize(obj,label,degree):
 cc=[fmpq_poly([]) for _ in range(degree+1)];seen=set()
 for ex,c in obj["terms"]:
  i,j,k=map(int,ex)
  assert 0<=i<74 and 0<=j<42 and 0<=k<=degree and (i,j,k) not in seen
  seen.add((i,j,k))
  cc[k]=cc[k]+fmpq(c)*up[i]*qp[j]
 while cc and not cc[-1]:cc.pop()
 assert cc
 initial=from_lambda_coefficients(cc);removed=[]
 for name,a in atoms:
  power=0
  while True:
   qr=[divmod(p,a) for p in cc]
   if any(rem for q,rem in qr):break
   assert all(q*a==p for (q,rem),p in zip(qr,cc))
   cc=[q for q,rem in qr];power+=1
  if power:removed.append([name,power])
 before_lambda=list(cc);power=0
 while cc and not cc[0]:cc=cc[1:];power+=1
 assert [fmpq_poly([]) for _ in range(power)]+cc==before_lambda
 if power:removed.append(["original lambda unit",power])
 assert cc
 result=from_lambda_coefficients(cc)
 say("new_main_rho_head_saved_D_polynomial_specialized",
  label=label,fullSpecialization=profile(initial),remainingCore=profile(result),
  strippedOnlyOriginalUnits=removed,allPureVFactorDivisionsMultipliedBack=True,
  oldOriginalDTargetAndF6RecurrenceNotRecomputed=True)
 return result
C6=specialize(P6obj,"P6",6)
C9=specialize(P9obj,"P9",9)
h7=fmpq_poly([1,2,-4,42,15,-12,36,48])
g=[fmpq_poly([64,-272,512,-544,336,-112,16]),
   fmpq_poly([-112,348,-496,440,-248,80,-12]),
   fmpq_poly([60,-123,104,-52,13]),fmpq_poly([-13,fmpq(53,4),-3]),one]
def evaluate(p,arg):
 out=zero
 for c in reversed(p.coeffs()):out=out*arg+c
 return out
actual_head=sum((evaluate(c,u)*Q**j for j,c in enumerate(g)),zero)
assert 4*actual_head==h7
assert (1+2*v)*(2*u-(1+2*v)*Q)-u*u==v*(4*v*v+3*v+1)
say("new_main_rho_head_complete_original_first_head_zero_fiber",
 originalIdentity="4*(-12 H1)(1+v,1-v)=h7(v)",
 unpaidWholeH7Ascending=[str(c) for c in h7.coeffs()],
 allH7RootsRetainedSeparately=True,
 wholeMainRhoHeadBranchExcluded=False)
checkpoint("new_saved_P6_P9_main_actual_specializations",
 {"variables":["v","lam"],"C6":[[int(e[0]),int(e[1]),str(c)] for e,c in sorted(C6.to_dict().items())],
  "C9":[[int(e[0]),int(e[1]),str(c)] for e,c in sorted(C9.to_dict().items())],
  "unpaidH7Ascending":[str(c) for c in h7.coeffs()]})
def primitive_integer(p):
 den=1
 for c in p.to_dict().values():den=math.lcm(den,int(fmpq(c).denominator))
 dd={e:int(fmpq(c)*den) for e,c in p.to_dict().items()}
 content=0
 for c in dd.values():content=math.gcd(content,abs(c))
 assert content
 out=ctx.from_dict({e:c//content for e,c in dd.items()})
 assert out*fmpq(content,den)==p
 return out,dict(integerMultiplier=den,integerContent=content)
I6,s6=primitive_integer(C6);I9,s9=primitive_integer(C9)
m,n=int(I6.degrees()[1]),int(I9.degrees()[1])
assert 0<=m<=6 and 0<=n<=9
say("new_fixed_small_original_main_QQ_resultant_started",
 originalLambdaDegrees=[m,n],fixedSylvesterOrder=m+n,
 actualIntegerInputProfiles=[profile(I6),profile(I9)],
 integerInputScales=[s6,s9],
 firstHeadZeroEntireH7Retained=True,resourceBudgetSeconds=120)
R=I6.resultant(I9,"lam")
if not R:
 say("accurate_new_fixed_small_main_QQ_resultant_identically_zero",
  fixedOriginalLambdaDegrees=[m,n],fixedOrder=m+n,
  noFiniteWeightCoverReturned=True,noCommonFactorDeclaredUnit=True,
  noLargerQQProjectionAttempted=True,wholePhiFaceExcluded=False)
 signal.alarm(0);raise SystemExit(0)
assert all(int(e[1])==0 for e in R.to_dict())
rv=fmpq_poly([0]*(int(R.degrees()[0])+1))
for e,c in R.to_dict().items():rv[int(e[0])]=c
assert ctx.from_dict({(i,0):c for i,c in enumerate(rv.coeffs()) if c})==R
say("complete_new_fixed_small_main_original_QQ_resultant",
 actualLambdaDegrees=[m,n],fixedSylvesterOrder=m+n,
 exactQQResultant=pprofile(rv),
 allLambdaLeadingZeroVFibersPreservedByFixedOriginalSylvester=True)
# This is a chart decomposition, not an unproved global H7 inverse:
# all h7=0 weights remain explicit; only its complement uses C6/C9.
original_R=rv;removed=[]
for label,a in atoms+[("UNPAID H7 retained as a separate complete branch",h7)]:
 while True:
  g0=rv.gcd(a)
  if g0.degree()<=0:break
  old=rv;rv,rem=divmod(rv,g0);assert not rem and rv*g0==old
  removed.append([label,pprofile(g0)])
rv=rv/rv[rv.degree()]
assert rv and rv[rv.degree()]==1
say("new_main_original_QQ_monic_weight_cover_off_H7",
 exactMonicCover=pprofile(rv),removedExactFactors=removed,
 allUnpaidH7RootsRetainedSeparately=True,
 allOtherRemovedFactorsActualOriginalUnits=True,
 actualIdentityOutsideH7="every original main point has R_remaining(v)=0",
 noLeadingZeroFiberDropped=True)
checkpoint("new_true_QQ_monic_main_weight_cover",
 {"variable":"v","coefficientsAscending":[str(c) for c in rv.coeffs()],
  "unpaidSeparateH7Ascending":[str(c) for c in h7.coeffs()],
  "completeOriginalLambdaDegrees":[m,n],"fixedOriginalOrder":m+n,
  "allOtherRemovedFactorsPhysicalUnits":True})
if rv.degree()==0:
 say("complete_new_main_original_weight_return",
  allRemainingMainWeightsSatisfyH7=True,
  exactUnpaidH7Degree=7,differentMainWeightParameterUpperBound=7,
  wholeH7OriginalFiberExcluded=False,wholeMainBranchExcluded=False,
  ordinaryISPClaim=False)
 signal.alarm(0);raise SystemExit(0)
IC,sc=primitive_integer(C71)
new_n=int(IC.degrees()[1]);assert new_n==29
# Choose by exact denominator and fixed-degree preservation only.
# Never choose a prime by its gcd or by the outcome of the new return.
chosen=None;rejected=[]
for prime in [1009,1013,1019,1021,1031,1033,1039]:
 if any(int(c.denominator)%prime==0 for c in rv.coeffs()):
  rejected.append([prime,"true monic QQ cover coefficient denominator"]);continue
 mc=nmod_mpoly_ctx.get(("v","lam"),prime,"lex")
 def pm(p):
  dd={}
  for e,c in p.to_dict().items():
   c=fmpq(c);assert int(c.denominator)==1
   z=int(c.numerator)%prime
   if z:dd[tuple(map(int,e))]=z
  return mc.from_dict(dd)
 f6m,c71m=pm(I6),pm(IC)
 if not f6m or not c71m or int(f6m.degrees()[1])!=m or int(c71m.degrees()[1])!=new_n:
  rejected.append([prime,"new fixed original lambda degree"]);continue
 chosen=prime;break
if chosen is None:
 say("accurate_new_main_no_good_small_prime_selected",
  exactQQWeightCoverAlreadyReturned=True,rejectedPrimes=rejected,
  noModularGaussConclusion=True,wholeMainBranchExcluded=False)
 signal.alarm(0);raise SystemExit(0)
prime=chosen
say("new_main_fixed_original_C6_C71_modular_projection_started",
 prime=prime,rejectedPrimes=rejected,
 trueMonicQQWeightCoverDegree=int(rv.degree()),
 bothOriginalLambdaDegrees=[m,new_n],fixedOriginalOrder=m+new_n,
 noCompleteQQC71ResultantExpanded=True)
smod=f6m.resultant(c71m,"lam")
if not smod:
 say("accurate_new_main_fixed_C6_C71_resultant_zero_mod_prime",
  prime=prime,previousExactQQCoverRemains=True,
  noStrongerGaussReturnClaimed=True,wholeMainBranchExcluded=False)
 signal.alarm(0);raise SystemExit(0)
scf=[0]*(int(smod.degrees()[0])+1)
for e,c in smod.to_dict().items():
 assert int(e[1])==0;scf[int(e[0])]=int(c)
Sm=nmod_poly(scf,prime)
rc=[]
for c in rv.coeffs():
 den=int(c.denominator)%prime;assert den
 iv=pow(den,-1,prime);assert iv*den%prime==1
 rc.append(int(c.numerator)%prime*iv%prime)
Rm=nmod_poly(rc,prime);assert Rm.degree()==rv.degree() and int(Rm[Rm.degree()])==1
gg,aa,bb=Rm.xgcd(Sm);assert aa*Rm+bb*Sm==gg
say("complete_new_main_saved_original_D_and_C71_Gauss_return",
 prime=prime,locallyMonicQQWeightCoverDegree=int(rv.degree()),
 newFixedOriginalLambdaDegrees=[m,new_n],fixedOriginalOrder=m+new_n,
 newFullModResultantDegree=int(Sm.degree()),
 actualFullCommonDegree=int(gg.degree()),
 actualFullCommonCoefficientsAscending=[int(c) for c in gg.coeffs()],
 completeNewBezoutProductReturned=True,
 bezoutDegrees=[int(aa.degree()),int(bb.degree())],
 differentWeightParametersOffH7UpperBound=int(gg.degree()),
 retainedWholeH7DifferentRootUpperBound=7,
 strictDifferentMainWeightParameterUpperBound=7+int(gg.degree()),
 countsWeightsNotAllPossibleLambdaTzValues=True,
 everyUnpaidH7AndLambdaLeadingZeroFiberRetained=True,
 wholeMainRhoHeadBranchExcluded=False,wholePhiFaceExcluded=False,ordinaryISPClaim=False)
checkpoint("new_fixed_original_C6_C71_full_mod_resultant",
 {"prime":prime,"variable":"v","coefficientsAscending":[int(c) for c in Sm.coeffs()],
  "fixedOriginalLambdaDegrees":[m,new_n],"fixedOriginalOrder":m+new_n,
  "noCharacteristicZeroDegreeClaimForThisNewResultant":True})
cf,fac=gg.factor();prod=nmod_poly([int(cf)],prime);out=[]
for p,k in fac:
 prod*=p**k;out.append(dict(degree=int(p.degree()),multiplicity=int(k),
                           coefficientsAscending=[int(c) for c in p.coeffs()]))
assert prod==gg
say("new_main_saved_D_actual_remaining_modular_factors_only",
 factors=out,completeProductReturned=True,noIndividualQQFactorLiftClaim=True)
say("new_main_rho_head_saved_D_input_finished",
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 noOldP6P9OrC71MathGateReplayed=True,ordinaryISPClaim=False)
signal.alarm(0)
