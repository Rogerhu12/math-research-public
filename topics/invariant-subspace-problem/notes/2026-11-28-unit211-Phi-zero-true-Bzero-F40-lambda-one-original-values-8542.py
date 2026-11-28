#!/usr/bin/env python3
"""NEW F40: whole original lambda-one specialization, at most 80 QQ dimensions.
The proven h1 is regenerated ONLY as a parameter: monic gcd(g6,n0),
identified by its already published final SHA.  No four-norm proof,
old six-pair Bezout, 480-dimensional matrix, or old positive target runs.
Keep the complete K40 and monic omega quadratic.  Rebuild six original
values after lambda=lambda*, perform a NEW omega Bezout, and only then
try Dval,Dval^2 as positive targets in that new quotient.  No D inverse.
120 seconds / 1 GiB, absolute nested deadline; small metadata only.
"""
import hashlib,json,math,os,pathlib,resource,signal,time
START=time.perf_counter();DEADLINE=START+120
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
RAW_ALARM=signal.alarm
def tick():
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute 120 second boundary')
def bounded_alarm(seconds):
 tick()
 left=max(1,math.ceil(DEADLINE-time.perf_counter()))
 return RAW_ALARM(left if seconds<=0 else max(1,min(int(seconds),left)))
signal.alarm=bounded_alarm;signal.alarm(120)
os.environ.setdefault('ISP_B_FACTOR_DEGREE','40')
assert os.environ['ISP_B_FACTOR_DEGREE']=='40'
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
assert hashlib.sha256(prefix.encode()).hexdigest()=='a922242b457a02320499c8157642aa920ac930001bace88d4ce59b1ed5f90201'
state={'__name__':'new_F40_lambda_one_necessary_parameter_definitions',
       '__file__':str(path),'print':lambda *a,**kw:None}
exec(compile(prefix,str(path)+'#necessary_definitions_only','exec'),state)
signal.alarm=bounded_alarm;signal.alarm(120)
K=state['K'];K0=state['K0'];K1=state['K1'];d=state['d'];assert d==40
pa,pn,ps,pc,pm,pd=[state[k] for k in ('pa','pn','ps','pc','pm','pd')]
pinfo=state['pinfo'];env=state['env'];cv=state['cv']
linear=state['linear'];qw=state['qw']
first=ps(pm(linear[0][0],linear[3][1]),pm(linear[0][1],linear[3][0]))
assert len(first)==7
g6=pc(first,first[-1].inverse())
assert pinfo(g6)['sha256']=='9a94efc0ec88870b215b47b5175bbc4832b9c3f75c66d14e16d59ab845198cfe'
# ONLY the previously defined parameter, not the four-norm certificate.
a0,b0=linear[0]
n0=pa(ps(pm(a0,a0),pm(qw[1],pm(a0,b0))),pm(qw[0],pm(b0,b0)))
left,right=g6,n0
parameter_divisions=0
while right:
 tick();_,rem=pd(left,right);left,right=right,rem;parameter_divisions+=1
h1=pc(left,left[-1].inverse())
assert len(h1)==2 and h1[1]==K1
assert pinfo(h1)['sha256']=='da857429ce495f99a8122be93572a2ea843d686399306736f686cc563b0851ee'
lamstar=-h1[0]
def peval(p,x):
 out=K0
 for c in reversed(p):out=out*x+c
 return out
assert peval(h1,lamstar)==K0
say('new_F40_lambda_one_parameter_input',
 constantDegree=40,provenMonicLambdaOne=pinfo(h1),
 necessaryPrefixSHA256=hashlib.sha256(prefix.encode()).hexdigest(),
 parameterOnlyOrdinaryDivisionCount=parameter_divisions,
 allFourNormsAndTheirBezoutNotReexecuted=True,
 old480MatrixAndOldPositiveTargetsNotExecuted=True,
 oldFullSourceSHA256=OLD_SHA)
def trim(p):
 p=list(p)
 while p and not p[-1]:p.pop()
 return p
