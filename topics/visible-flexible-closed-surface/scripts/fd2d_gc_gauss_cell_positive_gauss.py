"""R153 nonlinear Codazzi correction on the exact-endpoint affine background.

The existing endpoint consumer is used only for the original affine field.
The complete nonlinear Delta l and Delta l_xi, with their state and all
physical-profile/tail parameter derivatives, are then quadrature integrated.
"""
from __future__ import annotations
import numpy as np
from scipy import sparse
from fd2d_gc_gauss_cell_codazzi_endpoint_d2 import gauss_cell_codazzi_endpoint_d2
from fd2d_gc_gauss_cell_codazzi import _view
from fd2d_gc_codazzi_complement import _high,_bound_model
from fd2d_gc_d2_complements import d2_high_rows
from fd2d_gc_positive_gauss_l import positive_gauss_l_delta,gauss_delta_direction,gauss_delta_state_columns


def gauss_cell_positive_gauss(problem,vector,*,order=2,high_weight=1.,jacobian=True):
    result=gauss_cell_codazzi_endpoint_d2(problem,vector,order=order,high_weight=high_weight,jacobian=jacobian)
    rule=_view(problem,order);qv,tau,weights=rule['view'],rule['tau'],rule['weights'];cells=rule['cells'];order=rule['order']
    y,p=problem.unpack(vector)
    yq=((1-tau)[None,:,None]*y[:-1,None,:]+tau[None,:,None]*y[1:,None,:]).reshape(qv.N,qv.q)
    qvector=np.r_[yq.ravel(),p];ops=qv.operators(p[qv.profile_parameter_slice]);jet=ops['jet']
    lift=qv.lifting(p[qv.profile_parameter_slice],p[qv.tail_parameter_slice])
    fields=np.stack((qv.E@yq[:,:qv.e].T,qv.O@yq[:,qv.e:qv.d].T,qv.E@yq[:,qv.d:].T),axis=-1)+lift['values']
    angular=np.stack((qv.Ex@yq[:,:qv.e].T,qv.Ox@yq[:,qv.e:qv.d].T,qv.Ex@yq[:,qv.d:].T),axis=-1)+lift['xi']
    w=qv.window();D=positive_gauss_l_delta(fields,angular,jet['K'][None,:],w[None,:],minimum_active_n=problem.minimum_active_n)
    inv=ops['inv'];c=jet['c'];compression=d2_high_rows(problem)
    rhs=np.stack((c[None,:]*D['delta'],inv*D['delta_xi']),axis=-1)
    change=-np.einsum('wcqe,q->wce',rhs.reshape(qv.work,cells,order,2),weights)
    low=np.concatenate((qv.PE@change[:,:,0],qv.PO@change[:,:,1]),axis=0).T
    high=np.stack((_high(change[:,:,0],qv.E,qv.PE),_high(change[:,:,1],qv.O,qv.PO)),axis=-1)
    result['retained_cells']+=low;result['retained_residual']=result['retained_cells'].ravel()
    result['omitted_codazzi_cells']+=high;result['full_codazzi_cells']+=change
    omitted=result['omitted_codazzi_cells']
    result['high_residual']=high_weight*np.concatenate((compression.project(omitted[:,:,0],'even'),compression.project(omitted[:,:,1],'odd')),axis=0).T.ravel()
    result['point_gauss']=fields[:,:,0]*D['actual_l']-fields[:,:,1]**2-jet['K'][None,:]
    result['info'].update(schema='fd2d-positive-Gauss-l-exact-affine-endpoint-complete-nonlinear-Codazzi-v1',
        actual_field='R153 l=(1-w)*l_raw+w*(K+m^2)/n; only active window divided',
        full_nonlinear_delta_l_and_angular_delta_included=True,
        known_affine_endpoint_primitive_preserved=True,
        physical_g_changed=False,finite_field_representation_changed=True,
        sampled_active_n_minimum=D['sampled_minimum_active_n'],
        retained_cell_maximum=float(np.max(abs(result['retained_cells']),initial=0.)),
        sampled_full_average_codazzi_maximum=float(np.max(abs(result['full_codazzi_cells']),initial=0.)),
        sampled_omitted_average_codazzi_maximum=float(np.max(abs(omitted),initial=0.)),
        sampled_interior_Gauss_maximum=float(np.max(abs(result['point_gauss']),initial=0.)),
        finite_symmetry_and_compression={key:compression.diagnostics(omitted[:,:,i],parity)
            for i,(key,parity) in enumerate((('n','even'),('m','odd')))})
    if not jacobian:return result
    _,_,_,groups=_bound_model(qv,qvector,{'lift':lift},True)
    dp_groups=[]
    for group in groups:
        gi=group['indices'];profile=bool(gi[0]>=qv.profile_parameter_slice.start)
        kp=jet['K_parameters'][None,:,:] if profile else np.zeros((1,qv.N,len(gi)))
        dv,dx=gauss_delta_direction(D,group['values'],group['xi'],kp)
        pn=c[None,:,None]*dv+group['c'][None,:,:]*D['delta'][...,None]
        invp=-inv[...,None]*group['a'][None,:,:]/jet['a'][None,:,None]
        pm=inv[...,None]*dx+invp*D['delta_xi'][...,None]
        dp_groups.append((gi,pn,pm))
    low_parts=[[],[],[]];high_parts=[[],[],[]];offset=problem.N*problem.q
    def add(parts,row,columns,values):
        values=np.asarray(values,float);ii,jj=np.nonzero(values)
        if len(ii):parts[0].append(row+ii);parts[1].append(np.asarray(columns)[jj]);parts[2].append(values[ii,jj])
    def projections(pn,pm):
        small=np.concatenate((qv.PE@pn,qv.PO@pm),axis=0)
        high=np.concatenate((compression.project(_high(pn,qv.E,qv.PE),'even'),compression.project(_high(pm,qv.O,qv.PO),'odd')),axis=0)
        return small,high
    for cell in range(cells):
        left=np.zeros((problem.d,problem.q));right=left.copy()
        hleft=np.zeros((compression.cell_rows,problem.q));hright=hleft.copy()
        pars=np.zeros((problem.d,problem.parameter_count));hpars=np.zeros((compression.cell_rows,problem.parameter_count))
        for j,t,weight in zip(range(cell*order,(cell+1)*order),tau,weights):
            dv,dx=gauss_delta_state_columns(qv,D,j)
            small,high=projections(c[j]*dv,inv[:,j,None]*dx)
            left-=weight*(1-t)*small;right-=weight*t*small
            hleft-=weight*(1-t)*high;hright-=weight*t*high
            for gi,pn,pm in dp_groups:
                small,high=projections(pn[:,j],pm[:,j]);pars[:,gi]-=weight*small;hpars[:,gi]-=weight*high
        for node,low_block,high_block in ((cell,left,hleft),(cell+1,right,hright)):
            cols=node*problem.q+np.arange(problem.q)
            add(low_parts,cell*problem.d,cols,low_block)
            add(high_parts,cell*compression.cell_rows,cols,high_weight*high_block)
        add(low_parts,cell*problem.d,offset+np.arange(problem.parameter_count),pars)
        add(high_parts,cell*compression.cell_rows,offset+np.arange(problem.parameter_count),high_weight*hpars)
    def matrix(parts,shape):
        if not parts[2]:return sparse.csc_matrix(shape)
        out=sparse.coo_matrix((np.concatenate(parts[2]),(np.concatenate(parts[0]),np.concatenate(parts[1]))),shape=shape).tocsc()
        out.eliminate_zeros();return out
    result['retained_jacobian']+=matrix(low_parts,result['retained_jacobian'].shape)
    result['high_jacobian']+=matrix(high_parts,result['high_jacobian'].shape)
    result['retained_jacobian'].eliminate_zeros();result['high_jacobian'].eliminate_zeros()
    result['info']['retained_jacobian_nonzeros']=int(result['retained_jacobian'].nnz)
    result['info']['high_jacobian_nonzeros']=int(result['high_jacobian'].nnz)
    return result
