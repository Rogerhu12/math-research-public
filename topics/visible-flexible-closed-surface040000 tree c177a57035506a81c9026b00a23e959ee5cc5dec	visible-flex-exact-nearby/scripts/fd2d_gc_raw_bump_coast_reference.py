"""Same target metric with a frozen accurate-coast reference in the lifting.

The reference solves GC on the original base coast only. On a nonzero-delta
outer design it is just a fixed known function; all target residuals and
profile derivative terms remain present. Unknown n,m,l are still independent.
"""
from __future__ import annotations
import numpy as np
from fd2d_gc_raw_bump_turn_mesh import TurnResolvedRawBumpDAE
from fd2d_gc_raw_lifted_dae import step5
from fd2d_gc_frozen_coast_reference import FrozenCoastReference


def coast_window(x, entry_s, length, rim_fraction=.12):
    if not 0 < rim_fraction < .5 or not length > 0:
        raise ValueError('A positive plateau requires 0 < rim_fraction < one half')
    x=np.asarray(x,float);rim=float(length)*float(rim_fraction)
    left,left_q=step5((x-float(entry_s))/rim)
    right,right_q=step5((float(entry_s)+float(length)-x)/rim)
    return left*right, (left_q*right-left*right_q)/rim


def _forcing(problem,ops,value,radial,angular):
    extra=(1,)*(value.ndim-3)
    inv=np.asarray(ops['inv']).reshape((problem.work,problem.N)+extra)
    adv=np.asarray(ops['adv']).reshape((problem.work,problem.N)+extra)
    c=np.asarray(ops['jet']['c']).reshape((1,problem.N)+extra)
    fn=inv*angular[:,:,1]+c*(value[:,:,2]-value[:,:,0])+adv*angular[:,:,0]-radial[:,:,0]
    fm=inv*angular[:,:,2]-2*c*value[:,:,1]+adv*angular[:,:,1]-radial[:,:,1]
    return np.concatenate((np.einsum('ew,wn...->ne...',problem.PE,fn),
                           np.einsum('kw,wn...->nk...',problem.PO,fm)),axis=1)


