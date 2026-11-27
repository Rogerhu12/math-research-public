#!/usr/bin/env python3
"""NEW same-Q original resultant ideal on all five remaining P201 blocks.

Paid base: monic P201 in Z_(1009)[u], squarefree degree-201 reduction;
the complete original norm return retains exactly five P201 Hensel
blocks of residue degrees 1,1,3,4,5. Here we keep the FULL Q4 algebra
on each block and test the three original fixed lambda RESULTANTS
before taking any Q norm. This is a genuinely new same-Q condition.

Each original resultant is an integral element of the finite free
rank-4d completed weight algebra. Its multiples by ALL u^a Q^b form
the exact ideal multiplication matrix. Full rank and the selected
matrix times inverse=I close the WHOLE block. Otherwise its true
residue quotient dimension 4d-rank bounds the generic weight algebra
dimension above, so the sum bounds remaining distinct weight pairs.
Multiply this weight bound by the paid same-point 18 and 36 only.
No h, lambda head, physical D, or geometric/value norm is inverted.

Only necessary coefficients are reconstructed; old QQ Dixon Gaussian,
old norm Bezout, assignment/infinity gates, and old 85/122 prototype
are not executed. The F6 norm alone is reconstructed as the exact
definition of the already-paid G14 base; other two norms are not taken.
No coefficient payload or recomputable data artifact is emitted.
120s / 1GiB. 2026-11-28 Asia/Taipei.
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
pp,ps=read_source(
 "2026-11-28-unit211-Phi-zero-H1-P201-modular-pole-support-degree-saturation-8542.py",
 "6a2dc6a4b2434c60d8d3c6532bda0c4b23524583665ac7b558e00a7db48b42f3",
 "ISP_H1_P201_REDUCTION_SOURCE")
end="\ntry:\n completed=main()";cut="\n unit,factors=den.factor()"
assert ps.count(end)==ps.count(cut)==1
necessary=ps.split(end,1)[0].split(cut,1)[0]+"""
 assert den.degree()==356 and den.degree()<p
 rad=mmonic(mexact(den,den.gcd(den.derivative())))
 known=mp([0,1])*mp([-1,1])*Cbar
 support=mmonic(mexact(rad,rad.gcd(known)))
 assert support.degree()==201 and support.gcd(known).degree()==0
 assert support.gcd(support.derivative()).degree()==0
 return support
