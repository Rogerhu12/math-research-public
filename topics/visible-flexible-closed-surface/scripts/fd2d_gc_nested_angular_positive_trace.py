"""R158 exact angular nesting with an independent fixed tail degree.

Only raw Fourier and central curvature modes are enlarged.  The tail
Bernstein controls are copied unchanged, never degree-elevated or rounded.
The existing physical-bump, complete lifting, atlas and R153/R155 function
definitions remain the same.  More angular test rows/samples do not imply
that a finite residual stays numerically unchanged.
"""
from __future__ import annotations
import json
import numpy as np
from fd2d_gc_archive_arrays import identity
from fd2d_gc_raw_bump_positive_trace import PositiveTraceRawBumpDAE, checkpoint_arrays as original_checkpoint_arrays

SCHEMA = 'fd2d-independent-tail-angular-nesting-v1'
REPRESENTATION = 'ruling_atlas_coast_Gauss_l_terminal_positive_trace_fixed_tail_degree_v1'
LEGACY_REPRESENTATION = 'ruling_atlas_coast_Gauss_l_and_terminal_positive_trace_v1'


def _same_bits(a, b):
    a, b = np.asarray(a), np.asarray(b)
    return a.dtype == b.dtype and a.shape == b.shape and a.tobytes() == b.tobytes()


def zero_extend_angular_arrays(corrections, parameters, *, old_modes, new_modes,
                               tail_parameter_count, profile_count):
    """Exact array injection; no projection, interpolation or boundary reset."""
    k, kk, nt, npf = map(int, (old_modes, new_modes, tail_parameter_count, profile_count))
    y, p = np.asarray(corrections), np.asarray(parameters)
    if min(k, nt, npf) < 1 or kk <= k:
        raise ValueError('Use positive counts and a strict angular enlargement')
    if y.dtype != np.float64 or p.dtype != np.float64:
        raise ValueError('Preserve explicit binary64 defining coefficients')
    if y.ndim != 2 or y.shape[1] != 3*k+2 or p.shape != (k+nt+npf,):
        raise ValueError('Wrong explicitly declared independent parameter layout')
    if not np.all(np.isfinite(y)) or not np.all(np.isfinite(p)):
        raise FloatingPointError('Nonfinite defining arrays')
    z = np.zeros((len(y), 3*kk+2), np.float64)
    z[:, :k+1] = y[:, :k+1]
    z[:, kk+1:kk+1+k] = y[:, k+1:2*k+1]
    z[:, 2*kk+1:2*kk+k+2] = y[:, 2*k+1:]
    q = np.zeros(kk+nt+npf, np.float64)
    q[:k] = p[:k]
    q[kk:kk+nt] = p[k:k+nt]
    q[kk+nt:] = p[k+nt:]
    copied = [_same_bits(z[:,:k+1],y[:,:k+1]),
        _same_bits(z[:,kk+1:kk+1+k],y[:,k+1:2*k+1]),
        _same_bits(z[:,2*kk+1:2*kk+k+2],y[:,2*k+1:]),
        _same_bits(q[:k],p[:k]),_same_bits(q[kk:kk+nt],p[k:k+nt]),
        _same_bits(q[kk+nt:],p[k+nt:])]
    if not all(copied):
        raise AssertionError('A defining coefficient changed during copy')
    definition = dict(schema=SCHEMA, old_modes=k, new_modes=kk,
        old_maximum_physical_frequency=2*k,new_maximum_physical_frequency=2*kk,
        central_parameter_count=kk, tail_parameter_count=nt, tail_bernstein_degree=nt-1,
        profile_parameter_count=npf, tail_controls_bitwise_unchanged=True,
        profile_deltas_bitwise_unchanged=True, old_central_coefficients_bitwise_unchanged=True,
        old_raw_coefficients_bitwise_unchanged=True,
        added_raw_and_central_coefficients='exact positive binary zero',
        Fourier_projection_performed=False, radial_interpolation_performed=False,
        boundary_values_reimposed=False, Bernstein_degree_elevation_performed=False,
        mathematical_complete_field_preserved=True,
        mathematical_metric_preserved=True,
        finite_residual_preservation_claimed=False,
        old_parameter_layout=dict(central=[0,k],tail=[k,k+nt],physical_profile=[k+nt,k+nt+npf]),
        new_parameter_layout=dict(central=[0,kk],tail=[kk,kk+nt],physical_profile=[kk+nt,kk+nt+npf]))
    return z, q, definition


