"""Explicit new actual field with signed disjoint Gauss-trace windows.

The original archive is independently restored only as the physical and
finite structural origin. A signed archive is validated by this new
constructor; it is never presented to the original restore guard under
an old identity. Same-g representation transition and subsequent same-
representation restarts are distinguished in saved metadata.
"""
from __future__ import annotations
import copy,json
from pathlib import Path
import numpy as np
from scipy import sparse
from fd2d_gc_archive_arrays import identity,load_npz
from fd2d_gc_dyadic_tail_problem import DyadicTailRefinedDAE
from fd2d_gc_raw_bump_positive_trace import terminal_window,actual_state_columns
from fd2d_gc_raw_bump_ruling_atlas import RulingAtlasRawBumpDAE
from fd2d_gc_positive_trace_branch import trace_delta_direction,trace_delta_state_columns
from fd2d_gc_gauss_cell_frozen_operator_compatible import _OriginalR153BackgroundOnly
from fd2d_gc_signed_trace_windows import disjoint_trace_delta

SCHEMA='fd2d-R182-explicit-signed-disjoint-trace-window-field-v1'
REPRESENTATION='ruling_atlas_coast_Gauss_l_and_signed_disjoint_traces_v1'

def decoded(value):
    return json.loads(str(value))

def _window_definition(windows):
    out=[]
    for item in windows:
        name=str(item['name']);sign=int(item['sign']);breaks=tuple(map(float,item['breaks']))
        if sign not in (-1,1) or len(breaks)!=4 or not all(np.isfinite(breaks)) or not all(a<b for a,b in zip(breaks,breaks[1:])):
            raise ValueError('Each new window needs an ordered finite A<B<C<D and sign +/-1')
        out.append(dict(name=name,sign=sign,breaks=list(breaks),
            exact_dyadic_breaks=[list(x.as_integer_ratio()) for x in breaks]))
    out.sort(key=lambda d:d['breaks'][0])
    if len({p['name'] for p in out})!=len(out):raise ValueError('Window names must be distinct')
    if any(a['breaks'][3]>b['breaks'][0] for a,b in zip(out,out[1:])):
        raise ValueError('New active window supports overlap')
    return out

