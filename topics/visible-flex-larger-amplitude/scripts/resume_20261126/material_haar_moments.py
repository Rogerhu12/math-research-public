#!/usr/bin/env python3
"""R691 true material-Haar angular moments, with complete periodic tails.

The mathematical object is an EXACT full-circle integral. Q and derivative
order are working accuracy parameters, not a finite-quadrature target.
All original core modes enter rho and Theta. Integer outward arithmetic
pays sampled values, every operation and all Fourier aliasing tails.

The complete angular component can be consumed by a frozen continuous
target through P,Q,ell,b. This file alone does not freeze scalar/q/H inputs,
solve a field, certify its geometry, or implement a moving-target solver.
The extra reciprocal-square and phase moments expose complete angular
core variations for a later full moving J/J* consumer.

Science runs only in the public repository Actions. A same-run journal
saves sums after complete angular orbits and resumes naturally.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import math
import os
import sys
import time

import numpy as np


SCHEMA = 'R691-true-material-Haar-angular-moments-v1'
DEEP_ARITHMETIC_SHA = 'e091f67566ef6a380758a3aac5d79d9b41e4bffcc9a9860e66eaaa9b314257c2'
FACTORIES = {
    'R671-exact-reference-tail-lift-v1':
        ('resume_20261120/exact_reference_tail_lift.py',
         '2e0219c50543d859a9c649553bc4dde863df24daab26ffa75e5112baa4a90216'),
    'deep-valley-fixed-scalar-fullclosed-lift-v1':
        ('resume_20261126/deep_valley_reference_factory.py',
         '4ae012fbc0ccd58ae093069e0229ee8b72db9ef8d7d153565ef4507dc67db2d1')
}


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Actual angular moment work belongs only in public repository Actions')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                     allow_nan=False).encode()).hexdigest()


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
    raise ValueError('Recomputable moment carriers and journals remain outside the repository')


def arithmetic(path):
    path = Path(path).resolve()
    if sha(path) != DEEP_ARITHMETIC_SHA:
        raise ValueError('Use the complete stated integer outward/trigonometric arithmetic')
    name = '_Haar_integer_'+DEEP_ARITHMETIC_SHA[:16]
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def fraction_interval(value, d):
    return [str(F(value[0], d.SCALE)), str(F(value[1], d.SCALE))]


def exact_core_input(bundle, repo):
    with np.load(bundle, allow_pickle=False) as z:
        jets = np.array(z['qjets'], copy=True)
        fixed = np.array(z['fixed_core_first3'], copy=True)
        model = json.loads(str(z['reference_tail_model_json'].item()))
        mesh = np.array(z['mesh'], copy=True)
        tags = [float(z[key]) for key in ('reference_tail_lambda', 'exact_tail_lambda') if key in z]
    if jets.ndim != 3 or jets.shape[1] != 3 or (jets.shape[2]-2) % 3:
        raise ValueError('Need the complete original q coefficient layout')
    M = (jets.shape[2]-2)//3
    if M < 1 or jets.shape[0] != len(mesh) or not np.isfinite(jets).all():
        raise ValueError('Incomplete real finite candidate coefficients')
    if not np.isfinite(mesh).all() or not np.all(np.diff(mesh) > 0):
        raise ValueError('The actual radial carrier must be finite and increasing')
    core = jets[0, 0, 1:M+1].copy()
    expected = jets.copy()
    expected[0, 0] = 0.
    expected[0, 0, 0] = 1.
    expected[0, 0, 1:M+1] = core
    expected[0, 0, M+1:2*M+1] = -2*np.arange(1, M+1)*core
    expected[0, 1] = 0.
    expected[0, 1, 2*M+1] = 1.
    expected[0, 2, 2*M+1:] = 0.
    expected[-1] = 0.
    if not np.array_equal(expected, jets) or not np.array_equal(core[:len(fixed)], fixed):
        raise ValueError('The actual bundle violates its literal complete affine core/cap interface')
    if model.get('schema') not in FACTORIES or model.get('M') != M:
        raise ValueError('An explicit supported actual canonical field is required')
    relative, digest = FACTORIES[model['schema']]
    factory = Path(repo).resolve()/'topics/visible-flex-larger-amplitude/scripts'/relative
    if model.get('source_sha256') != digest or sha(factory) != digest:
        raise ValueError('The declared canonical source identity does not match actual bytes')
    lam = model.get('lambda_value')
    if not isinstance(lam, (int, float)) or not 0 <= lam <= 1 or not tags or any(value != lam for value in tags):
        raise ValueError('Canonical and supplemental lambda tags disagree')
    definition = dict(schema='R691-exact-full-circle-angular-integrals-v1', M=M,
        original_core_binary64_hex=[float(value).hex() for value in core],
        physical_angle='phi on [0,2*pi], pi is exact',
        frequencies='nu_j=2*j, j=1,...,M',
        rho='1+sum_j(1-nu_j^2)*c_j*cos(nu_j*phi)',
        material_angle='Theta=phi+sum_j(1-nu_j^2)*c_j*sin(nu_j*phi)/nu_j',
        normalization='Exact full-circle material Haar measure rho*dphi/(2*pi)',
        basis='R_j=cos(2j phi)e_r(phi), T_j=sin(2j phi)e_t(phi), Z_j=cos(2j phi)e_z',
        index_layout='R_0..R_M, T_1..T_M, Z_0..Z_M',
        exact_moments=dict(P='integral rho B_i.B_j / (2*pi)',
            Q='integral (dphi B_i).(dphi B_j)/rho / (2*pi)',
            ell='integral (dphi B_i).e_t(Theta)/(2*pi) = integral rho B_i.e_r(Theta)/(2*pi)',
            b='integral rho B_i.e_z/(2*pi)'),
        quadrature_nodes_are_not_part_of_target=True,
        original_finite_modes_truncated=False)
    return core, model, definition, record(factory)


class Circle:
    """Integer enclosures at all full-grid nodes from exact quarter symmetry."""
    def __init__(self, Q, d):
        self.Q, self.d = int(Q), d
        self.quarter = self.Q//4
        if self.Q < 8 or self.Q % 4:
            raise ValueError('Use a complete grid divisible by four')
        pi = d.pi_box()
        self.pi = pi
        self.table = []
        for j in range(self.quarter+1):
            if j == 0:
                value = (d.ZERO, d.ONE)
            elif j == self.quarter:
                value = (d.ONE, d.ZERO)
            else:
                value = d.sine_cosine(d.scale(pi, F(2*j, self.Q)))
            self.table.append(value)

    def pair(self, j):
        j = int(j) % self.Q
        quadrant, position = divmod(j, self.quarter)
        s, c = self.table[position]
        if quadrant == 0:
            return s, c
        if quadrant == 1:
            return c, self.d.neg(s)
        if quadrant == 2:
            return self.d.neg(s), self.d.neg(c)
        return self.d.neg(c), s


def derivative_bounds(coefficients, rho_lower, order):
    """All complete finite rho/delta and reciprocal derivative envelopes."""
    M = len(coefficients)
    rho = [sum((abs(value)*F(2*(j+1))**k for j, value in enumerate(coefficients)), F(0))
           for k in range(order+1)]
    rho[0] += 1
    delta = [None]+[sum((abs(value)*F(2*(j+1))**(k-1)
                       for j, value in enumerate(coefficients)), F(0))
                     for k in range(1, order+1)]
    inverse = [1/rho_lower]
    for j in range(1, order+1):
        inverse.append(sum((F(math.comb(j, k))*rho[k]*inverse[j-k]
                            for k in range(1, j+1)), F(0))/rho_lower)
    inverse2 = [sum((F(math.comb(j, k))*inverse[k]*inverse[j-k]
                    for k in range(j+1)), F(0)) for j in range(order+1)]
    phase = [F(1)]
    for j in range(1, order+1):
        phase.append(sum((F(math.comb(j-1, k-1))*delta[k]*phase[j-k]
                          for k in range(1, j+1)), F(0)))
    return dict(rho=rho, delta=delta[1:], inverse=inverse, inverse2=inverse2, phase=phase)


def alias_bounds(Q, M, order, derivatives):
    """Complete Fourier tails: 2*zeta(p) <= 4 for integer p>=2."""
    return {
        'gamma_inverse': F(4)*derivatives['inverse'][order]/F(Q-4*M)**order,
        'gamma_inverse2': F(4)*derivatives['inverse2'][order]/F(Q-6*M)**order,
        'cos_delta': F(4)*derivatives['phase'][order]/F(Q-4*M)**order,
        'sin_delta': F(4)*derivatives['phase'][order]/F(Q-4*M)**order
    }


def prepare_samples(core, Q, d):
    circle = Circle(Q, d)
    coefficients = [F(float(value))*(1-(2*(j+1))**2) for j, value in enumerate(core)]
    boxes = [d.box(value) for value in coefficients]
    phases = [d.box(value/F(2*(j+1))) for j, value in enumerate(coefficients)]
    samples = []
    for j in range(Q//4+1):
        rho, delta = d.ONE, d.ZERO
        for k, (coefficient, phase) in enumerate(zip(boxes, phases), 1):
            s, c = circle.pair(2*k*j)
            rho = d.add(rho, d.mul(coefficient, c))
            delta = d.add(delta, d.mul(phase, s))
        samples.append((rho, delta))
    derivative1 = sum((F(2*(j+1))*abs(value) for j, value in enumerate(coefficients)), F(0))
    sample_minimum = min(F(value[0][0], d.SCALE) for value in samples)
    covering_fee = F(circle.pi[1], d.SCALE)*derivative1/Q
    lower = sample_minimum-covering_fee
    detail = dict(full_grid_nodes=Q, explicit_quarter_orbits=len(samples),
        interior_orbit_multiplicity=4, endpoint_orbit_multiplicity=2,
        all_reflection_pi_symmetries_exact=True,
        minimum_integer_grid_rho_lower_exact=str(sample_minimum),
        complete_rho_derivative1_upper_exact=str(derivative1),
        half_angle_gap_pi_over_Q_upper_exact=str(F(circle.pi[1], d.SCALE)/Q),
        continuous_rho_cover_fee_exact=str(covering_fee),
        continuous_rho_lower_exact=str(lower),
        all_core_modes_included=True, positive_rho_certified=lower > 0)
    return circle, coefficients, samples, lower, detail


def interval_float(value, d):
    lo_exact, hi_exact = F(value[0], d.SCALE), F(value[1], d.SCALE)
    lo, hi = float(lo_exact), float(hi_exact)
    if F(lo) > lo_exact:
        lo = math.nextafter(lo, -math.inf)
    if F(hi) < hi_exact:
        hi = math.nextafter(hi, math.inf)
    return lo, hi


class MomentKernel:
    """Complete P,Q,ell,b from accurate vectors; no sampled target redefinition.

    midpoint_matrices()/numerical_means() are numerical working carriers.
    enclose_means() uses ALL interval coefficients and accepts complete
    outward integer scalar/q inputs. Caller owns exact radial/profile
    identity and its approximation errors; this angular object never
    declares a full frozen target certified by itself.
    """
    def __init__(self, carrier, arithmetic_source, *, expected_bundle_sha256=None):
        require_actions()
        self.d = arithmetic(arithmetic_source)
        self.carrier_path = Path(carrier).resolve()
        self.raw = json.loads(self.carrier_path.read_text())
        if (self.raw.get('schema') != SCHEMA or self.raw.get('complete') is not True
                or self.raw.get('integer_scale') != self.d.SCALE
                or self.raw.get('arithmetic_source_sha256') != DEEP_ARITHMETIC_SHA
                or self.raw.get('source', {}).get('sha256') != sha(__file__)
                or self.raw.get('positivity', {}).get('positive_rho_certified') is not True
                or F(self.raw.get('positivity', {}).get('continuous_rho_lower_exact', '0')) <= 0
                or self.raw.get('angular_identity_sha256') != canonical(self.raw['definition'])):
            raise ValueError('Need a complete exact-target angular moment carrier')
        if expected_bundle_sha256 is not None and self.raw['source_bundle']['sha256'] != expected_bundle_sha256:
            raise ValueError('Frozen angular moments came from another actual candidate bundle')
        self.M = int(self.raw['definition']['M'])
        self.core = [F(float.fromhex(value)) for value in self.raw['definition']['original_core_binary64_hex']]
        self.rho_coefficients = [value*(1-(2*(j+1))**2) for j, value in enumerate(self.core)]
        self.vectors = {key: [tuple(int(x) for x in value) for value in values]
                        for key, values in self.raw['moments_integer_intervals'].items()}
        lengths = dict(gamma_inverse=2*self.M+1, gamma_inverse2=3*self.M+1,
                       cos_delta=2*self.M+1, sin_delta=2*self.M+1)
        if set(self.vectors) != set(lengths) or len(self.core) != self.M:
            raise ValueError('Incomplete angular moment family')
        if any(len(self.vectors[key]) != size or any(lo > hi for lo, hi in self.vectors[key])
               for key, size in lengths.items()):
            raise ValueError('Invalid angular moment interval layout')
        self._blocks = self._numeric = None

    def _rho(self, index):
        if index == 0:
            return self.d.ONE
        return self.d.box(self.rho_coefficients[index-1]/2) if index <= self.M else self.d.ZERO

    def _products(self, vector, i, j):
        d = self.d
        return (d.scale(d.add(vector[abs(i-j)], vector[i+j]), F(1, 2)),
                d.scale(d.sub(vector[abs(i-j)], vector[i+j]), F(1, 2)))

    def interval_blocks(self):
        """Outward fixed-point coefficient blocks, including frame connection."""
        if self._blocks is not None:
            return self._blocks
        d, M = self.d, self.M
        rho = [self._rho(j) for j in range(2*M+1)]
        inverse = self.vectors['gamma_inverse']
        Prr, Ptt, Qrr, Qtt, Qrt, Qzz = [], [], [], [], [], []
        for i in range(M+1):
            pr, qr, qz, qt = [], [], [], []
            for j in range(M+1):
                C, S = self._products(inverse, i, j)
                Cr, Sr = self._products(rho, i, j)
                pr.append(Cr)
                qr.append(d.add(d.scale(S, 4*i*j), C))
                qz.append(d.scale(S, 4*i*j))
                if j:
                    qt.append(d.add(d.scale(S, 2*i), d.scale(C, 2*j)))
            Prr.append(pr); Qrr.append(qr); Qzz.append(qz); Qrt.append(qt)
            if i:
                pt, tt = [], []
                for j in range(1, M+1):
                    C, S = self._products(inverse, i, j)
                    _, Sr = self._products(rho, i, j)
                    pt.append(Sr)
                    tt.append(d.add(S, d.scale(C, 4*i*j)))
                Ptt.append(pt); Qtt.append(tt)
        c, s = self.vectors['cos_delta'], self.vectors['sin_delta']
        ellR = [d.add(c[j], d.scale(s[j], 2*j)) for j in range(M+1)]
        ellT = [d.add(d.scale(c[j], 2*j), s[j]) for j in range(1, M+1)]
        bZ = [self._rho(j) for j in range(M+1)]
        self._blocks = dict(Prr=Prr, Ptt=Ptt, Pzz=Prr, Qrr=Qrr, Qtt=Qtt,
                            Qrt=Qrt, Qzz=Qzz, ellR=ellR, ellT=ellT, bZ=bZ)
        return self._blocks

    def midpoint_matrices(self):
        """Numerical midpoints plus complete outward coefficient intervals."""
        if self._numeric is not None:
            return self._numeric
        d = self.d
        result = {}
        for key, value in self.interval_blocks().items():
            matrix = key not in ('ellR', 'ellT', 'bZ')
            rows = value if matrix else [value]
            endpoints = np.asarray([[interval_float(pair, d) for pair in row] for row in rows])
            if not matrix:
                endpoints = endpoints[0]
            lower, upper = endpoints[..., 0], endpoints[..., 1]
            result[key] = dict(midpoint=(lower+upper)/2, lower=lower, upper=upper)
        self._numeric = result
        return result

    def numerical_means(self, q, qs, f, fs, zs):
        """Fixed angular object; q/qs/f/fs/zs must be from its frozen field."""
        data, M = self.midpoint_matrices(), self.M
        q, qs = np.asarray(q), np.asarray(qs)
        if q.shape != qs.shape or q.shape[-1] != 3*M+2:
            raise ValueError('Use all original R/T/Z coefficients at each current radial point')
        R, T, Z = slice(0, M+1), slice(M+1, 2*M+1), slice(2*M+1, None)
        block = lambda name: data[name]['midpoint']
        quad = lambda value, name: np.einsum('...i,ij,...j->...', value, block(name), value)
        dot = lambda value, name: np.einsum('...i,i->...', value, block(name))
        pu = quad(qs[..., R], 'Prr')+quad(qs[..., T], 'Ptt')+quad(qs[..., Z], 'Pzz')
        qq = quad(q[..., R], 'Qrr')+quad(q[..., T], 'Qtt')+quad(q[..., Z], 'Qzz')
        qq += 2*np.einsum('...i,ij,...j->...', q[..., R], block('Qrt'), q[..., T])
        lu = dot(qs[..., R], 'ellR')+dot(qs[..., T], 'ellT')
        lq = dot(q[..., R], 'ellR')+dot(q[..., T], 'ellT')
        bu = dot(qs[..., Z], 'bZ')
        E = pu+2*np.asarray(fs)*lu+2*np.asarray(zs)*bu+np.asarray(fs)**2+np.asarray(zs)**2
        C = qq+2*np.asarray(f)*lq+np.asarray(f)**2
        return E, C

    def enclose_means(self, q, qs, f, fs, zs):
        """Accurate full means from integer boxes of EXACT radial quantities.

        q and qs have all 3M+2 coefficient intervals; f/fs/zs are intervals.
        No scalar or q interpolation error is silently assumed to be zero.
        """
        d, M = self.d, self.M
        if len(q) != 3*M+2 or len(qs) != len(q):
            raise ValueError('Complete radial coefficient intervals are required')
        blocks = self.interval_blocks()
        dot = lambda x, y: d.sum_intervals(d.mul(a, b) for a, b in zip(x, y))
        def bilinear(x, matrix, y):
            return d.sum_intervals(d.mul(x[i], d.mul(matrix[i][j], y[j]))
                                  for i in range(len(x)) for j in range(len(y)))
        R, T, Z = slice(0, M+1), slice(M+1, 2*M+1), slice(2*M+1, None)
        E = d.sum_intervals(bilinear(qs[index], blocks[name], qs[index])
                           for index, name in ((R, 'Prr'), (T, 'Ptt'), (Z, 'Pzz')))
        lu = d.add(dot(qs[R], blocks['ellR']), dot(qs[T], blocks['ellT']))
        bu = dot(qs[Z], blocks['bZ'])
        E = d.sum_intervals((E, d.scale(d.mul(fs, lu), 2), d.scale(d.mul(zs, bu), 2),
                            d.mul(fs, fs), d.mul(zs, zs)))
        C = d.sum_intervals(bilinear(q[index], blocks[name], q[index])
                           for index, name in ((R, 'Qrr'), (T, 'Qtt'), (Z, 'Qzz')))
        C = d.add(C, d.scale(bilinear(q[R], blocks['Qrt'], q[T]), 2))
        lq = d.add(dot(q[R], blocks['ellR']), dot(q[T], blocks['ellT']))
        C = d.sum_intervals((C, d.scale(d.mul(f, lq), 2), d.mul(f, f)))
        return E, C

    def core_direction_vectors(self, delta_core):
        """Complete angular variations for a later full moving J/J* caller.

        Returns delta gamma(rho), delta gamma(1/rho), delta ell and delta b.
        Multiplying these moment variations into the stated matrix formulas
        gives delta P/Q; q/u/H and physical-port variations remain the
        caller's complete original-variable derivatives.
        """
        require_actions()
        d, M = self.d, self.M
        if len(delta_core) != M:
            raise ValueError('Include every original core direction, with explicit zeros for fixed modes')
        dc = [F(float(value)) for value in delta_core]
        da = [value*(1-(2*(j+1))**2) for j, value in enumerate(dc)]
        dt = [value/F(2*(j+1)) for j, value in enumerate(da)]
        gamma_rho = [d.ZERO]+[d.box(value/2) for value in da]+[d.ZERO]*M
        inv2 = self.vectors['gamma_inverse2']
        inverse_variation = []
        for j in range(2*M+1):
            inverse_variation.append(d.neg(d.sum_intervals(
                d.scale(d.add(inv2[abs(j-k)], inv2[j+k]), da[k-1]/2)
                for k in range(1, M+1))))
        c, s = self.vectors['cos_delta'], self.vectors['sin_delta']
        ellR, ellT = [], []
        for i in range(M+1):
            radial, tangential = [], []
            for k in range(1, M+1):
                A = d.scale(d.sub(c[abs(i-k)], c[i+k]), F(1, 2))
                sign = 1 if k > i else -1 if k < i else 0
                B = d.scale(d.add(s[i+k], d.scale(s[abs(k-i)], sign)), F(1, 2))
                radial.append(d.scale(d.sub(d.scale(A, 2*i), B), dt[k-1]))
                tangential.append(d.scale(d.sub(A, d.scale(B, 2*i)), dt[k-1]))
            ellR.append(d.sum_intervals(radial))
            if i:
                ellT.append(d.sum_intervals(tangential))
        return dict(gamma_rho=gamma_rho, gamma_inverse=inverse_variation,
                    ellR=ellR, ellT=ellT, bZ=gamma_rho[:M+1],
                    complete_angular_core_direction=True,
                    full_physical_variable_J_or_Jstar_assembled_here=False)


def accumulated_weight(next_orbit, Q):
    if next_orbit == 0:
        return 0
    count = 2+4*(next_orbit-1)
    return count-2 if next_orbit == Q//4+1 else count


def main(args):
    require_actions()
    started = time.monotonic()
    repo = args.repo.resolve()
    out, journal, carrier = [outside(value, repo) for value in (args.out, args.journal, args.moments)]
    if out.exists():
        raise FileExistsError('Each real moment batch gets its own report')
    if carrier.exists():
        raise FileExistsError('Do not overwrite a completed moment carrier')
    if (args.angles < 8 or args.angles & (args.angles-1)
            or not 2 <= args.derivative_order <= 16
            or args.admission_seconds <= 0 or args.maximum_new_orbits < 1
            or F(args.target_moment_error) <= 0):
        raise ValueError('Declare a dyadic grid, order 2..16 and positive finite work budgets')
    core, model, definition, factory = exact_core_input(args.bundle, repo)
    M, Q, order = len(core), int(args.angles), int(args.derivative_order)
    if Q <= 6*M:
        raise ValueError('Use Q>6M to enclose every requested complete moving/frozen angular moment')
    path = (args.arithmetic_source or repo/'topics/visible-flex-larger-amplitude/scripts/resume_20261126/deep_valley_tail_input.py').resolve()
    d = arithmetic(path)
    angular_identity = canonical(definition)
    circle, rho_coeff, samples, rho_lower, positivity = prepare_samples(core, Q, d)
    report = dict(schema=SCHEMA, source_sha256=sha(__file__), source=record(__file__),
        source_bundle=record(args.bundle), declared_canonical_model_identity_sha256=canonical(model),
        canonical_factory=factory, arithmetic_source=record(path),
        definition=definition, angular_identity_sha256=angular_identity,
        complete=False, full_angles=Q, derivative_order=order, M=M,
        positivity=positivity, exact_target_is_full_material_Haar=True,
        target_redefined_as_discrete_quadrature=False,
        all_original_core_modes_retained=True,
        source_scalar_q_H_context_separately_validated=False,
        full_frozen_metric_constructed=False, moving_J_Jstar_solver_executed=False,
        nonlinear_field_solve_performed=False, continuous_geometry_certified=False,
        topic_complete=False, target_moment_error_exact=str(F(args.target_moment_error)),
        execution=dict(repository=os.environ['GITHUB_REPOSITORY'], run_id=os.environ.get('GITHUB_RUN_ID'),
                       run_attempt=os.environ.get('GITHUB_RUN_ATTEMPT'), workflow_trigger_commit=os.environ.get('GITHUB_SHA')))
    if rho_lower <= 0:
        report.update(status='complete_rho_positivity_lower_unpaid',
            exact_moment_integrals_enclosed=False, new_completed_quarter_orbits=0,
            completed_quarter_orbits=0, required_quarter_orbits=Q//4+1,
            seconds=time.monotonic()-started,
            reason='Increase only working Q or obtain a sharper same-core rho lower bound; no change of the exact Haar target is authorized here')
        write_json(out, report)
        print(json.dumps(dict(schema=SCHEMA, status=report['status'], report_sha256=sha(out),
            angular_identity_sha256=angular_identity, seconds=report['seconds'])), flush=True)
        return
    derivatives = derivative_bounds(rho_coeff, rho_lower, order)
    errors = alias_bounds(Q, M, order, derivatives)
    lengths = dict(gamma_inverse=2*M+1, gamma_inverse2=3*M+1,
                   cos_delta=2*M+1, sin_delta=2*M+1)
    identity = dict(schema='R691-actual-angular-orbit-sum-journal-v1',
        source_sha256=sha(__file__), arithmetic_source_sha256=DEEP_ARITHMETIC_SHA,
        source_bundle_sha256=sha(args.bundle), angular_identity_sha256=angular_identity,
        full_angles=Q, derivative_order=order, family_lengths=lengths,
        run_id=os.environ.get('GITHUB_RUN_ID'), run_attempt=os.environ.get('GITHUB_RUN_ATTEMPT'))
    identity_sha = canonical(identity)
    if journal.exists():
        state = json.loads(journal.read_text())
        if state.get('identity') != identity or state.get('identity_sha256') != identity_sha:
            raise ValueError('Use only the same actual source/core/full-grid/run angular journal')
    else:
        state = dict(identity=identity, identity_sha256=identity_sha, next_orbit=0,
            accumulated_full_grid_weight=0,
            sums={key: [[0, 0] for _ in range(size)] for key, size in lengths.items()})
    initial = int(state['next_orbit'])
    if (not 0 <= initial <= Q//4+1
            or state.get('accumulated_full_grid_weight') != accumulated_weight(initial, Q)
            or set(state['sums']) != set(lengths)
            or any(len(state['sums'][key]) != size for key, size in lengths.items())
            or any(not isinstance(lo, int) or not isinstance(hi, int) or lo > hi
                   for values in state['sums'].values() for lo, hi in values)):
        raise ValueError('Incomplete or invalid exact partial moment sums')
    done = initial
    for j in range(initial, Q//4+1):
        if done > initial and (time.monotonic()-started >= args.admission_seconds
                               or done-initial >= args.maximum_new_orbits):
            break
        rho, delta = samples[j]
        inverse = d.inverse(rho)
        phase_sine, phase_cosine = d.sine_cosine(delta)
        scalars = dict(gamma_inverse=inverse, gamma_inverse2=d.mul(inverse, inverse),
                       cos_delta=phase_cosine, sin_delta=phase_sine)
        trigonometry = [circle.pair(2*k*j) for k in range(3*M+1)]
        weight = 2 if j in (0, Q//4) else 4
        for family, size in lengths.items():
            position = 0 if family == 'sin_delta' else 1
            sums = state['sums'][family]
            for k in range(size):
                value = d.mul(scalars[family], trigonometry[k][position])
                sums[k][0] += weight*value[0]
                sums[k][1] += weight*value[1]
        done = j+1
        state.update(next_orbit=done, accumulated_full_grid_weight=accumulated_weight(done, Q))
        if done % 64 == 0 or done == Q//4+1:
            write_json(journal, state)
            print(json.dumps(dict(event='true_material_Haar_complete_orbits_saved',
                angular_identity_sha256=angular_identity, completed_quarter_orbits=done,
                required_quarter_orbits=Q//4+1, elapsed_seconds=time.monotonic()-started)), flush=True)
    write_json(journal, state)
    complete = done == Q//4+1
    report.update(complete=complete, status='complete' if complete else 'natural_orbit_budget_return',
        completed_quarter_orbits=done, required_quarter_orbits=Q//4+1,
        inherited_quarter_orbits=initial, new_completed_quarter_orbits=done-initial,
        accumulated_full_grid_weight=state['accumulated_full_grid_weight'],
        requested_admission_seconds=args.admission_seconds,
        maximum_new_orbits=args.maximum_new_orbits,
        journal=record(journal), journal_identity_sha256=identity_sha,
        alias_bounds_exact={key: str(value) for key, value in errors.items()},
        derivative_bounds_exact={key: [str(value) for value in values]
                                 for key, values in derivatives.items()},
        periodic_tail_proof='For |n|<=n0<Q, sum_{k!=0}|fhat(n+kQ)| <= 2*zeta(p)*||f^(p)||inf/(Q-n0)^p <= 4*bound/(Q-n0)^p',
        moment_frequency_caps=dict(gamma_inverse=4*M, gamma_inverse2=6*M,
                                   cos_delta=4*M, sin_delta=4*M),
        exact_moment_integrals_enclosed=complete,
        floating_FFT_or_libm_error_assumed_zero=False,
        moment_intervals_are_exact_target_enclosures_not_target_coefficients=True)
    if complete:
        if state['accumulated_full_grid_weight'] != Q:
            raise ArithmeticError('Every full-circle quadrature weight must be present')
        moments = {}
        widths = {}
        carrier_errors = {}
        for family, sums in state['sums'].items():
            fee = d.box(-errors[family], errors[family])
            values = [d.add(d.scale(tuple(value), F(1, Q)), fee) for value in sums]
            if family == 'sin_delta':
                values[0] = d.ZERO  # Exact sin(0 phi) test, not a quadrature guess.
            moments[family] = [list(value) for value in values]
            widths[family] = max(F(hi-lo, d.SCALE) for lo, hi in values)
            carrier_errors[family] = max(
                max(abs(F(value[0], d.SCALE)-F(float(F(value[0]+value[1], 2*d.SCALE)))),
                    abs(F(value[1], d.SCALE)-F(float(F(value[0]+value[1], 2*d.SCALE)))))
                for value in values)
        data = dict(schema=SCHEMA, complete=True, definition=definition,
            angular_identity_sha256=angular_identity, source=record(__file__),
            source_bundle=record(args.bundle), declared_canonical_model_identity_sha256=canonical(model),
            integer_scale=d.SCALE, arithmetic_source_sha256=DEEP_ARITHMETIC_SHA,
            moments_integer_intervals=moments, positivity=positivity,
            quadrature_work=dict(full_angles=Q, derivative_order=order,
                                 alias_bounds_exact={key: str(value) for key, value in errors.items()}),
            exact_target_is_full_material_Haar=True,
            finite_quadrature_nodes_not_frozen_as_mathematical_target=True,
            source_scalar_q_H_context_separately_validated=False)
        write_json(carrier, data)
        maximum_error = max(carrier_errors.values())
        report.update(moment_carrier=record(carrier),
            maximum_interval_width_exact_by_family={key: str(value) for key, value in widths.items()},
            maximum_midpoint_carrier_error_exact_by_family={key: str(value) for key, value in carrier_errors.items()},
            maximum_midpoint_carrier_error_exact=str(maximum_error),
            requested_moment_accuracy_reached=maximum_error <= F(args.target_moment_error),
            partial_quadrature_promoted_to_complete=False,
            next_interface='MomentKernel gives full P/Q/ell/b, interval frozen means and complete angular core variations. Bind one actual frozen full field/scalar/eta separately; current moving/frozen solver chains are not silently replaced.')
    else:
        report.update(moment_carrier=None, requested_moment_accuracy_reached=False,
            partial_quadrature_promoted_to_complete=False,
            next_interface='Resume the same runner journal with the same exact target and a fresh report path')
    report['seconds'] = time.monotonic()-started
    write_json(out, report)
    print(json.dumps(dict(schema=SCHEMA, status=report['status'], complete=complete,
        angular_identity_sha256=angular_identity, report_sha256=sha(out),
        completed_quarter_orbits=done, required_quarter_orbits=Q//4+1,
        requested_moment_accuracy_reached=report['requested_moment_accuracy_reached'],
        seconds=report['seconds'])), flush=True)


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('repo', 'bundle', 'moments', 'journal', 'out'):
        p.add_argument('--'+key, type=Path, required=True)
    p.add_argument('--arithmetic-source', type=Path)
    p.add_argument('--angles', type=int, default=8192)
    p.add_argument('--derivative-order', type=int, default=12)
    p.add_argument('--target-moment-error', default='1e-14')
    p.add_argument('--admission-seconds', type=float, default=900)
    p.add_argument('--maximum-new-orbits', type=int, default=4096)
    main(p.parse_args())
