#!/usr/bin/env python3
"""NEW correct Phi: QQ paid-factor entry valuations and exact matrix extraction.
Two already-defined original fixed Sylvester matrices are coefficient input.
For each PREDECLARED old paid weight h, compute every nonzero entry's exact
h-divisibility order. A MINIMUM assignment and its integral dual give K;
entrywise polynomial returns prove det(S)=h^K det(M) over QQ[u,Q].
Only these proved QQ factors are removed. No modular factor is removed.
The NEW quotient matrices are then compared on the SAME predetermined
p=1009, Q=2 and u=2 slices. Prior unnormalized determinants/gcds, upper
Hungarian gates, and highest matrices are NOT executed.
No expanded bivariate determinant, coefficient cache, or payload.
Absolute 120 seconds / 1 GiB. One pinned definition source + its four deps.
"""
import ast,hashlib,json,math,os,pathlib,resource,signal,time
from fractions import Fraction
from functools import reduce
START=time.perf_counter();DEADLINE=START+120
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
REAL_TIMER=signal.setitimer
def tick():
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute 120-second boundary')
def bounded_timer(which,seconds,interval=0):
 assert which==signal.ITIMER_REAL and not interval
 tick();remaining=DEADLINE-time.perf_counter()
 return REAL_TIMER(which,max(0.000001,remaining if seconds<=0
                            else min(float(seconds),remaining)),0)
def bounded_alarm(seconds):
 return int(math.ceil(bounded_timer(signal.ITIMER_REAL,seconds)[0]))
signal.setitimer=bounded_timer;signal.alarm=bounded_alarm
bounded_timer(signal.ITIMER_REAL,120)
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,sort_keys=True,separators=(',',':')),flush=True)
PRIME=1009
SLICES=[('u',0,2),('Q',1,2)]
DEP='2026-11-28-unit211-Phi-zero-corrected-Vlow-second-weight-support-two-axis-comparison-8542.py'
DEPSHA='060d321f863b93ef8d1825ca3dc86d41f12573101257b1ace3c3a6ac8e24e2f7'
PREFIXSHA='7313f0bda9d11c57e91e51019b7fe2fdc4c2d3442638df54d1355539a71bf678'
path=pathlib.Path(__file__).with_name(DEP)
if not path.exists():path=pathlib.Path(os.environ.get('ISP_INPUT_DIR',''))/DEP
oldtext=path.read_text()
assert hashlib.sha256(oldtext.encode()).hexdigest()==DEPSHA
marker='def sylvester_models(pair):'
assert oldtext.count(marker)==1
prefix=oldtext[:oldtext.index(marker)]
assert len(prefix.encode())==10491
assert hashlib.sha256(prefix.encode()).hexdigest()==PREFIXSHA
# Retain ONLY four pinned parameter definitions. Omit old clocks/logs.
# All parameter SHA assertions and exact arithmetic definitions stay.
kept=[];omitted=[]
for node in ast.parse(prefix,str(path)).body:
 skip=False
 if isinstance(node,ast.FunctionDef) and node.name in (
    'tick','bounded_timer','bounded_alarm','say'):skip=True
 if isinstance(node,ast.Assign):
  if any(isinstance(t,ast.Name) and t.id in (
       'ROOT_START','ROOT_DEADLINE','ORIGINAL_TIMER') for t in node.targets):skip=True
  if any(isinstance(t,ast.Attribute) and isinstance(t.value,ast.Name)
       and t.value.id=='signal' and t.attr in ('setitimer','alarm')
       for t in node.targets):skip=True
 if isinstance(node,ast.Expr) and isinstance(node.value,ast.Call):
  fn=node.value.func
  if isinstance(fn,ast.Name) and fn.id in ('say','bounded_timer'):skip=True
  if isinstance(fn,ast.Attribute) and isinstance(fn.value,ast.Name):
   if fn.value.id=='resource' and fn.attr=='setrlimit':skip=True
 if skip:omitted.append([node.lineno,type(node).__name__])
 else:kept.append(node)
