#!/usr/bin/env python3
# New 78718 explicit storage adaptation; original mathematical source is retained below.
"""Continuous metric and curvature bounds for an exact integrated finite tail.

The manifest defines V by exact binary nodal derivative data and exact
integration. A separate packet must enclose the same exact background
w(r), w_r(r) on every listed physical interval. This backend verifies the
packet partition and performs coefficient-first residual subtraction; it
does not prove the supplier's analytic claims. The R6 endpoint collar is
span -1. No source solver or approximate radial primitive is imported.
"""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import io
import json
import math
from pathlib import Path
import sys
import time
import numpy as np

from db6f_tail_integrated import IntegratedTail

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location('db6f_tail_metric_poly', HERE/'78718-prefix-metric-polynomial-storage-v1.py')
poly = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = poly
SPEC.loader.exec_module(poly)
base = poly.base
I, P, qbounds, up, down = poly.I, poly.P, poly.qbounds, poly.up, poly.down


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def check(condition, message):
    if not condition:
        raise ValueError(message)


def exact(x):
    return Q.from_float(float(x))


def intervals(values):
    values = [qbounds(x) for x in values]
    return I(np.array([float(x.lo) for x in values]), np.array([float(x.hi) for x in values]))


def real_coefficients(p):
    """Power coefficients of the real cosine or sine representation.

    P.c are real Laurent coefficients multiplied by i**phase. Taking the
    real part combines the opposite frequencies before any range bound.
    """
    degree, width = p.c.lo.shape
    last = p.first+width-1
    M = max(abs(p.first), abs(last))
    zero = I(np.zeros(degree))

    def coefficient(k):
        return p.c[:, k-p.first] if p.first <= k <= last else zero

    c = [coefficient(0) if p.phase == 0 else zero]
    for j in range(1, M+1):
        c.append(coefficient(-j)+coefficient(j) if p.phase == 0
                 else coefficient(-j)-coefficient(j))
    return base.stack(c, 1)


def value_range(p, trig=None):
    """Enclose p on its complete radial interval and each angular arc."""
    c = real_coefficients(p)
    bern = poly.interval_matmul(poly.bernstein_matrix(c.lo.shape[0]-1), c)
    by_mode = I(bern.lo.min(axis=0), bern.hi.max(axis=0))
    if trig is None:
        check(by_mode.lo.size == 1, 'A scalar range needs zero angular frequency')
        return by_mode[0]
    cosine, sine = trig
    count = cosine.lo.shape[1]
    result = I(np.zeros(count))+by_mode[0]
    functions = cosine if p.phase == 0 else sine
    check(by_mode.lo.size-1 <= functions.lo.shape[0], 'Trigonometric table is too short')
    for j in range(1, by_mode.lo.size):
        result = result+by_mode[j]*functions[j-1]
    return result


def vector_range(v, trig):
    return base.stack([value_range(x, trig) for x in v], -1)


def vector_norm_bound(v):
    b = [I(x.norm()) for x in v]
    squares = b[0].square()+b[1].square()+b[2].square()
    # Outward addition can turn the exact lower endpoint 0 into a negative
    # subnormal. The squared Euclidean norm is analytically nonnegative.
    squares = I(np.maximum(0, squares.lo), squares.hi)
    return float(squares.sqrt().hi)


