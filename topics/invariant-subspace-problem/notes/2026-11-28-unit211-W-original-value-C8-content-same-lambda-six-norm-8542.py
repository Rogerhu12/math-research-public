#!/usr/bin/env python3
"""NEW whole-W lambda content and same-point finite-algebra norm.
Regenerate only the NECESSARY fixed original C8 construction prefix.
Do not execute its old C8/chi division, the frozen 18-row module, any
old twelve-resultant, or the native NSPS two-parameter determinant.
First divide a common factor of ALL THREE original cofactor multipliers,
returning a new original polynomial Cstar on its ENTIRE zero fibre.
Write Cstar=U*G*P with U already paid and G UNPAID, all products returned.
In A_W[lambda]/(monic chi6), form the actual multiplication by P.
Clear columns by paid weight units only; return one determinant and its
entire original cofactor column. This proves G*det in the original I8.
G=0, norm=0 and all temporary pivot zero fibres are retained globally.
180 seconds /4GiB. Sources, definitions and small hashes only.
"""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
started=time.perf_counter();deadline=started+180
signal.alarm(180);resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**d):
 d['seconds']=time.perf_counter()-started
 print(json.dumps(d,separators=(',',':')),flush=True)
def frozen_prefix(name,sha,marker,size,phash,label):
 path=Path(__file__).with_name(name);raw=path.read_bytes()
 assert hashlib.sha256(raw).hexdigest()==sha and raw.count(marker)==1
 prefix=raw.split(marker)[0]
 assert len(prefix)==size and hashlib.sha256(prefix).hexdigest()==phash
 ns={'__file__':str(path),'__name__':label}
 # Older necessary prefixes set their own alarm. Cap each such call at
 # THIS source's original absolute deadline, never extending the 180s gate.
 saved_alarm=signal.alarm
 def bounded_alarm(seconds):
  remaining=max(.001,deadline-time.perf_counter())
  requested=float(seconds) if seconds>0 else remaining
  previous=signal.setitimer(signal.ITIMER_REAL,min(remaining,requested))
  return math.ceil(previous[0])
 signal.alarm=bounded_alarm
 try:
  with contextlib.redirect_stdout(io.StringIO()):
   exec(compile(prefix,str(path)+'#new_content_norm_input_only','exec'),ns)
 finally:
  signal.alarm=saved_alarm
 signal.setitimer(signal.ITIMER_REAL,max(.001,deadline-time.perf_counter()))
 return ns
inp=frozen_prefix(
 '2026-11-28-unit211-W-original-value-quartics-three-columns-lambda-five-8542.py',
 '87a890d6bf90e3f50e63eac989680bd78973e63299b60557f90d1fcb29d4e2ad',
 b'\n# Construct only the coefficients required for this NEW monic division.',
 7431,'e4c8ad9e117867918300972a4b15366f7e3281dbf858463bd1b2f4968a9ac55c',
 'only_fixed_original_value_C8_for_new_content_and_norm')
R=inp['R'];ctx=inp['ctx'];zero=inp['zero'];one=inp['one']
ep,kp=ctx.gens()[:2];Craw=inp['C'];pay=inp['pay'];strip=inp['strip']
assert Craw
def poly_profile(p):
 if not p:return dict(zero=True,terms=0)
 dd=p.to_dict();digest=hashlib.sha256();length=0
 for mm,co in sorted(dd.items()):
  raw=(json.dumps([list(map(int,mm)),str(co)],separators=(',',':'))+'\n').encode()
  digest.update(raw);length+=len(raw)
 return dict(degrees=list(map(int,p.degrees()[:5])),
             totalDegree=int(p.total_degree()),terms=len(dd),
             definitionEncoding='one sorted [eight-exponents,QQ-coefficient] JSON per line',
             bytes=length,sha256=digest.hexdigest())
def scalar_check(c):
 c=R(c)
 for p in [c.n,c.d]:
  assert all(not any(mm[j] for j in range(2,8)) for mm in p.to_dict())
 pay(c.d)
 return c
def scalar_profile(c):
 c=scalar_check(c)
 return dict(numerator=poly_profile(c.n),denominator=poly_profile(c.d))
