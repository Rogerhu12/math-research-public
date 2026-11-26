#!/usr/bin/env python3
"""Outward actual-node SO(3) meridian jets and complete working-value fees.

This component binds one actual complete direct-axisymmetric hDelta field.
It evaluates exact affine nodes and literal angles with integer intervals,
then compares the true jets to a fresh read by the byte-bound 7f26 operator.
It does not certify an integral, inverse chart, Gram matrix, reach or flex.
Scientific execution is restricted to the public repository Actions.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import time
import uuid
import numpy as np

SCHEMA = 'actual-node-direct-axisymmetric-SO3-outward-jets-v1'
REQUEST_SCHEMA = 'actual-node-direct-axisymmetric-SO3-literal-requests-v1'
TOPIC = 'topics/visible-flex-larger-amplitude'
CONTINUOUS_RELATIVE = 'scripts/resume_20261126/so3_axisymmetric_continuous_integrand.py'
CONTINUOUS_SHA = 'a846d373421df655da3bbba2491847b0cd016ae6db09b5d4176be227b2bc9ce6'
OPERATOR_SHA = '7f26ff35d115d6bfd748a7382e7b3eb159221cd0b12823bee8fa867dee123aaf'
REFERENCE_SHA = '4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3'
LOW_ORDER_SHA = '30ae7dc70ea836ab6f30e34b9b886f968c6e61c6646c807cd96a8611029c2636'
KEYS = ('T', 'Tp', 'Tpp', 'Ts')


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific outward nodes require this public repository Actions')


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
        allow_nan=False).encode()).hexdigest()


def file_record(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path), bytes=path.stat().st_size)


def load(name, path, expected):
    if sha(path) != expected:
        raise ValueError('Changed complete source '+str(path))
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def write_json(path, value):
    path = Path(path)
    temporary = path.with_name(path.name+'.partial')
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')
    temporary.replace(path)


def serialize(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, np.ndarray):
        return serialize(value.tolist())
    if isinstance(value, (np.integer,)):
        return int(value)
    if isinstance(value, (np.floating,)):
        if not math.isfinite(float(value)):
            raise ValueError('Do not serialize a nonfinite working value')
        return float(value)
    if isinstance(value, dict):
        return {key: serialize(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [serialize(item) for item in value]
    return value


def exact(value):
    """A float always denotes its literal binary64 value, never decimal text."""
    if isinstance(value, (float, np.floating)):
        value = float(value)
        if not math.isfinite(value):
            raise ValueError('A literal finite binary64 address is required')
        return F(value)
    return F(value)


def exact_interval(value):
    if isinstance(value, (tuple, list)):
        if len(value) != 2:
            raise ValueError('A rational interval has exactly two endpoints')
        low, high = (exact(v) for v in value)
    else:
        low = high = exact(value)
    if low > high:
        raise ValueError('Reversed rational interval')
    return low, high


def load_actual(args):
    require_actions()
    path = args.repo.resolve()/TOPIC/CONTINUOUS_RELATIVE
    module = load('_actual_outward_axis_continuous', path, CONTINUOUS_SHA)
    return module.ActualInput(args)


class IntervalSO3:
    """Exact-integer polynomial Exp and first/two-angle derivative enclosures.

    For degree L>=2, I+A_L(z)W+B_L(z)W^2 is exactly the matrix
    Taylor polynomial sum_{j=0}^L W^j/j!, not a different approximation.
    All remainder bounds use the global real-skew Frechet norm theorem.
    """
    def __init__(self, d, kernel, *, exp_order=24):
        require_actions()
        if exp_order != int(exp_order) or exp_order < 2:
            raise ValueError('The declared matrix Taylor degree must be at least two')
        self.d, self.k, self.L = d, kernel, int(exp_order)
        self.coefficient_boxes = {}
        for name, offset in (('A', 1), ('B', 2)):
            coefficients = [F((-1)**j, math.factorial(2*j+offset))
                for j in range((self.L-offset)//2+1)]
            for derivative in (0, 1, 2):
                values = [coefficients[j]*F(math.factorial(j), math.factorial(j-derivative))
                    for j in range(derivative, len(coefficients))]
                self.coefficient_boxes[(name, derivative)] = [d.box(v) for v in values]
        self.maximum_remainder = {key: F(0) for key in ('R', 'Rp', 'Rpp', 'Rs')}

    def add(self, *values):
        result = self.d.ZERO
        for value in values:
            result = self.d.add(result, value)
        return result

    def vadd(self, *vectors):
        return tuple(self.add(*(v[j] for v in vectors)) for j in range(3))

    def vscale(self, vector, rational):
        return tuple(self.d.scale(v, rational) for v in vector)

    def vmul(self, scalar, vector):
        return tuple(self.d.mul(scalar, v) for v in vector)

    def dot(self, a, b):
        return self.add(*(self.d.mul(x, y) for x, y in zip(a, b)))

    def square(self, value):
        low, high = value
        upper = max(low*low, high*high)
        lower = 0 if low <= 0 <= high else min(low*low, high*high)
        return lower//self.d.SCALE, -((-upper)//self.d.SCALE)

    def cross(self, a, b):
        d = self.d
        return (d.sub(d.mul(a[1], b[2]), d.mul(a[2], b[1])),
            d.sub(d.mul(a[2], b[0]), d.mul(a[0], b[2])),
            d.sub(d.mul(a[0], b[1]), d.mul(a[1], b[0])))

    def norm(self, vector):
        return self.k.sqrt_upper(sum((self.d.magnitude(v)**2 for v in vector), F(0)))

    def polynomial(self, coefficients, z):
        result = self.d.ZERO
        for coefficient in reversed(coefficients):
            result = self.d.add(self.d.mul(result, z), coefficient)
        return result

    def coefficients(self, w):
        z = self.add(*(self.square(v) for v in w))
        return {key: self.polynomial(value, z) for key, value in self.coefficient_boxes.items()}

    def remainder(self, w, wp, wpp, directions):
        r, rp, rpp = self.norm(w), self.norm(wp), self.norm(wpp)
        L = self.L
        e0 = r**(L+1)/math.factorial(L+1)
        e1 = rp*r**L/math.factorial(L)
        e2 = rpp*r**L/math.factorial(L)+rp**2*r**(L-1)/math.factorial(L-1)
        ed = {key: self.norm(value)*r**L/math.factorial(L) for key, value in directions.items()}
        self.maximum_remainder['R'] = max(self.maximum_remainder['R'], e0)
        self.maximum_remainder['Rp'] = max(self.maximum_remainder['Rp'], e1)
        self.maximum_remainder['Rpp'] = max(self.maximum_remainder['Rpp'], e2)
        if 's' in ed:
            self.maximum_remainder['Rs'] = max(self.maximum_remainder['Rs'], ed['s'])
        return dict(R=e0, Rp=e1, Rpp=e2, DR=ed)

    def expand(self, vector, error):
        extra = self.d.box(-error, error)
        return tuple(self.d.add(v, extra) for v in vector)

    def meridian_jets(self, w, wp, wpp, ws, U, Up, Upp, Us, *, unit_U=False):
        """All vectors are three component boxes; returns true T/Tp/Tpp/Ts."""
        d = self.d
        zero = (d.ZERO,)*3
        if all(vector == zero for vector in (w, wp, wpp, ws)):
            return dict(T=U, Tp=Up, Tpp=Upp, Ts=Us), dict(
                R=F(0), Rp=F(0), Rpp=F(0), DR={'s': F(0)},
                T=F(0), Tp=F(0), Tpp=F(0), Ts=F(0))
        coefficients = self.coefficients(w)
        A, B = coefficients[('A', 0)], coefficients[('B', 0)]
        Az, Bz = coefficients[('A', 1)], coefficients[('B', 1)]
        Azz, Bzz = coefficients[('A', 2)], coefficients[('B', 2)]
        zp = d.scale(self.dot(w, wp), 2)
        zpp = d.scale(self.add(self.dot(wp, wp), self.dot(w, wpp)), 2)
        zs = d.scale(self.dot(w, ws), 2)
        Ap, Bp = d.mul(Az, zp), d.mul(Bz, zp)
        App = self.add(d.mul(Azz, self.square(zp)), d.mul(Az, zpp))
        Bpp = self.add(d.mul(Bzz, self.square(zp)), d.mul(Bz, zpp))
        As, Bs = d.mul(Az, zs), d.mul(Bz, zs)
        V = self.cross(w, U)
        Vp = self.vadd(self.cross(wp, U), self.cross(w, Up))
        Vpp = self.vadd(self.cross(wpp, U), self.vscale(self.cross(wp, Up), 2), self.cross(w, Upp))
        Vs = self.vadd(self.cross(ws, U), self.cross(w, Us))
        Z = self.cross(w, V)
        Zp = self.vadd(self.cross(wp, V), self.cross(w, Vp))
        Zpp = self.vadd(self.cross(wpp, V), self.vscale(self.cross(wp, Vp), 2), self.cross(w, Vpp))
        Zs = self.vadd(self.cross(ws, V), self.cross(w, Vs))
        polynomial = dict(
            T=self.vadd(U, self.vmul(A, V), self.vmul(B, Z)),
            Tp=self.vadd(Up, self.vmul(Ap, V), self.vmul(A, Vp), self.vmul(Bp, Z), self.vmul(B, Zp)),
            Tpp=self.vadd(Upp, self.vmul(App, V), self.vscale(self.vmul(Ap, Vp), 2),
                self.vmul(A, Vpp), self.vmul(Bpp, Z), self.vscale(self.vmul(Bp, Zp), 2),
                self.vmul(B, Zpp)),
            Ts=self.vadd(Us, self.vmul(As, V), self.vmul(A, Vs), self.vmul(Bs, Z), self.vmul(B, Zs)))
        remainder = self.remainder(w, wp, wpp, {'s': ws})
        u0 = F(1) if unit_U else self.norm(U)
        u1, u2, us = self.norm(Up), self.norm(Upp), self.norm(Us)
        fees = dict(T=remainder['R']*u0,
            Tp=remainder['Rp']*u0+remainder['R']*u1,
            Tpp=remainder['Rpp']*u0+2*remainder['Rp']*u1+remainder['R']*u2,
            Ts=remainder['DR']['s']*u0+remainder['R']*us)
        return {key: self.expand(polynomial[key], fees[key]) for key in KEYS}, dict(remainder, **fees)

    def rotation_jets(self, w, wp=None, wpp=None, *, directions=None):
        """R, R_phi, R_phiphi and named DExp([w]x)[[direction]x].

        Directions may be entire real interval boxes.  No root center or
        pointwise small-angle assumption is made.  These matrices can be
        used by a separately bound zero-closure endpoint consumer.
        """
        d = self.d
        zero = (d.ZERO,)*3
        wp = zero if wp is None else tuple(wp)
        wpp = zero if wpp is None else tuple(wpp)
        directions = {} if directions is None else dict(directions)
        columns = {key: [] for key in ('R', 'Rp', 'Rpp')}
        directional_columns = {key: [] for key in directions}
        for column in range(3):
            U = tuple(d.ONE if j == column else d.ZERO for j in range(3))
            result, _ = self.meridian_jets(tuple(w), wp, wpp, zero, U, zero, zero, zero, unit_U=True)
            for key, jet in (('R', 'T'), ('Rp', 'Tp'), ('Rpp', 'Tpp')):
                columns[key].append(result[jet])
            for name, direction in directions.items():
                answer, _ = self.meridian_jets(tuple(w), zero, zero, tuple(direction),
                    U, zero, zero, zero, unit_U=True)
                directional_columns[name].append(answer['Ts'])
        transpose = lambda values: tuple(tuple(values[j][i] for j in range(3)) for i in range(3))
        return {key: transpose(value) for key, value in columns.items()} | {
            'DR': {key: transpose(value) for key, value in directional_columns.items()},
            'operator_norm_remainder_upper': self.remainder(tuple(w), wp, wpp, directions)}


class NodeOutwardEvaluator:
    """Exact-node true boxes plus a fresh complete working-operator read.

    Public q and x are the byte-bound same-field numerical operator and
    full saved free vector.  evaluate returns arrays in (P,A,3) order:
      working[key]: float64;
      intervals[key]: (lower,upper), each object array of SCALE integers;
      component_error_upper[key]: exact Fraction object array;
      norm_error_upper[key]: exact Fraction object array in (P,A).
    """
    def __init__(self, actual, *, working_cache_directory, exp_order=24):
        require_actions()
        module = sys.modules.get(actual.__class__.__module__)
        if module is None or sha(module.__file__) != CONTINUOUS_SHA:
            raise ValueError('Use the complete independently bound a846 ActualInput')
        self.actual, self.continuous = actual, module
        self.d, self.kernel = actual.context.modules['deep_scalar'], actual.kernel
        if (sha(actual.paths['operator']) != OPERATOR_SHA
                or sha(actual.paths['reference']) != REFERENCE_SHA
                or sha(actual.paths['low_order']) != LOW_ORDER_SHA):
            raise ValueError('Changed complete actual operator/reference/error kernel')
        self.scalar = module.ScalarWholeInterval(actual)
        self.omega = module.ExactOmegaBounds(actual, self.scalar)
        self.omega.omega = np.array(actual.omega, copy=True)
        self.omega.omega.setflags(write=False)
        self.fixed_chart_core = np.array(actual.context.core, copy=True)
        self.fixed_chart_core.setflags(write=False)
        self.rotation = IntervalSO3(self.d, self.kernel, exp_order=exp_order)
        self.operator_module = op = module.load('_actual_node_axis_operator',
            actual.paths['operator'], OPERATOR_SHA)
        working = actual.report['working_evaluation']
        order = int(working['integration_order'])
        if (int(actual.data['working_integration_order']) != order
                or int(actual.data['working_full_angles']) != int(actual.report['N'])):
            raise ValueError('The saved numerical integration/grid settings differ from the actual report')
        parent, prepared = actual.context.create_problem(N=int(actual.report['N']), stage_block=64)
        self.q = q = op.ClosedMeridianOperator(parent, prepared, actual.reference,
            cache_directory=working_cache_directory, integration_order=order,
            angle_block=int(working['angle_block']),
            root_iterations=int(working['inverse_root_iterations']),
            root_tolerance=float(working['inverse_root_tolerance']),
            expected_parent_bundle_sha256=actual.inputs['reference_bundle']['sha256'])
        if q.model != actual.model or q.identity != actual.identity:
            raise ValueError('The reconstructed complete numerical operator changed the mathematical field')
        self.x = q.load_checkpoint(actual.inputs['checkpoint']['path'])
        self.x.setflags(write=False)
        core, jets, height = q.unpack(self.x)
        if (not np.array_equal(core, actual.data['core'])
                or not np.array_equal(jets, actual.omega) or height != float(actual.data['Hcap'])):
            raise ValueError('Reconstruction changed current full core/omega/H words')
        self._tensor_x = op.tensor(self.x)
        self._torch_core, self._torch_jets, self._torch_height = q._unpack_torch(self._tensor_x)
        self._working_angle_key, self._working_angular_nodes = None, None
        self._chart_cache = {}
        self._angle_cache = {}
        self._fourier_cache = {}
        self._algebra_cell = None
        self._radial_cache = {}
        self.counts = dict(evaluate_calls=0, requested_node_vectors=0,
            working_meridian_calls=0, working_node_vectors=0, outward_node_vectors=0,
            scalar_point_enclosures=0, exact_Fourier_cell_angle_blocks=0,
            all_mode_terms_enclosed=0, fixed_chart_enclosures=0,
            full_F_reads=0, full_J_reads=0, full_Jtranspose_reads=0)
        self.maximum_errors = {key: F(0) for key in KEYS}
        self.last_query = None
        self.binding = dict(schema=SCHEMA, actual=actual.binding,
            source_sha256=sha(__file__), continuous_input_source_sha256=CONTINUOUS_SHA,
            operator_source_sha256=OPERATOR_SHA, reference_source_sha256=REFERENCE_SHA,
            low_order_source_sha256=LOW_ORDER_SHA,
            mathematical_integrand='T=Exp([omega]cross)*(b er(theta0)+c ez)',
            exact_scalar_has_b_squared_plus_c_squared_one=True,
            local_coordinate_semantics='exact affine cell plus literal binary64 u; working cell width is a carrier',
            angular_coordinate_semantics='literal phi in the fixed original theta0 chart',
            numeric_read_semantics='fresh complete 7f26 read; not an assertion about a previous BLAS batch or cache',
            component_interval_scale=str(self.d.SCALE), exp_order=int(exp_order),
            working_settings=working, working_runtime_torch_version=op.torch.__version__,
            working_runtime_numpy_version=np.__version__,
            working_stage_block_for_unused_full_field_interface=64,
            evaluation_angles_can_have_arbitrary_literal_values=True,
            scalar_and_fixed_chart_sources_bound_by_actual=True,
            full_F_J_recomputed_by_this_component=False)

    def rational_box(self, value):
        low, high = exact_interval(value)
        return self.d.box(low, high)

    def normal_frame(self, phi):
        box = self.rational_box(phi)
        sine, cosine = self.d.sine_cosine(box)
        return dict(phi=box, er=(cosine, sine, self.d.ZERO),
            et=(self.d.neg(sine), cosine, self.d.ZERO))

    def chart_for_core(self, core, phi):
        """The exact Theta/rho/rho' of any supplied literal complete core."""
        d = self.d
        core = np.asarray(core)
        if core.shape != (self.actual.M,) or not np.isfinite(core.astype(float)).all():
            raise ValueError('Use a complete finite core coefficient vector')
        theta, rho, rhop = self.rational_box(phi), d.ONE, d.ZERO
        for m, coefficient in enumerate(core, 1):
            coefficient = exact(coefficient)
            if coefficient == 0:
                continue
            nu = 2*m
            sine, cosine = d.sine_cosine(d.scale(self.rational_box(phi), nu))
            q = 1-nu*nu
            theta = d.add(theta, d.scale(sine, F(q, nu)*coefficient))
            rho = d.add(rho, d.scale(cosine, q*coefficient))
            rhop = d.add(rhop, d.scale(sine, -nu*q*coefficient))
        sine, cosine = d.sine_cosine(theta)
        return dict(phi=self.rational_box(phi), theta=theta, rho=rho, rho_phi=rhop,
            er=(cosine, sine, d.ZERO), et=(d.neg(sine), cosine, d.ZERO))

    def fixed_chart(self, phi):
        key = exact_interval(phi)
        if key not in self._chart_cache:
            self._chart_cache[key] = self.chart_for_core(self.fixed_chart_core, key)
            self.counts['fixed_chart_enclosures'] += 1
        return self._chart_cache[key]

    def _angular_basis(self, phi):
        key = exact_interval(phi)
        if key in self._angle_cache:
            return self._angle_cache[key]
        d = self.d
        base = self.rational_box(key)
        trigonometric = {}
        answer = []
        for channel, frequency in zip(self.omega.channels, self.omega.frequencies):
            if frequency not in trigonometric:
                trigonometric[frequency] = d.sine_cosine(d.scale(base, frequency))
            sine, cosine = trigonometric[frequency]
            if channel == 1:
                answer.append((cosine, d.scale(sine, -frequency), d.scale(cosine, -frequency**2)))
            else:
                answer.append((sine, d.scale(cosine, frequency), d.scale(sine, -frequency**2)))
        self._angle_cache[key] = answer
        return answer

    def _fourier_power(self, cell, phi):
        """Sum all literal Fourier modes before the radial Horner evaluation."""
        phi_key = exact_interval(phi)
        cache_key = (int(cell), phi_key)
        if cache_key in self._fourier_cache:
            return self._fourier_cache[cache_key]
        d = self.d
        if self._algebra_cell != int(cell):
            self.omega.prepared_cells.clear()
            self._fourier_cache.clear()
            self._algebra_cell = int(cell)
        width, polynomials = self.omega.prepare_cell(int(cell))
        basis = self._angular_basis(phi_key)
        result = [[[d.ZERO for _ in range(6)] for _ in range(3)] for _ in range(3)]
        for mode, polynomial in enumerate(polynomials):
            if polynomial is None:
                continue
            channel = self.omega.channels[mode]
            for angular in (0, 1, 2):
                factor = basis[mode][angular]
                for power, coefficient in enumerate(polynomial[0]):
                    result[angular][channel][power] = d.add(result[angular][channel][power],
                        d.mul(coefficient, factor))
            self.counts['all_mode_terms_enclosed'] += 1
        self._fourier_cache[cache_key] = (width, result)
        self.counts['exact_Fourier_cell_angle_blocks'] += 1
        return width, result

    def _point_polynomial(self, coefficients, local):
        result = self.d.ZERO
        for coefficient in reversed(coefficients):
            result = self.d.add(self.d.scale(result, local), coefficient)
        return result

    def _scalar_point(self, cell, local):
        key = int(cell), exact(local)
        if key not in self._radial_cache:
            definition = self.continuous.affine(self.actual.context.nodes, key[0], key[1])
            self._radial_cache[key] = (definition, self.actual.context.law.boxes(definition))
            self.counts['scalar_point_enclosures'] += 1
        return self._radial_cache[key]

    def enclose_node(self, cell, local_u, phi):
        """Pure true-node enclosure; phi may also be an entire rational interval."""
        require_actions()
        if cell != int(cell):
            raise ValueError('The exact node needs an integer original cell address')
        cell, local = int(cell), exact(local_u)
        if not 0 <= cell < self.actual.J-1 or not 0 <= local <= 1:
            raise ValueError('The true node must lie on an actual exact affine cell')
        d, r = self.d, self.rotation
        width, powers = self._fourier_power(cell, phi)
        values = [tuple(self._point_polynomial(powers[angular][channel], local)
            for channel in range(3)) for angular in (0, 1, 2)]
        inverse = d.inverse(width)
        ws = tuple(d.mul(self._point_polynomial(
            [d.scale(powers[0][channel][j+1], j+1) for j in range(5)], local), inverse)
            for channel in range(3))
        w, wp, wpp = values
        definition, (b, c, bs, cs) = self._scalar_point(cell, local)
        chart = self.fixed_chart(phi)
        er, et, rho, rhop = chart['er'], chart['et'], chart['rho'], chart['rho_phi']
        ez = (d.ZERO, d.ZERO, d.ONE)
        U = r.vadd(r.vmul(b, er), r.vmul(c, ez))
        Us = r.vadd(r.vmul(bs, er), r.vmul(cs, ez))
        Up = r.vmul(d.mul(b, rho), et)
        Upp = r.vmul(b, r.vadd(r.vmul(rhop, et), r.vmul(d.neg(r.square(rho)), er)))
        vectors, remainder = r.meridian_jets(w, wp, wpp, ws, U, Up, Upp, Us, unit_U=True)
        self.counts['outward_node_vectors'] += 1
        return dict(intervals=vectors,
            omega=dict(value=w, phi=wp, phiphi=wpp, s=ws),
            T0=dict(value=U, phi=Up, phiphi=Upp, s=Us),
            scalar_boxes=dict(b=b, c=c, bs=bs, cs=cs), chart=chart,
            exact_affine_node=definition, exact_physical_s_box=self.scalar.exact_affine_box(definition),
            exact_physical_width_box=width, exp_remainder_upper=remainder)

    @staticmethod
    def _literal_arrays(cells, local_u, phi):
        raw_cells = np.asarray(cells)
        if (raw_cells.ndim != 1 or not len(raw_cells)
                or not np.issubdtype(raw_cells.dtype, np.integer)):
            raise ValueError('Cells must be a nonempty one-dimensional integer array')
        cells = np.asarray(raw_cells, dtype=np.int64)
        local = np.asarray(local_u, dtype=np.float64)
        angles = np.asarray(phi, dtype=np.float64)
        if (local.shape != cells.shape or angles.ndim != 1 or not len(angles)
                or not np.isfinite(local).all() or not np.isfinite(angles).all()):
            raise ValueError('Use matching finite literal u and a nonempty finite literal angle vector')
        return cells, local, angles

    def working(self, cells, local_u, phi):
        """A fresh complete source read; this never calls numerical F or J."""
        require_actions()
        cells, local, angles = self._literal_arrays(cells, local_u, phi)
        q, op = self.q, self.operator_module
        query = q.make_query(cells, local)
        angle_key = tuple(float(v).hex() for v in angles)
        if angle_key != self._working_angle_key:
            with op.torch.no_grad():
                self._working_angular_nodes = tuple(q._angular_nodes(self._torch_jets, angles, order)
                    for order in (0, 1, 2))
            self._working_angle_key = angle_key
        with op.torch.no_grad():
            answer = q._meridians(*self._working_angular_nodes, query, angles, 'arbitrary', True)
        working = {key: np.array(answer[key].detach().numpy(), dtype=np.float64, copy=True) for key in KEYS}
        if any(value.shape != (len(cells), len(angles), 3) or not np.isfinite(value).all()
                for value in working.values()):
            raise FloatingPointError('The actual numerical meridian jets must all be finite with full shape')
        self.counts['working_meridian_calls'] += 1
        self.counts['working_node_vectors'] += len(cells)*len(angles)
        self.last_query = query
        return dict(working=working, query=query, cells=cells, local_u=local, phi=angles,
            operation='actual same-source arbitrary-label meridian read; not a stored old working cache')

    def evaluate(self, cells, local_u, phi):
        require_actions()
        actual = self.working(cells, local_u, phi)
        cells, local, angles = actual['cells'], actual['local_u'], actual['phi']
        shape = (len(cells), len(angles), 3)
        intervals = {key: (np.empty(shape, dtype=object), np.empty(shape, dtype=object)) for key in KEYS}
        errors = {key: np.empty(shape, dtype=object) for key in KEYS}
        norms = {key: np.empty(shape[:2], dtype=object) for key in KEYS}
        exp_remainders = {key: np.empty(shape[:2], dtype=object) for key in KEYS}
        radial_records = []
        for p, (cell, u) in enumerate(zip(cells, local)):
            cell, u = int(cell), float(u)
            definition, _ = self._scalar_point(cell, F(u))
            sbox = self.scalar.exact_affine_box(definition)
            width = self.scalar.width_box(self.actual.context.nodes[cell], self.actual.context.nodes[cell+1])
            swork, wwork = float(actual['query']['s'][p]), float(actual['query']['widths'][p])
            radial_records.append(dict(cell=cell, local_u_hex=u.hex(),
                exact_local_u=F(u), exact_affine_node=definition,
                exact_physical_s_box=sbox, actual_working_s_hex=swork.hex(),
                actual_working_s_error_upper=max(abs(F(sbox[0], self.d.SCALE)-F(swork)),
                    abs(F(sbox[1], self.d.SCALE)-F(swork))),
                exact_physical_width_box=width, actual_working_width_hex=wwork.hex(),
                actual_working_width_error_upper=max(abs(F(width[0], self.d.SCALE)-F(wwork)),
                    abs(F(width[1], self.d.SCALE)-F(wwork)))))
            for a, phi_value in enumerate(angles):
                node = self.enclose_node(cell, F(u), F(float(phi_value)))
                for key in KEYS:
                    component = []
                    for j, box in enumerate(node['intervals'][key]):
                        intervals[key][0][p, a, j], intervals[key][1][p, a, j] = box
                        word = F(float(actual['working'][key][p, a, j]))
                        error = max(abs(F(box[0], self.d.SCALE)-word), abs(F(box[1], self.d.SCALE)-word))
                        errors[key][p, a, j] = error
                        component.append(error)
                    norms[key][p, a] = self.kernel.sqrt_upper(sum(v*v for v in component))
                    self.maximum_errors[key] = max(self.maximum_errors[key], norms[key][p, a])
                    exp_remainders[key][p, a] = node['exp_remainder_upper'][key]
        self.counts['evaluate_calls'] += 1
        self.counts['requested_node_vectors'] += len(cells)*len(angles)
        return dict(working=actual['working'], intervals=intervals,
            component_error_upper=errors, norm_error_upper=norms,
            exp_remainder_upper=exp_remainders, query=actual['query'],
            cells=cells, local_u=local, phi=angles, radial_addresses=radial_records,
            phi_hex=[float(v).hex() for v in angles], component_interval_scale=self.d.SCALE,
            shape=shape, binding_identity_sha256=canonical(self.binding),
            working_source_sha256=OPERATOR_SHA,
            all_node_evaluation_errors_included=True,
            paid_errors=['exact width versus numerical Hermite width', 'fixed chart and every finite Fourier mode',
                'actual scalar reference carrier and normalization', 'trigonometry and rotation polynomial/branch',
                'actual vector arithmetic and summation in these meridian jets'],
            no_integral_root_Gram_or_geometry_certificate=True)

    def release_algebra_cache(self, *, include_radial=False):
        """Replaceable query cache only; no scientific history/address is lost."""
        self.omega.prepared_cells.clear()
        self._fourier_cache.clear()
        if include_radial:
            self._radial_cache.clear()
        self._algebra_cell = None

    def metadata(self):
        return dict(binding=self.binding, binding_identity_sha256=canonical(self.binding),
            actual_counts=dict(self.counts), actual_counts_are_this_execution_only=True,
            maximum_node_norm_error_upper=serialize(self.maximum_errors),
            maximum_rotation_operator_remainder_upper=serialize(self.rotation.maximum_remainder),
            working_operator_actual_counts=dict(self.q.counts),
            exact_underlying_unit_T0_not_numerical_normalization_claim=True,
            complete_node_error_paid_by_true_box_to_actual_word=True,
            query_scope_is_finite_nodes_not_whole_surface=True,
            quadrature_and_complete_field_arithmetic_not_in_this_component=True,
            inverse_chart_root_and_cap_error_not_in_this_component=True,
            continuous_metric_or_reach_certified=False, closed_isometry_accepted=False)


