#!/usr/bin/env python3
"""Verify the entire first bad band against confluent derivative jets.

The test uses the same prime p=103, with degree 7 and nine bad rows.
All ordinary coefficients through z^140 are computed in Q(i).  The
normalized bad rows are computed from exact powers of the actual graph,
then compared with the separate derivative-row formula from the note.
"""
from contextlib import redirect_stdout
from io import StringIO
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json
import runpy

root=Path(__file__).resolve().parents[1]
with redirect_stdout(StringIO()):
    env=runpy.run_path(str(root/'scripts/check-inert-saturated-plane-jet.py'))
flow=env['flow']; add=env['add']; neg=env['neg']; mul=env['mul']; red=env['red']
fa=env['fa']; fn=env['fn']; fm=env['fm']; fi=env['fi']; rref=env['rref']
p,r,degree,q=103,26,7,9
stop=r+q
zero,one=(F(0),F(0)),(F(1),F(0));Z,O=(0,0),(1,0)
h=flow['coefficients'](4*stop,1)
theta=flow['universal_sigma_theta'](4*stop)[1]
f=[];power=(1,0)
for n in range(stop+1):
    f.append((F(theta[4*n]*power[0],factorial(4*n)),F(theta[4*n]*power[1],factorial(4*n))))
    power=mul(power,(161,-240))
y=[zero];psi=[zero]
for n in range(1,stop+1):
    numerator=F(h[4*n],n*factorial(4*n))
    val=(numerator,F(0));pv=(numerator/F(4*n+1),F(0))
    for j in range(1,n+1):
        val=add(val,neg(mul(f[j],y[n-j])))
        if n<=q:
            pv=add(pv,neg(mul(f[j],psi[n-j])))
    y.append(val)
    if n<=q:
        psi.append(pv)
powers=[[one]+[zero]*stop]
for j in range(1,degree+1):
    cur=[zero]*(stop+1)
    for n in range(stop+1):
        for m in range(n+1):
            if powers[-1][m]!=zero and y[n-m]!=zero:
                cur[n]=add(cur[n],mul(powers[-1][m],y[n-m]))
    powers.append(cur)
cols=[(d-j,j) for d in range(degree+1) for j in range(d+1)]
prefix=[[red(powers[j][n-i]) if n>=i else Z for i,j in cols] for n in range(r+1)]
actual=[]
for n in range(r+1,r+q+1):
    actual.append([red(mul((p,0),powers[j][n-i])) if n>=i else Z for i,j in cols])
derivative=[]
for n in range(q):
    derivative.append([red(mul((j,0),powers[j-1][n-i])) if j>0 and n>=i else Z for i,j in cols])
psimod=[red(x) for x in psi]
factor=fn(red(mul((p,0),f[r])))  # -pa, independently from the reference.
predicted=[]
for s in range(1,q+1):
    row=[]
    for k in range(len(cols)):
        v=Z
        for ell in range(s):
            v=fa(v,fm(factor,fm(psimod[s-ell],derivative[ell][k])))
        row.append(v)
    predicted.append(row)
assert actual==predicted
rank_sequence=[]
for j in range(q+1):
    _,piv,det=rref(prefix+actual[:j])
    rank_sequence.append(len(piv))
_,piv,detactual=rref(prefix+actual)
_,pivc,detconfluent=rref(prefix+derivative)
assert factor == (42, 0)
assert rank_sequence == list(range(27, 37))
assert detactual == (93, 31)
assert detconfluent == (61, 89)
assert fm(factor, psimod[1]) == (29, 0)
print(json.dumps({'p':p,'degree':degree,'r':r,'q':q,'columns':len(cols),'factor_minus_pa':factor,
    'rank_sequence':rank_sequence,'full_scaled_determinant':detactual,
    'confluent_determinant':detconfluent,'triangular_diagonal':fm(factor,psimod[1]),
    'first_bad_band_verified':True,
    'ordinary_smith_exponents':[-1]*9+[0]*27},separators=(',',':')))
