#!/usr/bin/env python3
# Author: Astra-ISP-b2a9acde-20261120 / r150_structure; AI-assisted GPT-6 Astra Pro.
"""Supplement: exact QQ boundary and reverse-mean identities for unit 2+2.
This has no Groebner step and does not repeat the paid degree-24 certificate.
"""
import sympy as S
d,ss,tt,rr,j,k,e,h,beta=S.symbols("delta s t r j k e h beta")
one=S.Matrix([1,0,1,0])
def clean(x):return S.cancel(S.expand(x))
def eq(x,y=0):assert clean(x-y)==0,(x,y)
def amul(x,y):
    return S.Matrix([x[0]*y[0],x[0]*y[1]+x[1]*y[0],
                     x[2]*y[2],x[2]*y[3]+x[3]*y[2]])
def original(K,delta,local=False):
    a=(1+delta)/2;b=(1-delta)/2
    def tau(x):return a*x[0]+x[1]+b*x[2]+x[3]
    def DK(x):return S.Matrix([tau(amul(K.row(i).T,x)) for i in range(4)])
    dv=DK(one);F=tau(dv)/2
    rows=[K.row(i).T for i in range(4)]
    ev=S.Matrix([tau(amul(rows[0],rows[0])),
                 2*tau(amul(rows[0],rows[1])),
                 tau(amul(rows[2],rows[2])),
                 2*tau(amul(rows[2],rows[3]))])
    mean=[clean(x) for x in ev-2*DK(dv)-2*amul(dv,dv)+4*F*dv]
    if not local:return mean
    def cen(x):return x-tau(x)*one
    def P(x):
        z=cen(x);return clean(tau(amul(z,amul(z,z)))/2)
    def P1(x,v):return clean(3*tau(amul(amul(cen(x),cen(x)),cen(v)))/2)
    def N(x):return clean(tau(amul(dv-F*one,amul(x,x)))/2
                          -tau(x)*tau(amul(dv,x))+F*tau(x)**2
                          +tau(amul(x,DK(x)))/4)
    def N1(x,v):return clean(N(x+v)-N(x)-N(v))
    out=dict(p=P(K[:,0]),p1=P1(K[:,0],K[:,1]),
             q=P(K[:,2]),q1=P1(K[:,2],K[:,3]),
             n=N(K[:,0]),n1=N1(K[:,0],K[:,1]),
             o=N(K[:,2]),o1=N1(K[:,2],K[:,3]))
    out["ca"]=clean(3*out["p"]*out["n1"]-2*out["n"]*out["p1"])
    out["cb"]=clean(3*out["q"]*out["o1"]-2*out["o"]*out["q1"])
    return mean,out

# A=0 reverse mean classification; t=B-D.
B=(ss+tt)/2;D=(ss-tt)/2
KA=S.Matrix([[0,0,0,B],[0,j-e,D,e],
             [0,D,0,0],[B,e,0,-d*tt-j-e]])
ma=original(KA,d)
eq(ma[0]);eq(ma[2])
eq(ma[1]+ma[3],-8*j*tt+2*d*ss*tt-4*d*tt**2)
eq(ma[1]-ma[3],4*e*tt+2*d*tt**2)
Keq=S.Matrix([[0,0,0,beta],[0,j-e,beta,e],
              [0,beta,0,0],[beta,e,0,-j-e]])
me,ve=original(Keq,d,True)
for x in me:eq(x)
eq(ve["p"],beta**3);eq(ve["q"],beta**3)
eq(ve["n"]);eq(ve["o"])
eq(ve["n1"],beta**2*(j-(1+d)*beta/2))
eq(ve["o1"],beta**2*(-j-(1-d)*beta/2))
Ku=S.Matrix([[0,0,0,B],[0,d*ss/4,D,-d*tt/2],
             [0,D,0,0],[B,-d*tt/2,0,-d*ss/4]])
mu,vu=original(Ku,d,True)
for x in mu:eq(x)
eq(vu["p"],B**3);eq(vu["q"],D**3)
eq(vu["n"],tt*B**2/2);eq(vu["o"],-tt*D**2/2)
eq(vu["n"]**3*vu["q"]**2-vu["o"]**3*vu["p"]**2,
   tt**3*B**6*D**6/4)
eq(vu["cb"].subs(ss,-tt),3*d*tt**6/4)
print("PASS A=0 exhaustive mean branches and original local obstructions",flush=True)

# A=1,B+D=0,delta!=0.
E=h*(1-d*d-h)/2+d*d*(1-d*d)/8
Kz=S.Matrix([[0,0,1,d/2],[0,h/2-E,-d/2,E],
             [1,-d/2,0,0],[d/2,E,0,h/2-E]])
mz,vz=original(Kz,d,True)
for x in mz:eq(x)
rho=d*d+2*h
eq(vz["ca"]+vz["cb"],-3*d*d*(rho*rho+d*d)/128)
eq(vz["ca"]-vz["cb"],3*d*rho*(rho*rho-rho-d*d)/64)
def rd(x):
    return S.rem(S.Poly(clean(x.subs(h,S.Rational(3,8))),d,domain=S.QQ),
                 S.Poly(d*d+S.Rational(1,4),d,domain=S.QQ)).as_expr()
eq(rd(vz["p"]),d/8);eq(rd(vz["q"]),-d/8)
eq(rd(vz["n"]),(1+2*d)/64);eq(rd(vz["o"]),(1-2*d)/64)
eq(rd(vz["n"]**3-vz["o"]**3),d/32768)
print("PASS B+D=0 boundary and its nonzero cube obstruction",flush=True)

# A=1,s=B+D !=0: reverse derivation BEFORE imposing the final r,t chart.
B=(ss+tt)/2;D=(ss-tt)/2
Kg=S.Matrix([[0,0,1,B],[0,j-e,D,e],[1,D,0,0],[B,e,0,k-e]])
mg=original(Kg,d)
hs=j+k;ell=j-k
eq(mg[0]+mg[2],-d*d+d*tt-d*d*ss+2*d*tt*ss+2*hs*ss)
eq(mg[0]-mg[2],d**3-d*ss-3*d*d*tt+2*d*tt*tt
   +2*(tt-d)*hs+2*ell)
hs0=-d*d/2-d*rr-d*rr/(2*ss)
ell0=d*(ss*ss+rr*rr)/(2*ss)
E0=-d*rr/2+d*rr**3/(2*ss)-d*rr/(4*ss)-d*d/8-d*d*rr*rr/(8*ss*ss)
sub={tt:rr+d,j:(hs0+ell0)/2,k:(hs0-ell0)/2,e:E0}
re=[clean(x.subs(sub,simultaneous=True)) for x in mg]
eq(re[0]);eq(re[2]);eq(re[1]+re[3])
relation=ss**3+ss*rr**2-4*ss*rr**4+2*d*rr**3
eq(re[1]-re[3],-d*relation/(2*ss*ss))
print("PASS complete reverse regular-mean parametrization and sole remaining relation",
      flush=True)
print("ALL PASS: independent unit2+2 boundary and reverse source identities")
