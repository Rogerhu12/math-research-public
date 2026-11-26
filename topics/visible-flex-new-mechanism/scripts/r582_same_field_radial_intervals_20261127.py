#!/usr/bin/env python3
"""Continuous radial boxes for the SAME endpoint-defined 97q material field.

This module does not solve an ODE, reconstruct an old run, sample a geometry,
or assert a norm certificate.  A new declared public Actions scope supplies
its already-realized StableField and actual q.  The endpoint numbers are
exact binary64 coefficients of the C2 quintic stated by that source.  Exact
rational Bernstein arithmetic avoids introducing coefficient roundoff and
then amplifying it by the square of a tiny material-cell width.

The continuous object uses the original real formulas, the complete angular
primitive, and the fixed analytic cap height.  Floating evaluation of those
formulas is a separate approximation.  No identification with the infinite
flat ODE kernel, or with a finite FFT position interpolant, is made here.
"""
from bisect import bisect_left, bisect_right
from collections import defaultdict
from fractions import Fraction
import hashlib
import math
from pathlib import Path
import struct
import time


SCHEMA = 'r582-same-common-endpoint-field-continuous-radial-boxes-v1'
SOURCE_BINDINGS = {
    'r582_stable_material_field_20261126.py':
        '070acb1c46a4df055e84722227916a2997f3b6bba9bfaa3cc8c0ba820b8f71e8',
    'r582_paid_resonant_field_20261126.py':
        '1b046b20541fcee05d5c8722dfdd5a509e7018348aab7182bec77c0813a8b395',
    'r582_finite_resonant_radius_only_20261126.py':
        '445e3ac5098cbaaa08f080e1be5d8172e576f72a00b825b2cb000adad83725d2',
    'r582_local_tail_columns_model_20261126.py':
        '13339343918d873cb5ae37b5f2be7e21044ecfc306974fad4948232e5d466260',
    'r611_circular_reference_global_geometry_20261127.py':
        'eb18fb8c5bc5d44ce16aa8cfe3708197e72167e0c6885deb128816e96a902c5f',
}
TAIL_GATES = ((.78, .82), (.82, .84), (.84, .86), (.86, .88))
MODES = (2, 4, 6, 8)


def check_sources():
    for name, expected in SOURCE_BINDINGS.items():
        if hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() != expected:
            raise RuntimeError('same-field radial source changed: ' + name)


def exact(value):
    """An input binary64 number, not its abbreviated decimal display."""
    value = float(value)
    if not math.isfinite(value):
        raise ArithmeticError('nonfinite stored material datum')
    return Fraction.from_float(value)


def fraction_bounds(value):
    """Directed conversion checked against the exact rational itself."""
    rounded = float(value)
    if not math.isfinite(rounded):
        raise ArithmeticError('rational material bound overflows binary64')
    represented = Fraction.from_float(rounded)
    lo = math.nextafter(rounded, -math.inf) if represented > value else rounded
    hi = math.nextafter(rounded, math.inf) if represented < value else rounded
    return lo, hi


def rational_interval(backend, lo, hi=None):
    hi = lo if hi is None else hi
    return backend.I(fraction_bounds(lo)[0], fraction_bounds(hi)[1])


def split_bernstein(coefficients, t):
    """Exact de Casteljau restriction; returns the left and right polynomials."""
    row = tuple(coefficients)
    left, right = [row[0]], [row[-1]]
    for _ in range(len(row) - 1):
        row = tuple((1-t)*a+t*b for a, b in zip(row[:-1], row[1:]))
        left.append(row[0])
        right.append(row[-1])
    return tuple(left), tuple(reversed(right))


def restricted_bernstein(coefficients, left, right):
    if not 0 <= left <= right <= 1:
        raise ValueError('Bernstein restriction left the actual material cell')
    if left == 0 and right == 1:
        return coefficients
    if right == 0:
        return (coefficients[0],) * len(coefficients)
    initial = coefficients if right == 1 else split_bernstein(coefficients, right)[0]
    return initial if left == 0 else split_bernstein(initial, left/right)[1]


