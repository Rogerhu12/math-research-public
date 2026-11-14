#!/usr/bin/env python3
"""Actual three-state degree-six companion rows; search fixed U-degree S returns."""
import json
from pathlib import Path
import sympy as s

folder=Path(__file__).resolve().parent
x,y,V,U=s.symbols('x y V U')
b=s.Integer(1)
def red(P):
    return s.rem(s.Poly(s.expand(P),y),s.Poly(y*y-x**3-b,y)).as_expr().expand()
def D(P):
    return red(2*y*s.diff(P,x)+3*x*x*s.diff(P,y))
zd={2:-x,3:-2*y,4:-6*x*x,5:-24*x*y,6:-24*(5*x**3+2*b)}
e={k:s.expand(zd[k]*(34*(9*U)**k+(-V-280*U)**k-(-V+26*U)**k)/s.factorial(k))
   for k in range(2,7)}
E={0:s.Integer(1),1:s.Integer(0),2:e[2],3:e[3],
   4:e[4]+e[2]**2/2,5:e[5]+e[2]*e[3],
   6:e[6]+e[2]*e[4]+e[3]**2/2+e[2]**3/6}

raw443=json.loads((folder/'check-r443-residual-quarter-core.json').read_text())
def column(label,j,odd=False):
    P=sum(s.Rational(t['coefficient'])*x**t['x']
          for t in raw443[label] if t['z']==j)
    return y*P if odd else P

def contribution(P,n):
    Ds=[P]
    for k in range(6-n): Ds.append(D(Ds[-1]))
    return (V-17*U)**n*sum(E[6-n-k]*(9*U)**k/s.factorial(k)*Ds[k]
                            for k in range(7-n))

even=contribution(column('K1_even_terms',9),0)
even+=contribution(-s.Rational(6,5)*column('K1_even_terms',9),6)
for j in (6,7,8):
    even+=contribution(column('K1_even_terms',j),18-2*j)
odd=sum(contribution(-column('K1_oddodd_terms',j,True),15-2*j)
        for j in (5,6,7))
even=red(even);odd=red(odd)
assert not even.has(y) and not odd.has(y)
print('complete even and odd transported degree-six polynomials obtained',flush=True)

def matrix(P):
    poly=s.Poly(P,V,U)
    columns=[]
    for j in range(7):
        f=s.expand(poly.coeff_monomial(V**(6-j)*U**j)
                   *s.factorial(6-j)*s.factorial(j))
        assert all(m[0]%3==2 and m[0]<=17 for m,c in s.Poly(f,x).terms() if c)
        columns.append([f.coeff(x,2+3*a) for a in range(6)])
    return s.Matrix(columns).T
ME,MO=matrix(even),matrix(odd)
M1,MR=ME+MO,ME-MO
raw450=json.loads((folder/'check-r450-original-sixth-companion-moments.json').read_text())
M0=s.Matrix([[s.Rational(v) for v in row] for row in raw450['matrix']])
S=s.Matrix([-s.Rational(128,7),-s.Rational(80,7),-s.Rational(12,7),
             -s.Rational(53,7),1,0])
Dstate=s.Matrix([[0,1,-1],[1,0,1],[0,0,1]])
rows=[]
for j in range(7):
    C=M0[:,j].row_join(M1[:,j]).row_join(MR[:,j])
    ns=C.row_join(-S).nullspace()
    returns=[list(v) for v in ns if v[3]!=0]
    stable=C.row_join(-S).row_join(s.zeros(6,1)).col_join(
                (C*Dstate).row_join(s.zeros(6,1)).row_join(-S))
    stable_returns=[list(v) for v in stable.nullspace()
                    if v[3]!=0 or v[4]!=0]
    print('j',j,'rank',C.rank(),'S returns',returns,
          'D-stable returns',stable_returns,flush=True)
    plus=C*s.Matrix([1,s.Rational(1,2),-s.Rational(1,2)])
    print('common D+ state row:',list(plus),flush=True)
    rows.append({'j':j,'rank':C.rank(),
          'S_preimages':[[str(c) for c in v] for v in returns],
          'D_stable_S_preimages':[[str(c) for c in v] for v in stable_returns],
          'Dplus_original_row':[str(c) for c in plus]})

def strings(M): return [[str(c) for c in row] for row in M.tolist()]
dest=Path(__file__).with_suffix('.json')
dest.write_text(json.dumps({'normalization':raw450['normalization'],
    'M1':strings(M1),'MR':strings(MR),'Meven':strings(ME),'Modd':strings(MO),
    'fixed_U_degrees':rows},indent=2)+'\n')
print('saved',dest)
