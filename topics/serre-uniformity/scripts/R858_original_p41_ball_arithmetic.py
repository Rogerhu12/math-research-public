#!/usr/bin/env python3
"""Pure-Python balls in the original degree-14 completion at 41.

There is no CLI and importing this module performs no mathematical work.
Field construction and every arithmetic entry are restricted to the public
Rogerhu12/math-research-public Actions environment.

API, with all precision integers measured by v_B(B)=1, v_B(41)=7:

    K = Field(R854_configuration['field'])
    K.exact_rational(q, absolute_precision)
    K.exact_Bs(coefficients14, absolute_precision)       # B=lambda*b, s^2=-3
    K.exact_bs(coefficients14, absolute_precision)       # original b, s
    K.exact_bzeta(coefficients14_or_R791_encoding, absolute_precision)
    K.from_response(R854_four_response_stage, 'A0'|'A1'|'B0'|'B1'|0..3)
    K.from_data(serialized_ball)

PadicBall has +, -, *, /, integer powers, inverse(), shift(k), clamp(N),
valuation(), valuation_lower_bound(), absolute_precision, relative_precision,
is_zero_ball, certainly_nonzero, conjugate(), automorphism(sigma_b,power=1),
to_data()/serialize().  exact_bzeta accepts the unchanged original R791 pair
of {'numerator':[coefficients], 'denominator':integer} polynomial records.
conjugate fixes B and sends s to -s.  automorphism uses the complete original
sigma(b) in the b,zeta basis and fixes s; its order is the proved original 7.

A zero ball is O(B^N), not a statement of exact zero.  Boolean coercion and
ordinary equality are intentionally unavailable; use is_zero_ball or
same_ball(), and use overlaps() only as a finite-precision comparison.
An unproved nonzero denominator raises NeedPrecision.

The canonical nonzero form is B^v*u+O(B^(v+R)), with R>0 and an integral unit
u.  The unit has 14 coefficients, in B^0..B^6,s*B^0..s*B^6, each reduced
modulo 41^max(0,ceil((R-i)/7)).  Exact scalar inputs can supply any requested
precision; previously computed balls can only lose or preserve precision.
"""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import os
import sys

REPOSITORY = 'Rogerhu12/math-research-public'
P, E, F, DIM = 41, 7, 2, 14
BASIS = 'B^0..B^6,s*B^0..s*B^6; s^2=-3; B=lambda*b'
REPRESENTATION = 'original-p41-normalized-uniformizer-ball-v1'
RESPONSE_LABELS = ('A0', 'A1', 'B0', 'B1')
_AUTHORIZED = False


class NeedPrecision(RuntimeError):
    """A finite ball cannot justify a required nonzero value or precision."""
    def __init__(self, reason, node=None, bounds=None):
        self.reason = str(reason)
        self.node = node
        self.bounds = {} if bounds is None else dict(bounds)
        super().__init__(self.reason)

    def to_data(self):
        return {'type': type(self).__name__, 'reason': self.reason,
                'node': self.node, 'bounds': self.bounds}


def authorize():
    global _AUTHORIZED
    if not _AUTHORIZED:
        if (os.environ.get('GITHUB_ACTIONS') != 'true'
                or os.environ.get('GITHUB_REPOSITORY') != REPOSITORY):
            raise RuntimeError('New p41 arithmetic runs only in this public repository Actions.')
        if hasattr(sys, 'set_int_max_str_digits'):
            sys.set_int_max_str_digits(0)
        _AUTHORIZED = True


def _fraction(value):
    if isinstance(value, Fraction):
        return value
    if isinstance(value, bool) or isinstance(value, float):
        raise TypeError('Exact rational inputs must not be booleans or floating point.')
    if isinstance(value, (int, str)):
        return Fraction(value)
    if isinstance(value, (list, tuple)) and len(value) == 2:
        return Fraction(int(value[0]), int(value[1]))
    if isinstance(value, dict) and set(value) == {'numerator', 'denominator'}:
        return Fraction(int(value['numerator']), int(value['denominator']))
    raise TypeError('Expected an exact rational input.')


