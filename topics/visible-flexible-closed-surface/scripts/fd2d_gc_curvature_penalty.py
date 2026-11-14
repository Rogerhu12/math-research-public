"""Optional finite curvature merit for the independent-l,m,n raw branch.

The original Gauss/Codazzi residual is never changed. Returned extra rows select
a branch with smaller sampled FORMAL shape eigenvalues; they do not certify the
actual reconstructed map or add a final acceptance condition.

At an active repeated eigenvalue the spectral maximum is nondifferentiable. A
specified valid symmetric subgradient is returned and flagged, not called an
ordinary derivative. In particular radius=0 does not imply inactivity unless
the common eigenvalue lies in [-cap,cap].
"""
from __future__ import annotations
import numpy as np
from scipy import sparse


def shape_eigenvalues(fields):
    fields=np.asarray(fields,float)
    if fields.shape[-1]!=3 or not np.all(np.isfinite(fields)):
        raise ValueError('Expected finite fields[...,n,m,l]')
    n,m,l=fields[...,0],fields[...,1],fields[...,2]
    radius=np.hypot(n-l,2*m)
    trace=n+l
    return .5*(trace+radius),.5*(trace-radius),radius


def _active(fields,cap,weight):
    upper,lower,radius=shape_eigenvalues(fields)
    up=np.argwhere(upper>cap)
    down=np.argwhere(lower < -cap)
    labels=np.concatenate((up,down),axis=0)
    branch=np.r_[np.ones(len(up),dtype=np.int8),-np.ones(len(down),dtype=np.int8)]
    if len(labels):
        i,j=labels[:,0],labels[:,1]
        n,m,l=fields[i,j,0],fields[i,j,1],fields[i,j,2]
        d=radius[i,j]
        difference=np.divide(n-l,d,out=np.zeros_like(d),where=d!=0)
        offdiag=np.divide(2*m,d,out=np.zeros_like(d),where=d!=0)
        gradients=weight*np.column_stack((.5*(branch+difference),offdiag,
                                          .5*(branch-difference)))
        residual=weight*(.5*(branch*(n+l)+d)-cap)
        repeated=d==0
    else:
        gradients=np.empty((0,3));residual=np.empty(0);repeated=np.empty(0,dtype=bool)
    return residual,gradients,labels,branch,repeated,upper,lower


def penalty_values_on_labels(fields,labels,branch,*,cap,weight=1.):
    """Fixed labels for a directional check or a caller-owned active set."""
    fields=np.asarray(fields,float);labels=np.asarray(labels,int);branch=np.asarray(branch,int)
    if labels.shape!=(len(branch),2) or np.any(np.abs(branch)!=1):
        raise ValueError('Each label is [angle,node] and each branch is +/-1')
    if not len(branch):
        return np.empty(0)
    up,down,_=shape_eigenvalues(fields)
    i,j=labels[:,0],labels[:,1]
    values=np.where(branch>0,up[i,j],-down[i,j])
    return float(weight)*np.maximum(values-float(cap),0.)


