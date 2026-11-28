#!/usr/bin/env python3
"""NEW corrected Phi same-sigma odd-N/NV and odd-P/NV original cross rows.
Only necessary old raw Gram/mean/N1 coefficient definitions are regenerated.
No old NSPS, Vlow, centered, scalar, matrix-factor or Q-primary gate.
Each new cross returns all sigma coefficients to its original odd error,
COMPLETE ell^2*N4(Vphys), and the SAME original second moment q.
Then return two ordinary mean traces and one fixed new three-row cofactor.
All D=0, value-leading zero and new t-leading zero loci are retained.
Absolute 120 seconds / 1 GiB. One readable source dependency, no payload.
"""
import ast,hashlib,json,resource,signal,time
from pathlib import Path
START=time.perf_counter();DEADLINE=START+120
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
signal.setitimer(signal.ITIMER_REAL,120)
BASE_NAME='2026-11-28-unit211-Phi-zero-corrected-t-complete-Vlow-two-original-cofactors-8542.py'
BASE_SHA='0800a0f6ba0cad4cc4ddc7a592525c198bcc213bfa36df568ec0e9301b8f4335'
PREFIX_SHA='607238e08c402392a599e84cf13764aac341c6b7f0fb34e29c0ea6667c647abe'
base_path=Path(__file__).with_name(BASE_NAME)
base_text=base_path.read_text()
assert hashlib.sha256(base_text.encode()).hexdigest()==BASE_SHA
prefix=base_text[:7689]
assert prefix.endswith("assert [profile(v.n)['sha256'] for v in rN]==expectedN1\n")
assert hashlib.sha256(prefix.encode()).hexdigest()==PREFIX_SHA
tree=ast.parse(prefix,filename=str(base_path))
kept=[];omitted=[]
for node in tree.body:
 if isinstance(node,ast.Assign):
  names=[target.id for target in node.targets if isinstance(target,ast.Name)]
  if names in (['START'],['DEADLINE']):
   omitted.append(names[0]);continue
 if isinstance(node,ast.Expr) and isinstance(node.value,ast.Call):
  fun=node.value.func
  if isinstance(fun,ast.Attribute) and isinstance(fun.value,ast.Name):
   key=fun.value.id+'.'+fun.attr
   if key in ('resource.setrlimit','signal.setitimer'):
    omitted.append(key);continue
 kept.append(node)
assert omitted==['START','DEADLINE','resource.setrlimit','signal.setitimer']
exec(compile(ast.Module(body=kept,type_ignores=[]),str(base_path)+':necessary7689','exec'),globals())
# The prefix's tick/say functions use the ORIGINAL global START/DEADLINE.
# Its timer/limit assignments alone were omitted, never reset or extended.
statistics.clear()
statistics.update(exactDivisionProducts=0,
 newOddSigmaCoordinates=0,newCrossSigmaCoordinates=0,
 newMeanReductionSteps=0,newOrdinaryMeanIdentities=0,
 newReducedCoordinates=0,newCofactorCoordinates=0,newScalarReturnCoordinates=0)

def geo(value):
 value=checkden(value)
 return max((sum(map(int,ex[2:])) for ex in value.n.to_dict()),default=-1)

# Polynomials in the SAME sigma, stored as full coefficient lists over R.
# No sigma value is chosen; D=0 keeps the full quadratic nilpotent algebra.
def trim(a):
 a=list(a)
 while a and not a[-1]:a.pop()
 return a
def pa(a,b):
 return trim([(a[i] if i<len(a) else R())+(b[i] if i<len(b) else R())
              for i in range(max(len(a),len(b)))])
def pn(a):return [-v for v in a]
def ps(a,b):return pa(a,pn(b))
def pm(a,b):
 if not a or not b:return []
 out=[R() for _ in range(len(a)+len(b)-1)]
 for i,av in enumerate(a):
  for j,bv in enumerate(b):out[i+j]+=av*bv
 return trim(out)
def pc(a,v):return trim([v*x for x in a])
def return_sigma(left,right,label,counter):
 n=max(len(left),len(right))
 for i in range(n):
  aa=left[i] if i<len(left) else R()
  bb=right[i] if i<len(right) else R()
  assert aa==bb,(label,i)
  statistics[counter]+=1

A2=2*lam*lam-2*lam+1
D=ell*A2-T*T
A0=1+T/ell
# Necessary true singleton values, not weighted-NSPS substitutes.
NB=N4(rows[2]);PB=P2(rows[2])
No,Po=NB.b,PB.b
c_lambda=3-2*lam
Z0=(ell*ell*A1+4*ell*ell*(1-2*lam)*f+2*ell*f*D
    +2*ell*u*w*(ell*c_lambda+T)
    +2*V*(ell*ell+ell*c_lambda*T+T*T)
    +2*bc*t*(T*T-ell*ell))
Z1=(2*(ell*c_lambda+2*T)*(u*V-ell*W1)
    -2*ell*M*w+4*bc*m*T*t)
