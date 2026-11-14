#!/usr/bin/env python3
"""Independent exact saved-state audit of the restricted outer finite bootstrap.

Uses a stronger bound: sum every separately saved positive component, and
pay the saved shared complete-T source exactly once for the T mass.  No
saved acceptance Boolean or displayed floating sum is used as arithmetic.
This reviews a completed calculation; failure of its cut selfmap stays a
failure and is reported explicitly.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time

SOURCE = '31adc4e8163ab69293fcfe3a8c7b134c36d0fdc4f41260babf11669a81c42a12'
HELPER = '3d4ac8d58f9fe7683a13d29519f379fd6eff15a4cb4a0da6721e02767626a025'
HEAD = 'd89fbe3eb1cd0ea2b5bf5ff8376275dbbf3d95833de73af30f64aa926db751d6'
HEAD_EXPORT = '087c9dbdf8d7f86c96656ae439268963abc04c8f8dc1c761c34772620e0e2629'
JOINT = '36242d95a210e6aee3e38c994d0a70b61fa1fbb2df672a9ab3f4783bcca93ca1'
PARTS = ('C_low', 'low_squared', 'low_middle', 'middle_squared',
         'middle_high', 'high_squared', 'complete_T')
G = {}


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    p = Path(p)
    raw = p.read_bytes()
    return json.loads(gzip.decompress(raw) if p.suffix == '.gz' else raw)


def q(x):
    if isinstance(x, F):
        return x
    if isinstance(x, dict):
        if 'upper' in x:
            return q(x['upper'])
        if 'numerator' in x:
            return F(int(x['numerator']), int(x['denominator']))
        return F(int(x['mantissa']))*F(2)**int(x['binary_exponent'])
    if isinstance(x, list):
        return F(int(x[0]))*F(2)**int(x[1])
    if isinstance(x, (int, str)):
        return F(x)
    raise TypeError('Nonexact input')


def pack(x):
    x = F(x)
    if x < 0:
        raise ArithmeticError('Negative positive-budget value')
    if not x:
        return ['0', 0]
    e = x.numerator.bit_length()-x.denominator.bit_length()-160
    a = x/F(2)**e
    n = -((-a.numerator)//a.denominator)
    r = [str(n), e]
    if q(r) < x:
        raise ArithmeticError('Outward roundtrip failed')
    return r


def gate(label, yes):
    if label in G:
        raise ValueError('Repeated gate '+label)
    G[label] = bool(yes)
    if not yes:
        raise ArithmeticError('Unpaid saved-state audit gate: '+label)


def checked(record, label):
    gate('sha_'+label, sha(record['path']) == record['sha256'])
    return read(record['path'])


def caps(state):
    return {name: [[q(x) for x in row] for row in state[name]]
            if name in ('low_caps', 'window_caps') else list(map(q, state[name]))
            for name in ('low_caps', 'window_caps', 'finite_caps', 'high_caps', 'retained_parent94_mass_caps')}


def same_or_smaller(current, previous, label):
    for key in current:
        if key in ('low_caps', 'window_caps'):
            pairs = [(x, y) for r, s in zip(current[key], previous[key]) for x, y in zip(r, s)]
        else:
            pairs = list(zip(current[key], previous[key]))
        gate(label+'_'+key, all(0 < x <= y for x, y in pairs))


def cut_review(cut, projected, saved, label):
    gate(label+'_all_seven_components', set(cut['component_mode_caps']) == set(PARTS))
    parts = {name: list(map(q, cut['component_mode_caps'][name])) for name in PARTS}
    gate(label+'_all46_saved_components', all(len(v) == 46 for v in parts.values()))
    gate(label+'_nonnegative_all_components', all(x >= 0 for v in parts.values() for x in v))
    gate(label+'_strict_positive_infinite_cross_and_square',
         all(x > 0 for name in ('middle_high', 'high_squared') for x in parts[name]))
    # Each component was independently rounded upward.  Their saved sum is
    # another complete upper bound, possibly a few ulps above the saved total.
    conservative = [sum((parts[k][i] for k in PARTS), F(0)) for i in range(46)]
    source = cut['source_rows']
    gate(label+'_all25_source_blocks', [z['source_block'] for z in source] == list(range(25)))
    shared = F(0)
    for j, row in enumerate(source):
        one, sep = q(row['T_common_mass_paid_once']), q(row['T_separate_caps_sum'])
        gate(label+f'_shared_T_source{j}_once', 0 < one <= sep)
        shared += one
        choices = row['angular_loss_domains']
        gate(label+f'_complete_T_source{j}_five_domains', len(choices) == 5)
        deltas = [F(int(z['delta'][0]), int(z['delta'][1])) for z in choices]
        gate(label+f'_complete_T_source{j}_same_loss_grid', deltas[0] == 0 and deltas[1] > 0 and all(x == i*deltas[1] for i, x in enumerate(deltas)))
        gate(label+f'_complete_T_source{j}_full_physical_domains', all(0 < q(z['physical_domain']) < F(1, 2**34) for z in choices))
    # Positive per-source shared values are added once, not multiplied by40.
    # max with the saved upper safely also retains its final rounding.
    shared = max(shared, q(cut['complete_T_shared']))
    T = sum((sum(parts[k][6:], F(0)) for k in PARTS if k != 'complete_T'), F(0))+shared
    rows = []
    successes = []
    ratios = []
    gate(label+'_projected46_original_modes', [r['mode'] for r in projected['rows']] == list(range(2, 93, 2)))
    gate(label+'_saved46_original_modes', [r['mode'] for r in saved['rows']] == list(range(2, 93, 2)))
    for i, pr in enumerate(projected['rows']):
        b = q(pr['projected_map_value'])
        radius = F(1, 2) if i < 6 else q(pr['proposed_T_coordinate_radius'])
        complete = b+max(conservative[i], q(cut['mode_caps'][i]))
        strict = complete < radius
        ratios.append(complete/radius)
        successes.append(strict)
        gate(label+f'_same_original_axis_radius_{2*i+2}', q(saved['rows'][i]['working_coordinate_radius']) == radius)
        gate(label+f'_same_nonlow_correction_{2*i+2}', saved['rows'][i]['nonlow_cut_correction'] == cut['mode_caps'][i])
        # Strict status must be the same even under the separately saved sum.
        gate(label+f'_conservative_strict_status_{2*i+2}', strict == saved['gates']['strict_mode_'+str(2*i+2)])
        rows.append(dict(mode=2*i+2, saved_components_positive_sum=pack(conservative[i]),
                         projected_plus_conservative_nonlow=pack(complete),
                         working_radius=pack(radius), ratio=pack(complete/radius), strict=strict))
    Tmap = q(projected['T_projected_map'])+max(T, q(cut['T_l1']))
    strict_T = Tmap < F(1, 36)
    gate(label+'_same_shared_T_strict_status', strict_T == saved['gates']['strict_shared_T'])
    success = all(successes) and strict_T
    gate(label+'_complete_selfmap_status_matches', success == saved['all_strict_selfmap_gates'])
    gate(label+'_no_uniqueness_or_closed_surface', not saved['uniqueness_or_closed_surface_claimed'])
    return dict(rows=rows, all46_axes_strict=all(successes), shared_T_strict=strict_T,
                shared_complete_T_paid_once=pack(shared), conservative_T_map=pack(Tmap),
                conservative_T_radius={'numerator':'1','denominator':'36'},
                complete_strict_selfmap=success, maximum_axis_ratio=pack(max(ratios)),
                worst_mode=2*ratios.index(max(ratios))+2,
                positive_infinite_source_caps_count=92)


def main():
    start = time.monotonic()
    ap = argparse.ArgumentParser()
    ap.add_argument('--certificate', required=True)
    ap.add_argument('--resource', required=True)
    ap.add_argument('--joint', required=True)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()
    out = Path(args.out)
    if out.exists():
        raise FileExistsError('Fresh review output required')
    cert, res, joint = map(read, (args.certificate, args.resource, args.joint))
    gate('actual_formal_zero', res['exitcode'] == 0 and res['termination_signal'] is None)
    gate('actual_wait4_resource', res['resource_wrapper_sha256'] == 'bbf6c8ac8cb32cbc0f5c1e1c1c1e110ca1744c7839de0f272c172837a4ba3f59')
    gate('same_reviewed_sources', cert['source_sha256'] == SOURCE and cert['low_helper_sha256'] == HELPER)
    gate('same_original_R127_joint', sha(args.joint) == JOINT and joint['all_gates'])
    gate('actual_all_structural_gates', cert['all_gates'] and all(cert['gates'].values()))
    gate('same_existing_R127_field', cert['same_existing_R127_field'])
    gate('complete_original_problem', cert['complete_mean_inverse_and_infinite_high_retained'] and cert['all185_windows_and_original_source_materials_retained'] and cert['all186_refinement_and_parent94_constraint_retained'])
    ids = cert['inputs']
    head = checked(ids['new_head_primary'], 'head_primary')
    export = checked(ids['new_head_export'], 'head_export')
    gate('same_actual_r6_head', ids['new_head_primary']['sha256'] == HEAD and ids['new_head_export']['sha256'] == HEAD_EXPORT)
    gate('exact_restricted_domain_identity', cert['same_parameter_domain'] == export['domain'])
    gate('same_original_broad_domain', cert['original_parent_parameter_domain'] == joint['same_R100_parameter_domain'])
    projected = checked(ids['projected_profile'], 'projected_profile')
    seed = checked(ids['previous_full_bootstrap'], 'previous_full_bootstrap')
    seed_res = checked(ids['previous_full_resource'], 'previous_full_resource')
    gate('same_actual_completed_seed', seed_res['exitcode'] == 0 and seed_res['termination_signal'] is None and seed['all_gates'] and seed['same_existing_R127_field'])
    gate('same_or_wider_seed_domain', seed['same_parameter_domain'] in (cert['same_parameter_domain'], joint['same_R100_parameter_domain']))
    gate('same_original_operators_in_seed', seed['inputs']['original_outer_inputs']['sha256'] == ids['original_outer_inputs']['sha256'])
    windows = cert['windows']
    gate('exact186_partition', len(windows) == 186 and windows[:2] == [[94,94],[96,96]] and windows[-1][1] == 34814 and all(w[0] % 2 == w[1] % 2 == 0 and w[0] <= w[1] for w in windows) and all(b[0] == a[1]+2 for a,b in zip(windows,windows[1:])))
    prev = caps(seed) if 'retained_parent94_mass_caps' in seed else None
    if prev is None:
        prev = {name: [[q(x) for x in row] for row in seed[name]] if name in ('low_caps','window_caps') else list(map(q,seed[name])) for name in ('low_caps','window_caps','finite_caps','high_caps')}
        prev['retained_parent94_mass_caps'] = [row[0] for row in prev['window_caps']]
        prev['window_caps'] = [[row[0],row[0]]+row[1:] for row in prev['window_caps']]
    else:
        gate('exact186_seed_partition', seed['windows'] == windows)
    gate('same_original_full_seed_shape', len(prev['low_caps']) == 25 and all(len(r)==46 for r in prev['low_caps']) and all(len(r)==186 for r in prev['window_caps']))
    reviews = []
    for it, rec in enumerate(cert['state_records']):
        state = checked(rec, 'cycle'+str(it))
        current = caps(state)
        gate(f'cycle{it}_full_shapes', all(len(current[k])==25 for k in current) and all(len(r)==46 for r in current['low_caps']) and all(len(r)==186 for r in current['window_caps']))
        same_or_smaller(current, prev, f'cycle{it}_monotone')
        for j in range(25):
            r, h, parent = current['finite_caps'][j],current['high_caps'][j],current['retained_parent94_mass_caps'][j]
            # A saved group upper need not be <= the sum of independently
            # rounded child uppers. Both constraints are retained; their
            # intersection is consumed by the laminar greedy support.
            gate(f'cycle{it}_block{j}_parent_and_total_mass', 0 < parent <= r and all(0 < x <= r for x in current['window_caps'][j]))
            gate(f'cycle{it}_block{j}_inside_original_joint', r <= q(joint['finite_radii'][j]) and h <= q(joint['high_radii'][j]) and all(x <= q(y) for x,y in zip(current['low_caps'][j],joint['low_mode_radii'][j])))
        reviews.append(cut_review(state['complete_cut'],projected,state['projected_plus_nonlow_selfmap'],'cycle'+str(it)))
        prev=current
    gate('actual_cycle_count', len(reviews) == cert['actual_finite_cycles'])
    gate('final_state_exactly_last_saved_state', caps(cert) == prev)
    final = cut_review(cert['final_cut'],projected,cert['projected_plus_nonlow_selfmap'],'final')
    gate('final_claim_exactly_computed_status', cert['original_two_cell_low46_parameter_selfmap_certified'] == final['complete_strict_selfmap'])
    gate('no_closed_surface_claim', not cert['closed_surface_claimed'] and not cert['full_closed_surface_or_all_outer_cells_claimed'])
    report = dict(schema='independent-exact-saved186-cut-positive-components-audit-v1',
                  source_sha256=sha(__file__), certificate=dict(path=args.certificate,sha256=sha(args.certificate)),
                  resource=dict(path=args.resource,sha256=sha(args.resource)),
                  parameter_domain=cert['same_parameter_domain'], same_full_R127_field=True,
                  stronger_separately_saved_positive_sum_used=True, complete_T_shared_mass_paid_once=True,
                  all186_windows_and_parent94_mass_constraint_retained=True,
                  original_seed=dict(path=ids['previous_full_bootstrap']['path'],sha256=ids['previous_full_bootstrap']['sha256']),
                  cycles=reviews, final_review=final,
                  complete_original_two_cell_parameter_selfmap=final['complete_strict_selfmap'],
                  uniqueness_or_full_closed_surface_claimed=False, gates=G, all_audit_gates=all(G.values()),
                  elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    out.write_text(json.dumps(report,separators=(',',':'))+'\n')
    if read(out)!=report:
        raise ArithmeticError('Exact saved review differs')
    print(json.dumps(dict(all_audit_gates=report['all_audit_gates'],gates=len(G),
                          selfmap=final['complete_strict_selfmap'],worst_mode=final['worst_mode'],
                          max_axis_ratio=float(q(final['maximum_axis_ratio'])),
                          T_map=float(q(final['conservative_T_map'])),certificate_sha256=sha(args.certificate),
                          output_sha256=sha(out),elapsed_seconds=report['elapsed_seconds'])),flush=True)


if __name__=='__main__':
    main()