counts={'newOmegaDivisions':0,'newOmegaBezoutReturns':0,
        'newCompleteOriginalCoordinateReturns':0,
        'newPhysicalTargetCoordinateReturns':0}
def wdiv(a,b):
 tick();a=trim(a);b=trim(b);assert b
 r=a[:];q=[K0]*max(0,len(a)-len(b)+1);iv=b[-1].inverse()
 while r and len(r)>=len(b):
  j=len(r)-len(b);c=r[-1]*iv;q[j]=q[j]+c
  r=ps(r,[K0]*j+pc(b,c))
 q=trim(q)
 assert not ps(a,pa(pm(q,b),r))
 assert not r or len(r)<len(b)
 counts['newOmegaDivisions']+=1
 return q,r
def wxgcd(a,b):
 r0,r1=trim(a),trim(b);s0,s1=[K1],[];t0,t1=[],[K1]
 while r1:
  q,r=wdiv(r0,r1)
  r0,r1=r1,r
  s0,s1=s1,ps(s0,pm(q,s1));t0,t1=t1,ps(t0,pm(q,t1))
 if r0:
  iv=r0[-1].inverse();r0=pc(r0,iv);s0=pc(s0,iv);t0=pc(t0,iv)
 assert not ps(r0,pa(pm(s0,a),pm(t0,b)))
 counts['newOmegaBezoutReturns']+=1
 return r0,s0,t0
def wpow(p,n):
 out=[K1]
 for _ in range(n):out=pm(out,p)
 return out
