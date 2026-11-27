#!/usr/bin/env python3
"""Fixed p=29 original type-four PB4 Taylor detector.

Public Actions only. Imports the original R798 halfperiod projector; never
calls its main(), CM13 fiber(), or operator reconstruction. All six original
columns and the entire rank-three image are retained over Q(omega) and
(Z/29^2)[omega]/(omega^2+omega+1). No nonzero outcome is assumed.
Dependencies: Python stdlib and python-flint==0.9.0. No output files.
"""
from __future__ import annotations
import os, sys
sys.dont_write_bytecode = True
if (os.environ.get("GITHUB_ACTIONS") != "true"
        or os.environ.get("GITHUB_REPOSITORY", "").lower()
           != "rogerhu12/math-research-public"
        or not os.environ.get("GITHUB_RUN_ID")):
    raise SystemExit("This mathematical consumer runs only in the public repository Actions.")
import hashlib, importlib.util, json, math, pathlib, time
from fractions import Fraction as F

START = time.perf_counter()
HERE = pathlib.Path(__file__).resolve().parent
HP = HERE / "check-r798-type-four-halfperiod-and-cm13.py"
spec = importlib.util.spec_from_file_location("fixed_p29_r798", HP)
hp = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = hp
spec.loader.exec_module(hp)

P, MOD, BPAR, M, TOP = 29, 29**2, 17, 28, 4
assert P % 6 == 5 and M == P - 1
assert all(P % q for q in range(2, math.isqrt(P) + 1))