def lpoly_coeffs(p):
 cc={}
 for mm,c in p.to_dict().items():
  assert mm[2]==mm[3]==mm[5]==mm[6]==mm[7]==0
  j=int(mm[4]);cc[j]=cc.get(j,zero)+c*ep**int(mm[0])*kp**int(mm[1])
 return [cc.get(j,zero) for j in range(max(cc,default=-1)+1)]
# Cancel a factor of ALL ACTUAL SOURCE MULTIPLIERS, never an equation
# or an unproved unit. The normalized polynomial identity is global.
omega=inp['cof'];original_three_rows=inp['A']
source_common=next(c for c in omega if c)
for c in omega:
 if c:source_common=source_common.gcd(c)
source_common=source_common/source_common.coefficient(0)
normalized_omega=[]
for c in omega:
 qq=c/source_common;assert qq*source_common==c
 normalized_omega.append(qq)
C=sum((normalized_omega[i]*original_three_rows[i][0] for i in range(3)),zero)
assert C and C*source_common==Craw
for j in range(3):
 assert sum((normalized_omega[i]*original_three_rows[i][j] for i in range(3)),zero)==C*int(j==0)
say(stage='new_value_cofactor_common_multiplier_global_cancellation',
 sourceMultiplierCommon=poly_profile(source_common),
 normalizedOriginalPolynomial=poly_profile(C),
 allThreeMultiplierDivisionsAndAllThreeOriginalColumnsReturned=True,
 exactOriginalTraceDefinition='Cstar=sum_i normalized_omega_i*returned_original_eight_term_row_trace_i',
 allSourceCommonZeroFibresIncluded=True,
 sourceCommonNotDeclaredUnit=True,noOriginalEquationDividedAsIdealOperation=True,
 originalC8EqualsSourceCommonTimesCstar=True,wholeWExcluded=False)
cs=lpoly_coeffs(C)
g=next(c for c in cs if c)
gcd_steps=0
for c in cs:
 if c:
  g=g.gcd(c);gcd_steps+=1
g=g/g.coefficient(0)
assert g
pc=[]
for c in cs:
 q=c/g
 assert q*g==c
 pc.append(q)
P=C/g;assert P*g==C and lpoly_coeffs(P)==pc
G,U,paid_history=strip(g)
assert G*U==g and U*G*P==C
pay(U)
assert all(not any(mm[j] for j in range(2,8)) for mm in G.to_dict())
say(stage='new_original_Cstar_complete_lambda_content',
 originalLambdaDegree=len(cs)-1,exactQQWeightContent=poly_profile(g),
 actualContentGcdSteps=gcd_steps,
 paidContentRemoved=paid_history,paidPart=poly_profile(U),
 unpaidWholeContent=poly_profile(G),primitiveLambdaPolynomial=poly_profile(P),
 completeNineCoefficientAndWholePolynomialProductsReturned=True,
 exactIdentity='Cstar=U_paid*G_unpaid*P',
 originalIdealContainsProductNotPrimitivePart=True,
 wholeGZeroFibreRetained=True,
 noUnpaidContentOrLambdaHeadInverted=True,
 oldC8R5DivisionOrOldLargeGateExecuted=False,wholeWExcluded=False)
# Only the already proved monic coefficient definition is needed to
# construct this NEW finite-algebra multiplication/norm.
ch=frozen_prefix(
 '2026-11-28-unit211-W-global-physical-lambda-six-characteristic-original-input-8542.py',
 '563ef7c9682a4b52f30bea024a391588c747fd97b0a2e8a6c1a4f14a49ec2d65',
 b'# Strip only these TWO',8601,
 'ce868f00596f420d1a46a1503e2432be7bd13f0001e8ebc3e0cd68a53092fc7a',
 'only_original_monic_lambda_six_for_new_value_norm')
chi=[scalar_check(R(c.n,c.d)) for c in ch['chi']]
assert len(chi)==7 and chi[-1]==1
def trim(a):
 while a and not a[-1]:a.pop()
 return a
def padd(a,b):
 return trim([(a[j] if j<len(a) else R())+(b[j] if j<len(b) else R())
              for j in range(max(len(a),len(b)))])
def pmul(a,b):
 if not a or not b:return []
 ans=[R() for _ in range(len(a)+len(b)-1)]
 for i,c in enumerate(a):
  for j,d in enumerate(b):ans[i+j]+=c*d
 return trim(ans)
