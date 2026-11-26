#!/usr/bin/env sage-python
"""R986: native residue fields from the SAME original quadratic constants.

This standalone successor is not imported or bound by Artinian v8.  It keeps
the specified Q=k[t]/pi, k=F_(r^2), and the actual original omega.  A norm
polynomial for t or t+omega gives an absolute native field without factoring
pi over that field.  All coordinate-space returns of R974 are retained.

Only the original quadratic base is specialized.  Higher native residue
towers keep the R974 constructor through make_original_quadratic_selector.
No mathematical execution or original geometry PASS is claimed by this file.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public research Actions.")

from sage.all import GF, PolynomialRing
from original_ys_closed_point_tools import (
    ActualFiniteFieldQuotient, native_absolute_degree)
from original_ys_divisor_ideal_tools import (
    finite_field_coordinates, polynomial_digest)


SOURCE_DEPENDENCIES = (
    "original_quadratic_norm_field.py",
    "original_ys_closed_point_tools.py",
    "original_ys_divisor_ideal_tools.py",
)


def _omega_coordinates(base, omega):
    """Return the full original-base map c -> (a,b), c=a+b*omega."""
    assert native_absolute_degree(base) == 2
    assert omega.parent() is base
    assert omega != 1 and omega**2+omega+1 == 0
    fp = base.prime_subfield()
    omega_polynomial = omega.polynomial()
    assert omega_polynomial.degree() == 1
    u, v = fp(omega_polynomial[0]), fp(omega_polynomial[1])
    assert v

    def coordinates(value):
        value = base(value)
        polynomial = value.polynomial()
        assert polynomial.degree() <= 1
        b = fp(polynomial[1])/v
        a = fp(polynomial[0])-u*b
        assert base(a)+base(b)*omega == value
        return a, b

    assert coordinates(omega) == (fp.zero(), fp.one())
    assert coordinates(base.one()) == (fp.one(), fp.zero())
    return fp, coordinates


class OriginalQuadraticNormFiniteFieldQuotient(ActualFiniteFieldQuotient):
    """A R974-compatible quotient with an explicit norm-polynomial model.

    omega must be the caller's actual original CM constant.  The old base
    object and both maps to its original polynomial quotient are retained.
    """
    def __init__(self, polynomial, tag, omega):
        self.P = polynomial.parent()
        self.base = self.P.base_ring()
        assert omega.parent() is self.base
        assert native_absolute_degree(self.base) == 2
        characteristic = int(self.base.characteristic())
        assert characteristic in (29, 41)
        fp, coordinates = _omega_coordinates(self.base, omega)
        self.polynomial = self.P(polynomial).monic()
        self.relative_degree = d = int(self.polynomial.degree())
        assert d >= 1 and self.polynomial.is_irreducible()
        if d == 1:
            # Preserve R974's literal original-base model in the linear case.
            super().__init__(self.polynomial, tag)
            return
        self.tag = str(tag)
        self.quotient = self.P.quotient(
            self.polynomial, names="q_"+self.tag)
        assert self.quotient.is_field()

        # c=0 works unless pi is already defined over F_r.  In that case d
        # is odd, t lies in F_(r^d), and t+omega generates all F_(r^(2d)).
        original_coordinates = [coordinates(c)
                                for c in self.polynomial.list()]
        original_pi_over_prime_field = all(not b for _, b in original_coordinates)
        shift = int(original_pi_over_prime_field)
        if shift:
            assert d % 2 == 1
        shifted = self.P(self.polynomial(self.P.gen()-shift*omega))
        shifted_coordinates = [coordinates(c) for c in shifted.list()]
        prime_ring = PolynomialRing(fp, "absolute_"+self.tag)
        A = prime_ring([a for a, _ in shifted_coordinates])
        B = prime_ring([b for _, b in shifted_coordinates])
        assert A.degree() == d and A.is_monic()
        assert B and B.degree() < d
        assert self.P(A.list())+omega*self.P(B.list()) == shifted
        norm_polynomial = A*A-A*B+B*B
        assert norm_polynomial.degree() == 2*d and norm_polynomial.is_monic()

        # Its irreducibility follows from the complete finite-subfield proof
        # in R986.  Keep Sage's usual irreducibility check in the constructor;
        # no extra search for a polynomial or for all roots of pi is used.
        self.field = GF(characteristic**(2*d),
                        name="a_"+self.tag, modulus=norm_polynomial)
        assert native_absolute_degree(self.field) == 2*d
        alpha = self.field.gen()
        assert norm_polynomial(alpha) == 0
        B_alpha = B(alpha)
        assert B_alpha
        omega_image = -A(alpha)/B_alpha
        assert omega_image != 1 and omega_image**2+omega_image+1 == 0

        def embedded_coefficient(value):
            a, b = coordinates(value)
            return self.field(a)+self.field(b)*omega_image

        base_embedding = self.base.hom(
            [embedded_coefficient(self.base.gen())], self.field)
        assert base_embedding.domain() is self.base
        assert base_embedding.codomain() is self.field
        assert base_embedding(omega) == omega_image
        self.root = alpha-shift*omega_image
        native_ring = PolynomialRing(self.field, "specified_"+self.tag)
        native_polynomial = native_ring([
            base_embedding(c) for c in self.polynomial.list()])
        assert native_polynomial(self.root) == 0

        # The basis and both complete-space returns are exactly the R974
        # contract; only the native field/root construction above changes.
        basis = [self.root**i for i in range(d)]
        space, from_space, to_space = self.field.vector_space(
            base=base_embedding, basis=basis, map=True)
        assert space.base_ring() is self.base and space.dimension() == d

        def forward(value):
            coefficients = self.P(self.quotient(value).lift()).list()
            answer = self.field.zero()
            for coefficient in reversed(coefficients):
                answer = answer*self.root+base_embedding(coefficient)
            return answer

        def backward(value):
            value = self.field(value)
            original_coordinates = to_space(value)
            assert from_space(original_coordinates) == value
            return self.quotient(self.P(list(original_coordinates)))

        self.forward, self.backward = forward, backward
        for i in range(d):
            value = self.quotient.gen()**i
            assert self.forward(value) == basis[i]
            assert self.backward(self.forward(value)) == value
            assert list(to_space(basis[i])) == [
                self.base(int(i == j)) for j in range(d)]
        for i in range(2*d):
            value = self.field.gen()**i
            assert self.forward(self.backward(value)) == value
        for i in range(2):
            value = self.base.gen()**i
            assert self.forward(self.quotient(value)) == base_embedding(value)
            assert self.backward(base_embedding(value)) == self.quotient(value)
        assert self.backward(self.root) == self.quotient.gen()
        assert self.backward(omega_image) == self.quotient(omega)
        assert self.forward(self.quotient.gen()+shift*self.quotient(omega)) == alpha
        assert self.field.cardinality() == self.base.cardinality()**d
        assert self.reduce(self.polynomial) == 0
        assert self.lift(self.root) == self.P.gen() % self.polynomial
        assert self.lift(self.embed_base(self.base.gen())) == self.P(self.base.gen())
        assert self.lift(self.embed_base(omega)) == self.P(omega)
        self.native_model_receipt = {
            "method": "R986 original quadratic norm with t-or-t-plus-omega generator",
            "original_base_absolute_degree": 2,
            "native_absolute_degree": 2*d,
            "shift_in_original_omega": shift,
            "original_polynomial_defined_over_prime_field": original_pi_over_prime_field,
            "absolute_norm_polynomial_sha256": polynomial_digest(norm_polynomial),
            "split_A_sha256": polynomial_digest(A),
            "split_B_sha256": polynomial_digest(B),
            "nonzero_B_at_absolute_generator": True,
            "specified_root_coordinates": finite_field_coordinates(self.root, self.field),
            "original_omega_image_coordinates": finite_field_coordinates(omega_image, self.field),
            "original_base_generator_image_coordinates": finite_field_coordinates(
                base_embedding(self.base.gen()), self.field),
            "original_base_object_and_embedding_retained": True,
            "both_complete_coordinate_spaces_returned": True,
            "relative_degree_not_used_as_absolute_degree": True,
            "original_quotient_not_replaced_by_unidentified_root": True,
            "norm_target_remains_original_base_field": True,
            "all_roots_of_relative_polynomial_enumerated": False,
            "all_proper_subfields_excluded_by_R986": True,
        }


def make_original_quadratic_selector(original_base, original_omega):
    """Return an explicit constructor; install no bindings and run no job.

    Only literal use of the supplied original constant-field object takes
    the new branch.  Any tower over a residue field retains R974 unchanged.
    """
    assert native_absolute_degree(original_base) == 2
    assert original_omega.parent() is original_base
    assert original_omega != 1 and original_omega**2+original_omega+1 == 0

    def selected(polynomial, tag):
        if polynomial.parent().base_ring() is original_base:
            return OriginalQuadraticNormFiniteFieldQuotient(
                polynomial, tag, original_omega)
        return ActualFiniteFieldQuotient(polynomial, tag)

    return selected
