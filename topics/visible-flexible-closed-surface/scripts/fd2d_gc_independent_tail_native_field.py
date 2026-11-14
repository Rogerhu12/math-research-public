"""R158 native reader with independent central/raw and finite tail counts.

No legacy K+1 tail decoder is called. The actual archive is read unchanged
with its explicit layout. Existing R149/R153/R155 evaluation methods are
inherited, including the limited exact-cut angular trace contract. This
reader supports subsequent nonzero high coefficients as well as the saved
zero injection; embedding metadata alone is never a same-field proof.
"""
from __future__ import annotations
import copy
import json
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from fd2d_gc_archive_arrays import load_npz
from fd2d_gc_raw_native_field import identity, locate_bound
from fd2d_gc_bump_native_field import _explicit
from fd2d_gc_bump_seed_native_field import seed_definition
from fd2d_gc_bump_coast_native_field import decoded_definition, expected_coast_definition, window
from fd2d_gc_frozen_coast_reference import FrozenCoastReference
from fd2d_gc_frozen_coast_second_jets import FrozenCoastSecondJets
from fd2d_gc_raw_lifted_dae import CertifiedReference
from fd2d_gc_blended import BlendedIntrinsicGC
from fd2d_gc_frozen_ruling_atlas import FrozenRulingAtlas
from fd2d_gc_radial_bump_profile import RadialBumpProfile
from fd2d_gc_design_profile_positive import PositiveCoastDesignProfile
from fd2d_balanced_curvature_core import FixedBalancedGeometry, BalancedCurvatureCore
from fd2d_positive_flat_developable_family import PositiveFlatDevelopableFamily
from fd2d_gc_positive_trace_native_field_v2 import PositiveTraceNativeField, _declared

HERE = Path(__file__).resolve().parent
SCHEMA = 'fd2d-independent-tail-coast-Gauss-terminal-trace-native-v1'
REPRESENTATION = 'ruling_atlas_coast_Gauss_l_terminal_positive_trace_fixed_tail_degree_v1'
LAYOUT_SCHEMA = 'fd2d-independent-tail-angular-nesting-v1'


def _count(saved, key, supplied=None):
    value = np.asarray(_explicit(saved, key, supplied))
    if value.ndim != 0 or value.dtype.kind not in 'iu' or int(value) < 1:
        raise ValueError('Explicit layout counts must be positive scalar integers: '+key)
    return int(value)


