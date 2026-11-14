#!/usr/bin/env python3
"""High precision root Taylor finite-part probe for the frozen symmetric graph.

This computes ordinary Taylor coefficients at the actual high precision root
of a specified FINITE primitive. It never extrapolates a polynomial fitted
away from the root. Binary64 spline inputs are converted by exact integer
ratios, and local de Boor polynomial arithmetic is carried out by mpmath.

The result is a high precision diagnostic, NOT an interval certificate:
angular primitive alias/tail, angular quadrature, Taylor remainder, bulk
quadrature and all rounding still need directed bounds for a theorem.
"""
from __future__ import annotations

import argparse
from bisect import bisect_right
import hashlib
import json
import math
from pathlib import Path
import time

import mpmath as mp
import numpy as np


def exact_mpf(value):
    """Convert a saved binary64 exactly, before subsequent mp rounding."""
    if isinstance(value, (mp.mpf, mp.mpc)):
        return value
    if isinstance(value, (int, np.integer)):
        return mp.mpf(int(value))
    numerator, denominator = float(value).as_integer_ratio()
    return mp.mpf(numerator)/denominator


def object_map(function, array):
    array = np.asarray(array, dtype=object)
    return np.array([function(value) for value in array.flat],
                    dtype=object).reshape(array.shape)


class Taylor:
    """Ordinary coefficients, f(z)=sum c[n] z**n; vector shapes broadcast."""
    __array_priority__ = 1000

    def __init__(self, coefficients, active=None):
        self.c = np.asarray(coefficients, dtype=object)
        self.order = len(self.c)-1
        self.shape = self.c.shape[1:]
        self.active = self.order if active is None else min(active, self.order)

    @classmethod
    def constant(cls, value, order):
        value = np.asarray(value, dtype=object)
        coefficient = np.zeros((order+1,)+value.shape, dtype=object)
        coefficient[0] = value
        return cls(coefficient, 0)

    @classmethod
    def variable(cls, center, direction, order):
        value = cls.constant(center, order)
        if order:
            value.c[1] = direction
            value.active = 1
        return value

    def coerce(self, value):
        if isinstance(value, Taylor):
            if value.order != self.order:
                raise ValueError("Taylor orders differ")
            return value
        return Taylor.constant(value, self.order)

    def __add__(self, other):
        other = self.coerce(other)
        shape = np.broadcast_shapes(self.shape, other.shape)
        left = self.c.reshape((self.order+1,)+(1,)*(len(shape)-len(self.shape))+self.shape)
        right = other.c.reshape((self.order+1,)+(1,)*(len(shape)-len(other.shape))+other.shape)
        return Taylor(left+right, max(self.active, other.active))

    __radd__ = __add__

    def __neg__(self):
        return Taylor(-self.c, self.active)

    def __sub__(self, other):
        return self+-self.coerce(other)

    def __rsub__(self, other):
        return self.coerce(other)+-self

    def __mul__(self, other):
        other = self.coerce(other)
        shape = np.broadcast_shapes(self.shape, other.shape)
        out = np.zeros((self.order+1,)+shape, dtype=object)
        active = min(self.order, self.active+other.active)
        for n in range(active+1):
            for k in range(max(0, n-other.active), min(n, self.active)+1):
                out[n] += self.c[k]*other.c[n-k]
        return Taylor(out, active)

    __rmul__ = __mul__

    def reciprocal(self):
        out = np.zeros_like(self.c)
        out[0] = object_map(lambda z: mp.mpf(1)/z, self.c[0])
        for n in range(1, self.order+1):
            value = np.zeros(self.shape, dtype=object)
            for k in range(1, min(n, self.active)+1):
                value += self.c[k]*out[n-k]
            out[n] = -out[0]*value
        return Taylor(out)

    def __truediv__(self, other):
        if not isinstance(other, Taylor):
            return self*object_map(lambda z: mp.mpf(1)/z, np.asarray(other, dtype=object))
        return self*other.reciprocal()

    def __rtruediv__(self, other):
        return self.coerce(other)*self.reciprocal()

    def __pow__(self, power):
        if not isinstance(power, int):
            raise TypeError("use sqrt or exp for noninteger power")
        if power < 0:
            return self.reciprocal()**(-power)
        out = Taylor.constant(1, self.order)
        base = self
        while power:
            if power & 1:
                out = out*base
            base = base*base
            power //= 2
        return out

    def sqrt(self):
        out = np.zeros_like(self.c)
        out[0] = object_map(mp.sqrt, self.c[0])
        for n in range(1, self.order+1):
            value = np.array(self.c[n], dtype=object, copy=True)
            for k in range(1, n):
                value -= out[k]*out[n-k]
            out[n] = value/(2*out[0])
        return Taylor(out)

    def exp(self):
        out = np.zeros_like(self.c)
        out[0] = object_map(mp.exp, self.c[0])
        for n in range(1, self.order+1):
            for k in range(1, min(n, self.active)+1):
                out[n] += k*self.c[k]*out[n-k]
            out[n] /= n
        return Taylor(out)

    def derivative(self, count=1):
        out = np.zeros_like(self.c)
        for n in range(self.order+1-count):
            out[n] = math.factorial(n+count)//math.factorial(n)*self.c[n+count]
        return Taylor(out, max(0, self.active-count))

    def real(self):
        return Taylor(object_map(mp.re, self.c), self.active)

    def imag(self):
        return Taylor(object_map(mp.im, self.c), self.active)

    def conjugate(self):
        return Taylor(object_map(mp.conj, self.c), self.active)

    def reshape(self, *shape):
        return Taylor(self.c.reshape((self.order+1,)+shape), self.active)

    def take(self, *index):
        return Taylor(self.c[(slice(None),)+index], self.active)

    def sum(self, axis=None):
        if axis is None:
            axes = tuple(range(1, self.c.ndim))
        else:
            if isinstance(axis, int):
                axis = (axis,)
            axes = tuple(1+(a % len(self.shape)) for a in axis)
        return Taylor(np.sum(self.c, axis=axes), self.active)

    def value(self, point):
        out = np.array(self.c[-1], dtype=object, copy=True)
        for coefficient in self.c[-2::-1]:
            out = coefficient+point*out
        return out


