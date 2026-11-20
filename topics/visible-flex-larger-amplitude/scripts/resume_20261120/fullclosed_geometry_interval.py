#!/usr/bin/env python3
"""Outward continuous geometry of the complete q + analytic-lift field.

Consumes binary free coefficients, exact affine-in-S node definitions and
the already enclosed same-Hold S/R.  Derived core endpoint coefficients are
rebuilt by the exact-real affine formula.  Geometry never uses sampled a.
The original f512 IEEE interval/rigorous radix-two transform is reused.
The untruncated cos(delta),sin(delta) lift uses explicit interval Taylor
remainders; no finite Fourier degree is assigned to that nonlinear lift.

Only explicitly requested cells are covered.  All bounds are continuous
radial/angle rectangle enclosures under the stated IEEE arithmetic model.
No nonlinear solve, old prefix certificate or global reach claim is made.
"""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time
import numpy as np


INTERVAL_SHA = 'f512c96cbc1fb3896fc144c5e9d8d29aaa80e321d08d9cdbf1745beb54a5c57d'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class Reader:
    def __init__(self, bundle, node_report, interval_source, *, angles=8192,
                 radial_subdivisions=16, beta='1/4', witness=True):
        self.bundle_path = Path(bundle).resolve()
        self.node_report_path = Path(node_report).resolve()
        self.interval_path = Path(interval_source).resolve()
        if sha(self.interval_path) != INTERVAL_SHA:
            raise ValueError('Need the stated IEEE/outward interval arithmetic source')
        self.I = load('complete_geometry_interval_arithmetic', self.interval_path)
        self.Q = int(angles)
        self.subdivisions = int(radial_subdivisions)
        self.beta = F(beta)
        self.witness = bool(witness)
        if (self.Q < 2 or self.Q & (self.Q-1) or self.subdivisions < 1
                or self.subdivisions & (self.subdivisions-1) or self.beta <= 0):
            raise ValueError('Use positive beta and dyadic angle/radial grids')
        with np.load(self.bundle_path, allow_pickle=False) as data:
            self.mesh = np.array(data['mesh'])
            self.literal_jets = np.array(data['qjets'])
            self.H = F(float(data['Hcap']))
            self.width = F(float(data['width']))
            self.radius_carrier = float(data['radius'])
            self.fixed_core = np.array(data['fixed_core_first3'])
        self.J = len(self.mesh)
        self.M = (self.literal_jets.shape[-1]-2)//3
        self.n = 3*self.M+2
        if (self.literal_jets.shape != (self.J, 3, self.n)
                or not np.all(np.isfinite(self.literal_jets))
                or not np.all(np.diff(self.mesh) > 0) or self.Q <= 4*self.M
                or self.H <= 0 or self.width <= 0):
            raise ValueError('Need the complete finite closed-field input')
        report = json.loads(self.node_report_path.read_text())
        self.nodes = [(F(d['S_coefficient']), F(d['constant']))
                      for d in report['true_scalar_nodes']]
        if (len(self.nodes) != self.J or self.nodes[0] != (F(0), F(0))
                or self.nodes[-1] != (F(1), F(0))
                or report['S_carrier'] != float(self.mesh[-1])
                or report['radius_carrier'] != self.radius_carrier):
            raise ValueError('Candidate and exact affine node definition differ')
        self.scalar_identity = report['scalar']
        self.S_exact = tuple(F(report['scalar']['S'][key]) for key in ('lower_exact', 'upper_exact'))
        self.R_exact = tuple(F(report['scalar']['R'][key]) for key in ('lower_exact', 'upper_exact'))
        self.S = self.bounds(*self.S_exact)
        self.R = self.bounds(*self.R_exact)
        self.W = self.fraction(self.width)
        self.Hbox = self.fraction(self.H)
        self.core = self.literal_jets[0, 0, 1:self.M+1].copy()
        K = len(self.fixed_core)
        expected = self.literal_jets.copy()
        expected[0, 0] = 0.
        expected[0, 0, 0] = 1.
        expected[0, 0, 1:self.M+1] = self.core
        expected[0, 0, self.M+1:2*self.M+1] = -2*np.arange(1, self.M+1)*self.core
        expected[0, 1] = 0.; expected[0, 1, 2*self.M+1] = 1.
        expected[0, 2, 2*self.M+1:] = 0.
        expected[-1] = 0.
        if not np.array_equal(self.core[:K], self.fixed_core) or not np.array_equal(expected, self.literal_jets):
            raise ValueError('The candidate is outside the original literal affine interface')
        self.jets = (self.literal_jets.copy(), self.literal_jets.copy())
        exact_t = self.I.mul(self.I.exact(-2*np.arange(1, self.M+1)), self.I.exact(self.core))
        self.jets[0][0, 0, self.M+1:2*self.M+1] = exact_t[0]
        self.jets[1][0, 0, self.M+1:2*self.M+1] = exact_t[1]
        self.nu = 2*np.arange(self.M+1)
        self.transform = self.I.Transform(self.Q)
        self.angle_slice = slice(0, self.Q//4+1)
        self.step = self.I.div(self.I.exact(self.transform.pi_upper), self.I.exact(self.Q))
        self.halfstep2 = self.I.scale(self.I.square(self.step), .5)
        self.discount = float(self.I.sub(self.I.exact(1.),
            self.I.scale(self.halfstep2, (2*self.M)**2))[0])
        if self.discount <= 0:
            raise ValueError('The exact finite-polynomial angular cover needs a positive discount')
        self._prepare_core_angles()

    def bounds(self, lower, upper):
        lo, hi = float(lower), float(upper)
        if F(lo) > lower:
            lo = np.nextafter(lo, -np.inf)
        if F(hi) < upper:
            hi = np.nextafter(hi, np.inf)
        return np.asarray(lo), np.asarray(hi)

    def fraction(self, value):
        return self.bounds(value, value)

    def affine(self, coefficient, constant):
        if coefficient == 0:
            return self.fraction(constant)
        return self.I.add(self.I.mul(self.fraction(coefficient), self.S), self.fraction(constant))

    def time_box(self, definition):
        return self.affine(*definition)

    def width_box(self, left, right):
        return self.affine(right[0]-left[0], right[1]-left[1])

    def split(self, controls, u):
        I = self.I
        if np.ndim(u[0]) != 0:
            raise ValueError('The radial split parameter is scalar')
        work = controls
        left, right = [I.at(work, 0)], [I.at(work, -1)]
        one = I.sub(I.exact(1.), u)
        for _ in range(len(controls[0])-1):
            work = I.add(I.mul(one, I.at(work, slice(None, -1))),
                         I.mul(u, I.at(work, slice(1, None))))
            left.append(I.at(work, 0)); right.append(I.at(work, -1))
        return I.stack(left), I.stack(right[::-1])

    def restrict(self, controls, u0, u1):
        if float(u0[0]) == float(u0[1]) == 0. and float(u1[0]) == float(u1[1]) == 1.:
            return controls
        right = controls if float(u0[0]) == float(u0[1]) == 0. else self.split(controls, u0)[1]
        ratio = self.I.div(self.I.sub(u1, u0), self.I.sub(self.I.exact(1.), u0))
        return self.split(right, ratio)[0]

    def elevate(self, controls, degree=6):
        I = self.I
        while len(controls[0])-1 < degree:
            d = len(controls[0])-1
            out = [I.at(controls, 0)]
            for j in range(1, d+1):
                out.append(I.div(I.add(I.scale(I.at(controls, j-1), j),
                    I.scale(I.at(controls, j), d+1-j)), I.exact(d+1)))
            out.append(I.at(controls, -1))
            controls = I.stack(out)
        return controls

    def derivative(self, controls, width):
        return self.I.div(self.I.scale(self.I.sub(self.I.at(controls, slice(1, None)),
            self.I.at(controls, slice(None, -1))), len(controls[0])-1), width)

    def hermite(self, left, right, width):
        I = self.I
        y0, y1 = I.at(left, 0), I.at(right, 0)
        v0, v1 = I.mul(width, I.at(left, 1)), I.mul(width, I.at(right, 1))
        a0, a1 = I.mul(I.square(width), I.at(left, 2)), I.mul(I.square(width), I.at(right, 2))
        return I.stack([y0, I.add(y0, I.div(v0, I.exact(5))),
            I.add(I.add(y0, I.div(I.scale(v0, 2), I.exact(5))), I.div(a0, I.exact(20))),
            I.add(I.sub(y1, I.div(I.scale(v1, 2), I.exact(5))), I.div(a1, I.exact(20))),
            I.sub(y1, I.div(v1, I.exact(5))), y1])

    def linear_product(self, controls, left, right):
        I = self.I
        d = len(controls[0])-1
        result = []
        for j in range(d+2):
            value = I.exact(0.)
            if j <= d:
                value = I.add(value, I.div(I.scale(I.mul(I.at(controls, j), left), d+1-j), I.exact(d+1)))
            if j:
                value = I.add(value, I.div(I.scale(I.mul(I.at(controls, j-1), right), j), I.exact(d+1)))
            result.append(value)
        return I.stack(result)

    def angle_boxes(self, coefficients, parity):
        """All closed angle arcs; bandwidth applies only to this polynomial."""
        I, tr = self.I, self.transform
        value = tr.cosine_sine(coefficients, self.Q, parity)
        first = tr.cosine_sine(I.scale(coefficients, -self.nu if parity == 'cos' else self.nu),
                               self.Q, 'sin' if parity == 'cos' else 'cos')
        second = tr.cosine_sine(I.scale(coefficients, -self.nu*self.nu), self.Q, parity)
        bound = I.div(I.exact(I.absolute_upper(second).max(axis=-1)), I.exact(self.discount))[1]
        value = I.at(value, (..., self.angle_slice))
        first = I.at(first, (..., self.angle_slice))
        loss = I.add(I.mul(self.step, I.exact(I.absolute_upper(first))),
                     I.mul(self.halfstep2, I.exact(bound[..., None])))[1]
        return I.down(value[0]-loss), I.up(value[1]+loss)

    def sine_cosine(self, angle, terms=24):
        """Explicit real Taylor remainder; no libm transcendental enclosure."""
        I = self.I
        square = I.square(angle)
        cv = self.fraction(F((-1)**terms, math.factorial(2*terms)))
        sv = self.fraction(F((-1)**terms, math.factorial(2*terms+1)))
        for k in range(terms-1, -1, -1):
            cv = I.add(I.mul(cv, square), self.fraction(F((-1)**k, math.factorial(2*k))))
            sv = I.add(I.mul(sv, square), self.fraction(F((-1)**k, math.factorial(2*k+1))))
        sv = I.mul(angle, sv)
        radius = F(float(I.absolute_upper(angle).max()))
        ce = float(self.fraction(radius**(2*terms+2)/math.factorial(2*terms+2))[1])
        se = float(self.fraction(radius**(2*terms+3)/math.factorial(2*terms+3))[1])
        cv = I.add(cv, (-ce, ce)); sv = I.add(sv, (-se, se))
        cv = np.maximum(cv[0], -1.), np.minimum(cv[1], 1.)
        sv = np.maximum(sv[0], -1.), np.minimum(sv[1], 1.)
        return sv, cv

    def _prepare_core_angles(self):
        I = self.I
        amp = I.scale(I.exact(self.core), 1-self.nu[1:]**2)
        rho = I.stack([I.exact(1.)]+[I.at(amp, j) for j in range(self.M)])
        delta = I.stack([I.exact(0.)]+[I.div(I.at(amp, j), I.exact(self.nu[j+1])) for j in range(self.M)])
        rhop = I.stack([I.exact(0.)]+[I.scale(I.at(amp, j), -self.nu[j+1]) for j in range(self.M)])
        self.rho = self.angle_boxes(rho, 'cos')
        self.rho_phi = self.angle_boxes(rhop, 'sin')
        self.delta = self.angle_boxes(delta, 'sin')
        sine, cosine = self.sine_cosine(self.delta)
        zero = I.exact(np.zeros_like(sine[0]))
        self.er, self.et = [cosine, sine, zero], [I.neg(sine), cosine, zero]
        radius = I.exact(1.)
        for value in self.core:
            radius = I.add(radius, I.exact(value))
        self.witness_radius = radius
        cosine0 = (self.transform.cos[0, self.angle_slice], self.transform.cos[1, self.angle_slice])
        sine0 = (self.transform.sin[0, self.angle_slice], self.transform.sin[1, self.angle_slice])
        c_loss = I.add(I.mul(self.step, I.exact(I.absolute_upper(sine0))), self.halfstep2)[1]
        s_loss = I.add(I.mul(self.step, I.exact(I.absolute_upper(cosine0))), self.halfstep2)[1]
        cp = I.down(cosine0[0]-c_loss), I.up(cosine0[1]+c_loss)
        sp = I.down(sine0[0]-s_loss), I.up(sine0[1]+s_loss)
        self.witness_rotating = [I.mul(radius, sp), I.mul(radius, cp), zero]

    def channels(self, controls, order):
        I, M, nu = self.I, self.M, self.nu
        r = I.at(controls, (slice(None), slice(0, M+1)))
        t0 = I.at(controls, (slice(None), slice(M+1, 2*M+1)))
        t = np.pad(t0[0], ((0, 0), (1, 0))), np.pad(t0[1], ((0, 0), (1, 0)))
        z = I.at(controls, (slice(None), slice(2*M+1, None)))
        if order == 0:
            return [(r, 'cos'), (t, 'sin'), (z, 'cos')]
        if order == 1:
            return [(I.neg(I.add(I.scale(r, nu), t)), 'sin'),
                    (I.add(r, I.scale(t, nu)), 'cos'), (I.neg(I.scale(z, nu)), 'sin')]
        return [(I.neg(I.add(I.scale(r, nu*nu+1), I.scale(t, 2*nu))), 'cos'),
                (I.neg(I.add(I.scale(t, nu*nu+1), I.scale(r, 2*nu))), 'sin'),
                (I.neg(I.scale(z, nu*nu)), 'cos')]

    def _cell_pieces(self, cell):
        I = self.I
        left, right = self.nodes[cell], self.nodes[cell+1]
        breakpoint = (F(1), -self.width)
        dl = self.affine(left[0]-1, left[1]+self.width)
        dr = self.affine(right[0]-1, right[1]+self.width)
        zero, one = I.exact(0.), I.exact(1.)
        if float(dr[1]) <= 0:
            return [(left, right, zero, one, False)]
        if float(dl[0]) >= 0:
            return [(left, right, zero, one, True)]
        if float(dl[1]) < 0 < float(dr[0]):
            u = I.div(self.width_box(left, breakpoint), self.width_box(left, right))
            return [(left, breakpoint, zero, u, False), (breakpoint, right, u, one, True)]
        raise ValueError('The declared S enclosure does not determine the exact lift-piece placement')

    def lift_controls(self, left, right, active):
        I = self.I
        if not active:
            zero = I.exact(np.zeros(7))
            return dict(chi=zero, cp=zero, cpp=zero, f=zero, fp=zero, fpp=zero)
        def parameter(edge):
            if edge == (F(1), -self.width):
                return I.exact(0.)
            if edge == (F(1), F(0)):
                return I.exact(1.)
            return I.div(self.affine(edge[0]-1, edge[1]+self.width), self.W)
        r0, r1 = parameter(left), parameter(right)
        global_chi = I.exact(np.array([0., 0., 0., 1., 1., 1.]))
        global_cp = self.derivative(global_chi, self.W)
        global_cpp = self.derivative(global_cp, self.W)
        chi, cp, cpp = [self.restrict(v, r0, r1) for v in (global_chi, global_cp, global_cpp)]
        b0 = I.add(self.R, self.affine(1-left[0], -left[1]))
        b1 = I.add(self.R, self.affine(1-right[0], -right[1]))
        f = self.linear_product(chi, b0, b1)
        fp = I.sub(self.linear_product(cp, b0, b1), chi)
        fpp = I.sub(self.linear_product(cpp, b0, b1), I.scale(cp, 2))
        return {name: self.elevate(value) for name, value in
                dict(chi=chi, cp=cp, cpp=cpp, f=f, fp=fp, fpp=fpp).items()}

    def physical_controls(self, cell, piece):
        I = self.I
        left, right, u0, u1, active = piece
        h = self.width_box(self.nodes[cell], self.nodes[cell+1])
        if float(h[0]) <= 0:
            raise ValueError('Exact candidate cell width was not enclosed positively')
        b = self.hermite(I.at(self.jets, cell), I.at(self.jets, cell+1), h)
        db = self.derivative(b, h)
        ddb = self.derivative(db, h)
        b, db, ddb = [self.elevate(self.restrict(v, u0, u1)) for v in (b, db, ddb)]
        fields = {}
        for name, controls, order in [('X', b, 0), ('V', db, 0), ('T', b, 1),
                                      ('AA', ddb, 0), ('VT', db, 1), ('EE', b, 2)]:
            fields[name] = [self.angle_boxes(c, parity) for c, parity in self.channels(controls, order)]
        lift = self.lift_controls(left, right, active)
        lift = {key: (value[0][:, None], value[1][:, None]) for key, value in lift.items()}
        for name, scalar in [('X', 'f'), ('V', 'fp'), ('AA', 'fpp')]:
            fields[name] = [I.add(fields[name][k], I.mul(lift[scalar], self.er[k])) for k in range(3)]
        for name, scalar in [('X', 'chi'), ('V', 'cp'), ('AA', 'cpp')]:
            fields[name][2] = I.add(fields[name][2], I.mul(lift[scalar], self.Hbox))
        for name, scalar in [('T', 'f'), ('VT', 'fp')]:
            fields[name] = [I.add(fields[name][k], I.mul(lift[scalar], I.mul(self.rho, self.et[k]))) for k in range(3)]
        fields['EE'] = [I.add(fields['EE'][k], I.mul(lift['f'],
            I.sub(I.mul(self.rho_phi, self.et[k]), I.mul(I.square(self.rho), self.er[k])))) for k in range(3)]
        return fields

    def radial_parts(self, controls):
        parts = [controls]
        for _ in range(self.subdivisions.bit_length()-1):
            parts = [out for value in parts for out in self.split(value, self.I.exact(.5))]
        return parts

    def dot(self, v, w):
        I = self.I
        return I.add(I.add(I.mul(v[0], w[0]), I.mul(v[1], w[1])), I.mul(v[2], w[2]))

    def norm2(self, v):
        I = self.I
        return I.add(I.add(I.square(v[0]), I.square(v[1])), I.square(v[2]))

    def cross(self, v, w):
        I = self.I
        return [I.sub(I.mul(v[(k+1)%3], w[(k+2)%3]),
                      I.mul(v[(k+2)%3], w[(k+1)%3])) for k in range(3)]

    def shape_upper(self, V, T, AA, VT, EE, N, W2):
        I = self.I
        E, Fg = self.norm2(V), self.dot(V, T)
        e, f, g = [self.dot(N, vector) for vector in (AA, VT, EE)]
        W = I.sqrt(W2)
        FE = I.div(Fg, E)
        b11 = I.div(e, I.mul(W, E))
        b12 = I.div(I.sub(f, I.mul(FE, e)), W2)
        numerator = I.add(I.sub(g, I.scale(I.mul(FE, f), 2)), I.mul(I.square(FE), e))
        b22 = I.div(I.mul(E, numerator), I.mul(W, W2))
        aa, bb, dd = [I.exact(I.absolute_upper(v)) for v in (b11, b12, b22)]
        majorant = I.scale(I.add(I.add(aa, dd), I.sqrt(I.add(I.square(I.sub(aa, dd)),
                                                              I.scale(I.square(bb), 4)))), .5)[1]
        trace_abs = I.exact(I.absolute_upper(I.add(b11, b22)))
        eigen_bound = I.scale(I.add(trace_abs, I.sqrt(I.add(I.square(I.sub(b11, b22)),
                                                           I.scale(I.square(b12), 4)))), .5)[1]
        return np.minimum(majorant, eigen_bound), E

    def certify(self, cell):
        started = time.monotonic()
        if not 0 <= cell < self.J-1:
            raise ValueError('Original cell index is outside the candidate')
        I = self.I
        record = dict(cell=int(cell), symbolic_left=[str(v) for v in self.nodes[cell]],
            symbolic_right=[str(v) for v in self.nodes[cell+1]],
            carrier_left=float(self.mesh[cell]), carrier_right=float(self.mesh[cell+1]),
            maximum_radius_squared_upper=0., support_lower=float('inf'),
            curvature_upper=0., normal_squared_lower=float('inf'), metric_E_lower=float('inf'),
            witness_distance_squared_lower=float('inf'), unpaid_metric_boxes=0,
            worst_curvature=None, worst_support=None, worst_radius=None, worst_witness=None)
        pieces = self._cell_pieces(cell)
        for part, piece in enumerate(pieces):
            controls = self.physical_controls(cell, piece)
            values = {name: [self.radial_parts(component) for component in vector]
                      for name, vector in controls.items()}
            for sub in range(self.subdivisions):
                fields = {name: [(c[sub][0].min(axis=0), c[sub][1].max(axis=0)) for c in vector]
                          for name, vector in values.items()}
                X, V, T, AA, VT, EE = [fields[name] for name in ('X', 'V', 'T', 'AA', 'VT', 'EE')]
                radius2 = self.norm2(X)[1]
                idx = int(np.argmax(radius2))
                address = lambda k: dict(piece=part, radial_subcell=sub, angle_grid_index=int(k))
                if float(radius2[idx]) > record['maximum_radius_squared_upper']:
                    record['maximum_radius_squared_upper'] = float(radius2[idx]); record['worst_radius'] = address(idx)
                if self.witness:
                    for sign in (-1, 1):
                        distance2 = self.norm2([I.sub(X[k], I.scale(self.witness_rotating[k], sign)) for k in range(3)])[0]
                        idx = int(np.argmin(distance2))
                        if float(distance2[idx]) < record['witness_distance_squared_lower']:
                            record['witness_distance_squared_lower'] = max(0., float(distance2[idx]))
                            record['worst_witness'] = dict(**address(idx), witness_sign=sign)
                N = self.cross(T, V)
                E = self.norm2(V)
                W2a = self.norm2(N)
                W2b = I.sub(I.mul(E, self.norm2(T)), I.square(self.dot(V, T)))
                W2 = np.maximum(W2a[0], W2b[0]), np.minimum(W2a[1], W2b[1])
                record['normal_squared_lower'] = min(record['normal_squared_lower'], float(W2[0].min()))
                record['metric_E_lower'] = min(record['metric_E_lower'], float(E[0].min()))
                bad = (W2[0] <= 0) | (E[0] <= 0)
                record['unpaid_metric_boxes'] += int(np.count_nonzero(bad))
                if np.any(bad):
                    continue
                support = I.div(self.dot([X[0], X[1], I.mul(self.fraction(self.beta), X[2])], N), I.sqrt(W2))
                idx = int(np.argmin(support[0]))
                if float(support[0][idx]) < record['support_lower']:
                    record['support_lower'] = float(support[0][idx]); record['worst_support'] = address(idx)
                bound, _ = self.shape_upper(V, T, AA, VT, EE, N, W2)
                idx = int(np.argmax(bound))
                if float(bound[idx]) > record['curvature_upper']:
                    record['curvature_upper'] = float(bound[idx]); record['worst_curvature'] = address(idx)
        paid = record['unpaid_metric_boxes'] == 0
        if not paid:
            record['curvature_upper'] = None
            record['support_lower'] = None
        if not self.witness:
            record['witness_distance_squared_lower'] = None
        record.update(exact_pieces=len(pieces), all_radial_and_angular_points_covered=paid,
            position_bound_continuous=True, strict_under_stated_IEEE_arithmetic=True,
            seconds=time.monotonic()-started)
        return record

    def cap_bounds(self):
        I = self.I
        radius2 = I.add(I.square(self.R), I.square(self.Hbox))
        gap = I.sub(self.witness_radius, self.R)
        distance2 = I.add(I.square(self.Hbox), I.square((np.maximum(0., gap[0]), np.maximum(0., gap[1]))))
        return dict(flat_upper_and_reflected_lower_disks=True,
            maximum_radius_squared_upper=float(radius2[1]),
            support_lower=float(I.mul(self.fraction(self.beta), self.Hbox)[0]),
            curvature_upper=0., witness_distance_squared_lower=float(distance2[0]),
            scope='The existing flat disks only; a later fixed marker uses R650 Appendix C separately')

    def metadata(self):
        return dict(source_sha256=sha(__file__), bundle_sha256=sha(self.bundle_path),
            node_report_sha256=sha(self.node_report_path), interval_source_sha256=INTERVAL_SHA,
            source_paths=dict(bundle=str(self.bundle_path), node_report=str(self.node_report_path), interval=str(self.interval_path)),
            J=self.J, M=self.M, angles=self.Q, evaluated_angle_boxes=self.Q//4+1,
            radial_subdivisions_per_piece=self.subdivisions, beta_exact=str(self.beta),
            S_exact_box=[str(v) for v in self.S_exact], R_exact_box=[str(v) for v in self.R_exact],
            H_exact=str(self.H), width_exact=str(self.width),
            scalar_source_sha256=self.scalar_identity['source_sha256'],
            integer_oracle_sha256=self.scalar_identity['integer_oracle_sha256'],
            hold_source_sha256=self.scalar_identity['hold_source_sha256'],
            field_definition='Exact binary free jets on alpha*S+beta nodes; exact derived core T=-nu*c; complete analytic lift with exact same-Hold S/R',
            geometry_uses_a_samples=False, old_lambda_normalization_used=False,
            analytic_lift_truncated=False, core_rho_continuous_lower=float(self.rho[0].min()),
            interval_transcendentals='Rigorous radix-two finite trig transform plus 24-term interval Taylor sin/cos(delta) and explicit remainder',
            outward_arithmetic='IEEE binary64 +,-,*,/,sqrt followed by nextafter outward; exact rational input and Machin/integer twiddles from f512',
            normal_orientation='F_phi cross F_s', support_center=[0, 0, 0],
            witness='p=Rot(pi/2)F(0,0); quarter-angle coverage uses both p and -p; horizontal mirror preserves this plane witness' if self.witness else None)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--bundle', type=Path, required=True)
    p.add_argument('--node-report', type=Path, required=True)
    p.add_argument('--interval-source', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--cells', type=int, nargs='+', required=True)
    p.add_argument('--angles', type=int, default=8192)
    p.add_argument('--radial-subdivisions', type=int, default=16)
    p.add_argument('--beta', default='1/4')
    p.add_argument('--no-witness', action='store_true')
    a = p.parse_args()
    if a.out.exists():
        raise FileExistsError('Keep existing continuous-cell results and select a fresh output')
    np.seterr(over='raise', invalid='raise', divide='raise', under='ignore')
    started = time.monotonic()
    reader = Reader(a.bundle, a.node_report, a.interval_source, angles=a.angles,
        radial_subdivisions=a.radial_subdivisions, beta=a.beta, witness=not a.no_witness)
    report = dict(schema='fullclosed-complete-geometry-interval-selected-cells-20261120-v1',
        metadata=reader.metadata(), records=[], cap_bounds=reader.cap_bounds(),
        full_closed_scope_covered=False, reach_certified=False)
    for cell in a.cells:
        record = reader.certify(cell)
        report['records'].append(record)
        report['seconds'] = time.monotonic()-started
        a.out.parent.mkdir(parents=True, exist_ok=True)
        a.out.write_text(json.dumps(report, indent=2)+'\n')
        print(json.dumps(record), flush=True)
    print(json.dumps(dict(event='selected_continuous_geometry_complete',
        report=str(a.out.resolve()), report_sha256=sha(a.out), seconds=report['seconds'])), flush=True)


if __name__ == '__main__':
    main()
