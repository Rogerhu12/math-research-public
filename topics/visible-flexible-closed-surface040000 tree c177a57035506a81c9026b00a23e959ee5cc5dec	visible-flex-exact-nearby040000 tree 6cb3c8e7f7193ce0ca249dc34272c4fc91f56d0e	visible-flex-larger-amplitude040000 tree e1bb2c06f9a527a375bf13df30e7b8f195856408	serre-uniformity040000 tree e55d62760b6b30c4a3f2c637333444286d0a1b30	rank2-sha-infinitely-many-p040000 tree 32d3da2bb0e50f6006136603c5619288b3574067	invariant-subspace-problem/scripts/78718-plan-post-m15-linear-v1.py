#!/usr/bin/env python3
"""Read-only, success-only command plan for the new M15/N512/W15 post-coupled chain.

This program never executes a producer, solver, numerical callback or command.
It replays the frozen complete final audit, requires its separately saved report
and root's actual successful tool-exit observation, hashes pre-existing inputs,
and writes argv records for future work. A plan is not a certificate or a run.
The original single-container prefix family is the only executable family here.
The separately named byte-storage family remains outside this frozen v1 plan.
"""
import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
NOTES = TOPIC / 'notes'
REPO = TOPIC.parents[1]
SOURCE_ROOT = TOPIC / 'repro/source-root'
OLD_TOPIC = Path('/workspace/scratch/db6f0b0e7462/math-research/topics/visible-flexible-closed-surface')
PYTHON = '/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python'
NODE = '/opt/codex/runtimes/codex-primary-runtime/dependencies/node/bin/node'
AUDITOR = HERE / '78718-prefix-audit-m15-linear-v1.py'
AUDITOR_SHA = 'fd41b9ef4c2eea648cbb1ab1c3b638e61bc41d97d99d9213ad0370c042ff147e'
LAUNCH_SCHEMA = '78718-true-m15-w15-n512-linear-dn-launch-v1'
SUCCESS = 'PASS_ROOT_OBSERVED_M15_N512_W15_LINEAR_DN_FINITE_COUPLED_CLOSE'
LINEAR_PORT = OLD_TOPIC / 'notes/2026-11-09-950f-prefix-weighted-k6-port96-cusp1024.json'
LINEAR_PORT_SHA = '500e0a0c6d5388e07e3673ef192856804264c612edd6fe26ee09b882698a3702'
TERMINAL_BOUND_EXACT = '1/500000000'
PROVENANCE = {
    'sources': ('2026-11-10-78718-numerical-production-source-inventory.json',
                '7c55cce702b3d6364a372ccfe8923ded6fe69bc42eccbcb57d45e53ea3c6bdab'),
    'm8': ('2026-11-10-78718-numerical-m8-background-inputs.json',
           'c50af6d6c1f6f34d56335259e891dda9f3b664300193b89b031395d70802f335'),
    'proofs': ('2026-11-10-78718-numerical-fixed-proof-preflight.json',
               'c048343c9cf3fbd6661c01c6ce3ac2d6878e2457e970d65ca4659ee3c9b23fab'),
    'tight': ('2026-11-10-78718-numerical-first-dn-tight-background-preflight.json',
              '198be34d48c7c99106ca6609bce19d616a815f7a67838094c2ca87e2fe5e13cf'),
    'lowmetric': ('2026-11-10-78718-numerical-first-dn-lowmetric-background-preflight.json',
                  '74cc0ddea6120a7e67989602ddec3a079e3fb841afb3d25174e2be5203685275'),
}
EXTRA_SOURCES = {
    'db6f-tail-radial-invariant.py': '6c2318e1d2fc40bf9598c2c1dbbe110a0d86d98376e73b6ee64d3acfd054ac3b',
    'db6f-tail-background-point-lipschitz.py': 'ccd59bc42f6685e38229b5425e52c18d08437a43ddbd5073e55e93561a6a0bef',
    'db6f-tail-background-packet-totalwidth.py': 'fcc283c7c7e8d35e82c250b5025921d717bdc8c6130912c2e0d1b9429da09676',
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=True, allow_nan=False)


