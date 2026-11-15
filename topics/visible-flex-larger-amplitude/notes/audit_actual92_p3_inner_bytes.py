#!/usr/bin/env python3
"""Actual92 read-only JSON/byte audit, with no scientific recomputation.

Only transport, SHA256, exact decoded-JSON comparisons, binary64 serialization,
integer record/word counts and read-only Git blob access are used.  No numerical
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
import os
from pathlib import Path
import struct
import subprocess


ACTUAL = dict(run_id=43672921972,
    source_commit='1755a4f414a77d41d85eae9a0e1625f55a74be90',
    job_id=132686715503, artifact_id=14144239294,
    artifact_name='visible-mainline-smallcoreresonance-43672921972-1',
    artifact_zip_bytes=676336,
    artifact_zip_sha256='f10832bad2ebf3b48a4da501bc0a50b7556e7a839eb86ddd532cab497338d74a',
    job_conclusion='success')
TOPIC = 'topics/visible-flex-larger-amplitude/'
COMP = TOPIC+'computations/'
ENTRY = 'geometry_20261115_small_core_p3_inner_root_search.py'
ENTRY_SHA = '3b48efd71eb696fef66acbe7fbd163bb8dc8ca63287bfa8c4e873a2600fbf9d9'
STATUS = 'small-core-p3-inner-root/p3-inner-root-status.json'
PINNED = {
    STATUS: (498765, 'e822be884ac07e2b2c46ac7aba7f589ba5233e86cdbb33ad9c95108cc8dca01e'),
    'request92-input-and-source-identity.json': (37214, '4db8a276775b48da10f080f730e85690d0cd8a06eec59093da3cc4c265db1d9b'),
    'exact-diagnostic-command.json': (3447, '18d691b80b43752d7147d785e0c66b8f8d70ac2af95e8de61f37b9877ce7e460'),
    'public-source-preparation.json': (20424, '08eec62768177b89d8e7770318419c087d4006259360a89910d5d25346e1d0d2'),
    'small-core-resonance-readback.json': (78926, 'd0a5a3388bfb451dc74e322fbff5fa88118033c9bc699cc77a23a0fa88cb4183'),
    'prior-candidate/actual90-damped-resume-status.json': (60951, '5a4d157aa0bcada3cdd1d319adb419f23b94f52bfc1c945a3c6afe1207cb2f5a'),
    'small-core-p3-inner-root/parent-status.json': (60951, '5a4d157aa0bcada3cdd1d319adb419f23b94f52bfc1c945a3c6afe1207cb2f5a'),
    'small-core-p3-inner-root/circle-reference.json.gz': (140758, 'cfdc0e76d8c8bc47ba15ba0eb931c3ba75152af6c72799d4d3282d865b2c1359'),
    'small-core-p3-inner-root/complete-scalar-domain.json.gz': (143544, 'a6ace28f4bf341651790e700dedbc1d62d9db5cb953fc5357353c5ccd4bd7b17'),
    'small-core-p3-inner-root/large-arrays/original-model-evaluations.jsonl': (2039245, 'e1b087a4c9581c46226292a9bede43af1e93466457e6477a19222516f94bd0f1'),
}


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
    args = parser.parse_args()
    root, out = args.artifact_directory.resolve(), args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    checks, sources, arrays, git_cache = [], [], [], {}

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

    def git_raw(path):
        if path not in git_cache:
            (out/'audit-read-progress.json').write_text(json.dumps(
                dict(requested_public_blob=path, operation='read-only Git show; lazy fetch disabled'))+'\n')
            git_cache[path] = subprocess.run(
                ['git', 'show', ACTUAL['source_commit']+':'+path],
                cwd=args.repository, check=True, stdout=subprocess.PIPE,
                stderr=subprocess.PIPE, timeout=15,
                env={**os.environ, 'GIT_NO_LAZY_FETCH':'1'}).stdout
        return git_cache[path]

    def git_checked(path, expected, label):
        local = args.repository/path
        if path not in git_cache and local.is_file():
            candidate = local.read_bytes()
            if sha(candidate) == expected['sha256']:
                git_cache[path] = candidate
        raw = git_raw(path)
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
    base = 'small-core-p3-inner-root/'
    identity = load('request92-input-and-source-identity.json')
    request = identity['request']
    prep = load('public-source-preparation.json')
    command = load('exact-diagnostic-command.json')
    readback = load('small-core-resonance-readback.json')
    parent = load('prior-candidate/actual90-damped-resume-status.json')
    circle = load(base+'circle-reference.json.gz')
    scalar = load(base+'complete-scalar-domain.json.gz')
    same('identity source commit', identity['source_commit'], ACTUAL['source_commit'])
    same('scientific producer SHA', s['source_sha256'], ENTRY_SHA)
    same('request number', request['request_number'], 92)
    reqraw = git_checked(COMP+'public-small-core-resonance-request.json',
                         dict(sha256=identity['request_sha256']), 'original request Git bytes')
    same('request full JSON', request, json.loads(reqraw))
    check('71 requested sources', len(identity['verified_sources']) == 71 and
          len(request['source_sha256']) == 71)
    for r in identity['verified_sources']:
        same('request source pin '+r['file'], r['sha256'], request['source_sha256'][r['file']])
        path = COMP+r['file']
        raw = git_checked(path, r, 'actual source bytes '+r['file'])
        sources.append(dict(file=path, bytes=len(raw), sha256=sha(raw),
                            consumed_by_new_producer=r['file'] in s['consumed_source_sha256']))
    check('12 consumed source identities', len(s['consumed_source_sha256']) == 12)
    for name, digest in s['consumed_source_sha256'].items():
        same('consumed source '+name, digest, request['source_sha256'][name])
    source_tree = ast.parse(git_raw(COMP+ENTRY).decode())
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
                                     'RESUME_NAME','ORIGINAL_NAME','ORIGINAL_SHA256'):
                constants[node.targets[0].id] = source_literal(node.value)
    same('actual producer source schema', s['schema'], constants['SCHEMA'])
    same('actual producer source basename', ENTRY, constants['ENTRY_NAME'])
    same('producer full input pins', s['input_sha256'], constants['ORIGINAL_INPUTS'])
    same('producer consumed source closure', s['consumed_source_sha256'],
         {**constants['FROZEN'], ENTRY:ENTRY_SHA})
    for r in request['proofs']:
        git_checked(r['file'], r, 'declared proof/interface '+r['file'])
    same('public78 source commit', prep['actual_public_commit'], ACTUAL['source_commit'])
    same('public78 file count', len(prep['restored_files']), prep['verified_file_count'])
    same('public78 declared count', prep['verified_file_count'], 78)
    dependency_manifest = json.loads(git_raw(COMP+'source-dependencies.json'))
    same('public78 source manifest identity', sha(git_raw(COMP+'source-dependencies.json')),
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
        try:
            raw = git_checked(r['file'], r, 'full mathematical input bytes '+r['name'])
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
            input_records.append(dict(**r, verified_entire_public_file=False,
                scope='Full original Actions descriptor/producer/request SHA comparison only; local partial clone has no blob and network fetch is prohibited here'))
        else:
            input_records.append(dict(**r, verified_entire_public_file=True))
            input_objects[r['name']] = json.loads(gzip.decompress(raw) if raw.startswith(b'\x1f\x8b') else raw)
    prior = identity['verified_prior_candidate']['original_status']
    raw = git_checked(prior['file'], prior, 'complete actual90 parent public bytes')
    same('both preserved actual90 original copies', read('prior-candidate/actual90-damped-resume-status.json'),
         read(base+'parent-status.json'))
    check('parent copy is original public file', raw == read(base+'parent-status.json'))
    same('parent only literal final parameters', s['parent_status']['literal_parameters'], parent['final']['parameters'])
    same('current fresh initial parameters', s['initial']['parameters'], parent['final']['parameters'])
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
        same('literal readback field '+k, readback[k], s[k])
    for k, v in readback['initial_projection_summary'].items():
        check('readback initial projection '+k, literal_subset(v, s['initial_projection'][k]))
    for i, item in enumerate(readback['outer_search_summary']):
        for k, v in item.items():
            if k != 'trials':
                same('readback outer '+str(i)+'/'+k, v, s['searches'][i][k])
            else:
                for j, t in enumerate(v):
                    for a, b in t.items():
                        check('readback outer trial '+str(i)+'/'+str(j)+'/'+a,
                              literal_subset(b, s['searches'][i]['trials'][j][a]))

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
    same('all evaluation event counters', dict(eval_counts), s['original_call_trace']['counts'])
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
        for k in ('label','inner_call','usable_inner_root','residual_tolerance_met',
                  'original_full_J_finite','original_J33_finite_nonzero','stop_reason','seconds','original_call_cost'):
            same('inner summary '+str(number)+'/'+k, receipt[k], report[k])
        same('inner final summary '+str(number), receipt['last_probe'], report.get('last_probe'))
        check('inner never outer acceptance '+str(number), report['accepted_outer_state'] is False)
        same('inner first two fixed '+str(number), report['fixed_first_two_parameters'], report['seed_parameters'][:2])
        if number == 1:
            check('initial seed is newly evaluated current state', report['seed_is_reused_fresh_state'] is True)
            match_state('initial projection seed current bytes', report['initial'], fresh)
        else:
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
            usable_inner_root=report['usable_inner_root'], stop_reason=report['stop_reason'],
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
    same('projection inner receipt', projection['inner'], s['inner_reports'][0])
    match_state('projection actual new point', projection['actual_projected_point'], inner[1]['last_probe'])
    same('projection fresh J not parent J', projection['original_full_J'], initialJ['original_full_three_by_three_jacobian'])
    match_state('projection original point', projection['original_parent_point'], fresh)
    current = projection['actual_projected_point'] if projection['adopted_as_outer_baseline'] else fresh
    currentJ = inner[1]['steps'][-1]['original_full_three_by_three_jacobian'] if projection['adopted_as_outer_baseline'] else initialJ['original_full_three_by_three_jacobian']
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
            if report['usable_inner_root']:
                match_state('outer actual candidate '+str(number), trial['actual_projected_point'], report['last_probe'])
                same('outer candidate actual full merit '+str(number), trial['actual_merit'], report['last_probe']['original_three_equation_merit'])
                same('outer nonzero d3 literal '+str(number), trial['true_third_unit_residual_preserved'], report['last_probe']['low_equations_used'][2])
            else:
                check('unusable inner not promoted '+str(number),
                      trial['accepted'] is False and 'actual_projected_point' not in trial and 'actual_merit' not in trial)
            if trial['accepted']:
                accepted.append(trial)
                current = trial['actual_projected_point']
                currentJ = report['steps'][-1]['original_full_three_by_three_jacobian']
                outer_accepted += 1
            tr.append(dict(outer_iteration=index, trial=ti, alpha=trial['alpha'], inner_call=number,
                usable_inner_root=report['usable_inner_root'], outer_accepted=trial['accepted'],
                reason=trial['reason'], original_Armijo_bound=trial['original_Armijo_bound'],
                actual_merit=trial.get('actual_merit'), predicted_seed_parameters=trial['predicted_seed_parameters'],
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
    same('final description J also matches accepted-root full J', finalJ['original_full_three_by_three_jacobian'], currentJ)

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
    check('all original 957 leaf success flags preserved', all(
        leaf['strict_positive_radius_and_abs_ap_lt_one'] is True and
        leaf['definite_scalar_domain_failure'] is False for leaf in scalar['leaves']))
    same('scalar first endpoint literal', scalar['leaves'][0]['interval'][0], scalar['covered_interval'][0])
    same('scalar last endpoint literal', scalar['leaves'][-1]['interval'][1], scalar['covered_interval'][1])
    check('scalar exact endpoint text adjacency', all(
        scalar['leaves'][j]['interval'][1] == scalar['leaves'][j+1]['interval'][0]
        for j in range(len(scalar['leaves'])-1)))

    original_copies = []
    for name, raw in [
        ('2026-11-15-actual92-original-complete-status.json.gz', status_raw),
        ('2026-11-15-actual92-original-evaluation-ledger.jsonl.gz', ledger_raw)]:
        compressed = gzip.compress(raw, mtime=0)
        (out/name).write_bytes(compressed)
        check('lossless original copy '+name, gzip.decompress(compressed)==raw)
        original_copies.append(dict(file=name,bytes=len(compressed),sha256=sha(compressed),
                                    decoded_bytes=len(raw),decoded_sha256=sha(raw)))
    inner_name = '2026-11-15-actual92-original-inner-reports.json.gz'
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
        complete_mathematical_input_payloads_locally_verified=sum(r['verified_entire_public_file'] for r in input_records),
        original_inner_reports=len(inner),
        inner_original_J_records=step_total, inner_trial_records=trial_total,
        inner_accepted_updates=accepted_inner_total, outer_iterations=len(s['searches']),
        outer_trial_records=outer_count, outer_accepted_updates=outer_accepted,
        original_events=len(events), event_kind_counts=dict(kinds),
        original_actual_call_counters=s['original_call_trace']['counts'],
        inner_outcome_counts=dict(inner_failures), original_exception_counts=dict(exception_types),
        checked_array_identities=len(arrays), scalar_leaf_records=len(scalar['leaves']))
    literal = dict(schema='actual92-complete-original-p3-inner-literal-readout-v1', actual=ACTUAL,
        scope='Only copy original Actions values, schema, bits and record structure; no new scientific arithmetic',
        source_roles=s['source_roles'], consumed_source_sha256=s['consumed_source_sha256'],
        parent_status=s['parent_status'], input_sha256=s['input_sha256'],
        original_status=dict(file=STATUS,bytes=len(status_raw),sha256=sha(status_raw)),
        initial=s['initial'], initial_original_three_equation_merit=s['initial_original_three_equation_merit'],
        initial_projection=projection, outer_searches=outer_rows, inner_reports=inner_literal,
        final_inner_stored_word_equalities=final_inner_word_readout,
        final=s['final'], final_original_three_equation_merit=s['final_original_three_equation_merit'],
        last_accepted_parameters=s['last_accepted_parameters'], search_stop_reason=s['search_stop_reason'],
        original_complete_circle_check=s['original_complete_circle_check'], complete_scalar_domain=s['complete_scalar_domain'],
        flags={k:v for k,v in s.items() if isinstance(v,bool)}, counts=counts, seconds=s['seconds'],
        original_payload_copies=original_copies)
    literal_receipt = dump(out/'2026-11-15-actual92-literal-readout.json.gz', literal)
    audit = dict(schema='actual92-stdlib-original-byte-and-alias-audit-v1', actual=ACTUAL,
        scope=__doc__, original_artifact=root.name,
        transport_scope='Root supplied complete independently SHA/CRC-checked archive; this audit does not redownload or recheck the ZIP.',
        inventory=inventory, counts=counts, checks=checks, sources=sources,
        restored_public_sources=restored, original_inputs=input_records,
        array_identities=arrays, original_payload_copies=original_copies,
        new_scientific_computation=False, all_checks_passed=all(c['passed'] for c in checks))
    audit_receipt = dump(out/'2026-11-15-actual92-byte-audit.json.gz', audit)
    summary = dict(schema='actual92-stdlib-original-byte-audit-summary-v1', actual=ACTUAL,
        all_checks_passed=audit['all_checks_passed'], check_count=len(checks), counts=counts,
        source_sha256=sha(Path(__file__).read_bytes()), byte_audit=audit_receipt,
        literal_readout=literal_receipt, original_payload_copies=original_copies,
        native_solver_called=s['native_nonlinear_solver_called'], scientific_success=s['success'],
        diagnostic_completed=s['diagnostic_completed'], no_local_scientific_recomputation=True,
        limitations=['No SVD/Schur/merit/root/RHS/J/interval calculation was repeated.',
            'Only declared stored sources/values and full current-point aliases were checked.',
            'This is provenance and byte evidence, not an extra candidate or BVP gate.'])
    summary_receipt = dump(out/'2026-11-15-actual92-byte-audit-summary.json', summary)
    print(json.dumps(dict(summary=summary_receipt,counts=counts,check_count=len(checks),passed=True),ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
