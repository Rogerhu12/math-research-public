#!/usr/bin/env python3
"""A NEW exact FullHold tail input with unbounded valley/peak contrasts.

This is an input factory and scalar enclosure, not a nonlinear surface solve.
It preserves the old scalar through S-out/4 and defines the remaining tail
by an explicit positive, infinitely oscillating flat angle.  The cap radius
and height increment are NEW exact integrals.  Old surface/metric/geometry
certificates must not be attached to this input.

All scientific execution is restricted to this public repository's Actions.
No calculation or dependency import occurs merely by importing this module.
"""
from fractions import Fraction as Q
from functools import lru_cache
from math import comb, factorial
from pathlib import Path
import argparse
import gzip
import hashlib
import heapq
import importlib.util
import json
import os
import time

SCHEMA = 'fullhold-deep-valley-flat-tail-input-v1'
FULLHOLD_SHA = 'a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670'
INTEGER_SHA = 'babd589d07c91d8067f9ef2011ae53712aaf6dbdbe22bed25c29116771b237a0'
HOLD_SHA = 'ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1'
SCALE = 10**72
ZERO = (0, 0)
ONE = (SCALE, SCALE)


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific scalar input construction belongs only in public repository Actions')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def identity(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                     allow_nan=False).encode()).hexdigest()


def floor(value):
    return value.numerator // value.denominator


