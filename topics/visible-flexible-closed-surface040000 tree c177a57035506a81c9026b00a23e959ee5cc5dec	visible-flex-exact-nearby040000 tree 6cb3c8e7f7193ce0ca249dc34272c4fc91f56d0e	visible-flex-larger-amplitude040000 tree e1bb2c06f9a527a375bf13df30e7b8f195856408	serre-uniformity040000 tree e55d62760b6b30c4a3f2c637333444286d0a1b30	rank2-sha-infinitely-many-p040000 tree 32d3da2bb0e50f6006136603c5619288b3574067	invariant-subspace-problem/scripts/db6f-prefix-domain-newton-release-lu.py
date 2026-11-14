"""Lifetime-only derivative of the frozen domain-aware collocation Newton.

Original file SHA256:
6cb269210e609e1f49c20004be0ce3f9f68e43e47ab57eaf16bb9e56fa3be654

The solve_newton source has exactly one added statement: factor=None after
the refresh budget check and before evaluating the replacement Jacobian/LU.
This module never installs itself.  The separately bound selector must share
the original STATS object and declare the changed runtime function identity.
No existing run or mathematical success is asserted by this definition.
"""
import numpy as np
from scipy.sparse.linalg import splu
STATS={'calls':0,'rejected_domain_trials':0,'rejected_merit_trials':0,'accepted_steps':0,'no_step':0,'minimum_alpha':1.}

def solve_newton(n,m,h,col_fun,bc,jac,y,p,B,bvp_tol,bc_tol):
    STATS['calls']+=1
    def evaluate(Y,P):
        cr,ym,ff,fm=col_fun(Y,P);br=bc(Y[:,0],Y[:,-1],P)
        return (np.r_[cr.ravel(order='F'),br],cr,ym,ff,fm,br)
    data=evaluate(y,p);refresh=True;factors=0;threshold=h*(bvp_tol/30.)
    for iteration in range(24):
        residual,cr,ym,ff,fm,br=data
        if np.all(abs(cr)<threshold*(1+abs(fm))) and np.all(abs(br)<bc_tol):break
        if refresh:
            if factors>=8:break
            factor=None
            try:factor=splu(jac(y,p,ym,ff,fm,br))
            except RuntimeError:return y,p,True
            factors+=1;step=factor.solve(residual);cost=float(step@step)
        direction_y=step[:n*m].reshape((n,m),order='F');direction_p=step[n*m:];accepted=None
        for back in range(21):
            alpha=2.**(-back);trial_y=y-alpha*direction_y;trial_p=p-alpha*direction_p
            if B is not None:trial_y[:,0]=B@trial_y[:,0]
            try:
                trial=evaluate(trial_y,trial_p);newstep=factor.solve(trial[0]);newcost=float(newstep@newstep)
            except FloatingPointError:
                STATS['rejected_domain_trials']+=1;continue
            if np.isfinite(newcost) and newcost<(1-.4*alpha)*cost:
                accepted=(trial_y,trial_p,trial,newstep,newcost,alpha);break
            STATS['rejected_merit_trials']+=1
        if accepted is None:STATS['no_step']+=1;break
        y,p,data,step,cost,alpha=accepted;STATS['accepted_steps']+=1;STATS['minimum_alpha']=min(STATS['minimum_alpha'],alpha);refresh=alpha!=1.
    return y,p,False
