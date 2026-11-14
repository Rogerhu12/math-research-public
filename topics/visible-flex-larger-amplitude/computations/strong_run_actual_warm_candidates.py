#!/usr/bin/env python3
"""Run an explicit actual full-field warm plan sequentially, never a BVP.

The supplied proven local-check command supplies the accepted baseline and
frozen geometry inputs.  Only actual low-core targets, whole-field response,
fresh output paths and the explicit warm-inspection option change.  Each
child is formally waited and has its own wait4 resource record.  A warm
comparison is not an accepted actual solution or a nonlinear tail solve.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import time


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan', type=Path, required=True)
    parser.add_argument('--baseline-command', type=Path, required=True)
    parser.add_argument('--out-prefix', type=Path, required=True)
    args = parser.parse_args()
    plan = json.loads(args.plan.read_text())
    reference_command = json.loads(args.baseline_command.read_text())
    command = reference_command[reference_command.index('--')+1:]
    i = command.index('--inspect-local-output')
    del command[i:i+2]
    command[0] = sys.executable
    response = Path(plan['response_file'])
    if sha(response) != plan['response_sha256']:
        raise ValueError('The full actual response changed')
    hashes = {str(p): sha(p) for p in (Path(__file__), args.plan, args.baseline_command,
        response, Path(command[1]), Path(command[1]).with_name('strong_actual_augmented_core.py'),
        Path(command[1]).with_name('strong_actual_warm_screen.py'))}
    output = args.out_prefix.with_suffix('.json')
    if output.exists():
        raise FileExistsError('Use a fresh warm-batch output prefix')
    ledger = args.out_prefix.with_name(args.out_prefix.name+'-ledger.jsonl')
    if ledger.exists():
        raise FileExistsError('The warm-batch ledger already exists')
    results = []
    start = time.monotonic()
    for case in plan['candidates']:
        if not re.fullmatch('[a-z0-9-]+', case['name']):
            raise ValueError('Invalid candidate name')
        prefix = args.out_prefix.with_name(args.out_prefix.name+'-'+case['name'])
        report_file = prefix.with_name(prefix.name+'-screen.json')
        resource_file = prefix.with_name(prefix.name+'-resource.json')
        log_file = prefix.with_name(prefix.name+'-log.txt')
        current = command.copy()
        current[current.index('--out-prefix')+1] = str(prefix)
        j = current.index('--target-core')
        current[j+1:j+4] = [repr(v) for v in case['actual_target']]
        current += ['--response-data', str(response), '--inspect-warm-output', str(report_file),
                    '--max-nodes', '2400']
        wrapped = [sys.executable, str(Path(current[1]).with_name('strong_resource_run.py')),
            '--out', str(resource_file), '--', *current]
        row = dict(name=case['name'], actual_target=case['actual_target'], command=wrapped,
            source_sha256=hashes, expected_warm_profile=case['predicted_profile'])
        prefix.with_name(prefix.name+'-command.json').write_text(json.dumps(row, indent=2)+'\n')
        print(json.dumps(dict(event='warm_candidate_begin', name=case['name'], prefix=str(prefix))), flush=True)
        with log_file.open('w') as stream:
            completed = subprocess.run(wrapped, stdout=stream, stderr=subprocess.STDOUT)
        row.update(exitcode=completed.returncode, resource_file=str(resource_file),
            log_file=str(log_file), report_file=str(report_file))
        if completed.returncode != 0 or not report_file.is_file():
            row['finished'] = False
            with ledger.open('a') as stream:
                stream.write(json.dumps(row)+'\n')
            raise RuntimeError('Warm candidate did not finish: '+case['name'])
        report = json.loads(report_file.read_text())
        if (not report.get('finished') or report.get('nonlinear_solution')
                or report.get('true_new_H_tail_evaluated') or report.get('worker_start_attempts')):
            raise ValueError('The explicit unsolved warm scope changed')
        for field in ('delta', 'boost_length', 'boost_speed'):
            if abs(report['warm_profile'][field]-case['predicted_profile'][field]) > 3e-14:
                raise ValueError('The full warm parameter conversion differs: '+field)
        row.update(finished=True, report_sha256=sha(report_file),
            finite_domain_passed=report['finite_domain_passed'],
            full_collocation=report.get('full_collocation'),
            physical_budget=report.get('warm_physical_cubic_geometry'))
        with ledger.open('a') as stream:
            stream.write(json.dumps(row)+'\n')
        results.append(row)
        print(json.dumps(dict(event='warm_candidate_complete', name=case['name'],
            finite_domain_passed=row['finite_domain_passed'],
            rms=None if not row['full_collocation'] else row['full_collocation']['rms_max'],
            kappa_D=None if not row['physical_budget'] else row['physical_budget']['kappa_times_D_sample'],
            seconds=time.monotonic()-start)), flush=True)
    result = dict(scope=__doc__, finished=True, nonlinear_solution=False,
        source_sha256=hashes, candidates=results, seconds=time.monotonic()-start)
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(event='all_actual_warm_candidates_complete', count=len(results),
        seconds=result['seconds'], output=str(output))), flush=True)


if __name__ == '__main__':
    main()
