"""R163: same-g P1 subdivision with the original positive-trace field schema.

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


def same_bits(a, b):
    a, b = np.asarray(a), np.asarray(b)
    return a.dtype == b.dtype and a.shape == b.shape and a.tobytes() == b.tobytes()


def decoded(a):
    return json.loads(str(a))


def midpoint_refine_arrays(mesh, corrections, split_cells):
    """Preserve every old knot; add only the requested cell midpoints.

    Fractions quantify the actual stored nodal interpolation error relative
    to the old real P1 function at each actual new binary64 coordinate.
    They do not change the saved coefficient format or add a new reader.
    """
    x, y = np.asarray(mesh), np.asarray(corrections)
    cells = np.asarray(sorted(set(int(j) for j in split_cells)), int)
    if x.dtype != np.float64 or y.dtype != np.float64:
        raise ValueError('Expected original binary64 defining arrays')
    if x.ndim != 1 or y.ndim != 2 or len(y) != len(x) or np.any(np.diff(x) <= 0):
        raise ValueError('Expected a strictly ordered mesh and its nodal coefficients')
    if not np.all(np.isfinite(x)) or not np.all(np.isfinite(y)):
        raise FloatingPointError('Nonfinite original defining arrays')
    if not len(cells) or np.any(cells < 0) or np.any(cells >= len(x)-1):
        raise ValueError('Select existing cells by their original zero-based indices')
    mids = x[cells]+.5*(x[cells+1]-x[cells])
    if np.any(mids <= x[cells]) or np.any(mids >= x[cells+1]):
        raise ValueError('This binary64 cell has no distinct represented midpoint')
    xx = np.sort(np.r_[x, mids])
    old_ids = np.searchsorted(xx, x)
    new_ids = np.searchsorted(xx, mids)
    yy = np.empty((len(xx), y.shape[1]), dtype=y.dtype)
    yy[old_ids] = y
    t = (mids-x[cells])/(x[cells+1]-x[cells])
    yy[new_ids] = y[cells]+t[:,None]*(y[cells+1]-y[cells])
    if not same_bits(xx[old_ids], x) or not same_bits(yy[old_ids], y):
        raise AssertionError('Old knots/coefficient bytes changed during interpolation')
    max_error, slope_error, coordinate_error = F(0), F(0), F(0)
    rounding_rows = []
    for j, mid, node in zip(cells, mids, new_ids):
        left, right, actual = map(F.from_float, (float(x[j]), float(x[j+1]), float(mid)))
        alpha = (actual-left)/(right-left)
        ce = abs(actual-(left+right)/2)
        coordinate_error = max(coordinate_error, ce)
        row_error = F(0)
        for k in range(y.shape[1]):
            value = (1-alpha)*F.from_float(float(y[j,k]))+alpha*F.from_float(float(y[j+1,k]))
            row_error = max(row_error, abs(F.from_float(float(yy[node,k]))-value))
        max_error = max(max_error, row_error)
        slope_error = max(slope_error, row_error/min(actual-left, right-actual))
        rounding_rows.append(dict(old_cell=int(j), new_node=int(node), actual_s=float(mid),
            exact_midpoint_coordinate_error=str(ce), actual_interpolation_fraction=str(alpha),
            coefficient_error_exact_upper=str(row_error)))
    maps = []
    for j in range(len(x)-1):
        children = list(range(int(old_ids[j]), int(old_ids[j+1])))
        maps.append(dict(old_cell=j, old_interval=[float(x[j]),float(x[j+1])],
                         new_cells=children, new_cell_range=[children[0], children[-1]+1]))
    definition = dict(schema=SCHEMA, old_mesh=x.tolist(), actual_mesh=xx.tolist(),
        split_old_cells=cells.tolist(), old_node_to_new_node=old_ids.tolist(),
        inserted_node_indices=new_ids.tolist(), inserted_coordinates=mids.tolist(),
        old_cell_to_new_cells=maps, old_node_count=len(x), new_node_count=len(xx),
        all_old_node_bytes_preserved=True, old_raw_bytes_preserved_before_gauge=True,
        real_arithmetic_P1_injection_preserves_complete_function=True,
        saved_binary64_field_is_claimed_exactly_identical=False,
        interpolation_rounding=dict(rows=rounding_rows,
            raw_coefficient_uniform_error_exact_upper=str(max_error),
            raw_coefficient_uniform_error_float=float(max_error),
            raw_coefficient_cell_slope_error_exact_upper=str(slope_error),
            raw_coefficient_cell_slope_error_float=float(slope_error),
            midpoint_coordinate_error_exact_upper=str(coordinate_error)),
        physical_metric_changed=False, full_function_definitions_changed=False,
        Fourier_order_changed=False, tail_degree_changed=False,
        new_finite_equations_and_quadrature=True,
        old_finite_residual_preservation_claimed=False,
        nonlinear_solve_performed=False)
    return xx, yy, definition


def remap_old_cells(definition, old_cells):
    table = definition['old_cell_to_new_cells']
    out = []
    for j in old_cells:
        j = int(j)
        if not 0 <= j < len(table):
            raise ValueError('An old selected cell is outside the saved old mesh')
        out.extend(table[j]['new_cells'])
    return sorted(set(out))


class MidpointRefinedPositiveTraceDAE(PositiveTraceRawBumpDAE):
    """Original K/tail schema, original complete equations, explicit new mesh.

    Constructor creates an independent original problem, verifies all saved
    function identities, then changes only its numerical partition.  It
    never mutates an existing live problem or its source files.
    """
    def __init__(self, source, *, saved_field, split_cells, **kwargs):
        saved = load_npz(saved_field) if isinstance(saved_field,(str,Path)) else saved_field
        if str(saved['representation_kind']) != REPRESENTATION:
            raise ValueError('This thin subclass requires the explicit legacy K+1-tail schema')
        k, J = int(saved['modes']), int(saved['profile_count'])
        if 'tail_parameter_count' in saved and int(saved['tail_parameter_count']) != k+1:
            raise ValueError('Use an explicitly independent-tail refinement adapter for that layout')
        if len(saved['parameters']) != 2*k+1+J:
            raise ValueError('Do not infer or truncate the saved parameter slices')
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
            original_representation_kind=REPRESENTATION,representation_kind_unchanged=True,
            old_inactive_l_raw_nodes=np.asarray(saved['inactive_l_raw_nodes']).tolist(),
            new_inactive_l_raw_nodes=self.inactive_l_raw_nodes.tolist(),
            old_inactive_trace_nodes=np.asarray(saved['inactive_raw_trace_nodes']).tolist(),
            new_inactive_trace_nodes=self.inactive_trace_nodes.tolist(),
            new_trace_gauge_pairs=self.trace_gauge_pairs.tolist(),
            actual_trace_scalars_copied_from_saved_packet=True,
            new_raw_unknown_count=self.size,new_original_equation_count=self.residual_size,
            tail_parameter_count=self.K+1,physical_parameter_count=self.parameter_count)
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


def checkpoint_arrays(problem, vector, candidate_sha256, *, refinement_definition):
    out=original_checkpoint_arrays(problem,vector,candidate_sha256)
    saved=problem._subdivision_saved
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
