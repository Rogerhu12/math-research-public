"""Finite curvature and high-angular-Gauss guidance with explicit full p jets."""
from __future__ import annotations
import numpy as np
from scipy import sparse
from fd2d_gc_curvature_penalty import _active


def curvature_merit(problem,vector,*,cap=7.2,weight=1.,data=None,jacobian=True):
    if cap<=0 or weight<0 or not np.isfinite(cap+weight):
        raise ValueError('Use a positive cap and a nonnegative finite weight')
    if data is None:_,data=problem.evaluate(vector)
    r,g,labels,branch,repeated,up,down=_active(data['fields'],cap,weight)
    if weight==0:r=np.empty(0);g=np.empty((0,3));labels=np.empty((0,2),int)
    rows=len(r);info=dict(cap=cap,weight=weight,active_rows=rows,
        repeated_eigenvalue_rows=int(np.count_nonzero(repeated)),
        residual_l2=float(np.linalg.norm(r)),sampled_formal_curvature_maximum=float(max(np.max(abs(up)),np.max(abs(down)))),
        original_equations_changed=False,actual_geometry_certified=False)
    result=dict(residual=r,jacobian=None,info=info,labels=labels,branch=branch)
    if not jacobian:return result
    if not rows:
        result['jacobian']=sparse.csc_matrix((0,problem.size));return result
    i,j=labels[:,0],labels[:,1]
    local=np.concatenate((g[:,0,None]*problem.E[i],g[:,1,None]*problem.O[i],g[:,2,None]*problem.E[i]),axis=1)
    param=np.einsum('ri,rip->rp',g,data['fields_parameters'][i,j])
    rr=np.r_[np.repeat(np.arange(rows),problem.q),np.repeat(np.arange(rows),problem.parameter_count)]
    cc=np.r_[(j[:,None]*problem.q+np.arange(problem.q)).ravel(),
             np.broadcast_to(problem.N*problem.q+np.arange(problem.parameter_count),(rows,problem.parameter_count)).ravel()]
    vv=np.r_[local.ravel(),param.ravel()]
    result['jacobian']=sparse.coo_matrix((vv,(rr,cc)),shape=(rows,problem.size)).tocsc()
    result['jacobian'].eliminate_zeros();return result


def high_gauss_merit(problem,vector,*,weight=1.,data=None,jacobian=True):
    if not np.isfinite(weight) or weight<0:raise ValueError('Invalid high Gauss weight')
    if data is None:_,data=problem.evaluate(vector)
    def high(v):return v-problem.E@(problem.PE@v)
    full=data['full_gauss'];omitted=high(full[:,:-1]);scale=weight*np.sqrt(2./problem.work)
    residual=scale*omitted.T.ravel()
    info=dict(weight=weight,normalization='sqrt(2/angular_work)',rows=len(residual),
        sampled_full_gauss_maximum=float(np.max(abs(full))),
        sampled_omitted_gauss_maximum=float(np.max(abs(omitted))),
        residual_l2=float(np.linalg.norm(residual)),continuous_certificate=False,
        scope='Angular orthogonal complement on the actual finite working grid')
    result=dict(residual=residual,jacobian=None,info=info)
    if not jacobian:return result
    fields=data['fields'];n,m,l=(fields[:,:,i] for i in range(3))
    allp=data['fields_parameters'];kp=np.zeros((problem.N,problem.parameter_count))
    kp[:,problem.profile_parameter_slice]=data['profile_jet']['K_parameters']
    rr=[];cc=[];vv=[];offset=problem.N*problem.q
    def block(row,cols,values):
        a=scale*np.asarray(values,float);ii,jj=np.nonzero(a)
        rr.append(row+ii);cc.append(cols[jj]);vv.append(a[ii,jj])
    for j in range(problem.N-1):
        state=np.concatenate((l[:,j,None]*problem.E,-2*m[:,j,None]*problem.O,n[:,j,None]*problem.E),axis=1)
        gp=allp[:,j]
        param=l[:,j,None]*gp[:,0,:]+n[:,j,None]*gp[:,2,:]-2*m[:,j,None]*gp[:,1,:]-kp[j]
        block(j*problem.work,j*problem.q+np.arange(problem.q),high(state))
        block(j*problem.work,offset+np.arange(problem.parameter_count),high(param))
    result['jacobian']=sparse.coo_matrix((np.concatenate(vv),(np.concatenate(rr),np.concatenate(cc))),
        shape=(len(residual),problem.size)).tocsc()
    result['jacobian'].eliminate_zeros();info['jacobian_nonzeros']=int(result['jacobian'].nnz)
    return result
