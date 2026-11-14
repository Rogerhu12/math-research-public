#!/usr/bin/env python3
"""Compare sampled angular representation of one unchanged physical field.

Original physical latitude positions and their angular jets are composed with
the existing exact chart inverse/chain rules. The original live frame function
then evaluates their Frenet velocity. Both the old chart and the full accepted
support-core reference are screened at several Fourier orders. No radial ODE,
BVP, tail worker, mean-height integration or new accepted field is produced.
Latitude position projection error is invariant to its common vertical mean;
the mean is removed on both sides for that error only. No converted checkpoint
or vertically translated surface is written. All output is finite sampling.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
from types import SimpleNamespace
import numpy as np
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def document(path):
    path = Path(path)
    data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == '.gz' else data)


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('input', 'source-topic', 'port', 'audit', 'out'):
        p.add_argument('--' + name, type=Path, required=True)
    p.add_argument('--angular', type=int, default=2048)
    p.add_argument('--radial', type=int, default=31)
    p.add_argument('--modes', type=int, nargs='+', default=[28, 32, 40, 48, 64])
    a = p.parse_args()
    if a.out.exists():
        raise FileExistsError('Fresh output required')
    import strong_initial_laws_interior_fullmean_audit as laws
    if sha(HERE/'strong_initial_laws_interior_fullmean_audit.py') != '35155b17516ce3ff72ddfc957894e53cbd2c7a4a6707d57e62887a8d72e4fbe0':
        raise ValueError('Frozen original provider loader differs')
    observations = dict(provider_loads=0, saved_fields=[])
    pb = laws.install_audit_loader(load, observations)('strong_chart_spectrum_saved', HERE/'geometric-checkpoint-core-pullback.py')
    meta = document(a.input)
    audit = document(a.audit)
    if audit['input_sha256'] != sha(a.input):
        raise ValueError('The original physical audit does not bind this accepted field')
    saved, loader = pb.load_saved(a.input, a.source_topic, a.port, angular=int(meta['config']['angular']))
    f = saved.flow
    N = a.angular
    if N < 1360 or max(a.modes) > 128 or min(a.modes) < saved.M:
        raise ValueError('Keep original or higher angular resolution and projection order')
    ss = np.unique(np.r_[np.linspace(0., f.end, a.radial), f.breaks,
        [row['s'] for row in audit['top'].values()], 1.328164157021213, .9721471856177173])
    psi = 2*np.pi*np.arange(N)/N
    frame = f.frame.__func__
    frame_path = Path(frame.__code__.co_filename)
    charts = [('original_reference', f.general_core_chart),
              ('accepted_full_core_reference', pb.charts.GeneralCoreChart(
                  meta['core']['coefficients'], meta['core']['frequencies'], f.end))]
    original_basis = f.basis(N)
    results = []
    frame_equivalence = 0.
    inverse_max = 0.
    for label, chart in charts:
        peak = {M: {} for M in a.modes}
        for first in range(0, len(ss), 4):
            s = ss[first:first+4]
            ng = chart.geometry(s, psi, f.profile)
            eta, inverse_error, unused = saved.inverse(s, ng['theta'])
            inverse_max = max(inverse_max, float(inverse_error))
            og = saved.angle(s, eta)
            old_base = saved.base(s, eta)
            Y = saved.sol.sol(s)
            pos = old_base['pos'] + saved.q*saved.synth(Y, eta, 0)
            old_d = old_base['p1'] + saved.q*saved.synth(Y, eta, 1)
            old_dd = old_base['p2'] + saved.q*saved.synth(Y, eta, 2)
            ep = ng['rho']/og['rho']
            epp = (ng['rhop']-og['rhop']*ep*ep)/og['rho']
            d = old_d*ep[:, :, None]
            dd = old_dd*(ep*ep)[:, :, None] + old_d*epp[:, :, None]
            marker1 = np.zeros((1, N, 3))
            marker2 = np.zeros((1, N, 3))
            proxy = SimpleNamespace(geo=lambda s0, N0: ng, profile=f.profile)
            proxy.values = lambda state, B: d-ng['p1'] if B is marker1 else dd-ng['p2']
            exact = frame(proxy, s, None, marker1, marker2)
            if label == 'original_reference':
                direct = f.frame(s, saved.q*Y, original_basis[1], original_basis[2])
                err = max(float(abs(exact[k]-direct[k]).max()) for k in ('d', 'dd', 'Vnormal', 'V'))
                frame_equivalence = max(frame_equivalence, err)
                if err > 3e-11:
                    raise ValueError('Original-frame coordinate replay differs')
            for M in a.modes:
                B, B1, B2 = pb.basis_values(M, saved.mode, psi)
                C = pb.project(pos-ng['pos'], B)
                reconstructed = ng['pos'] + pb.values(C, B)
                diff = reconstructed-pos
                diff[:, :, 2] -= np.mean(diff[:, :, 2], axis=1)[:, None]
                projected_proxy = SimpleNamespace(geo=lambda s0, N0: ng, profile=f.profile, values=pb.values)
                projected = frame(projected_proxy, s, C, B1, B2)
                r0 = exact['V']-ng['s1']
                velocity = ng['s1']+pb.values(pb.project(r0, B), B)
                velocity[:, :, 2] += np.mean(r0[:, :, 2], axis=1)[:, None]
                r1 = projected['V']-ng['s1']
                v_projected = ng['s1']+pb.values(pb.project(r1, B), B)
                v_projected[:, :, 2] += np.mean(r1[:, :, 2], axis=1)[:, None]
                metric = np.sum(projected['d']**2, axis=2)/ng['rho']**2/f.profile(s)[0][:, None]**2-1
                quantities = dict(
                    latitude_position_projection=np.linalg.norm(diff, axis=2).max(axis=1),
                    angular_first_projection=np.linalg.norm(projected['d']-d, axis=2).max(axis=1),
                    angular_second_projection=np.linalg.norm(projected['dd']-dd, axis=2).max(axis=1),
                    exact_field_velocity_projection=np.linalg.norm(velocity-exact['V'], axis=2).max(axis=1),
                    projected_field_velocity_projection=np.linalg.norm(v_projected-projected['V'], axis=2).max(axis=1),
                    projected_vs_exact_normal_velocity=np.linalg.norm(projected['Vnormal']-exact['Vnormal'], axis=2).max(axis=1),
                    projected_field_metric_G_fft_l1=np.sum(abs(np.fft.fft(metric, axis=1)/N), axis=1))
                for key, value in quantities.items():
                    j = int(np.argmax(value))
                    if key not in peak[M] or value[j] > peak[M][key]['value']:
                        peak[M][key] = dict(value=float(value[j]), s=float(s[j]))
                del B, B1, B2
        result = dict(reference=label, coefficients=chart.coefficients.tolist(),
            frequencies=chart.frequencies.tolist(), rows=[dict(modes=M, peaks=peak[M]) for M in a.modes])
        results.append(result)
        print(json.dumps(result), flush=True)
    inputs = {str(path): sha(path) for path in (a.input, a.audit, a.port)}
    for item in meta['pp_coefficient_chunks']:
        path = a.input.parent/item['file']
        if sha(path) != item['sha256']:
            raise ValueError('Original complete physical polynomial chunk differs')
        inputs[str(path)] = item['sha256']
    output = dict(scope=__doc__, inputs_sha256=inputs, wrapper_sha256=sha(__file__),
        sources={str(path): sha(path) for path in (frame_path, HERE/'geometric-checkpoint-core-pullback.py',
            HERE/'geometric-general-core-chart.py', HERE/'strong_initial_laws_interior_fullmean_audit.py')},
        source_transforms=loader.TRANSFORMS, source_dependencies=loader.dependencies(a.source_topic),
        provider_observations=observations, angular=N, radial_samples=ss.tolist(),
        physical_profile=meta['frozen_profile'], full_core=meta['core'], gauge=saved.q,
        original_frame_replay_max_difference=frame_equivalence, angle_inverse_max_error=inverse_max,
        results=results, full_surface_certificate=False, actual_coordinate_refinement_solved=False,
        all_original_fields_unchanged=True, output_warm_checkpoint_created=False,
        limitations=['These selected radial samples do not bound the full field.',
            'Reprojection does not solve the new Galerkin BVP or remove the physical error of the source field.',
            'No absolute mean height, diameter, curvature maximum, isometry, closure, reach or held is inferred.'])
    with a.out.open('x') as stream:
        json.dump(output, stream, indent=2)
        stream.write('\n')


if __name__ == '__main__':
    main()
