#!/usr/bin/env python3
"""Exact second-band Bockstein and its central-coefficient deformation.

Only p=103 is used.  Ordinary coefficients through z^212 are obtained
from the fixed integer flow.  The old 53 rows are saturated before the
new divided row is restricted to their two-dimensional kernel.
"""
from contextlib import redirect_stdout
from io import StringIO
from fractions import Fraction as F
from math import factorial,comb
from pathlib import Path
import json,runpy

root=Path(__file__).resolve().parents[1]
with redirect_stdout(StringIO()):e=runpy.run_path(str(root/'scripts/check-inert-saturated-plane-jet.py'))
flow=e['flow'];add=e['add'];neg=e['neg'];mul=e['mul'];red=e['red']
fa=e['fa'];fn=e['fn'];fm=e['fm'];fi=e['fi'];rref=e['rref']
p,r,D=103,26,9;stop=2*r+1
zero,one=(F(0),F(0)),(F(1),F(0));Z,O=(0,0),(1,0)
h=flow['coefficients'](4*stop,1);theta=flow['universal_sigma_theta'](4*stop)[1]
f=[];power=(1,0)
for n in range(stop+1):
 f.append((F(theta[4*n]*power[0],factorial(4*n)),F(theta[4*n]*power[1],factorial(4*n))))
 power=mul(power,(161,-240))
y=[zero];finv=[one]
for n in range(1,stop+1):
 val=(F(h[4*n],n*factorial(4*n)),F(0));iv=zero
 for j in range(1,n+1):
  val=add(val,neg(mul(f[j],y[n-j])))
  iv=add(iv,neg(mul(f[j],finv[n-j])))
 y.append(val);finv.append(iv)
powers=[[one]+[zero]*stop]
for j in range(1,D+1):
 cur=[zero]*(stop+1)
 for n in range(stop+1):
  for k in range(n+1):
   if powers[-1][k]!=zero and y[n-k]!=zero:
    cur[n]=add(cur[n],mul(powers[-1][k],y[n-k]))
 powers.append(cur)
cols=[(d-j,j) for d in range(D+1) for j in range(d+1)]
prefix=[[red(powers[j][n-i]) if n>=i else Z for i,j in cols] for n in range(r+1)]
oldbad=[[red(mul((p,0),powers[j][n-i])) if n>=i else Z for i,j in cols] for n in range(r+1,2*r+1)]
rr,piv,detold=rref(prefix+oldbad)
free=[j for j in range(len(cols)) if j not in piv]
kernels=[]
for j in free:
 v=[Z]*len(cols);v[j]=O
 for i,c in enumerate(piv):v[c]=fn(rr[i][j])
 kernels.append(v)
a0=f[r];pa0=mul((p,0),a0)
row=[]
for i,j in cols:
 val=mul((p,0),powers[j][stop-i]) if stop>=i else zero
 if r+1>=i:
  val=add(val,mul(mul((F(p,6),0),a0),powers[j][r+1-i]))
 row.append(red(val))
def dot(x,v):
 out=Z
 for a,b in zip(x,v):out=fa(out,fm(a,b))
 return out
values=[dot(row,v) for v in kernels]
pyy=[fm((2,0),v[cols.index((0,2))]) for v in kernels]

# Exact deformation G -> G+w^r, with the chosen exponential a0.
change=[zero]*(stop+1)
for n in range(r,stop+1):
 change[n]=mul((F(1,r),0),finv[n-r])
 if n>=2*r:change[n]=add(change[n],mul(mul((F(1,2*r),0),a0),finv[n-2*r]))
change2=[zero]*(stop+1)
for n in range(2*r,stop+1):
 for k in range(r,n-r+1):change2[n]=add(change2[n],mul(change[k],change[n-k]))
def variation(n,i,j):
 if n<i or j==0:return zero
 n-=i;ans=zero
 for k in range(r,n+1):
  ans=add(ans,mul((j,0),mul(change[k],powers[j-1][n-k])))
 if j>=2:
  for k in range(2*r,n+1):
   ans=add(ans,mul((comb(j,2),0),mul(change2[k],powers[j-2][n-k])))
 return ans
drow=[]
for i,j in cols:
 val=mul((p,0),variation(stop,i,j))
 val=add(val,mul(mul((F(p,6),0),a0),variation(r+1,i,j)))
 drow.append(red(val))
deformed=[dot(drow,v) for v in kernels]
factor=fm(fn(red(pa0)),fi((5*r%p,0)))
assert deformed==[fm(factor,x) for x in pyy]
det2=fa(fm(values[0],pyy[1]),fn(fm(values[1],pyy[0]))) if len(values)==2 else None
assert len(piv) == 53 and free == [53, 54]
assert detold == (43, 48)
assert red(pa0) == (61, 0)
assert pyy == [(60, 50), (38, 102)]
assert values == [(59, 6), (1, 24)]
assert det2 == (92, 18)
assert factor == (13, 0)
assert deformed == [(59, 32), (82, 90)]
print(json.dumps({'p':p,'D':D,'old_rows':2*r+1,'columns':len(cols),'old_scaled_rank':len(piv),
 'old_unit_minor':detold,'free_columns':free,'pa0':red(pa0),
 'beta_p_plus_1':red((F(h[4*r],factorial(4*r)),F(0))),
 'Pyy_kernel':pyy,'bockstein_kernel':values,'bockstein_vs_Pyy_determinant':det2,
 'deformation_factor':factor,'deformation_kernel':deformed},separators=(',',':')))
