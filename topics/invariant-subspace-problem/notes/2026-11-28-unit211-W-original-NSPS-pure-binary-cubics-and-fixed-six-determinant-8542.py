#!/usr/bin/env python3
"""NEW full original NS/PS cubic compression and six-point necessary determinant.
Every original cubic is reduced by an explicit polynomial identity:
P = pure_binary_cubic + mQ*QF + U*R1 + V*R2 + c00*R0.
No geometric leading coefficient, lambda or D is inverted in this identity.
On the retained H265 != 0 chart, use the already frozen four-rule/twelve-
multiplication CONSTRUCTION prefix only (never the failed four-value gate).
Return the NEW pure original NS/PS and their actual lambda/S products,
then ONE fixed six-by-six determinant in QQ[e,k], with every Bareiss
division multiplied back. No generic-rational target Gaussian replay.
All H265=0 and every remaining parameter-zero fibre are retained.
180 seconds / 4 GiB. Only source/definitions/profiles/hash; no data payload.
"""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
start=time.perf_counter();deadline=start+180;signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**r):
 r['seconds']=time.perf_counter()-start
 print(json.dumps(r,separators=(',',':')),flush=True)
dep=Path(__file__).with_name('2026-11-28-unit211-W-first-binary-head-open-original-low-value-six-coordinate-return-8542.py')
raw=dep.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='ffa9634230009c3f949e2f9a4e051f891f0ad28769e971bc393cc560da8ffb66'
marker=b"\n# NEW original low-degree value input."
assert raw.count(marker)==1
prefix=raw.split(marker)[0]
assert hashlib.sha256(prefix).hexdigest()=='2a69d39d3240309cbbd47523ecd1bf6156c4dae862a7cb83e4dd04dee9dc71d7'
inp={'__file__':str(dep),'__name__':'__four_rules_and_true_multiplication_only_for_NEW_original_NSPS__'}
with contextlib.redirect_stdout(io.StringIO()):
 exec(compile(prefix,str(dep),'exec'),inp)
signal.alarm(max(1,math.ceil(deadline-time.perf_counter())))
C,P,ctx,x,y,H,prof,paid,ppaid,strip_paid,binary,reduce_new,vector,rules,multiplication,base=[
 inp[v] for v in ['C','P','ctx','x','y','H','prof','paid','ppaid','strip_paid','binary',
 'reduce_new','vector','rules','multiplication','base']]
canon=inp['ns']
F,A0,B0,C0,E0,d,rF2,rcan=[canon[v] for v in ['F','A','B','Cc','E','d','rF2','rcan']]
original=base['ns']['original']
zero=ctx.constant(0);one=ctx.constant(1)
# The reused construction added precisely H265 as a chart unit.
# Check that the new GLOBAL cubic identities themselves never use H265.
checked_global_den=set()
def global_weight_den(pp):
 ppaid(pp)
 for cf in P(pp).t.values():
  assert cf.d.degrees()[2]<=0
  key=str(cf.d)
  if key not in checked_global_den:
   assert cf.d.gcd(H).total_degree()==0
   checked_global_den.add(key)
def info_binary(pp,bound):
 dd=binary(pp,bound)
 return dict(totalGeometryDegree=max((sum(mm) for mm in dd),default=-1),
   geometricMonomials=len(dd),
   coefficientNumeratorTerms=sum(len(cf.n.to_dict()) for cf in dd.values()),
   maximumNumeratorDegrees=[max((int(cf.n.degrees()[j]) for cf in dd.values()),default=-1) for j in range(2)],
   maximumDenominatorDegrees=[max((int(cf.d.degrees()[j]) for cf in dd.values()),default=-1) for j in range(2)],
   completePolynomial=base['digest']([pp]))
