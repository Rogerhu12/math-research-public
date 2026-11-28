#!/usr/bin/env python3
"""NEW independent Delta/Tnum P: cubic-u discriminant, no previous gate.
Only the exact 2496-byte existing P parameter is read in runner scratch.
No M, F99 reconstruction, joint u gcd, Q projection, or original z gate.
Absolute 60 seconds / 1 GiB. Output only profiles and exact return flags.
"""
import base64,hashlib,json,resource,signal,time,zlib
from pathlib import Path
from flint import fmpq,fmpq_poly
START=time.perf_counter()
signal.alarm(60)
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,separators=(',',':')),flush=True)
def walk(x):
 if isinstance(x,dict):
  yield x
  for y in x.values():yield from walk(y)
 elif isinstance(x,list):
  for y in x:yield from walk(y)
def profile(p):
 data=[str(p[i]) for i in range(int(p.degree())+1)] if p else []
 raw=json.dumps(data,separators=(',',':')).encode()
 return dict(degree=int(p.degree()) if p else -1,terms=sum(bool(p[i]) for i in range(int(p.degree())+1)),
             bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
EXPECTED='8af7c105334af350ef5047ee49cf27a5aadbfa204a11b64f9b7f7b8a352dd49c'
path=Path(__file__).with_name('isp-hk-independent-Delta-Tnum-legacy.json')
doc=json.loads(path.read_text())
found=[r for r in walk(doc) if r.get('sha256')==EXPECTED
 and r.get('encoding')=='base64+zlib+json-lambda-u-coeff' and 'data' in r]
assert found
payload=zlib.decompress(base64.b64decode(found[0]['data']))
pdata=json.loads(payload)
canonical=json.dumps(pdata,separators=(',',':')).encode()
assert len(canonical)==2496 and hashlib.sha256(canonical).hexdigest()==EXPECTED
assert len(pdata)==115
table={(int(i),int(j)):fmpq(c) for i,j,c in pdata}
assert len(table)==115 and max(i for i,j in table)==28 and max(j for i,j in table)==3
assert all(i>=0 and 0<=j<=3 for i,j in table)
coeff=[fmpq_poly([table.get((i,j),fmpq(0)) for i in range(29)]) for j in range(4)]
back=[[i,j,str(coeff[j][i])] for i in range(29) for j in range(4) if coeff[j][i]]
assert back==pdata
del doc,found,payload,canonical,table,pdata
d,c,b,a=coeff
assert a
say('new_independent_P_cubic_u_coefficient_definition',
 originalP_SHA256=EXPECTED,originalPBytes=2496,
 coefficientOrder=['one','u','u^2','u^3'],coefficients=[profile(x) for x in coeff],
 completeCoefficientReassemblyReturned=True,
 noOldProjectionOrFactorGateExecuted=True)
disc=18*a*b*c*d-4*b**3*d+b*b*c*c-4*a*c**3-27*a*a*d*d
say('new_independent_P_exact_cubic_u_discriminant',
 definition='18abcd-4b^3d+b^2c^2-4ac^3-27a^2d^2',
 inputCoefficientOrder='a*u^3+b*u^2+c*u+d',
 discriminant=profile(disc),discriminantNonzero=bool(disc),
 spectralF99AndF300NotReconstructed=True,
 noJointUOrQGcdExecuted=True)
if disc:
 unit,factors=disc.factor()
 product=fmpq_poly([unit]);records=[]
 for fac,power in factors:
  assert int(power)>0 and int(fac.degree())>0
  product*=fac**int(power)
  records.append(dict(multiplicity=int(power),factor=profile(fac)))
 assert product==disc
 degrees=[int(fac.degree()) for fac,power in factors]
 small=all(n<99 for n in degrees)
 say('new_independent_P_discriminant_complete_QQ_factorization',
 constant=str(unit),factors=records,fullExactProductReturned=True,
 allIrreducibleFactorDegreesBelow99=small,
 nonvanishingOnBothExistingIrreducibleSpectralFieldsProvedByDegree=small,
 noChosenComplexRootOrFinitePrimeUsed=True,
 fullOriginalGeometryNotExecuted=True,wholeCollisionExcluded=False)
signal.alarm(0)
say('new_independent_P_discriminant_input_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 noCoefficientPayloadOrCacheSaved=True,ordinaryISPClaim=False)
