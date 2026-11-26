#!/usr/bin/env python3
"""Original L0 with b+c!=0, after the complete zero-weight-sum theorem.
Use p+q=2 and the entire kappa^2=1-pq algebra in three rational parameters.
All original nine conditions and all P1 leading-zero fibers are retained.
NEW complete original L0 K curve, including both beta-leading charts.
The whole P1 double-zero chart has been closed, so its t coefficient is paid.
"""
import hashlib,json,resource,signal,time,os
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx,fmpq_poly
started=time.perf_counter()
def say(stage,**kw):
 print(json.dumps(dict(stage=stage,elapsedSeconds=round(time.perf_counter()-started,6),**kw),sort_keys=True),flush=True)
def alarm(signum,frame):
 say("timeout_unknown",claimExcluded=False);raise SystemExit(124)
signal.signal(signal.SIGALRM,alarm);signal.alarm(300)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
ctx=fmpq_mpoly_ctx.get(("rho","lam","w"),"lex")
rp,lp,wp=ctx.gens();zz=ctx.constant(0);oo=ctx.constant(1)
def poly(v):return v if hasattr(v,"to_dict") else ctx.constant(v)
class R:
 def __init__(self,n=0,d=None,reduce=True):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  n=poly(n);d=oo if d is None else poly(d)
  assert d
  if not n:self.n=zz;self.d=oo;return
  if reduce:
   g=n.gcd(d);n=n/g;d=d/g
  lc=d.coefficient(0);self.n=n/lc;self.d=d/lc
 def __bool__(self):return bool(self.n)
 def __add__(self,o):
  o=R(o)
  if not self:return o
  if not o:return self
  g=self.d.gcd(o.d);a=self.d/g;b=o.d/g
  return R(self.n*b+o.n*a,a*o.d)
 __radd__=__add__
 def __neg__(self):return R(-self.n,self.d,False)
 def __sub__(self,o):return self+-R(o)
 def __rsub__(self,o):return R(o)+-self
 def __mul__(self,o):
  o=R(o)
  if not self or not o:return R()
  g=self.n.gcd(o.d);h=o.n.gcd(self.d)
  return R((self.n/g)*(o.n/h),(self.d/h)*(o.d/g),False)
 __rmul__=__mul__
 def __truediv__(self,o):
  o=R(o);assert o
  return self*R(o.d,o.n,False)
 def __rtruediv__(self,o):return R(o)/self
 def __pow__(self,n):
  if n<0:assert self;return R(self.d**(-n),self.n**(-n),False)
  return R(self.n**n,self.d**n,False)
 def __eq__(self,o):
  o=R(o);return self.n*o.d==o.n*self.d

rho=R(rp);lam=R(lp);w=R(wp)
A=2*lam*lam-2*lam+1;BB=4*lam**3-6*lam*lam+3*lam-1
RR=lam-1-w;Cmom=RR*BB-A*A
u=RR/rho;V2=A/(rho*rho)
Q=(2*A*rho-BB)/(rho*rho*RR);Delta=1-Q
l=(2*u-V2)/Q;T=RR
bc=(l*l*Delta-(u-l)**2)/(4*Delta)
P02=(2-3*u)*V2-Q*u+2*u**3;P0=P02/2
T0=V2-2*u*u
fsol=-(u*(w/2-w*w)+rho*T0/4+lam*rho*rho*P0)/(w*(w-1))
assert Cmom==4*rho**4*bc*Q*Delta
assert P02==(BB-3*RR*A+2*RR**3)/(rho**3)
# l!=0 is paid by the complete L0,b+c=0 theorem, not by a generic assumption.
# A may be zero on this complement and is never inverted.
units=[rp,lp,wp,wp-1,RR.n,Cmom.n,Delta.n,Q.n,P0.n,(u-1).n,l.n]
def strip_units(po):
 po=poly(po)
 for atom in units:
  assert atom
  while po:
   gg=po.gcd(atom)
   if int(gg.total_degree())==0:break
   old=po;po=po/gg;assert po*gg==old
 return po
denominators=set()
def paid(rr):
 dd=R(rr).d;key=str(dd)
 if key not in denominators:
  assert int(strip_units(dd).total_degree())==0
  denominators.add(key)
def profile(po):
 return dict(degrees=list(map(int,po.degrees())) if po else [-1,-1],terms=len(po.to_dict()),sha256=hashlib.sha256(str(po).encode()).hexdigest())
