#!/usr/bin/env python3
"""Native Arb enclosures of the exact infinite phase graph and root collar.

Reconstructed after the executor reset. All reports must be rerun with this
source hash; it is not a byte-for-byte restoration of the earlier program.
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
from flint import arb, acb, acb_series, ctx


def ball_record(value, digits=35):
    value = arb(value)
    return {"ball": value.str(digits), "lower": value.lower().str(digits),
            "upper": value.upper().str(digits), "mid_float": float(value.mid()),
            "radius_upper_float": float(value.rad().upper())}


def series_constant(value, precision=None):
    return acb_series([acb(value)], prec=ctx.cap if precision is None else precision)


def series_array(shape):
    out = np.empty(shape, dtype=object)
    for index in np.ndindex(shape):
        out[index] = series_constant(0)
    return out


def series_real(value):
    return acb_series([acb(value[k].real) for k in range(value.prec)], prec=value.prec)


def add_real_cauchy_error(value, error, scale, radius):
    return acb_series([acb(value[k].real+arb(0, (error*(scale/radius)**k).upper()))
                       for k in range(value.prec)], prec=value.prec)


def polynomial_disk_bound(value, radius):
    return sum((abs(value[n])*radius**n for n in range(value.prec)), arb(0)).upper()


def analytic_tail_derivative(bound, outer_radius, inner_radius, precision, order):
    """Taylor tail n>=precision, differentiated order times in the radius."""
    if not 0 < inner_radius < outer_radius or precision <= order:
        raise ValueError("invalid analytic Taylor remainder parameters")
    q = inner_radius/outer_radius
    total = arb(0)
    for v in range(order+1):
        falling = math.factorial(precision)//math.factorial(precision-order+v)
        total += math.comb(order, v)*falling*math.factorial(v)*q**v/(1-q)**(v+1)
    return (bound*outer_radius**(-order)*q**(precision-order)*total).upper()


def pad_complex(value, radius):
    return acb(value)+acb(arb(0, arb(radius).upper()), arb(0, arb(radius).upper()))


def primitive_fourier_budget(nodes, sigma, inner_sigma, radial_radius,
                             radius_bound, height_bound, tangent_bound):
    if not sigma > inner_sigma >= 0:
        raise ValueError("Fourier strips are not strictly nested")
    half, q = nodes//2, (-(sigma-inner_sigma)).exp()
    denominator = 1-(-sigma*nodes).exp()
    errors, finite = [], []
    for derivative in range(3):
        alias_sum, finite_sum = arb(0), arb(0)
        for k in range(half):
            factor = arb(1) if k == 0 else arb(1)/(4*k-1)
            weight = (4*k+1)**derivative*(inner_sigma*k).exp()
            alias = 2*(-sigma*nodes).exp()*(sigma*k).cosh()/denominator
            multiplicity = 1 if k == 0 else 2
            alias_sum += multiplicity*factor*weight*alias
            finite_sum += multiplicity*factor*weight*((-sigma*k).exp()+alias)
        moments = [1/(1-q), half/(1-q)+q/(1-q)**2,
                   half*half/(1-q)+2*half*q/(1-q)**2+q*(1+q)/(1-q)**3]
        tail = 2*q**half/(4*half-1)*sum(
            (math.comb(derivative, p)*4**p*moments[p] for p in range(derivative+1)), arb(0))
        errors.append((radius_bound*tangent_bound*(alias_sum+tail)).upper())
        finite.append((radius_bound*tangent_bound*finite_sum
                       +(height_bound if derivative == 0 else 0)).upper())
    return errors, finite


def series_derivative(value, scale=1, count=1):
    for _ in range(count):
        value = value.derivative()/scale
    return value


def array_derivative(values, scale=1, count=1):
    out = np.empty(values.shape, dtype=object)
    for key in np.ndindex(values.shape):
        out[key] = series_derivative(values[key], scale, count)
    return out


def vector_dot(left, right):
    return sum((left[j]*right[j] for j in range(3)), 0)


def vector_cross(left, right):
    return [left[1]*right[2]-left[2]*right[1], left[2]*right[0]-left[0]*right[2],
            left[0]*right[1]-left[1]*right[0]]


class NativeSpline:
    def __init__(self, knots, coefficients, degree, converted=False):
        self.knots_float = np.asarray([float(x) for x in knots])
        self.knots = [arb(x) if converted else arb(float(x)) for x in knots]
        self.degree = int(degree)
        raw = np.asarray(coefficients, dtype=object)
        self.coefficients = np.empty(raw.shape, object)
        for key in np.ndindex(raw.shape):
            self.coefficients[key] = arb(raw[key]) if converted else arb(float(raw[key]))
        self.cache = {}

    def germ(self, center, direction, selector=None):
        center = acb(center)
        selector = float(center.real.mid()) if selector is None else float(selector)
        span = bisect_right(self.knots_float.tolist(), selector)-1
        if not self.degree <= span < len(self.knots)-self.degree-1:
            raise ValueError("spline germ outside its nonextrapolated domain")
        key = (selector, span, ctx.prec)
        if key not in self.cache:
            old_cap, ctx.cap = ctx.cap, max(ctx.cap, self.degree+1)
            anchor, shape = arb(selector), self.coefficients.shape[1:]
            x = acb_series([acb(anchor), 1])
            polynomials = np.empty(shape, object)
            for index in np.ndindex(shape):
                work = [series_constant(self.coefficients[(span-self.degree+j,)+index])
                        for j in range(self.degree+1)]
                for level in range(1, self.degree+1):
                    for j in range(self.degree, level-1, -1):
                        kk = span-self.degree+j
                        weight = (x-self.knots[kk])/(self.knots[kk+self.degree-level+1]-self.knots[kk])
                        work[j] = (1-weight)*work[j-1]+weight*work[j]
                polynomials[index] = [work[self.degree][n] for n in range(self.degree+1)]
            ctx.cap = old_cap
            self.cache[key] = (anchor, polynomials)
        anchor, polynomials = self.cache[key]
        delta = acb_series([center-anchor, acb(direction)])
        out = np.empty(polynomials.shape, object)
        for index in np.ndindex(polynomials.shape):
            coefficients = polynomials[index]
            value = series_constant(coefficients[-1])
            for coefficient in coefficients[-2::-1]:
                value = coefficient+delta*value
            out[index] = value
        return out.item() if not out.shape else out

    def antiderivative(self):
        n = len(self.knots)-self.degree-1
        shape = (n+1,)+self.coefficients.shape[1:]
        coefficients = np.empty(shape, object)
        for index in np.ndindex(shape[1:]):
            running = arb(0)
            coefficients[(0,)+index] = running
            for j in range(n):
                running += self.coefficients[(j,)+index]*(self.knots[j+self.degree+1]-self.knots[j])/(self.degree+1)
                coefficients[(j+1,)+index] = running
        return NativeSpline([self.knots[0]]+self.knots+[self.knots[-1]], coefficients,
                            self.degree+1, converted=True)


class NativeFFT:
    def __init__(self):
        self.cache = {}

    def fft(self, values, inverse=False):
        n = values.shape[0]
        if n & (n-1):
            raise ValueError("FFT requires a power of two")
        key = (n, inverse, ctx.prec)
        if key not in self.cache:
            bits = n.bit_length()-1
            permutation = [int(format(k, f"0{bits}b")[::-1], 2) for k in range(n)]
            factors = {}
            for width in [1 << k for k in range(1, bits+1)]:
                factors[width] = [(acb(0, (2 if inverse else -2)*arb.pi()*k/width)).exp()
                                  for k in range(width//2)]
            self.cache[key] = permutation, factors
        permutation, factors = self.cache[key]
        result = values[permutation].copy()
        for width, roots in factors.items():
            half = width//2
            for start in range(0, n, width):
                for k, root in enumerate(roots):
                    left = result[start+k].copy()
                    right = result[start+k+half]*root
                    result[start+k], result[start+k+half] = left+right, left-right
        return result/n if inverse else result


class BallTarget:
    def __init__(self, snapshot, nodes, angles):
        with np.load(snapshot, allow_pickle=False) as saved:
            self.frozen = {key: saved[key].copy() for key in saved.files}
        f = self.frozen
        self.nodes, self.angles = int(nodes), int(angles)
        self.modes = f["phase_coefficients"].shape[1]
        if nodes < 4*self.modes+8 or angles < nodes:
            raise ValueError("insufficient primitive/evaluation grid")
        self.alpha = [arb(float(x)) for x in f["alpha"]]
        self.raw = NativeSpline(f["phase_knots"], f["phase_coefficients"], 5)
        self.base = NativeSpline(f["base_knots"], f["base_radius_coefficients"], int(f["base_degree"]))
        self.shift = NativeSpline(f["shift_knots"], f["shift_coefficients"], int(f["shift_degree"]))
        self.means = [NativeSpline(f[f"mean{j}_knots"], f[f"mean{j}_radius_coefficients"],
                                  int(f[f"mean{j}_degree"])) for j in range(len(self.alpha))]
        self.height_integrals = [NativeSpline(f[f"height{j}_slope_knots"], f[f"height{j}_slope_coefficients"],
                                             int(f[f"height{j}_slope_degree"])).antiderivative()
                                 for j in range(len(self.alpha)+1)]
        self.sines = np.empty((self.modes, nodes), object)
        for j in range(self.modes):
            for k in range(nodes):
                self.sines[j, k] = (2*arb.pi()*(j+1)*k/nodes).sin()
        self.frequency = [4*(k if k < nodes//2 else k-nodes) for k in range(nodes)]
        self.fourier = NativeFFT()

    def scalars(self, center, direction):
        bp, bm = self.base.germ(center, direction), self.base.germ(-center, -direction)
        pp, pm = self.raw.germ(center, direction), self.raw.germ(-center, -direction)
        beta, gamma = np.empty(self.modes, object), np.empty(self.modes, object)
        for j in range(self.modes):
            beta[j] = (pp[j, 0]*bp**3+pm[j, 0]*bm**3)/2
            gamma[j] = (pp[j, 1]*bp**2-pm[j, 1]*bm**2)/2
        radius = (bp+bm+self.shift.germ(center, direction)+self.shift.germ(-center, -direction))/2
        for alpha, sp in zip(self.alpha, self.means):
            radius += alpha*(sp.germ(center, direction)+sp.germ(-center, -direction))/2
        height = series_constant(0)
        for alpha, sp in zip([arb(1)]+self.alpha, self.height_integrals):
            height += alpha*(sp.germ(center, direction)-sp.germ(-center, -direction))/2
        return beta, gamma, radius, height

    def analytic_input_budget(self, root, radial_radius, sigma, E_radius):
        if not radial_radius > E_radius > 0:
            raise ValueError("radial Cauchy radii are not nested")
        old_cap, ctx.cap = ctx.cap, max(ctx.cap, 21)
        beta, gamma, radius, height = self.scalars(acb(root), 1)
        ctx.cap = old_cap
        B = sum((polynomial_disk_bound(beta[j], radial_radius)*(sigma*(j+1)).cosh()
                 for j in range(self.modes)), arb(0)).upper()
        G = sum((polynomial_disk_bound(gamma[j], radial_radius)*(sigma*(j+1)).cosh()
                 for j in range(self.modes)), arb(0)).upper()
        A, Z = polynomial_disk_bound(radius, radial_radius), polynomial_disk_bound(height, radial_radius)
        tangent = (B+G).exp().upper()
        errors, finite = primitive_fourier_budget(self.nodes, sigma, arb(0), radial_radius, A, Z, tangent)
        gap = radial_radius-E_radius
        e1, m1 = errors[0]/gap, finite[0]/gap
        E_error = (3*e1*(2*m1+e1)).upper()
        return {"radial_radius": radial_radius, "E_radius": E_radius, "sigma_normalized_x": sigma,
                "beta_bound": B, "gamma_bound": G, "radius_bound": A, "height_bound": Z,
                "tangent_bound": tangent, "field_errors": errors, "finite_field_bounds": finite,
                "E_error": E_error, "E_full_bound": (3*((finite[0]+errors[0])/gap)**2).upper()}

    def primitive(self, center, direction):
        beta, gamma, radius, height = self.scalars(center, direction)
        tangent = series_array((self.nodes, 3))
        for k in range(self.nodes):
            b = sum((beta[j]*self.sines[j, k] for j in range(self.modes)), series_constant(0))
            g = sum((gamma[j]*self.sines[j, k] for j in range(self.modes)), series_constant(0))
            sb, cb, sg, cg = b.sin(), b.cos(), g.sin(), g.cos()
            tangent[k] = [-cg*sb, cg*cb, sg]
        coefficient = self.fourier.fft(tangent)/self.nodes
        primitive = series_array((self.nodes, 3))
        for k, n in enumerate(self.frequency):
            primitive[k, 0] = (acb(0, n)*coefficient[k, 0]+coefficient[k, 1])/(1-n*n)
            primitive[k, 1] = (-coefficient[k, 0]+acb(0, n)*coefficient[k, 1])/(1-n*n)
            if n:
                primitive[k, 2] = coefficient[k, 2]/acb(0, n)
        for j in range(3):
            primitive[self.nodes//2, j] = series_constant(0)
        primitive[0, 1], primitive[0, 2] = series_constant(0), series_constant(0)
        for k in range(1, self.nodes//2):
            for j, parity in enumerate((1, -1, 1)):
                value = (primitive[k, j]+parity*primitive[-k, j])/2
                primitive[k, j], primitive[-k, j] = value, parity*value
        for key in np.ndindex(primitive.shape):
            primitive[key] = primitive[key]*radius
        primitive[0, 2] += height
        return primitive, radius

    def target(self, center, scale, budget=None):
        coefficient, radius = self.primitive(center, -scale)
        first = array_derivative(coefficient, -scale)
        E = sum((vector_dot(first[k], first[(-k) % self.nodes]) for k in range(self.nodes)), series_constant(0))
        E = series_real(E)
        if budget is not None:
            E = add_real_cauchy_error(E, budget["E_error"], scale, budget["E_radius"])
        ar, arr = series_derivative(radius, -scale), series_derivative(radius, -scale, 2)
        Er = series_derivative(E, -scale)
        C = ar*Er-2*arr*E
        K = C/(2*radius*E**2)
        return coefficient, radius, E, C, K

    def refine_certified_root(self, root, scale, budget, steps=3):
        trace = []
        for _ in range(steps):
            midpoint = root.mid()
            Cm = self.target(midpoint, scale, budget)[3][0].real
            CI = self.target(root, scale, budget)[3]
            derivative = (-CI[1]/scale).real
            if not derivative > 0:
                raise ValueError("certified root derivative is not positive")
            image = midpoint-Cm/derivative
            root = root.intersection(image)
            trace.append({"root": ball_record(root), "C_mid": ball_record(Cm),
                          "derivative": ball_record(derivative)})
        return root, trace

    def angular(self, coefficient, count=1):
        value = coefficient.copy()
        for _ in range(count):
            out = series_array(value.shape)
            for k, n in enumerate(self.frequency):
                out[k, 0], out[k, 1] = acb(0, n)*value[k, 0]-value[k, 1], acb(0, n)*value[k, 1]+value[k, 0]
                out[k, 2] = acb(0, n)*value[k, 2]
            value = out
        return value

    def evaluate(self, coefficient):
        padded = series_array((self.angles, 3))
        for k in range(self.nodes):
            signed = k if k < self.nodes//2 else k-self.nodes
            padded[signed % self.angles] = coefficient[k]
        out = self.fourier.fft(padded, inverse=True)*self.angles
        for key in np.ndindex(out.shape):
            out[key] = series_real(out[key])
        return out

    def root_density_taylor(self, root, scale, degree, budget):
        coefficient, radius, E, C, K = self.target(root, scale, budget)
        # The supplied certificate and interval Newton locate the true root.
        # Higher coefficients already enclose its derivatives. Its constant
        # curvature is exactly zero, after the infinite E correction.
        K = acb_series([0]+[K[n] for n in range(1, K.prec)], prec=K.prec)
        k2 = acb_series([-K[n+1]/scale for n in range(K.prec-1)], prec=K.prec-1)
        kappa = k2.sqrt()
        rho = acb_series([0, acb(scale)])
        samples = []
        for b in range(3):
            rows = self.evaluate(self.angular(coefficient, b))
            for key in np.ndindex(rows.shape):
                rows[key] = add_real_cauchy_error(rows[key], budget["field_errors"][b],
                                                  scale, budget["radial_radius"])
            samples.append(rows)
        F, Y, Ftt = samples
        X, Frr, Frt = array_derivative(F, -scale), array_derivative(F, -scale, 2), array_derivative(Y, -scale)
        total = series_constant(0)
        for j in range(self.angles):
            normal = vector_cross(Y[j], X[j])
            nr1, nr2 = vector_cross(Frt[j], X[j]), vector_cross(Y[j], Frr[j])
            nt1, nt2 = vector_cross(Ftt[j], X[j]), vector_cross(Y[j], Frt[j])
            nr, nt = [nr1[k]+nr2[k] for k in range(3)], [nt1[k]+nt2[k] for k in range(3)]
            area2, radius2, support = vector_dot(normal, normal), vector_dot(F[j], F[j]), vector_dot(normal, F[j])
            l, m, n = [vector_dot(normal, w[j]) for w in (Frr, Frt, Ftt)]
            a, b, c = -n/area2, m/area2, -l/area2
            actual_K = (l*n-m*m)/area2**2
            omega, chat = (actual_K-K)/a, (b*b+K)/a
            FX, FY = vector_dot(F[j], X[j]), vector_dot(F[j], Y[j])
            d = (a*(vector_dot(X[j], X[j])-FX*FX/radius2)
                 +2*b*(vector_dot(X[j], Y[j])-FX*FY/radius2)
                 +c*(vector_dot(Y[j], Y[j])-FY*FY/radius2))/radius2
            lzr = vector_dot(nr, F[j])/support-vector_dot(normal, nr)/area2-FX/radius2
            lzt = vector_dot(nt, F[j])/support-vector_dot(normal, nt)/area2-FY/radius2
            Lrho, Ltheta = kappa.derivative()/(scale*kappa)+2*lzr, -2*lzt
            ell = Y[j, 2]/F[j, 2]-FY/radius2
            AA = -a/(16*kappa)
            BB = -(a*Lrho-b*Ltheta)/(4*kappa)
            CC = (d+omega*(ell*ell+ell*Ltheta)
                  -(a*Lrho*Lrho-2*b*Lrho*Ltheta+chat*Ltheta*Ltheta)/4)/kappa
            total += AA+rho*BB+rho*rho*CC
        mean = total/self.angles
        coefficients = [(mean[n]/scale**n).real for n in range(degree+1)]
        return coefficients, {"K_prime_at_root": ball_record(k2[0].real),
                              "g0": ball_record(coefficients[0]), "g1": ball_record(coefficients[1])}

    @staticmethod
    def disk_series(value, scale, radius, order=0):
        """Range on the complex rho disk, for a finite normalized polynomial."""
        constant = math.factorial(order)*value[order]/scale**order
        fee = sum((math.factorial(n)//math.factorial(n-order)*abs(value[n])
                   *radius**(n-order)/scale**n for n in range(order+1, value.prec)), arb(0)).upper()
        return pad_complex(constant, fee)

    def collar_domain_bound(self, root, scale, radial_radius, angular_sigma, budget):
        R, R0, RE = radial_radius, budget["radial_radius"], budget["E_radius"]
        if not 0 < R < RE < R0:
            raise ValueError("collar complex disk not within Cauchy radii")
        coefficient, radius, Efinite, _, _ = self.target(root, scale, None)
        angular_width = angular_sigma+arb.pi()/self.angles
        errors, finite = primitive_fourier_budget(self.nodes, budget["sigma_normalized_x"], angular_width,
                                                   R0, budget["radius_bound"], budget["height_bound"],
                                                   budget["tangent_bound"])
        sources = [coefficient, self.angular(coefficient), self.angular(coefficient, 2)]
        fields = {}
        for ar, at in ((0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (0, 2)):
            source = array_derivative(sources[at], -scale, ar)
            angle_fee = [arb(0), arb(0), arb(0)]
            for k in range(self.nodes):
                mode = abs(k if k < self.nodes//2 else k-self.nodes)
                factor = (mode*angular_width).exp()-1
                for component in range(3):
                    angle_fee[component] += polynomial_disk_bound(source[k, component], R/scale)*factor
            rows = self.evaluate(source)
            tail = analytic_tail_derivative(finite[at], R0, R, coefficient[0, 0].prec, ar)
            infinite = math.factorial(ar)*errors[at]/(R0-R)**ar
            out = np.empty(rows.shape, object)
            for key in np.ndindex(rows.shape):
                out[key] = pad_complex(self.disk_series(rows[key], scale, R),
                                       angle_fee[key[1]]+tail+infinite)
            fields[(ar, at)] = out
        # E is bilinear in complex r. First bound the finite primitive's
        # analytic continuation, then add the full infinite correction.
        finite_E_bound = 3*(budget["finite_field_bounds"][0]/(R0-RE))**2
        Ej = []
        for order in range(4):
            tail = analytic_tail_derivative(finite_E_bound, RE, R, Efinite.prec, order)
            infinite = math.factorial(order)*budget["E_error"]/(RE-R)**order
            value = pad_complex(self.disk_series(Efinite, scale, R, order), tail+infinite)
            Ej.append((-1)**order*value)
        aj = [(-1)**order*self.disk_series(radius, scale, R, order) for order in range(5)]
        aa = acb_series([aj[j]/math.factorial(j) for j in range(5)], prec=5)
        ee = acb_series([Ej[j]/math.factorial(j) for j in range(4)], prec=4)
        kk = (aa.derivative()*ee.derivative()-2*aa.derivative().derivative()*ee)/(2*aa*ee**2)
        k2, k2rho = kk[1], -kk[2]
        if not k2.real > 0:
            raise ValueError("true deflated curvature has no positive real part on the disk")
        kappa = k2.sqrt(analytic=True)
        K = pad_complex(0, R*abs(k2))
        F, X, Frr, Y, Frt, Ftt = [fields[key] for key in
                                ((0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (0, 2))]
        maxima, minima = [], {name: [] for name in ("area2", "radius2", "support", "a", "Fz")}
        for j in range(self.angles):
            normal = vector_cross(Y[j], X[j])
            nr1, nr2 = vector_cross(Frt[j], X[j]), vector_cross(Y[j], Frr[j])
            nt1, nt2 = vector_cross(Ftt[j], X[j]), vector_cross(Y[j], Frt[j])
            nr, nt = [nr1[k]+nr2[k] for k in range(3)], [nt1[k]+nt2[k] for k in range(3)]
            area2, radius2, support = vector_dot(normal, normal), vector_dot(F[j], F[j]), vector_dot(normal, F[j])
            l, m, n = [vector_dot(normal, w[j]) for w in (Frr, Frt, Ftt)]
            if any(not z.real > 0 for z in (area2, radius2, support)):
                raise ValueError("actual geometry denominator gate failed on complete collar disk")
            a, b, c = -n/area2, m/area2, -l/area2
            if not a.real > 0 or not F[j, 2].real > 0:
                raise ValueError("actual a or Fz denominator gate failed on complete collar disk")
            for name, value in zip(minima, (area2, radius2, support, a, F[j, 2])):
                minima[name].append(value.real.lower())
            actual_K = (l*n-m*m)/area2**2
            omega, chat = (actual_K-K)/a, (b*b+K)/a
            FX, FY = vector_dot(F[j], X[j]), vector_dot(F[j], Y[j])
            d = (a*(vector_dot(X[j], X[j])-FX*FX/radius2)
                 +2*b*(vector_dot(X[j], Y[j])-FX*FY/radius2)
                 +c*(vector_dot(Y[j], Y[j])-FY*FY/radius2))/radius2
            lzr = vector_dot(nr, F[j])/support-vector_dot(normal, nr)/area2-FX/radius2
            lzt = vector_dot(nt, F[j])/support-vector_dot(normal, nt)/area2-FY/radius2
            Lrho, Ltheta = k2rho/(2*k2)+2*lzr, -2*lzt
            ell = Y[j, 2]/F[j, 2]-FY/radius2
            AA = -a/(16*kappa)
            BB = -(a*Lrho-b*Ltheta)/(4*kappa)
            CC = (d+omega*(ell*ell+ell*Ltheta)
                  -(a*Lrho*Lrho-2*b*Lrho*Ltheta+chat*Ltheta*Ltheta)/4)/kappa
            maxima.append((abs(AA)+R*abs(BB)+R*R*abs(CC)).upper())
        bound = max(maxima)
        return bound, {"G_bound": ball_record(bound), "deflated_curvature": k2.str(35),
                       "deflated_curvature_rho": k2rho.str(35),
                       "positive_real_minima": {key: ball_record(min(values)) for key, values in minima.items()},
                       "normalized_angular_width": ball_record(angular_width)}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--frozen-inputs", type=Path, required=True)
    ap.add_argument("--root-certificate", type=Path, required=True)
    ap.add_argument("--bits", type=int, default=192)
    ap.add_argument("--quarter-nodes", type=int, default=512)
    ap.add_argument("--angles", type=int, default=2048)
    ap.add_argument("--degree", type=int, default=24)
    ap.add_argument("--precision", type=int, default=72)
    ap.add_argument("--scale", default="1/4096")
    ap.add_argument("--radial-radius", default=".0006")
    ap.add_argument("--angular-sigma", default=".02")
    ap.add_argument("--tail-radius", default=".003")
    ap.add_argument("--E-radius", default=".0025")
    ap.add_argument("--tail-sigma", default=".32")
    ap.add_argument("--fixed-cut", default="1072423152036779/4503599627370496")
    ap.add_argument("--infinite-tail", action="store_true")
    ap.add_argument("--collar-domain", action="store_true")
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    ctx.prec, ctx.cap = args.bits, args.precision
    if args.precision <= args.degree+8 or not args.infinite_tail:
        raise ValueError("true infinite tail and sufficient series precision are mandatory")
    input_hash = hashlib.sha256(args.frozen_inputs.read_bytes()).hexdigest()
    root_hash = hashlib.sha256(args.root_certificate.read_bytes()).hexdigest()
    expected_root = "3d6018b0a17e1ea5ec1b21fd28d886bc7454a91973fbcfd0cfaa3d7ee4ecc66b"
    if input_hash != "bd9b4d14b104183f80feaeea4c4c1a5d8c40b511bd58974dbca1bda842474532" or root_hash != expected_root:
        raise ValueError("this recovered entry point currently admits only the certified original symmetric object")
    started = time.monotonic()
    scale_fraction = Fraction(args.scale)
    scale = arb(scale_fraction.numerator)/scale_fraction.denominator
    cut_fraction = Fraction(args.fixed_cut)
    cut = arb(cut_fraction.numerator)/cut_fraction.denominator
    root = arb(float(".23836991573145")).union(arb(float(".23836991573148")))
    target = BallTarget(args.frozen_inputs, args.quarter_nodes, args.angles)
    right_endpoint = Fraction.from_float(float(".23836991573148"))
    for key, values in target.frozen.items():
        if key.endswith("_knots"):
            for value in values:
                if cut_fraction < abs(Fraction.from_float(float(value))) < right_endpoint:
                    raise ValueError("the physical collar crosses an exact positive or negative scalar knot")
    budget = target.analytic_input_budget(root, arb(args.tail_radius), arb(args.tail_sigma), arb(args.E_radius))
    root, trace = target.refine_certified_root(root, scale, budget, steps=3)
    eta = root-cut
    if not eta > 0:
        raise ValueError("fixed physical cut is not below the actual root")
    coefficients, diagnostics = target.root_density_taylor(root, scale, args.degree, budget)
    polynomial = sum((coefficients[n]*eta**(arb(n)-arb(3)/2)/(arb(n)-arb(3)/2)
                      for n in range(args.degree+1)), arb(0))
    report = {"kind": "reconstructed_native_Arb_root_collar", "complete": False,
              "input_sha256": input_hash, "root_certificate_sha256": root_hash,
              "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "bits": args.bits, "quarter_nodes": args.quarter_nodes, "angles": args.angles,
              "degree": args.degree, "series_precision": args.precision, "root": ball_record(root),
              "fixed_cut": str(cut_fraction), "eta": ball_record(eta), "root_newton_trace": trace,
              "coefficients": [ball_record(c) for c in coefficients], "polynomial_finite_part": ball_record(polynomial),
              "coefficient_diagnostics": diagnostics,
              "input_budget": {key: ([ball_record(v) for v in value] if isinstance(value, list) else ball_record(value))
                               for key, value in budget.items()},
              "limitations": ["A collar enclosure is not a full beta or PDE-network certificate",
                              "Reconstructed source: all numerical outputs are rerun, not transferred by an old hash"]}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    def save():
        report["wall_seconds"] = time.monotonic()-started
        args.out.write_text(json.dumps(report, indent=2)+"\n")
    save()
    print(json.dumps({"stage": "coefficients", "g0": coefficients[0].str(20), "g1": coefficients[1].str(20)}), flush=True)
    if args.collar_domain:
        R, sigma = arb(args.radial_radius), arb(args.angular_sigma)
        if not eta < R:
            raise ValueError("physical collar is not inside the complex disk")
        bound, domain = target.collar_domain_bound(root, scale, R, sigma, budget)
        tail = bound*eta**(arb(args.degree)-arb(1)/2)/((arb(args.degree)-arb(1)/2)*R**(args.degree+1)*(1-eta/R))
        angular_mean = 2*bound*(-sigma*args.angles).exp()/(1-(-sigma*args.angles).exp())
        angular_fee = 2*angular_mean*eta**(-arb(3)/2)/(1-eta/R)
        result = polynomial+arb(0, (tail+angular_fee).upper())
        report.update({"domain": domain, "radial_radius": ball_record(R), "angular_sigma": ball_record(sigma),
                       "radial_tail_error": ball_record(tail.upper()), "angular_error": ball_record(angular_fee.upper()),
                       "collar_integral": ball_record(result), "complete": True})
        print(json.dumps({"stage": "complete collar", "integral": result.str(25)}), flush=True)
        save()


if __name__ == "__main__":
    main()