def endpoint_bernstein(left, right, width):
    """Six exact quintic Bernstein coefficients from shared 0/1/2 jets."""
    v0, d0, dd0 = left
    v1, d1, dd1 = right
    return (v0, v0+width*d0/5,
            v0+2*width*d0/5+width*width*dd0/20,
            v1-2*width*d1/5+width*width*dd1/20,
            v1-width*d1/5, v1)


def derivative_bernstein(coefficients, width):
    degree = len(coefficients)-1
    return tuple(degree*(b-a)/width for a, b in zip(coefficients[:-1], coefficients[1:]))


class ExactEndpointHermite:
    """A read-only snapshot of the material spline already constructed in Actions.

    This object never calls field.evaluate, field.tail, or an ODE solver.
    Its hash is precisely knots || endpoint_jets in the original Linux
    binary64 array order.  An expected paid mesh hash is mandatory.
    """
    def __init__(self, field, expected_mesh_sha256, backend, deadline=math.inf):
        self.backend, self.deadline = backend, deadline
        self.counts = defaultdict(int)
        self.knots = tuple(float(x) for x in field.material_knots)
        self.endpoints = tuple(tuple(tuple(float(x) for x in jet) for jet in row)
                               for row in field.material_endpoint_jets)
        if (len(self.knots) != len(self.endpoints) or len(self.knots) < 2
                or any(not a < b for a, b in zip(self.knots[:-1], self.knots[1:]))
                or any(len(row) != 2 or any(len(jet) != 3 for jet in row)
                       for row in self.endpoints)):
            raise ValueError('the complete shared-endpoint material data are required')
        all_values = list(self.knots)
        all_values.extend(x for row in self.endpoints for jet in row for x in jet)
        if not all(math.isfinite(x) for x in all_values):
            raise ValueError('nonfinite same-field endpoint data')
        digest = hashlib.sha256()
        for value in all_values:
            digest.update(struct.pack('<d', value))
        self.mesh_sha256 = digest.hexdigest()
        if (self.mesh_sha256 != expected_mesh_sha256
                or self.mesh_sha256 != field.material_mesh_sha256):
            raise ValueError('field realization differs from the exact requested mesh')
        self._cell_cache = {}
        k = len(self.knots)-1
        while k >= 0 and all(x == 0 for jet in self.endpoints[k] for x in jet):
            k -= 1
        self.exact_zero_suffix = self.knots[k+1] if k+1 < len(self.knots) else None

    def check(self):
        if time.monotonic() >= self.deadline:
            raise self.backend.original.ClockCheckpoint('same-field radial interval checkpoint')

    def polynomial_jets(self, index):
        self.check()
        if index not in self._cell_cache:
            width = exact(self.knots[index+1])-exact(self.knots[index])
            fields = []
            for field in range(2):
                left = tuple(exact(x) for x in self.endpoints[index][field])
                right = tuple(exact(x) for x in self.endpoints[index+1][field])
                p0 = endpoint_bernstein(left, right, width)
                p1 = derivative_bernstein(p0, width)
                p2 = derivative_bernstein(p1, width)
                fields.append((p0, p1, p2))
            self._cell_cache[index] = (width, tuple(fields))
            self.counts['new_exact_rational_Hermite_cells'] += 1
        return self._cell_cache[index]

    def cell_jets(self, index, left, right):
        if not self.knots[index] <= left <= right <= self.knots[index+1]:
            raise ValueError('interval must lie in the identified original Hermite cell')
        width, fields = self.polynomial_jets(index)
        t0 = (exact(left)-exact(self.knots[index]))/width
        t1 = (exact(right)-exact(self.knots[index]))/width
        result = []
        for field in fields:
            bounds = []
            for coefficients in field:
                restricted = restricted_bernstein(coefficients, t0, t1)
                bounds.append(rational_interval(self.backend, min(restricted), max(restricted)))
            result.append(tuple(bounds))
        self.counts['new_exact_Hermite_interval_queries'] += 1
        return tuple(result)

    def jets(self, left, right):
        """A,C value/first/second enclosures; supports spans of multiple cells."""
        if not self.knots[0] <= left <= right <= self.knots[-1]:
            raise ValueError('radial interval left the complete material domain')
        first = min(len(self.knots)-2, max(0, bisect_right(self.knots, left)-1))
        last = min(len(self.knots)-2, max(first, bisect_left(self.knots, right)-1))
        output = None
        for index in range(first, last+1):
            new = self.cell_jets(index, max(left, self.knots[index]),
                                 min(right, self.knots[index+1]))
            if output is None:
                output = new
            else:
                output = tuple(tuple(self.backend.I(min(a.lo, b.lo), max(a.hi, b.hi))
                                     for a, b in zip(old_field, new_field))
                               for old_field, new_field in zip(output, new))
        return output

    def receipt(self):
        return {'schema': SCHEMA, 'material_mesh_binary64_sha256': self.mesh_sha256,
            'endpoint_count': len(self.knots), 'whole_material_interval': [self.knots[0], self.knots[-1]],
            'exact_zero_material_suffix_starts_at': self.exact_zero_suffix,
            'shared_binary64_endpoints_interpreted_as_exact_rationals': True,
            'mathematical_quintic_and_its_actual_first_second_derivatives': True,
            'roundoff_free_Bernstein_construction_before_directed_conversion': True,
            'dense_ODE_not_queried_by_this_interface': True,
            'infinite_kernel_C2_error_certified': False,
            'floating_StableField_evaluation_error_certified': False,
            'new_counts': dict(self.counts)}


