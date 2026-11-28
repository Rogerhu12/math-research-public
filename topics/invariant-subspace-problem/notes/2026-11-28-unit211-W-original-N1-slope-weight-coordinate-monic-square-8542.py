#!/usr/bin/env python3
"""NEW N1 slope coordinate: a pure WEIGHT 2x2 determinant and monic z^2.
Use only the necessary three original mean rules, not any old cofactor,
module, norm, or resultant gate. Reduce the actual original N1 to
p0+(a*lambda+b)*x+(c*lambda+d)*y. Set DeltaN=a*d-b*c,z=a*x+c*y.
Both coordinate identities are global original polynomial identities.
On the explicit DeltaN!=0 chart, x,y recover without a geometric inverse.
The three actual mean rules then give monic z^2, with full I4 source.
All DeltaN=0 weight fibres remain unless already-paid factors exhaust it.
180 seconds /4GiB. Only small definitions/profiles/actual returns retained.
"""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
started=time.perf_counter();deadline=started+180
signal.alarm(180);resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**kw):
 kw['seconds']=time.perf_counter()-started
 print(json.dumps(kw,separators=(',',':')),flush=True)
path=Path(__file__).with_name(
 '2026-11-28-unit211-W-K7-open-physical-lambda-original-three-column-projection-binding-corrected-8542.py')
raw=path.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='7cf3ff802cdf8166e3fb96f3ea806b81b83570f9200d10fad11caa13862f2c3f'
marker=b'\nrows=[];rowtags=[];labels=[]';assert raw.count(marker)==1
prefix=raw.split(marker)[0]
assert len(prefix)==5833 and hashlib.sha256(prefix).hexdigest()=='8ea50cb422b81b5976bbb132e01809135ebbaedc06d545bcdb0c741fec4e3ff4'
tri={'__file__':str(path),'__name__':'only_three_original_mean_rules_for_new_N1_slope_coordinate'}
saved_alarm=signal.alarm
def bounded_alarm(seconds):
 remaining=max(.001,deadline-time.perf_counter())
 previous=signal.setitimer(signal.ITIMER_REAL,min(remaining,float(seconds) if seconds>0 else remaining))
 return math.ceil(previous[0])
signal.alarm=bounded_alarm
try:
 with contextlib.redirect_stdout(io.StringIO()):
  exec(compile(prefix,str(path)+'#new_N1_coordinate_necessary_prefix','exec'),tri)
finally:signal.alarm=saved_alarm
signal.setitimer(signal.ITIMER_REAL,max(.001,deadline-time.perf_counter()))
R=tri['R'];ctx=tri['ctx'];zero=tri['zero'];one=tri['one']
ep,kp,xp,yp,Lp,Zp=ctx.gens()[:6]
x,y,L=tri['xx'],tri['yy'],tri['L'];Z=R(Zp)
pay=tri['pay'];strip=tri['strip'];original=tri['original']
def profile(p):
 if not p:return dict(zero=True,terms=0)
 dd=p.to_dict();hh=hashlib.sha256();length=0
 for mm,c0 in sorted(dd.items()):
  rr=(json.dumps([list(map(int,mm)),str(c0)],separators=(',',':'))+'\n').encode()
  hh.update(rr);length+=len(rr)
 return dict(degrees=list(map(int,p.degrees()[:6])),totalDegree=int(p.total_degree()),
             terms=len(dd),bytes=length,sha256=hh.hexdigest())
def rp(c):return dict(numerator=profile(c.n),denominator=profile(c.d))
def coefficients_lambda(c):
 pay(c.d);out={}
 for mm,q in c.n.to_dict().items():
  assert mm[2]==mm[3]==mm[5]==mm[6]==mm[7]==0
  j=int(mm[4]);out[j]=out.get(j,zero)+q*ep**int(mm[0])*kp**int(mm[1])
 return {j:R(q,c.d) for j,q in out.items() if q}
