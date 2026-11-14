#!/usr/bin/env python3
"""Continuous metric enclosure of an explicitly frozen finite C2 prefix.

Binary64 nodal positions, derivatives and saved second jets define exact
rational quintics. The original scalar profile is retained exactly. Every
arithmetic operation below is enclosed with nextafter in binary extended
precision; FFT roots use half-angle square roots whose endpoints are checked
by exact rational squaring. No library FFT or sampled maximum is a proof step.
This certifies a finite approximate isometry, not an exact immersion, closed
surface, reach, or amplitude theorem.
"""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
import argparse
import bisect
import gzip
import hashlib
import importlib.util
import json
import math
import time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np

P = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('metric_interval_base', P/'geometry_20261114_r225_free_core_bvp.py')
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
LD = np.longdouble
INF = LD(np.inf)


def down(x):
    return np.nextafter(np.asarray(x, dtype=LD), -INF)


def up(x):
    return np.nextafter(np.asarray(x, dtype=LD), INF)


def rational(x):
    return Q(*LD(x).as_integer_ratio())


def float_down(x):
    y = float(x)
    return float(np.nextafter(y, -np.inf)) if LD(y) > x else y


def float_up(x):
    y = float(x)
    return float(np.nextafter(y, np.inf)) if LD(y) < x else y


class I:
    def __init__(self, lo, hi=None):
        self.lo = np.asarray(lo, dtype=LD)
        self.hi = self.lo.copy() if hi is None else np.asarray(hi, dtype=LD)

    @classmethod
    def fraction(cls, x):
        x = Q(x)
        v = LD(x.numerator)/LD(x.denominator)
        lo, hi = LD(v), LD(v)
        while rational(lo) > x:
            lo = np.nextafter(lo, -INF)
        while rational(hi) < x:
            hi = np.nextafter(hi, INF)
        return cls(lo, hi)

    def __getitem__(self, k):
        return I(self.lo[k], self.hi[k])

    def __setitem__(self, k, v):
        v = interval(v)
        self.lo[k], self.hi[k] = v.lo, v.hi

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __add__(self, v):
        v = interval(v)
        return I(down(self.lo+v.lo), up(self.hi+v.hi))

    __radd__ = __add__

    def __sub__(self, v):
        return self+-interval(v)

    def __rsub__(self, v):
        return interval(v)+-self

    def __mul__(self, v):
        v = interval(v)
        products = np.stack(np.broadcast_arrays(self.lo*v.lo, self.lo*v.hi,
                                                self.hi*v.lo, self.hi*v.hi))
        return I(down(products.min(axis=0)), up(products.max(axis=0)))

    __rmul__ = __mul__

    def __truediv__(self, v):
        v = interval(v)
        if np.any((v.lo <= 0) & (v.hi >= 0)):
            raise ZeroDivisionError('An interval divisor contains zero')
        return self*I(down(1/v.hi), up(1/v.lo))

    def __rtruediv__(self, v):
        return interval(v)/self

    def magnitude(self):
        return np.maximum(abs(self.lo), abs(self.hi))

    def copy(self):
        return I(self.lo.copy(), self.hi.copy())


def interval(x):
    return x if isinstance(x, I) else I(x)


def stack(items, axis=0):
    return I(np.stack([v.lo for v in items], axis=axis),
             np.stack([v.hi for v in items], axis=axis))


def sum_interval(a, axis=-1):
    lo = np.moveaxis(a.lo, axis, -1)
    hi = np.moveaxis(a.hi, axis, -1)
    while lo.shape[-1] > 1:
        n = lo.shape[-1]//2
        ll = down(lo[..., :2*n:2]+lo[..., 1:2*n:2])
        hh = up(hi[..., :2*n:2]+hi[..., 1:2*n:2])
        if lo.shape[-1] % 2:
            ll = np.concatenate([ll, lo[..., -1:]], axis=-1)
            hh = np.concatenate([hh, hi[..., -1:]], axis=-1)
        lo, hi = ll, hh
    return I(lo[..., 0], hi[..., 0])


