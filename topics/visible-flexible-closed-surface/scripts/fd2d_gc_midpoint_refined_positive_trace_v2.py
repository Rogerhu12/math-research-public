"""R163 v2: same-g P1 subdivision with either explicit saved tail layout.

The real-arithmetic P1 injection preserves the complete field.  The saved
binary64 warm has explicit interpolation/gauge rounding, reported rather
than called exact zero.  All physical parameters, full lifting functions,
atlas and nonlinear window endpoints stay fixed.  Only mesh-dependent
indices and the corresponding finite discretization are rebuilt.
"""
from __future__ import annotations
import copy
from fractions import Fraction as F
import json
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import identity, load_npz
from fd2d_gc_raw_bump_positive_trace import (
    PositiveTraceRawBumpDAE, checkpoint_arrays as original_checkpoint_arrays)

REPRESENTATION = 'ruling_atlas_coast_Gauss_l_and_terminal_positive_trace_v1'
SCHEMA = 'fd2d-saved-P1-midpoint-subdivision-v1'


from fd2d_gc_midpoint_refined_positive_trace import (
    same_bits, decoded, midpoint_refine_arrays, remap_old_cells)
from fd2d_gc_nested_angular_positive_trace import (
    FixedTailDegreePositiveTraceDAE, REPRESENTATION as INDEPENDENT_REPRESENTATION)


