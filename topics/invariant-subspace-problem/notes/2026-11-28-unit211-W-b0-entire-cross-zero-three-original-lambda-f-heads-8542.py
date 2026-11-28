#!/usr/bin/env python3
"""NEW current W b0: entire CROSS-ZERO pure-weight coefficient support.
Only necessary TRUE four means/qf/three ri definitions, then same b0 T.
B_i(λ)=B_i0+λ B_i1; cross(B0,B1)=0 iff all THREE B_i1=0 by the
published pure-weight v.B0=1,v.B1=0. This is ONLY the cross-zero branch.
NEW targets: old-paid normalization of the three actual pure-weight B_i1;
at most three fixed nu-Sylvester identities and a true QQ[u] Bezout.
Every returned cover has complete THREE coefficient-source multipliers.
No C2/Loww, NSPS, 4x5 adjugate, old six projections or PRS is regenerated.
Unpaid u fibers remain; only a real full unit return closes cross-zero.
120s/1GiB, self-contained. No sampling, coefficient payload or cache.
"""
import hashlib,json,resource,signal,time
from pathlib import Path
from flint import fmpq_mpoly_ctx,fmpq_poly
START=time.perf_counter()
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
signal.setitimer(signal.ITIMER_REAL,120)
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

# Only the b0 original Astar unit is added; no bare global head inverse.
Astar=4*u*Q-J
assert Astar==u*Q*(nu+2)
paid_atoms.append(('b0_original_Astar_nu_plus_two',kp+2))
kappa=ck(ell/(nu+2));Tb=-kappa*(3-2*lam)
def on_b0(value):
 value=R(value);assert weight(value.d)
 degree=max((int(ex[3]) for ex in value.n.to_dict()),default=-1)
 out=R()
 for j in range(degree,-1,-1):
  pp=ctx.from_dict({(int(ex[0]),int(ex[1]),int(ex[2]),0,int(ex[4])):cc
      for ex,cc in value.n.to_dict().items() if int(ex[3])==j})
  out=out*Tb+R(pp)
 return ck(out/R(value.d))
original_b=[on_b0(vv) for vv in original]
qf_b=on_b0(qf)
assert qf_b==f*f+on_b0(q1)*f+on_b0(q0)
B0=[];B1=[]
statistics.update(newWholeOriginalRemainderCoordinates=0,
                  newCoefficientSourceReturns=0,newNuSylvesterProducts=0,
                  newNuSylvesterCoordinates=0,newQQofUBezoutProducts=0)
for rr in rowdata:
 av=on_b0(rr['A']);bv=on_b0(rr['B']);value=on_b0(rr['value'])
 assert value==av+bv*f
 assert value==sum((rr['tag'][j]*original_b[j] for j in range(4)),R())
 for j in range(max(0,fdeg(value))+1):
  assert fc(value,j)==fc(av+bv*f,j)
  statistics['newWholeOriginalRemainderCoordinates']+=1
 co=[]
 for j in (0,1):
  pp=ctx.from_dict({(int(ex[0]),int(ex[1]),0,0,0):cc
       for ex,cc in bv.n.to_dict().items()
       if int(ex[2])==j and int(ex[3])==0 and int(ex[4])==0})
  co.append(ck(R(pp,bv.d)))
 assert bv==co[0]+co[1]*lam
 assert all(weight(vv.n) and weight(vv.d) for vv in co)
 B0.append(co[0]);B1.append(co[1])
def source_return(value,tag):
 value=R(value);assert len(tag)==3 and weight(value.n) and weight(value.d)
 assert sum((tag[i]*B1[i] for i in range(3)),R())==value
 for vv in [value]+list(tag):ck(vv)
 statistics['newCoefficientSourceReturns']+=1
def pure_u(p):
 return all(all(int(ex[j])==0 for j in (1,2,3,4)) for ex in p.to_dict())
def nu_degree(p):
 assert weight(p)
 return max((int(ex[1]) for ex in p.to_dict()),default=-1)
def to_u(p):
 assert pure_u(p)
 coefficients=p.to_dict();degree=max((int(ex[0]) for ex in coefficients),default=-1)
 return fmpq_poly([coefficients.get((j,0,0,0,0),0) for j in range(degree+1)])
def from_u(p):
 return ctx.from_dict({(j,0,0,0,0):p[j] for j in range(p.degree()+1) if p[j]})
def u_r(v):return R(from_u(v))
def nu_coefficient(p,j):
 assert weight(p)
 return to_u(ctx.from_dict({(int(ex[0]),0,0,0,0):cc
       for ex,cc in p.to_dict().items() if int(ex[1])==j}))
