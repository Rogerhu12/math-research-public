#!/usr/bin/env python3
"""Run and preserve the original R719 p137147 primitive-average certificate."""
from __future__ import annotations

import argparse
import datetime as dt
import gzip
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import traceback

from p41_public_actions_recovery import REPO, TOPIC, publish, read, sha

S = Path(__file__).resolve().parent
CORE = S / 'run_r719_p137147_primitive_certificate.py'
CPP = S / 'r719_visible_order_histogram.cpp'
REQUEST = TOPIC / 'notes/R719-public-p137147-primitive-request.json'
WORKFLOW = REPO / '.github/workflows/serre-p137147-primitive-average.yml'
CERTIFICATE = 'r719_p137147_primitive_certificate.json'
SESSION = Path(os.environ.get('RUNNER_TEMP', '/tmp')) / 'R719-public-session.json'
PROOF = 'notes/R719-p137147-original-primitive-visible-enumeration-method.md'


def save(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + '.next')
    temporary.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')
    temporary.replace(path)


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def validate_request(request):
    expected = {
        'result': 'R719-p137147-primitive',
        'prime': 137147, 'radius_multiplier': 25, 'audit_norm_cutoff': 10000,
        'precision_bits': 256, 'rational_upper_denominator': 10**12,
        'python_flint_version': '0.9.0', 'proof_path': PROOF,
    }
    if any(request.get(key) != value for key, value in expected.items()):
        raise ValueError('The fixed original R719 request parameters changed')
    if request['cpp_sha256'] != sha(CPP) or request['python_sha256'] != sha(CORE):
        raise ValueError('The original arithmetic sources do not match the request')
    if not isinstance(request['timeout_seconds'], int) or request['timeout_seconds'] <= 0:
        raise ValueError('An explicit positive process timeout is required')
    import flint
    if flint.__version__ != request['python_flint_version']:
        raise ValueError('python-flint must be the requested version 0.9.0')


def archive_sources(out, request, source):
    paths = [
        CPP, CORE, Path(__file__), S/'p41_public_actions_recovery.py',
        REQUEST, WORKFLOW, REPO/'README.md', TOPIC/'README.md',
        TOPIC/request['proof_path'],
        TOPIC/'results/R714-global-visible-count-and-sublogarithmic-divisor-primitive-region.md',
        TOPIC/'results/R616-original-CM-point-difference-and-explicit-height-basis.md',
    ]
    records = []
    for path in paths:
        relative = path.relative_to(REPO)
        target = out/'sources'/Path(str(relative)+'.gz')
        target.parent.mkdir(parents=True, exist_ok=True)
        data = path.read_bytes()
        with target.open('wb') as raw:
            with gzip.GzipFile(filename='', mode='wb', fileobj=raw, mtime=0) as stream:
                stream.write(data)
        records.append({
            'repository_path': str(relative), 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest(),
            'archive_file': str(target.relative_to(out)), 'archive_sha256': sha(target),
        })
    initial = {
        'result': request['result'], 'request': request, 'source_commit': source,
        'source_repository': 'Rogerhu12/math-research-public',
        'execution_environment': 'public-repository-github-actions',
        'request_sha256': sha(REQUEST), 'workflow_sha256': sha(WORKFLOW),
        'wrapper_sha256': sha(__file__),
        'publisher_sha256': sha(S/'p41_public_actions_recovery.py'),
        'root_readme_sha256': sha(REPO/'README.md'),
        'topic_readme_sha256': sha(TOPIC/'README.md'),
        'sources': records, 'prepared_at_utc': now(),
        'run_id': os.environ.get('GITHUB_RUN_ID'),
        'run_attempt': os.environ.get('GITHUB_RUN_ATTEMPT'),
        'mathematical_completion_claimed': False,
    }
    save(out/'public-wrapper-input.json', initial)
    return initial


