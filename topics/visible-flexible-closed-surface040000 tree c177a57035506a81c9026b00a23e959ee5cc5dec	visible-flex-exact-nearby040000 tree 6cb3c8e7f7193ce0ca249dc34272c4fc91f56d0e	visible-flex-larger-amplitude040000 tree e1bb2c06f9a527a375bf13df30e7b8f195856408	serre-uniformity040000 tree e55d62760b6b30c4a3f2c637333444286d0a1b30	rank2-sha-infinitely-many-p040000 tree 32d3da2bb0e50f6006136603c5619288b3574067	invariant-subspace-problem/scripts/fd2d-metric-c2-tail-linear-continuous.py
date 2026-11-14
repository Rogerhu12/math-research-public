#!/usr/bin/env python3
"""Continuous outer-tail linear strain for an actual C2 material field.

The saved field is a finite Fourier/shared-two-jet function of physical
radius r and angle u, but its first component p displaces meridian
arclength sigma.  Thus dr/dsigma = k = -1/sqrt(1+w^2).  We enclose
(X*e-g)+Lie_v(g), not the nonlinear pullback.  The original integrated
tail and the same proved background packet supply the actual metric.

Radial partitions of the field, exact tail increments and background
packets are merged. Small metric numerators are combined as interval
polynomials before bounding complete angular arcs. No point sampling,
ODE solver, physical source change, or new tail integration is used.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import bisect
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


def module(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE/filename)
    result = importlib.util.module_from_spec(spec)
    sys.modules[name] = result
    spec.loader.exec_module(result)
    return result


linear = module('fd2d_tail_linear_shared', 'fd2d-metric-c2-field-linear-continuous.py')
stream = module('fd2d_tail_linear_stream', 'db6f-audit-tail-stream.py')
light = module('fd2d_tail_linear_checked_reader', 'fd2d-light-tail-definition-reader.py')
# Preserve all strict exact accumulation and polynomial formulas. Only the
# unused numerical-reader allocations are omitted by this checked adapter.
stream.frozen.IntegratedTail = light.CheckedTailDefinition
I, P, qb, poly = linear.I, linear.P, linear.qb, linear.poly
identity = linear.diff.identity


def convert(p):
    # The two mathematical backends use distinct Python class identities.
    return P(I(p.c.lo, p.c.hi), p.first, p.phase)


def restricted(p, origin, width):
    return P(linear.restrict(p.c, origin, width), p.first, p.phase)


def phase_pair_sum(main, noise, trig):
    return linear.range_poly(main, trig)+linear.range_poly(noise, trig)


class Tail:
    def __init__(self, manifest, packet, field):
        self.manifest_path, self.packet_path = manifest, packet
        self.geom = stream.StreamingExactIntegratedTail(manifest)
        self.field = field
        if field.meta['region'] != 'tail':
            raise ValueError('The actual field is not defined on the tail')
        if field.mesh[0] != Q(float(.4)) or field.mesh[-1] != self.geom.rq[-1]:
            raise ValueError('Expected the complete recorded .4-to-cut activity domain')
        self.packet, self.data, self.packet_data = stream.frozen.load_packet(packet, self.geom)
        self.segments = []
        for row, span_value in enumerate(self.data['span_index']):
            span = int(span_value)
            origin = self.geom.cuff if span == -1 else self.geom.rq[span]
            length = self.geom.collar_length if span == -1 else self.geom.lq[span]
            left = origin+length*Q(float(self.data['u_left'][row]))
            right = origin+length*Q(float(self.data['u_right'][row]))
            self.segments.append((left, right, row, span))
        if any(a[1] != b[0] for a, b in zip(self.segments, self.segments[1:])):
            raise ValueError('The exact physical packet partition has a gap')
        if self.segments[0][0] != self.geom.cuff or self.segments[-1][1] != self.geom.rq[-1]:
            raise ValueError('Background packet omits a physical endpoint')
        begin, end = field.mesh[0], field.mesh[-1]
        packet_cuts = [x for row in self.segments for x in row[:2] if begin <= x <= end]
        self.mesh = sorted(set(field.mesh+packet_cuts))
        self.starts = [row[0] for row in self.segments]
        self.cached_row, self.cached_w = None, None

    def polynomials(self, left, right):
        entry = min(bisect.bisect_right(self.starts, left)-1, len(self.segments)-1)
        pl, pr, row, span = self.segments[entry]
        if not pl <= left < right <= pr:
            raise ValueError('Linear interval crosses a background packet')
        origin = self.geom.cuff if span == -1 else self.geom.rq[span]
        length = self.geom.collar_length if span == -1 else self.geom.lq[span]
        a, b = (left-origin)/length, (right-origin)/length
        fields = [[convert(p) for p in group] for group in self.geom.fields(span, a, b)]
        r = P(linear.diff.base.stack([qb(left), qb(right-left)], 0)[:, None])
        if self.cached_row != row:
            self.cached_w = convert(stream.frozen.poly.target_scalar(self.data, 'w', row))
            self.cached_row = row
        w = restricted(self.cached_w, (left-pl)/(pr-pl), (right-left)/(pr-pl))

        R, T, Z = fields[0]
        Rr, Tr, Zr = fields[1]
        Ru, Tu, Zu = R.theta()-T, R+T.theta(), Z.theta()
        # Identical coefficient-first formulas to the original tail verifier.
        Eres = 2*Rr+Rr*Rr+Tr*Tr+Zr*Zr+2*w*Zr
        Fres = (1+Rr)*Ru+Tr*(r+Tu)+(w+Zr)*Zu
        Gres = Ru*Ru+2*r*Tu+Tu*Tu+Zu*Zu

        wrange = linear.range_poly(w)
        E = 1+wrange.square()
        rootE = E.sqrt()
        k = -I(1.)/rootE
        field = self.field.fields(left, right)
        (pe, po), (qe, qo) = field[0]
        (pre, pro), (qre, qro) = field[1]
        r2 = r*r
        # Upper tail is the z reflection of the stored tail. The sign of the
        # sigma-r cross component changes because sigma increases inward.
        main = (Eres-2*pre*rootE,
                -Fres+pe.theta()*rootE-r2*qro,
                Gres+2*r*pe*k+2*r2*qo.theta())
        noise = (-2*pro*rootE,
                 po.theta()*rootE-r2*qre,
                 2*r*po*k+2*r2*qe.theta())
        return main, noise, r, E, row, span

    def bound(self, left, right, angular):
        main, noise, r, E, row, span = self.polynomials(left, right)
        radius = linear.range_poly(r)
        if radius.lo <= 0 or E.lo <= 0:
            raise ValueError('Nonpositive own target frame')
        modes = max(max(abs(p.first), abs(p.first+p.c.lo.shape[1]-1))
                    for p in (*main, *noise))
        trig = linear.trigonometry(modes, angular)
        a, b, c = [phase_pair_sum(x, y, trig) for x, y in zip(main, noise)]
        normalized = (a/E, b/(radius*E.sqrt()), c/radius.square())
        return linear.matrix_norm(*normalized), row, span


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--manifest', type=Path, required=True)
    ap.add_argument('--packet', type=Path, required=True)
    ap.add_argument('--field', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--rows', type=Path)
    ap.add_argument('--start', type=int, default=0)
    ap.add_argument('--stop', type=int)
    ap.add_argument('--angular', type=int, default=256)
    ap.add_argument('--radial-subdivisions', type=int, default=1)
    ap.add_argument('--threshold', type=float, default=1.9e-9)
    args = ap.parse_args()
    if args.out.exists() or (args.rows is not None and args.rows.exists()):
        raise FileExistsError('Use a new actual report name')
    if args.angular < 1 or args.radial_subdivisions < 1:
        raise ValueError('Positive complete radial and angular partitions required')
    started = time.monotonic()
    field = linear.Field(args.field)
    model = Tail(args.manifest, args.packet, field)
    total = len(model.mesh)-1
    stop = total if args.stop is None else min(total, args.stop)
    if not 0 <= args.start < stop:
        raise ValueError('Invalid selected radial cell range')
    maximum, worst, rows = 0., None, []
    for cell in range(args.start, stop):
        a, b = model.mesh[cell:cell+2]
        for sub in range(args.radial_subdivisions):
            left = a+(b-a)*Q(sub, args.radial_subdivisions)
            right = a+(b-a)*Q(sub+1, args.radial_subdivisions)
            bound, packet_row, span = model.bound(left, right, args.angular)
            row = dict(cell=cell, subdivision=sub, left_exact=str(left), right_exact=str(right),
                       packet_row=packet_row, tail_span=span, linear_operator_upper=bound)
            if bound > maximum:
                maximum, worst = bound, row
            if args.rows is not None:
                rows.append(row)
        if (cell-args.start+1) % 100 == 0:
            print(json.dumps(dict(cells=cell-args.start+1, total=stop-args.start,
                                  maximum=maximum, seconds=time.monotonic()-started)), flush=True)
    complete = args.start == 0 and stop == total
    report = dict(schema='fd2d-continuous-tail-linear-material-residual-v1', scope=__doc__,
                  script=identity(__file__), manifest=identity(args.manifest), packet=identity(args.packet),
                  low_memory_defining_reader=identity(HERE/'fd2d-light-tail-definition-reader.py'),
                  packet_data=identity(model.packet_data), field=identity(args.field), field_bindings=field.bindings,
                  exact_domain=list(map(str, (model.mesh[0], model.mesh[-1]))),
                  total_radial_cells=total, selected_cell_range=[args.start, stop],
                  selected_exact_domain=list(map(str, (model.mesh[args.start], model.mesh[stop]))),
                  selected_radial_cells=stop-args.start, radial_subdivisions=args.radial_subdivisions,
                  angular_arcs_covering_one_threefold_period=args.angular,
                  all_finite_angular_modes_covered=True, complete_tail_activity_domain=complete,
                  linear_operator_upper=maximum, worst_interval=worst,
                  threshold=args.threshold, threshold_met=complete and maximum <= args.threshold,
                  field_coordinates='p is meridian sigma displacement; stored two jets use physical r and u',
                  target_kind='original common rotational tail metric, same frozen background packet',
                  background_definition_hashes=model.packet.get('background_definition_hashes'),
                  nonlinear_pullback_certified=False, deep_tail_included=False, whole_surface_certified=False,
                  seconds=time.monotonic()-started)
    if args.rows is not None:
        if args.rows.suffix != '.gz':
            raise ValueError('Store continuous rows as gzip')
        payload = gzip.compress((json.dumps(rows, separators=(',', ':'))+'\n').encode(), mtime=0)
        if len(payload) >= 5_000_000:
            raise ValueError('Continuous rows exceed the repository per-file limit')
        args.rows.write_bytes(payload)
        report['row_data'] = identity(args.rows)
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(out=str(args.out), linear_operator_upper=maximum, complete=complete,
                          threshold_met=report['threshold_met'], seconds=report['seconds'])), flush=True)


if __name__ == '__main__':
    main()
