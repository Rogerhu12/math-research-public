#!/usr/bin/env python3
"""Original QQ exclusion of P0=0 in the remaining unit 2+1+1 chart.
No stored elimination arrays are inputs. All rational resultants stay in memory.
"""
import time,resource,hashlib,json
from pathlib import Path
from flint import fmpq_mpoly_ctx,fmpq
started=time.perf_counter()
resource.setrlimit(resource.RLIMIT_AS,(1536*1024**2,)*2)
resource.setrlimit(resource.RLIMIT_CPU,(360,370))
import sympy as S
b,c,A,r,s,t,p,q=S.symbols('b c A r s t p q')
a=1-b-c
one=S.Matrix([1,0,1,1])
K=S.Matrix([[0,0,p,q],[0,A,r,s],[p,r,0,t],[q,s,t,0]])
def mul(x,y):return S.Matrix([x[0]*y[0],x[0]*y[1]+x[1]*y[0],x[2]*y[2],x[3]*y[3]])
def tau(z):return a*z[0]+z[1]+b*z[2]+c*z[3]
def dk(z):return S.Matrix([tau(mul(K.row(i),z)) for i in range(4)])
d=dk(one);F=tau(d)/2
def pp(z):
 w=z-tau(z)*one
 return tau(mul(mul(w,w),w))/2

def nn(z):return tau(mul(d-F*one,mul(z,z)))/2-tau(z)*tau(mul(d,z))+F*tau(z)**2+tau(mul(z,dk(z)))/4
hjet=S.symbols('hjet')
Pbase=pp(K.row(0).T+hjet*K.row(1).T)
Nbase=nn(K.row(0).T+hjet*K.row(1).T)
Ps=[S.factor(Pbase.subs(hjet,0)),S.factor(S.diff(Pbase,hjet).subs(hjet,0)),S.factor(pp(K.row(2).T)),S.factor(pp(K.row(3).T))]
Ns=[S.factor(Nbase.subs(hjet,0)),S.factor(S.diff(Nbase,hjet).subs(hjet,0)),S.factor(nn(K.row(2).T)),S.factor(nn(K.row(3).T))]
e=S.Matrix([tau(mul(K.row(0),K.row(0))),2*tau(mul(K.row(0),K.row(1))),tau(mul(K.row(2),K.row(2))),tau(mul(K.row(3),K.row(3)))])
E=S.simplify(e-2*dk(d)-2*mul(d,d)+4*F*d)
def subfac(v,sub):return [S.factor(x.subs(sub,simultaneous=True)) for x in v]

u,l,X,Z=S.symbols('u l X Z')
J=2*u*u-3*(q+1)*u+q*q+q+1;D=3*u-q-1;H=q+1-2*u
bb=(q*l-u)/(q-1);cc=(u-l)/(q-1)
xx=X+cc*q*Z/u;yy=X-bb*Z/u;ff=X/2+u/2-(bb+cc*q*q)/(4*u)
chart={p:1,b:bb,c:cc,r:xx-(1-l)-cc*t,s:yy-q*(1-l)-bb*t,A:2*ff-2*bb*xx-2*cc*yy+2*bb*cc*t}
PP=subfac(Ps,chart);NN=subfac(Ns,chart)
assert S.factor(E[0].subs(chart,simultaneous=True))==0
assert S.factor(PP[0]-(u*J+q*l*D)/2)==0
assert S.factor(PP[0].subs(u,(q+1)/3))==(q+1)*(q-2)*(2*q-1)/54
l0=-u*J/(q*D)
regP=S.factor(PP[1].subs(l,l0));regN=S.factor(NN[0].subs(l,l0))
mat=S.Matrix([[S.diff(ex,var) for var in [X,Z]] for ex in [regP,regN]])
det=-3*u**2*(q-2*u)**3*(q-u)*(u-1)*(2*u-1)**3*H/(8*q*(q-1)*D**4)
assert S.factor(mat.det()-det)==0
sol=S.solve([regP,regN],[X,Z],dict=True);assert len(sol)==1;sol=sol[0]

# Reconstruct the original equations with native exact rational arithmetic.
ctx=fmpq_mpoly_ctx.get(('t','u','q'),'lex');tp,up,qp=ctx.gens();zero=ctx.constant(0);onep=ctx.constant(1)
class R:
 def __init__(self,x=0,d=None,reduce=True):
  if isinstance(x,R):self.n=x.n;self.d=x.d;return
  n=x if hasattr(x,'to_dict') else ctx.constant(x);d=onep if d is None else d
  if not n:self.n=zero;self.d=onep;return
  assert d
  if reduce:gg=n.gcd(d);n=n/gg;d=d/gg
  self.n=n;self.d=d
 def __add__(self,o):o=R(o);return R(self.n*o.d+o.n*self.d,self.d*o.d)
 __radd__=__add__
 def __neg__(self):return R(-self.n,self.d,False)
 def __sub__(self,o):return self+-R(o)
 def __rsub__(self,o):return R(o)+-self
 def __mul__(self,o):o=R(o);return R(self.n*o.n,self.d*o.d)
 __rmul__=__mul__
 def __truediv__(self,o):o=R(o);return R(self.n*o.d,self.d*o.n)
 def __rtruediv__(self,o):return R(o)/self
 def __pow__(self,n):return R(self.n**n,self.d**n,False) if n>=0 else R(self.d**(-n),self.n**(-n),False)
 def iszero(self):return not self.n
