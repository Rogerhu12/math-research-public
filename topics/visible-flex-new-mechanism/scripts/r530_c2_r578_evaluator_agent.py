#!/usr/bin/env python3
"""R581 exact C2 local ruling on the fixed R578 positive library.

Rebuilt from the reviewed formulas after the executor became unavailable.
This file has its own new SHA-256; it is not the old unpublished draft bytes.
Scientific execution is restricted to the declared public Actions repository.
Only A=0 local ruling is evaluated here. Full A/T endpoint dynamics are separate.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from functools import lru_cache
import gc
import json
import os
import time

import mpmath as mp
import numpy as np

import r530_compact_history_v2_agent as core


@dataclass(frozen=True)
class TimeCoefficient:
    """Scalar value and its first true time derivative."""
    value: float
    derivative: float = 0.0
    __array_priority__ = 10000

    @staticmethod
    def coerce(other):
        if isinstance(other, TimeCoefficient):
            return other
        return TimeCoefficient(float(other))

    def __add__(self, other):
        if isinstance(other, Polynomial):
            return NotImplemented
        other = self.coerce(other)
        return TimeCoefficient(self.value + other.value,
                               self.derivative + other.derivative)

    __radd__ = __add__

    def __neg__(self):
        return TimeCoefficient(-self.value, -self.derivative)

    def __sub__(self, other):
        if isinstance(other, Polynomial):
            return NotImplemented
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        if isinstance(other, Polynomial):
            return NotImplemented
        return self.coerce(other) - self

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            return NotImplemented
        other = self.coerce(other)
        return TimeCoefficient(self.value*other.value,
                               self.derivative*other.value
                               + self.value*other.derivative)

    __rmul__ = __mul__

    def reciprocal(self):
        return TimeCoefficient(1/self.value,
                               -self.derivative/self.value**2)

    def __truediv__(self, other):
        if isinstance(other, Polynomial):
            return NotImplemented
        return self*self.coerce(other).reciprocal()

    def __rtruediv__(self, other):
        if isinstance(other, Polynomial):
            return NotImplemented
        return self.coerce(other)*self.reciprocal()

    def __pow__(self, n):
        if not isinstance(n, int):
            raise TypeError("Only integer coefficient powers are used")
        if n == 0:
            return TimeCoefficient(1.0)
        return TimeCoefficient(self.value**n,
                               n*self.value**(n-1)*self.derivative)


IX, IU, IP, IR, IT, IJ0, IJ1, IJ2, IC, ID = range(10)
NV = 10
ZERO = (0,)*NV


class Polynomial:
    """Sparse polynomial in (y,u,p,r,t,J0,J1,J2,c,d)."""
    __array_priority__ = 10000

    def __init__(self, terms=None):
        self.terms = {}
        for key, value in (terms or {}).items():
            value = TimeCoefficient.coerce(value)
            if value.value != 0.0 or value.derivative != 0.0:
                self.terms[tuple(key)] = value

    @classmethod
    def constant(cls, value):
        return cls({ZERO: value})

    @classmethod
    def variable(cls, index):
        key = [0]*NV
        key[index] = 1
        return cls({tuple(key): 1.0})

    @staticmethod
    def coerce(other):
        return other if isinstance(other, Polynomial) else Polynomial.constant(other)

    def __add__(self, other):
        other = self.coerce(other)
        out = dict(self.terms)
        for key, value in other.terms.items():
            out[key] = out.get(key, TimeCoefficient(0.0)) + value
        return Polynomial(out)

    __radd__ = __add__

    def __neg__(self):
        return Polynomial({key: -value for key, value in self.terms.items()})

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        out = {}
        for left, a in self.terms.items():
            for right, b in other.terms.items():
                key = tuple(x+y for x, y in zip(left, right))
                out[key] = out.get(key, TimeCoefficient(0.0)) + a*b
        return Polynomial(out)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.coerce(other)
        if set(other.terms) != {ZERO}:
            raise TypeError("Only constant polynomial division is permitted")
        return self*other.terms[ZERO].reciprocal()

    def __rtruediv__(self, other):
        return self.coerce(other)/self

    def __pow__(self, n):
        if not isinstance(n, int) or n < 0:
            raise TypeError("Polynomial power must be a nonnegative integer")
        out = Polynomial.constant(1.0)
        factor = self
        while n:
            if n & 1:
                out = out*factor
            factor = factor*factor
            n //= 2
        return out

    def value_part(self):
        return Polynomial({key: TimeCoefficient(value.value)
                           for key, value in self.terms.items()})

    def time_derivative(self):
        return Polynomial({key: TimeCoefficient(value.derivative)
                           for key, value in self.terms.items()})

    def partial(self, index):
        out = {}
        for key, value in self.terms.items():
            n = key[index]
            if n:
                changed = list(key)
                changed[index] -= 1
                out[tuple(changed)] = value*n
        return Polynomial(out)

    def primitive(self, index):
        out = {}
        for key, value in self.terms.items():
            changed = list(key)
            changed[index] += 1
            out[tuple(changed)] = value/changed[index]
        return Polynomial(out)

    def coefficient(self, index, degree):
        out = {}
        for key, value in self.terms.items():
            if key[index] == degree:
                changed = list(key)
                changed[index] = 0
                out[tuple(changed)] = value
        return Polynomial(out)

    def coefficient_norm(self):
        return max((abs(value.value) for value in self.terms.values()), default=0.0)

    def evaluate(self, values):
        shape = np.asarray(values[IX]).shape
        maxima = [max((key[i] for key in self.terms), default=0) for i in range(NV)]
        powers = []
        for value, n in zip(values, maxima):
            row = [1.0]
            for _ in range(n):
                row.append(row[-1]*value)
            powers.append(row)
        out = np.zeros(shape)
        term = np.empty(shape)
        for key, coefficient in self.terms.items():
            if coefficient.value == 0.0:
                continue
            term.fill(coefficient.value)
            for i, power in enumerate(key):
                if power:
                    np.multiply(term, powers[i][power], out=term)
            out += term
        return out


X, U, P, R, T, J0, J1, J2, C, D = [Polynomial.variable(i) for i in range(NV)]


def d0(poly):
    """Original spatial total derivative with r'=t separated; all J' remain."""
    return (poly.partial(IX) + P*poly.partial(IU) + R*poly.partial(IP)
            - D*R**2*poly.partial(IJ0) - X*D*R**2*poly.partial(IJ1)
            - D*(X**2*R**2 + 2*P**2)*poly.partial(IJ2))


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), Polynomial())


def omega(k, v):
    return (-k*v[1], k*v[0] + v[2], -v[1])


def covariant(k, v):
    om = omega(k, v)
    return tuple(p.time_derivative() + q for p, q in zip(v, om))


def profile_operator_zero_jet(m):
    p0, p1, p2, t1, r1, s1, s0, r0 = m
    t0 = p0/4 + s1/2
    a0 = -p1/2 - p2*X
    a1 = p0 + p1*X + p2*X**2
    a2 = r1 + (s1-p0/2)*X + (t1-p1/2)*X**2 - p2*X**3/2
    b0 = r0 + r1*X - p0*X**2/4
    b1 = s0 + s1*X - p1*X**2/4
    b2 = t0 + t1*X - p2*X**2/4
    return (a0*D*U**2 + a1*D*U*P + a2*D*P**2
            + b0*J0 + b1*J1 + b2*J2)


def local_ruling_polynomial(h0, k0, eta0, gamma0, upsilon0, a=0.0, b=0.0):
    """Compile the complete unaveraged local R and its exact C2 integral."""
    h = TimeCoefficient(h0, gamma0)
    k = TimeCoefficient(k0, upsilon0)
    eta = TimeCoefficient(eta0, upsilon0/(2*h0))
    gamma = TimeCoefficient(gamma0, a)
    upsilon = TimeCoefficient(upsilon0, b)
    z = X + eta
    e = h*z - k
    q = 1 + e**2
    es = gamma*z - upsilon/2
    dg = h*eta - k
    pp, pr, rr = D*P**2, D*P*R, D*R**2
    tail_h = (1+k*k-h*h*eta*eta)*J0 - 2*h*h*eta*J1 - h*h*J2
    ah = (2*q*pr-z*q*rr-2*h*e*pp+tail_h)/(16*h*h)
    ak = (q*rr+2*h*(h*J1+dg*J0))/(32*h*h)
    local_eta = gamma*ah + upsilon*ak
    local_eta_x = D*q*(gamma*P-es*R)*T/(8*h*h)
    ptail = ((1+dg*dg)*J0+2*h*dg*J1+h*h*J2)/(8*h) + e*pp/8
    bfield = D*(P**2/4+(h*U-e*P/2)**2)/(2*h)
    px = -D*(R**2/4+(h*P/2-e*R/2)**2)/(2*h)
    bx = D*(P*R/4+(h*U-e*P/2)*(h*P/2-e*R/2))/h
    ky0 = (local_eta/h, z*ptail+bfield, e*local_eta/h)
    ky1 = (local_eta_x/h, ptail+z*px+bx, local_eta+e*local_eta_x/h)
    gy0 = (-C*P/2, Polynomial(), C*(h*U-e*P/2))
    gy1 = (-C*R/2, Polynomial(), C*(h*P/2-e*R/2))
    gc0, gc1 = covariant(k, gy0), covariant(k, gy1)
    kc0, kc1 = covariant(k, ky0), covariant(k, ky1)
    tt = dot(gy1, ky1)
    uu = dot(gy1, ky0) + dot(gy0, ky1)
    vv = dot(gc0, ky1) + dot(kc0, gy1)
    ww = dot(gc1, ky1) + dot(gy1, kc1)
    ff = C*(q*R-2*h*e*P+2*h*h*U)
    ff_x = C*q*T
    m = core.matrix_density(h0, k0, eta0, gamma0, upsilon0)
    vm = profile_operator_zero_jet(m)
    vm_x = d0(vm)  # vm has no explicit r; this is its full spatial derivative.
    raw = (-dot(ky1, ky1)/h-ff_x*vv/(2*h**3)-es*ff_x*tt/(2*h**4)
           +gamma*ff_x*uu/(2*h**4)-ff*ww/(2*h**3)+gamma*ff*tt/(2*h**4)
           -ff*C*T*(q*vm_x-2*h*e*vm)/(8*h**3)).value_part()
    highest = max((key[IT] for key in raw.terms), default=0)
    if highest > 2:
        raise RuntimeError("Unexpected higher micro derivative degree")
    actual_high = raw.coefficient(IT, 2)
    expected_high = (-(D**2+2*C**2*D)*q**3
                     *(gamma*P-es*R)**2/(64*h**7)).value_part()
    high_error = ((actual_high-expected_high).coefficient_norm()
                  /max(1.0, expected_high.coefficient_norm()))
    if high_error > 2.e-10:
        raise RuntimeError(f"Formal highest coefficient identity failed: {high_error}")
    linear = raw.coefficient(IT, 1)
    # Integration in r MUST precede D0; these two operations do not commute.
    primitive = linear.primitive(IR)
    low = (raw.coefficient(IT, 0)-d0(primitive)).value_part()
    if any(key[IT] for key in low.terms):
        raise RuntimeError("The C2 integrand retained a third micro derivative")
    return raw, low, {"raw_terms": len(raw.terms), "c2_terms": len(low.terms),
                      "formal_highest_relative_error": high_error}


@lru_cache(None)
def r578_graph():
    """The exact algebraic input from R578, evaluated at 90 decimal digits."""
    with mp.workdps(90):
        p5 = lambda x: (63*x**5-70*x**3+15*x)/8
        p6 = lambda x: (231*x**6-315*x**4+105*x*x-5)/16
        outer = mp.sqrt((35+2*mp.sqrt(70))/63)
        inner = mp.sqrt((35-2*mp.sqrt(70))/63)
        intervals = [-mp.mpf(1), -outer, -inner, mp.mpf(0), inner, outer, mp.mpf(1)]
        positions, weights = [], []
        worst_moment = mp.mpf(0)
        for rotation in range(6):
            tau = mp.mpf(2*rotation-5)/6
            qq = lambda x: p6(x)+tau*p5(x)
            roots = []
            for j in range(6):
                left, right = intervals[j], intervals[j+1]
                fl = qq(left)
                for _ in range(310):
                    midpoint = (left+right)/2
                    fm = qq(midpoint)
                    if fm == 0:
                        left = right = midpoint
                        break
                    if fl*fm > 0:
                        left = midpoint
                        fl = fm
                    else:
                        right = midpoint
                roots.append((left+right)/2)
            wr = []
            for j, xj in enumerate(roots):
                coeff = [mp.mpf(1)]
                for i, xi in enumerate(roots):
                    if i == j:
                        continue
                    out = [mp.mpf(0)]*(len(coeff)+1)
                    for power, value in enumerate(coeff):
                        out[power] -= xi*value/(xj-xi)
                        out[power+1] += value/(xj-xi)
                    coeff = out
                wr.append(sum(coeff[d]/(d+1) for d in range(0, len(coeff), 2)))
            for degree in range(11):
                target = mp.mpf(0) if degree % 2 else mp.mpf(1)/(degree+1)
                worst_moment = max(worst_moment, abs(
                    sum(w*x**degree for w, x in zip(wr, roots))-target))
            if min(wr) <= 0:
                raise RuntimeError("Nonpositive evaluated R578 weight")
            positions.append(roots)
            weights.append(wr)
        flattened = sorted(x for row in positions for x in row)
        separation = min(b-a for a, b in zip(flattened, flattened[1:]))
        if separation <= mp.mpf(199)/605000 or worst_moment > mp.mpf("1e-75"):
            raise RuntimeError("R578 evaluated graph failed its declared input bounds")
        info = {"blocks": 36, "micro_packets": 1152, "algebraic_precision_digits": 90,
                "evaluated_minimum_node_gap": mp.nstr(separation, 25),
                "proven_node_gap_lower_bound": "199/605000",
                "evaluated_moment_error": mp.nstr(worst_moment, 8),
                "micro_half_width": 2.e-6, "whole_block_envelope_radius": .000125,
                "each_open_collar_width": .000009}
        return (tuple(tuple(float(x) for x in row) for row in positions),
                tuple(tuple(float(w) for w in row) for row in weights), info)


class R578Grid(core.ProfileGrid):
    def __post_init__(self):
        positions, weights, self.graph_info = r578_graph()
        width = 2.e-6
        self.width, self.blocks = width, 36
        self.copy_positions, self.copy_weights = positions, weights
        self.block_weights = np.array([w for row in weights for w in row])
        offsets = np.array([self.center+x for row in positions for x in row])
        packet_centers = np.array([15*j+3*m-57 for j in range(8)
                                   for m in range(4)])*width
        self.segments = []
        nodes, quadrature, ids, mother_x = [], [], [], []
        fcoef, gcoef, rho4 = [], [], []
        cursor = 0
        for packet, pc in enumerate(packet_centers):
            if packet:
                left, right = packet_centers[packet-1]+width, pc-width
                n = self.gap_order
                xn, wn, jm = core.gauss_right_matrix(n)
                local = (left+right)/2+(right-left)/2*xn
                self.segments.append((slice(cursor, cursor+n), (right-left)/2, jm))
                nodes.extend(local)
                quadrature.extend((right-left)/2*wn)
                ids.extend([-1]*n)
                mother_x.extend([0.0]*n)
                fcoef.extend([0.0]*n)
                gcoef.extend([0.0]*n)
                rho4.extend([0.0]*n)
                cursor += n
            xn, wn, jm = core.gauss_right_matrix(self.order)
            self.segments.append((slice(cursor, cursor+self.order), width, jm))
            nodes.extend(pc+width*xn)
            quadrature.extend(width*wn)
            ids.extend([packet]*self.order)
            mother_x.extend(xn)
            macro, micro = divmod(packet, 4)
            amp = (-1)**macro*core.comb(7, macro)**(1/3)
            af = amp*(1 if micro == 0 else np.sqrt(3) if micro == 2 else 0)
            ag = amp*(np.sqrt(3) if micro == 1 else 1 if micro == 3 else 0)
            fcoef.extend([af]*self.order)
            gcoef.extend([ag]*self.order)
            rho4.extend([(af*af+ag*ag)**2]*self.order)
            cursor += self.order
        self.y = offsets[:, None]+np.asarray(nodes)[None, :]
        self.quad = np.asarray(quadrature)
        self.rho4 = np.broadcast_to(np.asarray(rho4), self.y.shape)
        active = np.asarray(ids) >= 0
        mother_x = np.asarray(mother_x)
        raw = np.zeros((5, cursor))
        with np.errstate(over="ignore", under="ignore", invalid="raise"):
            for j, fun in enumerate(core.bump_derivative_functions()):
                raw[j, active] = fun(mother_x[active])/width**j
        self.amplitude = width**1.75/256
        raw *= self.amplitude
        self.raw = np.broadcast_to(raw[:, None, :], (5, self.blocks, cursor)).copy()
        fcoef, gcoef = np.asarray(fcoef), np.asarray(gcoef)
        fcs, gcs = [], []
        trig = ((1.0, 0.0), (-.5, np.sqrt(3)/2), (-.5, -np.sqrt(3)/2))
        for rotation in range(6):
            cc, ss = trig[rotation % 3]
            reflection = 1 if rotation < 3 else -1
            fc = cc*fcoef-ss*reflection*gcoef
            gc_ = ss*fcoef+cc*reflection*gcoef
            for _ in range(6):
                fcs.append(fc)
                gcs.append(gc_)
        self.fcoef, self.gcoef = np.asarray(fcs), np.asarray(gcs)
        self.f = self.raw*self.fcoef[None, :, :]
        self.g = self.raw*self.gcoef[None, :, :]
        # Physical copies have amplitude w^(1/4). These arrays deliberately omit
        # that factor. Every evaluated local ruling is homogeneous of degree 4,
        # including true whole-block quadratic tails, so integral() extracts
        # exactly the fourth power w via block_weights. This is not a general
        # weighted integral for lower-degree fields or already accumulated t/nu.
        self.q_basis = self._make_q_basis()
        self.third_test = np.stack((self.g[4], self.y*self.g[4]+2*self.g[3],
                                   self.y**2*self.g[4]+4*self.y*self.g[3]))
        self.y_limits = (self.center-1, self.center+1)

    def formal_values(self):
        rr = self.f[2]**2-self.g[2]**2
        pp = self.f[1]**2-self.g[1]**2
        j0 = self.right(rr)
        j1 = self.right(self.y*rr)
        j2 = self.right(self.y**2*rr+2*pp)
        return (self.y, self.raw[0], self.raw[1], self.raw[2], self.raw[3],
                j0, j1, j2, self.gcoef, self.fcoef**2-self.gcoef**2)


def summarize_order(grid, compiled, state):
    raw, low, diagnostics = compiled[0]
    values = grid.formal_values()
    low_values = low.evaluate(values)
    stable = float(grid.integral(low_values))
    stable_l1 = float(grid.integral(np.abs(low_values)))
    coeff = []
    for auxiliary in compiled[1:]:
        difference = auxiliary[1]-low
        coeff.append(float(grid.integral(difference.evaluate(values))))
    positive = grid.acceleration_coefficients(*state[:3])
    # One-time new representation/conditioning diagnostic, not a repeated gate.
    direct, _ = core.evaluate_local(grid, *state, 0.0, 0.0, np.zeros(8),
                                   want_third=False)
    raw_values = raw.evaluate(values)
    transposed = float(grid.integral(raw_values))
    high_l1 = float(grid.integral(np.abs(raw_values)))
    return {
        "quadrature_order": grid.order, "gap_order": grid.gap_order,
        "center": grid.center, "geometry": list(state), "graph": grid.graph_info,
        "common_amplitude": grid.amplitude, "formal_polynomial": diagnostics,
        "stable_C2_local_ruling": stable, "stable_integrand_L1": stable_l1,
        "C2_acceleration_coefficients": coeff,
        "positive_integral_acceleration_coefficients": list(positive),
        "relative_acceleration_coefficient_error": float(
            np.linalg.norm(np.asarray(coeff)-positive)/np.linalg.norm(positive)),
        "direct_R56_local_ruling": float(direct),
        "unreduced_transposed_local_ruling": transposed,
        "unreduced_integrand_L1": high_l1,
        "raw_representation_absolute_difference": float(abs(direct-transposed)),
        "scope": "Exact local C2 rewrite on one new fixed R578 model; no endpoint ODE, root, or rank.",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--orders", default="48,96,192")
    parser.add_argument("--gap-order", type=int, default=8)
    parser.add_argument("--center", type=float, default=5.0)
    args = parser.parse_args()
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("This scientific entry is declared for the public Actions repository only.")
    started = time.time()
    state = (1.17, .23, .08, .11, -.31)
    compiled = [local_ruling_polynomial(*state, a, b)
                for a, b in ((0.0, 0.0), (1.0, 0.0), (0.0, 1.0))]
    print("R530_C2_FORMAL "+json.dumps({
        "elapsed_seconds": time.time()-started, "geometry": state,
        "cases": [v[2] for v in compiled]}, sort_keys=True), flush=True)
    for order in (int(n) for n in args.orders.split(",")):
        grid = R578Grid(order, args.gap_order, args.center)
        result = summarize_order(grid, compiled, state)
        result["elapsed_seconds_from_start"] = time.time()-started
        print("R530_C2_REDUCTION "+json.dumps(
            result, sort_keys=True, allow_nan=False), flush=True)
        del grid
        gc.collect()


if __name__ == "__main__":
    main()
