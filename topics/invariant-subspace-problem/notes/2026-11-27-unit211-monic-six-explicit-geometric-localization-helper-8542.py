#!/usr/bin/env python3
"""R150 exact monic T-degree-six arithmetic and explicit geometric localization.

This helper contains no norm inverse, Gaussian pivot inverse, or implicit
localization.  The caller supplies a rational coefficient ring R whose values
have T degree zero (its ambient mpoly context may include T).  Every external
coefficient is audited by coefficient_audit.
The six lower coefficients specify F(T)=T**6+sum(c[i]*T**i,i=0..5).
For the original moment relation the paid leading coefficient is
4*ell**2*(1-Q).  The caller must divide by it using its paid weight-unit audit.

A localized value is num/E**pole, where E is the product of named original
geometric units.  Only their named inverses and separately audited parameter
units are available.  Cross-product equality is a sufficient exact equality
certificate; failure of this certificate is NOT a proof of inequality in a
possibly nonreduced localization.  No claim that E is a non-zero-divisor occurs.

The module performs no original-input computation when imported.  Each
multiplication in the quotient checks the complete unreduced polynomial identity
raw = remainder + quotient*F, coefficient by coefficient over R.
"""
from functools import wraps

def cooperate_parameter_ring(R):
    """Let R scalar arithmetic defer to the two higher algebra classes.

    Call once if the caller's R unconditionally coerces its right operand.
    A caller's further quadratic-extension class may use
    _isp_quotient_level=3 to obtain the same cooperation.
    """
    if getattr(R, "_isp_cooperation_installed", False):
        return
    for name in ("__add__", "__sub__", "__mul__", "__truediv__", "__eq__"):
        original = getattr(R, name, None)
        if original is None:
            continue
        def wrap(fn):
            @wraps(fn)
            def operation(self, other):
                if getattr(other, "_isp_quotient_level", 0) > 0:
                    return NotImplemented
                return fn(self, other)
            return operation
        setattr(R, name, wrap(original))
    R._isp_cooperation_installed = True

