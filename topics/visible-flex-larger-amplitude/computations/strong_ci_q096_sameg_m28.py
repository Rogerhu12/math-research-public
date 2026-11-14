#!/usr/bin/env python3
"""Restore the published accepted q096, freeze it genuinely, then refine M28.

No accepted M24 BVP is repeated. Original 63-file published evidence is checked
locally (including losslessly published gzip logs), with no claim to a fresh
artifact ZIP download. A real zero-worker 27-to-24 RMS/BC check precedes the
same-g M28 actual solve. All stages are sequential and have their own wait4
record. Source/config/old data stay unchanged, and MJS are never edited.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import ast
import datetime
import gzip
import hashlib
import json
from pathlib import Path
import platform
import re
import subprocess
import sys
import time

TOPIC=Path('topics/visible-flex-larger-amplitude')
STEM='notes/2026-11-12-strong-actual-q096-ci-actions-43302113873-1-strong'
MANIFEST_SHA='cba8f854bd6cbc2c64ff68e7c96a2c956aac6a4379a0a235edefd084a67f5be6'
SOURCE_REVISION='869436630c99aa5a68afb55bd8877c826034d117'
DEPENDENCIES_SHA='7de25376ab0ec10277840ccdca8ec6b46b41bee6add97acd9d38c06bbc8cd941'
SOURCE_LOCKS={
    "strong_sameg_spectral_refinement.py": "65e81c73707c6f094ce5d494965d2fd468e971f4fa450d88513cf4ac622476fd",
    "strong_sameg_actual_comparison.py": "7c152306f09faf7de890377af4f69406677c374ed707b2bc2e391208c8d57f57",
    "root_actual_freeze_design_view.py": "4209f87b8cae531f8899c5fa9af48a13666411c340981ae759daa9034315628b",
    "strong_foreground_resource_run.py": "e683fbbeb1eb579d07799acbdd08b2254917e49209566c28a85628eb9cb72bc6",
    "strong_interior_jet_audit.py": "1b7f45785fffc41595eda9aae844c3081d2954d3ea08ac0da6e5a90c935294fa",
    "root_actual_seam_audit.py": "c084d31f8671434ce393d778507103c1b786353812126d60dbcd6db9fce2bb87"
}
SELF_SHA=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    path=Path(path);data=path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix=='.gz' else data)


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def write_new(path,value):
    data=(json.dumps(value,indent=2,allow_nan=False)+'\n').encode()
    if len(data)>=100_000:
        raise ValueError('Bounded bootstrap record exceeded 100 KB: '+str(path))
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('xb') as stream:
        stream.write(data)


def clean_authentication():
    removed=[]
    for key in list(os.environ):
        if (key in ('GH_TOKEN','GITHUB_TOKEN','GH_ENTERPRISE_TOKEN','GIT_ASKPASS','SSH_ASKPASS')
                or key.startswith('GIT_CONFIG_')):
            removed.append(key);os.environ.pop(key,None)
    # Only key names are reported; environment values are never recorded.
    return sorted(removed)


def materialize(repo,relative):
    relative=Path(relative)
    if relative.is_absolute() or '..' in relative.parts:
        raise ValueError('Repository paths must be safe and relative')
    path=repo/relative
    if path.is_file():
        return path
    if path.exists() or path.is_symlink():
        raise FileExistsError('A nonfile occupies the required source path: '+str(path))
    # Normal Git binary materialization is used only in an actual local/CI
    # checkout. No oversized binary is routed through the connector.
    data=subprocess.check_output(['git','show','HEAD:'+relative.as_posix()],cwd=repo)
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('xb') as stream:
        stream.write(data)
    return path


def gzip_owned_log(path):
    if not path.is_file():
        return None
    data=path.read_bytes();target=path.with_name(path.name+'.gz')
    encoded=gzip.compress(data,mtime=0)
    if len(encoded)>=5_000_000:
        raise ValueError('Owned compressed log exceeds the repository file limit')
    if target.exists():
        if gzip.decompress(target.read_bytes())!=data:
            raise FileExistsError('Different pre-existing compressed owned log')
    else:
        target.write_bytes(encoded)
    if gzip.decompress(target.read_bytes())!=data:
        raise ValueError('Owned log compression did not preserve exact bytes')
    path.unlink()
    return dict(file=str(target),sha256=sha(target),bytes=target.stat().st_size,
                original_bytes=len(data),original_sha256=hashlib.sha256(data).hexdigest())


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,required=True)
    parser.add_argument('--work-root',type=Path,required=True)
    parser.add_argument('--run-id',required=True)
    parser.add_argument('--source-topic',type=Path)
    parser.add_argument('--phase',choices=('inputs','freeze','all'),default='all')
    parser.add_argument('--node-heap',type=int,default=128)
    parser.add_argument('--max-nodes',type=int,default=3200)
    args=parser.parse_args()
    if not re.fullmatch(r'[A-Za-z0-9_-]{1,90}',args.run_id):
        raise ValueError('Use a fresh simple run identifier')
    repo=args.repo.resolve();topic=repo/TOPIC
    if not topic.is_dir():
        raise FileNotFoundError(topic)
    os.chdir(topic)
    stem=Path('notes/2026-11-12-strong-q096-sameg-m28-'+args.run_id)
    if list(stem.parent.glob(stem.name+'*')):
        raise FileExistsError('Use a fresh bootstrap run prefix')
    work=args.work_root.resolve()/('strong-sameg-m28-'+args.run_id)
    work.mkdir(parents=True,exist_ok=False)
    records=[];started=time.monotonic();stage_resources=[]
    descriptor=materialize(repo,TOPIC/(STEM+'-ci-stable-files.json'))
    if sha(descriptor)!=MANIFEST_SHA:
        raise ValueError('The exact original accepted-output manifest changed')
    original_manifest=read(descriptor)
    if len(original_manifest['files'])!=63:
        raise ValueError('Expected all original 63 accepted-output entries')
    for row in original_manifest['files']:
        relative=Path(row['path'])
        if (relative.is_absolute() or '..' in relative.parts or
                not relative.as_posix().startswith(STEM)):
            raise ValueError('Original artifact entry escaped its exact accepted prefix')
        target=topic/relative;source=target;decompressed=False
        if not source.is_file():
            compressed=target.with_name(target.name+'.gz')
            if compressed.is_file() and target.suffix in ('.log','.jsonl'):
                source=compressed;decompressed=True
            else:
                try:
                    source=materialize(repo,TOPIC/relative)
                except subprocess.CalledProcessError:
                    if target.suffix not in ('.log','.jsonl'):
                        raise
                    source=materialize(repo,TOPIC/Path(str(relative)+'.gz'))
                    decompressed=True
        data=source.read_bytes()
        if decompressed:
            data=gzip.decompress(data)
        if len(data)!=row['bytes'] or hashlib.sha256(data).hexdigest()!=row['sha256']:
            raise ValueError('Published accepted bytes differ: '+str(relative))
        records.append(dict(original_path=str(relative),published_path=str(source.relative_to(topic)),
            original_sha256=row['sha256'],original_bytes=row['bytes'],exact_original_bytes_verified=True,
            publication_gzip_decoded_for_verification=decompressed))
    primary=Path(STEM+'.json.gz');raw=Path(STEM+'-raw-collocation.json.gz')
    config=Path(STEM+'-config.json');tail=Path(STEM+'-tail-response_0003.json.gz')
    accepted=read(primary);terminal=read(Path(STEM+'-ci-terminal.json'))
    if (not accepted.get('solver_success') or accepted.get('audit_pending',True) or
            terminal.get('solver_success') is not True or terminal.get('audit_pending') is not False or
            terminal['owned_wait4_record'].get('exitcode')!=0 or
            terminal['owned_wait4_record'].get('termination_signal') is not None or
            terminal['owned_wait4_record'].get('wait4_observed') is not True):
        raise ValueError('The original q096 mathematical and formal terminal evidence is incomplete')
    if accepted['actual_tail']['final_response'].split('/')[-1]!=tail.name:
        raise ValueError('The exact accepted final response number changed')
    source_manifest=materialize(repo,TOPIC/'computations/source-dependencies.json')
    if sha(source_manifest)!=DEPENDENCIES_SHA:
        raise ValueError('Pinned 91-source descriptor changed')
    deps=read(source_manifest)
    if deps['source_revision']!=SOURCE_REVISION or len(deps['files'])!=91:
        raise ValueError('The complete pinned source revision is required')
    if args.source_topic:
        source_topic=args.source_topic.resolve();source_root=source_topic.parents[1]
    else:
        restorer=materialize(repo,TOPIC/'computations/prepare-source-dependencies.py')
        source_root=work/'source'
        restore=subprocess.run([sys.executable,str(restorer),'--repo',str(repo),'--dest',str(source_root)],
            cwd=topic,check=False)
        if restore.returncode:
            raise RuntimeError('Normal pinned Git source restoration failed')
        source_topic=source_root/'topics/visible-flexible-closed-surface'
    for item in deps['files']:
        path=source_root/item['path']
        if not path.is_file() or path.stat().st_size!=item['bytes'] or sha(path)!=item['sha256']:
            raise ValueError('Pinned source bytes differ: '+item['path'])
    supporting=[
        'computations/alternative-neck-provider-smallcut30-port32-r2048.json',
        'notes/2026-11-12-root-vu032-q085-fixed-actual-m20-staged-audit-ready.json',
        'notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json']
    for relative in supporting:
        materialize(repo,TOPIC/relative)
    for name,expected in SOURCE_LOCKS.items():
        path=materialize(repo,TOPIC/'computations'/name)
        if sha(path)!=expected:
            raise ValueError('Prepared source SHA mismatch: '+name)
        ast.parse(path.read_text(),filename=str(path))
    removed=clean_authentication()
    import numpy as np
    import scipy
    observed=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__)
    expected=dict(python='3.12.14',numpy='2.3.5',scipy='1.17.0')
    if observed!=expected:
        raise ValueError('Explicit original numerical runtime differs: '+repr(observed))
    restoration=dict(scope='Original accepted q096 restored from published Git files',
        entry_sha256=SELF_SHA,created_utc=utc(),source_manifest_sha256=MANIFEST_SHA,
        original_63_files=records,all_63_exact_original_bytes_verified=True,
        artifact_zip_downloaded_or_rechecked=False,
        original_artifact_id=13983440730,
        original_artifact_sha256='27c0e11f6ab2c0fc45338dd186c0fdd36cfe7f2f962f1b849f509708054331fb',
        original_artifact_hash_is_prior_record_not_a_new_zip_check=True,
        original_M24_recomputed=False,old_r7_session80885_terminal='unknown',
        original_solver_success=True,original_audit_pending=False,
        pinned_source_revision=SOURCE_REVISION,pinned_source_files=91,
        pinned_source_bytes=sum(item['bytes'] for item in deps['files']),
        numerical_runtime=observed,authentication_environment_key_names_removed=removed,
        no_authentication_values_recorded=True,prepared_source_sha256=SOURCE_LOCKS)
    write_new(Path(str(stem)+'-published-restoration.json'),restoration)
    if args.phase=='inputs':
        print(json.dumps(dict(event='same_g_M28_inputs_verified',phase='inputs',new_numerics=False)),flush=True)
        return
    port='computations/alternative-neck-provider-smallcut30-port32-r2048.json'
    frozen_ready='notes/2026-11-12-root-vu032-q085-fixed-actual-m20-staged-audit-ready.json'
    frozen_ledger='notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json'
    fixed=Path(str(stem)+'-fixed24')
    final=Path(str(stem)+'-actual28')
    command_plan=dict(entry_sha256=SELF_SHA,source_revision=SOURCE_REVISION,
        original_accepted_M24=str(primary),do_not_recompute_original_M24=True,
        fixed_profile=accepted['frozen_profile'],original_reference_t=accepted['numerical_meridian_chart']['reference_t'],
        phase=args.phase,source_topic=str(source_topic),stages=[],status='sequential execution prepared')
    plan_path=Path(str(stem)+'-commands.json')

    def execute(label,command):
        output=Path(str(stem)+'-'+label)
        resource=Path(str(output)+'-resource.json')
        heartbeat=Path(str(output)+'-heartbeat.jsonl')
        ownership=Path(str(output)+'-ownership.json')
        log=Path(str(output)+'.log')
        wrapped=[sys.executable,'-u','computations/strong_foreground_resource_run.py',
            '--out',str(resource),'--heartbeat',str(heartbeat),'--ownership',str(ownership),
            '--task-prefix',str(output),'--heartbeat-seconds','20','--',*command]
        command_plan['stages'].append(dict(label=label,command=command,resource=str(resource),
                                           log=str(log),status='before-start'))
        plan_path.write_text(json.dumps(command_plan,indent=2)+'\n')
        print(json.dumps(dict(event='same_g_M28_stage_start',label=label,command=command)),flush=True)
        with log.open('xb') as stream:
            result=subprocess.run(wrapped,cwd=topic,stdout=stream,stderr=subprocess.STDOUT,check=False)
        record=read(resource) if resource.is_file() else None
        log_data=log.read_bytes()
        compressed=gzip_owned_log(log)
        stage=dict(label=label,supervisor_returncode=result.returncode,
                   owned_wait4_record=record,log=compressed)
        stage_resources.append(stage)
        command_plan['stages'][-1].update(status='formally-returned',supervisor_returncode=result.returncode,
            owned_exitcode=record.get('exitcode') if record else None,
            owned_termination_signal=record.get('termination_signal') if record else None)
        plan_path.write_text(json.dumps(command_plan,indent=2)+'\n')
        print(json.dumps(dict(event='same_g_M28_stage_returned',label=label,returncode=result.returncode,
            exitcode=record.get('exitcode') if record else None,
            signal=record.get('termination_signal') if record else None)),flush=True)
        if (result.returncode!=0 or not record or record.get('exitcode')!=0 or
                record.get('termination_signal') is not None or not record.get('wait4_observed')):
            print(log_data[-12000:].decode('utf-8',errors='replace'),flush=True)
            raise RuntimeError('A formal owned stage did not complete: '+label)
        return stage

    status='running';failure=None
    try:
        freeze_cmd=[sys.executable,'-u','computations/root_actual_freeze_design_view.py',
            '--design-checkpoint',str(primary),'--design-raw',str(raw),'--design-tail',str(tail),
            '--fixed-view-prefix',str(fixed),'--radial-batch-size','8',
            '--source-topic',str(source_topic),'--port',port,'--tail-config',str(config)]
        execute('fixed-view',freeze_cmd)
        fixed_report=read(Path(str(fixed)+'-report.json'))
        if (fixed_report.get('original_parameter_count')!=27 or fixed_report.get('fixed_parameter_count')!=24 or
                fixed_report.get('counters')!={'raw_restorations':1,'residual_checks':1,'tail_start_attempts':0}):
            raise ValueError('The genuine 27-to-24 zero-worker check did not finish')
        if args.phase=='freeze':
            status='fixed-view-only-complete'
            return
        node_version=subprocess.check_output(['node','--version'],text=True).strip()
        if node_version!='v24.22.1':
            raise ValueError('The explicit Node runtime differs: '+node_version)
        temporary=work/'disk';temporary.mkdir()
        refine=[sys.executable,'-u','computations/strong_sameg_spectral_refinement.py',
            '--spectral-fixed-raw',str(fixed)+'-raw-collocation.json.gz',
            '--spectral-fixed-report',str(fixed)+'-report.json',
            '--spectral-warm-tail',str(tail),'--spectral-baseline-config',str(config),
            '--spectral-temporary-parent',str(temporary),'--spectral-node-young-space','4',
            '--fixed-reference',str(fixed)+'.json.gz',
            '--frozen-reference-ready',frozen_ready,'--frozen-calibration-ledger',frozen_ledger,
            '--source-topic',str(source_topic),'--port',port,
            '--out-prefix',str(final),'--modes','28','--angular','1024',
            '--tol','1e-7','--max-nodes',str(args.max_nodes),'--node-heap',str(args.node_heap)]
        execute('spectral-prepare',[*refine,'--spectral-prepare-only'])
        execute('actual28',refine)
        result=read(Path(str(final)+'-summary.json'))
        if not result.get('solver_success') or result.get('audit_pending',True):
            raise ValueError('M28 original actual acceptance was not paid')
        packet=Path(result['actual_tail']['final_response'])
        if not packet.is_absolute():
            packet=topic/packet
        packet=packet.resolve()
        if packet.parent!=topic/'notes' or not packet.name.startswith(final.name+'-tail-response_'):
            raise ValueError('The actual final response escaped the fresh output prefix')
        if not packet.is_file():
            raise FileNotFoundError(packet)
        for label,checkpoint in (('interior24',Path(str(fixed)+'.json.gz')),
                                 ('interior28',Path(str(final)+'.json.gz'))):
            execute(label,[sys.executable,'-u','computations/strong_interior_jet_audit.py',
                '--input',str(checkpoint),'--source-topic',str(source_topic),'--port',port,
                '--angular','1536','--batch','8','--radial','801',
                '--out',str(stem)+'-'+label+'.json'])
        execute('full-seam28',[sys.executable,'-u','computations/root_actual_seam_audit.py',
            '--checkpoint',str(final)+'.json.gz','--tail-response',str(packet),
            '--source-topic',str(source_topic),'--port',port,'--angular','768','1536',
            '--out',str(stem)+'-full-seam28.json'])
        execute('comparison',[sys.executable,'-u','computations/strong_sameg_actual_comparison.py',
            '--coarse',str(fixed)+'.json.gz','--fine',str(final)+'.json.gz',
            '--source-topic',str(source_topic),'--port',port,'--angular','768','--batch','8',
            '--out',str(stem)+'-comparison.json'])
        a24=read(Path(str(stem)+'-interior24.json'));a28=read(Path(str(stem)+'-interior28.json'))
        seam=read(Path(str(stem)+'-full-seam28.json'));comparison=read(Path(str(stem)+'-comparison.json'))
        scientific_keys=('metric_l1','flow_defect','darboux_l1','kappa_sample','rmax','heightmax',
                         'root_min','chart_rho_min','physical_bc')
        brief=dict(scope='Accepted same-g finite M24-to-M28 spectral refinement and actual quintic audits',
            new_solve='M28 only; original accepted M24 recovered and zero-worker frozen',
            entry_sha256=SELF_SHA,solver_success=True,audit_pending=False,
            physical_profile_unchanged=(result['frozen_profile']==accepted['frozen_profile']),
            gauge=result['gauge_amplitude'],actual_primary_amplitude=result['actual_primary_amplitude'],
            modes=result['modes'],nodes=result['nodes'],RMS=result['max_rms_collocation_residual'],
            full_core=result['core'],physical_profile=result['frozen_profile'],
            default_summary={key:result.get('summary',{}).get(key) for key in scientific_keys},
            complete_tail_residual=result['actual_tail']['residual'],
            complete_final_response=dict(file=str(packet),sha256=sha(packet)),
            coarse_interior=a24['top'],fine_interior=a28['top'],full_Cartesian_mean_seam=seam['rows'],
            same_g_material_point_and_two_jet_comparison=comparison['comparison'],
            exact_closure_or_continuous_C2_or_reach_claim=False)
        write_new(Path(str(stem)+'-brief.json'),brief)
        status='complete-original-gates-and-finite-postaudits'
    except BaseException as error:
        failure=repr(error);status='failed-or-interrupted-after-recorded-stages'
        raise
    finally:
        summary=dict(scope=__doc__,entry_sha256=SELF_SHA,status=status,error=failure,
            started_as_fresh_run=args.run_id,finished_utc=utc(),seconds=time.monotonic()-started,
            original_M24_recomputed=False,old_r7_terminal_still_unknown=True,
            new_M28_result_not_inferred_from_exit=True,stages=stage_resources)
        write_new(Path(str(stem)+'-bootstrap-terminal.json'),summary)
        files=[]
        for path in sorted(stem.parent.glob(stem.name+'*')):
            if not path.is_file() or path.name.endswith('-stable-files.json'):
                continue
            if path.suffix in ('.log','.jsonl'):
                compressed=gzip_owned_log(path)
                path=Path(compressed['file'])
            size=path.stat().st_size
            if size>=5_000_000:
                raise ValueError('An output exceeds the original single-file gate: '+str(path))
            files.append(dict(path=str(path),bytes=size,sha256=sha(path)))
        # Rows refer only to files made by this fresh bootstrap prefix.
        unique={row['path']:row for row in files}
        write_new(Path(str(stem)+'-stable-files.json'),dict(
            scope='Immutable completed prefix after the current supervisor returned',
            status=status,files=[unique[key] for key in sorted(unique)]))


if __name__=='__main__':
    main()
