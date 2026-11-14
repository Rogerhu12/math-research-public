#!/usr/bin/env python3
"""Recompute the exact finite-field certificate for R95, using only stdlib.

--check compares with the committed certificate.  --write refreshes that file.
The uniform-in-p conclusion is proved in R95; the model enumeration uses p=43.
"""
import sys
sys.dont_write_bytecode = True

import argparse
from collections import Counter
from math import isqrt, prod
from pathlib import Path
import json


def is_prime(n):
    if n < 2:
        return False
    return all(n % d for d in range(2, isqrt(n) + 1))


def compute():
    ell = 1033
    exponent = 43
    assert is_prime(ell)
    primes = [r for r in range(2, 462) if is_prime(r)]
    n = 116 * prod(primes)
    q = 432 * n * n - 1
    z = (-q) % ell
    assert n % ell == 598 and q % ell == 810 and z == 223

    character = [0] + [-1] * (ell - 1)
    roots = [[] for _ in range(ell)]
    for x in range(ell):
        roots[x * x % ell].append(x)
        if x:
            character[x * x % ell] = 1
    cubes = [x * x * x % ell for x in range(ell)]

    def trace_and_roots(a, b):
        trace = 0
        root_count = 0
        for x in range(ell):
            value = (cubes[x] + a * x + b) % ell
            trace -= character[value]
            root_count += value == 0
        return trace, root_count

    trace_a, roots_a = trace_and_roots(-1, 0)
    assert trace_a == -6 and roots_a == 3
    hasse = isqrt(4 * ell)
    admissible = [t for t in range(-hasse, hasse + 1)
                  if (t - trace_a) % exponent == 0]
    assert admissible == [-49, -6, 37]

    square_classes = {a for a in range(1, ell)
                      if pow(a, (ell - 1) // 2, ell) == 1}
    cube_classes = {a for a in range(1, ell)
                    if pow(a, (ell - 1) // 3, ell) == 1}
    excluded = set(range(1, ell)) - square_classes - cube_classes
    assert (len(square_classes), len(cube_classes),
            len(square_classes & cube_classes), len(excluded)) == (516, 344, 172, 344)
    assert z in excluded and (-z) % ell in excluded

    base_rhs = pow(z, exponent, ell)
    assert base_rhs == 135
    inv27 = pow(27, -1, ell)
    families = {}
    for name, multiplier, a_scale, b_scale, delta in [
        ("I", 1, -1, -2, 6),
        ("II", 8, -1, -2, 9),
        ("III", 1, -4, -16, 12),
    ]:
        rhs = multiplier * base_rhs % ell
        expected_discriminant = pow(2, delta, ell) * base_rhs % ell
        traces = Counter()
        two_root_counts = Counter()
        survivors = []
        count = 0
        for x in range(ell):
            w_square = (cubes[x] - rhs) * inv27 % ell
            for w in roots[w_square]:
                assert (x ** 3 - 27 * w * w - rhs) % ell == 0
                a, b = a_scale * x % ell, b_scale * w % ell
                discriminant = -16 * (4 * a ** 3 + 27 * b * b) % ell
                assert discriminant == expected_discriminant != 0
                trace, root_count = trace_and_roots(a, b)
                assert abs(trace) <= hasse
                traces[trace] += 1
                two_root_counts[root_count] += 1
                count += 1
                if (trace - trace_a) % exponent == 0:
                    survivors.append([x, w, trace])
        assert count == 1086
        assert two_root_counts == {1: 1086}
        assert {t % 6 for t in traces} == {2, 4}
        assert not survivors
        families[name] = {
            "rhs": rhs,
            "model_a4_scale": a_scale,
            "model_a6_scale": b_scale,
            "discriminant": expected_discriminant,
            "local_model_count": count,
            "two_division_root_counts": {str(k): two_root_counts[k]
                                         for k in sorted(two_root_counts)},
            "trace_histogram": {str(k): traces[k] for k in sorted(traces)},
            "trace_classes_mod_6": sorted({t % 6 for t in traces}),
            "mod_43_survivors": survivors,
        }
    assert [families[k]["discriminant"] for k in ("I", "II", "III")] == [376, 942, 305]
    assert families["I"]["trace_histogram"] == families["II"]["trace_histogram"]
    assert families["I"]["trace_histogram"] == families["III"]["trace_histogram"]

    return {
        "schema": "r95-1033-stdlib-v2-reconstructed",
        "ell": ell,
        "ell_primality_method": "trial division through floor(sqrt(ell))",
        "A_point_count": ell + 1 - trace_a,
        "A_trace": trace_a,
        "hasse_integer_bound": hasse,
        "uniform_prime_bound_check": {"minimum_prime_gt_37": 41,
                                      "twice_minimum_prime": 82,
                                      "maximum_absolute_trace_difference": 70},
        "residue_class_counts": {"nonzero": ell - 1,
                                 "squares": len(square_classes),
                                 "cubes": len(cube_classes),
                                 "sixth_powers": len(square_classes & cube_classes),
                                 "excluded": len(excluded)},
        "R53_parameters_mod_ell": {"primorial_cutoff": 461,
                                   "primorial_prime_count": len(primes),
                                   "n": n % ell,
                                   "q": q % ell,
                                   "minus_q": z,
                                   "minus_q_power_516": pow(z, 516, ell),
                                   "minus_q_power_344": pow(z, 344, ell),
                                   "q_power_516": pow(q, 516, ell),
                                   "q_power_344": pow(q, 344, ell)},
        "enumeration_exponent": exponent,
        "hasse_traces_congruent_to_A_mod_43": admissible,
        "even_hasse_traces_congruent_to_A_mod_43": [t for t in admissible if t % 2 == 0],
        "families": families,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--check", action="store_true")
    modes.add_argument("--write", action="store_true")
    args = parser.parse_args()
    certificate = compute()
    path = Path(__file__).with_name("r95_all_branches_at_1033_certificate.json")
    if args.check:
        expected = json.loads(path.read_text(encoding="utf-8"))
        assert certificate == expected, "certificate mismatch"
        print("R95: exact certificate verified; 1086 models per family; no mod-43 survivors.")
    elif args.write:
        path.write_text(json.dumps(certificate, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("R95: wrote recomputed certificate.")
    else:
        print(json.dumps(certificate, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
