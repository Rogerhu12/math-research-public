#!/usr/bin/env python3
"""Rational dual lower bound for all supported C3 curvature controls.

The seven physical low moments are frozen to the recorded old q=.04 state.
The function space is infinite dimensional: even C3 H2 support controls
vanishing on |phi-pi/3|<.21, with zero mean and primary moment.  A fixed
rational dual vector is certified using closed Green/Riesz integrals.
There is no floating inverse, quadrature, sampled extremum or BVP here.
"""
import argparse
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as F
from functools import lru_cache
import gzip
import hashlib
import json
import math
from pathlib import Path
import sys
import time

DIGITS = 80
DEN = 10**DIGITS
DEGREE = 200
N, M, A = 3, 8, F(21, 100)
DUAL = tuple(F(value) for value in (
    '788928.262860837', '-759591.044766777', '676940.171437999',
    '-555702.838249487', '416313.825141573', '-280027.372379647',
    '164205.493007490', '-79060.622577590', '26616.424412285'))


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def outward(lo, hi):
    lo, hi = F(lo), F(hi)
    return (F((lo.numerator*DEN)//lo.denominator, DEN),
            F(-((-hi.numerator*DEN)//hi.denominator), DEN))


def point(value):
    return outward(value, value)


def add(a, b):
    return outward(a[0]+b[0], a[1]+b[1])


def neg(a):
    return -a[1], -a[0]


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    values = [x*y for x in a for y in b]
    return outward(min(values), max(values))


def scale(a, value):
    value = F(value)
    return outward(a[0]*value, a[1]*value) if value >= 0 else outward(a[1]*value, a[0]*value)


def divide(a, b):
    if b[0] <= 0 <= b[1]:
        raise ArithmeticError('Interval denominator contains zero')
    return mul(a, outward(1/b[1], 1/b[0]))


def pi_interval():
    def atan(denominator):
        value = sum((F((-1)**j, (2*j+1)*denominator**(2*j+1))
                     for j in range(100)), F(0))
        next_term = F(1, 201*denominator**201)
        return outward(value, value+next_term)
    return sub(scale(atan(5), 16), scale(atan(239), 4))


def sincos(x):
    """Degree-200 Taylor polynomials, with their exact real remainder."""
    assert x[0] >= 0
    term, sine, cosine = point(1), point(0), point(0)
    for k in range(DEGREE+1):
        if k % 4 == 0:
            cosine = add(cosine, term)
        elif k % 4 == 1:
            sine = add(sine, term)
        elif k % 4 == 2:
            cosine = sub(cosine, term)
        else:
            sine = sub(sine, term)
        term = scale(mul(term, x), F(1, k+1))
    remainder = max(abs(term[0]), abs(term[1]))
    error = (-remainder, remainder)
    return add(sine, error), add(cosine, error)


def decimal(value, upper=False, digits=45):
    with localcontext() as context:
        context.prec = digits
        context.rounding = ROUND_CEILING if upper else ROUND_FLOOR
        return str(Decimal(value.numerator)/Decimal(value.denominator))


def show(interval):
    return [decimal(interval[0]), decimal(interval[1], True)]


def sqrt_lower(value, digits=40):
    scale = 10**digits
    integer = math.isqrt(value.numerator*scale**2//value.denominator)
    return F(integer, scale)


def gram_intervals():
    L = scale(pi_interval(), F(1, N))
    d = sub(L, point(A))
    sd, cd = sincos(d)
    determinant = add(d, mul(sd, cd))
    assert determinant[0] > 0
    frequencies, norms = [N*j for j in range(M+1)], [1]+[2]*M

    @lru_cache(None)
    def trig(k):
        return sincos(scale(d, k)) if k else (point(0), point(1))

    def S(k):
        return scale(trig(abs(k))[0], F(1, abs(k))) if k else d

    def Sprime(k):
        if not k:
            return point(0)
        sine, cosine = trig(abs(k))
        value = scale(sub(scale(mul(d, cosine), abs(k)), sine), F(1, k*k))
        return value if k > 0 else neg(value)

    def I(k, ell):
        return scale(add(S(k-ell), S(k+ell)), F(1, 2))

    def J(k, ell):
        return scale(sub(Sprime(k-ell), Sprime(k+ell)), F(1, 2))

    homogeneous = []
    for k, norm in zip(frequencies, norms):
        sine, cosine = trig(k)
        p = scale(cosine, F(norm, (1-k*k)**2))
        pp = scale(sine, F(-norm*k, (1-k*k)**2))
        aa = divide(add(neg(mul(add(sd, mul(d, cd)), p)), mul(mul(d, sd), pp)), determinant)
        bb = divide(neg(add(mul(sd, p), mul(cd, pp))), determinant)
        homogeneous.append((aa, bb))
    gram = []
    for k, norm in zip(frequencies, norms):
        row = []
        for ell, normj, (aa, bb) in zip(frequencies, norms, homogeneous):
            value = add(scale(I(k, ell), F(normj, (1-ell*ell)**2)),
                        add(mul(aa, I(k, 1)), mul(bb, J(k, 1))))
            row.append(divide(scale(value, norm), L))
        gram.append(row)
    # Exact symmetry is proved by the Riesz identity.  Intersections only
    # tighten existing enclosures of the same mathematical entry.
    for i in range(M+1):
        for j in range(i):
            value = max(gram[i][j][0], gram[j][i][0]), min(gram[i][j][1], gram[j][i][1])
            assert value[0] <= value[1]
            gram[i][j] = gram[j][i] = value
    return L, d, determinant, gram


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--control-record', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    record = json.loads(args.control_record.read_text())
    assert record['base_mode'] == N and record['modes'] == M
    assert F(str(record['halfwidth'])) == A and record['lock_fundamental']
    checkpoint = Path(record['input'])
    assert sha(checkpoint) == record['input_sha256']
    source = json.load(gzip.open(checkpoint, 'rt'))
    physical = [float(a*b) for a, b in zip(source['parameters'][1:], source['central_correction_scales'])]
    assert physical == record['physical_corrections'] and len(physical) == M-1
    moments = (F(0), F(0), *(F.from_float(value) for value in physical))
    numerator = sum((a*b for a, b in zip(DUAL, moments)), F(0))
    L, d, determinant, gram = gram_intervals()
    denominator = point(0)
    for i in range(M+1):
        for j in range(M+1):
            denominator = add(denominator, scale(gram[i][j], DUAL[i]*DUAL[j]))
    assert denominator[0] > 0 and numerator != 0
    dual = divide(point(numerator*numerator), denominator)
    rms = sqrt_lower(dual[0])
    linf_squared = divide(mul(point(dual[0]), L), d)
    linf = sqrt_lower(linf_squared[0])
    assert dual[0] > F(decimal(dual[0]))
    assert rms*rms < dual[0] and linf*linf < linf_squared[0]
    thresholds = dict(normalized_energy=F('144.10413879'),
                      rms=F('12.00433833'), linf=F('13.42575017'))
    assert dual[0] > thresholds['normalized_energy']
    assert rms > thresholds['rms']
    assert linf > thresholds['linf']
    result = dict(
        scope=__doc__, command=sys.argv, source_sha256=sha(__file__),
        input_record_sha256=sha(args.control_record), checkpoint_sha256=sha(checkpoint),
        input_q=source['actual_primary_amplitude'], n=N, maximum_low_mode=M,
        protected_halfwidth=str(A), exact_physical_binary64_moments=[str(v) for v in moments],
        rational_dual=[str(v) for v in DUAL],
        normalization='B(b,b)=(1/T) integral_0^T (b+b_second)^2, T=2*pi/3',
        L=show(L), complement_half_length=show(d), homogeneous_determinant=show(determinant),
        exact_dual_linear_functional=str(numerator),
        dual_quadratic=show(denominator), fixed_dual_value=show(dual),
        rigorous_energy_lower=decimal(dual[0]), rigorous_rms_lower=decimal(rms),
        rigorous_linf_lower=decimal(linf), certified_strict_thresholds={k: str(v) for k, v in thresholds.items()},
        gram= [[show(value) for value in row] for row in gram],
        proof_arithmetic=dict(outward_decimal_digits=DIGITS, sine_cosine_taylor_degree=DEGREE,
                              machin_atan_terms=100, all_bound_arithmetic='Fraction and integer floor/ceiling'),
        complete_infinite_dimensional_variational_formula='inf B(b,b) = moments^T G^-1 moments',
        fixed_dual_needs_no_numerical_inverse=True,
        restrictions='Frozen old low moments only; no positivity nonexistence claim and no restriction on controls being re-solved in a new actual homotopy.',
        seconds=time.monotonic()-started)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({key: result[key] for key in (
        'rigorous_energy_lower', 'rigorous_rms_lower', 'rigorous_linf_lower',
        'certified_strict_thresholds', 'seconds')}), flush=True)


if __name__ == '__main__':
    main()
