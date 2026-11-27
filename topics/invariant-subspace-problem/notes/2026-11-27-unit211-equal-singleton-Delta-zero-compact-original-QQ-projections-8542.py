#!/usr/bin/env python3
"""NEW entire h=k Delta=0 original compatibility and compact-mean projections.
Keep fixed original Q degrees and all Q-leading-zero fibers. Reconstruct
only the frozen compact input prefix, not its old cofactor proof gates.
New exact QQ resultant_Q curves; no Delta or new geometry-head inverse.
180 seconds / 4 GiB. No finite-point or exclusion claim from bivariate gcd.
"""
import json,time,hashlib,signal,resource,contextlib,io,math,zlib,base64
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx
signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
start=time.perf_counter();deadline=start+180
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-start)
 print(json.dumps(kw),flush=True)
dep=Path(__file__).with_name("2026-11-27-unit211-equal-singleton-global-compact-original-three-column-cofactors-8542.py")
raw=dep.read_bytes()
assert hashlib.sha256(raw).hexdigest()=="7bd915c3505e7c7e6bdd1aff7ec85362a29a2771b9f65f4ff5f8b8d067482bd8"
marker=b"\ndef cofactor(names):";assert raw.count(marker)==1
prefix=raw.split(marker)[0]
ns={"__file__":str(dep),"__name__":"__new_Delta_zero_original_projection_input__"}
with contextlib.redirect_stdout(io.StringIO()):
 exec(compile(prefix,str(dep),"exec"),ns)
signal.alarm(max(1,math.ceil(deadline-time.perf_counter())))
ctx,Lp,up,Qp,zeroP,oneP=[ns[x] for x in ["ctx","Lp","up","Qp","zeroP","oneP"]]
Delta,Tnum=ns["Delta"],ns["Tnum"]
strip_paid,audit_den,profile=[ns[x] for x in ["strip_paid","audit_den","profile"]]
Qfree_atoms=[(name,atom) for name,atom in ns["paid_atoms"] if int(atom.degrees()[2])==0]
def primitive_scalar(rr):
 audit_den(rr.d)
 out,removed,history=strip_paid(rr.n)
 assert out
 scale=out.coefficient(0);out=out/scale;removed*=scale
 assert out*removed==rr.n
 return out,history
dpoly,drem=primitive_scalar(Delta)
npoly,nrem=primitive_scalar(Tnum)
head=zeroP
for mm,cc in Delta.n.to_dict().items():
 if int(mm[2])==2:head+=cc*Lp**int(mm[0])*up**int(mm[1])
# The head of the original rational Delta, before any primitive division.
dcoeff=[ns["R"]() for _ in range(3)]
assert all(int(mm[2])<=2 for mm in Delta.n.to_dict())
assert all(int(mm[2])==0 for mm in Delta.d.to_dict())
dcoeff[2]=ns["R"](head,Delta.d)
assert dcoeff[2]==2*(ns["ell"]-1)*(ns["lam"]**2+ns["lam"]-1)
say("new_entire_equal_singleton_Delta_zero_original_projection_input",
 originalNecessaryRows=["Delta=0","Tnum=0"],
 fixedQDegrees=[int(dpoly.degrees()[2]),int(npoly.degrees()[2])],
 primitiveDelta=profile(dpoly),primitiveTnum=profile(npoly),
 onlyPaidOriginalRemovals=[drem,nrem],
 originalQSquaredHead="2*(ell-1)*(lambda^2+lambda-1)",
 headIdentityActuallyReturned=True,allHeadZeroFibersRetained=True,
 noDeltaOrNewHeadInverse=True,claimExcluded=False)
aa,bb,cc=[ns["rows"][x] for x in ["R","W","O"]]
det=(aa[0]*(bb[1]*cc[2]-bb[2]*cc[1])
    +bb[0]*(cc[1]*aa[2]-cc[2]*aa[1])
    +cc[0]*(aa[1]*bb[2]-aa[2]*bb[1]))
core,removed,history=strip_paid(det);core=core/core.coefficient(0)
assert profile(core)["sha256"]=="9403fd667daefd68e6b71b497071959b63590c2ddf28a6e8f2fa703df4615512"
say("new_Delta_zero_frozen_mean_cofactor_input",
 originalRows=["R","W","O"],necessaryCore=profile(core),
 onlyNecessaryPolynomialReconstructed=True,
 previousThreeColumnAdjugateAndCertificateGatesNotReplayed=True)
