#!/usr/bin/env python3
"""NEW Q-primary target for either of the two correct-Phi quotient matrices.
ISP_Q0_MODEL is frozen as F or G in separate FIRST workflows.
Only reconstruct the already-defined normalized matrix by its fixed integral
row/column scales; check its published profile. Never recompute entry
valuations/minimum assignments, old determinants, or any sliced gcd.
New arithmetic is QQ[u]-UNIMODULAR row Euclid at Q=0. Every two-row
Bezout change has determinant 1 and returns BOTH full QQ[u,Q] rows by
the inverse two-row identity. Only actual complete zero rows are divided
by Q. Each finished round proves a new exact determinant identity.
A full-rank constant matrix proves the resulting Q-order is EXACT;
a timeout retains only already finished rounds. No nonconstant u inverse,
no modular factor, no geometric localization or prime selection.
Absolute 120 seconds / 1 GiB per frozen F/G input.
"""
import ast,hashlib,json,math,os,pathlib,resource,signal,time
START=time.perf_counter();DEADLINE=START+120
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
REAL_TIMER=signal.setitimer
def tick():
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute 120-second boundary')
def bounded_timer(which,seconds,interval=0):
 assert which==signal.ITIMER_REAL and not interval
 tick();left=DEADLINE-time.perf_counter()
 return REAL_TIMER(which,max(0.000001,left if seconds<=0 else min(float(seconds),left)),0)
def bounded_alarm(seconds):
 return int(math.ceil(bounded_timer(signal.ITIMER_REAL,seconds)[0]))
signal.setitimer=bounded_timer;signal.alarm=bounded_alarm
bounded_timer(signal.ITIMER_REAL,120)
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,sort_keys=True,separators=(',',':')),flush=True)
MODEL=os.environ.get('ISP_Q0_MODEL','')
assert MODEL in ('F','G'),'A workflow must fix ISP_Q0_MODEL=F or G before execution.'
from flint import fmpq_poly
UP=fmpq_poly;ZERO=UP([]);ONE=UP([1])
DEP='2026-11-28-unit211-Phi-zero-corrected-Vlow-second-weight-support-two-axis-comparison-8542.py'
DEPSHA='060d321f863b93ef8d1825ca3dc86d41f12573101257b1ace3c3a6ac8e24e2f7'
PREFIXSHA='7313f0bda9d11c57e91e51019b7fe2fdc4c2d3442638df54d1355539a71bf678'
path=pathlib.Path(__file__).with_name(DEP)
if not path.exists():path=pathlib.Path(os.environ.get('ISP_INPUT_DIR',''))/DEP
oldtext=path.read_text()
assert hashlib.sha256(oldtext.encode()).hexdigest()==DEPSHA
marker='def sylvester_models(pair):';assert oldtext.count(marker)==1
prefix=oldtext[:oldtext.index(marker)]
assert len(prefix.encode())==10491
assert hashlib.sha256(prefix.encode()).hexdigest()==PREFIXSHA
kept=[]
for node in ast.parse(prefix,str(path)).body:
 skip=False
 if isinstance(node,ast.FunctionDef) and node.name in ('tick','bounded_timer','bounded_alarm','say'):skip=True
 if isinstance(node,ast.Assign):
  if any(isinstance(t,ast.Name) and t.id in ('ROOT_START','ROOT_DEADLINE','ORIGINAL_TIMER') for t in node.targets):skip=True
  if any(isinstance(t,ast.Attribute) and isinstance(t.value,ast.Name)
         and t.value.id=='signal' and t.attr in ('setitimer','alarm') for t in node.targets):skip=True
 if isinstance(node,ast.Expr) and isinstance(node.value,ast.Call):
  fn=node.value.func
  if isinstance(fn,ast.Name) and fn.id in ('say','bounded_timer'):skip=True
  if (isinstance(fn,ast.Attribute) and isinstance(fn.value,ast.Name)
      and fn.value.id=='resource' and fn.attr=='setrlimit'):skip=True
 if not skip:kept.append(node)
