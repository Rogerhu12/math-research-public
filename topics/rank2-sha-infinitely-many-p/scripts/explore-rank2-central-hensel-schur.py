#!/usr/bin/env python3
"""Exact R425 Schur substitution at specified original finite source budgets.

The Hensel-substituted matrix is a conditional finite model.  It is the actual
arithmetic matrix only if the original two complete central failures hold.
"""
import argparse
import importlib.util
import json
from math import comb, factorial
from pathlib import Path
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("r425", ROOT / "check-r425-complete-central-four-row.py")
r425 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r425)


def matmul(A, B, p):
    if not A:
        return []
    BT = list(zip(*B))
    return [[sum(x*y for x,y in zip(row,col)) % p for col in BT] for row in A]


def inverse_and_det(A, p):
    n = len(A)
    B = [[x % p for x in row] + [int(i == j) for j in range(n)] for i,row in enumerate(A)]
    determinant = 1
    for j in range(n):
        pos = next((i for i in range(j,n) if B[i][j]), None)
        if pos is None:
            return None, 0
        if pos != j:
            B[j], B[pos] = B[pos], B[j]
            determinant = -determinant
        pivot = B[j][j]
        determinant = determinant*pivot % p
        ip = pow(pivot,-1,p)
        B[j] = [x*ip % p for x in B[j]]
        for i in range(n):
            if i != j and B[i][j]:
                c = B[i][j]
                B[i] = [(x-c*y) % p for x,y in zip(B[i],B[j])]
    return [row[n:] for row in B], determinant % p


def central_solution(p):
    s = (p+1)//6
    G = r425.series(p,1,3*s+1)
    ang = G.scale(G.mul(G.mul(G.t,G.tm1),G.h),pow(7,-1,G.mod))
    S,T = G.mul(G.g,ang),G.Treg
    alpha = 36*pow(17,-1,G.mod) % G.mod
    ap = G.ap

    def coeff(A,q,k,u,v):
        ans = 0
        for m in range(k+1):
            for j in range(m+1):
                index = k*s-m*(s-2)-j
                if index >= 0:
                    ans += pow(q,m,G.mod)*pow(factorial(m),-1,G.mod)*comb(m,j)*pow(u,m-j,G.mod)*pow(v,j,G.mod)*A[index]
        return ans % G.mod

    def F(u,v):
        c = [coeff(S,1,k,u,v) for k in (1,2,3)]
        d = [coeff(T,alpha,k,u,v) for k in (1,2,3)]
        a = c[0]-p*pow(ap,-1,G.mod)*c[1]+2*p*p*pow(ap*ap,-1,G.mod)*c[2]
        b = pow(alpha,-1,G.mod)*d[0]-p*pow(alpha*alpha*ap,-1,G.mod)*d[1]+2*p*p*pow(alpha**3*ap*ap,-1,G.mod)*d[2]
        return a % G.mod,b % G.mod

    beta = (T[2]-S[2]) % p
    fs,ft = F(0,0)
    u = (fs-ft)*pow(beta,-1,p) % p
    v = (-fs-S[2]*u) % p
    for r in (1,2):
        fs,ft = F(u,v)
        assert fs % (p**r) == ft % (p**r) == 0
        a,b = fs//(p**r) % p,ft//(p**r) % p
        du = (a-b)*pow(beta,-1,p) % p
        dv = (-a-S[2]*du) % p
        u += p**r*du
        v += p**r*dv
    assert F(u,v) == (0,0)
    return (u,v), {"S":S[s] % p,"T":T[s] % p}, (S[2] % p,T[2] % p)


