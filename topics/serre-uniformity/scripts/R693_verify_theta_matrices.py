#!/usr/bin/env python3
"""Exact finite algebra in Q(i,sqrt(3)) for the actual R693 theta square.

This verifies all finite identities in the proof.  The analytic Poisson
identities are proved in the text and are not inferred from a numerical test.
"""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
from hashlib import sha256
import argparse,json

def e(a=0,b=0,c=0,d=0): return tuple(map(F,(a,b,c,d)))
Z=e();ONE=e(1);B=e(0,1);I=e(0,0,1);IB=e(0,0,0,1)
def add(x,y): return tuple(a+b for a,b in zip(x,y))
def scale(x,c): return tuple(a*F(c) for a in x)
def sub(x,y): return add(x,scale(y,-1))
def mul(x,y):
    z=[F(0)]*4
    for r,a in enumerate(x):
        for s,b in enumerate(y):
            z[r^s]+=a*b*(3 if r&s&1 else 1)*(-1 if r&s&2 else 1)
    return tuple(z)
def power(x,n):
    z=ONE
    while n:
        if n&1:z=mul(z,x)
        x=mul(x,x);n//=2
    return z
def sum_e(xs):
    a=Z
    for x in xs:a=add(a,x)
    return a
def mv(A,v):return [sum_e(mul(a,b) for a,b in zip(row,v)) for row in A]
def quad(A,v):return sum_e(mul(v[i],x) for i,x in enumerate(mv(A,v)))
def det(A):
    n=len(A);ans=Z
    for p in permutations(range(n)):
        s=(-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        t=ONE
        for i in range(n):t=mul(t,A[i][p[i]])
        ans=add(ans,scale(t,s))
    return ans
def strings(x):return [str(a) for a in x]

def run():
    # u=exp(-pi*i/3), t=exp(pi*i/6), om=exp(pi*i/3).
    u=e(F(1,2),0,0,F(-1,2));t=e(0,F(1,2),F(1,2));om=e(F(1,2),0,0,F(1,2))
    assert power(u,6)==ONE and power(t,12)==ONE
    kap=[[e(F(3,72),F(-((-1)**r+(-1)**s),72),0,F(-(-1)**(r+s),72))
          for s in range(6)] for r in range(6)]
    for M in range(6):
        for N in range(6):
            actual=sum_e(mul(kap[r][s],power(om,(M*s+N*r)%6))
                         for r in range(6) for s in range(6))
            expected={(0,0):e(F(3,2)),(3,0):scale(B,F(-1,2)),
                      (0,3):scale(B,F(-1,2)),(3,3):scale(IB,F(-1,2))}.get((M,N),Z)
            assert actual==expected,(M,N,actual,expected)
    mat=[[mul(kap[r][s],power(u,(r*s)%6)) for s in range(6)] for r in range(6)]
    FD=[[mul(power(u,(r*s)%6),power(t,(s*s)%12)) for s in range(6)] for r in range(6)]
    ao=e(F(1,2),F(1,2),F(1,2),F(1,2))
    vo=[Z,ao,ONE,Z,scale(ONE,-1),scale(ao,-1)]
    be=e(F(1,2),F(-1,2),F(-1,2),F(1,2))
    ce=e(F(1,4),0,0,F(-1,4));de=e(F(1,2),F(-1,4),F(1,4))
    ve=[be,ce,de,ONE,de,ce]
    lam_o=e(0,1,0,-1);lam_e=scale(lam_o,-1)
    assert mv(FD,vo)==[mul(lam_o,x) for x in vo]
    assert mv(FD,ve)==[mul(lam_e,x) for x in ve]
    qo=e(1,F(1,2),F(-1,2));qe=e(F(3,8),F(-3,8),F(-3,8),F(3,8))
    assert quad(mat,vo)==qo and quad(mat,ve)==qe
    odd_entry=sub(sub(FD[1][1],FD[1][5]),lam_o)
    assert odd_entry==e(0,F(-1,2),F(-3,2),1) and odd_entry!=Z
    # First three columns in the even parity basis (v0,v1,v2,v3).
    A=[]
    for r in range(3):
        row=[]
        for c,indices in enumerate([[0],[1,5],[2,4]]):
            val=sum_e(FD[r][j] for j in indices)
            if r in indices:val=sub(val,lam_e)
            row.append(val)
        A.append(row)
    minor=det(A)
    assert minor==e(0,-6,-18,-12) and minor!=Z
    return {'result':'R693','coefficient_basis':['1','sqrt(3)','i','i*sqrt(3)'],
            'kernel_fourier_entries_checked':36,'theta_eigenvector_identities':True,
            'odd_rank_minor':strings(odd_entry),'even_rank_minor':strings(minor),
            'odd_quadratic_scalar':strings(qo),'even_quadratic_scalar':strings(qe),
            'all_finite_identities_verified':True,
            'analytic_identities_inferred_from_computation':False,
            'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args();r=run();a.output.write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps(r))
