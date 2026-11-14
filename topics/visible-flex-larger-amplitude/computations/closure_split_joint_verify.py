#!/usr/bin/env python3
"""Strict full641 common-strip box check using untrusted dyadic proposals.

No matrix inverse is performed.  All original low/near/rest/infinite/far
nonlinear map rows, complete mean domains and weighted derivative rows
are evaluated with192-bit Arb.  The high triangles are streamed one cell
at a time.  The provenance of a test vector is irrelevant to its validity.
Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction
import gzip
import json
from pathlib import Path
import resource
import time
from flint import arb, ctx
from closure_real_head_source_enclosure import power2, ball_record, exact_q
from closure_real_head_green_enclosure import ball
from closure_split_joint_io import digest, read, iter_array, metadata_without_array, label, validate_common


def compact(value):
    if not isinstance(value, list) or len(value) != 2 or any(type(x) is not int for x in value):
        raise ValueError('Every test value and compact upper must be an exact dyadic pair')
    return arb(value[0]) * power2(value[1])


def labelled_power(value):
    if not isinstance(value, str) or not value.startswith('2^'):
        raise ValueError('An exact power-of-two label is required')
    return power2(int(value[2:]))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('low', 'split', 'density', 'proposal', 'out'):
        parser.add_argument('--' + name, type=Path, required=True)
    args = parser.parse_args()
    ctx.prec = 192
    started = time.monotonic()
    summary_path = args.out.with_name(args.out.name.removesuffix('.json.gz') + '-summary.json')
    if args.out.exists() or summary_path.exists():
        raise FileExistsError('Use a fresh strict verification prefix')
    if args.out.suffix != '.gz':
        raise ValueError('The original641 row ledger must be compressed')
    hashes = {str(getattr(args, n)): digest(getattr(args, n)) for n in ('low', 'split', 'density', 'proposal')}
    low = read(args.low)
    split = metadata_without_array(args.split, 'gamma_rows')
    density = read(args.density)
    proposal = read(args.proposal)
    cells = validate_common(low, split, density, hashes, args.density)
    for name in ('low', 'split', 'density'):
        path = str(getattr(args, name))
        if proposal['input_hashes'].get(path) != hashes[path]:
            raise ValueError('The test vector was built from different exact inputs')
    N = len(cells)
    dim, inf, zi = 3 * N + 2, 3 * N, 3 * N + 1
    if proposal['original_dimension'] != dim or len(proposal.get('proposal_rows', [])) != dim:
        raise ValueError('All641 original positive test radii and weights are required')
    r, W = [], []
    for i, row in enumerate(proposal['proposal_rows']):
        if row['index'] != i or any(row[k] != v for k, v in label(i, N).items()):
            raise ValueError('A test coordinate was reordered or omitted')
        r.append(compact(row['radius']))
        W.append(compact(row['metric_weight']))
    if not all(v > 0 for v in r + W):
        raise ValueError('Every original coordinate needs a strictly positive exact test value')
    rho = power2(proposal['physical_domain_log2'])
    target = exact_q(Fraction(proposal['metric_target']))
    if not 0 < rho < 1 or not 0 < target < 1:
        raise ValueError('The positive working and proposed contraction domains are invalid')
    A = [ball(row['V_over_w_upper']).upper() for row in density['rows']]
    ghi = ball(density['gamma_high']).upper()
    zstar = power2(split['z_log2'])
    zaux = labelled_power(low['auxiliary_far_z_bound'])
    CD = labelled_power(low['raw_D_constant'])
    if not zaux < zstar / 2:
        raise ValueError('The auxiliary exact tail needs its proved interior far margin')
    a = [(r[n] + r[N + n]).upper() for n in range(N)]
    t = [(a[n] + r[2 * N + n] + r[inf]).upper() for n in range(N)]
    aw = [(W[n] + W[N + n]).upper() for n in range(N)]
    tw = [(aw[n] + W[2 * N + n] + W[inf]).upper() for n in range(N)]
    poly = [(x + x * x + x * x * x / 3).upper() for x in t]
    square = [(arb(3) / 2 * x * x).upper() for x in t]
    kval = [(3 * t[n] + square[n] + 216 * A[n] * poly[n]).upper() for n in range(N)]
    slopes = [(3 * (1 + rho) + 216 * A[n] * (1 + rho) ** 2).upper() for n in range(N)]
    images, jw, constant = [[arb(0) for _ in range(dim)] for _ in range(3)]
    families = ('main', 'corr', 'base', 'remainder')
    if any(len(low['gamma_upper'][name]) != N or any(len(row) != N for row in low['gamma_upper'][name])
           or len(low['far_z_source_upper'][name]) != N for name in families):
        raise ValueError('The complete low/far Green domain is unavailable')
    beta_low = [(ball(row['B_low']).upper() * 4 * CD * zstar * zstar).upper() for row in low['rows']]
    beta_z = (ball(low['E_B_low']).upper() * 4 * CD * zstar).upper()
    for k in range(N):
        im, der = arb(0), arb(0)
        for n in range(N):
            gm, gc, gq, gr = [compact(low['gamma_upper'][name][k][n]) for name in families]
            if not all(v >= 0 for v in (gm, gc, gq, gr)):
                raise ValueError('A positive upper kernel contains a negative entry')
            c0 = (gm + 3 * gc).upper()
            ep = (3 * rho * gq + 216 * (1 + rho) ** 2 * gr).upper()
            im += c0 * a[n] + gq * square[n] + 216 * gr * poly[n]
            der += c0 * aw[n] + ep * tw[n]
        images[k] = (im + beta_low[k] * r[zi]).upper()
        jw[k] = (der + beta_low[k] * W[zi]).upper()
    fim, fder = arb(0), arb(0)
    for n in range(N):
        fm, fc, fq, fr = [compact(low['far_z_source_upper'][name][n]) for name in families]
        if not all(v >= 0 for v in (fm, fc, fq, fr)):
            raise ValueError('The positive far upper contains a negative entry')
        f0 = (fm + 3 * fc).upper()
        fe = (3 * rho * fq + 216 * (1 + rho) ** 2 * fr).upper()
        fim += f0 * a[n] + fq * square[n] + 216 * fr * poly[n]
        fder += f0 * aw[n] + fe * tw[n]
    images[zi] = (fim / zstar + beta_z * r[zi]).upper()
    jw[zi] = (fder / zstar + beta_z * W[zi]).upper()
    # The full exact low/far source input is now consumed; release its four
    # large compact matrices before streaming the complete high triangles.
    low_far_scale = low['far_scale_S']
    del low
    count = 0
    for k, row in enumerate(iter_array(args.split, 'gamma_rows')):
        if row['output_cell'] != 12 + k or len(row['sources']) != N - k:
            raise ValueError('The original split output-cell coverage differs')
        im = {group: arb(0) for group in ('near', 'rest')}
        der = {group: arb(0) for group in ('near', 'rest')}
        for n, entry in enumerate(row['sources'], k):
            if entry['source_cell'] != 12 + n:
                raise ValueError('The original split source-cell coverage differs')
            for group in ('near', 'rest'):
                h = ball(entry[group + '_gamma']).upper()
                if not h >= 0:
                    raise ValueError('A causal positive upper is negative')
                im[group] += h * kval[n]
                der[group] += h * slopes[n] * tw[n]
            count += 1
        for group, offset in [('near', N), ('rest', 2 * N)]:
            pure = ball(split['cells'][k]['pure_low_residual_' + group]).upper()
            far = ball(split['cells'][k]['far_boundary_' + group]).upper()
            constant[offset + k] = (pure + far).upper()
            images[offset + k] = (constant[offset + k] + im[group]).upper()
            jw[offset + k] = (der[group] + 4 * far * W[zi]).upper()
    if count != N * (N + 1) // 2:
        raise ValueError('Both entire213-cell high causal triangles are required')
    deep = ball(split['deep_high_boundary']).upper()
    pure_inf = ball(split['pure_low_infinite_residual']).upper()
    constant[inf] = (pure_inf + deep).upper()
    images[inf] = (constant[inf] + ghi * sum(kval, arb(0))).upper()
    jw[inf] = (ghi * sum((slopes[n] * tw[n] for n in range(N)), arb(0)) + 4 * deep * W[zi]).upper()
    lip = [(jw[i] / W[i]).upper() for i in range(dim)]
    slacks = [(r[i] - images[i]).lower() for i in range(dim)]
    gates = dict(all641_positive_radii=all(v > 0 for v in r),
        all641_map_inclusions=all(v > 0 for v in slacks),
        physical_correction_domain=all(v < rho for v in t),
        complete_mean_domain=all(A[n] * (1 + t[n]) < arb(1) / 64 for n in range(N)),
        exact_R18_parameter_domain=zaux + zstar * r[zi] < zstar,
        all641_metric_weights_positive=all(v > 0 for v in W),
        all641_joint_Lipschitz=max(lip) < 1)
    rows = [dict(index=i, **label(i, N), radius=ball_record(r[i]),
        metric_weight=ball_record(W[i]), constant_term=ball_record(constant[i]),
        image=ball_record(images[i]), map_slack=ball_record(slacks[i]),
        weighted_derivative_row=ball_record(lip[i])) for i in range(dim)]
    result = dict(status=('Complete real frequency-split common-strip head box proved'
        if all(gates.values()) else 'Completed original641 strict row check; explicit gates remain unpaid'),
        whole_head_closed=all(gates.values()),
        scope='Real physical cells12..224 and the actual R18 infinite tail. The true outer0..11/prefix matching and closed-surface amplitude/reach remain separate.',
        dimension=dim, original_rows_checked=dim, high_triangle_entries=count,
        exact_supports=dict(low=[2, 92], near=[94, 184], rest=[186, 8190], infinite=[8192, None]),
        centre='The certified real auxiliary low46 field, including its complete mean and true low far lift.',
        all46_shallow_heights_fixed=True, high_shallow_heights_free=True,
        independent_far_parameter=True, complete_mean_and_pointwise_inverse=True,
        physical_domain=ball_record(rho), independent_far_z=ball_record(zstar), auxiliary_far_z=ball_record(zaux),
        far_scale_S=low_far_scale, far_strip=38, far_physical_node=225,
        low_map='(main+3corr)*(low+near) +1.5 base*total^2 +216 remainder*(total+total^2+total^3/3) + exact far low feedback',
        high_map='Separate paid near/rest wide-centre residual and true far lift + group gamma*K(total), with full K and complete mean.',
        low_support_reason='The centre has only |m|<=92; its quadratic derivative to low |m|<=92 has no input |m|>=186. No deletion is made in the full216 remainder or the quadratic correction.',
        proposition='The untrusted float inverse and its eigenvalues are not used in any gate. Every exact dyadic test radius and weight is checked directly against all641 positive map and derivative rows.',
        gates=gates, proposed_metric_target=ball_record(target),
        actual_target_met=max(lip) < target,
        failed_map_coordinates=[dict(index=i, **label(i, N)) for i in range(dim) if not slacks[i] > 0],
        failed_derivative_coordinates=[dict(index=i, **label(i, N)) for i in range(dim) if not lip[i] < 1],
        maximum_cell_total_radius=ball_record(max(t)), maximum_joint_Lipschitz=ball_record(max(lip)),
        far_normalized_radius=ball_record(r[zi]),
        maximum_derivative_coordinate=dict(index=max(range(dim), key=lambda i: lip[i]),
            **label(max(range(dim), key=lambda i: lip[i]), N)),
        rows=rows, input_hashes=hashes, source_sha256=digest(Path(__file__)),
        helper_hashes={name: digest(Path(__file__).with_name(name)) for name in (
            'closure_split_joint_io.py', 'closure_real_head_source_enclosure.py', 'closure_real_head_green_enclosure.py')},
        precision_bits=ctx.prec, no_interval_matrix_inverse=True,
        elapsed_seconds=time.monotonic() - started,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    payload = gzip.compress((json.dumps(result, separators=(',', ':')) + '\n').encode(), mtime=0)
    if len(payload) >= 5000000:
        raise ArithmeticError('Repository file size cap exceeded')
    args.out.write_bytes(payload)
    summary = {key: value for key, value in result.items() if key != 'rows'}
    summary.update(output=str(args.out), output_sha256=digest(args.out), bytes=len(payload))
    summary_path.write_text(json.dumps(summary, indent=2) + '\n')
    print(json.dumps(dict(event='done', gates=gates, maximum_Lipschitz=str(max(lip)),
        maximum_total_radius_log2=str(max(t).log() / arb(2).log()),
        seconds=result['elapsed_seconds'], RSS_KiB=result['peak_RSS_KiB'])), flush=True)


if __name__ == '__main__':
    main()
