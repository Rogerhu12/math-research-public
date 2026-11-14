#!/usr/bin/env python3
"""Pure source/metadata/arithmetic checks for a conditional M14 export protocol.

No project module, numerical backend, exporter, transfer, geometry object,
solver, RK, root, or background factory is imported or executed.
Existing closed source records establish format only, never a new candidate.
"""
import ast
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
NOTES = TOPIC / 'notes'
NAME = '2026-11-09-db6f-tail-review-final-m14-w14-entry-and-export'
ROOT_NAME = '2026-11-09-db6f-root-final-m14-w14-entry-and-export'
sources = {}


def need(value, message):
    if not value:
        raise ValueError(message)


def identity(path):
    path = Path(path).resolve()
    size, h = 0, hashlib.sha256()
    with path.open('rb') as handle:
        for block in iter(lambda: handle.read(1 << 20), b''):
            size += len(block)
            h.update(block)
    row = {'path': str(path), 'bytes': size, 'sha256': h.hexdigest()}
    sources[str(path)] = row
    return row


def verify(row):
    need(identity(row['path']) == row, 'Changed source binding: ' + row['path'])


def read(path):
    identity(path)
    payload = Path(path).read_bytes()
    return json.loads(gzip.decompress(payload) if payload[:2] == b'\x1f\x8b' else payload)


def source(path):
    identity(path)
    return Path(path).read_text()


def assignment(path, name):
    matches = [node.value for node in ast.parse(source(path)).body
               if isinstance(node, ast.Assign) and
               any(isinstance(t, ast.Name) and t.id == name for t in node.targets)]
    need(len(matches) == 1, 'Missing unique top-level definition: ' + name)
    return matches[0]


def qconstant(path, name):
    node = assignment(path, name)
    need(isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'Q'
         and len(node.args) == 2 and not node.keywords, 'Not an explicit rational constant')
    return Fraction(*(ast.literal_eval(arg) for arg in node.args))


def exclusive(path, obj):
    with Path(path).open('x') as handle:
        json.dump(obj, handle, ensure_ascii=False, indent=2, allow_nan=False)
        handle.write('\n')


