#!/usr/bin/env python3
"""Pure source/input check for the conditional storage planner; no candidate argv."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
NOTES = HERE.parent / 'notes'
PYTHON = '/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python'
PLANNER = HERE / '78718-plan-post-m15-linear-storage-v1.py'
PLANNER_SHA = '4cd5386249e57e2f033638acf8e92f931aa6a3d1fe559496ba16d82b920211df'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if sys.executable != PYTHON:
        raise ValueError('Use the absolute frozen primary Python')
    if args.out.resolve().parent != NOTES.resolve() or args.out.exists():
        raise ValueError('Require a new immediate notes output')
    source = PLANNER.read_bytes()
    if hashlib.sha256(source).hexdigest() != PLANNER_SHA:
        raise ValueError('Changed frozen conditional storage planner')
    compile(source, str(PLANNER), 'exec', dont_inherit=True)
    spec = importlib.util.spec_from_file_location('checked_post_storage_v2', PLANNER)
    planner = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = planner
    spec.loader.exec_module(planner)
    base = planner.load_base()
    fixed = base.verify_fixed_inputs()
    storage = planner.verify_storage_inputs(base)
    bindings = base.Bindings()
    for group in (fixed['bindings'], storage['bindings']):
        for row in group:
            for role in row['roles']:
                bindings.bound(row, role)
    bindings.add(PLANNER, 'new-conditional-storage-plan', PLANNER_SHA)
    bindings.add(Path(__file__), 'this-pure-static-checker')
    names = storage['original_literal_command_sources']
    rows = {row['path']: row for row in bindings.output()}
    for name in names:
        path = str(HERE / name)
        if path not in rows:
            raise ValueError('Unbound original command source: ' + name)
    loaded_numerical = sorted(name for name in sys.modules
                              if name.split('.')[0] in ('numpy', 'scipy'))
    if loaded_numerical:
        raise ValueError('Unexpected numerical import in pure metadata check')
    report = {
        'schema': '78718-post-m15-linear-storage-v1-static-input-check-v1',
        'status': 'PASS_SOURCE_INPUT_CLOSURE_ONLY_NO_CANDIDATE_ARGV',
        'scope': __doc__, 'plan_ready': False,
        'planner': base.identity(PLANNER), 'checker': base.identity(__file__),
        'original_planner': base.pinned(HERE / planner.BASE_NAME, planner.BASE_SHA),
        'original_fixed_binding_count': len(fixed['bindings']),
        'storage_binding_count': len(storage['bindings']),
        'unique_preexisting_binding_count': len(bindings.output()),
        'preexisting_bindings': bindings.output(),
        'storage_source_count': storage['storage_source_count'],
        'command_file_substitution_count': storage['command_file_substitution_count'],
        'command_file_substitutions': storage['substitutions'],
        'original_literal_command_sources': names,
        'terminal_prefix_pin_count': storage['terminal_prefix_pin_count'],
        'original_terminal_pin_count': storage['original_terminal_pin_count'],
        'angular_pin_count': storage['angular_pin_count'],
        'terminal_reference_and_bound_AST_unchanged': True,
        'mesh_reviewer_exporter_pin_verified': True,
        'terminal_reference_ready': fixed['terminal_reference_ready'],
        'terminal_reference_missing_count': sum(not row['present']
                                                 for row in fixed['terminal_reference_objects']),
        'terminal_reference_unknown_descendant_count': len(fixed['terminal_reference_unknown_descendants']),
        'numpy_or_scipy_imported': False, 'adapter_imports': 0,
        'actual_solver_calls': 0, 'actual_production_calls': 0,
        'complete_final_audit_replayed': False, 'successful_main_claimed': False,
        'candidate_argv_constructed': False, 'production_commands_emitted': 0,
        'storage_branch_selected_or_activated': False,
        'production_directory_created': False,
    }
    payload = (json.dumps(report, indent=2, ensure_ascii=False, allow_nan=False) + '\n').encode()
    if len(payload) >= 100_000:
        raise ValueError('Unexpectedly large static metadata report')
    with args.out.open('xb') as stream:
        stream.write(payload)
    print(json.dumps({key: report[key] for key in (
        'status', 'original_fixed_binding_count', 'storage_binding_count',
        'unique_preexisting_binding_count', 'storage_source_count',
        'command_file_substitution_count', 'terminal_reference_ready',
        'actual_solver_calls', 'actual_production_calls', 'production_commands_emitted')}
        | {'output': base.identity(args.out)}))
    return 0


if __name__ == '__main__':
    sys.exit(main())