def add_jets(a, b):
    return tuple(x+y for x, y in zip(a, b))


def scale_jets(a, coefficient):
    return tuple(coefficient*x for x in a)


def multiply_jets(a, b):
    return (a[0]*b[0], a[1]*b[0]+a[0]*b[1],
            a[2]*b[0]+2*a[1]*b[1]+a[0]*b[2])


def inverse_jets(a):
    return (1/a[0], -a[1]/a[0]**2,
            2*a[1]**2/a[0]**3-a[2]/a[0]**2)


def rounded_core_angular_boxes(p, q=.18, offset=.2, backend=None):
    """Elementary whole-circle bounds for the original normalized ellipse core.

    Normal angle phi has rho=offset+p^2*q^2/h^3, where
    h^2=p^2*cos(phi)^2+q^2*sin(phi)^2.  theta_slope=rho/a0.
    The first cos(2*phi) harmonic is separated before bounding the remainder
    of rho; no elliptic-integral sample or numerical inverse is required.
    The proof and its exact real-parameter convention are in the companion note.
    """
    if backend is None:
        check_sources()
        import r611_circular_reference_global_geometry_20261127 as backend
    I = backend.I
    if not all(math.isfinite(v) for v in (p,q,offset)) or not p >= q > 0 or offset < 0:
        raise ValueError('positive ellipse semiaxes p>=q and nonnegative offset required')
    P, Q, D = I(p), I(q), I(offset)
    a0low = D+(P+Q)/2
    a0high = D+backend.sqrt_i((P**2+Q**2)/2)
    a0 = I(a0low.lo, a0high.hi)
    rhomin, rhomax = D+Q**2/P, D+P**2/Q
    rho = I(rhomin.lo, rhomax.hi)
    if p == q:
        zero = I(0)
        return {'a0': a0, 'rho': rho, 'u': zero, 'utheta': zero, 'uthetatheta': zero}
    # x=(p^2-q^2)/q^2 >= 0.  Use an exact rational construction to retain
    # this small positive difference without interval subtraction loss.
    xexact = (exact(p)**2-exact(q)**2)/exact(q)**2
    x = rational_interval(backend, xexact)
    harmonic_primitive = 3*Q*x/8
    remainder_lower_magnitude = 3*Q*x**2/2
    remainder_upper = 15*Q*(1+x)*x**2/8
    # Any bounded f on a quarter interval has centered primitive bounded by
    # oscillation(f)*length/4.  Here length=pi/2 and pi/8 < 11/28.
    primitive_remainder = (remainder_lower_magnitude+remainder_upper)*I(11)/28
    ubound = (harmonic_primitive+primitive_remainder)/a0low
    utheta = a0/rho-1
    delta = rational_interval(backend, exact(p)**2-exact(q)**2)
    rhoprime_bound = 3*P**2*delta/(2*Q**3)
    second_bound = a0high**2*rhoprime_bound/rhomin**3
    return {'a0': a0, 'rho': rho,
            'u': I(-ubound.hi, ubound.hi), 'utheta': utheta,
            'uthetatheta': I(-second_bound.hi, second_bound.hi)}


