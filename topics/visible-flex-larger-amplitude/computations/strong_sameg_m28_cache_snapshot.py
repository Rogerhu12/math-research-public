#!/usr/bin/env python3
"""Prepare a real-file M28 cache runtime from existing owned task data.

This copies bytes and checks hashes. It never alters an old snapshot, Git ref,
MJS source or mathematical parameter. A prepared command starts only the
already defined diagnostic/full-H tail path; it never repeats prefix Newton.
Only --execute-diagnostic replaces this small process with the owned resource
supervisor. No numerical process is started in the default preparation mode.
"""
from __future__ import annotations
import argparse
import ast
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys

TOPIC_NAME='visible-flex-larger-amplitude'
STEM='2026-11-12-strong-q096-sameg-m28-local-recovery6-r1'
READY='2026-11-13-strong-q096-sameg-m28-local-recovery6-r2-tail-ready.json'
READY_SHA='4c03e39776031a81935be8b884740f800b4967e90efca6b3612350676832f1a2'
LEDGER='2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json'
MANIFEST_SHA='42bcef485ba3e1aabbfbe843fbbce1a07a41ffe286b42b7ef83a000256ef4c1f'
PINNED_REV='869436630c99aa5a68afb55bd8877c826034d117'
PINNED_MANIFEST='7de25376ab0ec10277840ccdca8ec6b46b41bee6add97acd9d38c06bbc8cd941'
OWN={
 'strong_sameg_m28_staged_audit.py':'2bfd570f1497022767b0736d099ab42d248cd492a8914f3c69707fed3ef6bf8f',
 'strong_sameg_m28_cached_audit.py':'f10443df29783d0128ebcdbf660904bb5981503d292d336900d5a39a79ab2eda',
 'strong_observed_foreground_resource_run.py':'a9c8822148dec0f39e396effc9602e51adbe5e58a81e99952b45fd9e3044566d',
 'strong_sameg_m28_postprocess.py':'80044bf34cb90b104149e4c212647f322dce1d59dac6fe1ba7723d8ba60b5277',
 'strong_sameg_m28_complete.py':'905e256ab7e51364fe36cefb293f9d8198eae96ac2dca72e08d91993eeb48da1',
 'strong_tail_young_space_guard.py':'867244ef03a99ea50f7629d437873c073e9a07ee8a88b48568c79817be7b7eba',
}
SELF_SHA=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def sha(file):
    h=hashlib.sha256()
    with Path(file).open('rb') as stream:
        for block in iter(lambda:stream.read(1<<20),b''):h.update(block)
    return h.hexdigest()


def read(file):
    p=Path(file)
    return json.loads(gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes())


def write_new(file,value):
    p=Path(file);p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('x') as stream:stream.write(json.dumps(value,indent=2,allow_nan=False)+'\n')


def leafs(root,stack=()):
    root=Path(root)
    resolved=root.resolve(strict=True)
    if resolved in stack:raise ValueError('Cycle in explicitly supplied source tree')
    for item in sorted(root.iterdir(),key=lambda p:p.name):
        if item.name in ('__pycache__','.git'):continue
        if item.is_dir():yield from leafs(item,(*stack,resolved))
        elif item.is_file():yield item
        else:raise ValueError('Only complete regular source files may be copied: '+str(item))


def copy_tree_real(src,dst,limit):
    src,dst=Path(src),Path(dst)
    files=list(leafs(src))
    size=sum(p.stat().st_size for p in files)
    if size>limit:raise ValueError('Explicit source-copy budget exceeded')
    rows=[]
    for source in files:
        relative=source.relative_to(src);target=dst/relative
        target.parent.mkdir(parents=True,exist_ok=True)
        expected=sha(source);shutil.copyfile(source,target)
        if target.is_symlink() or sha(target)!=expected:
            raise ValueError('Source copy is not byte identical: '+str(relative))
        rows.append(dict(path=str(relative),bytes=target.stat().st_size,sha256=expected))
    return dict(input=str(src),output=str(dst),bytes=size,files=rows)


