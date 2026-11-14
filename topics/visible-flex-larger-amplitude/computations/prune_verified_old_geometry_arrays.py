#!/usr/bin/env python3
"""Remove only the 352 old derived arrays explicitly approved by root.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
All hashes, exact paths, original regeneration commands and resource identities
are written before deletion. Current q122 fields, every actual accepted input,
all metadata and all continuous-mean certificate inputs remain untouched.
"""
import hashlib
import json
from pathlib import Path
import re
import shutil


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):return json.loads(Path(path).read_text())


def main():
    root=Path(__file__).resolve().parent.parent
    out=root/'old-derived-array-cleanup-r1'
    if out.exists():raise FileExistsError('Fresh approved cleanup record required')
    fields=[];arrays=[]
    for name in ('m28-q096-r1','m28-q098-r1','m28-q106-r1'):
        folder=root/name;covered=set()
        for manifest in sorted(folder.glob('*-field.json')):
            data=read(manifest)
            if data['schema']!='complete-geometry-chunks-v1' or not data['complete']:
                raise ValueError('Only a complete original field manifest is eligible')
            resource=folder/(manifest.name[:-len('-field.json')]+'-resource.json')
            usage=read(resource)
            if usage['exitcode']!=0 or not isinstance(usage['command'],list):
                raise ValueError('The actual completed regeneration command is missing')
            index=len(fields)
            fields.append(dict(manifest=str(manifest),manifest_sha256=sha(manifest),
                resource=str(resource),resource_sha256=sha(resource),
                original_owned_resource=usage,complete_shape=data['shape']))
            for item in data['chunks']:
                if not re.fullmatch(r'.+-field-part\d{3}\.npy\.gz',item['file']):
                    raise ValueError('Only the explicitly reviewed old derived chunk names are eligible')
                path=folder/item['file']
                if path.is_symlink() or path in covered or not path.is_file():
                    raise ValueError('Unexpected old derived array path')
                stat=path.stat()
                if stat.st_size!=item['bytes'] or sha(path)!=item['sha256']:
                    raise ValueError('An old derived array no longer matches its complete manifest')
                arrays.append(dict(path=str(path),sha256=item['sha256'],bytes=stat.st_size,
                    link_count=stat.st_nlink,field_index=index,coverage=[item['start'],item['end']]))
                covered.add(path)
        if covered!=set(folder.glob('*-field-part*.npy.gz')):
            raise ValueError('An extra unreviewed old array exists')
    if len(arrays)!=352 or sum(a['bytes'] for a in arrays)!=510450868 or len(fields)!=28:
        raise ValueError('The exact approved path and byte inventory changed')
    before=shutil.disk_usage(root)
    inventory=dict(schema='approved-old-derived-geometry-array-cleanup-inventory-v1',
        source_sha256=sha(__file__),authorization='Root explicitly approved only these 352 verified old derived arrays, total 510450868 bytes, in the active collaboration.',
        fields=fields,arrays=arrays,array_count=len(arrays),total_bytes=sum(a['bytes'] for a in arrays),
        all_complete_manifest_hashes_verified_before_deletion=True,
        original_accepted_raw_source_metadata_current_fields_and_certificates_not_targeted=True,
        regeneration='Use each original resource command with a fresh consistent output prefix, retaining its pinned accepted inputs, original complete grid, mean and geometric parameters. No ODE/Jacobian is required.',
        observed_disk_free_before=before.free)
    out.mkdir();ip=out/'inventory.json';ip.write_text(json.dumps(inventory,indent=2)+'\n')
    deleted=[]
    for item in arrays:
        path=Path(item['path'])
        if path.is_symlink() or sha(path)!=item['sha256']:
            raise ValueError('A reviewed array changed between inventory and deletion')
        path.unlink();deleted.append(item['path'])
    for f in fields:
        if sha(f['manifest'])!=f['manifest_sha256'] or sha(f['resource'])!=f['resource_sha256']:
            raise ValueError('An original field manifest or resource changed during cleanup')
    after=shutil.disk_usage(root)
    result=dict(schema='approved-old-derived-geometry-array-cleanup-result-v1',
        source_sha256=sha(__file__),inventory=str(ip),inventory_sha256=sha(ip),
        deleted_count=len(deleted),deleted_logical_bytes=sum(a['bytes'] for a in arrays),
        all_listed_arrays_absent=all(not Path(p).exists() for p in deleted),
        all_original_manifests_and_resource_records_unchanged=True,
        current_fields_and_original_scientific_inputs_not_touched=True,
        observed_disk_free_before=before.free,observed_disk_free_after=after.free,
        concurrent_other_disk_activity_not_excluded=True)
    rp=out/'result.json';rp.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(result=str(rp),sha256=sha(rp),deleted_count=len(deleted),
        deleted_bytes=result['deleted_logical_bytes'],disk_free_after=after.free)),flush=True)


if __name__=='__main__':main()
