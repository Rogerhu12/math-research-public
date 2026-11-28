#!/usr/bin/env python3
"""NEW W positive-e generic unit-k: complete singleton P/N first e-jets.
Physical f and sigma are already proved integral on this precise chart.
Construct the actual dual Gram modulo e^2, then four NEW same-point forms:
P_B[0], (N_B-P_B)[1], P_C[1], N_C[1].
The physical P02 value terms have e-order >=2 and therefore vanish here.
Three fixed f-capacity (3,3) Sylvesters include the new first-order forms.
Return every source coordinate; remove only already excluded weight centers.
No old q2/R6/N5 projection, six-ray initial ideal, gcd, or frozen gate.
Self-contained first input: absolute 120 seconds / 1 GiB.
"""
import hashlib,json,resource,signal,time
from pathlib import Path
from flint import fmpq_mpoly_ctx
START=time.perf_counter();DEADLINE=START+120
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
signal.setitimer(signal.ITIMER_REAL,120)
ctx=fmpq_mpoly_ctx.get(('L','mu','f'),'lex')
lp,mp,fp=ctx.gens();ZERO=ctx.constant(0);ONE=ctx.constant(1)
STAT={'exactProducts':0,'newOriginalJetIdentities':0,
      'newSylvesterCoordinates':0,'newFullOriginalReturns':0,
      'oldPaidSupportProducts':0}
def tick():
 if time.perf_counter()>=DEADLINE:raise TimeoutError('absolute 120 seconds')
def say(stage,**d):
 d.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(d,separators=(',',':')),flush=True)
def poly(v):return v if hasattr(v,'to_dict') else ctx.constant(v)
def exact(a,b):
 tick();q,r=divmod(a,b);assert not r and q*b==a
 STAT['exactProducts']+=1;return q
class R:
 def __init__(self,n=0,d=None,reduced=False):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  n=poly(n);d=ONE if d is None else poly(d);assert d
  if not n:self.n=ZERO;self.d=ONE;return
  if not reduced:
   g=n.gcd(d);n=exact(n,g);d=exact(d,g)
  c=d.coefficient(0);self.n=n/c;self.d=d/c
 def __bool__(self):return bool(self.n)
 def __neg__(self):return R(-self.n,self.d,True)
 def __add__(self,v):
  v=R(v)
  if not self:return v
  if not v:return self
  g=self.d.gcd(v.d);a=exact(self.d,g);b=exact(v.d,g)
  return R(self.n*b+v.n*a,a*v.d)
 __radd__=__add__
 def __sub__(self,v):return self+-R(v)
 def __rsub__(self,v):return R(v)+-self
 def __mul__(self,v):
  v=R(v)
  if not self or not v:return R()
  a=self.n.gcd(v.d);b=v.n.gcd(self.d)
  return R(exact(self.n,a)*exact(v.n,b),
           exact(self.d,b)*exact(v.d,a),True)
 __rmul__=__mul__
 def __truediv__(self,v):
  v=R(v);assert v
  return self*R(v.d,v.n,True)
 def __rtruediv__(self,v):return R(v)/self
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  return R(self.n**n,self.d**n,True)
 def __eq__(self,v):
  v=R(v);return self.n*v.d==v.n*self.d
class J:
 """Exact ordinary coefficient algebra modulo e^2."""
 def __init__(self,a=0,b=0):
  if isinstance(a,J):self.a=a.a;self.b=a.b;return
  self.a=R(a);self.b=R(b)
 def __add__(self,v):
  v=J(v);return J(self.a+v.a,self.b+v.b)
 __radd__=__add__
 def __neg__(self):return J(-self.a,-self.b)
 def __sub__(self,v):return self+-J(v)
 def __rsub__(self,v):return J(v)+-self
 def __mul__(self,v):
  v=J(v);return J(self.a*v.a,self.a*v.b+self.b*v.a)
 __rmul__=__mul__
 def inverse(self):
  assert self.a
  return J(1/self.a,-self.b/(self.a*self.a))
 def __truediv__(self,v):return self*J(v).inverse()
 def __rtruediv__(self,v):return J(v)*self.inverse()
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  r=J(1)
  for _ in range(n):r=r*self
  return r
 def __eq__(self,v):
  v=J(v);return self.a==v.a and self.b==v.b
