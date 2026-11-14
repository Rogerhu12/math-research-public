#!/usr/bin/env python3
"""Compare six existing original RK48 points on the small stage28 cusp window.

Only one original shooting stage is replayed, with the original integration
grid and complete saved state.  A/B/C must reproduce their old point bytes,
mean and geometry exactly.  Three other already existing RK48 points then
define a local f48 GW readout beside the original f8 and f16 readouts.

This measures finite interpolation/metric/curvature effects.  It does not
solve a BVP, adopt a global alternative field, or impose a machine-precision
six-jet convergence requirement beyond the topic README's actual criteria.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time

for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
TOPIC = Path('topics/visible-flex-larger-amplitude')
PACKET = TOPIC / 'notes/2026-11-14-GW-cusp-compatibility-packet'
ANCHOR = TOPIC / 'notes/2026-11-14-stage28-original-rk48-input'
PACKET_SHA = 'ef3bd5d5fb05143c109de8875c21424068db5814d9158187950b2f5d132ea75e'
ANCHOR_SHA = '9be383b67f67ade092536cc1c7185130b13e61d5180408e242535c1b1c90825b'


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(65536), b''):
            digest.update(block)
    return digest.hexdigest()


def write(path, value):
    with Path(path).open('x') as stream:
        json.dump(value, stream, indent=2, allow_nan=False)
        stream.write('\n')


def public_bytes(relative):
    relative = Path(relative)
    if relative.is_absolute() or '..' in relative.parts:
        raise ValueError('Safe public repository paths required')
    existing = REPO / relative
    if existing.is_file():
        return existing.read_bytes()
    return subprocess.check_output(['git', '-C', str(REPO), 'show', 'HEAD:' + relative.as_posix()])


def restore_packet(relative, target, manifest_sha):
    """Copy only the hash-listed small files, including after sparse checkout."""
    target.mkdir(parents=True, exist_ok=False)
    raw = public_bytes(relative / 'manifest.json')
    if hashlib.sha256(raw).hexdigest() != manifest_sha:
        raise ValueError('The original byte extraction manifest changed')
    (target / 'manifest.json').write_bytes(raw)
    manifest = json.loads(raw)
    tables = ['files'] if 'files' in manifest else ['row_files', 'node_files']
    for table in tables:
        for name, record in manifest[table].items():
            name_path = Path(name)
            if name_path.is_absolute() or '..' in name_path.parts:
                raise ValueError('Unsafe packet file')
            data = public_bytes(relative / name_path)
            if len(data) != record['bytes'] or hashlib.sha256(data).hexdigest() != record['sha256']:
                raise ValueError('Changed original packet bytes: ' + name)
            destination = target / name_path
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(data)
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-topic', type=Path,
                        help='Optional existing pinned 78-file public source tree')
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--node-heap', type=int, default=1536)
    parser.add_argument('--angles', type=int, default=1024)
    args = parser.parse_args()
    if os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public':
        raise RuntimeError('Numerical execution belongs to this public repository Actions')
    if args.angles < 1024 or args.angles % 2 or args.node_heap < 512:
        raise ValueError('Keep at least the original 1024 angular samples and a usable Node heap')
    begin = time.monotonic()
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=False)
    work = Path(tempfile.mkdtemp(prefix='stage28-original-rk48-', dir=os.environ.get('RUNNER_TEMP')))
    packet, anchor = work / 'original-point-packet', work / 'original-anchor'
    packet_manifest = restore_packet(PACKET, packet, PACKET_SHA)
    anchor_manifest = restore_packet(ANCHOR, anchor, ANCHOR_SHA)
    source_hashes = {str(Path(__file__).resolve()): sha(__file__),
                     str(HERE / 'exact_20261114_stage28_original_rk48_readout.mjs'):
                         sha(HERE / 'exact_20261114_stage28_original_rk48_readout.mjs')}
    for name, digest in packet_manifest['consumed_source_sha256'].items():
        path = HERE / name
        if sha(path) != digest:
            raise ValueError('Original GW interpolation source changed: ' + name)
        source_hashes[str(path)] = digest
    if sha(HERE / 'tail_frozen_geometry.mjs') != 'db6664fcd7be618d2b684c39c01c53d97833d11e14af206b12c71e4b058713e3':
        raise ValueError('Original frozen physical source adapter changed')
    from exact_20261114_public_resume import prepare_public_source
    source = args.source_topic.resolve() if args.source_topic else prepare_public_source(REPO, work, out)
    origin_path = source / 'source-origin.json'
    origin = json.loads(origin_path.read_text())
    if origin.get('actual_public_repository') != 'Rogerhu12/math-research-public' or origin.get('verified_file_count') != 78:
        raise ValueError('Use the exact public-only 78-file numerical source restoration')
    # Check the consumed public source bytes again when a previous job prepared
    # the tree.  No private repository or missing-manifest approximation exists.
    source_repository_root = source.parents[1]
    for record in origin['restored_files']:
        path = source_repository_root / record['path']
        if path.stat().st_size != record['bytes'] or sha(path) != record['sha256']:
            raise ValueError('Changed restored public source: ' + record['path'])
    assets = {}
    for key, record in anchor_manifest['public_assets'].items():
        data = public_bytes(record['path'])
        if hashlib.sha256(data).hexdigest() != record['sha256']:
            raise ValueError('Changed original accepted RK48 asset: ' + key)
        path = work / Path(record['path']).name
        path.write_bytes(data)
        assets[key] = path
    command = ['node', '--expose-gc', '--max-old-space-size=' + str(args.node_heap),
        str(HERE / 'exact_20261114_stage28_original_rk48_readout.mjs'),
        '--repo-root', str(REPO), '--source-topic', str(source),
        '--packet', str(packet), '--anchor', str(anchor), '--out-dir', str(out / 'readout')]
    for key, path in assets.items():
        command += ['--' + key, str(path)]
    write(out / 'intent.json', dict(scope=__doc__, command=command,
        source_sha256_at_start=source_hashes, source_origin_sha256=sha(origin_path),
        packet_manifest_sha256=PACKET_SHA, anchor_manifest_sha256=ANCHOR_SHA,
        source_repository=os.environ.get('GITHUB_REPOSITORY'), source_commit=os.environ.get('GITHUB_SHA'),
        original_public_assets=anchor_manifest['public_assets'],
        original_stage=28, no_new_shooting_solve=True, original_RK_grid_unchanged=True,
        no_global_field_adoption=True, complete_task=False))
    started = time.monotonic()
    with (out / 'readout.log').open('wb') as stream:
        result = subprocess.run(command, cwd=REPO, stdout=stream, stderr=subprocess.STDOUT, check=False)
    write(out / 'readout-exit.json', dict(actual_exit_code=result.returncode, seconds=time.monotonic() - started))
    if result.returncode:
        raise RuntimeError('Original stage28 replay failed; retain the actual readout log/identity diagnostics')

    import numpy as np
    import exact_20261114_common_grid_refinement as core
    from exact_20261114_source_knot_rr_probe import TargetMetricTail

    readout = out / 'readout'
    complete = json.loads((readout / 'complete-local.json').read_text())
    samples = json.loads((readout / 'background-local.json').read_text())['points']
    identity = json.loads((readout / 'legacy-point-replay-identity.json').read_text())
    if identity.get('passed') is not True:
        raise ValueError('A/B/C identity must pass before local finite-field comparisons')
    theta = 2*np.pi*np.arange(args.angles)/args.angles
    radial = np.asarray([p['r'] for p in samples], np.longdouble)
    cutoff = max(row['x'] for row in complete['rows'])
    selection = {'f8': {42/48, cutoff}, 'f16': {42/48, 45/48, cutoff},
                 'f48': {row['x'] for row in complete['rows']}}
    layers = {}
    for label, chosen in selection.items():
        metadata = dict(complete)
        metadata['rows'] = [dict(row, file=str(Path('readout') / row['file']))
                            for row in complete['rows'] if row['x'] in chosen]
        metadata['scope'] = 'Explicit local selection only; not a complete tail'
        path = out / ('local-' + label + '.json')
        write(path, metadata)
        layers[label] = TargetMetricTail(path)

    def maximum(values, indices=None):
        data = np.asarray(values)
        if indices is None:
            indices = np.arange(len(samples))
        local = np.unravel_index(np.argmax(data[indices]), data[indices].shape)
        i, j = int(indices[local[0]]), int(local[1])
        return dict(value=float(data[i, j]), r=samples[i]['r'],
                    source_profile_x=samples[i]['source_profile_x'], theta=float(theta[j]),
                    original_sample_origins=samples[i]['origins'])

    def jet_maxima(values, indices=None):
        return {key: maximum(np.linalg.norm(value, axis=-1), indices) for key, value in values.items()}

    def represented(tail):
        answer = {key: np.empty((len(radial), args.angles, 3), np.longdouble)
                  for key in core.JET_RULES}
        spans = np.clip(np.searchsorted(tail.r, radial, side='right')-1, 0, len(tail.r)-2)
        for index in sorted(set(spans)):
            selected = np.flatnonzero(spans == index)
            h = tail.r[index+1]-tail.r[index]
            u = (radial[selected]-tail.r[index])/h
            if u.min() < -1e-10 or u.max() > 1+1e-10:
                raise ValueError('Requested common sample leaves the local span')
            coefficients = core.angle_coefficients(tail.span(int(index)), args.angles)
            for key, (dr, dt) in core.JET_RULES.items():
                answer[key][selected] = core.evaluate(coefficients[dt], np.clip(u, 0, 1), h, dr)
        answer['position'][:, :, 2] -= np.longdouble(packet_manifest['layers']['fine']['small_mean_at_cut'])
        return answer

    values = {name: represented(tail) for name, tail in layers.items()}
    measured = {name: core.measured_geometry(jets, radial, samples, theta)
                for name, jets in values.items()}
    old450 = np.array([i for i, p in enumerate(samples)
        if any(o.get('common_stage') == 450 for o in p['origins'])], dtype=int)
    old451 = np.array([i for i, p in enumerate(samples)
        if any(o.get('common_stage') == 451 for o in p['origins'])], dtype=int)
    if len(old450) != 17 or len(old451) != 17:
        raise ValueError('Every original 17-point common stage must be retained')
    windows = {'entire_local_union': None, 'original_common_stage450': old450,
               'original_common_stage451': old451}
    comparisons = {}
    for left, right in [('f8', 'f16'), ('f16', 'f48'), ('f8', 'f48')]:
        difference = {key: values[right][key]-values[left][key] for key in core.JET_RULES}
        comparisons[left+'-to-'+right] = {
            window: dict(six_jet_sample_differences=jet_maxima(difference, indices),
                metric_scalar_difference=maximum(abs(measured[right]['metric']-measured[left]['metric']), indices),
                curvature_scalar_difference=maximum(abs(measured[right]['kappa']-measured[left]['kappa']), indices))
            for window, indices in windows.items()}

    def scalar_angular_coefficients(c):
        polynomial = np.zeros((6, c.shape[0], 3), np.clongdouble)
        polynomial[0] = c
        return core.angle_coefficients(polynomial, args.angles)[0][0]

    def angular_error(coefficients):
        value = scalar_angular_coefficients(coefficients)
        norm = np.linalg.norm(value, axis=-1)
        k = int(np.argmax(norm))
        return dict(vector_max=float(norm[k]), theta=float(theta[k]), vector=[float(v) for v in value[k]],
                    vertical_max=float(np.max(abs(value[:, 2]))),
                    horizontal_max=float(np.max(np.linalg.norm(value[:, :2], axis=-1))))

    def cubic_velocity(tail, radius):
        index = int(np.clip(np.searchsorted(tail.r, radius, side='right')-1, 0, len(tail.r)-2))
        _, v0, a0 = tail.node_coefficients(index)
        _, v1, a1 = tail.node_coefficients(index+1)
        h = tail.r[index+1]-tail.r[index]
        u = (radius-tail.r[index])/h
        c = np.stack([v0, h*a0, 3*(v1-v0)-h*(2*a0+a1),
                      2*(v0-v1)+h*(a0+a1)])
        value = sum(c[j]*u**j for j in range(4))
        derivative = sum(j*c[j]*u**(j-1)/h for j in range(1, 4))
        return value, derivative

    actual = layers['f48']
    node_consistency = []
    for index in range(1, len(actual.r)-1):
        radius = actual.r[index]
        _, velocity, acceleration = actual.node_coefficients(index)
        record = dict(r=float(radius), original_source_x=actual.rows[index]['x'],
                      is_newly_retained_RK48_point=actual.rows[index]['x'] != 45/48,
                      GW_acceleration_scope='Target-metric completion of original point jets, not an independently established trajectory derivative.',
                      reference_cubic_velocity={})
        for label in ('f8', 'f16'):
            v, a = cubic_velocity(layers[label], radius)
            record['reference_cubic_velocity'][label] = dict(
                velocity_minus_actual=angular_error(v-velocity),
                radial_derivative_minus_actual_GW=angular_error(a-acceleration))
        rr = actual.r[index-1:index+2]
        vv = [actual.node_coefficients(j)[1] for j in range(index-1, index+2)]
        weights = [(2*radius-rr[(j+1) % 3]-rr[(j+2) % 3]) /
                   ((rr[j]-rr[(j+1) % 3])*(rr[j]-rr[(j+2) % 3])) for j in range(3)]
        derivative = sum(weight*v for weight, v in zip(weights, vv))
        record['velocity_only_adjacent_quadratic_derivative_minus_GW'] = angular_error(derivative-acceleration)
        record['velocity_only_stencil_r'] = [float(x) for x in rr]
        record['velocity_only_interpretation'] = ('A local derivative estimate using only three actual velocity nodes; '
            'independent of GW acceleration inputs, but without a continuous derivative error certificate.')
        node_consistency.append(record)

    arrays = {'r': actual.r}
    for index in range(len(actual.r)):
        for key, coefficients in zip(('position', 'radial_first', 'radial_second'), actual.node_coefficients(index)):
            arrays['node'+str(index)+'_'+key+'_coefficients'] = np.asarray(coefficients, np.complex128)
    np.savez_compressed(out / 'local-GW-node-coefficients.npz', **arrays)
    report = dict(finished=True, scope=__doc__, original_stage=28, angles=args.angles,
        source_profile_interval=[42/48, cutoff], radial_interval=[float(actual.r[0]), float(actual.r[-1])],
        local_common_radial_samples=len(samples), original_common_stage450_samples=len(old450),
        original_common_stage451_samples=len(old451), legacy_three_point_identity=identity,
        layers={label: dict(nodes=len(tail.r), source_profile_x=[row['x'] for row in tail.rows],
            physical_r=[float(x) for x in tail.r], GW_node_diagnostics=tail.diag,
            sampled_geometry={window: {key: maximum(value, indices) for key, value in measured[label].items()}
                              for window, indices in windows.items()}) for label, tail in layers.items()},
        adjacent_and_baseline_comparisons=comparisons, actual_node_velocity_consistency=node_consistency,
        original_saved_global_f8_f16_rr_difference=packet_manifest['original_comparison']['layer_comparison']['maxima']['radial_second'],
        output_node_coefficients_sha256=sha(out / 'local-GW-node-coefficients.npz'),
        replay_result_sha256=sha(readout / 'result.json'), source_sha256_at_start=source_hashes,
        seconds=time.monotonic()-begin, original_integration_grid_unchanged=True, no_new_shooting_solve=True,
        limitations=['All maxima are the stated finite local samples; no global maximum or continuous enclosure.',
            'New radial readout data use the same finite RK48 trajectory, not a more accurate BVP or time integrator.',
            'The GW rule is retained only for this local comparison; no complete assembly has adopted a new field.',
            'Metric and curvature changes are measured anew; they are not inherited from the original point jets.',
            'No independent criterion requiring machine-precision six-jet differences is added to the topic README.',
            'This does not address the large-amplitude candidate, all-phase reach or complete-task acceptance.'])
    write(out / 'report.json', report)
    print(json.dumps(dict(event='stage28-local-original-RK48-GW-complete',
        seconds=report['seconds'], angles=args.angles, local_radial_samples=len(samples),
        layers={label: {key: maximum(value)['value'] for key, value in measured[label].items()} for label in layers}), allow_nan=False), flush=True)


if __name__ == '__main__':
    main()
