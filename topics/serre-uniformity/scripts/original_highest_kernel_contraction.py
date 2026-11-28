#!/usr/bin/env python3
"""New finite exploration of R1199/R1200's full highest-kernel SS contraction.
All mathematical execution is restricted to this public repository's Actions.
This script does not test old prime windows or claim an all-prime theorem.
"""
import argparse
import hashlib
import json
import math
import os
import time

P = 0
ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)

def add(a, b):
    return tuple((x+y) % P for x, y in zip(a, b))

def neg(a):
    return tuple(-x % P for x in a)

def scale(a, c):
    return tuple(c*x % P for x in a)

def mul(a, b):
    x,y,dx,dy = a
    u,v,du,dv = b
    return ((x*u-y*v)%P, (x*v+y*u)%P,
            (dx*u-dy*v+x*du-y*dv)%P,
            (dx*v+dy*u+x*dv+y*du)%P)

def madd(c, a, b):
    x,y,dx,dy = a
    u,v,du,dv = b
    return ((c[0]+x*u-y*v)%P, (c[1]+x*v+y*u)%P,
            (c[2]+dx*u-dy*v+x*du-y*dv)%P,
            (c[3]+dx*v+dy*u+x*dv+y*du)%P)

def inv(a):
    x,y,dx,dy = a
    norm = (x*x+y*y) % P
    assert norm, "nonunit dual-number divisor"
    q = pow(norm, -1, P)
    z = (x*q%P, -y*q%P, 0, 0)
    correction = neg(mul(mul(z,z),(dx,dy,0,0)))
    return (z[0], z[1], correction[0], correction[1])

def power(a, n):
    if n < 0:
        return power(inv(a), -n)
    out = ONE
    while n:
        if n & 1:
            out = mul(out, a)
        a = mul(a, a)
        n //= 2
    return out

def value(a):
    return (a[0], a[1], 0, 0)

def derivative(a):
    return (a[2], a[3], 0, 0)

def smul(a, b, size):
    out = [ZERO] * size
    for i, x in enumerate(a[:size]):
        if x == ZERO:
            continue
        for j, y in enumerate(b[:size-i]):
            if y != ZERO:
                out[i+j] = madd(out[i+j], x, y)
    return out

def sscale(a, c):
    return [scale(x, c) for x in a]

def sinv(a, size):
    z = inv(a[0])
    out = [z]
    for n in range(1, size):
        c = ZERO
        for j in range(1, min(n+1, len(a))):
            c = madd(c, a[j], out[n-j])
        out.append(neg(mul(z, c)))
    return out

def spower(a, n, size):
    assert n >= 0
    out = [ONE]+[ZERO]*(size-1)
    a = a[:size]+[ZERO]*max(0,size-len(a))
    while n:
        if n & 1:
            out = smul(out, a, size)
        a = smul(a, a, size)
        n //= 2
    return out

def coeff_product(a, b, n):
    out = ZERO
    for i in range(n+1):
        if i < len(a) and n-i < len(b):
            out = madd(out, a[i], b[n-i])
    return out

def polynomial_at(coeff, b):
    out = ZERO
    for c in reversed(coeff):
        out = add(mul(out,b),(c%P,0,0,0))
    return out

def fmul(a, b):
    return ((a[0]*b[0]-a[1]*b[1])%P,
            (a[0]*b[1]+a[1]*b[0])%P)

def fpoly(coeff, z):
    out = (0,0)
    for c in reversed(coeff):
        t = fmul(out,z)
        out = ((t[0]+c)%P,t[1])
    return out

def hasse_Q(g):
    """Monic Q from the original R1023 hypergeometric ODE, not interpolation."""
    n = 2*g-1
    q = [1]
    i6, i3 = pow(6,-1,P), pow(3,-1,P)
    for j in range(n):
        num = (j+5*i6)**2 % P
        den = (j+1)*(j+4*i3) % P
        q.append(q[-1]*num*pow(den,-1,P)%P)
    lead_inv = pow(q[-1],-1,P)
    return [(c*lead_inv)%P for c in q]

def ode_pair(pc, qc, m):
    out = []
    for initial in [(ONE,ZERO),(ZERO,ONE)]:
        f = list(initial)
        for n in range(m-1):
            c = ZERO
            for j in range(n+1):
                c = madd(c,pc[j],scale(f[n-j+1],n-j+1))
                c = madd(c,qc[j],f[n-j])
            f.append(scale(c,-pow((n+2)*(n+1),-1,P)))
        assert len(f) == m+1
        out.append(f)
    return out

