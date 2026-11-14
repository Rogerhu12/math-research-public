#!/usr/bin/env python3
"""Pure metadata/source preparation for the frozen-affine M14 spectral trial.

No prefix object, bridge, flow, original Newton installation, BVP or tail
client is constructed. Expected callback identities come from source ASTs.
"""
import argparse
import ast
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
NOTES = TOPIC / 'notes'
REPO = TOPIC.parents[1]
STEM = '2026-11-09-db6f-prefix-flat-v17v18-fixed-m14-d12-p8-s32-q512-outer-from14'
RUNNER = HERE / 'db6f-prefix-spectral-affine-replay.py'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out-prefix', type=Path, required=True)
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location('spectral_affine_pure_helpers', RUNNER)
    h = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(h)  # Definitions only; h.main is not called.
    out = args.out_prefix.resolve()
    h.require(out.parent == NOTES.resolve() and not list(out.parent.glob(out.name + '*')),
              'Use a completely unused topic notes stem')
    source_root = TOPIC / 'repro/source-root'
    source_scripts = source_root / 'topics/large-amplitude-twist-flex/scripts'
    paths = {
        'checkpoint': NOTES / (STEM + '.json.gz'),
        'frozen_tail': NOTES / (STEM + '_tail_0002.json.gz'),
        'linear_port': NOTES / '2026-11-09-950f-prefix-weighted-k6-port96-cusp1024.json',
        'profile': NOTES / (STEM + '-frozen-profile.json'),
        'chart': NOTES / '2026-11-09-950f-prefix-adaptive-chart.json',
        'tail_config': NOTES / (STEM + '-tail-config.json'),
        'original_reproduction': NOTES / (STEM + '-reproduction.json'),
        'original_summary': NOTES / (STEM + '-summary.json'),
        'original_publication': NOTES / '2026-11-09-db6f-prefix-m14q512-m15failed-publication.json',
        'matched_source_closure': NOTES / '2026-11-09-db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-matched-cut-s63of64-01-input-bindings.json',
        'baseline': HERE / 'db6f-prefix-affine-replay.py',
        'spectral_module': HERE / 'db6f-root-spectral-collocation-v2.py',
        'spectral_review': NOTES / '2026-11-09-db6f-tail-review-spectral-conjugacy.md',
        'spectral_erratum': NOTES / '2026-11-09-db6f-root-spectral-collocation-v2-erratum.md',
        'runner': RUNNER, 'preparer': Path(__file__).resolve(),
    }
    expected = {
        'checkpoint': '3df8eefb18c4271283c7ae2b076afcda3fb42b169c8a7296ee4bce3e3b3ad3d0',
        'frozen_tail': '009bf5472ca412fae7d900d4ec18d26cd217221138666c2899dfceb3ead8f762',
        'linear_port': '500e0a0c6d5388e07e3673ef192856804264c612edd6fe26ee09b882698a3702',
        'original_reproduction': '0f5ded3b774e81d1e9d49e8901609672c08348c15a610b2ae4eb37c0dbda8655',
        'original_summary': '70fb5707b64841eb32d587b2f925600ef7d9f11dc693e9e362d5db23fe9181be',
        'original_publication': '3aada1964b73cc92cc4860c97c46ccdda4cbf41988b4e6f474c6dbe7d8c76f53',
        'matched_source_closure': '5b184918f4c5a86f10189c5433cd447af4a822856a2fe569df4439e03efdeb21',
        'baseline': '8eab6d580c2ad04a794e051c6b552eebe3d6d228feb653b9fa84cd4a9b3d34a4',
        'spectral_module': '47e1128c8cabb7c77797ebea6534cf77d63964add54f78a2cab827d1f0101854',
        'spectral_review': '252be823c11f33cb683c20a9c0dd521389ca2323c38ace8ce08298459ae243f5',
        'spectral_erratum': '632ef79dd055cbc612cdca517eda0fbea2ab8e6c1d4c6b871658f0ccb9a3ed9d',
    }
    identities = {key: h.identity(path) for key, path in paths.items()}
    for key, sha in expected.items():
        h.require(identities[key]['sha256'] == sha, 'Wrong frozen source/input: ' + key)
    rec, packet, publication, reproduction = [h.read(paths[key]) for key in
        ('checkpoint', 'frozen_tail', 'original_publication', 'original_reproduction')]
    outcomes = [row for row in publication['outcomes'] if row['stem'] == STEM]
    h.require(len(outcomes) == 1 and outcomes[0]['mathematical_success'] is True
              and outcomes[0]['actual_driver_exit_code'] == 0
              and reproduction['success'] is True and reproduction['exit_code'] == 0,
              'The actual M14/N512 source run was not successfully closed')
    source_closure = h.read(paths['matched_source_closure'])
    h.require(len(source_closure['bound_files']) == 121, 'Unexpected original source-closure anchor')
    bindings = {row['path']: row for row in identities.values()}
    # The earlier closure is a provenance anchor, not a claim that its M15
    # candidate is being used. Only its frozen source files enter this run.
    for row in source_closure['bound_files']:
        h.verify(row)
        if Path(row['path']).suffix in ('.py', '.mjs'):
            bindings[row['path']] = row
    roots = [source_scripts, NOTES, HERE]
    direct = [HERE / 'db6f-prefix-flat-coupled.py', HERE / 'db6f-prefix-flat-profile.py',
              HERE / '950f-prefix-flat-accel-screen.py', HERE / '950f-tail-client-v3.py',
              HERE / 'db6f-prefix-preserve-restart.py', NOTES / 'closing_tail_dependency_blobs.json']
    for p in direct:
        row = h.identity(p); bindings[row['path']] = row
    # Bind every supplied source-root Python file, and recursively resolve
    # normal local Python imports in source-root -> notes -> scripts order.
    pending = list(source_scripts.glob('*.py')) + [Path(row['path']) for row in bindings.values()
                                                  if Path(row['path']).suffix == '.py']
    visited = set()
    unresolved_local = set()
    deferred_cli_functions = []
    while pending:
        p = pending.pop().resolve()
        if p in visited:
            continue
        visited.add(p)
        row = h.identity(p); bindings[row['path']] = row
        tree = ast.parse(p.read_text(), filename=str(p))
        names = set()
        def imports(node):
            # The runner imports these dependency modules, but never calls
            # their unrelated command-line main(). The new runner's own
            # entry point is included; its imports must remain fully bound.
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == 'main' and p != RUNNER.resolve():
                deferred_cli_functions.append({'path': str(p), 'function': 'main', 'line': node.lineno,
                                               'scope': 'Unused dependency CLI entry; not part of the affine runner call graph.'})
                return
            if isinstance(node, ast.Import):
                names.update(item.name.split('.')[0] for item in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module and not node.level:
                names.add(node.module.split('.')[0])
            for child in ast.iter_child_nodes(node):
                imports(child)
        imports(tree)
        for name in names:
            candidates = [root / (name + '.py') for root in roots]
            found = next((q for q in candidates if q.is_file()), None)
            if found is not None:
                pending.append(found)
            elif name.startswith(('f6', 'curve_', 'construct_', 'fixed_metric_', 'repo_scan_')):
                unresolved_local.add(name)
    h.require(not unresolved_local, 'Unbound local Python import: ' + ', '.join(sorted(unresolved_local)))
    for name, sha in packet['source_sha256'].items():
        p = HERE / name; row = h.identity(p)
        h.require(row['sha256'] == sha, 'Original own-tail source changed: ' + name)
        bindings[row['path']] = row
    for item in rec['pp_coefficient_chunks']:
        p = paths['checkpoint'].parent / item['file']; row = h.identity(p)
        h.require(row['bytes'] == item['bytes'] and row['sha256'] == item['sha256'], 'Original coefficient identity differs')
        bindings[row['path']] = row
    # Importing this reviewed module defines the conjugacy; no solver factory
    # or solve function is called by preparation.
    spectral = h.module('spectral_affine_preparation_weights', paths['spectral_module'])
    import scipy.integrate._bvp as scipy_bvp
    import inspect
    scipy_source = h.identity(inspect.getfile(scipy_bvp))
    h.require(scipy_source['sha256'] == spectral.SCIPY_BVP_SHA256, 'Wrong reviewed SciPy layout')
    bindings[scipy_source['path']] = scipy_source
    callback_defs = {
        'fun': (NOTES / 'fixed_metric_mode3_bvp.py', 'SupportBVP.fun'),
        'fun_jac': (NOTES / 'fixed_metric_mode3_bvp.py', 'SupportBVP.fun_jac'),
        'bc': (NOTES / 'fixed_metric_mode3_bvp.py', 'SupportBVP.bc'),
        'bc_jac': (HERE / 'db6f-prefix-coupled.py', 'TailMixin.bc_jac'),
        'terminal': (HERE / 'db6f-prefix-coupled.py', 'TailMixin.terminal'),
        'initial': (HERE / '950f-prefix-warped-bvp.py', 'build_classes.<locals>.WarpedBVP.initial'),
        'chart': (NOTES / 'fixed_metric_mode3_bvp.py', 'SupportBVP.chart'),
        'physical_fun': (HERE / '950f-prefix-adaptive-chart-bvp-v2.py', 'build_classes.<locals>.Flow.adapt_fun'),
        'physical_fun_jac': (HERE / '950f-prefix-adaptive-chart-bvp-v2.py', 'build_classes.<locals>.Flow.adapt_fun_jac'),
        'physical_c2_interpolant': (HERE / '950f-prefix-adaptive-chart-bvp-v2.py', 'build_classes.<locals>.Flow.adapt_c2_interpolant'),
        'affine_dn': (HERE / 'db6f-prefix-coupled.py', 'AffineTailForInnerBVP.solve'),
        'restart': (HERE / 'db6f-prefix-preserve-restart.py', 'restart'),
        'save_checkpoint': (source_scripts / 'curve_stable_prefix_bvp.py', 'save_checkpoint'),
        'domain_install': (source_scripts / 'f6curve_domain_newton.py', 'install'),
        'domain_solve_newton': (source_scripts / 'f6curve_domain_newton.py', 'solve_newton'),
    }
    callbacks = {name: h.source_function(path, qualname) for name, (path, qualname) in callback_defs.items()}
    h.require(all(row['file']['path'] in bindings for row in callbacks.values()), 'A callback source is not bound')
    launch_path = Path(str(out) + '-launch.json')
    prep_path = Path(str(out) + '-preparation.json')
    launch = {'schema': 'db6f-spectral-affine-m14q512-v1', 'status': 'PREPARED_NOT_STARTED',
              'scope': h.SCOPE, 'scope_flags': h.FLAGS, **h.FLAGS, 'settings': h.SETTINGS,
              'launch_path': str(launch_path), 'out_prefix': str(out), 'source_root': str(source_root),
              **{key: identities[key] for key in ('checkpoint','frozen_tail','linear_port','profile','chart','tail_config')},
              'frozen_physical_fields': {key: rec[key] for key in h.PHYSICAL_FIELDS},
              'gauge_amplitude': rec['gauge_amplitude'], 'frozen_tail_sources': packet['source_sha256'],
              'callbacks': callbacks, 'weights': spectral.power2_weights(14).tolist(),
              'excluded_unused_dependency_cli_entries': sorted(deferred_cli_functions, key=lambda row: row['path']),
              'expected_runtime_newton': 'After original install(), scipy.integrate._bvp.solve_newton is f6curve_domain_newton.solve_newton; runtime source and signature are checked before the one BVP call.',
              'runtime_newton_identity_check_performed_in_preparation': False,
              'command': [sys.executable, str(RUNNER), '--launch', str(launch_path)], 'cwd': str(REPO),
              'stdout_log': str(out) + '-run.log', 'reproduction_file': str(out) + '-reproduction.json',
              'summary_file': str(out) + '-summary.json', 'checkpoint_output': str(out) + '.json.gz',
              'coefficient_output_pattern': str(out) + '_coeff_*.npy.gz',
              'bindings': sorted(bindings.values(), key=lambda row: row['path'])}
    h.validate_inputs(launch)
    # Every validation precedes all writes. No new CP, solver response,
    # coefficients, initialization state or positive weighted fixture exists.
    h.write_json(launch_path, launch, exclusive=True)
    report = {'status': 'PREPARED_ONLY_NO_INITIALIZATION_NO_SOLVER', 'scope': __doc__, **h.FLAGS,
              'launch': h.identity(launch_path), 'source_checkpoint': identities['checkpoint'],
              'own_actual_final_DN': identities['frozen_tail'],
              'own_actual_DN_residual': packet['response']['residual'], 'own_DN_Jacobian_length': len(packet['response']['heightJetJacobian']),
              'state_components': 43, 'original_modes': 14, 'original_angular': 512,
              'frozen_physical_field_count': len(h.PHYSICAL_FIELDS), 'callback_count': len(callbacks),
              'binding_count': len(launch['bindings']), 'recursively_visited_python_sources': len(visited),
              'unused_dependency_cli_entry_count': len(deferred_cli_functions),
              'settings': h.SETTINGS, 'source_root': str(source_root),
              'actual_new_DN_calls': 0, 'actual_BVP_calls': 0, 'actual_flow_or_bridge_initializations': 0,
              'actual_newton_install_calls': 0, 'actual_weighted_solver_factory_calls': 0,
              'runtime_newton_identity_check_status': 'NOT_RUN; the actual future runner must check after original install()',
              'existing_M14_tool_exit_provenance': identities['original_publication'],
              'future_tool_exit_scope': 'A root actual tool observation is required; no future process exit is asserted here.'}
    h.write_json(prep_path, report, exclusive=True)
    print(json.dumps({'status': report['status'], **h.FLAGS, 'binding_count': report['binding_count'],
                      'launch': h.identity(launch_path), 'preparation': h.identity(prep_path)}, indent=2))


if __name__ == '__main__':
    main()
