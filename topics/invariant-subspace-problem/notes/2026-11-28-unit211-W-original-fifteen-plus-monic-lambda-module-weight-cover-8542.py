#!/usr/bin/env python3
"""NEW whole-W exact 15-row module plus the monic physical-lambda six.
Work in QQ(e,k)[lambda]^3 with 3 chi*ei rows and the exact original
G, G*Mx, G*My presentation. Every polynomial row cancellation is returned
coefficient by coefficient and retained as a source-defined DAG.
If e0 is obtained, ONLY the final reachable DAG denominators form a new
weight cover; no temporary leading coefficient is paid as physical.
The complete zero set of that cover remains. Its explicit depth exponent
clears the entire DAG, giving cover^N in the SAME original I6.
No old cofactor, old 12-order Sylvester, old NSPS determinant or old
spectral-factor test is executed. 180s/4GiB, no coefficient/cache payload.
"""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
from flint import fmpq
started=time.perf_counter();deadline=started+180
signal.alarm(180);resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**x):
 x['seconds']=time.perf_counter()-started
 print(json.dumps(x,separators=(',',':')),flush=True)
def digest(o):
 b=json.dumps(o,separators=(',',':')).encode()
 return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def frozen_prefix(basename,sha,marker,nbytes,prefixsha,label):
 path=Path(__file__).with_name(basename);raw=path.read_bytes()
 assert hashlib.sha256(raw).hexdigest()==sha
 assert raw.count(marker)==1
 pre=raw.split(marker)[0]
 assert len(pre)==nbytes and hashlib.sha256(pre).hexdigest()==prefixsha
 ns={'__file__':str(path),'__name__':label}
 with contextlib.redirect_stdout(io.StringIO()):
  exec(compile(pre,str(path)+'#new_input_necessary_prefix','exec'),ns)
 signal.alarm(max(1,math.ceil(deadline-time.perf_counter())))
 return ns
ch=frozen_prefix(
 '2026-11-28-unit211-W-global-physical-lambda-six-characteristic-original-input-8542.py',
 '563ef7c9682a4b52f30bea024a391588c747fd97b0a2e8a6c1a4f14a49ec2d65',
 b'# Strip only these TWO',8601,
 'ce868f00596f420d1a46a1503e2432be7bd13f0001e8ebc3e0cd68a53092fc7a',
 'necessary_actual_monic_lambda_coefficients_only')
tri=frozen_prefix(
 '2026-11-28-unit211-W-K7-open-physical-lambda-original-three-column-projection-binding-corrected-8542.py',
 '7cf3ff802cdf8166e3fb96f3ea806b81b83570f9200d10fad11caa13862f2c3f',
 b'\ndef lcoeff(p):',7854,
 'a15f2afbeeba04ae49ea8a50bf0ad927f41c9be11308a232d6e4dec5496ce693',
 'necessary_original_three_rules_and_eleven_rows_only')
R=tri['R'];ctx=tri['ctx'];zero=tri['zero'];one=tri['one']
ep,kp,xp,yp,Lp=ctx.gens()[:5]
pay=tri['pay'];strip=tri['strip']
rows=tri['rows'];rowtags=tri['rowtags'];labels=tri['labels']
matrices=tri['matrices'];errors=tri['errors'];xx=tri['xx'];yy=tri['yy']
basis=tri['basis'];original=tri['original'];verify=tri['verify']
# K7 is now paid by the entire-K7 complete original exclusion theorem.
# The frozen prefix's old "explicit chart" label is not used as a proof.
assert len(rows)==11
for label in ['NS','PS']:
 idx=labels.index(label)
 for axis,var in enumerate([xx,yy]):
  row=[sum((R(rows[idx][i])*matrices[axis][i][j] for i in range(3)),R()) for j in range(3)]
  tag=[var*rowtags[idx][g]-sum((R(rows[idx][i])*errors[axis][i][g] for i in range(3)),R()) for g in range(6)]
  with contextlib.redirect_stdout(io.StringIO()):
   tri['addrow'](row,tag,label+'*'+'xy'[axis])
# This supplies exactly the missing four same-point products, retaining
# any actually zero row as a zero generator rather than a rank assumption.
wanted=['N1','same_point_commutator_1','same_point_commutator_2',
 'N1*x','N1*y','same_point_commutator_1*x','same_point_commutator_1*y',
 'same_point_commutator_2*x','same_point_commutator_2*y',
 'NS','PS','NS*x','NS*y','PS*x','PS*y']
assert all(s in wanted for s in labels)
def enc(p):
 return [[[int(i) for i in mm],str(c)] for mm,c in sorted(p.to_dict().items())]
def profile(p):
 if not p:return dict(zero=True,terms=0)
 return dict(degrees=list(map(int,p.degrees()[:2])),totalDegree=int(p.total_degree()),
             terms=len(p.to_dict()),**digest(enc(p)))
def scalar(c,paid=False):
 c=R(c)
 assert all(not any(mm[j] for j in range(2,8)) for p in [c.n,c.d] for mm in p.to_dict())
 if paid:pay(c.d)
 return c
