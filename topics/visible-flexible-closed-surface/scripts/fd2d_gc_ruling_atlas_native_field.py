"""Actual P1 raw field in the explicitly saved R149 frozen ruling atlas.

The new atlas is a coordinate definition, not a replacement target metric.
This reader uses the exact stored mesh and full lifting, keeps independent
l, and selects P1 and chart radial derivatives from the same requested side.
The frozen reference is evaluated directly at the known coast label.
"""
from __future__ import annotations
import copy
import json
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from fd2d_gc_archive_arrays import load_npz
from fd2d_gc_raw_native_field import identity, locate_bound
from fd2d_gc_raw_lifted_dae import CertifiedReference
from fd2d_gc_blended import BlendedIntrinsicGC
from fd2d_gc_bump_seed_native_field import RawBumpSeedNativeField
from fd2d_gc_bump_coast_native_field import RawBumpCoastNativeField, decoded_definition, window
from fd2d_gc_frozen_ruling_atlas import FrozenRulingAtlas
from fd2d_gc_ruling_reference_second_jets import ruling_reference_second_jets
from fd2d_balanced_curvature_core import FixedBalancedGeometry

HERE = Path(__file__).resolve().parent
SCHEMA = 'fd2d-raw-physical-bump-frozen-ruling-atlas-P1-v4'


