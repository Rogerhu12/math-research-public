#!/usr/bin/env python3
"""Check R417's actual source labels and its exact Schur invariant.

The proof is uniform in s.  Two actual p^3 matrices only check normalization,
the carry convention, and the claimed full Smith counts.
"""
from fractions import Fraction
import importlib.util
from pathlib import Path


def selected_labels(s, ell, budget):
    assert s >= 15 and 1 <= ell < s - 13 and budget >= s - 8
    chosen = [(0, 0, 0), (1, 0, 0)]
    for r in range(1, s):
        if r < ell:
            labels = [(0, 1, r - 1), (1, 1, r - 1), (0, 0, r)]
        elif r <= budget:
            labels = [(0, 0, r), (1, 0, r)]
        else:
            labels = [(1, r - budget, budget), (1, r - budget + 1, budget - 1)]
        for n, k, j in labels:
            assert n in (0, 1)
            assert 0 <= k <= (4 if n == 0 else 8)
            assert 0 <= j <= budget and k + j == r
        charges = [Fraction(n) + Fraction(36, 17) * j for n, k, j in labels]
        assert len(set(charges)) == len(charges)
        chosen.extend(labels)
    assert len(chosen) == 2 * s + ell - 1
    assert len(set(chosen)) == len(chosen)
    return chosen


def check_algebra():
    alpha = Fraction(36, 17)
    assert Fraction(1, 2) + alpha * (Fraction(1, 6) - 8) == Fraction(-547, 34)
    assert all(547 % d for d in range(2, 24)) and 547 % 6 == 1
    assert alpha * (alpha - 1) / 2 == Fraction(342, 289)
    for s in range(15, 61):
        for ell in (1, s - 14):
            for budget in (s - 8, s - 1, s + 3):
                selected_labels(s, ell, budget)
        L = 2 * s + 1
        boundary = [r for r in range(L) if (r + 13) // s - r // s]
        assert len(boundary) == 26 and s not in boundary and 2 * s not in boundary


def check_actual(p, ell):
    path = Path(__file__).with_name("explore-rank2-actual-small-source-smith.py")
    spec = importlib.util.spec_from_file_location("actual_three_blocks", path)
    actual = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(actual)
    G = actual.ThreeBlocks(p, ell)
    G.initialize()
    budget = G.s - 8
    cols, labels = G.columns(1, budget)
    witness = cols[labels.index((1, 8, budget))]
    assert all(x % p == 0 for x in witness)
    pairing = (witness[2 * G.s] - G.ap * pow(2, -1, G.mod) * witness[G.s]) % G.mod
    assert pairing % p == 0
    assert (pairing // p) % p == -547 * G.ap * pow(34, -1, p) % p
    assert pairing % (p * p)
    rows = [[c[r] for c in cols] for r in range(G.L)]
    jc, jr, _ = actual.smith_counts(rows, p)
    assert jc == [G.L - 1, 1, 0] and jr == 0, (p, ell, jc, jr)
    shifted = [[0] * len(cols) for _ in range(G.L + 13)]
    for r, row in enumerate(rows):
        factor = p ** ((r + 13) // G.s - r // G.s)
        shifted[r + 13] = [factor * x % G.mod for x in row]
    mc, mr, _ = actual.smith_counts(shifted, p)
    assert mc == [G.L - 27, 27, 0] and mr == 13, (p, ell, mc, mr)
    return {"p": p, "ell": ell, "J": budget, "J_smith": jc, "M_smith": mc}


if __name__ == "__main__":
    check_algebra()
    for parameters in ((89, 1), (113, 5)):
        print(check_actual(*parameters))
    print("R417: all checks passed")