def literal_float(word):
    if not isinstance(word, str):
        raise ValueError('Persisted numerical addresses use explicit Python binary64 hex strings')
    value = float.fromhex(word)
    if not math.isfinite(value) or value.hex() != word:
        raise ValueError('A canonical finite binary64 hex address is required')
    return value


def query_plan(evaluator, requests=None):
    """Every default original integration/observation address, without a sample cap."""
    q = evaluator.q
    if requests is not None:
        payload = json.loads(Path(requests).read_text())
        if payload.get('schema') != REQUEST_SCHEMA or not isinstance(payload.get('blocks'), list):
            raise ValueError('Use the explicit literal-node request schema')
        blocks = []
        for item in payload['blocks']:
            cells = np.asarray(item['cells'])
            local = np.array([literal_float(v) for v in item['local_u_hex']], dtype=np.float64)
            phi = np.array([literal_float(v) for v in item['phi_hex']], dtype=np.float64)
            cells, local, phi = evaluator._literal_arrays(cells, local, phi)
            if (np.any(cells < 0) or np.any(cells >= q.J-1) or np.any(local < 0) or np.any(local > 1)):
                raise ValueError('A requested literal node lies outside the actual complete domain')
            blocks.append((cells, local, phi))
        if not blocks:
            raise ValueError('There must be at least one actual node block')
        definition = dict(kind='explicit_complete_requested_blocks',
            request_file=file_record(requests), requested_blocks=len(blocks),
            requested_node_vectors=sum(len(c)*len(p) for c, u, p in blocks),
            original_full_grid_coverage_not_assumed=True)
        return blocks, definition
    locals_by_cell = []
    for cell in range(q.J-1):
        seen = set()
        values = []
        for value in list(q.gauss_u)+list(q.observation_u[q.observation_cells == cell]):
            value = float(value)
            if value.hex() not in seen:
                seen.add(value.hex())
                values.append(value)
        locals_by_cell.append(values)
    radial_blocks = [(np.full(len(local), cell, dtype=np.int64),
        np.array(local, dtype=np.float64)) for cell, local in enumerate(locals_by_cell)]
    blocks = []
    # One angular-node tensor contains every radial node.  Keep an angle
    # block fixed while visiting all cells, so the true working cache is
    # reused instead of recomputing the full J-by-mode contraction per cell.
    for first in range(0, len(q.phi), q.angle_block):
        phi = np.array(q.phi[first:first+q.angle_block], copy=True)
        for cells, local in radial_blocks:
            blocks.append((cells, local, phi))
    definition = dict(kind='all_original_working_integration_and_observation_nodes',
        traversal_order='angle_block_major_then_original_cell_order',
        exact_duplicate_binary_addresses_evaluated_once=True,
        radial_local_u_hex_by_cell=[[float(v).hex() for v in row] for row in locals_by_cell],
        phi_hex=[float(v).hex() for v in q.phi], actual_angle_block=q.angle_block,
        original_integration_order=q.integration_order, original_full_angles=q.full_N,
        requested_blocks=len(blocks), requested_node_vectors=sum(len(c)*len(p) for c, u, p in blocks),
        all_required_original_quadrature_and_observation_addresses_included=True,
        finite_address_coverage_is_not_a_continuous_surface_certificate=True)
    return blocks, definition