ns={'__name__':'only_original_support_parameter_definitions','__file__':str(path),
    'ROOT_START':START,'ROOT_DEADLINE':DEADLINE,'ORIGINAL_TIMER':REAL_TIMER,
    'tick':tick,'bounded_timer':bounded_timer,'bounded_alarm':bounded_alarm,
    'say':lambda *a,**kw:None,'print':lambda *a,**kw:None}
exec(compile(ast.fix_missing_locations(ast.Module(body=kept,type_ignores=[])),
             str(path)+'#original-coefficients-only','exec'),ns)
signal.setitimer=bounded_timer;signal.alarm=bounded_alarm;tick()
ctx=ns['ctx'];O=ns['O'];Z=ns['Z'];up=ns['up'];Qp=ns['Qp']
profile=ns['profile'];weightns=ns['ns']
# These short integer scale arrays define the PUBLISHED quotient matrices.
# They are not a replay of their valuation/minimum-assignment proof.
SCALES={
 'F':[
  {"factor":"Q","exponent":1,"rows":[1,1,1,1,1,1,1,1,1,1,1,1],"columns":[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0]},
  {"factor":"u-1","exponent":4,"rows":[2,2,2,2,1,1,2,2,2,1,1,1],"columns":[-2,-2,-2,-2,-2,-2,-1,-1,-1,0,0,0]},
  {"factor":"L","exponent":15,"rows":[7,7,6,5,4,3,7,7,6,6,6,5],"columns":[-7,-7,-7,-6,-6,-6,-5,-4,-3,-2,-1,0]}
 ],
 'G':[
  {"factor":"u-1","exponent":8,"rows":[3,3,3,3,3,3,2,2,3,3,3,3,2,2],"columns":[-3,-3,-3,-3,-3,-3,-3,-3,-2,-2,-1,-1,0,0]},
  {"factor":"delta","exponent":48,"rows":[6,7,8,9,10,11,12,13,8,9,10,11,12,13],"columns":[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13]},
  {"factor":"Kw","exponent":1,"rows":[1,1,1,1,1,1,1,1,1,1,1,1,1,1],"columns":[0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]},
  {"factor":"Mn","exponent":8,"rows":[4,4,4,4,3,3,2,2,4,4,4,4,3,3],"columns":[-4,-4,-4,-4,-4,-4,-4,-3,-3,-2,-2,-1,-1,0]},
  {"factor":"2ell-1 numerator","exponent":4,"rows":[2,3,3,3,3,3,3,3,2,3,3,3,3,3],"columns":[0,-1,-2,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3]}
 ]
}
EXPECTED={
 'F':'ec03ed0d0eae88a7349a8423167b559d62c7504436e27980bbcd78969c11ed8a',
 'G':'a93eb7f9abf50874a215866708a9f95c182fafda4ba49680871c21c3f51e2a42'}
DEGREE={
 'F':dict(uLower=368,uUpper=368,QExact=206,totalUpper=409),
 'G':dict(uLower=593,uUpper=594,QExact=302,totalUpper=633)}
atoms={'Q':Qp,'u-1':up-1,'delta':Qp-1,'Kw':Qp+4*(up-1),
       'L':-weightns['L'].n,'Mn':-weightns['Mn'].n,
       '2ell-1 numerator':-(2*weightns['L'].n-Qp)}
def weight_poly(data):
 return ctx.from_dict({(i,j,0,0,0):c for (i,j),c in data.items()})
def fixed_matrix(pair):
 a,b=pair;n=a['degree']+b['degree'];out=[]
 for model,count in ((a,b['degree']),(b,a['degree'])):
  for shift in range(count):
   row=[Z for _ in range(n)]
   for k,c in enumerate(model['coefficients']):row[shift+k]=weight_poly(c)
   out.append(row)
 assert len(out)==n and all(len(row)==n for row in out)
 return out
