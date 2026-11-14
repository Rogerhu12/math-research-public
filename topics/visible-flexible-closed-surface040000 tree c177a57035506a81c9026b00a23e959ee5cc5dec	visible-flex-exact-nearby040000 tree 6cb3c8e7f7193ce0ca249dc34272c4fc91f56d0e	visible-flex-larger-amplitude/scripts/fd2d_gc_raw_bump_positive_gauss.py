"""Same physical target with the R153 positive-n local Gauss-l field.

n and m retain their complete affine P1+lifting definitions. l is blended
to (K+m^2)/n only inside the selected coast. The actual Gauss rows and every
actual Codazzi/curvature derivative use this transformed field.
"""
from __future__ import annotations
import copy,json
import numpy as np
from scipy import sparse
from fd2d_gc_archive_arrays import identity
from fd2d_gc_raw_bump_ruling_atlas import RulingAtlasRawBumpDAE,checkpoint_arrays as affine_checkpoint_arrays
from fd2d_gc_raw_bump_coast_reference import coast_window
from fd2d_gc_positive_gauss_l import positive_gauss_l_delta,gauss_delta_direction,gauss_delta_state_columns


class PositiveGaussRawBumpDAE(RulingAtlasRawBumpDAE):
    def __init__(self,*args,minimum_active_n=.05,**kwargs):
        super().__init__(*args,**kwargs)
        self.minimum_active_n=float(minimum_active_n)
        if not self.minimum_active_n>0:raise ValueError('Use a positive finite search margin')
        ref=self.coast_reference;rim=ref.length*self.reference_rim_fraction
        self.gauss_plateau=(ref.entry_s+rim,ref.exit_s-rim)
        w,_=coast_window(self.x,ref.entry_s,ref.length,self.reference_rim_fraction)
        self.retained_gauss_nodes=np.flatnonzero(w[:-1]!=1.)
        self.inactive_l_raw_nodes=np.array([j for j in range(1,self.N-1)
            if self.x[j-1]>=self.gauss_plateau[0] and self.x[j+1]<=self.gauss_plateau[1]],int)
        self.additional_fixed_field_indices=np.concatenate([j*self.q+np.arange(self.d,self.q)
            for j in self.inactive_l_raw_nodes]) if len(self.inactive_l_raw_nodes) else np.array([],int)
        self.affine_residual_size=self.N*self.q+2*self.K+2
        self.residual_size=self.affine_residual_size-(self.N-1-len(self.retained_gauss_nodes))*self.e
        self.gauss_l_definition=dict(schema='fd2d-positive-n-local-Gauss-l-field-v1',
            provider_source_sha256=identity(__file__)['sha256'],
            algebra_source_sha256=identity(__import__('fd2d_gc_positive_gauss_l').__file__)['sha256'],
            support=[ref.entry_s,ref.exit_s],rim_fraction=self.reference_rim_fraction,
            weight='same S5 coast-window function as the declared frozen reference',
            l='(1-w)*l_raw+w*(K+m^2)/n; evaluate quotient only where w>0',
            n_and_m='unchanged complete affine P1 correction plus exact declared lifting',
            true_gauss_identity='G_actual=(1-w)*G_raw',
            exact_pointwise_domain='n>0 at every point with w>0; no positivity condition imposed at the flat n=0 tail',
            regularity_sufficient_domain='uniform n>=nu>0 on a neighborhood of the closed coast support, as in R153',
            actual_continuous_positive_certificate_paid=False,
            selected_finite_evaluation_floor=self.minimum_active_n,
            finite_floor_is_not_continuous_certificate_or_nonexistence_condition=True,
            gauss_plateau=list(self.gauss_plateau),
            inactive_l_raw_nodes=self.inactive_l_raw_nodes.tolist(),
            exact_elimination_reason='entire nodal P1 hat support lies in w=1, so (1-w)*hat is identically zero',
            rim_adjacent_l_nodes_not_removed=True,known_lifting_unchanged=True,
            physical_metric_changed_by_representation=False,
            active_profile_K_s='base K0 coast: -sum(delta_j*psi_j_third)/a + a_ss*a_s/a^2',
            old_field_preserved=False,full_actual_G_C_curvature_required=True)
        self.representation_kind='global_ruling_atlas_positive_n_local_Gauss_l_v1'
    def parameter_layout(self):
        out=super().parameter_layout();out.update(gauss_l_definition=self.gauss_l_definition,
            raw_equations=self.residual_size,inactive_l_field_columns=self.additional_fixed_field_indices.tolist())
        return out
    def impose_linear_boundary_values(self,vector):
        out=super().impose_linear_boundary_values(vector)
        out[self.additional_fixed_field_indices]=0.
        return out
    def window(self):
        ref=self.coast_reference
        return coast_window(self.x,ref.entry_s,ref.length,self.reference_rim_fraction)[0]
    def affine_view(self):
        view=copy.copy(self);view.residual_size=view.N*view.q+2*view.K+2
        return view
    def evaluate(self,vector,*,jacobian=False):
        vector=np.asarray(vector,float)
        raw_view=self.affine_view()
        if jacobian:old,J,data=RulingAtlasRawBumpDAE.evaluate(raw_view,vector,jacobian=True)
        else:old,data=RulingAtlasRawBumpDAE.evaluate(raw_view,vector);J=None
        y,p=self.unpack(vector);fields=data['fields'];lift=data['lift'];jet=data['profile_jet']
        angular=np.stack((self.Ex@y[:,:self.e].T,self.Ox@y[:,self.e:self.d].T,self.Ex@y[:,self.d:].T),axis=-1)+lift['xi']
        w=self.window();D=positive_gauss_l_delta(fields,angular,jet['K'][None,:],w[None,:],minimum_active_n=self.minimum_active_n)
        inv=1/(self.coords['u_xi']*jet['a'][None,:]);c=jet['c']
        correction_rhs=np.concatenate((self.PE@(c[None,:]*D['delta']),self.PO@(inv*D['delta_xi'])),axis=0).T
        cod=data['codazzi_cells']-.5*(correction_rhs[1:]+correction_rhs[:-1])
        # Only actual nonredundant Gauss rows remain. The platform identity
        # is exact mathematically; pointwise floating defects are still kept
        # in full_gauss diagnostics, never replaced by old raw Gauss.
        actual=fields.copy();actual[:,:,2]=D['actual_l']
        gauss=actual[:,:,0]*actual[:,:,2]-actual[:,:,1]**2-jet['K'][None,:]
        selected=np.flatnonzero(w[:-1]!=1.)
        count=(self.N-1)*self.d;gauss_count=(self.N-1)*self.e
        result=np.r_[cod.ravel(),(self.PE@gauss[:,selected]).T.ravel(),old[count+gauss_count:]]
        parameter_groups=[]
        for section,angular_p,profile in ((self.tail_parameter_slice,lift['xi_parameters'],False),
                (self.profile_parameter_slice,lift['profile_xi_parameters'],True)):
            directions=data['fields_parameters'][:,:,:,section]
            kp=jet['K_parameters'][None,:,:] if profile else np.zeros((1,self.N,section.stop-section.start))
            dv,dx=gauss_delta_direction(D,directions,angular_p,kp)
            parameter_groups.append((section,dv,dx,profile))
            data['fields_parameters'][:,:,2,section]=((1-D['weight'])[...,None]*directions[:,:,2]
                +D['gn'][...,None]*directions[:,:,0]+D['gm'][...,None]*directions[:,:,1]+D['gK'][...,None]*kp)
        data.update(affine_fields=fields,affine_full_gauss=data['full_gauss'],fields=actual,
            full_gauss=gauss,codazzi_cells=cod,projected_gauss=(self.PE@gauss[:,selected]).T,
            gauss_l_delta=D,gauss_l_definition=self.gauss_l_definition,
            affine_node_gauss_rows_removed=np.flatnonzero(w[:-1]==1.).tolist(),
            actual_field_and_parameter_jets_consistent=True)
        if not jacobian:return result,data
        rr=[];cc=[];vv=[];offset=self.N*self.q
        def block(row,columns,values):
            value=np.asarray(values,float);ii,jj=np.nonzero(value)
            if len(ii):rr.append(row+ii);cc.append(np.asarray(columns)[jj]);vv.append(value[ii,jj])
        for j in range(self.N):
            dv,dx=gauss_delta_state_columns(self,D,j)
            state=np.concatenate((self.PE@(c[j]*dv),self.PO@(inv[:,j,None]*dx)),axis=0)
            block(j*self.d,j*self.q+np.arange(self.q),state)
            for section,dp,dxp,profile in parameter_groups:
                dn=c[j]*dp[:,j];dm=inv[:,j,None]*dxp[:,j]
                if profile:
                    dn+=jet['c_parameters'][j][None,:]*D['delta'][:,j,None]
                    invp=-inv[:,j,None]*jet['a_parameters'][j][None,:]/jet['a'][j]
                    dm+=invp*D['delta_xi'][:,j,None]
                par=np.concatenate((self.PE@dn,self.PO@dm),axis=0)
                block(j*self.d,offset+np.arange(section.start,section.stop),par)
        nodeJ=sparse.coo_matrix((np.concatenate(vv),(np.concatenate(rr),np.concatenate(cc))),shape=(self.N*self.d,self.size)).tocsc()
        average=sparse.kron(sparse.diags([np.full(self.N-1,.5),np.full(self.N-1,.5)],[0,1],shape=(self.N-1,self.N)),sparse.eye(self.d),format='csc')
        Jcod=J[:count]-average@nodeJ
        GJ=J[count:count+gauss_count]
        GJ=sparse.diags(np.repeat(1-w[:-1],self.e))@GJ
        kept=(selected[:,None]*self.e+np.arange(self.e)).ravel()
        actualJ=sparse.vstack((Jcod,GJ[kept],J[count+gauss_count:]),format='csc');actualJ.eliminate_zeros()
        return result,actualJ,data


def checkpoint_arrays(problem,vector,candidate_sha256):
    out=affine_checkpoint_arrays(problem,vector,candidate_sha256)
    out['gauss_l_definition']=np.array(json.dumps(problem.gauss_l_definition,sort_keys=True))
    out['inactive_l_raw_nodes']=problem.inactive_l_raw_nodes
    out['finite_radial_scheme']=np.array('Exact affine lifting endpoints plus Gauss2 physical PDE with complete nonlinear Gauss-l correction')
    return out
