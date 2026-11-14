"""R153 coast field followed by the disjoint R155 terminal positive trace.

Only the fixed protected cut neighborhood is changed. n and l both receive
E, so the actual n endpoint primitive, angular drift, Gauss, curvature and
all parameter/state derivatives are transformed together. The exact flat
cut uses the original analytic tail directly, never a derivative at h=0.
"""
from __future__ import annotations
import copy,json
import numpy as np
from scipy import sparse
from fd2d_gc_archive_arrays import identity
from fd2d_gc_raw_bump_positive_gauss import PositiveGaussRawBumpDAE,checkpoint_arrays as coast_checkpoint_arrays
from fd2d_gc_positive_trace_branch import positive_trace_delta,trace_delta_direction,trace_delta_state_columns


def terminal_window(points,start,stop):
    t=np.clip((np.asarray(points,float)-start)/(stop-start),0.,1.)
    return t*t*t*(10+t*(-15+6*t))


def actual_state_columns(problem,data,node):
    """Full actual (n,m,l) derivative versus a local raw coefficient node."""
    j=int(node);zero=np.zeros_like(problem.E)
    n=np.concatenate((problem.E,np.zeros_like(problem.O),zero),axis=1)
    m=np.concatenate((zero,problem.O,zero),axis=1)
    D=data['gauss_l_delta']
    l=np.concatenate((D['gn'][:,j,None]*problem.E,D['gm'][:,j,None]*problem.O,
                      (1+D['gl'][:,j,None])*problem.E),axis=1)
    e,_=trace_delta_state_columns(problem,data['positive_trace_delta'],j)
    return n+e,m,l+e


