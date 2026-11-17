"""Finite nonlinear collocation Schur response to all terminal BC values.
This is a numerical derivative at the represented solution, not a theorem
about the infinite-dimensional exact-core boundary map.
"""
import numpy as np
from scipy.integrate._bvp import prepare_sys
from scipy.sparse.linalg import splu


def terminal_rank(obj,sol):
    n,N,k=obj.n,len(sol.x),len(sol.p)
    col,jac=prepare_sys(n,N,k,obj.fun,obj.bc,obj.fun_jac,obj.bc_jac,sol.x,np.diff(sol.x))
    res,mid,f,fmid=col(sol.y,sol.p)
    bc=obj.bc(sol.y[:,0],sol.y[:,-1],sol.p)
    J=jac(sol.y,sol.p,mid,f,fmid,bc).tocsc()
    rhs=np.zeros((J.shape[0],k));rhs[-k:]=np.eye(k)
    delta=splu(J).solve(rhs);response=delta[-k:]
    schur=np.linalg.inv(response)
    sv=np.linalg.svd(schur,compute_uv=False)
    norms=np.linalg.norm(schur,axis=0)
    sc=np.linalg.svd(schur/np.maximum(norms,1e-300)[None,:],compute_uv=False)
    return dict(scope=__doc__,nodes=N,modes=k,unknowns=J.shape[0],terminal_schur=schur.tolist(),parameter_response=response.tolist(),singular_values=sv.tolist(),condition=float(sv[0]/sv[-1]),column_normalized_singular_values=sc.tolist(),column_normalized_condition=float(sc[0]/sc[-1]),solve_residual=float(np.max(abs(J@delta-rhs))))
