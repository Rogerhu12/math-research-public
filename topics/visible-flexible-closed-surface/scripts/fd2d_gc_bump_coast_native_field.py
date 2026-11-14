"""Explicit R144 frozen-coast lifting on the actual saved P1 raw field.

The defining correction is the saved continuous P1 Fourier function.  Only
the OLD LIFTING is multiplied by (1-w); the correction is not multiplied
again.  Original readers and the active solver source are left unchanged.
"""
from __future__ import annotations
import copy
import json
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import load_npz
from fd2d_gc_raw_native_field import step5, identity, locate_bound
from fd2d_gc_bump_seed_native_field import RawBumpSeedNativeField
from fd2d_gc_frozen_coast_reference import FrozenCoastReference
from fd2d_gc_frozen_coast_second_jets import FrozenCoastSecondJets
from fd2d_balanced_curvature_core import FixedBalancedGeometry

HERE = Path(__file__).resolve().parent
SCHEMA = 'fd2d-raw-physical-bump-explicit-frozen-coast-P1-v3'


def decoded_definition(value):
    out = value if isinstance(value, dict) else json.loads(str(value))
    if not isinstance(out, dict):
        raise ValueError('The actual coast-reference definition must be a JSON object')
    return out


def expected_coast_definition(reference, rim_fraction):
    meta = reference.definition()
    static = {key: meta[key] for key in ('schema', 'binding_sha256', 'candidate_sha256',
        'physical_coast', 'a_c', 'v', 'component_order', 'inverse_tolerance', 'cached_jets_dtype')}
    return dict(reference=static, support=[reference.entry_s, reference.exit_s],
        rim_fraction=float(rim_fraction),
        weight='S5((s-entry)/rim)*S5((exit-s)/rim), each argument clipped to [0,1]',
        lifting='(1-w)*old_seed_tail_lifting+w*frozen_native_reference',
        reference_parameters_frozen=True, original_physical_g_changed=False,
        accurate_reference_GC_applies_only_to_base_delta_zero=True,
        target_defects_and_target_profile_derivatives_not_omitted=True,
        angular_chart_fixed_across_unknown_parameters=True)


def window(x, entry, length, fraction):
    if not 0 < fraction < .5 or not length > 0:
        raise ValueError('The recorded coast weight needs a positive plateau')
    rim = length*fraction
    left, left1, unused = step5((np.asarray(x, float)-entry)/rim)
    right, right1, unused = step5((entry+length-np.asarray(x, float))/rim)
    return left*right, (left1*right-left*right1)/rim


