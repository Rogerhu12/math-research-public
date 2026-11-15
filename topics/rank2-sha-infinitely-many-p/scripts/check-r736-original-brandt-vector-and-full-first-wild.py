#!/usr/bin/env python3
"""Fixed original quaternionic vector and complete first-wild incidence.

No certificate input is read.  The default job constructs only the fixed
level-36*17^2 model.  --prime p additionally computes ALL norm-p^2 CM points
with their actual modulo-p^2 anti-Fermat digit, never a sampled branch.
Run only in the repository's public Actions workflow.
"""
import argparse, hashlib, json, math
from collections import Counter, defaultdict, deque
from fractions import Fraction
from flint import fmpq_mat

def add(x,y,m): return ((x[0]+y[0])%m,(x[1]+y[1])%m)
def neg(x,m): return ((-x[0])%m,(-x[1])%m)
def mul(x,y,m):
    a,b=x; c,d=y
    return ((a*c-b*d)%m,(a*d+b*c-b*d)%m)
def conj(x,m): return ((x[0]-x[1])%m,(-x[1])%m)
def norm(x,m=None):
    n=x[0]*x[0]-x[0]*x[1]+x[1]*x[1]
    return n if m is None else n%m
def inv(x,m):
    z=pow(norm(x,m),-1,m)
    y=conj(x,m)
    return (z*y[0]%m,z*y[1]%m)
def fpow(x,n,m):
    y=(1,0)
    while n:
        if n&1: y=mul(y,x,m)
        x=mul(x,x,m); n//=2
    return y
def kmat(x,m):
    a,b=x
    return (a%m,(-b)%m,b%m,(a-b)%m)
def mmul(A,B,m):
    a,b,c,d=A; e,f,g,h=B
    return ((a*e+b*g)%m,(a*f+b*h)%m,
            (c*e+d*g)%m,(c*f+d*h)%m)
def qmat(q,m,t):
    # j acts as t times field conjugation; N(t)=-1.
    a=(q[0],q[1]); bt=mul((q[2],q[3]),t,m)
    A=kmat(a,m); B=mmul(kmat(bt,m),(1,-1,0,-1),m)
    return tuple((A[i]+B[i])%m for i in range(4))
def mob(A,z,m):
    a,b,c,d=A
    return mul(add((a*z[0]%m,a*z[1]%m),(b,0),m),
               inv(add((c*z[0]%m,c*z[1]%m),(d,0),m),m),m)
def qconj(q): return (q[0]-q[1],-q[1],-q[2],-q[3])
def qnorm(q): return norm(q[:2])+norm(q[2:])
def qmul(q,r):
    a=q[:2]; b=q[2:]; c=r[:2]; d=r[2:]
    def em(x,y):
        A,B=x; C,D=y
        return (A*C-B*D,A*D+B*C-B*D)
    def ec(x): return (x[0]-x[1],-x[1])
    ac=em(a,c); bdc=em(b,ec(d))
    ad=em(a,d); bcc=em(b,ec(c))
    return (ac[0]-bdc[0],ac[1]-bdc[1],
            ad[0]+bcc[0],ad[1]+bcc[1])
def k3(x):
    a,b=x[0]%3,x[1]%3
    if a: return (1,b*pow(a,-1,3)%3)
    assert b
    return (0,1)
K3=((1,0),(0,1),(1,1),(1,2))
def k3mul(x,y):
    a,b=x; c,d=y
    return k3((a*c-b*d,a*d+b*c))
def q3(q): return k3((q[0]+q[1],q[2]+q[3]))
def k3conj(x): return k3((x[0],-x[1]))
def act(q,y):
    z2=(y[0],y[1]); z17=(y[2],y[3]); k=(y[4],y[5])
    w2=mob(qmat(q,2,(1,0)),z2,2)
    w17=mob(qmat(q,17,(4,0)),z17,17)
    w3=k3mul(q3(q),k)
    return w2+w17+w3
UNITS=((1,0,0,0),(0,1,0,0),(-1,-1,0,0),
       (0,0,1,0),(0,0,0,1),(0,0,-1,-1))
FULL_UNITS=UNITS+tuple(tuple(-x for x in u) for u in UNITS)
def canon(y): return min(act(u,y) for u in UNITS)
def plus(y): return (y[4]*y[4]+y[5]*y[5])%3==1
def swap2(y): return canon(conj((y[0],y[1]),2)+y[2:])
def ram3(y):
    # Right multiplication by delta at 3, followed by global delta^-1.
    # Projectively delta^-1=delta.  On O_3/delta O_3 it sends j to -j.
    dq=(1,2,0,0)
    z2=mob(qmat(dq,2,(1,0)),(y[0],y[1]),2)
    z17=mob(qmat(dq,17,(4,0)),(y[2],y[3]),17)
    return canon(z2+z17+k3conj((y[4],y[5])))
