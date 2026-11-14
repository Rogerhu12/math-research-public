#!/usr/bin/env python3
"""Finite exact p^3 experiments on R403/R406 actual three-block matrices.

This is an exploratory calculation, not a cross-prime nonvanishing proof.
The theta/X recurrence and all carries are computed modulo p^3 directly.
"""
import argparse
import json


class ThreeBlocks:
    def __init__(self, p, ell):
        assert p % 6 == 5 and p > 83
        self.p, self.s, self.ell = p, (p+1)//6, ell
        assert 1 <= ell < self.s-13
        self.L, self.mod = 2*self.s+ell, p**3
        self.one = [1]+[0]*(self.L-1)
        self.zero = [0]*self.L

    def add(self, a, b):
        return [(x+y) % self.mod for x,y in zip(a,b)]

    def scale(self, a, c):
        return [(x*c) % self.mod for x in a]

    def mul(self, a, b):
        L, m = self.L, self.mod
        out = [0]*L
        for i, x in enumerate(a):
            if x:
                for j in range(L-i):
                    out[i+j] = (out[i+j]+x*b[j]) % m
        return out

    def gamma_mul(self, a, b):
        L, s, p, m = self.L, self.s, self.p, self.mod
        out = [0]*L
        for i, x in enumerate(a):
            if x:
                for j in range(L-i):
                    c = p if (i % s)+(j % s) >= s else 1
                    out[i+j] = (out[i+j]+c*x*b[j]) % m
        return out

    def inv(self, a):
        L, m = self.L, self.mod
        inv0 = pow(a[0], -1, m)
        out = [inv0]+[0]*(L-1)
        for n in range(1,L):
            out[n] = -inv0*sum(a[i]*out[n-i] for i in range(1,n+1)) % m
        return out

    def power(self, a, n, gamma=False):
        if n < 0:
            assert not gamma
            return self.power(self.inv(a), -n)
        result, base = self.one[:], a[:]
        mul = self.gamma_mul if gamma else self.mul
        while n:
            if n & 1:
                result = mul(result, base)
            n >>= 1
            if n:
                base = mul(base, base)
        return result

    def log(self, a):
        assert a[0] == 1
        derivative = [(i+1)*a[i+1] % self.mod for i in range(self.L-1)]+[0]
        product = self.mul(derivative,self.inv(a))
        return [0]+[product[i-1]*pow(i,-1,self.mod) % self.mod for i in range(1,self.L)]

    def exp(self, a):
        assert a[0] == 0
        out = self.one[:]
        for n in range(1,self.L):
            out[n] = sum(i*a[i]*out[n-i] for i in range(1,n+1))*pow(n,-1,self.mod) % self.mod
        return out

    def to_gamma(self, a):
        return [x*self.p**(r//self.s) % self.mod for r,x in enumerate(a)]

    def initialize(self):
        m,L,s,p = self.mod,self.L,self.s,self.p
        X = self.one[:]
        X[1] = -pow(7,-1,m) % m
        for n in range(2,L):
            X[n] = sum(X[i]*X[n-i] for i in range(1,n))*pow((6*n+1)*(n-1),-1,m) % m
        invX3 = self.power(X,-3)
        t = [0]+[-x % m for x in invX3[:-1]]
        F = [0]*L
        for n in range(1,L):
            if n != s:
                F[n] = -X[n]*pow(6*n*(6*n-1),-1,m) % m
        ap = -34*X[s]*pow(6*s,-1,m) % m
        assert ap % p
        self.ap, self.t = ap,t
        self.h = self.add(self.add(self.scale(self.one,7),self.scale(t,4)),self.scale(self.mul(t,t),16))
        self.tm1 = self.add(t,self.scale(self.one,-1))
        self.d = self.add(self.one,self.scale(t,8))
        logU17 = self.add(self.scale(self.log(X),17),self.scale(F,34))
        g = self.exp(self.add(logU17,self.log(self.d)))
        gaussian = self.one[:]
        gaussian[s] = ap
        gaussian[2*s] = ap*ap*pow(2,-1,m) % m
        self.R = self.gamma_mul(self.to_gamma(g), gaussian)
        a = self.mul(self.mul(t,self.tm1),self.h)
        f = self.scale(self.mul(self.d,a),pow(7,-1,m))
        v1 = self.add(self.one,self.scale(t,-4))
        v2 = self.add(self.add(self.one,self.scale(t,-20)),self.scale(self.mul(t,t),-8))
        v3 = self.add(self.add(self.add(self.one,self.scale(t,96)),self.scale(self.mul(t,t),48)),self.scale(self.power(t,3),-64))
        V = self.mul(self.mul(v1,v2),v3)
        alpha = 36*pow(17,-1,m) % m
        Treg = self.mul(self.exp(self.scale(logU17,alpha)),self.mul(f,V))
        self.g, self.Treg = g, Treg
        tgauss = self.one[:]
        tgauss[s] = alpha*ap % m
        tgauss[2*s] = alpha*alpha*ap*ap*pow(2,-1,m) % m
        self.T = self.gamma_mul(self.to_gamma(Treg), tgauss)
        self.t_powers = [self.one[:]]
        for _ in range(L):
            self.t_powers.append(self.mul(self.t_powers[-1],t))

    def columns(self,D,J):
        columns,labels = [],[]
        Rpow = [self.power(self.R,n,True) for n in range(D+1)]
        Tpow = [self.power(self.T,j,True) for j in range(J+1)]
        for n in range(D+1):
            A,B,C = (n+1)//4,(n+1)//3,n//2
            e = 3*((3*(n+1)+3)//4)+2*((n+2)//2)+(2*(n+1)+2)//3-2
            q = self.mul(self.mul(self.power(self.mul(self.t,self.h),A),self.power(self.tm1,B)),self.power(self.d,-C))
            angular = q
            for k in range(e+1):
                core = self.gamma_mul(Rpow[n],self.to_gamma(angular))
                for j in range(J+1):
                    columns.append(self.gamma_mul(core,Tpow[j]))
                    labels.append((n,k,j))
                angular = self.mul(angular,self.t)
        return columns,labels


def smith_counts(rows,p,precision=3):
    A = [r[:] for r in rows]
    counts = []
    for depth in range(precision):
        m = p**(precision-depth)
        nr,nc = len(A),len(A[0]) if A else 0
        k = 0
        while k < nr and k < nc:
            pos = next(((i,j) for j in range(k,nc) for i in range(k,nr) if A[i][j] % p),None)
            if pos is None:
                break
            i,j = pos
            A[k],A[i] = A[i],A[k]
            for row in A:
                row[k],row[j] = row[j],row[k]
            inv = pow(A[k][k],-1,m)
            A[k] = [x*inv % m for x in A[k]]
            for i in range(k+1,nr):
                c = A[i][k]
                if c:
                    A[i] = [(x-c*y) % m for x,y in zip(A[i],A[k])]
            k += 1
        counts.append(k)
        A = [[x//p for x in row[k:]] for row in A[k:]]
    return counts,len(A),len(A[0]) if A else 0


def run(p,ell,D,J):
    G = ThreeBlocks(p,ell)
    G.initialize()
    cols,labels = G.columns(D,J)
    rows = [[c[r] for c in cols] for r in range(G.L)]
    shifted = [[0]*len(cols) for _ in range(G.L+13)]
    for r,row in enumerate(rows):
        factor = p**((r+13)//G.s-r//G.s)
        shifted[r+13] = [x*factor % G.mod for x in row]
    jc,jrem,jcols = smith_counts(rows,p)
    mc,mrem,mcols = smith_counts(shifted,p)
    return {"p":p,"s":G.s,"ell":ell,"D":D,"J":J,"columns":len(cols),"ap_mod_p":G.ap % p,
            "J_smith_v0_v1_v2":jc,"J_remaining_rows":jrem,
            "M_smith_v0_v1_v2":mc,"M_remaining_rows":mrem}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--p",type=int,default=101)
    parser.add_argument("--ell",type=int,default=1)
    parser.add_argument("--D",type=int,default=3)
    parser.add_argument("--J",type=int,default=0)
    args = parser.parse_args()
    print(json.dumps(run(args.p,args.ell,args.D,args.J),indent=2))
