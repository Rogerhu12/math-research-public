#!/usr/bin/env python3
"""NEW original W pure (lambda,T) quartic input.
Basis: globally monic qT4, original R4, and newly proved full-N4 Bpure.
No f/native/old action matrix is rebuilt.  Original three-multiplier
identities give R3,B3, then new B2; head-free pseudodivision gives Q2.
Only NEW fixed (2,2) and (3,2) T resultants, 4/5 dimensions.  Actual
multiplier contents may be canceled only with all T coefficients returned.
All head/content zero fibers remain.  180 seconds /4 GiB, no dependencies.
"""
import hashlib,json,resource,signal,time
from pathlib import Path
from flint import fmpq_mpoly_ctx
START=time.perf_counter()
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
signal.setitimer(signal.ITIMER_REAL,180)
def say(stage,**data):
 data.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(data,separators=(',',':')),flush=True)
ctx=fmpq_mpoly_ctx.get(('e','k','lam','T'),'lex')
ep,kp,lp,tp=ctx.gens();Z=ctx.constant(0);O=ctx.constant(1)
def polynomial(v):return v if hasattr(v,'to_dict') else ctx.constant(v)
class R:
 def __init__(self,n=0,d=None,reduce=True):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  n=polynomial(n);d=O if d is None else polynomial(d);assert d
  if not n:self.n=Z;self.d=O;return
  if reduce:
   g=n.gcd(d);n=n/g;d=d/g
  s=d.coefficient(0);self.n=n/s;self.d=d/s
 def __bool__(self):return bool(self.n)
 def __add__(self,v):
  v=R(v)
  if not self:return v
  if not v:return self
  g=self.d.gcd(v.d);a=self.d/g;b=v.d/g
  return R(self.n*b+v.n*a,a*v.d)
 __radd__=__add__
 def __neg__(self):return R(-self.n,self.d,False)
 def __sub__(self,v):return self+-R(v)
 def __rsub__(self,v):return R(v)+-self
 def __mul__(self,v):
  v=R(v)
  if not self or not v:return R()
  g=self.n.gcd(v.d);h=v.n.gcd(self.d)
  return R((self.n/g)*(v.n/h),(self.d/h)*(v.d/g),False)
 __rmul__=__mul__
 def __truediv__(self,v):
  v=R(v);assert v
  return self*R(v.d,v.n,False)
 def __rtruediv__(self,v):return R(v)/self
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  return R(self.n**n,self.d**n,False)
 def __eq__(self,v):
  v=R(v);return self.n*v.d==v.n*self.d
e,k,lam,T=map(R,(ep,kp,lp,tp))
u=e+1;Q=e*k;Vbar=u*k+2;delta=1-Q
ell=u*((k+2)**2-2*e*k)/(k*Vbar)
m=u-ell;theta=u-ell*Q;V2=2*u-ell*Q
M=ell*V2-u*u;bc=M/(4*delta)
T0=V2-2*u*u;J=2*u*(1-u)+ell*Q
Phi=T0+4*u-4+Q;Pf=T0*(J-Q)
P02=(2-3*u)*V2-Q*u+2*u**3
assert M==ell*ell*delta-m*m
assert J*Phi-Pf==2*u*Q*Phi
Ast=4*u*Q-J;Cst=Ast*m*m+J*delta*ell*ell
Aval=2*lam*lam-2*lam+1
Bval=4*lam**3-6*lam*lam+3*lam-1
cval=3-2*lam;w=lam-1-T
D=ell*Aval-T*T
K=ell*ell*Bval-3*ell*Aval*T+2*T**3
ad=(M*ell*ell*Q*(3-4*lam)+M*Ast*T*T
    +2*M*u*Q*cval*ell*T+D*Cst)
b0=2*m*(Ast*T+u*Q*cval*ell);bd=M*b0
R4=M*ad*ad-D*bd*bd
C4=2*m*D*ad+K*bd
q4=C4/(8*m*u*Q*ell*ell*delta)