def same(left, right, message):
    require(canonical(left) == canonical(right), message)


def identity(path):
    path = Path(path).resolve()
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return {'path': str(path), 'bytes': path.stat().st_size, 'sha256': h.hexdigest()}


def read_json(path):
    raw = Path(path).read_bytes()
    if raw[:2] == b'\x1f\x8b':
        raw = gzip.decompress(raw)

    def reject(value):
        raise ValueError('Nonfinite JSON constant: ' + value)

    obj = json.loads(raw, parse_constant=reject)
    require(type(obj) is dict, 'Expected a JSON object: ' + str(path))
    return obj


def pinned(path, digest, size=None):
    row = identity(path)
    require(row['sha256'] == digest, 'Changed frozen input: ' + str(path))
    require(size is None or row['bytes'] == size, 'Changed frozen input size: ' + str(path))
    return row


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    sys.modules[name] = result
    spec.loader.exec_module(result)
    return result


class Bindings:
    def __init__(self):
        self.rows = {}

    def add(self, path, role, digest=None, size=None):
        row = identity(path) if digest is None else pinned(path, digest, size)
        previous = self.rows.get(row['path'])
        if previous is None:
            previous = dict(row, roles=[])
            self.rows[row['path']] = previous
        same({k: previous[k] for k in row}, row, 'Input changed during planning')
        if role not in previous['roles']:
            previous['roles'].append(role)
        return row

    def bound(self, row, role):
        return self.add(row['path'], role, row['sha256'], row['bytes'])

    def output(self):
        return [self.rows[key] for key in sorted(self.rows)]


def existing_reference(name, parent):
    """Use exactly the original terminal Files.file candidate ordering."""
    path = Path(name)
    choices = (path, Path(parent)/path, TOPIC/path, REPO/path, Path(parent)/path.name)
    return next((p.resolve() for p in choices if p.is_file()), None)


def intended_reference_path(name, parent):
    path = Path(name)
    if path.is_absolute():
        return (Path(parent)/path.name).resolve()
    return ((TOPIC/path) if path.parts and path.parts[0] in ('notes', 'scripts')
            else Path(parent)/path).resolve()


