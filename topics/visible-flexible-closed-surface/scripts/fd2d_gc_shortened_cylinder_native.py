"""R168 exact cylinder restriction/translation of a bound complete native field.

The mathematical field is the parent's complete function at s+Delta. No
candidate, window or P1 coefficient file is rewritten. Named integration
knots have exact rational translated coordinates and separate binary64
representatives. The parent cut is selected explicitly at the child cut.
"""
from __future__ import annotations
from fractions import Fraction as Q
import json
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import load_npz
from fd2d_gc_raw_native_field import identity, locate_bound, body_rhs_from_fields, actual_body_twojet
from fd2d_gc_actual_body_reader_factory import load_actual_body_reader

HERE=Path(__file__).resolve().parent
SCHEMA='fd2d-parent-complete-native-shortened-cylinder-v1'


def rational(value):
    if isinstance(value,Q):return value
    if isinstance(value,(float,np.floating)):return Q.from_float(float(value))
    return Q(str(value))


def fraction_record(value):
    value=rational(value)
    return dict(exact=str(value),approximate=float(value))


class RadialTranslation:
    """Exact symbolic shift plus its explicitly labelled floating evaluator."""
    def __init__(self,parent_nodes,delta):
        self.delta=rational(delta)
        self.delta_float=float(self.delta)
        old=np.asarray(parent_nodes,float)
        old_exact=[Q.from_float(float(x)) for x in old]
        if not 0<self.delta<old_exact[-1]:
            raise ValueError('Delta must lie strictly within the parent domain')
        indices=[j for j,q in enumerate(old_exact) if q>self.delta]
        self.parent_indices=[None]+indices
        self.exact_knots=[Q(0)]+[old_exact[j]-self.delta for j in indices]
        self.nodes=np.array([float(q) for q in self.exact_knots])
        if np.any(np.diff(self.nodes)<=0):
            raise ArithmeticError('Distinct exact translated knots lost binary64 ordering; no knots were silently merged')
        self.nodes.flags.writeable=False
        self.parent_nodes=old
        self.parent_end=float(old[-1]);self.end=float(self.nodes[-1])
        self._named={float(s):j for j,s in enumerate(self.nodes)}

    def __call__(self,s):
        ss=np.asarray(s,float)
        if np.any(~np.isfinite(ss)) or np.any(ss<0) or np.any(ss>self.end):
            raise ValueError('Outside the shortened radial domain')
        out=ss+self.delta_float
        # Exact equality selects a named knot, never a proximity snap.
        # This also makes the cut use the parent's declared accurate cut.
        for value in np.unique(ss):
            j=self._named.get(float(value))
            if j is not None:
                p=self.parent_indices[j]
                mapped=self.delta_float if p is None else float(self.parent_nodes[p])
                out=np.where(ss==value,mapped,out)
        return out

    def point_record(self,s):
        s=float(s);j=self._named.get(s)
        exact_s=Q.from_float(s) if j is None else self.exact_knots[j]
        mapped=float(self(s))
        return dict(child_binary64=s,named_knot_index=j,
            child_mathematical_coordinate=fraction_record(exact_s),
            displayed_coordinate_error=fraction_record(Q.from_float(s)-exact_s),
            parent_binary64=mapped,
            mapped_coordinate_error=fraction_record(Q.from_float(mapped)-exact_s-self.delta),
            parent_cut_selected_explicitly=bool(s==self.end and mapped==self.parent_end))

    def definition(self):
        return dict(Delta=fraction_record(self.delta),Delta_binary64=self.delta_float,
            Delta_binary64_error=fraction_record(Q.from_float(self.delta_float)-self.delta),
            formula='parent_s = child_s + Delta, mathematically exact; derivative is 1',
            exact_translated_saved_mesh=[str(q) for q in self.exact_knots],
            binary64_integration_mesh=self.nodes.tolist(),parent_node_indices=self.parent_indices,
            mesh_role='Mandatory P1 split coordinates only; no new interpolated coefficient array defines the field',
            parent_cut_binary64=self.parent_end,
            child_cut_exact_relative_to_parent_saved_coordinate=str(self.exact_knots[-1]),
            child_cut_binary64=self.end,
            named_knot_semantics='Exact equality with a listed representative denotes that exact named translated knot; no near-point snapping',
            ordinary_point_semantics='A non-named binary64 child coordinate is added to binary64 Delta; resulting scalar rounding is evaluation error',
            mathematical_profile_scope='Parent accurate profile and named-cut semantics are inherited; this layer supplies no new parent scalar interval certificate',
            parent_cut_called_explicitly=True)