def winfo(p):
 raw=json.dumps([v.coordinates() for v in trim(p)],separators=(',',':')).encode()
 return {'omegaDegree':len(trim(p))-1,'constantDegree':40,
         'coefficientBytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
qomega=[peval(v,lamstar) for v in qw]
assert len(qomega)==3 and qomega[2]==K1
FH=[peval(v,lamstar) for v in state['fhat']]
TH=[peval(v,lamstar) for v in state['that']]
assert len(FH)<=2 and len(TH)<=2
fpowers=[wpow(FH,j) for j in range(4)]
tpowers=[wpow(TH,j) for j in range(4)]
def specialize_original(value,limit):
 # Exact polynomial in omega BEFORE any q_omega reduction.  The
 # original value is a polynomial in the SAME f,t of total degree limit.
 out=[]
 for (i,j),coefficient in env['coefficients'](value,limit).items():
  tick();c=peval(cv(coefficient),lamstar)
  out=pa(out,pc(pm(fpowers[i],tpowers[j]),c))
 return trim(out)
raw_original=[specialize_original(value,2) for value in env['original']]
for i,raw in enumerate(raw_original):
 quotient,remainder=wdiv(raw,qomega)
 expected=trim([peval(v,lamstar) for v in linear[i]])
 assert not ps(remainder,expected)
 assert not ps(raw,pa(pm(quotient,qomega),expected))
 counts['newCompleteOriginalCoordinateReturns']+=max(3,len(raw))
# The original q identity is returned at this NEW exact lambda point.
tags=[peval(cv(v),lamstar) for v in env['tag']]
qret=[]
for tag,raw in zip(tags,raw_original):qret=pa(qret,pc(raw,tag))
assert not ps(qret,qomega)
counts['newCompleteOriginalCoordinateReturns']+=3
say('new_F40_complete_original_I4_at_lambda_one',
 wholeConstantFieldKept=True,monicOmegaQuadratic=winfo(qomega),
 fourRawOriginalOmegaDegrees=[len(v)-1 for v in raw_original],
 allFourOriginalSpecializationsReturned=True,
 originalMonicOmegaCombinationReturned=True,
 noOriginalOmegaLinearHeadInverted=True,
 necessaryQQEnvironmentDimension=80)
# These two complete values are NEW at lambda=lambda*, not the old
# lambda-six quotient rows or any old rational matrix.
raw_original.extend([specialize_original(env['NS'],3),
                     specialize_original(env['PS'],3)])
for v in raw_original[4:]:
 q,r=wdiv(v,qomega)
 assert not ps(v,pa(pm(q,qomega),r))
 counts['newCompleteOriginalCoordinateReturns']+=max(4,len(v))
say('new_F40_complete_original_NS_PS_at_lambda_one',
 originalRows=['E1','EBe','EBo','N1','NS','PS'],
 rawOriginalOmegaDegrees=[len(v)-1 for v in raw_original],
 bothCompleteRawWeightedValuesReturned=True,
 allLambdaAndOmegaMultiplicityKept=True,
 noDOrOmegaHeadInverse=True)
# NEW whole K40[omega] original ideal.  Every coefficient inverse
# is checked in the complete K40, never at one selected embedding.
h=qomega[:];beta_q=[K1];beta=[]
for i,row in enumerate(raw_original):
 tick();hh,a,b=wxgcd(h,row)
 beta_q=pm(a,beta_q);beta=[pm(a,c) for c in beta]+[b];h=hh
 check=pm(beta_q,qomega)
 for mult,raw in zip(beta,raw_original):check=pa(check,pm(mult,raw))
 assert not ps(check,h)
 say('new_F40_original_omega_ideal_checkpoint',
  throughOriginalRow=i,throughOriginalName=['E1','EBe','EBo','N1','NS','PS'][i],
  monicOmegaDegree=len(h)-1,completeOriginalPolynomialBezoutReturned=True)
 if len(h)==1:
  beta.extend([[] for _ in range(5-i)])
  break
assert len(beta)==6 and h and h[-1]==K1
# Remove q from the final representation by its ACTUAL original I4 tag.
original_beta=[c[:] for c in beta]
for i in range(4):original_beta[i]=pa(original_beta[i],pc(beta_q,tags[i]))
ret=[]
for mult,raw in zip(original_beta,raw_original):ret=pa(ret,pm(mult,raw))
assert not ps(ret,h)
counts['newCompleteOriginalCoordinateReturns']+=max(len(ret),len(h))
excluded=len(h)==1
physical_power=None
target_profiles=[]
if not excluded:
 # Dval has its original same-point value identity:
 # ell*(2*lambda^2-2*lambda+1)-T^2 = b*c*(h_U-k_U)^2.
 # It is only a positive target, never inverted.
 Traw=specialize_original(env['T'],1)
 ell=peval(cv(env['ell']),lamstar)
 Dval=ps([ell*(2*lamstar*lamstar-2*lamstar+1)],pm(Traw,Traw))
 for power in (1,2):
  tick();target=wpow(Dval,power);quotient,remainder=wdiv(target,h)
  target_profiles.append({'power':power,'remainder':winfo(remainder)})
  if remainder:continue
  mults=[pm(quotient,c) for c in original_beta]
  returned=[]
  for mult,raw in zip(mults,raw_original):returned=pa(returned,pm(mult,raw))
  assert not ps(returned,target)
  counts['newPhysicalTargetCoordinateReturns']+=max(len(target),len(returned))
  physical_power=power;excluded=True
  say('new_F40_original_positive_Dval_power_return',
   power=power,entireOriginalPolynomialReturned=True,
   noDvalOrNormInverse=True,allComplexAndNonreducedFibersKept=True)
  break
say('new_F40_lambda_one_complete_original_result',
 originalMonicOmegaRelation=winfo(h),
 rawQQQuotientDimension=40*(len(h)-1),
 wholeF40Excluded=excluded,unitIdealReturned=len(h)==1,
 positiveOriginalDvalPower=physical_power,physicalTargetProfiles=target_profiles,
 physicalDNonzeroScope=True,allConstantEmbeddingsKept=True,
 old480RationalMatrixAndOldTargetsNotExecuted=True,
 coefficientPayloadNotSaved=True,
 otherWeightFactorsNotTested=True,wholePhiExcluded=False,
 statistics=counts,
 sourceSHA256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
 ordinaryISPClaim=False)
