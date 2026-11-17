#!/usr/bin/env python3
"""Write compact provenance for the three candidate-only runs; no equation replay."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def file_record(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--work', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    versions = [('v1', '', 'propose_tail_internal_candidate.mjs', 62324, '73e06a'),
                ('v2', '-v2', 'propose_tail_internal_candidate_v2.mjs', 80768, '4a6316'),
                ('v3', '-v3', 'propose_tail_internal_candidate_v3.mjs', 50321, '411bd3')]
    runs, original_source = [], {}
    prior = None
    for version, suffix, name, session, chunk in versions:
        file = args.work/f'q060-call3-internal-candidate{suffix}-summary.json'
        summary = json.loads(file.read_text())
        source = root/name
        if summary['source_sha256'][str(source)] != sha(source):
            raise AssertionError('Executed candidate source changed')
        input_path, output_path = Path(summary['input']['path']), Path(summary['candidate']['path'])
        if sha(input_path) != summary['input']['sha256'] or sha(output_path) != summary['candidate']['sha256']:
            raise AssertionError('A candidate input or output changed')
        candidate = json.loads(gzip.decompress(output_path.read_bytes()))
        original = json.loads(gzip.decompress(input_path.read_bytes()))
        if prior is not None and prior != summary['input']:
            raise AssertionError('The versions did not use the same original failure')
        prior = summary['input']
        if (summary['original_solver_invoked'] is not False or
                candidate['solver_success'] is not False or candidate['candidate_only'] is not True):
            raise AssertionError('A candidate record was mislabeled as an accepted solution')
        if candidate['checkpoint']['states'] != original['response']['checkpoint']['states']:
            raise AssertionError('This compact report describes only the observed unchanged-state failures')
        count = sum(p['local_trial_count'] for p in summary['passes'])
        trials = [trial for p in summary['passes'] for trial in p['trials'] if 'norm' in trial]
        best = min(trials, key=lambda p: p['norm'])
        runs.append(dict(version=version, execution=dict(session=session, terminal_chunk=chunk,
                exit_code=0, seconds=summary['seconds']), source=file_record(source),
            command=summary['command'], summary=file_record(file), candidate=summary['candidate'],
            alphas=summary['alphas'], betas=summary['betas'], max_passes=summary['maxPasses'],
            maximum_trials_per_pass=len(summary['alphas'])*(1+len(summary['betas'])),
            actual_passes=len(summary['passes']), actual_trials=count,
            selected_passes=sum(p['selected'] is not None for p in summary['passes']),
            before=summary['before'], final_full_replay=summary['full_candidate_replay'],
            best_tried_nonaccepted=dict(alpha=best['alpha'], beta=best['beta'], norm=best['norm']),
            complete_internal_states_unchanged=True,
            strict_full_replay_improvement=summary['strict_full_replay_improvement'],
            original_solver_invoked=False, solver_success=False, stopped=summary['stopped']))
        original_source.update({k:v for k,v in summary['source_sha256'].items()
                                if 'propose_tail_internal_candidate' not in k})
    v1, v2, v3 = [(root/row[2]).read_text() for row in versions]
    if v2.replace('const alphas=[1/128,1/64,1/32,1/16,1/8,1/4,5/16,1/3,3/8,1/2,3/4,1];',
                  'const alphas=[1/8,1/4,5/16,1/3,3/8,1/2,3/4,1];') != v1:
        raise AssertionError('v2 contains a change beyond the declared alpha list')
    if v3.replace('if(downstream.norm>=currentNorm||upstream.norm<=cfg.solveTolerance||upstream.component<0)continue;',
                  'if(downstream.norm>cfg.solveTolerance||upstream.norm<=cfg.solveTolerance||upstream.component<0)continue;') != v2:
        raise AssertionError('v3 contains a change beyond the declared beta-eligibility condition')
    prep_file = args.work/'q060-recovery-v3-source-manifest.json'
    prep = json.loads(prep_file.read_text())
    reload_file = args.work/'q060-call3-v3-reload-arithmetic-check.json'
    reload_record = json.loads(reload_file.read_text())
    if reload_record['adapter_sha256'] != sha(root/'recovering_tail_client.py'):
        raise AssertionError('Reload arithmetic used a different adapter source')
    if reload_record['candidate'] != runs[-1]['candidate']:
        raise AssertionError('Reload arithmetic used a different v3 candidate')
    for key in ('original_source_sha256', 'original_runtime_source_sha256',
                'preparation_source_sha256', 'owned_source_sha256'):
        for path, digest in prep[key].items():
            if sha(path) != digest:
                raise AssertionError('Prepared source identity changed: '+path)
    record = dict(scope='Finite initial-candidate failures and a prepared original-worker recovery interface; no new DN acceptance or coupled prefix.',
        input=prior, locator=json.loads((args.work/'q060-call3-internal-candidate-summary.json').read_text())['locator'],
        original_source_sha256=original_source, runs=runs,
        source_differences=dict(v2='Only the declared four smaller alpha entries.',
                               v3='Only beta branch eligibility: downstream.norm >= currentNorm.'),
        owned_preparation=file_record(prep_file),
        original_worker_reload_arithmetic=dict(record=file_record(reload_file),
            result=reload_record['result']),
        prepared_source_sha256=prep['preparation_source_sha256'],
        prepared_owned_source_sha256=prep['owned_source_sha256'],
        runtime_source_sha256=prep['original_runtime_source_sha256'],
        preparation_verification=dict(reverse_coupler_patch_restores_original_bytes=True,
            original_sources_unchanged=True, source_root_identity=True,
            actual_solver_invoked=False, production_wrapper_executed=False),
        recorder_source=file_record(__file__),
        limitations=['The live recovery branch has no successful native-worker end-to-end execution yet.',
            'The former call3 run has no raw inner prefix; these files cannot recreate its lost cubic state.',
            'The next owned run saves a raw inner cubic and its exact accepted actual-DN affine anchor before requesting the new height.',
            'Unsuccessful local candidates do not prove that the finite DN problem has no solution.'])
    with args.output.open('x') as stream:
        json.dump(record, stream, indent=2, allow_nan=False)
        stream.write('\n')
    print(json.dumps(dict(output=str(args.output), sha256=sha(args.output),
                         actual_trials=[run['actual_trials'] for run in runs], solver_invoked=False)))


if __name__ == '__main__':
    main()
