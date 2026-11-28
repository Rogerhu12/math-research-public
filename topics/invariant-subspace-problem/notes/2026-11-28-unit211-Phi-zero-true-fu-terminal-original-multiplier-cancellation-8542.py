#!/usr/bin/env python3
"""NEW true Phi f=u: terminal original multipliers, not the coarse DAG LCM.
Only the already fixed first 18 original columns are reconstructed.
Their terminal coefficients are actually accumulated and returned in
all 12 coordinates.  The monic-Psi remainder is composed with the
necessary first 3x3 original Psi source.  Only the FINAL actual original
multipliers determine the new pure-u cover, with exponent one.
No old 24-column gate, C92 LCM, three-cofactor/gcd gate, or D action.
120 seconds / 1 GiB; nested absolute deadline; no coefficient payload.
"""
import hashlib,json,math,os,pathlib,resource,signal,time
from flint import fmpq_poly
START=time.perf_counter();DEADLINE=START+120
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
RAW_ALARM=signal.alarm
def bounded_alarm(seconds):
 if seconds<=0:return RAW_ALARM(0)
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute boundary')
 return RAW_ALARM(max(1,min(int(seconds),math.ceil(DEADLINE-time.perf_counter()))))
signal.alarm=bounded_alarm;signal.alarm(120)
BASENAME='2026-11-28-unit211-Phi-zero-true-fu-same-point-twelve-by-twentyfour-8542.py'
BASE_SHA='e35e019e9ee84448b8e4e5afc31c81f449b8b515598329e2fb8c2e38d4870aa6'
path=pathlib.Path(__file__).with_name(BASENAME)
if not path.exists():path=pathlib.Path(os.environ.get('ISP_INPUT_DIR',''))/BASENAME
full=path.read_text();assert hashlib.sha256(full.encode()).hexdigest()==BASE_SHA
MARKER="targets=[('one',flatten(oneP))]";assert full.count(MARKER)==1
original_prefix=full[:full.index(MARKER)]
prefix=original_prefix
def replace_once(a,b):
 global prefix
 assert prefix.count(a)==1
 prefix=prefix.replace(a,b)
# The nested original definition input is restricted to E,O,N; the
# actual NS/PS formulas and all their six unused columns are omitted.
replace_once("prefix=full[:full.index(MARKER)]",
 """nested_original_prefix=full[:full.index(MARKER)]
nested_lines=nested_original_prefix.splitlines()
nested_drop=[line for line in nested_lines if line.startswith('NS=pure(') or line.startswith('PS=pure(')]
assert len(nested_drop)==2
prefix='\\n'.join(line for line in nested_lines if line not in nested_drop)+'\\n'
old="original=[EB[0],EB[1],N1,NS,PS];names=['EBe','EBo','N1','NS','PS']"
assert prefix.count(old)==1
prefix=prefix.replace(old,"original=[EB[0],EB[1],N1];names=['EBe','EBo','N1']")""")
replace_once("assert len(prepared)==len(original)==len(input_scales)==5",
             "assert len(prepared)==len(original)==len(input_scales)==3")
replace_once("spec=[(0,0),(0,1),(1,0),(1,1),(2,0),(2,1),(3,0),(4,0)]",
             "spec=[(0,0),(0,1),(1,0),(1,1),(2,0),(2,1)]")
replace_once("assert len(inputs)==24","assert len(inputs)==18")
replace_once("originalInputColumns=24","originalInputColumns=18")
state={'__name__':'isp_fu_only_fixed_18_definition_DAG',
       '__file__':str(path),'print':lambda *a,**kw:None}
