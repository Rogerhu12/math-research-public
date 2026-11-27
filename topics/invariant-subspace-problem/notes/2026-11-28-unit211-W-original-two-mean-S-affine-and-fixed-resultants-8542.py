#!/usr/bin/env python3
"""NEW whole W common-S affine equation from the actual E1/EBe images.
No previous 12-row return or NS/NV cofactor is replayed. Only the frozen
common-F construction is used. Keep all two quadratic-head zeros and
the entire new affine-head-zero fibre. Return two NEW exact necessary
parameter inputs: fixed quadratic/quadratic and linear/monic-cubic
resultants with explicit original multipliers, without any new inverse.
180 seconds /4 GiB. Save only exact parameter chunks, no matrix cache."""
import json,time,hashlib,zlib,base64,signal,resource,contextlib,io,math
from pathlib import Path
start=time.perf_counter();deadline=start+180;signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**r):
 r['seconds']=time.perf_counter()-start
 print(json.dumps(r,separators=(',',':')),flush=True)
dep=Path(__file__).with_name('2026-11-28-unit211-W-G36-nonzero-full-original-three-column-return-8542.py')
raw=dep.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='8430b819844aeecf8bd02619f8724e5c9ab75cad3a7c8c601b943cf515f79351'
marker=b"\nsave('original_qF_substituted'"
assert raw.count(marker)==1
prefix=raw.split(marker)[0]
assert hashlib.sha256(prefix).hexdigest()=='8947c21464310d9eaf4fabe179ce333930dc3e6b03f4fd3a65f02412ec2bb7ac'
ns={'__file__':str(dep),'__name__':'__common_F_construction_only_for_new_affine_input__'}
with contextlib.redirect_stdout(io.StringIO()):
 exec(compile(prefix,str(dep),'exec'),ns)
signal.alarm(max(1,math.ceil(deadline-time.perf_counter())))
C,P,S,q3,ctx,prof,ppaid,primitive,strip_paid=[
 ns[x] for x in ['C','P','S','q3','ctx','prof','ppaid','primitive','strip_paid']]
image=ns['original_image'];original=ns['original'];zero=ctx.constant(0);one=ctx.constant(1)
ep,kp,lp=ctx.gens()
def data(p):return [[list(map(int,mm)),str(cf)] for mm,cf in sorted(p.to_dict().items())]
def exact_input(label,polys,scope):
 obj=dict(variables=['e','k','lambda'],components={n:data(p) for n,p in polys.items()},
          label=label,scope=scope,allUnpaidParameterAndGeometryLeadingZeroFibersRetained=True)
 raw0=json.dumps(obj,separators=(',',':')).encode()
 enc=base64.b64encode(zlib.compress(raw0,9)).decode()
 assert zlib.decompress(base64.b64decode(enc))==raw0
 chunks=[enc[j:j+75000] for j in range(0,len(enc),75000)]
 say(stage='new_W_mean_affine_exact_parameter_input',label=label,rawBytes=len(raw0),
     rawSHA256=hashlib.sha256(raw0).hexdigest(),base64Characters=len(enc),
     maximumChunkCharacters=75000,chunks=len(chunks),
     originalMatrixAndBezoutCacheWritten=False)
 for j,ch in enumerate(chunks):
  say(stage='new_W_mean_affine_exact_parameter_input_chunk',
      label=label,index=j,total=len(chunks),data=ch)
def necessary_parameter(label,cf,origin):
 cf=C(cf);ns['paid'](cf)
 if not cf:
  say(stage='new_W_mean_affine_new_necessary_parameter_identically_zero',
      label=label,origin=origin,noExclusionClaim=True)
  return None
 rem,removed=strip_paid(cf.n);scalar=rem.coefficient(0)
 rem=rem/scalar;removed*=scalar
 assert rem*removed==cf.n
 degree=int(rem.degrees()[2]);head=zero
 for mm,cc in rem.to_dict().items():
  if int(mm[2])==degree:head+=cc*ep**int(mm[0])*kp**int(mm[1])
 hh,paid_h=strip_paid(head);assert hh*paid_h==head
 say(stage='new_W_mean_affine_new_complete_necessary_parameter',
     label=label,origin=origin,remaining=prof(rem,True),
     completeLambdaHeadAfterOnlyPaidStripping=prof(hh,True),
     allClearingAndStrippingProductsActuallyReturned=True,
     allRemainingHeadsRetained=True,wholeWExcluded=False)
 exact_input(label,{'necessaryPolynomial':rem},
  'current whole paid W; original E1/EBe common F and same S, no new affine-head inverse')
 return rem