def dot(left, right):
    return (left*right).sum(-1)


def cross(left, right):
    columns = [
        left.take(slice(None), 1)*right.take(slice(None), 2)
        -left.take(slice(None), 2)*right.take(slice(None), 1),
        left.take(slice(None), 2)*right.take(slice(None), 0)
        -left.take(slice(None), 0)*right.take(slice(None), 2),
        left.take(slice(None), 0)*right.take(slice(None), 1)
        -left.take(slice(None), 1)*right.take(slice(None), 0),
    ]
    return Taylor(np.stack([value.c for value in columns], axis=-1))


class MPSpline:
    def __init__(self, knots, coefficients, degree, converted=False):
        self.degree = int(degree)
        self.knots = list(knots) if converted else [exact_mpf(v) for v in knots]
        effective = len(self.knots)-self.degree-1
        values = np.asarray(coefficients[:effective], dtype=object)
        self.coefficients = values if converted else object_map(exact_mpf, values)

    def jet(self, center, direction, order):
        span = min(len(self.coefficients)-1, bisect_right(self.knots, center)-1)
        if not self.knots[self.degree] <= center <= self.knots[len(self.coefficients)]:
            raise ValueError("spline center outside actual base interval")
        work = [Taylor.constant(self.coefficients[span-self.degree+j], order)
                for j in range(self.degree+1)]
        for level in range(1, self.degree+1):
            for j in range(self.degree, level-1, -1):
                index = span-self.degree+j
                denominator = self.knots[index+self.degree-level+1]-self.knots[index]
                weight = Taylor.variable(center-self.knots[index], direction, order)/denominator
                work[j] = (1-weight)*work[j-1]+weight*work[j]
        return work[self.degree]

    def antiderivative(self):
        out = np.zeros((len(self.coefficients)+1,)+self.coefficients.shape[1:],
                       dtype=object)
        for i, value in enumerate(self.coefficients):
            out[i+1] = out[i]+value*(self.knots[i+self.degree+1]-self.knots[i])/(self.degree+1)
        return MPSpline([self.knots[0]]+self.knots+[self.knots[-1]], out,
                        self.degree+1, converted=True)


