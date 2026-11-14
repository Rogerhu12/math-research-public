#!/usr/bin/env python3
"""Read-only local residual decomposition of an immutable saved atlas field.

Uses the actual reported worst Gauss node and worst n-Codazzi cell only.
No BVP, body integration or Jacobian is assembled.  Angular and quadrature
comparisons are finite diagnostics of the same actual field, not bounds.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import json
from pathlib import Path
import resource
import time
import numpy as np
from fd2d_gc_archive_arrays import identity, save_npz
from fd2d_gc_ruling_atlas_native_field import RulingAtlasRawBumpNativeField
from fd2d_gc_bump_coast_native_field import window


def maximum(q):
    return float(np.max(np.abs(q), initial=0.))


def pack(q, suffix=''):
    return np.stack([q[k+suffix] for k in ('n', 'm', 'l')], axis=-1)


def rhs(q, values, angular):
    n, m, l = values.T
    nx, mx, lx = angular.T
    inv = 1/(q['a']*q['U_xi'])
    c, adv = q['a_s']/q['a'], q['U_x']/q['U_xi']
    return np.stack((inv*mx+c*(l-n)+adv*nx,
                     inv*lx-2*c*m+adv*mx), axis=-1)


def projection(value, kept):
    z = np.fft.rfft(value, axis=0)
    z[kept+1:] = 0
    return np.fft.irfft(z, n=len(value), axis=0)


def spectral_summary(value, retained):
    W = len(value)
    z = np.fft.rfft(value, axis=0)/W
    amplitude = 2*abs(z)
    amplitude[0] *= .5
    if W % 2 == 0:
        amplitude[-1] *= .5
    answer = []
    for j, label in enumerate(('n', 'm')):
        order = np.argsort(amplitude[:, j])[::-1]
        bands = {}
        for lo, hi in ((0, retained), (retained+1, 62), (63, 126), (127, 254), (255, W//2)):
            if hi < lo:
                continue
            terms = amplitude[lo:min(hi+1, len(amplitude)), j]
            bands[f'{lo}:{hi}'] = dict(coefficient_l2=float(np.linalg.norm(terms)),
                                       maximum_coefficient=maximum(terms))
        tail_max = {str(k): maximum(value[:, j]-projection(value[:, j], k))
                    for k in (retained, 62, 126)}
        reflection = (-np.arange(W)) % W
        parity_sign = 1. if j == 0 else -1.
        answer.append(dict(component=label, sampled_maximum=maximum(value[:, j]),
            retained_maximum=maximum(projection(value[:, j], retained)),
            omitted_maximum=tail_max[str(retained)], hypothetical_residual_tail_after_projecting_to=tail_max,
            coefficient_bands=bands,
            top_modes=[dict(frequency=int(k), amplitude=float(amplitude[k, j])) for k in order[:16]],
            reflection_defect=maximum(value[reflection, j]-parity_sign*value[:, j]),
            half_period_defect=maximum(value[:W//2, j]-value[W//2:, j])))
    return answer


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--field', type=Path, required=True)
    ap.add_argument('--report', type=Path, required=True)
    ap.add_argument('--out-prefix', type=Path, required=True)
    ap.add_argument('--angles', type=int, default=1024)
    args = ap.parse_args()
    stem = args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):
        raise FileExistsError('Use a new immutable diagnostic stem')
    if args.angles < 512 or args.angles % 256:
        raise ValueError('Use at least 512 labels, a multiple of the original 256 grid')
    started = time.monotonic()
    source_report = json.loads(args.report.read_text())
    fid, rid = identity(args.field), identity(args.report)
    if source_report['latest_checkpoint']['sha256'] != fid['sha256']:
        raise ValueError('The selected closed report does not bind this checkpoint')
    settings = source_report['settings']
    r = RulingAtlasRawBumpNativeField(args.field, settings['candidate'],
        reference_inlet=settings['reference_inlet'], reference_cache=settings['reference_cache'])
    sources = [identity(__file__)]+[identity(Path(__file__).parent/name) for name in (
        'fd2d_gc_ruling_atlas_native_field.py', 'fd2d_gc_ruling_reference_second_jets.py',
        'fd2d_gc_frozen_ruling_atlas.py', 'fd2d_gc_raw_bump_ruling_atlas.py')]
    xi = 2*np.pi*np.arange(args.angles)/args.angles
    arrays = dict(xi=xi)
    point_rows = []

    def evaluate(s, side='right'):
        q = r.evaluate_native(float(s), xi, side=side)
        if np.max(abs(q['J']-1)) != 0:
            raise ValueError('This diagnostic requires actual physical-s coordinates')
        c = r._correction_jets(np.full(len(xi), s), xi, side)
        v, dx, da = pack(q), pack(q, '_x'), pack(q, '_xi')
        total_rhs, corr_rhs = rhs(q, v, da), rhs(q, c['values'], c['xi'])
        return dict(q=q, values=v, dx=dx, correction=c['values'],
            lifting=v-c['values'], rhs=total_rhs, rhs_correction=corr_rhs,
            rhs_lifting=total_rhs-corr_rhs,
            point_codazzi=dx[:, :2]-total_rhs)

    node = int(source_report['final_locations']['full_gauss']['node'])
    node_s = float(r.nodes[node]); p = evaluate(node_s)
    q = p['q']; reference = r.angular_atlas.ruling_jet(node_s, xi, include_native=True)['native']
    R = pack(reference); c = p['correction']
    w, ws = window(np.array([node_s]), r.coast_reference.entry_s,
                   r.coast_reference.length, r.reference_rim_fraction)
    if w[0] != 1 or ws[0] != 0:
        raise ValueError('The reported node is not inside the full-reference plateau')
    K = -q['a_ss']/q['a']
    G = q['n']*q['l']-q['m']*q['m']-K
    rank = R[:, 0]*R[:, 2]-R[:, 1]*R[:, 1]
    cross = R[:, 0]*c[:, 2]+R[:, 2]*c[:, 0]-2*R[:, 1]*c[:, 1]
    quadratic = c[:, 0]*c[:, 2]-c[:, 1]*c[:, 1]
    worst = int(np.argmax(abs(G)))
    coarse_step = args.angles//256
    worst_coarse = coarse_step*int(np.argmax(abs(G[::coarse_step])))

    def node_point(index):
        return dict(angular_index=index, xi=float(xi[index]), material_u=float(q['u'][index]),
            actual_n_m_l=p['values'][index].tolist(), frozen_reference_n_m_l=R[index].tolist(),
            correction_n_m_l=c[index].tolist(), target_K=float(K[index]),
            G=float(G[index]), reference_rank1_defect=float(rank[index]),
            linear_correction_contribution=float(cross[index]),
            quadratic_correction_contribution=float(quadratic[index]),
            target_contribution=float(-K[index]))

    node_result = dict(node=node, s=node_s, reference_weight=float(w[0]),
        sampled_peak=node_point(worst), original_256_grid_peak=node_point(worst_coarse),
        actual_minus_reference_minus_correction=maximum(p['values']-R-c),
        decomposition_roundoff=maximum(G-(rank+cross+quadratic-K)),
        sampled_minimum_n=float(np.min(q['n'])), sampled_minimum_l=float(np.min(q['l'])),
        actual_G_in_low_modes_maximum=maximum(projection(G, 2*r.K)),
        actual_G_in_high_modes_maximum=maximum(G-projection(G, 2*r.K)))
    arrays.update(node_actual=p['values'], node_reference=R, node_correction=c,
                  node_G=G, node_target_K=K)

    cell = int(source_report['final_locations']['full_angular_codazzi']['n']['cell'])
    left, right = map(float, r.nodes[cell:cell+2]); h = right-left
    endpoint_left, endpoint_right = evaluate(left, 'right'), evaluate(right, 'left')
    endpoint = (endpoint_right['values'][:, :2]-endpoint_left['values'][:, :2])/h
    endpoint_c = (endpoint_right['correction'][:, :2]-endpoint_left['correction'][:, :2])/h
    endpoint_l = endpoint-endpoint_c
    boundary = r.coast_reference.entry_s+r.coast_reference.length*(1-r.reference_rim_fraction)
    split = sorted(set([left, right]+([float(boundary)] if left < boundary < right else [])))

    def average(order, cuts, name):
        roots, weights = np.polynomial.legendre.leggauss(order)
        total = np.zeros((args.angles, 2)); corr = np.zeros_like(total)
        local = []
        for a, b in zip(cuts[:-1], cuts[1:]):
            for root, weight in zip(roots, weights):
                s = (a+b)/2+(b-a)*root/2
                e = evaluate(float(s))
                normalized_weight = (b-a)*weight/(2*h)
                total += normalized_weight*e['rhs']
                corr += normalized_weight*e['rhs_correction']
                local.append(dict(s=float(s), normalized_weight=float(normalized_weight),
                    point_codazzi_maximum=np.max(abs(e['point_codazzi']), axis=0).tolist()))
        residual = endpoint-total
        rc = endpoint_c-corr
        rl = endpoint_l-(total-corr)
        arrays[name+'_average_codazzi'] = residual
        arrays[name+'_correction_codazzi'] = rc
        arrays[name+'_lifting_codazzi'] = rl
        info = dict(name=name, order=order, cuts=cuts, samples=local,
            full=spectral_summary(residual, 2*r.K),
            correction=spectral_summary(rc, 2*r.K), lifting=spectral_summary(rl, 2*r.K),
            decomposition_roundoff=maximum(residual-rc-rl))
        return residual, info

    g2, row2 = average(2, [left, right], 'whole_Gauss2')
    print(json.dumps(dict(stage='whole_Gauss2', maxima=np.max(abs(g2), axis=0).tolist())), flush=True)
    g3, row3 = average(3, split, 'split_Gauss3')
    g8, row8 = average(8, split, 'split_Gauss8')
    original = g2[::coarse_step]
    original_summary = spectral_summary(original, 2*r.K)
    cell_result = dict(cell=cell, endpoints=[left, right], width=h, window_piece_boundary=boundary,
        original_256_grid=original_summary,
        angular_refinement_maximum_change=[row2['full'][j]['sampled_maximum']-original_summary[j]['sampled_maximum'] for j in range(2)],
        original_report_maxima=[source_report['final_locations']['full_angular_codazzi'][key]['maximum'] for key in ('n', 'm')],
        original_report_omitted_maxima=[source_report['final_locations']['omitted_angular_codazzi'][key]['maximum'] for key in ('n', 'm')],
        whole2_vs_split8_maximum=np.max(abs(g2-g8), axis=0).tolist(),
        split3_vs_split8_maximum=np.max(abs(g3-g8), axis=0).tolist(),
        quadrature=[row2, row3, row8],
        endpoint_full=spectral_summary(endpoint, 2*r.K),
        endpoint_correction=spectral_summary(endpoint_c, 2*r.K),
        endpoint_lifting=spectral_summary(endpoint_l, 2*r.K))
    arrays.update(cell_endpoints=np.array([left, right]), endpoint_full=endpoint,
        endpoint_correction=endpoint_c, endpoint_lifting=endpoint_l)
    packet = save_npz(Path(str(stem)+'-samples.npz'), **arrays)
    definition_path = Path(str(stem)+'-definition.json')
    definition_path.write_text(json.dumps(r.definition(), indent=2, allow_nan=False)+'\n')
    report = dict(schema='fd2d-actual-atlas-local-GC-decomposition-v1', actual_execution=True,
        field=fid, source_report=rid, sources=sources, definition=identity(definition_path),
        samples=packet, angular_points=args.angles, original_angular_points=256,
        maximum_retained_frequency=2*r.K, actual_node_count=len(r.nodes),
        gauss_node=node_result, codazzi_cell=cell_result,
        angular_diagnostics='Finite equally spaced xi labels with actual material U(s,xi); hypothetical projected tails do not define a new solution',
        quadrature_diagnostics='Same saved P1 field and exact full lifting endpoint difference; finite fixed-xi PDE averages, no rigorous remainder claim',
        actual_field_bytes_unchanged=identity(args.field)['sha256']==fid['sha256'],
        source_report_unchanged=identity(args.report)['sha256']==rid['sha256'],
        sources_unchanged=all(identity(row['path'])['sha256']==row['sha256'] for row in sources),
        seconds=time.monotonic()-started, maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        BVP_or_Jacobian_matrix_assembled=False, nonlinear_solve_performed=False,
        body_integration_run=False, continuous_certificate=False)
    p=Path(str(stem)+'-report.json');p.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(report=str(p),node_G=node_result['sampled_peak']['G'],
        cell_full=[row2['full'][j]['sampled_maximum'] for j in range(2)],
        split8_full=[row8['full'][j]['sampled_maximum'] for j in range(2)],
        seconds=report['seconds'],maximum_rss_kib=report['maximum_rss_kib'])),flush=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
