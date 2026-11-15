#!/usr/bin/env python3
"""Run only missing old-radial Airy Taylor degrees through twelve.

Freeze the original75 complete stages and the already accepted intrinsic jets.
Keep original and new stage identities separate and reuse every complete prefix.
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
PIPELINE = TOPIC/'scripts/fourfold_codazzi_old_rho_first_Airy_Taylor_extension_CI.py'


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
                      str(TOPIC/'notes/old_rho_first_Airy_Taylor_extension_ci/')))
        subprocess.run(gitbase+['sparse-checkout', 'set', '--no-cone', '--stdin'], cwd=root,
                       input='\n'.join('/'+p for p in sorted(paths))+'\n', text=True, check=True)
        print('Hydrated '+str(len(manifest['files']))+' exact repository inputs, including all75 exact original stages and the successful intrinsic jets through15.', flush=True)
        return
    if args.work is None or args.out_dir is None or args.prepared is None:
        raise ValueError('the immutable work and separate output directories are required')
    work, output = args.work.resolve(), args.out_dir.resolve()
    if work.exists() or output.exists():
        raise FileExistsError('preserve the actual output and scientific snapshot of every run')
    work.mkdir(parents=True)
    output.mkdir(parents=True)
    state = dict(kind='actual_public_append_only_Airy_Taylor_execution_and_publication',
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
        state['readme_checks'].append(dict(time=datetime.now(timezone.utc).isoformat(),
                                           before=before, after=after, actual_diff=diff,
                                           explicitly_reviewed_commit=rules['read_commit']))
        save(output/'worker-process.json', state)

    git('config', 'user.name', 'github-actions[bot]')
    git('config', 'user.email', '41898282+github-actions[bot]@users.noreply.github.com')
    sync()
    checked(args.manifest, args.manifest_sha)
    checked(args.rules, args.rules_sha)
    state['original_completed_auxiliary_domains_recomputed']=0
    state['original_infinite_tail_evaluations_recomputed']=0
    state['new_Taylor_degrees_requested']=list(range(7,13))
    state['strict_original75_stage_and_complete_intrinsic_reuse_required']=True
    state['old_root_targets_and_auxiliary_domains_recomputed']=0
    state['physical_background_identity_outside_original_piece_claimed']=False
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
    # Reuse only exact source, manifest, runtime and original-native identities.
    expected_source=next(x['sha256'] for x in manifest['files']
        if x['path']==str(TOPIC/'scripts/fourfold_codazzi_old_rho_first_Airy_Taylor_extension.py'))
    pins={entry['path']:entry['sha256'] for entry in manifest['files']}
    external_pins={entry['name']:entry['sha256'] for entry in manifest['external_completed_natives']}
    expected_runtime={k:manifest['runtime'][k] for k in ('python','python_flint','numpy','scipy')}
    old_source='e4ccbf4b343623d74d089f79b6605a0601975c6ea5c1d2e113bad568fe60167d'
    old_manifest='226e5acac42026431acbd166f92d423b6292ba6f73e65f58f808647d4701f1ad'
    old_native=work/manifest['input_paths']['old_native']
    old_index=json.loads(gzip.decompress(old_native.read_bytes()))
    old_inventory=old_index['stages']
    if len(old_inventory)!=75:raise ValueError('all75 exact accepted old stages are required')
    candidates=[]
    previous_root=root/TOPIC/'notes/old_rho_first_Airy_Taylor_extension_ci'
    processes=list(previous_root.glob('*/consumers/process.json')) if previous_root.exists() else []
    explicit=args.prepared.resolve()/'resume'/'consumers'/'process.json'
    if explicit.is_file():
        ep=json.loads(explicit.read_text())
        # An artifact's exact complete native supersedes only a repository
        # copy of that SAME native; it cannot silently replace another prefix.
        processes=[p for p in processes
            if json.loads(p.read_text()).get('native_sha256')!=ep.get('native_sha256')]
        processes.append(explicit)
    for process_path in processes:
        pd=json.loads(process_path.read_text())
        native_path=process_path.parent/'complete-old-rho-first-Airy-Taylor-through-twelve.json.gz'
        if (pd.get('public_repository')!=PUBLIC or pd.get('manifest_sha256')!=args.manifest_sha
            or pd.get('mathematical_source_sha256')!=expected_source or not native_path.is_file()):
            continue
        if sha(native_path)!=pd.get('native_sha256') or native_path.stat().st_size!=pd.get('native_bytes'):
            raise ValueError('an accepted Taylor extension prefix changed bytes')
        nd=json.loads(gzip.decompress(native_path.read_bytes()))
        if (nd.get('source_sha256')!=expected_source or nd.get('input_manifest_sha256')!=args.manifest_sha
            or nd.get('runtime')!=expected_runtime):
            raise ValueError('an accepted Taylor extension prefix changed scientific identity')
        originals=nd.get('original_stages',{});new=nd.get('stages',{})
        if set(originals)&set(new):
            raise ValueError('an accepted new stage replaced an original name')
        if any(name not in old_inventory or entry!=old_inventory[name] for name,entry in originals.items()):
            raise ValueError('an accepted original Taylor stage receipt changed')
        stages=[];seen=set()
        for role,records in (('original',originals),('new',new)):
            for name,entry in records.items():
                relative=Path(entry['file'])
                if relative.is_absolute() or '..' in relative.parts or relative.parts[0]!='stages':
                    raise ValueError('a completed natural stage leaves its directory')
                if str(relative) in seen:raise ValueError('accepted stages overwrite the same file')
                seen.add(str(relative));stagepath=native_path.parent/relative
                if not stagepath.is_file() or sha(stagepath)!=entry['sha256'] or stagepath.stat().st_size!=entry['bytes']:
                    raise ValueError('an accepted original or new stage has unavailable or changed bytes')
                sd=json.loads(gzip.decompress(stagepath.read_bytes()))
                names=[sd[k] for k in ('stage','name') if k in sd]
                source_id=old_source if role=='original' else expected_source
                manifest_id=old_manifest if role=='original' else args.manifest_sha
                if (not names or any(n!=name for n in names) or sd.get('complete') is not True
                    or sd.get('source_sha256')!=source_id or sd.get('input_manifest_sha256')!=manifest_id):
                    raise ValueError('an accepted original or new stage changed mathematical identity')
                stages.append(entry)
        if not new:continue
        counts=dict(original_natural_stages=len(originals),new_natural_stages=len(new),
            complete_new_derivative_budgets=len(nd.get('first_correction_derivative_budgets',[])))
        complete=bool(nd.get('complete') and nd.get('proved') and nd.get('failure') is None
            and nd.get('gates') and all(g['passed'] for g in nd['gates'])
            and originals==old_inventory and counts['complete_new_derivative_budgets']==3)
        if complete and pd.get('actual_returncode')!=0:continue
        score=(int(complete),counts['complete_new_derivative_budgets'],counts['new_natural_stages'])
        candidates.append((score,complete,counts,process_path,native_path,stages))
    if candidates:
        score,complete,counts,pp,np,stages=max(candidates,key=lambda z:z[0])
        accepted=work/'accepted-Taylor-extension-prefix';accepted.mkdir()
        resume=accepted/'complete-old-rho-first-Airy-Taylor-through-twelve.json.gz'
        shutil.copyfile(np,resume)
        if sha(resume)!=sha(np):raise ValueError('the immutable extension prefix index differs')
        for entry in stages:
            source=np.parent/entry['file'];target=accepted/entry['file']
            target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,target)
            if sha(target)!=entry['sha256']:raise ValueError('an accepted natural prefix changed during copy')
        command+=['--resume',str(resume),'--resume-sha',sha(resume)]
        evidence=output/'evidence';evidence.mkdir(exist_ok=True)
        shutil.copyfile(pp,evidence/'original-Taylor-extension-prefix-process.json')
        state['actual_prefix_reuse']=dict(original_process_sha256=sha(pp),original_native_sha256=sha(resume),
            original_native_bytes=resume.stat().st_size,completed_stage_counts=counts,
            original_complete_native=complete,all_original_and_new_natural_stage_files_preserved=True,
            all_source_runtime_and_input_pins_unchanged=True)
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
    report = root/TOPIC/'notes/old_rho_first_Airy_Taylor_extension_ci'/('run-'+state['run_id']+'-'+state['run_attempt'])
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
                                sha256=hashlib.sha256(raw).hexdigest(),
                                **({'original_sha256':original_sha} if hashlib.sha256(raw).hexdigest()!=original_sha else {})))
        publication=dict(actual_returncode=state['actual_returncode'],
             complete=state['complete'],repository=PUBLIC,run_id=state['run_id'],
             reviewed_pull_history=state['readme_checks'],files=entries,
             byte_identical_files_omit_only_duplicate_original_sha256=True,
             true_PDE_branch_or_final_family_claimed=False)
        raw=(json.dumps(publication,indent=2,allow_nan=False)+'\n').encode()
        if len(raw)>60000:
            inventory=report/'complete-publication-file-inventory.json.gz'
            inventory.write_bytes(gzip.compress((json.dumps(entries,indent=2,allow_nan=False)+'\n').encode(),mtime=0))
            publication.pop('files')
            publication['complete_file_inventory']=dict(file=inventory.name,
                bytes=inventory.stat().st_size,sha256=sha(inventory),files=len(entries),
                every_original_file_receipt_preserved=True)
        if len((json.dumps(publication,indent=2,allow_nan=False)+'\n').encode())>60000:
            raise ValueError('the complete readable publication receipt exceeds60000 bytes')
        save(report/'publication.json',publication)

    snapshot()
    owned = str(report.relative_to(root))
    git('add', '--sparse', '--', owned)
    git('commit', '-m', 'visible-exact: append only missing old-radial Airy Taylor degrees through12')
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
                          old_root_targets_and_auxiliary_domains_recomputed=False, original_complete_forcing_and_amplitudes_reused=True, complete_original_and_new_Taylor_prefixes_preserved=True, physical_background_replaced=False, report=owned)), flush=True)
    if not state['complete']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
