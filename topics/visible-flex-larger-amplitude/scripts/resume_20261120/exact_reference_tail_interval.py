#!/usr/bin/env python3
"""Continuous interval geometry for the canonical R671 reference-tail field.

No scientific work runs on import.  The CLI is restricted to this public
repository's Actions.  Original q Fourier coefficients and exact symbolic
nodes are retained.  New a/I terms are enclosed by a common Taylor jet,
independent derivative remainders and the original FullHold integer oracle;
they are never identified with a sampled or fitted polynomial.

The first-geometry and curvature consumers reuse R670/R672 angular and
shape formulas.  profile_controls() also exposes a_poly0/a_error0 and all
nine scalar jets for cancellation-preserving Gram consumers.  The optional
metric command is a complete direct interval bound, not the tighter R657
numerator-polynomial implementation and not an optimization objective.
"""
from fractions import Fraction as F
from pathlib import Path
from types import SimpleNamespace
import argparse
import gzip
import hashlib
import importlib.util
import json
import math
import sys
import time

import numpy as np


SCHEMA = 'R671-reference-tail-continuous-interval-v1'
FACTORY_SHA = '2e0219c50543d859a9c649553bc4dde863df24daab26ffa75e5112baa4a90216'
FIRST_SHA = 'eaa9a579eea227cbf348138295534144c39d07b669ea1c9ff494f22baa4ae599'
CURVATURE_SHA = '8ca81feefda43fd4423bee1877c8e9198c7774afae0cf8cc2227424765dac385'
SCALAR_SHA = 'f572c39c7c54f78c360194fd86a1eeba62335ca23f41062f6a7892653ef9a68e'
FULLHOLD_SHA = 'a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670'
INTEGER_SHA = 'babd589d07c91d8067f9ef2011ae53712aaf6dbdbe22bed25c29116771b237a0'
HOLD_SHA = 'ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical_sha(value):
    raw = json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def array_sha(value):
    value = np.ascontiguousarray(value)
    digest = hashlib.sha256()
    digest.update(str(value.dtype).encode())
    digest.update(json.dumps(list(value.shape)).encode())
    digest.update(value.tobytes())
    return digest.hexdigest()


def load(name, path, expected=None):
    path = Path(path).resolve()
    if expected is not None and sha(path) != expected:
        raise ValueError('Changed declared source: '+str(path))
    name = '_reference_tail_interval_'+name+'_'+sha(path)[:16]
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def source_paths(repo):
    topic = Path(repo).resolve()/'topics/visible-flex-larger-amplitude'
    src = topic/'scripts/resume_20261120'
    return dict(first_source=src/'actions_closed_postprocess.py',
        curvature_source=src/'actions_closed_curvature.py',
        scalar_polynomial_source=src/'fullclosed_gram_scalar.py',
        factory_source=src/'exact_reference_tail_lift.py',
        scalar_source=topic/'notes/2026-11-17-parallel-model-full-hold-oracle.py',
        integer_source=topic/'notes/2026-11-17-parallel-inward-integral-enclosure.py',
        hold_source=topic/'scripts/parallel_20261117_negative_hold_profile_ivp.py')


