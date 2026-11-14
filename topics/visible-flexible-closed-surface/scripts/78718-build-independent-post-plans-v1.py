#!/usr/bin/env python3
"""Derive separately named independent-actor post plans from frozen exact text.

This builder reads/writes source and provenance only. It does not import any
planner, auditor, solver, numerical backend or storage adapter.
"""
import argparse
import ast
import difflib
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
NOTES = HERE.parent / 'notes'
BASE_OLD = '78718-plan-post-restart8000-v1.py'
BASE_SHA = 'c6ef233eb40517bf1986b3ea25d0bb31d102d4b219727c6d69a97b38ee1e0456'
BASE_NEW = '78718-plan-post-independent-seed8000-v1.py'
STORAGE_OLD = '78718-plan-post-restart8000-storage-v2.py'
STORAGE_SHA = '99c053a1563a31c94de2b2d9b99db70aad603c2bafa89f023abc69800748badc'
STORAGE_NEW = '78718-plan-post-independent-seed8000-storage-v2.py'
AUDITOR = '78718-prefix-audit-independent-seed8000-v1.py'
AUDITOR_SHA = '067f8944cb0d75ceffc846119b1ca2511f0e6e886799258e4659b023d8828578'
ENTRY_REVIEW = '2026-11-10-78718-audit-independent-seed8000-entry-v1.md'
ENTRY_REVIEW_SHA = '4bf8d07536b0df21f824bf06ba753af3905d6db252744b46b58fadf0aeeff9e3'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def identity(path):
    path = Path(path).resolve()
    data = path.read_bytes()
    return {'path': str(path), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def source(path, digest):
    data = Path(path).read_bytes()
    require(hashlib.sha256(data).hexdigest() == digest, 'Changed frozen source: ' + str(path))
    return data.decode('utf-8')


def base_replacements():
    return [
        ('Read-only, success-only command plan for the original post-restart8000 chain.',
         'Read-only, success-only original-family plan after independent published-M14 seed8000.'),
        ("and root's actual successful tool-exit observation, hashes pre-existing inputs,",
         "and /root/independent_audit's actual successful tool-exit observation, hashes pre-existing inputs,"),
        ('The separately named byte-storage family remains outside this frozen v1 plan.',
         'The separately named independent byte-storage plan remains outside this frozen v1 plan.'),
        ("AUDITOR = HERE / '78718-prefix-audit-restart8000-v1.py'",
         "AUDITOR = HERE / '78718-prefix-audit-independent-seed8000-v1.py'"),
        ("AUDITOR_SHA = 'cd090888e4552317bce183c3b5788710ced9e17eea965b9489252e96d2f3496f'",
         "AUDITOR_SHA = '" + AUDITOR_SHA + "'"),
        ("LAUNCH_SCHEMA = '78718-true-m14-w14-restart8000-launch-v1'",
         "LAUNCH_SCHEMA = '78718-true-m14-w14-independent-seed8000-launch-v1'"),
        ("SUCCESS = 'PASS_ROOT_OBSERVED_RESTART8000_M14_W14_FINITE_COUPLED_CLOSE'",
         "SUCCESS = 'PASS_INDEPENDENT_OBSERVED_SEED8000_M14_W14_FINITE_COUPLED_CLOSE'"),
        ("module('post_restart8000_full_close_audit', AUDITOR)",
         "module('post_independent_seed8000_full_close_audit', AUDITOR)"),
        ("'Not the restart8000 launch schema'", "'Not the independent seed8000 launch schema'"),
        ("run.name.startswith('2026-11-10-78718-')",
         "run.name.startswith('2026-11-10-78718-independent-post-seed8000-')"),
        ("'Use a separately named immediate notes subdirectory'",
         "'Use the separately named independent-post-seed8000 immediate notes subdirectory'"),
        ("bindings.bound(final['root_observation'], 'actual-success-root-observation')",
         "bindings.bound(final['independent_observation'], 'actual-success-independent-observation')"),
        ("(args.observed_execution, 'actual-root-success-observation')",
         "(args.observed_execution, 'actual-independent-success-observation')"),
        ("'schema': '78718-post-restart8000-success-only-original-plan-v1'",
         "'schema': '78718-post-independent-seed8000-success-only-original-plan-v1'"),
        ("'status': 'ACTUAL_MAIN_SUCCESS_BOUND_FUTURE_PRODUCTION_PLAN_ONLY'",
         "'status': 'ACTUAL_INDEPENDENT_MAIN_SUCCESS_BOUND_FUTURE_PRODUCTION_PLAN_ONLY'"),
        ("'root_actual_exit_observation': identity(args.observed_execution)",
         "'independent_actual_exit_observation': identity(args.observed_execution)"),
        ("'The restart8000 ancestor failed CP is a declared true input, not an independent final rerun performed here.'",
         "'The published M14 seed and its own tail are the declared solver inputs; this plan does not execute or fabricate the independently observed solver run.'"),
    ]


def storage_replacements(base_digest):
    return [
        ('Success-only conditional storage plan, separate from frozen original plan-v1.',
         'Success-only conditional storage plan after independent published-M14 seed8000.'),
        ('The original complete main exit audit runs unchanged through the pinned parent\nplanner.',
         'The complete independent-actor main exit audit runs unchanged through the pinned\nindependent original-family planner.'),
        ("BASE_NAME = '" + BASE_OLD + "'", "BASE_NAME = '" + BASE_NEW + "'"),
        ("BASE_SHA = '" + BASE_SHA + "'", "BASE_SHA = '" + base_digest + "'"),
        ("'storage_v2_original_plan'", "'independent_storage_v2_original_plan'"),
        ("'Changed frozen original success-only planner'",
         "'Changed frozen independent success-only planner'"),
        ("'2026-11-10-78718-post-restart8000-storage-v2-'",
         "'2026-11-10-78718-independent-post-seed8000-storage-v2-'"),
        ("'Use the distinct post-restart8000-storage-v2 production namespace'",
         "'Use the distinct independent-post-seed8000-storage-v2 production namespace'"),
        ('# exact frozen call demands the genuine root exit and complete final report.',
         '# exact frozen call demands the genuine independent exit and complete final report.'),
        ("'78718-post-restart8000-success-only-conditional-storage-plan-v2'",
         "'78718-post-independent-seed8000-success-only-conditional-storage-plan-v2'"),
        ("'ACTUAL_MAIN_SUCCESS_BOUND_CONDITIONAL_STORAGE_PLAN_ONLY'",
         "'ACTUAL_INDEPENDENT_MAIN_SUCCESS_BOUND_CONDITIONAL_STORAGE_PLAN_ONLY'"),
    ]


def functions(text):
    tree = ast.parse(text)
    return {node.name: ast.dump(node, annotate_fields=True, include_attributes=False)
            for node in tree.body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))}


