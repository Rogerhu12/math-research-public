#!/usr/bin/env python3
"""One explicit changed-H solve preserving a genuine accepted tail interior.

Bind the accepted response, actual failed request, and executed source plan
by required caller-supplied SHA-256 values. Require the identical physical/
numerical tail design and native source. Preserve every accepted internal/
deep state and every cut momentum; encode only the new cut Dirichlet values
using the original JavaScript H/radius**4 formula. This is an unaccepted
initializer, never a fabricated response. One original worker owns the full
Newton/Jacobian/audit and strict 2e-9 gate. No automatic retry or H scan.
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
import subprocess
import sys
import time
import numpy as np

HERE = Path(__file__).resolve().parent
TRANSFER = HERE.parent/'resume_transfer'
sys.path.insert(0, str(TRANSFER))
from recovering_tail_client_v2 import (sha, read_gzip, write_new_json,
    exact_equal, check_original_reload_boundary, validate_parameter_io_mapping,
    physical_solver_config)



def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('source-topic', 'source-plan', 'accepted', 'seam-failure',
                'out-prefix', 'sparse-helper'):
        parser.add_argument('--'+key, type=Path, required=True)
    for key in ('accepted-sha', 'failure-sha', 'source-plan-sha'):
        parser.add_argument('--'+key, required=True)
    parser.add_argument('--node-heap', type=int, default=3072)
    args = parser.parse_args()
    ACCEPTED_SHA, FAILED_SHA, SOURCE_PLAN_SHA = args.accepted_sha, args.failure_sha, args.source_plan_sha
    if any(len(v) != 64 or any(c not in '0123456789abcdef' for c in v) for v in (ACCEPTED_SHA, FAILED_SHA, SOURCE_PLAN_SHA)):
        raise ValueError('Explicit lowercase SHA-256 bindings are required')
    topic, prefix = args.source_topic.resolve(), args.out_prefix.resolve()
    prefix.parent.mkdir(parents=True, exist_ok=True)
    files = {name: prefix.with_name(prefix.name+'-'+name+suffix) for name, suffix in
             [('candidate', '.json.gz'), ('entry', '.json'), ('config', '.json'),
              ('worker', '.jsonl'), ('summary', '.json')]}
    if any(p.exists() for p in files.values()):
        raise FileExistsError('Use one new output prefix')
    accepted_path, failed_path = args.accepted.resolve(), args.seam_failure.resolve()
    if (sha(accepted_path) != ACCEPTED_SHA or sha(failed_path) != FAILED_SHA or
            sha(args.source_plan) != SOURCE_PLAN_SHA):
        raise ValueError('Only the explicitly bound actual accepted/failed/source-plan inputs are allowed')
    accepted, failed = read_gzip(accepted_path), read_gzip(failed_path)
    response, failure = accepted['response'], failed['response']
    cfg0 = failed['config']
    J = np.asarray(response['heightJetJacobian'], float)
    if (response.get('converged') is not True or not math.isfinite(response['residual']) or
            not response['residual'] < cfg0['solveTolerance'] or
            J.size != 208 or not np.all(np.isfinite(J)) or response.get('audit') is None):
        raise ValueError('The reference must be an actually accepted complete original response')
    if (not isinstance(failure.get('failed'), str) or
            not failure['failed'].startswith('Error: multiple-shooting line search failed at ') or
            not math.isfinite(failure['lastIteration']['norm']) or
            not failure['lastIteration']['norm'] >= cfg0['solveTolerance']):
        raise ValueError('A complete actual original line-search failure above the original gate is required')
    if not exact_equal(physical_solver_config(accepted['config']), physical_solver_config(cfg0)):
        raise ValueError('The two records do not share their physical/numerical design')
    if not exact_equal(accepted['source_sha256'], failed['source_sha256']):
        raise ValueError('The original execution source changed')
    old, failed_cp = response['checkpoint'], failure['checkpoint']
    old_h, new_h = accepted['request']['height'], failed['request']['height']
    if (not exact_equal(old_h, old['cutHeight']) or
            not exact_equal(new_h, failed_cp['cutHeight']) or
            not exact_equal(failed['request'], dict(height=new_h, jacobian=True, audit=True))):
        raise ValueError('Complete actual request/checkpoint identities changed')
    changed_h = [j for j, (a, b) in enumerate(zip(old_h, new_h)) if not exact_equal(a, b)]
    if len(old_h) != 8 or len(new_h) != 8 or not changed_h or not all(math.isfinite(v) for v in old_h+new_h):
        raise ValueError('One explicitly different finite eight-component actual H is required')
    if (cfg0['modes'] != 8 or cfg0['spacing'] != 3 or cfg0['shootingParts'] != 16 or
            cfg0['steps'] != 16 or cfg0['solveTolerance'] != 2e-9 or cfg0.get('sharedEngines') or
            cfg0.get('designInitialCheckpoint') or cfg0.get('secantCheckpoint')):
        raise ValueError('The original finite solver and all original gates are required')
    validate_parameter_io_mapping(old['parameters'], failed_cp['parameters'], accepted['config'], cfg0)
    if (not exact_equal(old['rawNode'], failed_cp['rawNode']) or len(old['states']) != 1153 or
            any(len(row) != 16 for row in old['states'])):
        raise ValueError('The complete original finite grid is required')
    radius = cfg0['rCut']
    program = """
