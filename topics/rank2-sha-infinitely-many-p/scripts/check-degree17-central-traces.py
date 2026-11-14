#!/usr/bin/env python3
"""Exact global central traces needed to identify the degree-17 theta section.

The finite-ring engine is the existing independently checked conductor-orbit
certificate. This script adds explicit global denominator and complex bounds,
so that its residues uniquely determine rational Gaussian traces. No floating
point computation, CLS table, or assumed theta candidate enters this step.

Default: run the full orbit engine at 3^400. For a read-only cached run:
  python check-degree17-central-traces.py --cached /tmp/orbit.json
The positive signs of the three normalized Taylor coefficients are certified
separately by check-theta-explicit-section.py, using rigorous Gaussian balls.
"""

import argparse
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from math import ceil, factorial, lcm
from pathlib import Path
import json
import subprocess
import sys

F = Fraction
PRECISION = 400
MODULUS = 3**PRECISION
WEIGHTS = (1, 4, 8, 12, 16)


def derivation(poly):
    """D U=-X, D X=2Y, D Y=3X^2-17; reduce Y^2=X^3-17X."""
    out = defaultdict(int)
    for (a, b, c), value in poly.items():
        if a:
            out[a-1, b+1, c] -= a*value
        if b:
            if c == 0:
                out[a, b-1, 1] += 2*b*value
            else:
                out[a, b+2, 0] += 2*b*value
                out[a, b, 0] -= 34*b*value
        if c:
            out[a, b+2, 0] += 3*value
            out[a, b, 0] -= 17*value
    return {key: value for key, value in out.items() if value}


C = [{(0, 0, 0): 1}]
for _ in range(17):
    out = defaultdict(int, derivation(C[-1]))
    for (a, b, c), value in C[-1].items():
        out[a+1, b, c] += value
    C.append(dict(out))

wp = [F(0)]
log_q = [F(0)]
q = [F(1)]
for n in range(1, 5):
    numerator = 6*sum((wp[j]*wp[n-j] for j in range(1, n)), F(0))
    if n == 1:
        numerator -= 34
    wp.append(numerator/F((4*n-2)*(4*n-3)-12))
    log_q.append(wp[n]/(4*n*(4*n-1)))
    q.append(sum((j*log_q[j]*q[n-j] for j in range(1, n+1)), F(0))/n)


@lru_cache(None)
def d_power(k, n):
    return C[k] if n == 0 else derivation(d_power(k, n-1))


def central_polynomial(m):
    out = defaultdict(F)
    for j, qj in enumerate(q):
        if 4*j > m+1:
            break
        scale = qj/F(factorial(m)*factorial(m+1-4*j))
        for key, value in d_power(m+1-4*j, m).items():
            out[key] += scale*value
    return {key: value for key, value in out.items() if value}


def gaussian_mul(x, y):
    return x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0]


def gaussian_power(x, n):
    out = (1, 0)
    while n:
        if n & 1:
            out = gaussian_mul(out, x)
        x = gaussian_mul(x, x)
        n >>= 1
    return out


def global_reconstruction(m, row):
    poly = central_polynomial(m)
    assert len(poly) == row["polynomial_terms"]
    # D never increases the U-degree; C_(m+1-j) has U-degree <= m+1-j.
    assert max(a for a, _, _ in poly) <= m+1
    denominator = lcm(*(value.denominator for value in poly.values()))
    # Good-model estimates were proved for every primitive conductor point:
    # at 2: v(U)>=-3/2, v(X)>=0, v(Y)>=1/2;
    # at 17: v(U)>=-3/4, v(X)>=1/2, v(Y)>=3/4;
    # at other finite places U,X,Y are integral.
    clearing = (denominator
                * 2**ceil(F(3*(m+1), 2))
                * 17**ceil(F(3*(m+1), 4)))
    # The already proved complex lattice bounds give these strict integers.
    height = 256*sum((abs(value)*740**a*50000**b*3600000**c
                      for (a, b, c), value in poly.items()), F(0))
    assert 2*clearing*height < MODULUS
    loss = row["coefficient_denominator_loss"]
    assert clearing % 3**loss == 0
    residue_multiplier = clearing//3**loss
    coordinates = []
    for residue in row["trace_scaled_coefficients_1_i"]:
        integer = residue*residue_multiplier % MODULUS
        if 2*integer > MODULUS:
            integer -= MODULUS
        assert abs(integer) < clearing*height
        coordinates.append(F(integer, clearing))
    # Each coordinate is the unique integer in the proven symmetric bound.
    raw = tuple(coordinates)
    # Raw d1=64(1+i); the proved canonical d1=64(-1+i) fixes rotation i.
    # A rotation epsilon changes d_m by epsilon^(-(2m+1)).
    canonical = gaussian_mul(raw, gaussian_power((0, 1), (-(2*m+1)) % 4))
    conductor_power = gaussian_power((34, 34), 2*m+1)
    numerator = gaussian_mul(canonical, (conductor_power[0], -conductor_power[1]))
    norm = conductor_power[0]**2+conductor_power[1]**2
    assert numerator[1] == 0
    e = numerator[0]/norm
    return e, {
        "m": m,
        "polynomial_terms": len(poly),
        "coefficient_common_denominator": denominator,
        "global_clearing_integer": clearing,
        "strict_complex_bound": str(height),
        "twice_cleared_bound_is_below_3_to_400": True,
        "raw_d_coordinates_1_i": [str(x) for x in raw],
        "canonical_e": str(e),
    }


