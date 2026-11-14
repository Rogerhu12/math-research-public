#!/usr/bin/env python3
"""Visual PLY discretizations of an identified certified common-cut map.

The continuous graph is not changed. Prefix chart inversion uses material
theta, the entire upper-tail height perturbation is reflected, the lower
band is the z mirror, and only the upper fixed cap has three bumps.
The height sampler supplies numerical representatives, not rigorous vertex
error bounds. C2/metric/reach proofs refer to the identified continuous map.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'
import argparse
import bisect
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time
import numpy as np

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent


def check(ok, message):
    if not ok:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def module(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE/filename)
    obj = importlib.util.module_from_spec(spec)
    sys.modules[name] = obj
    spec.loader.exec_module(obj)
    return obj


def resolve(name, parent=TOPIC/'notes'):
    path = Path(name)
    if path.exists():
        return path
    path = Path(parent)/path.name
    check(path.exists(), 'Missing input '+str(name))
    return path


def prepare(geometry, whole_certificate):
    geometry, whole_certificate = Path(geometry), Path(whole_certificate)
    meta = json.loads(geometry.read_text())
    certificate = json.loads(whole_certificate.read_text())
    check(certificate['geometry_sha256'] == sha(geometry), 'Certificate belongs to another continuous graph')
    check(certificate['tail_manifest_sha256'] == meta['tail_manifest_sha256'], 'Certificate tail mismatch')
    check(certificate['README_geometric_and_metric_thresholds_1_2_3_4_6_paid_given_reviewed_inputs'] is True,
          'Underlying geometric and metric thresholds have not been recorded')
    matching = [name for name in ['db6f-root-common-cut.py', 'db6f-root-common-cut-v2.py']
                if sha(HERE/name) == meta['common_cut_implementation_sha256']]
    check(len(matching) == 1, 'No unique frozen common-cut implementation')
    base = module('mesh_prefix_intervals', 'db6f-audit-continuous-hermite.py')
    common = module('mesh_common_cut', matching[0])
    common.install(base)
    prefix = base.ExactHermite(geometry)
    stream = module('mesh_stream_geometry', 'db6f-audit-tail-stream.py')
    tail_path = resolve(meta['tail_manifest'], geometry.parent)
    tail = stream.StreamingExactIntegratedTail(tail_path)
    check(sha(tail_path) == meta['tail_manifest_sha256'], 'Tail data binding changed')
    check(prefix.inlet_exact['planar_z_values_zero'] and prefix.inlet_exact['horizontal_first_jet_zero']
          and prefix.inlet_exact['vertical_second_jet_zero'], 'Exact mirror inlet conditions fail')
    supplier = module('mesh_material_spline', 'db6f-audit-metric-supplier.py')
    sources = {name: sha(HERE/name) for name in [Path(__file__).name, matching[0],
        'db6f-audit-continuous-hermite.py', 'db6f-audit-tail-stream.py',
        'db6f-audit-tail-metric-curvature.py', 'db6f_tail_integrated.py', 'db6f-audit-metric-supplier.py']}
    return base, prefix, tail, supplier, sources


def distinct(values, lo, hi, tolerance):
    values = sorted(float(x) for x in values if float(lo) <= float(x) <= float(hi))
    result = [float(lo)]
    for value in values:
        if value-result[-1] > tolerance and float(hi)-value > tolerance:
            result.append(value)
    result.append(float(hi))
    return result


def flat_sampling_knots(cfg):
    delta, vu, vd, eps = [Q(float(cfg[k])) for k in ['delta', 'vu', 'vd', 'ramp']]
    eta = Q(float(cfg.get('ramp_eta', .1)))
    tu, td = delta/(vu*(1-eps)), delta/(vd*(1-eps))
    first, second = (tu, td) if cfg['direction'] == 'outward' else (td, tu)
    local = [0, eps*eta, eps*(1-eta), eps, 1-eps, 1-eps*(1-eta), 1-eps*eta, 1]
    result = []
    for cycle in range(int(cfg['cycles'])):
        start = cycle*(first+second)
        result.extend(start+first*x for x in local)
        result.extend(start+first+second*x for x in local)
    return result


def plan(args):
    check(args.angular >= 48 and args.angular % 12 == 0, 'Angular count must be a multiple of 12, at least 48')
    check(min(args.prefix_intervals, args.tail_intervals, args.collar_intervals, args.cap_intervals) > 0,
          'Positive sampling interval counts required')
    base, prefix, tail, _, sources = prepare(args.geometry, args.whole_certificate)
    end, cut, inner, cuff = Q(float(prefix.x[-1])), tail.rq[-1], tail.rq[0], tail.cuff
    check(Q(7, 50) < cuff < Q(3, 20) and cut == Q(float(tail.meta['parameters']['rCut'])),
          'Unexpected fixed cap or cut domain')
    u = [float(end*Q(j, args.prefix_intervals)) for j in range(args.prefix_intervals+1)]
    u += [float(end*Q(float(x))) for x in prefix.meta['chart']['knots']]
    u += list(map(float, flat_sampling_knots(prefix.meta['frozen_profile'])))
    u += [float(prefix.x[int(prefix.meta['correction_start_index'])])]
    tolerance = max(float(end), 1.)*1e-11
    u = distinct(u, Q(0), end, tolerance)
    radii = [float(inner+(cut-inner)*Q(j, args.tail_intervals)) for j in range(args.tail_intervals+1)]
    node = 0
    for block in tail.meta['files']:
        node += int(block['rows'])-1
        radii.append(float(tail.rq[node]))
    check(node == tail.N, 'Tail block/node bookkeeping mismatch')
    radii = distinct(radii, inner, cut, 1e-11)
    collar = [float(cuff+(inner-cuff)*Q(j, args.collar_intervals))
              for j in range(args.collar_intervals+1)]
    cap = [float(cuff*Q(j, args.cap_intervals)) for j in range(args.cap_intervals+1)]
    cap += [float(x) for x in [Q(1, 20), Q(13, 200), Q(2, 25), Q(19, 200), Q(11, 100)]]
    cap = distinct(cap, Q(0), cuff, 1e-11)
    upper = [dict(kind='prefix', coordinate=x) for x in u]
    upper[-1]['cut'] = True
    upper += [dict(kind='tail', coordinate=x) for x in radii[-2::-1]]
    upper += [dict(kind='collar', coordinate=x) for x in collar[-2::-1]]
    upper[-1]['cuff'] = True
    upper += [dict(kind='cap', coordinate=x) for x in cap[-2:0:-1]]
    rings = len(upper)*2-1
    vertices, faces = rings*args.angular+2, 2*rings*args.angular
    predicted = 24*vertices+13*faces+4096
    check(predicted < 5_000_000, 'Sampling plan would exceed the uncompressed per-file limit')
    height_radii = sorted(set(radii+collar+[float(cuff), float(cut)]))
    args.out_prefix.parent.mkdir(parents=True, exist_ok=True)
    radius_path = Path(str(args.out_prefix)+'-radii.json')
    radius_path.write_text(json.dumps(dict(radii=height_radii,
        finite_tail_manifest_sha256=prefix.meta['tail_manifest_sha256']), indent=2)+'\n')
    result = dict(status='visual-mesh-sampling-plan-not-a-new-continuous-map', scope=__doc__,
        geometry=dict(file=str(args.geometry.resolve()), sha256=sha(args.geometry)),
        whole_certificate=dict(file=str(args.whole_certificate.resolve()), sha256=sha(args.whole_certificate)),
        finite_tail_manifest_sha256=prefix.meta['tail_manifest_sha256'], source_sha256=sources,
        angular_nodes=args.angular, material_angles='theta_j=2*pi*j/N',
        times_exact=['0', '1/4', '1/2'], phase='alpha=2*pi*t/3',
        upper_rings=upper, height_radii_file=str(radius_path.resolve()), height_radii_sha256=sha(radius_path),
        cuff_radius=float(cuff), tail_inner_radius=float(inner), cut_radius=float(cut),
        prefix_end=float(end), sampling_merge_tolerance=tolerance,
        rings=rings, vertices=vertices, faces=faces, conservative_uncompressed_bytes=predicted,
        fixed_cap_definition=dict(upper_bump_count=3, centers_radius_exact='2/25', bump_radius_exact='3/100',
                                  bump_height_exact='1/2000', lower_cap='flat'),
        fixed_g_convergence_gate_5_paid=False, mesh_generated=False)
    target = Path(str(args.out_prefix)+'-plan.json')
    target.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(plan=str(target), radii=str(radius_path), rings=rings,
                         vertices=vertices, faces=faces, predicted_bytes=predicted)))


def interval_midpoint(interval):
    return np.asarray((interval.lo.astype(np.longdouble)+interval.hi.astype(np.longdouble))/2, dtype=np.float64)


def polynomial_value(base, power, parameter):
    # Prefix and tail loaders have separate module instances of the same
    # interval implementation. Copy endpoints to the polynomial's class;
    # no new arithmetic or interval narrowing is performed here.
    parameter = type(power)(parameter.lo, parameter.hi)
    result = power[-1]
    for degree in range(len(power.lo)-2, -1, -1):
        result = result*parameter+power[degree]
    return result


def exact_chart_values(prefix, supplier, values):
    knots, coefficients = supplier.exact_clamped_spline(prefix.meta['chart'])
    end, warp = Q(float(prefix.x[-1])), 8*Q(float(prefix.meta['warp_reference_q']))
    result = []
    for u in values:
        x = Q(float(u))/end
        j = min(bisect.bisect_right(knots, x)-1, len(coefficients)-1)
        y = Q(0)
        for coefficient in coefficients[j][::-1]:
            y = y*(x-knots[j])+coefficient
        if x > Q(3, 4):
            t = 4*x-3
            y *= 1-10*t**3+15*t**4-6*t**5
        value = warp*y
        check(abs(value) < 1, 'Sampled material chart is not strictly monotone')
        result.append(float(value))
    return np.array(result)


def invert_material_angle(theta, e):
    theta = np.broadcast_to(theta[None, :], (len(e), len(theta))).copy()
    e = e[:, None]
    low, high = theta-np.abs(e)/3, theta+np.abs(e)/3
    psi = theta.copy()
    for iteration in range(80):
        residual = psi-e*np.sin(3*psi)/3-theta
        active = np.abs(residual) > 8e-15
        if not np.any(active):
            break
        low = np.where(active & (residual < 0), psi, low)
        high = np.where(active & (residual >= 0), psi, high)
        proposed = psi-residual/(1-e*np.cos(3*psi))
        proposed = np.where((proposed > low) & (proposed < high), proposed, (low+high)/2)
        psi = np.where(active, proposed, psi)
    residual = psi-e*np.sin(3*psi)/3-theta
    check(float(np.max(np.abs(residual))) < 3e-14, 'Material-angle inverse did not converge')
    return psi, float(np.max(np.abs(residual))), iteration+1


def prefix_points(base, prefix, supplier, values, theta):
    e = exact_chart_values(prefix, supplier, values)
    psi, residual, iterations = invert_material_angle(theta, e)
    result = []
    maximum_coefficient_radius_sum = 0.
    m = prefix.M
    frequencies = 3*np.arange(1, m+1)
    for row, u in enumerate(values):
        index = min(max(int(np.searchsorted(prefix.x, u, side='right'))-1, 0), len(prefix.x)-2)
        parameter = (Q(float(u))-Q(float(prefix.x[index])))/(Q(float(prefix.x[index+1]))-Q(float(prefix.x[index])))
        check(0 <= parameter <= 1, 'Prefix query leaves its exact span')
        enclosure = polynomial_value(base, prefix.power[index], base.qbounds(parameter))
        c = interval_midpoint(enclosure)
        maximum_coefficient_radius_sum = max(maximum_coefficient_radius_sum,
                                             float(np.sum(enclosure.hi-enclosure.lo)/2))
        angles = psi[row, :, None]*frequencies[None, :]
        cosines, sines = np.cos(angles), np.sin(angles)
        radial = c[0]+cosines@c[1:m+1]
        tangential = sines@c[m+1:2*m+1]
        height = c[-1]+cosines@c[2*m+1:3*m+1]
        cp, sp = np.cos(psi[row]), np.sin(psi[row])
        result.append(np.column_stack([radial*cp-tangential*sp, radial*sp+tangential*cp, height]))
    return result, dict(maximum_material_inverse_residual_approx=residual, inverse_iterations=iterations,
                       maximum_sampled_absolute_chart_e=float(np.max(np.abs(e))),
                       maximum_prefix_coefficient_interval_radius_sum_approx=maximum_coefficient_radius_sum)


def tail_coefficient_value(base, tail, radius):
    r = Q(float(radius))
    if r < tail.rq[0]:
        parameter = (r-tail.cuff)/tail.collar_length
        check(0 <= parameter <= 1, 'Collar query leaves its exact interval')
        power = tail.collar[0]
    else:
        index = min(bisect.bisect_right(tail.rq, r)-1, tail.N-1)
        check(index >= 0, 'Tail query precedes the finite part')
        parameter = (r-tail.rq[index])/tail.lq[index]
        check(0 <= parameter <= 1, 'Tail query leaves its exact span')
        power = tail.span_polys(index)[0]
    return polynomial_value(base, power, base.qbounds(parameter))


def evaluate_tail(base, tail, radius, theta, cut_height, relative_height):
    enclosure = tail_coefficient_value(base, tail, radius)
    c = interval_midpoint(enclosure)
    planar = np.exp(1j*np.outer(theta, tail.reader.planar_modes))@c[:tail.P]
    height = np.cos(np.outer(theta, tail.reader.height_modes))@c[tail.P:]
    xy = radius*np.exp(1j*theta)+planar
    points = np.column_stack([xy.real, xy.imag, cut_height+relative_height-height])
    return points, float(np.sum(enclosure.hi-enclosure.lo)/2)


def cap_points(radius, theta, height, bumps):
    x, y = radius*np.cos(theta), radius*np.sin(theta)
    z = np.full(len(theta), height)
    if bumps:
        a, b, h = float(Q(2, 25)), float(Q(3, 100)), float(Q(1, 2000))
        centers = [(a, 0.), (-a/2, a*math.sqrt(3)/2), (-a/2, -a*math.sqrt(3)/2)]
        for cx, cy in centers:
            q = ((x-cx)**2+(y-cy)**2)/(b*b)
            z += h*np.maximum(1-q, 0.)**3
    return np.column_stack([x, y, z])


def triangle_faces(rings, angular):
    result = []
    for j in range(angular):
        k = (j+1) % angular
        result.append((0, 1+k, 1+j))
    for ring in range(rings-1):
        lo, hi = 1+ring*angular, 1+(ring+1)*angular
        for j in range(angular):
            k = (j+1) % angular
            result.extend([(lo+j, lo+k, hi+j), (lo+k, hi+k, hi+j)])
    pole, last = 1+rings*angular, 1+(rings-1)*angular
    for j in range(angular):
        result.append((last+j, last+(j+1) % angular, pole))
    return np.asarray(result, dtype='<i4')


def write_ply(path_prefix, vertices, faces, t):
    header = ('ply\nformat binary_little_endian 1.0\n'
        'comment Numerical visual discretization of the identified common-cut finite map\n'
        'comment Model coordinate units; continuous certificates refer to the underlying C2 map\n'
        'comment t='+str(t)+' alpha=2*pi*t/3; material theta is inverted through Theta\n'
        'element vertex '+str(len(vertices))+'\nproperty double x\nproperty double y\nproperty double z\n'
        'element face '+str(len(faces))+'\nproperty list uchar int vertex_indices\nend_header\n').encode('ascii')
    record = np.empty(len(faces), dtype=np.dtype([('count', 'u1'), ('indices', '<i4', (3,))], align=False))
    record['count'] = 3
    record['indices'] = faces
    raw = header+np.asarray(vertices, dtype='<f8').tobytes()+record.tobytes()
    check(len(raw) < 5_000_000, 'Uncompressed mesh exceeds the per-file limit')
    if len(raw) > 1_000_000:
        path, payload = Path(str(path_prefix)+'.ply.gz'), gzip.compress(raw, mtime=0)
    else:
        path, payload = Path(str(path_prefix)+'.ply'), raw
    check(len(payload) < 5_000_000, 'Stored mesh exceeds the per-file limit')
    path.write_bytes(payload)
    return dict(file=str(path), sha256=sha(path), uncompressed_bytes=len(raw), stored_bytes=len(payload))


def build(args):
    started = time.monotonic()
    planned = json.loads(args.plan.read_text())
    geometry = resolve(planned['geometry']['file'])
    certificate = resolve(planned['whole_certificate']['file'])
    check(sha(geometry) == planned['geometry']['sha256'] and sha(certificate) == planned['whole_certificate']['sha256'],
          'A planned continuous input changed')
    base, prefix, tail, supplier, sources = prepare(geometry, certificate)
    check(sources == planned['source_sha256'], 'A planned implementation changed')
    heights = json.loads(args.height_samples.read_text())
    check(heights.get('finished') is True and heights['heightIntervalCertificate'] is False,
          'Unexpected numerical height sample protocol')
    check(heights['inputs']['manifest']['sha256'] == prefix.meta['tail_manifest_sha256'], 'Height samples belong to another tail')
    radius_path = resolve(planned['height_radii_file'])
    check(sha(radius_path) == planned['height_radii_sha256'] == heights['inputs']['radii']['sha256'],
          'Height query radii changed')
    check(heights['scriptSHA256'] == sha(HERE/'db6f-tail-sample-background-height.mjs'), 'Height helper changed')
    height_lookup = {}
    for row in heights['rows']:
        radius, value = float(row['r']), float(row['heightFromRToCut'])
        check(math.isfinite(radius) and math.isfinite(value) and value >= 0, 'Invalid relative height sample')
        check(radius.hex() not in height_lookup, 'Duplicate height query')
        height_lookup[radius.hex()] = value
    queries = json.loads(radius_path.read_text())['radii']
    check(set(height_lookup) == {float(r).hex() for r in queries}, 'Height query coverage mismatch')
    cut, cuff = planned['cut_radius'], planned['cuff_radius']
    check(height_lookup[float(cut).hex()] == 0., 'Cut relative height must be exactly zero by definition')
    ordered = sorted(queries)
    check(all(height_lookup[float(a).hex()]+1e-13 >= height_lookup[float(b).hex()]
              for a, b in zip(ordered[:-1], ordered[1:])), 'Numerical background height is not monotone')
    cut_height = float(interval_midpoint(prefix.background_cut_height))
    cap_height = cut_height+height_lookup[float(cuff).hex()]
    angular = planned['angular_nodes']
    theta = 2*math.pi*np.arange(angular)/angular
    upper_layout = planned['upper_rings']
    prefix_u = [row['coordinate'] for row in upper_layout if row['kind'] == 'prefix']
    prefix_values, diagnostics = prefix_points(base, prefix, supplier, prefix_u, theta)
    maximum_seam_gap, maximum_tail_radius_sum = 0., 0.
    upper, fixed, prefix_index = [], [], 0
    for row in upper_layout:
        kind, coordinate = row['kind'], row['coordinate']
        if kind == 'prefix':
            points = prefix_values[prefix_index]
            prefix_index += 1
            if row.get('cut'):
                other, radius_sum = evaluate_tail(base, tail, cut, theta, cut_height, 0.)
                maximum_seam_gap = max(maximum_seam_gap, float(np.max(np.linalg.norm(points-other, axis=1))))
                maximum_tail_radius_sum = max(maximum_tail_radius_sum, radius_sum)
                points = other
            if coordinate == 0.:
                maximum_seam_gap = max(maximum_seam_gap, float(np.max(np.abs(points[:, 2]))))
                points[:, 2] = 0.
            is_fixed = False
        elif kind in ('tail', 'collar'):
            points, radius_sum = evaluate_tail(base, tail, coordinate, theta, cut_height,
                                               height_lookup[float(coordinate).hex()])
            maximum_tail_radius_sum = max(maximum_tail_radius_sum, radius_sum)
            is_fixed = bool(row.get('cuff'))
            if is_fixed:
                other = cap_points(cuff, theta, cap_height, False)
                maximum_seam_gap = max(maximum_seam_gap, float(np.max(np.linalg.norm(points-other, axis=1))))
                points = other
        else:
            check(kind == 'cap', 'Unknown meridional block')
            points = cap_points(coordinate, theta, cap_height, True)
            is_fixed = True
        upper.append(points)
        fixed.append(is_fixed)
    check(maximum_seam_gap < 1e-8, 'Numerical representatives disagree at a known exact common seam')
    lower = []
    for row, points in zip(upper_layout[1:][::-1], upper[1:][::-1]):
        reflected = points.copy()
        if row['kind'] == 'cap':
            reflected[:, 2] = -cap_height
        else:
            reflected[:, 2] *= -1
        lower.append(reflected)
    rings = np.stack(lower+upper)
    fixed_rings = np.asarray(fixed[1:][::-1]+fixed, dtype=bool)
    check(len(rings) == planned['rings'], 'Ring count differs from the plan')
    faces = triangle_faces(len(rings), angular)
    check(len(faces) == planned['faces'], 'Face count differs from the plan')
    fixed_mask = np.r_[True, np.repeat(fixed_rings, angular), True]
    first_fixed = None
    mesh_files = []
    args.out_prefix.parent.mkdir(parents=True, exist_ok=True)
    for time_value in planned['times_exact']:
        t = Q(time_value)
        shift = angular*t/3
        check(shift.denominator == 1, 'The material phase is not an exact grid permutation')
        phase_rings = np.roll(rings, int(shift), axis=1).copy()
        alpha = 2*math.pi*float(t)/3
        co, si = math.cos(alpha), math.sin(alpha)
        x, y = phase_rings[..., 0].copy(), phase_rings[..., 1].copy()
        phase_rings[..., 0], phase_rings[..., 1] = co*x-si*y, si*x+co*y
        phase_rings[fixed_rings] = rings[fixed_rings]
        vertices = np.concatenate([[[0., 0., -cap_height]], phase_rings.reshape(-1, 3), [[0., 0., cap_height]]])
        check(len(vertices) == planned['vertices'] and np.isfinite(vertices).all(), 'Invalid complete vertex array')
        if first_fixed is None:
            first_fixed = vertices[fixed_mask].copy()
        else:
            check(np.array_equal(first_fixed, vertices[fixed_mask]), 'Fixed cap vertices changed with phase')
        label = 't'+('0' if t == 0 else str(t.numerator)+'of'+str(t.denominator))
        info = write_ply(Path(str(args.out_prefix)+'-'+label), vertices, faces, t)
        info.update(time_exact=str(t), phase_expression='2*pi*('+str(t)+')/3', material_grid_shift=int(shift),
                    vertices=len(vertices), faces=len(faces), fixed_vertices=int(fixed_mask.sum()))
        mesh_files.append(info)
    diagnostics.update(maximum_independent_seam_gap_approx=maximum_seam_gap,
        maximum_tail_coefficient_interval_radius_sum_approx=maximum_tail_radius_sum,
        background_cut_height_approx=cut_height, fixed_cap_height_approx=cap_height,
        background_height_max_inverse_residual_approx=heights['maximumInverseRadiusResidualApprox'],
        background_height_max_split_difference_approx=heights['maximumSplitHeightDifferenceApprox'])
    result = dict(status='generated-numerical-visual-PLYs-pending-independent-discrete-validation', scope=__doc__,
        script_sha256=sha(__file__), plan=dict(file=str(args.plan), sha256=sha(args.plan)),
        geometry=planned['geometry'], whole_certificate=planned['whole_certificate'],
        finite_tail_manifest_sha256=prefix.meta['tail_manifest_sha256'], source_sha256=sources,
        height_samples=dict(file=str(args.height_samples), sha256=sha(args.height_samples)),
        numerical_height_scope=heights['scope'], height_deep_omission=heights['deepOmission'],
        mesh_files=mesh_files, fixed_caps_bitwise_identical_across_times=True,
        fixed_vertex_indices_file=None, diagnostics=diagnostics,
        material_phase_implementation='Theta is inverted on the uniform material grid. For these times N*t/3 is an exact integer; '
                                      'a cyclic grid permutation evaluates theta-alpha, followed by spatial R_alpha. Fixed cap rows are copied.',
        upper_cap_bumps=3, lower_cap_bumps=0,
        continuous_map_modified=False, continuous_vertex_error_certified=False,
        fixed_g_convergence_gate_5_paid=False, README_complete=False, seconds=time.monotonic()-started)
    mask_path = Path(str(args.out_prefix)+'-fixed-vertices.npz')
    np.savez_compressed(mask_path, fixed=fixed_mask)
    result['fixed_vertex_indices_file'] = dict(file=str(mask_path), sha256=sha(mask_path))
    output = Path(str(args.out_prefix)+'-manifest.json')
    output.write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(manifest=str(output), files=len(mesh_files), vertices=planned['vertices'],
                         faces=len(faces), maximum_seam_gap=maximum_seam_gap, seconds=result['seconds'])))


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest='task', required=True)
    p = sub.add_parser('plan')
    p.add_argument('--geometry', type=Path, required=True)
    p.add_argument('--whole-certificate', type=Path, required=True)
    p.add_argument('--out-prefix', type=Path, required=True)
    p.add_argument('--angular', type=int, default=144)
    p.add_argument('--prefix-intervals', type=int, default=128)
    p.add_argument('--tail-intervals', type=int, default=64)
    p.add_argument('--collar-intervals', type=int, default=4)
    p.add_argument('--cap-intervals', type=int, default=12)
    p.set_defaults(function=plan)
    p = sub.add_parser('build')
    p.add_argument('--plan', type=Path, required=True)
    p.add_argument('--height-samples', type=Path, required=True)
    p.add_argument('--out-prefix', type=Path, required=True)
    p.set_defaults(function=build)
    arguments = ap.parse_args()
    arguments.function(arguments)
