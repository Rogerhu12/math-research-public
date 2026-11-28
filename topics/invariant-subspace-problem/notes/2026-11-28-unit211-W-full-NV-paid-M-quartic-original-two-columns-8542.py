#!/usr/bin/env python3
"""NEW whole W: a genuinely lower-degree complete-NV quartic.
NEW paid-M normalization: bDelta=M*b0, Z1tilde=M*z1, Z2tilde=M*z2.
B4bar=b0*(Z0tilde+D*z2)-aDelta*z1.
(2m*ell^2*b0)*Vlow-z1*C4=2m*D*B4bar.
Only physical D, already nonzero in this chart, gives necessity; the
entire bDelta=0 face stays and no equivalence replacing Vlow is claimed.
Use the proved nine-variable full-N4 short identities, one NEW native
quartic reduction, then polynomial contraction through SIX pre-reduced
basis rows. No old lambda/T action, qT4/Vlow transport or pair is run.
180 seconds /4 GiB; all unproved heads/content remain.
"""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
START=time.perf_counter();DEADLINE=START+180
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
raw_timer=signal.setitimer;raw_alarm=signal.alarm
raw_timer(signal.ITIMER_REAL,180)
def say(**kw):
 kw['seconds']=time.perf_counter()-START
 print(json.dumps(kw,separators=(',',':')),flush=True)
def bounded_timer(which,seconds,interval=0.0):
 if which!=signal.ITIMER_REAL:return raw_timer(which,seconds,interval)
 assert not interval
 left=max(.001,DEADLINE-time.perf_counter())
 return raw_timer(which,min(left,float(seconds) if seconds>0 else left),0.0)
def bounded_alarm(seconds):return math.ceil(bounded_timer(signal.ITIMER_REAL,seconds)[0])
path=Path(__file__).with_name('2026-11-28-unit211-W-alpha-chi-full-original-ten-by-two-8542.py')
full=path.read_bytes()
assert hashlib.sha256(full).hexdigest()=='18101a4af587253e1dad49cee60d188c60db401ed34b13cf73edeb4e09b6d42b'
marker=b'\nnewfive=rawthree[:]';assert full.count(marker)==1
prefix=full.split(marker)[0]
assert len(prefix)==9855 and hashlib.sha256(prefix).hexdigest()=='c1436ea6bb67d4c720016091fb65f439be5bfcc7af131c00a0749321fcf45e43'
env={'__name__':'new_complete_NV_quartic_necessary_alpha_square_only','__file__':str(path)}
signal.alarm=bounded_alarm;signal.setitimer=bounded_timer
try:
 with contextlib.redirect_stdout(io.StringIO()):
  exec(compile(prefix,str(path)+'#monic_square_definition_only','exec'),env)