class MPFourier:
    def __init__(self):
        self.twiddles = {}
        self.permutations = {}

    def fft(self, array, inverse=False):
        """First array axis is frequency/sample; all other axes are batched."""
        array = np.asarray(array, dtype=object)
        count = len(array)
        if count < 1 or count & (count-1):
            raise ValueError("mp FFT size must be a power of two")
        if count not in self.permutations:
            bits = count.bit_length()-1
            self.permutations[count] = [
                int(format(j, f"0{bits}b")[::-1], 2) for j in range(count)]
        out = array[self.permutations[count]].copy()
        length = 2
        while length <= count:
            key = (length, inverse)
            if key not in self.twiddles:
                sign = 1 if inverse else -1
                self.twiddles[key] = [mp.exp(sign*2j*mp.pi*j/length)
                                      for j in range(length//2)]
            weights = self.twiddles[key]
            half = length//2
            for first in range(0, count, length):
                for j, weight in enumerate(weights):
                    even = out[first+j].copy()
                    odd = weight*out[first+j+half]
                    out[first+j] = even+odd
                    out[first+j+half] = even-odd
            length *= 2
        return out/count if inverse else out


class SymmetricMPTarget:
    def __init__(self, snapshot, quarter_nodes, angular_nodes):
        with np.load(snapshot, allow_pickle=False) as saved:
            self.frozen = {key: saved[key].copy() for key in saved.files}
        f = self.frozen
        self.nodes, self.angles = quarter_nodes, angular_nodes
        self.modes = f["phase_coefficients"].shape[1]
        for size in [self.nodes, self.angles]:
            if size & (size-1):
                raise ValueError("angular grids must be powers of two")
        if quarter_nodes < 4*self.modes+8 or angular_nodes < quarter_nodes:
            raise ValueError("insufficient finite primitive/evaluation grid")
        self.alpha = [exact_mpf(x) for x in f["alpha"]]
        self.raw = MPSpline(f["phase_knots"], f["phase_coefficients"], 5)
        self.base = MPSpline(f["base_knots"], f["base_radius_coefficients"],
                             int(f["base_degree"]))
        self.shift = MPSpline(f["shift_knots"], f["shift_coefficients"],
                              int(f["shift_degree"]))
        self.means = [
            MPSpline(f[f"mean{j}_knots"], f[f"mean{j}_radius_coefficients"],
                     int(f[f"mean{j}_degree"])) for j in range(len(self.alpha))]
        self.slopes = [
            MPSpline(f[f"height{j}_slope_knots"], f[f"height{j}_slope_coefficients"],
                     int(f[f"height{j}_slope_degree"])) for j in range(len(self.alpha)+1)]
        self.height_integrals = [sp.antiderivative() for sp in self.slopes]
        self.sines = np.array([
            [mp.sin(2*mp.pi*m*k/self.nodes) for k in range(self.nodes)]
            for m in range(1, self.modes+1)], dtype=object)
        self.frequency = [4*(k if k < self.nodes//2 else k-self.nodes)
                          for k in range(self.nodes)]
        self.fourier = MPFourier()

    def scalars(self, center, direction, order):
        bp = self.base.jet(center, direction, order)
        bm = self.base.jet(-center, -direction, order)
        pp = self.raw.jet(center, direction, order)
        pm = self.raw.jet(-center, -direction, order)
        beta = (pp.take(slice(None), 0)*(bp**3)
                +pm.take(slice(None), 0)*(bm**3))/2
        gamma = (pp.take(slice(None), 1)*(bp**2)
                 -pm.take(slice(None), 1)*(bm**2))/2
        radius = bp+bm+self.shift.jet(center, direction, order)+self.shift.jet(-center, -direction, order)
        for amplitude, sp in zip(self.alpha, self.means):
            radius += amplitude*(sp.jet(center, direction, order)+sp.jet(-center, -direction, order))
        radius /= 2
        height = Taylor.constant(0, order)
        for amplitude, sp in zip([mp.mpf(1)]+self.alpha, self.height_integrals):
            height += amplitude*(sp.jet(center, direction, order)-sp.jet(-center, -direction, order))/2
        return beta, gamma, radius, height

    def primitive(self, center, direction, order):
        beta, gamma, radius, height = self.scalars(center, direction, order)
        beta_grid = Taylor(beta.c@self.sines, beta.active)
        gamma_grid = Taylor(gamma.c@self.sines, gamma.active)
        eb, eg = (1j*beta_grid).exp(), (1j*gamma_grid).exp()
        tangent = np.stack([
            (-eg.real()*eb.imag()).c,
            (eg.real()*eb.real()).c,
            eg.imag().c], axis=-1)
        coefficient = np.transpose(
            self.fourier.fft(np.transpose(tangent, (1, 0, 2)))/self.nodes,
            (1, 0, 2))
        primitive = np.zeros_like(coefficient)
        for index, n in enumerate(self.frequency):
            primitive[:, index, 0] = (1j*n*coefficient[:, index, 0]+coefficient[:, index, 1])/(1-n*n)
            primitive[:, index, 1] = (-coefficient[:, index, 0]+1j*n*coefficient[:, index, 1])/(1-n*n)
            if n:
                primitive[:, index, 2] = coefficient[:, index, 2]/(1j*n)
        primitive[:, self.nodes//2, :] = 0
        primitive[:, 0, 1:] = 0
        primitive[:, 0, :] = object_map(mp.re, primitive[:, 0, :])
        # Enforce the real finite polynomial convention, changing only mp
        # roundoff; this convention is part of this diagnostic's definition.
        for k in range(1, self.nodes//2):
            value = (primitive[:, k, :]
                     +object_map(mp.conj, primitive[:, self.nodes-k, :]))/2
            primitive[:, k, :] = value
            primitive[:, self.nodes-k, :] = object_map(mp.conj, value)
        result = radius.reshape(1, 1)*Taylor(primitive)
        result.c[:, 0, 2] += height.c
        return result, radius

    def target(self, center, direction, order):
        coefficient, radius = self.primitive(center, direction, order)
        first = coefficient.derivative()
        E = (first*first.conjugate()).real().sum()
        ar, arr, Er = radius.derivative(), radius.derivative(2), E.derivative()
        C = ar*Er-2*arr*E
        K = C/(2*radius*E**2)
        return coefficient, radius, E, C, K

    def root(self, initial, iterations=12):
        point = mp.mpf(initial)
        trace = []
        for iteration in range(iterations):
            _, _, _, C, _ = self.target(point, 1, 3)
            step = mp.re(C.c[0]/C.c[1])
            trace.append({"iteration": iteration, "root": mp.nstr(point, mp.mp.dps),
                          "C": mp.nstr(C.c[0], 12), "step": mp.nstr(step, 12)})
            point -= step
            if abs(step) < mp.power(10, -mp.mp.dps+12):
                break
        _, _, _, C, K = self.target(point, 1, 3)
        return point, trace, C.c[0], K.c[0]

    def angular(self, coefficient, count=1):
        value = coefficient.c.copy()
        for _ in range(count):
            changed = np.zeros_like(value)
            for k, n in enumerate(self.frequency):
                changed[:, k, 0] = 1j*n*value[:, k, 0]-value[:, k, 1]
                changed[:, k, 1] = 1j*n*value[:, k, 1]+value[:, k, 0]
                changed[:, k, 2] = 1j*n*value[:, k, 2]
            value = changed
        return Taylor(value)

    def evaluate(self, coefficient):
        out = np.zeros((self.angles, coefficient.order+1, 3), dtype=object)
        for k in range(self.nodes):
            signed = k if k < self.nodes//2 else k-self.nodes
            out[signed % self.angles] = coefficient.c[:, k, :]
        samples = self.fourier.fft(out, inverse=True)*self.angles
        return Taylor(object_map(mp.re, np.transpose(samples, (1, 0, 2))))

    def root_density_taylor(self, root, degree, zero_order):
        # Three lost derivatives occur in K/rho; additional room keeps all
        # requested G coefficients independent of the padded high degrees.
        work_order = degree+5
        coefficient, radius, E, Ctarget, K = self.target(root, -1, work_order)
        residual = K.c[0]
        kappa_squared = np.zeros_like(K.c)
        kappa_squared[:-1] = -K.c[1:]
        kappa = Taylor(kappa_squared).sqrt()
        F = self.evaluate(coefficient)
        X = -F.derivative()
        Y = self.evaluate(self.angular(coefficient))
        Frr = F.derivative(2)
        Frt = -Y.derivative()
        Ftt = self.evaluate(self.angular(coefficient, 2))
        normal = cross(Y, X)
        normal_theta = cross(Ftt, X)+cross(Y, Frt)
        area2, radius2 = dot(normal, normal), dot(F, F)
        support = dot(normal, F)
        zeta = support/(area2*radius2).sqrt()
        lraw, mraw, nraw = [dot(normal, value) for value in (Frr, Frt, Ftt)]
        common = zeta**2*area2
        a, b, c = -nraw/common, mraw/common, -lraw/common
        curvature = (lraw*nraw-mraw**2)/area2**2
        omega = (curvature-K)/(zeta**4*a)
        chat = b*b/a+K/(zeta**4*a)
        U = F/radius2.sqrt().reshape(self.angles, 1)
        Ur = (X-U*dot(U, X).reshape(self.angles, 1))/radius2.sqrt().reshape(self.angles, 1)
        Ut = (Y-U*dot(U, Y).reshape(self.angles, 1))/radius2.sqrt().reshape(self.angles, 1)
        d = a*dot(Ur, Ur)+2*b*dot(Ur, Ut)+c*dot(Ut, Ut)
        log_zeta_theta = (dot(normal_theta, F)/support
                          -dot(normal, normal_theta)/area2-dot(F, Y)/radius2)
        kappa_total = kappa/zeta**2
        l_rho = kappa_total.derivative()/kappa_total
        l_theta = -2*log_zeta_theta
        if zero_order == "ground-state":
            ell = Y.take(slice(None), 2)/F.take(slice(None), 2)-dot(F, Y)/radius2
        elif zero_order == "unmodified-d":
            ell = Taylor.constant(np.zeros(self.angles, dtype=object), work_order)
        else:
            raise ValueError(zero_order)
        zero_term = d+omega*(ell*ell+ell*l_theta)
        # rho points into the negative component, so its mixed density is -b.
        brho = -b
        AA = -a/(16*kappa_total)
        BB = -(a*l_rho+brho*l_theta)/(4*kappa_total)
        CC = (zero_term-(a*l_rho*l_rho+2*brho*l_rho*l_theta+chat*l_theta*l_theta)/4)/kappa_total
        rho = Taylor.variable(mp.mpf(0), mp.mpf(1), work_order)
        G = (AA+rho*BB+rho*rho*CC).sum()/self.angles
        diagnostics = {
            "root_K_residual_before_division": mp.nstr(residual, mp.mp.dps),
            "kappa_radial_at_root": mp.nstr(kappa.c[0], mp.mp.dps),
            "minimum_a_at_root": mp.nstr(min(a.c[0]), 16),
            "minimum_zeta_at_root": mp.nstr(min(zeta.c[0]), 16),
            "minimum_Fz_over_r_at_root": mp.nstr(min(F.c[0, :, 2]/root), 16),
            "maximum_abs_omega_at_root": mp.nstr(max(abs(z) for z in omega.c[0]), 16),
            "work_Taylor_order": work_order,
            "rho_direction": "rho=t-r; mixed principal coefficient is minus the r coefficient",
        }
        return [mp.re(z) for z in G.c[:degree+1]], diagnostics


def parse_mpf(value):
    if "/" in value:
        first, second = value.split("/")
        return mp.mpf(first)/mp.mpf(second)
    return mp.mpf(value)


def finite_part_from_coefficients(coefficients, width, degree):
    return mp.fsum(coefficients[k]*width**(mp.mpf(k)-mp.mpf("1.5"))
                   /(mp.mpf(k)-mp.mpf("1.5")) for k in range(degree+1))


def uniform_grid_bulk_geometry(snapshot, quarter_nodes):
    """The frozen float evaluator with exact finite-grid FFT evaluation.

    The coefficient construction, radial means, and metric are inherited
    unchanged. Only evaluation of the SAME finite Fourier polynomial on a
    uniform tensor grid is replaced by an inverse FFT with zero padding.
    The generic evaluator remains frozen in fourfold_phase_beta_probe.py.
    Both paths use ordinary floating arithmetic, not directed arithmetic.
    """
    from fourfold_phase_beta_probe import SymmetricFrozenGeometry

    class UniformGridFrozenGeometry(SymmetricFrozenGeometry):
        def paired_jets(self, x, theta):
            x, theta = np.broadcast_arrays(np.asarray(x), np.asarray(theta))
            if x.ndim != 2:
                raise ValueError("bulk FFT evaluator requires a tensor grid")
            radial, count = x[:, 0], x.shape[1]
            if not np.all(x == radial[:, None]):
                raise ValueError("radial grid is not a tensor product")
            expected = np.arange(count)[None, :]*(np.pi/2)/count
            if not np.allclose(theta, expected, rtol=0., atol=1e-15):
                raise ValueError("angular grid is not the specified uniform grid")
            if count < self.nodes:
                raise ValueError("evaluation grid is smaller than the primitive")
            radial_fields = self.radial_coefficients(radial)["radial"]
            fields = (
                radial_fields[0], radial_fields[1], self.angular(radial_fields[0]),
                radial_fields[2], self.angular(radial_fields[1]), self.angular(radial_fields[0], 2),
                radial_fields[3], self.angular(radial_fields[2]), self.angular(radial_fields[1], 2),
                self.angular(radial_fields[0], 3),
            )
            signed = np.arange(self.nodes)
            signed = np.where(signed < self.nodes//2, signed, signed-self.nodes)

            def evaluate(coefficient):
                padded = np.zeros((len(radial), count, 3), dtype=complex)
                padded[:, signed % count, :] = coefficient
                return (np.fft.ifft(padded, axis=1)*count).real

            return tuple(evaluate(field) for field in fields)

    return UniformGridFrozenGeometry(snapshot, quarter_nodes)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--frozen-inputs", type=Path, required=True)
    ap.add_argument("--quarter-nodes", type=int, default=128)
    ap.add_argument("--angles", type=int, default=256)
    ap.add_argument("--dps", type=int, default=60)
    ap.add_argument("--degrees", type=int, nargs="+", default=[8, 12])
    ap.add_argument("--collars", nargs="+", default=["1/2048", "1/4096"])
    ap.add_argument("--gauss", type=int, default=12)
    ap.add_argument("--root-initial", default="0.238369915731")
    ap.add_argument("--zero-order", choices=["ground-state", "unmodified-d"],
                    default="ground-state")
    ap.add_argument("--no-bulk", action="store_true")
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    mp.mp.dps = args.dps
    started = time.monotonic()
    source_sha256 = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    geometry = SymmetricMPTarget(args.frozen_inputs, args.quarter_nodes, args.angles)
    root, root_trace, C_residual, K_residual = geometry.root(args.root_initial)
    print(json.dumps({"stage": "root", "root": mp.nstr(root, args.dps),
                      "C_residual": mp.nstr(C_residual, 12),
                      "seconds": time.monotonic()-started}), flush=True)
    coefficients, diagnostics = geometry.root_density_taylor(
        root, max(args.degrees), args.zero_order)
    print(json.dumps({"stage": "Taylor", "g0": mp.nstr(coefficients[0], 18),
                      "g1": mp.nstr(coefficients[1], 18),
                      "seconds": time.monotonic()-started}), flush=True)
    report = {
        "kind": "high_precision_root_Taylor_full_phase_diagnostic_not_interval_certificate",
        "inputs": str(args.frozen_inputs),
        "inputs_sha256": hashlib.sha256(args.frozen_inputs.read_bytes()).hexdigest(),
        "script_sha256": source_sha256,
        "dps": args.dps, "quarter_nodes": args.quarter_nodes,
        "angular_quadrature_nodes": args.angles,
        "root": mp.nstr(root, args.dps), "root_Newton_trace": root_trace,
        "root_K_residual": mp.nstr(K_residual, args.dps),
        "zero_order": args.zero_order,
        "exact_object_definition": "frozen binary64 spline inputs; physical a,beta even; gamma and exact-integral Z odd",
        "finite_primitive_definition": "mp DFT at stated quarter grid; Nyquist deleted; real conjugate symmetry projected",
        "Taylor_coefficient_definition": "G(rho)=rho^(5/2) times angular mean of R50 J, ordinary Taylor coefficients at rho=0",
        "G_Taylor_coefficients": [mp.nstr(value, args.dps) for value in coefficients],
        "root_diagnostics": diagnostics, "half_core_to_beta_factor": ".5",
        "bulk_method": "same frozen finite Fourier polynomial, zero-padded uniform-grid FFT, binary64 Gauss-Legendre",
        "gauss_order": args.gauss,
        "runs": [],
        "limitations": [
            "High precision ordinary arithmetic, not directed interval rounding",
            "Finite primitive and angular quadrature; no full infinite Fourier tail or alias error is paid",
            "A finite Taylor polynomial is integrated exactly; no analytic remainder bound is claimed",
            "Bulk quadrature, when used, is the original binary64 finite-primitive evaluator",
            "Root residual is reported before the formal division by rho; a directed root enclosure remains necessary",
            "R46 complete network, parameter family, finite low block and exact closed isometric family remain separate",
        ],
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+"\n")
    if not args.no_bulk:
        from fourfold_phase_beta_probe import integrate_bulk
        bulk_geometry = uniform_grid_bulk_geometry(args.frozen_inputs, args.quarter_nodes)
    for width_text in args.collars:
        width = parse_mpf(width_text)
        if width <= 0 or width >= root:
            raise ValueError("invalid collar width")
        if args.no_bulk:
            bulk, bulk_diagnostics = None, None
        else:
            bulk, bulk_diagnostics = integrate_bulk(
                bulk_geometry, float(root-width), args.gauss, args.angles, args.zero_order)
        for degree in args.degrees:
            collar = finite_part_from_coefficients(coefficients, width, degree)
            row = {
                "collar_width": width_text, "Taylor_degree": degree,
                "collar_finite_part_mp": mp.nstr(collar, args.dps),
                "bulk_float": bulk,
                "beta_mp_collar_plus_float_bulk": None if bulk is None
                    else mp.nstr((exact_mpf(bulk)+collar)/2, args.dps),
                "bulk_diagnostics": bulk_diagnostics,
            }
            report["runs"].append(row)
            args.out.write_text(json.dumps(report, indent=2)+"\n")
            print(json.dumps({key:value for key,value in row.items() if key!="bulk_diagnostics"}),
                  flush=True)
    report["finished"] = True
    report["wall_seconds"] = time.monotonic()-started
    args.out.write_text(json.dumps(report, indent=2)+"\n")


if __name__ == "__main__":
    main()
