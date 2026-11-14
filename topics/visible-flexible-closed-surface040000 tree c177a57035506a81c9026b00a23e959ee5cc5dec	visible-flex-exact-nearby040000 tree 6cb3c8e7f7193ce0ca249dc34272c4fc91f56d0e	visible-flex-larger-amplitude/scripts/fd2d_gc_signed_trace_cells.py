"""R182 signed disjoint trace: complete nonlinear endpoint and angular PDE/J.

The base R153+R152 contribution is evaluated on its explicit old field.
Only then is E added to both n and l. c(l-n) cancels exactly, leaving
Delta Cn=[E]/h-Q(adv E_xi), Delta Cm=-Q(inv E_xi).
"""
from __future__ import annotations
import numpy as np
from scipy import sparse
from fd2d_gc_gauss_cell_codazzi import _view
from fd2d_gc_positive_gauss_coast_hybrid import gauss_cell_positive_gauss_coast_hybrid
from fd2d_gc_codazzi_complement import _high,_bound_model
from fd2d_gc_d2_complements import d2_high_rows
from fd2d_gc_positive_trace_branch import positive_trace_delta,trace_delta_direction,trace_delta_state_columns


def _packet(view,y,p,jacobian):
    ops=view.operators(p[view.profile_parameter_slice]);jet=ops['jet']
    lift=view.lifting(p[view.profile_parameter_slice],p[view.tail_parameter_slice])
    f=np.stack((view.E@y[:,:view.e].T,view.O@y[:,view.e:view.d].T,view.E@y[:,view.d:].T),axis=-1)+lift['values']
    fx=np.stack((view.Ex@y[:,:view.e].T,view.Ox@y[:,view.e:view.d].T,view.Ex@y[:,view.d:].T),axis=-1)+lift['xi']
    T=view.trace_delta(f,fx,jet['K'][None,:],exact_tail_mask=view.trace_mask()[None,:])
    groups=[]
    if jacobian:
        _,_,_,original=_bound_model(view,np.r_[y.ravel(),p],{'lift':lift},True)
        for group in original:
            ids=group['indices'];profile=bool(ids[0]>=view.profile_parameter_slice.start)
            kp=jet['K_parameters'][None,:,:] if profile else np.zeros((1,view.N,len(ids)))
            ev,ex=trace_delta_direction(T,group['values'],group['xi'],kp)
            groups.append(dict(indices=ids,value=ev,angular=ex,a=group['a']))
    return ops,T,groups,f


