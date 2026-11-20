#!/usr/bin/env python3
"""Exact-rational Peano constants of the literal local G16 rule."""
from pathlib import Path
from fractions import Fraction as Q
from math import comb,factorial
import argparse,json,hashlib
p=argparse.ArgumentParser();p.add_argument('--rules',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
rec=json.loads(a.rules.read_text());g=rec['G16']
pairs=sorted(((1+Q.from_float(x))/2,Q.from_float(w)/2)for x,w in zip(g['x'],g['w']))
assert all(0<t<1 and w>0 for t,w in pairs)
def polynomial(n,b):
 return [Q(comb(n,j))*(-1)**j*b**(n-j)for j in range(n+1)]
def bernstein(c,l,r):
 n=len(c)-1;h=r-l
 power=[sum((c[j]*comb(j,k)*l**(j-k)*h**k for j in range(k,n+1)),Q(0))for k in range(n+1)]
 return [sum((power[j]*Q(comb(k,j),comb(n,j))for j in range(k+1)),Q(0))for k in range(n+1)]
def split(b):
 rows=[b]
 while len(rows[-1])>1:rows.append([(x+y)/2 for x,y in zip(rows[-1],rows[-1][1:])])
 return [v[0]for v in rows],[v[-1]for v in rows[::-1]]
def int_abs(b,h,depth=0):
 if min(b)>=0:return h*sum(b)/len(b)
 if max(b)<=0:return -h*sum(b)/len(b)
 upper=h*max(abs(t)for t in b)
 if upper<Q(1,10**35)or depth>=96:return upper
 l,r=split(b);return int_abs(l,h/2,depth+1)+int_abs(r,h/2,depth+1)
def sup_abs(b,depth=0):
 if depth>=4:return max(abs(t)for t in b)
 l,r=split(b);return max(sup_abs(l,depth+1),sup_abs(r,depth+1))
bounds=[]
for k in range(2,10):
 norm=Q(0);sup=Q(0)
 grid=[Q(0)]+[t for t,w in pairs]+[Q(1)]
 for l,r in zip(grid,grid[1:]):
  c=[v/factorial(k)for v in polynomial(k,Q(1))]
  for t,w in pairs:
   if t>=r:
    z=polynomial(k-1,t)
    for j,v in enumerate(z):c[j]-=w*v/factorial(k-1)
  b=bernstein(c,l,r);norm+=int_abs(b,r-l);sup=max(sup,sup_abs(b))
 bounds.append({'order':k,'l1_upper_exact':str(norm),'sup_upper_exact':str(sup),'l1_upper':float(norm),'sup_upper':float(sup)})
moments=[Q(1,j+1)-sum((w*t**j for t,w in pairs),Q(0))for j in range(9)]
out={'scope':'Exact literal affine G16 quadrature rule; all rational Peano bounds are rigorous. Decimal display is diagnostic; use exact rationals.','rules_sha256':hashlib.sha256(a.rules.read_bytes()).hexdigest(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'nodes':16,'weight_sum_exact':str(sum((w for _,w in pairs),Q(0))),'minimum_endpoint_node_distance_exact':str(min(pairs[0][0],1-pairs[-1][0])),'moment_defects_exact':list(map(str,moments)),'peano_bounds':bounds}
a.out.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'exact_peano_constants_done','bounds':[{k:v for k,v in x.items()if not k.endswith('_exact')}for x in bounds]}))
