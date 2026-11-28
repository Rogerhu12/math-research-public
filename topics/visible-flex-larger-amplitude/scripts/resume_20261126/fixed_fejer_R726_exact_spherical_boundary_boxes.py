#!/usr/bin/env python3
"""Accurate R726 spherical boundary and complete two-angle/radial interval jets.

This is the analytic Slerp function, including its zero-angle extension.
It does not evaluate the working degree32 approximation, solve a working
root, infer a global branch, or import a scientific solver. Exact rational
partial sums plus full infinite tails enclose every q in a paid [0,Q], Q<2.
All source/model/whole-domain obligations belong to the explicit caller.
"""
from __future__ import annotations

from fractions import Fraction as F
import hashlib
import json
import os
from pathlib import Path

SCHEMA = "complete-R726-accurate-spherical-boundary-and-jets-v1"
PARENT_MATH_SHA256 = "0471c626b7850fecf19513d68209e090f88830b89ff8ad7cc62c2d1709a75e5b"
PARENT_MATH_BYTES = 72182
THEOREM_PATH = "results/R726-spherical-boundary-strong-monotonicity-and-positive-mean-root.md"
THEOREM_SHA256 = "faa3e44cf1392e6f7e1fb4e04adb039afc54ac881ef3f99b0b4ca9810d9e226b"
THEOREM_BYTES = 27362
DEFAULT_SERIES_DEGREE = 64


class SphericalDomainUnavailable(ArithmeticError):
    """A complete accurate enclosure is not paid; no working failure is inferred."""


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Complete accurate spherical evaluation belongs to public Actions")


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(encode(value), sort_keys=True,
        separators=(",", ":"), allow_nan=False).encode()).hexdigest()


