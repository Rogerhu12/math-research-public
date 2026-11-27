#!/usr/bin/env python3
"""NEW fixed u-resultant of the two saved remaining collision curves.
The entire P3, J2, G2 and C4 original fibres are already excluded.
No previous Q projection, original four-row construction, or finite
Q-head gate is repeated. All actual u-head drops stay in the fixed
18/19 Sylvester polynomial. Return the complete squarefree lambda
cover, only after exact QQ result and original paid-factor divisions.
180 seconds /4 GiB. Exact final parameter chunks only, no big matrix."""
import json,time,hashlib,zlib,base64,signal,resource,math
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpq_mpoly_ctx
started=time.perf_counter()
signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(stage,**v):
 v.update(stage=stage,seconds=time.perf_counter()-started)
 print(json.dumps(v,separators=(',',':')),flush=True)
def read(name,sha):
 raw=Path(__file__).with_name(name).read_bytes()
 assert hashlib.sha256(raw).hexdigest()==sha
 return json.loads(raw)
def coeffs(p):return [str(c) for c in p.coeffs()]
def pprofile(p):
 raw=json.dumps(coeffs(p),separators=(',',':')).encode()
 return dict(degree=int(p.degree()),bytes=len(raw),
             sha256=hashlib.sha256(raw).hexdigest())
def checkpoint(label,obj):
 raw=json.dumps(obj,separators=(',',':')).encode()
 enc=base64.b64encode(zlib.compress(raw,9)).decode()
 assert zlib.decompress(base64.b64decode(enc))==raw
 chunks=[enc[j:j+75000] for j in range(0,len(enc),75000)]
 say('new_collision_E_lambda_exact_input',label=label,
     bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),
     base64Characters=len(enc),chunks=len(chunks),
     encoding='base64+zlib+json',maximumChunkCharacters=75000)
 for j,ch in enumerate(chunks):
  say('new_collision_E_lambda_exact_input_chunk',
      label=label,index=j,total=len(chunks),data=ch)
ctx=fmpq_mpoly_ctx.get(('lambda','u'),'lex')
manifest=read('2026-11-28-unit211-collision-two-QQ-projections-exact-factor-manifest-8542.json',
 '4a2206f910408ec2ef7bc0a7cc49b24cefe556a226d5bfe66f4c0059d45abb54')
