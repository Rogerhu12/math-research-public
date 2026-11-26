#!/usr/bin/env python3
"""Exact original P1 line and complete no-zero-line cover on S=Af=0.
This is a coordinate/cover lemma, not an exclusion of the whole S layer.
"""
import hashlib,json,resource,time
from pathlib import Path
import sympy as sp
started=time.perf_counter()
b,c,p,q,A1,r,s,t,f,lam,w=sp.symbols('b c p q A1 r s t f lam w')
a=1-b-c;u=b*p+c*q;V2=b*p*p+c*q*q;V3=b*p**3+c*q**3
Q=p*q;Psum=p+q;T0=V2-2*u*u
P02=V3-3*u*V2+2*u**3
def zero(x):assert sp.expand(x)==0
one=[1,0,1,1];k0=[0,0,p,q];k1=[0,A1,r,s]
def add(x,y):return [a+b for a,b in zip(x,y)]
def scale(a,x):return [a*v for v in x]
def mul(x,y):return [x[0]*y[0],x[0]*y[1]+x[1]*y[0],x[2]*y[2],x[3]*y[3]]
def tau(x):return a*x[0]+x[1]+b*x[2]+c*x[3]
v0=add(k0,scale(-tau(k0),one));v1=add(k1,scale(-tau(k1),one))
Bjet=tau(mul(mul(v0,v0),v1))
Cp=p*p-2*p*u-T0;Cq=q*q-2*q*u-T0
zero(Bjet-(-T0*A1+b*Cp*r+c*Cq*s))
# Clear the same global E0/N0 graph without any rational expansion.
den=2*b*c*p*q*(q-p)
W12=T0+4*f*u
W2=u*T0+f*(V2+2*u*u)-b*c*p*q*t+lam*P02
XD=c*q*(q*W12-2*W2)
YD=b*p*(2*W2-p*W12)
AD=2*f*den-2*b*XD-2*c*YD+2*b*c*t*den
rD=XD-a*p*den-c*t*den;sD=YD-a*q*den-b*t*den
lineD=-T0*AD+b*Cp*rD+c*Cq*sD-w*P02*den
# The unscaled line is (2/3)P1-2wP0=0.
lfQ=T0*((b+c-1)*Q+u*(Psum-2*u))
lt=b*c*(T0+2*u*Psum-Psum**2+Q)
lc2Q=T0*T0*(Psum-2*u)+2*P02*(lam*(Q-T0)-Q*(a+w))
zero(2*Q*lineD-den*(2*lfQ*f+2*Q*lt*t+lc2Q))
# Exact symmetric specialization and all simultaneous coefficient zeros.
uu,ll,QQ,z,ss,TT=sp.symbols('u l Q z s T')
R=3-4*lam;Al=2*lam**2-2*lam+1;Cl=-4*lam**2+5*lam-2
Tn=2*uu-ll*QQ-2*uu*uu
Af=QQ*R-z*(ll*QQ+2*uu*(1-uu))
lf=sp.expand(z*Tn*((ll-1)*QQ+2*uu*(1-uu))-QQ*Tn*(R-z))
zero(lf+Tn*Af)
# If z=R, Af=0 and the t coefficient zero give u=l=1, then P0=0.
Az=2*uu*(1-uu)-QQ*(1-ll)
Tz=2*QQ*(1-ll)+4*uu-4
zero(Tz+2*Az+4*(uu-1)**2)
P02n=(2-3*uu)*(2*uu-ll*QQ)-QQ*uu+2*uu**3
zero(P02n.subs({uu:1,ll:1}))
# If T0=0, the t coefficient gives Q=4(1-u), hence u=2l.
zero(Tn.subs(QQ,4*(1-uu))-2*(1-uu)*(uu-2*ll))
# On T0=0, P1 constant demands T=-l; Af then gives R=-2C.
zero(R+2*Cl+(4*lam-1)*(2*lam-1))
# lambda=1/2 gives a value collision. lambda=1/4 gives the displayed
# unique parameters, whose original moment discriminant is nonzero.
values={lam:sp.Rational(1,4),z:sp.Rational(20,13),ll:sp.Rational(13,20),uu:sp.Rational(13,10),QQ:-sp.Rational(6,5),ss:-sp.Rational(5,2),TT:-sp.Rational(13,20)}
zero((z*(Al-Cl)-ss*Cl).subs(values))
zero((ll*z+Cl).subs(values))
zero(Af.subs(values))
discriminant=(1-QQ)*(2*TT-ll*ss)**2-(ll-uu)**2*(ss*ss-4*z)
actual=sp.factor(discriminant.subs(values))
assert actual==sp.Rational(9971,52000) and actual!=0
# The divided identity has value 59/130; division by l is paid by
# P0 != 0, since on T0=0 one has 2P0=Q*u*(2l-1), u=2l.
zero((P02n-QQ*uu*(2*ll-1)).subs(QQ,2*uu*(1-uu)/ll))
assert sp.factor(actual/values[ll]**2)==sp.Rational(59,130)
halfvals={lam:sp.Rational(1,2),z:1,ss:-2}
zero((ss*ss-4*z).subs(halfvals))
print(json.dumps({'schema':'r150-unit211-original-P1-line-S0-cover-v1','status':'all_exact_original_line_and_exception_checks_pass','sourceSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'S0Af0LineNeverIdenticallyZeroOnOriginalSolutions':True,'quarterLambdaOriginalMomentDiscriminant':str(actual),'claimS0LayerEmpty':False,'claimLambdaLayerEmpty':False,'ordinaryISPClaim':False,'elapsedSeconds':round(time.perf_counter()-started,6),'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},sort_keys=True))
