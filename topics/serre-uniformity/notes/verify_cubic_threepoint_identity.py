#!/usr/bin/env python3
"""Exact checks for the full-multiplicativity cubic three-point identity.

Reads the separate abstract countermodel, verifies genuine identities for
the actual Cartan character, and displays which one the countermodel fails.
No curve-existence or actual exceptional-prime claim is made.
"""
from pathlib import Path
import json

data=json.loads(Path(__file__).with_name('cartan_order_three_countermodel.json').read_text())
p,ell,xi=data['p'],data['ell'],data['xi']
iv=[0]+[pow(x,-1,p) for x in range(1,p)]
def times(a,b):return ((a[0]*b[0]-3*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
def power(a,n):
    out=(1,0)
    while n:
        if n&1:out=times(out,a)
        a=times(a,a);n//=2
    return out
z=tuple(data['base_zeta_fp2'])
labels={power(z,i):i for i in range(3)}
actual={b:labels[power((1,b),(p*p-1)//3)] for b in range(p)}
actual[p]=0
fake={b:j for j,subset in enumerate(data['colour_sets']) for b in subset}
fake[p]=0
def phi(table,a,b):
    a%=p;b%=p
    if a:return table[b*iv[a]%p]
    return 0 if b else None
roots=[(1,0),(0,1),(-1,-1)]
def corr(table,abc):
    counts=[0,0,0]
    for x in range(p):
        for y in range(p):
            v=[phi(table,x-a,y-b) for a,b in abc]
            if None not in v:counts[sum(v)%3]+=1
    return (counts[0]-counts[2],counts[1]-counts[2])
def rhs(table,abc):
    cs=[phi(table,abc[i][0]-abc[(i+1)%3][0],abc[i][1]-abc[(i+1)%3][1]) for i in range(3)]
    r=(0,0) if None in cs else roots[-sum(cs)%3]
    return (p*r[0]-1+(p*p if abc[0]==abc[1]==abc[2] else 0),p*r[1])
examples=[]
for abc in [((0,0),(1,0),(2,0)),((0,0),(1,0),(0,1)),
            ((0,0),(1,0),(1,1)),((0,0),(1,0),(0,0)),
            ((0,0),(0,0),(0,0))]:
    value=corr(actual,abc)
    assert value==rhs(actual,abc)
    examples.append(dict(points=abc,actual=value,countermodel=corr(fake,abc),
                         countermodel_expected_if_identity_held=rhs(fake,abc)))

def add(a,b):return ((a[0]+b[0])%ell,(a[1]+b[1])%ell)
def mul(a,b):return ((a[0]*b[0]-a[1]*b[1])%ell,
                    (a[0]*b[1]+a[1]*b[0]-a[1]*b[1])%ell)
xp=[pow(xi,i,ell) for i in range(p)]
def dft(table):
    out=[]
    for a in range(p):
        u=v=0
        for b in range(p):
            w=xp[a*b%p]
            c=roots[table[b]]
            u+=w*c[0];v+=w*c[1]
        out.append((u%ell,v%ell))
    return out
def moment(S,t):
    ans=(0,0)
    for w in range(1,p):
        ans=add(ans,mul(mul(S[(t-1)*w%p],S[-t*w%p]),S[w]))
    return ans
sa,sf=dft(actual),dft(fake)
assert sf[1]==sf[-1]==(0,0)
moments=[]
for t in [0,1,2,3,p-1]:
    r=moment(sa,t)
    expected=((p+1 if t in [0,1] else (p+1)**2)%ell,0)
    assert r==expected
    moments.append(dict(t=t,actual=r,countermodel=moment(sf,t)))
print(json.dumps(dict(p=p,ell=ell,three_point_examples=examples,
                      multiplicative_fourier_moments=moments,
                      actual_identity_verified=True,
                      countermodel_violates_full_identity=True),indent=2))
