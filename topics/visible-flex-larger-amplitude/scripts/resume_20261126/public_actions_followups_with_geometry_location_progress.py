#!/usr/bin/env python3
"""Keep actual research arrays alive for explicitly queued same-job followups.

Imported by the public Actions controller. This module contains no scientific
solver. Queue scripts run as argv, in one new detached sparse source worktree
per unique step id, without GitHub credential environment variables.

Queue format:
  {"parent_request_id": "...", "finish_when_done": false, "steps": [
    {"id": "unique-id", "script": "topics/visible-flex-larger-amplitude/scripts/x.py",
     "args": ["--repo", "{repo}", "--bundle", "{work}/input.npz"],
     "parent_bundle": "input.npz", "outputs": ["result.json", "result.npz"],
     "summary": {"result.json": {"Phi": "final.phi_normalized"}},
     "cleanup_generated_patterns": ["output/inequality-rows-*"]} ]}

{repo} is the step's pinned source worktree; {work} is the existing runwork.
Only these literal substitutions occur. Summary paths are relative to runwork;
each value may be a list of dot-paths or a scalar-label -> dot-path mapping.
Budget exhaustion stops admission, then observes an active child to its natural
return. It is a job checkpoint, never a research-completion declaration.
Optional active progress is bounded, read-only scalar metadata. It never changes
scientific commands, inputs, budgets, completed-step status or admission order.
"""
import copy
import datetime
import glob
import hashlib
import json
import math
import os
from pathlib import Path, PurePosixPath
import shutil
import signal
import subprocess
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


TOPIC = 'topics/visible-flex-larger-amplitude'
REPOSITORY = 'Rogerhu12/math-research-public'
POLL_SECONDS = 35.
RULE_SECONDS = 3000.
PROGRESS_POLL_SECONDS = 300.
PROGRESS_MAX_FILE_BYTES = 95000
PROGRESS_MAX_PUBLIC_BYTES = 16384
TOKEN_NAMES = ('GITHUB_TOKEN', 'GH_TOKEN', 'TASK_GITHUB_TOKEN')


def _sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


MODULE_SHA = _sha(__file__)


def _utc():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def _event(kind, **data):
    print(json.dumps(dict(event=kind, **data), ensure_ascii=False), flush=True)


def _write(path, value):
    temporary = path.with_name(path.name + '.tmp')
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + '\n')
    temporary.replace(path)


def _relative(value):
    if not isinstance(value, str) or not value:
        raise ValueError('A nonempty relative path is required')
    path = PurePosixPath(value)
    if path.is_absolute() or '..' in path.parts or '\\' in value:
        raise ValueError('Path must stay inside its declared directory: ' + value)
    return path


def _work_path(value, runwork):
    value = value.replace('{work}', str(runwork))
    path = Path(value)
    if not path.is_absolute():
        path = runwork / _relative(value)
    path = path.resolve()
    if path == runwork or runwork not in path.parents:
        raise ValueError('File must stay inside runwork: ' + value)
    return path


