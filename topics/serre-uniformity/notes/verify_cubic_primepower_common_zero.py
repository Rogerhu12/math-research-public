#!/usr/bin/env python3
"""Exact arithmetic for the genuine q=5^203, ell=811 boundary example.
The rank-two extension formula is proved in the accompanying note, from
Katz's published Euler-characteristic and trace formulas. This script
checks its determinant from the degree-one and degree-two sums, then
checks every modular recurrence step. No empirical field-size cutoff.
"""
from math import gcd, isqrt
import json
p=5
# F_25 = F_5[t]/(t^2+3).
def add(a,b):return ((a[0]+b[0])%5,(a[1]+b[1])%5)
def neg(a):return (-a[0]%5,-a[1]%5)
def mul(a,b):return ((a[0]*b[0]-3*a[1]*b[1])%5,(a[0]*b[1]+a[1]*b[0])%5)
def power(a,n):
 r=(1,0)
 while n:
  if n&1:r=mul(r,a)
  a=mul(a,a);n//=2
 return r
one=(1,0);tau=(0,1);zero=(0,0)
z=power((1,1),8)
assert z!=one and power(z,3)==one
lab={power(z,i):i for i in range(3)}
f1=[lab[power((1,b),8)] for b in range(5)]
assert f1==[0,1,2,1,2]
counts2=[[0]*5 for _ in range(3)]
ram=[]
for a in range(5):
 for b in range(5):
  x=(a,b);xt=mul(x,tau);num=add(one,xt);den=add(one,neg(xt))
  if num==zero or den==zero:
   ram.append([a,b]);continue
  u=mul(num,power(den,23));col=lab[power(u,8)]
  tr=add(x,power(x,5));assert tr[1]==0
  counts2[col][tr[0]]+=1
assert len(ram)==2
# R=Z[z,xi]/(z²+z+1, Phi_5(xi)); arrays indexed by z^0,z^1 and xi^0..4.
roots=[(1,0),(0,1),(-1,-1)]
def red(a):return [[v-row[-1] for v in row[:-1]]+[0] for row in a]
def Radd(a,b):return red([[a[j][i]+b[j][i] for i in range(5)] for j in range(2)])
def Rmul(a,b):
 c=[[0]*5 for _ in range(2)]
 for i in range(5):
  for k in range(5):
   j=(i+k)%5
   c[0][j]+=a[0][i]*b[0][k]-a[1][i]*b[1][k]
   c[1][j]+=a[0][i]*b[1][k]+a[1][i]*b[0][k]-a[1][i]*b[1][k]
 return red(c)
S1=red([[roots[e][j] for e in f1] for j in range(2)])
S2=red([[counts2[0][i]-counts2[2][i] for i in range(5)],
        [counts2[1][i]-counts2[2][i] for i in range(5)]])
assert Radd(S2,Rmul(S1,S1))==[[10,0,0,0,0],[0]*5]
ell=811
assert all(ell%d for d in range(2,isqrt(ell)+1))
xi=next(power0 for g in range(2,ell) if (power0:=pow(g,(ell-1)//5,ell))!=1)
zeta=next(power0 for g in range(2,ell) if (power0:=pow(g,(ell-1)//3,ell))!=1)
assert pow(xi,5,ell)==pow(zeta,3,ell)==1
ss=[sum(pow(zeta,sgn*f1[b]%3,ell)*pow(xi,2*b%5,ell) for b in range(5))%ell for sgn in (1,-1)]
assert ss==[245,569]
old=[2,2];cur=ss[:];steps=[[0,*old],[1,*cur]]
for n in range(2,204):
 old,cur=cur,[(ss[i]*cur[i]-5*old[i])%ell for i in range(2)]
 steps.append([n,*cur])
assert cur==[0,0]
q=5**203
assert q%ell==754 and q%9==2 and ell<q
assert gcd(ell,3*q*(q*q-1))==1
# Independent binary matrix exponentiation for both Frobenius polynomials.
def matmul(a,b):return [[sum(a[i][k]*b[k][j] for k in range(2))%ell for j in range(2)] for i in range(2)]
traces=[];matrices=[]
for s in ss:
 M=[[s,-5%ell],[1,0]];R=[[1,0],[0,1]];n=203
 while n:
  if n&1:R=matmul(R,M)
  M=matmul(M,M);n//=2
 traces.append((R[0][0]+R[1][1])%ell)
 matrices.append(R)
 assert (R[0][0]*R[1][1]-R[0][1]*R[1][0])%ell==q%ell
assert traces==[0,0]
print(json.dumps(dict(base_prime=5,extension_degree=203,q=str(q),ell=ell,
    xi=xi,zeta=zeta,frequency=2,F25_cubic_root=z,F5_colours=f1,
    F25_colour_counts_by_trace=counts2,F25_ramification_points=ram,
    S1_reduced_coefficients=S1,S2_reduced_coefficients=S2,
    determinant_certificate='S2+S1^2=10 in Z[zeta3,zeta5]',
    base_fourier_pair=ss,recurrence_checkpoints=[r for r in steps if r[0] in (0,1,2,4,7,8,16,29,32,64,128,203)],
    binary_matrix_powers=matrices,binary_matrix_trace_check=traces,q_mod_ell=q%ell,q_mod_9=q%9,
    scope='Genuine full multiplicativity over a nonprime field; ell<q. Not a prime-p or actual Tate counterexample.'),indent=2))
