#!/usr/bin/env python3
"""NEW whole alpha=0: true qV/EBe norm, then fixed Q projections.
Only the earlier monic-two and original-row DEFINITIONS are reconstructed.
No earlier three-pair proof gate or old B/Phi elimination is replayed.
The norm is composed to the two RAW means, all four V coordinates return;
only the four actual multiplier contents are canceled.  New fixed
Q-resultants retain every leading-zero fiber.  120 seconds / 1 GiB.
"""
import hashlib,json,math,os,pathlib,resource,signal,time
from flint import fmpq_poly
START=time.perf_counter();DEADLINE=START+120
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
RAW_ALARM=signal.alarm
def tick():
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute 120 second boundary')
def bounded_alarm(seconds):
 tick();left=max(1,math.ceil(DEADLINE-time.perf_counter()))
 return RAW_ALARM(left if seconds<=0 else max(1,min(int(seconds),left)))
signal.alarm=bounded_alarm;signal.alarm(120)
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,sort_keys=True),flush=True)
BASE_NAME='2026-11-28-unit211-Phi-zero-true-whole-alpha-zero-monic-V-two-8542.py'
BASE_SHA='58cab31654894e8b4a4309f1c6b69619f5ee19591f74256f3128dd2026a4f025'
path=pathlib.Path(__file__).with_name(BASE_NAME)
if not path.exists():path=pathlib.Path(os.environ.get('ISP_INPUT_DIR',''))/BASE_NAME
full=path.read_text();assert hashlib.sha256(full.encode()).hexdigest()==BASE_SHA
assert full.count('results=[]')==1
prefix=full[:full.index('results=[]')]
assert hashlib.sha256(prefix.encode()).hexdigest()=='7d6fc9ed844a83daccf3978ed572a4b3a803266875c229fb5d3a42e3a75e751c'
ns={'__name__':'new_alpha_zero_norm_original_definitions','__file__':str(path),
    'print':lambda *a,**kw:None}
exec(compile(prefix,str(path)+'#monic_two_and_original_values_definitions','exec'),ns)
signal.alarm=bounded_alarm;signal.alarm(120)
R=ns['R'];ctx=ns['ctx'];oneP=ns['oneP'];zeroP=ns['zeroP']
vc=ns['vc'];paid=ns['paid'];strip=ns['strip'];exact=ns['exact'];info=ns['info']
EBe=ns['EBe'];EBo=ns['EBo'];head=ns['head'];q0,q1,_=ns['qcoeff']
rows=ns['valueRows'];a,b=rows[0].c0,rows[0].c1;e2=vc(EBe,2)
raw=[EBe,EBo];coeff=[[vc(v,j) for j in range(3)] for v in raw]
assert EBe-(q0+q1*ns['V']+ns['V']**2)*e2==a+b*ns['V']
norm=a*a-q1*a*b+q0*b*b
m0,m1=a-q1*b,-b
multipliers=[m0,m1,(b*b-e2*m0)/head,-e2*m1/head]
def returned(mm):
 out=[R() for _ in range(4)]
 for k in range(3):
  out[k]+=mm[0]*coeff[0][k]+mm[2]*coeff[1][k]
  out[k+1]+=mm[1]*coeff[0][k]+mm[3]*coeff[1][k]
 return out
ret=returned(multipliers)
assert ret[0]==norm and all(not v for v in ret[1:])
den=oneP
for v in multipliers:
 paid(v.d);den=exact(den,den.gcd(v.d))*v.d
paid(den)
nums=[v.n*exact(den,v.d) for v in multipliers]
content=zeroP
for v in nums:content=content.gcd(v)
assert content
primitive=[R(exact(v,content)) for v in nums]
ret=returned(primitive);assert all(not v for v in ret[1:])
scalar=ret[0];paid(scalar.d)
assert R(content)*scalar==R(den)*norm
def normalized(p):
 out,removed=strip(p)
 if out:
  lc=out.coefficient(0);out/=lc;removed*=lc
 assert out*removed==p
 return out
core=normalized(scalar.n)
say('new_whole_alpha_zero_original_qV_EBe_norm',
 normCore=info(core),actualFourMultiplierCommon=info(content),
 scalarDenominator=info(scalar.d),
 allFourRawMeanCoordinatesReturned=True,
 fullActualCommonZeroFaceKept=True,
 rawMeans=['EBe','EBo'],noOriginalLinearHeadInverse=True)
# These are PARAMETER definitions of three already returned scalars,
# not another execution of their old original-pair proof gate.
EXPECTED=[
 '9da720bb18618e80ba9db96559e73dd25c9e4600a8e1576e6e8f046d36e61ad1',
 '80c26662a4c2cbde3cb5e55976061cb117ea9a8ad7d9954c50a2b5e22b95ae83',
 'c04b14a34183209fa97fc6c34f6b503afedbc212c29bbdcc98a0c9b517c5338f']
old_cores=[]
for row,expected in zip(rows[1:],EXPECTED):
 value=row.c1*a-b*row.c0;paid(value.d)
 p=normalized(value.n)
 assert info(p)['sha256']==expected
 old_cores.append(p)
