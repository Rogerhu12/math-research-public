#!/usr/bin/env python3
"""Directed vector kernel; every FFT and elementary operation is enclosed.

The source was reconstructed after the executor reset. It retains complete
infinite Fourier error budgets and exact scalar-span selection. It is not a
floating FFT checker and does not turn a partial integration into a proof.
"""
from __future__ import annotations
import math
from fractions import Fraction
import numpy as np
from flint import arb, acb, ctx
from fourfold_phase_root_interval import Box, stack, rational_box
from fourfold_phase_uniform_tail import up, down
from fourfold_phase_beta_interval import primitive_fourier_budget
from fourfold_phase_beta_bulk_interval import BulkTarget, exact_arb, real_interval


def arb_box(value):
    value = arb(value)
    if not value.is_finite():
        raise ValueError("nonfinite transfer from Arb")
    if value == 0:
        return Box(0.)
    return Box(down(float(value.lower())), up(float(value.upper())))


def scalar_arb(value):
    return arb(float(value.lo)).union(arb(float(value.hi)))


def reduce_box(value, axis=0):
    lo, hi = np.moveaxis(value.lo, axis, 0), np.moveaxis(value.hi, axis, 0)
    while len(lo) > 1:
        n = len(lo)//2
        result = Box(lo[:2*n:2], hi[:2*n:2])+Box(lo[1:2*n:2], hi[1:2*n:2])
        if len(lo) % 2:
            lo, hi = np.concatenate([result.lo, lo[-1:]]), np.concatenate([result.hi, hi[-1:]])
        else:
            lo, hi = result.lo, result.hi
    return Box(lo[0], hi[0])


def square_box(value):
    a, b = value.lo*value.lo, value.hi*value.hi
    lower = np.where((value.lo <= 0)&(value.hi >= 0), 0., down(np.minimum(a, b)))
    return Box(lower, up(np.maximum(a, b)))


class CBox:
    __array_priority__ = 2000

    def __init__(self, real=0., imag=0.):
        self.real, self.imag = Box.coerce(real), Box.coerce(imag)
        shape = np.broadcast_shapes(self.real.lo.shape, self.imag.lo.shape)
        if self.real.lo.shape != shape:
            self.real = Box(np.broadcast_to(self.real.lo, shape).copy(), np.broadcast_to(self.real.hi, shape).copy())
        if self.imag.lo.shape != shape:
            self.imag = Box(np.broadcast_to(self.imag.lo, shape).copy(), np.broadcast_to(self.imag.hi, shape).copy())

    @property
    def is_real(self):
        # FFT views share arrays. A stored flag would become stale.
        return not np.any(self.imag.lo) and not np.any(self.imag.hi)

    @staticmethod
    def coerce(value):
        if isinstance(value, CBox):
            return value
        if isinstance(value, complex):
            return CBox(value.real, value.imag)
        return CBox(value)

    @staticmethod
    def from_acb(value):
        value = acb(value)
        return CBox(arb_box(value.real), arb_box(value.imag))

    def to_acb(self):
        return acb(scalar_arb(self.real), scalar_arb(self.imag))

    def __add__(self, value):
        value = self.coerce(value)
        return CBox(self.real+value.real) if self.is_real and value.is_real else CBox(self.real+value.real, self.imag+value.imag)

    __radd__ = __add__

    def __neg__(self):
        return CBox(-self.real, -self.imag)

    def __sub__(self, value):
        return self+-self.coerce(value)

    def __rsub__(self, value):
        return self.coerce(value)+-self

    def __mul__(self, value):
        value = self.coerce(value)
        if self.is_real:
            return CBox(self.real*value.real) if value.is_real else CBox(self.real*value.real, self.real*value.imag)
        if value.is_real:
            return CBox(self.real*value.real, self.imag*value.real)
        return CBox(self.real*value.real-self.imag*value.imag, self.real*value.imag+self.imag*value.real)

    __rmul__ = __mul__

    def reciprocal(self):
        denominator = square_box(self.real)+square_box(self.imag)
        return CBox(self.real/denominator, -self.imag/denominator)

    def __truediv__(self, value):
        return self*self.coerce(value).reciprocal()

    def __rtruediv__(self, value):
        return self.coerce(value)*self.reciprocal()

    def __pow__(self, n):
        if n < 0:
            return self.reciprocal()**(-n)
        result = CBox(1.)
        for _ in range(n):
            result = result*self
        return result

    def __getitem__(self, key):
        return CBox(self.real[key], self.imag[key])

    def __setitem__(self, key, value):
        value = self.coerce(value)
        for name in ("real", "imag"):
            destination, source = getattr(self, name), getattr(value, name)
            destination.lo[key], destination.hi[key] = source.lo, source.hi

    def reshape(self, *shape):
        return CBox(self.real.reshape(*shape), self.imag.reshape(*shape))

    def transpose(self, *axes):
        return CBox(self.real.transpose(*axes), self.imag.transpose(*axes))

    def sum(self, axis=0):
        return CBox(reduce_box(self.real, axis), reduce_box(self.imag, axis))

    def magnitude_upper(self):
        return up(self.real.abs_upper()+self.imag.abs_upper())

    def pad(self, fee, real_only=False):
        fee = Box.coerce(fee).hi
        return CBox(self.real+Box(-fee, fee), Box(np.zeros_like(self.real.lo)) if real_only else self.imag+Box(-fee, fee))


