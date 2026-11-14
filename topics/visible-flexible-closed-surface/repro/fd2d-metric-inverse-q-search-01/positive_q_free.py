"""Finite single-cell inverse-Q design, analytic optimizer derivatives.
This is a numerical design screen, not an interval or nonlinear certificate.
"""
import json,math,time
from pathlib import Path
import numpy as np
from scipy.special import softmax,roots_legendre,comb
from scipy.optimize import minimize
import positive_q as old

class FreeInverse:
 def __init__(self,right=.65,degree=24,grid=128,outer_w=.1):
  old.b=right;old.h=right-old.a;old.k1=-7/right
  self.m=old.PositiveInverse(degree,grid)
  self.a,self.b,self.h=old.a,right,right-old.a
  self.w0=old.w0;self.k0=old.k0;self.k1=-7/right
  self.target=math.log(outer_w/self.w0);self.outer_w=outer_w
  self.d=degree;self.grid=grid;self.nz=len(self.m.middle)
  self.r,self.rg=self.m.r,self.m.rg
  self.eye0=np.zeros(self.nz);self.eye0[0]=1
  self.cache=None
 def calculate(self,x):
  if self.cache is not None and np.array_equal(x,self.cache[0]):return self.cache[1]
  m=self.m;d=self.d;kap=np.exp(x[0]);q=self.nz
  alpha=softmax(np.r_[x[1:],0.]);z=np.zeros(d+1);dz=np.zeros((d+1,q))
  d0=1-self.h*(10/self.a+self.k0)/2
  c1=1+(1+self.h*(10/self.b+self.k1)/2)/d
  z[0]=1;z[1]=1+d0/d;z[-1]=kap;z[-2]=kap*c1
  dz[-1,0]=kap;dz[-2,0]=kap*c1
  target=(self.a**2+self.b**2*kap)/(12*self.h**2)
  rem=target-z@m.mom;dr=self.b**2*kap/(12*self.h**2)-dz[:,0]@m.mom
  z[m.middle]=rem*alpha/m.mom[m.middle]
  dz[m.middle,0]=dr*alpha/m.mom[m.middle]
  da=np.diag(alpha)[:,:-1]-alpha[:,None]*alpha[None,:-1]
  dz[m.middle,1:]=rem/m.mom[m.middle,None]*da
  kg=m.Kg@z;fg=m.Fg@z;dkg=m.Kg@dz;dfg=m.Fg@dz
  gt=-fg/(self.rg**2*kg)
  dgt=-(dfg-fg[:,None]*dkg/kg[:,None])/(self.rg**2*kg)[:,None]
  inc=gt.reshape(self.grid,8)@m.gw
  dinc=np.einsum('iaj,a->ij',dgt.reshape(self.grid,8,q),m.gw)
  logs=math.log(self.w0)+np.r_[0,np.cumsum(inc)]
  dlogs=np.vstack([np.zeros(q),np.cumsum(dinc,axis=0)])
  w=np.exp(np.clip(logs,-300,50));E=1+w*w
  kt=m.K@z;f=m.F@z;dk=m.K@dz;df=m.F@dz
  g=-f/(self.r**2*kt)
  dg=-(df-f[:,None]*dk/kt[:,None])/(self.r**2*kt)[:,None]
  bg=w*g/(self.h*E**1.5)
  dbg=(w/(self.h*E**1.5))[:,None]*dg+bg[:,None]*(1-3*w*w/E)[:,None]*dlogs
  scale=12*self.h**2/(self.b**6*kap)
  def affine(A):
   y=scale*(A@z);dy=scale*(A@dz)-y[:,None]*self.eye0
   return y,dy
  H,dH=affine(self.r[:,None]**4*m.Q)
  J,dJ=affine(self.r[:,None]**4*m.Qt/self.h)
  Hp,dHp=affine(4*self.r[:,None]**3*m.Q+self.r[:,None]**4*m.Qt/self.h)
  Hpp,dHpp=affine((self.r**2/self.h**2*m.t*(1-m.t))[:,None]*m.F)
  gamma=(self.a/self.b)**6/kap
  Gamma=J/w-4*H*w/self.r
  dGamma=(dJ-J[:,None]*dlogs)/w[:,None]-4*w[:,None]/self.r[:,None]*(dH+H[:,None]*dlogs)
  dl=-Hpp/np.sqrt(E);ddl=-dHpp/np.sqrt(E)[:,None]-dl[:,None]*(w*w/E)[:,None]*dlogs
  dn=-np.sqrt(E)*J/self.r;ddn=-np.sqrt(E)[:,None]*dJ/self.r[:,None]+dn[:,None]*(w*w/E)[:,None]*dlogs
  dm=2*H/self.r**2-2*Hp/self.r;ddm=2*dH/self.r[:,None]**2-2*dHp/self.r[:,None]
  # Exact max(abs(dl)+abs(dm),abs(dn)+abs(dm)) represented by linear signed rows.
  signed=np.concatenate([sl*dl+sm*dm for sl in [-1,1] for sm in [-1,1]]+[sn*dn+sm*dm for sn in [-1,1] for sm in [-1,1]])
  dsigned=np.vstack([sl*ddl+sm*ddm for sl in [-1,1] for sm in [-1,1]]+[sn*ddn+sm*ddm for sn in [-1,1] for sm in [-1,1]])
  o=dict(z=z,dz=dz,kap=kap,gamma=gamma,w=w,logs=logs,bg=bg,dbg=dbg,Gamma=Gamma,dGamma=dGamma,
    signed=signed,dsigned=dsigned,H=H,Hp=Hp,Hpp=Hpp,J=J,logratio=logs[-1]-logs[0],dlogratio=dlogs[-1],
    height=float(np.trapezoid(w,self.r)),meridian=float(np.trapezoid(np.sqrt(E),self.r)))
  self.cache=(x.copy(),o);return o
 def summary(self,o):
  return dict(right=self.b,left=self.a,degree=self.d,grid=self.grid,kap=float(o['kap']),gamma=float(o['gamma']),
   w_end=float(o['w'][-1]),w_max=float(max(o['w'])),w_min=float(min(o['w'])),background=float(max(abs(o['bg']))),
   Gamma=float(max(abs(o['Gamma']))),II_row=float(max(o['signed'])),Hpp=float(max(abs(o['Hpp']))),
   height=o['height'],meridian=o['meridian'])

