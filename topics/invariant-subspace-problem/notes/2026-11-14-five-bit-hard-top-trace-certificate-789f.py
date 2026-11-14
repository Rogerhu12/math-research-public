#!/usr/bin/env python3
"""Complete exact certificate for the whole-source five-bit hard-end S1.

No sampling is used.  The 5 x 5 matrices are operator coordinates under
x -> diag(b) x, with physical metric diag(z); ordinary Euclidean adjoints
are not substituted for physical adjoints.  Only similarity-invariant
traces and exact matrix products are computed.

Reconstructs Tr(K_hard)=N/D and checks every integer coefficient of
743 D - 782 N.  The JSON stores all symmetric monomial orbits and hashes,
so the complete polynomial certificate can be reconstructed without
writing large expanded matrices.
"""
from __future__ import annotations
import argparse
import hashlib
import itertools
import json
from pathlib import Path
import time
from fractions import Fraction
from flint import fmpz_mpoly_ctx


def build():
    started = time.monotonic()
    ctx = fmpz_mpoly_ctx.get(tuple(f'z{i}' for i in range(5)))
    z = ctx.gens()
    zero, one = ctx.constant(0), ctx.constant(1)

    def prod(xs):
        out = one
        for x in xs:
            out *= x
        return out

    def elementary(xs, degree):
        return sum((prod(v) for v in itertools.combinations(xs, degree)), zero)

    def mm(a, b):
        return [[sum((a[i][k]*b[k][j] for k in range(5)), zero)
                 for j in range(5)] for i in range(5)]

    def trace_product(a, b):
        return sum((a[i][j]*b[j][i] for i in range(5) for j in range(5)), zero)

    def exact_div(a, b):
        q, remainder = divmod(a, b)
        assert not remainder, 'non-exact polynomial division'
        return q

    def stats(poly):
        data = poly.to_dict()
        canonical = [[[int(e) for e in p], int(c)] for p, c in sorted(data.items())]
        return dict(terms=len(data), degree=int(poly.total_degree()),
                    negative_coefficients=sum(c < 0 for c in data.values()),
                    sha256=hashlib.sha256(json.dumps(canonical, separators=(',', ':')).encode()).hexdigest())

    S = sum(z, zero)
    Z = prod(z)
    e3, e4 = elementary(z, 3), elementary(z, 4)
    delta = S*S*e3 - 4*S*e4 + 12*Z
    Delta = 4*delta
    ds = [S-2*x for x in z]
    determinant_direct = prod(ds) + sum((z[i]*prod(ds[j] for j in range(5) if j != i)
                                        for i in range(5)), zero)
    assert determinant_direct == Delta
    # F is the full physical d d* after similarity x -> diag(b) x.
    F = [[(ds[i] if i == j else zero)+z[j] for j in range(5)] for i in range(5)]
    adj = [[
        -z[j]*prod(ds[k] for k in range(5) if k != i and k != j)
        if i != j else
        prod(ds[k] for k in range(5) if k != i)
        + sum((z[k]*prod(ds[l] for l in range(5) if l != i and l != k)
               for k in range(5) if k != i), zero)
        for j in range(5)] for i in range(5)]
    Fadj = mm(F, adj)
    assert all(Fadj[i][j] == (Delta if i == j else zero) for i in range(5) for j in range(5))
    P = [[(S if i == j else zero)-z[j] for j in range(5)] for i in range(5)]
    # L1 = L / den on the four-dimensional primitive source, zero on constants.
    L = mm(mm(P, adj), P)
    den = S*S*Delta
    # T/Z is the full physical e*e in the same (nonorthogonal) coordinates.
    T = [[(e4-2*exact_div(Z,z[i]) if i == j else zero)+exact_div(Z,z[i])
          for j in range(5)] for i in range(5)]
    # K/e4 is the inverse of the true compressed top Gram, zero on constants.
    K = [[
        exact_div(Z,z[i])*elementary(tuple(z[k] for k in range(5) if k != i),3)
        if i == j else -exact_div(Z*Z,z[i]*z[i]*z[j])
        for j in range(5)] for i in range(5)]
    assert all(sum(row,zero) == zero for row in L)
    assert all(sum(row,zero) == zero for row in K)
    assert all(sum((z[i]*K[i][j] for i in range(5)),zero) == zero for j in range(5))
    top_product = mm(P, [[z[i]*z[i]*K[i][j] for j in range(5)] for i in range(5)])
    assert all(top_product[i][j] == Z*e4*P[i][j] for i in range(5) for j in range(5))
    KL = mm(K,L)
    TL = mm(T,L)
    LL = mm(L,L)
    raw_numerator = den*trace_product(KL,TL)-9*Z*trace_product(KL,LL)
    raw_denominator = Z*e4*den**3
    # This explicit cancellation is checked; no numerical rational fitting.
    common = 64*Z*S**6
    N = exact_div(raw_numerator, common)
    D = e4*delta**3
    assert raw_denominator == common*D
    gap = 743*D-782*N
    nd, dd, gd = N.to_dict(), D.to_dict(), gap.to_dict()
    assert all(c >= 0 for c in dd.values()) and dd
    assert all(c >= 0 for c in gd.values()) and gd
    assert sum(nd.values()) == 0, 'equal-weight trace must vanish'
    assert all(sum(p) == 19 for p in set(nd)|set(dd)|set(gd))
    # Audit all symmetric orbits, with zero coefficients represented explicitly.
    orbits = {}
    for powers in set(nd)|set(dd)|set(gd):
        part = tuple(sorted(powers,reverse=True))
        coeffs = tuple(int(v.get(powers,0)) for v in (nd,dd,gd))
        if part in orbits:
            assert orbits[part] == coeffs, 'symmetric coefficient mismatch'
        orbits[part] = coeffs
    orbit_records = []
    support_count = [0,0,0]
    for part, coeffs in sorted(orbits.items(),reverse=True):
        orbit = set(itertools.permutations(part))
        for powers in orbit:
            assert tuple(int(v.get(powers,0)) for v in (nd,dd,gd)) == coeffs
        for j,c in enumerate(coeffs):
            support_count[j] += len(orbit)*(c != 0)
        orbit_records.append(dict(partition=[int(e) for e in part], multiplicity=len(orbit),
                                  N=coeffs[0], D=coeffs[1], gap=coeffs[2]))
    assert support_count == [len(nd),len(dd),len(gd)]
    positive_ratios = [(Fraction(int(c),int(dd[p])),p) for p,c in nd.items() if c > 0]
    best, witness = max(positive_ratios)
    assert best == Fraction(743,782)
    return dict(
        status='all_passed', theorem='M=5, r=2, all five independent positive weights; complete physical source',
        source_dimensions=dict(upper=5,lower=4), bound='743/782',
        identity='trace(K_hard)=N/D; D=e4*(S^2*e3-4*S*e4+12*e5)^3',
        exact_division='raw_N=(64*e5*S^6)*N; raw_D=(64*e5*S^6)*D',
        full_first_inverse_identity=True, compressed_top_inverse_identity=True,
        all_gap_coefficients_nonnegative=True, denominator_all_coefficients_positive=True,
        equal_weight_trace_zero=True, symmetry_orbits_complete=True,
        delta=stats(delta), numerator=stats(N), denominator=stats(D), gap=stats(gap),
        maximum_positive_coefficient_ratio=dict(ratio=str(best),exponents=[int(e) for e in witness],
                                                N=int(nd[witness]),D=int(dd[witness])),
        symmetric_orbit_count=len(orbit_records), symmetric_monomial_orbits=orbit_records,
        elapsed_seconds=time.monotonic()-started)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=Path(__file__).with_suffix('.json'))
    args=parser.parse_args()
    result=build()
    result['generator_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='symmetric_monomial_orbits'},indent=2))


if __name__=='__main__':
    main()