for val in [A,BB,RR,rho,u,V2,Q,Delta,bc,P02,fsol]:paid(val)
class E:
 def __init__(self,a=0,b=0):
  if isinstance(a,E):self.a=a.a;self.b=a.b;return
  self.a=R(a);self.b=R(b)
 def __bool__(self):return bool(self.a) or bool(self.b)
 def __add__(self,o):o=E(o);return E(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return E(-self.a,-self.b)
 def __sub__(self,o):return self+-E(o)
 def __rsub__(self,o):return E(o)+-self
 def __mul__(self,o):
  o=E(o);return E(self.a*o.a+Delta*self.b*o.b,self.a*o.b+self.b*o.a)
 __rmul__=__mul__
 def __pow__(self,n):
  assert n>=0
  out=E(1);v=self
  while n:
   if n&1:out=out*v
   v=v*v;n//=2
  return out
 def __eq__(self,o):o=E(o);return self.a==o.a and self.b==o.b
 def conj(self):return E(self.a,-self.b)

b=E(l/2,(u-l)/(2*Delta));c=b.conj();a=E(1-l)
p=E(1,1);q=p.conj()
h=E(1+rho,rho);k=h.conj()
assert b+c==E(l) and b*c==E(bc) and p*q==E(Q)
assert b*p+c*q==E(u) and b*p*p+c*q*q==E(V2)
assert b*p**3+c*q**3==E(2*V2-Q*u)
assert a+E(w)+b*h+c*k==E(lam)
assert a+E(2*w)+b*h*h+c*k*k==E(2*lam*lam)
assert a+E(3*w)+b*h**3+c*k**3==E(4*lam**3)
assert q*(h-1)-p*(k-1)==0
ivdiff=E(0,-1/(2*Delta))
ivbp=c*q*ivdiff*E(1/(bc*Q));ivcq=b*p*ivdiff*E(1/(bc*Q))
assert ivbp*b*p*(q-p)==1 and ivcq*c*q*(q-p)==1
for val in [b,c,p,q,h,k,ivdiff,ivbp,ivcq]:paid(val.a);paid(val.b)
sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
say("complete_original_L0_symmetric_nonzero_l_two_parameter_graph",sourceSha256=sha,retainedQuadraticRoots=2,paid_l_reason="complete original L0 zero-weight-sum theorem; A is retained including zero",claimExcluded=False)
class P:
 def __init__(self,co=None):self.co={ij:E(v) for ij,v in (co or {}).items() if E(v)}
 def __bool__(self):return bool(self.co)
 def __add__(self,o):
  if not isinstance(o,P):o=cp(o)
  dd=dict(self.co)
  for ij,v in o.co.items():dd[ij]=dd.get(ij,E())+v
  return P(dd)
 __radd__=__add__
 def __neg__(self):return P({ij:-v for ij,v in self.co.items()})
 def __sub__(self,o):return self+-o
 def __rsub__(self,o):return cp(o)+-self
 def __mul__(self,o):
  if not isinstance(o,P):return scale(E(o),self)
  dd={}
  for ij,v in self.co.items():
   for kl,vv in o.co.items():
    key=(ij[0]+kl[0],ij[1]+kl[1]);dd[key]=dd.get(key,E())+v*vv
  return P(dd)
 __rmul__=__mul__
 def __pow__(self,n):
  out=cp(1)
  for _ in range(n):out=out*self
  return out
 def conj(self):return P({ij:v.conj() for ij,v in self.co.items()})
def cp(v):return P({(0,0):E(v)})
def scale(v,pp):return P({ij:E(v)*vv for ij,vv in pp.co.items()})
fp=cp(fsol);tp=P({(0,1):E(1)});zero=P()
one=[cp(1),zero,cp(1),cp(1)]
def va(v,z0):return [x+y for x,y in zip(v,z0)]
def vs(v0,v):return [v0*x for x in v]
def vm(v,z0):return [v[0]*z0[0],v[0]*z0[1]+v[1]*z0[0],v[2]*z0[2],v[3]*z0[3]]
def tau(v):return scale(a,v[0])+v[1]+scale(b,v[2])+scale(c,v[3])
T0=V2-2*u*u
W1=cp(T0/2)+scale(E(2*u),fp)
W2=cp(u*T0+lam*P02)+scale(E(V2+2*u*u),fp)-scale(E(bc*Q),tp)
XX=scale(ivbp,scale(q,W1)-W2);YY=scale(ivcq,W2-scale(p,W1))
r=XX-cp(a*p)-scale(c,tp);ss=YY-cp(a*q)-scale(b,tp)
Arow=scale(E(2),fp)-scale(2*b,XX)-scale(2*c,YY)+scale(E(2*bc),tp)
assert not (r.conj()-ss) and not (Arow.conj()-Arow)
rows=[[zero,zero,cp(p),cp(q)],[zero,Arow,r,ss],[cp(p),r,zero,tp],[cp(q),ss,tp,zero]]
def DK(v):return [tau(vm(row,v)) for row in rows]
d=DK(one);F2=tau(d);DKd=DK(d);dd=vm(d,d)
assert not (F2-scale(E(2),fp))
def P2(v):
 cen=va(v,vs(-tau(v),one))
 return tau(vm(vm(cen,cen),cen))
def N4(v):
 return scale(E(2),tau(vm(d,vm(v,v))))-F2*tau(vm(v,v))-scale(E(4),tau(v)*tau(vm(d,v)))+scale(E(2),F2*tau(v)**2)+tau(vm(v,DK(v)))
def Pjet2(v,z0):
 v0=va(v,vs(-tau(v),one));z1=va(z0,vs(-tau(z0),one))
 return scale(E(3),tau(vm(vm(v0,v0),z1)))
def Njet4(v,z0):return N4(va(v,z0))-N4(v)-N4(z0)
def mean(jj):
 ev=scale(E(2),tau(vm(rows[0],rows[1]))) if jj==1 else tau(vm(rows[jj],rows[jj]))
 return ev-scale(E(2),DKd[jj])-scale(E(2),dd[jj])+scale(E(2),F2*d[jj])
assert not mean(0) and not (P2(rows[0])-cp(P02)) and not (N4(rows[0])-cp(2*lam*P02))

VV=[cp(1),cp(w),cp(h),cp(k)]
assert not P2(VV) and not N4(VV)
raw=[mean(1),mean(2),Pjet2(rows[0],rows[1])-cp(3*w*P02),P2(rows[2])-cp(h**3*E(P02)),Njet4(rows[0],rows[1])-cp(4*lam*w*P02),N4(rows[2])-cp(h*h*E(2*lam*P02))]
assert not (mean(3)-raw[1].conj())
Lf=T0*(l-1+2*u*(1-u)/Q);Lt=bc*(T0+4*u-4+Q)
Lc=(1-u)*T0*T0/Q+P02*(l+T-lam*T0/Q)
assert not (raw[2]-scale(E(3),scale(E(Lf),fp)+scale(E(Lt),tp)+cp(Lc)))
def parts(pp,part):
 dd={}
 for ij,v in pp.co.items():
  assert ij[0]==0
  rr=v.a if part==0 else v.b
  if rr:dd[ij[1]]=rr
 return dd
for jj in [0,2,4]:assert not parts(raw[jj],1)
names=["E1","EBe","EBo","P1","PBe","PBo","N1","NBe","NBo"]
base=[parts(raw[0],0),parts(raw[1],0),parts(raw[1],1),parts(raw[2],0),parts(raw[3],0),parts(raw[3],1),parts(raw[4],0),parts(raw[5],0),parts(raw[5],1)]
cleared=[]
for name,pp in zip(names,base):
 den=oo
 for vv in pp.values():
  paid(vv);den=den*(vv.d/den.gcd(vv.d))
 nums=[pp[j].n*(den/pp[j].d) if j in pp else zz for j in range(max(pp,default=-1)+1)]
 for atom in units:
  while any(nums):
   gg=atom
   for nn in nums:gg=gg.gcd(nn)
   if int(gg.total_degree())==0:break
   nums=[nn/gg for nn in nums]
 if any(nums):
  first=next(nn for nn in nums if nn)
  scale0=next(iter(first.to_dict().values()))
  nums=[nn/scale0 for nn in nums]
 while nums and not nums[-1]:nums.pop()
 cleared.append(nums)
 say("original_L0_symmetric_nonzero_l_condition",name=name,tDegree=len(nums)-1,coefficientProfiles=[profile(nn) for nn in nums],claimExcluded=False)
assert len(cleared[3])<=2
def norm(po):
 po=strip_units(po)
 return po/next(iter(po.to_dict().values())) if po else po
def det(mm):
 if not mm:return oo
 if len(mm)==1:return mm[0][0]
 return sum(((-1)**j*mm[0][j]*det([row[:j]+row[j+1:] for row in mm[1:]]) for j in range(len(mm)) if mm[0][j]),zz)
def resultant(p0,q0):
 if not p0 or not q0:return zz
 n=len(p0)-1;m=len(q0)-1
 if n==0:return p0[0]**m if m else p0[0]
 if m==0:return q0[0]**n
 matrix=[[zz]*i+p0[::-1]+[zz]*(m-1-i) for i in range(m)]
 matrix.extend([[zz]*i+q0[::-1]+[zz]*(n-1-i) for i in range(n)])
 return det(matrix)
alpha=cleared[3][1] if len(cleared[3])==2 else zz
beta=cleared[3][0] if cleared[3] else zz
eqs=[]
if not alpha and beta:eqs.append(("P1_constant",norm(beta)))
for name,co in zip(names,cleared):
 if not co or name=="P1":continue
 degree=len(co)-1
 value=norm(sum((v*(-beta)**j*alpha**(degree-j) for j,v in enumerate(co)),zz))
 if value:eqs.append(("P1_"+name,value))
for i,j in [(0,1),(0,2),(1,2),(0,6),(1,6),(2,6)]:
 value=norm(resultant(cleared[i],cleared[j]))
 if value:eqs.append((names[i]+"_"+names[j],value))
for name,po in eqs:say("original_L0_symmetric_nonzero_l_two_parameter_projection",name=name,profile=profile(po),allP1ZeroLeadingFibersRetained=True,claimExcluded=False)
assert eqs
eqs.sort(key=lambda item:(int(item[1].degrees()[1]),int(item[1].total_degree()),len(item[1].to_dict())))



lookup=dict(eqs)
alpha0=norm(alpha);beta0=norm(beta)
assert int(alpha0.degrees()[0])==2 and int(beta0.degrees()[0])==1
def rho_co(poly0,j):
 return ctx.from_dict({(0,int(m[1]),int(m[2])):co for m,co in poly0.to_dict().items() if int(m[0])==j})
b0=rho_co(beta0,0);b1=rho_co(beta0,1)
assert beta0==b0+rp*b1 and b1
curveW=4*lp*wp+2*lp-2*wp*wp-4*wp-1
class FE:
 def __init__(self,field,v=0):
  self.field=field
  if isinstance(v,FE):
   assert v.field is field;self.p=v.p;return
  pp=v if isinstance(v,fmpq_poly) else fmpq_poly([v])
  self.p=divmod(pp,field.mod)[1]
 def __bool__(self):return bool(self.p)
 def __add__(self,o):o=FE(self.field,o);return FE(self.field,self.p+o.p)
 __radd__=__add__
 def __neg__(self):return FE(self.field,-self.p)
 def __sub__(self,o):return self+-FE(self.field,o)
 def __rsub__(self,o):return FE(self.field,o)+-self
 def __mul__(self,o):o=FE(self.field,o);return FE(self.field,self.p*o.p)
 __rmul__=__mul__
 def __eq__(self,o):o=FE(self.field,o);return self.p==o.p
 def inv(self):
  assert self
  gg,ss,tt=self.p.xgcd(self.field.mod)
  assert self.p*ss+self.field.mod*tt==gg
  assert gg and gg.degree()==0
  vv=FE(self.field,ss/gg[0]);assert self*vv==1
  self.field.inverses+=1
  return vv
class Field:
 def __init__(self,phi):
  self.mod=phi/phi.leading_coefficient();self.inverses=0
  self.zero=FE(self,0);self.one=FE(self,1)
 def __call__(self,v=0):return FE(self,v)

def ftrim(pp):
 pp=list(pp)
 while pp and not pp[-1]:pp.pop()
 return pp
def fadd(pp,qq):
 if not pp:return list(qq)
 if not qq:return list(pp)
 field=pp[0].field
 out=[field.zero]*max(len(pp),len(qq))
 for i,v in enumerate(pp):out[i]=out[i]+v
 for i,v in enumerate(qq):out[i]=out[i]+v
 return ftrim(out)
def fneg(pp):return [-v for v in pp]
def fsub(pp,qq):return fadd(pp,fneg(qq))
def fmul(pp,qq):
 if not pp or not qq:return []
 field=pp[0].field;out=[field.zero]*(len(pp)+len(qq)-1)
 for i,u0 in enumerate(pp):
  for j,v0 in enumerate(qq):out[i+j]=out[i+j]+u0*v0
 return ftrim(out)
def fdivmod(pp,qq):
 pp=ftrim(pp);qq=ftrim(qq);assert qq
 original=list(pp);field=qq[0].field
 if len(pp)<len(qq):return [],pp
 quotient=[field.zero]*max(0,len(pp)-len(qq)+1);iv=qq[-1].inv()
 while pp and len(pp)>=len(qq):
  sh=len(pp)-len(qq);co=pp[-1]*iv
  quotient[sh]=quotient[sh]+co
  for j,v0 in enumerate(qq):pp[j+sh]=pp[j+sh]-co*v0
  pp=ftrim(pp)
 quotient=ftrim(quotient)
 assert fadd(fmul(quotient,qq),pp)==original
 assert not pp or len(pp)<len(qq)
 return quotient,pp
def fxgcd(pp,qq):
 pp=ftrim(pp);qq=ftrim(qq)
 if not pp and not qq:return [],[],[]
 field=(pp or qq)[0].field
 a0=list(pp);b0=list(qq)
 s0=[field.one];s1=[];t0=[];t1=[field.one]
 while qq:
  quot,rem=fdivmod(pp,qq);pp,qq=qq,rem
  s0,s1=s1,fsub(s0,fmul(quot,s1))
  t0,t1=t1,fsub(t0,fmul(quot,t1))
 if pp:
  iv=pp[-1].inv();pp=[iv*v0 for v0 in pp]
  s0=[iv*v0 for v0 in s0];t0=[iv*v0 for v0 in t0]
 assert fadd(fmul(a0,s0),fmul(b0,t0))==pp
 return pp,ftrim(s0),ftrim(t0)
def fgcd(pp,qq):return fxgcd(pp,qq)[0]
def fquot(pp,qq):
 answer,rem=fdivmod(pp,qq);assert not rem;return answer
def specialize(poly0,field):
 terms=poly0.to_dict()
 if not terms:return []
 assert all(int(m[0])==0 for m in terms)
 dz=max(int(m[2]) for m in terms);out=[]
 for j in range(dz+1):
  dd={int(m[1]):v0 for m,v0 in terms.items() if int(m[2])==j}
  coeff=fmpq_poly([dd.get(i,fmpq(0)) for i in range(max(dd,default=-1)+1)])
  out.append(field(coeff))
 return ftrim(out)


def field_power(v,n):
 out=v.field.one
 for _ in range(n):out=out*v
 return out

curveG=384*lp**7*wp**3 + 576*lp**7*wp**2 + 192*lp**7*wp - 128*lp**6*wp**4 - 1472*lp**6*wp**3 - 1904*lp**6*wp**2 - 464*lp**6*wp + 32*lp**6 + 352*lp**5*wp**4 + 2304*lp**5*wp**3 + 2592*lp**5*wp**2 + 368*lp**5*wp - 96*lp**5 - 400*lp**4*wp**4 - 1936*lp**4*wp**3 - 1916*lp**4*wp**2 - 20*lp**4*wp + 120*lp**4 + 248*lp**3*wp**4 + 952*lp**3*wp**3 + 828*lp**3*wp**2 - 156*lp**3*wp - 84*lp**3 - 88*lp**2*wp**4 - 264*lp**2*wp**3 - 194*lp**2*wp**2 + 120*lp**2*wp + 36*lp**2 + 16*lp*wp**4 + 28*lp*wp**3 + 10*lp*wp**2 - 42*lp*wp - 9*lp + 4*wp**3 + 4*wp**2 + 6*wp + 1


def lambda_remainder(po,phi):
 dic={}
 X=fmpq_poly([0,1])
 for mon,aa in po.to_dict().items():
  coeff=divmod(X**int(mon[1]),phi)[1]
  for i in range(coeff.degree()+1):
   key=(int(mon[0]),i,int(mon[2]));dic[key]=dic.get(key,fmpq(0))+aa*coeff[i]
 return ctx.from_dict({key:aa for key,aa in dic.items() if aa})

def return_rho(po,field,lvalue,wvalue):
 terms=po.to_dict()
 if not terms:return []
 degree=max(int(m[0]) for m in terms)
 lc=[field_power(lvalue,i) for i in range(max(int(m[1]) for m in terms)+1)]
 wc=[field_power(wvalue,i) for i in range(max(int(m[2]) for m in terms)+1)]
 out=[field.zero]*(degree+1)
 for m,aa in terms.items():out[int(m[0])]=out[int(m[0])]+aa*lc[int(m[1])]*wc[int(m[2])]
 return ftrim(out)



# Everything below is reconstructed from the original nine conditions above.
# No cached polynomial, finite-field search result or external coefficient file is read.
import math
from flint import nmod_mpoly_ctx,nmod_poly,nmod_mat,fmpq_mat

def degree0(p,i):return int(p.degrees()[i]) if p else -1
def leading0(p,i):
 d=degree0(p,i)
 return ctx.from_dict({tuple(0 if j==i else int(m[j]) for j in range(3)):a for m,a in p.to_dict().items() if int(m[i])==d})
mpseudo_checks=0
def pseudodiv(p,q,i):
 global mpseudo_checks
 assert q
 pp=p;qq=zz;factor=oo;xvar=[rp,lp,wp][i];qd=degree0(q,i);qc=leading0(q,i)
 while pp and degree0(pp,i)>=qd:
  sh=degree0(pp,i)-qd;cc=leading0(pp,i)
  pp=qc*pp-cc*xvar**sh*q;qq=qc*qq+cc*xvar**sh;factor*=qc
 assert factor*p==q*qq+pp
 mpseudo_checks+=1
 return qq,pp,factor
# All coefficients below are derived from the original nine equations above.
original_units=list(units)
Kraw=alpha0.resultant(beta0,'rho');Kcurve=norm(Kraw)
a2=rho_co(alpha0,2);a1=rho_co(alpha0,1);a0=rho_co(alpha0,0)
assert Kraw==a2*b0*b0-a1*b0*b1+a0*b1*b1
assert b1*b1*alpha0==beta0*(a2*b1*rp+a1*b1-a2*b0)+Kraw
assert leading0(Kcurve,2)==-lp*lp/75
assert int(strip_units(a2).total_degree())==0
say('complete_K_input',curve=profile(Kcurve),leadingW=str(leading0(Kcurve,2)),betaLeading=profile(b1),betaConstant=profile(b0),betaUnitIdentityMultipliedBack=True)

# REGULAR CHART: on K=0 and b1!=0 the already paid alpha0 forces beta0!=0.
# Every beta pseudo-division is returned exactly modulo the entire K curve.
units=original_units+[curveG,curveW,alpha0,b1]
rows={}
for name in ['P1_E1','P1_N1','P1_EBe']:
 pp=lookup[name];count=0
 while pp and degree0(pp,0)>=1:
  qq,rr,factor=pseudodiv(pp,beta0,0)
  div,rem=divmod(rr,Kcurve)
  if rem:break
  assert rr==div*Kcurve and factor*pp==beta0*qq+div*Kcurve
  pp=norm(qq);count+=1
 assert count==2
 rows[name]=pp
 say('regular_K_original_beta_return',name=name,removedBetaFactors=count,profile=profile(pp))
r1full=norm(rows['P1_E1'].resultant(rows['P1_N1'],'rho'))
assert degree0(r1full,0)==0
_,r1,factor=pseudodiv(r1full,Kcurve,2);r1=norm(r1)
say('regular_K_first_original_projection',rhoResultant=profile(r1full),wRemainder=profile(r1))
projection=norm(Kcurve.resultant(r1,'w'))
assert projection and degree0(projection,0)==degree0(projection,2)==0
def to_lambda_poly(po):
 assert po and all(int(m[0])==int(m[2])==0 for m in po.to_dict())
 cs=[fmpq(0)]*(degree0(po,1)+1)
 for m,a in po.to_dict().items():cs[int(m[1])]=a
 return fmpq_poly(cs)
univar=to_lambda_poly(projection)
deriv_gcd=univar.gcd(univar.derivative());sf,rr=divmod(univar,deriv_gcd)
assert not rr and sf*deriv_gcd==univar
content,factors=sf.factor();back=fmpq_poly([content])
for ph,n in factors:back*=ph**n
assert back==sf and all(n==1 for ph,n in factors)
phis=[ph for ph,n in factors]
assert univar.degree()==1253 and sf.degree()==329
assert sorted(ph.degree() for ph in phis)==[1,1,1,1,2,2,2,3,3,7,26,46,234]
say('complete_K_regular_lambda_cover',degree=univar.degree(),squarefreeDegree=sf.degree(),factorDegrees=[ph.degree() for ph in phis],projectionSha256=hashlib.sha256(str(univar).encode()).hexdigest(),factorProductMultipliedBack=True)

# This is the complete rational second rho projection. Its reduction is used
# only in UNIVARIATE coprimality certificates with degree-preserved phi.
r2=norm(rows['P1_E1'].resultant(rows['P1_EBe'],'rho'))
assert degree0(r2,0)==0
say('regular_K_second_original_projection',profile=profile(r2))
prime=1031
mc=nmod_mpoly_ctx.get(('rho','lam','w'),prime,'lex')
def modrat(a,p=prime):
 d=int(a.denominator)%p;assert d
 return int(a.numerator)%p*pow(d,-1,p)%p
def modmp(po):return mc.from_dict({tuple(map(int,m)):modrat(a) for m,a in po.to_dict().items()})
km=modmp(Kcurve);rm=modmp(r2)
assert int(km.degrees()[2])==degree0(Kcurve,2)==12
assert int(rm.degrees()[2])==degree0(r2,2)==224
pm=km.resultant(rm,'w');cs=[0]*(int(pm.degrees()[1])+1)
for m,a in pm.to_dict().items():assert int(m[0])==int(m[2])==0;cs[int(m[1])]=int(a)
p2=nmod_poly(cs,prime)
modular_closed=[];exact_phis=[]
for ph in phis:
 fm=nmod_poly([modrat(a) for a in ph],prime);assert fm.degree()==ph.degree()
 dg,aa,bb=fm.xgcd(p2);assert aa*fm+bb*p2==dg
 if dg.degree()==0:
  modular_closed.append(ph)
  say('regular_K_univariate_coprimality',lambdaDegree=ph.degree(),phiCoefficientsLowFirst=[str(a) for a in ph] if ph.degree()<10 else None,phiSha256=hashlib.sha256(str(ph).encode()).hexdigest(),prime=prime,completeSecondProjectionModDegree=p2.degree(),originalWDegrees=[12,224],bezoutSha256=hashlib.sha256((str(aa)+'\n'+str(bb)).encode()).hexdigest(),claimExcluded=True)
 else:exact_phis.append(ph)
assert sorted(ph.degree() for ph in modular_closed)==[1,26,234]

# Exact multiplication matrices keep small number-field inverses controlled.
def matrix_inv(self):
 assert self
 field=self.field;n=field.mod.degree();X=fmpq_poly([0,1])
 cols=[divmod(self.p*X**j,field.mod)[1] for j in range(n)]
 mat=fmpq_mat([[cols[j][i] for j in range(n)] for i in range(n)])
 rhs=fmpq_mat([[int(i==0)] for i in range(n)])
 sol=mat.solve(rhs,algorithm='dixon');assert mat*sol==rhs
 ans=field(fmpq_poly([sol[i,0] for i in range(n)]));assert self*ans==1
 field.inverses+=1;return ans
FE.inv=matrix_inv
parameter_atoms=[('original_'+str(i),po) for i,po in enumerate(original_units) if degree0(po,0)==0]
parameter_atoms += [('closed_W',curveW),('closed_G',curveG),('regular_b1',b1)]
small_reports=[]
for ph in exact_phis:
 if ph.degree()==46:continue
 assert ph.degree()<=7
 field=Field(ph);common=fgcd(specialize(Kcurve,field),specialize(r1,field))
 original_degree=len(common)-1;removed=[]
 for label,atom in parameter_atoms:
  uu=specialize(atom,field)
  if not uu:removed.append([label,'identically_zero']);common=[field.one];break
  while len(common)>1:
   dd=fgcd(common,uu)
   if len(dd)<=1:break
   common=fquot(common,dd);removed.append([label,len(dd)-1])
 assert len(common)==1
 rec=dict(phiCoefficientsLowFirst=[str(a) for a in ph],lambdaDegree=ph.degree(),originalWDegree=original_degree,removedPaidUnits=removed,fieldInverseMultiplyBacks=field.inverses,claimExcluded=True)
 small_reports.append(rec);say('regular_K_exact_small_parameter_return',**rec)
assert len(small_reports)==9

fpseudo_checks=0
primitive_checks=0
def primitive(pp):
 global primitive_checks
 pp=ftrim(pp)
 if not pp:return []
 field=pp[0].field;den=1;g=0
 for val in pp:
  for a in val.p:den=math.lcm(den,int(a.denominator))
 for val in pp:
  for a in val.p:g=math.gcd(g,int(a.numerator)*(den//int(a.denominator)))
 scalar=fmpq(den,g);out=[field(v.p*scalar) for v in pp]
 assert all(a.p*scalar==b.p for a,b in zip(pp,out))
 primitive_checks+=1
 return out
def fpseudodiv(pp,qq):
 global fpseudo_checks
 pp=ftrim(pp);qq=ftrim(qq);assert qq
 field=qq[0].field;original=list(pp);quot=[];factor=field.one
 while pp and len(pp)>=len(qq):
  sh=len(pp)-len(qq);a=qq[-1];b=pp[-1]
  quot=fadd([a*v for v in quot],[field.zero]*sh+[b])
  pp=fsub([a*v for v in pp],[field.zero]*sh+[b*v for v in qq]);factor=factor*a
 assert fadd(fmul(quot,qq),pp)==[factor*v for v in original]
 fpseudo_checks+=1
 return quot,pp,factor
def fpgcd(pp,qq):
 pp=primitive(pp);qq=primitive(qq)
 while qq:
  quo,rem,factor=fpseudodiv(pp,qq);pp,qq=qq,primitive(rem)
 return primitive(pp)
def fpquot(pp,qq):
 quo,rem,factor=fpseudodiv(pp,qq);assert not rem
 return primitive(quo)
def saturate(pp,atoms):
 history=[]
 for label,uu in atoms:
  assert uu # A zero unit polynomial would exclude this entire parameter fiber.
  while len(pp)>1:
   dd=fpgcd(pp,uu)
   if len(dd)<=1:break
   pp=fpquot(pp,dd);history.append([label,len(dd)-1])
  if len(pp)==1:break
 return pp,history

def exact_linear_w(field,gg):
 assert len(gg)==2 and gg[1]
 degree=field.mod.degree();lv=field(fmpq_poly([0,1]));a=gg[1];b=gg[0]
 columns=[(a*field_power(lv,j)).p for j in range(degree)]
 M=fmpq_mat([[columns[j][i] for j in range(degree)] for i in range(degree)])
 rhs=fmpq_mat([[-b.p[i]] for i in range(degree)])
 solution=M.solve(rhs,algorithm='dixon')
 assert M*solution==rhs
 wv=field(fmpq_poly([solution[i,0] for i in range(degree)]))
 assert a*wv+b==0
 # A genuine rational multiplication matrix, not a sampled geometric point.
 determinant_witness=None
 for p in [1031,1033,1039,1049,1051,1061,1063,1069,1087,1091]:
  if any(int(M[i,j].denominator)%p==0 for i in range(degree) for j in range(degree)):continue
  md=nmod_mat([[modrat(M[i,j],p) for j in range(degree)] for i in range(degree)],p).det()
  if md:determinant_witness=[p,int(md)];break
 assert determinant_witness is not None
 return wv,determinant_witness



# The remaining degree-46 field shares exactly one w point with the already
# closed G curve. Derive it afresh; do not read a cached algebraic value.
ph=next(ph for ph in exact_phis if ph.degree()==46)
field=Field(ph);lv=field(fmpq_poly([0,1]))
wg=fpgcd(specialize(Kcurve,field),specialize(curveG,field))
assert len(wg)==2
wv,witness=exact_linear_w(field,wg)
assert not return_rho(curveG,field,lv,wv)
def at_w(pp):
 out=field.zero
 for a in pp[::-1]:out=out*wv+a
 return out
def divide_w_linear(pp):
 original=list(pp);pp=list(pp);out=[field.zero]*(len(pp)-1)
 for i in range(len(pp)-1,0,-1):
  out[i-1]=pp[i];pp[i-1]=pp[i-1]+wv*pp[i]
 assert not pp[0] and fmul(out,[-wv,field.one])==ftrim(original)
 return ftrim(out)
kw=specialize(Kcurve,field);rw=specialize(r1,field);removed=0
while kw and not at_w(kw):kw=divide_w_linear(kw);removed+=1
assert removed==1 and len(kw)==len(rw)==12
c2=nmod_mpoly_ctx.get(('lam','w'),prime,'lex')
def fpoly_mod(pp):return c2.from_dict({(i,j):modrat(a) for j,v in enumerate(pp) for i,a in enumerate(v.p) if a})
km=fpoly_mod(kw);rm=fpoly_mod(rw)
assert int(km.degrees()[1])==len(kw)-1 and int(rm.degrees()[1])==len(rw)-1
zp0=km.resultant(rm,'w');cc=[0]*(int(zp0.degrees()[0])+1)
for m,a in zp0.to_dict().items():assert int(m[1])==0;cc[int(m[0])]=int(a)
zp=nmod_poly(cc,prime);phi46m=nmod_poly([modrat(a) for a in ph],prime)
assert phi46m.degree()==ph.degree()==46
dg,aa,bb=phi46m.xgcd(zp)
assert aa*phi46m+bb*zp==dg and dg.degree()==0
say('regular_K_entire_degree46_return',closedGFactorMultiplicity=removed,matrixDeterminantWitness=witness,derivedWValueSha256=hashlib.sha256(str(wv.p).encode()).hexdigest(),remainingWDegrees=[len(kw)-1,len(rw)-1],univariateResultantModDegree=zp.degree(),prime=prime,bezoutMultiplyBack=True,claimExcluded=True)

# BOUNDARY b1=0: Kraw=a2*b0^2 and the original a2 is a paid unit, so b0=0.
# Original P1 is then alpha*t=0; paid alpha forces the ORIGINAL t=0.
# Reconstruct the earlier complete b1=b0 cover, without imposing alpha=0.
boundary_paid=[('original_'+str(i),po) for i,po in enumerate(original_units) if degree0(po,0)==0]+[('closed_W',curveW)]
def strip_with(po,atoms):
 for label,atom in atoms:
  assert atom
  while po:
   gg=po.gcd(atom)
   if int(gg.total_degree())==0:break
   qq,rr=divmod(po,gg);assert not rr and qq*gg==po;po=qq
 return po/po.coefficient(0) if po else po
b1eq=strip_with(b1,boundary_paid);b0eq=strip_with(b0,boundary_paid)
boundary_projection=b1eq.resultant(b0eq,'w')
boundary_projection=strip_with(boundary_projection,[(n,a) for n,a in boundary_paid if degree0(a,2)==0])
bp=to_lambda_poly(boundary_projection);bc0,bfactors=bp.factor();back=fmpq_poly([bc0])
for ph,n in bfactors:back*=ph**n
assert back==bp and bp.degree()==42
say('boundary_beta_zero_complete_parameter_cover',degree=bp.degree(),factorDegrees=[ph.degree() for ph,n in bfactors],factorProductMultipliedBack=True,alphaZeroNeverAssumed=True)
boundary_reports=[];rho_returns=0
for ph,n in bfactors:
 field=Field(ph);lv=field(fmpq_poly([0,1]))
 atoms=[(label,specialize(atom,field)) for label,atom in boundary_paid]
 zero=next((label for label,atom in atoms if not atom),None)
 if zero:
  rec=dict(lambdaDegree=ph.degree(),zeroParameterUnit=zero,claimExcluded=True)
 else:
  common=fgcd(specialize(b1eq,field),specialize(b0eq,field));history=[]
  for label,atom in atoms:
   while len(common)>1:
    dd=fgcd(common,atom)
    if len(dd)<=1:break
    common=fquot(common,dd);history.append([label,len(dd)-1])
  rec=dict(lambdaDegree=ph.degree(),remainingWDegree=len(common)-1,parameterUnitRemovals=history)
  if len(common)>1:
   assert len(common)==2 and ph.degree() in [1,7]
   wv=-common[0]*common[1].inv()
   assert not return_rho(b0,field,lv,wv) and not return_rho(b1,field,lv,wv)
   rho_atoms=[('original_'+str(i),return_rho(a,field,lv,wv)) for i,a in enumerate(original_units)]
   rho_atoms += [('closed_W',return_rho(curveW,field,lv,wv)),('closed_G',return_rho(curveG,field,lv,wv)),('paid_alpha',return_rho(alpha0,field,lv,wv))]
   rz=next((label for label,atom in rho_atoms if not atom),None)
   if rz:rec['zeroRhoUnit']=rz
   else:
    rg=[];rh=[];used=[]
    for name,co in zip(names,cleared):
     if name=='P1':continue
     # Direct ORIGINAL coefficients at t=0, not the alpha=beta=0 equations.
     rg=fgcd(rg,return_rho(co[0],field,lv,wv));used.append(name)
     for label,atom in rho_atoms:
      while len(rg)>1:
       dd=fgcd(rg,atom)
       if len(dd)<=1:break
       rg=fquot(rg,dd);rh.append([label,len(dd)-1])
     if len(rg)==1:break
    assert len(rg)==1
    rec.update(originalTZeroRows=used,rhoUnitRemovals=rh,remainingRhoDegree=0)
   rho_returns+=1
   rec.update(phiCoefficientsLowFirst=[str(a) for a in ph],sameWValueCoefficientsLowFirst=[str(a) for a in wv.p],fieldInverseMultiplyBacks=field.inverses)
  rec['claimExcluded']=True
 boundary_reports.append(rec);say('boundary_beta_zero_original_t_zero_return',**rec)
assert rho_returns==2 and all(r['claimExcluded'] for r in boundary_reports)
signal.alarm(0)
say('complete_original_L0_K_curve_exclusion',scope='entire K(lambda,w)=0, both b1 charts, all original t/rho and leading fibers retained',regularCoverDegree=1253,regularSquarefreeDegree=329,modularParameterDomains=3,smallExactParameterDomains=9,degree46Domain=True,boundaryCoverDegree=42,boundaryOriginalTZeroReturns=rho_returns,originalSourceDenominatorCount=len(denominators),multivariatePseudoDivisionIdentities=mpseudo_checks,numberFieldPseudoDivisionIdentities=fpseudo_checks,rationalPrimitiveIdentities=primitive_checks,sourceSha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),claimExcluded=True,ordinaryISPClaim=False,peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
