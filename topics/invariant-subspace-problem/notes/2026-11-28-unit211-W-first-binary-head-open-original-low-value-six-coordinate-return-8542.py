#!/usr/bin/env python3
"""NEW actual original value return on the explicitly retained first
canonical binary-head principal open H265 != 0. It is NOT globally paid.
Return four real cubic rules, 12 multiplication columns, two ORIGINAL
overlap remainders, and the original pure R3/q4 value equations.
Try the constant 1 from these same-point rows and their true lambda/S
multiples over QQ(e,k). Any final parameter denominator and the whole
H265 zero curve remain in the weight cover. No freeness claim. No old
15-minor / NSNV / big resultant gate. 180 seconds / 4 GiB. No data cache."""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
start=time.perf_counter();deadline=start+180;signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**r):
 r['seconds']=time.perf_counter()-start
 print(json.dumps(r,separators=(',',':')),flush=True)
dep=Path(__file__).with_name('2026-11-28-unit211-W-six-original-binary-cubics-and-weight-head-8542.py')
raw=dep.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='edbba216705016a86f222a9b165bf9dd11320a5953438ddf21ea4a26c581b7b2'
marker=b"\ncombos=list(itertools.combinations(range(6),4))"
assert raw.count(marker)==1
prefix=raw.split(marker)[0]
assert hashlib.sha256(prefix).hexdigest()=='fe3da9b05cba74f3311e3cad5737d0baf67e0da3144f6396d1a740c3ac1e70d4'
ns={'__file__':str(dep),'__name__':'__six_cubic_input_only_for_new_same_point_value_return__'}
with contextlib.redirect_stdout(io.StringIO()):
 exec(compile(prefix,str(dep),'exec'),ns)
signal.alarm(max(1,math.ceil(deadline-time.perf_counter())))
C,P,ctx,x,y,head,scaled,cubics,detpoly,binary,prof,paid,ppaid,strip_paid,base=[
 ns[v] for v in ['C','P','ctx','x','y','head','scaled','cubics','detpoly','binary','prof','paid','ppaid','strip_paid','base']]
zero=ctx.constant(0);one=ctx.constant(1)
mat=[head[i] for i in [0,1,2,3]]
delta=detpoly(mat)
H,removed=strip_paid(delta)
scalar=H.coefficient(0);H=H/scalar;removed*=scalar
assert H*removed==delta
assert prof(H)['sha256']=='b7f6ab4da28caa429f15fdb73034135568d8e73428aa1e813ee8cca292ba35c3'
# EXPLICIT conditional chart. Keep H=0 in every later global cover.
# No change to the underlying globally paid list is asserted.
strip_paid.__globals__['atoms'].append(H)
paid.__globals__['new_atoms'].append(H)
paid(1/C(delta))
iv=[]
for i in range(4):
 row=[]
 for j in range(4):
  mm=[[mat[r][c] for c in range(4) if c!=i] for r in range(4) if r!=j]
  cf=detpoly(mm)*((-1)**(i+j))
  v=C(cf,delta);paid(v);row.append(v)
 iv.append(row)
for i in range(4):
 for j in range(4):
  assert sum((iv[i][h]*C(mat[h][j]) for h in range(4)),C())==C(int(i==j))
  assert sum((C(mat[i][h])*iv[h][j] for h in range(4)),C())==C(int(i==j))
mm3=[(3,0),(2,1),(1,2),(0,3)]
monomials=[(x**i)*(y**j) for i,j in mm3]
rules=[sum((scaled[h].scale(iv[j][h]) for h in range(4)),P()) for j in range(4)]
for j in range(4):
 binary(rules[j]-monomials[j],2);ppaid(rules[j])
say(stage='new_W_H265_open_actual_four_original_binary_rules',
 chart='only the whole explicitly retained H265 != 0 principal open',
 allThirtyTwoTrueWeightMatrixProductsReturned=True,
 allFourCompleteOriginalCubicRulesReturned=True,
 HZeroWholeOriginalFibreRetained=True,
 noUnpaidHeadDeclaredGlobalUnit=True,
 actualRuleCertificate=base['digest'](rules))
