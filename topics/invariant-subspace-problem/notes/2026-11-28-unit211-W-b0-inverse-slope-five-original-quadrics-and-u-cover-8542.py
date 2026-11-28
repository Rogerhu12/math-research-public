#!/usr/bin/env python3
"""NEW entire b0: inverse slope weights and FIVE true original quadrics.
Only the necessary original Gram definitions are built. No old C74/C78,
pure full-I11, adjugate-five-cubic, native or NV gate is replayed.
New targets: the four true mean/N1 quadrics plus original value q2 in
(lambda,f); six same-lambda original projections; primitive Q[u][nu] PRS
with every pure-u denominator zero retained in the final original cover.
q2's leading coefficient is NEVER inverted. D only enters the published
necessity of q2 on the current physical D!=0 branch. Complete original I11
is retained; no sample or multivariate gcd-one empty inference.
180 seconds / 4 GiB. No dependencies; no coefficient cache or chunks.
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
ctx=fmpq_mpoly_ctx.get(('u','nu','lam','dummy','f'),'lex')
ep,kp,lp,tp,fp=ctx.gens();Z=ctx.constant(0);O=ctx.constant(1)
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


# New whole current-W birational weight coordinates nu=beta/u.
u,nu,lam,dummy,f=map(R,(ep,kp,lp,tp,fp))
e=u-1;slope_unit=2*u-1
dweight=u*nu-slope_unit;rweight=slope_unit-nu
k=2*rweight/dweight
Vbar=u*k+2;Q=e*k;delta=1-Q
Hweight=nu*nu-(u+1)*nu+slope_unit
ell=u*Hweight/rweight
m=u-ell;theta=u-ell*Q;V2=2*u-ell*Q
M=ell*V2-u*u;bc=M/(4*delta)
T0=V2-2*u*u;J=2*u*(1-u)+ell*Q
Phi=T0+4*u-4+Q;Pf=T0*(J-Q)
P02=(2-3*u)*V2-Q*u+2*u**3
beta=2*u-J/Q
# These complete forward/inverse identities pay dweight/rweight through
# OLD physical units, not by deleting a new weight chart.
assert ell==u*((k+2)**2-2*e*k)/(k*Vbar)
assert nu==slope_unit*(k+2)/Vbar
assert dweight==2*slope_unit*e/Vbar
assert rweight==slope_unit*e*k/Vbar
assert Q==2*e*rweight/dweight
assert m==u*nu*(u-nu)/rweight
assert beta==u*nu
assert Phi==-2*e*(nu-1)
assert J-Q==-2*e*rweight
assert T0==-2*u*e*nu*(nu-1)/dweight
assert delta==(nu*(3*u-2)-slope_unit*slope_unit)/dweight
assert M==ell*ell*delta-m*m
assert J*Phi-Pf==2*u*Q*Phi
assert u-beta==u*(1-nu)
# ONLY the entire b0=0 original branch: Astar is already a unit there.
Astar=4*u*Q-J
assert Astar==u*Q*(nu+2)
kappa=ell/(nu+2)
assert kappa==u*Q*ell/Astar
T=-kappa*(3-2*lam)
G=lam*P02-(1-u)*T0
Pc=Q*P02*(ell+T)-G*T0
t=-(Pf*f+Pc)/(bc*Q*Phi)
V=(J*f-G+bc*Q*t)/Q
W1=T0/2+2*u*f
x=(theta*V-m*W1)/M
y=(ell*W1-u*V)/M
A1=2*f-2*V+2*bc*t
statistics={'exactPolynomialDivisionProducts':0,
 'originalFCoefficientReturns':0,'paidSupportProducts':0,
 'fourSourceContentCancellations':0,'sameFNormIdentities':0}
def exact(p,g):
 out,rem=divmod(p,g);assert not rem and out*g==p
 statistics['exactPolynomialDivisionProducts']+=1
 return out
def weight(p):
 return all(all(int(ex[j])==0 for j in (2,3,4)) for ex in p.to_dict())
def f_free(p):return all(int(ex[4])==0 for ex in p.to_dict())
def fdeg(v):
 v=R(v);assert weight(v.d)
 return max((int(ex[4]) for ex in v.n.to_dict()),default=-1)
def fc(v,j):
 v=R(v);assert weight(v.d)
 return R(ctx.from_dict({(int(ex[0]),int(ex[1]),int(ex[2]),int(ex[3]),0):c
       for ex,c in v.n.to_dict().items() if int(ex[4])==j}),v.d)
def geomdegree(v):
 v=R(v);assert weight(v.d)
 return max((sum(int(ex[j]) for j in (2,3,4))
      for ex in v.n.to_dict()),default=-1)
def profile(p):
 data=[[list(map(int,ex)),str(c)] for ex,c in sorted(p.to_dict().items())]
 raw=json.dumps(data,separators=(',',':')).encode()
 return {'zero':not bool(p),
  'degrees_u_nu_lambda_dummy_f':list(map(int,p.degrees())) if p else [-1]*5,
  'totalDegree':int(p.total_degree()) if p else -1,'terms':len(data),
  'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}

# All supports are pullbacks of ORIGINAL current-W units. nu+2 is paid
# only on the b0 branch by the full original b0/Astar proof.
paid_atoms=[
 ('original_u',ep),('original_e',ep-1),('original_JQ_two_u_minus_one',2*ep-1),
 ('inverse_coordinate_d',dweight.n),('inverse_coordinate_r',rweight.n),
 ('original_equal_weights_k_plus_two_nu',kp),
 ('original_Phi_nu_minus_one',kp-1),
 ('b0_original_Astar_nu_plus_two',kp+2),
 ('original_delta',delta.n),('original_M',M.n),('original_ell',ell.n),
 ('original_m',m.n),('original_P02',P02.n),
 ('whole_original_Lhalf',(2*ell-1).n)]
def strip(p):
 if not p:return p,O,[]
 before=p;removed=O;history=[]
 for label,atom in paid_atoms:
  assert atom and weight(atom)
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
def ck(v):
 v=R(v);paid(v.d);return v
for vv in [u,nu,e,slope_unit,dweight,rweight,k,Vbar,Q,delta,ell,m,M,bc,
           Phi,P02,Astar,kappa,T,t,V,W1,x,y,A1]:
 ck(vv)
assert fc(t,1)==beta/bc and fc(V,1)==2*u and fc(W1,1)==2*u
assert fc(x,1)==2*u*ell*delta/M and fc(y,1)==-2*u*m/M
# Actual quadratic extension and TRUE dual-number Gram. No compact
# derivative-square replacement is used anywhere in this source.
class E:
 def __init__(self,a=0,b=0):
  if isinstance(a,E):self.a=a.a;self.b=a.b;return
  self.a=R(a);self.b=R(b)
 def __bool__(self):return bool(self.a) or bool(self.b)
 def __add__(self,v):
  v=E(v);return E(self.a+v.a,self.b+v.b)
 __radd__=__add__
 def __neg__(self):return E(-self.a,-self.b)
 def __sub__(self,v):return self+-E(v)
 def __rsub__(self,v):return E(v)+-self
 def __mul__(self,v):
  v=E(v);return E(self.a*v.a+delta*self.b*v.b,self.a*v.b+self.b*v.a)
 __rmul__=__mul__
 def __truediv__(self,v):
  v=R(v);return E(self.a/v,self.b/v)
 def __pow__(self,n):
  assert isinstance(n,int) and n>=0
  out=E(1)
  for _ in range(n):out=out*self
  return out
 def __eq__(self,v):
  v=E(v);return self.a==v.a and self.b==v.b
 def conj(self):return E(self.a,-self.b)
b=E(ell/2,m/(2*delta));c=b.conj();a=E(1-ell)
p=E(1,1);q=p.conj();X=E(x,y);Y=X.conj()
assert b*c==E(bc)
assert b*X+c*Y==E(V)
assert b*p*X+c*q*Y==E(W1)
r=X-a*p-c*E(t);s=Y-a*q-b*E(t)
rows=[[E(),E(),p,q],[E(),E(A1),r,s],
      [p,r,E(),E(t)],[q,s,E(t),E()]]
one=[E(1),E(),E(1),E(1)]
def va(v,z):return [a+b for a,b in zip(v,z)]
def vs(h,v):return [h*a for a in v]
def vm(v,z):
 return [v[0]*z[0],v[0]*z[1]+v[1]*z[0],v[2]*z[2],v[3]*z[3]]
def tau(v):return a*v[0]+v[1]+b*v[2]+c*v[3]
def DK(v):return [tau(vm(row,v)) for row in rows]
d=DK(one);F2=tau(d);Kd=DK(d)
assert d==[E(u),E(2*f-V-(1-ell)*u),X,Y]
assert F2==E(2*f)
def mean(j):
 sq=2*tau(vm(rows[0],rows[1])) if j==1 else tau(vm(rows[j],rows[j]))
 return sq-2*Kd[j]-2*vm(d,d)[j]+2*F2*d[j]
E0=mean(0);E1=mean(1);EB=mean(2);EC=mean(3)
assert not E0 and not E1.b and EC==EB.conj()
# Full singleton expression checks 2*p*r, never r*r.
EB_direct=(a*p*p+2*p*r+c*E(t*t)
 -2*(a*p*E(u)+p*d[1]+r*E(u)+c*E(t)*Y)-2*X*X+4*E(f)*X)
assert EB==EB_direct

def N4(v):
 return (2*tau(vm(d,vm(v,v)))-F2*tau(vm(v,v))
   -4*tau(v)*tau(vm(d,v))+2*F2*tau(v)**2+tau(vm(v,DK(v))))
v0=rows[0];v1=rows[1]
Npolar=N4(va(v0,v1))-N4(v0)-N4(v1)
v0c=va(v0,vs(-tau(v0),one));v1c=va(v1,vs(-tau(v1),one))
Pjet=3*tau(vm(vm(v0c,v0c),v1c))
w=lam-1-T
assert N4(v0)==E(2*lam*P02)
assert Pjet==E(3*w*P02)
N1=Npolar-E(4*lam*w*P02)
assert not N1.b
original=[E1.a,EB.a,EB.b,N1.a]
assert all(geomdegree(v)<=2 for v in original)
for v in original:ck(v)


statistics.update(newOriginalFiveRowReturns=0,newPrimitiveScalarReturns=0,
 newBareissProducts=0,newSylvesterCoordinates=0,newWeightScalarReturns=0,
 newPRSContentProducts=0,newPRSEdges=0)
A_lambda=2*lam*lam-2*lam+1
B_lambda=4*lam**3-6*lam*lam+3*lam-1
Dphysical=ell*A_lambda-T*T
Kvalue=ell*ell*B_lambda-3*ell*A_lambda*T+2*T**3
Cstar=Astar*m*m+J*delta*ell*ell
ad=(M*ell*ell*Q*(3-4*lam)+M*Astar*T*T+
    2*M*u*Q*(3-2*lam)*ell*T+Dphysical*Cstar)
bzero=2*m*(Astar*T+u*Q*(3-2*lam)*ell)
assert not bzero
assert M*Astar+Cstar==4*u*Q*delta*ell*ell
q2=ck(2*ad/ell)
assert fdeg(q2)<=0 and geomdegree(q2)<=2
C4=2*m*Dphysical*ad+Kvalue*M*bzero
assert C4==m*Dphysical*ell*q2
Lq=ck(u*Q*delta*ell*kappa*kappa)
paid(Lq.n)
nvalue=2*lam-1
assert q2==2*M*ell*Q*(1-2*nvalue)+Cstar*(nvalue*nvalue+1)-8*Lq*(nvalue-2)**2
def lambda_coeff(v,j):
 v=R(v);assert weight(v.d)
 assert fdeg(v)<=0 and all(int(ex[3])==0 for ex in v.n.to_dict())
 return R(ctx.from_dict({(int(ex[0]),int(ex[1]),0,0,0):cc
  for ex,cc in v.n.to_dict().items() if int(ex[2])==j}),v.d)
qa=[lambda_coeff(q2,j) for j in range(3)]
assert q2==sum((qa[j]*lam**j for j in range(3)),R())
assert qa[2]+3*qa[1]+4*qa[0]==-32*Lq
original5=original+[q2]
cf=ck(bc/(2*u*(u-beta)))
qtag=[R(),cf,cf*ell*delta/m,R(),R()]
qf=sum((qtag[j]*original5[j] for j in range(5)),R())
q0=fc(qf,0);q1=fc(qf,1)
assert qf==f*f+q1*f+q0
assert geomdegree(q1)<=1 and geomdegree(q0)<=2
rowdata=[]
for jj in (0,2,3):
 hf=fc(original5[jj],2)
 rem=original5[jj]-hf*qf
 av=fc(rem,0);bv=fc(rem,1)
 assert rem==av+bv*f and geomdegree(av)<=2 and geomdegree(bv)<=1
 tag=[R(int(h==jj))-hf*qtag[h] for h in range(5)]
 assert sum((tag[h]*original5[h] for h in range(5)),R())==rem
 for vv in [rem,av,bv]+tag:ck(vv)
 rowdata.append(dict(A=av,B=bv,value=rem,tag=tag,source=jj))
 statistics['newOriginalFiveRowReturns']+=1
assert sum((qtag[h]*original5[h] for h in range(5)),R())==qf
statistics['newOriginalFiveRowReturns']+=1
say('new_b0_whole_inverse_weights_and_five_original_quadrics',
 weightCoordinates=['u','nu=beta/u'],
 allForwardInverseWeightIdentitiesReturned=True,
 noNewWeightChartDeleted=True,
 originalNames=['E1','EBe','EBo','N1','q2_from_entire_b0_values'],
 originalProfiles=[profile(v.n) for v in original5],
 allOriginalTotalLambdaFDegreesAtMostTwo=True,
 trueDualProductAndIndependentE1=True,
 qfMonicInF=True,
 q2TopCoefficientNotInverted=True,
 q2ThreeCoefficientPaidUnitCombinationReturned=True,
 q2NecessaryOnOriginalPhysicalDNonzeroBranch=True,
 allQ2DegreeDropFibersRetained=True,
 noOldC74C78OrFullSameFOrFiveCubicGateRun=True)

def original_return(value,tag):
 assert len(tag)==5
 back=sum((tag[j]*original5[j] for j in range(5)),R())
 assert back==value
 for jj in range(max(0,fdeg(back),fdeg(value))+1):
  assert fc(back,jj)==fc(value,jj)
 for vv in [value]+tag:ck(vv)
def primitive_original(label,value,tag,geometry_bound):
 value=R(value);tag=[R(v) for v in tag]
 original_return(value,tag)
 den=O
 for vv in tag:den=exact(den,den.gcd(vv.d))*vv.d
 paid(den)
 nums=[vv.n*exact(den,vv.d) for vv in tag]
 common=Z
 for pp in nums:common=common.gcd(pp)
 if not common:
  assert not value
  return R(),[R() for _ in range(5)]
 newtag=[R(exact(pp,common)) for pp in nums]
 newvalue=sum((newtag[j]*original5[j] for j in range(5)),R())
 assert R(common)*newvalue==R(den)*value
 original_return(newvalue,newtag)
 assert fdeg(newvalue)<=0 and geomdegree(newvalue)<=geometry_bound
 core,removed,hist=strip(newvalue.n)
 if core:
  scale=core.coefficient(0);core/=scale;removed*=scale
 assert core*removed==newvalue.n
 if not core:
  assert not newvalue
  return R(),newtag
 paid(removed)
 finaltag=[R(newvalue.d,removed)*vv for vv in newtag]
 out=R(core)
 original_return(out,finaltag)
 statistics['newPrimitiveScalarReturns']+=1
 return out,finaltag

def polynomial_lambda_coefficient(poly,j):
 assert all(int(ex[3])==0 and int(ex[4])==0 for ex in poly.to_dict())
 return ctx.from_dict({(int(ex[0]),int(ex[1]),0,0,0):cc
  for ex,cc in poly.to_dict().items() if int(ex[2])==j})
def original_sylvester_constant(qpoly,fpoly,nominal_f_degree):
 # Fixed row order: lambda^r*q, 0<=r<m; lambda^r*F, 0<=r<2.
 # It remains a polynomial matrix at EVERY leading-coefficient zero.
 mm=nominal_f_degree;size=mm+2
 qco=[polynomial_lambda_coefficient(qpoly,j) for j in range(3)]
 fco=[polynomial_lambda_coefficient(fpoly,j) for j in range(mm+1)]
 assert all(int(ex[2])<=mm for ex in fpoly.to_dict())
 matrix=[]
 for co,shifts in [(qco,mm),(fco,2)]:
  for shift in range(shifts):
   matrix.append([co[j-shift] if 0<=j-shift<len(co) else Z for j in range(size)])
 work=[rr[:] for rr in matrix]
 trans=[[O if ii==jj else Z for jj in range(size)] for ii in range(size)]
 previous=O
 for kk in range(size):
  pivotrow=next((ii for ii in range(kk,size) if work[ii][kk]),None)
  if pivotrow is None:
   return Z,[Z for _ in range(size)],matrix
  if pivotrow!=kk:
   work[kk],work[pivotrow]=work[pivotrow],work[kk]
   trans[kk],trans[pivotrow]=trans[pivotrow],trans[kk]
  pivot=work[kk][kk]
  for ii in range(size):
   if ii==kk:continue
   oldrow=work[ii][:];oldtrace=trans[ii][:]
   entry=oldrow[kk]
   for jj in range(size):
    if jj!=kk:
     numerator=pivot*oldrow[jj]-entry*work[kk][jj]
     work[ii][jj]=exact(numerator,previous)
     statistics['newBareissProducts']+=1
    trans[ii][jj]=exact(pivot*oldtrace[jj]-entry*trans[kk][jj],previous)
    statistics['newBareissProducts']+=1
   work[ii][kk]=Z
  previous=pivot
 scalar=work[0][0]
 for ii in range(size):
  for jj in range(size):
   assert work[ii][jj]==(scalar if ii==jj else Z)
   assert sum((trans[ii][kk]*matrix[kk][jj] for kk in range(size)),Z)==work[ii][jj]
   statistics['newSylvesterCoordinates']+=1
 return scalar,trans[0],matrix

new_weight=[]
for kind,first,second in [
 ('pair',0,1),('pair',0,2),('pair',1,2),
 ('same_f_norm',0,None),('same_f_norm',1,None),('same_f_norm',2,None)]:
 if kind=='pair':
  ri=rowdata[first];rj=rowdata[second]
  value=ri['A']*rj['B']-rj['A']*ri['B']
  tag=[rj['B']*ri['tag'][h]-ri['B']*rj['tag'][h] for h in range(5)]
  cap=3;label='pair_'+str(first)+'_'+str(second)
 else:
  ri=rowdata[first];av=ri['A'];bv=ri['B']
  value=av*av-q1*av*bv+q0*bv*bv
  multiplier=av-q1*bv-bv*f
  tag=[multiplier*ri['tag'][h]+bv*bv*qtag[h] for h in range(5)]
  cap=4;label='same_f_norm_'+str(first)
 scalar,stag=primitive_original(label,value,tag,cap)
 if not scalar:
  say('new_b0_lambda_condition_zero',label=label,
      originalFiveEquationsAndAllZeroFibersRetained=True)
  continue
 assert scalar.d==O
 say('new_b0_original_same_lambda_condition',
     label=label,numerator=profile(scalar.n),nominalLambdaDegree=cap,
     completeFiveOriginalSourceReturn=True,
     onlyActualFiveMultiplierCommonCancelled=True)
 if geomdegree(scalar)==0:
  weightvalue=scalar;weighttag=stag;fixedsize=0
 else:
  result,cofactor,matrix=original_sylvester_constant(q2.n,scalar.n,cap)
  if not result:
   say('new_b0_fixed_lambda_projection_zero',label=label,fixedSize=cap+2,
       allFiveOriginalEquationsRetained=True,noEmptyConclusion=True)
   continue
  qmult=sum((cofactor[j]*lp**j for j in range(cap)),Z)
  fmult=cofactor[cap]+cofactor[cap+1]*lp
  assert result==qmult*q2.n+fmult*scalar.n
  ptag=[R(fmult)*stag[j] for j in range(5)]
  ptag[4]=ptag[4]+R(qmult*q2.d)
  weightvalue,weighttag=primitive_original(label+'_weight',R(result),ptag,0)
  fixedsize=cap+2
 if not weightvalue:continue
 assert weight(weightvalue.n) and weightvalue.d==O
 original_return(weightvalue,weighttag)
 statistics['newWeightScalarReturns']+=1
 new_weight.append(dict(label=label,value=weightvalue.n,tag=weighttag))
 say('new_b0_complete_original_pure_weight_projection',
     label=label,fixedLambdaSylvesterSize=fixedsize,
     necessaryPolynomial=profile(weightvalue.n),
     allFiveOriginalSourceCoefficientsReturned=True,
     noQ2OrSameLambdaLeadingInverse=True,
     allInstantaneousBareissPivotAndHeadZeroFibersRetained=True,
     allUnpaidEquationContentZeroFibersRetained=True)
 if int(weightvalue.n.total_degree())==0:
  say('new_entire_b0_original_five_quadrics_unit',
      label=label,actualOriginalConstant=str(weightvalue.n),
      wholeCurrentB0Excluded=True,
      allFiveOriginalSourceCoefficientsReturned=True,
      physicalDOnlyUsedByOriginalQ2Necessity=True)
  break

# A genuinely NEW elimination in the NEW weight variable nu. Only pure-u
# coefficient contents are divided; every such zero fiber enters the final
# denominator cover. No multivariate gcd=1 is used to call a fiber empty.
prs_nodes=[]
def nu_degree(poly):
 return max((int(ex[1]) for ex in poly.to_dict()),default=-1)
def u_only(poly):
 return all(all(int(ex[j])==0 for j in (1,2,3,4)) for ex in poly.to_dict())
def nu_coefficient(poly,j):
 assert weight(poly)
 return ctx.from_dict({(int(ex[0]),0,0,0,0):cc
  for ex,cc in poly.to_dict().items() if int(ex[1])==j})
def u_content(poly):
 if not poly:return O
 content=Z
 for jj in range(nu_degree(poly)+1):
  content=content.gcd(nu_coefficient(poly,jj))
 assert content and u_only(content)
 content=content/content.coefficient(0)
 return content
def prs_node(raw,edge=None,initial=None):
 if not raw:return None
 content=u_content(raw)
 value=exact(raw,content)
 assert content*value==raw and weight(value)
 parents=[] if edge is None else [edge['left'],edge['right']]
 depth=1+max((prs_nodes[j]['depth'] for j in parents),default=0)
 node=dict(value=value,content=content,depth=depth,edge=edge,initial=initial)
 prs_nodes.append(node)
 statistics['newPRSContentProducts']+=1
 return len(prs_nodes)-1
def prs_subtract(left,right):
 lpv=prs_nodes[left]['value'];rpv=prs_nodes[right]['value']
 dl=nu_degree(lpv);dr=nu_degree(rpv);assert dl>=dr>=0
 aa=nu_coefficient(rpv,dr);bb=nu_coefficient(lpv,dl)
 assert aa and bb and u_only(aa) and u_only(bb)
 shift=dl-dr
 raw=aa*lpv-bb*kp**shift*rpv
 assert not raw or nu_degree(raw)<dl
 node=prs_node(raw,edge=dict(left=left,right=right,
                            leftCoefficient=aa,rightCoefficient=bb,
                            nuShift=shift))
 if node is not None:
  nd=prs_nodes[node]
  assert nd['content']*nd['value']==aa*lpv-bb*kp**shift*rpv
 statistics['newPRSEdges']+=1
 if statistics['newPRSEdges']%20==0:
  say('new_b0_nu_primitive_PRS_progress',
      completeEdges=statistics['newPRSEdges'],nodes=len(prs_nodes),
      currentNuDegree=nu_degree(raw),currentProfile=profile(raw))
 return node
def original_u_profile(poly):
 assert u_only(poly)
 data=poly.to_dict()
 coeffs=[str(data.get((j,0,0,0,0),0))
         for j in range(max((int(ex[0]) for ex in data),default=-1)+1)]
 raw=json.dumps(coeffs,separators=(',',':')).encode()
 return dict(degree=len(coeffs)-1,coefficientBytes=len(raw),
             coefficientSHA256=hashlib.sha256(raw).hexdigest())
unit_found=any(int(item['value'].total_degree())==0 for item in new_weight)
new_cover=None
if not unit_found and new_weight:
 order=sorted(range(len(new_weight)),key=lambda i:
              (nu_degree(new_weight[i]['value']),
               int(new_weight[i]['value'].total_degree()),i))
 current=None
 for idx in order:
  incoming=prs_node(new_weight[idx]['value'],initial=idx)
  if current is None:current=incoming
  else:
   left=current;right=incoming
   while right is not None:
    if left is None:
     left,right=right,None;break
    if nu_degree(prs_nodes[left]['value'])<nu_degree(prs_nodes[right]['value']):
     left,right=right,left
    while left is not None and nu_degree(prs_nodes[left]['value'])>=nu_degree(prs_nodes[right]['value']):
     left=prs_subtract(left,right)
    left,right=right,left
   current=left
  assert current is not None
  if nu_degree(prs_nodes[current]['value'])==0:break
 terminal=prs_nodes[current]['value']
 if nu_degree(terminal)>0:
  say('new_b0_nu_positive_degree_remainder_retained',
      currentNuDegree=nu_degree(terminal),profile=profile(terminal),
      noCompletePureUCoverClaim=True,
      allOriginalFiveQuadricsAndValueConditionsRetained=True)
 else:
  assert u_only(terminal) and int(terminal.total_degree())==0
  reachable=set();pending=[current]
  while pending:
   idx=pending.pop()
   if idx in reachable:continue
   reachable.add(idx)
   edge=prs_nodes[idx]['edge']
   if edge is not None:pending += [edge['left'],edge['right']]
  denominator=O
  for idx in sorted(reachable):
   cc=prs_nodes[idx]['content']
   denominator=exact(denominator,denominator.gcd(cc))*cc
  assert u_only(denominator) and denominator
  from flint import fmpq_poly
  def upoly(poly):
   assert u_only(poly)
   deg=max((int(ex[0]) for ex in poly.to_dict()),default=-1)
   result=fmpq_poly([poly.to_dict().get((j,0,0,0,0),0) for j in range(deg+1)])
   return result
  Hp=upoly(denominator);derivative=Hp.derivative();gg=Hp.gcd(derivative)
  sf,rem=divmod(Hp,gg)
  assert not rem and sf*gg==Hp and sf
  sf=sf/sf[sf.degree()]
  sfpoly=ctx.from_dict({(j,0,0,0,0):sf[j] for j in range(sf.degree()+1) if sf[j]})
  max_content_degree=max(1,max(upoly(prs_nodes[idx]['content']).degree() for idx in reachable))
  support_returns=0
  for idx in sorted(reachable):
   cp=upoly(prs_nodes[idx]['content'])
   if cp.degree()==0:continue
   exponent=max_content_degree
   acc=fmpq_poly([1]);base=sf
   while exponent:
    if exponent%2:
     product=acc*base;qq,acc=divmod(product,cp)
     assert qq*cp+acc==product;support_returns+=1
    exponent//=2
    if exponent:
     product=base*base;qq,base=divmod(product,cp)
     assert qq*cp+base==product;support_returns+=1
   assert not acc
  exponent_bound=max_content_degree*prs_nodes[current]['depth']
  core,paidpart,paid_history=strip(sfpoly)
  assert core and core*paidpart==sfpoly and u_only(core)
  paid(paidpart)
  core=core/core.coefficient(0)
  new_cover=core
  unit_found=int(core.total_degree())==0
  say('new_b0_complete_original_pure_u_cover',
      originalPolynomialParameter=original_u_profile(core),
      originalDAGTerminal=current,reachableDAGNodes=len(reachable),
      allPrimitivePRSEdgesReturned=True,
      onlyPureUContentsDivided=True,
      completeDenominatorSquarefreeSupport=original_u_profile(sfpoly),
      maximumContentMultiplicityBound=max_content_degree,
      contentSupportModularPowerProducts=support_returns,
      originalIdealCoverPowerBound=exponent_bound,
      exactClaim='cover^N belongs to the five-original-row ideal after ONLY old paid units',
      onlyOldPaidSupportsRemoved=paid_history,
      allNewPureUZeroFibersRetained=True,
      originalNuLeadingCoefficientsOnlyMultipliedNeverInverted=True,
      wholeCurrentB0Excluded=unit_found,
      noMultivariateGCDOneEmptyInference=True)
  if not unit_found:
   # This is the FIRST QQ factorization of the NEW pure-u cover.
   # The already completed cover checkpoint above remains valid even if
   # this distinct final parameter decomposition reaches the same budget.
   fpcover=upoly(core)
   factor_constant,factors=fpcover.factor()
   rebuilt=fmpq_poly([factor_constant]);factor_records=[]
   for fac,multiplicity in factors:
    rebuilt*=fac**int(multiplicity)
    factor_polynomial=ctx.from_dict({(j,0,0,0,0):fac[j] for j in range(fac.degree()+1) if fac[j]})
    factor_records.append(dict(parameter=original_u_profile(factor_polynomial),
                               multiplicity=int(multiplicity)))
   assert rebuilt==fpcover
   say('new_b0_pure_u_complete_QQ_cover_factors',
       completeOriginalCoverFactorProductReturned=True,
       factors=factor_records,
       allRemainingEntireConstantFieldsRetained=True,
       noRootSamplingOrModularEmptyInference=True)

say('new_b0_five_original_quadrics_and_first_weight_elimination_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 statistics=statistics,newWeightConditions=len(new_weight),
 wholeCurrentB0Excluded=unit_found,
 completeNewPureUCoverAvailable=new_cover is not None,
 oldC74C78FullSameFOrFiveCubicGateNotRun=True,
 originalI11StillRetained=True,
 physicalDOnlyUsedInPublishedOriginalQ2Necessity=True,
 noQ2LambdaHeadOrNewGeometryInverse=True,
 allUnpaidWeightAndLeadingZeroBranchesRetained=True,
 noLargeCoefficientCacheOrChunksWritten=True,
 maxRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 ordinaryISPClaim=False)
signal.setitimer(signal.ITIMER_REAL,0)
