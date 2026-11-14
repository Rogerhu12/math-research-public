#!/usr/bin/env python3
"""R317: four original pole orbits, actual elliptic Fermat quotients and trace.

The actual H3 first kernel is the exact R315 certificate shipped beside this
script. This file independently Hensel-lifts the original four algebraic poles,
computes their reduction orders and logarithm quotients by complete elliptic
addition, and checks the moving-pole trace against the full first defect.
It uses one fixed prime 59 and does not infer any infinite-prime assertion.
"""
from pathlib import Path
import json, math
CHECKS=[]
def check(name, condition):
    assert condition, name
    CHECKS.append(name)
P=59
PREC=12
MOD=P**PREC
class F:
    def __init__(self,a=0,b=0,m=MOD):
        self.a=int(a)%m; self.b=int(b)%m; self.m=m
    def c(self,o):
        if isinstance(o,F):
            assert o.m==self.m
            return o
        return F(o,0,self.m)
    def __add__(self,o):
        o=self.c(o); return F(self.a+o.a,self.b+o.b,self.m)
    __radd__=__add__
    def __neg__(self):return F(-self.a,-self.b,self.m)
    def __sub__(self,o):return self+-self.c(o)
    def __rsub__(self,o):return self.c(o)+-self
    def __mul__(self,o):
        o=self.c(o)
        return F(self.a*o.a-3*self.b*o.b,self.a*o.b+self.b*o.a,self.m)
    __rmul__=__mul__
    def inv(self):
        z=pow((self.a*self.a+3*self.b*self.b)%self.m,-1,self.m)
        return F(self.a*z,-self.b*z,self.m)
    def __truediv__(self,o):return self*self.c(o).inv()
    def __pow__(self,n):
        if n<0:return self.inv()**(-n)
        r=F(1,0,self.m);a=self
        while n:
            if n&1:r=r*a
            a=a*a;n//=2
        return r
    def __eq__(self,o):
        o=self.c(o);return self.a==o.a and self.b==o.b
    def mod(self,m):return F(self.a,self.b,m)
    def divp(self,n,m=None):
        d=P**n;assert self.a%d==self.b%d==0
        return F(self.a//d,self.b//d,m or self.m//d)
    def vp(self):
        v=0;a=self.a;b=self.b
        if a==b==0:return PREC
        while a%P==b%P==0:a//=P;b//=P;v+=1
        return v
    def tup(self):return [self.a,self.b]
def lift(root,fun,der):
    u=root
    for _ in range(5):
        u=(u-fun(u)*pow(der(u),-1,MOD))%MOD
    assert fun(u)%MOD==0
    return u
def root2(value):
    v=value%MOD
    sq=[a for a in range(1,P) if a*a%P==v%P]
    if sq:return F(lift(sq[0],lambda a:a*a-v,lambda a:2*a))
    vv=(-v*pow(3,-1,MOD))%MOD
    sq=[a for a in range(1,P) if a*a%P==vv%P]
    assert sq
    return F(0,lift(sq[0],lambda a:a*a-vv,lambda a:2*a))
def add_aff(A,B):
    if A is None:return B
    if B is None:return A
    x,y=A;u,v=B
    if x==u and y==-v:return None
    slope=3*x*x/(2*y) if x==u else (v-y)/(u-x)
    xx=slope*slope-x-u
    return xx,-y+slope*(x-xx)
def order(A):
    Q=None
    for n in range(1,P+2):
        Q=add_aff(Q,A)
        if Q is None:return n
    raise ValueError('order')
def dbl(Q):
    X,Y,Z=Q
    S=4*X*Y*Y;M=3*X*X
    XX=M*M-2*S
    return XX,M*(S-XX)-8*Y**4,2*Y*Z
def jadd(Q,A):
    X,Y,Z=Q;a,b=A
    U=a*Z*Z;S=b*Z**3;H=U-X;R=S-Y
    XX=R*R-H**3-2*X*H*H
    return XX,R*(X*H*H-XX)-Y*H**3,Z*H
def affine(Q,mod):
    X,Y,Z=Q
    v=Z.vp()
    assert PREC>=3*v+2
    X=X.divp(2*v,mod);Y=Y.divp(3*v,mod);Z=Z.divp(v,mod)
    return X/(Z*Z),Y/(Z**3)
def poly(K,r):
    ans=F(0,0,r.m)
    for c in K[::-1]:ans=ans*r+c
    return ans

j=json.loads(Path(__file__).with_name('check-jzero-actual-pole-kernel-no-scalar.json').read_text())
K=j['finite_certificate']['K_coefficients_ascending'];c0=j['finite_certificate']['kappa_inverse_div_p_mod_p']
check('original R315 H3 kernel input', K==[8,31,27,19,39,57,29,19,8,1] and c0==19)
Kd=[(k*c)%P for k,c in enumerate(K)][1:]
rows=[];Wsum=F(0,0,P);dsum=F(0,0,P*P);m0=F(0,0,P)
for u0 in [None,45,47,53]:
    if u0 is None:r=(-4*17)%MOD
    else:
        u=lift(u0,lambda u:u**3-204*u*u-384*u+64,lambda u:3*u*u-408*u-384)
        r=17*u%MOD
    a0=pow(r%P,pow(3,-1,P-1),P)
    aa=lift(a0,lambda a:a**3-r,lambda a:3*a*a)
    yy=root2(r+17)
    A=(F(aa),yy);ar=A[0]
    check(f'original algebraic pole on E17 u={u0}', yy*yy==ar**3+17)
    ordp=order((ar.mod(P),yy.mod(P)))
    Q=(ar,yy,F(1))
    for k in range(1,ordp):
        Q=dbl(Q) if k==1 else jadd(Q,A)
    check(f'complete reduction-order multiplication enters formal group u={u0}', Q[2].mod(P)==0 and Q[1].mod(P)!=0)
    t=-Q[0]*Q[2]/Q[1]
    check(f'integral formal logarithm quotient u={u0}', t.mod(P)==0)
    q=t.divp(1,P)/ordp
    if u0 is None:
        check('original three-torsion orbit is exactly fixed', t==0)
        A1=(ar.mod(P*P),yy.mod(P*P))
    else:
        td=t*((P+1)//ordp)
        A1=affine(jadd((F(1),F(1),td),A),P*P)
        check(f'actual moved pole on E17 modulo p2 u={u0}', A1[1]**2==A1[0]**3+17)
    ar2=ar.mod(P*P);y2=yy.mod(P*P);r2=ar2**3
    if u0 is None:Ac=F(1,0,P*P)/28
    else:Ac=27*r2*(r2+4*17)/(28*(3*r2*r2-408*17*r2-384*17*17))
    r1=A1[0]**3
    B1=Ac*A1[0]**2*A1[1]/(ar2**2*y2)
    delta=B1*poly(K,r1)-Ac*poly(K,r2)
    check(f'actual first trace difference has factor p u={u0}', delta.mod(P)==0)
    dsum=dsum+delta
    rr=r2.mod(P);aco=Ac.mod(P);ap=ar.mod(P);yp=yy.mod(P)
    G=(7*rr+4*17)*poly(K,rr)+6*rr*(rr+17)*poly(Kd,rr)
    coeff=c0*aco*G/(ap*yp)
    Wterm=coeff*q
    Wsum=Wsum+Wterm
    m0=m0+c0*aco*poly(K,rr)
    rows.append({'u0':u0,'r_modp':rr.tup(),'x_modp':ap.tup(),'y_modp':yp.tup(),'original_x_modp2':ar2.tup(),'original_y_modp2':y2.tup(),'moved_x_modp2':A1[0].tup(),'moved_y_modp2':A1[1].tup(),'order_reduction':ordp,'log_div_p':q.tup(),'A_modp':aco.tup(),'G_modp':G.tup(),'W_term':Wterm.tup(),'direct_step_divp':delta.divp(1,P).tup()})
direct=c0*dsum.divp(1,P)
check('independent actual moving-point trace equals negative tangent defect', direct==-Wsum)
check('original divided row is 1', m0==1)
check('actual weighted elliptic Fermat defect is 21', Wsum==21)
check('actual trace difference divided by p2 is 38', direct==38)
out={'status':'PASS','check_count':len(CHECKS),'checks':CHECKS,'arithmetic_precision':PREC,'sqrt_minus3_relation':'delta^2=-3','p':P,'rows':rows,'original_divided_row':m0.tup(),'W':Wsum.tup(),'actual_trace_difference_div_p2':direct.tup()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','check_count':len(CHECKS),'p':P,'W':Wsum.tup(),'actual_trace_difference_div_p2':direct.tup()},indent=2))

