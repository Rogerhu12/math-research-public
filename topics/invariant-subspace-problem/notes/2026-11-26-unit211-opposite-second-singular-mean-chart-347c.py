#!/usr/bin/env python3
"""Original QQ checks for q=-1,D2=0,D1!=0; l=0,1/2 are already closed."""
import hashlib,json,resource,time
from pathlib import Path
import sympy as S
from flint import fmpq_mpoly_ctx,fmpq
started=time.perf_counter()
u,l,A,r,s,t=S.symbols('u l A r s t');a=1-l;b=(l+u)/2;c=(l-u)/2
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
x=X+(v+1)/2;y=X-(v+1)/2;ff=X/2+u/2+l*v/(4*u)
chart={r:x-a-c*t,s:y+a-b*t,A:2*ff-2*b*x-2*c*y+2*b*c*t}
EC=sf(E,chart);PC=sf(Ps,chart);NC=sf(Ns,chart);eq(EC[0],0)
SP=S.factor(a*PC[0]+PC[1]+b*PC[2]+c*PC[3]-2*(a*NC[0]+NC[1]+b*NC[2]+c*NC[3]))
C0=S.factor(3*PC[0]*NC[1]-2*NC[0]*PC[1])
def ev(expr):
 nu,de=S.fraction(S.factor(expr))
 def cv(poly):
  po=S.Poly(poly,u);assert all(mm[0]%2==0 for mm,co in po.terms())
  return sum(co*e**(mm[0]//2) for mm,co in po.terms())
 return S.factor(cv(nu)/cv(de))
sub={X:T/u,t:w/u}
Ep=S.factor(e*ev((EC[2]+EC[3]).subs(sub,simultaneous=True)))
Em=S.factor(e*ev(((EC[2]-EC[3])/u).subs(sub,simultaneous=True)))
MM=S.factor(e*ev(EC[1].subs(sub,simultaneous=True)))
SS=ev((SP/u).subs(sub,simultaneous=True));CC=ev(C0.subs(sub,simultaneous=True))
B=v*v+v*w-w+1;D1=-2*l+v-w+1;D2=-2*l*(v+1)+B
eq(D2.subs(v,-1),2*(1-w))
eq(Ep.subs({v:-1,w:1}),l*(-4*T+4*e+1))
eq(Em.subs({v:-1,w:1}),(4*l+2)*(T-e)-1)
l2=B/(2*(v+1));T2=e-w*w/(2*(v-w))
eq(D1.subs(l,l2),2*v*(1-w)/(v+1))
eq(2*l2-1,(v-1)*(v+w)/(v+1))
eq(Ep.subs(l,l2),l2*(2*(v-w)*(T-e)+w*w))
K2=v**3-v*w*w-v*w+v-w*w-w
eq(Em.subs({l:l2,T:T2},simultaneous=True),(v-1)*(v+w)*K2/(2*(v+1)*(v-w)))
M2,S2,C2=[S.factor(z.subs({l:l2,T:T2},simultaneous=True)) for z in [MM,SS,CC]]
def nr(ex):return S.fraction(S.factor(ex))[0]
def remnum(ex):return nr(S.rem(nr(ex),K2,w))
MR,SR,CR=map(remnum,[M2,S2,C2])
ctx=fmpq_mpoly_ctx.get(('e','w','v'),'lex')
def fp(ex):return ctx.from_dict({mm:fmpq(str(co)) for mm,co in S.Poly(ex,e,w,v,domain=S.QQ).terms()})
mp,sp,cp,kp=map(fp,[MR,SR,CR,K2])
rms=mp.resultant(sp,'e');rmc=mp.resultant(cp,'e')
rs=rms.resultant(kp,'w');rc=rmc.resultant(kp,'w')
def degree(po,i):return max(mm[i] for mm in po.to_dict())
assert [degree(rs,2),degree(rc,2)]==[54,89]
gg=rs.gcd(rc);want=fp(v**23*(v-1)**4*(v+1)**8*(v*v+1)**8)
assert gg/gg.leading_coefficient()==want/want.leading_coefficient()
eq(S.rem(K2,v*v+1,v),-(v+1)*w*(w+1))
eq(S.rem(nr(M2.subs(w,-1)),v*v+1,v),-16*e*(v+1))
print(json.dumps({'schema':'r150-unit211-opposite-second-singular-mean-20261126-v1','status':'all_exact_QQ_checks_pass','scope':'p=1,q=-1,u nonzero,D2=0,D1 nonzero; l=0,1/2 referenced from prior exclusions','sourceSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'resultantDegrees':[54,89],'gcdFactors':[['v',23],['v-1',4],['v+1',8],['v^2+1',8]],'ordinaryISPClaim':False,'elapsedSeconds':round(time.perf_counter()-started,6),'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},sort_keys=True))
