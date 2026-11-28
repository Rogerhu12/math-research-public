#!/usr/bin/env python3
"""Same-runner research worker; terminal-git publication of scalar records only.

The worker owns one unique per-run result path.  Numerical children receive no
credential variables.  Every pull checks both rule files.  A changed rule pauses
the owned process group until the root coordinator records a reviewed commit;
the actual arrays remain in the same runner.  No artifact or Release is created.
"""
import argparse
import base64
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import re
import signal
import subprocess
import sys
import time

TOPIC = 'topics/visible-flex-held-10pct'
RULES = ['README.md', TOPIC+'/README.md']
LIMIT = 64*1024
FORBIDDEN = {'x', 'y', 'c', 'matrix', 'matrices', 'jacobian', 'jacobians', 'mesh',
             'cubic_c', 'cubic_x', 'coefficients', 'field', 'fields', 'raw_array',
             'arrays', 'data', 'pp_coefficients'}
VOLATILE = {'elapsed_seconds', 'elapsed', 'timestamp', 'utc', 'updated_at',
            'runtime_seconds', 'wall_seconds'}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def encoded(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()


def compact(value, depth=0):
    if depth > 9:
        return '[omitted: nesting]'
    if isinstance(value, float) and not math.isfinite(value):
        return {'nonfinite_float':repr(value)}
    if value is None or isinstance(value, (bool, int, float)):
        return value
    if isinstance(value, str):
        return value[:3000]
    if isinstance(value, list):
        if len(value) > 64 or any(isinstance(item, list) for item in value):
            return '[omitted: array]'
        return [compact(item, depth+1) for item in value]
    if isinstance(value, dict):
        return {str(key):compact(item, depth+1) for key,item in value.items()
                if key not in FORBIDDEN and key not in VOLATILE}
    return '[omitted: type]'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--workdir', type=Path, required=True)
    parser.add_argument('--request', type=Path, required=True)
    parser.add_argument('--reviewed-rules-commit', required=True)
    parser.add_argument('--worker-minutes', type=float, default=330.)
    args = parser.parse_args()
    repo, work, request_path = (p.resolve() for p in (args.repo, args.workdir, args.request))
    if repo == work or repo in work.parents or repo not in request_path.parents:
        raise ValueError('Work must be outside Git and the reviewed request inside the repository')
    if not re.fullmatch('[0-9a-f]{40}', args.reviewed_rules_commit):
        raise ValueError('The dispatch must supply the actually reviewed full rules commit')
    if not 1 <= args.worker_minutes <= 338:
        raise ValueError('The worker must leave time for actual terminal publication before the job limit')
    run_id = os.environ.get('GITHUB_RUN_ID', '')
    run_attempt = os.environ.get('GITHUB_RUN_ATTEMPT', '1')
    if not run_id.isdigit() or not run_attempt.isdigit():
        raise ValueError('A real Actions run/attempt identity is required')
    token = os.environ['GITHUB_TOKEN']
    auth_value = base64.b64encode(('x-access-token:'+token).encode()).decode()
    auth = 'AUTHORIZATION: basic '+auth_value
    worker_source_hash = sha(__file__)
    clean_env = {key:value for key,value in os.environ.items()
                 if not any(word in key.upper() for word in ('TOKEN', 'SECRET', 'PASSWORD'))}
    clean_env['GIT_TERMINAL_PROMPT'] = '0'
    for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
        clean_env[key] = '2'
    work.mkdir(parents=True, exist_ok=True)
    result_rel = TOPIC+'/ci/mapped-design-results/run-'+run_id+'-attempt-'+run_attempt+'.json'
    result_path = repo/result_rel
    result_path.parent.mkdir(parents=True, exist_ok=True)
    state_file = work/'terminal-worker-state.json'
    if state_file.exists():
        state = json.loads(state_file.read_text())
    else:
        state = dict(seen={}, published_digest=None)
    state.update(run_id=run_id, run_attempt=run_attempt,
                 worker_source_sha256=worker_source_hash, result_path=result_rel)
    active = output = request = None
    paused = False
    rule_difference = ''
    last_pull = -1e30
    began = time.monotonic()
    payload = dict(status='worker_ready', arrays_uploaded=False, complete_surface=False)

    def save():
        temporary = state_file.with_suffix('.tmp')
        temporary.write_bytes(encoded(state)+b'\n')
        temporary.replace(state_file)

    def git(*arguments, authenticated=False, check=True):
        command = ['git', '-C', str(repo), '-c', 'credential.helper=',
                   '-c', 'user.name=held10-actions',
                   '-c', 'user.email=held10-actions@users.noreply.github.com']
        if authenticated:
            command += ['-c', 'http.https://github.com/.extraheader='+auth]
        command += list(arguments)
        result = subprocess.run(command, env=clean_env, text=True,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode and check:
            error = result.stderr.replace(token, '[redacted]').replace(auth, '[redacted]').replace(auth_value, '[redacted]')
            raise RuntimeError('terminal git '+str(arguments[0])+' failed: '+error[-2500:])
        return result

    def pause_owned_group():
        nonlocal paused
        if active is not None and active.poll() is None and not paused:
            os.killpg(active.pid, signal.SIGSTOP)
            paused = True

    def rules_diff(reviewed):
        if not re.fullmatch('[0-9a-f]{40}', reviewed):
            raise ValueError('The reviewed rule anchor must be a full actual commit')
        if git('cat-file', '-e', reviewed+'^{commit}', check=False).returncode:
            git('fetch', '--depth=1', '--filter=blob:none', '--no-tags', 'origin', reviewed)
        return git('diff', reviewed, 'HEAD', '--', *RULES).stdout

    def pull():
        nonlocal last_pull, rule_difference
        before = git('rev-parse', 'HEAD').stdout.strip()
        # This is the immediate action after every rejected push as well as the
        # regular <=3500-second rule check.  No force push is ever used.
        git('pull', '--rebase', 'origin', 'main')
        after = git('rev-parse', 'HEAD').stdout.strip()
        changed = git('diff', before, after, '--', *RULES).stdout
        last_pull = time.monotonic()
        reviewed = (request or {}).get('read_rules_commit') or args.reviewed_rules_commit
        rule_difference = rules_diff(reviewed)
        state['last_rules_check'] = dict(before=before, pulled_commit=after,
            reviewed_commit=reviewed, pull_rule_diff_sha256=hashlib.sha256(changed.encode()).hexdigest(),
            reviewed_rule_diff_sha256=hashlib.sha256(rule_difference.encode()).hexdigest(),
            rules_unchanged=(not rule_difference))
        save()
        if rule_difference:
            pause_owned_group()
        print(json.dumps(dict(event='actual_pull_and_rules_check',
            **state['last_rules_check'], changed_rules=changed[:12000])), flush=True)

    def substitute(value):
        if not isinstance(value, str) or '\0' in value or '\n' in value:
            raise ValueError('Command arguments must be single-line strings')
        value = value.replace('@REPO@', str(repo)).replace('@WORK@', str(work))
        candidate = value.split('=', 1)[-1] if value.startswith('--') else value
        if '..' in Path(candidate).parts:
            raise ValueError('Parent path components are not accepted')
        if candidate.startswith('/'):
            path = Path(candidate).resolve()
            topic = (repo/TOPIC).resolve()
            if not (path in (repo, work, topic) or work in path.parents or topic in path.parents):
                raise ValueError('Command argument leaves the declared task directories')
        return value

    def load_request():
        if request_path.stat().st_size > LIMIT:
            raise ValueError('Reviewed request exceeds 64 KiB')
        obj = json.loads(request_path.read_text())
        if not re.fullmatch('[A-Za-z0-9_.-]{1,96}', obj.get('id', '')):
            raise ValueError('Invalid reviewed request identity')
        script = (repo/obj['script']).resolve()
        if ((repo/TOPIC/'scripts').resolve() not in script.parents
                or script.suffix != '.py' or not script.is_file()):
            raise ValueError('Only an existing held10 Python source may execute')
        obj['resolved_script'] = str(script)
        obj['resolved_args'] = [substitute(value) for value in obj.get('args', [])]
        obj['read_rules_commit'] = obj.get('read_rules_commit') or args.reviewed_rules_commit
        if not re.fullmatch('[0-9a-f]{40}', obj['read_rules_commit']):
            raise ValueError('The request has no reviewed full rules commit')
        diagnostic_projection(obj)
        return obj

    def diagnostic_projection(obj):
        result = {}
        for item in obj.get('diagnostics', [])[:8]:
            path = Path(substitute(item['path'])).resolve()
            if work not in path.parents or path.suffix != '.json':
                raise ValueError('Diagnostics must be JSON under this runner work directory')
            if not path.is_file():
                continue
            if path.stat().st_size > 1024*1024:
                result[str(path.relative_to(work))] = {'omitted':'Input exceeds 1 MiB'}
                continue
            try:
                value = json.loads(path.read_text())
            except (OSError, ValueError):
                continue
            if not isinstance(value, dict):
                raise ValueError('Diagnostic root must be a scalar record object')
            keys = item.get('keys')
            if keys is not None:
                if not isinstance(keys, list) or len(keys) > 64 or any(k in FORBIDDEN for k in keys):
                    raise ValueError('Invalid diagnostic field projection')
                value = {key:value[key] for key in keys if key in value}
            result[str(path.relative_to(work))] = compact(value)
        return result

    def publish(force=False):
        nonlocal payload
        semantic = dict(payload, diagnostics=diagnostic_projection(request) if request else {},
            rules_paused=paused, arrays_uploaded=False, complete_surface=False,
            run_id=run_id, run_attempt=run_attempt, worker_source_sha256=worker_source_hash)
        if rule_difference:
            semantic['rules_diff'] = rule_difference[:12000]
            semantic['rules_diff_sha256'] = hashlib.sha256(rule_difference.encode()).hexdigest()
        digest = hashlib.sha256(encoded(semantic)).hexdigest()
        if not force and digest == state.get('published_digest'):
            return
        document = dict(semantic, schema='held10-terminal-mapped-design-v1',
            last_rules_check=state.get('last_rules_check'),
            published_utc=datetime.now(timezone.utc).isoformat())
        data = encoded(document)+b'\n'
        if len(data) > LIMIT:
            # A bounded error is honest; never replace it with an array upload.
            document['diagnostics'] = {'projection_error':'Actual scalar record exceeded 64 KiB'}
            data = encoded(document)+b'\n'
        if len(data) > LIMIT:
            raise ValueError('The worker scalar result exceeds 64 KiB')
        result_path.write_bytes(data)
        git('add', '--', result_rel)
        if git('diff', '--cached', '--quiet', '--', result_rel, check=False).returncode:
            git('commit', '-m', 'held10: actual mapped design '+str(payload.get('status', 'state')),
                '--', result_rel)
        while True:
            pushed = git('push', 'origin', 'HEAD:main', authenticated=True, check=False)
            if pushed.returncode == 0:
                break
            # Required immediate pull/rebase and fresh rule inspection.  This
            # loop has no fixed retry count and never rewrites remote history.
            pull()
            message = pushed.stderr.lower()
            if any(term in message for term in ('authentication failed', 'permission denied',
                    'write access to repository not granted', 'http 403', 'http 401')):
                raise RuntimeError('Terminal git authentication/permission failure after the required pull')
        state['published_digest'] = digest
        state['last_published_result_sha256'] = hashlib.sha256(data).hexdigest()
        save()
        print(json.dumps(dict(event='terminal_git_result_published', result=result_rel,
            sha256=state['last_published_result_sha256'], status=payload.get('status'))), flush=True)

    def stop_owned_group():
        nonlocal paused
        if active is None or active.poll() is not None:
            return
        if paused:
            os.killpg(active.pid, signal.SIGCONT)
            paused = False
        os.killpg(active.pid, signal.SIGTERM)
        try:
            active.wait(timeout=25)
        except subprocess.TimeoutExpired:
            os.killpg(active.pid, signal.SIGKILL)
            active.wait()

    try:
        pull()
        request = load_request()
        rule_difference = rules_diff(request['read_rules_commit'])
        publish()
        while True:
            now = time.monotonic()
            if now-began >= 60*args.worker_minutes:
                stop_owned_group()
                payload = dict(payload, status='worker_job_budget_reached',
                    returncode=active.returncode if active else None,
                    mathematical_failure_inferred=False)
                publish(force=True)
                return 0
            if now-last_pull >= 3500 or paused:
                pull()
            # Read the checked-out request after a real pull, never a detached
            # API value.  The root coordinator may update a review or the next
            # command while this worker preserves the existing actual fields.
            incoming = load_request()
            if active is not None:
                if active.poll() is not None:
                    if output is not None:
                        output.close()
                    code = active.returncode
                    state['seen'][request['id']] = dict(status='finished', returncode=code)
                    payload = dict(payload, status='finished', returncode=code)
                    save()
                    active = None
                    paused = False
                    publish(force=True)
                elif (incoming['id'] == request['id']
                        and incoming['resolved_script'] == request['resolved_script']
                        and incoming['resolved_args'] == request['resolved_args']):
                    request = incoming
                    rule_difference = rules_diff(request['read_rules_commit'])
                    if rule_difference:
                        pause_owned_group()
                        payload = dict(payload, status='rules_changed_actual_group_paused')
                    elif paused:
                        os.killpg(active.pid, signal.SIGCONT)
                        paused = False
                        payload = dict(payload, status='running_after_reviewed_rules_update',
                            reviewed_rules_commit=request['read_rules_commit'])
                    publish()
                else:
                    publish()
            elif incoming['id'] not in state['seen']:
                request = incoming
                pull()
                request = load_request()
                rule_difference = rules_diff(request['read_rules_commit'])
                if rule_difference:
                    payload = dict(status='rules_changed_before_launch', id=request['id'])
                    publish()
                else:
                    command = [sys.executable, '-u', request['resolved_script'], *request['resolved_args']]
                    state['seen'][request['id']] = dict(status='started',
                        commit=git('rev-parse', 'HEAD').stdout.strip(),
                        script_sha256=sha(request['resolved_script']))
                    save()
                    output = (work/('live-'+request['id']+'.log')).open('xb')
                    active = subprocess.Popen(command, cwd=repo, env=clean_env, stdout=output,
                        stderr=subprocess.STDOUT, start_new_session=True)
                    payload = dict(status='running', id=request['id'], command=command,
                        script_sha256=sha(request['resolved_script']),
                        actual_process_id=active.pid,
                        reviewed_rules_commit=request['read_rules_commit'])
                    publish(force=True)
            # A request may change while numerical work is active.  A cheap
            # read-only fetch is not substituted for the required true pull;
            # pull every 15 seconds also lets rule acknowledgements arrive.
            time.sleep(15)
            pull()
    except BaseException as exc:
        stop_owned_group()
        if output is not None and not output.closed:
            output.close()
        payload = dict(payload, status='worker_error',
            error=(type(exc).__name__+': '+str(exc)).replace(token, '[redacted]').replace(auth, '[redacted]').replace(auth_value, '[redacted]'))
        try:
            publish(force=True)
        except Exception:
            pass
        raise
    finally:
        stop_owned_group()
        if output is not None and not output.closed:
            output.close()


if __name__ == '__main__':
    sys.exit(main())