class TranslatedProfile:
    """Read-only target metric composition; no candidate/window regeneration."""
    def __init__(self,parent,mapping):
        self.parent,self.mapping=parent,mapping
        self.end=mapping.end;self.a0=parent.a0
        self.central_end_exact=Q.from_float(float(parent.central_end))-mapping.delta
        self.central_end=float(self.central_end_exact)
        self.parameter_count=parent.parameter_count
        self.coefficients=parent.coefficients
        self.supports_exact=[[str(Q.from_float(float(v))-mapping.delta) for v in row]
            for row in parent.supports]
        self.supports=np.array([[float(Q(v)) for v in row] for row in self.supports_exact])
        self.supports.flags.writeable=False
        self.breaks_exact=[Q(0)]+[Q.from_float(float(v))-mapping.delta for v in parent.breaks
            if Q.from_float(float(v))>mapping.delta]
        self.breaks=np.array([float(v) for v in self.breaks_exact])
        self.breaks.flags.writeable=False

    def jet(self,s):
        ss=np.atleast_1d(np.asarray(s,float))
        out=dict(self.parent.jet(self.mapping(ss)))
        out['parent_s_evaluated']=np.asarray(out['s']).copy()
        out['s']=ss.copy()
        return out

    def profile(self,s):
        q=self.jet(s)
        return q['a'],q['a_s'],q['a_ss']

    def jvp(self,s,direction):
        # Delta is fixed; all physical profile directions are simply pulled back.
        return self.parent.jvp(self.mapping(s),direction)

    def definition(self):
        return dict(kind='fixed-Delta exact composition of the parent target metric',
            a='parent.a(s+Delta)',physical_metric='ds^2+parent.a(s+Delta)^2 du^2',
            Delta=str(self.mapping.delta),parent=self.parent.definition(),
            central_end_exact_relative_to_parent_saved_coordinate=str(self.central_end_exact),
            supports_exact_relative_to_parent_saved_coordinates=self.supports_exact,
            breaks_exact_relative_to_parent_saved_coordinates=[str(q) for q in self.breaks_exact],
            physical_metric_changed_from_parent=True,profile_parameters_unchanged=True,
            parent_candidate_edited=False)


def verify_parent_cylinder(parent):
    """Structural continuous-cylinder check, not a pointwise geometry sample.

    l=m=0 on every intersecting P1 hat and all noncentral liftings vanish.
    Their complete finite angle functions are therefore zero throughout.
    Raw n need not vanish and is deliberately preserved.
    """
    saved=load_npz(parent.arrays_path)
    declared=json.loads(str(saved['central_field_definition']))
    L=float(parent.profile.central_end)
    first=parent.profile.parent.base.segments[0] if isinstance(parent.profile,TranslatedProfile) else parent.profile.base.segments[0]
    if declared.get('kind')!='exact_central_cylinder' or declared.get('s_start')!=0 or declared.get('s_end')!=L:
        raise ValueError('The selected parent does not explicitly identify this exact central cylinder')
    j=int(np.searchsorted(parent.nodes,L,side='left'))
    covered=parent.values[:j+1]
    checks=dict(
        central_profile_coast=first.get('kind')=='coast' and first.get('p0')==0. and first.get('p1')==0.,
        complete_m_and_l_P1_coefficients_zero=bool(np.all(covered[:,parent.e:]==0.)),
        seed_plateau_covers_cylinder=parent.seed_weight_definition['kind']=='central_plateau' and parent.seed_weight_definition['start']>=L,
        tail_lifting_zero_on_cylinder=.42*parent.profile.end>=L,
        coast_lifting_zero_on_cylinder=parent.coast_reference.entry_s>=L,
        terminal_map_zero_on_cylinder=parent.trace_start>=L,
        profile_bumps_zero_on_cylinder=bool(np.all(parent.profile.supports[:,0]>=L)),
        original_angular_chart_stationary=parent.blend_interval[0]>=L,
        ruling_atlas_transition_after_cylinder=parent.angular_atlas_definition['entry_transition'][0]>=L)
    if not all(checks.values()):
        raise ValueError('The actual parent lacks a required cylinder identity: '+str(checks))
    return dict(parent_declared_definition=declared,checks=checks,
        half_length_binary64=L,half_length_saved_coordinate_exact=str(Q.from_float(L)),
        covered_P1_node_indices=list(range(j+1)),
        raw_n_coefficients_may_be_nonzero=True,
        all_central_raw_rows_identical=bool(np.all(covered==covered[0])),
        meaning='Actual fixed-material F_s=0 and X_s=e_z throughout the cylinder; no extra equality between floating raw n and core n is imposed')