say('existing_alpha_zero_three_scalar_parameters_defined',
 exactScalarHashes=EXPECTED,oldPairProofGateNotExecuted=True,
 necessaryPrefixSHA256=hashlib.sha256(prefix.encode()).hexdigest())
def qp(p):
 assert all(int(ex[2])==0 for ex in p.to_dict())
 return max((int(ex[1]) for ex in p.to_dict()),default=-1)
def univar(p):
 assert all(int(ex[1])==int(ex[2])==0 for ex in p.to_dict())
 n=int(p.degrees()[0]) if p else -1;out=[0]*(n+1)
 for ex,c in p.to_dict().items():out[int(ex[0])]=c
 return fmpq_poly(out)
def embed(p):
 return ctx.from_dict({(j,0,0):p[j] for j in range(int(p.degree())+1) if p[j]})
def pinfo(p):
 raw=str(p).encode()
 return {'degree':int(p.degree()),'coefficientBytes':len(raw),
         'sha256':hashlib.sha256(raw).hexdigest()}
if not core:
 say('new_alpha_zero_norm_identically_zero',
  originalIdentityReturned=True,wholeAlphaZeroExcluded=False,
  noNewProjectionComputed=True,ordinaryISPClaim=False)
elif int(core.total_degree())==0:
 say('new_alpha_zero_norm_original_unit',
  entireAlphaZeroExcluded=True,wholePhiExcluded=False,ordinaryISPClaim=False)
else:
 content0,factors=core.factor();back=ctx.constant(content0);facinfo=[]
 for fac,power in factors:
  power=int(power);back*=fac**power
  facinfo.append({'factor':info(fac),'multiplicity':power})
 assert back==core
 say('new_alpha_zero_norm_complete_QQ_factorization',
  entireProductReturned=True,factors=facinfo,allZeroFibersKept=True)
 # Whole original coefficient Bezout: no unproved vertical exclusion.
 conditions=[core]+old_cores;coefficients=[];vbez=[];vg=fmpq_poly([])
 positions=[]
 for index,p in enumerate(conditions):
  for j in range(qp(p)+1):
   cp=ctx.from_dict({(ex[0],0,0):c for ex,c in p.to_dict().items() if int(ex[1])==j})
   c=univar(cp)
   if not c:continue
   gg,aa,bb=vg.xgcd(c)
   assert aa*vg+bb*c==gg
   vbez=[aa*v for v in vbez]+[bb];coefficients.append(c)
   positions.append([index,j]);vg=gg
   assert sum((v*c0 for v,c0 in zip(vbez,coefficients)),fmpq_poly([]))==vg
   if int(vg.degree())==0:break
  if int(vg.degree())==0:break
 vertical_remaining=normalized(embed(vg))
 no_vertical=bool(vertical_remaining) and int(vertical_remaining.total_degree())==0
 say('new_alpha_zero_joint_vertical_coefficient_return',
  gcd=pinfo(vg),usedCoefficientPositions=positions,
  wholeQQCoefficientBezoutReturned=True,
  noPhysicalCommonVerticalFiber=no_vertical,
  remainingVerticalPolynomial=info(vertical_remaining))
 # NEW complete symbolic fixed resultants; all u-specialized heads kept.
 projections=[];g=fmpq_poly([]);bez=[]
 for label,p in zip(['CN','CS'],old_cores[:2]):
  tick();fixed_degrees=[qp(core),qp(p)]
  res=core.resultant(p,'Q');ru=univar(res)
  projections.append(ru)
  if ru:
   gg,aa,bb=g.xgcd(ru)
   assert aa*g+bb*ru==gg
   bez=[aa*v for v in bez]+[bb];g=gg
  else:bez.append(fmpq_poly([]))
  assert sum((b*r for b,r in zip(bez,projections)),fmpq_poly([]))==g
  say('new_alpha_zero_complete_fixed_Q_resultant',
   otherOriginalCondition=label,fixedQDegrees=fixed_degrees,
   fixedSylvesterSize=sum(fixed_degrees),resultant=pinfo(ru),
   allQLeadingZeroFibersKept=True,completeQQBezoutReturned=True,
   currentGCD=pinfo(g))
 remaining=normalized(embed(g))
 excluded=bool(remaining) and int(remaining.total_degree())==0
 maxQ=max(map(qp,conditions))
 bound=None
 if remaining and no_vertical:
  bound=maxQ*int(remaining.degrees()[0])
 say('new_alpha_zero_original_norm_projection_result',
  necessaryUPolynomial=info(remaining),
  entireAlphaZeroExcluded=excluded,
  noPhysicalCommonVerticalFiber=no_vertical,
  distinctWeightPointUpperBound=bound,
  maxOriginalQDegree=maxQ,
  allUnpaidWeightZeroFibersKept=True,
  onlyPaidWeightFactorsRemoved=True,wholePhiExcluded=False,
  ordinaryISPClaim=False)
