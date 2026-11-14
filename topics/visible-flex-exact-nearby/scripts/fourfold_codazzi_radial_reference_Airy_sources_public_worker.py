#!/usr/bin/env python3
"""Publish the true-radial-reference Airy profiles and complete source refinement.

Hydrate the complete fixed scientific closure and freeze an immutable scientific snapshot.
Restore the single completed original root native with exact SHA and byte checks.
Retain both complete repository natives and every new profile/integral prefix.
"""
from __future__ import annotations

import argparse
import base64
from datetime import datetime, timezone
import gzip
import hashlib
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import time

PUBLIC = 'Rogerhu12/math-research-public'
TOPIC = Path('topics/visible-flex-exact-nearby')
PIPELINE = TOPIC/'scripts/fourfold_codazzi_radial_reference_Airy_sources_CI.py'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def checked(path, expected):
    if sha(path) != expected:
        raise ValueError('a separately pinned input changed: '+str(path))
    return json.loads(Path(path).read_text())


def save(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+'.partial')
    temporary.write_text(json.dumps(data, indent=2, allow_nan=False)+'\n')
    temporary.replace(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mode', choices=('hydrate', 'run'), required=True)
    parser.add_argument('--manifest', type=Path, required=True)
    parser.add_argument('--manifest-sha', required=True)
    parser.add_argument('--pipeline-sha', required=True)
    parser.add_argument('--rules', type=Path, required=True)
    parser.add_argument('--rules-sha', required=True)
    parser.add_argument('--work', type=Path)
    parser.add_argument('--prepared', type=Path)
    parser.add_argument('--out-dir', type=Path)
    args = parser.parse_args()
    root = Path(os.environ['GITHUB_WORKSPACE']).resolve()
    if os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REPOSITORY') != PUBLIC:
        raise RuntimeError('this wrapper runs only in the real public repository Actions job')
    args.manifest = args.manifest.resolve()
    args.rules = args.rules.resolve()
    manifest = checked(args.manifest, args.manifest_sha)
    rules = checked(args.rules, args.rules_sha)
    if manifest['public_repository'] != PUBLIC or rules['repository'] != PUBLIC:
        raise ValueError('the manifest or reviewed rules belong to another repository')
    relative_manifest = args.manifest.relative_to(root)
    relative_rules = args.rules.relative_to(root)
    paths = set()
    for entry in manifest['files']:
        relative = Path(entry['path'])
        if relative.is_absolute() or '..' in relative.parts or not str(relative).startswith(str(TOPIC)+'/'):
            raise ValueError('a scientific input leaves the one authorized topic')
        paths.add(str(relative))
    gitbase = ['git', '-c', 'safe.directory='+str(root)]
    if args.mode == 'hydrate':
        paths.update(rules['readme_sha256'])
        paths.update((str(relative_manifest), str(relative_rules),
                      str(Path(__file__).resolve().relative_to(root)),
                      str(TOPIC/'notes/radial_reference_Airy_sources_ci/')))
        subprocess.run(gitbase+['sparse-checkout', 'set', '--no-cone', '--stdin'], cwd=root,
                       input='\n'.join('/'+p for p in sorted(paths))+'\n', text=True, check=True)
        print('Hydrated '+str(len(manifest['files']))+' exact files; one external root native and both repository natives remain separately verified.', flush=True)
        return
    if args.work is None or args.out_dir is None or args.prepared is None:
        raise ValueError('the immutable work and separate output directories are required')
    work, output = args.work.resolve(), args.out_dir.resolve()
    if work.exists() or output.exists():
        raise FileExistsError('preserve the actual output and scientific snapshot of every run')
    work.mkdir(parents=True)
    output.mkdir(parents=True)
    state = dict(kind='actual_public_radial_reference_Airy_sources_execution_and_publication',
                 repository=PUBLIC, run_id=os.environ['GITHUB_RUN_ID'],
                 run_attempt=os.environ['GITHUB_RUN_ATTEMPT'],
                 workflow_commit=os.environ['GITHUB_SHA'], worker_sha256=sha(__file__),
                 manifest_sha256=args.manifest_sha, reviewed_rules_sha256=args.rules_sha,
                 started_utc=datetime.now(timezone.utc).isoformat(), complete=False,
                 readme_checks=[], actual_returncode=None, final_topic_complete=False)
    environment = os.environ.copy()
    token = environment.pop('GITHUB_TOKEN')
    environment.update(GIT_TERMINAL_PROMPT='0', GIT_CONFIG_COUNT='1',
                       GIT_CONFIG_KEY_0='http.https://github.com/.extraheader',
                       GIT_CONFIG_VALUE_0='AUTHORIZATION: basic '+base64.b64encode(('x-access-token:'+token).encode()).decode())

    def git(*argv, check=True):
        process = subprocess.run(gitbase+list(argv), cwd=root, env=environment,
                                 text=True, capture_output=True, timeout=180)
        if check and process.returncode:
            print(process.stdout+process.stderr, flush=True)
            raise RuntimeError('actual Git operation failed: '+argv[0])
        return process

    def sync():
        before = git('rev-parse', 'HEAD').stdout.strip()
        git('pull', '--rebase', 'origin', 'main')
        after = git('rev-parse', 'origin/main').stdout.strip()
        diff = git('diff', before, after, '--', *rules['readme_sha256']).stdout
        for relative, expected in rules['readme_sha256'].items():
            if sha(root/relative) != expected:
                print(diff, flush=True)
                raise RuntimeError('an unread README change requires its actual diff to be read')
        state['readme_checks'].append(dict(before=before, after=after, actual_diff=diff,
                                           explicitly_reviewed_commit=rules['read_commit']))
        save(output/'worker-process.json', state)

    git('config', 'user.name', 'github-actions[bot]')
    git('config', 'user.email', '41898282+github-actions[bot]@users.noreply.github.com')
    sync()
    checked(args.manifest, args.manifest_sha)
    checked(args.rules, args.rules_sha)
    state['all_original_target_coefficient_ray_and_amplitude_solves_recomputed']=0
    for entry in manifest['files']:
        source, destination = root/entry['path'], work/entry['path']
        if sha(source) != entry['sha256'] or source.stat().st_size != entry['bytes']:
            raise ValueError('an original complete source or native changed: '+entry['path'])
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
        if sha(destination) != entry['sha256']:
            raise ValueError('the complete immutable snapshot differs')
    # Freeze only exact original complete artifact files, retaining their relative paths.
    original = work/'originals'
    original.mkdir()
    state['original_artifact_receipts']=[]
    for spec in manifest['external_completed_natives']:
        relative=spec['prepared_path']
        source=args.prepared.resolve()/relative
        if not source.is_file() or sha(source)!=spec['sha256'] or source.stat().st_size!=spec['bytes']:
            raise ValueError('a complete original native differs: '+relative)
        target=original/relative
        target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(source,target)
        if sha(target)!=spec['sha256']:
            raise ValueError('the immutable original native copy differs: '+relative)
        state['original_artifact_receipts'].append(dict(name=spec['name'],run_id=spec['run_id'],
            path=relative,sha256=spec['sha256'],bytes=target.stat().st_size))
    destination = work/relative_manifest
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(args.manifest, destination)
    if sha(work/PIPELINE) != args.pipeline_sha:
        raise ValueError('the exact reviewed pipeline changed')
    command = [sys.executable, '-u', str(work/PIPELINE), '--repo', str(work),
               '--manifest', str(destination), '--manifest-sha', args.manifest_sha,
               '--out-dir', str(output/'consumers'), '--prepared', str(original)]
    # Reuse only the identical producer/manifest and all exact original native identities.
    # Accepted radial-reference profiles and partial new source integrals are both preserved.
    expected_source=next(x['sha256'] for x in manifest['files']
        if x['path']==str(TOPIC/'scripts/fourfold_codazzi_radial_reference_Airy_sources.py'))
    candidates=[]
    previous_root=root/TOPIC/'notes/radial_reference_Airy_sources_ci'
    processes=list(previous_root.glob('*/consumers/process.json')) if previous_root.exists() else []
    explicit=args.prepared.resolve()/'resume'/'consumers'/'process.json'
    if explicit.is_file():processes.append(explicit)
    for process_path in processes:
        pd=json.loads(process_path.read_text())
        native_path=process_path.parent/'radial-reference-Airy-sources.json.gz'
        if (pd.get('public_repository')!=PUBLIC
            or pd.get('manifest_sha256')!=args.manifest_sha
            or pd.get('mathematical_source_sha256')!=expected_source
            or not native_path.is_file()):
            continue
        if sha(native_path)!=pd.get('native_sha256') or native_path.stat().st_size!=pd.get('native_bytes'):
            raise ValueError('a published actual source prefix changed its bytes')
        nd=json.loads(gzip.decompress(native_path.read_bytes()))
        if (nd.get('source_sha256')!=expected_source
            or nd.get('input_manifest_sha256')!=args.manifest_sha
            or nd.get('root_native_sha256')!=manifest['external_completed_natives'][0]['sha256']
            or nd.get('first_forcing_native_sha256')!=manifest['forcing_identity']['native_sha256']
            or nd.get('first_seam_native_sha256')!=manifest['first_seam_identity']['native_sha256']
            or nd.get('original_completed_directed_native_sha256')!=manifest['original_completed_directed_identity']['native_sha256']
            or nd.get('original_completed_analytic_native_sha256')!=manifest['original_completed_analytic_identity']['native_sha256']):
            raise ValueError('a saved source prefix has a different immutable identity')
        count=len(nd.get('coefficient_rows',[]))
        cells=sum(len(z.get('rows',[])) for z in nd.get('cases',[]))
        cases=sum(bool(z.get('complete')) for z in nd.get('cases',[]))
        profiles=sum(bool(z.get('complete_radial_reference_profile')) for z in nd.get('cases',[]))
        if count==0 and cells==0:continue
        complete=bool(nd.get('complete') and nd.get('proved') and nd.get('failure') is None
            and nd.get('gates') and all(g['passed'] for g in nd['gates']))
        if complete and pd.get('actual_returncode')!=0:continue
        candidates.append((complete,count,cells,cases,profiles,process_path,native_path))
    if candidates:
        complete,count,cells,cases,profiles,pp,np=max(candidates,key=lambda z:(z[0],z[1],z[2],z[3],z[4]))
        resume=work/'original-old-circle-source-prefix.json.gz'
        shutil.copyfile(np,resume)
        if sha(resume)!=sha(np):raise ValueError('the immutable original seam prefix differs')
        command+=['--resume',str(resume),'--resume-sha',sha(resume)]
        evidence=output/'evidence';evidence.mkdir(exist_ok=True)
        shutil.copyfile(pp,evidence/'original-old-circle-source-prefix-process.json')
        state['actual_prefix_reuse']=dict(original_process_sha256=sha(pp),original_native_sha256=sha(resume),
            original_native_bytes=resume.stat().st_size,completed_coefficient_rows=count,completed_integral_rows=cells,completed_radius_cases=cases,
            completed_radial_reference_profiles=profiles,
            original_complete_native=complete,all_source_and_input_pins_unchanged=True)
    state['command'] = command
    state['complete_original_inputs_verified'] = len(manifest['files'])
    save(output/'worker-process.json', state)
    child_environment = os.environ.copy()
    child_environment.pop('GITHUB_TOKEN', None)
    state['actual_scientific_checkout_commit'] = git('rev-parse', 'HEAD').stdout.strip()
    child_environment['VISIBLE_PHASE_SCIENCE_COMMIT'] = state['actual_scientific_checkout_commit']
    save(output/'worker-process.json', state)
    started = time.monotonic()
    with (output/'driver.stdout.log').open('wb') as stream:
        child = subprocess.Popen(command, cwd=work, env=child_environment,
                                 stdout=stream, stderr=subprocess.STDOUT, start_new_session=True)
        try:
            child.wait(timeout=3000)
        except subprocess.TimeoutExpired:
            state['actual_timeout_seconds'] = 3000
            os.killpg(child.pid, signal.SIGTERM)
            try:
                child.wait(timeout=10)
            except subprocess.TimeoutExpired:
                os.killpg(child.pid, signal.SIGKILL)
                child.wait()
        state['actual_returncode'] = child.returncode
    state['mathematical_wall_seconds'] = time.monotonic()-started
    state['complete'] = state['actual_returncode'] == 0
    save(output/'worker-process.json', state)
    # The one complete driver is bounded by50 minutes, below the hourly
    # pull requirement. Pull before publishing its actual complete outcome.
    sync()
    report = root/TOPIC/'notes/radial_reference_Airy_sources_ci'/('run-'+state['run_id']+'-'+state['run_attempt'])
    report.mkdir(parents=True, exist_ok=True)

    def snapshot():
        entries = []
        for source in sorted(output.rglob('*')):
            if not source.is_file() or source.name.endswith('.partial'):
                continue
            relative = source.relative_to(output)
            raw = source.read_bytes()
            original_sha = hashlib.sha256(raw).hexdigest()
            if len(raw) > 1_000_000 and source.suffix != '.gz':
                raw = gzip.compress(raw, mtime=0)
                relative = Path(str(relative)+'.gz')
            if len(raw) > 5_000_000:
                entries.append(dict(file=str(relative), original_sha256=original_sha,
                                    bytes=len(raw), retained_in_original_Actions_artifact=True))
                continue
            target = report/relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(raw)
            entries.append(dict(file=str(relative), bytes=len(raw),
                                sha256=hashlib.sha256(raw).hexdigest(), original_sha256=original_sha))
        save(report/'publication.json', dict(actual_returncode=state['actual_returncode'],
             complete=state['complete'], repository=PUBLIC, run_id=state['run_id'],
             reviewed_pull_history=state['readme_checks'], files=entries,
             true_PDE_branch_or_final_family_claimed=False))

    snapshot()
    owned = str(report.relative_to(root))
    git('add', '--sparse', '--', owned)
    git('commit', '-m', 'visible-exact: certify true radial Airy profiles and complete central tails')
    while True:
        push = git('push', 'origin', 'HEAD:refs/heads/main', check=False)
        print(push.stdout+push.stderr, flush=True)
        if push.returncode == 0:
            break
        if not any(word in push.stderr for word in ('non-fast-forward', 'fetch first', 'cannot lock ref', 'remote rejected')):
            raise RuntimeError('publication failed outside the concurrent-main retry path')
        sync()
        snapshot()
        git('add', '--sparse', '--', owned)
        git('commit', '--amend', '--no-edit')
    print(json.dumps(dict(complete=state['complete'], actual_returncode=state['actual_returncode'],
                          original_targets_recomputed=False, original_coefficient_rows_recomputed=False, original_amplitude_solves_recomputed=False, report=owned)), flush=True)
    if not state['complete']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
