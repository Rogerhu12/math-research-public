#!/usr/bin/env python3
"""Original E21609 complete analytic L'(1) certificate; public Actions only.

The fixed character is reconstructed from all 54 wild-three units, the
complete dyadic character and both split-seven residue embeddings.  All good
Euler coefficients are obtained from this character, checked on all six
associates and conjugation.  No database, point-count table, stored Fourier
coefficient or floating point L-value enters the calculation.
"""
from __future__ import annotations
import hashlib
import json
import math
import os
from pathlib import Path
import time

if os.environ.get("GITHUB_ACTIONS") != "true":
    raise RuntimeError("Mathematical execution requires public GitHub Actions.")
if os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
    raise RuntimeError("The original public repository is required.")
import flint
from flint import fmpq as Q
if flint.__version__ != "0.9.0":
    raise RuntimeError("python-flint==0.9.0 is required.")

START = time.monotonic()
CUTOFF = 1024
E1_TERMS = 144
DEN = 10**18
LEVEL = 47628
BAD = {2, 3, 7}
REPO = Path(__file__).resolve().parents[3]
PREFIX = "topics/rank2-sha-infinitely-many-p/"
PINS = (
    (PREFIX + "results/R302-jzero-original-degree-two-reference-and-exact-full-weight-square.md",
     "bd3204188d1c795053d4e0b15ebdef082cd688a918d3dae4b87f17b8bd549507"),
    (PREFIX + "results/R391-e24-original-wild-three-schwartz-and-heisenberg-transport.md",
     "5ee9acc1a7efb4374ed53a91bcca49d6fff0e4d951e20734ffbd4c027dc24cf9"),
    (PREFIX + "results/R1038-e3969-two-independent-points-and-complete-cm-character.md",
     "e0b474e876efc74af006e151d45293aa9f7a31aaa5dbb7d91a7f3bf5b1f3a950"),
    (PREFIX + "scripts/check-r732-two-cubic-rank-one-bounds.py",
     "abc12f49db1818351534889f31bd9b7bac7876a78cbd043a060834d97c2a8289"),
)
verified_pins = []
for rel, expected in PINS:
    raw = (REPO / rel).read_bytes()
    actual = hashlib.sha256(raw).hexdigest()
    if actual != expected:
        raise RuntimeError("Original input pin changed: " + rel)
    verified_pins.append({"path": rel, "bytes": len(raw), "sha256": actual})

def digest(obj):
    raw = json.dumps(obj, separators=(",", ":"), ensure_ascii=True).encode()
    return hashlib.sha256(raw).hexdigest()

def emul(a, b):
    x, y = a
    u, v = b
    return (x * u - y * v, x * v + y * u - y * v)

def econj(a):
    x, y = a
    return (x - y, -y)

def enorm(a):
    x, y = a
    return x * x - x * y + y * y

def escale(a, n):
    return (n * a[0], n * a[1])

def modpair(a, modulus):
    return (a[0] % modulus, a[1] % modulus)

def mmul(a, b, modulus):
    return modpair(emul(a, b), modulus)

def mpow(a, n, modulus):
    out = (1, 0)
    while n:
        if n & 1:
            out = mmul(out, a, modulus)
        a = mmul(a, a, modulus)
        n >>= 1
    return out

OMEGA = (0, 1)
OMEGA_POWERS = ((1, 0), (0, 1), (-1, -1))
UNITS = ((1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1))

# Full local O_K/(9) unit table: u=q*omega^j*g^k, g=1-3delta.
g = (7, 3)
rational_units = (1, 2, 4, 5, 7, 8)
table3 = {}
decomposition3 = {}
for q in rational_units:
    for j in range(3):
        for k in range(3):
            u = mmul((q, 0), mmul(mpow(OMEGA, j, 9), mpow(g, k, 9), 9), 9)
            assert u not in table3
            sign = 1 if q % 3 == 1 else -1
            table3[u] = (sign, (j + k) % 3)
            decomposition3[u] = (q, j, k)