def old_paid_normalize(value,tag):
 value=R(value);source_return(value,tag)
 assert weight(value.n) and weight(value.d)
 core,removed,hist=strip(value.n)
 if core:
  cscale=core.coefficient(0);core/=cscale;removed*=cscale
 assert core*removed==value.n
 if not core:return Z,[R(),R(),R()],hist
 paid(removed)
 outtag=[R(value.d,removed)*vv for vv in tag]
 source_return(R(core),outtag)
 return core,outtag,hist
def finish(closed=False,unit_tag=None):
 if closed:
  assert unit_tag is not None
  source_return(R(1),unit_tag)
 say('new_b0_entire_cross_zero_coefficient_support_finished',
     sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     statistics=statistics,wholeCrossZeroBranchExcluded=closed,
     wholeBzeroOrWholeWExcluded=False,
     noCoefficientHeadOrNewPureUInverse=True,
     everyUnpaidZeroFiberRetained=True,
     originalI11AndAllNonCrossZeroChartsRetained=True,
     noOldC2LowwAdjugateProjectionOrPRSReplayed=True,
     maxRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
     noLargeCoefficientPayloadOrCacheWritten=True,ordinaryISPClaim=False)
 signal.setitimer(signal.ITIMER_REAL,0)
say('new_b0_three_lambda_f_heads_original_definitions',
    originalB0Numerators=[profile(vv.n) for vv in B0],
    originalB0Denominators=[profile(vv.d) for vv in B0],
    originalB1Numerators=[profile(vv.n) for vv in B1],
    originalB1Denominators=[profile(vv.d) for vv in B1],
    threeRemaindersWholeOriginalFourSourceReturned=True,
    branch='B11=B21=B31=0 iff cross(B0,B1)=0 by published v',
    noC2OrLowwOrOldGHeadRegenerated=True)
polys=[];tags=[]
for i,vv in enumerate(B1):
 pp,tt,hist=old_paid_normalize(vv,[R(int(j==i)) for j in range(3)])
 polys.append(pp);tags.append(tt)
 say('new_b0_lambda_f_head_old_paid_normalization',
     index=i,necessaryNumerator=profile(pp),onlyOldPaidGcdLayers=hist,
     completeOriginalCoefficientSourceReturned=True,
     branchOnlyCrossZero=True)
 if pp and int(pp.total_degree())==0:
  assert pp==O
  say('new_b0_cross_zero_direct_original_unit',
      chosenHead=i,unitMultipliersNumerators=[profile(xx.n) for xx in tt],
      unitMultipliersDenominators=[profile(xx.d) for xx in tt],
      exactIdentity='sum(w_i B_i1)=1',
      wholeCrossZeroExcluded=True,wholeBzeroExcluded=False)
  finish(True,tt);raise SystemExit(0)

# NEW fixed univariate-in-nu polynomial matrices over QQ[u].
# The fixed symbolic degrees are recorded before any u specialization.
def exact_u(a,b):
 q,r=divmod(a,b);assert not r and q*b==a
 statistics['newNuSylvesterProducts']+=1
 return q
def fixed_nu_original(left,right):
 ml=nu_degree(left);nr=nu_degree(right)
 assert ml>0 and nr>0
 size=ml+nr;zero=fmpq_poly([]);onep=fmpq_poly([1])
 lc=[nu_coefficient(left,j) for j in range(ml+1)]
 rc=[nu_coefficient(right,j) for j in range(nr+1)]
 matrix=[]
 for co,shifts in [(lc,nr),(rc,ml)]:
  for shift in range(shifts):
   matrix.append([co[j-shift] if 0<=j-shift<len(co) else zero for j in range(size)])
 work=[row[:] for row in matrix]
 trans=[[onep if i==j else zero for j in range(size)] for i in range(size)]
 previous=onep
 for kk in range(size):
  pivotrow=next((ii for ii in range(kk,size) if work[ii][kk]),None)
  if pivotrow is None:return zero,[zero for _ in range(size)],ml,nr
  if pivotrow!=kk:
   work[kk],work[pivotrow]=work[pivotrow],work[kk]
   trans[kk],trans[pivotrow]=trans[pivotrow],trans[kk]
  pivot=work[kk][kk]
  for ii in range(size):
   if ii==kk:continue
   oldrow=work[ii][:];oldtrace=trans[ii][:]
   entry=oldrow[kk]
   for jj in range(size):
    if jj!=kk:work[ii][jj]=exact_u(pivot*oldrow[jj]-entry*work[kk][jj],previous)
    trans[ii][jj]=exact_u(pivot*oldtrace[jj]-entry*trans[kk][jj],previous)
   work[ii][kk]=zero
  previous=pivot
 scalar=work[0][0]
 for ii in range(size):
  for jj in range(size):
   assert work[ii][jj]==(scalar if ii==jj else zero)
   assert sum((trans[ii][kk]*matrix[kk][jj] for kk in range(size)),zero)==work[ii][jj]
   statistics['newNuSylvesterCoordinates']+=1
 return scalar,trans[0],ml,nr