"""
penv={"__file__":str(pp),"__name__":"__P201_base_for_new_same_Q_ideal__"}
with contextlib.redirect_stdout(io.StringIO()):
 exec(compile(necessary,str(pp)+":necessary-P201-coefficients","exec"),penv)
 Pbar=penv["main"]()
keep_deadline()
assert pdigest(Pbar)==dict(degree=201,bytes=789,
 sha256="013656af6b2c65fe4d306c891b50aca9612b13ed9ae46c7e61d2e50b228dd029")
vp,vs=read_source(
 "2026-11-28-unit211-Phi-zero-H1-polynomial-v-source-scaled-matrices-fixed-norm-input-8542.py",
 "5f6ba628dd4a660a7cedc7bb338a7cebc9cdc1ac3b6d6958a36409cb578b00ef",
 "ISP_H1_POLYNOMIAL_V_SOURCE")
tail="\nall_projections=[];all_names=[];all_modular_returns=[];common=None"
assert vs.count(tail)==1
defs=vs.split(tail,1)[0]
old="headNorm= pdigest(polynomial_norm(head)),"
assert defs.count(old)==1
defs=defs.replace(old,"headNormPreviouslyPublished=True,")
venv={"__file__":str(vp),"__name__":"__three_original_resultant_elements_for_new_weight_ideal__"}
with contextlib.redirect_stdout(io.StringIO()):
 exec(compile(defs,str(vp)+":necessary-original-polynomials","exec"),venv)
keep_deadline()
fh="\ndef modular_fixed_original_returns(projections,names):\n"
body=vs.split(fh,1)[1].split("\n converted=[]",1)[0]
body="\n".join(line[1:] if line.startswith(" ") else line for line in body.splitlines())
menv=dict(venv)
exec(compile(body,str(vp)+":coefficient-arithmetic-only","exec"),menv)
MA,MU,mp=menv["MA"],menv["MU"],menv["mp"]
expected=[
 ("RWN_O_scaled_T_commutator",[6,6],12),
 ("RWN_O_scaled_T_complete_F6",[6,9],15),
 ("RWN_O_scaled_T_complete_NV",[6,10],16)]
generator=venv["whole_polynomial_module"]()
original_resultants=[];Gbar=None
for index,(label,degrees,size) in enumerate(expected):
 with contextlib.redirect_stdout(io.StringIO()):
  inputs,names=next(generator)
 assert names[-1]==label and [f.degree() for f in inputs]==degrees
 converted=[]
 for ff in inputs:
  assert all(a.d==venv["one"] for a in ff.c)
  converted.append(MU([MA([mp(c) for c in a.n]) for a in ff.c]))
 assert [f.degree() for f in converted]==degrees
 with contextlib.redirect_stdout(io.StringIO()):
  result,steps=menv["fixed_resultant"](converted[0],converted[1],
       "new whole-Q original ideal "+label)
 assert result.d==menv["mo"]
 original_resultants.append((label,[c for c in result.n]))
 say("new_P201_fixed_original_resultant_element",
  label=label,fixedSymbolicLambdaDegrees=degrees,
  originalSylvesterOrderOverWholeQAlgebra=size,
  originalWholeQCoordinateCount=4,
  originalCoordinates=[pdigest(c) for c in result.n],
  finalCommonParameterDenominatorIsOne=True,
  allFixedLambdaLeadingDegreesKept=True,
  allEuclideanDivisionsMultipliedBack=True,
  completeOriginalPolynomialIdentityExtendsAcrossTemporaryPivots=True,
  originalParameterLambdaLeadingZeroFibresRetained=True,
  newTargetUsesElementBeforeItsNorm=True)
 if index==1:
  # Necessary regeneration of the known G14 base only. Do NOT call
  # the old three-norm Bezout driver or compute the other two norms.
  nf=menv["mdet"](result.regular_numerator())
  assert pdigest(nf)==dict(degree=5131,bytes=18348,
   sha256="4851fda73cad1c4ab0f037677b0a1881dc5000ce0765960e3785acbf63bd6959")
  Gbar=Pbar.gcd(nf)
  assert pdigest(Gbar)==dict(degree=14,bytes=58,
   sha256="73fb15af460042bc0f146122553e10262c97bbf75dec28aaaa471b88ee4a411d")
assert Gbar is not None
quot,rem=divmod(Pbar,Gbar);assert quot*Gbar+rem==Pbar and not rem
assert Gbar.gcd(quot).degree()==0
unit,factors=Gbar.factor();product=nmod_poly([int(unit)],PRIME)
for phi,e in factors:assert int(e)==1;product=product*phi
assert product==Gbar and sorted(phi.degree() for phi,e in factors)==[1,1,3,4,5]
say("new_P201_same_Q_complete_original_ideal_input",
 actualIntegralP201Reduction=pdigest(Pbar),
 actualRemainingP201CompletedBase=pdigest(Gbar),
 allFiveActualBlockFactorsMultipliedBack=True,
 residueBlockDegrees=[1,1,3,4,5],
 originalGenerators=[name for name,co in original_resultants],
 noHOrLambdaHeadUnitNeeded=True,noGeometricOrPhysicalDInverse=True,
 noOriginalQRootOrNilpotentComponentDropped=True,
 otherEightP201BlocksAlreadyExcludedByPublishedOriginalNorms=True,
 oldNormBezoutProofReplayed=False)

def test_whole_weight_ideal(phi):
 d=int(phi.degree());dim=4*d
 z=nmod_poly([],PRIME);one=nmod_poly([1],PRIME);u=nmod_poly([0,1],PRIME)
 counts={"uReductionProducts":0,"QReductionProducts":0}
 def ur(poly):
  q,r=divmod(poly,phi);assert q*phi+r==poly
  counts["uReductionProducts"]+=1
  return r
 qcoeff=[ur(mp(c)) for c in venv["g"]]
 assert len(qcoeff)==5 and qcoeff[-1]==one
 def qr(cc):
  cc=[ur(c) for c in cc]
  while len(cc)<4:cc.append(z)
  original=cc[:];quotient=[z for _ in range(max(0,len(cc)-4))]
  for j in range(len(cc)-1,3,-1):
   lead=cc[j];quotient[j-4]=lead
   for k in range(4):cc[j-4+k]=ur(cc[j-4+k]-lead*qcoeff[k])
   cc[j]=z
  back=cc[:]
  for j,lead in enumerate(quotient):
   for k in range(5):back[j+k]=ur(back[j+k]+lead*qcoeff[k])
  assert back==original
  counts["QReductionProducts"]+=1
  return cc[:4]
 def flat(v):
  return [int(c[a]) for c in v for a in range(d)]
 columns=[];tags=[]
 for label,coords in original_resultants:
  qpower=qr(coords)
  for b in range(4):
   upower=qpower[:]
   for a in range(d):
    columns.append(flat(upower));tags.append(dict(original=label,uPower=a,QPower=b))
    upower=[ur(u*c) for c in upower]
   qpower=qr([z]+qpower)
 assert len(columns)==3*dim and all(len(c)==dim for c in columns)
 matrix=nmod_mat([[columns[j][i] for j in range(len(columns))] for i in range(dim)],PRIME)
 rr,rank=matrix.rref();rank=int(rank)
 pivots=[]
 for i in range(rank):
  j=next(j for j in range(len(columns)) if int(rr[i,j])!=0)
  assert int(rr[i,j])==1;pivots.append(j)
 assert len(set(pivots))==rank
 assert rank%d==0
 closed=(rank==dim)
 detail={}
 if closed:
  selected=nmod_mat([[columns[j][i] for j in pivots] for i in range(dim)],PRIME)
  inverse=selected.inv()
  identity=nmod_mat(dim,dim,[1 if i==j else 0 for i in range(dim) for j in range(dim)],PRIME)
  assert selected*inverse==identity
  unit_weights=[int(inverse[j,0]) for j in range(dim)]
  assert all(sum(columns[pivots[j]][i]*unit_weights[j] for j in range(dim))%PRIME
             ==(1 if i==0 else 0) for i in range(dim))
  detail=dict(selectedOriginalProducts=[tags[j] for j in pivots],
   selectedMatrixIdentity=digest([[int(selected[i,j]) for j in range(dim)] for i in range(dim)]),
   unitCoefficientIdentity=digest(unit_weights),
   selectedMatrixTimesInverseReturned=True,
   originalConstantOneCombinationMultipliedBack=True)
 info=dict(actualP201ModularBlock=pdigest(phi),P201BlockMultiplicity=1,
   residueBaseDegree=d,completeWeightAlgebraRank=dim,
   actualWholeOriginalIdealRank=rank,actualResidueWeightQuotientDimension=dim-rank,
   characteristicZeroWeightQuotientDimensionUpperBound=dim-rank,
   wholeOriginalBlockExcluded=closed,
   fullThreeOriginalElementsAndAllWeightBasisProducts=True,
   idealMatrixShape=[dim,3*dim],
   noQRootOrNilpotentDiscarded=True,
   noHOrLambdaHeadUnitUsed=True,noDOrValueSaturation=True,
   arithmeticCounts=counts,**detail)
 say("new_P201_same_Q_actual_original_ideal_block",**info)
 return info
results=[]
for phi,e in sorted(factors,key=lambda x:(x[0].degree(),tuple(int(c) for c in x[0].coeffs()))):
 results.append(test_whole_weight_ideal(phi))
weight_bound=sum(r["actualResidueWeightQuotientDimension"] for r in results)
assert len(results)==5 and 0<=weight_bound<=56
say("new_P201_five_same_Q_original_ideal_finished",
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 prime=PRIME,actualOriginalBlockResults=results,
 totalResidualWeightQuotientDimension=weight_bound,
 characteristicZeroDistinctWeightPairUpperBound=weight_bound,
 characteristicZeroDistinctFiveCoordinatePointUpperBound=18*weight_bound,
 characteristicZeroDistinctFullNormalizedPointUpperBound=36*weight_bound,
 entireOriginalH1PhiDnonzeroGraphExcluded=(weight_bound==0),
 dimensionJustification="finite free completed original weight algebra, actual integral ideal matrix; generic rank is at least residue rank",
 originalNormComplementAlreadyPaid=True,
 noQQFactorIdentification=True,
 noOriginalLambdaOrGeometricFinitenessAssumedForWeightIdealTest=True,
 noOldHighDegreeRBlockDriverExecuted=True,
 noOldQQDixonGaussianReplayed=True,noOldNormBezoutProofReplayed=True,
 coefficientPayloadTransmitted=False,encodedOrSplitPayloadCreated=False,
 ordinaryISPClaim=False,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)
