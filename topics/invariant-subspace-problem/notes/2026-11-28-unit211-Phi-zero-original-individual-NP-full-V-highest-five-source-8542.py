#!/usr/bin/env python3
"""NEW whole Phi actual individual N/P and full V highest source.
Construct the genuine associated-graded original Gram and N4/P2.
No zero-mean or rescaled-Gram surrogate is used. The original complete
Nlow, Plow, Vlow give three new degree-five rows over the same actual
three mean generators. Full fixed polynomial source identities survive
highest extraction and filtered lifting. Only a final weight cover
can be divided; its entire zero set remains. No previous large
coefficient ideal, lambda determinant, or old highest unit gate runs.
120 seconds /1GiB including necessary definition prefixes.
"""
import os,time,json,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
START=time.perf_counter();DEADLINE=START+120
signal.setitimer(signal.ITIMER_REAL,120)
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,separators=(",",":")),flush=True)
path=Path(__file__).with_name("2026-11-28-unit211-Phi-zero-whole-first-head-original-NV-F6-highest-unit-filtered-lift-8542.py")
raw=path.read_bytes()
assert hashlib.sha256(raw).hexdigest()=="4cebc8a6e7e16c58e9dff2bc055acd2bc9e262132bc08d7d9dfa2bff0ca3cd41"
mark=b"\n# The graded highest-component functor:"
assert raw.count(mark)==1
prefix=raw.split(mark)[0]
assert len(prefix)==5375
assert hashlib.sha256(prefix).hexdigest()=="cd5abd21e7c805bfbca61b284ac56271482d4e724e9b44363cca1e2dc083620d"
sc={"__file__":str(path),"__name__":"new_individual_highest_original_three_mean_definition"}
oa=signal.alarm;ot=signal.setitimer
def bounded_timer(which,seconds,interval=0):
 if which!=signal.ITIMER_REAL:return ot(which,seconds,interval)
 assert not interval
 left=max(.001,DEADLINE-time.perf_counter())
 return ot(which,min(left,float(seconds) if seconds>0 else left),0)
def bounded_alarm(seconds):return math.ceil(bounded_timer(signal.ITIMER_REAL,seconds)[0])
signal.alarm=bounded_alarm;signal.setitimer=bounded_timer
try:
 with contextlib.redirect_stdout(io.StringIO()):
  exec(compile(prefix,str(path)+":only-genuine-three-mean-highest-definition","exec"),sc)