class IndependentTailPositiveTraceNativeField(PositiveTraceNativeField):
    def __init__(self, arrays, candidate, *, reference_inlet, reference_cache=None,
            central_parameter_count=None, tail_parameter_count=None, profile_count=None,
            nested_angular_definition=None, angular_atlas_definition=None,
            coast_reference_definition=None, gauss_l_definition=None,
            positive_trace_definition=None, seed_weight_definition=None,
            representation_kind=None, blend_interval=None, profile_supports=None,
            fixed_base_T=None, base_kind=None, tail_kind=None, candidate_sha256=None,
            collar_guard=.02, geometry=None):
        # This is the only archive decoder. None of the legacy constructors
        # is invoked and no padded, truncated or synthetic parameter archive
        # is created to pass an old dimension check.
        saved = load_npz(arrays)
        self.arrays_path, self.candidate_path = Path(arrays), Path(candidate)
        self.nodes, self.values, self.parameters = (saved[key] for key in ('mesh','corrections','parameters'))
        if not all(v.dtype == np.float64 and np.all(np.isfinite(v))
                   for v in (self.nodes, self.values, self.parameters)):
            raise ValueError('Actual defining arrays must be finite binary64')
        if self.nodes.ndim != 1 or len(self.nodes) < 2 or np.any(np.diff(self.nodes) <= 0):
            raise ValueError('The actual P1 mesh must be strictly increasing')
        if self.values.ndim != 2 or len(self.values) != len(self.nodes):
            raise ValueError('Actual correction array must have one row per saved node')
        self.K = _count(saved, 'modes')
        nc = _count(saved, 'central_parameter_count', central_parameter_count)
        nt = _count(saved, 'tail_parameter_count', tail_parameter_count)
        npf = _count(saved, 'profile_count', profile_count)
        if min(self.K, nc, nt, npf) < 1 or nc != self.K or self.values.shape[1] != 3*self.K+2:
            raise ValueError('Explicit central/raw dimensions disagree')
        self.e, self.d = self.K+1, 2*self.K+1
        self.central_parameter_count, self.tail_parameter_count, self.profile_count = nc, nt, npf
        self.parameter_count = nc+nt+npf
        if self.parameters.shape != (self.parameter_count,):
            raise ValueError('Expected exactly [declared central, declared fixed tail, declared physical profile]')
        self.central_slice = slice(0, nc)
        self.tail_parameter_slice = slice(nc, nc+nt)
        self.profile_parameter_slice = slice(nc+nt, self.parameter_count)
        layout = dict(central=[0,nc], tail=[nc,nc+nt], physical_profile=[nc+nt,self.parameter_count])
        self.explicit_parameter_layout = layout
        self.representation_kind = str(_explicit(saved, 'representation_kind', representation_kind))
        if self.representation_kind != REPRESENTATION:
            raise ValueError('This reader requires the explicit independent-tail complete-field kind')
        nested = _declared(saved, 'nested_angular_definition', nested_angular_definition)
        expected = dict(schema=LAYOUT_SCHEMA, angular_mode_count=self.K,
            central_parameter_count=nc, tail_parameter_count=nt, tail_bernstein_degree=nt-1,
            physical_profile_parameter_count=npf, layout=layout,
            inherited_full_function_definitions_unchanged=True,
            parameter_count_independent_of_equation_count=True,
            old_native_K_plus_one_tail_decoder_permitted=False,
            provider_source_sha256=identity(HERE/'fd2d_gc_nested_angular_positive_trace.py')['sha256'],
            inherited_provider_source_sha256=identity(HERE/'fd2d_gc_raw_bump_positive_trace.py')['sha256'])
        for key, value in expected.items():
            if nested.get(key) != value:
                raise ValueError('Different saved independent layout or defining source: '+key)
        self.nested_angular_definition = nested
        self.angular_embedding_definition = (None if 'angular_embedding_definition' not in saved
            else decoded_definition(saved['angular_embedding_definition']))
        if self.angular_embedding_definition is not None:
            emb = self.angular_embedding_definition
            if (emb.get('schema') != LAYOUT_SCHEMA or emb.get('new_modes') != self.K
                    or emb.get('tail_parameter_count') != nt or emb.get('profile_parameter_count') != npf
                    or emb.get('new_parameter_layout') != layout):
                raise ValueError('Embedding provenance has a different declared target layout')
        self.profile_kind = str(_explicit(saved, 'profile_kind', 'physical_bumps'))
        self.base_kind = str(_explicit(saved, 'base_kind', base_kind))
        self.tail_kind = str(_explicit(saved, 'tail_kind', tail_kind))
        if (self.base_kind not in ('balanced_seed','circle') or self.tail_kind != 'positive_bernstein'
                or self.profile_kind != 'physical_bumps'):
            raise ValueError('Unsupported actual physical/central/tail family')
        supports = _explicit(saved, 'profile_supports', profile_supports, dtype=float)
        if supports.shape != (npf,2) or not np.all(np.isfinite(supports)):
            raise ValueError('Explicit physical profile count differs from actual supports')
        self.fixed_base_T = float(_explicit(saved, 'fixed_base_T', fixed_base_T))
        bound_sha = str(_explicit(saved, 'candidate_sha256', candidate_sha256))
        if identity(candidate)['sha256'] != bound_sha:
            raise ValueError('Actual candidate bytes do not match the saved field')
        if self.fixed_base_T != PositiveCoastDesignProfile(candidate).reference_T:
            raise ValueError('Actual fixed base coast label differs from the candidate')
        self.profile = RadialBumpProfile(candidate, supports=supports, collar_guard=collar_guard,
            coefficients=self.parameters[self.profile_parameter_slice])
        self.geometry = FixedBalancedGeometry() if geometry is None else geometry
        self.core = BalancedCurvatureCore(self.parameters[self.central_slice],
            base_kind=self.base_kind, geometry=self.geometry)
        self.tail = PositiveFlatDevelopableFamily(self.parameters[self.tail_parameter_slice],
            cut_radius=.8, cuff_radius=.32, flat_radius=.34, plane_height=1.25)
        blend = _explicit(saved, 'blend', blend_interval, dtype=float)
        if blend.shape != (2,) or not 0 <= blend[0] < blend[1] <= self.profile.end:
            raise ValueError('Actual fixed physical blend lies outside the domain')
        self.blend_interval = tuple(float(v) for v in blend)
        if self.nodes[0] != 0. or abs(self.nodes[-1]-self.profile.end) > 1e-12:
            raise ValueError('Saved arrays do not cover the bound physical radial interval')
        self.frequencies = 2*np.arange(self.K+1, dtype=float)
        self._inverse_seed_cache = {}
        seed = seed_definition(_declared(saved, 'seed_weight_definition', seed_weight_definition))
        if seed['end'] > self.profile.end:
            raise ValueError('Explicit seed window lies outside the physical interval')
        self.seed_weight_definition = seed
        for a in (self.nodes, self.values, self.parameters):
            a.flags.writeable = False
        # Validation-only bootstraps below are copied from the frozen
        # readers. Their complete mathematical evaluation methods are
        # inherited verbatim, rather than copied or re-derived here.
        coast_definition = _declared(saved, 'coast_reference_definition', coast_reference_definition)
        _bind_coast(self, reference_inlet, reference_cache, coast_definition)
        atlas_definition = _declared(saved, 'angular_atlas_definition', angular_atlas_definition)
        _bind_atlas(self, saved, atlas_definition, reference_inlet)
        coast = _declared(saved, 'gauss_l_definition', gauss_l_definition)
        terminal = _declared(saved, 'positive_trace_definition', positive_trace_definition)
        _bind_nonlinear_definitions(self, saved, coast, terminal)
        expected_pairs = np.array([(j*(3*self.K+2)+k,j*(3*self.K+2)+self.d+k)
            for j in terminal['inactive_raw_trace_nodes'] for k in range(self.e)],int).reshape(-1,2)
        if 'trace_gauge_pairs' in saved and not np.array_equal(saved['trace_gauge_pairs'],expected_pairs):
            raise ValueError('Trace gauge uses different raw angular column indices')
        if ('inactive_raw_trace_nodes' in saved and not np.array_equal(
                saved['inactive_raw_trace_nodes'],terminal['inactive_raw_trace_nodes'])):
            raise ValueError('Saved terminal inactive nodes disagree with their actual definition')
        self.trace_gauge_pairs = expected_pairs

    def definition(self):
        # Existing evaluators produce their complete mathematical metadata;
        # explicitly replace the legacy descriptive layout, never the arrays.
        meta = PositiveTraceNativeField.definition(self)
        meta['schema'] = SCHEMA
        meta['sources'] = [identity(HERE/name) for name in (
            'fd2d_gc_independent_tail_native_field.py',
            'fd2d_gc_nested_angular_positive_trace.py')]+meta['sources']
        meta['parameter_layout'] = self.explicit_parameter_layout
        meta['parameters_order'] = '[declared central K, declared independent positive-tail count, declared physical profile count]; no variable T'
        meta['central_parameter_count'] = self.central_parameter_count
        meta['tail_parameter_count'] = self.tail_parameter_count
        meta['profile_count'] = self.profile_count
        meta['parameter_count'] = self.parameter_count
        meta['nested_angular_definition'] = self.nested_angular_definition
        meta['angular_embedding_definition'] = self.angular_embedding_definition
        meta['embedding_is_provenance_not_current_coefficient_equality_proof'] = True
        meta['legacy_K_plus_one_decoder_invoked'] = False
        meta['parameter_archive_padded_or_truncated'] = False
        meta['trace_gauge_pairs'] = self.trace_gauge_pairs.tolist()
        meta['independent_layout_scope'] = 'Any finite actual coefficients with this exact declared layout and unchanged full function definitions; not limited to zero padding'
        return meta

    @classmethod
    def from_definition(cls, path):
        path = Path(path); meta = json.loads(path.read_text())
        if meta['schema'] != SCHEMA:
            raise ValueError('Wrong independent-tail native definition schema')
        for row in meta['sources']:
            locate_bound(path,row)
        geometry = FixedBalancedGeometry(moments=locate_bound(path,meta['moments']),
            means=locate_bound(path,meta['means']))
        cache = meta.get('reference_cache_input')
        return cls(locate_bound(path,meta['arrays']),locate_bound(path,meta['candidate_input']),
            reference_inlet=locate_bound(path,meta['reference_inlet_input']),
            reference_cache=None if cache is None else locate_bound(path,cache),
            central_parameter_count=meta['central_parameter_count'],
            tail_parameter_count=meta['tail_parameter_count'],profile_count=meta['profile_count'],
            nested_angular_definition=meta['nested_angular_definition'],
            angular_atlas_definition=meta['angular_atlas_definition'],
            coast_reference_definition=meta['coast_reference_definition'],
            gauss_l_definition=meta['gauss_l_definition'],
            positive_trace_definition=meta['positive_trace_definition'],
            seed_weight_definition=meta['seed_weight_definition'],representation_kind=meta['representation_kind'],
            blend_interval=meta['blend_interval'],profile_supports=meta['profile_supports'],
            fixed_base_T=meta['fixed_base_T'],base_kind=meta['base_kind'],tail_kind=meta['tail_kind'],
            candidate_sha256=meta['candidate_input']['sha256'],collar_guard=meta['collar_guard'],geometry=geometry)


