"""Single inverse buffer coupled to the actually stored unchanged deep line.
All sampled constants and inverse-profile quadrature are numerical diagnostics.
"""
import json,math,time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
import positive_q as old
from positive_q_free04 import FreeInverse

cases=[dict(N=1,a=.3808860058501116,w=.003991159062404631,wr=-.0001047846233821564,CII=10165925.4827,CG=4936322.040405483/.047074026251901865),
 dict(N=2,a=.3435132337600405,w=.0021611134196327392,wr=-.002765767408468409,CII=62578564.7149,CG=368981.73353/.00021639189590773564)]

def one(c,seed,outer=.1,right=.65):
 old.a=c['a'];old.w0=c['w'];old.k0=c['wr']/c['w'];m=FreeInverse(right,32,160,outer);n=m.nz
 denom=1e5;iiweight=5/3
 def measures(x):
  o=m.calculate(x);v=o['gamma'];dg=np.zeros(n);dg[0]=-v
  vals=np.r_[o['Gamma'],-o['Gamma'],iiweight*o['signed'],c['CG']*v,iiweight*c['CII']*v]/denom
  jac=np.vstack([o['dGamma'],-o['dGamma'],iiweight*o['dsigned'],c['CG']*dg,iiweight*c['CII']*dg])/denom
  return vals,jac
 vals,_=measures(np.array(seed));x=np.r_[seed,max(vals)]
 def f(x):return x[-1]+1e-10*np.dot(x[:-1],x[:-1])
 def j(x):return np.r_[2e-10*x[:-1],1]
 def eq(x):return m.calculate(x[:-1])['logratio']-m.target
 def eqj(x):return np.r_[m.calculate(x[:-1])['dlogratio'],0]
 def con(x):
  o=m.calculate(x[:-1]);v,_=measures(x[:-1]);return np.r_[1-o['bg']/6.9,1+o['bg']/6.9,-o['logs'],x[-1]-v]
 def conj(x):
  o=m.calculate(x[:-1]);v,j=measures(x[:-1]);a=np.vstack([-o['dbg']/6.9,o['dbg']/6.9,-o['dlogs']]);return np.vstack([np.column_stack([a,np.zeros(len(a))]),np.column_stack([-j,np.ones(len(j))])])
 begin=time.monotonic();res=minimize(f,x,jac=j,method='SLSQP',bounds=[(-12,18)]+[(-40,40)]*(n-1)+[(0,1e8)],constraints=[dict(type='eq',fun=eq,jac=eqj),dict(type='ineq',fun=con,jac=conj)],options=dict(maxiter=1100,ftol=1e-9))
 o=m.calculate(res.x[:-1]);summary=m.summary(o);summary.update(deep_Gamma_proxy=c['CG']*o['gamma'],deep_II_proxy=c['CII']*o['gamma'])
 return dict(scope='finite inverse-design screen with sampled unchanged-deep scaling; no interval/full-tail certificate',case=c,right=right,outer_w=outer,result=summary,success=bool(res.success),status=int(res.status),message=res.message,nit=res.nit,nfev=res.nfev,seconds=time.monotonic()-begin,eq=float(eq(res.x)),constraint_minimum=float(min(con(res.x))),objective=float(res.x[-1]),params=res.x[:-1].tolist(),coefficients=o['z'].tolist())
if __name__=='__main__':
 base=next(x for x in json.loads(Path('positive-q-hardbg-04.json').read_text())['reports'] if x['result']['right']==.65)
 deeper=json.loads(Path('positive-q-inner-ports-07.json').read_text())['reports'];reports=[]
 for c in cases:
  seed=base['params'] if c['N']==1 else next(x for x in deeper if x['replace_outer_cells']==c['N'] and x['target_outer']==.1)['params']
  r=one(c,seed);reports.append(r);Path('positive-q-coupled-08.json').write_text(json.dumps(dict(reports=reports),indent=2)+'\n');print(json.dumps({k:v for k,v in r.items()if k not in ['params','coefficients']}),flush=True)