class _MidpointRefinementMixin:
    """Original explicit K/tail schema, complete equations, explicit new mesh.

    Constructor creates an independent original problem, verifies all saved
    function identities, then changes only its numerical partition.  It
    never mutates an existing live problem or its source files.
    """
    def __init__(self, source, *, saved_field, split_cells, **kwargs):
        saved = load_npz(saved_field) if isinstance(saved_field,(str,Path)) else saved_field
        kind = str(saved['representation_kind'])
        independent = kind == INDEPENDENT_REPRESENTATION
        if kind not in (REPRESENTATION, INDEPENDENT_REPRESENTATION) or independent != self._independent_tail:
            raise ValueError('Select the class matching the actual saved complete-field schema')
        k, J = int(saved['modes']), int(saved['profile_count'])
        nt = int(saved['tail_parameter_count']) if independent else k+1
        if independent and int(saved['central_parameter_count']) != k:
            raise ValueError('Explicit central/raw angular counts differ')
        if not independent and 'tail_parameter_count' in saved and int(saved['tail_parameter_count']) != nt:
            raise ValueError('Legacy schema must actually have its declared K+1 tail')
        if len(saved['parameters']) != k+nt+J:
            raise ValueError('Do not infer, pad or truncate saved parameter slices')
        if independent:
            if 'tail_parameter_count' in kwargs and int(kwargs['tail_parameter_count']) != nt:
                raise ValueError('Tail count must stay exactly fixed during radial subdivision')
            kwargs['tail_parameter_count'] = nt
        for name, value in dict(modes=k, profile_count=J, supports=saved['profile_supports'],
                base_kind=str(saved['base_kind']), blend=tuple(saved['blend'])).items():
            if name in kwargs and not np.array_equal(np.asarray(kwargs[name]),np.asarray(value)):
                raise ValueError('Constructor would change saved '+name)
            kwargs[name] = value
        atlas = decoded(saved['angular_atlas_definition'])
        for name, value in dict(atlas_entry_start=atlas['entry_transition'][0],
                atlas_exit_stop=atlas['exit_transition'][1],
                minimum_active_n=decoded(saved['gauss_l_definition'])['selected_finite_evaluation_floor']).items():
            if name in kwargs and kwargs[name] != value:
                raise ValueError('Constructor would change saved '+name)
            kwargs[name] = value
        super().__init__(source, **kwargs)
        if str(saved['candidate_sha256']) != identity(source)['sha256']:
            raise ValueError('Different base physical candidate')
        if not same_bits(saved['profile_supports'], self.profile.supports):
            raise ValueError('Different defining radial supports')
        if float(saved['fixed_base_T']) != self.fixed_base_T or str(saved['tail_kind']) != self.tail_kind:
            raise ValueError('Different fixed base T or exact tail family')
        matched = []
        for name in ('seed_weight_definition','angular_atlas_definition',
                     'coast_reference_definition','reference_evaluation_definition'):
            if decoded(saved[name]) != getattr(self,name):
                raise ValueError('Different complete function definition: '+name)
            matched.append(name)
        for name, index in (('gauss_l_definition','inactive_l_raw_nodes'),
                            ('positive_trace_definition','inactive_raw_trace_nodes'),
                            ('central_field_definition','fixed_node_indices')):
            original, generated = decoded(saved[name]), copy.deepcopy(getattr(self,name))
            original.pop(index,None);generated.pop(index,None)
            if original != generated:
                raise ValueError('Different complete function definition outside mesh indices: '+name)
            matched.append(name)
        if independent:
            if decoded(saved['nested_angular_definition']) != self.nested_angular_definition:
                raise ValueError('Changed explicit independent-tail layout definition')
            matched.append('nested_angular_definition')
        old = np.asarray(saved['mesh'],float)
        if old[0] != self.x[0] or old[-1] != self.x[-1] or not np.all(np.isin(self.x,old)):
            raise ValueError('Preserve all original physical/atlas knots and the whole domain')
        self._subdivision_saved = {key:np.array(v,copy=True) for key,v in saved.items()}
        self.x, self._interpolated_y, definition = midpoint_refine_arrays(old,saved['corrections'],split_cells)
        self.N=len(self.x);self.h=np.diff(self.x);self.size=self.N*self.q+self.parameter_count
        self.coords={key:np.asarray(value,float) for key,value in self.chart.coordinates(self.x).items()}
        self.fixed_central_nodes=np.flatnonzero(self.x<=self.profile.central_end)
        self.central_field_definition=decoded(saved['central_field_definition'])
        self.central_field_definition['fixed_node_indices']=self.fixed_central_nodes.tolist()
        self.gauss_l_definition=decoded(saved['gauss_l_definition'])
        self.gauss_plateau=tuple(self.gauss_l_definition['gauss_plateau'])
        self.inactive_l_raw_nodes=np.array([j for j in range(1,self.N-1)
            if self.x[j-1]>=self.gauss_plateau[0] and self.x[j+1]<=self.gauss_plateau[1]],int)
        self.gauss_l_definition['inactive_l_raw_nodes']=self.inactive_l_raw_nodes.tolist()
        self.positive_trace_definition=decoded(saved['positive_trace_definition'])
        # Copy saved scalar window endpoints, never recompute their values.
        self.trace_start=self.positive_trace_definition['start']
        self.trace_ramp_stop=self.positive_trace_definition['ramp_stop']
        self.trace_cut=self.positive_trace_definition['cut']
        self.inactive_trace_nodes=np.array([j for j in range(1,self.N-1)
            if self.x[j-1]>=self.trace_ramp_stop and self.x[j+1]<=self.trace_cut],int)
        self.positive_trace_definition['inactive_raw_trace_nodes']=self.inactive_trace_nodes.tolist()
        self.trace_gauge_pairs=np.array([(j*self.q+r,j*self.q+self.d+r)
            for j in self.inactive_trace_nodes for r in range(self.e)],int).reshape(-1,2)
        inactive=np.array([j*self.q+r for j in self.inactive_l_raw_nodes for r in range(self.d,self.q)],int)
        self.additional_fixed_field_indices=np.unique(np.r_[inactive,self.trace_gauge_pairs[:,1]])
        self.retained_gauss_nodes=np.flatnonzero(self.window()[:-1]!=1.)
        self.retained_actual_gauss_nodes=np.flatnonzero((self.window()[:-1]!=1.)&(self.x[:-1]<self.trace_ramp_stop))
        self.affine_residual_size=self.N*self.q+2*self.K+2
        self.residual_size=(self.N-1)*self.d+len(self.retained_actual_gauss_nodes)*self.e+self.q+2*self.K+2
        self.targeted_mesh_definition=decoded(saved['targeted_mesh_definition'])
        self.targeted_mesh_definition.update(actual_nodes=self.x.tolist(),actual_node_count=self.N,
            further_midpoint_subdivision=True,subdivision_parent_nodes=old.tolist())
        self.atlas_mesh_definition=dict(schema='fd2d-explicit-ruling-atlas-computational-mesh-v1',
            old_nodes=old.tolist(),actual_nodes=self.x.tolist(),
            added_nodes=definition['inserted_coordinates'],old_node_count=len(old),actual_node_count=self.N,
            minimum_cell=float(self.h.min()),all_old_nodes_retained=True,
            physical_metric_changed=False,finite_representation_changed=True)
        self._operator_cache={}
        for name in ('_cell_gauss_view_cache','_chunked_gauss_codazzi_views',
                     '_interior_constraint_point_cache','_positive_known_coast_view'):
            if hasattr(self,name):delattr(self,name)
        definition.update(helper_source=identity(__file__),matched_function_packets=matched,
            original_representation_kind=kind,representation_kind_unchanged=True,
            old_inactive_l_raw_nodes=np.asarray(saved['inactive_l_raw_nodes']).tolist(),
            new_inactive_l_raw_nodes=self.inactive_l_raw_nodes.tolist(),
            old_inactive_trace_nodes=np.asarray(saved['inactive_raw_trace_nodes']).tolist(),
            new_inactive_trace_nodes=self.inactive_trace_nodes.tolist(),
            new_trace_gauge_pairs=self.trace_gauge_pairs.tolist(),
            actual_trace_scalars_copied_from_saved_packet=True,
            new_raw_unknown_count=self.size,new_original_equation_count=self.residual_size,
            tail_parameter_count=nt,physical_parameter_count=self.parameter_count,
            interpolation_helper_source=identity(Path(__file__).with_name('fd2d_gc_midpoint_refined_positive_trace.py')),
            independent_tail_layout_preserved=independent)
        self.radial_refinement_definition=definition

    def inject_saved_field(self, *, canonicalize_redundant=True):
        """Return rounded P1 warm; optionally select the exact null gauges.

        Only entire-hat redundancies are changed. No generic boundary or
        central projection is called. Real-arithmetic full-field invariance
        follows from w=1 on those hats; rounding is explicitly measured.
        """
        y=self._interpolated_y.copy();before=y.copy()
        p=self._subdivision_saved['parameters'].copy()
        gauge_d_error=F(0)
        if canonicalize_redundant:
            y[self.inactive_l_raw_nodes,self.d:]=0.
            for node in self.inactive_trace_nodes:
                for j in range(self.e):
                    n0,l0=float(y[node,j]),float(y[node,self.d+j])
                    d=.5*(n0-l0);y[node,j]=d;y[node,self.d+j]=-d
                    gauge_d_error=max(gauge_d_error,abs(2*F.from_float(d)-(F.from_float(n0)-F.from_float(l0))))
        definition=copy.deepcopy(self.radial_refinement_definition)
        definition.update(canonicalized_entire_hat_redundancies=bool(canonicalize_redundant),
            generic_boundary_reimposition_performed=False,
            maximum_raw_gauge_coefficient_change=float(np.max(np.abs(y-before))),
            maximum_trace_d_coefficient_rounding_exact_upper=str(gauge_d_error),
            physical_parameter_bytes_unchanged=same_bits(p,self._subdivision_saved['parameters']))
        return np.r_[y.ravel(),p],definition



