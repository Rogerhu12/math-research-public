#!/usr/bin/env python3
"""Exact point witness against the global R10 support threshold at c=.35.

No candidate, BVP, numerical optimization or geometric integration is used.
"""
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', type=Path, required=True)
    a = ap.parse_args()
    topic = Path(__file__).resolve().parents[1]
    source_path = topic/'notes/2026-11-09-db6f-audit-poisson-twin-marker-bounds.json'
    raw = source_path.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == '9da6b3d013524995a831e5b55fe9d06b017957bbb87fd9b38fe093c7da8207ef'
    source = json.loads(raw)

    def frac(x):
        return Q(int(x['numerator']), int(x['denominator']))

    def enc(x):
        if isinstance(x, Q):
            return dict(numerator=str(x.numerator), denominator=str(x.denominator))
        if isinstance(x, dict):
            return {k: enc(v) for k, v in x.items()}
        return x

    hl = frac(source['source_bounds']['H_lower'])
    hu = frac(source['source_bounds']['H_upper'])
    ll = frac(source['witness_and_enclosures']['L0_lower'])
    lu = frac(source['witness_and_enclosures']['L0_upper'])
    assert 0 < hl <= hu and 0 < ll <= lu
    # q=(-X,0,Z) is the unchanged exact spherical-cap axis point.
    Xl, Xu = hl+hl/(5*lu), hu+hu/(5*ll)
    Zl, Zu = Q(3, 10)+Q(31, 1000)/lu, Q(3, 10)+Q(31, 1000)/ll
    # p=(-7/20,0,1/10), lambda=1/4, b=(p-lambda*q)/(1-lambda).
    bx_l, bx_u = (Xl-Q(7, 5))/3, (Xu-Q(7, 5))/3
    bz_l, bz_u = (Q(2, 5)-Zu)/3, (Q(2, 5)-Zl)/3
    assert bx_l <= bx_u < 0 < bz_l <= bz_u
    norm2_upper = max(bx_l*bx_l, bx_u*bx_u)+max(bz_l*bz_l, bz_u*bz_u)
    support_test = Q(1, 20)
    reach_goal = Q(189, 2500)
    assert norm2_upper < support_test**2 < reach_goal**2
    assert Q(34, 100) < Q(7, 20) < Q(36, 100)
    result = dict(status='EXACT_POINT_WITNESS_AGAINST_GLOBAL_SUPPORT_AT_LEAST_ONE_TWENTIETH',
                  source=dict(path=str(source_path.relative_to(topic)), bytes=len(raw),
                              sha256=hashlib.sha256(raw).hexdigest()),
                  script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  annulus_point=dict(x=-Q(7, 20), y=Q(0), z=Q(1, 10)),
                  convex_weight=Q(1, 4),
                  center_bounds=dict(x_lower=bx_l, x_upper=bx_u,
                                     y=Q(0), z_lower=bz_l, z_upper=bz_u),
                  center_squared_norm_upper=norm2_upper,
                  strict_norm_less_than=support_test, R10_goal=reach_goal,
                  candidate_or_solver_calls=0,
                  scope='Excludes only a closed connected completion with global x dot N >= 1/20 containing both exact points. Does not exclude positive support without this bound, or a reach proof by another route.')
    with a.out.open('x') as f:
        json.dump(enc(result), f, indent=2, ensure_ascii=False)
        f.write('\n')
    print(json.dumps(dict(status=result['status'], center_norm_squared_upper=float(norm2_upper),
                          strict_norm_less_than=float(support_test),
                          report_bytes=a.out.stat().st_size,
                          report_sha256=hashlib.sha256(a.out.read_bytes()).hexdigest())))


if __name__ == '__main__':
    main()