Z2=2*((u*u-ell*ell*Q)*V-2*m*ell*W1-ell*M*f-bc*M*t)
q_sigma=[-D,R(),M]
nv_sigma=[Z0,Z1,Z2]
aNV=Z0+D*Z2/M
return_sigma(nv_sigma,pa([aNV,Z1],pc(q_sigma,Z2/M)),
             'entire_N4_same_q_remainder','newOddSigmaCoordinates')

# Complete original odd errors, including their q quotients.
# EN=No+4 lambda P02 (A0+m sigma/ell) sigma.
# EP=Po+P02 [3(A0+m sigma/ell)^2 sigma+delta sigma^3].
aN=No+4*lam*P02*m*D/(ell*M)
bN=4*lam*P02*A0
cN=[4*lam*P02*m/(ell*M)]
eN=[No,4*lam*P02*A0,4*lam*P02*m/ell]
aP=Po+6*P02*A0*m*D/(ell*M)
bP=P02*(3*A0*A0+(3*m*m/(ell*ell)+delta)*D/M)
cP=[6*P02*A0*m/(ell*M),P02*(3*m*m/(ell*ell)+delta)/M]
eP=[Po,3*P02*A0*A0,6*P02*A0*m/ell,
    P02*(3*m*m/(ell*ell)+delta)]
for name,aa,bb,cc,ee in [('N',aN,bN,cN,eN),('P',aP,bP,cP,eP)]:
 return_sigma(ee,pa([aa,bb],pm(cc,q_sigma)),
              'complete_original_odd_'+name,'newOddSigmaCoordinates')
for value,bound in [(No,3),(Po,3),(Z0,3),(Z1,2),(Z2,1),
                    (aNV,3),(aN,3),(bN,2),(aP,3),(bP,2)]:
 assert geo(value)<=bound
say('new_same_sigma_original_coefficients_defined',
 rawOddN=rp(No),rawOddP=rp(Po),
 completeNVCoordinates=[rp(v) for v in nv_sigma],
 originalSecondMoment='q=M*sigma^2-D=ell*E2',
 oddOriginalSigmaRemaindersReturned=True,
 completeNVSameMomentRemainderReturned=True,
 noOldNSPSVlowOrValueProjectionGateExecuted=True,
 noDInverseOrDMultiplier=True)
tick()

# The genuinely NEW same-sigma minors. The H/N, H/P, H/NV minors are
# the previously known lower-D rows and are NOT computed here.
raw_cross=[]
original_sigma_sources=[]
for name,aa,bb,cc,ee in [('N',aN,bN,cN,eN),('P',aP,bP,cP,eP)]:
 value=aa*Z1-aNV*bb
 q_multiplier=ps([bb*Z2/M],pc(cc,Z1))
 # value = Z1*Eodd - bOdd*ell^2 NV
 #         +(bOdd*Z2/M-Z1*cOdd)*q.
 full=pa(pa(pc(ee,Z1),pc(nv_sigma,-bb)),pm(q_multiplier,q_sigma))
 return_sigma(full,[value],'new_'+name+'_NV_cross','newCrossSigmaCoordinates')
 assert geo(value)<=5
 for v in [Z1,-bb]+q_multiplier:checkden(v)
 raw_cross.append(value)
 original_sigma_sources.append((Z1,-bb,q_multiplier))
 say('new_original_same_sigma_cross_return',
     label='odd_'+name+'_with_complete_NV',raw=rp(value),
     actualTotalGeometryDegree=geo(value),
     sourceOddMultiplier=rp(Z1),sourceNVMultiplier=rp(-bb),
     sourceSecondMomentMultiplier=[rp(v) for v in q_multiplier],
     fullOriginalSigmaIdentityReturned=True,
     noSecondMomentOrValueRootSelection=True,
     noDivisionByDOrAnyValueHead=True,
     allHAndOtherOriginalConditionsRetained=True)
 tick()

# New ordinary polynomial reductions to the previously proved TRUE
# three-mean module. Full ordinary identities are returned; no bare
# matrix associativity or free-module assumption is used.
def reduce_new_cross(value):
 work=coeffs(value,5);tags=[R(),R(),R()]
 while True:
  tick()
  active=[key for key,v in work.items() if v and sum(key)>=2]
  if not active:break
  key=max(active,key=lambda ij:(sum(ij),ij))
  coefficient=work.pop(key);i,j=key
  if i>=2:which=0;ii,jj=i-2,j
  elif i and j:which=1;ii,jj=i-1,j-1
  else:which=2;ii,jj=i,j-2
  multiplier=coefficient*f**ii*V**jj
  for k in range(3):tags[k]+=multiplier*inv[which][k]
  for k,increment in enumerate([(0,0),(1,0),(0,1)]):
   at=(ii+increment[0],jj+increment[1])
   work[at]=work.get(at,R())+coefficient*rules[which][k]
  statistics['newMeanReductionSteps']+=1
 out=[work.get(key,R()) for key in slots[:3]]
 assert value==dot(out,basis)+dot(tags,forms)
 statistics['newOrdinaryMeanIdentities']+=1
 for j,v in enumerate(out):
  ck(v);assert td(v)<=5-int(j!=0)
 for v in tags:checkden(v);assert geo(v)<=3
 statistics['newReducedCoordinates']+=3
 return out,tags

