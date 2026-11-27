#!/usr/bin/env python3
"""NEW full h=k Delta=0 lambda cover and independent original N1 Gauss return.
Two previously paid exact Q projections are regenerated as required inputs,
without their old factor/gcd proof gates. New fixed resultant_u is over QQ.
Its genuine monic p-integrality pays a new independent N1 modular Gauss
return. All fixed-degree head-zero fibers and original variables remain.
180 seconds / 4 GiB; no multi-variable modular emptiness shortcut.
"""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
from flint import fmpq,fmpq_poly,nmod_mpoly_ctx,nmod_poly
signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
start=time.perf_counter();deadline=start+180
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-start)
 print(json.dumps(kw),flush=True)
dep=Path(__file__).with_name("2026-11-27-unit211-equal-singleton-Delta-zero-compact-original-QQ-projections-8542.py")
raw=dep.read_bytes()
assert hashlib.sha256(raw).hexdigest()=="a0e1efb16ec1939e50befbf4844e6cecb1603e17defcfa1b0fa1ae8fcd0abd0b"
marker=b"\nprojected={}"
assert raw.count(marker)==1
env={"__file__":str(dep),"__name__":"__new_exact_lambda_and_N1_Gauss_input__"}
with contextlib.redirect_stdout(io.StringIO()):
 exec(compile(raw.split(marker)[0],str(dep),"exec"),env)
signal.alarm(max(1,math.ceil(deadline-time.perf_counter())))
original=env["ns"]
dpoly,npoly,mean_core,zeroP=env["dpoly"],env["npoly"],env["core"],env["zeroP"]
strip_projected,to_biv,biv_profile=env["strip_projected"],env["to_biv"],env["biv_profile"]
P=to_biv(strip_projected(dpoly.resultant(npoly,"Q"))[0])
M=to_biv(strip_projected(dpoly.resultant(mean_core,"Q"))[0])
assert biv_profile(P)["sha256"]=="8af7c105334af350ef5047ee49cf27a5aadbfa204a11b64f9b7f7b8a352dd49c"
assert biv_profile(M)["sha256"]=="9be04b29c603db94642b6f3df66647427601e79714a1a989a80ba066a7e1cb82"
assert [int(P.degrees()[1]),int(M.degrees()[1])]==[3,17]
say("new_Delta_zero_exact_lambda_projection_input",
 fixedOriginalUDegrees=[3,17],fixedOriginalSylvesterSize=20,
 previousCompleteQQCurvesReconstructed=True,
 oldFactorsAndGcdGatesNotReplayed=True,
 allULeadingZeroFibersRetained=True,claimExcluded=False)
proj=P.resultant(M,"u");assert proj
def univar(p):
 dd={}
 for mm,cc in p.to_dict().items():
  assert int(mm[1])==0
  dd[int(mm[0])]=cc
 return fmpq_poly([dd.get(i,0) for i in range(max(dd,default=-1)+1)])
rawL=univar(proj)
assert rawL.degree()<=848
L=rawL;removed=fmpq_poly([1]);paid_records=[]
for name,atom in original["paid_atoms"]:
 if any(int(mm[1]) or int(mm[2]) for mm in atom.to_dict()):continue
 dd={int(mm[0]):cc for mm,cc in atom.to_dict().items()}
 ap=fmpq_poly([dd.get(j,0) for j in range(max(dd,default=-1)+1)])
 count=0
 while True:
  gg=L.gcd(ap)
  if gg.degree()<=0:break
  nxt,rr=divmod(L,gg);assert not rr and nxt*gg==L
  L=nxt;removed*=gg;count+=1
 if count:paid_records.append(dict(originalLambdaOnlyUnit=name,gcdLoops=count))