class RawBumpCoastNativeField(RawBumpSeedNativeField):
    def __init__(self, arrays, candidate, *, reference_inlet, reference_cache=None,
                 coast_reference_definition=None, **kwargs):
        data = load_npz(arrays)
        saved = data.get('coast_reference_definition')
        if saved is None and coast_reference_definition is None:
            raise ValueError('The actual field must explicitly declare its frozen-coast lifting')
        definition = decoded_definition(saved if coast_reference_definition is None else coast_reference_definition)
        if saved is not None and definition != decoded_definition(saved):
            raise ValueError('Caller coast lifting differs from the actual saved field')
        super().__init__(arrays, candidate, **kwargs)
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

    def _correction_jets(self, x, xi, side):
        coef, coefx, unused = self.state(x, side=side)
        phase = xi[:, None]*self.frequencies
        C, S, f = np.cos(phase), np.sin(phase), self.frequencies
        bases = (C, S[:, 1:], C)
        first = (-S*f, C[:, 1:]*f[1:], -S*f)
        second = (-C*f*f, -S[:, 1:]*f[1:]*f[1:], -C*f*f)
        sections = (slice(0, self.e), slice(self.e, self.d), slice(self.d, None))
        def sums(cc, bb):
            return np.stack([np.einsum('ij,ij->i', cc[:, ss], b)
                for ss, b in zip(sections, bb)], axis=-1)
        return dict(values=sums(coef, bases), x=sums(coefx, bases),
            xi=sums(coef, first), xixi=sums(coef, second), x_xi=sums(coefx, first))

    def evaluate_native(self, x, xi, *, side='right'):
        """Actual saved field, true cell slopes, and analytical angular jets."""
        xx, pp = np.broadcast_arrays(np.asarray(x, float), np.asarray(xi, float))
        shape = xx.shape; xf, pf = xx.ravel(), pp.ravel()
        old = RawBumpSeedNativeField.evaluate_native(self._plain_lifting_view, xf, pf, side=side)
        corr = self._correction_jets(xf, pf, side)
        ref = self.coast_reference
        w, ws = window(xf, ref.entry_s, ref.length, self.reference_rim_fraction)
        active = (w != 0)|(ws != 0)
        R = {name: np.zeros((len(xf), 3)) for name in ('values', 'x', 'xi', 'xixi', 'x_xi')}
        # Group only actual equal radial labels. At no point is a whole
        # work x nodes x modes tensor formed for the frozen reference.
        for s in np.unique(xf[active]):
            ids = np.flatnonzero(active&(xf == s))
            q = self.coast_second_jets.point(float(s), old['u'][ids])
            us, hu = old['U_x'][ids, None], old['U_xi'][ids, None]
            huu, hsu = old['U_xixi'][ids, None], old['U_x_xi'][ids, None]
            R['values'][ids] = q['values']
            R['x'][ids] = q['physical_s']+us*q['physical_u']
            R['xi'][ids] = hu*q['physical_u']
            R['xixi'][ids] = hu*hu*q['physical_uu']+huu*q['physical_u']
            R['x_xi'][ids] = (hu*q['physical_su']+us*hu*q['physical_uu']
                                  +hsu*q['physical_u'])
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
            raise ValueError('Wrong explicitly declared frozen-coast native schema')
        for source in meta['sources']:
            locate_bound(path, source)
        geometry = FixedBalancedGeometry(moments=locate_bound(path, meta['moments']),
                                         means=locate_bound(path, meta['means']))
        cache = meta.get('reference_cache_input')
        return cls(locate_bound(path, meta['arrays']), locate_bound(path, meta['candidate_input']),
            reference_inlet=locate_bound(path, meta['reference_inlet_input']),
            reference_cache=None if cache is None else locate_bound(path, cache),
            coast_reference_definition=meta['coast_reference_definition'],
            seed_weight_definition=meta['seed_weight_definition'], representation_kind=meta['representation_kind'],
            blend_interval=meta['blend_interval'], profile_supports=meta['profile_supports'],
            fixed_base_T=meta['fixed_base_T'], base_kind=meta['base_kind'], tail_kind=meta['tail_kind'],
            candidate_sha256=meta['candidate_input']['sha256'], collar_guard=meta['collar_guard'], geometry=geometry)

    def definition(self):
        meta = super().definition()
        meta['schema'] = SCHEMA
        extra = ('fd2d_gc_bump_coast_native_field.py', 'fd2d_gc_frozen_coast_second_jets.py',
                 'fd2d_gc_frozen_coast_reference.py', 'fd2d_k0_native_gc.py', 'fd2d_k0_ruling_coast.py')
        meta['sources'] = [identity(HERE/name) for name in extra]+meta['sources']
        meta['reference_inlet_input'] = identity(self.reference_inlet_path)
        meta['reference_cache_input'] = None if self.reference_cache_path is None else identity(self.reference_cache_path)
        meta['coast_reference_definition'] = self.coast_reference_definition
        meta['coast_reference_provenance'] = self.coast_reference.definition()
        meta['reference_second_jet_evaluator'] = self.coast_second_jets.definition()
        meta['lifting']['coast'] = self.coast_reference_definition
        meta['actual_complete_field'] = 'Saved P1 correction + (1-w)*old explicit seed/tail lifting + w*frozen reference'
        meta['correction_multiplied_by_reference_window_by_reader'] = False
        meta['cached_samples_define_the_reference_function'] = False
        meta['physical_target_unchanged_by_reference_lifting'] = True
        meta['target_GC_residuals_still_computed_from_actual_bump_metric'] = True
        return meta
