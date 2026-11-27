#!/usr/bin/env python3
"""NEW whole-W original six binary cubics in (lambda,S), over WEIGHTS only.
Use the paid canonical F rows, then transform original qF to F^2+dF+E.
Four new same-point overlaps have explicit complete original multipliers.
No q3-denominator is used in these six cubics. Keep original q3 and every
other N/P condition separately. Inspect new weight-only binary cubic
heads; if a head determinant is already paid, return its four rules and
all twelve true multiplication columns. No freedom of the final quotient
is assumed. All unpaid head-zero fibres stay. No old cofactor/resultant
or complete NS/NV gate replay. 180 seconds / 4 GiB."""
import json,time,hashlib,signal,resource,contextlib,io,math,itertools
from pathlib import Path
start=time.perf_counter();deadline=start+180;signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**r):
 r['seconds']=time.perf_counter()-start
 print(json.dumps(r,separators=(',',':')),flush=True)
dep=Path(__file__).with_name('2026-11-28-unit211-W-canonical-three-original-F-rows-and-S-affine-8542.py')
raw=dep.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='a8cbbc7c4300b3c9d5ad9839daf6e487e0107e68a951d0f59523d4955b46c265'
marker=b"\nsay(stage='new_W_canonical_three_original_rows_exact_ideal_identity',"
assert raw.count(marker)==1
prefix=raw.split(marker)[0]
assert hashlib.sha256(prefix).hexdigest()=='c0b0e212bd28341792645647c4e72b64d205e3795e7bf701756770f6c5226fad'
inp={'__file__':str(dep),'__name__':'__canonical_construction_only_for_new_binary_cubics__'}
with contextlib.redirect_stdout(io.StringIO()):
 exec(compile(prefix,str(dep),'exec'),inp)
signal.alarm(max(1,math.ceil(deadline-time.perf_counter())))
base=inp['ns']
C,P,ctx,F,S,lam,acan,rcan,prof,paid,ppaid,det,Fp,Flin=[
 inp[x] for x in ['C','P','ctx','F','S','lam','acan','rcan','prof','paid','ppaid','det','Fp','Flin']]
qF=base['qF'];q3=inp['q3'];strip_paid=base['strip_paid']
ep,kp,lp=ctx.gens();zero=ctx.constant(0);one=ctx.constant(1)
x=P(lam);y=S
A,B,Cc=acan
def weight_cl(cf,power):
 cf=C(cf);assert cf.d.degrees()[2]<=0
 out=zero
 for mm,v in cf.n.to_dict().items():
  if int(mm[2])==power:out+=v*ep**int(mm[0])*kp**int(mm[1])
 ans=C(out,cf.d)
 assert ans.n.degrees()[2]<=0 and ans.d.degrees()[2]<=0
 paid(ans);return ans
def binary(pp,bound):
 pp=P(pp);out={}
 for (ff,j),cf in pp.t.items():
  assert ff==0 and cf.d.degrees()[2]<=0
  for i in range(max(0,int(cf.n.degrees()[2]))+1):
   v=weight_cl(cf,i)
   if v:
    assert i+j<=bound
    out[(i,j)]=out.get((i,j),C())+v
 back=sum(((x**i)*(y**j).scale(v) for (i,j),v in out.items()),P())
 assert back==pp
 return out
abc=[binary(p,2) for p in [A,B,Cc]]
# Preserve the entire original qF; remove only its F*lambda and F*S
# coefficients by the two true canonical original rows.
p=P();q=P()
for (ff,j),cf in qF.t.items():
 if ff==2:
  assert j==0 and cf==1
 elif ff==1:p+=P.monomial((0,j),cf)
 else:
  assert ff==0;q+=P.monomial((0,j),cf)
pd=binary(p,1);binary(q,2)
d=pd.get((0,0),C());px=pd.get((1,0),C());py=pd.get((0,1),C())
assert p==P(d)+x.scale(px)+y.scale(py)
E=q-B.scale(px)-Cc.scale(py)
binary(E,2);ppaid(E)
rF2=F*F+F.scale(d)+E
assert rF2==qF-rcan[1].scale(px)-rcan[2].scale(py)
say(stage='new_W_binary_original_F_square_canonical_identity',
 entireOriginalQFPolynomialProductReturned=True,
 identity='F^2+d*F+E=qF-p_lambda*Rcan1-p_S*Rcan2',
 dOnlyWeights=True,EActualLambdaSDegreeAtMostTwo=True,
 A_B_C_E_ScalarDenominatorsOnlyPaidWeights=True,
 noPhysicalDOrGeometryOrNormInverse=True)
