#!/usr/bin/env python3
"""Full original R761 primitive-nine L'(1) certificate; public Actions only.

All three exact characters are reconstructed from their original 2/17 unit
tables and R302's degree-two Hecke character.  No database, saved Fourier
coefficients, original CM matrix rerun, floating point L evaluator, or output
file is used.  The rational E1 algorithm is the proven R735 method, applied
only to the three new characters.
"""
from __future__ import annotations
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import time

if os.environ.get("GITHUB_ACTIONS") != "true":
    raise RuntimeError("This mathematical producer runs only in public GitHub Actions.")
if os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
    raise RuntimeError("The original public repository is required.")
import flint
from flint import fmpq as Q
if flint.__version__ != "0.9.0":
    raise RuntimeError("python-flint==0.9.0 is required.")

START = time.monotonic()
CUTOFF = 512
E1_TERMS = 144
COS_TERMS = 32
DEN = 10**18
LABELS = (1, 7, 13)
LOCAL_L = {1: -8, 7: -2, 13: 4}
REPO = Path(__file__).resolve().parents[3]
PREFIX = "topics/rank2-sha-infinitely-many-p/"
PINS = (
    (PREFIX + "results/R302-jzero-original-degree-two-reference-and-exact-full-weight-square.md",
     "bd3204188d1c795053d4e0b15ebdef082cd688a918d3dae4b87f17b8bd549507"),
    (PREFIX + "results/R761-primitive-type-five-ninth-order-characters-and-point-fields.md",
     "db00a32be62403a016bb78f169cd478aefeb8d0354410c5b6373087d34f7a4b6"),
    (PREFIX + "scripts/check-r732-two-cubic-rank-one-bounds.py",
     "abc12f49db1818351534889f31bd9b7bac7876a78cbd043a060834d97c2a8289"),
)
verified_pins = []
for rel, expected in PINS:
    raw = (REPO / rel).read_bytes()
    actual = hashlib.sha256(raw).hexdigest()
    if actual != expected:
        raise RuntimeError("Original source pin changed: " + rel)
    verified_pins.append({"path": rel, "bytes": len(raw), "sha256": actual})

def digest(obj):
    return hashlib.sha256(json.dumps(obj, separators=(",", ":"), ensure_ascii=True).encode()).hexdigest()

# Exact Z[zeta_9], ordered basis 1,z,...,z^5, z^6+z^3+1=0.
ZERO = (0, 0, 0, 0, 0, 0)
ONE = (1, 0, 0, 0, 0, 0)

def reduce_cyclo(values):
    v = list(values)
    if len(v) < 6:
        v += [0] * (6 - len(v))
    for i in range(len(v) - 1, 5, -1):
        c = v[i]
        v[i - 3] -= c
        v[i - 6] -= c
    return tuple(v[:6])

def add_cyclo(a, b):
    return tuple(x + y for x, y in zip(a, b))

def scale_cyclo(a, c):
    return tuple(c * x for x in a)

def mul_cyclo(a, b):
    v = [0] * 11
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            v[i + j] += x * y
    return reduce_cyclo(v)

def root9(n):
    n %= 9
    v = [0] * (n + 1)
    v[n] = 1
    return reduce_cyclo(v)

ROOT9 = tuple(root9(i) for i in range(9))
OMEGA = ROOT9[3]

def root18(n):
    # zeta_18=-zeta_9^5; this fixes g0^6=omega without a new phase.
    return scale_cyclo(ROOT9[(5 * n) % 9], -1 if n % 2 else 1)

def automorphism(a, exponent):
    out = ZERO
    for i, c in enumerate(a):
        out = add_cyclo(out, scale_cyclo(ROOT9[(i * exponent) % 9], c))
    return out

def conjugate(a):
    return automorphism(a, 8)

def eisenstein_mul(a, b):
    x, y = a
    u, v = b
    return (x * u - y * v, x * v + y * u - y * v)

def eisenstein_conj(a):
    x, y = a
    return (x - y, -y)

def eisenstein_norm(a):
    x, y = a
    return x * x - x * y + y * y

# Whole F_289 and the original g0=2+4delta=6+8omega, not a sampled character.
def fmul(a, b):
    x, y = a
    u, v = b
    return ((x * u - y * v) % 17, (x * v + y * u - y * v) % 17)

def fpow(a, n):
    assert n >= 0
    out = (1, 0)
    while n:
        if n & 1:
            out = fmul(out, a)
        a = fmul(a, a)
        n >>= 1
    return out

G0 = (6, 8)
torus = {}
z = (1, 0)
for exponent in range(18):
    assert z not in torus
    torus[z] = exponent
    z = fmul(z, G0)
assert z == (1, 0)
assert fpow(G0, 6) == (0, 1)
assert all((x * x - x * y + y * y) % 17 == 1 for x, y in torus)

def theta_exponent(unit, ell):
    return torus[fpow(unit, (16 * ell) % 288)]