def checked_copy(src,dst,expected=None):
    src,dst=Path(src),Path(dst)
    digest=sha(src)
    if expected is not None and digest!=expected:
        raise ValueError('Input hash differs: '+str(src))
    if dst.is_symlink():dst.unlink()
    elif dst.exists():raise FileExistsError('Fresh copied input required: '+str(dst))
    dst.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(src,dst)
    if sha(dst)!=digest:raise ValueError('Copied input hash differs')
    return dict(path=str(dst),bytes=dst.stat().st_size,sha256=digest)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input-topic',type=Path,required=True)
    p.add_argument('--input-source-topic',type=Path,required=True)
    p.add_argument('--work-root',type=Path,required=True)
    p.add_argument('--run-label',required=True)
    p.add_argument('--python',type=Path,default=Path(sys.executable))
    p.add_argument('--overlay-source',action='append',default=[],metavar='NAME=PATH')
    p.add_argument('--max-source-bytes',type=int,default=134217728)
    p.add_argument('--execute-diagnostic',action='store_true')
    a=p.parse_args()
    if not re.fullmatch(r'[a-zA-Z0-9][a-zA-Z0-9._-]{0,99}',a.run_label):
        raise ValueError('A short fresh literal run label is required')
    input_topic=a.input_topic.resolve(strict=True)
    input_source=a.input_source_topic.resolve(strict=True)
    work=a.work_root.absolute()
    if work.exists():raise FileExistsError('Use a fresh owned work root')
    manifest_file=input_topic/'notes'/(STEM+'-stable-files.json')
    if sha(manifest_file)!=MANIFEST_SHA:raise ValueError('Original complete M28 manifest differs')
    manifest=read(manifest_file)
    if len(manifest['files'])!=60 or sum(r['bytes'] for r in manifest['files'])!=22213737:
        raise ValueError('Original complete 60-file M28 archive is required')
    for row in manifest['files']:
        relative=Path(row['path'])
        if relative.is_absolute() or '..' in relative.parts or relative.parts[0]!='notes':
            raise ValueError('The original manifest is not topic relative')
        source=input_topic/relative
        if source.stat().st_size!=row['bytes'] or sha(source)!=row['sha256']:
            raise ValueError('Original immutable M28 file differs: '+row['path'])
    if sha(input_topic/'notes'/READY)!=READY_SHA:
        raise ValueError('The genuine already constructed M28 ready record is missing or changed')
    origin=read(input_source/'source-origin.json')
    if origin.get('source_revision')!=PINNED_REV or origin.get('manifest_sha256')!=PINNED_MANIFEST:
        raise ValueError('The exact 91-file physical source origin is required')
    overlays={}
    for entry in a.overlay_source:
        name,separator,value=entry.partition('=')
        if not separator or name not in OWN or name in overlays:
            raise ValueError('Overlay only one explicitly pinned own Python source per name')
        file=Path(value).resolve(strict=True)
        if sha(file)!=OWN[name]:raise ValueError('Prepared source overlay hash differs: '+name)
        overlays[name]=file
    # Preserve this exact executed Python launcher in the real-file snapshot
    # as well. It participates in the later complete-Python cache namespace.
    if Path(__file__).name!='strong_sameg_m28_cache_snapshot.py':
        raise ValueError('Restore the launcher under its recorded module basename')
    overlays[Path(__file__).name]=Path(__file__).resolve(strict=True)
    # Nothing above mutates any input or creates a numerical process.
    topic=work/'runtime'/'topics'/TOPIC_NAME
    comp=topic/'computations';notes=topic/'notes';physical=work/'physical-source'
    work.mkdir(parents=True);notes.mkdir(parents=True)
    sources=copy_tree_real(input_topic/'computations',comp,a.max_source_bytes)
    physical_sources=copy_tree_real(input_source,physical,a.max_source_bytes)
    for name,file in overlays.items():
        target=comp/name
        if target.exists():target.unlink()
        shutil.copyfile(file,target)
    for name,file in overlays.items():
        rows=[row for row in sources['files'] if row['path']==name]
        replacement=dict(path=name,bytes=(comp/name).stat().st_size,sha256=sha(comp/name),
            explicit_overlay_source=str(file))
        if rows:
            replacement['pre_overlay_sha256']=rows[0]['sha256']
            sources['files'][sources['files'].index(rows[0])]=replacement
        else:sources['files'].append(replacement)
    sources['bytes']=sum(row['bytes'] for row in sources['files'])
    for name,expected in OWN.items():
        if sha(comp/name)!=expected:raise ValueError('Required own source differs: '+name)
        ast.parse((comp/name).read_text(),filename=str(comp/name))
    # Notes are outside all engine source trees. Nonselected old notes are
    # read-only input links; every complete M28 archive member is a real copy.
    skipped_input_links=[]
    for entry in (input_topic/'notes').iterdir():
        try:resolved=entry.resolve(strict=True)
        except FileNotFoundError:
            skipped_input_links.append(entry.name)
            continue
        (notes/entry.name).symlink_to(resolved,target_is_directory=entry.is_dir())
    copied=[]
    for row in manifest['files']:
        copied.append(checked_copy(input_topic/row['path'],topic/row['path'],row['sha256']))
    copied.append(checked_copy(manifest_file,notes/manifest_file.name,MANIFEST_SHA))
    copied.append(checked_copy(input_topic/'notes'/READY,notes/READY,READY_SHA))
    copied.append(checked_copy(input_topic/'notes'/LEDGER,notes/LEDGER))
    spectral=read(notes/(STEM+'-actual28-spectral-plan.json'))
    # The fixed24 metadata deliberately retains original M24 raw/physical
    # coefficient basenames. Preserve those exact indirect primaries too,
    # instead of relying only on links into an older runtime.
    indirect=[spectral[key] for key in ('fixed_reference','fixed_raw',
        'fixed_view_report','warm_tail','baseline_config')]
    indirect.extend(spectral['raw_pieces']);indirect.extend(spectral['physical_pieces'])
    copied_paths={row['path'] for row in copied}
    for item in indirect:
        name=Path(item['file']).name
        source=input_topic/'notes'/name;target=notes/name
        if target.is_file() and not target.is_symlink():
            if sha(target)!=item['sha256']:
                raise ValueError('An existing copied indirect primary differs: '+name)
            continue
        row=checked_copy(source,target,item['sha256'])
        if row['path'] not in copied_paths:
            copied.append(row);copied_paths.add(row['path'])
    for name,expected in spectral['source_sha256'].items():
        if Path(name).name!=name or sha(comp/name)!=expected:
            raise ValueError('Original spectral mathematical source differs: '+name)
    current={f.name:sha(f) for f in sorted(comp.glob('*.mjs'))}
    if current!=spectral['MJS_source_sha256']:
        raise ValueError('Original complete MJS map differs')
    for root in (comp,physical):
        if any(f.is_symlink() for f in root.rglob('*')):
            raise ValueError('A source snapshot still contains a symlink')
    prefix=notes/('2026-11-13-strong-q096-sameg-m28-'+a.run_label)
    if any(notes.glob(prefix.name+'*')):
        raise FileExistsError('The new diagnostic output prefix is not fresh')
    # Keep the supplied virtualenv entry path: resolving its interpreter symlink
    # would silently select the system Python and lose the recorded dependencies.
    interpreter=a.python.absolute()
    if not interpreter.is_file() or not os.access(interpreter,os.X_OK):
        raise FileNotFoundError('The explicit recorded Python entry is not executable')
    py=str(interpreter)
    rel=lambda suffix:'notes/'+STEM+suffix
    child=[py,'-u','computations/strong_sameg_m28_cached_audit.py',
        '--accepted-raw',rel('-actual28-raw-collocation.json.gz'),
        '--original-spectral-plan',rel('-actual28-spectral-plan.json'),
        '--node-young-space','4','--raw',rel('-actual28-outer-00-raw-collocation.json.gz'),
        '--config',rel('-actual28-config.json'),'--warm',rel('-actual28-tail-response_0002.json.gz'),
        '--source-topic',str(physical),'--out-prefix',str(prefix),
        '--node-heap','96','--storage','frozen','--point-cache-limit','8',
        '--reference-adapter','notes/'+READY,'--calibration-ledger','notes/'+LEDGER,
        '--cache-directory',str(work/'exact-stage-m28'),
        '--seed-prefix',str(prefix)+'-seed','--diagnostic-complete-evaluate']
    supervisor=[py,'-u','computations/strong_observed_foreground_resource_run.py',
        '--memory-observations',str(prefix)+'-memory.jsonl',
        '--out',str(prefix)+'-resource.json','--heartbeat',str(prefix)+'-heartbeat.json',
        '--ownership',str(prefix)+'-ownership.json','--task-prefix',prefix.name,
        '--heartbeat-seconds','20','--',*child]
    record=dict(scope=__doc__,source_sha256=SELF_SHA,prepared=True,executed=False,
        old_M28_solver_repeated=False,prefix_Newton_calls=0,
        original_60_file_archive_manifest_sha256=MANIFEST_SHA,
        true_M28_ready_sha256=READY_SHA,all_original_MJS_bytes_identical=True,
        original_spectral_sources_checked=True,copied_primary_files=copied,
        computation_snapshot=sources,physical_snapshot=physical_sources,
        prepared_source_overlays={name:dict(file=str(file),sha256=sha(file)) for name,file in overlays.items()},
        effective_own_sources={name:sha(comp/name) for name in OWN},
        source_snapshot_has_no_symlinks=True,notes_links_are_inputs_only=True,
        skipped_unresolvable_nonprimary_note_links=skipped_input_links,
        cache_uses_new_runtime_identity=True,old_M24_cache_reused=False,
        prepare_command=[*child,'--prepare-only'],diagnostic_supervisor_command=supervisor,
        cwd=str(topic),stdout=str(prefix)+'-stdout.log',
        existing_r4_terminal_must_be_inspected_separately=True,
        cgroup_counters_do_not_assign_a_death_cause=True,
        following_steps='After diagnostic, run a fresh normal cached audit using the saved exact seed; then strong_sameg_m28_complete.py invokes the unchanged zero-Newton postprocessor and verifies the full original spectral provenance before all original geometric audits.',
        numeric_scope='This preparation is not a stage equivalence or a full audit result.')
    write_new(work/'snapshot-plan.json',record)
    print(json.dumps(dict(event='M28_real_file_snapshot_prepared',
        plan=str(work/'snapshot-plan.json'),cwd=str(topic),
        old_M28_Newton_repeated=False,execute_diagnostic_requested=a.execute_diagnostic)),flush=True)
    if not a.execute_diagnostic:return
    # No other resident launcher is retained. The original owned supervisor
    # records true wait4 status and signals. An old job is never classified
    # from cross-process-namespace observations by this file.
    env=dict(os.environ)
    for key in tuple(env):
        if key in ('GH_TOKEN','GITHUB_TOKEN','GITHUB_PAT','GITHUB_ACCESS_TOKEN',
                   'GH_ENTERPRISE_TOKEN','GIT_TOKEN','GIT_ASKPASS','SSH_ASKPASS','SSH_AUTH_SOCK') or key.startswith('GIT_CONFIG_'):
            env.pop(key,None)
    for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
        env[key]='1'
    temp=work/'temporary';temp.mkdir();env['TMPDIR']=str(temp)
    os.chdir(topic)
    with Path(str(prefix)+'-stdout.log').open('x') as log:
        os.dup2(log.fileno(),1);os.dup2(log.fileno(),2)
    os.execve(py,supervisor,env)


if __name__=='__main__':main()
