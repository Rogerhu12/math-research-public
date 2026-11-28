#!/usr/bin/env python3
"""NEW corrected h=k Delta=0: fixed 17 by 17 u-Sylvester lambda cover.
Only the necessary Mtrue definition prefix is rebuilt and hash-checked.
The independent old P is read from pinned git history in runner memory.
No old P/M gcd, 722-point proof gate, false M, or frozen z target is run.
All u leading-zero fibers remain. Strip only paid lambda-only support.
180 seconds /4 GiB; QQ factor product and every Bareiss division return.
"""
import base64,contextlib,hashlib,io,json,math,resource,signal,time,zlib
from fractions import Fraction
from functools import reduce
from pathlib import Path
from flint import fmpq,fmpq_poly
START=time.perf_counter();DEADLINE=START+180
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
raw_timer=signal.setitimer;raw_alarm=signal.alarm
raw_timer(signal.ITIMER_REAL,180)
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,separators=(',',':')),flush=True)
def bounded_timer(which,seconds,interval=0.0):
 if which!=signal.ITIMER_REAL:return raw_timer(which,seconds,interval)
 assert not interval
 remaining=max(.001,DEADLINE-time.perf_counter())
 return raw_timer(which,min(remaining,float(seconds) if seconds>0 else remaining),0.0)
def bounded_alarm(seconds):
 return math.ceil(bounded_timer(signal.ITIMER_REAL,seconds)[0])
def tick():
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute 180 second boundary')
dep=Path(__file__).with_name('2026-11-28-unit211-h-equals-k-corrected-Delta-zero-RWO-Q-projection-8542.py')
full=dep.read_bytes()
assert hashlib.sha256(full).hexdigest()=='3fcc2e90677b7bbd0247d72c1922fc6ed0b60da4ced715a7cecbeae656aade33'
marker=b'\n # Reuse only the independent, already executed D/T curve P.'
assert full.count(marker)==1
prefix=full.split(marker)[0]
assert len(prefix)==6055 and hashlib.sha256(prefix).hexdigest()=='09e0b44a9b6f244d0e2a11c1361b5382219aa5cad609efc3ae08fd370d318c7b'
ns={'__name__':'new_fixed_u17_only_Mtrue_input_definition','__file__':str(dep)}
signal.alarm=bounded_alarm;signal.setitimer=bounded_timer
try:
 with contextlib.redirect_stdout(io.StringIO()):
  exec(compile(prefix,str(dep)+'#only_Mtrue_input_definition','exec'),ns)