def trim(p):
 while p and not p[-1]:p.pop()
 return p
def padd(a,b):
 return trim([(a[i] if i<len(a) else R())+(b[i] if i<len(b) else R()) for i in range(max(len(a),len(b)))])
def pshiftmul(a,c,s):
 if not c or not a:return []
 return [R() for _ in range(s)]+[c*x for x in a]
def pminus(a,b):
 return padd(a,[-x for x in b])
def parse_poly(p):
 d={}
 for mon,c in p.to_dict().items():
  assert mon[2]==mon[3]==0 and not any(mon[j] for j in range(5,8))
  j=int(mon[4]);d[j]=d.get(j,zero)+c*ep**int(mon[0])*kp**int(mon[1])
 return trim([scalar(R(d.get(j,zero)),True) for j in range(max(d,default=-1)+1)])
def parse_rational_lambda(p):
 p=R(p);pay(p.d)
 assert all(not any(mon[j] for j in range(2,8)) for mon in p.d.to_dict())
 return [c/R(p.d) for c in parse_poly(p.n)]
chi=[scalar(R(c.n,c.d),True) for c in ch['chi']]
assert len(chi)==7 and chi[-1]==1
# Both frozen definitions use exactly the same original coordinates and
# same paid forward/back substitution. chi coefficients are weight-only.
inputs=[];input_labels=[]
for j in range(3):
 inputs.append([chi[:] if h==j else [] for h in range(3)])
 input_labels.append('monic_original_chi_times_basis_'+str(j))
zero_rows=[]
for lab in wanted:
 if lab not in labels:
  zero_rows.append(lab);continue
 i=labels.index(lab)
 verify(sum((R(rows[i][j])*basis[j] for j in range(3)),R()),rowtags[i])
 inputs.append([parse_poly(p) for p in rows[i]])
 input_labels.append(lab)
def leading(row):
 choices=[(len(p)-1,j) for j,p in enumerate(row) if p]
 return max(choices) if choices else None
def vector_meta(row):
 return dict(lambdaDegrees=[len(p)-1 for p in row],
  coefficientTerms=sum(len(c.n.to_dict())+len(c.d.to_dict()) for p in row for c in p),
  identity=digest([[[enc(c.n),enc(c.d)] for c in p] for p in row]))
def same(a,b):return all(a[j]==b[j] for j in range(3))
say(stage='new_whole_W_exact_fifteen_and_monic_lambda_module_input',
 originalPresentation='I6 polynomial quotient = A[lambda]^3/span(G,GMx,GMy)',
 originalRowsReturned=len(inputs)-3,zeroOriginalRows=zero_rows,
 allOriginalProductsActuallyReturned=True,monicLambdaDegree=6,
 totalOriginalInputRows=len(inputs),inputLabels=input_labels,
 allInputWeightDenominatorsAlreadyPaid=True,
 inputDefinition=digest([[[[enc(c.n),enc(c.d)] for c in p] for p in row] for row in inputs]),
 oldCofactorAndTwelveSylvesterExecuted=False,oldSpectralStripExecuted=False,
 noMatrixFreenessAssumed=True,noNewHeadPaid=True,claimExcluded=False)
# Nodes are source-defined exact row identities, with no expansion of
# final source coefficients into a potentially huge recomputable cache.
nodes=[dict(kind='input',input=i,depth=0) for i in range(len(inputs))]
basis_rows=[inputs[i] for i in range(3)];basis_ids=list(range(3))
steps=0;returns=0;swaps=0;processed=[];target=None
def reduce_once(row,rid,pivot,pid,lp,shift):
 global steps,returns
 coefficient=scalar(row[lp][-1]/pivot[lp][-1])
 assert coefficient*pivot[lp][-1]==row[lp][-1]
 mult=[pshiftmul(p,coefficient,shift) for p in pivot]
 nxt=[pminus(row[j],mult[j]) for j in range(3)]
 # All three polynomial columns, all lambda coefficients, are returned.
 back=[padd(nxt[j],mult[j]) for j in range(3)]
 assert same(back,row)
 returns+=sum(max(len(row[j]),len(back[j])) for j in range(3))+1
 oldlead=leading(row);newlead=leading(nxt)
 assert newlead is None or newlead<oldlead
 node=dict(kind='subtract',left=rid,right=pid,coefficient=coefficient,
           shift=shift,depth=1+max(nodes[rid]['depth'],nodes[pid]['depth']))
 nodes.append(node);steps+=1
 return nxt,len(nodes)-1
def current_unit():
 row=basis_rows[0]
 if leading(row)==(0,0):
  a=scalar(row[0][0]);assert a and not row[1] and not row[2]
  return basis_ids[0],scalar(1/a)
 return None
