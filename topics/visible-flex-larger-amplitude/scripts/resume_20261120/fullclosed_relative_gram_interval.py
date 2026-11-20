#!/usr/bin/env python3
"""Continuous relative Gram bounds of the exact complete closed field.

Radial Bernstein products are formed before taking a radial or angle hull.
The analytic lift is reduced using er.er=et.et=1 and er.et=0.  Every
numerator has the exact form P+C*cos(delta)+S*sin(delta), with finite P/C/S;
the nonlinear angular remainder is explicit, not a false bandwidth claim.
Consumes same-Hold scalar boxes and exact scalar curvature laws.
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


GEOMETRY_SHA = '2a8d09fd1c85e96a9167b705c0fe77a9107bfe935928ceb914c271ffc5c17377'


def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module; spec.loader.exec_module(module)
    return module


class Gram:
    def __init__(self, bundle, node_report, interval_source, geometry_source,
                 scalar_source, scalar_input, *, angles=8192, subdivisions=16, scalar_degree=5):
        if sha(geometry_source) != GEOMETRY_SHA:
            raise ValueError('Require the proved complete geometry object definition')
        self.geometry_path, self.scalar_path = Path(geometry_source), Path(scalar_source)
        geometry = load('complete_geometry_for_relative_gram', geometry_source)
        self.r = geometry.Reader(bundle, node_report, interval_source, angles=angles,
                                 radial_subdivisions=subdivisions, witness=False)
        self.I, self.Q = self.r.I, self.r.Q
        self.scalar = load('same_scalar_for_relative_gram', scalar_source).Scalar(self.r, scalar_input, scalar_degree)
        self.m = 4*self.r.M
        self.discount = float(self.I.sub(self.I.exact(1.), self.I.scale(self.r.halfstep2, self.m*self.m))[0])
        if self.discount <= 0:
            raise ValueError('The finite Gram polynomial angular discount must be positive')
        self._prepare_angular_core()

    def zero(self, degree=0): return self.I.exact(np.zeros((degree+1, 5, self.Q)))

    def scalar_poly(self, controls):
        lo = np.zeros((len(controls[0]), 5, self.Q)); hi = lo.copy()
        lo[:, 0] = controls[0][:, None]; hi[:, 0] = controls[1][:, None]
        return lo, hi

    def constant(self, value):
        return self.scalar_poly(self.I.stack([self.r.fraction(F(value))]))

    def add(self, a, b):
        degree = max(len(a[0]), len(b[0]))-1
        return self.I.add(self.r.elevate(a, degree), self.r.elevate(b, degree))

    def sub(self, a, b): return self.add(a, self.I.neg(b))

    def multiply(self, a, b):
        """Exact Bernstein product plus angular Leibniz jets 0..4."""
        I = self.I; m, n = len(a[0])-1, len(b[0])-1
        values = []
        for ell in range(m+n+1):
            deriv = [I.exact(np.zeros(self.Q)) for _ in range(5)]
            for j in range(max(0, ell-n), min(m, ell)+1):
                k = ell-j
                weight = self.r.fraction(F(math.comb(m, j)*math.comb(n, k), math.comb(m+n, ell)))
                for order in range(5):
                    pair = I.exact(np.zeros(self.Q))
                    for split in range(order+1):
                        pair = I.add(pair, I.scale(I.mul(I.at(a, (j, split)), I.at(b, (k, order-split))),
                                                  math.comb(order, split)))
                    deriv[order] = I.add(deriv[order], I.mul(weight, pair))
            values.append(I.stack(deriv))
        return I.stack(values)

    def dot(self, a, b):
        result = self.multiply(a[0], b[0])
        for j in (1, 2): result = self.add(result, self.multiply(a[j], b[j]))
        return result

    def grid_jets(self, coefficients, parity):
        I = self.I; values = []; current = coefficients
        for order in range(5):
            values.append(self.r.transform.cosine_sine(current, self.Q, parity))
            current = I.scale(current, -self.r.nu if parity == 'cos' else self.r.nu)
            parity = 'sin' if parity == 'cos' else 'cos'
        stacked = I.stack(values)
        return np.moveaxis(stacked[0], 0, -2), np.moveaxis(stacked[1], 0, -2)

    def _prepare_angular_core(self):
        I, r = self.I, self.r
        amp = I.scale(I.exact(r.core), 1-r.nu[1:]**2)
        rho = I.stack([I.exact(1.)]+[I.at(amp, j) for j in range(r.M)])
        delta = I.stack([I.exact(0.)]+[I.div(I.at(amp, j), I.exact(r.nu[j+1])) for j in range(r.M)])
        self.rho_jets = self.grid_jets(rho, 'cos')
        self.delta_jets = self.grid_jets(delta, 'sin')
        sn, cs = r.sine_cosine(I.at(self.delta_jets, 0))
        d1, d2 = I.at(self.delta_jets, 1), I.at(self.delta_jets, 2)
        self.cos_delta = I.stack([cs, I.neg(I.mul(sn, d1)),
            I.neg(I.add(I.mul(cs, I.square(d1)), I.mul(sn, d2)))])
        self.sin_delta = I.stack([sn, I.mul(cs, d1),
            I.add(I.neg(I.mul(sn, I.square(d1))), I.mul(cs, d2))])
        db = [None]+[float(I.div(I.exact(I.absolute_upper(I.at(self.delta_jets, k)).max()),
                                 I.exact(r.discount))[1]) for k in range(1, 5)]
        d = [I.exact(v) if v is not None else None for v in db]
        B0, B1 = I.exact(1.), d[1]
        B2 = I.add(I.square(d[1]), d[2])
        B3 = I.add(I.add(I.mul(I.square(d[1]), d[1]), I.scale(I.mul(d[1], d[2]), 3)), d[3])
        B4 = I.add(I.add(I.square(I.square(d[1])), I.scale(I.mul(I.square(d[1]), d[2]), 6)),
                   I.add(I.add(I.scale(I.square(d[2]), 3), I.scale(I.mul(d[1], d[3]), 4)), d[4]))
        self.trig_derivative_bounds = [float(v[1]) for v in (B0, B1, B2, B3, B4)]
        self.rho_poly = (self.rho_jets[0][None, ...], self.rho_jets[1][None, ...])

    def physical_components(self, cell, piece):
        r, I = self.r, self.I
        left, right, u0, u1, active, _ = piece
        h = r.width_box(r.nodes[cell], r.nodes[cell+1])
        b = r.hermite(I.at(r.jets, cell), I.at(r.jets, cell+1), h)
        db = r.derivative(b, h)
        b, db = r.restrict(b, u0, u1), r.restrict(db, u0, u1)
        U = [self.grid_jets(c, parity) for c, parity in r.channels(db, 0)]
        T = [self.grid_jets(c, parity) for c, parity in r.channels(b, 1)]
        raw = r.lift_controls(left, right, active)
        lift = {k: self.scalar_poly(v) for k, v in raw.items()}
        return U, T, lift

    def numerator_controls(self, cell, piece, A):
        """Three exact P+C cos(delta)+S sin(delta) representations."""
        I = self.I
        U, T, lift = self.physical_components(cell, piece)
        c, f = lift['fp'], lift['f']
        d = I.mul(lift['cp'], self.r.Hbox)
        ap = self.scalar_poly(A)
        rho2 = self.multiply(self.rho_poly, self.rho_poly)
        Pe = self.sub(self.dot(U, U), self.constant(1))
        Pm = self.dot(U, T)
        Pg = self.sub(self.dot(T, T), self.multiply(self.multiply(ap, ap), rho2))
        if not piece[4]:
            return [(Pe, None, None), (Pm, None, None), (Pg, None, None)]
        Pe = self.add(Pe, self.add(self.multiply(c, c), self.multiply(d, d)))
        Pe = self.add(Pe, I.scale(self.multiply(d, U[2]), 2))
        Ce, Se = I.scale(self.multiply(c, U[0]), 2), I.scale(self.multiply(c, U[1]), 2)
        Pm = self.add(Pm, self.multiply(d, T[2]))
        fr = self.multiply(f, self.rho_poly)
        Cm = self.add(self.multiply(c, T[0]), self.multiply(fr, U[1]))
        Sm = self.sub(self.multiply(c, T[1]), self.multiply(fr, U[0]))
        Pg = self.add(Pg, self.multiply(self.multiply(f, f), rho2))
        Cg, Sg = I.scale(self.multiply(fr, T[1]), 2), I.scale(self.multiply(fr, T[0]), -2)
        return [(Pe, Ce, Se), (Pm, Cm, Sm), (Pg, Cg, Sg)]

    def nonlinear_grid(self, triple):
        """Grid jets after analytic cancellation, plus fourth derivative bound."""
        I, r = self.I, self.r
        P, C, S = triple
        if C is None:
            return I.at(P, (slice(None), slice(0, 3))), None
        degree = max(len(v[0]) for v in (P, C, S))-1
        P, C, S = [r.elevate(v, degree) for v in (P, C, S)]
        jets = []
        for order in range(3):
            value = I.at(P, (slice(None), order))
            for k in range(order+1):
                term = I.add(I.mul(I.at(C, (slice(None), k)), I.at(self.cos_delta, order-k)),
                             I.mul(I.at(S, (slice(None), k)), I.at(self.sin_delta, order-k)))
                value = I.add(value, I.scale(term, math.comb(order, k)))
            jets.append(value)
        stacked = I.stack(jets)
        jets = np.moveaxis(stacked[0], 0, 1), np.moveaxis(stacked[1], 0, 1)
        bound = I.div(I.exact(I.absolute_upper(I.at(P, (slice(None), 4))).max(axis=-1)), I.exact(self.discount))
        for k in range(5):
            finite = I.add(I.exact(I.absolute_upper(I.at(C, (slice(None), k))).max(axis=-1)),
                           I.exact(I.absolute_upper(I.at(S, (slice(None), k))).max(axis=-1)))
            finite = I.div(finite, I.exact(self.discount))
            bound = I.add(bound, I.scale(I.mul(finite, I.exact(self.trig_derivative_bounds[4-k])), math.comb(4, k)))
        return jets, bound

    def angle_enclosure(self, jets, fourth):
        """Complete coefficient angle arcs, before the radial convex hull."""
        I, r = self.I, self.r
        second_grid = I.exact(I.absolute_upper(I.at(jets, (slice(None), 2))).max(axis=-1))
        if fourth is None:
            B2 = I.div(second_grid, I.exact(self.discount))
            nonlinear_budget = np.zeros_like(B2[1])
        else:
            B2 = I.add(second_grid, I.mul(r.halfstep2, fourth))
            nonlinear_budget = I.mul(I.square(r.halfstep2), fourth)[1]
        value = I.at(jets, (slice(None), 0, r.angle_slice))
        first = I.at(jets, (slice(None), 1, r.angle_slice))
        pad = I.add(I.mul(r.step, I.exact(I.absolute_upper(first))),
                    I.mul(r.halfstep2, (B2[0][:, None], B2[1][:, None])))[1]
        return (I.down(value[0]-pad), I.up(value[1]+pad)), pad, nonlinear_budget

    def abs_interval(self, value):
        lo = np.where((value[0] <= 0) & (value[1] >= 0), 0., np.minimum(abs(value[0]), abs(value[1])))
        return lo, self.I.absolute_upper(value)

    def norm_interval(self, entries):
        I = self.I; e, m, g = entries
        return I.scale(I.add(self.abs_interval(I.add(e, g)),
            I.sqrt(I.add(I.square(I.sub(e, g)), I.scale(I.square(m), 4)))), .5)

    def relative(self, numerators, A_box, error, rho_box):
        I = self.I
        a = I.add(A_box, (-error, error))
        if np.any(a[0] <= 0) or np.any(rho_box[0] <= 0):
            raise ValueError('Same exact scalar and material density must be positive')
        ar = I.mul(a, rho_box)
        metric_error = I.div(I.mul(I.exact(error), I.add(I.scale(I.exact(I.absolute_upper(A_box)), 2), I.exact(error))), I.square(a))[1]
        entries = [numerators[0], I.div(numerators[1], ar),
                   I.add(I.div(numerators[2], I.square(ar)), (-metric_error, metric_error))]
        return entries, a, metric_error

    def certify(self, cell):
        I, r = self.I, self.r; start = time.monotonic()
        if not 0 <= cell < r.J-1: raise ValueError('Bad original cell index')
        record = dict(cell=int(cell), symbolic_left=[str(v) for v in r.nodes[cell]],
            symbolic_right=[str(v) for v in r.nodes[cell+1]],
            continuous_relative_gram_operator_upper=0., actual_supremum_lower=0.,
            maximum_component_absolute_upper=[0., 0., 0.],
            minimum_a_lower=float('inf'), minimum_rho_lower=float(r.rho[0].min()),
            scalar_remainder_relative_gram_upper=0., angular_padding_operator_upper=0.,
            nonlinear_angular_fourth_order_padding_upper=0.,
            numerator_coefficient_interval_width_upper=0.,
            scalar_pieces=[], worst=None, actual_lower_witness=None)
        pieces = self.scalar.pieces(cell)
        for part, piece in enumerate(pieces):
            A, error, scalar_info = self.scalar.approximation(piece)
            record['scalar_pieces'].append(dict(left=[str(v) for v in piece[0]], right=[str(v) for v in piece[1]],
                active_lift=bool(piece[4]), **scalar_info))
            triples = self.numerator_controls(cell, piece, A)
            grid = [self.nonlinear_grid(triple) for triple in triples]
            parts = [r.radial_parts(v) for v, _ in grid]
            fourths = [None if b is None else r.radial_parts(b) for _, b in grid]
            As = r.radial_parts(A)
            for sub in range(r.subdivisions):
                N, pads = [], []
                for j in range(3):
                    jpart = parts[j][sub]
                    box, pad, nonlinear = self.angle_enclosure(jpart, None if fourths[j] is None else fourths[j][sub])
                    N.append((box[0].min(axis=0), box[1].max(axis=0)))
                    pads.append(I.exact(pad.max(axis=0)))
                    record['nonlinear_angular_fourth_order_padding_upper'] = max(record['nonlinear_angular_fourth_order_padding_upper'], float(np.max(nonlinear)))
                    width = I.sub(I.at(jpart, (slice(None), 0)), I.at(jpart, (slice(None), 0)))
                    record['numerator_coefficient_interval_width_upper'] = max(record['numerator_coefficient_interval_width_upper'], float(width[1].max()))
                Apart = As[sub]
                A_box = np.asarray(Apart[0].min()), np.asarray(Apart[1].max())
                entries, a, fee = self.relative(N, A_box, error, r.rho)
                norm = self.norm_interval(entries)
                idx = int(np.argmax(norm[1]))
                address = dict(piece=part, radial_subcell=sub, angle_grid_index=idx)
                if float(norm[1][idx]) > record['continuous_relative_gram_operator_upper']:
                    record['continuous_relative_gram_operator_upper'] = float(norm[1][idx]); record['worst'] = address
                for j in range(3):
                    record['maximum_component_absolute_upper'][j] = max(record['maximum_component_absolute_upper'][j], float(I.absolute_upper(entries[j]).max()))
                record['minimum_a_lower'] = min(record['minimum_a_lower'], float(np.min(a[0])))
                record['scalar_remainder_relative_gram_upper'] = max(record['scalar_remainder_relative_gram_upper'], float(np.max(fee)))
                ar = I.mul(a, r.rho)
                pad_entries = [pads[0], I.div(pads[1], ar), I.div(pads[2], I.square(ar))]
                record['angular_padding_operator_upper'] = max(record['angular_padding_operator_upper'], float(self.norm_interval(pad_entries)[1].max()))
                # These are exact radial endpoints and exact Fourier angle points,
                # with interval field/scalar values.  They give a true lower bound
                # on the continuous supremum, not a claimed continuous upper.
                rho_grid = I.at(self.rho_jets, (0, r.angle_slice))
                for endpoint in (0, -1):
                    point = [I.at(parts[j][sub], (endpoint, 0, r.angle_slice)) for j in range(3)]
                    entry, _, _ = self.relative(point, I.at(Apart, endpoint), error, rho_grid)
                    lb = self.norm_interval(entry)[0]
                    ix = int(np.argmax(lb))
                    if float(lb[ix]) > record['actual_supremum_lower']:
                        record['actual_supremum_lower'] = max(0., float(lb[ix]))
                        record['actual_lower_witness'] = dict(piece=part, radial_subcell=sub,
                            endpoint=endpoint, angle_grid_index=ix)
        record.update(exact_pieces=len(pieces), all_radial_and_angular_points_covered=True,
            strict_under_stated_IEEE_arithmetic=True, target_1e_minus6_certified=record['continuous_relative_gram_operator_upper'] <= 1e-6,
            same_candidate_cannot_reach_1e_minus6_by_certificate_refinement=record['actual_supremum_lower'] > 1e-6,
            seconds=time.monotonic()-start)
        return record

    def metadata(self):
        return dict(source_sha256=sha(__file__), geometry_source_sha256=sha(self.geometry_path),
            scalar_source_sha256=sha(self.scalar_path), scalar_input_sha256=self.scalar.input_sha,
            complete_field=self.r.metadata(), scalar_degree=self.scalar.degree,
            relative_matrix='[[|Fs|^2-1,Fs.Fphi/(a*rho)],[same,|Fphi|^2/(a^2*rho^2)-1]]',
            numerator_structure='Exact radial Bernstein P+C*cos(delta)+S*sin(delta); er/et identities used before products',
            analytic_lift_truncated=False, scalar_interpolation_used=False,
            old_integral_certificates_rerun=False,
            nonlinear_angular_cover='Grid full numerator and first/second derivative; fourth derivative Bell/finite-polynomial bound pays the remaining closed arcs',
            scope='Only requested original cells; no full-surface metric claim')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('bundle', 'node-report', 'interval-source', 'geometry-source', 'scalar-source', 'scalar-input', 'out'):
        p.add_argument('--'+key, type=Path, required=True)
    p.add_argument('--cells', type=int, nargs='+', required=True)
    p.add_argument('--angles', type=int, default=8192)
    p.add_argument('--radial-subdivisions', type=int, default=16)
    p.add_argument('--scalar-degree', type=int, default=5)
    args = p.parse_args()
    if args.out.exists(): raise FileExistsError('Keep prior reports')
    np.seterr(over='raise', invalid='raise', divide='raise', under='ignore')
    start = time.monotonic()
    reader = Gram(args.bundle, args.node_report, args.interval_source, args.geometry_source,
        args.scalar_source, args.scalar_input, angles=args.angles,
        subdivisions=args.radial_subdivisions, scalar_degree=args.scalar_degree)
    report = dict(schema='complete-closed-relative-Gram-interval-selected-cells-20261120-v1',
        metadata=reader.metadata(), records=[], full_closed_scope_covered=False)
    for cell in args.cells:
        record = reader.certify(cell); report['records'].append(record)
        report['seconds'] = time.monotonic()-start
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(report, indent=2)+'\n')
        print(json.dumps(record), flush=True)
    print(json.dumps(dict(event='selected_continuous_Gram_complete', report=str(args.out.resolve()),
                         report_sha256=sha(args.out), seconds=report['seconds'])), flush=True)


if __name__ == '__main__': main()