finally:
 signal.alarm=raw_alarm;signal.setitimer=raw_timer
 raw_timer(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
assert 'newM' in ns and ns['newM']
mdata=[[int(mm[0]),int(mm[1]),str(c)] for mm,c in sorted(ns['newM'].to_dict().items())]
assert all(int(mm[2])==0 for mm in ns['newM'].to_dict())
mraw=json.dumps(mdata,separators=(',',':')).encode()
assert hashlib.sha256(mraw).hexdigest()=='65d420e901bd60b711d76ad23699daab655414b0595383a19a93d13180f30663'
assert list(map(int,ns['newM'].degrees()))==[110,14,0]
# The old independent curve is a pinned historical INPUT only.
legacy=Path(__file__).with_name('isp-hk-independent-Delta-Tnum-legacy.json')
doc=json.loads(legacy.read_text())
def walk(obj):
 if isinstance(obj,dict):
  yield obj
  for v in obj.values():yield from walk(v)
 elif isinstance(obj,list):
  for v in obj:yield from walk(v)
matches=[r for r in walk(doc)
 if r.get('sha256')=='8af7c105334af350ef5047ee49cf27a5aadbfa204a11b64f9b7f7b8a352dd49c'
 and r.get('encoding')=='base64+zlib+json-lambda-u-coeff' and 'data' in r]
assert len(matches)>=1
pdata=json.loads(zlib.decompress(base64.b64decode(matches[0]['data'])))
praw=json.dumps(pdata,separators=(',',':')).encode()
assert hashlib.sha256(praw).hexdigest()=='8af7c105334af350ef5047ee49cf27a5aadbfa204a11b64f9b7f7b8a352dd49c'
def degrees(data):return [max(int(r[j]) for r in data) for j in range(2)]
assert degrees(pdata)==[28,3] and degrees(mdata)==[110,14]
say('new_fixed_u17_original_inputs_ready',
 independentP={'degrees':[28,3],'sha256':hashlib.sha256(praw).hexdigest()},
 correctedM={'degrees':[110,14],'sha256':hashlib.sha256(mraw).hexdigest()},
 necessaryPrefixBytes=6055,
 necessaryPrefixSHA256=hashlib.sha256(prefix).hexdigest(),
 oldPAndMQQGCDNotExecuted=True,old722PointGateNotExecuted=True,
 oldDTProjectionNotExecuted=True,wrongMNeverDecoded=True,
 inputDefinitionRegenerationNotANewConclusion=True,
 allFixedULeadingZeroFibersKept=True)
del doc,matches,praw,mraw
stats={'inputRationalScalingCoefficients':0,'exactDivisionProducts':0,
       'bareissDivisionProducts':0,'bareissRowSwaps':0,'paidSupportProducts':0,
       'factorProductReturns':0}
P0=fmpq_poly([]);P1=fmpq_poly([1])
def coeff_profile(poly):
 data=[str(poly[i]) for i in range(int(poly.degree())+1)] if poly else []
 raw=json.dumps(data,separators=(',',':')).encode()
 return dict(degree=int(poly.degree()) if poly else -1,
             nonzeroCoefficients=sum(bool(poly[i]) for i in range(len(data))),
             bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
def exact(a,b):
 tick();assert b
 q,r=divmod(a,b);assert not r and q*b==a
 stats['exactDivisionProducts']+=1
 return q
def primitive_integer_u_coefficients(data,du,dl):
 assert len({(int(i),int(j)) for i,j,_ in data})==len(data)
 rational={(int(i),int(j)):Fraction(str(c)) for i,j,c in data}
 assert all(0<=i<=dl and 0<=j<=du for i,j in rational)
 den=1
 for v in rational.values():den=math.lcm(den,v.denominator)
 integers={m:v.numerator*(den//v.denominator) for m,v in rational.items()}
 content=reduce(math.gcd,(abs(v) for v in integers.values()))
 assert content>0
 scale=fmpq(den,content)
 ints={m:v//content for m,v in integers.items()}
 for (i,j),z in ints.items():
  assert fmpq(z)==scale*fmpq(str(rational[(i,j)]))
  stats['inputRationalScalingCoefficients']+=1
 rows=[]
 for j in range(du+1):
  rows.append(fmpq_poly([ints.get((i,j),0) for i in range(dl+1)]))
 assert rows[-1]
 # Constant rational scaling never loses a finite geometric fiber.
 return rows,scale
pc,pscale=primitive_integer_u_coefficients(pdata,3,28)
mc,mscale=primitive_integer_u_coefficients(mdata,14,110)
N=17
matrix=[]
for shift in range(14):
 row=[P0]*N
 for j,p in enumerate(pc):row[shift+j]=p
 matrix.append(row)
for shift in range(3):
 row=[P0]*N
 for j,p in enumerate(mc):row[shift+j]=p
 matrix.append(row)
assert len(matrix)==N and all(len(r)==N for r in matrix)
# Ascending-u evaluation columns (1,u,...,u^16) annihilate this fixed
# matrix at every common finite root, including all leading-zero fibers.
say('new_fixed_u17_sylvester_defined',
 matrixShape=[17,17],originalUDegrees=[3,14],
 originalLambdaDegrees=[28,110],lambdaDegreeUpperBound=722,
 nonzeroRationalInputScalingsReturned=True,
 noULeadingCoefficientInverted=True,
 completeFixedCommonFiniteRootNecessary=True)
def bareiss_det(a):
 a=[r[:] for r in a];previous=P1;sign=1
 for k in range(N-1):
  tick()
  pivotrow=next((i for i in range(k,N) if a[i][k]),None)
  if pivotrow is None:return P0
  if pivotrow!=k:
   a[k],a[pivotrow]=a[pivotrow],a[k]
   sign=-sign;stats['bareissRowSwaps']+=1
  pivot=a[k][k]
  for i in range(k+1,N):
   for j in range(k+1,N):
    numerator=pivot*a[i][j]-a[i][k]*a[k][j]
    a[i][j]=exact(numerator,previous)
    stats['bareissDivisionProducts']+=1
   a[i][k]=P0
  previous=pivot
  say('new_fixed_u17_bareiss_complete_step',step=k,
      pivotDegree=int(pivot.degree()),divisionProducts=stats['bareissDivisionProducts'],
      allActualDivisionProductsReturned=True,
      intermediatePivotZeroFibersKeptByPolynomialIdentity=True)
 return sign*a[-1][-1]
raw=bareiss_det(matrix)
say('new_fixed_u17_original_lambda_resultant',
 raw=coeff_profile(raw),fixedSylvesterSize=17,
 nonzero=bool(raw),allLeadingZeroFibersRetained=True,
 onlyOriginalConstantScalingsUsed=True)
if not raw:
 say('new_fixed_u17_zero_resultant_retained',
     noNewLambdaFiniteCoverOrExclusion=True,
     statistics=stats,ordinaryISPClaim=False)
else:
 assert int(raw.degree())<=722
 lp=fmpq_poly([0,1]);A=fmpq_poly([1,-2,2]);B=fmpq_poly([-1,3,-6,4])
 half=fmpq_poly([-1,2]);Sn=fmpq_poly([1,-2,-2,4])
 assert Sn==half*fmpq_poly([-1,0,2])
 atoms=[('A',A),('B',B),('physical_lambda',lp),
        ('independent_physical_two_lambda_minus_one',half),
        ('entire_original_S_numerator',Sn)]
 rest=raw;removed=P1;history=[]
 for name,atom in atoms:
  count=0
  while True:
   g=rest.gcd(atom)
   if int(g.degree())==0:break
   rest=exact(rest,g);removed*=g;count+=1
   assert rest*removed==raw
   stats['paidSupportProducts']+=1
  if count:history.append({'originalPaidLambdaSupport':name,'gcdLayers':count})
 lead=rest[int(rest.degree())]
 assert lead
 rest=rest/lead;removed*=lead
 assert rest*removed==raw
 say('new_fixed_u17_complete_necessary_lambda_cover',
     rawDegree=int(raw.degree()),remaining=coeff_profile(rest),
     onlyAlreadyPaidLambdaSupportRemoved=history,
     allUnpaidLambdaFactorsAndMultiplicitiesKept=True,
     allOriginalUQGramFibersStillNeedTheirOriginalReturns=True,
     wholeNamedPfDeltaChartExcluded=int(rest.degree())==0,
     PfZeroChartUnchanged=True)
 unit,fac=rest.factor()
 factored=[]
 for f,multiplicity in fac:
  factored.append((f,int(multiplicity)))
 factored.sort(key=lambda fm:(int(fm[0].degree()),[str(fm[0][j]) for j in range(int(fm[0].degree())+1)]))
 back=fmpq_poly([unit]);sf=P1;records=[]
 for index,(f,multiplicity) in enumerate(factored):
  assert multiplicity>=1 and int(f.degree())>=1
  back*=f**multiplicity;sf*=f
  rec=dict(index=index,multiplicity=multiplicity,
           irreducibleFactor=coeff_profile(f))
  records.append(rec)
 assert back==rest
 stats['factorProductReturns']+=1
 normalizedSF=sf/sf[int(sf.degree())]
 say('new_fixed_u17_entire_QQ_factor_cover',
     factors=records,entireQQFactorProductReturned=True,
     remainingDegree=int(rest.degree()),squareFreeNecessary=coeff_profile(normalizedSF),
     allIrreducibleQQFactorsRetained=True,
     lambdaCandidateValuesAtMost=int(normalizedSF.degree()),
     allUSpecializationsAndQLeadingZerosRetained=True,
     noModularEmptyOrNumericRootInference=True,
     wholeNamedPfDeltaChartExcluded=int(rest.degree())==0,
     noClaimEntireCollisionExcluded=True)
say('new_fixed_u17_lambda_cover_first_run_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 statistics=stats,
 necessaryMDefinitionOnlyRegenerated=True,
 oldPAndMQQGCDAnd722GateNotExecuted=True,
 noOldWrongProjectionRestored=True,
 noFrozenZTargetExecuted=True,
 noCoefficientCachePayloadOrChunksSaved=True,
 ordinaryISPClaim=False,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
raw_timer(signal.ITIMER_REAL,0)