all_units3 = [(a, b) for a in range(9) for b in range(9)
              if (a * a - a * b + b * b) % 3 != 0]
assert len(table3) == 54 and set(table3) == set(all_units3)
for u in all_units3:
    su, eu = table3[u]
    assert table3[modpair(econj(u), 9)] == (su, (-eu) % 3)
    for v in all_units3:
        sv, ev = table3[v]
        assert table3[mmul(u, v, 9)] == (su * sv, (eu + ev) % 3)
assert table3[g] == (1, 1)
assert table3[(0, 1)] == (1, 1)
assert table3[(8, 0)] == (-1, 0)

table2 = {(1, 0): 0, (0, 1): 1, (1, 1): 2}
for u, eu in table2.items():
    for v, ev in table2.items():
        assert table2[mmul(u, v, 2)] == (eu + ev) % 3

# gamma7=3+omega: omega -> 4; conjugate prime: omega -> 2.
# Character values are residue^4.  The value is lifted in the same embedding.
decode7 = ({1: 0, 4: 1, 2: 2}, {1: 0, 2: 1, 4: 2})
table7 = []
for branch, omega_residue in enumerate((4, 2)):
    vals = {u: decode7[branch][pow(u, 4, 7)] for u in range(1, 7)}
    for u in range(1, 7):
        for v in range(1, 7):
            assert vals[(u * v) % 7] == (vals[u] + vals[v]) % 3
    assert len(set(vals.values())) == 3
    table7.append(vals)

# Exact cyclotomic Gauss sum.  zeta9^6+zeta9^3+1=0.
def root9(n):
    n %= 9
    v = [0] * max(6, n + 1)
    v[n] = 1
    for j in range(len(v) - 1, 5, -1):
        v[j - 3] -= v[j]
        v[j - 6] -= v[j]
    return tuple(v[:6])

gauss = [0] * 6
for q in rational_units:
    for j in range(3):
        for k in range(3):
            sign = 1 if q % 3 == 1 else -1
            B = (-3 * q * k if j == 0 else
                 q * (5 - 3 * k) if j == 1 else q * (4 - 3 * k))
            term = root9(-3 * (j + k) - B)
            for i, value in enumerate(term):
                gauss[i] += sign * value
assert tuple(gauss) == (9, 0, 0, 0, 0, 0)

def teich(a):
    return table2[modpair(a, 2)]

def primitive_hecke(a, which="new"):
    assert math.gcd(enorm(a), 42) == 1
    sign, e3 = table3[modpair(a, 9)]
    e = teich(a)
    if which == "base":
        return escale(emul(a, OMEGA_POWERS[(-e) % 3]), sign)
    e += e3 if which == "new" else -e3
    for branch, omega_residue in enumerate((4, 2)):
        r = (a[0] + omega_residue * a[1]) % 7
        assert r != 0
        power = 4 if which == "new" else 2
        e += decode7[branch][pow(r, power, 7)]
    return escale(emul(a, OMEGA_POWERS[(-e) % 3]), sign)

assert all(primitive_hecke(u) == (1, 0) for u in UNITS)

spf = list(range(CUTOFF + 1))
for p in range(2, math.isqrt(CUTOFF) + 1):
    if spf[p] == p:
        for n in range(p * p, CUTOFF + 1, p):
            if spf[n] == n:
                spf[n] = p
primes = [p for p in range(2, CUTOFF + 1) if spf[p] == p]