def zeros(shape):
    return CBox(Box(np.zeros(shape)), Box(np.zeros(shape)))


def cstack(values, axis=0):
    return CBox(stack([v.real for v in values], axis), stack([v.imag for v in values], axis))


SCOEF = [rational_box(Fraction((-1)**((n-1)//2), math.factorial(n))) if n % 2 else Box(0.) for n in range(33)]
CCOEF = [rational_box(Fraction((-1)**(n//2), math.factorial(n))) if n % 2 == 0 else Box(0.) for n in range(33)]


def complex_sincos(value):
    radius = arb(float(np.max(value.magnitude_upper())))
    if not radius < 3:
        raise ValueError("complex phase argument too wide")
    sine, cosine = CBox(0.), CBox(0.)
    for n in range(32, -1, -1):
        sine, cosine = sine*value+SCOEF[n], cosine*value+CCOEF[n]
    fee = arb_box((radius.exp()*radius**33/math.factorial(33)).upper())
    return sine.pad(fee, value.is_real), cosine.pad(fee, value.is_real)


def trig_jets(value):
    s, c = complex_sincos(value[0])
    b1, b2, b3 = value[1], value[2], value[3]
    return (cstack([s, c*b1, c*b2-s*b1*b1, c*b3-3*s*b1*b2-c*b1*b1*b1]),
            cstack([c, -s*b1, -s*b2-c*b1*b1, -s*b3-3*c*b1*b2+s*b1*b1*b1]))


def jet_product(left, right):
    return cstack([sum((math.comb(n, j)*left[j]*right[n-j] for j in range(n+1)), CBox(0.)) for n in range(4)])


def cdot(left, right):
    return (left*right).sum(-1)


def ccross(left, right):
    return cstack([left[..., 1]*right[..., 2]-left[..., 2]*right[..., 1],
                   left[..., 2]*right[..., 0]-left[..., 0]*right[..., 2],
                   left[..., 0]*right[..., 1]-left[..., 1]*right[..., 0]], -1)


class DirectedFFT:
    def __init__(self):
        self.cache = {}

    def fft(self, value, axis=0, inverse=False):
        if axis:
            order = [axis]+[j for j in range(value.real.lo.ndim) if j != axis]
            return self.fft(value.transpose(*order), inverse=inverse).transpose(*np.argsort(order))
        n = value.real.lo.shape[0]
        if n & (n-1):
            raise ValueError("FFT length not a power of two")
        key = n, inverse, ctx.prec
        if key not in self.cache:
            bits = n.bit_length()-1
            permutation = [int(format(j, f"0{bits}b")[::-1], 2) for j in range(n)]
            factors = {}
            for width in (1 << j for j in range(1, bits+1)):
                factors[width] = cstack([CBox.from_acb(acb(0, (2 if inverse else -2)*arb.pi()*j/width).exp())
                                        for j in range(width//2)])
            self.cache[key] = permutation, factors
        permutation, factors = self.cache[key]
        result = CBox(Box(value.real.lo[permutation].copy(), value.real.hi[permutation].copy()),
                      Box(value.imag.lo[permutation].copy(), value.imag.hi[permutation].copy()))
        rest = result.real.lo.shape[1:]
        for width, roots in factors.items():
            half = width//2
            grouped = result.reshape(n//width, width, *rest)
            a, b = grouped[:, :half], grouped[:, half:]*roots.reshape(1, half, *([1]*len(rest)))
            top, bottom = a+b, a-b
            grouped[:, :half], grouped[:, half:] = top, bottom
        return result/n if inverse else result


class FastBulkTarget(BulkTarget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fast_fourier, self.fast_cell_cache, self.tail_factor_cache = DirectedFFT(), {}, {}
        self.sample_count = self.angles//2+1
        self.fast_sines = CBox(stack([stack([arb_box(x) for x in row]) for row in self.sines]))
        self.angle_sines = CBox(stack([stack([arb_box((2*arb.pi()*m*k/self.angles).sin()) for k in range(self.sample_count)])
                                       for m in range(1, self.modes+1)]))
        self.angle_cosines = CBox(stack([stack([arb_box((2*arb.pi()*m*k/self.angles).cos()) for k in range(self.sample_count)])
                                         for m in range(1, self.modes+1)]))
        self.angle_shift_cache = {}

    def set_cell(self, left, right):
        super().set_cell(left, right)
        if self.cell not in self.fast_cell_cache:
            anchor = exact_arb((self.cell[0]+self.cell[1])/2)
            old_cap, ctx.cap = ctx.cap, 21
            scalar = self.scalars(acb(anchor), 1)
            lower, upper = [], []
            for group in scalar:
                if isinstance(group, np.ndarray):
                    array = group
                else:
                    array = np.empty((), object)
                    array[()] = group
                lo, hi = np.zeros((21,)+array.shape), np.zeros((21,)+array.shape)
                for index in np.ndindex(array.shape):
                    for n in range(21):
                        value = array[index][n]
                        if not value.imag.contains(0):
                            raise ValueError("real scalar germ lost real structure")
                        interval = arb_box(value.real)
                        lo[(n,)+index], hi[(n,)+index] = interval.lo, interval.hi
                lower.append(lo.reshape(21, -1)); upper.append(hi.reshape(21, -1))
            ctx.cap = old_cap
            self.fast_cell_cache[self.cell] = anchor, CBox(Box(np.concatenate(lower, 1), np.concatenate(upper, 1)))
        self.anchor, self.scalar_poly = self.fast_cell_cache[self.cell]
        self.scalar_abs = self.scalar_poly.magnitude_upper()

    def finite_data(self, radial):
        delta = CBox.from_acb(radial-acb(self.anchor))
        jet = zeros((4, 2*self.modes+2))
        for n in range(20, -1, -1):
            jet = jet*delta+cstack([self.scalar_poly[n], jet[0], 2*jet[1], 3*jet[2]])
        beta, gamma, radius, height = jet[:, :self.modes], jet[:, self.modes:2*self.modes], jet[:, -2], jet[:, -1]
        self.last_scalar = beta, gamma, radius, height
        b = (beta.reshape(4, self.modes, 1)*self.fast_sines.reshape(1, self.modes, self.nodes)).sum(1)
        g = (gamma.reshape(4, self.modes, 1)*self.fast_sines.reshape(1, self.modes, self.nodes)).sum(1)
        sb, cb = trig_jets(b); sg, cg = trig_jets(g)
        tangent = cstack([-jet_product(cg, sb), jet_product(cg, cb), sg], -1)
        coefficient = self.fast_fourier.fft(tangent, 1)/self.nodes
        primitive = zeros((4, self.nodes, 3))
        n = np.asarray(self.frequency)
        ii = CBox(0., Box(n.reshape(1, -1)))
        primitive[:, :, 0] = (ii*coefficient[:, :, 0]+coefficient[:, :, 1])/Box((1-n*n).reshape(1, -1))
        primitive[:, :, 1] = (-coefficient[:, :, 0]+ii*coefficient[:, :, 1])/Box((1-n*n).reshape(1, -1))
        nonzero = np.flatnonzero(n)
        primitive[:, nonzero, 2] = coefficient[:, nonzero, 2]/CBox(0., Box(n[nonzero].reshape(1, -1)))
        primitive[:, self.nodes//2, :] = 0.
        primitive[:, 0, 1], primitive[:, 0, 2] = 0., 0.
        pos = np.arange(1, self.nodes//2)
        for j, parity in enumerate((1, -1, 1)):
            value = (primitive[:, pos, j]+parity*primitive[:, -pos, j])/2
            primitive[:, pos, j], primitive[:, -pos, j] = value, parity*value
        primitive = jet_product(primitive, radius.reshape(4, 1, 1))
        primitive[:, 0, 2] = primitive[:, 0, 2]+height
        return primitive, radius

    def tail_errors(self, radial, inner_sigma=arb(0)):
        rho = arb_box(abs(radial-acb(self.anchor)).upper()+self.tail_radius).hi
        bounds = np.zeros(2*self.modes+2)
        for n in range(20, -1, -1):
            bounds = up(up(bounds*rho)+self.scalar_abs[n])
        phase = sum(((arb(float(bounds[j]))+arb(float(bounds[self.modes+j])))*(self.tail_sigma*(j+1)).cosh()
                     for j in range(self.modes)), arb(0)).upper()
        key = inner_sigma.str(35)
        if key not in self.tail_factor_cache:
            self.tail_factor_cache[key] = primitive_fourier_budget(self.nodes, self.tail_sigma, inner_sigma,
                self.tail_radius, arb(1), arb(0), arb(1))[0]
        factor = arb(float(bounds[-2]))*phase.exp()
        return [(x*factor).upper() for x in self.tail_factor_cache[key]]

    def complete_fast_data(self, radial):
        coefficient, radius = self.finite_data(radial)
        errors = self.tail_errors(radial)
        reverse = (-np.arange(self.nodes)) % self.nodes
        E0 = cdot(coefficient[1], coefficient[1, reverse]).sum()
        E1 = 2*cdot(coefficient[1], coefficient[2, reverse]).sum()
        E2 = 2*(cdot(coefficient[2], coefficient[2, reverse])+cdot(coefficient[1], coefficient[3, reverse])).sum()
        eps = [arb_box(math.factorial(j)*errors[0]/self.tail_radius**j) for j in range(4)]
        B = [Box(np.max(reduce_box(Box(coefficient[j].magnitude_upper())).hi)) for j in range(4)]
        fees = [3*(2*B[1]*eps[1]+eps[1]*eps[1]),
                6*(B[1]*eps[2]+B[2]*eps[1]+eps[1]*eps[2]),
                6*(2*B[2]*eps[2]+eps[2]*eps[2]+B[1]*eps[3]+B[3]*eps[1]+eps[1]*eps[3])]
        real = radial.imag == 0
        E0, E1, E2 = [E.pad(fee, real) for E, fee in zip((E0, E1, E2), fees)]
        a, ar, arr, arrr = [radius[j] for j in range(4)]
        N, Np = ar*E1-2*arr*E0, ar*E2-arr*E1-2*arrr*E0
        K = N/(2*a*E0*E0)
        Kp = Np/(2*a*E0*E0)-K*(ar/a+2*E1/E0)
        if real:
            K, Kp = CBox(K.real), CBox(Kp.real)
        return coefficient, K, Kp, errors, real

    def fast_fields(self, radial, coefficient, errors, real, sigma=None):
        if sigma is not None:
            if not real:
                raise ValueError("complex angle cover requires real r")
            errors = self.tail_errors(radial, sigma+arb.pi()/self.angles)
            modes = np.abs(np.asarray(self.frequency)//4)
            re = stack([arb_box(k*arb.pi()/self.angles+(k*sigma).cosh()-1) for k in modes]).reshape(-1, 1)
            im = stack([arb_box((k*sigma).sinh()) for k in modes]).reshape(-1, 1)
        fields = {}
        for ar in range(3):
            values = coefficient[ar]
            fee = arb_box(math.factorial(ar)*errors[0]/self.tail_radius**ar)
            data = zeros((self.angles, 3))
            data[(np.asarray(self.frequency)//4) % self.angles] = values
            samples = (self.fast_fourier.fft(data, inverse=True)*self.angles)[:self.sample_count]
            if sigma is None:
                fields[(ar, 0)] = samples.pad(fee, real)
            else:
                magnitude = Box(values.magnitude_upper())
                rf, imf = (fee+reduce_box(magnitude*re)).hi, (fee+reduce_box(magnitude*im)).hi
                fields[(ar, 0)] = CBox(samples.real+Box(-rf, rf), Box(-imf, imf))
        beta, gamma, radius, _ = self.last_scalar
        ss, cc = self.angle_sines, self.angle_cosines
        if sigma is not None:
            key = sigma.str(35)
            if key not in self.angle_shift_cache:
                gap, width = arb_box(arb.pi()/self.angles).hi, arb_box(sigma).hi
                shift = CBox(Box(-gap, gap), Box(-width, width))
                s, c = complex_sincos(CBox(np.arange(1, self.modes+1))*shift)
                s, c = s.reshape(-1, 1), c.reshape(-1, 1)
                self.angle_shift_cache[key] = ss*c+cc*s, cc*c-ss*s
            ss, cc = self.angle_shift_cache[key]
        b = (beta.reshape(4, self.modes, 1)*ss.reshape(1, self.modes, self.sample_count)).sum(1)
        g = (gamma.reshape(4, self.modes, 1)*ss.reshape(1, self.modes, self.sample_count)).sum(1)
        sb, cb = trig_jets(b); sg, cg = trig_jets(g)
        T = cstack([-jet_product(cg, sb), jet_product(cg, cb), sg], -1)
        modes = CBox((4*np.arange(1, self.modes+1)).reshape(-1, 1))
        bt, gt = (beta[0].reshape(-1, 1)*modes*cc).sum(), (gamma[0].reshape(-1, 1)*modes*cc).sum()
        dT = cstack([sg[0]*gt*sb[0]-cg[0]*cb[0]*bt-T[0, :, 1],
                     -sg[0]*gt*cb[0]-cg[0]*sb[0]*bt+T[0, :, 0], cg[0]*gt], -1)
        fields[(0, 1)], fields[(1, 1)], fields[(0, 2)] = radius[0]*T[0], radius[1]*T[0]+radius[0]*T[1], radius[0]*dT
        if real and sigma is None:
            for key in ((0, 1), (1, 1), (0, 2)):
                fields[key] = CBox(fields[key].real)
        return fields

    def fast_density(self, radial, sigma=None, waist=False):
        self.evaluations += 1
        coefficient, K, Kp, errors, real = self.complete_fast_data(radial)
        if not np.all(K.real.hi < 0):
            raise ValueError("negative target curvature gate failed")
        kappa = CBox.from_acb((-K).to_acb().sqrt(analytic=True))
        fields = self.fast_fields(radial, coefficient, errors, real, sigma)
        F, X, Frr, Y, Frt, Ftt = [fields[key] for key in ((0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (0, 2))]
        normal = ccross(Y, X)
        nr, nt = ccross(Frt, X)+ccross(Y, Frr), ccross(Ftt, X)+ccross(Y, Frt)
        area, radius, support = cdot(normal, normal), cdot(F, F), cdot(normal, F)
        if any(not np.all(z.real.lo > 0) for z in (area, radius, support)):
            raise ValueError("area/radius/support denominator gate failed")
        l, m, n = [cdot(normal, q) for q in (Frr, Frt, Ftt)]
        a, b, c = -n/area, m/area, -l/area
        if not np.all(a.real.lo > 0):
            raise ValueError("actual zeta^2 a denominator gate failed")
        omega, chat = ((l*n-m*m)/(area*area)-K)/a, (b*b+K)/a
        FX, FY = cdot(F, X), cdot(F, Y)
        d = (a*(cdot(X, X)-FX*FX/radius)+2*b*(cdot(X, Y)-FX*FY/radius)+c*(cdot(Y, Y)-FY*FY/radius))/radius
        lzr, lzt = cdot(nr, F)/support-cdot(normal, nr)/area-FX/radius, cdot(nt, F)/support-cdot(normal, nt)/area-FY/radius
        fr, ft = Kp/(2*K)-2*lzr, -2*lzt
        if waist:
            if not np.all(X[:, 2].real.lo > 0):
                raise ValueError("waist Fz/r derivative lower bound failed")
            ell = Frt[:, 2]/X[:, 2]-FY/radius
        else:
            if not np.all(F[:, 2].real.lo > 0):
                raise ValueError("actual Fz denominator gate failed")
            ell = Y[:, 2]/F[:, 2]-FY/radius
        value = (d+omega*(ell*ell+ell*ft)-(a*fr*fr+2*b*fr*ft+chat*ft*ft)/4)/kappa
        if not np.all(np.isfinite(value.magnitude_upper())):
            raise ValueError("nonfinite actual phase density")
        return value

    def mean_callback(self, radial, analytic):
        try:
            value = self.fast_density(radial)
            # Exact reflection F(-theta)=diag(1,-1,1)F(theta) makes J even.
            return ((value[0]+value[-1]+2*value[1:-1].sum())/self.angles).to_acb()
        except (ValueError, ZeroDivisionError, OverflowError):
            self.failed_analytic_evaluations += 1
            return acb("nan")

    def angular_domain(self, left, right, sigma, waist=False):
        values = self.fast_density(acb(real_interval(left, right)), sigma, waist)
        bound = arb(float(np.max(values.magnitude_upper())))
        return bound, (2*bound*(-sigma*self.angles).exp()/(1-(-sigma*self.angles).exp())).upper()

    def waist_cap(self, width):
        self.set_cell(Fraction(0), width)
        value = self.fast_density(acb(real_interval(0, width)), arb(0), True)
        bound = arb(float(np.max(value.magnitude_upper())))
        return arb(0, (exact_arb(width)*bound).upper()), bound