def _bind_coast(self, reference_inlet, reference_cache, definition):
    self.reference_inlet_path = Path(reference_inlet)
    self.reference_cache_path = None if reference_cache is None else Path(reference_cache)
    self.coast_reference = FrozenCoastReference(reference_inlet, cache_path=reference_cache)
    self.coast_second_jets = FrozenCoastSecondJets(self.coast_reference)
    ref = self.coast_reference
    if ref.candidate_sha256 != identity(self.candidate_path)['sha256']:
        raise ValueError('The frozen reference is not for this bound base candidate')
    for name in ('moments_path', 'means_path'):
        if identity(getattr(self.geometry, name))['sha256'] != identity(getattr(ref.geometry, name))['sha256']:
            raise ValueError('Field and frozen reference must use the identical seed chart')
    if ref.entry_s < self.profile.central_end or ref.exit_s >= self.profile.end:
        raise ValueError('The reference window must avoid the central cylinder and cut')
    fraction = float(definition['rim_fraction'])
    expected = expected_coast_definition(ref, fraction)
    # Extra provenance may be retained, but every defining field is
    # checked. Dynamic cache statistics and paths are not substituted
    # for the immutable reference binding.
    for key, value in expected.items():
        if key not in definition or definition[key] != value:
            raise ValueError('Unsupported or changed actual coast definition: '+key)
    self.coast_reference_definition = definition
    self.reference_rim_fraction = fraction
    window(self.nodes, ref.entry_s, ref.length, fraction)
    # A lightweight view evaluates the old full lifting with zero
    # correction. It is only an evaluation device; the actual archived
    # arrays stay immutable and are never rewritten as a zero field.
    self._plain_lifting_view = copy.copy(self)
    self._plain_lifting_view.values = np.zeros_like(self.values)
    self._plain_lifting_view.values.flags.writeable = False