basis_powers=[(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]
basis=[(x**i)*(y**j) for i,j in basis_powers]
reduction_count=0
def reduce_new(pp,label,bound=6):
 global reduction_count
 initial=P(pp);rem=P(pp);qq=[P() for _ in range(4)]
 while True:
  dd=binary(rem,bound)
  high=[mm for mm in dd if sum(mm)>=3]
  if not high:break
  i,j=max(high,key=lambda z:(sum(z),z[0],z[1]))
  if i>=3:h=0
  elif i>=2:h=1
  elif i>=1:h=2
  else:h=3
  di,dj=mm3[h]
  term=((x**(i-di))*(y**(j-dj))).scale(dd[(i,j)])
  rem-=term*rules[h];qq[h]+=term
 assert initial==rem+sum((qq[j]*rules[j] for j in range(4)),P())
 binary(rem,2);ppaid(rem);reduction_count+=1
 return rem,qq
def vector(pp):
 dd=binary(pp,2)
 assert all(mm in basis_powers for mm in dd)
 return [dd.get(mm,C()) for mm in basis_powers]
def vprofile(v):
 assert len(v)==6
 for c in v:assert c.n.degrees()[2]<=0 and c.d.degrees()[2]<=0
 dat=json.dumps([dict(n=prof(c.n),d=prof(c.d)) for c in v],separators=(',',':')).encode()
 return dict(coordinates=6,coefficientProfileBytes=len(dat),
             coefficientProfileSHA256=hashlib.sha256(dat).hexdigest(),
             maxNumeratorDegrees=[max((int(c.n.degrees()[j]) for c in v),default=-1) for j in range(2)],
             maxDenominatorDegrees=[max((int(c.d.degrees()[j]) for c in v),default=-1) for j in range(2)],
             numeratorTerms=sum(len(c.n.to_dict()) for c in v))
multiplication={}
column_polys=[]
for name,var in [('lambda',x),('S',y)]:
 cols=[]
 for j,bp in enumerate(basis):
  rem,qq=reduce_new(var*bp,name+'_times_basis_'+str(j),3)
  assert var*bp==rem+sum((qq[h]*rules[h] for h in range(4)),P())
  cols.append(vector(rem));column_polys.append(rem)
 multiplication[name]=[[cols[j][i] for j in range(6)] for i in range(6)]
say(stage='new_W_H265_open_twelve_true_weight_multiplication_columns',
 actualGenerators=['1','lambda','S','lambda^2','lambda*S','S^2'],
 allTwelveCompleteOriginalProductsReturned=True,
 noFreedomOrCommutativityOfChosenSixGeneratorsAssumed=True,
 columnCertificate=base['digest'](column_polys),
 allScalarDenominatorsOnlyPaidWeightsAndExplicitHChart=True)
# NEW original low-degree value input. Its entire R4/C4 identity is used,
# not a bare q3 coefficient equation with a geometric head inverted here.
original=base['ns']
R4=original['R4'];q4=original['q4'];q3=original['q3'];theta=original['theta']
L4=R4.t.get((0,4),C())
R3=R4-q4.scale(L4)
assert R3==q3.scale(theta)
binary(R3,4);binary(q4,4)
inputs=[('original_h4_overlap',cubics[4]),('original_h5_overlap',cubics[5]),
        ('entire_original_R3_value',R3),('entire_original_q4_value',q4)]
vectors=[];names=[];input_traces={}
for name,pp in inputs:
 rem,qq=reduce_new(pp,name,4)
 vv=vector(rem)
 vectors.append(vv);names.append(name)
 input_traces[name]=base['digest'](qq)
 say(stage='new_W_H265_open_true_original_six_coordinate_row',
     name=name,remainderZero=not bool(rem),profile=vprofile(vv),
     completeOriginalPolynomialAndFourRuleMultipliersReturned=True,
     originalTrace=input_traces[name],
     noPhysicalDOrNewGeometricInverse=True,
     HZeroFibreRetained=True,wholeWExcluded=False)
say(stage='new_W_H265_open_complete_new_same_point_value_input',
 fourOriginalRows=names,
 originalR3Identity='R3=R4-[S^4]R4*q4=theta*q3',
 noGeometricThreeMinusTwoLambdaInverseInNewValueRows=True,
 allOriginalRulesMultiplicationAndInputRowsActuallyReturned=True,
 actualNewPolynomialReductionProducts=reduction_count,
 originalFullNPStillRequiredUnlessThisNecessarySubsystemExcludes=True,
 noOldWholeCofactorGateReplayed=True)
# True value row v satisfies v*M_lambda=lambda*v and v*M_S=S*v.
# Consequently each product below is a same-point original necessary
# column even when the displayed generators are not free.
def matvec(mm,v):
 return [sum((mm[i][j]*v[j] for j in range(6)),C()) for i in range(6)]
basis_cols=[];raw_columns=[];raw_names=[]
def add_original_column(v,name):
 raw_columns.append(list(v));raw_names.append(name)
 idx=len(raw_columns)-1
 vec=list(v);tag={idx:C(1)}
 for rec in basis_cols:
  cc=vec[rec['pivot']]
  if not cc:continue
  vec=[v0-cc*w0 for v0,w0 in zip(vec,rec['vector'])]
  for j,c0 in rec['tag'].items():
   tag[j]=tag.get(j,C())-cc*c0
   if not tag[j]:del tag[j]
 pivot=next((j for j,c0 in enumerate(vec) if c0),None)
 if pivot is not None:
  # Generic QQ(e,k) pivot; NOT asserted to be globally paid.
  pc=vec[pivot];ip=C(1)/pc
  assert ip*pc==1
  vec=[c0*ip for c0 in vec];tag={j:c0*ip for j,c0 in tag.items() if c0*ip}
  assert vec[pivot]==1
  basis_cols.append(dict(pivot=pivot,vector=vec,tag=tag))
  say(stage='new_W_H265_generic_weight_column_pivot',
      originalColumn=name,rank=len(basis_cols),ambientDimension=6,
      actualPivotInverseProductActuallyReturned=True,
      noGenericPivotDeclaredGlobalUnit=True,
      normalizedVectorProfile=vprofile(vec))
 return idx
def try_one():
 target=[C(1),C(),C(),C(),C(),C()];vec=target[:];tag={}
 for rec in basis_cols:
  cc=vec[rec['pivot']]
  if not cc:continue
  vec=[v0-cc*w0 for v0,w0 in zip(vec,rec['vector'])]
  for j,c0 in rec['tag'].items():tag[j]=tag.get(j,C())+cc*c0
 if any(vec):return None
 coef=[tag.get(j,C()) for j in range(len(raw_columns))]
 assert all(sum((coef[j]*raw_columns[j][i] for j in range(len(raw_columns))),C())==target[i] for i in range(6))
 return coef
solution=None
for name,vv in zip(names,vectors):
 add_original_column(vv,name);solution=try_one()
 if solution is not None:break
if solution is None:
 for i in [0,1,2,3]:
  if solution is not None:break
  for var in ['lambda','S']:
   vv=matvec(multiplication[var],vectors[i])
   add_original_column(vv,var+'_times_'+names[i]);solution=try_one()
   if solution is not None:break
if solution is None:
 say(stage='accurate_W_H265_original_constant_target_unreturned',
     actualRank=len(basis_cols),columns=raw_names,
     allOriginalWeightFibresRemain=True,HZeroWholeFibreRetained=True,
     noNecessaryNewFiniteCoverClaim=True,wholeWExcluded=False)
else:
 # Final original-column identity is verified above in ALL six genuine
 # weight coordinates. Intermediate Gaussian poles which have cancelled
 # do not need to be retained; H and every final coefficient pole do.
 den=one
 for cf in solution:
  assert cf.d.degrees()[2]<=0
  gg=den.gcd(cf.d);div=den/gg;assert div*gg==den;den=div*cf.d
 rest,removed=strip_paid(den)
 assert rest*removed==den
 scalar=rest.coefficient(0);rest=rest/scalar;removed*=scalar
 assert rest*removed==den
 cover=H*rest
 cert=json.dumps([dict(n=[[list(map(int,mm)),str(cc)] for mm,cc in sorted(v.n.to_dict().items())],
                       d=[[list(map(int,mm)),str(cc)] for mm,cc in sorted(v.d.to_dict().items())]) for v in solution],
                 separators=(',',':')).encode()
 say(stage='new_W_H265_open_original_constant_one_and_weight_curve_cover',
     allSixFullOriginalColumnProductsActuallyReturned=True,
     originalColumns=raw_names,actualRank=len(basis_cols),
     exactCoefficientCertificateBytes=len(cert),
     exactCoefficientCertificateSHA256=hashlib.sha256(cert).hexdigest(),
     finalParameterDenominator=prof(den),
     onlyGloballyPaidWeightsAndExplicitHRemovedFromChartDenominator=True,
     remainingChartParameterCover=prof(rest),
     completeGlobalWeightCover=prof(cover),
     exactCoverDefinition='H265 times the normalized final coefficient lcm after stripping already paid weights and H265 on its explicit complement',
     entireHZeroFibreRetainedEvenIfItCancelledFromFinalCoefficients=True,
     polynomialCoverSquarefreeNotAsserted=True,
     HNonzeroChartEntirelyExcluded=(rest.total_degree()==0),
     wholeWExcluded=False,ordinaryISPClaim=False)
say(stage='new_W_H265_original_low_value_six_coordinate_attempt_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 trueOriginalConstantOneReturned=(solution is not None),
 actualRank=len(basis_cols),originalColumns=raw_names,
 allUnpaidWeightZeroFibresRetained=True,
 noOldFifteenMinorNSNVCofactorOrResultantGateReplayed=True,
 noEncodedOrChunkedCoefficientPayloadCreated=True,
 noRegenerableMatrixOrCertificateCacheWritten=True,
 wholeWExcluded=False,ordinaryISPClaim=False,
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)