finally:
 signal.alarm=raw_alarm;signal.setitimer=raw_timer
 raw_timer(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
R,NR,ctx,ns=[env[key] for key in ['R','NR','ctx','ns']]
ep,kp,cp,ap=ctx.gens()
zz,oo=ctx.constant(0),ctx.constant(1)
paid,strip,profile,embed=[env[key] for key in ['paid','strip','profile','embed']]
qc,qalpha,alpha=env['qc'],env['qalpha'],env['alpha']
ac,adeg=env['ac'],env['adeg']
basis=ns['basis'];oldoriginal=ns['original']
newbasis=[R(1),env['xx'],env['yy'],env['tt'],env['yy']**2,env['yy']*env['tt']]
assert len(basis)==len(newbasis)==6
assert not any(ns['tags'][j][i] for j in range(6) for i in [4,5])
native_den_paid=set()
def native_coefficient(c):
 c=NR(c)
 for p in [c.n,c.d]:
  assert all(not any(int(v) for v in mon[2:]) for mon in p.to_dict())
 key=str(c.d)
 if key not in native_den_paid:
  paid(embed(c.d));native_den_paid.add(key)
 return c
def row_profile(row):
 return [{'n':profile(embed(native_coefficient(c).n)),
          'd':profile(embed(c.d))} for c in row]
def row_digest(row):
 encoded=json.dumps([[[list(map(int,mon[:2])),str(c)]
             for mon,c in sorted(p.to_dict().items())]
             for v in row for p in [v.n,v.d]],separators=(',',':')).encode()
 return dict(bytes=len(encoded),sha256=hashlib.sha256(encoded).hexdigest())
nu,nQ,nell,nM,nP02,nJ=[ns[key] for key in ['u','Q','l','M','P02','J']]
nm=nu-nell;ndelta=1-nQ
for unit in [nu,nQ,nell,nM,nm,ndelta,nP02]:
 paid(embed(unit.n));paid(embed(unit.d))
nlam,nT=ns['lam'],ns['T']

# The three polynomial scaled-N4 formulas were independently proved on
# nine free raw Gram/value variables by source SHA39b490ebb38cb807...
# Here they only DEFINE this genuinely new degree-four input.
nA1E=ns['A'];nVE=ns['b']*ns['X']+ns['c']*ns['Y']
physical_p,physical_q=ns['rows'][0][2],ns['rows'][0][3]
assert physical_p.conj()==physical_q
nWE=ns['b']*physical_p*ns['X']+ns['c']*physical_q*ns['Y']
assert not nA1E.b and not nVE.b and not nWE.b
nA1,nV,nW=nA1E.a,nVE.a,nWE.a
nf,nbc=ns['f'],ns['bc']
assert 4*nbc*ndelta==nM
cval=3-2*nlam;w=nlam-1-nT
Aval=2*nlam*nlam-2*nlam+1
Bval=4*nlam**3-6*nlam*nlam+3*nlam-1
Dval=nell*Aval-nT*nT
Kval=nell*nell*Bval-3*nell*Aval*nT+2*nT**3
Z0=(nell*nell*nA1+4*nell*nell*(1-2*nlam)*nf+2*nell*nf*Dval
 +2*nell*nu*w*(nell*cval+nT)
 +2*nV*(nell*nell+nell*cval*nT+nT*nT)
 +2*nbc*ns['t']*(nT*nT-nell*nell))
Z1=(2*(nell*cval+2*nT)*(nu*nV-nell*nW)
 -2*nell*nM*w+4*nbc*nm*nT*ns['t'])
Z2=2*((nu*nu-nell*nell*nQ)*nV-2*nm*nell*nW-nell*nM*nf-nbc*nM*ns['t'])
Ast=4*nu*nQ-nJ;Cst=Ast*nm*nm+nJ*ndelta*nell*nell
ad=(nM*nell*nell*nQ*(3-4*nlam)+nM*Ast*nT*nT
 +2*nM*nu*nQ*cval*nell*nT+Dval*Cst)
bd=2*nM*nm*(Ast*nT+nu*nQ*cval*nell)
C4=2*nm*Dval*ad+Kval*bd
# Exact native two-coordinate identities pay a COMMON pure-weight M
# before the new quartic is formed, without altering any old source.
assert nV==nell*ns['x0']+nm*ns['x1']
assert nu*nV-nell*nW==-nM*ns['x1']
b0=2*nm*(Ast*nT+nu*nQ*cval*nell)
z1=-2*(nell*cval+2*nT)*ns['x1']-2*nell*w+nm*nT*ns['t']/ndelta
z2=2*(nell*(ns['x0']-nf)-nm*ns['x1']-nbc*ns['t'])
assert bd==nM*b0 and Z1==nM*z1 and Z2==nM*z2
# Complete identity in the THREE formal (Z0tilde,z1,z2) coordinates;
# no old Vlow polynomial target or quotient is reconstructed.
vcoef=[Dval,Kval*nM/(2*nm),Dval*Dval]
bcoef=[b0,-ad,b0*Dval]
for j in range(3):
 assert 2*nm*b0*vcoef[j]-(C4 if j==1 else NR())==2*nm*Dval*bcoef[j]
Bfour=b0*(Z0+Dval*z2)-ad*z1
for poly in [Bfour.n,Bfour.d]:
 assert all(not any(int(mm[j]) for j in range(5,8)) for mm in poly.to_dict())
assert all(sum(map(int,mm[2:5]))<=4 for mm in Bfour.n.to_dict())
paid(embed(Bfour.d))
def native_profile(v):
 raw=json.dumps([[[list(map(int,mm)),str(c)]
       for mm,c in sorted(p.to_dict().items())] for p in [v.n,v.d]],
       separators=(',',':')).encode()
 return dict(numeratorDegrees=list(map(int,v.n.degrees())) if v else [-1]*8,
             numeratorTerms=len(v.n.to_dict()),bytes=len(raw),
             sha256=hashlib.sha256(raw).hexdigest())
say(stage='new_full_NV_physical_D_lowered_original_quartic_defined',
 originalIdentity='(2m*ell^2*b0)*Vlow-z1*C4=2m*D*B4bar',
 allThreeFormalZCombinationCoefficientsReturned=True,
 allThreePaidMFactorProductsReturned=True,
 nativeVAndHLinearIdentitiesReturned=True,
 originalRawDegreeAtMostFour=True,rawQuartic=native_profile(Bfour),
 physicalDNonzeroUsedOnlyForNecessity=True,
 bDeltaZeroFiberKept=True,VlowReplacementEquivalenceClaim=False,
 oldCompleteVlowTransportOrPairNotExecuted=True)
newrow,newtag=ns['reduce_six'](Bfour)
assert not newtag[4] and not newtag[5]
for c in newrow:native_coefficient(c)
say(stage='new_full_NV_quartic_native_original_trace_return',
 oldNativeDenominatorWhitelistPassedUnchanged=True,
 completeOriginalQuarticMeanSourceReturned=True,
 coefficientDefinition=row_digest(newrow),
 noOldTwelveLambdaTActions=True,
 noOldFullValueOrPairTargets=True)
# Polynomial, not repeated rational, transport of this NEW input.
# For each original basis element b_i, compute once
# DB*b_i=B_i0+B_i1*alpha+H_i*qalpha.
# These SIX actual identities are then contracted by the actual native
# row, with all denominators cleared in the pure-weight ring.
divisions=0;basisIdentities=0
def dex(a,b):
 global divisions
 q,r=divmod(a,b);assert not r and q*b==a
 divisions+=1;return q
def lcm_poly(a,b):return dex(a,a.gcd(b))*b
def clear_coeff(v,den):
 v=R(v);paid(v.d)
 return v.n*dex(den,v.d)
basisA=[];basisL=[]
DB=oo
for v in newbasis:
 assert adeg(v)<=2
 aa=[ac(v,j) for j in range(3)]
 ll=[aa[0]-aa[2]*qc[0],aa[1]-aa[2]*qc[1]]
 for c in aa+ll:
  paid(c.d);DB=lcm_poly(DB,c.d)
 basisA.append(aa);basisL.append(ll)
paid(DB)
QA=oo
for c in qc[:2]:QA=lcm_poly(QA,c.d)
paid(QA)
qnums=[clear_coeff(c,QA) for c in qc[:2]]
Ap=[[clear_coeff(c,DB) for c in row] for row in basisA]
Bp=[[clear_coeff(c,DB) for c in row] for row in basisL]
Hp=[row[2] for row in Ap]
for i in range(6):
 assert QA*(Ap[i][0]-Bp[i][0])==Hp[i]*qnums[0]
 assert QA*(Ap[i][1]-Bp[i][1])==Hp[i]*qnums[1]
 basisIdentities+=2
say(stage='new_quartic_transport_six_actual_basis_identities',
 actualCoefficientIdentities=basisIdentities,
 monicAlphaSquaredCoordinatesIdentified=6,
 allPureWeightDenominatorsPaid=True,
 commonBasisWeightDenominator=profile(DB),
 noOldValueLinearRowRecomputed=True)
DR=oo;converted=[]
for c in newrow:
 v=R(embed(c.n),embed(c.d));paid(v.d)
 converted.append(v);DR=lcm_poly(DR,v.d)
paid(DR)
rp=[clear_coeff(c,DR) for c in converted]
cols=[sum((rp[i]*Bp[i][j] for i in range(6)),zz) for j in range(2)]
head=sum((rp[i]*Hp[i] for i in range(6)),zz)
# Complete identity is the polynomial linear combination of the SIX
# actual identities above. Retain its coefficients rp and head as a DAG;
# no extra giant rational resummation or false freeness assumption.
for j in range(2):
 assert not sum((rp[i]*(QA*(Ap[i][j]-Bp[i][j])-Hp[i]*qnums[j])
                for i in range(6)),zz)
def primitive_pair(cols):
 before=cols[:];g=cols[0].gcd(cols[1])
 if g:rest,removed,hist=strip(g)
 else:removed=oo;hist=[]
 out=[dex(c,removed) for c in cols]
 if any(out):
  a=next(c for c in out if c).coefficient(0)
  out=[c/a for c in out];removed*=a
 paid(removed)
 assert all(out[j]*removed==before[j] for j in range(2))
 return out,removed,hist
Bcols,Bremoved,Bhist=primitive_pair(cols)
paid(DB*DR)
say(stage='new_complete_NV_quartic_alpha_chi_two_columns_returned',
 columns=[profile(c) for c in Bcols],
 onlyPaidWeightContentRemoved=Bhist,
 completeIdentity='DB*DR*B4bar=Bremoved*(B0+B1*alpha)+head*qalpha-DB*DR*originalMeanDAG',
 nativeOriginalTraceAndSixActualBasisProductsComposed=True,
 polynomialContractionCoefficientsReturned=True,
 giantRationalReExpansionNotClaimed=True,
 noUnpaidChiOrBDeltaHeadInverted=True,
 oldVlowAndQT4TransportNotExecuted=True,
 allOriginalConditionsRetainedByReference=True)
# Only two NEW fixed targets: this quartic and original EW / EBo.
# The original N1 and every full individual value are still retained.
meanRows=[]
for index,label in [(0,'original_EW'),(1,'original_EBo')]:
 v=env['rawthree'][index]
 lin=v-ac(v,2)*qalpha;assert adeg(lin)<=1
 pair=[ac(lin,0),ac(lin,1)]
 assert v==pair[0]+pair[1]*alpha+ac(v,2)*qalpha
 den=oo
 for c in pair:paid(c.d);den=lcm_poly(den,c.d)
 po=[clear_coeff(c,den) for c in pair]
 out,removed,hist=primitive_pair(po)
 assert all(R(out[j])*R(removed,den)==pair[j] for j in range(2))
 meanRows.append((label,out))
results=[]
for label,left in meanRows:
 right=Bcols
 mu=[right[1],-left[1]];g=mu[0].gcd(mu[1])
 if not g:
  say(stage='new_quartic_mean_pair_constant_rows',labels=[label,'B4'],
      originalConstants=[profile(left[0]),profile(right[0])],
      noUnitClaim=True)
  continue
 mu=[dex(c,g) for c in mu]
 scalar=mu[0]*left[0]+mu[1]*right[0]
 assert not mu[0]*left[1]+mu[1]*right[1]
 assert mu[0]*(left[0]+left[1]*ap)+mu[1]*(right[0]+right[1]*ap)==scalar
 necessary,removed,hist=strip(scalar)
 if necessary:
  cc=necessary.coefficient(0);necessary/=cc;removed*=cc
 assert necessary*removed==scalar
 rec=dict(labels=[label,'new_full_NV_B4'],actualMultiplierCommon=profile(g),
          originalScalar=profile(scalar),necessary=profile(necessary),
          onlyPaidWeightRemoval=hist,
          bothOriginalColumnProductsReturned=True,
          entireActualMultiplierCommonZeroFiberKept=True,
          noNewLeadingFactorOrGeometryUnitAssumed=True)
 results.append(rec);say(stage='new_complete_NV_quartic_original_mean_scalar',**rec)
say(stage='new_lowered_full_NV_quartic_original_first_return_complete',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 exactPolynomialDivisionProducts=divisions,
 actualBasisCoefficientIdentities=basisIdentities,
 originalQuarticTraceReturned=True,
 completeQuarticTwoColumnReturned=True,
 oldLambdaTActionsValuesPairsAndNormsNotExecuted=True,
 wholeWExcluded=any(not r['necessary']['zero'] and
                   r['necessary']['totalDegree']==0 for r in results),
 noCoefficientCachePayloadOrChunksSaved=True,ordinaryISPClaim=False,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
raw_timer(signal.ITIMER_REAL,0)