def batch_record(evaluator, result, index, raw_directory=None):
    serial = serialize({key: value for key, value in result.items() if key != 'query'})
    raw = json.dumps(serial, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()
    record = dict(block=index, node_vectors=int(result['shape'][0]*result['shape'][1]),
        radial_addresses=serial['radial_addresses'], phi_hex=serial['phi_hex'],
        complete_returned_node_payload_sha256=hashlib.sha256(raw).hexdigest(),
        complete_returned_node_payload_bytes=len(raw), maxima={}, maximum_locations={},
        working_array_sha256={key: evaluator.continuous.array_sha(result['working'][key]) for key in KEYS},
        raw_node_record=None)
    for key in KEYS:
        fees = result['norm_error_upper'][key]
        flat = max(range(fees.size), key=lambda j: fees.flat[j])
        p, a = np.unravel_index(flat, fees.shape)
        record['maxima'][key] = str(fees[p, a])
        record['maximum_locations'][key] = dict(cell=int(result['cells'][p]),
            local_u_hex=float(result['local_u'][p]).hex(), phi_hex=float(result['phi'][a]).hex())
    if raw_directory is not None:
        path = Path(raw_directory)/('block-'+str(index).zfill(7)+'.json.gz')
        if path.exists():
            raise ValueError('Never overwrite a completed raw node record')
        temporary = path.with_name(path.name+'.partial')
        temporary.write_bytes(gzip.compress(raw, compresslevel=6, mtime=0))
        temporary.replace(path)
        record['raw_node_record'] = file_record(path)
    return record


def main(args):
    require_actions()
    started = time.monotonic()
    actual = load_actual(args)
    cache = args.outdir.parent/(args.outdir.name+'-working-cache-'+uuid.uuid4().hex)
    evaluator = NodeOutwardEvaluator(actual, working_cache_directory=cache, exp_order=args.exp_order)
    blocks, plan = query_plan(evaluator, args.requests)
    identity = dict(schema=SCHEMA, source_sha256=sha(__file__),
        evaluator_binding_identity_sha256=canonical(evaluator.binding),
        actual_field_identity_sha256=actual.identity, actual_checkpoint_sha256=actual.inputs['checkpoint']['sha256'],
        actual_selected_state=args.state, query_plan_sha256=canonical(plan), exp_order=args.exp_order,
        write_node_records=args.write_node_records)
    identity_sha = canonical(identity)
    report_path, journal = args.outdir/'report.json', args.outdir/'node-blocks.jsonl'
    complete_blocks, chain, vectors = 0, identity_sha, 0
    maxima = {key: F(0) for key in KEYS}
    if args.outdir.exists():
        if not args.resume or not report_path.is_file() or not journal.is_file():
            raise ValueError('Existing output needs its explicit bound natural journal resume')
        prior = json.loads(report_path.read_text())
        if prior.get('identity') != identity or prior.get('query_plan') != plan:
            raise ValueError('Do not resume another actual state, source, query plan or arithmetic degree')
        for line in journal.read_text().splitlines():
            entry = json.loads(line)
            record = entry['record']
            if record['block'] != complete_blocks or entry['previous_record_identity_sha256'] != chain:
                raise ValueError('The exact-node journal has a missing or reordered block')
            if entry['record_identity_sha256'] != canonical(dict(previous=chain, record=record)):
                raise ValueError('A persisted full node block record changed')
            if record.get('raw_node_record') is not None:
                raw = record['raw_node_record']
                if sha(raw['path']) != raw['sha256']:
                    raise ValueError('A persisted raw node record changed')
            chain = entry['record_identity_sha256']
            complete_blocks += 1
            vectors += int(record['node_vectors'])
            for key in KEYS:
                maxima[key] = max(maxima[key], F(record['maxima'][key]))
        if complete_blocks > len(blocks):
            raise ValueError('The journal exceeds this exact query plan')
    else:
        if args.resume:
            raise ValueError('A resume requires an existing complete output identity')
        args.outdir.mkdir(parents=True)
        journal.write_text('')
    raw_directory = args.outdir/'raw-node-records' if args.write_node_records else None
    if raw_directory is not None:
        raw_directory.mkdir(exist_ok=True)
    source_commit = subprocess.check_output(['git', '-C', str(args.repo), 'rev-parse', 'HEAD'],
        text=True).strip()
    initial_blocks = complete_blocks
    failure = None

    def save():
        complete = complete_blocks == len(blocks) and failure is None
        report = dict(schema=SCHEMA, source_sha256=sha(__file__), source_commit=source_commit,
            identity=identity, identity_sha256=identity_sha, query_plan=plan,
            actual_binding=actual.binding, node_evaluator=evaluator.metadata(),
            complete=complete, complete_requested_finite_nodes=complete,
            completed_blocks=complete_blocks, requested_blocks=len(blocks),
            completed_node_vectors=vectors, requested_node_vectors=plan['requested_node_vectors'],
            processed_node_maxima=serialize(maxima),
            requested_scope_maxima=serialize(maxima) if complete else None,
            unprocessed_blocks_not_promoted_to_full_scope=not complete,
            journal=file_record(journal), journal_chain_sha256=chain,
            newly_completed_blocks=complete_blocks-initial_blocks,
            actual_seconds=time.monotonic()-started, admission_seconds=args.admission_seconds,
            current_execution_working_cache_path=str(cache), failure=failure,
            processed_node_rounding_and_carrier_fees_paid=True,
            previous_solver_values_not_assumed_bitwise_reproduced=True,
            scientific_full_F_or_J_recomputed=False,
            integrals_and_closed_field_arithmetic_certified=False,
            inverse_chart_or_cap_certified=False,
            continuous_metric_or_geometry_certified=False, closed_isometry_accepted=False,
            execution=dict(repository=os.environ['GITHUB_REPOSITORY'],
                run_id=os.environ.get('GITHUB_RUN_ID'), attempt=os.environ.get('GITHUB_RUN_ATTEMPT')))
        write_json(report_path, report)
        return report

    save()
    try:
        while complete_blocks < len(blocks):
            if time.monotonic()-started >= args.admission_seconds and complete_blocks > initial_blocks:
                break
            block_started = time.monotonic()
            cells, local, phi = blocks[complete_blocks]
            result = evaluator.evaluate(cells, local, phi)
            record = batch_record(evaluator, result, complete_blocks, raw_directory)
            next_chain = canonical(dict(previous=chain, record=record))
            with journal.open('a') as stream:
                stream.write(json.dumps(dict(previous_record_identity_sha256=chain,
                    record_identity_sha256=next_chain, record=record),
                    separators=(',', ':'), allow_nan=False)+'\n')
                stream.flush()
                os.fsync(stream.fileno())
            chain = next_chain
            vectors += record['node_vectors']
            for key in KEYS:
                maxima[key] = max(maxima[key], F(record['maxima'][key]))
            complete_blocks += 1
            save()
            print(json.dumps(dict(event='actual_outward_meridian_node_block',
                completed_blocks=complete_blocks, requested_blocks=len(blocks),
                block_node_vectors=record['node_vectors'], block_seconds=time.monotonic()-block_started,
                maxima=record['maxima']), separators=(',', ':'), allow_nan=False), flush=True)
    except Exception as exc:
        failure = dict(type=type(exc).__name__, message=str(exc), next_block=complete_blocks)
        save()
        raise
    report = save()
    print(json.dumps(dict(event='actual_outward_meridian_node_admission_returned',
        complete=report['complete'], completed_blocks=complete_blocks,
        report_sha256=sha(report_path), actual_seconds=report['actual_seconds'],
        no_integral_Gram_or_geometry_claim=True), separators=(',', ':'), allow_nan=False), flush=True)


def parse_args():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('repo', 'report', 'checkpoint', 'reference-bundle', 'carrier', 'node-report',
                 'scalar-input', 'preparation-report', 'outdir'):
        p.add_argument('--'+name, type=Path, required=True)
    p.add_argument('--state', choices=('initial', 'final'), default='final')
    p.add_argument('--panels', type=int, default=128)
    p.add_argument('--exp-order', type=int, default=24)
    p.add_argument('--requests', type=Path)
    p.add_argument('--write-node-records', action='store_true')
    p.add_argument('--admission-seconds', type=float, default=600.)
    p.add_argument('--resume', action='store_true')
    args = p.parse_args()
    if (args.panels < 1 or args.exp_order < 2 or not math.isfinite(args.admission_seconds)
            or args.admission_seconds <= 0):
        raise ValueError('Use explicit positive whole-component arithmetic and natural return budgets')
    return args


if __name__ == '__main__':
    main(parse_args())
