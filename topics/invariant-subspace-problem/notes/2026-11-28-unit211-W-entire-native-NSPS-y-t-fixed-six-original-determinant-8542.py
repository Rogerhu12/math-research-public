#!/usr/bin/env python3
"""Entire current W chart: NEW original native-coordinate NS/PS fixed minor.
The formerly explicit (k+2)*J19*C9 chart is now paid by THREE whole original
theorems. Use the actual basis (1,x,y,t,y^2,y*t), with no H265 inverse.
The new fixed six rows are NS,PS,y*NS,t*NS,y*PS,t*PS. They are not the old
lambda/S determinant and no old commutator/Gaussian tail is executed.
180 seconds / 4 GiB. Only source, parameter definitions and small receipts;
no encoded/chunked coefficients, matrix cache or certificate artifact.
"""
import json,time,hashlib,io,contextlib,signal,resource
from pathlib import Path
start=time.perf_counter()
signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**r):
 r['seconds']=time.perf_counter()-start
 print(json.dumps(r,separators=(',',':')),flush=True)
def digest(obj):
 raw=json.dumps(obj,separators=(',',':')).encode()
 return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
here=Path(__file__).resolve().parent
dep=here/'2026-11-27-unit211-generic-LS-W-C9-six-generator-original-parameter-cofactors-8542.py'
raw=dep.read_text()
assert hashlib.sha256(raw.encode()).hexdigest()=='10720660772a9a1252b905b1227b697e038d1b974b7e96ec30e485477b21d3f1'
marker='\ndef multiply_matrix(MM,NN):'
assert raw.count(marker)==1
prefix=raw.split(marker)[0]
assert hashlib.sha256(prefix.encode()).hexdigest()=='c09268d1b0d4b21f565600b8d51fa13e493dd1aeb6628d5b0acceb9d1a6ffd22'
ns={'__file__':str(dep),'__name__':'frozen_C9_necessary_construction'}
with contextlib.redirect_stdout(io.StringIO()):
 exec(compile(prefix,str(dep),'exec'),ns)
signal.alarm(max(1,180-int(time.perf_counter()-start)))
R=ns['R'];ctx=ns['ctx'];ep=ns['ep'];kp=ns['kp'];zero=ns['zz'];one=ns['oo']
basis=ns['basis'];variables=ns['variables'];original=ns['original']
matrices=ns['matrices'];errors=ns['errors']
strip=ns['strip_known'];coeffmap=ns['coeffmap'];verify=ns['verify_trace']
assert ns['freemons']==[(0,0,0),(1,0,0),(0,1,0),(0,0,1),(0,2,0),(0,1,1)]
assert len(original)==6 and len(matrices)==3 and all(len(m)==6 for m in matrices)
# The whole J19 theorem is independent of C9 and D27:
# R150-appendix-unit211-W-J19-entire-original-weight-curve-exclusion.md
# The independent entire C9 theorem is:
# R150-appendix-essential-four-unit-two-plus-one-plus-one-generic-LS-W-C9-complete-original-exclusion.md
# k+2 is paid by the whole equal-weights theorem on this W chart:
# R150-appendix-unit211-equal-weights-complete-original-exclusion.md
J19=(16*ep**4*kp**3-8*ep**3*kp**4-16*ep**3*kp**3-96*ep**3*kp**2
 -ep**2*kp**5-8*ep**2*kp**4+24*ep**2*kp**3+64*ep**2*kp**2+192*ep**2*kp
 -2*ep*kp**5-14*ep*kp**4-12*ep*kp**3-128*ep
 -kp**5-10*kp**4-40*kp**3-104*kp**2-160*kp-128)
C9=ns['C9']
paid_atoms=ns['base_units']+[
 ('whole_equal_weights_k_plus_two',kp+2),
 ('whole_original_J19',J19),('whole_original_C9',C9)]
def paid_poly(p):
 assert p
 rest,removed,hist=strip(p,paid_atoms)
 assert rest*removed==p and rest.total_degree()==0
 return hist
def paid_scalar(c):
 c=R(c)
 assert all(all(mm[j]==0 for j in range(2,8)) for mm in c.n.to_dict())
 assert all(all(mm[j]==0 for j in range(2,8)) for mm in c.d.to_dict())
 paid_poly(c.d)
 return c
def poly_profile(p):
 dd=p.to_dict()
 assert all(all(mm[j]==0 for j in range(2,8)) for mm in dd)
 return dict(degrees=list(map(int,p.degrees()[:2])),
  totalDegree=int(p.total_degree()),terms=len(dd),
  **digest([[int(mm[0]),int(mm[1]),str(cc)] for mm,cc in sorted(dd.items())]))