mat=fixed_matrix(ns['lmodels'] if MODEL=='F' else ns['tmodels'])
size=len(mat);assert size==(12 if MODEL=='F' else 14)
for spec in SCALES[MODEL]:
 h=atoms[spec['factor']];aa=spec['rows'];bb=spec['columns']
 assert len(aa)==size and len(bb)==size
 assert sum(aa)+sum(bb)==spec['exponent']
 cache={0:O}
 def hp(k):
  if k not in cache:cache[k]=h**k
  return cache[k]
 new=[]
 for i,row in enumerate(mat):
  newrow=[]
  for j,value in enumerate(row):
   e=aa[i]+bb[j]
   if not value:value0=Z
   elif e>=0:
    value0,rem=divmod(value,hp(e));assert not rem
   else:value0=value*hp(-e)
   newrow.append(value0)
  new.append(newrow)
 mat=new
digest=hashlib.sha256()
for i,row in enumerate(mat):
 for j,value in enumerate(row):
  digest.update(json.dumps([i,j,profile(value)],sort_keys=True,separators=(',',':')).encode())
assert digest.hexdigest()==EXPECTED[MODEL]
say('new_Q_primary_quotient_parameter_definition',
 model=MODEL,size=size,publishedQuotientMatrixProfileSHA256=digest.hexdigest(),
 sourceOfDefinitionRun=46158891405,sourceOfDefinitionJob=141021539125,
 originalDefinitionPrefixBytes=10491,originalDefinitionPrefixSHA256=PREFIXSHA,
 allFourNestedParameterDependenciesSHA256Checked=True,
 fixedScaleRowsAndColumnsOnly=True,
 noOldValuationsAssignmentsDeterminantsOrSlicedGCDsExecuted=True,
 knownGlobalDegreeBounds=DEGREE[MODEL],factor='Q',
 newTarget='unimodular QQ[u] row Euclid and full QQ[u,Q] Q-division')

# Use a fixed, fully faithful rectangular COEFFICIENT CONTAINER:
# entry j is a QQ[u] polynomial list for Q^0,...,Q^QMAX.
# It is not a quotient by Q^(QMAX+1): every original coefficient is present,
# and the new row operations never increase Q-degree.
QMAX=max(int(ex[1]) for row in mat for value in row for ex in value.to_dict())
WIDTH=QMAX+1
def unpack(value):
 data={}
 for ex,c in value.to_dict().items():
  assert not any(ex[2:]);data.setdefault(int(ex[1]),{})[int(ex[0])]=c
 out=[]
 for q in range(WIDTH):
  d=data.get(q,{})
  co=[0]*(1+max(d,default=-1))
  for u,c in d.items():co[u]=c
  out.append(UP(co))
 return out
rows=[[v for value in row for v in unpack(value)] for row in mat]
assert all(len(row)==size*WIDTH for row in rows)
def pack(coefficients):
 data={}
 for q,p0 in enumerate(coefficients):
  for u in range(int(p0.degree())+1):
   if p0[u]:data[(u,q,0,0,0)]=p0[u]
 return ctx.from_dict(data)
for i in range(size):
 for j in range(size):
  assert pack(rows[i][j*WIDTH:(j+1)*WIDTH])==mat[i][j]
del mat
say('new_full_bivariate_row_container_returned',
 model=MODEL,size=size,QCoefficientWidth=WIDTH,fullOriginalEntryReturns=size*size,
 noQTruncationOrNilpotentQuotient=True,
 everyNewOperationPreservesOrLowersQDegree=True)

COUNTS=dict(twoRowBezoutBlocks=0,quotientReturns=0,determinantOneReturns=0,
            fullInverseRowCoordinateReturns=0,rowSwaps=0,
            fullQDivisionCoordinateReturns=0,echelonZeroChecks=0)
