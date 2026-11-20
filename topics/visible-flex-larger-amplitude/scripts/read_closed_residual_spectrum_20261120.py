#!/usr/bin/env python3
"""Read exact finite angular energy and optional point curvature of a bundle.

This is a diagnostic of the existing finite shared-quintic model. It does
not bound any continuous surface quantity. Reports and arrays stay in scratch.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np
from scipy.fft import dct, dst


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--bundle', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--angles', type=int, default=2048)
    parser.add_argument('--curvature', action='store_true')
    args = parser.parse_args()
    if args.out.exists():
        raise FileExistsError('Use a fresh diagnostic output name')
    topic = args.repo/'topics/visible-flex-larger-amplitude'
    batch_path = topic/'scripts/resume_20261120_batched_closed_gram.py'
    dense_path = topic/'notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py'
    helper_path = topic/'scripts/resume_20261120/fullclosed_lm.py'
    batch = load('residual_spectrum_batch', batch_path)
    helper = load('residual_spectrum_helpers', helper_path)
    data = np.load(args.bundle, allow_pickle=False)
    operator = batch.create(dense_path, data['mesh'], data['a_stages'],
                            float(data['radius']), data['fixed_core_first3'],
                            M=(data['qjets'].shape[2]-2)//3, N=args.angles,
                            width=float(data['width']), quarter=True)
    x, affine = operator.pack(data['qjets'], float(data['Hcap']), require_affine=True)
    residual = operator.raw_residual(x)
    length = operator.N-1
    cosine = dct(residual[:, :, [0, 2]], type=1, axis=1)/length
    cosine[:, [0, -1], :] /= 2
    sine = dst(residual[:, 1:-1, 1], type=1, axis=1)/length
    power = np.sum(cosine*cosine, axis=(0, 2))/2
    power[[0, -1]] *= 2
    power[1:-1] += np.sum(sine*sine, axis=0)
    cumulative = np.cumsum(power)/power.sum()
    e, f, g = residual[..., 0], residual[..., 1], residual[..., 2]
    norm = (abs(e+g)+np.sqrt((e-g)**2+4*f*f))/2
    peaks = np.max(norm, axis=1)
    indices = np.argsort(peaks)[-12:][::-1]
    report = dict(schema='closed-finite-residual-spectrum-20261120-v1',
                  source_sha256=sha(__file__), bundle_sha256=sha(args.bundle),
                  batch_sha256=sha(batch_path), dense_sha256=sha(dense_path),
                  helper_sha256=sha(helper_path), affine=affine,
                  raw_sse_parseval=float(power.sum()*operator.full_N),
                  energy_mode_cutoffs={str(q):int(np.searchsorted(cumulative, q))
                                       for q in (.5, .9, .99, .999)},
                  first_21_mode_energy_fractions=(power[:21]/power.sum()).tolist(),
                  top_stage_peaks=[[int(i), float(operator.times[i]), float(peaks[i]),
                                    float(operator.phi[np.argmax(norm[i])])]
                                   for i in indices],
                  continuous_geometry_certified=False)
    if args.curvature:
        report['point_curvature'] = helper.point_curvatures(operator, x)
        prepared = operator.prepare(x)
        maximum_radius = 0.
        radius_where = None
        for stage in range(operator.P):
            y = operator.stage_jets(prepared.jets, stage)[0]
            chi, _, _, lift, _, _ = operator.lift_scalar[stage]
            position = operator.synth(y)+lift*prepared.er
            position[:, 2] += chi*prepared.height
            radius = np.linalg.norm(position, axis=1)
            k = int(np.argmax(radius))
            if radius[k] > maximum_radius:
                maximum_radius = float(radius[k])
                radius_where = dict(stage=stage, s=float(operator.times[stage]),
                                    phi=float(operator.phi[k]))
        # The closed model includes reflection in z=0. Together with its
        # pi angular symmetry this contains -F for every active-body F.
        # Axial phase rotation preserves these radii; adding fixed interior
        # cap markers does not remove the unchanged active-body point pairs.
        diameter_lower = 2*maximum_radius
        curvature = report['point_curvature']
        report['closed_body_diameter_point_lower'] = dict(
            value=diameter_lower, maximum_radius_point=radius_where,
            cap_height_lower=2*abs(float(prepared.height)),
            scope='Reflected closed body and its axial phase family only; '
                  'a different family reference F0 must be assessed separately',
            reach_ratio_necessary_point_product=(.03*diameter_lower*
                curvature['maximum_absolute_principal_curvature'])
                if curvature.get('complete') else None,
            interval_certified=False)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report), flush=True)


if __name__ == '__main__':
    main()