def fp(ex):return ctx.from_dict({mm:fmpq(str(co)) for mm,co in S.Poly(ex,t,u,q,domain=S.QQ).terms()})
def sp(po):return S.Poly.from_dict({mm:S.Rational(str(co)) for mm,co in po.to_dict().items()},(t,u,q)).as_expr()
def tor(ex):n,d=S.fraction(S.cancel(ex));return R(fp(n),fp(d))
rt,ru,rq=R(tp),R(up),R(qp);rl=tor(l0);rb=(rq*rl-ru)/(rq-1);rc=(ru-rl)/(rq-1);ra=1-rl
rx=tor(sol[X])+rc*rq*tor(sol[Z])/ru;ry=tor(sol[X])-rb*tor(sol[Z])/ru
rf=tor(sol[X])/2+ru/2-(rb+rc*rq*rq)/(4*ru)
rr=rx-ra-rc*rt;rs=ry-rq*ra-rb*rt;rA=2*rf-2*rb*rx-2*rc*ry+2*rb*rc*rt
RK=[[R(0),R(0),R(1),rq],[R(0),rA,rr,rs],[R(1),rr,R(0),rt],[rq,rs,rt,R(0)]]
rone=[R(1),R(0),R(1),R(1)]
def add(x,y):return [a+b for a,b in zip(x,y)]
def scale(a,x):return [a*b for b in x]
def rmul(x,y):return [x[0]*y[0],x[0]*y[1]+x[1]*y[0],x[2]*y[2],x[3]*y[3]]
def rtau(x):return ra*x[0]+x[1]+rb*x[2]+rc*x[3]
def rdk(x):return [rtau(rmul(k,x)) for k in RK]
rd=rdk(rone);rF=rtau(rd)/2
def rP(x):z=add(x,scale(-rtau(x),rone));return rtau(rmul(rmul(z,z),z))/2
def rN(x):return rtau(rmul(add(rd,scale(-rF,rone)),rmul(x,x)))/2-rtau(x)*rtau(rmul(rd,x))+rF*rtau(x)**2+rtau(rmul(x,rdk(x)))/4
def rPjet(x,y):z=add(x,scale(-rtau(x),rone));h=add(y,scale(-rtau(y),rone));return 3*rtau(rmul(rmul(z,z),h))/2
assert rP(RK[0]).iszero() and rPjet(RK[0],RK[1]).iszero() and rN(RK[0]).iszero()
rN1=rN(add(RK[0],RK[1]))-rN(RK[0])-rN(RK[1])
re=[rtau(rmul(RK[0],RK[0])),2*rtau(rmul(RK[0],RK[1])),rtau(rmul(RK[2],RK[2])),rtau(rmul(RK[3],RK[3]))]
rE=add(add(re,scale(-2,rdk(rd))),add(scale(-2,rmul(rd,rd)),scale(4*rF,rd)))
assert rE[0].iszero()
known=q*(q-1)*(q+1)*u*(u-1)*(2*u-1)*(q-u)*(q-2*u)*D*H
def strip(po,kn):
 while po:
  gg=po.gcd(kn)
  if gg.total_degree()==0:return po
  po=po/gg
 return po
def monic(po):return po/po.leading_coefficient()
def strip_s(ex,kn):return sp(strip(fp(ex),fp(kn)))
LA=(q-1)**2*(q-2*u)*(2*u-1);LB=-u*(2*q*q-4*q*u+q-4*u+2);LL=LA+LB*t
assert monic(strip(rN1.n,fp(known)))==monic(fp(t*J*LL))
ms=[sp(v.n) for v in rE[1:]]

# t=0: the only abstract mean family has rank two and U=0.
tpols=[S.factor(strip_s(S.factor(v.subs(t,0)),known)) for v in ms]
assert all(S.Poly(x,u,q).monic().as_expr()==u-q-1 for x in tpols)
tz={p:1,b:-(q+2)/(2*(q-1)),c:(2*q+1)/(2*(q-1)),A:0,r:0,s:0,t:0}
assert all(x==0 for x in subfac(list(E)+Ps+Ns,tz))
assert S.factor(sol[X].subs({u:q+1,t:0},simultaneous=True)-(2*q*q+3*q+2)/(4*(q+1)))==0
assert S.factor(sol[Z].subs({u:q+1,t:0},simultaneous=True)+(q-1)/2)==0

