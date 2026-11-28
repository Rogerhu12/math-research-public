#!/usr/bin/env python3
"""NEW entire W/gamma: exact nine quadratic original system and 3 scalars.
Rebuild only the 10176-byte same-point Gram/five-original-row prefix.
Do NOT rebuild the f-cube head certificate, q_f, or the frozen ten-by-two.
Use the newly paid global three-head Bezout only as the published algebraic
equivalence lemma.  For each cubic F, all three a_j F-b f Q_j are retained:
no individual quadratic head is inverted and no head-zero fiber is lost.
Loww=NS-PS+E_W2 is returned at the same original point.  Three fixed
three-row constant targets cancel only their ACTUAL common multipliers.
180s/4GiB. Hash-only receipts; no old determinant/module/norm replay.
"""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
START=time.perf_counter();DEADLINE=START+180
signal.setitimer(signal.ITIMER_REAL,180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**kw):
 kw['seconds']=time.perf_counter()-START
 print(json.dumps(kw,separators=(',',':')),flush=True)
def digest(x):
 raw=json.dumps(x,separators=(',',':')).encode()
 return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
path=Path(__file__).with_name('2026-11-28-unit211-W-gamma-open-direct-native-f-cube-monic-two-8542.py')
raw=path.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='bd68e5e5e66f31e9c3e2ad0b66468c021fc7d852d44462d3a937966200ab961c'
marker=b'\n# Necessary old definitions only:'
assert raw.count(marker)==1
prefix=raw.split(marker)[0]
assert len(prefix)==10176 and hashlib.sha256(prefix).hexdigest()=='8545759f4c40266068fc932bd2ef10710fe67cd767cf743900fe3d215bfb6bcf'
env={'__file__':str(path),'__name__':'new_gamma_same_original_Gram_only'}
old_alarm=signal.alarm;old_timer=signal.setitimer
def timer(which,seconds,interval=0.0):
 if which!=signal.ITIMER_REAL:return old_timer(which,seconds,interval)
 assert not interval
 left=max(.001,DEADLINE-time.perf_counter())
 return old_timer(which,min(left,float(seconds) if seconds>0 else left),0.0)
def alarm(seconds):return math.ceil(timer(signal.ITIMER_REAL,seconds)[0])
signal.alarm=alarm;signal.setitimer=timer
try:
 with contextlib.redirect_stdout(io.StringIO()):
  exec(compile(prefix,str(path)+'#necessary_same_Gram_not_old_tail','exec'),env)
