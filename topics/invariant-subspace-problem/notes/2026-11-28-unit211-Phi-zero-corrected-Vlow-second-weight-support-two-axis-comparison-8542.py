#!/usr/bin/env python3
"""NEW correct Phi: complete Vlow gives a second fixed pure-weight support.
Known C6(t), C8_N(t), and the two old C6(lambda) are ONLY coefficient
parameters, regenerated from pinned necessary definitions. No prior
ordinary-source, action, scalar, head-factor, or point proof gate is run.
Define the new fixed 14x14 t resultant by its universal adjugate.
On the PREDETERMINED p=1009, Q=2 and u=2 slices, compute full polynomial
determinants and common gcds with the known fixed12 lambda support.
Each coordinate direction has a rigorous QQ degree upper bound and a
returned leading-matrix witness. Both directions are required before a
QQ no-common-curve claim. No modular paid-factor deletion is permitted.
No expanded QQ bivariate determinant, coefficient payload, or cache.
Absolute 120 seconds / 1 GiB. Four pinned SMALL source dependencies.
"""
import ast,hashlib,json,math,os,pathlib,resource,signal,time
from fractions import Fraction
from functools import reduce
from flint import nmod_poly
ROOT_START=time.perf_counter();ROOT_DEADLINE=ROOT_START+120
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
ORIGINAL_TIMER=signal.setitimer
def tick():
 if time.perf_counter()>=ROOT_DEADLINE:raise TimeoutError('absolute 120-second boundary')
def bounded_timer(which,seconds,interval=0):
 assert which==signal.ITIMER_REAL and not interval
 tick();remaining=ROOT_DEADLINE-time.perf_counter()
 duration=remaining if seconds<=0 else min(float(seconds),remaining)
 return ORIGINAL_TIMER(which,max(0.000001,duration),0)
def bounded_alarm(seconds):
 old=bounded_timer(signal.ITIMER_REAL,seconds)
 return int(math.ceil(old[0]))
signal.setitimer=bounded_timer;signal.alarm=bounded_alarm
bounded_timer(signal.ITIMER_REAL,120)
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-ROOT_START)
 print(json.dumps(kw,sort_keys=True,separators=(',',':')),flush=True)
PRIME=1009
SLICES=[('u',0,2),('Q',1,2)]
assert all(PRIME%d for d in range(2,math.isqrt(PRIME)+1))
DEPENDENCIES=[
 ('Vlow','2026-11-28-unit211-Phi-zero-corrected-t-complete-Vlow-two-original-cofactors-8542.py',
  '0800a0f6ba0cad4cc4ddc7a592525c198bcc213bfa36df568ec0e9301b8f4335'),
 ('fixed12','2026-11-28-unit211-Phi-zero-corrected-two-sextics-fixed-lambda-resultant-support-8542.py',
  '39631a64da054107209d296765b755e2fe25a685f5734cb5607165dd39100b7b'),
 ('fifteen','2026-11-28-unit211-Phi-zero-corrected-whole-original-I6-fifteen-by-three-8542.py',
  '84e0efcc19a0274d571484b187b7b155c81ebf255e40a39c38ac13a03f911cf0'),
 ('truehead','2026-11-28-unit211-Phi-zero-corrected-dual-germ-four-original-quadratic-heads-8542.py',
  '5ee86ff89db7c8babaf3a22c7d72570dcdfbbf92646f56adf37bff854a87ace7')]
paths={};texts={}
for label,basename,known in DEPENDENCIES:
 path=pathlib.Path(__file__).with_name(basename)
 if not path.exists():path=pathlib.Path(os.environ.get('ISP_INPUT_DIR',''))/basename
 full=path.read_text()
 assert hashlib.sha256(full.encode()).hexdigest()==known
 paths[label]=path;texts[label]=full
say('new_two_supports_fixed_input',
 prime=PRIME,slices=[dict(variable=s[0],otherCoordinate=2) for s in SLICES],
 allFourFullSourceSHA256CheckedBeforeAnyDefinitionExecution=True,
 noPostGCDPrimeSliceOrPointChoice=True,modularPaidFactorDeletionForbidden=True)

