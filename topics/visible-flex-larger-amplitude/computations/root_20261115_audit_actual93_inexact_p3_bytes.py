#!/usr/bin/env python3
"""Actual93 read-only JSON/byte audit, with no scientific recomputation.

Only transport, SHA256, exact decoded-JSON comparisons, binary64 serialization,
integer record/word counts and local file reads are used.  No numerical
package or scientific producer is imported; no norm, ratio, matrix action,
finite difference, scalar profile, equation, interval, SVD or solve is computed.
"""
from __future__ import annotations

import argparse
import ast
from collections import Counter, defaultdict
import gzip
import hashlib
import json
from pathlib import Path
import struct


ACTUAL = dict(run_id=43674264245,
    source_commit='8adc3251a8fe2ee7bcbc5d6d8381631b1558141e',
    job_id=132690828561, artifact_id=14145249554,
    artifact_name='visible-mainline-smallcoreresonance-43674264245-1',
    artifact_zip_bytes=620340,
    artifact_zip_sha256='16bb4f5542472de72a5d03ef72fc5da113c925de844ff4fbd8a7856f17662d37',
    job_conclusion='success')
TOPIC = 'topics/visible-flex-larger-amplitude/'
COMP = TOPIC+'computations/'
ENTRY = 'geometry_20261115_small_core_inexact_p3_restoration.py'
ENTRY_SHA = 'ce93a364f8423c89e9e696e1e2c96662b61c6daaf225bd51c44fcd572e05654e'
STATUS = 'small-core-inexact-p3-restoration/inexact-p3-restoration-status.json'
PINNED = {'small-core-inexact-p3-restoration/inexact-p3-restoration-status.json': (372627, '0913ea5d90ddb23bd408b33175887b5b24665fe0db8324d873bbe0b08c12a647'), 'request93-input-and-source-identity.json': (36295, '3753c83b2cc4c77189e9837af75e290329fe3c59c03615a2acab43812b080c1a'), 'exact-diagnostic-command.json': (3849, '9ef81c5f2b0b107f71cc09f72df39f1b26856e0123bcba065410c76d732e35c0'), 'public-source-preparation.json': (20424, 'fff395a4250ee029338a68a73b098c41ca98916a2bae73653803671a71b6c457'), 'small-core-resonance-readback.json': (21702, '404de15d168ddd45800b12207773fbf745642fdbbf99b875e96f239c8183a6c8'), 'large-arrays/complete-diagnostic-readback.json': (97529, 'e4ed56a106860b462c2b0879bfcbd940d54c6425b92c532dbd45aad13230b276'), 'prior-candidate/actual92-p3-inner-root-status.json': (498765, 'e822be884ac07e2b2c46ac7aba7f589ba5233e86cdbb33ad9c95108cc8dca01e'), 'small-core-inexact-p3-restoration/parent-status.json': (498765, 'e822be884ac07e2b2c46ac7aba7f589ba5233e86cdbb33ad9c95108cc8dca01e'), 'small-core-inexact-p3-restoration/circle-reference.json.gz': (140101, '36eb3f6e4c182893fac4f5860a07242ed27dd38ee071d9b2689125a3e5db40af'), 'small-core-inexact-p3-restoration/complete-scalar-domain.json.gz': (161830, '073739bcad3c7f7ae6748f8e059762b3d1557d0d6f34ed8c9583d1eb14812ec1'), 'small-core-inexact-p3-restoration/large-arrays/original-model-evaluations.jsonl': (1148511, '07ccdb8ce07fd32c07cb2b8b5c75292936d7612f4e9a98af31f9026957e596ec')}
PREVIOUS_BYTE_AUDIT = dict(file='2026-11-15-actual92-byte-audit.json.gz',
    bytes=65135,sha256='dca47829ec3202809cb96e615d0909796d0fa4bbc4471cdd944bdf2a79f31409')



def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def equal(a, b):
    if isinstance(a, bool) or isinstance(b, bool):
        return type(a) is bool and type(b) is bool and a is b
    if isinstance(a, dict) or isinstance(b, dict):
        return (isinstance(a, dict) and isinstance(b, dict) and a.keys() == b.keys()
                and all(equal(a[k], b[k]) for k in a))
    if isinstance(a, list) or isinstance(b, list):
        return (isinstance(a, list) and isinstance(b, list) and len(a) == len(b)
                and all(equal(x, y) for x, y in zip(a, b)))
    if isinstance(a, int) and isinstance(b, int):
        return a == b
    if isinstance(a, (float, int)) or isinstance(b, (float, int)):
        return (isinstance(a, (float, int)) and isinstance(b, (float, int))
                and struct.pack('<d', a) == struct.pack('<d', b))
    return type(a) is type(b) and a == b


def literal_subset(a, b):
    if isinstance(a, dict):
        return isinstance(b, dict) and a.keys() <= b.keys() and all(literal_subset(v,b[k]) for k,v in a.items())
    if isinstance(a, list):
        return isinstance(b,list) and len(a)==len(b) and all(literal_subset(x,y) for x,y in zip(a,b))
    return equal(a,b)


def arr(value, shape):
    if not shape:
        if isinstance(value, bool) or not isinstance(value, (float, int)):
            raise ValueError('Expected a numeric JSON leaf')
        return struct.pack('<d', value)
    if not isinstance(value, list) or len(value) != shape[0]:
        raise ValueError('Wrong stored array shape: '+repr(shape))
    return b''.join(arr(v, shape[1:]) for v in value)


