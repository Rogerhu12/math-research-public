#!/usr/bin/env python3
"""Derive seven new independent-seed8000 entry/metadata sources, without math.

All inputs are frozen reviewed source bytes. Every change is included in a
complete unified diff. This script compiles source text only; it never imports
a scientific module, prepares a launch or starts a solver. Original files stay
unchanged. The new route starts from the published M14 seed, not run02 failure.
"""
import argparse
import ast
import difflib
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCES = {
    '78718-prefix-restart8000-inputs-v1.py': '8730f041dd471c8b37c915589ed3be9cc32049f6f2e34e43b05df481811d0dd6',
    '78718-prefix-prepare-restart8000-v1.py': 'dded46af332d471e7e6e12535295fcfb901ffc312689fdd748b6845f149b08a5',
    '78718-prefix-spectral-restart8000-v1.py': '200792dbe56a84c2cf1b3954f3a4c73a060bab8579029612d16ffe2f162c9b30',
    '78718-prefix-audit-restart8000-v1.py': 'cd090888e4552317bce183c3b5788710ced9e17eea965b9489252e96d2f3496f',
    '78718-check-restart8000-runtime-v1.py': '57b49ef7d7ab4531c0cfed567a3cc3d85b5167773425b1fb9c1e3addeeadfdd6',
    '78718-prepare-restart8000-guard-v1.py': '124c7acf14d9e52e25a41857db443231f3287c2f88ddda524b775e35c8b59b02',
    '78718-record-root-tool-observation-v1.py': 'd7115aa54f2148ea579161e164de5c79585269dc5522f13b1b1bb228c8d4440b',
}
TARGETS = {
    '78718-prefix-restart8000-inputs-v1.py': '78718-prefix-independent-seed8000-inputs-v1.py',
    '78718-prefix-prepare-restart8000-v1.py': '78718-prefix-prepare-independent-seed8000-v1.py',
    '78718-prefix-spectral-restart8000-v1.py': '78718-prefix-spectral-independent-seed8000-v1.py',
    '78718-prefix-audit-restart8000-v1.py': '78718-prefix-audit-independent-seed8000-v1.py',
    '78718-check-restart8000-runtime-v1.py': '78718-check-independent-seed8000-runtime-v1.py',
    '78718-prepare-restart8000-guard-v1.py': '78718-prepare-independent-seed8000-guard-v1.py',
    '78718-record-root-tool-observation-v1.py': '78718-record-independent-tool-observation-v1.py',
}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def replace(text, old, new, count=1):
    if text.count(old) != count:
        raise ValueError('Expected ' + str(count) + ' replacements: ' + old[:140])
    return text.replace(old, new)


def function(text, name, replacement):
    nodes = [n for n in ast.parse(text).body if isinstance(n, ast.FunctionDef) and n.name == name]
    if len(nodes) != 1:
        raise ValueError('Ambiguous function: ' + name)
    node, lines = nodes[0], text.splitlines(keepends=True)
    return ''.join(lines[:node.lineno-1]) + replacement.rstrip() + '\n' + ''.join(lines[node.end_lineno:])


def rename_references(text):
    for old, new in TARGETS.items():
        text = text.replace(old, new)
    # These are only explicit importlib aliases, not original solver modules.
    return text.replace('restart8000_', 'independent_seed8000_')


