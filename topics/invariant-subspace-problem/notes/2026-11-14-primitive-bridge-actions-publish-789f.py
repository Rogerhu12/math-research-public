"""Publish only this run's bounded outputs; the token stays in process memory.

Every pull is followed by both README fingerprint comparisons. Rule changes
leave the calculation in Actions artifacts for the active research session.
"""

import base64
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
from datetime import datetime, timezone


NOTES = Path('topics/invariant-subspace-problem/notes')
spec = importlib.util.spec_from_file_location(
    'primitive_bridge_supervisor', NOTES/'2026-11-14-primitive-bridge-actions-runner-789f.py')
supervisor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(supervisor)


def utc():
    return datetime.now(timezone.utc).isoformat()


def concurrent_rejection(stderr):
    return any(marker in stderr.lower() for marker in (
        'non-fast-forward', 'fetch first', '[rejected]', 'cannot lock ref',
        'remote rejected] main (failed to update ref'))


def main():
    target, run, attempt, source = supervisor.context()
    destination = NOTES/'primitive-bridge-actions-789f'/(run+'-'+attempt)/target
    report = {'target': target, 'run_id': run, 'run_attempt': attempt,
              'destination': destination.as_posix(), 'started_at_utc': utc(),
              'status': 'starting', 'sync_checks': []}
    def save_report():
        supervisor.write_json(source/'publication.json', report)

    save_report()
    provenance_path = source/'provenance.json'
    if not provenance_path.exists():
        report.update(status='artifact_only_no_provenance', finished_at_utc=utc())
        save_report()
        return 1
    provenance = json.loads(provenance_path.read_text())
    if (provenance.get('target') != target or provenance.get('run_id') != run
            or provenance.get('run_attempt') != attempt
            or os.environ.get('GITHUB_REPOSITORY', '').casefold() != 'rogerhu12/math-research-public'):
        report.update(status='artifact_only_context_mismatch', finished_at_utc=utc())
        save_report()
        return 1

    token = os.environ.pop('ISP_BRIDGE_ACTIONS_TOKEN')
    encoded = base64.b64encode(('x-access-token:'+token).encode()).decode()
    auth_header = 'Authorization: Basic '+encoded
    environment = os.environ.copy()
    for key in ('GIT_TRACE', 'GIT_TRACE_CURL', 'GIT_CURL_VERBOSE'):
        environment.pop(key, None)
    environment.update(
        GIT_TERMINAL_PROMPT='0', GIT_CONFIG_COUNT='2',
        GIT_CONFIG_KEY_0='http.https://github.com/.extraheader',
        GIT_CONFIG_VALUE_0=auth_header,
        GIT_CONFIG_KEY_1='credential.helper', GIT_CONFIG_VALUE_1='')

    def redact(text):
        for secret in (auth_header, encoded, token):
            text = text.replace(secret, '[REDACTED]')
        return text

    def git(*arguments):
        completed = subprocess.run(['git', *arguments], env=environment,
                                   capture_output=True, text=True, errors='replace', timeout=180)
        completed.stdout, completed.stderr = redact(completed.stdout), redact(completed.stderr)
        for value in (completed.stdout, completed.stderr):
            if value.strip():
                print(value.rstrip(), flush=True)
        return completed

    def remote_rules():
        tip = git('rev-parse', 'origin/main')
        if tip.returncode:
            raise RuntimeError('Cannot identify origin/main after pull')
        current = {}
        for name in supervisor.RULES:
            content = subprocess.run(['git', 'show', 'origin/main:'+name], env=environment,
                                     capture_output=True, timeout=60)
            if content.returncode:
                raise RuntimeError('Cannot read a required remote README after pull')
            current[name] = hashlib.sha256(content.stdout).hexdigest()
        return tip.stdout.strip(), current

    try:
        remote = git('remote', 'get-url', 'origin')
        expected = 'https://github.com/rogerhu12/math-research-public'
        address = remote.stdout.strip().rstrip('/')
        if address.endswith('.git'):
            address = address[:-4]
        if remote.returncode or address.casefold() != expected:
            raise RuntimeError('Origin is not the authorized public repository')
        for key, value in (
                ('user.name', 'github-actions[bot]'),
                ('user.email', '41898282+github-actions[bot]@users.noreply.github.com')):
            if git('config', key, value).returncode:
                raise RuntimeError('Cannot configure the non-secret commit author')

        while True:
            pull = git('pull', '--rebase', 'origin', 'main')
            tip, current = remote_rules()
            unchanged = current == provenance['readme_sha256']
            report['sync_checks'].append({'utc': utc(), 'origin_main': tip,
                                           'pull_exit_code': pull.returncode,
                                           'readme_sha256': current,
                                           'unchanged_readmes': unchanged})
            if not unchanged:
                report.update(status='artifact_only_readme_drift', finished_at_utc=utc(),
                              source_readme_sha256=provenance['readme_sha256'],
                              source_commit=provenance['source_commit'],
                              instruction='The active session must read the README diff and apply the new rules.')
                save_report()
                print('README fingerprints changed; output remains in Actions artifacts.', flush=True)
                return 0
            if pull.returncode:
                report.update(status='artifact_only_rebase_failed', finished_at_utc=utc(),
                              error=pull.stderr[-4000:])
                save_report()
                return 1

            report.update(status='ready_to_push', publication_attempt=len(report['sync_checks']))
            save_report()
            supervisor.bounded_files(source)
            destination.mkdir(parents=True, exist_ok=True)
            for path in source.iterdir():
                if not path.is_file() or path.is_symlink():
                    continue
                size = path.stat().st_size
                if size > 5_000_000 or (size > 1_000_000 and path.suffix != '.gz'):
                    raise RuntimeError('Output was not normalized to the repository size rules')
                shutil.copyfile(path, destination/path.name)
            if git('add', '--', destination.as_posix()).returncode:
                raise RuntimeError('Cannot stage this run directory')
            staged = git('diff', '--cached', '--name-only')
            if staged.returncode:
                raise RuntimeError('Cannot inspect the staged output paths')
            names = staged.stdout.splitlines()
            if any(not name.startswith(destination.as_posix()+'/') for name in names):
                raise RuntimeError('Refusing to commit any path outside this run directory')
            if names:
                commit = git('commit', '-m',
                             f'isp: preserve primitive bridge {run}-{attempt} {target} output')
                if commit.returncode:
                    raise RuntimeError('Cannot commit this run output')
            pushed = git('push', 'origin', 'HEAD:main')
            if pushed.returncode == 0:
                tip = git('rev-parse', 'HEAD')
                report.update(status='published', published_commit=tip.stdout.strip(),
                              finished_at_utc=utc())
                save_report()
                print(json.dumps({'publication': 'published', 'target': target,
                                  'destination': destination.as_posix(),
                                  'commit': report['published_commit']}), flush=True)
                return 0
            report.update(last_push_exit_code=pushed.returncode, last_push_error=pushed.stderr[-4000:])
            save_report()
            if not concurrent_rejection(pushed.stderr):
                report.update(status='artifact_only_push_failed', finished_at_utc=utc())
                save_report()
                return 1
            # A rejected concurrent update immediately returns to pull --rebase.
            # No force push and no amendment of an already-published commit.
    except BaseException as exc:
        report.update(status='artifact_only_publisher_error', finished_at_utc=utc(),
                      error=redact(type(exc).__name__+': '+str(exc))[:4000])
        save_report()
        print(report['error'], flush=True)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
