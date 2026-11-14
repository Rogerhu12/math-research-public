#!/usr/bin/env python3
"""Independent metadata/AST check of the true-M14 explicit LU variant.

Uses only Python's standard library. Does not import candidate/solver modules,
call install/select_newton, or create any mathematical success fixture.
The separate actual pure preparation and negative-gate receipts are recorded
by the reviewer, not inferred by this check.
"""
import ast
import copy
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
NOTES = TOPIC / 'notes'
NAME = '2026-11-09-db6f-tail-review-spectral-true-m14-release-lu'
AUTHOR = NOTES / '2026-11-09-db6f-prefix-spectral-true-m14q512-release-lu-01'
REPLAY = NOTES / '2026-11-09-db6f-tail-review-spectral-true-m14q512-release-lu-pure-01'
OLD = NOTES / '2026-11-09-db6f-prefix-spectral-true-m14q512-01-launch.json'
PUB = NOTES / '2026-11-09-db6f-prefix-spectral-true-m14-release-lu-publication.json'
REVIEWER = '/root/tail_review_continued_2'
sources = {}
checks = []


def require(value, message):
    if not value:
        raise ValueError(message)


def identity(path):
    path = Path(path).resolve()
    data = path.read_bytes()
    row = {'path': str(path), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}
    sources[str(path)] = row
    return row


def verify(row):
    require(identity(row['path']) == row, 'Source identity mismatch: ' + row['path'])


def read(path):
    identity(path)
    return json.loads(Path(path).read_text())


def equal(a, b, message):
    # JSON typed equality: true, 1, and 1.0 are not interchangeable.
    encode = lambda x: json.dumps(x, sort_keys=True, separators=(',', ':'), allow_nan=False)
    require(encode(a) == encode(b), message)


def record(label, **values):
    checks.append({'check': label, 'status': 'PASS', **values})


def tree(path):
    identity(path)
    return ast.parse(Path(path).read_text(), filename=str(path))


def find(root, qualname):
    node = root
    for part in qualname.split('.'):
        if part == '<locals>':
            continue
        matches = [n for n in node.body
                   if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and n.name == part]
        require(len(matches) == 1, 'Missing/ambiguous AST definition: ' + qualname)
        node = matches[0]
    return node


def dump(node):
    return ast.dump(node, include_attributes=False)


def source_callback(row):
    path = Path(row['file']['path'])
    node = find(tree(path), row['qualname'])
    text = '\n'.join(path.read_text().splitlines()[node.lineno - 1:node.end_lineno]).rstrip()
    actual = {'file': identity(path), 'qualname': row['qualname'], 'first_line': node.lineno,
              'source_sha256_rstrip': hashlib.sha256(text.encode()).hexdigest()}
    equal(actual, row, 'Source callback mismatch: ' + row['qualname'])


def call_lines(node, name):
    return [n.lineno for n in ast.walk(node) if isinstance(n, ast.Call)
            and isinstance(n.func, ast.Name) and n.func.id == name]


def normalized(obj, stem, bindings):
    if isinstance(obj, dict):
        if set(obj) == {'path', 'bytes', 'sha256'} and obj['path'] in bindings:
            return {'checked_binding': bindings[obj['path']]}
        return {k: normalized(v, stem, bindings) for k, v in obj.items()}
    if isinstance(obj, list):
        return [normalized(v, stem, bindings) for v in obj]
    if isinstance(obj, str):
        return obj.replace(str(stem), '<independent-unused-stem>')
    return obj


def exclusive(path, obj):
    with Path(path).open('x') as handle:
        json.dump(obj, handle, ensure_ascii=False, indent=2, allow_nan=False)
        handle.write('\n')


