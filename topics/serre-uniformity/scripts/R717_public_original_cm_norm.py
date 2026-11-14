#!/usr/bin/env python3
"""Public R717 runner: preserve original inputs, resume, and publish certificates.

This wrapper was reconstructed after loss of the execution environment.
The mathematical core is separately pinned; this file changes no formula.
"""
from __future__ import annotations

import argparse
import datetime as dt
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import re
import shutil
import signal
import subprocess
import sys
import traceback

from p41_public_actions_recovery import REPO, TOPIC, publish, read, sha

S = Path(__file__).resolve().parent
CORE = S / 'R717_certified_original_CM_norm.py'
REQUEST = TOPIC / 'notes/R717-public-original-CM-norm-request.json'
WORKFLOW = REPO / '.github/workflows/serre-certified-original-CM-norm.yml'
FINAL = 'R717-exact-original-CM-norm.json'
SESSION = Path(os.environ.get('RUNNER_TEMP', '/tmp')) / 'R717-public-session.json'


def save(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + '.next')
    temporary.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')
    temporary.replace(path)


def canonical_digest(obj):
    raw = json.dumps(obj, sort_keys=True, separators=(',', ':')).encode()
    return hashlib.sha256(raw).hexdigest()


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def result_name(request, phase, shard):
    base = request['result']
    if not re.fullmatch(r'R717-[A-Za-z0-9_-]+', base):
        raise ValueError('The result name must be a plain R717 identifier')
    if phase == 'bins':
        return base + '-bins-' + str(shard)
    if phase == 'recover':
        return base + '-recover'
    return base


def validate_request(request, phase, shard):
    p = request['prime']
    if not isinstance(p, int) or p < 41 or p % 6 != 5:
        raise ValueError('R717 requires p >= 41 and p == 5 mod 6')
    count = request['shard_count']
    if not 1 <= count <= 16 or not 0 <= shard < count:
        raise ValueError('Invalid shard count or index')
    if phase == 'all' and count != 1:
        raise ValueError('Use bins and recover phases for a sharded request')
    for key in ('prec_bits', 'tail_bits', 'cutoff_multiple', 'checkpoint_rows',
                'timeout_seconds'):
        if not isinstance(request[key], int) or request[key] <= 0:
            raise ValueError('A positive explicit request parameter is required: ' + key)
    if request['python_flint_version'] != '0.9.0':
        raise ValueError('The certified arithmetic version must be 0.9.0')
    if sha(CORE) != request['arithmetic_sha256']:
        raise ValueError('The mathematical source does not match the request SHA')
    expected = request.get('expect_p2_product')
    if expected is not None and not 0 <= expected < p*p:
        raise ValueError('The expected calibration must be reduced modulo p^2')