def curvature_penalty(problem,vector,*,cap,weight=1.,data=None,
                      jacobian=True,field_T=None):
    """Return {residual,jacobian,labels,branch,info}, without altering raw F.

    data may be RawLiftedDAE.evaluate(...)[-1]. Its fields order is n,m,l and
    lift.parameters has shape (work,N,3,K+1). Analytic state and tail columns are
    exact derivatives of these finite formula evaluations. The sole T column
    uses the same centered lifting difference/epsilon as the raw provider.

    To reuse an already computed T column, pass field_T with shape (work,N,3).
    Otherwise the provider's lifting is evaluated twice, then physical T is
    restored. Central c columns are zero when raw node coefficients are treated
    as independent; a caller imposing linear boundary identities composes that
    linear map with this Jacobian (or uses directions tangent to those rows).
    """
    cap,weight=float(cap),float(weight)
    if not np.isfinite(cap) or cap<=0 or not np.isfinite(weight) or weight<0:
        raise ValueError('Use a positive finite cap and a nonnegative finite weight')
    vector=np.asarray(vector,float)
    if vector.shape!=(problem.size,):
        raise ValueError('Wrong raw vector dimension')
    if data is None:
        _,data=problem.evaluate(vector)
    fields=np.asarray(data['fields'],float)
    if fields.shape!=(problem.work,problem.N,3):
        raise ValueError('Unexpected raw field axes')
    residual,gradient,labels,branch,repeated,upper,lower=_active(fields,cap,weight)
    unweighted_count=len(residual)
    if weight==0:
        residual=np.empty(0);gradient=np.empty((0,3));labels=np.empty((0,2),dtype=int)
        branch=np.empty(0,dtype=np.int8);repeated=np.empty(0,dtype=bool)
    rows=len(residual)
    info=dict(cap=cap,weight=weight,active_rows=rows,
        upper_active_rows=int(np.count_nonzero(branch>0)),
        lower_active_rows=int(np.count_nonzero(branch<0)),
        active_rows_before_zero_weight=unweighted_count,
        active_repeated_eigenvalue_rows=int(np.count_nonzero(repeated)),
        sampled_formal_curvature_maximum=float(np.max(np.maximum(np.abs(upper),np.abs(lower)))),
        sampled_exact_cap_equalities=int(np.count_nonzero((upper==cap)|(lower == -cap))),
        residual_l2=float(np.linalg.norm(residual)),
        original_equations_changed=False,actual_geometry_certified=False,
        derivative_kind='Ordinary derivative at simple active eigenvalues; valid symmetric spectral subgradient at flagged active repeated eigenvalues.',
        repeated_eigenvalue_subgradient='branch*weight*(1/2,0,1/2) in (n,m,l)',
        central_parameter_columns='zero before composing caller linear boundary projection',
        scope='Optional sampled formal-curvature merit only; original F and actual geometry remain separate.')
    result=dict(residual=residual,jacobian=None,labels=labels,branch=branch,
                repeated_eigenvalue=repeated,info=info)
    if not jacobian:
        return result
    if not rows:
        result['jacobian']=sparse.csc_matrix((0,problem.size))
        info['T_column']='not needed because no active row'
        return result
    i,j=labels[:,0],labels[:,1]
    local=np.concatenate((gradient[:,0,None]*problem.E[i],
                          gradient[:,1,None]*problem.O[i],
                          gradient[:,2,None]*problem.E[i]),axis=1)
    state_columns=j[:,None]*problem.q+np.arange(problem.q)[None,:]
    row_numbers=np.repeat(np.arange(rows),problem.q)
    rr=[row_numbers];cc=[state_columns.ravel()];vv=[local.ravel()]
    offset=problem.N*problem.q
    parameter_derivatives=np.asarray(data['lift']['parameters'],float)
    expected=(problem.work,problem.N,3,problem.K+1)
    if parameter_derivatives.shape!=expected:
        raise ValueError('The exact lifting tail Jacobian is not the recorded one')
    tail=np.einsum('ri,rip->rp',gradient,parameter_derivatives[i,j])
    rr.append(np.repeat(np.arange(rows),problem.K+1))
    cc.append(np.broadcast_to(offset+problem.K+np.arange(problem.K+1),
                              (rows,problem.K+1)).ravel())
    vv.append(tail.ravel())
    if field_T is None:
        _,p=problem.unpack(vector)
        T=float(p[-1]);tail_parameters=p[problem.K:-1]
        eps=min(1e-6*(1+abs(T)),.2*T,.2*(problem.profile.model.Tmax-T))
        if eps<=0:
            raise ValueError('The T difference needs an interior physical coast')
        try:
            plus=problem.lifting(T+eps,tail_parameters)['values']
            minus=problem.lifting(T-eps,tail_parameters)['values']
            field_T=(plus-minus)/(2*eps)
        finally:
            problem.profile.set_parameter(T)
        info['T_column']='centered actual lifting difference, same epsilon as raw provider'
        info['T_difference_epsilon']=float(eps)
    else:
        info['T_column']='caller-supplied actual field T derivative'
    field_T=np.asarray(field_T,float)
    if field_T.shape!=fields.shape or not np.all(np.isfinite(field_T)):
        raise ValueError('Wrong or nonfinite actual field T derivative')
    tvalues=np.sum(gradient*field_T[i,j],axis=1)
    rr.append(np.arange(rows));cc.append(np.full(rows,problem.size-1));vv.append(tvalues)
    matrix=sparse.coo_matrix((np.concatenate(vv),(np.concatenate(rr),np.concatenate(cc))),
                            shape=(rows,problem.size)).tocsc()
    matrix.eliminate_zeros()
    result['jacobian']=matrix
    info['jacobian_nonzeros']=int(matrix.nnz)
    return result