finally:
 signal.alarm=oa;signal.setitimer=ot
 ot(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
R,ctx,zero,one,weight,check_weight,weight_only,profile,rprofile,exact,strip_paid,pay,rm,mt,mz,low1,amb1,amb2=[sc[k] for k in
 ["R","ctx","zero","one","weight","check_weight","weight_only","profile","rprofile","exact","strip_paid","pay","rm","mt","mz","low1","amb1","amb2"]]
u,Q,ell,delta,m,M,bc,T0,J,P02,Pf=[sc[k] for k in
 ["u","Q","ell","delta","m","M","bc","T0","J","P02","Pf"]]
up,Qp,Lp,Tp,zp=ctx.gens()
# The graded highest-component functor: degree is a PROVED upper bound.
# Addition at unequal bounds keeps only the higher component; products
# add bounds. Vanishing components never silently lower the full bound.
# t and s below denote T/lambda and z/lambda ONLY in this functor.
top_operation_count=0
class Top:
 __slots__=("degree","value")
 def __init__(self,value=0,degree=0):
  if isinstance(value,Top):self.degree=value.degree;self.value=value.value;return
  value=R(value);assert weight_only(value.d)
  assert all(e[2]==0 and int(e[3])+int(e[4])<=degree for e in value.n.to_dict())
  self.degree=degree;self.value=value
 def __neg__(self):return Top(-self.value,self.degree)
 def __add__(self,o):
  global top_operation_count
  o=Top(o);d=max(self.degree,o.degree)
  value=(self.value if self.degree==d else R())+(o.value if o.degree==d else R())
  top_operation_count+=1;return Top(value,d)
 __radd__=__add__
 def __sub__(self,o):return self+-Top(o)
 def __rsub__(self,o):return Top(o)+-self
 def __mul__(self,o):
  global top_operation_count
  o=Top(o);top_operation_count+=1
  return Top(self.value*o.value,self.degree+o.degree)
 __rmul__=__mul__
 def __truediv__(self,o):
  # Only an original weight coefficient is divided, never a spectral
  # leading coefficient or an element of an unproved quotient field.
  o=R(o);assert weight_only(o.n) and weight_only(o.d)
  pay(o.n);pay(o.d)
  return Top(self.value/o,self.degree)
 def __pow__(self,n):
  assert n>=0
  out=Top(1);base=self
  while n:
   if n&1:out=out*base
   n//=2
   if n:base=base*base
  return out
l=Top(1,1);t=Top(R(Tp),1);s=Top(R(zp),1)
class E:
 __slots__=("a","b")
 def __init__(self,a=0,b=0):
  if isinstance(a,E):
   assert b==0;self.a=a.a;self.b=a.b;return
  self.a=Top(a);self.b=Top(b)
 def __neg__(self):return E(-self.a,-self.b)
 def __add__(self,other):
  other=E(other);return E(self.a+other.a,self.b+other.b)
 __radd__=__add__
 def __sub__(self,other):return self+-E(other)
 def __rsub__(self,other):return E(other)+-self
 def __mul__(self,other):
  other=E(other)
  return E(self.a*other.a+(self.b*other.b)*delta,
           self.a*other.b+self.b*other.a)
 __rmul__=__mul__
 def __truediv__(self,other):return E(self.a/other,self.b/other)
 def conj(self):return E(self.a,-self.b)
def same_top(a,b):
 a=Top(a);b=Top(b)
 if not a.value and not b.value:return True
 return a.degree==b.degree and a.value==b.value
def same_E(a,b):
 a=E(a);b=E(b);return same_top(a.a,b.a) and same_top(a.b,b.b)
rho=E(0,1);p=E(1)+rho;q=E(1)-rho
bw=E(ell/2,m/(2*delta));cw=E(ell/2,-m/(2*delta));aw=E(1-ell)
assert same_E(bw*cw,E(bc))
GG=l*P02+(u-1)*T0
ff=(GG*T0-(t+ell)*(Q*P02))/Pf
vv=(ff*J-GG+s*bc)/Q
ww=(ff*(4*u)+T0)/2
X=(E(ww)-q*E(vv))*cw*rho/(2*bc*delta)
Y=(p*E(vv)-E(ww))*bw*rho/(2*bc*delta)
tt=E(s/Q)
germ=E(ff*2-vv*2+s*(2*bc/Q))
rr=X-aw*p-cw*tt
ss=Y-aw*q-bw*tt
gram=[[E(),E(),p,q],[E(),germ,rr,ss],
      [p,rr,E(),tt],[q,ss,tt,E()]]
perm=[0,1,3,2]
assert all(same_E(gram[i][j].conj(),gram[perm[i]][perm[j]]) for i in range(4) for j in range(4))
onev=[E(1),E(),E(1),E(1)]
def vm(a,b):return [a[0]*b[0],a[0]*b[1]+a[1]*b[0],a[2]*b[2],a[3]*b[3]]
def tau(a):return a[0]*aw+a[1]+a[2]*bw+a[3]*cw
def DK(a):return [tau(vm(row,a)) for row in gram]
dvec=DK(onev);F2=tau(dvec)
assert same_E(F2,E(ff*2))
def N4(a):
 av=vm(a,a);ta=tau(a)
 return (tau(vm(dvec,av))*2-F2*tau(av)
         -ta*tau(vm(dvec,a))*4+F2*ta*ta*2+tau(vm(a,DK(a))))
def P2(a):
 ta=tau(a);cent=[a[i]-ta*onev[i] for i in range(4)]
 return tau(vm(vm(cent,cent),cent))
NB=N4(gram[2]);PB=P2(gram[2])
assert NB.a.degree==NB.b.degree==PB.a.degree==PB.b.degree==3
A2=l*l*2-l*2+1;B3=l*l*l*4-l*l*6+l*3-1
DD=A2*ell-t*t
KK=B3*(ell*ell)-t*A2*(3*ell)+t*t*t*2
A0=t/ell+1
NS=NB.a*ell+NB.b*m-(t*2+ell+A2)*(l*(2*P02))
PS=PB.a*ell+PB.b*m-(t*3+ell+A2*3+B3)*P02
NL=DD*NB.b+KK*A0*l*(2*P02/m)+DD*DD*l*(4*P02*m/(ell*M))
PL=(DD*PB.b+KK*A0*A0*(3*P02/(2*m))
    +KK*DD*(P02*(3*m*m/(ell*ell)+delta)/(2*m*M))
    +A0*DD*DD*(6*P02*m/(ell*M)))
V0=[E(1),E(l-1-t),E(A0),E(A0)]
V1=[E(),E(),E(m/ell,-1),E(m/ell,1)]
N0=N4(V0);N2=N4(V1)
# N4 is homogeneous quadratic in its vector argument.  Form its true
# polarization directly: taking only the top of N4(V0+V1) would drop
# the needed lower-degree cross term.
def N4_bilinear(a,b):
 ta=tau(a);tb=tau(b);ab=vm(a,b)
 return (tau(vm(dvec,ab))*4-F2*tau(ab)*2
         -(ta*tau(vm(dvec,b))+tb*tau(vm(dvec,a)))*4
         +F2*ta*tb*4+tau(vm(a,DK(b)))+tau(vm(b,DK(a))))
N1=N4_bilinear(V0,V1)
assert not N0.b.value and not N1.b.value and not N2.b.value
assert N0.a.degree==3 and N1.a.degree==2 and N2.a.degree==1
VL=DD*N0.a+KK*N1.a/(2*m)+DD*DD*N2.a/M
assert NS.degree==PS.degree==3 and NL.degree==PL.degree==VL.degree==5
# Independent explicit coefficient formulas for all degree-five inputs.
tv=R(Tp);sv=R(zp)
D2=2*ell-tv*tv
K3=4*ell*ell-6*ell*tv+2*tv**3
assert DD.value==D2 and KK.value==K3
assert NL.value==D2*NB.b.value+K3*(tv/ell)*(2*P02/m)+D2*D2*(4*P02*m/(ell*M))
assert PL.value==(D2*PB.b.value+K3*(tv/ell)**2*(3*P02/(2*m))
 +K3*D2*(P02*(3*m*m/(ell*ell)+delta)/(2*m*M))
 +(tv/ell)*D2*D2*(6*P02*m/(ell*M)))
assert VL.value==D2*N0.a.value+K3*N1.a.value/(2*m)+D2*D2*N2.a.value/M
say("new_actual_individual_original_NP_and_full_V_highest_input",
 completeOriginalGramConstructed=True,originalTraceAndF2ProductsReturned=True,
 completeBCEquivarianceReturned=True,originalMeanNeverReplacedByZero=True,
 actualFullOriginalValueDefinitions=["Nlow","Plow","D*N4(V0)+K*N4_bilinear(V0,V1)/(2m)+D^2*N4(V1)/M"],
 genuinePolarizationNeededForCrossDegree=True,
 exactHighestDegrees=[5,5,5],
 actualExplicitHighestProductsReturned=True,
 noPhysicalDOrHighestD2Inverse=True,
 gradedFunctorOperationCount=top_operation_count,
 noOldHighestNVUnitOrCoefficientIdealGateReplayed=True)
# Reduce the ACTUAL highest polynomial by the same genuine mean rules.
# The fixed order is first T powers, then z powers; no free commutation.
cache={(0,0):[R(1),R(),R()]}
def monomial_row(a,b):
 if (a,b) not in cache:
  if b:cache[a,b]=rm(monomial_row(a,b-1),mz)
  else:cache[a,b]=rm(monomial_row(a-1,0),mt)
 return cache[a,b]
def reduce_top(p):
 p=R(p);assert weight_only(p.d);pay(p.d)
 coeff={}
 for e,c in p.n.to_dict().items():
  assert e[2]==0
  key=(int(e[3]),int(e[4]))
  term=ctx.from_dict({(int(e[0]),int(e[1]),0,0,0):c})
  coeff[key]=coeff.get(key,zero)+term
 out=[R(),R(),R()]
 for (a,b),co in coeff.items():
  q=check_weight(R(co,p.d));vec=monomial_row(a,b)
  out=[x+q*y for x,y in zip(out,vec)]
 for x in out:check_weight(x)
 return out
new_values=[NL,PL,VL,NS,PS]
labels=["original_Nlow_degree5","original_Plow_degree5","entire_original_Vlow_degree5",
        "original_NS_degree3","original_PS_degree3","original_N1_degree2",
        "original_T2z_ambiguity_degree3","original_Tz2_ambiguity_degree3"]
grades=[5,5,5,3,3,2,3,3]
rawrows=[]
for label,obj in zip(labels,new_values):
 row=reduce_top(obj.value)
 rawrows.append(row)
 say("new_complete_individual_highest_three_mean_row",label=label,degree=obj.degree,
     coefficients=[rprofile(x) for x in row],
     fixedOriginalMeanReduction="e0*mt^a*mz^b",
     sourceRetainedByTrueAssociatedGradedOriginalExpression=True)
rawrows.extend([low1,amb1,amb2]);assert len(rawrows)==8
basis={};selected=[]
for index,original in enumerate(rawrows):
 row=original[:];comb=[R(int(k==index)) for k in range(8)]
 for pivot in sorted(basis):
  br,bs=basis[pivot];factor=row[pivot]
  if factor:
   row=[a-factor*b for a,b in zip(row,br)]
   comb=[a-factor*b for a,b in zip(comb,bs)]
 pivot=next((j for j,a in enumerate(row) if a),None)
 if pivot is None:
  assert all(sum((comb[k]*rawrows[k][j] for k in range(8)),R())==0 for j in range(3))
  continue
 factor=row[pivot];row=[a/factor for a in row];comb=[a/factor for a in comb]
 for opivot in list(basis):
  br,bs=basis[opivot];factor=br[pivot]
  if factor:basis[opivot]=([a-factor*b for a,b in zip(br,row)],[a-factor*b for a,b in zip(bs,comb)])
 basis[pivot]=(row,comb);selected.append(index)
 assert all(sum((comb[k]*rawrows[k][j] for k in range(8)),R())==row[j] for j in range(3))
 say("new_individual_highest_actual_weight_row_basis",selectedOriginal=labels[index],
     rank=len(basis),allOriginalThreeCoordinatesReturned=True)
 if len(basis)==3:break
if 0 not in basis or basis[0][0]!=[R(1),R(),R()]:
 say("new_individual_highest_unit_not_obtained",rank=len(basis),
     noNewFiniteLambdaCoverClaim=True,noWholePhiExclusionClaim=True)
 signal.setitimer(signal.ITIMER_REAL,0);raise SystemExit(0)
unitrow,alpha=basis[0]
assert all(sum((alpha[k]*rawrows[k][j] for k in range(8)),R())==int(j==0) for j in range(3))
C=one
for a in alpha:
 assert weight_only(a.n) and weight_only(a.d)
 C=exact(C,C.gcd(a.d))*a.d
beta=[a.n*exact(C,a.d) for a in alpha]
assert all(sum((R(beta[k])*rawrows[k][j] for k in range(8)),R())==R(C)*int(j==0) for j in range(3))
core,paidpart,paid_history=strip_paid(C)
active=[k for k,a in enumerate(alpha) if a];N=max(grades[k] for k in active)
say("new_original_individual_highest_final_weight_cover_and_filtered_lift",
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 activeOriginalRows=[labels[k] for k in active],selectedIndices=selected,
 allEightSourceThreeCoefficientProductsReturned=True,
 finalWeightDenominator=profile(C),finalOriginalMultipliers=[profile(a) for a in beta],
 retainedEntireFinalWeightCover=profile(core),removedOnlyPaidWeights=paid_history,
 exactOriginalWeightIdentity="C*e0=sum(beta_i*highest(original_i))",
 actualFullFilteredLift="sum(beta_i*lambda^(N-grade_i)*original_row_i)",
 liftDegree=N,strictLowerLambdaDegreeBounds=[N-1,N-2,N-2],
 monicLambdaPolynomialOnlyOnCoverComplementDegree=3*N,
 sameOriginalMeanModuleGeneratorsOnlyOnCoverComplement=3*N,
 allFinalWeightZeroFibresRetained=True,noNewWeightUnitAssumed=True,
 noAllWeightsFiniteOrWholePhiExclusionClaim=True,
 coefficientPayloadSaved=False,ordinaryISPClaim=False,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.setitimer(signal.ITIMER_REAL,0)
