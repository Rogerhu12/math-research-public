#!/usr/bin/env python3
"""Strict fixed-W constant for the continuous R42 orthogonal coordinates.

The three W moments are reused from the published R41 enclosure.  Only
the three chi**2 moments are newly integrated.  Every finite operation is
rational with outward rounding; no quadrature, FFT, floating eigenvalue
or BVP is used.  This is an L2 coordinate bound, not a BVP Jacobian bound.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import sys
import time

import integral_core_intervals as ri
from certify_protected_arc_curvature_dual import decimal, show
from generic_raw_core_intervals import primitive_degree


A, WIDTH = F(21, 100), F(2, 5)
R41_SHA256 = 'fed7050c460076fd29eb5ca60f547bc1318bc8704de4bef241985f422f858316'
INVERSE_SQUARED_UPPER = F(86161, 10000)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def polynomial_square(coefficients):
    result = [F(0)]*(2*len(coefficients)-1)
    for j, a in enumerate(coefficients):
        for k, b in enumerate(coefficients):
            result[j+k] += a*b
    return tuple(result)


def squared_cutoff_integral(frequency, degree):
    """Enclose int_0^(a+b) chi(s)^2 exp(i*k*s) ds.

    On the transition chi is the literal degree-nine polynomial, and
    chi**2 is in [0,1].  Expanding the unit-modulus exponential through
    degree R gives the integrated complex remainder
    b*|k*b|**(R+1)/(R+2)!, also valid after rotation exp(i*k*a).
    """
    assert isinstance(frequency, int) and frequency >= 0 and degree >= 0
    coefficients = polynomial_square(ri.CHI)
    real, imaginary = F(0), F(0)
    z = frequency*WIDTH
    for r in range(degree+1):
        moment = sum((value/F(r+j+1) for j, value in enumerate(coefficients)), F(0))
        term = z**r/F(math.factorial(r))*moment
        if r % 4 == 0:
            real += term
        elif r % 4 == 1:
            imaginary += term
        elif r % 4 == 2:
            real -= term
        else:
            imaginary -= term
    sine, cosine = ri.signed_sincos(ri.point(frequency*A))
    rotated_real = ri.scale(ri.sub(ri.scale(cosine, real), ri.scale(sine, imaginary)), WIDTH)
    rotated_imag = ri.scale(ri.add(ri.scale(sine, real), ri.scale(cosine, imaginary)), WIDTH)
    error = WIDTH*abs(z)**(degree+1)/math.factorial(degree+2)
    base_real, base_imag = ri.plain_integrals(frequency, ri.point(A))
    return (ri.add(base_real, ri.add(rotated_real, (-error, error))),
            ri.add(base_imag, ri.add(rotated_imag, (-error, error)))), error


def symmetric_matrix(entries):
    return ((entries[0], entries[1]), (entries[1], entries[2]))


def determinant(matrix):
    return ri.sub(ri.mul(matrix[0][0], matrix[1][1]), ri.power(matrix[0][1], 2))


def multiply(left, right):
    return tuple(tuple(ri.add(ri.mul(left[i][0], right[0][j]),
                             ri.mul(left[i][1], right[1][j]))
                       for j in range(2)) for i in range(2))


def inverse_symmetric(matrix):
    det = determinant(matrix)
    assert matrix[0][0][0] > 0 and det[0] > 0
    return ((ri.divide(matrix[1][1], det), ri.neg(ri.divide(matrix[0][1], det))),
            (ri.neg(ri.divide(matrix[0][1], det)), ri.divide(matrix[0][0], det)))


def matrix_entries(matrix):
    return [show(matrix[0][0]), show(matrix[0][1]), show(matrix[1][1])]


def source_hashes():
    directory = Path(__file__).resolve().parent
    names = (Path(__file__).name, 'generic_raw_core_intervals.py',
             'fast_integral_core_intervals.py', 'integral_core_intervals.py',
             'certify_protected_arc_curvature_dual.py')
    return {name: sha(directory/name) for name in names}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--r41-execution', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    assert sha(args.r41_execution) == R41_SHA256
    previous = json.loads(args.r41_execution.read_text())
    inputs = previous['exact_inputs']
    assert F(inputs['halfwidth']) == A
    assert F(inputs['control_transition']) == WIDTH
    assert inputs['center'] == 'pi/3'
    assert previous['core_control_path'] == 'raw-mean-primary-compact-v1'

    # This is a reuse of published strict intervals, not a fresh G1 run.
    m0, m1, m2 = tuple(tuple(map(F, interval))
                       for interval in previous['raw_projection']['gram_entries'])
    G1 = symmetric_matrix((m0, m1, m2))
    L = ri.scale(ri.pi_interval(), F(1, 3))
    assert A+WIDTH < L[0]
    degree = primitive_degree(WIDTH, 6)
    square_integrals, remainders = zip(*(squared_cutoff_integral(3*j, degree) for j in range(3)))
    chi_square_cosine = [ri.scale(ri.divide(value[0], L), (-1)**j)
                         for j, value in enumerate(square_integrals)]
    w_cosine = (m0, m1, ri.sub(ri.scale(m2, 2), m0))
    squared_w_cosine = [ri.add(ri.sub(ri.scale(w_cosine[j], 2), ri.point(int(j == 0))),
                              chi_square_cosine[j]) for j in range(3)]
    nu0, nu1 = squared_w_cosine[:2]
    nu2 = ri.scale(ri.add(squared_w_cosine[0], squared_w_cosine[2]), F(1, 2))
    G2 = symmetric_matrix((nu0, nu1, nu2))
    assert G2[0][0][0] > 0 and determinant(G2)[0] > 0

    inverse_G1 = inverse_symmetric(G1)
    S = multiply(multiply(inverse_G1, G2), inverse_G1)
    # The exact product is symmetric. Intersect its two valid off-diagonal
    # enclosures; neither floating symmetrization nor an approximate K is used.
    offdiag = max(S[0][1][0], S[1][0][0]), min(S[0][1][1], S[1][0][1])
    assert offdiag[0] <= offdiag[1]
    S = symmetric_matrix((S[0][0], offdiag, S[1][1]))
    T = symmetric_matrix((ri.sub(ri.point(INVERSE_SQUARED_UPPER), S[0][0]),
                          ri.neg(S[0][1]),
                          ri.sub(ri.point(INVERSE_SQUARED_UPPER), S[1][1])))
    assert T[0][0][0] > 0 and determinant(T)[0] > 0
    gram_upper = 1+F(3, 2)*INVERSE_SQUARED_UPPER
    assert gram_upper < 14

    output = dict(
        scope=__doc__, command=sys.argv,
        source_sha256=source_hashes(),
        reused_R41_execution_sha256=R41_SHA256,
        exact_cutoff=dict(n=3, halfwidth=str(A), control_transition=str(WIDTH),
                          center='pi/3', chi='1-126*t^5+420*t^6-540*t^7+315*t^8-70*t^9',
                          inner_product='dphi/(2*pi)', x='cos(3*phi)'),
        integration=dict(new_frequencies=[0, 3, 6], exponential_degree=degree,
                         complex_remainder_upper=decimal(max(remainders), True),
                         exact_rational_polynomial=True, quadrature_used=False,
                         W_moments_recomputed=False),
        symmetric_entry_order=['00', '01', '11'],
        G1_W_moment_intervals=matrix_entries(G1),
        G1_determinant=show(determinant(G1)),
        G2_squared_W_moment_intervals=matrix_entries(G2),
        G2_determinant=show(determinant(G2)),
        inverse_norm_square_matrix_intervals=matrix_entries(S),
        inverse_norm_square_upper=str(INVERSE_SQUARED_UPPER),
        inverse_gate_first_minor=show(T[0][0]),
        inverse_gate_determinant=show(determinant(T)),
        uniform_gram_upper=str(gram_upper),
        uniform_gram_upper_decimal=decimal(gram_upper, True),
        strict_gram_less_than_14=True,
        independent_of_modes_amplitude_controls_and_primary_width=True,
        limitations=['The stated fixed W only; changing a or the control width requires new moments.',
                     'An L2 coordinate Gram bound, not a derivative, rho, metric or BVP Jacobian bound.',
                     'No continuous high-degree production recurrence coefficients are certified here.'],
        elapsed_seconds=time.monotonic()-started)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(dict(output=str(args.out), output_sha256=sha(args.out),
                          inverse_norm_square_upper=str(INVERSE_SQUARED_UPPER),
                          uniform_gram_upper=str(gram_upper),
                          elapsed_seconds=output['elapsed_seconds'])))


if __name__ == '__main__':
    main()
