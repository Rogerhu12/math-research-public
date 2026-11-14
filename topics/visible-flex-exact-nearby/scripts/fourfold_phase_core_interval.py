#!/usr/bin/env python3
"""Continuous N/support bounds for one explicitly symmetric R33 input graph.

Closed radial knot spans are covered by complete polynomial Taylor intervals.
Angular node values use outward trigonometry and a direct interval DFT; a
proved angular Lipschitz allowance covers the arcs between every pair of
nodes. Infinite-primitive tail/alias errors are added before geometric
products. This is a geometry certificate, not an exact metric solution.
"""
from __future__ import annotations

import argparse
from bisect import bisect_right
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import time

import numpy as np

from fourfold_interval_scalar import floor_float, ceiling_float, interval_exp
from fourfold_phase_root_interval import (
    Box, SymmetricTarget, stack, sum_box, interval_dot, rational_box,
    sincos, machin_pi, angular_grid,
)
from fourfold_phase_uniform_tail import (
    derivative_coefficients, up, down, add_up, mul_up, power_up,
    exact_iv, endpoint_up, exp_up, weighted_sum_up,
)


class ClosedSpline:
    """Polynomial-span intervals including both endpoints of a closed cell.

The rational midpoint need not itself be a representable binary64 number.
It selects a span by exact comparisons, and interval de Boor encloses the
jet at that exact midpoint. The complete Taylor polynomial then covers the
closed interval, including an endpoint knot. Every used jet order is below
the continuity order at the simple interior knots of these frozen inputs.
"""
    def __init__(self, knots, degree, coefficients):
        t, k = np.asarray(knots), int(degree)
        c = Box.coerce(coefficients)
        low, high = c.lo, c.hi
        self.states = []
        for order in range(k+1):
            self.states.append((t, k-order, low, high,
                [Fraction.from_float(float(v)) for v in t]))
            if order < k:
                t, _, low, high = derivative_coefficients(t, k-order, low, high)

    def jets(self, x, order=3):
        lo, hi = Fraction.from_float(float(x.lo)), Fraction.from_float(float(x.hi))
        midpoint = (lo+hi)/2
        point = rational_box(midpoint)
        coefficients = []
        for t, k, low, high, exact_knots in self.states:
            span = bisect_right(exact_knots, midpoint)-1
            if not (exact_knots[span] <= lo <= hi <= exact_knots[span+1]):
                raise ValueError('closed radial cell crosses an input knot')
            d = [Box(low[span-k+j], high[span-k+j]) for j in range(k+1)]
            for level in range(1, k+1):
                for j in range(k, level-1, -1):
                    index = span-k+j
                    weight = (point-t[index])/(Box(t[index+k-level+1])-t[index])
                    d[j] = (1-weight)*d[j-1]+weight*d[j]
            coefficients.append(d[k])
        displacement = x-point
        answer = []
        for derivative in range(order+1):
            last = len(coefficients)-1-derivative
            value = coefficients[-1]/math.factorial(last)
            for power in range(last-1, -1, -1):
                value = value*displacement+coefficients[derivative+power]/math.factorial(power)
            answer.append(value)
        return stack(answer)


def primitive_spline(knots, degree, coefficients):
    """Exact antiderivative controls enclosed by interval arithmetic."""
    t, k, c = np.asarray(knots), int(degree), Box.coerce(coefficients)
    count = len(t)-k-1
    values = [Box(0.)]
    for j in range(count):
        values.append(values[-1]+c[j]*(Box(t[j+k+1])-t[j])/(k+1))
    return ClosedSpline(np.r_[t[0], t, t[-1]], k+1, stack(values))


def cross(a, b):
    return stack([a[:, 1]*b[:, 2]-a[:, 2]*b[:, 1],
                  a[:, 2]*b[:, 0]-a[:, 0]*b[:, 2],
                  a[:, 0]*b[:, 1]-a[:, 1]*b[:, 0]], axis=-1)


def absolute_coefficient_sum(value):
    return float(sum_box(sum_box(Box(value.abs_upper()), axis=-1), axis=0).hi)


def vector_node_norm_upper(value):
    """Euclidean norm at all enclosed nodes, with a checked square root.

    math.sqrt only proposes an endpoint. The exact rational comparison of
    its square with the binary64 upper input determines whether that endpoint
    is adequate; nextafter increases it until it is a proved upper bound.
    """
    absolute = value.abs_upper()
    squares = mul_up(absolute, absolute)
    squared_norm = np.zeros(squares.shape[:-1])
    for j in range(squares.shape[-1]):
        squared_norm = add_up(squared_norm, squares[..., j])
    bound = float(np.max(squared_norm))
    exact_bound = Fraction.from_float(bound)
    answer = math.sqrt(bound)
    while Fraction.from_float(answer)**2 < exact_bound:
        answer = math.nextafter(answer, math.inf)
    return answer


