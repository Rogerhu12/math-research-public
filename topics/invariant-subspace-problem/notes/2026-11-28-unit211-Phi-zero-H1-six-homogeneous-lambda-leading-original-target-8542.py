#!/usr/bin/env python3
"""NEW six true lambda-six leading columns on original Phi/H1.
Use only the four cleared original row construction, then the total
quadratic homogeneous part at lambda=1. No complete old cofactor, norm
resultant, Dixon Gaussian or data payload is rebuilt. The six actual
leading scalars come from the same adjugate columns. Only named paid
weight units and the now-published entire h-zero exclusion are removed,
each by a complete polynomial product. Whole-Q4 regular adjugates and
a QQ[u] norm Bezout give a new explicit common leading target C(u).
Its every remaining zero factor is retained. 120s/1GiB.
2026-11-28 Asia/Taipei.
"""
import os,time,json,hashlib,signal,resource,contextlib,io,itertools
from pathlib import Path
from flint import fmpq,fmpq_poly
started=time.perf_counter();deadline=started+120
signal.alarm(120);resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-started)
 print(json.dumps(kw,separators=(",",":")),flush=True)
basename="2026-11-28-unit211-Phi-zero-H1-polynomial-v-source-scaled-matrices-fixed-norm-input-8542.py"
path=Path(os.environ.get("ISP_H1_POLYNOMIAL_V_SOURCE",str(Path(__file__).with_name(basename))))
raw=path.read_bytes()
assert hashlib.sha256(raw).hexdigest()=="5f6ba628dd4a660a7cedc7bb338a7cebc9cdc1ac3b6d6958a36409cb578b00ef"
vs=raw.decode()
marker="\n DD=ell*A2-Tr*Tr;B3="
assert vs.count(marker)==1
prefix=vs.split(marker,1)[0]+"\n return cleared,units\n"
assert "def whole_polynomial_module" not in prefix
env={"__file__":str(path),"__name__":"__four_original_rows_for_NEW_lambda_leading_target__"}
with contextlib.redirect_stdout(io.StringIO()):
 exec(compile(prefix,str(path)+"::<new-homogeneous-head-only>","exec"),env)
 originals,units=env["new_original_polynomials"]()
signal.setitimer(signal.ITIMER_REAL,max(.001,deadline-time.perf_counter()))
A,P,pol,up,one,zero,qrow,det3,adj3,exact,monic,pdigest=[
 env[k] for k in ["A","P","pol","up","one","zero","qrow","det3","adj3","exact","monic","pdigest"]]
u,Q=env["u"],env["Q"]
fullqr=[qrow(p) for p in originals]
assert all(sum(e)<=2 for p in originals for e in p.v)
# The coefficient map here is the exact total-degree-two part,
# followed by lambda=1. It is not a numerical specialization of lambda.
homogeneous=[]
for p in originals:
 hp=P.from_terms({(0,tt,vv):co for (ll,tt,vv),co in p.v.items() if ll+tt+vv==2})
 homogeneous.append(hp)
qr0=[qrow(p) for p in homogeneous]
assert all(c.degree()<=0 for row in qr0 for c in row)
qr=[[c.c[0] if c.c else A() for c in row] for row in qr0]
heads=[row[3:] for row in qr]
assert det3(heads[:3])==0
indices=[0,1,3]
hh=[heads[i] for i in indices];h=det3(hh);ad=adj3(hh)
assert h and h.d==one
assert all(sum((ad[i][k]*hh[k][j] for k in range(3)),A())==(h if i==j else 0)
           for i in range(3) for j in range(3))
# A lambda coefficient lambda^d T^a v^b has d+a+b equal to its
# total degree. Thus leading profiles (2,1,1)/(3,2,2) are read exactly
# by the homogeneous functor and these six scalar determinants.
rules=[[-sum((ad[j][i]*qr[indices[i]][k] for i in range(3)),A())
        for k in range(3)] for j in range(3)]
T,V=env["Tr"],env["z"]
def avec(v):
 return sum((P(c)*b for c,b in zip(v,[P(1),T,V])),P())
hmon=[T*T,T*V,V*V]
for j in range(3):
 assert h*hmon[j]-avec(rules[j])==sum((ad[j][i]*homogeneous[indices[i]] for i in range(3)),P())
MT=[[A(),rules[0][i],rules[1][i]] for i in range(3)]
MV=[[A(),rules[1][i],rules[2][i]] for i in range(3)]
MT[1][0]=h;MV[2][0]=h
def matmul(a,b):
 return [[sum((a[i][k]*b[k][j] for k in range(3)),A()) for j in range(3)] for i in range(3)]
def mv(a,v):
 return [sum((a[i][j]*v[j] for j in range(3)),A()) for i in range(3)]
