#!/usr/bin/env python3
"""NEW actual Q-linear residue relation and SAME-lambda original ideal.

The prior same-Q ideal on each actual P201 completion block has residue
K-dimension one. This source explicitly returns its Q-qbar relation
from a 3d-by-3d UNIT MINOR OF THE ORIGINAL IDEAL MATRIX, then checks
g4(qbar) and all three original resultant values. It does not identify
a QQ linear Q factor. The full finite completed weight quotient is a
quotient of O_phi by Nakayama, and its reduction is this actual K.

Next evaluate the FOUR fixed original lambda polynomials at the same
residual Q. A finite lambda model is used only when the coefficient
of a FIXED symbolic degree 6,6,9,10 is a whole unit in this actual
weight quotient. Never lower an unproved QQ degree from a mod drop.
The chosen head has an actual residue-field inverse product; it lifts
to a unit of the complete finite weight quotient. All four original
lambda polynomials times the whole u/lambda basis form the true ideal
matrix. Rank/quotient bounds and a full original-column unit return
therefore lift by finite-module Nakayama. No h/T/v head or physical D
is inverted, no modular root is asserted to be a QQ factor.

Unreturned lambda heads or nonzero lambda quotients remain. Only all
five actual blocks closed implies whole H1 closure in the paid Phi,
physical D!=0 scope. 120s/1GiB. 2026-11-28 Asia/Taipei. Small receipts.
"""
import os,time,json,hashlib,signal,resource,contextlib,io
from pathlib import Path
from flint import fmpq,fmpq_poly,nmod_poly,nmod_mat
START=time.perf_counter();DEADLINE=START+120;PRIME=1009
signal.alarm(120);resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,separators=(",",":")),flush=True)
def read_source(name,sha,environ):
 pp=Path(os.environ.get(environ,str(Path(__file__).with_name(name))))
 raw=pp.read_bytes();assert hashlib.sha256(raw).hexdigest()==sha
 return pp,raw.decode()
def digest(obj):
 raw=json.dumps(obj,separators=(",",":")).encode()
 return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
def pdigest(poly):
 ob=digest([int(c) for c in poly.coeffs()]);ob["degree"]=int(poly.degree());return ob