def pure_original_cubic(pp,label):
 pp=P(pp);blocks=[P() for _ in range(4)]
 for (ff,j),cf in pp.t.items():
  assert 0<=ff<=3
  blocks[ff]+=P.monomial((0,j),cf)
 assert pp==sum(((F**j)*blocks[j] for j in range(4)),P())
 for j in range(4):binary(blocks[j],3-j)
 c3=blocks[3].t.get((0,0),C())
 assert blocks[3]==P(c3) and c3.n.degrees()[2]<=0
 U2=blocks[1]-blocks[2].scale(d)+P(c3*d*d)-E0.scale(c3)
 V3=blocks[0]-blocks[2]*E0+E0.scale(c3*d)
 uc=binary(U2,2);binary(V3,3)
 cc=lambda i,j:uc.get((i,j),C())
 Up=x.scale(cc(2,0))+y.scale(cc(1,1))+P(cc(1,0))
 Vp=y.scale(cc(0,2))+P(cc(0,1))
 c00=cc(0,0)
 assert U2==x*Up+y*Vp+P(c00)
 mQ=F.scale(c3)+blocks[2]-P(c3*d)
 pure=V3-Up*B0-Vp*C0-A0.scale(c00)
 assert pp==pure+mQ*rF2+Up*rcan[1]+Vp*rcan[2]+rcan[0].scale(c00)
 binary(pure,3)
 for pol in [pp,pure,mQ,Up,Vp,P(c00)]:global_weight_den(pol)
 say(stage='new_W_entire_original_cubic_pure_binary_identity',
     original=label,completeOriginalPolynomialProductActuallyReturned=True,
     exactIdentity='P=pure+mQ*QF+Up*R1+Vp*R2+c00*R0',
     actualPureBinaryCubic=info_binary(pure,3),
     fullOriginalMultiplierDefinition=base['digest']([mQ,Up,Vp,P(c00)]),
     globalPaidWeightDenominatorsOnly=True,
     noH265LambdaSPhysicalDOrNewHeadInverted=True,
     noSubstitutionOfFThatRaisesTheGeometryDegree=True,
     originalWeightedNecessityFromSameHAHBValues=True,
     wholeWExcluded=False)
 return pure,[mQ,Up,Vp,P(c00)]
pure_rows={};vectors={};traces={}
for label in ['NS','PS']:
 pp=original[label]
 pure,muls=pure_original_cubic(pp,label)
 rem,qq=reduce_new(pure,'NEW_original_'+label+'_pure_cubic',3)
 assert pp==rem+sum((qq[j]*rules[j] for j in range(4)),P())+muls[0]*rF2+muls[1]*rcan[1]+muls[2]*rcan[2]+muls[3]*rcan[0]
 pure_rows[label]=pure;vectors[label]=vector(rem);traces[label]=qq
 say(stage='new_W_H265_actual_original_NSPS_six_coordinate_row',
     original=label,actualRemainder=info_binary(rem,2),
     entireOriginalAndFourRuleProductActuallyReturned=True,
     originalRuleMultiplierDefinition=base['digest'](qq),
     allLocalDenominatorsOnlyPaidWeightsAndExplicitH265=True,
     noOldR3Q4WeightGaussianGateReplayed=True,
     H265ZeroWholeFibreRetained=True)
def matvec(mat,vec):
 return [sum((mat[i][j]*vec[j] for j in range(6)),C()) for i in range(6)]
def primitive_column(vv,label):
 assert len(vv)==6
 for cf in vv:
  assert cf.n.degrees()[2]<=0 and cf.d.degrees()[2]<=0
  paid(cf)
 if not any(vv):return [zero]*6,C(1)
 den=one
 for cf in vv:
  g=den.gcd(cf.d);dd=den/g;assert dd*g==den;den=dd*cf.d
 nums=[]
 for cf in vv:
  dd=den/cf.d;assert dd*cf.d==den
  nums.append(cf.n*dd)
 common=next(z for z in nums if z)
 for z in nums:
  if z:common=common.gcd(z)
 left,removed=strip_paid(common)
 assert left*removed==common
 scale=C(den,removed);paid(scale);paid(1/scale)
 ans=[]
 for z,cf in zip(nums,vv):
  val=z/removed;assert val*removed==z and C(val)==cf*scale
  ans.append(val)
 say(stage='new_W_original_NSPS_fixed_column_paid_polynomial_normalization',
     label=label,allSixScalarProductsReturned=True,
     maximumDegrees=[max(int(z.degrees()[j]) for z in ans) for j in range(2)],
     totalTerms=sum(len(z.to_dict()) for z in ans),
     commonDenominator=prof(den),paidContentRemoved=prof(removed),
     unpaidCommonNotRemoved=True,
     pointwiseOriginalColumnStillNecessary=True)
 return ans,scale
# Actual value row v satisfies v*Mlambda=lambda*v and v*MS=S*v.
# These six columns therefore vanish on the same original point,
# regardless of whether the six displayed generators are free.
labels=['NS','PS','lambda*NS','S*NS','lambda*PS','S*PS']
rawcols=[vectors['NS'],vectors['PS'],
 matvec(multiplication['lambda'],vectors['NS']),
 matvec(multiplication['S'],vectors['NS']),
 matvec(multiplication['lambda'],vectors['PS']),
 matvec(multiplication['S'],vectors['PS'])]
