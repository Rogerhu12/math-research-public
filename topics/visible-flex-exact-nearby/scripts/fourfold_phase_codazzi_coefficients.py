#!/usr/bin/env python3
"""True fixed-target Codazzi coefficients and exact finite waist curvature.

All target E derivatives use the original complete angular primitive and
its infinite remainder.  All radial boxes stay in one actual common scalar
germ, and the original full real affine parameter interval is retained.
The initial orthonormal C is computed from the exact finite tangent phase,
not by differentiating a sampled position.  This provider alone does not
assert existence over a specified radial interval.
"""
from __future__ import annotations
import argparse
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
import time

import numpy as np
from flint import arb, acb, ctx

from fourfold_phase_newton_source_centered import CenteredSource, CenteredPolynomial
from fourfold_phase_two_jet_newton_source import (
    Box, CBox, zeros, real_interval, common_cells, load_definition,
    save, record, sha, dot, box_abs_upper, range_record,
)
from fourfold_phase_beta_bulk_box import cdot, reduce_box


def real_part(value, name):
    z = value.to_acb() if hasattr(value, "to_acb") else acb(value)
    if not z.imag.contains(0):
        raise ValueError("real coefficient lost its imaginary zero: "+name)
    return z.real


class CodazziCoefficientTarget(CenteredSource):
    def set_actual_cell(self, left, right):
        left, right = Fraction(left), Fraction(right)
        cuts = common_cells(self)
        i = bisect_right(cuts, left)-1
        if i < 0 or not cuts[i] <= left <= right <= cuts[i+1]:
            raise ValueError("radial box crosses an exact common scalar germ")
        self.set_cell(cuts[i], cuts[i+1])

    def coefficients(self, left, right):
        """Return actual Arb scalar coefficients on a complete closed box."""
        self.set_actual_cell(left, right)
        radial = acb(real_interval(Fraction(left), Fraction(right)))
        FF, _, aa, EF, _, tail = self.scalar_jets_and_fourier(radial)
        a = [real_part(aa[j], "a"+str(j)) for j in range(4)]
        # Evaluate the exact finite zero convolution directly.  Reusing a
        # complete nonconstant-product error in its mean was valid but
        # needlessly widened the scalar target on a radial interval.
        reverse = (-np.arange(self.nodes)) % self.nodes
        norms = [arb(float(np.max(reduce_box(Box(f.magnitude_upper())).hi))).upper()
                 for f in FF]

        def product_mean(i, j):
            finite = cdot(FF[i], FF[j][reverse]).sum().to_acb()
            if not finite.imag.contains(0):
                raise ValueError("real finite target mean lost its reality enclosure")
            error = 3*(norms[i]*EF[j][0]+norms[j]*EF[i][0]+EF[i][0]*EF[j][0])
            return finite.real+arb(0, error.upper())

        E = product_mean(1, 1)
        E1 = 2*product_mean(1, 2)
        E2 = 2*product_mean(2, 2)+2*product_mean(1, 3)
        if not a[0] > 0 or not E > 0:
            raise ValueError("actual target positivity unresolved")
        K = -a[2]/(a[0]*E)+a[1]*E1/(2*a[0]*E*E)
        K1 = (-a[3]/(a[0]*E)+a[1]*a[2]/(a[0]*a[0]*E)
              +3*a[2]*E1/(2*a[0]*E*E)+a[1]*E2/(2*a[0]*E*E)
              -a[1]*a[1]*E1/(2*a[0]*a[0]*E*E)
              -a[1]*E1*E1/(a[0]*E**3))
        gamma = E.sqrt()/a[0]
        beta = a[1]/a[0]
        loggamma1 = E1/(2*E)-beta
        loggamma2 = E2/(2*E)-E1*E1/(2*E*E)-a[2]/a[0]+beta*beta
        values = dict(a=a[0], a1=a[1], a2=a[2], a3=a[3],
                      E=E, E1=E1, E2=E2, K=K, K1=K1,
                      gamma=gamma, gamma1=gamma*loggamma1,
                      gamma2=gamma*(loggamma1*loggamma1+loggamma2),
                      beta=beta, primitive_tail=tail)
        if K < 0:
            values.update(k=(-K).sqrt(), kappa=K1/(4*K))
        return values

    def exact_initial_C_polynomials(self, orders=3):
        """Finite physical-theta curvature derivatives, with parameter boxes."""
        self.set_actual_cell(Fraction(0), Fraction(0))
        self.unit_finite_data(acb(0))
        phase, vertical, radius, _ = self.last_scalar
        a0 = real_part(radius[0], "initial radius")
        if not a0 > 0:
            raise ValueError("initial radius positivity unresolved")
        # The actual waist reflection makes gamma(0,theta)=0.  Retain an
        # enclosure check; the mathematical identity is R33's symmetry.
        for j in range(self.modes):
            if not vertical[0, j].to_acb().contains(0):
                raise ValueError("exact planar waist symmetry is not enclosed")
        c = zeros((self.product_grid,))
        c[0] = CBox.from_acb(acb(-1/a0))
        for j in range(1, self.modes+1):
            bj = real_part(phase[0, j-1], "initial phase coefficient")
            cj = CBox.from_acb(acb(-2*j*bj/a0))
            c[j] = cj
            c[-j] = cj
        frequencies = 4*np.asarray([
            j if j < self.product_grid//2 else j-self.product_grid
            for j in range(self.product_grid)
        ])
        result = []
        for order in range(orders+1):
            # Differentiate the original interval coefficients BEFORE
            # centering, so every derivative pays its own complete error.
            derivative = c
            for _ in range(order):
                derivative = derivative*CBox(0., Box(frequencies))
            result.append(CenteredPolynomial(
                derivative, arb(0), self.modes, self.polynomial_fft))
        return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--object", type=Path, default=Path(
        "data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json"))
    parser.add_argument("--half-width", type=Fraction, default=Fraction(1, 10**9))
    parser.add_argument("--left", type=Fraction, default=Fraction(0))
    parser.add_argument("--right", type=Fraction, default=Fraction(1, 1000))
    parser.add_argument("--nodes", type=int, default=512)
    parser.add_argument("--angles", type=int, default=16384)
    parser.add_argument("--bits", type=int, default=192)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = args.bits
    ctx.cap = 4
    start = time.monotonic()
    target = CodazziCoefficientTarget(
        args.object, args.half_width, args.nodes, args.angles)
    coefficients = target.coefficients(args.left, args.right)
    radial_cell = list(map(str, target.cell))
    initial = target.exact_initial_C_polynomials(3)
    cells = [p.angular_cells(args.angles) for p in initial]
    initial_C = cells[0]
    if not (np.all(initial_C.hi < 0) or np.all(initial_C.lo > 0)):
        raise ValueError("initial noncharacteristic C does not have a fixed sign")
    definition, _, _, center = load_definition(args.object)
    doc = dict(
        kind="actual_complete_fixed_target_Codazzi_coefficients",
        complete=True,
        whole_radial_interval=True,
        radial_interval=[str(args.left), str(args.right)],
        exact_common_scalar_germ=radial_cell,
        whole_parameter_interval=True,
        exact_center_parameter=str(center),
        exact_parameter_half_width=str(args.half_width),
        original_target_unchanged=True,
        object_sha256=sha(args.object),
        origin_sha256=definition["origin_inputs"]["sha256"],
        direction_sha256=definition["direction"]["sha256"],
        source_sha256=sha(__file__),
        dependency_sha256={
            name: sha(Path(__file__).with_name(name)) for name in (
                "fourfold_phase_newton_source_centered.py",
                "fourfold_phase_two_jet_newton_source.py",
                "fourfold_phase_metric_defect.py",
                "fourfold_phase_cap_scaled_body.py",
                "fourfold_phase_cap_parameter_comparison.py",
                "fourfold_phase_beta_bulk_box.py",
            )
        },
        coefficients={key: record(value) for key, value in coefficients.items()},
        strict_negative_target=bool(coefficients["K"] < 0),
        exact_initial_B="0",
        exact_initial_C_formula="-(1+sum_j 4j beta_j(0) cos(4j theta))/a(0)",
        complete_initial_angular_circle=True,
        initial_C_derivative_ranges=[range_record(value) for value in cells],
        initial_C_derivative_absolute_bounds=[
            record(box_abs_upper(value)) for value in cells],
        initial_C_derivative_Wiener_bounds=[
            record((p.norm()+p.error).upper()) for p in initial],
        primitive_nodes=args.nodes, closed_angular_cells=args.angles,
        exact_phase_modes=target.modes, bits=args.bits,
        wall_seconds=time.monotonic()-start,
        numerical_Codazzi_solution_validated=False,
        specified_width_Cauchy_continuation_claimed=False,
        full_closed_surface_completion_claimed=False,
    )
    save(args.out, doc)
    print({"out": str(args.out), "strict_negative_target": doc["strict_negative_target"],
           "coefficients": {key: value.str(14) for key, value in coefficients.items()
                            if key in ("K", "K1", "gamma", "beta", "kappa")},
           "wall_seconds": doc["wall_seconds"]}, flush=True)


if __name__ == "__main__":
    main()