class ShortenedCylinderNativeField:
    def __init__(self,parent_definition,delta='7/50'):
        self.parent_definition_path=Path(parent_definition)
        self.parent=load_actual_body_reader(self.parent_definition_path).native
        self.parent_metadata=json.loads(self.parent_definition_path.read_text())
        self.cylinder_certificate=verify_parent_cylinder(self.parent)
        delta=rational(delta)
        if not 0<delta<Q.from_float(float(self.parent.profile.central_end)):
            raise ValueError('Require 0 < Delta < the actual parent cylinder half-length')
        self.mapping=RadialTranslation(self.parent.nodes,delta)
        self.nodes=self.mapping.nodes
        self.profile=TranslatedProfile(self.parent.profile,self.mapping)
        for name in ('K','e','d','core','geometry','parameters','parameter_count',
                'central_parameter_count','tail_parameter_count','profile_count',
                'explicit_parameter_layout','central_slice','tail_parameter_slice',
                'profile_parameter_slice','arrays_path','candidate_path','base_kind','tail_kind'):
            setattr(self,name,getattr(self.parent,name))
        # This is a position-reference used only by the existing single-rigid
        # cut comparison. Actual Z comes from the reconstructed body/registration.
        self.tail=self.parent.tail

    def _coordinates(self,out,s):
        out=dict(out)
        shape=np.shape(out['n'])
        ss=np.broadcast_to(np.asarray(s,float),shape)
        out['parent_x_evaluated']=np.asarray(out['x']).copy()
        out['parent_s_evaluated']=np.asarray(out['s']).copy()
        out['x']=ss.copy();out['s']=ss.copy()
        # Parent cell labels are provenance, not indices into the child mesh.
        if 'cell' in out:out['parent_cell']=out.pop('cell')
        return out

    def evaluate_angular_native(self,s,xi,*,side='right'):
        return self._coordinates(self.parent.evaluate_angular_native(self.mapping(s),xi,side=side),s)

    def evaluate_native(self,s,xi,*,side='right'):
        return self._coordinates(self.parent.evaluate_native(self.mapping(s),xi,side=side),s)

    def physical_angular(self,s,u,*,side='right'):
        return self._coordinates(self.parent.physical_angular(self.mapping(s),u,side=side),s)

    def physical(self,s,u,*,side='right'):
        return self._coordinates(self.parent.physical(self.mapping(s),u,side=side),s)

    def chart(self,s,xi,*,side=None):
        return self.parent.chart(self.mapping(s),xi,side=side)

    def invert_angle(self,s,u):return self.parent.invert_angle(self.mapping(s),u)
    def body_initial(self,u):return self.parent.body_initial(u)

    def body_rhs(self,s,state,u):
        q=self.physical_angular(s,u)
        return body_rhs_from_fields(state,**{k:q[k] for k in ('J','l','m','l_u','m_u','l_uu','m_uu')})

    def body_jets(self,s,state,u):
        q=self.physical_angular(s,u)
        return actual_body_twojet(state,a=q['a'],l=q['l'])

    def translate_parent_body_state(self,state,*,upper=True):
        out=np.array(state,dtype=float,copy=True)
        if out.shape[-1]!=24:raise ValueError('Require the existing 24-component actual body state')
        out[...,2]+=(-1 if upper else 1)*self.mapping.delta_float
        return out

    def definition(self):
        return dict(schema=SCHEMA,source=identity(__file__),
            parent_native_definition=identity(self.parent_definition_path),
            parent_complete_definition=self.parent_metadata,
            arrays=identity(self.arrays_path),candidate_input=identity(self.candidate_path),
            sources=[identity(__file__),identity(HERE/'fd2d_gc_actual_body_reader_factory.py')]+self.parent_metadata['sources'],
            Delta=str(self.mapping.delta),radial_mapping=self.mapping.definition(),
            parent_cylinder_certificate=self.cylinder_certificate,
            mode_count=self.K,node_count=len(self.nodes),parameter_count=self.parameter_count,
            central_parameter_count=self.central_parameter_count,
            tail_parameter_count=self.tail_parameter_count,profile_count=self.profile_count,
            parameter_layout=self.explicit_parameter_layout,
            full_field='Parent complete n,m,l and all jets composed with s+Delta; the radial derivative of this exact shift is 1',
            physical_target=self.profile.definition(),
            physical_metric_changed_from_parent=True,
            parent_layout_coefficients_atlas_lifting_windows_sources_unchanged=True,
            child_coefficient_archive_created=False,
            parent_values_are_not_child_mesh_P1_coefficients=True,
            reference_tail_position_placement='Unchanged parent reference only; the existing one-rigid registration determines the actual new Z',
            exact_upper_body_relation='X_new(s,u)=X_parent(s+Delta,u)-Delta*e_z; F and all angular variations unchanged',
            exact_lower_body_relation='Reflected lower half translated +Delta*e_z',
            true_cuff_height_relation='Z_new=Z_parent-Delta; neither actual Z is claimed paid here',
            inherited_geometry_scope='R168 section8; within halves and pairs involving the retained cylinder inherit parent normal balls',
            unpaid_geometry=['current complete metric posterior','actual cut registration and Z','new whole-core held ball','new smaller origin ball','upper-exterior versus lower-exterior normal balls'],
            body_ODE_run=False,complete_geometry_certified=False)

    @classmethod
    def from_definition(cls,path):
        path=Path(path);meta=json.loads(path.read_text())
        if meta.get('schema')!=SCHEMA:raise ValueError('Wrong explicit shortened-cylinder schema')
        for row in meta['sources']:locate_bound(path,row)
        out=cls(locate_bound(path,meta['parent_native_definition']),meta['Delta'])
        if out.mapping.definition()!=meta['radial_mapping']:
            raise ValueError('The recorded exact shift or numerical knot representatives changed')
        if out.cylinder_certificate!=meta['parent_cylinder_certificate']:
            raise ValueError('The structural parent cylinder identity changed')
        if out.parent_metadata!=meta['parent_complete_definition']:
            raise ValueError('The complete parent definition changed')
        return out


