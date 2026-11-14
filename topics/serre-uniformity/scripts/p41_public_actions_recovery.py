#!/usr/bin/env python3
"""Resume the published p41 prefixes and publish bounded actual outputs."""
import argparse
import datetime as dt
import gzip
import hashlib
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import tarfile

S = Path(__file__).resolve().parent
REPO = S.parents[2]
TOPIC = REPO / 'topics/serre-uniformity'
REQUEST = TOPIC / 'notes/public-p41-recovery-request.json'

def read(path):
    path = Path(path)
    data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == '.gz' else data)

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def git(*args, check=True):
    auth = ['-c', 'credential.helper=', '-c',
            'credential.helper=!f() { printf "%s\\n" "username=x-access-token" "password=$SERRE_ACTIONS_TOKEN"; }; f']
    result = subprocess.run(['git', *auth, *args], cwd=REPO, text=True,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if result.stdout:
        print(result.stdout, flush=True)
    if check and result.returncode:
        raise RuntimeError('Git command failed: ' + args[0])
    return result

def prepare(item, work, out):
    work.mkdir(parents=True, exist_ok=True)
    out.mkdir(parents=True, exist_ok=True)
    archive = S / 'data' / item['prefix_archive']
    assert sha(archive) == item['prefix_sha256']
    with tarfile.open(archive, 'r:gz') as tf:
        for member in tf.getmembers():
            relative = Path(member.name)
            assert member.isfile() and not relative.is_absolute() and '..' not in relative.parts
            target = work / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            data = tf.extractfile(member).read()
            if target.exists():
                assert target.read_bytes() == data
            else:
                target.write_bytes(data)
    manifest = read(work / 'prefix-snapshot-manifest.json')
    assert manifest['result'] == item['result'] and manifest['disk_id'] == item['disk_id']
    assert manifest['saved_bits'] == item['saved_bits']
    for row in manifest['files']:
        assert sha(work / row['file']) == row['sha256']
    state = read(work / 'f2/chain' / (item['disk_id'] + '_multiply47.json.gz'))
    assert state['bits_done'] == item['saved_bits'] and state['target_bits'] == 304
    source = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=REPO, text=True).strip()
    save(out / 'public-actions-input.json', {
        'result': item['result'], 'disk_id': item['disk_id'], 'source_commit': source,
        'source_repository': 'Rogerhu12/math-research-public',
        'request_sha256': sha(REQUEST), 'driver_sha256': sha(__file__),
        'prefix': item, 'restored_prefix_files': len(manifest['files']),
        'root_readme_sha256': sha(REPO / 'README.md'),
        'topic_readme_sha256': sha(TOPIC / 'README.md'),
        'run_url': os.environ.get('GITHUB_SERVER_URL', 'https://github.com') + '/' +
                   os.environ.get('GITHUB_REPOSITORY', 'Rogerhu12/math-research-public') +
                   '/actions/runs/' + os.environ.get('GITHUB_RUN_ID', 'local-prepare'),
        'prepared_at_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
        'mathematical_completion_claimed': False,
    })

def run(item, work, out, budget):
    command = [sys.executable, '-u', str(S / 'p41_resume_ramified_local47.py'),
               '--script-dir', str(S), '--work-dir', str(work), '--output', str(out),
               '--result-id', item['result'], '--disk-id', item['disk_id']]
    error = None
    with (out / 'public-actions-run.log').open('w') as stream:
        process = subprocess.Popen(command, stdout=stream, stderr=subprocess.STDOUT,
                                   start_new_session=True)
        try:
            code = process.wait(timeout=budget * 60)
        except subprocess.TimeoutExpired:
            error = 'Runner budget exhausted; preserved actual prefix and stage outputs.'
            os.killpg(process.pid, signal.SIGTERM)
            try:
                process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.wait()
            code = 124
    if not (out / 'run-receipt.json').exists():
        from p41_ci_recover_ramified_ss47 import preserve
        files2 = preserve(work / 'f2', out / 'f2', item['disk_id'])
        files3 = preserve(work / 'f3', out / 'f3', item['disk_id'])
        save(out / 'run-receipt.json', {'result': item['result'], 'disk_id': item['disk_id'],
            'complete': False, 'exit_code': code, 'error': error or 'Driver stopped before receipt.',
            'F2_files': files2, 'F3_files': files3})
    receipt = read(out / 'run-receipt.json')
    receipt.update(execution_environment='public-repository-github-actions',
        workflow_run_id=os.environ.get('GITHUB_RUN_ID'),
        workflow_attempt=os.environ.get('GITHUB_RUN_ATTEMPT'),
        source_commit=read(out / 'public-actions-input.json')['source_commit'],
        original_prefix_bits=item['saved_bits'], saved_chain_prefix_repeated=False,
        process_exit_code=code, finished_at_utc=dt.datetime.now(dt.timezone.utc).isoformat())
    if code:
        receipt['complete'] = False
    save(out / 'run-receipt.json', receipt)
    print(json.dumps({'result': item['result'], 'complete': receipt['complete'],
                      'process_exit_code': code, 'output': str(out)}), flush=True)
    return code