# Bpure is the exact f^0 coefficient, NOT a physical f=0 restriction.
G=lam*P02-(1-u)*T0
Pc=Q*P02*(ell+T)-G*T0
ts=-Pc/(bc*Q*Phi)
Vs=-G/Q-Pc/(Q*Phi)
Ws=T0/2;A1s=2*G/Q
xs=(theta*Vs-m*Ws)/M;ys=(ell*Ws-u*Vs)/M
assert A1s==-2*Vs+2*bc*ts
z1=-2*(ell*cval+2*T)*ys-2*ell*w+m*T*ts/delta
z2=2*(ell*xs-m*ys-bc*ts)
Z0=(ell*ell*A1s+2*ell*u*w*(ell*cval+T)
    +2*Vs*(ell*ell+ell*cval*T+T*T)
    +2*bc*ts*(T*T-ell*ell))
Bpure=b0*(Z0+D*z2)-ad*z1
# These small coefficient identities are part of this exact input definition.
# They do not rebuild native/full-N4 or either previous quartic scalar.
beta=2*u-J/Q
xf=2*u*ell*delta/M;yf=-2*u*m/M
z1f=-2*(ell*cval+2*T)*yf+m*T*beta/(bc*delta)
z2f=2*(ell*(xf-1)-m*yf-beta)
Z0f=(ell*ell*(2-2*J/Q)+4*ell*ell*(1-2*lam)+2*ell*D
     +4*u*(ell*ell+ell*cval*T+T*T)+2*beta*(T*T-ell*ell))
assert M*Q*z1f==2*b0
assert M*Q*(Z0f+D*z2f)==2*ad
assert not (b0*(Z0f+D*z2f)-ad*z1f)

statistics={'exactPolynomialDivisionProducts':0,'originalCoefficientReturns':0,
            'paidSupportProducts':0,'pseudoDivisionSteps':0,
            'fixedFiveBareissProducts':0,'factorProductReturns':0}
def exact(p,g):
 out,rem=divmod(p,g);assert not rem and out*g==p
 statistics['exactPolynomialDivisionProducts']+=1;return out
def weight(p):return all(int(ex[2])==0 and int(ex[3])==0 for ex in p.to_dict())
def t_free(p):return all(int(ex[3])==0 for ex in p.to_dict())
def degT(v):
 v=R(v);assert weight(v.d)
 return max((int(ex[3]) for ex in v.n.to_dict()),default=-1)
def coeffT(v,j):
 v=R(v);assert weight(v.d)
 return R(ctx.from_dict({(ex[0],ex[1],ex[2],0):c
    for ex,c in v.n.to_dict().items() if int(ex[3])==j}),v.d)
