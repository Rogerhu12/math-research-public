import json,math,time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from positive_q_free04 import FreeInverse

def elevate(c,d):
 c=np.array(c)
 while len(c)<=d:
  n=len(c);a=np.arange(n+1)/n
  c=a*np.r_[0,c]+(1-a)*np.r_[c,0]
 return c

def one(row,mode='hardbg',degree=32,outer=.1,seed=None):
 m=FreeInverse(row['right'],degree,160,outer);n=m.nz
 c=elevate(row['coef'],degree);alpha=c[m.m.middle]*m.m.mom[m.m.middle]
 x=np.r_[math.log(c[-1]),np.log(np.maximum(alpha[:-1],1e-20)/max(alpha[-1],1e-20))]
 x=np.clip(x,-35,35)
 if seed is not None:x=np.array(seed)
 o=m.calculate(x);initial=m.summary(o)
 def measure(z):
  o=m.calculate(z);return np.r_[o['Gamma']/1000,-o['Gamma']/1000,o['signed']/1000],np.vstack([o['dGamma']/1000,-o['dGamma']/1000,o['dsigned']/1000])
 vals,_=measure(x);x=np.r_[x,max(vals)]
 def obj(x):return x[-1]+1e-9*np.dot(x[:-1],x[:-1])
 def jac(x):return np.r_[2e-9*x[:-1],1]
 def eq(x):return m.calculate(x[:-1])['logratio']-m.target
 def eqj(x):return np.r_[m.calculate(x[:-1])['dlogratio'],0]
 def con(x):
  o=m.calculate(x[:-1]);v,_=measure(x[:-1]);return np.r_[1-o['bg']/6.95,1+o['bg']/6.95,-o['logs'],x[-1]-v]
 def conj(x):
  o=m.calculate(x[:-1]);v,j=measure(x[:-1]);a=np.vstack([-o['dbg']/6.95,o['dbg']/6.95,-o['dlogs']]);return np.vstack([np.column_stack([a,np.zeros(len(a))]),np.column_stack([-j,np.ones(len(j))])])
 began=time.monotonic();r=minimize(obj,x,jac=jac,method='SLSQP',bounds=[(-12,14)]+[(-40,40)]*(n-1)+[(0,1e6)],constraints=[dict(type='eq',fun=eq,jac=eqj),dict(type='ineq',fun=con,jac=conj)],options=dict(maxiter=700,ftol=3e-10))
 o=m.calculate(r.x[:-1]);out=dict(scope='single-cell inverse profile numerical screen; no complete-tail claim',initial=initial,mode=mode,target_outer=outer,success=bool(r.success),status=int(r.status),message=r.message,iterations=r.nit,seconds=time.monotonic()-began,result=m.summary(o),endpoint_log_error=float(eq(r.x)),constraint_minimum=float(min(con(r.x))),epigraph=float(r.x[-1]),params=r.x[:-1].tolist(),coefficients=o['z'].tolist())
 return out
if __name__=='__main__':
 old=json.loads(Path('positive-q-widen-02.json').read_text())['rows'];rows=[]
 for b in [.6,.65,.7,.75]:
  r=one(next(x for x in old if x['right']==b));rows.append(r);Path('positive-q-hardbg-04.json').write_text(json.dumps(dict(reports=rows),indent=2)+'\n');print(json.dumps({k:v for k,v in r.items()if k not in ['params','coefficients','initial']}),flush=True)