class ReferenceIntervalReader:
    """Same canonical field, with all Taylor errors in the physical six jets."""

    def __init__(self, *, repo, bundle, node_report, scalar_input,
                 reference_carrier=None, angles=256, low_modes=24,
                 angular_taylor_degree=12, scalar_degree=5, radial_block=4,
                 panels=128, beta='1/4', first_geometry_report=None):
        self.paths = source_paths(repo)
        self.paths.update(bundle=Path(bundle).resolve(), node_report=Path(node_report).resolve(),
                          scalar_input=Path(scalar_input).resolve())
        if reference_carrier is not None:
            self.paths['reference_carrier'] = Path(reference_carrier).resolve()
        self.first = load('first', self.paths['first_source'], FIRST_SHA)
        self.curvature_module = load('curvature', self.paths['curvature_source'], CURVATURE_SHA)
        self.scalar_module = load('scalar', self.paths['scalar_polynomial_source'], SCALAR_SHA)
        if sha(self.paths['factory_source']) != FACTORY_SHA:
            raise ValueError('Canonical R671 source identity changed')
        self.old_paths = self.first.source_paths(repo)
        args = SimpleNamespace(bundle=self.paths['bundle'], node_report=self.paths['node_report'],
            beta=beta, taylor_degree=int(angular_taylor_degree), low_modes=int(low_modes),
            plan=[(int(angles), 1)])
        self.b = self.first.make_direct_reader(args, self.old_paths)
        self.r, self.I = self.b.r, self.b.I
        self.r.node_report_path = self.paths['node_report']
        self.r.transform = self.b.angle.transform
        if not 3 <= int(scalar_degree) <= 8:
            raise ValueError('This implementation supports scalar Taylor degree 3 through 8; default is 5')
        self.scalar = self.scalar_module.Scalar(self.r, self.paths['scalar_input'], degree=scalar_degree)
        self.degree = int(scalar_degree)+5
        self.radial_block = int(radial_block)
        if self.radial_block < 1:
            raise ValueError('Positive radial block count required')
        self.curvature = self.curvature_module.CurvatureReader(self.b, radial_block=self.radial_block)
        self.data = self.b.d.base
        self.model = self._read_model()
        self.model_sha = canonical_sha(self.model)
        self.lam = F(float(self.model['lambda_value']))
        self.eta_left = tuple(F(v) for v in self.model['eta_start_symbolic'])
        self.eta_right = tuple(F(v) for v in self.model['eta_end_symbolic'])
        if (self.scalar.cmp((F(0), self.scalar.cut), self.eta_left) >= 0
                or self.scalar.cmp(self.eta_left, self.eta_right) >= 0
                or self.eta_right != (F(1), -self.r.width)
                or self.scalar.cmp(self.eta_right, (F(1), -self.scalar.out)) >= 0):
            raise ValueError('eta must start inside Hold and reach one before the complete out ramp')
        self.anchor_cache = {}
        self.oracle_anchor_queries = 0
        self.saved_anchor_uses = 0
        self.profile_anchor_count = 0
        self.maximum_transform_group_entries = 0
        self.maximum_scalar_remainders = np.zeros((2, 3))
        self._q_cache = None
        self.full = None
        self.full_metadata = None
        if self.lam:
            oracle = load('fullhold', self.paths['scalar_source'], FULLHOLD_SHA)
            if sha(self.paths['integer_source']) != INTEGER_SHA or sha(self.paths['hold_source']) != HOLD_SHA:
                raise ValueError('Changed original FullHold integer dependency')
            raw = self.paths['scalar_input'].read_bytes()
            data = json.loads(gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw)
            self.full = oracle.FullHold(data, self.paths['integer_source'], self.paths['hold_source'], panels=int(panels))
            self.full_metadata = self.full.metadata()
            self._check_fullhold_identity()
            if reference_carrier is not None:
                self._load_profile_anchors(self.paths['reference_carrier'])
        self.previous = None
        self.previous_identity = None
        if first_geometry_report is not None:
            path = Path(first_geometry_report).resolve()
            old = json.loads(path.read_text())
            si = old.get('source_inputs', {})
            if (old.get('source_sha256') != sha(__file__) or old.get('mode') != 'first'
                    or not old.get('complete_scope') or old.get('model_identity_sha256') != self.model_sha
                    or si.get('bundle', {}).get('sha256') != sha(self.paths['bundle'])
                    or si.get('node_report', {}).get('sha256') != sha(self.paths['node_report'])
                    or [v['cell'] for v in old.get('records', [])] != list(range(self.r.J-1))):
                raise ValueError('Only the exact same new-field complete first-form bounds may be reused')
            self.previous = old['records']
            self.previous_identity = dict(path=str(path), sha256=sha(path),
                scope='Only actual same-candidate E/W2 lower bounds; no old-lift certificate')

    def _read_model(self):
        data, r = self.data, self.r
        if 'reference_tail_model_json' not in data or 'reference_tail_lambda' not in data:
            raise ValueError('A canonical R671 bundle and explicit lambda tag are required')
        model = json.loads(str(data['reference_tail_model_json'].item()))
        if (model.get('schema') != 'R671-exact-reference-tail-lift-v1'
                or model.get('source_sha256') != FACTORY_SHA
                or model.get('mesh_sha256') != array_sha(data['mesh'])
                or model.get('M') != r.M
                or model.get('scalar_input_sha256') != sha(self.paths['scalar_input'])
                or model.get('node_report_sha256') != sha(self.paths['node_report'])):
            raise ValueError('The canonical field definition does not match its actual inputs')
        value = float(model.get('lambda_value', -1))
        if not np.isfinite(value) or not 0 <= value <= 1:
            raise ValueError('Invalid fixed R671 lambda')
        for key in ('reference_tail_lambda', 'exact_tail_lambda'):
            if key in data and float(data[key]) != value:
                raise ValueError('Conflicting R671 lambda tags')
        for key, expected in (('scalar_source', FULLHOLD_SHA), ('integer_source', INTEGER_SHA), ('hold_source', HOLD_SHA)):
            if model.get('source_sha256s', {}).get(key) != expected or sha(self.paths[key]) != expected:
                raise ValueError('Changed canonical scalar definition: '+key)
        for role, key in (('dense', 'operator'), ('batch', 'batch_source'), ('observed', 'observed_source')):
            actual = sha(self.old_paths[key])
            if model.get('operator_source_sha256s', {}).get(role) != actual:
                raise ValueError('Canonical field operator source differs from the stated representation: '+role)
            if role == 'observed' and model.get('source_sha256s', {}).get('observed_source') != actual:
                raise ValueError('Canonical observation source identities disagree')
            self.paths['canonical_'+role+'_source'] = self.old_paths[key]
        for key in ('eta_start', 'eta_end'):
            index = int(model[key+'_node'])
            if not 0 < index < r.J-1 or tuple(F(v) for v in model[key+'_symbolic']) != r.nodes[index]:
                raise ValueError('eta physical endpoints must match the current exact symbolic mesh')
        return model

    def _check_fullhold_identity(self):
        p, I, r = self.full, self.I, self.r
        for name, old in (('S', r.S), ('R', r.R)):
            box = getattr(p, name)
            new = r.bounds(F(box[0], p.h.S), F(box[1], p.h.S))
            if float(new[1]) < float(old[0]) or float(old[1]) < float(new[0]):
                raise ValueError('Original scalar endpoint enclosures are disjoint: '+name)
        if (p.carrier(p.S) != float(r.mesh[-1]) or p.carrier(p.R) != float(self.data['radius'])
                or p.cut != self.scalar.cut or p.origin != self.scalar.origin):
            raise ValueError('The same exact Hold definition has changed')

    def _load_profile_anchors(self, path):
        declared = str(self.data.get('reference_tail_carrier_sha256', np.array('')).item())
        if not declared or declared != sha(path):
            raise ValueError('Reference carrier must have the actual canonical bundle SHA')
        with np.load(path, allow_pickle=False) as z:
            definition = json.loads(str(z['model_definition_json'].item()))
            if definition != self.model or not np.array_equal(z['mesh'], self.data['mesh']):
                raise ValueError('Reference carrier belongs to another canonical field')
            values, errors = z['reference_values'], z['reference_absolute_error']
            active = np.asarray(z['reference_active'], dtype=bool)
            cells, uu = z['observation_cells'], z['observation_u']
            if values.shape != errors.shape or values.shape != (len(active), 6):
                raise ValueError('Incomplete six-column reference carrier')
            for stage in np.flatnonzero(active):
                cell, u = int(cells[stage]), F(float(uu[stage]))
                if not 0 <= cell < self.r.J-1 or not 0 <= u <= 1:
                    raise ValueError('Saved reference anchor is outside its exact carrier')
                point = self.interpolate(self.r.nodes[cell], self.r.nodes[cell+1], u)
                if np.any(errors[stage] < 0) or not np.isfinite(values[stage]).all() or not np.isfinite(errors[stage]).all():
                    raise ValueError('Invalid outward reference carrier errors')
                pair = []
                for col in (0, 3):
                    v, e = F(float(values[stage, col])), F(float(errors[stage, col]))
                    pair.append(self.r.bounds(v-e, v+e))
                self.anchor_cache[point] = (*pair, 'saved_complete_integer_oracle_carrier')
            self.profile_anchor_count = len(self.anchor_cache)

    @staticmethod
    def interpolate(left, right, u):
        return tuple((1-u)*a+u*b for a, b in zip(left, right))

    def _anchor(self, point):
        if point in self.anchor_cache:
            self.saved_anchor_uses += 1
            return self.anchor_cache[point]
        p = self.full
        if p is None:
            raise ValueError('No reference oracle is needed or instantiated at lambda zero')
        box = p.affine_time(*point)
        a, inc = p.at_box(box)
        if inc is None:
            raise ValueError('Reference I is only defined on the original Hold extension')
        integral = (0, 0) if point == (F(1), F(0)) else p.o.subtract(p.height_increment, inc)
        if point == (F(1), F(0)):
            a = p.R
        pair = tuple(self.r.bounds(F(v[0], p.h.S), F(v[1], p.h.S)) for v in (a, integral))
        answer = (*pair, 'original_integer_oracle_at_exact_symbolic_center')
        self.anchor_cache[point] = answer
        self.oracle_anchor_queries += 1
        return answer

    def _parameters(self, cell, left, right):
        r, I = self.r, self.I
        h = r.width_box(r.nodes[cell], r.nodes[cell+1])
        if float(h[0]) <= 0:
            raise ValueError('Original symbolic cell width must be positive')
        u0 = I.exact(0.) if left == r.nodes[cell] else I.div(r.width_box(r.nodes[cell], left), h)
        u1 = I.exact(1.) if right == r.nodes[cell+1] else I.div(r.width_box(r.nodes[cell], right), h)
        return u0, u1

    def pieces(self, cell):
        """Joint exact partition: scalar segments, old chi, and both eta nodes."""
        result = []
        for piece in self.scalar.pieces(cell):
            left, right, _, _, old_active, segment = piece
            cuts = [left]
            for point in (self.eta_left, self.eta_right):
                if self.scalar.cmp(left, point) < 0 and self.scalar.cmp(point, right) < 0:
                    cuts.append(point)
            cuts.append(right)
            for a, b in zip(cuts, cuts[1:]):
                u0, u1 = self._parameters(cell, a, b)
                result.append((a, b, u0, u1, old_active, segment))
        return result

    def subpiece(self, cell, piece, j, count):
        left, right = [self.interpolate(piece[0], piece[1], F(k, count)) for k in (j, j+1)]
        u0, u1 = self._parameters(cell, left, right)
        return left, right, u0, u1, piece[4], piece[5]

    def product(self, a, b):
        """Exact rational Bernstein multiplication with outward operations."""
        I, r = self.I, self.r
        m, n = len(a[0])-1, len(b[0])-1
        out = []
        for k in range(m+n+1):
            value = I.exact(0.)
            for j in range(max(0, k-n), min(m, k)+1):
                weight = r.fraction(F(math.comb(m, j)*math.comb(n, k-j), math.comb(m+n, k)))
                value = I.add(value, I.mul(weight, I.mul(I.at(a, j), I.at(b, k-j))))
            out.append(value)
        return I.stack(out)

    def add(self, a, b):
        degree = max(len(a[0]), len(b[0]))-1
        return self.I.add(self.r.elevate(a, degree), self.r.elevate(b, degree))

    def _eta_controls(self, left, right):
        I, r, cmp = self.I, self.r, self.scalar.cmp
        zero, one = I.exact(np.array([0.])), I.exact(np.array([1.]))
        if cmp(right, self.eta_left) <= 0:
            return [zero, zero, zero]
        if cmp(self.eta_right, left) <= 0:
            return [one, zero, zero]
        if cmp(left, self.eta_left) < 0 or cmp(self.eta_right, right) < 0:
            raise ValueError('The eta polynomial must not cross a declared piece boundary')
        width = r.width_box(self.eta_left, self.eta_right)
        u0 = I.exact(0.) if left == self.eta_left else I.div(r.width_box(self.eta_left, left), width)
        u1 = I.exact(1.) if right == self.eta_right else I.div(r.width_box(self.eta_left, right), width)
        controls = I.exact(np.array([0., 0., 0., 1., 1., 1.]))
        deriv = r.derivative(controls, width)
        second = r.derivative(deriv, width)
        return [r.restrict(v, u0, u1) for v in (controls, deriv, second)]

    def _reference_polynomials(self, piece):
        """One common Taylor jet; derivative polynomials formed in power form."""
        I, r, scalar = self.I, self.r, self.scalar
        left, right, _, _, _, segment = piece
        if segment['kind'] == 'old_exact_quintic':
            raise ValueError('A nonzero eta may not enter the old scalar prefix')
        anchor = self.interpolate(left, right, F(1, 2))
        a0, j0, origin = self._anchor(anchor)
        alpha, alpha_bounds = scalar.alpha_power(segment, anchor)
        sn, cs = r.sine_cosine(alpha[0])
        sine, cosine = [sn], [cs]
        n = scalar.degree
        for j in range(n-1):
            sv, cv = I.exact(0.), I.exact(0.)
            for k in range(min(j+1, len(alpha)-1)):
                coefficient = I.scale(alpha[k+1], k+1)
                sv = I.add(sv, I.mul(coefficient, cosine[j-k]))
                cv = I.sub(cv, I.mul(coefficient, sine[j-k]))
            sine.append(I.div(sv, I.exact(j+1)))
            cosine.append(I.div(cv, I.exact(j+1)))
        a_power = [a0]+[I.div(sine[j], I.exact(j+1)) for j in range(n)]
        j_power = [j0]+[I.neg(I.div(cosine[j], I.exact(j+1))) for j in range(n)]
        bell = [I.exact(1.)]
        for j in range(n):
            value = I.exact(0.)
            for k in range(min(j+1, len(alpha_bounds))):
                value = I.add(value, I.scale(I.mul(I.exact(alpha_bounds[k]), bell[j-k]), math.comb(j, k)))
            bell.append(value)
        radius = max(float(I.absolute_upper(r.width_box(anchor, edge))) for edge in (left, right))
        width, shift = r.width_box(left, right), r.width_box(anchor, left)
        all_controls = []
        for coefficients in (a_power, j_power):
            jets = []
            for order in range(3):
                powers = [I.scale(coefficients[k], math.factorial(k)//math.factorial(k-order))
                          for k in range(order, len(coefficients))]
                jets.append(scalar.power_to_piece(powers, shift, width))
            all_controls.append(jets)
        errors = [float(r.fraction(F(float(bell[n][1]))*F(radius)**(n+1-order)
                                   /math.factorial(n+1-order))[1]) for order in range(3)]
        return all_controls[0], all_controls[1], errors, dict(
            anchor_symbolic=[str(v) for v in anchor], anchor_source=origin,
            radius_upper=radius, derivative_order=n+1, derivative_bound_upper=float(bell[n][1]),
            scalar_jet_remainders=errors, scalar_degree=n, scalar_segment=segment['kind'])

    def profile_controls(self, piece, *, include_target=False):
        """Return f/h/k/z jets and errors, plus the same-g a polynomial/error.

        z=h*H+k is combined before bounds.  Every coefficient array is in
        local Bernstein coordinates.  The remainder is a uniform bound on
        THIS subpiece and the stated derivative, not a polynomial term.
        """
        I, r = self.I, self.r
        left, right, _, _, old_active, _ = piece
        old = r.lift_controls(left, right, old_active)
        oldf = [old[k] for k in ('f', 'fp', 'fpp')]
        oldh = [old[k] for k in ('chi', 'cp', 'cpp')]
        zero = I.exact(np.array([0.]))
        active = bool(self.lam and self.scalar.cmp(right, self.eta_left) > 0)
        if not active:
            f, h = oldf, oldh
            k = [zero]*3
            z = [I.mul(v, self.b.H) for v in h]
            errors_f, errors_z = [0.]*3, [0.]*3
            reference_a, reference_I, reference_errors = None, None, None
            A, ae, detail = None, None, dict(reference_active=False)
            if include_target:
                A, ae, detail = self.scalar.approximation(piece)
                detail = dict(detail, reference_active=False)
        else:
            eta = self._eta_controls(left, right)
            a, integral, errors, detail = self._reference_polynomials(piece)
            reference_a, reference_I, reference_errors = a, integral, errors
            integral_minus_H = [I.sub(integral[0], self.b.H), *integral[1:]]
            f, h, k, z, errors_f, errors_z = [], [], [], [], [], []
            lam, one = r.fraction(self.lam), r.fraction(1-self.lam)
            eta_abs = [F(float(I.absolute_upper(v).max())) for v in eta]
            for order in range(3):
                pa, pj, pz = zero, zero, zero
                for split in range(order+1):
                    factor = math.comb(order, split)
                    pa = self.add(pa, I.scale(self.product(eta[split], a[order-split]), factor))
                    pj = self.add(pj, I.scale(self.product(eta[split], integral[order-split]), factor))
                    pz = self.add(pz, I.scale(self.product(eta[split], integral_minus_H[order-split]), factor))
                f.append(self.add(I.mul(one, oldf[order]), I.mul(lam, pa)))
                h.append(self.add(I.mul(one, oldh[order]), I.mul(lam, eta[order])))
                k.append(I.neg(I.mul(lam, pj)))
                z.append(self.add(I.mul(I.mul(one, oldh[order]), self.b.H), I.neg(I.mul(lam, pz))))
                error = self.lam*sum((F(math.comb(order, split))*eta_abs[split]
                                     *F(errors[order-split]) for split in range(order+1)), F(0))
                fee = float(r.fraction(error)[1])
                errors_f.append(fee); errors_z.append(fee)
            A, ae = a[0], errors[0]
            detail = dict(detail, reference_active=True)
        for j, values in enumerate((errors_f, errors_z)):
            self.maximum_scalar_remainders[j] = np.maximum(self.maximum_scalar_remainders[j], values)
        return dict(f=[r.elevate(v, self.degree) for v in f],
            h=[r.elevate(v, self.degree) for v in h],
            k=[r.elevate(v, self.degree) for v in k],
            z=[r.elevate(v, self.degree) for v in z],
            f_error=errors_f, z_error=errors_z, k_error=errors_z,
            h_error=[0.]*3, a_poly0=A, a_error0=ae,
            reference_a_jets=reference_a, reference_I_jets=reference_I,
            reference_jet_errors=reference_errors, detail=detail)

    def _q_polynomials(self, cell):
        if self._q_cache is None or self._q_cache[0] != cell:
            r, I = self.r, self.I
            width = r.width_box(r.nodes[cell], r.nodes[cell+1])
            q = r.hermite(I.at(self.b.basejets, cell), I.at(self.b.basejets, cell+1), width)
            v = r.derivative(q, width)
            self._q_cache = cell, (q, v, r.derivative(v, width))
        return self._q_cache[1]

    def piece_definitions(self, cell, piece, mode='first'):
        b, r, I = self.b, self.r, self.I
        q, v, acc = [r.elevate(r.restrict(value, piece[2], piece[3]), self.degree)
                     for value in self._q_polynomials(cell)]
        p = self.profile_controls(piece, include_target=mode == 'metric')
        even, odd = ('cos', 'sin', 'cos'), ('sin', 'cos', 'sin')
        definitions = {}
        # Tuple: complete finite coefficients, parities, scalar polynomial,
        # analytic angular tail, physical scalar horizontal/vertical errors.
        def put(name, controls, angular_order, radial_order, C, S, tail, norm, vertical):
            channels = b.channels(controls, angular_order)
            if vertical:
                channels = b.add_z0(channels, p['z'][radial_order], I.exact(1.))
            channels = b.add_horizontal(channels, p['f'][radial_order], C, S)
            eh = float(I.mul(I.exact(p['f_error'][radial_order]), I.exact(norm))[1])
            ev = p['z_error'][radial_order] if vertical else 0.
            definitions[name] = (channels, even if angular_order % 2 == 0 else odd,
                p['f'][radial_order], tail, eh, ev)
        put('V', v, 0, 1, b.er_cos, b.er_sin, b.er_tail, 1., True)
        put('T', q, 1, 0, I.neg(b.rhoer_sin), b.rhoer_cos, b.rhoer_tail, b.rho_upper, False)
        if mode == 'first':
            put('X', q, 0, 0, b.er_cos, b.er_sin, b.er_tail, 1., True)
        if mode == 'curvature':
            put('AA', acc, 0, 2, b.er_cos, b.er_sin, b.er_tail, 1., True)
            put('VT', v, 1, 1, I.neg(b.rhoer_sin), b.rhoer_cos, b.rhoer_tail, b.rho_upper, False)
            c = self.curvature
            put('EE', q, 2, 0, c.second_cos, c.second_sin, c.second_total_tail,
                c.second_multiplier_abs_upper, False)
        return definitions, p

    def _field_batch(self, rows):
        b, I, L = self.b, self.I, self.b.low_modes
        names = list(rows[0])
        fields = {name: [None]*3 for name in names}
        groups, losses, addresses = ({'cos': [], 'sin': []} for _ in range(3))
        diagnostics = {}
        for name in names:
            definitions = [row[name] for row in rows]
            scalar = I.stack([d[2] for d in definitions])
            angular = I.mul(I.exact(I.absolute_upper(scalar)), I.exact(
                np.asarray([d[3] for d in definitions])[:, None]))[1]
            horizontal = I.add(I.exact(angular), I.exact(np.asarray([d[4] for d in definitions])[:, None]))[1]
            vertical = np.broadcast_to(np.asarray([d[5] for d in definitions])[:, None], horizontal.shape)
            diagnostics[name] = dict(remaining_finite_mode_component_upper=0.,
                complete_angular_lift_tail_component_upper=float(angular.max()),
                physical_scalar_horizontal_remainder_upper=max(d[4] for d in definitions),
                physical_scalar_vertical_remainder_upper=max(d[5] for d in definitions))
            for k, parity in enumerate(definitions[0][1]):
                coefficients = I.stack([d[0][k] for d in definitions])
                high = I.sum_upper(I.absolute_upper(I.at(coefficients, (..., slice(L+1, None)))), axis=-1)
                fee = horizontal if k < 2 else vertical
                loss = I.add(I.exact(high), I.exact(fee))[1]
                groups[parity].append(I.at(coefficients, (..., slice(0, L+1))))
                losses[parity].append(loss)
                addresses[parity].append((name, k))
                diagnostics[name]['remaining_finite_mode_component_upper'] = max(
                    diagnostics[name]['remaining_finite_mode_component_upper'], float(high.max()))
        for parity in ('cos', 'sin'):
            if not groups[parity]:
                continue
            self.maximum_transform_group_entries = max(self.maximum_transform_group_entries,
                len(groups[parity])*len(rows)*(self.degree+1)*b.angle.Q)
            values = b.angle.angle_boxes(I.stack(groups[parity]), parity)
            loss = np.asarray(losses[parity])[..., None]
            values = I.down(values[0]-loss), I.up(values[1]+loss)
            for j, (name, k) in enumerate(addresses[parity]):
                fields[name][k] = values[0][j].min(axis=-2), values[1][j].max(axis=-2)
        return fields, diagnostics

    def blocks(self, cell, radial, mode='first'):
        if not 0 <= cell < self.r.J-1 or radial < 1 or radial & (radial-1):
            raise ValueError('Use an original cell and a positive dyadic radial count')
        if mode not in ('first', 'curvature', 'metric'):
            raise ValueError('Unknown geometric consumer')
        largest_group = {'first': 5, 'curvature': 8, 'metric': 3}[mode]
        count = min(self.radial_block, max(1, (1 << 20)//(
            largest_group*(self.degree+1)*self.b.angle.Q)))
        for part, piece in enumerate(self.pieces(cell)):
            for first in range(0, radial, count):
                stop = min(radial, first+count)
                subpieces = [self.subpiece(cell, piece, j, radial) for j in range(first, stop)]
                made = [self.piece_definitions(cell, sub, mode) for sub in subpieces]
                fields, tails = self._field_batch([d[0] for d in made])
                yield dict(piece=part, first=first, stop=stop, fields=fields,
                    tails=tails, profiles=[d[1] for d in made], subpieces=subpieces)

    def _old_formula_applies(self, cell):
        return not self.lam or self.scalar.cmp(self.r.nodes[cell+1], self.eta_left) <= 0

    def _forms(self, cell, fields):
        r, I = self.r, self.I
        V, T = fields['V'], fields['T']
        N, E = r.cross(T, V), r.norm2(V)
        wa = r.norm2(N)
        wb = I.sub(I.mul(E, r.norm2(T)), I.square(r.dot(V, T)))
        W2 = np.maximum(wa[0], wb[0]), np.minimum(wa[1], wb[1])
        if self.previous is not None:
            old = self.previous[cell]
            E = np.maximum(E[0], old['minimum_E_lower']), E[1]
            W2 = np.maximum(W2[0], old['minimum_normal_squared_lower']), W2[1]
        if np.any(E[0] > E[1]) or np.any(W2[0] > W2[1]):
            raise ArithmeticError('Two same-field enclosures do not intersect')
        return N, E, W2, (E[0] > 0) & (W2[0] > 0)

    def first_cell(self, cell, radial):
        if self._old_formula_applies(cell):
            result = self.b.cell(cell, radial)
            result.update(reference_lift_active=False, current_candidate_recomputed=True)
            return result
        started = time.monotonic()
        r, I, b = self.r, self.I, self.b
        record = dict(cell=cell, angles=b.angle.Q, radial_subdivisions=radial,
            minimum_normal_squared_lower=None, minimum_E_lower=None, support_lower=None,
            maximum_radius_squared_upper=0., witness_distance_squared_lower=None,
            unpaid_immersion_boxes=0, worst_support=None, worst_witness=None)
        supports, normals, speeds, distances = [], [], [], []
        for block in self.blocks(cell, radial, 'first'):
            fields = block['fields']; X = fields['X']
            record['maximum_radius_squared_upper'] = max(record['maximum_radius_squared_upper'],
                float(r.norm2(X)[1].max()))
            for sign in (-1, 1):
                d2 = r.norm2([I.sub(X[k], I.scale(b.witness_rotating[k], sign)) for k in range(3)])[0]
                at = np.unravel_index(int(np.argmin(d2)), d2.shape)
                low = max(0., float(d2[at]))
                if not distances or low < min(distances):
                    record['worst_witness'] = dict(piece=block['piece'],
                        radial_subcell=block['first']+int(at[0]), angle_grid_index=int(at[1]), witness_sign=sign)
                distances.append(low)
            N, E, W2, good = self._forms(cell, fields)
            normals.append(float(W2[0].min())); speeds.append(float(E[0].min()))
            record['unpaid_immersion_boxes'] += int(np.count_nonzero(~good))
            if np.any(good):
                AX = [X[0], X[1], I.mul(r.fraction(b.beta), X[2])]
                numerator = r.dot(AX, N)
                support = I.div(I.at(numerator, good), I.sqrt(I.at(W2, good)))[0]
                best = float(support.min())
                if not supports or best < min(supports):
                    at = np.argwhere(good)[int(np.argmin(support))]
                    record['worst_support'] = dict(piece=block['piece'],
                        radial_subcell=block['first']+int(at[0]), angle_grid_index=int(at[1]))
                supports.append(best)
        record.update(minimum_normal_squared_lower=min(normals), minimum_E_lower=min(speeds),
            witness_distance_squared_lower=min(distances),
            support_lower=min(supports) if not record['unpaid_immersion_boxes'] else None,
            exact_lift_pieces=len(self.pieces(cell)), reference_lift_active=True,
            all_original_radial_and_angular_points_covered=True,
            full_analytic_lift_and_all_original_modes_paid=True,
            outward_arithmetic=True, seconds=time.monotonic()-started)
        return record

    def curvature_cell(self, cell, radial):
        if self._old_formula_applies(cell) and self.previous is None:
            result = self.curvature.cell(cell, radial)
            result.update(reference_lift_active=False, current_candidate_recomputed=True,
                          radial_subdivisions=radial)
            return result
        started = time.monotonic()
        r, I = self.r, self.I
        best, unpaid, worst = 0., 0, None
        normals, speeds = [], []
        for block in self.blocks(cell, radial, 'curvature'):
            fields = block['fields']
            N, E, W2, good = self._forms(cell, fields)
            normals.append(float(W2[0].min())); speeds.append(float(E[0].min()))
            unpaid += int(np.count_nonzero(~good))
            if np.any(good):
                subset = lambda v: [I.at(x, good) for x in v]
                values = self.curvature.shape_upper(*[subset(fields[key]) for key in ('V', 'T', 'AA', 'VT', 'EE')],
                    subset(N), I.at(W2, good), I.at(E, good))
                j = int(np.argmax(values)); bound = float(values[j])
                if bound > best:
                    at = np.argwhere(good)[j]
                    best = bound
                    worst = dict(piece=block['piece'], radial_subcell=block['first']+int(at[0]),
                                 angle_grid_index=int(at[1]), angle_grid_denominator=self.b.angle.Q)
        return dict(cell=cell, angles=self.b.angle.Q, retained_angle_modes=self.b.low_modes,
            radial_subdivisions=radial, radial_subdivisions_per_piece=radial,
            minimum_E_lower=min(speeds), minimum_normal_squared_lower=min(normals),
            unpaid_immersion_boxes=unpaid, curvature_upper=best if unpaid == 0 else None,
            curvature_bound_certified=unpaid == 0, worst_curvature=worst,
            reference_lift_active=not self._old_formula_applies(cell),
            actual_first_form_used=True, sampled_a_used_as_geometry=False,
            all_original_points_covered=True, full_original_modes_and_complete_analytic_lift_paid=True,
            strict_outward_arithmetic=True, seconds=time.monotonic()-started)

    def metric_cell(self, cell, radial):
        """Complete, possibly wide, direct interval relative-Gram enclosure."""
        started = time.monotonic()
        r, I, best, worst = self.r, self.I, 0., None
        minimum_a, component_max = None, [0., 0., 0.]
        unpaid = 0
        for block in self.blocks(cell, radial, 'metric'):
            fields = block['fields']; V, T = fields['V'], fields['T']
            lo, hi = [], []
            for p in block['profiles']:
                A, fee = p['a_poly0'], p['a_error0']
                box = I.add((np.asarray(A[0].min()), np.asarray(A[1].max())), (-fee, fee))
                lo.append(float(box[0])); hi.append(float(box[1]))
            a = np.asarray(lo)[:, None], np.asarray(hi)[:, None]
            minimum_a = min(lo) if minimum_a is None else min(minimum_a, min(lo))
            ar = I.mul(a, self.b.rho)
            good = (a[0] > 0) & (self.b.rho[0] > 0) & (ar[0] > 0)
            unpaid += int(np.count_nonzero(~good))
            if not np.any(good):
                continue
            e = I.sub(r.norm2(V), I.exact(1.))
            m = r.dot(V, T); g = r.norm2(T)
            entries = [I.at(e, good), I.div(I.at(m, good), I.at(ar, good)),
                I.sub(I.div(I.at(g, good), I.square(I.at(ar, good))), I.exact(1.))]
            e, m, g = entries
            bound = I.scale(I.add(I.exact(I.absolute_upper(I.add(e, g))),
                I.sqrt(I.add(I.square(I.sub(e, g)), I.scale(I.square(m), 4)))), .5)[1]
            j = int(np.argmax(bound))
            if float(bound[j]) > best:
                at = np.argwhere(good)[j]; best = float(bound[j])
                worst = dict(piece=block['piece'], radial_subcell=block['first']+int(at[0]),
                             angle_grid_index=int(at[1]))
            for k, entry in enumerate(entries):
                component_max[k] = max(component_max[k], float(I.absolute_upper(entry).max()))
        return dict(cell=cell, angles=self.b.angle.Q, radial_subdivisions=radial,
            continuous_relative_gram_operator_upper=best if unpaid == 0 else None,
            maximum_component_absolute_upper=component_max, minimum_a_lower=minimum_a,
            minimum_rho_lower=float(self.b.rho[0].min()), unpaid_target_metric_boxes=unpaid,
            worst=worst, complete_same_g=True, direct_interval_metric=True,
            R657_numerator_polynomial_cancellation_used=False, seconds=time.monotonic()-started)

    def set_resolution(self, angles, modes):
        self.curvature.set_resolution(int(angles), int(modes))

    def metadata(self):
        b, r = self.b, self.r
        inputs = dict(self.b.paths, **self.paths)
        return dict(schema=SCHEMA, source_sha256=sha(__file__),
            source_inputs={key:dict(path=str(Path(path).resolve()), sha256=sha(path)) for key, path in inputs.items()},
            model_definition=self.model, model_identity_sha256=self.model_sha,
            reference_tail_lambda=float(self.lam), exact_S_box=[str(v) for v in r.S_exact],
            exact_R_box=[str(v) for v in r.R_exact], exact_width=str(r.width),
            exact_height=str(b.height_exact), beta_exact=str(b.beta),
            witness_radius_exact=str(b.witness_radius_exact), J=r.J, M=r.M,
            scalar_taylor_degree=self.scalar.degree, maximum_polynomial_degree=self.degree,
            angular_taylor_degree=b.taylor_degree, fullhold=self.full_metadata,
            complete_angular_exponential_remainder_upper=b.taylor_remainder,
            er_laurent_tail_upper=b.er_fourier_tail, rhoer_laurent_tail_upper=b.rhoer_fourier_tail,
            second_multiplier_absolute_upper=self.curvature.second_multiplier_abs_upper,
            second_complete_angular_tail_upper=self.curvature.second_total_tail,
            integer_oracle_anchor_queries=self.oracle_anchor_queries,
            saved_reference_anchor_count=self.profile_anchor_count, cached_anchor_uses=self.saved_anchor_uses,
            maximum_physical_scalar_remainders_f_z=self.maximum_scalar_remainders.tolist(),
            maximum_transform_group_entries=self.maximum_transform_group_entries,
            exact_scalar_jets_not_obtained_by_differencing_anchor_intervals=True,
            exact_symbolic_scalar_eta_chi_piece_partition=True,
            full_original_modes_and_complete_analytic_lift_paid=True,
            old_field_certificates_inherited=False, optional_same_field_first_geometry=self.previous_identity,
            nonplanarity_certified=False, four_fixed_markers_pay_positive_Euclidean_shape_distance=False,
            marker_scope='No old polynomial-lift nonplanarity/marker certificate is reused for the analytic reference lift',
            reach_certified=False, normal_orientation='F_phi cross F_s',
            arithmetic='Original integer/Fraction oracle; outward f512 Bernstein and complete Laurent/Taylor tails')


