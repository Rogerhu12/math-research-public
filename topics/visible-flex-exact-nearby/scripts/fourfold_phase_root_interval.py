#!/usr/bin/env python3
"""Directed local R37 target-root bounds for the explicitly symmetric phase graph.

Uses only frozen scalar spline inputs. Physical a,beta are averaged evenly;
gamma and the exact integral height are averaged oddly. No Gaussian smoothing,
Newton iteration, or implicit mirror assumption about binary64 knots is used.
The target E is the full angular mean of the INFINITE R33 primitive. A small
direct interval DFT plus analytic tail/alias budgets encloses that mean.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from fourfold_interval_scalar import floor_float, ceiling_float, interval_exp, Interval
from fourfold_phase_uniform_tail import (
    derivative_coefficients, up, down, add_up, mul_up, power_up,
    primitive_unit_factors, endpoint_up, exact_iv, exp_up, weighted_sum_up,
)


class Box:
    __array_priority__ = 1000

    def __init__(self, lo, hi=None):
        self.lo = np.asarray(lo, dtype=float)
        self.hi = self.lo.copy() if hi is None else np.asarray(hi, dtype=float)
        if np.any(self.lo > self.hi):
            raise ValueError('reversed interval')

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Box) else Box(value)

    def __add__(self, value):
        value = self.coerce(value)
        return Box(down(self.lo+value.lo), up(self.hi+value.hi))

    __radd__ = __add__

    def __neg__(self):
        return Box(-self.hi, -self.lo)

    def __sub__(self, value):
        return self+-self.coerce(value)

    def __rsub__(self, value):
        return self.coerce(value)+-self

    def __mul__(self, value):
        value = self.coerce(value)
        products = (self.lo*value.lo, self.lo*value.hi,
                    self.hi*value.lo, self.hi*value.hi)
        return Box(down(np.minimum.reduce(products)), up(np.maximum.reduce(products)))

    __rmul__ = __mul__

    def reciprocal(self):
        if np.any((self.lo <= 0)&(self.hi >= 0)):
            raise ZeroDivisionError('interval contains zero')
        return Box(down(1/self.hi), up(1/self.lo))

    def __truediv__(self, value):
        return self*self.coerce(value).reciprocal()

    def __getitem__(self, key):
        return Box(self.lo[key], self.hi[key])

    def reshape(self, *shape):
        return Box(self.lo.reshape(*shape), self.hi.reshape(*shape))

    def transpose(self, *axes):
        return Box(self.lo.transpose(*axes), self.hi.transpose(*axes))

    def abs_upper(self):
        return np.maximum(abs(self.lo), abs(self.hi))

    def pair(self):
        return [float(self.lo), float(self.hi)]


def stack(values, axis=0):
    return Box(np.stack([v.lo for v in values], axis=axis),
               np.stack([v.hi for v in values], axis=axis))


def sum_box(value, axis=0):
    low, high = np.moveaxis(value.lo, axis, 0), np.moveaxis(value.hi, axis, 0)
    result = Box(np.zeros(low.shape[1:]))
    for a, b in zip(low, high):
        result = result+Box(a, b)
    return result


def interval_dot(matrix, values):
    result = Box(np.zeros((matrix.lo.shape[0],)+values.lo.shape[1:]))
    for j in range(matrix.lo.shape[1]):
        result = result+matrix[:, j].reshape(-1, 1)*values[j]
    return result


def rational_box(value):
    return Box(floor_float(value), ceiling_float(value))


def sincos(value):
    """Taylor degree32, rigorous real Lagrange remainder, no libm trig."""
    if np.max(value.abs_upper()) > 2:
        raise ValueError('reduce real trig argument to absolute value <=2')
    sin_value, cos_value = Box(np.zeros_like(value.lo)), Box(np.zeros_like(value.lo))
    for degree in range(32, -1, -1):
        sin_c = Fraction((-1)**((degree-1)//2), math.factorial(degree)) if degree % 2 else Fraction(0)
        cos_c = Fraction((-1)**(degree//2), math.factorial(degree)) if degree % 2 == 0 else Fraction(0)
        sin_value = sin_value*value+rational_box(sin_c)
        cos_value = cos_value*value+rational_box(cos_c)
    remainder = mul_up(power_up(value.abs_upper(), 33),
                       ceiling_float(Fraction(1, math.factorial(33))))
    padding = Box(-remainder, remainder)
    return sin_value+padding, cos_value+padding


def machin_pi():
    def atan_inverse(q, terms):
        z = Fraction(1, q)
        total = sum(((-1)**j*z**(2*j+1)/ (2*j+1) for j in range(terms)), Fraction(0))
        remainder = z**(2*terms+1)/(2*terms+1)
        return (total, total+remainder) if terms % 2 == 0 else (total-remainder, total)
    a, b = atan_inverse(5, 48), atan_inverse(239, 16)
    return Box(floor_float(16*a[0]-4*b[1]), ceiling_float(16*a[1]-4*b[0]))


def angular_grid(nodes):
    pi = machin_pi()
    remainder = np.arange(nodes) % (nodes//4)
    quadrant = 4*np.arange(nodes)//nodes
    angle = pi*Box(2*remainder)/nodes
    s, c = sincos(angle)
    sl, sh, cl, ch = np.empty(nodes), np.empty(nodes), np.empty(nodes), np.empty(nodes)
    choices = [(s, c), (c, -s), (-s, -c), (-c, s)]
    for j, (ss, cc) in enumerate(choices):
        mask = quadrant == j
        sl[mask], sh[mask] = ss.lo[mask], ss.hi[mask]
        cl[mask], ch[mask] = cc.lo[mask], cc.hi[mask]
    return Box(sl, sh), Box(cl, ch)


def jet_product(left, right):
    return stack([sum((math.comb(order, j)*left[j]*right[order-j]
                       for j in range(order+1)), Box(0.)) for order in range(4)])


class SplineBox:
    def __init__(self, knots, coefficients, degree, order=5):
        self.states = []
        t, k, low, high = np.asarray(knots), degree, np.asarray(coefficients), np.asarray(coefficients)
        for derivative in range(order+1):
            self.states.append((t, k, low, high))
            if derivative < order:
                t, k, low, high = derivative_coefficients(t, k, low, high)

    def jets(self, x, order=3):
        center = float((float(x.lo)+float(x.hi))/2)
        point = Box(center)
        coefficients = []
        for t, k, low, high in self.states:
            left_span = int(np.searchsorted(t, float(x.lo), side='right')-1)
            right_span = int(np.searchsorted(t, float(x.hi), side='right')-1)
            if left_span != right_span:
                raise ValueError('radial interval crosses an input knot; subdivide it')
            span = left_span
            d = [Box(low[span-k+j], high[span-k+j]) for j in range(k+1)]
            for level in range(1, k+1):
                for j in range(k, level-1, -1):
                    index = span-k+j
                    weight = (point-t[index])/(Box(t[index+k-level+1])-t[index])
                    d[j] = (1-weight)*d[j-1]+weight*d[j]
            coefficients.append(d[k])
        # On this common span the spline is one polynomial. A centered
        # Taylor form avoids repeating the interval x inside every de Boor
        # weight; all point coefficients are still outward enclosures.
        displacement = x-center
        answer = []
        for derivative in range(order+1):
            last = len(coefficients)-1-derivative
            value = coefficients[-1]/math.factorial(last)
            for power in range(last-1, -1, -1):
                value = value*displacement+coefficients[derivative+power]/math.factorial(power)
            answer.append(value)
        return stack(answer)


class SymmetricTarget:
    def __init__(self, frozen, nodes):
        self.frozen, self.nodes = frozen, nodes
        if nodes % 4 or nodes < 4*frozen['phase_coefficients'].shape[1]+8:
            raise ValueError('quarter node count must be a multiple of four >=4M+8')
        self.alpha = frozen['alpha']
        self.phase = SplineBox(frozen['phase_knots'], frozen['phase_coefficients'], 5)
        self.base = SplineBox(frozen['base_knots'], frozen['base_radius_coefficients'], int(frozen['base_degree']))
        self.means = [SplineBox(frozen[f'mean{j}_knots'], frozen[f'mean{j}_radius_coefficients'],
                                int(frozen[f'mean{j}_degree'])) for j in range(len(self.alpha))]
        self.shift = SplineBox(frozen['shift_knots'], frozen['shift_coefficients'], int(frozen['shift_degree']))
        self.slopes = [SplineBox(frozen[f'height{j}_slope_knots'], frozen[f'height{j}_slope_coefficients'],
                                 int(frozen[f'height{j}_slope_degree'])) for j in range(len(self.alpha)+1)]
        self.modes = frozen['phase_coefficients'].shape[1]
        s, c = angular_grid(nodes)
        phase_indices = (np.arange(nodes)[:, None]*np.arange(1, self.modes+1)[None, :]) % nodes
        self.phase_sine = Box(s.lo[phase_indices], s.hi[phase_indices])
        self.keep = nodes//2-1
        indices = (np.arange(1, self.keep+1)[:, None]*np.arange(nodes)[None, :]) % nodes
        self.sine = Box(s.lo[indices], s.hi[indices])
        self.cosine = Box(c.lo[indices], c.hi[indices])
        self.tail_factors = {sigma: primitive_unit_factors(sigma, 4*nodes, 2*nodes-3)
                             for sigma in [.04, .06, .08]}

    def one_side(self, x):
        base = self.base.jets(x)
        raw = self.phase.jets(x)
        ajet = base.reshape(4, 1, 1)
        beta = raw[:, :, 0]
        gamma = raw[:, :, 1]
        for _ in range(3):
            beta = jet_product(beta, base.reshape(4, 1))
        for _ in range(2):
            gamma = jet_product(gamma, base.reshape(4, 1))
        radius = base+self.shift.jets(x)
        for alpha, sp in zip(self.alpha, self.means):
            radius = radius+alpha*sp.jets(x)
        slope = self.slopes[0].jets(x, order=2)
        for alpha, sp in zip(self.alpha, self.slopes[1:]):
            slope = slope+alpha*sp.jets(x, order=2)
        return beta, gamma, radius, slope

    def scalars(self, x):
        plus, minus = self.one_side(x), self.one_side(-x)
        sign = np.array([1., -1., 1., -1.])
        beta = (plus[0]+minus[0]*sign[:, None])*.5
        gamma = (plus[1]-minus[1]*sign[:, None])*.5
        radius = (plus[2]+minus[2]*sign)*.5
        slope = (plus[3]+minus[3]*sign[:3])*.5
        return beta, gamma, radius, slope

    def tangent(self, beta, gamma):
        b = interval_dot(self.phase_sine, beta.transpose(1, 0))
        g = interval_dot(self.phase_sine, gamma.transpose(1, 0))
        sb, cb = sincos(b[:, 0])
        sg, cg = sincos(g[:, 0])
        zero = Box(np.zeros(self.nodes))
        t = stack([-cg*sb, cg*cb, sg], axis=-1)
        tb = stack([-cg*cb, -cg*sb, zero], axis=-1)
        tg = stack([sg*sb, -sg*cb, cg], axis=-1)
        tbb = stack([cg*sb, -cg*cb, zero], axis=-1)
        tbg = stack([sg*cb, sg*sb, zero], axis=-1)
        tbbg = stack([-sg*sb, sg*cb, zero], axis=-1)
        b1, b2, b3 = [b[:, j].reshape(-1, 1) for j in (1, 2, 3)]
        g1, g2, g3 = [g[:, j].reshape(-1, 1) for j in (1, 2, 3)]
        t1 = tb*b1+tg*g1
        t2 = tb*b2+tg*g2+tbb*b1*b1+2*tbg*b1*g1-t*g1*g1
        t3 = (tb*(b3-b1*b1*b1-3*b1*g1*g1)+tg*(g3-g1*g1*g1)
              +3*tbb*b1*b2+3*tbg*(b2*g1+b1*g2)-3*t*g1*g2+3*tbbg*b1*b1*g1)
        return stack([t, t1, t2, t3], axis=1)

    def primitive(self, tangent):
        sine = interval_dot(self.sine, tangent.reshape(self.nodes, 12))*(Box(2)/self.nodes)
        cosine = interval_dot(self.cosine, tangent.reshape(self.nodes, 12))*(Box(2)/self.nodes)
        sine, cosine = sine.reshape(self.keep, 4, 3), cosine.reshape(self.keep, 4, 3)
        n = (4*np.arange(1, self.keep+1)).reshape(-1, 1)
        aa, bb, cc = sine[:, :, 0], cosine[:, :, 1], sine[:, :, 2]
        uu, vv, ww = -(n*aa+bb)/(n*n-1), (aa+n*bb)/(n*n-1), -cc/n
        modes = stack([uu, vv, ww], axis=-1).transpose(1, 0, 2)
        average = sum_box(tangent[:, :, 1], axis=0)/self.nodes
        mean = stack([average, Box(np.zeros(4)), Box(np.zeros(4))], axis=-1).reshape(4, 1, 3)
        return Box(np.concatenate([mean.lo, modes.lo], axis=1), np.concatenate([mean.hi, modes.hi], axis=1))

    def tail_errors(self, beta, gamma, radius):
        choices = []
        for sigma, factor in self.tail_factors.items():
            weights = []
            for mode in 4*np.arange(1, self.modes+1):
                v = exact_iv(sigma)*int(mode)
                weights.append(endpoint_up((interval_exp(v)+interval_exp(-v))/2))
            b, g = (weighted_sum_up(v.abs_upper(), weights) for v in (beta, gamma))
            def bell(v):
                return np.array([1., v[1], add_up(v[2], mul_up(v[1], v[1])),
                    add_up(add_up(v[3], mul_up(3, mul_up(v[1], v[2]))), power_up(v[1], 3))])
            horizontal = mul_up(2, exp_up(add_up(sigma, add_up(b[0], g[0]))))
            mt = add_up(mul_up(horizontal, bell(add_up(b, g))), mul_up(exp_up(g[0]), bell(g)))
            primitive = mul_up(mt, factor[0])
            aa = radius.abs_upper()
            errors = []
            for order in range(1, 4):
                value = 0.
                for j in range(order+1):
                    value = add_up(value, mul_up(math.comb(order, j), mul_up(aa[j], primitive[order-j])))
                errors.append(float(value))
            choices.append((max(errors), sigma, errors))
        _, sigma, errors = min(choices)
        return sigma, np.asarray(errors)

    def evaluate(self, x):
        beta, gamma, radius, slope = self.scalars(x)
        primitive = self.primitive(self.tangent(beta, gamma))
        fields = []
        for order in range(1, 4):
            value = sum((math.comb(order, j)*radius[j]*primitive[order-j]
                         for j in range(order+1)), Box(0.))
            low, high = value.lo.copy(), value.hi.copy()
            zz = Box(low[0, 2], high[0, 2])+slope[order-1]
            low[0, 2], high[0, 2] = zz.lo, zz.hi
            fields.append(Box(low, high))
        weights = np.r_[1., np.full(self.keep, .5)][:, None]
        def pair(a, b):
            return sum_box(sum_box(a*b*weights, axis=1), axis=0)
        f1, f2, f3 = fields
        ee = [pair(f1, f1), 2*pair(f1, f2), 2*(pair(f2, f2)+pair(f1, f3))]
        sigma, error = self.tail_errors(beta, gamma, radius)
        norms = [float(sum_box(sum_box(Box(v.abs_upper()), axis=1), axis=0).hi) for v in fields]
        l1, l2, l3 = norms
        e1, e2, e3 = error
        corrections = [add_up(mul_up(2*l1, e1), mul_up(e1, e1)),
            mul_up(2, add_up(add_up(mul_up(l1, e2), mul_up(l2, e1)), mul_up(e1, e2))),
            mul_up(2, add_up(add_up(mul_up(2*l2, e2), mul_up(e2, e2)),
                add_up(add_up(mul_up(l1, e3), mul_up(l3, e1)), mul_up(e1, e3))))]
        ee = [value+Box(-pad, pad) for value, pad in zip(ee, corrections)]
        e, ep, epp = ee
        a, ap, app, appp = [radius[j] for j in range(4)]
        c = ap*ep-2*app*e
        cp = ap*epp-app*ep-2*appp*e
        denominator = 2*a*e*e
        kp = cp/denominator-c*(2*ap*e*e+4*a*e*ep)/(denominator*denominator)
        return dict(x=x.pair(), a=a.pair(), E=e.pair(), Eprime=ep.pair(), Esecond=epp.pair(),
                    C=c.pair(), Cprime=cp.pair(), K=(c/denominator).pair(), Kprime=kp.pair(),
                    tail_sigma=sigma, primitive_radial_jet_errors=error.tolist(),
                    angular_mean_corrections=list(map(float, corrections)))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inputs', type=Path, required=True)
    ap.add_argument('--left', type=float, default=.2383698)
    ap.add_argument('--right', type=float, default=.2383701)
    ap.add_argument('--quarter-nodes', type=int, default=256)
    ap.add_argument('--collar-radius', type=float, default=0.)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    with np.load(args.inputs, allow_pickle=False) as saved:
        frozen = {key: saved[key].copy() for key in saved.files}
    target = SymmetricTarget(frozen, args.quarter_nodes)
    rows = [target.evaluate(Box(args.left)), target.evaluate(Box(args.right)),
            target.evaluate(Box(args.left, args.right))]
    knots = []
    for key, value in frozen.items():
        if key.endswith('_knots'):
            knots.extend(value.tolist())
            knots.extend((-value[::-1]).tolist())
    knots = np.unique(knots)
    cell = [float(knots[knots <= args.left].max()), float(knots[knots >= args.right].min())]
    collar = None
    if args.collar_radius:
        center = (args.left+args.right)/2
        lo, hi = float(down(center-args.collar_radius)), float(up(center+args.collar_radius))
        if not cell[0] < lo < hi < cell[1]:
            raise ValueError('requested collar is not inside the common input span')
        collar = target.evaluate(Box(lo, hi))
    success = rows[0]['C'][1] < 0 < rows[1]['C'][0] and rows[2]['Cprime'][0] > 0
    report = dict(kind='directed_local_simple_root_certificate_for_explicitly_symmetric_infinite_phase_target',
        inputs=str(args.inputs), inputs_sha256=hashlib.sha256(args.inputs.read_bytes()).hexdigest(),
        source_checkpoint_sha256=json.loads(str(frozen['metadata']))['checkpoint_sha256'],
        run_source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        dependency_sha256={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                           for name in ['fourfold_interval_scalar.py', 'fourfold_phase_uniform_tail.py']},
        quarter_nodes=args.quarter_nodes, full_circle_nodes=4*args.quarter_nodes,
        radial_symmetry='a,beta even; exact-integral Z and gamma odd, by explicit averaging before R33',
        target='E=<Fx dot Fx> of the infinite primitive, g0=E dx^2+a^2 dtheta^2',
        root_function='C=a_prime E_prime-2 a_second E; C_prime=a_prime E_second-a_second E_prime-2 a_third E',
        evaluations=rows, sign_and_simple_root_gate=success,
        isolating_interval=[args.left, args.right], common_spline_cell=cell,
        distances_to_cell_boundary=[float(down(args.left-cell[0])), float(down(cell[1]-args.right))],
        optional_collar_evaluation=collar,
        limitations=['Local root enclosure only; no exclusion of all other roots on the body',
                     'No actual isometric PDE solution, cap construction or whole transfer inverse',
                     'No claim that an earlier floating return already belongs to this explicitly symmetric object'])
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2), flush=True)
    if not success:
        raise SystemExit('root interval did not pass; keep the failed diagnostic and refine')


if __name__ == '__main__':
    main()
