#!/usr/bin/env python3
"""Read saved prefix cut traces using the actual coupled-tail sign convention.

This is a read-only comparison of saved finite objects. It neither starts a
tail worker nor creates a new nonlinear solution or transformed warm state.
The coupled runner's actual tail_height function is extracted from its AST
and evaluated with the saved endpoint and the real provider bridge.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import ast
import gzip
import hashlib
import importlib.util
import io
import json
from pathlib import Path
from types import SimpleNamespace

import numpy as np

HERE = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read_json(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def source_function(path, name):
    raw = Path(path).read_bytes()
    tree = ast.parse(raw.decode(), filename=str(path))
    matches = [node for node in ast.walk(tree)
               if isinstance(node, ast.FunctionDef) and node.name == name]
    if len(matches) != 1:
        raise ValueError(f'Expected one actual {name} function')
    node = matches[0]
    module = ast.Module(body=[node], type_ignores=[])
    namespace = {'np': np}
    exec(compile(ast.fix_missing_locations(module), str(path), 'exec'), namespace)
    return namespace[name], ast.get_source_segment(raw.decode(), node), hashlib.sha256(raw).hexdigest()


def prefix_endpoint(path):
    data = read_json(path)
    if not data['solver_success']:
        raise ValueError('Prefix packet is not a successful finite prefix')
    M = int(data['modes'])
    n = 3*M+1
    mesh = np.asarray(data['mesh'], dtype=float)
    h = mesh[-1]-mesh[-2]
    end = np.empty(n, dtype=float)
    assigned = np.zeros(n, dtype=bool)
    hashes = {}
    for record in data['pp_coefficient_chunks']:
        file = Path(path).parent/record['file']
        raw = file.read_bytes()
        sha = hashlib.sha256(raw).hexdigest()
        if sha != record['sha256']:
            raise ValueError('Saved coefficient hash mismatch: '+str(file))
        c = np.load(io.BytesIO(gzip.decompress(raw)), allow_pickle=False)
        first, last = record['state_first'], record['state_last_exclusive']
        if c.shape != (6, len(mesh)-1, last-first):
            raise ValueError('Unexpected physical quintic coefficient layout')
        value = c[0, -1].copy()
        for row in c[1:, -1]:
            value = h*value+row
        if np.any(assigned[first:last]):
            raise ValueError('Overlapping coefficient chunks')
        end[first:last] = value
        assigned[first:last] = True
        hashes[str(file)] = sha
    if not np.all(assigned):
        raise ValueError('Incomplete physical state coefficient chunks')
    return data, end, hashes


def compare(target, reference):
    target = np.asarray(target, dtype=float)
    reference = np.asarray(reference, dtype=float)
    count = max(len(target), len(reference))
    H = np.pad(target, (0, count-len(target)))
    W = np.pad(reference, (0, count-len(reference)))
    ratio = float(H[0]/W[0])
    difference = H-ratio*W
    return dict(first_mode_matched_uniform_factor=ratio,
                source_amplitude_warm_ratio_is_eligible=bool(.25 < ratio < 4),
                target_length=len(target), reference_length=len(reference),
                vector_comparison_scope='Zero padding is only the source loader warm embedding convention, not a claim about uncomputed solution modes.',
                physical_frequencies=(2*np.arange(1, count+1)).tolist(),
                target_height=H.tolist(), reference_height=W.tolist(),
                uniform_scaled_reference=(ratio*W).tolist(),
                remaining_boundary_height_correction=difference.tolist(),
                correction_linf=float(np.max(abs(difference))),
                correction_l1=float(np.sum(abs(difference))),
                pi_over_2_rotated_reference_first_mode_factor=-ratio,
                current_first_mode_sign_matches=bool(ratio > 0),
                note='The actual tail request already includes sigma=-1 reflection. A further pi/2 phase would reverse H2 and fail the positive amplitude-warm ratio test. The full higher-mode correction and true nonlinear tail solve remain required.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-topic', type=Path, required=True)
    parser.add_argument('--prefix', type=Path, action='append', required=True)
    parser.add_argument('--warm', type=Path, required=True)
    parser.add_argument('--ray-response', type=Path)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    source_sha = digest(__file__)
    runner = HERE/'root_actual_neck_bvp.py'
    actual_tail_height, actual_source, actual_sha = source_function(runner, 'tail_height')
    provider_path = HERE/'alternative-neck-provider.py'
    provider_sha = digest(provider_path)
    spec = importlib.util.spec_from_file_location('strong_tail_trace_provider', provider_path)
    provider = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(provider)
    warm = read_json(args.warm)
    checkpoint = warm['response']['checkpoint']
    W = np.asarray(warm['request']['height'], dtype=float)
    if not np.array_equal(W, np.asarray(checkpoint['cutHeight'], dtype=float)):
        raise ValueError('Warm request and recorded cutHeight differ')
    if not warm['response']['converged']:
        raise ValueError('Requested old warm record is not a converged finite response')
    scripts = args.source_topic/'scripts'
    old_client = scripts/'db6f-prefix-tail-trial-client.py'
    worker = scripts/'78718-prefix-tail-tangent-fourier-worker.mjs'
    ray = read_json(args.ray_response) if args.ray_response else None
    rows = []
    for file in args.prefix:
        saved, endpoint, coefficient_hashes = prefix_endpoint(file)
        M = int(saved['modes'])
        q = float(saved['gauge_amplitude'])
        bridge = provider.NeckTerminalBridge(saved['physical_tail_cut'])
        obj = SimpleNamespace(bridge=bridge, q=q, iz=2*M+1)
        H = actual_tail_height(obj, endpoint)
        physical_height = q*endpoint[obj.iz:]
        if bridge.sigma != -1 or not np.array_equal(H, -physical_height):
            raise ValueError('Unexpected coupled-tail sign convention')
        physical_mismatches = {}
        for key, value in saved['physical_tail_parameters'].items():
            if checkpoint['parameters'].get(key) != value:
                physical_mismatches[key] = dict(prefix=value, warm=checkpoint['parameters'].get(key))
        row = dict(prefix=str(file), prefix_sha256=digest(file),
                   modes=M, gauge_amplitude=q, bridge_sigma=float(bridge.sigma),
                   coefficient_sha256=coefficient_hashes,
                   prefix_nonmean_height=physical_height.tolist(),
                   actual_tail_request_height=H.tolist(),
                   actual_height_equals_negative_prefix_height=True,
                   physical_tail_parameter_mismatches=physical_mismatches,
                   old_q040_warm_comparison=compare(H, W))
        if ray is not None:
            row['old_q070_ray_comparison'] = compare(H, ray['request']['height'])
        rows.append(row)
    if not all(row['old_q040_warm_comparison']['current_first_mode_sign_matches']
               and row.get('old_q070_ray_comparison', {}).get('current_first_mode_sign_matches', True)
               for row in rows):
        raise ValueError('Unexpected first-mode sign difference: inspect instead of applying the recorded conclusion')
    result = dict(scope=__doc__, nonlinear_solve_run=False,
                  transformed_warm_created=False,
                  convention=dict(actual_tail_height_source=actual_source,
                                  prefix_relation='Z_prefix = sigma*Z_tail + constant; sigma=-1.',
                                  client_relation='WeightedTailPort.solve converts height to float and sends the complete vector without sign or phase changes.',
                                  phase_conclusion='No pi/2 transformation is indicated. Earlier comparison using q*y instead of sigma*q*y omitted the existing reflection and is withdrawn.'),
                  warm=dict(file=str(args.warm), sha256=digest(args.warm),
                            modes=int(checkpoint['parameters']['modes']),
                            request_height=W.tolist(),
                            request_equals_checkpoint_cutHeight=True,
                            finite_response_converged=True,
                            finite_response_residual=warm['response']['residual'],
                            states=len(checkpoint['states']), state_width=len(checkpoint['states'][0])),
                  sources={str(Path(__file__)):source_sha, str(runner):actual_sha,
                           str(provider_path):provider_sha,
                           str(old_client):digest(old_client), str(worker):digest(worker)},
                  prefixes=rows)
    if args.ray_response:
        result['ray_response'] = dict(file=str(args.ray_response), sha256=digest(args.ray_response))
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(out=str(args.out), rows=[dict(prefix=r['prefix'],
        tail_first_three=r['actual_tail_request_height'][:3],
        warm_factor=r['old_q040_warm_comparison']['first_mode_matched_uniform_factor'],
        warm_correction_linf=r['old_q040_warm_comparison']['correction_linf'],
        physical_tail_parameter_mismatches=r['physical_tail_parameter_mismatches']) for r in rows]), indent=2))


if __name__ == '__main__':
    main()
