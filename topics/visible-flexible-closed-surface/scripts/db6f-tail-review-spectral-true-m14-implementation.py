#!/usr/bin/env python3
"""Independent metadata/AST and historical-data review; no candidate solve.

This checker never calls the new selector main, a candidate constructor,
restart, flow, Newton install, weighted solver factory, BVP, DN, or RHS.
The only numeric operation is PPoly evaluation of already-closed old M14
coefficients through the new read-only auditor. No future success fixture
is constructed. New artifacts are the small review report only.
"""
import argparse
import ast
import copy
import gzip
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
NOTES = HERE.parent / 'notes'
PREFIX = '2026-11-09-db6f-'
LAUNCH = NOTES / (PREFIX + 'prefix-spectral-true-m14q512-01-launch.json')
FROZEN = {
    'db6f-prefix-spectral-true-m14.py': 'd0eba3d875f5691c939825ee4824e0bf009b840e5c60f21ffa2138b3f228df99',
    'db6f-prefix-prepare-spectral-true-m14.py': 'de3ce21bdc49880a7057a7e3fdd1737a18cc23f5b5a5ffce44b4b881fab5d7ff',
    'db6f-prefix-audit-spectral-true-m14.py': '1aa5e53985b5574dee68a032aa84ac47aa43e9aa8bd185b4af8650b618dcf0fa',
}
IO = {'initialCheckpoint', 'traceFile', 'iterationCheckpointFile',
      'trialDiagnosticFile', 'trialStatePrefix'}


def demand(value, message):
    if not value:
        raise AssertionError(message)


def canon(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)


def load(path):
    path = Path(path)
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw)


def ident(path):
    path = Path(path).resolve()
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        while block := stream.read(262144):
            digest.update(block)
    return {'path': str(path), 'bytes': path.stat().st_size, 'sha256': digest.hexdigest()}