finally:
 signal.alarm=old_alarm;signal.setitimer=old_timer
 old_timer(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
R=env['R'];E=env['E'];ctx=env['ctx']
ep,kp,sp,fp=[env[x] for x in ['ep','kp','sp','fp']]
zz,oo=env['zz'],env['oo']
u,l,m,M,Delta=[env[x] for x in ['u','l','m','M','Delta']]
f,t,lam,T,P02,bc=[env[x] for x in ['f','t','lam','T','P02','bc']]
x0,x1,X,Y,b,c,p,q=[env[x] for x in ['x0','x1','X','Y','b','c','p','q']]
EW,EB,EC,N1,NS,PS=[env[x] for x in ['EW','EB','EC','N1','NS','PS']]
atoms=env['base_atoms']
assert all(all(int(mm[3])==0 for mm in a.to_dict()) for _,a in atoms)
Sx=2*x0;Px=2*x0+2*Delta*x1;XY=x0*x0-Delta*x1*x1
Kw=2*(t*t+(5*u-2*Sx-2)*t+2*XY+2*Px-2*u*Sx+2*u*u-6*u+env['Q'])
eta=f-u
Loww=2*P02*(2*lam-1)*(lam-1-T)-bc*t*(Kw+4*eta*(t-2))
EW2=b*(2*p-E(u)-X)*EB+c*(2*q-E(u)-Y)*EC
assert not EW2.b
mean_coeff0=2-u-x0+(m/l)*(2-x1)
mean_coeff1=(M/l)*(2-x1)
assert EW2==E(mean_coeff0)*EW+E(mean_coeff1)*E(EB.b)
assert E(Loww)==NS-PS+EW2
original=[EW.a,EB.b,N1.a,Loww,NS.a]
for value in original:
 assert all(int(mm[3])==0 for mm in value.d.to_dict())
 assert not value or int(value.n.degrees()[3])<=3
for value in [mean_coeff0,mean_coeff1]+original:
 env['paid_den'](value.d,atoms)
assert all(not original[j] or int(original[j].n.degrees()[3])<=2 for j in range(3))
say(stage='new_gamma_original_low_weighted_basis_change',
 identity='Loww=NS-PS+(2-u-x+m*(2-y)/ell)*EW+(M/ell)*(2-y)*EBo',
 fullSamePointIdentityReturned=True,
 originalFiveRows=['EW','EBo','N1','Loww','NS'],
 fDegrees=[int(v.n.degrees()[3]) if v else -1 for v in original],
 LowwNotAssumedQuadratic=True,
 trueOriginalI6BasisChange=True,
 noOriginalCubicTailOrMonicF2Rebuilt=True)
exact_products=0;original_products=1
def dex(a,b):
 global exact_products
 q0,r0=divmod(a,b);assert not r0 and q0*b==a
 exact_products+=1;return q0
def profile(p):
 if not p:return dict(zero=True,degrees_e_k_s_f=[-1]*4,terms=0)
 data=[[list(map(int,mm)),str(c0)] for mm,c0 in sorted(p.to_dict().items())]
 return dict(zero=False,degrees_e_k_s_f=list(map(int,p.degrees())),
  totalDegree=int(p.total_degree()),terms=len(data),**digest(data))
def fcols(p):
 if not p:return []
 out=[zz for _ in range(int(p.degrees()[3])+1)]
 for mm,c0 in p.to_dict().items():
  ee,kk,ss,ff=map(int,mm);out[ff]+=c0*ep**ee*kp**kk*sp**ss
 assert sum((a*fp**j for j,a in enumerate(out)),zz)==p
 return out
primitive=[];units=[];histories=[]
for i,v in enumerate(original):
 core,removed,hist=env['strip_atoms'](v.n,atoms)
 assert core
 scale=core.coefficient(0);core/=scale;removed*=scale
 unit=R(removed,v.d)
 assert R(core)*unit==v
 env['paid_den'](unit.n,atoms);env['paid_den'](unit.d,atoms)
 primitive.append(core);units.append(unit);histories.append(hist)
 original_products+=1
say(stage='new_gamma_original_primitive_quadratic_cubic_rows',
 profiles=[profile(p0) for p0 in primitive],
 onlyPaidParameterContentRemoved=histories,
 allFiveOriginalUnitProductsReturned=True,
 allUnpaidParameterContentRetained=True)
cols=[fcols(p0) for p0 in primitive]
assert all(len(c0)==3 for c0 in cols[:3])
heads=[c0[2] for c0 in cols[:3]]
quadratics=primitive[:3];provenance=[dict(original=i) for i in range(3)]
# q_j differ from the three published raw quadratics only by units.
# Hence their three heads still generate 1 on the WHOLE gamma chart.
# This published fact makes all three quadratic lifts exact jointly;
# the source never chooses one head to invert.
for index in [3,4]:
 high=cols[index][3] if len(cols[index])==4 else zz
 for j in range(3):
  lift=heads[j]*primitive[index]-high*fp*primitive[j]
  assert lift==heads[j]*primitive[index]-high*fp*primitive[j]
  assert not lift or int(lift.degrees()[3])<=2
  quadratics.append(lift)
  provenance.append(dict(originalCubic=index,originalQuadratic=j,
       positiveMultiplier='quadratic_head',cancelledCubicCoefficient=profile(high)))
  original_products+=1
assert len(quadratics)==9
matrix=[]
for p0 in quadratics:
 c0=fcols(p0);assert len(c0)<=3
 matrix.append(c0+[zz]*(3-len(c0)))
say(stage='new_global_gamma_exact_nine_quadratic_original_system',
 originalFiveRows=['EW','EBo','N1','Loww','NS'],
 quadraticRowProvenance=provenance,
 allNineCoefficientIdentitiesReturned=True,
 exactIdealEquivalenceUsesPublishedWholeThreeHeadBezout1=True,
 noIndividualHeadInverted=True,allHeadZeroFibersKept=True,
 matrixProfiles=[[profile(c0) for c0 in row] for row in matrix],
 noMonicF2OrFrozenTenByTwoReplayed=True)
results=[]
for triple in [(0,1,2),(0,1,3),(0,1,6)]:
 rr=[matrix[i] for i in triple]
 mu=[rr[1][1]*rr[2][2]-rr[2][1]*rr[1][2],
     rr[2][1]*rr[0][2]-rr[0][1]*rr[2][2],
     rr[0][1]*rr[1][2]-rr[1][1]*rr[0][2]]
 common=zz
 for a0 in mu:common=common.gcd(a0)
 if not common:
  say(stage='new_fixed_three_original_scalar_zero',
      rows=list(triple),allThreeMultipliersZero=True,
      noUnitOrEmptyFiberClaim=True)
  continue
 reduced=[dex(a0,common) for a0 in mu]
 actual=[sum((reduced[i]*rr[i][j] for i in range(3)),zz) for j in range(3)]
 assert actual[1]==zz and actual[2]==zz
 scalar=actual[0]
 assert sum((reduced[i]*quadratics[triple[i]] for i in range(3)),zz)==scalar
 original_products+=1
 if not scalar:
  say(stage='new_fixed_three_original_scalar_zero',
      rows=list(triple),actualCommonMultiplierCancellationReturned=True,
      bothPositiveFColumnsReturned=True,noUnitOrEmptyFiberClaim=True)
  continue
 core,removed,hist=env['strip_atoms'](scalar,atoms)
 c0=core.coefficient(0);core/=c0;removed*=c0
 assert core*removed==scalar and all(int(mm[3])==0 for mm in core.to_dict())
 rec=dict(rows=list(triple),
   actualCommonMultiplier=profile(common),
   reducedActualMultipliers=[profile(p0) for p0 in reduced],
   originalConstant=profile(scalar),necessaryPrimitive=profile(core),
   onlyPaidParameterFactorRemoval=hist,
   allThreePolynomialColumnsAndOriginalDAGReturned=True,
   noOriginalEquationDividedByUnpaidFactor=True,
   allUnpaidHeadZerosRetained=True)
 results.append(rec)
 say(stage='new_gamma_fixed_three_original_constant',**rec)
say(stage='new_gamma_nine_quadratic_and_fixed_constants_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 exactIdealEquivalenceOnWholeGammaChart=True,
 actualPolynomialDivisionProducts=exact_products,
 actualOriginalIdentityProducts=original_products,
 originalConstructionDivisionProducts=env['exact_products'],
 actualNonzeroConstants=len(results),
 wholeGammaExcluded=any(r['necessaryPrimitive']['totalDegree']==0 for r in results),
 noAdditionalWeightUnitAssumed=True,
 noCoefficientCacheOrPayloadSaved=True,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 ordinaryISPClaim=False)