SEED_INPUTS = '''def published_seed_inputs(original, ancestor):
    """Original public true M14 inputs and runtime source closure; no new solve."""
    pinned(PUBLISHED_CP, PUBLISHED_CP_SHA)
    pinned(LAST_TAIL, LAST_TAIL_SHA)
    equal(ancestor['launch']['source_checkpoint'], identity(PUBLISHED_CP),
          'The original ancestor did not declare the published M14 seed')
    equal(ancestor['launch']['own_actual_tail_warm'], identity(LAST_TAIL),
          'The original ancestor did not declare its own published last tail')
    pinned(RUNTIME_SOURCE_GUARD, RUNTIME_SOURCE_GUARD_SHA)
    guard = original.read(RUNTIME_SOURCE_GUARD)
    equal(guard['command'], ancestor['launch']['command'], 'Original source guard command differs')
    require(len(guard['bound_files']) == 152, 'Original runtime source closure extent changed')
    guard_bindings = {}
    for row in guard['bound_files']:
        verify(row)
        require(row['path'] not in guard_bindings, 'Duplicate original runtime source binding')
        guard_bindings[row['path']] = row
    for row in ancestor['launch']['bindings']:
        equal(guard_bindings.get(row['path']), row, 'Original guard omitted a launch source')
    cp, prior = ancestor['seed'], ancestor['prior']
    require(cp.get('solver_success') is True and cp.get('nodes') == 2633,
            'The declared published seed is not the reviewed finite M14 solution')
    require(cp['tail_seam']['tail_record'] == LAST_TAIL.name,
            'Published warm packet is not the seed own last actual tail')
    auditor_path = OLD_HERE / 'db6f-prefix-audit-spectral-true-m14-direct-csc.py'
    equal(ancestor['bindings'].get(auditor_path.resolve()), identity(auditor_path),
          'Frozen ancestor auditor differs')
    auditor = module('independent_seed8000_published_input_schema', auditor_path)
    warm = auditor.check_packet(LAST_TAIL, prior['request']['height'], True,
                                {'config': prior['config'], 'prior': prior})
    chunks = []
    for chunk in cp['pp_coefficient_chunks']:
        row = identity(PUBLISHED_CP.parent / chunk['file'])
        require(row['bytes'] == chunk['bytes'] and row['sha256'] == chunk['sha256'],
                'Published coefficient input changed')
        equal(guard_bindings.get(row['path']), row, 'Original source closure omitted a seed chunk')
        chunks.append(row)
    record = {'scope': 'Original published finite M14 seed and own tail as inputs only; no new mathematical success.',
              'checkpoint': identity(PUBLISHED_CP), 'own_last_packet': identity(LAST_TAIL),
              'original_prefix_nodes': cp['nodes'], 'original_prefix_success': True,
              'own_last_packet_check': warm, 'coefficient_files': chunks,
              'original_runtime_source_guard': identity(RUNTIME_SOURCE_GUARD),
              'original_runtime_source_bindings': len(guard_bindings),
              'failed_CP_warm_input_used': False, 'solver_calls': 0}
    return {'record': record, 'original_runtime_closure': list(guard_bindings.values())}
'''