rr=[];primitives=[]
for name in ['E1','EBe']:
 pp=image('new_affine_original_'+name,original[name])
 row,trace=primitive(pp)
 assert len(row)==3
 rp=sum((P.monomial((0,j),C(row[j])) for j in range(3)),P())
 rr.append(rp);primitives.append(row)
 say(stage='new_W_mean_affine_true_original_quadratic_input',name=name,
     coefficients=[prof(p) for p in row],originalPaidNormalizationTrace=trace,
     completeOriginalQFQ3FLinearTrace=ns['traces']['new_affine_original_'+name],
     noOldParameterCofactorExecuted=True)
f,g=rr
f0,f1,f2=primitives[0];g0,g1,g2=primitives[1]
a=g2*f1-f2*g1;b=g2*f0-f2*g0;c=f1*g0-f0*g1
L=f.scale(g2)-g.scale(f2)
assert L==S.scale(a)+P(b)
assert L.degree()<=1
ppaid(L)
line,normalization=primitive(L)
assert not line[2]
b0,a1=line[0],line[1]
say(stage='new_W_mean_affine_full_original_S_linear_identity',
     identity='L=g2*f-f2*g=a*S+b',
     allOriginalSQuadraticAndLinearProductsActuallyReturned=True,
     bothOriginalSQuadraticLeadingZeroFibersRetained=True,
     primitiveConstant=prof(b0,True),primitiveSHead=prof(a1,True),
     paidNormalization=normalization,
     allNewSHeadZeroFibersRetained=True,
     noNewGeometryParameterOrDInverse=True,
     originalWholeWConditionsNotReplacedByThisNecessaryRow=True)
exact_input('new_original_mean_S_affine',
            {'L0':b0,'L1':a1},
            'whole current W; retain L1=0 together with L0=0 and every original row')
if a1 or b0:
 common=a1.gcd(b0)
 qq0=b0/common;qq1=a1/common
 assert qq0*common==b0 and qq1*common==a1
 say(stage='new_W_mean_affine_complete_common_parameter_factor',
     common=prof(common,True),constantQuotient=prof(qq0),headQuotient=prof(qq1),
     actualTwoFactorProductsReturned=True,
     commonZeroEntireFiberRetained=True,
     commonNotPaidOrRemovedFromOriginalLine=True,
     noMultivariateGcdEmptinessClaim=True)
# This is the fixed original (2,2) resultant, including both degree drops.
# Its explicit degree-one original multipliers are returned in all S columns.
res=b*b+a*c
mf=S.scale(-a*g2)+P(b*g2-a*g1)
mg=S.scale(a*f2)+P(-b*f2+a*f1)
assert mf*f+mg*g==P(res)
say(stage='new_W_mean_affine_original_fixed_four_by_four_resultant_identity',
     fullOriginalSZeroThroughS3ColumnsActuallyReturned=True,
     identity='(b*g2-a*g1-a*g2*S)*f+(-b*f2+a*f1+a*f2*S)*g=b^2+a*c',
     allOriginalSHeadZeroFibersRetained=True,noHeadDivision=True,
     originalCombinationCertificate=ns['digest']([mf,mg]))
necessary_parameter('new_original_two_means_fixed_S_resultant',C(res),
 'actual original quadratic/quadratic four-column constant combination')
# On the original point, a1*S+b0=0 and q3(S)=0. Homogenize the
# substitution, so a1=0 and the simultaneous a1=b0=0 fibre remain.
aa=C(a1);bb=C(b0)
beta2=q3.t.get((0,2),C());beta1=q3.t.get((0,1),C());beta0=q3.t.get((0,0),C())
H=-bb**3+beta2*bb*bb*aa-beta1*bb*aa*aa+beta0*aa**3
qq=S*S
quot=qq.scale(aa*aa)+S.scale(aa*aa*beta2-aa*bb)+P(aa*aa*beta1-aa*bb*beta2+bb*bb)
assert q3.scale(aa**3)-P(H)==(S.scale(aa)+P(bb))*quot
say(stage='new_W_mean_affine_original_linear_cubic_resultant_identity',
     completeHomogenizedOriginalFourColumnProductReturned=True,
     identity='a1^3*q3-H=(a1*S+b0)*explicit_quadratic',
     noA1InverseAndAllZeroHeadFibersRetained=True,
     originalCombinationCertificate=ns['digest']([quot]))
necessary_parameter('new_original_mean_affine_monic_cubic_resultant',H,
 'same original affine row and monic q3 with homogeneous clearing, no a1 inverse')
say(stage='new_W_original_mean_affine_and_two_parameter_resultants_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 allThreeNewOriginalIdentitiesActuallyReturned=True,
 allExactNewNecessaryParameterInputsOutput=True,
 noPreviousNSNVCofactorOrTwelveRowGateReplayed=True,
 allOriginalAffineAndQuadraticHeadZeroFibersRetained=True,
 noPhysicalDInverse=True,wholeWExcluded=False,ordinaryISPClaim=False,
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)