def verify_math(request, out):
    receipt = read(out/'run-receipt.json')
    certificate = read(out/CERTIFICATE)
    inputs = read(out/'public-actions-input.json')
    wrapper_inputs = read(out/'public-wrapper-input.json')
    if not receipt.get('complete') or not receipt.get('mathematical_bound_closed'):
        raise ValueError('The exact run has not closed the mathematical bound')
    if receipt.get('repository') != 'Rogerhu12/math-research-public':
        raise ValueError('Wrong execution repository')
    if receipt['source_commit'] != wrapper_inputs['source_commit']:
        raise ValueError('The archived arithmetic source commit changed')
    expected_sources = {'cpp': request['cpp_sha256'], 'python': request['python_sha256']}
    if receipt['source_sha256'] != expected_sources:
        raise ValueError('The completed receipt has different arithmetic sources')
    parameters = inputs['parameters']
    expected_parameters = {
        'p': 137147, 'M': 45716, 'radius_multiplier': 25,
        'norm_cutoff': 25*137147, 'audit_norm_cutoff': 10000,
        'arb_precision_bits': request['precision_bits'],
        'rational_upper_denominator': request['rational_upper_denominator'],
    }
    if parameters != expected_parameters or inputs['python_flint_version'] != '0.9.0':
        raise ValueError('The completed input parameters differ from the fixed request')
    if certificate.get('status') != 'proved' or certificate.get('p') != 137147:
        raise ValueError('No proved certificate for the requested prime')
    for key in (
        'formal_public_actions_run', 'B_less_than_one_half',
        'original_cubic_phase_retained',
        'original_positive_quotient_and_negative_second_factor_retained',
        'original_R616_nonvanishing_rank_log_premise_certified',
        'tail_includes_all_primary_points_above_cutoff',
    ):
        if certificate.get(key) is not True:
            raise ValueError('The certificate is missing a mathematical condition: '+key)
    bound = certificate['common_error_B_strict_rational_upper']
    numerator, denominator = bound['numerator'], bound['denominator']
    if (not isinstance(numerator, int) or not isinstance(denominator, int)
            or numerator < 0 or denominator != request['rational_upper_denominator']
            or not bound.get('strict_arb_upper_comparison_verified')
            or not 2*numerator < denominator):
        raise ValueError('The original common error B is not certified strictly below 1/2')
    if not certificate['audit']['all_small_radius_points_and_orders_equal']:
        raise ValueError('The complete independent small-radius order audit failed')
    if certificate['input_receipt_sha256'] != sha(out/'public-actions-input.json'):
        raise ValueError('The mathematical input receipt changed')
    for filename, digest in receipt['outputs_sha256'].items():
        if sha(out/filename) != digest:
            raise ValueError('A preserved mathematical output changed: '+filename)
    for row in wrapper_inputs['sources']:
        if sha(out/row['archive_file']) != row['archive_sha256']:
            raise ValueError('A preserved original source changed: '+row['repository_path'])
    return {
        'certificate': CERTIFICATE, 'certificate_sha256': sha(out/CERTIFICATE),
        'common_error_B_strict_rational_upper': bound,
        'original_R616_nonvanishing_rank_log_premise_certified': True,
    }


def compute():
    request = read(REQUEST)
    out = Path(os.environ['RUNNER_TEMP'])/'serre-cartier'/request['result']
    out.mkdir(parents=True, exist_ok=True)
    logs = out/'wrapper'
    logs.mkdir(exist_ok=True)
    session = {'request': request, 'output': str(out)}
    save(SESSION, session)
    summary = {
        'result': request['result'], 'complete': False,
        'started_at_utc': now(), 'mathematical_completion_claimed': False,
    }
    code = 1
    # The publisher can preserve this fallback even if preparation fails.
    source = os.environ.get('GITHUB_SHA')
    save(out/'public-actions-input.json', {
        'source_commit': source, 'result': request['result'],
        'preparation_complete': False, 'mathematical_completion_claimed': False,
    })
    try:
        source = subprocess.check_output(
            ['git', 'rev-parse', 'HEAD'], cwd=REPO, text=True).strip()
        summary['source_commit'] = source
        archive_sources(out, request, source)
        validate_request(request)
        command = [
            sys.executable, '-u', str(CORE), '--output', str(out),
            '--cpp-source', str(CPP), '--repo-root', str(REPO),
            '--proof-path', str(TOPIC/request['proof_path']),
            '--precision', str(request['precision_bits']),
            '--denominator', str(request['rational_upper_denominator']),
        ]
        save(out/'R719-command.json', {
            'argv': command, 'timeout_seconds': request['timeout_seconds']})
        environment = os.environ.copy()
        environment['GITHUB_SHA'] = source
        # Keep this growing log below a subdirectory: the original driver
        # binds all root-level output files before its final stdout message.
        with (logs/'R719-public-run.log').open('w') as log:
            process = subprocess.Popen(
                command, cwd=REPO, env=environment, stdout=log,
                stderr=subprocess.STDOUT, start_new_session=True)
            try:
                code = process.wait(timeout=request['timeout_seconds'])
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGTERM)
                try:
                    process.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGKILL)
                    process.wait()
                code = 124
        summary['process_exit_code'] = code
        if code:
            raise RuntimeError('Original R719 process returned '+str(code)
                               +'; complete and failed outputs are retained')
        summary.update(verify_math(request, out))
        summary['complete'] = True
    except Exception:
        (logs/'R719-public-failure.txt').write_text(traceback.format_exc())
        summary['failure_file'] = 'wrapper/R719-public-failure.txt'
        if code == 0:
            code = 1
    summary['finished_at_utc'] = now()
    save(out/'wrapper-receipt.json', summary)
    print(json.dumps({
        'result': request['result'], 'complete': summary['complete'],
        'process_exit_code': code, 'output': str(out),
    }), flush=True)
    return 0 if summary['complete'] else code or 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=['compute', 'publish', 'verify'])
    args = parser.parse_args()
    if args.mode == 'compute':
        return compute()
    session = read(SESSION)
    request, out = session['request'], Path(session['output'])
    # Publication may check out a newer main; use the original saved request.
    if args.mode == 'publish':
        return publish({'result': request['result']}, out, artifact_prefix='serre-cartier')
    summary = read(out/'wrapper-receipt.json')
    if not summary.get('complete'):
        print(json.dumps({'complete': False, 'failure_file': summary.get('failure_file')}))
        return 1
    verified = verify_math(request, out)
    print(json.dumps({'complete': True, 'result': request['result'], 'verified': verified}))
    return 0


if __name__ == '__main__':
    sys.exit(main())