def norm_elements(n):
    by=defaultdict(list)
    B=2*math.isqrt(n)+2
    for b in range(-B,B+1):
        disc=4*n-3*b*b
        if disc<0: continue
        r=math.isqrt(disc)
        for a in range((b-r+1)//2,(b+r)//2+1):
            z=(a,b); nz=norm(z)
            if nz<=n: by[nz].append(z)
    out=[]
    for aN,aa in by.items():
        bb=by.get(n-aN,())
        for a in aa:
            for b in bb: out.append(a+b)
    out.sort()
    assert all(qnorm(q)==n for q in out)
    return out
def a_ell(ell):
    count=1
    for x in range(ell):
        v=(x*x*x+17)%ell
        count+=1 if not v else (2 if pow(v,(ell-1)//2,ell)==1 else 0)
    return ell+1-count
def nullspace(M):
    R,r=M.rref(); r=int(r)
    piv=[]
    for i in range(r):
        piv.append(next(j for j in range(R.ncols()) if R[i,j]))
        assert R[i,piv[-1]]==1
    free=[j for j in range(R.ncols()) if j not in set(piv)]
    N=fmpq_mat(R.ncols(),len(free))
    for c,j in enumerate(free):
        N[j,c]=1
        for i,k in enumerate(piv): N[k,c]=-R[i,j]
    MN=M*N
    assert all(MN[i,j]==0 for i in range(MN.nrows()) for j in range(MN.ncols()))
    return N
def build_model():
    raw=[(a,b,c,d)+k for a in range(2) for b in (1,)
         for c in range(17) for d in range(1,17) for k in K3]
    X=sorted({canon(y) for y in raw}); ix={x:i for i,x in enumerate(X)}
    assert len(raw)==2176 and len(X)==368
    assert sum(plus(x) for x in X)==184
    # Integer signed orbit basis: norm plus, sign at 2, toric delta at 3.
    labels={}; representatives=[]
    for x in X:
        if not plus(x) or x in labels: continue
        lab=len(representatives); representatives.append(x)
        labels[x]=(lab,1); todo=deque([x])
        while todo:
            z=todo.popleft(); _,sg=labels[z]
            for nxt,factor in ((swap2(z),-1),(ram3(z),1)):
                want=(lab,sg*factor)
                if nxt in labels: assert labels[nxt]==want
                else: labels[nxt]=want; todo.append(nxt)
    assert len(representatives)==47
    B=fmpq_mat(len(X),47)
    for x,(c,s) in labels.items(): B[ix[x],c]=s
    return X,ix,B,representatives

def fixed_vector():
    X,ix,B,reps=build_model()
    ranks=[]
    # Every step includes all 368 target rows, including the opposite norm fibre.
    for ell in (5,7,11,13,19,31,37,43):
        qs=norm_elements(ell)
        assert len(qs)==12*(ell+1)
        T=fmpq_mat(len(X),B.ncols())
        for i,x in enumerate(X):
            for q in qs:
                j=ix[canon(act(qconj(q),x))]
                for k in range(B.ncols()): T[i,k]+=B[j,k]
        T=T/12
        eig=a_ell(ell)
        K=nullspace(T-B*eig)
        ranks.append({"ell":ell,"a_ell":eig,"before":B.ncols(),"after":K.ncols()})
        B=B*K
        assert B.ncols()>0, "Original E17 vector must survive the exact constraints"
        if B.ncols()==1:
            break
    assert B.ncols()==1, "More fixed good Hecke constraints are required"
    den=1
    for i in range(len(X)): den=math.lcm(den,Fraction(str(B[i,0])).denominator)
    vals=[int(Fraction(str(B[i,0]))*den) for i in range(len(X))]
    g=0
    for a in vals: g=math.gcd(g,a)
    vals=[a//g for a in vals]
    if next(a for a in vals if a)!=abs(next(a for a in vals if a)):
        vals=[-a for a in vals]
    base=canon((1,1,1,1,1,0)) # fixed eigenline 1+omega of multiplication by omega
    assert vals[ix[base]]==0, "Original class-number-one central value is zero"
    assert all(not vals[i] for i,x in enumerate(X) if not plus(x))
    assert all(vals[ix[swap2(x)]]==-vals[i] and vals[ix[ram3(x)]]==vals[i]
               for i,x in enumerate(X))
    return X,ix,vals,reps,ranks,base

def lift_j(p):
    # Deterministic norm(-1) element over Z/p^2; no primitive-root assumption.
    t=None
    for a in range(p):
        for b in range(p):
            if norm((a,b),p)==p-1:
                t=(a,b); break
        if t is not None: break
    a,b=t; e=(norm(t)+1)//p
    A=(2*a-b)%p; B=(2*b-a)%p
    if A: a+=p*((-e*pow(A,-1,p))%p)
    else: b+=p*((-e*pow(B,-1,p))%p)
    out=(a%(p*p),b%(p*p))
    assert norm(out,p*p)==p*p-1
    return out
def wild_digit(z,p):
    pp=p*p
    u=mul(fpow(z,p,pp),inv(conj(z,pp),pp),pp)
    assert (u[0]-1)%p==0 and u[1]%p==0
    q=(((u[0]-1)//p)%p,(u[1]//p)%p)
    qa=add(q,neg(conj(q,p),p),p)
    v=mul(qa,inv((1,2),p),p)
    assert v[1]==0
    return (-34*v[0])%p
def all_first_wild(p,X,ix,vals,base):
    assert p>19 and p%6==5 and all(p%d for d in range(2,math.isqrt(p)+1))
    pp=p*p; t=lift_j(p)
    sums=[0]*p; squares=0; counts=[0]*p
    pointmap={}
    for q in norm_elements(pp):
        if all(a%p==0 for a in q): continue
        A=qmat(q,pp,t)
        v=(A[0],A[2]) if (A[0]%p or A[2]%p) else (A[1],A[3])
        assert v[0]%p or v[1]%p
        if v[0]%p: key=(1,v[1]*pow(v[0],-1,pp)%pp)
        else: key=(v[0]*pow(v[1],-1,pp)%pp,1)
        digit=wild_digit(v,p)
        value=vals[ix[canon(act(qconj(q),base))]]
        if key in pointmap: assert pointmap[key]==(digit,value)
        else: pointmap[key]=(digit,value)
        sums[digit]+=value; counts[digit]+=1; squares+=value*value
    assert len(pointmap)==p*(p+1)
    assert counts==[12*(p+1)]*p
    assert all(a%36==0 for a in sums) and squares%36==0
    A=[a//36 for a in sums]
    D=squares//36
    assert sum(A)==-(p+1)*vals[ix[base]]//3
    # Every branch is doubled by the original ramified toric class.
    assert all(a%2==0 for a in A)
    S=sum(a*a for a in A)
    return {"p":p,"CM_points":p*(p+1)//3,"A_t":A,"D_p":D,
            "sum_A":sum(A),"sum_A_squared":S,"remaining_sync_after_two_diagonals":S-2*D,
            "all_first_wild_zero":not any(A),
            "local_j_norm":norm(t,pp),"full_p2_matching":True}
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--prime",type=int,action="append",default=[])
    args=ap.parse_args()
    X,ix,vals,reps,ranks,base=fixed_vector()
    table=[{"class":list(x),"f":vals[i]} for i,x in enumerate(X)]
    canonical=json.dumps(table,sort_keys=True,separators=(",",":")).encode()
    mass=sum((Fraction(1,sum(act(u,x)==x for u in UNITS)) for x in X if plus(x)),Fraction(0))
    energy=sum((Fraction(vals[i]*vals[i],sum(act(u,x)==x for u in UNITS)) for i,x in enumerate(X) if plus(x)),Fraction(0))
    assert mass==Fraction(544,3)
    summary={"norm_fibre_mass":str(mass),"fixed_c_f":str(energy/mass),"model":"K+Kj, j^2=-1; R=OK+34delta OKj",
             "raw_cosets":2176,"ideal_classes":368,"norm_plus":184,
             "fixed_toric_sign_dimension":47,"Hecke_kernel_dimensions":ranks,
             "primitive_integer_value_distribution":dict(sorted(Counter(vals).items())),
             "base_value":vals[ix[base]],"fixed_table_sha256":hashlib.sha256(canonical).hexdigest(),
             "fixed_47_values":[{"class":list(x),"f":vals[ix[x]]} for x in reps],
             "prime_records":[all_first_wild(p,X,ix,vals,base) for p in args.prime]}
    print(json.dumps(summary,sort_keys=True,separators=(",",":")))
if __name__=="__main__": main()