VALIDATE = '''def validate(launch, planned_config=None):
    original, ancestor = ancestor_context()
    require(launch['schema'] == LAUNCH_SCHEMA, 'Wrong separately named independent seed launch')
    equal(launch['settings'], SETTINGS, 'Changed declared seed8000 numerical policy')
    equal(launch['ancestor_launch'], identity(ANCESTOR), 'Different frozen source ancestor')
    equal(launch['reference_preparation'], ancestor['launch']['reference_preparation'],
          'Different original published M14 reference')
    seed_inputs = published_seed_inputs(original, ancestor)
    equal(launch['source_checkpoint'], identity(PUBLISHED_CP), 'Different original M14 seed')
    equal(launch['own_actual_tail_warm'], identity(LAST_TAIL), 'Different original M14 own warm tail')
    equal(launch['published_seed_input_check'], seed_inputs['record'], 'Published seed input ledger differs')
    require(launch.get('executor') == EXECUTOR == '/root/independent_audit',
            'The declared independent executor changed')
    equal(launch['observation_recorder'], identity(TOOL_OBSERVER), 'Different fixed-actor tool observer')
    require(launch.get('failed_CP_warm_input_used') is False
            and launch.get('exact_replay_of_failed_CP_restart_route') is False,
            'The independent seed route must not be relabeled as failed-CP restart replay')
    require(not {'failed_source_root_observation', 'restart_budget_diagnostic',
                 'ancestor_source_checkpoint', 'ancestor_tail_warm'} & set(launch),
            'Unexpected failed-restart input fields')
    for key in ('frozen_physical_fields', 'source_root', 'weights', 'callbacks',
                'newton_lifetime_definitions', 'csc_selection_definitions', 'csc_prerequisites'):
        equal(launch[key], ancestor['launch'][key], 'Changed frozen original definition: ' + key)
    evidence = code_evidence(launch['typed_code_prerequisite']['report']['path'],
                             launch['typed_code_prerequisite']['root_observation']['path'])
    equal(launch['typed_code_prerequisite'], evidence, 'Common typed-code source prerequisite changed')
    out = Path(launch['out_prefix']).resolve()
    require(out.parent == NOTES.resolve() and out.name.startswith('2026-11-10-78718-independent-'),
            'Use the explicit new independent output namespace')
    cfg_path = Path(str(out) + '-tail-config.json')
    launch_path = Path(str(out) + '-launch.json')
    equal(launch['command'], [sys.executable, str(RUNNER), '--launch', str(launch_path)],
          'Wrong separately named independent runtime command')
    require(launch['launch_path'] == str(launch_path) and launch['cwd'] == str(REPO),
            'Wrong independent launch path or cwd')
    equal(launch['delegated_parser_argv'], expected_argv(ancestor, cfg_path, out),
          'Undeclared original coupled argument change')
    cfg = planned_config if planned_config is not None else original.read(cfg_path)
    equal(cfg, expected_config(original, ancestor, out), 'Wrong original warm config or new I/O')
    bindings = {}
    for row in launch['bindings']:
        path = Path(row['path']).resolve()
        require(path not in bindings, 'Duplicate independent source binding')
        bindings[path] = row
        if planned_config is not None and path == cfg_path:
            data = (json.dumps(cfg, indent=2, ensure_ascii=False, allow_nan=False) + '\\n').encode()
            equal(row, {'path': str(path), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()},
                  'Planned independent config differs')
            require(not path.exists(), 'Pure preparation refuses an existing config')
        else:
            verify(row)
    required = ancestor['launch']['bindings'] + seed_inputs['original_runtime_closure'] + evidence['bindings']
    required += [identity(path) for path in (ANCESTOR, RUNTIME_SOURCE_GUARD,
                  RUNNER, PREPARER, AUDITOR, Path(__file__), CODE_CORE, CODE_CHECKER,
                  RUNTIME_CHECKER, GUARD_PREPARER, TOOL_OBSERVER)]
    for row in required:
        equal(bindings.get(Path(row['path'])), row, 'Required original/new source omitted')
    equal(launch['tail_config'], bindings.get(cfg_path), 'Independent tail config is unbound')
    return {'reference': ancestor['reference'], 'seed': ancestor['seed'], 'prior': ancestor['prior'],
            'port': ancestor['port'], 'config': cfg, 'out': out, 'launch': launch,
            'bindings': bindings, 'csc_prerequisites': ancestor['csc_prerequisites'],
            'ancestor_context': ancestor, 'published_seed_inputs': seed_inputs,
            'typed_code_prerequisite': evidence}
'''