def make_six_quotient(R, lower_six, coefficient_audit, parameter_unit_audit):
    """Return an algebra object with K6, Localization, T, and checked operations.

    coefficient_audit(R-value) must verify that the denominator contains only
    the caller's paid weight factors and that no T variable is in R.
    parameter_unit_audit(name,R-value) must verify a SPECIFIED original
    parameter unit; it must raise on an unregistered/unproved unit.
    Audits concern the actual caller's domain, not the entire parameter spectrum.
    """
    assert callable(coefficient_audit) and callable(parameter_unit_audit)
    stats = dict(multiplications=0, reductions=0,
                 polynomial_identity_coefficients=0,
                 external_coefficient_audits=0,
                 named_parameter_inverses=0, geometric_inverse_checks=0,
                 rebase_checks=0)
    zero, one = R(0), R(1)
    def external_coefficient(c):
        c = R(c)
        coefficient_audit(c)
        stats["external_coefficient_audits"] += 1
        return c
    lower = tuple(external_coefficient(c) for c in lower_six)
    assert len(lower) == 6
    full_relation = lower + (one,)

    def reduce_polynomial(raw):
        raw = list(raw)
        if not raw:
            raw = [zero]
        while len(raw) > 1 and raw[-1] == zero:
            raw.pop()
        rem = raw[:]
        quotient = [zero] * max(0, len(raw)-6)
        for j in range(len(rem)-1, 5, -1):
            lead = rem[j]
            if lead == zero:
                continue
            quotient[j-6] = lead
            rem[j] = zero
            for i in range(6):
                if lower[i] != zero:
                    rem[j-6+i] = rem[j-6+i] - lead*lower[i]
        remainder = (rem[:6] + [zero]*6)[:6]
        # Full original difference, not evaluation at sample points.
        check = raw[:] + [zero]*max(0, 6-len(raw))
        for i in range(6):
            check[i] = check[i] - remainder[i]
        for j, lead in enumerate(quotient):
            if lead == zero:
                continue
            for i, cc in enumerate(full_relation):
                if cc != zero:
                    check[j+i] = check[j+i] - lead*cc
        assert all(c == zero for c in check), "failed full monic reduction"
        stats["reductions"] += 1
        stats["polynomial_identity_coefficients"] += len(check)
        return tuple(remainder)

    class K6:
        _isp_quotient_level = 1
        __slots__ = ("coefficients",)
        def __init__(self, value=0):
            if isinstance(value, K6):
                self.coefficients = value.coefficients
                return
            if isinstance(value, (list, tuple)):
                assert len(value) <= 6
                c = [external_coefficient(v) for v in value]
                self.coefficients = tuple(c+[zero]*(6-len(c)))
            else:
                self.coefficients = (external_coefficient(value),)+(zero,)*5
        @classmethod
        def _internal(cls, coefficients):
            assert len(coefficients) == 6
            obj = object.__new__(cls)
            obj.coefficients = tuple(coefficients)
            return obj
        def __bool__(self):
            return any(c != zero for c in self.coefficients)
        def __add__(self, other):
            if getattr(other, "_isp_quotient_level", 0) > 1:
                return NotImplemented
            other = K6(other)
            return K6._internal(tuple(a+b for a,b in
                                      zip(self.coefficients,other.coefficients)))
        __radd__ = __add__
        def __neg__(self):
            return K6._internal(tuple(-a for a in self.coefficients))
        def __sub__(self, other):
            if getattr(other, "_isp_quotient_level", 0) > 1:
                return NotImplemented
            return self + (-K6(other))
        def __rsub__(self, other):
            return K6(other) + (-self)
        def __mul__(self, other):
            if getattr(other, "_isp_quotient_level", 0) > 1:
                return NotImplemented
            other = K6(other)
            stats["multiplications"] += 1
            raw = [zero]*11
            for i,a in enumerate(self.coefficients):
                if a == zero:
                    continue
                for j,b in enumerate(other.coefficients):
                    if b != zero:
                        raw[i+j] = raw[i+j] + a*b
            return K6._internal(reduce_polynomial(raw))
        __rmul__ = __mul__
        def __truediv__(self, other):
            # Only literal rational constants are implicitly inverted.
            if isinstance(other, int) and other != 0:
                inv = one/R(other)
                return K6._internal(tuple(c*inv for c in self.coefficients))
            raise TypeError("Use a named paid parameter or geometric inverse")
        def __pow__(self, n):
            if not isinstance(n, int) or n < 0:
                raise TypeError("K6 allows only nonnegative integer powers")
            ans, cur = K6(1), self
            while n:
                if n & 1:
                    ans = ans*cur
                n >>= 1
                if n:
                    cur = cur*cur
            return ans
        def __eq__(self, other):
            if getattr(other, "_isp_quotient_level", 0) > 1:
                return NotImplemented
            other = K6(other)
            return all(a == b for a,b in
                       zip(self.coefficients,other.coefficients))

    def from_polynomial(coefficients):
        return K6._internal(reduce_polynomial(
            [external_coefficient(c) for c in coefficients]))

    def inverse_parameter(name, value):
        assert isinstance(name, str) and name
        value = external_coefficient(value)
        parameter_unit_audit(name, value)
        assert value != zero, "the specified parameter unit is identically zero"
        inv = external_coefficient(one/value)
        assert value*inv == one, "parameter inverse multiplication failed"
        stats["named_parameter_inverses"] += 1
        return K6(inv)

    class Localization:
        """Explicit localization by a fixed finite list of original units."""
        def __init__(self, named_factors):
            self.factors = {}
            self.provenance = {}
            for name, factor, provenance in named_factors:
                assert isinstance(name,str) and name and name not in self.factors
                assert isinstance(provenance,str) and provenance
                self.factors[name] = K6(factor)
                self.provenance[name] = provenance
            assert self.factors
            ep = K6(1)
            for factor in self.factors.values():
                ep = ep*factor
            self.E = ep
            self._powers = [K6(1), ep]
            self._inverse_cache = {}
            owner = self
            class Fraction:
                _isp_quotient_level = 2
                __slots__ = ("numerator", "pole_order")
                def __init__(self, numerator=0, pole_order=0):
                    if isinstance(numerator, Fraction):
                        assert pole_order == 0
                        self.numerator = numerator.numerator
                        self.pole_order = numerator.pole_order
                        return
                    assert isinstance(pole_order,int) and pole_order >= 0
                    self.numerator = K6(numerator)
                    self.pole_order = 0 if self.numerator == 0 else pole_order
                def has_zero_numerator(self):
                    return self.numerator == 0
                def __bool__(self):
                    raise TypeError("Use has_zero_numerator() or exact "
                                    "cross-product equality; no unit test exists")
                def __add__(self, other):
                    if getattr(other, "_isp_quotient_level", 0) > 2:
                        return NotImplemented
                    other = Fraction(other)
                    k = max(self.pole_order,other.pole_order)
                    a = self.numerator*owner.power(k-self.pole_order)
                    b = other.numerator*owner.power(k-other.pole_order)
                    return Fraction(a+b,k)
                __radd__ = __add__
                def __neg__(self):
                    return Fraction(-self.numerator,self.pole_order)
                def __sub__(self, other):
                    if getattr(other, "_isp_quotient_level", 0) > 2:
                        return NotImplemented
                    return self + (-Fraction(other))
                def __rsub__(self, other):
                    return Fraction(other) + (-self)
                def __mul__(self, other):
                    if getattr(other, "_isp_quotient_level", 0) > 2:
                        return NotImplemented
                    other = Fraction(other)
                    return Fraction(self.numerator*other.numerator,
                                    self.pole_order+other.pole_order)
                __rmul__ = __mul__
                def __truediv__(self, other):
                    if isinstance(other,int) and other != 0:
                        return Fraction(self.numerator/other,self.pole_order)
                    raise TypeError("Use named original-unit inverses")
                def __pow__(self,n):
                    if not isinstance(n,int) or n < 0:
                        raise TypeError("Only nonnegative integer powers")
                    return Fraction(self.numerator**n,self.pole_order*n)
                def equal_by_cross_product(self,other):
                    other = Fraction(other)
                    k = max(self.pole_order,other.pole_order)
                    return (self.numerator*owner.power(k-self.pole_order)
                            == other.numerator*owner.power(k-other.pole_order))
                def __eq__(self,other):
                    if getattr(other, "_isp_quotient_level", 0) > 2:
                        return NotImplemented
                    return self.equal_by_cross_product(other)
            self.Fraction = Fraction
        def power(self,n):
            assert isinstance(n,int) and n >= 0
            while len(self._powers) <= n:
                self._powers.append(self._powers[-1]*self.E)
            return self._powers[n]
        def inverse_atom(self,name):
            assert name in self.factors, "unregistered geometric inverse"
            if name not in self._inverse_cache:
                complement = K6(1)
                for other,factor in self.factors.items():
                    if other != name:
                        complement = complement*factor
                assert self.factors[name]*complement == self.E
                stats["geometric_inverse_checks"] += 1
                self._inverse_cache[name] = self.Fraction(complement,1)
            return self._inverse_cache[name]
        def inverse_parameter(self,name,value):
            return self.Fraction(inverse_parameter(name,value))
        def rebase_checked(self,value,numerator,pole_order=0):
            value = self.Fraction(value)
            candidate = self.Fraction(numerator,pole_order)
            assert value.equal_by_cross_product(candidate), \
                "unproved explicit denominator cancellation"
            stats["rebase_checks"] += 1
            return candidate

    class Algebra:
        pass
    out = Algebra()
    out.K6 = K6
    out.Localization = Localization
    out.T = K6([zero,one])
    out.lower_six = lower
    out.from_polynomial = from_polynomial
    out.inverse_parameter = inverse_parameter
    out.statistics = stats
    return out