def array_receipt(value, shape, label):
    raw = arr(value, tuple(shape))
    classes = Counter()
    for word, in struct.iter_unpack('<Q', raw):
        exponent = (word >> 52) & 2047
        fraction = word & ((1 << 52)-1)
        if exponent == 2047:
            classes['nan' if fraction else 'infinity'] += 1
        else:
            classes['finite'] += 1
        if word & ((1 << 63)-1) == 0:
            classes['negative_zero' if word >> 63 else 'positive_zero'] += 1
    return dict(label=label, shape=list(shape), dtype='<f8', order='C',
                bytes=len(raw), raw_sha256=sha(raw), words=len(raw)//8,
                word_classes=dict(classes),
                scope='JSON-decoded binary64 words; no mathematical operation')


def dump(path, obj):
    raw = (json.dumps(obj, ensure_ascii=False, sort_keys=True, indent=2,
                      allow_nan=False)+'\n').encode()
    if path.suffix == '.gz':
        raw = gzip.compress(raw, mtime=0)
    path.write_bytes(raw)
    return dict(file=path.name, bytes=len(raw), sha256=sha(raw))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--artifact-directory', type=Path, required=True)
    parser.add_argument('--repository', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--previous-audit', type=Path, required=True)
    args = parser.parse_args()
    root, out = args.artifact_directory.resolve(), args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    checks, sources, arrays, public_cache = [], [], [], {}

    def check(name, ok, **details):
        checks.append(dict(check=name, passed=bool(ok), **details))
        if not ok:
            raise AssertionError(name)

    def same(name, a, b):
        check(name, equal(a, b))

    def read(relative):
        p = root/relative
        if p.is_symlink() or root not in p.resolve().parents:
            raise ValueError('Not an ordinary file within this artifact')
        return p.read_bytes()

    def load(relative):
        raw = read(relative)
        return json.loads(gzip.decompress(raw) if raw.startswith(b'\x1f\x8b') else raw)

    def public_raw(path):
        if path not in public_cache:
            target = args.repository/path
            if not target.is_file() or target.is_symlink():
                raise FileNotFoundError(path)
            public_cache[path] = target.read_bytes()
        return public_cache[path]

    def public_checked(path, expected, label):
        local = args.repository/path
        if path not in public_cache and local.is_file():
            candidate = local.read_bytes()
            if sha(candidate) == expected['sha256']:
                public_cache[path] = candidate
        raw = public_raw(path)
        check(label, sha(raw) == expected['sha256'] and
              ('bytes' not in expected or len(raw) == expected['bytes']),
              file=path, bytes=len(raw), sha256=sha(raw))
        return raw

    def desc(relative, expected, label):
        raw = read(relative)
        check(label, len(raw) == expected['bytes'] and sha(raw) == expected['sha256'])
        return raw

    inventory = []
    for p in sorted(root.rglob('*')):
        if not p.is_file():
            continue
        rel = p.relative_to(root).as_posix()
        check('artifact ordinary member '+rel, not p.is_symlink())
        raw = p.read_bytes()
        inventory.append(dict(file=rel, bytes=len(raw), sha256=sha(raw)))
    for rel, (size, digest) in PINNED.items():
        desc(rel, dict(bytes=size, sha256=digest), 'pinned original '+rel)

    status_raw = read(STATUS)
    s = json.loads(status_raw)
    base = 'small-core-inexact-p3-restoration/'
    identity = load('request93-input-and-source-identity.json')
    request = identity['request']
    prep = load('public-source-preparation.json')
    command = load('exact-diagnostic-command.json')
    readback = load('small-core-resonance-readback.json')
    parent = load('prior-candidate/actual92-p3-inner-root-status.json')
    circle = load(base+'circle-reference.json.gz')
    scalar = load(base+'complete-scalar-domain.json.gz')
    same('identity source commit', identity['source_commit'], ACTUAL['source_commit'])
    same('scientific producer SHA', s['source_sha256'], ENTRY_SHA)
    same('request number', request['request_number'], 93)
    reqraw = public_checked(COMP+'public-small-core-resonance-request.json',
                         dict(sha256=identity['request_sha256']), 'original request bytes, matching local source checkout')
    same('request full JSON', request, json.loads(reqraw))
    check('72 requested sources', len(identity['verified_sources']) == 72 and
          len(request['source_sha256']) == 72)
    for r in identity['verified_sources']:
        same('request source pin '+r['file'], r['sha256'], request['source_sha256'][r['file']])
        path = COMP+r['file']
        raw = public_checked(path, r, 'actual source bytes '+r['file'])
        sources.append(dict(file=path, bytes=len(raw), sha256=sha(raw),
                            consumed_by_new_producer=r['file'] in s['consumed_source_sha256']))
    check('13 consumed source identities', len(s['consumed_source_sha256']) == 13)
    for name, digest in s['consumed_source_sha256'].items():
        same('consumed source '+name, digest, request['source_sha256'][name])
    source_tree = ast.parse(public_raw(COMP+ENTRY).decode())
    constants = {}
    def source_literal(node):
        if isinstance(node, ast.Name):
            return constants[node.id]
        if isinstance(node, ast.Dict):
            return {source_literal(k):source_literal(v) for k,v in zip(node.keys,node.values)}
        return ast.literal_eval(node)
    for node in source_tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            if node.targets[0].id in ('FROZEN', 'ORIGINAL_INPUTS', 'ENTRY_NAME', 'SCHEMA',
                                     'RESUME_NAME','ORIGINAL_NAME','ORIGINAL_SHA256','PREVIOUS_NAME','PREVIOUS_SCHEMA',
                                     'ACTUAL92_STATUS_BYTES','ACTUAL92_STATUS_SHA256'):
                constants[node.targets[0].id] = source_literal(node.value)
    same('actual producer source schema', s['schema'], constants['SCHEMA'])
    same('actual producer source basename', ENTRY, constants['ENTRY_NAME'])
    same('producer full input pins', s['input_sha256'], constants['ORIGINAL_INPUTS'])
    same('producer consumed source closure', s['consumed_source_sha256'],
         {**constants['FROZEN'], ENTRY:ENTRY_SHA})
    proof_receipts = []
    for r in request['proofs']:
        target = args.repository/r['file']
        if target.is_file():
            public_checked(r['file'], r, 'declared proof/interface '+r['file'])
            proof_receipts.append(dict(**r, local_payload_verified=True))
        else:
            proof_receipts.append(dict(**r, local_payload_verified=False,
                scope='Original request receipt only; optional proof document not restored again locally'))
    previous_raw = args.previous_audit.read_bytes()
    check('actual92 complete byte audit original bytes',
          len(previous_raw) == PREVIOUS_BYTE_AUDIT['bytes'] and sha(previous_raw) == PREVIOUS_BYTE_AUDIT['sha256'])
    previous = json.loads(gzip.decompress(previous_raw))
    check('actual92 byte audit completed', previous['all_checks_passed'] is True)
    previous_inputs = {r['name']:r for r in previous['original_inputs']}
    same('public78 source commit', prep['actual_public_commit'], ACTUAL['source_commit'])
    same('public78 file count', len(prep['restored_files']), prep['verified_file_count'])
    same('public78 declared count', prep['verified_file_count'], 78)
    dependency_manifest = json.loads(public_raw(COMP+'source-dependencies.json'))
    same('public78 source manifest identity', sha(public_raw(COMP+'source-dependencies.json')),
         prep['source_manifest_sha256'])
    subset = [{k:r[k] for k in ('path','bytes','sha256')} for r in dependency_manifest['files']
              if r['path'].startswith('topics/visible-flexible-closed-surface/')
              and r['path'] != prep['omitted_unconsumed_client']['path']]
    same('complete public78 runtime receipts against frozen manifest', prep['restored_files'], subset)
    restored = []
    for r in prep['restored_files']:
        restored.append(dict(**r, scope='Original Actions receipt and frozen complete source manifest compared; no second local payload restoration'))
    input_records, input_objects = [], {}
    for r in identity['verified_original_inputs']:
        declared = request['inputs'][r['name']]
        same('original input descriptor '+r['name'], {k:v for k,v in r.items() if k != 'name'}, declared)
        same('original input runtime pin '+r['name'], s['input_sha256'][r['name']], r['sha256'])
        target = args.repository/r['file']
        earlier = previous_inputs[r['name']]
        same('same original input previously byte audited '+r['name'],
             {k:earlier[k] for k in ('name','file','bytes','sha256')}, r)
        check('previous complete input payload paid '+r['name'], earlier['verified_entire_public_file'] is True)
        if target.is_file():
            raw = public_checked(r['file'], r, 'full mathematical input bytes '+r['name'])
            input_records.append(dict(**r, verified_entire_public_file=True,
                previous_actual92_complete_payload_verified=True))
            input_objects[r['name']] = json.loads(gzip.decompress(raw) if raw.startswith(b'\x1f\x8b') else raw)
        else:
            input_records.append(dict(**r, verified_entire_public_file=False,
                previous_actual92_complete_payload_verified=True,
                scope='Same complete input SHA as independently byte-audited actual92; no second local payload download or scientific reconstruction'))
    prior = identity['verified_prior_candidate']['original_status']
    parent_raw = read('prior-candidate/actual92-p3-inner-root-status.json')
    check('actual92 parent matches complete public descriptor',len(parent_raw)==prior['bytes'] and sha(parent_raw)==prior['sha256'])
    same('both preserved actual92 original copies', parent_raw, read(base+'parent-status.json'))
    prior_receipt = next(r for r in previous['inventory'] if r['file'] == 'small-core-p3-inner-root/p3-inner-root-status.json')
    same('parent is the previous independently byte-audited original status',
         {k:prior_receipt[k] for k in ('bytes','sha256')}, {k:prior[k] for k in ('bytes','sha256')})
    same('parent only literal final parameters', s['parent_status']['literal_parameters'], parent['final']['parameters'])
    same('current fresh initial parameters', s['initial']['parameters'], parent['final']['parameters'])
    same('same original immutable zero-tail Jacobian metadata',
         s['initial']['zero_tail_slope_J'], parent['final']['zero_tail_slope_J'])
    same('final same original immutable zero-tail Jacobian metadata',
         s['final']['zero_tail_slope_J'], s['initial']['zero_tail_slope_J'])
    same('request initial parameters', request['diagnostic']['parameters'], parent['final']['parameters'])
    check('parent J and merit explicitly not reused',
          s['parent_status']['saved_parent_J_merit_state_or_FD_reused'] is False and
          s['initial_model_evaluation_and_description_are_fresh'] is True)
    same('command source chain', command['source_chain'], request['source_chain'])
    same('command parameters', command['parameters'], request['diagnostic'])
    check('old LM direction engines not executed', command['parent_three_coordinate_direction_engine_executed'] is False)
    same('readback original status descriptor', readback['original_status'],
         dict(file=STATUS, bytes=len(status_raw), sha256=sha(status_raw)))
    for k in readback.keys() & s.keys():
        check('literal readback field '+k, literal_subset(readback[k], s[k]))
    complete_readback = load('large-arrays/complete-diagnostic-readback.json')
    check('complete readback descriptor from small readback',
          len(read('large-arrays/complete-diagnostic-readback.json')) == readback['complete_readback_bytes'] and
          sha(read('large-arrays/complete-diagnostic-readback.json')) == readback['complete_readback_sha256'])
    for packet_name, packet in [('bounded',readback),('complete',complete_readback)]:
        for k,v in packet.items():
            if k in s:
                check(packet_name+' readback field '+k,literal_subset(v,s[k]))
        check(packet_name+' initial projection summary',literal_subset(packet['initial_projection_summary'],s['initial_projection']))
        for i,item in enumerate(packet['outer_search_summary']):
            for k,v in item.items():
                if k != 'trials':
                    check(packet_name+' outer '+str(i)+'/'+k,literal_subset(v,s['searches'][i][k]))
                else:
                    for j,t in enumerate(v):
                        check(packet_name+' outer trial '+str(i)+'/'+str(j),literal_subset(t,s['searches'][i]['trials'][j]))

    ledger_raw = desc(base+s['original_call_trace']['file']['file'],
                      s['original_call_trace']['file'], 'complete event ledger bytes')
    events = [json.loads(line) for line in ledger_raw.splitlines()]
    contexts = defaultdict(list)
    kinds, eval_counts, exception_types = Counter(), Counter(), Counter()
    for n, e in enumerate(events, 1):
        same('event ordering '+str(n), e['event_number'], n)
        check('event observer scope '+str(n), e['this_event_does_not_accept_an_outer_candidate'] is True)
        contexts[e['context']].append(e)
        kinds[e['kind']] += 1
        if e['kind'].startswith('original_evaluate_'):
            eval_counts['evaluation_attempts'] += 1
            eval_counts['real_evaluation_attempts' if e['real_parameters'] else 'complex_evaluation_attempts'] += 1
            if e['kind'] == 'original_evaluate_return':
                eval_counts['evaluation_returns'] += 1
            else:
                eval_counts['evaluation_exceptions'] += 1
                exception_types[e['original_exception_class']+': '+e['exception']] += 1
        if e['kind'].startswith('original_jacobian_'):
            eval_counts['jacobian_attempts'] += 1
            if e['kind'] == 'original_jacobian_return':
                eval_counts['jacobian_returns'] += 1
    eval_counts['description_attempts'] = 2
    same('all evaluation event counters', {k:eval_counts[k] for k in s['original_call_trace']['counts']}, s['original_call_trace']['counts'])
    same('all event count', len(events), s['original_call_trace']['events'])
    same('no observer errors', s['original_call_trace']['observer_errors'], [])
    evaluation_events = [e for e in events if e['kind'].startswith('original_evaluate_')]
    jacobian_events = [e for e in events if e['kind'].startswith('original_jacobian_')]
    same('evaluation index full sequence', [e['evaluation_index'] for e in evaluation_events],
         list(range(1, len(evaluation_events)+1)))
    same('Jacobian index full sequence', [e['jacobian_index'] for e in jacobian_events],
         list(range(1, len(jacobian_events)+1)))

    def event(context, kind):
        found = [e for e in contexts[context] if e['kind'] == kind]
        check('unique event '+context+'/'+kind, len(found) == 1)
        return found[0]

    def match_state(label, saved, observed):
        same(label, saved, observed)

    fresh = event('fresh-parent-state', 'original_evaluate_return')['returned']
    initialJ = event('fresh-parent-original-description-FD', 'original_jacobian_return')
    finalJ = event('final-original-description-FD', 'original_jacobian_return')
    for label, description, je in [('initial', s['initial'], initialJ), ('final', s['final'], finalJ)]:
        same(label+' J actual parameter binding', description['parameters'], je['parameters'])
        same(label+' actual complete J', description['three_by_three_parameter_jacobian'],
             je['original_full_three_by_three_jacobian'])
        arrays.append(array_receipt(description['three_by_three_parameter_jacobian'], [3,3], label+'/original-J'))
    for k in ('parameters','unit_diagonal_defects','low_equations_used',
              'complete_first_order_right_residual','full_first_order_native_height'):
        same('fresh initial '+k, s['initial'][k], fresh[k])
    same('fresh initial original merit', s['initial_original_three_equation_merit'], fresh['original_three_equation_merit'])

    inner, inner_literal, final_inner_word_readout = {}, [], []
    step_total = trial_total = accepted_inner_total = 0
    inner_failures = Counter()
    all_J_contexts = set()
    for number, receipt in enumerate(s['inner_reports'], 1):
        same('inner call ordering '+str(number), receipt['inner_call'], number)
        raw = desc(base+receipt['file'], receipt, 'complete inner report '+str(number))
        decoded = gzip.decompress(raw)
        report = json.loads(decoded)
        inner[number] = report
        for k in ('label','inner_call','usable_inner_root','usable_restoration_point','residual_tolerance_met',
                  'original_full_J_finite','original_J33_finite_nonzero','stop_reason','seconds','original_call_cost'):
            same('inner summary '+str(number)+'/'+k, receipt[k], report[k])
        same('inner final summary '+str(number), receipt['last_probe'], report.get('last_probe'))
        check('inner never outer acceptance '+str(number), report['accepted_outer_state'] is False)
        same('inner first two fixed '+str(number), report['fixed_first_two_parameters'], report['seed_parameters'][:2])
        check('each inner seed evaluated freshly '+str(number), report['seed_is_reused_fresh_state'] is False)
        es = contexts[report['label']+'/seed']
        check('one real inner seed call '+str(number), len(es) == 1 and es[0]['real_parameters'] is True)
        same('inner seed point '+str(number), es[0]['parameters'], report['seed_parameters'])
        if 'initial' in report:
            match_state('inner initial event '+str(number), report['initial'], es[0]['returned'])
        else:
            same('inner seed exception '+str(number), report['domain_or_cell_error'], es[0]['exception'])
        current = report.get('initial')
        linked_steps = []
        for expected_index, step in enumerate(report['steps']):
            tag = str(number)+'/'+str(expected_index)
            same('inner step order '+tag, step['iteration'], expected_index)
            match_state('inner step state continuity '+tag, step['point'], current)
            same('inner current fixed coordinates '+tag, step['point']['parameters'][:2], report['fixed_first_two_parameters'])
            ctx = report['label']+'/inner-'+str(expected_index)+'/original-full-J'
            je = event(ctx, 'original_jacobian_return')
            all_J_contexts.add(ctx)
            same('inner J actual point '+tag, je['parameters'], step['point']['parameters'])
            same('inner full J event '+tag, je['original_full_three_by_three_jacobian'], step['original_full_three_by_three_jacobian'])
            same('inner J33 is stored matrix entry '+tag, step['original_J33'], step['original_full_three_by_three_jacobian'][2][2])
            arrays.append(array_receipt(step['original_full_three_by_three_jacobian'], [3,3], 'inner-'+tag+'/J'))
            accepted = []
            for ti, trial in enumerate(step['trials']):
                tt = tag+'/'+str(ti)
                same('inner trial order '+tt, trial['trial'], ti)
                same('inner trial fixed coordinates '+tt, trial['parameters'][:2], report['fixed_first_two_parameters'])
                context = report['label']+'/inner-'+str(expected_index)+'/trial-'+str(ti)
                ee = contexts[context]
                check('one original inner trial event '+tt, len(ee) == 1 and ee[0]['real_parameters'] is True)
                same('inner trial actual parameters '+tt, trial['parameters'], ee[0]['parameters'])
                if 'point' in trial:
                    match_state('inner trial full original return '+tt, trial['point'], ee[0]['returned'])
                else:
                    same('inner trial original exception '+tt, trial['domain_or_cell_error'], ee[0]['exception'])
                check('inner trial not outer acceptance '+tt, trial['outer_candidate_accepted'] is False)
                if trial['inner_step_accepted']:
                    accepted.append(trial)
                    current = trial['point']
                trial_total += 1
            check('inner at most one accepted step '+tag, len(accepted) <= 1)
            same('inner step accepted flag '+tag, step['inner_step_accepted'], bool(accepted))
            if accepted:
                check('accepted inner trial was final attempted trial '+tag, accepted[0] is step['trials'][-1])
                accepted_inner_total += 1
            linked_steps.append(dict(iteration=step['iteration'], original_J_event_number=je['event_number'],
                point=step['point'], original_J33=step['original_J33'],
                p3_newton_direction=step.get('p3_newton_direction'),
                inner_step_accepted=step['inner_step_accepted'], trials=step['trials']))
            step_total += 1
        same('inner last actual state continuity '+str(number), report.get('last_probe'), current)
        same('final J parameter identity '+str(number),report['final_J_parameter_identity'],current['parameters'])
        if report['original_final_J_reused_only_at_exact_same_fresh_point']:
            same('final J is stored same-current last step J '+str(number),
                 report['final_original_full_three_by_three_jacobian'],report['steps'][-1]['original_full_three_by_three_jacobian'])
            same('final J same-current parameter words '+str(number),
                 current['parameters'],report['steps'][-1]['point']['parameters'])
        else:
            ctx = report['label']+'/last-actual-point-original-full-J'
            je = event(ctx,'original_jacobian_return')
            all_J_contexts.add(ctx)
            same('fresh final J original event '+str(number),je['original_full_three_by_three_jacobian'],report['final_original_full_three_by_three_jacobian'])
            same('fresh final J point '+str(number),je['parameters'],current['parameters'])
        check('inner last point eligible independently of root flag '+str(number), report['usable_restoration_point'] is True)

        selected = [e for e in events if e['context'].startswith(report['label']+'/')]
        cost = Counter()
        for e in selected:
            if e['kind'].startswith('original_evaluate_'):
                cost['evaluation_attempts'] += 1
                cost['real_evaluation_attempts' if e['real_parameters'] else 'complex_evaluation_attempts'] += 1
                cost['evaluation_returns' if e['kind']=='original_evaluate_return' else 'evaluation_exceptions'] += 1
            if e['kind'].startswith('original_jacobian_'):
                cost['jacobian_attempts'] += 1
                if e['kind']=='original_jacobian_return':cost['jacobian_returns'] += 1
        observed_cost = {k:cost[k] for k in report['original_call_cost']}
        same('inner original cost from events '+str(number), observed_cost, report['original_call_cost'])
        inner_failures[report['stop_reason']] += 1
        inner_literal.append(dict(receipt=receipt, decoded_bytes=len(decoded), decoded_sha256=sha(decoded),
            inner_call=number, label=report['label'], seed_parameters=report['seed_parameters'],
            usable_inner_root=report['usable_inner_root'], usable_restoration_point=report['usable_restoration_point'],
            final_original_full_three_by_three_jacobian=report['final_original_full_three_by_three_jacobian'],
            final_J_parameter_identity=report['final_J_parameter_identity'], stop_reason=report['stop_reason'],
            last_probe=report.get('last_probe'), steps=linked_steps,
            original_call_cost=report['original_call_cost']))
        if report['steps']:
            last = report['steps'][-1]
            current_words = arr(last['point']['parameters'], [3])
            rows = []
            for trial in last['trials']:
                rows.append(dict(trial=trial['trial'], alpha=trial['alpha'],
                    parameters=trial['parameters'],
                    parameters_equal_to_current_bits=arr(trial['parameters'],[3]) == current_words,
                    returned_d3=(trial.get('point') or {}).get('low_equations_used',[None,None,None])[2],
                    returned_d3_equal_to_current_bits=(equal(trial['point']['low_equations_used'][2],
                        last['point']['low_equations_used'][2]) if 'point' in trial else None),
                    original_domain_error=trial.get('domain_or_cell_error')))
            final_inner_word_readout.append(dict(inner_call=number,label=report['label'],
                current_parameters=last['point']['parameters'],current_parameters_raw_sha256=sha(current_words),
                current_d3=last['point']['low_equations_used'][2],
                saved_p3_newton_direction=last.get('p3_newton_direction'),trials=rows,
                identical_parameter_trial_count=sum(row['parameters_equal_to_current_bits'] for row in rows),
                scope='Only stored parameter and residual word equality; no subtraction, ULP or new evaluation'))
    same('all inner count', len(inner), s['inner_call_count'])
    check('all current inner J events accounted for',
          len(all_J_contexts)+2 == s['original_call_trace']['counts']['jacobian_returns'])

    projection = s['initial_projection']
    check('no initial projection of fresh parent',projection['performed'] is False and projection['fresh_original_parent_retained'] is True)
    current = fresh
    currentJ = initialJ['original_full_three_by_three_jacobian']
    outer_count, outer_accepted = 0, 0
    outer_rows, all_outer_points = [], []
    for index, search in enumerate(s['searches']):
        same('outer order '+str(index), search['iteration'], index)
        same('outer state parameter continuity '+str(index), search['parameters'], current['parameters'])
        same('outer state original residual continuity '+str(index), search['residual'], current['low_equations_used'])
        same('outer original merit continuity '+str(index), search['merit_before'], current['original_three_equation_merit'])
        same('outer actual complete J continuity '+str(index), search['derivative'], currentJ)
        model = search['direction_model']
        same('model original J '+str(index), model['original_full_three_by_three_jacobian'], currentJ)
        same('model original actual residual '+str(index), model['original_residual'], current['low_equations_used'])
        same('model actual d3 not replaced '+str(index), model['actual_original_third_unit_residual'], current['low_equations_used'][2])
        same('outer actual d3 alias '+str(index), search['actual_third_unit_residual'], current['low_equations_used'][2])
        same('model actual J33 alias '+str(index), model['original_J33'], currentJ[2][2])
        same('model retained third linear residual alias '+str(index),
             model['third_linear_residual_not_overwritten'],model['full_linear_residual_after_direction'][2])
        same('model retained third action alias '+str(index),
             model['original_full_Jd_third_component'],model['original_full_J_times_direction'][2])
        same('model spectrum retained third residual alias '+str(index),
             model['same_model_spectrum']['original_third_residual_retained_in_normal_correction'],current['low_equations_used'][2])
        same('full true model slope alias '+str(index), model['original_full_three_merit_model_slope'], search['true_model_merit_slope'])
        for key, shape in [('schur_matrix',[2,2]),('scaled_schur_matrix',[2,2]),
            ('augmented_matrix',[4,2]),('augmented_rhs',[4]),('coordinate_scale',[2]),
            ('lifted_original_three_parameter_direction',[3]),('original_full_J_times_direction',[3])]:
            arrays.append(array_receipt(model[key], shape, 'outer-'+str(index)+'/'+key))
        accepted = []
        tr = []
        for ti, trial in enumerate(search['trials']):
            number = trial['inner']['inner_call']
            report = inner[number]
            same('outer inner receipt '+str(number), trial['inner'], s['inner_reports'][number-1])
            same('outer inner label '+str(number), report['label'], 'outer-'+str(index)+'/trial-'+str(ti))
            same('outer actual inner seed '+str(number), trial['predicted_seed_parameters'], report['seed_parameters'])
            if report['usable_restoration_point']:
                match_state('outer actual candidate '+str(number), trial['actual_projected_point'], report['last_probe'])
                same('outer candidate actual full merit '+str(number), trial['actual_merit'], report['last_probe']['original_three_equation_merit'])
                same('outer nonzero d3 literal '+str(number), trial['true_third_unit_residual_preserved'], report['last_probe']['low_equations_used'][2])
                same('outer actual inner threshold flag '+str(number),trial['inner_unit_threshold_met'],report['residual_tolerance_met'])
                check('outer preserves actual restoration rather than replacing seed '+str(number),
                      trial['original_seed_direction_not_relabelled_as_actual_restoration_displacement'] is True)
            else:
                check('unusable inner not promoted '+str(number),
                      trial['accepted'] is False and 'actual_projected_point' not in trial and 'actual_merit' not in trial)
            if trial['accepted']:
                accepted.append(trial)
                current = trial['actual_projected_point']
                currentJ = report['final_original_full_three_by_three_jacobian']
                outer_accepted += 1
            tr.append(dict(outer_iteration=index, trial=ti, alpha=trial['alpha'], inner_call=number,
                usable_inner_root=report['usable_inner_root'], usable_restoration_point=report['usable_restoration_point'],
                inner_unit_threshold_met=trial.get('inner_unit_threshold_met'),outer_accepted=trial['accepted'],
                reason=trial['reason'], original_Armijo_bound=trial['original_Armijo_bound'],
                actual_merit=trial.get('actual_merit'), predicted_seed_parameters=trial['predicted_seed_parameters'],
                actual_total_parameter_displacement=trial.get('actual_total_parameter_displacement'),
                actual_restoration_displacement_from_seed=trial.get('actual_restoration_displacement_from_seed'),
                last_inner_probe=report.get('last_probe')))
            outer_count += 1
        same('outer accepted flag '+str(index), search['accepted'], bool(accepted))
        check('outer at most one acceptance '+str(index), len(accepted) <= 1)
        if accepted:check('outer accepted last trial '+str(index), accepted[0] is search['trials'][-1])
        outer_rows.append(dict(iteration=index, parameters=search['parameters'], residual=search['residual'],
            merit_before=search['merit_before'], true_model_merit_slope=search['true_model_merit_slope'],
            direction_model=model, trials=tr, accepted=search['accepted']))
        all_outer_points.extend(tr)
    same('last accepted parameters', s['last_accepted_parameters'], current['parameters'])
    same('last accepted original merit', s['final_original_three_equation_merit'], current['original_three_equation_merit'])
    for k in ('parameters','unit_diagonal_defects','low_equations_used',
              'complete_first_order_right_residual','full_first_order_native_height'):
        same('final original '+k, s['final'][k], current[k])
    same('final fresh J at final accepted point', finalJ['parameters'], current['parameters'])
    final_repeated_J_words_equal = equal(finalJ['original_full_three_by_three_jacobian'], currentJ)

    for label in ('initial','final'):
        for key, shape in [('parameters',[3]),('unit_diagonal_defects',[3]),
            ('complete_first_order_right_residual',[112]),('full_first_order_native_height',[112]),
            ('singular_values',[3])]:
            arrays.append(array_receipt(s[label][key], shape, label+'/'+key))
        high_words = arr(s[label]['complete_first_order_right_residual'][3:], [109])
        check(label+' recorded high109 right words are signed zeros only',
              all(word & ((1<<63)-1) == 0 for word, in struct.iter_unpack('<Q', high_words)))
    if 'tail_anchor' in input_objects:
        anchor = input_objects['tail_anchor']
        HJ = anchor['heightJetJacobian']
        check('true complete anchor Jacobian flat 338x112', isinstance(HJ, list) and len(HJ)==338*112)
        J112 = [HJ[k*112:(k+1)*112] for k in range(112)]
        arrays.append(array_receipt(J112,[112,112],'original-zero-tail-slope-J112'))
        check('original complete J112 offdiagonal words exactly signed zero',
              all(struct.unpack('<Q',struct.pack('<d',J112[i][j]))[0] & ((1<<63)-1) == 0
                  for i in range(112) for j in range(112) if i!=j))
    if 'accepted' in input_objects:
        same('target original first three', s['final']['source_target_first_three'], input_objects['accepted']['core']['coefficients'][:3])
    same('zero-core circle targets remain explicitly distinct', circle['fixed_core_targets'], [0.0,0.0,0.0])
    check('zero-core reference does not retain original large-core targets',
          circle['original_large_core_targets_retained'] is False)
    same('circle final actual parameter identity', circle['complete_scalar_profile']['frozen_design_parameters'], s['final']['parameters'])
    for key, shape in [('mesh',[699]),('states',[699,453]),('rhs',[699,453]),
                       ('low_three_unit_modes_UH',[699,3,2]),('low_three_unit_modes_rhs_UH',[699,3,2])]:
        arrays.append(array_receipt(circle[key], shape, 'circle/'+key))
    if 'prepared' in input_objects:
        same('circle original mesh', circle['mesh'], input_objects['prepared']['mesh'])
    same('circle actual full domain readout', circle['actual_original_residual_and_domain'], s['original_complete_circle_check']['actual_domain'])
    same('circle full FFT checks', circle['original_full_FFT_tangent_checks'], s['original_complete_circle_check']['original_full_FFT_tangent_checks'])
    same('circle compressed identity', sha(read(base+'circle-reference.json.gz')), s['original_complete_circle_check']['reference_sha256'])
    for k,v in s['complete_scalar_domain'].items():
        same('final original scalar report '+k, v, scalar[k])
    same('scalar all leaf count', len(scalar['leaves']), scalar['leaf_count'])
    check('all original scalar leaf success flags preserved', all(
        leaf['strict_positive_radius_and_abs_ap_lt_one'] is True and
        leaf['definite_scalar_domain_failure'] is False for leaf in scalar['leaves']))
    same('scalar first endpoint literal', scalar['leaves'][0]['interval'][0], scalar['covered_interval'][0])
    same('scalar last endpoint literal', scalar['leaves'][-1]['interval'][1], scalar['covered_interval'][1])
    check('scalar exact endpoint text adjacency', all(
        scalar['leaves'][j]['interval'][1] == scalar['leaves'][j+1]['interval'][0]
        for j in range(len(scalar['leaves'])-1)))

    original_copies = []
    for name, raw in [
        ('2026-11-15-actual93-original-complete-status.json.gz', status_raw),
        ('2026-11-15-actual93-original-evaluation-ledger.jsonl.gz', ledger_raw)]:
        compressed = gzip.compress(raw, mtime=0)
        (out/name).write_bytes(compressed)
        check('lossless original copy '+name, gzip.decompress(compressed)==raw)
        original_copies.append(dict(file=name,bytes=len(compressed),sha256=sha(compressed),
                                    decoded_bytes=len(raw),decoded_sha256=sha(raw)))
    inner_name = '2026-11-15-actual93-original-inner-reports.json.gz'
    inner_combined = b'[\n'+b',\n'.join(gzip.decompress(read(base+r['file'])).strip() for r in s['inner_reports'])+b'\n]\n'
    compressed = gzip.compress(inner_combined, mtime=0)
    (out/inner_name).write_bytes(compressed)
    same('all inner full original records lossless JSON transport', json.loads(gzip.decompress(compressed)), [inner[n] for n in range(1,len(inner)+1)])
    original_copies.append(dict(file=inner_name,bytes=len(compressed),sha256=sha(compressed),
        decoded_bytes=len(inner_combined),decoded_sha256=sha(inner_combined),
        scope='All complete original inner JSON objects, joined without altering their numeric tokens'))
    counts = dict(local_inventory_files=len(inventory),
        original_artifact_members=len([r for r in inventory if r['file'] != '.download-complete']),
        local_transport_markers=len([r for r in inventory if r['file'] == '.download-complete']),
        requested_source_files=len(sources),
        consumed_source_files=len(s['consumed_source_sha256']), restored_public_source_receipts=len(restored),
        original_mathematical_inputs=len(input_records),
        same_input_payloads_previously_verified_in_actual92=sum(r['previous_actual92_complete_payload_verified'] for r in input_records),
        complete_mathematical_input_payloads_locally_verified=sum(r['verified_entire_public_file'] for r in input_records),
        original_inner_reports=len(inner),
        inner_original_J_records=step_total, inner_trial_records=trial_total,
        inner_accepted_updates=accepted_inner_total, outer_iterations=len(s['searches']),
        outer_trial_records=outer_count, outer_accepted_updates=outer_accepted,
        original_events=len(events), event_kind_counts=dict(kinds),
        original_actual_call_counters=s['original_call_trace']['counts'],
        inner_outcome_counts=dict(inner_failures), original_exception_counts=dict(exception_types),
        checked_array_identities=len(arrays), scalar_leaf_records=len(scalar['leaves']))
    literal = dict(schema='actual93-complete-original-inexact-p3-literal-readout-v1', actual=ACTUAL,
        scope='Only copy original Actions values, schema, bits and record structure; no new scientific arithmetic',
        source_roles=s['source_roles'], consumed_source_sha256=s['consumed_source_sha256'],
        parent_status=s['parent_status'], input_sha256=s['input_sha256'],
        original_status=dict(file=STATUS,bytes=len(status_raw),sha256=sha(status_raw)),
        initial=s['initial'], initial_original_three_equation_merit=s['initial_original_three_equation_merit'],
        initial_projection=projection, outer_searches=outer_rows, inner_reports=inner_literal,
        final_inner_stored_word_equalities=final_inner_word_readout,
        final_repeated_J_words_equal=final_repeated_J_words_equal,
        final=s['final'], final_original_three_equation_merit=s['final_original_three_equation_merit'],
        last_accepted_parameters=s['last_accepted_parameters'], search_stop_reason=s['search_stop_reason'],
        original_complete_circle_check=s['original_complete_circle_check'], complete_scalar_domain=s['complete_scalar_domain'],
        flags={k:v for k,v in s.items() if isinstance(v,bool)}, counts=counts, seconds=s['seconds'],
        original_payload_copies=original_copies)
    literal_receipt = dump(out/'2026-11-15-actual93-literal-readout.json.gz', literal)
    audit = dict(schema='actual93-stdlib-original-byte-and-alias-audit-v1', actual=ACTUAL,
        scope=__doc__, original_artifact=root.name,
        transport_scope='Root supplied complete independently SHA/CRC-checked archive; this audit does not redownload or recheck the ZIP.',
        inventory=inventory, counts=counts, checks=checks, sources=sources,
        restored_public_sources=restored, original_inputs=input_records,
        previous_complete_byte_audit=PREVIOUS_BYTE_AUDIT,declared_proof_receipts=proof_receipts,
        array_identities=arrays, original_payload_copies=original_copies,
        new_scientific_computation=False, all_checks_passed=all(c['passed'] for c in checks))
    audit_receipt = dump(out/'2026-11-15-actual93-byte-audit.json.gz', audit)
    summary = dict(schema='actual93-stdlib-original-byte-audit-summary-v1', actual=ACTUAL,
        all_checks_passed=audit['all_checks_passed'], check_count=len(checks), counts=counts,
        source_sha256=sha(Path(__file__).read_bytes()), byte_audit=audit_receipt,
        literal_readout=literal_receipt, original_payload_copies=original_copies,
        native_solver_called=s['native_nonlinear_solver_called'], scientific_success=s['success'],
        diagnostic_completed=s['diagnostic_completed'], no_local_scientific_recomputation=True,
        limitations=['No SVD/Schur/merit/root/RHS/J/interval calculation was repeated.',
            'Only declared stored sources/values and full current-point aliases were checked.',
            'The same four mathematical input payloads were fully audited in actual92; no second local download or Git operation was made.',
            'The restored78 public-source entries are original Actions receipts matched to the frozen source manifest, not a second payload restoration.',
            'This is provenance and byte evidence, not an extra candidate or BVP gate.'])
    summary_receipt = dump(out/'2026-11-15-actual93-byte-audit-summary.json', summary)
    print(json.dumps(dict(summary=summary_receipt,counts=counts,check_count=len(checks),passed=True),ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
