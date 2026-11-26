#!/usr/bin/env python3
"""Small exact factor ledger supplement; no large resultant is rerun."""
import hashlib,json,resource,time
from pathlib import Path
started=time.perf_counter()
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
def norms(P,N,aa,bb,cc):
 P0,P1,PB,PC=P;N0,N1,NB,NC=N
 return [3*P0*N1-2*N0*P1,3*N0*NB*NC-(3*aa*P0+P1)*NB*NC-3*bb*PB*N0*NC-3*cc*PC*N0*NB,N0**3*PB**2-NB**3*P0**2,N0**3*PC**2-NC**3*P0**2,NB**3*PC**2-NC**3*PB**2]

x,f=S.symbols('x f')
bb=-c*q;aa=1-bb-c;yy=x+(q-1)/2
sub={p:1,b:bb,c:c,q:q,r:x-aa-c*t,s:yy-aa*q-bb*t,A:2*f-2*bb*x-2*c*yy+2*bb*c*t}
EC=subfac(E,sub);rawP=subfac(Ps,sub);rawN=subfac(Ns,sub)
def num(v):return S.fraction(S.factor(v))[0]
qq=x*(1-2*x)/(x-1);Fa=2*x*x-2*x+1;Q2=2*x*x-4*x+1
Tx=-(4*x**4-4*x**3-2*x+1)/((x-1)*Q2)
ffD=S.factor(-EC[2].subs({q:qq,t:Tx,f:0},simultaneous=True)/(4*(x-1)))
ED=num(EC[1].subs({q:qq,t:Tx,f:ffD},simultaneous=True))
unit,fac=S.factor_list(ED)
keep=[(fi,mult) for fi,mult in fac if S.degree(fi,c)>0]
drop=[(fi,mult) for fi,mult in fac if S.degree(fi,c)==0]
assert len(keep)==1 and keep[0][1]==1 and S.degree(keep[0][0],c)==2
assert drop==[(Fa,1)]
assert S.expand(ED-unit*S.prod(fi**mult for fi,mult in fac))==0
Drecord={'unit':str(unit),'removed':[[str(fi),mult] for fi,mult in drop],'retainedDegreeC':2}
H=2*t*t-3*(q+1)*t+(q-1)**2
ch=-(q-1)/(2*H);fh=t*(q*q-q*t+4*q-t+1)/(4*H)
caseh={x:S.Rational(1,2),c:ch,f:fh}
PP,NN=subfac(rawP,caseh),subfac(rawN,caseh)
J=S.factor((1+ch*(q-1))*PP[0]+PP[1]-ch*q*PP[2]+ch*PP[3]-3*((1+ch*(q-1))*NN[0]+NN[1]-ch*q*NN[2]+ch*NN[3]))
vals=[S.factor(EC[1].subs(caseh,simultaneous=True)),S.factor(3*PP[0]*NN[1]-2*NN[0]*PP[1]),S.factor(2*NN[0]**3+J*PP[0]**2)]
expected=[t*(q+1),3*q*q*t*(q-1)**4*(q+1),q**3*t*(q-1)**6*(q+1)**2]
denexpected=[2*H**2,64*H**4,2048*H**6]
hrecord=[]
for idx,val in enumerate(vals):
    numerator,denominator=S.fraction(val)
    assert S.cancel(denominator/denexpected[idx])==1
    unit,fac=S.factor_list(numerator)
    keep=[(fi,mult) for fi,mult in fac if S.degree(fi,t)>1]
    drop=[(fi,mult) for fi,mult in fac if S.degree(fi,t)<=1]
    assert len(keep)==1 and keep[0][1]==1
    assert S.degree(keep[0][0],t)==[3,3,6][idx]
    gone=S.factor(unit*S.prod(fi**mult for fi,mult in drop))
    assert S.expand(gone-expected[idx])==0
    assert S.expand(numerator-gone*keep[0][0])==0
    hrecord.append({'removedProduct':str(gone),'retainedDegreeT':int(S.degree(keep[0][0],t))})
print(json.dumps({'schema':'r150-unit211-zero-base-mean-factor-ledger-20261126-v1','status':'all_exact_QQ_checks_pass','sourceSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'singularD':Drecord,'xhalf':hrecord,'largeResultantsRerun':False,'elapsedSeconds':round(time.perf_counter()-started,6),'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},sort_keys=True))
