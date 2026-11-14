"""Exact calibration of actual adjacent-ratio kernels and their derivative generator.
All arithmetic uses Fraction. The general theorem is proved in the companion text.
No imported repository code, precomputed tables, root approximation, or floating point.
"""
from fractions import Fraction as F
from math import comb
from itertools import combinations

def coeff(q,L,j):
 return [F(comb(q,r)*comb(L,j-r))if 0<=r<=q and 0<=j-r<=L else F(0)for r in range(q+1)]
def taylor(c,z,K):
 return [sum((c[r]*comb(r,k)*z**r for r in range(k,len(c))),F(0))for k in range(K+1)]
def determinant(a):
 if not a:return F(1)
 return sum(((-1)**j*a[0][j]*determinant([r[:j]+r[j+1:]for r in a[1:]])for j in range(len(a))),F(0))
def psd(a):
 for k in range(1,len(a)+1):
  for I in combinations(range(len(a)),k):assert determinant([[a[i][j]for j in I]for i in I])>=0

def moments(q,L,j,z,K=6):
 # rho_j = Z_j/Z_(j+1), Taylor coefficients in epsilon where z=z0(1+epsilon).
 den=taylor(coeff(q,L,j+1),z,K+1);num=taylor(coeff(q,L,j),z,K)
 aa=[v/den[0]for v in den];bb=[v/den[0]for v in num]
 jj=j+1;Nt=q+L
 for k in range(K):
  assert (1-z)*(k+2)*(k+1)*aa[k+2]+(L-jj+1+(q+jj-1)*z+k*(1-2*z))*(k+1)*aa[k+1]-z*(q-k)*(jj-k)*aa[k]==0
 for k in range(K+1):assert bb[k]==((jj-k)*aa[k]-(z-1)*(k+1)*aa[k+1]/z)/(Nt-jj+1)
 cc=[]
 for k in range(K+1):cc.append(bb[k]-sum((aa[i]*cc[k-i]for i in range(1,k+1)),F(0)))
 return [(-1)**k*cc[k]/cc[0]for k in range(K+1)],num,den

cases=0
for q,L in ((1,1),(2,3),(4,4),(5,7)):
 for j in range(q+L):
  for z in (F(1,4),F(1),F(4)):
   S,_,_=moments(q,L,j,z)
   for typ in range(4):
    A=[[S[a+b]if typ==0 else S[a+b+1]if typ==1 else S[a+b]-S[a+b+1]if typ==2 else S[a+b+1]-S[a+b+2]for b in range(3)]for a in range(3)]
    psd(A)
   cases+=1
print('EXACT_HIGHER_MOMENT_LOCALIZERS_PASS',cases)
for q,L,n,z in ((4,4,3,F(4)),(5,7,4,F(3)),(2,6,3,F(1,4))):
 m=q+L-1-n;M=m+1;N=n+1
 def mv(j):
  tt=taylor(coeff(q,L,j),z,2);mm=tt[1]/tt[0];return mm,(2*tt[2]+tt[1])/tt[0]-mm*mm
 mn,vn=mv(n);mp,vp=mv(n+1)
 p=(q-mn)/M;r=mp/N;B=r*(1-r);A=p*(1-p);theta=vp/(N*B)
 u=A*(1-theta)/(B*theta);eta=(r-p)**2*theta/A
 delta=M*u-N;V=1+u+u*eta;J=V+delta;K=V-delta
 S,_,_=moments(q,L,n,z)
 assert S[1]==mp-mn
 assert S[2]-S[1]**2==J*B*theta/2
 assert S[1]-S[2]==K*B*theta/2
print('ACTUAL_PHASE_J_K_IDENTITIES_PASS',3)
print('ALL_PASS')
