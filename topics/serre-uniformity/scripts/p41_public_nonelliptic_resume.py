#!/usr/bin/env python3
"""Resume preserved nonelliptic outputs with the original R379 clearing input."""
import argparse
import datetime as dt
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import tarfile
import time

from p41_public_actions_recovery import REPO, S, TOPIC, publish, read, save, sha
from p41_ci_recover_ramified_ss47 import preserve

REQUEST = TOPIC / 'notes/public-p41-nonelliptic-resume-request.json'
D = S / 'data'


def prepare(item, base, request_path=REQUEST):
    prior, work, out = base / 'prior', base / 'work', base / 'output'
    prior.mkdir(parents=True, exist_ok=True)
    out.mkdir(parents=True, exist_ok=True)
    subprocess.run(['gh', 'run', 'download', str(item['prior_run']),
        '--repo', 'Rogerhu12/math-research-public', '--name', item['artifact'],
        '--dir', str(prior)], check=True)
    receipt = read(prior / 'run-receipt.json')
    initial = read(prior / 'public-actions-input.json')
    assert receipt['result'] == item['result'] and receipt['disk_id'] == item['disk_id']
    assert receipt['source_commit'] == initial['source_commit'] == item['prior_source']
    assert not receipt['complete'], 'Consume a completed result instead of repeating it.'
    for direction in ['f2', 'f3']:
        rows = receipt[direction.upper() + '_files']
        for row in rows:
            assert sha(prior / direction / row['file']) == row['sha256']
        if (prior / direction).exists():
            shutil.copytree(prior / direction, work / direction, dirs_exist_ok=True)
    f2 = work / 'f2'
    archive = f2 / ('p41_' + item['disk_id'] + '_principal_transports47.tar.gz')
    with tarfile.open(archive, 'r:gz') as tf:
        for member in tf.getmembers():
            path = Path(member.name)
            assert member.isfile() and not path.is_absolute() and '..' not in path.parts
            assert path.parts[0] == 'SS-principal-transports'
            target = f2 / path
            target.parent.mkdir(parents=True, exist_ok=True)
            data = tf.extractfile(member).read()
            if target.exists():
                assert target.read_bytes() == data
            else:
                target.write_bytes(data)
    disk = item['disk_id']
    state = read(f2 / 'chain' / (disk + '_multiply47.json.gz'))
    assert state['bits_done'] == state['target_bits'] == 304
    if item['kind'] == 'ramified':
        derivative = D / 'p41_serre_clearing_126_disks47.json.gz'
        clearing = read(derivative)
        assert clearing['result'] == 'R435' and clearing['all126_requested_rational_disks_unit']
    else:
        derivative = D / 'p41_serre_clearing_nonelliptic_disks47.json.gz'
        clearing = read(derivative)
        assert clearing['result'] == 'R379' and clearing['all_nonelliptic_rational_disks_unit']
        assert disk in {x['disk_id'] for x in clearing['actual_nonelliptic_disk_values']}
    source = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=REPO, text=True).strip()
    save(out / 'public-actions-input.json', {
        'result': item['result'], 'disk_id': disk, 'request_item': item,
        'source_commit': source, 'request_sha256': sha(request_path),
        'prior_receipt_sha256': sha(prior / 'run-receipt.json'),
        'prior_input_sha256': sha(prior / 'public-actions-input.json'),
        'original_chain_bits_restored': 304, 'clearing_result': clearing['result'],
        'clearing_sha256': sha(derivative),
        'root_readme_sha256': sha(REPO / 'README.md'),
        'topic_readme_sha256': sha(TOPIC / 'README.md'),
        'mathematical_assertions_relaxed': False,
    })


