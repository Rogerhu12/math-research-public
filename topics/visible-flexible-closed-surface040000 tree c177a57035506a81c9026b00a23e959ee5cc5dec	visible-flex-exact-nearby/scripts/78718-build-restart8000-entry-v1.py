#!/usr/bin/env python3
"""Deterministic textual derivation of two separately named entry/audit sources.

Only source text/AST is read and written. No scientific module is imported.
Every old file remains unchanged. A complete unified diff is emitted for review.
"""
import argparse
import ast
import difflib
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def sha(data):
    return hashlib.sha256(data).hexdigest()


def replace(text, old, new):
    if text.count(old) != 1:
        raise ValueError('Expected one textual replacement: ' + old[:120])
    return text.replace(old, new, 1)


def function(text, name, replacement):
    nodes = [node for node in ast.parse(text).body
             if isinstance(node, ast.FunctionDef) and node.name == name]
    if len(nodes) != 1:
        raise ValueError('Ambiguous function: ' + name)
    node = nodes[0]
    lines = text.splitlines(keepends=True)
    return ''.join(lines[:node.lineno-1]) + replacement.rstrip() + '\n' + ''.join(lines[node.end_lineno:])


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--ledger', type=Path, required=True)
    p.add_argument('--diff', type=Path, required=True)
    a = p.parse_args()
    outputs = []
    old_driver = HERE / 'db6f-prefix-spectral-true-m14-direct-csc.py'
    old_auditor = HERE / 'db6f-prefix-audit-spectral-true-m14-direct-csc.py'
    originals = {path: path.read_bytes() for path in (old_driver, old_auditor)}
    old = originals[old_driver].decode()
    text = replace(old, 'HERE = Path(__file__).resolve().parent\nTOPIC = HERE.parent',
                   "NEW_HERE = Path(__file__).resolve().parent\nHERE = Path('/workspace/scratch/db6f0b0e7462/math-research/topics/visible-flexible-closed-surface/scripts')\nSOURCE_NOTES = HERE.parent / 'notes'\nTOPIC = NEW_HERE.parent")
    text = replace(text, "REFERENCE = NOTES / '2026-11-09-db6f-prefix-spectral-affine-m14q512-01-launch.json'",
                   "REFERENCE = SOURCE_NOTES / '2026-11-09-db6f-prefix-spectral-affine-m14q512-01-launch.json'")
    text = replace(text, "'flow_selector': (NOTES/'fixed_metric_mode3_bvp.py','SupportBVP.flow')",
                   "'flow_selector': (SOURCE_NOTES/'fixed_metric_mode3_bvp.py','SupportBVP.flow')")
    text = replace(text, "'max_nodes': 6500", "'max_nodes': 8000")
    text = replace(text, 'number, vector = h.number, h.vector',
                   "number, vector = h.number, h.vector\ni = module('restart8000_closed_input_definitions', NEW_HERE / '78718-prefix-restart8000-inputs-v1.py')\ntyped = module('restart8000_live_typed_code', NEW_HERE / '78718-canonical-runtime-code-v1.py')\nSCOPE = i.SCOPE\nrequire(SETTINGS == i.SETTINGS, 'New numerical policy differs from input gate')")
    text = function(text, 'expected_config', '''def expected_config(reference, out):
    original, ancestor = i.ancestor_context()
    equal(reference, ancestor['reference'], 'Changed original reference')
    return i.expected_config(original, ancestor, out)
''')
    text = function(text, 'expected_parser_argv', '''def expected_parser_argv(reference, config_path, out):
    _, ancestor = i.ancestor_context()
    equal(reference, ancestor['reference'], 'Changed original reference')
    return i.expected_argv(ancestor, config_path, out)
''')
    text = function(text, 'validate_inputs', '''def validate_inputs(launch, planned_config=None):
    """New explicit identity; the immutable ancestor validates itself first."""
    return i.validate(launch, planned_config=planned_config)
''')
    text = function(text, 'runtime_csc', '''def runtime_csc(context):
    selection = context.get('csc_selection')
    require(selection is not None, 'Explicit direct-CSC selection was not made')
    h.check_callback(type(selection).check, context['launch']['callbacks']['csc_runtime_check'])
    record = selection.check()
    equal(record['definitions'], context['launch']['csc_selection_definitions'],
          'Runtime CSC source identity differs')
    equal(record['prerequisite_inputs'], context['csc_prerequisites']['inputs'],
          'Runtime CSC prerequisite identity differs')
    return {'schema': '78718-direct-csc-typed-runtime-envelope-v1',
            'raw': record, 'canonical_functions': typed.capture_selection(selection, record)}


def restore_runtime_csc(context):
    """Retain the original restoration record plus actual typed before/after."""
    selection = context['csc_selection']
    before = runtime_csc(context)
    raw = selection.restore()
    equal(raw['before_restore'], before['raw'], 'Original restoration changed its before record')
    after = typed.capture_selection(selection, raw['before_restore'])
    equal(after, before['canonical_functions'], 'Typed code identity changed during restoration')
    return {'schema': '78718-direct-csc-typed-restoration-envelope-v1',
            'raw': raw, 'before_restore': before, 'canonical_after_restore': after}
''')
    text = replace(text, "'schema': 'db6f-spectral-true-m14-direct-csc-program-record-v1'",
                   "'schema': i.PROGRAM_SCHEMA")
    text = replace(text, "HERE / 'db6f-prefix-audit-spectral-true-m14-direct-csc.py'",
                   "NEW_HERE / '78718-prefix-audit-restart8000-v1.py'")
    text = replace(text, "manifest['csc_restoration'] = selection.restore()",
                   "manifest['csc_restoration'] = restore_runtime_csc(context)")
    text = text.replace('DIRECT_CSC_FINITE_M14_COUPLED_PROGRAM_SUCCESS', 'RESTART8000_FINITE_M14_COUPLED_PROGRAM_SUCCESS')
    text = text.replace('DIRECT_CSC_FINITE_M14_COUPLED_PROGRAM_FAILURE', 'RESTART8000_FINITE_M14_COUPLED_PROGRAM_FAILURE')
    text = text.replace('"""Explicit direct-CSC / release-LU variant of the actual-DN M14 W14 runner.',
                        '"""New restart8000 / typed-code identity of the actual-DN M14 W14 runner.')
    outputs.append((old_driver, HERE / '78718-prefix-spectral-restart8000-v1.py', text))

    old = originals[old_auditor].decode()
    if old.count("HERE / 'db6f-prefix-spectral-true-m14-direct-csc.py'") != 2:
        raise ValueError('Changed original auditor driver references')
    text = old.replace("HERE / 'db6f-prefix-spectral-true-m14-direct-csc.py'",
                        "HERE / '78718-prefix-spectral-restart8000-v1.py'")
    text = replace(text, '2 <= n <= 6500', "2 <= n <= c.SETTINGS['max_nodes']")
    text = replace(text, "('maximum_nodes',6500)", "('maximum_nodes',c.SETTINGS['max_nodes'])")
    text = replace(text, "2 <= record['initial_nodes'] <= 6500", "2 <= record['initial_nodes'] <= c.SETTINGS['max_nodes']")
    text = replace(text, "2 <= record['final_nodes'] <= 6500", "2 <= record['final_nodes'] <= c.SETTINGS['max_nodes']")
    text = function(text, '_compiled_runtime_record', '''def _compiled_runtime_record(row, path, qualname, module, typed_row):
    """Compile pinned text and compare complete typed code; keep raw evidence."""
    gate = c.module('closed_csc_identity_gate', c.CSC_GATES)
    gate.runtime_function_record(row)
    c.typed.check_record(typed_row, row, path, qualname, module)
''')
    text = replace(text, 'def check_csc_runtime_record(record, context):\n    keys =',
                   "def check_csc_runtime_record(envelope, context):\n    require(type(envelope) is dict and set(envelope) == {'schema', 'raw', 'canonical_functions'}\n            and envelope['schema'] == '78718-direct-csc-typed-runtime-envelope-v1',\n            'Missing new typed-code runtime envelope')\n    record = envelope['raw']; typed_rows = envelope['canonical_functions']\n    require(type(typed_rows) is dict and set(typed_rows) == {\n        'original.prepare_sys', 'original.construct_global_jac', 'original.compute_jac_indices',\n        'original.solve_bvp', 'foundation.dimensions', 'foundation.column_segments',\n        'foundation._assemble_csc', 'selected.prepare_sys', 'selected.construct_global_jac',\n        'newton.solve_newton'}, 'Incomplete complete typed-code closure')\n    keys =")
    text = replace(text, "_compiled_runtime_record(row,bvp_path,name,'scipy.integrate._bvp')",
                   "_compiled_runtime_record(row,bvp_path,name,'scipy.integrate._bvp',typed_rows['original.'+name])")
    text = replace(text, "_compiled_runtime_record(row,c.CSC_FOUNDATION,name,gate.RUNTIME_MODULE)",
                   "_compiled_runtime_record(row,c.CSC_FOUNDATION,name,gate.RUNTIME_MODULE,typed_rows['foundation.'+name])")
    text = replace(text, "_compiled_runtime_record(row,c.CSC_FOUNDATION,'make_functions.<locals>.'+name,gate.RUNTIME_MODULE)",
                   "_compiled_runtime_record(row,c.CSC_FOUNDATION,'make_functions.<locals>.'+name,gate.RUNTIME_MODULE,typed_rows['selected.'+name])")
    text = replace(text, "'solve_newton','db6f_lu_lifetime_selected_definition_v1')",
                   "'solve_newton','db6f_lu_lifetime_selected_definition_v1',typed_rows['newton.solve_newton'])")
    text = function(text, 'check_csc_restoration', '''def check_csc_restoration(envelope, context):
    require(type(envelope) is dict and set(envelope) ==
            {'schema', 'raw', 'before_restore', 'canonical_after_restore'}
            and envelope['schema'] == '78718-direct-csc-typed-restoration-envelope-v1',
            'Missing typed original-prepare restoration')
    record = envelope['raw']
    require(type(record) is dict and set(record) ==
            {'schema','before_restore','restored_original_prepare','newton_runtime_unchanged',
             'backend_prepare_restored','scope'}
            and record['schema'] == 'db6f-explicit-direct-csc-restoration-v1',
            'Missing original unmodified restoration record')
    check_csc_runtime_record(envelope['before_restore'], context)
    equal(record['before_restore'], envelope['before_restore']['raw'],
          'Original raw restoration record is detached from typed identity')
    equal(envelope['canonical_after_restore'], envelope['before_restore']['canonical_functions'],
          'Typed code identity changed during restoration')
    equal(record['restored_original_prepare'],
          record['before_restore']['original_runtime']['prepare_sys'],
          'Restored prepare is not the original function')
    equal(record['newton_runtime_unchanged'], record['before_restore']['newton_runtime_unchanged'],
          'Restoration changed the separately selected Newton')
    require(record['backend_prepare_restored'] is True and type(record['scope']) is str,
            'Original prepare restoration did not pass')
''')
    text = replace(text, "equal(repro['schema'],'db6f-spectral-true-m14-direct-csc-program-record-v1',",
                   "equal(repro['schema'],c.i.PROGRAM_SCHEMA,")
    text = text.replace('DIRECT_CSC_FINITE_M14_COUPLED_PROGRAM_SUCCESS', 'RESTART8000_FINITE_M14_COUPLED_PROGRAM_SUCCESS')
    text = text.replace('PASS_DIRECT_CSC_FINITE_M14_PROGRAM_OUTPUTS', 'PASS_RESTART8000_FINITE_M14_PROGRAM_OUTPUTS')
    text = text.replace('PASS_ROOT_OBSERVED_TRUE_M14_W14_DIRECT_CSC_FINITE_COUPLED_CLOSE',
                        'PASS_ROOT_OBSERVED_RESTART8000_M14_W14_FINITE_COUPLED_CLOSE')
    text = text.replace('"""Read-only close audit for the explicit direct-CSC/release-LU true M14 entry.',
                        '"""New read-only close audit for restart8000 and complete typed runtime code.')
    outputs.append((old_auditor, HERE / '78718-prefix-audit-restart8000-v1.py', text))

    expected = {old_driver.name: 'b6fd772b5f44819186fc7e31af370ffa199bfa5c9b14a2722b36345bcf26cd24',
                old_auditor.name: 'b6222f3394c53eebd8409c922ed2e009de85b4bcdbfa5a6e8c8d57b2294967e0'}
    records = []
    diffs = []
    for source, output, text in outputs:
        data = text.encode()
        compile(data, str(output), 'exec', dont_inherit=True)
        if expected[source.name].startswith('TO_BE_'):
            raise ValueError('Freeze the actual original whole-file hashes before deriving')
        if sha(originals[source]) != expected[source.name]:
            raise ValueError('Changed old derivation source')
        if output.exists() and output.read_bytes() != data:
            raise FileExistsError(output)
        if not output.exists():
            with output.open('xb') as stream:
                stream.write(data)
        records.append({'source': str(source), 'source_bytes': len(originals[source]),
                        'source_sha256': sha(originals[source]), 'output': str(output),
                        'output_bytes': len(data), 'output_sha256': sha(data)})
        diffs.extend(difflib.unified_diff(originals[source].decode().splitlines(True), text.splitlines(True),
                                         fromfile=source.name, tofile=output.name))
    ledger = {'schema': '78718-restart8000-explicit-source-derivation-v1',
              'generator_sha256': sha(Path(__file__).read_bytes()), 'files': records,
              'old_sources_modified': False, 'source_compilation_only': True,
              'mathematical_functions_executed': 0}
    for path, data in ((a.ledger, (json.dumps(ledger, indent=2)+'\n').encode()),
                       (a.diff, ''.join(diffs).encode())):
        if len(data) >= 100_000:
            raise ValueError('Review text too large')
        if path.exists() and path.read_bytes() != data:
            raise FileExistsError(path)
        if not path.exists():
            with path.open('xb') as stream:
                stream.write(data)
    print(json.dumps({'status': 'DERIVED_SOURCE_ONLY_NOT_READY_FOR_SOLVER', 'files': len(records),
                      'ledger_bytes': a.ledger.stat().st_size, 'diff_bytes': a.diff.stat().st_size,
                      'solver_calls': 0}))


if __name__ == '__main__':
    main()
