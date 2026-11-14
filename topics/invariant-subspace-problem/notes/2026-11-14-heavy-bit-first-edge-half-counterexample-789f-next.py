"""Exact full symmetric-input certificate for a real Boolean first edge > 1/2."""
from fractions import Fraction as Q
from math import comb

HEADS = (frozenset(), frozenset((0,)), frozenset((1,)), frozenset((0, 1)))
WEIGHTS = (Q(4), Q(4))
POOL = 6
BIRTH = 2


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def matrix(height):
    result = []
    for source in HEADS:
        row = []
        pool_target = BIRTH-len(source)
        for target in HEADS:
            value = Q(0)
            if source <= target:
                deleted = target-source
                value = Q(choose(POOL-pool_target, height-len(deleted)))
                for bit in deleted:
                    value *= WEIGHTS[bit]
            row.append(value)
        result.append(row)
    return result


def solve(a, b):
    m = [list(row)+[entry] for row, entry in zip(a, b)]
    n = len(b)
    for j in range(n):
        pivot = next(i for i in range(j, n) if m[i][j])
        m[j], m[pivot] = m[pivot], m[j]
        p = m[j][j]
        m[j] = [v/p for v in m[j]]
        for i in range(n):
            if i != j:
                c = m[i][j]
                m[i] = [x-c*y for x, y in zip(m[i], m[j])]
    return [row[-1] for row in m]


def main():
    a, b = WEIGHTS
    source = [a*b/15, -b/6, -a/6, Q(1)]
    assert 5*source[0]+a*source[1]+b*source[2] == 0
    assert 6*source[1]+b*source[3] == 0
    assert 6*source[2]+a*source[3] == 0
    grams = []
    for height in range(3):
        actual = matrix(height)
        lift = solve(actual, source)
        assert all(sum(x*y for x, y in zip(row, lift)) == v
                   for row, v in zip(actual, source))
        cost = sum(value**2*choose(POOL, BIRTH+height-len(head))
                   for value, head in zip(lift, HEADS))
        grams.append(cost)
    assert grams == [Q(117, 5), Q(151, 10), Q(281, 15)]
    ratio = grams[1]**2/(grams[0]*grams[2])
    assert ratio == Q(22801, 43836) and ratio > Q(1, 2) and ratio < 1
    print("exact grams:", ", ".join(map(str, grams)))
    print("exact first-edge ratio:", ratio)
    print("PASS: actual N=8, birth=2, weights=(4,4,1,1,1,1,1,1) exceeds 1/2")


if __name__ == "__main__":
    main()
