#!/usr/bin/env python3
"""Success-only conditional storage plan, separate from frozen original plan-v1.

The original complete main exit audit runs unchanged through the pinned parent
planner. This file only substitutes the fully reviewed prefix storage family in
the resulting future argv/source records. It executes no command, producer,
solver, physical callback or storage writer. It does not select the storage
branch: the original single-container route remains the first actual route.
"""
import argparse
import ast
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
NOTES = HERE.parent / 'notes'
BASE_NAME = '78718-plan-post-restart8000-v1.py'
BASE_SHA = 'c6ef233eb40517bf1986b3ea25d0bb31d102d4b219727c6d69a97b38ee1e0456'
FAMILY = {
    '78718-prefix-byte-shards-v1.py': 'e23153ae6b364854a24acc464be97921b134f7e25024e82c8c91995ca2f96f39',
    '78718-prefix-storage-v1.py': '83cf59cfe5ab373421e53d0c0d8d2274edfc6a6b266fc2ab6161274b474a4329',
    '78718-prefix-fullxyz-hermite-storage-v1.py': '2ab813fba7d3a33ef273799a4f6d27628b9cc2f98285fb3d3371fdacb49b009d',
    '78718-prefix-mirror-hermite-storage-v1.py': 'f975ab40ca05f5237954398533934eda2365ceda38cb0ba4dfe8d9e3287f6957',
    '78718-prefix-continuous-hermite-storage-v1.py': '09e8c748c7cc49347876d849029e835a8cd0e5f097d36eaf6cf2fd7c0f2ddc18',
    '78718-prefix-metric-polynomial-storage-v1.py': 'd290543f75224509fef8287db838265540a74b7caec38d7b9f34cea563d8359e',
    '78718-prefix-metric-supplier-storage-v1.py': 'f2d8e79504a2a3895ec8705457eabe46321e80b68b8e7c7de11f13015d160ff3',
    '78718-prefix-volume-moment-storage-v1.py': '16f493774c7176566dda1f08e494b2af74d2f6e04b970b43c802838b08a5f654',
    '78718-prefix-common-cut-storage-v1.py': '34b0b92c6f4d92bd497f3d84d28cbd73cb29271e36b240d3a19795987f057d43',
    '78718-prefix-angular-arithmetic-storage-v2.py': '4977cb407bc9cdd64a580c999727a9978bf4041011e89cab192be7ecd2c2f5dd',
    '78718-prefix-metric-budget-storage-v2.py': '18599b65771eae53199442589547105292489c323aac333e5eee6f2dacadb3aa',
    '78718-prefix-closed-budget-storage-v1.py': '375261a22c8465c9ce318624818493590b1ceee4eb28ce9cd3c1c253a9f8f150',
    '78718-prefix-angular-metric-storage-v2.py': '7f60b8431c10ef93878049be0ae9d9677df268b7cb3963315096103bafdd0dc1',
    '78718-prefix-terminal-error-storage-v2.py': '882086b30a5af04fbac558234295eab035e24608727c605a9dfd9aae36a0cabd',
    '78718-prefix-export-closed-mesh-storage-v1.py': '5126cfca789877456463ae640d0f174d45ab50dffbe83233c080b02f21119ea5',
    '78718-prefix-review-closed-mesh-storage-v1.py': '9a211f07178ae7653518b59a243dee0046825cec2e7fae287762ebdef5a11611',
}
SWAPS = {
    'db6f-root-mirror-hermite.py': '78718-prefix-mirror-hermite-storage-v1.py',
    'db6f-audit-metric-supplier.py': '78718-prefix-metric-supplier-storage-v1.py',
    'db6f-audit-metric-polynomial.py': '78718-prefix-metric-polynomial-storage-v1.py',
    'db6f-root-common-cut-v2.py': '78718-prefix-common-cut-storage-v1.py',
    'db6f-audit-prefix-angular-metric.py': '78718-prefix-angular-metric-storage-v2.py',
    'db6f-audit-closed-budget-transfer-v3.py': '78718-prefix-closed-budget-storage-v1.py',
    'db6f-audit-terminal-error-gate.py': '78718-prefix-terminal-error-storage-v2.py',
    'db6f-export-closed-mesh.py': '78718-prefix-export-closed-mesh-storage-v1.py',
    'db6f-tail-review-closed-mesh.py': '78718-prefix-review-closed-mesh-storage-v1.py',
}
PROVENANCE = {
    'source-ledger': ('2026-11-10-78718-storage-adapters-source-ledger-03.json',
                      '1b7e05df897d10e77c056151e2beb0b8eee1ea7e86e28fb9bdef9899b22a6dde'),
    'v2-full-diff': ('2026-11-10-78718-storage-provenance-fix-diff-03.txt',
                     '100fd59c1ca1281f8b455dbf4dc77c019cfc0e715fae38b453c6c18477fc9c9b'),
    'v1-complete-review': ('2026-11-10-78718-audit-storage-family-v1.md',
                           '4912e2cd32bb2df8b8095d1e93e968bbe9417aa357894114caddd22cda230093'),
    'v2-complete-review': ('2026-11-10-78718-audit-storage-family-v2.md',
                           '2fe0c4a0d62c0864a8e318c4ac5e07111c67f024e2d3319565a96bcc4a733b1f'),
    'v2-independent-source-check': ('2026-11-10-78718-audit-storage-v2-source-closure-01.json',
                                     '7215eeda5b88d5895e804f659873762c348b8a3a15c19fbaaffa081c07a8a6dd'),
    'v2-actual-reader-check': ('2026-11-10-78718-storage-readers-check-03.json',
                              '0cd8154250c031eb41304d07374f4b1cc7692b5be8b612c730e62b0abd4dcdb7'),
    'original-complete-plan-review': ('2026-11-10-78718-audit-post-restart8000-plan-v1.md',
                                     'e53db48be38381a3e793fb2e2b016b0c0ba51c3ea8acf9fb0c530fadf736cdfb'),
}
TOOL_SOURCES = {
    '78718-build-storage-adapters-v3.py': '110457adcd109dcfd28cc285dc6458c97b37cd68858962b6ad44a5d3d8f43683',
    '78718-check-storage-readers-v2.py': '78faf566f9b3ca3800d221b02fcd0363f64826025c4a4f8ac3c359bc42747565',
}
TERMINAL_NAME = '78718-prefix-terminal-error-storage-v2.py'
ANGULAR_NAME = '78718-prefix-angular-metric-storage-v2.py'
EXPORT_NAME = '78718-prefix-export-closed-mesh-storage-v1.py'
REVIEW_NAME = '78718-prefix-review-closed-mesh-storage-v1.py'
STORAGE_POLICY = (
    'Conditional resource branch only: first use the original single-container plan. '
    'Select this separately named complete family only for an actually observed '
    'single-container size need. This planner neither infers that need nor selects '
    'or executes either branch. All source/data identities and every original '
    'mathematical gate remain required.'
)
PREFIX_COMPLETION = (
    'Natural exit 0; the defining M24 base and its actual data_storage descriptor '
    'plus every content-addressed part must close and hash correctly. The original '
    'logical gzip/NPZ bytes are retained by the reviewed codec, with each raw part '
    '<=4,600,000 bytes and each physical file <5,000,000 bytes. The unchanged '
    'RLIMIT_FSIZE 4,999,999 wrapper remains; storage success is not a graph certificate.'
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load_base():
    path = HERE / BASE_NAME
    require(hashlib.sha256(path.read_bytes()).hexdigest() == BASE_SHA,
            'Changed frozen original success-only planner')
    spec = importlib.util.spec_from_file_location('storage_v2_original_plan', path)
    base = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = base
    spec.loader.exec_module(base)
    return base


def assignment(path, name):
    tree = ast.parse(Path(path).read_text(), filename=str(path))
    values = [node.value for node in tree.body if isinstance(node, ast.Assign)
              and any(isinstance(target, ast.Name) and target.id == name
                      for target in node.targets)]
    require(len(values) == 1, 'Missing or ambiguous frozen assignment: ' + name)
    return values[0]


def literal(path, name):
    return ast.literal_eval(assignment(path, name))


def source_ast(path, name):
    return ast.dump(assignment(path, name), annotate_fields=True, include_attributes=False)


def static_command_names():
    """Inspect literal source names without creating any candidate argv."""
    tree = ast.parse((HERE / BASE_NAME).read_text(), filename=str(HERE / BASE_NAME))
    functions = [node for node in tree.body if isinstance(node, ast.FunctionDef)
                 and node.name == 'command_plan']
    require(len(functions) == 1, 'Missing original command plan')
    names = set()
    for node in ast.walk(functions[0]):
        if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Name):
            continue
        index = 1 if node.func.id == 'add' else 0 if node.func.id == 'script' else None
        if index is not None and len(node.args) > index:
            value = node.args[index]
            if isinstance(value, ast.Constant) and type(value.value) is str:
                names.add(value.value)
    require(set(SWAPS) <= names, 'A declared storage CLI is absent from original plan')
    require(len(names) == 22, 'Changed original literal command-source coverage')
    return sorted(names)