ns={'__name__':'only_pinned_original_support_coefficients','__file__':str(path),
    'ROOT_START':START,'ROOT_DEADLINE':DEADLINE,'ORIGINAL_TIMER':REAL_TIMER,
    'tick':tick,'bounded_timer':bounded_timer,'bounded_alarm':bounded_alarm,
    'say':lambda *a,**kw:None,'print':lambda *a,**kw:None}
exec(compile(ast.fix_missing_locations(ast.Module(body=kept,type_ignores=[])),
             str(path)+'#10491-definition-bytes-only','exec'),ns)
signal.setitimer=bounded_timer;signal.alarm=bounded_alarm;tick()
assert ns['PRIME']==PRIME and ns['SLICES']==SLICES
ctx=ns['ctx'];O=ns['O'];Z=ns['Z'];up=ns['up'];Qp=ns['Qp']
profile=ns['profile'];wdict=ns['wdict']
weightns=ns['ns']  # nested original t-Gram definitions hold L, Mn, gg
# Reuse arithmetic FUNCTION DEFINITIONS only, after the old fixed-matrix
# definition. No old Hungarian upper or leading-rank function is imported.
helper_names={'axis_degree','modular_polynomial','poly_profile',
              'polynomial_det','xgcd_return'}
helper_nodes=[n for n in ast.parse(oldtext,str(path)).body
              if isinstance(n,ast.FunctionDef) and n.name in helper_names]
assert {n.name for n in helper_nodes}==helper_names
ns['stats']=dict(newPolynomialBareissProducts=0,newPolynomialEuclideanProducts=0)
ns['say']=lambda stage,**kw:say('new_QQ_extracted_'+stage,**kw)
exec(compile(ast.fix_missing_locations(ast.Module(body=helper_nodes,type_ignores=[])),
             str(path)+'#arithmetic-functions-only','exec'),ns)
modpoly=ns['modular_polynomial'];poly_profile=ns['poly_profile']
poly_det=ns['polynomial_det'];xgcd=ns['xgcd_return']
NEW=dict(exactValuationDivisions=0,failedValuationRemaindersReturned=0,
         assignmentDualInequalities=0,extractedEntryReturns=0,
         positiveMultiplicationReturns=0,integerCoefficientChecks=0)

def from_weight_dict(data):
 return ctx.from_dict({(i,j,0,0,0):c for (i,j),c in data.items()})
def fixed_matrix(pair):
 a,b=pair;m,n=a['degree'],b['degree'];size=m+n
 out=[]
 for model,count in ((a,n),(b,m)):
  for shift in range(count):
   row=[Z for _ in range(size)]
   for k,co in enumerate(model['coefficients']):
    row[shift+k]=from_weight_dict(co)
   out.append(row)
 assert len(out)==size and all(len(row)==size for row in out)
 return out
models=[
 dict(label='F12_QQ_paid_quotient',matrix=fixed_matrix(ns['lmodels']),
      originalTotalUpper=444,originalAxisUpper=[402,222],
      originalAxisLower=[402,222],originalExactAxes=[True,True]),
 dict(label='G14_QQ_paid_quotient',matrix=fixed_matrix(ns['tmodels']),
      originalTotalUpper=730,originalAxisUpper=[643,371],
      originalAxisLower=[642,371],originalExactAxes=[False,True])]
assert [len(x['matrix']) for x in models]==[12,14]
say('new_QQ_paid_matrix_input',
 originalDefinitionSourceSHA256=DEPSHA,necessaryPrefixBytes=10491,
 necessaryPrefixSHA256=PREFIXSHA,omittedClockAndLogStatements=omitted,
 allFourNestedParameterDependenciesSHA256Checked=True,
 newTarget='exact QQ paid divisors of both original matrices, then only quotient supports',
 priorProofRun=46156015273,
 priorGlobalDegreeBoundsUsedAsTheorems=True,
 noOldUnnormalizedDeterminantGCDOrLeadingMatrixExecuted=True,
 fixedPrime=PRIME,fixedSlices=[dict(variable=s[0],otherCoordinate=s[2]) for s in SLICES],
 noPostResultPrimeSliceOrOrderChoice=True)