class SignedTraceRefinedDAE(DyadicTailRefinedDAE):
    def __init__(self,source,*,origin_field,saved_field=None,windows,split_cells=(),**kwargs):
        if tuple(split_cells):
            raise ValueError('This explicit constructor keeps the actual saved mesh; subdivision needs its own declared operation')
        if not isinstance(origin_field,(str,Path)):
            raise TypeError('The immutable original archive path is required explicitly')
        origin=load_npz(origin_field);origin_identity=identity(origin_field)
        if str(origin.get('representation_kind',''))==REPRESENTATION:
            raise ValueError('Origin must be the actual old-domain archive, not a relabelled signed field')
        super().__init__(source,saved_field=origin,split_cells=(),**kwargs)
        self._signed_origin_arrays={k:np.array(v,copy=True) for k,v in origin.items()}
        self._signed_origin_identity={k:origin_identity[k] for k in ('sha256','bytes')}
        self.original_positive_trace_definition=copy.deepcopy(self.positive_trace_definition)
        self.original_trace_start=float(self.trace_start)
        self.original_trace_ramp_stop=float(self.trace_ramp_stop)
        self.signed_windows=_window_definition(windows)
        coast_end=float(self.gauss_l_definition['support'][1])
        for part in self.signed_windows:
            A,B,C,D=part['breaks']
            if A<=coast_end or D>=self.original_trace_start:
                raise ValueError('New signed windows must be disjoint from the old R153 coast and original terminal window')
        self.trace_start=min([self.original_trace_start]+[p['breaks'][0] for p in self.signed_windows])
        # Keep original terminal scalar for source readers which explicitly
        # name that endpoint. All actual selection uses the whole window.
        self.trace_ramp_stop=self.original_trace_ramp_stop
        plateaus=[(p['breaks'][1],p['breaks'][2]) for p in self.signed_windows]
        plateaus.append((self.original_trace_ramp_stop,self.trace_cut))
        self.inactive_trace_nodes=np.array([j for j in range(1,self.N-1)
            if any(self.x[j-1]>=a and self.x[j+1]<=b for a,b in plateaus)],int)
        self.trace_gauge_pairs=np.array([(j*self.q+k,j*self.q+self.d+k)
            for j in self.inactive_trace_nodes for k in range(self.e)],int).reshape(-1,2)
        coast=np.array([j*self.q+k for j in self.inactive_l_raw_nodes for k in range(self.d,self.q)],int)
        self.additional_fixed_field_indices=np.unique(np.r_[coast,self.trace_gauge_pairs[:,1]])
        self.retained_actual_gauss_nodes=np.flatnonzero(self.retained_gauss_mask())
        self.residual_size=(self.N-1)*self.d+len(self.retained_actual_gauss_nodes)*self.e+self.q+2*self.K+2
        self.signed_trace_definition=dict(schema=SCHEMA,provider_source_sha256=identity(__file__)['sha256'],
            algebra_source_sha256=identity(Path(__file__).with_name('fd2d_gc_signed_trace_windows.py'))['sha256'],
            immutable_structural_origin=self._signed_origin_identity,origin_representation=str(origin['representation_kind']),
            original_terminal_definition=self.original_positive_trace_definition,windows=copy.deepcopy(self.signed_windows),
            window_formula='S5((s-A)/(B-A))*S5((D-s)/(D-C)), each S5 clipped to [0,1]',
            signed_shift='E=sum w_j*(sigma_j*sqrt((n-l)^2+4*m^2+4*K)-n-l)/2',
            original_terminal_sign=1,original_exact_PSD_tail_bypass_retained=True,
            disjoint_from_original_coast=True,physical_g_changed_by_representation=False,
            actual_field_changed_by_representation=True,unknown_mesh_changed=False,
            entire_hat_plateau_gauge_only=True,inactive_raw_trace_nodes=self.inactive_trace_nodes.tolist(),
            point_guard='K>=0 at active non-cut sample; h>0 for divided derivative',
            continuous_K_certificate_not_inferred_from_finite_guard=True)
        self.positive_trace_definition=copy.deepcopy(self.signed_trace_definition)
        self.representation_kind=REPRESENTATION
        self.parameter_layout()  # materialize no arrays; records explicit own schema
        if saved_field is None:
            saved=origin;transition=True
        else:
            saved=load_npz(saved_field) if isinstance(saved_field,(str,Path)) else saved_field
            kind=str(saved.get('representation_kind',''))
            if kind!=REPRESENTATION:
                if not isinstance(saved_field,(str,Path)) or identity(saved_field)['sha256']!=origin_identity['sha256']:
                    raise ValueError('Only the exact immutable origin may enter the declared representation transition')
                transition=True
            else:
                transition=False
                if decoded(saved['signed_trace_definition'])!=self.signed_trace_definition:
                    raise ValueError('Signed field definition, origin or source identity changed')
                for key in ('mesh','profile_supports','modes','candidate_sha256','angular_atlas_definition',
                            'seed_weight_definition','coast_reference_definition','reference_evaluation_definition','gauss_l_definition'):
                    if key not in saved or not np.array_equal(saved[key],origin[key]):
                        raise ValueError('Signed restart changed the defining physical/finite origin: '+key)
        if saved['corrections'].shape!=(self.N,self.q) or len(saved['parameters'])!=self.parameter_count:
            raise ValueError('Wrong saved signed state dimensions')
        self._signed_saved_arrays={k:np.array(v,copy=True) for k,v in saved.items()}
        self.signed_transition_from_original=transition
        self._operator_cache={}
        for name in ('_cell_gauss_view_cache','_chunked_gauss_codazzi_views','_interior_constraint_point_cache','_positive_known_coast_view'):
            if hasattr(self,name):delattr(self,name)

    def signed_trace_components(self):
        if not hasattr(self,'signed_windows'):
            return [dict(name='original_terminal_positive',sign=1,weight=terminal_window(self.x,self.trace_start,self.trace_ramp_stop)[None,:],original_terminal=True)]
        parts=[]
        for part in self.signed_windows:
            A,B,C,D=part['breaks']
            weight=terminal_window(self.x,A,B)*terminal_window(-self.x,-D,-C)
            parts.append(dict(name=part['name'],sign=part['sign'],weight=weight[None,:],original_terminal=False))
        parts.append(dict(name='original_terminal_positive',sign=1,
            weight=terminal_window(self.x,self.original_trace_start,self.original_trace_ramp_stop)[None,:],original_terminal=True))
        return parts

    def trace_window(self):
        return sum((p['weight'][0] for p in self.signed_trace_components()),np.zeros(self.N))

    def retained_gauss_mask(self):
        mask=(self.window()!=1.)&(self.trace_window()!=1.)&(self.x!=self.trace_cut)
        return np.asarray(mask,bool)

    def trace_delta(self,fields,angular,K,*,exact_tail_mask=None):
        return disjoint_trace_delta(fields,angular,K,self.signed_trace_components(),
            exact_tail_mask=self.trace_mask()[None,:] if exact_tail_mask is None else exact_tail_mask)

    def coast_background_view(self):
        return _OriginalR153BackgroundOnly.coast_background_view(self)

    def parameter_layout(self):
        out=super().parameter_layout()
        if hasattr(self,'signed_trace_definition'):
            out['signed_trace_definition']=self.signed_trace_definition
            out['retained_actual_gauss_nodes']=self.retained_actual_gauss_nodes.tolist()
        return out

    def evaluate(self,vector,*,jacobian=False):
        bg=self.coast_background_view()
        if jacobian and not np.any(bg.window()>0):
            # The old R153 transformation and every one of its node jets
            # are exactly zero here. Use the original affine node Jacobian,
            # avoiding the frozen R153 zero-list assembly bug in this new
            # local-only case. Its non-J evaluation supplies matching data.
            _,J,_unused=RulingAtlasRawBumpDAE.evaluate(bg.affine_view(),vector,jacobian=True)
            del _unused
            old,data=bg.evaluate(vector)
        elif jacobian:old,J,data=bg.evaluate(vector,jacobian=True)
        else:old,data=bg.evaluate(vector);J=None
        y,p=self.unpack(vector);lift=data['lift'];jet=data['profile_jet'];fields=data['fields']
        angular=np.stack((self.Ex@y[:,:self.e].T,self.Ox@y[:,self.e:self.d].T,self.Ex@y[:,self.d:].T),axis=-1)+lift['xi']
        angular[:,:,2]=data['gauss_l_delta']['actual_l_xi']
        T=self.trace_delta(fields,angular,jet['K'][None,:],exact_tail_mask=self.trace_mask()[None,:])
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
        selected=np.flatnonzero(self.retained_gauss_mask()[:-1])
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