cover=fmpq_poly([]);cover_tag=[R(),R(),R()]
def add_cover(label,polynomial,tag):
 global cover,cover_tag
 assert pure_u(polynomial)
 source_return(R(polynomial),tag)
 core,tt,hist=old_paid_normalize(R(polynomial),tag)
 if not core:return False
 cp=to_u(core)
 if not cover:
  cover=cp;cover_tag=tt
 else:
  old=cover
  gg,ss,ttt=old.xgcd(cp)
  assert ss*old+ttt*cp==gg
  statistics['newQQofUBezoutProducts']+=1
  cover_tag=[u_r(ss)*cover_tag[j]+u_r(ttt)*tt[j] for j in range(3)]
  cover=gg
 source_return(u_r(cover),cover_tag)
 say('new_b0_cross_zero_complete_u_cover_step',
     label=label,newOriginalPureUProjection=profile(core),
     onlyOldPaidGcdLayers=hist,cover=profile(from_u(cover)),
     completeThreeOriginalCoefficientSourceReturned=True,
     allNuLeadingZeroFibersRetained=True)
 if cover.degree()==0:
  cst=cover[0];cover_tag=[vv/R(cst) for vv in cover_tag]
  source_return(R(1),cover_tag)
  say('new_b0_cross_zero_true_three_head_Bezout_unit',
      unitMultipliersNumerators=[profile(xx.n) for xx in cover_tag],
      unitMultipliersDenominators=[profile(xx.d) for xx in cover_tag],
      exactIdentity='sum(w_i B_i1)=1',
      onlyOldPureWeightDenominators=True,
      wholeCrossZeroExcluded=True,wholeBzeroExcluded=False)
  finish(True,cover_tag);return True
 return False
# A genuine pure-u original head is already an exact projection.
for i,pp in enumerate(polys):
 if pp and nu_degree(pp)==0:
  if add_cover('direct_pure_u_head_'+str(i),pp,tags[i]):raise SystemExit(0)
for i,j in [(0,1),(0,2),(1,2)]:
 if not polys[i] or not polys[j] or nu_degree(polys[i])<=0 or nu_degree(polys[j])<=0:
  continue
 determinant,cofactor,ml,nr=fixed_nu_original(polys[i],polys[j])
 if not determinant:
  say('new_b0_cross_zero_fixed_nu_projection_zero',pair=[i,j],
      fixedNuDegrees=[ml,nr],allOriginalWeightComponentsRetained=True)
  continue
 lm=sum((u_r(cofactor[h])*nu**h for h in range(nr)),R())
 rm=sum((u_r(cofactor[nr+h])*nu**h for h in range(ml)),R())
 result=u_r(determinant)
 assert result==lm*R(polys[i])+rm*R(polys[j])
 tag=[lm*tags[i][h]+rm*tags[j][h] for h in range(3)]
 source_return(result,tag)
 if add_cover('heads_'+str(i)+'_'+str(j),result.n,tag):raise SystemExit(0)
if cover:
 assert cover.degree()>0
 say('new_b0_cross_zero_remaining_complete_u_cover',
     exactClaim='cover(u) belongs to the three pure-weight B_i1 coefficients',
     cover=profile(from_u(cover)),allRemainingUFieldsRetained=True,
     wholeCrossZeroExcluded=False)
 unit,factors=cover.factor();product=fmpq_poly([unit]);factor_profiles=[]
 for ff,mm in factors:
  product*=ff**int(mm)
  factor_profiles.append({'factor':profile(from_u(ff)),'multiplicity':int(mm)})
 assert product==cover
 say('new_b0_cross_zero_u_cover_QQ_factors',
     factors=factor_profiles,wholeFactorProductReturned=True,
     noAdditionalExclusion=True)
else:
 say('new_b0_cross_zero_no_nonzero_u_projection_returned',
     allThreeOriginalHeadsAndEntireCrossZeroBranchRetained=True,
     noMultivariateGcdOneEmptinessInference=True)
finish()