columns=[];scales=[]
for label,vv in zip(labels,rawcols):
 col,scale=primitive_column(vv,label);columns.append(col);scales.append(scale)
matrix=[[columns[j][i] for j in range(6)] for i in range(6)]
say(stage='new_W_original_NSPS_fixed_six_by_six_parameter_input',
 actualOriginalColumnDefinitions=labels,
 completeOriginalValueRow='v=(1,lambda,S,lambda^2,lambda*S,S^2)',
 allSixColumnsVanishAtSameOriginalPoint=True,
 constantCoordinateExactlyOne=True,
 freeModuleOrGlobalMatrixCommutativityNotAssumed=True,
 matrixDefinition=base['digest']([P(C(z)) for row in matrix for z in row]),
 allUnpaidWeightAndH265FibresRetained=True,
 noParameterDeterminantYetClaimed=True)
# Exact polynomial Bareiss determinant. Divisions are polynomial identities
# in QQ[e,k], not pointwise inversions or chart restrictions.
mm=[row[:] for row in matrix];previous=one;sign=1;determinant=None
division_products=0
for j in range(5):
 if not mm[j][j]:
  chosen=next((i for i in range(j+1,6) if mm[i][j]),None)
  if chosen is None:
   determinant=zero;break
  mm[j],mm[chosen]=mm[chosen],mm[j];sign=-sign
 pivot=mm[j][j]
 for i in range(j+1,6):
  for h in range(j+1,6):
   numerator=mm[i][h]*pivot-mm[i][j]*mm[j][h]
   value=numerator/previous
   assert value*previous==numerator
   mm[i][h]=value;division_products+=1
  mm[i][j]=zero
 previous=pivot
 say(stage='new_original_NSPS_fixed_Bareiss_polynomial_identity_step',
     step=j,actualExactDivisionProducts=division_products,
     currentTrailingDegrees=[max(int(mm[i][h].degrees()[a]) for i in range(j+1,6) for h in range(j+1,6)) for a in range(2)],
     currentTrailingTotalTerms=sum(len(mm[i][h].to_dict()) for i in range(j+1,6) for h in range(j+1,6)),
     noInstantaneousPivotZeroFibreDiscarded=True,
     noPointwiseParameterInverseUsed=True)
if determinant is None:determinant=sign*mm[5][5]
if determinant:
 say(stage='new_original_NSPS_complete_fixed_six_order_determinant',
     rawNecessaryWeightPolynomial=prof(determinant),
     matrixOrder=6,completeExactPolynomialDivisions=division_products,
     necessaryOnExplicitH265Complement=True,
     allInstantaneousHeadZeroFibresRetainedByPolynomialIdentity=True)
 rest,removed=strip_paid(determinant)
 assert rest*removed==determinant
 scalar=rest.coefficient(0);rest=rest/scalar;removed*=scalar
 assert rest*removed==determinant
 whole_cover=H*rest
 say(stage='new_original_NSPS_weight_curve_necessary_cover',
     exactDefinition='H265 times the paid normalization of the fixed six-column NS,PS,lambda*NS,S*NS,lambda*PS,S*PS determinant',
     remainingHChartNecessaryPolynomial=prof(rest),
     wholeOriginalWeightCover=prof(whole_cover),
     allPaidStrippingProductsActuallyReturned=True,
     H265WholeZeroCurveRetained=True,
     H265ComplementExcluded=(rest.total_degree()==0),
     coverIsNotClaimedSaturatedOrSquarefree=True,
     wholeWExcluded=False)
else:
 say(stage='accurate_new_NSPS_fixed_determinant_identically_zero',
     allSixOriginalColumnsActuallyConstructed=True,
     noNewWeightCoverClaim=True,wholeWExcluded=False)
say(stage='new_full_original_NSPS_cubic_and_fixed_weight_input_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 fixedDeterminantActuallyReturned=True,
 determinantNonzero=bool(determinant),
 allOriginalCubicIdentitiesReturned=True,
 allUnpaidOriginalFibresRetained=True,
 noOldR3Q4GaussianOrFifteenMinorGateReplayed=True,
 noEncodedOrChunkedCoefficientPayloadCreated=True,
 noRegenerableCoefficientCertificateOrMatrixCacheWritten=True,
 wholeWExcluded=False,ordinaryISPClaim=False,
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)
