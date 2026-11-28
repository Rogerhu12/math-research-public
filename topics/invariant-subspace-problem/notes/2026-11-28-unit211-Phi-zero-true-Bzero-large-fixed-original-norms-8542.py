#!/usr/bin/env python3
"""NEW true B: norms of the four original omega-linear rows.
One complete F34/F40 constant field per independent first run.  The
already returned monic lambda-six is an input; its coefficients are
regenerated from its first nonzero original pair and identified by SHA.
No old pair-gcd proof gate, no original I6 rational basis matrix,
no NS/PS reduction, no positive target, and no resource-limit increase.
Each new row norm is a fixed Sylvester identity including b_i=0.
A final complete three-coordinate identity returns to r_i and q_omega.
"""
import hashlib,json,math,os,pathlib,resource,signal,time
START=time.perf_counter();DEADLINE=START+120
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
RAW_ALARM=signal.alarm
def tick():
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute 120 second boundary')
def bounded_alarm(seconds):
 if seconds<=0:return RAW_ALARM(0)
 tick();return RAW_ALARM(max(1,min(int(seconds),math.ceil(DEADLINE-time.perf_counter()))))
signal.alarm=bounded_alarm;signal.alarm(120)
DEG=int(os.environ.get('ISP_B_FACTOR_DEGREE','34'));assert DEG in (34,40)
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,sort_keys=True),flush=True)
OLD_NAME='2026-11-28-unit211-Phi-zero-true-Bzero-large-constant-original-fiber-8542.py'
OLD_SHA='a44a8fc4ca4842d97c4d94215250e8399f5988407c3971bdc68ffe96b3b77a48'
path=pathlib.Path(__file__).with_name(OLD_NAME)
if not path.exists():path=pathlib.Path(os.environ.get('ISP_INPUT_DIR',''))/OLD_NAME
old=path.read_text();assert hashlib.sha256(old.encode()).hexdigest()==OLD_SHA
MARKER="for i,value in enumerate(env['original']):"
assert old.count(MARKER)==1
prefix=old[:old.index(MARKER)]
state={'__name__':'new_B_fixed_norm_necessary_definitions_only',
       '__file__':str(path),'print':lambda *a,**kw:None}
# The outer absolute alarm bounds all nested prefix alarm requests too.
exec(compile(prefix,str(path)+'#necessary_constant_and_original_row_definitions','exec'),state)
signal.alarm=bounded_alarm;signal.alarm(120)
K=state['K'];K0=state['K0'];K1=state['K1'];d=state['d']
pa,pn,ps,pc,pm,pd,pgcd=[state[k] for k in ('pa','pn','ps','pc','pm','pd','pgcd')]
qw=state['qw'];linear=state['linear'];pinfo=state['pinfo']
assert d==DEG and len(linear)==4 and len(qw)==3 and qw[2]==[K1]
# This is only the exact definition of the already proved monic g_6.
# The old six-pair gcd and its full original proof return are NOT run.
first=ps(pm(linear[0][0],linear[3][1]),pm(linear[0][1],linear[3][0]))
assert len(first)==7
scale=first[-1].inverse();g=pc(first,scale)
EXPECTED_G={
 34:'f2d41bd0b2b1623745f9e0fd69a0cb488650f07bcd264a3f18b4a63bf8188b0c',
 40:'9a94efc0ec88870b215b47b5175bbc4832b9c3f75c66d14e16d59ab845198cfe'}
assert pinfo(g)['sha256']==EXPECTED_G[d] and g[-1]==K1
say('new_B_fixed_norm_original_input',
 constantDegree=d,originalFourRowDegrees=[[len(v)-1 for v in r] for r in linear],
 monicOmegaCoefficientDegrees=[len(v)-1 for v in qw],
 existingMonicLambdaSix=pinfo(g),oldFullSourceSHA256=OLD_SHA,
 necessaryPrefixSHA256=hashlib.sha256(prefix.encode()).hexdigest(),
 oldSixPairGCDAndOriginalReturnNotExecuted=True,
 oldI6FullRationalMatrixNotExecuted=True,noCoefficientPayloadPrinted=True)
