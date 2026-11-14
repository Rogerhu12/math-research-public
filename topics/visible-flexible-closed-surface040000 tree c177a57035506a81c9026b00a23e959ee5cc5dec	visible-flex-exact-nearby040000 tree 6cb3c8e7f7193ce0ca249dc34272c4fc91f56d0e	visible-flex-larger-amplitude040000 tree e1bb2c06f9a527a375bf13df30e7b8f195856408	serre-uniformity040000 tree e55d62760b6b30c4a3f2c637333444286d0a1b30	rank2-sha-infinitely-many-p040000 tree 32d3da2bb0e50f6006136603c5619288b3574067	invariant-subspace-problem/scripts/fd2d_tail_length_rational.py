#!/usr/bin/env python3
"""Rational comparisons for the cuff .32 / cut .4 tail-length lemma.

The accompanying proof bounds the exact profile, including its unchanged
infinite source.  No quadrature value is promoted to a rigorous interval.
The input is the intended monotone radial construction with a positive exact
warp normalization and the existing deep calibration bracket [1/2, 2].
This calculation does not certify that normalization, a nonlinear tail map,
or a closed surface.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def pack(x):
    return dict(numerator=str(x.numerator), denominator=str(x.denominator),
                display=float(x))


def atan_partial(x, terms):
    return sum(((-1) ** k * x ** (2 * k + 1) / (2 * k + 1)
                for k in range(terms)), F(0))


def certificate(config):
    p = json.loads(config.read_text())
    assert p['orientation'] == 1 and p['capMode'] == 'cut-preserving'
    assert p['protectCell'] == 160 and p.get('rejoinR20At') is None
    assert p.get('flatOuterThroughCell') is None
    assert p.get('prefixEtaMultiplier', 1) == 1
    wc, cap = F(p['wCut']), F(p['slopeCap'])
    d0, c0 = F(p.get('delta0', .006)), F(p.get('etaRatioAtN0', .05))
    assert F(p.get('a', 2.75)) == F(11, 4)
    assert p.get('R', 64) == 64
    assert F(1, 200) <= d0 <= F(1, 160)
    assert F(1, 25) <= c0 <= F(1, 16)
    assert wc <= F(1, 2)
    assert d0 < F(7, 1000) and c0 < F(51, 1000)
    # The last transition has cap level cap at both of its endpoints.
    assert F(p['pulseCaps'][0][1]) == cap
    assert (d0 * wc / cap) ** 4 * 2 ** 11 > 1
    caps = [cap]
    caps += [F(v) for row in p.get('pulseCaps', []) for v in row]
    caps += [F(v) for v in p.get('valleyCaps', [])]
    assert max(caps) < F(81, 1000)

    # The two final source segments have total log-radius length
    # 2*c0*d0/sqrt(12).  exp(x) <= 1/(1-x) for 0 <= x < 1.
    sqrt12_lower = F(433, 125)
    assert sqrt12_lower ** 2 < 12
    exponent_upper = 14 * c0 * d0 / sqrt12_lower
    assert 0 < exponent_upper < 1
    slope_upper = wc / (1 - exponent_upper)
    simple_slope_upper = F(50061, 500000)  # .100122
    assert slope_upper < simple_slope_upper

    # R15 section 2.2 uses only the uniform d0,c0 box, the source exponent,
    # R=64, and wc<=1/2 for this raw slope bound.  Changing cuff radius
    # cancels between the source normalization and r^-7.
    deep_slope_upper = F(1280, 2 ** 280)
    assert deep_slope_upper < cap < simple_slope_upper

    # Use the actual binary64 endpoint convention of the source assembler.
    rc = float(p['rCut']) - float(p['width'])
    radial_width = F(p['rCut']) - F(rc)
    assert radial_width <= F(800000000000001, 10 ** 16)
    length_upper = F(201, 2500)  # .0804
    assert radial_width ** 2 * (1 + simple_slope_upper ** 2) < length_upper ** 2

    # Machin's identity and alternating-series bounds give an exact pi lower
    # bound.  An even number of terms is lower, an odd number is upper.
    pi_lower = 16 * atan_partial(F(1, 5), 12) - 4 * atan_partial(F(1, 239), 5)
    assert pi_lower > F(314159, 100000)
    cosine_upper = 4 * length_upper / pi_lower
    assert cosine_upper < F(102369, 10 ** 6)
    return dict(
        schema='fd2d-tail-length-rational-v1', source_sha256=digest(__file__),
        config_file=config.name, config_sha256=digest(config),
        proof_file='2026-11-12-fd2d-geometry-tail-length-necessary-bound.md',
        scope=__doc__,
        assumptions=[
            'Exact positive monotone radial warp with the stated source and cut/cuff endpoints.',
            'Unchanged n>=160 source uses the existing exact calibration bracket [1/2,2].',
            'The actual surface, if supplied, obeys the same material metric and a constant cuff height.'
        ],
        comparisons={
            'actual_binary_radial_width': pack(radial_width),
            'cut_restore_exponent_upper': pack(exponent_upper),
            'slope_upper_from_geometric_series': pack(slope_upper),
            'simple_global_slope_upper': pack(simple_slope_upper),
            'unchanged_deep_slope_upper': pack(deep_slope_upper),
            'strict_length_upper': pack(length_upper),
            'pi_lower': pack(pi_lower),
            'strict_material_cosine_coefficient_upper': pack(F(102369, 10 ** 6))
        },
        passed=True, finite_quadrature_used=False,
        warp_normalization_certified=False, nonlinear_tail_certified=False,
        full_core_geometry_certified=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path,
        default=ROOT/'notes/2026-11-12-fd2d-ellipse-cuff032-cut04-config.json')
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    report = certificate(args.config)
    args.out.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(dict(out=str(args.out), passed=report['passed'],
        length_upper='.0804', material_cosine_upper='.102369',
        finite_quadrature_used=False)))


if __name__ == '__main__':
    main()
