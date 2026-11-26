#!/usr/bin/env python3
"""Self-contained original QQ verification: p=1,q=-1,b+c=0,b-c!=0."""
import hashlib,json,resource,time
from pathlib import Path
import sympy as S
started=time.perf_counter()
u,A,r,s,t=S.symbols('u A r s t');a=S.Integer(1);b=u/2;c=-u/2
one=S.Matrix([1,0,1,1]);K=S.Matrix([[0,0,1,-1],[0,A,r,s],[1,r,0,t],[-1,s,t,0]])
def mul(x,y):return S.Matrix([x[0]*y[0],x[0]*y[1]+x[1]*y[0],x[2]*y[2],x[3]*y[3]])
def tau(x):return a*x[0]+x[1]+b*x[2]+c*x[3]
def dk(x):return S.Matrix([tau(mul(K.row(i),x)) for i in range(4)])
d=dk(one);F=tau(d)/2
def P(x):
 z=x-tau(x)*one
 return tau(mul(mul(z,z),z))/2
def N(x):return tau(mul(d-F*one,mul(x,x)))/2-tau(x)*tau(mul(d,x))+F*tau(x)**2+tau(mul(x,dk(x)))/4
evec=S.Matrix([tau(mul(K.row(0),K.row(0))),2*tau(mul(K.row(0),K.row(1))),tau(mul(K.row(2),K.row(2))),tau(mul(K.row(3),K.row(3)))])
E=[S.factor(z) for z in evec-2*dk(d)-2*mul(d,d)+4*F*d]
j=S.symbols('j');pj=P(K.row(0).T+j*K.row(1).T);nj=N(K.row(0).T+j*K.row(1).T)
Ps=[pj.subs(j,0),S.diff(pj,j).subs(j,0),P(K.row(2).T),P(K.row(3).T)]
Ns=[nj.subs(j,0),S.diff(nj,j).subs(j,0),N(K.row(2).T),N(K.row(3).T)]
def eq(x,y):assert S.cancel(x-y)==0
def sf(seq,sub):return [S.factor(z.subs(sub,simultaneous=True)) for z in seq]
X,v,T,w,e=S.symbols('X v T w e')
chart={r:X+(v-1)/2+u*t/2,s:X+(1-v)/2-u*t/2,A:X-u*v-u*u*t/2}
EC=sf(E,chart);PC=sf(Ps,chart);NC=sf(Ns,chart)
eq(EC[0],0)
SP=S.factor(PC[0]+PC[1]+b*PC[2]+c*PC[3]-2*(NC[0]+NC[1]+b*NC[2]+c*NC[3]))
C0=S.factor(3*PC[0]*NC[1]-2*NC[0]*PC[1])
def ev(expr):
 nu,de=S.fraction(S.factor(expr))
 def cv(poly):
  po=S.Poly(poly,u);assert all(mm[0]%2==0 for mm,co in po.terms())
  return sum(co*e**(mm[0]//2) for mm,co in po.terms())
 return S.factor(cv(nu)/cv(de))
sub={X:T/u,t:w/u}
Ep=e*ev((EC[2]+EC[3]).subs(sub,simultaneous=True))
Em=e*ev(((EC[2]-EC[3])/u).subs(sub,simultaneous=True))
MM=e*ev(EC[1].subs(sub,simultaneous=True))
SS=ev((SP/u).subs(sub,simultaneous=True));CC=ev(C0.subs(sub,simultaneous=True))
B=v*v+v*w-w+1;D=v-w+1;H=5*v*w-2*v+w*w-5*w+4
eq(Ep,-e*B);eq(Em,-2*D*(T-e)-w*w)
eq(B.subs(w,v+1),2*v*v)
eq(Em.subs({v:0,w:1}),-1)
T0=e-w*w/(2*D)
M0,S0,Cz=[S.factor(z.subs(T,T0)) for z in [MM,SS,CC]]
def nr(ex):return S.fraction(S.factor(ex))[0]
eq(S.rem(nr(M0),B,v),-w*w*(e*H-w*w))
eq(S.rem(nr(S0),B,v).subs(w,0),8*e*(v-1))
res=[];remainders=[]
for val in [S0,Cz]:
 nv=nr(val.subs(e,w*w/H))
 rr=S.factor(S.rem(nv,B,v));remainders.append(rr)
 res.append(S.factor(S.resultant(B,rr,v)))
eq(res[0],-64*(w-1)**4*(w**4+4*w**3-12*w*w+8*w-2))
Q8=2*w**8+14*w**7-78*w**6-503*w**5+402*w**4+2112*w**3-3750*w*w+2282*w-490
eq(res[1],-288*w**8*(w-1)**4*Q8)
eq(S.Poly(S.gcd(*res),w).monic().as_expr(),(w-1)**4)
eq(B.subs(w,1),v*(v+1));eq(D.subs(w,1),v)
eq(remainders[0].subs(w,1),4*v)
print(json.dumps({'schema':'r150-unit211-opposite-zero-total-20261126-v1','status':'all_exact_QQ_checks_pass','scope':'p=1,q=-1,b+c=0,b-c nonzero; complete original mean and zero-point conditions','sourceSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'resultantDegrees':[S.degree(rr,w) for rr in res],'monicGcd':'(w-1)^4','ordinaryISPClaim':False,'elapsedSeconds':round(time.perf_counter()-started,6),'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},sort_keys=True,default=int))
