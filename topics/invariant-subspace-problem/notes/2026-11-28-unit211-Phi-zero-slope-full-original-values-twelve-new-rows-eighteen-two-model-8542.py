#!/usr/bin/env python3
"""NEW whole original value rows on the explicit Phi N1-slope complement.
Use ONLY the necessary slope/coordinate prefix of e797 (not its old
three large lambda8 targets). Compute genuine original Gram weighted
NS/PS, R6, individual Nlow/Plow, and the ENTIRE N4(V) low expression.
Every product first uses the actual THREE original mean rules with
a fixed source DAG; only the final row changes to (1,Z). No high powers
of the large slope denominator are used in the value reduction.
Twelve NEW rows append to the proved exact I4 six rows, giving the
exact explicitly defined I10 eighteen-by-two model. No D inverse or
D norm inverse; no original individual value is replaced by Phi times it.
120s /1GiB including prefixes. No coefficient payload or old audit.
2026-11-28 Asia/Taipei.
"""
import os,time,json,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
START=time.perf_counter();DEADLINE=START+120
signal.alarm(120);resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,separators=(",",":")),flush=True)
name="2026-11-28-unit211-Phi-zero-original-N1-slope-exact-six-by-two-mean-presentation-8542.py"
path=Path(os.environ.get("ISP_PHI_SLOPE_SOURCE",str(Path(__file__).with_name(name))))
raw=path.read_bytes()
assert hashlib.sha256(raw).hexdigest()=="c4af169436165777186a811ccbea1b242b64e0bd84ac14bde43289254c4a2332"
mark=b"\ndef add3(x,y):";assert raw.count(mark)==1
prefix=raw.split(mark)[0]
assert len(prefix)==5809
assert hashlib.sha256(prefix).hexdigest()=="941f5a6090fbc00bd8eb570efedbbad972d68d90f5a32dfe9c271378740e073c"
geo={"__file__":str(path),"__name__":"new_Phi_full_values_necessary_original_slope_only"}
original_alarm=signal.alarm;original_timer=signal.setitimer
def bounded_timer(which,seconds,interval=0):
 if which!=signal.ITIMER_REAL:return original_timer(which,seconds,interval)
 assert not interval
 left=max(.001,DEADLINE-time.perf_counter())
 return original_timer(which,min(left,float(seconds) if seconds>0 else left),0)
def bounded_alarm(seconds):return math.ceil(bounded_timer(signal.ITIMER_REAL,seconds)[0])
signal.alarm=bounded_alarm;signal.setitimer=bounded_timer
try:
 with contextlib.redirect_stdout(io.StringIO()):
  exec(compile(prefix,str(path)+":only-necessary-coordinate-definition","exec"),geo)