def sqrt_checked(a):
    """Only used for scalar FFT roots; certify both results by rational square."""
    if a.lo < 0:
        raise ValueError('Negative square root input')
    lo = LD(np.sqrt(a.lo))
    hi = LD(np.sqrt(a.hi))
    while rational(lo)**2 > rational(a.lo):
        lo = np.nextafter(lo, -INF)
    while rational(hi)**2 < rational(a.hi):
        hi = np.nextafter(hi, INF)
    assert rational(lo)**2 <= rational(a.lo)
    assert rational(hi)**2 >= rational(a.hi)
    return I(lo, hi)


def complex_mul(ar, ai, br, bi):
    return ar*br-ai*bi, ar*bi+ai*br


class IntervalFFT:
    def __init__(self, n):
        if n < 4 or n & (n-1):
            raise ValueError('A power-of-two FFT length at least four is needed')
        self.n = n
        bits = n.bit_length()-1
        self.reverse = np.array([int(f'{k:0{bits}b}'[::-1], 2) for k in range(n)])
        self.twiddles = {}
        root_c = I(0)
        self.twiddles[2] = (I([1]), I([0]))
        length = 4
        while length <= n:
            if length == 4:
                cr, sr = I(0), I(1)
            else:
                cr = sqrt_checked((1+root_c)/2)
                sr = sqrt_checked((1-root_c)/2)
            root_c = cr
            real, imag = [I(1)], [I(0)]
            for j in range(1, length//2):
                re, im = complex_mul(real[-1], imag[-1], cr, sr)
                real.append(re)
                imag.append(im)
            self.twiddles[length] = stack(real), stack(imag)
            length *= 2

    def transform(self, re, im=None, sign=1):
        """Unnormalized sum c[k] exp(sign*2*pi*i*j*k/n)."""
        re = re[..., self.reverse].copy()
        im = I(np.zeros_like(re.lo)) if im is None else im[..., self.reverse].copy()
        original_shape = re.lo.shape
        length = 2
        while length <= self.n:
            half = length//2
            shape = original_shape[:-1]+(self.n//length, length)
            rr = I(re.lo.reshape(shape), re.hi.reshape(shape))
            ii = I(im.lo.reshape(shape), im.hi.reshape(shape))
            ar, ai = rr[..., :half], ii[..., :half]
            wr, wi = self.twiddles[length]
            if sign == -1:
                wi = -wi
            br, bi = complex_mul(rr[..., half:], ii[..., half:], wr, wi)
            left_r, right_r = ar+br, ar-br
            left_i, right_i = ai+bi, ai-bi
            re = I(np.concatenate([left_r.lo, right_r.lo], axis=-1).reshape(original_shape),
                   np.concatenate([left_r.hi, right_r.hi], axis=-1).reshape(original_shape))
            im = I(np.concatenate([left_i.lo, right_i.lo], axis=-1).reshape(original_shape),
                   np.concatenate([left_i.hi, right_i.hi], axis=-1).reshape(original_shape))
            length *= 2
        return re, im


def bezier(y0, d0, dd0, y1, d1, dd1, h):
    return stack([y0, y0+h*d0/5, y0+2*h*d0/5+h*h*dd0/20,
                  y1-2*h*d1/5+h*h*dd1/20, y1-h*d1/5, y1])


def split_bezier(c, t):
    row = c.copy()
    left, right = [row[0]], [row[-1]]
    while len(row.lo) > 1:
        row = (1-t)*row[:-1]+t*row[1:]
        left.append(row[0])
        right.append(row[-1])
    return stack(left), stack(right[::-1])


def elevate(a, degree):
    old = len(a.lo)-1
    return stack([sum((I.fraction(Q(math.comb(old, i)*math.comb(degree-old, k-i),
                                    math.comb(degree, k)))*a[i]
                       for i in range(max(0, k-(degree-old)), min(old, k)+1)), I(0))
                  for k in range(degree+1)])


def bernstein_product(a, b, dot=False):
    p, q = len(a.lo)-1, len(b.lo)-1
    rows = []
    for k in range(p+q+1):
        terms = []
        for i in range(max(0, k-q), min(p, k)+1):
            v = a[i]*b[k-i]
            if dot:
                v = sum_interval(v, axis=-2)
            weight = I.fraction(Q(math.comb(p, i)*math.comb(q, k-i), math.comb(p+q, k)))
            terms.append(v*weight)
        rows.append(sum(terms, I(0)))
    return stack(rows)


def polar_spectrum(field, M, n):
    shape = field.lo.shape[:-1]+(3, n)
    re, im = I(np.zeros(shape)), I(np.zeros(shape))
    re[..., 0, 0] = field[..., 0]
    re[..., 2, 0] = field[..., 2*M+1]
    for m in range(1, M+1):
        for index in (m, n-m):
            re[..., 0, index] = field[..., m]/2
            re[..., 2, index] = field[..., 2*M+1+m]/2
        im[..., 1, m] = -field[..., M+m]/2
        im[..., 1, n-m] = field[..., M+m]/2
    return re, im


def angular_spectrum(re, im, frequency):
    rr, ii = -im*frequency, re*frequency
    rr[..., 0, :] = rr[..., 0, :]-re[..., 1, :]
    rr[..., 1, :] = rr[..., 1, :]+re[..., 0, :]
    ii[..., 0, :] = ii[..., 0, :]-im[..., 1, :]
    ii[..., 1, :] = ii[..., 1, :]+im[..., 0, :]
    return rr, ii


def angular_margin(values, fft, maximum_frequency, radius):
    coeff_r, coeff_i = fft.transform(values, sign=-1)
    coeff_r, coeff_i = coeff_r/fft.n, coeff_i/fft.n
    freq = np.arange(fft.n)
    freq = 2*np.where(freq <= fft.n//2, freq, freq-fft.n)
    structural_zero = (abs(freq) > maximum_frequency) | (freq % 2 != 0)
    coeff_r[..., structural_zero] = 0
    coeff_i[..., structural_zero] = 0
    deriv_r, _ = fft.transform(-coeff_i*freq, coeff_r*freq)
    abs_coeff = I(coeff_r.magnitude())+I(coeff_i.magnitude())
    second = sum_interval(abs_coeff*(freq*freq), axis=-1)
    lower = I(values.lo)-radius*I(deriv_r.magnitude())-radius*radius*second[..., None]/2
    row, angle = np.unravel_index(np.argmin(lower.lo), lower.lo.shape)
    return dict(lower=float_down(lower.lo[row, angle]),
                bernstein_control=int(row), angle_index=int(angle),
                sample_interval=[float_down(values.lo[row, angle]), float_up(values.hi[row, angle])],
                derivative_abs_upper=float_up(deriv_r.magnitude()[row, angle]),
                second_derivative_upper=float_up(second.hi[row]),
                coefficient_interval_width=float_up(max((coeff_r.hi-coeff_r.lo).max(),
                                                        (coeff_i.hi-coeff_i.lo).max())))


def dump_gzip(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(gzip.compress((json.dumps(obj)+'\n').encode(), mtime=0))


def finite_jets(data):
    M, N = data['M'], data['N']
    law = data['original_metric_identity']['law']
    c = np.array(data['core']['coefficients'])
    q = base.native.outward.FullCoreProbe(c, M, N, law['velocity'], law['length'], law['k0'])
    q.profile = base.fixed.FixedProfile(data['fixed_scalar_profile']['geometry']).profile
    base.fixed.fft.enable_fft(q)
    result = []
    for s, y, yp in zip(data['mesh'], data['states'], data['rhs']):
        y, yp = np.array(y), np.array(yp)
        f = q.frame(s, y)
        eps = 1e-25
        state = q.project(q.frame(s, y.astype(complex)+1j*eps*yp, strict=False)['V']).imag/eps
        da = -f['app']/(f['a']*f['kap'])+f['ap']**2/(f['a']**2*f['kap'])
        db = -f['al']*da/f['be']
        result.append((state+q.project(da[:, None]*f['N']+db[:, None]*f['B'])).tolist())
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--second-jets', type=Path, required=True)
    parser.add_argument('--angles', type=int, default=1024)
    parser.add_argument('--max-intervals', type=int)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    begin = time.time()
    source_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    input_sha = hashlib.sha256(args.input.read_bytes()).hexdigest()
    data = base.fixed.read(args.input)
    M, N = data['M'], data['N']
    if args.angles <= 8*M:
        raise ValueError('The angular transform must resolve the actual Gram frequency 4M')
    if np.finfo(LD).nmant < 63:
        raise RuntimeError('This enclosure requires at least 64-bit extended significands')
    if args.second_jets.exists():
        saved = base.fixed.read(args.second_jets)
        if saved['accepted_input_sha256'] != input_sha:
            raise ValueError('Frozen second jets belong to a different accepted field')
        DDY = saved['second_jets_binary64']
    else:
        DDY = finite_jets(data)
        dump_gzip(args.second_jets, dict(accepted_input_sha256=input_sha,
                  definition='These binary64 numbers are exact rational nodal second jets of the finite C2 field.',
                  second_jets_binary64=DDY))
    X = [I(v) for v in data['mesh']]
    Y, DY, DDY = I(data['states']), I(data['rhs']), I(DDY)
    # All polar components and all Gram polynomials have period pi in phi.
    # A length angles/2 transform in 2*phi gives exactly the same distinct
    # physical samples as angles points on the full 2*pi circle.
    fft = IntervalFFT(args.angles//2)
    freq = np.arange(fft.n)
    freq = 2*np.where(freq <= fft.n//2, freq, freq-fft.n)
    radius = I.fraction(Q(355, 113*args.angles))
    epsilon = I.fraction(Q(1, 1000000))
    rho_spec = I(np.zeros(fft.n))
    rho_spec[0] = 1
    for m, c in enumerate(data['core']['coefficients'], 1):
        value = I(c)*(1-4*m*m)/2
        rho_spec[m] = value
        rho_spec[-m] = value
    rho, _ = fft.transform(rho_spec)
    rho_margin = angular_margin(I(rho.lo[None, :], rho.hi[None, :]), fft, 2*M, radius)
    if rho_margin['lower'] <= 0:
        raise RuntimeError('This interval enclosure did not establish a positive material density')
    knots = data['fixed_scalar_profile']['geometry']['knots']
    sx = np.array([r['s'] for r in knots])
    if sx[0] != 0:
        raise ValueError('This source handles profiles frozen from the core s=0')
    law = data['fixed_scalar_profile']['geometry']['initial_law']
    exact_first = base.fixed.exact_original_jet(law, sx[0])
    knot_jets = [[I(v[k]) for k in ('a', 'ap', 'app')] for v in knots]
    knot_jets[0] = [I.fraction(v) for v in exact_first]
    count = len(X)-1 if args.max_intervals is None else min(len(X)-1, args.max_intervals)
    rows = []
    a_positive = LD(np.inf)
    for j in range(count):
        h = X[j+1]-X[j]
        field = bezier(Y[j], DY[j], DDY[j], Y[j+1], DY[j+1], DDY[j+1], h)
        velocity = 5/h*(field[1:]-field[:-1])
        fr, fi = polar_spectrum(field, M, fft.n)
        vr, vi = polar_spectrum(velocity, M, fft.n)
        ar, ai = angular_spectrum(fr, fi, freq)
        v_values, _ = fft.transform(vr, vi)
        a_values, _ = fft.transform(ar, ai)
        E = bernstein_product(v_values, v_values, dot=True)-1
        F = bernstein_product(v_values, a_values, dot=True)
        G = bernstein_product(a_values, a_values, dot=True)
        old = max(0, min(len(knots)-2, bisect.bisect_right(sx, float(X[j].lo))-1))
        left, right = knots[old], knots[old+1]
        if float(X[j+1].hi) > right['s']+2e-15:
            raise ValueError('A radial interval crosses an unresolved scalar-profile knot')
        H = I(right['s'])-I(left['s'])
        ab = bezier(*knot_jets[old], *knot_jets[old+1], H)
        u0 = (X[j]-I(left['s']))/H
        u1 = (X[j+1]-I(left['s']))/H
        # Endpoint equality is exact for identical binary64 mesh/knot values.
        if data['mesh'][j+1] != right['s']:
            ab = split_bezier(ab, u1)[0]
        if data['mesh'][j] != left['s']:
            ab = split_bezier(ab, u0/u1)[1]
        a_positive = min(a_positive, ab.lo.min())
        a2 = bernstein_product(ab, ab)
        ae = elevate(ab, 9)
        target = a2[..., None]*rho*rho
        middle = ae[..., None]*rho
        polynomials = [('E_plus', epsilon+E), ('E_minus', epsilon-E),
                       ('F_plus', epsilon*middle+F), ('F_minus', epsilon*middle-F),
                       ('G_plus', (1+epsilon)*target-G), ('G_minus', G-(1-epsilon)*target)]
        margins = {name: angular_margin(poly, fft, 4*M, radius) for name, poly in polynomials}
        rows.append(dict(interval=j, s_left=data['mesh'][j], s_right=data['mesh'][j+1],
                         minimum_margin=min(v['lower'] for v in margins.values()), margins=margins))
        if (j+1) % 10 == 0:
            print(json.dumps(dict(event='interval_metric', intervals=j+1,
                                 minimum_margin=min(r['minimum_margin'] for r in rows),
                                 seconds=time.time()-begin)), flush=True)
    worst = min(rows, key=lambda r: r['minimum_margin'])
    passed = worst['minimum_margin'] > 0 and a_positive > 0 and count == len(X)-1
    report = dict(scope=__doc__, passed=passed, epsilon='1/1000000',
                  intervals_checked=count, intervals_total=len(X)-1,
                  all_intervals_checked=count == len(X)-1, M=M, angles=args.angles,
                  distinct_period_pi_samples=fft.n,
                  minimum_margin=worst['minimum_margin'], worst=worst, rows=rows,
                  material_density_lower=rho_margin['lower'], material_density_details=rho_margin,
                  scalar_positive_lower=float_down(a_positive),
                  normalized_metric_bound='max(|E-1|,|F|/(a*rho),|G/(a*a*rho*rho)-1|) < 1/1000000',
                  angular_radius_upper='355/(113*angles)',
                  field_definition='Unique rational quintics through binary64 Y, saved RHS and the frozen second-jets file.',
                  arithmetic='Basic binary extended operations enlarged with numpy.nextafter; exact rational squared endpoint checks for every square-root root construction.',
                  longdouble_mantissa_bits=int(np.finfo(LD).nmant+1),
                  source_sha256=source_sha, input_sha256=input_sha,
                  second_jets_sha256=hashlib.sha256(args.second_jets.read_bytes()).hexdigest(),
                  exact_scalar_profile_sha256=data['fixed_scalar_profile']['exact_coefficient_sha256'],
                  exact_isometry=False, closed_surface=False, continuous_reach=False,
                  seconds=time.time()-begin)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('passed', 'intervals_checked', 'minimum_margin',
                                          'material_density_lower', 'scalar_positive_lower', 'seconds')}), flush=True)


if __name__ == '__main__':
    main()