cross_rows=[];cross_tags=[]
for name,value in zip(['N_NV','P_NV'],raw_cross):
 rr,tag=reduce_new_cross(value)
 cross_rows.append(rr);cross_tags.append(tag)
 say('new_same_sigma_cross_true_t_mean_return',
     label=name,coefficientProfiles=[rp(v) for v in rr],
     tDegrees=[td(v) for v in rr],
     originalMeanMultipliers=[rp(v) for v in tag],
     ordinaryPolynomialIdentityReturned=True,
     originalThreeMeansOnly=True,
     originalSourceFromSameQAndCompleteOddAndNV=True,
     noFreeThreeGeneratorAlgebraAssumed=True)
 tick()

# ONE predetermined new cofactor: N1, C_(N,NV), C_(P,NV).
# Existing N1 coefficient definition is used solely as an input. No
# old weighted scalar or old value cofactor is regenerated or checked.
# The weighted row-degree upper bound is 2+5+5-(0+1+1)=10.
def new_three_row_scalar():
 rows3=[rN,cross_rows[0],cross_rows[1]]
 mu=[rows3[1][1]*rows3[2][2]-rows3[1][2]*rows3[2][1],
     rows3[2][1]*rows3[0][2]-rows3[2][2]*rows3[0][1],
     rows3[0][1]*rows3[1][2]-rows3[0][2]*rows3[1][1]]
 if not any(mu):
  say('new_same_sigma_three_row_cofactor_zero',
      allOriginalRowsAndValueZeroFibersRetained=True,
      wholePhiExcluded=False)
  return
 denominator=O
 for value in mu:
  ck(value);denominator=exact(denominator,denominator.gcd(value.d))*value.d
 numerators=[v.n*exact(denominator,v.d) for v in mu]
 common=Z
 for value in numerators:common=common.gcd(value)
 assert common
 primitive=[R(exact(value,common)) for value in numerators]
 actual=[sum((primitive[i]*rows3[i][j] for i in range(3)),R())
         for j in range(3)]
 assert not actual[1] and not actual[2]
 statistics['newCofactorCoordinates']+=3
 value=ck(actual[0]);assert td(value)<=10
 if not value:
  say('new_same_sigma_scalar_identically_zero',
      originalRows=['N1','oddN_NV_cross','oddP_NV_cross'],
      actualThreeMultiplierCommonContent=profile(common),
      allThreeOriginalCoordinatesReturned=True,
      wholePhiExcluded=False,allOriginalConditionsRetained=True)
  return
 core,removed=strip(value.n)
 lead=core.coefficient(0);core/=lead;removed*=lead
 assert core*removed==value.n
 final=[checkden(v*R(value.d)/R(removed)) for v in primitive]
 again=[sum((final[i]*rows3[i][j] for i in range(3)),R())
        for j in range(3)]
 assert again==[R(core),R(),R()]
 statistics['newScalarReturnCoordinates']+=3
 degree=max((int(ex[2]) for ex in core.to_dict()),default=-1)
 top=ctx.from_dict({(ex[0],ex[1],0,0,0):cc for ex,cc in core.to_dict().items()
                    if int(ex[2])==degree})
 say('new_complete_same_sigma_original_t_scalar_return',
     originalRows=['N1','oddN_NV_cross','oddP_NV_cross'],
     actualThreeMultiplierCommonContent=profile(common),
     scalarNumerator=profile(value.n),scalarDenominator=profile(value.d),
     finalThreeOriginalMultipliers=[rp(v) for v in final],
     necessaryPolynomial=profile(core),tDegree=degree,
     tDegreeUpperBound=10,trueTLeadingNumerator=profile(top),
     allSixCofactorAndNormalizedCoordinatesReturned=True,
     sourceByOrdinaryMeanTracesAndSameSigmaOriginalIdentities=True,
     allCommonFactorAndLeadingZeroLociRetained=True,
     noDOrSlopeOrValueHeadInverse=True,
     noIndependentNormSameRootInference=True,
     wholePhiExcluded=int(core.total_degree())==0)
 tick()

new_three_row_scalar()
say('new_correct_Phi_same_sigma_two_crosses_and_one_scalar_finished',
 statistics=statistics,
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 oneSourceDependency=BASE_NAME,fullDependencySHA256=BASE_SHA,
 exactNecessaryPrefixBytes=7689,exactNecessaryPrefixSHA256=PREFIX_SHA,
 absoluteOriginalDeadlinePreserved=True,
 noOldQPrimaryOrSylvesterOrWeightedOrVlowCofactorGateReplayed=True,
 noCoefficientPayloadOrChunksSaved=True,
 noNewUnconditionalFinitePointOrUnitHeadClaim=True,ordinaryISPClaim=False)
signal.setitimer(signal.ITIMER_REAL,0)
