#!/usr/bin/env python3
"""R322: executed finite residue recurrence, not an upper-unit evaluator.

The actual global Y and X are the R311 radicals.  This program recomputes
all 44 base z residues from the marked elliptic curve and checks the exact
integer group-ring quotient and every affine recurrence.  It leaves the
one remaining phase and the canonical L explicitly uncomputed.
"""
import argparse
import hashlib
import json
from pathlib import Path

P = 43
N = 44
OMEGA = (8, 25)


def mul(a, b, q):
    return ((a[0]*b[0]-a[1]*b[1]) % q,
            (a[0]*b[1]+a[1]*b[0]) % q)


def add(a, b, q):
    return ((a[0]+b[0]) % q, (a[1]+b[1]) % q)


def neg(a, q):
    return ((-a[0]) % q, (-a[1]) % q)


def scale(a, b, q):
    return (a[0]*b % q, a[1]*b % q)


def inv(a, q):
    d = pow((a[0]*a[0]+a[1]*a[1]) % q, -1, q)
    return (a[0]*d % q, -a[1]*d % q)


def power(a, n, q):
    out = (1, 0)
    while n:
        if n & 1:
            out = mul(out, a, q)
        a = mul(a, a, q)
        n >>= 1
    return out


def rank_mod(rows, p):
    a = [[x % p for x in row] for row in rows]
    rank = 0
    for col in range(len(a[0])):
        pivot = next((j for j in range(rank, len(a)) if a[j][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        v = pow(a[rank][col], -1, p)
        a[rank] = [v*x % p for x in a[rank]]
        for j in range(len(a)):
            if j != rank and a[j][col]:
                v = a[j][col]
                a[j] = [(x-v*y) % p for x, y in zip(a[j], a[rank])]
        rank += 1
        if rank == len(a):
            break
    return rank


def base_residue_logs(source):
    raw = source.read_bytes()
    data = json.loads(raw)
    q = int(data['q'])
    point = tuple(tuple(map(int, a)) for a in data['P'])
    first_point = point
    zeta = tuple(map(int, data['zeta_Weil']))
    f = [int(a) for a in data['factors'][0]['coefficients']]
    zero, one, ii = (0, 0), (1, 0), (0, 1)

    def sub(a, b):
        return add(a, neg(b, q), q)

    def div(a, b):
        return mul(a, inv(b, q), q)

    def on(a):
        return a is None or mul(a[1], a[1], q) == sub(power(a[0], 3, q), a[0])

    def ecadd(a, b):
        if a is None:
            return b
        if b is None:
            return a
        if a[0] == b[0]:
            if add(a[1], b[1], q) == zero:
                return None
            slope = div(sub(scale(mul(a[0], a[0], q), 3, q), one), scale(a[1], 2, q))
        else:
            slope = div(sub(b[1], a[1]), sub(b[0], a[0]))
        x = sub(sub(mul(slope, slope, q), a[0]), b[0])
        y = sub(mul(slope, sub(a[0], x), q), a[1])
        out = (x, y)
        assert on(out)
        return out

    def ecmul(a, n):
        out = None
        while n:
            if n & 1:
                out = ecadd(out, a)
            a = ecadd(a, a)
            n >>= 1
        return out

    def cm_i(a):
        return (neg(a[0], q), mul(ii, a[1], q))

    assert q % 172 == 171
    assert on(point) and ecmul(point, P) is None
    assert all(v[1] == 0 for v in point)
    assert power(zeta, P, q) == one and zeta != one
    roots = {power(zeta, j, q): j for j in range(P)}
    assert len(roots) == P
    z_rows = []
    for j in range(N):
        assert on(point) and ecmul(point, P) is None
        r = point
        kernels = []
        for k in range(21):
            x, y = r
            t = sub(scale(mul(x, x, q), 6, q), (2, 0))
            v = scale(mul(y, y, q), 4, q)
            kernels.append((x, t, v))
            r = ecadd(r, point)

        def phi_x(a):
            x = a[0]
            out = x
            for u, t, v in kernels:
                d = inv(sub(x, u), q)
                out = add(out, add(mul(t, d, q), mul(v, mul(d, d, q), q), q), q)
            return out

        e0 = phi_x((zero, zero))
        em = phi_x(((q-1, 0), zero))
        p4 = phi_x((ii, (1, q-1)))
        z = div(neg(mul(ii, sub(p4, e0), q), q), sub(em, e0))
        v = zero
        for c in reversed(f):
            v = add(mul(v, z, q), (c % q, 0), q)
        assert v == zero
        z_rows.append(z)
        point = ecadd((point[0], neg(point[1], q)), ecmul(cm_i(point), 2))
    assert point == ecmul(first_point, 5)
    assert len(set(z_rows)) == N
    for j, z in enumerate(z_rows):
        assert power(z, q, q) == z_rows[-j % N]
        assert inv(z, q) == z_rows[(j+22) % N]
        assert div(add(mul(ii, z, q), one, q), add(z, ii, q)) == z_rows[(j+33) % N]
    m = (q*q-1)//P
    assert m % P == 21
    logs = [roots[power(z, m, q)] for z in z_rows]
    weights = [((15*power(OMEGA, j, P)[0]+21) % P)-21 for j in range(N)]
    u1 = one
    for j, exponent in enumerate(weights):
        z = z_rows[(j+1) % N]
        if exponent < 0:
            z, exponent = inv(z, q), -exponent
        u1 = mul(u1, power(z, exponent, q), q)
    assert power(u1, m, q) == one
    beta1 = power(u1, pow(P, -1, m), q)
    assert power(beta1, P, q) == u1 and power(beta1, m, q) == one
    anchor = {
        'q': str(q),
        'fixed_zeta': [str(x) for x in zeta],
        'sigma_U_residue': [str(x) for x in u1],
        'canonical_beta1': [str(x) for x in beta1],
        'canonical_beta1_power_7': [str(x) for x in power(beta1, 7, q)],
        'canonical_beta1_power_43_equals_sigma_U_residue': True,
        'canonical_beta1_power_m_equals_1': True,
    }
    return logs, hashlib.sha256(raw).hexdigest(), anchor


def build(source):
    logs, source_sha, anchor = base_residue_logs(source)
    omega = [power(OMEGA, j, P) for j in range(N)]
    weights = [((15*a[0]+21) % P)-21 for a in omega]
    numerators = [weights[(j-2) % N]-16*weights[(j-1) % N]+weights[j] for j in range(N)]
    assert all(a % P == 0 for a in numerators)
    b = [a//P for a in numerators]
    assert all(b[(j+22) % N] == -b[j] for j in range(N))
    v = [sum(b[k]*logs[(j+k) % N] for k in range(N)) % P for j in range(N)]
    assert all(sum(weights[k]*logs[(j+k) % N] for k in range(N)) % P == 0 for j in range(N))
    forcing = [7*x % P for x in v]
    aa, cc = [0, 1], [0, 0]
    for j in range(N):
        aa.append((16*aa[-1]-aa[-2]) % P)
        cc.append((16*cc[-1]-cc[-2]+forcing[j]) % P)
    assert aa[N:] == [0, 1] and cc[N:] == [0, 0]
    aa, cc = aa[:N], cc[:N]
    assert aa == [w[1]*pow(25, -1, P) % P for w in omega]
    for a in (aa, cc):
        assert a[0] == a[22] == 0
        assert all(a[-j % N] == -a[j] % P for j in range(N))
        assert all(a[(j+22) % N] == -a[j] % P for j in range(N))
    mat = []
    for j in range(N):
        row = [0]*N
        row[j] += 1
        row[(j+1) % N] -= 16
        row[(j+2) % N] += 1
        mat.append(row)
        assert sum(row[k]*aa[k] for k in range(N)) % P == 0
        assert sum(row[k]*cc[k] for k in range(N)) % P == forcing[j]
    rank_cyclic = rank_mod(mat, P)
    assert rank_cyclic == 42
    zero_row = [1]+[0]*43
    rank_real = rank_mod(mat+[zero_row], P)
    assert rank_real == 43
    rank_augmented = rank_mod([row+[rhs] for row, rhs in zip(mat, forcing)]+[zero_row+[0]], P)
    assert rank_augmented == 43
    coeff = 19*sum(omega[j][1]*aa[j] for j in range(1, 22)) % P
    constant = (19*sum(omega[j][1]*cc[j] for j in range(1, 22))-3) % P
    assert coeff == 29 and constant == 0
    x_cc = [37*c % P for c in cc]
    assert all((x_cc[(j+2) % N]-16*x_cc[(j+1) % N]+x_cc[j]) % P == v[j] for j in range(N))
    assert 4*sum(omega[j][1]*aa[j] for j in range(1, 22)) % P == 31
    assert (4*sum(omega[j][1]*x_cc[j] for j in range(1, 22))-3) % P == 0
    assert 29*21 % P == 7 and 31*21 % P == 6
    return {
        'result': 'R322',
        'status': 'exact one-phase compression of the fixed R311 X/Y; remaining phase not evaluated',
        'base_input_sha256': source_sha,
        'all_44_marked_q_z_residues_recomputed': True,
        'computed_base_residue_anchor': anchor,
        'p': P,
        'omega': list(OMEGA),
        'base_z_logs': logs,
        'Pi_centered_integer_coefficients': weights,
        'Lambda': [1, -16, 1],
        'B_equals_Lambda_Pi_over_43_integer_coefficients': b,
        'V_sigma_logs': v,
        'Y_recurrence_rhs': forcing,
        'Y_log_coefficient_of_h1': aa,
        'Y_log_constant': cc,
        'X_log_coefficient_of_k1': aa,
        'X_log_constant': x_cc,
        'cyclic_recurrence_rank': rank_cyclic,
        'recurrence_plus_h0_zero_rank': rank_real,
        'recurrence_plus_h0_zero_augmented_rank': rank_augmented,
        'L_coefficient_of_h1_Y_log': coeff,
        'L_constant': constant,
        'L_coefficient_of_t1_Y_phase': 7,
        'L_coefficient_of_k1_X_log': 31,
        'L_coefficient_of_s1_X_phase': 6,
        'L_10_equivalent_Y_h1': 30,
        'L_10_equivalent_Y_t1': 26,
        'L_40_equivalent_Y_h1': 34,
        'L_40_equivalent_Y_t1': 18,
        'q_robert_product_evaluated': False,
        'upper_X_or_Y_coordinates_computed': False,
        'remaining_q_phase_computed': False,
        'actual_L_computed': False,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('source', type=Path)
    ap.add_argument('--certificate', type=Path)
    ap.add_argument('--write', type=Path)
    args = ap.parse_args()
    data = build(args.source)
    if args.certificate:
        assert json.loads(args.certificate.read_text()) == data
    if args.write:
        args.write.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')
    print('PASS: all 44 marked base residues, exact integer quotient, 44 affine recurrences, ranks 42/43, L=29*h1=7*t1=31*k1=6*s1')
    print('NOT EVALUATED: actual upper X/Y, the remaining q phase, canonical L')


if __name__ == '__main__':
    main()