# ONLY the true raw t mean/N1/NS/PS coefficient definitions, before the
# previous reduction/trace/cubic-pair/full-Vlow proof sections.
marker='# Necessary deterministic coefficient/trace definitions only.'
full=texts['Vlow'];assert full.count(marker)==1
prefix=full[:full.index(marker)]
assert len(prefix)==8247
assert hashlib.sha256(prefix.encode()).hexdigest()=='84424bf3fe62591fc4f9316b5809d6240cca96fd01cd196f411157c085ef2e1f'
kept=[];omitted=[]
for node in ast.parse(prefix,str(paths['Vlow'])).body:
 skip=isinstance(node,(ast.Assert,ast.For))
 if isinstance(node,ast.Assign):
  names={t.id for t in node.targets if isinstance(t,ast.Name)}
  skip=skip or bool(names&{'START','DEADLINE'})
 if isinstance(node,ast.Expr) and isinstance(node.value,ast.Call):
  fun=node.value.func
  skip=skip or isinstance(fun,ast.Name) and fun.id=='say'
  skip=skip or isinstance(fun,ast.Attribute) and fun.attr in ('setrlimit','setitimer')
 if skip:omitted.append([node.lineno,type(node).__name__])
 else:kept.append(node)
ns={'__name__':'known_true_t_coefficient_definitions','__file__':str(paths['Vlow']),
    'START':ROOT_START,'DEADLINE':ROOT_DEADLINE,'print':lambda *a,**kw:None}
exec(compile(ast.fix_missing_locations(ast.Module(body=kept,type_ignores=[])),
             str(paths['Vlow'])+'#8247-definition-bytes-only','exec'),ns)
signal.alarm=bounded_alarm;signal.setitimer=bounded_timer
R=ns['R'];ctx=ns['ctx'];O=ns['O'];Z=ns['Z']
u,Q,t,f,V=(ns[k] for k in ('u','Q','t','f','V'))
up,Qp=(ns[k] for k in ('up','Qp'))
ell,m,delta,M,bc,P02,T0,J=(ns[k] for k in
 ('ell','m','delta','M','bc','P02','T0','J'))
lam,T,w,W1,A1=(ns[k] for k in ('lam','T','w','W1','A1'))
A2,B3=ns['A2'],ns['B3']
exact=ns['exact'];profile=ns['profile'];strip=ns['strip']
rules=ns['rules'];rN=ns['rN']
paid6=up*Qp*(1-Qp)*(up-1)*ns['Kw'].n*ns['L'].n*ns['Mn'].n*ns['gg'].n
paid8=paid6*m.n
def reduced_parameter(value,cap):
 # Coefficient recurrence only: no old raw trace/tag or action return gate.
 work=ns['coeffs'](value,cap)
 while True:
  tick()
  active=[key for key,val in work.items() if val and sum(key)>=2]
  if not active:break
  i,j=max(active,key=lambda ij:(sum(ij),ij))
  coefficient=work.pop((i,j))
  if i>=2:which,ii,jj=0,i-2,j
  elif i and j:which,ii,jj=1,i-1,j-1
  else:which,ii,jj=2,i,j-2
  for k,inc in enumerate(((0,0),(1,0),(0,1))):
   at=(ii+inc[0],jj+inc[1])
   work[at]=work.get(at,R())+coefficient*rules[which][k]
 return [work.get(key,R()) for key in ((0,0),(1,0),(0,1))]
rNS,rPS=[reduced_parameter(value,3) for value in ns['raw_values']]
def tc(value,k):
 return R(ctx.from_dict({(ex[0],ex[1],0,0,0):cc
         for ex,cc in value.n.to_dict().items() if int(ex[2])==k}),value.d)
af,bf=tc(rN[1],1),tc(rN[1],0)
av,bv=tc(rN[2],1),tc(rN[2],0)
slope=af*bv-bf*av
# This is the already published scalar's DEFINITION, not a new slope inverse
# on the physical chart. Its whole original identity was separately paid.
omegaNS=(rN[2]*rNS[1]-rN[1]*rNS[2])/slope
omegaPS=(rN[2]*rPS[1]-rN[1]*rPS[2])/slope
pair=[omegaPS,-omegaNS];den=O
for a in pair:den=exact(den,den.gcd(a.d))*a.d
# Existing common content was exactly 1; no old gcd gate is repeated.
mu=[R(a.n*exact(den,a.d)) for a in pair]
kappa=(mu[0]*(-av*rNS[1]+af*rNS[2])
       +mu[1]*(-av*rPS[1]+af*rPS[2]))/slope
