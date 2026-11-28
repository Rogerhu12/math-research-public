#!/usr/bin/env python3
"""NEW corrected h=k Delta=0: one true RWO Q-projection.
The formerly published second curve used Rbad and remains withdrawn.
Only 5121 bytes of corrected R/W/O definitions are used here, followed
by the definition of the already proved true F61. No old cofactor gate,
D/T projection, frozen low-z gate or old incorrect M is rerun.
An independent OLD D/T curve is read only from pinned git history into
runner memory, never printed or re-saved, for the NEW exact curve gcd.
180 seconds / 4 GiB; all unknown leading-zero fibers retained.
"""
import base64,contextlib,hashlib,io,json,math,resource,signal,time,zlib
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx
START=time.perf_counter();DEADLINE=START+180
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
raw_alarm=signal.alarm;raw_timer=signal.setitimer
raw_timer(signal.ITIMER_REAL,180)
def bounded_alarm(seconds):
 return math.ceil(raw_timer(signal.ITIMER_REAL,max(.001,min(float(seconds) if seconds>0 else 180,DEADLINE-time.perf_counter())))[0])
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,separators=(',',':')),flush=True)
dep=Path(__file__).with_name('2026-11-28-unit211-h-equals-k-corrected-dual-germ-five-original-rows-three-cofactors-8542.py')
full=dep.read_bytes()
assert hashlib.sha256(full).hexdigest()=='2ea618c508489fedffdec7418cc153f6fc213ef46b329f8c55743be312d9faa2'
marker=b'\nalpha=ell*(1-u)-m';assert full.count(marker)==1
prefix=full.split(marker)[0]
assert len(prefix)==5121 and hashlib.sha256(prefix).hexdigest()=='325c32cb81f37b3f31affd4e98f01c39fcee75b2cc0eae1d9cbb079edaf6d078'
ns={'__name__':'new_corrected_Delta_only_RWO_definitions','__file__':str(dep)}
signal.alarm=bounded_alarm
try:
 with contextlib.redirect_stdout(io.StringIO()):
  exec(compile(prefix,str(dep)+'#necessary_RWO_definitions_only','exec'),ns)