other=qr[2]
r=[h*other[k]+sum((other[j+3]*rules[j][k] for j in range(3)),A()) for k in range(3)]
assert h*homogeneous[2]-avec(r)==sum((other[j+3]*(h*hmon[j]-avec(rules[j])) for j in range(3)),P())
ma,mb=matmul(MT,MV),matmul(MV,MT)
comm=[[ma[i][j]-mb[i][j] for i in range(3)] for j in range(3)]
assert not any(comm[0])
cols=[r,mv(MT,r),mv(MV,r),comm[1],comm[2]]
labels=["scaled_original_O","scaled_T_original_O","scaled_v_original_O",
 "scaled_actual_commutator_T","scaled_actual_commutator_v"]
say("new_H1_six_exact_homogeneous_leading_columns",
 originalQuadricRows=4,originalHeadAdjugateProductsReturned=True,
 originalHomogeneousRelationProductsReturned=True,
 totalDegreeProfiles=[[2,1,1],[3,2,2]],
 actualLambdaDegreeUpperBound=6,
 completeOldLambdaCofactorsRebuilt=False,
 oldResultantOrGaussianExecuted=False,
 affinePointOrGenericLambdaValueSubstituted=False)

ln=Q-2*(u-1)*(u-2);mn=u*Q-ln
paid=[("published_complete_actual_three_head_zero_exclusion",h)]+units+[
 ("whole_Q_equals_one_minus_u",Q+u-1),
 ("whole_rho_quadratic_head",(ln-Q)*(1-Q)*Q-2*mn*mn)]
def score(a):
 assert a.d==one
 return sum(max(0,int(p.degree())+1) for p in a.n)
def primitive_lead(value,label):
 original=A(value);out=A(value);factor=A(1);removed=[]
 for unit_label,unit in paid:
  iv=unit.inverse("new exact lambda leading factor "+unit_label)
  for exponent in range(96):
   candidate=out*iv
   if candidate.d!=one or score(candidate)>=score(out):break
   assert candidate*unit==out
   out=candidate;factor=factor*unit
   if removed and removed[-1]["unit"]==unit_label:removed[-1]["power"]+=1
   else:removed.append(dict(unit=unit_label,power=1))
 assert factor*out==original and out.d==one
 say("new_H1_actual_lambda_leading_paid_factor_return",
  originalColumns=label,removed=removed,
  residualIdentity=env["pprofile"](P(out)),
  completeFourCoordinatePolynomialProductReturned=True,
  hPaidOnlyByPublishedOriginalValueExclusion=True,
  noNormOrUnpaidAlgebraElementTreatedAsOriginalUnit=True)
 return out,factor

def det_poly(mat):
 n=len(mat)
 if not n:return one
 mm=[row[:] for row in mat];previous=one;sign=1
 for j in range(n-1):
  if not mm[j][j]:
   sw=next((i for i in range(j+1,n) if mm[i][j]),None)
   if sw is None:return zero
   mm[j],mm[sw]=mm[sw],mm[j];sign=-sign
  pivot=mm[j][j]
  for i in range(j+1,n):
   for k in range(j+1,n):
    mm[i][k]=exact(mm[i][k]*pivot-mm[i][j]*mm[j][k],previous)
   mm[i][j]=zero
  previous=pivot
 return sign*mm[-1][-1]
def whole_regular_adjugate(value):
 cs=[value*A([0]*j+[1]) for j in range(4)]
 assert all(c.d==one for c in cs)
 matrix=[[cs[j].n[i] for j in range(4)] for i in range(4)]
 norm=det_poly(matrix)
 # adj(matrix)e0: cofactor of row 0 and column j.
 adj=[]
 for j in range(4):
  minor=[[matrix[r][c] for c in range(4) if c!=j] for r in range(1,4)]
  adj.append(((-1)**j)*det_poly(minor))
 witness=A(adj)
 assert witness.d==one and value*witness==A(norm)
 return norm,witness

leads=[];factors=[];norms=[];adjoints=[];column_labels=[]
for i,j in itertools.combinations(range(1,5),2):
 label=[labels[k] for k in (0,i,j)]
 raw_lead=det3([[cols[k][r0] for k in (0,i,j)] for r0 in range(3)])
 assert raw_lead.d==one
 if not raw_lead:
  say("new_H1_actual_lambda_six_leading_identically_zero",
   originalColumns=label,allQQCoordinatesZero=True,
   lowerLambdaTermsNotDiscarded=True)
  continue
 lead,factor=primitive_lead(raw_lead,label)
 norm,adjoint=whole_regular_adjugate(lead)
 leads.append(lead);factors.append(factor);norms.append(norm);adjoints.append(adjoint);column_labels.append(label)
 say("new_H1_actual_leading_whole_Q4_norm_and_adjugate",
  originalColumns=label,normIdentity=pdigest(norm),
  completeRegularAdjugateProductReturned=True,
  actualQ4LeadingScalarIdentity="lead*adjoint=norm",
  wholeWeightAlgebraKept=True,coefficientPayloadTransmitted=False)