def run(item, base, budget):
    work, out = base / 'work', base / 'output'
    f2, f3 = work / 'f2', work / 'f3'
    disk, result = item['disk_id'], item['result']
    derivative = D / 'p41_serre_clearing_nonelliptic_disks47.json.gz'
    canonical = D / 'p41_canonical_SS_robust47_raw.json.gz'
    certificate = D / 'p41_canonical_SS_robust47_certificate.json.gz'
    deadline = time.monotonic() + 60 * budget
    stages, status, error = [], 1, None

    def execute(stage, command):
        left = deadline - time.monotonic()
        if left <= 0:
            raise TimeoutError('Internal budget exhausted before ' + stage)
        with (out / (stage + '.log')).open('w') as log:
            process = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT,
                                       start_new_session=True)
            try:
                code = process.wait(timeout=left)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()
                raise TimeoutError('Internal budget exhausted during ' + stage)
        stages.append({'stage': stage, 'command': command, 'exit_code': code})
        if code:
            raise subprocess.CalledProcessError(code, command)

    try:
        if item['kind'] == 'moved_j9':
            execute('resume_original_moved_stages', [sys.executable, '-u',
                str(S / 'p41_recover_R470_moved_j9_ss47.py'), '--script-dir', str(S),
                '--work-dir', str(f2), '--output', str(out), '--disk-id', disk,
                '--result-id', result, '--budget-minutes', str(budget)])
            f3 = f2 / 'f3'
        else:
            based = f2 / (result + '_' + disk + '_based_points47.json.gz')
            assert based.is_file()
            execute('resume_original_shifted_F2', [sys.executable, '-u',
                str(S / 'p41_rebuild_shifted_SS_F2_clearing_frame47.py'),
                '--script-dir', str(S), '--work-dir', str(f2), '--disk-id', disk,
                '--result-id', result, '--canonical', str(canonical),
                '--canonical-certificate', str(certificate), '--derivative', str(derivative),
                '--based-points', str(based), '--rebuild-chain', '--resume-stages'])
            poly = read(f2 / (disk + '_actual_canonical_F2_polynomial47.json.gz'))
            if poly['residual_QC_roots']:
                execute('actual_same_component_F3', [sys.executable, '-u',
                    str(S / 'p41_run_shifted_SS_F3_derivative47.py'),
                    '--script-dir', str(S), '--source-dir', str(S), '--f2-dir', str(f2),
                    '--chain-dir', str(f2 / 'chain'), '--transport-directory',
                    str(f2 / 'SS-principal-transports' / disk),
                    '--recovery-dir', str(f2 / 'recovery-inputs'), '--based-points', str(based),
                    '--canonical', str(canonical), '--derivative', str(derivative),
                    '--f2-polynomial', str(f2 / (disk + '_actual_canonical_F2_polynomial47.json.gz')),
                    '--f2-audit', str(f2 / (disk + '-principal-F2-independent-audit.json')),
                    '--support-source', str(S / 'p41_selected_shifted_SS_T3_support47.py'),
                    '--poly-source', str(S / 'p41_selected_SS_F3_local_polynomial_all_unit_fractions_derivative47.py'),
                    '--audit-source', str(S / 'verify_selected_SS_F3_all_unit_fractions_derivative47.py'),
                    '--work-dir', str(f3), '--output-dir', str(f3),
                    '--disk-id', disk, '--result-id', result])
        status = 0
    except Exception as exc:
        error = type(exc).__name__ + ': ' + str(exc)
    finally:
        files2, files3 = preserve(f2, out / 'f2', disk), preserve(f3, out / 'f3', disk)
        receipt = {'result': result, 'disk_id': disk, 'complete': status == 0,
            'exit_code': status, 'error': error, 'stages': stages,
            'F2_files': files2, 'F3_files': files3,
            'source_commit': read(out / 'public-actions-input.json')['source_commit'],
            'execution_environment': 'public-repository-github-actions',
            'original_chain_repeated': False, 'prior_run': item['prior_run'],
            'workflow_run_id': os.environ.get('GITHUB_RUN_ID'),
            'finished_at_utc': dt.datetime.now(dt.timezone.utc).isoformat()}
        p2 = f2 / (disk + '_actual_canonical_F2_polynomial47.json.gz')
        p3 = f3 / (disk + '_actual_canonical_F3_polynomial47.json.gz')
        if p2.exists():
            value = read(p2)
            receipt['F2_residual_roots'] = value['residual_QC_roots']
            receipt['F2_entire_disk_excluded'] = value['entire_disk_excluded_for_all_four_bad_components']
        if p3.exists():
            value = read(p3)
            receipt['F3_remaining_pairs'] = value['remaining_F2_F3_candidate_and_component_pairs']
            receipt['F2_F3_entire_disk_excluded'] = value['entire_disk_excluded_by_F2_and_F3_for_all_four_bad_components']
        save(out / 'run-receipt.json', receipt)
    print(json.dumps({'result': result, 'complete': status == 0, 'error': error}), flush=True)
    return status


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=['prepare', 'run', 'publish', 'verify'])
    parser.add_argument('--result', required=True)
    parser.add_argument('--budget-minutes', type=int, default=320)
    args = parser.parse_args()
    item = next(x for x in read(REQUEST)['jobs'] if x['result'] == args.result)
    base = Path(os.environ['RUNNER_TEMP']) / 'serre-p41-nonelliptic' / args.result
    if args.mode == 'prepare':
        prepare(item, base)
        return 0
    if args.mode == 'run':
        return run(item, base, args.budget_minutes)
    if args.mode == 'publish':
        return publish(item, base / 'output', artifact_prefix='serre-p41-nonelliptic',
                       omit_derived_based_points=True)
    return 0 if read(base / 'output/run-receipt.json')['complete'] else 1


if __name__ == '__main__':
    sys.exit(main())
