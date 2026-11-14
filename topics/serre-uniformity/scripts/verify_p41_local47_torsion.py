#!/usr/bin/env python3
"""Independent standard-library verification of the actual local torsion data."""
import json
from pathlib import Path
import sys


def trim(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a


def poly_div(a,b,p):
    a=trim([x%p for x in a]);b=trim([x%p for x in b])
    q=[0]*max(1,len(a)-len(b)+1);ib=pow(b[-1],-1,p)
    while a!=[0] and len(a)>=len(b):
        k=len(a)-len(b);c=a[-1]*ib%p;q[k]=c
        for j,v in enumerate(b):a[k+j]=(a[k+j]-c*v)%p
        trim(a)
    return trim(q),a


def poly_add(a,b,p):
    return trim([((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0))%p
                 for i in range(max(len(a),len(b)))])


def poly_mul(a,b,p):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%p
    return trim(c)


def poly_gcd(a,b,p):
    while b!=[0]:a,b=b,poly_div(a,b,p)[1]
    return [x*pow(a[-1],-1,p)%p for x in a]


class Ring:
    def __init__(self,f,q):
        assert f[-1]==1
        self.f=f;self.n=len(f)-1;self.q=q
        self.nonzero=[(i,c) for i,c in enumerate(f[:-1]) if c]
        self.zero=(0,)*self.n
        self.one=(1,)+(0,)*(self.n-1)
        self.x=(0,1)+(0,)*(self.n-2)

    def element(self,a):
        if isinstance(a,int):return (a%self.q,)+(0,)*(self.n-1)
        assert len(a)<=self.n
        return tuple(x%self.q for x in a)+(0,)*(self.n-len(a))

    def add(self,a,b):return tuple((x+y)%self.q for x,y in zip(a,b))
    def sub(self,a,b):return tuple((x-y)%self.q for x,y in zip(a,b))
    def scale(self,a,c):return tuple(c*x%self.q for x in a)

    def mul(self,a,b):
        out=[0]*(2*self.n-1)
        aa=[(i,x) for i,x in enumerate(a) if x];bb=[(j,y) for j,y in enumerate(b) if y]
        for i,x in aa:
            for j,y in bb:out[i+j]+=x*y
        for k in range(len(out)-1,self.n-1,-1):
            c=out[k]%self.q
            if c:
                for j,v in self.nonzero:out[k-self.n+j]-=c*v
        return tuple(x%self.q for x in out[:self.n])

    def power(self,a,n):
        assert n>=0
        out=self.one
        while n:
            if n&1:out=self.mul(out,a)
            n//=2
            if n:a=self.mul(a,a)
        return out

    def evaluate(self,coefficients,a):
        out=self.zero
        for c in reversed(coefficients):out=self.add(self.mul(out,a),self.element(c))
        return out

    def inverse(self,a):
        r0=self.f[:];r1=trim([x%47 for x in a]);t0=[0];t1=[1]
        assert r1!=[0]
        while r1!=[0]:
            q,r=poly_div(r0,r1,47);r0,r1=r1,r
            t0,t1=t1,poly_add(t0,[-x for x in poly_mul(q,t1,47)],47)
        assert len(r0)==1
        inv0=poly_div([x*pow(r0[0],-1,47)%47 for x in t0],self.f,47)[1]
        b=self.element(inv0)
        for _ in range(2):b=self.mul(b,self.sub(self.element(2),self.mul(a,b)))
        assert self.mul(a,b)==self.one
        return b


class Curve:
    def __init__(self,ring,A,B):self.r=ring;self.A=A;self.B=B

    def on_curve(self,P):
        if P is None:return True
        r=self.r;x,y=P
        return r.mul(y,y)==r.add(r.add(r.power(x,3),r.scale(x,self.A)),r.element(self.B))

    def line(self,P,Q,T=None):
        r=self.r
        if P is None:return Q,r.one
        if Q is None:return P,r.one
        x,y=P;xx,yy=Q
        if x==xx and r.add(y,yy)==r.zero:
            return None,r.one if T is None else r.sub(T[0],x)
        if x==xx:
            assert P==Q
            s=r.mul(r.add(r.scale(r.mul(x,x),3),r.element(self.A)),r.inverse(r.scale(y,2)))
        else:s=r.mul(r.sub(yy,y),r.inverse(r.sub(xx,x)))
        zx=r.sub(r.sub(r.mul(s,s),x),xx)
        zy=r.sub(r.mul(s,r.sub(x,zx)),y)
        Z=(zx,zy)
        assert self.on_curve(Z)
        if T is None:return Z,r.one
        numerator=r.sub(r.sub(T[1],y),r.mul(s,r.sub(T[0],x)))
        return Z,r.mul(numerator,r.inverse(r.sub(T[0],zx)))

    def add(self,P,Q):return self.line(P,Q)[0]

    def mul(self,P,n):
        if P is None:return None
        if n<0:P=(P[0],self.r.scale(P[1],-1));n=-n
        Q=None
        while n:
            if n&1:Q=self.add(Q,P)
            n//=2
            if n:P=self.add(P,P)
        return Q

    def miller(self,P,Q,n):
        r=self.r;T=P;v=r.one
        for bit in bin(n)[3:]:
            T,line=self.line(T,T,Q);v=r.mul(r.mul(v,v),line)
            if bit=='1':T,line=self.line(T,P,Q);v=r.mul(v,line)
        assert T is None
        return v


def main(path):
    data=json.loads(path.read_text())
    assert (data['level'],data['auxiliary_prime'],data['precision'],data['modulus'],data['residue_degree'])==(41,47,4,47**4,80)
    f=data['field_polynomial_ascending']
    assert len(f)==81 and f[-1]==1 and all(0<=x<47 for x in f)
    residue=Ring(f,47);u=residue.x
    for k in range(1,81):
        u=residue.power(u,47)
        if k in (16,40):assert poly_gcd(f,trim(list(residue.sub(u,residue.x))),47)==[1]
    assert u==residue.x
    r=Ring(f,47**4);phi=r.element(data['frobenius_lift'])
    assert r.evaluate(f,phi)==r.zero
    assert residue.element(phi)==residue.power(residue.x,47)
    print('Irreducible degree80 residue field and the exact unramified Frobenius lift verified.',flush=True)
    for record in data['curves']:
        A,B=record['curve_A'],record['curve_B'];C=Curve(r,A,B)
        P=tuple(r.element(v) for v in record['P']);Q=tuple(r.element(v) for v in record['Q'])
        assert C.on_curve(P) and C.on_curve(Q)
        assert C.mul(P,41) is None and C.mul(Q,41) is None
        def frobenius(T):return tuple(r.evaluate(v,phi) for v in T)
        assert frobenius(P)==Q
        assert frobenius(Q)==C.mul(P,-47)
        # x^2+47 is irreducible modulo41: Q cannot be a multiple of P.
        assert pow((-47)%41,20,41)==40
        ew=r.element(record['weil_pairing'])
        assert r.power(ew,41)==r.one and residue.element(ew)!=residue.one
        direct=r.scale(r.mul(C.miller(P,Q,41),r.inverse(C.miller(Q,P,41))),-1)
        assert direct==ew
        if record['CM_unit']:
            cmu=r.element(record['CM_unit']);U=record['CM_matrix'];aa,ee=record['CM_necklace']
            assert r.add(r.add(r.mul(cmu,cmu),cmu),r.one)==r.zero
            assert (r.mul(cmu,P[0]),P[1])==C.add(C.mul(P,U[0][0]),C.mul(Q,U[1][0]))
            assert (r.mul(cmu,Q[0]),Q[1])==C.add(C.mul(P,U[0][1]),C.mul(Q,U[1][1]))
            R=[[((2*U[i][j])+int(i==j))%41 for j in range(2)] for i in range(2)]
            scale=pow(R[1][0],-1,41);R=[[scale*x%41 for x in row] for row in R]
            assert R==[[aa,(ee-aa*aa)%41],[1,(-aa)%41]]
            assert pow(ee,20,41)==40
        else:assert record['CM_matrix']==[] and record['CM_necklace']==[]
        assert record['j_mod47']==1728*4*A**3*pow((4*A**3+27*B*B)%47,-1,47)%47
        print(record['label']+': exact curve, 41-torsion, Frobenius, and actual Weil pairing all verified.',flush=True)
    print('This verifies local torsion coordinates and level structures; it does not claim a QC root certificate.')


if __name__=='__main__':
    p=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name('data')/'p41_local47_torsion_certificate.json'
    main(p)
