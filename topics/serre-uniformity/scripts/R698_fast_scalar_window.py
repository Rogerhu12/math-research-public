#!/usr/bin/env python3
"""Exact R698 scalar coefficients, with FLINT Newton exponentiation.

Only the requested finite prime interval is tested.  No all-prime
nonvanishing assertion is made.  A zero is recorded, not silently skipped.
Requires python-flint>=0.8.  Every formal denominator is a proved p-unit.
"""
import argparse
import hashlib
import json
from math import isqrt
from pathlib import Path
import time
import flint
from flint import nmod_poly


def series_exp(f, length, p):
    """exp(f) mod w**length for f[0]=0 and length<=p.

    Newton step g -> g*(1+f-log(g)) doubles the correct precision.
    log(g)=integral(g'/g), and every integrated index is <p.
    """
    assert int(f[0]) == 0 and 1 <= length <= p
    g = nmod_poly([1], p)
    n = 1
    while n < length:
        n2 = min(2*n, length)
        logg = g.derivative().mul_low(g.inverse_series_trunc(n2-1), n2-1).integral()
        g = g.mul_low(nmod_poly([1], p) + f.truncate(n2) - logg, n2)
        n = n2
    return g


def digest_values(values):
    return hashlib.sha256(json.dumps(values, separators=(',', ':')).encode()).hexdigest()


def run(p, full=False):
    assert p >= 41 and p % 6 == 5 and all(p % d for d in range(2, isqrt(p)+1))
    start = time.monotonic()
    N = (p-5)//6
    # Linear-time inverses of every integer that can occur in the truncation.
    inv = [0]*(p-3)
    inv[1] = 1
    for j in range(2, p-3):
        inv[j] = (p-(p//j)*inv[p % j]) % p
    c = [1]*(N+1)
    z = [1]*(N+1)
    h = [1]*(N+1)
    f = [0]*(N+1)
    for j in range(1, N+1):
        c[j] = c[j-1]*(2*j-1)*inv[2*j] % p
        z[j] = c[j]*inv[6*j+1] % p
        h[j] = h[j-1]*(6*j-4)*inv[6*j-1] % p
        f[j] = h[j]*inv[j] % p
    cp, zp, hp = (nmod_poly(v, p) for v in (c, z, h))
    tp = series_exp(nmod_poly(f, p), N+1, p)
    # A full exact recurrence certificate, independent of the Newton update.
    residual = (tp.derivative().left_shift(1) - tp.mul_low(hp-1, N+1)).truncate(N+1)
    assert residual.is_zero()
    z3 = zp.mul_low(zp, N+1).mul_low(zp, N+1)
    u = int(tp.mul_low(cp, N+1)[N])
    v = int(tp.mul_low(z3, N+1)[N])
    ell2 = pow(2, (p-1)//2, p)
    ap, aq = -ell2*u % p, 2*inv[3]*ell2*v % p
    coeffs = {'C': c, 'Z': z, 'H': h, 'T': [int(tp[j]) for j in range(N+1)]}
    result = {'prime': p, 'N': N, 'legendre_2': ell2,
              'coefficient_TC': u, 'coefficient_TZ3': v,
              'A_p': ap, 'A_p_minus_3': aq,
              'C_p': -3*ap*ap % p, 'C_p_minus_3': -3*aq*aq % p,
              'zero_channels': [name for name, val in [('C_p', u), ('C_p_minus_3', v)] if val == 0],
              'full_exponential_recurrence_checked': True,
              'maximum_divisor': 6*N+1, 'first_excluded_H_denominator': p,
              'coefficient_sha256': {k: digest_values(vals) for k, vals in coeffs.items()},
              'runtime_seconds': time.monotonic()-start}
    if full or u == 0 or v == 0:
        result['coefficients'] = coeffs
        result['TC_summands'] = [int(tp[j])*c[N-j] % p for j in range(N+1)]
        result['TZ3_summands'] = [int(tp[j])*int(z3[N-j]) % p for j in range(N+1)]
        assert sum(result['TC_summands']) % p == u
        assert sum(result['TZ3_summands']) % p == v
    return result


def primes_in_interval(lo, hi):
    assert hi >= lo >= 2
    sieve = bytearray(b'\x01')*(hi+1)
    sieve[:2] = b'\x00\x00'
    for q in range(2, isqrt(hi)+1):
        if sieve[q]:
            sieve[q*q:hi+1:q] = b'\x00'*(((hi-q*q)//q)+1)
    return [p for p in range(lo, hi+1) if sieve[p] and p % 9 in (2, 5)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prime', type=int)
    parser.add_argument('--lower', type=int, default=2001)
    parser.add_argument('--upper', type=int, default=20000)
    parser.add_argument('--shard-count', type=int, default=1)
    parser.add_argument('--shard-index', type=int, default=0)
    parser.add_argument('--full', action='store_true')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    assert 1 <= args.shard_count and 0 <= args.shard_index < args.shard_count
    prime_list = [args.prime] if args.prime else primes_in_interval(args.lower, args.upper)
    selected = prime_list[args.shard_index::args.shard_count]
    output = {'result': 'R698-fast', 'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'python_flint_version': flint.__version__,
              'lower': args.prime or args.lower, 'upper': args.prime or args.upper,
              'shard_count': args.shard_count, 'shard_index': args.shard_index,
              'candidate_count_before_sharding': len(prime_list),
              'all_prime_unit_claimed': False, 'division_by_p_used': False,
              'results': []}
    for p in selected:
        row = run(p, full=args.full)
        output['results'].append(row)
        output['tested_count'] = len(output['results'])
        output['zero_count'] = sum(bool(r['zero_channels']) for r in output['results'])
        args.output.write_text(json.dumps(output, indent=2)+'\n')
        print(json.dumps({k: row[k] for k in ['prime', 'N', 'A_p', 'A_p_minus_3', 'zero_channels', 'runtime_seconds']}), flush=True)
    if not selected:
        output['tested_count'] = output['zero_count'] = 0
        args.output.write_text(json.dumps(output, indent=2)+'\n')


if __name__ == '__main__':
    main()
