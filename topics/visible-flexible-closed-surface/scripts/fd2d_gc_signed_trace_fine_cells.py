"""Complete R182 field in common split-fine cell averages.

Only cells intersecting a new signed window use this finite rule. Full
actual n/m endpoints, the whole common-point RHS and all state/profile/
tail derivatives are retained. This is a new finite equation, not a
certificate that G8 equals the continuous integral.
"""
from __future__ import annotations
import numpy as np
from scipy import sparse
from fd2d_gc_archive_arrays import identity
from fd2d_gc_grouped_coast_codazzi import _actual_packet as _coast_packet
from fd2d_gc_hybrid_lifting_codazzi_d2 import fixed_lifting_breaks,point_view,quadrature_on_parts
from fd2d_gc_positive_gauss_l import gauss_delta_direction,gauss_delta_state_columns
from fd2d_gc_positive_trace_branch import trace_delta_direction,trace_delta_state_columns
from fd2d_gc_raw_bump_positive_trace import actual_state_columns
from fd2d_gc_d2_complements import d2_high_rows
from fd2d_gc_codazzi_complement import _high


def _packet(view,y,p,jacobian):
    out=_coast_packet(view,y,p,jacobian)
    T=view.trace_delta(out['actual'],out['actual_xi'],out['jet']['K'][None,:],
                       exact_tail_mask=view.trace_mask()[None,:])
    out['coast_actual']=out['actual'];out['coast_actual_xi']=out['actual_xi']
    out['actual']=T['actual'];out['actual_xi']=T['actual_angular'];out['trace']=T
    f=out['actual'];fx=out['actual_xi'];inv=out['ops']['inv'];adv=out['ops']['adv'];c=out['jet']['c']
    out['rhs']=np.stack((inv*fx[:,:,1]+c[None,:]*(f[:,:,2]-f[:,:,0])+adv*fx[:,:,0],
                        inv*fx[:,:,2]-2*c[None,:]*f[:,:,1]+adv*fx[:,:,1]),axis=-1)
    out['gauss']=f[:,:,0]*f[:,:,2]-f[:,:,1]**2-out['jet']['K'][None,:]
    return out


def _group_fields(view,packet,group):
    ids=group['indices'];physical=bool(ids[0]>=view.profile_parameter_slice.start)
    kp=packet['jet']['K_parameters'][None,:,:] if physical else np.zeros((1,view.N,len(ids)))
    value=np.array(group['values'],copy=True);angular=np.array(group['xi'],copy=True)
    dv,dx=gauss_delta_direction(packet['delta'],value,angular,kp)
    value[:,:,2]+=dv;angular[:,:,2]+=dx
    ev,ex=trace_delta_direction(packet['trace'],value,angular,kp)
    value[:,:,0]+=ev;value[:,:,2]+=ev
    angular[:,:,0]+=ex;angular[:,:,2]+=ex
    return ids,value,angular


def _group_rhs(view,packet,group):
    ids,value,angular=_group_fields(view,packet,group)
    a=packet['jet']['a'];c=packet['jet']['c'];inv=packet['ops']['inv'];adv=packet['ops']['adv']
    ap=group['a'];cp=group['c'];ip=-inv[:,:,None]*ap[None,:,:]/a[None,:,None]
    f=packet['actual'];fx=packet['actual_xi']
    n=(ip*fx[:,:,1,None]+inv[:,:,None]*angular[:,:,1]+cp[None,:,:]*(f[:,:,2]-f[:,:,0])[:,:,None]
       +c[None,:,None]*(value[:,:,2]-value[:,:,0])+adv[:,:,None]*angular[:,:,0])
    m=(ip*fx[:,:,2,None]+inv[:,:,None]*angular[:,:,2]-2*cp[None,:,:]*f[:,:,1,None]
       -2*c[None,:,None]*value[:,:,1]+adv[:,:,None]*angular[:,:,1])
    return ids,n,m


def _project(problem,rows,n,m):
    return (np.concatenate((problem.PE@n,problem.PO@m),axis=0),
            np.concatenate((rows.project(_high(n,problem.E,problem.PE),'even'),
                            rows.project(_high(m,problem.O,problem.PO),'odd')),axis=0))


