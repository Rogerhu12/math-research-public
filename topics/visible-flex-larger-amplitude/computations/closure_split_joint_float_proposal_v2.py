#!/usr/bin/env python3
"""Untrusted float proposals for the full641 R50 frequency-split inequalities.

The positive factor has427 coordinates (low+near,total,far_z).  A floating
inverse is used only to choose exact dyadic test radii and metric weights.
Every mathematical assertion must instead be checked by the separate
streaming Arb verifier on all641 original nonlinear/derivative rows.
Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction
import json
import math
from pathlib import Path
import resource
import time
import numpy as np
from closure_split_joint_io_v2 import digest, read, iter_array, metadata_without_array, label, validate_common


def lp(v):
    m, e = int(v[0]), int(v[1])
    return math.log2(m) + e if m > 0 else -math.inf


def lr(v):
    return lp([v['upper']['mantissa'], v['upper']['binary_exponent']])


def la(*values):
    out = -math.inf
    for value in values:
        out = float(np.logaddexp2(out, value))
    return out


def ls(a):
    a = np.asarray(a)
    m = float(np.max(a))
    return m + math.log2(float(np.exp2(a - m).sum())) if math.isfinite(m) else -math.inf


def rowsum(a):
    mx = np.max(a, axis=1)
    return mx + np.log2(np.exp2(a - mx[:, None]).sum(axis=1))


def powlabel(value):
    if not isinstance(value, str) or not value.startswith('2^'):
        raise ValueError('An exact power-of-two label is required')
    return int(value[2:])


def proposal_dyadic(value, bits=48):
    if not math.isfinite(value):
        raise ArithmeticError('A strictly positive finite-logarithm proposal is required')
    e = math.floor(value) - bits + 1
    # This rounding is deliberately not trusted as an interval operation.
    # The result is simply an exact positive dyadic test value.
    return [math.ceil(math.exp2(value - e)), e]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('low', 'split', 'density', 'out'):
        parser.add_argument('--' + name, type=Path, required=True)
    parser.add_argument('--physical-domain-log2', type=int, default=-30)
    parser.add_argument('--metric-target', default='3/4')
    args = parser.parse_args()
    started = time.monotonic()
    if args.out.exists():
        raise FileExistsError('Use a fresh proposal prefix')
    target_q = Fraction(args.metric_target)
    target = float(target_q)
    if not 0 < target < 1:
        raise ValueError('The proposed metric target must lie strictly between zero and one')
    hashes = {str(getattr(args, n)): digest(getattr(args, n)) for n in ('low', 'split', 'density')}
    low = read(args.low)
    split = metadata_without_array(args.split, 'gamma_rows')
    density = read(args.density)
    cells = validate_common(low, split, density, hashes, args.density)
    N = len(cells)
    dim = 3 * N + 2
    reduced_dim = 2 * N + 1
    inf, zi = 3 * N, 3 * N + 1
    G = {name: np.array([[lp(x) for x in row] for row in low['gamma_upper'][name]])
         for name in ('main', 'corr', 'base', 'remainder')}
    F = {name: np.array([lp(x) for x in low['far_z_source_upper'][name]]) for name in G}
    if any(a.shape != (N, N) for a in G.values()) or any(a.shape != (N,) for a in F.values()):
        raise ValueError('The complete low and far Green matrices are required')
    cdlog = powlabel(low['raw_D_constant'])
    zlog = split['z_log2']
    auxlog = powlabel(low['auxiliary_far_z_bound'])
    if auxlog >= zlog - 1:
        raise ValueError('The auxiliary real tail lies outside the stated far working ball')
    beta = np.array([lr(r['B_low']) + 2 + cdlog + 2 * zlog for r in low['rows']])
    beta_z = lr(low['E_B_low']) + 2 + cdlog + zlog
    del low
    A = np.array([lr(r['V_over_w_upper']) for r in density['rows']])
    gamma = lr(density['gamma_high'])
    del density
    far = {g: np.array([lr(r['far_boundary_' + g]) for r in split['cells']]) for g in ('near', 'rest')}
    pure = {g: np.array([lr(r['pure_low_residual_' + g]) for r in split['cells']]) for g in ('near', 'rest')}
    deep, pure_inf = lr(split['deep_high_boundary']), lr(split['pure_low_infinite_residual'])
    H = {g: np.full((N, N), -math.inf) for g in ('near', 'rest')}
    count = 0
    for k, row in enumerate(iter_array(args.split, 'gamma_rows')):
        if row['output_cell'] != 12 + k or len(row['sources']) != N - k:
            raise ValueError('The true split causal row coverage changed')
        for n, entry in enumerate(row['sources'], k):
            if entry['source_cell'] != 12 + n:
                raise ValueError('The true split causal source coverage changed')
            for g in H:
                H[g][k, n] = lr(entry[g + '_gamma'])
            count += 1
    if count != N * (N + 1) // 2:
        raise ValueError('The two complete causal triangles are required')
    rho = math.exp2(args.physical_domain_log2)
    one = math.log2(1 + rho)
    C0 = np.logaddexp2(G['main'], G['corr'] + math.log2(3))
    E = np.logaddexp2(G['base'] + math.log2(3) + args.physical_domain_log2,
                     G['remainder'] + math.log2(216) + 2 * one)
    F0 = np.logaddexp2(F['main'], F['corr'] + math.log2(3)) - zlog
    FE = np.logaddexp2(F['base'] + math.log2(3) + args.physical_domain_log2,
                      F['remainder'] + math.log2(216) + 2 * one) - zlog
    slopes = np.logaddexp2(math.log2(3) + one, math.log2(216) + A + 2 * one)
    HN, HR = H['near'] + slopes[None, :], H['rest'] + slopes[None, :]
    IC = gamma + slopes
    del G, F, H

    def B_apply(x):
        a = np.logaddexp2(x[:N], x[N:2 * N])
        t = np.logaddexp2(np.logaddexp2(a, x[2 * N:3 * N]), x[inf])
        return np.concatenate([a, t, [x[zi]]])

    def C_apply(y):
        a, t, z = y[:N], y[N:2 * N], y[-1]
        out = np.full(dim, -math.inf)
        out[:N] = np.logaddexp2(np.logaddexp2(rowsum(C0 + a[None, :]), rowsum(E + t[None, :])), beta + z)
        out[N:2 * N] = np.logaddexp2(rowsum(HN + t[None, :]), far['near'] + 2 + z)
        out[2 * N:3 * N] = np.logaddexp2(rowsum(HR + t[None, :]), far['rest'] + 2 + z)
        out[inf] = la(ls(IC + t), deep + 2 + z)
        out[zi] = la(ls(F0 + a), ls(FE + t), beta_z + z)
        return out

    b = np.full(dim, -math.inf)
    b[N:2 * N] = np.logaddexp2(pure['near'], far['near'])
    b[2 * N:3 * N] = np.logaddexp2(pure['rest'], far['rest'])
    b[inf] = la(pure_inf, deep)
    R = np.full((reduced_dim, reduced_dim), -math.inf)
    R[:N, :N] = C0
    R[N:2 * N, :N] = C0
    R[:N, N:2 * N] = np.logaddexp2(E, HN)
    R[N:2 * N, N:2 * N] = np.logaddexp2(np.logaddexp2(E, HN), np.logaddexp2(HR, IC[None, :]))
    R[:N, -1] = np.logaddexp2(beta, far['near'] + 2)
    R[N:2 * N, -1] = np.logaddexp2(np.logaddexp2(beta, far['near'] + 2), np.logaddexp2(far['rest'] + 2, deep + 2))
    R[-1, :N], R[-1, N:2 * N], R[-1, -1] = F0, FE, beta_z
    scale = np.zeros(reduced_dim)
    history = []
    for iteration in range(96):
        y = rowsum(R + scale[None, :])
        ratios = y - scale
        if iteration in (0, 3, 15, 31, 63, 95):
            history.append(dict(iteration=iteration + 1,
                collatz_log2_lower_float=float(np.min(ratios)),
                collatz_log2_upper_float=float(np.max(ratios))))
        scale = y - np.max(y)
    scale = np.floor(scale)
    exponents = R + scale[None, :] - scale[:, None]
    if np.max(exponents) > 1000:
        raise ArithmeticError('The diagnostic scaling still overflows')
    lost = ~np.isfinite(exponents) | (exponents < -1074)
    matrix = np.exp2(np.maximum(exponents, -1074))
    matrix[lost] = 0
    spectral = float(np.max(np.abs(np.linalg.eigvals(matrix))))
    seed = np.logaddexp2(b, C_apply(B_apply(b)))
    if not np.isfinite(seed).all():
        raise ArithmeticError('A positive proposal seed is missing in an original coordinate')
    rhs_log = B_apply(seed) - scale
    rhs_shift = float(np.max(rhs_log))
    rhs = np.exp2(np.maximum(rhs_log - rhs_shift, -1074))
    rhs[~np.isfinite(rhs_log)] = 0
    system = target * np.eye(reduced_dim) - matrix
    sol = np.linalg.solve(system, rhs)
    residual = float(np.max(np.abs(system @ sol - rhs)))
    bad = [int(i) for i in np.flatnonzero(sol <= 0)]
    result = dict(status='Float proposal only; no joint inequality has been proved',
        mathematical_gates_paid=False, original_dimension=dim, proposal_dimension=reduced_dim,
        physical_domain_log2=args.physical_domain_log2, metric_target=str(target_q),
        exact_supports=dict(low=[2, 92], near=[94, 184], rest=[186, 8190], infinite=[8192, None]),
        factor='J=C B; B=(low+near,low+near+rest+infinite,far_z). Only proposals use BC.',
        complete_mean_and_pointwise_inverse=True, independent_far_parameter=True,
        spectral_radius_float=spectral, collatz_history=history,
        condition_2_float=float(np.linalg.cond(system)), inverse_residual_inf_float=residual,
        nonpositive_proposal_coordinates=bad,
        scaled_underflow_count=int(np.count_nonzero(lost & np.isfinite(exponents))),
        proposal_only='Float underflows, eigenvalues and inverse signs do not pay any mathematical gate. The serialized radii and weights are exact dyadic guesses for independent original641 Arb checks.',
        input_hashes=hashes, source_sha256=digest(Path(__file__)),
        helper_hashes={name: digest(Path(__file__).with_name(name)) for name in ('closure_split_joint_io.py','closure_split_joint_io_v2.py')},
        numpy_version=np.__version__)
    if not bad:
        y = scale + rhs_shift + np.log2(sol)
        Wlog = np.logaddexp2(seed, C_apply(y)) - math.log2(target)
        JWlog = C_apply(B_apply(Wlog))
        # A common radius proportional to W avoids zero forcing slack on
        # the low/far coordinates.  The separate verifier checks the actual
        # nonlinear map, not merely this sufficient linear construction.
        multiplier_log2 = math.ceil(float(np.max(b - Wlog)) + math.log2(2 / (1 - target)))
        rlog = Wlog + multiplier_log2
        total_log = B_apply(rlog)[N:2 * N]
        result.update(proposal_rows=[dict(index=i, **label(i, N),
            radius=proposal_dyadic(float(rlog[i])), metric_weight=proposal_dyadic(float(Wlog[i])),
            radius_log2_float=float(rlog[i]), weighted_derivative_log2_float=float(JWlog[i] - Wlog[i]))
            for i in range(dim)],
            radius_weight_multiplier_log2=multiplier_log2,
            maximum_total_radius_log2_float=float(np.max(total_log)),
            far_normalized_radius_log2_float=float(rlog[zi]),
            maximum_weighted_derivative_float=math.exp2(float(np.max(JWlog - Wlog))))
    result.update(elapsed_seconds=time.monotonic() - started,
                  peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    args.out.write_text(json.dumps(result, indent=2, allow_nan=False) + '\n')
    print(json.dumps(dict(event='done', output=str(args.out), spectral_radius_float=spectral,
        nonpositive_proposals=len(bad),
        maximum_total_radius_log2_float=result.get('maximum_total_radius_log2_float'),
        maximum_weighted_derivative_float=result.get('maximum_weighted_derivative_float'),
        seconds=result['elapsed_seconds'], RSS_KiB=result['peak_RSS_KiB'])), flush=True)


if __name__ == '__main__':
    main()
