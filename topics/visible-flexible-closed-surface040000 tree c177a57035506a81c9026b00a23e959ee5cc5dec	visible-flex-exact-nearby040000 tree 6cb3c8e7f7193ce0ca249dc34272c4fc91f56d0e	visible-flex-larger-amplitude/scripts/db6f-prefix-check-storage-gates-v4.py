#!/usr/bin/env python3
"""Pure source/stdlib storage checks; no mathematical object or candidate certificate.

The only positive data check is the existing old M12 base packet's actual
storage closure, passed in both identity positions of the new byte helper.
No new common-cut metadata, numerical report, mesh, or future candidate is made.
"""
import argparse
import ast
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
NOTES = TOPIC/'notes'
C_SOURCES = {
    'db6f-prefix-angular-metric-storage.py': '2f24cdf9b9649a5ecd34bdbbdabaf294f1fb985288578b54217a6143c98e902c',
    'db6f-prefix-export-closed-mesh-storage.py': 'd776e41ef75741be0d5d44a8156d2c71a70ad016ef3678605d718a32ba7684d1',
    'db6f-prefix-review-closed-mesh-storage.py': '698e8b0528ffa7b1bbe1bc84c574079f60261156f1d3a6ddae048af0f9c0c479',
    'db6f-prefix-terminal-error-storage.py': '809cc7ab61903f11847653fda018506f7c2bed38a7501007909200eb0bf69584',
    'db6f-prefix-terminal-error-storage-v2.py': 'a00f8210d561983e9d137a848cb7b582e33de8450c0b70497e3933080c297aa1',
    'db6f-prefix-terminal-error-storage-v3.py': '8db94c71a9035f2f977daea9c315b669bce4c20800f80e7886b77c66af6f7ed7',
}
TRANSFORMS = [
    ('2026-11-09-db6f-prefix-storage-gates-transformations.json',
     '0417ac80883dda492618f8535a06ce0eaab230decf0eec4751d2b8c41b25dd88'),
    ('2026-11-09-db6f-prefix-storage-terminal-v2-transformations.json',
     '82bbb53a65803c1f2531a6d2544f82d86f820d458acfeb5494f07f3d7b7f3d69'),
    ('2026-11-09-db6f-prefix-storage-terminal-v3-transformations.json',
     '4299872c6189de869d137682ace26eee965fdabc0af01a2c47a25342bab1e336'),
]
OLD_BASE = '2026-11-09-db6f-prefix-storage-old-m12-01.json'
OLD_LOGICAL_SHA = '359d491cd592962d467fdd538013977ee9a92070346de41c227d9ca3e1ef3bd0'


def check(ok, message):
    if not ok:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def record(path):
    path = Path(path).resolve()
    return dict(file=str(path), bytes=path.stat().st_size, sha256=sha(path))


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def assigned(source, name):
    for item in ast.parse(source).body:
        if isinstance(item, ast.Assign) and any(isinstance(t, ast.Name) and t.id == name for t in item.targets):
            return ast.literal_eval(item.value)
    raise ValueError('Missing assignment '+name)


def functions(source):
    return {node.name: ast.get_source_segment(source, node) for node in ast.parse(source).body
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))}


def replay_transformation(entry):
    original, path = HERE/entry['old'], HERE/entry['new']
    check(sha(original) == entry['old_sha256'] and sha(path) == entry['new_sha256'],
          'Changed source in the transformation ledger')
    value = original.read_text()
    for step in entry['replacements']:
        check(value.count(step['old']) == step['count'], 'Ambiguous forward replacement')
        value = value.replace(step['old'], step['new'])
    check(value.encode() == path.read_bytes(), 'Full transformed source differs from the frozen source')
    check(ast.dump(ast.parse(value), include_attributes=False) ==
          ast.dump(ast.parse(path.read_text()), include_attributes=False), 'AST differs')
    return dict(old=entry['old'], new=entry['new'], replacements=len(entry['replacements']),
                byte_identical_to_complete_declared_transformation=True, ast_identical=True)


def reject(label, fn, output):
    try:
        fn()
    except (ValueError, KeyError, FileNotFoundError, TypeError) as error:
        output.append(dict(case=label, rejected=True, error_type=type(error).__name__, message=str(error)))
    else:
        raise ValueError('Negative case accepted: '+label)


