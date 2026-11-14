#!/usr/bin/env python3
"""Fresh local same-g M28 bootstrap using an owned small runtime and two disks.

The accepted q096 is restored by links to exact published bytes. No original
M24 BVP is rerun. The original serial bootstrap runs unchanged; exactly its two
M28 prepare/solve child commands are routed through a directory-only storage
wrapper. No old checkout/index, MJS, scientific gate or cache key is modified.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import ast
import datetime
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import time

HERE=Path(__file__).resolve().parent
SELF_SHA=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
TOPIC=Path('topics/visible-flex-larger-amplitude')
ORIGINAL='notes/2026-11-12-strong-actual-q096-ci-actions-43302113873-1-strong'
BOOTSTRAP_SHA='77903999c2a1beb3101fb15de27829c330db4121deee1463c145d8d27cd98422'
SPLIT_SHA='4cfec7a654611d94f54e6c17ef8580c9a04c775adce65ed35c561efd3194f437'
MANIFEST_SHA='cba8f854bd6cbc2c64ff68e7c96a2c956aac6a4379a0a235edefd084a67f5be6'
SOURCE_SHA='7de25376ab0ec10277840ccdca8ec6b46b41bee6add97acd9d38c06bbc8cd941'


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def write_new(path,value):
    data=(json.dumps(value,indent=2,allow_nan=False)+'\n').encode()
    if len(data)>=100000:
        raise ValueError('Local launcher record exceeded100KB')
    with Path(path).open('xb') as stream:
        stream.write(data);stream.flush();os.fsync(stream.fileno())


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--frozen-runtime',type=Path,required=True)
    parser.add_argument('--owned-root',type=Path,required=True)
    parser.add_argument('--matrix-parent',type=Path,required=True)
    parser.add_argument('--source-topic',type=Path,required=True)
    parser.add_argument('--run-id',required=True)
    parser.add_argument('--source-reference',required=True)
    parser.add_argument('--phase',choices=('inputs','freeze','all'),default='all')
    args=parser.parse_args()
    if not re.fullmatch(r'[A-Za-z0-9_-]{1,90}',args.run_id):
        raise ValueError('Fresh simple run ID required')
    if not re.fullmatch(r'[0-9a-f]{40}',args.source_reference):
        raise ValueError('Record the parent-provided exact frozen source commit')
    frozen=args.frozen_runtime.resolve();source_topic=args.source_topic.resolve()
    owned=args.owned_root.resolve();matrix_parent=args.matrix_parent.resolve()
    if owned.exists() or matrix_parent.exists():
        raise FileExistsError('Owned root and matrix parent must both be fresh; do not touch unknown old runs')
    original_topic=frozen/TOPIC;original_computations=original_topic/'computations'
    bootstrap_file=original_computations/'strong_ci_q096_sameg_m28.py'
    if digest(bootstrap_file)!=BOOTSTRAP_SHA or digest(HERE/'strong_sameg_split_storage.py')!=SPLIT_SHA:
        raise ValueError('The locked bootstrap/split source differs')
    descriptor=original_topic/(ORIGINAL+'-ci-stable-files.json')
    if digest(descriptor)!=MANIFEST_SHA:
        raise ValueError('The accepted original63 descriptor differs')
    old_manifest=read(descriptor)
    if len(old_manifest['files'])!=63:
        raise ValueError('Expected exactly the original63 accepted entries')
    dependency=original_computations/'source-dependencies.json'
    if digest(dependency)!=SOURCE_SHA:
        raise ValueError('The original91 source manifest differs')
    dependencies=read(dependency);source_root=source_topic.parents[1]
    if len(dependencies['files'])!=91 or dependencies['source_revision']!='869436630c99aa5a68afb55bd8877c826034d117':
        raise ValueError('The pinned91-source identity differs')
    for item in dependencies['files']:
        path=source_root/item['path']
        if not path.is_file() or path.stat().st_size!=item['bytes'] or digest(path)!=item['sha256']:
            raise ValueError('An existing pinned source is absent/different: '+item['path'])
    removed=[]
    for key in list(os.environ):
        if (key in ('GH_TOKEN','GITHUB_TOKEN','GH_ENTERPRISE_TOKEN','GIT_ASKPASS','SSH_ASKPASS')
                or key.startswith('GIT_CONFIG_')):
            removed.append(key);os.environ.pop(key,None)
    owned.mkdir(parents=True,exist_ok=False)
    matrix_parent.mkdir(parents=True,exist_ok=False)
    repo=owned/'runtime';topic=repo/TOPIC
    computations=topic/'computations';notes=topic/'notes'
    computations.mkdir(parents=True);notes.mkdir()
    work=owned/'work-root';work.mkdir()
    factor_parent=owned/'factor-arena';factor_parent.mkdir()
    linked_sources=0
    for original in sorted(original_computations.iterdir()):
        if original.is_file() and original.name!='strong_sameg_split_storage.py':
            (computations/original.name).symlink_to(original.resolve())
            linked_sources+=1
    # The small split helper is a real owned file, so its HERE is the owned
    # computations directory even when this launcher was restored separately.
    split_file=computations/'strong_sameg_split_storage.py'
    shutil.copyfile(HERE/'strong_sameg_split_storage.py',split_file)
    if digest(split_file)!=SPLIT_SHA:
        raise ValueError('Owned split helper bytes differ')
    linked=[]
    def link_note(relative):
        relative=Path(relative)
        if relative.is_absolute() or '..' in relative.parts or relative.parts[0]!='notes':
            raise ValueError('Only declared local note paths may be linked')
        original=original_topic/relative
        if not original.is_file():
            raise FileNotFoundError(original)
        target=topic/relative;target.parent.mkdir(parents=True,exist_ok=True)
        if target.exists() or target.is_symlink():
            if not target.is_file() or target.resolve()!=original.resolve():
                raise FileExistsError(target)
            return
        target.symlink_to(original.resolve())
        linked.append(str(relative))
    link_note(ORIGINAL+'-ci-stable-files.json')
    for row in old_manifest['files']:
        relative=Path(row['path'])
        if relative.is_absolute() or '..' in relative.parts or not relative.as_posix().startswith(ORIGINAL):
            raise ValueError('Original accepted path escaped its exact prefix')
        if (original_topic/relative).is_file():
            link_note(relative)
        elif relative.suffix in ('.log','.jsonl') and (original_topic/Path(str(relative)+'.gz')).is_file():
            link_note(str(relative)+'.gz')
        else:
            raise FileNotFoundError(original_topic/relative)
    for relative in (
        'notes/2026-11-12-root-vu032-q085-fixed-actual-m20-staged-audit-ready.json',
        'notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json'):
        link_note(relative)
    for path in (Path(__file__),HERE/'strong_sameg_split_storage.py',bootstrap_file):
        ast.parse(path.read_text(),filename=str(path))
    stem=notes/('2026-11-12-strong-q096-sameg-m28-'+args.run_id)
    routes=[];started=time.monotonic();failure=None
    provenance=dict(scope=__doc__,created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        entry_sha256=SELF_SHA,bootstrap_sha256=BOOTSTRAP_SHA,split_sha256=SPLIT_SHA,
        frozen_runtime=str(frozen),parent_provided_source_reference=args.source_reference,
        source_reference_not_inferred_by_this_non_git_overlay=True,
        original63_descriptor_sha256=MANIFEST_SHA,pinned_source_manifest_sha256=SOURCE_SHA,
        all91_existing_source_bytes_verified=True,source_topic=str(source_topic),
        owned_repo=str(repo),owned_work_root=str(work),matrix_parent=str(matrix_parent),
        factor_parent=str(factor_parent),all_new_numerical_outputs_under=str(notes),
        linked_existing_sources=linked_sources,linked_existing_notes=linked,
        authentication_key_names_removed=sorted(removed),authentication_values_never_recorded=True,
        no_git_or_API_restore_required=True,MJS_sources_changed=False,
        original_M24_BVP_repeated=False,old_r7_session80885_terminal='unknown',
        dimensions=dict(initial_nodes=2181,modes=28,angular=1024,tol=1e-7,max_nodes=3200),
        storage=dict(initial_matrix_bytes=293515200,initial_QR_bytes=546754680,
            initial_total_temporary_bytes=840269880,
            max3200_matrix_bytes=430713360,max3200_QR_bytes=802442160,
            boundary_blocks_are_resident_not_file_bytes=True),
        free_bytes_observed=dict(matrix=shutil.disk_usage(matrix_parent).free,
                                factor=shutil.disk_usage(factor_parent).free),
        child_routes=routes)
    prelude=owned/'launcher-prelude.json';write_new(prelude,provenance)
    print(json.dumps(dict(event='local_M28_runtime_ready',owned_repo=str(repo),
        original63_links_ready=True,source91_exact=True,storage=provenance['storage'],
        free_bytes=provenance['free_bytes_observed'])),flush=True)
    original_run=subprocess.run
    route_stream=(owned/'launcher-routes.jsonl').open('x')
    target='computations/strong_sameg_spectral_refinement.py'
    def routed_run(command,*positional,**kwargs):
        if isinstance(command,(list,tuple)) and target in command:
            if command.count(target)!=1 or 'computations/strong_foreground_resource_run.py' not in command or '--' not in command:
                raise ValueError('Unexpected spectral child command; no broad process interception is allowed')
            changed=list(command);index=changed.index(target)
            if index<=changed.index('--'):
                raise ValueError('The spectral child is not inside its owned original wait4 supervisor')
            changed[index:index+1]=['computations/strong_sameg_split_storage.py',
                '--split-matrix-parent',str(matrix_parent),
                '--split-factor-parent',str(factor_parent)]
            row=dict(original_command=list(command),actual_command=changed,
                scope='Only owned storage wrapper added; original remaining spectral arguments preserved')
            routes.append(row);route_stream.write(json.dumps(row)+'\n');route_stream.flush();os.fsync(route_stream.fileno())
            print(json.dumps(dict(event='local_M28_storage_route',prepare='--spectral-prepare-only' in changed,
                actual_command=changed)),flush=True)
            return original_run(changed,*positional,**kwargs)
        return original_run(command,*positional,**kwargs)
    spec=importlib.util.spec_from_file_location('strong_original_M28_bootstrap',bootstrap_file)
    bootstrap=importlib.util.module_from_spec(spec);sys.modules[spec.name]=bootstrap
    spec.loader.exec_module(bootstrap)
    prior_argv=sys.argv;subprocess.run=routed_run
    sys.argv=[str(bootstrap_file),'--repo',str(repo),'--work-root',str(work),
        '--run-id',args.run_id,'--source-topic',str(source_topic),
        '--phase',args.phase,'--node-heap','128','--max-nodes','3200']
    try:
        bootstrap.main()
        if len(routes)!=(2 if args.phase=='all' else 0):
            raise RuntimeError('The original expected number of spectral child routes did not complete')
    except BaseException as error:
        failure=repr(error)
        raise
    finally:
        sys.argv=prior_argv;subprocess.run=original_run;route_stream.close()
        provenance.update(seconds=time.monotonic()-started,error=failure,
            bootstrap_returned=True,child_routes=routes,
            scientific_success_is_only_in_original_bootstrap_and_summary=True)
        final_record=Path(str(stem)+'-local-launcher.json')
        write_new(final_record,provenance)
        print(json.dumps(dict(event='local_M28_launcher_returned',error=failure,
            record=str(final_record),original_bvp_result_not_inferred=True)),flush=True)


if __name__=='__main__':
    main()