exec(compile(prefix,str(path)+'#only_fixed_18_definitions','exec'),state)
signal.alarm=bounded_alarm;signal.alarm(120)
orig=state['env'];R=state['R'];ctx=state['ctx']
up,Qp,yp,Tp,zp=ctx.gens();oneP=ctx.constant(1);zeroP=ctx.constant(0)
Fr=state['Fr'];nodes=state['nodes'];inputs=state['inputs']
prepared=state['prepared'];raw=state['original'];scales=state['input_scales']
Psi=state['Psi'];DIM=12
assert len(inputs)==18 and len(raw)==3 and len(state['basis'])==12
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,sort_keys=True),flush=True)
def tick():
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute boundary')
def pinfo(p):
 out={'degree':int(p.degree()),
      'sha256':hashlib.sha256(str(p).encode()).hexdigest()}
 if p and int(p.degree())<=12:out['polynomial']=str(p)
 return out
say('new_fu_only_fixed_eighteen_original_definition_input',
 originalFullSourceSHA256=BASE_SHA,
 originalNecessaryPrefixSHA256=hashlib.sha256(original_prefix.encode()).hexdigest(),
 actuallyUsedPrefixSHA256=hashlib.sha256(prefix.encode()).hexdigest(),
 nestedActuallyUsedOriginalPrefixSHA256=hashlib.sha256(state['prefix'].encode()).hexdigest(),
 necessaryOriginalColumns=18,definitionDAGNodes=len(nodes),
 noNSPSDefinitionsOrLastSixColumns=True,
 noOldC92LCMOrFactorSupportGate=True)
target=state['flatten'](oneP)
rem,comb=state['reduce_target'](target);assert not any(rem)
weights=dict(comb);coeff=[Fr() for _ in inputs];reachable=set()
for n in sorted(range(len(nodes)),reverse=True):
 tick();c=weights.get(n,Fr())
 if not c:continue
 reachable.add(n);node=nodes[n]
 if node['seed'] is not None:
  coeff[node['seed']]=coeff[node['seed']]+c*node['seed_scale']
 else:
  for parent,a in node['parents']:
   weights[parent]=weights.get(parent,Fr())+c*a
for j in range(DIM):
 assert sum((c*Fr(v[j]) for c,v in zip(coeff,inputs)),Fr())==Fr(int(j==0))
say('new_fu_terminal_eighteen_actual_original_coefficients',
 allTwelveCoordinatesReturned=True,reachableDefinitionNodes=len(reachable),
 nonzeroOriginalCoefficients=sum(bool(c) for c in coeff),
 actualCoefficientDenominatorDegrees=[int(c.d.degree()) for c in coeff],
 noCoarseDAGLCMComputed=True)
def rat(c):return R(state['multivar'](c.n),state['multivar'](c.d))
beta=[R() for _ in raw]
for c,(row,shift,k) in zip(coeff,state['input_descriptions']):
 beta[row]+=rat(c)*R(Qp**k*yp**shift)
difference=sum((b*R(v) for b,v in zip(beta,prepared)),R())-1
assert state['pure_u'](difference.d)
rr,quot=state['qreduce'](difference.n)
assert not rr
kappa=R(quot,difference.d)
assert difference==kappa*R(Psi)
# The necessary original source of Psi is only the first fixed 3x3
# adjugate definition from E,O,N.  No previous three-cofactor/gcd gate.
coef=orig['coef']
matrix=[[coef(prepared[i],j) for j in range(3)] for i in range(3)]
def det2(a,b,c,d):return a*d-b*c
cof=[]
for i in range(3):
 I=[j for j in range(3) if j!=i]
 cof.append((-1)**i*det2(matrix[I[0]][1],matrix[I[0]][2],
                         matrix[I[1]][1],matrix[I[1]][2]))
det0=sum((cof[i]*matrix[i][0] for i in range(3)),zeroP)
assert det0
for j in range(3):
 assert sum((cof[i]*matrix[i][j] for i in range(3)),zeroP)==(det0 if j==0 else zeroP)
