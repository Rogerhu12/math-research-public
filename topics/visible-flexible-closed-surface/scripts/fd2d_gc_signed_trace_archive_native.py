"""Explicit native reader for actual R182 signed-window archives.

Only the real immutable old archive enters the old structural constructor.
The new archive is decoded here, under its own schema, and its actual raw
and parameter arrays replace no input identity.  All parameter-dependent
core/profile/tail and plain-lifting objects are rebuilt explicitly.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path
import numpy as np

from fd2d_gc_archive_arrays import identity, load_npz
from fd2d_gc_raw_native_field import locate_bound
from fd2d_gc_dyadic_tail_archive_native import (
    DyadicTailArchiveNativeField, bind_dyadic_tail_archive_native,
    _bind_nonlinear_definitions)
from fd2d_gc_radial_bump_profile import RadialBumpProfile
from fd2d_balanced_curvature_core import BalancedCurvatureCore
from fd2d_dyadic_bernstein_tail import DyadicBernsteinFlatDevelopableFamily
from fd2d_gc_positive_trace_native_field_v2 import (
    PositiveTraceNativeField, positive_trace_native_jets, terminal_window_jets,
    physical_profile_third, maximum)

HERE=Path(__file__).resolve().parent
SCHEMA='fd2d-R182-actual-signed-disjoint-trace-archive-native-v1'
REPRESENTATION='ruling_atlas_coast_Gauss_l_and_signed_disjoint_traces_v1'
FIELD_SCHEMA='fd2d-R182-explicit-signed-disjoint-trace-window-field-v1'
PARENT_SHA256='e4a5c9c30aff8bb008dda528da07f6a92b2d6a8f5d1c14487245c63b2e6230e8'


def declared(arrays,key):
    if key not in arrays:
        raise ValueError('The actual signed archive must declare '+key)
    return json.loads(str(arrays[key]))


def signed_native_jets(background,weight,weight_s,sign,*,exact_tail_mask=None,
                       K_s=None,include_radial=True):
    """P_minus(S)=-P_plus(-S), with every actual value/angle/radial jet."""
    if sign==1:
        return positive_trace_native_jets(background,weight,weight_s,
            exact_tail_mask=exact_tail_mask,K_s=K_s,include_radial=include_radial)
    if sign!=-1:
        raise ValueError('A constant trace sign +/-1 is required')
    if exact_tail_mask is not None and np.any(exact_tail_mask):
        raise ValueError('The original accurate PSD tail is the positive branch only')
    negative=dict(background)
    keys=[name+suffix for name in ('n','m','l')
          for suffix in ('','_x','_xi','_xixi','_x_xi') if name+suffix in background]
    for key in keys:
        negative[key]=-np.asarray(background[key])
    answer=positive_trace_native_jets(negative,weight,weight_s,
        K_s=K_s,include_radial=include_radial)
    for key in keys:
        if key in answer:
            answer[key]=-answer[key]
    return answer


class SignedTraceArchiveNativeField(DyadicTailArchiveNativeField):
    def __init__(self,arrays,*,origin_field,foundation_definition):
        if identity(HERE/'fd2d_gc_dyadic_tail_archive_native.py')['sha256']!=PARENT_SHA256:
            raise ValueError('The frozen structural-origin reader changed')
        saved=load_npz(arrays);origin=load_npz(origin_field)
        if str(saved.get('representation_kind',''))!=REPRESENTATION:
            raise ValueError('This constructor only decodes the explicit signed representation')
        definition=declared(saved,'signed_trace_definition')
        if (definition.get('schema')!=FIELD_SCHEMA or
                declared(saved,'positive_trace_definition')!=definition):
            raise ValueError('The complete signed definition and its declared alias disagree')
        origin_id=identity(origin_field)
        if definition.get('immutable_structural_origin')!={k:origin_id[k] for k in ('bytes','sha256')}:
            raise ValueError('The actual structural origin differs')
        for key,name in [('provider_source_sha256','fd2d_gc_signed_trace_problem.py'),
                         ('algebra_source_sha256','fd2d_gc_signed_trace_windows.py')]:
            if definition.get(key)!=identity(HERE/name)['sha256']:
                raise ValueError('Changed signed mathematical source: '+key)
        # Only this genuine old archive is passed to the old decoder.
        original=bind_dyadic_tail_archive_native(origin_field,
                                                foundation_definition=foundation_definition)
        self.__dict__.update(original.__dict__)
        self.origin_field_path=Path(origin_field)
        self.foundation_definition_path=Path(foundation_definition)
        static=('mesh','profile_supports','modes','central_parameter_count','tail_parameter_count',
            'profile_count','candidate_sha256','fixed_base_T','base_kind','tail_kind','profile_kind',
            'blend','angular_atlas_definition','seed_weight_definition','coast_reference_definition',
            'reference_evaluation_definition','gauss_l_definition','nested_angular_definition',
            'tail_search_domain_kind','tail_search_domain_definition')
        for key in static:
            if key not in saved or key not in origin or not np.array_equal(saved[key],origin[key]):
                raise ValueError('The declared fixed structural origin changed: '+key)
        self.arrays_path=Path(arrays)
        self.nodes,self.values,self.parameters=(np.asarray(saved[k]) for k in ('mesh','corrections','parameters'))
        if (self.values.shape!=(len(self.nodes),3*self.K+2) or
                self.parameters.shape!=(self.parameter_count,) or
                not all(v.dtype==np.float64 and np.all(np.isfinite(v))
                        for v in (self.nodes,self.values,self.parameters))):
            raise ValueError('Malformed actual signed arrays or explicit independent layout')
        self.profile=RadialBumpProfile(self.candidate_path,supports=saved['profile_supports'],
            collar_guard=float(original.definition()['collar_guard']),
            coefficients=self.parameters[self.profile_parameter_slice])
        self.core=BalancedCurvatureCore(self.parameters[self.central_slice],
            base_kind=self.base_kind,geometry=self.geometry)
        self.tail=DyadicBernsteinFlatDevelopableFamily(self.parameters[self.tail_parameter_slice],
            cut_radius=.8,cuff_radius=.32,flat_radius=.34,plane_height=1.25)
        if (not self.tail.control_certificate['passed'] or
                declared(saved,'tail_search_domain_certificate')!=self.tail.control_certificate):
            raise ValueError('The complete actual tail certificate must match the current controls')
        for array in (self.nodes,self.values,self.parameters):
            array.flags.writeable=False
        self._inverse_seed_cache={}
        terminal=definition.get('original_terminal_definition')
        if terminal!=original.positive_trace_definition:
            raise ValueError('The original terminal component changed')
        # This validates the explicitly nested old component and the coast,
        # not the new archive under an old representation identifier.
        _bind_nonlinear_definitions(self,saved,declared(saved,'gauss_l_definition'),terminal)
        self.original_positive_trace_definition=copy.deepcopy(terminal)
        self.signed_trace_definition=copy.deepcopy(definition)
        self.positive_trace_definition=copy.deepcopy(definition)
        self.signed_windows=copy.deepcopy(definition['windows'])
        previous=float(self.coast_reference.exit_s)
        names=set()
        for item in self.signed_windows:
            A,B,C,D=map(float,item['breaks'])
            if (item['sign'] not in (-1,1) or item['name'] in names or
                    not previous<A<B<C<D<self.trace_start or
                    item['exact_dyadic_breaks']!=[list(v.as_integer_ratio()) for v in (A,B,C,D)]):
                raise ValueError('Invalid or overlapping exact signed support/plateau definition')
            names.add(item['name']);previous=D
        expected=dict(original_terminal_sign=1,original_exact_PSD_tail_bypass_retained=True,
            disjoint_from_original_coast=True,physical_g_changed_by_representation=False,
            actual_field_changed_by_representation=True,unknown_mesh_changed=False,
            entire_hat_plateau_gauge_only=True,
            window_formula='S5((s-A)/(B-A))*S5((D-s)/(D-C)), each S5 clipped to [0,1]',
            signed_shift='E=sum w_j*(sigma_j*sqrt((n-l)^2+4*m^2+4*K)-n-l)/2')
        for key,value in expected.items():
            if definition.get(key)!=value:
                raise ValueError('Unsupported signed full-function definition: '+key)
        plateaus=[(p['breaks'][1],p['breaks'][2]) for p in self.signed_windows]
        plateaus.append((self.trace_ramp_stop,self.trace_cut))
        inactive=[j for j in range(1,len(self.nodes)-1)
            if any(self.nodes[j-1]>=a and self.nodes[j+1]<=b for a,b in plateaus)]
        pairs=np.array([(j*(3*self.K+2)+k,j*(3*self.K+2)+self.d+k)
            for j in inactive for k in range(self.e)],dtype=int).reshape(-1,2)
        if (definition['inactive_raw_trace_nodes']!=inactive or
                not np.array_equal(saved['inactive_raw_trace_nodes'],inactive) or
                not np.array_equal(saved['trace_gauge_pairs'],pairs)):
            raise ValueError('Signed gauge indices must use the complete current P1 hats')
        self.trace_gauge_pairs=pairs
        self.representation_kind=REPRESENTATION
        # The zero-correction lifting view must use the current parameters,
        # not the structural origin's former core/profile/tail instances.
        self._plain_lifting_view=copy.copy(self)
        self._plain_lifting_view.values=np.zeros_like(self.values)
        self._plain_lifting_view.values.flags.writeable=False

    def signed_components(self,x):
        x=np.asarray(x,float);result=[]
        for part in self.signed_windows:
            A,B,C,D=part['breaks']
            rise,rise_s=terminal_window_jets(x,A,B)
            fall,fall_negative_s=terminal_window_jets(-x,-D,-C)
            result.append((part['sign'],rise*fall,rise_s*fall-rise*fall_negative_s,False))
        w,ws=terminal_window_jets(x,self.trace_start,self.trace_ramp_stop)
        result.append((1,w,ws,True))
        return result

    def _signed_apply(self,background,x,*,include_radial,side):
        x=np.asarray(x,float);components=self.signed_components(x)
        active=np.zeros(x.shape,bool)
        for sign,w,ws,terminal in components:
            if np.any(active&(w>0)):
                raise ValueError('The actual signed supports overlap')
            active|=w>0
        ks=np.zeros(x.shape,float)
        if include_radial and np.any(active):
            unique,inverse=np.unique(x[active],return_inverse=True)
            third=physical_profile_third(self.profile,unique,side=side)[inverse]
            a,av,acc=(np.asarray(background[key])[active] for key in ('a','a_s','a_ss'))
            ks[active]=-third/a+acc*av/(a*a)
            self._maximum_terminal_abs_K_s=max(self._maximum_terminal_abs_K_s,maximum(abs(ks[active])))
        output=background
        for sign,w,ws,terminal in components:
            output=signed_native_jets(output,w,ws,sign,
                exact_tail_mask=(x==self.trace_cut) if terminal else None,
                K_s=ks,include_radial=include_radial)
        return output

    def evaluate_angular_native(self,x,xi,*,side='right'):
        xx,angle=np.broadcast_arrays(np.asarray(x,float),np.asarray(xi,float))
        background=self.evaluate_coast_angular_native(xx,angle,side=side)
        return self._signed_apply(background,xx,include_radial=False,side=side)

    def evaluate_native(self,x,xi,*,side='right'):
        xx,angle=np.broadcast_arrays(np.asarray(x,float),np.asarray(xi,float))
        if np.any(xx==self.trace_cut):
            raise ValueError('The exact cut has angular jets only; no signed map assigns radial II jets there')
        background=self.evaluate_coast_native(xx,angle,side=side)
        return self._signed_apply(background,xx,include_radial=True,side=side)

    def definition(self):
        meta=DyadicTailArchiveNativeField.definition(self)
        meta.update(schema=SCHEMA,source=identity(__file__),
            sources=[identity(HERE/name) for name in ('fd2d_gc_signed_trace_archive_native.py',
                'fd2d_gc_signed_trace_problem.py','fd2d_gc_signed_trace_windows.py')]+meta['sources'],
            origin_input=identity(self.origin_field_path),
            foundation_definition_input=identity(self.foundation_definition_path),
            signed_trace_definition=self.signed_trace_definition,
            original_terminal_definition=self.original_positive_trace_definition,
            signed_archive_decoded_by_legacy_constructor=False,
            legacy_constructor_receives_only_real_origin_archive=True,
            actual_complete_field='Actual raw/affine/atlas plus original coast R153, declared disjoint signed R182 windows and original positive terminal component',
            signed_second_jet_formula='P_minus(S)=-P_plus(-S), with full value/xi/xixi/s/sxi; exact K_s only when the radial jets are requested',
            no_source_field_or_solver_mutation=True,
            continuous_positive_K_domain_not_inferred_from_point_evaluation=True)
        return meta

    @classmethod
    def from_definition(cls,path):
        path=Path(path);meta=json.loads(path.read_text())
        if meta.get('schema')!=SCHEMA:
            raise ValueError('Wrong explicit signed archive-native schema')
        for source in meta['sources']:
            locate_bound(path,source)
        result=cls(locate_bound(path,meta['arrays']),
            origin_field=locate_bound(path,meta['origin_input']),
            foundation_definition=locate_bound(path,meta['foundation_definition_input']))
        if result.signed_trace_definition!=meta['signed_trace_definition']:
            raise ValueError('The saved signed native mathematical definition changed')
        return result


__all__=['SignedTraceArchiveNativeField','signed_native_jets','SCHEMA']
