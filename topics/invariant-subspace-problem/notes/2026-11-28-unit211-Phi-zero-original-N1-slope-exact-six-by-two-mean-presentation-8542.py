#!/usr/bin/env python3
"""NEW exact two-generator original Phi mean/N1 presentation.
On the paid whole first quadratic head, extract the actual N1 slope
Delta=a*d-b*c. Keep its ENTIRE zero weight locus. On Delta!=0 change
(1,T,z) to (1,Z,Nrow), Z=a*T+c*z, and eliminate only Nrow.
The three original means become three quadratics in Z. Their genuine
original combination is MONIC Z^2-beta1*Z-beta0. Hence the whole four
original mean/N1 ideal is exactly a monic square plus three linear
rows, or SIX exact stable rows over the physical lambda ring.
Return their actual coefficient identities and new primitive constant
targets of the three individual original rows and their Z products.
No old P6/P9, weak Popov, Gaussian, norm, or complete Gram audit.
120 seconds /1 GiB. Source definitions and small receipts only.
2026-11-28 Asia/Taipei.
"""
import os,time,json,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
START=time.perf_counter();DEADLINE=START+120
signal.alarm(120);resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,separators=(",",":")),flush=True)
name="2026-11-27-unit211-Phi-zero-first-quadratic-head-three-original-rows-D-input-8542.py"
path=Path(os.environ.get("ISP_PHI_FIRST_HEAD_RULE_SOURCE",str(Path(__file__).with_name(name))))
raw=path.read_bytes()
assert hashlib.sha256(raw).hexdigest()=="100ce4dfb7380da1591cd453aae392e2dafcaaceb3a601c4500d07852841ecaf"
mark=b"\ndet0=determinant(rows)\n";assert raw.count(mark)==1
prefix=raw.split(mark)[0]
assert len(prefix)==7097
assert hashlib.sha256(prefix).hexdigest()=="9467955925e4f6bd05aaf74c5d8fb7e747a03c0a5119fb17ee2b87e7703a701b"
ns={"__file__":str(path),"__name__":"new_original_Phi_two_generator_definition"}
original_alarm=signal.alarm;original_timer=signal.setitimer
def bounded_timer(which,seconds,interval=0):
 if which!=signal.ITIMER_REAL:return original_timer(which,seconds,interval)
 remaining=max(.001,DEADLINE-time.perf_counter())
 requested=float(seconds) if seconds>0 else remaining
 return original_timer(which,min(remaining,requested),0)
def bounded_alarm(seconds):
 return math.ceil(bounded_timer(signal.ITIMER_REAL,seconds)[0])
signal.alarm=bounded_alarm;signal.setitimer=bounded_timer
try:
 with contextlib.redirect_stdout(io.StringIO()):
  exec(compile(prefix,str(path)+":only-original-three-rules","exec"),ns)