def verify_storage_inputs(base):
    """Source/hash/AST metadata only; no adapter import or mathematical call."""
    bindings = base.Bindings()
    bindings.add(HERE / BASE_NAME, 'frozen-original-success-only-planner', BASE_SHA)
    for role, (name, digest) in PROVENANCE.items():
        bindings.add(NOTES / name, 'storage-provenance:' + role, digest)
    for name, digest in TOOL_SOURCES.items():
        bindings.add(HERE / name, 'storage-reviewed-generation-or-check-source', digest)
    for name, digest in FAMILY.items():
        bindings.add(HERE / name, 'complete-storage-v2-family', digest)
    ledger = base.read_json(NOTES / PROVENANCE['source-ledger'][0])
    base.same(set(ledger['new_source_names'].values()) == set(FAMILY), True,
              'Wrong complete storage source family')
    require(len(ledger['transformations']) == 14, 'Incomplete storage derivation rows')
    derived = dict(ledger['core_sources'])
    for row in ledger['transformations']:
        require(row['new'] not in derived, 'Duplicate storage derivation identity')
        derived[row['new']] = row['new_sha256']
        bindings.add(HERE / row['old'], 'original-storage-derivation-source',
                     row['old_sha256'], row['old_bytes'])
        bindings.add(HERE / row['new'], 'actual-reviewed-storage-derivation',
                     row['new_sha256'], row['new_bytes'])
    base.same(derived, FAMILY, 'Storage ledger differs from complete frozen family')
    terminal = HERE / TERMINAL_NAME
    old_terminal = HERE / 'db6f-audit-terminal-error-gate.py'
    terminal_prefix = literal(terminal, 'PREFIX_SOURCES')
    expected_prefix = {name: digest for name, digest in FAMILY.items()
                       if name not in (TERMINAL_NAME, EXPORT_NAME, REVIEW_NAME)}
    base.same(terminal_prefix, expected_prefix, 'Incomplete new terminal prefix source pins')
    original_sources = literal(old_terminal, 'SOURCES')
    base.same(literal(terminal, 'SOURCES'), original_sources,
              'Original terminal tail/reference source family changed')
    require(len(original_sources) == 21, 'Wrong original terminal source count')
    for name, digest in original_sources.items():
        bindings.add(HERE / name, 'unchanged-original-terminal-source', digest)
    for name in ('BOUND', 'FACTOR', 'LOWER', 'REFERENCE'):
        base.same(source_ast(terminal, name), source_ast(old_terminal, name),
                  'Changed original terminal/reference assignment: ' + name)
    angular_sources = literal(HERE / ANGULAR_NAME, 'SOURCES')
    require(len(angular_sources) == 11, 'Wrong angular dependency closure size')
    for name, digest in angular_sources.items():
        bindings.add(HERE / name, 'actual-storage-angular-source', digest)
        if name.startswith('78718-'):
            require(FAMILY.get(name) == digest, 'Angular uses another new storage family')
    require(literal(HERE / REVIEW_NAME, 'EXPORTER_SHA') == FAMILY[EXPORT_NAME],
            'Mesh reviewer does not bind the actual new exporter')
    names = static_command_names()
    substitutions = []
    for old, new in SWAPS.items():
        old_identity = bindings.add(HERE / old, 'original-planned-cli-source')
        new_identity = bindings.add(HERE / new, 'storage-replacement-cli-source', FAMILY[new])
        substitutions.append({'old': old_identity, 'new': new_identity})
    return {'bindings': bindings.output(), 'substitutions': substitutions,
            'storage_source_count': len(FAMILY), 'command_file_substitution_count': len(SWAPS),
            'original_literal_command_sources': names,
            'terminal_prefix_pin_count': len(terminal_prefix),
            'original_terminal_pin_count': len(original_sources),
            'angular_pin_count': len(angular_sources),
            'terminal_reference_and_bound_AST_unchanged': True,
            'mesh_reviewer_exporter_pin_verified': True,
            'actual_solver_calls': 0, 'actual_production_calls': 0,
            'adapter_imports': 0, 'candidate_argv_constructed': False}


