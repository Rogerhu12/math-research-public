#!/usr/bin/env python3
"""One original full DN with explicit native-provider marker handling (v2).

Retain every scalar of a real failed same-H checkpoint as the unaccepted
initializer. Change only initializer/trace I/O paths. The original worker's
first required full-Jacobian evaluation is the first whole native batch;
there is no separate full-state evaluation, local candidate scan or retry.
All original residual, domain, line-search, stopping, cut and audit gates
remain. Native shooting state/literal Jacobian arithmetic is a declared new
provider, never labeled byte-identical to the historical V8 calculation.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import copy
import gzip
import importlib.util
import json
import math
from pathlib import Path
import sys
import time
import numpy as np

HERE = Path(__file__).resolve().parent
TRANSFER = HERE.parent/'resume_transfer'
sys.path.insert(0, str(TRANSFER))
from recovering_tail_client_v2 import (sha, read_gzip, write_new_json, exact_equal,
    check_original_reload_boundary, validate_parameter_io_mapping)
from m3_literal_tail_provider_v2 import (bind_provider, runtime_environment,
    provider_parameter_io_mapping, check_native_response_metadata)


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('failed-tail', 'source-plan', 'provider-manifest', 'out-prefix', 'sparse-helper'):
        parser.add_argument('--'+name, type=Path, required=True)
    for name in ('failure-sha', 'source-plan-sha', 'provider-manifest-sha'):
        parser.add_argument('--'+name, required=True)
    parser.add_argument('--node-heap', type=int, default=3072)
    args = parser.parse_args()
    failed_path, plan_path = args.failed_tail.resolve(), args.source_plan.resolve()
    prefix = args.out_prefix.resolve()
    prefix.parent.mkdir(parents=True, exist_ok=True)
    files = {name: prefix.with_name(prefix.name+'-'+name+suffix) for name, suffix in
             [('candidate', '.json.gz'), ('entry', '.json'), ('config', '.json'),
              ('worker', '.jsonl'), ('summary', '.json')]}
    if any(path.exists() for path in files.values()):
        raise FileExistsError('Use a fresh explicit output prefix')
    if sha(failed_path) != args.failure_sha or sha(plan_path) != args.source_plan_sha:
        raise ValueError('The real failed state or original runtime plan changed')
    old = read_gzip(failed_path)
    plan = json.loads(plan_path.read_text())
    response, cfg0, request = old['response'], old['config'], old['request']
    if (old['source_sha256'] != plan['native_tail_source_sha256'] or
            not isinstance(response.get('failed'), str) or
            not response['failed'].startswith('Error: multiple-shooting line search failed at ') or
            not math.isfinite(response['lastIteration']['norm']) or
            not response['lastIteration']['norm'] >= cfg0['solveTolerance'] or
            request.get('jacobian') is not True or request.get('audit') is not True):
        raise ValueError('A complete real failed original same-H request is required')
    cp = response['checkpoint']
    H = request['height']
    if (cp['parameters']['projectionFloor'] != .05 or len(H) != 8 or
            not exact_equal(H, cp['cutHeight']) or len(cp['states']) != 1153 or
            any(len(row) != 16 for row in cp['states']) or
            not all(math.isfinite(v) for row in cp['states'] for v in row) or
            not exact_equal(cp['rawStates'], [cp['states'][i] for i in cp['rawNode']])):
        raise ValueError('The complete original .05-floor checkpoint is required')
    provider = bind_provider(args.provider_manifest, args.provider_manifest_sha,
                             old['source_sha256'], cfg0)
    candidate = dict(scope=__doc__, candidate_only=True, solver_success=False,
        historical_failed_record=ref(failed_path), request=copy.deepcopy(request),
        config=copy.deepcopy(cfg0), source_sha256=copy.deepcopy(old['source_sha256']),
        checkpoint=copy.deepcopy(cp))
    with files['candidate'].open('xb') as stream:
        stream.write(gzip.compress((json.dumps(candidate, separators=(',', ':'), allow_nan=False)+'\n').encode(), mtime=0))
    # No claimed new candidate correction: every original checkpoint field,
    # including its material/physical metadata, remains literal.
    if not exact_equal(read_gzip(files['candidate'])['checkpoint'], cp):
        raise AssertionError('Serializing the initializer changed the original checkpoint')
    cfg = copy.deepcopy(cfg0)
    cfg['initialCheckpoint'] = str(files['candidate'])
    cfg['traceFile'] = str(files['worker'])
    changed = sorted(k for k in cfg.keys() | cfg0.keys() if not exact_equal(cfg.get(k), cfg0.get(k)))
    if set(changed) != {'initialCheckpoint', 'traceFile'}:
        raise ValueError('Only initializer/trace I/O may change')
    write_new_json(files['config'], cfg)
    sources = {**plan['source_sha256'], **provider['source_sha256']}
    for file in (Path(__file__).resolve(), HERE/'m3_literal_tail_provider_v2.py',
                 TRANSFER/'recovering_tail_client_v2.py', args.sparse_helper.resolve()):
        sources[str(file)] = sha(file)
    for path, digest in sources.items():
        if sha(path) != digest:
            raise ValueError('An execution input/source changed: '+path)
    environment = runtime_environment(provider, prefix.parent)
    environment.update(VISIBLE_FLEX_SPARSE_LINEAR_HELPER=str(args.sparse_helper.resolve()),
                       VISIBLE_FLEX_SPARSE_PYTHON=sys.executable)
    os.environ.update(environment)
    reload_check = check_original_reload_boundary(files['candidate'], H, cfg['rCut'])
    entry = dict(scope=__doc__, command=[sys.executable, *sys.argv],
        historical_failed_record=ref(failed_path), original_source_plan=ref(plan_path),
        provider_manifest=provider['manifest'], active_tail_provider=provider,
        source_sha256=sources, environment=environment,
        provider_client_source_root=provider['source_root'],
        candidate=ref(files['candidate']), candidate_checkpoint_equal_original=True,
        changed_state_coordinates=[], candidate_is_not_accepted=True,
        configuration=ref(files['config']), configuration_changed_keys=changed,
        original_request=copy.deepcopy(request), original_failed_norm=response['lastIteration']['norm'],
        original_gate=cfg['solveTolerance'], original_projection_floor=.05,
        reload_arithmetic=reload_check, preliminary_full_replay_invoked=False,
        prefix_solver_invoked=False, node_heap_resource_only=args.node_heap)
    write_new_json(files['entry'], entry)
    spec = importlib.util.spec_from_file_location('bound_m3_literal_native_client', provider['client']['path'])
    client = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(client)
    tail = None
    started = time.monotonic()
    result = dict(scope=__doc__, entry=ref(files['entry']), solver_success=False,
        provider_manifest=provider['manifest'], prefix_solver_invoked=False,
        preliminary_full_replay_invoked=False)
    print(json.dumps(dict(event='bound_native_original_DN_started', entry=ref(files['entry']))), flush=True)
    try:
        tail = client.WeightedTailPort(files['config'], Path(provider['source_root']),
            prefix.with_name(prefix.name+'_tail'), node_heap=args.node_heap)
        if tail.sources != provider['native_tail_source_sha256'] or tail.cut['radius'] != cfg['rCut']:
            raise ValueError('The actual worker source/cut changed')
        result['ready_parameter_metadata_transition'] = provider_parameter_io_mapping(
            cp['parameters'], tail.ready['parameters'], cfg0, cfg, provider)
        if tail.ready['parameters']['projectionFloor'] != .05:
            raise ValueError('The actual original .05 domain gate changed')
        response = tail.solve(np.asarray(H, float), jacobian=True, audit=True)
        check_native_response_metadata(dict(response=response), provider)
        J = np.asarray(response['heightJetJacobian'], float)
        if (response.get('converged') is not True or not math.isfinite(response['residual']) or
                not response['residual'] < 2e-9 or J.size != 208 or
                not np.all(np.isfinite(J)) or response.get('audit') is None):
            raise ValueError('The original full DN/Jacobian/audit gate did not return successfully')
        result.update(solver_success=True, original_residual=response['residual'],
            finite_jacobian_entries=int(J.size), audit_returned=True,
            final_state_nodes=len(response['checkpoint']['states']), native_iterations=len(response['history']),
            final_states_equal_original_failed=exact_equal(response['checkpoint']['states'], cp['states']))
    except Exception as error:
        result['error'] = repr(error)
    finally:
        if tail is not None:
            try:
                result['native_calls'] = tail.calls
                record = tail.record_prefix.with_name(tail.record_prefix.name+f'_{tail.calls:04d}.json.gz')
                if record.is_file():
                    saved = read_gzip(record)
                    if (not exact_equal(saved['request'], request) or not exact_equal(saved['config'], cfg) or
                            saved['source_sha256'] != provider['native_tail_source_sha256']):
                        raise AssertionError('The actual request/config/provider identity changed')
                    result['native_record'] = ref(record)
                    if saved['response'].get('lastIteration'):
                        result['last_iteration'] = saved['response']['lastIteration']
            finally:
                tail.close()
            result['worker_returncode'] = tail.proc.poll()
        for path, digest in sources.items():
            if sha(path) != digest:
                raise AssertionError('An executed source changed: '+path)
        result['seconds'] = time.monotonic()-started
        write_new_json(files['summary'], result)
        print(json.dumps(dict(event='bound_native_original_DN_terminal', **result)), flush=True)
    if not result['solver_success']:
        raise SystemExit(2)


if __name__ == '__main__':
    main()
