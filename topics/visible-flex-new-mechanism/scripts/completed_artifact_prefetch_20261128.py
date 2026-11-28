"""Administrative byte transport before any public scientific process starts.

Receive an immutable complete parent ZIP and optionally restore an exact naturally
finished checkpoint. No scientific imports, evaluations, changed coefficients, or
log requests occur here. Signed addresses and credentials are never persisted.
"""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import time
import urllib.error
import urllib.request
import zipfile

from r754_ranged_zip import REPO, NoRedirect, api, artifact_metadata, signed_url

CHUNK = 64 * 2**20
RESERVE = 2 * 2**30


def require(condition, message):
    if not condition:
        raise ValueError(message)


def plain(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def emit(value):
    print('COMPLETED_ARCHIVE_TRANSPORT ' + plain(value), flush=True)


def verified_metadata(spec):
    run_id, job_id = int(spec['run_id']), int(spec['job_id'])
    conclusion = spec.get('expected_conclusion', 'success')
    require(conclusion in ('success', 'failure'), 'only a pinned natural success or failure can be restored')
    with api('/actions/runs/' + str(run_id)) as f:
        run = json.load(f)
    with api('/actions/jobs/' + str(job_id)) as f:
        job = json.load(f)
    require(run['id'] == run_id and run['head_sha'] == spec['head_sha']
            and run['status'] == 'completed' and run['conclusion'] == conclusion,
            'the pinned original run is not naturally completed with its recorded conclusion')
    require(job['id'] == job_id and job['run_id'] == run_id and job['head_sha'] == spec['head_sha']
            and job['status'] == 'completed' and job['conclusion'] == conclusion
            and job.get('completed_at') == spec['naturally_completed_at'],
            'the pinned original job and natural completion receipt differ')
    provider = artifact_metadata(spec)
    return dict(**provider, job_id=job_id, conclusion=conclusion, completed_at=job['completed_at'])


def space(directory, needed):
    usage = shutil.disk_usage(directory)
    require(usage.free >= needed + RESERVE, 'insufficient measured disk space for original bytes and the 2 GiB reserve')
    return dict(free_bytes=usage.free, required_new_bytes=needed, reserve_bytes=RESERVE)


def receive(spec, destination):
    start = time.monotonic()
    provider = verified_metadata(spec)
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    require(not destination.exists(), 'do not replace an existing original parent archive')
    size = int(spec['artifact_bytes'])
    capacity = space(destination.parent, size)
    temporary = destination.with_name(destination.name + '.receiving')
    require(not temporary.exists(), 'ambiguous prior partial administrative download')
    sha = hashlib.sha256()
    offset = 0
    address = None
    tag = spec.get('strong_etag')
    count = 0
    renewals = 0
    with temporary.open('xb') as output:
        while offset < size:
            end = min(offset + CHUNK, size) - 1
            for attempt in range(4):
                if address is None:
                    address = signed_url(spec['artifact_id'])
                    renewals += 1
                headers = {'Range': f'bytes={offset}-{end}', 'Accept-Encoding': 'identity'}
                if tag is not None:
                    headers['If-Match'] = tag
                request = urllib.request.Request(address, headers=headers)
                try:
                    with urllib.request.build_opener(NoRedirect).open(request, timeout=60) as response:
                        actual_tag = response.headers.get('ETag', '')
                        require(response.status == 206
                                and response.headers.get('Content-Range') == f'bytes {offset}-{end}/{size}'
                                and response.headers.get('Content-Encoding', 'identity') == 'identity'
                                and re.fullmatch(r'"[^"]+"', actual_tag) is not None
                                and tag in (None, actual_tag),
                                'original artifact range, total size or strong ETag differs')
                        block = response.read(end - offset + 2)
                        require(len(block) == end - offset + 1, 'short original artifact range')
                    tag = actual_tag
                    break
                except urllib.error.HTTPError as error:
                    status = error.code
                    error.close()
                    if status in (401, 403) and attempt < 3:
                        address = None
                        continue
                    if status in (408, 429, 500, 502, 503, 504) and attempt < 3:
                        time.sleep(1 + attempt)
                        continue
                    raise OSError('administrative artifact range status ' + str(status)) from None
                except (urllib.error.URLError, TimeoutError, OSError):
                    if attempt == 3:
                        raise OSError('administrative original byte transport unavailable') from None
                    time.sleep(1 + attempt)
            output.write(block)
            sha.update(block)
            offset += len(block)
            count += 1
    require(offset == size and sha.hexdigest() == spec['artifact_sha256'],
            'complete original artifact ZIP SHA256 mismatch')
    temporary.replace(destination)
    record = dict(provider=provider, full_zip_sha256=sha.hexdigest(), strong_etag=tag,
                  bytes=offset, ranges=count, signed_address_acquisitions=renewals,
                  measured_disk_capacity=capacity, administrative_seconds=time.monotonic() - start,
                  scientific_evaluations=0, old_log_requests=0)
    emit(record)
    return record


def restore(archive, spec, target, parent):
    start = time.monotonic()
    target = Path(target)
    require(not target.exists(), 'do not overwrite a prior working scientific state')
    temporary = target.with_name(target.name + '.restoring')
    require(not temporary.exists(), 'ambiguous prior scientific restoration directory')
    with zipfile.ZipFile(archive) as z:
        members = z.infolist()
        names = [v.filename for v in members]
        require(len(names) == len(set(names)), 'duplicate original member path')
        for member in members:
            name = member.filename
            parts = PurePosixPath(name)
            require(not parts.is_absolute() and '..' not in parts.parts and '\\' not in name
                    and parts.parts and '\x00' not in name, 'unsafe original archive path')
            mode = stat.S_IFMT(member.external_attr >> 16)
            require(mode in (0, stat.S_IFREG, stat.S_IFDIR), 'links and special files are not restoration data')
        roots = [n for n in names if n == 'input-identity.json' or n.endswith('/input-identity.json')]
        require(len(roots) == 1, 'ambiguous original checkpoint identity')
        prefix = roots[0][:-len('input-identity.json')]
        documents = {}
        rawdocs = {}
        for name in ('input-identity', 'terminal', 'continuation', 'source-identity'):
            member = prefix + name + '.json'
            require(z.getinfo(member).file_size <= 32 * 2**20, 'unexpected original metadata size')
            raw = z.read(member)
            rawdocs[name] = raw
            documents[name] = dict(member=member, bytes=len(raw), sha256=digest(raw))
        terminal = json.loads(rawdocs['terminal'])
        identity = json.loads(rawdocs['input-identity'])
        continuation = json.loads(rawdocs['continuation'])
        require(documents['terminal']['bytes'] == spec['expected_artifact_terminal_bytes']
                and documents['terminal']['sha256'] == spec['expected_artifact_terminal_sha256'],
                'completed artifact terminal is not the one original log FINAL')
        require(digest(plain(identity).encode()) == spec['input_identity']
                and terminal['input_identity'] == spec['input_identity']
                and terminal['run'].split('-')[0] == str(spec['run_id'])
                and terminal.get('error') == spec['terminal_error'],
                'the original terminal or scientific identity differs')
        require(identity['settings']['immutable_parent'] == parent,
                'the exact immutable parent receipt changed')
        for target_key, source_key in (('accepted', 'accepted'), ('phase_index', 'next_phase_index'),
                                        ('iteration', 'next_iteration'), ('line', 'next_backtrack')):
            require(continuation[target_key] == spec[source_key], 'the original exact next operation differs')
        require(len(continuation['records']) == spec['finished_phase_records'], 'original completed phases differ')
        selected = [v for v in members if v.filename.startswith(prefix) and not v.is_dir()]
        total = sum(v.file_size for v in selected)
        capacity = space(target.parent, total)
        temporary.mkdir()
        for member in selected:
            relative = PurePosixPath(member.filename[len(prefix):])
            path = temporary.joinpath(*relative.parts)
            path.parent.mkdir(parents=True, exist_ok=True)
            with z.open(member) as source, path.open('xb') as dest:
                shutil.copyfileobj(source, dest, length=2**20)
        previous = temporary / 'previous-terminals'
        previous.mkdir(exist_ok=True)
        (previous / (terminal['run'] + '.json')).write_bytes(rawdocs['terminal'])
        temporary.replace(target)
    record = dict(original_run=spec['run_id'], restored_original_members=len(selected),
                  restored_original_bytes=total, documents=documents,
                  input_identity=spec['input_identity'], accepted=continuation['accepted'],
                  next_phase_index=continuation['phase_index'], next_iteration=continuation['iteration'],
                  next_backtrack=continuation['line'], original_completed_phases=len(continuation['records']),
                  measured_disk_capacity=capacity, administrative_seconds=time.monotonic() - start,
                  scientific_evaluations=0, coefficients_changed=False)
    emit(record)
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--parent-metadata', required=True)
    parser.add_argument('--parent-zip', required=True)
    parser.add_argument('--checkpoint-metadata')
    parser.add_argument('--state', required=True)
    args = parser.parse_args()
    require(os.environ.get('GITHUB_ACTIONS') == 'true'
            and os.environ.get('GITHUB_REPOSITORY', '').lower() == REPO.lower()
            and os.environ.get('GITHUB_RUN_ID', '').isdigit(),
            'complete archives are transported only on the public Actions runner')
    require(os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN'),
            'the administrative artifact transport needs its own Actions credential')
    start = time.monotonic()
    parent = json.loads(Path(args.parent_metadata).read_text())
    report = dict(started_at=utc(), consumer_run=os.environ['GITHUB_RUN_ID'],
                  consumer_attempt=os.environ.get('GITHUB_RUN_ATTEMPT', '1'))
    state = Path(args.state)
    if args.checkpoint_metadata:
        checkpoint = json.loads(Path(args.checkpoint_metadata).read_text())
        archive = Path(os.environ['RUNNER_TEMP']) / ('original-checkpoint-' + str(checkpoint['artifact_id']) + '.zip')
        report['checkpoint_download'] = receive(checkpoint, archive)
        report['exact_restore'] = restore(archive, checkpoint, state, parent)
        archive.unlink()
    else:
        require(not state.exists(), 'fresh science must not replace an existing paid state')
        state.mkdir(parents=True)
    report['parent_download'] = receive(parent, Path(args.parent_zip))
    report.update(completed_at=utc(), administrative_seconds=time.monotonic() - start,
                  scientific_evaluations=0, old_log_requests=0,
                  signed_urls_and_credentials_written=False)
    output = state / 'transport' / (report['consumer_run'] + '-' + report['consumer_attempt'] + '.json')
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(plain(report) + '\n')
    emit(dict(transport_complete=True, consumer_run=report['consumer_run'],
              administrative_seconds=report['administrative_seconds'], scientific_evaluations=0))


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        # URL-bearing transport exceptions must never disclose their signed address.
        emit(dict(transport_complete=False, error_type=type(error).__name__,
                  error=str(error) if isinstance(error, ValueError) else 'original-byte transport failed',
                  scientific_evaluations=0))
        raise SystemExit(2) from None
