#!/usr/bin/env python3
"""Certify an actual strong full46 parameter family by the paid R58 J and W.

Only exact Fraction arithmetic is used. The actual strong normalization is
V_s=sigma_n V_q on the identical continuous q strip. Thus every true linear
lift column is divided by sigma_n; the physical far evaluation E is unchanged.
The parameter lift is included in the full working and mean domains. No new
Green kernel, ODE, quadrature, matrix inverse, or nonlinear solve is performed.
Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
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


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def exact(value):
    a, b = lower(value), upper(value)
    if a != b:
        raise ValueError('A chosen norm envelope, radius or weight must be an exact dyadic point')
    return a


def up_pair(q, bits=32):
    if q < 0:
        raise ValueError('Only positive upper coefficients are accepted')
    if q == 0:
        return [0, 0]
    e = floorlog2(q) - bits + 1
    scaled = q / pair(1, e)
    m = -(-scaled.numerator // scaled.denominator)
    v = pair(m, e)
    if not q <= v or not v < q * (1 + pair(1, 1-bits)):
        raise AssertionError('Exact positive outward rounding failed')
    return [m, e]


def write_new(path, data):
    if path.exists():
        raise FileExistsError('Every execution requires a fresh output path: '+str(path))
    raw = (json.dumps(data, separators=(',', ':'))+'\n').encode()
    payload = gzip.compress(raw, mtime=0) if path.suffix == '.gz' else raw
    if len(payload) >= 5_000_000:
        raise ValueError('Repository per-file cap exceeded')
    path.write_bytes(payload)
    return dict(path=str(path), bytes=len(payload), sha256=hashlib.sha256(payload).hexdigest())


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('joint', 'density', 'q-density', 'q-lifts', 'cut-axes', 'out-lifts', 'out', 'summary'):
        p.add_argument('--'+name, type=Path, required=True)
    args = p.parse_args()
    for path in (args.out_lifts, args.out, args.summary):
        if path.exists():
            raise FileExistsError('No previous mathematical output may be overwritten')
    started = time.monotonic()
    docs, hashes = {}, {}
    for name in ('joint', 'density', 'q_density', 'q_lifts', 'cut_axes'):
        path = getattr(args, name)
        docs[name], hashes[str(path)] = read(path)
    joint, strong, q, lifts, cut = [docs[k] for k in ('joint', 'density', 'q_density', 'q_lifts', 'cut_axes')]
    if not joint['whole_head_closed'] or not all(joint['gates'].values()):
        raise ValueError('The complete original641 actual strong certificate is required')
    if not all(strong['gates'].values()) or not all(q['gates'].values()):
        raise ValueError('Both certified normalization/strip ledgers are required')
    if joint['input_hashes'].get(str(args.density)) != hashes[str(args.density)]:
        raise ValueError('The actual successful strong problem changed')
    origin = strong['continuous_strip_origin']
    if (origin['path'] != str(args.q_density) or origin['sha256'] != hashes[str(args.q_density)]
            or not origin['do_not_renormalize_using_new_strong_density']):
        raise ValueError('The identical original continuous q strip must be retained')
    if (strong['input_hashes'].get(str(args.q_density)) != hashes[str(args.q_density)]
            or lifts['input_hashes'].get(str(args.q_density)) != hashes[str(args.q_density)]
            or cut['input_hashes'].get(str(args.q_lifts)) != hashes[str(args.q_lifts)]):
        raise ValueError('The real source/linear-column/true-cut provenance differs')
    verified = {}
    for key in ('input_hashes', 'panel_hashes', 'group_hashes'):
        for filename, sha in lifts[key].items():
            if filename not in verified:
                if digest(Path(filename)) != sha:
                    raise ValueError('A paid true linear lift dependency changed: '+filename)
                verified[filename] = sha
    source_file = 'notes/2026-11-12-closure-real-head-source-enclosure.json'
    if digest(Path(source_file)) != cut['input_hashes'][source_file]:
        raise ValueError('The paid true radius enclosure changed')
    N, inf, zi = 213, 639, 640
    cells, modes = list(range(12, 225)), list(range(2, 93, 2))
    if (joint['dimension'] != 641 or len(joint['rows']) != 641 or lifts['cells'] != cells
            or lifts['modes'] != modes or not lifts['all46_chart_directions']
            or [r['cell'] for r in q['rows']] != cells or [r['cell'] for r in strong['rows']] != cells):
        raise ValueError('Every original mode and every physical cell is required')
    same_fields = ('B', 'Q_coefficient', 'mu_lower', 'mu_upper', 'normalized_width_upper',
                   'TV_log_w_upper', 'w_lower', 'tau_inner', 'tau_outer', 'reference_tau',
                   'certified_reference_tau', 'minimum_strip_buffer')
    sigma = []
    for n in range(N):
        qs, ss = q['rows'][n], strong['rows'][n]
        if any(qs[k] != ss[k] for k in same_fields):
            raise ValueError('A source, norm geometry, or strip field changed at cell '+str(cells[n]))
        sq = exact(qs['canonical_total_envelope'])
        st = exact(ss['canonical_total_envelope'])
        if min(sq, st) <= 0 or ss['original_q_canonical_total_envelope'] != qs['canonical_total_envelope']:
            raise ValueError('The actual canonical envelope ratio is not identified')
        ratio = st/sq
        if not lower(ss['scale_from_original_q']) <= ratio <= upper(ss['scale_from_original_q']):
            raise ValueError('The exact normalization ratio escaped the recorded interval')
        sigma.append(ratio)
    qA = [[compact(v) for v in row] for row in lifts['A_upper']]
    E = [compact(v) for v in lifts['far_E_upper']]
    if len(qA) != N or any(len(row) != 46 for row in qA) or len(E) != 46:
        raise ValueError('The complete213x46 parameter columns are required')
    Apairs = [[up_pair(qA[n][j]/sigma[n]) for j in range(46)] for n in range(N)]
    A = [[compact(v) for v in row] for row in Apairs]
    if not all(A[n][j]*sigma[n] >= qA[n][j] for n in range(N) for j in range(46)):
        raise AssertionError('A rescaled true lift was rounded inward')
    r, W, image, lip = [], [], [], []
    for i, row in enumerate(joint['rows']):
        expected = ('low', cells[i]) if i < N else ('near', cells[i-N]) if i < 2*N else \
                   ('rest', cells[i-2*N]) if i < 3*N else ('infinite', None) if i == inf else ('far_z', None)
        if row['index'] != i or (row['block'], row['cell']) != expected:
            raise ValueError('A full641 coordinate was dropped or reordered')
        r.append(exact(row['radius'])); W.append(exact(row['metric_weight']))
        image.append(upper(row['image'])); lip.append(upper(row['weighted_derivative_row']))
    if not all(r[i] > image[i] >= 0 and W[i] > 0 for i in range(641)):
        raise ValueError('The original strict box was not paid')
    lam = F(3970, 4096)
    if not max(lip) < lam < 1:
        raise ValueError('The same full-domain derivative does not obey the chosen dyadic bound')
    rho, Z = exact(joint['physical_domain']), exact(joint['independent_far_z'])
    zaux = upper(joint['auxiliary_far_z'])
    if Z != exact(lifts['parameter_far_scale']) or rho != pair(1, -30):
        raise ValueError('The actual physical/far domains changed')
    An = [upper(row['V_over_w_upper']) for row in strong['rows']]
    total = [r[n]+r[N+n]+r[2*N+n]+r[inf] for n in range(N)]
    total_W = [W[n]+W[N+n]+W[2*N+n]+W[inf] for n in range(N)]
    limits = []
    for n in range(N):
        limits.append(((rho-total[n])/(4*total_W[n]), 'physical', cells[n]))
        limits.append(((1/(64*An[n])-1-total[n])/(4*total_W[n]), 'mean', cells[n]))
    limits.append(((1-zaux/Z-r[zi])/(4*W[zi]), 'far', 225))
    if not all(x[0] > 0 for x in limits):
        raise ValueError('The actual domain has no certified expansion room')
    bound, kind, where = min(limits, key=lambda v: v[0])
    s_exp = floorlog2(bound); s = pair(1, s_exp)
    eta_exp = floorlog2(s*(1-lam)/(4*(1+lam))); eta = pair(1, eta_exp)
    expanded = [r[i]+s*W[i] for i in range(641)]
    units, axes = [], []
    hf, hl = cut['Q_to_physical_H_factor'], cut['Q_to_physical_H_log2_factor']
    b = cut['true_cut_radius']
    if not lower(hf) <= lower(b)**4 <= upper(b)**4 <= upper(hf):
        raise ValueError('The true H=b^4 Q conversion does not enclose the radius interval')
    for j in range(46):
        constraints = [(eta*W[n]/A[n][j], 'cell', cells[n]) for n in range(N) if A[n][j] > 0]
        if E[j] > 0:
            constraints.append((eta*Z*W[zi]/E[j], 'far', 225))
        limit, axis_kind, axis_cell = min(constraints, key=lambda v: v[0])
        exp = floorlog2(limit); unit = pair(1, exp); units.append(unit)
        axes.append(dict(j=j+1, physical_mode=modes[j], canonical_Q_axis_log2=exp,
            canonical_Q_axis=record(unit), limiting_lift=dict(kind=axis_kind, cell=axis_cell),
            actual_physical_height_axis=record(lower(hf)*unit, upper(hf)*unit),
            actual_physical_height_axis_log2=record(lower(hl)+exp, upper(hl)+exp),
            guaranteed_physical_height_axis=record(pair(1, exp-18)),
            guaranteed_physical_height_axis_log2=exp-18))
    lift = [max(A[n][j]*units[j] for j in range(46)) for n in range(N)]
    lifted_total = [total[n]+s*total_W[n]+lift[n] for n in range(N)]
    out_image = [image[i]+(s*lam+eta*(1+lam))*W[i] for i in range(641)]
    # This controls the actual fixed point in the SAME weighted metric.
    K = compact(up_pair(eta*(1+lam)/(1-lam), 64))
    gates = dict(original_full641_success=all(joint['gates'].values()),
        same_real_source_and_exact_continuous_strip=True,
        all213x46_lifts_rounded_outward=all(A[n][j]*sigma[n] >= qA[n][j] for n in range(N) for j in range(46)),
        far_E_unchanged=True, all641_same_uniform_derivative=max(lip) < lam < 1,
        all641_expanded_radii_positive=all(v > 0 for v in expanded),
        all46_parameter_axes_positive=all(v > 0 for v in units),
        all213x46_actual_lifts_within_low_weight=all(A[n][j]*units[j] <= eta*W[n] for n in range(N) for j in range(46)),
        all46_actual_far_lifts_within_far_weight=all(E[j]*units[j] <= eta*Z*W[zi] for j in range(46)),
        all213_combined_physical_domains=all(v < rho for v in lifted_total),
        all213_complete_mean_domains=all(An[n]*(1+lifted_total[n]) < F(1,64) for n in range(N)),
        true_independent_R18_domain=zaux+Z*expanded[zi] < Z,
        all641_parameter_map_rows_strict=all(out_image[i] < expanded[i] for i in range(641)),
        full46_physical_height_dyadic_axes_valid=pair(1,-18) < lower(hf) < upper(hf) < pair(1,-17),
        same_original_metric_remains_contracting=max(lip) < 1)
    provenance = dict(input_hashes=hashes, paid_linear_dependency_hashes=verified,
        source_sha256=digest(Path(__file__)),
        helper_sha256=digest(Path(__file__).with_name('closure_balance_parameter_axes_v2.py')))
    rescaled = dict(status='Complete actual strong true linear parameter lifts on the identical original q continuous strip',
        cells=cells, modes=modes, all46_chart_directions=True,
        A_upper=Apairs, far_E_upper=lifts['far_E_upper'],
        parameter_far_scale=joint['independent_far_z'],
        compact_number='Exact32-bit-significand nonnegative dyadic upper endpoints; relative rounding overhead <2^-31.',
        norm='A_nj bounds the full real cosine shallow canonical Q mode in the strong physical mixed A1 norm. Both signed Fourier halves are included.',
        rescaling='A_strong[n,j] >= A_q[n,j]/sigma_n with V_strong=sigma_n V_q; far_E is identical, with no target physical renormalization.',
        sigma=[dict(cell=cells[n], exact_numerator=str(sigma[n].numerator), exact_denominator=str(sigma[n].denominator)) for n in range(N)],
        continuous_strip_origin=origin, true_cut_radius=b,
        Q_to_physical_H_factor=hf, physical_height_convention='delta H=b^4 delta Q; no extra w.',
        source_same_as_R26_and_R58=True, new_linear_solves=0, new_radial_integrations=0, **provenance)
    lifts_written = write_new(args.out_lifts, rescaled)
    result = dict(status='Actual strong complete-frequency full46 parameter family certified', all_gates=all(gates.values()),
        gates=gates, original_dimension=641, physical_cells=cells, parameter_modes=modes,
        same_R58_background_and_rho_and_J_and_W=True, original_auxiliary_centre='R39 actual q085 strong M20 on the R26 true new rational metric',
        parameter_norm='sum_j |delta Q_(2j)(b)|/v_j <=1; an axial l1 ball, not the product of the listed intervals.',
        physical_domain=joint['physical_domain'], independent_far_z=joint['independent_far_z'], auxiliary_far_z=joint['auxiliary_far_z'],
        lambda_upper=record(lam), actual_uniform_Lipschitz=joint['maximum_joint_Lipschitz'],
        expansion_s=record(s), expansion_s_log2=s_exp, parameter_lift_eta=record(eta), parameter_lift_eta_log2=eta_exp,
        original_radius_multiple_of_weight=record(r[0]/W[0]),
        all_original_radii_share_this_multiple=all(r[i]/W[i] == r[0]/W[0] for i in range(641)),
        limiting_expansion=dict(kind=kind,cell=where), maximum_combined_total_radius=record(max(lifted_total)),
        maximum_mean_domain=record(max(An[n]*(1+lifted_total[n]) for n in range(N))),
        expanded_far_normalized_radius=record(expanded[zi]),
        fixed_point_parameter_Lipschitz_in_W=record(K),
        parameter_Lipschitz_reason='B|delta a| <=eta(1+lambda)W ||delta a||_axes and uniform J contraction; the complete unknown correction satisfies ||delta x||_W <= eta(1+lambda)/(1-lambda) ||delta a||_axes.',
        true_cut_radius=b, Q_to_physical_H_factor=hf, Q_to_physical_H_log2_factor=hl,
        axes=axes,
        cells=[dict(cell=cells[n], parameter_lift=record(lift[n]), low_weight_budget=record(eta*W[n]),
            original_total=record(total[n]), expanded_unknown_total=record(total[n]+s*total_W[n]),
            combined_total=record(lifted_total[n]), complete_mean_domain=record(An[n]*(1+lifted_total[n])),
            field_parameter_Lipschitz=record(eta*W[n]+K*total_W[n])) for n in range(N)],
        rows=[dict(index=i, block=joint['rows'][i]['block'], cell=joint['rows'][i]['cell'],
            original_radius=record(r[i]), expanded_radius=record(expanded[i]), metric_weight=record(W[i]),
            original_image_upper=record(image[i]), parameter_image_upper=record(out_image[i]),
            map_slack=record(expanded[i]-out_image[i]), uniform_weighted_derivative_upper=record(lip[i])) for i in range(641)],
        rescaled_lifts=lifts_written, exact_arithmetic='fractions.Fraction for every bound and comparison; serialized endpoints are exact dyadics.',
        scope='The R58 actual strong head on physical cells12..224 with the real R18 infinite tail. Outer0..11/prefix matching and full closed-surface amplitude/reach are not asserted.',
        new_kernels=0, new_radial_integrations=0, new_matrix_inverses=0, **provenance,
        elapsed_seconds=time.monotonic()-started, peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    out_written = write_new(args.out, result)
    summary = {k:v for k,v in result.items() if k not in ('rows','cells','paid_linear_dependency_hashes')}
    summary['full_ledger'] = out_written
    write_new(args.summary, summary)
    print(json.dumps(dict(all_gates=result['all_gates'],gates=gates,expansion_s_log2=s_exp,
        parameter_lift_eta_log2=eta_exp,first_Q_axis_log2=axes[0]['canonical_Q_axis_log2'],
        last_Q_axis_log2=axes[-1]['canonical_Q_axis_log2'],output=out_written,lifts=lifts_written,
        elapsed_seconds=result['elapsed_seconds'],peak_RSS_KiB=result['peak_RSS_KiB'])),flush=True)
    if not result['all_gates']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
