"""Exact normalization check for R177, one fixed p and coefficient field.
The general theorem is proved in the mathematical text; this is not a scan.
"""
from math import isqrt
from pathlib import Path
import json
p,z,a,ell=41,3,1,1723
d=(p+1)//3
assert all(ell%r for r in range(2,isqrt(ell)+1))
assert (ell-1)%p==0 and pow(z,(p-1)//2,p)==p-1
prime_factors=(2,3,7,41)
cgen=next(g for g in range(2,ell) if all(pow(g,(ell-1)//r,ell)!=1 for r in prime_factors))
psi=pow(cgen,(ell-1)//p,ell)
ps=[pow(psi,j,ell) for j in range(p)]
ai=pow(a,-1,p); pi=pow(p,-1,ell); di=pow(d,-1,ell)

def fm(u,v):return ((u[0]*v[0]+z*u[1]*v[1])%p,(u[0]*v[1]+u[1]*v[0])%p)
def fp(v,n):
 r=(1,0)
 while n:
  if n&1:r=fm(r,v)
  v=fm(v,v);n//=2
 return r

def norm(v):return (v[0]*v[0]-z*v[1]*v[1])%p
H=[t for t in range(p) if fp((t,1),(p*p-1)//3)==(1,0)]
assert len(H)==d-1 and 0 in H
AH=[sum(ps[t*y%p] for t in H)%ell for y in range(p)]
root=next(r for r in range(p) if z*r*r%p==(-3)%p)
zeta=((-pow(2,-1,p))%p,root*pow(2,-1,p)%p)
assert fp(zeta,3)==(1,0) and zeta!=(1,0) and norm(zeta)==1
mu6=[]
for j in range(3):
 v=fp(zeta,j);mu6.extend([v,(-v[0]%p,-v[1]%p)])
assert len(set(mu6))==6

I=[[int(i==j) for j in range(p)] for i in range(p)]
R=[[int(i==(-j)%p) for j in range(p)] for i in range(p)]
def mm(A,B):
 BT=list(zip(*B))
 return [[sum(x*y for x,y in zip(row,col))%ell for col in BT] for row in A]
def rank(A):
 A=[r[:] for r in A];n=len(A);m=len(A[0]);r=0
 for j in range(m):
  s=next((i for i in range(r,n) if A[i][j]),None)
  if s is None:continue
  A[r],A[s]=A[s],A[r];iv=pow(A[r][j],-1,ell)
  A[r]=[x*iv%ell for x in A[r]]
  for i in range(n):
   if i!=r and A[i][j]:
    v=A[i][j];A[i]=[(x-v*y)%ell for x,y in zip(A[i],A[r])]
  r+=1
  if r==n:break
 return r

def D(v):
 x,y=v;A=[[0]*p for _ in range(p)]
 for j in range(p):A[(j+x)%p][j]=ps[(-2*z*x*y-4*z*j*y)*ai%p]
 return A
cache={}
def K(t):
 t%=p
 if t not in cache:
  cache[t]=[[(-pi*ps[t*(r-j)*(r-j)*ai%p]*sum(ps[(-t*z*y*y-2*z*(r+j)*y)*ai%p] for y in range(p)))%ell
             for j in range(p)] for r in range(p)]
 return cache[t]
assert K(0)==[[(-x)%ell for x in row] for row in R]
for t,s in ((1,2),(3,5),(7,-7)):
 expect=I if (t+s)%p==0 else K((t*s+z)*pow((t+s)%p,-1,p))
 assert mm(K(t),K(s))==expect
P=[[di*(I[r][j]+sum(K(t)[r][j] for t in H))%ell for j in range(p)] for r in range(p)]
assert mm(P,P)==P and rank(P)==2
assert mm(P,R)==[[(-x)%ell for x in row] for row in P]
Ds=[D((a*v[0]%p,a*v[1]%p)) for v in mu6]
Q=[[sum(M[r][j] for M in Ds)%ell for j in range(p)] for r in range(p)]
PQ=mm(P,Q)
assert any(any(row) for row in PQ)
coeff_count=0
orbit={(a*v[0]%p,a*v[1]%p) for v in mu6}
for x in range(p):
 for y in range(p):
  F=0
  for kap in mu6:
   u=fm((x,y),kap)
   F+=ps[-2*z*u[1]%p]*AH[norm(((u[0]-a)%p,u[1]))*ai%p]
  expected=di*(int((x,y) in orbit)-pi*F)%ell
  actual=pi*sum(ps[(2*z*x*y+4*z*j*y)*ai%p]*PQ[(j+x)%p][j] for j in range(p))%ell
  assert actual==expected,(x,y,actual,expected)
  coeff_count+=1
# Integral coordinates for X=D_a, Y=D_(a*zeta).
X=D((a,0));Y=D((a*zeta[0]%p,a*zeta[1]%p))
omega=ps[(2*z*a*zeta[1])%p]
assert omega!=1 and pow(omega,p,ell)==1
q=omega*omega%ell
assert mm(X,Y)==[[(q*x)%ell for x in row] for row in mm(Y,X)]
cols=[];e=[1]*p
for j in range(p):
 cols.append(e)
 e=[sum(Y[r][s]*e[s] for s in range(p))%ell for r in range(p)]
assert e==cols[0]
E=[list(row) for row in zip(*cols)]
assert rank(E)==p
assert mm(R,E)==[[E[r][(-j)%p] for j in range(p)] for r in range(p)]
Qrec=[[0]*p for _ in range(p)]
for j in range(p):
 Qrec[j][j]=(pow(omega,2*j%p,ell)+pow(omega,-2*j%p,ell))%ell
 Qrec[(j+1)%p][j]=(1+pow(omega,(2*j+1)%p,ell))%ell
 Qrec[(j-1)%p][j]=(1+pow(omega,(-2*j+1)%p,ell))%ell
assert mm(Q,E)==mm(E,Qrec)
assert all((1+pow(omega,j,ell))%ell for j in range(p))
odd_images=[[(Qrec[j][k]-Qrec[(-j)%p][k])%ell for k in range(p)] for j in range(1,(p+1)//2)]
odd_kernel=(p-1)//2-rank(odd_images)
assert odd_kernel<=1
result={'p':p,'z':z,'a':a,'coefficient_prime':ell,'psi_root':psi,'cubic_parameter':list(zeta),
        'torus_product_checks':[[1,2],[3,5],[7,-7]],'H_order':d,'projector_rank':2,
        'projector_parity':'odd','PQ_coefficients_checked':coeff_count,
        'odd_left_kernel_dimension_in_this_check':odd_kernel,
        'scope':'One exact normalization check; general contradiction proved using the integral rank-two projector and a second-order recurrence.'}
Path('/tmp/r177_weil_odd_kernel_certificate.json').write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
print(json.dumps(result,sort_keys=True))