def _bind_atlas(self, saved, declared, reference_inlet):
    # This object only evaluates an angular coordinate function. No
    # intrinsic ODE, BVP operator or new unknown mesh is constructed.
    original = BlendedIntrinsicGC(SimpleNamespace(end=float(self.profile.end)),
        maximum_mode=2*self.K+1, oversample=4,
        reference=CertifiedReference(self.geometry), blend_interval=self.blend_interval)
    self.angular_atlas = FrozenRulingAtlas(original, reference_inlet,
        entry_start=float(declared['entry_transition'][0]),
        exit_stop=float(declared['exit_transition'][1]))
    if self.angular_atlas.chart_definition() != declared:
        raise ValueError('The saved atlas input/source/formula does not match this evaluator')
    if self.angular_atlas.ruling.base.candidate_sha256 != self.coast_reference.candidate_sha256:
        raise ValueError('Atlas and frozen lifting use different base candidates')
    self.angular_atlas_definition = declared
    if 'atlas_mesh_definition' not in saved or 'reference_evaluation_definition' not in saved:
        raise ValueError('Save both the actual atlas mesh and direct-label evaluation identities')
    self.atlas_mesh_definition = decoded_definition(saved['atlas_mesh_definition'])
    if self.atlas_mesh_definition.get('actual_nodes') != self.nodes.tolist():
        raise ValueError('Declared atlas mesh differs from the actual defining P1 array')
    self.reference_evaluation_definition = decoded_definition(saved['reference_evaluation_definition'])
    evaluation = self.reference_evaluation_definition
    if (evaluation.get('schema') != 'fd2d-known-ruling-label-fixed-reference-evaluation-v1'
            or evaluation.get('physical_reference_binding_sha256') != self.coast_reference.binding_sha256
            or evaluation.get('angular_atlas_source_sha256') != declared['source_sha256']
            or evaluation.get('source_sha256') != identity(HERE/'fd2d_gc_raw_bump_ruling_atlas.py')['sha256']
            or evaluation.get('physical_function_changed') is not False
            or evaluation.get('unknown_raw_n_divided') is not False):
        raise ValueError('Changed or unsupported checkpoint reference-evaluation identity')
    self.finite_radial_scheme = str(saved.get('finite_radial_scheme', 'explicitly absent'))
    self._chart_side = 'coast'
    self._plain_lifting_view.angular_atlas = self.angular_atlas
    self._plain_lifting_view.angular_atlas_definition = declared
    self._plain_lifting_view._chart_side = 'coast'
    self._maximum_label_material_rounding_difference = 0.
    self._maximum_direct_first_jet_formula_discrepancy = 0.


def _bind_nonlinear_definitions(self, saved, coast, terminal):
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
    self.trace_start=float(terminal['start'])
    self.trace_ramp_stop=float(terminal['ramp_stop'])
    self.trace_cut=float(terminal['cut'])
    last_piece=self.profile.base.segments[-1]
    actual_endpoint_definition=(float(self.profile.end-.02),
        float(last_piece['s0']+.5*last_piece['L']),float(self.profile.end))
    if (self.trace_start,self.trace_ramp_stop,self.trace_cut)!=actual_endpoint_definition:
        raise ValueError('Saved terminal endpoints differ from the bound provider actual operations')
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

