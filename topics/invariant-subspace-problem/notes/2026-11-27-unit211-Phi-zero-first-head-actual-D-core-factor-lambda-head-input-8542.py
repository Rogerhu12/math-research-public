#!/usr/bin/env python3
"""NEW factor and lambda-head input from the saved actual D necessary core.
No original means, commutators, cofactor, or D-return is recomputed.
Read and SHA-check the exact 3101-term polynomial, factor its true
lambda-leading coefficient, and then factor the whole QQ core.
All factor products and exact original-unit divisions are multiplied
back. Preserve every new leading-zero weight curve; no unverified
factor is a unit. 120 seconds /1 GiB, one exact JSON dependency.
"""
import json,time,hashlib,base64,zlib,signal,resource
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx
signal.alarm(120);resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
began=time.perf_counter()
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-began)
 print(json.dumps(kw),flush=True)
name="2026-11-27-unit211-Phi-zero-first-quadratic-head-actual-D-core-exact-input-8542.json"
raw=Path(__file__).with_name(name).read_bytes()
assert hashlib.sha256(raw).hexdigest()=="7cc9dcf4c8f716055518324966cf8c156c961c5204dfb156ede054f63568765b"
data=json.loads(raw);record=data["polynomial"]
unpacked=zlib.decompress(base64.b64decode(record["data"]))
assert hashlib.sha256(unpacked).hexdigest()=="9e50cc2a30cf8500b7bef25f8e579334c2b46f8d896662759cdc0ec85f35542c"
obj=json.loads(unpacked);assert obj["variables"]==["u","Q","lambda"]
ctx=fmpq_mpoly_ctx.get(("u","Q","lam"),"lex");u,Q,lam=ctx.gens()
p=ctx.from_dict({tuple(e):fmpq(c) for e,c in obj["terms"]})
assert list(map(int,p.degrees()))==[39,20,6] and len(p.to_dict())==3101
padded=sorted((tuple(e)+(0,0),c) for e,c in p.to_dict().items())
assert hashlib.sha256(str(padded).encode()).hexdigest()=="d12d36de38995832f521156d012ce93b6160dc7b1d870903923051ac5da0bf15"
def info(pp):
 return dict(degrees=list(map(int,pp.degrees())),terms=len(pp.to_dict()),
             sha256=hashlib.sha256(str(sorted(pp.to_dict().items())).encode()).hexdigest())
def saved(pp):
 bb=json.dumps({"variables":["u","Q","lambda"],
                "terms":[[list(map(int,e)),str(c)] for e,c in sorted(pp.to_dict().items())]},
               separators=(",",":")).encode()
 back=json.loads(zlib.decompress(zlib.compress(bb,9)))
 assert ctx.from_dict({tuple(e):fmpq(c) for e,c in back["terms"]})==pp
 return dict(profile=info(pp),encoding="base64+zlib+json",
             payloadSha256=hashlib.sha256(bb).hexdigest(),
             data=base64.b64encode(zlib.compress(bb,9)).decode())
LC=ctx.from_dict({(int(e[0]),int(e[1]),0):c for e,c in p.to_dict().items() if int(e[2])==6})
assert LC
elln=Q-2*(u-1)*(u-2);mn=u*Q-elln
Mnum=elln*(2*u-elln)-u*u*Q
atoms=[("u",u),("u-1",u-1),("Q",Q),("1-Q",1-Q),
       ("ell numerator",elln),("u-ell numerator",mn),("M numerator",Mnum),
       ("-T0",Q+4*(u-1)),("u+Q-1",u+Q-1)]
remaining=LC;removals=[]
for label,a in atoms:
 while True:
  gg=remaining.gcd(a)
  if gg.total_degree()==0:break
  q=remaining/gg;assert q*gg==remaining
  remaining=q;removals.append([label,info(gg)])
scalar,factors=remaining.factor()
prod=ctx.constant(scalar);factor_records=[]
for fac,e in factors:
 prod=prod*fac**e
 factor_records.append(dict(multiplicity=int(e),polynomial=str(fac),exact=saved(fac)))
assert prod==remaining
say("new_complete_true_lambda_six_leading_coefficient",
    actualOriginalLC=saved(LC),paidUnitDivisions=removals,
    remainingLC=saved(remaining),irreducibleQQWeightFactors=factor_records,
    exactWholeFactorProductReturned=True,
    onlyOnFirstOriginalQuadraticHeadChart=True,
    allNewLambdaLeadingZeroWeightCurvesRetained=True,
    wholeLambdaHeadPaidUnit=remaining.total_degree()==0,
    noOriginalDAGRecomputed=True)
say("new_whole_saved_D_core_factorization_started",originalCore=info(p))
scalar,factors=p.factor()
prod=ctx.constant(scalar);out=[]
for fac,e in factors:
 prod=prod*fac**e
 out.append(dict(multiplicity=int(e),exact=saved(fac)))
assert prod==p
say("complete_new_saved_actual_D_core_QQ_factorization",
    irreducibleQQFactors=out,exactWholeOriginalCoreFactorProductReturned=True,
    firstOriginalHeadZeroCurveRetained=True,
    newLambdaLeadingZeroWeightCurvesRetained=True,
    noNewFactorDeclaredUnit=True,wholePhiFaceExcluded=False,ordinaryISPClaim=False)
