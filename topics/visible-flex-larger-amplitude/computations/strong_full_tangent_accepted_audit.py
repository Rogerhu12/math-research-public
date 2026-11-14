#!/usr/bin/env python3
"""Reevaluate an accepted tail at its exact H and save its full tangent.

The original accepted fixed prefix is unchanged. The original complete tail
residual, full Jacobian and requested physical audit run again at the exact
saved H. The new worker only retains already computed full-stage flow
Jacobians. Its exact binary roundtrip and unchanged original predictor are
checked before the sidecar is marked usable. No prefix Newton is run.
"""
from __future__ import annotations

import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
for key in tuple(os.environ):
    if key in ('GH_TOKEN', 'GITHUB_TOKEN', 'GITHUB_PAT') or key.startswith('GIT_CONFIG_'):
        os.environ.pop(key, None)

import argparse
import ast
import hashlib
import json
from pathlib import Path
import sys

import numpy as np
import root_actual_staged_tail as retained

HERE = Path(__file__).resolve().parent
RETAINED_SHA = 'b6f587ac428a477f32e04c13a2686ecb196cbefd342deadc669e13cc988e6753'


def main():
    parser = argparse.ArgumentParser(add_help=False, description=__doc__)
    parser.add_argument('--accepted-reference', type=Path, required=True)
    parser.add_argument('--stage-cache-directory', type=Path, required=True)
    parser.add_argument('--node-young-space', type=int, choices=(1, 2, 4, 8, 16), default=4)
    own, remaining = parser.parse_known_args()

    def arg(name):
        if remaining.count(name) != 1:
            raise ValueError('One explicit '+name+' is required')
        return Path(remaining[remaining.index(name)+1])

    raw_path, warm_path, prefix = arg('--raw'), arg('--warm'), arg('--out-prefix')
    config, topic = arg('--config'), arg('--source-topic')
    heap = int(str(arg('--node-heap')))
    if str(arg('--storage')) != 'frozen' or heap < 1:
        raise ValueError('Original frozen storage and an explicit positive Node heap are required')
    reference = retained.read_json(own.accepted_reference)
    raw, arrays = retained.raw_arrays(raw_path)
    warm = retained.read_json(warm_path)
    ident = raw['identity']
    M = int(ident['modes'])
    if (not reference.get('solver_success') or reference.get('audit_pending', True)
            or not reference['config'].get('actual_nonlinear_tail')
            or not raw.get('solver_success') or raw.get('status') != 0 or not ident['fixed']
            or reference['raw_collocation_checkpoint']['sha256'] != retained.sha(raw_path)
            or arrays['p'].shape != (M,) or arrays['y'].shape[0] != 3*M+1
            or float(np.max(arrays['rms'])) > ident['tol']):
        raise ValueError('A completely accepted fixed actual reference/raw pair is required')
    for a, b in (('gauge', 'gauge_amplitude'), ('profile', 'frozen_profile'),
                 ('physical_tail_parameters', 'physical_tail_parameters'),
                 ('physical_tail_cut', 'physical_tail_cut')):
        if ident[a] != reference[b]:
            raise ValueError('Accepted physical identity differs: '+a)
    height = -float(ident['gauge'])*arrays['y'][2*M+1:, -1]
    request, response = warm['request'], warm['response']
    if (not request.get('jacobian') or not request.get('audit')
            or not response.get('converged') or response.get('audit') is None
            or response['residual'] > warm['config']['solveTolerance']
            or warm['source_sha256'] != reference['actual_tail']['source_sha256']
            or np.asarray(request['height'], dtype=np.float64).tobytes() != height.tobytes()
            or np.asarray(response['checkpoint']['cutHeight'], dtype=np.float64).tobytes() != height.tobytes()
            or len(response['heightJetJacobian']) != (3*M+2)*M
            or not np.isfinite(response['heightJetJacobian']).all()):
        raise ValueError('The exact accepted full-H Jacobian/audit packet is required')
    if retained.equation_config(retained.read_json(config)) != retained.equation_config(warm['config']):
        raise ValueError('The original complete tail problem differs')
    for name, expected in warm['source_sha256'].items():
        candidate = HERE/name
        if not candidate.is_file():
            candidate = topic/'scripts'/name
        if not candidate.is_file() or retained.sha(candidate) != expected:
            raise ValueError('An original accepted-tail source differs: '+name)
    source_path = Path(retained.__file__)
    source = source_path.read_text()
    if retained.sha(source_path) != RETAINED_SHA:
        raise ValueError('Original staged audit source differs')
    before = ("    if (raw['solver_success'] or raw['status'] != 0 or\n"
              "            not raw['provenance'].get('actual_nonlinear_coupling_pending') or\n"
              "            not raw['provenance'].get('affine_inner_success')):\n"
              "        raise ValueError('Expected a successful affine inner state awaiting true DN')")
    after = ("    if not raw['solver_success'] or raw['status'] != 0:\n"
             "        raise ValueError('Expected the original formally accepted fixed prefix')")
    edits = [
        (before, after),
        ("    plan = dict(scope=__doc__, status='prepared', raw=str(args.raw),",
         "    plan = dict(scope=__doc__, full_flow_tangent_storage=FULL_TANGENT_WRAPPER,\n"
         "                status='prepared', raw=str(args.raw),"),
    ]
    for a, b in edits:
        if source.count(a) != 1:
            raise ValueError('Accepted-tail storage runner anchor is not unique')
        source = source.replace(a, b, 1)
    doc_first = source.index('"""')
    doc_last = source.index('"""', doc_first+3)+3
    source = source[:doc_first]+repr(__doc__)+source[doc_last:]
    ast.parse(source, filename='<accepted-full-tangent-original-audit>')
    record = dict(
        scope=__doc__, wrapper_sha256=retained.sha(__file__), retained_source_sha256=RETAINED_SHA,
        transformed_source_sha256=hashlib.sha256(source.encode()).hexdigest(),
        replacements=[dict(before=a, after=b, count=1) for a, b in edits],
        accepted_reference=dict(file=str(own.accepted_reference), sha256=retained.sha(own.accepted_reference)),
        accepted_raw=dict(file=str(raw_path), sha256=retained.sha(raw_path)),
        accepted_tail=dict(file=str(warm_path), sha256=retained.sha(warm_path)),
        full_H_bitwise_equal=True, modes=M, nodes=len(arrays['x']),
        original_complete_problem_unchanged=True, original_tolerance=warm['config']['solveTolerance'],
        original_RMS_max=float(np.max(arrays['rms'])), prefix_Newton_calls=0,
        stage_cache_directory=str(own.stage_cache_directory.resolve()),
        node_old_heap_MiB=heap, node_young_semi_space_MiB=own.node_young_space,
    )
    prefix.parent.mkdir(parents=True, exist_ok=True)
    guard_file = prefix.with_name(prefix.name+'-accepted-storage-guards.json')
    with guard_file.open('x') as stream:
        json.dump(record, stream, indent=2)
        stream.write('\n')
    import tail_frozen_client
    import strong_full_tangent_tail_client as client
    from strong_full_tangent_resource_guard import resource_port_class
    old_client = tail_frozen_client.WeightedTailPort
    tail_frozen_client.WeightedTailPort = resource_port_class(client.WeightedTailPort, heap, own.node_young_space)
    updates = {
        'VISIBLE_FLEX_SOURCE_TOPIC': str(topic.resolve()),
        'VISIBLE_FLEX_EXACT_STAGE_CACHE': str(own.stage_cache_directory.resolve()),
        'VISIBLE_FLEX_EXACT_STAGE_SEED_PREFIX': str(prefix.resolve())+'-exact-initial',
    }
    old_environment = {key: os.environ.get(key) for key in updates}
    old_argv = sys.argv
    namespace = dict(__file__=str(source_path), __name__='full_tangent_accepted_original_audit',
                     FULL_TANGENT_WRAPPER=record)
    try:
        os.environ.update(updates)
        sys.argv = [old_argv[0], *remaining]
        exec(compile(source, '<accepted-full-tangent-original-audit>', 'exec'), namespace)
        namespace['main']()
        if '--prepare-only' not in remaining:
            packet = prefix.with_name(prefix.name+'-response_0001.json.gz')
            saved = retained.read_json(packet)['response']
            snapshot = saved.get('fullFlowTangentSnapshot')
            if (not snapshot or not snapshot.get('roundtrip', {}).get('allBaseAndFlowValuesBitwiseEqual')
                    or not snapshot['roundtrip'].get('originalFactoryPredictorCheck', {}).get('allStateValuesBitwiseEqual')):
                raise RuntimeError('The true tail response is retained, but usable full tangent storage did not finish: '
                                   +repr(saved.get('fullFlowTangentStorageError')))
            result = dict(record, status='complete', tail_response=str(packet), tail_response_sha256=retained.sha(packet),
                          snapshot=snapshot, old_prefix_unchanged=True, no_new_prefix_accepted=True)
            with prefix.with_name(prefix.name+'-storage-summary.json').open('x') as stream:
                json.dump(result, stream, indent=2)
                stream.write('\n')
            print(json.dumps(dict(event='accepted_full_tangent_storage_complete',
                tail_residual=saved['residual'], snapshot=snapshot, prefix_Newton_calls=0)), flush=True)
    finally:
        tail_frozen_client.WeightedTailPort = old_client
        sys.argv = old_argv
        for key, value in old_environment.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value


if __name__ == '__main__':
    main()