nrow,ntag=tri['reduce_row'](original[3],[R(int(j==3)) for j in range(6)])
p0,p1,p2=nrow
Nrow=p0+p1*x+p2*y
assert Nrow==sum((ntag[j]*original[j] for j in range(6)),R())
assert not ntag[4] and not ntag[5]
lc0,lc1,lc2=[coefficients_lambda(c) for c in nrow]
assert max(lc0,default=-1)<=2 and max(lc1,default=-1)<=1 and max(lc2,default=-1)<=1
a,b=lc1.get(1,R()),lc1.get(0,R())
c,d=lc2.get(1,R()),lc2.get(0,R())
assert p1==a*L+b and p2==c*L+d
Delta=a*d-b*c
for co in [a,b,c,d,Delta]:
 pay(co.d)
 assert all(not any(mm[j] for j in range(2,8)) for pp in [co.n,co.d] for mm in pp.to_dict())
z=a*x+c*y
# These identities retain Nrow itself; no pointwise cancellation.
assert Delta*x==p2*z+c*p0-c*Nrow
assert Delta*y==-p1*z-a*p0+a*Nrow
say(stage='new_W_original_N1_slope_two_by_two_weight_identity',
 actualN1RowIdentityReturned=True,allOriginalN1GermTermsPreserved=True,
 rowLambdaDegrees=[max(lc0,default=-1),max(lc1,default=-1),max(lc2,default=-1)],
 scalarCoordinateDefinition='z=a*x+c*y',
 slopeCoefficientProfiles=[rp(t) for t in [a,b,c,d]],
 pureWeightDeterminant=rp(Delta),
 bothGlobalPolynomialCoordinateProductsReturned=True,
 exactIdentities=['DeltaN*x=p2*z+c*p0-c*Nrow',
                  'DeltaN*y=-p1*z-a*p0+a*Nrow'],
 noOriginalEquationOrGeometricLeadingFactorDivided=True,
 wholeWExcluded=False)
if not Delta:
 say(stage='accurate_new_N1_slope_weight_determinant_identically_zero',
     twoGeneratorChartNotObtained=True,
     originalN1AndAllWeightFibresRetained=True,
     noOtherCoordinateOrSameNormRetryExecuted=True,
     ordinaryISPClaim=False,wholeWExcluded=False)
 signal.setitimer(signal.ITIMER_REAL,0);signal.alarm(0);raise SystemExit(0)
remaining,paidpart,hist=strip(Delta.n)
assert paidpart*remaining==Delta.n
pay(paidpart);pay(Delta.d)
whole=(remaining.total_degree()==0)
scalar,factors=remaining.factor();back=ctx.constant(scalar);fac_profiles=[]
for fac,power in factors:
 power=int(power);back*=fac**power
 fac_profiles.append(dict(power=power,definition=profile(fac)))
assert back==remaining
say(stage='new_N1_slope_weight_determinant_complete_QQ_support',
 paidFactorLabelsAndCounts=hist,remainingWholeWeightFactor=profile(remaining),
 completeQQFactorScalar=str(scalar),completeQQFactors=fac_profiles,
 allFactorProductsActuallyReturned=True,
 DeltaNAlreadyPaidOnWholeCurrentW=whole,
 entireUnpaidDeltaNZeroFibreRetained=(not whole),
 noModularRankOrSampleEmptinessUsed=True,wholeWExcluded=False)
def pay_chart(p):
 assert p
 rest,removed,h=strip(p);assert rest*removed==p
 while rest.total_degree()>0:
  gg=rest.gcd(Delta.n)
  assert gg.total_degree()>0,'new denominator beyond explicit DeltaN chart'
  qq=rest/gg;assert qq*gg==rest
  rest=qq
 assert rest
def legal(c):
 assert all(not any(mm[j] for j in range(2,8)) for mm in c.d.to_dict())
 for pp in [c.n,c.d]:
  assert all(mm[6]==mm[7]==0 for mm in pp.to_dict())
 pay_chart(c.d);return c
