#!/usr/bin/env python3
"""QQ verification: p=1,q=-1,b=c in the original unit 2+1+1 branch.
Includes the original highest equation at the isolated zero point.
"""
import hashlib,json,resource,time
from pathlib import Path
import sympy as S
start=time.perf_counter()
c,A,r,s,t=S.symbols('c A r s t')
a=1-2*c
one=S.Matrix([1,0,1,1])
K=S.Matrix([[0,0,1,-1],[0,A,r,s],[1,r,0,t],[-1,s,t,0]])
def mul(x,y):return S.Matrix([x[0]*y[0],x[0]*y[1]+x[1]*y[0],x[2]*y[2],x[3]*y[3]])
def tau(x):return a*x[0]+x[1]+c*x[2]+c*x[3]
def dk(x):return S.Matrix([tau(mul(K.row(j),x)) for j in range(4)])
d=dk(one);F=tau(d)/2

def P(x):
    z=x-tau(x)*one
    return tau(mul(mul(z,z),z))/2

def N(x):return tau(mul(d-F*one,mul(x,x)))/2-tau(x)*tau(mul(d,x))+F*tau(x)**2+tau(mul(x,dk(x)))/4

e=S.Matrix([tau(mul(K.row(0),K.row(0))),2*tau(mul(K.row(0),K.row(1))),tau(mul(K.row(2),K.row(2))),tau(mul(K.row(3),K.row(3)))])
E=[S.factor(v) for v in e-2*dk(d)-2*mul(d,d)+4*F*d]
j=S.symbols('j')
pj=P(K.row(0).T+j*K.row(1).T);nj=N(K.row(0).T+j*K.row(1).T)
Ps=[pj.subs(j,0),S.diff(pj,j).subs(j,0),P(K.row(2).T),P(K.row(3).T)]
Ns=[nj.subs(j,0),S.diff(nj,j).subs(j,0),N(K.row(2).T),N(K.row(3).T)]
def sf(seq,sub):return [S.factor(v.subs(sub,simultaneous=True)) for v in seq]
def eq(x,y):assert S.cancel(x-y)==0
x,f,V=S.symbols('x f V')
# E0 gives y=x-1; P0=0 gives U0=0; its jet P1=0 gives this f.
sub={r:V+S.Rational(1,2)-(1-2*c)-c*t,s:V-S.Rational(1,2)+(1-2*c)-c*t,A:2*((2*c+1)*V-c*t)/2-2*c*(2*V)+2*c*c*t}
EE=sf(E,sub);PP=sf(Ps,sub);NN=sf(Ns,sub)
assert PP[0]==PP[1]==0
expected=[0,2*V*V-4*V*c*t+2*c*c*t*t+4*c*c-c,
 (8*V*V*c-8*V*c*t+4*V*c-2*V+2*c*t*t+4*c-1)/2,
 (8*V*V*c-8*V*c*t-4*V*c+2*V+2*c*t*t+4*c-1)/2]
for u,v in zip(EE,expected):eq(u,v)
eq(NN[0],-V*c*(2*c-1)/2)
eq(NN[1],c*(2*c-1)*(-(4*c+1)*V+2*c*t)/2)
assert sf(PP,{c:S.Rational(1,4),V:0,t:0})==[0,0,0,0]
assert sf(NN,{c:S.Rational(1,4),V:0,t:0})==[0,0,0,0]

# The zero-point highest identity is valid without division, in full weights.
aa,bb,cc=S.symbols('aa bb cc')
U0,U1,UB,UC=S.symbols('U0 U1 UB UC')
aa=1-bb-cc
m=aa*U0+U1+bb*UB+cc*UC
PU=((aa*U0**3+3*U0**2*U1+bb*UB**3+cc*UC**3)-3*m*(aa*U0**2+2*U0*U1+bb*UB**2+cc*UC**2)+2*m**3)/2
ps=[-U0**3,-3*U0**2*U1,-UB**3,-UC**3]
ns=[-m*U0**2,-2*m*U0*U1,-m*UB**2,-m*UC**2]
J=aa*ps[0]+ps[1]+bb*ps[2]+cc*ps[3]-3*(aa*ns[0]+ns[1]+bb*ns[2]+cc*ns[3])
eq(2*PU,2*m**3-J)

# c=1/2, i=2V-t, with the exact mean relation i^2+1=0.
i=S.symbols('i')
subhalf={c:S.Rational(1,2),V:(t+i)/2}
def rem(v):
    num,den=S.fraction(S.factor(v))
    return S.factor(S.rem(num,i*i+1,i)/den)
Ph=[rem(v) for v in sf(PP,subhalf)]
Nh=[rem(v) for v in sf(NN,subhalf)]
for lhs,rhs in zip(Ph,[0,0,-(2*i+3*t-2)/4,-(2*i+3*t+2)/4]):eq(lhs,rhs)
for j in [2,3]:eq(Nh[j],Ph[j]/2)
for v in sf(EE,subhalf):assert rem(v)==0
Jh=S.factor((Ph[2]+Ph[3]-3*Nh[2]-3*Nh[3])/2)
eq(Jh,(2*i+3*t)/8)
new=[S.fraction(rem(2*Nh[j]**3+Jh*Ph[j]**2))[0] for j in [2,3]]
G=S.groebner([i*i+1,*new],t,i,domain=S.QQ)
assert list(G)==[t*t+4*i*t/3-S.Rational(8,9),i*i+1]
assert G.reduce((3*t+2*i)**2-4)[1]==0
for value in [-2,2]:
    tt=(value-2*i)/3
    assert [S.factor(v.subs(t,tt)) for v in Ph[2:]]==[-S.Rational(value-2,4),-S.Rational(value+2,4)]
print(json.dumps({'schema':'r150-unit211-opposite-zero-mean-20261126-v1','status':'all_exact_QQ_checks_pass','scope':'p=1,q=-1,b=c nonzero; both weight branches and both zero-point-highest fibers','sourceSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'halfFiber':'(3t+2i)^2=4, i^2=-1','ordinaryISPClaim':False,'elapsedSeconds':round(time.perf_counter()-start,6),'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},sort_keys=True))