class CoreTarget(SymmetricTarget):
    def __init__(self, frozen, nodes, angular_nodes):
        super().__init__(frozen, nodes)
        def create(prefix, field='radius_coefficients'):
            return ClosedSpline(frozen[f'{prefix}_knots'], int(frozen[f'{prefix}_degree']),
                                frozen[f'{prefix}_{field}'])
        self.phase = ClosedSpline(frozen['phase_knots'], 5, frozen['phase_coefficients'])
        self.base = create('base')
        self.means = [create(f'mean{j}') for j in range(len(self.alpha))]
        self.shift = create('shift', 'coefficients')
        self.slopes = [ClosedSpline(frozen[f'height{j}_slope_knots'],
                int(frozen[f'height{j}_slope_degree']), frozen[f'height{j}_slope_coefficients'])
                       for j in range(len(self.alpha)+1)]
        height_knots = frozen['height0_slope_knots']
        height_degree = int(frozen['height0_slope_degree'])
        height_controls = Box(frozen['height0_slope_coefficients'])
        for j, parameter in enumerate(self.alpha, 1):
            if not np.array_equal(height_knots, frozen[f'height{j}_slope_knots']):
                raise ValueError('height slope knots differ')
            if int(frozen[f'height{j}_slope_degree']) != height_degree:
                raise ValueError('height slope degrees differ')
            height_controls += parameter*Box(frozen[f'height{j}_slope_coefficients'])
        # The odd height is (primitive(x)-primitive(-x))/2. Its arbitrary
        # integration constant cancels; the frozen numerical primitive is
        # never substituted for the exact integral of the slope input.
        self.height_primitive = primitive_spline(height_knots, height_degree, height_controls)
        if angular_nodes % 4 or angular_nodes <= 2*self.keep:
            raise ValueError('angular cover needs a multiple of four greater than twice keep')
        self.angular_nodes = angular_nodes
        s, c = angular_grid(angular_nodes)
        index = (np.arange(angular_nodes)[:, None]*np.arange(self.keep+1)[None, :]) % angular_nodes
        self.eval_sine = Box(s.lo[index], s.hi[index])
        self.eval_cosine = Box(c.lo[index], c.hi[index])
        self.eval_phase_sine = self.eval_sine[:, 1:self.modes+1]
        self.eval_phase_cosine = self.eval_cosine[:, 1:self.modes+1]
        self.half_angular_gap = float(up(machin_pi().hi/(4*angular_nodes)))

    def height(self, x):
        return (self.height_primitive.jets(x, order=0)[0]
                -self.height_primitive.jets(-x, order=0)[0])*.5

    def physical_tangent_values(self, beta, gamma):
        frequencies = (4*np.arange(1, self.modes+1))[:, None]
        phase = stack([beta[0], gamma[0]], axis=1)
        phase_theta = phase*frequencies
        values = interval_dot(self.eval_phase_sine, phase)
        theta_values = interval_dot(self.eval_phase_cosine, phase_theta)
        b, g = values[:, 0], values[:, 1]
        bt, gt = theta_values[:, 0], theta_values[:, 1]
        sb, cb = sincos(b)
        sg, cg = sincos(g)
        t = stack([-cg*sb, cg*cb, sg], axis=-1)
        # Cylindrical components of the true Cartesian angular derivative.
        tt = stack([sg*gt*sb-cg*cb*(1+bt),
                    -sg*gt*cb-cg*sb*(1+bt), cg*gt], axis=-1)
        return t, tt

    def angular_evaluate(self, coefficients):
        co = interval_dot(self.eval_cosine, coefficients)
        si = interval_dot(self.eval_sine, coefficients)
        return stack([co[:, 0], si[:, 1], co[:, 2]], axis=-1)

    def primitive_errors(self, beta, gamma, radius):
        choices = []
        for sigma, factor in self.tail_factors.items():
            weights = []
            for mode in 4*np.arange(1, self.modes+1):
                v = exact_iv(sigma)*int(mode)
                weights.append(endpoint_up((interval_exp(v)+interval_exp(-v))/2))
            b, g = (weighted_sum_up(v.abs_upper(), weights) for v in (beta, gamma))
            horizontal = mul_up(2, exp_up(add_up(sigma, add_up(b[0], g[0]))))
            vertical = exp_up(g[0])
            mt0 = add_up(horizontal, vertical)
            mt1 = add_up(mul_up(horizontal, add_up(b[1], g[1])), mul_up(vertical, g[1]))
            aa = radius.abs_upper()
            e0 = mul_up(mul_up(aa[0], mt0), factor[0])
            e1 = mul_up(add_up(mul_up(aa[1], mt0), mul_up(aa[0], mt1)), factor[0])
            choices.append((max(e0, e1), sigma, float(e0), float(e1)))
        _, sigma, e0, e1 = min(choices)
        return sigma, e0, e1

    def evaluate_core(self, left, right):
        x = Box(left, right)
        beta, gamma, radius, slope = self.scalars(x)
        primitives = self.primitive(self.tangent(beta, gamma))
        fcoeff = radius[0]*primitives[0]
        fxcoeff = radius[1]*primitives[0]+radius[0]*primitives[1]
        z = self.height(x)
        def add_vertical_mean(coefficients, mean):
            low, high = coefficients.lo.copy(), coefficients.hi.copy()
            value = Box(low[0, 2], high[0, 2])+mean
            low[0, 2], high[0, 2] = value.lo, value.hi
            return Box(low, high)
        fcoeff = add_vertical_mean(fcoeff, z)
        fxcoeff = add_vertical_mean(fxcoeff, slope[0])
        sigma, e0, e1 = self.primitive_errors(beta, gamma, radius)
        f = self.angular_evaluate(fcoeff)+Box(-e0, e0)
        fx = self.angular_evaluate(fxcoeff)+Box(-e1, e1)
        t, tt = self.physical_tangent_values(beta, gamma)
        raw_n = -radius[0]*radius[0]*sum_box(fx*cross(t, tt), axis=1)
        transverse = cross(t, fx)
        support_numerator = radius[0]*sum_box(f*transverse, axis=1)
        ones = np.ones(self.modes)
        frequency = 4*np.arange(1, self.modes+1)
        b0, g0 = beta.abs_upper(), gamma.abs_upper()
        tx = float(add_up(weighted_sum_up(b0[1], ones), weighted_sum_up(g0[1], ones)))
        ttheta = float(add_up(1, add_up(weighted_sum_up(b0[0], frequency),
                                       weighted_sum_up(g0[0], frequency))))
        ttheta2 = float(add_up(add_up(weighted_sum_up(b0[0], frequency**2),
                                      weighted_sum_up(g0[0], frequency**2)),
                               mul_up(ttheta, ttheta)))
        amax = float(radius[0].abs_upper())
        apmax = float(radius[1].abs_upper())
        # Ftheta=aT and Fx_theta=a'T+aTx. These true infinite-object
        # identities fill the arcs for the vector norms themselves.
        fnorm = float(min(add_up(absolute_coefficient_sum(fcoeff), e0),
            add_up(vector_node_norm_upper(f), mul_up(amax, self.half_angular_gap))))
        fx_theta = float(add_up(apmax, mul_up(amax, tx)))
        fxnorm = float(min(add_up(absolute_coefficient_sum(fxcoeff), e1),
            add_up(vector_node_norm_upper(fx), mul_up(fx_theta, self.half_angular_gap))))
        n_lipschitz = float(mul_up(mul_up(amax, amax),
            add_up(mul_up(mul_up(amax, tx), ttheta), mul_up(fxnorm, ttheta2))))
        support_lipschitz = float(mul_up(mul_up(amax, fnorm),
            add_up(mul_up(ttheta, fxnorm), mul_up(amax, tx))))
        n_allowance = float(mul_up(n_lipschitz, self.half_angular_gap))
        support_allowance = float(mul_up(support_lipschitz, self.half_angular_gap))
        n_upper = float(up(np.max(raw_n.hi)+n_allowance))
        numerator_lower = float(down(np.min(support_numerator.lo)-support_allowance))
        transverse_lipschitz = float(add_up(mul_up(ttheta, fxnorm), mul_up(amax, tx)))
        transverse_norm = float(min(fxnorm, add_up(vector_node_norm_upper(transverse),
            mul_up(transverse_lipschitz, self.half_angular_gap))))
        area_upper = float(mul_up(amax, transverse_norm))
        support_lower = float(down(numerator_lower/area_upper)) if numerator_lower > 0 else None
        zeta_denominator = float(mul_up(area_upper, fnorm))
        zeta_lower = float(down(numerator_lower/zeta_denominator)) if numerator_lower > 0 else None
        n_normalized_upper = float(up(n_upper/area_upper)) if n_upper < 0 else None
        return dict(radial_interval=[left, right], a=radius[0].pair(), height=z.pair(),
            raw_N_upper=n_upper, normalized_N_upper=n_normalized_upper,
            support_numerator_lower=numerator_lower, support_lower=support_lower,
            zeta_lower=zeta_lower,
            area_upper=area_upper, F_norm_upper=fnorm, Fx_norm_upper=fxnorm,
            tangent_x_norm_upper=tx, tangent_theta_norm_upper=ttheta,
            tangent_theta2_norm_upper=ttheta2, raw_N_angular_Lipschitz=n_lipschitz,
            support_numerator_angular_Lipschitz=support_lipschitz,
            raw_N_angular_gap_allowance=n_allowance,
            support_numerator_angular_gap_allowance=support_allowance,
            tail_sigma=sigma, F_primitive_tail=e0, Fx_primitive_tail=e1,
            passed=bool(n_upper < 0 and numerator_lower > 0))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inputs', type=Path, required=True)
    ap.add_argument('--core', type=float, default=.25)
    ap.add_argument('--quarter-nodes', type=int, default=256)
    ap.add_argument('--angular-nodes', type=int, default=4096)
    ap.add_argument('--minimum-width', type=float, default=1e-5)
    ap.add_argument('--max-cells', type=int, default=10000)
    ap.add_argument('--resume', action='store_true')
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    if not 0 < args.core < 1:
        raise ValueError('this certificate is for a finite central core')
    with np.load(args.inputs, allow_pickle=False) as saved:
        frozen = {key: saved[key].copy() for key in saved.files}
    config = dict(inputs_sha256=hashlib.sha256(args.inputs.read_bytes()).hexdigest(),
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        core=args.core, quarter_nodes=args.quarter_nodes, angular_nodes=args.angular_nodes,
        minimum_width=args.minimum_width)
    target = CoreTarget(frozen, args.quarter_nodes, args.angular_nodes)
    cuts = np.unique(np.concatenate([np.array([0., args.core])]+[
        np.r_[value, -value] for key, value in frozen.items() if key.endswith('_knots')]))
    cuts = cuts[(cuts >= 0)&(cuts <= args.core)]
    queue = [[float(left), float(right)] for left, right in zip(cuts[:-1], cuts[1:])]
    accepted, failed, attempts, elapsed_previous = [], [], 0, 0.
    if args.resume and args.out.exists():
        old = json.loads(args.out.read_text())
        if old['configuration'] != config:
            raise ValueError('resume configuration/source/input does not match')
        queue, accepted, failed = old['pending'], old['cells'], old['failed_cells']
        attempts, elapsed_previous = old['attempts'], old['elapsed_seconds']
    start = time.monotonic()
    def save():
        report = dict(kind='continuous_symmetric_infinite_R33_core_N_and_support_intervals',
            configuration=config, inputs=str(args.inputs),
            source_checkpoint_sha256=json.loads(str(frozen['metadata']))['checkpoint_sha256'],
            dependency_sha256={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                for name in ['fourfold_phase_root_interval.py','fourfold_phase_uniform_tail.py','fourfold_interval_scalar.py']},
            radial_core=[-args.core, args.core], initial_positive_radial_cells=len(cuts)-1,
            half_angular_gap_upper=target.half_angular_gap, attempts=attempts,
            elapsed_seconds=elapsed_previous+time.monotonic()-start, pending=queue,
            cells=accepted, failed_cells=failed,
            complete=bool(not queue and not failed),
            raw_N_upper=max((r['raw_N_upper'] for r in accepted), default=None),
            normalized_N_upper=max((r['normalized_N_upper'] for r in accepted), default=None),
            support_lower=min((r['support_lower'] for r in accepted), default=None),
            zeta_lower=min((r['zeta_lower'] for r in accepted), default=None),
            limitations=['Only the explicitly symmetrized object associated with this input hash is covered',
                'N and support geometry do not assert an exact radial metric equation, fixed caps, or a closed isometric family',
                'Positive area on this core is independently paid by the scalar gate; normal N here uses the outward orientation Ftheta cross Fx'])
        args.out.parent.mkdir(parents=True, exist_ok=True)
        tmp = args.out.with_suffix(args.out.suffix+'.tmp')
        tmp.write_text(json.dumps(report, indent=2)+'\n')
        tmp.replace(args.out)
        return report
    while queue and attempts < args.max_cells:
        left, right = queue.pop(0)
        result = target.evaluate_core(left, right)
        attempts += 1
        if result['passed']:
            accepted.append(result)
        elif right-left > args.minimum_width:
            middle = float((Fraction.from_float(left)+Fraction.from_float(right))/2)
            if left < middle < right:
                queue[0:0] = [[left, middle], [middle, right]]
            else:
                failed.append(result)
        else:
            failed.append(result)
        if attempts % 10 == 0 or not result['passed'] or not queue:
            report = save()
            print(json.dumps(dict(attempts=attempts, accepted=len(accepted), pending=len(queue),
                failed=len(failed), current=result['radial_interval'],
                raw_N_upper=result['raw_N_upper'], support_lower=result['support_lower'],
                elapsed_seconds=report['elapsed_seconds'])), flush=True)
    report = save()
    print(json.dumps({key:value for key,value in report.items()
                      if key not in ['cells','failed_cells','pending']}, indent=2), flush=True)
    if not report['complete']:
        raise SystemExit('core coverage incomplete; inspect failed cells or resume pending work')


if __name__ == '__main__':
    main()