class EnvelopedSpline:
    """Original beta times degree-five B-spline, including true two jets."""
    def __init__(self, coefficients, backend):
        self.backend = backend
        if len(coefficients) != 8:
            raise ValueError('eight original radial controls required')
        item = (tuple(float(v) for v in backend.KNOTS),
                [backend.I(float(v)) for v in coefficients], 5)
        self.polynomials = [item]
        for _ in range(2):
            item = backend.derivative_spline(*item)
            self.polynomials.append(item)

    def jets(self, s):
        b, I = self.backend, self.backend.I
        if s.hi <= b.C or s.lo >= b.L:
            return I(0), I(0), I(0)
        width = I(b.L)-b.C
        x = (s-b.C)/width
        x = I(max(0., x.lo), min(1., x.hi))
        p = tuple(b.original.spline_interval(x, knots, coefficients, degree)/width**k
                  for k, (knots, coefficients, degree) in enumerate(self.polynomials))
        chi, product, first, second = b.step_jets(s, b.C, b.L)
        beta = (4*product, 4*first*(1-2*chi),
                4*second*(1-2*chi)-8*first**2)
        return multiply_jets(beta, p)


class SameFieldRadialDesign:
    """The original full radial coefficient fields, with no angular fitting.

    frozen_radius is reconstructed from the very same SOURCE_Q and mu as
    RadiusOnlyField.  No height query, ODE query, finite grid, or new seed is
    needed.  This is a new interval observation and must be charged as such.
    """
    def __init__(self, field, q, p, expected_q_sha256, expected_mesh_sha256,
                 deadline=math.inf, backend=None):
        check_sources()
        if backend is None:
            import r611_circular_reference_global_geometry_20261127 as backend
        self.b, self.I = backend, backend.I
        self.q = tuple(float(x) for x in q)
        if len(self.q) != 97 or not all(math.isfinite(x) for x in self.q):
            raise ValueError('the literal actual 97q state is required')
        self.q_sha256 = hashlib.sha256(b''.join(struct.pack('<d', v) for v in self.q)).hexdigest()
        if self.q_sha256 != expected_q_sha256:
            raise ValueError('q is not the requested actual retained state')
        if not math.isfinite(p) or p < .18:
            raise ValueError('invalid fixed nonround core p')
        self.p = float(p)
        self.epsilon = rational_interval(backend, exact(p)-exact(.18))
        self.hermite = ExactEndpointHermite(field, expected_mesh_sha256, backend, deadline)
        if self.hermite.knots[0] != 0. or self.hermite.knots[-1] != backend.L:
            raise ValueError('the original complete material interval is required')
        self.reference_alpha = EnvelopedSpline(backend.Q[64:72], backend)
        self.u_splines = tuple(EnvelopedSpline(self.q[m:32:4], backend) for m in range(4))
        self.v_splines = tuple(EnvelopedSpline(self.q[32+m:64:4], backend) for m in range(4))
        self.reference_mu = self.I(-.040019082162222074)
        self.reference_core_radius = float(backend.original.CIRCLE_RADIUS)
        if exact(self.reference_core_radius) != exact(.38):
            raise ValueError('core subtraction and reference radius identities differ')
        # Real formula 3/(4*r), enclosed before the division.  The ordinary
        # floating quotient is not declared an exact extra model constant.
        self.core_subtraction = rational_interval(backend, Fraction(3)/(4*exact(.38)))
        self.named_interfaces = tuple(sorted(set((0., backend.C, backend.L,
            backend.BACKGROUND_END, backend.CONTROL_LEFT, backend.CONTROL_RIGHT,
            *(v for pair in TAIL_GATES for v in pair)))))

    def background_jets(self, s):
        chi, _, first, second = self.b.step_jets(s, self.b.C, self.b.BACKGROUND_END)
        return (chi, first, second), (1-chi, -first, -second)

    def frozen_radius_jets(self, s):
        b, I = self.b, self.I
        if s.hi <= b.C:
            return I(self.reference_core_radius), I(0), I(0)
        alpha = add_jets(self.reference_alpha.jets(s),
            scale_jets(b.bump_jets(s), self.reference_mu))
        (chi, first, second), _ = self.background_jets(s)
        core, tail = I(self.reference_core_radius), I(b.RC)+b.L-s
        base = ((1-chi)*core+chi*tail,
                first*(tail-core)-chi, second*(tail-core)-2*first)
        e = b.exp_i(alpha[0])
        return (e*base[0], e*(base[1]+base[0]*alpha[1]),
                e*(base[2]+2*base[1]*alpha[1]+base[0]*(alpha[2]+alpha[1]**2)))

    def seed_jets(self, left, right):
        I, s = self.I, self.I(left, right)
        # These are exact identities of the specified real formulas, not a
        # suppression of small sampled numbers or a new endpoint cutoff.
        if right <= self.b.C:
            A, C = self.hermite.jets(left, right)
            if any((v.lo, v.hi) != target for v, target in zip(
                    A+C, ((.5,.5),(0.,0.),(0.,0.),(0.,0.),(0.,0.),(0.,0.)))):
                raise ValueError('actual material core does not have the stated constant jets')
            return (I(0), I(0), I(0)), (I(0), I(0), I(0))
        suffix = self.hermite.exact_zero_suffix
        if suffix is not None and left >= max(suffix, self.b.BACKGROUND_END):
            return (I(0), I(0), I(0)), (I(0), I(0), I(0))
        A, C = self.hermite.jets(left, right)
        radius = self.frozen_radius_jets(s)
        if radius[0].lo <= 0:
            raise ArithmeticError('frozen reference radius needs subdivision')
        inverse = inverse_jets(radius)
        _, complement = self.background_jets(s)
        U = add_jets(scale_jets(multiply_jets(A, inverse), I(1.5)),
                     scale_jets(complement, -self.core_subtraction))
        V = scale_jets(multiply_jets(C, inverse), I(-2))
        return U, V

    def coefficients(self, left, right):
        """Return complete radial 0/1/2 jets of every original sine mode.

        u = complement(s)*u_core(theta) + sum_m u_m(s)*sin(m*theta)
        v = sum_m v_m(s)*sin(m*theta), m = 2,4,6,8.
        The seed and tail columns are combined BEFORE interval bounds, so
        the actual cancellation in 1+sum_j d_j*chi_j is preserved.
        """
        self.hermite.check()
        I, s = self.I, self.I(left, right)
        seed_u, seed_v = self.seed_jets(left, right)
        _, complement = self.background_jets(s)
        gates = []
        for a, b in TAIL_GATES:
            chi, _, first, second = self.b.step_jets(s, a, b)
            gates.append((chi, first, second))
        result = {'modes': MODES, 'core_complement': complement, 'u': [], 'v': []}
        for name, splines, seed, extra_start in (
                ('u', self.u_splines, seed_u, 80), ('v', self.v_splines, seed_v, 88)):
            for mode_index, mode in enumerate(MODES):
                multiplier = (I(1 if mode == 2 else 0), I(0), I(0))
                if mode in (2,4):
                    for gate_index, gate in enumerate(gates):
                        coefficient = self.q[extra_start+2*gate_index+mode_index]
                        multiplier = add_jets(multiplier, scale_jets(gate, I(coefficient)))
                seed_term = scale_jets(multiply_jets(seed, multiplier), self.epsilon)
                result[name].append(add_jets(splines[mode_index].jets(s), seed_term))
            result[name] = tuple(result[name])
        return result

    def angular_box(self, left, right, core_u, core_utheta, core_uthetatheta=None):
        """Complete-circle u/v boxes, conditional only on exact core-angle boxes.

        The core bounds must refer to the SAME rounded ellipse and normalized
        arclength angle, not a sine fit or its finite inverse-root samples.
        The optional theta-theta bound gives every mixed second derivative.
        """
        if not isinstance(core_u, self.I) or not isinstance(core_utheta, self.I):
            raise TypeError('continuous same-core angular interval inputs required')
        if core_uthetatheta is not None and not isinstance(core_uthetatheta, self.I):
            raise TypeError('core second angular derivative must also be an interval')
        radial = self.coefficients(left, right)
        complement, I = radial['core_complement'], self.I
        result = {}
        for name in ('u','v'):
            values = {key: I(0) for key in ('value','s','ss','theta','s_theta')}
            if core_uthetatheta is not None:
                values['theta_theta'] = I(0)
            if name == 'u':
                for key, k in (('value',0),('s',1),('ss',2)):
                    values[key] = complement[k]*core_u
                values['theta'] = complement[0]*core_utheta
                values['s_theta'] = complement[1]*core_utheta
                if core_uthetatheta is not None:
                    values['theta_theta'] = complement[0]*core_uthetatheta
            for mode, jets in zip(MODES, radial[name]):
                for key, k in (('value',0),('s',1),('ss',2)):
                    values[key] = values[key]+jets[k]*I(-1,1)
                values['theta'] = values['theta']+jets[0]*I(-mode,mode)
                values['s_theta'] = values['s_theta']+jets[1]*I(-mode,mode)
                if core_uthetatheta is not None:
                    values['theta_theta'] = values['theta_theta']+jets[0]*I(-mode*mode,mode*mode)
            result[name] = values
        return result

    def initial_partition(self):
        """Literal interface union.  In particular .82 and L-.08 are not merged."""
        return tuple(sorted(set(self.hermite.knots+self.named_interfaces)))

    def receipt(self):
        return {'schema': SCHEMA, 'actual_q_binary64_sha256': self.q_sha256,
            'fixed_p': self.p, 'mesh': self.hermite.receipt(),
            'material_definition': 'exact shared-endpoint C2 quintic, not dense ODE output',
            'arithmetic_definition': 'original real formulas with exact stored binary64 parameters',
            'core_subtraction_is_the_original_real_ratio_3_over_4_r': True,
            'all_original_B_spline_and_sixteen_tail_coordinates_retained': True,
            'tail_seed_multiplier_combined_before_interval_hull': True,
            'complete_circle_bounds_require_same_exact_core_angle_bounds': True,
            'position_uses_exact_continuous_zero_mean_primitive': True,
            'floating_array_roundoff_and_FFT_error_not_inherited_as_zero': True,
            'full_nonround_field_not_identically_circular_on_seed_zero_suffix': True,
            'full_domain_C0_C1_C2_or_reach_certificate_issued': False}