L,mu,physical_f=map(R,(lp,mp,fp))
e=J(0,1);k=J(2/(L-1));u=1+e;Q=e*k;delta=1-Q
Vbar=u*k+2
ell=u*((k+2)**2-2*e*k)/(k*Vbar)
m=u-ell;M=ell*ell*delta-m*m;bc=M/(4*delta)
lam=J((mu+3)/2);T=u*ell*J(mu)/(4*u+2*u/k-ell)
# Exact factored weight definitions, no e inverse in the jet algebra.
t0=-(2*u+k*ell)
phi2=-2*(k+4)/Vbar
p2=2*u*(k*k+(5-2*e)*k+8)/Vbar
g2=lam*p2+t0
pc=k*p2*(ell+T)-g2*t0
ts=-pc/(bc*k*phi2)
Vs=-e*g2/k-pc/(k*phi2)
JoverQ=ell-2*u/k;beta=2*u-JoverQ
f=J(physical_f)
t=beta*f/bc+ts;V=2*u*f+Vs;W1=e*t0/2+2*u*f
theta=u-ell*Q
x=(theta*V-m*W1)/M;y=(ell*W1-u*V)/M
A1=2*f-2*V+2*bc*t
rho=J(1,-k.a/2)
assert rho*rho==delta
aw=1-ell;b=(ell+m/rho)/2;c=(ell-m/rho)/2
p=1+rho;q=1-rho;X=x+rho*y;Y=x-rho*y
rg=X-aw*p-c*t;sg=Y-aw*q-b*t
rows=[[J(),J(),p,q],[J(),A1,rg,sg],
      [p,rg,J(),t],[q,sg,t,J()]]
one=[J(1),J(),J(1),J(1)]
def vm(v,w):return [v[0]*w[0],v[0]*w[1]+v[1]*w[0],v[2]*w[2],v[3]*w[3]]
def va(v,w):return [v[i]+w[i] for i in range(4)]
def vs(a,v):return [a*w for w in v]
def tr(v):return aw*v[0]+v[1]+b*v[2]+c*v[3]
def DK(v):return [tr(vm(row,v)) for row in rows]
d=DK(one);F2=tr(d)
assert F2==2*f
def N4(v):
 vv=vm(v,v);tv=tr(v)
 return 2*tr(vm(d,vv))-F2*tr(vv)-4*tv*tr(vm(d,v))+2*F2*tv*tv+tr(vm(v,DK(v)))
def P2(v):
 cv=va(v,vs(-tr(v),one))
 return tr(vm(vm(cv,cv),cv))
NB,NC=N4(rows[2]),N4(rows[3])
PB,PC=P2(rows[2]),P2(rows[3])
assert NB.a==PB.a and not PC.a and not NC.a
STAT['newOriginalJetIdentities']+=5
FORMS=[PB.a,(NB-PB).b,PC.b,NC.b]
LABELS=['complete_P_B_order_zero','complete_N_B_minus_P_B_divided_e',
        'complete_P_C_divided_e','complete_N_C_divided_e']
ATOMS=[lp,lp-1,2*lp-1,2*lp-3]
def weight(p):return all(int(ex[1])==0 and int(ex[2])==0 for ex in p.to_dict())
def strip(p):
 rem=p;removed=ONE
 if not p:return p,removed
 for atom in ATOMS:
  while rem:
   g=rem.gcd(atom)
   if int(g.total_degree())==0:break
   rem=exact(rem,g);removed*=g
   STAT['oldPaidSupportProducts']+=1
 assert rem*removed==p
 return rem,removed
def paid(p):
 assert p and weight(p)
 rem,_=strip(p);assert int(rem.total_degree())==0
def profile(p):
 data=[[list(map(int,ex)),str(c)] for ex,c in sorted(p.to_dict().items())]
 bb=json.dumps(data,separators=(',',':')).encode()
 return {'degrees':list(map(int,p.degrees())) if p else [-1,-1,-1],
         'totalDegree':int(p.total_degree()) if p else -1,
         'terms':len(data),'bytes':len(bb),'sha256':hashlib.sha256(bb).hexdigest()}
def coeff(p,j):
 return ctx.from_dict({(int(ex[0]),int(ex[1]),0):cc for ex,cc in p.to_dict().items() if int(ex[2])==j})
for value in FORMS:
 paid(value.d)
 assert all(int(ex[1])+int(ex[2])<=3 for ex in value.n.to_dict())
 for pp0 in [value.n,value.d]:
  for cc in pp0.to_dict().values():
   ss=str(cc);den=int(ss.split('/')[1]) if '/' in ss else 1
   assert den%1009
raw=[v.n for v in FORMS]
head=R(coeff(raw[0],3),FORMS[0].d)
assert head==16*((2*L-1)-1)*((2*L-1)-2)/(2*L-1)**2
STAT['newOriginalJetIdentities']+=1
say('new_complete_singleton_original_first_jets',
     sourceCount=4,labels=LABELS,jetAlgebra='ordinary full Gram modulo e^2',
     originalNumerators=[profile(v.n) for v in FORMS],
     originalDenominators=[profile(v.d) for v in FORMS],
     originalPhysicalValueTermsHaveOrderAtLeastTwo=True,
     physicalFAndSigmaIntegralityPaidBySeparateOriginalPaper=True,
     allFourEquationsAtSameL_mu_f=True,
     noPhysicalFZeroOrLambdaSpecialization=True,
     firstFormCubicHeadAlreadyPaidNonzero=True,
     retainedWeightSupports=['L','L-1','2L-1','2L-3'],
     fixedNewPairs=[[0,1],[0,2],[0,3]],fixedFCapacities=[3,3])