def contraction_at(b0, g):
    """P_m(T*) and d/db P_m(T*) at b0 via exact dual numbers."""
    m = 6*g-1
    b = (b0[0],b0[1],1,0)
    bt = [b,ONE]
    bt2 = smul(bt,bt,m)
    bt3 = smul(bt2,bt,m)
    rt = [neg(c) for c in bt3]
    rt[0] = add(ONE,rt[0])
    rinv = sinv(rt,m)
    pc = sscale(smul(bt2,rinv,m),-3)
    five_minus_four = sscale(bt3,-4)
    five_minus_four[0] = add((5,0,0,0),five_minus_four[0])
    qc = sscale(smul(smul(bt,five_minus_four,m),smul(rinv,rinv,m),m),
                 -pow(4,-1,P))
    f0,f1 = ode_pair(pc,qc,m)
    # R=t/xi=f0/(f1/t), through t^(m-1).
    reversion_factor = smul(f0[:m],sinv(f1[1:],m),m)
    lam0 = sscale(rinv,-6)
    lam1 = sscale(smul(bt,rinv,m),-6)
    # T*= -r^(2g-1), hence e-tilde(t)= -r(t)^(4g) f0(t)^3.
    et = sscale(smul(spower(rt,4*g,m),spower(f0[:m],3,m),m),-1)
    et_prime = [scale(et[j+1],j+1) for j in range(m-1)]
    D0 = [ZERO]*(m+1)
    D1 = [ZERO]*(m+1)
    ev = [ZERO]*m
    ev[0] = et[0]
    Rpow = [ONE]+[ZERO]*(m-1)
    for a in range(1,m+1):
        Rpow = smul(Rpow,reversion_factor,m)
        D0[a] = scale(coeff_product(lam0,Rpow,a-1),pow(a,-1,P))
        D1[a] = scale(coeff_product(lam1,Rpow,a-1),pow(a,-1,P))
        if a < m:
            ev[a] = scale(coeff_product(et_prime,Rpow,a-1),pow(a,-1,P))
    # Exactly the reference weights of R1199 and R1200, not binomial weights.
    fac = [1]
    for j in range(1,m+2):
        fac.append(fac[-1]*j%P)
    total0, total1 = ZERO, ZERO
    for a in range(1,m+1):
        n = m-a
        w = 2*((-1)**n)*fac[m-1]*pow(fac[a-1]*fac[n+2]%P,-1,P)%P
        total0 = add(total0,scale(mul(D0[a],ev[n]),w))
        total1 = add(total1,scale(mul(D1[a],ev[n]),w))
    pref = power(rt[0],m-2*g-1)
    return mul(pref,total0), mul(pref,total1), value(rt[0])

def compute(p):
    global P
    P = p
    assert p % 12 == 11 and p > 47
    assert all(p % d for d in range(2,math.isqrt(p)+1))
    g, m = (p+1)//12, (p-1)//2
    q = hasse_Q(g)
    A = [0]*(3*(len(q)-1)+2)
    for j,c in enumerate(q):
        A[3*j+1] = c
    Aprime = [(j+1)*A[j+1]%p for j in range(len(A)-1)]
    roots = []
    for x in range(p):
        for y in range(p):
            z = (x,y)
            z3 = fmul(fmul(z,z),z)
            if z == (0,0) or fpoly(q,z3) == (0,0):
                roots.append(z)
    assert len(roots) == m-1, ("SS root count",p,len(roots),m-1)
    sum_double = [ZERO,ZERO]
    sum_simple = [ZERO,ZERO]
    simple_nonzero = [0,0]
    rows = []
    for s in roots:
        pb0, pb1, rs = contraction_at(s,g)
        ap = value(polynomial_at(Aprime,(s[0],s[1],0,0)))
        assert ap != ZERO and rs != ZERO
        den = mul(power(rs,2*g+1),mul(ap,ap))
        den_inv = inv(den)
        simple_den_inv = inv(mul(rs,den))
        row = {"s":list(s),"components":[]}
        for i,pb in enumerate((pb0,pb1)):
            double = mul(value(pb),den_inv)
            condition = add(mul(rs,derivative(pb)),
                            scale(mul(power((s[0],s[1],0,0),2),value(pb)),m))
            simple = mul(condition,simple_den_inv)
            simple_nonzero[i] += condition != ZERO
            sum_double[i] = add(sum_double[i],double)
            sum_simple[i] = add(sum_simple[i],simple)
            row["components"].append({
                "lambda_power":i,"P":list(pb[:2]),"dP":list(pb[2:]),
                "double":list(double[:2]),"simple":list(simple[:2])})
        rows.append(row)
    assert all(z[1] == 0 for z in sum_double+sum_simple), "trace not in F_p"
    assert sum_double[0] == ZERO, "complete mu_3 orbit cancellation failed"
    c0 = (-1)**((m-1)//2)*math.comb(m-1,(m-1)//2)%p
    normalized_V = scale(add(sum_double[0],sum_double[1]),-m*c0)
    k = 4*g-1
    cartier = -sum(q[j]*(-1)**(k-j)*math.comb(m,k-j)
                  for j in range(len(q)) if 0 <= k-j <= m) % p
    canonical = json.dumps(rows,sort_keys=True,separators=(",",":")).encode()
    return {"p":p,"g":g,"m":m,"SS_count":len(roots),
            "sum_double_by_lambda_power":[z[0] for z in sum_double],
            "phase_free_V":normalized_V[0],
            "simple_nonzero_count":simple_nonzero,
            "sum_simple_by_lambda_power":[z[0] for z in sum_simple],
            "kernel_Cartier_coefficient":cartier,
            "SS_rows_sha256":hashlib.sha256(canonical).hexdigest(),
            "boundary":"Finite exact values only; phase_free_V is V/nu; no all-prime nonvanishing or C-projection claimed."}

def main():
    assert os.environ.get("GITHUB_ACTIONS") == "true", "public Actions only"
    assert os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public"
    parser = argparse.ArgumentParser()
    parser.add_argument("--primes",type=int,nargs="+",default=[59,71,83])
    args = parser.parse_args()
    assert args.primes == [59,71,83], "fixed new-functional exploration only"
    started = time.monotonic()
    results = []
    for p in args.primes:
        row = compute(p)
        results.append(row)
        print("KERNEL_CONTRACTION="+json.dumps(row,sort_keys=True),flush=True)
    canonical = json.dumps(results,sort_keys=True,separators=(",",":")).encode()
    print("KERNEL_EXPLORATION_DONE="+json.dumps({
        "results_sha256":hashlib.sha256(canonical).hexdigest(),
        "script_sha256":hashlib.sha256(open(__file__,"rb").read()).hexdigest(),
        "elapsed_seconds":round(time.monotonic()-started,3),
        "storage":"stdout only; no artifact, Release or raw repository output"
    },sort_keys=True),flush=True)

if __name__ == "__main__":
    main()
