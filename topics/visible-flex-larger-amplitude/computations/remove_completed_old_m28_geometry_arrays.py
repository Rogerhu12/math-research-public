#!/usr/bin/env python3
"""Remove only SHA-verified regenerable arrays from the completed old17 fields.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Explicit root authorization: reclaim the old M28 q122 geometry arrays, retain
all metadata, actual raw inputs, fullflow/response arrays and the true current
A baseline. A complete inventory and reproduction commands precede deletion.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import time


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):return json.loads(Path(path).read_text())
def owned_wait4(record):
    root=Path(__file__).resolve().parent
    old='bbf6c8ac8cb32cbc0f5c1e1c1c1e110ca1744c7839de0f272c172837a4ba3f59'
    new='e683fbbeb1eb579d07799acbdd08b2254917e49209566c28a85628eb9cb72bc6'
    digest=record.get('resource_wrapper_sha256')
    if digest==old:
        return sha(root/'strong_resource_run.py')==old
    if digest==new:
        return sha(root/'strong_foreground_resource_run.py')==new and record.get('wait4_observed') is True
    return False
def write(path,data):
    with Path(path).open('x') as out:
        out.write(json.dumps(data,indent=2)+'\n');out.flush();os.fsync(out.fileno())


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--old-plan',type=Path,required=True)
    p.add_argument('--current-plan',type=Path,required=True)
    p.add_argument('--out-directory',type=Path,required=True)
    a=p.parse_args()
    old=read(a.old_plan);current=read(a.current_plan)
    if sha(a.old_plan)!='0bfc0774122aa74cb10b242ffb964ef57db7e81526a56382f1333ca615f63ff1':
        raise ValueError('Only the completed frozen old17 plan is authorized')
    if sha(a.current_plan)!='3687c4d2fb65319981091f17723d05ccd75442967284996e1cc8ac98874fd7a8':
        raise ValueError('The true current A baseline plan changed')
    if old['modes']!=28 or len(old['candidates'])!=17 or current['modes']!=32 or not current['baseline_only']:
        raise ValueError('Keep the actual old/new scientific objects distinct')
    if Path.cwd()!=Path(old['cwd']) or Path.cwd()!=Path(current['cwd']):
        raise ValueError('Preserve the original reproducible cwd')
    a.out_directory.mkdir(parents=True,exist_ok=True)
    inventory_path=a.out_directory/'inventory.json';result_path=a.out_directory/'result.json'
    if inventory_path.exists() or result_path.exists():raise FileExistsError('A fresh cleanup record is required')
    old_root=a.old_plan.parent.resolve();new_dependencies=set()
    for path,digest in current['source_and_input_sha256'].items():
        if sha(path)!=digest:raise ValueError('A real current input changed: '+path)
        new_dependencies.add(Path(path).resolve())
    current_files=[]
    for row in current['candidates']:
        for key in ('report','field','resource'):
            path=Path(row[key]);new_dependencies.add(path.resolve());current_files.append(dict(path=str(path),sha256=sha(path)))
        m=read(row['field']);owned=read(row['resource'])
        if owned['exitcode']!=0 or not owned_wait4(owned) or not m['complete']:
            raise ValueError('The completed real A baseline must be preserved')
        for chunk in m['chunks']:
            path=Path(row['field']).with_name(chunk['file'])
            if sha(path)!=chunk['sha256']:raise ValueError('A new current baseline chunk changed')
            new_dependencies.add(path.resolve());current_files.append(dict(path=str(path),sha256=chunk['sha256']))
    files=[];rows=[];seen=set()
    for row in old['candidates']:
        owned,screen,manifest=(read(row[key]) for key in ('resource','report','field'))
        if (owned['exitcode']!=0 or not owned_wait4(owned) or owned['termination_signal'] is not None or
                not screen['finished'] or not screen['finite_domain_passed'] or screen['worker_start_attempts']!=0 or
                screen['nonlinear_solution'] or manifest!=screen['geometry_fields']['storage'] or
                not manifest['complete'] or sha(row['field'])!=screen['geometry_fields']['sha256'] or
                owned['command']!=row['command'][row['command'].index('--')+1:]):
            raise ValueError('Every old field must have its original complete successful outcome')
        cursor=0
        for item in manifest['chunks']:
            path=Path(row['field']).with_name(item['file']);actual=path.resolve()
            if (actual.parent!=old_root or actual in new_dependencies or actual in seen or
                    not path.name.endswith('.npy.gz') or '-field-part' not in path.name or
                    item['start']!=cursor or not cursor<item['end']<=manifest['shape'][0]):
                raise ValueError('Only the exact old derived field chunks are authorized')
            stat=path.stat()
            if stat.st_size!=item['bytes'] or sha(path)!=item['sha256']:
                raise ValueError('An old derived array changed or is already absent: '+str(path))
            seen.add(actual);cursor=item['end']
            files.append(dict(path=str(path),absolute_path=str(actual),sha256=item['sha256'],
                bytes=stat.st_size,allocated_bytes=stat.st_blocks*512,field=row['name'],start=item['start'],end=item['end']))
        if cursor!=manifest['shape'][0]:raise ValueError('An old field does not have complete radial coverage')
        rows.append(dict(name=row['name'],original_command=row['command'],
            owned_resource=dict(path=row['resource'],sha256=sha(row['resource']),exitcode=0,
                wall_seconds=owned['wall_seconds'],peak_rss_kib=owned['peak_rss_kib']),
            report=dict(path=row['report'],sha256=sha(row['report'])),
            complete_field_manifest=dict(path=row['field'],sha256=sha(row['field'])),
            shape=manifest['shape']))
    if len(files)!=306 or sum(item['bytes'] for item in files)!=451_721_535:
        raise ValueError('The authorized complete17 derived-array inventory differs')
    before=os.statvfs(Path.cwd());available_before=before.f_bavail*before.f_frsize
    inventory=dict(schema='authorized-completed-old17-derived-geometry-removal-inventory-v1',
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),
        authorization='Root message: reclaim the completed old17 M28 q122 derived fields after exact SHA/recipe/resource verification; preserve actual inputs and current A baseline.',
        original_plan=dict(path=str(a.old_plan),sha256=sha(a.old_plan)),
        original_owned_wait4_contracts={name:sha(Path(__file__).with_name(name)) for name in ('strong_resource_run.py','strong_foreground_resource_run.py')},
        actual_current_plan=dict(path=str(a.current_plan),sha256=sha(a.current_plan)),cwd=str(Path.cwd()),
        old_completed_fields=rows,files=files,total_files=len(files),
        total_logical_bytes=sum(item['bytes'] for item in files),total_allocated_bytes=sum(item['allocated_bytes'] for item in files),
        all_expected_original_chunks_read_and_hashed=True,
        no_current_plan_dependency_intersects_deleted_arrays=True,preserved_current_baseline_files=current_files,
        retained_all_old_metadata_sources_and_commands=True,
        retained_actual_raw_fullflow_and_full_half_response_arrays=True,
        retained_Awarm_and_Bwarm_Cartesian_arrays=True,
        reproduction='Use each saved original command in the original cwd with the original inputs/source hashes and explicit fresh resource/log output paths. The scientific output chunk bytes are verified against this inventory. No geometry model or source is changed by deletion.',
        filesystem_available_bytes_before=available_before,
        created_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()))
    write(inventory_path,inventory)
    removed=[]
    journal=a.out_directory/'removed.jsonl'
    with journal.open('x') as out:
        for item in files:
            path=Path(item['path'])
            if path.stat().st_size!=item['bytes'] or sha(path)!=item['sha256']:
                raise ValueError('An authorized chunk changed after inventory persistence')
            path.unlink();removed.append(item['path'])
            out.write(json.dumps(dict(path=item['path'],sha256=item['sha256'],bytes=item['bytes']))+'\n')
            out.flush()
        os.fsync(out.fileno())
    for item in current_files:
        if sha(item['path'])!=item['sha256']:raise ValueError('A current baseline file changed during old-array cleanup')
    after=os.statvfs(Path.cwd());available_after=after.f_bavail*after.f_frsize
    result=dict(schema='authorized-completed-old17-derived-geometry-removal-result-v1',
        source_sha256=sha(__file__),inventory_sha256=sha(inventory_path),journal_sha256=sha(journal),
        all_authorized_arrays_removed=True,removed_files=len(removed),
        removed_logical_bytes=inventory['total_logical_bytes'],removed_allocated_bytes=inventory['total_allocated_bytes'],
        current_baseline_rehashed_unchanged=True,old_metadata_raw_fullflow_response_and_point_arrays_retained=True,
        filesystem_available_bytes_before=available_before,filesystem_available_bytes_after=available_after,
        filesystem_available_change_includes_other_concurrent_jobs=True,
        finished_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),new_mathematical_or_numerical_result_claimed=False)
    write(result_path,result)
    print(json.dumps(dict(event='old_completed17_derived_arrays_removed',result=str(result_path),sha256=sha(result_path),
        removed=len(removed),logical_bytes=result['removed_logical_bytes'],allocated_bytes=result['removed_allocated_bytes'],free_after=available_after)),flush=True)


if __name__=='__main__':main()