def main():
    publication_path = NOTES / (ROOT_NAME + '-publication.json')
    need(identity(publication_path)['sha256'] ==
         '8c27e37ff6d33c309352ef9c779fccc811c15ae18cb16d758a05263e655db7cb',
         'Root protocol publication changed')
    publication = read(publication_path)
    need(publication['file_count'] == len(publication['files']) == 2, 'Wrong publication count')
    for row in publication['files']:
        verify(row)
    need(identity(NOTES / (ROOT_NAME + '.md'))['sha256'] ==
         '174991707495b531b44e3f53fdf00de1c098d0d907b9ded28d9fa2162f59f060',
         'Root conditional note changed')
    root_sources = read(NOTES / (ROOT_NAME + '-sources.json'))
    need(len(root_sources['bindings']) == 24, 'Wrong root source count')
    for row in root_sources['bindings']:
        verify(row)

    # Existing real M14 records only: prove the input envelope distinction.
    launch = read(NOTES / '2026-11-09-db6f-prefix-spectral-true-m14q512-release-lu-01-launch.json')
    prefix_row, tail_row = launch['source_checkpoint'], launch['own_actual_tail_warm']
    verify(prefix_row)
    verify(tail_row)
    prefix, record = read(prefix_row['path']), read(tail_row['path'])
    response = record['response']
    staged = response['checkpoint']
    seam_tail = Path(prefix['tail_seam']['tail_record'])
    if not seam_tail.is_absolute():
        seam_tail = Path(prefix_row['path']).parent / seam_tail
    need(identity(seam_tail) == tail_row, 'Old real prefix and own final tail are not paired')
    need(type(prefix['parameters']) is list and len(prefix['parameters']) == 14 and 'states' not in prefix,
         'Unexpected prefix CP schema')
    need(type(staged['parameters']) is dict and staged['parameters']['modes'] == 14
         and staged['parameters']['shootingParts'] == 8 and
         len(staged['states']) == 865 and all(len(row) == 28 for row in staged['states']) and
         len(staged['rawStates']) == 13 and all(len(row) == 28 for row in staged['rawStates']),
         'Unexpected actual M14 staged-tail schema')
    need(record['request']['jacobian'] is True and record['request']['audit'] is True,
         'Old final source is not its true Jac/audit response')
    exporter = source(HERE / 'db6f-prefix-endpoint-critical-increment-export.mjs')
    for anchor in ('response=rec.response??rec,cp=response.checkpoint??response.tail_checkpoint??response.seam?.tail_checkpoint??response',
                   "if(!cp.parameters||!cp.states)throw Error('missing checkpoint')",
                   'M=p.modes,K=2*M', 'N>=2*degree+4',
                   'cp.rawNode[D]!==stages.cells.length',
                   'for(let m=-degree;m<=degree;m++)if((m-1)%3===0)planar.push(m)',
                   'length:M+1', 'stride=3+4*C',
                   'Math.ceil((xb-xa)*flowSteps)', 'start+=999', 'start+1000',
                   "if(bytes.length>=5000000)throw Error('packet exceeds 5 MB')"):
        need(anchor in exporter, 'Expected reviewed exporter interface missing: ' + anchor)

    # Exact integer arithmetic, independent of any curve/ODE evaluation.
    modes, degree, angular, maximum_rows = 14, 192, 512, 1000
    planar = [m for m in range(-degree, degree + 1) if (m - 1) % 3 == 0]
    height = [3 * j for j in range(modes + 1)]
    count = len(planar) + len(height)
    stride = 3 + 4 * count
    common_minimum = max(max(abs((m - 1) // 3) for m in planar), max(m // 3 for m in height))
    need((len(planar), len(height), count, stride, maximum_rows * stride * 8, common_minimum)
         == (128, 15, 143, 575, 4600000, 64), 'Wrong M14 layout arithmetic')
    need(angular >= 2 * degree + 4, 'Insufficient angular extraction count')

    # Read the already closed P8 proposal only; do not rerun plan-only,
    # which itself would evaluate background profiles and local increments.
    plan_path = NOTES / '2026-11-09-db6f-prefix-endpoint-grid-m15-quarter-p8-r0025-grid-plan.json'
    plan = read(plan_path)
    need(plan['status'] == 'numerical-grid-proposal-only', 'Wrong existing proposal status')
    for path, digest in plan['planningSourceSHA256'].items():
        need(identity(path)['sha256'] == digest, 'Changed original proposal source')
    need(identity(plan['input'])['sha256'] == plan['inputSHA256'], 'Changed existing quarter input')
    settings = {'depth': 8, 'steps': 32, 'grid': 'critical', 'criticalRatio': .05,
                'criticalBaseSteps': 64, 'criticalCells': [0], 'endpointRatio': .025,
                'flowSteps': 32, 'angularNodes': 512, 'degree': 192,
                'radialDifferenceStep': .00005, 'auditAngularNodes': 128,
                'auditFractions': [.25, .5, .75]}
    need(plan['settings'] == settings, 'Root proposed settings do not match existing P8 plan')
    stages = plan['gridPlan']
    unique_nodes = 1 + sum(row['nodes'] - 1 for row in stages)
    endpoints = [row for row in stages if row['endpointLayers']]
    need(len(stages) == 576 and unique_nodes == 21031 and len(endpoints) == 1,
         'Unexpected existing proposal counts')
    selected = {key: endpoints[0][key] for key in ('stage', 'rawCell', 'rawSegment', 'rawLeft', 'rawRight', 'nodes')}
    need(selected == dict(stage=15, rawCell=0, rawSegment=7, rawLeft=0, rawRight=.125, nodes=168),
         'Wrong source-coordinate restoration selector')

    producer = HERE / 'db6f-tail-transfer-background-v3.py'
    consumer = HERE / 'db6f-audit-closed-budget-transfer-v3.py'
    terminal = HERE / 'db6f-audit-terminal-error-gate.py'
    need(ast.literal_eval(assignment(consumer, 'TRANSFER_SHA256')) == identity(producer)['sha256'],
         'Consumer does not pin the reviewed paired transfer')
    background = ast.literal_eval(assignment(consumer, 'BACKGROUND_SHA256'))
    need(background == ast.literal_eval(assignment(terminal, 'BACKGROUND')) and
         set(background) == {'checkpoint', 'calibrations', 'alpha', 'cell_zero_A', 'inner_A', 'outer_B'},
         'Consumer and terminal disagree on the six frozen background definitions')
    for path in (producer, consumer, terminal):
        text = source(path)
        need("modes spacing depth physicalDepth steps quadrature linearFar" in text,
             'Expected approved numerical modes policy missing')
    terminal_sources = ast.literal_eval(assignment(terminal, 'SOURCES'))
    for name, digest in terminal_sources.items():
        need(identity(HERE / name)['sha256'] == digest, 'Changed normal terminal source: ' + name)
    normal = source(terminal)
    need("mode.add_argument('--whole'" in normal and 'upper <= BOUND' in normal
         and 'lower > FACTOR*upper' in normal and "fixed_g_convergence_gate_5_paid=False" in normal,
         'Normal terminal interface/scope changed')
    bound, factor, lower = (qconstant(terminal, key) for key in ('BOUND', 'FACTOR', 'LOWER'))
    need(bound == Fraction(1, 500000000) and lower - factor * bound > 0,
         'Original fixed terminal threshold/decrease constants differ')
    whole = source(HERE / 'db6f-root-whole-metric-reach-v2.py')
    need("metric <= Q(1, 10**6)" in whole and "'fixed_g_convergence_gate_5_paid': False" in whole,
         'Whole threshold/scope changed')
    common = source(HERE / 'db6f-root-common-cut-v2.py')
    need('max(abs((tail.planar_modes-1)//3))' in common and 'max(tail.height_modes//3)' in common,
         'Common-cut does not retain the actual complete tail modes')
    identity(NOTES / '2026-11-09-db6f-tail-review-spectral-true-m14-release-lu.md')
    identity(NOTES / '2026-11-09-db6f-tail-review-spectral-true-m14-release-lu-publication.json')
    identity(__file__)

    ledger_path = NOTES / (NAME + '-sources.json')
    frozen = sorted(sources.values(), key=lambda row: row['path'])
    exclusive(ledger_path, {'status': 'FROZEN_CONDITIONAL_PROTOCOL_REVIEW_SOURCE_LEDGER',
                           'reviewer': '/root/tail_review_continued_2', 'bindings': frozen, 'count': len(frozen),
                           'scope': 'Existing source, plan and old paired M14 records only. No future numeric object.'})
    output = NOTES / (NAME + '-check.json')
    report = {'status': 'PASS_CONDITIONAL_PROTOCOL_METADATA_AND_EXACT_ARITHMETIC',
              'scope': __doc__, 'root_source_bindings_verified': 24,
              'source_ledger': identity(ledger_path), 'source_count': len(frozen),
              'input_envelope': {'prefix': prefix_row, 'own_final_tail': tail_row,
                                'prefix_parameters': '14-element list; no staged states',
                                'tail_parameters': 'dictionary with M14/P8; 865x28 staged and 13x28 raw states',
                                'old_records_only': True, 'future_candidate_supplied': False},
              'M14_export_layout': {'planar_modes': len(planar), 'height_modes': len(height),
                                   'coefficient_count': count, 'stride': stride,
                                   'raw_bytes_at_1000_rows': maximum_rows * stride * 8,
                                   'minimum_common_cut_modes': common_minimum,
                                   'angular_512_satisfies_2degree_plus_4': True},
              'existing_P8_proposal': {'identity': identity(plan_path), 'stage_count': len(stages),
                                       'unique_nodes': unique_nodes, 'restoration_stage': selected,
                                       'settings': settings, 'future_M14_export_generated': False},
              'paired_transfer_source_verified': True,
              'terminal': {'normal_option': '--whole', 'threshold_exact': str(bound),
                           'fixed_old_lower_minus_factor_threshold_exact': str(lower - factor * bound),
                           'normal_candidate_branch_run': False, 'new_upper_bound_asserted': False},
              'actual_calls': {'solver': 0, 'root': 0, 'RK': 0, 'flow': 0, 'background_factory': 0,
                               'exporter': 0, 'transfer': 0, 'geometry': 0, 'continuous_backend': 0},
              'G5': False, 'README_completed': False}
    exclusive(output, report)
    print(json.dumps({'status': report['status'], 'report': identity(output),
                      'source_ledger': identity(ledger_path), 'source_count': len(frozen),
                      'actual_numerical_calls': 0}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