def create_signed_trace_problem(source,*,origin_field,saved_field=None,windows,split_cells=(),**kwargs):
    return SignedTraceRefinedDAE(source,origin_field=origin_field,saved_field=saved_field,
        windows=windows,split_cells=split_cells,**kwargs)

def checkpoint_arrays(problem,vector,candidate_sha256,*,refinement_definition=None):
    if problem.representation_kind!=REPRESENTATION or candidate_sha256!=str(problem._signed_origin_arrays['candidate_sha256']):
        raise ValueError('Only this explicit signed field and original physical source can be saved')
    out={k:np.array(v,copy=True) for k,v in problem._signed_saved_arrays.items()}
    y,p=problem.unpack(np.asarray(vector,float))
    for key in ('full_gauss_nodes','codazzi_cells','omitted_codazzi_cells'):
        out.pop(key,None)
    out.update(corrections=y.copy(),parameters=p.copy(),representation_kind=np.array(REPRESENTATION),
        positive_trace_definition=np.array(json.dumps(problem.positive_trace_definition,sort_keys=True)),
        signed_trace_definition=np.array(json.dumps(problem.signed_trace_definition,sort_keys=True)),
        inactive_raw_trace_nodes=problem.inactive_trace_nodes.copy(),trace_gauge_pairs=problem.trace_gauge_pairs.copy(),
        tail_search_domain_definition=np.array(json.dumps(problem.tail_search_domain_definition,sort_keys=True)),
        tail_search_domain_kind=np.array(problem.tail_search_domain_kind))
    if refinement_definition is not None:
        out['radial_mesh_rebind_definition']=np.array(json.dumps(refinement_definition,sort_keys=True))
    return out
