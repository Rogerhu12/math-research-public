"""Small scalar inverse-profile experiment, not a nonlinear tail solve."""
from explore_inverse import a,b,h,w0,k0,k1,trajectory,inlet
import numpy as np
import math,gzip,json,time
from scipy.special import comb,roots_legendre,softmax
from scipy.optimize import least_squares,nnls
from pathlib import Path

def bernstein_matrix(d,x):
 x=np.atleast_1d(x)
 return np.stack([comb(d,i)*x**i*(1-x)**(d-i)for i in range(d+1)],axis=1)

def multiply(c,d):
 n,m=len(c)-1,len(d)-1;o=np.zeros(n+m+1)
 for i,x in enumerate(c):
  for j,y in enumerate(d):o[i+j]+=x*y*comb(n,i)*comb(m,j)/comb(n+m,i+j)
 return o

class PositiveInverse:
 def __init__(self,degree=18,grid=256):
  self.d=degree;self.grid=grid;d=degree
  self.t=np.linspace(0,1,grid+1);x,w=roots_legendre(8)
  self.tg=(np.arange(grid)[:,None]+(x+1)[None,:]/2)/grid
  self.gw=w/(2*grid)
  self.mom=np.array([(i+1)*(d-i+1)/((d+1)*(d+2)*(d+3))for i in range(d+1)])
  self.middle=np.arange(2,d-1);self.end=np.array([0,1,d-1,d])
  qm=np.zeros((d+3,d+1))
  for j in range(d+1):qm[j+1,j]=(j+1)*(d-j+1)/((d+1)*(d+2))
  self.qtm=qm
  self.Qm=np.vstack([np.zeros(d+1),np.cumsum(qm,axis=0)/(d+3)])
  self.Qm[:,0]-=a*a/(12*h*h)
  fm=[]
  for j in range(d+1):
   q=qm[:,j];qq=(d+2)*np.diff(q)
   f=multiply([a*a,a*b,b*b],qq)+8*h*multiply([a,b],q)+12*h*h*self.Qm[:,j]
   degreeF=d+3
   fm.append(np.array([f[i]*degreeF*(degreeF-1)/(i*(degreeF-i))for i in range(1,degreeF)]))
  self.fm=np.stack(fm,axis=1)
  self.K=bernstein_matrix(d,self.t);self.F=bernstein_matrix(d+1,self.t)@self.fm
  self.Q=bernstein_matrix(d+3,self.t)@self.Qm;self.Qt=bernstein_matrix(d+2,self.t)@qm
  self.Kg=bernstein_matrix(d,self.tg.ravel());self.Fg=bernstein_matrix(d+1,self.tg.ravel())@self.fm
  self.r=a+h*self.t;self.rg=a+h*self.tg.ravel()
  self.target=math.log(.1/w0)
 def coefficients(self,kap,logits):
  d=self.d;z=np.zeros(d+1)
  d0=1-h*(10/a+k0)/2;d1=-kap*(1+h*(10/b+k1)/2)
  z[0]=1;z[1]=1+d0/d;z[d]=kap;z[d-1]=kap-d1/d
  target=(a*a+b*b*kap)/(12*h*h)
  remainder=target-np.dot(z,self.mom)
  if remainder<=0 or min(z[self.end])<=0:raise ValueError('Positive defining coefficients unavailable')
  alpha=softmax(np.r_[logits,0.])
  z[self.middle]=remainder*alpha/self.mom[self.middle]
  return z
 def evaluate(self,kap,logits):
  z=self.coefficients(kap,logits);kg=self.Kg@z;fg=self.Fg@z
  gt=-fg/(self.rg*self.rg*kg)
  increments=gt.reshape(self.grid,8)@self.gw
  logs=math.log(w0)+np.r_[0,np.cumsum(increments)]
  w=np.exp(np.clip(logs,-700,100));E=1+w*w
  f=self.F@z;kt=self.K@z;q=self.Q@z;qt=self.Qt@z
  logder=-f/(self.r*self.r*kt)
  background=w*logder/(h*E**1.5)
  scale=12*h*h/(b**6*kap)
  H=scale*self.r**4*q;Hp=scale*(4*self.r**3*q+self.r**4*qt/h)
  Hpp=scale*self.r*self.r/(h*h)*self.t*(1-self.t)*f
  J=scale*self.r**4*qt/h
  dl=-Hpp/np.sqrt(E);dn=-np.sqrt(E)*J/self.r;dm=2*H/self.r**2-2*Hp/self.r
  chart=J/w-4*H*w/self.r
  row=np.maximum(abs(dl)+abs(dm),abs(dn)+abs(dm))
  return dict(z=z,kap=kap,gamma=(a/b)**6/kap,log_ratio=logs[-1]-logs[0],
   background=background,chart=chart,row=row,Hpp=Hpp,H=H,Hp=Hp,w=w,
   min_k=float(min(kt)),meridian=float(np.trapz(np.sqrt(E),self.r)),height=float(np.trapz(w,self.r)))
 def seed(self,gamma):
  kap=(a/b)**6/gamma;self.gamma=gamma
  data=[]
  with gzip.open(trajectory,'rt')as f:
   for line in f:
    row=json.loads(line)
    if row['cell']==0 and a<row['r']<b:
     t=(row['r']-a)/h;J=row['Hr']-4*row['H']/row['r'];data.append((t,h*J/row['r']**4/(t*(1-t))))
  t,v=np.array(data).T
  scale=-12*h*h*inlet['H']/a**6;v=v/scale
  zero=self.coefficients(kap,np.zeros(len(self.middle)-1));end=zero.copy();end[self.middle]=0
  mat=bernstein_matrix(self.d,t);raw,_=nnls(mat[:,self.middle],v-mat@end)
  alpha=np.maximum(raw*self.mom[self.middle],1e-12);alpha/=sum(alpha)
  logits=np.log(alpha[:-1]/alpha[-1]);return kap,logits
 def summary(self,o):
  return dict(kappa=o['kap'],gamma=o['gamma'],w_end=float(o['w'][-1]),w_max=float(max(o['w'])),w_min=float(min(o['w'])),
   background=float(max(abs(o['background']))),Gamma=float(max(abs(o['chart']))),II_row=float(max(o['row'])),
   Hpp=float(max(abs(o['Hpp']))),height=o['height'],meridian=o['meridian'],minimum_k=o['min_k'])

if __name__=='__main__':
 began=time.monotonic();m=PositiveInverse();kap,x=m.seed(.047074026251901865)
 print(json.dumps(dict(stage='initial',**m.summary(m.evaluate(kap,x)))),flush=True)
 evals=0
 def fun(z):
  global evals
  o=m.evaluate(kap,z);evals+=1
  result=np.r_[20*(o['log_ratio']-m.target),
   np.maximum(abs(o['background'])/6.8-1,0)*.4,
   np.maximum(.00037*abs(o['chart'])/.5-1,0)*.02,
   np.maximum(.00037*o['row']/.8-1,0)*.02,
   z*.0001]
  return result
 result=least_squares(fun,x,max_nfev=400,xtol=3e-10,ftol=3e-10,gtol=3e-10)
 o=m.evaluate(kap,result.x)
 out=dict(scope='Finite scalar inverse-profile trial; no interval certificate, no complete new tail',
  degree=m.d,grid=m.grid,iterations=result.nfev,calls=evals,success=bool(result.success),message=result.message,
  params=result.x.tolist(),coefficient_bernstein=o['z'].tolist(),result=m.summary(o),seconds=time.monotonic()-began)
 Path('positive-q-screen-01.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items()if k not in ['params','coefficient_bernstein']}),flush=True)
