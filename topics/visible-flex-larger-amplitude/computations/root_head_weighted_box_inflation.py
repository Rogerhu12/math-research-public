#!/usr/bin/env python3
"""Expand a certified head box along its already paid positive metric weight.

Exact Fraction arithmetic only. The same whole-domain derivative J, mean
branch, physical rho, actual background and true far graph are retained.
The previous R53 parameter cross-polytope is retained in the enlarged box;
new axes are combined by the exact convex hull of the old/new axial points.
No new kernel, inverse, radial integration, or nonlinear solve is performed.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time
from closure_balance_parameter_axes_v2 import read, pair, upper, lower, compact, record, floorlog2


def exact(value):
    lo, hi = lower(value), upper(value)
    if lo != hi:
        raise ValueError('A chosen radius or weight must be an exact dyadic point')
    return lo


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ('joint', 'density', 'lifts', 'parameter-ball', 'balanced', 'out'):
        ap.add_argument('--'+name, type=Path, required=True)
    args = ap.parse_args()
    if args.out.exists() or args.out.suffix != '.gz':
        raise ValueError('Use a fresh compressed full-row ledger')
    started = time.monotonic()
    docs, hashes = {}, {}
    for name in ('joint', 'density', 'lifts', 'parameter_ball', 'balanced'):
        path = getattr(args, name)
        docs[name], hashes[str(path)] = read(path)
    joint, density, lifts, domain, balanced = [docs[name] for name in
        ('joint', 'density', 'lifts', 'parameter_ball', 'balanced')]
    if (not joint['whole_head_closed'] or not all(joint['gates'].values())
            or not domain['all_gates'] or not all(domain['gates'].values())
            or not balanced['all_gates'] or not all(balanced['checks'].values())):
        raise ValueError('All actual original and parameter-domain certificates must be successful')
    for doc, name in [(joint, 'density'), (lifts, 'density'), (domain, 'joint'),
                      (domain, 'lifts'), (balanced, 'lifts'), (balanced, 'parameter_ball')]:
        path = str(getattr(args, name))
        if doc['input_hashes'].get(path) != hashes[path]:
            raise ValueError('The exact source/background or certified domain changed: '+name)
    cells = list(range(12, 225))
    if (lifts['cells'] != cells or lifts['modes'] != list(range(2, 93, 2))
            or len(density['rows']) != 213 or joint['dimension'] != 641
            or len(joint['rows']) != 641 or len(domain['rows']) != 641
            or len(balanced['cells']) != 213 or len(balanced['rows']) != 46):
        raise ValueError('The complete original dimensions are required')
    N, inf, zi = 213, 639, 640
    r, weights, images, lips, old_slack = [], [], [], [], []
    for i, (row, parameter_row) in enumerate(zip(joint['rows'], domain['rows'])):
        if row['index'] != i or parameter_row['index'] != i:
            raise ValueError('A certified coordinate was reordered')
        r.append(exact(row['radius']))
        weights.append(exact(row['metric_weight']))
        images.append(upper(row['image']))
        lips.append(upper(row['weighted_derivative_row']))
        old_slack.append(lower(parameter_row['retained_map_slack']))
    old_slack[zi] = lower(balanced['certified_remaining_far_slack'])
    if not all(value > 0 for value in r+weights+old_slack):
        raise ValueError('A required original positive coordinate or slack is absent')
    lam = F(3970, 4096)
    if not max(lips) < lam < 1:
        raise ValueError('The original complete weighted derivative is not below this dyadic lambda')
    rho = exact(joint['physical_domain'])
    Z = exact(joint['independent_far_z'])
    if Z != exact(lifts['parameter_far_scale']):
        raise ValueError('The actual far normalization differs')
    auxiliary = upper(joint['auxiliary_far_z'])
    A = [[compact(value) for value in row] for row in lifts['A_upper']]
    E = [compact(value) for value in lifts['far_E_upper']]
    if len(A) != N or any(len(row) != 46 for row in A) or len(E) != 46:
        raise ValueError('All true linear lift columns are required')
    old_units = [exact(row['canonical_Q_axis']) for row in balanced['rows']]
    old_lift = [max(A[n][j]*old_units[j] for j in range(46)) for n in range(N)]
    v_over_w = [upper(row['V_over_w_upper']) for row in density['rows']]
    t = [r[n]+r[N+n]+r[2*N+n]+r[inf] for n in range(N)]
    tw = [weights[n]+weights[N+n]+weights[2*N+n]+weights[inf] for n in range(N)]
    limits = []
    for n in range(N):
        limits.append(((rho-t[n]-old_lift[n])/(4*tw[n]), 'total_state', cells[n]))
        limits.append(((1/(64*v_over_w[n])-1-t[n]-old_lift[n])/(4*tw[n]), 'mean', cells[n]))
    limits.append(((1-auxiliary/Z-r[zi])/(4*weights[zi]), 'far', 225))
    if not all(value > 0 for value, _, _ in limits):
        raise ValueError('No expansion room remains after retaining all old parameters')
    bound, kind, where = min(limits, key=lambda item: item[0])
    s_exp = floorlog2(bound)
    s = pair(1, s_exp)
    eta_exp = floorlog2(s*(1-lam)/(4*(1+lam)))
    eta = pair(1, eta_exp)
    expanded = [r[i]+s*weights[i] for i in range(641)]
    axes = []
    units = []
    fresh_units = []
    hfactor, hlog = balanced['Q_to_physical_H_factor'], balanced['Q_to_physical_H_log2_factor']
    for j in range(46):
        bounds = [(eta*weights[n]/A[n][j], 'cell', cells[n]) for n in range(N) if A[n][j] > 0]
        if E[j] > 0:
            bounds.append((eta*Z*weights[zi]/E[j], 'far', 225))
        limit, origin, location = min(bounds, key=lambda item: item[0])
        fresh_exp = floorlog2(limit)
        fresh = pair(1, fresh_exp)
        chosen = max(old_units[j], fresh)
        chosen_exp = floorlog2(chosen)
        if chosen != pair(1, chosen_exp):
            raise ValueError('The axial convex hull must retain exact dyadic axis units')
        fresh_units.append(fresh); units.append(chosen)
        axes.append(dict(j=j+1, physical_mode=2*(j+1), old_Q_axis_log2=floorlog2(old_units[j]),
            new_sufficient_axis_log2=fresh_exp, canonical_Q_axis_log2=chosen_exp,
            gain_over_R53_bits=chosen_exp-floorlog2(old_units[j]), canonical_Q_axis=record(chosen),
            selected_from='expanded-weight-domain' if fresh > old_units[j] else 'retained-R53-domain',
            fresh_axis_limiter=dict(kind=origin,cell=location),
            actual_physical_height_axis=record(lower(hfactor)*chosen,upper(hfactor)*chosen),
            guaranteed_physical_height_axis=record(lower(hfactor)*chosen),
            actual_physical_height_axis_log2=record(lower(hlog)+chosen_exp,upper(hlog)+chosen_exp)))
    new_lift = [max(A[n][j]*units[j] for j in range(46)) for n in range(N)]
    total = [t[n]+s*tw[n]+new_lift[n] for n in range(N)]
    old_branch_image = [r[i]-old_slack[i]+s*lam*weights[i] for i in range(641)]
    fresh_branch_image = [images[i]+(s*lam+eta*(1+lam))*weights[i] for i in range(641)]
    image_bound = [max(old_branch_image[i], fresh_branch_image[i]) for i in range(641)]
    old_source_increment = [r[i]-old_slack[i]-images[i] for i in range(641)]
    gates = dict(original_all641_uniform_derivatives_below_lambda=max(lips) < lam < 1,
        all641_retained_parameter_source_budgets_nonnegative=all(v >= 0 for v in old_source_increment),
        all641_expanded_radii_positive=all(value > 0 for value in expanded),
        all46_previous_axes_contained=all(units[j] >= old_units[j] for j in range(46)),
        all46_fresh_lifts_below_weight_budget=all(A[n][j]*fresh_units[j] <= eta*weights[n]
            for n in range(N) for j in range(46)),
        all46_fresh_far_lifts_below_weight_budget=all(E[j]*fresh_units[j] <= eta*Z*weights[zi] for j in range(46)),
        all213_combined_total_domains=all(value < rho for value in total),
        all213_combined_mean_domains=all(v_over_w[n]*(1+total[n]) < F(1,64) for n in range(N)),
        enlarged_independent_true_far_domain=auxiliary+Z*expanded[zi] < Z,
        all641_combined_map_rows_strict=all(image_bound[i] < expanded[i] for i in range(641)),
        same_original_metric_remains_contracting=max(lips) < 1)
    out = dict(scope=__doc__, status='Completed exact inherited-box and parameter-hull certification',
        all_gates=all(gates.values()), gates=gates, original_dimension=641,
        same_background_and_rho_and_J_and_W=True, expansion_s=record(s), expansion_s_log2=s_exp,
        fresh_lift_eta=record(eta), fresh_lift_eta_log2=eta_exp, lambda_upper=record(lam),
        actual_original_Lipschitz=joint['maximum_joint_Lipschitz'],
        limiting_expansion=dict(kind=kind,cell=where), physical_domain=joint['physical_domain'],
        maximum_combined_total_radius=record(max(total)),
        independent_far_z=joint['independent_far_z'], auxiliary_far_z=joint['auxiliary_far_z'],
        parameter_norm='sum_j |delta Q_(2j)(b)|/v_j <=1; convex hull of retained R53 and fresh axial cross-polytopes, not a product box.',
        Q_to_physical_H_factor=hfactor, Q_to_physical_H_log2_factor=hlog,
        physical_height_convention='Same true b; delta H=b^4 delta Q, no extra w.', axes=axes,
        cells=[dict(cell=cells[n], combined_lift=record(new_lift[n]),
            original_total=record(t[n]), weight_total=record(tw[n]),
            combined_total=record(total[n]), full_mean_domain=record(v_over_w[n]*(1+total[n]))) for n in range(N)],
        rows=[dict(index=i, block=joint['rows'][i]['block'], cell=joint['rows'][i]['cell'],
            expanded_radius=record(expanded[i]), inherited_metric_weight=record(weights[i]),
            retained_parameter_source_budget=record(old_source_increment[i]),
            old_parameter_branch_image=record(old_branch_image[i]),
            new_parameter_branch_image=record(fresh_branch_image[i]), combined_image=record(image_bound[i]),
            combined_map_slack=record(expanded[i]-image_bound[i])) for i in range(641)],
        input_hashes=hashes, source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        helper_sha256=hashlib.sha256(Path(__file__).with_name('closure_balance_parameter_axes_v2.py').read_bytes()).hexdigest(),
        exact_arithmetic='fractions.Fraction for every inequality; every serialized numerical endpoint is dyadic.',
        new_kernel_calculations=0, new_radial_integrations=0, new_matrix_inverses=0,
        scope_limit='Same q003 head12..224 and R18 true tail. Outer0..11, actual strong prefix and closed geometry remain separate.',
        seconds=time.monotonic()-started, peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    payload = gzip.compress((json.dumps(out,separators=(',',':'))+'\n').encode(),mtime=0)
    if len(payload) >= 5_000_000:
        raise ValueError('The compressed full ledger exceeds the repository cap')
    args.out.write_bytes(payload)
    print(json.dumps(dict(all_gates=all(gates.values()),gates=gates,expansion_s_log2=s_exp,
        fresh_lift_eta_log2=eta_exp,first_Q_axis_log2=axes[0]['canonical_Q_axis_log2'],
        last_Q_axis_log2=axes[-1]['canonical_Q_axis_log2'],maximum_gain_bits=max(a['gain_over_R53_bits'] for a in axes),
        bytes=len(payload),sha256=hashlib.sha256(payload).hexdigest(),seconds=out['seconds'],RSS_KiB=out['peak_RSS_KiB'])),flush=True)
    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
