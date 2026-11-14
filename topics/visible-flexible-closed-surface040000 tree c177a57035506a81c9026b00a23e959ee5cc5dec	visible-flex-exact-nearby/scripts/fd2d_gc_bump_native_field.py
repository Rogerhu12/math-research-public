"""Actual P1 raw field with explicitly saved physical radial bump parameters.

This is a distinct reader; the frozen coast-T reader is unchanged. Inherited
spatial evaluation and the 24-component fixed-material body equations are the
same proved formulas. Only the explicit target/parameter binding is replaced.
The last parameter is a physical delta, never a coast clock T.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import load_npz
from fd2d_gc_raw_native_field import RawLiftedNativeField, identity, locate_bound
from fd2d_gc_radial_bump_profile import RadialBumpProfile
from fd2d_gc_design_profile_positive import PositiveCoastDesignProfile
from fd2d_balanced_curvature_core import FixedBalancedGeometry, BalancedCurvatureCore
from fd2d_positive_flat_developable_family import PositiveFlatDevelopableFamily

SCHEMA = 'fd2d-raw-physical-bump-piecewise-linear-exact-lifting-v1'
HERE = Path(__file__).resolve().parent


def _explicit(saved, key, supplied, *, dtype=None):
    """Resolve an explicitly saved or caller-bound value, without inference."""
    have = saved.get(key)
    if supplied is None:
        if have is None:
            raise ValueError('Missing explicit physical-bump field setting: '+key)
        value = have
    else:
        value = supplied
        if have is not None and not np.array_equal(np.asarray(have), np.asarray(value)):
            raise ValueError('Caller setting differs from the actual field: '+key)
    return np.asarray(value, dtype=dtype) if dtype is not None else value


class RawBumpNativeField(RawLiftedNativeField):
    def __init__(self, arrays, candidate, *, blend_interval=None,
                 profile_supports=None, fixed_base_T=None, base_kind=None,
                 tail_kind=None, candidate_sha256=None, collar_guard=.02,
                 geometry=None):
        # Do not call the old constructor with a fabricated final T value.
        # The actual archive and all its parameters remain unchanged.
        self.arrays_path, self.candidate_path = Path(arrays), Path(candidate)
        data = load_npz(arrays)
        self.nodes, self.values, self.parameters = (data[key] for key in ('mesh', 'corrections', 'parameters'))
        if not all(q.dtype == np.float64 and np.all(np.isfinite(q))
                   for q in (self.nodes, self.values, self.parameters)):
            raise ValueError('Defining arrays must be finite binary64')
        if self.nodes.ndim != 1 or len(self.nodes) < 2 or np.any(np.diff(self.nodes) <= 0):
            raise ValueError('Actual radial nodes must be strictly increasing')
        if self.values.ndim != 2 or self.values.shape[0] != len(self.nodes):
            raise ValueError('Actual correction array must be (nodes,3K+2)')
        self.K = (self.values.shape[1]-2)//3
        self.e, self.d = self.K+1, 2*self.K+1
        if self.K < 1 or self.values.shape[1] != 3*self.K+2:
            raise ValueError('Inconsistent actual Fourier dimensions')
        kind = str(_explicit(data, 'profile_kind', 'physical_bumps'))
        if kind != 'physical_bumps':
            raise ValueError('This reader requires the explicit physical-bump definition')
        self.profile_kind = kind
        self.base_kind = str(_explicit(data, 'base_kind', base_kind))
        self.tail_kind = str(_explicit(data, 'tail_kind', tail_kind))
        if self.base_kind not in ('balanced_seed', 'circle') or self.tail_kind != 'positive_bernstein':
            raise ValueError('Unsupported explicit central/tail family')
        supports = _explicit(data, 'profile_supports', profile_supports, dtype=float)
        if supports.ndim != 2 or supports.shape[1] != 2 or not len(supports):
            raise ValueError('The actual physical support array must be J by 2')
        self.profile_count = len(supports)
        if 'profile_count' in data and int(data['profile_count']) != self.profile_count:
            raise ValueError('Recorded physical-profile count differs from supports')
        if self.parameters.shape != (2*self.K+1+self.profile_count,):
            raise ValueError('Expected [central K, tail K+1, physical delta J]')
        self.central_slice = slice(0, self.K)
        self.tail_parameter_slice = slice(self.K, 2*self.K+1)
        self.profile_parameter_slice = slice(2*self.K+1, len(self.parameters))
        self.fixed_base_T = float(_explicit(data, 'fixed_base_T', fixed_base_T))
        bound_sha = str(_explicit(data, 'candidate_sha256', candidate_sha256))
        if identity(candidate)['sha256'] != bound_sha:
            raise ValueError('Candidate bytes differ from this actual field')
        # The base candidate's coast has a fixed label only. This comparison
        # verifies it; the actual radial target below is the direct base plus
        # its saved bumps, with no coast coordinate map applied.
        base_label = PositiveCoastDesignProfile(candidate).reference_T
        if self.fixed_base_T != base_label:
            raise ValueError('Saved fixed base coast T differs from the supplied candidate')
        self.profile = RadialBumpProfile(candidate, supports=supports,
            collar_guard=collar_guard, coefficients=self.parameters[self.profile_parameter_slice])
        self.geometry = FixedBalancedGeometry() if geometry is None else geometry
        self.core = BalancedCurvatureCore(self.parameters[self.central_slice],
            base_kind=self.base_kind, geometry=self.geometry)
        self.tail = PositiveFlatDevelopableFamily(self.parameters[self.tail_parameter_slice],
            cut_radius=.8, cuff_radius=.32, flat_radius=.34, plane_height=1.25)
        blend = _explicit(data, 'blend', blend_interval, dtype=float)
        if blend.shape != (2,):
            raise ValueError('The actual fixed-physical-s angular blend needs two endpoints')
        self.blend_interval = tuple(float(q) for q in blend)
        if not 0 <= blend[0] < blend[1] <= self.profile.end:
            raise ValueError('Actual angular blend lies outside the fixed physical domain')
        if self.nodes[0] != 0. or abs(self.nodes[-1]-self.profile.end) > 1e-12:
            raise ValueError('Actual arrays do not cover this fixed physical radial domain')
        self.frequencies = 2*np.arange(self.K+1, dtype=float)
        self._inverse_seed_cache = {}
        for q in (self.nodes, self.values, self.parameters):
            q.flags.writeable = False

    @classmethod
    def from_definition(cls, path):
        path = Path(path)
        meta = json.loads(path.read_text())
        if meta['schema'] != SCHEMA:
            raise ValueError('Wrong physical-bump native definition schema')
        for row in meta['sources']:
            locate_bound(path, row)
        geometry = FixedBalancedGeometry(moments=locate_bound(path, meta['moments']),
                                         means=locate_bound(path, meta['means']))
        return cls(locate_bound(path, meta['arrays']), locate_bound(path, meta['candidate_input']),
            blend_interval=meta['blend_interval'], profile_supports=meta['profile_supports'],
            fixed_base_T=meta['fixed_base_T'], base_kind=meta['base_kind'],
            tail_kind=meta['tail_kind'], candidate_sha256=meta['candidate_input']['sha256'],
            collar_guard=meta['collar_guard'], geometry=geometry)

    def definition(self):
        files = ['fd2d_gc_bump_native_field.py', 'fd2d_gc_raw_native_field.py',
            'fd2d_gc_archive_arrays.py', 'fd2d_gc_radial_bump_profile.py',
            'fd2d_gc_three_field_residual.py', 'fd2d_frozen_ellipse_candidate.py',
            'fd2d_balanced_curvature_core.py', 'fd2d_positive_flat_developable_family.py',
            'fd2d_gc_design_profile_positive.py']
        layout = dict(central=[0, self.K], tail=[self.K, 2*self.K+1],
                      physical_profile=[2*self.K+1, len(self.parameters)])
        return dict(schema=SCHEMA, arrays=identity(self.arrays_path),
            candidate_input=identity(self.candidate_path), sources=[identity(HERE/f) for f in files],
            moments=identity(self.geometry.moments_path), means=identity(self.geometry.means_path),
            profile_kind=self.profile_kind, tail_kind=self.tail_kind, base_kind=self.base_kind,
            node_count=len(self.nodes), mode_count=self.K, profile_count=self.profile_count,
            profile_supports=self.profile.supports.tolist(), fixed_base_T=self.fixed_base_T,
            collar_guard=self.profile.collar_guard, parameter_layout=layout,
            parameters_order='[central K, positive tail K+1, physical radial delta J]; no variable T',
            physical_deltas=self.parameters[self.profile_parameter_slice].tolist(),
            correction_order='[n_0,n_2,...,n_2K,m_2,...,m_2K,l_0,l_2,...,l_2K]',
            radial_interpolation='Exact continuous P1 binary-node corrections in physical s=x',
            node_derivative='One-sided cell slope; side affects no value or angular derivative',
            independent_l_saved=True, no_shape_denominator=True,
            cut_correction_exactly_zero=bool(np.all(self.values[-1] == 0.)),
            cut_correction_absolute_max=float(np.max(abs(self.values[-1]))),
            central_l_correction_exactly_zero=bool(np.all(self.values[0, self.d:] == 0.)),
            central_m_correction_exactly_zero=bool(np.all(self.values[0, self.e:self.d] == 0.)),
            physical_profile=self.profile.definition(), blend_interval=list(self.blend_interval),
            angular_chart='u=(1-beta(s))*U_seed(xi)+beta(s)*xi; fixed across delta',
            central_definition=self.core.definition(),
            lifting=dict(component_order=['n', 'm', 'l'], tail_start_fraction=.42,
                tail_end='fixed physical endpoint', seed_end='min(.55,.4*physical endpoint)',
                radial_weights='quintic steps; complete central and tail functions, no angular truncation'),
            actual_map='R119/R124 fixed physical u; F_s=F*A, X_s=F*e1; 24 body/angle-variation components',
            field_evaluation_is_floating=True, full_residual_certified=False,
            closed_surface=False, physical_g_changes_with_delta=True)