units17 = [(a, b) for a in range(17) for b in range(17) if (a, b) != (0, 0)]
character_table = {}
for label in LABELS:
    ell = LOCAL_L[label]
    vals = [theta_exponent(u, ell) for u in units17]
    assert len(set(vals)) == 9 and all(v % 2 == 0 for v in vals)
    assert all(theta_exponent((a, 0), ell) == 0 for a in range(1, 17))
    assert theta_exponent((1, 2), ell) == 0
    assert theta_exponent((0, 1), ell) == 6
    for u, v in zip(units17, vals):
        uc = ((u[0] - u[1]) % 17, -u[1] % 17)
        assert (theta_exponent(uc, ell) + v) % 18 == 0
    character_table[label] = vals

# Checking all powers of a primitive generator proves the whole multiplicative table.
primitive = None
for u in units17:
    if fpow(u, 144) != (1, 0) and fpow(u, 96) != (1, 0):
        primitive = u
        break
assert primitive is not None
cycle = []
z = (1, 0)
for exponent in range(288):
    cycle.append(z)
    z = fmul(z, primitive)
assert z == (1, 0) and len(set(cycle)) == 288
for label in LABELS:
    ell = LOCAL_L[label]
    e = theta_exponent(primitive, ell)
    assert all(theta_exponent(u, ell) == (n * e) % 18 for n, u in enumerate(cycle))

def teich_exponent(a):
    r = (a[0] % 2, a[1] % 2)
    return {(1, 0): 0, (0, 1): 1, (1, 1): 2}[r]

def original_hecke(a, label):
    # psi0(a)=a*epsilon1(a)^-1; eta(a)=(Teich(a)^-1*theta_l(a))^-1.
    # Thus Psi_j(a)=a*epsilon_delta(a)*Teich(a)^-2*theta_l(a).
    x, y = a
    residue3 = (x + y) % 3
    assert residue3 in (1, 2)
    sign = 1 if residue3 == 1 else -1
    t = teich_exponent(a)
    residue17 = (x % 17, y % 17)
    assert residue17 != (0, 0)
    e = theta_exponent(residue17, LOCAL_L[label])
    av = (x, 0, 0, y, 0, 0)
    return scale_cyclo(mul_cyclo(mul_cyclo(av, ROOT9[(-6 * t) % 9]), root18(e)), sign)

spf = list(range(CUTOFF + 1))
for p in range(2, math.isqrt(CUTOFF) + 1):
    if spf[p] == p:
        for n in range(p * p, CUTOFF + 1, p):
            if spf[n] == n:
                spf[n] = p
primes = [p for p in range(2, CUTOFF + 1) if spf[p] == p]
BAD = {2, 3, 17}
UNITS = ((1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1))

