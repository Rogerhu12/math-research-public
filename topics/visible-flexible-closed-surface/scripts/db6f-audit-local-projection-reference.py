#!/usr/bin/env python3
"""Independent binding/statistics audit of four frozen projection diagnostics.

No root or flow is called. The independently executed 80/120-digit reference
remains numerical evidence, not an interval certificate. The floating-value
comparator is reviewed separately by /root/coupled_prefix.
"""
import argparse
from decimal import Decimal as D, localcontext
import gzip
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
NOTES = ROOT / 'notes'
STEM = '2026-11-09-db6f-'
FROZEN = {
    'scripts/db6f-tail-local-projection-points.mjs': '837a2361bdf17731903fdf31afaadd1c46023db63bcff665feeec0f2f621a377',
    'scripts/db6f-prefix-one-m14-root-packet.mjs': '7b28538a9c92b391cddba341b7ca3469fdc3c006eb491788fd31e8259cd68ca2',
    'scripts/db6f-tail-local-projection-reference.py': '5ab87f037a40579bae5164ef0b50b9e701d58703411177569a91ec94b810249a',
    'scripts/db6f-tail-local-projection-values.mjs': '99aec526e2cc5c7949a2050f18b3f98c02cd8c270821fbb44a09c6f21b889444',
    'notes/'+STEM+'tail-local-projection-points-three.json.gz': 'be48b24e08a8cdd6aec1b6c4c377ab62cb1a10bb989d19c98293bd666c7dbc86',
    'notes/'+STEM+'prefix-m14-q512-stage37-projection-input.json.gz': '62076b6b944cd1665fde25f3d4858322c5019af8b916e8e13ec663004781af4f',
    'notes/'+STEM+'tail-local-projection-values.json.gz': '8146e56b0a1d9f9dcd03d5bc5f81ea955112d2f8f8962ad65d6611f79f8595a3',
    'notes/'+STEM+'tail-local-projection-reference.json.gz': '89886e6ed3b5d68adb07ebe3f82473061ae5a91ff8d44c6aaf537a9f2dc3e601',
    'notes/'+STEM+'tail-local-projection-summary.json': '9f13b792b14e7e486e365cfc13659ad417fff3af75d82eaf9e2ab19d2f2d96a8',
    'notes/'+STEM+'tail-local-projection-comparison.md': 'ef93eb972b9c0fa71279756da7c56344292dec0503e4e87072b222834278a055',
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    b = Path(path).read_bytes()
    return json.loads(gzip.decompress(b) if b[:2] == b'\x1f\x8b' else b)


def note(name):
    return NOTES / (STEM+name)


def check(ok, message):
    if not ok:
        raise ValueError(message)


def without(data, keys):
    return {k:v for k,v in data.items() if k not in keys}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    check(not args.out.exists(), 'Refusing to replace output')
    for name, digest in FROZEN.items():
        check(sha(ROOT/name) == digest, 'Frozen input changed: '+name)
    three = read(note('tail-local-projection-points-three.json.gz'))
    m14 = read(note('prefix-m14-q512-stage37-projection-input.json.gz'))
    values = read(note('tail-local-projection-values.json.gz'))
    author = read(note('tail-local-projection-reference.json.gz'))
    summary = read(note('tail-local-projection-summary.json'))
    replay_path = note('audit-local-projection-reference-observed.json.gz')
    replay_summary_path = note('audit-local-projection-reference-observed-summary.json')
    replay, replay_summary = read(replay_path), read(replay_summary_path)
    execution_path = note('audit-local-projection-reference-observed-execution.json')
    execution = read(execution_path)
    check(execution['exit_code'] == 0 and execution['new_original_root_calls'] == 0, 'Reference execution failed')
    expected_values = note('tail-local-projection-values.json.gz')
    for data in (author,replay,summary,replay_summary):
        check(data['input_sha256'] == sha(expected_values) and Path(data['input']).name == expected_values.name,
              'Reference input spelling does not name the same frozen values')
    check(without(author, {'input','seconds'}) == without(replay, {'input','seconds'}), 'Reference mathematical fields differ')
    check(without(summary, {'input','seconds','full_report','full_report_sha256'}) ==
          without(replay_summary, {'input','seconds','full_report','full_report_sha256'}), 'Summary mathematical fields differ')
    for data, path in [(summary, note('tail-local-projection-reference.json.gz')),
                       (replay_summary, replay_path)]:
        check(data['full_report_sha256'] == sha(path), 'Full-reference hash mismatch')
        check(Path(data['full_report']).name == path.name, 'Wrong full-reference path')
    bound_paths = set()
    for item in three['inputSHA256'].values():
        check(sha(item['file']) == item['sha256'], 'Three-point input hash differs')
        bound_paths.add(item['file'])
    for path, digest in three['sourceSHA256'].items():
        check(sha(path) == digest, 'Three-point source hash differs')
        bound_paths.add(path)
    for item in m14['sourceBindings']:
        check(sha(item['path']) == item['sha256'] and Path(item['path']).stat().st_size == item['bytes'],
              'M14 source/input binding differs')
        bound_paths.add(item['path'])
    inputs = {k: read(v['file']) for k,v in three['inputSHA256'].items()}
    diag, stage, control, previous = [inputs[k] for k in
                                    ('diagnostic','stage-input','control-checkpoint','control-report')]
    failure_cases = [(i,c) for i,c in enumerate(diag['cases'])
                     if c['inputSHA256'] == three['inputSHA256']['stage-input']['sha256']]
    check(len(failure_cases) == 1 and failure_cases[0][0] == 4, 'Closed failure pointer differs')
    failure = failure_cases[0][1]['firstFailure']
    check(stage['stage'] == 35 and stage['rawCell'] == 0 and stage['rawSegment'] == 4 and
          stage['trial']['step'] == .0625 and stage['parameters']['projectionFloor'] == .05, 'Wrong failed point')
    check(failure['sourceX'] == 0 and failure['substage'] == 0 and failure['ordinaryStep'] == 0,
          'Wrong first failing evaluation')
    first, last, success = three['points']
    for item in (first,last):
        check(item['state'] == failure['state'] == stage['inputState']+[0,0], 'Failed state not copied exactly')
        check(item['Q'] == item['state'][:15] and item['target'] == failure['target'], 'Failed Q/target differs')
        for key in ('r','logw','w','w2','E','drdx','dlogwdx'):
            check(item['geometry'][key] == failure['geometry'][key], 'Failed geometry differs')
        check(item['rootDiagnostic'] is None, 'Nonroot point relabelled as root')
    check(first['L'] == failure['target'] and last['L'] == failure['rootTrace']['lastL'], 'Saved L not copied exactly')
    cp = control.get('checkpoint', control.get('response', {}).get('checkpoint', control))
    check(success['state'] == cp['states'][36]+[0,0] and success['Q'] == cp['states'][36][:15],
          'M15 control state differs')
    for key in ('minA','minD','minS','residual','scale'):
        check(success['sourceEvaluation'][key] == previous['controlResult']['root'][key],
              'Old independently reviewed successful-control scalar differs: '+key)
    m14_cp = read(m14['origin']['checkpoint'])
    check(m14_cp['response']['converged'] is True, 'M14 checkpoint not converged')
    check(m14['state'] == m14_cp['response']['checkpoint']['states'][38]+[0,0], 'M14 state differs')
    check(m14['Q'] == m14['state'][:14] and m14['location']['stage'] == 37 and
          m14['location']['rawX'] == .25 and m14['options']['projectionFloor'] == .05, 'Wrong M14 point')
    check(m14['root']['iterations'] == 5 and not m14['root']['roundoffFallback'], 'M14 root record differs')
    check(three['originalRootCalls'] == m14['singleOriginalRootCalls'] == 1 and
          m14['flowCalls'] == m14['wholeDNEvaluations'] == values['originalRootCalls'] ==
          author['original_root_calls_in_this_script'] == 0, 'Wrong scope/count')
    for packet in values['inputPackets']:
        check(sha(packet['file']) == packet['sha256'], 'Comparator input packet changed')
    check(author['input_sha256'] == sha(note('tail-local-projection-values.json.gz')) and
          author['precisions'] == [80,120] and not author['new_engine_implemented'] and
          not author['global_solver_run'], 'Reference is not the fixed four-point diagnostic')
    check(len(values['values']) == len(author['cases']) == len(summary['cases']) == 4, 'Wrong number of points')
    records = []
    with localcontext() as context:
        context.prec = 130
        for index,(case, full, brief) in enumerate(zip(values['values'], author['cases'], summary['cases'])):
            check(case['id'] == full['id'] == brief['id'], 'Case order differs')
            pnt = case['point']
            if index < 3:
                check(without(pnt, {'inputPacket'}) == three['points'][index], 'Comparator changed one of first three points')
            else:
                for key in ('state','Q','L','geometry','target','options'):
                    check(pnt[key] == m14[key], 'Comparator changed M14 '+key)
                basis = values['bases'][case['basisKey']]
                for key in ('cs','sn'):
                    check(basis[key] == m14['originalRoundedBasis'][key], 'M14 binary table differs')
                for key in ('p','pt','L','U'):
                    check(case['frozenCoefficients'][key] == m14[key], 'M14 frozen coefficient differs')
            check(case['frozenCoefficients']['L'] == pnt['L'], 'Changed fixed L')
            check(case['originalRowReconstructionPassed'] and case['originalOutputReconstructionPassed'],
                  'Comparator did not reconstruct original values')
            for key in ('moments','quad','B'):
                check(case['original'][key] == pnt['sourceEvaluation'][key], 'Original source output differs')
            for model in ('rounded-table','ideal-grid'):
                minimum = full['high_precision_references'][model]['minimum']
                check(min(D(z) for z in minimum.values()) > D.from_float(.05), 'High precision branch guard fails')
            residuals = {}
            for method in ('original','algebraSameTable','analyticLowProjection'):
                residuals[method] = max(abs(D.from_float(a)-D.from_float(b))
                                        for a,b in zip(case[method]['moments'], pnt['target']))
            moment_change = max(abs(D.from_float(a)-D.from_float(b)) for a,b in
                                zip(case['analyticLowProjection']['moments'], case['original']['moments']))
            relative_change = moment_change / D.from_float(case['originalScale'])
            check(relative_change == D(brief['maximum_new_moment_change_over_original_scale']),
                  'Reported relative change differs')
            errors = brief['ideal_grid_max_errors']
            for key in ('quad','B','nonlinearFlux'):
                check(D(errors['analyticLowProjection'][key]) < D(errors['original'][key]),
                      'Claimed four-point maximum error improvement is absent')
            records.append(dict(id=case['id'],relative_moment_change=str(relative_change),
                                fixed_L_maximum_residual={k:str(v) for k,v in residuals.items()},
                                maximum_reference_precision_difference=brief['maximum_reference_precision_difference']))
        max_change = max(D(c['relative_moment_change']) for c in records)
        max_stability = max(D(c['maximum_reference_precision_difference']) for c in records)
        check(max_change < D('4.77e-16') and max_stability < D('1.19e-78'), 'Rounded display claim is false')
        check(D(records[1]['fixed_L_maximum_residual']['analyticLowProjection']) > D('.022'), 'Failure residual disappeared')
        for index in (2,3):
            check(D(records[index]['fixed_L_maximum_residual']['analyticLowProjection']) <
                  D('8e-14') * D.from_float(values['values'][index]['originalScale']), 'Successful control exceeds original stop gate')
    report = dict(status='PASS-independent-extraction-reference-and-finite-statistics-review',
                  script_sha256=sha(__file__),frozen_inputs=FROZEN,checked_binding_files=len(bound_paths),
                  new_root_calls=0,new_flow_calls=0,reference_replay_exit_code=execution['exit_code'],
                  reference_replay_sha256=sha(replay_path),summary_replay_sha256=sha(replay_summary_path),
                  execution_sha256=sha(execution_path),
                  mathematical_reference_fields_identical=True,mathematical_summary_fields_identical=True,
                  ignored_reference_fields=['input','seconds'],ignored_summary_fields=['input','seconds','full_report','full_report_sha256'],
                  original_extractor_root_calls=2,maximum_relative_moment_change=str(max_change),
                  maximum_reference_precision_difference=str(max_stability),cases=records,
                  scope='Four frozen points only. Decimal 80/120 agreement is not an interval certificate. '
                        'Original extracted roots were not rerun. Floating-value comparator is separately reviewed by coupled_prefix. '
                        'No new solver, global conclusion, or G5 assertion.')
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('status','checked_binding_files','new_root_calls',
                                          'reference_replay_exit_code','maximum_relative_moment_change')}))


if __name__ == '__main__':
    main()