def replace_command_records(base, original, storage):
    """Only exact script path tokens and their corresponding source identities."""
    result = copy.deepcopy(original)
    replacements = {row['old']['path']: row for row in storage['substitutions']}
    seen = {path: 0 for path in replacements}
    changes = []
    for group, argv_key in (('commands', 'argv'),
                            ('manifest_or_independent_input_templates', 'argv_template')):
        for before, after in zip(original[group], result[group], strict=True):
            token_changes = []
            for index, token in enumerate(before[argv_key]):
                if type(token) is str and token in replacements:
                    row = replacements[token]
                    after[argv_key][index] = row['new']['path']
                    seen[token] += 1
                    token_changes.append({'index': index, 'old': token, 'new': row['new']['path']})
            source_path = before['source']['path']
            if source_path in replacements:
                row = replacements[source_path]
                base.same(before['source'], row['old'], 'Original command source changed')
                after['source'] = copy.deepcopy(row['new'])
            for index, source in enumerate(before.get('additional_sources', [])):
                if source['path'] in replacements:
                    row = replacements[source['path']]
                    base.same(source, row['old'], 'Original additional source changed')
                    after['additional_sources'][index] = copy.deepcopy(row['new'])
            if before['id'] == 'prefix-base':
                after['completion_requirement'] = PREFIX_COMPLETION
            # Compare everything else, including every numerical argument, gate,
            # output name, condition, dependency and unresolved manifest selector.
            restored = copy.deepcopy(after)
            for change in token_changes:
                require(restored[argv_key][change['index']] == change['new'],
                        'Incorrect exact source-path substitution')
                restored[argv_key][change['index']] = change['old']
            if source_path in replacements:
                base.same(restored['source'], replacements[source_path]['new'],
                          'Incorrect replacement source identity')
                restored['source'] = copy.deepcopy(before['source'])
            for index, source in enumerate(before.get('additional_sources', [])):
                if source['path'] in replacements:
                    base.same(restored['additional_sources'][index],
                              replacements[source['path']]['new'],
                              'Incorrect replacement additional source identity')
                    restored['additional_sources'][index] = copy.deepcopy(source)
            if before['id'] == 'prefix-base':
                restored['completion_requirement'] = before['completion_requirement']
            base.same(restored, before, 'Non-storage command metadata changed')
            if token_changes:
                changes.append({'group': group, 'id': before['id'], 'path_token_changes': token_changes})
    require(all(value > 0 for value in seen.values()), 'An intended storage CLI was not substituted')
    return result, changes, seen


