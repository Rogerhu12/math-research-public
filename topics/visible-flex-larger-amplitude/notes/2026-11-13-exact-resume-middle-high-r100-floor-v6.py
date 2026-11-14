#!/usr/bin/env python3
"""Actual R100-domain finite/infinite-high fixed-floor causal budget.

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The low46 centre is held fixed.  The high unknown gets its own balanced
radius on every true comparison block; a global high radius is never
inserted as though it were already present near the initial head.
Complete mean, inverse, three finite source materials and both true high
initial components are retained.  All decisions use exact fractions.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time


def digest(p):
    h = hashlib.sha256()
    with Path(p).open('rb') as stream:
        for part in iter(lambda: stream.read(1 << 20), b''):
            h.update(part)
    return h.hexdigest()


def read(p):
    raw = Path(p).read_bytes()
    return json.loads(gzip.decompress(raw) if Path(p).suffix == '.gz' else raw)


def ex(v):
    if isinstance(v, list):
        return F(int(v[0])) * F(2) ** int(v[1])
    if 'upper' in v:
        return ex(v['upper'])
    if 'mantissa' in v:
        return F(int(v['mantissa'])) * F(2) ** int(v['binary_exponent'])
    return F(int(v['numerator']), int(v['denominator']))


def rec(v):
    return dict(numerator=str(v.numerator), denominator=str(v.denominator), display_only=float(v))


def up96(v):
    if v <= 0:
        raise ArithmeticError('A positive radius or metric weight is required')
    unit = F(2) ** (v.numerator.bit_length() - v.denominator.bit_length() - 96)
    return (v // unit + 1) * unit


def named_hash(mapping, name):
    found = [v for k, v in mapping.items() if Path(k).name == name]
    if len(found) != 1:
        raise ValueError('Exactly one input identity required for ' + name)
    return found[0]


def inverse_positive_matrix(diagonal, matrix, vector):
    a, b, c, d = matrix
    u, v = diagonal - a, diagonal - d
    det = u * v - b * c
    if min(u, v, det) <= 0 or min(b, c) < 0:
        return None
    return ((v * vector[0] + b * vector[1]) / det,
            (c * vector[0] + u * vector[1]) / det)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for n in ('finite', 'finite-resource', 'source', 'head', 'common', 'out-prefix', 'high-kernel', 'high-resource', 'balanced', 'r100-head', 'r100-resource'):
        ap.add_argument('--' + n, type=Path, required=True)
    ap.add_argument('--allow-incomplete-finite', action='store_true')
    ap.add_argument('--transverse-radius',default='1')
    args = ap.parse_args(); started = time.monotonic()
    output = Path(str(args.out_prefix) + '.json.gz'); summary = Path(str(args.out_prefix) + '-summary.json')
    if output.exists() or summary.exists():
        raise FileExistsError('Fresh actual finite/high budget output required')
    finite, usage, source, head, common = [read(getattr(args, n)) for n in
        ('finite', 'finite_resource', 'source', 'head', 'common')]
    M = common['leaf_primary']['high_cutoff']; case = next(r for r in common['cases'] if r['high_threshold'] == M)
    coverage = [m for lo, hi in finite['windows'] for m in range(lo, hi + 1, 2)]
    complete_finite = coverage == list(range(94, M, 2))
    if not complete_finite and not args.allow_incomplete_finite:
        raise ValueError('The complete enlarged finite middle is required before a full nonlow claim')
    finite_case = finite.get('fixed_common_strip', finite.get('fixed_strip'))
    gates = dict(paid_finite_actual_inputs=finite['all_gates'] and all(finite['gates'].values()),
        finite_formal_exit_zero=usage['exitcode'] == 0 and usage['termination_signal'] is None,
        same_actual_common_strip=finite_case == case and common['all_identity_gates'] and all(common['gates'].values()),
        same_complete_source=named_hash(finite['input_hashes'], args.source.name) == digest(args.source),
        same_true_head=named_hash(finite['input_hashes'], args.head.name) == digest(args.head),
        paid_complete_source=source['all_gates'] and all(source['gates'].values()),
        paid_complete_true_head=head['all_gates'] and all(head['gates'].values()),
        actual_common_strip_floor=ex(case['common_terminal_strip']) > F(1, 64),
        high_head_is_subset_original_infinite_band=M >= 8192,
        complete_high_centre_source_is_subset_original_high=M >= 5760)
    if not all(gates.values()):
        raise ArithmeticError('A complete actual input or shared-space identity failed: ' + str(gates))
    partition = finite['comparison_partition']; count = len(partition)
    if count != 25 or len(finite['rows']) != 25:
        raise ValueError('All25 exact original comparison blocks must remain')
    G = {p: [[ex(v['value']) for v in row['all_material_rows'][str(p)]] for row in finite['rows']] for p in (2, 1, 0)}
    V = [ex(row['V_max']) for row in finite['rows']]
    r100 = read(args.r100_head); r100_usage = read(args.r100_resource); tr = F(args.transverse_radius)
    if not (0 <= tr <= 1 and r100['all_gates'] and all(r100['gates'].values())
            and r100_usage['exitcode'] == 0 and r100_usage['termination_signal'] is None
            and r100['input_identities']['r78']['sha256'] == digest(args.head)
            and r100['input_identities']['trace']['sha256'] == named_hash(read(args.balanced)['input_hashes'],'2026-11-12-closure-strong-true-cut-trace-r1.json')
            and r100['true_far_added_once_per_whole_mass'] and r100['complete_mean_inverse_and_far_retained']):
        raise ArithmeticError('Actual R100 whole-domain high head and same physical trace required')
    bands = r100['complete_high']['head']['bands']
    if [b['name'] for b in bands] != ['near94to184','rest186to8190','infinite8192up']:
        raise ValueError('All three true R100 head bands required')
    old_masses = [ex(v) for v in head['complete_coarse_trace_rows']['head']['high_bands_value_upper']]
    head_masses = [ex(b['uniform']['uniform_value_upper']) if tr == 1 else old_masses[k]+tr*ex(b['transverse_global_lipschitz']) for k,b in enumerate(bands)]
    Hfinite = [sum((mass*ex(row['given_band_gains'][band]['gain']) for mass,band in zip(head_masses,('near','rest','infinite'))),F(0)) for row in finite['rows']]
    gates['actual_R100_head_all_three_bands_reweighted_once'] = True
    Rfinite = [ex(row['complete_shared_centre_source']) for row in finite['rows']]
    C, B, D, Binv = F(10), F(18555), F(257), F(256)
    GH = ex(case['full_R93_source_inverse'])
    if GH != (1 + F(1, M)) * (1 << 18):
        raise ArithmeticError('The complete weak-to-strong high source inverse changed')
    high_packet = read(args.high_kernel); high_usage = read(args.high_resource); balanced = read(args.balanced)
    if not (high_packet['all_gates'] and all(high_packet['gates'].values()) and high_usage['exitcode'] == 0
            and high_usage['termination_signal'] is None and high_packet['common_strip'] == case
            and high_packet['high_cutoff'] == M and high_packet['comparison_partition'] == partition
            and high_packet['head_strip_gap_already_paid']
            and high_packet['gates'].get('actual_ordered_balanced_target_six_columns_and_head_paid',False)
            and named_hash(high_packet['input_hashes'], args.balanced.name) == digest(args.balanced)):
        raise ArithmeticError('The actual complete high localV/source-frame bridge must be paid')
    physical_high_blocks = {5}
    floors = list(map(ex,high_packet['target_V_floors']))
    if not (high_packet['gates'].get('fixed_positive_target_V_plus_floor_paid',False) and len(floors)==count and floors[21]>0 and all(v==0 for i,v in enumerate(floors) if i!=21)):
        raise ArithmeticError('Exactly the declared fixed high target floor must be paid')
    KH = {normalization: {p: [[F(0) for j in range(i+1)] for i in range(count)] for p in (2,1,0)}
          for normalization in ('physical_source','already_divided_by_frame')}
    high_head_mass = head_masses[2]
    boundary_B = ex(balanced['balanced_B_lower'])
    first_b = ex(high_packet['first_actual_frame'])
    delta = ex(high_packet['head_strip_gap'])
    d = min(F(1), up96(1/(1+M*delta/65536)))
    for _ in range(16):d = min(F(1), up96(d*d))
    balanced_head = high_head_mass * max(1/boundary_B, 1/first_b) * d
    high_head = []
    for i,row in enumerate(high_packet['rows']):
        if ex(row['V_max']) != V[i] or len(row['source_rows']) != i+1:
            raise ValueError('The high bridge must retain the identical actualV and all causal source positions')
        cols = row['initial_shifted_localV_separate_component_sups']
        high_head.append(high_head_mass*max(ex(row['initial_balanced_column_sups'][0])/boundary_B,ex(row['initial_balanced_column_sups'][1])) if i in physical_high_blocks else high_head_mass *
                         max(sum(map(ex,cols[0]),F(0))/boundary_B,sum(map(ex,cols[1]),F(0))))
        for j,source_row in enumerate(row['source_rows']):
            if source_row['source_comparison_block'] != j or len(source_row['density_rows']) != 6:
                raise ValueError('Both complete three-material high source normalizations are required')
            for density in source_row['density_rows']:
                normalization,power = density['source_normalization'],density['V_power']
                value = max(ex(density['shifted_localV_strong_output_row']),ex(density['shifted_P_sup'])+ex(density['shifted_K_sup']))
                if i in physical_high_blocks:
                    value = ex(density['balanced_strong_output_row'])
                KH[normalization][power][i][j] = value
    gates['complete_actual_mixed_high_spaces_and_six_source_columns'] = True
    high_centre = ex(source['complete_infinite_high_shared_mass'])
    radii = []; hradii = []; W = []; rows = []; failure = None; q = F(1, 2)

    def finite_feedback(i, j, r, h):
        if j not in physical_high_blocks:
            t,z = r+h,floors[j]*h
            return G[2][i][j]*(4*C*t+2*t*t)+4*G[1][i][j]*(C+t)*z+2*G[0][i][j]*z*z
        physical_h = B*h
        return (G[2][i][j]*(4*C*r+2*r*r)
                +4*G[1][i][j]*(C+r)*physical_h+2*G[0][i][j]*physical_h*physical_h)

    def high_feedback(i, j, r, h):
        A = KH['physical_source']; Q = KH['already_divided_by_frame']
        if j not in physical_high_blocks:
            t,z = r+h,floors[j]*h
            return A[2][i][j]*(4*C*t+2*t*t)+4*A[1][i][j]*(C+t)*z+2*A[0][i][j]*z*z
        return (A[2][i][j]*(4*C*r+2*r*r)
                +4*Q[1][i][j]*D*(C+r)*h+2*Q[0][i][j]*D*B*h*h)

    def derivative_block(i, j, r, h):
        A = KH['physical_source']; Q = KH['already_divided_by_frame']
        if j not in physical_high_blocks:
            t,e,z = r+h,floors[j],floors[j]*h
            return (4*((C+t)*G[2][i][j]+z*G[1][i][j]),
                    4*((C+t)*(G[2][i][j]+e*G[1][i][j])+z*(G[1][i][j]+e*G[0][i][j])),
                    4*((C+t)*A[2][i][j]+z*A[1][i][j]),
                    4*((C+t)*(A[2][i][j]+e*A[1][i][j])+z*(A[1][i][j]+e*A[0][i][j])))
        physical_h = B*h
        return (4*((C+r)*G[2][i][j]+physical_h*G[1][i][j]),
                4*B*((C+r)*G[1][i][j]+physical_h*G[0][i][j]),
                4*(C+r)*A[2][i][j]+16*D*h*Q[1][i][j],
                4*D*((C+r)*Q[1][i][j]+physical_h*Q[0][i][j]))

    for i, part in enumerate(partition):
        hf = Hfinite[i] + Rfinite[i]
        hh = high_head[i] + high_centre * sum(KH['physical_source'][2][i],F(0))
        af = hf + sum((finite_feedback(i, j, radii[j], hradii[j]) for j in range(i)), F(0))
        ah = hh + sum((high_feedback(i, j, radii[j], hradii[j]) for j in range(i)), F(0))
        linear = ((4*C*G[2][i][i],4*C*B*G[1][i][i],4*C*KH['physical_source'][2][i][i],4*C*D*KH['already_divided_by_frame'][1][i][i])
                  if i in physical_high_blocks else
                  (4*C*G[2][i][i],4*C*(G[2][i][i]+floors[i]*G[1][i][i]),4*C*KH['physical_source'][2][i][i],4*C*(KH['physical_source'][2][i][i]+floors[i]*KH['physical_source'][1][i][i])))
        seed = inverse_positive_matrix(F(1), linear, (af, ah))
        if seed is None:
            failure = dict(block=i, reason='positive_affine_two_by_two_inverse_failed', matrix=[rec(v) for v in linear]); break
        r, h = up96(2 * seed[0]), up96(2 * seed[1])
        radius_search = []
        for radius_iteration in range(64):
            image_f = af + finite_feedback(i, i, r, h)
            image_h = ah + high_feedback(i, i, r, h)
            radius_search.append(dict(finite=rec(r), high=rec(h), finite_ratio=rec(image_f/r), high_ratio=rec(image_h/h)))
            if image_f < r and image_h < h:
                break
            r, h = max(r,up96(F(9,8)*image_f)), max(h,up96(F(9,8)*image_h))
            if (C+r)*V[i]+(B*h if i in physical_high_blocks else h*(V[i]+floors[i])) >= F(2)**-34:
                break
        image_f = af + finite_feedback(i, i, r, h)
        image_h = ah + high_feedback(i, i, r, h)
        radii.append(r); hradii.append(h)
        domain = (C+r)*V[i]+(B*h if i in physical_high_blocks else h*(V[i]+floors[i]))
        blocks = [derivative_block(i, j, radii[j], hradii[j]) for j in range(i + 1)]
        vf = 1 + sum((blocks[j][0] * W[j][0] + blocks[j][1] * W[j][1] for j in range(i)), F(0))
        vh = 1 + sum((blocks[j][2] * W[j][0] + blocks[j][3] * W[j][1] for j in range(i)), F(0))
        metric = inverse_positive_matrix(q, blocks[i], (vf, vh))
        if metric is None:
            failure = dict(block=i, reason='complete_derivative_two_by_two_half_metric_failed',
                           matrix=[rec(v) for v in blocks[i]], finite_radius=rec(r), high_radius=rec(h),
                           finite_image=rec(image_f), high_image=rec(image_h), domain=rec(domain)); break
        wf, wh = up96(metric[0]), up96(metric[1]); W.append((wf, wh))
        dist_f = sum((blocks[j][0] * W[j][0] + blocks[j][1] * W[j][1] for j in range(i + 1)), F(0)) / wf
        dist_h = sum((blocks[j][2] * W[j][0] + blocks[j][3] * W[j][1] for j in range(i + 1)), F(0)) / wh
        rows.append(dict(index=i, partition=part, V_max=rec(V[i]), finite_radius=rec(r), high_radius=rec(h),
            high_space=('balanced_physical' if i in physical_high_blocks else 'physical_local_V_plus_floor'),
            target_V_floor=rec(floors[i]),W_max=rec(V[i]+floors[i]),
            actual_radius_search=radius_search,
            complete_finite_image=rec(image_f), complete_high_image=rec(image_h),
            finite_image_over_radius=rec(image_f / r), high_image_over_radius=rec(image_h / h),
            finite_strict_slack=rec(r - image_f), high_strict_slack=rec(h - image_h),
            true_finite_head_and_centre=rec(hf), true_high_head_and_complete_centre=rec(hh),
            finite_previous_sources=rec(af - hf), high_previous_sources=rec(ah - hh),
            actual_complete_mean_domain=rec(domain), finite_distance_weight=rec(wf), high_distance_weight=rec(wh),
            finite_complete_weighted_distance_row=rec(dist_f), high_complete_weighted_distance_row=rec(dist_h),
            complete_causal_derivative_blocks=[[rec(v) for v in b] for b in blocks],
            all_finite_source_materials={str(p): [rec(v) for v in G[p][i]] for p in (2, 1, 0)},
            all_high_source_materials={n:{str(p):[rec(v) for v in KH[n][p][i]] for p in (2,1,0)} for n in KH},
            gates=dict(finite_strict_selfmap=image_f < r, high_strict_selfmap=image_h < h,
                actual_whole_ball_mean_domain_below_two_minus34=domain < F(2) ** -34,
                full_finite_distance_below_half=dist_f < q, full_high_distance_below_half=dist_h < q)))
    gates['all25_coupled_selfmap_domain_and_two_distance_rows'] = len(rows) == count and all(all(r['gates'].values()) for r in rows)
    passed = all(gates.values()) and failure is None
    physical_f = sum((ex(row['finite_radius']) * ex(row['V_max']) for row in rows), F(0))
    physical_h = sum(((B if row['index'] in physical_high_blocks else ex(row['W_max']))*ex(row['high_radius']) for row in rows),F(0))
    result = dict(schema='visible-flex-actual-R100-middle-high-fixed-floor-v6', author='exact_closure (GPT-6 Astra Pro; AI-assisted)',
        all_gates=passed, gates=gates, failure=failure,
        status=('All actual causal finite/high budget gates pass' if passed else 'An actual sufficient finite/high comparison failed'),
        fixed_point_claimed=passed, full_infinite_nonlow_block_closed=passed and complete_finite,
        finite_gap_still_omitted=not complete_finite, finite_positive_mode_count=len(coverage),
        high_cutoff=M, high_modes_all_signed_even_at_or_above_cutoff=True,
        equations=['v = true_finite_head + G_M Pi_M N(C_L+v+H)',
                   'H = true_high_head + G_H Pi_H N(C_L+v+H)'],
        parameter_domain='R100 six original complex R74 axes of radius1 and forty R59 weighted-l1 axes of the exact stated transverse radius; common real phase; same complete R101 low46 centre',
        transverse_radius=rec(tr),actual_R100_head_band_masses=[rec(v) for v in head_masses],
        head_at_zero_transverse_uses_R100_R74_identification=True,
        fixed_common_strip=case, complete_mean_and_inverse_retained=True,
        same_original_background_and10793_leaves=True, comparison_partition=partition, rows=rows,
        balanced_high_source_inverse=rec(GH), physical_high_conversion=rec(B), high_direction_divided_by_frame=rec(D),
        physical_direction_to_high_source=rec(Binv), true_complete_high_head_mass=rec(high_head_mass), high_head_lift_rows=[rec(v) for v in high_head],
        complete_high_centre_shared_source=rec(high_centre),
        high_source_block_kernel='Actual ordered six-column kernel in localV or balanced target norm as declared; every source frame and attenuation retained; causal j<=i only',
        physical_high_comparison_blocks=sorted(physical_high_blocks),fixed_high_V_floors=[rec(v) for v in floors], high_cross_derivative_uses_paid_complete_Hessian16=True,
        high_radius_is_local_to_each_true_block=True, no_global_high_radius_injected_at_early_sources=True,
        complete_finite_physical_norm_upper=rec(physical_f), complete_high_physical_norm_upper=rec(physical_h),
        maximum_whole_ball_physical_domain=rec(max((ex(row['actual_complete_mean_domain']) for row in rows), default=F(0))),
        maximum_finite_image_ratio=rec(max((ex(row['finite_image_over_radius']) for row in rows), default=F(0))),
        maximum_high_image_ratio=rec(max((ex(row['high_image_over_radius']) for row in rows), default=F(0))),
        maximum_complete_weighted_distance=rec(max((max(ex(row['finite_complete_weighted_distance_row']), ex(row['high_complete_weighted_distance_row'])) for row in rows), default=F(0))),
        low_feedback_equation_closed=False, all46_cut_closed=False, full_outer_or_closed_surface_claimed=False,
        input_hashes={str(getattr(args, n)): digest(getattr(args, n)) for n in ('finite', 'finite_resource', 'source', 'head', 'common', 'high_kernel', 'high_resource', 'balanced', 'r100_head', 'r100_resource')},
        source_sha256=digest(__file__), elapsed_seconds=time.monotonic() - started,
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    with output.open('wb') as raw:
        with gzip.GzipFile(filename='', mode='wb', fileobj=raw, mtime=0, compresslevel=9) as packed:
            packed.write((json.dumps(result, separators=(',', ':')) + '\n').encode())
    if output.stat().st_size >= 5_000_000:
        raise ArithmeticError('Partition the exact completed output before archival')
    short = {k: v for k, v in result.items() if k != 'rows'}
    short['primary'] = dict(path=str(output), bytes=output.stat().st_size, sha256=digest(output))
    summary.write_text(json.dumps(short, indent=2) + '\n')
    print(json.dumps(dict(all_gates=passed, failure=failure, complete_finite=complete_finite, rows=len(rows),
        finite_physical=float(physical_f), high_physical=float(physical_h),
        maximum_domain=result['maximum_whole_ball_physical_domain']['display_only'],
        maximum_distance=result['maximum_complete_weighted_distance']['display_only'],
        elapsed_seconds=result['elapsed_seconds'], peak_rss_kib=result['peak_rss_kib'])), flush=True)


if __name__ == '__main__':
    main()