def parse_levels(value):
    result = []
    for item in value.split(','):
        values = tuple(int(v) for v in item.split(':'))
        if len(values) != 3:
            raise argparse.ArgumentTypeError('Use angles:radial:retained_modes')
        q, radial, modes = values
        if q < 4 or q & (q-1) or radial < 1 or radial & (radial-1) or modes < 1 or q <= 4*modes:
            raise argparse.ArgumentTypeError('Use positive dyadic angles/radial and retained_modes < angles/4')
        result.append(values)
    if not result:
        raise argparse.ArgumentTypeError('At least one finite cover level is required')
    return result


def combine(reader, old, new, mode):
    if mode == 'first':
        result = reader.first.combine_cell(old, new)
        result['passes'][-1]['retained_modes'] = reader.b.low_modes
        return result
    if old is None:
        result = dict(new); result['passes'] = []
    else:
        result = dict(old)
        result['seconds'] += new['seconds']
        key = 'curvature_upper' if mode == 'curvature' else 'continuous_relative_gram_operator_upper'
        available = [v for v in (old.get(key), new.get(key)) if v is not None]
        if available:
            result[key] = min(available)
        if new.get(key) is not None and (old.get(key) is None or new[key] < old[key]):
            result['worst_curvature' if mode == 'curvature' else 'worst'] = new.get(
                'worst_curvature' if mode == 'curvature' else 'worst')
        if mode == 'curvature':
            for field in ('minimum_E_lower', 'minimum_normal_squared_lower'):
                result[field] = max(old[field], new[field])
            result['curvature_bound_certified'] = bool(result.get('curvature_upper') is not None)
            result['unpaid_immersion_boxes'] = 0 if result['curvature_bound_certified'] else new['unpaid_immersion_boxes']
        else:
            result['minimum_a_lower'] = max(old['minimum_a_lower'], new['minimum_a_lower'])
            result['minimum_rho_lower'] = max(old['minimum_rho_lower'], new['minimum_rho_lower'])
            result['unpaid_target_metric_boxes'] = 0 if result.get(key) is not None else new['unpaid_target_metric_boxes']
    result['passes'] = result['passes']+[dict(angles=new['angles'],
        radial_subdivisions=new['radial_subdivisions'], retained_modes=reader.b.low_modes)]
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('repo', 'bundle', 'node-report', 'scalar-input', 'out'):
        parser.add_argument('--'+key, type=Path, required=True)
    parser.add_argument('--reference-carrier', type=Path)
    parser.add_argument('--first-geometry-report', type=Path)
    parser.add_argument('--mode', choices=('first', 'curvature', 'metric'), default='first')
    parser.add_argument('--cells', default='all')
    parser.add_argument('--levels', type=parse_levels, default=parse_levels('256:1:24,512:2:32,1024:4:48,2048:8:64,4096:16:96'))
    parser.add_argument('--target-support', type=float, default=.14)
    parser.add_argument('--target-diameter', type=float)
    parser.add_argument('--target-curvature', type=float, default=8.1)
    parser.add_argument('--target-metric', type=float, default=1e-6)
    parser.add_argument('--angular-taylor-degree', type=int, default=12)
    parser.add_argument('--scalar-degree', type=int, default=5)
    parser.add_argument('--radial-block', type=int, default=4)
    parser.add_argument('--panels', type=int, default=128)
    parser.add_argument('--beta', default='1/4')
    args = parser.parse_args()
    first = load('execution_context', source_paths(args.repo)['first_source'], FIRST_SHA)
    execution = first.actions_context()
    if args.out.exists():
        raise FileExistsError('Use a fresh actual new-field report path')
    started = time.monotonic()
    q, _, modes = args.levels[0]
    reader = ReferenceIntervalReader(repo=args.repo, bundle=args.bundle, node_report=args.node_report,
        scalar_input=args.scalar_input, reference_carrier=args.reference_carrier,
        angles=q, low_modes=modes, angular_taylor_degree=args.angular_taylor_degree,
        scalar_degree=args.scalar_degree, radial_block=args.radial_block, panels=args.panels,
        beta=args.beta, first_geometry_report=args.first_geometry_report)
    r, I, b = reader.r, reader.I, reader.b
    cells = list(range(r.J-1)) if args.cells == 'all' else sorted(set(int(v) for v in args.cells.split(',')))
    if not cells or cells[0] < 0 or cells[-1] >= r.J-1:
        raise ValueError('Selected exact original cells are out of range')
    complete = cells == list(range(r.J-1))
    records, pending = {cell:None for cell in cells}, cells[:]
    report = dict(reader.metadata(), execution=execution, mode=args.mode,
        requested_cells=cells, refinement_plan=args.levels, covered_cells=[], records=[],
        complete_scope=False, embedding_certified=False, metric_certified=False,
        target_support=args.target_support, target_diameter=args.target_diameter,
        target_curvature=args.target_curvature, target_metric=args.target_metric)
    method = getattr(reader, args.mode+'_cell')
    def needed(row):
        if args.mode == 'first':
            return (row['support_lower'] is None or row['support_lower'] < args.target_support
                or row['minimum_normal_squared_lower'] <= 0 or row['minimum_E_lower'] <= 0
                or (args.target_diameter is not None and row['maximum_radius_squared_upper']
                    > float(F(args.target_diameter)**2/4)))
        key = 'curvature_upper' if args.mode == 'curvature' else 'continuous_relative_gram_operator_upper'
        target = args.target_curvature if args.mode == 'curvature' else args.target_metric
        return row.get(key) is None or row[key] > target
    for level, (q, radial, modes) in enumerate(args.levels):
        if not pending:
            break
        reader.set_resolution(q, modes)
        for done, cell in enumerate(pending[:], 1):
            records[cell] = combine(reader, records[cell], method(cell, radial), args.mode)
            if done % 32 == 0 or done == len(pending):
                report.update(reader.metadata())
                report.update(covered_cells=[c for c, value in records.items() if value is not None],
                    records=[v for v in records.values() if v is not None],
                    seconds=time.monotonic()-started, last_completed_level=level)
                first.write_json(args.out, report)
                first.announce(event='reference_tail_continuous_progress', mode=args.mode,
                    level=level, angles=q, radial=radial, complete_in_level=done,
                    total_in_level=len(pending), seconds=time.monotonic()-started)
        pending = [cell for cell in cells if needed(records[cell])]
    values = list(records.values())
    report.update(reader.metadata())
    report.update(complete_scope=complete, covered_cells=cells, records=values,
        remaining_below_requested_goal=pending, seconds=time.monotonic()-started,
        status='completed', historical_candidate_hash_assumed=False)
    if args.mode == 'first':
        caps = b.cap_bounds()
        paid = all(v['support_lower'] is not None and v['support_lower'] > 0
            and v['minimum_normal_squared_lower'] > 0 and v['minimum_E_lower'] > 0 for v in values)
        support = min(caps['support_lower'], *(v['support_lower'] for v in values)) if paid else None
        radius2 = max(caps['maximum_radius_squared_upper'], *(v['maximum_radius_squared_upper'] for v in values))
        distance2 = min(caps['witness_distance_squared_lower'], *(v['witness_distance_squared_lower'] for v in values))
        diameter = float(I.scale(I.sqrt(I.exact(radius2)), 2)[1])
        distance = float(I.sqrt(I.exact(max(0., distance2)))[0])
        rho = float(b.rho[0].min())
        embedding = bool(complete and paid and rho > 0 and caps['support_lower'] > 0)
        report.update(cap_bounds=caps, core_rho_continuous_lower=rho,
            covered_support_lower=support, embedding_certified=embedding,
            covered_minimum_normal_squared_lower=min(v['minimum_normal_squared_lower'] for v in values),
            covered_minimum_E_lower=min(v['minimum_E_lower'] for v in values),
            continuous_diameter_upper=diameter if complete else None,
            continuous_fixed_witness_distance_lower=distance if complete else None,
            held_amplitude_over_diameter_lower=float(I.div(I.exact(distance), I.exact(diameter))[0]) if embedding else None,
            exact_closed_caps_and_reflection_included=True,
            embedding_proof='R650 positive-flow projection and R671 exact closed C2 interfaces',
            nonplanarity_certified=False, marker_certified=False)
    elif args.mode == 'curvature':
        paid = all(v.get('curvature_upper') is not None for v in values)
        bound = max(v['curvature_upper'] for v in values) if paid else None
        report.update(covered_curvature_upper=bound, complete_body_curvature_upper=bound if complete else None,
            all_covered_curvature_paid=paid, flat_caps_curvature_upper=0.,
            reflection_preserves_absolute_principal_curvatures=True, reach_certified=False)
    else:
        paid = all(v.get('continuous_relative_gram_operator_upper') is not None for v in values)
        bound = max(v['continuous_relative_gram_operator_upper'] for v in values) if paid else None
        report.update(covered_relative_gram_operator_upper=bound,
            complete_relative_gram_operator_upper=bound if complete else None,
            requested_metric_bound_paid=bool(complete and paid and bound <= args.target_metric),
            metric_certified=bool(complete and paid and bound <= 1e-6),
            metric_bound_scope='Same fixed g on the band and its reflection; unchanged flat cap metrics are exact',
            mesh_frequency_refinement_convergence_claimed=False)
    first.write_json(args.out, report)
    first.announce(event='reference_tail_continuous_completed', mode=args.mode,
        bundle_sha256=sha(args.bundle), report_sha256=sha(args.out),
        complete_scope=complete, remaining=len(pending), seconds=report['seconds'])


if __name__ == '__main__':
    main()
