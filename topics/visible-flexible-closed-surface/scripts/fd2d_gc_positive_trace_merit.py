"""Actual curvature and nonredundant high-Gauss rows for R153 fields."""
import numpy as np
from scipy import sparse
from fd2d_gc_curvature_penalty import _active
from fd2d_gc_codazzi_complement import _high
from fd2d_gc_d2_complements import d2_high_rows
from fd2d_gc_raw_bump_positive_trace import actual_state_columns


def curvature_merit(problem,vector,*,cap=7.2,weight=1.,data=None,jacobian=True):
    if data is None:_,data=problem.evaluate(vector)
    r,g,labels,branch,repeated,up,down=_active(data['fields'],cap,weight)
    if weight==0:r=np.empty(0);g=np.empty((0,3));labels=np.empty((0,2),int)
    rows=len(r);info=dict(cap=cap,weight=weight,active_rows=rows,repeated_eigenvalue_rows=int(np.count_nonzero(repeated)),
        residual_l2=float(np.linalg.norm(r)),sampled_formal_curvature_maximum=float(max(np.max(abs(up)),np.max(abs(down)))),
        actual_field='R153 coast plus R155 terminal n/l positive trace',complete_chain_derivative=True,actual_geometry_certified=False)
    result=dict(residual=r,jacobian=None,info=info,labels=labels,branch=branch)
    if not jacobian:return result
    if not rows:result['jacobian']=sparse.csc_matrix((0,problem.size));return result
    i,j=labels[:,0],labels[:,1];D=data['gauss_l_delta']
    T=data['positive_trace_delta'];trace_g=g[:,0]+g[:,2]
    gn=g[:,0]+g[:,2]*D['gn'][i,j]+trace_g*T['gn'][i,j]
    gm=g[:,1]+g[:,2]*D['gm'][i,j]+trace_g*T['gm'][i,j]
    gl=g[:,2]*(1+D['gl'][i,j])+trace_g*T['gl'][i,j]
    local=np.concatenate((gn[:,None]*problem.E[i],gm[:,None]*problem.O[i],gl[:,None]*problem.E[i]),axis=1)
    param=np.einsum('ri,rip->rp',g,data['fields_parameters'][i,j])
    rr=np.r_[np.repeat(np.arange(rows),problem.q),np.repeat(np.arange(rows),problem.parameter_count)]
    cc=np.r_[(j[:,None]*problem.q+np.arange(problem.q)).ravel(),
        np.broadcast_to(problem.N*problem.q+np.arange(problem.parameter_count),(rows,problem.parameter_count)).ravel()]
    vv=np.r_[local.ravel(),param.ravel()]
    result['jacobian']=sparse.coo_matrix((vv,(rr,cc)),shape=(rows,problem.size)).tocsc()
    result['jacobian'].eliminate_zeros();return result


def high_gauss_merit(problem,vector,*,weight=1.,data=None,jacobian=True):
    if data is None:_,data=problem.evaluate(vector)
    rows=d2_high_rows(problem);w=problem.window();selected=np.flatnonzero((w[:-1]!=1.)&(problem.x[:-1]<problem.trace_ramp_stop))
    full=data['full_gauss'];omitted=_high(full[:,selected],problem.E,problem.PE)
    residual=weight*rows.project(omitted,'even').T.ravel()
    info=dict(weight=weight,rows=len(residual),retained_radial_node_indices=selected.tolist(),
        exact_zero_plateau_nodes_removed=np.flatnonzero((w[:-1]==1.)|(problem.x[:-1]>=problem.trace_ramp_stop)).tolist(),
        sampled_full_gauss_maximum=float(np.max(abs(full))),sampled_omitted_gauss_maximum=float(np.max(abs(omitted),initial=0.)),
        residual_l2=float(np.linalg.norm(residual)),actual_field='Complete R153 plus R155 actual Gauss, not scaled old G',
        normalization='D2 isometric Fourier rows, same complete nonzero high-Gauss objective',continuous_certificate=False)
    result=dict(residual=residual,jacobian=None,info=info)
    if not jacobian:return result
    n,m,l=(data['fields'][:,:,i] for i in range(3))
    allp=data['fields_parameters'];kp=np.zeros((problem.N,problem.parameter_count));kp[:,problem.profile_parameter_slice]=data['profile_jet']['K_parameters']
    rr=[];cc=[];vv=[];offset=problem.N*problem.q
    def block(row,columns,values):
        small=weight*rows.project(_high(values,problem.E,problem.PE),'even');ii,jj=np.nonzero(small)
        if len(ii):rr.append(row+ii);cc.append(np.asarray(columns)[jj]);vv.append(small[ii,jj])
    for out,j in enumerate(selected):
        dn,dm,dl=actual_state_columns(problem,data,j)
        state=l[:,j,None]*dn+data['fields'][:,j,0,None]*dl-2*m[:,j,None]*dm
        gp=allp[:,j];par=l[:,j,None]*gp[:,0]+n[:,j,None]*gp[:,2]-2*m[:,j,None]*gp[:,1]-kp[j]
        block(out*rows.e,j*problem.q+np.arange(problem.q),state)
        block(out*rows.e,offset+np.arange(problem.parameter_count),par)
    shape=(len(residual),problem.size)
    result['jacobian']=(sparse.coo_matrix((np.concatenate(vv),(np.concatenate(rr),np.concatenate(cc))),shape=shape).tocsc()
        if vv else sparse.csc_matrix(shape))
    result['jacobian'].eliminate_zeros();info['jacobian_nonzeros']=int(result['jacobian'].nnz);return result