def primitive_integer(p):
 p=ctx.constant(p) if not hasattr(p,'to_dict') else p
 assert p and int(p.total_degree())>0
 data={ex:Fraction(str(c)) for ex,c in p.to_dict().items()}
 dd=1
 for c in data.values():dd=math.lcm(dd,c.denominator)
 vals={ex:c.numerator*(dd//c.denominator) for ex,c in data.items()}
 cc=reduce(math.gcd,(abs(v) for v in vals.values()))
 assert cc>0
 out=ctx.from_dict({ex:v//cc for ex,v in vals.items()})
 assert out*cc==p*dd
 if Fraction(str(out.coefficient(0)))<0:out=-out;cc=-cc
 assert out*cc==p*dd
 return out,dict(multiplier=str(Fraction(dd,cc)),profile=profile(out))
# These are old paid factors of the SAME correct original physical chart.
# Last factor is paid by m=(u-1)(Q+2u-4)/Q. No theta/alpha/new head.
atoms_raw=[
 ('Q',Qp),('u',up),('u-1',up-1),('delta',1-Qp),
 ('Kw',Qp+4*(up-1)),('L',weightns['L'].n),('Mn',weightns['Mn'].n),
 ('2ell-1 numerator',2*weightns['L'].n-Qp),('m linear factor',Qp+2*up-4)]
assert ns['m']*ns['Q']==ns['R']((up-1)*(Qp+2*up-4))
assert weightns['gg']*ns['Q']==ns['R'](2*weightns['L'].n-Qp)
atoms=[]
for label,p0 in atoms_raw:
 h,info=primitive_integer(p0)
 assert all(not any(int(e) for e in ex[2:]) for ex in h.to_dict())
 atoms.append((label,h,info))
say('new_predeclared_original_paid_integer_factors',
 orderedFactors=[dict(label=label,**info) for label,h,info in atoms],
 mPaymentIdentityReturned=True,twoEllMinusOnePaymentIdentityReturned=True,
 noNewFactorInverted=True,noModularFactorInspectedOrDeleted=True)

def matrix_profile(mat):
 digest=hashlib.sha256();nonzero=0;largestTotal=-1
 for i,row in enumerate(mat):
  for j,p0 in enumerate(row):
   digest.update(json.dumps([i,j,profile(p0)],sort_keys=True,separators=(',',':')).encode())
   if p0:nonzero+=1;largestTotal=max(largestTotal,int(p0.total_degree()))
 return dict(size=len(mat),nonzeroEntries=nonzero,largestEntryTotalDegree=largestTotal,
             entryProfileListSHA256=digest.hexdigest())
def check_integral(p0):
 for c in p0.to_dict().values():
  assert Fraction(str(c)).denominator==1
  NEW['integerCoefficientChecks']+=1
def exact_order(p0,h):
 assert p0
 current=p0;order=0
 while True:
  tick();quot,rem=divmod(current,h)
  assert quot*h+rem==current
  NEW['exactValuationDivisions']+=1
  if rem:
   NEW['failedValuationRemaindersReturned']+=1
   return order
  assert quot and int(quot.total_degree())<int(current.total_degree())
  current=quot;order+=1

def minimum_assignment(values):
 """Integral MINIMUM dual a_i+b_j<=v_ij; zero entries are forbidden."""
 n=len(values)
 finite=[v for row in values for v in row if v is not None]
 assert finite
 big=(max(finite)+1)*(n+1)+1
 cost=[[big if v is None else v for v in row] for row in values]
 pu=[0]*(n+1);pv=[0]*(n+1);p=[0]*(n+1);way=[0]*(n+1)
 for i in range(1,n+1):
  p[0]=i;j0=0;best=[10**12]*(n+1);used=[False]*(n+1)
  while True:
   used[j0]=True;i0=p[j0];change=10**12;j1=0
   for j in range(1,n+1):
    if not used[j]:
     cur=cost[i0-1][j-1]-pu[i0]-pv[j]
     if cur<best[j]:best[j]=cur;way[j]=j0
     if best[j]<change:change=best[j];j1=j
   assert j1
   for j in range(n+1):
    if used[j]:pu[p[j]]+=change;pv[j]-=change
    else:best[j]-=change
   j0=j1
   if p[j0]==0:break
  while True:
   j1=way[j0];p[j0]=p[j1];j0=j1
   if not j0:break
 assignment=[None]*n
 for j in range(1,n+1):assignment[p[j]-1]=j-1
 assert all(j is not None and values[i][j] is not None
            for i,j in enumerate(assignment))
 a=pu[1:];b=pv[1:]
 for i,row in enumerate(values):
  for j,v in enumerate(row):
   if v is not None:
    assert a[i]+b[j]<=v
    NEW['assignmentDualInequalities']+=1
 total=sum(a)+sum(b)
 assert total==sum(values[i][j] for i,j in enumerate(assignment)) and total>=0
 return dict(rowWeights=a,columnWeights=b,assignment=assignment,exponent=total)

for model in models:
 mat=model['matrix'];model['inputProfile']=matrix_profile(mat)
 model['factors']=[];model['extractedTotalDegree']=0
 model['extractedAxisDegrees']=[0,0]
 for label,h,info in atoms:
  tick()
  values=[[exact_order(p0,h) if p0 else None for p0 in row] for row in mat]
  dual=minimum_assignment(values);power=dual['exponent']
  if power:
   cache={0:O}
   def hp(k):
    if k not in cache:cache[k]=h**k
    return cache[k]
   newmat=[]
   for i,row in enumerate(mat):
    newrow=[]
    for j,p0 in enumerate(row):
     exponent=dual['rowWeights'][i]+dual['columnWeights'][j]
     if not p0:q0=Z
     elif exponent>=0:
      q0,rem=divmod(p0,hp(exponent))
      assert not rem and q0*hp(exponent)==p0
     else:
      q0=p0*hp(-exponent)
      assert q0==p0*hp(-exponent)
      NEW['positiveMultiplicationReturns']+=1
     check_integral(q0);newrow.append(q0)
     NEW['extractedEntryReturns']+=1
    newmat.append(newrow)
   mat=newmat
   model['factors'].append((label,h,power))
   model['extractedTotalDegree']+=power*int(h.total_degree())
   for axis in (0,1):
    model['extractedAxisDegrees'][axis]+=power*int(h.degrees()[axis])
  valbytes=json.dumps(values,separators=(',',':')).encode()
  say('new_QQ_paid_entry_valuation_and_universal_matrix_identity',
      support=model['label'],factor=label,primitiveFactor=info,
      completeEntryValuationMatrixSHA256=hashlib.sha256(valbytes).hexdigest(),
      completeNonzeroValuationsReturned=True,minimumAssignmentDual=dual,
      exactDeterminantIdentity='det(previous)=h^K det(next)',
      negativeDualExponentsOnlyMultiplyOldPaidPolynomial=True,
      allSquareEntryIdentitiesReturned=bool(power),
      zeroExtractionLeavesMatrixUnchanged=not bool(power),
      currentMatrix=matrix_profile(mat),
      totalExtractedDegree=model['extractedTotalDegree'],
      extractedAxisDegrees=model['extractedAxisDegrees'],
      noGenericDVRPivotAndNoClaimAllDivisibilityExtracted=True)
 model['matrix']=mat
 model['totalUpper']=model['originalTotalUpper']-model['extractedTotalDegree']
 model['axisUpper']=[model['originalAxisUpper'][i]-model['extractedAxisDegrees'][i]
                     for i in (0,1)]
 model['axisLower']=[max(0,model['originalAxisLower'][i]-model['extractedAxisDegrees'][i])
                     for i in (0,1)]
 assert model['totalUpper']>=0 and all(x>=0 for x in model['axisUpper'])
 model['wdicts']=[[wdict(p0) for p0 in row] for row in mat]
 say('new_QQ_quotient_support_defined',
     support=model['label'],originalInputProfile=model['inputProfile'],
     quotientMatrixProfile=matrix_profile(mat),
     exactOldPaidFactorExponents=[dict(label=l,exponent=k) for l,h,k in model['factors']],
     originalPolynomialIdealMembershipPreservedAfterOldWeightLocalization=True,
     totalDegreeUpper=model['totalUpper'],
     coordinateDegreeLower=model['axisLower'],coordinateDegreeUpper=model['axisUpper'],
     exactCoordinateFlags=model['originalExactAxes'],
     knownNonzeroOriginalSupportMakesQuotientNonzero=True,
     noBivariateDeterminantExpanded=True)

if not all(model['factors'] for model in models):
 say('new_QQ_entry_extraction_retained_without_replaying_unchanged_support',
     eachMatrixHasPositiveExtraction=[bool(model['factors']) for model in models],
     exactQQMatrixExtractionsAndDegreeBoundsAlreadyReturned=True,
     quotientAxisComparisonNotEntered=True,
     noOldUnnormalizedDeterminantOrGCDReexecuted=True,
     allUnsettledSupportFibresRetained=True,wholePhiExcluded=False,
     statistics=NEW)
 REAL_TIMER(signal.ITIMER_REAL,0)
 raise SystemExit(0)

axis_results=[]
for axis_name,axis,fixed in SLICES:
 polys=[];support_records=[]
 for model in models:
  tick()
  determinant=poly_det([[modpoly(co,axis,fixed) for co in row]
                       for row in model['wdicts']],model['label'],axis_name)
  upper=model['axisUpper'][axis];lower=model['axisLower'][axis]
  assert not determinant or int(determinant.degree())<=upper
  # This is a NEW quotient coefficient check, using already proved QQ degrees.
  # We never run the old unnormalized determinant/leading-matrix proof gate.
  preserved=(bool(determinant) and model['originalExactAxes'][axis]
             and int(determinant.degree())==upper)
  polys.append(determinant)
  support_records.append(dict(support=model['label'],QQDegreeLower=lower,
     QQDegreeUpper=upper,QQDegreeAlreadyExact=model['originalExactAxes'][axis],
     quotientModularPolynomial=poly_profile(determinant),
     quotientDegreePreserved=preserved))
 gcd0,a,b=xgcd(*polys)
 unit=bool(gcd0) and int(gcd0.degree())==0
 preserved=any(r['quotientDegreePreserved'] for r in support_records)
 result=dict(variable=axis_name,otherCoordinate=fixed,prime=PRIME,
     supports=support_records,wholeModularGCD=poly_profile(gcd0),
     firstBezoutMultiplier=poly_profile(a),secondBezoutMultiplier=poly_profile(b),
     completeNewTwoSupportBezoutReturned=True,
     strictQQCommonPositiveDegreeExclusion=bool(unit and preserved),
     QQCommonFactorDegreeUpper=(int(gcd0.degree()) if gcd0 and preserved else None),
     noModularPaidFactorDeletion=True,
     allRemainingHeadZerosAndFactorsRetained=not bool(unit and preserved))
 axis_results.append(result)
 say('new_QQ_paid_quotient_support_fixed_axis_result',**result)
all_paid=all(x['strictQQCommonPositiveDegreeExclusion'] for x in axis_results)
say('new_QQ_paid_entry_extraction_two_support_comparison_finished',
 sourceSHA256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
 outcomes=[dict(support=model['label'],
     exactOldPaidFactorExponents=[dict(label=l,exponent=k) for l,h,k in model['factors']],
     quotientTotalDegreeUpper=model['totalUpper'],
     quotientCoordinateLower=model['axisLower'],quotientCoordinateUpper=model['axisUpper'],
     quotientMatrixProfile=matrix_profile(model['matrix'])) for model in models],
 QQNoCommonCurveProved=all_paid,
 pureQContentSeparatelyCovered=axis_results[1]['strictQQCommonPositiveDegreeExclusion'],
 QQCommonFactorBidegreeUpper=[x['QQCommonFactorDegreeUpper'] for x in axis_results],
 weightPointBezoutUpper=(models[0]['totalUpper']*models[1]['totalUpper'] if all_paid else None),
 allResidualQQDivisibilityAndWeightFibresRetained=not all_paid,
 noOldUnnormalizedAxisProofReplayed=True,
 noExpandedDeterminantOrCoefficientPayloadSaved=True,
 wholePhiExcluded=False,ordinaryISPClaim=False,
 statistics=NEW,newQuotientUnivariateStatistics=ns['stats'],
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
REAL_TIMER(signal.ITIMER_REAL,0)