PREPARE_MAIN = '''def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out-prefix', type=Path, required=True)
    ap.add_argument('--code-check-report', type=Path, required=True)
    ap.add_argument('--code-check-observed', type=Path, required=True)
    ap.add_argument('--check-current-gate', action='store_true')
    args = ap.parse_args()
    i = module('independent_seed8000_pure_input_definitions', HERE / '78718-prefix-independent-seed8000-inputs-v1.py')
    original, ancestor = i.ancestor_context()
    seed_inputs = i.published_seed_inputs(original, ancestor)
    evidence = i.code_evidence(args.code_check_report, args.code_check_observed)
    if args.check_current_gate:
        print(json.dumps({'status': 'PASS_PUBLISHED_SEED8000_INPUTS_ONLY', 'writes': 0,
                          'failed_CP_warm_input_used': False, 'solver_calls': 0,
                          'warm_residual': seed_inputs['record']['own_last_packet_check']['residual']}))
        return 0
    out = args.out_prefix.resolve()
    i.require(out.parent == i.NOTES.resolve() and out.name.startswith('2026-11-10-78718-independent-')
              and not list(out.parent.glob(out.name + '*')), 'Use a completely unused independent notes stem')
    c = module('independent_seed8000_pure_driver_definitions', i.RUNNER)
    cfg_path = Path(str(out) + '-tail-config.json')
    launch_path = Path(str(out) + '-launch.json')
    prep_path = Path(str(out) + '-preparation.json')
    cfg = i.expected_config(original, ancestor, out)
    cfg_data = (json.dumps(cfg, indent=2, ensure_ascii=False, allow_nan=False) + '\\n').encode()
    cfg_row = {'path': str(cfg_path), 'bytes': len(cfg_data), 'sha256': hashlib.sha256(cfg_data).hexdigest()}
    rows = ancestor['launch']['bindings'] + seed_inputs['original_runtime_closure'] + evidence['bindings']
    rows += [i.identity(path) for path in (i.ANCESTOR, i.RUNTIME_SOURCE_GUARD,
             i.RUNNER, i.PREPARER, i.AUDITOR, HERE / '78718-prefix-independent-seed8000-inputs-v1.py',
             i.CODE_CORE, i.CODE_CHECKER, i.RUNTIME_CHECKER, i.GUARD_PREPARER, i.TOOL_OBSERVER)]
    bindings = {row['path']: row for row in rows}
    bindings[str(cfg_path)] = cfg_row
    launch = {key: ancestor['launch'][key] for key in (
        'reference_preparation', 'frozen_physical_fields', 'source_root', 'callbacks',
        'weights', 'newton_lifetime_definitions', 'csc_prerequisites', 'csc_selection_definitions')}
    launch.update(schema=i.LAUNCH_SCHEMA, status='PREPARED_NOT_STARTED', scope=i.SCOPE,
        settings=i.SETTINGS, ancestor_launch=i.identity(i.ANCESTOR),
        source_checkpoint=i.identity(i.PUBLISHED_CP), own_actual_tail_warm=i.identity(i.LAST_TAIL),
        published_seed_input_check=seed_inputs['record'], executor=i.EXECUTOR,
        observation_recorder=i.identity(i.TOOL_OBSERVER),
        typed_code_prerequisite=evidence, launch_path=str(launch_path), out_prefix=str(out),
        tail_config=cfg_row, command=[sys.executable, str(i.RUNNER), '--launch', str(launch_path)],
        cwd=str(i.REPO), delegated_parser_argv=i.expected_argv(ancestor, cfg_path, out),
        stdout_log=str(out)+'-run.log', reproduction_file=str(out)+'-reproduction.json',
        original_summary_file=str(out)+'-summary.json', checkpoint_output=str(out)+'.json.gz',
        first_request_binding=str(out)+'-first-request-binding.json',
        coefficient_output_pattern=str(out)+'_coeff_*.npy.gz',
        bindings=sorted(bindings.values(), key=lambda row: row['path']),
        original_equations_and_callback_identity_unchanged=True,
        changed_numeric_policy={'max_nodes': {'source_ancestor': 6500, 'new': 8000}},
        restart_scope='Published true M14 seed and its own published audited tail_0002; no current root failed-CP warm input.',
        failed_CP_warm_input_used=False, exact_replay_of_failed_CP_restart_route=False,
        runtime_code_gate='Retain every original raw identity/closure gate and all ten live typed-code source identities before/after each real BVP and restoration.',
        final_gate='Actual successful outer/CP/tail and genuine /root/independent_audit natural tool exit0 remain mandatory.')
    c.validate_inputs(launch, planned_config=cfg)
    c.write_json(cfg_path, cfg, exclusive=True)
    c.write_json(launch_path, launch, exclusive=True)
    report = {'schema': '78718-independent-seed8000-pure-preparation-v1',
        'status': 'PREPARED_ONLY_NO_NEW_CANDIDATE_NO_SOLVER', 'scope': __doc__,
        'launch': i.identity(launch_path), 'tail_config': i.identity(cfg_path),
        'source_ancestor_launch': i.identity(i.ANCESTOR),
        'original_seed_input_check': seed_inputs['record'], 'executor': i.EXECUTOR,
        'settings': i.SETTINGS, 'bindings': len(bindings),
        'callback_definitions': len(launch['callbacks']), 'typed_code_evidence': evidence,
        'operations': {'candidate_objects': 0, 'restart_calls': 0, 'RHS_calls': 0,
            'Newton_install_calls': 0, 'CSC_factory_calls': 0, 'matrix_calls': 0,
            'BVP_calls': 0, 'DN_calls': 0},
        'failed_CP_warm_input_used': False, 'independent_numerical_replay_performed': False,
        'future_actual_exit': 'NOT_STARTED; only /root/independent_audit can supply its actual tool observation'}
    c.write_json(prep_path, report, exclusive=True)
    print(json.dumps({'status': report['status'], 'bindings': len(bindings),
        'launch': i.identity(launch_path), 'preparation': i.identity(prep_path),
        'failed_CP_warm_input_used': False, 'solver_calls': 0}, indent=2))
    return 0
'''