def solve(right,outer_w=.1,degree=24,mode='background',seed=None,iterations=250):
 m=FreeInverse(right,degree,128,outer_w);n=m.nz
 if seed is None:x=np.r_[math.log((m.a/m.b)**6/.047074026251901865),np.zeros(n-1)]
 else:x=np.array(seed)
 o=m.calculate(x);start=m.summary(o);x=np.r_[x,max(abs(o['bg']))/7+1]
 def measures(x):
  o=m.calculate(x[:-1]);vals=[o['bg']/7,-o['bg']/7];jacs=[o['dbg']/7,-o['dbg']/7]
  if mode!='background':
   h=.00378586
   vals += [h*o['Gamma']/.5,-h*o['Gamma']/.5,h*o['signed']/1.0]
   jacs += [h*o['dGamma']/.5,-h*o['dGamma']/.5,h*o['dsigned']/1.0]
  return np.concatenate(vals),np.vstack(jacs)
 def fun(x):return x[-1]+1e-7*np.dot(x[:-1],x[:-1])
 def jac(x):return np.r_[2e-7*x[:-1],1]
 def eq(x):return m.calculate(x[:-1])['logratio']-m.target
 def eqj(x):return np.r_[m.calculate(x[:-1])['dlogratio'],0]
 def con(x):return x[-1]-measures(x)[0]
 def conj(x):return np.column_stack([-measures(x)[1],np.ones(len(measures(x)[0]))])
 began=time.monotonic()
 res=minimize(fun,x,jac=jac,method='SLSQP',bounds=[(-12,14)]+[(-18,18)]*(n-1)+[(0,1e7)],
   constraints=[{'type':'eq','fun':eq,'jac':eqj},{'type':'ineq','fun':con,'jac':conj}],
   options=dict(maxiter=iterations,ftol=1e-9,disp=False))
 o=m.calculate(res.x[:-1]);report=dict(scope='finite single-cell numerical design; no full tail or interval certificate',
  mode=mode,target_outer_w=outer_w,success=bool(res.success),status=int(res.status),message=res.message,
  iterations=res.nit,calls=res.nfev,seconds=time.monotonic()-began,initial=start,result=m.summary(o),
  endpoint_log_error=float(eq(res.x)),constraint_minimum=float(min(con(res.x))),params=res.x[:-1].tolist(),
  coefficients=o['z'].tolist(),epigraph=float(res.x[-1]))
 return report

if __name__=='__main__':
 reports=[]
 for b in [.55,.6,.65]:
  for mode in ['background','combined']:
   seed=None
   if mode=='combined':seed=reports[-1]['params']
   r=solve(b,mode=mode,seed=seed,iterations=300);reports.append(r)
   Path('positive-q-free-03.json').write_text(json.dumps(dict(reports=reports),indent=2)+'\n')
   print(json.dumps({k:v for k,v in r.items()if k not in ['params','coefficients','initial']}),flush=True)