def _gauss_cell_signed_trace_g2(problem,vector,*,order=2,high_weight=1.,jacobian=True):
    background=problem.coast_background_view()
    base=gauss_cell_positive_gauss_coast_hybrid(background,vector,order=order,high_weight=high_weight,jacobian=jacobian)
    # Return caches to the original local view so an unchanged physical
    # parameter value can reuse its bounded affine integration packet.
    if hasattr(background,'_positive_known_coast_view'):
        problem._positive_known_coast_view=background._positive_known_coast_view
    if float(problem.x[-1])<=problem.trace_start:
        base['info']['terminal_trace_change_identically_zero_on_block']=True
        return base
    rule=_view(problem,order);qv=rule['view'];tau=rule['tau'];weights=rule['weights'];order=rule['order'];cells=rule['cells']
    y,p=problem.unpack(np.asarray(vector,float))
    yq=((1-tau)[None,:,None]*y[:-1,None,:]+tau[None,:,None]*y[1:,None,:]).reshape(qv.N,qv.q)
    ops,T,groups,fields=_packet(qv,yq,p,jacobian)
    nops,Tn,ngroups,_=_packet(problem,y,p,jacobian)
    inv,adv=ops['inv'],ops['adv'];rows=d2_high_rows(problem)
    rhs=np.stack((adv*T['delta_xi'],inv*T['delta_xi']),axis=-1)
    change=-np.einsum('wcqe,q->wce',rhs.reshape(problem.work,cells,order,2),weights)
    change[:,:,0]+=np.diff(Tn['delta'],axis=1)/problem.h[None,:]
    low=np.concatenate((problem.PE@change[:,:,0],problem.PO@change[:,:,1]),axis=0).T
    high=np.stack((_high(change[:,:,0],problem.E,problem.PE),_high(change[:,:,1],problem.O,problem.PO)),axis=-1)
    result=dict(base);result['retained_cells']=base['retained_cells']+low
    result['retained_residual']=result['retained_cells'].ravel()
    result['full_codazzi_cells']=base['full_codazzi_cells']+change
    result['omitted_codazzi_cells']=base['omitted_codazzi_cells']+high
    result['high_residual']=base['high_residual']+high_weight*np.concatenate((rows.project(high[:,:,0],'even'),rows.project(high[:,:,1],'odd')),axis=0).T.ravel()
    result['point_gauss']=base['point_gauss']+T['delta']*(fields[:,:,0]+fields[:,:,2])+T['delta']**2
    info=dict(base['info']);info.update(schema='fd2d-R182-background-plus-complete-signed-trace-primitives-v1',
        actual_n_endpoint_changed=True,trace_shift_in_both_n_l=True,c_l_minus_n_cancels_exactly=True,
        retained_cell_maximum=float(np.max(abs(result['retained_cells']),initial=0.)),
        sampled_full_average_codazzi_maximum=float(np.max(abs(result['full_codazzi_cells']),initial=0.)),
        sampled_omitted_average_codazzi_maximum=float(np.max(abs(result['omitted_codazzi_cells']),initial=0.)),
        sampled_interior_Gauss_maximum=float(np.max(abs(result['point_gauss']),initial=0.)),
        terminal_C_definition='[E]/h-Q(adv E_xi) in n, -Q(inv E_xi) in m; all signed windows, exact nonlinear endpoint and complete derivatives',
        sampled_minimum_terminal_h=T['minimum_active_h'],no_n_or_h_floor_added=True,
        cut_trace_bypassed_exactly=True,actual_continuous_geometry_not_claimed=True)
    result['info']=info
    if not jacobian:return result
    lowparts=[[],[],[]];highparts=[[],[],[]];offset=problem.N*problem.q
    def add(parts,row,columns,values):
        ii,jj=np.nonzero(values)
        if len(ii):parts[0].append(row+ii);parts[1].append(np.asarray(columns)[jj]);parts[2].append(values[ii,jj])
    def project(n,m):
        return np.vstack((problem.PE@n,problem.PO@m)),np.vstack((rows.project(_high(n,problem.E,problem.PE),'even'),rows.project(_high(m,problem.O,problem.PO),'odd')))
    for cell in range(cells):
        left=np.zeros((problem.d,problem.q));right=left.copy();hl=np.zeros((rows.cell_rows,problem.q));hr=hl.copy()
        pp=np.zeros((problem.d,problem.parameter_count));hp=np.zeros((rows.cell_rows,problem.parameter_count))
        for node,sign in ((cell,-1),(cell+1,1)):
            ev,_=trace_delta_state_columns(problem,Tn,node)
            a,b=project(sign*ev/problem.h[cell],np.zeros_like(ev))
            if sign<0:left+=a;hl+=b
            else:right+=a;hr+=b
            for group in ngroups:
                ev=sign*group['value'][:,node]/problem.h[cell]
                a,b=project(ev,np.zeros_like(ev));pp[:,group['indices']]+=a;hp[:,group['indices']]+=b
        for j,t,weight in zip(range(cell*order,(cell+1)*order),tau,weights):
            _,ex=trace_delta_state_columns(qv,T,j)
            a,b=project(adv[:,j,None]*ex,inv[:,j,None]*ex)
            left-=weight*(1-t)*a;right-=weight*t*a;hl-=weight*(1-t)*b;hr-=weight*t*b
            for group in groups:
                ids=group['indices'];ex=group['angular'][:,j]
                invp=-inv[:,j,None]*group['a'][j][None,:]/ops['jet']['a'][j]
                a,b=project(adv[:,j,None]*ex,inv[:,j,None]*ex+invp*T['delta_xi'][:,j,None])
                pp[:,ids]-=weight*a;hp[:,ids]-=weight*b
        for node,a,b in ((cell,left,hl),(cell+1,right,hr)):
            cols=node*problem.q+np.arange(problem.q)
            add(lowparts,cell*problem.d,cols,a);add(highparts,cell*rows.cell_rows,cols,high_weight*b)
        add(lowparts,cell*problem.d,offset+np.arange(problem.parameter_count),pp)
        add(highparts,cell*rows.cell_rows,offset+np.arange(problem.parameter_count),high_weight*hp)
    def matrix(parts,shape):
        if not parts[2]:return sparse.csc_matrix(shape)
        out=sparse.coo_matrix((np.concatenate(parts[2]),(np.concatenate(parts[0]),np.concatenate(parts[1]))),shape=shape).tocsc();out.eliminate_zeros();return out
    result['retained_jacobian']=base['retained_jacobian']+matrix(lowparts,base['retained_jacobian'].shape)
    result['high_jacobian']=base['high_jacobian']+matrix(highparts,base['high_jacobian'].shape)
    for key in ('retained_jacobian','high_jacobian'):result[key].eliminate_zeros()
    result['info']['retained_jacobian_nonzeros']=int(result['retained_jacobian'].nnz)
    result['info']['high_jacobian_nonzeros']=int(result['high_jacobian'].nnz)
    return result