lc=L[L.degree()];L=L/lc;removed*=lc
assert L*removed==rawL
def qprofile(p):
 arr=[str(c) for c in p];raw=json.dumps(arr,separators=(",",":")).encode()
 ans=dict(degree=int(p.degree()),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
 if len(raw)<=12000:ans["coefficientsAscending"]=arr
 return ans
say("new_Delta_zero_entire_exact_QQ_lambda_cover",
 fixedOriginalUDegrees=[3,17],rawQQCover=qprofile(rawL),
 monicQQCover=qprofile(L),onlyPaidLambdaRemovals=paid_records,
 allStrippingProductsActuallyReturned=True,allOriginalULeadingZerosRetained=True,
 upperDistinctOriginalLambdaUBasePoints=int(L.degree()),
 noAllQOrFreeGramFiberExclusionClaim=True,claimExcluded=False)

# New independent original N1 cofactor, no replay of the prior 3-column proof.
aa,bb,cc=[original["rows"][x] for x in ["R","W","N1"]]
det=(aa[0]*(bb[1]*cc[2]-bb[2]*cc[1])
    +bb[0]*(cc[1]*aa[2]-cc[2]*aa[1])
    +cc[0]*(aa[1]*bb[2]-aa[2]*bb[1]))
Ncore,_,_=original["strip_paid"](det);Ncore=Ncore/Ncore.coefficient(0)
assert original["profile"](Ncore)["sha256"]=="8c5998f06c4815d3e20173caa8ec85f84e9a336d5bdf4122d39ee97f0d3c8cda"
Nproj=dpoly.resultant(Ncore,"Q")
assert Nproj
Ncurve=to_biv(strip_projected(Nproj)[0])
say("new_Delta_zero_independent_original_N1_Q_projection",
 fixedOriginalQDegrees=[int(dpoly.degrees()[2]),int(Ncore.degrees()[2])],
 necessaryCurve=biv_profile(Ncurve),allQLeadingZeroFibersRetained=True,
 previousCofactorProofGateNotReplayed=True,claimExcluded=False)
def integer_terms(p):
 terms=p.to_dict();den=1
 for cc in terms.values():den=math.lcm(den,int(fmpq(cc).denominator))
 ints={tuple(map(int,mm)):int(fmpq(cc)*den) for mm,cc in terms.items()}
 content=0
 for v in ints.values():content=math.gcd(content,abs(v))
 assert content
 ints={mm:v//content for mm,v in ints.items()}
 return ints
pi,ni=integer_terms(P),integer_terms(Ncurve)
chosen=None
for prime in [1009,1013,1019,1021,1031]:
 lcfs=[]
 for cc in L:
  rat=fmpq(cc);den=int(rat.denominator);num=int(rat.numerator)
  if den%prime==0:break
  lcfs.append((num%prime)*pow(den%prime,-1,prime)%prime)
 else:
  mc=nmod_mpoly_ctx.get(("lam","u"),prime,"lex")
  pm=mc.from_dict({mm:v%prime for mm,v in pi.items()})
  nm=mc.from_dict({mm:v%prime for mm,v in ni.items()})
  if int(pm.degrees()[1])!=int(P.degrees()[1]) or int(nm.degrees()[1])!=int(Ncurve.degrees()[1]):continue
  chosen=(prime,lcfs,pm,nm);break
if chosen is None:
 say("new_Delta_zero_QQ_cover_integral_prime_not_yet_paid",
     triedPrimes=[1009,1013,1019,1021,1031],trueQQCoverStillRetained=True,
     noModularGaussClaim=True)
else:
 prime,lcfs,pm,nm=chosen
 Lbar=nmod_poly(lcfs,prime);assert Lbar.degree()==L.degree() and int(Lbar[Lbar.degree()])==1
 sm=pm.resultant(nm,"u")
 dd={}
 for mm,cc in sm.to_dict().items():
  assert int(mm[1])==0;dd[int(mm[0])]=int(cc)
 Sbar=nmod_poly([dd.get(j,0) for j in range(max(dd,default=-1)+1)],prime)
 g,aa,bb=Lbar.xgcd(Sbar)
 assert aa*Lbar+bb*Sbar==g
 assert g and int(g[g.degree()])==1
 say("new_Delta_zero_independent_original_N1_complete_Gauss_return",
     prime=prime,firstCoverGenuineMonicQQ=True,
     everyExactFirstCoverCoefficientActuallyIntegralAtPrime=True,
     actualFirstCoverDegree=int(Lbar.degree()),
     newFixedOriginalUDegrees=[int(P.degrees()[1]),int(Ncurve.degrees()[1])],
     secondProjectionIsTrueOriginalIntegerSylvesterReduction=True,
     actualSecondModDegree=int(Sbar.degree()),
     actualCommonModDegree=int(g.degree()),
     bezoutCoefficientDegrees=[int(aa.degree()),int(bb.degree())],
     fullBezoutProductActuallyReturned=True,
     commonPolynomialCoefficientsAscending=[int(g[j]) for j in range(g.degree()+1)],
     upperDistinctOriginalLambdaUBasePoints=int(g.degree()),
     entireOriginalDeltaZeroChartExcluded=(g.degree()==0),
     allOriginalQAndULeadingZerosRetained=True,
     ordinaryISPClaim=False)
 if g.degree()>0:
  scalar,factors=L.factor();product=fmpq_poly([scalar]);records=[]
  for fac,mult in factors:
   product*=fac**mult
   phi=fac/fac[fac.degree()]
   cfs=[]
   for cc in phi:
    rat=fmpq(cc);den=int(rat.denominator)
    assert den%prime
    cfs.append((int(rat.numerator)%prime)*pow(den%prime,-1,prime)%prime)
   fm=nmod_poly(cfs,prime);assert fm.degree()==phi.degree()
   support=fm.gcd(g)
   records.append(dict(multiplicity=int(mult),wholeMonicQQFactor=qprofile(phi),
      commonModSupportDegree=int(support.degree()),
      entireQQFactorExcludedByMonicGauss=(support.degree()==0),
      allRootsOfSurvivingQQFactorsRetained=True))
  assert product==L
  say("new_Delta_zero_complete_QQ_factor_and_original_mod_support_return",
      prime=prime,factors=records,fullQQFactorProductActuallyReturned=True,
      noModularFactorInferredToBeQQFactor=True,
      survivingWholeQQFibersStillRequireOriginalReturn=True)
signal.alarm(0)
say("new_Delta_zero_exact_lambda_cover_and_independent_N1_return_complete",
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    ordinaryISPClaim=False,peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