def make_six_from_mpoly(R, ctx, relation, idxT, coefficient_audit,
                        parameter_unit_audit, leading_unit_name):
    """Adapter for an ambient fmpq_mpoly context containing the T variable.

    relation is the ORIGINAL polynomial F6, not assumed monic.  Its T-leading
    coefficient must be the specified paid parameter unit.  This adapter checks
    the full coefficient extraction and the monic normalization, and provides
    out.from_mpoly(p) for further original polynomial numerators.
    """
    gens = ctx.gens()
    assert isinstance(idxT,int) and 0 <= idxT < len(gens)
    def split(pp):
        terms = pp.to_dict()
        degree = max((int(m[idxT]) for m in terms), default=0)
        parts = [{} for _ in range(degree+1)]
        for m,c in terms.items():
            power = int(m[idxT])
            key = tuple(0 if j == idxT else int(v) for j,v in enumerate(m))
            parts[power][key] = c
        coefficients = [ctx.from_dict(d) for d in parts]
        back = ctx.constant(0)
        for j,c in enumerate(coefficients):
            back += c*gens[idxT]**j
        assert back == pp, "T coefficient extraction did not multiply back"
        return coefficients
    coefficients = split(relation)
    assert len(coefficients) == 7 and coefficients[6]
    lead = R(coefficients[6])
    coefficient_audit(lead)
    parameter_unit_audit(leading_unit_name,lead)
    inverse_lead = R(1)/lead
    coefficient_audit(inverse_lead)
    assert lead*inverse_lead == R(1)
    lower = [R(c)*inverse_lead for c in coefficients[:6]]
    for c,normalized in zip(coefficients[:6],lower):
        assert lead*normalized == R(c)
    out = make_six_quotient(R,lower,coefficient_audit,parameter_unit_audit)
    def from_mpoly(pp):
        return out.from_polynomial(split(pp))
    out.from_mpoly = from_mpoly
    out.idxT = idxT
    out.original_leading_coefficient = lead
    out.original_relation_verified = True
    assert from_mpoly(relation) == 0
    return out
