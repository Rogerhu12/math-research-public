#!/usr/bin/env python3
"""NEW correct whole Phi: a fixed lambda-Sylvester pure-weight support.
Only the already established two C6 parameter definitions are rebuilt.
No old 15-column, action, cofactor certificate, head factor or gcd gate.
Select the FIRST eligible member of the fixed point list using only paid
weights and the TWO fixed top coefficients. After the new lambda test
there is NO further point/prime choice. A nonzero determinant only proves
one nonzero original pure-weight polynomial; no original fiber is called empty.
120 seconds /1 GiB, no expanded QQ determinant or coefficient payload.
"""
import ast,hashlib,json,math,os,pathlib,resource,signal,time
from fractions import Fraction
from functools import reduce
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
PRIME=1009
POINTS=[(2,2),(3,2),(4,2),(5,2),(6,2),(2,3),(3,3),(4,3)]
assert all(PRIME%d for d in range(2,math.isqrt(PRIME)+1))
NAME='2026-11-28-unit211-Phi-zero-corrected-whole-original-I6-fifteen-by-three-8542.py'
path=pathlib.Path(__file__).with_name(NAME)
if not path.exists():path=pathlib.Path(os.environ.get('ISP_INPUT_DIR',''))/NAME
full=path.read_text()
assert hashlib.sha256(full.encode()).hexdigest()=='84e0efcc19a0274d571484b187b7b155c81ebf255e40a39c38ac13a03f911cf0'
# The definition-only AST below deliberately omits old top-level asserts.
# Pin the second full dependency OUTSIDE that AST before any execution.
SECOND_NAME='2026-11-28-unit211-Phi-zero-corrected-dual-germ-four-original-quadratic-heads-8542.py'
second=path.with_name(SECOND_NAME)
if not second.exists():second=pathlib.Path(os.environ.get('ISP_INPUT_DIR',''))/SECOND_NAME
assert hashlib.sha256(second.read_bytes()).hexdigest()=='5ee86ff89db7c8babaf3a22c7d72570dcdfbbf92646f56adf37bff854a87ace7'
marker='seeds=[rN,rNS,rPS,c1,c2]'
assert full.count(marker)==1
prefix=full[:full.index(marker)]
assert len(prefix)==12067 and hashlib.sha256(prefix.encode()).hexdigest()=='e2e9bab84bca700400c8e26d5787208c9aceafe27c64aa7ecf828b0552025a1f'
kept=[];omitted=[]
for node in ast.parse(prefix,str(path)).body:
 skip=isinstance(node,ast.Assert)
 if isinstance(node,ast.Expr) and isinstance(node.value,ast.Call):
  skip=skip or isinstance(node.value.func,ast.Name) and node.value.func.id=='say'
 if isinstance(node,ast.For):
  skip=not(isinstance(node.target,ast.Name) and node.target.id=='f'
           and isinstance(node.iter,ast.Name) and node.iter.id=='forms')
 if isinstance(node,ast.Assign):
  names={v.id for v in node.targets if isinstance(v,ast.Name)}
  skip=skip or bool(names & {'AA','BB','normalized','eT','eZ','ntrace'})
 if skip:omitted.append([node.lineno,type(node).__name__])
 else:kept.append(node)
ns={'__name__':'new_fixed_lambda_resultant_known_coefficient_definitions',
    '__file__':str(path),'print':lambda *a,**kw:None}
exec(compile(ast.fix_missing_locations(ast.Module(body=kept,type_ignores=[])),
             str(path)+'#coefficient-definitions-only','exec'),ns)
signal.alarm=bounded_alarm;signal.alarm(120)
R=ns['R'];ctx=ns['ctx'];O=ns['O'];Z=ns['Z']
exact=ns['exact'];profile=ns['profile'];strip_paid=ns['strip_paid']
seeds=[ns['rN'],ns['rNS'],ns['rPS'],ns['c1'],ns['c2']]
expected=[
 ('NP',[0,1,2],
  'fcf79be98410a2eea2ebdb588b441b8f4aceb20acb4704a96ee34fc0012d01d5',
  '63c05c345cbc7055d652d46c173684bd7fdb159db3741232ef94d6cb58992bf6'),
 ('overlaps',[0,3,4],
  '2407107501f1790a288ecabd75f14f92c7602859bfc033727b76312675f91014',
  '9794fac2ee8bf7de08d80b9f3102480f1d06c9cfb4ff8be3981817dcfbd682fb')]