def split_generator(p):
    assert p % 3 == 1
    for b in range(math.isqrt(4 * p // 3) + 2):
        disc = 4 * p - 3 * b * b
        if disc < 0:
            continue
        a2 = math.isqrt(disc)
        if a2 * a2 == disc and (b + a2) % 2 == 0:
            out = ((b + a2) // 2, b)
            assert enorm(out) == p
            return out
    raise AssertionError("A split prime had no Eisenstein generator.")

ap = {}
split_checks = 0
for p in primes:
    if p in BAD or p % 3 == 2:
        ap[p] = 0
        continue
    a = split_generator(p)
    value = primitive_hecke(a)
    assert enorm(value) == p
    assert primitive_hecke(econj(a)) == econj(value)
    for u in UNITS:
        associate = emul(u, a)
        assert enorm(associate) == p
        assert primitive_hecke(associate) == value
    old = primitive_hecke(a, "old")
    base = primitive_hecke(a, "base")
    assert emul(value, old) == emul(base, base)
    ap[p] = 2 * value[0] - value[1]
    assert ap[p] * ap[p] <= 4 * p
    split_checks += 1
assert (ap[13], ap[19], ap[31]) == (5, -1, -4)

local_powers = {}
for p in primes:
    powers = [1, ap[p]]
    power = p * p
    while power <= CUTOFF:
        powers.append(0 if p in BAD else ap[p] * powers[-1] - p * powers[-2])
        power *= p
    local_powers[p] = powers
coefficients = [0] * (CUTOFF + 1)
coefficients[1] = 1
for n in range(2, CUTOFF + 1):
    p = spf[n]
    rem, exponent = n, 0
    while rem % p == 0:
        rem //= p
        exponent += 1
    coefficients[n] = coefficients[rem] * local_powers[p][exponent]
assert all(type(a) is int for a in coefficients)
assert all(coefficients[n] == 0 for n in range(1, CUTOFF + 1)
           if math.gcd(n, 42) != 1)

# All interval endpoints are exact rational numbers.
def round_lower(x, den=DEN):
    return Q((x.p * den) // x.q, den)

def round_upper(x, den=DEN):
    return Q((x.p * den) // x.q + 1, den)

def atan_interval(q, terms=32):
    a = Q(1, q)
    s = Q(0)
    for j in range(terms):
        s += (-1 if j % 2 else 1) * a**(2 * j + 1) / Q(2 * j + 1)
    err = a**(2 * terms + 1) / Q(2 * terms + 1)
    return (s, s + err) if terms % 2 == 0 else (s - err, s)

l5, u5 = atan_interval(5)
l239, u239 = atan_interval(239)
pilo = round_lower(16 * l5 - 4 * u239)
pihi = round_upper(16 * u5 - 4 * l239)
sqrt_integer = math.isqrt(3 * DEN * DEN)
assert sqrt_integer * sqrt_integer < 3 * DEN * DEN < (sqrt_integer + 1)**2
sqrtlo, sqrthi = Q(sqrt_integer, DEN), Q(sqrt_integer + 1, DEN)
clo, chi = pilo / (63 * sqrthi), pihi / (63 * sqrtlo)
assert Q(1, 35) < clo < chi < Q(1, 34)
assert chi * CUTOFF < 31

def log_atanh(x, terms=24):
    t = (x - 1) / (x + 1)
    assert 0 <= t <= Q(1, 3)
    s = 2 * sum((t**(2 * j + 1) / Q(2 * j + 1)
                 for j in range(terms)), Q(0))
    err = 2 * t**(2 * terms + 1) / (Q(2 * terms + 1) * (1 - t * t))
    return s, s + err

l2, h2 = log_atanh(Q(2))

def log_interval(x):
    exponent = 0
    while x < 1:
        x *= 2
        exponent -= 1
    while x > 2:
        x /= 2
        exponent += 1
    lo, hi = log_atanh(x)
    if exponent >= 0:
        return lo + exponent * l2, hi + exponent * h2
    return lo + exponent * h2, hi + exponent * l2

M = 128
harm = sum((Q(1, j) for j in range(1, M + 1)), Q(0))
lm, hm = log_interval(Q(M))
base_gamma = harm - Q(1, 2 * M) + Q(1, 12 * M * M) - Q(1, 120 * M**4)
glo, ghi = base_gamma - hm, base_gamma - lm + Q(1, 252 * M**6)

def e1_interval(x):
    lo_log, hi_log = log_interval(x)
    term = x
    s = term
    for k in range(2, E1_TERMS + 1):
        term *= x * Q(k - 1, k * k)
        s += term if k % 2 else -term
    nxt = term * x * Q(E1_TERMS, (E1_TERMS + 1)**2)
    assert x < E1_TERMS + 1 and E1_TERMS % 2 == 0
    return (round_lower(-ghi - hi_log + s),
            round_upper(-glo - lo_log + s + nxt))

lo_sum, hi_sum = Q(0), Q(0)
used_terms = 0
for n in range(1, CUTOFF + 1):
    a = coefficients[n]
    if a == 0:
        continue
    # E1 decreases in its positive argument.
    e1lo, e1hi = e1_interval(chi * n)[0], e1_interval(clo * n)[1]
    assert e1lo <= e1hi
    if a > 0:
        lo_sum += Q(2 * a, n) * e1lo
        hi_sum += Q(2 * a, n) * e1hi
    else:
        lo_sum += Q(2 * a, n) * e1hi
        hi_sum += Q(2 * a, n) * e1lo
    used_terms += 1

# Hasse plus the full Hecke recurrence: |a_n| <= d(n)sqrt(n) <= 2n.
z = 1 / (1 + clo)
tail = 4 * z**(CUTOFF + 1) / (clo * (CUTOFF + 1) * (1 - z))
assert 0 < tail < Q(1, 10**10)
lo_print = round_lower(lo_sum - tail, 10**12)
hi_print = round_upper(hi_sum + tail, 10**12)
assert lo_print <= hi_print
nonzero = lo_print > 0 or hi_print < 0
local_serialization = {
    "two": [[list(u), e] for u, e in sorted(table2.items())],
    "three": [[list(u), list(decomposition3[u]), list(table3[u])]
              for u in sorted(table3)],
    "seven": [sorted(t.items()) for t in table7],
}
report = {
    "status": "PASS" if nonzero else "INCONCLUSIVE_NONVANISHING",
    "request": "original-e21609-complete-lprime",
    "mathematical_method_complete": True,
    "curve": "y^2=x^3+21609",
    "hecke_conductor": "2*delta^4*7",
    "classical_level": LEVEL,
    "root_number": -1,
    "bad_euler_factors": {"2": 1, "3": 1, "7": 1},
    "parameters": {"cutoff": CUTOFF, "e1_terms": E1_TERMS,
                   "directed_denominator": DEN, "atan_terms": 32,
                   "log_terms": 24, "euler_maclaurin_M": M},
    "verified_inputs": verified_pins,
    "all_54_units_and_2916_products_checked": True,
    "full_gauss_sum_in_zeta9_basis": gauss,
    "finite_local_character_sha256": digest(local_serialization),
    "all_six_associates_and_conjugates_checked_at_split_primes": split_checks,
    "full_inverse_twist_identity_checked_at_split_primes": split_checks,
    "good_anchor_a13_a19_a31": [ap[13], ap[19], ap[31]],
    "all_1024_coefficients_kept": True,
    "coefficient_array_sha256": digest(coefficients[1:]),
    "coefficients_n1_through_1024": coefficients[1:],
    "good_and_bad_prime_coefficients": [[p, ap[p]] for p in primes],
    "used_n_terms": used_terms,
    "sqrt3_lower": str(sqrtlo),
    "sqrt3_upper": str(sqrthi),
    "c_lower": str(round_lower(clo)),
    "c_upper": str(round_upper(chi)),
    "tail_less_than": "1/10000000000",
    "complete_tail_verified": True,
    "Lprime_lower": str(lo_print),
    "Lprime_upper": str(hi_print),
    "certified_nonzero": nonzero,
    "analytic_order_one": nonzero,
    "outputs_persisted": False,
    "mathematical_elapsed_seconds": time.monotonic() - START,
}
print(json.dumps(report, separators=(",", ":"), ensure_ascii=True))