def build(args):
    base = load_base()
    require(args.run_directory.name.startswith('2026-11-10-78718-post-restart8000-storage-v2-'),
            'Use the distinct post-restart8000-storage-v2 production namespace')
    # No monkeypatch, synthetic CP, alternate status or substituted audit. This
    # exact frozen call demands the genuine root exit and complete final report.
    original = base.build(args)
    storage = verify_storage_inputs(base)
    result, changes, counts = replace_command_records(base, original, storage)
    bindings = base.Bindings()
    for row in original['preexisting_bindings']:
        for role in row['roles']:
            if row['path'] == str(HERE / BASE_NAME) and role == 'this-plan-source':
                role = 'ancestor-original-plan-source'
            bindings.bound(row, role)
    for row in storage['bindings']:
        for role in row['roles']:
            bindings.bound(row, role)
    bindings.add(Path(__file__), 'this-plan-source')
    result['preexisting_bindings'] = bindings.output()
    result['schema'] = '78718-post-restart8000-success-only-conditional-storage-plan-v2'
    result['status'] = 'ACTUAL_MAIN_SUCCESS_BOUND_CONDITIONAL_STORAGE_PLAN_ONLY'
    result['branch_policy']['storage'] = STORAGE_POLICY
    result['storage_branch_selected_or_activated'] = False
    result['storage_branch_policy'] = STORAGE_POLICY
    result['original_planner_source'] = base.pinned(HERE / BASE_NAME, BASE_SHA)
    result['storage_family_verified'] = storage
    result['source_path_substitution_ledger'] = changes
    result['source_path_substitution_counts'] = counts
    result['storage_changes_are_resource_representation_only'] = True
    result['original_mathematical_gate_assignments_unchanged'] = True
    result['no_successful_producer_or_candidate_storage_run_claimed'] = True
    source_paths = {row['path'] for row in result['preexisting_bindings']}
    old_paths = set(counts)
    for entry in result['commands'] + result['manifest_or_independent_input_templates']:
        require(entry['source']['path'] in source_paths, 'Unbound selected command source')
        for row in entry.get('additional_sources', []):
            require(row['path'] in source_paths, 'Unbound selected additional source')
        for key in ('argv', 'argv_template'):
            require(not any(type(value) is str and value in old_paths
                            for value in entry.get(key, [])), 'Unreplaced prefix CLI')
    require(result['terminal_bound_exact'] == '1/500000000', 'Changed original terminal bound')
    require(result['branch_selection_performed'] is False, 'Unexpected branch selection')
    require(result['actual_solver_calls'] == result['actual_production_calls'] == 0,
            'A pure plan cannot execute mathematical work')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--launch', type=Path, required=True)
    parser.add_argument('--observed-execution', type=Path, required=True)
    parser.add_argument('--final-audit', type=Path, required=True)
    parser.add_argument('--run-directory', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    require(not args.out.exists(), 'Refusing to replace a previous plan or rejection')
    report = {'status': 'NOT_READY_OR_REJECTED', 'plan_ready': False,
              'actual_solver_calls': 0, 'actual_production_calls': 0,
              'complete_final_audit_replayed': False, 'production_commands_emitted': 0,
              'storage_branch_selected_or_activated': False}
    code = 2
    try:
        report = build(args)
        report['production_commands_emitted'] = len(report['commands'])
        code = 0
    except (ValueError, KeyError, FileNotFoundError) as error:
        report['reason'] = repr(error)
    payload = (json.dumps(report, indent=2, ensure_ascii=False, allow_nan=False) + '\n').encode()
    require(len(payload) < 1_000_000, 'Unexpectedly large metadata-only plan')
    require(args.out.resolve().parent == NOTES.resolve(), 'Output must stay in current notes')
    with args.out.open('xb') as stream:
        stream.write(payload)
    print(json.dumps({key: report[key] for key in (
        'status', 'plan_ready', 'actual_solver_calls', 'actual_production_calls',
        'complete_final_audit_replayed', 'production_commands_emitted',
        'storage_branch_selected_or_activated')}
        | {'output': {'path': str(args.out.resolve()), 'bytes': len(payload),
                      'sha256': hashlib.sha256(payload).hexdigest()}}
        | ({'reason': report['reason']} if 'reason' in report else {})))
    return code


if __name__ == '__main__':
    sys.exit(main())
