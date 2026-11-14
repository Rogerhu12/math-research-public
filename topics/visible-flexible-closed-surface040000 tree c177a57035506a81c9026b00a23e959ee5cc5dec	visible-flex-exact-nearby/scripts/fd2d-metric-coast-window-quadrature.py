#!/usr/bin/env python3
"""Exact scalar mass comparison for the actual R144 quintic coast windows.

This does not inspect a BVP state or build an operator.  Binary window
coefficients actually produced by the source are treated as exact rationals.
For the two boundary cells the uncut Gauss2 mass is an exact polynomial in
lambda=cell_width/rim_width.  Three-point quadrature on the known polynomial
pieces removes this scalar quartic error, but not every nonpolynomial GC
quadrature error.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import json
import math
from pathlib import Path
import time
import numpy as np
from fd2d_gc_archive_arrays import identity, load_npz
from fd2d_gc_bump_coast_native_field import window


def rational(q):
    return dict(numerator=str(q.numerator), denominator=str(q.denominator))


def outward_float(q):
    value = float(q)
    lo = np.nextafter(value, -np.inf) if Fraction(value) > q else value
    hi = np.nextafter(value, np.inf) if Fraction(value) < q else value
    return [float(lo), float(hi)]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ('field', 'inlet', 'out-prefix'):
        ap.add_argument('--'+name, type=Path, required=True)
    args = ap.parse_args(); start = time.monotonic()
    output = args.out_prefix.with_name(args.out_prefix.name+'-report.json')
    if list(output.parent.glob(args.out_prefix.name+'*')):
        raise FileExistsError('Use a new output stem')
    data = load_npz(args.field); inlet = load_npz(args.inlet)
    definition = json.loads(str(data['coast_reference_definition']))
    x = np.asarray(data['mesh'], float)
    entry, length = float(inlet['entry_s']), float(inlet['coast_length'])
    fraction = float(definition['rim_fraction'])
    exit_s, rim = entry+length, length*fraction
    if definition['support'] != [entry, exit_s]:
        raise ValueError('The actual saved support differs from the inlet')
    if not 0 < fraction < .5:
        raise ValueError('Need disjoint rims')
    left_cell = np.flatnonzero(x[:-1] == entry)
    right_cell = np.flatnonzero(x[1:] == exit_s)
    if len(left_cell) != 1 or len(right_cell) != 1:
        raise ValueError('This exact diagnostic expects the actual support endpoints among the saved nodes')
    root_three_lower = Fraction(math.isqrt(3*(2**200)), 2**100)
    root_three_upper = root_three_lower+Fraction(1, 2**100)
    alpha_lower = Fraction(1, 2)-root_three_upper/6
    beta_upper = Fraction(1, 2)+root_three_upper/6
    gx, gw = np.polynomial.legendre.leggauss(2); gp = (gx+1)/2; gw = gw/2
    g3, w3 = np.polynomial.legendre.leggauss(3); g3 = (g3+1)/2; w3 = w3/2
    rows = []
    for cell, sign in ((int(left_cell[0]), 1), (int(right_cell[0]), -1)):
        a, b = map(float, x[cell:cell+2])
        width_q = Fraction(b)-Fraction(a)
        lam = width_q/Fraction(rim)
        if ((sign == 1 and Fraction(b) > Fraction(exit_s)-Fraction(rim))
                or (sign == -1 and Fraction(a) < Fraction(entry)+Fraction(rim))):
            raise ValueError('A boundary cell enters the opposite ramp; the single-ramp mass formula does not apply')
        if not lam >= 1 or not lam*alpha_lower > 0 or not lam*beta_upper < 1:
            raise ValueError('Actual boundary-cell Gauss2 points do not lie inside one full quintic ramp')
        # Both Gauss nodes lie in the ramp while the cell extends past it.
        # alpha+beta=1, alpha*beta=1/6 eliminates every radical exactly.
        mass = 10*lam**3-15*lam**4+Fraction(35, 6)*lam**5
        signed_mass = sign*mass
        error = signed_mass-sign
        points = a+(b-a)*gp
        numerical_mass = (b-a)*float(gw@window(points, entry, length, fraction)[1])
        # In the left rim use q=(s-entry)/rim; in the right use
        # q=(exit-s)/rim. The polynomial coefficient is the same.
        exact_split_three = Fraction(sign)
        numerical_split_three = sign*float(np.sum(w3*30*g3*g3*(1-g3)*(1-g3)))
        rows.append(dict(cell=cell, left=a, right=b, width=float(width_q),
            lambda_exact=rational(lam), lambda_enclosure=outward_float(lam),
            Gauss2_points=points.tolist(), exact_endpoint_mass=sign,
            exact_Gauss2_mass=rational(signed_mass), exact_Gauss2_mass_enclosure=outward_float(signed_mass),
            exact_Gauss2_error=rational(error), exact_Gauss2_error_enclosure=outward_float(error),
            actual_float_Gauss2_mass=numerical_mass,
            float_vs_exact_scalar_quadrature_difference=numerical_mass-float(signed_mass),
            rim_piece_three_point_exact_mass=rational(exact_split_three),
            rim_piece_three_point_float_mass=numerical_split_three,
            rim_piece_two_point_exact_mass=rational(Fraction(5*sign, 6))))
    ideal = Fraction(25, 21)
    ideal_mass = 10*ideal**3-15*ideal**4+Fraction(35, 6)*ideal**5
    report = dict(schema='fd2d-R144-actual-window-Gauss2-mass-v1',
        actual_execution=True, source=identity(__file__),
        reader_source=identity(Path(__file__).parent/'fd2d_gc_bump_coast_native_field.py'),
        field=identity(args.field), inlet=identity(args.inlet),
        actual_saved_mesh_node_count=len(x), reference_definition=definition,
        weight_coefficients=dict(entry_s=entry, exit_s=exit_s, length=length,
            rim_fraction=fraction, rim_width=rim,
            exact_representatives={k:rational(Fraction(v)) for k,v in
                dict(entry_s=entry,exit_s=exit_s,rim_width=rim).items()},
            convention='Round entry+length and length*fraction as the existing floating provider does, then regard those binary coefficients as exact polynomial constants'),
        rows=rows, ideal_uniform_coast_ratio=rational(ideal),
        ideal_Gauss2_mass=rational(ideal_mass), ideal_Gauss2_mass_enclosure=outward_float(ideal_mass),
        exact_lemma='If lambda>=1 and lambda*(1/2+sqrt(3)/6)<1, integral Gauss2 of S5_prime over the containing cell equals 10lambda^3-15lambda^4+(35/6)lambda^5, while the endpoint mass is one.',
        split_uniform_Gauss2_ramp_mass='1-1/(6*N^4) for N equal polynomial ramp cells',
        piecewise_three_point_exact_for_scalar_weight_derivative=True,
        complete_nonpolynomial_GC_quadrature_claimed_exact=False,
        unknown_fields_evaluated=False, body_integration_run=False,
        large_matrix_assembled=False, nonlinear_solve_performed=False,
        metric_or_BVP_failure_inferred=False, seconds=time.monotonic()-start)
    output.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(report=identity(output), seconds=report['seconds'],
        boundary_cells=[r['cell'] for r in rows],
        exact_missing_mass_enclosures=[outward_float(abs(Fraction(r['exact_Gauss2_error']['numerator'])/int(r['exact_Gauss2_error']['denominator']))) for r in rows]),allow_nan=False),flush=True)


if __name__ == '__main__':
    main()