def verify_fixed_inputs():
    """Hashes/metadata only. No tail reader, interval backend or physical flow."""
    bindings = Bindings()
    evidence = {}
    for key, (name, digest) in PROVENANCE.items():
        path = NOTES/name
        bindings.add(path, 'fixed-provenance:' + key, digest)
        evidence[key] = read_json(path)
    source = evidence['sources']
    require(source['actual_source_root'] == str(SOURCE_ROOT), 'Different frozen snapshot root')
    require(source['source_snapshot_count'] == 43 and
            source['terminal_required_source_count'] == 21 and
            source['terminal_required_source_hashes_all_match'] is True and
            source['unresolved_literal_references'] == [], 'Incomplete original source inventory')
    bindings.bound(source['source_snapshot_manifest'], 'source-snapshot-manifest')
    for key in ('source_snapshot_files', 'literal_source_closure'):
        for row in source[key]:
            bindings.bound(row, key)
    for name, digest in EXTRA_SOURCES.items():
        bindings.add(HERE/name, 'additional-original-source', digest)
    bindings.add(LINEAR_PORT, 'original-linear-port', LINEAR_PORT_SHA)
    m8 = evidence['m8']
    bindings.bound(m8['manifest'], 'fixed-m8-manifest')
    require(m8['all_raw_hashes_match'] is True and m8['all_files_below_5000000'] is True
            and len(m8['raw_parts']) == 8, 'Incomplete original M8 source record')
    for row in m8['raw_parts']:
        bindings.bound(row, 'fixed-m8-raw')
    roles = {'old_manifest': m8['manifest']['path'], 'linear_port': str(LINEAR_PORT)}
    definitions = None
    for kind in ('tight', 'lowmetric'):
        report = evidence[kind]
        same(report['old_manifest_sha256'], m8['manifest']['sha256'], 'M8 manifest identity differs')
        require(report['background_definition_hashes_verified'] is True and
                report['geometric_transfer_performed'] is False and
                report['finite_map_was_created'] is False, 'Expected only the original fixed-input preflight')
        for path_key, hash_key in (('input_packet', 'input_packet_sha256'),
                                   ('input_data_file', 'input_data_sha256')):
            bindings.add(report[path_key], 'fixed-' + kind + ':' + path_key, report[hash_key])
        roles[kind + '_packet'] = report['input_packet']
        if definitions is not None:
            same(definitions, report['verified_background_definition_files'], 'Different background definitions')
        definitions = report['verified_background_definition_files']
        for key, row in definitions.items():
            bindings.add(row['file'], 'fixed-background:' + key, row['sha256'])
            roles[key] = row['file']
    proof = evidence['proofs']
    bindings.bound(proof['terminal_source'], 'original-terminal-source')
    for key, row in proof['fixed_background_proofs'].items():
        bindings.bound(row, 'fixed-background-proof:' + key)
        roles[key] = row['path']
    for key, row in proof['fixed_reference_headers'].items():
        bindings.bound(row, 'terminal-reference-header:' + key)
    point_path = Path(proof['fixed_reference_headers']['point']['path'])
    point = read_json(point_path)
    for name, digest in point['source_sha256'].items():
        bindings.add(HERE/name, 'terminal-reference-point-source', digest)

    # Discover missing final-reference objects from pinned real metadata.
    # Missing objects receive expected hashes, never invented observed hashes.
    deferred = []

    def defer(name, digest, parent, role, size=None):
        found = existing_reference(name, parent)
        row = {'role': role, 'declared_file': str(name), 'sha256_expected': digest,
               'parent': str(parent), 'present': found is not None}
        if size is not None:
            row['bytes_expected'] = size
        if found is None:
            row['fetch_target'] = str(intended_reference_path(name, parent))
        else:
            row['actual'] = bindings.add(found, role, digest, size)
        deferred.append(row)
        return found

    manifest_path = Path(proof['fixed_reference_headers']['manifest']['path'])
    manifest = read_json(manifest_path)
    for index, row in enumerate(manifest['files']):
        defer(row['path'], row['sha256'], manifest_path.parent,
              'terminal-reference-m12-raw:' + str(index), row['bytes'])
    defer(manifest['input'], manifest['inputSHA256'], manifest_path.parent,
          'terminal-reference-m12-tail-checkpoint')
    packet = point['inputs']['packet']
    packet_path = defer(packet['file'], packet['sha256'], point_path.parent,
                        'terminal-reference-m12-point-packet')
    unknown = []
    if packet_path is None:
        unknown.append({'parent_expected_sha256': packet['sha256'],
                        'parent_declared_file': packet['file'],
                        'fields_to_resolve_after_fetch': ['data_file', 'data_sha256'],
                        'reason': 'The missing actual packet header determines its data binding.'})
    else:
        meta = read_json(packet_path)
        defer(meta['data_file'], meta['data_sha256'], packet_path.parent,
              'terminal-reference-m12-point-packet-data')
    return {'bindings': bindings.output(), 'roles': roles,
            'terminal_reference_objects': deferred,
            'terminal_reference_unknown_descendants': unknown,
            'terminal_reference_ready': all(row['present'] for row in deferred) and not unknown,
            'actual_solver_calls': 0, 'actual_production_calls': 0}