def series_mul(a, b, order):
    return [sum((a[j]*b[n-j] for j in range(n+1)), F(0))
            for n in range(order)]


def series_power(a, exponent, order):
    """Binomial power of a unit series with constant coefficient one."""
    assert a[0] == 1
    u = list(a)
    u[0] = F(0)
    power = [F(1)]+[F(0)]*(order-1)
    result = list(power)
    binomial = F(1)
    for k in range(1, order):
        power = series_mul(power, u, order)
        binomial *= (exponent-k+1)/k
        result = [x+binomial*y for x, y in zip(result, power)]
    return result


def section_parameters(positive_b):
    """Exact triangular conversion, conditional only on the certified signs."""
    order = 5
    X = [F(1)]+wp[1:5]
    logarithm = [F(0)]+[-17*wp[n]/(4*n*(4*n-1)) for n in range(1, 5)]
    sigma17 = [F(1)]
    for n in range(1, order):
        sigma17.append(sum((j*logarithm[j]*sigma17[n-j]
                            for j in range(1, n+1)), F(0))/n)
    basis = {}
    for j in range(1, 5):
        unshifted = series_mul(sigma17, series_power(X, F(17-4*j, 2), order), order)
        basis[j] = [F(0)]*j+unshifted[:order-j]
    coefficients = {}
    for j in range(1, 5):
        coefficients[j] = positive_b[4*j]-sum(
            (coefficients[k]*basis[k][j] for k in coefficients), F(0))
    assert list(coefficients.values()) == [F(1), F(51, 5), F(-289, 5), F(4913, 5)]
    return [str(x) for x in coefficients.values()]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cached", type=Path)
    args = parser.parse_args()
    if args.cached:
        data = json.loads(args.cached.read_text())
    else:
        engine = Path(__file__).with_name("check-central-theta-inert.py")
        output = subprocess.run(
            [sys.executable, str(engine), "3", "16", str(PRECISION)],
            capture_output=True, text=True, check=True)
        data = json.loads(output.stdout)
    assert data["prime"] == 3 and data["ring_precision"] == PRECISION
    assert data["orbit_size"] == 256 and data["no_CLS_calibration"]
    values, rows = {}, []
    for m in WEIGHTS:
        value, row = global_reconstruction(m, data["rows"][m])
        values[m] = value
        rows.append(row)
    assert values[1] == F(4, 17**3)
    expected = {
        4: F(5**2, 2**9*17**10),
        8: F(97**2, 2**25*3**2*17**20),
        12: F((13*37*67)**2, 2**43*3**4*5**2*7**2*17**30),
        16: F((2659*10903)**2, 2**59*3**8*5**4*7**2*11**2*13**2*17**38),
    }
    for m, value in expected.items():
        assert values[m] == value
    positive_b = {
        4: F(1), 8: F(1649, 60), 12: F(9313603, 50400),
        16: F(2421363742117, 1297296000),
    }
    for m, b in positive_b.items():
        assert values[m]/values[4]*(17*2312)**(m-4) == b*b
    square_constant = values[4]*(17*2312)**4
    assert square_constant == 57800
    coefficients = section_parameters(positive_b)
    print(json.dumps({
        "status": "exact global traces and Taylor squares certified",
        "modulus": "3^400",
        "global_trace_certificates": rows,
        "positive_square_roots_certified_by_separate_gaussian_script": {
            str(m): str(b) for m, b in positive_b.items()},
        "section_coefficients_after_positive_sign_certificate": coefficients,
        "exact_central_square_constant": str(square_constant),
        "orbit_engine_seconds": data["elapsed_seconds"],
    }, indent=2))


if __name__ == "__main__":
    main()