def rational_profile(c):
 c=R(c);return dict(numerator=poly_profile(c.n),denominator=poly_profile(c.d))
def rows_digest(rows):
 entries=[]
 def enc(p):
  return [[[int(v) for v in mm],str(cc)] for mm,cc in sorted(p.to_dict().items())]
 for row in rows:
  for c in row:
   c=R(c);entries.append([enc(c.n),enc(c.d)])
 return digest(entries)
# Pay the ACTUAL two selected determinants, not an old explicit-chart label.
d2_paid=paid_poly(ns['delta2'])
d3_num_paid=paid_poly(ns['delta3'].n)
d3_den_paid=paid_poly(ns['delta3'].d)
for rule,tag in zip(ns['q'],ns['tags']):
 verify(rule,tag)
 for c in coeffmap(rule).values():paid_scalar(c)
 for c in tag:
  # Tags can involve geometry, but their denominator must be a weight unit.
  paid_poly(c.d)
for axis in range(3):
 for i in range(6):
  assert variables[axis]*basis[i]==sum((matrices[axis][i][j]*basis[j] for j in range(6)),R())+sum((errors[axis][i][g]*original[g] for g in range(6)),R())
  for c in matrices[axis][i]:paid_scalar(c)
  for c in errors[axis][i]:paid_poly(c.d)
say(stage='new_entire_W_original_native_six_rule_interface',
 oldSourceSHA256=hashlib.sha256(raw.encode()).hexdigest(),
 executedNecessaryPrefixSHA256=hashlib.sha256(prefix.encode()).hexdigest(),
 oldCommGaussianAndParameterCofactorTailExecuted=False,
 actualQuadraticHeadPayment=d2_paid,
 actualCubicNumeratorPayment=d3_num_paid,actualCubicDenominatorPayment=d3_den_paid,
 sixCompleteOriginalRuleProductsReturned=True,
 eighteenCompleteOriginalMultiplicationProductsReturned=True,
 allDenominatorsPaidOnEntireCurrentW=True,
 H265NotInverted=True,wholeH265ZeroCurveIncluded=True,
 basis='1,x,y,t,y^2,y*t',matrixOrientation='M_axis*v=axis*v modulo original equations',
 sixGeneratorFreenessNotAssumed=True,ordinaryISPClaim=False)
# The full frozen prefix already returned these original weighted cubics.
base_rows=[row[:] for row in ns['necessary']]
base_tags=[row[:] for row in ns['necessary_tags']]
assert ns['necessary_labels']==['NS','PS'] and len(base_rows)==2
row_specs=[(None,0,'NS'),(None,1,'PS'),
 (1,0,'y*NS'),(2,0,'t*NS'),(1,1,'y*PS'),(2,1,'t*PS')]
rawrows=[];rawtags=[];labels=[]
for axis,which,label in row_specs:
 row=base_rows[which];tag=base_tags[which]
 if axis is not None:
  nr=[sum((row[i]*matrices[axis][i][j] for i in range(6)),R()) for j in range(6)]
  nt=[variables[axis]*tag[g]-sum((row[i]*errors[axis][i][g] for i in range(6)),R()) for g in range(6)]
  row,tag=nr,nt
 verify(sum((row[i]*basis[i] for i in range(6)),R()),tag)
 for c in row:paid_scalar(c)
 for c in tag:paid_poly(c.d)
 rawrows.append(row);rawtags.append(tag);labels.append(label)
 say(stage='new_entire_W_native_original_value_row_return',
  label=label,fullOriginalSixMultiplierProductReturned=True,
  maximumNumeratorDegrees=[max(int(c.n.degrees()[j]) for c in row) for j in range(2)],
  totalNumeratorTerms=sum(len(c.n.to_dict()) for c in row),
  completeRowDefinition=rows_digest([row]),
  noNewGeometryOrWeightUnitAssumed=True,wholeH265ZeroCurveIncluded=True)