def derive(old, digest, new, replacements, unchanged_required, changed_expected):
    before = source(HERE / old, digest)
    after = before
    ledger = []
    for index, (left, right) in enumerate(replacements):
        count = after.count(left)
        require(count == 1, f'{old} replacement {index} has {count} matches')
        require(left != right, 'Empty source transformation')
        after = after.replace(left, right, 1)
        ledger.append({'index': index, 'old_text': left, 'new_text': right, 'exact_match_count': count})
    compile(after, str(HERE / new), 'exec', dont_inherit=True)
    old_functions, new_functions = functions(before), functions(after)
    require(old_functions.keys() == new_functions.keys(), 'Function set changed')
    changed = sorted(name for name in old_functions if old_functions[name] != new_functions[name])
    require(changed == sorted(changed_expected), 'Unexpected function AST changes: ' + str(changed))
    for name in unchanged_required:
        require(old_functions[name] == new_functions[name], 'Changed mathematical route function: ' + name)
    data = after.encode('utf-8')
    row = {'old': identity(HERE / old),
           'new': {'path': str((HERE / new).resolve()), 'bytes': len(data),
                   'sha256': hashlib.sha256(data).hexdigest()},
           'replacements': ledger,
           'exact_AST_unchanged_functions': sorted(set(old_functions) - set(changed)),
           'identity_string_changes_only_in_functions': changed,
           'explicit_preserved_route_functions': list(unchanged_required)}
    diff = ''.join(difflib.unified_diff(before.splitlines(keepends=True), after.splitlines(keepends=True),
                                      fromfile=old, tofile=new))
    return data, row, diff


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ledger', type=Path, required=True)
    parser.add_argument('--diff', type=Path, required=True)
    args = parser.parse_args()
    require(not args.ledger.exists() and not args.diff.exists(), 'New provenance files required')
    require(args.ledger.resolve().parent == NOTES.resolve() and args.diff.resolve().parent == NOTES.resolve(),
            'Provenance must be immediate notes files')
    source(HERE / AUDITOR, AUDITOR_SHA)
    source(NOTES / ENTRY_REVIEW, ENTRY_REVIEW_SHA)
    base_data, base_row, base_diff = derive(
        BASE_OLD, BASE_SHA, BASE_NEW, base_replacements(),
        ('verify_fixed_inputs', 'command_plan'), ('audited_success', 'build'))
    storage_data, storage_row, storage_diff = derive(
        STORAGE_OLD, STORAGE_SHA, STORAGE_NEW, storage_replacements(base_row['new']['sha256']),
        ('verify_storage_inputs', 'replace_command_records', 'static_command_names'), ('load_base', 'build'))
    outputs = [(HERE / BASE_NEW, base_data), (HERE / STORAGE_NEW, storage_data)]
    for path, data in outputs:
        require(not path.exists() or path.read_bytes() == data, 'Refusing to replace differing source: ' + str(path))
    diff_bytes = (base_diff + '\n' + storage_diff).encode('utf-8')
    require(len(diff_bytes) < 100_000, 'Unexpectedly large two-plan complete diff')
    for path, data in outputs:
        if not path.exists():
            with path.open('xb') as stream:
                stream.write(data)
    with args.diff.open('xb') as stream:
        stream.write(diff_bytes)
    report = {'schema': '78718-independent-post-plans-exact-source-derivation-v1',
              'status': 'SOURCE_ONLY_DERIVATION_NOT_SUCCESSFUL_CANDIDATE',
              'builder': identity(__file__), 'independent_final_auditor': identity(HERE / AUDITOR),
              'independent_entry_complete_review': identity(NOTES / ENTRY_REVIEW),
              'plans': [base_row, storage_row], 'full_diff': identity(args.diff),
              'actual_solver_calls': 0, 'actual_production_calls': 0, 'planner_imports': 0,
              'numerical_backend_imports': 0, 'candidate_argv_constructed': False,
              'root_only_source_globals_modified': False,
              'source_ancestors_unchanged': [identity(HERE / BASE_OLD), identity(HERE / STORAGE_OLD)]}
    payload = (json.dumps(report, indent=2, ensure_ascii=False, allow_nan=False) + '\n').encode('utf-8')
    require(len(payload) < 100_000, 'Unexpectedly large exact transformation ledger')
    with args.ledger.open('xb') as stream:
        stream.write(payload)
    source(HERE / BASE_OLD, BASE_SHA)
    source(HERE / STORAGE_OLD, STORAGE_SHA)
    print(json.dumps({'status': report['status'], 'outputs': [identity(path) for path, _ in outputs],
                      'replacement_counts': [len(row['replacements']) for row in report['plans']],
                      'ledger': identity(args.ledger), 'diff': identity(args.diff),
                      'actual_solver_calls': 0, 'actual_production_calls': 0}))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
