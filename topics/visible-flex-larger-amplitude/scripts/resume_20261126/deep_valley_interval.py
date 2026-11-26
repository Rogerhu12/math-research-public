#!/usr/bin/env python3
"""Continuous first/curvature/fixed-g Gram for the NEW R690 scalar field.

This is a different canonical reader from R674. The actual new bundle,
node report, observation carrier, exact scalar profile and every source
are checked before using the existing complete radial/Laurent formulas.
An explicit scratch-only radial view supplies accurate NEW S/R to those
pure formulas; it is never labelled as an old scalar or field certificate.

Every modified finite tail subpiece uses one integer Taylor jet and full
derivative errors. The entire infinite tail uses exact R+t / zero
polynomials plus complete flat-angle derivative bounds. All original
Fourier modes and all analytic angular lift tails remain paid.

Only public repository Actions may execute science. Whole cells finish
naturally before the next admission decision. A same-field runner journal
allows later batches to continue without discarding completed enclosures.
"""
from fractions import Fraction as F
from pathlib import Path
from types import MethodType, SimpleNamespace
import argparse
import gzip
import hashlib
import importlib.util
import json
import math
import os
import sys
import time

import numpy as np


SCHEMA = 'R690-deep-fixed-scalar-continuous-interval-v1'
MODEL_SCHEMA = 'deep-valley-fixed-scalar-fullclosed-lift-v1'
FACTORY_SHA = '4ae012fbc0ccd58ae093069e0229ee8b72db9ef8d7d153565ef4507dc67db2d1'
DEEP_SHA = 'e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2'
BASE_FACTORY_SHA = '2e0219c50543d859a9c649553bc4dde863df24daab26ffa75e5112baa4a90216'
PARENT_READER_SHA = 'f1220a2e83578bb186ec1043c5dc5fd70dd988f1a108897537117344590de225'
FIRST_SHA = 'eaa9a579eea227cbf348138295534144c39d07b669ea1c9ff494f22baa4ae599'
CURVATURE_SHA = '8ca81feefda43fd4423bee1877c8e9198c7774afae0cf8cc2227424765dac385'
SCALAR_POLYNOMIAL_SHA = 'f572c39c7c54f78c360194fd86a1eeba62335ca23f41062f6a7892653ef9a68e'
FULLHOLD_SHA = 'a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670'
INTEGER_SHA = 'babd589d07c91d8067f9ef2011ae53712aaf6dbdbe22bed25c29116771b237a0'
HOLD_SHA = 'ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1'


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('New scientific evaluation belongs only in public repository Actions')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                     allow_nan=False).encode()).hexdigest()


def array_sha(value):
    value = np.ascontiguousarray(value)
    result = hashlib.sha256()
    result.update(str(value.dtype).encode())
    result.update(json.dumps(list(value.shape)).encode())
    result.update(value.tobytes())
    return result.hexdigest()


def load(name, path, expected):
    path = Path(path).resolve()
    if sha(path) != expected:
        raise ValueError('Changed byte-bound source: '+str(path))
    key = '_deep_continuous_'+name+'_'+expected[:16]
    if key in sys.modules:
        return sys.modules[key]
    spec = importlib.util.spec_from_file_location(key, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[key] = module
    spec.loader.exec_module(module)
    return module


def record(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path), bytes=path.stat().st_size)


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+'.partial')
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')
    temporary.replace(path)


def outside(path, repo):
    path, repo = Path(path).resolve(), Path(repo).resolve()
    try:
        path.relative_to(repo)
    except ValueError:
        return path
    raise ValueError('Recomputable reports, views and journals stay outside the repository')


def source_paths(repo):
    topic = Path(repo).resolve()/'topics/visible-flex-larger-amplitude'
    old, new = topic/'scripts/resume_20261120', topic/'scripts/resume_20261126'
    return dict(first_source=old/'actions_closed_postprocess.py',
        curvature_source=old/'actions_closed_curvature.py',
        parent_reader_source=old/'exact_reference_tail_interval.py',
        scalar_polynomial_source=old/'fullclosed_gram_scalar.py',
        factory_source=new/'deep_valley_reference_factory.py',
        deep_scalar_source=new/'deep_valley_tail_input.py',
        base_factory_source=old/'exact_reference_tail_lift.py',
        scalar_source=topic/'notes/2026-11-17-parallel-model-full-hold-oracle.py',
        integer_source=topic/'notes/2026-11-17-parallel-inward-integral-enclosure.py',
        hold_source=topic/'scripts/parallel_20261117_negative_hold_profile_ivp.py')


