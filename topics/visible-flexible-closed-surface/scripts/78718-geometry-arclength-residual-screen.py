#!/usr/bin/env python3
"""Floating R105 screen for one actual Cartesian prefix and its own target.

This is NOT a continuous certificate, a metric bound, an ODE solve, or a
repaired geometry.  It samples radial circles, evaluates their finite Fourier
coefficients, and uses a trigonometric-interpolation primitive for R105 J.
The target is the supplied FROZEN a,e,e_s target, with radial zeta=1.
An exact bridge's later lambda/target transfer is deliberately not guessed.
For a common-cut input its own correction is included through its reader.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'

import argparse
import bisect
from dataclasses import dataclass
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
from scipy import fft

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
LD = np.longdouble
CD = np.clongdouble


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value


def resolve(name, anchor):
    p = Path(name)
    for candidate in (p, Path(anchor)/p, Path(anchor)/p.name, HERE.parent/p):
        if candidate.is_file():
            return candidate.resolve()
    raise FileNotFoundError(name)


def ldq(value):
    q = Q(value)
    return LD(q.numerator)/LD(q.denominator)


def midpoint(lo, hi):
    return (np.asarray(lo, dtype=LD)+np.asarray(hi, dtype=LD))/LD(2)


def horner(coefficients, x):
    value = np.zeros(np.shape(coefficients)[1:], dtype=coefficients.dtype)
    for coefficient in coefficients[::-1]:
        value = value*x+coefficient
    return value


@dataclass
class Laurent:
    """Angular coefficients of sum c_j exp(3 i j psi), in long precision."""
    c: np.ndarray
    first: int = 0

    @classmethod
    def scalar(cls, value):
        return cls(np.array([value], dtype=CD), 0)

    def __add__(self, other):
        if not isinstance(other, Laurent):
            other = Laurent.scalar(other)
        left = min(self.first, other.first)
        right = max(self.first+len(self.c), other.first+len(other.c))
        values = np.zeros(right-left, dtype=CD)
        values[self.first-left:self.first-left+len(self.c)] += self.c
        values[other.first-left:other.first-left+len(other.c)] += other.c
        return Laurent(values, left)

    __radd__ = __add__

    def __neg__(self):
        return Laurent(-self.c, self.first)

    def __sub__(self, other):
        return self+(-other)

    def __mul__(self, other):
        if not isinstance(other, Laurent):
            return Laurent(self.c*other, self.first)
        return Laurent(np.convolve(self.c, other.c), self.first+other.first)

    __rmul__ = __mul__

    def angular(self):
        j = np.arange(self.first, self.first+len(self.c), dtype=LD)
        return Laurent(self.c*(CD(3j)*j), self.first)

    def values(self, count):
        # No aliasing of these finite *polynomials*: nonlinear quotients and
        # square roots below still have unrepresented Fourier tails.
        if count <= 2*max(abs(self.first), abs(self.first+len(self.c)-1)):
            raise ValueError('Angular count aliases a finite residual polynomial')
        spectrum = np.zeros(count, dtype=CD)
        indices = np.arange(self.first, self.first+len(self.c))
        spectrum[indices % count] = self.c
        values = fft.ifft(spectrum, norm='forward')
        return values.real, float(np.max(abs(values.imag)))


def expand(values, modes):
    """Same cylindrical coefficient convention as the existing metric backend."""
    fields = [np.zeros(2*modes+1, dtype=CD) for _ in range(3)]
    fields[0][modes] = values[0]
    fields[2][modes] = values[-1]
    for j in range(1, modes+1):
        fields[0][modes+j] = fields[0][modes-j] = values[j]/LD(2)
        fields[1][modes+j] = -CD(1j)*values[modes+j]/LD(2)
        fields[1][modes-j] = CD(1j)*values[modes+j]/LD(2)
        fields[2][modes+j] = fields[2][modes-j] = values[2*modes+j]/LD(2)
    return tuple(Laurent(c, -modes) for c in fields)


def angular_vector(fields):
    r, t, z = fields
    return r.angular()-t, r+t.angular(), z.angular()


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), Laurent.scalar(0))


def exact_shared_jet_power(base, path):
    """Long-precision evaluation of the actual binary shared-jet definition.

    The mean height origin is reset per span.  All derivatives and angular
    derivatives used here are unchanged; its exact saved mean increment is
    retained.  No RHS mean velocity replaces that defined polynomial.
    """
    meta, payload, bindings = base.storage.read_payload(path, verify_arrays=True)
    with np.load(io.BytesIO(gzip.decompress(payload)), allow_pickle=False) as raw:
        x = raw['mesh'].copy()
        jets = np.asarray(raw['jets'], dtype=LD)
        increments = np.asarray(raw['mean_increments'], dtype=LD)
    h = np.diff(np.asarray(x, dtype=LD))[:, None]
    y, d, q2 = jets
    c0 = y[:-1].copy()
    c0[:, -1] = 0
    delta = y[1:]-y[:-1]
    delta[:, -1] = increments
    c1, c2 = h*d[:-1], h*h*q2[:-1]/LD(2)
    e0 = delta-c1-c2
    e1 = h*(d[1:]-d[:-1])-h*h*q2[:-1]
    e2 = h*h*(q2[1:]-q2[:-1])
    power = np.stack((c0, c1, c2, 10*e0-4*e1+e2/2,
                      -15*e0+7*e1-e2, 6*e0-3*e1+e2/2), axis=1)
    return meta, x, power, bindings


class FrozenSlope:
    """Actual frozen analytic a_s, without differentiating a remainder bound."""
    def __init__(self, supplier, meta, target, port):
        cfg = meta['frozen_profile']
        if cfg.get('ramp_law') != 'flat':
            raise ValueError('Only the actual flat-ramp target is implemented')
        if cfg['direction'] not in ('outward', 'inward'):
            raise ValueError('Unknown flat-ramp direction')
        self.sign = 1 if cfg['direction'] == 'outward' else -1
        self.delta, vu, vd, self.eps = (Q(float(cfg[k])) for k in
                                       ('delta', 'vu', 'vd', 'ramp'))
        self.eta = Q(float(cfg.get('ramp_eta', .1)))
        tu = self.delta/(vu*(1-self.eps))
        td = self.delta/(vd*(1-self.eps))
        self.first, self.second = (tu, td) if self.sign == 1 else (td, tu)
        self.period = tu+td
        self.end = self.period*int(cfg['cycles'])
        if self.end != Q(target['exact_prefix_end']):
            raise ValueError('Target prefix endpoint differs from its own profile')
        self.L, self.pt, self.ps = (Q(target['bridge_constants'][k])
                                    for k in ('L', 'pt', 'ps'))
        cut = Q(float(port['cut']['radius']))
        self.sigma = 1 if cut > 1 else -1 if cut < 1 else 0
        if not self.sigma:
            raise ValueError('Frozen bridge has identical endpoint radii')
        self.polynomial = supplier.Target.a_prefix_poly

    def __call__(self, location):
        s = Q(float(location))
        if s >= self.end:
            t = (s-self.end)/self.L
            phi = (3*self.pt-self.L*self.ps)*t*t+(-2*self.pt+self.L*self.ps)*t*t*t
            return LD(self.sigma)*np.sin(ldq(phi))
        cycle = int(s//self.period)
        start = cycle*self.period
        if s < start+self.first:
            phase, duration = 0, self.first
        else:
            phase, duration, start = 1, self.second, start+self.first
        u = (s-start)/duration
        e, eta = self.eps, self.eta
        cuts = [Q(0), e*eta, e*(1-eta), e, 1-e,
                1-e+e*eta, 1-e*eta, Q(1)]
        branch = min(max(bisect.bisect_right(cuts, u)-1, 0), 6)
        c = self.polynomial(self, s, s+1, (phase, duration, start, branch))
        return ldq(c[1]) if len(c) > 1 else LD(0)


def target_point(raw, packet, tau):
    values, uncertainty = {}, {}
    for key in ('a', 'e', 'ep'):
        lo, hi = raw[key+'_lo'][packet], raw[key+'_hi'][packet]
        middle = midpoint(lo, hi)
        radius = (np.asarray(hi, dtype=LD)-np.asarray(lo, dtype=LD))/2
        values[key] = horner(middle, tau)
        uncertainty[key] = float(horner(radius, abs(tau))+
                                 LD(raw.get(key+'_remainder',
                                            np.zeros(len(raw['left'])))[packet]))
    return values, uncertainty


def periodic_primitive(samples):
    """Primitive of the sampled trigonometric interpolant, anchored at psi=0."""
    count = len(samples)
    coeff = fft.fft(samples, norm='forward')
    mean_removed = float(abs(coeff[0]))
    coeff[0] = 0
    indices = np.r_[np.arange(0, (count+1)//2),
                    np.arange(-(count//2), 0)]
    multiplier = CD(3j)*indices.astype(LD)
    primitive = np.zeros(count, dtype=CD)
    mask = indices != 0
    primitive[mask] = coeff[mask]/multiplier[mask]
    if count % 2 == 0:
        # The real Nyquist cosine has a sine primitive vanishing at these nodes.
        primitive[count//2] = 0
    result = fft.ifft(primitive, norm='forward').real
    result -= result[0]
    outer = abs(indices) >= count//3
    return result, mean_removed, float(np.sum(abs(coeff[outer]), dtype=LD))


def symmetric_norm(a, b, c):
    return (abs(a+c)+np.hypot(a-c, 2*b))/2


def summarize(values):
    k = int(np.argmax(abs(values)))
    return dict(min=float(np.min(values)), max=float(np.max(values)),
                max_abs=float(abs(values[k])), max_abs_angular_index=k)


def circle(power, span, s, mesh, modes, target, ap, angular):
    width = LD(mesh[span+1])-LD(mesh[span])
    tau = (LD(s)-LD(mesh[span]))/width
    val = horner(power[span], tau)
    ds = horner(power[span, 1:]*np.arange(1, 6, dtype=LD)[:, None], tau)/width
    fields, radial = expand(val, modes), expand(ds, modes)
    angular_fields, mixed = angular_vector(fields), angular_vector(radial)
    E, F, G = dot(radial, radial), dot(radial, angular_fields), dot(angular_fields, angular_fields)
    Gs = 2*dot(angular_fields, mixed)
    a, e, ep = target['a'], target['e'], target['ep']
    rho = Laurent(np.array([-e/2, 1, -e/2], dtype=CD), -1)
    nu = Laurent(np.array([-CD(1j)*ep/6, 0, CD(1j)*ep/6], dtype=CD), -1)
    rhos = Laurent(np.array([-ep/2, 0, -ep/2], dtype=CD), -1)
    # Subtract finite Fourier coefficients before angular evaluation.
    Dss = E-(Laurent.scalar(1)+a*a*(nu*nu))
    Dsp = F-a*a*(nu*rho)
    N = G-a*a*(rho*rho)
    Ns = Gs-2*a*ap*(rho*rho)-2*a*a*(rho*rhos)
    polys = dict(Dss=Dss, Dsp=Dsp, N=N, Ns=Ns, Np=N.angular(),
                 rho=rho, nu=nu, rhos=rhos, rhop=rho.angular())
    observed, imaginary = {}, 0.
    for key, polynomial in polys.items():
        observed[key], imag = polynomial.values(angular)
        imaginary = max(imaginary, imag)
    rho_v, nu_v = observed['rho'], observed['nu']
    if a <= 0 or np.min(rho_v) <= 0:
        raise ArithmeticError('Sampled frozen target radius/rho is not positive')
    b = nu_v/rho_v
    bp = (observed['rhos']*rho_v-nu_v*observed['rhop'])/(rho_v*rho_v)
    # zeta=1 belongs to this frozen target.  No bridge lambda is silently used.
    epsilon_rr = observed['Dss']-2*b*observed['Dsp']+b*b*observed['N']
    f = (observed['Dsp']-b*observed['N'])/(a*rho_v)
    gamma = observed['N']/(a*a*rho_v*rho_v)
    if np.min(1+gamma) <= 0:
        raise ArithmeticError('Sampled angular metric is not positive')
    q = np.sqrt(1+gamma)
    h = ((observed['Ns']-b*observed['Np'])/(a*a*rho_v*rho_v)
         -2*gamma*(ap/a+bp))
    # rho has exact mean 1.  Use the small square-root increment to avoid
    # subtracting two order-one circumference quantities.
    ell_minus_one = np.mean(rho_v*gamma/(1+q), dtype=LD)
    ell = 1+ell_minus_one
    ell_squared_minus_one = ell_minus_one*(2+ell_minus_one)
    material_mean_gamma = np.mean(rho_v*gamma, dtype=LD)
    mean_h_over_2q = np.mean(rho_v*h/(2*q), dtype=LD)
    integrand = rho_v*(h/(2*q)-(mean_h_over_2q/ell)*q)
    J, drift, high_frequency_l1 = periodic_primitive(integrand)
    aJ = a*J
    f_over_q = f/q
    d = epsilon_rr-f*f/(1+gamma)
    w = f_over_q-aJ
    repaired_rr = epsilon_rr-2*f_over_q*aJ+aJ*aJ
    original_norm = symmetric_norm(epsilon_rr, f, gamma)
    repaired_norm = symmetric_norm(repaired_rr, ell*w, ell_squared_minus_one)
    return dict(
        sample_s=float(s), geometry_span=int(span), target_radius=float(a),
        target_radius_derivative=float(ap), minimum_rho_sampled=float(np.min(rho_v)),
        minimum_q_sampled=float(np.min(q)), target_zeta=1.,
        epsilon_rr=summarize(epsilon_rr), f=summarize(f), gamma=summarize(gamma),
        d=summarize(d), h=summarize(h), aJ=summarize(aJ), w=summarize(w),
        material_mean_gamma=float(material_mean_gamma),
        ell_minus_one=float(ell_minus_one),
        ell_squared_minus_one=float(ell_squared_minus_one),
        original_metric_norm_sampled_max=float(np.max(original_norm)),
        repaired_metric_norm_sampled_max=float(np.max(repaired_norm)),
        unavoidable_d_sampled_max=float(np.max(abs(d))),
        primitive_zero_mode_removed=drift,
        primitive_high_frequency_sampled_l1=high_frequency_l1,
        polynomial_imaginary_roundoff_max=imaginary)


def run(args):
    started = time.monotonic()
    if args.out.exists():
        raise FileExistsError('Use a new report name')
    if args.radial_samples < 2 or args.angular < 16:
        raise ValueError('Insufficient sampling grid')
    backend = module('geometry_r105_metric_polynomial',
                     HERE/'78718-prefix-metric-polynomial-storage-v1.py')
    supplier = module('geometry_r105_metric_supplier',
                      HERE/'78718-prefix-metric-supplier-storage-v1.py')
    meta = json.loads(args.geometry.read_text())
    common = meta.get('representation') == 'exact-common-cut-prefix'
    base_path = args.geometry
    if common:
        adapter = module('geometry_r105_common_reader',
                         HERE/'78718-prefix-common-cut-storage-v1.py')
        adapter.install(backend.base)
        base_path = resolve(meta['base_geometry'], args.geometry.parent)
    geom = backend.base.ExactHermite(args.geometry)
    base_meta = json.loads(base_path.read_text())
    target = json.loads(args.target.read_text())
    if target['geometry_sha256'] != sha(base_path):
        raise ValueError('Target is not bound to this actual defining base')
    if target['frozen_profile'] != base_meta['frozen_profile']:
        raise ValueError('Target profile differs from its own base')
    target_data = resolve(target['data_file'], args.target.parent)
    if sha(target_data) != target['data_sha256']:
        raise ValueError('Changed own target packet')
    with np.load(io.BytesIO(gzip.decompress(target_data.read_bytes())),
                 allow_pickle=False) as data:
        raw = {key: data[key].copy() for key in data.files}
    left, right = raw['left'], raw['right']
    if not (left[0] == geom.x[0] and right[-1] == geom.x[-1] and
            np.array_equal(right[:-1], left[1:]) and np.all(right > left)):
        raise ValueError('Own target does not partition the represented prefix')
    port_path = resolve(base_meta['linear_port'], base_path.parent)
    if sha(port_path) != base_meta['port_sha256']:
        raise ValueError('Changed own frozen port')
    port = json.loads(port_path.read_text())
    slope = FrozenSlope(supplier, base_meta, target, port)
    if common:
        power = midpoint(geom.power.lo, geom.power.hi)
        eval_method = ('Midpoints of the actual common-cut reader coefficient '
                       'enclosures; their uncertainty is not propagated into '
                       'the sampled nonlinear quantities.')
        coefficient_radius = float(np.max(
            (np.asarray(geom.power.hi, dtype=LD)-
             np.asarray(geom.power.lo, dtype=LD))/2))
    else:
        own_meta, mesh, power, bindings = exact_shared_jet_power(backend.base, base_path)
        if own_meta != base_meta or not np.array_equal(mesh, geom.x):
            raise ValueError('Actual stored graph changed during read')
        eval_method = ('Long-precision reconstruction from the same saved binary '
                       'nodal jets and exact mean increments, using the shared '
                       'quintic definition; floating rounding is not certified.')
        coefficient_radius = None
    if args.angular <= 4*geom.M:
        raise ValueError('Angular count must exceed four times geometry modes')
    locations = np.linspace(float(geom.x[0]), float(geom.x[-1]), args.radial_samples)
    if args.all_nodes:
        locations = np.r_[locations, geom.x]
    correction_start = float(geom.x[int(meta['correction_start_index'])]) if common else None
    if common:
        locations = np.r_[locations, correction_start]
    locations = np.unique(locations)
    rows = []
    for s in locations:
        p = min(max(int(np.searchsorted(left, s, side='right')-1), 0), len(left)-1)
        u = (LD(s)-LD(left[p]))/(LD(right[p])-LD(left[p]))
        target_values, uncertainty = target_point(raw, p, u)
        span = min(max(int(np.searchsorted(geom.x, s, side='right')-1), 0), len(geom.x)-2)
        row = circle(power, span, s, geom.x, geom.M, target_values, slope(s), args.angular)
        row['target_packet'] = p
        row['target_packet_point_uncertainty'] = uncertainty
        row['in_common_correction_support'] = bool(common and s >= correction_start)
        rows.append(row)
    maxima = {
        'd_sampled_abs_max': max(r['d']['max_abs'] for r in rows),
        'ell_squared_minus_one_sampled_abs_max': max(abs(r['ell_squared_minus_one']) for r in rows),
        'w_sampled_abs_max': max(r['w']['max_abs'] for r in rows),
        'aJ_sampled_abs_max': max(r['aJ']['max_abs'] for r in rows),
        'original_metric_norm_sampled_max': max(r['original_metric_norm_sampled_max'] for r in rows),
        'repaired_metric_norm_sampled_max': max(r['repaired_metric_norm_sampled_max'] for r in rows)}
    report = dict(
        scope=__doc__, schema='actual-cartesian-r105-floating-screen-v1',
        geometry=str(args.geometry), geometry_sha256=sha(args.geometry),
        defining_base=str(base_path), defining_base_sha256=sha(base_path),
        target=str(args.target), target_sha256=sha(args.target),
        target_data_sha256=sha(target_data), script_sha256=sha(__file__),
        storage_bindings=geom.storage_bindings,
        target_kind='own frozen analytic target; zeta=1; no exact bridge transfer',
        exact_bridge_transfer_applied=False, target_zeta=1.,
        geometry_evaluation=eval_method,
        common_correction_included=common, common_correction_start=correction_start,
        common_reader_power_coefficient_radius_max=coefficient_radius,
        angular_samples_per_threefold_period=args.angular,
        angular_coordinate='psi=2*pi*k/(3*N), material Theta=psi-e(s)*sin(3psi)/3',
        material_means='rho-weighted; rho=1-e*cos(3psi); physical origin Theta(s,0)=0',
        primitive='zero-mean sampled trigonometric interpolant; no Fourier-tail certificate',
        radial_samples=len(rows), all_saved_nodes_included=args.all_nodes,
        longdouble_mantissa_bits=int(np.finfo(LD).nmant),
        finite_polynomial_aliasing_excluded=True, nonlinear_aliasing_excluded=False,
        continuous_certificate=False, metric_error_upper_certified=False,
        repaired_map_constructed=False, complete_closed_surface=False,
        ode_calls=0, solver_calls=0, maxima=maxima, rows=rows,
        derivative_scope=('a_s uses the own frozen analytic profile, not the '
                          'derivative of a uniform radius remainder.  All geometry '
                          'derivatives come from the saved Cartesian polynomial.'),
        limitations=[
            'Only the listed radial points and angular nodes are examined.',
            'Packet midpoint, rounding, quadrature and nonlinear Fourier-tail errors are not certified.',
            'Sampled positivity does not certify immersion or a globally valid arclength map.',
            'No fixed-cap, cuff two-jet, whole-surface, or README completion condition is inferred.',
            'A repaired graph requires its own continuous metric proof and its own exact target transfer.'],
        seconds=time.monotonic()-started)
    payload = json.dumps(report, indent=2, allow_nan=False).encode()+b'\n'
    if args.out.suffix == '.gz':
        payload = gzip.compress(payload, mtime=0)
    if len(payload) >= 5_000_000 or (len(payload) > 1_000_000 and args.out.suffix != '.gz'):
        raise ValueError('Use a gzip output name or fewer samples under repository file limits')
    args.out.write_bytes(payload)
    print(json.dumps(dict(report=str(args.out), radial_samples=len(rows),
                          angular_samples_per_threefold_period=args.angular,
                          **maxima, continuous_certificate=False,
                          seconds=report['seconds']), indent=2, allow_nan=False))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--geometry', type=Path, required=True)
    parser.add_argument('--target', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--radial-samples', type=int, default=42)
    parser.add_argument('--angular', type=int, default=1024)
    parser.add_argument('--all-nodes', action='store_true',
                        help='Add every saved geometry node; still not a continuous bound')
    run(parser.parse_args())