psi_source=[R(Psi*c,det0) for c in cof]
for c in psi_source:assert orig['supported'](c.d)
assert sum((c*R(v) for c,v in zip(psi_source,prepared)),R())==R(Psi)
actual_prepared=[beta[i]-kappa*psi_source[i] for i in range(3)]
assert sum((c*R(v) for c,v in zip(actual_prepared,prepared)),R())==1
actual=[actual_prepared[i]/scales[i] for i in range(3)]
assert sum((c*v for c,v in zip(actual,raw)),R())==1
# NS and PS have actual zero multipliers; they were not recomputed.
say('new_fu_full_original_terminal_multipliers_returned',
 allEONCompletePolynomialMultipliersReturned=True,
 fiveOriginalMultipliersWithNSPSExactlyZero=True,
 fullOriginalPolynomialPsiDivisionReturned=True,
 necessaryPsiOriginalThreeByThreeSourceReturned=True,
 noTemporaryDeterminantDeclaredPhysicalUnit=True,
 noOldThreeCofactorOrGCDGate=True)
# u is independently paid by the true Frobenius zero-base-mean theorem.
# The new theta unit is deliberately unnecessary in this source.
paid=orig['paid']*up
new_divisions=0
def mex(a,b):
 global new_divisions
 q,r=divmod(a,b);assert not r and q*b==a
 new_divisions+=1;return q
def strip_actual_den(p):
 assert orig['weight'](p);rem=p
 while rem and int(rem.total_degree())>0:
  g=rem.gcd(paid)
  if int(g.total_degree())<=0:break
  rem=mex(rem,g)
 return rem
C=fmpq_poly([1])
den_profiles=[]
for c in actual:
 rest=strip_actual_den(c.d)
 assert state['pure_u'](rest),('unpaid non-u denominator',str(rest))
 cp=state['univar'](rest)
 C=state['plcm'](C,cp)
 den_profiles.append({'fullWeightDenominatorDegrees':list(map(int,c.d.degrees())),
                      'unpaidPureUDenominator':pinfo(cp)})
Cpoly=state['multivar'](C)
scaled=[R(Cpoly)*c for c in actual]
for c in scaled:
 rest=strip_actual_den(c.d)
 assert rest and int(rest.total_degree())==0
assert sum((c*v for c,v in zip(scaled,raw)),R())==R(Cpoly)
say('new_fu_final_original_once_cover',
 actualOriginalMultiplierDenominators=den_profiles,
 retainedPureUCover=pinfo(C),exponent=1,
 fullOriginalIdentity='Cnew=sum_i Omega_i*Fi in the paid original ring; NS/PS multipliers zero',
 allFullPolynomialMultiplierProductsReturned=True,
 independentlyPaidUZeroSource='R150-appendix-essential-four-unit-two-plus-one-plus-one-zero-base-mean-exclusion.md',
 thetaNewUnitUsed=False,
 allNewPureUZeroFibersKept=True,noYHeadOrPhysicalDInverse=True,
 differentUPointUpperBound=int(C.degree()),
 differentWeightPairUpperBound=3*int(C.degree()),
 completeOriginalPointFinitenessClaim=False,
 wholeFuExcluded=int(C.degree())==0,
 newExactDenominatorDivisions=new_divisions,
 originalDefinitionStatistics=state['stats'],
 wholePhiExcluded=False,ordinaryISPClaim=False)
if C and int(C.degree())>0:
 const,factors=C.factor();prod=fmpq_poly([const]);rad=fmpq_poly([1]);power=0
 profiles=[]
 for f,e in factors:
  e=int(e);prod*=f**e;rad*=f;power=max(power,e)
  profiles.append({'factor':pinfo(f),'multiplicity':e})
 assert prod==C
 q,r=divmod(rad**power,C);assert not r and q*C==rad**power
 say('new_fu_terminal_exact_factor_support',
     factors=profiles,radical=pinfo(rad),maximumMultiplicity=power,
     completeQQFactorProductAndRadicalPowerDivisionReturned=True,
     differentUPointUpperBound=int(rad.degree()),
     differentWeightPairUpperBound=3*int(rad.degree()),
     allFactorZeroFibersKept=True,completeOriginalPointFinitenessClaim=False,
     wholeFuExcluded=False,wholePhiExcluded=False,ordinaryISPClaim=False)
