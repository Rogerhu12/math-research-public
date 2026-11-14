#!/usr/bin/env python3
"""Restore complete frozen cap FE artifacts without forwarding credentials.

The numerical collectors remain responsible for all mathematical energy
bounds. This entry preserves each original topic-relative scientific path,
checks artifact and worker/file identities, and retains the original log.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import urllib.error
import urllib.request
import zipfile

BASE = 'https://api.github.com/repos/Rogerhu12/math-research'


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def read(path):
    path = Path(path)
    return json.load(gzip.open(path, 'rt')) if path.suffix == '.gz' else json.loads(path.read_text())


def relative(value):
    path = PurePosixPath(value)
    if path.is_absolute() or '..' in path.parts:
        raise ValueError('unsafe artifact-relative path')
    return path


def api_request(path):
    return urllib.request.Request(BASE + path, headers={
        'Authorization': 'Bearer ' + os.environ['TASK_GITHUB_TOKEN'],
        'Accept': 'application/vnd.github+json',
        'User-Agent': 'visible-exact-cap-artifact-intake'})


def api_json(path):
    with urllib.request.build_opener(NoRedirect()).open(api_request(path), timeout=45) as response:
        return json.load(response)


def artifact_bytes(artifact_id):
    opener = urllib.request.build_opener(NoRedirect())
    try:
        with opener.open(api_request('/actions/artifacts/%d/zip' % artifact_id), timeout=45) as response:
            return response.read()
    except urllib.error.HTTPError as error:
        if error.code not in (301, 302, 303, 307, 308):
            raise RuntimeError('artifact API returned HTTP %d' % error.code) from None
        location = error.headers.get('Location')
        if not location:
            raise RuntimeError('artifact redirect omitted its temporary destination') from None
        # The second request is new and contains no Authorization. The
        # signed address is never printed, saved, or included in an error.
        try:
            with opener.open(urllib.request.Request(location), timeout=90) as response:
                return response.read()
        except urllib.error.HTTPError as second:
            raise RuntimeError('credential-free artifact request returned HTTP %d' % second.code) from None
        except Exception:
            raise RuntimeError('credential-free artifact download failed') from None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run', type=int, required=True)
    parser.add_argument('--scratch', type=Path, required=True)
    args = parser.parse_args()
    topic = Path(__file__).resolve().parents[1]
    os.chdir(topic)
    args.scratch.mkdir(parents=True, exist_ok=True)
    listing = api_json('/actions/runs/%d/artifacts?per_page=100' % args.run)
    run = api_json('/actions/runs/%d' % args.run)
    run_record = {key: run.get(key) for key in (
        'id', 'head_sha', 'head_branch', 'status', 'conclusion', 'run_attempt',
        'created_at', 'updated_at')}
    notes = topic / 'notes' / '2026-11-12-cap-ci-outcomes' / str(args.run)
    notes.mkdir(parents=True, exist_ok=True)
    for artifact in sorted(listing['artifacts'], key=lambda item: item['name']):
        match = re.fullmatch(r'visible-exact-cap-native-(\d+)-(\d+)', artifact['name'])
        if not match:
            continue
        first, last = map(int, match.groups())
        out = notes / artifact['name']
        report_path = out / 'intake.json'
        if report_path.exists() and read(report_path).get('complete'):
            print('ALREADY_INTAKEN', artifact['name'], flush=True)
            continue
        payload = artifact_bytes(artifact['id'])
        archive_sha = digest(payload)
        if artifact.get('digest') != 'sha256:' + archive_sha:
            raise ValueError('artifact archive digest differs')
        stage = args.scratch / artifact['name']
        stage.mkdir(parents=True, exist_ok=True)
        prefix = 'data/cap_physical4_energy/native_ci_%d/block_%d_%d' % (args.run, first, last)
        inventory = []
        with zipfile.ZipFile(io.BytesIO(payload)) as archive:
            names = archive.namelist()
            if len(names) != len(set(names)):
                raise ValueError('duplicate artifact member')
            for name in names:
                rel = relative(name)
                if name.endswith('/'):
                    continue
                if not (name.startswith(prefix + '/') or name == 'ci-output/cap-native.log'):
                    raise ValueError('unexpected artifact member: ' + name)
                raw = archive.read(name)
                path = stage / str(rel)
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(raw)
                inventory.append(dict(path=name, sha256=digest(raw), bytes=len(raw)))
        del payload
        out.mkdir(parents=True, exist_ok=True)
        log = stage / 'ci-output/cap-native.log'
        if log.is_file():
            shutil.copyfile(log, out / 'cap-native.log')
        block = stage / prefix
        worker = read(block / 'worker_provenance.json')
        manifest = read(block / 'manifest.json')
        complete = worker.get('complete') and manifest.get('complete')
        report = dict(run=run_record, artifact_id=artifact['id'],
            artifact_name=artifact['name'], artifact_archive_sha256=archive_sha,
            artifact_archive_bytes=artifact['size_in_bytes'],
            original_topic_relative_directory=prefix, file_inventory=inventory,
            complete=False, partial_preserved=str(block),
            scope='Intake and identity validation only; the unchanged energy collector must validate complete interval proofs.')
        if not complete:
            report_path.write_text(json.dumps(report, indent=2) + '\n')
            print('PRESERVED_PARTIAL', artifact['name'], flush=True)
            continue
        identity = worker['identity']
        if (identity['requested_element_range'] != [first, last]
            or identity['out_dir'] != prefix
            or manifest['requested_element_range'] != [first, last]
            or worker['observed_child_returncode'] != 0):
            raise ValueError('completed artifact describes another job')
        checked = 0
        for name, expected in identity['complete_input_sha256'].items():
            path = topic / str(relative(name))
            if digest(path.read_bytes()) != expected:
                raise ValueError('a complete CI input differs locally: ' + name)
            checked += 1
        for name, expected in identity['source_closure_sha256'].items():
            if identity['complete_input_sha256'].get(name) != expected:
                raise ValueError('worker source closure differs from its checked inputs')
        if (digest((topic / identity['input_manifest']).read_bytes()) != identity['input_manifest_sha256']
            or digest((topic / 'scripts/fourfold_phase_cap_native_ci.py').read_bytes()) != identity['worker_sha256']
            or digest((topic / identity['kernel']).read_bytes()) != identity['kernel_sha256']):
            raise ValueError('the frozen worker/kernel/input manifest differs')
        if worker['completed_manifest'] != dict(path=prefix + '/manifest.json',
                sha256=digest((block / 'manifest.json').read_bytes())):
            raise ValueError('worker binds a different completed FE manifest')
        if (manifest['identity']['source_sha256'] != identity['kernel_sha256']
            or manifest['identity']['object_sha256'] != identity['object_sha256']
            or manifest['requested_exact_radial_interval'] != identity['exact_radial_interval']):
            raise ValueError('native mathematical identity differs from frozen worker')
        rows = manifest['elements']
        if [row['element'] for row in rows] != list(range(first, last)):
            raise ValueError('completed artifact misses or repeats an element')
        for row in rows:
            path = stage / str(relative(row['path']))
            if not row['complete'] or digest(path.read_bytes()) != row['sha256']:
                raise ValueError('completed element bytes differ from manifest')
            proof = read(path)
            if not proof['complete'] or proof['identity'] != manifest['identity']:
                raise ValueError('complete element has a different mathematical identity')
        destination = topic / prefix
        if destination.exists():
            raise ValueError('refuse to overwrite existing scientific block: ' + prefix)
        destination.parent.mkdir(parents=True, exist_ok=True)
        block.rename(destination)
        report.update(complete=True, partial_preserved=None,
            checked_frozen_input_files=checked,
            complete_elements=[row['element'] for row in rows],
            manifest_sha256=digest((destination / 'manifest.json').read_bytes()),
            worker_sha256=digest((destination / 'worker_provenance.json').read_bytes()),
            all_original_scientific_paths_preserved=True,
            mathematical_energy_collector_still_required=True)
        report_path.write_text(json.dumps(report, indent=2) + '\n')
        print(json.dumps(dict(artifact=artifact['name'], complete=True,
            elements=report['complete_elements'], checked_input_files=checked,
            manifest_sha256=report['manifest_sha256'])), flush=True)


if __name__ == '__main__':
    main()
