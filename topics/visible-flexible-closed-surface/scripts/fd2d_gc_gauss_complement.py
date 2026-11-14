"""The omitted angular Gauss equations as an explicit finite search residual.

This supplements the original projected Gauss rows with their orthogonal
complement on the *same* recorded angular grid. It changes no equation of the
continuous problem and supplies no continuous residual certificate. Original
Gauss/Codazzi residuals remain separately recorded by the branch finder.
"""
from __future__ import annotations
import numpy as np
from scipy import sparse


def gauss_complement(problem,vector,*,weight=1.,data=None,jacobian=True,
                     fields_T=None):
    """Return finite omitted-Gauss rows and their analytic state/tail columns.

Rows are ordered by radial node then angle, excluding the exact cut node.
The T derivative must be supplied by the recorded analytic profile provider.
No numerically vanishing boundary distance is used to pick a difference step.
Central parameter columns are zero before composing the explicit boundary
identity; bounded_schur_direction performs that composition for its caller.
    """
    weight=float(weight)
    if not np.isfinite(weight) or weight<0:
        raise ValueError('Use a finite nonnegative angular Gauss weight')
    if data is None:
        _,data=problem.evaluate(vector)
    full=np.asarray(data['full_gauss'],float)
    fields=np.asarray(data['fields'],float)
    if full.shape!=(problem.work,problem.N) or fields.shape!=(problem.work,problem.N,3):
        raise ValueError('Unexpected native angular/radial field shape')
    def high(value):
        return value-problem.E@(problem.PE@value)
    omitted=high(full[:,:-1])
    scale=weight*np.sqrt(2./problem.work)
    residual=scale*omitted.T.ravel()
    info=dict(weight=weight,normalization='weight*sqrt(2/angular_work)',
        rows=len(residual),sampled_full_gauss_maximum=float(np.max(np.abs(full))),
        sampled_omitted_gauss_maximum=float(np.max(np.abs(omitted))),
        residual_l2=float(np.linalg.norm(residual)),
        original_equations_changed=False,continuous_certificate=False,
        scope='Orthogonal complement of the existing finite even Fourier Gauss projection on its recorded angular grid')
    result=dict(residual=residual,jacobian=None,info=info)
    if not jacobian:
        return result
    if fields_T is None:
        fields_T=data.get('fields_T')
    if fields_T is None:
        raise ValueError('An explicitly bound analytic fields_T is required')
    fields_T=np.asarray(fields_T,float)
    if fields_T.shape!=fields.shape or not np.all(np.isfinite(fields_T)):
        raise ValueError('Wrong or nonfinite analytic T derivative')
    lift_parameters=np.asarray(data['lift']['parameters'],float)
    expected=(problem.work,problem.N,3,problem.K+1)
    if lift_parameters.shape!=expected:
        raise ValueError('Unexpected exact tail parameter derivative axes')
    n,m,l=fields[...,0],fields[...,1],fields[...,2]
    rr,cc,vv=[],[],[]
    pcol=problem.N*problem.q
    def block(row,columns,values):
        values=scale*np.asarray(values,float)
        ii,jj=np.nonzero(values)
        rr.append(row+ii);cc.append(np.asarray(columns)[jj]);vv.append(values[ii,jj])
    for j in range(problem.N-1):
        row=j*problem.work
        state=np.concatenate((l[:,j,None]*problem.E,
                              -2*m[:,j,None]*problem.O,
                              n[:,j,None]*problem.E),axis=1)
        block(row,j*problem.q+np.arange(problem.q),high(state))
        lp=lift_parameters[:,j]
        tail=l[:,j,None]*lp[:,0]+n[:,j,None]*lp[:,2]-2*m[:,j,None]*lp[:,1]
        block(row,pcol+problem.K+np.arange(problem.K+1),high(tail))
        # K_T is constant in angle and is annihilated by this complement.
        tangent=l[:,j]*fields_T[:,j,0]+n[:,j]*fields_T[:,j,2]-2*m[:,j]*fields_T[:,j,1]
        block(row,np.array([problem.size-1]),high(tangent[:,None]))
    result['jacobian']=sparse.coo_matrix((np.concatenate(vv),
        (np.concatenate(rr),np.concatenate(cc))),shape=(len(residual),problem.size)).tocsc()
    result['jacobian'].eliminate_zeros()
    info['jacobian_nonzeros']=int(result['jacobian'].nnz)
    info['T_column']='analytic provider fields_T; angular-constant K_T annihilated'
    return result