QORDER_BOUND=min(DEGREE[MODEL]['QExact'],DEGREE[MODEL]['totalUpper']-DEGREE[MODEL]['uLower'])
assert QORDER_BOUND>=0
q_power=0;det_sign=1;rounds=[]
say('new_Q_primary_a_priori_order_bound',model=MODEL,QOrderUpper=QORDER_BOUND,
    source='known total upper minus known u lower; no new computation of old degrees')

def polynomial_profile(p0):
 co=[str(p0[i]) for i in range(int(p0.degree())+1)]
 raw=json.dumps(co,separators=(',',':')).encode()
 return dict(degree=int(p0.degree()),terms=sum(bool(p0[i]) for i in range(len(co))),
             sha256=hashlib.sha256(raw).hexdigest())

def full_rows_profile(rr):
 digest=hashlib.sha256();terms=0;max_u=-1;max_q=-1;max_total=-1
 for i,row in enumerate(rr):
  for j in range(size):
   for q,p0 in enumerate(row[j*WIDTH:(j+1)*WIDTH]):
    for u in range(int(p0.degree())+1):
     c=p0[u]
     if c:
      digest.update(json.dumps([i,j,u,q,str(c)],separators=(',',':')).encode())
      terms+=1;max_u=max(max_u,u);max_q=max(max_q,q);max_total=max(max_total,u+q)
 return dict(size=size,termsAcrossAllEntries=terms,largestEntryUDegree=max_u,
             largestEntryQDegree=max_q,largestEntryTotalDegree=max_total,
             fullCoefficientStreamSHA256=digest.hexdigest())

def unimodular_echelon(rr,round_index):
 # At each column choose the least degree among the remaining NONZERO
 # entries, then the lowest row index. This deterministic rule is frozen.
 # There are no modular choices, points, or nonconstant polynomial inverses.
 rr=[row[:] for row in rr]
 rank=0;sign=1;pivots=[]
 for column in range(size):
  tick()
  slot=column*WIDTH
  choices=[(int(rr[i][slot].degree()),i) for i in range(rank,size) if rr[i][slot]]
  if not choices:continue
  chosen=min(choices)[1]
  if chosen!=rank:
   rr[chosen],rr[rank]=rr[rank],rr[chosen]
   sign=-sign;COUNTS['rowSwaps']+=1
  for i in range(rank+1,size):
   tick()
   b=rr[i][slot]
   if not b:continue
   a=rr[rank][slot];assert a
   g,s0,t0=a.xgcd(b)
   assert g and s0*a+t0*b==g
   aa,ra=divmod(a,g);bb,rb=divmod(b,g)
   assert not ra and not rb and aa*g==a and bb*g==b
   COUNTS['quotientReturns']+=2
   assert s0*aa+t0*bb==ONE
   COUNTS['determinantOneReturns']+=1
   old_a=rr[rank];old_b=rr[i]
   new_a=[s0*x+t0*y for x,y in zip(old_a,old_b)]
   new_b=[-bb*x+aa*y for x,y in zip(old_a,old_b)]
   # FULL inverse two-row return, including every Q coefficient.
   # [[aa,-t0],[bb,s0]] is the exact inverse over QQ[u].
   for x,y,old_x,old_y in zip(new_a,new_b,old_a,old_b):
    assert aa*x-t0*y==old_x and bb*x+s0*y==old_y
    COUNTS['fullInverseRowCoordinateReturns']+=2
   assert new_a[slot]==g and not new_b[slot]
   rr[rank]=new_a;rr[i]=new_b
   COUNTS['twoRowBezoutBlocks']+=1
  assert rr[rank][slot]
  for i in range(rank+1,size):
   assert not rr[i][slot]
   COUNTS['echelonZeroChecks']+=1
  pivots.append((column,rr[rank][slot]))
  rank+=1
  if rank==size:break
  if rank%3==0:
   say('new_unimodular_Q0_echelon_partial_round',
       model=MODEL,round=round_index,completedPivots=rank,
       alreadyProvedQPower=q_power,
       completedTwoRowBlocks=COUNTS['twoRowBezoutBlocks'],
       noNewQPowerClaimedBeforeFullZeroRowReturn=True)
 # Entire zero rows, not merely zeros in selected pivot columns.
 for i in range(rank,size):
  assert all(not rr[i][j*WIDTH] for j in range(size))
  COUNTS['echelonZeroChecks']+=size
 # Pivot rows are genuinely independent over QQ(u); no pivot polynomial
 # is inverted in the transformations or interpreted as a physical unit.
 for i,(column,pivot) in enumerate(pivots):
  assert pivot and all(not rr[k][column*WIDTH] for k in range(i+1,size))
 return rr,rank,sign,pivots