class PositiveTraceRawBumpDAE(PositiveGaussRawBumpDAE):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.trace_start=float(self.profile.end-.02)
        self.trace_ramp_stop=float(self.profile.end-.013)
        self.trace_cut=float(self.profile.end)
        if self.trace_start<float(np.max(self.profile.supports[:,1])):
            raise ValueError('Terminal trace must be in the fixed protected physical metric')
        if self.trace_start<=self.gauss_l_definition['support'][1]:
            raise ValueError('The actual two nonlinear windows must have disjoint supports')
        self.inactive_trace_nodes=np.array([j for j in range(1,self.N-1)
            if self.x[j-1]>=self.trace_ramp_stop and self.x[j+1]<=self.trace_cut],int)
        self.trace_gauge_pairs=np.array([(j*self.q+k,j*self.q+self.d+k)
            for j in self.inactive_trace_nodes for k in range(self.e)],int).reshape(-1,2)
        if len(self.trace_gauge_pairs):
            self.additional_fixed_field_indices=np.unique(np.r_[self.additional_fixed_field_indices,self.trace_gauge_pairs[:,1]])
        w=self.window();tw=self.trace_window()
        self.retained_actual_gauss_nodes=np.flatnonzero((w[:-1]!=1.)&(tw[:-1]!=1.))
        self.residual_size=(self.N-1)*self.d+len(self.retained_actual_gauss_nodes)*self.e+self.q+2*self.K+2
        self.positive_trace_definition=dict(schema='fd2d-terminal-positive-trace-Gauss-field-v1',
            provider_source_sha256=identity(__file__)['sha256'],
            algebra_source_sha256=identity(__import__('fd2d_gc_positive_trace_branch').__file__)['sha256'],
            composition_order='R153 coast positive-n Gauss-l first, then disjoint R155 terminal positive trace',
            start=self.trace_start,ramp_stop=self.trace_ramp_stop,cut=self.trace_cut,step=5,
            weight='S5((s-start)/(ramp_stop-start)), clipped, then exactly one up to cut',
            invariant_fields='d=n-l and m from the actual R153 background',
            h='sqrt((n-l)^2+4*m^2+4*K)',E='w*(h-n-l)/2',
            actual_fields='n_new=n+E,m_new=m,l_new=l+E',
            exact_tail_bypass='At s=cut take E=E_xi=all E parameter/state partials=0 along the accurate analytic nonnegative tail family',
            tail_contract='All correction coefficients at cut are exactly zero; existing positive tail parameters define the complete true trace',
            positive_K_domain='K>=0 at active non-cut points; h>0 when its general derivative is used; no n floor added',
            mathematical_field_changed=True,physical_metric_changed_by_representation=False,
            inactive_raw_trace_nodes=self.inactive_trace_nodes.tolist(),
            exact_trace_gauge='At entire-hat plateau nodes set raw n correction=(old n-old l)/2, raw l correction=negative of it; d unchanged',
            no_continuous_geometry_claim=True)
        self.representation_kind='ruling_atlas_coast_Gauss_l_and_terminal_positive_trace_v1'
    def trace_window(self):return terminal_window(self.x,self.trace_start,self.trace_ramp_stop)
    def trace_mask(self):return self.x==self.trace_cut
    def parameter_layout(self):
        out=super().parameter_layout();out.update(positive_trace_definition=self.positive_trace_definition,
            trace_gauge_pairs=self.trace_gauge_pairs.tolist(),raw_equations=self.residual_size)
        return out
    def impose_linear_boundary_values(self,vector):
        out=super().impose_linear_boundary_values(vector)
        # Parent zeros additional fixed columns. Preserve d BEFORE that zero
        # for the new coupled trace gauge, while retaining its old constraints.
        original=np.asarray(vector,float)
        for ni,li in self.trace_gauge_pairs:
            d=(original[ni]-original[li])/2;out[ni]=d;out[li]=-d
        return out
    def coast_background_view(self):
        """An explicit old R153 field view, used only for its background."""
        view=PositiveGaussRawBumpDAE.__new__(PositiveGaussRawBumpDAE)
        view.__dict__.update(self.__dict__)
        w=view.window();view.residual_size=view.N*view.q+2*view.K+2-np.count_nonzero(w[:-1]==1)*view.e
        return view
    def evaluate(self,vector,*,jacobian=False):
        bg=self.coast_background_view()
        if jacobian:old,J,data=bg.evaluate(vector,jacobian=True)
        else:old,data=bg.evaluate(vector);J=None
        y,p=self.unpack(vector);lift=data['lift'];jet=data['profile_jet'];fields=data['fields']
        angular=np.stack((self.Ex@y[:,:self.e].T,self.Ox@y[:,self.e:self.d].T,self.Ex@y[:,self.d:].T),axis=-1)+lift['xi']
        angular[:,:,2]=data['gauss_l_delta']['actual_l_xi']
        T=positive_trace_delta(fields,angular,jet['K'][None,:],self.trace_window()[None,:],exact_tail_mask=self.trace_mask()[None,:])
        Ep=np.zeros((self.work,self.N,self.parameter_count));Exp=np.zeros_like(Ep)
        for section,xip,profile in ((self.tail_parameter_slice,lift['xi_parameters'],False),
                (self.profile_parameter_slice,lift['profile_xi_parameters'],True)):
            kp=jet['K_parameters'][None,:,:] if profile else np.zeros((1,self.N,section.stop-section.start))
            val,ang=trace_delta_direction(T,data['fields_parameters'][:,:,:,section],xip,kp)
            Ep[:,:,section]=val;Exp[:,:,section]=ang
        data['fields_parameters'][:,:,0,:]+=Ep;data['fields_parameters'][:,:,2,:]+=Ep
        inv=1/(self.coords['u_xi']*jet['a'][None,:]);adv=self.coords['advection']
        rhs=np.concatenate((self.PE@(adv*T['delta_xi']),self.PO@(inv*T['delta_xi'])),axis=0).T
        primitive=np.concatenate(((self.PE@T['delta']).T,np.zeros((self.N,self.K))),axis=1)
        cod=data['codazzi_cells']+np.diff(primitive,axis=0)/self.h[:,None]-.5*(rhs[1:]+rhs[:-1])
        actual=T['actual'];gauss=actual[:,:,0]*actual[:,:,2]-actual[:,:,1]**2-jet['K'][None,:]
        selected=np.flatnonzero((self.window()[:-1]!=1)&(self.trace_window()[:-1]!=1))
        old_selected=np.flatnonzero(self.window()[:-1]!=1);count=(self.N-1)*self.d
        result=np.r_[cod.ravel(),(self.PE@gauss[:,selected]).T.ravel(),old[count+len(old_selected)*self.e:]]
        data.update(coast_background_fields=fields,fields=actual,full_gauss=gauss,codazzi_cells=cod,
            projected_gauss=(self.PE@gauss[:,selected]).T,positive_trace_delta=T,
            positive_trace_definition=self.positive_trace_definition,
            removed_actual_positive_trace_gauss_nodes=np.flatnonzero(self.trace_window()[:-1]==1).tolist())
        if not jacobian:return result,data
        parts_prim=[[],[],[]];parts_rhs=[[],[],[]];parts_gauss=[[],[],[]];offset=self.N*self.q
        def add(parts,row,columns,values):
            values=np.asarray(values,float);ii,jj=np.nonzero(values)
            if len(ii):parts[0].append(row+ii);parts[1].append(np.asarray(columns)[jj]);parts[2].append(values[ii,jj])
        for j in range(self.N):
            ev,ex=trace_delta_state_columns(self,T,j)
            add(parts_prim,j*self.d,j*self.q+np.arange(self.q),np.vstack((self.PE@ev,np.zeros((self.K,self.q)))))
            add(parts_rhs,j*self.d,j*self.q+np.arange(self.q),np.vstack((self.PE@(adv[:,j,None]*ex),self.PO@(inv[:,j,None]*ex))))
            ep,exp=Ep[:,j],Exp[:,j]
            add(parts_prim,j*self.d,offset+np.arange(self.parameter_count),np.vstack((self.PE@ep,np.zeros((self.K,self.parameter_count)))))
            invp=np.zeros((self.work,self.parameter_count));invp[:,self.profile_parameter_slice]=-inv[:,j,None]*jet['a_parameters'][j][None,:]/jet['a'][j]
            add(parts_rhs,j*self.d,offset+np.arange(self.parameter_count),np.vstack((self.PE@(adv[:,j,None]*exp),self.PO@(inv[:,j,None]*exp+invp*T['delta_xi'][:,j,None]))))
        for out,j in enumerate(selected):
            dn,dm,dl=actual_state_columns(self,data,j);n,m,l=actual[:,j].T
            state=l[:,None]*dn+n[:,None]*dl-2*m[:,None]*dm
            fp=data['fields_parameters'][:,j]
            par=l[:,None]*fp[:,0]+n[:,None]*fp[:,2]-2*m[:,None]*fp[:,1]
            par[:,self.profile_parameter_slice]-=jet['K_parameters'][j]
            add(parts_gauss,out*self.e,j*self.q+np.arange(self.q),self.PE@state)
            add(parts_gauss,out*self.e,offset+np.arange(self.parameter_count),self.PE@par)
        def matrix(parts,rows):
            if not parts[2]:return sparse.csc_matrix((rows,self.size))
            return sparse.coo_matrix((np.concatenate(parts[2]),(np.concatenate(parts[0]),np.concatenate(parts[1]))),shape=(rows,self.size)).tocsc()
        primJ=matrix(parts_prim,self.N*self.d);rhsJ=matrix(parts_rhs,self.N*self.d)
        diff=sparse.kron(sparse.diags([-1/self.h,1/self.h],[0,1],shape=(self.N-1,self.N)),sparse.eye(self.d),format='csc')
        avg=sparse.kron(sparse.diags([np.full(self.N-1,.5),np.full(self.N-1,.5)],[0,1],shape=(self.N-1,self.N)),sparse.eye(self.d),format='csc')
        codJ=J[:count]+diff@primJ-avg@rhsJ
        final=sparse.vstack((codJ,matrix(parts_gauss,len(selected)*self.e),J[count+len(old_selected)*self.e:]),format='csc');final.eliminate_zeros()
        return result,final,data


def checkpoint_arrays(problem,vector,candidate_sha256):
    out=coast_checkpoint_arrays(problem,vector,candidate_sha256)
    out['positive_trace_definition']=np.array(json.dumps(problem.positive_trace_definition,sort_keys=True))
    out['inactive_raw_trace_nodes']=problem.inactive_trace_nodes
    out['trace_gauge_pairs']=problem.trace_gauge_pairs
    return out
