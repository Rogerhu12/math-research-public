#!/usr/bin/env python3
"""Read candidate phase-geometry diagnostics on the original finite grid.

No continuous support, distance, embeddedness, reach, or held certificate is
asserted. In particular nearest sampled distance is an upper approximation
to distance from the complete image, and cannot be a held lower bound.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo', type=Path, required=True)
    p.add_argument('--bundle', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    if a.out.exists():
        raise FileExistsError('Use a fresh output name')
    topic = a.repo/'topics/visible-flex-larger-amplitude'
    batch_path = topic/'scripts/resume_20261120_batched_closed_gram.py'
    dense_path = topic/'notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py'
    batch = load('closed_phase_batch', batch_path)
    data = np.load(a.bundle, allow_pickle=False)
    o = batch.create(dense_path, data['mesh'], data['a_stages'],
                     float(data['radius']), data['fixed_core_first3'],
                     M=(data['qjets'].shape[2]-2)//3, N=2048,
                     width=float(data['width']), quarter=True)
    x, affine = o.pack(data['qjets'], float(data['Hcap']), require_affine=True)
    prepared = o.prepare(x)
    core = o.six_jets(prepared, 0)['F']
    witness_radius = float(core[0, 0])
    beta = np.array([.25, .4])
    minimum_support = np.full(len(beta), np.inf)
    support_where = [None for _ in beta]
    maximum_radius = 0.
    radius_where = None
    minimum_distance = float('inf')
    distance_where = None
    minimum_z = float('inf')
    co, si = np.cos(o.phi), np.sin(o.phi)
    for stage in range(o.P):
        jets = o.six_jets(prepared, stage)
        position, velocity, angular = jets['F'], jets['Fs'], jets['Fphi']
        normal = np.cross(angular, velocity)
        area = np.linalg.norm(normal, axis=1)
        if np.any(area <= 0) or not np.isfinite(area).all():
            raise ValueError('Nonregular sampled stage')
        normal /= area[:, None]
        horizontal = np.sum(position[:, :2]*normal[:, :2], axis=1)
        vertical = position[:, 2]*normal[:, 2]
        support = horizontal[:, None]+vertical[:, None]*beta[None, :]
        for j in range(len(beta)):
            k = int(np.argmin(support[:, j]))
            if support[k, j] < minimum_support[j]:
                minimum_support[j] = float(support[k, j])
                support_where[j] = [stage, float(o.times[stage]), float(o.phi[k])]
        radius = np.linalg.norm(position, axis=1)
        k = int(np.argmax(radius))
        if radius[k] > maximum_radius:
            maximum_radius = float(radius[k])
            radius_where = [stage, float(o.times[stage]), float(o.phi[k])]
        cart_x = position[:, 0]*co-position[:, 1]*si
        cart_y = position[:, 0]*si+position[:, 1]*co
        # Half-period/reflection orbits allow independent horizontal signs;
        # the witness is Rot(pi/2)F(core,phi=0)=(0,witness_radius,0).
        distance = np.sqrt(cart_x**2+(np.abs(cart_y)-witness_radius)**2+position[:, 2]**2)
        k = int(np.argmin(distance))
        if distance[k] < minimum_distance:
            minimum_distance = float(distance[k])
            distance_where = [stage, float(o.times[stage]), float(o.phi[k])]
        minimum_z = min(minimum_z, float(np.min(position[:, 2])))
    flat_cap_distance = float(np.hypot(max(0., abs(witness_radius)-o.R), prepared.height))
    # For each unmarked flat cap, the positive-definite support is beta*|H|.
    closed_support = np.minimum(minimum_support, beta*abs(float(prepared.height)))
    report = dict(schema='closed-phase-point-geometry-20261120-v1',
                  source_sha256=sha(__file__), bundle_sha256=sha(a.bundle),
                  batch_sha256=sha(batch_path), dense_sha256=sha(dense_path),
                  affine=affine, height=float(prepared.height),
                  observed_upper_half_minimum_z=minimum_z,
                  sampled_diameter_lower=2*maximum_radius,
                  maximum_radius_where=radius_where,
                  weighted_support_points=[dict(beta=float(b),
                      active_minimum=float(minimum_support[j]),
                      including_unmarked_caps=float(closed_support[j]),
                      active_worst=support_where[j]) for j, b in enumerate(beta)],
                  rotated_core_witness=[0., witness_radius, 0.],
                  nearest_body_sample_distance=minimum_distance,
                  nearest_body_sample=distance_where,
                  exact_unmarked_flat_cap_distance=flat_cap_distance,
                  sampled_distance_over_sampled_diameter=(min(minimum_distance,
                      flat_cap_distance)/(2*maximum_radius)),
                  interpretation='Point diagnostics only. The sampled nearest '
                      'distance is NOT a continuous lower bound; the displayed '
                      'ratio is NOT held/D. Fixed cap markers and exact scalar '
                      'roundoff are not certified by this reader.',
                  continuous_geometry_certified=False)
    a.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report), flush=True)


if __name__ == '__main__':
    main()