def split_generator(p):
    assert p % 3 == 1
    for b in range(math.isqrt(4 * p // 3) + 2):
        disc = 4 * p - 3 * b * b
        if disc < 0:
            continue
        a2 = math.isqrt(disc)
        if a2 * a2 == disc and (b + a2) % 2 == 0:
            out = ((b + a2) // 2, b)
            assert eisenstein_norm(out) == p
            return out
    raise AssertionError("Split prime did not have an Eisenstein generator.")

ap = {label: {} for label in LABELS}
split_checks = 0
for p in primes:
    if p in BAD or p % 3 == 2:
        for label in LABELS:
            ap[label][p] = ZERO
        continue
    a = split_generator(p)
    for label in LABELS:
        value = original_hecke(a, label)
        assert mul_cyclo(value, conjugate(value)) == scale_cyclo(ONE, p)
        assert original_hecke(eisenstein_conj(a), label) == conjugate(value)
        for u in UNITS:
            associate = eisenstein_mul(u, a)
            assert eisenstein_norm(associate) == p
            assert original_hecke(associate, label) == value
        ap[label][p] = add_cyclo(value, conjugate(value))
        assert conjugate(ap[label][p]) == ap[label][p]
    assert ap[7][p] == automorphism(ap[1][p], 7)
    assert ap[13][p] == automorphism(ap[1][p], 4)
    split_checks += 1

coefficients = {}
for label in LABELS:
    local_powers = {}
    for p in primes:
        powers = [ONE, ap[label][p]]
        power = p * p
        while power <= CUTOFF:
            nxt = ZERO if p in BAD else add_cyclo(
                mul_cyclo(ap[label][p], powers[-1]), scale_cyclo(powers[-2], -p))
            powers.append(nxt)
            power *= p
        local_powers[p] = powers
    aa = [ZERO] * (CUTOFF + 1)
    aa[1] = ONE
    for n in range(2, CUTOFF + 1):
        p = spf[n]
        rem = n
        exponent = 0
        while rem % p == 0:
            rem //= p
            exponent += 1
        aa[n] = mul_cyclo(aa[rem], local_powers[p][exponent])
    assert all(conjugate(a) == a for a in aa)
    coefficients[label] = aa
assert all(coefficients[7][n] == automorphism(coefficients[1][n], 7)
           and coefficients[13][n] == automorphism(coefficients[1][n], 4)
           for n in range(CUTOFF + 1))

# Rational real intervals. No binary floating-point quantity enters any bound.
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
clo, chi = pilo / 51, pihi / 51

def cos_interval(lo, hi):
    assert 0 <= lo <= hi
    lower, upper = Q(0), Q(0)
    for j in range(COS_TERMS):
        fac = math.factorial(2 * j)
        a, b = lo**(2 * j) / fac, hi**(2 * j) / fac
        if j % 2:
            lower -= b
            upper -= a
        else:
            lower += a
            upper += b
    err = hi**(2 * COS_TERMS) / math.factorial(2 * COS_TERMS)
    return round_lower(lower - err), round_upper(upper + err)

cosines = [(Q(1), Q(1))]
for j in range(1, 6):
    cosines.append(cos_interval(2 * j * pilo / 9, 2 * j * pihi / 9))

def real_interval(a):
    assert conjugate(a) == a
    lo, hi = Q(0), Q(0)
    for c, (cl, ch) in zip(a, cosines):
        if c >= 0:
            lo += c * cl
            hi += c * ch
        else:
            lo += c * ch
            hi += c * cl
    return lo, hi

def log_atanh(x, terms=24):
    t = (x - 1) / (x + 1)
    assert 0 <= t <= Q(1, 3)
    s = 2 * sum((t**(2 * j + 1) / Q(2 * j + 1) for j in range(terms)), Q(0))
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
base = harm - Q(1, 2 * M) + Q(1, 12 * M * M) - Q(1, 120 * M**4)
glo, ghi = base - hm, base - lm + Q(1, 252 * M**6)

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

def interval_product(a, b):
    values = (a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1])
    return min(values), max(values)

bounds = {label: [Q(0), Q(0)] for label in LABELS}
used_terms = 0
for n in range(1, CUTOFF + 1):
    if all(coefficients[label][n] == ZERO for label in LABELS):
        continue
    # E1 is decreasing on positive arguments; both endpoints have rational certificates.
    e1 = (e1_interval(chi * n)[0], e1_interval(clo * n)[1])
    assert e1[0] <= e1[1]
    for label in LABELS:
        term = interval_product(real_interval(coefficients[label][n]), e1)
        bounds[label][0] += Q(2, n) * term[0]
        bounds[label][1] += Q(2, n) * term[1]
    used_terms += 1

# |a_n| <= d(n)sqrt(n) <= 2n, valid in every one of the three embeddings.
z = 1 / (1 + clo)
tail = 4 * z**(CUTOFF + 1) / (clo * (CUTOFF + 1) * (1 - z))
assert 0 < tail < Q(1, 10**10)
certificates = []
for label in LABELS:
    lo = bounds[label][0] - tail
    hi = bounds[label][1] + tail
    assert lo <= hi
    # Printed endpoints themselves certify the reported nonvanishing.
    lo_print = round_lower(lo, 10**12)
    hi_print = round_upper(hi, 10**12)
    nonzero = lo_print > 0 or hi_print < 0
    certificates.append({
        "original_label": label,
        "local_l": LOCAL_L[label],
        "level": 10404,
        "root_number": -1,
        "coefficient_basis": "1,zeta9,zeta9^2,zeta9^3,zeta9^4,zeta9^5",
        "a1": list(coefficients[label][1]),
        "a13": list(ap[label][13]),
        "coefficient_1_through_512_sha256": digest(coefficients[label][1:]),
        "Lprime_lower": str(lo_print),
        "Lprime_upper": str(hi_print),
        "certified_nonzero": nonzero,
        "analytic_order_one": nonzero,
    })
all_nonzero = all(c["certified_nonzero"] for c in certificates)
report = {
    "status": "PASS" if all_nonzero else "INCONCLUSIVE_NONVANISHING",
    "request": "original-r761-three-primitive-nine-analytic-rank",
    "mathematical_method_complete": True,
    "all_three_characters_kept": True,
    "all_three_nonzero": all_nonzero,
    "parameters": {"cutoff": CUTOFF, "e1_terms": E1_TERMS,
                   "cos_terms": COS_TERMS, "directed_denominator": DEN,
                   "euler_maclaurin_M": M},
    "verified_inputs": verified_pins,
    "finite_17_units": 288,
    "finite_17_primitive_generator": list(primitive),
    "finite_17_full_character_sha256": digest(character_table),
    "all_six_associates_and_conjugate_checked_at_split_primes": split_checks,
    "all_512_coefficients_and_all_three_Galois_returns_checked": True,
    "complete_coefficient_array_sha256": digest(coefficients),
    "used_n_terms": used_terms,
    "bad_euler_factors": {"2": 1, "3": 1, "17": 1},
    "tail_less_than": "1/10000000000",
    "tail_bound_verified": True,
    "certificates": certificates,
    "outputs_persisted": False,
    "mathematical_elapsed_seconds": time.monotonic() - START,
}
print(json.dumps(report, separators=(",", ":"), ensure_ascii=True))
