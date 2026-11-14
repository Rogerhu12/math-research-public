#!/usr/bin/env python3
"""Coarse double-normal candidates on a saved physical prefix and its mirror.

The complete Fourier field, its actual physical PPoly derivative, the full
height mean and material angle are retained.  This searches finite clouds,
not the continuous annulus, and supplies neither a curvature enclosure nor
a reach certificate.  The nominal warped-metric path estimate is only a
candidate classification; the saved approximate map need not have that
metric exactly.  Boundary circles do not represent a completed cap.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import hashlib
import heapq
import importlib.util
import inspect
import json
from pathlib import Path
import textwrap
import time
import types
import numpy as np
from scipy.spatial import cKDTree

HERE = Path(__file__).resolve().parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('checkpoint', 'source-topic', 'port', 'out'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--radial', type=int, default=321)
    parser.add_argument('--angular', type=int, default=128)
    parser.add_argument('--height-angular', type=int, default=512)
    parser.add_argument('--query-radial', type=int, default=81)
    parser.add_argument('--query-angular', type=int, default=32)
    parser.add_argument('--batch', type=int, default=8)
    parser.add_argument('--keep', type=int, default=16)
    parser.add_argument('--chord-radius-factor', type=float, default=2.3)
    args = parser.parse_args()
    start = time.monotonic()
    if args.angular % args.query_angular or not 1 <= args.batch <= 16:
        raise ValueError('Query angles must divide the cloud angles; use batch <=16')
    source_hashes = {str(Path(__file__)): sha(__file__),
        str(args.checkpoint): sha(args.checkpoint), str(args.port): sha(args.port),
        str(HERE/'geometric-checkpoint-core-pullback.py'): sha(HERE/'geometric-checkpoint-core-pullback.py')}
    pb = load('strong_bottleneck_pullback', HERE/'geometric-checkpoint-core-pullback.py')
    saved, _ = pb.load_saved(args.checkpoint, args.source_topic, args.port,
        angular=max(args.angular, args.height_angular))
    if not saved.rec.get('solver_success') or saved.rec.get('audit_pending', True):
        raise ValueError('An audited converged saved finite prefix is required')
    if saved.mode != 2 or sha(args.port) != saved.rec['physical_port_sha256']:
        raise ValueError('The central symmetry and exact saved physical port are required')
    f = saved.flow
    pp = saved.sol.sol
    prefix = f._alternative_neck
    segments = []
    for seg in prefix.segments:
        label = 'initial-hermite' if seg['kind'] == 'hermite' else (
            'boost' if seg['kind'] == 'boost' else
            ('loop-' if seg['s0'] >= prefix.loop_begin-1e-13 else 'descending-')+seg['kind'])
        segments.append(dict(index=len(segments), label=label,
            lo=seg['s0'], hi=seg['s1']))
    for seg in f.bridge.segments:
        segments.append(dict(index=len(segments), label='terminal-'+seg['kind'],
            lo=prefix.end+seg['s0'], hi=prefix.end+seg['s1']))

    def segment_at(s):
        return next((r for r in segments if r['lo']-1e-12 <= abs(s) <= r['hi']+1e-12), segments[-1])

    query_s = np.unique(np.r_[np.linspace(0, f.end, args.query_radial), f.breaks, 0., f.end])
    s = np.unique(np.r_[np.linspace(0, f.end, args.radial), query_s])
    original = textwrap.dedent(inspect.getsource(f.height_integral.__func__))
    if original.count('128') != 3:
        raise ValueError('The original independent height batch sites changed')
    transformed = original.replace('128', str(args.batch))
    scope = {'np': np}
    exec(compile(transformed, '<original-height-integral-bounded-batch>', 'exec'), scope)
    height = types.MethodType(scope['height_integral'], f)(saved.sol, s, args.height_angular, 6)
    B, B1, B2 = f.basis(args.angular)
    _, H1, H2 = f.basis(args.height_angular)
    upper = np.empty((len(s), args.angular, 3))
    upper_normal = np.empty_like(upper)
    theta_upper = np.empty((len(s), args.angular))
    area_min = float('inf')
    for first in range(0, len(s), args.batch):
        sl = slice(first, first+args.batch)
        ss = s[sl]
        Y, Yp = pp(ss), pp(ss, 1)
        frame = f.frame(ss, saved.q*Y, B1, B2)
        geo = frame['geo']
        hp = np.mean(f.frame(ss, saved.q*Y, H1, H2)['V'][:, :, 2], axis=1)
        X = geo['pos']+saved.q*f.values(Y, B)
        X[:, :, 2] += height[sl, None]
        Fsc = geo['s1']+saved.q*f.values(Yp, B)
        Fsc[:, :, 2] += hp[:, None]
        Fs = Fsc-geo['v'][:, :, None]*frame['d']
        Ft = frame['d']/geo['rho'][:, :, None]
        cross = np.cross(Ft, Fs)
        area = np.linalg.norm(cross, axis=2)
        if np.min(area) <= 0:
            raise FloatingPointError('A sampled tangent area vanished')
        upper[sl] = X
        upper_normal[sl] = cross/area[:, :, None]
        theta_upper[sl] = geo['theta']
        area_min = min(area_min, float(np.min(area)))
    print(json.dumps(dict(event='physical_cloud_restored', upper_radial=len(s),
        angular=args.angular, seconds=time.monotonic()-start)), flush=True)
    reflection = np.array([1., 1., -1.])
    signed_s = np.r_[-s[:0:-1], s]
    X = np.concatenate((upper[:0:-1]*reflection, upper)).reshape(-1, 3)
    normals = np.concatenate((upper_normal[:0:-1]*reflection, upper_normal)).reshape(-1, 3)
    theta = np.concatenate((theta_upper[:0:-1], theta_upper)).ravel()
    S = np.repeat(signed_s, args.angular)
    psi = np.tile(2*np.pi*np.arange(args.angular)/args.angular, len(signed_s))
    segment_ids = np.repeat([segment_at(t)['index'] for t in signed_s], args.angular)
    radial_profile = f.profile(abs(signed_s))[0]
    A = np.repeat(radial_profile, args.angular)
    tree = cKDTree(X)
    D = 2*float(np.linalg.norm(X, axis=1).max())
    K = float(saved.rec['summary']['kappa_sample'])
    tau = .03*D
    radius = args.chord_radius_factor*tau
    local_window = float(np.pi/K)
    waypoint_s = np.unique(np.r_[0., f.breaks, -np.asarray(f.breaks), f.end, -f.end])
    waypoint_a = f.profile(abs(waypoint_s))[0]
    signed_query_s = np.r_[-query_s[:0:-1], query_s]
    query_rows = np.searchsorted(signed_s, signed_query_s)
    if not np.array_equal(signed_s[query_rows], signed_query_s):
        raise ValueError('Lost a requested query row')
    query = np.array([row*args.angular+j for row in query_rows
        for j in range(0, args.angular, args.angular//args.query_angular)], int)
    groups = {name: dict(count=0, below_2tau=0, quotient_below_tau=0,
        min_distance=None, min_quotient=None, min_double_normal=None, heap=[])
        for name in ('all_near', 'nominal_path_at_least_pi_over_K',
            'nonadjacent_meridian_pieces', 'loop_nonadjacent_meridian_pieces',
            'opposite_halves_nonlocal', 'terminal_involved')}
    serial = 0

    def point(k):
        seg = segments[int(segment_ids[k])]
        return dict(index=int(k), signed_s=float(S[k]), psi=float(psi[k]),
            material_theta=float(theta[k]), side='upper' if S[k] >= 0 else 'lower',
            segment_index=seg['index'], segment=seg['label'], point=X[k].tolist(),
            outward_normal=normals[k].tolist())

    def arrays(i, ids):
        delta = X[ids]-X[i]
        length = np.linalg.norm(delta, axis=1)
        dp, dq = delta@normals[i], np.sum(delta*normals[ids], axis=1)
        denom = np.maximum(abs(dp), abs(dq))
        Q = np.divide(length*length, 2*denom, out=np.full_like(length, np.inf), where=denom > 1e-18)
        sinp = np.sqrt(np.maximum(0., 1.-np.divide(dp*dp, length*length,
            out=np.zeros_like(length), where=length > 1e-12)))
        sinq = np.sqrt(np.maximum(0., 1.-np.divide(dq*dq, length*length,
            out=np.zeros_like(length), where=length > 1e-12)))
        angle = abs((theta[ids]-theta[i]+np.pi) % (2*np.pi)-np.pi)
        path = abs(S[ids]-S[i])+np.minimum(A[i], A[ids])*angle
        for u, au in zip(waypoint_s, waypoint_a):
            path = np.minimum(path, abs(S[i]-u)+abs(S[ids]-u)+au*angle)
        return dict(distance=length, quotient=Q, sin_p=sinp, sin_q=sinq,
            double_normal=np.maximum(sinp, sinq), nominal_path=path,
            normal_dot_p=dp, normal_dot_q=dq)

    def record(i, j, values, k):
        length = float(values['distance'][k])
        return dict(first=point(i), second=point(j), distance=length, half_distance=length/2,
            minimum_ordered_normal_chord_quotient=float(values['quotient'][k]),
            tangent_projection_over_chord_first=float(values['sin_p'][k]),
            tangent_projection_over_chord_second=float(values['sin_q'][k]),
            double_normal_residual_max=float(values['double_normal'][k]),
            tangent_projection_length_first=length*float(values['sin_p'][k]),
            tangent_projection_length_second=length*float(values['sin_q'][k]),
            signed_normal_component_first=float(values['normal_dot_p'][k]),
            signed_normal_component_second=float(values['normal_dot_q'][k]),
            nominal_warped_path_upper_estimate=float(values['nominal_path'][k]),
            chord_below_twice_target=length < 2*tau)

    def add(group, i, ids, values, mask):
        nonlocal serial
        ix = np.flatnonzero(mask)
        if not len(ix):
            return
        group['count'] += len(ix)
        group['below_2tau'] += int(np.count_nonzero(values['distance'][ix] < 2*tau))
        group['quotient_below_tau'] += int(np.count_nonzero(values['quotient'][ix] < tau))
        for key, metric in (('min_distance', 'distance'), ('min_quotient', 'quotient'),
                            ('min_double_normal', 'double_normal')):
            k = int(ix[np.argmin(values[metric][ix])])
            old = group[key]
            old_metric = {'distance':'distance', 'quotient':'minimum_ordered_normal_chord_quotient',
                'double_normal':'double_normal_residual_max'}[metric]
            if old is None or values[metric][k] < old[old_metric]:
                group[key] = record(i, int(ids[k]), values, k)
        choices = ix[np.argsort(values['double_normal'][ix])[:args.keep]]
        for k in choices:
            score = float(values['double_normal'][k])
            serial += 1
            if len(group['heap']) < args.keep or score < -group['heap'][0][0]:
                item = (-score, serial, record(i, int(ids[k]), values, int(k)))
                if len(group['heap']) < args.keep:
                    heapq.heappush(group['heap'], item)
                else:
                    heapq.heapreplace(group['heap'], item)

    for done, i in enumerate(query):
        ids = np.asarray(tree.query_ball_point(X[i], radius), int)
        vals = arrays(i, ids)
        good = vals['distance'] > 1e-8
        nonlocal_path = vals['nominal_path'] >= local_window
        nonadjacent = (np.sign(S[ids]) == np.sign(S[i])) & (abs(segment_ids[ids]-segment_ids[i]) >= 2)
        loop = np.array([segments[k]['label'].startswith('loop-') for k in segment_ids[ids]])
        loop |= segments[segment_ids[i]]['label'].startswith('loop-')
        terminal = (abs(S[i]) >= prefix.end-1e-12) | (abs(S[ids]) >= prefix.end-1e-12)
        masks = (good, good & nonlocal_path, good & nonadjacent,
            good & nonadjacent & loop, good & nonlocal_path & (S[ids]*S[i] < 0), good & terminal)
        for group, mask in zip(groups.values(), masks):
            add(group, int(i), ids, vals, mask)
        if done and done % 1024 == 0:
            print(json.dumps(dict(event='bottleneck_pairs', done=done, total=len(query),
                seconds=time.monotonic()-start)), flush=True)

    # Explicit core versus the complete sampled terminal cuff strip, even
    # though its distance is too large to enter the near-chord query ball.
    endpoint_groups = {}
    core = np.flatnonzero(S == 0.)
    for side, mask in [('upper', S >= prefix.end-1e-12), ('lower', S <= -prefix.end+1e-12)]:
        ids = np.flatnonzero(mask)
        group = dict(count=0, below_2tau=0, quotient_below_tau=0,
            min_distance=None, min_quotient=None, min_double_normal=None, heap=[])
        for i in core:
            vals = arrays(int(i), ids)
            add(group, int(i), ids, vals, np.ones(len(ids), bool))
        endpoint_groups['core_to_'+side+'_terminal_strip'] = group
    for group in [*groups.values(), *endpoint_groups.values()]:
        group['best_double_normal_candidates'] = [row[2] for row in sorted(group.pop('heap'), reverse=True)]
    result = dict(scope=__doc__, source_sha256=source_hashes, checkpoint=str(args.checkpoint),
        actual_primary_amplitude=saved.rec['actual_primary_amplitude'], gauge_amplitude=saved.q,
        modes=saved.M, physical_metric_l1_sample=saved.rec['summary']['metric_l1'],
        saved_curvature_sample=K, diameter_this_centrally_symmetric_cloud=D,
        target_tau_sample=.03*D, twice_target_tau_sample=2*tau,
        curvature_sample_times_target=K*tau, nominal_local_path_window=local_window,
        upper_radial_samples=len(s), angular_samples=args.angular, target_points=len(X),
        query_points=len(query), query_radial_per_half=len(query_s), query_angular=args.query_angular,
        chord_search_radius=radius, keep_candidates_per_group=args.keep,
        mean_height_angular=args.height_angular, mean_height_quadrature_order=6,
        radial_batch=args.batch, minimum_tangent_area_sample=area_min,
        height_integral_batch_transform=dict(original_sha256=hashlib.sha256(original.encode()).hexdigest(),
            transformed_sha256=hashlib.sha256(transformed.encode()).hexdigest(), replacements=3,
            original_integration_order_preserved=True),
        normal_formula='Ftheta cross Fs, normalized; actual physical PPoly and full mean derivatives.',
        nominal_path_formula='min_u |sp-u|+|sq-u|+a(u)*wrapped_material_angle; u includes both endpoints and every signed physical profile break.',
        segments=segments, near_pair_groups=groups, core_cuff_groups=endpoint_groups,
        candidate_thresholds_are_not_continuum_exclusions=True,
        limitations=['Only the recorded finite linear-DN design is screened, not a new actual joined solution.',
            'The metric defect of this source exceeds 1e-6; there is no exact isometry certificate.',
            'Neither the curvature sample nor the point-cloud diameter is a continuous envelope.',
            'The nominal path window is not a paid bound for the saved approximate metric.',
            'No exact infinite tail, caps, markers, or boundary normal cones are included.',
            'Small residuals identify numerical candidates; absent candidates do not exclude unsampled double normals.'],
        seconds=time.monotonic()-start)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(event='bottleneck_screen_complete', out=str(args.out),
        seconds=result['seconds'], D=D, tau=tau,
        minima={k:dict(pairs=v['count'], quotient=None if v['min_quotient'] is None else v['min_quotient']['minimum_ordered_normal_chord_quotient'],
            double_normal=None if v['min_double_normal'] is None else v['min_double_normal']['double_normal_residual_max'],
            quotient_below_target=v['quotient_below_tau']) for k, v in groups.items()})), flush=True)


if __name__ == '__main__':
    main()