polys=[];scales=[]
for name,expected in [('E177-18',[177,18]),('E182-19',[182,19])]:
 item=next(x for x in manifest['factors'] if x['name']==name)
 chunks=[read(p['filename'],p['sha256'])['dataChunk'] for p in item['parts']]
 enc=''.join(chunks)
 assert hashlib.sha256(enc.encode()).hexdigest()==item['encodedDataSHA256']
 raw=zlib.decompress(base64.b64decode(enc))
 assert len(raw)==item['payloadBytes']
 assert hashlib.sha256(raw).hexdigest()==item['payloadSHA256']
 obj=json.loads(raw);assert obj['variables']==['lambda','u','Q']
 dd={}
 for (a,b,q),c in obj['terms']:
  assert q==0 and (a,b) not in dd
  dd[(a,b)]=fmpq(c)
 original=ctx.from_dict(dd)
 assert list(map(int,original.degrees()))==expected
 den=1
 for c in dd.values():den=math.lcm(den,int(c.denominator))
 ints={e:int(c*den) for e,c in dd.items()}
 content=0
 for c in ints.values():content=math.gcd(content,abs(c))
 assert content
 integer=ctx.from_dict({e:c//content for e,c in ints.items()})
 assert integer*fmpq(content,den)==original
 polys.append(integer);scales.append(dict(name=name,denominator=den,content=content))
 say('new_collision_E_original_saved_curve_loaded',
     name=name,degrees=expected,terms=len(dd),
     originalPayloadSHA256=item['payloadSHA256'],
     completePrimitiveIntegerInputProductReturned=True,
     noPriorProjectionReconstruction=True)
assert int(polys[0].degrees()[1])==18 and int(polys[1].degrees()[1])==19
say('new_collision_E_fixed_u_QQ_resultant_started',
    originalUDegrees=[18,19],fixedOriginalSylvesterOrder=37,
    primitiveIntegerInputScales=scales,
    allUHeadZeroLambdaFibersRetained=True,
    resourceBudgetSeconds=180,resourceBudgetBytes=4*1024**3)
res=polys[0].resultant(polys[1],'u')
if not res:
 say('accurate_new_collision_E_u_resultant_identically_zero',
     noFiniteLambdaCoverReturned=True,previousFiniteFiveCoordinateBoundRetained=True,
     noAdditionalGateOrLargerBudgetAttempted=True,
     wholeCollisionExcluded=False,ordinaryISPClaim=False)
 signal.alarm(0);raise SystemExit(0)
assert all(int(ex[1])==0 for ex in res.to_dict())
rp=fmpq_poly([0]*(int(res.degrees()[0])+1))
for ex,c in res.to_dict().items():rp[int(ex[0])]=c
assert ctx.from_dict({(i,0):c for i,c in enumerate(rp.coeffs()) if c})==res
say('new_collision_E_fixed_u_original_QQ_resultant_completed',
    exactResultant=pprofile(rp),fixedOriginalSylvesterOrder=37,
    allActualUHeadDropsRemainInNecessaryCover=True)
x=fmpq_poly([0,1])
units=[
 ('original lambda',x),
 ('original A',2*x*x-2*x+1),
 ('original B',4*x**3-6*x*x+3*x-1),
 ('original S first factor',2*x-1),
 ('original S second factor',2*x*x-1),
 ('complete original J2 fibre excluded',3*x*x-2*x+1),
 ('complete original G2 fibre excluded',x*x+x-1),
 ('complete original C4 fibre excluded',8*x**4-24*x**3+24*x*x-12*x+3)]
remaining=rp;removed=[];product=fmpq_poly([1])
for label,unit in units:
 exponent=0
 while True:
  quotient,remainder=divmod(remaining,unit)
  if remainder:break
  assert quotient*unit==remaining
  remaining=quotient;product*=unit;exponent+=1
 if exponent:
  removed.append(dict(originalPaidUnit=label,coefficientsAscending=coeffs(unit),power=exponent))
  say('new_collision_E_actual_paid_lambda_factor_removed',
      originalPaidUnit=label,power=exponent,remainingDegree=int(remaining.degree()),
      allActualDivisionProductsReturned=True)
assert product*remaining==rp
remaining=remaining/remaining[remaining.degree()]
common=remaining.gcd(remaining.derivative())
sf,remainder=divmod(remaining,common)
assert not remainder and sf*common==remaining and sf
sf=sf/sf[sf.degree()]
assert sf.gcd(sf.derivative()).degree()==0
say('new_collision_E_complete_squarefree_lambda_cover',
    exactSquarefreeMonicLambdaCover=pprofile(sf),
    onlyAlreadyExcludedOriginalLambdaFibersRemoved=removed,
    allOriginalUAndQHeadZeroFibersRetained=True,
    currentCollisionOriginalPointsHaveLambdaInThisCover=True,
    noDifferentUOrQRootsCombined=True,
    countsLambdaOnlyNotAllRemainingValues=True,
    wholeCollisionExcluded=(sf.degree()==0),
    ordinaryISPClaim=False)
checkpoint('new_complete_original_E_intersection_lambda_cover',
 dict(variable='lambda',coefficientsAscending=coeffs(sf),
      fixedOriginalEliminationVariable='u',fixedOriginalDegrees=[18,19],
      originalCurvePayloadSHA256s=[
       '65736a226b106d5b25240130131e37956abfe918aa3a0264159027a135b9494a',
       '182f94064ead0432161fff015836b38de3f1e958491d3158867dfee918bd952c'],
      sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      onlyPaidLambdaFactorsRemoved=removed,
      originalFiniteFiveCoordinateUpperBound=235170,
      allRemainingOriginalValueFibersRetained=True))
say('new_collision_E_fixed_u_projection_attempt_finished',
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    completeNewQQCoverReturned=True,
    noPreviousQProjectionOrCompletedFibreGateReplayed=True,
    wholeCollisionExcluded=(sf.degree()==0),ordinaryISPClaim=False)
signal.alarm(0)