class MidpointRefinedPositiveTraceDAE(_MidpointRefinementMixin, PositiveTraceRawBumpDAE):
    _independent_tail = False


class MidpointRefinedFixedTailDAE(_MidpointRefinementMixin, FixedTailDegreePositiveTraceDAE):
    _independent_tail = True


def create_midpoint_refined_problem(source, *, saved_field, split_cells, **kwargs):
    """Choose only from the explicitly saved original or independent layout.

    To combine R158 and R163, first perform exact angular zero injection on
    the unchanged old mesh, save that independent-tail archive, then pass
    it here. No Fourier or Bernstein transformation occurs in this helper.
    """
    saved=load_npz(saved_field) if isinstance(saved_field,(str,Path)) else saved_field
    kind=str(saved['representation_kind'])
    cls={REPRESENTATION:MidpointRefinedPositiveTraceDAE,
         INDEPENDENT_REPRESENTATION:MidpointRefinedFixedTailDAE}.get(kind)
    if cls is None:raise ValueError('Unsupported explicitly saved positive-trace layout')
    return cls(source,saved_field=saved,split_cells=split_cells,**kwargs)


def checkpoint_arrays(problem, vector, candidate_sha256, *, refinement_definition):
    out=original_checkpoint_arrays(problem,vector,candidate_sha256)
    saved=problem._subdivision_saved
    if problem._independent_tail:
        out['tail_parameter_count']=np.array(problem.tail_parameter_count)
        out['central_parameter_count']=np.array(problem.K)
        out['nested_angular_definition']=np.array(json.dumps(problem.nested_angular_definition,sort_keys=True))
        if 'angular_embedding_definition' in saved:
            out['angular_embedding_definition']=np.array(saved['angular_embedding_definition'],copy=True)
    out['radial_refinement_definition']=np.array(json.dumps(refinement_definition,sort_keys=True))
    if 'finite_interior_rows_definition' in saved:
        old=decoded(saved['finite_interior_rows_definition'])
        new=copy.deepcopy(old)
        new['cells']=remap_old_cells(refinement_definition,old['cells'])
        new.update(parent_selected_cells=old['cells'],
            selection='all refined children of the same explicitly saved old physical intervals',
            finite_discretization_changed=True,previous_finite_residual_preservation_claimed=False)
        out['finite_interior_rows_definition']=np.array(json.dumps(new,sort_keys=True))
        out['parent_finite_interior_rows_definition']=np.array(json.dumps(old,sort_keys=True))
    return out