def fine_signed_cells(problem,vector,*,high_weight=1.,jacobian=True,fine_order=8,point_batch=2):
    y,p=problem.unpack(np.asarray(vector,float))
    cells=problem.N-1;W=problem.work;q=problem.q;P=problem.parameter_count
    if cells<1 or int(fine_order)!=fine_order or not 2<=fine_order<=16 or not 1<=point_batch<=8:
        raise ValueError('Use actual positive cells and bounded split-fine quadrature')
    rows=d2_high_rows(problem)
    knots,definitions=fixed_lifting_breaks(problem)
    extra=[x for part in problem.signed_windows for x in part['breaks']]
    knots=np.array(sorted(set(knots.tolist()+extra)))
    full=np.empty((W,cells,2));retained=np.empty((cells,problem.d));omitted=np.empty_like(full)
    point_gauss=np.empty((W,2*cells));point_coordinates=np.empty(2*cells)
    low_parts=[[],[],[]];high_parts=[[],[],[]];observations=[]
    def add(parts,row,columns,matrix):
        ii,jj=np.nonzero(matrix)
        if len(ii):parts[0].append(row+ii);parts[1].append(np.asarray(columns)[jj]);parts[2].append(matrix[ii,jj])
    if jacobian:
        zn=np.zeros((W,q));zm=zn.copy();zl=zn.copy();zxn=zn.copy();zxm=zn.copy();zxl=zn.copy()
        zn[:,:problem.e]=problem.E;zm[:,problem.e:problem.d]=problem.O;zl[:,problem.d:]=problem.E
        zxn[:,:problem.e]=problem.Ex;zxm[:,problem.e:problem.d]=problem.Ox;zxl[:,problem.d:]=problem.Ex
    for cell in range(cells):
        left,right=map(float,problem.x[cell:cell+2]);h=right-left
        cuts=[left]+knots[(knots>left)&(knots<right)].tolist()+[right]
        xx,weights,panels=quadrature_on_parts(left,right,cuts,int(fine_order))
        ev=point_view(problem,[left,right]);endpoint=_packet(ev,y[cell:cell+2],p,jacobian)
        end=(endpoint['actual'][:,1,:2]-endpoint['actual'][:,0,:2])/h
        average=np.zeros((W,2));fine_g=0.;minimum_h=np.inf
        if jacobian:
            jl=np.zeros((problem.d,q));jr=jl.copy();hl=np.zeros((rows.cell_rows,q));hr=hl.copy()
            jp=np.zeros((problem.d,P));hp=np.zeros((rows.cell_rows,P))
            compatible=dict(gauss_l_delta=endpoint['delta'],positive_trace_delta=endpoint['trace'])
            for j,sgn in ((0,-1),(1,1)):
                dn,dm,dl=actual_state_columns(ev,compatible,j)
                a,b=_project(problem,rows,sgn*dn/h,sgn*dm/h)
                if j==0:jl+=a;hl+=b
                else:jr+=a;hr+=b
            for group in endpoint['groups']:
                ids,value,angle=_group_fields(ev,endpoint,group)
                d=(value[:,1,:2]-value[:,0,:2])/h
                a,b=_project(problem,rows,d[:,0],d[:,1]);jp[:,ids]+=a;hp[:,ids]+=b
        del endpoint,ev
        for start in range(0,len(xx),int(point_batch)):
            pts=xx[start:start+point_batch];ww=weights[start:start+point_batch];t=(pts-left)/h
            view=point_view(problem,pts);yy=(1-t[:,None])*y[cell]+t[:,None]*y[cell+1]
            packet=_packet(view,yy,p,jacobian)
            average+=np.einsum('wje,j->we',packet['rhs'],ww)
            fine_g=max(fine_g,float(np.max(abs(packet['gauss']),initial=0.)))
            mh=packet['trace']['minimum_active_h']
            if mh is not None:minimum_h=min(minimum_h,mh)
            if jacobian:
                pr=[_group_rhs(view,packet,g) for g in packet['groups']]
                for j,(tau,w) in enumerate(zip(t,ww)):
                    cv,cx=gauss_delta_state_columns(view,packet['delta'],j)
                    tv,tx=trace_delta_state_columns(view,packet['trace'],j)
                    # R153 and every signed support are disjoint, so the
                    # trace state columns act on raw fields here exactly.
                    dn=zn+tv;dm=zm;dl=zl+cv+tv
                    nx=zxn+tx;mx=zxm;lx=zxl+cx+tx
                    inv=packet['ops']['inv'][:,j,None];adv=packet['ops']['adv'][:,j,None];c=packet['jet']['c'][j]
                    fn=inv*mx+c*(dl-dn)+adv*nx;fm=inv*lx-2*c*dm+adv*mx
                    a,b=_project(problem,rows,fn,fm)
                    jl-=w*(1-tau)*a;jr-=w*tau*a;hl-=w*(1-tau)*b;hr-=w*tau*b
                    for ids,pn,pm in pr:
                        a,b=_project(problem,rows,pn[:,j],pm[:,j]);jp[:,ids]-=w*a;hp[:,ids]-=w*b
                del pr
            del packet,view
        full[:,cell]=end-average
        low,high=_project(problem,rows,full[:,cell,0],full[:,cell,1])
        retained[cell]=low
        omitted[:,cell,0]=_high(full[:,cell,0],problem.E,problem.PE)
        omitted[:,cell,1]=_high(full[:,cell,1],problem.O,problem.PO)
        if jacobian:
            for node,a,b in ((cell,jl,hl),(cell+1,jr,hr)):
                cols=node*q+np.arange(q);add(low_parts,cell*problem.d,cols,a);add(high_parts,cell*rows.cell_rows,cols,high_weight*b)
            cols=problem.N*q+np.arange(P);add(low_parts,cell*problem.d,cols,jp);add(high_parts,cell*rows.cell_rows,cols,high_weight*hp)
        gx,gw,_=quadrature_on_parts(left,right,[left,right],2);gt=(gx-left)/h
        gv=point_view(problem,gx);gd=_packet(gv,(1-gt[:,None])*y[cell]+gt[:,None]*y[cell+1],p,False)
        point_gauss[:,2*cell:2*cell+2]=gd['gauss'];point_coordinates[2*cell:2*cell+2]=gx
        del gd,gv
        observations.append(dict(local_cell=cell,endpoints=[left,right],cuts=cuts,points=xx.tolist(),
            average_weights=weights.tolist(),panels=panels,fine_sampled_Gauss_maximum=fine_g,
            finite_minimum_signed_h=None if np.isinf(minimum_h) else float(minimum_h)))
    def matrix(parts,count):
        if not parts[2]:return sparse.csc_matrix((count,problem.size))
        out=sparse.coo_matrix((np.concatenate(parts[2]),(np.concatenate(parts[0]),np.concatenate(parts[1]))),shape=(count,problem.size)).tocsc()
        out.eliminate_zeros();return out
    high=high_weight*np.concatenate((rows.project(omitted[:,:,0],'even'),rows.project(omitted[:,:,1],'odd')),axis=0).T.ravel()
    info=dict(schema='fd2d-R182-whole-actual-signed-split-fine-cell-v1',source_sha256=identity(__file__)['sha256'],
        order=2,diagnostic_Gauss_order=2,grouped_signed_order=int(fine_order),grouped_signed_local_cells=list(range(cells)),
        grouped_signed_rules=observations,declared_physical_knots=definitions,signed_window_knots=extra,
        selected_coast_local_cells=[],grouped_coast_local_cells=[],known_lifting_full_change_maximum=0.,
        known_lifting_change_not_separately_evaluated=True,whole_actual_common_point_integral=True,
        actual_n_and_m_endpoints=True,all_state_tail_and_physical_parameter_derivatives=True,
        finite_equations_changed=True,unknown_mesh_changed=False,physical_g_changed=False,
        retained_cell_maximum=float(np.max(abs(retained),initial=0.)),
        sampled_full_average_codazzi_maximum=float(np.max(abs(full),initial=0.)),
        sampled_omitted_average_codazzi_maximum=float(np.max(abs(omitted),initial=0.)),
        sampled_interior_Gauss_maximum=float(np.max(abs(point_gauss),initial=0.)),
        fine_sampled_interior_Gauss_maximum=max(z['fine_sampled_Gauss_maximum'] for z in observations),
        continuous_certificate=False,finite_G8_not_an_exact_integral=True)
    return dict(retained_residual=retained.ravel(),high_residual=high,retained_cells=retained,
        omitted_codazzi_cells=omitted,full_codazzi_cells=full,point_gauss=point_gauss,quadrature_points=point_coordinates,
        retained_jacobian=matrix(low_parts,cells*problem.d) if jacobian else None,
        high_jacobian=matrix(high_parts,cells*rows.cell_rows) if jacobian else None,info=info)