def derive(originals):
    outputs = {}
    for name, raw in originals.items():
        outputs[name] = rename_references(raw.decode())

    name = '78718-prefix-restart8000-inputs-v1.py'
    text = outputs[name]
    text = replace(text, '''"""Closed metadata/input identities for the separately named restart8000 run.

The frozen ancestor is validated by its own unchanged entry.  The failed CP
and its audited last tail are additional declared warm inputs, never relabeled
as a successful candidate.  No candidate, restart, RHS, Newton, DN or matrix
factory is called here; saved polynomial evaluation is only an input check.
"""''', '''"""Pure inputs for an independently executed published-M14-seed8000 route.

The original 97/141/152 source closures validate themselves. This new route
uses the published true M14 prefix and its own tail_0002, not the current root
failed CP. It is not byte-for-byte replay of the failed-CP restart route.
No candidate, restart, RHS, Newton, DN, matrix or solver factory is called.
"""''')
    begin = text.index('FAILED_CP = ')
    end = text.index('RUNNER = ', begin)
    text = text[:begin] + '''PUBLISHED_STEM = '2026-11-09-db6f-prefix-flat-v17v18-fixed-m14-d12-p8-s32-q512-outer-from14'
PUBLISHED_CP = OLD_TOPIC / 'notes' / (PUBLISHED_STEM + '.json.gz')
PUBLISHED_CP_SHA = '3df8eefb18c4271283c7ae2b076afcda3fb42b169c8a7296ee4bce3e3b3ad3d0'
LAST_TAIL = OLD_TOPIC / 'notes' / (PUBLISHED_STEM + '_tail_0002.json.gz')
LAST_TAIL_SHA = '009bf5472ca412fae7d900d4ec18d26cd217221138666c2899dfceb3ead8f762'
RUNTIME_SOURCE_GUARD = OLD_TOPIC / 'notes' / (STEM + '-guard-launch.json')
RUNTIME_SOURCE_GUARD_SHA = 'c5a9bb2d5bba1099db7b489d52b423b0fff135be339a8ea435989f235d3b8063'
EXECUTOR = '/root/independent_audit'
TOOL_OBSERVER = HERE / '78718-record-independent-tool-observation-v1.py'
RUNTIME_CHECKER = HERE / '78718-check-independent-seed8000-runtime-v1.py'
GUARD_PREPARER = HERE / '78718-prepare-independent-seed8000-guard-v1.py'
''' + text[end:]
    text = text.replace('78718-true-m14-w14-restart8000-', '78718-true-m14-w14-independent-seed8000-')
    scope_start = text.index('SCOPE = (')
    scope_end = text.index('\n\n\ndef require', scope_start)
    text = text[:scope_start] + '''SCOPE = ('Original fixed-g M14/N512 W14 true-DN equations, starting anew from the '
         'published true M14 prefix and its own audited tail_0002, max_nodes8000, '
         'unchanged reviewed release-LU/direct-CSC kernels and complete typed live-code identity. '
         'Execution observer is /root/independent_audit. This is a separately declared '
         'independent numerical route, not exact replay of the root failed-CP restart route.')''' + text[scope_end:]
    text = function(text, 'failure_inputs', SEED_INPUTS)
    text = replace(text, "('--restart', str(FAILED_CP))", "('--restart', str(PUBLISHED_CP))")
    text = replace(text, "'Restart tail physical equations or discretization changed'",
                   "'Original seed tail physical equations or discretization changed'")
    text = function(text, 'validate', VALIDATE)
    outputs[name] = text

    name = '78718-prefix-prepare-restart8000-v1.py'
    text = outputs[name]
    old_doc = ast.get_docstring(ast.parse(text))
    new_doc = ('Pure preparation for the independent published-M14 seed route at max8000.\n\n'
               'Validates original 97/141/152 source inputs, the original true M14 seed\n'
               'and own tail_0002, plus existing common typed-code source evidence.\n'
               'Creates metadata only; no candidate/restart/RHS/Newton/factory/BVP/DN.\n'
               'This preparation is not an independent numerical execution.')
    text = replace(text, '"""' + old_doc + '\n"""', '"""' + new_doc + '\n"""')
    text = function(text, 'main', PREPARE_MAIN)
    outputs[name] = text

    name = '78718-prefix-spectral-restart8000-v1.py'
    text = outputs[name]
    text = replace(text, 'New restart8000 / typed-code identity', 'Independent published-M14 seed8000 / typed-code identity')
    text = replace(text, 'and must be launched separately by root.',
                   'and must be launched separately by /root/independent_audit.')
    text = replace(text, 'Program requested exit only; root actual tool observation is separate.',
                   'Program requested exit only; /root/independent_audit actual tool observation is separate.')
    text = text.replace('RESTART8000_FINITE_M14_', 'INDEPENDENT_SEED8000_FINITE_M14_')
    outputs[name] = text

    name = '78718-prefix-audit-restart8000-v1.py'
    text = outputs[name]
    text = replace(text, 'New read-only close audit for restart8000', 'Read-only close audit for independent published-M14 seed8000')
    text = replace(text, "Final CLI mode additionally requires root's real tool-exit observation.",
                   "Final CLI mode requires /root/independent_audit's genuine tool-exit observation.")
    text = replace(text, "'NOT_READY: root actual tool-exit observation is required'",
                   "'NOT_READY: /root/independent_audit actual tool-exit observation is required'")
    text = replace(text, "obs.get('observer') == '/root'", "obs.get('observer') == '/root/independent_audit'")
    text = replace(text, "'Wrong actual root observation identity'", "'Wrong actual independent observation identity'")
    text = replace(text, "require(obs['actual_exit_code'] == 0, 'Root observed a nonzero tool exit')", '''require(obs['actual_exit_code'] == 0, 'Independent executor observed a nonzero tool exit')
    equal(obs.get('recorder_source'), identity(c.i.TOOL_OBSERVER), 'Wrong fixed-actor observation recorder source')
    tool = obs.get('tool_return_metadata')
    require(type(tool) is dict and type(tool.get('exit_code')) is int
            and tool['exit_code'] == obs['actual_exit_code']
            and tool.get('chunk_id') == obs['tool_receipt'] and tool.get('session_id') is None,
            'Observation is detached from a completed actual terminal-tool return')''')
    text = text.replace('RESTART8000_FINITE_M14_', 'INDEPENDENT_SEED8000_FINITE_M14_')
    text = replace(text, 'Duplicate root output binding', 'Duplicate independent output binding')
    text = replace(text, 'Root observation omitted or changed closed file:', 'Independent observation omitted or changed closed file:')
    text = replace(text, 'Root observation must bind closed outputs', 'Independent observation must bind closed outputs')
    text = replace(text, 'PASS_ROOT_OBSERVED_RESTART8000_M14_W14_FINITE_COUPLED_CLOSE',
                   'PASS_INDEPENDENT_OBSERVED_SEED8000_M14_W14_FINITE_COUPLED_CLOSE')
    text = replace(text, 'root_observation=identity(observed)', 'independent_observation=identity(observed)')
    outputs[name] = text

    name = '78718-check-restart8000-runtime-v1.py'
    outputs[name] = outputs[name].replace('78718-restart8000-runtime-identity-check-v1',
                                         '78718-independent-seed8000-runtime-identity-check-v1')

    name = '78718-prepare-restart8000-guard-v1.py'
    text = outputs[name]
    text = replace(text, 'frozen restart8000 launch', 'frozen independent seed8000 launch')
    text = replace(text, '78718-restart8000-resource-bound-command-v1',
                   '78718-independent-seed8000-resource-bound-command-v1')
    text = replace(text, "'root_start_command':command, 'solver_started':False,",
                   "'executor_start_command':command, 'executor':c.i.EXECUTOR,\n             'observation_recorder':c.identity(c.i.TOOL_OBSERVER), 'solver_started':False,")
    text = replace(text, "'root_start_command':command},indent=2)",
                   "'executor_start_command':command,'executor':c.i.EXECUTOR},indent=2)")
    outputs[name] = text

    name = '78718-record-root-tool-observation-v1.py'
    text = outputs[name]
    text = replace(text, 'actual root terminal-tool return', 'actual /root/independent_audit terminal-tool return')
    text = replace(text, 'The root orchestration cell must supply the genuine tool result.',
                   'Only /root/independent_audit supplies its genuine tool result to this fixed-actor recorder.')
    text = replace(text, '"observer": "/root"', '"observer": "/root/independent_audit"')
    text = text.replace('-root-observed-', '-independent-observed-')
    text = replace(text, '-root-unavailable-session.json', '-independent-unavailable-session.json')
    text = replace(text, 'Actual root orchestration tool return;', 'Actual /root/independent_audit orchestration tool return;')
    outputs[name] = text
    return outputs


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--ledger', type=Path, required=True)
    ap.add_argument('--diff', type=Path, required=True)
    args = ap.parse_args()
    originals = {name: (HERE/name).read_bytes() for name in SOURCES}
    for name, raw in originals.items():
        if sha(raw) != SOURCES[name]:
            raise ValueError('Frozen old source changed: ' + name)
    derived = derive(originals)
    records, diffs = [], []
    for name, text in derived.items():
        output = HERE/TARGETS[name]
        raw = text.encode()
        compile(raw, str(output), 'exec', dont_inherit=True, optimize=0)
        if len(raw) >= 100_000:
            raise ValueError('A source exceeded the review size limit')
        if output.exists() and output.read_bytes() != raw:
            raise FileExistsError(output)
        records.append({'source': str(HERE/name), 'source_bytes': len(originals[name]),
                        'source_sha256': sha(originals[name]), 'output': str(output),
                        'output_bytes': len(raw), 'output_sha256': sha(raw)})
        diffs.extend(difflib.unified_diff(originals[name].decode().splitlines(True), text.splitlines(True),
                                         fromfile=name, tofile=output.name))
    ledger = {'schema': '78718-independent-seed8000-source-derivation-v1',
              'generator_sha256': sha(Path(__file__).read_bytes()), 'files': records,
              'source_compilation_only': True, 'old_sources_modified': False,
              'mathematical_functions_executed': 0, 'solver_started': False,
              'route': 'Published original true M14 seed and own tail; not exact failed-CP restart replay.',
              'execution_observer': '/root/independent_audit'}
    generated = [(HERE/TARGETS[name], text.encode()) for name, text in derived.items()]
    generated += [(args.ledger, (json.dumps(ledger, indent=2)+'\n').encode()),
                  (args.diff, ''.join(diffs).encode())]
    for path, raw in generated:
        if len(raw) >= 100_000:
            raise ValueError('Generated review file exceeds 100KB')
        if path.exists() and path.read_bytes() != raw:
            raise FileExistsError(path)
    for path, raw in generated:
        if not path.exists():
            with path.open('xb') as stream:
                stream.write(raw)
    for name, raw in originals.items():
        if (HERE/name).read_bytes() != raw:
            raise ValueError('Old source changed during source-only derivation')
    print(json.dumps({'status': 'SOURCE_DERIVED_NOT_PREPARED_NOT_STARTED', 'sources': len(records),
                      'ledger_bytes': args.ledger.stat().st_size, 'diff_bytes': args.diff.stat().st_size,
                      'mathematical_functions_executed': 0, 'solver_calls': 0}))


if __name__ == '__main__':
    main()