xhat=(p2*Z+c*p0)/Delta
yhat=(-p1*Z-a*p0)/Delta
legal(xhat);legal(yhat)
assert a*xhat+c*yhat==Z
assert p0+p1*xhat+p2*yhat==0
# Full source for the square rule: reduce z^2 by the three original means.
zr,ztag=tri['reduce_row'](z*z)
assert not ztag[3] and not ztag[4] and not ztag[5]
assert zr[0]+zr[1]*x+zr[2]*y-z*z==sum((ztag[j]*original[j] for j in range(6)),R())
qZ=Z*Z-zr[0]-zr[1]*xhat-zr[2]*yhat
legal(qZ)
def zcoeff(rr):
 out={}
 for mm,co in rr.n.to_dict().items():
  assert mm[2]==mm[3]==mm[6]==mm[7]==0
  j=int(mm[5])
  out[j]=out.get(j,zero)+co*ep**int(mm[0])*kp**int(mm[1])*Lp**int(mm[4])
 return {j:R(po,rr.d) for j,po in out.items() if po}
zcs=zcoeff(qZ)
assert max(zcs)==2 and zcs[2]==1
beta0,beta1=zcs.get(0,R()),zcs.get(1,R())
# beta denominators can include DeltaN only in the stated complement;
# check lambda degrees directly without calling the global pay function.
for co,bound in [(beta0,3),(beta1,2)]:
 legal(co)
 assert all(not any(mm[j] for j in [2,3,5,6,7]) for mm in co.n.to_dict())
 assert all(mm[4]<=bound for mm in co.n.to_dict())
# Evaluate the FORMAL z polynomial at the original a*x+c*y exactly.
qZ_at_original=sum((co*z**j for j,co in zcs.items()),R())
correction=(a*zr[2]-c*zr[1])/Delta
qtag=[-ztag[j]+correction*ntag[j] for j in range(6)]
assert not qtag[4] and not qtag[5]
assert qZ_at_original==sum((qtag[j]*original[j] for j in range(6)),R())
for co in qtag:legal(co)
say(stage='new_W_N1_slope_coordinate_monic_square_complete_original_return',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 exactChart=('whole current paid W' if whole else 'explicit DeltaN!=0 only'),
 originalCoordinateRecovery=['x=(p2*z+c*p0)/DeltaN','y=(-p1*z-a*p0)/DeltaN'],
 exactCoordinateEquivalenceModuloActualN1Row=True,
 formalMonicRule='qz=z^2+beta1(lambda)*z+beta0(lambda)',
 coefficientProfiles={'beta0':rp(beta0),'beta1':rp(beta1)},
 originalRuleIdentity='qz(a*x+c*y)=sum_j[-ztag_j+(a*zr2-c*zr1)/DeltaN*ntag_j]*original_j',
 completeOriginalI4SourceActuallyReturned=True,
 bothCoordinateInverseProductsReturned=True,
 allFourOriginalMeanCoefficientsPreserved=True,
 originalMeanQuotientGeneratedOverWeightLambdaRingBy=['1','z'],
 freeRankTwoClaimOnlyForExplicitMonicEnvironment=True,
 originalQuotientFreenessNotAssumed=True,
 wholeCurrentWTwoGeneratorsProved=whole,
 entireUnpaidWeightZeroFibreStillRetained=(not whole),
 noLambdaPhysicalDOrNormInverse=True,
 noFullNSPSOrIndividualValueMatrixYetComputed=True,
 noOldC8NormTwelveResultantOrEighteenModuleExecuted=True,
 noCoefficientPayloadOrEncodedCacheWritten=True,
 wholeWExcluded=False,ordinaryISPClaim=False,
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.setitimer(signal.ITIMER_REAL,0);signal.alarm(0)