def encode(value):
    if isinstance(value, F):
        return str(value)
    if hasattr(value, "lo") and hasattr(value, "hi"):
        return [str(value.lo), str(value.hi)]
    if isinstance(value, dict):
        return {str(k): encode(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [encode(v) for v in value]
    return value


def definition():
    return dict(
        schema=SCHEMA,
        accurate_coefficient="f_a(q)=sin(a*acos(1-q))/sin(acos(1-q)); analytic at q=0",
        coefficient_domain="0<=a<=1, 0<=q<=Q<2",
        exact_coefficient_recurrence="c0=a; c[n+1]=((n+1)^2-a^2)/((n+1)*(2n+3))*c[n]",
        complete_infinite_series=True,
        coefficient_envelope="0<=c[n]<=2^-n",
        a_derivative_envelope="abs(dc[n]/da)<=5*2^-n",
        a_derivative_recurrence="g0=1; g[n+1]=r[n]*g[n]-2*a*c[n]/((n+1)*(2n+3))",
        exact_value_q_first_q_second_and_a_first=True,
        full_tail_included_after_every_finite_partial_sum=True,
        default_finite_partial_sum_degree=DEFAULT_SERIES_DEGREE,
        finite_working_polynomial_is_not_used_as_exact_function=True,
        working_small_large_switch_is_not_used=True,
        both_inputs_normalized_with_complete_first_and_second_jets=True,
        accurate_output_normalization="identity since exact Slerp of two unit inputs is unit",
        all_reference_mean_mixed_angular_terms_included=True,
        exact_material_derivative_includes_reference_turn_and_cutoff_turn=True,
        raw_v_Jacobian_has_all_three_columns=True,
        source_of_rational_interval_operations=PARENT_MATH_SHA256,
        original_quadrature_or_working_word_error_bound_inferred=False,
        accurate_mean_root_or_global_branch_inferred=False,
        closed_surface_or_normal32_certificate_inferred=False)


def bind_parent_math(parent):
    path = Path(parent.__file__)
    if (sha(path) != PARENT_MATH_SHA256 or path.stat().st_size != PARENT_MATH_BYTES
            or sha(parent.normalized_jets.__code__.co_filename) != PARENT_MATH_SHA256
            or sha(parent.trig_boxes.__code__.co_filename) != PARENT_MATH_SHA256):
        raise ValueError("Use the entire original outward interval/profile mathematics")
    return parent


class ExactSphericalBoundary:
    """One source-bound outward arithmetic context, with no independent budget."""

    def __init__(self, parent_math, *, bits=192, degree=DEFAULT_SERIES_DEGREE,
                 budget_check=None):
        require_actions()
        self.k = bind_parent_math(parent_math)
        if type(bits) is not int or not 64 <= bits <= 1024:
            raise ValueError("Use the original explicit outward arithmetic precision")
        if type(degree) is not int or degree < 2:
            raise ValueError("A complete series partial sum includes at least degrees zero to two")
        if budget_check is not None and not callable(budget_check):
            raise ValueError("The supplied budget check must be the caller's actual check")
        self.bits, self.degree = bits, degree
        self.I = self.k.Interval
        self.budget_check = budget_check
        self.counts = dict(coefficient_enclosures=0, complete_boundary_jet_enclosures=0,
            raw_mean_Jacobian_enclosures=0, material_jet_enclosures=0)
        self.definition = definition()
        self.definition_identity = canonical(self.definition)

    def check(self):
        if self.budget_check is not None:
            self.budget_check()

    def point(self, value):
        value = F(value)
        return self.I(value, value, self.bits)

    def box(self, value):
        if hasattr(value, "lo") and hasattr(value, "hi"):
            return self.I(F(value.lo), F(value.hi), self.bits)
        if isinstance(value, dict):
            if set(value) != {"lower_exact", "upper_exact"}:
                raise ValueError("Use both complete exact endpoints of an interval")
            return self.I(F(value["lower_exact"]), F(value["upper_exact"]), self.bits)
        if isinstance(value, (list, tuple)):
            return self.k.box(value, self.bits)
        return self.point(value)

    def vector(self, value):
        if not isinstance(value, (list, tuple)) or len(value) != 3:
            raise ValueError("Retain all three complete vector components")
        return [self.box(q) for q in value]

    def jets(self, value):
        if not isinstance(value, (list, tuple)) or len(value) != 3:
            raise ValueError("Retain value, first and second complete angular jets")
        return [self.vector(q) for q in value]

    def U(self, value):
        return self.k.upper_dyadic(F(value), self.bits)

    def coefficient(self, a, q):
        """Outward f, f_q, f_qq and f_a including complete infinite tails."""
        require_actions()
        self.check()
        a, q = self.box(a), self.box(q)
        if not 0 <= a.lo <= a.hi <= 1:
            raise ValueError("The accurate cutoff coefficient must be enclosed in [0,1]")
        if not 0 <= q.lo <= q.hi < 2:
            raise SphericalDomainUnavailable("No complete strict non-antipodal q upper bound")
        c, ca = a, self.point(1)
        coefficients, a_coefficients = [c], [ca]
        for n in range(self.degree):
            if n % 16 == 0:
                self.check()
            k = n+1
            denominator = k*(2*k+1)
            ratio = (k*k-a*a)/denominator
            next_c = ratio*c
            next_ca = ratio*ca-(2*a/denominator)*c
            c, ca = next_c, next_ca
            coefficients.append(c)
            a_coefficients.append(ca)
        value, first, second = coefficients[-1], self.point(0), self.point(0)
        a_first = a_coefficients[-1]
        for n in range(self.degree-1, -1, -1):
            second, first, value = second*q+2*first, first*q+value, value*q+coefficients[n]
            a_first = a_first*q+a_coefficients[n]
        t, N = q.hi/2, self.degree
        gap = 1-t
        # These are exact rational sums of the full positive geometric tails.
        tail0 = self.U(t**(N+1)/gap)
        tail1 = self.U(((N+1)*t**N/gap+t**(N+1)/(gap*gap))/2)
        tail2 = self.U((N*(N+1)*t**(N-1)/gap
            +2*(N+1)*t**N/(gap*gap)+2*t**(N+1)/(gap**3))/4)
        taila = self.U(5*t**(N+1)/gap)
        value = value+self.I(0, tail0, self.bits)
        first = first+self.I(0, tail1, self.bits)
        second = second+self.I(0, tail2, self.bits)
        a_first = a_first+self.I(-taila, taila, self.bits)
        # The coefficient endpoint laws are exact. Its a derivative remains.
        if a.lo == a.hi == 0:
            value, first, second = self.point(0), self.point(0), self.point(0)
        elif a.lo == a.hi == 1:
            value, first, second = self.point(1), self.point(0), self.point(0)
        self.counts["coefficient_enclosures"] += 1
        return dict(value=value, q_first=first, q_second=second, a_first=a_first,
            evidence=dict(schema=SCHEMA+"-coefficient",
                a_interval=a, q_interval=q, finite_partial_sum_degree=N,
                exact_complete_tail_upper=dict(value=tail0,q_first=tail1,
                    q_second=tail2,a_first_absolute=taila),
                q_derivative_tails_are_nonnegative=True,
                a_derivative_tail_is_signed=True,
                all_infinite_series_terms_enclosed=True,
                finite_working_coefficients_reused=False))

    def normalized(self, raw_jets, *, norm_lower, norm_upper):
        values = self.jets(raw_jets)
        lower, upper = F(norm_lower), F(norm_upper)
        if not 0 < lower <= upper:
            raise SphericalDomainUnavailable("A positive complete raw-vector norm bound is required")
        unit, radius = self.k.normalized_jets(*values,
            norm_lower=lower, norm_upper=upper)
        # Intersections use only the exact N(x) unit-vector identity.
        unit[0] = [q.intersect(-1,1) for q in unit[0]]
        return values, unit, radius

    def boundary(self, raw_u_jets, raw_v_jets, chi, *,
                 u_norm_lower, u_norm_upper, v_norm_lower, v_norm_upper,
                 raw_u_s=None, chi_s=None, nonantipodal_q_upper=None,
                 include_raw_v_Jacobian=False):
        """Complete exact Slerp graph on one paid radial/angle domain.

        norm and q bounds are caller-paid mathematical constraints on actual
        values. Intersecting them with boxes does not repair a working word.
        The v candidate/accurate mean is independent of material s.
        """
        require_actions()
        self.check()
        k = self.k
        raw_u, uj, ur = self.normalized(raw_u_jets,
            norm_lower=u_norm_lower,norm_upper=u_norm_upper)
        raw_v, dj, vr = self.normalized(raw_v_jets,
            norm_lower=v_norm_lower,norm_upper=v_norm_upper)
        chi = self.box(chi)
        if not 0 <= chi.lo <= chi.hi <= 1:
            raise ValueError("The complete actual cutoff law must enclose chi in [0,1]")
        u, u1, u2 = uj
        d, d1, d2 = dj
        difference = k.vsub(u,d)
        first_difference = k.vsub(u1,d1)
        second_difference = k.vsub(u2,d2)
        q = k.dot(difference,difference)/2
        # The exact two normalized inputs obey q>=0. A supplied strict upper
        # comes only from the caller's complete non-antipodal/R727 evidence.
        cap = q.hi
        if nonantipodal_q_upper is not None:
            paid_cap = F(nonantipodal_q_upper)
            if not 0 <= paid_cap < 2:
                raise ValueError("A supplied non-antipodal bound must be an actual strict bound below two")
            cap = min(cap,paid_cap)
        q = q.intersect(0,cap)
        if q.hi >= 2:
            raise SphericalDomainUnavailable("The complete normalized input pair is not separated from antipodality")
        q1 = k.dot(difference,first_difference)
        q2 = k.dot(first_difference,first_difference)+k.dot(difference,second_difference)
        A, B = self.coefficient(1-chi,q), self.coefficient(chi,q)
        C = k.vadd(k.vscale(u,A["q_first"]),k.vscale(d,B["q_first"]))
        value = k.vadd(k.vscale(u,A["value"]),k.vscale(d,B["value"]))
        first = k.vadd(k.vadd(k.vscale(u1,A["value"]),k.vscale(d1,B["value"])),
            k.vscale(C,q1))
        second = k.vadd(
            k.vadd(k.vscale(u2,A["value"]),k.vscale(d2,B["value"])),
            k.vadd(k.vscale(k.vadd(k.vscale(u1,A["q_first"]),
                k.vscale(d1,B["q_first"])),2*q1),
                k.vadd(k.vscale(C,q2),
                    k.vscale(k.vadd(k.vscale(u,A["q_second"]),
                        k.vscale(d,B["q_second"])),q1*q1))))
        # Exact Slerp is already unit. There is no finite-polynomial output
        # normalization or unproved normalization denominator in this graph.
        value = [q.intersect(-1,1) for q in value]
        radial = None
        if (raw_u_s is None) != (chi_s is None):
            raise ValueError("The full material derivative requires both T0_s and chi_s")
        if raw_u_s is not None:
            xs, cs = self.vector(raw_u_s), self.box(chi_s)
            us = k.vscale(k.vsub(xs,k.vscale(u,k.dot(u,xs))),1/ur[0])
            qs = k.dot(difference,us)
            As = A["q_first"]*qs-A["a_first"]*cs
            Bs = B["q_first"]*qs+B["a_first"]*cs
            radial = k.vadd(k.vscale(us,A["value"]),
                k.vadd(k.vscale(u,As),k.vscale(d,Bs)))
            self.counts["material_jet_enclosures"] += 1
        matrix = None
        if include_raw_v_Jacobian:
            zero, one = self.point(0), self.point(1)
            Dv = [[((one if i==j else zero)-d[i]*d[j])/vr[0]
                for j in range(3)] for i in range(3)]
            middle = [[(B["value"] if i==j else zero)-C[i]*difference[j]
                for j in range(3)] for i in range(3)]
            matrix = [[sum((middle[i][ell]*Dv[ell][j] for ell in range(3)),zero)
                for j in range(3)] for i in range(3)]
            self.counts["raw_mean_Jacobian_enclosures"] += 1
        self.counts["complete_boundary_jet_enclosures"] += 1
        return dict(
            value=value, phi=first, phiphi=second, material_s=radial,
            raw_v_Jacobian=matrix,
            normalized_reference_jets=uj,normalized_mean_jets=dj,
            raw_reference_radius_jets=ur,raw_mean_radius_jets=vr,
            evidence=dict(schema=SCHEMA+"-full-boundary",
                exact_chi=chi,
                complete_raw_reference_jets=raw_u,complete_raw_mean_jets=raw_v,
                raw_reference_norm_constraint=[str(F(u_norm_lower)),str(F(u_norm_upper))],
                raw_mean_norm_constraint=[str(F(v_norm_lower)),str(F(v_norm_upper))],
                q_interval=q,q_phi=q1,q_phiphi=q2,
                supplied_nonantipodal_q_upper=(None if nonantipodal_q_upper is None
                    else str(F(nonantipodal_q_upper))),
                A_coefficient=A["evidence"],B_coefficient=B["evidence"],
                reference_and_mean_normalizations_differentiated=True,
                all_zero_first_second_reference_mean_cross_terms_retained=True,
                exact_unit_output_identity_from_R726=True,
                material_reference_and_cutoff_terms_included=radial is not None,
                all_three_raw_mean_columns_included=matrix is not None,
                working_graph_error_or_true_mean_root_not_inferred=True))

    def metadata(self):
        return dict(schema=SCHEMA,source_sha256=sha(__file__),
            definition=self.definition,definition_identity_sha256=self.definition_identity,
            complete_parent_math_sha256=PARENT_MATH_SHA256,
            theorem_sha256=THEOREM_SHA256,
            precision_bits=self.bits,finite_partial_sum_degree=self.degree,
            complete_infinite_tail_enclosed=True,
            actual_counts=dict(self.counts),
            scientific_working_field_or_mean_solve_calls=0,
            independent_budget_created=False,
            original_budgets_unchanged=True,
            whole_mean_or_normal_branch_certified=False)
