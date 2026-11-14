"""Exact checks of actual finite product-weight identities; no comparison claim."""
from fractions import Fraction as F
from math import comb,factorial

def inv3(A):
 B=[list(r)+[F(i==j) for j in range(3)] for i,r in enumerate(A)]
 for i in range(3):
  k=next(k for k in range(i,3) if B[k][i]);B[i],B[k]=B[k],B[i]
  d=B[i][i];B[i]=[x/d for x in B[i]]
  for k in range(3):
   if k!=i:
    d=B[k][i];B[k]=[x-d*y for x,y in zip(B[k],B[i])]
 return [r[3:]for r in B]
def Zmom(q,L,z):
 N=q+L;Z=[];mean=[];var=[]
 for k in range(N+1):
  a=[(r,F(comb(q,r)*comb(L,k-r))*z**r)for r in range(max(0,k-L),min(q,k)+1)]
  Z.append(sum(v for _,v in a));mean.append(sum(r*v for r,v in a)/Z[-1]);var.append(sum(r*r*v for r,v in a)/Z[-1]-mean[-1]**2)
 return Z,mean,var
count=0
for q,L in [(1,2),(2,3),(4,6),(7,9)]:
 N=q+L
 for z,w in [(F(4),F(2)),(F(1,4),F(1,3)),(F(1),F(5))]:
  Z,means,vs=Zmom(q,L,z);K=F(factorial(q)**2)*z**q
  zz=lambda j:Z[j]if 0<=j<=N else F(0)
  for j in range(N+1):
   assert (j+1)*zz(j+1)==(q*z+L-(z+1)*j)*zz(j)+z*(N-j+1)*zz(j-1)
   if z!=1:
    assert means[j]==z/(z-1)*(j-(N-j+1)*zz(j-1)/zz(j))
    U=j*(N-j)*zz(j)**2-(j+1)*(N-j+1)*zz(j-1)*zz(j+1)
    assert vs[j]==z/(z-1)**2*U/zz(j)**2
   assert vs[j]<=means[j]*(1-means[j]/q)
   assert vs[j]<=(j-means[j])*(1-(j-means[j])/L)
  for n in range(N):
   k=n+1;delta=means[k]-means[n];assert 0<delta<1
   A=K*(1/Z[n]+w/Z[k]);B=K*w/(Z[k]*vs[k]+w*Z[n]*vs[n])
   H=[[A+B*delta**2,B*delta],[B*delta,B]]
   M=[[F(0)for _ in range(3)]for _ in range(3)]
   for bit in [0,1]:
    for r in range(max(0,k-bit-L),min(q,k-bit)+1):
     s=k-bit-r;v=F(comb(q,r)*comb(L,s))*z**r*w**bit;ct=[r,s,bit]
     for i in range(3):
      for j in range(3):M[i][j]+=v*ct[i]*ct[j]
   Mi=inv3(M);U=[[0,1],[-1,-1],[1,0]]
   direct=[[K*w*sum(F(U[a][i])*Mi[a][b]*U[b][j]for a in range(3)for b in range(3))for j in range(2)]for i in range(2)]
   assert H==direct,(q,L,z,w,n)
   if n==0:assert H==[[K*(1+w/L),K*w/L],[K*w/L,K*(w/L+w/(q*z))]]
   if 2<=n<=N-3 and z!=1:
    us={j:j*(N-j)*zz(j)**2-(j+1)*(N-j+1)*zz(j-1)*zz(j+1)for j in range(n-1,n+3)}
    xs=(us[n-1]/(Z[n-1]*Z[n])-us[n]/(Z[n]*Z[n+1]))/n
    ys=(us[n+1]/(Z[n+1]*Z[n+2])-us[n]/(Z[n]*Z[n+1]))/(n+1)
    dm=means[n]-means[n-1];dp=means[n+2]-means[n+1]
    assert xs==(delta-dm)*(z-1)/z
    assert ys==(delta-dp)*(z-1)/z
   count+=1
print('ALL_PASS',count,'full 3x3 inverses, both physical endpoints, source Gram, linear recurrence, Newton-defect curvature, scaled Pearson, group negative-correlation bounds')
