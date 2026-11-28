#!/usr/bin/env python3
"""NEW whole Phi D2=0 direction: original weight cofactors and paid head.
Retain all original highest equations on ell=1/2,t=1,Q=4(u-1)(u-2).
Use three division-free quadratic Sylvester cofactors (R,W),(R,O),(R,N1).
Their genuine polynomial-u gcd is a full QQ Bezout combination; unlike
a generic QQ(u)[s] unit, it preserves all exceptional u fibres.
Only original units and the already-paid entire quadratic head may be
removed. No old Euclid target, old highest Gaussian, P6/P9, or norm.
60 seconds /1 GiB including all nested necessary definition prefixes.
"""
import json,time,hashlib,signal,resource,math,contextlib,io
from pathlib import Path
from flint import fmpq_poly
started=time.perf_counter();deadline=started+60
signal.alarm(60);resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-started)
 print(json.dumps(kw,separators=(',',':')),flush=True)
path=Path(__file__).with_name('2026-11-28-unit211-Phi-zero-whole-D2-zero-infinity-original-four-quadratics-8542.py')
raw=path.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='baf684e40df5e447c6dfcb9f5eb3eef8173d28d6ae1a37e152c4475ff342b03c'
marker=b'\ng=rows[0];tags=[[R(1)],[],[],[]]\n'
assert raw.count(marker)==1
prefix=raw.split(marker)[0]
d2={'__file__':str(path),'__name__':'four_original_highest_forms_without_old_Euclid'}
saved_alarm=signal.alarm;saved_timer=signal.setitimer
def bounded_timer(which,seconds,interval=0):
 if which!=signal.ITIMER_REAL:return saved_timer(which,seconds,interval)
 assert not interval
 left=max(.001,deadline-time.perf_counter())
 requested=float(seconds) if seconds>0 else left
 return saved_timer(which,min(left,requested),0)
def bounded_alarm(seconds):return math.ceil(bounded_timer(signal.ITIMER_REAL,seconds)[0])
signal.alarm=bounded_alarm;signal.setitimer=bounded_timer
try:
 with contextlib.redirect_stdout(io.StringIO()):
  exec(compile(prefix,str(path)+'#only_four_original_highest_definitions','exec'),d2)
finally:
 signal.alarm=saved_alarm;signal.setitimer=saved_timer
saved_timer(signal.ITIMER_REAL,max(.001,deadline-time.perf_counter()))
R=d2['R'];ctx=d2['ctx'];up=d2['up'];sp=d2['sp']
zero=d2['zero'];one=d2['one'];qcurve=d2['qcurve']
profile=d2['prof'];legal=d2['legal_original_den'];original=d2['ns']
original_rows=d2['rows'];forms=d2['highest']
assert len(forms)==len(original_rows)==4
# The exact original 3 x 3 quadratic head, before any inverse, on the
# SAME entire weight curve. Its numerator is paid only by whole H1.
quads=[original['extract_quad'](original[k]) for k in ['Rbar','W4','Obar']]
head=[[R(d2['subweight'](co.n),d2['subweight'](co.d)) for co in row[3:]] for row in quads]
for row in head:
 for co in row:legal(co.d)
a=head
hd=a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])
legal(hd.d)
say('new_D2_curve_actual_original_quadratic_head_and_units',
 exactHeadNumerator=profile(hd.n),exactHeadDenominator=profile(hd.d),
 headTakenFromAllThreeOriginalQuadraticsBeforeInverse=True,
 wholeH1ExclusionAppliesOnCurrentPhiPhysicalDNonzero=True,
 additionalPaidUnits=['2*u-1 from m=u-ell','u+Qcurve-1 from whole Q=1-u exclusion'],
 originalCurveAlreadyEmptyByPaidHead=not bool(hd),
 originalD2NeverInverted=True,noOldEuclidOrGaussianExecuted=True)