def publish(item, out, artifact_prefix='serre-p41', omit_derived_based_points=False):
    initial = read(out / 'public-actions-input.json')
    source = initial['source_commit']
    run_id = os.environ['GITHUB_RUN_ID'] + '-' + os.environ['GITHUB_RUN_ATTEMPT']
    relative = Path('topics/serre-uniformity/computations') / item['result'] / run_id
    git('fetch', 'origin', 'main')
    difference = git('diff', source, 'origin/main', '--', 'README.md',
                     'topics/serre-uniformity/README.md')
    if difference.stdout.strip():
        save(out / 'publication-receipt.json', {'published': False,
             'reason': 'README changed; root continuation must read and apply the diff.',
             'rules_diff': difference.stdout})
        return 3
    git('checkout', '-B', 'serre-output-' + run_id + '-' + item['result'], 'origin/main')
    destination = REPO / relative
    destination.mkdir(parents=True, exist_ok=True)
    rows = []
    for path in sorted(out.rglob('*')):
        if not path.is_file() or path.name == 'publication-receipt.json':
            continue
        rel = path.relative_to(out)
        size = path.stat().st_size
        derived_input = omit_derived_based_points and 'based_points' in path.name
        include = size < 5_000_000 and not derived_input
        rows.append({'file': str(rel), 'bytes': size, 'sha256': sha(path),
                     'included_in_git': include})
        if derived_input:
            rows[-1]['omitted_reason'] = ('Reproducible based-point input; original input archive '
                'or atlas, exact command and SHA are retained. Full copy is in the Actions artifact.')
        if include:
            target = destination / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            if size > 1_000_000 and path.suffix != '.gz':
                target = target.with_name(target.name + '.gz')
                with target.open('wb') as raw:
                    with gzip.GzipFile(fileobj=raw, mode='wb', mtime=0, filename='') as gz:
                        gz.write(path.read_bytes())
                rows[-1]['stored_file'] = str(target.relative_to(destination))
                rows[-1]['stored_sha256'] = sha(target)
            else:
                shutil.copyfile(path, target)
    save(destination / 'files-manifest.json', {'files': rows,
         'full_outputs_artifact': artifact_prefix + '-' + item['result'] + '-' + run_id,
         'source_commit': source, 'mathematical_theorem_registered': False})
    git('config', 'user.name', 'github-actions[bot]')
    git('config', 'user.email', '41898282+github-actions[bot]@users.noreply.github.com')
    git('add', '--sparse', str(relative))
    git('commit', '-m', 'serre: preserve ' + item['result'] + ' actual public Actions outputs')
    while True:
        git('pull', '--rebase', 'origin', 'main')
        difference = git('diff', source, 'origin/main', '--', 'README.md',
                         'topics/serre-uniformity/README.md')
        if difference.stdout.strip():
            save(out / 'publication-receipt.json', {'published': False,
                 'reason': 'README changed during publication.', 'rules_diff': difference.stdout})
            return 3
        result = git('push', 'origin', 'HEAD:main', check=False)
        if result.returncode == 0:
            commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=REPO, text=True).strip()
            save(out / 'publication-receipt.json', {'published': True, 'commit': commit,
                 'repository_path': str(relative)})
            return 0
        if '[rejected]' not in result.stdout or not any(x in result.stdout for x in ['fetch first', 'non-fast-forward']):
            save(out / 'publication-receipt.json', {'published': False, 'reason': result.stdout})
            return result.returncode

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=['prepare', 'run', 'publish', 'verify'])
    parser.add_argument('--result', required=True)
    parser.add_argument('--budget-minutes', type=int, default=320)
    args = parser.parse_args()
    request = read(REQUEST)
    item = next(x for x in request['jobs'] if x['result'] == args.result)
    base = Path(os.environ['RUNNER_TEMP']) / 'serre-p41-public' / args.result
    work, out = base / 'work', base / 'output'
    if args.mode == 'prepare':
        prepare(item, work, out)
        return 0
    if args.mode == 'run':
        return run(item, work, out, args.budget_minutes)
    if args.mode == 'publish':
        return publish(item, out)
    receipt = read(out / 'run-receipt.json')
    return 0 if receipt['complete'] else 1

if __name__ == '__main__':
    sys.exit(main())
