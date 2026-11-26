#!/usr/bin/env python3
"""Original QQ verification for q=-1, b+c=1/2, b-c!=0.
Uses the isolated-zero mean and highest equations, including all mean fibers.
"""
import hashlib,json,resource,time
from pathlib import Path
import sympy as S
started=time.perf_counter()
u,A,r,s,t=S.symbols('u A r s t')
b=(1+2*u)/4;c=(1-2*u)/4;a=S.Rational(1,2)
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
def sf(seq,sub):return [S.factor(z.subs(sub,simultaneous=True)) for z in seq]
def eq(x,y):assert S.cancel(x-y)==0

def cons(Ps,Ns):
 nb=a*Ns[0]+Ns[1]+b*Ns[2]+c*Ns[3]
 sp=a*Ps[0]+Ps[1]+b*Ps[2]+c*Ps[3]-2*nb
 return S.factor(sp),S.factor(3*Ps[0]*Ns[1]-2*Ns[0]*Ps[1]),S.factor(2*Ns[0]**3-nb*Ps[0]**2)

# E0 solved using only u!=0. These remaining mean identities exhaust the chart.
X,v,T,w=S.symbols('X v T w')
ff=X/2+u/2+v/(8*u)
chart={r:X+v/2-c*t,s:X-v/2-b*t,A:2*ff-X-u*(v+1)+2*b*c*t,t:t}
EC=sf(E,chart)
eq(EC[0],0)
Ep=S.factor(u*u*(EC[2]+EC[3]).subs({X:T/u,t:w/u},simultaneous=True))
Em=S.factor(u*(EC[2]-EC[3]).subs({X:T/u,t:w/u},simultaneous=True))
Elast=S.factor(u*u*EC[1].subs({X:T/u,t:w/u},simultaneous=True))
eq(2*Ep+Em,-2*(u*u-S.Rational(1,4))*(v-1)*(v+w))
eq(Ep.subs(w,-v),2*v*(T-u*u+v/4))
eq(Ep.subs(v,1),(1-w)*(T-u*u)+w*w/2)
eq(Elast.subs({v:1,T:u*u-w*w/(2*(1-w))},simultaneous=True),-(4*u*u-1)*(w+1)*(w*w+2*w-1)/(8*(w-1)))
eq(Elast.subs({w:-v,T:u*u-v/4},simultaneous=True),0)

# v=w=0: X is retained, not divided out.
zero={A:0,r:X,s:X,t:0}
pz,nz=sf(Ps,zero),sf(Ns,zero)
Sz,Cz,Gz=cons(pz,nz)
eq(Cz,-3*X*X*(4*u*u-1)**2/32)
eq(pz[0],u*(4*u*u-1)/4)
assert sf([pz[1],pz[2],pz[3]],{X:0})==[0,0,0]

# w=-v, v!=0: the genuine original mean family.
family={A:t*(4*u*u-1)/8,r:u,s:u,t:t}
assert sf(E,family)==[0,0,0,0]
pf,nf=sf(Ps,family),sf(Ns,family)
SS,CC,GG=cons(pf,nf)
eq(SS,t*(4*u*u-1)*(t*t*(4*u*u-1)-12)/128)
eq(CC,3*(4*u*u-1)**2*(t*t*(4*u*u-1)+4*t*u*(4*u*u-1)-16*u*u)/512)
ee=S.symbols('ee')
eq((4*ee-3)**2-12*ee*(4*ee-1),-(8*ee-3)*(4*ee+3))
for ev,tt,want in [(S.Rational(3,8),-3/u,-S.Rational(135,65536)),(-S.Rational(3,4),3/(2*u),S.Rational(1431,2048))]:
    expr=S.factor(u**3*GG.subs(t,tt)-want)
    assert S.rem(S.fraction(expr)[0],u*u-ev,u)==0

# v=1, w!=-1: retain both roots of Qw and all allowed u.
Qw=w*w+2*w-1
TT=u*u-w*w/(2*(1-w));XX=TT/u;tt=w/u;ff=(TT+u*u+S.Rational(1,4))/(2*u)
case={r:XX+S.Rational(1,2)-c*tt,s:XX-S.Rational(1,2)-b*tt,t:tt,A:2*ff-XX-2*u+2*b*c*tt}
pv,nv=sf(Ps,case),sf(Ns,case)
Sv,Cv,_=cons(pv,nv)
Sr=S.factor(S.rem(S.fraction(S.factor(Sv))[0],Qw,w))
Cr=S.factor(S.rem(S.fraction(S.factor(Cv))[0],Qw,w))
eq(Sr,4*(4*u*u-1)*(8*u*u*w-4*u*u-5*w+2))
eq(Cr,6*(4*u*u-1)**3*(8*u*u*w-4*u*u-w+1))
assert Qw.subs(w,S.Rational(1,4))==-S.Rational(7,16)

# General, division-free source of the new scalar conditions.
ba,ca=S.symbols('ba ca');aa=1-ba-ca
U0,U1,UB,UC=S.symbols('U0 U1 UB UC');m=aa*U0+U1+ba*UB+ca*UC
u2=aa*U0*U0+2*U0*U1+ba*UB*UB+ca*UC*UC
u3=aa*U0**3+3*U0*U0*U1+ba*UB**3+ca*UC**3
PU=(u3-3*m*u2+2*m**3)/2
Svalue=-u3+2*m*u2
eq(Svalue+2*PU+m*(u2-2*m*m),0)
print(json.dumps({'schema':'r150-unit211-opposite-half-total-20261126-v1','status':'all_exact_QQ_checks_pass','scope':'p=1,q=-1,b+c=1/2,b-c nonzero; both complete mean families and every singular fiber','sourceSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'nonzeroFamilyNormReadouts':['-135/65536','1431/2048'],'ordinaryISPClaim':False,'elapsedSeconds':round(time.perf_counter()-started,6),'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},sort_keys=True))
