"""Domain-aware collocation Newton backtracking for scipy.integrate.solve_bvp.
Astra curve_transition, AI-assisted 2026-11-08. This is an independent small
implementation of the usual affine-invariant Newton merit/backtracking method.
Invalid Frenet/core trials are rejected; no square root or geometric data are
clipped. The SciPy mesh/refinement and final residual tests are unchanged.
Uses the installed private solve_newton signature, checked when installed.
"""
import inspect
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

def install():
    import scipy.integrate._bvp as module
    wanted=['n','m','h','col_fun','bc','jac','y','p','B','bvp_tol','bc_tol']
    if list(inspect.signature(module.solve_newton).parameters)!=wanted:raise RuntimeError('Installed SciPy BVP Newton signature differs; refusing patch')
    module.solve_newton=solve_newton
    return STATS
