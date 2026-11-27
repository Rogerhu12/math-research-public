#!/usr/bin/env python3
"""NEW fixed-Q QQ projections of the four saved original collision polynomials.
Read the exact completed same-(f,z) input, with no old mean/cofactor replay.
Factor the true Q heads, retain their entire zero fibers, then compute two
fixed original resultants in Q. Only genuine original Q-free units may be
removed. Full QQ factors and their products are retained; a multivariate
unit gcd is never interpreted as an empty intersection.
180 seconds /4 GiB, two small exact-input fragments, no helper code."""
import json,time,hashlib,signal,resource,base64,zlib
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx
signal.alarm(180);resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
start=time.perf_counter()
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-start);print(json.dumps(kw),flush=True)
spec=[["2026-11-27-unit211-collision-Delta-nonzero-four-original-exact-input-part1-8542.json","c4723da150647c453cd53151b4e9f84e5d6ed1c45dffcf4c39299b9ef968c3e6"],["2026-11-27-unit211-collision-Delta-nonzero-four-original-exact-input-part2-8542.json","8f8a547ba11ffc2baafd0229f9ffce5a16576206d06460d627927b80d4671682"]]
parts=[]
for i,(name,sha) in enumerate(spec):
 raw=Path(__file__).with_name(name).read_bytes();assert hashlib.sha256(raw).hexdigest()==sha
 data=json.loads(raw);assert data["part"]==i+1 and data["total"]==2
 assert data["payloadSHA256"]=="11046373e5362f4b5606e2940483929954a74382e152e40f211fbe79ec42b292"
 parts.append(data["dataChunk"])
raw=zlib.decompress(base64.b64decode("".join(parts)))
assert hashlib.sha256(raw).hexdigest()=="11046373e5362f4b5606e2940483929954a74382e152e40f211fbe79ec42b292"
data=json.loads(raw);assert data["variables"]==["lambda","u","Q"]
ctx=fmpq_mpoly_ctx.get(("lam","u","Q"),"lex");lam,u,Q=ctx.gens()
one,zero=ctx.constant(1),ctx.constant(0)
values={name:ctx.from_dict({tuple(e):fmpq(c) for e,c in records})
        for name,records in data["polynomials"].items()}
A=2*lam**2-2*lam+1;B=4*lam**3-6*lam**2+3*lam-1
atoms=[("lambda",lam),("u",u),("u-1",u-1),("A",A),("B",B),
       ("u-ell",u*B**2-A**3),("S",(2*lam-1)*(2*lam**2-1))]
def profile(p):
 rows=[[list(map(int,e)),str(c)] for e,c in sorted(p.to_dict().items())]
 raw=json.dumps(rows,separators=(",",":")).encode()
 return dict(degrees_lambda_u_Q=list(map(int,p.degrees())),
             totalDegree=int(p.total_degree()),terms=len(rows),
             bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
def saved(p,limit=400000):
 rows=[[list(map(int,e)),str(c)] for e,c in sorted(p.to_dict().items())]
 raw=json.dumps({"variables":["lambda","u","Q"],"terms":rows},separators=(",",":")).encode()
 out=dict(profile=profile(p),payloadBytes=len(raw),payloadSHA256=hashlib.sha256(raw).hexdigest())
 if len(raw)<=limit:
  enc=zlib.compress(raw,9);restored=json.loads(zlib.decompress(enc))
  assert ctx.from_dict({tuple(e):fmpq(c) for e,c in restored["terms"]})==p
  out.update(encoding="base64+zlib+json",data=base64.b64encode(enc).decode(),
             completeCoefficientReconstructionReturned=True)
 return out
def strip(p):
 original=p;prod=one;history=[]
 for label,a in atoms:
  count=0
  while p:
   gg=p.gcd(a)
   if gg.total_degree()==0:break
   q=p/gg;assert q*gg==p;p=q;prod*=gg;count+=1
  if count:history.append(dict(originalQFreeUnit=label,gcdLoops=count))
 if p:
  lc=p.coefficient(0);p=p/lc;prod*=lc
 assert p*prod==original
 return p,history
for label,p in values.items():
 degree=int(p.degrees()[2])
 head=ctx.from_dict({(int(e[0]),int(e[1]),0):c for e,c in p.to_dict().items() if int(e[2])==degree})
 rem,history=strip(head);scalar,fac=rem.factor();prod=ctx.constant(scalar);records=[]
 for f,m in fac:
  prod*=f**m;records.append(dict(multiplicity=int(m),factor=saved(f)))
 assert prod==rem
 say("new_original_Q_head_complete_QQ_factorization",name=label,
     originalQDegree=degree,originalHead=profile(head),
     paidOriginalQFreeRemovals=history,remainingHead=profile(rem),
     fullQQFactorProductReturned=True,unpaidFactors=records,
     headPaidUnit=rem.total_degree()==0,allHeadZeroFibersRetained=True)
projected={}
for label,other in [("RW","W"),("RN1","N1")]:
 first,second=values["R"],values[other];t=time.perf_counter()
 result=first.resultant(second,"Q")
 assert all(int(e[2])==0 for e in result.to_dict())
 say("new_same_original_fixed_Q_resultant_returned",name=label,
     originalQDegrees=[int(first.degrees()[2]),int(second.degrees()[2])],
     fixedSylvesterSize=int(first.degrees()[2])+int(second.degrees()[2]),
     actualFullQQResultant=profile(result),
     allOriginalQLeadingZeroFibersRetained=True,
     resultantSeconds=time.perf_counter()-t)
 if not result:
  say("new_original_zero_projection_retained",name=label,claimExcluded=False);continue
 rem,history=strip(result);projected[label]=rem
 say("new_complete_original_projected_necessary_curve",name=label,
     originalNecessaryCurve=saved(rem),
     onlyPaidOriginalQFreeRemovals=history,claimExcluded=rem.total_degree()==0)
 scalar,fac=rem.factor();prod=ctx.constant(scalar);records=[]
 for f,m in fac:
  prod*=f**m;records.append(dict(multiplicity=int(m),factor=saved(f)))
 assert prod==rem
 say("new_complete_original_projected_QQ_factor_cover",name=label,
     irreducibleQQFactors=records,scalar=str(scalar),
     wholeQQFactorProductReturned=True,allComponentsAndIntersectionsRetained=True)
if len(projected)==2:
 a,b=list(projected.values());g=a.gcd(b);ar=a/g;br=b/g
 assert ar*g==a and br*g==b
 say("new_original_two_projected_curves_exact_decomposition",
     sharedCurve=saved(g),firstResidual=saved(ar),secondResidual=saved(br),
     exactSetCover="sharedCurve=0 OR (firstResidual=0 AND secondResidual=0)",
     residualCurvesHaveNoCommonIrreducibleComponent=True,
     residualDifferentBasePointBezoutBound=int(ar.total_degree())*int(br.total_degree()),
     unitMultivariateGcdNotCalledEmpty=True)
say("new_remaining_collision_two_QQ_original_projections_finished",
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    originalInputReplayed=False,allOriginalHeadsRetained=True,
    allNewParameterCurvesAndFiniteIntersectionsRetained=True,
    individualNBPBStillRequired=True,ordinaryISPClaim=False,
    peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)