common=zero;tags=[zero for _ in norms];bezout_steps=0
for i,nn in enumerate(norms):
 if not nn:continue
 if not common:
  c=nn[nn.degree()];common=nn/c;tags[i]=one/c
 else:
  gg,aa,bb=common.xgcd(nn)
  assert aa*common+bb*nn==gg
  c=gg[gg.degree()];gg=gg/c;aa=aa/c;bb=bb/c
  tags=[aa*t for t in tags];tags[i]=tags[i]+bb
  common=gg;bezout_steps+=1
 assert sum((t*n for t,n in zip(tags,norms)),zero)==common
 if common.degree()==0:break
if not common:
 say("accurate_new_H1_no_nonzero_regular_leading_norm",
  entireOriginalGraphRetained=True,monicLambdaSixClaim=False,
  sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
 signal.alarm(0)
 raise SystemExit(0)
assert common[common.degree()]==1
weights=[A(t)*a for t,a in zip(tags,adjoints)]
assert sum((w*l for w,l in zip(weights,leads)),A())==A(common)
say("new_H1_actual_six_leading_original_target_identity",
 commonNormGcd=pdigest(common),completeQQNormBezoutSteps=bezout_steps,
 completeQQPolynomialBezoutProductReturned=True,
 completeFourCoordinateLeadingTargetReturned=True,
 identity="sum_i tag_i(u)*adjoint_i*rawLeading_i/paidFactor_i = C(u)",
 associatedOriginalDegreeSixPolynomial="sum_i tag_i(u)*adjoint_i*rawOriginalCofactor_i/paidFactor_i",
 trueLambdaSixLeadingEqualsSameC=True,
 currentOriginalPaidUnitsOnly=True,
 entireCZeroRetained=True,wholeH1ExclusionClaim=False)
constant,ff=common.factor();product=pol(constant)
for pp,e in ff:product=product*pp**e
assert product==common
known=[up,up-1,up-fmpq(3,2),up-fmpq(12,5),up-fmpq(5,2),
 pol([fmpq(-15,4),8,-5,1]),pol([4,-9,10,-5,1]),
 pol([fmpq(-52,9),20,fmpq(-995,36),fmpq(349,18),fmpq(-83,12),1]),
 pol([-8,fmpq(124,3),fmpq(-187,2),fmpq(709,6),fmpq(-4279,48),fmpq(319,8),fmpq(-39,4),1]),
 pol([fmpq(-864,11),fmpq(4464,11),fmpq(-7408,11),fmpq(6026,11),fmpq(-5255,22),fmpq(426,11),fmpq(291,22),fmpq(-81,11),1])]
paid_hashes={pdigest(f)["sha256"] for f in known}
paid_hashes.add("98fe71762eb2c2d0fd5a4e5ed09066704be36b65ee2e81ae88aa8a9f7a56b4cc")
profile=[];new_support=one
for pp,e in ff:
 pp=monic(pp);ident=pdigest(pp);old=ident["sha256"] in paid_hashes
 profile.append(dict(identity=ident,multiplicity=int(e),
  entireUFibreAlreadyPaid=old,
  reason=("published exact C55 whole-u exclusion or original u unit" if old
          else "new exact potential common-leading zero u factor; entire original fibre retained")))
 if not old:new_support=new_support*pp
say("new_H1_exact_six_lambda_leading_common_support",
 originalNormGcd=pdigest(common),completeQQFactorProductReturned=True,
 factors=profile,unpaidSquarefreeSupport=pdigest(new_support),
 allSixLeadingZeroNecessarilyOnUnpaidSupport=True,
 oneActualDegreeSixLeadingPaidEverywhere=(new_support.degree()==0),
 noOldClosedWeightValueGateReplayed=True,
 noPrimeOrNormZeroFactorTreatedAsUnit=True,
 originalPolynomialLeadingCombinationExistsAwayFromC=True)
say("new_H1_six_homogeneous_leading_original_input_finished",
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 actualLeadingCofactorCount=len(leads),commonNormGcd=pdigest(common),
 unpaidLeadingZeroSupport=pdigest(new_support),
 noCompleteOldCofactorOrResultantReplayed=True,
 currentP201DistinctWeightPairBound=804,
 P201CoefficientsKnown=False,ordinaryISPClaim=False,
 noCoefficientPayloadTransmitted=True,encodedOrSplitPayload=False,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)
