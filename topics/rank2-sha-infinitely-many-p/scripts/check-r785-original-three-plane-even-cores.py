#!/usr/bin/env python3
"""R785 exact original six-input geometry and complete even-core centers.
All computation is intended for public Actions; no generated files.
"""
from fractions import Fraction as F
import hashlib,json,sys
class C:
    def __init__(self,a=0,b=0): self.a,self.b=F(a),F(b)
    def __add__(self,o):
        o=cv(o);return C(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return C(-self.a,-self.b)
    def __sub__(self,o): return self+-cv(o)
    def __rsub__(self,o): return cv(o)+-self
    def __mul__(self,o):
        o=cv(o);a,b,c,d=self.a,self.b,o.a,o.b
        return C(a*c-b*d,a*d+b*c-b*d)
    __rmul__=__mul__
    def bar(self): return C(self.a-self.b,-self.b)
    def norm(self): return self.a*self.a-self.a*self.b+self.b*self.b
    def __truediv__(self,o):
        o=cv(o);z=self*o.bar();n=o.norm()
        return C(z.a/n,z.b/n)
    def __rtruediv__(self,o): return cv(o)/self
    def __eq__(self,o):
        o=cv(o);return self.a==o.a and self.b==o.b
    def __pow__(self,n):
        if n<0:return (1/self)**(-n)
        z=C(1);x=self
        while n:
            if n&1:z=z*x
            x=x*x;n//=2
        return z
    def out(self): return [str(self.a),str(self.b)]
def cv(x): return x if isinstance(x,C) else C(x)
def vec(xs): return list(map(cv,xs))
def add(a,b): return [x+y for x,y in zip(a,b)]
def sc(c,a): return [cv(c)*x for x in a]
def sub(a,b): return add(a,sc(-1,b))
def ip(a,b): return sum((x*y.bar() for x,y in zip(a,b)),C())
def norm(a):
    z=ip(a,a);assert z.b==0;return z.a
def matdet(rows):
    a=[r[:] for r in rows];out=C(1);n=len(a)
    for j in range(n):
        k=next(i for i in range(j,n) if a[i][j]!=0)
        if k!=j:a[k],a[j]=a[j],a[k];out=-out
        u=a[j][j];out=out*u
        for i in range(j+1,n):
            q=a[i][j]/u
            a[i]=[x-q*y for x,y in zip(a[i],a[j])]
    return out
checks=0
def eq(a,b):
    global checks
    assert a==b,(a,b);checks+=1
def orth(a,b):eq(ip(a,b),C())
def integer(z):
    assert z.a.denominator==z.b.denominator==1
    return int(z.a),int(z.b)
def modz(z,n):
    a,b=integer(z);return [a%n,b%n]
def crt(a,m,b,n):return (a+m*((b-a)*pow(m,-1,n)%n))%(m*n)

w=C(0,1);delta=1+2*w
basis=[vec([int(i==j) for i in range(6)]) for j in range(6)]
X1,X2,X3,X,c,d=basis
r=sc(1/delta,vec([1,0,-w*w,w,0,0]))
s=add(r,c);t=sub(r,c)
B=vec([-1,0,w,-w*w,0,0]);H=add(B,sc(2,X2))
A0=add(sc(2*delta,X2),sc(-4*delta/3,B));A=add(A0,r)
Y=add(add(A0,s),sc(2,d))
aa=1+3*w;alpha=17-3*w;h0=17+3*w;bY=(20+3*w)/17
P=add(add(A0,sc(2+3*w,s)),sc(4,d));W=sub(P,sc(aa,t))
Vt=add(sc(aa.bar(),P),sc(29,t))
R=sub(Y,sc(alpha/29,P));Z0=sub(P,sc(bY,Y))
J=add(add(sc(3*w*w/14,A0),s),sc(2+3*w,d))
J0=sc(7*delta,J);Lt=sc(2*delta,t);Lp=sc(2*delta,P)
Fv=add(add(sub(s,B),sc(w*w,X2)),sc(2+3*w,d))
Caxis=sc(1/delta,vec([1,0,-1,1,0,0]))
G=add(sc(13,H),sc(3-2*w,Fv))
E=add(add(sc(5+6*w,A),sc(-29,c)),sc(-(58+87*w),d))
hs=sub(s,sc(F(1,17),Y));hd=sub(d,sc(F(1,17),Y));U=sub(sc(F(1,2),hs),sc(3,hd))
eq(J,sub(Fv,sc(-(5+2*w)/7,H)))
eq(J0,vec([13+6*w,9+9*w,13+7*w,w,7*delta,-28+7*w]))
for v,n in [(A0,28),(s,2),(d,1),(t,2),(Y,34),(P,58),(W,72),(Vt,2088),
            (R,F(288,29)),(Z0,F(288,17)),(J,F(72,7)),(J0,1512),(Lt,24),(Lp,696),(E,7627)]:
    eq(norm(v),F(n))
for x in [Y,P,t,R,Z0,W,Vt]:
    for z in [Caxis,H,J]:orth(x,z)
for x in [Caxis,Fv,G]:
    for z in [Y,P,t,R,Z0]:orth(x,z)
for x,y in [(Y,t),(Y,Z0),(Z0,t),(P,t),(P,R),(R,t),(W,Vt),(J,t),(J,Y),(J,Z0),(J,W),(E,Y),(E,W)]:
    orth(x,y)
eq(matdet([[ip(x,y) for y in [Y,P,t]] for x in [Y,P,t]]),C(1152))
eq(ip(E,J),C(-263))
eq(E,add(add(sc(-17*(25+48*w)/144,Z0),sc(h0,t)),sc(F(-1841,72),J)))
eq(hs,sub(sc(F(7,36),J),sc((17+24*w)/72,Z0)))
eq(hd,add(sc(-7*aa/72,J),sc((17+3*w)/144,Z0)))
eq(U,sub(sc(7*(4+9*w)/72,J),sc((68+33*w)/144,Z0)))
eq(sub(sc(36,Y),sc(alpha,W)),add(sc(36,R),sc(alpha*aa/29,Vt)))
for L in [J0,Lt,Lp]:
    residues=[modz(v,2) for v in L]
    eq(sum(x!=[0,0] for x in residues)%2,0)
for L in [Lt,Lp]:
    eq(modz(ip(L,W),4),[0,0])
eq(ip(Lt,W),-4*delta*aa.bar());eq(ip(Lp,W),116*delta)
# Existing ray: g=(11+8w) mod16 and g=1 mod27,7,29.
odd=27*7*29;ga=crt(11,16,1,odd);gb=crt(8,16,0,odd);g=C(ga,gb)
for degree in [24,696,1512]:
    eq(modz(g*g,2*degree),[(1+degree)%(2*degree),0])
gamma7=3+w;eq(gamma7.norm(),F(7));eq((6*delta*gamma7).norm(),F(756))
eq((2*delta).norm(),F(12));eq(4*174,696)
report={"format":"R785 original complete geometry and core centers","checks":checks,
        "source":"Original six-input rows; no added observed source",
        "norms":{"J0":1512,"2delta_t":24,"2delta_P":696,"R":"288/29","Z0":"288/17"},
        "retained_gram_determinant":1152,
        "E_J_coefficient":"-1841/72",
        "complete_center_degrees":[24,696,1512],
        "outputs_persisted":False}
print(json.dumps(report,separators=(",",":")))