def main():
    require(identity(PUB)['sha256'] ==
            '8fdc29cc861e59b1b4ae3dd2f3d75941ce56b212a9d5c7cb14476fc448571915',
            'Author publication changed')
    publication = read(PUB)
    require(publication['file_count'] == len(publication['files']) == 10, 'Wrong author publication count')
    for row in publication['files']:
        verify(row)
    require(sum(row['bytes'] for row in publication['files']) == publication['total_bytes'] == 173253,
            'Wrong author publication byte total')
    verify(publication['dependency_publication'])
    dependency = read(publication['dependency_publication']['path'])
    for row in dependency['files']:
        verify(row)
    record('author_publication_and_previously_reviewed_function_batch', files=10,
           dependency_files=len(dependency['files']))

    launches = [read(Path(str(stem) + '-launch.json')) for stem in (AUTHOR, REPLAY)]
    preparations = [read(Path(str(stem) + '-preparation.json')) for stem in (AUTHOR, REPLAY)]
    configs = [read(Path(str(stem) + '-tail-config.json')) for stem in (AUTHOR, REPLAY)]
    old = read(OLD)
    for launch in launches:
        require(len(launch['bindings']) == 117, 'Wrong new closure count')
        require(len({row['path'] for row in launch['bindings']}) == 117, 'Repeated source path')
        for row in launch['bindings']:
            verify(row)
        require(launch['schema'] == 'db6f-spectral-true-m14q512-release-lu-v1'
                and launch['status'] == 'PREPARED_NOT_STARTED', 'Wrong new launch identity/scope')
        require(len(launch['callbacks']) == 24, 'Wrong callback count')
        for row in launch['callbacks'].values():
            source_callback(row)
        for key in ('settings', 'weights', 'source_checkpoint', 'own_actual_tail_warm', 'frozen_physical_fields'):
            equal(launch[key], old[key], 'Changed original physical problem: ' + key)
        require(len(old['callbacks']) == 21, 'Wrong original callback count')
        for key, row in old['callbacks'].items():
            equal(launch['callbacks'][key], row, 'Changed original callback: ' + key)
        defs = launch['newton_lifetime_definitions']
        equal(defs['original_newton'], launch['callbacks']['domain_solve_newton'], 'Wrong original Newton metadata')
        equal(defs['derived_newton'], launch['callbacks']['selected_domain_solve_newton'], 'Wrong new Newton metadata')
        equal(defs['original_install'], launch['callbacks']['domain_install'], 'Wrong original install metadata')
        require(defs['statement_added'] == 'factor=None' and defs['installed'] is False
                and type(defs['solver_calls']) is int and defs['solver_calls'] == 0,
                'Pure definition metadata claims installation or computation')
    record('complete_source_closure_and_rederived_callbacks', bindings_per_launch=117, callbacks=24,
           unchanged_original_callbacks=21, added_identity_callbacks=3)

    normalized_launches, normalized_preparations, normalized_configs = [], [], []
    for stem, launch, preparation, config in zip((AUTHOR, REPLAY), launches, preparations, configs):
        config_path = Path(str(stem) + '-tail-config.json')
        launch_path = Path(str(stem) + '-launch.json')
        verify(launch['tail_config'])
        equal(preparation['tail_config'], identity(config_path), 'Preparation config binding differs')
        equal(preparation['launch'], identity(launch_path), 'Preparation launch binding differs')
        markers = {str(config_path): 'actual-config-verified', str(launch_path): 'actual-launch-verified'}
        normalized_configs.append(normalized(config, stem, {}))
        normalized_launch = normalized(launch, stem, markers)
        # The complete new-stem config binding changes its lexicographic
        # position in the path-sorted closure; order carries no source identity.
        normalized_launch['bindings'].sort(key=lambda row: json.dumps(row, sort_keys=True))
        normalized_launches.append(normalized_launch)
        normalized_preparations.append(normalized(preparation, stem, markers))
        require(all(type(v) is int and v == 0 for v in preparation['operations'].values()),
                'Unexpected pure-preparation operation counter')
        require(preparation['callback_definitions'] == 24 and preparation['bindings'] == 117,
                'Preparation counts differ')
    equal(*normalized_configs, 'Independent preparation changes non-path config')
    equal(*normalized_launches, 'Independent preparation changes launch beyond own I/O identities')
    equal(*normalized_preparations, 'Independent preparation result differs')
    expected_files = {Path(str(REPLAY) + suffix).resolve() for suffix in
                      ('-launch.json', '-tail-config.json', '-preparation.json')}
    require({p.resolve() for p in NOTES.glob(REPLAY.name + '*')} == expected_files,
            'Independent pure stem contains additional/future output')
    record('independent_real_preparation_equivalence', output_files=3,
           no_new_CP_PPoly_tail_reproduction_or_observation=True)

    original_runner = tree(HERE / 'db6f-prefix-spectral-true-m14.py')
    new_runner = tree(HERE / 'db6f-prefix-spectral-true-m14-release-lu.py')
    original_audit = tree(HERE / 'db6f-prefix-audit-spectral-true-m14.py')
    new_audit = tree(HERE / 'db6f-prefix-audit-spectral-true-m14-release-lu.py')
    unchanged = ['expected_config', 'expected_parser_argv', 'without_io', 'equal', 'module',
                 'write_json', 'runtime_callbacks']
    for name in unchanged:
        require(dump(find(original_runner, name)) == dump(find(new_runner, name)), 'Changed physical helper: ' + name)
    old_gate = copy.deepcopy(find(original_runner, 'runtime_newton'))
    old_gate.name = 'runtime_original_newton'
    require(dump(old_gate) == dump(find(new_runner, 'runtime_original_newton')), 'Original Newton gate was weakened')
    for name in ('check_packet', 'polynomial_endpoint', 'main'):
        require(dump(find(original_audit, name)) == dump(find(new_audit, name)), 'Changed old closed-data gate: ' + name)

    class IdentityStrings(ast.NodeTransformer):
        def visit_Constant(self, node):
            values = {'db6f-prefix-spectral-true-m14-release-lu.py': 'db6f-prefix-spectral-true-m14.py',
                      'PASS_LU_RELEASE_FINITE_M14_PROGRAM_OUTPUTS': 'PASS_ORIGINAL_FINITE_M14_PROGRAM_OUTPUTS'}
            if type(node.value) is str and node.value in values:
                node.value = values[node.value]
            return node

    for name in ('check_outputs', 'first_packet'):
        restored = IdentityStrings().visit(copy.deepcopy(find(new_audit, name)))
        require(dump(restored) == dump(find(original_audit, name)), 'Changed original finite output gate: ' + name)
    record('AST_original_numeric_gates', unchanged_helpers=7, original_Newton_gate_rename_only=True,
           unchanged_packet_polynomial_CLI=3, identity_only_output_first_packet=2)

    # This is a source-order check, not an invocation of any callback or factory.
    selected_nodes = [n for n in ast.walk(find(new_runner, 'main'))
                      if isinstance(n, ast.FunctionDef) and n.name == 'selected']
    require(len(selected_nodes) == 1, 'Missing or ambiguous actual selected wrapper')
    selected = selected_nodes[0]
    positions = {name: call_lines(selected, name) for name in
                 ('runtime_callbacks', 'select_runtime_newton', 'runtime_newton', 'selected_solver')}
    require(len(positions['runtime_callbacks']) == len(positions['select_runtime_newton']) ==
            len(positions['selected_solver']) == 1 and len(positions['runtime_newton']) == 2,
            'Unexpected selected wrapper call graph')
    before, after = sorted(positions['runtime_newton'])
    require(positions['runtime_callbacks'][0] < positions['select_runtime_newton'][0] < before
            < positions['selected_solver'][0] < after, 'Wrong callback/selection/identity order')
    tries = [n for n in ast.walk(selected) if isinstance(n, ast.Try) and n.finalbody]
    require(any(any(call_lines(n, 'runtime_newton') for n in t.finalbody) for t in tries),
            'Missing new runtime check in actual BVP finally')
    original_main = find(tree(launches[0]['callbacks']['original_main']['file']['path']), 'main')
    require(len(call_lines(original_main, 'install')) == 1 and
            call_lines(original_main, 'install')[0] < min(call_lines(original_main, 'solve_with_actual_tail')),
            'Original coupled install does not precede true outer solver')

    conjugacy = tree(HERE / 'db6f-root-spectral-collocation-v2.py')
    require(any(isinstance(n, ast.ImportFrom) and n.module == 'scipy.integrate'
                and any(a.name == 'solve_bvp' and a.asname == 'scipy_solve_bvp' for a in n.names)
                for n in conjugacy.body), 'W14 does not use the original SciPy solve_bvp function')
    require(len(call_lines(conjugacy, 'scipy_solve_bvp')) == 1, 'Unexpected W14 solver function capture')
    scipy_rows = [r for r in launches[0]['bindings'] if Path(r['path']).name == '_bvp.py']
    require(len(scipy_rows) == 1 and scipy_rows[0]['sha256'] ==
            '59afffb3607b272ae77f346d86428e43eca359fe90f2605da60a9571e60970d2', 'Wrong SciPy layout')
    solve_bvp = find(tree(scipy_rows[0]['path']), 'solve_bvp')
    require(len(call_lines(solve_bvp, 'solve_newton')) == 1 and
            not any(isinstance(n, ast.Name) and n.id == 'solve_newton' and isinstance(n.ctx, ast.Store)
                    for n in ast.walk(solve_bvp)) and
            not any(a.arg == 'solve_newton' for a in solve_bvp.args.args),
            'SciPy BVP does not resolve the selected Newton global at call time')
    record('runtime_source_order_and_SciPy_global_resolution',
           original_install_before_true_outer=True, physical_callbacks_before_selection=True,
           selected_identity_before_and_in_finally=True, solver_factory_execution=0)

    for name in ('2026-11-09-db6f-tail-review-newton-release-lu.md',
                 '2026-11-09-db6f-tail-review-newton-release-lu-publication.json'):
        identity(NOTES / name)
    identity(__file__)
    source_path = NOTES / (NAME + '-sources.json')
    exclusive(source_path, {'status': 'FROZEN_FULL_REVIEW_SOURCE_LEDGER', 'reviewer': REVIEWER,
                           'scope': 'Metadata/AST only; includes prepared input closures, no active run output.',
                           'bindings': sorted(sources.values(), key=lambda row: row['path']), 'count': len(sources)})
    output = NOTES / (NAME + '-check.json')
    result = {'status': 'PASS_INDEPENDENT_SOURCE_CLOSURE_AND_PURE_PREPARATION', 'reviewer': REVIEWER,
              'scope': __doc__, 'checks': checks, 'source_ledger': identity(source_path),
              'source_count': len(sources) - 1,
              'actual_numerical_calls': {'install': 0, 'select_newton': 0, 'BVP': 0, 'DN': 0,
                                         'RK': 0, 'flow': 0, 'full_Newton': 0},
              'G5': False, 'README_completed': False}
    exclusive(output, result)
    print(json.dumps({'status': result['status'], 'checks': len(checks), 'source_count': result['source_count'],
                      'report': identity(output), 'source_ledger': identity(source_path),
                      'actual_solver_calls': 0}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