def monic_divide(cs):
 cs=trim(cs[:]);rem=cs[:];quot=[R() for _ in range(max(0,len(cs)-6))]
 while len(rem)>=7:
  j=len(rem)-7;lead=rem[-1];quot[j]+=lead
  for i in range(7):rem[j+i]-=lead*chi[i]
  trim(rem)
 quot=trim(quot)
 assert padd(pmul(quot,chi),rem)==cs
 for c in quot+rem:scalar_check(c)
 return quot,rem
QP,r=monic_divide([R(c) for c in pc])
say(stage='new_primitive_value_input_in_same_monic_lambda_six',
 primitiveDegree=len(pc)-1,quotientDegree=len(QP)-1,remainderDegree=len(r)-1,
 primitiveRemainderCoefficientProfiles=[scalar_profile(c) for c in r],
 completeNewPrimitiveDivisionProductReturned=True,
 exactIdentity='P=QP*chi6+r',
 originalNecessaryRelation='G_unpaid*r in I8',
 allUnpaidContentAndRemainderHeadZeroFibresRetained=True,wholeWExcluded=False)
if not r:
 say(stage='new_primitive_norm_is_identically_zero_from_zero_remainder',
     noNewWeightConstraintClaimed=True,wholeGZeroFibreRetained=True,
     wholeWExcluded=False,ordinaryISPClaim=False)
 signal.setitimer(signal.ITIMER_REAL,0);signal.alarm(0);raise SystemExit(0)
# Column j is r*lambda^j in the ACTUAL monic quotient.  Keep the
# monic-division quotient for every column: these are polynomial
# identities over the paid ring, not numerical or free-original-module claims.
columns=[];column_quotients=[];scales=[]
for j in range(6):
 qj,mj=monic_divide([R()]*j+r)
 column_quotients.append(qj)
 mj=mj+[R()]*(6-len(mj))
 den=one
 for c in mj:
  gg=den.gcd(c.d);qq=c.d/gg
  assert gg*qq==c.d
  den*=qq
 pay(den)
 pp=[]
 for c in mj:
  qq=den/c.d;assert qq*c.d==den
  pp.append(c.n*qq)
 first=next((c for c in pp if c),None)
 if first is None:
  columns.append([zero]*6);scales.append(R(1))
  say(stage='new_value_norm_zero_multiplication_column',column=j,
      actualSixColumnCoefficientsZero=True,wholeWExcluded=False)
  continue
 common=first
 for c in pp:
  if c:common=common.gcd(c)
 unproved,removed,hist=strip(common)
 assert common==unproved*removed
 pay(removed)
 clean=[c/removed for c in pp]
 assert all(clean[i]*removed==pp[i] for i in range(6))
 rational=next(c for c in clean if c).coefficient(0)
 clean=[c/rational for c in clean]
 scale=R(den,removed)/rational
 scalar_check(scale);pay(scale.n)
 assert all(R(clean[i])==scale*mj[i] for i in range(6))
 columns.append(clean);scales.append(scale)
 say(stage='new_primitive_value_actual_monic_quotient_multiplication_column',
     column=j,actualDivisionIdentity='lambda^j*r=qj*chi6+mj',
     completePolynomialDivisionAndAllSixColumnScaleProductsReturned=True,
     paidColumnCommonRemoved=hist,
     retainedUnpaidColumnCommon=poly_profile(unproved),
     polynomialColumnProfiles=[poly_profile(c) for c in clean],
     onlyPaidWeightColumnScale=True,unpaidColumnContentNotDivided=True,
     wholeWExcluded=False)
