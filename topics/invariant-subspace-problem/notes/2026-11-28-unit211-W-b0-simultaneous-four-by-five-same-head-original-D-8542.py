#!/usr/bin/env python3
"""NEW entire b0: simultaneous 4-by-5 original quadratic coefficient
matrix and adjugate recovery of lambda,f,lambda^2,lambda*f.
The old six Sylvester projections and frozen nu PRS are NOT executed.
Only the necessary true five-quadrics, qf, r_i DEFINITIONS are rebuilt.
No new head is inverted. One common factor of all twenty true original
multipliers is cancelled simultaneously, preserving one SAME head h.
New targets are h*D-C_D and three pure-weight Veronese/qf combinations;
every target returns all FIVE true original sources.
180 seconds /4 GiB; self-contained. All h=0 fibers and all I11 remain.
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
 'originalFCoefficientReturns':0,'paidSupportProducts':0}
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

# Fixed OLD 36-term original G36 definition. Only its new rational
# pullback is used; no old whole-G36 exclusion gate or factor is replayed.
# Source c489948be8e967575417a1e21de51cd5a915dc80 and published whole
# R150-appendix-unit211-W-G36-entire-original-exclusion-and-global-F-recovery.md.
GDATA=[[0,0,"4096"],[0,1,"9216"],[0,2,"7680"],[0,3,"3072"],[0,4,"592"],[0,5,"24"],[0,6,"-10"],[0,7,"-1"],[1,1,"-6144"],[1,2,"-16128"],[1,3,"-14336"],[1,4,"-6048"],[1,5,"-1416"],[1,6,"-186"],[1,7,"-9"],[2,2,"512"],[2,3,"6016"],[2,4,"6560"],[2,5,"2528"],[2,6,"468"],[2,7,"50"],[2,8,"2"],[3,3,"1792"],[3,4,"832"],[3,5,"-832"],[3,6,"-392"],[3,7,"-50"],[3,8,"-2"],[4,4,"-256"],[4,5,"-544"],[4,6,"-24"],[4,7,"24"],[4,8,"4"],[5,5,"-192"],[5,7,"-8"],[6,6,"32"]]
G36_original_definition=ctx.from_dict({(i,j,0,0,0):int(cc) for i,j,cc in GDATA})
assert len(GDATA)==36
assert profile(G36_original_definition)['sha256']=='994fe0821fb8c70e7f82edf8aea19a17ee1ffa99fd5fd4b5b3c065daea84ad78'
G36_pullback=sum((R(int(cc))*e**i*k**j for i,j,cc in GDATA),R())
G36_clear=sum((int(cc)*(ep-1)**i*(2*rweight.n)**j*dweight.n**(8-j)
              for i,j,cc in GDATA),Z)
assert G36_pullback*R(dweight.n**8)==R(G36_clear)
assert weight(G36_pullback.n) and weight(G36_pullback.d)


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
 ('whole_original_Lhalf',(2*ell-1).n),
 ('whole_original_G36_pullback',G36_pullback.n)]
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
           Phi,P02,G36_pullback,Astar,kappa,T,t,V,W1,x,y,A1]:
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


statistics.update(newOriginalFiveRowReturns=0)
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

# NEW simultaneous source matrix: no old lambda projection/PRS construction.
statistics.update(newOriginalFiveSourceCoordinates=0,newAdjugateCoordinates=0,
                  newCommonTwentyMultiplierProducts=0,
                  newPureWeightOriginalReturns=0)
def original_return(value,tag):
 assert len(tag)==5
 value=R(value);back=sum((tag[j]*original5[j] for j in range(5)),R())
 assert back==value
 for jj in range(max(0,fdeg(back),fdeg(value))+1):
  assert fc(back,jj)==fc(value,jj)
  statistics['newOriginalFiveSourceCoordinates']+=1
 for vv in [value]+list(tag):ck(vv)

monomials=[R(1),lam,f,lam*lam,lam*f]
powers=[(0,0),(1,0),(0,1),(2,0),(1,1)]
def coefficient_pair(value,a0,b0):
 value=R(value);assert weight(value.d)
 return R(ctx.from_dict({(int(ex[0]),int(ex[1]),0,0,0):cc
  for ex,cc in value.n.to_dict().items()
  if int(ex[2])==a0 and int(ex[4])==b0}),value.d)
rawfour=[rr['value'] for rr in rowdata]+[q2]
rawtags=[rr['tag'] for rr in rowdata]+[[R(),R(),R(),R(),R(1)]]
matrix=[];clearedtags=[];clearedvalues=[]
for value,tag in zip(rawfour,rawtags):
 assert all(weight(vv.n) and weight(vv.d) for vv in tag)
 assert all(int(ex[3])==0 and (int(ex[2]),int(ex[4])) in powers
            for ex in value.n.to_dict())
 coeffs=[coefficient_pair(value,*ex) for ex in powers]
 assert sum((coeffs[j]*monomials[j] for j in range(5)),R())==value
 den=O
 for v0 in coeffs:den=exact(den,den.gcd(v0.d))*v0.d
 paid(den)
 row=[v0.n*exact(den,v0.d) for v0 in coeffs]
 trow=[R(den)*v0 for v0 in tag]
 vrow=R(den)*value
 assert sum((R(row[j])*monomials[j] for j in range(5)),R())==vrow
 original_return(vrow,trow)
 matrix.append(row);clearedtags.append(trow);clearedvalues.append(vrow)
say('new_b0_simultaneous_original_four_by_five_ready',
    monomials=['1','lambda','f','lambda^2','lambda*f'],
    entireNuForwardInverseWeightsAndBzeroQ2Definitions=True,
    onlyOldG36DefinitionPullbackAddedToNewPaidSupports=True,
    fourOriginalRowValues=[profile(v0.n) for v0 in clearedvalues],
    allTwentySourceCoordinatesOriginal=True,
    noOldSixSylvesterOrPrimitivePRSRun=True)
# Matrix rows are four equations; columns are (1,lambda,f,lambda^2,lambda*f).
# B consists of columns 1..4. adj(B)*four = det(B)*monomials[1:]+adj(B)*col0.
B=[row[1:] for row in matrix]
col0=[row[0] for row in matrix]
def det3(A):
 return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
        -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
        +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
adj=[]
for i in range(4):
 row=[]
 for j in range(4):
  sub=[[B[aa][bb] for bb in range(4) if bb!=i]
       for aa in range(4) if aa!=j]
  row.append((-1)**(i+j)*det3(sub))
 adj.append(row)
hraw=sum((B[0][j]*adj[j][0] for j in range(4)),Z)
for i in range(4):
 for j in range(4):
  lhs=sum((B[i][k0]*adj[k0][j] for k0 in range(4)),Z)
  rhs=sum((adj[i][k0]*B[k0][j] for k0 in range(4)),Z)
  assert lhs==(hraw if i==j else Z) and rhs==lhs
  statistics['newAdjugateCoordinates']+=2
vraw=[sum((adj[i][j]*col0[j] for j in range(4)),Z) for i in range(4)]
raw_recovery_tags=[
 [sum((R(adj[i][j])*clearedtags[j][a0] for j in range(4)),R())
  for a0 in range(5)] for i in range(4)]
for i in range(4):
 original_return(R(hraw)*monomials[i+1]+R(vraw[i]),raw_recovery_tags[i])
# ONE cancellation shared by ALL four recovery rows. Thus they retain
# the SAME h; no separate normalization can silently change that head.
den=O
for row in raw_recovery_tags:
 for vv in row:den=exact(den,den.gcd(vv.d))*vv.d
paid(den)
nums=[[vv.n*exact(den,vv.d) for vv in row] for row in raw_recovery_tags]
common=Z
for row in nums:
 for pp in row:common=common.gcd(pp)
if not common:
 assert not hraw and all(not v0 for v0 in vraw)
 say('new_b0_adjugate_all_original_multipliers_zero',
     allFiveOriginalEquationsAndEntireHeadZeroLocusRetained=True,
     noRecoveryOrEmptyConclusion=True)
 raise SystemExit(0)
recovery_tags=[[R(exact(pp,common)) for pp in row] for row in nums]
h=R(den*hraw,common)
K=[-R(den*v0,common) for v0 in vraw]
H=[h*monomials[i+1]-K[i] for i in range(4)]
for i in range(4):
 original_return(H[i],recovery_tags[i])
 assert R(common)*H[i]==R(den)*(R(hraw)*monomials[i+1]+R(vraw[i]))
 statistics['newCommonTwentyMultiplierProducts']+=1
for vv in [h]+K:ck(vv);assert weight(vv.n)
for i in range(4):
 assert R(matrix[i][0])*h+sum((R(B[i][j])*K[j] for j in range(4)),R())==0
 assert sum((R(B[i][j])*H[j] for j in range(4)),R())==h*clearedvalues[i]
hcore,hpaid,hpaid_history=strip(h.n)
head_paid=bool(hcore) and int(hcore.total_degree())==0
say('new_b0_same_head_four_complete_original_recovery_rows',
    rawHead=profile(hraw),normalizedHeadNumerator=profile(h.n),
    normalizedHeadDenominator=profile(h.d),
    allTwentyActualMultiplierCommon=profile(common),
    normalizedKernelNumerators=[profile(v0.n) for v0 in K],
    normalizedKernelDenominators=[profile(v0.d) for v0 in K],
    sameHeadForAllFourRows=True,
    headIsAlreadyPaid=bool(head_paid),
    remainingHeadSupport=profile(hcore),
    headPaidGcdLayers=hpaid_history,
    noHeadInverseUsed=True,
    headZeroFibersKeepAllFourKAndAllFiveOriginalEquations=True)
# A genuinely NEW direct D relation, without treating its norm or h as a unit.
dd=[lambda_coeff(Dphysical,j) for j in range(3)]
assert Dphysical==sum((dd[j]*lam**j for j in range(3)),R())
CD=dd[2]*K[2]+dd[1]*K[0]+dd[0]*h
Dtag=[dd[2]*recovery_tags[2][j]+dd[1]*recovery_tags[0][j] for j in range(5)]
original_return(h*Dphysical-CD,Dtag)
assert weight(CD.n)
say('new_b0_direct_entire_original_D_recovery_relation',
    literalIdentity='h*D-C_D = d2*H_lambda2+d1*H_lambda',
    CDNumerator=profile(CD.n),CDDenominator=profile(CD.d),
    CDIsIdenticallyZero=not bool(CD),
    wholePhysicalBzeroExcluded=bool(head_paid and not CD),
    allFiveOriginalSourceCoordinatesReturned=True,
    DOnlyUsedAsPositivePolynomialTarget=True,
    hZeroLocusNeverDeleted=True)
if head_paid and not CD:
 say('new_entire_b0_original_positive_D_unit_exclusion',
     originalRelation='h*D belongs to J5',hHasOnlyOldPaidWeightSupport=True,
     physicalDNonzeroIsTheOriginalBranchAssumption=True,
     noOldWeightProjectionReplayed=True,
     sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
 raise SystemExit(0)

def new_scalar(label,value,tag):
 original_return(value,tag);assert weight(R(value).n)
 den0=O
 for vv in tag:den0=exact(den0,den0.gcd(vv.d))*vv.d
 paid(den0)
 ns=[vv.n*exact(den0,vv.d) for vv in tag];gc=Z
 for pp in ns:gc=gc.gcd(pp)
 if not gc:
  assert not value
  say('new_b0_simultaneous_weight_scalar_zero',label=label,
      originalFiveEquationsRetained=True)
  return False
 newtag=[R(exact(pp,gc)) for pp in ns]
 raw=sum((newtag[j]*original5[j] for j in range(5)),R())
 assert R(gc)*raw==R(den0)*value and weight(raw.n)
 original_return(raw,newtag)
 core,removed,hist=strip(raw.n)
 if core:
  lc=core.coefficient(0);core/=lc;removed*=lc
 assert core*removed==raw.n
 if not core:
  say('new_b0_simultaneous_weight_scalar_zero',label=label,
      completeOriginalReturn=True)
  return False
 paid(removed)
 tagfinal=[R(raw.d,removed)*vv for vv in newtag]
 final=R(core)
 original_return(final,tagfinal)
 statistics['newPureWeightOriginalReturns']+=1
 unit=int(core.total_degree())==0
 say('new_b0_simultaneous_complete_original_pure_weight_scalar',
     label=label,necessaryPolynomial=profile(core),
     actualFiveMultiplierCommon=profile(gc),paidGcdLayers=hist,
     allFiveOriginalSourceCoefficientsReturned=True,
     commonZeroAndHeadZeroLociRetained=True,
     wholePhysicalBzeroExcluded=unit)
 return unit

unit_found=False
if not h:
 # Each H_j=-K_j is already a pure-weight original relation.
 for i in range(4):
  unit_found=new_scalar('identically_zero_head_K_'+str(i),-K[i],recovery_tags[i])
  if unit_found:break
else:
 # No division by h in any of these Veronese/qf compatibility identities.
 Klam,Kf,Klam2,Klamf=K
 s1=h*Klam2-Klam*Klam
 tag1=[(h*lam+Klam)*recovery_tags[0][j]-h*recovery_tags[2][j]
       for j in range(5)]
 assert s1==(h*lam+Klam)*H[0]-h*H[2]
 unit_found=new_scalar('lambda_square_compatibility',s1,tag1)
 if not unit_found:
  s2=h*Klamf-Klam*Kf
  tag2=[h*lam*recovery_tags[1][j]+Kf*recovery_tags[0][j]
         -h*recovery_tags[3][j] for j in range(5)]
  assert s2==h*lam*H[1]+Kf*H[0]-h*H[3]
  unit_found=new_scalar('lambda_f_compatibility',s2,tag2)
 if not unit_found:
  a1=lambda_coeff(q1,1);b1=lambda_coeff(q1,0)
  c2=lambda_coeff(q0,2);d1=lambda_coeff(q0,1);e0=lambda_coeff(q0,0)
  assert q1==a1*lam+b1 and q0==c2*lam*lam+d1*lam+e0
  sq=(Kf*Kf+(a1*Klam+b1*h)*Kf+c2*Klam*Klam+d1*h*Klam+e0*h*h)
  vf=h*f+Kf+a1*h*lam+b1*h
  vl=a1*Kf+c2*(h*lam+Klam)+d1*h
  tagq=[h*h*qtag[j]-vf*recovery_tags[1][j]-vl*recovery_tags[0][j]
        for j in range(5)]
  assert sq==h*h*qf-vf*H[1]-vl*H[0]
  unit_found=new_scalar('same_f_monic_quadratic_compatibility',sq,tagq)

say('new_b0_simultaneous_four_by_five_original_target_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 statistics=statistics,wholePhysicalBzeroExcluded=unit_found,
 sameHeadOpenChartHasUniqueLambdaAndF=bool(h),
 headIdenticallyZeroHasNoRecoveryChart=not bool(h),
 headZeroFiberKeepsAllOriginalFiveEquationsAndFourK=True,
 noNewPureUCoverFactorOrResultantComputed=True,
 noOldSixProjectionOrPRSGateReplayed=True,
 entireOriginalI11StillRetained=True,
 maxRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 noLargeCoefficientCacheWritten=True,ordinaryISPClaim=False)
signal.setitimer(signal.ITIMER_REAL,0)