def gauss_cell_signed_trace(problem,vector,*,order=2,high_weight=1.,jacobian=True,fine_order=8,point_batch=2):
    """Fine complete RHS only on cells meeting the new signed supports."""
    from fd2d_gc_signed_trace_fine_cells import fine_signed_cells
    from fd2d_gc_positive_trace_stream_normal import radial_view
    from fd2d_gc_archive_arrays import identity
    if order!=2:raise ValueError('Preserve the original G2 diagnostic grid')
    selected=np.zeros(problem.N-1,bool)
    for part in problem.signed_windows:
        A,B,C,D=part['breaks']
        selected|=(problem.x[:-1]<D)&(problem.x[1:]>A)
    if not np.any(selected):
        out=_gauss_cell_signed_trace_g2(problem,vector,order=order,high_weight=high_weight,jacobian=jacobian)
        out['info']=dict(out['info'],grouped_signed_local_cells=[],grouped_signed_rules=[],signed_consumer_source_sha256=identity(__file__)['sha256'])
        return out
    if np.all(selected):
        return fine_signed_cells(problem,vector,high_weight=high_weight,jacobian=jacobian,fine_order=fine_order,point_batch=point_batch)
    y,p=problem.unpack(vector)
    cuts=np.r_[0,np.flatnonzero(selected[1:]!=selected[:-1])+1,problem.N-1]
    keys=('retained_residual','high_residual','retained_cells','omitted_codazzi_cells','full_codazzi_cells','point_gauss','quadrature_points')
    values={k:[] for k in keys};matrices={k:[] for k in ('retained_jacobian','high_jacobian')};infos=[];rules=[]
    for first,last in zip(cuts[:-1],cuts[1:]):
        first,last=int(first),int(last);view=radial_view(problem,np.arange(first,last+1));local=np.r_[y[first:last+1].ravel(),p]
        if selected[first]:
            packet=fine_signed_cells(view,local,high_weight=high_weight,jacobian=jacobian,fine_order=fine_order,point_batch=point_batch)
        else:
            packet=_gauss_cell_signed_trace_g2(view,local,order=2,high_weight=high_weight,jacobian=jacobian)
        for key in keys:values[key].append(packet[key])
        infos.append(packet['info'])
        for item in packet['info'].get('grouped_signed_rules',[]):rules.append(dict(item,local_cell=first+item['local_cell']))
        if jacobian:
            for key in matrices:
                a=packet[key].tocoo(copy=False);bound=view.N*view.q
                col=np.where(a.col<bound,a.col+first*problem.q,a.col-bound+problem.N*problem.q)
                matrices[key].append(sparse.coo_matrix((a.data,(a.row,col)),shape=(a.shape[0],problem.size)).tocsc())
    out={key:np.concatenate(rows,axis=1 if key in ('omitted_codazzi_cells','full_codazzi_cells','point_gauss') else 0) for key,rows in values.items()}
    for key,rows in matrices.items():out[key]=sparse.vstack(rows,format='csc') if jacobian else None
    info=dict(infos[0],grouped_signed_local_cells=np.flatnonzero(selected).tolist(),grouped_signed_rules=rules,
        signed_consumer_source_sha256=identity(__file__)['sha256'],signed_rule='complete same-point split G8; exact full n/m endpoints')
    for key in ('retained_cell_maximum','sampled_full_average_codazzi_maximum','sampled_omitted_average_codazzi_maximum','sampled_interior_Gauss_maximum'):
        info[key]=max(item[key] for item in infos)
    out['info']=info;return out