def keep_deadline():
 signal.setitimer(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
ip,isrc=read_source(
 "2026-11-28-unit211-Phi-zero-H1-P201-five-whole-Q-original-resultant-ideals-8542.py",
 "8a9a18855a2c3c63c484192c5054f5cee0aed80e547267e5885c9fd389c1e470",
 "ISP_H1_P201_SAME_Q_IDEAL_SOURCE")
cut="\ndef test_whole_weight_ideal(phi):"
assert isrc.count(cut)==1
prefix=isrc.split(cut,1)[0]
old="original_resultants=[];Gbar=None"
assert prefix.count(old)==1
prefix=prefix.replace(old,old+";retained_original_lambda={}")
old="assert names[-1]==label and [f.degree() for f in inputs]==degrees"
assert prefix.count(old)==1
prefix=prefix.replace(old,old+"""
 for source_name,source_polynomial in zip(names,inputs):
  retained_original_lambda[source_name]=source_polynomial""")
ienv={"__file__":str(ip),"__name__":"__same_Q_inputs_for_new_Q_relation_and_lambda_ideal__"}
with contextlib.redirect_stdout(io.StringIO()):
 exec(compile(prefix,str(ip)+":necessary-original-elements-and-coefficients","exec"),ienv)
keep_deadline()
Pbar,Gbar=ienv["Pbar"],ienv["Gbar"]
factors=ienv["factors"];original_resultants=ienv["original_resultants"]
venv=ienv["venv"];mp=ienv["mp"]
polynomials=ienv["retained_original_lambda"]
labels=["RWN_O_scaled_T_v","RWN_O_scaled_T_commutator",
        "RWN_O_scaled_T_complete_F6","RWN_O_scaled_T_complete_NV"]
degrees=[6,6,9,10]
assert set(polynomials)==set(labels)
assert [polynomials[label].degree() for label in labels]==degrees
# Read an already-constructed original polynomial head from the suspended
# generator, not a new head or norm calculation. This is diagnostic only.
frame=ienv["generator"].gi_frame
assert frame is not None
original_head=frame.f_locals["head"]
assert original_head.d==venv["one"]
say("new_P201_same_Q_same_lambda_original_input",
 exactP201Reduction=pdigest(Pbar),actualRemainingBase=pdigest(Gbar),
 actualRemainingBlockDegrees=sorted(phi.degree() for phi,e in factors),
 originalLambdaLabels=labels,fixedSymbolicLambdaDegrees=degrees,
 QRelationSource="original three-resultant ideal, nonconstant Q rows",
 oldSameQStandaloneRankDriverReplayed=False,
 oldQQDixonGaussianReplayed=False,oldNormBezoutProofReplayed=False,
 noQQLinearQFactorAssumed=True,noValueOrGeometricHeadInverted=True)

def test_block(phi):
 d=int(phi.degree());p=PRIME
 zero=nmod_poly([],p);one=nmod_poly([1],p);u=nmod_poly([0,1],p)
 counts={"fieldReductionProducts":0,"fieldInverseProducts":0,
         "QReductionProducts":0,"lambdaDivisionProducts":0}
 def kr(a):
  q,r=divmod(a,phi);assert q*phi+r==a
  counts["fieldReductionProducts"]+=1
  return r
 def kmul(a,b):return kr(a*b)
 def kinv(a,label):
  assert a,label
  gg,s,t=a.xgcd(phi);assert a*s+phi*t==gg and gg.degree()==0
  result=kr(s*pow(int(gg[0]),-1,p));assert kmul(a,result)==one
  counts["fieldInverseProducts"]+=1
  return result
 qcoeff=[kr(mp(c)) for c in venv["g"]]
 assert qcoeff[-1]==one
 def qr(cc):
  cc=[kr(c) for c in cc]
  while len(cc)<4:cc.append(zero)
  original=cc[:];quot=[zero for _ in range(max(0,len(cc)-4))]
  for j in range(len(cc)-1,3,-1):
   lead=cc[j];quot[j-4]=lead
   for k in range(4):cc[j-4+k]=kr(cc[j-4+k]-lead*qcoeff[k])
   cc[j]=zero
  back=cc[:]
  for j,lead in enumerate(quot):
   for k in range(5):back[j+k]=kr(back[j+k]+lead*qcoeff[k])
  assert back==original
  counts["QReductionProducts"]+=1
  return cc[:4]
 def evaluateQ(coords,q):
  ans=zero
  for c in reversed(coords):ans=kr(ans*q+kr(c))
  return ans
 def flat(v):
  return [int(c[a]) for c in v for a in range(d)]
 columns=[];column_tags=[]
 for name,coords in original_resultants:
  qpower=qr(coords)
  for b in range(4):
   upower=qpower[:]
   for a in range(d):
    columns.append(flat(upower))
    column_tags.append(dict(original=name,uPower=a,QPower=b))
    upower=[kr(u*c) for c in upower]
   qpower=qr([zero]+qpower)
 # The previous result gave the full ideal rank 3d and quotient K.
 # Here return a NEW explicit 3d unit minor and all original relations.
 dim=4*d;nonconstant_dim=3*d
 lower=nmod_mat([[columns[j][i] for j in range(len(columns))]
                for i in range(d,dim)],p)
 rr,rank=lower.rref();assert int(rank)==nonconstant_dim
 pivots=[]
 for i in range(nonconstant_dim):
  j=next(j for j in range(len(columns)) if int(rr[i,j])!=0)
  assert int(rr[i,j])==1;pivots.append(j)
 assert len(set(pivots))==nonconstant_dim
 square=nmod_mat([[columns[j][i] for j in pivots] for i in range(d,dim)],p)
 inv=square.inv()
 eye=nmod_mat(nonconstant_dim,nonconstant_dim,
      [1 if i==j else 0 for i in range(nonconstant_dim) for j in range(nonconstant_dim)],p)
 assert square*inv==eye
 full=nmod_mat([[columns[j][i] for j in pivots] for i in range(dim)],p)
 relation=full*inv
 assert all(int(relation[d+i,j])==(1 if i==j else 0)
            for i in range(nonconstant_dim) for j in range(nonconstant_dim))
 qbar=kr(nmod_poly([(-int(relation[a,0]))%p for a in range(d)],p))
 q_powers=[one,qbar,kmul(qbar,qbar)]
 q_powers.append(kmul(q_powers[-1],qbar))
 for b in range(1,4):
  for a in range(d):
   j=(b-1)*d+a
   top=nmod_poly([int(relation[i,j]) for i in range(d)],p)
   assert kr(top+q_powers[b]*(u**a))==zero
 assert evaluateQ(qcoeff,qbar)==zero
 for name,coords in original_resultants:
  assert evaluateQ([kr(c) for c in coords],qbar)==zero
 derivative=evaluateQ([qcoeff[j]*j for j in range(1,5)],qbar)
 if derivative:assert kmul(derivative,kinv(derivative,"actual original Q4 derivative"))==one
 hvalue=evaluateQ([kr(mp(c)) for c in original_head.n],qbar)
 block_id=pdigest(phi)
 q_return=dict(actualP201Block=block_id,sourceIdealRank=3*d,
  nonconstantQUnitMinorOrder=3*d,
  selectedOriginalProductColumns=[column_tags[j] for j in pivots],
  selectedMinorIdentity=digest([[int(square[i,j]) for j in range(3*d)] for i in range(3*d)]),
  selectedMinorTimesInverseReturned=True,
  allThreeQPowerFamiliesReturnedAsActualOriginalCombinations=True,
  exactResidualQValue=pdigest(qbar),
  originalQ4AndAllThreeResultantsReturnedAtSameQ=True,
  originalQ4Derivative=pdigest(derivative),
  originalQ4DerivativeResidueUnit=bool(derivative),
  diagnosticOriginalQuadraticHeadZero=(not hvalue),
  diagnosticOriginalQuadraticHead=pdigest(hvalue),
  actualCompleteWeightQuotientIsQuotientOfOphi=True,
  noQQLinearQFactorIdentification=True)
 say("new_P201_actual_original_Q_linear_relation",**q_return)

 values=[];profiles=[]
 for label,symbolic_degree in zip(labels,degrees):
  original=polynomials[label]
  assert original.degree()==symbolic_degree and all(c.d==venv["one"] for c in original.c)
  coefficients=[evaluateQ([kr(mp(c)) for c in co.n],qbar) for co in original.c]
  while coefficients and not coefficients[-1]:coefficients.pop()
  actual_degree=len(coefficients)-1
  values.append(coefficients)
  head=(coefficients[symbolic_degree] if actual_degree==symbolic_degree else zero)
  profiles.append(dict(original=label,fixedSymbolicLambdaDegree=symbolic_degree,
    actualResidualLambdaDegree=actual_degree,
    fixedTopCoefficient=pdigest(head),fixedTopIsResidueUnit=bool(head),
    completeResidualCoefficientIdentity=digest([[int(c) for c in a.coeffs()] for a in coefficients])))
 eligible=next((j for j,info in enumerate(profiles) if info["fixedTopIsResidueUnit"]),None)
 if eligible is None:
  say("accurate_P201_same_lambda_model_retained_without_unit_head",
   actualP201Block=block_id,allFourOriginalProfiles=profiles,
   noReducedDegreePromotedToCharacteristicZero=True,
   noOriginalValueOrHeadInverted=True,wholeBlockRetained=True)
  return dict(block=block_id,weightRelation=q_return,lambdaEligible=False,
   excluded=False,profiles=profiles,remainingWeightUpperBound=d,
   remainingWeightLambdaUpperBound=6*d,arithmeticCounts=counts)
 m=degrees[eligible];head=values[eligible][m]
 inverse_head=kinv(head,"fixed original lambda head")
 F=[kmul(c,inverse_head) for c in values[eligible]]
 assert len(F)==m+1 and F[-1]==one
 assert [kmul(c,head) for c in F]==values[eligible]
 def trim(a):
  a=list(a)
  while a and not a[-1]:a.pop()
  return a
 def multiply_lambda(a,b):
  if not a or not b:return []
  out=[zero for _ in range(len(a)+len(b)-1)]
  for i,x in enumerate(a):
   for j,y in enumerate(b):
    if x and y:out[i+j]=kr(out[i+j]+x*y)
  return trim(out)
 def remainder(a):
  a=trim(a);original=a[:]
  quotient=[zero for _ in range(max(0,len(a)-m))]
  for j in range(len(a)-1,m-1,-1):
   co=a[j];quotient[j-m]=co
   for k in range(m):a[j-m+k]=kr(a[j-m+k]-co*F[k])
   a[j]=zero
  rem=trim(a[:m]);back=multiply_lambda(trim(quotient),F)
  while len(back)<len(rem):back.append(zero)
  for j,c in enumerate(rem):back[j]=kr(back[j]+c)
  assert trim(back)==original
  counts["lambdaDivisionProducts"]+=1
  return rem+[zero for _ in range(m-len(rem))]
 D=m*d;lambda_columns=[];lambda_tags=[]
 for label,poly in zip(labels,values):
  for j in range(m):
   reduced=remainder([zero]*j+poly)
   for a in range(d):
    col=[kmul(c,u**a) for c in reduced]
    lambda_columns.append(flat(col))
    lambda_tags.append(dict(original=label,lambdaPower=j,uPower=a))
 assert all(len(c)==D for c in lambda_columns)
 matrix=nmod_mat([[lambda_columns[j][i] for j in range(len(lambda_columns))] for i in range(D)],p)
 rr,rank=matrix.rref();rank=int(rank);assert rank%d==0
 quotient_dimension=D-rank
 detail={}
 if rank==D:
  pivots=[]
  for i in range(D):
   j=next(j for j in range(len(lambda_columns)) if int(rr[i,j])!=0)
   assert int(rr[i,j])==1;pivots.append(j)
  selected=nmod_mat([[lambda_columns[j][i] for j in pivots] for i in range(D)],p)
  inverse=selected.inv()
  eye=nmod_mat(D,D,[1 if i==j else 0 for i in range(D) for j in range(D)],p)
  assert selected*inverse==eye
  unit_coefficients=[int(inverse[j,0]) for j in range(D)]
  assert all(sum(lambda_columns[pivots[j]][i]*unit_coefficients[j] for j in range(D))%p
             ==(1 if i==0 else 0) for i in range(D))
  detail=dict(selectedOriginalProducts=[lambda_tags[j] for j in pivots],
   selectedMatrixIdentity=digest([[int(selected[i,j]) for j in range(D)] for i in range(D)]),
   originalUnitCoefficientIdentity=digest(unit_coefficients),
   selectedMatrixTimesInverseReturned=True,
   originalConstantOneCombinationReturned=True)
 closed=(rank==D)
 result=dict(block=block_id,lambdaEligible=True,excluded=closed,
  fixedOriginalMonicGenerator=labels[eligible],
  fixedOriginalLambdaDegree=m,
  fixedHeadInverseProductReturned=True,
  actualCompleteFiniteLambdaRank=D,
  actualFourOriginalIdealRank=rank,
  actualResidualWeightLambdaQuotientDimension=quotient_dimension,
  characteristicZeroWeightLambdaDimensionUpperBound=quotient_dimension,
  remainingWeightUpperBound=(0 if closed else d),
  remainingWeightLambdaUpperBound=min(6*d,quotient_dimension),
  profiles=profiles,arithmeticCounts=counts,**detail)
 say("new_P201_actual_same_Q_same_lambda_original_ideal",**result)
 return result
results=[]
for phi,e in sorted(factors,key=lambda x:(x[0].degree(),tuple(int(c) for c in x[0].coeffs()))):
 assert int(e)==1
 results.append(test_block(phi))
weight_bound=sum(r["remainingWeightUpperBound"] for r in results)
lambda_bound=sum(r["remainingWeightLambdaUpperBound"] for r in results)
closed=all(r["excluded"] for r in results)
say("new_P201_Q_relation_same_lambda_input_finished",
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 actualBlockReturns=results,
 characteristicZeroDistinctWeightPairUpperBound=weight_bound,
 characteristicZeroDistinctWeightLambdaUpperBound=lambda_bound,
 characteristicZeroDistinctFiveCoordinatePointUpperBound=3*lambda_bound,
 characteristicZeroDistinctFullNormalizedPointUpperBound=6*lambda_bound,
 wholeOriginalH1PhiDnonzeroGraphExcluded=closed,
 noUnpaidLambdaDegreeDrop=True,
 noQQLinearQOrModularFactorIdentification=True,
 originalGeometricPointBoundThreeUsedOnlyOnAlreadyPaidActualQQScope=True,
 everyNonunitHeadAndUnclosedBlockRetained=True,
 noHOrPhysicalDInverseUsed=True,
 coefficientPayloadTransmitted=False,encodedOrSplitPayloadCreated=False,
 ordinaryISPClaim=False,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)