value6=-kappa*rN[0]+mu[0]*rNS[0]+mu[1]*rPS[0]
C6,unused=strip(value6.n,paid6);C6/=C6.coefficient(0)
assert profile(C6)['sha256']=='5041106f2793c3a95fb8c0fdc1a177e23de00e18bce476efb2e42b871d926be1'

# Complete Vlow parameter, not a component or a Phi multiple.
D=ell*A2-T*T
Kval=ell*ell*B3-3*ell*A2*T+2*T**3
cl=3-2*lam
Z0=(ell*ell*A1+4*ell*ell*(1-2*lam)*f+2*ell*f*D
    +2*ell*u*w*(ell*cl+T)
    +2*V*(ell*ell+ell*cl*T+T*T)+2*bc*t*(T*T-ell*ell))
Z1=2*(ell*cl+2*T)*(u*V-ell*W1)-2*ell*M*w+4*bc*m*T*t
Z2=2*((u*u-ell*ell*Q)*V-2*m*ell*W1-ell*M*f-bc*M*t)
Vlow=D*Z0+Kval*Z1/(2*m)+D*D*Z2/M
rVL=reduced_parameter(Vlow,5)
expectedVL=['baa8cd4b46098d259783d15a7012b550bdb2a29bee95c12912e0b9a5e5c4aee7',
 '9e6cb8870a5c0853b910076ba0c2bd0f6059338f53b302ead34889237ceec108',
 '8e60199f7e082e438cad0c4d324811a2fc70163562429f7b162382397ead1cbe']
assert [profile(a.n)['sha256'] for a in rVL]==expectedVL
rr=[rN,rNS,rVL]
mu8=[rr[1][1]*rr[2][2]-rr[1][2]*rr[2][1],
     rr[2][1]*rr[0][2]-rr[2][2]*rr[0][1],
     rr[0][1]*rr[1][2]-rr[0][2]*rr[1][1]]
den=O
for a in mu8:den=exact(den,den.gcd(a.d))*a.d
# This triple's already returned common content was also exactly 1.
nums=[a.n*exact(den,a.d) for a in mu8]
value8=sum((R(nums[i])*rr[i][0] for i in range(3)),R())
C8,unused=strip(value8.n,paid8);C8/=C8.coefficient(0)
assert profile(C8)['sha256']=='7be3f86635bb87c309fc15c6b386303624c0ca951e8578dce37d490fc925d3ea'
say('necessary_original_t_C6_C8_parameter_identities',
 C6=profile(C6),C8=profile(C8),wholeVlowRowProfilesMatched=True,
 originalSource='C6 in I6; C8 in I6+(complete Vlow)',
 onlyNecessaryCoefficientDefinitionsRegenerated=True,
 omittedOldTopLevelStatements=omitted,
 noOldFullMeanTracePairSixMultiplierOrHeadFactorGateExecuted=True)

# Old F12 is needed ONLY as a polynomial parameter in the NEW common-support
# test. Stop before its old degree/point/Bezout/determinant proof gate.
markerF='def evaluate_weight(poly,u0,q0):'
fullF=texts['fixed12'];assert fullF.count(markerF)==1
prefixF=fullF[:fullF.index(markerF)]
assert len(prefixF)==6371
assert hashlib.sha256(prefixF.encode()).hexdigest()=='4e49026df6f798e62370af93c1ff821b698b82011ed797a72137bab24a358b16'
fs={'__name__':'known_fixed12_original_coefficient_definitions',
    '__file__':str(paths['fixed12']),'print':lambda *a,**kw:None}
exec(compile(prefixF,str(paths['fixed12'])+'#6371-definition-bytes-only','exec'),fs)
signal.alarm=bounded_alarm;signal.setitimer=bounded_timer;tick()
assert [fs['profile'](v['core'])['sha256'] for v in fs['models']]==[
 'fcf79be98410a2eea2ebdb588b441b8f4aceb20acb4704a96ee34fc0012d01d5',
 '2407107501f1790a288ecabd75f14f92c7602859bfc033727b76312675f91014']

def wdict(p):
 out={}
 for ex,c in p.to_dict().items():
  assert not any(int(e) for e in ex[2:])
  value=Fraction(str(c));assert value.denominator==1
  out[(int(ex[0]),int(ex[1]))]=value.numerator
 return out