def clear_original_row(row,tag,label):
 if not any(row):
  verify(R(),tag)
  return [zero]*6,tag[:]
 den=one
 for c in row:
  g=den.gcd(c.d);a=den/g
  assert a*g==den
  den=a*c.d
 paid_poly(den)
 nums=[]
 for c in row:
  dd=den/c.d;assert dd*c.d==den
  nums.append(c.n*dd)
 common=next(p for p in nums if p)
 for p in nums:
  if p:common=common.gcd(p)
 rest,removed,hist=strip(common,paid_atoms)
 assert rest*removed==common
 paid_poly(removed)
 answer=[]
 for c,p in zip(row,nums):
  v=p/removed;assert v*removed==p
  assert R(v)==R(den,removed)*c
  answer.append(v)
 trace=[R(den,removed)*v for v in tag]
 verify(sum((R(answer[i])*basis[i] for i in range(6)),R()),trace)
 say(stage='new_entire_W_native_row_paid_polynomial_normalization',
  label=label,allSixScalarProductsAndFullOriginalTraceReturned=True,
  maximumDegrees=[max(int(p.degrees()[j]) for p in answer) for j in range(2)],
  totalTerms=sum(len(p.to_dict()) for p in answer),
  denominator=poly_profile(den),paidContent=poly_profile(removed),
  remainingUnpaidCommonFactorRetained=True,paidRemoved=hist)
 return answer,trace
rows=[];traces=[]
for row,tag,label in zip(rawrows,rawtags,labels):
 rr,tt=clear_original_row(row,tag,label);rows.append(rr);traces.append(tt)
say(stage='new_entire_W_native_NSPS_fixed_six_order_original_input',
 rowDefinitions=labels,matrixDefinition=rows_digest(rows),
 exactValueColumn='v=(1,x,y,t,y^2,y*t)^t',
 actualIdentity='M*v=0 at every original point and v[0]=1',
 allSixOriginalRowProductsReturned=True,
 noFreeAlgebraOrCommutativityAssumption=True,
 allCurrentWIncludingH265ZeroCovered=True,
 noOriginalWPointExcludedYet=True)
# A NEW fixed native-coordinate determinant, not a resumption or reordering
# of the failed lambda/S matrix or the old C9 adaptive parameter cofactor.
mm=[row[:] for row in rows];previous=one;sign=1;det=None;divisions=0
for j in range(5):
 if not mm[j][j]:
  sw=next((i for i in range(j+1,6) if mm[i][j]),None)
  if sw is None:
   det=zero;break
  mm[j],mm[sw]=mm[sw],mm[j];sign=-sign
 pivot=mm[j][j]
 for i in range(j+1,6):
  for h in range(j+1,6):
   numerator=mm[i][h]*pivot-mm[i][j]*mm[j][h]
   value=numerator/previous
   assert value*previous==numerator
   mm[i][h]=value;divisions+=1
  mm[i][j]=zero
 previous=pivot
 say(stage='new_native_fixed_determinant_exact_polynomial_step',
  step=j,actualDivisionProducts=divisions,
  trailingMaximumDegrees=[max(int(mm[i][h].degrees()[a]) for i in range(j+1,6) for h in range(j+1,6)) for a in range(2)],
  trailingTotalTerms=sum(len(mm[i][h].to_dict()) for i in range(j+1,6) for h in range(j+1,6)),
  parameterPivotZeroFibresNotDeleted=True)
if det is None:det=sign*mm[5][5]
if det:
 rest,removed,hist=strip(det,paid_atoms)
 assert rest*removed==det
 scalar=rest.coefficient(0);assert scalar
 rest=rest/scalar;removed*=scalar
 assert rest*removed==det
 say(stage='new_entire_W_native_original_NSPS_weight_necessary_polynomial',
  fullDeterminant=poly_profile(det),necessaryRemainingWeightPolynomial=poly_profile(rest),
  exactParameterDefinition='paid primitive fixed determinant of NS,PS,yNS,tNS,yPS,tPS in the frozen C9 original basis',
  allPaidStrippingProductsReturned=True,paidRemoved=hist,
  allCurrentWIncludingH265ZeroCovered=True,
  instantaneousPivotZeroFibresRetainedByPolynomialIdentity=True,
  wholeCurrentWExcluded=(rest.total_degree()==0),
  noSquarefreeOrRadicalClaim=True,ordinaryISPClaim=False)
else:
 say(stage='accurate_new_native_original_fixed_determinant_zero',
  noNecessaryWeightCurveObtained=True,allOriginalRowIdentitiesPreserved=True,
  wholeCurrentWExcluded=False)
say(stage='new_entire_W_native_original_NSPS_fixed_input_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 actualDeterminantReturned=True,determinantNonzero=bool(det),
 actualExactDivisionProducts=divisions,
 noOldFrozenFailedGateReplayed=True,
 noEncodedOrChunkedDataOrRecomputableMatrixCacheWritten=True,
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 ordinaryISPClaim=False)
signal.alarm(0)