def child_check():
    path = HERE/'db6f-prefix-terminal-error-storage-v3.py'
    terminal = module('storage_terminal_pure_check_child', path)
    base_path = NOTES/OLD_BASE
    base = json.loads(base_path.read_text())
    files = terminal.Files()
    bindings = terminal.prefix_storage(files, base_path, base, base)
    terminal.prefix_storage_ledger(files, bindings, bindings, base_path.parent, 'old-base-only-control')
    relocated = [dict(item, file=str(Path('/nonexistent-relocated-old-checkout')/Path(item['file']).name))
                 for item in bindings]
    terminal.prefix_storage_ledger(files, relocated, bindings, base_path.parent, 'relocated-old-base-control')
    check('numpy' not in sys.modules and 'scipy' not in sys.modules,
          'A numerical backend was imported')
    check(base['data_sha256'] == OLD_LOGICAL_SHA, 'Old logical map identity changed')
    print(json.dumps(dict(status='PASS-old-base-storage-only', storage_bindings=len(bindings),
                         numpy_imported=False, scipy_imported=False,
                         candidate_branch_executed=False)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path)
    parser.add_argument('--child-stdlib', action='store_true')
    args = parser.parse_args()
    if args.child_stdlib:
        child_check()
        return
    check(args.out is not None and not args.out.exists(), 'Need a fresh output report')
    inputs = []
    for name, digest in C_SOURCES.items():
        check(sha(HERE/name) == digest, 'Changed frozen C source '+name)
        ast.parse((HERE/name).read_text())
        inputs.append(record(HERE/name))
    entries = []
    for name, digest in TRANSFORMS:
        path = NOTES/name
        check(sha(path) == digest, 'Changed source transformation ledger')
        data = json.loads(path.read_text())
        entries.extend(data.get('transformations', [data]))
        inputs.append(record(path))
    transformed = [replay_transformation(entry) for entry in entries]
    for entry in entries:
        inputs.append(record(HERE/entry['old']))
    old_terminal = (HERE/'db6f-audit-terminal-error-gate.py').read_text()
    new_terminal = (HERE/'db6f-prefix-terminal-error-storage-v3.py').read_text()
    oldfunc, newfunc = functions(old_terminal), functions(new_terminal)
    fixed_functions = ['check', 'canonical', 'binary', 'exact', 'same', 'parameters',
        'checkpoint_parameters', 'definitions', 'manifest_files', 'reference', 'transfer',
        'tail_certificate', 'scalar_gate', 'main']
    check(all(oldfunc[name] == newfunc[name] for name in fixed_functions),
          'An old tail/reference/threshold function changed')
    check(assigned(old_terminal, 'SOURCES') == assigned(new_terminal, 'SOURCES'),
          'Old source family was replaced or extended')
    for name in ('REFERENCE', 'BACKGROUND', 'PREFIX_KEYS', 'BRIDGE_KEYS'):
        check(assigned(old_terminal, name) == assigned(new_terminal, name), 'Changed original '+name)
    prefix_sources = assigned(new_terminal, 'PREFIX_SOURCES')
    for name, digest in prefix_sources.items():
        check(sha(HERE/name) == digest, 'Changed actual prefix source '+name)
        inputs.append(record(HERE/name))
    angular = (HERE/'db6f-prefix-angular-metric-storage.py').read_text()
    for name, digest in assigned(angular, 'SOURCES').items():
        check(sha(HERE/name) == digest, 'Changed actual angular source '+name)
        inputs.append(record(HERE/name))
    angular_functions = functions(angular)
    original_angular = functions((HERE/'db6f-audit-prefix-angular-metric.py').read_text())
    check(all(angular_functions[name] == original_angular[name] for name in ('trig_table', 'verify_rows')),
          'Angular arithmetic/coverage changed')
    mesh = (HERE/'db6f-prefix-export-closed-mesh-storage.py').read_text()
    mesh_funcs, old_mesh_funcs = functions(mesh), functions((HERE/'db6f-export-closed-mesh.py').read_text())
    mesh_fixed = sorted(set(old_mesh_funcs)-{'prepare', 'plan', 'build'})
    check(all(mesh_funcs[name] == old_mesh_funcs[name] for name in mesh_fixed),
          'Mesh mathematics or writer changed')
    replay = (HERE/'db6f-prefix-review-closed-mesh-storage.py').read_text()
    check(assigned(replay, 'EXPORTER_SHA') == sha(HERE/'db6f-prefix-export-closed-mesh-storage.py'),
          'New mesh replay pins another exporter')
    terminal = module('storage_terminal_pure_check', HERE/'db6f-prefix-terminal-error-storage-v3.py')
    base_path = NOTES/OLD_BASE
    base = json.loads(base_path.read_text())
    files = terminal.Files()
    bindings = terminal.prefix_storage(files, base_path, base, base)
    terminal.prefix_storage_ledger(files, bindings, bindings, base_path.parent, 'old-base-only-control')
    relocated = [dict(item, file=str(Path('/nonexistent-relocated-old-checkout')/Path(item['file']).name))
                 for item in bindings]
    terminal.prefix_storage_ledger(files, relocated, bindings, base_path.parent, 'relocated-old-base-control')
    inputs.extend(bindings)
    check(base['data_sha256'] == OLD_LOGICAL_SHA and base['source_modes'] == 12 and base['modes'] == 24,
          'Not the exact reviewed old M12 base')
    bad = []
    missing = NOTES/'db6f-storage-test-intentionally-missing-whole.json'
    check(not missing.exists(), 'Missing-input test name has been used')
    reject('normal-candidate-missing-whole',
           lambda: terminal.candidate(terminal.Files(), missing, None, None, {}), bad)
    reject('new-prefix-cannot-claim-old-backend', lambda: files.prefix_source(
        'db6f-prefix-continuous-hermite-storage.py', terminal.SOURCES['db6f-audit-continuous-hermite.py']), bad)
    reject('old-tail-cannot-claim-new-backend', lambda: files.source(
        'db6f-audit-continuous-hermite.py', terminal.PREFIX_SOURCES['db6f-prefix-continuous-hermite-storage.py']), bad)
    reject('missing-storage-item', lambda: terminal.prefix_storage_ledger(
        files, bindings[:-1], bindings, base_path.parent, 'negative'), bad)
    repeated = copy.deepcopy(bindings); repeated[-1] = copy.deepcopy(repeated[0])
    reject('repeated-storage-item', lambda: terminal.prefix_storage_ledger(
        files, repeated, bindings, base_path.parent, 'negative'), bad)
    for label, mutate in [('boolean-byte-count', lambda row: row.update(bytes=True)),
                          ('wrong-byte-count', lambda row: row.update(bytes=row['bytes']+1)),
                          ('wrong-sha256', lambda row: row.update(sha256='0'*64)),
                          ('extra-item-field', lambda row: row.update(unpaid=True))]:
        rows = copy.deepcopy(bindings); mutate(rows[0])
        reject(label, lambda rows=rows: terminal.prefix_storage_ledger(
            files, rows, bindings, base_path.parent, 'negative'), bad)
    wrong_common = copy.deepcopy(base); wrong_common['data_storage']['logical_bytes'] += 1
    reject('different-common-base-reference', lambda: terminal.prefix_storage(
        terminal.Files(), base_path, base, wrong_common), bad)
    wrong_loaded = copy.deepcopy(base); wrong_loaded['modes'] += 1
    reject('base-metadata-changed-before-read', lambda: terminal.prefix_storage(
        terminal.Files(), base_path, wrong_loaded, wrong_loaded), bad)
    legacy = copy.deepcopy(base); legacy.pop('data_storage'); legacy['data_file'] = 'not-used.npz.gz'
    reject('new-candidate-helper-rejects-legacy-storage', lambda: terminal.prefix_storage(
        terminal.Files(), base_path, legacy, legacy), bad)
    check('numpy' not in sys.modules and 'scipy' not in sys.modules,
          'Numerical module imported during source/storage checks')
    child = subprocess.run([sys.executable, '-I', str(Path(__file__).resolve()), '--child-stdlib'],
                           check=False, text=True, capture_output=True)
    check(child.returncode == 0 and not child.stderr, 'Fresh stdlib child failed: '+child.stderr)
    child_report = json.loads(child.stdout)
    before = {item['file']: (item['bytes'], item['sha256']) for item in inputs}
    check(all(Path(path).stat().st_size == count and sha(path) == digest
              for path, (count, digest) in before.items()), 'An input changed during checks')
    result = dict(status='PASS-source-and-actual-old-base-byte-storage-only',
        script_sha256=sha(__file__), transformations=transformed,
        original_terminal_sources_dictionary_unchanged=True,
        original_terminal_functions_unchanged=fixed_functions,
        original_mesh_functions_unchanged=mesh_fixed,
        actual_prefix_source_count=len(prefix_sources),
        old_base=dict(file=str(base_path), sha256=sha(base_path), modes=base['modes'],
                      source_modes=base['source_modes'], logical_sha256=base['data_sha256']),
        positive_scope='Existing old base metadata in both helper identity positions; no common-cut candidate or numerical certificate was manufactured.',
        relocated_old_base_storage_ledger_verified=True,
        storage_bindings=bindings, negative_cases=bad, fresh_stdlib_child=child_report,
        inputs=[dict(file=path, bytes=count, sha256=digest) for path, (count, digest) in sorted(before.items())],
        producer_calls=0, mathematical_object_constructions=0,
        angular_verifier_run=False, numerical_backends_imported=False,
        continuous_metric_or_curvature_run=False, new_geometry_or_mesh_generated=False,
        actual_new_root_flow_solver_calls=0, future_positive_candidate_branch_executed=False)
    payload = json.dumps(result, indent=2, allow_nan=False)+'\n'
    with args.out.open('x') as stream:
        stream.write(payload)
    print(json.dumps(dict(status=result['status'], complete_source_transformation_checks=len(transformed),
        negative_cases=len(bad), actual_source_inputs=len(before),
        sha256=sha(args.out), mathematical_object_constructions=0)))


if __name__ == '__main__':
    main()
