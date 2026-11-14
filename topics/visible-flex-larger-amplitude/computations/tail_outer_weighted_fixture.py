#!/usr/bin/env python3
"""Exact finite-polynomial fixture only; no real source or numerical flow.

Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
from fractions import Fraction as F
import json
from flint import ctx
from closure_real_head_source_enclosure import exact_q
from tail_outer_weighted_compatible import (
    make_weighted_candidate, weighted_panel_fields, cell_source_coordinate)


def main():
    ctx.prec = 192
    scale = F(1, 2**20)
    left = {"H": {2: 7*scale}, "K": {2: 5*scale}, "Ku": {2: 4*scale}}
    right = {"H": {2: F(122, 5)*scale}, "K": {2: 15*scale}, "Ku": {2: 20*scale}}
    bases = {"00": [1, 0, -3, 2], "10": [0, 1, -2, 1],
             "01": [0, 0, 3, -2], "11": [0, 0, 1, -1],
             "b": [0, 0, 1, -2, 1]}
    def moment(row, u):
        return sum((2*F(v)*u**(j+1)/(j+1) for j, v in enumerate(row)), F(0))
    total = {key: moment(row, F(1)) for key, row in bases.items()}
    candidate = make_weighted_candidate(left, right, total)
    checks = {"quartic_bubble": bool(
        candidate["bubble_coefficient"][2].contains(exact_q(scale)))}
    for u in (F(0), F(1, 3), F(1)):
        prefix = {key: moment(row, u) for key, row in bases.items()}
        suffix = {key: total[key]-prefix[key] for key in total}
        H, K, Kx = weighted_panel_fields(candidate, u=u, u_x=1,
                                        prefix_moments=prefix, suffix_moments=suffix)
        expected = {
            "H": (7+2*(u**5/5+u**4/2+u**3+2*u*u+5*u))*scale,
            "K": (u**4+2*u**3+3*u*u+4*u+5)*scale,
            "Kx": (4*u**3+6*u*u+6*u+4)*scale,
        }
        for name, field in (("H", H), ("K", K), ("Kx", Kx)):
            checks[f"{name}@{u}"] = bool(field[2].real.contains(exact_q(expected[name]/2)))
    u, ux = cell_source_coordinate(list(range(1, 10)), 4, F(1, 2))
    checks["unequal_source_coordinate"] = bool(
        u.contains(exact_q(F(5, 18))) and ux.contains(exact_q(F(1, 9))))
    if not all(checks.values()):
        raise AssertionError(checks)
    print(json.dumps(dict(scope="Constant positive weight and finite polynomial only",
                          checks=checks, all_passed=True, actual_source_evaluated=False)))


if __name__ == "__main__":
    main()