const fs=require('node:fs'); const d=JSON.parse(fs.readFileSync(0,'utf8'));
const old=d.oldH.map(v=>v/d.radius**4), target=d.newH.map(v=>v/d.radius**4);
if(!old.every((v,j)=>Object.is(v,d.oldCut[j])))throw Error('Original cut encoding differs');
console.log(JSON.stringify({target,old,power:d.radius**4}));
"""
    encoding = json.loads(subprocess.run(['node', '-e', program],
        input=json.dumps(dict(radius=radius, oldH=old_h, newH=new_h,
                              oldCut=old['states'][0][:8])),
        text=True, capture_output=True, check=True).stdout)
    cp = copy.deepcopy(old)
    cp['parameters'] = copy.deepcopy(failed_cp['parameters'])
    cp['cutHeight'] = copy.deepcopy(new_h)
    cp['states'][0][:8] = encoding['target']
    cp['rawStates'] = [copy.deepcopy(cp['states'][i]) for i in cp['rawNode']]
    cp['scope'] = 'UNACCEPTED initializer for the actual new seam H; all accepted interior/deep states and cut momenta are preserved.'
    changed = [(i, j, a, b) for i, (u, v) in enumerate(zip(old['states'], cp['states']))
               for j, (a, b) in enumerate(zip(u, v)) if not exact_equal(a, b)]
    expected_cut = [(0, j) for j, (a, b) in enumerate(zip(encoding['old'], encoding['target'])) if not exact_equal(a, b)]
    if [(i, j) for i, j, _, _ in changed] != expected_cut or any(j not in changed_h for _, j in expected_cut):
        raise ValueError('Only the exactly re-encoded new cut Dirichlet scalars may differ')
    if not exact_equal(cp['states'][1:], old['states'][1:]) or not exact_equal(cp['states'][0][8:], old['states'][0][8:]):
        raise ValueError('An internal/deep state or cut momentum changed')
    candidate = dict(scope=__doc__, candidate_only=True, solver_success=False,
        accepted_reference=dict(path=str(accepted_path), sha256=ACCEPTED_SHA),
        failed_request=dict(path=str(failed_path), sha256=FAILED_SHA),
        request=copy.deepcopy(failed['request']), config=copy.deepcopy(cfg0),
        source_sha256=copy.deepcopy(failed['source_sha256']), checkpoint=cp)
    with files['candidate'].open('xb') as stream:
        stream.write(gzip.compress((json.dumps(candidate, separators=(',', ':'), allow_nan=False)+'\n').encode(), mtime=0))
    sources = dict(json.loads(args.source_plan.read_text())['source_sha256'])
    for name, digest in failed['source_sha256'].items():
        sources[str(topic/'scripts'/name)] = digest
    sparse = args.sparse_helper.resolve()
    for file in (Path(__file__).resolve(), TRANSFER/'recovering_tail_client_v2.py', sparse):
        sources[str(file)] = sha(file)
    for file, digest in sources.items():
        if sha(file) != digest:
            raise ValueError('Execution source changed: '+file)
    os.environ['VISIBLE_FLEX_SPARSE_LINEAR_HELPER'] = str(sparse)
    os.environ['VISIBLE_FLEX_SPARSE_PYTHON'] = sys.executable
    cfg = copy.deepcopy(cfg0)
    cfg['initialCheckpoint'] = str(files['candidate'])
    cfg['traceFile'] = str(files['worker'])
    cfg_changes = sorted(k for k in cfg.keys() | cfg0.keys() if not exact_equal(cfg.get(k), cfg0.get(k)))
    if set(cfg_changes) != {'initialCheckpoint', 'traceFile'}:
        raise ValueError('Only the initializer/trace paths may change')
    write_new_json(files['config'], cfg)
    entry = dict(scope=__doc__, command=[sys.executable, *sys.argv],
        accepted_reference=dict(path=str(accepted_path), sha256=ACCEPTED_SHA),
        failed_request=dict(path=str(failed_path), sha256=FAILED_SHA),
        original_source_plan=dict(path=str(args.source_plan.resolve()), sha256=SOURCE_PLAN_SHA),
        source_sha256=sources, candidate=dict(path=str(files['candidate']), sha256=sha(files['candidate'])),
        configuration=dict(path=str(files['config']), sha256=sha(files['config'])),
        configuration_changed_keys=cfg_changes, original_gate=cfg['solveTolerance'],
        old_height=old_h, new_height=new_h, changed_height_components=changed_h,
        changed_cut_dirichlet=[dict(node=i, component=j, before=a, after=b) for i, j, a, b in changed],
        preserved_internal_and_deep_states=True, preserved_cut_momenta=True,
        javascript_cut_encoding=encoding, candidate_is_not_accepted=True,
        requested_jacobian=True, requested_audit=True, node_heap_resource_only=args.node_heap)
    write_new_json(files['entry'], entry)
    client = topic/'scripts/950f-tail-client-v3.py'
    spec = importlib.util.spec_from_file_location('trace_path_seam_preserved_original_client', client)
    native = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(native)
    tail = None
    began = time.monotonic()
    result = dict(scope=__doc__, entry=dict(path=str(files['entry']), sha256=sha(files['entry'])),
                  solver_success=False, prefix_solver_invoked=False, preliminary_full_replay_invoked=False)
    print(json.dumps(dict(event='seam_preserved_interior_original_native_started', entry=str(files['entry']))), flush=True)
    try:
        tail = native.WeightedTailPort(files['config'], topic/'repro/source-root',
                                      prefix.with_name(prefix.name+'_tail'), node_heap=args.node_heap)
        if not exact_equal(tail.sources, failed['source_sha256']) or not exact_equal(tail.cut['radius'], radius):
            raise ValueError('The original worker source or cut radius changed')
        result['ready_parameter_metadata_transition'] = validate_parameter_io_mapping(cp['parameters'], tail.ready['parameters'], cfg0, cfg)
        result['reload_arithmetic'] = check_original_reload_boundary(files['candidate'], new_h, tail.cut['radius'])
        response = tail.solve(np.asarray(new_h, float), jacobian=True, audit=True)
        J = np.asarray(response['heightJetJacobian'], float)
        if (response.get('converged') is not True or not math.isfinite(response['residual']) or
                not response['residual'] < cfg['solveTolerance'] or J.size != 208 or
                not np.all(np.isfinite(J)) or response.get('audit') is None):
            raise ValueError('The original full gate/Jacobian/audit did not return successfully')
        result.update(solver_success=True, original_residual=response['residual'],
            finite_jacobian_entries=int(J.size), audit_returned=True,
            final_state_nodes=len(response['checkpoint']['states']), native_iterations=len(response['history']),
            original_worker_final_states_equal_candidate=exact_equal(response['checkpoint']['states'], cp['states']))
    except Exception as error:
        result['error'] = repr(error)
    finally:
        if tail is not None:
            try:
                result['native_calls'] = tail.calls
                record = tail.record_prefix.with_name(tail.record_prefix.name+f'_{tail.calls:04d}.json.gz')
                if record.is_file():
                    saved = read_gzip(record)
                    if not exact_equal(saved['request'], failed['request']) or not exact_equal(saved['config'], cfg):
                        raise AssertionError('The original native request/config identity changed')
                    result['native_record'] = dict(path=str(record), sha256=sha(record))
                    if saved['response'].get('lastIteration'):
                        result['last_iteration'] = saved['response']['lastIteration']
            finally:
                tail.close()
            result['worker_returncode'] = tail.proc.poll()
        for file, digest in sources.items():
            if sha(file) != digest:
                raise AssertionError('An executed source changed: '+file)
        result['seconds'] = time.monotonic()-began
        write_new_json(files['summary'], result)
        print(json.dumps(dict(event='seam_preserved_interior_original_native_terminal', **result)), flush=True)
    if not result['solver_success']:
        raise SystemExit(2)


if __name__ == '__main__':
    main()