A=[[columns[j][i] for j in range(6)] for i in range(6)]
# Fraction-free elimination with ONE augmented target e0.
# Every division is an exact polynomial quotient and is multiplied back.
# Final adjugate-column identity is returned on ALL six original columns.
# Thus temporary pivots do not become open conditions.
division_products=0
def original_constant_cofactor(mat):
 global division_products
 n=6
 work=[list(mat[i])+[ctx.constant(int(i==0))] for i in range(n)]
 previous=one;sign=1
 for k in range(n-1):
  pivot=next((i for i in range(k,n) if work[i][k]),None)
  if pivot is None:
   return zero,None,dict(zeroColumnAt=k)
  if pivot!=k:
   work[k],work[pivot]=work[pivot],work[k];sign=-sign
  lead=work[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n+1):
    numerator=lead*work[i][j]-work[i][k]*work[k][j]
    quotient=numerator/previous
    assert quotient*previous==numerator
    work[i][j]=quotient;division_products+=1
   work[i][k]=zero
  previous=lead
  say(stage='new_value_norm_fraction_free_original_cofactor_step',
      step=k,allExactDivisionProductsSoFar=division_products,
      pivotDegrees=list(map(int,lead.degrees()[:2])),
      pivotTerms=len(lead.to_dict()),allPivotZeroFibresRetained=True,
      noUnitOrWeightCurveYetClaimed=True)
 rawdet=work[n-1][n-1]
 if not rawdet:return zero,None,dict(lastDeterminantZero=True)
 v=[zero]*n
 for i in range(n-1,-1,-1):
  numerator=rawdet*work[i][n]-sum((work[i][j]*v[j] for j in range(i+1,n)),zero)
  quotient=numerator/work[i][i]
  assert quotient*work[i][i]==numerator
  v[i]=quotient;division_products+=1
 det=rawdet*sign;v=[c*sign for c in v]
 for i in range(n):
  assert sum((mat[i][j]*v[j] for j in range(n)),zero)==det*int(i==0)
 return det,v,dict(allSixOriginalCofactorColumnProductsReturned=True)
norm_scaled,cofactor,detail=original_constant_cofactor(A)
if not norm_scaled:
 say(stage='new_same_value_finite_algebra_norm_identically_zero',
     completeFractionFreeProducts=division_products,
     determinantStatus=detail,noNewWeightConstraintClaimed=True,
     wholeGZeroFibreRetained=True,wholeWExcluded=False,ordinaryISPClaim=False)
 signal.setitimer(signal.ITIMER_REAL,0);signal.alarm(0);raise SystemExit(0)
# If B=sum_j scale_j*cofactor_j*lambda^j, the six ACTUAL column
# division identities and A*cofactor=N*e0 prove
# r*B-N=chi*sum_j scale_j*cofactor_j*qj.
# Combining Cstar=U*G*(QP*chi+r) yields G*N in I8.
# No expanded huge final source trace or universal matrix freeness is claimed.
norm_remaining,norm_paid,norm_history=strip(norm_scaled)
assert norm_remaining*norm_paid==norm_scaled
pay(norm_paid)
scale_product=R(1)
for t in scales:
 scale_product*=t;scalar_check(scale_product);pay(scale_product.n)
say(stage='new_whole_W_original_value_lambda_content_and_norm_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 actualMonicFreeEnvironmentRank=6,
 originalCoordinateModuleFreenessNotAssumed=True,
 actualNormScaledPolynomial=poly_profile(norm_scaled),
 actualNormScale=scalar_profile(scale_product),
 exactNormIdentity='det(A)=(product_j scale_j)*Norm(P mod chi6)',
 completeOriginalCofactorReturn=detail,
 completeExactPolynomialDivisionProducts=division_products,
 actualSourceCombinationDefinition='B=sum_j scale_j*cofactor_j*lambda^j',
 actualReturnedIdentity='r*B-det(A)=chi6*sum_j scale_j*cofactor_j*qj',
 globalOriginalIdealIdentity='G*det(A)=U^(-1)*B*Cstar-chi6*G*(B*QP+sum_j scale_j*cofactor_j*qj)',
 originalIdeal='I8=(E1,EBe,EBo,N1,NS,PS,R4,C4) over only previously paid weight ring',
 paidNormFactorsRemoved=norm_history,
 unpaidWholeContent=poly_profile(G),
 remainingNormWeightPolynomial=poly_profile(norm_remaining),
 globalNecessaryWeightProductDefinition='G_unpaid*remainingNormWeightPolynomial',
 productOriginalIdealIdentityAfterOnlyPaidWeightUnits=True,
 noUnpaidLambdaContentLeadingOrTemporaryPivotInverted=True,
 wholeGZeroAndNormZeroFibresRetained=True,
 noCoefficientPayloadOrEncodingOrCacheSaved=True,
 wholeWExcluded=(G.total_degree()==0 and norm_remaining.total_degree()==0),
 ordinaryISPClaim=False,
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.setitimer(signal.ITIMER_REAL,0);signal.alarm(0)