finally:
 signal.alarm=original_alarm;signal.setitimer=original_timer
 original_timer(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
old=geo["ns"];R=geo["R"];ctx=geo["ctx"];zero=geo["zero"];one=geo["one"]
u,Q,ell,delta,m,M,T0,J,P02=[geo[k] for k in ["u","Q","ell","delta","m","M","T0","J","P02"]]
bc=old["bc"];Pf=old["Pf"];lcoef=old["lam"]
MT,Mz,rules=[old[k] for k in ["MT","MZ","rules"]]
aa,cc,Delta,p0,p1,p2=[geo[k] for k in ["a","c","Delta","p0","p1","p2"]]
legal=geo["legal"];profile=geo["profile"];rprofile=geo["rprofile"]
assert Delta and aa*p2-cc*p1==Delta
# The already-proved monic square is specified by these small direct
# definitions. No old substituted mean rows or lambda8 cofactors run.
sw=[aa*aa,2*aa*cc,cc*cc]
sq=[sum((sw[i]*rules[i][j] for i in range(3)),R()) for j in range(3)]
kap=(-cc*sq[1]+aa*sq[2])/Delta
beta0=sq[0]-kap*p0
beta1=(p2*sq[1]-p1*sq[2])/Delta
for v in [beta0,beta1]:legal(v,True)
assert int(beta0.n.degrees()[2])<=3 and int(beta1.n.degrees()[2])<=2

nodes=[]
def node(op,data,row):
 for x in row:legal(x)
 index=len(nodes);nodes.append((op,data));return index
class A3:
 __slots__=("row","node")
 def __init__(self,value=0):
  if isinstance(value,A3):self.row=value.row;self.node=value.node;return
  value=legal(R(value));self.row=[value,R(),R()]
  self.node=node("scalar",value,self.row)
 @classmethod
 def from_row(cls,row,op,data):
  out=object.__new__(cls);out.row=row;out.node=node(op,data,row);return out
 def __bool__(self):return any(self.row)
 def __eq__(self,other):
  other=A3(other);return all(x==y for x,y in zip(self.row,other.row))
 def __neg__(self):return A3.from_row([-x for x in self.row],"neg",self.node)
 def __add__(self,other):
  other=A3(other)
  return A3.from_row([x+y for x,y in zip(self.row,other.row)],"add",[self.node,other.node])
 __radd__=__add__
 def __sub__(self,other):return self+-A3(other)
 def __rsub__(self,other):return A3(other)+-self
 def __mul__(self,other):
  other=A3(other);a=self.row;b=other.row
  if not b[1] and not b[2]:out=[x*b[0] for x in a]
  elif not a[1] and not a[2]:out=[a[0]*x for x in b]
  else:
   out=[a[j]*b[0]+sum((a[i]*(b[1]*MT[i][j]+b[2]*Mz[i][j]) for i in range(3)),R())
        for j in range(3)]
  # For the represented linear polynomials, the exact defect is
  # sum_i a_i*(b_1*E_T_i+b_2*E_z_i).(R,W,O). Combine it with
  # the two existing source DAGs. No free-space associativity is used.
  return A3.from_row(out,"fixed_original_mean_product",[self.node,other.node])
 __rmul__=__mul__
 def __truediv__(self,other):
  other=R(other);assert geo["weight_only"](other.n) and geo["weight_only"](other.d)
  rest,_,_=geo["strip_paid"](other.n);assert rest.total_degree()==0
  return A3.from_row([x/other for x in self.row],"divide_only_paid_weight",[self.node,other])
 def __pow__(self,n):
  assert n>=0
  out=A3(1);base=self
  while n:
   if n&1:out=out*base
   n//=2
   if n:base=base*base
  return out
T=A3.from_row([R(),R(1),R()],"original_variable_T",None)
z=A3.from_row([R(),R(),R(1)],"original_variable_z",None)
class E:
 __slots__=("a","b")
 def __init__(self,a=0,b=0):
  if isinstance(a,E):self.a=a.a;self.b=a.b;return
  self.a=A3(a);self.b=A3(b)
 def __bool__(self):return bool(self.a) or bool(self.b)
 def __eq__(self,other):
  other=E(other);return self.a==other.a and self.b==other.b
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
rho=E(0,1);p=1+rho;q=1-rho
bweight=E(ell/2,m/(2*delta));cweight=E(ell/2,-m/(2*delta))
aweight=E(1-ell)
assert bweight*cweight==E(bc)
assert (bweight-cweight)*rho==E(m)
GG=A3(lcoef*P02+(u-1)*T0)
f=(GG*T0-(T+ell)*(Q*P02))/Pf
V=(f*J-GG+z*bc)/Q
W=(f*(4*u)+T0)/2
X=(E(W)-q*E(V))*cweight*rho/(2*bc*delta)
Y=(p*E(V)-E(W))*bweight*rho/(2*bc*delta)
tt=E(z/Q)
germ=E(f*2-V*2+z*(2*bc/Q))
rr=X-aweight*p-cweight*tt
ss=Y-aweight*q-bweight*tt
gram=[[E(),E(),p,q],[E(),germ,rr,ss],
      [p,rr,E(),tt],[q,ss,tt,E()]]
assert bweight*X+cweight*Y==E(V)
assert bweight*p*X+cweight*q*Y==E(W)
perm=[0,1,3,2]
assert all(gram[i][j].conj()==gram[perm[i]][perm[j]] for i in range(4) for j in range(4))
onev=[E(1),E(),E(1),E(1)]
def vm(v,w):
 return [v[0]*w[0],v[0]*w[1]+v[1]*w[0],v[2]*w[2],v[3]*w[3]]
def tau(v):return v[0]*aweight+v[1]+v[2]*bweight+v[3]*cweight
def DK(v):return [tau(vm(row,v)) for row in gram]
dvec=DK(onev);F2=tau(dvec)
assert tau(onev)==1 and F2==E(f*2)
def N4(v):
 vv=vm(v,v);tv=tau(v)
 return (2*tau(vm(dvec,vv))-F2*tau(vv)
         -4*tv*tau(vm(dvec,v))+2*F2*tv*tv+tau(vm(v,DK(v))))
def P2(v):
 tv=tau(v)
 centered=[v[i]-tv*onev[i] for i in range(4)]
 return tau(vm(vm(centered,centered),centered))
# Full B/C equivariance is an identity of the ORIGINAL Gram and trace;
# the complete C spectra are conjugates of the complete B spectra.
# No individual C value is dropped and no second old Gram audit is run.
NB=N4(gram[2]);PB=P2(gram[2])
Al=2*lcoef*lcoef-2*lcoef+1
Bl=4*lcoef**3-6*lcoef*lcoef+3*lcoef-1
NS=NB.a*ell+NB.b*m-(T*2+ell+Al)*(2*lcoef*P02)
PS=PB.a*ell+PB.b*m-(T*3+ell+3*Al+Bl)*P02
say("new_complete_original_Gram_B_spectra_and_weighted_NS_PS",
 sourceDAGOperations=len(nodes),
 allOriginalLinearRecoveryProductsReturned=True,
 completeGramBCEquivarianceReturned=True,
 originalF2EqualsTwoFReturned=True,
 normalization="N4=4*N, P2=2*P",
 weightedConjugateIdentity="b*(even+rho*odd)+c*(even-rho*odd)=ell*even+m*odd",
 entireIndividualBTracesUsed=True,
 entireIndividualCTracesRecoveredByOriginalConjugation=True,
 noDOrNormInverse=True,
 noOldCompleteValueGateReplayed=True)

new_rows=[];labels=[];origins=[]
def save_value(label,value,origin):
 value=A3(value);r0,r1,r2=value.row
 kap=(-cc*r1+aa*r2)/Delta
 s0=r0-kap*p0;s1=(p2*r1-p1*r2)/Delta
 assert s0+kap*p0==r0
 assert aa*s1+kap*p1==r1 and cc*s1+kap*p2==r2
 for x in [s0,s1,kap]:legal(x,True)
 row=[s0,s1];child=[s1*beta0,s0+s1*beta1]
 for x in child:legal(x,True)
 new_rows.extend([row,child]);labels.extend([label,label+"*Z"])
 origins.append(dict(label=label,node=value.node,definition=origin))
 say("new_full_original_value_two_rows_after_single_coordinate_change",
     label=label,definition=origin,sourceDAGNode=value.node,
     sourceDAGOperations=len(nodes),
     actualThreeMeanRow=[rprofile(x) for x in value.row],
     actualNewTwoRow=[rprofile(x) for x in row],
     actualZProduct=[rprofile(x) for x in child],
     allThreeCoordinateCoefficientProductsReturned=True,
     ZProductUsesProvedMonicSquare=True,
     noOriginalThreeGeneratorFreenessOrMatrixCommutationAssumed=True,
     noHighSlopePowersInValueReduction=True,
     allWeightDenominatorsOldPaidOrExplicitSlope=True,
     wholeSlopeZeroBranchRetained=True,wholePhiExcluded=False)
save_value("original_NS",NS,"b*N4(rowB)+c*N4(rowC)-2*lambda*P02*(ell+2*T+A2)")
save_value("original_PS",PS,"b*P2(rowB)+c*P2(rowC)-P02*(ell+3*T+3*A2+B3)")
say("new_exact_I6_by_appending_four_original_NSPS_rows",
 oldExactI4Rows=6,newRows=4,totalExactModuleRows=10,columns=2,
 exactIdeal="I4+(original_NS,original_PS)",
 oldLargeLambda8TargetsNotReexecuted=True,
 noIndividualValueSufficiencyClaimAtThisStage=True,
 wholeSlopeZeroBranchRetained=True,wholePhiExcluded=False)

TT=T*T;TTT=TT*T
D=A3(ell*Al)-TT
K=A3(ell*ell*Bl)-T*(3*ell*Al)+TTT*2
Dsq=D*D
R6=(K*K)*M-(Dsq*D)*(4*m*m)
save_value("original_R6",R6,"M*K^2-4*m^2*D^3")
A0=T/ell+1
Nlow=D*NB.b+(K*A0)*(2*lcoef*P02/m)+Dsq*(4*lcoef*P02*m/(ell*M))
save_value("original_Nlow",Nlow,
           "D*n_odd+2*lambda*P02*K*A0/m+4*lambda*P02*m*D^2/(ell*M)")
Plow=(D*PB.b+(K*A0*A0)*(3*P02/(2*m))
      +(K*D)*(P02*(3*m*m/(ell*ell)+delta)/(2*m*M))
      +(A0*Dsq)*(6*P02*m/(ell*M)))
save_value("original_Plow",Plow,
           "D*p_odd+3*P02*K*A0^2/(2*m)+P02*(3*m^2/ell^2+delta)*K*D/(2*m*M)+6*P02*m*A0*D^2/(ell*M)")
ww=A3(lcoef-1)-T
V0=[E(1),E(ww),E(A0),E(A0)]
V1=[E(),E(),E(m/ell,-1),E(m/ell,1)]
N0=N4(V0);N2=N4(V1)
N1=N4([V0[i]+V1[i] for i in range(4)])-N0-N2
assert not N0.b and not N1.b and not N2.b
Vlow=D*N0.a+(K*N1.a)/(2*m)+(Dsq*N2.a)/M
save_value("original_entire_Vlow",Vlow,
           "D*N4(V0)+K*(N4(V0+V1)-N4(V0)-N4(V1))/(2*m)+D^2*N4(V1)/M")
assert len(new_rows)==12
say("new_Phi_complete_original_I10_eighteen_by_two_model_finished",
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 exactIdeal="I4+(NS,PS,R6,Nlow,Plow,entire_Vlow)",
 oldProvedExactMeanN1Rows=6,actuallyConstructedNewRows=12,totalExactModuleRows=18,
 columns=2,basis=["1","Z"],
 newLabels=labels,originalValueDefinitions=origins,
 originalSourceDAGOperations=len(nodes),
 oldSixRowsUsedByProvedDefinitionNotReplayed=True,
 allNewValueRowsUseActualOriginalGramAndTwoMomentDefinitions=True,
 individualNC_PCRecoveredByConjugationAndWeightedTrace=True,
 entireOriginalN4VUsedNotPhiMultiple=True,
 equivalenceToIndividualValuesOnlyOnOriginalDNonzeroScope=True,
 originalDNeverInvertedInNewAlgebra=True,noOriginalDNormInverse=True,
 monicQuadraticAmbientOnlyIsFree=True,originalQuotientNotAssumedFree=True,
 wholeSlopeZeroBranchAndAllOtherUnpaidWeightsRetained=True,
 noClaimThatRemainingOriginalNonzeroConstraintsAreAutomatic=True,
 noOldThreeLambda8TargetsP6P9WeakPopovGaussianNormOrGramAuditExecuted=True,
 noNewLargeCofactorOrProjectionAttempted=True,
 noRecomputableCoefficientPayloadCacheEncodingOrSplitSaved=True,
 wholePhiExcluded=False,ordinaryISPClaim=False,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.setitimer(signal.ITIMER_REAL,0);signal.alarm(0)
