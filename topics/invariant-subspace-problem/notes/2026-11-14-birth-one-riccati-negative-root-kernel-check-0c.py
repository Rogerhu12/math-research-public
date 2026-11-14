"""Standalone exact checks; theorem is the finite Rolle/Gram proof in the manuscript."""
from fractions import Fraction as F
from math import comb

def moments(q,L,z):
 Z=[];m=[];v=[];vp=[]
 for j in range(q+L+1):
  vv=[(r,F(comb(q,r)*comb(L,j-r))*z**r) for r in range(max(0,j-L),min(q,j)+1)]
  zz=sum(t for r,t in vv);mm=sum(r*t for r,t in vv)/zz
  Z.append(zz);m.append(mm);v.append(sum((r-mm)**2*t for r,t in vv)/zz);vp.append(sum((r-mm)**3*t for r,t in vv)/zz)
 return Z,m,v,vp

def det(A):
 A=[list(r)for r in A];d=F(1)
 for i in range(len(A)):
  if not A[i][i]:
   k=next((k for k in range(i+1,len(A))if A[k][i]),None)
   if k is None:return F(0)
   A[i],A[k]=A[k],A[i];d=-d
  p=A[i][i];d*=p
  for k in range(i+1,len(A)):
   u=A[k][i]/p
   for l in range(i+1,len(A)):A[k][l]-=u*A[i][l]
 return d

count=0
for q,L in [(1,2),(2,3),(4,6),(7,9)]:
 N=q+L
 for z in [F(1,4),F(1),F(4,3),F(16)]:
  Z,m,v,vp=moments(q,L,z)
  for j in range(1,N):
   assert (z-1)*(v[j]+m[j]**2)-(z*(q+j)+L-j)*m[j]+z*q*j==0
   rho=Z[j-1]/Z[j]
   if z!=1:
    aa=q+j+F(N)/(z-1)
    assert vp[j]==(aa-2*m[j])*v[j]-z*(N*m[j]-q*j)/(z-1)**2
    assert rho*(m[j-1]-m[j])==(z*(N-j+1)*rho**2+(q*z+L-(z+1)*j+1)*rho-j)/(z-1)
   r0=max(0,j-L);degree=min(q,j);d=degree-r0;xi=m[j]-r0
   left=xi*(v[j]+vp[j])-2*v[j]**2
   right=(d-xi)*(v[j]-vp[j])-2*v[j]**2
   bound=xi*(1-xi/d)-v[j]
   assert min(left,right,bound)>=0
   assert (left==right==bound==0)if d==1 else min(left,right,bound)>0
   # Z_j(z(1+t))/Z_j(z), then remove all forced (1+t) factors.
   ee=[sum(F(comb(q,r)*comb(L,j-r)*comb(r,k))*z**r for r in range(max(k,r0),degree+1))/Z[j]for k in range(degree+1)]
   for _ in range(r0):
    out=[ee[0]]
    for k in range(1,len(ee)-1):out.append(ee[k]-out[-1])
    assert ee[-1]==out[-1];ee=out
   assert len(ee)==d+1
   S=[F(d)]
   for k in range(1,2*min(3,d)+1):
    sk=sum((-1)**(i-1)*ee[i]*S[k-i]for i in range(1,min(k-1,d)+1))
    if k<=d:sk+=(-1)**(k-1)*k*ee[k]
    S.append(sk)
   assert S[1]==xi and S[2]==xi-v[j]
   for sz in range(1,min(3,d)+1):
    assert det([[S[a+b]for b in range(sz)]for a in range(sz)])>0
    assert det([[S[a+b]-S[a+b+1]for b in range(sz)]for a in range(sz)])>0
   count+=1

# Exact actual triangle-coefficient obstruction, normalizing K_0=1.
q,L,z,w=2,3,F(16),F(1,100);N=q+L
Z,m,v,_=moments(q,L,z);S0=[];Se=[]
for n in range(N):
 delta=m[n+1]-m[n];A=1/Z[n]+w/Z[n+1];B=w/(Z[n+1]*v[n+1]+w*Z[n]*v[n])
 S0.append(B*(1-delta));Se.append(A-B*delta*(1-delta))
assert S0[1:4]==[F(167,6520672),F(16909,183598176),F(167,569620)]
assert Se[2:5]==[F(8068091,2868721500),F(2613601,2278480000),F(1,25600)]
assert S0[2]**2/(S0[1]*S0[3])==F(8296663252194670655,7344457079993490888)>1
assert Se[3]**2/(Se[2]*Se[4])==F(39191957837185067043,3272286042388925500)>1
print('ALL_PASS',count,'actual Riccati/ratio identities, forced-root moments, strict differential bounds, Hankel/localizing minors, both exact triangle-coefficient obstructions')