def profile(p):
 data=[[list(map(int,ex)),str(c)] for ex,c in sorted(p.to_dict().items())]
 raw=json.dumps(data,separators=(',',':')).encode()
 return {'zero':not bool(p),'degrees_e_k_lambda_T':list(map(int,p.degrees())) if p else [-1]*4,
         'totalDegree':int(p.total_degree()) if p else -1,'terms':len(data),
         'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
# Only already paid CURRENT W weight supports.  Neither Astar nor b0
# nor any R3/B2/Q2 head is paid in this source.
paid_atoms=[('e',ep),('k',kp),('u',ep+1),('delta',ep*kp-1),
 ('Vbar',(ep+1)*kp+2),('Phi_k_plus_four',kp+4),('P02',P02.n),
 ('M',M.n),('whole_equal_weights_k_plus_two',kp+2),
 ('whole_ell_zero',ell.n),('whole_equal_weights_m',m.n),
 ('whole_original_Lhalf',(2*ell-1).n)]
def strip(p,terminal=False):
 if not p:return p,O,[]
 before=p;removed=O;history=[]
 atoms=paid_atoms+([('original_nonzero_lambda',lp),
                    ('whole_W_lambda_three_halves',2*lp-3)] if terminal else [])
 for label,atom in atoms:
  assert atom and t_free(atom)
  if not terminal:assert weight(atom)
  layers=0
  while p:
   gg=p.gcd(atom)
   if int(gg.total_degree())==0:break
   p=exact(p,gg);removed*=gg;layers+=1
   statistics['paidSupportProducts']+=1
  if layers:history.append({'paidSupport':label,'gcdLayers':layers})
 assert p*removed==before
 return p,removed,history
den_seen=set()
def paid(p):
 assert p and weight(p)
 key=str(p)
 if key in den_seen:return
 rr,_,_=strip(p);assert rr and int(rr.total_degree())==0
 den_seen.add(key)
def ck(v):v=R(v);paid(v.d);return v
for val in [q4,R4,Bpure,ts,Vs,Ws,A1s,xs,ys,z1,z2,Z0]:
 ck(val)
assert degT(q4)==4 and coeffT(q4,4)==1
assert degT(R4)<=4 and degT(Bpure)<=4
assert all(int(ex[2])+int(ex[3])<=4 for ex in Bpure.n.to_dict())
basis=[q4,R4,Bpure]
say('new_pure_lambda_T_three_original_quartics_defined',
 originalBasis=['qT4=C4/(8*m*u*Q*ell^2*delta)','R4','full_N4_Bpure'],
 fIndependenceCoefficientIdentitiesReturned=True,
 actualTDegrees=[degT(v) for v in basis],
 Bpure=profile(Bpure.n),BpureDenominator=profile(Bpure.d),
 allDenominatorsOnlyOldPureWeightUnits=True,
 entire_b0_and_Astar_zero_faces_kept=True,
 noNativeOrPreviousScalarReplayed=True)

def lincomb(tag):
 return sum((tag[i]*basis[i] for i in range(3)),R())
def check_original(value,tag):
 back=lincomb(tag)
 assert back==value
 cap=max(degT(back),degT(value),0)
 for j in range(cap+1):
  assert coeffT(back,j)==coeffT(value,j)
  statistics['originalCoefficientReturns']+=1

# Cancel ONLY all three actual original multipliers' common numerator.
# Return every T coordinate after this cancellation: no original equation
# and no unseen head/content is divided in the physical source.
def primitive_original(label,value,tag,cap):
 check_original(value,tag)
 den=O
 for v in tag:
  ck(v);den=exact(den,den.gcd(v.d))*v.d
 paid(den)
 nums=[v.n*exact(den,v.d) for v in tag]
 common=Z
 for p in nums:common=common.gcd(p)
 if not common:
  assert not value
  say('new_original_three_multiplier_zero',label=label)
  return R(),[R(),R(),R()]
 prim=[R(exact(p,common)) for p in nums]
 out=lincomb(prim)
 assert R(common)*out==R(den)*value
 ck(out);assert degT(out)<=cap
 check_original(out,prim)
 say('new_original_three_multiplier_primitive',
     label=label,actualTdegree=degT(out),
     actualCommonMultiplier=profile(common),
     numerator=profile(out.n),denominator=profile(out.d),
     allTCoordinatesReturned=True,entireCommonZeroFaceKept=True,
     noNewHeadInverted=True)
 return out,prim

R3,tagR=primitive_original('R3_from_qT4_and_R4',
 R4-coeffT(R4,4)*q4,[-coeffT(R4,4),R(1),R()],3)
B3,tagB=primitive_original('NEW_B3_from_qT4_and_full_N4',
 Bpure-coeffT(Bpure,4)*q4,[-coeffT(Bpure,4),R(),R(1)],3)
rhead=coeffT(R3,3);bhead=coeffT(B3,3)
S2,tagS=primitive_original('NEW_B2_common_T_cubic_head_cancellation',
 rhead*B3-bhead*R3,
 [rhead*tagB[i]-bhead*tagR[i] for i in range(3)],2)
say('new_full_N4_T_two_head_row_complete',
 oldR3Tdegree=degT(R3),newB3Tdegree=degT(B3),newB2Tdegree=degT(S2),
 R3CubicHead=profile(rhead.n),B3CubicHead=profile(bhead.n),
 allCubicHeadZeroFibersKept=True,
 threeOriginalMultiplierIdentitiesReturned=True)

def clear_input(label,v,tag,cap):
 ck(v);assert degT(v)<=cap
 pp,removed,hist=strip(v.n,False)
 if pp:
  scalar=pp.coefficient(0);pp/=scalar;removed*=scalar
 assert pp*removed==v.n
 # This uses only weight units; all lambda and T heads remain un-inverted.
 paid(removed)
 outtag=[R(v.d,removed)*z for z in tag]
 check_original(R(pp),outtag)
 say('new_fixed_T_resultant_original_input',
   label=label,polynomial=profile(pp),
   onlyPaidWeightSupportRemoval=hist,
   fullThreeOriginalMultiplierReturn=True,
   noLambdaOrTHeadInverted=True)
 return pp,outtag

def fixed_five(A,B):
 # Fixed degree bounds 3,2, even when one or both leading coefficients vanish.
 mat=[]
 for pp,degree,count in [(A,3,2),(B,2,3)]:
  co=[coeffT(R(pp),j).n for j in range(degree+1)]
  assert sum((v*tp**j for j,v in enumerate(co)),Z)==pp
  for shift in range(count):
   row=[Z]*5
   for j,v in enumerate(co):row[j+shift]=v
   assert sum((v*tp**j for j,v in enumerate(row)),Z)==pp*tp**shift
   mat.append(row)
 original=[row[:] for row in mat];last=O;sgn=1
 for p in range(4):
  ii=next((i for i in range(p,5) if mat[i][p]),None)
  if ii is None:return Z
  if ii!=p:mat[ii],mat[p]=mat[p],mat[ii];sgn=-sgn
  pivot=mat[p][p]
  for i in range(p+1,5):
   for j in range(p+1,5):
    mat[i][j]=exact(pivot*mat[i][j]-mat[i][p]*mat[p][j],last)
    statistics['fixedFiveBareissProducts']+=1
   mat[i][p]=Z
  last=pivot
  say('new_fixed_three_two_T_complete_Bareiss_step',
      step=p,pivot=profile(pivot),
      fullFixedRowsReturned=True,
      allIntermediatePivotZeroFibersKeptByPolynomialIdentity=True)
 return sgn*mat[4][4]

targets=[];terminal_cache={}
if R3 and degT(R3)>=1:
 # New pseudo remainder only as input for the new full-N4 target.
 # No R3 head inverse: scale*q4=quotient*R3+remainder.
 rem=q4;quo=R();scale=R(1);d=degT(R3);head=coeffT(R3,d)
 while rem and degT(rem)>=d:
  shift=degT(rem)-d;lc=coeffT(rem,degT(rem))
  rem=head*rem-lc*T**shift*R3
  quo=head*quo+lc*T**shift
  scale*=head
  assert scale*q4==quo*R3+rem
  statistics['pseudoDivisionSteps']+=1
 assert degT(rem)<d
 Q2,tagQ=primitive_original('qT4_pseudoremainder_needed_only_for_NEW_B2',
    rem,[(scale if i==0 else R())-quo*tagR[i] for i in range(3)],2)
 A,Atag=clear_input('Q2',Q2,tagQ,2)
 B,Btag=clear_input('NEW_B2',S2,tagS,2)
 # A=a*T^2+b*T+c, B=d*T^2+e*T+f.  These FOUR actual
 # multipliers produce Res_{2,2}=p^2-q*r on all head-zero fibers.
 c,b,a=[coeffT(R(A),j).n for j in range(3)]
 f,ee,dd=[coeffT(R(B),j).n for j in range(3)]
 pp=a*f-c*dd;qq=a*ee-b*dd;rr=b*f-c*ee
 mul=[qq*ee-pp*dd,qq*dd,-qq*b+pp*a,-qq*a]
 target=pp*pp-qq*rr
 def pair_return(mm):
  out=[Z]*4
  for j in range(3):
   ac=[c,b,a][j];bc0=[f,ee,dd][j]
   out[j]+=mm[0]*ac+mm[2]*bc0
   out[j+1]+=mm[1]*ac+mm[3]*bc0
  return out
 ret=pair_return(mul)
 assert ret==[target,Z,Z,Z]
 common=Z
 for v in mul:common=common.gcd(v)
 if common:
  prim=[exact(v,common) for v in mul]
  ret=pair_return(prim);assert ret[1:]==[Z,Z,Z]
  scalar4=ret[0];assert common*scalar4==target
  tA=R(prim[0]+prim[1]*tp);tB=R(prim[2]+prim[3]*tp)
  finaltag=[tA*Atag[i]+tB*Btag[i] for i in range(3)]
  check_original(R(scalar4),finaltag)
  say('new_fixed_two_two_T_resultant_full_return',
      rawResultant=profile(target),actualFourMultiplierCommon=profile(common),
      returnedPrimitiveScalar=profile(scalar4),
      allFourTCoordinatesReturned=True,
      allThreeOriginalSourceMultipliersReturned=True,
      allHeadAndMultiplierCommonZeroFacesKept=True)
 else:
  assert not target
  scalar4=Z
  say('new_fixed_two_two_T_resultant_zero',noNewScalarClaim=True)
 targets.append(('NEW_fixed_T_two_two',scalar4))
 pre4=strip(scalar4,True)
 terminal_cache['NEW_fixed_T_two_two']=pre4
 if pre4[0] and int(pre4[0].total_degree())==0:
  say('new_first_original_scalar_already_paid_unit',
      fixedFiveNotNeededAndNotRun=True,wholeCurrentWExcluded=True)
 else:
  A3,A3tag=clear_input('R3_for_NEW_full_N4_fixed_five',R3,tagR,3)
  scalar5=fixed_five(A3,B)
  assert t_free(scalar5)
  say('new_fixed_three_two_T_resultant_complete',
     scalar=profile(scalar5),allFixedFiveOriginalRowsReturned=True,
     allFiniteCommonTRootsCovered=True,
     noLambdaOrTHeadInverted=True)
  targets.append(('NEW_fixed_T_three_two',scalar5))
else:
 say('new_old_R3_degenerate_input',
     R3IsZero=not bool(R3),R3Tdegree=degT(R3),
     exactOriginalR3=profile(R3.n),
     noFixedResultantAttempted=True,wholeWExcluded=False,
     fullOriginalBpureRetained=True)

# Any remaining lambda content is RETAINED unless already paid.
# A nonconstant target is only necessary, never a W emptiness claim.
for label,scalar in targets:
 assert t_free(scalar)
 pp,removed,hist=terminal_cache[label] if label in terminal_cache else strip(scalar,True)
 if pp:
  cc=pp.coefficient(0);pp/=cc;removed*=cc
 assert pp*removed==scalar
 say('new_pure_value_retained_lambda_weight_condition',
    label=label,necessary=profile(pp),onlyPaidSupportRemoval=hist,
    fullTerminalProductReturned=True,
    allUnpaidParameterAndLambdaFactorsKept=True,
    wholeWExcluded=bool(pp) and int(pp.total_degree())==0)
 if pp:
  content,factors=pp.factor();back=ctx.constant(content);facts=[]
  for fac,exponent in factors:
   back*=fac**int(exponent)
   facts.append({'multiplicity':int(exponent),'factor':profile(fac)})
  assert back==pp;statistics['factorProductReturns']+=1
  say('new_pure_value_complete_QQ_factorization',
      label=label,factors=facts,completeProductReturned=True,
      allUnpaidFactorZeroFibersRemain=int(pp.total_degree())>0,
      noMultivariateGcdEmptinessInference=True)
say('new_pure_lambda_T_first_low_resultants_complete',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 statistics=statistics,
 noB0OrAstarPaymentAnywhere=True,
 entireB0AndAllNewHeadZeroFacesKept=True,
 noOldT4R6OrNlowPlowGateReplayed=True,
 noSufficiencyClaimForValueOnlySubsystem=True,
 noCoefficientCachePayloadOrChunksSaved=True,ordinaryISPClaim=False,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.setitimer(signal.ITIMER_REAL,0)