for index in range(3,len(inputs)):
 row=inputs[index];rid=index
 while leading(row) is not None:
  degree,lp=leading(row);bp=basis_rows[lp];bid=basis_ids[lp]
  bd,blp=leading(bp);assert blp==lp
  if degree<bd:
   basis_rows[lp],row=row,bp;basis_ids[lp],rid=rid,bid
   swaps+=1;degree,lp=leading(row);bp=basis_rows[lp];bid=basis_ids[lp]
   bd,blp=leading(bp);assert lp==blp and degree>=bd
  row,rid=reduce_once(row,rid,bp,bid,lp,degree-bd)
  target=current_unit()
  if target is not None:break
 processed.append(input_labels[index])
 say(stage='new_original_lambda_module_insertion',
     lastOriginalInput=input_labels[index],processedOriginalInputs=len(processed),
     reductionSteps=steps,allLambdaCoefficientReturnCount=returns,
     rowSwaps=swaps,basisLeadingPairs=[list(leading(r)) for r in basis_rows],
     basisProfiles=[vector_meta(r) for r in basis_rows],
     exactGenericUnitReached=(target is not None),
     allUnpaidParameterZeroFibresStillRetained=True,claimExcluded=False)
 if target is not None:break
if target is None:
 say(stage='new_original_lambda_module_finished_without_unit',
     processedOriginalInputs=processed,basisLeadingPairs=[list(leading(r)) for r in basis_rows],
     totalReductionSteps=steps,allCoefficientProductsReturned=returns,
     noCoverOrWeightEmptinessClaim=True,wholeCurrentWExcluded=False,
     sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
 signal.alarm(0);raise SystemExit(2)
tid,normalizer=target
assert leading(basis_rows[0])==(0,0)
assert pshiftmul(basis_rows[0][0],normalizer,0)==[R(1)]
assert not basis_rows[0][1] and not basis_rows[0][2]
# Keep exactly the reachable source DAG, not every discarded pivot.
todo=[tid];reachable=set()
while todo:
 i=todo.pop()
 if i in reachable:continue
 reachable.add(i);n=nodes[i]
 if n['kind']=='subtract':todo.extend([n['left'],n['right']])
h=hashlib.sha256();dag_bytes=0
for i in sorted(reachable):
 n=nodes[i]
 if n['kind']=='input':out=[i,'input',n['input'],n['depth']]
 else:
  c=n['coefficient'];out=[i,'subtract',n['left'],n['right'],n['shift'],
                         enc(c.n),enc(c.d),n['depth']]
 bb=json.dumps(out,separators=(',',':')).encode();h.update(bb);h.update(b'\n')
 dag_bytes+=len(bb)+1
identity=digest(dict(finalNode=tid,normalizer=[enc(normalizer.n),enc(normalizer.d)],
                    exactUnitRow=[1,0,0]))
say(stage='new_original_lambda_module_exact_generic_unit_DAG',
 actualTarget=[1,0,0],allFinalThreeLambdaColumnsReturned=True,
 allLocalThreeColumnPolynomialIdentitiesReturned=True,
 originalInputRows=len(inputs),processedOriginalInputs=processed,
 totalReductionSteps=steps,coefficientProductsReturned=returns,
 reachableNodes=len(reachable),sourceDAGBytes=dag_bytes,sourceDAGSHA256=h.hexdigest(),
 normalizedTargetIdentity=identity,
 sourceDagIsOriginalCombinationByExplicitInduction=True,
 expandedLeafCoefficientVectorClaimed=False,
 allUnpaidParameterZeroFibresRetained=True,claimExcluded=False)
# All q coefficients are pure weights. If delta contains each reachable
# denominator, delta^(depth+1) clears the entire recursively composed
# original combination, including the final normalizer.
delta=one;denominator_checks=0
coefficients=[normalizer]+[nodes[i]['coefficient'] for i in sorted(reachable) if nodes[i]['kind']=='subtract']
for c in coefficients:
 scalar(c)
 gg=delta.gcd(c.d);qq=c.d/gg;assert gg*qq==c.d
 delta*=qq
for c in coefficients:
 qq=delta/c.d;assert qq*c.d==delta
 denominator_checks+=1
cover,paid,hist=strip(delta)
assert cover*paid==delta;pay(paid)
norm=cover.coefficient(0);assert norm
cover=cover/norm
assert cover*norm*paid==delta
power=nodes[tid]['depth']+1
assert power>=1
say(stage='new_whole_W_original_module_complete_weight_cover',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 exactOriginalIdealConsequence='cover^power belongs to the original I6 after ONLY previously paid weight localization',
 power=power,cover=profile(cover),commonReachableDenominator=profile(delta),
 allReachableDenominatorProductsReturned=denominator_checks,
 paidStrippedFactors=hist,allStrippedProductsReturned=True,
 allParameterPolesOfReturnedOriginalIdentityContainedInCoverZero=True,
 cancelledTemporaryPivotsAreCoveredByTheExactCrossMultipliedIdentities=True,
 onlyExactReachableDAGDenominatorsUsed=True,
 numericalSamplingOrModularEmptinessUsed=False,
 squarefreeOrIrreducibleCoverClaim=False,
 finalSourceDAGBytes=dag_bytes,finalSourceDAGSHA256=h.hexdigest(),
 noRegenerableMatrixOrCoefficientCacheOrEncodedChunks=True,
 wholeCurrentWExcluded=(cover.total_degree()==0),
 ordinaryISPClaim=False,peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)
