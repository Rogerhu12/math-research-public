#!/usr/bin/env python3
"""Original unit211: equal nonzero base pairings, t=0, and the original zero-point mean/highest identity.
AI-assisted GPT-6 Astra Pro / Astra-ISP-347c-20261126. All identities over QQ.
"""
import hashlib,json,resource,signal,time
from pathlib import Path
import sympy as S
started=time.monotonic();resource.setrlimit(resource.RLIMIT_AS,(1024*1024**2,)*2)
def timeout(*args):raise TimeoutError('180-second exact certificate budget')
signal.signal(signal.SIGALRM,timeout);signal.alarm(180)
b,c,A,r,s,t,h,V,j=S.symbols('b c A r s t h V j');a=1-b-c
one=S.Matrix([1,0,1,1]);K=S.Matrix([[0,0,1,1],[0,A,r,s],[1,r,0,t],[1,s,t,0]])
def mul(x,y):return S.Matrix([x[0]*y[0],x[0]*y[1]+x[1]*y[0],x[2]*y[2],x[3]*y[3]])
def tau(x):return a*x[0]+x[1]+b*x[2]+c*x[3]
def DK(x):return S.Matrix([tau(mul(K.row(i),x)) for i in range(4)])
d=DK(one);F=tau(d)/2
def P(x):
 w=x-tau(x)*one;return tau(mul(mul(w,w),w))/2
def N(x):return tau(mul(d-F*one,mul(x,x)))/2-tau(x)*tau(mul(d,x))+F*tau(x)**2+tau(mul(x,DK(x)))/4
e=S.Matrix([tau(mul(K.row(0),K.row(0))),2*tau(mul(K.row(0),K.row(1))),tau(mul(K.row(2),K.row(2))),tau(mul(K.row(3),K.row(3)))])
E=[S.expand(x) for x in e-2*DK(d)-2*mul(d,d)+4*F*d]
pj=P(K.row(0).T+j*K.row(1).T);nj=N(K.row(0).T+j*K.row(1).T)
Ps=[pj.subs(j,0),S.diff(pj,j).subs(j,0),P(K.row(2).T),P(K.row(3).T)]
Ns=[nj.subs(j,0),S.diff(nj,j).subs(j,0),N(K.row(2).T),N(K.row(3).T)]
def eq(x,y=0):assert S.cancel(x-y)==0
def sub(v,chart):return S.factor(v.subs(chart,simultaneous=True))
def seq(vs,chart):return [sub(v,chart) for v in vs]
J=a*Ps[0]+Ps[1]+b*Ps[2]+c*Ps[3]-3*(a*Ns[0]+Ns[1]+b*Ns[2]+c*Ns[3])
eq(Ps[0],(b+c)*(b+c-1)*(2*b+2*c-1)/2)
# The original zero-point mean tau(U^2)=2m^2 together with its
# highest equation supplies Sbar=Pbar-2Nbar=0, with no division.
U0,U1,UB,UC=S.symbols('U0 U1 UB UC');m=a*U0+U1+b*UB+c*UC
T2=a*U0**2+2*U0*U1+b*UB**2+c*UC**2
T3=a*U0**3+3*U0**2*U1+b*UB**3+c*UC**3
PU=(T3-3*m*T2+2*m**3)/2
Pbar=-T3;Nbar=-m*T2
eq(Pbar-2*Nbar,-2*PU-m*(T2-2*m*m))
Sbar=a*Ps[0]+Ps[1]+b*Ps[2]+c*Ps[3]-2*(a*Ns[0]+Ns[1]+b*Ns[2]+c*Ns[3])
l,Z,delta,beta,U,W=S.symbols('l Z delta beta U W');cc=l-b;X=l+V;hh=2*l-1
chart={c:cc,t:0,r:X+cc*Z/l-(1-l),s:X-b*Z/l-(1-l),A:(1-2*l)*(X-S.Rational(1,2))}
EC=seq(E,chart);Sb=sub(Sbar,chart)
BETA=b*(l-b);DELTA=2*b-l
Ew=S.factor((b*EC[2]+cc*EC[3])/l)
eq(EC[0]);eq(Ew,-2*BETA*Z*Z/l**2+V*hh)
eq(EC[1]-l*Ew,-2*hh*(V-S.Rational(1,2))*(V+l-S.Rational(1,2)))
eq(EC[2]-EC[3],Z*(2*DELTA*Z-l*(2*V+2*l-1))/l)
# Invariants beta=bc,U=Z^2,W=(b-c)Z. The substitution is rechecked
# against the original rational expression, not assumed as a free model.
expr=S.cancel(Sb.subs(b,(l+delta)/2));num,den=S.fraction(expr);assert not den.has(delta,Z)
inv=0
for (i,jj),co in S.Poly(num,delta,Z).terms():
 assert i%2==jj%2
 inv+=co*(l*l-4*beta)**(i//2)*U**(jj//2)*W**(i%2)
inv=S.factor(inv/den)
eq(inv.subs({beta:BETA,U:Z*Z,W:DELTA*Z},simultaneous=True),Sb)
first={V:S.Rational(1,2),U:l*l*hh/(4*beta),W:l*l}
second={V:S.Rational(1,2)-l,U:-hh*hh,W:0,beta:l*l/4}
eq(inv.subs(first,simultaneous=True),l*hh*hh/2)
eq(inv.subs(second,simultaneous=True),-l*(l-1)*hh*hh/2)
# The second branch uses W=0,Z!=0 -> delta=0 -> beta=l^2/4.
# The first branch does not divide by l^2+2l-1 or use its discriminant.
signal.alarm(0)
print(json.dumps({'schema':'r150-unit211-equal-base-zero-single-pairing-20261126-v1','status':'all_exact_QQ_checks_pass','sourceSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'p=q nonzero,t=0,l not 0,1/2,1; cited prior result covers those three l values','zeroPointMeanHighestIdentityVerified':True,'meanBranches':['V=1/2','V=1/2-l'],'originalSbarValues':['l(2l-1)^2/2','-l(l-1)(2l-1)^2/2'],'allInvariantIdentitiesRemultiplied':True,'ordinaryISPClaim':False,'elapsedSeconds':round(time.monotonic()-started,6),'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},sort_keys=True))