def F_times_quad(p0,coeff,label):
 v=lambda i,j:coeff.get((i,j),C())
 h1=x.scale(v(2,0))+y.scale(v(1,1))+P(v(1,0))
 h2=y.scale(v(0,2))+P(v(0,1))
 pure=-(x*B).scale(v(2,0))-(y*B).scale(v(1,1))-(y*Cc).scale(v(0,2))-B.scale(v(1,0))-Cc.scale(v(0,1))
 assert F*p0==pure+F.scale(v(0,0))+h1*rcan[1]+h2*rcan[2]
 binary(pure,3)
 say(stage='new_W_binary_original_F_quadratic_overlap_product',
     label=label,completeOriginalProductReturned=True,
     identity='F*P=pure+p00*F+h1*Rcan1+h2*Rcan2',
     certificate=base['digest']([pure,h1,h2]),allScalarDenominatorsOnlyWeights=True)
 return pure,h1,h2,v(0,0)
tA,a1,a2,a0=F_times_quad(A,abc[0],'A')
tB,b1,b2,b0=F_times_quad(B,abc[1],'B')
tC,c1,c2,c0=F_times_quad(Cc,abc[2],'C')
h0=B-x*A
h1=Cc-y*A
h2=x*Cc-y*B
h3=E+A.scale(a0-d)-tA
h4=x*E+A.scale(b0)-B.scale(d)-tB
h5=y*E+A.scale(c0)-Cc.scale(d)-tC
assert h0==rcan[1]-x*rcan[0]
assert h1==rcan[2]-y*rcan[0]
assert h2==x*rcan[2]-y*rcan[1]
assert -h3==F*rcan[0]-rF2-a1*rcan[1]-a2*rcan[2]-rcan[0].scale(a0-d)
assert -h4==F*rcan[1]-x*rF2-b1*rcan[1]-b2*rcan[2]+rcan[1].scale(d)-rcan[0].scale(b0)
assert -h5==F*rcan[2]-y*rF2-c1*rcan[1]-c2*rcan[2]+rcan[2].scale(d)-rcan[0].scale(c0)
cubics=[h0,h1,h2,h3,h4,h5]
names=['B-lambda*A','C-S*A','lambda*C-S*B','F_times_Rcan0_minus_Fsquare',
       'F_times_Rcan1_minus_lambda_Fsquare','F_times_Rcan2_minus_S_Fsquare']
coeffs=[binary(p,3) for p in cubics]
for p in cubics:ppaid(p)
columns=[(3,0),(2,1),(1,2),(0,3)]
head_raw=[[co.get(mm,C()) for mm in columns] for co in coeffs]
def primitive_head(vals,p0):
 # A unit rescaling is chosen from the head alone. Every coefficient of
 # the scaled WHOLE polynomial is still checked for paid denominators.
 den=one
 for cf in vals:
  gg=den.gcd(cf.d);div=den/gg;assert div*gg==den;den=div*cf.d
 nums=[]
 for cf in vals:
  div=den/cf.d;assert div*cf.d==den
  nums.append(cf.n*div)
 common=next((v for v in nums if v),None)
 if common is None:
  return nums,p0,dict(zeroHead=True)
 for v in nums:
  if v:common=common.gcd(v)
 left,removed=strip_paid(common)
 norm=[]
 for v in nums:
  div=v/removed;assert div*removed==v;norm.append(div)
 scalar=C(den,removed);paid(scalar)
 scaled=p0.scale(scalar);ppaid(scaled)
 cc=binary(scaled,3)
 assert all(cc.get(mm,C())==C(norm[j]) for j,mm in enumerate(columns))
 return norm,scaled,dict(paidCommonDenominator=prof(den),
   onlyPaidHeadContentRemoved=prof(removed),fullPolynomialUnitRescalingReturned=True)
head=[];scaled=[];normalization=[]
for vals,p0 in zip(head_raw,cubics):
 vv,pp,rr=primitive_head(vals,p0);head.append(vv);scaled.append(pp);normalization.append(rr)
def pdata(p):
 return [[list(map(int,mm)),str(cf)] for mm,cf in sorted(p.to_dict().items())]
say(stage='new_W_six_binary_cubics_complete_original_identities',
 scalarVariables=['e','k'],geometricVariables=['lambda','S'],
 originalCubics=names,headColumns=['lambda^3','lambda^2*S','lambda*S^2','S^3'],
 allSixCompleteOriginalPolynomialIdentitiesReturned=True,
 completeActualFQuadraticOverlapsReturned=True,
 actualCubicProfiles=[base['pprofile'](p) for p in cubics],
 headProfiles=[[prof(v) for v in row] for row in head],headNormalization=normalization,
 originalQFKeptThroughItsExactCanonicalF2Identity=True,
 originalQ3AndAllRemainingNPStillRequired=True,
 allCoefficientDenominatorsOnlyAlreadyPaidWeights=True,
 noOriginalQuotientFreedomAssumed=True,wholeWExcluded=False)
# Only the mathematical definition, byte count and digest are output.
# No encoded/chunked coefficient payload or regenerable cache is produced.
head_data=json.dumps(dict(variables=['e','k','lambda'],lambdaExponentAlwaysZero=True,
 rows=names,columns=['lambda^3','lambda^2*S','lambda*S^2','S^3'],
 coefficientData=[[pdata(v) for v in row] for row in head],
 normalization=normalization),separators=(',',':')).encode()