def _validate_queue(queue, request_id):
    if not isinstance(queue, dict) or queue.get('parent_request_id') != request_id:
        raise ValueError('followup parent_request_id does not match the active request')
    steps = queue.get('steps', [])
    if not isinstance(steps, list):
        raise ValueError('steps must be a list')
    if not isinstance(queue.get('finish_when_done', False), bool):
        raise ValueError('finish_when_done must be a JSON boolean')
    seen = set()
    for step in steps:
        if not isinstance(step, dict) or not isinstance(step.get('id'), str) or not step['id']:
            raise ValueError('Each step needs a nonempty unique string id')
        if step['id'] in seen:
            raise ValueError('Duplicate step id in queue: ' + step['id'])
        seen.add(step['id'])
        script = str(_relative(step.get('script')))
        if not script.startswith(TOPIC + '/') or not script.endswith('.py'):
            raise ValueError('Step script must be a Python file inside the declared topic')
        for key in ('args', 'outputs', 'cleanup_generated_patterns'):
            if not isinstance(step.get(key, []), list) or any(not isinstance(v, str) for v in step.get(key, [])):
                raise ValueError(key + ' must be a list of strings')
        for value in step.get('outputs', []):
            _relative(value)
        for value in step.get('cleanup_generated_patterns', []):
            _relative(value)
        if step.get('parent_bundle') is not None and not isinstance(step['parent_bundle'], str):
            raise ValueError('parent_bundle must be a path string')
        if not isinstance(step.get('summary', {}), dict):
            raise ValueError('summary must map JSON report paths to scalar dot-paths')
        progress = step.get('progress_summary', {})
        if not isinstance(progress, dict) or len(progress) > 4:
            raise ValueError('Optional progress must name at most four small metadata files')
        selector_count = 0
        for relative, fields in progress.items():
            _relative(relative)
            if not isinstance(fields, dict):
                raise ValueError('Optional progress fields must be a complete scalar label mapping')
            selector_count += len(fields)
            if any(not isinstance(k, str) or not isinstance(v, str) or not k or not v
                   or len(k) > 256 or len(v) > 256 for k, v in fields.items()):
                raise ValueError('Optional progress labels and dot-paths must be short complete strings')
        if selector_count > 64:
            raise ValueError('Optional progress is limited to 64 explicit scalar fields')
    return queue


def _summary(specification, runwork):
    metrics, errors, sources = {}, [], []
    for relative, fields in specification.items():
        try:
            path = _work_path(relative, runwork)
            data = json.loads(path.read_text())
            sources.append(dict(role='summary_report', path=str(path), sha256=_sha(path)))
            fields = {name: name for name in fields} if isinstance(fields, list) else fields
            if not isinstance(fields, dict):
                raise ValueError('Expected a list or mapping of scalar dot-paths')
            values = {}
            for label, dotted in fields.items():
                try:
                    value = data
                    for part in dotted.split('.'):
                        value = value[int(part)] if isinstance(value, list) else value[part]
                    if not isinstance(value, (str, int, float, bool, type(None))):
                        raise ValueError('Requested summary is not scalar')
                    if isinstance(value, float) and not math.isfinite(value):
                        value = str(value)
                    values[label] = value
                except (KeyError, IndexError, TypeError, ValueError, AttributeError) as error:
                    errors.append(dict(report=relative, field=str(dotted), error=str(error)))
            metrics[relative] = values
        except (OSError, ValueError, TypeError) as error:
            errors.append(dict(report=relative, error=str(error)))
    return metrics, errors, sources


def _matches(patterns, runwork):
    result = set()
    for pattern in patterns:
        for name in glob.glob(str(runwork / str(_relative(pattern))), recursive=True):
            path = Path(name)
            resolved = path.resolve()
            if resolved != runwork and runwork in resolved.parents:
                result.add(path.absolute())
    return result


def _cleanup(patterns, runwork, existed, protected):
    """Remove only explicitly matched newly generated caches, after exit.

    Preexisting matches, symlinks, inputs and declared outputs are retained.
    A newly created inequality-rows-* directory can contain its regular .f64
    array. Every member is checked before that explicitly requested tree is
    removed; no general work-directory cleanup is performed.
    """
    deleted, skipped = [], []
    for path in sorted(_matches(patterns, runwork), key=str):
        reason = None
        members = []
        if path in existed:
            reason = 'existed_before_child'
        elif any(node.is_symlink() for node in (path, *path.parents)
                 if node != runwork and runwork in node.parents):
            reason = 'symlink_or_symlink_parent'
        elif any(path.resolve() == p or path.resolve() in p.parents or p in path.resolve().parents for p in protected):
            reason = 'protected_input_or_output'
        elif path.is_dir():
            members = list(path.rglob('*'))
            if any(item.is_symlink() or not (item.is_file() or item.is_dir()) for item in members):
                reason = 'cache_tree_contains_nonregular_member'
        elif not path.is_file():
            reason = 'not_a_generated_regular_cache'
        if reason:
            skipped.append(dict(path=str(path), reason=reason))
            continue
        try:
            if path.is_dir():
                files = [item for item in members if item.is_file()]
                size = sum(item.stat().st_size for item in files)
                names = [str(item) for item in files]
                shutil.rmtree(path)
                deleted.append(dict(path=str(path), bytes=size, files=names))
            else:
                size = path.stat().st_size
                path.unlink()
                deleted.append(dict(path=str(path), bytes=size))
        except OSError as error:
            skipped.append(dict(path=str(path), reason='cleanup_error', error=str(error)))
    return dict(deleted=deleted, skipped=skipped,
        scope='Only explicit patterns, newly generated regular caches and an already returned child; never parent/input/output files')