class CoastReferenceRawBumpDAE(TurnResolvedRawBumpDAE):
    def __init__(self,*args,reference_inlet,reference_cache=None,
                 reference_rim_fraction=.12,**kwargs):
        super().__init__(*args,**kwargs)
        self.coast_reference=FrozenCoastReference(reference_inlet,cache_path=reference_cache)
        self.reference_rim_fraction=float(reference_rim_fraction)
        ref=self.coast_reference
        if ref.candidate_sha256 != self.profile.source_identity['sha256']:
            raise ValueError('The reference coast is not bound to this base candidate')
        if ref.entry_s < self.profile.central_end or ref.entry_s+ref.length >= self.profile.end:
            raise ValueError('Reference support must avoid the central cylinder and actual cut')
        coast_window(self.x,ref.entry_s,ref.length,self.reference_rim_fraction)
        self.representation_kind='targeted_turn_mesh_exact_cylinder_frozen_coast_reference_v1'
        # Functional checkpoint identity must not depend on mutable cache
        # counters or the checkout's absolute filesystem path.
        provenance=ref.definition()
        self.coast_reference_provenance=provenance
        reference_identity={key:provenance[key] for key in
            ('schema','binding_sha256','candidate_sha256','physical_coast',
             'a_c','v','component_order','inverse_tolerance','cached_jets_dtype')}
        self.coast_reference_definition=dict(reference=reference_identity,
            support=[ref.entry_s,ref.entry_s+ref.length],rim_fraction=self.reference_rim_fraction,
            weight='S5((s-entry)/rim)*S5((exit-s)/rim), each argument clipped to [0,1]',
            lifting='(1-w)*old_seed_tail_lifting+w*frozen_native_reference',
            reference_parameters_frozen=True,original_physical_g_changed=False,
            accurate_reference_GC_applies_only_to_base_delta_zero=True,
            target_defects_and_target_profile_derivatives_not_omitted=True,
            angular_chart_fixed_across_unknown_parameters=True)

    def parameter_layout(self):
        out=super().parameter_layout()
        out['coast_reference_definition']=self.coast_reference_definition
        return out

    def lifting(self,delta,tail_parameters):
        out=super().lifting(delta,tail_parameters)
        ref=self.coast_reference
        w,ws=coast_window(self.x,ref.entry_s,ref.length,self.reference_rim_fraction)
        reference=ref.jet_on_grid(self.x,self.coords,active_mask=(w!=0)|(ws!=0))
        V,X,Xi=(np.asarray(reference[k],float) for k in ('values','x','xi'))
        expected=(self.work,self.N,3)
        if any(q.shape!=expected or not np.all(np.isfinite(q)) for q in (V,X,Xi)):
            raise ValueError('Wrong or nonfinite fixed-reference value and true spatial jets')
        old,old_x,old_xi=out['values'],out['x'],out['xi']
        scalar=w[None,:,None];scalar_x=ws[None,:,None]
        out['values']=(1-scalar)*old+scalar*V
        out['x']=(1-scalar)*old_x+scalar*X+scalar_x*(V-old)
        out['xi']=(1-scalar)*old_xi+scalar*Xi
        wp=w[None,:,None,None];wsp=ws[None,:,None,None]
        oldp=out['parameters']
        out['parameters']=(1-wp)*oldp
        out['x_parameters']=(1-wp)*out['x_parameters']-wsp*oldp
        out['xi_parameters']=(1-wp)*out['xi_parameters']
        oldp=out['profile_parameters']
        out['profile_parameters']=(1-wp)*oldp
        out['profile_s_parameters']=(1-wp)*out['profile_s_parameters']-wsp*oldp
        out['profile_x_parameters']=out['profile_s_parameters']
        out['profile_xi_parameters']=(1-wp)*out['profile_xi_parameters']
        ops=self.operators(delta)
        out['forcing']=_forcing(self,ops,out['values'],out['x'],out['xi'])
        out['forcing_parameters']=_forcing(self,ops,out['parameters'],out['x_parameters'],out['xi_parameters'])
        out['coast_reference_definition']=self.coast_reference_definition
        return out

    def warm_from_plain_bump(self,mesh,corrections,parameters,*,source_representation_kind):
        """New initializer, NOT a representation-preserving conversion.

        At original nodes the entire previous field is convexly blended
        with the reference. Between nodes the new correction is the P1
        interpolant of the new node coefficients, not a nonlinear product.
        """
        if 'coast_reference' in str(source_representation_kind):
            raise ValueError('Do not apply the initializer twice to an existing reference field')
        mesh=np.asarray(mesh,float);y=np.asarray(corrections,float);p=np.asarray(parameters,float)
        if not np.array_equal(mesh,self.x) or y.shape!=(self.N,self.q) or p.shape!=(self.parameter_count,):
            raise ValueError('Explicitly transfer mesh/order/layout before selecting this new initializer')
        ref=self.coast_reference
        w,_=coast_window(self.x,ref.entry_s,ref.length,self.reference_rim_fraction)
        yy=(1-w)[:,None]*y
        before=np.r_[yy.ravel(),p.copy()]
        vector=self.impose_linear_boundary_values(before)
        return vector,dict(schema='fd2d-frozen-coast-new-initial-field-v1',
            old_representation_kind=str(source_representation_kind),
            new_representation_kind=self.representation_kind,
            same_mesh=True,parameters_unchanged=bool(np.array_equal(self.unpack(vector)[1],p)),
            same_physical_metric=True,nonlinear_solve_performed=False,
            nodal_target='(1-w)*old_full_field+w*frozen_reference',
            exact_reference_plateau_node_count=int(np.count_nonzero(w==1)),
            changed_correction_node_count=int(np.count_nonzero(w!=0)),
            correction_change_maximum=float(np.max(abs(yy-y))),
            exact_cylinder_boundary_projection_change=float(np.max(abs(vector-before))),
            preserved_old_complete_field=False,
            between_nodes='Actual new P1 correction plus the declared smooth reference lifting; recompute the complete residual')