class DeepIntervalReader:
    """Reuse original complete field formulas with explicitly NEW profiles."""
    def __getattr__(self, name):
        module = self.__dict__.get('_parent_module')
        method = None if module is None else getattr(module.ReferenceIntervalReader, name, None)
        if method is None:
            raise AttributeError(name)
        return MethodType(method, self) if callable(method) else method

    @staticmethod
    def interpolate(left, right, u):
        return tuple((1-u)*a+u*b for a, b in zip(left, right))

    def __init__(self, *, repo, bundle, observations, node_report, scalar_input,
                 scratch, reference_carrier=None, node_producer_source=None, angles=256, low_modes=24,
                 angular_taylor_degree=12, scalar_degree=5, radial_block=4,
                 panels=128, beta='1/4', scalar_tail_cutoff='1/8',
                 scalar_integral_tolerance='1e-18', scalar_admission_seconds=300,
                 first_geometry_report=None):
        require_actions()
        self.repo = Path(repo).resolve()
        self.paths = source_paths(self.repo)
        self.paths.update(bundle=Path(bundle).resolve(), observations=Path(observations).resolve(),
                          node_report=Path(node_report).resolve(), scalar_input=Path(scalar_input).resolve())
        self.paths['node_producer_source'] = (self.paths['factory_source'] if node_producer_source is None
                                              else Path(node_producer_source).resolve())
        if reference_carrier is not None:
            self.paths['reference_carrier'] = Path(reference_carrier).resolve()
        expected = dict(first_source=FIRST_SHA, curvature_source=CURVATURE_SHA,
            parent_reader_source=PARENT_READER_SHA, scalar_polynomial_source=SCALAR_POLYNOMIAL_SHA,
            factory_source=FACTORY_SHA, deep_scalar_source=DEEP_SHA,
            base_factory_source=BASE_FACTORY_SHA, scalar_source=FULLHOLD_SHA,
            integer_source=INTEGER_SHA, hold_source=HOLD_SHA)
        for role, value in expected.items():
            if sha(self.paths[role]) != value:
                raise ValueError('Changed complete source identity: '+role)
        self._parent_module = load('proved_field_formulas', self.paths['parent_reader_source'], PARENT_READER_SHA)
        self.first = load('first', self.paths['first_source'], FIRST_SHA)
        self.curvature_module = load('curvature', self.paths['curvature_source'], CURVATURE_SHA)
        self.scalar_module = load('old_scalar_pieces', self.paths['scalar_polynomial_source'], SCALAR_POLYNOMIAL_SHA)
        self.deep_module = load('new_exact_scalar', self.paths['deep_scalar_source'], DEEP_SHA)
        oracle = load('original_FullHold', self.paths['scalar_source'], FULLHOLD_SHA)
        raw = self.paths['scalar_input'].read_bytes()
        data = json.loads(gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw)
        self.full = oracle.FullHold(data, self.paths['integer_source'], self.paths['hold_source'], panels=int(panels))
        scalar_identity = {key: sha(self.paths[key]) for key in
                           ('scalar_input', 'scalar_source', 'integer_source', 'hold_source')}
        self.deep = self.deep_module.DeepValleyTail(self.full, input_identity=scalar_identity,
            epsilon=F(scalar_tail_cutoff), integral_tolerance=F(scalar_integral_tolerance),
            admission_seconds=float(scalar_admission_seconds))
        self.full_metadata = self.full.metadata()
        with np.load(self.paths['bundle'], allow_pickle=False) as z:
            self.data = {key: np.array(z[key], copy=True) for key in z.files}
        with np.load(self.paths['observations'], allow_pickle=False) as z:
            carrier = {key: np.array(z[key], copy=True) for key in z.files}
        for key in ('mesh', 'a_stages', 'radius', 'width', 'fixed_core_first3'):
            if not np.array_equal(self.data[key], carrier[key]):
                raise ValueError('Actual bundle and NEW scalar observations disagree: '+key)
        self.node_report = json.loads(self.paths['node_report'].read_text())
        self.old_paths = self.first.source_paths(self.repo)
        self.model = self._read_new_model(carrier)
        self.model_sha = canonical_sha(self.model)
        self.lam = F(1)
        self.eta_left = tuple(F(value) for value in self.model['eta_start_symbolic'])
        self.eta_right = tuple(F(value) for value in self.model['eta_end_symbolic'])
        self.scratch = outside(scratch, self.repo)
        self.scratch.mkdir(parents=True, exist_ok=True)
        view = self._write_radial_view()
        args = SimpleNamespace(bundle=self.paths['bundle'], node_report=view,
            beta=beta, taylor_degree=int(angular_taylor_degree), low_modes=min(int(low_modes), int(self.model['M'])),
            plan=[(int(angles), 1)])
        # This source reads only the actual affine q interface, exact nodes,
        # and the explicit S/R supplied by our NEW mathematical view.
        self.b = self.first.make_direct_reader(args, self.old_paths)
        self.r, self.I = self.b.r, self.b.I
        self.r.node_report_path = view
        self.r.transform = self.b.angle.transform
        if not 3 <= int(scalar_degree) <= 8:
            raise ValueError('Use scalar Taylor order 3 through 8')
        self.scalar = self.scalar_module.Scalar(self.r, self.paths['scalar_input'], degree=int(scalar_degree))
        self._add_unchanged_scalar_anchors()
        self.degree = int(scalar_degree)+5
        self.radial_block = int(radial_block)
        if self.radial_block < 1:
            raise ValueError('A positive explicit radial block is required')
        self.curvature = self.curvature_module.CurvatureReader(self.b, radial_block=self.radial_block)
        if (self.scalar.cmp((F(0), self.scalar.cut), self.eta_left) >= 0
                or self.scalar.cmp(self.eta_left, self.eta_right) >= 0
                or self.eta_right != (F(1), -self.r.width)
                or self.scalar.cmp(self.eta_right, (F(1), -self.scalar.out)) >= 0):
            raise ValueError('The exact same eta must stay in Hold and finish before the out ramp')
        self.new_anchor = (F(1), -self.deep.width/4)
        self.new_cutoff = (F(1), -self.deep.width/8)
        self.tail_cutoff = (F(1), -self.deep.width*self.deep.epsilon)
        self.anchor_cache = {}
        self.oracle_anchor_queries = self.saved_anchor_uses = self.profile_anchor_count = 0
        self.maximum_transform_group_entries = 0
        self.maximum_scalar_remainders = np.zeros((2, 3))
        self._q_cache = None
        if reference_carrier is not None:
            # Same exact model, bundle carrier hash, nodes and complete six
            # scalar errors are checked by the unchanged anchor loader.
            self._parent_module.ReferenceIntervalReader._load_profile_anchors(
                self, self.paths['reference_carrier'])
        self.previous = self.previous_identity = self.previous_report = None
        if first_geometry_report is not None:
            path = Path(first_geometry_report).resolve()
            old = json.loads(path.read_text())
            identities = old.get('source_inputs', {})
            if (old.get('schema') != SCHEMA or old.get('source_sha256') != sha(__file__)
                    or old.get('mode') != 'first' or not old.get('complete_scope')
                    or old.get('model_identity_sha256') != self.model_sha
                    or identities.get('bundle', {}).get('sha256') != sha(self.paths['bundle'])
                    or identities.get('node_report', {}).get('sha256') != sha(self.paths['node_report'])
                    or identities.get('observations', {}).get('sha256') != sha(self.paths['observations'])
                    or [row['cell'] for row in old.get('records', [])] != list(range(self.r.J-1))):
                raise ValueError('Only actual complete first bounds for THIS NEW field may be reused')
            self.previous = old['records']
            self.previous_report = old
            self.previous_identity = record(path)
            self.previous_identity['scope'] = 'Actual same-new-field E/W2 bounds only'

    def _read_new_model(self, carrier):
        data, report = self.data, self.node_report
        if 'reference_tail_model_json' not in data or 'reference_tail_lambda' not in data:
            raise ValueError('The new exact scalar must be declared canonically')
        model = json.loads(str(data['reference_tail_model_json'].item()))
        M = (data['qjets'].shape[-1]-2)//3
        nodes = [(F(row['S_coefficient']), F(row['constant']))
                 for row in report['true_scalar_nodes']]
        if (model.get('schema') != MODEL_SCHEMA or model.get('source_sha256') != FACTORY_SHA
                or model.get('base_reference_factory_source_sha256') != BASE_FACTORY_SHA
                or model.get('deep_scalar_source_sha256') != DEEP_SHA
                or model.get('profile_identity_sha256') != self.deep.model_identity_sha256
                or model.get('profile_definition') != self.deep.definition
                or model.get('fixed_new_scalar_metric') is not True
                or model.get('target_is_a_moving_angular_mean') is not False
                or model.get('lambda_value') != 1.
                or model.get('mesh_sha256') != array_sha(data['mesh'])
                or model.get('M') != M
                or model.get('width_exact') != str(F(float(data['width'])))
                or model.get('scalar_input_sha256') != sha(self.paths['scalar_input'])
                or model.get('node_report_sha256') != sha(self.paths['node_report'])
                or model.get('original_observation_carrier_sha256') != sha(self.paths['observations'])):
            raise ValueError('The NEW canonical scalar/field definition differs from actual inputs')
        for key in ('reference_tail_lambda', 'exact_tail_lambda'):
            if key in data and float(data[key]) != 1.:
                raise ValueError('Conflicting actual lambda tags')
        if (report.get('schema') != 'deep-valley-fixed-scalar-symbolic-nodes-v1'
                or report.get('scalar_model_identity_sha256') != self.deep.model_identity_sha256
                or report.get('scalar_model_definition') != self.deep.definition
                or report.get('input_sha256') != sha(self.paths['scalar_input'])
                or report.get('new_carrier_sha256') != sha(self.paths['observations'])
                or report.get('mesh_sha256') != array_sha(data['mesh'])
                or report.get('source_sha256') != sha(self.paths['node_producer_source'])
                or report.get('S_carrier') != self.full.carrier(self.full.S)
                or report.get('S_carrier') != float(data['mesh'][-1])
                or report.get('radius_carrier') != float(data['radius'])
                or len(nodes) != len(data['mesh'])
                or nodes[0] != (F(0), F(0)) or nodes[-1] != (F(1), F(0))):
            raise ValueError('New exact scalar/node provenance does not match the actual field')
        for key, expected in (('scalar_source', FULLHOLD_SHA), ('integer_source', INTEGER_SHA),
                              ('hold_source', HOLD_SHA)):
            if model.get('source_sha256s', {}).get(key) != expected:
                raise ValueError('Changed mathematical scalar dependency: '+key)
        for role, key in (('dense', 'operator'), ('batch', 'batch_source'), ('observed', 'observed_source')):
            actual = sha(self.old_paths[key])
            if model.get('operator_source_sha256s', {}).get(role) != actual:
                raise ValueError('Actual full physical operator changed: '+role)
            if role == 'observed' and model.get('source_sha256s', {}).get('observed_source') != actual:
                raise ValueError('Conflicting actual observation source identity')
            self.paths['canonical_'+role+'_source'] = self.old_paths[key]
        for key in ('eta_start', 'eta_end'):
            index = int(model[key+'_node'])
            if (not 0 < index < len(nodes)-1
                    or tuple(F(value) for value in model[key+'_symbolic']) != nodes[index]
                    or float(model[key+'_carrier']) != float(data['mesh'][index])):
                raise ValueError('Changed actual eta interface')
        if str(carrier.get('deep_valley_scalar_identity_sha256', np.array('')).item()) != self.deep.model_identity_sha256:
            raise ValueError('Observation carrier does not bind the fixed new scalar')
        return model

    def _write_radial_view(self):
        old = self.full.metadata()
        scalar = dict(old)
        scalar['S'] = self.full.enclosure(self.full.S)
        scalar['R'] = self.deep_module.enclosure(self.deep.R)
        scalar['mathematical_profile_scope'] = (
            'NEW S/R for complete radial geometry; original scalar law metadata is used ONLY '
            'on its unchanged prefix. New tail polynomials and errors come from this reader.')
        view = dict(schema='R690-explicit-new-scalar-radial-view-v1',
            input_sha256=sha(self.paths['scalar_input']),
            S_carrier=self.node_report['S_carrier'], radius_carrier=self.node_report['radius_carrier'],
            true_scalar_nodes=self.node_report['true_scalar_nodes'],
            true_a_stage_boxes=[], scalar=scalar, source_sha256=sha(__file__),
            canonical_new_node_report=record(self.paths['node_report']),
            canonical_new_model_identity_sha256=self.model_sha,
            fixed_new_scalar_metric_identity_sha256=self.deep.model_identity_sha256,
            all_old_field_certificates_inherited=False,
            empty_stage_box_list_scope='No sampled a anchors reused; exact original prefix anchors are supplied separately')
        path = self.scratch/'explicit-new-scalar-radial-view.json'
        write_json(path, view)
        self.paths['radial_view'] = path
        return path

    def _add_unchanged_scalar_anchors(self):
        seen = {point for point, _, _ in self.scalar.anchors}
        for segment in self.scalar.segments:
            if segment['kind'] == 'old_exact_quintic':
                continue
            point = segment['left']
            if point in seen:
                continue
            radius, _ = self.full.at_box(self.full.affine_time(*point))
            value = self.r.bounds(F(radius[0], self.full.h.S), F(radius[1], self.full.h.S))
            self.scalar.anchors.append((point, value, 'exact_unchanged_prefix_boundary'))
            seen.add(point)

    def _anchor(self, point):
        if point in self.anchor_cache:
            self.saved_anchor_uses += 1
            return self.anchor_cache[point]
        values = self.deep.reference_at_affine(*point)
        pair = tuple(self.r.bounds(F(value[0], self.deep_module.SCALE),
                                   F(value[1], self.deep_module.SCALE))
                     for value in (values[0], values[3]))
        result = (*pair, 'complete_NEW_integer_scalar_at_exact_symbolic_center')
        self.anchor_cache[point] = result
        self.oracle_anchor_queries += 1
        return result

    def pieces(self, cell):
        result = []
        for piece in self.scalar.pieces(cell):
            left, right, _, _, active, segment = piece
            points = [left]
            for point in (self.eta_left, self.eta_right, self.new_anchor,
                          self.new_cutoff, self.tail_cutoff):
                if self.scalar.cmp(left, point) < 0 and self.scalar.cmp(point, right) < 0:
                    points.append(point)
            points.append(right)
            # Every added point has alpha=1 except the two original eta
            # nodes. Sort using the exact common-S interval comparator.
            from functools import cmp_to_key
            points = sorted(set(points), key=cmp_to_key(self.scalar.cmp))
            for a, b in zip(points, points[1:]):
                u0, u1 = self._parameters(cell, a, b)
                result.append((a, b, u0, u1, active, segment))
        return result

    def _x_bounds(self, point):
        alpha, beta = point
        d = self.deep_module
        t = d.box(-beta) if alpha == 1 else d.sub(
            d.scale(self.deep._from_old(self.full.S), 1-alpha), d.box(beta))
        return F(t[0], d.SCALE)/self.deep.width, F(t[1], d.SCALE)/self.deep.width

    def _finite_beta_jets(self, low, high, order):
        d = self.deep_module
        if not 0 < low <= high:
            raise ValueError('Finite tail Taylor queries must stay away from the exact cap')
        if low == high:
            return self.deep._beta_jets(low, order=order)
        cuts = sorted(set([low, high]+[point for point in (F(1, 8), F(1, 4))
                                      if low < point < high]))
        rows = [self.deep._beta_jets(a, b, order=order) for a, b in zip(cuts, cuts[1:])]
        return [d.hull([row[j] for row in rows]) for j in range(order+1)]

    def _linear_tail_enclosure(self, piece, *, infinite):
        """One exact linear/zero main part; separate a and I derivative fees."""
        left, right = piece[:2]
        I, r = self.I, self.r
        zero = I.exact(np.array([0.]))
        tleft = r.width_box(left, (F(1), F(0)))
        tright = r.width_box(right, (F(1), F(0)))
        a = [I.stack([I.add(r.R, tleft), I.add(r.R, tright)]),
             I.exact(np.array([-1.])), zero]
        integral = [zero, zero, zero]
        _, xmax = self._x_bounds(left)
        if infinite:
            B0, B1 = self.deep.tail_bounds[:2]
            tmax = min(self.deep.width*self.deep.epsilon, self.deep.width*xmax)
            kind = 'entire_infinite_deep_tail'
        else:
            # These are the exact complete R690 replacement-tail bounds,
            # including the cutoff and every unresolved oscillation.
            B0 = self.deep.amplitude*F(29, 4096)
            B1 = self.deep.kappa*F(11737, 32768)
            tmax = min(self.deep.width/4, self.deep.width*xmax)
            kind = 'complete_R690_replacement_low_order_enclosure'
        ea = [tmax*B0*B0/2, B0*B0/2, B0*B1]
        ei = [tmax*B0, B0, B1]
        common = [max(x, y) for x, y in zip(ea, ei)]
        outward = lambda values: [float(r.fraction(value)[1]) for value in values]
        return a, integral, outward(common), dict(
            scalar_segment=kind, exact_tail_cutoff=str(self.deep.epsilon) if infinite else None,
            polynomial_a='EXACT new R+t', polynomial_I='zero',
            complete_flat_angle_bounds_exact=[str(B0), str(B1)],
            a_jet_remainders_exact=[str(value) for value in ea],
            I_jet_remainders_exact=[str(value) for value in ei],
            a_jet_remainders=outward(ea), I_jet_remainders=outward(ei),
            common_a_I_jet_remainders_exact=[str(value) for value in common],
            scalar_jet_remainders=outward(common), all_oscillations_included=True,
            distinct_a_I_fees_preserved_in_physical_fields=True,
            dropped_tail_or_sampled_polynomial=False)

    def _reference_polynomials(self, piece):
        left, right = piece[:2]
        if self.scalar.cmp(right, self.new_anchor) <= 0:
            # a is the original exact function here; I differs only by
            # the NEW fixed terminal integral. _anchor supplies that I.
            result = self._parent_module.ReferenceIntervalReader._reference_polynomials(self, piece)
            detail = dict(result[3], exact_new_height_increment_in_anchor=True,
                          original_out_ramp_used_only_before_new_replacement=True)
            return result[0], result[1], result[2], detail
        if self.scalar.cmp(left, self.new_anchor) < 0:
            raise ValueError('A complete new scalar piece cannot straddle the exact replacement anchor')
        I, r, d, scalar = self.I, self.r, self.deep_module, self.scalar
        zero = I.exact(np.array([0.]))
        if self.scalar.cmp(self.tail_cutoff, left) <= 0:
            return self._linear_tail_enclosure(piece, infinite=True)
        anchor = self.interpolate(left, right, F(1, 2))
        a0, integral0, origin = self._anchor(anchor)
        n = int(scalar.degree)
        x0, x1 = self._x_bounds(anchor)
        beta = self._finite_beta_jets(x0, x1, n)
        # Integer jet coefficients are factorial normalized in x.
        # x=(S-s)/d, hence the physical s coefficient is (-1/d)^j.
        beta_s = [d.scale(value, (-1/self.deep.width)**j) for j, value in enumerate(beta)]
        sine, cosine = d.jsine_cosine(beta_s)
        convert = lambda value: r.bounds(F(value[0], d.SCALE), F(value[1], d.SCALE))
        a_power = [a0]+[I.neg(I.div(convert(cosine[j]), I.exact(j+1))) for j in range(n)]
        integral_power = [integral0]+[I.neg(I.div(convert(sine[j]), I.exact(j+1))) for j in range(n)]
        low = self._x_bounds(right)[0]
        high = self._x_bounds(left)[1]
        beta_whole = self._finite_beta_jets(low, high, n)
        derivative_bounds = [F(math.factorial(j))*d.magnitude(beta_whole[j])/self.deep.width**j
                             for j in range(1, n+1)]
        bell = [F(1)]
        for j in range(1, n+1):
            bell.append(sum((F(math.comb(j-1, k-1))*derivative_bounds[k-1]*bell[j-k]
                             for k in range(1, j+1)), F(0)))
        radius = max(F(float(I.absolute_upper(r.width_box(anchor, edge)))) for edge in (left, right))
        shift, width = r.width_box(anchor, left), r.width_box(left, right)
        controls = []
        for coefficients in (a_power, integral_power):
            jets = []
            for order in range(3):
                powers = [I.scale(coefficients[k], math.factorial(k)//math.factorial(k-order))
                          for k in range(order, len(coefficients))]
                jets.append(scalar.power_to_piece(powers, shift, width))
            controls.append(jets)
        errors_exact = [bell[n]*radius**(n+1-order)/math.factorial(n+1-order) for order in range(3)]
        fallback = self._linear_tail_enclosure(piece, infinite=False)
        ea = [F(value) for value in fallback[3]['a_jet_remainders_exact']]
        ei = [F(value) for value in fallback[3]['I_jet_remainders_exact']]
        if any(error > bound for error, bound in zip(errors_exact, ea)) or any(
                error > bound for error, bound in zip(errors_exact, ei)):
            fallback[3].update(
                finite_Taylor_replaced_by_complete_low_order_enclosure=True,
                reason='The valid high-order interval Bell bound is wider than the proved low-order enclosure',
                mathematical_profile_or_domain_changed=False)
            return fallback
        errors = [float(r.fraction(value)[1]) for value in errors_exact]
        return controls[0], controls[1], errors, dict(
            scalar_segment='finite_NEW_deep_valley_piece', scalar_degree=n,
            anchor_symbolic=[str(value) for value in anchor], anchor_source=origin,
            x_interval_exact=[str(low), str(high)], radius_upper=float(radius),
            common_a_I_derivative_order=n+1, common_a_I_derivative_bound_exact=str(bell[n]),
            scalar_jet_remainders=errors,
            common_a_I_jet_remainders_exact=[str(value) for value in errors_exact],
            one_integer_Taylor_jet_with_derivative_polynomials=True,
            complete_outward_derivative_bounds=True)

    def profile_controls(self, piece, *, include_target=False):
        """Pay independent a/I errors in ALL f/h/k/z jets and same-g a."""
        I, r = self.I, self.r
        left, right, _, _, old_active, _ = piece
        old = r.lift_controls(left, right, old_active)
        oldf = [old[key] for key in ('f', 'fp', 'fpp')]
        oldh = [old[key] for key in ('chi', 'cp', 'cpp')]
        zero = I.exact(np.array([0.]))
        active = self.scalar.cmp(right, self.eta_left) > 0
        if not active:
            f, h, k = oldf, oldh, [zero]*3
            z = [I.mul(value, self.b.H) for value in h]
            ef, ez = [0.]*3, [0.]*3
            reference_a = reference_I = common = ea = ei = None
            A, ae, detail = None, None, dict(reference_active=False)
            if include_target:
                A, ae, detail = self.scalar.approximation(piece)
                detail = dict(detail, reference_active=False)
        else:
            eta = self._eta_controls(left, right)
            a, integral, common, detail = self._reference_polynomials(piece)
            ea = detail.get('a_jet_remainders', common)
            ei = detail.get('I_jet_remainders', common)
            reference_a, reference_I = a, integral
            integral_minus_H = [I.sub(integral[0], self.b.H), *integral[1:]]
            f, h, k, z, ef, ez = [], list(eta), [], [], [], []
            eta_abs = [F(float(I.absolute_upper(value).max())) for value in eta]
            for order in range(3):
                pa, pj, pz = zero, zero, zero
                for split in range(order+1):
                    factor = math.comb(order, split)
                    pa = self.add(pa, I.scale(self.product(eta[split], a[order-split]), factor))
                    pj = self.add(pj, I.scale(self.product(eta[split], integral[order-split]), factor))
                    pz = self.add(pz, I.scale(self.product(eta[split], integral_minus_H[order-split]), factor))
                f.append(pa)
                k.append(I.neg(pj))
                z.append(I.neg(pz))
                for fees, destination in ((ea, ef), (ei, ez)):
                    fee = sum((F(math.comb(order, split))*eta_abs[split]*F(fees[order-split])
                               for split in range(order+1)), F(0))
                    destination.append(float(r.fraction(fee)[1]))
            A, ae = a[0], ea[0]
            detail = dict(detail, reference_active=True,
                a_error_not_replaced_by_I_error=True, complete_lambda_one_Leibniz_chain=True)
        for j, values in enumerate((ef, ez)):
            self.maximum_scalar_remainders[j] = np.maximum(self.maximum_scalar_remainders[j], values)
        return dict(f=[r.elevate(value, self.degree) for value in f],
            h=[r.elevate(value, self.degree) for value in h],
            k=[r.elevate(value, self.degree) for value in k],
            z=[r.elevate(value, self.degree) for value in z],
            f_error=ef, z_error=ez, k_error=ez, h_error=[0.]*3,
            a_poly0=A, a_error0=ae,
            reference_a_jets=reference_a, reference_I_jets=reference_I,
            reference_jet_errors=common, reference_a_jet_errors=ea,
            reference_I_jet_errors=ei, detail=detail)

    def set_resolution(self, angles, modes):
        # Retaining more modes than exist is unnecessary; every remaining
        # finite mode is still paid by the complete l1 tail mechanism.
        self.curvature.set_resolution(int(angles), min(int(modes), self.r.M))

    def metadata(self):
        result = self._parent_module.ReferenceIntervalReader.metadata(self)
        # Old code above contributes only descriptive angular/radial data;
        # every scientific identity and model statement below is NEW.
        result.update(schema=SCHEMA, source_sha256=sha(__file__),
            source_inputs={key: record(path) for key, path in dict(self.b.paths, **self.paths).items()},
            source_formula_reuse=dict(parent_reader=PARENT_READER_SHA, first=FIRST_SHA,
                curvature=CURVATURE_SHA, original_scalar_pieces=SCALAR_POLYNOMIAL_SHA),
            model_definition=self.model, model_identity_sha256=self.model_sha,
            fixed_new_scalar_metric_identity_sha256=self.deep.model_identity_sha256,
            fixed_target='g_n=ds^2+a_new(s)^2*dtheta^2',
            target_is_a_moving_angular_mean=False,
            new_exact_scalar=self.deep.metadata(),
            original_fullhold_used_only_as_unchanged_input=self.full_metadata,
            fullhold=None,
            exact_new_scalar_piece_partition=True,
            new_tail_cut_points=[[str(value) for value in point] for point in
                                 (self.new_anchor, self.new_cutoff, self.tail_cutoff)],
            exact_infinite_tail_included=True,
            old_scalar_or_field_certificates_inherited=False,
            radial_view_scope='Explicit NEW R/S carrier view, only original pure radial/Laurent formulas reused',
            marker_scope='No marker/nonplanarity or old-field geometry certificate is inherited',
            arithmetic='Full NEW integer scalar; original outward f512 Bernstein and complete Laurent tails')
        return result


def ranges(values):
    values = sorted(set(int(value) for value in values))
    result = []
    for value in values:
        if not result or value != result[-1][1]+1:
            result.append([value, value])
        else:
            result[-1][1] = value
    return ','.join(str(a) if a == b else str(a)+'-'+str(b) for a, b in result)


def parse_cells(value, count):
    if value == 'all':
        return list(range(count))
    result = set()
    for item in value.split(','):
        ends = item.split('-')
        if len(ends) == 1:
            result.add(int(ends[0]))
        elif len(ends) == 2:
            a, b = (int(part) for part in ends)
            if a > b:
                raise ValueError('An explicit cell range is reversed')
            result.update(range(a, b+1))
        else:
            raise ValueError('Use cell numbers and inclusive ranges')
    answer = sorted(result)
    if not answer or answer[0] < 0 or answer[-1] >= count:
        raise ValueError('Requested original cells are outside the complete domain')
    return answer


def parse_levels(value):
    result = []
    for item in value.split(','):
        parts = tuple(int(part) for part in item.split(':'))
        if len(parts) != 3:
            raise argparse.ArgumentTypeError('Use angles:radial:retained_modes')
        q, radial, modes = parts
        if q < 4 or q & (q-1) or radial < 1 or radial & (radial-1) or modes < 1 or q <= 4*modes:
            raise argparse.ArgumentTypeError('Use dyadic angles/radial and modes below angles/4')
        result.append(parts)
    if not result:
        raise argparse.ArgumentTypeError('At least one actual complete cover level is required')
    return result


def aggregate(reader, mode, rows, target_metric):
    r, I, b = reader.r, reader.I, reader.b
    values = [rows[cell] for cell in sorted(rows)]
    complete = sorted(rows) == list(range(r.J-1))
    result = dict(complete_scope=complete, covered_cell_count=len(rows),
        covered_cell_ranges=ranges(rows), total_original_cells=r.J-1,
        embedding_certified=False, metric_certified=False, reach_certified=False,
        nonplanarity_certified=False, marker_certified=False,
        closed_isometry_accepted=False, fixed_metric_refinement_convergence_claimed=False,
        topic_complete=False)
    if not values:
        return result
    if mode == 'first':
        caps = b.cap_bounds()
        paid = all(value['support_lower'] is not None and value['support_lower'] > 0
            and value['minimum_normal_squared_lower'] > 0 and value['minimum_E_lower'] > 0
            for value in values)
        support = min(caps['support_lower'], *(value['support_lower'] for value in values)) if paid else None
        radius2 = max(caps['maximum_radius_squared_upper'],
                      *(value['maximum_radius_squared_upper'] for value in values))
        distance2 = min(caps['witness_distance_squared_lower'],
                        *(value['witness_distance_squared_lower'] for value in values))
        diameter = float(I.scale(I.sqrt(I.exact(radius2)), 2)[1])
        distance = float(I.sqrt(I.exact(max(0., distance2)))[0])
        rho = float(b.rho[0].min())
        embedding = bool(complete and paid and rho > 0 and caps['support_lower'] > 0)
        result.update(cap_bounds=caps, core_rho_continuous_lower=rho,
            all_covered_first_form_paid=paid, covered_support_lower=support,
            covered_minimum_normal_squared_lower=min(value['minimum_normal_squared_lower'] for value in values),
            covered_minimum_E_lower=min(value['minimum_E_lower'] for value in values),
            covered_radius_squared_upper=radius2, covered_witness_distance_squared_lower=max(0., distance2),
            continuous_diameter_upper=diameter if complete else None,
            continuous_fixed_witness_distance_lower=distance if complete else None,
            held_amplitude_over_diameter_lower=float(I.div(I.exact(distance), I.exact(diameter))[0]) if embedding else None,
            embedding_certified=embedding, exact_closed_caps_and_reflection_included=True,
            embedding_proof='R650 positive-flow projection plus the original affine core and NEW R690 flat C2 cap jets',
            marked_surface_certificate_included=False)
    elif mode == 'curvature':
        paid = all(value.get('curvature_upper') is not None for value in values)
        bound = max(value['curvature_upper'] for value in values) if paid else None
        result.update(covered_curvature_upper=bound,
            complete_body_curvature_upper=bound if complete else None,
            all_covered_curvature_paid=paid,
            covered_minimum_normal_squared_lower=min(value['minimum_normal_squared_lower'] for value in values),
            covered_minimum_E_lower=min(value['minimum_E_lower'] for value in values),
            flat_caps_curvature_upper=0.,
            reflection_preserves_absolute_principal_curvatures=True)
    else:
        paid = all(value.get('continuous_relative_gram_operator_upper') is not None for value in values)
        bound = max(value['continuous_relative_gram_operator_upper'] for value in values) if paid else None
        result.update(covered_relative_gram_operator_upper=bound,
            complete_relative_gram_operator_upper=bound if complete else None,
            all_covered_metric_paid=paid,
            covered_minimum_a_lower=min(value['minimum_a_lower'] for value in values),
            core_rho_continuous_lower=min(value['minimum_rho_lower'] for value in values),
            requested_metric_bound_paid=bool(complete and paid and bound <= target_metric),
            metric_certified=bool(complete and paid and bound <= 1e-6),
            metric_bound_scope='The SAME fixed NEW g_n on the band and reflection; NEW flat caps have their own exact induced metric',
            numerator_polynomial_cancellation_used=False)
    return result


def main(args):
    require_actions()
    started = time.monotonic()
    if args.admission_seconds <= 0 or args.maximum_new_cells < 1:
        raise ValueError('Use positive natural admission budget and maximum new cell count')
    out = outside(args.out, args.repo)
    journal = outside(args.journal, args.repo)
    scratch = outside(args.scratch, args.repo)
    if out.exists():
        raise FileExistsError('Use a new report for each actual batch')
    q, _, modes = args.levels[0]
    reader = DeepIntervalReader(repo=args.repo, bundle=args.bundle, observations=args.observations,
        node_report=args.node_report, scalar_input=args.scalar_input, scratch=scratch,
        reference_carrier=args.reference_carrier, node_producer_source=args.node_producer_source,
        angles=q, low_modes=modes,
        angular_taylor_degree=args.angular_taylor_degree, scalar_degree=args.scalar_degree,
        radial_block=args.radial_block, panels=args.panels, beta=args.beta,
        scalar_tail_cutoff=args.scalar_tail_cutoff,
        scalar_integral_tolerance=args.scalar_integral_tolerance,
        scalar_admission_seconds=args.scalar_admission_seconds,
        first_geometry_report=args.first_geometry_report)
    curvature_target_derivation = None
    if args.mode == 'curvature':
        if reader.previous_report is None:
            raise ValueError('A complete actual SAME-NEW-FIELD first report sets the curvature target')
        actual_D = reader.previous_report.get('continuous_diameter_upper')
        if actual_D is None or not math.isfinite(float(actual_D)) or float(actual_D) <= 0:
            raise ValueError('The complete same-field first report needs its actual positive diameter upper bound')
        D = F(float(actual_D))
        marked_D = D+F(1, 500)
        sufficient_target = F(100)/(3*marked_D)
        requested = None if args.target_curvature is None else F(args.target_curvature)
        if requested is not None and requested <= 0:
            raise ValueError('Use a positive optional stricter curvature target')
        target = sufficient_target if requested is None else min(sufficient_target, requested)
        args.target_curvature = float(reader.r.fraction(target)[0])
        curvature_target_derivation = dict(actual_same_field_first=reader.previous_identity,
            body_diameter_upper_exact=str(D), marker_diameter_fee_exact='1/500',
            marked_diameter_upper_exact=str(marked_D), formula='100/(3*(D_actual+1/500))',
            sufficient_body_K_target_exact=str(sufficient_target), applied_target_exact=str(target),
            applied_target_downward_float=args.target_curvature,
            expected_or_old_field_D_used=False, marker_curvature_bound_separately_required=True)
    execution = reader.first.actions_context()
    selected = parse_cells(args.cells, reader.r.J-1)
    identity = dict(schema='R690-same-run-continuous-whole-cell-journal-v1',
        source_sha256=sha(__file__), model_identity_sha256=reader.model_sha,
        fixed_scalar_metric_identity_sha256=reader.deep.model_identity_sha256,
        inputs={role: sha(reader.paths[role]) for role in
                ('bundle', 'observations', 'node_report', 'scalar_input')},
        mode=args.mode, levels=[list(level) for level in args.levels],
        beta_exact=str(F(args.beta)), angular_taylor_degree=args.angular_taylor_degree,
        scalar_degree=args.scalar_degree, exact_infinite_tail_cutoff=str(reader.deep.epsilon),
        run_id=os.environ.get('GITHUB_RUN_ID'), run_attempt=os.environ.get('GITHUB_RUN_ATTEMPT'))
    journal_identity = canonical_sha(identity)
    if journal.exists():
        state = json.loads(journal.read_text())
        if (state.get('identity') != identity or state.get('identity_sha256') != journal_identity):
            raise ValueError('This runner journal belongs to another actual field/source/domain/run')
    else:
        state = dict(identity=identity, identity_sha256=journal_identity, rows={}, completed_levels={},
                     completed_whole_cell_evaluations=0)
    rows = {int(key): value for key, value in state['rows'].items()}
    levels_done = {int(key): int(value) for key, value in state['completed_levels'].items()}
    if set(rows) != set(levels_done) or any(cell != row.get('cell') or not 0 <= cell < reader.r.J-1
                                           for cell, row in rows.items()):
        raise ValueError('Invalid whole-cell runner journal address set')
    if any(not 0 <= level < len(args.levels) for level in levels_done.values()):
        raise ValueError('Journal contains a resolution outside the declared finite plan')
    initial_covered = sorted(rows)
    initial_evaluations = int(state['completed_whole_cell_evaluations'])
    new_evaluations, admitted = 0, []
    first_target_radius2 = None if args.target_diameter is None else F(args.target_diameter)**2/4

    def needed(row):
        if row is None:
            return True
        if args.mode == 'first':
            return (row.get('support_lower') is None or row['support_lower'] < args.target_support
                or row['minimum_normal_squared_lower'] <= 0 or row['minimum_E_lower'] <= 0
                or (first_target_radius2 is not None
                    and F(row['maximum_radius_squared_upper']) > first_target_radius2))
        key = 'curvature_upper' if args.mode == 'curvature' else 'continuous_relative_gram_operator_upper'
        target = args.target_curvature if args.mode == 'curvature' else args.target_metric
        return row.get(key) is None or row[key] > target

    method = getattr(reader, args.mode+'_cell')
    stop_reason = 'Every selected cell reached the current goal or exhausted its declared resolution plan'
    while True:
        work = [(levels_done.get(cell, -1)+1, cell) for cell in selected
                if needed(rows.get(cell)) and levels_done.get(cell, -1)+1 < len(args.levels)]
        if not work:
            break
        if new_evaluations and (time.monotonic()-started >= args.admission_seconds
                                or new_evaluations >= args.maximum_new_cells):
            stop_reason = 'Natural admission budget reached after saving a complete whole-cell enclosure'
            break
        level, cell = min(work)
        q, radial, modes = args.levels[level]
        reader.set_resolution(q, modes)
        modes = reader.b.low_modes
        row = method(cell, radial)
        rows[cell] = reader._parent_module.combine(reader, rows.get(cell), row, args.mode)
        levels_done[cell] = level
        new_evaluations += 1
        admitted.append(cell)
        state.update(rows={str(key): rows[key] for key in sorted(rows)},
                     completed_levels={str(key): levels_done[key] for key in sorted(levels_done)},
                     completed_whole_cell_evaluations=initial_evaluations+new_evaluations)
        write_json(journal, state)
        reader.first.announce(event='deep_new_scalar_complete_cell_saved', mode=args.mode,
            cell=cell, level=level, angles=q, radial=radial, retained_modes=modes,
            new_completed_evaluations=new_evaluations, covered_cell_ranges=ranges(rows),
            elapsed_seconds=time.monotonic()-started)
    metadata = reader.metadata()
    aggregate_bounds = aggregate(reader, args.mode, rows, args.target_metric)
    selected_pending = [cell for cell in selected if needed(rows.get(cell))]
    remaining = [cell for cell in range(reader.r.J-1) if needed(rows.get(cell))]
    report = dict(metadata, execution=execution, mode=args.mode,
        requested_cells=selected, requested_cell_ranges=ranges(selected),
        refinement_plan=[list(level) for level in args.levels],
        covered_cells=sorted(rows), records=[rows[key] for key in sorted(rows)],
        inherited_same_run_covered_cell_ranges=ranges(initial_covered),
        new_completed_cell_ranges=ranges(admitted), new_whole_cell_evaluations=new_evaluations,
        journal=record(journal) if journal.exists() else None,
        journal_identity_sha256=journal_identity,
        requested_admission_seconds=args.admission_seconds,
        maximum_new_cell_evaluations=args.maximum_new_cells,
        status='naturally_returned', stop_reason=stop_reason,
        remaining_selected_below_goal_ranges=ranges(selected_pending),
        remaining_all_cells_below_goal_ranges=ranges(remaining),
        remaining_all_cells_below_goal_count=len(remaining),
        target_support=args.target_support, target_diameter=args.target_diameter,
        target_curvature=args.target_curvature, target_metric=args.target_metric,
        curvature_target_from_actual_first=curvature_target_derivation,
        seconds=time.monotonic()-started, historical_candidate_hash_assumed=False,
        raw_records_publication_requested=False,
        finite_budget_exhaustion_is_not_geometric_impossibility=True,
        **aggregate_bounds)
    write_json(out, report)
    reader.first.announce(event='deep_new_scalar_continuous_batch_returned',
        mode=args.mode, report_sha256=sha(out),
        bundle_sha256=sha(args.bundle), node_report_sha256=sha(args.node_report),
        fixed_scalar_metric_identity_sha256=reader.deep.model_identity_sha256,
        complete_scope=report['complete_scope'],
        covered_cell_ranges=report['covered_cell_ranges'],
        remaining_below_goal=report['remaining_all_cells_below_goal_count'],
        seconds=report['seconds'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('repo', 'bundle', 'observations', 'node-report', 'scalar-input', 'scratch', 'journal', 'out'):
        parser.add_argument('--'+key, type=Path, required=True)
    parser.add_argument('--reference-carrier', type=Path)
    parser.add_argument('--node-producer-source', type=Path)
    parser.add_argument('--first-geometry-report', type=Path)
    parser.add_argument('--mode', choices=('first', 'curvature', 'metric'), default='first')
    parser.add_argument('--cells', default='all')
    parser.add_argument('--levels', type=parse_levels, default=parse_levels(
        '256:1:24,512:2:32,1024:4:48,2048:8:64,4096:16:96'))
    parser.add_argument('--target-support', type=float, default=.14)
    parser.add_argument('--target-diameter', type=str)
    parser.add_argument('--target-curvature', type=str)
    parser.add_argument('--target-metric', type=float, default=1e-6)
    parser.add_argument('--angular-taylor-degree', type=int, default=12)
    parser.add_argument('--scalar-degree', type=int, default=5)
    parser.add_argument('--radial-block', type=int, default=4)
    parser.add_argument('--panels', type=int, default=128)
    parser.add_argument('--beta', default='1/4')
    parser.add_argument('--scalar-tail-cutoff', default='1/8')
    parser.add_argument('--scalar-integral-tolerance', default='1e-18')
    parser.add_argument('--scalar-admission-seconds', type=float, default=300)
    parser.add_argument('--admission-seconds', type=float, default=600)
    parser.add_argument('--maximum-new-cells', type=int, default=1024)
    main(parser.parse_args())
