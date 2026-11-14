"""Actual R153/R155 Gauss and curvature rows inside selected saved P1 cells.

This adds finite equations at the two existing Gauss points of specifically
located bad rim cells. The field, chart, physical metric family and unknowns
are unchanged. Full chain derivatives map each sample to its two endpoints.
"""
from __future__ import annotations
import copy
import numpy as np
from scipy import sparse
from fd2d_gc_codazzi_complement import _high
from fd2d_gc_d2_complements import d2_high_rows
from fd2d_gc_positive_gauss_l import positive_gauss_l_delta,gauss_delta_direction
from fd2d_gc_positive_trace_branch import positive_trace_delta,trace_delta_direction
from fd2d_gc_raw_bump_positive_trace import actual_state_columns
from fd2d_gc_positive_trace_merit import curvature_merit


def point_view(problem,cells=(63,71,118),order=2):
    cells=np.asarray(cells,int)
    if len(cells)==0 or np.any(cells<0) or np.any(cells>=problem.N-1) or len(np.unique(cells))!=len(cells):
        raise ValueError('Choose distinct actual cell indices')
    key=(tuple(cells),int(order),np.asarray(problem.x,float).tobytes())
    cache=getattr(problem,'_interior_constraint_point_cache',None)
    if cache is not None and cache[0]==key:return cache[1]
    if order!=2:raise ValueError('This finite scheme uses the existing two Gauss points')
    t,w=np.polynomial.legendre.leggauss(order);t=(t+1)/2;w=w/2
    cell=np.repeat(cells,order);fraction=np.tile(t,len(cells));weights=np.tile(w,len(cells))
    x=problem.x[cell]+np.diff(problem.x)[cell]*fraction
    view=copy.copy(problem);view.x=x;view.N=len(x);view.h=np.diff(x)
    view.size=view.N*view.q+view.parameter_count
    view.coords={k:np.asarray(v,float) for k,v in view.chart.coordinates(x).items()}
    view._operator_cache={};view._cell_gauss_view_cache=None;view._chunked_gauss_codazzi_views=None
    out=dict(view=view,cells=cell,fractions=fraction,weights=weights,selected_cells=cells)
    problem._interior_constraint_point_cache=(key,out);return out


def actual_point_packet(problem,vector,*,cells=(63,71,118),jacobian=True):
    layout=point_view(problem,cells);view=layout['view'];ids=layout['cells'];t=layout['fractions']
    y,p=problem.unpack(np.asarray(vector,float));yq=(1-t[:,None])*y[ids]+t[:,None]*y[ids+1]
    key=np.asarray(p[view.profile_parameter_slice],float).tobytes()
    if key not in view._operator_cache:view._operator_cache.clear()
    ops=view.operators(p[view.profile_parameter_slice]);jet=ops['jet']
    lift=view.lifting(p[view.profile_parameter_slice],p[view.tail_parameter_slice])
    affine=np.stack((view.E@yq[:,:view.e].T,view.O@yq[:,view.e:view.d].T,view.E@yq[:,view.d:].T),axis=-1)+lift['values']
    angular=np.stack((view.Ex@yq[:,:view.e].T,view.Ox@yq[:,view.e:view.d].T,view.Ex@yq[:,view.d:].T),axis=-1)+lift['xi']
    D=positive_gauss_l_delta(affine,angular,jet['K'][None,:],view.window()[None,:],minimum_active_n=problem.minimum_active_n)
    background=affine.copy();background[:,:,2]=D['actual_l']
    bangular=angular.copy();bangular[:,:,2]=D['actual_l_xi']
    T=positive_trace_delta(background,bangular,jet['K'][None,:],view.trace_window()[None,:],exact_tail_mask=view.trace_mask()[None,:])
    actual=T['actual'];G=actual[:,:,0]*actual[:,:,2]-actual[:,:,1]**2-jet['K'][None,:]
    data=dict(fields=actual,full_gauss=G,profile_jet=jet,gauss_l_delta=D,positive_trace_delta=T)
    if jacobian:
        fp=np.zeros((view.work,view.N,3,view.parameter_count))
        for section,vname,xname,physical in ((view.tail_parameter_slice,'parameters','xi_parameters',False),
                (view.profile_parameter_slice,'profile_parameters','profile_xi_parameters',True)):
            value=np.array(lift[vname],float,copy=True);angle=np.array(lift[xname],float,copy=True)
            kp=jet['K_parameters'][None,:,:] if physical else np.zeros((1,view.N,section.stop-section.start))
            dv,dx=gauss_delta_direction(D,value,angle,kp);value[:,:,2]+=dv;angle[:,:,2]+=dx
            ev,_=trace_delta_direction(T,value,angle,kp);value[:,:,0]+=ev;value[:,:,2]+=ev
            fp[:,:,:,section]=value
        data['fields_parameters']=fp
    return layout,np.r_[yq.ravel(),p],data


