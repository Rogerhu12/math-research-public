#!/usr/bin/env python3
"""Static/hash review only; never import the auditor, its positive data, or an engine."""
import argparse
import ast
import gzip
import hashlib
import json
from pathlib import Path

T = Path(__file__).resolve().parent.parent
N, S, R = T/'notes', T/'scripts', T.parent.parent
P = '2026-11-09-db6f-'
STEM = P+'prefix-flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-matched-cut-s63of64-01'
V1, V2 = S/'db6f-prefix-audit-matched-cut-closed.py', S/'db6f-prefix-audit-matched-cut-closed-v2.py'
PINS = {
    V1: 'af5349d6ea2d7f5f3331aee245bd04b605e0cf6d006d2fb25979fd2adf312b31',
    V2: '00c048161cde786c830199d092b76e4a6027e081eab180e2fc449133515050a7',
    N/(STEM+'-input-bindings.json'): '5b184918f4c5a86f10189c5433cd447af4a822856a2fe569df4439e03efdeb21',
    N/(P+'prefix-matched-cut-closed-auditor-method.md'): '58b6bb3265fdec134f2aadee204d7de16adb0ee52fef398cb11fa2911c3fbd71',
    N/(P+'prefix-matched-cut-closed-auditor-v2.md'): '994c6864ca88642a0f2159f7883765f985d7f63f15e4da5db7caae70ebf3e988',
    N/(P+'prefix-matched-cut-closed-auditor-sources.json'): 'b002023d368e877f179056bb94e2ad52ab954e2adf844539111e47ec2ca45446',
    N/(P+'prefix-matched-cut-closed-auditor-v2-sources.json'): '35efa713b19ae4a24ccec22584a9f2c9b0105fc02bef7e8c6af34a0ae1de6c95',
}


def record(path):
    path = Path(path).resolve()
    return {'path': str(path), 'bytes': path.stat().st_size,
            'sha256': hashlib.sha256(path.read_bytes()).hexdigest()}


def read(path):
    path = Path(path)
    data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == '.gz' else data)


def demand(value, message):
    if not value:
        raise AssertionError(message)