class ShortenedCylinderBodyView:
    def __init__(self,native):self.native=native
    def __getattr__(self,name):return getattr(self.native,name)
    def physical(self,s,u,*,side='right'):return self.native.physical_angular(s,u,side=side)
    @property
    def values(self):
        # Only the frozen generic cut diagnostic uses values[-1]. These are
        # explicitly the parent cut coefficients, not a new child P1 array.
        return self.native.parent.values
    def definition(self):return self.native.definition()
    def body_adapter_definition(self):
        return dict(schema='fd2d-shortened-cylinder-angular-body-view-v1',
            source=identity(__file__),launcher=identity(HERE/'fd2d-shortened-cylinder-body-screen.py'),
            parent_native_definition=identity(self.native.parent_definition_path),
            input_field=identity(self.arrays_path),Delta=str(self.mapping.delta),
            mathematical_definition=SCHEMA,mode_count=self.K,node_count=len(self.nodes),
            parameter_layout=self.explicit_parameter_layout,
            body_physical_dispatch='shortened.physical_angular(s,u,side), which delegates parent.physical_angular(s+Delta,u,side)',
            parent_cut_selected_explicitly=True,radial_cut_II_contract_extended=False,
            legacy_values_property_scope='Parent raw cut-row diagnostic only; never child P1 interpolation',
            original_R124_body_and_R126_cut_formulas_unchanged=True,
            mathematical_metric_changed=True,actual_new_Z_or_held_or_reach_certified=False)


def load_shortened_body_reader(path):
    return ShortenedCylinderBodyView(ShortenedCylinderNativeField.from_definition(path))