def fixed_pair(j):
 tick();capacities=[3,3];size=6
 aa=[coeff(raw[0],i) for i in range(4)]
 bb=[coeff(raw[j],i) for i in range(4)]
 columns=[]
 for vv in [aa,bb]:
  for shift in range(3):
   columns.append([ZERO]*shift+vv+[ZERO]*(2-shift))
 matrix=[[columns[c0][i] for c0 in range(size)] for i in range(size)]
 work=[list(matrix[i])+[ONE if i==0 else ZERO] for i in range(size)]
 prev=ONE;sgn=1
 for i in range(size-1):
  pivot=next((r for r in range(i,size) if work[r][i]),None)
  if pivot is None:
   say('new_fixed_singleton_jet_resultant_zero',
       pair=[0,j],step=i,allOriginalFibersRetained=True)
   return {'pair':[0,j],'zero':True}
  if pivot!=i:work[i],work[pivot]=work[pivot],work[i];sgn=-sgn
  a=work[i][i]
  for r in range(i+1,size):
   old=work[r][i]
   for c0 in range(i+1,size+1):
    work[r][c0]=exact(a*work[r][c0]-old*work[i][c0],prev)
   work[r][i]=ZERO
  prev=a
 if not work[-1][-2]:
  say('new_fixed_singleton_jet_resultant_zero',
      pair=[0,j],step=5,allOriginalFibersRetained=True)
  return {'pair':[0,j],'zero':True}
 det=sgn*work[-1][-2];co=[ZERO]*size
 for i in range(size-1,-1,-1):
  got=det*work[i][-1]
  for c0 in range(i+1,size):got-=work[i][c0]*co[c0]
  co[i]=exact(got,work[i][i])
 for i in range(size):
  assert sum((matrix[i][j0]*co[j0] for j0 in range(size)),ZERO)==(det if i==0 else ZERO)
  STAT['newSylvesterCoordinates']+=1
 left=sum((co[i]*fp**i for i in range(3)),ZERO)
 right=sum((co[i+3]*fp**i for i in range(3)),ZERO)
 assert left*raw[0]+right*raw[j]==det
 STAT['newFullOriginalReturns']+=1
 reduced,removed=strip(det)
 final=[R() for _ in range(4)]
 final[0]=R(left*FORMS[0].d,removed)
 final[j]=R(right*FORMS[j].d,removed)
 for vv in final:
  paid(vv.d)
  for pp0 in [vv.n,vv.d]:
   for cc in pp0.to_dict().values():
    ss=str(cc);den=int(ss.split('/')[1]) if '/' in ss else 1
    assert den%1009
 assert sum((final[i]*FORMS[i] for i in range(4)),R())==R(reduced)
 STAT['newFullOriginalReturns']+=1
 assert all(int(ex[2])==0 for ex in reduced.to_dict())
 constant=int(reduced.total_degree())==0
 unit=False
 if constant:
  ss=str(reduced.coefficient(0))
  nu,de=map(int,ss.split('/')) if '/' in ss else (int(ss),1)
  unit=bool(nu%1009) and bool(de%1009)
 say('new_fixed_singleton_jet_complete_four_original_return',
     pair=[0,j],fixedFCapacities=capacities,
     determinant=profile(det),reducedNecessaryScalar=profile(reduced),
     removedOnlyPreviouslyExcludedWeightSupports=profile(removed),
     fourActualOriginalMultiplierProfiles=[
       {'numerator':profile(v.n),'denominator':profile(v.d)} for v in final],
     allSixSylvesterCoordinatesReturned=True,
     completeFourOriginalJetIdentityReturned=True,
     allUnpaidHeadsAndFixedDegreeDropFibersRetained=True,
     originalResidualScalarP1009Unit=unit,
     noOldQ2R6N5GateReplayed=True)
 return {'pair':[0,j],'zero':False,'profile':profile(reduced),'unit':unit}
answers=[fixed_pair(j) for j in [1,2,3]]
say('new_generic_positive_e_complete_singleton_first_jet_input_finished',
    fixedPairs=answers,statistics=STAT,
    onlyThisAlreadyIntegralGenericKChart=True,
    noClaimFromNonzeroScalarAlone=True,
    genericResidueChartExcludedByReturnedUnit=any(v.get('unit',False) for v in answers),
    noEntirePositiveERayOrWholeWClaim=True,ordinaryISPClaim=False,
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    noCoefficientCacheWritten=True)