say(stage='new_W_exact_binary_weight_head_definition_and_hash',
    definition='four total-degree-three coefficients of the six explicit original cubics; normalize only by paid weight units',
    bytes=len(head_data),sha256=hashlib.sha256(head_data).hexdigest(),
    encodedOrChunkedDataOutput=False,coefficientCacheWritten=False)
del head_data
def detpoly(mat):
 n=len(mat);ans=zero
 for perm in itertools.permutations(range(n)):
  z=one
  for i,j in enumerate(perm):z=z*mat[i][j]
  if sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))%2:ans-=z
  else:ans+=z
 return ans
combos=list(itertools.combinations(range(6),4))
# A fixed size ordering, selected before any determinant result.
combos.sort(key=lambda ids:(sum(len(head[i][j].to_dict()) for i in ids for j in range(4)),ids))
chosen=None;records=[]
for ids in combos:
 mat=[head[i] for i in ids]
 delta=detpoly(mat)
 if not delta:
  records.append(dict(rows=list(ids),determinantZero=True))
  say(stage='new_W_binary_weight_head_minor_zero',rows=list(ids))
  continue
 rem,removed=strip_paid(delta)
 scalar=rem.coefficient(0);rem=rem/scalar;removed*=scalar
 assert rem*removed==delta
 allpaid=rem.total_degree()==0
 rec=dict(rows=list(ids),determinantZero=False,rawProfile=prof(delta),
          unpaidRemainingHead=prof(rem,True),alreadyPaidUnit=allpaid,
          completePaidFactorProductReturned=True)
 records.append(rec)
 say(stage='new_W_binary_weight_head_minor_actual_return',**rec,
     allUnpaidMinorZeroFibresRetained=True)
 if allpaid:
  chosen=(ids,mat,delta);break
if chosen is not None:
 ids,mat,delta=chosen
 iv=[]
 for i in range(4):
  row=[]
  for j in range(4):
   mm=[[mat[r][c] for c in range(4) if c!=i] for r in range(4) if r!=j]
   cc=detpoly(mm)*((-1)**(i+j))
   v=C(cc,delta);paid(v);row.append(v)
  iv.append(row)
 for i in range(4):
  for j in range(4):
   assert sum((iv[i][h]*C(mat[h][j]) for h in range(4)),C())==C(int(i==j))
   assert sum((C(mat[i][h])*iv[h][j] for h in range(4)),C())==C(int(i==j))
 monomials=[(x**i)*(y**j) for i,j in columns]
 rules=[sum((scaled[ids[h]].scale(iv[j][h]) for h in range(4)),P()) for j in range(4)]
 lower=[rules[j]-monomials[j] for j in range(4)]
 for p in lower:binary(p,2);ppaid(p)
 bs=[(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]
 basis=[(x**i)*(y**j) for i,j in bs]
 multiplications=[]
 for variable,var in [('lambda',x),('S',y)]:
  for j,bp in enumerate(basis):
   pp=var*bp;co=binary(pp,3);rem=pp;combo=P()
   for h,mm in enumerate(columns):
    cf=co.get(mm,C())
    rem-=rules[h].scale(cf);combo+=rules[h].scale(cf)
   binary(rem,2);ppaid(rem);assert pp==rem+combo
   multiplications.append(rem)
 say(stage='new_W_binary_global_six_generator_original_rules_returned',
     chosenHeadRows=list(ids),allThirtyTwoHeadInverseProductsReturned=True,
     allFourFullOriginalCubicRulesReturned=True,
     actualGenerators=['1','lambda','S','lambda^2','lambda*S','S^2'],
     allTwelveTrueMultiplicationColumnProductsReturned=True,
     originalRuleAndColumnCertificate=base['digest'](rules+multiplications),
     onlyPaidWeightDenominators=True,
     sixGeneratorsNotClaimedFreeInOriginalQuotient=True,
     originalQ3AndEveryNPConditionStillRequired=True,wholeWExcluded=False)
else:
 say(stage='accurate_W_new_binary_head_chart_zero_fibres_retained',
     allFifteenWeightHeadMinorsProcessed=True,
     noSingleGloballyPaidHeadReturned=True,
     noOriginalDegreeThreeReductionClaimOutsideActualPrincipalOpens=True,
     entireAllHeadMinorsZeroFibreRetained=True,wholeWExcluded=False)
say(stage='new_W_six_original_binary_cubics_and_weight_head_attempt_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 numberOfActualHeadMinors=len(records),headMinorRecords=records,
 globalSixGeneratorRulesActuallyReturned=(chosen is not None),
 noOldC9CofactorNSNVOrResultantGateReplayed=True,
 noNewUnpaidHeadOrPhysicalDInverse=True,
 largeRegenerableOriginalMatrixCachesWritten=False,
 wholeWExcluded=False,ordinaryISPClaim=False,
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)