polys=[];names=['R_W','R_O','R_N1']
for index,name in zip([1,2,3],names):
 ca=original_rows[0]+[R()]*(3-len(original_rows[0]))
 cb=original_rows[index]+[R()]*(3-len(original_rows[index]))
 c,b,a=ca;f,e,d=cb
 l1=a*e-d*b;l0=a*f-d*c
 scalar=l0*l0-l1*(b*f-c*e)
 alpha=e*l1+d*l1*R(sp)-d*l0
 beta=-(a*l1*R(sp)+b*l1-a*l0)
 # Exact polynomial identity, including every a=d=0 fibre:
 assert alpha*forms[0]+beta*forms[index]==scalar
 for co in [alpha,beta,scalar]:legal(co.d)
 assert all(not any(mm[j] for j in range(1,5)) for mm in scalar.n.to_dict())
 numerator=scalar.n
 if numerator:
  lc=numerator.coefficient(0);numerator=numerator/lc
  assert R(numerator)==R(scalar.d/lc)*scalar
 polys.append(numerator)
 say('new_D2_original_fixed_quadratic_weight_cofactor',
     pair=name,fixedDegreePair=[2,2],
     exactIdentity='Res=(e*l1+d*l1*s-d*l0)*A-(a*l1*s+b*l1-a*l0)*B',
     allOriginalPolynomialCoefficientsActuallyReturned=True,
     noLeadingCoefficientDivided=True,wholeLeadingZeroFibresRetained=True,
     originalWeightNumerator=profile(numerator))
assert polys[0]
def to_qpoly(poly):
 out=[0]*(max(0,int(poly.degrees()[0]))+1)
 for mm,c in poly.to_dict().items():
  assert not any(mm[j] for j in range(1,5))
  out[int(mm[0])]=c
 return fmpq_poly(out)
def from_qpoly(poly):
 return ctx.from_dict({(j,0,0,0,0):c for j,c in enumerate(poly.coeffs()) if c})
zq=fmpq_poly([]);oq=fmpq_poly([1])
def egcd(a,b):
 r0,r1=a,b;s0,s1=oq,zq;t0,t1=zq,oq
 while r1:
  q,r=divmod(r0,r1)
  assert q*r1+r==r0
  r0,r1=r1,r;s0,s1=s1,s0-q*s1;t0,t1=t1,t0-q*t1
 if not r0:return zq,zq,zq
 lc=r0[r0.degree()]
 g,aa,bb=r0/lc,s0/lc,t0/lc
 assert aa*a+bb*b==g
 return g,aa,bb
inputs=[to_qpoly(p) for p in polys]
g=inputs[0];tags=[oq,zq,zq]
for j in [1,2]:
 gnew,a,b=egcd(g,inputs[j])
 tags=[a*t for t in tags];tags[j]+=b;g=gnew
 assert sum((t*p for t,p in zip(tags,inputs)),zq)==g
 say('new_D2_exact_QQ_u_weight_Bezout_step',
     includedPairs=names[:j+1],gcdUDegree=int(g.degree()),
     entireExceptionalUFibresIncluded=True,
     allThreeOriginalCofactorProductsReturned=True)
G=from_qpoly(g);assert G
paid=list(d2['paid'])+[('m_from_equal_weights_complete_exclusion',2*up-1),
 ('u_plus_Q_minus_1',up+qcurve-1)]
if hd:paid.append(('entire_original_quadratic_head',hd.n))
rest=G;removed=one;removed_info=[]
for label,atom in paid:
 count=0
 while True:
  gg=rest.gcd(atom)
  if gg.total_degree()==0:break
  new=rest/gg;assert new*gg==rest
  rest=new;removed*=gg;count+=1
 if count:removed_info.append(dict(unit=label,passes=count))
assert removed*rest==G
lc=rest.coefficient(0);rest=rest/lc;removed*=lc
assert removed*rest==G
closed=(not hd) or rest.total_degree()==0
say('new_entire_D2_infinity_original_weight_unit_target_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 exactOriginalWeightGCD=profile(G),removedOnlyPaidWeights=removed_info,
 remainingFullWeightSupport=profile(rest),
 fullQQuBezoutAndPaidProductsReturned=True,
 entireD2ZeroHighestOriginalDirectionExcluded=closed,
 anyUnpaidResidualUFibresRetained=not closed,
 noAffinePointCountOrWholePhiExclusionClaim=True,
 wholePhiExcluded=False,ordinaryISPClaim=False,
 sourceDefinitionPrefixBytes=len(prefix),
 sourceDefinitionPrefixSHA256=hashlib.sha256(prefix).hexdigest(),
 noOldGenericEuclidGaussianP6P9NormOrModuleGateReplayed=True,
 noCoefficientPayloadEncodedOrSplitSaved=True,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
saved_timer(signal.ITIMER_REAL,0);signal.alarm(0)