class _Followups:
    def __init__(self, repo, work, runwork, publisher, status, request, started):
        self.repo, self.work, self.runwork = Path(repo).resolve(), Path(work).resolve(), Path(runwork).resolve()
        self.publisher, self.status, self.request = publisher, status, request
        self.deadline = started + float(request.get('controller_budget_seconds', 20000))
        self.file = str(_relative(request['followup_file']))
        self.token = os.environ.get('GITHUB_TOKEN')
        if not self.token:
            raise RuntimeError('The controller needs GITHUB_TOKEN for its followup metadata polling')
        self.journal = status.setdefault('followups', dict(attempted_ids=[], records=[]))
        self.journal['module_sha256'] = MODULE_SHA
        self.attempted = set(self.journal.get('attempted_ids', []))
        self.queue, self.queue_info, self.child, self.active = None, None, None, None
        self.last_poll, self.last_poll_error = 0., None
        self.last_api_commit = None
        self.last_progress_poll = 0.
        self.last_progress_identity = None
        self.logs = self.runwork / 'followup-logs'
        self.sources = self.work / 'followup-sources'
        self.logs.mkdir(parents=True, exist_ok=True)
        self.sources.mkdir(parents=True, exist_ok=True)

    def save(self):
        self.journal['updated_utc'] = _utc()
        _write(self.runwork / 'status.json', self.status)
        _write(self.runwork / 'followup-journal.json', self.journal)

    def publish(self, code=None, force=False):
        self.save()
        self.publisher.publish(self.status, exit_code=code, force=force)

    def poll(self):
        now = time.monotonic()
        if now - self.last_poll < POLL_SECONDS:
            return
        self.last_poll = now
        query = urlencode(dict(sha='main', path=self.file, per_page=1))
        url = f'https://api.github.com/repos/{REPOSITORY}/commits?{query}'
        headers = {'Accept': 'application/vnd.github+json',
            'Authorization': 'Bearer ' + self.token, 'X-GitHub-Api-Version': '2022-11-28',
            'User-Agent': 'visible-flex-public-actions-controller'}
        try:
            with urlopen(Request(url, headers=headers), timeout=20) as response:
                raw = response.read(95001)
            if len(raw) > 95000:
                raise ValueError('Unexpectedly large commit metadata response')
            commits = json.loads(raw)
            commit = commits[0]['sha'] if commits else None
            self.last_poll_error = None
        except (HTTPError, URLError, OSError, ValueError, KeyError, TypeError) as error:
            description = type(error).__name__ + ': ' + str(error)
            self.journal['last_poll_error'] = description
            if description != self.last_poll_error:
                _event('followup_poll_deferred', error=description)
            self.last_poll_error = description
            self.save()
            return
        if commit is None or commit == self.last_api_commit:
            return
        # Publisher.publish calls its real pull/rebase + both-README check and
        # writes the read rule commit to HANDOFF. No polling pull occurs when
        # the path-specific API commit has not changed.
        self.publish(force=True)
        self.last_api_commit = commit
        path = self.repo / self.file
        self.queue = None
        if not path.exists():
            self.journal['queue_missing_at_commit'] = commit
            self.save()
            return
        try:
            if path.is_symlink() or path.stat().st_size >= 95000:
                raise ValueError('Followup request must be a complete small repository JSON file')
            queue = _validate_queue(json.loads(path.read_text()), self.request['request_id'])
            self.queue_info = dict(path=self.file, path_commit=commit,
                checkout_commit=self.publisher.git('rev-parse', 'HEAD').stdout.strip(), sha256=_sha(path))
            self.queue = copy.deepcopy(queue)
            self.journal['queue'] = self.queue_info
            self.journal.pop('queue_error', None)
            if self.status.get('error', '').startswith('Followup queue:'):
                self.status.pop('error', None)
            _event('followup_queue_loaded', **self.queue_info, steps=len(queue.get('steps', [])),
                   finish_when_done=bool(queue.get('finish_when_done', False)))
            self.save()
        except (OSError, ValueError, TypeError) as error:
            self.journal['queue_error'] = dict(commit=commit, error=str(error))
            self.status['error'] = 'Followup queue: ' + str(error)
            _event('followup_queue_rejected', commit=commit, error=str(error))
            self.publish(force=True)


    def poll_active_progress(self):
        """Observe only explicitly requested small scalar progress files.

        A missing/changing/large file leaves an observation error, not a failed
        scientific step. Both bounded captures must agree. No full raw report,
        field array, root packet or per-location dataset is published.
        """
        if self.active is None or self.child is None or self.child.poll() is not None:
            return
        specification = self.active['requested_step'].get('progress_summary', {})
        if not specification or time.monotonic() - self.last_progress_poll < PROGRESS_POLL_SECONDS:
            return
        self.last_progress_poll = time.monotonic()
        metrics, errors, sources = {}, [], []
        for relative, fields in specification.items():
            try:
                path = _work_path(relative, self.runwork)
                before = path.stat().st_size
                if before >= PROGRESS_MAX_FILE_BYTES:
                    raise ValueError('Progress file exceeds its declared small-file bound')
                with path.open('rb') as handle:
                    raw = handle.read(PROGRESS_MAX_FILE_BYTES)
                if len(raw) != before or len(raw) >= PROGRESS_MAX_FILE_BYTES:
                    raise ValueError('Progress file changed or exceeded its bounded capture')
                with path.open('rb') as handle:
                    second = handle.read(PROGRESS_MAX_FILE_BYTES)
                if second != raw or path.stat().st_size != len(raw):
                    raise ValueError('Progress bytes changed between the two bounded captures')
                data = json.loads(raw)
                values = {}
                for label, dotted in fields.items():
                    try:
                        value = data
                        for part in dotted.split('.'):
                            value = value[int(part)] if isinstance(value, list) else value[part]
                        if not isinstance(value, (str, int, float, bool, type(None))):
                            raise ValueError('Requested progress field is not scalar')
                        if isinstance(value, float) and not math.isfinite(value):
                            raise ValueError('Requested progress field is not finite')
                        if isinstance(value, str) and len(value.encode('utf-8')) > 512:
                            raise ValueError('Requested progress string is too large for scalar metadata')
                        values[label] = value
                    except (KeyError, IndexError, TypeError, ValueError, AttributeError) as error:
                        errors.append(dict(report=relative, field=dotted,
                            error=type(error).__name__ + ': ' + str(error)))
                metrics[relative] = values
                sources.append(dict(path=relative, bytes=len(raw),
                    sha256=hashlib.sha256(raw).hexdigest(),
                    two_complete_bounded_reads_agreed=True))
            except (OSError, ValueError, TypeError) as error:
                errors.append(dict(report=relative,
                    error=type(error).__name__ + ': ' + str(error)))
        body = dict(step_id=self.active['step_id'],
            scientific_source_commit=self.active.get('source_commit'),
            scientific_source_sha256=self.active.get('source_sha256'),
            pid=self.active.get('pid'), observations=metrics,
            complete_small_progress_file_identities=sources, observation_errors=errors,
            child_exit_code=None, child_natural_return_not_observed=True,
            observations_are_not_a_completed_step_or_a_scientific_certificate=True)
        encoded = json.dumps(body, sort_keys=True, ensure_ascii=False,
            separators=(',', ':'), allow_nan=False).encode('utf-8')
        if len(encoded) >= PROGRESS_MAX_PUBLIC_BYTES:
            body = dict(step_id=self.active['step_id'],
                progress_metadata_not_published=True,
                reason='The complete optional scalar observation exceeds its public bound',
                original_complete_observation_bytes=len(encoded),
                original_complete_observation_sha256=hashlib.sha256(encoded).hexdigest(),
                child_exit_code=None, child_natural_return_not_observed=True,
                full_optional_progress_remains_in_runner_files=True)
            encoded = json.dumps(body, sort_keys=True, separators=(',', ':')).encode('utf-8')
        identity = hashlib.sha256(encoded).hexdigest()
        if identity == self.last_progress_identity:
            return
        self.last_progress_identity = identity
        observation = dict(body, observation_identity_sha256=identity, observed_utc=_utc())
        self.status['active_progress_observation'] = observation
        self.journal.setdefault('active_progress_observation_history', []).append(copy.deepcopy(observation))
        self.save()
        self.publish(force=True)

    def maintenance(self):
        self.poll()
        self.poll_active_progress()
        if time.monotonic() - self.publisher.last_pull >= RULE_SECONDS:
            self.publish(force=True)

    def begin(self, step):
        step_id = step['id']
        self.attempted.add(step_id)
        self.journal['attempted_ids'].append(step_id)
        self.status.pop('failed', None)
        self.status.pop('active_progress_observation', None)
        self.last_progress_poll = 0.
        self.last_progress_identity = None
        self.status.update(stage='followup:' + step_id, state='running')
        record = dict(name='followup:' + step_id, step_id=step_id, state='running',
            scope=step.get('scope', 'Explicit same-job scientific followup; no inherited certificate or research-completion claim'),
            followup_queue=copy.deepcopy(self.queue_info), requested_step=copy.deepcopy(step),
            started_utc=_utc(), module_sha256=MODULE_SHA, input_files=[], outputs=[])
        self.active = record
        self.journal['active'] = record
        self.save()
        started = time.monotonic()
        self.active_started = started
        tag = f'{len(self.journal["attempted_ids"]):04d}-' + hashlib.sha256(step_id.encode()).hexdigest()[:12]
        log_path = self.logs / (tag + '.log')
        record['log'] = str(log_path)
        try:
            commit = self.publisher.git('rev-parse', 'HEAD').stdout.strip()
            source = self.sources / (tag + '-' + commit[:12])
            self.publisher.git('worktree', 'add', '--no-checkout', '--detach', str(source), commit)
            subprocess.run(['git', 'sparse-checkout', 'set', '--cone', TOPIC], cwd=source, check=True,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            subprocess.run(['git', 'reset', '--hard', commit], cwd=source, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            script = (source / step['script']).resolve()
            if source / TOPIC not in script.parents or not script.is_file():
                raise ValueError('Pinned script is missing or escapes the topic')
            args = [value.replace('{repo}', str(source)).replace('{work}', str(self.runwork))
                    for value in step.get('args', [])]
            command = [sys.executable, '-u', str(script), *args]
            record.update(source_commit=commit, source_sha256=_sha(script), source_worktree=str(source), command=command)
            record['input_files'].append(dict(role='source', path=step['script'], commit=commit,
                sha256=record['source_sha256'], command=command))
            parent = _work_path(step['parent_bundle'], self.runwork) if step.get('parent_bundle') else None
            if parent:
                record.update(parent_bundle=str(parent), parent_sha256=_sha(parent))
                record['input_files'].append(dict(role='parent_bundle', path=str(parent), sha256=record['parent_sha256']))
            outputs = [_work_path(path, self.runwork) for path in step.get('outputs', [])]
            protected = set(outputs + ([_work_path(path, self.runwork) for path in step.get('summary', {})]))
            protected.update((log_path.resolve(), self.runwork / 'status.json',
                              self.runwork / 'followup-journal.json'))
            if parent:
                protected.add(parent)
            # Protect explicit preexisting path arguments too. The broad {work}
            # directory is not a deletion candidate; matching preexisting files
            # are independently protected by the before-child snapshot below.
            for value in args:
                candidate = value.split('=', 1)[-1] if value.startswith('--') and '=' in value else value
                path = Path(candidate)
                if path.is_absolute() and path.exists() and path.resolve() != self.runwork:
                    protected.add(path.resolve())
            patterns = step.get('cleanup_generated_patterns', [])
            existed = _matches(patterns, self.runwork)
            environment = {key: value for key, value in os.environ.items() if key not in TOKEN_NAMES}
            environment.update(OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1',
                NUMEXPR_NUM_THREADS='1', PYTHONDONTWRITEBYTECODE='1', PYTHONUNBUFFERED='1')
            output = log_path.open('w')
            try:
                self.child = subprocess.Popen(command, cwd=source, env=environment, stdout=output,
                    stderr=subprocess.STDOUT, start_new_session=True)
            finally:
                output.close()
            record['pid'] = self.child.pid
            self.save()
            _event('followup_started', step_id=step_id, source_commit=commit,
                   source_sha256=record['source_sha256'], parent_sha256=record.get('parent_sha256'), pid=self.child.pid)
            return started, outputs, patterns, existed, protected
        except (OSError, ValueError, subprocess.SubprocessError) as error:
            if self.child is not None:
                # A failure after Popen belongs to the controller exception
                # path; never abandon a live child as a setup-only failure.
                raise
            record.update(state='failed', returncode=None, seconds=time.monotonic() - started,
                          setup_error=str(error), metrics=dict(setup_error=str(error)),
                          scope='Followup setup failed; no scientific child result claimed')
            self.finish_record(record)
            return None

    def finish_record(self, record):
        if 'active_progress_observation' in self.status:
            record['last_active_progress_observation'] = self.status.pop('active_progress_observation')
        record['returned_utc'] = _utc()
        self.journal['records'].append(copy.deepcopy(record))
        self.journal.pop('active', None)
        self.status['completed'].append(copy.deepcopy(record))
        self.status.update(stage=record['name'], state=record['state'])
        if record['state'] == 'failed':
            self.status['failed'] = copy.deepcopy(record)
        self.active = None
        # Persist the complete result before either stdout or publication.
        self.save()
        _event('followup_returned', step_id=record['step_id'], state=record['state'],
            returncode=record.get('returncode'), seconds=record['seconds'],
            source_commit=record.get('source_commit'), source_sha256=record.get('source_sha256'),
            parent_sha256=record.get('parent_sha256'), outputs=record.get('outputs', []),
            metrics=record.get('metrics', {}))
        if record['state'] == 'failed' and Path(record['log']).is_file():
            # Bounded tail only. The scientific child never received the three
            # GitHub credential variables; the complete log remains in runwork.
            with Path(record['log']).open('rb') as stream:
                stream.seek(max(0, Path(record['log']).stat().st_size - 6000))
                tail = stream.read().decode(errors='replace')
            _event('followup_failed_log_tail', step_id=record['step_id'], text=tail)
        self.publisher.publish(self.status, exit_code=record.get('returncode'))
        # A result publication itself pulled main. Recheck the path-specific
        # request before admitting another id, rather than using a stale queue.
        self.last_poll = 0.

    def run_step(self, step):
        prepared = self.begin(step)
        if prepared is None:
            return
        started, outputs, patterns, existed, protected = prepared
        while self.child.poll() is None:
            self.maintenance()
            if time.monotonic() >= self.deadline and not self.journal.get('budget_reached'):
                self.journal.update(budget_reached=True, budget_scope='Admission closed; the active child is still observed until natural return')
                self.publish(force=True)
                _event('followup_budget_admission_closed', active_step=step['id'], pid=self.child.pid)
            time.sleep(5)
        code = self.child.returncode
        self.child = None
        record = self.active
        record.update(returncode=code, seconds=time.monotonic() - started, log_sha256=_sha(record['log']))
        missing = []
        for path in outputs:
            if path.is_file():
                record['outputs'].append(dict(path=str(path), sha256=_sha(path), bytes=path.stat().st_size))
            else:
                missing.append(str(path))
        metrics, errors, reports = _summary(step.get('summary', {}), self.runwork)
        record.update(metrics=metrics, summary_errors=errors, output_reports=reports,
            state='completed' if code == 0 and not missing else 'failed', missing_outputs=missing)
        record['input_files'].append(dict(role='followup_queue', **record['followup_queue']))
        record['cleanup_generated'] = _cleanup(patterns, self.runwork, existed, protected)
        self.finish_record(record)

    def checkpoint(self, reason):
        self.journal.update(stop_reason=reason, stopped_utc=_utc(), research_complete=False)
        self.status.update(stage='followup_' + reason,
            state='failed' if self.status.get('failed') else 'completed')
        self.publish(force=True)
        _event('followup_controller_checkpoint', reason=reason,
            actual_returned_steps=len(self.journal['records']), research_complete=False)
        return self.status

    def run(self):
        try:
            self.status.update(stage='followup_waiting', state='running')
            self.save()
            _event('followup_waiting', request_file=self.file,
                   budget_remaining_seconds=max(0., self.deadline-time.monotonic()))
            while True:
                if time.monotonic() >= self.deadline:
                    return self.checkpoint('budget_checkpoint')
                self.maintenance()
                if time.monotonic() >= self.deadline:
                    return self.checkpoint('budget_checkpoint')
                pending = [step for step in self.queue.get('steps', []) if step['id'] not in self.attempted] if self.queue else []
                if pending:
                    self.run_step(copy.deepcopy(pending[0]))
                    continue
                if self.queue and self.queue.get('finish_when_done', False):
                    return self.checkpoint('queue_finished')
                self.status.update(stage='followup_waiting', state='running')
                self.save()
                time.sleep(min(5., max(.1, self.deadline - time.monotonic())))
        except BaseException as error:
            # Only a genuine controller exception can interrupt a running group.
            # Normal budget exhaustion always takes the natural-return path.
            interrupted = False
            if self.child is not None and self.child.poll() is None:
                interrupted = True
                os.killpg(self.child.pid, signal.SIGINT)
                try:
                    self.child.wait(timeout=30)
                except subprocess.TimeoutExpired:
                    os.killpg(self.child.pid, signal.SIGTERM)
                    self.child.wait(timeout=30)
            if self.active:
                self.active.update(state='failed',
                    returncode=self.child.returncode if self.child is not None else self.active.get('returncode'),
                    seconds=time.monotonic()-self.active_started,
                    controller_exception=repr(error),
                    interrupted_for_controller_exception=interrupted,
                    scope='Actual controller exception; any recorded child exit remains literal, no successful scientific stage is inferred')
                self.journal['interrupted'] = copy.deepcopy(self.active)
                self.status['failed'] = copy.deepcopy(self.active)
            self.status.update(state='failed', error=repr(error))
            self.save()
            raise


def run_followups(repo, work, runwork, publisher, status, request, started_monotonic):
    """Observe queued followups in the same public Actions job; return status.

    Failure of one scientific step is retained and is never retried under that
    id. A later distinct id may repair it. A malformed or unrelated queue is
    recorded, not executed, and does not cancel an already running valid child.
    """
    if not request.get('followup_file'):
        return status
    if (os.environ.get('GITHUB_ACTIONS') != 'true' or
            os.environ.get('GITHUB_REPOSITORY') != REPOSITORY):
        raise RuntimeError('Followup scientific execution is restricted to the authorized public Actions repository')
    return _Followups(repo, work, runwork, publisher, status, request, started_monotonic).run()
