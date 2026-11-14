#!/usr/bin/env python3
"""Background-only enclosing-ball screen after changing the initial speed law.

The accepted physical profile and its original provider determine every later
piece, including the bridge.  Only the first piece is replaced by the explicit
radius-preserving pulse from strong_initial_speed_pulse_budget.py.  No Flow,
RHS, Jac, BVP, Node worker, actual flexible field, tail, or cap is evaluated.
The sampled background envelope and its unit-speed sampling pad do not include
an interval enclosure of the provider's quadrature error.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'
import argparse
import gzip
import hashlib
import importlib.util
import json
import math
import time
from pathlib import Path
import numpy as np

P = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--accepted-reference', type=Path, required=True)
    parser.add_argument('--pulse-budget', type=Path, required=True)
    parser.add_argument('--samples-per-piece', type=int, default=1025)
    parser.add_argument('--batch', type=int, default=16)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    started = time.time()
    hashes = {str(path): digest(path) for path in [Path(__file__),
        args.accepted_reference, args.pulse_budget,
        P/'alternative-neck-provider.py', P/'strong_angle_boost.py',
        P/'alternative-neck-flatturn.py', P/'alternative-neck-excursion.py']}
    raw = args.accepted_reference.read_bytes()
    record = json.loads(gzip.decompress(raw) if args.accepted_reference.suffix == '.gz' else raw)
    budget = json.loads(args.pulse_budget.read_text())
    if not record['solver_success'] or record.get('audit_pending'):
        raise ValueError('An accepted reference is required')
    if budget['accepted_reference_sha256'] != digest(args.accepted_reference):
        raise ValueError('The exact first-piece budget has a different reference')
    if args.samples_per_piece < 3 or args.batch < 1:
        raise ValueError('Invalid numerical sampling settings')
    spec = importlib.util.spec_from_file_location('strong_pulse_envelope_provider', P/'alternative-neck-provider.py')
    provider = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(provider)
    cfg = dict(record['frozen_profile'])
    prefix = provider.NeckPrefix(cfg)
    bridge = provider.NeckTerminalBridge(record['physical_tail_cut'])
    pieces = prefix.segments + bridge.segments
    first = pieces[0]
    if first['kind'] != 'hermite' or first['a0'] != 1.:
        raise ValueError('Unexpected first physical piece')
    delta, V, k0 = (float(cfg[key]) for key in ('delta', 'vu', 'start_acceleration'))
    ugrid = np.linspace(0., 1., args.samples_per_piece)
    rows = []
    for pulse in (0., .2, .35, .5, .6):
        # At b=0 retain the exact original floating computation and first jet.
        c = V/2 + 16*pulse/35
        S = first['length'] if pulse == 0 else 2*delta/(math.sqrt(c*c+k0*delta/3)+c)
        def initial_jet(u):
            if pulse == 0:
                return provider.piece_jet(first, u)
            v = V*u*u*(3-2*u) + k0*S*u*(1-u)**2 + 64*pulse*u**3*(1-u)**3
            dv = 6*V*u*(1-u)+k0*S*(1-u)*(1-3*u)+192*pulse*u*u*(1-u)**2*(1-2*u)
            primitive = (V*u**3*(2-u)/2 + k0*S*u*u*(6-8*u+3*u*u)/12
                + (16*pulse/35)*u**4*(35-84*u+70*u*u-20*u**3))
            return 1+S*primitive, v, dv/S
        z0 = 0.
        s0 = 0.
        best = dict(norm=0.)
        max_k = 0.
        max_gaussian = 0.
        largest_gap = 0.
        endpoint_quad_disagreement = 0.
        segment_rows = []
        for index, segment in enumerate(pieces):
            length = S if index == 0 else segment['length']
            segment_k = 0.
            h_end = None
            for start in range(0, len(ugrid), args.batch):
                u = ugrid[start:start+args.batch]
                if index == 0:
                    radius, v, acc = initial_jet(u)
                    q = u[:, None]*provider.base.gu[None, :]
                    vq = initial_jet(q)[1]
                    h = length*u/2*(np.sqrt(1-vq*vq)@provider.base.gw)
                else:
                    radius, v, acc = provider.piece_jet(segment, u)
                    if segment['kind'] == 'boost' and not segment.get('strong_angle_boost'):
                        vq = provider.velocity(segment, u[:, None]*provider.base.gu[None, :])
                        h = length*u/2*(np.sqrt(1-vq*vq)@provider.base.gw)
                    else:
                        h = length*provider.fl.integral(segment, u, 'cos')
                vertical_speed = np.sqrt(1-v*v)
                curvature = np.maximum(abs(acc)/vertical_speed, vertical_speed/radius)
                segment_k = max(segment_k, float(curvature.max()))
                max_gaussian = max(max_gaussian, float(np.max(abs(acc/radius))))
                z = z0+h
                norm = np.hypot(radius, z)
                j = int(np.argmax(norm))
                if float(norm[j]) > best['norm']:
                    best = dict(norm=float(norm[j]), radius=float(radius[j]), height=float(z[j]),
                        s=float(s0+length*u[j]), segment=index, kind=segment['kind'], u=float(u[j]))
                if start+len(u) == len(ugrid):
                    h_end = float(h[-1])
            if index > 0 or pulse == 0:
                endpoint_quad_disagreement += abs(h_end-segment['dh'])
            segment_rows.append(dict(index=index, kind=segment['kind'], length=length,
                height=h_end, curvature_max_sample=segment_k))
            max_k = max(max_k, segment_k)
            largest_gap = max(largest_gap, length/(len(ugrid)-1))
            z0 += h_end
            s0 += length
        rows.append(dict(pulse=pulse, initial_length=S, first_height=segment_rows[0]['height'],
            background_prefix_bridge_height=z0, background_prefix_bridge_length=s0,
            twice_max_sampled_norm=2*best['norm'], maximizer=best,
            unit_speed_diameter_sampling_pad=largest_gap,
            provider_endpoint_quadrature_disagreement=endpoint_quad_disagreement,
            envelope_with_sampling_pad_and_endpoint_disagreement=2*best['norm']+largest_gap+2*endpoint_quad_disagreement,
            background_curvature_max_sample=max_k,
            metric_necessary_curvature_lower_sample=math.sqrt(max_gaussian),
            initial_endpoint_jet=[float(np.asarray(x)) for x in initial_jet(np.asarray(1.))],
            initial_radius_endpoint_error=float(initial_jet(np.asarray(1.))[0]-(1+delta)),
            remaining_tail_and_cap_height_B_formula='2*sqrt(rCut^2+(background_prefix_bridge_height+B)^2)',
            rCut=float(record['physical_tail_cut']['radius']), segments=segment_rows))
    result = dict(scope=__doc__, source_sha256_at_start=hashes,
        reference_profile=cfg, physical_cut=record['physical_tail_cut'],
        reference_physical_length=record['meridian_length'],
        baseline_length_disagreement=rows[0]['background_prefix_bridge_length']-record['meridian_length'],
        samples_per_piece=args.samples_per_piece, batch=args.batch, rows=rows,
        original_later_radius_curves_and_speeds_unchanged=True,
        later_background_heights_shift_only_by_first_piece_height=True,
        numerical_newton_or_flow_or_tail_evaluations=0,
        actual_complete_field_and_tail_cap_envelope_not_computed=True,
        exact_first_piece_curvature_certificate=str(args.pulse_budget),
        global_D_or_reach_certificate=False, seconds=time.time()-started)
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(event='background_pulse_envelope_complete', seconds=result['seconds'],
        baseline_length_disagreement=result['baseline_length_disagreement'],
        rows=[{k:r[k] for k in ('pulse','first_height','background_prefix_bridge_height',
            'twice_max_sampled_norm','background_curvature_max_sample','initial_radius_endpoint_error')}
            for r in rows])), flush=True)


if __name__ == '__main__':
    main()
