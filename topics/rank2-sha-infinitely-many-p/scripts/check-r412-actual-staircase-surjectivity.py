#!/usr/bin/env python3
"""Exact finite bookkeeping for R412's parameter proof (no prime search)."""
import json


def A(n):
    return (n+1)//4


def e(m):
    return 3*((3*m+3)//4)+2*((m+1)//2)+(2*m+2)//3-2


def b(n):
    return A(n)+e(n+1)


def rho(r):
    n = 0
    while b(n) < r:
        n += 1
    return n


table = [b(n)-4*n for n in range(12)]
assert table == [4,4,5,3,5,4,6,4,5,5,7,4]
for n in range(12):
    assert b(n+12) == b(n)+50
    assert b(n+1) > b(n)


def staircase(s, ell):
    D = max(1+rho(s-1), 2+rho(ell-1))
    selected = []
    for r in range(s):
        m = 3 if r < ell else 2
        first = rho(r)
        for n in range(first, first+m):
            angular_power = r-A(n)
            assert n <= D
            assert 0 <= angular_power <= e(n+1)
            selected.append((n, angular_power))
    assert len(selected) == len(set(selected)) == 2*s+ell
    L = 2*s+ell
    delta = [(r+13)//s-r//s for r in range(L)]
    assert delta.count(1) == 26
    assert delta.count(0) == L-26
    return {"s": s, "ell": ell, "D_star": D, "L": L,
            "unit_factors": L-26, "p_factors": 26,
            "free_cokernel_rank": 13,
            "selected_column_count": len(selected)}


# These are block lengths, not a search over arithmetic target primes.
examples = [staircase(17,1), staircase(30,10), staircase(60,40)]
print(json.dumps({"status": "passed", "floor_table": table,
                  "block_examples": examples}, indent=2))