def integer_model(label,p,degree):
 data={ex:Fraction(str(c)) for ex,c in p.to_dict().items()}
 assert all(not any(int(e) for e in ex[3:]) and int(ex[2])<=degree for ex in data)
 dd=1
 for c in data.values():dd=math.lcm(dd,c.denominator)
 vals={ex:c.numerator*(dd//c.denominator) for ex,c in data.items()}
 content=reduce(math.gcd,(abs(c) for c in vals.values()))
 assert content>0
 vals={ex:c//content for ex,c in vals.items()}
 actual=ctx.from_dict(vals)
 assert actual*content==p*dd
 coeff=[]
 for j in range(degree+1):
  coeff.append({(int(ex[0]),int(ex[1])):c for ex,c in vals.items() if int(ex[2])==j})
 assert coeff[-1]
 return dict(label=label,coefficients=coeff,degree=degree,
             total=int(p.total_degree()),scale=str(Fraction(dd,content)),
             integerProfile=profile(actual))
tmodels=[integer_model('whole_t_C6',C6,6),integer_model('complete_Vlow_t_C8N',C8,8)]
lmodels=[dict(label=v['label'],coefficients=[wdict(p) for p in v['coefficients']],
              degree=6,total=v['total'],scale=str(v['scale']),
              integerProfile=fs['profile'](v['integer'])) for v in fs['models']]
def sylvester_models(pair):
 a,b=pair;m,n=a['degree'],b['degree'];size=m+n
 mat=[];rowweights=[]
 for model,count in ((a,n),(b,m)):
  for shift in range(count):
   row=[{} for _ in range(size)]
   for j,co in enumerate(model['coefficients']):row[shift+j]=co
   mat.append(row);rowweights.append(model['total']+shift)
 colweights=[-j for j in range(size)]
 checks=0
 for i,row in enumerate(mat):
  for j,co in enumerate(row):
   if co:
    assert max(sum(ex) for ex in co)<=rowweights[i]+colweights[j]
    checks+=1
 return dict(matrix=mat,size=size,totalUpper=sum(rowweights)+sum(colweights),
             rows=rowweights,columns=colweights,entryChecks=checks)
fixedF=sylvester_models(lmodels);fixedG=sylvester_models(tmodels)
assert fixedF['size']==12 and fixedF['totalUpper']==444
assert fixedG['size']==14 and fixedG['totalUpper']==730
say('new_fixed14_original_complete_Vlow_weight_support_defined',
 definition='G=det Sylvester_t(integer C6,integer C8N), capacities 6 and 8',
 universalAdjugateOriginalIdentity=True,
 originalIdeal='I6+(complete Vlow)',allOriginalLeadingZeroFibersRetained=True,
 fixed14TotalWeightDegreeUpperBound=fixedG['totalUpper'],
 fixed14DegreeRowWeights=fixedG['rows'],fixed14DegreeColumnWeights=fixedG['columns'],
 fixed14ActualEntryBounds=fixedG['entryChecks'],
 originalFixed12SupportUsedOnlyAsComparisonParameter=True,
 originalFixed12TotalUpper=fixedF['totalUpper'],
 noQQBivariateDeterminantExpanded=True,
 originalParameterIntegerScalings=[dict(label=v['label'],scale=v['scale'],
 integerProfile=v['integerProfile']) for v in tmodels+lmodels])

def axis_degree(co,axis):
 return max((ex[axis] for ex in co),default=-1)
def hungarian_upper(mat,axis):
 """Exact integer assignment dual. Zero entries are FORBIDDEN, not degree 0."""
 n=len(mat);degs=[[axis_degree(c,axis) for c in row] for row in mat]
 big=10**6
 costs=[[-d if d>=0 else big for d in row] for row in degs]
 pu=[0]*(n+1);pv=[0]*(n+1);p=[0]*(n+1);way=[0]*(n+1)
 for i in range(1,n+1):
  p[0]=i;j0=0;minv=[10**12]*(n+1);used=[False]*(n+1)
  while True:
   used[j0]=True;i0=p[j0];delta0=10**12;j1=0
   for j in range(1,n+1):
    if not used[j]:
     cur=costs[i0-1][j-1]-pu[i0]-pv[j]
     if cur<minv[j]:minv[j]=cur;way[j]=j0
     if minv[j]<delta0:delta0=minv[j];j1=j
   assert j1
   for j in range(n+1):
    if used[j]:pu[p[j]]+=delta0;pv[j]-=delta0
    else:minv[j]-=delta0
   j0=j1
   if p[j0]==0:break
  while True:
   j1=way[j0];p[j0]=p[j1];j0=j1
   if j0==0:break
 assignment=[None]*n
 for j in range(1,n+1):assignment[p[j]-1]=j-1
 if any(degs[i][j]<0 for i,j in enumerate(assignment)):
  return None
 a=[-pu[i+1] for i in range(n)];b=[-pv[j+1] for j in range(n)]
 for i,row in enumerate(degs):
  for j,d0 in enumerate(row):
   if d0>=0:assert d0<=a[i]+b[j]
 bound=sum(a)+sum(b)
 assert bound==sum(degs[i][j] for i,j in enumerate(assignment))
 return dict(bound=bound,rowWeights=a,columnWeights=b,assignment=assignment)

def modular_polynomial(co,axis,fixed):
 n=axis_degree(co,axis)+1;out=[0]*n
 for ex,c in co.items():
  out[ex[axis]]=(out[ex[axis]]+c*pow(fixed,ex[1-axis],PRIME))%PRIME
 return nmod_poly(out,PRIME)
def modular_head(co,axis,d0,fixed):
 if d0<0:return 0
 return sum(c*pow(fixed,ex[1-axis],PRIME) for ex,c in co.items()
            if ex[axis]==d0)%PRIME
def numeric_det_return(S):
 n=len(S);mat=[row[:] for row in S]
 E=[[int(i==j) for j in range(n)] for i in range(n)]
 rank=0;sign=1
 for col in range(n):
  pr=next((i for i in range(rank,n) if mat[i][col]),None)
  if pr is None:continue
  if pr!=rank:
   mat[rank],mat[pr]=mat[pr],mat[rank]
   E[rank],E[pr]=E[pr],E[rank];sign=-sign
  iv=pow(mat[rank][col],-1,PRIME)
  for i in range(rank+1,n):
   cc=mat[i][col]*iv%PRIME
   if cc:
    mat[i]=[(x-cc*y)%PRIME for x,y in zip(mat[i],mat[rank])]
    E[i]=[(x-cc*y)%PRIME for x,y in zip(E[i],E[rank])]
  rank+=1
  if rank==n:break
 for i in range(n):
  for j in range(n):
   assert sum(E[i][k]*S[k][j] for k in range(n))%PRIME==mat[i][j]
 determinant=0
 if rank==n:
  determinant=sign
  for i in range(n):determinant=determinant*mat[i][i]%PRIME
 return determinant%PRIME,rank,n*n
stats=dict(newPolynomialBareissProducts=0,newPolynomialEuclideanProducts=0,
           newHighestMatrixCoordinates=0)
def poly_profile(p):
 values=[int(p[i]) for i in range(int(p.degree())+1)] if p else []
 raw=json.dumps(values,separators=(',',':')).encode()
 return dict(degree=int(p.degree()) if p else -1,
             nonzeroTerms=sum(bool(c) for c in values),bytes=len(raw),
             sha256=hashlib.sha256(raw).hexdigest())
def polynomial_det(S,label,axis_name):
 n=len(S);mat=[row[:] for row in S]
 previous=nmod_poly([1],PRIME);sign=1
 for k in range(n-1):
  tick()
  pr=next((i for i in range(k,n) if mat[i][k]),None)
  if pr is None:
   say('new_fixed_polynomial_determinant_identically_zero',
       support=label,variable=axis_name,stoppedColumn=k,
       noPostTestSliceChange=True)
   return nmod_poly([],PRIME)
  if pr!=k:mat[k],mat[pr]=mat[pr],mat[k];sign=-sign
  pivot=mat[k][k]
  for i in range(k+1,n):
   aik=mat[i][k]
   for j in range(k+1,n):
    numerator=pivot*mat[i][j]-aik*mat[k][j]
    value,rem=divmod(numerator,previous)
    assert not rem and value*previous==numerator
    mat[i][j]=value;stats['newPolynomialBareissProducts']+=1
   mat[i][k]=nmod_poly([],PRIME)
  previous=pivot
  if k in (0,n//2,n-2):
   say('new_fixed_polynomial_determinant_checkpoint',
       support=label,variable=axis_name,size=n,completedStep=k,
       pivot=poly_profile(pivot),exactPolynomialDivision=True)
 return sign*mat[-1][-1]
def xgcd_return(a,b):
 one=nmod_poly([1],PRIME);zero=nmod_poly([],PRIME)
 a0,b0=a,b;r0,r1=a,b;s0,s1=one,zero;t0,t1=zero,one
 while r1:
  tick();q,r=divmod(r0,r1)
  assert q*r1+r==r0
  stats['newPolynomialEuclideanProducts']+=1
  r0,r1=r1,r;s0,s1=s1,s0-q*s1;t0,t1=t1,t0-q*t1
 if not r0:return zero,zero,zero
 iv=pow(int(r0[int(r0.degree())]),-1,PRIME)
 g=iv*r0;s0=iv*s0;t0=iv*t0
 assert s0*a0+t0*b0==g
 return g,s0,t0

axis_results=[];new_G_nonzero=False
for axis_name,axis,fixed in SLICES:
 output=[];polys=[]
 for label,model in (('F12_original_I6',fixedF),('G14_complete_Vlow',fixedG)):
  tick();mat=model['matrix'];du= hungarian_upper(mat,axis)
  if du is not None:
   H=[[modular_head(mat[i][j],axis,du['rowWeights'][i]+du['columnWeights'][j],fixed)
       for j in range(model['size'])] for i in range(model['size'])]
   hd,hr,coords=numeric_det_return(H)
   stats['newHighestMatrixCoordinates']+=coords
  else:hd,hr,coords=0,0,0
  say('new_QQ_axis_degree_upper_and_fixed_modular_leading_witness',
      support=label,variable=axis_name,otherCoordinate=fixed,prime=PRIME,
      assignmentDual=du,leadingDeterminant=hd,leadingMatrixRank=hr,
      completeLeadingTransformationCoordinates=coords,
      noPhysicalLeadingInverse=True,QQDegreePaid=bool(hd))
  S=[[modular_polynomial(co,axis,fixed) for co in row] for row in mat]
  determinant=polynomial_det(S,label,axis_name)
  if du is not None:
   assert not determinant or int(determinant.degree())<=du['bound']
   if hd:
    assert determinant and int(determinant.degree())==du['bound']
    assert int(determinant[du['bound']])==hd
  else:assert not determinant
  if label=='G14_complete_Vlow' and determinant:new_G_nonzero=True
  polys.append(determinant)
  output.append(dict(support=label,actualModularPolynomial=poly_profile(determinant),
                     QQGlobalAxisDegreeUpper=du['bound'] if du else None,
                     QQGlobalDegreeAndThisSlicePreserved=bool(hd),
                     leadingDeterminant=hd))
 g,a,b=xgcd_return(*polys)
 unit=bool(g) and int(g.degree())==0
 preserved=any(v['QQGlobalDegreeAndThisSlicePreserved'] for v in output)
 paid=unit and preserved
 result=dict(variable=axis_name,otherCoordinate=fixed,prime=PRIME,
             supports=output,actualCommonGCD=poly_profile(g),
             firstBezoutMultiplier=poly_profile(a),secondBezoutMultiplier=poly_profile(b),
             completeTwoSupportBezoutReturned=True,
             noModularPaidFactorsRemoved=True,
             strictQQCommonPositiveDegreeExclusion=paid,
             allUnpaidDegreeGapsAndFactorsRetained=not paid)
 axis_results.append(result)
 say('new_two_original_pure_weight_supports_fixed_axis_result',**result)
all_paid=all(v['strictQQCommonPositiveDegreeExclusion'] for v in axis_results)
say('new_complete_Vlow_second_weight_support_comparison_finished',
 sourceSHA256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
 newWholeWeightNecessaryG14ProvedNonzero=new_G_nonzero,
 fixedG14TotalWeightDegreeUpperBound=730,
 twoCoordinateDirectionsActuallyPaid=[v['strictQQCommonPositiveDegreeExclusion'] for v in axis_results],
 QQNoCommonCurveProved=all_paid,
 pureQContentSeparatelyCovered=axis_results[1]['strictQQCommonPositiveDegreeExclusion'],
 originalWeightPointBezoutUpper=444*730 if all_paid else None,
 allHeadZeroAndUnprovedSupportFibresRetained=not all_paid,
 wholePhiExcluded=False,ordinaryISPClaim=False,
 noOldKnownScalarOrFixedPointProofGateReplayed=True,
 noExpandedQQBivariateDeterminantOrCoefficientPayloadSaved=True,
 statistics=stats,peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
ORIGINAL_TIMER(signal.ITIMER_REAL,0)
