#!/usr/bin/env python3
"""Original unit211: q=p nonzero, b+c=1/2 or 1, with zero-point highest condition.
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
# l=1/2. No division by r-s, by P_B, or by the mean m.
chalf=S.Rational(1,2)-b;betah=b*chalf
half={c:chalf}
eq(sub(E[0],half),A-2*betah*t)
eq(sub(Ps[0],half));eq(sub(Ps[1],half))
eq(sub(Ns[0],{c:chalf,A:2*betah*t}),betah*t/2)
eq(sub(2*(b*E[2]+c*E[3]),{c:chalf,A:0,t:0}),-8*betah*(r-s)**2)
hfinal={c:chalf,A:0,t:0,r:V,s:V};pval=V*V*(2*V-3)/2
assert seq(E,hfinal)==[0,0,0,0]
for lhs,rhs in zip(seq(Ps,hfinal),[0,0,pval,pval]):eq(lhs,rhs)
for lhs,rhs in zip(seq(Ns,hfinal),[0,0,pval/2,pval/2]):eq(lhs,rhs)
eq(sub(J,hfinal),-pval/4)
# l=1: P1=0 first forces A=0, then E0 fixes the weighted first jet.
cone=1-b;beta=b*cone;delta=2*b-1
unit={c:cone}
eq(sub(Ps[0],unit));eq(sub(Ps[1],unit),3*A/2)
eq(sub(E[0],unit),2*A+2*(b*r+cone*s)-1)
chart={c:cone,A:0,r:S.Rational(1,2)+cone*h,s:S.Rational(1,2)-b*h}
EU=seq(E,chart);PU=seq(Ps,chart);NU=seq(Ns,chart)
eq(EU[0]);eq(PU[0]);eq(PU[1]);eq(NU[0])
eq(NU[1],-beta*delta*h*t/2)
eq(EU[1],2*beta*delta*h*t-2*beta*h*h-S.Rational(1,2))
eq(EU[2].subs(t,0),-2*cone*cone*h*h-S.Rational(1,2))
eq(EU[3].subs(t,0),-2*b*b*h*h-S.Rational(1,2))
# Entire surviving abstract mean surface: b=c=1/2, h^2=-1, arbitrary t.
def red(v):
 n,dd=S.fraction(S.factor(v));return S.factor(S.rem(n,h*h+1,h)/dd)
fiber={b:S.Rational(1,2)}
PP=[red(v.subs(fiber)) for v in PU];NN=[red(v.subs(fiber)) for v in NU]
assert all(red(v.subs(fiber))==0 for v in EU)
H=3*t-2;target=[0,0,-(H+2*h)/4,-(H-2*h)/4]
for lhs,rhs in zip(PP,target):eq(lhs,rhs)
for i in range(4):eq(NN[i],PP[i]/2)
JJ=red(sub(J,chart).subs(fiber));eq(JJ,H/8)
norms=[red(2*NN[i]**3+JJ*PP[i]**2) for i in [2,3]]
Q=9*t*t-12*t+8
for val,sgn in zip(norms,[1,-1]):eq(val,(H+sgn*2*h)*Q/256)
eq(norms[0]-norms[1],h*Q/64)
eq(H*H+4,Q)
for sign in [1,-1]:
 tt=(2+sign*2*h)/3;pp=[red(v.subs(t,tt)) for v in PP[2:]]
 expected=[-h,0] if sign==1 else [0,h]
 for x,y in zip(pp,expected):eq(x,y)
signal.alarm(0)
print(json.dumps({'schema':'r150-unit211-equal-half-or-unit-weight-20261126-v1','status':'all_exact_QQ_checks_pass','sourceSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'p=q nonzero and b+c in {1/2,1}; original mean and zero-point highest identity','halfWeightAbstractFamily':'A=t=0,r=s=V; P_B=P_C=V^2(2V-3)/2, N_i=P_i/2','unitWeightAbstractFamily':'b=c=1/2,A=0,r=(1+h)/2,s=(1-h)/2,h^2=-1','unitWeightZeroPointFibers':'3t-2=+2h or -2h','allPhysicalExclusions':'U0=U1=0 and A=0 force forbidden isotropic 2+1 physical jets','ordinaryISPClaim':False,'elapsedSeconds':round(time.monotonic()-started,6),'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},sort_keys=True))