def schur(p,ell,D,J):
    s,L = (p+1)//6,2*((p+1)//6)+ell
    G = r425.series(p,ell,L+13)
    cols,labels,ordinary,carrier = r425.carrier_and_ordinary_columns(G,D,J)
    N = len(cols)
    assert N == L, "This calculation retains all free 13 rows and uses the square finite part"
    active = [[c[r] for c in cols] for r in range(13,L+13)]
    K = r425.nullspace(active,p)
    left = r425.nullspace(list(map(list,zip(*active))),p)
    assert len(K) == len(left)
    MPdiv = []
    for P in K:
        MP = [sum(x*c[r] for x,c in zip(P,cols)) % G.mod for r in range(13,L+13)]
        assert all(x % p == 0 for x in MP)
        MPdiv.append([x//p % p for x in MP])
    B0 = [[sum(x*y for x,y in zip(l,v)) % p for v in MPdiv] for l in left]
    Binv,detB = inverse_and_det(B0,p)
    base_smith = r425.actual.smith_counts([[c[r] for c in cols] for r in range(L+13)],p)[0]
    if Binv is None:
        return {"p":p,"ell":ell,"D":D,"J":J,"N":N,"base_smith":base_smith,
                "base_first_lift_det":0,"conditional_model":True}
    rows = [2*s-2,2*s-1,L+11,L+12]
    U = [[l[r-13] for r in rows] for l in left]
    tails = []
    alpha = 36*pow(17,-1,p) % p
    for P in K:
        values = []
        for power,index in ((1,s-13),(1,s-12),(2,ell),(2,ell+1)):
            values.append(sum(c*pow((n+40+alpha*j)%p,power,p)*A[index] for c,(n,k,j),A in zip(P,labels,ordinary)) % p)
        tails.append(values)
    Vu = [[v[0] for v in tails],[v[1] for v in tails],
          [G.ap*v[2] % p for v in tails],[G.ap*v[3] % p for v in tails]]
    Vv = [[0]*len(K),[v[0] for v in tails],[0]*len(K),[G.ap*v[2] % p for v in tails]]
    BinvU = matmul(Binv,U,p)
    Au,Av = matmul(Vu,BinvU,p),matmul(Vv,BinvU,p)
    pair, first, low = central_solution(p)
    u,v = pair
    small = [[(int(i==j)+u*Au[i][j]+v*Av[i][j]) % p for j in range(4)] for i in range(4)]
    detsmall = inverse_and_det(small,p)[1]
    h = G.zero[:]
    h[s-2],h[s-1] = u,v
    hg = G.to_gamma(h)
    alpha_full = 36*pow(17,-1,G.mod) % G.mod
    G.R = G.gamma_mul(G.R,r425.scalar_exp_gamma(G,hg,1))
    G.T = G.gamma_mul(G.T,r425.scalar_exp_gamma(G,hg,alpha_full))
    new_rel,new_labels = G.columns(D,J)
    assert new_labels == labels
    new_carrier = G.gamma_mul(carrier,r425.scalar_exp_gamma(G,hg,40))
    changed = [G.gamma_mul(new_carrier,c) for c in new_rel]
    assert all((x-y) % p == 0 for a,b in zip(cols,changed) for x,y in zip(a,b))
    new_div = []
    for P in K:
        MP = [sum(x*c[r] for x,c in zip(P,changed)) % G.mod for r in range(13,L+13)]
        assert all(x % p == 0 for x in MP)
        new_div.append([x//p % p for x in MP])
    Bnew = [[sum(x*y for x,y in zip(l,w)) % p for w in new_div] for l in left]
    assert inverse_and_det(Bnew,p)[1] == detB*detsmall % p
    new_smith = r425.actual.smith_counts([[c[r] for c in changed] for r in range(L+13)],p)[0]
    import sympy as sp
    uu,vv,xx,yy = sp.symbols("u v x y")
    pencil = sp.Matrix([[int(i==j)+uu*Au[i][j]+vv*Av[i][j] for j in range(4)] for i in range(4)])
    poly = sp.Poly(sp.expand(pencil.det()),uu,vv,modulus=p)
    s2,t2 = low
    cs,ct = first["S"],first["T"]*pow(alpha,-1,p)%p
    uxy = (yy-xx+cs-ct)*pow((t2-s2)%p,-1,p)
    vxy = xx-cs-s2*uxy
    central_poly = sp.Poly(sp.expand(poly.as_expr().subs({uu:uxy,vv:vxy})),xx,yy,modulus=p)
    return {"p":p,"ell":ell,"D":D,"J":J,"N":N,
            "base_smith":base_smith,"base_first_lift_det":detB,
            "actual_first_central_weights":first,
            "unique_conditional_hensel_pair_mod_p3":[u,v],
            "first_lift_four_by_four_u":Au,"first_lift_four_by_four_v":Av,
            "relative_first_lift_determinant":str(poly.as_expr()),
            "same_determinant_in_first_central_coordinates":str(central_poly.as_expr()),
            "conditional_determinant_ratio":detsmall,
            "conditional_full_smith":new_smith,
            "conditional_model_is_not_asserted_actual":True}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--p",type=int,default=113)
    parser.add_argument("--ell",type=int,default=4)
    parser.add_argument("--D",type=int,default=1)
    parser.add_argument("--J",type=int,default=2)
    parser.add_argument("--out",type=Path)
    args = parser.parse_args()
    result = schur(args.p,args.ell,args.D,args.J)
    output = json.dumps(result,indent=2)
    if args.out:
        args.out.write_text(output+"\n")
    print(output)