class ExactIntegratedTail:
    """Outward enclosures of the exact manifest-defined polynomial map.

    IntegratedTail is used only as a checked binary-data reader. Its
    long-double value_nodes, r, L and evaluators are deliberately unused.
    """
    def __init__(self, manifest):
        self.path = Path(manifest)
        self.reader = t = IntegratedTail(manifest)
        self.meta = t.meta
        self.N, self.C, self.P = len(t.nodes)-1, t.C, t.P
        check(np.isfinite(t.nodes).all(), 'Nonfinite finite-tail data')
        check(t.first.shape == (self.N+1, self.C), 'Unexpected derivative shape')
        check(self.C == len(t.planar_modes)+len(t.height_modes), 'Mode count mismatch')
        check(len(set(map(int, t.planar_modes))) == self.P, 'Duplicate planar mode')
        check(len(set(map(int, t.height_modes))) == len(t.height_modes), 'Duplicate height mode')
        check(np.all(t.planar_modes % 3 == 1), 'Planar modes must be 1 modulo 3')
        check(np.all(t.height_modes >= 0) and np.all(t.height_modes % 3 == 0),
              'Height modes must be nonnegative multiples of 3')
        self.M = max(max(abs((int(m)-1)//3) for m in t.planar_modes),
                     max(int(m)//3 for m in t.height_modes))
        if t.unscaled_lengths is None:
            self.rq = [exact(r) for r in t.nodes[:, 0]]
            self.lq = [b-a for a, b in zip(self.rq[:-1], self.rq[1:])]
        else:
            radial = t.meta['radialGeometry']
            self.lq = [exact(d)*t.radial_scale for d in t.unscaled_lengths]
            self.rq = [exact(radial['innerAnchor'])]
            for d in self.lq:
                self.rq.append(self.rq[-1]+d)
            check(self.rq[-1] == exact(radial['outerAnchor']),
                  'Exact normalized increments do not reach the declared outer anchor')
        check(all(d > 0 for d in self.lq), 'Nonpositive exact physical span')
        self.cuff = exact(self.meta['parameters']['rCuff'])
        self.collar_length = self.rq[0]-self.cuff
        check(self.cuff > 0 and self.collar_length > 0, 'Invalid R6 collar')
        L = intervals(self.lq)[:, None]
        u0, u1 = I(t.first[:-1]), I(t.first[1:])
        v0, v1 = L*I(t.second[:-1]), L*I(t.second[1:])
        bubble = 16*I(t.midpoint)-8*(u0+u1)-2*(v0-v1)
        G = base.stack([u0, v0, -3*u0+3*u1-2*v0-v1+bubble,
                        2*u0-2*u1+v0+v1-2*bubble, bubble], 1)
        increment = L*(qbounds(Q(7, 30))*(u0+u1)+qbounds(Q(8, 15))*I(t.midpoint)
                       +qbounds(Q(1, 60))*(v0-v1))
        node = I(t.source_values[0])
        vl, vh = [], []
        for j in range(self.N):
            vl.append(node.lo.copy())
            vh.append(node.hi.copy())
            node = node+increment[j]
        V0 = I(np.array(vl), np.array(vh))
        F = base.stack([V0]+[L*G[:, j, :]*qbounds(Q(1, j+1)) for j in range(5)], 1)
        Gp = base.stack([G[:, j+1, :]*(j+1)/L for j in range(4)], 1)
        self.polys = [F, G, Gp]
        self.endpoint_value_enclosure = node

        cl = qbounds(self.collar_length)
        a0, a1, a2 = I(t.source_values[0]), I(t.first[0]), I(t.second[0])
        zero = I(np.zeros(self.C))
        c3 = 10*a0-4*cl*a1+qbounds(Q(1, 2))*cl.square()*a2
        c4 = -15*a0+7*cl*a1-cl.square()*a2
        c5 = 6*a0-3*cl*a1+qbounds(Q(1, 2))*cl.square()*a2
        self.collar = [
            base.stack([zero, zero, zero, c3, c4, c5], 0),
            base.stack([zero, zero, 3*c3/cl, 4*c4/cl, 5*c5/cl], 0),
            base.stack([zero, 6*c3/cl.square(), 12*c4/cl.square(), 20*c5/cl.square()], 0)]

    def interval_radius(self, index, a, b):
        left = self.cuff if index == -1 else self.rq[index]
        length = self.collar_length if index == -1 else self.lq[index]
        c = base.stack([qbounds(left+length*a), qbounds(length*(b-a))], 0)
        return P(c[:, None]), left+length*a, left+length*b

    def expand(self, coefficients):
        degree = coefficients.lo.shape[0]
        shape = (degree, 2*self.M+1)
        fields = [I(np.zeros(shape), np.zeros(shape)) for _ in range(3)]

        def add(axis, frequency, value):
            slot = frequency+self.M
            y = fields[axis][:, slot]+value
            fields[axis].lo[:, slot] = y.lo
            fields[axis].hi[:, slot] = y.hi

        for col, mode in enumerate(self.reader.planar_modes):
            k = (int(mode)-1)//3
            c = coefficients[:, col]
            if k == 0:
                add(0, 0, c)
            else:
                half = c/2
                add(0, k, half)
                add(0, -k, half)
                add(1, -k, half)
                add(1, k, -half)
        for col, mode in enumerate(self.reader.height_modes):
            k = int(mode)//3
            c = coefficients[:, self.P+col]
            if k == 0:
                add(2, 0, c)
            else:
                half = c/2
                add(2, k, half)
                add(2, -k, half)
        return [P(x, -self.M, 1 if axis == 1 else 0) for axis, x in enumerate(fields)]

    def fields(self, index, a, b):
        result = []
        for order in range(3):
            raw = self.collar[order] if index == -1 else self.polys[order][index]
            local = poly.compose(raw, qbounds(a), qbounds(b-a))
            result.append(self.expand(local))
        return result


def load_packet(path, geom):
    path = Path(path)
    meta = json.loads(path.read_text())
    check(meta['finite_tail_manifest_sha256'] == sha(geom.path), 'Packet/manifest hash mismatch')
    data = path.parent/meta['data_file']
    check(sha(data) == meta['data_sha256'], 'Background packet data hash mismatch')
    source = data.read_bytes()
    if source[:2] == b'\x1f\x8b':
        source = gzip.decompress(source)
    raw = np.load(io.BytesIO(source), allow_pickle=False)
    required = ('span_index', 'u_left', 'u_right', 'w_lo', 'w_hi', 'w_remainder',
                'wr_lo', 'wr_hi', 'wr_remainder')
    check(all(k in raw for k in required), 'Incomplete background packet')
    index = raw['span_index']
    left, right = raw['u_left'], raw['u_right']
    check(index.ndim == 1 and np.issubdtype(index.dtype, np.integer), 'Invalid span-index array')
    n = len(index)
    check(n > 0 and left.shape == right.shape == index.shape, 'Invalid partition shapes')
    check(np.isfinite(left).all() and np.isfinite(right).all(), 'Nonfinite local coordinates')
    check(np.all((0 <= left) & (left < right) & (right <= 1)), 'Invalid local partition intervals')
    check(index[0] == -1 and index[-1] == geom.N-1, 'Packet omits an endpoint span')
    previous_index, previous_right = -1, 0.
    for k in range(n):
        i, a, b = int(index[k]), float(left[k]), float(right[k])
        if i == previous_index:
            check(a == previous_right, 'Gap or overlap within a background span')
        else:
            check(i == previous_index+1 and previous_right == 1 and a == 0,
                  'Missing span or mismatched background endpoint')
        previous_index, previous_right = i, b
    check(previous_right == 1, 'Background packet stops before the final endpoint')
    for name in ('w', 'wr'):
        lo, hi, err = raw[name+'_lo'], raw[name+'_hi'], raw[name+'_remainder']
        check(lo.ndim == 2 and lo.shape == hi.shape and lo.shape[0] == n and lo.shape[1] >= 1,
              'Invalid background coefficient shape')
        check(err.shape == (n,), 'Invalid background remainder shape')
        check(np.isfinite(lo).all() and np.isfinite(hi).all() and np.isfinite(err).all()
              and np.all(lo <= hi) and np.all(err >= 0), 'Invalid background enclosure')
    return meta, raw, data


def metric_residuals(fields, r, w):
    R, T, Z = fields[0]
    Rr, Tr, Zr = fields[1]
    angular_R, angular_T, angular_Z = R.theta()-T, R+T.theta(), Z.theta()
    Eres = 2*Rr+Rr*Rr+Tr*Tr+Zr*Zr+2*w*Zr
    Fres = (1+Rr)*angular_R+Tr*(r+angular_T)+(w+Zr)*angular_Z
    Gres = angular_R*angular_R+2*r*angular_T+angular_T*angular_T+angular_Z*angular_Z
    err = [p.norm() for p in (Eres, Fres, Gres)]
    rr, ww = value_range(r), value_range(w)
    E = 1+ww.square()
    check(float(rr.lo) > 0, 'Physical radius lower bound is not positive')
    check(float(E.lo) > 0, 'Background metric lower bound is not positive')
    rmin, Emin = I(float(rr.lo)), I(float(E.lo))
    normalized = [I(err[0])/Emin, I(err[1])/(rmin*Emin.sqrt()), I(err[2])/rmin.square()]
    op = float(max((normalized[0]+normalized[1]).hi, (normalized[1]+normalized[2]).hi))
    return op, err, (Eres, Fres, Gres), rr, ww, E


def perturbative_curvature(fields, r, w, wr, metric, background_curvature):
    """Compare ambient covariant Hessians in the background orthonormal frame."""
    R, T, Z = fields[0]
    Rr, Tr, Zr = fields[1]
    Rrr, Trr, Zrr = fields[2]
    Vr = [Rr, Tr, Zr]
    Vrr = [Rrr, Trr, Zrr]
    Vtheta = [R.theta()-T, R+T.theta(), Z.theta()]
    Vrtheta = [Rr.theta()-Tr, Rr+Tr.theta(), Zr.theta()]
    Vthetatheta = [R.theta().theta()-2*T.theta()-R,
                   2*R.theta()+T.theta().theta()-T, Z.theta().theta()]
    rr, ww, wrr = value_range(r), value_range(w), value_range(wr)
    E = 1+ww.square()
    invE, invr = I(1)/E, I(1)/rr
    gamma = ww*wrr*invE
    H11 = [(a-b*gamma)*invE for a, b in zip(Vrr, Vr)]
    H12 = [(a-b*invr)*(invr/E.sqrt()) for a, b in zip(Vrtheta, Vtheta)]
    H22 = [(a+r*b*invE)*invr.square() for a, b in zip(Vthetatheta, Vr)]
    h = [vector_norm_bound(x) for x in (H11, H12, H22)]
    eta = float(max((I(h[0])+I(h[1])).hi, (I(h[1])+I(h[2])).hi))
    bound = float(((I(background_curvature)+I(eta))/(1-I(metric))).hi) if metric < 1 else None
    return bound, eta, h


def direct_curvature(fields, r, w, wr, trig, metric):
    """Bound the actual shape roots; preserve w_r+Z_rr before range evaluation."""
    R, T, Z = fields[0]
    Rr, Tr, Zr = fields[1]
    Rrr, Trr, Zrr = fields[2]
    Fr = [1+Rr, Tr, w+Zr]
    Ft = [R.theta()-T, r+R+T.theta(), Z.theta()]
    Frr = [Rrr, Trr, wr+Zrr]
    Frt = [Rr.theta()-Tr, 1+Rr+Tr.theta(), Zr.theta()]
    Ftt = [R.theta().theta()-2*T.theta()-R-r,
           2*R.theta()+T.theta().theta()-T, Z.theta().theta()]
    a, b, c, d, e = [vector_range(v, trig) for v in (Fr, Ft, Frr, Frt, Ftt)]
    area = base.cross(a, b)
    length = base.norm(area)
    if metric < 1:
        rr, ww = value_range(r), value_range(w)
        analytic_lower = I(float(rr.lo))*(1+ww.square()).sqrt()*(1-I(metric))
        # Both bounds enclose the same positive area element.
        length = I(np.maximum(length.lo, float(analytic_lower.lo)), length.hi)
    if np.any(length.lo <= 0):
        return None, None
    check(np.all(length.lo <= length.hi), 'Contradictory area enclosures')
    normal = area/length[..., None]
    E, F, G = base.dot(a, a), base.dot(a, b), base.dot(b, b)
    L, M, N = base.dot(c, normal), base.dot(d, normal), base.dot(e, normal)
    det = length.square()
    trace = (L*G-2*M*F+N*E)/det
    gaussian = (L*N-M.square())/det
    discriminant = trace.square()-4*gaussian
    discriminant = I(np.maximum(discriminant.lo, 0), np.maximum(discriminant.hi, 0))
    kappa = (trace.abs()+discriminant.sqrt())/2
    return float(kappa.hi.max()), float(length.lo.min())


def restricted(p, a, b):
    return P(poly.compose(p.c, qbounds(a), qbounds(b-a)), p.first, p.phase)


def run(args):
    started = time.monotonic()
    check(args.angular > 0 and args.radial > 0, 'Positive angular/radial subdivisions required')
    check(math.isfinite(args.background_curvature) and args.background_curvature >= 0,
          'Invalid background curvature input')
    check(math.isfinite(args.direct_threshold) and args.direct_threshold >= 0,
          'Invalid direct-curvature threshold')
    geom = ExactIntegratedTail(args.manifest)
    meta, data, data_path = load_packet(args.packet, geom)
    stop = geom.N if args.maximum_span_exclusive is None else args.maximum_span_exclusive
    check(-1 <= args.minimum_span < stop <= geom.N, 'Invalid selected span range')
    selected = np.flatnonzero((data['span_index'] >= args.minimum_span) & (data['span_index'] < stop))
    if args.limit is not None:
        check(args.limit > 0, 'A pilot limit must be positive')
        selected = selected[:args.limit]
    check(len(selected) > 0, 'No selected packet intervals')
    trig = None
    rows = []
    out = dict(status='continuous-finite-tail-bounds-conditional-on-background-packet', scope=__doc__,
        manifest=str(args.manifest.resolve()), manifest_sha256=sha(args.manifest),
        packet=str(args.packet.resolve()), packet_sha256=sha(args.packet), packet_data_sha256=sha(data_path),
        script_sha256=sha(__file__), polynomial_backend_sha256=sha(HERE/'78718-prefix-metric-polynomial-storage-v1.py'),
        interval_backend_sha256=sha(HERE/'db6f-audit-continuous-hermite.py'),
        reader_sha256=sha(HERE/'db6f_tail_integrated.py'),
        supplier_definition=meta.get('analytic_definition'), supplier_independently_verified=False,
        background_curvature_upper_assumed=args.background_curvature,
        background_curvature_proof=meta.get('background_curvature_proof'),
        total_finite_spans=geom.N, collar_included=args.minimum_span == -1,
        packet_intervals=len(data['span_index']), checked_packet_intervals=len(selected),
        angular_intervals_per_threefold_period=args.angular, radial_subdivisions=args.radial,
        selected_span_interval=[args.minimum_span, stop], metric_operator_upper=0.,
        coordinate_residual_upper=[0., 0., 0.], principal_curvature_upper=0.,
        curvature_all_checked_intervals_resolved=True, area_element_lower_from_direct=None,
        direct_curvature_calls=0, perturbative_curvature_wins=0, direct_curvature_wins=0,
        worst_metric_packet=None, worst_curvature_packet=None,
        entire_finite_tail_and_collar_covered=(args.minimum_span == -1 and stop == geom.N
                                             and len(selected) == len(data['span_index'])),
        complete_closed_surface=False,
        not_certified=['analytic validity of supplier packets', 'background curvature theorem',
                       'nonlinear infinite-tail solution', 'complete closed-surface metric or reach',
                       'README completion'])
    for row in selected:
        span = int(data['span_index'][row])
        ua, ub = exact(data['u_left'][row]), exact(data['u_right'][row])
        w0, wr0 = (poly.target_scalar(data, name, row) for name in ('w', 'wr'))
        result = dict(packet_row=int(row), span_index=span, metric_operator_upper=0.,
                      principal_curvature_upper=0., covariant_hessian_upper=0.,
                      direct_curvature_upper=None, perturbative_curvature_upper=None,
                      curvature_resolved=True)
        for child in range(args.radial):
            a, b = Q(child, args.radial), Q(child+1, args.radial)
            left, right = ua+(ub-ua)*a, ua+(ub-ua)*b
            fields = geom.fields(span, left, right)
            r, physical_left, physical_right = geom.interval_radius(span, left, right)
            w, wr = restricted(w0, a, b), restricted(wr0, a, b)
            metric, errors, _, _, _, _ = metric_residuals(fields, r, w)
            kp, eta, h = perturbative_curvature(fields, r, w, wr, metric, args.background_curvature)
            kd, area = None, None
            if kp is None or kp > args.direct_threshold:
                if trig is None:
                    trig = base.trigonometry(geom.M, args.angular)
                kd, area = direct_curvature(fields, r, w, wr, trig, metric)
                out['direct_curvature_calls'] += 1
            choices = [x for x in (kp, kd) if x is not None and math.isfinite(x)]
            kappa = min(choices) if choices else None
            if kappa is None:
                out['curvature_all_checked_intervals_resolved'] = False
                result['curvature_resolved'] = False
            else:
                result['principal_curvature_upper'] = max(result['principal_curvature_upper'], kappa)
                if kp is not None and kappa == kp:
                    out['perturbative_curvature_wins'] += 1
                else:
                    out['direct_curvature_wins'] += 1
                if kappa > out['principal_curvature_upper']:
                    out['principal_curvature_upper'] = kappa
                    out['worst_curvature_packet'] = dict(row=int(row), span=span, child=child)
            result['metric_operator_upper'] = max(result['metric_operator_upper'], metric)
            result['covariant_hessian_upper'] = max(result['covariant_hessian_upper'], eta)
            for name, value in [('direct_curvature_upper', kd), ('perturbative_curvature_upper', kp)]:
                if value is not None:
                    result[name] = max(result[name] or 0., value)
            if metric > out['metric_operator_upper']:
                out['metric_operator_upper'] = metric
                out['worst_metric_packet'] = dict(row=int(row), span=span, child=child)
            out['coordinate_residual_upper'] = [max(x, y) for x, y in zip(out['coordinate_residual_upper'], errors)]
            if area is not None:
                out['area_element_lower_from_direct'] = min(out['area_element_lower_from_direct'] or area, area)
        rows.append(result)
        if args.progress and len(rows) % args.progress == 0:
            print(json.dumps(dict(checked=len(rows), total=len(selected), metric=out['metric_operator_upper'],
                                  curvature=out['principal_curvature_upper'])), flush=True)
    out['metric_immersion_certified_on_checked_intervals'] = out['metric_operator_upper'] < 1
    if not out['curvature_all_checked_intervals_resolved']:
        out['principal_curvature_upper'] = None
    out['seconds'] = time.monotonic()-started
    row_file = args.out.with_suffix('.rows.json.gz')
    row_file.write_bytes(gzip.compress(json.dumps(rows, separators=(',', ':'), allow_nan=False).encode(), mtime=0))
    check(row_file.stat().st_size < 5_000_000, 'Row report exceeds the repository file-size limit')
    out['row_data_file'], out['row_data_sha256'] = row_file.name, sha(row_file)
    args.out.write_text(json.dumps(out, indent=2, allow_nan=False)+'\n')
    print(json.dumps({key: out[key] for key in ('checked_packet_intervals', 'entire_finite_tail_and_collar_covered',
          'metric_operator_upper', 'principal_curvature_upper', 'curvature_all_checked_intervals_resolved',
          'direct_curvature_calls', 'seconds')}))


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--manifest', type=Path, required=True)
    ap.add_argument('--packet', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--angular', type=int, default=128)
    ap.add_argument('--radial', type=int, default=1)
    ap.add_argument('--background-curvature', type=float, default=6.)
    ap.add_argument('--direct-threshold', type=float, default=6.35,
                    help='Compute direct curvature when the perturbative upper bound exceeds this value')
    ap.add_argument('--minimum-span', type=int, default=-1)
    ap.add_argument('--maximum-span-exclusive', type=int)
    ap.add_argument('--limit', type=int, help='Pilot number of packet rows; complete coverage will be false')
    ap.add_argument('--progress', type=int, default=100)
    run(ap.parse_args())