def ceil(value):
    return -((-value.numerator) // value.denominator)


def box(low, high=None):
    low, high = Q(low), Q(low if high is None else high)
    if low > high:
        raise ValueError('Reversed exact scalar interval')
    return floor(low*SCALE), ceil(high*SCALE)


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def neg(a):
    return -a[1], -a[0]


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    products = [x*y for x in a for y in b]
    return min(products)//SCALE, -((-max(products))//SCALE)


def scale(a, factor):
    values = [Q(factor)*value for value in a]
    return floor(min(values)), ceil(max(values))


def inverse(a):
    if a[0] <= 0:
        raise ValueError('A strictly positive scalar interval is required')
    return floor(Q(SCALE*SCALE, a[1])), ceil(Q(SCALE*SCALE, a[0]))


def intersect(a, b):
    result = max(a[0], b[0]), min(a[1], b[1])
    if result[0] > result[1]:
        raise ArithmeticError('Independent outward scalar enclosures disagree')
    return result


def hull(values):
    return min(value[0] for value in values), max(value[1] for value in values)


def magnitude(a):
    return Q(max(abs(a[0]), abs(a[1])), SCALE)


def enclosure(a):
    return dict(lower_exact=str(Q(a[0], SCALE)), upper_exact=str(Q(a[1], SCALE)),
                approximate=[float(Q(a[0], SCALE)), float(Q(a[1], SCALE))])


@lru_cache(maxsize=1)
def pi_box():
    def atan_inverse(n):
        partial = sum((Q((-1)**k, (2*k+1)*n**(2*k+1))
                       for k in range(128)), Q(0))
        return partial, partial+Q(1, 257*n**257)
    low, high = atan_inverse(5), atan_inverse(239)
    return box(16*low[0]-4*high[1], 16*low[1]-4*high[0])


def sine_cosine(a):
    """Range reduction by an enclosed pi; Lipschitz transport of all width."""
    if a[1]-a[0] >= 2*SCALE:
        return (-SCALE, SCALE), (-SCALE, SCALE)
    pi = pi_box()
    midpoint = Q(a[0]+a[1], 2*SCALE)
    pi_midpoint = Q(pi[0]+pi[1], 2*SCALE)
    turns = floor(midpoint/(2*pi_midpoint)+Q(1, 2))
    reduced = sub(a, scale(pi, 2*turns))
    X = (reduced[0]+reduced[1])//2
    radius = max(X-reduced[0], reduced[1]-X)
    if abs(X) > 4*SCALE:
        raise ArithmeticError('Enclosed trigonometric reduction exceeded its Taylor domain')
    # 4^193/193! < 10^-72 pays both Taylor remainders.  Every rounding
    # in the recurrence is also enclosed, independently of that remainder.
    if 4**193*SCALE >= factorial(193):
        raise ArithmeticError('The fixed trigonometric remainder is not one unit')
    def series(sine):
        term = (X, X) if sine else ONE
        total = term
        for j in range(1, 97):
            divisor = (2*j)*(2*j+1) if sine else (2*j-1)*(2*j)
            denominator = SCALE*SCALE*divisor
            term = ((-term[1]*X*X)//denominator,
                    -((-(-term[0]*X*X))//denominator))
            total = add(total, term)
        return intersect((total[0]-radius-1, total[1]+radius+1), (-SCALE, SCALE))
    return series(True), series(False)


def exp_negative(a):
    """Outward exp on a nonpositive interval, using scaled alternating sums."""
    if a[1] > 0:
        raise ValueError('This explicit exponential kernel needs a nonpositive argument')
    def point(u):
        if u < 0:
            raise ValueError('exp(-u) requires u >= 0')
        halvings = 0
        y = u
        while y > Q(1, 2):
            y /= 2
            halvings += 1
        total, term = Q(1), Q(1)
        for k in range(1, 65):
            term *= -y/k
            total += term
        next_term = y**65/factorial(65)
        result = box(total-next_term, total)
        for _ in range(halvings):
            result = mul(result, result)
        return intersect(result, (0, SCALE))
    low = point(-Q(a[0], SCALE))
    high = point(-Q(a[1], SCALE))
    return low[0], high[1]


def constant(value, order=4):
    return [box(value)]+[ZERO]*order


def jadd(a, b):
    return [add(x, y) for x, y in zip(a, b)]


def jscale(a, factor):
    return [scale(value, factor) for value in a]


def jmul(a, b):
    return [sum_intervals(mul(a[k], b[n-k]) for k in range(n+1))
            for n in range(len(a))]


def sum_intervals(values):
    result = ZERO
    for value in values:
        result = add(result, value)
    return result


def jpower(a, power):
    if power < 0:
        inv = [inverse(a[0])]
        for n in range(1, len(a)):
            inv.append(neg(mul(inv[0], sum_intervals(
                mul(a[k], inv[n-k]) for k in range(1, n+1)))))
        return jpower(inv, -power)
    result = constant(1, len(a)-1)
    for _ in range(power):
        result = jmul(result, a)
    return result


def jsine_cosine(a):
    sn, cs = sine_cosine(a[0])
    sine, cosine = [sn], [cs]
    for n in range(1, len(a)):
        sine.append(scale(sum_intervals(scale(mul(a[k], cosine[n-k]), k)
                                        for k in range(1, n+1)), Q(1, n)))
        cosine.append(scale(sum_intervals(scale(mul(a[k], sine[n-k]), -k)
                                          for k in range(1, n+1)), Q(1, n)))
    return sine, cosine


def jexp_negative(a):
    result = [exp_negative(a[0])]
    for n in range(1, len(a)):
        result.append(scale(sum_intervals(scale(mul(a[k], result[n-k]), k)
                                           for k in range(1, n+1)), Q(1, n)))
    return result


def polynomial_add(a, b):
    result = dict(a)
    for power, coefficient in b.items():
        result[power] = result.get(power, Q(0))+coefficient
    return {power: value for power, value in result.items() if value}


def polynomial_scale(a, factor, shift=0):
    return {power+shift: factor*coefficient for power, coefficient in a.items()}


def polynomial_derivative(a):
    return {power-1: power*coefficient for power, coefficient in a.items() if power}


def polynomial_multiply(a, b):
    result = {}
    for p, c in a.items():
        for q, d in b.items():
            result[p+q] = result.get(p+q, Q(0))+c*d
    return result


def tail_derivative_envelopes(epsilon, amplitude, width, orders=4):
    """Complete Bell-polynomial bounds on 0<x<=epsilon; no sampled turns."""
    epsilon = Q(epsilon)
    if not 0 < epsilon <= Q(1, 8):
        raise ValueError('The analytic infinite-tail cutoff must lie in (0,1/8]')
    # g=-x^-2-x^-4-x^-4 sin(x^-4).  Each derivative is A+B sin+C cos.
    A, B, C = {-2: Q(-1), -4: Q(-1)}, {-4: Q(-1)}, {}
    G = [None]
    for _ in range(orders):
        A, B, C = (polynomial_derivative(A),
            polynomial_add(polynomial_derivative(B), polynomial_scale(C, 4, -5)),
            polynomial_add(polynomial_derivative(C), polynomial_scale(B, -4, -5)))
        absolute = {}
        for piece in (A, B, C):
            absolute = polynomial_add(absolute, {p: abs(v) for p, v in piece.items()})
        G.append(absolute)
    bells = [{0: Q(1)}]
    for n in range(orders):
        result = {}
        for j in range(n+1):
            product = polynomial_multiply(bells[n-j], G[j+1])
            result = polynomial_add(result, polynomial_scale(product, comb(n, j)))
        bells.append(result)
    exp_upper = Q(3, 8)**floor(1/epsilon**2)
    bounds = []
    for order, polynomial in enumerate(bells):
        max_inverse_power = max(-power for power in polynomial)
        if max_inverse_power > 2/epsilon**2:
            raise ValueError('Choose a smaller cutoff for the requested derivative order')
        # x^-p exp(-x^-2) is increasing here.  exp(g)<=exp(-x^-2).
        bound = sum((coefficient*epsilon**power for power, coefficient in polynomial.items()), Q(0))
        bounds.append(amplitude*exp_upper*bound/width**order)
    return bounds


class DeepValleyTail:
    """Exact NEW tail plus reusable complete scalar integral enclosures.

    reference_at_affine(alpha,beta) returns outward (a,a_s,a_ss,I,I_s,I_ss)
    at the exact old symbolic point alpha*S+beta.  It is the complete scalar
    interface needed by an explicitly NEW R671-style factory.  The old
    canonical reader intentionally does not accept this new model schema.
    """
    def __init__(self, full, *, input_identity, epsilon=Q(1, 8),
                 integral_tolerance=Q('1e-18'), admission_seconds=300):
        require_actions()
        if integral_tolerance <= 0 or admission_seconds <= 0:
            raise ValueError('Positive explicit enclosure accuracy/admission budget required')
        self.old = full
        self.width, self.kappa = Q(full.out), Q(full.kp)
        if self.kappa != Q(3, 2) or not 0 < self.width < Q(1, 40):
            raise ValueError('The proved replacement is for this original FullHold out ramp')
        self.amplitude = self.kappa*self.width
        self.epsilon = Q(epsilon)
        self.tail_bounds = tail_derivative_envelopes(self.epsilon, self.amplitude,
                                                    self.width, orders=4)
        self.input_identity = input_identity
        self.definition = dict(schema=SCHEMA, original_input=input_identity,
            S_definition='The SAME exact original FullHold terminal S',
            out_width_exact=str(self.width), plateau_curvature_exact=str(self.kappa),
            amplitude_exact=str(self.amplitude), x_definition='x=(S-s)/out_width',
            old_angle='kappa*out_width*(5*x^4/2-3*x^5+x^6)',
            deep_angle='kappa*out_width*exp(-x^-2-x^-4*(1+sin(x^-4)))',
            cutoff='chi=1 for x<=1/8; chi=1-S5(8*x-1) for 1/8<x<1/4; chi=0 for x>=1/4',
            S5='10*u^3-15*u^4+6*u^5',
            angle='beta=(1-chi)*old_angle+chi*deep_angle; beta(0)=0',
            radial='a_new(S-t)=a_old(S-out_width/4)-Integral[t,out_width/4] cos(beta(v)) dv',
            height='Z_new(S-t)=Z_old(S-out_width/4)+Integral[t,out_width/4] sin(beta(v)) dv',
            prefix='Original FullHold a and Z unchanged for s<=S-out_width/4',
            I='Z_new(S)-Z_new(s), defined by the complete explicit integrals',
            scalar_target='ds^2+a_new(s)^2*dtheta^2; explicitly a NEW metric input',
            source_sha256=sha(__file__))
        self.model_identity_sha256 = identity(self.definition)
        self.integration_started = time.monotonic()
        self.integration_tolerance = Q(integral_tolerance)
        self.admission_seconds = float(admission_seconds)
        self._integral_cache = {}
        self._build_integral_table()
        anchor = full.affine_time(1, -self.width/4)
        radius, height = full.at_box(anchor)
        if height is None:
            raise ValueError('The replacement anchor must lie inside the original Hold')
        self.anchor_radius = self._from_old(radius)
        self.anchor_height = self._from_old(height)
        cosine, sine = self.integrals(Q(1, 4))
        self.R = sub(self.anchor_radius, cosine)
        self.height_increment = add(self.anchor_height, sine)
        self.height_change = sub(self.height_increment, self._from_old(full.height_increment))

    def _from_old(self, value):
        return box(Q(value[0], self.old.h.S), Q(value[1], self.old.h.S))

    def _beta_jets(self, low, high=None, order=4):
        low, high = Q(low), Q(low if high is None else high)
        if not 0 < low <= high <= 1:
            raise ValueError('Finite tail jet pieces require 0<x<=1')
        if (low < Q(1, 8) < high) or (low < Q(1, 4) < high):
            raise ValueError('Split a jet piece at both exact cutoff knots')
        x = [box(low, high), ONE]+[ZERO]*(order-1)
        old = jscale(jadd(jadd(jscale(jpower(x, 4), Q(5, 2)),
                               jscale(jpower(x, 5), -3)), jpower(x, 6)), self.amplitude)
        if low >= Q(1, 4):
            return old
        inverse4 = jpower(x, -4)
        phase_sine, _ = jsine_cosine(inverse4)
        positive = jadd(constant(1, order), phase_sine)
        positive[0] = intersect(positive[0], (0, 2*SCALE))
        exponent = jscale(jadd(jpower(x, -2), jmul(inverse4, positive)), -1)
        exponent[0] = intersect(exponent[0], (exponent[0][0], 0))
        deep = jscale(jexp_negative(exponent), self.amplitude)
        if high <= Q(1, 8):
            return deep
        u = jadd(jscale(x, 8), constant(-1, order))
        smooth = jadd(jadd(jscale(jpower(u, 3), 10),
                          jscale(jpower(u, 4), -15)), jscale(jpower(u, 5), 6))
        smooth[0] = intersect(smooth[0], (0, SCALE))
        chi = jadd(constant(1, order), jscale(smooth, -1))
        result = jadd(jmul(smooth, old), jmul(chi, deep))
        result[0] = intersect(result[0], box(0, self.amplitude*Q(29, 4096)))
        return result

    def _leaf(self, low, high):
        width = high-low
        if width <= 0:
            raise ValueError('A scalar integral leaf must have positive exact width')
        bjets = self._beta_jets(low, high)
        sine_jets, cosine_jets = jsine_cosine(bjets)
        points = []
        for x in (low, (low+high)/2, high):
            beta = self._beta_jets(x)[0]
            points.append(sine_cosine(beta))
        values = []
        for component, jets in ((1, cosine_jets), (0, sine_jets)):
            weighted = add(add(points[0][component], scale(points[1][component], 4)),
                           points[2][component])
            simpson = scale(weighted, width/6)
            # jets[4]=f''''/4!; Simpson remainder width^5*f''''/2880.
            error = magnitude(jets[4])*width**5/120
            simpson = add(simpson, box(-error, error))
            rectangle = scale(jets[0], width)
            values.append(intersect(simpson, rectangle))
        return dict(low=low, high=high, values=tuple(values))

    def _tail_integrals(self, x):
        if not 0 <= x <= self.epsilon:
            raise ValueError('The complete infinite-tail box has a declared fixed domain')
        b0 = self.tail_bounds[0]
        return box(x*(1-b0*b0/2), x), box(0, x*b0)

    def _build_integral_table(self):
        tail = self._tail_integrals(self.epsilon)
        points = sorted(set((self.epsilon, Q(1, 8), Q(1, 4))))
        live, heap, sequence = {}, [], 0
        total = list(tail)
        def admit(leaf):
            nonlocal sequence
            sequence += 1
            live[sequence] = leaf
            width = sum(value[1]-value[0] for value in leaf['values'])
            heapq.heappush(heap, (-width, sequence))
            for j in range(2):
                total[j] = add(total[j], leaf['values'][j])
        for low, high in zip(points, points[1:]):
            admit(self._leaf(low, high))
        count = len(live)
        while heap:
            uncertainty = max(Q(value[1]-value[0], SCALE)*self.width for value in total)
            if uncertainty <= self.integration_tolerance:
                break
            if time.monotonic()-self.integration_started >= self.admission_seconds:
                break
            _, key = heapq.heappop(heap)
            leaf = live.pop(key)
            for j in range(2):
                # Remove interval endpoint sums exactly; interval subtraction
                # would add the old leaf's uncertainty a second time.
                total[j] = (total[j][0]-leaf['values'][j][0],
                            total[j][1]-leaf['values'][j][1])
            middle = (leaf['low']+leaf['high'])/2
            admit(self._leaf(leaf['low'], middle))
            admit(self._leaf(middle, leaf['high']))
            count += 2
        self.leaves = sorted(live.values(), key=lambda leaf: leaf['low'])
        self.total_integrals_dimensionless = tuple(total)
        self.leaves_evaluated = count
        self.integral_uncertainty = max(Q(value[1]-value[0], SCALE)*self.width for value in total)
        self.requested_integral_accuracy_reached = self.integral_uncertainty <= self.integration_tolerance

    def integrals(self, x):
        """Outward integrals in physical t from the cap to x*out_width."""
        x = Q(x)
        if not 0 <= x <= Q(1, 4):
            raise ValueError('New scalar integral outside the replacement interval')
        if x in self._integral_cache:
            return self._integral_cache[x]
        if x <= self.epsilon:
            result = self._tail_integrals(x)
        else:
            result = list(self._tail_integrals(self.epsilon))
            for leaf in self.leaves:
                if x <= leaf['low']:
                    break
                values = leaf['values'] if leaf['high'] <= x else self._leaf(leaf['low'], x)['values']
                for j in range(2):
                    result[j] = add(result[j], values[j])
                if x <= leaf['high']:
                    break
        result = tuple(scale(value, self.width) for value in result)
        self._integral_cache[x] = result
        return result

    def beta_and_curvature(self, low, high):
        low, high = Q(low), Q(high)
        if not 0 <= low <= high <= Q(1, 4):
            raise ValueError('New angle query outside the exact replacement tail')
        if high == 0:
            return ZERO, ZERO
        pieces = []
        if low < self.epsilon:
            pieces.append((box(0, self.tail_bounds[0]),
                           box(-self.tail_bounds[1], self.tail_bounds[1])))
        start = max(low, self.epsilon)
        if high > start:
            points = sorted(set([start, high]+[q for q in (Q(1, 8), Q(1, 4)) if start < q < high]))
            for left, right in zip(points, points[1:]):
                jet = self._beta_jets(left, right)
                pieces.append((jet[0], scale(jet[1], 1/self.width)))
        elif low >= self.epsilon:
            jet = self._beta_jets(low)
            pieces.append((jet[0], scale(jet[1], 1/self.width)))
        return hull([piece[0] for piece in pieces]), hull([piece[1] for piece in pieces])

    def _old_angle_curvature(self, sbox):
        """The unchanged original FullHold formula, through its old integer oracle."""
        p, h, o = self.old, self.old.h, self.old.o
        lo, hi = Q(sbox[0], h.S), Q(sbox[1], h.S)
        kmax = Q(5, 2)
        kprime = Q(4653, 1000)*Q(15, 8)/p.f
        endpoint_k = [p.K, h.interval(p.kn), h.interval(p.kn),
                      h.interval(p.kp), h.interval(p.kp), h.interval(Q(0))]
        for j, boundary in enumerate(p.time):
            left, right = Q(boundary[0], h.S), Q(boundary[1], h.S)
            if lo <= right and hi >= left:
                fee = max(abs(lo-right), abs(hi-left))
                return (h.add(p.alpha[j], o.box(-kmax*fee, kmax*fee)),
                        h.add(endpoint_k[j], o.box(-kprime*fee, kprime*fee)))
        j = next((i for i in range(5) if lo > Q(p.time[i][1], h.S)
                  and hi < Q(p.time[i+1][0], h.S)), None)
        if j is None:
            raise ValueError('Original reference query lies outside one Hold segment')
        tbox = o.subtract(sbox, p.time[j])
        if j not in p.ramps:
            k = p.kn if j == 1 else p.kp
            return o.subtract(p.alpha[j], h.scale(tbox, k)), h.interval(k)
        ramp = p.ramps[j]
        tl, th = Q(tbox[0], h.S), Q(tbox[1], h.S)
        mid, radius = (tl+th)/2, (th-tl)/2
        u = mid/ramp.width
        smooth = 10*u**3-15*u**4+6*u**5
        k = h.add(h.scale(ramp.left, 1-smooth), h.scale(ramp.right, smooth))
        return (h.add(ramp.angle(mid), o.box(-kmax*radius, kmax*radius)),
                h.add(k, o.box(-kprime*radius, kprime*radius)))

    def reference_at_affine(self, alpha, beta):
        """Same symbolic location; new exact (a,a_s,a_ss,I,I_s,I_ss) boxes."""
        require_actions()
        alpha, beta = Q(alpha), Q(beta)
        p, h = self.old, self.old.h
        if alpha == 1:
            t = box(-beta)
        else:
            t = sub(scale(self._from_old(p.S), 1-alpha), box(beta))
        tl, th = Q(t[0], SCALE), Q(t[1], SCALE)
        if th < 0:
            raise ValueError('A new reference point lies past the cap')
        if tl >= self.width/4:
            sbox = p.affine_time(alpha, beta)
            a, increment = p.at_box(sbox)
            if increment is None:
                raise ValueError('Reference I is queried only in the original Hold')
            angle, curvature = self._old_angle_curvature(sbox)
            b, c = h.sine_cosine(angle)
            K = self._from_old(curvature)
            b, c = self._from_old(b), self._from_old(c)
            return (self._from_old(a), b, neg(mul(K, c)),
                    sub(self.height_increment, self._from_old(increment)),
                    neg(c), neg(mul(K, b)))
        if tl < 0:
            raise ValueError('The query point box extends past the exact cap endpoint')
        if th > self.width/4:
            # The exact symbolic point may have a narrow S-box straddling
            # the new anchor.  Its value is NOT obtained by choosing one
            # branch from a floating midpoint.  Pay both physical pieces.
            if th > self.width:
                raise ValueError('The anchor-spanning point box extends beyond the original out ramp')
            anchor = self.width/4
            fee = max(anchor-tl, th-anchor)
            integral_sin = self.integrals(Q(1, 4))[1]
            a = add(self.anchor_radius, box(-fee, fee))
            integral_sin = add(integral_sin, box(-fee, fee))
            left_angle, left_curvature = self.beta_and_curvature(tl/self.width, Q(1, 4))
            right = self._beta_jets(Q(1, 4), th/self.width)
            angle = hull((left_angle, right[0]))
            curvature = hull((left_curvature, scale(right[1], 1/self.width)))
            sine, cosine = sine_cosine(angle)
            return (a, neg(cosine), neg(mul(curvature, sine)),
                    integral_sin, neg(sine), mul(curvature, cosine))
        if th == 0:
            return self.R, box(-1), ZERO, ZERO, ZERO, ZERO
        middle, radius = (tl+th)/2, (th-tl)/2
        integral_cos, integral_sin = self.integrals(middle/self.width)
        # Both integrands have absolute value <=1, paying the symbolic S box.
        integral_cos = add(integral_cos, box(-radius, radius))
        integral_sin = add(integral_sin, box(-radius, radius))
        angle, curvature = self.beta_and_curvature(tl/self.width, th/self.width)
        sine, cosine = sine_cosine(angle)
        return (add(self.R, integral_cos), neg(cosine), neg(mul(curvature, sine)),
                integral_sin, neg(sine), mul(curvature, cosine))

    def metadata(self):
        B = self.amplitude*Q(29, 4096)
        radius_change_bound = self.width*B*B/8
        height_change_bound = self.width*B/4
        reference_kappa_bound = self.kappa*Q(11737, 32768)
        return dict(schema=SCHEMA, definition=self.definition,
            model_identity_sha256=self.model_identity_sha256,
            actual_new_terminal_radius=enclosure(self.R),
            actual_new_reference_height_increment=enclosure(self.height_increment),
            actual_reference_height_change=enclosure(self.height_change),
            old_terminal_radius=self.old.enclosure(self.old.R),
            original_S=self.old.enclosure(self.old.S),
            analytic_radius_change_bound_exact=str(radius_change_bound),
            analytic_height_change_bound_exact=str(height_change_bound),
            analytic_replacement_reference_meridian_curvature_bound_exact=str(reference_kappa_bound),
            original_Hold_extension_plus_new_tail_reference_curvature_bound_exact='5/2',
            reference_curvature_scope='Axisymmetric Hold extension only; no bound on the earlier scalar prefix or on a noncircular q candidate',
            infinite_tail_cutoff_exact=str(self.epsilon),
            whole_infinite_tail_beta_derivative_bounds_exact=[str(value) for value in self.tail_bounds],
            integral_enclosure_width_exact=str(self.integral_uncertainty),
            requested_integral_width_exact=str(self.integration_tolerance),
            requested_integral_accuracy_reached=self.requested_integral_accuracy_reached,
            integral_leaves=len(self.leaves), integral_leaves_evaluated=self.leaves_evaluated,
            all_tail_domain_included=True, unresolved_oscillations_dropped=False,
            admission_seconds=self.admission_seconds,
            elapsed_seconds=time.monotonic()-self.integration_started,
            arithmetic='Integer/Fraction outward 10^-72 intervals; enclosed pi reduction; scaled alternating exp; complete Bell tail; Simpson/interval-range intersection',
            original_metric_unchanged=False, scalar_prefix_unchanged=True,
            original_cap_radius_unchanged=False, original_symbolic_S_unchanged=True,
            old_certificates_inherited=False, new_nonradial_solution_exists=False,
            nonlinear_surface_solved=False, new_fixed_metric_refinement_performed=False,
            complete_geometric_certificate=False, topic_complete=False,
            next_interface='reference_at_affine(alpha,beta) supplies all six scalar jets to an explicitly NEW R671-style factory; old R671/R674 canonical readers must reject this different model')


def load(path, expected, label):
    path = Path(path).resolve()
    if sha(path) != expected:
        raise ValueError('Changed original scalar dependency: '+label)
    spec = importlib.util.spec_from_file_location('_deep_valley_'+label, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main(args):
    require_actions()
    for key, expected in (('integer_source', INTEGER_SHA), ('hold_source', HOLD_SHA)):
        if sha(getattr(args, key)) != expected:
            raise ValueError('Changed complete original '+key)
    raw = args.scalar_input.read_bytes()
    data = json.loads(gzip.decompress(raw) if args.scalar_input.suffix == '.gz' else raw)
    full_module = load(args.scalar_source, FULLHOLD_SHA, 'fullhold')
    full = full_module.FullHold(data, args.integer_source, args.hold_source, panels=args.panels)
    inputs = {role: dict(path=str(getattr(args, role).resolve()), sha256=sha(getattr(args, role)))
              for role in ('scalar_input', 'scalar_source', 'integer_source', 'hold_source')}
    canonical_inputs = {role: value['sha256'] for role, value in inputs.items()}
    tail = DeepValleyTail(full, input_identity=canonical_inputs, epsilon=Q(args.tail_cutoff),
        integral_tolerance=Q(args.integral_tolerance), admission_seconds=args.admission_seconds)
    report = tail.metadata()
    report.update(inputs=inputs, source=dict(path=str(Path(__file__).resolve()), sha256=sha(__file__)),
        execution=dict(repository=os.environ['GITHUB_REPOSITORY'],
            run_id=os.environ.get('GITHUB_RUN_ID'), run_attempt=os.environ.get('GITHUB_RUN_ATTEMPT'),
            commit=os.environ.get('GITHUB_SHA')))
    if args.out.exists():
        raise FileExistsError('Use a new scalar input report path')
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(schema=SCHEMA, model_identity_sha256=tail.model_identity_sha256,
        actual_new_terminal_radius=report['actual_new_terminal_radius'],
        integral_enclosure_width_exact=report['integral_enclosure_width_exact'],
        requested_integral_accuracy_reached=report['requested_integral_accuracy_reached'],
        integral_leaves=report['integral_leaves'], all_tail_domain_included=True,
        nonlinear_surface_solved=False, report_sha256=sha(args.out)), sort_keys=True))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--scalar-input', type=Path, required=True)
    parser.add_argument('--scalar-source', type=Path, required=True)
    parser.add_argument('--integer-source', type=Path, required=True)
    parser.add_argument('--hold-source', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--panels', type=int, default=128)
    parser.add_argument('--tail-cutoff', default='1/8')
    parser.add_argument('--integral-tolerance', default='1e-18')
    parser.add_argument('--admission-seconds', type=float, default=300)
    main(parser.parse_args())