for round_index in range(QORDER_BOUND+1):
 tick()
 transformed,rank,sign,pivots=unimodular_echelon(rows,round_index)
 nullity=size-rank
 if nullity==0:
  # Full triangular/echelon head has product of nonzero pivots, hence
  # nonzero determinant in QQ[u]. This pays exact Q valuation.
  det_sign*=sign;rows=transformed
  final=full_rows_profile(rows)
  say('new_Q_primary_exact_valuation_finished',
      model=MODEL,size=size,round=round_index,rank=rank,QExponent=q_power,
      exactQOrder=True,allQQUPivotsNonzero=True,
      nonzeroConstantDeterminantDefinedByPivotProduct=True,
      constantHeadPivotProfiles=[dict(column=j,**polynomial_profile(p)) for j,p in pivots],
      exactDeterminantIdentity='published_quotient = sign * Q^exponent * det(final_matrix)',
      determinantSign=det_sign,wholeBivariateMatrix=final,
      newQDegree=DEGREE[MODEL]['QExact']-q_power,
      newUDegreeLower=DEGREE[MODEL]['uLower'],
      newUDegreeUpper=DEGREE[MODEL]['uUpper'],
      newTotalDegreeUpper=DEGREE[MODEL]['totalUpper']-q_power,
      noNonconstantUPolynomialInverted=True,
      noNewAxisOrModularComparisonExecuted=True,
      noGeometricFibreDiscarded=True,wholePhiExcluded=False,
      completedRounds=rounds,statistics=COUNTS,
      sourceSHA256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
      peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
  REAL_TIMER(signal.ITIMER_REAL,0)
  break
 newrows=[row[:] for row in transformed[:rank]]
 for i in range(rank,size):
  old=transformed[i];new=[]
  for j in range(size):
   co=old[j*WIDTH:(j+1)*WIDTH]
   assert not co[0]
   after=co[1:]+[ZERO]
   assert len(after)==WIDTH
   for q in range(WIDTH):
    assert co[q]==(ZERO if q==0 else after[q-1])
    COUNTS['fullQDivisionCoordinateReturns']+=1
   new.extend(after)
  assert any(new),'Known nonzero determinant forbids a full zero polynomial row.'
  newrows.append(new)
 assert len(newrows)==size
 q_power+=nullity;det_sign*=sign
 assert q_power<=QORDER_BOUND
 rows=newrows
 actual=dict(round=round_index,rank=rank,nullity=nullity,
             cumulativeQExponent=q_power,determinantSign=det_sign)
 rounds.append(actual)
 say('new_complete_unimodular_Q_primary_round_returned',
     model=MODEL,**actual,
     fullZeroRowsAndEveryQDivisionCoordinateReturned=True,
     everyRowOperationUnimodularOverQQU=True,
     allNonconstantUPivotZeroSetsPreserved=True,
     exactDeterminantIdentity='published_quotient = sign * Q^exponent * det(current_matrix)',
     QExponentIsProvedLowerBoundUntilFullRank=True,
     currentMatrixProfile=full_rows_profile(rows),
     statistics=COUNTS,wholePhiExcluded=False)
else:
 raise AssertionError('Nonzero determinant and known Q degree require termination.')
