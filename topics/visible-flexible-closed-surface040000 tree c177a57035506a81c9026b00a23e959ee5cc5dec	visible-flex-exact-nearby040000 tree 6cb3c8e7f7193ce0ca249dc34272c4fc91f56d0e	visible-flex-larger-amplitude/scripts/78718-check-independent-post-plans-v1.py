#!/usr/bin/env python3
"""Check independent post-plan source derivation and static inputs; no candidate argv."""
import argparse
import ast
import difflib
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
NOTES = HERE.parent / 'notes'
PYTHON = '/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python'
BASE = HERE / '78718-plan-post-independent-seed8000-v1.py'
BASE_SHA = 'b3526176d56179a3edce6a71a159591a1e9f5ceecd9d253a4eeec95887e07053'
STORAGE = HERE / '78718-plan-post-independent-seed8000-storage-v2.py'
STORAGE_SHA = 'c94d7b8204ad8184a181fc6d8b4b9b495f3dd0d9fdf3609f6ea23168ed4fc223'
LEDGER = NOTES / '2026-11-10-78718-numerical-independent-post-plans-derivation-01.json'
LEDGER_SHA = 'c85e5953bfb4298c765c59e4e03fa9a1a13b938e4cebaa2b56957fc10dbf13ac'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    sys.modules[name] = result
    spec.loader.exec_module(result)
    return result


