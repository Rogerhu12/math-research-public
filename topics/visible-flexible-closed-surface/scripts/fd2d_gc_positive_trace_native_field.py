"""Actual R153 coast plus disjoint R155 terminal positive-trace field.

The old saved P1/atlas/lifting chain is reused. Interior full native jets
include the true K_s when requested. The exact cut has only the original
tail value and angular jets assigned here: a trace identity is not a zero
radial derivative. Body consumers use the angular-only interface, which
does not request unnecessary radial II derivatives or K_s.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import load_npz
from fd2d_gc_raw_native_field import (identity, locate_bound, body_rhs_from_fields,
                                    actual_body_twojet)
from fd2d_gc_bump_coast_native_field import decoded_definition
from fd2d_gc_ruling_atlas_native_field import RulingAtlasRawBumpNativeField
from fd2d_gc_positive_gauss_l_native_field import (
    PositiveGaussLNativeField, physical_profile_third)
from fd2d_gc_positive_trace_branch import positive_trace_delta
from fd2d_balanced_curvature_core import FixedBalancedGeometry

HERE=Path(__file__).resolve().parent
SCHEMA='fd2d-actual-coast-Gauss-and-terminal-positive-trace-native-v1'


def terminal_window_jets(points,start,stop):
    if not start<stop:
        raise ValueError('The fixed terminal transition needs positive width')
    x=np.asarray(points,float);t=np.clip((x-start)/(stop-start),0.,1.)
    w=t*t*t*(10+t*(-15+6*t))
    ws=30*t*t*(1-t)*(1-t)/(stop-start)
    return w,ws


def positive_trace_native_jets(background,weight,weight_s,*,exact_tail_mask=None,
                              K_s=None,include_radial=True):
    """True native angular two-jet and optional interior radial/mixed jet.

    Exact tail bypass applies to the angular trace only. The general
    interior derivative formula is never silently extended to h=0.
    """
    n,m,l=(np.asarray(background[key],float) for key in ('n','m','l'))
    packed=lambda suffix:np.stack([np.asarray(background[key+suffix],float)
                                  for key in ('n','m','l')],axis=-1)
    K=-np.asarray(background['a_ss'],float)/np.asarray(background['a'],float)
    w,ws,unused=np.broadcast_arrays(np.asarray(weight,float),np.asarray(weight_s,float),n)
    cut=np.zeros(n.shape,bool) if exact_tail_mask is None else np.broadcast_to(
        np.asarray(exact_tail_mask,bool),n.shape)
    if include_radial and np.any(cut):
        raise ValueError('Exact cut radial II jets are not assigned by the tail trace identity; '
                         'use the angular-only or physical_angular interface')
    if include_radial and K_s is None:
        raise ValueError('Requested interior radial/mixed jets need actual K_s')
    D=positive_trace_delta(packed(''),packed('_xi'),K,w,exact_tail_mask=cut)
    active=D['active'];out=dict(background)
    suffixes=('', '_xi', '_xixi') if not include_radial else ('', '_x', '_xi', '_xixi', '_x_xi')
    for name in ('n','l'):
        for suffix in suffixes:
            out[name+suffix]=np.array(background[name+suffix],copy=True)
        if not include_radial:
            out.pop(name+'_x',None);out.pop(name+'_x_xi',None)
    increments={'':D['delta'],'_xi':D['delta_xi'],'_xixi':np.zeros_like(n)}
    if include_radial:
        increments.update(_x=np.zeros_like(n),_x_xi=np.zeros_like(n))
    if np.any(active):
        get=lambda name:np.asarray(background[name],float)[active]
        d=n[active]-l[active];mi=m[active];h=D['h'][active];hu=D['h_xi'][active]
        du=get('n_xi')-get('l_xi');mu=get('m_xi')
        duu=get('n_xixi')-get('l_xixi');muu=get('m_xixi')
        huu=(du*du+d*duu+4*(mu*mu+mi*muu)-hu*hu)/h
        increments['_xixi'][active]=w[active]*(huu-get('n_xixi')-get('l_xixi'))/2
        if include_radial:
            dx=get('n_x')-get('l_x');mx=get('m_x')
            dxu=get('n_x_xi')-get('l_x_xi');mxu=get('m_x_xi')
            ks=np.broadcast_to(np.asarray(K_s,float),n.shape)[active]
            hx=(d*dx+4*mi*mx+2*ks)/h
            hxu=(dx*du+d*dxu+4*(mx*mu+mi*mxu)-hx*hu)/h
            increments['_x'][active]=(w[active]*(hx-get('n_x')-get('l_x'))
                                       +ws[active]*(h-n[active]-l[active]))/2
            increments['_x_xi'][active]=(w[active]*(hxu-get('n_x_xi')-get('l_x_xi'))
                                          +ws[active]*(hu-get('n_xi')-get('l_xi')))/2
    for name in ('n','l'):
        for suffix in suffixes:
            out[name+suffix]+=increments[suffix]
            if not np.all(np.isfinite(out[name+suffix])):
                raise FloatingPointError('Nonfinite actual positive-trace jet '+name+suffix)
    return out


def _declared(saved,key,supplied):
    present=saved.get(key)
    if present is None and supplied is None:
        raise ValueError('The actual saved field must explicitly declare '+key)
    value=decoded_definition(present if supplied is None else supplied)
    if present is not None and decoded_definition(present)!=value:
        raise ValueError('Caller definition differs from saved '+key)
    return value


class PositiveTraceNativeField(PositiveGaussLNativeField):
    """Thin explicitly declared extension; original frozen sources untouched."""
    def __init__(self,arrays,candidate,*,gauss_l_definition=None,
                 positive_trace_definition=None,**kwargs):
        saved=load_npz(arrays)
        coast=_declared(saved,'gauss_l_definition',gauss_l_definition)
        terminal=_declared(saved,'positive_trace_definition',positive_trace_definition)
        # Reuse the complete R149 chain. The frozen R153 constructor only
        # accepts its own representation_kind, so validate the same R153
        # input explicitly before composing the additional declared map.
        RulingAtlasRawBumpNativeField.__init__(self,arrays,candidate,**kwargs)
        if self.representation_kind!='ruling_atlas_coast_Gauss_l_and_terminal_positive_trace_v1':
            raise ValueError('Wrong explicitly saved combined representation')
        if coast.get('schema')!='fd2d-positive-n-local-Gauss-l-field-v1':
            raise ValueError('Unsupported coast Gauss definition')
        for key,name in dict(provider_source_sha256='fd2d_gc_raw_bump_positive_gauss.py',
                             algebra_source_sha256='fd2d_gc_positive_gauss_l.py').items():
            if coast.get(key)!=identity(HERE/name)['sha256']:
                raise ValueError('Changed coast defining source: '+key)
        ref=self.coast_reference;rim=ref.length*self.reference_rim_fraction
        expected_coast=dict(support=[ref.entry_s,ref.exit_s],rim_fraction=self.reference_rim_fraction,
            weight='same S5 coast-window function as the declared frozen reference',
            l='(1-w)*l_raw+w*(K+m^2)/n; evaluate quotient only where w>0',
            n_and_m='unchanged complete affine P1 correction plus exact declared lifting',
            true_gauss_identity='G_actual=(1-w)*G_raw',
            gauss_plateau=[ref.entry_s+rim,ref.exit_s-rim],known_lifting_unchanged=True,
            physical_metric_changed_by_representation=False)
        for key,value in expected_coast.items():
            if coast.get(key)!=value:raise ValueError('Changed coast field definition: '+key)
        inactive=[j for j in range(1,len(self.nodes)-1)
                  if self.nodes[j-1]>=ref.entry_s+rim and self.nodes[j+1]<=ref.exit_s-rim]
        if coast.get('inactive_l_raw_nodes')!=inactive:
            raise ValueError('Saved coast inactive hats differ from the actual mesh')
        if 'inactive_l_raw_nodes' in saved and not np.array_equal(saved['inactive_l_raw_nodes'],inactive):
            raise ValueError('Saved coast inactive node array disagrees')
        self.gauss_l_definition=coast
        self.minimum_active_n=float(coast['selected_finite_evaluation_floor'])
        if not np.isfinite(self.minimum_active_n) or self.minimum_active_n<=0:
            raise ValueError('The original finite positive coast margin must be explicit')
        self._minimum_sampled_active_n=None;self._maximum_consumed_abs_K_s=0.
        if terminal.get('schema')!='fd2d-terminal-positive-trace-Gauss-field-v1':
            raise ValueError('Unsupported terminal positive-trace schema')
        for key,name in dict(provider_source_sha256='fd2d_gc_raw_bump_positive_trace.py',
                             algebra_source_sha256='fd2d_gc_positive_trace_branch.py').items():
            if terminal.get(key)!=identity(HERE/name)['sha256']:
                raise ValueError('Changed terminal defining source: '+key)
        self.trace_start=float(self.profile.end-.02)
        self.trace_ramp_stop=float(self.profile.end-.013)
        self.trace_cut=float(self.profile.end)
        if self.trace_start<max(float(np.max(self.profile.supports[:,1])),ref.exit_s):
            raise ValueError('Terminal map must be protected and disjoint from the coast map')
        expected_terminal=dict(
            composition_order='R153 coast positive-n Gauss-l first, then disjoint R155 terminal positive trace',
            start=self.trace_start,ramp_stop=self.trace_ramp_stop,cut=self.trace_cut,step=5,
            weight='S5((s-start)/(ramp_stop-start)), clipped, then exactly one up to cut',
            invariant_fields='d=n-l and m from the actual R153 background',
            h='sqrt((n-l)^2+4*m^2+4*K)',E='w*(h-n-l)/2',
            actual_fields='n_new=n+E,m_new=m,l_new=l+E',
            exact_tail_bypass='At s=cut take E=E_xi=all E parameter/state partials=0 along the accurate analytic nonnegative tail family',
            tail_contract='All correction coefficients at cut are exactly zero; existing positive tail parameters define the complete true trace',
            physical_metric_changed_by_representation=False,mathematical_field_changed=True)
        for key,value in expected_terminal.items():
            if terminal.get(key)!=value:raise ValueError('Changed terminal field definition: '+key)
        trace_inactive=[j for j in range(1,len(self.nodes)-1)
            if self.nodes[j-1]>=self.trace_ramp_stop and self.nodes[j+1]<=self.trace_cut]
        if terminal.get('inactive_raw_trace_nodes')!=trace_inactive:
            raise ValueError('Declared raw-trace hats differ from the actual mesh')
        if not np.all(self.values[-1]==0.) or np.any(self.tail.coefficients<0.):
            raise ValueError('Exact tail bypass requires actual zero cut correction and nonnegative tail')
        if self.profile.jet([self.trace_cut])['K'][0]!=0.:
            raise ValueError('The exact tail bypass requires the bound flat cut')
        self.positive_trace_definition=terminal
        self._maximum_terminal_abs_K_s=0.

    def evaluate_coast_native(self,x,xi,*,side='right'):
        return PositiveGaussLNativeField.evaluate_native(self,x,xi,side=side)

    def evaluate_coast_angular_native(self,x,xi,*,side='right'):
        return PositiveGaussLNativeField.evaluate_angular_native(self,x,xi,side=side)

    def evaluate_angular_native(self,x,xi,*,side='right'):
        background=self.evaluate_coast_angular_native(x,xi,side=side)
        xx,unused=np.broadcast_arrays(np.asarray(x,float),np.asarray(xi,float))
        w,ws=terminal_window_jets(xx,self.trace_start,self.trace_ramp_stop)
        return positive_trace_native_jets(background,w,ws,exact_tail_mask=xx==self.trace_cut,
                                          include_radial=False)

    def evaluate_native(self,x,xi,*,side='right'):
        xx,unused=np.broadcast_arrays(np.asarray(x,float),np.asarray(xi,float))
        if np.any(xx==self.trace_cut):
            raise ValueError('Exact cut radial II jets are not claimed; use evaluate_angular_native '
                             'or physical_angular for the complete actual cut value and angular two-jet')
        background=self.evaluate_coast_native(x,xi,side=side)
        w,ws=terminal_window_jets(xx,self.trace_start,self.trace_ramp_stop)
        active=w>0;ks=np.zeros(xx.shape,float)
        if np.any(active):
            unique,inverse=np.unique(xx[active],return_inverse=True)
            third=physical_profile_third(self.profile,unique,side=side)[inverse]
            a,av,acc=(np.asarray(background[key],float)[active] for key in ('a','a_s','a_ss'))
            ks[active]=-third/a+acc*av/(a*a)
            self._maximum_terminal_abs_K_s=max(self._maximum_terminal_abs_K_s,maximum(abs(ks[active])))
        return positive_trace_native_jets(background,w,ws,K_s=ks,include_radial=True)

    def physical_angular(self,x,u,*,side='right'):
        xi=self.invert_angle(x,u);out=self.evaluate_angular_native(x,xi,side=side)
        h,hxi=out['U_xi'],out['U_xixi']
        for name in ('l','m','n'):
            out[name+'_u']=out[name+'_xi']/h
            out[name+'_uu']=(out[name+'_xixi']-out[name+'_u']*hxi)/(h*h)
        out['requested_u']=np.broadcast_to(np.asarray(u,float),np.shape(xi))
        out['angle_inverse_error']=out['u']-out['requested_u']
        return out

    def body_rhs(self,x,state,u):
        q=self.physical_angular(x,u)
        return body_rhs_from_fields(state,**{k:q[k] for k in ('J','l','m','l_u','m_u','l_uu','m_uu')})

    def body_jets(self,x,state,u):
        q=self.physical_angular(x,u)
        return actual_body_twojet(state,a=q['a'],l=q['l'])

    @classmethod
    def from_definition(cls,path):
        path=Path(path);meta=json.loads(path.read_text())
        if meta['schema']!=SCHEMA:raise ValueError('Wrong combined native schema')
        for row in meta['sources']:locate_bound(path,row)
        geometry=FixedBalancedGeometry(moments=locate_bound(path,meta['moments']),
                                       means=locate_bound(path,meta['means']))
        cache=meta.get('reference_cache_input')
        return cls(locate_bound(path,meta['arrays']),locate_bound(path,meta['candidate_input']),
            reference_inlet=locate_bound(path,meta['reference_inlet_input']),
            reference_cache=None if cache is None else locate_bound(path,cache),
            angular_atlas_definition=meta['angular_atlas_definition'],
            coast_reference_definition=meta['coast_reference_definition'],
            gauss_l_definition=meta['gauss_l_definition'],
            positive_trace_definition=meta['positive_trace_definition'],
            seed_weight_definition=meta['seed_weight_definition'],representation_kind=meta['representation_kind'],
            blend_interval=meta['blend_interval'],profile_supports=meta['profile_supports'],
            fixed_base_T=meta['fixed_base_T'],base_kind=meta['base_kind'],tail_kind=meta['tail_kind'],
            candidate_sha256=meta['candidate_input']['sha256'],collar_guard=meta['collar_guard'],geometry=geometry)

    def definition(self):
        meta=PositiveGaussLNativeField.definition(self);meta['schema']=SCHEMA
        meta['sources']=[identity(HERE/name) for name in (
            'fd2d_gc_positive_trace_native_field.py','fd2d_gc_positive_trace_branch.py',
            'fd2d_gc_raw_bump_positive_trace.py')]+meta['sources']
        meta['positive_trace_definition']=self.positive_trace_definition
        meta['actual_complete_field']='Full saved affine P1/lifting/atlas, then declared coast R153, then disjoint terminal R155'
        meta['independent_n_is_actual_everywhere']=False
        meta['jet_requirements']['outside_window']='Outside both declared windows original actual jets are retained; no profile third derivative is queried by the terminal map there'
        meta['jet_requirements']['radial_and_mixed']='Actual one-sided K_s for the coast and terminal interiors only; exact cut radial II jets are not assigned'
        meta['terminal_cut_jet_scope']=dict(
            actual_cut_values_and_angular_first_second='Original accurate nonnegative tail directly; increment is identically zero as an angular trace function',
            radial_and_mixed_cut_jets='Not assigned by this reader; no assertion E_s=0 or general square-root differentiability at h=0',
            interior_radial_and_mixed='Complete quotient/product formulas with actual piecewise K_s',
            angular_queries_require_K_s=False,
            interior_to_cut_angular_second_trace_continuity_certified=False,
            arbitrary_saved_P1_field_C2_join_certified=False,
            added_C3_completion_requirement=False)
        meta['actual_shape_denominator']='Original coast n in its declared positive domain; terminal h only at active non-cut interior points'
        meta['terminal_native_statistics']=dict(maximum_consumed_abs_K_s=self._maximum_terminal_abs_K_s,
            continuous_geometry_certificate=False)
        meta['actual_body_consumer']='Existing fixed-material 24-column formula, using physical_angular only; no radial II endpoint jet requested and no body solve performed here'
        return meta


def maximum(value):
    return float(np.max(np.asarray(value),initial=0.))
