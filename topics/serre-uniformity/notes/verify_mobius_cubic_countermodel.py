#!/usr/bin/env python3
"""An abstract cubic-colouring test, not an actual Cartan character.

Keeps the true order-three Cartan Mobius covariance, W-invariance,
reflection/inverse covariance, balance, and Tate-compatible ell=6p+1.
Finds whether these constraints alone force paired Fourier nonvanishing.
"""
from itertools import product
from math import isqrt
import json

P=263
ELL=1579
INF=P
assert all(P%d for d in range(2,isqrt(P)+1))
assert all(ELL%d for d in range(2,isqrt(ELL)+1))
assert ELL==6*P+1 and ELL%3==1
assert (P*P-1)%3==0 and (P*P-1)%9!=0

def fp2_mul(a,b):
    return ((a[0]*b[0]-3*a[1]*b[1])%P,
            (a[0]*b[1]+a[1]*b[0])%P)

def fp2_pow(a,n):
    b=(1,0)
    while n:
        if n&1:b=fp2_mul(b,a)
        a=fp2_mul(a,a)
        n//=2
    return b

def T(b):
    if b==INF:return (-pow(3,-1,P))%P
    if (1-3*b)%P==0:return INF
    return (b+1)*pow(1-3*b,-1,P)%P

def W(b):
    if b==INF:return 0
    if b==0:return INF
    return -pow(3*b,-1,P)%P

def R(b):return INF if b==INF else (-b)%P
assert all(T(T(T(b)))==b and W(W(b))==b and R(R(b))==b
           and T(W(b))==W(T(b)) and R(T(R(b)))==T(T(b))
           and R(W(R(b)))==W(b) for b in range(P+1))

ZETA=fp2_pow((1,1),(P*P-1)//3)
assert ZETA!=(1,0) and fp2_pow(ZETA,3)==(1,0)
colours={fp2_pow(ZETA,i):i for i in range(3)}
base={b:colours[fp2_pow((1,b),(P*P-1)//3)] for b in range(P)}
base[INF]=0
assert all(base[T(b)]==(base[b]+1)%3 for b in range(P+1))
assert all(base[W(b)]==base[b] for b in range(P+1))
assert all(base[R(b)]==(-base[b])%3 for b in range(P+1))

orbits=[]
remaining=set(range(P+1))
while remaining:
    start=min(remaining)
    orbit=set()
    todo=[start]
    while todo:
        b=todo.pop()
        if b in orbit:continue
        orbit.add(b)
        todo.extend([T(b),W(b)])
    assert len(orbit)==6
    remaining-=orbit
    orbits.append(tuple(sorted(orbit)))
index={b:i for i,o in enumerate(orbits) for b in o}
mirror=[index[R(o[0])] for o in orbits]
assert all(set(orbits[mirror[i]])=={R(b) for b in o} for i,o in enumerate(orbits))

# F_ell[z]/(z^2+z+1), an etale rank-two algebra.
# A zero pair is equivalent to zero at both choices of a primitive cube root.
def add(a,b):return ((a[0]+b[0])%ELL,(a[1]+b[1])%ELL)
def neg(a):return ((-a[0])%ELL,(-a[1])%ELL)
def mul(a,b):
    return ((a[0]*b[0]-a[1]*b[1])%ELL,
            (a[0]*b[1]+a[1]*b[0]-a[1]*b[1])%ELL)
zeta=[(1,0),(0,1),(-1%ELL,-1%ELL)]
XI=64
assert pow(XI,P,ELL)==1 and XI!=1
def orbit_sum(o):
    ans=(0,0)
    for b in o:
        if b!=INF:ans=add(ans,mul(zeta[base[b]],(pow(XI,b,ELL),0)))
    return ans
sums=[orbit_sum(o) for o in orbits]
fixed=(0,0)
variables=[]
for i,o in enumerate(orbits):
    j=mirror[i]
    if j==i:fixed=add(fixed,sums[i])
    elif i<j:
        options=[add(mul(zeta[a],sums[i]),mul(zeta[-a%3],sums[j])) for a in range(3)]
        variables.append((i,j,options))

def combine(vs):
    for choices in product(range(3),repeat=len(vs)):
        value=(0,0)
        for var,a in zip(vs,choices):value=add(value,var[2][a])
        yield value,choices
cut=len(variables)//2
left={v:c for v,c in combine(variables[:cut])}
answer=None
for value,choices in combine(variables[cut:]):
    target=neg(add(fixed,value))
    if target in left:
        answer=left[target]+choices
        break
assert answer is not None
phases=[0]*len(orbits)
for (i,j,_),a in zip(variables,answer):phases[i]=a;phases[j]=-a%3
fake={b:(base[b]+phases[index[b]])%3 for b in range(P+1)}
assert fake[0]==fake[INF]==0
assert all(fake[T(b)]==(fake[b]+1)%3 for b in range(P+1))
assert all(fake[W(b)]==fake[b] for b in range(P+1))
assert all(fake[R(b)]==(-fake[b])%3 for b in range(P+1))
assert [sum(fake[b]==i for b in range(P+1)) for i in range(3)]==[(P+1)//3]*3
fourier=[sum(pow(XI,b,ELL) for b in range(P) if fake[b]==i)%ELL for i in range(3)]
assert fourier==[0,0,0]
def g(t,b):
    if b==INF:return INF if t==0 else -pow(3*t,-1,P)%P
    if (1-3*t*b)%P==0:return INF
    return (b+t)*pow(1-3*t*b,-1,P)%P
witness=next((t,b,g(t,b),fake[t],fake[b],fake[g(t,b)])
             for t in range(P) for b in range(P+1)
             if fake[g(t,b)]!=(fake[t]+fake[b])%3)
payload=dict(p=P,ell=ELL,xi=XI,zeta_relation='zeta^2+zeta+1=0',
    base_zeta_fp2=list(ZETA),variables=len(variables),
    orbit_representatives=[o[0] for o in orbits],orbit_phases=phases,
    colour_sets=[[b for b in range(P) if fake[b]==i] for i in range(3)],
    three_fourier_sums=fourier,
    actual_cartan_three_fourier_sums=[sum(pow(XI,b,ELL) for b in range(P) if base[b]==i)%ELL for i in range(3)],
    failure_of_full_cartan_covariance=dict(zip(['t','b','image','colour_t','colour_b','colour_image'],witness)),
    scope='Counterexample only to the restricted identity package; not an actual Cartan exception.')
print(json.dumps(payload,indent=2))