def function_asts(text):
    return {node.name: ast.dump(node, annotate_fields=True, include_attributes=False)
            for node in ast.parse(text).body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    require(sys.executable == PYTHON, 'Use the absolute frozen primary Python')
    require(args.out.resolve().parent == NOTES.resolve() and not args.out.exists(),
            'Require a new immediate notes output')
    require(sha(BASE) == BASE_SHA and sha(STORAGE) == STORAGE_SHA and sha(LEDGER) == LEDGER_SHA,
            'Changed independent planner or derivation ledger')
    base = module('checked_independent_original_postplan', BASE)
    storage = module('checked_independent_storage_postplan', STORAGE)
    ledger = base.read_json(LEDGER)
    bindings = base.Bindings()
    bindings.add(LEDGER, 'complete-exact-source-derivation', LEDGER_SHA)
    for key in ('builder', 'independent_final_auditor', 'independent_entry_complete_review', 'full_diff'):
        bindings.bound(ledger[key], 'derivation:' + key)
    require(len(ledger['plans']) == 2, 'Expected exactly two independently named plans')
    changes = []
    diffs = []
    for row in ledger['plans']:
        bindings.bound(row['old'], 'frozen-root-plan-ancestor')
        bindings.bound(row['new'], 'derived-independent-post-plan')
        original = Path(row['old']['path']).read_text()
        reconstructed = original
        for index, change in enumerate(row['replacements']):
            require(change['index'] == index and change['exact_match_count'] == 1
                    and reconstructed.count(change['old_text']) == 1,
                    'Source replacement not unique or ordered')
            reconstructed = reconstructed.replace(change['old_text'], change['new_text'], 1)
        actual = Path(row['new']['path']).read_text()
        require(reconstructed == actual, 'Independent source differs from exact declared replacements')
        compile(actual, row['new']['path'], 'exec', dont_inherit=True)
        old_funcs, new_funcs = function_asts(original), function_asts(actual)
        require(old_funcs.keys() == new_funcs.keys(), 'Changed complete function set')
        unchanged = sorted(name for name in old_funcs if old_funcs[name] == new_funcs[name])
        changed = sorted(set(old_funcs) - set(unchanged))
        base.same(unchanged, row['exact_AST_unchanged_functions'], 'Wrong unchanged function record')
        base.same(changed, row['identity_string_changes_only_in_functions'], 'Unexpected changed function')
        require(set(row['explicit_preserved_route_functions']) <= set(unchanged),
                'A fixed mathematical route function changed')
        diffs.append(''.join(difflib.unified_diff(original.splitlines(keepends=True), actual.splitlines(keepends=True),
                                                fromfile=Path(row['old']['path']).name,
                                                tofile=Path(row['new']['path']).name)))
        changes.append({'old': row['old'], 'new': row['new'],
                        'unique_exact_replacements': len(row['replacements']),
                        'unchanged_functions': unchanged, 'changed_identity_functions': changed,
                        'preserved_route_functions': row['explicit_preserved_route_functions']})
    require((diffs[0] + '\n' + diffs[1]).encode() == Path(ledger['full_diff']['path']).read_bytes(),
            'Complete two-source diff differs')
    require(base.AUDITOR.name == '78718-prefix-audit-independent-seed8000-v1.py'
            and base.AUDITOR_SHA == '067f8944cb0d75ceffc846119b1ca2511f0e6e886799258e4659b023d8828578',
            'Wrong independent full auditor')
    bindings.add(base.AUDITOR, 'complete-independent-final-auditor', base.AUDITOR_SHA)
    require(base.LAUNCH_SCHEMA == '78718-true-m14-w14-independent-seed8000-launch-v1'
            and base.SUCCESS == 'PASS_INDEPENDENT_OBSERVED_SEED8000_M14_W14_FINITE_COUPLED_CLOSE',
            'Wrong independent main identity')
    require(storage.BASE_NAME == BASE.name and storage.BASE_SHA == BASE_SHA,
            'Storage wrapper is detached from the independent base')
    fixed = base.verify_fixed_inputs()
    storage_inputs = storage.verify_storage_inputs(base)
    for group in (fixed['bindings'], storage_inputs['bindings']):
        for row in group:
            for role in row['roles']:
                bindings.bound(row, role)
    bindings.add(STORAGE, 'conditional-independent-storage-planner', STORAGE_SHA)
    bindings.add(Path(__file__), 'this-pure-source-input-checker')
    source_paths = {row['path'] for row in bindings.output()}
    for name in storage_inputs['original_literal_command_sources']:
        require(str(HERE / name) in source_paths, 'Unbound original backend source: ' + name)
    require(not any(name.split('.')[0] in ('numpy', 'scipy') for name in sys.modules),
            'Unexpected mathematical backend import')
    report = {
        'schema': '78718-independent-post-plans-source-input-check-v1',
        'status': 'PASS_INDEPENDENT_PLAN_SOURCE_AND_STATIC_INPUTS_ONLY',
        'scope': __doc__, 'plan_ready': False,
        'checker': base.identity(__file__), 'source_replay': changes,
        'original_plan': base.identity(BASE), 'conditional_storage_plan': base.identity(STORAGE),
        'expected_actor': '/root/independent_audit',
        'expected_launch_schema': base.LAUNCH_SCHEMA, 'expected_complete_final_status': base.SUCCESS,
        'expected_final_observation_field': 'independent_observation',
        'original_fixed_binding_count': len(fixed['bindings']),
        'storage_binding_count': len(storage_inputs['bindings']),
        'unique_preexisting_binding_count': len(bindings.output()),
        'preexisting_bindings': bindings.output(),
        'storage_source_count': storage_inputs['storage_source_count'],
        'command_file_substitution_count': storage_inputs['command_file_substitution_count'],
        'original_literal_command_sources': storage_inputs['original_literal_command_sources'],
        'terminal_prefix_pin_count': storage_inputs['terminal_prefix_pin_count'],
        'original_terminal_pin_count': storage_inputs['original_terminal_pin_count'],
        'angular_pin_count': storage_inputs['angular_pin_count'],
        'terminal_reference_and_bound_AST_unchanged': True,
        'mesh_reviewer_exporter_pin_verified': True,
        'terminal_reference_ready': fixed['terminal_reference_ready'],
        'terminal_reference_missing_count': sum(not row['present']
                                                 for row in fixed['terminal_reference_objects']),
        'terminal_reference_unknown_descendant_count': len(fixed['terminal_reference_unknown_descendants']),
        'root_only_source_globals_modified': False,
        'numpy_or_scipy_imported': False, 'adapter_imports': 0,
        'actual_solver_calls': 0, 'actual_production_calls': 0,
        'complete_final_audit_replayed': False, 'successful_main_claimed': False,
        'candidate_argv_constructed': False, 'production_commands_emitted': 0,
        'storage_branch_selected_or_activated': False, 'production_directory_created': False,
    }
    payload = (json.dumps(report, indent=2, ensure_ascii=False, allow_nan=False) + '\n').encode()
    require(len(payload) < 100_000, 'Unexpectedly large static metadata report')
    with args.out.open('xb') as stream:
        stream.write(payload)
    print(json.dumps({key: report[key] for key in (
        'status', 'original_fixed_binding_count', 'storage_binding_count',
        'unique_preexisting_binding_count', 'storage_source_count', 'command_file_substitution_count',
        'terminal_reference_ready', 'actual_solver_calls', 'actual_production_calls',
        'production_commands_emitted')} | {'output': base.identity(args.out)}))
    return 0


if __name__ == '__main__':
    sys.exit(main())