class RulingAtlasRawBumpNativeField(RawBumpCoastNativeField):
    def __init__(self, arrays, candidate, *, reference_inlet, reference_cache=None,
                 angular_atlas_definition=None, **kwargs):
        saved = load_npz(arrays)
        actual = saved.get('angular_atlas_definition')
        if actual is None and angular_atlas_definition is None:
            raise ValueError('The actual field must explicitly declare its full angular atlas')
        declared = decoded_definition(actual if angular_atlas_definition is None else angular_atlas_definition)
        if actual is not None and decoded_definition(actual) != declared:
            raise ValueError('Caller atlas differs from the actual saved field')
        super().__init__(arrays, candidate, reference_inlet=reference_inlet,
                         reference_cache=reference_cache, **kwargs)
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

    def chart(self, x, xi, *, side=None):
        side = getattr(self, '_chart_side', 'coast') if side is None else side
        if side not in ('coast', 'left', 'right'):
            raise ValueError('The chart side must be coast, left, or right')
        xx, pp = np.broadcast_arrays(np.asarray(x, float), np.asarray(xi, float))
        shape = xx.shape; xf, pf = xx.ravel(), pp.ravel()
        names = dict(u='u', u_x='u_s', u_xi='u_xi', u_xixi='u_xixi',
                     u_x_xi='u_sxi', u_xx='u_ss')
        result = {name: np.empty(len(xf)) for name in names}
        # coordinates() is a tensor-grid API. Group actual equal radial
        # labels rather than taking an accidental outer product of all
        # flattened point pairs.
        for s in np.unique(xf):
            ids = np.flatnonzero(xf == s)
            q = self.angular_atlas.coordinates(np.array([s]), coordinate=pf[ids], side=side)
            for target, source in names.items():
                result[target][ids] = np.asarray(q[source][:, 0], float)
        return {name: value.reshape(shape) for name, value in result.items()}

    def evaluate_native(self, x, xi, *, side='right'):
        if side not in ('left', 'right'):
            raise ValueError('Select the same left or right side for both P1 slope and chart radial jets')
        xx, pp = np.broadcast_arrays(np.asarray(x, float), np.asarray(xi, float))
        shape = xx.shape; xf, pf = xx.ravel(), pp.ravel()
        plain_view = copy.copy(self._plain_lifting_view)
        plain_view._chart_side = side
        old = RawBumpSeedNativeField.evaluate_native(plain_view, xf, pf, side=side)
        corr = self._correction_jets(xf, pf, side)
        ref = self.coast_reference
        w, ws = window(xf, ref.entry_s, ref.length, self.reference_rim_fraction)
        active = (w != 0)|(ws != 0)
        R = {name: np.zeros((len(xf), 3)) for name in ('values', 'x', 'xi', 'xixi', 'x_xi')}
        for s in np.unique(xf[active]):
            ids = np.flatnonzero(active&(xf == s))
            q = ruling_reference_second_jets(self.angular_atlas, s, pf[ids])
            mismatch = np.max(abs(q['material_u']-np.asarray(old['u'][ids], np.longdouble)))
            if mismatch > 32*np.finfo(float).eps*(1+np.max(abs(q['material_u']))):
                raise ArithmeticError('Known ruling label is not the actual requested material coordinate')
            self._maximum_label_material_rounding_difference = max(
                self._maximum_label_material_rounding_difference, float(mismatch))
            self._maximum_direct_first_jet_formula_discrepancy = max(
                self._maximum_direct_first_jet_formula_discrepancy,
                q['diagnostics']['first_u_formula_discrepancy'])
            us, hu = old['U_x'][ids, None], old['U_xi'][ids, None]
            huu, hsu = old['U_xixi'][ids, None], old['U_x_xi'][ids, None]
            R['values'][ids] = q['values']
            R['x'][ids] = q['physical_s']+us*q['physical_u']
            R['xi'][ids] = hu*q['physical_u']
            R['xixi'][ids] = hu*hu*q['physical_uu']+huu*q['physical_u']
            R['x_xi'][ids] = hu*q['physical_su']+us*hu*q['physical_uu']+hsu*q['physical_u']
        values = np.stack([old[name] for name in ('n', 'm', 'l')], axis=-1)
        angular = np.stack([old[name+'_xi'] for name in ('n', 'm', 'l')], axis=-1)
        wcol, wscol = w[:, None], ws[:, None]
        for key, suffix in (('values', ''), ('x', '_x'), ('xi', '_xi'),
                            ('xixi', '_xixi'), ('x_xi', '_x_xi')):
            base = np.stack([old[name+suffix] for name in ('n', 'm', 'l')], axis=-1)
            out = corr[key]+(1-wcol)*base+wcol*R[key]
            if key == 'x':
                out += wscol*(R['values']-values)
            elif key == 'x_xi':
                out += wscol*(R['xi']-angular)
            for j, name in enumerate(('n', 'm', 'l')):
                old[name+suffix] = out[:, j]
        return {name: np.asarray(value).reshape(shape) for name, value in old.items()}

    @classmethod
    def from_definition(cls, path):
        path = Path(path); meta = json.loads(path.read_text())
        if meta['schema'] != SCHEMA:
            raise ValueError('Wrong explicit frozen-ruling-atlas native schema')
        for row in meta['sources']:
            locate_bound(path, row)
        geometry = FixedBalancedGeometry(moments=locate_bound(path, meta['moments']),
                                         means=locate_bound(path, meta['means']))
        cache = meta.get('reference_cache_input')
        return cls(locate_bound(path, meta['arrays']), locate_bound(path, meta['candidate_input']),
            reference_inlet=locate_bound(path, meta['reference_inlet_input']),
            reference_cache=None if cache is None else locate_bound(path, cache),
            angular_atlas_definition=meta['angular_atlas_definition'],
            coast_reference_definition=meta['coast_reference_definition'],
            seed_weight_definition=meta['seed_weight_definition'], representation_kind=meta['representation_kind'],
            blend_interval=meta['blend_interval'], profile_supports=meta['profile_supports'],
            fixed_base_T=meta['fixed_base_T'], base_kind=meta['base_kind'], tail_kind=meta['tail_kind'],
            candidate_sha256=meta['candidate_input']['sha256'], collar_guard=meta['collar_guard'], geometry=geometry)

    def definition(self):
        meta = super().definition()
        meta['schema'] = SCHEMA
        extra = ('fd2d_gc_ruling_atlas_native_field.py', 'fd2d_gc_ruling_reference_second_jets.py',
                 'fd2d_gc_frozen_ruling_atlas.py', 'fd2d_gc_raw_bump_ruling_atlas.py', 'fd2d_gc_blended.py')
        meta['sources'] = [identity(HERE/name) for name in extra]+meta['sources']
        meta['angular_atlas_definition'] = self.angular_atlas_definition
        meta['atlas_mesh_definition'] = self.atlas_mesh_definition
        meta['checkpoint_reference_evaluation_definition'] = self.reference_evaluation_definition
        meta['checkpoint_finite_radial_scheme'] = self.finite_radial_scheme
        meta['angular_chart'] = 'R149 explicit global frozen ruling atlas; saved blend is only the unchanged original-chart component'
        meta['coast_label'] = 'Frozen inlet seed-normal xi; incoming material t=U_seed(xi)'
        meta['reference_second_jet_evaluator'] = dict(source=identity(HERE/'fd2d_gc_ruling_reference_second_jets.py'),
            physical_derivatives=['s', 'u', 'uu', 'su'], material_inverse_used=False,
            formula='Original R139 values/first jets at the known ruling label, with analytic finite-inlet third derivatives',
            maximum_label_material_rounding_difference=self._maximum_label_material_rounding_difference,
            maximum_first_jet_formula_discrepancy=self._maximum_direct_first_jet_formula_discrepancy,
            continuous_numeric_certificate=False)
        meta['native_interface_side'] = 'side=left or right applies jointly to actual P1 slope and actual chart radial jets; default right'
        meta['chart_only_default_side'] = 'coast, matching the finite solver convention'
        meta['source_checkpoint_projection_reinterpreted_as_exact'] = False
        meta['mesh_rebuilt_or_cleaned_by_reader'] = False
        return meta
