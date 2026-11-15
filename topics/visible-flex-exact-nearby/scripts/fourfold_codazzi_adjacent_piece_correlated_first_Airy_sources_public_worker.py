#!/usr/bin/env python3
"""Consume correlated complete sources on the two true neighbors of the root piece.

Freeze the complete original norm and source files; retain every new scalar,
operator, integral and recombination prefix without repeating accepted work.
"""
from __future__ import annotations

import argparse
import base64
import copy
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
PIPELINE = TOPIC/'scripts/fourfold_codazzi_adjacent_piece_correlated_first_Airy_sources_CI.py'


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


def recover_prefix_receipts(previous,base,original_cases,expected):
    """Recover complete atomic stages and cases solely by exact byte/payload lineage."""
    base=Path(base)
    def read_file(path):
        raw=Path(path).read_bytes()
        return json.loads(gzip.decompress(raw) if str(path).endswith(".gz") else raw)
    def rec(path):return dict(file=str(path.relative_to(base)),bytes=path.stat().st_size,sha256=sha(path))
    def digest(value):
        return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
    def identity(value):
        if any(value.get(key)!=value0 for key,value0 in expected.items()):
            raise ValueError("a complete adjacent-piece prefix changed exact source, helper, inputs or runtime")
    allowed={"new_exact_cubic_difference_stages","new_intrinsic_consumption_stages",
        "new_reference_coefficient_norm_stages","new_piece_comparison_stages",
        "new_reference_radius_budgets","new_complete_source_rows","new_case_summaries"}
    stages=copy.deepcopy(previous.get("stages",{}));cases=copy.deepcopy(previous.get("case_stages",[]))
    audit=[];payloads={}
    for path in sorted((base/"stages").glob("*.json.gz")):
        value=read_file(path);name=value.get("stage");identity(value)
        if (not isinstance(name,str) or value.get("name")!=name or path.name!=name+".json.gz"
            or value.get("complete") is not True or value.get("stage_kind") not in allowed
            or value.get("payload_sha256")!=digest(value.get("payload"))):
            raise ValueError("an unindexed complete natural stage changed its payload identity")
        current=rec(path)
        if name in stages:
            if any(stages[name][key]!=current[key] for key in ("file","bytes","sha256")):
                raise ValueError("an already accepted immutable stage changed bytes")
        else:
            stages[name]=dict(**current,stage_kind=value["stage_kind"])
            audit.append(dict(kind="complete_stage_before_index",stage=name,receipt=current))
        payloads[name]=value["payload"]
    if set(stages)!=set(payloads):
        raise ValueError("an accepted complete natural stage is absent")
    for ci,source in enumerate(original_cases):
        old=source["document"];radius=old["exact_radius"]
        path=base/"cases"/("radius-"+radius.replace("/","-")+".json.gz")
        if not path.is_file():
            if ci<len(cases):raise ValueError("an accepted original complete case file is missing")
            break
        value=read_file(path);identity(value);current=rec(path)
        if (value.get("complete") is not True or value.get("exact_radius")!=radius
            or value.get("original_complete_case_sha256")!=source["sha256"]
            or value.get("exact_cover")!=old.get("exact_cover")):
            raise ValueError("a completed case changed its original exact identity")
        if ci<len(cases) and any(cases[ci][key]!=current[key] for key in ("file","bytes","sha256")):
            raise ValueError("an immutable indexed complete case changed bytes")
        rows=value["rows"];roles=value["row_roles"]
        if len(rows)!=len(roles) or len(rows)!=len(old["rows"]):
            raise ValueError("a complete case lost its original exact row cover")
        selection=value["selection_stage"]
        if (selection not in payloads or stages[selection]["stage_kind"]!="new_piece_comparison_stages"
            or payloads[selection].get("row_roles")!=roles
            or payloads[selection].get("original_complete_case_sha256")!=source["sha256"]):
            raise ValueError("a complete selected row ledger lacks its accepted immutable selection")
        for serial,(row,role) in enumerate(zip(rows,roles)):
            original=old["rows"][serial];kind=role["kind"]
            if (role["oldserial"]!=serial or role["original_complete_row_payload_sha256"]!=digest(original)
                or row["interval"]!=original["interval"] or row["side"]!=original["side"]):
                raise ValueError("a complete row changed its original interval or payload lineage")
            if kind in ("copied_original_complete_row","copied_original_better_complete_bound"):
                if row!=original:raise ValueError("an unchanged row differs from its full original payload")
            elif kind!="new_complete_neighbor_bound":
                raise ValueError("an unknown complete row role was supplied")
            if kind!="copied_original_complete_row":
                name=role["stage"]
                if name not in payloads or stages[name]["stage_kind"]!="new_complete_source_rows":
                    raise ValueError("a candidate complete new row lacks its independent stage")
                if role["new_complete_row_payload_sha256"]!=digest(payloads[name]):
                    raise ValueError("a candidate complete new row changed its accepted payload")
                if kind=="new_complete_neighbor_bound" and row!=payloads[name]:
                    raise ValueError("a selected complete row differs from its accepted natural source stage")
        name=value["summary_stage"]
        if (name not in payloads or stages[name]["stage_kind"]!="new_case_summaries"
            or value["complete_case_summary"]!=payloads[name]):
            raise ValueError("a complete case summary lacks its accepted independent stage")
        for key in ("original_normalized_seam_ledger","original_complete_outward_states",
                    "original_complete_case_summary"):
            if key in old and value.get(key)!=old[key]:
                raise ValueError("a complete case changed original seam or failure evidence")
        new=dict(current);new.update(accepted_rows=len(rows),complete=True)
        if ci<len(cases):cases[ci]=new
        else:
            cases.append(new);audit.append(dict(kind="complete_case_before_index",case=ci,receipt=new))
    return stages,cases,audit

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
                      str(TOPIC/'notes/correlated_adjacent_piece_first_Airy_sources_ci/')))
        subprocess.run(gitbase+['sparse-checkout', 'set', '--no-cone', '--stdin'], cwd=root,
                       input='\n'.join('/'+p for p in sorted(paths))+'\n', text=True, check=True)
        print('Hydrated '+str(len(manifest['files']))+' exact inputs preserving all original coefficients, complete norms, source rows and two true cubic neighbors.', flush=True)
        return
    if args.work is None or args.out_dir is None or args.prepared is None:
        raise ValueError('the immutable work and separate output directories are required')
    work, output = args.work.resolve(), args.out_dir.resolve()
    if work.exists() or output.exists():
        raise FileExistsError('preserve the actual output and scientific snapshot of every run')
    work.mkdir(parents=True)
    output.mkdir(parents=True)
    state = dict(kind='actual_public_correlated_adjacent_piece_first_Airy_source_execution_and_publication',
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
    state['original_same_order_matrix_conversions_recomputed']=0
    state['original_complete_Airy_profiles_recomputed']=0
    state['original_completed_auxiliary_domains_recomputed']=0
    state['original_complete_angular_tail_factors_recomputed']=0
    state['only_new_two_neighbor_correlated_difference_and_complete_source_consumption']=True
    state['new_true_root_high_order_point_evaluation_requested']=False
    state['strict_original_completed_coefficient_and_amplitude_reuse_required']=True
    state['old_root_targets_and_auxiliary_domains_recomputed']=0
    state['auxiliary_background_substituted_for_actual_neighbors']=False
    state['mathematical_source_sha256']=next(x['sha256'] for x in manifest['files']
        if x['path']==str(TOPIC/'scripts/fourfold_codazzi_adjacent_piece_correlated_first_Airy_sources.py'))
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
        target=work/spec['path']
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
               '--out-dir', str(output/'consumers')]
    # Exact reuse of completed new natural stages and recombination rows.
    expected_source=next(x['sha256'] for x in manifest['files']
        if x['path']==str(TOPIC/'scripts/fourfold_codazzi_adjacent_piece_correlated_first_Airy_sources.py'))
    expected_runtime={k:manifest['runtime'][k] for k in ('python','python_flint','numpy','scipy')}
    expected_algebra=next(x['sha256'] for x in manifest['files']
        if x['path']==str(TOPIC/'scripts/fourfold_codazzi_adjacent_piece_correlated_Airy_algebra.py'))
    expected_identity={'algebra_sha256':expected_algebra}
    expected_recovery=dict(source_sha256=expected_source,input_manifest_sha256=args.manifest_sha,
        runtime=expected_runtime,**expected_identity)
    original_cases=[]
    for ci in range(6):
        pp=work/manifest['input_paths']['whole_case_'+str(ci)]
        original_cases.append(dict(document=json.loads(gzip.decompress(pp.read_bytes())),sha256=sha(pp)))
    candidates=[]
    unavailable_matching_prefixes=[]
    previous_root=root/TOPIC/'notes/correlated_adjacent_piece_first_Airy_sources_ci'
    processes=list(previous_root.glob('*/consumers/process.json')) if previous_root.exists() else []
    explicit=args.prepared.resolve()/'resume'/'consumers'/'process.json'
    if explicit.is_file():processes.append(explicit)
    for process_path in processes:
        pd=json.loads(process_path.read_text())
        native_path=process_path.parent/'correlated-adjacent-piece-first-Airy-sources.json.gz'
        if (pd.get('public_repository')!=PUBLIC or pd.get('manifest_sha256')!=args.manifest_sha
            or pd.get('mathematical_source_sha256')!=expected_source or not native_path.is_file()):
            continue
        if sha(native_path)!=pd.get('native_sha256') or native_path.stat().st_size!=pd.get('native_bytes'):
            raise ValueError('an original complete new prefix index changed bytes')
        nd=json.loads(gzip.decompress(native_path.read_bytes()))
        if (nd.get('source_sha256')!=expected_source or nd.get('input_manifest_sha256')!=args.manifest_sha
            or nd.get('runtime')!=expected_runtime or any(nd.get(k)!=v for k,v in expected_identity.items())):
            raise ValueError('an accepted physical-piece prefix changed its scientific identity')
        if nd.get('failure') is not None:
            raise ValueError('Preserve the actual mathematical failure; a correction is required before its failed gate can run again.')
        indexed=[*nd.get('stages',{}).values(),*nd.get('case_stages',[])]
        absent=[v['file'] for v in indexed if not (native_path.parent/v['file']).is_file()]
        if absent:
            unavailable_matching_prefixes.append(dict(process=str(process_path),run_id=nd.get('run_id'),
                run_attempt=nd.get('run_attempt'),missing_original_natural_files=absent))
            continue
        adopted_stages,adopted_cases,recovery=recover_prefix_receipts(
            nd,native_path.parent,original_cases,expected_recovery)
        stages=[*adopted_stages.values(),*adopted_cases]
        counts=dict(complete_scalar_stages=0,source_rows=0,complete_cases=0,natural_stage_files=len(stages))
        missing=[]
        for entry in stages:
            relative=Path(entry['file'])
            if relative.is_absolute() or '..' in relative.parts or relative.parts[0] not in ('stages','cases'):
                raise ValueError('a completed natural source stage leaves its output directory')
            stagepath=native_path.parent/relative
            if not stagepath.is_file():
                missing.append(str(relative));continue
            if sha(stagepath)!=entry['sha256'] or stagepath.stat().st_size!=entry['bytes']:
                raise ValueError('an accepted natural source prefix changed bytes')
            sd=json.loads(gzip.decompress(stagepath.read_bytes()))
            if sd.get('source_sha256')!=expected_source or sd.get('input_manifest_sha256')!=args.manifest_sha:
                raise ValueError('a complete prefix stage changed its science or manifest')
            if relative.parts[0]=='stages':
                if not sd.get('complete'):raise ValueError('a scalar stage is not complete')
                counts['complete_scalar_stages']+=1
            else:
                rows=sd.get('rows',[]);ledger=sd.get('row_roles',[])
                if len(rows)!=len(ledger):raise ValueError('a complete source row-role ledger is missing')
                counts['source_rows']+=len(rows)
                counts['complete_cases']+=int(bool(sd.get('complete')))
        if missing:
            unavailable_matching_prefixes.append(dict(process=str(process_path.relative_to(root))
                if process_path.is_relative_to(root) else str(process_path),
                run_id=nd.get('run_id'),run_attempt=nd.get('run_attempt'),
                missing_original_natural_files=missing))
            continue
        if not counts['complete_scalar_stages'] and not counts['source_rows']:continue
        complete=bool(nd.get('complete') and nd.get('proved') and nd.get('failure') is None
            and nd.get('gates') and all(g['passed'] for g in nd['gates'])
            and counts['complete_cases']==6 and counts['complete_scalar_stages']>0)
        if complete and not (pd.get('actual_returncode')==0 or
            (pd.get('original_complete_success_reused') is True
             and pd.get('original_mathematical_actual_returncode')==0)):continue
        score=(int(complete),counts['complete_scalar_stages'],counts['source_rows'])
        candidates.append((score,complete,counts,process_path,native_path,stages,recovery))
    state['matching_prefixes_requiring_original_artifact']=unavailable_matching_prefixes
    if unavailable_matching_prefixes and not candidates:
        save(output/'worker-process.json',state)
        raise RuntimeError('A matching accepted prefix requires its complete original Actions artifact; restore it with resume_run before continuing. No mathematics was restarted.')
    if candidates:
        score,complete,counts,pp,np,stages,recovery=max(candidates,key=lambda z:z[0])
        accepted=work/'accepted-correlated-adjacent-piece-prefix';accepted.mkdir()
        resume=accepted/'correlated-adjacent-piece-first-Airy-sources.json.gz'
        shutil.copyfile(np,resume)
        if sha(resume)!=sha(np):raise ValueError('the immutable source prefix index differs')
        for entry in stages:
            source=np.parent/entry['file'];target=accepted/entry['file']
            target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,target)
            if sha(target)!=entry['sha256']:raise ValueError('an accepted natural stage changed during copy')
        command+=['--resume',str(resume),'--resume-sha',sha(resume)]
        if complete:
            original_process=accepted/'original-complete-process.json'
            shutil.copyfile(pp,original_process)
            command+=['--adopt-process',str(original_process),'--adopt-process-sha',sha(original_process)]
        evidence=output/'evidence';evidence.mkdir(exist_ok=True)
        shutil.copyfile(pp,evidence/'original-correlated-adjacent-piece-prefix-process.json')
        shutil.copyfile(np,evidence/'original-correlated-adjacent-piece-prefix-native.json.gz')
        state['actual_prefix_reuse']=dict(original_process_sha256=sha(pp),original_native_sha256=sha(resume),
            original_native_bytes=resume.stat().st_size,completed_stage_counts=counts,
            original_complete_native=complete,all_original_natural_stage_files_preserved=True,
            all_source_runtime_and_input_pins_unchanged=True,
            original_native_index_copied_byte_identically=True,atomic_receipt_reconciliation=recovery)
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
    report = root/TOPIC/'notes/correlated_adjacent_piece_first_Airy_sources_ci'/('run-'+state['run_id']+'-'+state['run_attempt'])
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
    git('commit', '-m', 'visible-exact: consume correlated complete sources on the two true neighboring pieces')
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
                          old_root_targets_and_auxiliary_domains_recomputed=False, original_complete_norms_and_exterior_sources_reused=True, complete_correlated_adjacent_piece_prefixes_preserved=True, physical_background_replaced=False, report=owned)), flush=True)
    if not state['complete']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
