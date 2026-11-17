#!/usr/bin/env python3
"""Read the same actual radial geometry plus a genuine core witness and ball.

This extension hooks the frozen reconstruction's actual positions.  It does
not replace any jet, ODE, Gram, or curvature computation.  The new extrema
cover only the specified open tail samples, not the entire closed surface.
"""
import argparse
import contextlib
import gzip
import hashlib
import importlib.util
import io
import json
from pathlib import Path

import numpy as np


def main(args):
    source_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    raw = args.witness_prefix.read_bytes()
    prefix = json.loads(gzip.decompress(raw))
    if not prefix.get('success'):
        raise ValueError('The witness prefix must be an actual accepted source')
    core = np.asarray(prefix['states'][0])
    major = float(core[0]+np.sum(core[1:prefix['M']+1]))
    witness = np.array([0., major, 0.])
    spec = importlib.util.spec_from_file_location('frozen_radial_geometry', args.radial_reader)
    radial = importlib.util.module_from_spec(spec); spec.loader.exec_module(radial)
    original = radial.read_geometry
    extrema = dict(minimum_witness_distance=float('inf'), maximum_origin_norm=0.,
                   max_delta_P_or_Ptilde=0., max_delta_K=0., max_delta_c=0.,
                   maximum_reported_mean_tolerance=0.)
    witness_location = {}; ball_location = {}
    def observed(alpha, xy, mean_height, data, coefficients, rho):
        nonlocal witness_location, ball_location
        geometry = original(alpha, xy, mean_height, data, coefficients, rho)
        points = geometry['F']
        distances = np.linalg.norm(points-witness, axis=2)
        norms = np.linalg.norm(points, axis=2)
        if np.min(distances) < extrema['minimum_witness_distance']:
            i, j = np.unravel_index(np.argmin(distances), distances.shape)
            extrema['minimum_witness_distance'] = float(distances[i, j])
            witness_location = dict(r=float(data['r'][i]), phi=float(2*np.pi*j/args.angles),
                                    point=points[i, j].tolist())
        if np.max(norms) > extrema['maximum_origin_norm']:
            i, j = np.unravel_index(np.argmax(norms), norms.shape)
            extrema['maximum_origin_norm'] = float(norms[i, j])
            ball_location = dict(r=float(data['r'][i]), phi=float(2*np.pi*j/args.angles),
                                 point=points[i, j].tolist())
        for output, key in [('max_delta_P_or_Ptilde', 'delta_P'), ('max_delta_K', 'delta_K'), ('max_delta_c', 'delta_c')]:
            extrema[output] = max(extrema[output], float(np.max(abs(data[key]))))
        if 'root_residual_tolerance' in data:
            extrema['maximum_reported_mean_tolerance'] = max(extrema['maximum_reported_mean_tolerance'],
                float(np.max(data['root_residual_tolerance'])))
        return geometry
    radial.read_geometry = observed
    final_out = args.out
    args.out = None
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        radial.run(args)
    result = json.loads(captured.getvalue())
    result['measurement_extension_sha256'] = source_sha
    result['core_witness'] = dict(prefix_sha256=hashlib.sha256(raw).hexdigest(),
                                  point=witness.tolist(), major=major,
                                  definition='Quarter-turn of the actual phi=0 core point from the accepted prefix',
                                  same_field_full_alignment_certified=False)
    result['tail_position_measurements'] = dict(**extrema, witness_location=witness_location,
        ball_location=ball_location, reflection_about_z0_preserves_both_values=True,
        scope='Actual sampled open-tail positions only; no full closed D or held lower bound inferred')
    if final_out:
        final_out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    folder = Path(__file__).parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--background', type=Path, required=True)
    parser.add_argument('--out', type=Path)
    parser.add_argument('--witness-prefix', type=Path, required=True)
    parser.add_argument('--radial-reader', type=Path, default=folder/'2026-11-17-parallel-geometry-radial-tail-readout.py')
    parser.add_argument('--height-reader', type=Path, default=folder/'2026-11-17-parallel-geometry-stable-height-reader.py')
    parser.add_argument('--angular-helper', type=Path, default=folder/'2026-11-17-parallel-model-angular-reconstruct.py')
    parser.add_argument('--angles', type=int, default=512)
    parser.add_argument('--radial-gauss', type=int, default=8)
    parser.add_argument('--height-gauss', type=int, default=8)
    parser.add_argument('--height-anchor', choices=('left', 'right'))
    parser.add_argument('--anchor-mean-height', type=float, default=0.)
    parser.add_argument('--batch-cells', type=int, default=8)
    main(parser.parse_args())