class FixedTailDegreePositiveTraceDAE(PositiveTraceRawBumpDAE):
    """Same equations, separately sized central/raw and tail spaces."""
    def __init__(self, *args, tail_parameter_count=16, **kwargs):
        nt = int(tail_parameter_count)
        if nt != tail_parameter_count or nt < 1:
            raise ValueError('Tail parameter count must be a positive integer')
        super().__init__(*args, **kwargs)
        self.tail_parameter_count = nt
        self.central_slice = slice(0, self.K)
        self.tail_slice = slice(self.K, self.K+nt)
        self.profile_slice = slice(self.K+nt, self.K+nt+self.J)
        self.tail_parameter_slice, self.profile_parameter_slice = self.tail_slice, self.profile_slice
        self.parameter_count = self.K+nt+self.J
        self.size = self.N*self.q+self.parameter_count
        # Residual rows are physical Fourier/boundary conditions. They do
        # not acquire rows merely because the parameter count changed.
        self._operator_cache = {}
        self._cell_gauss_view_cache = None
        self._chunked_gauss_codazzi_views = None
        self.nested_angular_definition = dict(schema=SCHEMA,
            provider_source_sha256=identity(__file__)['sha256'],
            inherited_provider_source_sha256=identity(__import__('fd2d_gc_raw_bump_positive_trace').__file__)['sha256'],
            angular_mode_count=self.K, central_parameter_count=self.K,
            tail_parameter_count=nt, tail_bernstein_degree=nt-1,
            physical_profile_parameter_count=self.J,
            layout=dict(central=[0,self.K],tail=[self.K,self.K+nt],
                        physical_profile=[self.K+nt,self.parameter_count]),
            inherited_full_function_definitions_unchanged=True,
            parameter_count_independent_of_equation_count=True,
            old_native_K_plus_one_tail_decoder_permitted=False)
        self.representation_kind = REPRESENTATION

    def parameter_layout(self):
        out = super().parameter_layout()
        out['nested_angular_definition'] = self.nested_angular_definition
        out['tail_parameter_count'] = self.tail_parameter_count
        return out

    def inject_saved_field(self, saved):
        """Bind an old actual field, then inject its coefficients unchanged."""
        old_kind = str(saved.get('representation_kind',''))
        if old_kind not in (LEGACY_REPRESENTATION, REPRESENTATION):
            raise ValueError('Explicit complete positive-trace input required')
        old_k = int(saved['modes'])
        old_nt = int(saved['tail_parameter_count']) if 'tail_parameter_count' in saved else old_k+1
        if old_nt != self.tail_parameter_count:
            raise ValueError('Tail degree must stay exactly fixed')
        if str(saved['candidate_sha256']) != identity(self.source)['sha256']:
            raise ValueError('Different physical base candidate')
        if not _same_bits(saved['mesh'], self.x):
            raise ValueError('The actual radial mesh must be preserved, not regenerated approximately')
        if not _same_bits(saved['profile_supports'], self.profile.supports):
            raise ValueError('Different actual radial-bump supports')
        if float(saved['fixed_base_T']) != self.fixed_base_T:
            raise ValueError('Different fixed physical base coast')
        if str(saved['base_kind']) != self.base_kind or str(saved['tail_kind']) != self.tail_kind:
            raise ValueError('Different exact central or tail family')
        matched = []
        for name in ('seed_weight_definition','angular_atlas_definition',
                'coast_reference_definition','reference_evaluation_definition',
                'gauss_l_definition','positive_trace_definition'):
            if name not in saved or json.loads(str(saved[name])) != getattr(self,name):
                raise ValueError('Different complete function definition: '+name)
            matched.append(name)
        z,q,definition = zero_extend_angular_arrays(saved['corrections'],saved['parameters'],
            old_modes=old_k,new_modes=self.K,tail_parameter_count=old_nt,profile_count=self.J)
        definition.update(preserved_definition_packets=matched,actual_radial_mesh_bitwise_unchanged=True,
            actual_profile_supports_bitwise_unchanged=True,
            complete_field_preservation='Raw/central exact zero injection, same finite degree tail, same metric/atlas/full lifting, then the same pointwise nonlinear maps')
        return np.r_[z.ravel(),q], definition


def checkpoint_arrays(problem, vector, candidate_sha256, *, embedding_definition=None):
    out = original_checkpoint_arrays(problem, vector, candidate_sha256)
    out['tail_parameter_count'] = np.array(problem.tail_parameter_count)
    out['central_parameter_count'] = np.array(problem.K)
    out['nested_angular_definition'] = np.array(json.dumps(problem.nested_angular_definition,sort_keys=True))
    if embedding_definition is not None:
        out['angular_embedding_definition'] = np.array(json.dumps(embedding_definition,sort_keys=True))
    return out
