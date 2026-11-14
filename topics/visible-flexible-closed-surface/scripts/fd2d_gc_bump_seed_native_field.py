"""Explicit seed-weight extension of the frozen physical-bump native reader.

The archive must declare its actual seed weight. The saved P1 mesh, corrections,
target metric, angular chart and complete tail lifting are left untouched.
This reader does not infer a new lifting from a clean-mesh filename or label.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import load_npz
from fd2d_gc_bump_native_field import RawBumpNativeField
from fd2d_gc_raw_native_field import step5, identity, locate_bound
from fd2d_balanced_curvature_core import FixedBalancedGeometry

SCHEMA = 'fd2d-raw-physical-bump-explicit-seed-P1-v2'
HERE = Path(__file__).resolve().parent


def seed_definition(value):
    if not isinstance(value, dict):
        value = json.loads(str(value))
    required = {'kind', 'start', 'end', 'step'}
    if not required.issubset(value):
        raise ValueError('Explicit seed weight needs kind/start/end/step')
    if value['kind'] not in ('central_plateau', 'origin_decay') or value['step'] != 5:
        raise ValueError('Unsupported explicitly saved seed weight')
    start, end = float(value['start']), float(value['end'])
    if not np.isfinite(start+end) or not 0 <= start < end:
        raise ValueError('The explicit seed-weight interval must have positive length')
    return dict(kind=value['kind'], start=start, end=end, step=5)


class RawBumpSeedNativeField(RawBumpNativeField):
    def __init__(self, arrays, candidate, *, seed_weight_definition=None,
                 representation_kind=None, **kwargs):
        data = load_npz(arrays)
        saved_seed = data.get('seed_weight_definition')
        if saved_seed is None and seed_weight_definition is None:
            raise ValueError('The actual seed_weight_definition must be explicitly recorded')
        definition = seed_definition(saved_seed if seed_weight_definition is None else seed_weight_definition)
        if saved_seed is not None and definition != seed_definition(saved_seed):
            raise ValueError('Caller seed weight differs from the actual saved definition')
        saved_representation = data.get('representation_kind')
        if saved_representation is not None and representation_kind is not None and str(saved_representation) != str(representation_kind):
            raise ValueError('Caller representation label differs from the actual saved field')
        self.seed_weight_definition = definition
        self.representation_kind = str(saved_representation if representation_kind is None else representation_kind)
        super().__init__(arrays, candidate, **kwargs)
        if definition['end'] > self.profile.end:
            raise ValueError('Actual seed-weight interval extends outside the physical domain')

    def evaluate_native(self, x, xi, *, side='right'):
        out = super().evaluate_native(x, xi, side=side)
        xx, pp = np.broadcast_arrays(np.asarray(x, float), np.asarray(xi, float))
        old_length = min(.55, .4*self.profile.end)
        old_step, old_first, _ = step5(xx/old_length)
        start, end = (self.seed_weight_definition[key] for key in ('start', 'end'))
        new_step, new_first, _ = step5((xx-start)/(end-start))
        change = old_step-new_step
        change_x = old_first/old_length-new_first/(end-start)
        seed, seed_xi, seed_xixi = self._seed(pp)
        # All seed-profile derivatives are parameter-independent. The only
        # change is this explicitly declared n lifting and its actual jets.
        out['n'] += change*seed
        out['n_x'] += change_x*seed
        out['n_xi'] += change*seed_xi
        out['n_xixi'] += change*seed_xixi
        out['n_x_xi'] += change_x*seed_xi
        return out

    @classmethod
    def from_definition(cls, path):
        path = Path(path)
        meta = json.loads(path.read_text())
        if meta['schema'] != SCHEMA:
            raise ValueError('Wrong explicit-seed physical-bump definition schema')
        for row in meta['sources']:
            locate_bound(path, row)
        geometry = FixedBalancedGeometry(moments=locate_bound(path, meta['moments']),
                                         means=locate_bound(path, meta['means']))
        return cls(locate_bound(path, meta['arrays']), locate_bound(path, meta['candidate_input']),
            seed_weight_definition=meta['seed_weight_definition'], representation_kind=meta['representation_kind'],
            blend_interval=meta['blend_interval'], profile_supports=meta['profile_supports'],
            fixed_base_T=meta['fixed_base_T'], base_kind=meta['base_kind'], tail_kind=meta['tail_kind'],
            candidate_sha256=meta['candidate_input']['sha256'], collar_guard=meta['collar_guard'], geometry=geometry)

    def definition(self):
        meta = super().definition()
        meta['schema'] = SCHEMA
        meta['sources'] = [identity(Path(__file__))]+meta['sources']
        meta['seed_weight_definition'] = self.seed_weight_definition.copy()
        meta['representation_kind'] = self.representation_kind
        meta['lifting']['seed_weight'] = '1-S5((s-start)/(end-start)), clipped to 1/0 outside the saved interval'
        meta['lifting']['seed_start'] = self.seed_weight_definition['start']
        meta['lifting']['seed_end'] = self.seed_weight_definition['end']
        meta['field_definition_changed_if_seed_weight_changes'] = True
        meta['mesh_rebuilt_or_cleaned_by_reader'] = False
        return meta
