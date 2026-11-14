"""Rescale the audited N160 deep-background certificate in the cuff radius.

The cut slope, delta sequence and R,a stay fixed. Source normalization epsilon
scales exactly as r_c**7; consequently W_n is radius-independent, B_n is
proportional to 1/r_c, and the remaining height bound is proportional to r_c.
Only the unchanged rotational background is certified.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import sys
from closing_deep_background_rational import run as audited_default


def exact(entry):
    return F(int(entry['numerator']), int(entry['denominator']))


def show(value):
    return {'numerator': str(value.numerator), 'denominator': str(value.denominator),
            'approx': float(value)}


def run():
    source = audited_default()
    old_radius = F(1, 4)
    curvature = exact(source['meridian_curvature_upper'])
    angular = exact(source['angular_curvature_upper'])
    height = exact(source['remaining_height_upper'])
    rows = []
    for radius, strict_bound in [(F(1, 10), F(1, 20)), (F(3, 20), F(1, 30)),
                                 (F(1, 5), F(1, 40)), (F(1, 4), F(1, 50)),
                                 (F(7, 20), F(1, 70))]:
        k = curvature * old_radius / radius
        a = angular * old_radius / radius
        h = height * radius / old_radius
        assert k < strict_bound
        assert a < F(1, 10**79)
        assert h < F(1, 10**131)
        rows.append({'rCuff': str(radius), 'meridian_curvature_upper': show(k),
                     'strict_meridian_bound': str(strict_bound),
                     'angular_curvature_upper': show(a), 'remaining_height_upper': show(h)})
    assert curvature * old_radius / F(1, 10) < F(1, 20)
    return {
        'scope': 'Exact-rational rescaling of the audited unchanged n>=160 rotational background only; finite warp and nonrotational perturbation remain separate.',
        'source_r28_blob': source['source_r28_blob'],
        'parameters': {'rCuff_range': ['1/10', '7/20'], 'wCut': '1/2',
                       'delta0': '3/500', 'R': 64, 'a': '11/4', 'N': 160},
        'uniform_strict_meridian_bound': '1/20',
        'radius_scaling': {'epsilon': 'r_c^7', 'W_n': 'r_c^0', 'B_n': 'r_c^-1',
                           'remaining_height_bound': 'r_c'},
        'rows': rows,
        'conclusion': 'Every radius 1/10 <= r_c <= 7/20 has deep background |kappa_mer|<.05 and a C2 flat disk join; r_c=3/20 has |kappa_mer|<1/30.'
    }


if __name__ == '__main__':
    result = run()
    text = json.dumps(result, indent=2) + '\n'
    if len(sys.argv) > 1:
        Path(sys.argv[1]).write_text(text)
    print(text)