# r_i=a_i+b_i*omega.  n_i=(a_i-q1*b_i-b_i*omega)*r_i+b_i^2*q.
norms=[];norm_quotients=[];norm_remainders=[];identity_coordinates=0
for i,(a,b) in enumerate(linear):
 tick()
 a_minus_q1b=ps(a,pm(qw[1],b));b2=pm(b,b)
 n=pa(pm(a_minus_q1b,a),pm(b2,qw[0]))
 raw0=pa(pm(a_minus_q1b,a),pm(b2,qw[0]))
 raw1=pa(ps(pm(a_minus_q1b,b),pm(b,a)),pm(b2,qw[1]))
 raw2=pa(pn(pm(b,b)),pm(b2,qw[2]))
 assert not ps(raw0,n) and not raw1 and not raw2
 quotient,remainder=pd(n,g)
 norms.append(n);norm_quotients.append(quotient);norm_remainders.append(remainder)
 identity_coordinates+=3
 say('new_B_original_fixed_two_plus_one_norm',
  constantDegree=d,originalRow=i,norm=pinfo(n),remainderDegree=len(remainder)-1,
  allThreeOmegaCoordinatesReturned=True,
  fixedSylvesterIdentity=True,originalLinearHeadZeroKept=True)
# A genuinely new scalar ideal (g_6, n_0,n_1,n_2,n_3).
h=g;beta_g=[K1];beta=[]
for i,(n,q,r) in enumerate(zip(norms,norm_quotients,norm_remainders)):
 tick()
 if r:
  hh,a,b=pgcd(h,r)
 else:
  hh,a,b=h,[K1],[]
 beta_g=ps(pm(a,beta_g),pm(b,q))
 beta=[pm(a,v) for v in beta]+[b];h=hh
 check=pm(beta_g,g)
 for c,ni in zip(beta,norms):check=pa(check,pm(c,ni))
 assert not ps(check,h)
 say('new_B_original_norm_common_ideal_checkpoint',
  constantDegree=d,throughOriginalRow=i,monicGCDDegree=len(h)-1,
  completeScalarBezoutReturned=True)
 if len(h)==1:
  beta.extend([[] for _ in range(3-i)])
  break
assert h and h[-1]==K1 and len(beta)==4
# Compose only this NEW Bezout with the exact fixed identities.
# g=scale*(b_3*r_0-b_0*r_3); all other terms are the new n_i.
omega_multipliers=[[[],[]] for _ in range(4)]
omega_multipliers[0][0]=pm(pc(beta_g,scale),linear[3][1])
omega_multipliers[3][0]=pn(pm(pc(beta_g,scale),linear[0][1]))
q_multiplier=[]
for i,(a,b) in enumerate(linear):
 omega_multipliers[i][0]=pa(omega_multipliers[i][0],
                           pm(beta[i],ps(a,pm(qw[1],b))))
 omega_multipliers[i][1]=pn(pm(beta[i],b))
 q_multiplier=pa(q_multiplier,pm(beta[i],pm(b,b)))
ret=[[],[],[]]
for mult,(a,b) in zip(omega_multipliers,linear):
 ret[0]=pa(ret[0],pm(mult[0],a))
 ret[1]=pa(ret[1],pa(pm(mult[0],b),pm(mult[1],a)))
 ret[2]=pa(ret[2],pm(mult[1],b))
for j in range(3):ret[j]=pa(ret[j],pm(q_multiplier,qw[j]))
assert not ps(ret[0],h) and not ret[1] and not ret[2]
identity_coordinates+=3
say('new_B_fixed_original_norm_complete_result',
 constantDegree=d,oldLambdaDegree=6,newMonicNecessaryLambdaDegree=len(h)-1,
 actualFinalRelation=pinfo(h),newNorms=[pinfo(n) for n in norms],
 completeThreeCoordinateOriginalI4IdentityReturned=True,
 newFixedNormIdentityCoordinates=identity_coordinates,
 wholeFactorExcluded=len(h)==1,
 fullNecessaryQQEnvironmentDimension=2*d*(len(h)-1) if len(h)>1 else 0,
 allComplexConstantEmbeddingsKept=True,allRemainingLambdaAndOmegaMultiplicityKept=True,
 originalLinearHeadZeroFibersKept=True,
 noDOrLambdaOrTOrNormInverse=True,
 noOriginalI6MatrixOrPositiveTargetExecuted=True,
 otherConstantFactorNotTested=True,wholeBExcluded=False,wholePhiExcluded=False,
 sourceSHA256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
 ordinaryISPClaim=False)
