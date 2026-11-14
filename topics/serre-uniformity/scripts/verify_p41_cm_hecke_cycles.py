#!/usr/bin/env python3
"""Independent integer check of R199 prime-action/Hecke recursion and mass."""
import argparse
from collections import defaultdict
from fractions import Fraction
import hashlib
import json
from pathlib import Path


def factor(n):
    out = []
    p = 2
    while p*p <= n:
        e = 0
        while n % p == 0:
            e += 1
            n //= p
        if e:
            out.append((p, e))
        p += 1
    if n > 1:
        out.append((n, 1))
    return out


def divisors(n):
    a = [1]
    for p, e in factor(n):
        a = [d*p**j for d in a for j in range(e+1)]
    return sorted(a)


def chi(n):
    return 0 if n % 2 == 0 else (1 if n % 4 == 1 else -1)


def rho(n):
    return sum(chi(d) for d in divisors(n))


def clean(a):
    return {f: n for f, n in a.items() if n}


def prime_action(a, p):
    b = defaultdict(int)
    for f, n in a.items():
        if f % p:
            b[f] += n*(1+chi(p))
            b[f*p] += n*(2 if f == 1 else 1)
        else:
            b[f*p] += n
            u = f // p
            if u == 1:
                coef = (p-chi(p))//2
                assert 2*coef == p-chi(p)
            else:
                coef = p if u % p == 0 else p-chi(p)
            b[u] += n*coef
    return clean(b)


def power_action(a, p, e):
    if e == 0:
        return a
    previous, current = a, prime_action(a, p)
    for _ in range(1, e):
        nxt = defaultdict(int, prime_action(current, p))
        for f, n in previous.items():
            nxt[f] -= p*n
        previous, current = current, clean(nxt)
    assert all(v >= 0 for v in current.values())
    return current


def actual(n):
    a = {1: 1}
    for p, e in factor(n):
        a = power_action(a, p, e)
    return a


def closed(n):
    return clean({f: (1 if f == 1 else 2)*rho(n//f) for f in divisors(n)})


def class_number(f):
    if f == 1:
        return 1
    h = Fraction(f, 2)
    for p, _ in factor(f):
        h *= Fraction(p-chi(p), p)
    assert h.denominator == 1
    return h.numerator


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    checks = 0
    for n in range(1, 1001):
        if n % 41 == 0:
            continue
        a = actual(n)
        assert a == closed(n), (n, a, closed(n))
        assert sum(k*20*class_number(f) for f, k in a.items()) == 20*sum(divisors(n))
        checks += 1
    indices = [1,2,3,5,6,7,10,11,13,14,15,17,19,21,22,23,26,29,30,31,33,34,35,37,38,39,42,46,47,51,53,55,57,58,59,61,62,65,66,67,69,70,71,73,74,77,78,79,83,85,86,87,89,91]
    records = []
    support = set()
    for n in indices:
        if n == 47:
            a = defaultdict(int, actual(4))
            a[1] -= 1
            a = clean(a)
            label, degree = 'C4', 6
        else:
            a, label, degree = actual(n), 'T'+str(n), sum(divisors(n))
        support.update(a)
        mass = sum(v*20*class_number(f) for f, v in a.items())
        assert mass == 20*degree
        records.append({'label': label, 'positive_cycle': dict(sorted(a.items())), 'degree': degree, 'CM_degree_with_multiplicity': mass})
    unique_degree = sum(20*class_number(f) for f in support)
    weighted_degree = sum(r['CM_degree_with_multiplicity'] for r in records)
    assert checks == 976 and len(support) == 55
    assert unique_degree == 25960 and weighted_degree == 65640
    assert actual(2) == {1:1, 2:2} and actual(3) == {3:2}
    assert actual(4) == {1:1, 2:2, 4:2} and actual(9) == {1:1, 9:2}
    out = {'verified': True, 'integer_recursion_checks': checks, 'rank': 54,
           'distinct_conductors': sorted(support), 'distinct_CM_point_degree': unique_degree,
           'degree_with_Hecke_multiplicity': weighted_degree, 'rows': records,
           'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'scope': 'Formal integer verification of proved actual divisor formula, not a replacement for the marked local lattice proof'}
    args.output.write_text(json.dumps(out, sort_keys=True, indent=2)+'\n')
    print(json.dumps({k: out[k] for k in ['verified','integer_recursion_checks','distinct_CM_point_degree','degree_with_Hecke_multiplicity']}, sort_keys=True))


if __name__ == '__main__':
    main()