def map_point_matrix(problem,layout,matrix):
    """Exact global Jacobian of P1 point samples, before all Schur gauges."""
    view=layout['view'];A=matrix.tocoo(copy=False);limit=view.N*view.q
    state=A.col<limit;j=A.col[state]//view.q;k=A.col[state]%view.q
    cell=layout['cells'][j];t=layout['fractions'][j]
    rr=np.r_[A.row[state],A.row[state],A.row[~state]]
    cc=np.r_[cell*problem.q+k,(cell+1)*problem.q+k,problem.N*problem.q+A.col[~state]-limit]
    vv=np.r_[(1-t)*A.data[state],t*A.data[state],A.data[~state]]
    out=sparse.coo_matrix((vv,(rr,cc)),shape=(matrix.shape[0],problem.size)).tocsc();out.eliminate_zeros();return out


def interior_gauss_curvature(problem,vector,*,cells=(63,71,118),gauss_weight=1.,curvature_cap=7.2,curvature_weight=1.,jacobian=True):
    layout,qvector,data=actual_point_packet(problem,vector,cells=cells,jacobian=jacobian)
    view=layout['view'];weights=np.sqrt(layout['weights']);rows=d2_high_rows(view)
    G=data['full_gauss'];high=_high(G,view.E,view.PE)
    low_r=(gauss_weight*weights[None,:]*(view.PE@G)).T.ravel()
    high_r=(gauss_weight*weights[None,:]*rows.project(high,'even')).T.ravel()
    curv=curvature_merit(view,qvector,cap=curvature_cap,weight=curvature_weight,data=data,jacobian=jacobian)
    cw=weights[curv['labels'][:,1]];curv_r=cw*curv['residual']
    result=dict(retained_residual=low_r,high_residual=high_r,curvature_residual=curv_r,
        retained_jacobian=None,high_jacobian=None,curvature_jacobian=None)
    i,j=np.unravel_index(int(np.argmax(abs(G))),G.shape)
    info=dict(schema='fd2d-actual-selected-interior-Gauss-curvature-v1',selected_cells=layout['selected_cells'].tolist(),
        points=view.x.tolist(),sample_cell_indices=layout['cells'].tolist(),fractions=layout['fractions'].tolist(),
        quadrature_mean_weights=layout['weights'].tolist(),row_weight='sqrt(Gauss average weight) times specified guidance weight',
        physical_field_unchanged=True,physical_g_unchanged_by_extra_rows=True,unknown_mesh_unchanged=True,
        finite_Gauss_equations_changed=True,complete_actual_Gauss=True,full_parameter_chain_rule=True,
        full_Gauss_maximum=float(np.max(abs(G))),high_Gauss_maximum=float(np.max(abs(high))),
        retained_residual_l2=float(np.linalg.norm(low_r)),high_residual_l2=float(np.linalg.norm(high_r)),
        curvature_residual_l2=float(np.linalg.norm(curv_r)),curvature=curv['info'],
        maximum_location=dict(cell=int(layout['cells'][j]),s=float(view.x[j]),xi=float(view.chart.theta[i]),
            material_u=float(view.coords['u'][i,j]),G=float(G[i,j]),n_m_l=data['fields'][i,j].tolist(),K=float(data['profile_jet']['K'][j])),
        continuous_certificate=False)
    result['info']=info
    if not jacobian:return result
    lowparts=[[],[],[]];highparts=[[],[],[]];offset=view.N*view.q
    def add(parts,row,columns,block):
        ii,jj=np.nonzero(block)
        if len(ii):parts[0].append(row+ii);parts[1].append(np.asarray(columns)[jj]);parts[2].append(block[ii,jj])
    for j in range(view.N):
        n,m,l=data['fields'][:,j].T;dn,dm,dl=actual_state_columns(view,data,j)
        state=l[:,None]*dn+n[:,None]*dl-2*m[:,None]*dm
        fp=data['fields_parameters'][:,j]
        par=l[:,None]*fp[:,0]+n[:,None]*fp[:,2]-2*m[:,None]*fp[:,1]
        par[:,view.profile_parameter_slice]-=data['profile_jet']['K_parameters'][j]
        for col,values in ((j*view.q+np.arange(view.q),state),(offset+np.arange(view.parameter_count),par)):
            scale=gauss_weight*weights[j]
            add(lowparts,j*view.e,col,scale*(view.PE@values))
            add(highparts,j*rows.e,col,scale*rows.project(_high(values,view.E,view.PE),'even'))
    def matrix(parts,nrows):
        if not parts[2]:return sparse.csc_matrix((nrows,view.size))
        return sparse.coo_matrix((np.concatenate(parts[2]),(np.concatenate(parts[0]),np.concatenate(parts[1]))),shape=(nrows,view.size)).tocsc()
    result['retained_jacobian']=map_point_matrix(problem,layout,matrix(lowparts,len(low_r)))
    result['high_jacobian']=map_point_matrix(problem,layout,matrix(highparts,len(high_r)))
    result['curvature_jacobian']=map_point_matrix(problem,layout,sparse.diags(cw)@curv['jacobian'])
    return result