def source_part(path, first, last=None):
    text = path.read_text()
    start = text.index(first)
    stop = len(text) if last is None else text.index(last, start+len(first))
    return text[start:stop]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    demand(not args.out.exists(), 'Refuse overwrite')
    bound = {}
    for path, expected in PINS.items():
        info = record(path)
        demand(info['sha256'] == expected, 'Frozen pin '+str(path))
        bound[info['path']] = info
    launch = read(N/(STEM+'-input-bindings.json'))
    demand(len(launch['bound_files']) == 121, 'Original 121 bindings')
    lists = [launch['bound_files'],
             read(N/(P+'prefix-matched-cut-closed-auditor-sources.json'))['files'],
             read(N/(P+'prefix-matched-cut-closed-auditor-v2-sources.json'))['files']]
    for rows in lists:
        for row in rows:
            path = Path(row['path'])
            if not path.is_absolute():
                path = R/path
            info = record(path)
            demand(info['sha256'] == row['sha256'], 'Source SHA '+str(path))
            if 'bytes' in row:
                demand(info['bytes'] == row['bytes'], 'Source bytes '+str(path))
            bound[info['path']] = info
    a, b = V1.read_text(), V2.read_text()
    before = "vector(cp['central_correction_scales'], M)"
    after = "vector(cp['central_correction_scales'], M-1)"
    demand(a.count(before) == 1 and a.replace(before, after) == b, 'Single expression repair')
    tree = ast.parse(b)
    modules = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            modules.extend(x.name for x in node.names)
        elif isinstance(node, ast.ImportFrom):
            modules.append(node.module)
    demand(set(modules) == {'argparse', 'gzip', 'hashlib', 'io', 'json', 'math', 're', 'pathlib',
                            'numpy', 'scipy.interpolate'}, 'Only stdlib and stored-polynomial dependencies')
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            demand(node.func.attr not in {'write_bytes', 'write_text', 'rename', 'unlink', 'replace'},
                   'Unexpected file mutation')
    functions = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
    root = ast.get_source_segment(b, functions['root_observation'])
    demand("obs['session_id'] == 5817" in root and "obs.get('observer') == '/root'" in root,
           'Real root session identity')
    demand("obs.get('status') == 'observed-process-completed'" in root and
           "obs['actual_exit_code'] != 0" in root and "obs.get('tool_receipt')" in root,
           'Root tool observation, not guard child')
    run = ast.get_source_segment(b, functions['run'])
    demand("if args.mode == 'first':" in run and "process_exit_required=False" in run,
           'First response scope')
    final = ast.get_source_segment(b, functions['final_run'])
    demand(final.index('root_observation(') < final.index('repro_path ='), 'Final must obtain real observation first')

    names = ['db6f-prefix-tail-trial-client.py', 'db6f-prefix-tail-trial-worker.mjs',
             'db6f-prefix-tail-trial-core.mjs', 'db6f-prefix-tail-trial-split.mjs',
             '950f-tail-subdivision.mjs', '950f-tail-warm-remesh.mjs',
             'closing_weighted_tail.mjs', 'closing_recalibrated_tail.mjs']
    launch_paths = {str(Path(x['path']).resolve()): x for x in launch['bound_files']}
    actual_sources = []
    for name in names:
        path = S/name
        info = record(path)
        demand(str(path) in launch_paths and info['sha256'] == launch_paths[str(path)]['sha256'],
               'Exact sibling path '+name)
        actual_sources.append(info)
    client = (S/names[0]).read_text()
    demand("worker.with_name(name).read_bytes()" in client and "worker=Path(__file__).with_name('db6f-prefix-tail-trial-worker.mjs')" in client,
           'Client packet source identities are these actual siblings')
    recalc = (S/'closing_recalibrated_tail.mjs').read_text()
    weighted = (S/'closing_weighted_tail.mjs').read_text()
    core = (S/'db6f-prefix-tail-trial-core.mjs').read_text()
    worker = (S/'db6f-prefix-tail-trial-worker.mjs').read_text()
    demand('rejoinIndexOffset:4,...input};' in recalc and 'parameters:{...p,' in recalc,
           'Recalibration preserves input keys')
    demand('parameters:{...tail.parameters,' in weighted and 'parameters:{...physical.parameters,' in core,
           'Weighted and shooting stages preserve parameters')
    demand('checkpoint={parameters:sol.parameters,states:sol.states' in worker,
           'Successful CP uses actual returned parameters')
    hist = source_part(S/'db6f-prefix-tail-trial-core.mjs', 'function solve(target,opts={})', '\n return {solve,initial,')
    demand(hist.index('if(ev.norm<') < hist.index('history.at(-1).chartCondition='),
           'Converged base row has no mandatory chart condition')
    demand('history.at(-1).step=lambda;accepted=true;' in hist,
           'Step is supplied only by accepted line search')
    demand('if(!last||last.norm>=(opts.tolerance??1e-10)){last=evaluate(states,target,true,scales);}' in hist,
           'Final residual can differ from last history base point')
    outer = source_part(S/'db6f-prefix-coupled.py', 'def solve_with_actual_tail(', '\ndef main():')
    failblock = outer[outer.index('if not sol.success:'):outer.index('candidate=')]
    demand('inner_success=False' in failblock and 'return sol,history' in failblock,
           'No later successful outer path after an unsuccessful inner BVP')
    demand("if defect<=a.bc_tol:return sol,history" in outer,
           'Original actual BC threshold')
    warped = (S/'950f-prefix-warped-bvp.py').read_text()
    demand('self.pscale=np.maximum(q**np.arange(2,M+1),1e-9)' in warped,
           'Original correction count is M-1')
    frozen_warm = read(N/(P+'prefix-matched-cut-s63of64-warm-01.json.gz'))
    demand(len(frozen_warm['parameters']) == 15 and len(frozen_warm['central_correction_scales']) == 14,
           'Real immutable warm metadata agrees with source')

    out = {'status': 'PASS-static-v2-source-identity-and-original-schema-review',
           'reviewer': '/root/tail_theory', 'checker': record(__file__),
           'scope': 'No auditor positive branch, current DN response, active trace, future closed data, or synthetic success fixture was read or executed.',
           'v1': record(V1), 'v2': record(V2), 'one_expression_diff': True,
           'bound_input_count': 121, 'source_ledger_counts': [len(x) for x in lists[1:]],
           'distinct_closed_files_rehashed': len(bound),
           'source_files': list(sorted(bound.values(), key=lambda x: x['path'])),
           'eight_source_paths': actual_sources,
           'original_source_conclusions': {
               'five_IO_keys_preserved_by_input_and_parameter_spreads': True,
               'normal_checkpoint_parameters_from_actual_solve': True,
               'optional_history_chart_and_step_allow_absence': True,
               'last_history_and_final_norm_not_forced_equal': True,
               'all_successful_outer_inner_flags_true_follows_from_early_return': True,
               'correction_scale_count_is_14_while_parameter_count_is_15': True,
               'first_mode_has_no_exit_claim': True,
               'final_mode_requires_root_5817_tool_observation': True,
               'no_new_second_jet_or_node_worker_exit_threshold': True},
           'positive_branches_executed': 0, 'synthetic_positive_fixtures': 0,
           'solvers_or_RK_or_flow_calls': 0}
    with args.out.open('x') as handle:
        json.dump(out, handle, ensure_ascii=False, indent=2)
        handle.write('\n')
    print(json.dumps({'status': out['status'], 'distinct_closed_files': len(bound),
                      'output_sha256': record(args.out)['sha256']}))


if __name__ == '__main__':
    main()