def audited_success(launch_path, observed_path, final_path):
    """The complete original new-identity audit is the sole success predicate."""
    require(sys.executable == PYTHON, 'Use the frozen absolute primary Python interpreter')
    pinned(AUDITOR, AUDITOR_SHA)
    audit = module('post_m15_linear_full_close_audit', AUDITOR)
    launch = read_json(launch_path)
    require(launch.get('schema') == LAUNCH_SCHEMA, 'Not the M15/N512 linear-DN launch schema')
    context = audit.c.validate_inputs(launch)
    require(Path(launch_path).resolve() == Path(context['launch']['launch_path']), 'Wrong launch file')
    actual = {'scope': audit.__doc__, 'mode': 'final', 'ready': False,
              'solver_calls': 0, 'active_trace_read': False}
    actual.update(audit.final_audit(context, Path(observed_path)))
    actual['ready'] = True
    require(actual['status'] == SUCCESS, 'The complete final gate did not pass')
    saved = read_json(final_path)
    same(actual, saved, 'Saved final report differs from complete fresh audit')
    cp_path = Path(actual['prefix_CP']['path'])
    same(identity(cp_path), actual['prefix_CP'], 'CP changed after final audit')
    cp = read_json(cp_path)
    tail_name = cp['tail_seam']['tail_record']
    tail = Path(tail_name)
    tail = tail if tail.is_absolute() else cp_path.parent/tail
    tail = tail.resolve()
    require(tail.name == context['out'].name + f"_tail_{cp['tail_calls']:04d}.json.gz",
            'Not this CP own last tail packet')
    closed = {row['path']: row for row in actual['required_closed_files']}
    same(identity(tail), closed.get(str(tail)), 'Own final tail not bound by the complete audit')
    require(cp['physical_port_sha256'] == LINEAR_PORT_SHA, 'Different physical linear port')
    return context, actual, cp_path, tail