def compatible_configuration(cfg, request):
    p = request['prime']
    cutoff = request['cutoff_multiple'] * p
    expected = {
        'result': 'R717', 'prime': p, 'n': p + 1,
        'D': str(2**37 * 3**26 * p**5),
        'source_sha256': request['arithmetic_sha256'],
        'python_flint': '0.9.0', 'prec_bits': request['prec_bits'],
        'tail_bits': request['tail_bits'], 'cutoff': cutoff,
        'cutoff_multiple': request['cutoff_multiple'],
        'a_max': math.isqrt((4*cutoff)//3),
        'shard_count': request['shard_count'],
        'normalization': 'R588 original chi6, theta_{-1}, S2*S3/C0^2; R717 v1',
    }
    if not isinstance(cfg, dict) or any(cfg.get(k) != v for k, v in expected.items()):
        return False
    without_digest = {k: v for k, v in cfg.items() if k != 'parameter_sha256'}
    return cfg.get('parameter_sha256') == canonical_digest(without_digest)


def local_file(directory, name):
    relative = Path(name)
    if relative.is_absolute() or relative.name != name or name in ('', '.', '..'):
        raise ValueError('Core artifacts must be plain filenames')
    return Path(directory) / relative


def check_final(path, request, require_artifacts=True):
    receipt = read(path)
    if not receipt.get('complete') or not compatible_configuration(receipt.get('configuration'), request):
        raise ValueError('An existing complete result has incompatible source or parameters: ' + str(path))
    if not receipt.get('all_rows_covered') or not receipt.get('all_trace_roundings_unique'):
        raise ValueError('The completed receipt lacks full coverage or trace uniqueness')
    expected = request.get('expect_p2_product')
    if expected is not None and receipt['padic_result'].get('p2_S2S3_mod_p2') != expected:
        raise ValueError('The current historical calibration failed, including on reuse')
    if require_artifacts:
        for row in receipt['artifacts']:
            file = local_file(Path(path).parent, row['file'])
            if not file.is_file() or sha(file) != row['sha256']:
                raise ValueError('A completed artifact is absent or has a wrong SHA: ' + str(file))
    return receipt


def check_bin(record, request, shard, require_complete=False):
    if not compatible_configuration(record.get('configuration'), request):
        raise ValueError('Incompatible bin configuration')
    if record.get('shard_index') != shard:
        raise ValueError('Wrong bin shard')
    cfg = record['configuration']
    expected_rows = len(range(shard+1, cfg['a_max']+1, request['shard_count']))
    rows = record['row_count']
    if not 0 <= rows <= expected_rows:
        raise ValueError('Invalid checkpoint row count')
    last = shard+1+(rows-1)*request['shard_count'] if rows else 0
    if record['completed_through_a'] != last:
        raise ValueError('The checkpoint does not contain a consecutive assigned prefix')
    if record.get('complete') and rows != expected_rows:
        raise ValueError('A completed bin omits rows')
    if require_complete and not record.get('complete'):
        raise ValueError('Recovery requires a complete bin')
    if record.get('bin_basis') != ['5:1', '5:zeta', '7:1', '7:zeta']:
        raise ValueError('Wrong exact Q(zeta) bin basis')
    if len(record['bins']) != 4 or any(len(row) != cfg['n'] for row in record['bins']):
        raise ValueError('Incomplete character bins')
    return record


def roots_for(names):
    # Large published outputs may be restored by an Actions download-artifact
    # step under this import directory.  They are never transmitted via chat.
    roots = []
    for base in (TOPIC/'computations', Path(os.environ.get('RUNNER_TEMP', '/tmp'))/'R717-imports'):
        for name in names:
            root = base/name
            if root.is_dir():
                roots.append(root)
    return roots


def candidates(names, filename):
    output = []
    for root in roots_for(names):
        output.extend(sorted(root.rglob(filename)))
    return output


def copy_exact(source, destination):
    source, destination = Path(source), Path(destination)
    if source.resolve() != destination.resolve():
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
    if sha(source) != sha(destination):
        raise ValueError('An exact artifact copy changed its SHA')


def restore_complete(request, out, phase):
    if phase == 'bins':
        return None
    names = [request['result'], request['result']+'-recover']
    possible = candidates(names, FINAL)
    if (out/FINAL).is_file():
        possible.insert(0, out/FINAL)
    valid = []
    missing = []
    for path in possible:
        data = read(path)
        if not data.get('complete'):
            continue
        # A completed result under this name is never silently recalculated
        # with new arithmetic or parameters; use an explicit new result name.
        check_final(path, request, require_artifacts=False)
        try:
            check_final(path, request, require_artifacts=True)
        except ValueError as error:
            missing.append(str(error))
            continue
        valid.append(path)
    if valid:
        path = valid[0]
        receipt = check_final(path, request)
        for row in receipt['artifacts']:
            copy_exact(local_file(path.parent, row['file']), local_file(out, row['file']))
        copy_exact(path, out/FINAL)
        return {'kind': 'complete_original_norm', 'source_receipt': str(path),
                'source_sha256': sha(path), 'arithmetic_repeated': False}
    if missing:
        raise RuntimeError('A completed result exists only partially in git. Restore its full '
                           'Actions artifact under RUNNER_TEMP/R717-imports before resuming. '
                           + missing[0])
    return None


def restore_bin(request, out, shard, require_complete):
    name = f'R717-bins-{shard}.json.gz'
    names = [request['result'], request['result']+'-recover',
             request['result']+'-bins-'+str(shard)]
    possible = candidates(names, name)
    if (out/name).is_file():
        possible.insert(0, out/name)
    valid = []
    for path in possible:
        record = read(path)
        if not compatible_configuration(record.get('configuration'), request):
            if record.get('complete'):
                raise RuntimeError('A completed bin has different source or precision; '
                                   'a new result identifier is required: ' + str(path))
            continue
        check_bin(record, request, shard)
        if not require_complete or record.get('complete'):
            valid.append((int(bool(record.get('complete'))), record['row_count'], path, record))
    if not valid:
        # A public complete-bin receipt may be present while its large .gz
        # lives only in the original Actions artifact.  Do not repeat it.
        for path in candidates(names, 'run-receipt.json'):
            summary = read(path)
            if summary.get('complete') and summary.get('phase') == 'bins':
                raise RuntimeError('A complete bin is recorded but its full artifact is missing. '
                                   'Restore the original Actions artifact under R717-imports.')
        if require_complete:
            raise RuntimeError('No complete certified bin was restored for shard ' + str(shard))
        return None
    valid.sort(key=lambda item: (item[0], item[1]), reverse=True)
    _, _, path, record = valid[0]
    copy_exact(path, out/name)
    return {'kind': 'bin', 'shard_index': shard, 'source_file': str(path),
            'source_sha256': sha(path), 'complete': record['complete'],
            'row_count': record['row_count'],
            'completed_through_a': record['completed_through_a'],
            'completed_prefix_repeated': False}


def archive_sources(out, request, source):
    paths = [CORE, Path(__file__), S/'p41_public_actions_recovery.py',
             REQUEST, WORKFLOW, REPO/'README.md', TOPIC/'README.md']
    source_rows = []
    for path in paths:
        relative = path.relative_to(REPO)
        target = out/'sources'/Path(str(relative)+'.gz')
        target.parent.mkdir(parents=True, exist_ok=True)
        data = path.read_bytes()
        with target.open('wb') as raw:
            with gzip.GzipFile(filename='', mode='wb', fileobj=raw, mtime=0) as stream:
                stream.write(data)
        source_rows.append({'repository_path': str(relative), 'bytes': len(data),
                            'sha256': hashlib.sha256(data).hexdigest(),
                            'archive_file': str(target.relative_to(out)), 'archive_sha256': sha(target)})
    initial = {
        'result': request['result'], 'source_commit': source,
        'source_repository': 'Rogerhu12/math-research-public',
        'execution_environment': 'public-repository-github-actions',
        'request': request, 'request_sha256': sha(REQUEST),
        'arithmetic_sha256': sha(CORE), 'wrapper_sha256': sha(__file__),
        'publisher_sha256': sha(S/'p41_public_actions_recovery.py'),
        'workflow_sha256': sha(WORKFLOW),
        'root_readme_sha256': sha(REPO/'README.md'),
        'topic_readme_sha256': sha(TOPIC/'README.md'),
        'sources': source_rows, 'prepared_at_utc': now(),
        'run_url': os.environ.get('GITHUB_SERVER_URL', 'https://github.com')+'/'
                   +os.environ.get('GITHUB_REPOSITORY', 'Rogerhu12/math-research-public')
                   +'/actions/runs/'+os.environ.get('GITHUB_RUN_ID', 'unregistered'),
        'mathematical_completion_claimed': False,
    }
    save(out/'public-actions-input.json', initial)


def core_command(request, out, phase, shard):
    command = [sys.executable, '-u', str(CORE), '--prime', str(request['prime']),
               '--phase', phase, '--output-dir', str(out),
               '--shard-count', str(request['shard_count']), '--shard-index', str(shard),
               '--prec-bits', str(request['prec_bits']), '--tail-bits', str(request['tail_bits']),
               '--cutoff-multiple', str(request['cutoff_multiple']),
               '--checkpoint-rows', str(request['checkpoint_rows'])]
    expected = request.get('expect_p2_product')
    if expected is not None:
        command += ['--expect-p2-product', str(expected)]
    return command


def verify_math(request, out, phase, shard):
    if phase == 'bins':
        path = out/f'R717-bins-{shard}.json.gz'
        data = check_bin(read(path), request, shard, require_complete=True)
        return {'bin_file': path.name, 'bin_sha256': sha(path),
                'row_count': data['row_count'], 'term_count': data['term_count']}
    receipt = check_final(out/FINAL, request)
    return {'core_receipt': FINAL, 'core_receipt_sha256': sha(out/FINAL),
            'padic_result': receipt['padic_result'],
            'all_rows_covered': True, 'all_trace_roundings_unique': True}


def compute(phase, shard):
    request = read(REQUEST)
    result = result_name(request, phase, shard)
    out = Path(os.environ['RUNNER_TEMP'])/'serre-cartier'/result
    out.mkdir(parents=True, exist_ok=True)
    session = {'request': request, 'result': result, 'output': str(out),
               'phase': phase, 'shard_index': shard}
    save(SESSION, session)
    summary = {'result': result, 'phase': phase, 'shard_index': shard,
               'complete': False, 'started_at_utc': now(),
               'workflow_run_id': os.environ.get('GITHUB_RUN_ID'),
               'workflow_attempt': os.environ.get('GITHUB_RUN_ATTEMPT'),
               'execution_environment': 'public-repository-github-actions',
               'arithmetic_sha256': sha(CORE), 'mathematical_completion_claimed': False}
    save(out/'run-receipt.json', summary)
    code = 1
    try:
        source = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=REPO, text=True).strip()
        archive_sources(out, request, source)
        summary['source_commit'] = source
        validate_request(request, phase, shard)
        restored = []
        completed = restore_complete(request, out, phase)
        if completed:
            restored.append(completed)
        elif phase == 'recover':
            for index in range(request['shard_count']):
                restored.append(restore_bin(request, out, index, require_complete=True))
        else:
            found = restore_bin(request, out, shard, require_complete=False)
            if found:
                restored.append(found)
        save(out/'R717-restored-inputs.json', {'restored': restored,
                                              'all_completed_prefixes_preserved': True})
        command = core_command(request, out, phase, shard)
        save(out/'R717-command.json', {'argv': command, 'timeout_seconds': request['timeout_seconds'],
                                      'request': request})
        with (out/'R717-public-run.log').open('w') as log:
            process = subprocess.Popen(command, cwd=REPO, stdout=log, stderr=subprocess.STDOUT,
                                       start_new_session=True)
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
            raise RuntimeError('The mathematical process did not complete; exit code ' + str(code))
        summary.update(verify_math(request, out, phase, shard))
        summary['complete'] = True
        summary['reused_or_resumed_inputs'] = restored
    except Exception:
        (out/'R717-public-failure.txt').write_text(traceback.format_exc())
        summary['complete'] = False
        summary['failure_file'] = 'R717-public-failure.txt'
        if code == 0:
            code = 1
    summary['finished_at_utc'] = now()
    save(out/'run-receipt.json', summary)
    print(json.dumps({'result': result, 'phase': phase, 'complete': summary['complete'],
                      'exit_code': code, 'output': str(out)}), flush=True)
    return 0 if summary['complete'] else code or 1


def saved_session():
    session = read(SESSION)
    out = Path(session['output'])
    initial = read(out/'public-actions-input.json')
    if initial['request'] != session['request']:
        raise ValueError('The saved request changed across publication')
    return session, out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=['compute', 'publish', 'verify'])
    parser.add_argument('--phase', choices=['all', 'bins', 'recover'], default='all')
    parser.add_argument('--shard-index', type=int, default=0)
    args = parser.parse_args()
    if args.mode == 'compute':
        return compute(args.phase, args.shard_index)
    # Publication checks out the latest main.  The original immutable session
    # controls result names and calibration after that checkout as well.
    session, out = saved_session()
    if args.mode == 'publish':
        return publish({'result': session['result']}, out, artifact_prefix='serre-cartier')
    summary = read(out/'run-receipt.json')
    if not summary.get('complete'):
        print(json.dumps({'complete': False, 'failure_file': summary.get('failure_file')}), flush=True)
        return 1
    verified = verify_math(session['request'], out, session['phase'], session['shard_index'])
    print(json.dumps({'complete': True, 'result': session['result'], 'verified': verified}), flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())
