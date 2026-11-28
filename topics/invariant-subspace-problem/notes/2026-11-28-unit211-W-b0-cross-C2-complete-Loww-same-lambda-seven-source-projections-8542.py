#!/usr/bin/env python3
"""NEW entire W b0: original C2 and complete Loww at the SAME f/lambda.
Only true Gram/qf/ri and the ALREADY PUBLISHED pure-weight v definitions.
No former six pair/norm projections, 4-by-5 adjugate, pure-weight h/K,
primitive PRS, full I11, or whole NS/PS six-cofactor gate is replayed.
mu=B0 cross B1 yields C2=mu.A=mu.r without a cross/head inverse.
Complete Loww=NS-PS+EW2 is divided by monic qf, then uses the existing
entire f+g original identity. Each new condition returns SEVEN sources.
Only NEW fixed (2,4) Sylvester targets: q2/Loww, C2/Loww. All heads,
cross-zero and original five/I11 conditions remain. 180s/4GiB.
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
ctx=fmpq_mpoly_ctx.get(('u','nu','lam','T','f'),'lex')
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
u,nu,lam,T,f=map(R,(ep,kp,lp,tp,fp))
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
Pbar=(3*u-2)*nu*nu-(2*u*u+3*u-3)*nu+slope_unit*slope_unit
P02=2*u*e*Pbar/dweight
assert P02==(2-3*u)*V2-Q*u+2*u**3
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
  'degrees_u_nu_lambda_T_f':list(map(int,p.degrees())) if p else [-1]*5,
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

# Only the currently proved pure-weight W supports. Neither E1=EW,
# nor any new lambda,T,f head nor D is assumed.
paid_atoms=[
 ('original_u',ep),('original_e',ep-1),
 ('original_JQ_two_u_minus_one',2*ep-1),
 ('inverse_coordinate_d',dweight.n),('inverse_coordinate_r',rweight.n),
 ('original_equal_weights_k_plus_two_nu',kp),
 ('original_Phi_nu_minus_one',kp-1),
 ('original_delta',delta.n),('original_M',M.n),
 ('original_ell',ell.n),('original_m',m.n),('original_P02',P02.n),
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
for v in [u,nu,e,slope_unit,dweight,rweight,k,Q,Vbar,delta,ell,m,M,bc,Phi,P02,G36_pullback,t,V,W1,x,y,A1]:
 ck(v)
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

cf=bc/(2*u*(u-beta))
qtag=[R(),cf,cf*ell*delta/m,R()]
qf=sum((qtag[i]*original[i] for i in range(4)),R())
q0=fc(qf,0);q1=fc(qf,1)
assert qf==f*f+q1*f+q0
rowdata=[]
for j in (0,2,3):
 hh=fc(original[j],2)
 rr=original[j]-hh*qf
 aa=fc(rr,0);bb=fc(rr,1)
 assert rr==aa+bb*f and geomdegree(aa)<=2 and geomdegree(bb)<=1
 tt=[(R(1) if i==j else R())-hh*qtag[i] for i in range(4)]
 rowdata.append(dict(A=aa,B=bb,value=rr,tag=tt,originalIndex=j))
def P2(vv):
 vc=va(vv,vs(-tau(vv),one))
 return tau(vm(vm(vc,vc),vc))
A_lambda=2*lam*lam-2*lam+1
B_lambda=4*lam**3-6*lam*lam+3*lam-1
NB=N4(rows[2]);NC=N4(rows[3])
PB=P2(rows[2]);PC=P2(rows[3])
assert NC==NB.conj() and PC==PB.conj()
NSext=b*NB+c*NC-E(2*lam*P02*(ell+2*T+A_lambda))
PSext=b*PB+c*PC-E(P02*(ell+3*T+3*A_lambda+B_lambda))
assert not NSext.b and not PSext.b
NS=ck(NSext.a);PS=ck(PSext.a)
assert geomdegree(NS)<=3 and geomdegree(PS)<=3
assert geomdegree(NB.b)<=3 and geomdegree(PB.b)<=3
original6=original+[NS,PS]


# Necessary definition of the already-published global pure-weight
# v.B=1, f+g relation, before b0 specialization. No old head-factor,
# six pair/norm, or pure-I11 proof tail is executed.
Bmatrix=[]
for rr in rowdata:
 bb=rr['B'];co=[]
 for dl,dT in [(0,0),(1,0),(0,1)]:
  pp=ctx.from_dict({(int(ex[0]),int(ex[1]),0,0,0):cc
     for ex,cc in bb.n.to_dict().items()
     if int(ex[2])==dl and int(ex[3])==dT and int(ex[4])==0})
  co.append(R(pp,bb.d))
 assert bb==co[0]+co[1]*lam+co[2]*T
 Bmatrix.append(co)
mu_global=[Bmatrix[1][1]*Bmatrix[2][2]-Bmatrix[1][2]*Bmatrix[2][1],
 Bmatrix[2][1]*Bmatrix[0][2]-Bmatrix[2][2]*Bmatrix[0][1],
 Bmatrix[0][1]*Bmatrix[1][2]-Bmatrix[0][2]*Bmatrix[1][1]]
raw_global_head=sum((mu_global[i]*Bmatrix[i][0] for i in range(3)),R())
assert raw_global_head and weight(raw_global_head.n)
# No physical raw_head!=0 assumption: cancel each actual ratio, pay
# its FINAL denominator, then return the complete global source.
v_unit=[ck(mu_global[i]/raw_global_head) for i in range(3)]
assert all(weight(vv.n) and weight(vv.d) for vv in v_unit)
assert sum((v_unit[i]*rowdata[i]['B'] for i in range(3)),R())==1
g_global=sum((v_unit[i]*rowdata[i]['A'] for i in range(3)),R())
r_global_tag=[ck(sum((v_unit[i]*rowdata[i]['tag'][j]
                     for i in range(3)),R())) for j in range(4)]
assert sum((r_global_tag[j]*original[j] for j in range(4)),R())==f+g_global

# Necessary original b0 substitution. nu+2 is paid ONLY on this b0
# branch by A*=u*Q*(nu+2); it was not added to the whole-W map.
Astar=4*u*Q-J
assert Astar==u*Q*(nu+2)
paid_atoms.append(('b0_original_Astar_nu_plus_two',kp+2))
kappa=ck(ell/(nu+2));Tb=-kappa*(3-2*lam)
def on_b0(value):
 value=R(value);assert weight(value.d)
 degree=max((int(ex[3]) for ex in value.n.to_dict()),default=-1)
 out=R()
 for j in range(degree,-1,-1):
  coefficient=ctx.from_dict({(int(ex[0]),int(ex[1]),int(ex[2]),0,int(ex[4])):cc
       for ex,cc in value.n.to_dict().items() if int(ex[3])==j})
  out=out*Tb+R(coefficient)
 result=out/R(value.d)
 assert all(int(ex[3])==0 for ex in result.n.to_dict())
 return ck(result)
assert on_b0(T)==Tb and on_b0(T+Tb)==2*Tb
Db=ell*A_lambda-Tb*Tb
Cstar=Astar*m*m+J*delta*ell*ell
ad=M*ell*ell*Q*(3-4*lam)+M*Astar*Tb*Tb+2*M*u*Q*(3-2*lam)*ell*Tb+Db*Cstar
bzero=2*m*(Astar*Tb+u*Q*(3-2*lam)*ell)
assert not bzero
q2=ck(2*ad/ell)
qf_b=on_b0(qf);q0_b=on_b0(q0);q1_b=on_b0(q1)
assert qf_b==f*f+q1_b*f+q0_b
original7=[on_b0(rr) for rr in original]+[q2,on_b0(NS),on_b0(PS)]
source_names=['E1','EBe','EBo','N1','q2','NS','PS']
qtag7=qtag+[R(),R(),R()]
rline_tag7=r_global_tag+[R(),R(),R()]
gb=on_b0(g_global)
assert sum((rline_tag7[j]*original7[j] for j in range(7)),R())==f+gb
assert fdeg(gb)<=0 and geomdegree(gb)<=2
rows_b=[]
for rr in rowdata:
 row={key:on_b0(rr[key]) for key in ['A','B','value']}
 row['tag']=rr['tag']+[R(),R(),R()]
 assert row['value']==row['A']+row['B']*f
 assert sum((row['tag'][j]*original7[j] for j in range(7)),R())==row['value']
 rows_b.append(row)
def lamcoef(value,j):
 value=R(value);assert weight(value.d)
 assert all(int(ex[3])==0 and int(ex[4])==0 for ex in value.n.to_dict())
 return R(ctx.from_dict({(int(ex[0]),int(ex[1]),0,0,0):cc
          for ex,cc in value.n.to_dict().items() if int(ex[2])==j}),value.d)
def lamdegree(value):
 value=R(value);assert weight(value.d)
 assert all(int(ex[3])==0 and int(ex[4])==0 for ex in value.n.to_dict())
 return max((int(ex[2]) for ex in value.n.to_dict()),default=-1)
B0=[lamcoef(row['B'],0) for row in rows_b]
B1=[lamcoef(row['B'],1) for row in rows_b]
assert all(rows_b[i]['B']==B0[i]+lam*B1[i] for i in range(3))
assert sum((v_unit[i]*B0[i] for i in range(3)),R())==1
assert not sum((v_unit[i]*B1[i] for i in range(3)),R())

statistics.update(newOriginalSevenSourceReturns=0,newOriginalFCoefficientReturns=0,
 newActualSevenMultiplierCancellations=0,newLowwMonicDivisionProducts=0,
 newFixedSylvesterExactProducts=0,newFixedSylvesterCoordinates=0)
def original_return(value,tag):
 value=R(value);assert len(tag)==7
 back=sum((tag[j]*original7[j] for j in range(7)),R())
 assert back==value
 for j in range(max(0,fdeg(value),fdeg(back))+1):
  assert fc(value,j)==fc(back,j)
  statistics['newOriginalFCoefficientReturns']+=1
 for vv in [value]+tag:ck(vv)
 statistics['newOriginalSevenSourceReturns']+=1
def primitive_original(label,value,tag,bound):
 value=R(value);tag=[R(vv) for vv in tag]
 original_return(value,tag)
 den=O
 for vv in tag:den=exact(den,den.gcd(vv.d))*vv.d
 paid(den)
 nums=[vv.n*exact(den,vv.d) for vv in tag]
 common=Z
 for pp in nums:common=common.gcd(pp)
 if not common:
  assert not value
  say('new_b0_C2_Loww_original_condition_zero',label=label,
      allOriginalConditionsAndZeroFibersRetained=True)
  return R(),[R() for _ in range(7)]
 primitive=[R(exact(pp,common)) for pp in nums]
 newvalue=sum((primitive[j]*original7[j] for j in range(7)),R())
 assert R(common)*newvalue==R(den)*value
 original_return(newvalue,primitive)
 assert lamdegree(newvalue)<=bound
 core,removed,hist=strip(newvalue.n)
 if core:
  cscale=core.coefficient(0);core/=cscale;removed*=cscale
 assert core*removed==newvalue.n
 if not core:
  assert not newvalue
  return R(),primitive
 paid(removed)
 final=[R(newvalue.d,removed)*vv for vv in primitive]
 out=R(core);original_return(out,final)
 statistics['newActualSevenMultiplierCancellations']+=1
 say('new_b0_C2_Loww_complete_original_condition',label=label,
     necessaryNumerator=profile(core),actualLambdaDegree=lamdegree(out),
     actualSevenMultiplierCommon=profile(common),onlyOldPaidRemoval=hist,
     allSevenSourceAndAllFCoefficientReturns=True,
     noUnpaidCommonOrHeadInverse=True,
     sourceMultiplierNumerators=[profile(vv.n) for vv in final],
     sourceMultiplierDenominators=[profile(vv.d) for vv in final])
 return out,final

# NEW C2: constant cross annihilates BOTH f columns, with no cross inverse.
mu=[B0[1]*B1[2]-B0[2]*B1[1],
    B0[2]*B1[0]-B0[0]*B1[2],
    B0[0]*B1[1]-B0[1]*B1[0]]
assert not sum((mu[i]*B0[i] for i in range(3)),R())
assert not sum((mu[i]*B1[i] for i in range(3)),R())
Craw=sum((mu[i]*rows_b[i]['A'] for i in range(3)),R())
Ctag=[sum((mu[i]*rows_b[i]['tag'][j] for i in range(3)),R()) for j in range(7)]
assert Craw==sum((mu[i]*rows_b[i]['value'] for i in range(3)),R())
C2,C2tag=primitive_original('pure_lambda_C2_cross',Craw,Ctag,2)

# NEW complete Loww, with its explicit SIX raw original N/P/mean source.
# First check the whole free-T identity; then specialize the SAME point.
EW2=b*(2*p-E(u)-X)*EB+c*(2*q-E(u)-Y)*EC
assert not EW2.b
ewbe=2*u-u*ell-V
ewbo=2*theta-u*m-m*x-ell*delta*y
assert EW2.a==ewbe*original[1]+ewbo*original[2]
Kw=2*(t*t+(5*u-4*x-2)*t+2*(x*x-delta*y*y)
      +4*x+4*delta*y-4*u*x+2*u*u-6*u+Q)
Loww=2*P02*(2*lam-1)*w-bc*t*(Kw+4*(f-u)*(t-2))
assert Loww==NS-PS+EW2.a
low=on_b0(Loww)
lowtag=[R(),on_b0(ewbe),on_b0(ewbo),R(),R(),R(1),R(-1)]
original_return(low,lowtag)
quot=R();rem=low
while fdeg(rem)>=2:
 degree=fdeg(rem);term=fc(rem,degree)*f**(degree-2)
 before=rem;rem=rem-term*qf_b;quot+=term
 assert before==term*qf_b+rem and fdeg(rem)<degree
 statistics['newLowwMonicDivisionProducts']+=1
al=fc(rem,0);bl=fc(rem,1)
assert low==quot*qf_b+al+bl*f
pure_low=al-bl*gb
pure_low_tag=[lowtag[j]-quot*qtag7[j]-bl*rline_tag7[j] for j in range(7)]
assert lamdegree(pure_low)<=4
PL,PLtag=primitive_original('complete_Loww_at_same_f',pure_low,pure_low_tag,4)
say('new_b0_C2_and_true_Loww_same_lambda_interface',
    q2Numerator=profile(q2.n),C2Numerator=profile(C2.n),
    pureLowwNumerator=profile(PL.n),
    literalLowwIdentity='Loww=NS-PS+EW2',
    trueFreeFCorrection='Kw+4*(f-u)*(t-2)',
    pureWeightVdotB0OneAndVdotB1Zero=True,
    crossZeroAndAllQ2LeadingZeroFibersRetained=True,
    no1898AdjugateOrOldSixProjectionOrPRSReplayed=True,
    originalI11StillRetained=True)

# Only NEW fixed 2+4 matrices involving the newly constructed Loww.
def fixed_sylvester(leftpoly,rightpoly):
 lc=[lamcoef(R(leftpoly),j).n for j in range(3)]
 rc=[lamcoef(R(rightpoly),j).n for j in range(5)]
 assert lamdegree(R(leftpoly))<=2 and lamdegree(R(rightpoly))<=4
 matrix=[]
 for co,shifts in [(lc,4),(rc,2)]:
  for shift in range(shifts):
   matrix.append([co[j-shift] if 0<=j-shift<len(co) else Z for j in range(6)])
 work=[row[:] for row in matrix]
 trans=[[O if i==j else Z for j in range(6)] for i in range(6)]
 previous=O
 for pivotcol in range(6):
  pivotrow=next((ii for ii in range(pivotcol,6) if work[ii][pivotcol]),None)
  if pivotrow is None:return Z,[Z]*6,matrix
  if pivotrow!=pivotcol:
   work[pivotcol],work[pivotrow]=work[pivotrow],work[pivotcol]
   trans[pivotcol],trans[pivotrow]=trans[pivotrow],trans[pivotcol]
  pivot=work[pivotcol][pivotcol]
  for ii in range(6):
   if ii==pivotcol:continue
   oldrow=work[ii][:];oldtrace=trans[ii][:]
   entry=oldrow[pivotcol]
   for jj in range(6):
    if jj!=pivotcol:
     work[ii][jj]=exact(pivot*oldrow[jj]-entry*work[pivotcol][jj],previous)
     statistics['newFixedSylvesterExactProducts']+=1
    trans[ii][jj]=exact(pivot*oldtrace[jj]-entry*trans[pivotcol][jj],previous)
    statistics['newFixedSylvesterExactProducts']+=1
   work[ii][pivotcol]=Z
  previous=pivot
 scalar=work[0][0]
 for ii in range(6):
  for jj in range(6):
   assert work[ii][jj]==(scalar if ii==jj else Z)
   assert sum((trans[ii][kk]*matrix[kk][jj] for kk in range(6)),Z)==work[ii][jj]
   statistics['newFixedSylvesterCoordinates']+=1
 return scalar,trans[0],matrix
def finish(closed=False):
 say('new_b0_C2_Loww_fixed_original_input_finished',
     sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     statistics=statistics,wholePhysicalBzeroExcluded=closed,
     maxRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
     crossZero_q2HeadZero_globalHeadZero_AllRetained=True,
     onlyNewLowwContainingTargets=True,noOldSixProjectionPRSOr1898AdjugateReplayed=True,
     noNewWeightFiberBoundWithoutActualProof=True,
     noLargeCoefficientCacheWritten=True,ordinaryISPClaim=False)
 signal.setitimer(signal.ITIMER_REAL,0)
for label,value in [('C2',C2),('pure_Loww',PL)]:
 if value and int(value.n.total_degree())==0:
  say('new_b0_original_constant_from_new_input',label=label,
      actualRationalConstant=str(value.n),wholePhysicalBzeroExcluded=True)
  finish(True);raise SystemExit(0)
if not PL or lamdegree(PL)==0:
 say('new_b0_Loww_fixed_projection_not_needed',
     pureWeightNecessaryCondition=profile(PL.n),
     pureLowwIsZero=not bool(PL),allOriginalConditionsRetained=True)
 finish();raise SystemExit(0)
new_weight=[]
for label,left,lefttag in [
 ('q2_with_complete_Loww',q2,[R(),R(),R(),R(),R(1),R(),R()]),
 ('C2_with_complete_Loww',C2,C2tag)]:
 if not left:
  say('new_b0_fixed_Loww_projection_zero_left',label=label,
      crossZeroAndOriginalConditionsRetained=True)
  continue
 if lamdegree(left)==0:
  say('new_b0_left_already_pure_weight',label=label,numerator=profile(left.n),
      allOriginalConditionsRetained=True)
  continue
 scalar,cofactor,matrix=fixed_sylvester(left.n,PL.n)
 if not scalar:
  say('new_b0_fixed_Loww_projection_zero',label=label,fixedSize=6,
      allLeadingZeroAndOriginalConditionsRetained=True,noEmptyConclusion=True)
  continue
 leftmult=sum((cofactor[j]*lp**j for j in range(4)),Z)
 lowmult=cofactor[4]+cofactor[5]*lp
 assert scalar==leftmult*left.n+lowmult*PL.n
 tag=[R(leftmult)*R(left.d)*lefttag[j]+R(lowmult)*PLtag[j] for j in range(7)]
 core,ctag=primitive_original(label+'_pure_weight',R(scalar),tag,0)
 if not core:continue
 assert weight(core.n)
 new_weight.append(dict(label=label,profile=profile(core.n)))
 say('new_b0_Loww_fixed_pure_weight_original_return',
     label=label,fixedLambdaCapacity=[2,4],fixedSize=6,
     necessaryWeightPolynomial=profile(core.n),
     allSevenRawSourceCoefficientsReturned=True,
     completeCrossAndHeadZeroLociRetained=True,
     noTemporaryPivotOrNewContentUnitAssumed=True)
 if int(core.n.total_degree())==0:
  finish(True);raise SystemExit(0)
say('new_b0_Loww_new_weight_conditions_finished',conditions=new_weight,
    noQQFactorOrGcdOrPureUCoverGateRun=True,
    originalC2q2AndAllSevenEquationsStillRetained=True)
finish()
