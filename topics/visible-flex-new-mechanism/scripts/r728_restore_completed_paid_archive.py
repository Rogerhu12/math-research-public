"""Administrative transport of one completed paid checkpoint; no scientific imports."""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import stat
import tempfile
import time
from urllib import error, parse, request
from zipfile import ZipFile


def digest_file(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--request', required=True)
    args = ap.parse_args()
    if os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REPOSITORY', '').lower() != 'rogerhu12/math-research-public':
        raise SystemExit('The authorized public Actions transport is required.')
    started = time.monotonic()
    cfg = json.loads(Path(args.request).read_bytes())
    spec = cfg['completed_paid_checkpoint']
    if digest_file(Path(__file__)) != spec['transport_sha256']:
        raise ValueError('The administrative transport source differs from the request.')
    for name, sha in cfg['source_sha256'].items():
        if digest_file(Path(name)) != sha:
            raise ValueError('The frozen scientific source or bound workflow differs: ' + name)
    token = os.environ.get('GITHUB_TOKEN')
    if not token:
        raise RuntimeError('Read-only Actions authentication is missing.')
    api = 'https://api.github.com/repos/Rogerhu12/math-research-public'
    headers = {'Authorization': 'Bearer ' + token, 'Accept': 'application/vnd.github+json', 'User-Agent': 'visible-flex-paid-resume'}

    def metadata(path):
        with request.urlopen(request.Request(api + path, headers=headers), timeout=45) as response:
            return json.load(response)

    run = metadata('/actions/runs/' + str(spec['run']))
    job = metadata('/actions/jobs/' + str(spec['job']))
    artifact = metadata('/actions/artifacts/' + str(spec['artifact']))
    if any((run['id'] != spec['run'], run['head_sha'] != spec['head'], run['status'] != 'completed',
            run['conclusion'] != 'success', job['id'] != spec['job'], job['run_id'] != spec['run'],
            job['status'] != 'completed', job['conclusion'] != 'success', artifact['id'] != spec['artifact'],
            artifact['name'] != spec['name'], artifact['workflow_run']['id'] != spec['run'], artifact['expired'],
            artifact['size_in_bytes'] != spec['bytes'], artifact['digest'] != 'sha256:' + spec['sha256'])):
        raise ValueError('The completed parent run, job or original archive identity differs.')
    temp = Path(os.environ['RUNNER_TEMP'])
    dest = temp / 'r728-paid-checkpoint'
    if dest.exists() and any(dest.iterdir()):
        raise ValueError('Do not merge into an unverified or existing checkpoint.')
    staging = Path(tempfile.mkdtemp(prefix='r728-verified-archive-', dir=temp))
    archive_path = staging / 'original.zip'

    class NoRedirect(request.HTTPRedirectHandler):
        def redirect_request(self, *unused):
            return None

    endpoint = api + '/actions/artifacts/' + str(spec['artifact']) + '/zip'
    try:
        response = request.build_opener(NoRedirect).open(request.Request(endpoint, headers=headers), timeout=45)
    except error.HTTPError as exc:
        if exc.code not in (301, 302, 303, 307, 308):
            raise
        location = exc.headers['Location']
        if parse.urlparse(location).scheme != 'https':
            raise ValueError('The authenticated archive handoff is not HTTPS.')
        response = request.urlopen(location, timeout=60)
    # The signed object download receives no GitHub authorization header.
    with response, archive_path.open('wb') as out:
        while True:
            chunk = response.read(1024 * 1024)
            if not chunk:
                break
            out.write(chunk)
            if out.tell() > spec['bytes']:
                raise ValueError('The paid archive exceeds its authenticated length.')
    if archive_path.stat().st_size != spec['bytes'] or digest_file(archive_path) != spec['sha256']:
        raise ValueError('The paid archive is not the original authenticated ZIP.')
    extracted = staging / 'checked'
    extracted.mkdir()
    with ZipFile(archive_path) as archive:
        names = archive.namelist()
        if len(names) != len(set(names)) or names.count('ledger.json') != 1 or names.count('r703-original-final.json') != 1:
            raise ValueError('Original checkpoint members are not unique.')
        ledger = json.loads(archive.read('ledger.json'))
        if ledger['fingerprint'] != spec['fingerprint'] or len(ledger['kept']) != spec['kept']:
            raise ValueError('Original paid operation identity or retained count differs.')
        if ledger['latest_state'] != spec['latest_state'] or ledger['pending'] != spec['pending']:
            raise ValueError('Original continuation is not at the declared next unpaid operation.')
        if ledger['counts'] != spec['counts']:
            raise ValueError('The inherited original scientific costs differ.')
        required = {'ledger.json', 'r703-original-final.json'} | {key + '.npz' for key in ledger['kept']}
        if set(names) != required:
            raise ValueError('The original artifact does not contain exactly the retained ledger members.')
        for info in archive.infolist():
            p = PurePosixPath(info.filename)
            mode = info.external_attr >> 16
            if p.is_absolute() or len(p.parts) != 1 or '..' in p.parts or stat.S_ISLNK(mode) or info.is_dir():
                raise ValueError('The original numeric checkpoint has an unsafe member path.')
            with archive.open(info) as src, (extracted / info.filename).open('wb') as out:
                shutil.copyfileobj(src, out, 1024 * 1024)
        for key, (length, sha) in ledger['kept'].items():
            path = extracted / (key + '.npz')
            if path.stat().st_size != length or digest_file(path) != sha:
                raise ValueError('Original retained paid block failed its ledger identity: ' + key)
    literal = extracted / 'r703-original-final.json'
    if literal.stat().st_size != 39163 or digest_file(literal) != 'bd5a52dcc40e31e898d3e02b99e4e5c0d449bfd697ac95faa8a168082c6012b2':
        raise ValueError('Original source literal differs inside the completed checkpoint.')
    if dest.exists():
        dest.rmdir()
    extracted.rename(dest)
    shutil.rmtree(staging)
    report = dict(kind='r728_original_paid_checkpoint_restored', parent_run=spec['run'], parent_artifact=spec['artifact'],
                  zip_bytes=spec['bytes'], zip_sha256=spec['sha256'], fingerprint=ledger['fingerprint'],
                  inherited_counts=ledger['counts'], inherited_cumulative_seconds=ledger['cumulative_seconds'],
                  exact_latest_state=ledger['latest_state'], exact_next_operation=ledger['pending'],
                  retained_blocks=len(ledger['kept']), retired_equivalent_blocks=len(ledger['retired']),
                  administrative_seconds=time.monotonic() - started, completed_original_log_requests=0,
                  new_scientific_evaluations=0, credentials_passed_to_scientific_child=False)
    print('R728_PAID_ARCHIVE_RESTORED ' + json.dumps(report, sort_keys=True, separators=(',', ':')), flush=True)


if __name__ == '__main__':
    main()