def command_plan(run, cp, tail, fixed):
    """Construct literal argv records; no branch is selected or executed here."""
    run, cp, tail = Path(run).resolve(), Path(cp).resolve(), Path(tail).resolve()
    roles = fixed['roles']
    p = lambda name: str(run/name)
    script = lambda name: str(HERE/name)
    nodes, deferred_templates = [], []

    def add(key, name, argv, needs=(), outputs=(), condition='always', node=False,
            completion=None, extra_sources=()):
        entry = {'id': key, 'argv': ([NODE, '--max-old-space-size=1536'] if node else [PYTHON])
                 + [script(name)] + [str(x) for x in argv],
                 'cwd': str(REPO), 'depends_on': list(needs), 'condition': condition,
                 'source': identity(HERE/name), 'expected_output_paths': list(outputs),
                 'executed': False}
        if completion is not None:
            entry['completion_requirement'] = completion
        if extra_sources:
            entry['additional_sources'] = [identity(HERE/n) for n in extra_sources]
        nodes.append(entry)
        return key

    add('tail-export', 'db6f-prefix-endpoint-critical-increment-export.mjs',
        [tail, p('tail'), '--source-root', SOURCE_ROOT, '--depth', 8, '--steps', 32,
         '--flow-steps', 32, '--angular-nodes', 512, '--degree', 192, '--grid', 'critical',
         '--critical-cells', 0, '--critical-base-steps', 64, '--critical-ratio', '.05',
         '--endpoint-ratio', '.025', '--difference-step', '.00005',
         '--audit-angular-nodes', 128, '--audit-fractions', '.25,.5,.75'],
        outputs=[p('tail-manifest.json'), p('tail-collar.json')], node=True,
        completion='Natural exit 0 and completed manifest, every own shard and own later-written collar.')
    add('tail-radial', 'db6f-tail-radial-invariant.py',
        [p('tail-manifest.json'), p('tail-radial.json')], ['tail-export'], [p('tail-radial.json')])
    add('tail-collar', 'db6f-tail-collar-exact-check.py',
        [p('tail-collar.json'), p('tail-collar-check.json')], ['tail-export'], [p('tail-collar-check.json')])
    add('tail-first', 'db6f-tail-first-bounds-stream.py',
        [p('tail-manifest.json'), p('tail-first.json'), '--batch', 128],
        ['tail-export', 'tail-radial', 'tail-collar'], [p('tail-first.json')])
    add('prefix-base', '78718-run-file-cap.py',
        ['--', PYTHON, script('db6f-root-mirror-hermite.py'), '--source-root', SOURCE_ROOT,
         '--checkpoint', cp, '--linear-port', roles['linear_port'], '--out-prefix', p('prefix-base'),
         '--modes', 24, '--angular', 768, '--quadrature', 8, '--subdivide', 1, '--ell', 0],
        outputs=[p('prefix-base.json')], extra_sources=['db6f-root-mirror-hermite.py'],
        completion='Original single container under RLIMIT_FSIZE 4,999,999; an actual size failure is not a graph.')
    add('prefix-target', 'db6f-audit-metric-supplier.py',
        ['--geometry', p('prefix-base.json'), '--source-root', SOURCE_ROOT, '--out-prefix', p('prefix-target')],
        ['prefix-base'], [p('prefix-target.json')])
    add('prefix-base-metric', 'db6f-audit-metric-polynomial.py',
        ['--geometry', p('prefix-base.json'), '--target', p('prefix-target.json'), '--out', p('prefix-base-metric.json')],
        ['prefix-target'], [p('prefix-base-metric.json')])
    add('bridge', 'db6f-root-exact-bridge.py',
        ['--geometry', p('prefix-base.json'), '--target', p('prefix-target.json'),
         '--tail-manifest', p('tail-manifest.json'), '--metric-certificate', p('prefix-base-metric.json'),
         '--out', p('bridge.json')], ['prefix-base-metric', 'tail-radial', 'tail-collar'], [p('bridge.json')])
    add('common-cut', 'db6f-root-common-cut-v2.py',
        ['make', '--geometry', p('prefix-base.json'), '--tail', p('tail-manifest.json'),
         '--bridge', p('bridge.json'), '--width', '.15', '--out', p('closed-map.json')],
        ['bridge'], [p('closed-map.json')])
    add('prefix-geometry', 'db6f-root-common-cut-v2.py',
        ['geometry', '--geometry', p('closed-map.json'), '--angular', 256, '--radial', 1,
         '--out', p('prefix-geometry.json')], ['common-cut'], [p('prefix-geometry.json')])
    add('prefix-baseline', 'db6f-root-common-cut-v2.py',
        ['metric', '--geometry', p('closed-map.json'), '--target', p('prefix-target.json'),
         '--out', p('prefix-baseline-metric.json')], ['common-cut'], [p('prefix-baseline-metric.json')])
    add('prefix-moment', 'db6f-root-common-cut-v2.py',
        ['moment', '--geometry', p('closed-map.json'), '--angular', 512, '--radial', 1,
         '--out', p('prefix-moment.json')], ['common-cut'], [p('prefix-moment.json')])
    add('prefix-angular', 'db6f-audit-prefix-angular-metric.py',
        ['--geometry', p('closed-map.json'), '--target', p('prefix-target.json'),
         '--baseline', p('prefix-baseline-metric.json'), '--bridge', p('bridge.json'),
         '--budget', '2e-9', '--initial-arcs', 128, '--max-depth', 4,
         '--out', p('prefix-angular-metric.json')], ['prefix-baseline'], [p('prefix-angular-metric.json')],
        'Only if actual baseline target transfer exceeds 1/500000000 and the original angular branch is selected.',
        completion='Entire prefix covered; no --intervals restriction; local diagnostic output is ineligible.')
    for kind, source_role in [('k', 'tight_packet'), ('e', 'lowmetric_packet')]:
        add('background-' + kind, 'db6f-tail-transfer-background-v3.py',
            ['--old-manifest', roles['old_manifest'], '--packet', roles[source_role],
             '--new-manifest', p('tail-manifest.json'), '--out-prefix', p('background-' + kind)],
            ['tail-radial', 'tail-collar'], [p('background-' + kind + '.json')],
            'always' if kind == 'k' else 'Only if complete tail-full has not attained the original metric bound.')
    add('tail-full', 'db6f-audit-tail-stream.py',
        ['--manifest', p('tail-manifest.json'), '--packet', p('background-k.json'), '--angular', 128,
         '--radial', 1, '--background-curvature', 6, '--direct-threshold', '8.5', '--block-size', 128,
         '--out', p('tail-full.json')], ['background-k'], [p('tail-full.json')],
        completion='All finite spans and collar (-1), every row shard, no limit or local-only selection.')
    add('tail-metric', 'db6f-audit-tail-metric-only.py',
        ['--manifest', p('tail-manifest.json'), '--packet', p('background-e.json'), '--radial', 1,
         '--block-size', 128, '--out', p('tail-metric.json')], ['background-e', 'tail-full'], [p('tail-metric.json')],
        'Only if complete tail-full has not attained the original metric bound.')
    add('tail-completeness', 'db6f-audit-complete-metric-report.py',
        ['--report', p('tail-metric.json'), '--curvature-report', p('tail-full.json'),
         '--out', p('tail-completeness.json')], ['tail-metric'], [p('tail-completeness.json')],
        'Required if metric-only is actually used.')

    route_ids = []
    for prefix_kind, prefix_file in [('baseline', 'prefix-baseline-metric.json'),
                                     ('angular', 'prefix-angular-metric.json')]:
        budget = 'closed-budget-' + prefix_kind
        add(budget, 'db6f-audit-closed-budget-transfer-v3.py',
            ['--geometry', p('closed-map.json'), '--geometry-certificate', p('prefix-geometry.json'),
             '--metric-certificate', p(prefix_file), '--moment-certificate', p('prefix-moment.json'),
             '--tail-first', p('tail-first.json'), '--height', roles['height'],
             '--positive-alpha', roles['positive_alpha'], '--background-transfer', p('background-k.json'),
             '--out', p(budget + '.json')],
            ['prefix-geometry', 'prefix-' + prefix_kind, 'prefix-moment', 'tail-first', 'background-k'],
            [p(budget + '.json')], 'Only for the selected complete ' + prefix_kind + ' certificate.')
        for tail_kind in ('full', 'metric-only'):
            route = prefix_kind + '-' + tail_kind
            route_ids.append(route)
            condition = 'Selected complete route: ' + route + '; mutually exclusive with the other final routes.'
            whole, terminal, mesh = 'whole-' + route, 'terminal-' + route, 'mesh-' + route
            argv = ['--closed-budget', p(budget + '.json'), '--tail-certificate', p('tail-full.json')]
            needs = [budget, 'tail-full']
            if tail_kind == 'metric-only':
                argv += ['--tail-metric-certificate', p('tail-metric.json')]
                needs.append('tail-completeness')
            argv += ['--out', p(whole + '.json')]
            add(whole, 'db6f-root-whole-metric-reach-v2.py', argv, needs, [p(whole + '.json')], condition)
            add(terminal, 'db6f-audit-terminal-error-gate.py',
                ['--whole', p(whole + '.json'), '--prefix-target', p('prefix-target.json'),
                 '--out', p(terminal + '.json')], [whole], [p(terminal + '.json')], condition,
                completion='Normal forward candidate mode at exact 1/500000000; all actual M12 reference objects must first be present.')
            add(mesh + '-plan', 'db6f-export-closed-mesh.py',
                ['plan', '--geometry', p('closed-map.json'), '--whole-certificate', p(whole + '.json'),
                 '--out-prefix', p(mesh), '--angular', 144, '--prefix-intervals', 128,
                 '--tail-intervals', 64, '--collar-intervals', 4, '--cap-intervals', 12],
                [terminal], [p(mesh + '-plan.json'), p(mesh + '-radii.json')], condition)
            add(mesh + '-heights', 'db6f-tail-sample-background-height.mjs',
                ['--manifest', p('tail-manifest.json'), '--calibrations', roles['calibrations'],
                 '--alpha', roles['alpha'], '--radii', p(mesh + '-radii.json'), '--source-root', SOURCE_ROOT,
                 '--out', p(mesh + '-heights.json')], [mesh + '-plan'], [p(mesh + '-heights.json')], condition, node=True)
            add(mesh + '-build', 'db6f-export-closed-mesh.py',
                ['build', '--plan', p(mesh + '-plan.json'), '--height-samples', p(mesh + '-heights.json'),
                 '--out-prefix', p(mesh)], [mesh + '-heights'], [p(mesh + '-manifest.json')], condition,
                completion='Read actual mesh_files from the closed manifest; verify all files <5MB, with >1MB data gzip.')
            for exact_time, label in [('0', 't0'), ('1/4', 't1of4'), ('1/2', 't1of2')]:
                deferred_templates.append({
                    'id': mesh + '-PL-' + label, 'depends_on': [mesh + '-build'], 'condition': condition,
                    'argv_template': [PYTHON, script('db6f-audit-closed-mesh.py'), '--mesh',
                        {'resolve_from_closed_manifest': p(mesh + '-manifest.json'), 'array': 'mesh_files',
                         'select': {'time_exact': exact_time}, 'field': 'file', 'also_verify': ['sha256', 'stored_bytes']},
                        '--out', p(mesh + '-PL-' + label + '.json'), '--batch', '2048'],
                    'cwd': str(REPO), 'source': identity(HERE/'db6f-audit-closed-mesh.py'),
                    'reason_not_literal_argv_yet': 'The actual output selects .ply or .ply.gz; do not guess it.',
                    'executed': False})
            deferred_templates.append({
                'id': mesh + '-independent-same-plan-review', 'condition': condition,
                'argv_template': [PYTHON, script('db6f-tail-review-closed-mesh.py'),
                    '--manifest', p(mesh + '-manifest.json'), '--replay-manifest',
                    {'required_external_input': 'An actually independently built mesh manifest with this exact plan SHA.'},
                    '--out', p(mesh + '-independent-byte-review.json')],
                'cwd': str(REPO), 'source': identity(HERE/'db6f-tail-review-closed-mesh.py'),
                'does_not_pay_original_seed_full_replay': True, 'executed': False})

    ids = {node['id'] for node in nodes}
    require(len(ids) == len(nodes), 'Duplicate command identity')
    for node in nodes:
        require(set(node['depends_on']) <= ids, 'Unknown command dependency')
        require(all(type(arg) is str for arg in node['argv']), 'Nonliteral executable argv')
    return {'commands': nodes, 'manifest_or_independent_input_templates': deferred_templates,
            'mutually_exclusive_final_routes': route_ids,
            'branch_selection_performed': False,
            'branch_policy': {
                'prefix': 'Compare actual epsilon*(1+eta)+eta with exact 1/500000000. Use complete baseline if sufficient; otherwise diagnose actual angular overestimate before original complete angular run.',
                'tail': 'Use full alone if sufficient. If metric-only is needed, run its complete coverage check with the same actual full curvature report and include its whole flag only in that route.',
                'storage': 'Actual single-container size failure may justify a separately reviewed new-storage plan in a new namespace. This v1 never switches source families.'}}