models=[];constant_scale_returns=0
for label,chosen,knowncore,knownhead in expected:
 rr=[seeds[i] for i in chosen]
 mu=[rr[1][1]*rr[2][2]-rr[1][2]*rr[2][1],
     rr[2][1]*rr[0][2]-rr[2][2]*rr[0][1],
     rr[0][1]*rr[1][2]-rr[0][2]*rr[1][1]]
 den=O
 for v in mu:den=exact(den,den.gcd(v.d))*v.d
 nums=[v.n*exact(den,v.d) for v in mu];common=Z
 for p in nums:common=common.gcd(p)
 primitive=[R(exact(p,common)) for p in nums]
 scalar=sum((primitive[i]*rr[i][0] for i in range(3)),R())
 core,removed=strip_paid(scalar.n)
 lc=core.coefficient(0);core/=lc;removed*=lc
 assert core*removed==scalar.n and profile(core)['sha256']==knowncore
 head=ctx.from_dict({(ex[0],ex[1],0,0,0):c for ex,c in core.to_dict().items()
                     if int(ex[2])==6})
 assert profile(head)['sha256']==knownhead
 assert all(int(ex[3])==0 and int(ex[4])==0 and int(ex[2])<=6
            for ex in core.to_dict())
 data={ex:Fraction(str(c)) for ex,c in core.to_dict().items()}
 denominator=1
 for c in data.values():denominator=math.lcm(denominator,c.denominator)
 nums={ex:c.numerator*(denominator//c.denominator) for ex,c in data.items()}
 content=reduce(math.gcd,(abs(c) for c in nums.values()))
 assert content>0
 ints={ex:c//content for ex,c in nums.items()}
 integer_model=ctx.from_dict(ints)
 scale=Fraction(denominator,content)
 assert integer_model*content==core*denominator
 constant_scale_returns+=len(ints)
 total=int(core.total_degree())
 coefficients=[]
 for j in range(7):
  cj=ctx.from_dict({(ex[0],ex[1],0,0,0):c for ex,c in ints.items()
                    if int(ex[2])==j})
  assert not cj or int(cj.total_degree())<=total-j
  coefficients.append(cj)
 assert coefficients[6]
 models.append(dict(label=label,core=core,integer=integer_model,
                    coefficients=coefficients,total=total,scale=scale))
say('new_fixed_lambda_original_input_definitions_ready',
 twoOriginalCoreSHA256=[profile(m['core'])['sha256'] for m in models],
 primitiveIntegerModels=[profile(m['integer']) for m in models],
 onlyNonzeroRationalConstantScalingsUsed=True,
 actualConstantScalingCoefficientReturns=constant_scale_returns,
 originalLambdaDegrees=[6,6],originalTotalDegrees=[m['total'] for m in models],
 originalNecessaryPrefixBytes=len(prefix),
 omittedOldTopLevelProofStatements=omitted,
 noOldActionOverlapFifteenRowCofactorOrHeadGCDGateExecuted=True,
 noPhysicalDOrItsNormInverse=True)
def evaluate_weight(poly,u0,q0):
 ans=0
 for ex,c in poly.to_dict().items():
  assert not any(int(ex[j]) for j in (2,3,4))
  cc=Fraction(str(c))
  assert cc.denominator%PRIME
  ans=(ans+cc.numerator*pow(cc.denominator,-1,PRIME)
       *pow(u0,int(ex[0]),PRIME)*pow(q0,int(ex[1]),PRIME))%PRIME
 return ans
# Neither point selection nor prime selection depends on an ideal/gcd test.
selected=None;point_checks=[]
for u0,q0 in POINTS:
 paid=evaluate_weight(ns['paidSupport'],u0,q0)
 h=[evaluate_weight(m['coefficients'][6],u0,q0) for m in models]
 eligible=paid!=0 and u0%PRIME!=0 and all(h)
 point_checks.append(dict(point=[u0,q0],originalPaidProduct=paid,
                          twoActualFixedTopCoefficients=h,eligible=bool(eligible)))
 if eligible:
  selected=(u0,q0);break
# Entry degree certificate for the FIXED original 12 by 12 matrix.
# Rows 0..5 are lambda^r C_NP, rows 6..11 are lambda^r C_ov,
# and columns are lambda^0,...,lambda^11. No leading coefficient inverse.
row_weights=[models[0]['total']+r for r in range(6)]+[models[1]['total']+r for r in range(6)]
column_weights=[-j for j in range(12)]
defined_nonzero_entries=0
for i in range(12):
 mi=0 if i<6 else 1;shift=i%6
 for j in range(12):
  a=j-shift
  if 0<=a<=6:
   p=models[mi]['coefficients'][a]
   if p:
    assert int(p.total_degree())<=row_weights[i]+column_weights[j]
    defined_nonzero_entries+=1
degree_upper=sum(row_weights)+sum(column_weights)
assert degree_upper==6*sum(m['total'] for m in models)-36
say('new_fixed_lambda_sylvester_whole_definition_and_degree_bound',
 shape=[12,12],fixedOriginalLambdaDegrees=[6,6],
 rowDegreeWeights=row_weights,columnDegreeWeights=column_weights,
 totalPureWeightDegreeUpperBound=degree_upper,
 allNonzeroEntryBoundsReturned=defined_nonzero_entries,
 noQQDeterminantExpansion=True,allLambdaLeadingZeroFibersKept=True,
 predeterminedPrime=PRIME,predeterminedPointList=[list(x) for x in POINTS],
 eligiblePointChecks=point_checks,selectedPoint=list(selected) if selected else None,
 noPostIdealTestPointOrPrimeChange=True)
def trim(a):
 a=[int(x)%PRIME for x in a]
 while a and not a[-1]:a.pop()
 return a
def add(a,b):
 return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
              for i in range(max(len(a),len(b)))])
def neg(a):return trim([-x for x in a])
def mul(a,b):
 if not a or not b:return []
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%PRIME
 return trim(c)
def smul(a,c):return trim([v*c for v in a])
divisions=0
def pdiv(a,b):
 global divisions
 a=trim(a);b=trim(b);assert b;original=a[:]
 q=[0]*max(0,len(a)-len(b)+1);bi=pow(b[-1],-1,PRIME)
 while len(a)>=len(b):
  j=len(a)-len(b);c=a[-1]*bi%PRIME;q[j]=(q[j]+c)%PRIME
  for k,v in enumerate(b):a[j+k]=(a[j+k]-c*v)%PRIME
  a=trim(a)
 q=trim(q);assert add(mul(q,b),a)==original;divisions+=1
 return q,a
def xgcd(a,b):
 r0=a[:];r1=b[:];s0=[1];s1=[];t0=[];t1=[1]
 while r1:
  q,r=pdiv(r0,r1)
  r0,r1=r1,r
  s0,s1=s1,add(s0,neg(mul(q,s1)))
  t0,t1=t1,add(t0,neg(mul(q,t1)))
 inv=pow(r0[-1],-1,PRIME)
 g=smul(r0,inv);s0=smul(s0,inv);t0=smul(t0,inv)
 assert add(mul(s0,a),mul(t0,b))==g
 return g,s0,t0
def det_with_return(S):
 a=[r[:] for r in S];E=[[int(i==j) for j in range(12)] for i in range(12)]
 sign=1;rank=0
 for k in range(12):
  r=next((i for i in range(k,12) if a[i][k]),None)
  if r is None:
   det=0;break
  if r!=k:
   a[k],a[r]=a[r],a[k];E[k],E[r]=E[r],E[k];sign=-sign
  iv=pow(a[k][k],-1,PRIME)
  for i in range(k+1,12):
   cc=a[i][k]*iv%PRIME
   if cc:
    a[i]=[(x-cc*y)%PRIME for x,y in zip(a[i],a[k])]
    E[i]=[(x-cc*y)%PRIME for x,y in zip(E[i],E[k])]
  rank+=1
 else:
  det=sign
  for i in range(12):det=det*a[i][i]%PRIME
 for i in range(12):
  for j in range(12):
   assert sum(E[i][k]*S[k][j] for k in range(12))%PRIME==a[i][j]
 return det%PRIME,rank
if selected is None:
 say('new_fixed_lambda_point_not_eligible',
     noNewQQNonzeroDeterminantClaim=True,allOriginalFibersRetained=True)
else:
 f0=[evaluate_weight(p,*selected) for p in models[0]['coefficients']]
 f1=[evaluate_weight(p,*selected) for p in models[1]['coefficients']]
 assert len(trim(f0))==7 and len(trim(f1))==7
 g,a,b=xgcd(f0,f1)
 S=[]
 for row in (f0,f1):
  for shift in range(6):
   r=[0]*12
   for j,c in enumerate(row):r[shift+j]=c
   S.append(r)
 determinant,rank=det_with_return(S)
 assert bool(determinant)==(len(g)==1)
 say('new_original_fixed_lambda_same_point_return',
     prime=PRIME,point=list(selected),
     firstOriginalLambdaPolynomial=f0,secondOriginalLambdaPolynomial=f1,
     actualSameLambdaMonicGCD=g,
     firstBezoutMultiplier=a,secondBezoutMultiplier=b,
     completeOriginalLambdaBezoutReturned=True,
     exactModularDivisionProducts=divisions,
     fixed12SylvesterDeterminant=determinant,
     fixed12WholeTransformationCoordinatesReturned=144,
     modularEliminationPivots=rank,
     newQQPureWeightDeterminantProvedNonzero=bool(determinant),
     determinantTotalPureWeightDegreeAtMost=degree_upper,
     originalWholeWeightNecessityUsesFixedAdjugate=True,
     allOriginalLambdaLeadingZeroFibersRetained=True,
     all434CommonHeadWeightFibersRetained=True,
     noGlobalEmptyOrExactQQDegreeInference=True,
     originalWholePhiExcluded=False,ordinaryISPClaim=False)
say('new_fixed_lambda_pure_weight_support_first_input_finished',
 sourceSHA256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
 noExpandedQQDeterminantComputed=True,noCoefficientPayloadSaved=True,
 noOldProofGateReplayed=True,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
RAW_ALARM(0)
