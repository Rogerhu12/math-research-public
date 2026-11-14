#!/usr/bin/env python3
"""Continue only preserved missing ramified stages, with complete pole/root checks."""
import argparse
import datetime as dt
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time
from p41_public_actions_recovery import S, TOPIC, publish, read, save
from p41_public_nonelliptic_resume import prepare
from p41_ci_recover_ramified_ss47 import preserve

REQUEST = TOPIC / 'notes/public-p41-ramified-tail-request.json'
D = S / 'data'


def run(item, base, budget):
    out, f2, f3 = base / 'output', base / 'work/f2', base / 'work/f3'
    disk, ident = item['disk_id'], item['result']
    based = f2 / (ident + '_' + disk + '_based_points47.json.gz')
    derivative = D / 'p41_serre_clearing_126_disks47.json.gz'
    rc = D / 'p41_ramified_j_regular_height_derivative47.json.gz'
    ra = D / 'p41_ramified_j_regular_height_derivative47_independent.json'
    stages, error, code = [], None, 1
    started = time.monotonic()

    def execute(label, command):
        remaining = budget * 60 - (time.monotonic() - started)
        if remaining <= 0:
            raise TimeoutError('Preserved-tail time budget exhausted before ' + label)
        with (out / (label + '.log')).open('w') as log:
            process = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
            try:
                status = process.wait(timeout=remaining)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()
                raise TimeoutError('Preserved-tail time budget exhausted during ' + label)
        stages.append({'stage': label, 'command': command, 'exit_code': status})
        if status:
            raise subprocess.CalledProcessError(status, command)

    def f3_command():
        return [sys.executable, '-u', str(S / 'p41_rebuild_ramified_SS_F3_unit_parameter47.py'),
            '--script-dir', str(S), '--source-dir', str(S), '--f2-dir', str(f2),
            '--recovery-dir', str(f2 / 'recovery-inputs'), '--based-points', str(based),
            '--canonical', str(D / 'p41_canonical_SS_robust47_raw.json.gz'),
            '--derivative', str(derivative), '--ramified-j-certificate', str(rc),
            '--ramified-j-audit', str(ra), '--work-dir', str(f3),
            '--disk-id', disk, '--result-id', ident]

    try:
        if item['missing_stage'] == 'F2_multiple_root_audit':
            command = [sys.executable, '-u', str(S / 'verify_selected_SS_F2_ramified_unit_parameter47.py'),
                '--script-dir', str(S), '--source-dir', str(S),
                '--ramified-j-certificate', str(rc), '--ramified-j-audit', str(ra),
                '--poly-source', str(S / 'p41_selected_SS_F2_polynomial_ramified_unit_parameter47.py'),
                '--polynomial', str(f2 / (disk + '_actual_canonical_F2_polynomial47.json.gz')),
                '--derivative', str(derivative),
                '--norm-source', str(S / 'p41_SS_F2_full_canonical_norm_ramified_unit_parameter47.py'),
                '--center-source', str(S / 'p41_selected_SS_F2_connection_ramified_unit_parameter47.py'),
                '--qc-dir', str(f2), '--chain-dir', str(f2 / 'chain'),
                '--transport-dir', str(f2 / 'SS-principal-transports' / disk),
                '--based-points', str(based), '--disk-id', disk, '--result-id', ident,
                '--output', str(f2 / (disk + '-principal-F2-independent-audit.json'))]
        elif item['missing_stage'] == 'F2_finite_flat_poles':
            command = [sys.executable, '-u', str(S / 'p41_rebuild_ramified_SS_F2_unit_parameter47.py'),
                '--script-dir', str(S), '--work-dir', str(f2), '--disk-id', disk,
                '--result-id', ident, '--canonical', str(D / 'p41_canonical_SS_robust47_raw.json.gz'),
                '--canonical-certificate', str(D / 'p41_canonical_SS_robust47_certificate.json.gz'),
                '--derivative', str(derivative), '--ramified-j-certificate', str(rc),
                '--ramified-j-audit', str(ra), '--based-points', str(based),
                '--rebuild-chain', '--resume-stages']
        else:
            assert item['missing_stage'] == 'F3_auxiliary_denominator'
            command = f3_command()
        execute(item['missing_stage'], command)
        if item['missing_stage'] == 'F2_finite_flat_poles':
            polynomial = read(f2 / (disk + '_actual_canonical_F2_polynomial47.json.gz'))
            audit = read(f2 / (disk + '-principal-F2-independent-audit.json'))
            if polynomial['residual_QC_roots'] and not audit.get('entire_disk_excluded_by_F2_after_exact_lifting', False):
                execute('actual_same_component_F3', f3_command())
        code = 0
    except Exception as exc:
        code = 1
        error = type(exc).__name__ + ': ' + str(exc)
    finally:
        rows2, rows3 = preserve(f2, out / 'f2', disk), preserve(f3, out / 'f3', disk)
        receipt = {'result': ident, 'disk_id': disk, 'complete': code == 0, 'exit_code': code,
            'error': error, 'stages': stages, 'F2_files': rows2, 'F3_files': rows3,
            'source_commit': read(out / 'public-actions-input.json')['source_commit'],
            'execution_environment': 'public-repository-github-actions',
            'original_chain_repeated': False, 'prior_run': item['prior_run'],
            'workflow_run_id': os.environ.get('GITHUB_RUN_ID'),
            'elapsed_seconds': round(time.monotonic() - started, 3),
            'finished_at_utc': dt.datetime.now(dt.timezone.utc).isoformat()}
        p2 = f2 / (disk + '_actual_canonical_F2_polynomial47.json.gz')
        a2 = f2 / (disk + '-principal-F2-independent-audit.json')
        p3 = f3 / (disk + '_actual_canonical_F3_polynomial47.json.gz')
        if p2.exists():
            value = read(p2)
            receipt['F2_residual_roots'] = value['residual_QC_roots']
            receipt['F2_entire_disk_excluded'] = value['entire_disk_excluded_for_all_four_bad_components']
        if a2.exists():
            receipt['F2_entire_disk_excluded_after_exact_lifting'] = read(a2).get('entire_disk_excluded_by_F2_after_exact_lifting', False)
        if p3.exists():
            value = read(p3)
            receipt['F3_remaining_pairs'] = value['remaining_F2_F3_candidate_and_component_pairs']
            receipt['F2_F3_entire_disk_excluded'] = value['entire_disk_excluded_by_F2_and_F3_for_all_four_bad_components']
        save(out / 'run-receipt.json', receipt)
    print(json.dumps({'result': ident, 'complete': code == 0, 'error': error}), flush=True)
    return code


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=['prepare', 'run', 'publish', 'verify'])
    parser.add_argument('--result', required=True)
    parser.add_argument('--budget-minutes', type=int, default=320)
    args = parser.parse_args()
    item = next(x for x in read(REQUEST)['jobs'] if x['result'] == args.result)
    base = Path(os.environ['RUNNER_TEMP']) / 'serre-p41-ramified-tail' / args.result
    if args.mode == 'prepare':
        prepare(item, base, request_path=REQUEST)
        return 0
    if args.mode == 'run':
        return run(item, base, args.budget_minutes)
    if args.mode == 'publish':
        return publish(item, base / 'output', artifact_prefix='serre-p41-ramified-tail', omit_derived_based_points=True)
    return 0 if read(base / 'output/run-receipt.json')['complete'] else 1


if __name__ == '__main__':
    sys.exit(main())