def _vp_integer(value):
    value = abs(int(value))
    if not value:
        raise ValueError('The exact valuation of zero is not a finite integer.')
    result = 0
    while value % P == 0:
        value //= P
        result += 1
    return result


def _vp_rational(value):
    assert isinstance(value, Fraction) and value
    return _vp_integer(value.numerator)-_vp_integer(value.denominator)


def _fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


class Field:
    """The original Q_41(B,s), not a new twist or an auxiliary-prime field."""
    def __init__(self, field_description, lambda_value=None, default_precision=56, budget=None):
        authorize()
        self.description = field_description if isinstance(field_description, dict) else None
        if self.description is not None:
            coefficients = self.description['integral_B_minimal_polynomial']
            original_lambda = self.description['lambda']
            if lambda_value is not None:
                assert _fraction(lambda_value) == _fraction(original_lambda)
            lambda_value = original_lambda
            assert self.description.get('original_b_replaced_by_another_twist', False) is False
        else:
            coefficients = field_description
        self.f = tuple(int(x) for x in coefficients)
        assert len(self.f) == 8 and self.f[7] == 1
        assert _vp_integer(self.f[0]) == 1 and all(x % P == 0 for x in self.f[:7])
        assert lambda_value is not None, 'The original B=lambda*b scale must be supplied.'
        self.lambda_value = _fraction(lambda_value)
        assert self.lambda_value > 0 and _vp_rational(self.lambda_value) == 0
        self.default_precision = int(default_precision)
        assert self.default_precision > 0
        self.budget = (lambda: None) if budget is None else budget
        self.field_identity = {'p': P, 'ramification_index': E, 'residue_degree': F,
            'basis': BASIS, 'integral_B_minimal_polynomial': [str(x) for x in self.f],
            'lambda': [str(self.lambda_value.numerator), str(self.lambda_value.denominator)]}
        self.fingerprint = _fingerprint(self.field_identity)
        self._moduli, self._caps, self._f_mod = {}, {}, {}
        self._gamma_cache, self._sigma_cache = {}, {}

    def _N(self, precision):
        return self.default_precision if precision is None else int(precision)

    def _modulus(self, precision):
        assert precision > 0
        exponent = (precision+6)//7
        if exponent not in self._moduli:
            self._moduli[exponent] = P**exponent
        return self._moduli[exponent]

    def _cap(self, precision, degree):
        assert 0 <= degree < E and precision >= 0
        key = (precision, degree)
        if key not in self._caps:
            self._caps[key] = P**max(0, (precision-degree+6)//7)
        return self._caps[key]

    def _canonical(self, coefficients, precision):
        assert len(coefficients) == DIM and precision >= 0
        return tuple(int(x) % self._cap(precision, k % E) for k, x in enumerate(coefficients))

    def _zero_coefficients(self):
        return (0,)*DIM

    def _one_coefficients(self, precision):
        assert precision > 0
        return (1,)+(0,)*(DIM-1)

    def _integral_valuation(self, coefficients, precision):
        result = precision
        for k, raw in enumerate(coefficients):
            value = int(raw) % self._cap(precision, k % E)
            if value:
                result = min(result, E*_vp_integer(value)+(k % E))
        return result

    def _add_integral(self, a, b, precision):
        return self._canonical([x+y for x, y in zip(a, b)], precision)

    def _sub_integral(self, a, b, precision):
        return self._canonical([x-y for x, y in zip(a, b)], precision)

    def _mul_integral(self, a, b, precision):
        """Multiplication in the exact source algebra, then reduction mod B^N."""
        assert precision > 0 and len(a) == len(b) == DIM
        self.budget()
        modulus = self._modulus(precision)
        if modulus not in self._f_mod:
            self._f_mod[modulus] = tuple(x % modulus for x in self.f[:7])
        f = self._f_mod[modulus]

        def product(x, y):
            result = [0]*13
            for i in range(7):
                if x[i]:
                    for j in range(7):
                        if y[j]:
                            result[i+j] += x[i]*y[j]
            return [x % modulus for x in result]

        aa = product(a[:7], b[:7])
        bb = product(a[7:], b[7:])
        cross = product([a[i]+a[i+7] for i in range(7)],
                        [b[i]+b[i+7] for i in range(7)])
        real = [(x-3*y) % modulus for x, y in zip(aa, bb)]
        imag = [(z-x-y) % modulus for x, y, z in zip(aa, bb, cross)]
        for part in (real, imag):
            for degree in range(12, 6, -1):
                leading = part[degree] % modulus
                if leading:
                    for j in range(7):
                        k = degree-7+j
                        part[k] = (part[k]-leading*f[j]) % modulus
        return self._canonical(real[:7]+imag[:7], precision)

    def _mul_pi(self, coefficients, input_precision, output_precision=None):
        target = input_precision+1 if output_precision is None else int(output_precision)
        assert 0 < target <= input_precision+1
        values = self._canonical(coefficients, input_precision)
        result = []
        for off in (0, 7):
            leading = values[off+6]
            result.append(-self.f[0]*leading)
            for i in range(1, 7):
                result.append(values[off+i-1]-self.f[i]*leading)
        return self._canonical(result, target)

    def _div_pi(self, coefficients, precision):
        if precision <= 1:
            raise NeedPrecision('Division by B would exhaust the known integral precision.',
                                bounds={'integral_absolute_precision_B': precision})
        old = self._canonical(coefficients, precision)
        assert old[0] % P == old[7] % P == 0
        target = precision-1
        modulus = self._modulus(target)
        inverse_unit = pow(self.f[0]//P, -1, modulus)
        result = []
        for off in (0, 7):
            last = -(old[off]//P)*inverse_unit
            for i in range(6):
                result.append(old[off+i+1]+self.f[i+1]*last)
            result.append(last)
        result = self._canonical(result, target)
        assert self._mul_pi(result, target, precision) == old
        return result

    def _shift_integral(self, coefficients, input_precision, shift, target):
        assert shift >= 0 and target > 0 and target <= input_precision+shift
        if shift >= target:
            return self._zero_coefficients()
        known = target-shift
        value = self._canonical(coefficients, known)
        for _ in range(shift):
            self.budget()
            value = self._mul_pi(value, known)
            known += 1
        assert known == target
        return value

    def _inverse_unit(self, coefficients, precision):
        """F_41^2 constant inverse, B-nilpotent lift, then certified Newton."""
        assert precision > 0
        value = self._canonical(coefficients, precision)
        assert self._integral_valuation(value, precision) == 0
        a, b = value[0] % P, value[7] % P
        denominator = (a*a+3*b*b) % P
        assert denominator != 0
        constant = [0]*DIM
        inverse = pow(denominator, -1, P)
        constant[0], constant[7] = a*inverse % P, -b*inverse % P
        initial = min(7, precision)
        one = self._one_coefficients(initial)
        # B^7=0 modulo 41.  We may choose arbitrary coefficients above a
        # shorter known B precision, but claim only min(7,precision) digits.
        defect = self._sub_integral(one,
            self._mul_integral(value, constant, initial), initial)
        assert self._integral_valuation(defect, initial) >= 1
        series, power = one, one
        for _ in range(1, 7):
            power = self._mul_integral(power, defect, initial)
            series = self._add_integral(series, power, initial)
        answer = self._mul_integral(constant, series, initial)
        assert self._mul_integral(value, answer, initial) == one
        known = initial
        while known < precision:
            self.budget()
            target = min(2*known, precision)
            # answer is an exact chosen lift of its known residue.  Newton's
            # error identity proves the doubled precision; no ball is relabelled.
            product = self._mul_integral(value, answer, target)
            two = [0]*DIM
            two[0] = 2
            correction = self._sub_integral(two, product, target)
            candidate = self._mul_integral(answer, correction, target)
            assert self._canonical(candidate, known) == answer
            assert self._mul_integral(value, candidate, target) == self._one_coefficients(target)
            answer, known = candidate, target
        return answer

    def _pow_integral(self, coefficients, exponent, precision):
        exponent = int(exponent)
        base = self._canonical(coefficients, precision)
        if exponent < 0:
            base = self._inverse_unit(base, precision)
            exponent = -exponent
        answer = self._one_coefficients(precision)
        while exponent:
            self.budget()
            if exponent & 1:
                answer = self._mul_integral(answer, base, precision)
            exponent >>= 1
            if exponent:
                base = self._mul_integral(base, base, precision)
        return answer

    def _gamma(self, precision):
        if precision not in self._gamma_cache:
            # gamma=B^7/41 is an exact integral unit in the original algebra.
            self._gamma_cache[precision] = self._canonical(
                [-x//P for x in self.f[:7]]+[0]*7, precision)
            assert self._integral_valuation(self._gamma_cache[precision], precision) == 0
        return self._gamma_cache[precision]

    def _unit_rational(self, value, precision):
        assert value and isinstance(value, Fraction)
        a, b = value.numerator, value.denominator
        va, vb = _vp_integer(a), _vp_integer(b)
        modulus = self._modulus(precision)
        coefficient = (a//P**va)*pow(b//P**vb, -1, modulus) % modulus
        return self._canonical([coefficient]+[0]*13, precision), va-vb

    def _normalize(self, valuation, coefficients, relative_precision):
        assert relative_precision > 0
        value = self._canonical(coefficients, relative_precision)
        extra = self._integral_valuation(value, relative_precision)
        absolute = int(valuation)+relative_precision
        if extra >= relative_precision:
            return self.zero(absolute)
        for _ in range(extra):
            self.budget()
            value = self._div_pi(value, relative_precision)
            relative_precision -= 1
        return PadicBall(self, int(valuation)+extra, relative_precision, value)

    def zero(self, absolute_precision=None):
        authorize()
        return PadicBall(self, None, 0, self._zero_coefficients(), self._N(absolute_precision))

    def one(self, absolute_precision=None):
        return self.exact_rational(1, self._N(absolute_precision))

    def uniformizer(self, absolute_precision=None):
        value = [0]*DIM
        value[1] = 1
        return self.exact_Bs(value, self._N(absolute_precision))

    pi = uniformizer

    def _coordinates(self, value):
        if (isinstance(value, (list, tuple)) and len(value) == 2
                and all(isinstance(x, dict) and set(x) == {'numerator', 'denominator'} for x in value)):
            answer = []
            for block in value:
                numerators = block['numerator']
                assert isinstance(numerators, (list, tuple)) and len(numerators) <= 7
                denominator = int(block['denominator'])
                assert denominator > 0
                answer.extend([Fraction(int(x), denominator) for x in numerators])
                answer.extend([Fraction(0)]*(7-len(numerators)))
            return answer
        assert isinstance(value, (list, tuple)) and len(value) == DIM
        return [_fraction(x) for x in value]

    def exact_rational(self, value, absolute_precision=None):
        authorize()
        precision = self._N(absolute_precision)
        value = _fraction(value)
        if not value:
            return self.zero(precision)
        k = _vp_rational(value)
        valuation = E*k
        if valuation >= precision:
            return self.zero(precision)
        relative = precision-valuation
        unit, actual_k = self._unit_rational(value, relative)
        assert actual_k == k
        gamma_power = self._pow_integral(self._gamma(relative), -k, relative)
        unit = self._mul_integral(unit, gamma_power, relative)
        return PadicBall(self, valuation, relative, unit)

    def exact_Bs(self, coefficients, absolute_precision=None):
        """Evaluate exact source coordinates without high-denominator lifting."""
        authorize()
        precision = self._N(absolute_precision)
        coefficients = self._coordinates(coefficients)
        terms = [(k, value, _vp_rational(value)) for k, value in enumerate(coefficients) if value]
        if not terms:
            return self.zero(precision)
        valuation = min(E*vp+(k % E) for k, value, vp in terms)
        if valuation >= precision:
            return self.zero(precision)
        relative = precision-valuation
        answer = self._zero_coefficients()
        for k, value, vp in terms:
            self.budget()
            shift = E*vp+(k % E)-valuation
            if shift >= relative:
                continue
            needed = relative-shift
            unit, actual_vp = self._unit_rational(value, needed)
            assert actual_vp == vp
            unit = self._mul_integral(unit,
                self._pow_integral(self._gamma(needed), -vp, needed), needed)
            if k >= E:
                unit = self._canonical([-3*x for x in unit[7:]]+list(unit[:7]), needed)
            shifted = self._shift_integral(unit, needed, shift, relative)
            answer = self._add_integral(answer, shifted, relative)
        # Distinct B degrees have distinct valuations modulo seven.  At the
        # minimal degree the independent residue basis 1,s forbids cancellation.
        assert self._integral_valuation(answer, relative) == 0
        return PadicBall(self, valuation, relative, answer)

    def exact_bs(self, coefficients, absolute_precision=None):
        """Original b,s coordinates; apply B=lambda*b exactly once."""
        values = self._coordinates(coefficients)
        return self.exact_Bs([value/self.lambda_value**(k % E)
                             for k, value in enumerate(values)], absolute_precision)

    def exact_bzeta(self, coefficients, absolute_precision=None):
        """Original b,zeta coordinates, with zeta=(s-1)/2 exactly once."""
        values = self._coordinates(coefficients)
        first = [(values[i]-values[i+7]/2)/self.lambda_value**i for i in range(7)]
        second = [(values[i+7]/2)/self.lambda_value**i for i in range(7)]
        return self.exact_Bs(first+second, absolute_precision)

    def from_integral(self, coefficients, absolute_precision):
        authorize()
        precision = int(absolute_precision)
        if precision <= 0:
            return self.zero(precision)
        assert len(coefficients) == DIM
        return self._normalize(0, tuple(int(x) for x in coefficients), precision)

    def from_response(self, response, index):
        """Read a certified R854 ball; never apply its old integer scale again."""
        authorize()
        assert response['actual_original_p41_four_response_balls_certified'] is True
        assert response['expanded_exact_L_coordinates_accepted'] is False
        assert response['A1_exact_zero_proved'] is False
        assert response['original_CM_scale_applied_again'] is False
        assert response['B_response_free1186_constant_preserved'] is True
        assert tuple(response['labels']) == RESPONSE_LABELS
        if isinstance(index, str):
            assert index in RESPONSE_LABELS
            index = RESPONSE_LABELS.index(index)
        assert isinstance(index, int) and not isinstance(index, bool) and 0 <= index < 4
        if 'configuration' in response:
            original = response['configuration']['field']
            assert tuple(int(x) for x in original['integral_B_minimal_polynomial']) == self.f
            assert _fraction(original['lambda']) == self.lambda_value
        data = response['numerators']
        assert data['shape'] == [4, 1] and data['p'] == P and data['ramification_index'] == E
        assert data['basis'] == 'B^0..B^6,s*B^0..s*B^6; s^2=-3'
        assert data['uniformizer'] == 'original B=lambda*b'
        precision = int(data['absolute_B_precision'])
        coefficients = data['coefficients']
        assert len(coefficients) == DIM
        values = []
        for k, rows in enumerate(coefficients):
            assert len(rows) == 4 and all(len(row) == 1 for row in rows)
            value = int(rows[index][0])
            assert 0 <= value < self._cap(precision, k % E)
            values.append(value)
        denominator_B = int(response['common_denominator_B_power'])
        denominator_41 = int(response['common_denominator_p41_power'])
        assert denominator_B >= 0 and denominator_41 >= 0
        target = int(response['absolute_B_precision'])
        assert target <= precision-denominator_B-E*denominator_41
        ball = self.from_integral(values, precision).shift(-denominator_B)
        ball = ball*Fraction(1, P**denominator_41)
        return ball.clamp(target)

    def from_data(self, data):
        authorize()
        assert data['representation'] == REPRESENTATION and data['field_sha256'] == self.fingerprint
        assert data['p'] == P and data['ramification_index'] == E and data['residue_degree'] == F
        assert data['basis'] == BASIS and data['uniformizer'] == 'original B=lambda*b'
        absolute = int(data['absolute_precision_B'])
        relative = int(data['relative_precision_B'])
        coefficients = tuple(int(x) for x in data['unit_coefficients'])
        assert len(coefficients) == DIM
        assert isinstance(data['zero_ball'], bool)
        if data['zero_ball']:
            assert data['valuation_B'] is None and relative == 0 and not any(coefficients)
            return self.zero(absolute)
        valuation = int(data['valuation_B'])
        assert relative > 0 and valuation+relative == absolute
        assert coefficients == self._canonical(coefficients, relative)
        return PadicBall(self, valuation, relative, coefficients)

    def _sigma_unit(self, sigma_b, relative_precision):
        coefficients = self._coordinates(sigma_b)
        source = tuple((x.numerator, x.denominator) for x in coefficients)
        key = (source, relative_precision)
        if key in self._sigma_cache:
            return self._sigma_cache[key]
        # sigma(B) must be known to R+1 to obtain its unit eta=sigma(B)/B
        # to R.  Its original exact source permits this additional input digit.
        image = self.exact_bzeta(coefficients, relative_precision+1)*self.lambda_value
        if image.is_zero_ball:
            raise NeedPrecision('The exact sigma(B) image did not resolve at its required precision.',
                                bounds={'requested_absolute_precision_B': relative_precision+1})
        assert image.valuation() == 1, 'Original sigma must preserve the unique p41 valuation.'
        eta = image.shift(-1)
        assert eta.valuation() == 0 and eta.relative_precision == relative_precision
        image_integral = self._shift_integral(eta.unit_coefficients, relative_precision,
                                              1, relative_precision)
        self._sigma_cache[key] = (eta.unit_coefficients, image_integral)
        return self._sigma_cache[key]

    def automorphism(self, ball, sigma_b, power=1):
        authorize()
        ball._same_field(self)
        assert isinstance(power, int) and not isinstance(power, bool)
        power %= 7
        if ball.is_zero_ball or power == 0:
            return self.from_data(ball.to_data())
        result = ball
        for _ in range(power):
            self.budget()
            relative = result.relative_precision
            eta, image = self._sigma_unit(sigma_b, relative)
            parts = []
            for off in (0, 7):
                value = self._zero_coefficients()
                for i in range(6, -1, -1):
                    value = self._mul_integral(value, image, relative)
                    addition = [0]*DIM
                    addition[0] = result.unit_coefficients[off+i]
                    value = self._add_integral(value, addition, relative)
                parts.append(value)
            second_times_s = self._canonical([-3*x for x in parts[1][7:]]+list(parts[1][:7]), relative)
            unit_image = self._add_integral(parts[0], second_times_s, relative)
            factor = self._pow_integral(eta, result.valuation(), relative)
            unit_image = self._mul_integral(unit_image, factor, relative)
            assert self._integral_valuation(unit_image, relative) == 0
            result = PadicBall(self, result.valuation(), relative, unit_image)
        assert result.absolute_precision == ball.absolute_precision
        return result

    def conjugate(self, ball):
        ball._same_field(self)
        return ball.conjugate()


class PadicBall:
    """A ball, never an unqualified exact algebraic number or zero test."""
    __slots__ = ('field', '_v', '_R', '_u', '_N')

    def __init__(self, field, valuation, relative_precision, unit_coefficients, zero_absolute_precision=None):
        authorize()
        assert isinstance(field, Field)
        self.field = field
        self._u = tuple(int(x) for x in unit_coefficients)
        assert len(self._u) == DIM
        if valuation is None:
            assert int(relative_precision) == 0 and zero_absolute_precision is not None and not any(self._u)
            self._v, self._R, self._N = None, 0, int(zero_absolute_precision)
        else:
            self._v, self._R = int(valuation), int(relative_precision)
            assert self._R > 0
            assert self._u == field._canonical(self._u, self._R)
            assert field._integral_valuation(self._u, self._R) == 0
            self._N = self._v+self._R

    @property
    def absolute_precision(self):
        return self._N

    @property
    def relative_precision(self):
        return self._R

    @property
    def absolute_precision_B(self):
        return self._N

    @property
    def relative_precision_B(self):
        return self._R

    @property
    def unit_coefficients(self):
        return self._u

    @property
    def is_zero_ball(self):
        return self._v is None

    @property
    def certainly_nonzero(self):
        return self._v is not None

    def valuation(self):
        if self.is_zero_ball:
            raise NeedPrecision('A zero ball gives only a valuation lower bound, not an exact zero.',
                                bounds={'valuation_lower_bound_B': self._N,
                                        'absolute_precision_B': self._N})
        return self._v

    def valuation_lower_bound(self):
        return self._N if self.is_zero_ball else self._v

    def _same_field(self, other):
        other_field = other.field if isinstance(other, PadicBall) else other
        assert isinstance(other_field, Field) and self.field.fingerprint == other_field.fingerprint

    def clamp(self, absolute_precision):
        target = int(absolute_precision)
        if target > self._N:
            raise NeedPrecision('A computed ball cannot be relabelled at higher absolute precision.',
                                bounds={'available_absolute_precision_B': self._N,
                                        'requested_absolute_precision_B': target})
        if self.is_zero_ball or self._v >= target:
            return self.field.zero(target)
        return PadicBall(self.field, self._v, target-self._v,
                         self.field._canonical(self._u, target-self._v))

    def shift(self, power):
        """Multiply by the exact original uniformizer B^power."""
        assert isinstance(power, int) and not isinstance(power, bool)
        if self.is_zero_ball:
            return self.field.zero(self._N+power)
        return PadicBall(self.field, self._v+power, self._R, self._u)

    def __bool__(self):
        raise TypeError('A ball is not an exact zero predicate; use is_zero_ball or certainly_nonzero.')

    def __eq__(self, other):
        raise TypeError('Ball equality is not exact field equality; use same_ball() or overlaps().')

    def same_ball(self, other):
        if not isinstance(other, PadicBall) or self.field.fingerprint != other.field.fingerprint:
            return False
        return (self._v, self._R, self._N, self._u) == (other._v, other._R, other._N, other._u)

    def overlaps(self, other):
        return (self-other).is_zero_ball

    def __neg__(self):
        if self.is_zero_ball:
            return self.field.zero(self._N)
        return PadicBall(self.field, self._v, self._R,
                         self.field._canonical([-x for x in self._u], self._R))

    def __add__(self, other):
        if not isinstance(other, PadicBall):
            other = self.field.exact_rational(other, self._N)
        self._same_field(other)
        absolute = min(self._N, other._N)
        valuation = min(self.valuation_lower_bound(), other.valuation_lower_bound())
        if valuation >= absolute:
            return self.field.zero(absolute)
        relative = absolute-valuation
        parts = []
        for value in (self, other):
            if value.is_zero_ball or value._v >= absolute:
                parts.append(self.field._zero_coefficients())
            else:
                parts.append(self.field._shift_integral(value._u, value._R,
                                                       value._v-valuation, relative))
        return self.field._normalize(valuation,
            self.field._add_integral(parts[0], parts[1], relative), relative)

    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, PadicBall):
            return self+(-other)
        return self+self.field.exact_rational(-_fraction(other), self._N)

    def __rsub__(self, other):
        return (-self)+other

    def __mul__(self, other):
        if not isinstance(other, PadicBall):
            rational = _fraction(other)
            if not rational:
                # This is the exact known scalar zero, so any finite requested
                # absolute precision is valid; preserve the existing request.
                return self.field.zero(self._N)
            valuation = E*_vp_rational(rational)
            if self.is_zero_ball:
                return self.field.zero(self._N+valuation)
            other = self.field.exact_rational(rational, valuation+self._R)
        self._same_field(other)
        if self.is_zero_ball or other.is_zero_ball:
            return self.field.zero(self.valuation_lower_bound()+other.valuation_lower_bound())
        relative = min(self._R, other._R)
        unit = self.field._mul_integral(self._u, other._u, relative)
        return PadicBall(self.field, self._v+other._v, relative, unit)

    __rmul__ = __mul__

    def inverse(self):
        if self.is_zero_ball:
            raise NeedPrecision('The denominator ball contains zero; its inverse is not certified.',
                                bounds={'denominator_absolute_precision_B': self._N})
        inverse = self.field._inverse_unit(self._u, self._R)
        return PadicBall(self.field, -self._v, self._R, inverse)

    def __truediv__(self, other):
        if not isinstance(other, PadicBall):
            rational = _fraction(other)
            if not rational:
                raise NeedPrecision('The exact scalar denominator is zero.', bounds={'exact_zero_denominator': True})
            return self*(1/rational)
        return self*other.inverse()

    def __rtruediv__(self, other):
        rational = _fraction(other)
        return self.inverse()*rational

    def __pow__(self, exponent, modulo=None):
        assert modulo is None and isinstance(exponent, int) and not isinstance(exponent, bool)
        if exponent == 0:
            return self.field.one(max(1, self._R if not self.is_zero_ball else self._N))
        if self.is_zero_ball:
            if exponent < 0:
                return self.inverse()**(-exponent)
            return self.field.zero(exponent*self._N)
        unit = self.field._pow_integral(self._u, exponent, self._R)
        return PadicBall(self.field, exponent*self._v, self._R, unit)

    def conjugate(self):
        """Only the original involution B fixed, s sent to -s."""
        if self.is_zero_ball:
            return self.field.zero(self._N)
        value = self.field._canonical(list(self._u[:7])+[-x for x in self._u[7:]], self._R)
        return PadicBall(self.field, self._v, self._R, value)

    def automorphism(self, sigma_b, power=1):
        return self.field.automorphism(self, sigma_b, power)

    def to_data(self):
        return {'representation': REPRESENTATION, 'field_sha256': self.field.fingerprint,
            'p': P, 'ramification_index': E, 'residue_degree': F,
            'basis': BASIS, 'uniformizer': 'original B=lambda*b',
            'zero_ball': self.is_zero_ball, 'valuation_B': self._v,
            'relative_precision_B': self._R, 'absolute_precision_B': self._N,
            'unit_coefficients': [str(x) for x in self._u],
            'zero_ball_is_not_an_exact_zero_assertion': True,
            'precision_is_absolute_in_original_uniformizer_units': True}

    serialize = to_data

    def __repr__(self):
        if self.is_zero_ball:
            return 'PadicBall(O(B^'+str(self._N)+'))'
        return 'PadicBall(vB='+str(self._v)+', relative='+str(self._R)+', absolute='+str(self._N)+')'