# J=0: complete resultants and all surviving fibers.
jps=[strip_s(S.fraction(S.factor(S.rem(v,J,u)))[0],known) for v in ms]
f0,f1,f2,fj=map(fp,jps+[J]);jr=[f0.resultant(v,'t').resultant(fj,'u') for v in [f1,f2]]
jg=jr[0].gcd(jr[1]);jtarget=q**6*(q-2)**8*(q-1)**8*(2*q-1)**8*(q*q+q+1)**3
assert monic(jg)==monic(fp(jtarget))
assert [max(mm[2] for mm in x.to_dict()) for x in jr]==[41,42]
for qv,uv in [(S.Integer(2),S.Rational(7,2)),(S.Rational(1,2),S.Rational(7,4))]:
 assert S.degree(S.gcd_list([v.subs({q:qv,u:uv}) for v in ms]),t)==0
Q3=q*q+q+1
j3=[S.rem(v.subs(u,3*(q+1)/2),Q3,q) for v in ms]
assert list(S.groebner(j3+[Q3],t,q,domain=S.QQ))==[S.Integer(1)]

# Last factor L=0: pay its leading coefficient before division.
us=(2*q*q+q+2)/(4*(q+1))
assert S.factor(LA.subs(u,us)-q*(q-2)*(q-1)**2*(2*q-1)/(4*(q+1)**2))==0
lps=[strip_s(S.fraction(S.factor(v.subs(t,-LA/LB)))[0],known*LB) for v in ms]
f0,f1,f2=map(fp,lps);lr=[f0.resultant(v,'u') for v in [f1,f2]]
lg=lr[0].gcd(lr[1]);ltarget=q**5*(q-2)**6*(2*q-1)**6*(25*q*q-14*q+25)
assert monic(lg)==monic(fp(ltarget))
assert [max(mm[2] for mm in x.to_dict()) for x in lr]==[31,31]
for qv,target in [(S.Integer(2),(u-1)**2),(S.Rational(1,2),(u-S.Rational(1,2))**2)]:
 gg=S.Poly(S.gcd_list([v.subs(q,qv) for v in lps]),u).monic().as_expr();assert S.expand(gg-target)==0
Q25=25*q*q-14*q+25
gb=list(S.groebner(lps+[Q25],u,q,domain=S.QQ))
assert gb==[u-q/2-S.Rational(1,2),q*q-S.Rational(14,25)*q+1]

# D=0: q=2,u=1, with q=1/2 obtained by swapping and common scaling.
bb2=2*l-1;cc2=1-l;xx2=X+2*cc2*Z;yy2=X-bb2*Z;ff2=X/2+l/2-S.Rational(1,4)
ch2={p:1,q:2,b:bb2,c:cc2,r:xx2-(1-l)-cc2*t,s:yy2-2*(1-l)-bb2*t,A:2*ff2-2*bb2*xx2-2*cc2*yy2+2*bb2*cc2*t}
p2=subfac(Ps,ch2);n2=subfac(Ns,ch2)
mat2=S.Matrix([[S.diff(v,w) for w in [X,Z]] for v in [p2[1],n2[0]]])
assert S.factor(mat2.det()+3*(l-1)*(2*l-1)**3/8)==0
sol2=S.solve([p2[1],n2[0]],[X,Z],dict=True);assert len(sol2)==1;sol2=sol2[0]
ee2=[S.factor(v.subs(sol2,simultaneous=True)) for v in subfac(E,ch2)]
assert S.factor(n2[1].subs(sol2,simultaneous=True)+2*l*t*(l-1)*(6*l*t-2*l-t+1))==0
for sub,target in [({l:0},S.Integer(1)),({t:0},l-S.Rational(1,2)),({t:(2*l-1)/(6*l-1)},S.Integer(1))]:
 pol=[S.fraction(S.factor(v.subs(sub)))[0] for v in ee2[1:]]
 vv=t if l in sub else l;gg=S.Poly(S.gcd_list(pol),vv).monic().as_expr();assert gg==target

# H=0: original half weights force an excluded isotropic 2A+Z.
hb={p:1,b:S.Rational(1,2),c:S.Rational(1,2)}
hlin=[S.factor(v.subs(hb,simultaneous=True)) for v in [E[0],Ps[1],Ns[0]]]
hsol=S.solve(hlin,[A,s],dict=True);assert len(hsol)==1 and hsol[0][A]==0 and S.factor(hsol[0][s]-q*(1-r))==0
hh=hb|{A:0,s:q*(1-r)};he=subfac(E,hh)
assert all(S.factor(v+q*(2*r*r-2*r+1))==0 for v in he[1:])
hP=subfac(Ps,hh);hN=subfac(Ns,hh)
for idx in [2,3]:
 num=S.fraction(S.factor(hP[idx]-2*hN[idx]))[0];assert S.rem(num,2*r*r-2*r+1,r)==0
assert hP[0]==hP[1]==hN[0]==hN[1]==0

proof_digest=hashlib.sha256('\n'.join(str(S.factor(x)) for x in [det,LL,jtarget,ltarget]+gb).encode()).hexdigest()
print(json.dumps({'status':'all original identities and QQ elimination fibers verified','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'resultant_degrees':{'J':[41,42],'L':[31,31]},'proof_identity_sha256':proof_digest,'runtime_seconds':time.perf_counter()-started,'maxrss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},sort_keys=True),flush=True)