bctx=fmpq_mpoly_ctx.get(("lam","u"),"lex");bl,bu=bctx.gens()
def to_biv(pp):
 assert all(int(mm[2])==0 for mm in pp.to_dict())
 out=bctx.from_dict({(int(mm[0]),int(mm[1])):cc for mm,cc in pp.to_dict().items()})
 back=ctx.from_dict({(int(mm[0]),int(mm[1]),0):cc for mm,cc in out.to_dict().items()})
 assert back==pp
 return out
def strip_projected(pp):
 original=pp;prod=oneP;history=[]
 for name,atom in Qfree_atoms:
  count=0
  while pp:
   gg=pp.gcd(atom)
   if gg.total_degree()==0:break
   nxt=pp/gg;assert nxt*gg==pp;pp=nxt;prod*=gg;count+=1
  if count:history.append(dict(originalQFreeUnit=name,gcdLoops=count))
 if pp:
  sc=pp.coefficient(0);pp=pp/sc;prod*=sc
 assert prod*pp==original
 return pp,history
def biv_profile(pp):
 data=[[int(mm[0]),int(mm[1]),str(cc)] for mm,cc in sorted(pp.to_dict().items())]
 raw=json.dumps(data,separators=(",",":")).encode()
 out=dict(degrees_lambda_u=list(map(int,pp.degrees())),totalDegree=int(pp.total_degree()),
          terms=len(data),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
 if len(raw)<=20000:
  packed=zlib.compress(raw,9)
  restored=json.loads(zlib.decompress(packed))
  assert bctx.from_dict({(i,j):fmpq(c) for i,j,c in restored})==pp
  out.update(encoding="base64+zlib+json-lambda-u-coeff",data=base64.b64encode(packed).decode())
 return out
projected={}
for name,second in [("original_Delta_Tnum_compatibility",npoly),
                    ("original_Delta_all_means_cofactor",core)]:
 began=time.perf_counter()
 result=dpoly.resultant(second,"Q")
 assert all(int(mm[2])==0 for mm in result.to_dict())
 say("new_entire_Delta_zero_fixed_original_Q_resultant_returned",
     name=name,rawOriginalQQResultant=profile(result),
     fixedOriginalQDegrees=[int(dpoly.degrees()[2]),int(second.degrees()[2])],
     fixedOriginalSylvesterSize=int(dpoly.degrees()[2])+int(second.degrees()[2]),
     allOriginalQLeadingZeroFibersRetained=True,
     projectionSeconds=time.perf_counter()-began,claimExcluded=False)
 if not result:
  say("new_entire_Delta_zero_original_zero_projection_retained",
      name=name,noExclusionClaim=True)
  continue
 pp,hist=strip_projected(result)
 biv=to_biv(pp);projected[name]=biv
 say("new_entire_Delta_zero_original_projected_necessary_curve",
     name=name,necessaryCurve=biv_profile(biv),onlyPaidQFreeRemovals=hist,
     polynomialNotReplacedByMultivariateGcd=True,
     wholeOriginalDeltaZeroChartExcluded=(biv.total_degree()==0))
 # Full QQ factors define the whole curve; no chosen root or generic slice.
 unit,factors=biv.factor();product=bctx.constant(unit);records=[]
 for fac,power in factors:
  product*=fac**power
  records.append(dict(multiplicity=int(power),factor=biv_profile(fac)))
 assert product==biv
 say("new_entire_Delta_zero_complete_projected_QQ_factor_cover",
     name=name,unit=str(unit),factors=records,fullQQProductReturned=True,
     allFactorsAndAllIntersectionsRetained=True,
     noFiniteCandidateOrExclusionClaim=True)
if len(projected)==2:
 first,second=list(projected.values());common=first.gcd(second)
 if common:
  qa=first/common;qb=second/common
  assert qa*common==first and qb*common==second
  say("new_Delta_zero_two_necessary_curve_exact_decomposition",
      sharedCurve=biv_profile(common),firstResidual=biv_profile(qa),secondResidual=biv_profile(qb),
      exactSetCover="sharedCurve=0 OR (firstResidual=0 AND secondResidual=0)",
      multivariateUnitGcdNOTTreatedAsEmptySet=True,
      allZeroDimensionalResidualIntersectionsRetained=True)
signal.alarm(0)
say("new_entire_equal_singleton_Delta_zero_two_original_QQ_projections_complete",
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    noDeltaInverse=True,allQLeadingZeroFibersRetained=True,
    oldCofactorProofGateNotReplayed=True,
    wholeOriginalDeltaZeroExclusionClaim=False,ordinaryISPClaim=False,
    peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
