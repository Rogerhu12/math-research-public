#!/usr/bin/env python3
"""NEW saved-P6 necessary condition on the complete exceptional Phi chart.
No old cofactor, Gram reduction, first-head rule, or long module is rebuilt.
Specialize the already proved original D-target polynomial at
u=(rho+3)/2,Q=1-rho^2,ell=3/2.  Keep the entire first-head-zero fiber
by multiplying its exact unpaid rho-quartic h4.  Compute a NEW fixed
original rho resultant mod1009, then NEW full Bezout against the true
QQ-divided, locally monic R and the other original projection S.
Every discarded scalar rho factor is an already paid physical unit;
all specialized rho-leading zeros remain in the fixed Sylvester.
2026-11-28 Asia/Taipei. 120 seconds /1 GiB. Four saved JSON dependencies.
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
 data=Path(__file__).with_name(name).read_bytes()
 assert hashlib.sha256(data).hexdigest()==sha,("wrong pinned input",name)
 return json.loads(data)
inputF=dependency(
 "2026-11-27-unit211-Phi-zero-exceptional-F26-exact-input-8542.json",
 "67c73f8f5fef33d509ffebd8165487e5b6abcc59fe391acc4075da1f22287d61")
inputG=dependency(
 "2026-11-27-unit211-Phi-zero-exceptional-PB-core-and-mod-resultant-exact-input-8542.json",
 "74891d2b2f8bd21f74ff063cef7aeed85532a2378e71dac07ad5cfc4d240c8c9")
inputH=dependency(
 "2026-11-27-unit211-Phi-zero-exceptional-mixed-core-and-mod-return-exact-input-8542.json",
 "a9ab01ff03d894ed1fe6033b68268ecbf7b9d36dc2cd4ff3d7bf69b771387073")
inputP6=dependency(
 "2026-11-27-unit211-Phi-zero-first-quadratic-head-actual-D-core-exact-input-8542.json",
 "7cc9dcf4c8f716055518324966cf8c156c961c5204dfb156ede054f63568765b")
def unpack_record(rec):
 raw=zlib.decompress(base64.b64decode(rec["data"]))
 assert hashlib.sha256(raw).hexdigest()==rec["payloadSha256"]
 assert len(raw)==rec["uncompressedBytes"]
 return json.loads(raw)
ctx=fmpq_mpoly_ctx.get(("rho","lam"),"lex")
rawF=unpack_record(inputF["polynomial"])
assert rawF["variables"]==["rho","lam"]
F=ctx.from_dict({(int(i),int(j)):fmpq(c) for i,j,c in rawF["terms"]})
assert list(map(int,F.degrees()))==[26,26] and len(F.to_dict())==729
assert hashlib.sha256(str(sorted(F.to_dict().items())).encode()).hexdigest()=="9057238c5d37c8cd9f62f3f512dcff1f6d2e385cd6c0e39250a571713f0aaac7"
rawP=unpack_record(inputP6["polynomial"])
assert rawP["variables"]==["u","Q","lambda"] and len(rawP["terms"])==3101
zero=fmpq_poly([]);one=fmpq_poly([1])
r=fmpq_poly([0,1]);u=(r+3)/2;Q=1-r*r
up=[u**i for i in range(40)];qp=[Q**i for i in range(21)]
coeff=[zero for _ in range(7)]
seen=set()
for ex,cc in rawP["terms"]:
 i,j,k=map(int,ex)
 assert 0<=i<=39 and 0<=j<=20 and 0<=k<=6 and (i,j,k) not in seen
 seen.add((i,j,k));coeff[k]=coeff[k]+fmpq(cc)*up[i]*qp[j]
# Actual polynomial change of weights, with no cofactor recomputation.
specialized=ctx.from_dict({(i,k):p[i] for k,p in enumerate(coeff)
                           for i in range(p.degree()+1) if p[i]})
assert specialized and int(specialized.degrees()[1])<=6
def profile(p):
 return dict(degrees=list(map(int,p.degrees())),terms=len(p.to_dict()),
  sha256=hashlib.sha256(str(sorted(p.to_dict().items())).encode()).hexdigest())
# This exact H1 residual was previously saved in the original four heads.
g=[fmpq_poly([64,-272,512,-544,336,-112,16]),
   fmpq_poly([-112,348,-496,440,-248,80,-12]),
   fmpq_poly([60,-123,104,-52,13]),
   fmpq_poly([-13,fmpq(53,4),-3]),one]
def evaluate(poly,arg):
 out=zero
 for c in reversed(poly.coeffs()):out=out*arg+c
 return out
gsub=sum((evaluate(c,u)*(Q**j) for j,c in enumerate(g)),zero)
h4=fmpq_poly([9,-18,44,-14,11])
assert 4*gsub==r*r*(r+1)**2*h4
assert (u-1)*2==r+1 and (1-Q)==r*r
assert -Q-4*(u-1)==(r-3)*(r+1)
assert 2*(u+Q-1)==-(2*r-3)*(r+1)
say("new_saved_original_D_polynomial_exceptional_specialization",
 originalP6Profile=inputP6["polynomial"]["core"],
 actualSpecializedP6=profile(specialized),
 exactOriginalFirstHeadIdentity="(-12 H1)=rho^2(rho+1)^2*h4/4",
 unpaidEntireFirstHeadFactorAscending=[str(c) for c in h4.coeffs()],
 sameOriginalExceptionalWeights=True,noOldCofactorOrDTargetRecomputed=True)
# Remove only genuine already-paid pure-rho units, with all coefficient
# divisions multiplied back.  h4 is NOT in this list and is NOT inverted.
removed=[]
atoms=[("1-Q: rho",r),("Q and u-1: rho+1",r+1),("Q: rho-1",r-1),
       ("u: rho+3",r+3),("T0: rho-3",r-3),
       ("u+Q-1: 2rho-3",2*r-3)]
for label,a in atoms:
 multiplicity=0
 while True:
  qr=[divmod(c,a) for c in coeff]
  if any(rem for q,rem in qr):break
  assert all(q*a==old for (q,rem),old in zip(qr,coeff))
  coeff=[q for q,rem in qr];multiplicity+=1
 if multiplicity:removed.append([label,multiplicity])
assert any(coeff)
core=ctx.from_dict({(i,k):p[i] for k,p in enumerate(coeff)
                    for i in range(p.degree()+1) if p[i]})
H4=ctx.from_dict({(i,0):c for i,c in enumerate(h4.coeffs()) if c})
newNecessary=core*H4
assert newNecessary and newNecessary==H4*core
say("new_entire_exceptional_original_D_necessary_polynomial",
 exactStrippedP6=profile(core),newEntireNecessary=profile(newNecessary),
 strippedOnlyPaidPureRhoFactors=removed,
 unpaidHeadZeroFactorKeptAsMultiplicand=True,
 fullOriginalSamePointNecessity="h4(rho)*P6_specialized=0",
 coversBothH1NonzeroAndEntireH1Zero=True,
 noLambdaOrUnclassifiedParameterUnitAdded=True)
def primitive_integer(p):
 dd=1
 for c in p.to_dict().values():dd=math.lcm(dd,int(fmpq(c).denominator))
 ints={e:int(fmpq(c)*dd) for e,c in p.to_dict().items()}
 content=0
 for c in ints.values():content=math.gcd(content,abs(c))
 assert content
 ints={e:c//content for e,c in ints.items()}
 out=ctx.from_dict(ints)
 assert out*fmpq(content,dd)==p
 return out,dict(integerMultiplier=dd,integerContent=content)
FI,scF=primitive_integer(F);NI,scN=primitive_integer(newNecessary)
m,n=int(FI.degrees()[0]),int(NI.degrees()[0])
assert m==26
prime=1009;mc=nmod_mpoly_ctx.get(("rho","lam"),prime,"lex")
def reduce_integer(p):
 out={}
 for e,c in p.to_dict().items():
  c=fmpq(c);assert int(c.denominator)==1
  if int(c.numerator)%prime:out[tuple(map(int,e))]=int(c.numerator)%prime
 return mc.from_dict(out)
fm,nm=reduce_integer(FI),reduce_integer(NI)
assert fm and nm
if int(fm.degrees()[0])!=m or int(nm.degrees()[0])!=n:
 say("accurate_new_original_fixed_input_bad_prime_rho_degree",
  fixedQQDegrees=[m,n],actualModDegrees=[int(fm.degrees()[0]),int(nm.degrees()[0])],
  fixedSylvesterNotYetReturned=True,existing112BoundUnchanged=True)
 raise SystemExit(0)
say("new_fixed_original_h4P6_Sylvester_input",
 fixedOriginalRhoDegrees=[m,n],fixedOriginalOrder=m+n,
 originalQQPrimitiveInputScales=[scF,scN],
 bothRhoDegreesRetainedAtPrime=True,prime=prime,
 noQQResultantExpanded=True,allSpecializedLambdaHeadZeroFibersRetained=True)
# The native operation returns the exact reduction of this fixed original
# Sylvester determinant. No parameter leading factor is inverted in the
# resulting polynomial, including at its zero lambda fibers.
res=fm.resultant(nm,"rho")
if not res:
 say("accurate_new_original_h4P6_resultant_zero_mod1009",
  fixedOriginalRhoDegrees=[m,n],fixedOriginalOrder=m+n,
  newModularPolynomialIsZero=True,existing112BoundUnchanged=True,
  noCharacteristicZeroEmptinessClaim=True)
 raise SystemExit(0)
rc=[0]*(int(res.degrees()[1])+1)
for e,c in res.to_dict().items():
 assert int(e[0])==0;rc[int(e[1])]=int(c)
newS=nmod_poly(rc,prime)
def encode_coefficients(p):
 raw=json.dumps([int(p[i]) for i in range(p.degree()+1)],separators=(",",":")).encode()
 data=base64.b64encode(zlib.compress(raw,9)).decode()
 assert zlib.decompress(base64.b64decode(data))==raw
 return dict(degree=int(p.degree()),polynomialSHA256=hashlib.sha256(str(p).encode()).hexdigest(),
             rawBytes=len(raw),rawSHA256=hashlib.sha256(raw).hexdigest(),data=data)
say("complete_new_fixed_original_h4P6_resultant_mod1009",
 fixedQQRhoDegrees=[m,n],fixedOriginalSylvesterOrder=m+n,
 fullResultant=encode_coefficients(newS),
 allRhoLeadingZeroFibersIncluded=True,noQQDegreeClaimForThisNewResultant=True)
def load_mod(rec,sha,degree):
 raw=zlib.decompress(base64.b64decode(rec["fullCoefficientsData"]))
 assert hashlib.sha256(raw).hexdigest()==rec["fullCoefficientsPayloadSha256"]
 p=nmod_poly(json.loads(raw),prime)
 assert p.degree()==degree and hashlib.sha256(str(p).encode()).hexdigest()==sha
 return p
oldR=load_mod(inputG["full_fixed_mod1009_resultant"],
 "f4505a726a6c2691ac52b92ec424160f7cc748d6a9b17751ce8b2f9f3f0eaa85",2033)
oldS=load_mod(inputH["fixed_mod_resultant"],
 "060c2f63b871fec6e649ce3bdfbf29612df9402b07c3c4d381245f639edb8e12",2050)
phi1=fmpq_poly([fmpq(-1,2),1])
phi6=fmpq_poly([fmpq(5,64),fmpq(39,80),fmpq(63,80),
 fmpq(-7,10),fmpq(-9,4),fmpq(3,5),1])
phiD=fmpq_poly([fmpq(1,32),fmpq(-3,16),fmpq(27,32),fmpq(-17,8),
 fmpq(27,8),-3,1])
phiJ=fmpq_poly([fmpq(916,420),fmpq(-3084,420),fmpq(3663,420),fmpq(-1884,420),1])
# Only currently proved QQ multiplicities. In particular phiJ^8 has NOT
# been assumed from the modular multiplicity or the failed whole-g4 lift.
paid=phi1**10*phi6**2*phiD**3*phiJ**4
def mod_qq(p):
 cc=[]
 for c in p.coeffs():
  d=int(c.denominator)%prime;assert d
  inv=pow(d,-1,prime);assert inv*d%prime==1
  cc.append(int(c.numerator)%prime*inv%prime)
 return nmod_poly(cc,prime)
paidmod=mod_qq(paid);R,qrem=divmod(oldR,paidmod)
assert not qrem and R*paidmod==oldR and R.degree()==1977
# Both divisions are NEW: the first includes this new h4P6 resultant.
# Do not repeat the old R/S-only xgcd as an audit gate.
g1,a1,b1=R.xgcd(newS)
assert a1*R+b1*newS==g1
g2,a2,b2=g1.xgcd(oldS)
assert a2*g1+b2*oldS==g2
ar=a2*a1;an=a2*b1;ao=b2
assert ar*R+an*newS+ao*oldS==g2
say("complete_new_h4P6_actual_original_Gauss_return",
 locallyMonicQQRRemainingDegree=1977,
 originalQQR2033DegreeAnd1009LeadingUnitPreviouslyPaid=True,
 removedTrueQQMultiplicities=[10,2,3,4],noUnprovedPhiEightUsed=True,
 newFixedSylvesterRhoDegrees=[m,n],newFixedSylvesterOrder=m+n,
 fullNewModularResultantDegree=int(newS.degree()),
 afterNewConditionGcdDegree=int(g1.degree()),
 finalCommonDegree=int(g2.degree()),finalCommonCoefficientsAscending=[int(c) for c in g2.coeffs()],
 fullThreeOriginalProjectionBezoutReturned=True,
 finalBezoutCoefficientDegrees=[int(ar.degree()),int(an.degree()),int(ao.degree())],
 strictDifferentOrderedBasePointBound=min(112,int(g2.degree())),
 boundFromThisSpecificNewReturn=int(g2.degree()),
 F26NoVerticalFibersPreviouslyPaidByQQIrreducibility=True,
 allUnpaidFirstHeadZeroRootsAndLeadingZeroFibersRetained=True,
 wholeExceptionalOrderedBranchExcluded=(g2.degree()==0),
 BCSwappedChartSeparatelyCovered=True,wholePhiFaceExcluded=False,ordinaryISPClaim=False)
cf,fac=g2.factor();back=nmod_poly([int(cf)],prime);out=[]
for p,k in fac:
 back*=p**k
 out.append(dict(degree=int(p.degree()),multiplicity=int(k),
                 coefficientsAscending=[int(c) for c in p.coeffs()]))
assert back==g2
say("new_h4P6_actual_remaining_modular_support_only",
 factors=out,completeFactorProductReturned=True,
 noIndividualQQFactorOrBranchLiftClaim=True)
payload=json.dumps({"variables":["rho","lam"],
 "terms":[[int(e[0]),int(e[1]),str(c)] for e,c in sorted(newNecessary.to_dict().items())]},
 separators=(",",":")).encode()
encoded=base64.b64encode(zlib.compress(payload,9)).decode()
assert zlib.decompress(base64.b64decode(encoded))==payload
say("new_h4P6_exact_original_necessary_input",
 profile=profile(newNecessary),rawBytes=len(payload),
 rawSHA256=hashlib.sha256(payload).hexdigest(),
 encodedCharacters=len(encoded),maximumChunkCharacters=75000)
chunks=[encoded[i:i+75000] for i in range(0,len(encoded),75000)]
for i,data in enumerate(chunks):say("new_h4P6_exact_input_chunk",index=i,total=len(chunks),data=data)
say("new_h4P6_saved_input_attempt_finished",
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 noOldCofactorOrQQProjectionReplayed=True,ordinaryISPClaim=False)
signal.alarm(0)