def convolution(a, b, top, modulus=None):
    zero = 0 if modulus is not None else F(0)
    out = [zero for _ in range(top + 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j <= top:
                out[i + j] += x * y
    return [x % modulus for x in out] if modulus is not None else out

def actual_series(modulus=None):
    def quotient(num, den):
        if modulus is None:
            return F(num, den)
        assert math.gcd(den, modulus) == 1
        return (num * pow(den, -1, modulus)) % modulus
    one = 1 if modulus is not None else F(1)
    zero = 0 if modulus is not None else F(0)
    a = [zero for _ in range(TOP + 1)]
    a[0], a[1] = one, quotient(-1, 7)
    for n in range(2, TOP + 1):
        a[n] = quotient(sum(a[i] * a[n-i] for i in range(1, n)),
                        (n-1) * (6*n+1))
    a2 = convolution(a, a, TOP, modulus)
    a3 = convolution(a2, a, TOP, modulus)
    lhs = convolution([(1-3*n)*a[n] for n in range(TOP+1)],
                      [(1-3*n)*a[n] for n in range(TOP+1)], TOP, modulus)
    rhs = a3[:]
    rhs[1] += one
    if modulus is not None:
        rhs = [x % modulus for x in rhs]
    assert lhs == rhs, "The entire paid elliptic equation window is required."
    f = [zero for _ in range(TOP+1)]
    for n in range(1, TOP+1):
        f[n] = quotient(-a[n], 6*n*(6*n-1))
    e = [zero for _ in range(TOP+1)]
    e[0] = one
    for n in range(1, TOP+1):
        e[n] = quotient(34 * sum(k*f[k]*e[n-k] for k in range(1, n+1)), n)
    powers = [one] + [zero for _ in range(TOP)]
    row, indices = [], []
    for j in range(6):
        index = j - 1
        assert 34 - 6*j + 6*index == M
        indices.append(index)
        row.append(zero if index < 0 else
                   convolution(e, powers, TOP, modulus)[index])
        if j < 5:
            powers = convolution(powers, a3, TOP, modulus)
    return a, f, e, row, indices

def rational_mod(x, modulus):
    num, den = int(x.numerator), int(x.denominator)
    assert math.gcd(den, modulus) == 1
    return num % modulus * pow(den, -1, modulus) % modulus

def kmod(x, modulus):
    return (rational_mod(x[0], modulus), rational_mod(x[1], modulus))

def kmul(x, y, modulus):
    t = x[1]*y[1]
    return ((x[0]*y[0]-t) % modulus,
            (x[0]*y[1]+x[1]*y[0]-t) % modulus)

def madd(x, y, modulus):
    return ((x[0]+y[0]) % modulus, (x[1]+y[1]) % modulus)

def mproduct(a, b, modulus):
    out = []
    for row in a:
        line = []
        for col in zip(*b):
            total = (0, 0)
            for x, y in zip(row, col):
                total = madd(total, kmul(x, y, modulus), modulus)
            line.append(total)
        out.append(line)
    return out

def rank_over_residue_field(a):
    a = [[(x % P, y % P) for x, y in row] for row in a]
    rank, pivots = 0, []
    for j in range(len(a[0])):
        pos = next((i for i in range(rank, len(a)) if a[i][j] != (0, 0)), None)
        if pos is None:
            continue
        a[rank], a[pos] = a[pos], a[rank]
        x, y = a[rank][j]
        norm = (x*x-x*y+y*y) % P
        assert norm, "omega^2+omega+1 is irreducible at the fixed inert prime."
        ni = pow(norm, -1, P)
        inverse = ((x-y)*ni % P, -y*ni % P)
        a[rank] = [kmul(z, inverse, P) for z in a[rank]]
        for i in range(len(a)):
            if i == rank or a[i][j] == (0, 0):
                continue
            c = a[i][j]
            a[i] = [((v[0]-w[0]) % P, (v[1]-w[1]) % P)
                    for v, w in zip(a[i], [kmul(c, z, P) for z in a[rank]])]
        pivots.append(j)
        rank += 1
        if rank == len(a):
            break
    return rank, pivots

def ek(x):
    return [str(x[0]), str(x[1])]

def em(a):
    return [[ek(x) for x in row] for row in a]

def digest(value):
    raw = json.dumps(value, separators=(",", ":"), sort_keys=True).encode()
    return hashlib.sha256(raw).hexdigest()

def valuation29(x):
    if not x:
        return None
    num, den = abs(int(x.numerator)), int(x.denominator)
    v = 0
    while num % P == 0:
        num //= P
        v += 1
    while den % P == 0:
        den //= P
        v -= 1
    return v

def minimum_k_valuation(row):
    values = [valuation29(c) for x in row for c in x if c]
    return min(values) if values else None

def main():
    a, f, e, row, indices = actual_series()
    am, fm, emod, rowm, indicesm = actual_series(MOD)
    for exact, reduced in ((a, am), (f, fm), (e, emod), (row, rowm)):
        assert [rational_mod(x, MOD) for x in exact] == reduced
    assert indices == indicesm

    pb = hp.PB4
    assert len(pb) == 6 and all(len(x) == 6 for x in pb)
    assert hp.mm(pb, pb) == pb
    _, pivots, _ = hp.rref(pb)
    assert len(pivots) == 3
    basis = [[r[j] for j in pivots] for r in pb]
    assert hp.mm(pb, basis) == basis
    exact_row = [(hp.Q(x.numerator, x.denominator), hp.Q(0)) for x in row]
    projected = hp.mm([exact_row], pb)[0]
    basis_values = hp.mm([exact_row], basis)[0]
    assert basis_values == [projected[j] for j in pivots]
    assert hp.mm([projected], pb)[0] == projected

    pbm = [[kmod(x, MOD) for x in r] for r in pb]
    pbp = [[kmod(x, P) for x in r] for r in pb]
    assert mproduct(pbm, pbm, MOD) == pbm
    rank, pivots_modp = rank_over_residue_field(pbp)
    assert rank == 3
    direct_projected_modp2 = mproduct([[(x, 0) for x in rowm]], pbm, MOD)[0]
    assert direct_projected_modp2 == [kmod(x, MOD) for x in projected]

    factorial = math.factorial(M)
    b_power = BPAR**4
    full_scalar = factorial * b_power
    hurwitz_row = [hp.scale(x, hp.Q(full_scalar)) for x in exact_row]
    projected_hurwitz = [hp.scale(x, hp.Q(full_scalar)) for x in projected]
    assert hp.mm([hurwitz_row], pb)[0] == projected_hurwitz
    projected_modp = [kmod(x, P) for x in projected]
    projected_hurwitz_modp2 = [kmod(x, MOD) for x in projected_hurwitz]

    report = {
        "format": "fixed p29 complete original PB4 Taylor diagnostic",
        "status": "PASS",
        "status_scope": "Exact and residue-ring structural gates, irrespective of whether the observed row vanishes.",
        "fixed_prime": P, "modulus": MOD, "b": BPAR,
        "field": "Q(omega), omega^2+omega+1=0",
        "residue_ring": "(Z/841Z)[omega]/(omega^2+omega+1); coordinates [1,omega]",
        "moment_degree": M, "series_max_index": TOP,
        "basis": "b^(5-j)*sigma_b^34*x_b^(3*j), j=0,...,5",
        "basis_orders": [34-6*j for j in range(6)],
        "basis_coefficient_indices": indices,
        "series_exact": {"A": [str(x) for x in a],
                         "log_sigma_over_z": [str(x) for x in f],
                         "exp34_log_sigma_over_z": [str(x) for x in e]},
        "elliptic_equation_full_window_exact_and_mod841": True,
        "exact_raw_taylor_row_without_common_b_power": [str(x) for x in row],
        "mod841_raw_taylor_row_without_common_b_power": rowm,
        "halfperiod_absolute_anchor": "Original R798 H(S)=omega^2 S",
        "PB4_exact": em(pb), "PB4_mod841": pbm,
        "PB4_rank_exact": len(pivots), "PB4_rank_mod29": rank,
        "PB4_pivot_columns_exact": pivots,
        "PB4_pivot_columns_mod29": pivots_modp,
        "PB4_basis_exact": em(basis),
        "exact_projected_taylor_row_without_common_b_power": [ek(x) for x in projected],
        "exact_values_on_three_basis_columns": [ek(x) for x in basis_values],
        "mod29_projected_taylor_row_without_common_b_power": projected_modp,
        "mod841_projected_taylor_row_without_common_b_power": direct_projected_modp2,
        "factorial_28": str(factorial),
        "common_b_power_17_pow4": b_power,
        "factorial_times_common_b_power": str(full_scalar),
        "factorial_times_common_b_power_mod841": full_scalar % MOD,
        "exact_original_hurwitz_row": [ek(x) for x in hurwitz_row],
        "exact_projected_original_hurwitz_row": [ek(x) for x in projected_hurwitz],
        "mod841_projected_original_hurwitz_row": projected_hurwitz_modp2,
        "observed_exact_projected_row_nonzero": any(x != hp.Z for x in projected),
        "observed_mod29_projected_row_nonzero": any(x != (0, 0) for x in projected_modp),
        "observed_mod841_projected_row_nonzero": any(x != (0, 0) for x in direct_projected_modp2),
        "exact_minimum_29_valuation_projected_row": minimum_k_valuation(projected),
        "complete_exact_PB4_sha256": digest(em(pb)),
        "input_sha256": {
            x.name: hashlib.sha256(x.read_bytes()).hexdigest() for x in (HP, hp.path)
        },
        "script_sha256": hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
        "public_run_id": os.environ["GITHUB_RUN_ID"],
        "elapsed_seconds": time.perf_counter() - START,
        "CM13_main_or_fibers_executed": False,
        "scope": "Only the fixed p29 full PB4 row. No eigenline nonvanishing, geometric identification, cross-prime claim, or canonical-zero propagation is inferred.",
        "outputs_persisted": False,
    }
    output = json.dumps(report, separators=(",", ":"), sort_keys=True)
    assert len(output.encode()) < 10000
    print(output)

if __name__ == "__main__":
    main()
