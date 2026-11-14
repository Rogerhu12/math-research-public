import numpy as np
from numpy.polynomial import polynomial as P
from scipy.linalg import solve
from scipy.special import roots_legendre
import math, gzip, json
from pathlib import Path

topic=Path('/workspace/scratch/fd2dbfd2c83e/math-research/topics/visible-flexible-closed-surface')
trajectory=topic/'notes/2026-11-12-fd2d-layered64-wc01-recovery02-m2-n512-trajectory.jsonl.gz'
with gzip.open(trajectory,'rt')as f:
 for line in f:
  row=json.loads(line)
  if row['cell']==0 and row['segment']==0 and row['x']==0:inlet=row;break
a,b=inlet['r'],.5;h=b-a;w0=inlet['w'];k0=inlet['wr']/w0;k1=-7/b
M=np.array([[1,1,1,1],[4,5,6,7],[12,20,30,42],[24,60,120,210]],float)
B0=np.zeros(9);B0[4:]=256*np.array([1,-4,6,-4,1]);B=[B0]
for j in range(1,5):B.append(P.polymul(B[-1],[-1,2]))
xg,wg=roots_legendre(256);tg=(xg+1)/2;wg=wg/2

def coefficients(gamma,alpha):
 left=[-gamma,h*4*(-gamma)/a,0,h**3*12*k0*(-gamma)/a**2]
 right=[1,h*4/b,0,h**3*12*k1/b**2]
 c=np.zeros(8);c[:4]=[left[j]/math.factorial(j) for j in range(4)]
 rhs=[right[j]-P.polyval(1,P.polyder(c,m=j))for j in range(4)];c[4:]=solve(M,rhs)
 for value,base in zip(alpha,B):c=P.polyadd(c,value*base)
 return c

def quotients(c):
 N=P.polysub(P.polymul([a,h],P.polyder(c)/h),4*c)
 A=P.polyder(c,m=2)
 return np.cumsum(N[1:-1]),np.cumsum(A[1:-1])

def logratio(gamma,alpha):
 c=coefficients(gamma,alpha);R,A=quotients(c)
 r=P.polyval(tg,R);minimum=min(r)
 if minimum<=0:return None,minimum
 k=-(a+h*tg)*P.polyval(tg,A)/(h*h*r)
 return h*np.dot(wg,k),minimum

if __name__=='__main__':
 target=math.log(.1/w0);best=[]
 for gamma in [.047074026251901865,.01,.001]:
  good=[]
  for al0 in np.linspace(-.8,.4,49):
   for al1 in np.linspace(-.8,.4,49):
    v,m=logratio(gamma,[al0,al1])
    if v is not None:good.append((abs(v-target),v,m,al0,al1))
  good.sort();best.append(dict(gamma=gamma,feasible=len(good),best=good[:3],maximum=max(v[1]for v in good)))
 print(json.dumps(dict(a=a,b=b,w0=w0,k0=k0,target=target,results=best),indent=2))