finally:
 signal.alarm=raw_alarm;raw_timer(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
ctx,Lp,up,Qp,zeroP,oneP,R,U=[ns[k] for k in ['ctx','Lp','up','Qp','zeroP','oneP','R','U']]
A,B,lam,u,Q,disc,Pf,bc,S,Delta=[ns[k] for k in ['A','B','lam','u','Q','disc','Pf','bc','S','Delta']]
base_atoms=[('A',A.n),('B',B.n),('Q',Q.n),('1-Q',disc.n),('Pf',Pf.n)]
qfree_atoms=[('A',A.n),('B',B.n),('lambda',lam.n),('u',u.n),
             ('symmetric_u_minus_one',(u-1).n),('entire_original_S',S.n)]
divisions=0
def ex(a,b):
 global divisions
 q,r=divmod(a,b);assert not r and q*b==a
 divisions+=1;return q
def strip(p,atoms):
 before=p;removed=oneP;history=[]
 if not p:return p,removed,history
 for name,atom in atoms:
  n=0
  while True:
   g=p.gcd(atom)
   if int(g.total_degree())==0:break
   p=ex(p,g);removed*=g;n+=1
  if n:history.append([name,n])
 assert p*removed==before
 return p,removed,history
def profile(p):
 data=[[list(map(int,m)),str(c)] for m,c in sorted(p.to_dict().items())]
 raw=json.dumps(data,separators=(',',':')).encode()
 return dict(degrees=list(map(int,p.degrees())) if p else [-1]*3,
             totalDegree=int(p.total_degree()) if p else -1,
             terms=len(data),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
def normalized(p):
 assert p
 return p/p.coefficient(0)
def base_den(p):
 rem,_,_=strip(p,base_atoms);assert rem and int(rem.total_degree())==0
def define_row(value):
 den=oneP
 for c in value.c:
  base_den(c.d);den=ex(den,den.gcd(c.d))*c.d
 base_den(den)
 nums=[c.n*ex(den,c.d) for c in value.c]
 nums+=[zeroP]*(3-len(nums));assert len(nums)==3
 common=next(p for p in nums if p)
 for p in nums:common=common.gcd(p)
 _,removed,_=strip(common,base_atoms)
 row=[ex(p,removed) for p in nums]
 scalar=next(p for p in row if p).coefficient(0)
 row=[p/scalar for p in row];removed*=scalar
 # Only necessary input definition, not the old five-row certificate gate.
 assert U([R(p*removed,den) for p in row])==value
 return row
aa,bb,cc=[define_row(ns[k]) for k in ['compact_R','compact_W','compact_O']]
cof=[bb[1]*cc[2]-bb[2]*cc[1],
     cc[1]*aa[2]-cc[2]*aa[1],
     aa[1]*bb[2]-aa[2]*bb[1]]
det=sum((v*r[0] for v,r in zip(cof,[aa,bb,cc])),zeroP)
core,_,_=strip(det,base_atoms);core=normalized(core)
Z=B.n**4*up**2-2*A.n**3*B.n**2*up+A.n**6*Qp
F=ex(core*56668397794435742564352,(2*Lp-1)**2*Z**3)
assert profile(F)['sha256']=='69babd37fc45ade649b12b4b849151574080a2bf92c7c2266141d17be1a9d999'
base_den(Delta.d)
dpoly,_,dpaid=strip(Delta.n,base_atoms);dpoly=normalized(dpoly)
assert int(dpoly.degrees()[2])==2 and int(F.degrees()[2])==9
say('new_true_Delta_zero_RWO_projection_definitions',
    originalTrueF61=profile(F),actualDelta=profile(dpoly),
    necessaryPrefixBytes=len(prefix),necessaryPrefixSHA256=hashlib.sha256(prefix).hexdigest(),
    oldFiveRowCofactorGateNotExecuted=True,oldDeltaTnumProjectionNotExecuted=True,
    wrongRbadAndWrongSecondCurveNotUsed=True,
    physicalScope='h=k, Delta=0, A*B*Q*(1-Q)*Pf*bc*P02 != 0',
    noDeltaInverse=True,allQLeadingZeroFibersKept=True)
# The exact FLINT resultant is the fixed-degree 2+9 Sylvester
# determinant. Its finite-common-root necessity includes head zeros.
raw=dpoly.resultant(F,'Q')
assert all(int(m[2])==0 for m in raw.to_dict())
say('new_corrected_Delta_RWO_fixed_Q_resultant',
    fixedOriginalQDegrees=[2,9],fixedSylvesterSize=11,
    raw=profile(raw),allLeadingZeroFibersRetained=True,
    noNewGeometryHeadInverted=True,ordinaryISPClaim=False)
if not raw:
 say('new_corrected_Delta_RWO_zero_resultant_retained',
     noFiniteBaseOrExclusionClaim=True)
else:
 for name,atom in qfree_atoms:assert all(int(m[2])==0 for m in atom.to_dict())
 newM,removed,hist=strip(raw,qfree_atoms)
 sc=newM.coefficient(0);newM/=sc;removed*=sc
 assert newM*removed==raw
 say('new_corrected_Delta_RWO_necessary_QQ_curve',
     necessaryCurve=profile(newM),onlyPaidQIndependentRemoval=hist,
     symmetricUMinusOneUsesNew6516WholeOriginalProof=True,
     uZeroUsesIndependent347cTrueDualAndNonzeroScaling=True,
     SZeroUsesThreeOriginalStaticAudits=True,
     allUnpaidWeightFibersKept=True,
     wholeNamedDeltaChartExcluded=int(newM.total_degree())==0)
 # Reuse only the independent, already executed D/T curve P. The
 # historical data is staged by terminal git, not transmitted via tools.
 legacy=Path(__file__).with_name('isp-hk-independent-Delta-Tnum-legacy.json')
 olddoc=json.loads(legacy.read_text())
 def walk(obj):
  if isinstance(obj,dict):
   yield obj
   for v in obj.values():yield from walk(v)
  elif isinstance(obj,list):
   for v in obj:yield from walk(v)
 matches=[r for r in walk(olddoc)
          if r.get('sha256')=='8af7c105334af350ef5047ee49cf27a5aadbfa204a11b64f9b7f7b8a352dd49c'
          and r.get('encoding')=='base64+zlib+json-lambda-u-coeff' and 'data' in r]
 assert matches,'independent frozen P not found; new M already returned above'
 data=json.loads(zlib.decompress(base64.b64decode(matches[0]['data'])))
 encoded=json.dumps(data,separators=(',',':')).encode()
 assert hashlib.sha256(encoded).hexdigest()=='8af7c105334af350ef5047ee49cf27a5aadbfa204a11b64f9b7f7b8a352dd49c'
 bctx=fmpq_mpoly_ctx.get(('lam','u'),'lex')
 oldP=bctx.from_dict({(int(i),int(j)):fmpq(c) for i,j,c in data})
 assert list(map(int,oldP.degrees()))==[28,3]
 fresh=bctx.from_dict({(int(m[0]),int(m[1])):c for m,c in newM.to_dict().items()})
 assert ctx.from_dict({(int(m[0]),int(m[1]),0):c for m,c in fresh.to_dict().items()})==newM
 def binfo(p):
  dat=[[int(m[0]),int(m[1]),str(c)] for m,c in sorted(p.to_dict().items())]
  rr=json.dumps(dat,separators=(',',':')).encode()
  return dict(degrees=list(map(int,p.degrees())) if p else [-1,-1],
              totalDegree=int(p.total_degree()) if p else -1,
              terms=len(dat),bytes=len(rr),sha256=hashlib.sha256(rr).hexdigest())
 say('new_corrected_Delta_only_independent_legacy_input',
     originalDTRun=46025096446,originalDTJob=140594347573,
     historicalCommit='ac40c96b0cfb3758fbf8bd380d18ca288a23601f',
     independentP=binfo(oldP),legacyWrongMNotDecodedOrUsed=True,
     oldDTSylvesterAndFactorizationNotExecuted=True,
     payloadPrintedSavedOrRecommitted=False)
 common=oldP.gcd(fresh);assert common
 pleft=ex(oldP,common);mleft=ex(fresh,common)
 say('new_corrected_Delta_actual_two_curve_decomposition',
     sharedCurve=binfo(common),independentResidual=binfo(pleft),
     correctedResidual=binfo(mleft),
     exactCover='sharedCurve=0 OR (independentResidual=0 AND correctedResidual=0)',
     allSharedAndLeadingZeroFibersKept=True,
     multivariateGCDOneNotTreatedAsEmpty=True,
     allOriginalPointFinitenessClaim=False)
 if int(common.total_degree())==0:
  dl,du=map(int,oldP.degrees());el,eu=map(int,fresh.degrees())
  bound=dl*eu+el*du
  say('new_corrected_Delta_finite_original_base_bound',
      differentLambdaUPointsAtMost=bound,
      proof='fixed u-Sylvester degree bound plus independent evaluation columns and determinant vanishing orders',
      completeQAndGramFibersStillRetained=True,
      ordinaryISPClaim=False,wholeNamedDeltaChartExcluded=int(fresh.total_degree())==0)
 else:
  # Optional classification only of this newly obtained common curve,
  # after the actual corrected projection and gcd have been returned.
  unit,factors=common.factor();back=bctx.constant(unit);records=[]
  for f,power in factors:
   back*=f**int(power);records.append(dict(power=int(power),factor=binfo(f)))
  assert back==common
  say('new_corrected_Delta_common_curve_full_QQ_support',
      factors=records,completeFactorProductReturned=True,
      noFactorRootOrIntersectionDiscarded=True)
say('new_corrected_Delta_Q_projection_finished',
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    exactDivisionProducts=divisions,
    oldFrozenLowZTargetsNotExecuted=True,
    noOldWrongCoverageRestored=True,
    noCoefficientCacheSaved=True,ordinaryISPClaim=False,
    peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
raw_timer(signal.ITIMER_REAL,0)