def build(args):
    run, out = args.run_directory.resolve(), args.out.resolve()
    require(run.parent == NOTES.resolve() and run.name.startswith('2026-11-10-78718-'),
            'Use a separately named immediate notes subdirectory')
    require(not run.exists(), 'Production directory must be entirely new')
    require(out.parent == NOTES.resolve() and not out.exists(), 'Plan output must be a new notes file')
    require(not out.is_relative_to(run), 'The plan must not precreate the future production directory')
    context, final, cp, tail = audited_success(args.launch, args.observed_execution, args.final_audit)
    fixed = verify_fixed_inputs()
    bindings = Bindings()
    for row in fixed['bindings']:
        for role in row['roles']:
            bindings.bound(row, role)
    for row in context['launch']['bindings']:
        bindings.bound(row, 'actual-success-launch-binding')
    for row in final['required_closed_files']:
        bindings.bound(row, 'actual-success-closed-output')
    bindings.bound(final['reproduction'], 'actual-success-reproduction')
    bindings.bound(final['root_observation'], 'actual-success-root-observation')
    for path, role in [(args.launch, 'actual-success-launch'), (args.observed_execution, 'actual-root-success-observation'),
                       (args.final_audit, 'saved-complete-final-audit'), (AUDITOR, 'complete-final-auditor'),
                       (Path(__file__), 'this-plan-source'), (Path(PYTHON), 'primary-python-binary'),
                       (Path(NODE), 'primary-node-binary')]:
        bindings.add(path, role)
    plan = command_plan(run, cp, tail, fixed)
    source_paths = {row['path'] for row in bindings.output()}
    for entry in plan['commands'] + plan['manifest_or_independent_input_templates']:
        require(entry['source']['path'] in source_paths, 'Unbound command source')
        for row in entry.get('additional_sources', []):
            require(row['path'] in source_paths, 'Unbound additional command source')
    return {'schema': '78718-post-m15-linear-success-only-original-plan-v1',
            'status': 'ACTUAL_MAIN_SUCCESS_BOUND_FUTURE_PRODUCTION_PLAN_ONLY',
            'plan_ready': True, 'mathematical_completion_claimed': False,
            'actual_solver_calls': 0, 'actual_production_calls': 0,
            'complete_final_audit_replayed': True,
            'full_final_status': final['status'], 'full_final_report': identity(args.final_audit),
            'root_actual_exit_observation': identity(args.observed_execution),
            'own_successful_checkpoint': identity(cp), 'own_final_audited_tail': identity(tail),
            'production_directory': str(run), 'production_directory_created': False,
            'directory_preparation': ['mkdir', '--', str(run)],
            'planner_python_version': sys.version,
            'cwd': str(REPO), 'environment': {'OPENBLAS_NUM_THREADS': '1', 'OMP_NUM_THREADS': '1',
                'MKL_NUM_THREADS': '1', 'NUMEXPR_NUM_THREADS': '1',
                'VISIBLE_FLEX_SOURCE_ROOT': str(SOURCE_ROOT),
                'CLOSING_TAIL_CACHE': str(SOURCE_ROOT/'topics/large-amplitude-twist-flex/scripts')},
            'terminal_bound_exact': TERMINAL_BOUND_EXACT,
            'ordinary_whole_1e_minus_6_is_not_terminal_success': True,
            'preexisting_bindings': bindings.output(),
            'fixed_input_roles': fixed['roles'],
            'terminal_reference_ready': fixed['terminal_reference_ready'],
            'terminal_reference_objects': fixed['terminal_reference_objects'],
            'terminal_reference_unknown_descendants': fixed['terminal_reference_unknown_descendants'],
            'future_output_hashes': None,
            'completion_rule_for_every_executed_stage':
                'Record actual argv/cwd/environment, natural exit, unchanged input/source hashes, complete own outputs and their hashes. Never infer completion from an active log or a partial manifest.',
            'remaining_final_obligations': [
                'Every selected downstream producer and continuous verifier must actually run for this own new graph.',
                'The normal terminal gate must pass exact 1/500000000 with the real original M12 lower-bound files.',
                'G5 refinement record and all README geometry/time conditions remain separate obligations.',
                'An uninvolved auditor must perform the actual frozen-seed solver-to-mesh workflow in fresh processes; metadata replay and same-plan mesh comparison do not replace it.',
                'The old matched M15 prefix remains UNSOLVED and its old local N256 DN is only a declared warm input; no independent final rerun is performed here.',
                'Finite numerical certificates do not prove the strict infinite-tail exact existence theorem.',
                'Continue the stronger amplitude/reach objectives after all basic completion conditions are actually paid.'],
            **plan}


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
              'complete_final_audit_replayed': False, 'production_commands_emitted': 0}
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
    print(json.dumps({k: report[k] for k in ('status', 'plan_ready', 'actual_solver_calls',
          'actual_production_calls', 'complete_final_audit_replayed', 'production_commands_emitted')}
          | {'output': identity(args.out)} | ({'reason': report['reason']} if 'reason' in report else {})))
    return code


if __name__ == '__main__':
    sys.exit(main())