finally:
 signal.alarm=original_alarm;signal.setitimer=original_timer
 original_timer(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
R=ns["R"];ctx=ns["ctx"];zero=ns["zeroP"];one=ns["oneP"]
up,Qp,Lp,Tp,zp=ctx.gens()
u,Q,ell,delta,m,M,T0,J,P02=[ns[s] for s in ["u","Q","ell","delta","m","M","T0","J","P02"]]
head=ns["head_det"];head_adj=ns["head_adj"];quads=ns["quads"]
rules=ns["rules"];leftover=ns["leftover"]
def profile(p):
 h=hashlib.sha256();nb=0
 for e,c in sorted(p.to_dict().items()):
  raw=(json.dumps([list(map(int,e)),str(c)],separators=(",",":"))+"\n").encode()
  h.update(raw);nb+=len(raw)
 return dict(degrees=list(map(int,p.degrees())),totalDegree=int(p.total_degree()),
             terms=len(p.to_dict()),bytes=nb,sha256=h.hexdigest())
def rprofile(x):return dict(numerator=profile(x.n),denominator=profile(x.d))
def weight_only(p):return all(not any(e[2:]) for e in p.to_dict())
def exact(a,b):
 q=a/b;assert q*b==a
 return q
paid=[("u",u.n),("u-1",(u-1).n),("Q",Q.n),("1-Q",delta.n),
 ("ell",ell.n),("u-ell",m.n),("M",M.n),("T0",T0.n),
 ("J-Q",(J-Q).n),("P02",P02.n),("u+Q-1",(u+Q-1).n),
 ("whole_Phi_first_head_now_paid",head.n),
 ("whole_Phi_ell_three_halves_already_excluded",(2*ell-3).n)]
for _,p in paid:assert p and weight_only(p)
def strip_paid(p,chart=False):
 assert p
 result=p;unit=one;history=[]
 atoms=paid+([("new_slope_chart",Delta.n)] if chart else [])
 for label,atom in atoms:
  count=0
  while True:
   g=result.gcd(atom)
   if g.total_degree()==0:break
   result=exact(result,g);unit*=g;count+=1
  if count:history.append(dict(unit=label,passes=count))
 scalar=result.coefficient(0)
 result=exact(result,ctx.constant(scalar));unit*=scalar
 assert unit*result==p
 return result,unit,history
def legal(x,chart=False):
 x=R(x)
 assert all(e[3]==e[4]==0 for e in x.n.to_dict())
 assert weight_only(x.d)
 rest,_,_=strip_paid(x.d,chart);assert rest.total_degree()==0
 return x
def coeff_lambda(x,maximum):
 x=legal(x)
 out=[zero for _ in range(maximum+1)]
 for e,c in x.n.to_dict().items():
  k=int(e[2]);assert k<=maximum
  out[k]+=ctx.from_dict({(int(e[0]),int(e[1]),0,0,0):c})
 result=[R(p,x.d) for p in out]
 assert sum((v*R(Lp)**i for i,v in enumerate(result)),R())==x
 return result
p0,p1,p2=leftover
cc1=coeff_lambda(p1,1);cc2=coeff_lambda(p2,1);coeff_lambda(p0,2)
b,a=cc1;d,c=cc2
Delta=a*d-b*c
assert Delta==a*p2-c*p1
if not Delta:
 say("new_Phi_N1_slope_identically_zero",
     wholeWeightZeroLocusRetained=True,
     noTwoGeneratorChartOrOriginalExclusionClaim=True)
 signal.setitimer(signal.ITIMER_REAL,0);raise SystemExit(0)
slope_core,slope_paid,slope_removed=strip_paid(Delta.n)
assert slope_core*slope_paid==Delta.n
say("new_Phi_original_N1_weight_slope_input",
 actualN1RowLambdaUpperBounds=[2,1,1],
 exactSlopeIdentityReturned=True,
 actualSlope=rprofile(Delta),retainedEntireSlopeWeightSupport=profile(slope_core),
 removedOnlyExistingWholePhiUnits=slope_removed,
 wholeSlopeZeroBranchRetained=True,
 noLambdaOrPhysicalDInverseUsed=True)

# Coefficient vectors below are in a NEW FORMAL Z, over the same
# physical lambda ring. These are actual invertible coordinates:
# Z=a*T+c*z; Nrow=p0+p1*T+p2*z.
# T=(p2*Z-c*Nrow+c*p0)/Delta,
# z=(-p1*Z+a*Nrow-a*p0)/Delta.
tx=[c*p0/Delta,p2/Delta]
zx=[-a*p0/Delta,-p1/Delta]
assert a*tx[0]+c*zx[0]==0 and a*tx[1]+c*zx[1]==1
assert p0+p1*tx[0]+p2*zx[0]==0
assert p1*tx[1]+p2*zx[1]==0
def add3(x,y):return [x[i]+y[i] for i in range(3)]
def scale3(x,s):return [v*s for v in x]
def affine3(x):return [x[0],x[1],R()]
def mul_affine(x,y):
 return [x[0]*y[0],x[0]*y[1]+x[1]*y[0],x[1]*y[1]]
def transformed_quad(q):
 out=[q[0],R(),R()]
 out=add3(out,scale3(affine3(tx),q[1]))
 out=add3(out,scale3(affine3(zx),q[2]))
 out=add3(out,scale3(mul_affine(tx,tx),q[3]))
 out=add3(out,scale3(mul_affine(tx,zx),q[4]))
 out=add3(out,scale3(mul_affine(zx,zx),q[5]))
 for v in out:legal(v,True)
 return out
transformed=[transformed_quad(q) for q in quads]
means=transformed[:3]
h4=quads[3][3:]
n1_from_means=[sum((h4[i]*head_adj[i][j]/head for i in range(3)),R())
               for j in range(3)]
assert all(sum((n1_from_means[i]*means[i][j] for i in range(3)),R())==transformed[3][j]
           for j in range(3))
# The square comes DIRECTLY from the paid three original mean rules.
sqweight=[a*a,2*a*c,c*c]
srow=[sum((sqweight[i]*rules[i][j] for i in range(3)),R()) for j in range(3)]
kappa=(-c*srow[1]+a*srow[2])/Delta
beta0=srow[0]-kappa*p0
beta1=(p2*srow[1]-p1*srow[2])/Delta
for v in [beta0,beta1]:legal(v,True)
square_source=[sum((sqweight[i]*head_adj[i][j]/head for i in range(3)),R())
               for j in range(3)]
monic=[-beta0,-beta1,R(1)]
assert all(sum((square_source[i]*means[i][j] for i in range(3)),R())==monic[j]
           for j in range(3))
assert int(beta0.n.degrees()[2])<=3 and int(beta1.n.degrees()[2])<=2
# These full identities establish an exact polynomial-ideal
# presentation, not just necessary rows at original solutions.
remainders=[]
for i,q in enumerate(means):
 row=[q[0]+q[2]*beta0,q[1]+q[2]*beta1]
 assert q[0]==row[0]+q[2]*monic[0]
 assert q[1]==row[1]+q[2]*monic[1]
 assert q[2]==q[2]*monic[2]
 remainders.append(row)
say("new_Phi_exact_original_four_polynomial_two_generator_presentation",
 invertibleSamePointCoordinate="Z=a*T+c*z; Nrow=p0+p1*T+p2*z",
 determinant="Delta=a*d-b*c",
 allFourAffineCoordinateCoefficientProductsReturned=True,
 transformedOriginalN1ExactlyInThreeTransformedMeanIdeal=True,
 allThreeN1CoefficientProductsReturned=True,
 monicSquareOriginalCombinationReturned=True,
 monicSquare="Z^2-beta1*Z-beta0",
 monicSquareCoefficients=[rprofile(beta0),rprofile(beta1)],
 monicSquareLambdaDegreeUpperBounds=[3,2],
 allNineOriginalMeanDecompositionProductsReturned=True,
 exactOriginalFourPolynomialIdeal=True,
 threeLinearRemainders=[ [rprofile(x) for x in rr] for rr in remainders],
 originalQuotientFreeNotAssumed=True,
 fullIndividualOriginalValueEquationsNotYetIncluded=True,
 wholeSlopeZeroBranchRetained=True,wholePhiExcluded=False)
def times_Z(row):
 return [row[1]*beta0,row[0]+row[1]*beta1]
# In the actual monic-square environment, this multiplication closes
# EVERY row: Z^2*r=beta1*(Z*r)+beta0*r, with full two-column products.
stable=[]
for i,row in enumerate(remainders):
 child=times_Z(row);twice=times_Z(child)
 assert all(twice[j]==beta1*child[j]+beta0*row[j] for j in range(2))
 stable.extend([row,child])
 for v in row+child:legal(v,True)
say("new_Phi_complete_six_by_two_original_module",
 basis=["1","Z"],originalMeanCount=3,moduleRelationCount=6,
 sourceRows=["R","Z*R","W","Z*W","O","Z*O"],
 allSixClosureCoefficientProductsReturned=True,
 exactPresentationOverPhysicalLambdaRing=True,
 monicQuadraticAmbientOnlyIsFree=True,
 noOldMultiplicationCommutatorModuleOrGaussianExecuted=True,
 wholeSlopeZeroBranchRetained=True,wholePhiExcluded=False)
def polynomial_row(row):
 den=one
 for x in row:
  legal(x,True);den=exact(den,den.gcd(x.d))*x.d
 pp=[x.n*exact(den,x.d) for x in row]
 if not any(pp):return [zero,zero],R(1)
 g=pp[0].gcd(pp[1]);_,unit,_=strip_paid(g,True)
 pp=[exact(p,unit) for p in pp]
 scalar=next(p for p in pp if p).coefficient(0)
 pp=[exact(p,ctx.constant(scalar)) for p in pp]
 multiplier=R(den,unit*scalar)
 for j in range(2):assert R(pp[j])==multiplier*row[j]
 legal(multiplier,True)
 return pp,multiplier
# A new fixed target per ORIGINAL mean: r and its genuine Z product.
# Cancelling a common factor from the TWO actual multipliers is safe;
# the complete returned column identity preserves that factor's zeros.
targets=[]
for i,label in enumerate(["R","W","O"]):
 rr,scale0=polynomial_row(stable[2*i])
 zr,scale1=polynomial_row(stable[2*i+1])
 omega=[zr[1],-rr[1]]
 if not any(omega):
  say("new_Phi_original_mean_constant_target_degenerate",
      original=label,bothZCoefficientsZero=True,
      actualConstantRows=[profile(rr[0]),profile(zr[0])],
      entireOriginalRowsRetained=True)
  targets.append(dict(original=label,degenerate=True));continue
 common=omega[0].gcd(omega[1])
 primitive=[exact(v,common) for v in omega]
 target=primitive[0]*rr[0]+primitive[1]*zr[0]
 assert primitive[0]*rr[1]+primitive[1]*zr[1]==0
 assert target*common==rr[0]*zr[1]-rr[1]*zr[0]
 if not target:
  say("new_Phi_original_mean_constant_target_zero",
      original=label,twoExactColumnProductsReturned=True,
      commonMultiplierFactor=profile(common),
      noOriginalExclusionClaim=True)
  targets.append(dict(original=label,zero=True));continue
 result,unit,removed=strip_paid(target,True)
 beta=[R(primitive[0])*scale0/R(unit),R(primitive[1])*scale1/R(unit)]
 for x in beta:legal(x,True)
 assert sum((beta[k]*stable[2*i+k][0] for k in range(2)),R())==R(result)
 assert sum((beta[k]*stable[2*i+k][1] for k in range(2)),R())==0
 record=dict(original=label,polynomial=profile(result))
 targets.append(record)
 say("new_Phi_actual_original_mean_Z_product_scalar_target",
     original=label,actualScalarOriginalIdealElement=profile(result),
     commonFactorCancelledOnlyFromBothActualMultipliers=profile(common),
     allNewTwoColumnSourceProductsReturned=True,
     removedOnlyOldUnitsAndExplicitSlopeChart=removed,
     sourceDefinition="sum_j beta_j*(remainder_of_original_mean_or_its_Z_product)",
     wholeCommonMultiplierZeroFibresPreserved=True,
     allUnpaidScalarContentsAndLambdaHeadZeroFibresRetained=True,
     noPrimitiveScalarAloneClaimIfUnpaidContentRemains=True,
     wholePhiExcluded=False)
say("new_Phi_original_N1_slope_exact_six_two_module_finished",
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 necessaryOriginalPrefixBytes=len(prefix),
 originalSlopeWeightSupport=profile(slope_core),
 exactOriginalMeanN1QuotientOnSlopeComplement=True,
 completeStableModuleRows=6,completeStableModuleColumns=2,
 newOriginalConstantTargets=targets,
 noClaimAboutWholeSlopeZeroBranch=True,
 noClaimOfOriginalLambdaHeadUnit=True,
 noOldP6P9WeakPopovGaussianNormOrGramGateReplayed=True,
 noRecomputableCoefficientCacheEncodingOrSplitSaved=True,
 wholePhiExcluded=False,ordinaryISPClaim=False,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.setitimer(signal.ITIMER_REAL,0);signal.alarm(0)