def callback_from_ast(path, name):
    path = Path(path)
    text = path.read_text()
    found = []
    stack = [(ast.parse(text), '')]
    while stack:
        node, prefix = stack.pop()
        for child in getattr(node, 'body', []):
            if isinstance(child, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
                qualname = prefix + child.name
                if qualname == name:
                    found.append(child)
                stack.append((child, qualname + ('.' if isinstance(child, ast.ClassDef) else '.<locals>.')))
    demand(len(found) == 1 and isinstance(found[0], ast.FunctionDef), 'Callback not uniquely found: ' + name)
    node = found[0]
    demand(not node.decorator_list, 'Decorated callback requires a different review')
    segment = '\n'.join(text.splitlines()[node.lineno - 1:node.end_lineno]).rstrip()
    return {'file': ident(path), 'qualname': name, 'first_line': node.lineno,
            'source_sha256_rstrip': hashlib.sha256(segment.encode()).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    demand(not args.out.exists(), 'Review refuses output overwrite')
    rows = {}
    def bind(path):
        row = ident(path)
        prior = rows.get(row['path'])
        demand(prior is None or prior == row, 'Input changed during review')
        rows[row['path']] = row
        return row
    for filename, digest in FROZEN.items():
        demand(bind(HERE / filename)['sha256'] == digest, 'Unreviewed entry source: ' + filename)
    launch = load(LAUNCH)
    demand(bind(LAUNCH)['sha256'] == '710fbd942be28cc67bddcc511d3e01a1bcc9de77adc5e7fea91f69adb5562666',
           'Changed prepared launch')
    reference = load(launch['reference_preparation']['path'])
    for ledger in (launch['bindings'], reference['bindings']):
        demand(len({row['path'] for row in ledger}) == len(ledger), 'Duplicate source binding')
        for row in ledger:
            demand(bind(row['path']) == row, 'Bound source differs')
    demand(len(launch['bindings']) == 106 and len(reference['bindings']) == 97, 'Unexpected source extent')
    listed = {row['path']: row for row in launch['bindings']}
    demand(all(listed.get(row['path']) == row for row in reference['bindings']), 'Original closure omitted')
    callbacks = launch['callbacks']
    demand(len(callbacks) == 21, 'Incomplete callback ledger')
    for key, row in callbacks.items():
        demand(callback_from_ast(row['file']['path'], row['qualname']) == row, 'AST callback differs: ' + key)
        demand(listed.get(row['file']['path']) == row['file'], 'Callback source outside closure')
    for key, row in reference['callbacks'].items():
        demand(callbacks[key] == row, 'Changed original affine/common callback definition')
    prior = load(reference['frozen_tail']['path'])
    seed = load(reference['checkpoint']['path'])
    cfg = load(launch['tail_config']['path'])
    demand(canon({k:v for k,v in cfg.items() if k not in IO}) ==
           canon({k:v for k,v in prior['config'].items() if k not in IO}), 'Changed actual tail mathematics')
    demand(cfg['initialCheckpoint'] == reference['frozen_tail']['path'], 'Warm is not the own true final packet')
    for optional in ('trialDiagnosticFile','trialStatePrefix','projectionFloor','correctInitialBoundary'):
        demand(optional not in cfg and optional not in prior['config'], 'Old option absence was not preserved')
    for name, digest in prior['source_sha256'].items():
        path = HERE / name
        demand(bind(path)['sha256'] == digest and str(path.resolve()) in listed, 'Wrong original shared tail source')
    demand(len(prior['source_sha256']) == 8, 'Expected original shared eight-source tail')
    weights = [1.] + [float(2 ** ((9*j*j).bit_length())) for _ in range(3) for j in range(1,15)]
    demand(launch['weights'] == weights and len(weights) == 43 and max(weights) == 2048, 'Wrong W14')
    demand(all(1+9*j*j <= weights[j] < 2*(1+9*j*j) for j in range(1,15)), 'Weight enclosure differs')
    argv = launch['delegated_parser_argv']
    demand(argv[0] == str(HERE/'db6f-prefix-flat-coupled.py'), 'Changed original entry')
    for key, value in {'--modes':'14','--angular':'512','--audit-angular':'1024','--nodes':'1601',
                       '--max-nodes':'6500','--tol':'2e-09','--bc-tol':'1e-08',
                       '--physical-bc-tol':'2e-11','--node-heap':'1536'}.items():
        demand(argv.count(key) == 1 and argv[argv.index(key)+1] == value, 'Changed original option: ' + key)
    demand(argv[-4:] == ['--fixed','--warmup-scales','--lagged-tail','--preserve-restart-mesh'],
           'Warmup must be empty and true lagged restart retained')
    selector_tree = ast.parse((HERE/'db6f-prefix-spectral-true-m14.py').read_text())
    overrides = [ast.unparse(target) for node in ast.walk(selector_tree) if isinstance(node,ast.Assign)
                 for target in node.targets if isinstance(target,ast.Attribute)]
    demand(overrides == ['runner.solve_bvp','sys.argv','sys.argv'], 'Unexpected module mathematical override')
    original_tree = ast.parse((HERE/'db6f-prefix-coupled.py').read_text())
    outer = next(node for node in original_tree.body if isinstance(node,ast.FunctionDef) and node.name=='solve_with_actual_tail')
    bvp_calls = [node for node in ast.walk(outer) if isinstance(node,ast.Call)
                 and isinstance(node.func,ast.Name) and node.func.id=='solve_bvp']
    demand(len(bvp_calls)==2, 'Original insertion points changed')
    restore = [node for node in ast.walk(outer) if isinstance(node,ast.Try)
               and any(isinstance(v,ast.Assign) and ast.unparse(v)=='o.tail = tail' for v in node.finalbody)]
    demand(len(restore)==1, 'True tail is not restored in original finally')
    originals = {str((HERE/name).resolve()) for name in ('db6f-prefix-coupled.py','db6f-prefix-spectral-true-m14.py')}
    demand(set(launch['included_runtime_cli_main_sources']) == originals, 'True main omitted from closure scan')
    demand(all(row['path'] not in originals for row in launch['excluded_unused_dependency_cli_entries']),
           'A real main was incorrectly excluded')
    before_modules = set(sys.modules)
    spec = importlib.util.spec_from_file_location('tail_review_true_m14_closed_only', HERE/'db6f-prefix-audit-spectral-true-m14.py')
    auditor = importlib.util.module_from_spec(spec); spec.loader.exec_module(auditor)
    imported = set(sys.modules)-before_modules
    demand(not any(name.startswith(('f6curve','curve_stable','fixed_metric_mode3')) for name in imported),
           'Read-only definitions imported a candidate implementation')
    context = auditor.c.validate_inputs(launch)
    historical_context = {'config':prior['config'], 'prior':prior}
    historical = auditor.check_packet(reference['frozen_tail']['path'], prior['request']['height'], True, historical_context)
    old_path = Path(reference['checkpoint']['path'])
    demand(str(old_path).endswith('.json.gz'), 'Unexpected old CP suffix')
    saved_height, chunk_rows, pp = auditor.polynomial_endpoint(seed, {'out':Path(str(old_path)[:-8])})
    demand(canon(saved_height) == canon(prior['request']['height']), 'New read-only PPoly endpoint convention differs from old true seam')
    for row in chunk_rows:
        demand(bind(row['path']) == row, 'Saved coefficient changed')
    # Only corrupt already-historical bytes in memory. Every corruption must
    # reject before the method can emit a success report or file identity.
    faults = {}
    sentinel = Path('/__tail_review_historical_rejection_only__')
    real_read = auditor.read
    mutations = {
        'false_convergence': lambda x:x['response'].__setitem__('converged',False),
        'missing_Jacobian_entry': lambda x:x['response']['heightJetJacobian'].pop(),
        'wrong_raw_mirror': lambda x:x['response']['checkpoint']['rawStates'][0].__setitem__(0,123.0),
        'typed_config_bool': lambda x:x['config'].__setitem__('sharedEngines',1),
        'wrong_audit_request': lambda x:x['request'].__setitem__('audit',False),
        'extra_failure_marker': lambda x:x['response'].__setitem__('failed',False),
    }
    try:
        for name, change in mutations.items():
            damaged = copy.deepcopy(prior); change(damaged)
            auditor.read = lambda path, value=damaged: value if Path(path)==sentinel else real_read(path)
            try:
                auditor.check_packet(sentinel, prior['request']['height'], True, historical_context)
            except ValueError as error:
                faults[name] = str(error)
            else:
                raise AssertionError('Historical corruption was accepted: '+name)
    finally:
        auditor.read = real_read
    try:
        auditor.final_audit(context,None)
    except ValueError as error:
        no_observer = str(error)
        demand(no_observer.startswith('NOT_READY: root actual tool-exit observation'), 'Wrong actual-exit negative gate')
    else:
        raise AssertionError('Final gate accepted absence of root actual exit')
    for row in list(rows.values()):
        demand(ident(row['path']) == row, 'Source changed while checking')
    report = {'status':'PASS_INDEPENDENT_TRUE_M14_IMPLEMENTATION_STATIC_AND_HISTORICAL_CHECKS',
              'scope':__doc__, 'source_bindings':sorted(rows.values(),key=lambda r:r['path']),
              'new_launch':ident(LAUNCH),'new_launch_bindings':106,'original_bindings':97,
              'callbacks_independently_reconstructed':21,'weights':{'states':43,'maximum':2048},
              'original_global_solve_bvp_calls':len(bvp_calls),'module_assignment_targets':overrides,
              'historical_real_packet':historical,'historical_saved_polynomial':pp,
              'historical_endpoint_equals_own_actual_seam':True,
              'historical_corruptions_rejected':faults,'actual_observer_required':no_observer,
              'operations':{'candidate_initialization':0,'restart':0,'flow':0,'RHS':0,'Newton_install':0,
                            'weighted_solver_factory':0,'BVP':0,'DN':0,'saved_PPoly_endpoint':1},
              'future_true_M14_result':'NOT_RUN_AND_NOT_INFERRED'}
    raw=(json.dumps(report,indent=2,ensure_ascii=False,allow_nan=False)+'\n').encode()
    demand(len(raw)<100000,'Review metadata unexpectedly large')
    args.out.parent.mkdir(parents=True,exist_ok=True)
    with args.out.open('xb') as stream:stream.write(raw)
    print(json.dumps({'status':report['status'],'unique_inputs':len(rows),'callbacks':21,
                      'historical_rejections':len(faults),'solver_calls':0,'report':ident(args.out)}))


if __name__=='__main__':
    main()
